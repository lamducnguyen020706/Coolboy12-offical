"""Boundary proofs for Artifact 036 — where the allocator stops.

Artifact 036 owns one decision — which ordinal is next — and holds one durable
fact. Its risk is taking on any of the responsibilities around it::

    034  grammar, frozen              ← not restated here
    035  parse · format · key         ← formatting stays there
    036  allocate · record · never reuse   ← this module
    037  structural validation        ← not duplicated here

Plus three standing boundaries: the Registry owns kind meaning (Blueprint
§13.11, §9.4), the six Record Models own their own semantics (§13.7a, I-101),
and canon changes only through the Mutation Coordinator (Spine law 2, I-83),
which is Roadmap 152 and does not exist yet.

Each boundary is proved behaviourally where it can be and statically against
the module's own source where it cannot. The static checks are not a lint pass;
they name the specific things Artifact 036 must not contain.
"""

from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from coolboy12.bootstrap import ordinal as ordinal_module
from coolboy12.bootstrap.identity import (
    MAX_ORDINAL,
    MIN_ORDINAL,
    WSV_SINGLETON,
    format_object_id,
)
from coolboy12.bootstrap.ordinal import (
    OrdinalAllocationError,
    OrdinalAllocator,
    OrdinalErrorCode,
)

SOURCE = Path(inspect.getsourcefile(ordinal_module)).read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)


def _code_literals() -> set[str]:
    """Every string literal in the module except its docstrings.

    The module docstring explains why the allocation record may not live in
    ``canon/**`` or ``derived/**``, so a raw substring search over the source
    finds those words in prose that exists precisely to keep them out. Only a
    literal the code actually uses can send a write somewhere.
    """
    docstrings = set()
    for node in ast.walk(TREE):
        if isinstance(
            node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            first = node.body[0] if node.body else None
            if (
                isinstance(first, ast.Expr)
                and isinstance(first.value, ast.Constant)
                and isinstance(first.value.value, str)
            ):
                docstrings.add(id(first.value))

    return {
        node.value
        for node in ast.walk(TREE)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and id(node) not in docstrings
    }


@pytest.fixture
def allocator(tmp_path):
    return OrdinalAllocator.create(tmp_path / "ordinals.json")


# ---------------------------------------------------------------------------
# Non-reuse is structural, not merely enforced
# ---------------------------------------------------------------------------


def test_no_public_operation_can_release_an_ordinal():
    """The reuse path does not exist, so it cannot be reintroduced by accident.

    Artifact 036 does not own the record lifecycle (a retirement is somebody
    else's event), and it deliberately offers no way to be told that an ordinal
    is free. The proof is the API surface: nothing here frees, releases,
    retires, resets, rolls back, or assigns a frontier.
    """
    forbidden = (
        "release", "free", "retire", "reset", "rollback", "reclaim",
        "delete", "remove", "clear", "rewind", "decrement", "set_",
    )  # fmt: skip
    public = [
        name
        for name in dir(OrdinalAllocator)
        if not name.startswith("_") or name in {"__init__"}
    ]

    assert not [n for n in public if any(word in n.lower() for word in forbidden)]
    assert sorted(n for n in public if not n.startswith("_")) == [
        "allocate",
        "create",
        "highest_allocated",
        "namespaces",
        "record_path",
    ]


def test_the_frontier_is_read_only_with_no_setter():
    """``highest_allocated`` reads; there is no companion that writes."""
    assert not hasattr(OrdinalAllocator, "set_highest_allocated")
    assert isinstance(
        inspect.getattr_static(OrdinalAllocator, "highest_allocated"),
        type(lambda: None),
    )


def test_a_frontier_never_decreases_across_any_sequence_of_calls(allocator):
    """Whatever the interleaving, the number only goes up."""
    seen = 0
    for index in range(50):
        allocator.allocate("W", "CH")
        if index % 3 == 0:
            allocator.allocate("E", "CH")
        frontier = allocator.highest_allocated("W", "CH")
        assert frontier > seen
        seen = frontier


def test_the_module_carries_no_reclamation_vocabulary():
    """Static half of the non-reuse boundary."""
    names = {
        node.name
        for node in ast.walk(TREE)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }
    forbidden = ("release", "free", "reclaim", "recycle", "retire", "rollback", "reset")

    assert not [n for n in names if any(word in n.lower() for word in forbidden)]


# ---------------------------------------------------------------------------
# 035 — formatting stays there
# ---------------------------------------------------------------------------


def test_the_allocator_returns_an_ordinal_not_a_formatted_identity(allocator):
    """036 owns which ordinal; 035 owns how it is written."""
    ordinal = allocator.allocate("W", "CH")

    assert isinstance(ordinal, int)
    assert not isinstance(ordinal, str)
    assert format_object_id(ordinal) == "000001"


def test_the_module_does_not_reimplement_object_id_formatting():
    """No second six-digit convention, and no competing formatter."""
    assert "zfill" not in SOURCE
    assert ":06" not in SOURCE
    assert "%06" not in SOURCE
    assert "def format_object_id" not in SOURCE
    assert not [n for n in dir(ordinal_module) if n.startswith("format_")]


def test_the_range_is_taken_from_035_and_not_restated():
    """A second copy of the bounds is a second copy that can drift."""
    assert ordinal_module.MIN_ORDINAL is MIN_ORDINAL
    assert ordinal_module.MAX_ORDINAL is MAX_ORDINAL
    assert not [t for t in _code_literals() if "999999" in t or "999_999" in t]
    assert not [
        node
        for node in ast.walk(TREE)
        if isinstance(node, ast.Constant) and node.value == MAX_ORDINAL
    ]
    # MIN_ORDINAL is 1, and a bare 1 in this module is the record version or an
    # increment rather than a restated floor, so identity above is the proof
    # that both bounds come from 035 — not a hunt for the digit.


def test_the_singleton_kind_code_is_taken_from_035_and_not_restated():
    """``WS`` lives in exactly one module in the repository.

    Artifact 035 holds it, derived from Blueprint §13.9a's kind table and RMS
    §8.1's frozen roster. 036 reads it rather than repeating it, so the code
    cannot come to mean two things.
    """
    literals = {
        node.value
        for node in ast.walk(TREE)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    codes = {t for t in literals if len(t) == 2 and t.isascii() and t.isupper()}

    assert codes == set()
    assert ordinal_module._SINGLETON_NAMESPACE == (
        WSV_SINGLETON.partition,
        WSV_SINGLETON.kind,
    )


def test_035_remains_stateless_while_036_holds_the_state(allocator):
    """The formatter is not consulted about what comes next, and cannot be."""
    assert format_object_id(7) == format_object_id(7) == "000007"

    allocator.allocate("W", "CH")
    assert format_object_id(7) == "000007"


# ---------------------------------------------------------------------------
# Registry, Record Models, 037
# ---------------------------------------------------------------------------


def test_allocation_needs_no_kind_meaning(allocator):
    """``CH`` is a namespace key. The Registry owns what it means."""
    assert allocator.allocate("W", "CH") == 1
    assert allocator.allocate("W", "ZQ") == 1
    assert allocator.allocate("I", "QQ") == 1


def test_the_module_imports_only_the_standard_library_and_035():
    """Row 036's hard dependency is 035, and that is the only one taken."""
    imported = set()
    for node in ast.walk(TREE):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)

    project = {name for name in imported if name.startswith("coolboy12")}
    assert project == {"coolboy12.bootstrap.identity"}

    stdlib = {n for n in imported if not n.startswith("coolboy12")}
    assert stdlib <= {
        "__future__",
        "json",
        "os",
        "contextlib",
        "dataclasses",
        "enum",
        "pathlib",
        "typing",
        "collections.abc",
    }


def test_no_registry_and_no_record_model_is_reached():
    for forbidden in (
        "registry",
        "world",
        "epistemic",
        "production",
        "visual",
        "issue",
    ):
        assert f"import {forbidden}" not in SOURCE.lower()
        assert f"coolboy12.{forbidden}" not in SOURCE.lower()


def test_the_structural_validator_is_neither_imported_nor_anticipated():
    """037 owns structural validation; 036 checks only what allocation needs."""
    assert "coolboy12.bootstrap.validate" not in SOURCE
    assert not hasattr(ordinal_module, "validate")
    assert not [n for n in ordinal_module.__all__ if "valid" in n.lower()]


def test_the_allocator_is_not_a_parser(allocator):
    """It takes a namespace, never an identity string.

    Handing it a formatted identity is not a supported call; parsing belongs
    to 035, and 036 does no more checking than allocation safety needs.
    """
    with pytest.raises(OrdinalAllocationError) as raised:
        allocator.allocate("W-CH-000001-Maximus", "CH")

    assert raised.value.code is OrdinalErrorCode.INVALID_NAMESPACE
    assert not [n for n in dir(ordinal_module) if n.startswith("parse")]


# ---------------------------------------------------------------------------
# Storage — an allocation record, not a Record store
# ---------------------------------------------------------------------------


def test_the_record_holds_allocation_metadata_and_nothing_else(allocator, tmp_path):
    """Row 036 is ``CD: no``: no canonical data, no Record, no payload."""
    import json

    allocator.allocate("W", "CH")
    state = json.loads((tmp_path / "ordinals.json").read_text(encoding="utf-8"))

    assert set(state) == {"version", "namespaces"}
    assert set(state["namespaces"][0]) == {"partition", "kind", "highest_allocated"}
    for absent in ("slug", "provenance", "registry_ref", "sot_class", "tier", "status"):
        assert absent not in (tmp_path / "ordinals.json").read_text(encoding="utf-8")


def test_the_record_path_is_required_and_never_implicit():
    """No default path, so this module claims no zone in the Artifact 001 tree.

    No source names a home for authoritative non-canonical state, so 036 does
    not pick one — see the module docstring, which reports that as an open
    item rather than resolving it.
    """
    signature = inspect.signature(OrdinalAllocator.__init__)
    assert signature.parameters["record_path"].default is inspect.Parameter.empty

    zones = ("canon", "derived", "reports", "fixtures", "/tmp", "/var", "src/")
    used_as_code = [
        text for text in _code_literals() if any(zone in text for zone in zones)
    ]
    assert used_as_code == []


def test_nothing_is_written_outside_the_record_and_its_lock(tmp_path):
    """Allocation touches two paths, both beside the record it was given."""
    record = tmp_path / "ordinals.json"
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")
    allocator.allocate("E", "CH")

    assert sorted(p.name for p in tmp_path.iterdir()) == ["ordinals.json"]


def test_the_allocator_commits_no_canon():
    """Spine law 2: canon changes only through the Mutation Coordinator.

    That is Roadmap 152 and does not exist. 036 has ``Auth: allocating`` — it
    decides an ordinal, and that is the whole of its authority.
    """
    imported = {
        node.module
        for node in ast.walk(TREE)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    assert not [m for m in imported if "mutation" in m or "canon" in m]

    assert not [n for n in dir(ordinal_module) if "commit" in n.lower()]
    assert not [text for text in _code_literals() if "canon" in text.lower()]


# ---------------------------------------------------------------------------
# The invariant under stress
# ---------------------------------------------------------------------------


def test_no_ordinal_is_ever_repeated_within_a_namespace(allocator):
    issued = [allocator.allocate("W", "CH") for _ in range(500)]

    assert issued == sorted(issued)
    assert len(set(issued)) == 500
    assert issued[0] == MIN_ORDINAL


def test_namespaces_never_leak_into_one_another(allocator):
    pairs = [
        ("W", "CH"),
        ("W", "CO"),
        ("E", "CH"),
        ("P", "XX"),
        ("R", "ZZ"),
        ("V", "AA"),
    ]
    for _ in range(10):
        for partition, kind in pairs:
            allocator.allocate(partition, kind)

    assert {allocator.highest_allocated(p, k) for p, k in pairs} == {10}


def test_reopening_the_record_between_every_call_changes_nothing(tmp_path):
    """The frontier lives on disk, so an instance is never the source of truth."""
    record = tmp_path / "ordinals.json"
    OrdinalAllocator.create(record)

    issued = [OrdinalAllocator(record).allocate("W", "CH") for _ in range(20)]

    assert issued == list(range(1, 21))
