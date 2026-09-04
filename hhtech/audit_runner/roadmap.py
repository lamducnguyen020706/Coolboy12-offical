"""Roadmap manifest row parsing and target-scope derivation.

BUILD spec §8, §9: the Roadmap is authoritative for a target artifact's
intended file/path scope. Git diff is evidence of what changed, never a
second source of what is allowed to change (§12 there, patch-standard.md §3).

Row shape (Artifact 003's 25-field convention), one row per artifact:

    **042** · Record Model definition · `docs/constitution/record_model.md` ·
    Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE ·
    Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a · Req: RR-06 ·
    BP: §13 · RMS: §6 · H: 039 · S: — · LS: — · G: — · → 040 ·
    Val: what a Record Model owns, enumerated · Done: definition ·
    Why: "the place where X lives" is not a definition · Risk: medium ·
    ∥: no

Parsing is anchored on the field *labels*, not on splitting the row by the
" · " separator, because a field's own value (Name, Val, Why) may itself
legitimately contain that separator or punctuation that looks like it.
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


@dataclass(frozen=True)
class ManifestRow:
    id: str
    name: str
    path: str
    fields: dict[str, str]
    raw: str

    def get(self, label: str) -> str:
        return self.fields[label]


def find_manifest_row(roadmap_text: str, artifact_id: str) -> ManifestRow:
    """Locate and parse artifact_id's manifest row. Raise InputError if absent
    or if the row does not match the expected 25-field shape."""
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


@dataclass(frozen=True)
class TargetScope:
    declared_path: str
    is_glob: bool
    is_directory: bool
    matched_files: tuple[str, ...]  # repo-relative, sorted, currently existing


def derive_target_scope(repo_root: Path, row: ManifestRow) -> TargetScope:
    """Derive the artifact's COMPLETE declared file/path scope from its
    Roadmap manifest Path field (BUILD spec §9). Never assumes one file.

    The Path field is one of:
      - a single literal file (e.g. docs/constitution/record_model.md)
      - a glob pattern (e.g. docs/models/*/model.md, tests/**)
      - a directory (e.g. .claude/commands/, src/coolboy12/production/) —
        every file currently under it is in scope
    """
    raw_path = row.path
    is_glob = "*" in raw_path
    is_directory = raw_path.endswith("/") and "*" not in raw_path

    if is_directory:
        pattern = raw_path.rstrip("/") + "/**"
    elif is_glob:
        pattern = raw_path
    else:
        pattern = raw_path

    if is_glob or is_directory:
        matches = sorted(
            p for p in glob_module.glob(str(repo_root / pattern), recursive=True)
            if Path(p).is_file()
        )
        matched_files = tuple(str(Path(p).relative_to(repo_root)) for p in matches)
    else:
        # A literal path is a declared file identity regardless of whether
        # it exists yet — a brand-new artifact has an empty git diff and no
        # file on disk, but its declared scope is still exactly this path
        # (BUILD spec §10). Non-existence is reported by sources.py's
        # target_files map, not by shrinking scope to nothing.
        matched_files = (raw_path,)

    return TargetScope(
        declared_path=raw_path,
        is_glob=is_glob,
        is_directory=is_directory,
        matched_files=matched_files,
    )


def parse_citation_numbers(citation: str) -> list[str]:
    """Parse a BP/RMS citation field into section number tokens.

    "§13" -> ["13"], "§13.7a" -> ["13.7a"], "§§2,3" -> ["2", "3"],
    "n/a" or "—" -> [].
    """
    if citation in ("n/a", "—", ""):
        return []
    return [
        tok.strip().lstrip("§").strip()
        for tok in citation.split(",")
        if tok.strip()
    ]
