"""Register lookup: Spine, invariants, anti-orderings, requirements.

An audit that needs invariant I-87 needs what I-87 *says*, not the label
"I-87". This module extracts the actual register text from the actual
documents, so nothing is reconstructed from the model's memory.

Register locations are discovered by heading/table shape, not by hardcoded
line numbers, so a re-versioned source document does not silently break
resolution — an unfound register is reported UNAVAILABLE, never faked.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Section-heading matcher shared with the section extractor: any markdown
# heading level, optional §, numeric section id.
_HEADING = re.compile(r"^(#{1,6})\s+§?(\d+(?:\.\d+)*[a-z]?)\.?\s+(.*)$", re.MULTILINE)

# A register row: "| I-87 | text | where |" or "| X-08 | order | reason | ... |"
_TABLE_ROW = re.compile(r"^\|\s*\**\s*([A-Z]{1,2}-\d{2,3})\s*\**\s*\|(.*)$", re.MULTILINE)


@dataclass(frozen=True)
class Section:
    """A located document section."""

    number: str
    heading: str
    body: str


@dataclass(frozen=True)
class RegisterEntry:
    """One resolved register row, with the document it actually came from."""

    entry_id: str
    text: str
    source_label: str


def find_section(text: str, number: str) -> Section | None:
    """Extract one numbered section, ending at the next heading of the same
    or shallower depth. Depth is compared *relatively*, so this works whether
    a document writes its top level as `#` (RMS) or `##` (Blueprint).
    """
    headings = [
        (m.start(), len(m.group(1)), m.group(2), m.group(0).strip())
        for m in _HEADING.finditer(text)
    ]
    hit = next((h for h in headings if h[2] == number), None)
    if hit is None:
        return None
    start, level, _number, heading_line = hit
    end = len(text)
    for h_start, h_level, _n, _line in headings:
        if h_start > start and h_level <= level:
            end = h_start
            break
    return Section(number=number, heading=heading_line, body=text[start:end].rstrip())


def find_section_by_title(text: str, title_pattern: str) -> Section | None:
    """Locate a section by its heading text — for registers that are named
    rather than numbered (the Roadmap's `PART IX — ANTI-ORDERINGS`)."""
    pattern = re.compile(rf"^(#{{1,6}})\s+.*{title_pattern}.*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(text)
    if match is None:
        return None
    level = len(match.group(1))
    start = match.start()
    end = len(text)
    for following in re.finditer(r"^(#{1,6})\s+.*$", text[match.end():], re.MULTILINE):
        if len(following.group(1)) <= level:
            end = match.end() + following.start()
            break
    return Section(
        number=match.group(0).strip().lstrip("# ").strip(),
        heading=match.group(0).strip(),
        body=text[start:end].rstrip(),
    )


def extract_register_entries(section_text: str, source_label: str) -> dict[str, RegisterEntry]:
    """Parse every `| ID | … |` row of a register section, keyed by ID."""
    entries: dict[str, RegisterEntry] = {}
    for match in _TABLE_ROW.finditer(section_text):
        entry_id = match.group(1)
        row = match.group(0).strip()
        if entry_id not in entries:
            entries[entry_id] = RegisterEntry(
                entry_id=entry_id, text=row, source_label=source_label
            )
    return entries


def find_prose_mentions(text: str, entry_id: str, source_label: str) -> RegisterEntry | None:
    """Find an ID stated in prose rather than a table row (RMS §26 lists its
    invariants as a sentence). Returns the sentence-ish span carrying it."""
    pattern = re.compile(rf"[^.\n·]*\b{re.escape(entry_id)}\b[^.\n·]*")
    match = pattern.search(text)
    if match is None:
        return None
    return RegisterEntry(
        entry_id=entry_id, text=match.group(0).strip(), source_label=source_label
    )


def resolve_ids(
    ids: list[str],
    registers: list[tuple[str, str]],
) -> tuple[dict[str, RegisterEntry], list[str]]:
    """Resolve register IDs against ordered (register_text, label) pairs.

    Returns (resolved, unresolved). An ID that no register carries is
    reported unresolved — never invented, never paraphrased.
    """
    resolved: dict[str, RegisterEntry] = {}
    unresolved: list[str] = []

    table_caches = [
        (extract_register_entries(section_text, label), section_text, label)
        for section_text, label in registers
    ]

    for entry_id in ids:
        found: RegisterEntry | None = None
        for table, section_text, label in table_caches:
            if entry_id in table:
                found = table[entry_id]
                break
            prose = find_prose_mentions(section_text, entry_id, label)
            if prose is not None:
                found = prose
                break
        if found is None:
            unresolved.append(entry_id)
        else:
            resolved[entry_id] = found

    return resolved, unresolved
