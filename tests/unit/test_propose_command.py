"""Surface proofs for the Artifact 025 ``/propose`` command.

Artifact 025's ``Val`` is *"produces a proposal, never a write"*. Half of that
is a claim about what the command surface **says**, and half is a claim about
what it **cannot do** — so the tests are split the same way: the command must
read as a proposal entry point, and it must carry no instruction that would
reach canon.

The command is prose, not code, so these are checks on a document. That is the
right shape for a ``T: config`` · ``R: SURFACE`` artifact: there is no engine
to exercise, and inventing one to make the tests look busier would be the scope
creep this artifact exists to avoid.

Nothing here writes anything, and no test names a canonical path as a target.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
COMMAND = REPO_ROOT / ".claude/commands/propose.md"


def text() -> str:
    return COMMAND.read_text(encoding="utf-8")


def flowed() -> str:
    """The document with line wrapping collapsed.

    Phrase assertions run against this, so that reflowing a paragraph never
    breaks a test. A wrapped ``Registry\\ndefinition`` is the same statement as
    the unwrapped one, and a test that disagrees is testing the margin.
    """
    return re.sub(r"\s+", " ", COMMAND.read_text(encoding="utf-8"))


def fenced_blocks(body: str) -> list[tuple[str, str]]:
    """Every fenced block as ``(language, contents)``."""
    return re.findall(r"```(\w*)\n(.*?)```", body, re.DOTALL)


# --------------------------------------------------------------------------
# Val, first half — it produces a proposal.
# --------------------------------------------------------------------------


def test_command_file_exists_at_the_roadmap_path():
    """Roadmap row 025 fixes the path; ``Done`` is *present*."""
    assert COMMAND.is_file()
    assert COMMAND.read_text(encoding="utf-8").strip()


def test_command_declares_itself_as_propose():
    """The surface is ``/propose`` and says so in its first heading."""
    first_heading = text().splitlines()[0]

    assert first_heading == "# /propose"


def test_command_establishes_the_six_required_elements():
    """Role, input, behavior, constraint, output, stop condition.

    These are the elements a command surface needs to be unambiguous about
    what it takes, what it does, and — the part that matters here — where it
    stops.
    """
    headings = {line.strip("# ").lower() for line in text().splitlines() if line.startswith("## ")}

    assert {"role", "input", "behavior", "constraint", "output", "stop condition"} <= headings


def test_command_is_intent_centric_rather_than_a_form():
    """§23.3 — asking the author to choose capabilities is a P-13 failure.

    The author states an intent; the system composes. A surface that made the
    author pick a domain, a validator or a severity would have moved a
    Composer decision onto them.
    """
    body = flowed().lower()

    assert "plain-language intent" in body
    assert "do not make the author name a domain" in body


def test_command_names_the_mutation_path_and_its_own_place_in_it():
    """Blueprint §12.6 — one route, and this surface is its first stage."""
    body = flowed()

    for stage in ("PROPOSE", "CHECK", "HUMAN GATE", "TRANSACTION"):
        assert stage in body, stage
    assert "§12.6" in body


# --------------------------------------------------------------------------
# Val, second half — never a write.
# --------------------------------------------------------------------------


def test_command_contains_no_executable_block():
    """The strongest guarantee available to a prose surface: nothing to run.

    A command that carries no shell or Python block cannot instruct a write by
    accident. The only fenced blocks here are ``text`` diagrams. This is
    checked structurally rather than by scanning for dangerous strings,
    because a prohibition necessarily contains the words it prohibits.
    """
    for language, _ in fenced_blocks(text()):
        assert language in ("", "text"), f"executable block: {language!r}"


def test_command_issues_no_write_instruction():
    """No imperative that would reach the filesystem or version control.

    Phrased as instruction patterns rather than bare words: the document says
    "never treat a git commit as approval", and a naive scan for "git commit"
    would fail on its own prohibition.
    """
    body = flowed().lower()
    forbidden = (
        "run `git commit",
        "then commit",
        "apply the proposal",
        "write the record",
        "edit the record",
        "update the canonical",
        "commit the change",
    )

    for pattern in forbidden:
        assert pattern not in body, pattern


def test_command_forbids_canonical_mutation_explicitly():
    """The prohibition is stated, not merely implied by omission."""
    body = flowed()

    assert "never change a canonical record" in body.lower()
    assert "§26.8" in body
    for protected in ("History Record", "WSV", "Registry definition", "epoch baseline"):
        assert protected in body, protected


def test_command_claims_no_authority():
    """``Auth: none`` — it cannot approve, gate, canonicalize or commit."""
    body = flowed().lower()

    assert "auth: none" in body
    assert "sole authority" in body


def test_command_does_not_claim_later_stages_have_run():
    """CHECK, the Human Gate and the Coordinator are not built.

    A surface that reported them as passed would be describing a mutation path
    that does not exist.
    """
    body = flowed().lower()

    assert "never state that check, the human gate, or a commit has happened" in body
    assert "stop when the proposal is stated" in body


def test_command_refuses_to_treat_author_assent_as_a_gate():
    """"Yes, do it" is not the Human Gate — the surface says so and stops.

    Without this, the obvious next turn after a proposal becomes a hidden
    approval path.
    """
    assert "is not a Human Gate" in flowed()


def test_command_assigns_no_severity():
    """Severity is CHECK's finding (§12.6), not this surface's."""
    body = flowed().lower()

    assert "never assign a severity class" in body
    for claim in ("this is trivial", "this is standard", "this is structural"):
        assert claim not in body, claim


# --------------------------------------------------------------------------
# Scope — 025 is a surface, and stays one.
# --------------------------------------------------------------------------


def test_command_invents_no_proposal_persistence():
    """No proposal area exists yet, and this artifact does not create one.

    §26.8 anticipates one; the repository has none. Artifact 146 owns the
    proposal record. The surface must say so rather than inventing a
    directory, a schema or a file format — and the directory must genuinely
    not exist, or the disclaimer is stale.
    """
    body = flowed().lower()

    assert "no proposal staging area in this repository yet" in body
    assert "artifact 146" in body
    assert not (REPO_ROOT / "proposals").exists()


def test_command_does_not_fake_a_basis_stamp():
    """P-22 is named as unmet, not simulated.

    §12.6 requires a proposal to carry the canon revision, epoch and objects
    read. None of that exists. Claiming it would be a false guarantee; the
    surface records what it actually read instead.
    """
    body = flowed().lower()

    assert "p-22" in body
    assert "do not fabricate a basis stamp" in body


def test_artifact_025_creates_no_downstream_artifact():
    """025 is the surface alone — 026-028, 127, 146 and 152 stay unbuilt."""
    assert not (REPO_ROOT / "docs/constitution/proposal.md").exists()
    for sibling in ("validate.md", "simulate.md", "render.md", "rebuild.md"):
        assert not (REPO_ROOT / ".claude/commands" / sibling).exists(), sibling


def test_artifact_025_does_not_touch_its_dependencies():
    """The surface consumes 022/023/024; it does not re-implement them.

    A reference to the hook, the zone file or the settings would mean policy
    had migrated into a command surface that holds no authority.
    """
    body = flowed()

    for owned_elsewhere in ("canon_deny.py", "zones.json", "settings.json", "PreToolUse"):
        assert owned_elsewhere not in body, owned_elsewhere
