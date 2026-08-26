"""Alignment proofs for the Artifact 023 zone configuration.

Artifact 023's ``Val`` is *"zones match 017 exactly"*, so the check that
matters is not that ``zones.json`` is well-formed — it is that it agrees with
the declaration it encodes. These tests therefore **parse Artifact 017's own
zone inventory** out of ``docs/boundaries/canonical_zones.md`` and compare,
rather than asserting against a second hardcoded copy of the same list.

That direction matters. A test holding its own copy of the six zones would
pass while both the artifact and the test drifted away from 017 together; one
that reads 017 fails the moment either side moves. Artifact 017 stays the
single source of the zone inventory, exactly as its §4 states: *"This is the
complete zone inventory. Artifact 022 denies direct writes across it; Artifact
023 encodes it. Neither may add a zone, remove one, or reinterpret an owner."*

**What is source-required, and what is this artifact's own choice.** No source
defines a schema for ``zones.json``. The Roadmap fixes its path, its ``Val``
(*"zones match 017 exactly"*) and its ``Why`` (*"hook needs machine-readable
zones"*); Artifact 017 §12 fixes which list to match — *"§4 is the list it
must match"* — and 017 defines no identifiers, no descriptions, and no
metadata beyond that tree. So exactly three things are source-required: the
zone **paths**, their **Record Model owners**, and the **count**. Every field
*name* here (``artifact``, ``schema_version``, ``declared_by``,
``canonical_root``, ``id``, ``description``) is Artifact 023's own encoding
choice.

Tests below are grouped accordingly. The source-required group may not be
relaxed. The encoding-contract group fixes 023's output shape so Artifact 024
can consume it without probing — that is a real contract, but it is 023's,
not the Blueprint's, and this file does not pretend otherwise.

No test writes anything under ``canon/**``.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ZONES = REPO_ROOT / ".claude/hooks/zones.json"
DECLARATION = REPO_ROOT / "docs/boundaries/canonical_zones.md"

# Artifact 017 §4 renders the inventory as a tree, one zone per line:
#     ├── canon/world/**        W — World
_ZONE_LINE = re.compile(
    r"^[│├└─\s]*(canon/(\w+)/\*\*)\s+([WEPRVI])\s+—\s+(\w+)", re.MULTILINE
)


def load_config() -> dict:
    return json.loads(ZONES.read_text(encoding="utf-8"))


def declared_zones() -> list[tuple[str, str, str]]:
    """The (path, model_code, model_name) triples Artifact 017 declares."""
    section = DECLARATION.read_text(encoding="utf-8")
    found = [(m.group(1), m.group(3), m.group(4)) for m in _ZONE_LINE.finditer(section)]
    assert found, "Artifact 017's zone tree could not be parsed — the test is blind"
    return found


# --------------------------------------------------------------------------
# Val — zones match 017 exactly.
# --------------------------------------------------------------------------


def test_zone_paths_match_artifact_017_exactly():
    """The encoded paths are 017's inventory and nothing else.

    Compared as an ordered list. No source requires 023 to preserve 017's
    ordering — that part is determinism, chosen because 017's order is the
    obvious one and a stable file diffs cleanly. The membership, though, is
    the ``Val``, and it is exact in both directions: nothing missing, nothing
    extra.
    """
    config = load_config()

    assert [zone["path"] for zone in config["zones"]] == [
        path for path, _, _ in declared_zones()
    ]


def test_zone_owners_match_artifact_017_exactly():
    """Each zone carries the Record Model 017 assigns it.

    017 §4: neither 022 nor 023 "may add a zone, remove one, or reinterpret an
    owner".
    """
    config = load_config()
    declared = {path: code for path, code, _ in declared_zones()}

    assert {z["path"]: z["record_model"] for z in config["zones"]} == declared


def test_exactly_six_zones_and_no_seventh():
    """RMS fixes six sovereign Record Models; 017 §4 fixes six zones."""
    config = load_config()

    assert len(config["zones"]) == 6
    assert len(declared_zones()) == 6


def test_canonical_root_is_the_family_root_of_017_s_tree():
    """The root is the line 017 §4's tree hangs the six zones from.

    Asserting only that ``canon/**`` appears *somewhere* in 017 would pass on
    any incidental mention; the string occurs many times in that document.
    This pins it to the tree's own root line.
    """
    declaration = DECLARATION.read_text(encoding="utf-8")
    tree_root = re.search(r"^(canon/\*\*)\s*$", declaration, re.MULTILINE)

    assert tree_root, "017 §4's tree root line could not be found — the test is blind"
    assert load_config()["canonical_root"] == tree_root.group(1)


# --------------------------------------------------------------------------
# Structural integrity.
# --------------------------------------------------------------------------


def test_file_is_valid_json_and_deterministic():
    """Parses, and re-serializes to itself — no ambiguity in the encoding."""
    raw = ZONES.read_text(encoding="utf-8")
    config = json.loads(raw)

    assert json.dumps(config, indent=2, ensure_ascii=False) + "\n" == raw


def test_identifiers_and_paths_are_unique():
    config = load_config()
    ids = [zone["id"] for zone in config["zones"]]
    paths = [zone["path"] for zone in config["zones"]]

    assert len(set(ids)) == len(ids)
    assert len(set(paths)) == len(paths)


def test_zone_paths_follow_the_grammar_017_renders():
    """Every path is exactly ``canon/<name>/**``, the form 017 §4 uses.

    Stronger than "starts with canon/ and has no ``..``", which would admit
    ``canon//world/**``, ``canon/world/*``, ``canon/world`` and
    ``canon/../world/**``. The grammar is source-backed: 017 §4 renders all
    six zones in this one shape and no other.
    """
    grammar = re.compile(r"^canon/[a-z]+/\*\*$")

    for zone in load_config()["zones"]:
        assert grammar.fullmatch(zone["path"]), zone["path"]


def test_no_zone_escapes_the_canonical_root():
    """Belt and braces on the grammar: nothing traverses out of canon."""
    for zone in load_config()["zones"]:
        assert zone["path"].startswith("canon/"), zone["path"]
        assert ".." not in zone["path"], zone["path"]


def test_description_names_the_record_model_017_assigns():
    """``description`` is non-authoritative, but it is not free prose either.

    017 §4 writes each zone as ``canon/world/** W — World``. The description
    must name that model, so a reader cannot be told something 017 does not
    say. Nothing downstream may treat this string as semantics: the model
    codes are the machine-readable part, and 017 remains the meaning.
    """
    declared = {path: name for path, _, name in declared_zones()}

    for zone in load_config()["zones"]:
        assert declared[zone["path"]] in zone["description"], zone["path"]


def test_every_zone_carries_the_same_four_fields():
    """023's own encoding contract — not a source requirement.

    No source names a field of ``zones.json``. This assertion fixes the shape
    Artifact 023 emits so Artifact 024 can consume it without probing, and it
    doubles as the structural scope guard: a permission or mutation field
    cannot be added without failing here.
    """
    for zone in load_config()["zones"]:
        assert set(zone) == {"id", "path", "record_model", "description"}


# --------------------------------------------------------------------------
# Scope — 023 describes, it does not enforce.
# --------------------------------------------------------------------------


def test_configuration_encodes_no_permission_or_mutation_policy():
    """Artifact 023 answers what zones exist, never who may write.

    Write authority is Artifact 017's declaration and Artifact 022's
    enforcement. A permission rule encoded here would be a second, competing
    statement of the same boundary.

    Checked over the structure's *keys* rather than the raw text. A substring
    scan of the whole file would fail the day a description legitimately
    contained "allowed", which is a false positive that teaches people to
    weaken the guard.
    """
    forbidden = {
        "permission",
        "permissions",
        "write_access",
        "allow",
        "deny",
        "authorization",
        "mutation_rules",
        "readonly",
        "writable",
        "write",
    }

    def keys(node):
        if isinstance(node, dict):
            for key, value in node.items():
                yield key
                yield from keys(value)
        elif isinstance(node, list):
            for item in node:
                yield from keys(item)

    present = {key.lower() for key in keys(load_config())}

    assert present.isdisjoint(forbidden), present & forbidden


def test_artifact_022_does_not_read_this_file():
    """The dependency runs 017 -> 022 and 017 -> 023, never 023 -> 022.

    Roadmap row 023 declares ``H: 017,022``. Artifact 022 predates this file
    and must keep working without it, so a reference from the hook would
    invert the declared direction.
    """
    hook = (REPO_ROOT / ".claude/hooks/canon_deny.py").read_text(encoding="utf-8")
    body = hook.split('"""', 2)[-1]

    assert "zones.json" not in body
