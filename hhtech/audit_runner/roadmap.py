"""Roadmap manifest parsing, scope resolution, and reference fields.

The Roadmap (Tier 3) is authoritative for what an artifact *owns*: its
declared path scope, dependencies (H/S/LS/G), unlocks (→), requirements,
BP/RMS citations, and Val/Done. Git diff is Tier 5 evidence of what
*changed* and is never a substitute for declared scope.

Row shape is Artifact 003's 25-field convention, one row per artifact:

    **042** · Record Model definition · `docs/constitution/record_model.md` ·
    Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE ·
    Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a · Req: RR-06 ·
    BP: §13 · RMS: §6 · H: 039 · S: — · LS: — · G: — · → 040 ·
    Val: … · Done: … · Why: … · Risk: medium · ∥: no

Parsing anchors on field *labels*, never on splitting by " · ", because a
free-text field (Name, Val, Why) may legitimately contain that separator.
"""

from __future__ import annotations

import glob as glob_module
import re
from dataclasses import dataclass
from pathlib import Path

from .errors import InputError

_ROW_PATTERN = re.compile(
    r"^\*\*(?P<id>\d{3})\*\*\s*·\s*(?P<name>.*?)\s*·\s*`(?P<path>[^`]*)`\s*·\s*"
    r"Own:\s*(?P<Own>.*?)\s*·\s*"
    r"RM:\s*(?P<RM>.*?)\s*·\s*"
    r"T:\s*(?P<T>.*?)\s*·\s*"
    r"R:\s*(?P<R>.*?)\s*·\s*"
    r"SoT:\s*(?P<SoT>.*?)\s*·\s*"
    r"Auth:\s*(?P<Auth>.*?)\s*·\s*"
    r"Canon:\s*(?P<Canon>.*?)\s*·\s*"
    r"CD:\s*(?P<CD>.*?)\s*·\s*"
    r"Ph/St:\s*(?P<PhSt>.*?)\s*·\s*"
    r"Req:\s*(?P<Req>.*?)\s*·\s*"
    r"BP:\s*(?P<BP>.*?)\s*·\s*"
    r"RMS:\s*(?P<RMS>.*?)\s*·\s*"
    r"H:\s*(?P<H>.*?)\s*·\s*"
    r"S:\s*(?P<S>.*?)\s*·\s*"
    r"LS:\s*(?P<LS>.*?)\s*·\s*"
    r"G:\s*(?P<G>.*?)\s*·\s*"
    r"→\s*(?P<Unlocks>.*?)\s*·\s*"
    r"Val:\s*(?P<Val>.*?)\s*·\s*"
    r"Done:\s*(?P<Done>.*?)\s*·\s*"
    r"Why:\s*(?P<Why>.*?)\s*·\s*"
    r"Risk:\s*(?P<Risk>.*?)\s*·\s*"
    r"∥:\s*(?P<Parallel>.*?)\s*$",
    re.MULTILINE,
)

FIELD_NAMES = (
    "id", "name", "path", "Own", "RM", "T", "R", "SoT", "Auth", "Canon",
    "CD", "PhSt", "Req", "BP", "RMS", "H", "S", "LS", "G", "Unlocks",
    "Val", "Done", "Why", "Risk", "Parallel",
)

# Fields whose value can name other artifacts, and the dependency semantics
# each one carries. Kept as data so the resolver never special-cases "H".
DEPENDENCY_FIELDS = (
    ("H", "hard dependency — must exist before this can be authored or finalized"),
    ("S", "soft dependency — supporting context, not a blocker"),
    ("LS", "lockstep — must land together in one authoring cycle"),
    ("G", "gate — must be passed before this may legally proceed"),
    ("Unlocks", "unlocks (→) — what becomes possible after completion"),
)

_EMPTY_VALUES = ("—", "n/a", "N/A", "", "-", "–")


def is_empty_field(value: str) -> bool:
    return value.strip() in _EMPTY_VALUES


@dataclass(frozen=True)
class ManifestRow:
    id: str
    name: str
    path: str
    fields: dict[str, str]
    raw: str

    def get(self, label: str) -> str:
        return self.fields[label]


def parse_all_rows(roadmap_text: str) -> dict[str, ManifestRow]:
    """Parse every manifest row in the Roadmap, keyed by three-digit ID.

    Used for neighbor discovery and for resolving referenced artifact IDs to
    their declared paths. Rows that do not match the 25-field shape are
    skipped here (a malformed *target* row still fails closed in
    find_manifest_row) so one malformed neighbour cannot break every audit.
    """
    rows: dict[str, ManifestRow] = {}
    for match in _ROW_PATTERN.finditer(roadmap_text):
        fields = {name: match.group(name).strip() for name in FIELD_NAMES}
        rows[fields["id"]] = ManifestRow(
            id=fields["id"], name=fields["name"], path=fields["path"],
            fields=fields, raw=match.group(0).strip(),
        )
    return rows


def find_manifest_row(roadmap_text: str, artifact_id: str) -> ManifestRow:
    """Locate and parse artifact_id's manifest row. Fail closed if absent or
    if the row does not match the expected 25-field shape."""
    line_pattern = re.compile(rf"^\*\*{artifact_id}\*\*\s*·.*$", re.MULTILINE)
    line_match = line_pattern.search(roadmap_text)
    if not line_match:
        raise InputError(f"artifact {artifact_id} not found in the Roadmap manifest")
    raw = line_match.group(0)

    match = _ROW_PATTERN.match(raw)
    if not match:
        raise InputError(
            f"artifact {artifact_id}'s Roadmap row does not match the expected "
            f"25-field shape; refusing to guess field boundaries: {raw!r}"
        )
    fields = {name: match.group(name).strip() for name in FIELD_NAMES}
    return ManifestRow(
        id=fields["id"], name=fields["name"], path=fields["path"],
        fields=fields, raw=raw,
    )


def previous_artifact_id(artifact_id: str) -> str | None:
    """The immediately preceding artifact in Roadmap order, or None for 001."""
    value = int(artifact_id)
    return f"{value - 1:03d}" if value > 1 else None


# ---------------------------------------------------------------------------
# Scope
# ---------------------------------------------------------------------------

SCOPE_FILE = "file"
SCOPE_GLOB = "glob"
SCOPE_DIRECTORY = "directory"


@dataclass(frozen=True)
class TargetScope:
    """The artifact's COMPLETE Roadmap-declared scope.

    `declared_path` is what the Roadmap says the artifact owns.
    `matched_files` is what currently exists under it — for a literal path
    that is the path itself whether or not the file exists yet (a not-yet-
    built artifact still owns its declared path); for a glob or directory it
    is every file currently matching, which may legitimately be empty.

    `multi_file` records that the entry declares many files under one
    responsibility (Roadmap §0.5 RULE G3), so the auditor is told the whole
    set is one artifact rather than several.
    """

    declared_path: str
    kind: str
    matched_files: tuple[str, ...]

    @property
    def is_glob(self) -> bool:
        return self.kind == SCOPE_GLOB

    @property
    def is_directory(self) -> bool:
        return self.kind == SCOPE_DIRECTORY

    @property
    def multi_file(self) -> bool:
        return self.kind in (SCOPE_GLOB, SCOPE_DIRECTORY) or len(self.matched_files) > 1

    @property
    def existing_files(self) -> tuple[str, ...]:
        return self.matched_files


def derive_target_scope(repo_root: Path, row: ManifestRow) -> TargetScope:
    """Resolve the artifact's complete declared scope. Fail closed if the
    Roadmap declares no usable path — never ask the model to guess scope."""
    raw_path = row.path.strip()
    if not raw_path or is_empty_field(raw_path):
        raise InputError(
            f"artifact {row.id} declares no resolvable path in its Roadmap row "
            f"(Path field is {row.path!r}); refusing to derive scope"
        )

    if "*" in raw_path:
        kind = SCOPE_GLOB
        pattern = raw_path
    elif raw_path.endswith("/"):
        kind = SCOPE_DIRECTORY
        pattern = raw_path.rstrip("/") + "/**"
    else:
        kind = SCOPE_FILE
        pattern = raw_path

    if kind == SCOPE_FILE:
        # A literal path is a declared file identity whether or not the file
        # exists yet. Non-existence is reported by the source resolver, not
        # by shrinking scope to nothing.
        matched_files: tuple[str, ...] = (raw_path,)
    else:
        matches = sorted(
            p for p in glob_module.glob(str(repo_root / pattern), recursive=True)
            if Path(p).is_file()
        )
        matched_files = tuple(str(Path(p).relative_to(repo_root)) for p in matches)

    return TargetScope(declared_path=raw_path, kind=kind, matched_files=matched_files)


# ---------------------------------------------------------------------------
# Field value parsing
# ---------------------------------------------------------------------------

_ARTIFACT_TOKEN = re.compile(r"\b(\d{3})\b")
_RANGE_TOKEN = re.compile(r"\b(\d{3})\s*[–—-]\s*(\d{3})\b")

# A range in a dependency/unlock field can span dozens of artifacts (e.g.
# "→ 040–059"). Expanding all of them would flood the context, so a range is
# represented by its endpoints only; the auditor is told it is a range.
_MAX_RANGE_EXPANSION = 2


def parse_artifact_references(value: str) -> tuple[list[str], list[str]]:
    """Split a manifest field into (artifact IDs, non-numeric tokens).

    Non-numeric tokens are real and must not be silently dropped: rows carry
    values like "PART IX", "all", "all models". They are reported to the
    auditor as declared-but-non-artifact references.
    """
    if is_empty_field(value):
        return [], []

    ids: list[str] = []
    text = value

    for start, end in _RANGE_TOKEN.findall(value):
        for endpoint in (start, end)[:_MAX_RANGE_EXPANSION]:
            if endpoint not in ids:
                ids.append(endpoint)
        text = text.replace(f"{start}–{end}", " ").replace(f"{start}-{end}", " ")

    for token in _ARTIFACT_TOKEN.findall(text):
        if token not in ids:
            ids.append(token)

    residue = _ARTIFACT_TOKEN.sub(" ", text)
    non_numeric = [
        tok.strip(" ,·")
        for tok in re.split(r"[,;]", residue)
        if tok.strip(" ,·") and not is_empty_field(tok)
    ]
    return ids, non_numeric


def parse_citation_numbers(citation: str) -> list[str]:
    """Parse a BP/RMS citation field into section number tokens.

    "§13" -> ["13"] · "§13.7a" -> ["13.7a"] · "§§2,3" -> ["2", "3"] ·
    "n/a" / "—" -> [].
    """
    if is_empty_field(citation):
        return []
    out: list[str] = []
    for token in citation.split(","):
        cleaned = token.strip().lstrip("§").strip()
        if cleaned and cleaned not in out:
            out.append(cleaned)
    return out


def parse_requirement_ids(req_field: str) -> list[str]:
    """Parse a Req field into requirement IDs, e.g. "BR-17,RR-01"."""
    if is_empty_field(req_field):
        return []
    return [
        match.group(0)
        for match in re.finditer(r"\b[A-Z]{2,3}-\d{2,3}\b", req_field)
    ]
