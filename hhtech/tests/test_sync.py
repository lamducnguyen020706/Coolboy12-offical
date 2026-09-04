"""Remote synchronization: the runner must never audit stale local state.

Every case runs against throwaway repositories with a local bare `origin`.
No network, no real remote, no paid API call — where a full pipeline run is
exercised, Luna is stubbed.
"""

from __future__ import annotations

import pytest
from audit_runner import outputs, pipeline, sync
from audit_runner.errors import EXIT_SUCCESS, EXIT_SYNC_FAILURE, SyncFailure

from .conftest import LunaStub, git, verdict_stub


def _clone_second_worktree(tmp_path, origin_path):
    """A second clone of the same origin, standing in for another machine
    (or Claude Code) pushing a commit."""
    other = tmp_path / "other"
    git(tmp_path, "clone", "--quiet", str(origin_path), str(other))
    git(other, "config", "user.email", "other@example.invalid")
    git(other, "config", "user.name", "Other Worker")
    return other


@pytest.fixture
def origin_path(repo):
    return repo.parent / "origin.git"


# ---------------------------------------------------------------------------
# Relationship classification
# ---------------------------------------------------------------------------

def test_equal_is_a_no_op(repo):
    result = sync.synchronize(repo)
    assert result.relation == sync.RELATION_EQUAL
    assert result.action == sync.ACTION_NONE
    assert result.head_before == result.head_after == result.remote_head
    assert not result.fast_forwarded


def test_remote_ahead_fast_forwards(repo, tmp_path, origin_path):
    head_before = git(repo, "rev-parse", "HEAD").strip()

    other = _clone_second_worktree(tmp_path, origin_path)
    (other / "docs" / "target" / "thing.md").write_text("# updated remotely\n")
    git(other, "commit", "-q", "-am", "remote update to the target artifact")
    git(other, "push", "-q", "origin", "main")

    result = sync.synchronize(repo)

    assert result.relation == sync.RELATION_REMOTE_AHEAD
    assert result.fast_forwarded
    assert result.head_before == head_before
    assert result.head_after == result.remote_head != head_before
    # the fast-forward actually brought the new content into the worktree
    assert (repo / "docs" / "target" / "thing.md").read_text() == "# updated remotely\n"


def test_local_ahead_fails_closed(repo):
    (repo / "docs" / "target" / "thing.md").write_text("# local only\n")
    git(repo, "commit", "-q", "-am", "local commit never pushed")

    with pytest.raises(SyncFailure) as exc:
        sync.synchronize(repo)
    assert sync.NON_FAST_FORWARD_LOCAL_STATE in str(exc.value)


def test_diverged_history_fails_closed(repo, tmp_path, origin_path):
    other = _clone_second_worktree(tmp_path, origin_path)
    (other / "docs" / "target" / "dep041.md").write_text("# remote side\n")
    git(other, "commit", "-q", "-am", "remote-side commit")
    git(other, "push", "-q", "origin", "main")

    (repo / "docs" / "target" / "thing.md").write_text("# local side\n")
    git(repo, "commit", "-q", "-am", "local-side commit")

    with pytest.raises(SyncFailure) as exc:
        sync.synchronize(repo)
    assert sync.DIVERGED_HISTORY in str(exc.value)


def test_fetch_failure_fails_closed(repo):
    git(repo, "remote", "set-url", "origin", str(repo.parent / "does-not-exist.git"))
    with pytest.raises(SyncFailure) as exc:
        sync.synchronize(repo)
    assert sync.FETCH_FAILURE in str(exc.value)


def test_detached_head_fails_closed(repo):
    head = git(repo, "rev-parse", "HEAD").strip()
    git(repo, "checkout", "-q", "--detach", head)
    with pytest.raises(SyncFailure) as exc:
        sync.synchronize(repo)
    assert sync.BRANCH_STATE_FAILURE in str(exc.value)


def test_branch_without_remote_counterpart_fails_closed(repo):
    git(repo, "checkout", "-q", "-b", "local-only-branch")
    with pytest.raises(SyncFailure) as exc:
        sync.synchronize(repo)
    assert sync.BRANCH_STATE_FAILURE in str(exc.value)


# ---------------------------------------------------------------------------
# Working-tree protection
# ---------------------------------------------------------------------------

def test_fast_forward_conflict_fails_closed_without_touching_the_file(
    repo, tmp_path, origin_path
):
    other = _clone_second_worktree(tmp_path, origin_path)
    (other / "docs" / "target" / "thing.md").write_text("# remote version\n")
    git(other, "commit", "-q", "-am", "remote edits the same file")
    git(other, "push", "-q", "origin", "main")

    (repo / "docs" / "target" / "thing.md").write_text("# precious local edit\n")

    with pytest.raises(SyncFailure) as exc:
        sync.synchronize(repo)
    assert sync.WORKTREE_SYNC_CONFLICT in str(exc.value)
    assert "docs/target/thing.md" in str(exc.value)
    # the local edit survives untouched
    assert (repo / "docs" / "target" / "thing.md").read_text() == "# precious local edit\n"


def test_unrelated_local_modifications_survive_a_fast_forward(
    repo, tmp_path, origin_path
):
    """The reports/*.json case: local tracking state the remote never touched
    must cross a fast-forward unchanged."""
    (repo / "reports").mkdir(exist_ok=True)
    for name in ("implement-log.json", "progress.json"):
        (repo / "reports" / name).write_text('{"seed": true}\n')
    git(repo, "add", "reports")
    git(repo, "commit", "-q", "-m", "seed local tracking files")
    git(repo, "push", "-q", "origin", "main")

    for name in ("implement-log.json", "progress.json"):
        (repo / "reports" / name).write_text('{"local": "uncommitted"}\n')

    other = _clone_second_worktree(tmp_path, origin_path)
    (other / "docs" / "target" / "thing.md").write_text("# remote update\n")
    git(other, "commit", "-q", "-am", "remote update elsewhere")
    git(other, "push", "-q", "origin", "main")

    result = sync.synchronize(repo)

    assert result.fast_forwarded
    for name in ("implement-log.json", "progress.json"):
        assert (repo / "reports" / name).read_text() == '{"local": "uncommitted"}\n'
    assert "reports/" in git(repo, "status", "--short")


def test_sync_never_runs_a_destructive_command():
    from pathlib import Path

    text = Path(sync.__file__).read_text()
    for argument in ("reset", "clean", "stash", "--hard", "--force", "checkout", "rebase"):
        for literal in (f'"{argument}"', f"'{argument}'"):
            assert literal not in text, f"sync.py passes {argument!r} to git"


# ---------------------------------------------------------------------------
# Snapshot coherence
# ---------------------------------------------------------------------------

def test_snapshot_records_post_sync_head(repo):
    result = sync.synchronize(repo)
    snapshot = sync.capture_snapshot(repo, result)
    assert snapshot.head == result.head_after
    assert snapshot.branch == result.branch
    snapshot.verify_unchanged(repo)


def test_snapshot_drift_fails_closed(repo):
    snapshot = sync.capture_snapshot(repo, sync.synchronize(repo))
    (repo / "docs" / "target" / "thing.md").write_text("# moved on\n")
    git(repo, "commit", "-q", "-am", "repository moves mid-run")

    with pytest.raises(SyncFailure) as exc:
        snapshot.verify_unchanged(repo)
    assert sync.SNAPSHOT_DRIFT in str(exc.value)


def test_snapshot_branch_change_fails_closed(repo):
    snapshot = sync.capture_snapshot(repo, sync.synchronize(repo))
    git(repo, "checkout", "-q", "-b", "somewhere-else")
    with pytest.raises(SyncFailure) as exc:
        snapshot.verify_unchanged(repo)
    assert sync.SNAPSHOT_DRIFT in str(exc.value)


# ---------------------------------------------------------------------------
# Pipeline integration
# ---------------------------------------------------------------------------

def test_pipeline_audits_the_post_sync_artifact_not_the_stale_one(
    repo, tmp_path, origin_path
):
    """The motivating case: Claude Code pushes a patch, then the runner is
    invoked. The audit must see the pushed version, not the local one."""
    other = _clone_second_worktree(tmp_path, origin_path)
    (other / "docs" / "target" / "thing.md").write_text(
        "# patched remotely\n\nPATCHED-CONTENT-MARKER\n"
    )
    git(other, "commit", "-q", "-am", "Claude Code pushes a patch")
    git(other, "push", "-q", "origin", "main")
    pushed_head = git(other, "rev-parse", "HEAD").strip()

    stub = verdict_stub("042", "PASS")
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_SUCCESS

    _system, user_content = stub.calls[0]
    assert "PATCHED-CONTENT-MARKER" in user_content, "the audit read stale content"
    assert pushed_head in user_content, "the audit did not state the synchronized HEAD"


def test_pipeline_source_discovery_happens_after_sync(repo, tmp_path, origin_path):
    """A source file that only exists on the remote must be discoverable."""
    other = _clone_second_worktree(tmp_path, origin_path)
    (other / "docs" / "target" / "new.md").write_text("# artifact 043 now exists\n")
    git(other, "add", "docs/target/new.md")
    git(other, "commit", "-q", "-m", "add artifact 043 remotely")
    git(other, "push", "-q", "origin", "main")

    stub = verdict_stub("043", "PASS")
    assert pipeline.main(["043"], luna=stub, repo_root=repo) == EXIT_SUCCESS
    _system, user_content = stub.calls[0]
    assert "artifact 043 now exists" in user_content
    assert "DECLARED BUT NOT PRESENT ON DISK" not in user_content


def test_sync_failure_never_invokes_the_auditor(repo):
    (repo / "docs" / "target" / "thing.md").write_text("# local only\n")
    git(repo, "commit", "-q", "-am", "local commit never pushed")

    stub = LunaStub([])
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_SYNC_FAILURE
    assert stub.calls == [], "a paid audit was spent despite a synchronization failure"


def test_sync_failure_leaves_outputs_untouched(repo):
    git(repo, "remote", "set-url", "origin", str(repo.parent / "gone.git"))
    stub = LunaStub([])

    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_SYNC_FAILURE
    assert (repo / outputs.AUDIT_REPORT_REL).read_text() == ""
    assert (repo / outputs.PATCH_PROMPT_REL).read_text() == ""


def test_sync_failure_exit_code_is_distinct_from_artifact_outcomes():
    """A runner/infrastructure failure must be distinguishable from every
    verdict-bearing outcome."""
    from audit_runner.errors import (
        EXIT_API_FAILURE,
        EXIT_GIT_SAFETY_FAILURE,
        EXIT_INPUT_ERROR,
        EXIT_INVALID_AUDIT_RESPONSE,
        EXIT_PATCH_GENERATION_FAILURE,
    )

    others = {
        EXIT_SUCCESS, EXIT_INPUT_ERROR, EXIT_API_FAILURE,
        EXIT_INVALID_AUDIT_RESPONSE, EXIT_PATCH_GENERATION_FAILURE,
        EXIT_GIT_SAFETY_FAILURE,
    }
    assert EXIT_SYNC_FAILURE not in others


def test_pipeline_reports_the_audited_head(repo, capsys):
    pipeline.main(["042"], luna=verdict_stub("042", "PASS"), repo_root=repo)
    printed = capsys.readouterr().out
    assert "Synchronizing with the remote branch" in printed
    assert "Audited HEAD:" in printed
    assert git(repo, "rev-parse", "HEAD").strip()[:12] in printed
