"""Patch prompt validation — shape and verdict agreement, fail closed.

A patchprompt that contradicts its own audit is worse than no patchprompt:
it sends an implementation agent to change an artifact the audit never
faulted, or to "fix" a blocked audit by editing the target. Both are
rejected here before anything is written or committed.

As in verdict.py, this validates contract shape only, never the substance
of Luna's remediation direction.
"""

from __future__ import annotations

import re

from .errors import PatchGenerationFailure

# patch-standard.md §20: a patch RESULT is an execution outcome, never a
# repository file. A generated prompt that instructs one is malformed.
FORBIDDEN_SUBSTRINGS = (
    "patchreport.md",
    "HHTECH_API_KEY",
)

# Authority protection (patch-standard.md §10): the patch agent may never
# edit an authority source to make an audit pass. Matched as verb + direct
# object, so "patch Artifact 042 under patch-standard.md" — patching the
# artifact *according to* the standard — is not mistaken for editing it.
_AUTHORITY_DOCUMENT = (
    r"(?:(?:Master\s+)?Blueprint|RMS|Record\s+Model\s+System|Roadmap"
    r"|audit-standard\.md|patch-standard\.md)"
)
_AUTHORITY_EDIT_PATTERNS = (
    re.compile(
        r"\b(?:edit|modify|update|change|rewrite|amend|revise|adjust|patch|weaken|relax)\s+"
        r"(?:the\s+|its\s+|our\s+|this\s+)?(?:current\s+|existing\s+)?"
        + _AUTHORITY_DOCUMENT
        + r"\b",
        re.IGNORECASE,
    ),
)

# Negations that make an authority mention safe — the prompt is FORBIDDING
# the edit, which is exactly what the standard requires it to do.
_NEGATION = re.compile(
    r"\b(?:do not|don't|never|must not|may not|forbidden|prohibited|without)\b",
    re.IGNORECASE,
)

NO_PATCH_PHRASE = "NO PATCH REQUIRED"
DO_NOT_PATCH_PHRASE = "DO NOT PATCH"

_MIN_LENGTH = 200


def _find_authority_edit_instruction(text: str) -> str | None:
    """Return an offending clause, or None. A clause that negates the edit
    ("do not modify the Blueprint") is compliant, not a violation — so the
    split is clause-level, not sentence-level, and a negation in one clause
    cannot excuse an instruction in the next."""
    for sentence in re.split(r"(?<=[.!?;\n])\s+", text):
        for pattern in _AUTHORITY_EDIT_PATTERNS:
            match = pattern.search(sentence)
            if match and not _NEGATION.search(sentence):
                return sentence.strip()[:200]
    return None


def validate_patch_prompt(
    text: str, artifact_id: str, verdict_value: str, api_key: str = ""
) -> None:
    """Validate the generated patchprompt against its verdict. Fail closed."""
    if not text or not text.strip():
        raise PatchGenerationFailure("patch prompt response was empty")

    if len(text.strip()) < _MIN_LENGTH:
        raise PatchGenerationFailure(
            f"patch prompt is only {len(text.strip())} characters; too short to "
            "carry the required target, authority, action and validation content"
        )

    if api_key and api_key in text:
        raise PatchGenerationFailure(
            "patch prompt contains the HHTECH API key; refusing to write it"
        )

    lowered = text.lower()
    for token in FORBIDDEN_SUBSTRINGS:
        if token.lower() in lowered:
            raise PatchGenerationFailure(
                f"patch prompt contains a forbidden reference: {token!r}"
            )

    if artifact_id not in text:
        raise PatchGenerationFailure(
            f"patch prompt never mentions artifact {artifact_id}; "
            "refusing to accept it as this artifact's patch prompt"
        )

    offending = _find_authority_edit_instruction(text)
    if offending is not None:
        raise PatchGenerationFailure(
            "patch prompt instructs modification of an authority source "
            f"(patch-standard.md §10 forbids this): {offending!r}"
        )

    upper = text.upper()
    has_no_patch = NO_PATCH_PHRASE in upper
    has_do_not_patch = DO_NOT_PATCH_PHRASE in upper

    if verdict_value == "PASS":
        if not has_no_patch:
            raise PatchGenerationFailure(
                f"verdict is PASS but the patch prompt does not state "
                f"{NO_PATCH_PHRASE!r}; refusing a prompt that could be read as "
                "authorising a patch"
            )
    elif verdict_value == "BLOCKED":
        if not has_do_not_patch:
            raise PatchGenerationFailure(
                f"verdict is BLOCKED but the patch prompt does not state "
                f"{DO_NOT_PATCH_PHRASE!r}; a blocked audit must never be cleared "
                "by patching the artifact"
            )
        if has_no_patch:
            raise PatchGenerationFailure(
                "verdict is BLOCKED but the patch prompt says "
                f"{NO_PATCH_PHRASE!r}, which states the PASS contract; BLOCKED is "
                "not a pass"
            )
        if "audit" not in lowered:
            raise PatchGenerationFailure(
                "verdict is BLOCKED but the patch prompt does not require the "
                "audit to be re-run once the evidence gap is resolved"
            )
    elif verdict_value == "PATCH REQUIRED":
        if has_no_patch:
            raise PatchGenerationFailure(
                f"verdict is PATCH REQUIRED but the patch prompt says "
                f"{NO_PATCH_PHRASE!r}; the prompt contradicts its own audit"
            )
    else:
        raise PatchGenerationFailure(
            f"cannot validate a patch prompt against unknown verdict {verdict_value!r}"
        )
