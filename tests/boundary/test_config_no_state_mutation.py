"""Boundary proofs for the Artifact 021 configuration loader.

Artifact 021 is ``Auth: none``. It loads execution-environment configuration
and stops there. These tests prove the forbidden edges rather than the
behaviour: that loading touches no canonical state, creates no derived state,
and reaches for no later artifact.

No canonical write is implemented in order to test its prevention. The
fixtures below hold placeholder text in a temporary directory and are never
Canon; ``canon/**`` in this repository is empty of records at P0.
"""

from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from coolboy12.bootstrap import config as config_module
from coolboy12.bootstrap.config import SecretInProtectedPathError, load_config


def _snapshot(root: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def test_loading_does_not_mutate_canonical_state(tmp_path):
    """Test E — canonical content is unchanged by a load."""
    canon = tmp_path / "canon" / "world"
    canon.mkdir(parents=True)
    record = canon / "placeholder.md"
    record.write_text("placeholder — not a Record\n", encoding="utf-8")

    before = _snapshot(tmp_path)

    load_config(
        {"COOLBOY12_LOG_LEVEL": "debug", "COOLBOY12_WORKSPACE": "src"},
        root=tmp_path,
    )

    assert _snapshot(tmp_path) == before


def test_loading_does_not_create_derived_state(tmp_path):
    """Test F — no derived store is created or updated as a side effect."""
    (tmp_path / "derived").mkdir()

    before = _snapshot(tmp_path)

    load_config({"COOLBOY12_LOG_LEVEL": "debug"}, root=tmp_path)

    assert _snapshot(tmp_path) == before
    assert list((tmp_path / "derived").iterdir()) == []


def test_refusal_writes_nothing_either(tmp_path):
    """A rejected configuration leaves the workspace exactly as it was."""
    (tmp_path / "canon").mkdir()
    before = _snapshot(tmp_path)

    with pytest.raises(SecretInProtectedPathError):
        load_config({"COOLBOY12_API_TOKEN": "canon/access.txt"}, root=tmp_path)

    assert _snapshot(tmp_path) == before


def test_loader_runs_without_the_configured_root_existing(tmp_path):
    """The zone check is lexical: it consults no filesystem.

    A path check that stat-ed the workspace would couple the loader to
    filesystem state and make it non-deterministic across environments.
    """
    absent = tmp_path / "does" / "not" / "exist"

    assert len(load_config({"COOLBOY12_A": "1"}, root=absent)) == 1


def test_module_imports_only_the_standard_library():
    """Artifact 021 declares ``H: 005,015`` and adds no dependency.

    In particular it imports nothing from a later artifact: no rebuild engine
    (020/226), no canonical-zone module (017), no hook (022), no zone
    configuration (023).
    """
    imported: set[str] = set()
    for node in ast.walk(ast.parse(inspect.getsource(config_module))):
        if isinstance(node, ast.Import):
            imported |= {alias.name.split(".")[0] for alias in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    imported.discard("__future__")

    assert imported <= {"os", "collections", "types"}


def test_module_exposes_no_canonical_write_surface():
    """No ``write_canon``-shaped entry point exists, by any name."""
    surface = {name.lower() for name in dir(config_module)}
    forbidden = (
        "write_canon",
        "save_record",
        "commit_canon",
        "write_record",
        "mutate",
        "rebuild",
        "deny",
        "enforce",
    )

    assert surface.isdisjoint(forbidden)
