"""Shared fixtures for the HHTECH audit runner test suite.

Every test runs against a throwaway git repository built here, with a local
bare "origin" — never the real COOLBOY12 repository, never a real network
remote, and never a real HHTECH API key. Luna is always a stub supplied by
the test, so no test makes a paid API call.

The fixture repository mirrors the real one's *shapes*: version-stamped
source filenames, a Spine section, invariant registers as markdown tables,
an anti-ordering PART, a gate PART, 25-field manifest rows, and a universal
conformance artifact whose row unlocks `all`.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

REAL_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(cwd), *args], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, f"git {args} failed: {result.stderr}"
    return result.stdout


BLUEPRINT_TEXT = textwrap.dedent(
    """\
    # coolboy12 v9.9.9 (test fixture)

    ## 7. Design Principles

    P-1 through P-40, abbreviated for the fixture.

    ## 10. The Spine — The Frozen Constitutional Core

    | # | Law | Rule |
    |---|---|---|
    | 1 | One Canon | Exactly one canonical truth about the universe. |
    | 2 | One Path | Canon changes only through propose to gate to commit. |
    | 3 | One Authority | Only the human commits canon. |

    The Spine is frozen. Ten laws, unamended.

    ## 13. The Record System

    Section 13 body text. The Record System supersedes the Canon Object Model.

    ### 13.6 Six sovereign Record Models

    W, E, P, R, V, I. No seventh model.

    ## 14. Knowledge-State Architecture

    Unrelated section that must never leak into a §13 extraction.

    ## 36. Invariant Register

    ### 36.1 Truth and Authority

    | # | Invariant | Where |
    |---|---|---|
    | I-01 | Exactly one canonical truth exists. | Spine 1 |
    | I-87 | The Record is the architectural unit, not a universal semantic model. | §13 |
    | I-101 | Every partition owns exactly one sovereign Record Model. | §13.6 |
    | I-104 | Record and Canon are not synonyms. | §13.0 |
    """
)

RMS_TEXT = textwrap.dedent(
    """\
    # COOLBOY12_RECORD_MODEL_SYSTEM_v9.9 (test fixture)

    # 2. Constitutional Status

    The RMS is joint primary authority with the Blueprint.

    # 6. Record Model Definition

    A Record Model owns a semantic question no other model answers.

    ## 6.1 The Seven Architectural Categories `FROZEN`

    Categories listed here.

    # 7. World Record Model

    Unrelated section.

    # 26. System-wide Invariants

    I-16 partition ownership · I-87 Record is the architectural unit · I-101 sovereignty ·
    I-102 RR/HR World-specific · I-104 Record is not Canon.
    """
)

AUDIT_STANDARD_TEXT = (
    "# audit-standard.md (test fixture)\n\n"
    "Audit procedure only, never architectural authority.\n\n"
    "## 13. Verdict Model\n\nPASS / PATCH REQUIRED / BLOCKED.\n\n"
    "## 14. Audit Report Contract\n\nFifteen sections, in order.\n"
)
PATCH_STANDARD_TEXT = (
    "# patch-standard.md (test fixture)\n\n"
    "Patch procedure only, never architectural authority.\n\n"
    "## 21. Universal Patch Execution Contract\n\n"
    "READ -> VALIDATE -> PLAN -> PATCH -> TEST -> INSPECT DIFF -> SELF-AUDIT -> HAND OFF.\n"
)

CLAUDE_TEXT = "# COOLBOY12 — Standing Instructions (test fixture)\n\nSession conduct only.\n"

CONVENTIONS_TEXT = (
    "# Artifact + Phase Conventions (test fixture)\n\n"
    "Twenty-five fields, stated never inherited. RULE G / G2 / G3.\n"
)


def manifest_row(
    artifact_id: str,
    name: str,
    path: str,
    *,
    h: str = "—",
    s: str = "—",
    ls: str = "—",
    g: str = "—",
    unlocks: str = "999",
    bp: str = "§13",
    rms: str = "§6",
    req: str = "RR-06",
) -> str:
    return (
        f"**{artifact_id}** · {name} · `{path}` · "
        "Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · "
        f"Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a · Req: {req} · "
        f"BP: {bp} · RMS: {rms} · H: {h} · S: {s} · LS: {ls} · G: {g} · → {unlocks} · "
        "Val: test validation criterion · Done: test done criterion · "
        "Why: test rationale · Risk: medium · ∥: no"
    )


ROADMAP_TEXT = "\n".join(
    [
        "# COOLBOY12 — FILE BUILD ROADMAP (test fixture)",
        "",
        "# PART IV — COMPLETE ARTIFACT MANIFEST",
        "",
        manifest_row(
            "003", "artifact + phase conventions",
            "docs/conventions/artifact_conventions.md",
            h="001", unlocks="all", bp="§7", rms="n/a", req="BR-01",
        ),
        "",
        manifest_row("039", "Record System constitution", "docs/target/dep039.md",
                     h="031", unlocks="040–059", bp="§13", rms="§§2,6"),
        "",
        manifest_row("041", "six-model sovereignty contract", "docs/target/dep041.md",
                     h="039", s="040", bp="§13.6", rms="§2"),
        "",
        manifest_row("042", "Target artifact", "docs/target/thing.md",
                     h="039", ls="043", g="G-TEST", unlocks="040"),
        "",
        manifest_row("043", "Brand-new artifact", "docs/target/new.md", ls="042"),
        "",
        manifest_row("044", "Glob-scoped artifact", "docs/target/multi/*.md"),
        "",
        manifest_row("045", "Directory-scoped artifact", "docs/target/dir/"),
        "",
        manifest_row("046", "Malformed-row artifact", "docs/target/broken.md"),
        "",
        "# PART VIII — GATES",
        "",
        "| Gate | Meaning |",
        "|---|---|",
        "| G-TEST | fixture gate, must be passed before the artifact may proceed |",
        "",
        "# PART IX — ANTI-ORDERINGS",
        "",
        "| ID | Prohibited order | Reason | Source | Phase |",
        "|---|---|---|---|---|",
        "| X-04 | Implementation before architecture | Code encodes undecided semantics | RMS §13 | all |",
        "| X-08 | World mechanism becoming universal | RR/HR exported | I-102 | all |",
        "",
        "# PART X — CANONICAL DATA GATES",
        "",
        "Nothing here.",
        "",
    ]
)

# The target artifact cites Artifact 041, invariants, an anti-ordering, and
# sections beyond its declared BP/RMS citations — exactly the "citation
# coverage is a floor" case the resolver must handle generically.
TARGET_042_TEXT = textwrap.dedent(
    """\
    # Record Model definition (test fixture target)

    A Record Model owns a semantic question. See Artifact 041 for the
    sovereignty contract this definition depends on, and Artifact 039 for the
    Record System constitution.

    Invariant I-101 establishes sovereignty; I-104 separates Record from
    Canon. Anti-ordering X-08 forbids exporting a World mechanism.

    Blueprint §13.6 fixes the six models. RMS §2 states constitutional status.
    Requirement RR-06 governs this artifact.
    """
)


def make_audit_response(
    artifact_id: str, verdict_word: str, findings: str = "(none blocking in this fixture)"
) -> str:
    """A contract-complete auditreport.md body: all fifteen §14.1 sections and
    exactly one terminal VERDICT line, as the final line."""
    return textwrap.dedent(
        f"""\
        # hhtech/auditreport.md

        ## Audit Identity
        Artifact {artifact_id} audit, GPT-5.6 Luna, test fixture run.

        ## Target Artifact
        Artifact {artifact_id} — target artifact under test.

        ## Audit Mode
        Full Artifact Audit.

        ## Source Set
        Blueprint §13 (supplied), RMS §6 (supplied), Roadmap row {artifact_id}
        (supplied), target file (supplied).

        ## Scope
        The declared Roadmap scope for artifact {artifact_id}.

        ## Executive Verdict
        The result is stated on the terminal line of this report.

        ## Requirement Coverage
        RR-06: UNVERIFIABLE, non-blocking — requirement register absent.

        ## Findings
        {findings}

        ## Evidence
        Target content matches its declared scope.

        ## Regression Analysis
        Compared against the committed baseline; nothing weakened.

        ## Diff Analysis
        No unrelated changed files within the declared scope.

        ## Unverifiable Items
        RR-06, non-blocking.

        ## False-Positive Checks
        The §10 checklist was applied; no suspicion was promoted to a finding.

        ## Final Verdict
        Restated on the terminal line below.

        ## Re-Audit Requirements
        Re-run ./hhtech/audit {artifact_id} after any change.

        VERDICT: {verdict_word}
        """
    )


def make_patch_prompt(artifact_id: str, verdict_word: str) -> str:
    """A contract-valid patchprompt for each verdict."""
    if verdict_word == "PATCH REQUIRED":
        return textwrap.dedent(
            f"""\
            # hhtech/patchprompt.md

            ## Task
            Patch Artifact {artifact_id} under patch-standard.md. A patch is required.

            ## Target scope
            Only the declared Roadmap scope of Artifact {artifact_id}.

            ## Findings
            AUD-{artifact_id}-01 (P1): fixture finding, per the audit report.
            Requirement: RR-06. Evidence: cited in the audit report.
            Remediation: correct the stated defect, minimally.

            ## Authority constraints
            Do not modify the Blueprint, the RMS, the Roadmap or either standard.
            Severity is exactly what the audit assigned.

            ## Required steps
            READ -> VALIDATE -> PLAN -> PATCH -> TEST -> INSPECT DIFF -> SELF-AUDIT
            -> HAND OFF FOR RE-AUDIT.

            ## Validation
            Re-run the repository checks and inspect the diff.

            ## Re-audit handoff
            Re-run ./hhtech/audit {artifact_id}.
            """
        )
    if verdict_word == "PASS":
        return textwrap.dedent(
            f"""\
            # hhtech/patchprompt.md

            ## Task
            NO PATCH REQUIRED for Artifact {artifact_id}.

            ## Result
            The audit completed with PASS. The next operation is no artifact patch.

            ## Forbidden
            Do not modify the target artifact. Do not invent a patch. Do not weaken
            any source requirement to create work. Do not modify the Blueprint, the
            RMS, the Roadmap or either standard.

            ## Re-audit
            Re-running ./hhtech/audit {artifact_id} is how a later re-audit happens.
            """
        )
    return textwrap.dedent(
        f"""\
        # hhtech/patchprompt.md

        ## Task
        DO NOT PATCH Artifact {artifact_id}. The audit is BLOCKED.

        ## Blocking reason
        A required evidence source was not supplied to the audit, so a mandatory
        condition's compliance could not be determined.

        ## Unavailable sources
        - Requirement register (absent from the repository)

        ## This is an audit-context gap, not an artifact defect
        Nothing here establishes a defect in Artifact {artifact_id}. Do not patch the
        artifact to clear the block, do not invent source content, and do not weaken
        any requirement.

        ## Required action
        Resolve the evidence gap, then re-run the audit: ./hhtech/audit {artifact_id}.
        """
    )


class LunaStub:
    """Records every call and returns queued responses in order. Raises if
    called more often than responses were queued, or if an exception instance
    was queued for that call. Never makes a network request."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls: list[tuple[str, str]] = []

    def __call__(self, config, system_prompt, user_content):
        self.calls.append((system_prompt, user_content))
        if not self.responses:
            raise AssertionError("LunaStub called more times than responses were queued")
        result = self.responses.pop(0)
        if isinstance(result, BaseException):
            raise result
        return result


def verdict_stub(artifact_id: str, verdict_word: str) -> LunaStub:
    """The two-call stub every successful run needs: audit, then patchprompt."""
    return LunaStub(
        [
            make_audit_response(artifact_id, verdict_word),
            make_patch_prompt(artifact_id, verdict_word),
        ]
    )


def build_fixture_repo(tmp_path: Path) -> Path:
    origin = tmp_path / "origin.git"
    origin.mkdir()
    git(origin, "init", "--bare", "-b", "main")

    work = tmp_path / "work"
    work.mkdir()
    git(work, "init", "-b", "main")
    git(work, "config", "user.email", "test@example.invalid")
    git(work, "config", "user.name", "Test Runner")
    git(work, "remote", "add", "origin", str(origin))

    sources = work / "docs" / "sources"
    sources.mkdir(parents=True)
    (sources / "COOLBOY12_MASTER_BLUEPRINT_v9.9.9.md").write_text(BLUEPRINT_TEXT)
    (sources / "COOLBOY12_RECORD_MODEL_SYSTEM_v9.9.md").write_text(RMS_TEXT)
    (sources / "COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md").write_text(ROADMAP_TEXT)

    standards = work / "hhtech" / "standards"
    standards.mkdir(parents=True)
    (standards / "audit-standard.md").write_text(AUDIT_STANDARD_TEXT)
    (standards / "patch-standard.md").write_text(PATCH_STANDARD_TEXT)
    (work / "hhtech" / "auditreport.md").write_text("")
    (work / "hhtech" / "patchprompt.md").write_text("")
    # The runner-tree markers repo.find_repo_root() looks for.
    (work / "hhtech" / "audit_runner").mkdir(parents=True)

    (work / "CLAUDE.md").write_text(CLAUDE_TEXT)
    conventions = work / "docs" / "conventions"
    conventions.mkdir(parents=True)
    (conventions / "artifact_conventions.md").write_text(CONVENTIONS_TEXT)

    target = work / "docs" / "target"
    (target / "multi").mkdir(parents=True)
    (target / "dir").mkdir(parents=True)
    (target / "thing.md").write_text(TARGET_042_TEXT)
    (target / "dep039.md").write_text("# Record System constitution (fixture)\n")
    (target / "dep041.md").write_text("# Sovereignty contract (fixture)\n")
    (target / "multi" / "a.md").write_text("# multi a\n")
    (target / "multi" / "b.md").write_text("# multi b\n")
    (target / "dir" / "one.md").write_text("# dir one\n")
    (target / "dir" / "two.md").write_text("# dir two\n")
    # 043's docs/target/new.md is deliberately absent: a declared but
    # not-yet-built artifact with no committed baseline.

    git(work, "add", "-A")
    git(work, "commit", "-m", "initial fixture state")
    git(work, "push", "-u", "origin", "main")
    return work


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """A throwaway repo with a local bare origin, on branch `main`."""
    work = build_fixture_repo(tmp_path)
    monkeypatch.setenv("HHTECH_API_KEY", "test-fixture-key-not-real")
    # Deliberately chdir somewhere unrelated: nothing in the runner may
    # resolve the repository from the process working directory.
    monkeypatch.chdir(tmp_path)
    return work
