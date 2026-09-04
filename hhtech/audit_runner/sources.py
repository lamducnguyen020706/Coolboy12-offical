"""Authoritative source collection.

Tiers, per audit-standard.md §1.1 / patch-standard.md §2:
  Tier 1  Blueprint sections the target's BP citation names
  Tier 2  RMS sections the target's RMS citation names
  Tier 3  the target's own manifest row + relevant Roadmap context
  Tier 4  the complete current content of every file in the target's scope
  Tier 5  git state (collected separately, gitstate.py)

Also loads audit-standard.md and patch-standard.md whole (they are audit
*procedure*, explicitly not architectural authority — the prompt built in
prompts.py says so directly, per audit-standard.md §0's own distinction).

Never truncates. If a cited section cannot be located, that is recorded as a
gap and reported to the caller rather than silently omitted (BUILD spec §36).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .errors import InputError
from .roadmap import ManifestRow, parse_citation_numbers

_HEADING = re.compile(r"^(#{1,6})\s+§?(\d+(?:\.\d+)*[a-z]?)\.?\s+.*$", re.MULTILINE)


@dataclass(frozen=True)
class ExtractedSection:
    citation: str
    heading: str
    body: str
    found: bool


def _extract_sections(text: str, numbers: list[str]) -> list[ExtractedSection]:
    headings = [
        (m.start(), len(m.group(1)), m.group(2), m.group(0).strip())
        for m in _HEADING.finditer(text)
    ]
    out: list[ExtractedSection] = []
    for number in numbers:
        hit = next((h for h in headings if h[2] == number), None)
        if hit is None:
            out.append(ExtractedSection(citation=number, heading="", body="", found=False))
            continue
        start, level, _num, heading_line = hit
        end = len(text)
        for h_start, h_level, _n, _line in headings:
            if h_start > start and h_level <= level:
                end = h_start
                break
        out.append(
            ExtractedSection(
                citation=number, heading=heading_line,
                body=text[start:end].rstrip(), found=True,
            )
        )
    return out


@dataclass(frozen=True)
class SourceBundle:
    blueprint_sections: list[ExtractedSection]
    rms_sections: list[ExtractedSection]
    audit_standard: str
    patch_standard: str
    roadmap_row_raw: str
    target_files: dict[str, str | None]  # repo-relative path -> content or None if missing
    unavailable: list[str]  # citations that could not be located — reported, never hidden


def collect_sources(
    repo_root: Path,
    row: ManifestRow,
    target_paths: tuple[str, ...],
    blueprint_path: Path,
    rms_path: Path,
    audit_standard_path: Path,
    patch_standard_path: Path,
) -> SourceBundle:
    blueprint_text = blueprint_path.read_text(encoding="utf-8")
    rms_text = rms_path.read_text(encoding="utf-8")

    bp_numbers = parse_citation_numbers(row.get("BP"))
    rms_numbers = parse_citation_numbers(row.get("RMS"))

    bp_sections = _extract_sections(blueprint_text, bp_numbers)
    rms_sections = _extract_sections(rms_text, rms_numbers)

    unavailable = [
        f"Blueprint §{s.citation}" for s in bp_sections if not s.found
    ] + [
        f"RMS §{s.citation}" for s in rms_sections if not s.found
    ]

    target_files: dict[str, str | None] = {}
    for rel_path in target_paths:
        full = repo_root / rel_path
        if full.is_file():
            target_files[rel_path] = full.read_text(encoding="utf-8", errors="replace")
        else:
            target_files[rel_path] = None

    return SourceBundle(
        blueprint_sections=bp_sections,
        rms_sections=rms_sections,
        audit_standard=audit_standard_path.read_text(encoding="utf-8"),
        patch_standard=patch_standard_path.read_text(encoding="utf-8"),
        roadmap_row_raw=row.raw,
        target_files=target_files,
        unavailable=unavailable,
    )


def collect_dependency_context(
    repo_root: Path, roadmap_text: str, h_field: str
) -> dict[str, str]:
    """Minimal H-dependency inspection, per audit-standard.md §5.1/§3.2 and
    patch-standard.md §2's imported rule: existence + declared row only,
    never a full audit of the dependency's own content, never recursive.
    """
    from .roadmap import find_manifest_row

    if h_field in ("—", "n/a", ""):
        return {}
    context: dict[str, str] = {}
    for token in re.split(r"[,\s]+", h_field.strip()):
        token = token.strip()
        if not re.fullmatch(r"\d{1,3}", token):
            continue
        dep_id = f"{int(token):03d}"
        try:
            dep_row = find_manifest_row(roadmap_text, dep_id)
        except InputError:
            context[dep_id] = "NOT FOUND IN ROADMAP"
            continue
        context[dep_id] = dep_row.raw
    return context
