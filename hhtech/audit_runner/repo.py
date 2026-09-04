"""Repository root resolution.

Resolves robustly rather than assuming $PWD, per BUILD spec §41: uses
`git rev-parse --show-toplevel` from the runner script's own location, so
the runner works correctly however it is invoked.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from .errors import InputError


def find_repo_root(start: Path) -> Path:
    """Return the git repository root containing `start`."""
    try:
        result = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise InputError(f"could not resolve repository root: {exc}") from exc
    if result.returncode != 0:
        raise InputError(
            f"not inside a git repository (from {start}): "
            f"{result.stderr.strip()}"
        )
    root = result.stdout.strip()
    if not root:
        raise InputError(f"git rev-parse returned no repository root for {start}")
    return Path(root)
