"""Refusal proofs for the Artifact 050 source-of-truth classification mechanism.

Fail-closed: a missing, invalid or plural classification is refused, never
repaired, guessed, defaulted or narrowed to one. Blueprint §29.6a — *"Every data
class in the system carries exactly one of these"* — admits no other outcome.
"""

from __future__ import annotations

from enum import Enum, StrEnum

import pytest

from coolboy12.kernel.sot import (
    SourceOfTruthError,
    SourceOfTruthErrorCode,
    validate_record_source_of_truth,
    validate_source_of_truth_class,
)

MISSING = SourceOfTruthErrorCode.MISSING_SOURCE_OF_TRUTH_CLASS
INVALID = SourceOfTruthErrorCode.INVALID_SOURCE_OF_TRUTH_CLASS
MULTIPLE = SourceOfTruthErrorCode.MULTIPLE_SOURCE_OF_TRUTH_CLASSES


def _code(value: object) -> SourceOfTruthErrorCode:
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_source_of_truth_class(value)
    return excinfo.value.code


def test_dev_env_is_not_a_record_level_class():
    """DEV-ENV classifies repository paths, not records (016 §2, 033 §5.7)."""
    assert _code("DEV-ENV") is INVALID


@pytest.mark.parametrize(
    "value",
    [
        "CANON",
        "CANONICAL",
        "WORKING",
        "PRODUCTION",
        "UNKNOWN",
        "unknown",
        "DEV_ENV",
        "DEVELOPMENT",
        "CACHE",
        "SOURCE",
        "EXTERNALLY_MANAGED",
        "SYSTEM",
        "RUNTIME",
        "LOCAL",
        "CONFIG",
        "SECRET",
        "GENERATED",
        "IMPLEMENTATION",
        "anything",
    ],
)
def test_no_sixth_class_and_no_alias(value):
    """Includes every alias Artifact 016 §3 refuses by name."""
    assert _code(value) is INVALID


@pytest.mark.parametrize(
    "value",
    [
        "authoritative",
        "Derived",
        "cached",
        "Temporary",
        "external",
        "DERIVED ",
        " AUTHORITATIVE ",
        "\tCACHED",
        "AUTHORITATIVE\n",
        "",
        " ",
    ],
)
def test_case_and_whitespace_are_not_repaired(value):
    """No case-folding and no trimming: one canonical spelling."""
    assert _code(value) is INVALID


def test_none_carries_no_class():
    assert _code(None) is MISSING


@pytest.mark.parametrize(
    "value",
    [
        ["AUTHORITATIVE", "DERIVED"],
        ("AUTHORITATIVE", "DERIVED"),
        {"AUTHORITATIVE", "DERIVED"},
        frozenset({"CACHED", "TEMPORARY"}),
        {"primary": "AUTHORITATIVE", "secondary": "DERIVED"},
        ["AUTHORITATIVE", "AUTHORITATIVE"],
        ["AUTHORITATIVE", "DERIVED", "CACHED", "TEMPORARY", "EXTERNAL"],
    ],
)
def test_more_than_one_class_is_refused_and_none_is_chosen(value):
    """Shortcut F: two classes are never narrowed to the first."""
    assert _code(value) is MULTIPLE


@pytest.mark.parametrize(
    "value", [[], ["AUTHORITATIVE"], ("DERIVED",), {}, {"k": "CACHED"}]
)
def test_a_container_is_not_a_class_even_with_one_entry(value):
    assert _code(value) is INVALID


def test_another_enum_that_spells_a_class_is_refused():
    """Equality is not identity: a foreign enum is not this vocabulary."""

    class Foreign(StrEnum):
        DERIVED = "DERIVED"

    class Plain(Enum):
        AUTHORITATIVE = "AUTHORITATIVE"

    assert _code(Foreign.DERIVED) is INVALID
    assert _code(Plain.AUTHORITATIVE) is INVALID


@pytest.mark.parametrize("value", [0, 1, 1.5, True, b"DERIVED", object()])
def test_a_non_string_is_refused(value):
    assert _code(value) is INVALID


class _HostileValue:
    """Its rendering raises. Proves the refusal never renders a caller value."""

    def __repr__(self) -> str:
        raise RuntimeError("repr bomb")

    def __str__(self) -> str:
        raise RuntimeError("str bomb")


def test_a_hostile_value_cannot_break_the_refusal_path():
    assert _code(_HostileValue()) is INVALID


# --- record level ----------------------------------------------------------


def test_a_record_without_a_class_is_refused():
    """Shortcuts A and B: no class supplied is never AUTHORITATIVE or DERIVED."""
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_record_source_of_truth({})

    assert excinfo.value.code is MISSING


def test_a_record_whose_class_is_none_is_refused():
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_record_source_of_truth({"sot_class": None})

    assert excinfo.value.code is MISSING


def test_a_record_carrying_two_classes_is_refused():
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_record_source_of_truth({"sot_class": ["AUTHORITATIVE", "DERIVED"]})

    assert excinfo.value.code is MULTIPLE


@pytest.mark.parametrize(
    "key", ["source_of_truth", "source_of_truth_class", "truth_class", "SOT_CLASS"]
)
def test_only_the_envelope_spelling_is_read(key):
    """A synonym key is not the field; the record still carries no class."""
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_record_source_of_truth({key: "AUTHORITATIVE"})

    assert excinfo.value.code is MISSING


@pytest.mark.parametrize("record", [None, "AUTHORITATIVE", ["sot_class"], 7])
def test_a_record_that_is_not_a_mapping_is_refused(record):
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_record_source_of_truth(record)

    assert excinfo.value.code is SourceOfTruthErrorCode.INVALID_INPUT_TYPE
