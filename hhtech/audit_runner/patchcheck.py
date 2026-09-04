"""Patch-prompt response shape validation. BUILD spec §20, §34.

The runner validates contract shape only, never Luna's semantic content —
patch-standard.md §0 draws exactly this line for audit findings, and the
same discipline applies here to a generated patch prompt.
"""

from __future__ import annotations

from .errors import PatchGenerationFailure

_FORBIDDEN_SUBSTRINGS = (
    "patchreport.md",
    "HHTECH_API_KEY",
)

_REQUIRED_MENTIONS = (
    "Task",
    "Target",
)


def validate_patch_prompt(text: str, artifact_id: str, api_key: str = "") -> None:
    if not text or not text.strip():
        raise PatchGenerationFailure("patch prompt response was empty")

    if api_key and api_key in text:
        raise PatchGenerationFailure(
            "patch prompt contains the HHTECH API key; refusing to write it"
        )

    for token in _FORBIDDEN_SUBSTRINGS:
        if token.lower() in text.lower():
            raise PatchGenerationFailure(
                f"patch prompt contains a forbidden reference: {token!r}"
            )

    if artifact_id not in text:
        raise PatchGenerationFailure(
            f"patch prompt never mentions artifact {artifact_id}; "
            "refusing to accept it as this artifact's patch prompt"
        )

    missing = [m for m in _REQUIRED_MENTIONS if m not in text]
    if missing:
        raise PatchGenerationFailure(
            f"patch prompt is missing required content: {missing}"
        )
