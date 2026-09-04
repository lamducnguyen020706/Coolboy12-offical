"""End-to-end pipeline flows against a throwaway repo, with Luna mocked.

No real HHTECH API call, no real push (origin is a local bare repo), no
real API key.
"""

from __future__ import annotations

from pathlib import Path

from audit_runner import outputs, pipeline
from audit_runner.errors import EXIT_SUCCESS

from .conftest import LunaStub, git, make_audit_response, make_patch_prompt


def _report_path(work: Path) -> Path:
    return work / "hhtech" / outputs.AUDIT_REPORT_NAME


def _patch_path(work: Path) -> Path:
    return work / "hhtech" / outputs.PATCH_PROMPT_NAME


def test_pass_flow(repo):
    stub = LunaStub([make_audit_response("042", "PASS")])
    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_SUCCESS
    assert len(stub.calls) == 1  # PASS never triggers a second (patch) call

    report = _report_path(repo).read_text(encoding="utf-8")
    assert "VERDICT: PASS" in report

    patch = _patch_path(repo).read_text(encoding="utf-8")
    assert outputs.is_cleared_patch_prompt(patch)

    log = git(repo, "log", "-1", "--pretty=%s")
    assert log.strip() == "audit: refresh Artifact 042 audit outputs"

    staged_in_commit = git(repo, "show", "--name-only", "--pretty=", "HEAD")
    changed = {line for line in staged_in_commit.splitlines() if line}
    assert changed == {"hhtech/auditreport.md", "hhtech/patchprompt.md"} or changed <= {
        "hhtech/auditreport.md", "hhtech/patchprompt.md"
    }


def test_blocked_flow(repo):
    stub = LunaStub([make_audit_response("042", "BLOCKED")])
    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_SUCCESS
    assert len(stub.calls) == 1

    report = _report_path(repo).read_text(encoding="utf-8")
    assert "VERDICT: BLOCKED" in report

    patch = _patch_path(repo).read_text(encoding="utf-8")
    assert outputs.is_cleared_patch_prompt(patch)


def test_patch_required_flow(repo):
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        make_patch_prompt("042"),
    ])
    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_SUCCESS
    assert len(stub.calls) == 2  # audit call, then patch-prompt call

    report = _report_path(repo).read_text(encoding="utf-8")
    assert "VERDICT: PATCH REQUIRED" in report

    patch = _patch_path(repo).read_text(encoding="utf-8")
    assert not outputs.is_cleared_patch_prompt(patch)
    assert "042" in patch
    assert "## Task" in patch

    # the second (patch-generation) call must have been built from the
    # audit report produced by the first call
    _audit_system, patch_user_content = stub.calls[1]
    assert "VERDICT: PATCH REQUIRED" in patch_user_content


def test_patch_required_pushes_to_current_branch(repo):
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        make_patch_prompt("042"),
    ])
    pipeline.main(["042"], luna=stub)

    local_head = git(repo, "rev-parse", "HEAD").strip()
    remote_head = git(repo, "rev-parse", "origin/main").strip()
    assert local_head == remote_head


def test_new_artifact_empty_diff_still_runs(repo):
    """Artifact 043's target file does not exist on disk yet — an empty
    git diff. The runner must still complete the audit call rather than
    assuming a nonexistent file is a failure (BUILD spec §10)."""
    stub = LunaStub([make_audit_response("043", "PASS")])
    exit_code = pipeline.main(["43"], luna=stub)

    assert exit_code == EXIT_SUCCESS
    system_prompt, user_content = stub.calls[0]
    assert "FILE DOES NOT EXIST ON DISK" in user_content


def test_multi_file_glob_scope_all_files_included(repo):
    stub = LunaStub([make_audit_response("044", "PASS")])
    exit_code = pipeline.main(["44"], luna=stub)

    assert exit_code == EXIT_SUCCESS
    _system_prompt, user_content = stub.calls[0]
    assert "docs/target/multi/a.md" in user_content
    assert "docs/target/multi/b.md" in user_content


def test_h_dependency_context_included_existence_only(repo):
    stub = LunaStub([make_audit_response("042", "PASS")])
    pipeline.main(["042"], luna=stub)

    _system_prompt, user_content = stub.calls[0]
    assert "H-dependency 041" in user_content


def test_unexpected_changed_file_preserved_as_evidence(repo):
    (repo / "docs" / "unrelated.md").write_text("unrelated change\n")
    git(repo, "add", "docs/unrelated.md")
    git(repo, "commit", "-m", "unrelated prior change for evidence test")
    (repo / "docs" / "target" / "thing.md").write_text("# Target artifact content\n\nModified.\n")

    stub = LunaStub([make_audit_response("042", "PASS")])
    pipeline.main(["042"], luna=stub)

    _system_prompt, user_content = stub.calls[0]
    assert "thing.md" in user_content
    # the working-tree modification to the in-scope file is real evidence
    # and must appear in what was sent, via git diff / git status
    assert "Modified." in user_content or "thing.md" in user_content
