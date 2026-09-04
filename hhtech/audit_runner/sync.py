"""Remote synchronization — runs before any source is read.

The remote branch is the source of the latest committed artifact. A patch
pushed by Claude Code is only visible here after a fetch, so auditing local
state without synchronizing risks auditing a superseded artifact and
attributing a stale defect to it.

The whole module is non-destructive. It fetches, classifies the local/remote
relationship, and fast-forwards only when that is provably safe. It never
resets, cleans, stashes, force-checks-out, rebases, merges non-fast-forward,
or rewrites history. Where safety cannot be established it fails closed with
a named reason, because a refused audit is recoverable and a destroyed
working tree is not.

Failure reasons are stable identifiers, so a runner/infrastructure failure is
never mistaken for an artifact defect:

    BRANCH_STATE_FAILURE        HEAD is not on a resolvable local branch, or
                                origin/<branch> does not exist
    FETCH_FAILURE               the remote could not be contacted or read
    NON_FAST_FORWARD_LOCAL_STATE  local holds commits the remote does not
    DIVERGED_HISTORY            both sides hold commits the other lacks
    WORKTREE_SYNC_CONFLICT      fast-forwarding would overwrite local edits
    HEAD_VERIFICATION_FAILURE   HEAD is not the expected commit after sync
    SNAPSHOT_DRIFT              the repository moved while context was built
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from .errors import SyncFailure

_TIMEOUT = 120

BRANCH_STATE_FAILURE = "BRANCH_STATE_FAILURE"
FETCH_FAILURE = "FETCH_FAILURE"
NON_FAST_FORWARD_LOCAL_STATE = "NON_FAST_FORWARD_LOCAL_STATE"
DIVERGED_HISTORY = "DIVERGED_HISTORY"
WORKTREE_SYNC_CONFLICT = "WORKTREE_SYNC_CONFLICT"
HEAD_VERIFICATION_FAILURE = "HEAD_VERIFICATION_FAILURE"
SNAPSHOT_DRIFT = "SNAPSHOT_DRIFT"

RELATION_EQUAL = "EQUAL"
RELATION_REMOTE_AHEAD = "REMOTE_AHEAD"
RELATION_LOCAL_AHEAD = "LOCAL_AHEAD"
RELATION_DIVERGED = "DIVERGED"

ACTION_NONE = "already in sync"
ACTION_FAST_FORWARDED = "fast-forwarded to the remote branch"

REMOTE = "origin"


def _fail(reason: str, detail: str) -> SyncFailure:
    return SyncFailure(f"{reason}: {detail}")


def _run(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", "-C", str(repo_root), *args],
            capture_output=True, text=True, timeout=_TIMEOUT, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise _fail(FETCH_FAILURE, f"git {' '.join(args)} could not run: {exc}") from exc


def _out(repo_root: Path, args: list[str], reason: str) -> str:
    result = _run(repo_root, args)
    if result.returncode != 0:
        raise _fail(reason, f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


@dataclass(frozen=True)
class SyncResult:
    """What synchronization did, and the state it established."""

    branch: str
    remote_ref: str
    head_before: str
    head_after: str
    remote_head: str
    relation: str
    action: str

    @property
    def fast_forwarded(self) -> bool:
        return self.action == ACTION_FAST_FORWARDED


@dataclass(frozen=True)
class AuditSnapshot:
    """The single coherent repository state the audit is performed against.

    Every source read and every piece of git evidence in one audit belongs to
    this snapshot. If the repository moves while the context is being built,
    the run fails closed rather than auditing a mixture of two states.
    """

    branch: str
    head: str
    status_short: str

    def verify_unchanged(self, repo_root: Path) -> None:
        current_head = _out(repo_root, ["rev-parse", "HEAD"], SNAPSHOT_DRIFT)
        if current_head != self.head:
            raise _fail(
                SNAPSHOT_DRIFT,
                f"HEAD moved from {self.head[:12]} to {current_head[:12]} while the "
                "audit context was being prepared; refusing to audit a mixed state",
            )
        current_branch = _out(
            repo_root, ["symbolic-ref", "--quiet", "--short", "HEAD"], SNAPSHOT_DRIFT
        )
        if current_branch != self.branch:
            raise _fail(
                SNAPSHOT_DRIFT,
                f"branch changed from {self.branch!r} to {current_branch!r} during "
                "the run; refusing to audit a mixed state",
            )


def resolve_branch(repo_root: Path) -> str:
    """The checked-out local branch. Never a hardcoded name, never a guess."""
    result = _run(repo_root, ["symbolic-ref", "--quiet", "--short", "HEAD"])
    if result.returncode != 0 or not result.stdout.strip():
        raise _fail(
            BRANCH_STATE_FAILURE,
            "HEAD is detached or not on a local branch; the runner audits and "
            "pushes a named branch and will not check one out for you",
        )
    return result.stdout.strip()


def fetch_branch(repo_root: Path, branch: str) -> None:
    """Non-destructive fetch of one branch. No prune, no force, no tags.

    A remote that cannot be reached and a branch the remote does not carry
    are different problems, and are reported as such: the first is a fetch
    failure, the second a branch-state failure. Neither is an artifact defect.
    """
    result = _run(repo_root, ["fetch", "--no-tags", REMOTE, branch])
    if result.returncode == 0:
        return

    stderr = result.stderr.strip()
    if "couldn't find remote ref" in stderr or "not found in upstream" in stderr:
        raise _fail(
            BRANCH_STATE_FAILURE,
            f"{REMOTE} does not carry a branch named {branch!r}. The runner "
            "audits and pushes an existing tracked branch; it will not create "
            "one or fall back to another",
        )
    raise _fail(
        FETCH_FAILURE,
        f"could not fetch {REMOTE}/{branch}: {stderr}. "
        "This is a runner synchronization failure, not an artifact defect",
    )


def _remote_head(repo_root: Path, branch: str) -> str:
    remote_ref = f"{REMOTE}/{branch}"
    result = _run(repo_root, ["rev-parse", "--verify", "--quiet", remote_ref])
    head = result.stdout.strip()
    if result.returncode != 0 or not head:
        raise _fail(
            BRANCH_STATE_FAILURE,
            f"{remote_ref} does not exist after fetching; the runner will not "
            "invent a fallback branch or push a branch the remote does not track",
        )
    return head


def classify(repo_root: Path, local_head: str, remote_head: str) -> str:
    """Classify local vs remote by ancestry, never by commit dates."""
    if local_head == remote_head:
        return RELATION_EQUAL
    local_is_ancestor = _run(
        repo_root, ["merge-base", "--is-ancestor", local_head, remote_head]
    ).returncode == 0
    remote_is_ancestor = _run(
        repo_root, ["merge-base", "--is-ancestor", remote_head, local_head]
    ).returncode == 0
    if local_is_ancestor:
        return RELATION_REMOTE_AHEAD
    if remote_is_ancestor:
        return RELATION_LOCAL_AHEAD
    return RELATION_DIVERGED


def _locally_modified_paths(repo_root: Path) -> set[str]:
    """Tracked paths with uncommitted changes, staged or not."""
    status = _out(repo_root, ["status", "--porcelain"], WORKTREE_SYNC_CONFLICT)
    paths: set[str] = set()
    for line in status.splitlines():
        if not line or line.startswith("??"):
            continue
        path = line[3:].strip()
        # rename entries read "old -> new"; both sides matter
        if " -> " in path:
            before, after = path.split(" -> ", 1)
            paths.update({before.strip(), after.strip()})
        else:
            paths.add(path)
    return paths


def _incoming_paths(repo_root: Path, local_head: str, remote_head: str) -> set[str]:
    diff = _out(
        repo_root,
        ["diff", "--name-only", f"{local_head}..{remote_head}"],
        WORKTREE_SYNC_CONFLICT,
    )
    return {line.strip() for line in diff.splitlines() if line.strip()}


def fast_forward(repo_root: Path, branch: str, local_head: str, remote_head: str) -> None:
    """Fast-forward to the remote, refusing if local work would be lost.

    The overlap between locally-modified paths and paths the incoming commits
    touch is computed first, so the refusal names the conflicting files rather
    than relying on git's own error text. Local edits to files the remote did
    not touch are carried across untouched — which is why
    `reports/implement-log.json` and `reports/progress.json` survive a sync.
    """
    modified = _locally_modified_paths(repo_root)
    incoming = _incoming_paths(repo_root, local_head, remote_head)
    collisions = sorted(modified & incoming)
    if collisions:
        raise _fail(
            WORKTREE_SYNC_CONFLICT,
            f"fast-forwarding {branch} would overwrite uncommitted local changes to "
            f"{collisions}. Nothing was changed. Commit, or set those changes aside "
            "yourself, then re-run — the runner will not discard local work to make "
            "an audit possible",
        )

    result = _run(repo_root, ["merge", "--ff-only", f"{REMOTE}/{branch}"])
    if result.returncode != 0:
        raise _fail(
            WORKTREE_SYNC_CONFLICT,
            f"fast-forward of {branch} refused by git: {result.stderr.strip()}. "
            "Nothing was reset, cleaned or stashed",
        )


def synchronize(repo_root: Path) -> SyncResult:
    """Bring the checked-out branch up to date with its remote, safely.

    Returns the established state. Raises SyncFailure — never a partial or
    speculative sync — when safety cannot be shown.
    """
    branch = resolve_branch(repo_root)
    head_before = _out(repo_root, ["rev-parse", "HEAD"], BRANCH_STATE_FAILURE)

    fetch_branch(repo_root, branch)
    remote_head = _remote_head(repo_root, branch)
    relation = classify(repo_root, head_before, remote_head)

    if relation == RELATION_LOCAL_AHEAD:
        raise _fail(
            NON_FAST_FORWARD_LOCAL_STATE,
            f"local {branch} holds commits {REMOTE}/{branch} does not. The runner "
            "does not decide whether to push, rebase or reset that work. Push or "
            "reconcile it yourself, then re-run",
        )
    if relation == RELATION_DIVERGED:
        raise _fail(
            DIVERGED_HISTORY,
            f"local {branch} and {REMOTE}/{branch} have diverged — each holds "
            "commits the other lacks. The runner does not decide which history is "
            "correct. Reconcile them yourself, then re-run",
        )

    action = ACTION_NONE
    if relation == RELATION_REMOTE_AHEAD:
        fast_forward(repo_root, branch, head_before, remote_head)
        action = ACTION_FAST_FORWARDED

    head_after = _out(repo_root, ["rev-parse", "HEAD"], HEAD_VERIFICATION_FAILURE)
    if head_after != remote_head:
        raise _fail(
            HEAD_VERIFICATION_FAILURE,
            f"after synchronization HEAD is {head_after[:12]} but {REMOTE}/{branch} "
            f"is {remote_head[:12]}; refusing to audit an unverified state",
        )

    return SyncResult(
        branch=branch,
        remote_ref=f"{REMOTE}/{branch}",
        head_before=head_before,
        head_after=head_after,
        remote_head=remote_head,
        relation=relation,
        action=action,
    )


def capture_snapshot(repo_root: Path, result: SyncResult) -> AuditSnapshot:
    """Freeze the post-sync state the whole audit is performed against."""
    return AuditSnapshot(
        branch=result.branch,
        head=result.head_after,
        status_short=_out(repo_root, ["status", "--short"], SNAPSHOT_DRIFT),
    )
