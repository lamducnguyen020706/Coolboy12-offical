"""CLI entry point: ./hhtech/audit as a standalone command.

The runner is a standalone CLI. It must not depend on a Claude Code custom
command, and it must resolve the same repository root from any working
directory.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
from audit_runner import pipeline
from audit_runner import repo as repo_module
from audit_runner.errors import EXIT_INPUT_ERROR, EXIT_SUCCESS

REAL_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ENTRY_POINT = REAL_REPO_ROOT / "hhtech" / "audit"


def _run_entry(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ENTRY_POINT), *args],
        capture_output=True, text=True, cwd=str(cwd), timeout=60, check=False,
    )


# ---------------------------------------------------------------------------
# The entry point itself
# ---------------------------------------------------------------------------

def test_entry_point_exists_and_is_executable():
    assert ENTRY_POINT.is_file()
    assert ENTRY_POINT.stat().st_mode & 0o111, "hhtech/audit must be executable"


def test_entry_point_delegates_to_the_pipeline_and_holds_no_logic():
    text = ENTRY_POINT.read_text()
    assert "audit_runner.pipeline" in text
    assert "main(sys.argv[1:])" in text
    for leaked in ("hhtechapi.net", "git commit", "VERDICT:", "chat/completions"):
        assert leaked not in text, f"entry point must not implement {leaked!r} itself"


def test_no_claude_custom_command_dependency():
    """The architecture is a standalone CLI: no .claude/commands/audit.md,
    and nothing in the runner may reference one."""
    assert not (REAL_REPO_ROOT / ".claude" / "commands" / "audit.md").exists()

    runner_dir = REAL_REPO_ROOT / "hhtech" / "audit_runner"
    for source_file in [*runner_dir.glob("*.py"), ENTRY_POINT]:
        assert ".claude/commands" not in source_file.read_text(), (
            f"{source_file.name} references a Claude custom command"
        )


def test_help_runs_without_an_api_key(monkeypatch):
    monkeypatch.delenv("HHTECH_API_KEY", raising=False)
    assert pipeline.main(["--help"]) == EXIT_SUCCESS


def test_help_via_the_real_entry_point():
    result = _run_entry("--help", cwd=REAL_REPO_ROOT)
    assert result.returncode == 0
    assert "usage: audit <artifact-id>" in result.stdout
    assert "HHTECH_API_KEY" in result.stdout
    assert "PASS" in result.stdout and "BLOCKED" in result.stdout


def test_help_documents_that_every_verdict_writes_a_patchprompt():
    result = _run_entry("--help", cwd=REAL_REPO_ROOT)
    assert "NO PATCH REQUIRED" in result.stdout
    assert "DO NOT PATCH" in result.stdout
    assert "EVERY verdict" in result.stdout


@pytest.mark.parametrize(
    "args,expected_fragment",
    [
        ([], "usage"),
        (["foo"], "not a valid artifact ID"),
        (["0"], "out of range"),
        (["491"], "out of range"),
        (["42", "extra"], "exactly one artifact ID"),
    ],
)
def test_invalid_arguments_rejected_by_the_entry_point(args, expected_fragment):
    result = _run_entry(*args, cwd=REAL_REPO_ROOT)
    assert result.returncode == EXIT_INPUT_ERROR
    assert expected_fragment in result.stderr


# ---------------------------------------------------------------------------
# Working-directory independence
# ---------------------------------------------------------------------------

def test_repo_root_resolves_from_the_runner_anchor_not_the_cwd(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    assert repo_module.find_repo_root() == REAL_REPO_ROOT


def test_repo_root_identical_from_nested_directories(monkeypatch):
    monkeypatch.chdir(REAL_REPO_ROOT / "docs")
    from_docs = repo_module.find_repo_root()
    monkeypatch.chdir(REAL_REPO_ROOT / "hhtech" / "standards")
    from_standards = repo_module.find_repo_root()
    assert from_docs == from_standards == REAL_REPO_ROOT


def test_entry_point_behaves_identically_from_a_nested_directory():
    from_root = _run_entry("--help", cwd=REAL_REPO_ROOT)
    from_nested = _run_entry("--help", cwd=REAL_REPO_ROOT / "docs" / "sources")
    assert from_root.returncode == from_nested.returncode == 0
    assert from_root.stdout == from_nested.stdout


def test_repo_root_rejects_a_non_repository_anchor(tmp_path):
    from audit_runner.errors import InputError

    with pytest.raises(InputError):
        repo_module.find_repo_root(tmp_path / "does-not-exist")


def test_repo_root_requires_the_runner_tree(tmp_path):
    """A git repo without hhtech/audit_runner is not this runner's root."""
    from audit_runner.errors import InputError

    from .conftest import git

    stray = tmp_path / "stray"
    stray.mkdir()
    git(stray, "init", "-b", "main")
    with pytest.raises(InputError) as exc:
        repo_module.find_repo_root(stray)
    assert "runner tree" in str(exc.value)
