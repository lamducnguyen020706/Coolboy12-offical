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
    Provenance,
    ProvenanceCaptureError,
    ProvenanceErrorCode,
    capture_provenance,
    provenance_from_mapping,
    provenance_to_mapping,
)

WHO = "an author"
WHEN = "2026-09-20T12:00:00Z"
WHY = "a recorded reason"


def test_the_public_constructor_cannot_bypass_validation():
    """The value type has no unvalidated back door.

    Before ``__post_init__`` existed, ``Provenance(who="", when="not-a-time",
    why="")`` constructed cleanly and rendered through the mapping helper —
    an invalid capture could enter the system without ever meeting the
    contract the factory advertised.
    """
    with pytest.raises(ProvenanceCaptureError):
        Provenance(who="", when="not-a-time", why="")


@pytest.mark.parametrize(
    ("kwargs", "code"),
    [
        ({"who": "", "when": WHEN, "why": WHY}, ProvenanceErrorCode.MISSING_DIMENSION),
        ({"who": WHO, "when": WHEN, "why": ""}, ProvenanceErrorCode.MISSING_DIMENSION),
        (
            {"who": 123, "when": WHEN, "why": WHY},
            ProvenanceErrorCode.INVALID_INPUT_TYPE,
        ),
        (
            {"who": WHO, "when": "2026-02-29T12:00:00Z", "why": WHY},
            ProvenanceErrorCode.INVALID_WHEN,
        ),
        (
            {"who": WHO, "when": "2026-09-20T12:00:60Z", "why": WHY},
            ProvenanceErrorCode.INVALID_WHEN,
        ),
        (
            {"who": WHO, "when": "not-a-time", "why": WHY},
            ProvenanceErrorCode.INVALID_WHEN,
        ),
    ],
)
def test_direct_construction_raises_the_same_codes_as_the_factory(kwargs, code):
    """One rule set, whichever construction path a caller takes."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        Provenance(**kwargs)

    assert excinfo.value.code is code


def test_direct_construction_of_a_valid_capture_succeeds():
    """Closing the back door must not close the front one."""
    provenance = Provenance(
        who="author",
        when="2026-09-20T12:00:00Z",
        why="restore intended reveal timing",
    )

    assert provenance.who == "author"
    assert provenance.when == "2026-09-20T12:00:00Z"
    assert provenance.why == "restore intended reveal timing"


def test_the_factory_and_the_constructor_agree():
    """capture_provenance is a thin wrapper, not a second rule set."""
    assert capture_provenance(who=WHO, when=WHEN, why=WHY) == Provenance(
        who=WHO, when=WHEN, why=WHY
    )


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
        "2026-09-20T12:00:00+00:00",
        "2026/09/20T12:00:00Z",
        "yesterday",
        "1758369600",
    ],
)
def test_a_lexically_wrong_instant_is_refused_not_guessed(when):
    """Layer A — the value is not in the accepted representation at all."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=WHO, when=when, why=WHY)

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_WHEN


@pytest.mark.parametrize(
    "when",
    [
        "2026-99-99T99:99:99Z",
        "2026-13-01T12:00:00Z",
        "2026-09-31T12:00:00Z",
        "2026-02-29T12:00:00Z",
        "2026-09-20T24:00:00Z",
        "2026-09-20T12:60:00Z",
        "2026-09-20T12:00:61Z",
    ],
)
def test_an_impossible_instant_is_refused(when):
    """Layer B — lexically well-formed, but not a moment that exists.

    Each of these passes the representation pattern and names no real instant.
    A regex alone accepted all seven; they are refused, never rolled forward
    into a neighbouring valid instant.
    """
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=WHO, when=when, why=WHY)

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_WHEN


def test_an_impossible_instant_does_not_leak_a_parser_error():
    """INVALID_WHEN stays the contract; no raw ValueError escapes."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=WHO, when="2026-02-29T12:00:00Z", why=WHY)

    assert excinfo.value.code is ProvenanceErrorCode.INVALID_WHEN
    assert isinstance(excinfo.value.__cause__, ValueError)


@pytest.mark.parametrize("fraction", [".1234567", ".12345678", "."])
def test_fractional_precision_beyond_the_chosen_format_is_refused(fraction):
    """The accepted format is 1-6 fractional digits; it is not widened here."""
    with pytest.raises(ProvenanceCaptureError) as excinfo:
        capture_provenance(who=WHO, when=f"2026-09-20T12:00:00{fraction}Z", why=WHY)

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


def test_heterogeneous_unknown_keys_refuse_without_leaking_a_type_error():
    """Unknown keys that cannot be compared must still refuse deterministically.

    Sorting the unknown keys raised ``TypeError: '<' not supported between
    instances of 'int' and 'NoneType'`` before this was fixed — refusing a
    fourth dimension must not itself be refusable.
    """
    payload = {"who": WHO, "when": WHEN, "why": WHY, 1: "x", None: "y"}

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    assert excinfo.value.code is ProvenanceErrorCode.UNKNOWN_DIMENSION


class _HostileKey:
    """A hashable key whose rendering raises.

    Not a production concern in itself — it exists to prove the refusal path
    never executes caller code to build its own error message.
    """

    def __hash__(self) -> int:
        return 7

    def __eq__(self, other: object) -> bool:
        return self is other

    def __repr__(self) -> str:
        raise RuntimeError("repr bomb")

    def __str__(self) -> str:
        raise RuntimeError("str bomb")


def test_a_hostile_key_cannot_break_the_refusal_path():
    """UNKNOWN_DIMENSION survives a key that refuses to be rendered.

    Rendering the offending key into the message ran the caller's __repr__
    inside the refusal, so a hostile key raised RuntimeError out of
    provenance_from_mapping instead of the promised UNKNOWN_DIMENSION. The
    diagnostic no longer touches the key.
    """
    payload = {"who": WHO, "when": WHEN, "why": WHY, _HostileKey(): "smuggled"}

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    assert excinfo.value.code is ProvenanceErrorCode.UNKNOWN_DIMENSION


def test_the_refusal_message_is_independent_of_caller_values():
    """The message is a fixed string; the code is the contract."""
    payload = {"who": WHO, "when": WHEN, "why": WHY, _HostileKey(): "x", 1: "y"}

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    # Constructing the message must not raise, and must name no key.
    assert "who, when, why" in str(excinfo.value)


@pytest.mark.parametrize("key", [1, None, True, 2.5, (), frozenset()])
def test_any_unhashable_shaped_unknown_key_is_refused(key):
    """A single non-string unknown key is refused whatever its type."""
    payload = {"who": WHO, "when": WHEN, "why": WHY, key: "smuggled"}

    with pytest.raises(ProvenanceCaptureError) as excinfo:
        provenance_from_mapping(payload)

    assert excinfo.value.code is ProvenanceErrorCode.UNKNOWN_DIMENSION


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
