"""Fail-closed behavior: documented exit code, no commit, no push, no
half-written output. Every HHTECH call is mocked.
"""

from __future__ import annotations

from audit_runner import outputs, pipeline
from audit_runner.errors import (
    EXIT_API_FAILURE,
    EXIT_GIT_SAFETY_FAILURE,
    EXIT_INPUT_ERROR,
    EXIT_INVALID_AUDIT_RESPONSE,
    EXIT_PATCH_GENERATION_FAILURE,
    ApiFailure,
)

from .conftest import LunaStub, git, make_audit_response, make_patch_prompt


def _head(repo):
    return git(repo, "rev-parse", "HEAD").strip()


def _outputs_untouched(repo):
    return (
        (repo / outputs.AUDIT_REPORT_REL).read_text(encoding="utf-8") == ""
        and (repo / outputs.PATCH_PROMPT_REL).read_text(encoding="utf-8") == ""
    )


def test_first_call_api_failure(repo):
    before = _head(repo)
    stub = LunaStub([ApiFailure("simulated HHTECH outage")])
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_API_FAILURE
    assert _head(repo) == before
    assert _outputs_untouched(repo)


def test_api_timeout_fails_closed(repo):
    stub = LunaStub([ApiFailure("HHTECH request timed out after 180s")])
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_API_FAILURE
    assert _outputs_untouched(repo)


def test_malformed_response_no_terminal_verdict(repo):
    before = _head(repo)
    malformed = make_audit_response("042", "PASS").replace("VERDICT: PASS", "no marker")
    assert pipeline.main(
        ["042"], luna=LunaStub([malformed]), repo_root=repo
    ) == EXIT_INVALID_AUDIT_RESPONSE
    assert _head(repo) == before
    assert _outputs_untouched(repo)


def test_malformed_response_missing_required_section(repo):
    malformed = make_audit_response("042", "PASS").replace("## False-Positive Checks\n", "")
    assert pipeline.main(
        ["042"], luna=LunaStub([malformed]), repo_root=repo
    ) == EXIT_INVALID_AUDIT_RESPONSE
    assert _outputs_untouched(repo)


def test_conflicting_verdict_markers(repo):
    malformed = make_audit_response("042", "BLOCKED").replace(
        "## Executive Verdict\n", "## Executive Verdict\nVERDICT: PASS\n"
    )
    assert pipeline.main(
        ["042"], luna=LunaStub([malformed]), repo_root=repo
    ) == EXIT_INVALID_AUDIT_RESPONSE
    assert _outputs_untouched(repo)


def test_report_for_the_wrong_artifact_rejected(repo):
    wrong = make_audit_response("099", "PASS")
    assert pipeline.main(
        ["042"], luna=LunaStub([wrong]), repo_root=repo
    ) == EXIT_INVALID_AUDIT_RESPONSE


def test_second_call_failure_leaves_report_but_never_commits(repo):
    """The audit succeeded; the patch prompt did not. Nothing is committed,
    and patchprompt.md is never left holding a partial prompt."""
    before = _head(repo)
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        ApiFailure("simulated outage on the patch-prompt call"),
    ])
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_API_FAILURE
    assert _head(repo) == before
    assert (repo / outputs.PATCH_PROMPT_REL).read_text(encoding="utf-8") == ""
    assert "VERDICT: PATCH REQUIRED" in (repo / outputs.AUDIT_REPORT_REL).read_text()


def test_malformed_patch_prompt_rejected(repo):
    before = _head(repo)
    stub = LunaStub([make_audit_response("042", "PATCH REQUIRED"), "   "])
    assert pipeline.main(
        ["042"], luna=stub, repo_root=repo
    ) == EXIT_PATCH_GENERATION_FAILURE
    assert _head(repo) == before
    assert (repo / outputs.PATCH_PROMPT_REL).read_text(encoding="utf-8") == ""


def test_patch_prompt_contradicting_verdict_rejected(repo):
    """A PASS-contract prompt returned for a PATCH REQUIRED audit."""
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        make_patch_prompt("042", "PASS"),
    ])
    assert pipeline.main(
        ["042"], luna=stub, repo_root=repo
    ) == EXIT_PATCH_GENERATION_FAILURE


def test_blocked_patch_prompt_that_tries_to_patch_is_rejected(repo):
    import re

    unsafe = re.sub(
        r"do not patch", "patch", make_patch_prompt("042", "BLOCKED"), flags=re.IGNORECASE
    )
    stub = LunaStub([make_audit_response("042", "BLOCKED"), unsafe])
    assert pipeline.main(
        ["042"], luna=stub, repo_root=repo
    ) == EXIT_PATCH_GENERATION_FAILURE


def test_patch_prompt_referencing_patchreport_rejected(repo):
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        make_patch_prompt("042", "PATCH REQUIRED") + "\nWrite hhtech/patchreport.md.\n",
    ])
    assert pipeline.main(
        ["042"], luna=stub, repo_root=repo
    ) == EXIT_PATCH_GENERATION_FAILURE


def test_patch_prompt_editing_architecture_rejected(repo):
    stub = LunaStub([
        make_audit_response("042", "PATCH REQUIRED"),
        make_patch_prompt("042", "PATCH REQUIRED")
        + "\nUpdate the Blueprint so this audit passes.\n",
    ])
    assert pipeline.main(
        ["042"], luna=stub, repo_root=repo
    ) == EXIT_PATCH_GENERATION_FAILURE


def test_unknown_artifact_is_an_input_error(repo):
    assert pipeline.main(["099"], luna=LunaStub([]), repo_root=repo) == EXIT_INPUT_ERROR


def test_missing_api_key_fails_before_any_call(repo, monkeypatch):
    monkeypatch.delenv("HHTECH_API_KEY", raising=False)
    stub = LunaStub([])
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_INPUT_ERROR
    assert stub.calls == []


def test_missing_roadmap_fails_closed(repo):
    (repo / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md").unlink()
    stub = LunaStub([])
    assert pipeline.main(["042"], luna=stub, repo_root=repo) == EXIT_INPUT_ERROR
    assert stub.calls == []


def test_preexisting_unrelated_staged_file_aborts_before_any_call(repo):
    (repo / "src_change.py").write_text("X = 1\n")
    git(repo, "add", "src_change.py")

    stub = LunaStub([])
    assert pipeline.main(
        ["042"], luna=stub, repo_root=repo
    ) == EXIT_GIT_SAFETY_FAILURE
    assert stub.calls == [], "no paid call may be spent on a run that cannot commit"
    # the user's staged work is still staged, untouched
    assert "src_change.py" in git(repo, "diff", "--cached", "--name-only")
