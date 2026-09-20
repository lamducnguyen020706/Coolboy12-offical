"""Provenance capture mechanism — Artifact 047.

Artifact 047 · ``src/coolboy12/kernel/provenance.py`` · Own: CONST · RM: all ·
T: code · R: IMPL · SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no ·
Ph/St: P2/2b · Req: BR-15 · BP: §10 Spine 9 · RMS: §18 · H: 033 · S: — ·
LS: — · G: — · → 133 · Val: captures who/when/why; meaning left to models ·
Done: capture only · Why: obligation universal, meaning not · Risk: medium ·
∥: yes

What this module is
-------------------
The capture half of provenance, and nothing else::

    033  the envelope names `provenance` as one of seven fields
      ↓
    047  capture who / when / why                      ← this module
      ↓
    048  what provenance MEANS — model-owned boundary

Blueprint §13.7b fixes what provenance answers: *"Who made this, when, and
**why**"*, held as *"an envelope property on the Record."* RMS §18 lists the
same three and separates provenance from five neighbouring concepts. This
module records those three values and decides nothing about them.

Spine law 9 is why the obligation is universal: *"Every Record traces to the
decision that created or last changed it. No anonymous canon; a change with no
recorded reason is an audit flag."* All three dimensions are therefore
required — a capture missing ``why`` is the very thing law 9 names.

Two classes of rule, kept apart
-------------------------------
``SOURCE FACT``
    Stated by Blueprint §13.7a / §13.7b / §12.16 / §10 law 9 or RMS §18, and
    frozen there. This module implements such a rule and may not vary it. The
    source facts are: provenance answers who, when and why; capture is shared
    infrastructure while meaning is model-owned; ``when`` carries Real-World
    Time; a reason is required.

``047 DECISION``
    An operational representation choice. Artifact 033 §5.5 names the
    ``provenance`` field and its three dimensions but establishes **no**
    internal representation — no field spelling, no text encoding, no instant
    format, no mapping shape. Those are decided here for operational use, are
    **not** source facts, and carry no constitutional meaning. A later
    authorial act may revise any of them without touching the envelope.

**The Python objects below are an 047 implementation, not a constitution.**
The three *dimensions* are source-fixed; the dataclass that carries them, its
field spellings, its instant format and its mapping helper are this artifact's
current way of capturing them. No source establishes a universal provenance
schema or a universal wire format, and nothing here should be read as one —
the meaning of a captured value stays governed by the owning Record Model and
by Artifact 048's boundary.

What this module is not
-----------------------
Not audit, not history, not revision, not version, not derivation. RMS §18 and
Blueprint §13.7b separate six concepts that *"are not interchangeable"*, and
this module implements exactly one of them:

===============  ====================================================  =========
Concept          What it answers                                       Owner
===============  ====================================================  =========
**provenance**   who made this, when, why                              **here**
audit            under what approval mode, in which session            elsewhere
history          how this Record's state came to be what it is         model
revision         this Record changed, and here is the change           model
version          a distinct issued state of the same thing            model
derivation       this came from that                                   model
===============  ====================================================  =========

So **session and approval mode are audit, not provenance** (§13.7b, RMS §18)
and are absent below. Nothing here approves, gates, versions, or explains how a
Record came to be as it is.

``why`` is a recorded reason, not a causal account
--------------------------------------------------
The ``why`` captured here is the rationale the caller supplies at the moment of
capture. It is **not** a causal graph, an event chain, a derivation chain, or
the History answer to *how this Record came to be what it is* — Blueprint
§13.7b assigns that to history, which is model-owned packaging. This module
stores the text and interprets none of it.

No model semantics, and no branch on one
----------------------------------------
Blueprint §13.7a lists provenance **capture** as shared infrastructure while
what provenance *means* in a model is not decided by it; RMS §6 makes
provenance meaning one of the nine things a Record Model owns. Nothing below
takes a partition, a kind, a Record or a Record Model as input, so this module
**cannot** vary its behaviour by model even by accident. Artifact 048 states
that boundary constitutionally; this module simply has no way to cross it.

``when`` names its axis: Real-World Time
----------------------------------------
Blueprint P-21 requires every temporal statement to name its axis, so this one
does. §12.16 lists three canonical axes and states where each is authoritative;
**Real-World Time** — *"The operational clock at which a canonical action
occurred"* — is authoritative in *"History Record, WSV-H, provenance."*

``when`` is therefore the caller-supplied Real-World Time value for the action
this provenance records. That is the axis, and naming it is all this module
does with it.

**Capturing a Real-World Time value is not owning the temporal architecture.**
This module does not define World Time, does not define Session Number, does
not define the issue ordinal (which §12.16 holds is not a temporal axis at
all), does not order captures, does not derive one axis from another — §12.16:
*"no axis is derivable from another"* — and does not package history, which is
model-owned (§13.7b, Artifact 054, I-90).

**Syntax does not confer canonical status.** I-86: a timestamp produced by an
external system *"becomes World Time, Session Number, or Real-World Time only
by being recorded as such through the mutation path — never by having been
generated by a tool."* This module validates that a supplied value is a real
instant in the representation it accepts; it does **not** thereby rule that the
value has canonical Real-World Time standing. That is the mutation path's to
confer, not a validator's.

Accordingly nothing here is defaulted to the clock: a caller states ``when`` or
the capture is refused, so no instant is ever generated, inferred or
substituted by this module.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Final

__all__ = [
    "PROVENANCE_DIMENSIONS",
    "Provenance",
    "ProvenanceCaptureError",
    "ProvenanceErrorCode",
    "capture_provenance",
    "provenance_from_mapping",
    "provenance_to_mapping",
]

PROVENANCE_DIMENSIONS: Final = ("who", "when", "why")
"""The three dimensions provenance answers, in the sources' own words.

SOURCE FACT — that provenance answers exactly who, when and why (Blueprint
§13.7b, RMS §18, row 047 ``Val``). 047 DECISION — that this tuple is how the
implementation names them. The spellings are the sources' own nouns rather
than invented synonyms: ``actor``, ``author``, ``timestamp`` and ``reason``
are deliberately not used, because none is a source term and each drags in a
semantic the sources did not grant.
"""

_WHEN_PATTERN: Final = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$"
)
"""047 DECISION: the accepted spelling of a capture instant.

An RFC 3339 / ISO 8601 instant in UTC, ``Z``-terminated, with optional
fractional seconds. Chosen because it is textual, sorts lexicographically,
round-trips through JSON unchanged, and names no timezone the caller must
interpret. **This is a transport format, not a temporal semantic** — see the
module docstring. No source establishes it, and revising it touches no
constitutional rule.
"""


class ProvenanceErrorCode(StrEnum):
    """Why a provenance capture was refused.

    Deterministic and small. Each code names the *one* rule that failed, so a
    caller can branch on the code rather than on message text, and the message
    itself is never part of the contract.
    """

    INVALID_INPUT_TYPE = "INVALID_INPUT_TYPE"
    """A supplied dimension was not text, or the mapping was not a mapping."""

    MISSING_DIMENSION = "MISSING_DIMENSION"
    """One of who / when / why was absent or empty.

    All three are required. Blueprint §10 law 9: *"a change with no recorded
    reason is an audit flag"* — so a capture that drops ``why`` is refused
    rather than stored incomplete.
    """

    INVALID_WHEN = "INVALID_WHEN"
    """``when`` was not the accepted capture-instant spelling (047 DECISION)."""

    UNKNOWN_DIMENSION = "UNKNOWN_DIMENSION"
    """A mapping carried a key that is not one of the three dimensions.

    Refused rather than ignored: silently dropping an unrecognised key would
    lose data the caller believed captured, and silently keeping it would let
    provenance grow semantics this artifact has no authority to grant.
    """


class ProvenanceCaptureError(Exception):
    """A provenance capture broke the 047 contract.

    Carries a :class:`ProvenanceErrorCode` and the dimension that failed, so a
    caller can act on the failure without reading a traceback or a message.
    """

    _ECHO_LIMIT: Final = 120

    def __init__(
        self,
        code: ProvenanceErrorCode,
        message: str,
        *,
        value: object = None,
        dimension: str | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.value = value
        self.dimension = dimension
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
class Provenance:
    """A captured provenance value: who, when, why — and no fourth dimension.

    047 DECISION — the current implementation shape. The three *dimensions*
    are the source fact (Blueprint §13.7b, RMS §18); this dataclass is how
    047 carries them and is **not** a constitutional universal provenance
    schema. Another implementation could carry the same three differently
    without touching a source rule.

    The instance is immutable after construction. That is an implementation
    property of this Python value object; it defines no mutation, revision,
    version, derivation or history semantics, none of which 047 owns.
    Canonical mutation travels the governed path (Spine law 2), which this
    module neither implements nor bypasses.

    **Construction validates.** The same structural invariants the factory
    applies are enforced here, so the type has no unvalidated back door: a
    ``Provenance`` that exists is a ``Provenance`` that passed the capture
    contract.

    It is not a Record, not an envelope, and not an eighth envelope field. The
    envelope is seven fields (RMS §4, Artifact 033) and holds *one* of them,
    ``provenance``; this is the value that field carries.
    """

    who: str
    """Who made this. Opaque text: this module reads no identity out of it."""

    when: str
    """The caller-supplied **Real-World Time** value for the action this
    provenance records, in the 047 DECISION instant spelling.

    Real-World Time is the axis (Blueprint §12.16, which makes it
    authoritative in provenance), and naming it is all 047 does with it: this
    module does not derive, order, convert or reinterpret temporal axes, and
    confers no canonical status by validating the value (I-86).

    **It is the time of the action, not of this function call.** If an action
    occurred at 10:15 and is captured at 10:17, ``when`` is 10:15 — whatever
    the caller supplied. Nothing here substitutes the moment of capture, and
    nothing here reads a clock.
    """

    why: str
    """Why it was made — the reason the caller recorded, uninterpreted."""

    def __post_init__(self) -> None:
        """Enforce the capture contract on every construction path.

        Validation lives in the private checkers and is called from exactly
        one place per dimension, so the factory and the constructor cannot
        drift into two rule sets. The checkers read primitives and build no
        ``Provenance``, so there is no construction cycle.
        """
        _check_text(self.who, "who")
        _check_when(self.when)
        _check_text(self.why, "why")


def _check_text(value: object, dimension: str) -> str:
    """Require non-empty text, and return it unchanged.

    047 DECISION: surrounding whitespace is rejected rather than stripped.
    Normalising a captured value would edit what the caller said happened, and
    a capture mechanism that quietly rewrites its input is not a capture
    mechanism.
    """
    if not isinstance(value, str):
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.INVALID_INPUT_TYPE,
            f"{dimension} must be text",
            value=value,
            dimension=dimension,
        )
    if not value or value.strip() != value:
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.MISSING_DIMENSION,
            f"{dimension} must be non-empty and free of surrounding whitespace",
            value=value,
            dimension=dimension,
        )
    return value


def _check_when(value: object) -> str:
    """Require a real UTC instant in the 047 DECISION spelling.

    Two layers, because they catch different failures:

    **Lexical** — the value matches the accepted representation. A regex alone
    settles this and nothing more.

    **Calendar** — the components describe an instant that exists. The regex
    admits ``2026-02-29T12:00:00Z`` and ``2026-09-20T12:00:61Z``; neither is a
    moment, so both are refused here. :mod:`datetime` decides this rather than
    hand-written calendar rules, which would have to re-derive leap years.

    A refusal is never a repair: an impossible instant is rejected, never
    rolled forward into a neighbouring valid one.
    """
    when = _check_text(value, "when")
    if not _WHEN_PATTERN.match(when):
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.INVALID_WHEN,
            "when must be a UTC instant such as 2026-09-20T12:00:00Z",
            value=when,
            dimension="when",
        )
    try:
        datetime.fromisoformat(when)
    except ValueError as exc:
        # The parser's ValueError never escapes: INVALID_WHEN stays the
        # contract, so a caller branches on the code and not on a message
        # whose text belongs to the standard library.
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.INVALID_WHEN,
            "when must be a real UTC instant",
            value=when,
            dimension="when",
        ) from exc
    return when


def capture_provenance(*, who: str, when: str, why: str) -> Provenance:
    """Capture who, when and why as an immutable provenance value.

    All three are required and keyword-only, so no dimension can be supplied
    positionally into the wrong slot and none is silently defaulted. In
    particular ``when`` is never read from the clock: the caller states the
    instant, or the capture is refused.

    Raises :class:`ProvenanceCaptureError` on any structural failure. It
    fabricates nothing — no substitute actor, no invented instant, no inferred
    reason — because a fabricated provenance is worse than a refused one under
    Spine law 9.

    A thin wrapper over the constructor: :meth:`Provenance.__post_init__`
    applies the same invariants, so both construction paths enforce one rule
    set and neither is the safe one.
    """
    return Provenance(who=who, when=when, why=why)


def provenance_to_mapping(provenance: Provenance) -> dict[str, str]:
    """Render a capture as a plain mapping of the three dimensions.

    047 DECISION: this helper renders the current 047 implementation
    representation as a three-key, string-valued, JSON-compatible mapping.
    That shape is an implementation convenience — it **is** a format, chosen
    here — and is **not** a constitutional universal provenance wire schema.

    SOURCE FACT: provenance answers who, when and why.
    047 DECISION: those three are currently carried under these three keys.
    """
    if not isinstance(provenance, Provenance):
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.INVALID_INPUT_TYPE,
            "value must be a Provenance",
            value=provenance,
        )
    return {
        "who": provenance.who,
        "when": provenance.when,
        "why": provenance.why,
    }


def provenance_from_mapping(mapping: object) -> Provenance:
    """Rebuild a capture from a mapping, refusing anything it does not state.

    An unknown key is refused rather than dropped or absorbed
    (:attr:`ProvenanceErrorCode.UNKNOWN_DIMENSION`): this is how the three
    dimensions stay three, and how a caller cannot grow provenance a fourth by
    round-tripping one through storage.
    """
    if not isinstance(mapping, dict):
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.INVALID_INPUT_TYPE,
            "provenance mapping must be a dict",
            value=mapping,
        )
    # Ordered by their appearance in the mapping, not sorted: keys need not be
    # mutually orderable, and a mapping carrying both `1` and `None` must still
    # produce UNKNOWN_DIMENSION rather than leak the TypeError that comparing
    # them raises. Refusing a fourth dimension must not itself be refusable.
    known = frozenset(PROVENANCE_DIMENSIONS)
    unknown = [key for key in mapping if key not in known]
    if unknown:
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.UNKNOWN_DIMENSION,
            f"provenance carries only {', '.join(PROVENANCE_DIMENSIONS)}",
            value=", ".join(repr(key) for key in unknown),
            dimension=str(unknown[0]),
        )
    for dimension in PROVENANCE_DIMENSIONS:
        if dimension not in mapping:
            raise ProvenanceCaptureError(
                ProvenanceErrorCode.MISSING_DIMENSION,
                f"{dimension} is absent",
                dimension=dimension,
            )
    return capture_provenance(
        who=mapping["who"],
        when=mapping["when"],
        why=mapping["why"],
    )
