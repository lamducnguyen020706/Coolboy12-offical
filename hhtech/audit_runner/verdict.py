"""Verdict extraction and audit-response shape validation.

BUILD spec §16: exactly one machine-detectable verdict marker, never
guessed, never invented by the runner. Fail closed on anything else.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .errors import InvalidAuditResponse

VALID_VERDICTS = ("PASS", "PATCH REQUIRED", "BLOCKED")

_VERDICT_LINE = re.compile(
    r"^VERDICT:\s*(PASS|PATCH REQUIRED|BLOCKED)\s*$", re.MULTILINE
)

_REQUIRED_SECTIONS = (
    "Audit Identity",
    "Target Artifact",
    "Audit Mode",
    "Source Set",
    "Scope",
    "Executive Verdict",
    "Requirement Coverage",
    "Findings",
    "Evidence",
    "Regression Analysis",
    "Unverifiable Items",
)


@dataclass(frozen=True)
class AuditResult:
    text: str
    verdict: str


def extract_verdict(response_text: str, api_key: str = "") -> AuditResult:
    """Extract exactly one verdict marker. Raise InvalidAuditResponse
    otherwise — the runner never guesses and never falls back to a default.
    """
    if api_key and api_key in response_text:
        raise InvalidAuditResponse(
            "audit response contains the HHTECH API key; refusing to write it"
        )

    matches = _VERDICT_LINE.findall(response_text)
    if len(matches) == 0:
        raise InvalidAuditResponse(
            "audit response contains no `VERDICT: PASS|PATCH REQUIRED|BLOCKED` line"
        )
    if len(matches) > 1:
        distinct = set(matches)
        if len(distinct) > 1:
            raise InvalidAuditResponse(
                f"audit response contains conflicting verdict lines: {sorted(distinct)}"
            )
        raise InvalidAuditResponse(
            "audit response contains more than one verdict line "
            "(even though they agree) — exactly one is required"
        )

    verdict = matches[0]

    missing_sections = [s for s in _REQUIRED_SECTIONS if s not in response_text]
    if missing_sections:
        raise InvalidAuditResponse(
            f"audit response is missing required report sections: {missing_sections}"
        )

    return AuditResult(text=response_text, verdict=verdict)


def validate_artifact_identity(response_text: str, artifact_id: str) -> None:
    if artifact_id not in response_text:
        raise InvalidAuditResponse(
            f"audit response never mentions artifact {artifact_id}; "
            "refusing to accept it as this artifact's audit"
        )
