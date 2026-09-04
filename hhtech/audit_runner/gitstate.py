"""Git state collection. Tier 5 — fact, never architecture.

BUILD spec §10: for a brand-new artifact, `git diff` may be empty; the
runner must still read the actual target files from disk (sources.py does
that from Roadmap-derived scope, not from the diff).
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from .errors import InputError

_TIMEOUT = 15


def _run(repo_root: Path, args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), *args],
            capture_output=True, text=True, timeout=_TIMEOUT, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise InputError(f"git {' '.join(args)} failed: {exc}") from exc
    if result.returncode != 0:
        raise InputError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


@dataclass(frozen=True)
class GitState:
    branch: str
    head: str
    status_short: str
    diff_name_status: str
    diff_stat: str
    diff: str
    untracked: tuple[str, ...]


def collect_git_state(repo_root: Path) -> GitState:
    branch = _run(repo_root, ["branch", "--show-current"]).strip()
    if not branch:
        raise InputError(
            "HEAD is detached or the branch could not be determined; "
            "the runner requires a checked-out branch to push to"
        )
    head = _run(repo_root, ["rev-parse", "HEAD"]).strip()
    status_short = _run(repo_root, ["status", "--short"])
    diff_name_status = _run(repo_root, ["diff", "--name-status"])
    diff_stat = _run(repo_root, ["diff", "--stat"])
    diff = _run(repo_root, ["diff"])
    untracked_raw = _run(
        repo_root, ["ls-files", "--others", "--exclude-standard"]
    )
    untracked = tuple(line for line in untracked_raw.splitlines() if line)

    return GitState(
        branch=branch, head=head, status_short=status_short,
        diff_name_status=diff_name_status, diff_stat=diff_stat, diff=diff,
        untracked=untracked,
    )


def get_staged_names(repo_root: Path) -> tuple[str, ...]:
    out = _run(repo_root, ["diff", "--cached", "--name-only"])
    return tuple(line for line in out.splitlines() if line)
