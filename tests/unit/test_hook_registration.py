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

Registration is live — CONFLICT-D resolved
-------------------------------------------
Artifact 024 **is** registered, at ``PreToolUse`` with ``matcher: ""``. That
became possible only once CONFLICT-D was resolved: Artifact 022 used to deny
its ``OPAQUE`` Bash class unconditionally, and ``pytest``, ``git commit`` and
``sed`` are all ``OPAQUE``, so registering across Bash denied the runner that
would have proved ``Val: hooks registered``. Artifact 022's controlled
unfreeze moved that decision to canonical reachability, so broad registration
is now both safe and required — Bash must stay inside the boundary, because a
matcher excluding it was experimentally shown to let a Bash redirect write
``canon/**`` unseen.

The assertions that presuppose a registration remain gated on one actually
existing, keyed to **any** lifecycle rather than to ``PreToolUse``. That gate
is now satisfied, so all of them run; it is kept because gating on the correct
lifecycle would have skipped exactly the tests that detect a wrong one.
"""

from __future__ import annotations

import json
import subprocess
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
        "no Artifact 022 registration in .claude/settings.json; these arm as "
        "soon as canon_deny.py appears under any lifecycle. Expected to be "
        "satisfied — Artifact 024 is registered — so a skip here means the "
        "registration was removed"
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
    for event in (
        "PostToolUse",
        "Stop",
        "SubagentStop",
        "Notification",
        "SessionStart",
        "SessionEnd",
    ):
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
def test_matcher_is_exactly_the_empty_string():
    """The approved matcher is ``""`` — asserted exactly, not permissively.

    ``""`` matches every tool, which is what the resolved contract requires:
    Artifact 022 must receive the full ``PreToolUse`` surface, Bash included.

    This is deliberately strict. ``None``, ``"*"`` and ``".*"`` are rejected
    even though some would behave the same, because a matcher that merely
    "looks broad" is how the excluding form gets in later. Narrowing to
    ``Write|Edit|MultiEdit|NotebookEdit`` was proven to leave a Bash redirect
    into ``canon/**`` completely unguarded — the hook is never invoked, so
    Artifact 022's own logic never gets to run.
    """
    (entry,) = canon_deny_entries("PreToolUse")

    assert entry["matcher"] == "", f"matcher is {entry['matcher']!r}, must be ''"


@needs_registration
def test_no_critical_tool_is_filtered_out():
    """The reason the empty matcher is required, stated as its own check.

    Every tool here can reach the filesystem, so each must cross the boundary.
    If a future edit replaces ``""`` with a named matcher, this fails unless
    that matcher still names all five.
    """
    (entry,) = canon_deny_entries("PreToolUse")
    matcher = entry["matcher"]

    if matcher == "":
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
def test_registered_command_runs_the_hook_and_denies_a_canonical_write():
    """Integration — the registered command really is an executable guard.

    Runs the command exactly as registered, resolving ``CLAUDE_PROJECT_DIR``
    the way Claude Code does, and feeds it a synthetic ``PreToolUse`` payload.
    Proves the registration string is not merely well-formed but wired to a
    hook that denies. Artifact 022 owns *what* is denied and proves it across
    158 cases; this asserts only that registration did not disconnect it.

    No canonical file is touched — the payload is synthetic and the hook
    writes nothing.
    """
    (entry,) = canon_deny_entries("PreToolUse")
    command = entry["command"].replace("${CLAUDE_PROJECT_DIR:-.}", str(REPO_ROOT))
    payload = {
        "tool_name": "Write",
        "tool_input": {"file_path": "canon/world/registration_probe.md"},
    }

    result = subprocess.run(
        command,
        shell=True,
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        check=False,
    )

    assert result.returncode == 2, result.stderr
    assert not (REPO_ROOT / "canon/world/registration_probe.md").exists()


@pytest.mark.parametrize(
    "command",
    [
        "python -m pytest -q",
        "git status --short",
        "git branch --show-current",
        "git diff",
        "ruff check .",
        "sed -n '1,5p' file.txt",
    ],
)
@needs_registration
def test_registration_does_not_reinstate_the_conflict_d_failure(command):
    """Integration — the failure that blocked this artifact must stay gone.

    Each of these was denied when the hook was registered broadly over the
    pre-resolution Artifact 022, which is what made CONFLICT-D blocking. None
    names a canonical path, so under the resolved contract none may be denied
    merely for being opaque.

    This is the regression guard for the whole conflict: if a future change
    reinstates blanket opacity denial, the build breaks here rather than
    silently at the next session's first command.
    """
    (entry,) = canon_deny_entries("PreToolUse")
    registered = entry["command"].replace("${CLAUDE_PROJECT_DIR:-.}", str(REPO_ROOT))
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    result = subprocess.run(
        registered,
        shell=True,
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        check=False,
    )

    assert result.returncode == 0, f"{command} denied: {result.stderr}"


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
