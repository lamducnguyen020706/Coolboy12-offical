"""Unit tests for the Artifact 047 provenance capture mechanism.

Proves row 047's ``Val`` — *captures who/when/why; meaning left to models* —
and its ``Done`` — *capture only*. Refusal proofs live in ``tests/negative/``
and boundary proofs in ``tests/boundary/``, per the suite responsibilities
Artifact 010 established.

Nothing below is a Record and nothing below is canonical. The ``who`` and
``why`` strings are opaque text: no test asserts a meaning for either, because
provenance meaning is model-owned (RMS §6) and Artifact 048 states that
boundary.
"""

from __future__ import annotations

import json

import pytest

from coolboy12.kernel.provenance import (
    PROVENANCE_DIMENSIONS,
    Provenance,
    ProvenanceCaptureError,
    ProvenanceErrorCode,
    capture_provenance,
    provenance_from_mapping,
    provenance_to_mapping,
)

WHO = "an author"
WHEN = "2026-09-20T12:00:00Z"
WHY = "recorded because law 9 requires a reason"


def test_a_valid_capture_succeeds():
    """Test A — basic capture."""
    provenance = capture_provenance(who=WHO, when=WHEN, why=WHY)

    assert isinstance(provenance, Provenance)


def test_b_all_three_dimensions_survive_capture():
    """Test B — who, when and why are each preserved, none dropped."""
    provenance = capture_provenance(who=WHO, when=WHEN, why=WHY)

    assert provenance.who == WHO
    assert provenance.when == WHEN
    assert provenance.why == WHY


@pytest.mark.parametrize(
    "when",
    [
        "2026-09-20T12:00:00Z",
        "2026-09-20T12:00:00.1Z",
        "2026-09-20T12:00:00.12Z",
        "2026-09-20T12:00:00.123Z",
        "2026-09-20T12:00:00.1234Z",
        "2026-09-20T12:00:00.12345Z",
        "2026-09-20T12:00:00.123456Z",
        "2024-02-29T00:00:00Z",
        "2026-12-31T23:59:59Z",
    ],
)
def test_a_real_instant_in_the_accepted_format_is_captured(when):
    """Valid instants across the format's range, including a real leap day."""
    assert capture_provenance(who=WHO, when=when, why=WHY).when == when


def test_b_capture_preserves_values_byte_for_byte():
    """No normalisation: a capture records what the caller said, unedited."""
    why = "because  of   irregular internal spacing"
    provenance = capture_provenance(who=WHO, when=WHEN, why=why)

    assert provenance.why == why


def test_c_capture_adds_no_semantic_enrichment():
    """Test C — 047 adds no history, audit, revision, version or lineage."""
    provenance = capture_provenance(who=WHO, when=WHEN, why=WHY)

    forbidden = (
        "history",
        "audit",
        "revision",
        "version",
        "lineage",
        "derivation",
        "approval",
        "approved_by",
        "cause",
        "session",
        "world_time",
        "issue_ordinal",
        "authority",
        "canonical",
    )
    for name in forbidden:
        assert not hasattr(provenance, name), f"047 grew a {name!r} dimension"


def test_c_the_three_dimensions_are_the_whole_value():
    """The captured value carries the three source dimensions and no fourth."""
    assert PROVENANCE_DIMENSIONS == ("who", "when", "why")
    assert set(provenance_to_mapping(capture_provenance(
        who=WHO, when=WHEN, why=WHY
    ))) == set(PROVENANCE_DIMENSIONS)


def test_d_capture_requires_no_eighth_envelope_field():
    """Test D — the envelope stays seven fields (RMS §4, Artifact 033).

    A capture is a value carried *by* the existing ``provenance`` field. This
    module exports no envelope, no Record, and no field beyond it.
    """
    import coolboy12.kernel.provenance as module

    exported = set(module.__all__)
    envelope_fields = {
        "partition",
        "kind",
        "object_id",
        "slug",
        "registry_ref",
        "sot_class",
    }
    assert exported.isdisjoint(envelope_fields)
    assert not any("envelope" in name.lower() for name in exported)


def test_f_capture_is_model_neutral():
    """Test F — capture takes no partition, kind, Record or Record Model.

    The mechanism cannot branch on W/E/P/R/V/I because it is never told which
    one it is serving.
    """
    import inspect

    signature = inspect.signature(capture_provenance)
    assert list(signature.parameters) == ["who", "when", "why"]


def test_f_identical_input_captures_identically_for_every_caller():
    """No caller identity, partition or kind changes what is captured."""
    first = capture_provenance(who=WHO, when=WHEN, why=WHY)
    second = capture_provenance(who=WHO, when=WHEN, why=WHY)

    assert first == second


def test_round_trip_through_a_mapping_is_lossless():
    """capture → mapping → capture returns an equal value."""
    original = capture_provenance(who=WHO, when=WHEN, why=WHY)

    restored = provenance_from_mapping(provenance_to_mapping(original))

    assert restored == original


def test_round_trip_through_json_is_lossless():
    """The mapping crosses a JSON boundary without semantic loss."""
    original = capture_provenance(who=WHO, when=WHEN, why=WHY)

    restored = provenance_from_mapping(
        json.loads(json.dumps(provenance_to_mapping(original)))
    )

    assert restored == original


def test_a_captured_value_is_immutable():
    """A capture states a moment that has passed; it is not edited in place."""
    provenance = capture_provenance(who=WHO, when=WHEN, why=WHY)

    with pytest.raises((AttributeError, TypeError)):
        provenance.why = "a different reason"  # type: ignore[misc]


def test_error_codes_are_branchable_without_reading_messages():
    """The code is the contract; the message is not."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=WHO, when=WHEN, why="")

    assert excinfo.value.code is ProvenanceErrorCode.MISSING_DIMENSION
    assert excinfo.value.dimension == "why"
