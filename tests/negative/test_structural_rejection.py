"""Rejection proofs for the Artifact 037 structural validator.

Row 037's ``Val`` is *well-formedness only*, and this suite is the half that
refuses. Every structural rule 037 enforces is proved to report, with the code
that names it — so a rule cannot quietly stop being checked while the
positive suite still passes.

The eighth-field case gets the most attention here for the reason row 033
gives: *"the historical failure point — any eighth field universalizes a
semantic."*
"""

from __future__ import annotations

import pytest

from coolboy12.bootstrap.validate import (
    ENVELOPE_FIELDS,
    ValidationCode,
    validate_envelope,
    validate_identity,
)


def envelope(**overrides):
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
# The eighth field
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "eighth",
    ["tier", "status", "knowledge_state", "canonical", "lifecycle", "anything"],
)
def test_an_eighth_field_is_refused(eighth):
    """SOURCE-FROZEN: exactly seven, and no eighth (RMS §4, Artifact 033).

    ``tier`` and ``status`` are named individually rather than left to
    arithmetic, because they are the two the sources single out: World Record
    Model properties whose universalization row 033 calls the historical
    failure point.
    """
    result = validate_envelope(envelope(**{eighth: "whatever"}))

    assert not result.valid
    assert result.codes == (ValidationCode.UNKNOWN_ENVELOPE_FIELD,)
    assert result.findings[0].field == eighth


def test_several_extra_fields_are_all_reported():
    """A caller fixing an envelope should see every extra field at once."""
    result = validate_envelope(envelope(tier=4, status="CANON"))

    assert [f.field for f in result.findings] == ["status", "tier"]
    assert set(result.codes) == {ValidationCode.UNKNOWN_ENVELOPE_FIELD}


# ---------------------------------------------------------------------------
# A missing field
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("absent", ENVELOPE_FIELDS)
def test_a_missing_universal_field_is_refused(absent):
    """*Exactly* seven cuts both ways: six is not an envelope either."""
    partial = {k: v for k, v in envelope().items() if k != absent}
    result = validate_envelope(partial)

    assert not result.valid
    assert ValidationCode.MISSING_ENVELOPE_FIELD in result.codes
    assert absent in [f.field for f in result.findings]


def test_an_empty_mapping_reports_all_seven():
    result = validate_envelope({})

    assert len(result.findings) == 7
    assert set(result.codes) == {ValidationCode.MISSING_ENVELOPE_FIELD}
    assert sorted(f.field for f in result.findings) == sorted(ENVELOPE_FIELDS)


# ---------------------------------------------------------------------------
# The identity components, delegated to 035
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("override", "origin"),
    [
        ({"partition": "w"}, "INVALID_PARTITION"),
        ({"partition": "X"}, "INVALID_PARTITION"),
        ({"partition": "WW"}, "INVALID_PARTITION"),
        ({"kind": "ch"}, "INVALID_KIND"),
        ({"kind": "C"}, "INVALID_KIND"),
        ({"kind": "CHA"}, "INVALID_KIND"),
        ({"object_id": "1"}, "INVALID_OBJECT_ID"),
        ({"object_id": "00001"}, "INVALID_OBJECT_ID"),
        ({"object_id": "1000000"}, "INVALID_OBJECT_ID"),
        ({"slug": ""}, "INVALID_SLUG"),
        ({"slug": "_Maximus"}, "INVALID_SLUG"),
        ({"slug": "Maximus_"}, "INVALID_SLUG"),
        ({"slug": "Maximus__Great"}, "INVALID_SLUG"),
        ({"slug": "Maximus The Great"}, "INVALID_SLUG"),
        ({"slug": "Maximus!"}, "INVALID_SLUG"),
        ({"slug": "Maximus-The-Great"}, "INVALID_SEPARATOR"),
    ],
)
def test_a_malformed_identity_component_is_refused(override, origin):
    """037 reports; 035 decides. The ``origin`` names the rule that was broken.

    037 states no rule of its own here — every one of these is Artifact 035's,
    reached by construction rather than restated.
    """
    result = validate_envelope(envelope(**override))

    assert not result.valid
    assert ValidationCode.INVALID_IDENTITY_STRUCTURE in result.codes
    assert result.findings[0].origin == origin


@pytest.mark.parametrize(
    ("partition", "kind"),
    [("W", "CH"), ("W", "CO"), ("E", "WS"), ("R", "XX"), ("V", "WS"), ("I", "WS")],
)
def test_the_singleton_marker_outside_the_singleton_is_refused(partition, kind):
    """``000000`` is the WSV marker and is well-formed nowhere else.

    The rule is the *pair*: ``WS`` in another partition is an ordinary code,
    and it is the combination that carries the marker, not the kind alone.
    """
    result = validate_envelope(
        envelope(partition=partition, kind=kind, object_id="000000")
    )

    assert not result.valid
    assert result.findings[0].origin == "INVALID_WSV"
    assert result.findings[0].field == "object_id"


@pytest.mark.parametrize("component", ["partition", "kind", "object_id", "slug"])
@pytest.mark.parametrize("value", [None, 7, ["W"], object()])
def test_a_component_of_the_wrong_runtime_type_is_refused_by_035(component, value):
    """037 has no type system of its own, and this proves it.

    A component that is not a string is refused — but the refusal comes back
    with Artifact 035's own code in ``origin``, because 037 asked 035 rather
    than deciding. There is no ``isinstance`` check, no width rule and no
    regular expression anywhere in 037 that could have produced this; if 035
    ever changes how it refuses, 037 forwards the new answer unchanged.
    """
    result = validate_envelope(envelope(**{component: value}))

    assert not result.valid
    assert result.codes == (ValidationCode.INVALID_IDENTITY_STRUCTURE,)
    assert result.findings[0].origin == "INVALID_INPUT_TYPE"
    assert result.findings[0].field == component


def test_the_wrong_type_refusal_reaches_the_identity_entry_point_too():
    """Same delegation, through :func:`validate_identity`."""

    class WrongTypes:
        partition = None
        kind = 7
        object_id = ("000001",)  # a tuple: still not a str, and not mutable
        slug = object()

    result = validate_identity(WrongTypes())

    assert result.codes == (ValidationCode.INVALID_IDENTITY_STRUCTURE,)
    assert result.findings[0].origin == "INVALID_INPUT_TYPE"


def test_an_object_that_only_resembles_a_mapping_is_refused():
    """037 DECISION: the input contract is a ``Mapping``, checked as one.

    The refusal is about input shape alone. It changes no rule about which
    keys matter, and inspects no value.
    """

    class LooksLikeAMapping:
        def keys(self):
            return envelope().keys()

        def __getitem__(self, key):
            return envelope()[key]

    result = validate_envelope(LooksLikeAMapping())

    assert result.codes == (ValidationCode.INVALID_INPUT_TYPE,)
    assert "Mapping" in result.findings[0].detail


def test_a_malformed_identity_is_refused_on_its_own_too():
    """Not only inside an envelope — the identity entry point refuses as well."""

    class Loose:
        partition = "w"
        kind = "CH"
        object_id = "000001"
        slug = "Maximus"

    result = validate_identity(Loose())

    assert not result.valid
    assert result.codes == (ValidationCode.INVALID_IDENTITY_STRUCTURE,)


# ---------------------------------------------------------------------------
# Input that is not the shape being asked about
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("value", [None, 42, "W-CH-000001-Maximus", object()])
def test_something_that_is_not_an_identity_is_refused(value):
    """A raw string is not an identity here — parsing is Artifact 035's."""
    result = validate_identity(value)

    assert not result.valid
    assert result.codes == (ValidationCode.INVALID_INPUT_TYPE,)


@pytest.mark.parametrize("value", [None, 42, ["partition"], "partition", object()])
def test_something_that_is_not_a_mapping_is_refused(value):
    result = validate_envelope(value)

    assert not result.valid
    assert result.codes == (ValidationCode.INVALID_INPUT_TYPE,)


def test_an_identity_missing_a_component_is_refused():
    class Partial:
        partition = "W"
        kind = "CH"

    result = validate_identity(Partial())

    assert not result.valid
    assert result.codes == (ValidationCode.INVALID_INPUT_TYPE,)
    assert result.findings[0].field == "object_id"


def test_the_same_invalid_input_always_produces_the_same_result():
    """Determinism: no ordering, no state, no environment."""
    bad = envelope(tier=4, status="X", partition="w")
    results = [str(validate_envelope(bad)) for _ in range(20)]

    assert len(set(results)) == 1
