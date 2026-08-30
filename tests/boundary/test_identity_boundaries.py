"""Boundary proofs for Artifact 035 — where the parser stops.

Artifact 035 sits between a frozen grammar and three artifacts that do not
exist yet, and its whole risk is leaking into them::

    034  grammar, frozen          ← not restated here
    035  parse · format · key     ← this module
    036  ordinal allocation       ← must not happen here
    037  structural validation    ← must not be duplicated here

Plus two standing boundaries: the Registry owns kind meaning (Blueprint
§13.11, §9.4), and Record resolution belongs to a Record resolver (Blueprint
§9.4), not to this layer.

A boundary that is not tested is a boundary that erodes, so each is proved
twice where it can be: behaviourally, and statically against the module's own
source and namespace. The static checks are deliberately not a lint pass —
they name the specific things Artifact 035 must not contain.
"""

from __future__ import annotations

import ast
import dataclasses
import inspect
from pathlib import Path

import pytest

from coolboy12.bootstrap import identity as identity_module
from coolboy12.bootstrap.identity import (
    PARTITIONS,
    WSV_SINGLETON_IDENTITY,
    format_object_id,
    parse_identity,
    resolve_identity,
)

SOURCE = Path(inspect.getsourcefile(identity_module)).read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)


# ---------------------------------------------------------------------------
# 036 — no allocation
# ---------------------------------------------------------------------------


def test_parsing_allocates_nothing_and_carries_no_state():
    """Parsing an identity brings nothing into existence.

    The same call, a thousand times, yields the same object identity and never
    advances a counter — because there is no counter. Which ordinal comes
    next, and how non-reuse survives a restart, is Artifact 036's.
    """
    first = parse_identity("W-CH-000001-Maximus")
    for _ in range(1000):
        assert parse_identity("W-CH-000001-Maximus") == first


def test_formatting_an_ordinal_is_representation_not_allocation():
    """``format_object_id`` never chooses; it only renders what it was given."""
    assert [format_object_id(1) for _ in range(5)] == ["000001"] * 5
    assert format_object_id(7) == "000007"
    assert format_object_id(7) == "000007"


def test_the_module_holds_no_mutable_state():
    """Nothing at module level can be advanced, appended to, or reassigned.

    A parser that kept a mutable container would be one edit away from being
    an allocator.
    """
    mutable = {
        name: value
        for name, value in vars(identity_module).items()
        if not name.startswith("__") and isinstance(value, (list, dict, set, bytearray))
    }

    assert mutable == {}


def test_the_singleton_marker_is_unreachable_from_the_ordinal_formatter():
    """036 can never allocate the reserved marker through this module."""
    for ordinal in (0, -1, 1_000_000):
        with pytest.raises(Exception):  # noqa: B017 - refusal is the point
            format_object_id(ordinal)

    assert all(format_object_id(n) != "000000" for n in (1, 2, 999_998, 999_999))


def test_no_allocation_vocabulary_appears_in_the_module():
    """Static half of the 036 boundary."""
    names = {
        node.name
        for node in ast.walk(TREE)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }
    forbidden = ("allocate", "reserve", "mint", "next_ordinal", "counter", "ledger")

    assert not [
        name for name in names if any(word in name.lower() for word in forbidden)
    ]


# ---------------------------------------------------------------------------
# Registry — no kind meaning
# ---------------------------------------------------------------------------


def test_parsing_needs_no_kind_mapping():
    """A kind code is syntactic data; the Registry owns what it means.

    ``CH`` parses without anyone having said what ``CH`` is, and so does a
    code no source has ever stated.
    """
    assert parse_identity("W-CH-000001-Maximus").kind == "CH"
    assert parse_identity("W-ZQ-000001-Example").kind == "ZQ"
    assert parse_identity("I-QQ-000001-Example").kind == "QQ"


def test_the_module_embeds_no_kind_roster():
    """Static half of the Registry boundary.

    Every string literal in the module is inspected, rather than its prose:
    the only two-character uppercase code the module may *hold as data* is
    ``WS``, and only to reserve the singleton marker's one legal home. A
    roster creeping in would show up here as a second code.
    """
    literals = {
        node.value
        for node in ast.walk(TREE)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    codes = {
        text
        for text in literals
        if len(text) == 2 and text.isascii() and text.isupper()
    }

    assert codes == {"WS"}


def test_no_mapping_from_a_kind_code_to_a_meaning_exists():
    """No dict anywhere in the module keys a two-character code."""
    for node in ast.walk(TREE):
        if not isinstance(node, ast.Dict):
            continue
        keys = [k.value for k in node.keys if isinstance(k, ast.Constant)]
        assert not [
            k for k in keys if isinstance(k, str) and len(k) == 2 and k.isupper()
        ]


def test_the_module_imports_nothing_outside_the_standard_library():
    """Registry-independent, Record-independent, dependency-free.

    Artifact 005 declares no runtime dependency, and row 035's hard dependency
    is 034 — a document. Nothing here reaches a later artifact either.
    """
    imported = set()
    for node in ast.walk(TREE):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])

    assert imported <= {"__future__", "re", "dataclasses", "enum", "typing"}
    assert "coolboy12" not in imported


# ---------------------------------------------------------------------------
# Record resolution — the narrow boundary
# ---------------------------------------------------------------------------


def test_resolution_stops_at_the_identity_components():
    """Blueprint §9.4 puts reference resolution with a Record resolver.

    What comes back is three strings. It is not a Record of any of the six
    models, carries no payload, and reached no storage to be produced.
    """
    key = resolve_identity("W-CH-000001-Maximus")
    fields = [field.name for field in dataclasses.fields(key)]

    assert fields == ["partition", "kind", "object_id"]
    assert {type(getattr(key, name)) for name in fields} == {str}


def test_the_slug_is_never_a_resolution_key():
    """Blueprint §13.9a: *nothing resolves, matches, or validates against a slug.*"""
    keys = {
        resolve_identity(f"W-CH-000001-{slug}")
        for slug in ("Maximus", "Maximus_New", "MAXIMUS", "Something_Else_Entirely")
    }

    assert len(keys) == 1


def test_the_singleton_slug_is_written_but_never_enforced():
    """Even the reserved singleton does not validate against its slug."""
    assert WSV_SINGLETON_IDENTITY.endswith("-WorldStateVariables")
    assert parse_identity("W-WS-000000-AnythingElse").object_id == "000000"


def test_nothing_in_the_module_touches_storage_or_the_environment():
    """No filesystem, no network, no clock, no process state."""
    forbidden = (
        "open(",
        "Path(",
        "os.",
        "socket",
        "requests",
        "urllib",
        "sqlite",
        "time.",
    )

    for token in forbidden:
        assert token not in SOURCE, f"{token} appears in the module"


# ---------------------------------------------------------------------------
# 034 and 037 — neither restated nor pre-empted
# ---------------------------------------------------------------------------


def test_the_frozen_grammar_is_implemented_exactly_as_034_states_it():
    """Six single-character partitions, two-character kinds, four elements."""
    assert PARTITIONS == ("W", "E", "P", "R", "V", "I")
    assert all(len(partition) == 1 for partition in PARTITIONS)

    identity = parse_identity("W-CH-000001-Maximus")
    assert len(identity.kind) == 2
    assert [field.name for field in dataclasses.fields(identity)] == [
        "partition",
        "kind",
        "object_id",
        "slug",
    ]


def test_the_module_does_not_reach_for_the_structural_validator():
    """037 owns structural validation; 035 must not import or anticipate it."""
    assert "coolboy12.bootstrap.validate" not in SOURCE
    assert not hasattr(identity_module, "validate")

    public = [name for name in identity_module.__all__ if "valid" in name.lower()]
    assert public == []


def test_no_seventh_identity_component_and_no_envelope_field():
    """Artifact 033's envelope fields are not identity components."""
    identity = parse_identity("W-CH-000001-Maximus")
    fields = {field.name for field in dataclasses.fields(identity)}

    assert fields == {"partition", "kind", "object_id", "slug"}
    for absent in ("provenance", "registry_ref", "sot_class", "tier", "status"):
        assert absent not in fields
        assert not hasattr(identity, absent)


def test_the_module_performs_no_unicode_normalization():
    """No NFC, NFKC, casefold, transliteration or silent case change."""
    for token in (
        "unicodedata",
        "normalize",
        "casefold",
        ".upper()",
        ".lower()",
        ".title()",
    ):
        assert token not in SOURCE, f"{token} appears in the module"
