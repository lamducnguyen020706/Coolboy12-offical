"""Acceptance case: Artifact 042 against the REAL repository content.

Artifact 042 is the acceptance example, not the architecture: nothing here
is special-cased in the runner. The resolver reaches 039, 041, 003, the
Spine, the invariant registers and the anti-orderings purely from the
Roadmap row, the artifact's own references, and the audit-standard's
mandatory context.

The context tests are read-only against the real checkout. The end-to-end
test runs against a throwaway clone whose `origin` is a local bare repo, so
no test can ever push to the real remote, and Luna is always mocked.
"""

from __future__ import annotations

import subprocess

import pytest
from audit_runner import outputs, pipeline
from audit_runner.errors import EXIT_SUCCESS
from audit_runner.sources import STATUS_AVAILABLE, SourceResolver

from .conftest import REAL_REPO_ROOT, git, verdict_stub

ARTIFACT = "042"


@pytest.fixture(scope="module")
def real_resolution():
    """Read-only resolution against the real repository. Mutates nothing."""
    return SourceResolver(REAL_REPO_ROOT).resolve(ARTIFACT)


def _entry(resolution, label):
    return next((e for e in resolution.source_set.entries if e.label == label), None)


def _available(resolution, label):
    entry = _entry(resolution, label)
    assert entry is not None, f"{label} was never resolved"
    assert entry.status == STATUS_AVAILABLE, f"{label} is {entry.status}: {entry.detail}"
    return entry


# ---------------------------------------------------------------------------
# Context discovery — the bug class this patch fixes
# ---------------------------------------------------------------------------

def test_target_and_scope_resolved_from_the_real_roadmap(real_resolution):
    assert real_resolution.row.id == ARTIFACT
    assert real_resolution.row.name == "Record Model definition"
    assert real_resolution.scope.declared_path == "docs/constitution/record_model.md"
    assert real_resolution.scope.existing_files == ("docs/constitution/record_model.md",)


def test_hard_dependency_039_is_loaded(real_resolution):
    """042's row declares H: 039."""
    _available(real_resolution, "Artifact 039 (Roadmap row)")
    content = _available(real_resolution, "Artifact 039 (content)")
    assert "Record System" in content.content


def test_referenced_artifact_041_is_loaded(real_resolution):
    """041 is NOT on 042's dependency fields — the artifact's own text cites
    it. The previous runner missed exactly this and blocked the audit for a
    source the repository already contained."""
    _available(real_resolution, "Artifact 041 (Roadmap row)")
    content = _available(real_resolution, "Artifact 041 (content)")
    assert content.content.strip(), "041 was resolved but supplied empty"
    assert "041" in real_resolution.references.artifacts


def test_artifact_003_conventions_loaded_as_conformance_context(real_resolution):
    entry = _available(real_resolution, "Artifact 003 (content)")
    assert "docs/conventions/artifact_conventions.md" == entry.path
    assert "unlocks `all`" in entry.reason, "003 must arrive generically, not hardcoded"


def test_spine_section_10_supplied_as_real_text(real_resolution):
    spine = _available(real_resolution, "Blueprint §10")
    assert "The Spine" in spine.content
    assert "One Canon" in spine.content
    assert "Nothing Bypasses the Composer" in spine.content
    assert "Universe Architecture" not in spine.content  # stops at §11


def test_cited_invariants_resolved_to_register_rows(real_resolution):
    for invariant in ("I-101", "I-104", "I-105", "I-87"):
        entry = _available(real_resolution, f"Invariant {invariant}")
        assert invariant in entry.content
        assert len(entry.content) > len(invariant) + 10, "only the label was supplied"


def test_anti_ordering_register_available(real_resolution):
    register = _available(real_resolution, "Roadmap anti-ordering register")
    assert "X-01" in register.content and "X-22" in register.content


def test_gate_register_available(real_resolution):
    _available(real_resolution, "Roadmap gate register")


def test_declared_and_referenced_sections_both_resolved(real_resolution):
    _available(real_resolution, "Blueprint §13")   # declared BP citation
    _available(real_resolution, "RMS §6")          # declared RMS citation
    _available(real_resolution, "Blueprint §13.7a")  # referenced by the artifact
    _available(real_resolution, "RMS §2")            # referenced by the artifact


def test_requirement_rr06_state_is_reported_not_invented(real_resolution):
    entry = _entry(real_resolution, "Requirement RR-06")
    assert entry is not None
    if entry.status != STATUS_AVAILABLE:
        assert "must NOT be inferred" in entry.detail
    else:
        assert "RR-06" in entry.content


def test_standards_and_claude_md_supplied(real_resolution):
    _available(real_resolution, "hhtech/standards/audit-standard.md")
    _available(real_resolution, "hhtech/standards/patch-standard.md")
    _available(real_resolution, "CLAUDE.md (session conduct)")


def test_dependency_artifacts_are_not_in_the_audit_scope(real_resolution):
    scope_paths = {f.path for f in real_resolution.scope.files}
    assert scope_paths == {"docs/constitution/record_model.md"}
    assert "docs/constitution/sovereignty.md" not in scope_paths


def test_context_is_bounded_not_the_whole_repository(real_resolution):
    """Bounded context, not a repository dump."""
    loaded_artifacts = [
        e for e in real_resolution.source_set.entries
        if e.label.endswith("(content)") and e.status == STATUS_AVAILABLE
    ]
    assert 1 <= len(loaded_artifacts) <= 10, (
        f"{len(loaded_artifacts)} artifact bodies loaded — context is unbounded"
    )


def test_no_artifact_id_branching_in_the_runner():
    """No control flow anywhere in the runner keys off a specific artifact ID.

    Documentation examples ("**042** · Record Model definition …" in a
    docstring) are fine; a comparison against an ID literal is not.
    """
    import re

    branching = re.compile(r"""(?:[=!]=\s*["']\d{3}["']|\bin\s*[\(\[]?\s*["']\d{3}["'])""")
    runner_dir = REAL_REPO_ROOT / "hhtech" / "audit_runner"
    for source_file in runner_dir.glob("*.py"):
        for lineno, line in enumerate(source_file.read_text().splitlines(), start=1):
            assert not branching.search(line), (
                f"{source_file.name}:{lineno} branches on an artifact ID: {line.strip()!r}"
            )


# ---------------------------------------------------------------------------
# End-to-end against a throwaway clone of the real repository
# ---------------------------------------------------------------------------

@pytest.fixture
def real_clone(tmp_path, monkeypatch):
    """A shallow clone of the real repository whose origin is a local bare
    repo — pushing here can never reach the real remote."""
    origin = tmp_path / "origin.git"
    origin.mkdir()
    git(origin, "init", "--bare", "-b", "main")

    work = tmp_path / "work"
    subprocess.run(
        ["git", "clone", "--depth", "1", "--quiet", str(REAL_REPO_ROOT), str(work)],
        check=True, capture_output=True, timeout=180,
    )
    git(work, "config", "user.email", "test@example.invalid")
    git(work, "config", "user.name", "Test Runner")
    git(work, "remote", "set-url", "origin", str(origin))
    # A --depth 1 clone restricts its fetch refspec to the cloned branch, so
    # remote-tracking refs for any other branch are never created. Restore
    # the wildcard so `origin/main` exists to assert against.
    git(work, "config", "remote.origin.fetch", "+refs/heads/*:refs/remotes/origin/*")
    git(work, "checkout", "-B", "main")
    git(work, "push", "-u", "origin", "main")

    monkeypatch.setenv("HHTECH_API_KEY", "test-fixture-key-not-real")
    monkeypatch.chdir(tmp_path)
    return work


@pytest.mark.parametrize("word", ["PASS", "PATCH REQUIRED", "BLOCKED"])
def test_end_to_end_042_on_real_content(real_clone, word):
    stub = verdict_stub(ARTIFACT, word)
    assert pipeline.main([ARTIFACT], luna=stub, repo_root=real_clone) == EXIT_SUCCESS

    report = (real_clone / outputs.AUDIT_REPORT_REL).read_text(encoding="utf-8")
    patch = (real_clone / outputs.PATCH_PROMPT_REL).read_text(encoding="utf-8")
    assert f"VERDICT: {word}" in report
    assert patch.strip(), "every verdict must leave a fresh patchprompt"

    committed = {
        line for line in
        git(real_clone, "show", "--name-only", "--pretty=", "HEAD").splitlines() if line
    }
    assert committed == {"hhtech/auditreport.md", "hhtech/patchprompt.md"}
    assert git(real_clone, "rev-parse", "HEAD").strip() == git(
        real_clone, "rev-parse", "origin/main"
    ).strip()


def test_end_to_end_042_supplies_real_context_to_the_model(real_clone):
    stub = verdict_stub(ARTIFACT, "PASS")
    pipeline.main([ARTIFACT], luna=stub, repo_root=real_clone)
    _system, user_content = stub.calls[0]

    assert "SOURCE: Artifact 041 (content)" in user_content
    assert "SOURCE: Artifact 039 (content)" in user_content
    assert "SOURCE: Blueprint §10" in user_content
    assert "SOURCE: Invariant I-101" in user_content
    assert "SOURCE: Roadmap anti-ordering register" in user_content
    assert "docs/constitution/record_model.md" in user_content
