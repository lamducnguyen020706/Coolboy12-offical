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


_BODY_ECHO_LIMIT = 400


def _bounded(value: object) -> str:
    """Render a server-supplied value, truncated to the echo limit."""
    text = str(value)
    if len(text) <= _BODY_ECHO_LIMIT:
        return text
    return text[:_BODY_ECHO_LIMIT] + "…"


def _describe_unexpected(parsed: object, config: HhtechConfig) -> str:
    """Say what actually came back when the response was not a completion.

    A gateway commonly answers HTTP 200 with an error document — an unknown
    model, an exhausted quota, a rejected key — and the caller then sees only
    ``'choices'``, which names the missing key and not the reason. That turns
    a one-line server message into a debugging session.

    The body is echoed bounded and never in full. It cannot carry the
    credential (the key travels in the request header, not the response), but
    a response is still untrusted input and is truncated rather than pasted.
    """
    if isinstance(parsed, dict):
        error = parsed.get("error")
        if isinstance(error, dict):
            message = error.get("message") or error.get("type") or "no message given"
            code = error.get("code")
            detail = f"HHTECH reported an error: {_bounded(message)}"
            if code:
                detail += f" (code {_bounded(code)})"
            return f"{detail}. Model requested: {config.model!r}."
        if isinstance(error, str) and error.strip():
            return (
                f"HHTECH reported an error: {_bounded(error)}. "
                f"Model requested: {config.model!r}."
            )
        keys = ", ".join(sorted(map(str, parsed))) or "none"
        return f"Top-level keys returned: {keys}. Model requested: {config.model!r}."
    return f"Response was {type(parsed).__name__}, not an object."


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
        with urllib.request.urlopen(
            request, timeout=config.timeout_seconds
        ) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
        except Exception:  # noqa: BLE001, S110 — best-effort diagnostic only;
            # the HTTP status below is the real error, and a body that cannot
            # be read must never mask it or leak into the failure path.
            pass
        raise ApiFailure(f"HHTECH returned HTTP {exc.code}: {detail}") from exc
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
            "HHTECH response did not have the expected chat-completions shape: "
            f"{exc}. {_describe_unexpected(parsed, config)}"
        ) from exc

    if not isinstance(content, str) or not content.strip():
        raise ApiFailure("HHTECH returned an empty model response")

    return content
