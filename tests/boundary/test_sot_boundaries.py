"""Boundary proofs for the Artifact 050 source-of-truth classification mechanism.

Two boundaries. First, classification is explicit: Blueprint §29.6a makes the
class *"part of its definition rather than a property of how it happens to be
stored"*, so nothing about a record's location, partition or model may decide
it. Second, 050 classifies and stops: canonicality (052), authority (051),
derived-state discipline (053) and any Record base type (§13.7a) are not here.

Where practical these are structural checks of the module itself.
"""

from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from coolboy12.kernel import sot
from coolboy12.kernel.sot import (
    SourceOfTruthClass,
    SourceOfTruthError,
    SourceOfTruthErrorCode,
    validate_record_source_of_truth,
)

SOURCE = Path(sot.__file__).read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)


# --- classification is explicit, never inferred from storage ----------------


@pytest.mark.parametrize(
    "place",
    [
        {"path": "derived/index/search.json"},
        {"path": "canon/world/W-CH-000001-Arthur.md"},
        {"path": "cache/render/page-1.png"},
        {"path": "tmp/working/draft.md"},
        {"path": "external/service/result.json"},
        {"directory": "derived/", "filename": "projection.json"},
        {"partition": "W", "kind": "CH"},
        {"model": "Registry"},
    ],
)
def test_where_a_record_sits_never_supplies_a_missing_class(place):
    """Shortcuts C and D: a record under derived/ is not thereby DERIVED."""
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_record_source_of_truth(place)

    assert excinfo.value.code is SourceOfTruthErrorCode.MISSING_SOURCE_OF_TRUTH_CLASS


def test_where_a_record_sits_never_overrides_its_declared_class():
    """A record declared AUTHORITATIVE stays AUTHORITATIVE under a derived/ path."""
    record = {"path": "derived/projection.json", "sot_class": "AUTHORITATIVE"}

    assert validate_record_source_of_truth(record) is SourceOfTruthClass.AUTHORITATIVE


def test_no_public_function_takes_a_location_model_or_kind():
    location_words = {
        "path",
        "directory",
        "dir",
        "filename",
        "location",
        "store",
        "partition",
        "model",
        "kind",
        "backend",
    }
    for name in sot.__all__:
        obj = getattr(sot, name)
        if inspect.isfunction(obj):
            assert location_words.isdisjoint(inspect.signature(obj).parameters), name


def test_the_module_imports_nothing_that_could_look_at_storage():
    """Standard library only, and no filesystem, network, process or database access.

    Also rules out an import cycle: 050 imports no coolboy12 module at all.
    """
    imported = set()
    for node in ast.walk(TREE):
        if isinstance(node, ast.Import):
            imported |= {alias.name.split(".")[0] for alias in node.names}
        elif isinstance(node, ast.ImportFrom):
            imported.add((node.module or "").split(".")[0])

    assert imported <= {"__future__", "collections", "enum", "typing"}, imported


def test_validation_does_not_write_to_the_record():
    record = {"sot_class": "DERIVED", "slug": "unchanged"}
    before = dict(record)

    validate_record_source_of_truth(record)

    assert record == before


# --- 050 classifies and stops ----------------------------------------------


@pytest.mark.parametrize(
    "fragment",
    [
        "canon",
        "authority",
        "authorize",
        "rebuild",
        "promote",
        "commit",
        "persist",
        "store",
        "write",
        "record_base",
        "baserecord",
        "universalrecord",
    ],
)
def test_no_public_name_reaches_beyond_classification(fragment):
    """Shortcuts G, H and I: no canonical flag, no promotion, no rebuild."""
    public = [name for name in dir(sot) if not name.startswith("_")]

    assert not [name for name in public if fragment in name.lower()], fragment


def test_no_class_is_defined_for_records_to_inherit():
    """Shortcut J: no Record base type (§13.7a). Only the vocabulary and the error."""
    classes = {node.name for node in ast.walk(TREE) if isinstance(node, ast.ClassDef)}

    assert classes == {
        "SourceOfTruthClass",
        "SourceOfTruthErrorCode",
        "SourceOfTruthError",
    }


def test_no_class_is_promoted_or_mapped_to_another():
    """Every accepted value comes back as itself; EXTERNAL is never AUTHORITATIVE."""
    for member in SourceOfTruthClass:
        assert sot.validate_source_of_truth_class(member.value) is member

    assert (
        sot.validate_source_of_truth_class("EXTERNAL")
        is not SourceOfTruthClass.AUTHORITATIVE
    )


def test_the_vocabulary_carries_no_canonicality():
    """AUTHORITATIVE says where a fact lives, not that it is canon (I-104)."""
    assert not [name for name in dir(SourceOfTruthClass) if "canon" in name.lower()]
