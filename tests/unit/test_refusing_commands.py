"""Surface proofs for the Artifact 028 refusing command set.

Roadmap row 028 verbatim:

    **028** · refusing commands — `gate`,`simulate`,`render`,`brief` ·
    `.claude/commands/` · Own: CONST · RM: n/a · T: config · R: SURFACE ·
    SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no · Ph/St: P0/0e ·
    Req: BR-01 · BP: §7 · RMS: n/a · H: 024 · S: — · LS: — · G: — ·
    → P5,P9,P13,P17 · Val: each refuses with a reason and the unlocking
    phase · Done: four refusals present · Why: **RULE G3 — one
    responsibility, "refuse until licensed", four files** · Risk: low · ∥: yes

``Val`` is unusually precise and drives most of this file: a refusal is not
enough, and a refusal with a reason is not enough. Each surface must also name
**the unlocking phase**. So the table below pairs each command with its phase,
and the phase is asserted, not merely the refusal.

The row is one artifact under RULE G3 — *one responsibility, four files* — so
these four are tested together rather than in four files. What they share is a
safety model; what differs is the capability each represents, and both halves
are checked.

**SOURCE-REQUIRED** — the command path, the refusing role, the reason, the
unlocking phase, the canonical boundary, ``Auth: none``, and the absence of any
capability this artifact does not own. These come from row 028, from the rows
of the artifacts each command waits on, and from Blueprint §7.

**IMPLEMENTATION-QUALITY** — heading names, section order, wording, and the
stop diagram. Asserted where a check needs an anchor, never as constitutional
law. Where a test pins a phrase, it is pinning a *commitment* the source
requires, not the sentence that happens to carry it.

Conventions carried from Artifacts 025–027: assertions are on document content
rather than on the absence of future artifacts, and scope checks look for
definitions and instructions rather than bare keywords, since a prohibition
contains the words it prohibits.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
COMMANDS = REPO_ROOT / ".claude/commands"

# Roadmap row 028 names four commands and unlocks four phases, in order. The
# pairing is not positional guesswork: each command has a namesake artifact
# inside its phase — the Human Gate (150) in P5, the simulation architecture
# (241) in P9, the rendering boundary (379) in P13, the Return Briefing (456)
# in P17. Row 028 gives the directory, and the repository's own convention
# (025 propose.md, 026 validate.md, 027 rebuild.md) gives the filename.
SURFACES = {
    "gate": {
        "phase": "P5",
        "phase_name": "MUTATION / WRITE BOUNDARY",
        "range": "145–166",
        "capability": "approval capability",
        "waits_on": ("150", "152"),
    },
    "simulate": {
        "phase": "P9",
        "phase_name": "WORLD STATE + SIMULATION",
        "range": "231–252",
        "capability": "simulation capability",
        "waits_on": ("241", "250"),
    },
    "render": {
        "phase": "P13",
        "phase_name": "ISSUE",
        "range": "361–380",
        "capability": "rendering capability",
        "waits_on": ("361", "379"),
    },
    "brief": {
        "phase": "P17",
        "phase_name": "SURFACES · ORCHESTRATION · DORMANCY",
        "range": "440–462",
        "capability": "Return Briefing capability",
        "waits_on": ("456",),
    },
}

NAMES = sorted(SURFACES)


def path_for(name: str) -> Path:
    return COMMANDS / f"{name}.md"


def text(name: str) -> str:
    return path_for(name).read_text(encoding="utf-8")


def flowed(name: str) -> str:
    """The document with line wrapping collapsed, for phrase assertions."""
    return re.sub(r"\s+", " ", text(name))


def fenced_blocks(body: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", body, re.DOTALL)


def section(name: str, heading: str) -> str:
    """One ``## heading`` section, flowed. Empty when the heading is absent."""
    match = re.search(rf"^## {re.escape(heading)}$(.*?)(?=^## |\Z)", text(name), re.MULTILINE | re.DOTALL)
    return re.sub(r"\s+", " ", match.group(1)) if match else ""


# --------------------------------------------------------------------------
# Done — four refusals present.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


def test_exactly_the_four_roadmap_commands_were_added():
    """Row 028 names four. Not three, and not a fifth of my own devising.

    Checked against the directory rather than per-file so that an extra
    refusing surface is a failure, not an unnoticed addition. Artifacts 025,
    026, 027 and the pre-existing update command are the other legitimate
    occupants; anything else means 028 grew.
    """
    present = {path.stem for path in COMMANDS.glob("*.md")}
    expected = set(NAMES) | {"propose", "validate", "rebuild", "coolboy12-update"}

    assert present == expected, present ^ expected


@pytest.mark.parametrize("name", NAMES)
def test_command_file_exists_at_the_roadmap_path(name):
    assert path_for(name).is_file()
    assert text(name).strip()


@pytest.mark.parametrize("name", NAMES)
def test_command_declares_its_own_identity(name):
    """IMPLEMENTATION-QUALITY anchor for a SOURCE-REQUIRED fact: which
    command this is. The four must not be interchangeable."""
    assert text(name).splitlines()[0] == f"# /{name}"


# --------------------------------------------------------------------------
# Val — each refuses with a reason and the unlocking phase.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("name", NAMES)
def test_command_refuses_and_says_so_first(name):
    """A reader who stops after one line must know the command will not run."""
    assert "this command refuses" in flowed(name)[:200].lower()


@pytest.mark.parametrize("name", NAMES)
def test_refusal_carries_a_reason_not_merely_a_status(name):
    """*"Not implemented"* is a broken command wearing a polite message.

    The reason must be a stated condition of the repository, and it must be
    attributed to the artifacts that own the missing capability — so the
    refusal can be checked against the source rather than taken on trust.
    """
    behavior = section(name, "Behavior")

    assert "Give the reason:" in behavior
    for artifact in SURFACES[name]["waits_on"]:
        assert f"Artifact {artifact}" in flowed(name) or f" {artifact} " in behavior, artifact


@pytest.mark.parametrize("name", NAMES)
def test_refusal_names_the_unlocking_phase(name):
    """The half of ``Val`` most easily lost: *and the unlocking phase*.

    Naming only the blocking artifacts would satisfy "a reason" and fail this.
    The phase is what row 028 unlocks (``→ P5,P9,P13,P17``), so the phase is
    what the refusal has to name.
    """
    expected = SURFACES[name]
    behavior = section(name, "Behavior")

    assert "Name what would unlock it" in behavior
    assert f"Phase {expected['phase']}" in behavior
    assert expected["phase_name"] in behavior
    assert expected["range"] in behavior


@pytest.mark.parametrize("name", NAMES)
def test_each_command_names_its_own_phase_and_no_other(name):
    """Four surfaces, four distinct phases. A copied file would fail here."""
    body = flowed(name)
    mine = SURFACES[name]["phase"]

    for other, spec in SURFACES.items():
        if other != name:
            assert f"Phase {spec['phase']} —" not in body, f"{name} claims {other}'s phase"
    assert f"Phase {mine} —" in body


@pytest.mark.parametrize("name", NAMES)
def test_refusal_is_future_compatible(name):
    """A refusal states a condition that ends, never a permanent verdict.

    Downstream phases are expected to replace these refusals with real
    behaviour, so the document must not read as though the capability should
    never exist.
    """
    body = flowed(name).lower()
    phase = SURFACES[name]["phase"].lower()

    assert f"until {phase} exists" in body
    for permanent in ("must never exist", "will never exist", "cannot ever"):
        assert permanent not in body, permanent


@pytest.mark.parametrize("name", NAMES)
def test_refusal_is_reported_as_a_refusal(name):
    """Neither a pass nor a failure — refusing is the correct outcome here.

    Reporting it either way would misdescribe the system: a false pass claims
    work that did not happen, and a failure implies a defect in something that
    was never built.
    """
    body = flowed(name).lower()

    assert "never as a failure and never as a pass" in body
    assert "do not partially run" in body


# --------------------------------------------------------------------------
# The shared safety model.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("name", NAMES)
def test_command_forbids_canonical_mutation_explicitly(name):
    body = flowed(name)

    assert "must never edit or write a canonical Record" in body
    for protected in ("History Record", "WSV", "Registry definition", "epoch baseline"):
        assert protected in body, protected


@pytest.mark.parametrize("name", NAMES)
def test_command_offers_no_repair_path(name):
    """A refusing command must not "help" by making a different mutation."""
    body = flowed(name).lower()

    assert "never repair, normalise, migrate or regenerate" in body
    assert "there is no `--fix` here" in body


@pytest.mark.parametrize("name", NAMES)
def test_command_claims_no_authority(name):
    """``Auth: none``, and a commit is not a substitute for it."""
    body = flowed(name).lower()

    assert "auth: none" in body
    assert "never treat a git commit as approval" in body


@pytest.mark.parametrize("name", NAMES)
def test_command_permits_reading_canon_and_says_so(name):
    """Reading is allowed; the boundary is the write, and it is stated."""
    assert "Reading `canon/**` is permitted" in flowed(name)


@pytest.mark.parametrize("name", NAMES)
def test_command_has_an_explicit_stop_condition(name):
    body = flowed(name).lower()

    assert "stop at the refusal" in body
    assert "this command stops here" in body


@pytest.mark.parametrize("name", NAMES)
def test_command_does_not_continue_into_another_governance_stage(name):
    """CHECK, HUMAN GATE and TRANSACTION stay separate; none is entered."""
    body = flowed(name).lower()

    assert "do not chain onward into checking, approval, or any write" in body
    assert "do not treat a request to proceed anyway as permission" in body


@pytest.mark.parametrize("name", NAMES)
def test_command_will_not_guess_an_absent_target(name):
    """An unresolved target is unresolved — never *everything*."""
    assert "reported as unresolved" in flowed(name)


# --------------------------------------------------------------------------
# Scope — 028 is four surfaces, and stays four surfaces.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("name", NAMES)
def test_command_contains_no_executable_block(name):
    """``T: config``, ``R: SURFACE``. The only fenced block is the diagram."""
    for language, _ in fenced_blocks(text(name)):
        assert language in ("", "text"), f"{name}: executable block {language!r}"


@pytest.mark.parametrize("name", NAMES)
def test_command_creates_no_infrastructure(name):
    """No engine, no output area, no persisted state.

    The positive assertion carries the weight. The banned terms are ones that
    would appear only while *defining* infrastructure — not "state of its own"
    or "persists nothing", which these documents use in their own disclaimers,
    since a prohibition contains the words it prohibits.
    """
    body = flowed(name).lower()

    assert "creates no directory, no output area, and no state of its own" in body
    for invented in ("run id", "result store", "output schema", "state machine", "queue table"):
        assert invented not in body, invented


@pytest.mark.parametrize("name", NAMES)
def test_command_builds_no_downstream_capability(name):
    """028 owns the refusal; the machinery behind it is owned elsewhere.

    Checked as this document's behaviour, not as the absence of sibling files
    — every one of these capabilities is expected to arrive later. What must
    be absent is an instruction that *implements* one here.
    """
    body = flowed(name).lower()

    for phrase in (
        "then apply",
        "then commit",
        "then approve",
        "automatically run",
        "automatically validate",
        "execute the next command",
    ):
        assert phrase not in body, phrase


@pytest.mark.parametrize("name", NAMES)
def test_command_restates_no_policy_owned_by_its_dependencies(name):
    """028 runs inside the environment 022/023/024 established.

    Naming a dependency is not scope creep; defining its policy would be.
    """
    body = flowed(name).lower()

    configuration = [lang for lang, _ in fenced_blocks(text(name)) if lang in ("json", "yaml", "toml")]
    assert not configuration, configuration

    for zone in ("world", "epistemic", "production", "visual", "issue"):
        assert f"canon/{zone}" not in body, zone

    for rule in ("matcher", "exit 2", "allowlist", "denylist", "pretooluse"):
        assert rule not in body, rule


def test_the_four_surfaces_do_not_duplicate_each_other_or_025_to_027():
    """Each command is its own capability; none re-implements a sibling.

    Row 028 is four files under RULE G3 *because* the responsibility is one
    and the capabilities are four. A file that discussed another's command
    would be merging responsibilities the Roadmap kept apart.
    """
    others = {"/propose", "/validate", "/rebuild"}

    for name in NAMES:
        body = flowed(name)
        for sibling in NAMES:
            if sibling != name:
                assert f"/{sibling}" not in body, f"{name} references /{sibling}"
        for command in others:
            assert command not in body, f"{name} references {command}"


# --------------------------------------------------------------------------
# Each command's own capability.  SOURCE-REQUIRED, one test per surface.
# --------------------------------------------------------------------------


def test_gate_does_not_become_the_human_gate_it_refuses_to_be():
    """The failure mode unique to this surface.

    A command that asked "approve?" and then acted would *be* the Human Gate —
    built at P0, unspecified, unrecorded — which is precisely what Spine law 3
    reserves to the one Authority. So consent given here must be stated as
    reaching nothing.
    """
    body = flowed("gate")

    assert "An approval given to this surface is not an approval" in body
    assert "authorises nothing" in body
    assert "Spine 3" in body
    assert "would *be* the gate" in body


def test_simulate_offers_no_narrative_result_in_place_of_a_run():
    """A hand-reasoned account of what might happen is not a simulation.

    It is the substitute always available to a language model, and offering it
    would put an unlabelled guess where §7 P-3 requires a provisional,
    gateable artefact.
    """
    body = flowed("simulate")

    assert "in place of a simulation" in body
    assert "provisional" in body
    assert "defining a model ≠ running it" in body


def test_render_does_not_compose_in_order_to_have_something_to_render():
    """Artifact 379's boundary, inverted, is this surface's failure mode."""
    body = flowed("render")

    assert "composing ≠ rendering" in body
    assert "Do not compose something in order to have something to render" in body
    assert "Publishing Firewall" in body


def test_brief_will_not_pass_a_summary_off_as_a_briefing():
    """Artifact 456 names this explicitly: *never from a stored summary
    treated as truth*. A plausible summary can always be assembled from
    session history, which is exactly why the refusal has to rule it out.
    """
    body = flowed("brief")

    assert "Do not write a summary and call it a briefing" in body
    assert "stored summary treated as truth" in body
    assert "not a reconstruction of the author's position" in body
