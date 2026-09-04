"""Fail-closed behavior: every failure mode must produce the documented
exit code, must never commit, and must never push. No real network call.
"""

from __future__ import annotations

from audit_runner import outputs, pipeline
from audit_runner.errors import (
    EXIT_API_FAILURE,
    EXIT_INVALID_AUDIT_RESPONSE,
    EXIT_PATCH_GENERATION_FAILURE,
)
from audit_runner.errors import ApiFailure

from .conftest import LunaStub, git, make_audit_response, make_patch_prompt


def _head(work) -> str:
    return git(work, "rev-parse", "HEAD").strip()


def test_malformed_audit_response_no_verdict_line(repo):
    before = _head(repo)
    malformed = make_audit_response("042", "PASS").replace("VERDICT: PASS", "no marker at all")
    stub = LunaStub([malformed])

    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_INVALID_AUDIT_RESPONSE
    assert _head(repo) == before  # no commit happened
    # the pre-existing (empty) output files must not have been overwritten
    # with a malformed report
    assert (repo / "hhtech" / outputs.AUDIT_REPORT_NAME).read_text(encoding="utf-8") == ""


def test_malformed_audit_response_two_conflicting_verdicts(repo):
    before = _head(repo)
    malformed = make_audit_response("042", "PASS") + "\nVERDICT: BLOCKED\n"
    stub = LunaStub([malformed])

    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_INVALID_AUDIT_RESPONSE
    assert _head(repo) == before


def test_first_call_api_failure(repo):
    before = _head(repo)
    stub = LunaStub([ApiFailure("simulated HHTECH outage")])

    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_API_FAILURE
    assert _head(repo) == before
    assert (repo / "hhtech" / outputs.AUDIT_REPORT_NAME).read_text(encoding="utf-8") == ""
    assert (repo / "hhtech" / outputs.PATCH_PROMPT_NAME).read_text(encoding="utf-8") == ""


def test_second_call_api_failure_leaves_valid_report_but_no_commit(repo):
    before = _head(repo)
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        ApiFailure("simulated HHTECH outage on the patch-prompt call"),
    ])

    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_API_FAILURE
    assert _head(repo) == before  # no commit, no push despite a valid first-call result

    # patchprompt.md must not contain a partial/malformed prompt — it was
    # never touched by this failed run
    patch_content = (repo / "hhtech" / outputs.PATCH_PROMPT_NAME).read_text(encoding="utf-8")
    assert patch_content == ""


def test_second_call_malformed_patch_prompt(repo):
    before = _head(repo)
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        "   ",  # empty/whitespace-only response — fails patchcheck
    ])

    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_PATCH_GENERATION_FAILURE
    assert _head(repo) == before
    patch_content = (repo / "hhtech" / outputs.PATCH_PROMPT_NAME).read_text(encoding="utf-8")
    assert patch_content == ""


def test_patch_prompt_forbidden_reference_fails_closed(repo):
    before = _head(repo)
    bad_patch = make_patch_prompt("042") + "\nAlso update hhtech/patchreport.md.\n"
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        bad_patch,
    ])

    exit_code = pipeline.main(["042"], luna=stub)

    assert exit_code == EXIT_PATCH_GENERATION_FAILURE
    assert _head(repo) == before


def test_missing_artifact_in_roadmap(repo):
    stub = LunaStub([])
    exit_code = pipeline.main(["099"], luna=stub)
    assert exit_code != 0
    assert stub.calls == []  # never even reached HHTECH
