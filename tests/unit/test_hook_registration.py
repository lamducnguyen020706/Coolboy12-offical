"""Registration proofs for the Artifact 024 agent settings.

Artifact 024's ``Val`` is *"hooks registered"*. That is a claim about
``.claude/settings.json``'s structure, not about what the hook does once
invoked — Artifact 022 already owns every behavioural proof in
``tests/negative/test_canon_deny.py``, and none of them is repeated here.

The split is deliberate::

    tests/negative/test_canon_deny.py  ->  does the hook enforce the boundary?
    this file                          ->  is the hook wired up at all?

Every assertion walks the *parsed* structure. Searching the raw text for
``canon_deny.py`` would pass on a mention in an unrelated key, on a
``PostToolUse`` registration that fires after the write it was meant to
prevent, and on a duplicate. Each of those is tested against explicitly.

Registration is currently deferred — CONFLICT-D
-----------------------------------------------
Artifact 024 is **not registered**. Artifact 022 denies its ``OPAQUE`` Bash
class unconditionally, and ``pytest``, ``git commit`` and ``sed`` are all
``OPAQUE``, so registering the hook across Bash denies the runner that would
prove ``Val: hooks registered``. The artifact cannot evidence its own exit
condition while in force. See ``docs/conventions/revolving_resolution_note.md``,
CONFLICT-D; the registration awaits an authorial ruling.

So the assertions that presuppose a registration are skipped **only while no
registration exists anywhere in the file**. The moment ``canon_deny.py``
appears under any lifecycle, every one of them runs — including the checks
that it is at ``PreToolUse`` and nowhere later. A blanket skip would let a
wrong registration land unnoticed; this one cannot.

The checks that hold at baseline — valid JSON, absence from later lifecycles,
survival of the pre-existing hook, no policy in settings — always run.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SETTINGS = REPO_ROOT / ".claude/settings.json"
HOOK_FILENAME = "canon_deny.py"

# Artifact 022 handles these; a matcher that filtered any of them out would
# leave the canonical boundary unenforced on that path.
CRITICAL_TOOLS = ("Write", "Edit", "NotebookEdit", "MultiEdit", "Bash")


def load_settings() -> dict:
    return json.loads(SETTINGS.read_text(encoding="utf-8"))


def entries_for(event: str) -> list[dict]:
    """Every hook command registered under ``event``, flattened."""
    found = []
    for group in load_settings().get("hooks", {}).get(event, []):
        for entry in group.get("hooks", []):
            found.append({**entry, "matcher": group.get("matcher")})
    return found


def canon_deny_entries(event: str) -> list[dict]:
    return [e for e in entries_for(event) if HOOK_FILENAME in e.get("command", "")]


def registered_anywhere() -> bool:
    """Is Artifact 022 named under *any* lifecycle in the settings file?

    Deliberately not ``canon_deny_entries("PreToolUse")``. Gating on the
    correct lifecycle would skip the very tests that detect a registration at
    the wrong one.
    """
    return any(canon_deny_entries(event) for event in load_settings().get("hooks", {}))


needs_registration = pytest.mark.skipif(
    not registered_anywhere(),
    reason=(
        "Artifact 024 registration deferred pending the CONFLICT-D ruling; "
        "these arm as soon as canon_deny.py appears in .claude/settings.json"
    ),
)


# --------------------------------------------------------------------------
# Val — hooks registered.
# --------------------------------------------------------------------------


def test_settings_file_exists_and_is_valid_json():
    assert SETTINGS.is_file()
    assert isinstance(load_settings(), dict)


@needs_registration
def test_artifact_022_is_registered_at_pretooluse():
    """The lifecycle must be PreToolUse, so the hook runs before the write.

    Artifact 022's own docstring assigns this: "Registration as a
    ``PreToolUse`` hook belongs to Artifact 024."
    """
    assert canon_deny_entries("PreToolUse"), "Artifact 022 is not registered"


def test_artifact_022_is_not_registered_at_a_later_lifecycle():
    """PostToolUse would fire after the write it exists to prevent.

    A guard that runs afterwards is not a guard. This fails if the
    registration is ever moved to any event that cannot block the action.
    """
    for event in ("PostToolUse", "Stop", "SubagentStop", "Notification", "SessionEnd"):
        assert not canon_deny_entries(event), f"registered at {event}"


@needs_registration
def test_registration_is_not_duplicated():
    """One registration, in one lifecycle.

    A duplicate would run the hook twice per tool call and make a later
    edit's effect ambiguous.
    """
    events = load_settings().get("hooks", {})
    total = sum(len(canon_deny_entries(event)) for event in events)

    assert total == 1, f"expected exactly one registration, found {total}"


@needs_registration
def test_registered_command_invokes_the_real_hook_file():
    """The command must point at the artifact that actually exists.

    Checked against the file on disk, so a typo or a stale path fails here
    rather than silently registering nothing.
    """
    (entry,) = canon_deny_entries("PreToolUse")
    command = entry["command"]

    assert HOOK_FILENAME in command
    assert ".claude/hooks/" in command
    assert (REPO_ROOT / ".claude/hooks" / HOOK_FILENAME).is_file()


@needs_registration
def test_registration_uses_the_command_type():
    (entry,) = canon_deny_entries("PreToolUse")

    assert entry["type"] == "command"


@needs_registration
def test_matcher_does_not_filter_out_any_critical_tool():
    """Artifact 022 must receive every tool that can reach the filesystem.

    An empty matcher matches all tools, which is the form this environment's
    own settings use. If a future edit narrows it, the narrowed matcher must
    still name each critical tool — otherwise that path silently loses its
    guard, which is the one failure this test exists to catch.
    """
    (entry,) = canon_deny_entries("PreToolUse")
    matcher = entry["matcher"]

    if matcher in ("", None):
        return
    for tool in CRITICAL_TOOLS:
        assert tool in matcher, f"matcher {matcher!r} excludes {tool}"


# --------------------------------------------------------------------------
# Existing configuration must survive.
# --------------------------------------------------------------------------


def test_the_pre_existing_prompt_hook_is_preserved():
    """Artifact 024 adds a registration; it does not replace the file.

    ``.claude/settings.json`` already carried a ``UserPromptSubmit`` hook
    before Artifact 024 existed. Overwriting the file wholesale would have
    silently removed it.
    """
    prompt_hooks = entries_for("UserPromptSubmit")

    assert prompt_hooks, "the pre-existing UserPromptSubmit hook was lost"
    assert any("coolboy12_prompt_log.py" in e.get("command", "") for e in prompt_hooks)


# --------------------------------------------------------------------------
# Scope — 024 registers, it does not decide.
# --------------------------------------------------------------------------


def test_settings_encode_no_canonical_policy():
    """Registration only. The boundary lives in 017, 022 and 023.

    A zone path, a Record Model, or a permission rule appearing here would be
    a second statement of a boundary that already has exactly one home.
    """
    raw = SETTINGS.read_text(encoding="utf-8")

    for forbidden in ("canon/", "zones.json", "world", "epistemic", "registry"):
        assert forbidden not in raw, forbidden


@needs_registration
def test_settings_do_not_wrap_the_hook_in_a_shell_pipeline():
    """The hook's exit code is its verdict, so nothing may rewrite it.

    Artifact 022 signals deny with exit 2 and allow with exit 0. A pipe or a
    ``&&`` chain would substitute another process's status for the hook's and
    quietly turn a denial into an allow.
    """
    (entry,) = canon_deny_entries("PreToolUse")
    command = entry["command"]

    for construct in ("|", "&&", ";", "||"):
        assert construct not in command, construct
