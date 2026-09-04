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


# audit-standard.md §13 names two BLOCKED subtypes. The machine-read verdict
# stays one of the three base values so the pipeline's control flow and the
# patchprompt contracts are unchanged; the subtype is carried alongside it, so
# an evidence gap is never confused with an infrastructure failure.
BLOCKED_QUALIFIERS = (
    "INSUFFICIENT AUTHORITATIVE EVIDENCE",
    "RUNNER/INFRASTRUCTURE FAILURE",
)

_QUALIFIER_SPLIT = re.compile(r"\s*[—–-]{1,2}\s*")


@dataclass(frozen=True)
class AuditResult:
    text: str
    verdict: str
    qualifier: str = ""

    @property
    def full_verdict(self) -> str:
        return f"{self.verdict} — {self.qualifier}" if self.qualifier else self.verdict


def _split_verdict(stated: str) -> tuple[str, str]:
    """Split `BLOCKED — INSUFFICIENT AUTHORITATIVE EVIDENCE` into its base
    verdict and qualifier. An unqualified verdict returns an empty qualifier."""
    for base in VALID_VERDICTS:
        if stated == base:
            return base, ""
        if stated.startswith(base):
            remainder = stated[len(base):]
            parts = _QUALIFIER_SPLIT.split(remainder, maxsplit=1)
            if len(parts) == 2 and parts[0] == "":
                return base, parts[1].strip()
    return stated, ""


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

    stated = terminal_match.group(1).strip()
    verdict, qualifier = _split_verdict(stated)
    if verdict not in VALID_VERDICTS:
        raise InvalidAuditResponse(
            f"terminal verdict {stated!r} is not one of {list(VALID_VERDICTS)} "
            f"(optionally qualified, for BLOCKED, by one of {list(BLOCKED_QUALIFIERS)})"
        )
    if qualifier and verdict != "BLOCKED":
        raise InvalidAuditResponse(
            f"terminal verdict {stated!r} carries a qualifier, but only BLOCKED "
            "may be qualified"
        )
    if qualifier and qualifier not in BLOCKED_QUALIFIERS:
        raise InvalidAuditResponse(
            f"BLOCKED qualifier {qualifier!r} is not one of {list(BLOCKED_QUALIFIERS)}"
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

    return AuditResult(text=response_text, verdict=verdict, qualifier=qualifier)


def validate_artifact_identity(response_text: str, artifact_id: str) -> None:
    if artifact_id not in response_text:
        raise InvalidAuditResponse(
            f"audit report never mentions artifact {artifact_id}; "
            "refusing to accept it as this artifact's audit"
        )
