"""Git firewall and baseline collection.

The runner commits exactly two paths, never destroys working-tree work, and
never runs a destructive git command.
"""

from __future__ import annotations

import pytest
from audit_runner import gitops, gitstate, pipeline
from audit_runner.errors import EXIT_SUCCESS, GitSafetyFailure

from .conftest import git, verdict_stub


def _committed_paths(repo):
    return {
        line for line in git(repo, "show", "--name-only", "--pretty=", "HEAD").splitlines()
        if line
    }


def test_most_dangerous_case_only_the_two_outputs_are_committed(repo):
    """A working tree dirty with source, test, doc and report changes. The
    runner must commit only its own two outputs and leave everything else
    exactly as the user left it."""
    dirty = {
        "src_change.py": "# pretend source change\nX = 1\n",
        "tests_change_test.py": "# pretend test change\n",
        "docs_change.md": "# pretend doc change\n",
        "reports/progress.json": '{"progress": 1}\n',
        "reports/implement-log.json": '{"log": []}\n',
    }
    (repo / "reports").mkdir(exist_ok=True)
    for path, content in dirty.items():
        (repo / path).write_text(content)
    git(repo, "add", "-A")
    git(repo, "commit", "-m", "unrelated prior work")
    # Push it: the runner synchronizes before auditing and refuses a
    # local-ahead branch, so prior work must be on the remote like any real
    # committed state. The firewall assertions below are unchanged.
    git(repo, "push", "-q", "origin", "main")

    # now dirty them again, uncommitted
    for path, content in dirty.items():
        (repo / path).write_text(content.replace("1", "2") + "# v2\n")

    assert pipeline.main(
        ["042"], luna=verdict_stub("042", "PASS"), repo_root=repo
    ) == EXIT_SUCCESS

    assert _committed_paths(repo) == {"hhtech/auditreport.md", "hhtech/patchprompt.md"}

    status = git(repo, "status", "--short")
    still_dirty = {line[3:] for line in status.splitlines() if line}
    for path in dirty:
        assert path in still_dirty, f"{path} lost its uncommitted change"
        assert (repo / path).read_text().endswith("# v2\n")

    assert git(repo, "diff", "--cached", "--name-only").strip() == ""


def test_firewall_aborts_and_unstages_only_its_own_paths(repo):
    (repo / "hhtech/auditreport.md").write_text("fresh report\n")
    (repo / "sneaky.txt").write_text("must never be committed by the runner\n")
    git(repo, "add", "--", "hhtech/auditreport.md")
    git(repo, "add", "--", "sneaky.txt")

    with pytest.raises(GitSafetyFailure) as exc:
        gitops.validate_staged(repo)
    assert "sneaky.txt" in str(exc.value)

    staged = git(repo, "diff", "--cached", "--name-only")
    assert "sneaky.txt" in staged, "the user's staged work must be preserved"
    assert "hhtech/auditreport.md" not in staged, "the runner must unstage its own path"


def test_preflight_never_unstages_user_work(repo):
    (repo / "user_file.py").write_text("Y = 1\n")
    git(repo, "add", "user_file.py")

    with pytest.raises(GitSafetyFailure):
        gitops.assert_index_committable(repo)

    assert "user_file.py" in git(repo, "diff", "--cached", "--name-only")


def test_allowed_paths_are_exactly_the_two_outputs():
    assert gitops.ALLOWED_PATHS == ("hhtech/auditreport.md", "hhtech/patchprompt.md")


def test_commit_is_pathspec_limited(repo):
    """Even with an unrelated file already staged, the pathspec-limited commit
    itself never carries it — the second safety layer."""
    (repo / "hhtech/auditreport.md").write_text("report\n")
    (repo / "hhtech/patchprompt.md").write_text("prompt\n")
    (repo / "unrelated.txt").write_text("unrelated\n")
    git(repo, "add", "--", "hhtech/auditreport.md", "hhtech/patchprompt.md", "unrelated.txt")

    commit_hash = gitops.commit(repo, "audit: refresh Artifact 042 audit outputs")
    assert commit_hash
    assert _committed_paths(repo) == {"hhtech/auditreport.md", "hhtech/patchprompt.md"}
    assert "unrelated.txt" in git(repo, "diff", "--cached", "--name-only")


def test_push_refuses_when_the_branch_changed_mid_run(repo):
    with pytest.raises(GitSafetyFailure) as exc:
        gitops.push_current_branch(repo, "some-other-branch")
    assert "refusing to push" in str(exc.value)


def test_commit_message_format():
    assert gitops.build_commit_message("042") == "audit: refresh Artifact 042 audit outputs"


# ---------------------------------------------------------------------------
# Baseline collection — read-only
# ---------------------------------------------------------------------------

def test_baseline_for_tracked_unchanged_file(repo):
    state = gitstate.collect_git_state(repo, ("docs/target/thing.md",))
    baseline = state.baselines[0]
    assert baseline.tracked
    assert baseline.exists_on_disk
    assert baseline.head_content is not None
    assert not baseline.changed_since_head


def test_baseline_for_modified_file_carries_the_head_diff(repo):
    (repo / "docs/target/thing.md").write_text("# rewritten\n")
    state = gitstate.collect_git_state(repo, ("docs/target/thing.md",))
    baseline = state.baselines[0]
    assert baseline.changed_since_head
    assert "rewritten" in baseline.diff_vs_head
    assert "Record Model definition" in (baseline.head_content or "")


def test_baseline_for_untracked_new_artifact(repo):
    (repo / "docs/target/new.md").write_text("# brand new\n")
    state = gitstate.collect_git_state(repo, ("docs/target/new.md",))
    baseline = state.baselines[0]
    assert not baseline.tracked
    assert baseline.exists_on_disk
    assert baseline.head_content is None
    assert baseline.changed_since_head, "a new artifact is not an unchanged one"


def test_baseline_for_declared_but_absent_file(repo):
    state = gitstate.collect_git_state(repo, ("docs/target/new.md",))
    baseline = state.baselines[0]
    assert not baseline.tracked
    assert not baseline.exists_on_disk


def test_state_collection_captures_staged_and_unstaged_separately(repo):
    (repo / "docs/target/thing.md").write_text("# unstaged edit\n")
    (repo / "docs/target/dep041.md").write_text("# staged edit\n")
    git(repo, "add", "docs/target/dep041.md")

    state = gitstate.collect_git_state(repo, ("docs/target/thing.md",))
    assert "thing.md" in state.diff_name_status
    assert "dep041.md" in state.staged_name_status
    assert "dep041.md" not in state.diff_name_status


def test_collecting_state_mutates_nothing(repo):
    before_status = git(repo, "status", "--short")
    before_head = git(repo, "rev-parse", "HEAD")
    (repo / "docs/target/thing.md").write_text("# edited\n")

    gitstate.collect_git_state(repo, ("docs/target/thing.md", "docs/target/new.md"))

    assert (repo / "docs/target/thing.md").read_text() == "# edited\n"
    assert git(repo, "rev-parse", "HEAD") == before_head
    assert before_status != git(repo, "status", "--short")  # our own edit, nothing else


def test_runner_never_invokes_a_destructive_git_command():
    """No reset, clean, stash, checkout or force-push is ever passed to git.

    Scans for the argument *literals*, so prose in a docstring saying the
    runner never force-pushes does not itself trip the check.
    """
    from pathlib import Path

    runner_dir = Path(gitops.__file__).parent
    forbidden_arguments = (
        "reset", "clean", "stash", "checkout", "--hard", "--force", "-f", "+HEAD",
    )
    for source_file in runner_dir.glob("*.py"):
        text = source_file.read_text()
        for argument in forbidden_arguments:
            for literal in (f'"{argument}"', f"'{argument}'"):
                assert literal not in text, (
                    f"{source_file.name} passes {argument!r} to git"
                )
