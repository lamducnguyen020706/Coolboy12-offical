"""Surface proofs for the Artifact 027 ``/rebuild`` stub.

Roadmap row 027 is unusual among the command surfaces: its ``Val`` is
*"refuses until the derived layer exists"* and its ``Done`` is *"stub refuses
cleanly"*. The artifact succeeds by **not** working, so the tests prove a
refusal rather than a capability.

Three things have to hold together:

* the refusal is stated, with a reason and an unlocking condition — *"honest
  refusal beats a broken command"*;
* the condition it refuses on is really true, so the refusal cannot go stale
  unnoticed;
* refusing does not quietly become a licence to do something else — no
  rebuild, no repair, no write.

Conventions carried from Artifacts 025 and 026: assertions are on this
document's content rather than on the absence of future artifacts, and scope
checks look for definitions and instructions rather than bare keywords, since
a prohibition contains the words it prohibits.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
COMMAND = REPO_ROOT / ".claude/commands/rebuild.md"

# Artifact 020 — the governing rebuild contract this stub defers to.
CONVENTION = REPO_ROOT / "docs/conventions/rebuild.md"
DERIVED = REPO_ROOT / "derived"


def text() -> str:
    return COMMAND.read_text(encoding="utf-8")


def flowed() -> str:
    """The document with line wrapping collapsed, for phrase assertions."""
    return re.sub(r"\s+", " ", COMMAND.read_text(encoding="utf-8"))


def fenced_blocks(body: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", body, re.DOTALL)


# --------------------------------------------------------------------------
# Val — refuses until the derived layer exists.
# --------------------------------------------------------------------------


def test_command_file_exists_at_the_roadmap_path():
    """Roadmap row 027 fixes the path; ``Done`` is *stub refuses cleanly*."""
    assert COMMAND.is_file()
    assert COMMAND.read_text(encoding="utf-8").strip()


def test_command_declares_itself_as_rebuild():
    assert text().splitlines()[0] == "# /rebuild"


def test_command_refuses_and_says_so_first():
    """The refusal is the headline, not a caveat buried at the end.

    A reader who stops after one line must already know the command will not
    rebuild anything.
    """
    opening = flowed()[:200].lower()

    assert "this command refuses" in opening


def test_refusal_carries_a_reason_and_an_unlocking_condition():
    """*Honest refusal beats a broken command* — row 027's ``Why``.

    A bare "not implemented" would be a broken command wearing a polite
    message. The refusal has to say why it refuses and what would end it.
    """
    body = flowed().lower()

    assert "the repository holds no derived data" in body
    assert "declare their rebuild methods" in body
    assert "artifact 173" in body and "artifact 227" in body


def test_the_condition_it_refuses_on_is_actually_true():
    """The derived layer really is empty, so the refusal is not stale.

    Checked against the filesystem: ``derived/`` holds only the ``PURPOSE.md``
    files Artifact 001 created. If derived artifacts ever land, this test asks
    for the stub to be revisited rather than letting it keep refusing on a
    reason that stopped being true.
    """
    derived_artifacts = [
        path
        for path in DERIVED.rglob("*")
        if path.is_file() and path.name != "PURPOSE.md"
    ]

    assert not derived_artifacts, derived_artifacts


def test_command_defers_to_artifact_020_for_what_rebuilding_means():
    """020 is ``Auth: governing`` for rebuild; 027 is ``Auth: none``.

    The stub must point at the contract rather than restate or invent one.
    """
    body = flowed()

    assert "Artifact 020" in body
    assert "docs/conventions/rebuild.md" in body
    assert CONVENTION.is_file()
    assert "§29.8" in body


# --------------------------------------------------------------------------
# Refusing is not a licence to do something else.
# --------------------------------------------------------------------------


def test_command_contains_no_executable_block():
    """Nothing to run. The only fenced block is the ``text`` stop diagram."""
    for language, _ in fenced_blocks(text()):
        assert language in ("", "text"), f"executable block: {language!r}"


def test_command_forbids_canonical_mutation_explicitly():
    body = flowed()

    assert "never edit or write a canonical record" in body.lower()
    for protected in ("History Record", "WSV", "Registry definition", "epoch baseline"):
        assert protected in body, protected


def test_command_never_rewrites_source_truth_to_make_a_rebuild_pass():
    """The inversion §29.8 exists to catch.

    A rebuild reconstructs derived state *from* canon. Editing canon so a
    rebuild succeeds would destroy the very signal the drill is run to
    produce — and would turn a rebuild command into a canonical writer.
    """
    body = flowed().lower()

    assert "it never rewrites source truth to make a rebuild succeed" in body
    assert "architectural finding" in body
    assert "there is no `--fix` here" in body


def test_command_does_not_report_a_refusal_as_success_or_failure():
    """A missing capability is neither a pass nor a broken run.

    Collapsing either way would misreport the state of the system: "rebuilt
    nothing, all good" is a false pass, and "rebuild failed" would look like a
    defect in something that was never built.
    """
    body = flowed().lower()

    assert "do not report success for a no-op" in body
    assert "never as a failure and never as a pass" in body


def test_command_does_not_partially_run_or_simulate():
    body = flowed().lower()

    assert "do not partially run" in body
    assert "do not simulate a rebuild" in body


def test_command_claims_no_authority():
    """``Auth: none`` — a rebuild is not approval, a gate, or a commit."""
    body = flowed().lower()

    assert "auth: none" in body
    assert "not approval, not a gate, and not a commit" in body
    assert "never treat a git commit as approval" in body


def test_command_is_not_an_arbitrary_command_runner():
    """It would invoke declared methods, never a command it is handed."""
    body = flowed().lower()

    assert "this surface invokes declared methods, not supplied ones" in body


def test_command_will_not_guess_a_target():
    """An absent target is unresolved, never *rebuild everything*."""
    body = flowed().lower()

    assert "will not be treated as *rebuild everything*" in body
    assert "reported as unresolved" in body


# --------------------------------------------------------------------------
# Scope — 027 is a stub, and stays one.
# --------------------------------------------------------------------------


def test_stub_creates_no_rebuild_infrastructure():
    """No engine, no output area, no persisted state.

    A command surface does not justify infrastructure, and a *refusing* one
    justifies none at all.

    The positive assertion carries the weight. The banned terms are ones that
    would appear only while *defining* infrastructure — deliberately not
    "status store", which the document uses in its own disclaimer, since a
    prohibition contains the words it prohibits.
    """
    body = flowed().lower()

    assert "creates no directory, no output area, and no rebuild state of its own" in body
    for invented in ("build graph", "rebuild manifest", "artifact cache", "rebuild id"):
        assert invented not in body, invented


def test_stub_builds_no_downstream_stage():
    """027 owns the refusal; the stages after it are not implemented here.

    Checked as this document's behaviour, not as the absence of sibling files
    — Artifact 028's commands and the P8 rebuild capability are expected to
    arrive.
    """
    body = flowed().lower()

    for downstream in (
        "workflow graph",
        "capability routing",
        "transaction coordinator",
        "mutation coordinator",
        "human gate",
    ):
        assert downstream not in body, downstream


def test_stub_restates_no_policy_owned_by_its_dependencies():
    """027 runs inside the environment 022/023/024 established.

    Naming a dependency is not scope creep; defining its policy would be.
    """
    body = flowed().lower()

    configuration = [lang for lang, _ in fenced_blocks(text()) if lang in ("json", "yaml", "toml")]
    assert not configuration, configuration

    for zone in ("world", "epistemic", "production", "visual", "issue"):
        assert f"canon/{zone}" not in body, zone

    for rule in ("matcher", "exit 2", "allowlist", "denylist", "pretooluse"):
        assert rule not in body, rule


def test_stub_does_not_duplicate_the_other_command_surfaces():
    """025 states intent, 026 invokes validators, 027 refuses. Kept apart."""
    body = flowed().lower()

    assert "/propose" not in body
    assert "/validate" not in body
    assert "formulate a proposal" not in body
