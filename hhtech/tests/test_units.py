"""Unit tests for individual audit_runner modules — no repo, no network."""

from __future__ import annotations

import pytest

from audit_runner import artifact_id, patchcheck, verdict
from audit_runner.errors import InputError, InvalidAuditResponse, PatchGenerationFailure
from audit_runner.roadmap import derive_target_scope, find_manifest_row, parse_citation_numbers

from .conftest import ROADMAP_TEXT, make_audit_response, make_patch_prompt


# ---------------------------------------------------------------------------
# artifact_id
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("raw,expected", [("1", "001"), ("42", "042"), ("042", "042"), ("490", "490")])
def test_normalize_artifact_id_valid(raw, expected):
    assert artifact_id.normalize_artifact_id(raw) == expected


@pytest.mark.parametrize("raw", ["0", "491", "foo", "", "   ", "42abc", "-1", "+1", "4 2"])
def test_normalize_artifact_id_invalid(raw):
    with pytest.raises(InputError):
        artifact_id.normalize_artifact_id(raw)


def test_parse_single_argument_no_args():
    with pytest.raises(InputError):
        artifact_id.parse_single_argument([])


def test_parse_single_argument_too_many_args():
    with pytest.raises(InputError):
        artifact_id.parse_single_argument(["42", "extra"])


def test_parse_single_argument_ok():
    assert artifact_id.parse_single_argument(["42"]) == "042"


# ---------------------------------------------------------------------------
# roadmap: manifest lookup, citation parsing, target scope
# ---------------------------------------------------------------------------

def test_find_manifest_row_ok():
    row = find_manifest_row(ROADMAP_TEXT, "042")
    assert row.id == "042"
    assert row.name == "Target artifact"
    assert row.path == "docs/target/thing.md"
    assert row.get("H") == "041"


def test_find_manifest_row_missing():
    with pytest.raises(InputError):
        find_manifest_row(ROADMAP_TEXT, "999")


@pytest.mark.parametrize(
    "citation,expected",
    [("§13", ["13"]), ("n/a", []), ("—", []), ("§13.7a", ["13.7a"]), ("§2, §3", ["2", "3"])],
)
def test_parse_citation_numbers(citation, expected):
    assert parse_citation_numbers(citation) == expected


def test_derive_target_scope_literal_file(repo):
    row = find_manifest_row(ROADMAP_TEXT, "042")
    scope = derive_target_scope(repo, row)
    assert scope.matched_files == ("docs/target/thing.md",)
    assert not scope.is_glob
    assert not scope.is_directory


def test_derive_target_scope_literal_path_kept_even_when_file_missing(repo):
    """A brand-new artifact's declared literal path stays in scope even
    though the file does not exist on disk yet — non-existence is reported
    by sources.collect_sources' target_files map, not by shrinking scope to
    nothing (BUILD spec §10's empty-diff-for-new-artifact case)."""
    row = find_manifest_row(ROADMAP_TEXT, "043")
    scope = derive_target_scope(repo, row)
    assert scope.matched_files == ("docs/target/new.md",)


def test_derive_target_scope_glob_multi_file(repo):
    row = find_manifest_row(ROADMAP_TEXT, "044")
    scope = derive_target_scope(repo, row)
    assert set(scope.matched_files) == {"docs/target/multi/a.md", "docs/target/multi/b.md"}
    assert scope.is_glob


# ---------------------------------------------------------------------------
# verdict extraction — fail-closed behavior
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word", ["PASS", "PATCH REQUIRED", "BLOCKED"])
def test_extract_verdict_valid(word):
    text = make_audit_response("042", word)
    result = verdict.extract_verdict(text)
    assert result.verdict == word


def test_extract_verdict_no_marker():
    text = make_audit_response("042", "PASS").replace("VERDICT: PASS", "no marker here")
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_conflicting_markers():
    text = make_audit_response("042", "PASS") + "\nVERDICT: BLOCKED\n"
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_duplicate_agreeing_markers():
    text = make_audit_response("042", "PASS") + "\nVERDICT: PASS\n"
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_missing_required_section():
    text = make_audit_response("042", "PASS").replace("## Findings\n", "")
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_rejects_embedded_api_key():
    text = make_audit_response("042", "PASS").replace(
        "## Audit Identity\n", "## Audit Identity\nLeaked key: test-fixture-key-not-real\n"
    )
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text, api_key="test-fixture-key-not-real")


def test_validate_artifact_identity_missing():
    text = make_audit_response("042", "PASS").replace("042", "999")
    with pytest.raises(InvalidAuditResponse):
        verdict.validate_artifact_identity(text, "042")


# ---------------------------------------------------------------------------
# patchcheck
# ---------------------------------------------------------------------------

def test_validate_patch_prompt_ok():
    patchcheck.validate_patch_prompt(make_patch_prompt("042"), "042")


def test_validate_patch_prompt_empty():
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt("   ", "042")


def test_validate_patch_prompt_forbidden_patchreport_reference():
    text = make_patch_prompt("042") + "\nSee hhtech/patchreport.md for details.\n"
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042")


def test_validate_patch_prompt_forbidden_api_key_token():
    text = make_patch_prompt("042") + "\nExport HHTECH_API_KEY before running.\n"
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042")


def test_validate_patch_prompt_rejects_embedded_api_key_value():
    text = make_patch_prompt("042").replace(
        "## Task\n", "## Task\nLeaked key: test-fixture-key-not-real\n"
    )
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042", api_key="test-fixture-key-not-real")


def test_validate_patch_prompt_missing_artifact_mention():
    text = make_patch_prompt("042").replace("042", "999")
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042")
