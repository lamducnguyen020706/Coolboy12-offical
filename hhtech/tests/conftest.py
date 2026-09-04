"""Shared fixtures for the HHTECH audit runner test suite.

Every test in this suite runs against a throwaway git repository built
here, with a local bare "origin" — never the real COOLBOY12 repository,
never a real network remote, and never a real HHTECH API key. Luna is
always a stub supplied by the test.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(cwd), *args], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, f"git {args} failed: {result.stderr}"
    return result.stdout


BLUEPRINT_TEXT = textwrap.dedent(
    """\
    # COOLBOY12 Master Blueprint (test fixture)

    ## 13. Record Model Definition

    Section 13 body text for testing citation extraction.

    ## 14. Something Else Entirely

    Unrelated section that must never leak into a §13 extraction.
    """
)

RMS_TEXT = textwrap.dedent(
    """\
    # COOLBOY12 Record Model System (test fixture)

    # 6. Record Model Boundaries

    Section 6 body text for testing citation extraction.

    # 7. Something Else Entirely

    Unrelated section.
    """
)

AUDIT_STANDARD_TEXT = "# audit-standard.md (test fixture)\n\nProcedure only, not architecture.\n"
PATCH_STANDARD_TEXT = "# patch-standard.md (test fixture)\n\nProcedure only, not architecture.\n"


def manifest_row(artifact_id: str, name: str, path: str, h: str = "—", bp: str = "§13", rms: str = "§6") -> str:
    return (
        f"**{artifact_id}** · {name} · `{path}` · "
        "Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · "
        "Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a · Req: BR-01 · "
        f"BP: {bp} · RMS: {rms} · H: {h} · S: — · LS: — · G: — · → 999 · "
        "Val: test validation criterion · Done: test done criterion · "
        "Why: test rationale · Risk: medium · ∥: no"
    )


ROADMAP_TEXT = "\n".join(
    [
        "# Roadmap (test fixture)",
        "",
        manifest_row("041", "Dependency artifact", "docs/target/dep.md"),
        "",
        manifest_row("042", "Target artifact", "docs/target/thing.md", h="041"),
        "",
        manifest_row("043", "Brand-new artifact", "docs/target/new.md"),
        "",
        manifest_row("044", "Glob-scoped artifact", "docs/target/multi/*.md"),
        "",
    ]
)


def make_audit_response(artifact_id: str, verdict_word: str, extra_findings: str = "(none blocking for this fixture)") -> str:
    """A minimal but contract-complete auditreport.md body, per
    audit-standard.md §14.1's section list (verdict.py._REQUIRED_SECTIONS).
    Exactly one `VERDICT: <word>` line, as the very last line.
    """
    return textwrap.dedent(
        f"""\
        # hhtech/auditreport.md

        ## Audit Identity
        Artifact {artifact_id} audit, HHTECH GPT-5.6 Luna, test fixture run.

        ## Target Artifact
        Artifact {artifact_id} — target artifact under test.

        ## Audit Mode
        Full Artifact Audit.

        ## Source Set
        Blueprint §13 (read), RMS §6 (read), Roadmap row {artifact_id} (read),
        target file content (read).

        ## Scope
        Declared Roadmap scope for artifact {artifact_id}.

        ## Executive Verdict
        The result is stated as the final line of this report.

        ## Requirement Coverage
        BR-01: covered.

        ## Findings
        {extra_findings}

        ## Evidence
        Target content matches declared scope.

        ## Regression Analysis
        No regression detected.

        ## Diff Analysis
        No unexpected files changed beyond declared scope.

        ## Unverifiable Items
        None.

        ## False-Positive Checks
        None triggered.

        ## Final Verdict
        See the terminal VERDICT line below.

        ## Re-Audit Requirements
        None beyond a normal re-run.

        VERDICT: {verdict_word}
        """
    )


def make_patch_prompt(artifact_id: str) -> str:
    return textwrap.dedent(
        f"""\
        # hhtech/patchprompt.md

        ## Task
        Resolve the confirmed findings for Artifact {artifact_id} per
        patch-standard.md.

        ## Target
        The declared Roadmap scope for artifact {artifact_id}.

        ## Findings
        AUD-{artifact_id}-01: fixture finding, P2, per the supplied audit report.

        ## Scope Boundary
        Only the files in artifact {artifact_id}'s declared scope.

        ## Validation
        Confirm the target files still match their declared Roadmap scope.
        """
    )


class LunaStub:
    """Records every call and returns queued responses in order. Raises if
    called more times than responses were queued, or an exception instance
    was queued for that call. Never makes a real network request.
    """

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


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """A throwaway git repo with a local bare 'origin' remote, on branch
    'main', containing a minimal Blueprint/RMS/Roadmap/standards fixture
    set and target artifacts 041 (dependency), 042 (normal target, exists
    on disk), 043 (declared but not yet created on disk), and 044
    (glob-scoped, multiple files).
    """
    origin = tmp_path / "origin.git"
    origin.mkdir()
    git(origin, "init", "--bare", "-b", "main")

    work = tmp_path / "work"
    work.mkdir()
    git(work, "init", "-b", "main")
    git(work, "config", "user.email", "test@example.invalid")
    git(work, "config", "user.name", "Test Runner")
    git(work, "remote", "add", "origin", str(origin))

    (work / "docs" / "sources").mkdir(parents=True)
    (work / "docs" / "sources" / "COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md").write_text(BLUEPRINT_TEXT)
    (work / "docs" / "sources" / "COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md").write_text(RMS_TEXT)
    (work / "docs" / "sources" / "COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md").write_text(ROADMAP_TEXT)

    (work / "hhtech" / "standards").mkdir(parents=True)
    (work / "hhtech" / "standards" / "audit-standard.md").write_text(AUDIT_STANDARD_TEXT)
    (work / "hhtech" / "standards" / "patch-standard.md").write_text(PATCH_STANDARD_TEXT)
    (work / "hhtech" / "auditreport.md").write_text("")
    (work / "hhtech" / "patchprompt.md").write_text("")

    (work / "docs" / "target" / "multi").mkdir(parents=True)
    (work / "docs" / "target" / "thing.md").write_text("# Target artifact content\n\nSome content.\n")
    (work / "docs" / "target" / "dep.md").write_text("# Dependency artifact content\n")
    (work / "docs" / "target" / "multi" / "a.md").write_text("# multi a\n")
    (work / "docs" / "target" / "multi" / "b.md").write_text("# multi b\n")
    # 043's docs/target/new.md is deliberately NOT created — brand-new
    # artifact with an empty diff, per BUILD spec §10.

    git(work, "add", "-A")
    git(work, "commit", "-m", "initial fixture state")
    git(work, "push", "-u", "origin", "main")

    monkeypatch.chdir(work)
    monkeypatch.setenv("HHTECH_API_KEY", "test-fixture-key-not-real")

    return work
