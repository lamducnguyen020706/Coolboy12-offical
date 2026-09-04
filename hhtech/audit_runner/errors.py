"""Exit codes and exception types for the audit runner.

Exit codes are part of the runner's contract (BUILD spec §33) and are
depended on by tests and by the /audit command wrapper.
"""

from __future__ import annotations

EXIT_SUCCESS = 0
EXIT_INPUT_ERROR = 1
EXIT_API_FAILURE = 2
EXIT_INVALID_AUDIT_RESPONSE = 3
EXIT_PATCH_GENERATION_FAILURE = 4
EXIT_GIT_SAFETY_FAILURE = 5


class RunnerError(Exception):
    """Base class for a runner failure that maps to a specific exit code."""

    exit_code = EXIT_INPUT_ERROR


class InputError(RunnerError):
    exit_code = EXIT_INPUT_ERROR


class ApiFailure(RunnerError):
    exit_code = EXIT_API_FAILURE


class InvalidAuditResponse(RunnerError):
    exit_code = EXIT_INVALID_AUDIT_RESPONSE


class PatchGenerationFailure(RunnerError):
    exit_code = EXIT_PATCH_GENERATION_FAILURE


class GitSafetyFailure(RunnerError):
    exit_code = EXIT_GIT_SAFETY_FAILURE
