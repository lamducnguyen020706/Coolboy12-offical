"""The standards, where the runner is actually coupled to them.

These tests deliberately do not assert prose. They check the couplings that
would silently break the pipeline — the §14.1 report contract the runner
validates against, the verdict vocabulary it parses — and they check that
the sections carrying existing protections still exist, so a future
reorganization cannot quietly drop one.
"""

from __future__ import annotations

import pytest
from audit_runner import patchcheck, verdict

from .conftest import REAL_REPO_ROOT

AUDIT_STANDARD = REAL_REPO_ROOT / "hhtech" / "standards" / "audit-standard.md"
PATCH_STANDARD = REAL_REPO_ROOT / "hhtech" / "standards" / "patch-standard.md"


@pytest.fixture(scope="module")
def audit_text():
    return AUDIT_STANDARD.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def patch_text():
    return PATCH_STANDARD.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Couplings between the runner and the standards
# ---------------------------------------------------------------------------

def test_report_contract_sections_match_the_runner(audit_text):
    """Every section the runner requires in a report is a section the audit
    standard actually asks for. A divergence here rejects valid reports."""
    for section in verdict.REQUIRED_SECTIONS:
        assert section in audit_text, (
            f"the runner requires a {section!r} section that audit-standard.md "
            "no longer asks the auditor to produce"
        )


def test_verdict_vocabulary_is_documented(audit_text):
    for value in verdict.VALID_VERDICTS:
        assert value in audit_text
    for qualifier in verdict.BLOCKED_QUALIFIERS:
        assert qualifier in audit_text, (
            f"the runner accepts the BLOCKED qualifier {qualifier!r} but the "
            "standard does not define it"
        )


def test_patchprompt_safety_phrases_are_documented(patch_text):
    """The phrases patchcheck enforces are contract, so the standard — not
    only the runner's prompt string — must define them."""
    assert patchcheck.NO_PATCH_PHRASE in patch_text
    assert patchcheck.DO_NOT_PATCH_PHRASE in patch_text


def test_three_patchprompt_contracts_are_defined(patch_text):
    section = patch_text.split("## 33. The Three Patch-Prompt Contracts", 1)[1]
    section = section.split("\n## ", 1)[0]
    for verdict_value in ("PATCH REQUIRED", "PASS", "BLOCKED"):
        assert verdict_value in section


def test_patchreport_remains_forbidden(patch_text):
    """patch-standard.md §20 defines a result schema, not a repository file;
    the runner rejects a prompt that instructs one."""
    assert "patchreport.md" in patch_text  # named, in order to be forbidden
    assert "not** a required repository file" in patch_text or (
        "not a required repository file" in patch_text
    )


# ---------------------------------------------------------------------------
# Existing protections must survive any reorganization (§47)
# ---------------------------------------------------------------------------

EXISTING_AUDIT_SECTIONS = (
    "Authoritative Source Set and Precedence",
    "Audit Scope",
    "Audit Modes",
    "Mandatory Audit Passes",
    "Evidence Standard",
    "Requirement Traceability",
    "Severity",
    "False-Positive Control",
    "Test Audit",
    "Diff Audit",
    "Verdict Model",
    "Audit Report Contract",
    "Re-Audit Rules",
    "Patch Boundary",
    "Negative Audit",
    "Verification Checklist",
)

EXISTING_PATCH_SECTIONS = (
    "Authoritative Inputs",
    "Patch Scope",
    "Finding Intake",
    "Pre-Patch Analysis",
    "Finding Validation",
    "Patch Order",
    "Minimal Change Rule",
    "Preservation Rule",
    "Authority Protection",
    "Traceability",
    "Diff Firewall",
    "Implementation Validation",
    "Negative Validation",
    "Regression Control",
    "Disputed / Unverifiable Findings",
    "Patch Completion Criteria",
    "Post-Patch Self-Audit",
    "Re-Audit Handoff",
    "Patch Result Contract",
    "Universal Patch Execution Contract",
)


@pytest.mark.parametrize("section", EXISTING_AUDIT_SECTIONS)
def test_existing_audit_protections_survive(audit_text, section):
    assert section in audit_text


@pytest.mark.parametrize("section", EXISTING_PATCH_SECTIONS)
def test_existing_patch_protections_survive(patch_text, section):
    assert section in patch_text


# ---------------------------------------------------------------------------
# The new mandatory contracts are present
# ---------------------------------------------------------------------------

NEW_AUDIT_CONTRACTS = (
    "The Reasoning Chain",
    "The Constitutional Gate",
    "Ownership and Custody Matrix",
    "Cross-Artifact Collision Audit",
    "Universalization Audit",
    "Open-Boundary Audit",
    "Severity Justification",
    "The P0/P1 Gate",
    "Finding Deduplication",
    "Finding Closure Contract",
    "Patch Minimality Review",
    "Post-Patch Regression Audit",
    "Diff and Scope Proof",
    "Verdict Vocabulary",
)

NEW_PATCH_CONTRACTS = (
    "The Eleven-Stage Patch Pipeline",
    "Reproduce Before Edit",
    "Direct Source Reading",
    "The Forbidden Patch Escape",
    "Architectural Protection",
    "Adversarial Regression",
    "Proportional Structural Validation",
    "Local Tracking File Protection",
    "The Self-Audit Matrix",
    "Independent Re-Audit Closes the Finding",
)


@pytest.mark.parametrize("contract", NEW_AUDIT_CONTRACTS)
def test_new_audit_contracts_present(audit_text, contract):
    assert contract in audit_text


@pytest.mark.parametrize("contract", NEW_PATCH_CONTRACTS)
def test_new_patch_contracts_present(patch_text, contract):
    assert contract in patch_text


def test_constitutional_gate_lists_all_fourteen_conditions(audit_text):
    gate = audit_text.split("## 20. The Constitutional Gate", 1)[1].split("\n## ", 1)[0]
    rows = [line for line in gate.splitlines() if line.strip().startswith("| ")]
    numbered = [r for r in rows if r.strip().lstrip("| ").split(" |")[0].strip().isdigit()]
    assert len(numbered) == 14, f"expected 14 gate conditions, found {len(numbered)}"


def test_reproduce_before_edit_names_all_four_outcomes(patch_text):
    for outcome in (
        "FINDING REPRODUCIBLE",
        "FINDING NOT REPRODUCIBLE",
        "FINDING CONTRADICTED BY SOURCE",
        "INSUFFICIENT EVIDENCE",
    ):
        assert outcome in patch_text


def test_local_tracking_files_named_in_the_protection_section(patch_text):
    section = patch_text.split("## 31. Local Tracking File Protection", 1)[1]
    section = section.split("\n## ", 1)[0]
    assert "reports/implement-log.json" in section
    assert "reports/progress.json" in section


def test_standards_claim_no_architectural_authority(audit_text, patch_text):
    """The procedure/authority boundary must survive the upgrade."""
    for text in (audit_text, patch_text):
        # normalized: these sentences wrap across lines in the source
        flat = " ".join(text.split())
        assert "carries no architectural authority" in flat
        assert "they are right and this document is wrong" in flat
