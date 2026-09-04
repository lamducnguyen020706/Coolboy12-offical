"""Pipeline orchestration. BUILD spec §42.

This module is the runner's `main()` and implements the exact required call
order. It is orchestration only: it collects inputs and invokes Luna under
hhtech/standards/audit-standard.md and hhtech/standards/patch-standard.md.
It decides no architectural truth, no finding severity, no verdict (BUILD
spec §43).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Optional

from . import artifact_id, config, gitops, gitstate, outputs, patchcheck, prompts, repo, roadmap, sources, verdict
from .errors import EXIT_SUCCESS, InvalidAuditResponse, PatchGenerationFailure, RunnerError
from .luna_client import call_luna as default_call_luna

BLUEPRINT_PATH = "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md"
RMS_PATH = "docs/sources/COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md"
ROADMAP_PATH = "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"
AUDIT_STANDARD_PATH = "hhtech/standards/audit-standard.md"
PATCH_STANDARD_PATH = "hhtech/standards/patch-standard.md"

TOTAL_STEPS = 8

LunaFn = Callable[[config.HhtechConfig, str, str], str]

_HELP_TEXT = """\
usage: audit <artifact-id>

Runs the HHTECH audit pipeline for a single COOLBOY12 Roadmap artifact:
  1. Collects Blueprint / RMS / Roadmap / target-file / git-state context
     for <artifact-id>.
  2. Calls GPT-5.6 Luna (HHTECH) to produce hhtech/auditreport.md.
  3. If the verdict is PATCH REQUIRED, calls Luna a second time to produce
     hhtech/patchprompt.md; otherwise clears hhtech/patchprompt.md.
  4. Commits and pushes exactly those two files to the current branch.

<artifact-id> is a Roadmap artifact number, 1-490 (e.g. "042" or "42").
Exactly one artifact ID is accepted.

The runner is orchestration only. It is not the auditor and not the
implementation agent: it does not patch the audited artifact and does not
commit or push anything other than hhtech/auditreport.md and
hhtech/patchprompt.md.

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
"""


def _progress(n: int, label: str) -> None:
    print(f"[{n}/{TOTAL_STEPS}] {label}")


def _validate_output_files(
    hhtech_dir: Path, artifact: str, verdict_value: str, api_key: str
) -> None:
    """Re-read what actually landed on disk and validate contract shape
    only, per BUILD spec §34. Never validates Luna's semantic content.
    """
    report_path = hhtech_dir / outputs.AUDIT_REPORT_NAME
    report_text = report_path.read_text(encoding="utf-8")
    if not report_text.strip():
        raise InvalidAuditResponse("auditreport.md is empty after writing")
    if api_key and api_key in report_text:
        raise InvalidAuditResponse("auditreport.md contains the HHTECH API key")
    verdict.extract_verdict(report_text)
    verdict.validate_artifact_identity(report_text, artifact)

    patch_path = hhtech_dir / outputs.PATCH_PROMPT_NAME
    patch_text = patch_path.read_text(encoding="utf-8")
    if not patch_text.strip():
        raise PatchGenerationFailure("patchprompt.md is empty after writing")
    if api_key and api_key in patch_text:
        raise PatchGenerationFailure("patchprompt.md contains the HHTECH API key")

    if verdict_value == "PATCH REQUIRED":
        if outputs.is_cleared_patch_prompt(patch_text):
            raise PatchGenerationFailure(
                "patchprompt.md was not actually written for a PATCH REQUIRED verdict"
            )
        patchcheck.validate_patch_prompt(patch_text, artifact, api_key=api_key)
    else:
        if not outputs.is_cleared_patch_prompt(patch_text):
            raise InvalidAuditResponse(
                "patchprompt.md is not cleared even though the verdict was not "
                "PATCH REQUIRED — refusing to commit stale patch content"
            )


def _report_success(
    artifact: str,
    verdict_value: str,
    commit_hash: Optional[str],
    branch: str,
) -> None:
    patch_prompt_status = (
        f"hhtech/{outputs.PATCH_PROMPT_NAME}"
        if verdict_value == "PATCH REQUIRED"
        else "cleared"
    )
    print("")
    print(f"Artifact:          {artifact}")
    print(f"Verdict:           {verdict_value}")
    print(f"Audit report path: hhtech/{outputs.AUDIT_REPORT_NAME}")
    print(f"Patch prompt path: {patch_prompt_status}")
    print(f"Commit hash:       {commit_hash or '(nothing to commit — outputs unchanged)'}")
    print(f"Branch:            {branch}")
    print(f"Push:              {'SUCCESS' if commit_hash else 'SKIPPED (nothing to commit)'}")


def main(argv: list[str], *, luna: Optional[LunaFn] = None) -> int:
    if argv in (["--help"], ["-h"]):
        print(_HELP_TEXT)
        return EXIT_SUCCESS

    luna_call: LunaFn = luna if luna is not None else default_call_luna

    try:
        artifact = artifact_id.parse_single_argument(argv)
        _progress(1, f"Validating artifact {artifact}")

        repo_root = repo.find_repo_root(Path.cwd())
        cfg = config.load_config()

        _progress(2, "Loading Roadmap scope")
        roadmap_text = (repo_root / ROADMAP_PATH).read_text(encoding="utf-8")
        row = roadmap.find_manifest_row(roadmap_text, artifact)
        scope = roadmap.derive_target_scope(repo_root, row)

        _progress(3, "Collecting source context")
        source_bundle = sources.collect_sources(
            repo_root,
            row,
            scope.matched_files,
            repo_root / BLUEPRINT_PATH,
            repo_root / RMS_PATH,
            repo_root / AUDIT_STANDARD_PATH,
            repo_root / PATCH_STANDARD_PATH,
        )
        dependency_context = sources.collect_dependency_context(
            repo_root, roadmap_text, row.get("H")
        )

        _progress(4, "Collecting repository state")
        git_state = gitstate.collect_git_state(repo_root)

        _progress(5, "Running GPT-5.6 Luna audit")
        audit_user_content = prompts.build_audit_user_content(
            artifact, row, scope, source_bundle, git_state, dependency_context
        )
        audit_response = luna_call(cfg, prompts.AUDIT_SYSTEM_PROMPT, audit_user_content)
        audit_result = verdict.extract_verdict(audit_response, api_key=cfg.api_key)
        verdict.validate_artifact_identity(audit_result.text, artifact)

        hhtech_dir = repo_root / "hhtech"

        _progress(6, "Writing auditreport.md")
        outputs.write_audit_report(hhtech_dir, audit_result.text)

        if audit_result.verdict == "PATCH REQUIRED":
            _progress(7, "Generating patchprompt.md")
            patch_user_content = prompts.build_patch_prompt_user_content(
                artifact, row, scope, source_bundle, git_state, audit_result.text
            )
            # A second-call failure must NOT touch patchprompt.md and must
            # NOT commit/push — auditreport.md may remain as the valid
            # result of the (already-succeeded) first call (BUILD spec §24).
            patch_response = luna_call(cfg, prompts.PATCH_PROMPT_SYSTEM_PROMPT, patch_user_content)
            patchcheck.validate_patch_prompt(patch_response, artifact, api_key=cfg.api_key)
            outputs.write_patch_prompt(hhtech_dir, patch_response)
        else:
            _progress(7, "Clearing patchprompt.md")
            outputs.clear_patch_prompt(hhtech_dir)

        _validate_output_files(hhtech_dir, artifact, audit_result.verdict, cfg.api_key)

        _progress(8, "Commit + push")
        baseline_staged = gitstate.get_staged_names(repo_root)
        gitops.stage_outputs(repo_root)
        gitops.validate_staged(repo_root, baseline_staged)
        message = gitops.build_commit_message(artifact)
        commit_hash = gitops.commit(repo_root, message)
        if commit_hash is not None:
            gitops.push_current_branch(repo_root, git_state.branch)

        _report_success(artifact, audit_result.verdict, commit_hash, git_state.branch)
        return EXIT_SUCCESS

    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return exc.exit_code


def run() -> int:
    return main(sys.argv[1:])
