"""Artifact 030 — P0 conformance suite. The exit-P0 gate.

Roadmap row 030 verbatim:

    **030** · P0 conformance suite · `tests/conformance/p0.py` · Own: CONST ·
    RM: n/a · T: test · R: PROOF · SoT: DEV-ENV · Auth: none · Canon: n/a ·
    CD: no · Ph/St: P0/0f · Req: BR-01…BR-07 · BP: §7,§9.5,§10 · RMS: §2 ·
    H: 001–029 · S: — · LS: — · G: **exit-P0** · → P1 ·
    Val: tree, boundaries, hooks, 108-register present; zero current COM
    terms · Done: green · Why: no semantics before the foundation holds ·
    Risk: low · ∥: no

The question this suite answers is whether the P0 **foundation** is
structurally present — not whether anything means what it will eventually
mean. P0 is pre-semantic by construction: there is no Record Model, no
Registry, no canon, no runtime. So every check here is deterministic, static
and offline, and reads the repository rather than trusting a declaration
about it.

**What this suite must never do.** It must not assert that six model schemas
are complete, that Registry definitions are active, that canonical records
exist, or that simulation, rendering, search or any adapter provider works.
Those belong to later phases, and asserting them here would turn the exit-P0
gate into a claim the repository cannot support.

**Not-yet-testable is not a pass, and the gate now behaves accordingly.** Two
of the seven gated requirements have no P0 artifact to test — see
``test_br03`` and ``test_br05`` — and they are reported through Artifact 011's
harness as skips carrying a reason, never as green checks. Artifact 011 exists
for exactly this: *"an unavailable check is never represented as a successful
proof."*

But a pytest skip does not change an exit status, so this suite once said that
sentence and then exited 0 with both requirements unproven.
``test_exit_p0_gate_is_not_green_while_a_gated_requirement_is_unresolved``
carries the consequence: while anything in BR-01…BR-07 is unresolved, the gate
fails. **It fails today.** That is the truthful state and not a defect in the
repository — the Roadmap assigns no P0 artifact to BR-03, and BR-05's only
carrier is artifact 062 in P3. Closing that gap is an authorial act. This
suite may report it; it may not assume it away.

**Collection.** The Roadmap fixes this file at ``p0.py``, which does not match
pytest's ``test_*.py`` discovery pattern, so a bare ``pytest`` run does not
collect it. That is the Roadmap's path, not an oversight to correct here, and
Artifact 011's ``harness.py`` sits at a Roadmap path the same way. Run the
gate explicitly::

    pytest tests/conformance/p0.py

Blueprint §7 (design principles), §9.5 (execution environment), §10 (the
Spine). RMS §2. Depends on Artifacts 001–029.
"""

from __future__ import annotations

import ast
import importlib.util
import json
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ROADMAP = REPO_ROOT / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"
REGISTER = REPO_ROOT / "tests/constitutional/register.md"
ADAPTERS = REPO_ROOT / "src/coolboy12/adapters"
CLAUDE_DIR = REPO_ROOT / ".claude"


def _harness():
    """Artifact 011's harness, loaded by path.

    ``src/`` and ``tests/`` carry no ``__init__.py`` — the project uses
    implicit namespace packages — so the harness is loaded the way the
    repository's other suites load path-addressed modules.
    """
    path = REPO_ROOT / "tests/constitutional/harness.py"
    spec = importlib.util.spec_from_file_location("coolboy12_constitutional_harness", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


harness = _harness()


# ---------------------------------------------------------------------------
# The P0 artifact table, transcribed from Roadmap rows 001–029.
#
# Each entry carries the check its own Role justifies, because "present" means
# different things for a contract document, a parseable config and an empty
# shell. Requiring implementation of a documentation artifact would fail the
# gate on artifacts that are correct.
# ---------------------------------------------------------------------------

DOC_ARTIFACTS = {
    "002": ("README.md", "BR-02"),
    "003": ("docs/conventions/artifact_conventions.md", "BR-01"),
    "004": ("CLAUDE.md", "BR-01,BR-07,BR-17"),
    "013": ("docs/boundaries/version_control.md", "BR-21"),
    "014": ("docs/boundaries/environment.md", "BR-06"),
    "015": ("docs/boundaries/secrets.md", "BR-06"),
    "016": ("docs/boundaries/source_of_truth.md", "BR-04,BR-107,BR-108"),
    "017": ("docs/boundaries/canonical_zones.md", "BR-04"),
    "018": ("docs/conventions/roles.md", "BR-01"),
    "019": ("docs/conventions/restart.md", "BR-104"),
    "020": ("docs/conventions/rebuild.md", "BR-107"),
}

CONFIG_ARTIFACTS = {
    "005": ("pyproject.toml", "BR-06"),
    "006": ("uv.lock", "BR-06"),
    "023": (".claude/hooks/zones.json", "BR-04"),
    "024": (".claude/settings.json", "BR-06"),
}

CODE_ARTIFACTS = {
    "021": ("src/coolboy12/bootstrap/config.py", "BR-06"),
    "022": (".claude/hooks/canon_deny.py", "BR-07"),
}

TEST_ARTIFACTS = {
    "011": ("tests/constitutional/harness.py", "BR-113"),
    "012": ("tests/constitutional/register.md", "BR-113"),
}

COMMAND_ARTIFACTS = {
    "025": (".claude/commands/propose.md", "BR-14"),
    "026": (".claude/commands/validate.md", "BR-01"),
    "027": (".claude/commands/rebuild.md", "BR-107"),
}

# Artifact 028's four refusing surfaces, with the phase each names as its
# unlock. Row 028's Val: "each refuses with a reason and the unlocking phase".
REFUSING_COMMANDS = {
    "gate": "P5",
    "simulate": "P9",
    "render": "P13",
    "brief": "P17",
}

# Artifact 029's eleven boundaries (Blueprint §26.3a rows A-1 … A-11).
ADAPTER_SHELLS = {
    "a01_deconstruction": "A-01",
    "a02_vision_analysis": "A-02",
    "a03_visual_index": "A-03",
    "a04_search_index": "A-04",
    "a05_causal_graph_traversal": "A-05",
    "a06_simulation_numerics": "A-06",
    "a07_sensitivity_calibration": "A-07",
    "a08_rendering": "A-08",
    "a09_index_query_store": "A-09",
    "a10_public_viewer": "A-10",
    "a11_version_control": "A-11",
}


# The complete set of files Artifact 001 placed under canon/: one PURPOSE.md
# at the root and one per partition. Pinned as exact paths rather than
# exempting the *name* ``PURPOSE.md``, which would have let arbitrary
# canonical data pass by being called that — including at a path no partition
# owns. No future canonical structure is anticipated here; when the Mutation
# Coordinator (Artifact 152) makes canonical writes legal, this set is
# expected to be revisited.
P0_CANON_FILES = {
    "canon/PURPOSE.md",
    "canon/epistemic/PURPOSE.md",
    "canon/issue/PURPOSE.md",
    "canon/production/PURPOSE.md",
    "canon/registry/PURPOSE.md",
    "canon/visual/PURPOSE.md",
    "canon/world/PURPOSE.md",
}


def missing(paths: dict[str, tuple[str, str]]) -> list[str]:
    """Artifacts whose declared path is absent, named for the failure text."""
    return [
        f"Artifact {artifact} ({requirement}): expected file missing: {relative}"
        for artifact, (relative, requirement) in sorted(paths.items())
        if not (REPO_ROOT / relative).exists()
    ]


# ---------------------------------------------------------------------------
# Val — tree.
# ---------------------------------------------------------------------------


def test_p0_frozen_expectations_still_match_the_roadmap():
    """Drift guard for the tables above.

    Those tables are a frozen P0 contract, which is fine — but frozen against
    what? If the Roadmap changed and this file did not, every check would keep
    passing against a stale expectation and the gate would be quietly
    meaningless. So the few numbers that define the contract's *shape* are
    re-read from the Roadmap rows they were transcribed from.

    Deliberately not a Roadmap parser. It checks the counts and identifiers
    that would reveal drift, not the content of 490 rows — that would make
    Artifact 030 a second source of truth, which it must never be.
    """
    roadmap = ROADMAP.read_text(encoding="utf-8")

    row_028 = re.search(r"^\*\*028\*\*.*$", roadmap, re.MULTILINE)
    row_029 = re.search(r"^\*\*029\*\*.*$", roadmap, re.MULTILINE)
    row_030 = re.search(r"^\*\*030\*\*.*$", roadmap, re.MULTILINE)
    assert row_028 and row_029 and row_030, "Roadmap rows 028–030 not found"

    # Row 030 gates BR-01…BR-07. If that range moves, the seven explicit
    # requirement tests below are gating the wrong thing.
    assert "Req: BR-01…BR-07" in row_030.group(0), (
        f"Roadmap row 030 no longer gates BR-01…BR-07: {row_030.group(0)[:200]}"
    )

    # Row 028 names the four refusing commands.
    for command in REFUSING_COMMANDS:
        assert f"`{command}`" in row_028.group(0), (
            f"Roadmap row 028 no longer names the {command!r} command"
        )
    assert len(REFUSING_COMMANDS) == 4

    # Row 029 fixes eleven adapter boundary shells.
    assert "eleven adapter boundary shells" in row_029.group(0), (
        "Roadmap row 029 no longer declares eleven adapter boundary shells"
    )
    numbers = sorted(int(identifier.split("-")[1]) for identifier in ADAPTER_SHELLS.values())
    assert numbers == list(range(1, 12)), f"adapter identifiers are not A-01…A-11: {numbers}"

    # Every P0 artifact appears in exactly one table.
    tables = (DOC_ARTIFACTS, CONFIG_ARTIFACTS, CODE_ARTIFACTS, TEST_ARTIFACTS, COMMAND_ARTIFACTS)
    identifiers = [artifact for table in tables for artifact in table]
    duplicates = sorted({a for a in identifiers if identifiers.count(a) > 1})
    assert not duplicates, f"artifact declared in more than one table: {duplicates}"

    # And each path this suite expects is the path its Roadmap row declares.
    #
    # Rows whose declared path is `/` are exempt, and the exemption is the
    # Roadmap's own doing: 002, 005, 006, 007, 008 and 009 place their
    # artifact at the repository root without naming a file, because the
    # concrete filename is an implementation choice recorded elsewhere —
    # `uv.lock` is an author ruling at GAP-G, not a Roadmap declaration.
    # Asserting a filename the source never states would be inventing one.
    unverifiable: list[str] = []
    for table in tables:
        for artifact, (relative, _) in table.items():
            row = re.search(rf"^\*\*{artifact}\*\* · [^·]+· `([^`]+)`", roadmap, re.MULTILINE)
            assert row, f"Roadmap row {artifact} not found, or its path field changed shape"
            declared = row.group(1)
            if declared == "/":
                unverifiable.append(f"{artifact} ({relative})")
                continue
            assert declared.lstrip("/") == relative or relative.endswith(declared.lstrip("/")), (
                f"Artifact {artifact}: this suite expects {relative}, "
                f"but Roadmap row {artifact} declares {declared}"
            )

    # Recorded, not silently ignored: these are the rows whose filename this
    # gate cannot verify against the source.
    assert sorted(unverifiable) == ["002 (README.md)", "005 (pyproject.toml)", "006 (uv.lock)"], (
        "the set of rows declaring a bare `/` path has changed; "
        f"this gate now cannot verify: {sorted(unverifiable)}"
    )


def test_p0_repository_foundation_exists():
    """Artifact 001's tree and the P0 artifacts the Roadmap places in it."""
    absent = missing(DOC_ARTIFACTS | CONFIG_ARTIFACTS | CODE_ARTIFACTS
                     | TEST_ARTIFACTS | COMMAND_ARTIFACTS)

    assert not absent, "P0 foundation incomplete:\n  " + "\n  ".join(absent)


def test_p0_declared_directories_exist():
    """The partitions and package roots Artifact 001 established.

    Presence only. What lives in ``canon/`` is a P5-and-later question, and
    this suite must not imply otherwise.
    """
    required = [
        "canon", "derived", "docs/boundaries", "docs/conventions", "docs/sources",
        "src/coolboy12", "src/coolboy12/adapters", "src/coolboy12/bootstrap",
        "tests/conformance", "tests/constitutional", ".claude/commands", ".claude/hooks",
    ]
    absent = [name for name in required if not (REPO_ROOT / name).is_dir()]

    assert not absent, f"expected directories missing: {absent}"


def test_p0_config_artifacts_parse():
    """``T: config`` means parseable, not merely present.

    A JSON config that exists and cannot be read is not a foundation.
    """
    for artifact, (relative, requirement) in sorted(CONFIG_ARTIFACTS.items()):
        path = REPO_ROOT / relative
        raw = path.read_bytes()

        assert raw.strip(), f"Artifact {artifact} ({requirement}): {relative} is empty"

        if path.suffix == ".json":
            try:
                json.loads(raw.decode("utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError) as error:
                pytest.fail(
                    f"Artifact {artifact} ({requirement}): {relative} is not valid JSON — {error}")
        elif path.suffix in (".toml", ".lock"):
            try:
                tomllib.loads(raw.decode("utf-8"))
            except (tomllib.TOMLDecodeError, UnicodeDecodeError) as error:
                pytest.fail(
                    f"Artifact {artifact} ({requirement}): {relative} is invalid TOML — {error}")
        else:
            pytest.fail(
                f"Artifact {artifact} ({requirement}): {relative} has no parser in this suite — "
                "add one rather than letting the file pass unparsed")


def test_p0_pyproject_declares_the_project_and_its_tooling():
    """Parsed structure, not a substring.

    Artifacts 005, 007 and 008 all live inside this one file, so the gate
    reads it as data: a ``[tool.ruff]`` heading sitting inside a comment
    would satisfy a text search and configure nothing.
    """
    config = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    tools = config.get("tool", {})

    assert config.get("project", {}).get("name") == "coolboy12", \
        f"Artifact 005 (BR-06): [project].name is {config.get('project', {}).get('name')!r}"
    assert isinstance(tools.get("pytest", {}).get("ini_options"), dict), \
        "Artifact 007 (BR-06): [tool.pytest.ini_options] missing from pyproject.toml"
    assert "ruff" in tools, \
        "Artifact 008 (BR-06): [tool.ruff] missing from pyproject.toml"


# ---------------------------------------------------------------------------
# Val — boundaries.  Blueprint §9.5.
# ---------------------------------------------------------------------------


def test_p0_environment_boundary_states_the_execution_ordering():
    """§9.5 — the environment runs coolboy12 and does not define it.

    The ordering is what the boundary exists to fix: an environment described
    as a domain, a partition or an engine would have made the tooling the
    architecture (P-33).
    """
    body = (REPO_ROOT / "docs/boundaries/environment.md").read_text(encoding="utf-8")
    flowed = " ".join(body.split())

    for layer in ("AUTHOR", "AI-ASSISTED DEVELOPMENT", "EXECUTION ENVIRONMENT",
                  "COOLBOY12 SYSTEM", "EXTERNAL CAPABILITY COMPONENTS"):
        assert layer in body, f"Artifact 014: execution ordering missing layer {layer!r}"

    assert re.search(r"never be described as a domain, a partition, an engine, a primitive",
                     flowed, re.IGNORECASE), \
        "Artifact 014: the environment is not declared to be outside coolboy12's own categories"


def test_p0_source_of_truth_boundary_separates_authority_from_location():
    """Artifact 016 — SoT class is where a thing is held, not what governs it."""
    flowed = " ".join((REPO_ROOT / "docs/boundaries/source_of_truth.md")
                      .read_text(encoding="utf-8").split())

    for sot_class in ("AUTHORITATIVE", "DERIVED", "CACHED", "TEMPORARY", "EXTERNAL", "DEV-ENV"):
        assert sot_class in flowed, f"Artifact 016: source-of-truth class {sot_class!r} not declared"


def test_p0_canonical_zone_declaration_names_the_canonical_root():
    """Artifact 017 — the zones the deny hook enforces."""
    flowed = " ".join((REPO_ROOT / "docs/boundaries/canonical_zones.md")
                      .read_text(encoding="utf-8").split())

    assert "canon/" in flowed, "Artifact 017: canonical root not declared"


# ---------------------------------------------------------------------------
# Val — hooks.  Blueprint §10, the canonical write-deny foundation.
# ---------------------------------------------------------------------------


def test_p0_canon_deny_hook_is_registered():
    """settings → PreToolUse registration → the deny hook file.

    Existence of the hook proves nothing on its own: an unregistered hook
    denies nothing. The chain is what P0 has to establish.
    """
    settings = json.loads((CLAUDE_DIR / "settings.json").read_text(encoding="utf-8"))
    all_events = settings.get("hooks", {})

    # Where the hook is registered, across every event, so a registration in
    # the wrong place is reported as wrong rather than as absent. Searching
    # only PreToolUse for the filename proved that *a* string mentioning the
    # hook exists somewhere — not that it is attached where it fires before
    # the tool runs, and not under what applicability.
    placements = [
        (event, group.get("matcher"))
        for event, groups in all_events.items()
        for group in groups
        for entry in group.get("hooks", [])
        if "canon_deny.py" in entry.get("command", "")
    ]

    assert placements, (
        "Artifact 024: canon deny hook not registered in .claude/settings.json — "
        f"no hook command references canon_deny.py under any event (events: {sorted(all_events)})"
    )

    pre_tool_use = [matcher for event, matcher in placements if event == "PreToolUse"]
    assert pre_tool_use, (
        "Artifact 024: canon deny hook registered under an unexpected event — found at "
        f"{[event for event, _ in placements]}, must be PreToolUse. A hook that runs after "
        "the tool cannot prevent the write."
    )

    # ``matcher: ""`` — every tool event reaches the hook. Artifact 024 fixed
    # this value deliberately and its own suite asserts it exactly: a matcher
    # that filtered any tool out was experimentally shown to let a Bash
    # redirect through. Read from that artifact, not invented here.
    assert "" in pre_tool_use, (
        f"Artifact 024: canon deny hook registered under an unexpected matcher {pre_tool_use!r}, "
        'expected "" (all tools). A narrower matcher lets a write path escape the hook.'
    )

    # The registration must point at the hook that exists.
    registered_commands = [
        entry.get("command", "")
        for group in all_events.get("PreToolUse", [])
        for entry in group.get("hooks", [])
        if "canon_deny.py" in entry.get("command", "")
    ]
    assert any(".claude/hooks/canon_deny.py" in command for command in registered_commands), (
        "Artifact 024: registration does not reference .claude/hooks/canon_deny.py — "
        f"commands are {registered_commands}"
    )

    hook = CLAUDE_DIR / "hooks/canon_deny.py"
    assert hook.is_file(), f"Artifact 022: registered hook file missing: {hook.relative_to(REPO_ROOT)}"


def test_p0_zone_configuration_is_machine_readable_and_declares_canon():
    """Artifact 023 — the deny hook's zone configuration.

    Read as data rather than as text: a zones file that has drifted into
    something unparseable would leave the hook without its declaration.
    """
    zones = json.loads((CLAUDE_DIR / "hooks/zones.json").read_text(encoding="utf-8"))

    assert zones.get("canonical_root") == "canon/**", \
        f"Artifact 023: canonical_root is {zones.get('canonical_root')!r}, expected 'canon/**'"
    assert isinstance(zones.get("zones"), list) and zones["zones"], \
        "Artifact 023: no zones declared"


def test_p0_deny_hook_refuses_a_canonical_write_without_touching_canon():
    """Runtime proof: the registered hook actually denies, and reads still pass.

    Registration and file existence are separate claims from *the deny
    works*, and this is the one that can be established safely. The hook is a
    classifier over a payload — it never executes the command it is shown —
    and the probe names a file that does not exist, so even a hook that failed
    to deny would write nothing. Nothing is created, and ``canon/`` is not
    touched either way.

    Reads are probed alongside the writes because a hook that denied
    everything would also pass a deny-only check while breaking the boundary
    in the other direction: Artifact 017 permits reading canon.
    """
    hook = CLAUDE_DIR / "hooks/canon_deny.py"
    environment = {**os.environ, "CLAUDE_PROJECT_DIR": str(REPO_ROOT)}

    def decide(payload: dict) -> tuple[int, str]:
        finished = subprocess.run(
            [sys.executable, str(hook)],
            input=json.dumps(payload), text=True, capture_output=True,
            env=environment, cwd=str(REPO_ROOT),
            # A non-zero exit is the expected outcome here — exit 2 *is* the
            # deny. Raising on it would turn the proof into an error.
            check=False,
        )
        return finished.returncode, finished.stderr.strip()

    inside = "canon/world/p0-conformance-probe-does-not-exist.md"
    outside = "derived/p0-conformance-probe-does-not-exist.md"

    # The matrix, both directions. Denies alone prove nothing about the
    # boundary: a hook that denied *everything* would satisfy every deny case
    # and would have broken the environment rather than protected canon. The
    # allow rows are what make this a boundary proof instead of a deny proof.
    matrix = (
        ("Write", "inside canon/", 2,
         {"tool_name": "Write", "tool_input": {"file_path": inside, "content": "x"}}),
        ("Bash redirect", "inside canon/", 2,
         {"tool_name": "Bash", "tool_input": {"command": f"echo x > {inside}"}}),
        ("Read", "inside canon/", 0,
         {"tool_name": "Read", "tool_input": {"file_path": inside}}),
        ("Write", "outside canon/", 0,
         {"tool_name": "Write", "tool_input": {"file_path": outside, "content": "x"}}),
        ("Bash redirect", "outside canon/", 0,
         {"tool_name": "Bash", "tool_input": {"command": f"echo x > {outside}"}}),
    )

    for operation, location, expected, payload in matrix:
        code, reason = decide(payload)
        verdict = {0: "allow", 2: "deny"}
        assert code == expected, (
            f"Artifact 022: {operation} {location} exited {code}, expected {expected} "
            f"({verdict.get(expected, '?')}). stderr: {reason[:200]!r}"
        )
        if expected == 2:
            assert "DENIED" in reason, (
                f"Artifact 022: {operation} {location} denied without a stated reason"
            )

    # The probe must leave the canonical tree exactly as it found it.
    residue = [
        path.relative_to(REPO_ROOT).as_posix()
        for path in (REPO_ROOT / "canon").rglob("*")
        if path.is_file() and path.name != "PURPOSE.md"
    ]
    assert not residue, f"the deny probe wrote into canon/: {residue}"


# ---------------------------------------------------------------------------
# Val — the 108-invariant register.
# ---------------------------------------------------------------------------


def register_ids() -> list[str]:
    """Invariant IDs, parsed from the register's own table rows.

    Anchored to ``| I-NN |`` at the start of a row, which is the entry format
    Artifact 012 uses. Counting every ``I-`` occurrence would also count the
    prose that cites invariants, and would report a number that means nothing.
    """
    return re.findall(r"^\| (I-\d{2,3}) \|", REGISTER.read_text(encoding="utf-8"), re.MULTILINE)


def test_p0_invariant_register_has_exactly_108_invariants():
    """Artifact 012 — I-01 … I-108, complete, unique, and nothing else.

    Existence is not the check. A register missing I-57, carrying I-31 twice,
    or having grown an I-109 would still exist and would no longer be the
    register the Blueprint's §36 states.
    """
    found = register_ids()
    numbers = [int(identifier.split("-")[1]) for identifier in found]
    expected = set(range(1, 109))

    duplicates = sorted({identifier for identifier in found if found.count(identifier) > 1})
    assert not duplicates, f"duplicate invariant: {', '.join(duplicates)}"

    absent = sorted(expected - set(numbers))
    assert not absent, "expected invariant missing: " + ", ".join(f"I-{n:02d}" for n in absent)

    unexpected = sorted(set(numbers) - expected)
    assert not unexpected, "unexpected invariant: " + ", ".join(f"I-{n}" for n in unexpected)

    assert len(found) == 108, f"expected 108 invariant entries, found {len(found)}"


def test_p0_invariant_ids_use_the_canonical_form():
    """``I-01`` … ``I-108``, so a downstream test can cite an entry by ID.

    The register says so itself: *"Entry IDs are canonical and stable in
    exactly one form"*. Mixed padding would break every citation.
    """
    malformed = [
        identifier for identifier in register_ids()
        if identifier != f"I-{int(identifier.split('-')[1]):02d}"
    ]

    assert not malformed, f"invariant IDs not in canonical form: {malformed}"


# ---------------------------------------------------------------------------
# Val — the eleven adapter boundaries (Artifact 029).
# ---------------------------------------------------------------------------


def test_p0_all_eleven_adapter_shells_exist():
    present = sorted(path.stem for path in ADAPTERS.glob("*.py"))
    expected = sorted(ADAPTER_SHELLS)

    absent = [stem for stem in expected if stem not in present]
    assert not absent, f"adapter shell missing: {absent}"
    assert present == expected, f"unexpected adapter module: {sorted(set(present) - set(expected))}"


@pytest.mark.parametrize("stem", sorted(ADAPTER_SHELLS))
def test_p0_adapter_shells_are_empty_boundaries(stem):
    """P0 emptiness: a boundary that has not acquired an implementation.

    Parsed rather than grepped, so the check does not overfit to one way of
    writing a shell: whatever the prose, the module body must be a docstring
    and nothing else. Comments and boundary wording are free; a statement,
    an import, a class or a function is evidence of implementation.

    Artifact 445 implements these. When it does, this assertion is expected to
    be revisited — it states a P0 condition, not a permanent ban.
    """
    path = ADAPTERS / f"{stem}.py"
    body = ast.parse(path.read_text(encoding="utf-8")).body

    executable = [node for node in body if not (
        isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )]
    assert not executable, (
        f"adapter shell contains executable implementation: {stem}.py — "
        f"{[type(node).__name__ for node in executable]}"
    )

    imports = [node for node in ast.walk(ast.parse(path.read_text(encoding="utf-8")))
               if isinstance(node, (ast.Import, ast.ImportFrom))]
    assert not imports, (
        f"adapter shell imports a module before Artifact 445: {stem}.py — "
        f"{[ast.unparse(node) for node in imports]}"
    )

    definitions = [
        node.name for node in ast.walk(ast.parse(path.read_text(encoding="utf-8")))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    ]
    assert not definitions, (
        f"adapter shell defines adapter code before Artifact 445: {stem}.py — {definitions}"
    )


@pytest.mark.parametrize("stem", sorted(ADAPTER_SHELLS))
def test_p0_adapter_shells_mark_world_constructs_world_only(stem):
    """Row 029's third Val clause, checked as meaning rather than wording.

    The five constructs must be named *and* claimed for the World Record
    Model. Listing them and calling them "not universal" leaves out whose they
    are, which is the half that stops a later reader treating WSV or the
    History Record as something every Record Model has (I-102).
    """
    body = (ADAPTERS / f"{stem}.py").read_text(encoding="utf-8")
    flowed = " ".join(body.split())

    for construct in ("World Record", "World Relationship Record",
                      "World History Record", "WSV", "WSV-H"):
        assert construct in body, f"World-only guard missing from: {stem}.py — no {construct!r}"

    assert re.search(r"are World Record Model constructs", flowed), \
        f"World-only guard missing from: {stem}.py — constructs listed but not claimed for World"
    assert re.search(r"not be assumed as universal", flowed), \
        f"World-only guard missing from: {stem}.py — no universality prohibition"


# ---------------------------------------------------------------------------
# Val — the P0 refusing command surfaces (Artifact 028).
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("command", sorted(REFUSING_COMMANDS))
def test_p0_refusing_commands_are_present_and_refuse(command):
    """Row 028's contract, not the future capability.

    Three things: the surface exists, it refuses, and it names the phase that
    ends the refusal. Whether P5 or P17 eventually works is not a P0 question.
    """
    path = CLAUDE_DIR / f"commands/{command}.md"
    assert path.is_file(), f"expected file missing: .claude/commands/{command}.md"

    flowed = " ".join(path.read_text(encoding="utf-8").split())
    phase = REFUSING_COMMANDS[command]

    assert re.search(r"\b(command|this|it)\b[^.]{0,40}\brefuses\b", flowed, re.IGNORECASE), \
        f"/{command}: no refusal stated"
    assert re.search(r"not (yet )?available|capability is not", flowed, re.IGNORECASE), \
        f"/{command}: refusal states no reason"
    assert re.search(rf"\b{phase}\b", flowed), \
        f"/{command}: unlocking phase {phase} not identified"


# ---------------------------------------------------------------------------
# Val — zero current COM terms.  The retired-vocabulary firewall.
# ---------------------------------------------------------------------------

# Retired Canon Object Model vocabulary. The Roadmap retires the model and
# states that CO / COR / COH appear only in historical notes; semantic
# ownership runs on W · E · P · R · V · I.
RETIRED_TERMS = (
    r"Canon Object Model",
    r"\bCOM\b",
    r"\bCOR\b",
    r"\bCOH\b",
    r"universal Canon Object",
    r"nine domains",
    r"nine-domain",
)

# Two of these are retired outright and one is retired *in a specific use*,
# and the Roadmap says which is which in one sentence (line 29):
#
#   "Semantic ownership runs on W · E · P · R · V · I only. The nine-domain
#    taxonomy is retired **as an ownership axis**. Canon Object Model is
#    retired. CO/COR/COH appear only in historical notes."
#
# So "Canon Object Model", COM, COR, COH and "universal Canon Object" are
# forbidden as current architecture in any use. The nine-domain vocabulary is
# forbidden only where it is doing the retired job — owning records, or
# standing as the current axis, taxonomy or architecture. The Blueprint's own
# §9.5 layer diagram enumerates "the nine domains, six partitions, two
# primitives, ten laws" and assigns ownership to the partitions in the same
# breath; that is a structural enumeration, not an ownership claim, and the
# scoped rule lets it stand on its own merits rather than on a whitelist.
_OWNERSHIP_SCOPED_TERMS = (r"nine domains", r"nine-domain")

# The retired job, in the Roadmap's own words: an *ownership axis*. Note what
# is deliberately not here — "partition". The §9.5 diagram reads "the nine
# domains, six partitions, two primitives, ten laws", and the partitions
# beside it are what make the line an enumeration; treating that word as
# evidence of an ownership claim would fail the very line the scoping exists
# to judge fairly.
_OWNERSHIP_USE = re.compile(
    r"\b(?:own|owns|owned|owning|ownership|axis|taxonomy|architecture|"
    r"semantic\s+ownership|records?)\b",
    re.IGNORECASE,
)

# The current-architecture surface: everything in this repository that states
# what coolboy12 *is* today.
#
#   CLAUDE.md    Artifact 004, governing session conduct.
#   docs/        every subdirectory except sources/ — the boundaries and
#                conventions are AUTHORITATIVE contracts, and the rest
#                (constitution/, models/, registry/, governance/, …) are
#                empty scaffolds now that fill with current architecture from
#                P2 on. Scanning them while empty costs nothing and means the
#                surface does not silently miss them later; naming only the
#                two populated ones would have.
#   src/         the implementation.
#   .claude/     the execution environment.
#
# Excluded, each for a stated reason rather than by convenience:
#
#   docs/sources/  verbatim reference copies of the three governing
#                  documents — its own PURPOSE.md says so, and says the
#                  directory "does not interpret them, summarize them, or
#                  amend them". The Blueprint's §36 amendment history and the
#                  Roadmap's "not inherited from the old roadmap" line
#                  preserve retired vocabulary deliberately; flagging the
#                  constitution for recording its own history would be wrong.
#   reports/       generated output, no architectural authority.
#   tests/         DEV-ENV proof, and this file itself necessarily names every
#                  retired term it forbids.
CURRENT_ARCHITECTURE = ("CLAUDE.md", "docs", "src", ".claude")
EXCLUDED_FROM_SCAN = ("docs/sources",)

# Prohibition constructions that BIND TO ONE OCCURRENCE.
#
# Two false-pass paths lived here and both are closed below. The first was a
# block-wide test whose word list included a bare `no`: any paragraph
# containing that word exempted every retired term in it. The second was
# subtler and survived the first repair — testing the whole *line* meant a
# single prohibition anywhere on it exempted every occurrence, so
#
#     The current system uses COM; COM must not be used.
#     The current architecture uses COM, although COM is retired.
#
# both passed. The retirement clause is real; it simply does not license the
# other occurrence, and a line that makes a current-use claim must fail on
# that claim however correct its other half is.
#
# So the question asked is always: *is THIS occurrence the thing being
# forbidden?* — and the binder must sit immediately against the term, with no
# sentence boundary between them.

# Directly after the term: "COM is retired", "COR must not be used".
_PROHIBITED_AFTER = re.compile(
    r"^\s*"
    # The terms are often retired together — "CO/COR/COH are historical
    # terms" — so a slash- or comma-joined continuation may sit between this
    # occurrence and the verb that retires the whole list.
    r"(?:[/,]\s*[\w-]+\s*)*"
    r"(?:terminology\s+|vocabulary\s+|terms?\s+)?"
    r"(?:(?:is|are|was|were)\s+(?:now\s+)?"
    r"(?:retired|forbidden|prohibited|historical|deprecated|no longer\b)"
    r"|must not\b|may not\b|cannot\b|shall not\b)",
    re.IGNORECASE,
)

# Directly before the term, with no sentence break in between:
#   "do not use COM", "must not use as current architecture: … COM",
#   "retired Canon Object Model terminology", "No COM Terminology".
_PROHIBITED_BEFORE = (
    re.compile(
        r"\b(?:do not|does not|must not|may not|shall not|cannot|never|no longer)\b"
        r"[^.;]{0,60}?\b(?:use|used|using|introduce|adopt|revive|rely on|reference|treat)\b"
        r"[^.;]{0,40}$",
        re.IGNORECASE,
    ),
    re.compile(r"\b(?:retired|deprecated|legacy|former)\s+(?:\w+\s+){0,2}$", re.IGNORECASE),
)

# "### No COM Terminology as Current Architecture" — `no` only in this shape.
_PROHIBITED_HEADING_BEFORE = re.compile(r"\bno\s+(?:\w+\s+){0,2}$", re.IGNORECASE)
_TERMINOLOGY_AFTER = re.compile(r"^\s*(?:terminology|vocabulary)\b", re.IGNORECASE)

# "| Introduces COM terminology | **No** |" — a compliance row answering No.
_TABLE_ANSWER_AFTER = re.compile(r"^[^|]*\|\s*\*{0,2}no\b", re.IGNORECASE)


def architecture_files() -> list[Path]:
    files: list[Path] = []
    for entry in CURRENT_ARCHITECTURE:
        path = REPO_ROOT / entry
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(
                child for child in sorted(path.rglob("*"))
                if child.is_file()
                and child.suffix in (".md", ".py", ".json")
                and "__pycache__" not in child.parts
                and not any(
                    child.is_relative_to(REPO_ROOT / excluded)
                    for excluded in EXCLUDED_FROM_SCAN
                )
            )
    return files


def test_p0_com_scan_covers_the_current_architecture_surface():
    """The scan reaches what it claims to, and skips only what it declares.

    A scope that quietly stopped covering a directory would make the firewall
    pass by not looking, which is the failure mode a scan cannot report about
    itself.
    """
    scanned = {path.relative_to(REPO_ROOT).as_posix() for path in architecture_files()}

    for required in ("CLAUDE.md", "docs/boundaries/environment.md",
                     "docs/conventions/artifact_conventions.md",
                     ".claude/hooks/canon_deny.py",
                     "src/coolboy12/adapters/a01_deconstruction.py"):
        assert required in scanned, f"current architecture file not scanned: {required}"

    assert not [path for path in scanned if path.startswith("docs/sources/")], \
        "docs/sources/ is verbatim constitutional source and must not be scanned"


def normalize(line: str) -> str:
    """Whitespace-collapsed line, for exact comparison against the Blueprint."""
    return " ".join(line.split())


# There is deliberately no Blueprint-comparison helper here any more. The
# quotation allowance — first ``line in blueprint_flat``, then an exact
# whole-line set — is gone in both forms. Neither proved that *this* use is
# historical: text can be reproduced from the constitution and still be
# asserted as current. Classification is from local evidence only, and the
# nine-domain vocabulary is judged against the retired use the Roadmap names
# rather than against a list of quotable lines.


def is_prohibited_occurrence(lines: list[str], index: int, start: int, end: int) -> bool:
    """Is *this* occurrence the thing being forbidden, rather than used?

    Bound to the span, not to the line. The binder must sit immediately
    against the term — no sentence boundary between them — which is what
    stops a correct retirement clause from licensing a current-use claim
    elsewhere in the same sentence.

    One line of lookback survives, and it is gated twice: the previous line
    must end in a colon *and* carry a list-introducing prohibition. That is
    the one real continuation shape here — CLAUDE.md writes

        MUST NOT use as **current** architecture:
        Canon Object Model · COM · universal Canon Object · …

    so the terms sit on a line with no verb of their own. Ungated, the
    lookback would be the block-wide loophole in a smaller disguise.
    """
    line = lines[index]
    before, after = line[:start], line[end:]

    if _PROHIBITED_AFTER.match(after):
        return True
    if any(pattern.search(before) for pattern in _PROHIBITED_BEFORE):
        return True
    if _PROHIBITED_HEADING_BEFORE.search(before) and _TERMINOLOGY_AFTER.match(after):
        return True
    if before.lstrip().startswith("|") and _TABLE_ANSWER_AFTER.match(after):
        return True

    if index > 0:
        previous = lines[index - 1].rstrip()
        introduces_a_list = previous.endswith(":") and any(
            pattern.search(previous + " x") for pattern in _PROHIBITED_BEFORE
        )
        if introduces_a_list:
            return True

    return False


def com_findings(text: str) -> list[str]:
    """Retired-term occurrences in ``text`` that are current-architecture use.

    Classification is from local evidence only. There is no whitelist: the
    allowance used to be "this line also appears somewhere in the Blueprint",
    which proved string duplication and nothing about whether *this* use is
    historical. A sentence can reproduce constitutional wording and still
    assert it as current.

    Two rules, both from the Roadmap's own scoping (line 29):

    * ``Canon Object Model``, ``COM``, ``COR``, ``COH`` and ``universal Canon
      Object`` are retired outright — allowed only where the local text says
      so, per :func:`is_prohibited_occurrence`;
    * the nine-domain vocabulary is retired **as an ownership axis**, so it is
      a finding only where it is doing that job.

    Split out so the classification runs on in-memory strings: a conformance
    gate that must damage the repository to prove itself is not read-only.
    """
    lines = text.splitlines()
    findings: list[str] = []

    for index, line in enumerate(lines):
        for term in RETIRED_TERMS:
            for match in re.finditer(term, line):
                if is_prohibited_occurrence(lines, index, match.start(), match.end()):
                    continue
                if term in _OWNERSHIP_SCOPED_TERMS:
                    # Judged in a window around the occurrence rather than over
                    # the whole line, so an ownership word in a distant clause
                    # is not read as this occurrence's meaning.
                    window = line[max(0, match.start() - 90):match.end() + 90]
                    if not _OWNERSHIP_USE.search(window):
                        continue
                findings.append(
                    f"line {index + 1} — term {match.group(0)!r} — {normalize(line)[:110]}"
                )

    return findings


def test_p0_current_architecture_contains_no_retired_com_vocabulary():
    """*Historical record allowed; current architecture forbidden.*

    A repository-wide substring search would be wrong: the Blueprint's own
    amendment history preserves this vocabulary deliberately, and CLAUDE.md
    and Artifact 003 both carry prohibitions that name what they prohibit.

    Classification is from **local evidence only**, through the single
    classifier :func:`com_findings`, which the adversarial tests below drive
    as well. Blueprint text duplication is not an exemption and no Blueprint
    content is read here: a line can reproduce constitutional wording and
    still assert it as current, so quotability never excused anything.

    Two rules, both from the Roadmap's own scoping:

    * a retired term is allowed where *that occurrence* is being prohibited or
      retired — bound to the span, so a correct retirement clause cannot
      excuse a current-use claim beside it;
    * the nine-domain vocabulary is retired *as an ownership axis*, so it is a
      finding only where it does that job. ``docs/boundaries/environment.md``
      reproduces the §9.5 layer diagram and passes on being an enumeration
      that assigns ownership to the partitions, not on being quotable.

    Anything else using retired vocabulary is a current-architecture claim.
    """
    findings = [
        f"current COM term found: path {path.relative_to(REPO_ROOT)} — {finding}"
        for path in architecture_files()
        for finding in com_findings(path.read_text(encoding="utf-8"))
    ]

    assert not findings, "\n  ".join(["retired vocabulary used as current architecture:"] + findings)


def test_com_firewall_rejects_current_use_and_allows_prohibition():
    """The firewall's own adversarial cases, run on in-memory strings.

    Exercised against the classifier rather than by planting violations in
    real files: a conformance gate that has to damage the repository to prove
    itself is not read-only, and a fixture left behind would be worse than the
    defect it tested for.

    The rejected cases are the ones that used to pass. A block-wide rule let
    an unrelated "no" excuse anything nearby; a line-wide rule let a correct
    retirement clause excuse a current-use claim in the same sentence. Both
    are here.
    """
    must_fail = (
        "The current architecture uses COM.",
        "No semantic migration is required.\nThe current architecture uses COM.",
        "The current architecture uses COM, although COM is retired.",
        "COM is retired, but the current implementation still uses COM.",
        "The current architecture uses COM even though the Blueprint says COM is retired.",
        "The current architecture has no dependency on X.\nIt uses COM as the object model.",
        "The current system uses COM; COM must not be used.",
        "The system still relies on COR.",
        "COH is used by the current architecture.",
        "The current domain model is the Canon Object Model.",
        # The §9.5 enumeration turned into an ownership claim. Nothing about
        # resembling Blueprint text protects it; the added clause is what
        # makes it a finding.
        "The nine domains, six partitions, two primitives, ten laws are the current axis.",
    )
    for case in must_fail:
        assert com_findings(case), f"current COM use was not caught: {case!r}"

    must_pass = (
        "COM is retired.",
        "COM is retired and must not be used.",
        "Do not use COM in the current architecture.",
        "COR must not be used.",
        "Do not introduce COR.",
        "Do not use retired Canon Object Model terminology as current architecture.",
        "### No COM Terminology as Current Architecture",
        "| Introduces COM terminology | **No** |",
        # The list-continuation shape CLAUDE.md actually uses.
        "MUST NOT use as **current** architecture:\nCanon Object Model · COM · universal Canon Object",
    )
    for case in must_pass:
        assert not com_findings(case), (
            f"prohibition or retirement wrongly rejected: {case!r} — {com_findings(case)}"
        )


def test_com_firewall_scopes_nine_domain_to_the_retired_ownership_use():
    """The nine-domain rule follows the Roadmap's own scoping, not a whitelist.

    The exemption here used to be *"this line also appears somewhere in the
    Blueprint"*, which proved string duplication and nothing about whether the
    use is historical — a sentence can reproduce constitutional wording and
    still assert it as current. It is gone.

    What replaces it is the Roadmap's own sentence (line 29): *"The
    nine-domain taxonomy is retired **as an ownership axis**."* Retired in a
    named use, so a finding is a use of it in that job. The §9.5 layer diagram
    enumerates the system's parts and assigns ownership to the partitions in
    the same line; it stands on that, not on being quotable.
    """
    enumeration = "↓  the nine domains, six partitions, two primitives, ten laws"
    assert not com_findings(enumeration), "a structural enumeration was read as an ownership claim"

    for ownership_claim in (
        "The nine-domain architecture owns the records.",
        "The nine domains are the current ownership axis.",
        "Records are owned along the nine-domain taxonomy.",
    ):
        assert com_findings(ownership_claim), (
            f"nine-domain used as an ownership axis was not caught: {ownership_claim!r}"
        )

    # And the outright-retired terms are not scoped this way: no ownership
    # word is needed for them to be a finding.
    assert com_findings("The system uses COM."), "COM is retired outright and must not be scoped"


def test_p0_record_model_axis_is_the_six_sovereign_models():
    """The axis that replaced the retired one, asserted positively.

    Rejecting the old vocabulary is only half the firewall — a repository
    could drop every retired term and still not state the current model. RMS
    §2 fixes six sovereign Record Models, and CLAUDE.md carries them as
    standing session law.
    """
    flowed = " ".join((REPO_ROOT / "CLAUDE.md").read_text(encoding="utf-8").split())

    for model in ("World", "Epistemic", "Production", "Registry", "Visual", "Issue"):
        assert model in flowed, f"Record Model {model!r} not named in CLAUDE.md"
    assert "six sovereign Record Models" in flowed, \
        "CLAUDE.md does not state the six sovereign Record Models"


# ---------------------------------------------------------------------------
# BR-01 … BR-07 — the requirements row 030 gates.
#
# The authoritative requirement register is unavailable (standing GAP-C), so
# no requirement text is invented here. What each test checks is the P0
# artifacts the Roadmap's own `Req:` fields assign to that requirement.
# ---------------------------------------------------------------------------


def test_br01_artifact_and_session_conventions_are_declared():
    """BR-01 — Roadmap: artifacts 003, 004, 018, 026, 028."""
    absent = missing({key: DOC_ARTIFACTS[key] for key in ("003", "004", "018")})
    absent += missing({"026": COMMAND_ARTIFACTS["026"]})
    absent += [
        f"Artifact 028 (BR-01): expected file missing: .claude/commands/{command}.md"
        for command in sorted(REFUSING_COMMANDS)
        if not (CLAUDE_DIR / f"commands/{command}.md").is_file()
    ]

    assert not absent, "BR-01 unsatisfied:\n  " + "\n  ".join(absent)


def test_br02_readme_declares_the_project():
    """BR-02 — Roadmap: artifact 002."""
    absent = missing({"002": DOC_ARTIFACTS["002"]})
    assert not absent, "BR-02 unsatisfied:\n  " + "\n  ".join(absent)

    assert (REPO_ROOT / "README.md").read_text(encoding="utf-8").strip(), \
        "Artifact 002 (BR-02): README.md is empty"


def test_br03_has_no_p0_artifact_to_gate():
    """BR-03 — nothing to check, and that is reported rather than passed.

    ``BR-03`` appears nowhere in the Roadmap: no artifact in any phase carries
    it, and the authoritative requirement register is unavailable (GAP-C), so
    its text cannot be read either. Row 030 gates the range ``BR-01…BR-07``,
    which includes it.

    Marked not-yet-testable through Artifact 011's harness rather than
    asserted, because a green check here would claim proof of something this
    repository cannot currently express.
    """
    harness.not_yet_testable(
        "BR-03",
        "no Roadmap artifact carries BR-03 and the requirement register is "
        "unavailable (GAP-C), so there is no P0 obligation to verify",
    )


def test_br04_canonical_and_source_of_truth_boundaries_exist():
    """BR-04 — Roadmap: artifacts 016, 017, 023."""
    absent = missing({key: DOC_ARTIFACTS[key] for key in ("016", "017")})
    absent += missing({"023": CONFIG_ARTIFACTS["023"]})

    assert not absent, "BR-04 unsatisfied:\n  " + "\n  ".join(absent)


def test_br05_has_no_p0_artifact_to_gate():
    """BR-05 — carried by artifact 062, which is P3.

    The only Roadmap row carrying ``BR-05`` is 062 (Registry kernel, P3), so
    there is no P0 artifact for the exit-P0 gate to check. Reported rather
    than passed, for the same reason as BR-03.
    """
    harness.not_yet_testable(
        "BR-05",
        "the only artifact carrying BR-05 is 062 (P3); no P0 artifact is assigned to it",
    )


def test_br06_execution_environment_and_tooling_are_configured():
    """BR-06 — Roadmap: artifacts 005–010, 014, 015, 021, 024."""
    absent = missing({key: CONFIG_ARTIFACTS[key] for key in ("005", "006", "024")})
    absent += missing({key: DOC_ARTIFACTS[key] for key in ("014", "015")})
    absent += missing({"021": CODE_ARTIFACTS["021"]})

    # Artifacts 007–010 are configuration *inside* pyproject.toml and the test
    # tree, rather than files of their own, so they are checked as the
    # declarations they are.
    pyproject = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    if "[tool.pytest.ini_options]" not in pyproject:
        absent.append("Artifact 007 (BR-06): pytest configuration missing from pyproject.toml")
    if "[tool.ruff]" not in pyproject:
        absent.append("Artifact 008 (BR-06): ruff configuration missing from pyproject.toml")
    if not (REPO_ROOT / "tests").is_dir():
        absent.append("Artifact 010 (BR-06): tests/ scaffolding missing")

    assert not absent, "BR-06 unsatisfied:\n  " + "\n  ".join(absent)


def test_br07_canonical_write_deny_foundation_is_present_and_wired():
    """BR-07 — Roadmap: artifacts 004, 022.

    The hook file, its registration, and its zone configuration together.
    Any one of the three alone leaves canon undefended.
    """
    absent = missing({"022": CODE_ARTIFACTS["022"], "004": DOC_ARTIFACTS["004"]})
    assert not absent, "BR-07 unsatisfied:\n  " + "\n  ".join(absent)

    settings = json.loads((CLAUDE_DIR / "settings.json").read_text(encoding="utf-8"))
    commands = [
        entry.get("command", "")
        for group in settings.get("hooks", {}).get("PreToolUse", [])
        for entry in group.get("hooks", [])
    ]

    assert any("canon_deny.py" in command for command in commands), \
        "BR-07 unsatisfied: canon deny hook not registered in .claude/settings.json"
    assert (CLAUDE_DIR / "hooks/zones.json").is_file(), \
        "BR-07 unsatisfied: expected file missing: .claude/hooks/zones.json"


# ---------------------------------------------------------------------------
# The gate itself.
# ---------------------------------------------------------------------------


def unresolved_gated_requirements() -> dict[str, str]:
    """Gated requirements with no P0 artifact to prove them, read from source.

    Derived from the Roadmap rather than from a constant in this file, and
    derived independently of whether the ``test_brNN`` tests ran — so the gate
    below is order-independent and is not proving its own assumption.

    A requirement is unresolved when no P0 artifact (001–030) carries it in a
    ``Req:`` field. Nothing here interprets what any requirement *means*; the
    authoritative register is unavailable (GAP-C) and inventing text for it
    would be worse than reporting the gap.
    """
    roadmap = ROADMAP.read_text(encoding="utf-8")
    rows = re.findall(r"^\*\*(\d{3})\*\*.*?Req: ([^·]+)·", roadmap, re.MULTILINE)

    carried_in_p0: dict[str, set[str]] = {}
    carried_anywhere: dict[str, set[str]] = {}
    for artifact, requirements in rows:
        for requirement in re.findall(r"BR-\d+", requirements):
            carried_anywhere.setdefault(requirement, set()).add(artifact)
            if artifact <= "030":
                carried_in_p0.setdefault(requirement, set()).add(artifact)

    unresolved: dict[str, str] = {}
    for number in range(1, 8):
        requirement = f"BR-{number:02d}"
        if carried_in_p0.get(requirement):
            continue
        elsewhere = sorted(carried_anywhere.get(requirement, ()))
        unresolved[requirement] = (
            f"carried only by artifact(s) {', '.join(elsewhere)}, none in P0"
            if elsewhere else
            "no Roadmap artifact carries it, and the requirement register is unavailable (GAP-C)"
        )
    return unresolved


def test_exit_p0_gate_is_not_green_while_a_gated_requirement_is_unresolved():
    """The gate itself. ``G: exit-P0`` — and a skip is not a proof.

    ``test_br03`` and ``test_br05`` report their state truthfully through
    Artifact 011's harness, which makes them pytest *skips*. Skips do not
    change pytest's exit status, so before this check the command

        pytest tests/conformance/p0.py

    exited 0 while two of the seven gated requirements had no proof at all.
    The suite said "not-yet-testable is not a pass" and the gate then behaved
    as though it were.

    So the truthful reporting stays exactly as it is — an unresolved
    requirement is still surfaced as unresolved, never as a failure of the
    repository — and this test carries the consequence: while anything in
    BR-01…BR-07 is unresolved, exit-P0 is **not green**.

    This fails today. That is the correct state: the repository is not at
    fault, the Roadmap has no P0 artifact for these two, and the gap belongs
    to the source. Resolving it is an authorial act, not something this suite
    may assume away.
    """
    unresolved = unresolved_gated_requirements()

    assert not unresolved, "\n  ".join(
        ["exit-P0 cannot be GREEN — gated requirements are unresolved:"]
        + [
            f"{requirement} unresolved: {reason}; no P0 proof exists"
            for requirement, reason in sorted(unresolved.items())
        ]
        + ["(BR-01…BR-07 is the range row 030 gates; see test_br03 / test_br05)"]
    )


def test_p0_canon_holds_no_canonical_data_yet():
    """P0 is pre-semantic, and the gate should say so out loud.

    ``canon/`` carries Artifact 001's ``PURPOSE.md`` files and nothing else.
    A canonical record appearing before the Mutation Coordinator (Artifact
    152) would mean something wrote canon outside the governed path — the
    exact condition Artifact 022 exists to prevent, and a far more serious
    finding than a missing file.
    """
    present = {
        path.relative_to(REPO_ROOT).as_posix()
        for path in (REPO_ROOT / "canon").rglob("*")
        if path.is_file()
    }

    unexpected = sorted(present - P0_CANON_FILES)
    assert not unexpected, (
        "canon/ holds data before the Mutation Coordinator (Artifact 152) exists: "
        f"{unexpected}"
    )

    absent = sorted(P0_CANON_FILES - present)
    assert not absent, f"Artifact 001: canonical zone scaffold missing: {absent}"
