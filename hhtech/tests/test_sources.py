"""Source discovery and resolution.

These cover the bug class the patch exists to fix: context the repository
actually contains must be found and supplied, so a runner-side gap can never
be mistaken for an artifact defect.
"""

from __future__ import annotations

import pytest
from audit_runner.errors import InputError
from audit_runner.sources import (
    STATUS_AVAILABLE,
    STATUS_NOT_REQUIRED,
    STATUS_UNAVAILABLE,
    SourceResolver,
)


@pytest.fixture
def resolution(repo):
    return SourceResolver(repo).resolve("042")


def _by_label(resolution, label):
    return next((e for e in resolution.source_set.entries if e.label == label), None)


def _labels(resolution):
    return [e.label for e in resolution.source_set.entries]


# ---------------------------------------------------------------------------
# Always-required authority
# ---------------------------------------------------------------------------

def test_mandatory_authority_all_present(resolution):
    for label in (
        "Master Blueprint (document)",
        "Record Model System (document)",
        "Build Roadmap (document)",
        "hhtech/standards/audit-standard.md",
        "hhtech/standards/patch-standard.md",
        "CLAUDE.md (session conduct)",
        "Blueprint §10",
        "Roadmap anti-ordering register",
        "Roadmap gate register",
    ):
        entry = _by_label(resolution, label)
        assert entry is not None, f"{label} was never resolved"
        assert entry.status == STATUS_AVAILABLE, f"{label} is {entry.status}"


def test_spine_section_carries_real_text_not_just_a_label(resolution):
    spine = _by_label(resolution, "Blueprint §10")
    assert "The Spine" in spine.content
    assert "One Canon" in spine.content
    # …and stops before the next same-level section
    assert "Knowledge-State Architecture" not in spine.content


def test_anti_ordering_register_has_real_rows(resolution):
    anti = _by_label(resolution, "Roadmap anti-ordering register")
    assert "X-08" in anti.content
    assert "X-04" in anti.content


def test_documents_are_discovered_by_pattern_not_hardcoded_filename(repo):
    """Version-stamped filenames differ from the real repo's; discovery must
    still find them."""
    resolver = SourceResolver(repo)
    assert resolver.blueprint_path.name == "COOLBOY12_MASTER_BLUEPRINT_v9.9.9.md"
    assert resolver.rms_path.name == "COOLBOY12_RECORD_MODEL_SYSTEM_v9.9.md"


def test_missing_blueprint_fails_closed(repo):
    (repo / "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v9.9.9.md").unlink()
    with pytest.raises(InputError) as exc:
        SourceResolver(repo)
    assert "Master Blueprint" in str(exc.value)


def test_missing_standard_fails_closed(repo):
    (repo / "hhtech/standards/audit-standard.md").unlink()
    with pytest.raises(InputError):
        SourceResolver(repo)


def test_ambiguous_document_fails_closed(repo):
    (repo / "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v9.9.10.md").write_text("# decoy\n")
    with pytest.raises(InputError) as exc:
        SourceResolver(repo)
    assert "ambiguous" in str(exc.value)


# ---------------------------------------------------------------------------
# Declared citations and the target's own references
# ---------------------------------------------------------------------------

def test_declared_bp_and_rms_citations_resolved(resolution):
    assert _by_label(resolution, "Blueprint §13").status == STATUS_AVAILABLE
    assert _by_label(resolution, "RMS §6").status == STATUS_AVAILABLE


def test_citation_coverage_is_a_floor_not_a_ceiling(resolution):
    """§13.6 and RMS §2 are cited by the artifact's own text, not by its row."""
    assert _by_label(resolution, "Blueprint §13.6").status == STATUS_AVAILABLE
    assert _by_label(resolution, "RMS §2").status == STATUS_AVAILABLE


def test_unlocatable_section_is_reported_unavailable_not_faked(repo):
    resolution = SourceResolver(repo).resolve("042")
    # §99 does not exist; ask for it explicitly through a referenced artifact
    resolver = SourceResolver(repo)
    (repo / "docs/target/thing.md").write_text("References Blueprint §99 only.\n")
    resolution = resolver.resolve("042")
    entry = _by_label(resolution, "Blueprint §99")
    assert entry is not None
    assert entry.status == STATUS_UNAVAILABLE
    assert entry.content == ""


# ---------------------------------------------------------------------------
# Registers: invariants, anti-orderings, requirements
# ---------------------------------------------------------------------------

def test_cited_invariants_resolved_to_register_text(resolution):
    i101 = _by_label(resolution, "Invariant I-101")
    assert i101.status == STATUS_AVAILABLE
    assert "sovereign Record Model" in i101.content


def test_cited_anti_ordering_resolved_to_register_row(resolution):
    x08 = _by_label(resolution, "Anti-ordering X-08")
    assert x08.status == STATUS_AVAILABLE
    assert "World mechanism" in x08.content


def test_unknown_invariant_reported_unresolved(repo):
    (repo / "docs/target/thing.md").write_text("Cites I-999 which does not exist.\n")
    resolution = SourceResolver(repo).resolve("042")
    entry = _by_label(resolution, "Invariant I-999")
    assert entry.status == STATUS_UNAVAILABLE


def test_no_invariant_cited_is_not_required_not_unavailable(repo):
    (repo / "docs/target/thing.md").write_text("Plain content with no citations.\n")
    resolution = SourceResolver(repo).resolve("042")
    entry = _by_label(resolution, "Invariant lookup")
    assert entry.status == STATUS_NOT_REQUIRED


def test_requirement_register_gap_reported_never_invented(repo):
    resolution = SourceResolver(repo).resolve("042")
    entry = _by_label(resolution, "Requirement RR-06")
    assert entry is not None
    if entry.status == STATUS_UNAVAILABLE:
        assert "must NOT be inferred" in entry.detail
    else:
        # If the fixture Roadmap happens to mention it, the text supplied is
        # the actual line, never a paraphrase.
        assert "RR-06" in entry.content


# ---------------------------------------------------------------------------
# Dependency, reference and neighbour context
# ---------------------------------------------------------------------------

def test_h_dependency_row_and_content_loaded(resolution):
    assert _by_label(resolution, "Artifact 039 (Roadmap row)").status == STATUS_AVAILABLE
    assert _by_label(resolution, "Artifact 039 (content)").status == STATUS_AVAILABLE


def test_explicitly_referenced_artifact_is_loaded(resolution):
    """Artifact 042's row does not declare 041; its text references it. The
    old runner missed exactly this and blocked the audit for it."""
    row_entry = _by_label(resolution, "Artifact 041 (Roadmap row)")
    content_entry = _by_label(resolution, "Artifact 041 (content)")
    assert row_entry.status == STATUS_AVAILABLE
    assert content_entry.status == STATUS_AVAILABLE
    assert "Sovereignty contract" in content_entry.content
    assert "referenced" in content_entry.reason


def test_lockstep_gate_and_unlock_fields_all_handled(resolution):
    fields = {entry["field"]: entry for entry in resolution.dependency_context}
    assert set(fields) == {"H", "S", "LS", "G", "Unlocks"}
    assert fields["LS"]["artifact_ids"] == ["043"]
    assert fields["Unlocks"]["artifact_ids"] == ["040"]
    assert fields["G"]["non_artifact_tokens"] == ["G-TEST"]
    assert fields["S"]["empty"] is True


def test_previous_artifact_is_neighbour_context(resolution):
    assert _by_label(resolution, "Artifact 041 (Roadmap row)") is not None


def test_universal_conformance_artifact_loaded_generically(resolution):
    """Artifact 003's row unlocks `all`, so it is conformance context for
    every later artifact — derived from the Roadmap, never hardcoded."""
    entry = _by_label(resolution, "Artifact 003 (content)")
    assert entry.status == STATUS_AVAILABLE
    assert "RULE G" in entry.content
    assert "unlocks `all`" in entry.reason


def test_dependency_content_is_context_only_never_a_second_target(resolution):
    entry = _by_label(resolution, "Artifact 039 (content)")
    assert "CONTEXT ONLY" in entry.reason
    assert "never as a second audit target" in entry.reason


def test_missing_referenced_artifact_reported_not_invented(repo):
    (repo / "docs/target/dep041.md").unlink()
    resolution = SourceResolver(repo).resolve("042")
    entry = _by_label(resolution, "Artifact 041 (content)")
    assert entry.status == STATUS_UNAVAILABLE
    assert "does not exist" in entry.detail


def test_source_set_labels_are_stable_and_deduplicated(resolution):
    labels = _labels(resolution)
    assert len(labels) == len(set(labels))


# ---------------------------------------------------------------------------
# Source Set vs Audit Scope
# ---------------------------------------------------------------------------

def test_audit_scope_is_only_the_target(resolution):
    assert resolution.scope.artifact_id == "042"
    assert [f.path for f in resolution.scope.files] == ["docs/target/thing.md"]


def test_dependency_is_in_source_set_but_not_in_audit_scope(resolution):
    scope_paths = {f.path for f in resolution.scope.files}
    assert "docs/target/dep041.md" not in scope_paths
    assert _by_label(resolution, "Artifact 041 (content)").status == STATUS_AVAILABLE


def test_target_file_absent_is_reported_in_scope_and_source_set(repo):
    resolution = SourceResolver(repo).resolve("043")
    assert resolution.scope.missing_files == ("docs/target/new.md",)
    entry = _by_label(resolution, "TARGET docs/target/new.md")
    assert entry.status == STATUS_UNAVAILABLE
    assert "not present on disk" in entry.detail


def test_multi_file_scope_all_files_are_audit_scope(repo):
    resolution = SourceResolver(repo).resolve("044")
    assert resolution.scope.multi_file
    assert set(resolution.scope.existing_files) == {
        "docs/target/multi/a.md", "docs/target/multi/b.md"
    }
