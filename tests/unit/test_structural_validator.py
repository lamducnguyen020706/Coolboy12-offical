"""Unit tests for the Artifact 037 bootstrap structural validator.

Proves row 037's ``Val`` — *well-formedness only* — and the half of row 038's
exit-P1 clause this artifact supplies: *"envelope is 7 fields; identity parses
six partitions."*

The other half of row 037 — ``Done: refuses semantic checks by design`` — is
proved in ``tests/boundary/``, because a refusal is a boundary, and refusal
proofs of malformed input are in ``tests/negative/``, per the suite
responsibilities Artifact 010 established.

``XX`` and ``ZZ`` below are two-character codes and nothing more. The Registry
owns what a kind means (Blueprint §13.11, §9.4) and no test here asks.
"""

from __future__ import annotations

import pytest

from coolboy12.bootstrap.identity import PARTITIONS, WSV_SINGLETON, parse_identity
from coolboy12.bootstrap.validate import (
    ENVELOPE_FIELDS,
    ValidationCode,
    ValidationResult,
    validate_envelope,
    validate_identity,
)


def envelope(**overrides):
    """A well-formed envelope, with any field replaced or added."""
    base = {
        "partition": "W",
        "kind": "CH",
        "object_id": "000001",
        "slug": "Maximus",
        "provenance": None,
        "registry_ref": None,
        "sot_class": None,
    }
    base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# The envelope — exactly seven
# ---------------------------------------------------------------------------


def test_the_seven_fields_are_the_ones_the_source_freezes():
    """SOURCE-FROZEN: RMS §4, Artifact 033, row 033's ``Val``, in order."""
    assert ENVELOPE_FIELDS == (
        "partition",
        "kind",
        "object_id",
        "slug",
        "provenance",
        "registry_ref",
        "sot_class",
    )
    assert len(ENVELOPE_FIELDS) == 7
    assert "tier" not in ENVELOPE_FIELDS
    assert "status" not in ENVELOPE_FIELDS


def test_a_well_formed_envelope_validates():
    """Row 038's exit-P1 clause: *envelope is 7 fields*."""
    result = validate_envelope(envelope())

    assert result.valid
    assert bool(result) is True
    assert result.findings == ()
    assert str(result) == "VALID"


def test_the_envelope_values_beyond_the_identity_are_not_inspected():
    """Artifact 033 §9: no source establishes a type or default for any field.

    ``provenance``, ``registry_ref`` and ``sot_class`` carry whatever they
    carry. Judging them would be deciding what they ought to mean, which is the
    scope creep row 037's ``Why`` names.
    """
    for value in (None, "", 0, [], {"anything": "at all"}, object()):
        assert validate_envelope(
            envelope(provenance=value, registry_ref=value, sot_class=value)
        ).valid


# ---------------------------------------------------------------------------
# The identity — six partitions
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("partition", PARTITIONS)
def test_every_partition_validates(partition):
    """Row 038's other clause: *identity parses six partitions*."""
    assert validate_envelope(envelope(partition=partition)).valid
    assert validate_identity(parse_identity(f"{partition}-XX-000001-Example")).valid


def test_an_identity_built_by_035_validates():
    assert validate_identity(parse_identity("W-CH-000001-Maximus")).valid


def test_the_wsv_singleton_validates():
    """SOURCE-FROZEN: RMS §5 admits the singleton; 035 holds its shape."""
    assert validate_identity(WSV_SINGLETON).valid
    assert validate_envelope(
        envelope(
            partition=WSV_SINGLETON.partition,
            kind=WSV_SINGLETON.kind,
            object_id=WSV_SINGLETON.object_id,
            slug=WSV_SINGLETON.slug,
        )
    ).valid


@pytest.mark.parametrize("object_id", ["000001", "000002", "001234", "999999"])
def test_the_normal_object_id_range_validates(object_id):
    """000001..999999, the range 035 and 036 settled."""
    assert validate_envelope(envelope(object_id=object_id)).valid


# ---------------------------------------------------------------------------
# The result object
# ---------------------------------------------------------------------------


def test_a_result_carries_its_reasons_and_answers_as_a_boolean():
    good = validate_envelope(envelope())
    bad = validate_envelope(envelope(tier=4))

    assert good.valid and bool(good)
    assert not bad.valid and not bool(bad)
    assert bad.codes == (ValidationCode.UNKNOWN_ENVELOPE_FIELD,)
    assert bad.findings[0].field == "tier"
    assert "UNKNOWN_ENVELOPE_FIELD" in str(bad)


def test_a_result_is_immutable():
    result = validate_envelope(envelope())

    with pytest.raises(Exception):  # noqa: B017 - frozen dataclass
        result.findings = ()


def test_a_finding_names_the_035_rule_it_came_from():
    """The delegation is visible: 037 reports which frozen rule 035 refused."""
    finding = validate_envelope(envelope(partition="w")).findings[0]

    assert finding.code is ValidationCode.INVALID_IDENTITY_STRUCTURE
    assert finding.origin == "INVALID_PARTITION"
    assert finding.field == "partition"


def test_an_empty_result_is_the_valid_one():
    assert ValidationResult().valid
    assert ValidationResult().codes == ()
