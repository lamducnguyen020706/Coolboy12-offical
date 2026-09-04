"""Minimal HHTECH (GPT-5.6 Luna) chat-completions client.

Stdlib only (urllib), per BUILD spec §7 — no SDK added solely for this
runner. The credential is read once by config.load_config() and is never
logged, printed, or embedded in a request that gets echoed back into an
output file.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request

from .config import HhtechConfig
from .errors import ApiFailure

LunaCall = "Callable[[HhtechConfig, str, str], str]"


def call_luna(config: HhtechConfig, system_prompt: str, user_content: str) -> str:
    """POST a chat-completion request to HHTECH and return the assistant's
    message text. Raises ApiFailure on any network, HTTP, or shape error —
    never returns a partial or guessed result.
    """
    payload = {
        "model": config.model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    }
    body = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        config.endpoint,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config.api_key}",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=config.timeout_seconds) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
        except Exception:  # noqa: BLE001 — best-effort diagnostic only
            pass
        raise ApiFailure(
            f"HHTECH returned HTTP {exc.code}: {detail}"
        ) from exc
    except urllib.error.URLError as exc:
        raise ApiFailure(f"HHTECH request failed: {exc.reason}") from exc
    except TimeoutError as exc:
        raise ApiFailure(
            f"HHTECH request timed out after {config.timeout_seconds}s"
        ) from exc

    try:
        parsed = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ApiFailure(f"HHTECH returned malformed JSON: {exc}") from exc

    try:
        choices = parsed["choices"]
        if not choices:
            raise ApiFailure("HHTECH returned an empty choices list")
        content = choices[0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ApiFailure(
            f"HHTECH response did not have the expected chat-completions shape: {exc}"
        ) from exc

    if not isinstance(content, str) or not content.strip():
        raise ApiFailure("HHTECH returned an empty model response")

    return content
