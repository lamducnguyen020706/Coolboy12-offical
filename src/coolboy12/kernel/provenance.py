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
``SOURCE-FROZEN``
    Stated by Blueprint §13.7a / §13.7b / §10 law 9 or RMS §18, and frozen
    there. This module implements such a rule and may not vary it.

``047 DECISION``
    An operational representation choice. Artifact 033 §5.5 names the
    ``provenance`` field and its three dimensions but establishes **no**
    internal representation — no field spelling, no text encoding, no instant
    format. Those are decided here for operational use, are **not** source
    facts, and carry no constitutional meaning. A later authorial act may
    revise any of them without touching the envelope.

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

No universal temporal model
---------------------------
Blueprint P-21 names several temporal axes — world-time, authoring sequence,
session, issue ordinal — and requires a temporal statement to name its axis.
``when`` below is **none of them**. It is a capture-time transport value: the
instant the caller states the capture happened. It is not world-time, not an
authoring ordinal, not a session, not an issue ordinal, and this module asserts
no relation between it and any model's temporal architecture (Artifact 054,
I-90). Nothing is defaulted to the clock: a caller states ``when`` or the
capture is refused, so no instant is ever silently invented.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
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

SOURCE-FROZEN (Blueprint §13.7b, RMS §18, row 047 ``Val``). The field spellings
are the sources' nouns rather than invented synonyms — ``actor``, ``author``,
``timestamp`` and ``reason`` are deliberately not used, because none is a
source term and each drags in a semantic the sources did not grant.
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

    SOURCE-FROZEN shape (Blueprint §13.7b, RMS §18). Frozen because a capture
    is a statement about a moment that has passed: it is superseded by a new
    capture, never edited in place, and this type gives no way to edit it.
    That is a value-semantics property of the dataclass and **not** a
    constitutional mutation lifecycle — canonical mutation travels the governed
    path (Spine law 2), which this module neither implements nor bypasses.

    It is not a Record, not an envelope, and not an eighth envelope field. The
    envelope is seven fields (RMS §4, Artifact 033) and holds *one* of them,
    ``provenance``; this is the value that field carries.
    """

    who: str
    """Who made this. Opaque text: this module reads no identity out of it."""

    when: str
    """When the capture happened, in the 047 DECISION instant spelling.

    A capture-time transport value, not a COOLBOY12 temporal axis.
    """

    why: str
    """Why it was made — the reason the caller recorded, uninterpreted."""


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
    """Require the 047 DECISION capture-instant spelling."""
    when = _check_text(value, "when")
    if not _WHEN_PATTERN.match(when):
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.INVALID_WHEN,
            "when must be a UTC instant such as 2026-09-20T12:00:00Z",
            value=when,
            dimension="when",
        )
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
    """
    return Provenance(
        who=_check_text(who, "who"),
        when=_check_when(when),
        why=_check_text(why, "why"),
    )


def provenance_to_mapping(provenance: Provenance) -> dict[str, str]:
    """Render a capture as a plain mapping of the three dimensions.

    047 DECISION: exactly three string-valued keys, JSON-compatible, so the
    value crosses a serialization boundary without this module introducing a
    format of its own.
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
    unknown = sorted(set(mapping) - set(PROVENANCE_DIMENSIONS))
    if unknown:
        raise ProvenanceCaptureError(
            ProvenanceErrorCode.UNKNOWN_DIMENSION,
            f"provenance carries only {', '.join(PROVENANCE_DIMENSIONS)}",
            value=", ".join(str(key) for key in unknown),
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
