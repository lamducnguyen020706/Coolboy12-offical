"""Pipeline orchestration.

    parse args -> validate ID -> resolve repo root -> load config
      -> SYNCHRONIZE with origin/<branch> and capture the audit snapshot
      -> resolve Roadmap row and target scope        (post-sync)
      -> resolve the complete Source Set             (post-sync)
      -> collect git state and regression baseline
      -> verify the snapshot did not drift
      -> Luna audit call -> validate report -> write auditreport.md
      -> Luna patch-prompt call (EVERY verdict) -> validate -> write patchprompt.md
      -> pre-commit self-check -> stage exactly two files -> commit -> push

Synchronization comes first and nothing is read before it: the remote branch
carries the latest committed artifact, so auditing local state unchecked
risks judging a superseded copy and blaming the artifact for it. Every source
in one run is read at one commit, and the run is refused if the repository
moves underneath it.

The runner is not the auditor and not the implementation agent. It decides
no architectural truth, no severity and no verdict: it resolves evidence,
bounds the context, and validates the shape of what comes back.

Both outputs are refreshed on every successful run. A patchprompt is never
conditional on the verdict — PASS and BLOCKED get their own contracts.
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from pathlib import Path

from . import artifact_id as artifact_id_module
from . import (
    config,
    gitops,
    gitstate,
    outputs,
    patchcheck,
    prompts,
    repo,
    sync,
    verdict,
)
from .errors import (
    EXIT_SUCCESS,
    InvalidAuditResponse,
    PatchGenerationFailure,
    RunnerError,
)
from .luna_client import call_luna as default_call_luna
from .sources import SourceResolver

TOTAL_STEPS = 9

LunaFn = Callable[[config.HhtechConfig, str, str], str]

_HELP_TEXT = """\
usage: audit <artifact-id>

Runs the HHTECH audit pipeline for a single COOLBOY12 Roadmap artifact:

  0. Synchronizes with origin/<current branch> BEFORE reading anything, so
     the audit never judges a superseded local copy of the artifact. Fetch
     is non-destructive; only a provably safe fast-forward is performed.
     Local-ahead, diverged history, and a fast-forward that would overwrite
     uncommitted work all fail closed, untouched, with a named reason.
  1. Resolves the artifact's Roadmap row and its complete declared scope.
  2. Resolves the Source Set — Blueprint, RMS, Roadmap, both HHTECH
     standards, CLAUDE.md, the Spine, invariant and anti-ordering registers,
     declared and referenced sections, dependency and neighbour context.
  3. Reads repository state and the committed baseline of the target files.
  4. Calls GPT-5.6 Luna (HHTECH) to produce hhtech/auditreport.md.
  5. Calls Luna again to produce hhtech/patchprompt.md — on EVERY verdict.
  6. Commits and pushes exactly those two files to the current branch.

<artifact-id> is a Roadmap artifact number, 1-490 (e.g. "042" or "42").
Exactly one artifact ID is accepted.

Every run overwrites both outputs:

  PASS            patchprompt states NO PATCH REQUIRED
  BLOCKED         patchprompt states DO NOT PATCH, names the evidence gap,
                  and requires ./hhtech/audit <ID> to be re-run
  PATCH REQUIRED  patchprompt contains actionable patch instructions

The runner is orchestration only: it never patches the audited artifact and
never commits or pushes anything but its own two outputs.

Environment:
  HHTECH_API_KEY   required; the HHTECH bearer credential. Never printed,
                   never logged, never written to any output file.

Exit codes:
  0  pipeline completed — outputs committed and pushed
  1  user / input / configuration error
  2  HHTECH / API failure
  3  audit response invalid
  4  patch prompt generation failure
  5  git / staging / commit / push safety failure
  6  remote synchronization failure — a runner/infrastructure failure, never
     a statement about the artifact; no audit was run
"""


def _progress(n: int, label: str) -> None:
    print(f"[{n}/{TOTAL_STEPS}] {label}")


def _self_check(
    hhtech_dir: Path, artifact_id: str, verdict_value: str, api_key: str
) -> None:
    """Pre-commit consistency check against what actually landed on disk."""
    report_path = hhtech_dir / outputs.AUDIT_REPORT_NAME
    patch_path = hhtech_dir / outputs.PATCH_PROMPT_NAME

    if not report_path.is_file():
        raise InvalidAuditResponse("auditreport.md does not exist after writing")
    if not patch_path.is_file():
        raise PatchGenerationFailure("patchprompt.md does not exist after writing")

    report_text = report_path.read_text(encoding="utf-8")
    result = verdict.extract_verdict(report_text, api_key=api_key)
    verdict.validate_artifact_identity(report_text, artifact_id)
    if result.verdict != verdict_value:
        raise InvalidAuditResponse(
            f"auditreport.md on disk carries verdict {result.verdict!r} but the "
            f"run produced {verdict_value!r}; refusing to commit an inconsistent pair"
        )

    patch_text = patch_path.read_text(encoding="utf-8")
    patchcheck.validate_patch_prompt(patch_text, artifact_id, verdict_value, api_key=api_key)


def _report_success(
    artifact_id: str,
    verdict_value: str,
    commit_hash: str | None,
    snapshot: sync.AuditSnapshot,
    sync_result: sync.SyncResult,
    pushed: bool,
) -> None:
    print()
    print(f"Artifact:          {artifact_id}")
    print(f"Verdict:           {verdict_value}")
    print(f"Synchronization:   {sync_result.relation} — {sync_result.action}")
    print(f"Audited HEAD:      {snapshot.head}")
    print(f"Audit report:      {outputs.AUDIT_REPORT_REL}")
    print(f"Patch prompt:      {outputs.PATCH_PROMPT_REL}")
    print(f"Commit hash:       {commit_hash or '(nothing to commit — outputs unchanged)'}")
    print(f"Branch:            {snapshot.branch}")
    print(f"Push:              {'SUCCESS' if pushed else 'SKIPPED (nothing to commit)'}")


def main(
    argv: list[str],
    *,
    luna: LunaFn | None = None,
    repo_root: Path | None = None,
) -> int:
    """Run one audit. `repo_root` is an explicit override for tests and for
    auditing a different checkout; it is never taken from the process CWD."""
    if argv in (["--help"], ["-h"]):
        print(_HELP_TEXT)
        return EXIT_SUCCESS

    luna_call: LunaFn = luna if luna is not None else default_call_luna

    try:
        artifact_id = artifact_id_module.parse_single_argument(argv)
        _progress(1, f"Validating artifact {artifact_id}")

        root = repo_root if repo_root is not None else repo.find_repo_root()
        cfg = config.load_config()

        # Synchronization comes first: the remote branch is the source of the
        # latest committed artifact, so nothing may be read from disk until
        # the working tree provably matches it.
        _progress(2, "Synchronizing with the remote branch")
        sync_result = sync.synchronize(root)
        snapshot = sync.capture_snapshot(root, sync_result)
        print(
            f"      branch {sync_result.branch} · {sync_result.relation} · "
            f"{sync_result.action} · HEAD {snapshot.head[:12]}"
        )

        _progress(3, "Resolving Roadmap scope (post-sync)")
        resolver = SourceResolver(root)

        _progress(4, "Resolving source set (post-sync)")
        resolution = resolver.resolve(artifact_id)

        _progress(5, "Collecting repository state")
        git_state = gitstate.collect_git_state(
            root, tuple(f.path for f in resolution.scope.files)
        )
        # Fail closed before spending a paid call on a run that could never
        # legally commit: the runner may only ever commit its own two paths.
        gitops.assert_index_committable(root)

        # One coherent state: every source above was read at this commit, and
        # the audit is refused if the repository moved underneath it.
        snapshot.verify_unchanged(root)

        _progress(6, "Running GPT-5.6 Luna audit")
        audit_response = luna_call(
            cfg,
            prompts.AUDIT_SYSTEM_PROMPT,
            prompts.build_audit_user_content(resolution, git_state, snapshot),
        )
        audit_result = verdict.extract_verdict(audit_response, api_key=cfg.api_key)
        verdict.validate_artifact_identity(audit_result.text, artifact_id)

        hhtech_dir = root / "hhtech"

        _progress(7, f"Writing auditreport.md (verdict: {audit_result.verdict})")
        outputs.write_audit_report(hhtech_dir, audit_result.text)

        # Every verdict gets a fresh patchprompt. The contract differs by
        # verdict; the existence of the file does not.
        _progress(8, "Generating patchprompt.md")
        patch_response = luna_call(
            cfg,
            prompts.PATCH_PROMPT_SYSTEM_PROMPT,
            prompts.build_patch_prompt_user_content(
                resolution, git_state, audit_result.text, audit_result.verdict
            ),
        )
        patchcheck.validate_patch_prompt(
            patch_response, artifact_id, audit_result.verdict, api_key=cfg.api_key
        )
        outputs.write_patch_prompt(hhtech_dir, patch_response)

        _self_check(hhtech_dir, artifact_id, audit_result.verdict, cfg.api_key)

        _progress(9, "Commit + push")
        gitops.stage_outputs(root)
        gitops.validate_staged(root)
        commit_hash = gitops.commit(root, gitops.build_commit_message(artifact_id))
        pushed = False
        if commit_hash is not None:
            gitops.push_current_branch(root, snapshot.branch)
            pushed = True

        _report_success(
            artifact_id, audit_result.verdict, commit_hash, snapshot, sync_result, pushed
        )
        return EXIT_SUCCESS

    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return exc.exit_code


def run() -> int:
    return main(sys.argv[1:])
