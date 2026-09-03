"""Bootstrap structural validator — Artifact 037.

Artifact 037 · ``src/coolboy12/bootstrap/validate.py`` · Own: CONST · RM: all ·
T: code · R: VALID · SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no ·
Ph/St: P1/1c · Req: BR-20 · BP: §13.7a · RMS: §20 · H: 033,035 · S: 036 ·
LS: — · G: — · → 038,111 · Val: well-formedness only — **nothing semantic** ·
Done: refuses semantic checks by design · Why: scope creep here creates a
universal semantic owner · Risk: medium · ∥: no

What this module is
-------------------
The last of the four bootstrap identity artifacts, and the narrowest::

    033  the envelope contract — seven fields, no eighth
    034  the identity grammar, frozen
    035  parse · format · identity-level resolution
    036  allocate · record · never reuse
    037  is this well-formed?  ← here
    038  the exit-P1 conformance gate

Blueprint §13.7a's shared-mechanism table states the scope in one line:

    | Structural validation | Is this a well-formed Record at all |
    | Kind legality, tier rules, relationship legality — all semantic |

Two columns, and the second is as binding as the first. What structural
validation *does* is ask whether a thing is well-formed. What it **does not
decide** is anything semantic — and the table names three examples rather than
drawing a boundary, so the rule is the category, not the list.

RMS §20 places this artifact precisely. Validation has four tiers:
*"constitutional invariant (108, Blueprint) · CONSTRAINT-DEFINITION (Registry:
the condition) · VALIDATION-RULE (Registry: the checking mechanism) ·
implementation validation (runtime, structural, shared)."* This module is the
fourth and only the fourth. RMS §10.6 `FROZEN` adds the rule that keeps the
tiers apart: *"Registry owns definitions for both; runtime validators implement
validation. **These are never collapsed.**"*

What it validates
-----------------
Row 037's hard dependencies are **033 and 035**, and both are load-bearing,
because a well-formed Record is well-formed in two respects:

* its **envelope** — exactly the seven fields Artifact 033 fixes, and no
  eighth (:func:`validate_envelope`);
* its **identity** — the four components of the frozen grammar
  (:func:`validate_identity`).

Row 038, the exit-P1 gate this artifact unlocks, asks for exactly that pair:
*"envelope is 7 fields; identity parses six partitions."*

What it refuses, by design
--------------------------
Row 037's ``Done`` is not *omits* semantic checks but **refuses** them, and its
``Why`` says what is at stake: *"scope creep here creates a universal semantic
owner."* Blueprint §13.7a lists the prohibitions this artifact could violate by
growing — **no Universal Record Base**, **no universal Record schema**, no
universal kind taxonomy, no universal lifecycle, no universal canonicality.

So nothing below asks, or can ask:

* what a kind *means*, or whether a kind exists — the Registry owns that
  (Blueprint §13.11, §9.4), and an unknown two-character code is well-formed;
* whether an ordinal was ever allocated, reused, or retired — Artifact 036
  owns the allocation record, and this module never opens it;
* whether an identity resolves to a Record, or what that Record contains;
* whether the slug is *correct* — Blueprint §13.9a: *"nothing resolves,
  matches, or validates against a slug"*;
* whether a Record is canonical, active, retired, or published — six models,
  six meanings (§13.7c), and none of them is universal;
* which source-of-truth class a value ought to be. Artifact 033 §5.7 is
  explicit that it *"declares the field. It does not create the vocabulary"*,
  and §13.7a assigns the *set* of five to the shared layer while leaving
  *"which class a model's data belongs to"* model-owned. Choosing is semantic,
  so no value in the envelope is inspected at all.

It also holds no state, opens no file, and mutates nothing — including its own
input. Artifact 035 owns parsing and every normalization decision; a validator
that corrected what it was given would be a second parser with a different
answer.

One parser, not two
-------------------
Where a component must be checked against the frozen grammar, this module
**delegates to Artifact 035** by constructing an :class:`Identity` and reading
the refusal, rather than restating the rules. That is the point of the layering:
035's contract is the only definition of a well-formed component, so a second
copy here could only ever drift from it.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Final

from coolboy12.bootstrap.identity import Identity, IdentityParseError

__all__ = [
    "ENVELOPE_FIELDS",
    "Finding",
    "ValidationCode",
    "ValidationResult",
    "validate_envelope",
    "validate_identity",
]


ENVELOPE_FIELDS: Final = (
    "partition",
    "kind",
    "object_id",
    "slug",
    "provenance",
    "registry_ref",
    "sot_class",
)
"""SOURCE-FROZEN: the universal envelope, in order. Exactly seven, no eighth.

RMS §4 freezes them and Artifact 033 is the repository's statement of that
contract — *"exactly seven fields, common to all six sovereign Record Models,
and no eighth"*. Row 033 names why it is CRITICAL: *"the historical failure
point — any eighth field universalizes a semantic."*

``tier`` and ``status`` are absent deliberately, and row 033's ``Val`` names
them: they are World Record Model properties, and ``status`` admits a value two
models can never reach (Blueprint §13.7, §13.7c). They are the two fields most
likely to be added back, which is why the refusal below is tested for them by
name and not only by arithmetic.

This tuple is a **field roster, not a schema**. Blueprint §13.7a prohibits a
Universal Record Base and a universal Record schema alike, so nothing here
declares a type, a default, a serialization rule, or an order of assignment —
Artifact 033 §9 records that no authoritative source establishes any of those.
"""

_IDENTITY_FIELDS: Final = ENVELOPE_FIELDS[:4]
"""The four envelope fields that are also identity components (§13.9a)."""


class ValidationCode(StrEnum):
    """Why a structure is not well-formed.

    037 DECISION: four codes, each naming one structural rule. Deliberately
    small — a large taxonomy here would be the first step toward the universal
    semantic owner row 037's ``Why`` warns about, because most of the
    distinctions worth drawing beyond these are distinctions of meaning.
    """

    INVALID_INPUT_TYPE = "INVALID_INPUT_TYPE"
    """The value handed in was not of a shape this module can inspect."""

    MISSING_ENVELOPE_FIELD = "MISSING_ENVELOPE_FIELD"
    """One of the seven universal fields is absent."""

    UNKNOWN_ENVELOPE_FIELD = "UNKNOWN_ENVELOPE_FIELD"
    """A field beyond the seven is present — the eighth-field failure."""

    INVALID_IDENTITY_STRUCTURE = "INVALID_IDENTITY_STRUCTURE"
    """A component does not satisfy the frozen identity grammar."""


@dataclass(frozen=True, slots=True)
class Finding:
    """One structural defect: what failed, and where.

    ``origin`` carries the Artifact 035 error code when the finding came from
    delegating to the parser, so a caller can see which frozen rule was broken
    without this module restating the rule itself.
    """

    code: ValidationCode
    detail: str
    field: str | None = None
    origin: str | None = None

    def __str__(self) -> str:
        where = f" [{self.field}]" if self.field else ""
        return f"{self.code.value}{where}: {self.detail}"


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """The answer, and the reasons.

    037 DECISION: a structured result rather than a bare ``bool``, so a caller
    that wants the reason does not have to re-derive it, and a caller that
    wants only the verdict can use the object in a boolean context.

    It is a *verdict about structure*. It says nothing about whether the thing
    described is a Record that should exist, means anything, or is canonical —
    those are the questions this artifact refuses.
    """

    findings: tuple[Finding, ...] = field(default_factory=tuple)

    @property
    def valid(self) -> bool:
        """Whether the structure is well-formed."""
        return not self.findings

    @property
    def codes(self) -> tuple[ValidationCode, ...]:
        """The codes of every finding, in the order they were found."""
        return tuple(finding.code for finding in self.findings)

    def __bool__(self) -> bool:
        return self.valid

    def __str__(self) -> str:
        if self.valid:
            return "VALID"
        return "INVALID: " + "; ".join(str(finding) for finding in self.findings)


def validate_identity(identity: object) -> ValidationResult:
    """Is this a well-formed identity?

    :param identity: an :class:`~coolboy12.bootstrap.identity.Identity`, or any
        object carrying the four component attributes.
    :returns: a :class:`ValidationResult`.

    **Delegates rather than restates.** The definition of a well-formed
    component is Artifact 035's, so this reconstructs the identity through 035
    and reports what 035 refuses. There is one parser in the repository and
    this is not it.

    A genuine :class:`Identity` is already well-formed — 035 validates on
    construction — so for that input this is a re-affirmation rather than a
    discovery. The case it exists for is the one where the four components
    arrive separately: out of an envelope, across a boundary, or from an object
    that never went through 035 at all. Row 038 asks the question of an
    envelope, and an envelope carries fields, not an ``Identity``.

    Nothing is mutated, normalized, or corrected. The result describes the
    input; it does not improve it.
    """
    components = {}
    for name in _IDENTITY_FIELDS:
        if not hasattr(identity, name):
            return ValidationResult(
                (
                    Finding(
                        ValidationCode.INVALID_INPUT_TYPE,
                        f"an identity carries {', '.join(_IDENTITY_FIELDS)}; "
                        f"{type(identity).__name__} has no {name!r}",
                        field=name,
                    ),
                )
            )
        components[name] = getattr(identity, name)

    return _validate_components(components)


def validate_envelope(envelope: Mapping[str, object]) -> ValidationResult:
    """Is this a well-formed Record envelope?

    :param envelope: a mapping of field name to value.
    :returns: a :class:`ValidationResult`.

    Two structural questions, and no third:

    1. **Are the fields exactly the seven?** Row 033's ``Val`` — *"exactly
       seven fields … `tier` and `status` absent"* — and row 038's exit-P1
       clause, *"envelope is 7 fields"*.
    2. **Are the four identity components well-formed?** Delegated to Artifact
       035, as in :func:`validate_identity`.

    **No value other than the four identity components is inspected**, and that
    is deliberate rather than unfinished. Artifact 033 §9 records that no
    authoritative source establishes a type, default or serialization rule for
    any of the seven, and §5.7 says of ``sot_class`` that 033 *"declares the
    field. It does not create the vocabulary."* Judging a provenance, a
    registry reference or a source-of-truth class is deciding what it should
    mean, and that is the scope creep row 037 exists to refuse.

    A mapping is taken rather than a Record object because Blueprint §13.7a
    prohibits a **Universal Record Base** and a **universal Record schema**.
    This module inspects a shape; it does not define a type for six models to
    inherit.

    037 DECISION: the input contract is :class:`collections.abc.Mapping`, and
    it is checked as one. An earlier revision probed for ``keys`` and
    ``__getitem__`` while the annotation promised a ``Mapping``, so an object
    that merely looked like one was accepted — the signature and the behaviour
    disagreed. They now say the same thing. This fixes the *shape* accepted and
    changes no rule about which keys matter or what any value may be.
    """
    if not isinstance(envelope, Mapping):
        return ValidationResult(
            (
                Finding(
                    ValidationCode.INVALID_INPUT_TYPE,
                    f"an envelope is a Mapping of field name to value; "
                    f"got {type(envelope).__name__}",
                ),
            )
        )

    present = set(envelope.keys())
    findings: list[Finding] = []

    for name in ENVELOPE_FIELDS:
        if name not in present:
            findings.append(
                Finding(
                    ValidationCode.MISSING_ENVELOPE_FIELD,
                    "the universal envelope carries exactly seven fields (RMS §4)",
                    field=name,
                )
            )

    for name in sorted(present - set(ENVELOPE_FIELDS)):
        findings.append(
            Finding(
                ValidationCode.UNKNOWN_ENVELOPE_FIELD,
                "there is no eighth universal field; an added one universalizes a "
                "semantic (Artifact 033, Blueprint §13.7a)",
                field=str(name),
            )
        )

    if all(name in present for name in _IDENTITY_FIELDS):
        findings.extend(
            _validate_components(
                {name: envelope[name] for name in _IDENTITY_FIELDS}
            ).findings
        )

    return ValidationResult(tuple(findings))


def _validate_components(components: Mapping[str, object]) -> ValidationResult:
    """Ask Artifact 035 whether these four components form an identity.

    The whole of this module's identity checking, in one place and in one
    direction: build through 035, and report its refusal. Nothing here knows
    what a partition code is, how wide an object identity runs, or which pair
    reserves the singleton marker — 035 knows, and is the only thing that
    should.

    A refusal is reported as a single finding rather than a list because 035
    raises on the first rule broken. That is a faithful account of what was
    asked, and inventing further findings would mean checking the rest here,
    which is the duplication this delegation exists to avoid.
    """
    try:
        Identity(**components)  # type: ignore[arg-type]
    except IdentityParseError as refusal:
        return ValidationResult(
            (
                Finding(
                    ValidationCode.INVALID_IDENTITY_STRUCTURE,
                    refusal.message,
                    field=refusal.component,
                    origin=refusal.code.value,
                ),
            )
        )
    return ValidationResult()
