"""Refusal proofs for the Artifact 047 provenance capture mechanism.

Test E of row 047's obligations: malformed or unusable input fails explicitly
rather than being silently repaired into a different meaning. Nothing here is
a Record and nothing here is canonical.

The governing reason these are refusals rather than repairs is Blueprint §10
law 9 — *"No anonymous canon; a change with no recorded reason is an audit
flag."* A fabricated provenance is worse than a refused one.
"""

from __future__ import annotations

import pytest

from coolboy12.kernel.provenance import (
    ProvenanceCaptureError,
    ProvenanceErrorCode,
    capture_provenance,
    provenance_from_mapping,
    provenance_to_mapping,
)

WHO = "an author"
WHEN = "2026-09-20T12:00:00Z"
WHY = "a recorded reason"


@pytest.mark.parametrize("dimension", ["who", "when", "why"])
def test_an_empty_dimension_is_refused_not_defaulted(dimension):
    """No dimension is silently substituted, including ``why``."""
    argument = {"who": WHO, "when": WHEN, "why": WHY} | {dimension: ""}

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(**argument)

    assert excinfo.value.code is ProvenanceErrorCode.MISSING_DIMENSION
    assert excinfo.value.dimension == dimension


@pytest.mark.parametrize("dimension", ["who", "when", "why"])
def test_a_missing_dimension_cannot_be_omitted(dimension):
    """All three are required arguments; none carries a default."""
    argument = {"who": WHO, "when": WHEN, "why": WHY}
    del argument[dimension]

    with pytest.raises(TypeError):
        capture_provenance(**argument)


@pytest.mark.parametrize("value", [None, 1, 1.0, [], {}, object()])
def test_non_text_is_refused(value):
    """A dimension that is not text is refused rather than coerced."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=value, when=WHEN, why=WHY)

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_INPUT_TYPE


@pytest.mark.parametrize(
    "when",
    [
        "2026-09-20",
        "2026-09-20 12:00:00",
        "2026-09-20T12:00:00",
        "2026-09-20T12:00:00+07:00",
        "yesterday",
        "1758369600",
    ],
)
def test_an_unusable_instant_is_refused_not_guessed(when):
    """``when`` is never inferred, parsed loosely, or replaced by the clock."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=WHO, when=when, why=WHY)

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_WHEN


def test_surrounding_whitespace_is_refused_rather_than_stripped():
    """Normalising would edit what the caller said happened."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=f"  {WHO}  ", when=WHEN, why=WHY)

    assert excinfo.value.code is ProvenanceErrorCode.MISSING_DIMENSION


@pytest.mark.parametrize(
    "extra",
    ["history", "audit", "revision", "version", "lineage", "approved_by", "session"],
)
def test_a_fourth_dimension_cannot_be_smuggled_through_a_mapping(extra):
    """Provenance cannot grow a fourth dimension by round-tripping storage."""
    payload = {"who": WHO, "when": WHEN, "why": WHY, extra: "smuggled"}

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    assert excinfo.value.code is ProvenanceErrorCode.UNKNOWN_DIMENSION


@pytest.mark.parametrize("dimension", ["who", "when", "why"])
def test_a_mapping_missing_a_dimension_is_refused(dimension):
    """An incomplete stored capture is refused, never completed by guess."""
    payload = {"who": WHO, "when": WHEN, "why": WHY}
    del payload[dimension]

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    assert excinfo.value.code is ProvenanceErrorCode.MISSING_DIMENSION
    assert excinfo.value.dimension == dimension


@pytest.mark.parametrize("payload", [None, "who", 1, ["who"], object()])
def test_a_non_mapping_is_refused(payload):
    """Rebuilding from something that is not a mapping fails explicitly."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_INPUT_TYPE


def test_rendering_a_non_provenance_is_refused():
    """The renderer will not accept an arbitrary object."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_to_mapping({"who": WHO, "when": WHEN, "why": WHY})

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_INPUT_TYPE
