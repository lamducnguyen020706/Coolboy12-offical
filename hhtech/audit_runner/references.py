"""Deterministic reference extraction.

audit-standard.md §6.2 makes citation coverage a floor, not a ceiling: an
artifact's own text names the sources its compliance depends on, and those
must be resolved and supplied, not left to the model's memory.

This module extracts references from text. It resolves nothing and reads no
file — resolution is sources.py's job — so the extraction rules stay
generic: no artifact ID, section, or invariant is ever special-cased.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# Reference syntaxes actually used across the Blueprint, RMS, Roadmap and the
# authored artifacts. Each pattern captures the canonical token form.
_ARTIFACT_REF = re.compile(r"\bArtifact\s+(\d{3})\b")

# Blueprint sections are recognised in two forms, and a bare flat `§N` is
# deliberately NOT one of them.
#
# A constitutional artifact numbers its own sections `## 1.` … `## 18.` and
# cross-references them inline — `(§8)`, `(§11, §14)`, "everything named in
# §16". Treating those as Blueprint citations made the resolver load whole
# Blueprint mega-sections that the artifact never cited: for Artifact 045 that
# was §12 (51KB), §15 (38KB), §14 (34KB), §9, §11 and §7 — 223KB, a third of
# the entire audit prompt, which is what pushed generation past the timeout.
#
# A dotted or lettered section (`§13.6a`, `§12.13`) cannot be a self-reference,
# because no artifact numbers its own sections that way, so it is attributed
# without needing the prefix. A flat `§N` requires the explicit word.
#
# The cost is a miss, not a mislabel: a genuinely bare `Blueprint §36` in prose
# is dropped. audit-standard.md §6.2 already treats an artifact's citations as
# "a floor, not a ceiling", the Roadmap row's declared `BP:` field is resolved
# by its own path, and a missing source is recoverable where a 223KB false
# positive is not.
_BLUEPRINT_SECTION_QUALIFIED = re.compile(r"Blueprint\s*:?\s*§+(\d+(?:\.\d+)*[a-z]?)\b")
_BLUEPRINT_SECTION_SUBSECTION = re.compile(r"§(\d+\.\d+[a-z]?)\b")

# The colon form is not optional decoration: every artifact's metadata header
# writes `RMS: §2`, so requiring whitespace after "RMS" mis-attributed every
# metadata citation in the repository to the Blueprint.
_RMS_SECTION = re.compile(r"RMS\s*:?\s*§+(\d+(?:\.\d+)*[a-z]?)\b")

# A citation run continues across commas: `RMS §2, §25` and
# `RMS §§22,23` name two RMS sections, not one RMS and one Blueprint. Without
# this the trailing member fell through to the Blueprint pattern.
_CITATION_RUN = re.compile(
    r"(Blueprint|RMS)\s*:?\s*((?:§+\d+(?:\.\d+)*[a-z]?)(?:\s*,\s*§*\d+(?:\.\d+)*[a-z]?)*)"
)
_RUN_MEMBER = re.compile(r"(\d+(?:\.\d+)*[a-z]?)")
_INVARIANT = re.compile(r"\bI-(\d{2,3})\b")
_ANTI_ORDERING = re.compile(r"\bX-(\d{2})\b")
_REQUIREMENT = re.compile(r"\b([A-Z]{2,3})-(\d{2,3})\b")
_SPINE_LAW = re.compile(r"\bSpine\s+(?:law\s+)?(\d{1,2})\b", re.IGNORECASE)

# Requirement prefixes are distinguished from invariants/anti-orderings by
# prefix, so "I-101" and "X-08" never leak into the requirement set.
_NON_REQUIREMENT_PREFIXES = frozenset({"I", "X", "AD", "P", "C", "G"})


@dataclass
class ReferenceSet:
    """Everything a piece of text explicitly names. Order-preserving and
    de-duplicated, so a label appears once no matter how often it is cited."""

    artifacts: list[str] = field(default_factory=list)
    blueprint_sections: list[str] = field(default_factory=list)
    rms_sections: list[str] = field(default_factory=list)
    invariants: list[str] = field(default_factory=list)
    anti_orderings: list[str] = field(default_factory=list)
    requirements: list[str] = field(default_factory=list)
    spine_laws: list[str] = field(default_factory=list)

    def merge(self, other: ReferenceSet) -> ReferenceSet:
        for name in (
            "artifacts", "blueprint_sections", "rms_sections", "invariants",
            "anti_orderings", "requirements", "spine_laws",
        ):
            mine = getattr(self, name)
            for value in getattr(other, name):
                if value not in mine:
                    mine.append(value)
        return self

    def is_empty(self) -> bool:
        return not any(
            (
                self.artifacts, self.blueprint_sections, self.rms_sections,
                self.invariants, self.anti_orderings, self.requirements,
                self.spine_laws,
            )
        )


def _dedup(values) -> list[str]:
    out: list[str] = []
    for value in values:
        if value not in out:
            out.append(value)
    return out


def extract_references(text: str) -> ReferenceSet:
    """Extract every explicit reference from a body of text.

    An `RMS §6` citation is attributed to the RMS, not the Blueprint: the
    bare-`§` pattern would otherwise claim it, and mislabelling a source is
    worse than missing one.
    """
    if not text:
        return ReferenceSet()

    # Citation runs first: they settle attribution for every member of
    # `RMS §2, §25`, so a trailing member never falls through to the Blueprint
    # pattern below.
    run_rms: list[str] = []
    run_blueprint: list[str] = []
    for source, run in _CITATION_RUN.findall(text):
        members = _RUN_MEMBER.findall(run)
        (run_rms if source == "RMS" else run_blueprint).extend(members)

    rms_sections = _dedup([*run_rms, *_RMS_SECTION.findall(text)])

    # Remove every resolved citation run before scanning for unqualified
    # subsections, so an RMS run is not re-read as a Blueprint reference.
    blueprint_scan = _CITATION_RUN.sub(" ", text)
    blueprint_sections = _dedup(
        [
            *run_blueprint,
            *_BLUEPRINT_SECTION_QUALIFIED.findall(blueprint_scan),
            *_BLUEPRINT_SECTION_SUBSECTION.findall(blueprint_scan),
        ]
    )

    requirements: list[str] = []
    for prefix, number in _REQUIREMENT.findall(text):
        if prefix in _NON_REQUIREMENT_PREFIXES:
            continue
        token = f"{prefix}-{number}"
        if token not in requirements:
            requirements.append(token)

    return ReferenceSet(
        artifacts=_dedup(_ARTIFACT_REF.findall(text)),
        blueprint_sections=blueprint_sections,
        rms_sections=rms_sections,
        invariants=_dedup(f"I-{n}" for n in _INVARIANT.findall(text)),
        anti_orderings=_dedup(f"X-{n}" for n in _ANTI_ORDERING.findall(text)),
        requirements=requirements,
        spine_laws=_dedup(_SPINE_LAW.findall(text)),
    )
