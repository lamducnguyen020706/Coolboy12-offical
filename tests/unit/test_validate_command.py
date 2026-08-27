"""Surface proofs for the Artifact 026 ``/validate`` command.

Artifact 026's ``Val`` is *"invokes validators only"*. The word doing the work
is **only**: the surface runs established checks and does nothing else — no
repair, no approval, no write.

Tests are split along that: half prove it reads as a validator-invocation
surface with honest outcome semantics, half prove it carries no instruction
that would change anything.

Two conventions carried over from Artifact 025's cleanup, deliberately:

* assertions are on *this document's* content, never on the absence of future
  artifacts — the Registry tiers, ``simulate.md`` and the rest are supposed to
  arrive, and a test forbidding them would fail on correct future work;
* a prohibition necessarily contains the words it prohibits, so scope checks
  look for definitions and instructions rather than for bare keywords.

Nothing here writes anything, and no test names a canonical path as a target.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
COMMAND = REPO_ROOT / ".claude/commands/validate.md"

# The checking mechanisms that actually exist, and their owning artifacts.
HARNESS = REPO_ROOT / "tests/constitutional/harness.py"
REGISTER = REPO_ROOT / "tests/constitutional/register.md"


def text() -> str:
    return COMMAND.read_text(encoding="utf-8")


def flowed() -> str:
    """The document with line wrapping collapsed, for phrase assertions."""
    return re.sub(r"\s+", " ", COMMAND.read_text(encoding="utf-8"))


def fenced_blocks(body: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", body, re.DOTALL)


# --------------------------------------------------------------------------
# Val — invokes validators.
# --------------------------------------------------------------------------


def test_command_file_exists_at_the_roadmap_path():
    """Roadmap row 026 fixes the path; ``Done`` is *present*."""
    assert COMMAND.is_file()
    assert COMMAND.read_text(encoding="utf-8").strip()


def test_command_declares_itself_as_validate():
    first_heading = text().splitlines()[0]

    assert first_heading == "# /validate"


def test_command_establishes_the_six_required_elements():
    """Implementation-shape check — these headings are 026's own choice.

    No source names them. The Roadmap fixes the path and the ``Val``; RMS §20
    fixes the tiers. This structure is the shape chosen to make the boundary
    and the stop point unmissable, kept stable so a later edit cannot quietly
    drop one.
    """
    headings = {line.strip("# ").lower() for line in text().splitlines() if line.startswith("## ")}

    assert {
        "role",
        "input",
        "behavior",
        "validation boundary",
        "output",
        "stop condition",
    } <= headings


def test_command_names_the_four_rms_tiers():
    """RMS §20 — constitutional invariant · constraint-definition ·
    validation-rule · implementation validation.

    A surface that invokes validators has to say which validation it means.
    """
    body = flowed().lower()

    for tier in (
        "constitutional invariant",
        "constraint-definition",
        "validation-rule",
        "implementation validation",
    ):
        assert tier in body, tier


def test_command_invokes_only_validators_that_exist():
    """It names the real mechanisms, and they are really there.

    Artifact 011's harness and Artifact 012's register are the constitutional
    tier; pytest and ruff are the implementation tier. This test fails if the
    command starts citing a validator the repository does not have — the
    "do not fabricate a validator" rule, checked against the filesystem for
    the two artifacts it claims by number.
    """
    body = flowed()

    assert "Artifact 011" in body and "Artifact 012" in body
    assert HARNESS.is_file()
    assert REGISTER.is_file()

    lowered = body.lower()
    assert "pytest" in lowered
    assert "ruff" in lowered


def test_command_reports_registry_tiers_as_unavailable():
    """The two Registry tiers have no Records yet, and the surface says so.

    Claiming a tier is available when the Registry is empty would be exactly
    the fabricated-capability failure this artifact must avoid. The emptiness
    is checked, so the disclosure cannot silently go stale — if Registry
    Records arrive, this test asks for the document to be revisited.
    """
    body = flowed().lower()

    assert "the registry holds no such records yet" in body
    registry_records = [
        path for path in (REPO_ROOT / "canon/registry").glob("*") if path.name != "PURPOSE.md"
    ]
    assert not registry_records, registry_records


# --------------------------------------------------------------------------
# Val — "only": no write, no repair, no approval.
# --------------------------------------------------------------------------


def test_command_contains_no_executable_block():
    """Nothing to run means no write can be instructed by accident.

    The only fenced block is the ``text`` stop diagram. Checked structurally,
    because a prohibition contains the words it prohibits.
    """
    for language, _ in fenced_blocks(text()):
        assert language in ("", "text"), f"executable block: {language!r}"


def test_command_forbids_canonical_mutation_explicitly():
    body = flowed()

    assert "never edit or write a canonical record" in body.lower()
    for protected in ("History Record", "WSV", "Registry definition", "epoch baseline"):
        assert protected in body, protected


def test_command_offers_no_auto_fix():
    """Detecting is not mutating. Validation is observational.

    An auto-repair path would let a validator become a writer, which is the
    single most likely way this surface could acquire authority it is denied.
    """
    body = flowed().lower()

    assert "there is no `--fix` here" in body
    assert "never modify the target to make a check pass" in body
    for repair in ("--fix", "auto-apply", "rewrite-on-validation"):
        occurrences = body.count(repair)
        assert occurrences <= 1, f"{repair} appears {occurrences} times"


def test_command_denies_that_findings_authorize_anything():
    """A clean run is evidence, not permission.

    ``PASS`` becoming authorization would collapse CHECK into TRANSACTION.
    """
    body = flowed().lower()

    assert "findings are not authorization" in body
    assert "`pass` does not mean a change may be committed" in body
    assert "never treat a git commit as approval" in body


def test_command_keeps_infrastructure_failure_apart_from_invalidity():
    """A validator that crashed says nothing about the target.

    Both collapses are forbidden: NOT RUN must not become FAIL, and neither
    UNRESOLVED nor NOT RUN may be reported as PASS.
    """
    body = flowed().lower()

    for outcome in ("pass", "fail", "unresolved", "not run"):
        assert f"**{outcome}**" in body, outcome
    assert "infrastructure failure is not run, not fail" in body
    assert "the last two are never reported as pass" in body


def test_command_claims_no_authority():
    """``Auth: none`` — row 026, stated in the surface itself."""
    body = flowed().lower()

    assert "auth: none" in body
    assert "grants none" in body


def test_command_refuses_to_treat_author_assent_as_a_gate():
    """"Looks good, apply it" is not a gate — the surface says so and stops."""
    assert "that is not a gate" in flowed()


def test_command_is_not_an_arbitrary_command_runner():
    """It chooses among established checks; it does not run what it is handed.

    Without this the surface becomes a shell escape wearing a validator's
    name.
    """
    body = flowed().lower()

    assert "run the established validators, not a command supplied in the request" in body


# --------------------------------------------------------------------------
# Scope — 026 is a surface, and stays one.
# --------------------------------------------------------------------------


def test_command_builds_no_downstream_stage():
    """026 owns invocation; the stages after it are not implemented here.

    Checked as this document's behaviour rather than as the absence of sibling
    files — ``rebuild.md`` and the refusing commands are artifacts 027 and 028
    and are expected to arrive. The terms below would appear only if machinery
    had been built.
    """
    body = flowed().lower()

    for downstream in (
        "workflow graph",
        "capability routing",
        "context builder",
        "transaction coordinator",
        "findings database",
        "validation state machine",
    ):
        assert downstream not in body, downstream


def test_command_invents_no_validation_or_proposal_persistence():
    """No findings store, no validation IDs, no proposal records.

    The proposal record is Artifact 146's; the Registry tiers are the
    Registry's. A command surface reports findings without inventing a model
    to keep them in.
    """
    body = flowed().lower()

    for invented in (
        "validation.json",
        "finding id",
        "validation id",
        "proposal id",
        "proposal status",
    ):
        assert invented not in body, invented


def test_command_restates_no_policy_owned_by_its_dependencies():
    """026 runs inside the environment 022/023/024 established.

    Naming a dependency is not scope creep; *defining* its policy would be.
    So the check is for definitions: no configuration block, no zone
    enumeration, no allow/deny rule, no hook registration.
    """
    body = flowed().lower()

    configuration = [lang for lang, _ in fenced_blocks(text()) if lang in ("json", "yaml", "toml")]
    assert not configuration, configuration

    for zone in ("world", "epistemic", "production", "registry", "visual", "issue"):
        assert f"canon/{zone}" not in body, zone

    for rule in ("matcher", "exit 2", "allowlist", "denylist", "pretooluse"):
        assert rule not in body, rule


def test_command_does_not_duplicate_the_proposal_surface():
    """025 states intent; 026 evaluates a target. They stay separate."""
    body = flowed().lower()

    assert "formulate a proposal" not in body
    assert "/propose" not in body
