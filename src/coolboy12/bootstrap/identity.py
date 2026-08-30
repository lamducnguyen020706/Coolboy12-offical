"""Identity parser and formatter — Artifact 035.

Artifact 035 · ``src/coolboy12/bootstrap/identity.py`` · Own: CONST · RM: all ·
T: code · R: IMPL · SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no ·
Ph/St: P1/1b · Req: BR-23 · BP: §13.9a · RMS: §5 · H: 034 · S: — · LS: — ·
G: — · → 036,037, all models · Val: parses six partitions; rejects malformed;
slug decoration only · Done: round-trip proven · Why: fan-out to every model ·
Risk: HINGE · ∥: no

What this module is
-------------------
The first executable identity component beneath the grammar Artifact 034
states::

    034  grammar, frozen
      ↓
    035  parse · format · identity-level resolution   ← this module
      ↓
    036  ordinal allocation and durable non-reuse
      ↓
    037  structural validation

It turns a canonical identity string into four components and back again. It
allocates nothing, stores nothing, looks nothing up, and decides nothing about
what any named thing means.

Two classes of rule, kept apart
-------------------------------
Every rule below is labelled in place, because they do not carry the same
authority and a later reader must be able to tell them apart:

``SOURCE-FROZEN``
    Stated by Blueprint §13.9a / §13.11 or RMS §5, and frozen there. This
    module implements such a rule and may not vary it.

``035 DECISION``
    An operational serialization choice made for this artifact. Artifact 034
    §6 records that the supplied sources establish **no** character set, no
    ``OBJECT_ID`` width, padding, radix or bound, and no case rule — so these
    are decided here for operational use and are **not** source facts. A later
    authorial act may revise any of them without touching the grammar.

What this module is not
-----------------------
Not an allocator (Artifact 036), not the structural validator (Artifact 037),
not a Registry, not a Record store, not an envelope. It holds no kind roster
and no kind meaning: a kind code is syntactic data here, and the Registry owns
the authoritative kind-code mapping (Blueprint §13.11, §9.4). Nothing below
opens a file, reads the environment, imports a later artifact, or mutates
module state, so it cannot allocate an ordinal or reach a Record.

Slug is decoration, and this module treats it that way
------------------------------------------------------
Blueprint §13.9a: *"Decoration only — nothing resolves, matches, or validates
against a slug."* So :func:`resolve_identity` keys on partition, kind and
object identity alone, and no check anywhere below compares a slug against an
expected value — including for the WSV singleton, whose slug is a convention
this module writes and never enforces.

A recorded conflict — CONFLICT-035-A
------------------------------------
The Artifact 035 task supplied ``W-WSV-000000-WorldStateVariables`` as the
canonical WSV singleton. ``WSV`` is three characters, which the frozen rule
forbids. ``WSV`` is the *kind name*; ``WS`` is the *kind code*:

* Blueprint §13.11 — *"Kind codes are two characters, frozen. Every Record
  kind in every partition uses a two-character code."*
* Blueprint §13.9a kind table — ``| WSV (singleton) | WS | W-WS-001-<world> |``
* RMS §5 `FROZEN` — *"two-character kind codes"*
* RMS §8.1 `FROZEN` — *"WSV ``WS`` is World state, not an instance-bearing
  Kind."*

The task's own scope lock says the grammar is frozen and that 035 implements
against it, so the source governs and the sentinel is written ``WS`` here. The
conflict is reported, not patched into any source document. If the author
intends ``WSV`` literally, that is a change to a frozen kind-code width and
belongs in the Blueprint and the RMS, not in this module.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import StrEnum
from typing import Final

__all__ = [
    "KIND_LENGTH",
    "MAX_ORDINAL",
    "MIN_ORDINAL",
    "OBJECT_ID_LENGTH",
    "PARTITIONS",
    "SEPARATOR",
    "SLUG_WORD_SEPARATOR",
    "WSV_SINGLETON",
    "WSV_SINGLETON_IDENTITY",
    "WSV_SINGLETON_OBJECT_ID",
    "Identity",
    "IdentityErrorCode",
    "IdentityKey",
    "IdentityParseError",
    "format_identity",
    "format_object_id",
    "parse_identity",
    "resolve_identity",
]


# ---------------------------------------------------------------------------
# Grammar constants
# ---------------------------------------------------------------------------

SEPARATOR: Final = "-"
"""The structural separator, and nothing else.

SOURCE-FROZEN: Blueprint §13.9a and RMS §5 state the grammar as
``[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]``. The hyphen therefore belongs to the
grammar. 035 DECISION: it is reserved exclusively for that role — a hyphen
inside a component is a rejection, never an escape (see
:data:`IdentityErrorCode.INVALID_SEPARATOR`). No escaping scheme exists in
this module, by design.
"""

COMPONENT_COUNT: Final = 4
"""SOURCE-FROZEN: four elements, in order (Blueprint §13.9a, RMS §5)."""

PARTITIONS: Final = ("W", "E", "P", "R", "V", "I")
"""The six partition codes.

SOURCE-FROZEN. Blueprint §13.9a: *"``W`` World · ``E`` Epistemic · ``P``
Production · ``R`` Registry · ``V`` Visual Library · ``I`` Issue"*, corrected
at v0.7.0 from the stale four-partition row. RMS §2 names the same six
sovereign Record Models. **All six, and no seventh** — a seventh partition
code would name a Record Model that does not exist (I-101).

They are *single* characters. The two-character rule is a rule about ``KIND``
(Blueprint §13.11), not about partition; the Blueprint's own example
``W-CH-001-Maximus`` shows the shape — one character, then two.
"""

KIND_LENGTH: Final = 2
"""SOURCE-FROZEN: Blueprint §13.11 — *"Kind codes are two characters,
frozen. Every Record kind in every partition uses a two-character code."*
RMS §5 states the same rule as part of the frozen grammar."""

OBJECT_ID_LENGTH: Final = 6
"""035 DECISION: the object identity is serialized as six characters.

Blueprint §13.9a states only *"Stable ordinal. Never reused, including after
retirement."* Artifact 034 §4.5 records explicitly that the source *"states no
width, padding, radix or upper bound, and none is invented here."* Six digits
is this artifact's serialization choice, not a Blueprint requirement.
"""

MIN_ORDINAL: Final = 1
MAX_ORDINAL: Final = 999_999
"""035 DECISION: ``000001`` is ordinal #1 and ``999999`` is the largest
representable ordinal — the range that six zero-padded decimal digits admits
once ``000000`` is reserved (below). One-based, so no ordinal #0 exists."""

SLUG_WORD_SEPARATOR: Final = "_"
"""035 DECISION: a space between slug words is written ``_``.

The underscore is a *word separator* and carries no other meaning, so it may
not lead, trail, or repeat. Blueprint §13.9a fixes only that the slug is
human-readable and decoration; the representation is decided here.
"""


# ---------------------------------------------------------------------------
# The WSV singleton
# ---------------------------------------------------------------------------

WSV_SINGLETON_OBJECT_ID: Final = "000000"
"""The reserved singleton marker. **Not ordinal #0.**

RMS §5, accommodated variance: *"WSV bears no per-instance ordinal — the
grammar already admits a singleton."* 035 DECISION: that variance is
represented by the reserved marker ``000000``, which sits outside the
allocatable range :data:`MIN_ORDINAL`–:data:`MAX_ORDINAL` entirely. It is not
zero, it is not an ordinal, and Artifact 036 can never allocate it —
:func:`format_object_id`, the only ordinal-to-string operation here, cannot
produce it.
"""

WSV_SINGLETON_PARTITION: Final = "W"
WSV_SINGLETON_KIND: Final = "WS"
"""SOURCE-FROZEN kind code. Blueprint §13.9a's World kind table gives
``WSV (singleton)`` the code ``WS`` with the example ``W-WS-001-<world>``, and
RMS §8.1 `FROZEN` states *"WSV ``WS`` is World state, not an instance-bearing
Kind."* See CONFLICT-035-A in the module docstring: the task supplied a
three-character ``WSV`` in this position, which the frozen two-character rule
forbids, so the source governs here."""

WSV_SINGLETON_SLUG: Final = "WorldStateVariables"
"""035 DECISION, and decoration only.

This is the slug this module *writes* for the singleton. Nothing validates
against it: Blueprint §13.9a says nothing resolves, matches or validates
against a slug, so :func:`parse_identity` accepts the singleton marker with
any well-formed slug and never compares one.
"""

_WSV_SINGLETON_TUPLE: Final = (WSV_SINGLETON_PARTITION, WSV_SINGLETON_KIND)
"""The one kind code this module recognizes, and the only one.

035 DECISION, narrowly bounded: the marker ``000000`` has to be legal
*somewhere* and illegal everywhere else, which cannot be decided without
naming the pair that bears it. Recognizing this pair is a syntactic
reservation, **not** a kind roster and **not** a kind meaning — no mapping
from ``WS`` to any concept exists in this module, and none of the other kind
codes appears anywhere in it. The Registry owns kind meaning (Blueprint
§13.11, §9.4).

What this deliberately does *not* do: it does not stop ``W-WS-000001-…`` from
parsing. That WSV bears no per-instance ordinal is a World Record Model
semantic (RMS §5, §8.1), and enforcing a model's semantics is neither this
artifact's job nor this layer's (§13.7a, I-103).
"""


# ---------------------------------------------------------------------------
# Character classes
# ---------------------------------------------------------------------------
#
# Every class below is written as an explicit ASCII range. This is deliberate
# and load-bearing: ``\d`` matches Unicode decimal digits, ``str.isdigit()``
# accepts more still, and ``str.isupper()`` is true of non-ASCII uppercase. Any
# of those would let a visually identical non-ASCII identity through, which is
# the hidden normalization this artifact must not perform.

_KIND_PATTERN: Final = re.compile(r"\A[A-Z]{2}\Z")
"""SOURCE-FROZEN width (two characters, Blueprint §13.11). 035 DECISION for
the character class: uppercase-only is the supplied 035 policy, and "uppercase"
is undefined for uncased characters, so the class is resolved to ASCII ``A-Z``
— which is what every kind code stated in either source already is (``CH``,
``CO``, ``OR``, ``LI``, ``SP``, ``EV``, ``LO``, ``WS``). Artifact 034 §6
records that no source establishes a character set for any element."""

_OBJECT_ID_PATTERN: Final = re.compile(r"\A[0-9]{6}\Z")
"""035 DECISION: exactly six ASCII decimal digits, zero-padded."""

_SLUG_FORBIDDEN_RUN: Final = SLUG_WORD_SEPARATOR * 2


class IdentityErrorCode(StrEnum):
    """Why an identity was refused.

    Deterministic and small. Each code names the *one* rule that failed, so a
    caller can branch on the code rather than on message text, and the message
    itself is never part of the contract.
    """

    INVALID_INPUT_TYPE = "INVALID_INPUT_TYPE"
    """The value handed in was not of the required type."""

    INVALID_ARITY = "INVALID_ARITY"
    """Fewer than four components — the identity is missing elements."""

    INVALID_SEPARATOR = "INVALID_SEPARATOR"
    """More than four components, or the separator inside a component.

    035 DECISION: because the grammar is fixed at four elements and ``-`` is
    reserved as the structural separator, an extra field can only mean a
    hyphen appeared inside a component — the ``W-CH-000001-Maximus-The-Great``
    case. Naming it a separator failure rather than an arity failure says
    which rule was actually broken.
    """

    INVALID_PARTITION = "INVALID_PARTITION"
    """Not one of the six single-character partition codes."""

    INVALID_KIND = "INVALID_KIND"
    """Not exactly two uppercase characters."""

    INVALID_OBJECT_ID = "INVALID_OBJECT_ID"
    """Not the canonical six-digit representation, or out of range."""

    INVALID_WSV = "INVALID_WSV"
    """The reserved singleton marker appeared outside the singleton."""

    INVALID_SLUG = "INVALID_SLUG"
    """Empty, whitespace-bearing, or an underscore used as anything but a
    separator between two slug words."""


class IdentityParseError(Exception):
    """An identity string or an identity component broke the 035 contract.

    Carries a :class:`IdentityErrorCode` and the component that failed, so a
    caller can act on the failure without reading a traceback or a message.
    Raised by construction, parsing and formatting alike: the contract is one
    contract, and an :class:`Identity` that could not be parsed is an
    :class:`Identity` that must not be built.
    """

    _ECHO_LIMIT: Final = 120

    def __init__(
        self,
        code: IdentityErrorCode,
        message: str,
        *,
        value: object = None,
        component: str | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.value = value
        self.component = component
        super().__init__(f"{code.value}: {message}{self._echo(value)}")

    @classmethod
    def _echo(cls, value: object) -> str:
        """Quote the offending value, truncated, or say nothing."""
        if not isinstance(value, str):
            return ""
        shown = (
            value if len(value) <= cls._ECHO_LIMIT else value[: cls._ECHO_LIMIT] + "…"
        )
        return f" (got {shown!r})"


@dataclass(frozen=True, slots=True)
class IdentityKey:
    """What an identity resolves to: partition, kind, object identity.

    The resolution target of :func:`resolve_identity`, and the answer to
    Artifact 034 §5.3's rename invariant — *"A rename must not silently create
    a new canonical identity"* (Blueprint §13.9a, I-82). The slug is absent
    because it is decoration: two identities differing only in slug produce the
    same key, so renaming cannot mint a second identity.

    It is a key over identity *components* and nothing more. It is not a
    Record, not a handle, not a storage address, and resolving it fetches
    nothing — Record resolution belongs to a Record resolver (Blueprint §9.4),
    not to this layer.
    """

    partition: str
    kind: str
    object_id: str


@dataclass(frozen=True, slots=True)
class Identity:
    """A parsed identity: the four grammar elements, and no fifth.

    SOURCE-FROZEN shape (Blueprint §13.9a, RMS §5). ``provenance``,
    ``registry_ref`` and ``sot_class`` are envelope fields (Artifact 033) and
    are not identity components; ``tier`` and ``status`` are World Record Model
    properties and are neither (Blueprint §13.7). Artifact 034 §4.2 states the
    boundary: *"No other element participates."*

    Immutable, and validated on construction, so an ill-formed identity cannot
    exist as an object. ``object_id`` stays a string: it is the canonical
    representation, and holding it as an integer would lose the padding that
    :func:`format_identity` would then have to reconstruct — and would turn the
    reserved marker ``000000`` into the number zero, which it is not.
    """

    partition: str
    kind: str
    object_id: str
    slug: str

    def __post_init__(self) -> None:
        _check_partition(self.partition)
        _check_kind(self.kind)
        _check_object_id(self.object_id)
        _check_singleton_marker(self.partition, self.kind, self.object_id)
        _check_slug(self.slug)

    @property
    def key(self) -> IdentityKey:
        """This identity without its decoration — see :class:`IdentityKey`."""
        return IdentityKey(self.partition, self.kind, self.object_id)

    @property
    def is_singleton(self) -> bool:
        """Whether this identity carries the reserved singleton marker."""
        return self.object_id == WSV_SINGLETON_OBJECT_ID

    def __str__(self) -> str:
        return format_identity(self)


# ---------------------------------------------------------------------------
# Component checks
#
# One function per rule, each raising the one code that names it. Parsing and
# formatting share them, so a string and a structured value are held to the
# same contract and cannot drift apart.
#
# These are *syntax* checks, sufficient to parse and emit a canonical
# representation (the boundary the task sets for 035). They are not the
# structural validation contract, which is Artifact 037's and is neither
# imported nor anticipated here.
# ---------------------------------------------------------------------------


def _check_text(value: object, component: str) -> str:
    """Require a ``str``. No coercion — ``str(value)`` would invent an identity."""
    if not isinstance(value, str):
        raise IdentityParseError(
            IdentityErrorCode.INVALID_INPUT_TYPE,
            f"{component} must be a str, not {type(value).__name__}",
            component=component,
        )
    return value


def _check_partition(partition: object) -> None:
    """SOURCE-FROZEN: one of six single characters. 035 DECISION: uppercase only.

    A lowercase partition is refused rather than folded. Silently uppercasing
    ``w`` would return an identity the caller did not supply, and an identity
    this layer rewrote is an identity nobody can audit.
    """
    text = _check_text(partition, "partition")
    if text not in PARTITIONS:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_PARTITION,
            f"partition must be one of {'/'.join(PARTITIONS)}, uppercase",
            value=text,
            component="partition",
        )


def _check_kind(kind: object) -> None:
    """SOURCE-FROZEN width; 035 DECISION case and class. No roster is consulted.

    Whether ``CH`` is a kind that *exists* is a Registry question, and this
    module does not ask it. It checks the shape and keeps the code as data.
    """
    text = _check_text(kind, "kind")
    if _KIND_PATTERN.match(text) is None:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_KIND,
            f"kind must be exactly {KIND_LENGTH} uppercase characters",
            value=text,
            component="kind",
        )


def _check_object_id(object_id: object) -> None:
    """035 DECISION: exactly six ASCII decimal digits.

    Nothing is padded on the caller's behalf. ``"1"`` is not ``"000001"``
    here; converting it would be this module deciding which ordinal was meant.
    :func:`format_object_id` exists for callers that hold a number and want the
    canonical string — that is an explicit request, not a silent repair.
    """
    text = _check_text(object_id, "object_id")
    if _OBJECT_ID_PATTERN.match(text) is None:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_OBJECT_ID,
            f"object_id must be exactly {OBJECT_ID_LENGTH} decimal digits, zero-padded",
            value=text,
            component="object_id",
        )


def _check_singleton_marker(partition: str, kind: str, object_id: str) -> None:
    """The reserved marker is legal for the singleton and nowhere else."""
    if object_id != WSV_SINGLETON_OBJECT_ID:
        return
    if (partition, kind) != _WSV_SINGLETON_TUPLE:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_WSV,
            f"{WSV_SINGLETON_OBJECT_ID} is the reserved singleton marker and is legal "
            f"only for {WSV_SINGLETON_PARTITION}-{WSV_SINGLETON_KIND}; it is not "
            f"ordinal #0 and no ordinal #0 exists",
            value=f"{partition}-{kind}-{object_id}",
            component="object_id",
        )


def _check_slug(slug: object) -> None:
    """035 DECISION: non-empty words, joined by ``_``, and nothing else.

    Four refusals, one rule each: a slug must exist; it may not carry the
    structural separator; it may not carry whitespace, because a space between
    words is written ``_`` and internal whitespace is never trimmed away for
    the caller; and the underscore separates two words, so it may not lead,
    trail, or double.

    Case is preserved exactly. ``Maximus``, ``MAXIMUS`` and ``maximus`` are
    three slugs, and no folding, transliteration or normalization happens
    anywhere in this module.

    Beyond these rules the slug is left alone. No source and no 035 decision
    establishes a slug character set (Artifact 034 §6), so none is invented
    here — refusing more than was decided would be this module writing policy.
    """
    text = _check_text(slug, "slug")

    if not text:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_SLUG,
            "slug must not be empty",
            value=text,
            component="slug",
        )
    if SEPARATOR in text:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_SEPARATOR,
            f"{SEPARATOR!r} is the structural separator and may not appear in a slug; "
            f"a space between slug words is written {SLUG_WORD_SEPARATOR!r}",
            value=text,
            component="slug",
        )
    if any(character.isspace() for character in text):
        raise IdentityParseError(
            IdentityErrorCode.INVALID_SLUG,
            f"slug must not contain whitespace; a space between slug words is "
            f"written {SLUG_WORD_SEPARATOR!r}",
            value=text,
            component="slug",
        )
    if (
        text.startswith(SLUG_WORD_SEPARATOR)
        or text.endswith(SLUG_WORD_SEPARATOR)
        or _SLUG_FORBIDDEN_RUN in text
    ):
        raise IdentityParseError(
            IdentityErrorCode.INVALID_SLUG,
            f"{SLUG_WORD_SEPARATOR!r} separates two slug words and may not lead, "
            f"trail, or repeat",
            value=text,
            component="slug",
        )


# ---------------------------------------------------------------------------
# The public operations
# ---------------------------------------------------------------------------


def parse_identity(value: str) -> Identity:
    """Parse a canonical identity string into its four components.

    :param value: the identity. Surrounding whitespace is trimmed (035
        DECISION); whitespace *inside* a component is not, and makes the
        identity invalid rather than repaired.
    :returns: the parsed :class:`Identity`.
    :raises IdentityParseError: with the :class:`IdentityErrorCode` naming the
        rule that failed.

    Deterministic and self-contained. It consults no Registry, reads no
    Record, touches no filesystem, allocates no ordinal and keeps no state
    between calls: the same string always yields the same result, and parsing
    an identity brings nothing into existence.
    """
    text = _check_text(value, "identity").strip()

    parts = text.split(SEPARATOR)
    if len(parts) < COMPONENT_COUNT:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_ARITY,
            f"an identity has {COMPONENT_COUNT} components "
            f"(PARTITION{SEPARATOR}KIND{SEPARATOR}OBJECT_ID{SEPARATOR}SLUG); "
            f"got {len(parts)}",
            value=text,
        )
    if len(parts) > COMPONENT_COUNT:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_SEPARATOR,
            f"{SEPARATOR!r} is the structural separator and may not appear inside a "
            f"component; got {len(parts)} components where {COMPONENT_COUNT} are allowed",
            value=text,
        )

    partition, kind, object_id, slug = parts
    return Identity(partition=partition, kind=kind, object_id=object_id, slug=slug)


def format_identity(identity: Identity) -> str:
    """Serialize an identity to its canonical string.

    :param identity: an :class:`Identity`, or any object carrying the four
        component attributes.
    :returns: ``PARTITION-KIND-OBJECT_ID-SLUG``.
    :raises IdentityParseError: if any component breaks the 035 contract.

    Nothing is repaired on the way out. Components are re-checked and an
    invalid one is refused, rather than uppercased, padded or trimmed into
    shape — a formatter that silently corrects its input is a second, hidden
    parser, and the value it emits is not the value it was given.
    """
    partition = getattr(identity, "partition", None)
    kind = getattr(identity, "kind", None)
    object_id = getattr(identity, "object_id", None)
    slug = getattr(identity, "slug", None)

    _check_partition(partition)
    _check_kind(kind)
    _check_object_id(object_id)
    _check_singleton_marker(str(partition), str(kind), str(object_id))
    _check_slug(slug)

    return SEPARATOR.join((str(partition), str(kind), str(object_id), str(slug)))


def resolve_identity(value: str | Identity) -> IdentityKey:
    """Resolve an identity to its components — and no further.

    :param value: a canonical identity string, or an :class:`Identity`.
    :returns: the :class:`IdentityKey` — partition, kind, object identity.
    :raises IdentityParseError: if a supplied string is not a valid identity.

    This is identity-level resolution and stops there::

        identity string → parse → Identity → key

    Row 035 names this artifact the *identity parser and formatter* and states
    no resolution mechanics; Blueprint §13.9a establishes that a resolution
    contract is shared infrastructure without defining what it reaches. So the
    narrow boundary holds: **no Record of any of the six models is fetched
    here**, no storage is consulted, and no Registry is asked what the kind
    means. Blueprint §9.4 places reference resolution with a Record resolver,
    not with the Registry and not with this module.

    The slug is never the key (Blueprint §13.9a). Renaming an object changes
    its slug and leaves what this function returns identical, which is the
    rename invariant made executable.
    """
    identity = parse_identity(value) if isinstance(value, str) else value
    if not isinstance(identity, Identity):
        raise IdentityParseError(
            IdentityErrorCode.INVALID_INPUT_TYPE,
            f"identity must be a str or Identity, not {type(identity).__name__}",
            component="identity",
        )
    return identity.key


def format_object_id(ordinal: int) -> str:
    """Render an ordinal the caller already holds as a canonical object_id.

    :param ordinal: an integer in ``1..999999``.
    :returns: the six-digit zero-padded representation.
    :raises IdentityParseError: for a non-integer, or an ordinal out of range.

    **This is representation, not allocation.** It does not choose an ordinal,
    increment a counter, reserve, persist, or consult a ledger, and it holds no
    state — call it twice with 1 and it returns ``"000001"`` twice. Which
    ordinal comes next, and how non-reuse survives a restart, is Artifact 036's
    and appears nowhere in this module.

    The range is closed below at 1 and above at 999999, which is what makes the
    reserved singleton marker unreachable: there is no integer this function
    accepts that renders as ``000000``, so no ordinal can ever be minted into
    the singleton's place.
    """
    if isinstance(ordinal, bool) or not isinstance(ordinal, int):
        raise IdentityParseError(
            IdentityErrorCode.INVALID_INPUT_TYPE,
            f"ordinal must be an int, not {type(ordinal).__name__}",
            component="object_id",
        )
    if not MIN_ORDINAL <= ordinal <= MAX_ORDINAL:
        raise IdentityParseError(
            IdentityErrorCode.INVALID_OBJECT_ID,
            f"ordinal must be in {MIN_ORDINAL}..{MAX_ORDINAL}; ordinals are one-based "
            f"and {WSV_SINGLETON_OBJECT_ID} is a reserved marker, not ordinal #0",
            value=str(ordinal),
            component="object_id",
        )
    return f"{ordinal:0{OBJECT_ID_LENGTH}d}"


# ---------------------------------------------------------------------------
# The canonical singleton, built from the contract above rather than declared
# beside it — so if any rule here ever stopped admitting it, importing this
# module would fail loudly instead of shipping a sentinel the parser rejects.
# ---------------------------------------------------------------------------

WSV_SINGLETON: Final = Identity(
    partition=WSV_SINGLETON_PARTITION,
    kind=WSV_SINGLETON_KIND,
    object_id=WSV_SINGLETON_OBJECT_ID,
    slug=WSV_SINGLETON_SLUG,
)
"""The canonical WSV singleton identity. See CONFLICT-035-A above on ``WS``."""

WSV_SINGLETON_IDENTITY: Final = format_identity(WSV_SINGLETON)
"""The canonical WSV singleton, serialized: ``W-WS-000000-WorldStateVariables``."""
