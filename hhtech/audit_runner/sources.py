"""Deterministic source resolution.

Two things this module keeps strictly apart (they are not the same set):

    SOURCE SET   what the auditor is allowed and required to read
    AUDIT SCOPE  what the target artifact itself is judged on

A dependency artifact belongs in the Source Set and never in the Audit
Scope. Confusing the two is how a runner-side context gap turns into a
false finding against the target.

Every entry carries a status — AVAILABLE / UNAVAILABLE / NOT APPLICABLE /
NOT REQUIRED — established by actually touching the filesystem. Nothing is
reported read unless it was read, and nothing is reported missing unless it
was looked for.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .errors import InputError
from .references import ReferenceSet, extract_references
from .registers import find_section, find_section_by_title, resolve_ids
from .roadmap import (
    DEPENDENCY_FIELDS,
    ManifestRow,
    TargetScope,
    derive_target_scope,
    find_manifest_row,
    is_empty_field,
    parse_all_rows,
    parse_artifact_references,
    parse_citation_numbers,
    parse_requirement_ids,
    previous_artifact_id,
)

STATUS_AVAILABLE = "AVAILABLE"
STATUS_UNAVAILABLE = "UNAVAILABLE"
STATUS_NOT_APPLICABLE = "NOT APPLICABLE"
STATUS_NOT_REQUIRED = "NOT REQUIRED"

# Document discovery patterns — matched against the repository rather than
# hardcoded to a version-stamped filename, so a re-versioned source document
# resolves instead of silently reporting itself missing.
BLUEPRINT_GLOB = "docs/sources/*MASTER_BLUEPRINT*.md"
RMS_GLOB = "docs/sources/*RECORD_MODEL_SYSTEM*.md"
ROADMAP_GLOB = "docs/sources/*ROADMAP*.md"
AUDIT_STANDARD_PATH = "hhtech/standards/audit-standard.md"
PATCH_STANDARD_PATH = "hhtech/standards/patch-standard.md"
CLAUDE_CANDIDATES = ("CLAUDE.md", "docs/constitution/CLAUDE.md")

SPINE_SECTION = "10"
BLUEPRINT_INVARIANT_SECTION = "36"
RMS_INVARIANT_SECTION = "26"
ANTI_ORDERING_TITLE = r"ANTI-ORDERING"
GATES_TITLE = r"PART VIII"

# Whole documents small enough to supply in full. The Blueprint (600 KB) and
# the Roadmap (250 KB) are supplied by resolved section/row instead — every
# supplied piece is labelled individually, so the Source Set stays honest
# about exactly what the auditor received.
_WHOLE_DOCUMENT_LIMIT = 120_000

# A referenced artifact is supplied as context, not as an audit target. This
# caps how many are loaded so context stays bounded (§11) without dropping
# hard dependencies, which are always loaded first.
_MAX_CONTEXT_ARTIFACTS = 8


@dataclass(frozen=True)
class ResolvedSource:
    """One source, with the evidence status established by inspection."""

    label: str
    reason: str
    status: str
    path: str = ""
    section: str = ""
    content: str = ""
    detail: str = ""

    @property
    def is_available(self) -> bool:
        return self.status == STATUS_AVAILABLE


@dataclass
class SourceSet:
    """Ordered, de-duplicated set of everything supplied to the auditor."""

    entries: list[ResolvedSource] = field(default_factory=list)

    def add(self, source: ResolvedSource) -> None:
        for existing in self.entries:
            if existing.label == source.label:
                return
        self.entries.append(source)

    def has(self, label: str) -> bool:
        return any(entry.label == label for entry in self.entries)

    @property
    def available(self) -> list[ResolvedSource]:
        return [e for e in self.entries if e.status == STATUS_AVAILABLE]

    @property
    def unavailable(self) -> list[ResolvedSource]:
        return [e for e in self.entries if e.status == STATUS_UNAVAILABLE]


@dataclass(frozen=True)
class ScopedFile:
    path: str
    exists: bool
    content: str | None


@dataclass(frozen=True)
class AuditScope:
    """What the target artifact is judged on — never the Source Set."""

    artifact_id: str
    artifact_name: str
    declared_path: str
    kind: str
    multi_file: bool
    files: tuple[ScopedFile, ...]

    @property
    def existing_files(self) -> tuple[str, ...]:
        return tuple(f.path for f in self.files if f.exists)

    @property
    def missing_files(self) -> tuple[str, ...]:
        return tuple(f.path for f in self.files if not f.exists)


@dataclass
class ResolutionResult:
    row: ManifestRow
    scope: AuditScope
    target_scope: TargetScope
    source_set: SourceSet
    references: ReferenceSet
    dependency_context: list[dict]
    roadmap_text: str


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _discover(repo_root: Path, pattern: str, description: str) -> Path:
    matches = sorted(repo_root.glob(pattern))
    if not matches:
        raise InputError(
            f"{description} not found in this repository (looked for {pattern}); "
            "the runner does not audit without its authoritative sources"
        )
    if len(matches) > 1:
        raise InputError(
            f"{description} is ambiguous — {len(matches)} files match {pattern}: "
            f"{[str(m.relative_to(repo_root)) for m in matches]}; refusing to guess"
        )
    return matches[0]


class SourceResolver:
    """Resolves the complete bounded context for one artifact audit."""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self.blueprint_path = _discover(repo_root, BLUEPRINT_GLOB, "Master Blueprint")
        self.rms_path = _discover(repo_root, RMS_GLOB, "Record Model System")
        self.roadmap_path = _discover(repo_root, ROADMAP_GLOB, "Build Roadmap")

        for rel in (AUDIT_STANDARD_PATH, PATCH_STANDARD_PATH):
            if not (repo_root / rel).is_file():
                raise InputError(
                    f"required HHTECH standard {rel} is missing; the runner does "
                    "not audit without the standard that governs the audit"
                )

        self.blueprint_text = _read(self.blueprint_path)
        self.rms_text = _read(self.rms_path)
        self.roadmap_text = _read(self.roadmap_path)
        self.audit_standard = _read(repo_root / AUDIT_STANDARD_PATH)
        self.patch_standard = _read(repo_root / PATCH_STANDARD_PATH)
        self.all_rows = parse_all_rows(self.roadmap_text)

    # -- helpers ---------------------------------------------------------

    def _rel(self, path: Path) -> str:
        return str(path.relative_to(self.repo_root))

    def _add_file(
        self,
        source_set: SourceSet,
        rel_path: str,
        label: str,
        reason: str,
        *,
        limit: int = _WHOLE_DOCUMENT_LIMIT,
    ) -> bool:
        full = self.repo_root / rel_path
        if not full.is_file():
            source_set.add(
                ResolvedSource(
                    label=label, reason=reason, status=STATUS_UNAVAILABLE,
                    path=rel_path, detail="file does not exist in this repository",
                )
            )
            return False
        content = _read(full)
        if len(content) > limit:
            source_set.add(
                ResolvedSource(
                    label=label, reason=reason, status=STATUS_UNAVAILABLE,
                    path=rel_path,
                    detail=(
                        f"file is {len(content)} bytes, beyond this call's whole-document "
                        f"limit of {limit}; supplied by resolved section instead — do not "
                        "treat unsupplied parts of it as read"
                    ),
                )
            )
            return False
        source_set.add(
            ResolvedSource(
                label=label, reason=reason, status=STATUS_AVAILABLE,
                path=rel_path, content=content,
            )
        )
        return True

    def _add_section(
        self,
        source_set: SourceSet,
        document_text: str,
        document_label: str,
        document_path: str,
        number: str,
        reason: str,
    ) -> bool:
        section = find_section(document_text, number)
        label = f"{document_label} §{number}"
        if section is None:
            source_set.add(
                ResolvedSource(
                    label=label, reason=reason, status=STATUS_UNAVAILABLE,
                    path=document_path, section=f"§{number}",
                    detail="section number not located in the document",
                )
            )
            return False
        source_set.add(
            ResolvedSource(
                label=label, reason=reason, status=STATUS_AVAILABLE,
                path=document_path, section=f"§{number}", content=section.body,
            )
        )
        return True

    # -- resolution phases ------------------------------------------------

    def _resolve_mandatory_authority(self, source_set: SourceSet) -> None:
        """Layer A — always-required authority, per audit-standard.md §1.1."""
        source_set.add(
            ResolvedSource(
                label="Master Blueprint (document)",
                reason="Tier 1 architectural authority; supplied by resolved section",
                status=STATUS_AVAILABLE,
                path=self._rel(self.blueprint_path),
                content=(
                    f"Document located at {self._rel(self.blueprint_path)}, "
                    f"{len(self.blueprint_text)} bytes. Sections are supplied "
                    "individually below and each is listed in this Source Set. "
                    "Sections NOT listed were not supplied and must not be "
                    "treated as read."
                ),
            )
        )
        source_set.add(
            ResolvedSource(
                label="Record Model System (document)",
                reason="Tier 2 architectural authority, supplied in full",
                status=STATUS_AVAILABLE,
                path=self._rel(self.rms_path),
                content=self.rms_text,
            )
        )
        source_set.add(
            ResolvedSource(
                label="Build Roadmap (document)",
                reason="Tier 3 build decomposition; supplied by resolved row and part",
                status=STATUS_AVAILABLE,
                path=self._rel(self.roadmap_path),
                content=(
                    f"Document located at {self._rel(self.roadmap_path)}, "
                    f"{len(self.roadmap_text)} bytes, {len(self.all_rows)} manifest "
                    "rows parsed. Rows and parts are supplied individually below."
                ),
            )
        )
        source_set.add(
            ResolvedSource(
                label="hhtech/standards/audit-standard.md",
                reason="audit procedure (not architectural authority)",
                status=STATUS_AVAILABLE,
                path=AUDIT_STANDARD_PATH, content=self.audit_standard,
            )
        )
        source_set.add(
            ResolvedSource(
                label="hhtech/standards/patch-standard.md",
                reason="patch procedure (not architectural authority)",
                status=STATUS_AVAILABLE,
                path=PATCH_STANDARD_PATH, content=self.patch_standard,
            )
        )

        claude_found = False
        for candidate in CLAUDE_CANDIDATES:
            if (self.repo_root / candidate).is_file():
                claude_found = self._add_file(
                    source_set, candidate, f"{candidate} (session conduct)",
                    "standing operational instructions governing session conduct",
                )
                break
        if not claude_found:
            source_set.add(
                ResolvedSource(
                    label="CLAUDE.md (session conduct)",
                    reason="standing operational instructions",
                    status=STATUS_UNAVAILABLE,
                    detail=f"none of {list(CLAUDE_CANDIDATES)} exists in this repository",
                )
            )

        self._add_section(
            source_set, self.blueprint_text, "Blueprint",
            self._rel(self.blueprint_path), SPINE_SECTION,
            "the Spine — frozen constitutional core; mandatory for any Spine-touching pass",
        )

        anti = find_section_by_title(self.roadmap_text, ANTI_ORDERING_TITLE)
        source_set.add(
            ResolvedSource(
                label="Roadmap anti-ordering register",
                reason="prohibited build orders; mandatory for ordering checks",
                status=STATUS_AVAILABLE if anti else STATUS_UNAVAILABLE,
                path=self._rel(self.roadmap_path),
                content=anti.body if anti else "",
                detail="" if anti else "anti-ordering register section not located",
            )
        )

        gates = find_section_by_title(self.roadmap_text, GATES_TITLE)
        source_set.add(
            ResolvedSource(
                label="Roadmap gate register",
                reason="gate definitions governing whether this artifact may proceed",
                status=STATUS_AVAILABLE if gates else STATUS_UNAVAILABLE,
                path=self._rel(self.roadmap_path),
                content=gates.body if gates else "",
                detail="" if gates else "gate register section not located",
            )
        )

    def _resolve_citations(
        self, source_set: SourceSet, row: ManifestRow, references: ReferenceSet
    ) -> None:
        """Layers B and C — declared citations plus the target's own references."""
        declared_bp = parse_citation_numbers(row.get("BP"))
        declared_rms = parse_citation_numbers(row.get("RMS"))

        for number in declared_bp:
            self._add_section(
                source_set, self.blueprint_text, "Blueprint",
                self._rel(self.blueprint_path), number,
                f"declared BP citation on artifact {row.id}'s Roadmap row",
            )
        for number in declared_rms:
            self._add_section(
                source_set, self.rms_text, "RMS",
                self._rel(self.rms_path), number,
                f"declared RMS citation on artifact {row.id}'s Roadmap row",
            )

        # Citation coverage is a floor, not a ceiling (audit-standard §6.2):
        # sections the artifact itself cites are resolved too.
        for number in references.blueprint_sections:
            if number in declared_bp:
                continue
            self._add_section(
                source_set, self.blueprint_text, "Blueprint",
                self._rel(self.blueprint_path), number,
                "explicitly referenced by the target artifact's own text",
            )
        for number in references.rms_sections:
            if number in declared_rms:
                continue
            self._add_section(
                source_set, self.rms_text, "RMS",
                self._rel(self.rms_path), number,
                "explicitly referenced by the target artifact's own text",
            )

    def _resolve_registers(
        self, source_set: SourceSet, references: ReferenceSet, row: ManifestRow
    ) -> None:
        """Invariants, anti-orderings, Spine laws and requirements — resolved
        to their actual register text, never left as a bare label."""
        bp_register = find_section(self.blueprint_text, BLUEPRINT_INVARIANT_SECTION)
        rms_register = find_section(self.rms_text, RMS_INVARIANT_SECTION)

        registers: list[tuple[str, str]] = []
        if bp_register:
            registers.append((bp_register.body, f"Blueprint §{BLUEPRINT_INVARIANT_SECTION}"))
        if rms_register:
            registers.append((rms_register.body, f"RMS §{RMS_INVARIANT_SECTION}"))

        if not registers:
            source_set.add(
                ResolvedSource(
                    label="Invariant registers",
                    reason="invariant text required by cited invariants",
                    status=STATUS_UNAVAILABLE,
                    detail=(
                        f"neither Blueprint §{BLUEPRINT_INVARIANT_SECTION} nor "
                        f"RMS §{RMS_INVARIANT_SECTION} could be located"
                    ),
                )
            )

        if references.invariants and registers:
            resolved, unresolved = resolve_ids(references.invariants, registers)
            for entry_id, entry in resolved.items():
                source_set.add(
                    ResolvedSource(
                        label=f"Invariant {entry_id}",
                        reason="cited by the target artifact or its Roadmap row",
                        status=STATUS_AVAILABLE,
                        path=self._rel(self.blueprint_path)
                        if entry.source_label.startswith("Blueprint")
                        else self._rel(self.rms_path),
                        section=entry.source_label,
                        content=entry.text,
                    )
                )
            for entry_id in unresolved:
                source_set.add(
                    ResolvedSource(
                        label=f"Invariant {entry_id}",
                        reason="cited by the target artifact",
                        status=STATUS_UNAVAILABLE,
                        detail="not found in either invariant register",
                    )
                )
        elif not references.invariants:
            source_set.add(
                ResolvedSource(
                    label="Invariant lookup",
                    reason="no invariant is cited by this artifact or its row",
                    status=STATUS_NOT_REQUIRED,
                )
            )

        anti_entry = next(
            (e for e in source_set.entries if e.label == "Roadmap anti-ordering register"),
            None,
        )
        if references.anti_orderings and anti_entry and anti_entry.is_available:
            resolved, unresolved = resolve_ids(
                references.anti_orderings,
                [(anti_entry.content, "Roadmap anti-ordering register")],
            )
            for entry_id, entry in resolved.items():
                source_set.add(
                    ResolvedSource(
                        label=f"Anti-ordering {entry_id}",
                        reason="cited by the target artifact",
                        status=STATUS_AVAILABLE,
                        path=self._rel(self.roadmap_path), content=entry.text,
                    )
                )
            for entry_id in unresolved:
                source_set.add(
                    ResolvedSource(
                        label=f"Anti-ordering {entry_id}",
                        reason="cited by the target artifact",
                        status=STATUS_UNAVAILABLE,
                        detail="not found in the anti-ordering register",
                    )
                )

        # Requirements: the register is a known repository gap (audit-standard
        # §8.3 / CLAUDE.md). Report the state; never manufacture the text.
        declared_reqs = parse_requirement_ids(row.get("Req"))
        for req_id in dict.fromkeys([*declared_reqs, *references.requirements]):
            hits = [
                line.strip()
                for line in self.roadmap_text.splitlines()
                if req_id in line and not line.startswith("**")
            ]
            if hits:
                source_set.add(
                    ResolvedSource(
                        label=f"Requirement {req_id}",
                        reason="declared on the Roadmap row or cited by the artifact",
                        status=STATUS_AVAILABLE,
                        path=self._rel(self.roadmap_path),
                        content="\n".join(hits[:5]),
                    )
                )
            else:
                source_set.add(
                    ResolvedSource(
                        label=f"Requirement {req_id}",
                        reason="declared on the Roadmap row or cited by the artifact",
                        status=STATUS_UNAVAILABLE,
                        detail=(
                            "the authoritative requirement register is not present in "
                            "this repository; the requirement ID is preserved and its "
                            "text must NOT be inferred (audit-standard §8.3)"
                        ),
                    )
                )

    def _resolve_dependencies(
        self, source_set: SourceSet, row: ManifestRow, references: ReferenceSet
    ) -> list[dict]:
        """Layers D and E — H/S/LS/G/→, explicit artifact references, and the
        immediately previous artifact. Context only: never a second audit."""
        context: list[dict] = []
        seen: set[str] = {row.id}
        ordered_ids: list[tuple[str, str]] = []  # (artifact_id, why)

        for field_label, semantics in DEPENDENCY_FIELDS:
            value = row.get(field_label)
            ids, non_numeric = parse_artifact_references(value)
            context.append(
                {
                    "field": field_label,
                    "semantics": semantics,
                    "declared": value,
                    "artifact_ids": ids,
                    "non_artifact_tokens": non_numeric,
                    "empty": is_empty_field(value),
                }
            )
            for artifact_id in ids:
                if artifact_id not in seen:
                    seen.add(artifact_id)
                    ordered_ids.append((artifact_id, f"{field_label} dependency ({semantics})"))

        for artifact_id in references.artifacts:
            if artifact_id not in seen:
                seen.add(artifact_id)
                ordered_ids.append(
                    (artifact_id, "explicitly referenced by the target artifact's own text")
                )

        previous = previous_artifact_id(row.id)
        if previous and previous not in seen:
            seen.add(previous)
            ordered_ids.append((previous, "immediately previous artifact in Roadmap order"))

        # Universal context: any artifact whose Roadmap row unlocks "all" is
        # conformance context for every later artifact (this is how Artifact
        # 003's conventions arrive — derived from the Roadmap, not hardcoded).
        for other_id, other_row in self.all_rows.items():
            if other_id in seen or other_id >= row.id:
                continue
            unlocks = other_row.get("Unlocks").strip().lower()
            if unlocks == "all" or unlocks.startswith("all "):
                seen.add(other_id)
                ordered_ids.append(
                    (other_id, "universal conformance context (its Roadmap row unlocks `all`)")
                )

        loaded = 0
        for artifact_id, why in ordered_ids:
            dep_row = self.all_rows.get(artifact_id)
            if dep_row is None:
                source_set.add(
                    ResolvedSource(
                        label=f"Artifact {artifact_id} (Roadmap row)",
                        reason=why, status=STATUS_UNAVAILABLE,
                        detail="no manifest row with this ID exists in the Roadmap",
                    )
                )
                continue

            source_set.add(
                ResolvedSource(
                    label=f"Artifact {artifact_id} (Roadmap row)",
                    reason=why, status=STATUS_AVAILABLE,
                    path=self._rel(self.roadmap_path), content=dep_row.raw,
                )
            )

            if loaded >= _MAX_CONTEXT_ARTIFACTS:
                source_set.add(
                    ResolvedSource(
                        label=f"Artifact {artifact_id} (content)",
                        reason=why, status=STATUS_NOT_REQUIRED,
                        path=dep_row.path,
                        detail=(
                            "context-artifact budget reached; the declared row was "
                            "supplied but the file content was not — do not treat its "
                            "content as read"
                        ),
                    )
                )
                continue

            dep_path = dep_row.path.strip()
            if not dep_path or "*" in dep_path or dep_path.endswith("/"):
                source_set.add(
                    ResolvedSource(
                        label=f"Artifact {artifact_id} (content)",
                        reason=why, status=STATUS_NOT_APPLICABLE,
                        path=dep_path,
                        detail="declared scope is a directory or pattern, not a single file",
                    )
                )
                continue

            if self._add_file(
                source_set, dep_path, f"Artifact {artifact_id} (content)",
                f"{why} — supplied as CONTEXT ONLY, never as a second audit target",
            ):
                loaded += 1

        return context

    # -- entry point ------------------------------------------------------

    def resolve(self, artifact_id: str) -> ResolutionResult:
        row = find_manifest_row(self.roadmap_text, artifact_id)
        target_scope = derive_target_scope(self.repo_root, row)

        files: list[ScopedFile] = []
        target_text_parts: list[str] = []
        for rel_path in target_scope.matched_files:
            full = self.repo_root / rel_path
            if full.is_file():
                content = _read(full)
                files.append(ScopedFile(path=rel_path, exists=True, content=content))
                target_text_parts.append(content)
            else:
                files.append(ScopedFile(path=rel_path, exists=False, content=None))

        scope = AuditScope(
            artifact_id=row.id,
            artifact_name=row.name,
            declared_path=target_scope.declared_path,
            kind=target_scope.kind,
            multi_file=target_scope.multi_file,
            files=tuple(files),
        )

        references = extract_references("\n".join(target_text_parts))
        references.merge(extract_references(row.raw))

        source_set = SourceSet()
        self._resolve_mandatory_authority(source_set)

        source_set.add(
            ResolvedSource(
                label=f"Roadmap manifest row for artifact {row.id}",
                reason="the target artifact's own declared contract",
                status=STATUS_AVAILABLE,
                path=self._rel(self.roadmap_path), content=row.raw,
            )
        )

        for scoped in files:
            source_set.add(
                ResolvedSource(
                    label=f"TARGET {scoped.path}",
                    reason="Tier 4 — the artifact under audit (this is the Audit Scope)",
                    status=STATUS_AVAILABLE if scoped.exists else STATUS_UNAVAILABLE,
                    path=scoped.path,
                    content=scoped.content or "",
                    detail="" if scoped.exists else "declared by the Roadmap but not present on disk",
                )
            )

        self._resolve_citations(source_set, row, references)
        self._resolve_registers(source_set, references, row)
        dependency_context = self._resolve_dependencies(source_set, row, references)

        return ResolutionResult(
            row=row,
            scope=scope,
            target_scope=target_scope,
            source_set=source_set,
            references=references,
            dependency_context=dependency_context,
            roadmap_text=self.roadmap_text,
        )
