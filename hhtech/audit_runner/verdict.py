"""Audit response validation and terminal-verdict extraction.

The verdict is read from the report's TERMINAL line, deterministically. An
earlier line that happens to read `VERDICT: PASS` is a duplicate marker, not
a verdict, and is rejected rather than guessed at — a report that states two
machine-readable verdicts is ambiguous, and ambiguity fails closed.

Validation here is contract shape only: section presence, verdict form, no
leaked credential. It never judges the audit's substance — that is Luna's
job under audit-standard.md, and the runner is not the auditor.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .errors import InvalidAuditResponse

VALID_VERDICTS = ("PASS", "PATCH REQUIRED", "BLOCKED")

_VERDICT_LINE = re.compile(r"^VERDICT:\s*(.+?)\s*$", re.MULTILINE)

# audit-standard.md §14.1, all fifteen sections, in order.
REQUIRED_SECTIONS = (
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
    "Diff Analysis",
    "Unverifiable Items",
    "False-Positive Checks",
    "Final Verdict",
    "Re-Audit Requirements",
)


@dataclass(frozen=True)
class AuditResult:
    text: str
    verdict: str


def _terminal_line(text: str) -> str:
    for line in reversed(text.splitlines()):
        if line.strip():
            return line.strip()
    return ""


def extract_verdict(response_text: str, api_key: str = "") -> AuditResult:
    """Extract the single terminal verdict, or fail closed."""
    if not response_text or not response_text.strip():
        raise InvalidAuditResponse("audit response was empty")

    if api_key and api_key in response_text:
        raise InvalidAuditResponse(
            "audit response contains the HHTECH API key; refusing to write it"
        )

    markers = _VERDICT_LINE.findall(response_text)
    if not markers:
        raise InvalidAuditResponse(
            "audit response contains no terminal `VERDICT: PASS|PATCH REQUIRED|BLOCKED` line"
        )

    terminal = _terminal_line(response_text)
    terminal_match = re.fullmatch(r"VERDICT:\s*(.+?)\s*", terminal)
    if terminal_match is None:
        raise InvalidAuditResponse(
            "the audit report's final line is not the terminal verdict marker "
            f"(final line was {terminal[:120]!r}); refusing to infer a verdict "
            "from an earlier occurrence"
        )

    verdict = terminal_match.group(1).strip()
    if verdict not in VALID_VERDICTS:
        raise InvalidAuditResponse(
            f"terminal verdict {verdict!r} is not one of {list(VALID_VERDICTS)}"
        )

    if len(markers) > 1:
        raise InvalidAuditResponse(
            f"audit response contains {len(markers)} bare verdict lines "
            f"({sorted(set(markers))}); exactly one terminal marker is required, "
            "and an earlier bare marker makes the machine-read verdict ambiguous"
        )

    missing = [s for s in REQUIRED_SECTIONS if s not in response_text]
    if missing:
        raise InvalidAuditResponse(
            f"audit report is missing required §14.1 section(s): {missing}"
        )

    return AuditResult(text=response_text, verdict=verdict)


def validate_artifact_identity(response_text: str, artifact_id: str) -> None:
    if artifact_id not in response_text:
        raise InvalidAuditResponse(
            f"audit report never mentions artifact {artifact_id}; "
            "refusing to accept it as this artifact's audit"
        )
