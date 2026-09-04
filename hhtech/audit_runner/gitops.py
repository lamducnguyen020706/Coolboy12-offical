"""Commit/push firewall.

The runner may commit exactly two paths and nothing else, ever. It never
runs `git add .`, `git add -A`, or `git commit -am`; never resets, cleans,
checks out, or stashes; never rewrites history; never force-pushes.

Two independent layers enforce this:

  1. the staged set is compared for EXACT equality against the two output
     paths (plus whatever the user had already staged before the run), and
     anything unexpected aborts after unstaging only what the runner staged;
  2. the commit itself is pathspec-limited to the two files, so even a
     bookkeeping error cannot sweep an unrelated change into the commit.

Unrelated working-tree work — source, tests, docs, reports — is left
exactly as the user left it.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from .errors import GitSafetyFailure
from .gitstate import get_staged_names
from .outputs import AUDIT_REPORT_REL, PATCH_PROMPT_REL

_TIMEOUT = 30

ALLOWED_PATHS = (AUDIT_REPORT_REL, PATCH_PROMPT_REL)


def _run(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", "-C", str(repo_root), *args],
            capture_output=True, text=True, timeout=_TIMEOUT, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GitSafetyFailure(f"git {' '.join(args)} failed: {exc}") from exc


def stage_outputs(repo_root: Path) -> None:
    result = _run(repo_root, ["add", "--", *ALLOWED_PATHS])
    if result.returncode != 0:
        raise GitSafetyFailure(f"git add failed: {result.stderr.strip()}")


def unstage_outputs(repo_root: Path) -> None:
    """Unstage only the runner's own paths, never the user's."""
    _run(repo_root, ["restore", "--staged", "--", *ALLOWED_PATHS])


def assert_index_committable(repo_root: Path) -> None:
    """Preflight: refuse before the API calls if the index already holds work
    the runner may not commit.

    Nothing is unstaged here — the user's staged work is theirs. The run
    simply refuses, so a paid audit is never spent on a run that could not
    have committed anyway.
    """
    unexpected = sorted(set(get_staged_names(repo_root)) - set(ALLOWED_PATHS))
    if unexpected:
        raise GitSafetyFailure(
            f"the index already contains staged path(s) the runner may not "
            f"commit: {unexpected}. The runner commits only "
            f"{list(ALLOWED_PATHS)}. Nothing was unstaged and no audit was run "
            "— commit or unstage that work, then re-run."
        )


def validate_staged(repo_root: Path) -> tuple[str, ...]:
    """The firewall: `git diff --cached --name-only` may contain nothing but
    the two output paths.

    Anything else — whether the runner staged it or the user had it staged
    before the run — aborts. The runner unstages only its own two paths and
    leaves every unrelated staged change exactly where it was, so no user
    work is lost.

    Returns the runner's staged paths, which may be a strict subset of
    ALLOWED_PATHS when an output file's content is unchanged, or empty when
    neither changed.
    """
    current = get_staged_names(repo_root)
    unexpected = sorted(set(current) - set(ALLOWED_PATHS))
    if unexpected:
        unstage_outputs(repo_root)
        raise GitSafetyFailure(
            f"staging firewall tripped — the index contains path(s) the runner "
            f"may not commit: {unexpected}. Unstaged only the runner's own two "
            "output paths and aborted before commit; unrelated staged work was "
            "left exactly as it was."
        )
    return tuple(sorted(current))


def commit(repo_root: Path, message: str) -> str | None:
    """Pathspec-limited commit of exactly ALLOWED_PATHS. Returns the new
    commit hash, or None when there was nothing to commit."""
    result = _run(repo_root, ["commit", "-m", message, "--", *ALLOWED_PATHS])
    if result.returncode != 0:
        combined = (result.stdout + result.stderr).lower()
        if "nothing to commit" in combined or "no changes added to commit" in combined:
            return None
        raise GitSafetyFailure(f"git commit failed: {result.stderr.strip()}")
    head = _run(repo_root, ["rev-parse", "HEAD"])
    if head.returncode != 0:
        raise GitSafetyFailure("commit appeared to succeed but HEAD could not be read")
    return head.stdout.strip()


def push_current_branch(repo_root: Path, expected_branch: str) -> None:
    """Push the branch that is actually checked out — never a hardcoded one,
    never with --force."""
    current = _run(repo_root, ["branch", "--show-current"]).stdout.strip()
    if current != expected_branch:
        raise GitSafetyFailure(
            f"branch changed during the run (was {expected_branch!r}, now "
            f"{current!r}); refusing to push"
        )
    result = _run(repo_root, ["push", "-u", "origin", expected_branch])
    if result.returncode != 0:
        raise GitSafetyFailure(
            f"git push to origin/{expected_branch} failed: {result.stderr.strip()}"
        )


def build_commit_message(artifact_id: str) -> str:
    return f"audit: refresh Artifact {artifact_id} audit outputs"
