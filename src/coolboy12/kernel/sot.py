"""Source-of-truth classification mechanism — Artifact 050.

Artifact 050 · ``src/coolboy12/kernel/sot.py`` · Own: CONST · RM: all ·
T: code · R: VALID · SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no ·
Ph/St: P2/2c · Req: BR-108 · BP: §29.6a · RMS: §4 · H: 016,033 · S: — ·
LS: — · G: — · → P8 · Val: every record carries exactly one class ·
Done: enforced · Why: derived must never become authority · Risk: medium ·
∥: yes

What this module is
-------------------
The executable form of one rule, and nothing else::

    033  the envelope declares `sot_class`          — the field
    016  the Blueprint's five govern at record level — the vocabulary
    037  `sot_class` is present                      — the roster
      ↓
    050  `sot_class` holds exactly one of the five   ← this module

Blueprint §29.6a: *"Every data class in the system carries exactly one of
these, and the classification is part of its definition rather than a property
of how it happens to be stored."* This module checks that a value is exactly
one of the five and says which. It decides nothing else.

Artifact 037 checks that an envelope carries ``sot_class`` and deliberately
does not judge its value. This module judges the value and nothing about the
other six envelope fields. The two do not overlap.

Two classes of rule, kept apart
-------------------------------
``SOURCE FACT``
    Stated by Blueprint §29.6a, RMS §4, Artifact 016 or Artifact 033, and
    frozen there. The source facts are: there are exactly five record-level
    classes, spelled AUTHORITATIVE · DERIVED · CACHED · TEMPORARY · EXTERNAL;
    every data class carries exactly one; the class is part of the data
    class's definition, not a property of its storage; and the repository
    class DEV-ENV is not a record-level value (Artifact 016 §2, Artifact 033
    §5.7).

``050 DECISION``
    An operational choice made here so the rule can be enforced. None is a
    source fact, and a later authorial act may revise any of them:

    * values match exactly as §29.6a spells them — case-sensitive, never
      trimmed, never aliased;
    * a caller may pass a plain ``str`` or a :class:`SourceOfTruthClass`
      member; any other type, including another enum whose value happens to
      spell a class, is refused;
    * a built-in list, tuple, set, frozenset or dict holding two or more
      entries is refused as *multiple*; one holding fewer is refused as
      *invalid*, because a container is not a class either way;
    * an absent ``sot_class`` key and a ``None`` value both carry zero
      classes, and are refused as *missing*;
    * refusal messages never render the caller's value, so a hostile
      ``__repr__`` cannot break the refusal path (the defect found and fixed
      in Artifact 047).

What this module is not
-----------------------
Each boundary below is a later artifact's, or no artifact's:

* **Not canonicality** (Artifact 052; I-104). ``AUTHORITATIVE`` says where a
  fact lives. It does not say the fact is canon. A Registry definition, a
  Production State record and an Issue record may each be AUTHORITATIVE and
  none of them is World Canon. Nothing here takes, returns or implies a
  canonical flag.
* **Not authority** (Artifact 051). Who may commit, and what a Record governs,
  are not decided by a class.
* **Not derived-state discipline** (Artifact 053). This module may say a value
  is DERIVED. Whether it really is — whether it can be rebuilt with no loss —
  is 053's question and the rebuild drill's (§29.8). Nothing here rebuilds.
* **Not storage inference.** No function takes a path, a directory, a file
  name, a partition, a Kind or a model. A value found under ``derived/`` is
  whatever its ``sot_class`` says, and a missing class is refused rather than
  guessed from where the value sits.
* **Not a Record type.** Blueprint §13.7a prohibits a Universal Record Base.
  Records are taken as mappings, as in Artifact 037; no class is defined for
  six models to inherit.
* **Not a promotion path.** No function turns one class into another. In
  particular nothing turns EXTERNAL into AUTHORITATIVE.

On I-84 and the external-store rule. I-84: *"Every external store is DERIVED
or CACHED, never AUTHORITATIVE."* An *external store* (§26.2d) is a component
the system builds from canonical records; it is not the same thing as the
EXTERNAL class, which §29.6a defines as what *"lives outside coolboy12
entirely"*. Whether a given value is held by an external store is a fact about
where it is stored, and this module is forbidden to infer from storage. It
therefore cannot enforce I-84 on its own and does not claim to. It offers no
path by which any class — external store or not — becomes AUTHORITATIVE.

No model semantics
------------------
RMS §4 lists source-of-truth classification among the universal mechanisms.
The mechanism is shared by all six Record Models. No semantic of any model is:
the same five values mean the same five things in W, E, P, R, V and I, and what
a model does with its AUTHORITATIVE Records is that model's business (I-103).
"""

from __future__ import annotations

from collections.abc import Mapping
from enum import StrEnum
from typing import Final

__all__ = [
    "SOT_CLASS_FIELD",
    "SourceOfTruthClass",
    "SourceOfTruthError",
    "SourceOfTruthErrorCode",
    "validate_record_source_of_truth",
    "validate_source_of_truth_class",
]


SOT_CLASS_FIELD: Final = "sot_class"
"""SOURCE FACT: the envelope field's spelling, as Artifact 033 and RMS §4 fix it.

Only this spelling is read. No synonym is recognized.
"""


class SourceOfTruthClass(StrEnum):
    """SOURCE FACT: the five record-level classes of Blueprint §29.6a.

    Exactly five. ``DEV-ENV`` is not a member: it classifies repository paths,
    not records (Artifact 016 §2, Artifact 033 §5.7). No alias, synonym or
    ``UNKNOWN`` value exists — an absent or unrecognized class is an error, not
    a class.

    The meanings are §29.6a's, verbatim.
    """

    AUTHORITATIVE = "AUTHORITATIVE"
    """This is where the fact lives."""

    DERIVED = "DERIVED"
    """Recomputable with no loss from authoritative sources."""

    CACHED = "CACHED"
    """Recomputable and disposable, held only for speed."""

    TEMPORARY = "TEMPORARY"
    """Exists within one workflow and does not outlive it."""

    EXTERNAL = "EXTERNAL"
    """Lives outside coolboy12 entirely."""


class SourceOfTruthErrorCode(StrEnum):
    """Why a source-of-truth classification was refused."""

    MISSING_SOURCE_OF_TRUTH_CLASS = "MISSING_SOURCE_OF_TRUTH_CLASS"
    """Zero classes: the ``sot_class`` key is absent, or its value is ``None``."""

    INVALID_SOURCE_OF_TRUTH_CLASS = "INVALID_SOURCE_OF_TRUTH_CLASS"
    """A value that is not exactly one of the five."""

    MULTIPLE_SOURCE_OF_TRUTH_CLASSES = "MULTIPLE_SOURCE_OF_TRUTH_CLASSES"
    """Two or more classes offered at once. None is chosen."""

    INVALID_INPUT_TYPE = "INVALID_INPUT_TYPE"
    """A record that is not a mapping at all."""


class SourceOfTruthError(ValueError):
    """A classification was refused. ``code`` is the contract; the message is not."""

    def __init__(self, code: SourceOfTruthErrorCode, message: str) -> None:
        self.code = code
        super().__init__(f"{code.value}: {message}")


_VALID: Final = ", ".join(member.value for member in SourceOfTruthClass)

_CONTAINERS: Final = (list, tuple, set, frozenset, dict)
"""050 DECISION: the built-in shapes recognized as an attempt at plurality.

Matched by exact type, so no caller-defined ``__len__`` or ``__iter__`` runs.
"""


def validate_source_of_truth_class(value: object) -> SourceOfTruthClass:
    """Return the one class ``value`` names, or refuse it.

    Accepts exactly the five spellings of §29.6a, as a plain ``str`` or as a
    :class:`SourceOfTruthClass` member. Nothing is trimmed, case-folded,
    aliased or guessed, and nothing is chosen from a collection.

    Raises:
        SourceOfTruthError: ``MISSING_SOURCE_OF_TRUTH_CLASS`` for ``None``;
            ``MULTIPLE_SOURCE_OF_TRUTH_CLASSES`` for a container holding two or
            more entries; ``INVALID_SOURCE_OF_TRUTH_CLASS`` for anything else
            that is not exactly one of the five.
    """
    if value is None:
        raise SourceOfTruthError(
            SourceOfTruthErrorCode.MISSING_SOURCE_OF_TRUTH_CLASS,
            f"a source-of-truth class is required; exactly one of {_VALID}",
        )
    if type(value) is SourceOfTruthClass:
        return value
    if type(value) in _CONTAINERS:
        count = len(value)  # type: ignore[arg-type]
        if count >= 2:
            raise SourceOfTruthError(
                SourceOfTruthErrorCode.MULTIPLE_SOURCE_OF_TRUTH_CLASSES,
                f"a record carries exactly one source-of-truth class; "
                f"{count} were offered and none is chosen",
            )
        raise SourceOfTruthError(
            SourceOfTruthErrorCode.INVALID_SOURCE_OF_TRUTH_CLASS,
            f"a source-of-truth class is one value, not a container; "
            f"exactly one of {_VALID}",
        )
    # Exact type: a str subclass — including another enum whose value spells a
    # class — is refused rather than accepted by equality.
    if type(value) is str and value in SourceOfTruthClass.__members__:
        return SourceOfTruthClass[value]
    raise SourceOfTruthError(
        SourceOfTruthErrorCode.INVALID_SOURCE_OF_TRUTH_CLASS,
        f"not a record-level source-of-truth class; exactly one of {_VALID}",
    )


def validate_record_source_of_truth(record: object) -> SourceOfTruthClass:
    """Return the one class a record's ``sot_class`` carries, or refuse it.

    ``record`` is a mapping, as in Artifact 037 — no Record type is defined
    (Blueprint §13.7a). Only ``sot_class`` is read. No other field, and nothing
    about where the record is stored, influences the result.

    Raises:
        SourceOfTruthError: ``INVALID_INPUT_TYPE`` if ``record`` is not a
            mapping; ``MISSING_SOURCE_OF_TRUTH_CLASS`` if ``sot_class`` is
            absent; otherwise as :func:`validate_source_of_truth_class`.
    """
    if not isinstance(record, Mapping):
        raise SourceOfTruthError(
            SourceOfTruthErrorCode.INVALID_INPUT_TYPE,
            f"a record is a mapping carrying the envelope field {SOT_CLASS_FIELD!r}",
        )
    if SOT_CLASS_FIELD not in record:
        raise SourceOfTruthError(
            SourceOfTruthErrorCode.MISSING_SOURCE_OF_TRUTH_CLASS,
            f"the record carries no {SOT_CLASS_FIELD!r}; every data class "
            f"carries exactly one of {_VALID} (Blueprint §29.6a)",
        )
    return validate_source_of_truth_class(record[SOT_CLASS_FIELD])
