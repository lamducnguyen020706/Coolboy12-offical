"""Git state and regression baseline. Tier 5 — fact, never architecture.

Everything here is read-only. The runner never mutates the working tree to
collect evidence: no reset, no checkout, no clean, no stash. The HEAD copy
of a target file is read with `git show`, which touches nothing on disk.

A brand-new artifact legitimately has an empty diff and no HEAD baseline;
that is reported as a distinct state, not as a failure.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from .errors import InputError

_TIMEOUT = 20


def _run(repo_root: Path, args: list[str], *, check: bool = True) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), *args],
            capture_output=True, text=True, timeout=_TIMEOUT, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise InputError(f"git {' '.join(args)} failed: {exc}") from exc
    if result.returncode != 0:
        if check:
            raise InputError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
        return ""
    return result.stdout


@dataclass(frozen=True)
class FileBaseline:
    """A target file compared against its committed state."""

    path: str
    tracked: bool
    exists_on_disk: bool
    head_content: str | None
    changed_since_head: bool
    diff_vs_head: str


@dataclass(frozen=True)
class GitState:
    branch: str
    head: str
    status_short: str
    diff_name_status: str
    diff_stat: str
    diff: str
    staged_name_status: str
    staged_diff: str
    untracked: tuple[str, ...]
    baselines: tuple[FileBaseline, ...]

    @property
    def has_uncommitted_changes(self) -> bool:
        return bool(self.status_short.strip())


def collect_git_state(repo_root: Path, target_paths: tuple[str, ...] = ()) -> GitState:
    branch = _run(repo_root, ["branch", "--show-current"]).strip()
    if not branch:
        raise InputError(
            "HEAD is detached or the branch could not be determined; "
            "the runner requires a checked-out branch to push to"
        )
    head = _run(repo_root, ["rev-parse", "HEAD"]).strip()
    untracked_raw = _run(repo_root, ["ls-files", "--others", "--exclude-standard"])

    return GitState(
        branch=branch,
        head=head,
        status_short=_run(repo_root, ["status", "--short"]),
        diff_name_status=_run(repo_root, ["diff", "--name-status"]),
        diff_stat=_run(repo_root, ["diff", "--stat"]),
        diff=_run(repo_root, ["diff"]),
        staged_name_status=_run(repo_root, ["diff", "--cached", "--name-status"]),
        staged_diff=_run(repo_root, ["diff", "--cached"]),
        untracked=tuple(line for line in untracked_raw.splitlines() if line),
        baselines=collect_baselines(repo_root, target_paths),
    )


def collect_baselines(
    repo_root: Path, target_paths: tuple[str, ...]
) -> tuple[FileBaseline, ...]:
    """Read the committed (HEAD) state of each target file, without touching
    the working tree. An untracked file reports tracked=False rather than
    being mistaken for an unchanged one."""
    baselines: list[FileBaseline] = []
    for rel_path in target_paths:
        on_disk = (repo_root / rel_path).is_file()
        listed = _run(
            repo_root, ["ls-files", "--error-unmatch", "--", rel_path], check=False
        ).strip()
        tracked = bool(listed)

        head_content: str | None = None
        if tracked:
            head_content = _run(repo_root, ["show", f"HEAD:{rel_path}"], check=False) or None

        diff_vs_head = (
            _run(repo_root, ["diff", "HEAD", "--", rel_path], check=False) if tracked else ""
        )
        baselines.append(
            FileBaseline(
                path=rel_path,
                tracked=tracked,
                exists_on_disk=on_disk,
                head_content=head_content,
                changed_since_head=bool(diff_vs_head.strip()) or not tracked,
                diff_vs_head=diff_vs_head,
            )
        )
    return tuple(baselines)


def get_staged_names(repo_root: Path) -> tuple[str, ...]:
    out = _run(repo_root, ["diff", "--cached", "--name-only"])
    return tuple(line for line in out.splitlines() if line)
