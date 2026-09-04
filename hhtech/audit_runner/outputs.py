"""Atomic writes for the two runner output files.

Every audit run overwrites BOTH files. There is no "clear" state and no
stale-output state: a patchprompt is generated for every verdict, so the two
files are always a matched pair describing the same run.

Writes are atomic — temp file in the destination directory, fsync, atomic
rename — so a crashed run never leaves a half-written report, and neither
destination is truncated before validated content exists to replace it.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

AUDIT_REPORT_NAME = "auditreport.md"
PATCH_PROMPT_NAME = "patchprompt.md"

AUDIT_REPORT_REL = f"hhtech/{AUDIT_REPORT_NAME}"
PATCH_PROMPT_REL = f"hhtech/{PATCH_PROMPT_NAME}"


def atomic_write(path: Path, content: str) -> None:
    directory = path.parent
    directory.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=str(directory), prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def write_audit_report(hhtech_dir: Path, content: str) -> Path:
    path = hhtech_dir / AUDIT_REPORT_NAME
    atomic_write(path, content)
    return path


def write_patch_prompt(hhtech_dir: Path, content: str) -> Path:
    path = hhtech_dir / PATCH_PROMPT_NAME
    atomic_write(path, content)
    return path
