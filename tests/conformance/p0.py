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

**Not-yet-testable is not a pass.** Two of the seven gated requirements have
no P0 artifact to test — see ``test_br03`` and ``test_br05`` — and they are
reported through Artifact 011's harness as skips carrying a reason, never as
green checks. Artifact 011 exists for exactly this: *"an unavailable check is
never represented as a successful proof."*

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
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT = REPO_ROOT / "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md"
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
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                pytest.fail(f"Artifact {artifact} ({requirement}): {relative} is not valid JSON — {error}")
        else:
            assert path.read_text(encoding="utf-8").strip(), \
                f"Artifact {artifact} ({requirement}): {relative} is empty"


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
    settings_path = CLAUDE_DIR / "settings.json"
    settings = json.loads(settings_path.read_text(encoding="utf-8"))

    groups = settings.get("hooks", {}).get("PreToolUse")
    assert groups, "Artifact 024: canon deny hook not registered in .claude/settings.json — no PreToolUse group"

    commands = [
        entry.get("command", "")
        for group in groups
        for entry in group.get("hooks", [])
    ]
    registered = [command for command in commands if "canon_deny.py" in command]
    assert registered, (
        "Artifact 024: canon deny hook not registered in .claude/settings.json — "
        f"PreToolUse commands are {commands}"
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

    absent = "canon/world/p0-conformance-probe-does-not-exist.md"

    for label, payload in (
        ("a direct Write", {"tool_name": "Write",
                            "tool_input": {"file_path": absent, "content": "x"}}),
        ("a shell redirect", {"tool_name": "Bash",
                              "tool_input": {"command": f"echo x > {absent}"}}),
    ):
        code, reason = decide(payload)
        assert code == 2, (
            f"Artifact 022: {label} into canon/ exited {code}, expected 2 (deny). "
            f"stderr: {reason[:200]!r}"
        )
        assert "DENIED" in reason, f"Artifact 022: {label} denied without a stated reason"

    code, _ = decide({"tool_name": "Read", "tool_input": {"file_path": absent}})
    assert code == 0, (
        f"Artifact 022: reading canon/ exited {code}, expected 0 — Artifact 017 permits reads"
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

# Current-architecture surface. Deliberately excludes docs/sources/** — those
# are the constitution itself, and the Blueprint's own historical and
# amendment material is exactly what must not be flagged — and reports/**,
# which is generated.
CURRENT_ARCHITECTURE = ("CLAUDE.md", "docs/boundaries", "docs/conventions", "src", ".claude")

# A block is a prohibition when it tells you not to use the term. A
# prohibition necessarily contains the words it prohibits, and every current
# occurrence in this repository is one. `\bno\b` is broad on purpose: a false
# *failure* on the repository's own prohibition sections would be worse than
# the narrow risk that a violation happens to sit in a block containing "no",
# and the term list is small enough to keep that risk small.
PROHIBITION = re.compile(
    r"\b(?:must not|do not|does not|never|retired|retire|no longer|forbidden|prohibited|no)\b",
    re.IGNORECASE,
)


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
            )
    return files


def blocks(lines: list[str]) -> list[tuple[int, list[str]]]:
    """Blank-line-separated blocks, with the 1-based line number of each.

    Blocks rather than lines because a prohibition's verb often sits above the
    list it forbids — CLAUDE.md's retired-terminology section is written that
    way — and a line-by-line reading would call the list a violation.
    """
    found: list[tuple[int, list[str]]] = []
    start = 0
    for index, line in enumerate(lines):
        if not line.strip():
            if index > start:
                found.append((start, lines[start:index]))
            start = index + 1
    if start < len(lines):
        found.append((start, lines[start:]))
    return found


def test_p0_current_architecture_contains_no_retired_com_vocabulary():
    """*Historical record allowed; current architecture forbidden.*

    A repository-wide substring search would be wrong: the Blueprint's own
    amendment history preserves this vocabulary deliberately, and CLAUDE.md
    and Artifact 003 both carry prohibitions that name what they prohibit.
    Two narrow, mechanical allowances instead of a language classifier:

    * the block is a prohibition; or
    * the line reproduces Blueprint text, so the repository is quoting its own
      constitution — ``docs/boundaries/environment.md`` reproduces the §9.5
      layer diagram, which says *"the nine domains"* in the Blueprint's own
      words.

    Anything else using retired vocabulary is a current-architecture claim.
    """
    blueprint_flat = " ".join(BLUEPRINT.read_text(encoding="utf-8").split())
    findings: list[str] = []

    for path in architecture_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        for offset, block in blocks(lines):
            block_text = "\n".join(block)
            is_prohibition = bool(PROHIBITION.search(block_text))
            for inner, line in enumerate(block):
                hits = [term for term in RETIRED_TERMS if re.search(term, line)]
                if not hits:
                    continue
                if is_prohibition:
                    continue
                flat = " ".join(line.split())
                if flat and flat in blueprint_flat:
                    continue
                findings.append(
                    f"current COM term found in current architecture file: "
                    f"{path.relative_to(REPO_ROOT)}:{offset + inner + 1} — {hits} — {flat[:110]}"
                )

    assert not findings, "\n  ".join(["retired vocabulary used as current architecture:"] + findings)


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


def test_p0_canon_holds_no_canonical_data_yet():
    """P0 is pre-semantic, and the gate should say so out loud.

    ``canon/`` carries Artifact 001's ``PURPOSE.md`` files and nothing else.
    A canonical record appearing before the Mutation Coordinator (Artifact
    152) would mean something wrote canon outside the governed path — the
    exact condition Artifact 022 exists to prevent, and a far more serious
    finding than a missing file.
    """
    canonical_data = [
        path.relative_to(REPO_ROOT).as_posix()
        for path in (REPO_ROOT / "canon").rglob("*")
        if path.is_file() and path.name != "PURPOSE.md"
    ]

    assert not canonical_data, (
        "canon/ holds data before the Mutation Coordinator exists: " f"{canonical_data}"
    )
