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
    """The encoded paths are 017's inventory, in 017's order, and nothing else."""
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


def test_canonical_root_is_the_family_declared_by_017():
    config = load_config()

    assert config["canonical_root"] == "canon/**"
    assert "canon/**" in DECLARATION.read_text(encoding="utf-8")


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


def test_no_zone_escapes_the_canonical_root():
    """Every encoded zone lives beneath ``canon/``. None may point outside it."""
    for zone in load_config()["zones"]:
        assert zone["path"].startswith("canon/"), zone["path"]
        assert ".." not in zone["path"], zone["path"]


def test_every_zone_carries_the_same_four_fields():
    """The shape is uniform, so a consumer can rely on it without probing."""
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
    """
    raw = ZONES.read_text(encoding="utf-8").lower()

    for forbidden in (
        "permission",
        "write_access",
        "allow",
        "deny",
        "authorization",
        "mutation_rule",
        "readonly",
        "writable",
    ):
        assert forbidden not in raw, forbidden


def test_artifact_022_does_not_read_this_file():
    """The dependency runs 017 -> 022 and 017 -> 023, never 023 -> 022.

    Roadmap row 023 declares ``H: 017,022``. Artifact 022 predates this file
    and must keep working without it, so a reference from the hook would
    invert the declared direction.
    """
    hook = (REPO_ROOT / ".claude/hooks/canon_deny.py").read_text(encoding="utf-8")
    body = hook.split('"""', 2)[-1]

    assert "zones.json" not in body
