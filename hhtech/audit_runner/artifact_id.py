"""Artifact identifier validation and normalization.

BUILD spec §5: exactly one artifact identifier, normalized to the Roadmap's
three-digit form, range 1..490 inclusive. Reject everything else. Never
silently interpret an arbitrary string.
"""

from __future__ import annotations

import re

from .errors import InputError

_DIGITS = re.compile(r"\A[0-9]{1,3}\Z")

MIN_ARTIFACT = 1
MAX_ARTIFACT = 490


def normalize_artifact_id(raw: str) -> str:
    """Return the canonical three-digit artifact ID, or raise InputError.

    Accepts "1", "01", "001", "42", "042", "490". Rejects empty input,
    non-digit input, leading '+'/'-', extra tokens, and out-of-range values.
    """
    if raw is None:
        raise InputError("no artifact ID given")
    token = raw.strip()
    if not token:
        raise InputError("no artifact ID given")
    if " " in token or "\t" in token:
        raise InputError(
            f"exactly one artifact ID is accepted, got extra token(s) in {raw!r}"
        )
    if not _DIGITS.match(token):
        raise InputError(f"{raw!r} is not a valid artifact ID (expected digits 1-490)")
    value = int(token)
    if value < MIN_ARTIFACT or value > MAX_ARTIFACT:
        raise InputError(
            f"artifact ID {value} is out of range ({MIN_ARTIFACT}-{MAX_ARTIFACT})"
        )
    return f"{value:03d}"


def parse_single_argument(argv: list[str]) -> str:
    """Validate that argv is exactly one artifact-ID argument.

    Rejects zero arguments and more than one argument outright, before any
    digit validation, so "/audit 42 extra" fails for the right reason.
    """
    if len(argv) == 0:
        raise InputError("usage: audit <artifact-id>")
    if len(argv) > 1:
        raise InputError(
            f"exactly one artifact ID is accepted, got {len(argv)} arguments: {argv!r}"
        )
    return normalize_artifact_id(argv[0])
