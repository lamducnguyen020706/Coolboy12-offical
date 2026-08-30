"""Rejection proofs for the Artifact 035 identity parser.

Row 035's ``Val`` states *rejects malformed*. This suite is that clause: every
rule the parser enforces is proved to refuse, with the specific
:class:`IdentityErrorCode` that names it, so a rule cannot silently stop being
enforced while the positive tests still pass.

Nothing here is repaired, normalized, padded or folded. A refusal is the whole
behaviour under test — a parser that quietly fixed its input would return an
identity the caller never supplied.
"""

from __future__ import annotations

import pytest

from coolboy12.bootstrap.identity import (
    MAX_ORDINAL,
    Identity,
    IdentityErrorCode,
    IdentityParseError,
    format_identity,
    format_object_id,
    parse_identity,
    resolve_identity,
)


def _refusal(value):
    """Parse ``value``, require a refusal, and hand back the error."""
    with pytest.raises(IdentityParseError) as raised:
        parse_identity(value)
    return raised.value


@pytest.mark.parametrize(
    "value",
    ["w-CH-000001-Maximus", "e-XX-000001-Example", "i-XX-000001-Example"],
)
def test_lowercase_partition_is_refused_not_uppercased(value):
    """035 DECISION: canonicalization is not mutation.

    ``w`` is not quietly promoted to ``W``. The identity is refused, and the
    caller learns which rule refused it.
    """
    assert _refusal(value).code is IdentityErrorCode.INVALID_PARTITION


@pytest.mark.parametrize(
    "value",
    [
        "X-CH-000001-Maximus",  # not one of the six
        "Q-XX-000001-Example",  # not one of the six
        "WW-CH-000001-Maximus",  # two characters is the KIND rule, not this one
        "Ww-CH-000001-Maximus",
        "-CH-000001-Maximus",  # empty partition
    ],
)
def test_a_partition_outside_the_six_is_refused(value):
    """Blueprint §13.9a fixes the enum at six; a seventh code names nothing."""
    assert _refusal(value).code is IdentityErrorCode.INVALID_PARTITION


@pytest.mark.parametrize(
    "value",
    [
        "W-ch-000001-Maximus",  # lowercase
        "W-Ch-000001-Maximus",  # mixed case
        "W-C-000001-Maximus",  # one character
        "W-CHA-000001-Maximus",  # three characters
        "W-CHAR-000001-Maximus",
        "W--000001-Maximus",  # empty kind
        "W-C1-000001-Maximus",  # not two uppercase letters
    ],
)
def test_a_kind_that_is_not_two_uppercase_characters_is_refused(value):
    """SOURCE-FROZEN: *"Kind codes are two characters, frozen"* (§13.11)."""
    assert _refusal(value).code is IdentityErrorCode.INVALID_KIND


@pytest.mark.parametrize(
    "value",
    [
        "W-CH-1-Maximus",
        "W-CH-01-Maximus",
        "W-CH-00001-Maximus",  # five digits
        "W-CH-0000001-Maximus",  # seven digits
        "W-CH-1000000-Maximus",  # above the range, seven digits
        "W-CH--Maximus",  # empty
        "W-CH-00000a-Maximus",
        "W-CH-٠٠٠٠٠١-Maximus",  # Arabic-Indic digits: not ASCII decimal
    ],
)
def test_a_noncanonical_object_id_is_refused_never_padded(value):
    """035 DECISION: exactly six ASCII decimal digits, and no silent padding.

    ``"1"`` does not become ``"000001"``. Deciding which ordinal a short
    string meant is exactly the invention this module must not perform.
    """
    assert _refusal(value).code is IdentityErrorCode.INVALID_OBJECT_ID


def test_a_signed_or_hexadecimal_object_id_is_refused():
    """``+``, ``-`` and ``0x`` are not part of the representation.

    A leading ``-`` is caught earlier, as a separator: the grammar reserves
    the hyphen, so the string simply has too many components.
    """
    assert _refusal("W-CH-+00001-Maximus").code is IdentityErrorCode.INVALID_OBJECT_ID
    assert _refusal("W-CH-0x0001-Maximus").code is IdentityErrorCode.INVALID_OBJECT_ID
    assert _refusal("W-CH--000001-Maximus").code is IdentityErrorCode.INVALID_SEPARATOR


@pytest.mark.parametrize(
    "value",
    [
        "W-CH-000000-Maximus",  # right partition, wrong kind
        "W-XX-000000-Example",
        "E-WS-000000-Example",  # right kind code, wrong partition
        "R-XX-000000-Example",
    ],
)
def test_the_reserved_marker_is_refused_outside_the_singleton(value):
    """``000000`` is the singleton marker and is legal nowhere else.

    It is not ordinal #0 — no ordinal #0 exists — so it can never stand in for
    a normal allocated identity.
    """
    assert _refusal(value).code is IdentityErrorCode.INVALID_WSV


def test_the_marker_is_refused_on_a_structured_identity_too():
    """The rule holds on construction, not only on parsing."""
    with pytest.raises(IdentityParseError) as raised:
        Identity(partition="W", kind="CH", object_id="000000", slug="Maximus")

    assert raised.value.code is IdentityErrorCode.INVALID_WSV


def test_a_hyphen_inside_a_slug_is_refused_and_never_escaped():
    """The hyphen is the structural separator and has no second role.

    No escaping scheme exists — not ``%2D``, not a backslash, not a doubled
    delimiter — so an identity carrying one is refused outright.
    """
    error = _refusal("W-CH-000001-Maximus-The-Great")

    assert error.code is IdentityErrorCode.INVALID_SEPARATOR


def test_too_few_components_is_an_arity_failure():
    """Four elements, in order (Blueprint §13.9a). Three is not an identity."""
    assert _refusal("W-CH-000001").code is IdentityErrorCode.INVALID_ARITY
    assert _refusal("W-CH").code is IdentityErrorCode.INVALID_ARITY
    assert _refusal("").code is IdentityErrorCode.INVALID_ARITY
    assert _refusal("W_CH_000001_Maximus").code is IdentityErrorCode.INVALID_ARITY


def test_an_empty_slug_is_refused():
    """035 DECISION: there is no empty-slug representation."""
    assert _refusal("W-CH-000001-").code is IdentityErrorCode.INVALID_SLUG


@pytest.mark.parametrize(
    "value",
    [
        "W-CH-000001-_Maximus",  # leading
        "W-CH-000001-Maximus_",  # trailing
        "W-CH-000001-Maximus__Great",  # repeated
        "W-CH-000001-_",
    ],
)
def test_an_underscore_used_as_anything_but_a_word_separator_is_refused(value):
    """035 DECISION: ``_`` stands for a space *between two slug words*.

    It is not arbitrary punctuation, so it may not lead, trail, or double —
    each of those would be an underscore with no word on one side of it.
    """
    assert _refusal(value).code is IdentityErrorCode.INVALID_SLUG


@pytest.mark.parametrize(
    "value",
    [
        "W-CH-000001-Maximus The Great",  # internal spaces
        "W-CH-000001- Maximus",  # inside the component, not around the identity
        "W-CH-000001-Maximus\tThe",
        "W-CH-000001-Max imus",
    ],
)
def test_internal_whitespace_is_refused_not_trimmed(value):
    """035 DECISION, stated explicitly rather than left accidental.

    Surrounding whitespace is trimmed; whitespace inside a component is not.
    A space between slug words is written ``_``, so a literal space in the
    serialized form is a malformed identity — and silently deleting it would
    hand back a slug the caller did not write.
    """
    assert _refusal(value).code is IdentityErrorCode.INVALID_SLUG


def test_trimming_reaches_the_outside_only():
    """The two halves of the rule, side by side."""
    assert (
        parse_identity("   W-CH-000001-Maximus_The_Great   ").slug
        == "Maximus_The_Great"
    )
    assert (
        _refusal("W-CH-000001-Maximus The Great").code is IdentityErrorCode.INVALID_SLUG
    )


@pytest.mark.parametrize("value", [None, 42, b"W-CH-000001-Maximus", ["W"], object()])
def test_a_non_string_input_is_refused_never_coerced(value):
    """``str(value)`` would invent an identity out of a repr."""
    with pytest.raises(IdentityParseError) as raised:
        parse_identity(value)

    assert raised.value.code is IdentityErrorCode.INVALID_INPUT_TYPE


def test_resolution_refuses_a_non_identity():
    with pytest.raises(IdentityParseError) as raised:
        resolve_identity(42)

    assert raised.value.code is IdentityErrorCode.INVALID_INPUT_TYPE


def test_the_formatter_refuses_invalid_components_rather_than_repairing_them():
    """A formatter that corrects its input is a second, hidden parser."""

    class Loose:
        """Bypasses :class:`Identity`'s own construction checks on purpose."""

        partition = "w"
        kind = "ch"
        object_id = "1"
        slug = "Maximus The Great"

    with pytest.raises(IdentityParseError) as raised:
        format_identity(Loose())

    assert raised.value.code is IdentityErrorCode.INVALID_PARTITION


@pytest.mark.parametrize("ordinal", [0, -1, MAX_ORDINAL + 1, 1_000_000])
def test_format_object_id_refuses_an_ordinal_outside_the_range(ordinal):
    """Zero is refused, which is what keeps the marker unmintable.

    No integer this function accepts renders as ``000000``, so an ordinal can
    never be formatted into the singleton's reserved place.
    """
    with pytest.raises(IdentityParseError) as raised:
        format_object_id(ordinal)

    assert raised.value.code is IdentityErrorCode.INVALID_OBJECT_ID


@pytest.mark.parametrize("ordinal", ["1", 1.0, None, True])
def test_format_object_id_refuses_a_non_integer(ordinal):
    """``True`` is an ``int`` in Python and is refused anyway."""
    with pytest.raises(IdentityParseError) as raised:
        format_object_id(ordinal)

    assert raised.value.code is IdentityErrorCode.INVALID_INPUT_TYPE


def test_a_refusal_names_its_rule_without_a_traceback():
    """The error is the contract; the message text is not."""
    error = _refusal("w-CH-000001-Maximus")

    assert error.code is IdentityErrorCode.INVALID_PARTITION
    assert error.component == "partition"
    assert error.value == "w"  # the component that failed, not the whole string
    assert "INVALID_PARTITION" in str(error)


def test_a_long_value_is_truncated_in_the_message():
    """A malformed input is echoed for diagnosis, not dumped."""
    error = _refusal("W-CH-000001-_" + "x" * 500)

    assert len(str(error)) < 400
    assert "…" in str(error)
