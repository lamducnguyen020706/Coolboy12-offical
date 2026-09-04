"""Commit/push firewall. BUILD spec §25-29.

The runner stages and commits exactly hhtech/auditreport.md and
hhtech/patchprompt.md. Never `git add .` / `git add -A` / `git commit -am`.
Never touches unrelated working-tree state. Never force-pushes. Never
rewrites history.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from .errors import GitSafetyFailure
from .gitstate import get_staged_names

_TIMEOUT = 30

ALLOWED_PATHS = ("hhtech/auditreport.md", "hhtech/patchprompt.md")


def _run(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", "-C", str(repo_root), *args],
            capture_output=True, text=True, timeout=_TIMEOUT, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GitSafetyFailure(f"git {' '.join(args)} failed: {exc}") from exc


def snapshot_other_paths(repo_root: Path) -> str:
    """git status --short, with the two runner output paths filtered out —
    used to detect a concurrent change to anything else (BUILD spec §29)."""
    result = _run(repo_root, ["status", "--short"])
    if result.returncode != 0:
        raise GitSafetyFailure(f"git status failed: {result.stderr.strip()}")
    lines = [
        line for line in result.stdout.splitlines()
        if not any(line.endswith(p) for p in ALLOWED_PATHS)
    ]
    return "\n".join(lines)


def stage_outputs(repo_root: Path) -> None:
    result = _run(repo_root, ["add", "--", *ALLOWED_PATHS])
    if result.returncode != 0:
        raise GitSafetyFailure(f"git add failed: {result.stderr.strip()}")


def validate_staged(repo_root: Path, baseline_staged: tuple[str, ...]) -> tuple[str, ...]:
    """Assert the current staged set is a subset of baseline ∪ ALLOWED_PATHS.
    If anything else is staged, unstage exactly what this runner staged and
    raise — never commit an unexpected file (BUILD spec §25).
    """
    current = get_staged_names(repo_root)
    allowed = set(baseline_staged) | set(ALLOWED_PATHS)
    unexpected = [p for p in current if p not in allowed]
    if unexpected:
        _run(repo_root, ["restore", "--staged", "--", *ALLOWED_PATHS])
        raise GitSafetyFailure(
            f"staging firewall tripped — unexpected path(s) staged: {unexpected}. "
            "Unstaged the runner's own additions and aborted before commit."
        )
    return current


def commit(repo_root: Path, message: str) -> str | None:
    """Pathspec-limited commit of exactly ALLOWED_PATHS, regardless of what
    else is staged or modified in the working tree. Returns the new commit
    hash, or None if there was nothing to commit (identical content).
    """
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
