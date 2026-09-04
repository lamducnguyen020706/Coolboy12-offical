"""Unit tests: artifact ID, Roadmap parsing/scope, references, verdict, patchcheck."""

from __future__ import annotations

import pytest
from audit_runner import artifact_id, patchcheck, references, verdict
from audit_runner.errors import InputError, InvalidAuditResponse, PatchGenerationFailure
from audit_runner.roadmap import (
    SCOPE_DIRECTORY,
    SCOPE_FILE,
    SCOPE_GLOB,
    derive_target_scope,
    find_manifest_row,
    parse_all_rows,
    parse_artifact_references,
    parse_citation_numbers,
    parse_requirement_ids,
    previous_artifact_id,
)

from .conftest import (
    ROADMAP_TEXT,
    TARGET_042_TEXT,
    make_audit_response,
    make_patch_prompt,
)

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
# Roadmap parsing
# ---------------------------------------------------------------------------

def test_find_manifest_row_all_fields():
    row = find_manifest_row(ROADMAP_TEXT, "042")
    assert row.id == "042"
    assert row.name == "Target artifact"
    assert row.path == "docs/target/thing.md"
    assert row.get("H") == "039"
    assert row.get("LS") == "043"
    assert row.get("G") == "G-TEST"
    assert row.get("Unlocks") == "040"
    assert row.get("Req") == "RR-06"


def test_find_manifest_row_missing_fails_closed():
    with pytest.raises(InputError):
        find_manifest_row(ROADMAP_TEXT, "999")


def test_find_manifest_row_malformed_fails_closed():
    broken = "**046** · Malformed-row artifact · `docs/target/broken.md` · Own: CONST\n"
    with pytest.raises(InputError):
        find_manifest_row(broken, "046")


def test_parse_all_rows_skips_malformed_without_breaking_others():
    text = ROADMAP_TEXT + "\n**470** · broken row with no fields\n"
    rows = parse_all_rows(text)
    assert "042" in rows and "041" in rows
    assert "470" not in rows


def test_previous_artifact_id():
    assert previous_artifact_id("042") == "041"
    assert previous_artifact_id("001") is None


@pytest.mark.parametrize(
    "citation,expected",
    [("§13", ["13"]), ("n/a", []), ("—", []), ("§13.7a", ["13.7a"]), ("§§2,6", ["2", "6"])],
)
def test_parse_citation_numbers(citation, expected):
    assert parse_citation_numbers(citation) == expected


def test_parse_requirement_ids():
    assert parse_requirement_ids("BR-17,RR-01") == ["BR-17", "RR-01"]
    assert parse_requirement_ids("—") == []


def test_parse_artifact_references_ranges_and_words():
    ids, words = parse_artifact_references("040–059")
    assert ids == ["040", "059"]  # endpoints, not fifty expanded IDs
    assert words == []

    ids, words = parse_artifact_references("PART IX")
    assert ids == []
    assert words == ["PART IX"]

    ids, words = parse_artifact_references("all models")
    assert ids == []
    assert words == ["all models"]

    assert parse_artifact_references("—") == ([], [])


# ---------------------------------------------------------------------------
# Scope resolution
# ---------------------------------------------------------------------------

def test_scope_single_file(repo):
    scope = derive_target_scope(repo, find_manifest_row(ROADMAP_TEXT, "042"))
    assert scope.kind == SCOPE_FILE
    assert scope.matched_files == ("docs/target/thing.md",)
    assert not scope.multi_file


def test_scope_literal_path_kept_when_file_absent(repo):
    """A declared-but-unbuilt artifact still owns its declared path."""
    scope = derive_target_scope(repo, find_manifest_row(ROADMAP_TEXT, "043"))
    assert scope.matched_files == ("docs/target/new.md",)


def test_scope_glob_multi_file(repo):
    scope = derive_target_scope(repo, find_manifest_row(ROADMAP_TEXT, "044"))
    assert scope.kind == SCOPE_GLOB
    assert set(scope.matched_files) == {"docs/target/multi/a.md", "docs/target/multi/b.md"}
    assert scope.multi_file


def test_scope_directory(repo):
    scope = derive_target_scope(repo, find_manifest_row(ROADMAP_TEXT, "045"))
    assert scope.kind == SCOPE_DIRECTORY
    assert set(scope.matched_files) == {"docs/target/dir/one.md", "docs/target/dir/two.md"}
    assert scope.multi_file  # RULE G3: many files, one artifact


def test_scope_unresolvable_path_fails_closed(repo):
    row = find_manifest_row(ROADMAP_TEXT, "042")
    empty = type(row)(id=row.id, name=row.name, path="—", fields=row.fields, raw=row.raw)
    with pytest.raises(InputError):
        derive_target_scope(repo, empty)


# ---------------------------------------------------------------------------
# Reference extraction
# ---------------------------------------------------------------------------

def test_extract_references_from_target_text():
    refs = references.extract_references(TARGET_042_TEXT)
    assert "041" in refs.artifacts
    assert "039" in refs.artifacts
    assert "I-101" in refs.invariants and "I-104" in refs.invariants
    assert "X-08" in refs.anti_orderings
    assert "RR-06" in refs.requirements
    assert "13.6" in refs.blueprint_sections
    assert "2" in refs.rms_sections


def test_rms_citation_not_misattributed_to_blueprint():
    refs = references.extract_references("RMS §6 governs this.")
    assert refs.rms_sections == ["6"]
    assert refs.blueprint_sections == []


def test_invariants_and_anti_orderings_are_not_requirements():
    refs = references.extract_references("I-101 and X-08 and RR-06 and BR-17")
    assert refs.requirements == ["RR-06", "BR-17"]


def test_reference_extraction_deduplicates():
    refs = references.extract_references("Artifact 041 Artifact 041 I-101 I-101")
    assert refs.artifacts == ["041"]
    assert refs.invariants == ["I-101"]


# ---------------------------------------------------------------------------
# Verdict extraction — terminal-line determinism
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word", ["PASS", "PATCH REQUIRED", "BLOCKED"])
def test_extract_verdict_valid(word):
    assert verdict.extract_verdict(make_audit_response("042", word)).verdict == word


def test_extract_verdict_requires_all_fifteen_sections():
    text = make_audit_response("042", "PASS").replace("## Diff Analysis\n", "")
    with pytest.raises(InvalidAuditResponse) as exc:
        verdict.extract_verdict(text)
    assert "Diff Analysis" in str(exc.value)


def test_extract_verdict_no_marker():
    text = make_audit_response("042", "PASS").replace("VERDICT: PASS", "no marker here")
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_earlier_bare_marker_is_ambiguous():
    """An earlier prose line reading `VERDICT: PASS` must never be mistaken
    for the terminal verdict — two machine-readable markers fail closed."""
    text = make_audit_response("042", "BLOCKED").replace(
        "## Executive Verdict\n", "## Executive Verdict\nVERDICT: PASS\n"
    )
    with pytest.raises(InvalidAuditResponse) as exc:
        verdict.extract_verdict(text)
    assert "ambiguous" in str(exc.value) or "bare verdict" in str(exc.value)


def test_extract_verdict_trailing_text_after_marker_rejected():
    text = make_audit_response("042", "PASS") + "\nSome trailing commentary.\n"
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_unknown_value_rejected():
    text = make_audit_response("042", "PASS").replace("VERDICT: PASS", "VERDICT: MAYBE")
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text)


def test_extract_verdict_rejects_embedded_api_key():
    text = make_audit_response("042", "PASS").replace(
        "## Audit Identity\n", "## Audit Identity\nLeaked: test-fixture-key-not-real\n"
    )
    with pytest.raises(InvalidAuditResponse):
        verdict.extract_verdict(text, api_key="test-fixture-key-not-real")


def test_validate_artifact_identity_missing():
    text = make_audit_response("042", "PASS").replace("042", "999")
    with pytest.raises(InvalidAuditResponse):
        verdict.validate_artifact_identity(text, "042")


# ---------------------------------------------------------------------------
# Patch prompt validation
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word", ["PASS", "PATCH REQUIRED", "BLOCKED"])
def test_validate_patch_prompt_accepts_matching_contract(word):
    patchcheck.validate_patch_prompt(make_patch_prompt("042", word), "042", word)


def test_patch_prompt_empty_rejected():
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt("   ", "042", "PASS")


def test_patch_prompt_too_short_rejected():
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt("NO PATCH REQUIRED 042", "042", "PASS")


def test_patch_prompt_forbidden_patchreport_reference():
    text = make_patch_prompt("042", "PASS") + "\nWrite hhtech/patchreport.md too.\n"
    with pytest.raises(PatchGenerationFailure) as exc:
        patchcheck.validate_patch_prompt(text, "042", "PASS")
    assert "patchreport.md" in str(exc.value)


def test_patch_prompt_rejects_embedded_api_key():
    text = make_patch_prompt("042", "PASS").replace(
        "## Task\n", "## Task\nkey: test-fixture-key-not-real\n"
    )
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042", "PASS", api_key="test-fixture-key-not-real")


def test_patch_prompt_missing_artifact_mention():
    text = make_patch_prompt("042", "PASS").replace("042", "999")
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042", "PASS")


def test_patch_prompt_rejects_architecture_modification():
    text = make_patch_prompt("042", "PATCH REQUIRED") + (
        "\nAlso update the Roadmap so the audit passes.\n"
    )
    with pytest.raises(PatchGenerationFailure) as exc:
        patchcheck.validate_patch_prompt(text, "042", "PATCH REQUIRED")
    assert "authority source" in str(exc.value)


def test_patch_prompt_allows_forbidding_authority_edits():
    """"Do not modify the Blueprint" is the required instruction, not a violation."""
    patchcheck.validate_patch_prompt(
        make_patch_prompt("042", "PATCH REQUIRED"), "042", "PATCH REQUIRED"
    )


def test_patch_prompt_verdict_mismatch_pass_contract_on_patch_required():
    text = make_patch_prompt("042", "PASS")
    with pytest.raises(PatchGenerationFailure) as exc:
        patchcheck.validate_patch_prompt(text, "042", "PATCH REQUIRED")
    assert "contradicts" in str(exc.value)


def test_patch_prompt_verdict_mismatch_patch_contract_on_pass():
    text = make_patch_prompt("042", "PATCH REQUIRED")
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042", "PASS")


def test_patch_prompt_blocked_must_not_claim_no_patch_required():
    text = make_patch_prompt("042", "BLOCKED").replace(
        "## Blocking reason", "NO PATCH REQUIRED\n\n## Blocking reason"
    )
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042", "BLOCKED")


def test_patch_prompt_blocked_without_do_not_patch_rejected():
    import re as _re

    text = _re.sub(
        r"[Dd]o not patch", "Consider patching",
        make_patch_prompt("042", "BLOCKED"), flags=_re.IGNORECASE,
    )
    assert "DO NOT PATCH" not in text.upper()
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(text, "042", "BLOCKED")


def test_patch_prompt_unknown_verdict_rejected():
    with pytest.raises(PatchGenerationFailure):
        patchcheck.validate_patch_prompt(make_patch_prompt("042", "PASS"), "042", "MAYBE")
