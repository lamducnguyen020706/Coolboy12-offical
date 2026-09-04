"""Atomic writes for the two runner output files. BUILD spec §23.

write-temp -> fsync -> atomic rename. Never truncates the destination before
a successful, validated response exists.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

AUDIT_REPORT_NAME = "auditreport.md"
PATCH_PROMPT_NAME = "patchprompt.md"

_CLEARED_PATCH_PROMPT = (
    "# hhtech/patchprompt.md\n\n"
    "Cleared. The most recent audit did not return VERDICT: PATCH REQUIRED, "
    "so there is no patch prompt to generate. See hhtech/auditreport.md for "
    "the current audit result.\n"
)


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


def clear_patch_prompt(hhtech_dir: Path) -> Path:
    path = hhtech_dir / PATCH_PROMPT_NAME
    atomic_write(path, _CLEARED_PATCH_PROMPT)
    return path


def is_cleared_patch_prompt(content: str) -> bool:
    return content.strip() == _CLEARED_PATCH_PROMPT.strip()
