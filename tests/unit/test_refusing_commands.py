"""Document-conformance proofs for the Artifact 028 refusing command set.

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

**What these tests check, and what they do not.** Row 028 is ``T: config``,
``R: SURFACE`` — the artifact *is* four documents, so these are document
conformance checks. Nothing here executes a command or exercises a future
capability, and a passing run says nothing about whether P5, P9, P13 or P17 is
correctly built. Where a test asserts that a document names Artifact 150, that
proves **traceability** — the refusal cites the artifact that owns the missing
capability — and never that 150 itself is right.

**SOURCE-REQUIRED** — the command path, the refusing role, the reason, the
unlocking phase, the canonical boundary, ``Auth: none``, and the absence of any
capability this artifact does not own. These come from row 028, from the rows
of the artifacts each command waits on, and from Blueprint §7.

**IMPLEMENTATION-QUALITY** — heading names, section order, and wording. These
documents may be rewritten freely, so the assertions below target the
*commitment* rather than the sentence carrying it: each is a small family of
accepted phrasings, wide enough that a rewrite in different words still passes
and narrow enough that a document which dropped the commitment fails. Two
places still pin an exact string — the ``# /name`` heading and the ``Auth:
none`` field — because both are identifiers rather than prose.

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
ROADMAP = REPO_ROOT / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"


def roadmap_phases() -> dict[str, tuple[str, str]]:
    """``{phase id: (name, artifact range)}``, read from the Roadmap itself.

    These were hand-copied into the table below, and P17's name was copied
    short — *"SURFACES · ORCHESTRATION · DORMANCY"*, dropping *"·
    EXTENSIBILITY"*. Nothing caught it: the assertion checked the metadata
    against the document, so a truncated mapping proved itself correct, and
    the surface with the longest phase name had the weakest traceability
    proof of the four.

    A copy of source data cannot verify itself, so the copy is gone. The
    Roadmap is the source of the mapping and is now read as one.
    """
    header = re.compile(r"^## PHASE (P\d+) — (.+?) \((\d+–\d+)\)", re.MULTILINE)
    found = {
        phase: (name.strip(), artifact_range)
        for phase, name, artifact_range in header.findall(ROADMAP.read_text(encoding="utf-8"))
    }
    assert len(found) == 19, f"expected 19 phases, parsed {len(found)}"
    return found


PHASES = roadmap_phases()

# Roadmap row 028 names four commands and unlocks four phases, in order. The
# pairing is not positional guesswork: each command has a namesake artifact
# inside its phase — the Human Gate (150) in P5, the simulation architecture
# (241) in P9, the rendering boundary (379) in P13, the Return Briefing (456)
# in P17. Row 028 gives the directory, and the repository's own convention
# (025 propose.md, 026 validate.md, 027 rebuild.md) gives the filename.
SURFACES = {
    "gate": {"phase": "P5", "waits_on": ("150", "152")},
    "simulate": {"phase": "P9", "waits_on": ("241", "250")},
    "render": {"phase": "P13", "waits_on": ("361", "379")},
    "brief": {"phase": "P17", "waits_on": ("456",)},
}


def phase_of(name: str) -> tuple[str, str, str]:
    """``(phase id, name, range)`` for a surface, name and range from source."""
    phase = SURFACES[name]["phase"]
    return (phase, *PHASES[phase])


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
    pattern = rf"^## {re.escape(heading)}$(.*?)(?=^## |\Z)"
    match = re.search(pattern, text(name), re.MULTILINE | re.DOTALL)
    return re.sub(r"\s+", " ", match.group(1)) if match else ""


def states(name: str, *alternatives: str, where: str | None = None) -> bool:
    """Does the document (or one section) express any of these commitments?

    Each alternative is a regex. Passing several is how a semantic commitment
    is asserted without freezing one sentence: the document may say it in any
    of the accepted ways, and must say it in one of them.
    """
    body = section(name, where) if where else flowed(name)
    return any(re.search(alternative, body, re.IGNORECASE) for alternative in alternatives)


# --------------------------------------------------------------------------
# Identity — four refusals present.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("name", NAMES)
def test_command_file_exists_at_the_roadmap_path(name):
    assert path_for(name).is_file()
    assert text(name).strip()


def test_all_four_roadmap_commands_are_represented():
    """``Done: four refusals present``. Four, and these four.

    Scoped to the files 028 owns rather than to the contents of
    ``.claude/commands/``. An earlier version asserted the whole directory
    equalled a fixed list, which would have failed the moment a later Roadmap
    artifact legitimately added a command — turning "028 is complete" into
    "the repository looks exactly as it did in P0". Whether 028 itself grew is
    a question about 028's diff, not about what the directory holds later.
    """
    assert set(NAMES) == {"brief", "gate", "render", "simulate"}
    for name in NAMES:
        assert path_for(name).is_file(), name


@pytest.mark.parametrize("name", NAMES)
def test_command_declares_its_own_identity(name):
    """An exact pin, deliberately: this is the command's identifier, not prose.

    The four must not be interchangeable.
    """
    assert text(name).splitlines()[0] == f"# /{name}"


# --------------------------------------------------------------------------
# Val — each refuses with a reason and the unlocking phase.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("name", NAMES)
def test_command_refuses_and_says_so_early(name):
    """A reader who stops after the opening must know it will not run."""
    opening = flowed(name)[:300]

    assert re.search(r"\b(command|this|it)\b[^.]{0,40}\brefuses\b", opening, re.IGNORECASE), opening[:120]


@pytest.mark.parametrize("name", NAMES)
def test_refusal_carries_a_reason(name):
    """*"Not implemented"* is a broken command wearing a polite message.

    The reason must be stated as a reason and must be attributed to the
    artifacts that own the missing capability, so a reader can check it
    against the Roadmap instead of taking it on trust. Naming those artifacts
    proves traceability only — it makes no claim about them being built right.
    """
    assert states(name, r"give the reason", r"\bbecause\b", r"the reason is", where="Behavior")

    body = flowed(name)
    for artifact in SURFACES[name]["waits_on"]:
        assert f"Artifact {artifact}" in body or re.search(rf"\b{artifact}\b", body), artifact


@pytest.mark.parametrize("name", NAMES)
def test_refusal_names_the_unlocking_phase(name):
    """The half of ``Val`` most easily lost: *and the unlocking phase*.

    Naming only the blocking artifacts would satisfy "a reason" and fail this.
    The phase is what row 028 unlocks (``→ P5,P9,P13,P17``), so the phase is
    what the refusal has to name — by ID, by name, and by artifact range, so
    the reader can find it without the Roadmap open.
    """
    phase, phase_name, artifact_range = phase_of(name)
    behavior = section(name, "Behavior")

    assert states(name, r"unlock", r"until .* exists", where="Behavior")
    assert phase in behavior
    assert artifact_range in behavior

    # Segment by segment, against the name the Roadmap states. A plain
    # substring check would accept a document that dropped a trailing segment
    # of a multi-part phase name; matching each part independently catches
    # that while still letting the document wrap or reflow the name.
    for segment in (part.strip() for part in phase_name.split("·")):
        assert segment in behavior, f"{name}: phase name missing {segment!r}"


@pytest.mark.parametrize("name", NAMES)
def test_each_command_names_its_own_phase_and_no_other(name):
    """Four surfaces, four distinct phases. A copied file would fail here."""
    body = flowed(name)

    for other in SURFACES:
        if other != name:
            _, _, other_range = phase_of(other)
            assert other_range not in body, f"{name} claims {other}'s phase range"
    assert phase_of(name)[2] in body


@pytest.mark.parametrize("name", NAMES)
def test_refusal_is_temporary_not_a_permanent_verdict(name):
    """A refusal states a condition that ends.

    Downstream phases are expected to replace these surfaces with real
    behaviour, so the document must read as *not yet*, never as *not ever*.
    """
    phase = SURFACES[name]["phase"]

    assert states(name, rf"until {phase}\b", rf"when {phase}\b", rf"{phase} exists")
    for permanent in (r"must never exist", r"will never exist", r"cannot ever", r"never be built"):
        assert not states(name, permanent), permanent


@pytest.mark.parametrize("name", NAMES)
def test_refusal_is_reported_as_a_refusal(name):
    """Neither a pass nor a failure — refusing is the correct outcome here.

    Reporting it either way would misdescribe the system: a false pass claims
    work that did not happen, and a failure implies a defect in something that
    was never built.
    """
    # The commitment is that a refusal is reported as neither outcome. Any
    # phrasing that distinguishes it from both satisfies that; the original
    # sentence was one way to say it, not the contract.
    assert states(
        name,
        r"never as a failure and never as a pass",
        r"not a failure.{0,40}not a pass",
        r"neither a (failure|pass)",
        r"refusal.{0,60}(not|never).{0,20}(failure|pass)",
    )
    assert states(name, r"do not partially run", r"never partially", r"no partial run")


# --------------------------------------------------------------------------
# The shared safety model.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("name", NAMES)
def test_command_forbids_canonical_mutation(name):
    """No canonical write, and the protected kinds are named individually.

    Naming them matters: "do not write canon" is easy to read as being about a
    directory, while History Record, WSV and the Registry are the things a
    plausible mistake would actually reach for.
    """
    assert states(name, r"never (edit or write|write or edit|write)[^.]{0,60}canonical")
    for protected in ("History Record", "WSV", "Registry definition", "epoch baseline"):
        assert protected in flowed(name), protected


@pytest.mark.parametrize("name", NAMES)
def test_command_offers_no_repair_path(name):
    """A refusing command must not "help" by making a different mutation."""
    assert states(name, r"never repair", r"no repair", r"not repair")
    assert states(name, r"normalis|normaliz") and states(name, r"regenerat")
    assert states(name, r"no `?--fix`?", r"there is no `--fix`")


@pytest.mark.parametrize("name", NAMES)
def test_command_claims_no_authority(name):
    """``Auth: none`` — pinned exactly, because it is a Roadmap field value."""
    assert "auth: none" in flowed(name).lower()
    assert states(name, r"commit[^.]{0,40}(is not|never)[^.]{0,20}approval",
                  r"never treat a git commit as approval")


@pytest.mark.parametrize("name", NAMES)
def test_command_permits_reading_canon_and_says_so(name):
    """Reading is allowed; the boundary is the write, and it is stated.

    Left implicit, a reader could reasonably conclude these surfaces may not
    touch canon at all — which would be a tighter boundary than the source
    draws and would misdescribe every one of these capabilities.
    """
    assert states(name, r"reading `canon/\*\*` is permitted", r"read[^.]{0,30}canon[^.]{0,30}permitted")


@pytest.mark.parametrize("name", NAMES)
def test_command_persists_nothing_while_it_refuses(name):
    """A refusing surface has no state, no output area, and no identifiers.

    Scoped to ``Boundary``. Checked against the whole document, the claim in
    the ``Output`` section — *"nothing persisted"* — kept this green while
    ``Boundary`` was mutated to say the command stores its decision. The
    boundary is where the commitment has to live.
    """
    assert states(name, r"creates no directory", r"no directory, no output area", where="Boundary")
    assert states(name, r"persists nothing", r"nothing persisted", r"persist nothing", where="Boundary")
    assert states(name, r"mints no identifier", r"no identifier", where="Boundary")
    assert not states(name, r"stores the (decision|result|run|briefing|output)", where="Boundary")


@pytest.mark.parametrize("name", NAMES)
def test_command_has_an_explicit_stop_condition(name):
    assert states(name, r"stop at the refusal", r"stops at the refusal")
    assert states(name, r"this command stops here", r"stops here")


@pytest.mark.parametrize("name", NAMES)
def test_command_does_not_continue_into_another_governance_stage(name):
    """CHECK, HUMAN GATE and TRANSACTION stay separate; none is entered.

    The second assertion is the one that matters under pressure: a user who
    says *do it anyway* must not move the surface.
    """
    assert states(name, r"do not chain onward", r"does not chain", r"no( hidden)? transition")
    assert states(name, r"proceed anyway as permission", r"request to proceed[^.]{0,40}not permission")


@pytest.mark.parametrize("name", NAMES)
def test_command_will_not_guess_an_absent_target(name):
    """An unresolved target is unresolved — never *everything*."""
    assert states(name, r"reported as unresolved", r"remains unresolved", r"as unresolved")


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

    ``test_command_persists_nothing_while_it_refuses`` carries the positive
    claim. Here the banned terms are ones that would appear only while
    *defining* infrastructure — deliberately not "state of its own" or
    "persists nothing", which these documents use in their own disclaimers,
    since a prohibition contains the words it prohibits.
    """
    body = flowed(name).lower()

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
# Each command's own failure mode.  SOURCE-REQUIRED, one test per surface.
# --------------------------------------------------------------------------


def test_gate_does_not_become_the_human_gate_it_refuses_to_be():
    """The failure mode unique to this surface.

    A command that asked "approve?" and then acted would *be* the Human Gate —
    built at P0, unspecified, unrecorded — which is what Blueprint §10 Spine 3
    reserves to the one Authority. So consent given here must be stated as
    reaching nothing.
    """
    assert states("gate", r"approval given to this surface is not an approval",
                  r"consent[^.]{0,60}(authorises|authorizes) nothing")
    assert states("gate", r"authorises nothing", r"authorizes nothing", r"changes nothing")
    assert states("gate", r"spine 3", r"only a human commits")
    assert states("gate", r"would \*?be\*? th(e|at) gate", r"become th(e|at) gate")


def test_simulate_offers_no_narrative_result_in_place_of_a_run():
    """A hand-reasoned account of what might happen is not a simulation.

    It is the substitute always available to a language model, and offering it
    would put an unlabelled guess where §7 P-3 requires a provisional,
    gateable artefact.
    """
    # Stated as an instruction, not only as an observation. Removing the
    # prohibition while leaving the remark that follows it — "a narrative
    # account ... is not a simulation output" — left this green against a
    # document that no longer forbade anything.
    assert states(
        "simulate",
        r"(do not|never) (produce|offer|give|report)[^.]{0,90}(in place of|instead of|as a substitute)",
    )
    assert states("simulate", r"provisional")
    assert states("simulate", r"defining a model ≠ running it", r"defining[^.]{0,30}not[^.]{0,20}running")


def test_render_does_not_compose_in_order_to_have_something_to_render():
    """Artifact 379's boundary, inverted, is this surface's failure mode."""
    assert states("render", r"composing ≠ rendering", r"composing is not rendering")
    assert states("render", r"do not compose[^.]{0,60}render", r"never compose[^.]{0,60}render")
    assert states("render", r"publishing firewall")


def test_render_may_eventually_produce_the_rendered_artifact():
    """The boundary is *canon*, not *output* — this surface exists to render.

    An earlier draft listed "published artifact" inside the canonical-write
    prohibition and stated flatly that the command writes no rendered file.
    That contradicted the surface's own purpose and Spine 5, which puts a
    published artifact outside canon by construction: producing one is not a
    canonical write, so forbidding it forever would have made `/render`
    permanently pointless rather than temporarily refusing.

    What must survive is the real boundary: nothing it produces enters canon,
    and an already-published artifact is never rewritten.
    """
    body = flowed("render")

    assert states("render", r"producing one is what this surface is for",
                  r"produces the rendered publication artifact",
                  r"may[^.]{0,40}produce[^.]{0,40}rendered")
    assert states("render", r"never become canon", r"nothing this surface produces enters canon")
    assert states("render", r"already published is never rewritten", r"stays exactly as published")

    # The canonical-write prohibition must not sweep the rendered artifact in.
    prohibition = re.search(r"must never edit or write[^.]*\.", body)
    assert prohibition, "no canonical-write prohibition found"
    assert "published artifact" not in prohibition.group(0), prohibition.group(0)

    # And guarded from the other side. Asserting only that the may-produce
    # commitment is present left the document able to contradict itself: a
    # flat "it will not write output" alongside "producing one is what this
    # surface is for" satisfied the positive check while restoring the very
    # defect this test exists to prevent.
    for absolute in (
        r"writes no rendered file, ever",
        r"will not write output",
        r"never (writes|write|produces|produce)[^.]{0,30}(rendered|output|publication)",
    ):
        assert not states("render", absolute), absolute


def test_brief_will_not_pass_a_summary_off_as_a_briefing():
    """Artifact 456 names this explicitly: *never from a stored summary
    treated as truth*. A plausible summary can always be assembled from
    session history, which is exactly why the refusal has to rule it out.
    """
    assert states("brief", r"do not write a summary and call it a briefing",
                  r"summary[^.]{0,40}is not a briefing")
    assert states("brief", r"stored summary treated as truth")
    assert states("brief", r"not a reconstruction of the author's position")


CAPABILITY_CLAIMS = {
    "gate": (r"approval capability is not (yet )?available",
             r"human gate capability is not (yet )?available"),
    "simulate": (r"simulation capability is not (yet )?available",),
    "render": (r"rendering capability is not (yet )?available",),
    "brief": (r"return briefing capability is not (yet )?available",),
}

# Claims that every blocking artifact is absent. Each was actually written
# into these documents and found wrong; the list guards the known accidents
# rather than attempting to detect state-dependence in general, which no
# string test can do.
#
# Deliberately NOT banned: statements about a missing *input* in the current
# refusal state — "no simulation model exists to name", "nothing composed
# exists to render". Those describe today's input contract truthfully. What is
# banned is making future readiness depend on total absence.
STALE_CLAIMS = (
    "canon is empty",
    "no world state for a model to read",
    "none exists",
    "none of which exist",
    "none of the three",
    "none of the sources",
    "neither is built",
    "neither exists",
    "holds neither",
    "holds none",
    "the repository holds",
    "is not built, and neither",
    "nothing to reconstruct from",
    "does not exist yet",
    "is unbuilt, and none of it",
    # Build-state wording. "Unbuilt" describes the repository at a moment;
    # what makes these commands refuse is that a capability is not available,
    # which stays true through a partial build. The "until both/all are"
    # family is the same mistake in conjunction form — it reads as *refuse
    # while every part is missing*, when the rule is *refuse while any part
    # is*.
    "is unbuilt",
    "are unbuilt",
    "until both are",
    "until both exist",
    "until all three are",
    "until they are",
    "until they exist",
)


@pytest.mark.parametrize("name", NAMES)
def test_refusal_rests_on_capability_unavailability(name):
    """The positive half: a reason that survives the repository growing.

    Deleting a stale claim without replacing it would satisfy the blocklist
    below and leave the document with no reason at all, so the capability
    claim is asserted directly — and asserted in both places a reader looks,
    the opening and the ``Behavior`` steps.
    """
    claims = CAPABILITY_CLAIMS[name]
    opening = flowed(name)[:300]

    # The opening, checked directly. Asserting over the whole document let the
    # headline reason be deleted while the Behavior step kept the test green —
    # leaving a document that refuses in its first line without saying why.
    assert any(re.search(claim, opening, re.IGNORECASE) for claim in claims), opening[:150]
    assert states(name, *claims, where="Behavior"), claims


@pytest.mark.parametrize("name", NAMES)
def test_refusal_does_not_rest_on_a_passing_repository_fact(name):
    """The reason must still be true when the repository moves on.

    ``/brief`` said *"canon is empty"* and ``/simulate`` said *"there is no
    world state for a model to read"*. Both were true when written and both
    would go false while the refusal stayed architecturally correct — canon
    fills at P7, world state arrives at 232, and neither event builds the
    capability either command is waiting for.

    The deeper version of the same mistake is a claim that **every** blocking
    artifact is absent. Phases are built in order, not at once: 150 lands
    before 152, 232 before 250, 361 before 379, 433 and 437 before 456. In
    each window *"neither is built"* is false and the refusal is still right —
    so the document would be wrong without becoming visibly wrong, which is
    the failure mode worth testing for.

    Scanned across the whole document. Restricted to ``Behavior``, this passed
    a set of files whose ``Role`` sections, openings, ``Input`` sections and
    stop diagrams still carried the claim.
    """
    body = flowed(name).lower()

    for stale in STALE_CLAIMS:
        assert stale not in body, f"{name}: {stale!r}"


def test_current_input_statements_are_not_banned_by_the_blocklist():
    """The blocklist must not overreach into honest input descriptions.

    A refusing surface may say what it has no input for — *"no simulation
    model exists to name"* is an accurate account of today's input contract,
    not a claim that P9 can never arrive. Asserting these survive keeps a
    future tightening of ``STALE_CLAIMS`` from quietly forbidding documents
    from describing their own refusal state.
    """
    assert states("simulate", r"no simulation model exists to name")
    assert states("render", r"nothing composed exists to render")

    for name in ("simulate", "render"):
        body = flowed(name).lower()
        for stale in STALE_CLAIMS:
            assert stale not in body, f"{name}: blocklist now hits a valid input line ({stale!r})"
