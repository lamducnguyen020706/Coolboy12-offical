"""End-to-end pipeline flows, with Luna mocked.

The central guarantee under test: EVERY verdict produces a fresh
auditreport.md and a fresh patchprompt.md, and both are committed together.
"""

from __future__ import annotations

import pytest
from audit_runner import outputs, pipeline
from audit_runner.errors import EXIT_SUCCESS

from .conftest import (
    LunaStub,
    git,
    verdict_stub,
)


def _report(repo):
    return (repo / outputs.AUDIT_REPORT_REL).read_text(encoding="utf-8")


def _patch(repo):
    return (repo / outputs.PATCH_PROMPT_REL).read_text(encoding="utf-8")


def _committed_paths(repo):
    return {
        line for line in git(repo, "show", "--name-only", "--pretty=", "HEAD").splitlines()
        if line
    }


@pytest.mark.parametrize("word", ["PASS", "PATCH REQUIRED", "BLOCKED"])
def test_every_verdict_produces_both_outputs_and_commits_both(repo, word):
    stub = verdict_stub("042", word)
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_SUCCESS

    # two calls: the audit, then the patch prompt — on every verdict
    assert len(stub.calls) == 2

    assert f"VERDICT: {word}" in _report(repo)
    assert _patch(repo).strip(), "patchprompt.md must never be left empty"
    assert "042" in _patch(repo)

    assert _committed_paths(repo) == {
        "hhtech/auditreport.md", "hhtech/patchprompt.md"
    }
    assert git(repo, "log", "-1", "--pretty=%s").strip() == (
        "audit: refresh Artifact 042 audit outputs"
    )


def test_pass_patchprompt_forbids_patching(repo):
    pipeline.main(["042"], luna=verdict_stub("042", "PASS"), repo_root=repo)
    patch = _patch(repo).upper()
    assert "NO PATCH REQUIRED" in patch
    assert "DO NOT MODIFY THE TARGET ARTIFACT" in patch


def test_blocked_patchprompt_forbids_patching_and_requires_reaudit(repo):
    pipeline.main(["042"], luna=verdict_stub("042", "BLOCKED"), repo_root=repo)
    patch = _patch(repo)
    assert "DO NOT PATCH" in patch.upper()
    assert "./hhtech/audit 042" in patch
    assert "not an artifact defect" in patch.lower()


def test_patch_required_patchprompt_is_actionable(repo):
    pipeline.main(["042"], luna=verdict_stub("042", "PATCH REQUIRED"), repo_root=repo)
    patch = _patch(repo)
    assert "AUD-042-01" in patch
    assert "NO PATCH REQUIRED" not in patch.upper()
    assert "SELF-AUDIT" in patch.upper()


def test_patch_call_receives_the_audit_report_and_verdict_contract(repo):
    stub = verdict_stub("042", "BLOCKED")
    pipeline.main(["042"], luna=stub, repo_root=repo)
    _system, patch_user_content = stub.calls[1]
    assert "VERDICT: BLOCKED" in patch_user_content
    assert "CONTRACT C" in patch_user_content


def test_stale_patchprompt_is_overwritten_on_the_next_run(repo):
    pipeline.main(["042"], luna=verdict_stub("042", "PATCH REQUIRED"), repo_root=repo)
    assert "AUD-042-01" in _patch(repo)

    pipeline.main(["042"], luna=verdict_stub("042", "PASS"), repo_root=repo)
    refreshed = _patch(repo)
    assert "AUD-042-01" not in refreshed, "stale patch content survived a PASS run"
    assert "NO PATCH REQUIRED" in refreshed.upper()


def test_push_targets_the_current_branch(repo):
    pipeline.main(["042"], luna=verdict_stub("042", "PASS"), repo_root=repo)
    assert git(repo, "rev-parse", "HEAD").strip() == git(repo, "rev-parse", "origin/main").strip()


def test_branch_detected_dynamically_not_hardcoded(repo):
    main_before = git(repo, "rev-parse", "origin/main").strip()
    git(repo, "checkout", "-b", "claude/some-other-branch")
    git(repo, "push", "-u", "origin", "claude/some-other-branch")

    assert pipeline.main(
        ["042"], luna=verdict_stub("042", "PASS"), repo_root=repo
    ) == EXIT_SUCCESS

    assert git(repo, "rev-parse", "HEAD").strip() == git(
        repo, "rev-parse", "origin/claude/some-other-branch"
    ).strip()
    assert git(repo, "rev-parse", "origin/main").strip() == main_before


def test_new_artifact_with_no_baseline_still_audits(repo):
    stub = verdict_stub("043", "BLOCKED")
    assert pipeline.main(["43"], luna=stub, repo_root=repo) == EXIT_SUCCESS
    _system, user_content = stub.calls[0]
    assert "DECLARED BUT NOT PRESENT ON DISK" in user_content
    assert "NEW/UNTRACKED" in user_content


def test_multi_file_scope_reaches_the_model(repo):
    stub = verdict_stub("044", "PASS")
    assert pipeline.main(["44"], luna=stub, repo_root=repo) == EXIT_SUCCESS
    _system, user_content = stub.calls[0]
    assert "docs/target/multi/a.md" in user_content
    assert "docs/target/multi/b.md" in user_content


def test_audit_prompt_separates_source_set_from_audit_scope(repo):
    stub = verdict_stub("042", "PASS")
    pipeline.main(["042"], luna=stub, repo_root=repo)
    _system, user_content = stub.calls[0]
    assert "## AUDIT SCOPE (what is being judged)" in user_content
    assert "## SOURCE SET (what you were given to read)" in user_content
    assert "Findings may be raised ONLY against these paths" in user_content


def test_audit_prompt_supplies_spine_and_invariant_text(repo):
    stub = verdict_stub("042", "PASS")
    pipeline.main(["042"], luna=stub, repo_root=repo)
    _system, user_content = stub.calls[0]
    assert "SOURCE: Blueprint §10" in user_content
    assert "One Canon" in user_content          # the Spine's actual text
    assert "SOURCE: Invariant I-101" in user_content
    assert "sovereign Record Model" in user_content   # the invariant's actual text


def test_audit_prompt_forbids_recursive_audits_and_invented_sources(repo):
    stub = verdict_stub("042", "PASS")
    pipeline.main(["042"], luna=stub, repo_root=repo)
    system_prompt, _user = stub.calls[0]
    assert "MUST NOT audit it" in system_prompt
    assert "Do not invent a requirement" in system_prompt
    assert "UNVERIFIABLE" in system_prompt


def test_unrelated_working_tree_change_is_evidence_not_scope(repo):
    (repo / "docs" / "unrelated.md").write_text("unrelated working-tree change\n")
    stub = verdict_stub("042", "PASS")
    pipeline.main(["042"], luna=stub, repo_root=repo)
    _system, user_content = stub.calls[0]
    assert "docs/unrelated.md" in user_content          # supplied as git evidence
    assert "TARGET docs/unrelated.md" not in user_content  # never as audit scope


def test_second_identical_run_is_a_no_op_but_still_succeeds(repo):
    pipeline.main(["042"], luna=verdict_stub("042", "PASS"), repo_root=repo)
    head_after_first = git(repo, "rev-parse", "HEAD").strip()

    assert pipeline.main(
        ["042"], luna=verdict_stub("042", "PASS"), repo_root=repo
    ) == EXIT_SUCCESS
    assert git(repo, "rev-parse", "HEAD").strip() == head_after_first


def test_luna_never_called_for_an_unknown_artifact(repo):
    stub = LunaStub([])
    assert pipeline.main(["099"], luna=stub, repo_root=repo) != 0
    assert stub.calls == []
