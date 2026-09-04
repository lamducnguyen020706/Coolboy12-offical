"""Git commit/push safety firewall tests — BUILD spec §38's "most dangerous
case" and the surrounding staging/branch/commit-message/push guarantees.

No real network remote (origin is a local bare repo); no real API key.
"""

from __future__ import annotations

from audit_runner import gitops, outputs, pipeline
from audit_runner.errors import EXIT_SUCCESS

from .conftest import LunaStub, git, make_audit_response, make_patch_prompt


def test_most_dangerous_case_only_hhtech_files_staged(repo):
    """A working tree with source changes, test changes, doc changes, AND
    the two hhtech output files dirty. After the runner's commit logic
    runs, ONLY the two hhtech files may be staged/committed — everything
    else must remain untouched in the working tree.
    """
    (repo / "src_change.py").write_text("# pretend source change\nX = 1\n")
    (repo / "tests_change_test.py").write_text("# pretend test change\n")
    (repo / "docs_change.md").write_text("# pretend doc change\n")
    git(repo, "add", "src_change.py", "tests_change_test.py", "docs_change.md")
    git(repo, "commit", "-m", "unrelated prior work in progress")

    # further, still-uncommitted dirt on top, exactly mirroring §38's scenario
    (repo / "src_change.py").write_text("# pretend source change v2\nX = 2\n")
    (repo / "tests_change_test.py").write_text("# pretend test change v2\n")
    (repo / "docs_change.md").write_text("# pretend doc change v2\n")

    stub = LunaStub([make_audit_response("042", "PASS")])
    exit_code = pipeline.main(["042"], luna=stub)
    assert exit_code == EXIT_SUCCESS

    committed = {
        line
        for line in git(repo, "show", "--name-only", "--pretty=", "HEAD").splitlines()
        if line
    }
    assert committed == {"hhtech/auditreport.md", "hhtech/patchprompt.md"}

    # the artifact/source/test/doc changes remain UNSTAGED, not committed
    status = git(repo, "status", "--short")
    dirty_paths = {line[3:] for line in status.splitlines() if line}
    assert "src_change.py" in dirty_paths
    assert "tests_change_test.py" in dirty_paths
    assert "docs_change.md" in dirty_paths

    staged_now = git(repo, "diff", "--cached", "--name-only")
    assert staged_now.strip() == ""  # nothing left staged after the commit


def test_staging_firewall_unit_aborts_on_unexpected_staged_file(repo):
    """Direct unit test of the firewall: if something unexpected ends up
    staged, validate_staged() must abort and unstage the runner's own
    additions rather than allow a commit.
    """
    (repo / "hhtech" / outputs.AUDIT_REPORT_NAME).write_text("fake report\n")
    (repo / "sneaky.txt").write_text("should never be committed by the runner\n")

    baseline = ()
    git(repo, "add", "--", "hhtech/auditreport.md")
    git(repo, "add", "--", "sneaky.txt")  # simulates unexpected concurrent staging

    from audit_runner.errors import GitSafetyFailure

    try:
        gitops.validate_staged(repo, baseline)
        raised = False
    except GitSafetyFailure:
        raised = True
    assert raised

    staged_after = git(repo, "diff", "--cached", "--name-only")
    # sneaky.txt must still be staged (untouched by the firewall — it only
    # unstages the runner's own ALLOWED_PATHS), auditreport.md must have
    # been unstaged by the abort path
    assert "sneaky.txt" in staged_after
    assert "hhtech/auditreport.md" not in staged_after


def test_stale_patchprompt_cleared_on_subsequent_pass(repo):
    stub1 = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        make_patch_prompt("042"),
    ])
    pipeline.main(["042"], luna=stub1)
    patch_after_first = (repo / "hhtech" / outputs.PATCH_PROMPT_NAME).read_text(encoding="utf-8")
    assert not outputs.is_cleared_patch_prompt(patch_after_first)

    stub2 = LunaStub([make_audit_response("042", "PASS")])
    exit_code = pipeline.main(["042"], luna=stub2)
    assert exit_code == EXIT_SUCCESS

    patch_after_second = (repo / "hhtech" / outputs.PATCH_PROMPT_NAME).read_text(encoding="utf-8")
    assert outputs.is_cleared_patch_prompt(patch_after_second)
    assert "AUD-042-01" not in patch_after_second  # no stale finding content survives


def test_branch_is_detected_dynamically_not_hardcoded(repo):
    main_before = git(repo, "rev-parse", "origin/main").strip()
    git(repo, "checkout", "-b", "claude/some-other-branch-name")
    git(repo, "push", "-u", "origin", "claude/some-other-branch-name")

    stub = LunaStub([make_audit_response("042", "PASS")])
    exit_code = pipeline.main(["042"], luna=stub)
    assert exit_code == EXIT_SUCCESS

    local_head = git(repo, "rev-parse", "HEAD").strip()
    remote_head = git(repo, "rev-parse", "origin/claude/some-other-branch-name").strip()
    assert local_head == remote_head

    main_after = git(repo, "rev-parse", "origin/main").strip()
    assert main_after == main_before  # main must be untouched by this push


def test_no_op_when_nothing_changed_still_reports_success(repo):
    """Running the identical audit twice in a row: the second run's commit
    is a no-op (identical file content) and must not fail or push
    needlessly, but must still exit 0."""
    stub1 = LunaStub([make_audit_response("042", "PASS")])
    pipeline.main(["042"], luna=stub1)

    stub2 = LunaStub([make_audit_response("042", "PASS")])
    exit_code = pipeline.main(["042"], luna=stub2)
    assert exit_code == EXIT_SUCCESS
