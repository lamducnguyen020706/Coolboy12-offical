"""Repository root resolution — anchored on the runner's own location.

The runner must resolve the same repository root however it is invoked:

    /repo/hhtech/audit 042
    cd /repo/docs && ../hhtech/audit 042

so resolution never consults the process working directory. The anchor is
this module's own file (``<root>/hhtech/audit_runner/repo.py``), validated
against `git rev-parse --show-toplevel` run *from that anchor*.

Fail closed: if the anchor is not inside a git repository, or the resolved
root does not carry the runner's own tree, the runner refuses rather than
guessing.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from .errors import InputError

_TIMEOUT = 10

# Markers that prove a candidate directory really is the COOLBOY12 repository
# root that this runner belongs to, rather than an unrelated parent.
_RUNNER_MARKERS = ("hhtech/audit_runner", "hhtech/standards")


def _git_toplevel(start: Path) -> Path | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=_TIMEOUT,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise InputError(f"could not resolve repository root: {exc}") from exc
    if result.returncode != 0:
        return None
    root = result.stdout.strip()
    return Path(root) if root else None


def _has_runner_markers(candidate: Path) -> bool:
    return all((candidate / marker).is_dir() for marker in _RUNNER_MARKERS)


def runner_anchor() -> Path:
    """The directory the runner package lives in: ``<root>/hhtech``."""
    return Path(__file__).resolve().parent.parent


def find_repo_root(anchor: Path | None = None) -> Path:
    """Resolve the repository root from the runner's own location.

    `anchor` exists for tests and for callers that deliberately target a
    different checkout; it is never taken from the process CWD.
    """
    start = (anchor or runner_anchor()).resolve()
    if not start.exists():
        raise InputError(f"runner anchor does not exist: {start}")

    toplevel = _git_toplevel(start if start.is_dir() else start.parent)
    if toplevel is None:
        raise InputError(
            f"not inside a git repository (anchored at {start}); the runner "
            "requires a git checkout to read repository state and to push"
        )

    if _has_runner_markers(toplevel):
        return toplevel

    # The git toplevel exists but does not carry the runner tree — e.g. the
    # runner package was vendored into a subdirectory of another repository.
    # Walk up from the anchor looking for the marker set, staying inside the
    # git toplevel, and fail closed rather than guessing.
    for candidate in [start, *start.parents]:
        if _has_runner_markers(candidate):
            return candidate
        if candidate == toplevel:
            break

    raise InputError(
        f"resolved git root {toplevel} does not contain the runner tree "
        f"({', '.join(_RUNNER_MARKERS)}); refusing to guess a repository root"
    )
