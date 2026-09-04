"""--help output and the /audit command wrapper."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from audit_runner import pipeline
from audit_runner.errors import EXIT_SUCCESS

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def test_pipeline_help_flag_exits_zero_no_key_needed(monkeypatch):
    monkeypatch.delenv("HHTECH_API_KEY", raising=False)
    exit_code = pipeline.main(["--help"])
    assert exit_code == EXIT_SUCCESS


def test_entrypoint_script_help_runs_end_to_end():
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "hhtech" / "audit"), "--help"],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        timeout=30,
    )
    assert result.returncode == 0
    assert "usage: audit <artifact-id>" in result.stdout
    assert "HHTECH_API_KEY" in result.stdout


def test_entrypoint_script_rejects_extra_argument():
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "hhtech" / "audit"), "42", "extra"],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        timeout=30,
    )
    assert result.returncode == 1
    assert "extra" in result.stderr or "exactly one" in result.stderr


def test_command_wrapper_file_exists_and_delegates():
    wrapper = REPO_ROOT / ".claude" / "commands" / "audit.md"
    assert wrapper.is_file()
    text = wrapper.read_text(encoding="utf-8")
    assert "./hhtech/audit" in text
    # the wrapper must not reimplement the pipeline itself
    assert "hhtechapi.net" not in text
    assert "HHTECH_API_KEY" not in text or "never printed" in text.lower()
