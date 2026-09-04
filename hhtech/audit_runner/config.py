"""HHTECH endpoint configuration.

Credential comes from the environment only (BUILD spec §6). Never hard-coded,
never printed, never written to any output file, log, or commit.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from .errors import InputError

HHTECH_BASE_URL = "https://hhtechapi.net"
HHTECH_ENDPOINT = f"{HHTECH_BASE_URL}/v1/chat/completions"
HHTECH_MODEL = "gpt-5.6-luna"
API_KEY_ENV_VAR = "HHTECH_API_KEY"

DEFAULT_TIMEOUT_SECONDS = 180


@dataclass(frozen=True)
class HhtechConfig:
    endpoint: str
    model: str
    api_key: str
    timeout_seconds: int


def load_config(timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS) -> HhtechConfig:
    api_key = os.environ.get(API_KEY_ENV_VAR, "").strip()
    if not api_key:
        raise InputError(
            f"{API_KEY_ENV_VAR} is not set in the environment. "
            "The runner does not call HHTECH without it, and never "
            "prompts for or invents one."
        )
    return HhtechConfig(
        endpoint=HHTECH_ENDPOINT,
        model=HHTECH_MODEL,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
    )
