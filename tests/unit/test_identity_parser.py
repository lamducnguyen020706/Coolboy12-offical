"""Unit tests for the Artifact 035 identity parser and formatter.

Proves row 035's ``Val`` — *parses six partitions; rejects malformed; slug
decoration only* — and its ``Done`` — *round-trip proven*. Rejection proofs
live in ``tests/negative/`` and boundary proofs in ``tests/boundary/``, per
the suite responsibilities Artifact 010 established.

Every identity below is a syntactic example. None is a Record, none is
canonical, and no kind code here carries meaning: the Registry owns the
authoritative kind-code mapping (Blueprint §13.11, §9.4). ``XX`` is used
wherever a two-character code is needed and no source states one, precisely so
that no roster is implied by a test fixture.
"""

from __future__ import annotations

import pytest

from coolboy12.bootstrap.identity import (
    MAX_ORDINAL,
    MIN_ORDINAL,
    PARTITIONS,
    WSV_SINGLETON,
    WSV_SINGLETON_IDENTITY,
    WSV_SINGLETON_OBJECT_ID,
    Identity,
    IdentityKey,
    format_identity,
    format_object_id,
    parse_identity,
    resolve_identity,
)

CANONICAL = "W-CH-000001-Maximus"


def test_canonical_identity_parses_into_four_components():
    """The whole of the grammar: four elements, in order, and no fifth."""
    identity = parse_identity(CANONICAL)

    assert isinstance(identity, Identity)
    assert identity.partition == "W"
    assert identity.kind == "CH"
    assert identity.object_id == "000001"
    assert identity.slug == "Maximus"

    # No envelope field and no World property rode along (Artifact 034 §4.2).
    for absent in ("provenance", "registry_ref", "sot_class", "tier", "status"):
        assert not hasattr(identity, absent)


@pytest.mark.parametrize("partition", PARTITIONS)
def test_all_six_partitions_parse(partition):
    """Row 035's ``Val``: *parses six partitions*.

    All six sovereign Record Models are nameable — the defect Artifact 034's
    ``Why`` exists to prevent, in executable form.
    """
    identity = parse_identity(f"{partition}-XX-000001-Example")

    assert identity.partition == partition


def test_the_six_partitions_are_exactly_the_six_record_models():
    """No seventh partition code exists (Blueprint §13.9a, RMS §2, I-101)."""
    assert PARTITIONS == ("W", "E", "P", "R", "V", "I")


@pytest.mark.parametrize(
    "value",
    [
        "W-CH-000001-Maximus",
        "W-CH-000002-Maximus_The_Great",
        "E-XX-000123-Epistemic_Record",
        "P-XX-999999-Production_Record",
        "R-XX-000001-Registry_Record",
        "V-XX-000001-Visual_Record",
        "I-XX-000001-Issue_Record",
        WSV_SINGLETON_IDENTITY,
    ],
)
def test_round_trip_is_exact(value):
    """Row 035's ``Done``: *round-trip proven*.

    ``format_identity(parse_identity(x)) == x`` for every canonical form,
    including the reserved singleton.
    """
    assert format_identity(parse_identity(value)) == value


def test_round_trip_holds_after_trimming_but_not_against_raw_input():
    """Trimming is input policy, so the canonical form is what comes back."""
    assert format_identity(parse_identity(f"  {CANONICAL}  ")) == CANONICAL
    assert format_identity(parse_identity(f"\t{CANONICAL}\n")) == CANONICAL


def test_str_of_an_identity_is_its_canonical_form():
    assert str(parse_identity(CANONICAL)) == CANONICAL


@pytest.mark.parametrize(
    ("object_id", "meaning"),
    [("000001", MIN_ORDINAL), ("000002", 2), ("000010", 10), ("001234", 1234)],
)
def test_object_id_is_one_based_and_zero_padded(object_id, meaning):
    """035 DECISION: ``000001`` is ordinal #1, not ordinal #0 and not #2."""
    assert parse_identity(f"W-XX-{object_id}-Example").object_id == object_id
    assert format_object_id(meaning) == object_id


def test_the_ordinal_boundaries_are_both_representable():
    assert format_object_id(MIN_ORDINAL) == "000001"
    assert format_object_id(MAX_ORDINAL) == "999999"
    assert parse_identity("W-XX-999999-Example").object_id == "999999"


def test_the_wsv_singleton_is_exactly_one_string():
    """The reserved marker, in the only place it is legal.

    ``WS`` is the kind *code* — Blueprint §13.9a's World kind table gives
    ``WSV (singleton)`` the code ``WS``, and RMS §8.1 `FROZEN` repeats it. The
    two-character rule (Blueprint §13.11) admits nothing longer.
    """
    assert WSV_SINGLETON_IDENTITY == "W-WS-000000-WorldStateVariables"

    identity = parse_identity(WSV_SINGLETON_IDENTITY)
    assert identity == WSV_SINGLETON
    assert identity.partition == "W"
    assert identity.kind == "WS"
    assert identity.object_id == WSV_SINGLETON_OBJECT_ID == "000000"
    assert identity.slug == "WorldStateVariables"
    assert identity.is_singleton
    assert len(identity.kind) == 2


def test_the_singleton_marker_is_not_the_integer_zero():
    """``000000`` is a reserved marker, never ordinal #0 (RMS §5 variance)."""
    identity = parse_identity(WSV_SINGLETON_IDENTITY)

    assert identity.object_id == "000000"
    assert isinstance(identity.object_id, str)
    # It survives as six characters rather than collapsing to a number.
    assert identity.object_id != 0
    assert not parse_identity(CANONICAL).is_singleton


@pytest.mark.parametrize(
    ("slug", "why"),
    [
        ("Maximus", "one word"),
        ("Maximus_The_Great", "spaces written as underscores"),
        ("MAXIMUS", "case preserved as given"),
        ("maximus", "case preserved as given"),
        ("Maximus2", "ASCII digits are inside the 035 slug character set"),
    ],
)
def test_well_formed_slugs_survive_verbatim(slug, why):
    assert parse_identity(f"W-XX-000001-{slug}").slug == slug, why


@pytest.mark.parametrize(
    "slug",
    ["Maximus", "Maximus_The_Great", "maximus", "MAXIMUS", "Record123", "A1_B2"],
)
def test_the_ascii_slug_character_set_is_accepted(slug):
    """035 DECISION: ASCII ``A-Z``, ``a-z``, ``0-9`` and ``_``.

    Letters in either case, digits, and the word separator — the whole set,
    and the slug comes back exactly as written.
    """
    assert parse_identity(f"W-XX-000001-{slug}").slug == slug


def test_slug_case_is_never_folded():
    """035 DECISION: the slug is case-sensitive; three slugs, not one."""
    slugs = {
        parse_identity(f"W-XX-000001-{s}").slug
        for s in ("Maximus", "MAXIMUS", "maximus")
    }

    assert slugs == {"Maximus", "MAXIMUS", "maximus"}


def test_a_rename_does_not_create_a_new_identity():
    """Blueprint §13.9a and I-82, executable.

    *"A rename must not silently create a new canonical identity."* The slug
    is decoration (row 035's ``Val``: *slug decoration only*), so changing it
    leaves what the identity resolves to untouched.
    """
    before = resolve_identity("W-CH-000001-Maximus")
    after = resolve_identity("W-CH-000001-Maximus_New")

    assert before == after == IdentityKey("W", "CH", "000001")

    # Two different objects, because they are two different representations —
    # but one identity, because the key is what identity means.
    assert parse_identity("W-CH-000001-Maximus") != parse_identity(
        "W-CH-000001-Maximus_New"
    )
    assert (
        parse_identity("W-CH-000001-Maximus").key
        == parse_identity("W-CH-000001-Maximus_New").key
    )


def test_resolution_exposes_the_three_components_and_no_slug():
    key = resolve_identity(CANONICAL)

    assert (key.partition, key.kind, key.object_id) == ("W", "CH", "000001")
    assert not hasattr(key, "slug")


def test_resolve_accepts_a_parsed_identity_as_well_as_a_string():
    assert resolve_identity(parse_identity(CANONICAL)) == resolve_identity(CANONICAL)


def test_identity_is_immutable():
    identity = parse_identity(CANONICAL)

    with pytest.raises(Exception):  # noqa: B017 - frozen dataclass raises FrozenInstanceError
        identity.slug = "Other"


def test_parsing_is_deterministic():
    """The same string, ten times, is the same identity every time."""
    results = {format_identity(parse_identity(CANONICAL)) for _ in range(10)}

    assert results == {CANONICAL}


def test_a_structured_identity_can_be_built_and_formatted_directly():
    identity = Identity(
        partition="E", kind="XX", object_id="000123", slug="Example_Record"
    )

    assert format_identity(identity) == "E-XX-000123-Example_Record"
