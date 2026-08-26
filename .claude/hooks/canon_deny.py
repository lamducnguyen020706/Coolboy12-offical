#!/usr/bin/env python3
"""Canon write-deny hook — Artifact 022.

Artifact 022 · ``.claude/hooks/canon_deny.py`` · Own: CONST · RM: n/a ·
T: code · R: VALID · SoT: DEV-ENV · Auth: enforcing · Canon: n/a · CD: no ·
Ph/St: P0/0e · Req: BR-07 · BP: §10 Spine 2 · RMS: §4 · H: 017,021 · S: — ·
LS: — · G: enforces all canonical gates · → 133 ·
Val: direct write to ``canon/**`` denied · Done: deny proven by negative test ·
Why: built in P0 so bypass is impossible even while P5 is under construction ·
Risk: CRITICAL · ∥: no

What this hook is
-----------------
A Claude Code execution-environment guardrail::

    Claude Code environment
            ↓
       this hook
            ↓
    direct write attempt into canon/**
            ↓
          DENIED

Spine law 2 (Blueprint §10) fixes one path for canon: *propose → check →
human gate → commit → changelog → log*. Spine law 3 reserves the commit to
the human. I-83 names the Mutation Coordinator the only component that writes
canon. Artifact 017 §13 rule 4 states it without exemption: "Every direct
write to ``canon/**`` is prohibited, for every actor, with no exemption for
trust, position, or convenience. A second write path is a second canon."

The Mutation Coordinator is Roadmap artifact 152, in P5, and does not exist
yet. This hook exists in P0 precisely so the environment cannot quietly
become a second canonical write path while P5 is still being built.

**This hook does not make canon writable through the right path. It only
makes the wrong path fail.**

What this hook is not
---------------------
Not the Mutation Coordinator, not the Human Gate, not a canonical validation
pipeline, not a transaction system, not a History Record or WSV-H writer, not
Creative Memory, and not a Registry validator. It reads no canonical content,
writes nothing anywhere, and decides nothing about whether a proposed change
is *good* — only about whether the path being written is inside the canonical
zone. ``Auth: enforcing`` is enforcement of a boundary, never authority over
what the boundary protects (P-31: dependencies provide capability, never
authority; I-84: no external component holds canonical semantics).

Blueprint I-83 is explicit that a guard like this one is defence in depth:
"Execution-substrate guard rails are defence-in-depth, never constitutional
authority." The constitutional guarantee arrives with artifact 152. This is a
door that fails shut in the meantime.

Adjacent artifacts, and where this one stops
--------------------------------------------
* **017** ``docs/boundaries/canonical_zones.md`` — declares the canonical
  zones. This hook consumes that declaration's boundary (``canon/**``) and
  reproduces no part of its taxonomy, ownership table, or semantics.
* **021** ``src/coolboy12/bootstrap/config.py`` — the configuration loader.
  Not imported: a hook must run under a bare interpreter with no package
  install, and 021 is DEV-ENV runtime code, not a hook dependency.
* **023** ``.claude/hooks/zones.json`` — machine-readable zones. **Roadmap
  row 023 declares ``H: 017,022``, so 023 depends on this hook, not the
  reverse.** This hook therefore reads no zones file and must not: it holds
  the one boundary its own ``Val`` names, and 023 will encode the full zone
  inventory later.
* **024** ``.claude/settings.json`` — registers hooks. Registration is 024's
  job (``Val: hooks registered``); this artifact does not modify settings.

Reads are never blocked
-----------------------
Artifact 017 restricts *writing* ``canon/**``, not reading it. An operator
and the environment must be able to inspect canon. ``READ canon/**`` is
allowed; ``WRITE canon/**`` is denied.

Hook contract
-------------
Confirmed from the hooks actually running in this environment rather than
assumed: a payload arrives as JSON on stdin; **exit 2 with a message on
stderr denies** the action and shows the reason; **exit 0 allows**. That is
the mechanism ``~/.claude/stop-hook-git-check.sh`` uses, observed working.
Registration as a ``PreToolUse`` hook belongs to Artifact 024.
"""

from __future__ import annotations

import json
import os
import re
import sys

EXIT_ALLOW = 0
EXIT_DENY = 2

CANONICAL_ROOT_NAME = "canon"
"""The one directory name this hook protects.

Artifact 017 §4 declares the canonical family as ``canon/**`` with six model
subtrees beneath it. Guarding the family root covers every subtree, including
``canon/registry/**``, without reproducing 017's inventory here — the zone
taxonomy is 017's and the machine-readable encoding is 023's.
"""

WRITE_TOOLS = frozenset({"Write", "Edit", "NotebookEdit", "MultiEdit"})
"""Tools whose purpose is to change a file at a named path."""

READ_TOOLS = frozenset({"Read", "Glob", "Grep", "NotebookRead"})
"""Tools that inspect without changing. Never denied (see *Reads*, above)."""

PATH_KEYS = ("file_path", "notebook_path", "path", "filePath")
"""Keys a write tool may carry its target path under."""

READ_ONLY_SHELL = frozenset(
    {
        "cat",
        "grep",
        "rg",
        "egrep",
        "fgrep",
        "ls",
        "find",
        "head",
        "tail",
        "wc",
        "diff",
        "cmp",
        "file",
        "stat",
        "du",
        "less",
        "more",
        "sort",
        "uniq",
        "cut",
        "md5sum",
        "sha256sum",
        "basename",
        "dirname",
        "realpath",
        "readlink",
        "echo",
    }
)
"""Shell commands that inspect without changing anything.

A Bash command touching the canonical zone is allowed **only** when every one
of its segments is one of these. That is an allowlist, not a blocklist: an
unrecognized command near ``canon/`` is denied rather than permitted, because
a blocklist of mutating verbs can always be evaded (``python3 -c "open(...,
'w')"``) while an allowlist fails in the safe direction.
"""

GIT_READ_ONLY_SUBCOMMANDS = frozenset(
    {
        "status",
        "log",
        "diff",
        "show",
        "ls-files",
        "blame",
        "cat-file",
        "rev-parse",
        "describe",
        "shortlog",
        "grep",
    }
)
"""Git subcommands that only read. ``git checkout``/``restore``/``rm`` write."""

_STDERR_REDIRECT = re.compile(r"\d*>&\d+|\d+>\s*\S+")
"""``2>&1``, ``2>/dev/null`` and friends.

Stripped before scanning for write redirects. Treating a stderr redirect as a
write is how ``cat canon/PURPOSE.md 2>/dev/null`` — an ordinary read — would
otherwise be denied, which Artifact 017 does not prohibit and §9 of this
artifact's contract forbids blocking.
"""

_WRITE_REDIRECT = re.compile(r">")

_SEGMENT_SPLIT = re.compile(r"\|\||&&|[;|&`]|\$\(")


def repository_root() -> str:
    """Locate the repository root without trusting the process's cwd.

    The hook lives at ``<root>/.claude/hooks/canon_deny.py``, so its own
    location fixes the root. ``CLAUDE_PROJECT_DIR`` is honoured only when it
    actually looks like this repository, so an unrelated or hostile value
    cannot redirect the boundary somewhere harmless.
    """
    from_file = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    declared = os.environ.get("CLAUDE_PROJECT_DIR")
    if declared:
        candidate = os.path.abspath(os.path.expanduser(declared))
        if os.path.isdir(os.path.join(candidate, ".claude")):
            return candidate
    return from_file


def canonical_root(root: str) -> str:
    """Absolute, symlink-resolved path of the protected ``canon/`` directory."""
    return os.path.realpath(os.path.join(root, CANONICAL_ROOT_NAME))


def is_inside_canon(target: str, root: str, cwd: str | None = None) -> bool:
    """Whether ``target`` resolves inside ``<root>/canon``.

    Normalizes before deciding, so ``./canon/f.md`` and ``docs/../canon/f.md``
    are both recognized, and ``canon/../elsewhere`` is not. ``realpath``
    resolves symlinks, so a link pointing into the canonical tree cannot be
    used to arrive there by another name.

    Comparison is path-segment based, never string-prefix, so ``canonical/``
    and ``canon_backup/`` are correctly outside the boundary despite sharing
    a textual prefix with ``canon``.
    """
    candidate = (target or "").strip()
    if not candidate:
        return False

    base = cwd if cwd and os.path.isabs(cwd) else root
    resolved = os.path.realpath(os.path.join(base, os.path.expanduser(candidate)))
    protected = canonical_root(root)

    if resolved == protected:
        return True
    return resolved.startswith(protected + os.sep)


def _mentions_canon(text: str) -> bool:
    """Whether ``text`` references the canonical zone as a path segment.

    Matches ``canon/`` and a bare ``canon`` used as a path token, so
    ``cd canon && ...`` is seen. Segment-anchored, so ``canonical/`` and
    ``canon_backup/`` do not match.
    """
    boundary = rf"(?<![\w.-]){CANONICAL_ROOT_NAME}(?:/|$|[\s'\")])"
    return bool(re.search(boundary, text))


def _shell_touches_canon_destructively(command: str) -> bool:
    """Whether a canon-referencing shell command may change the filesystem.

    Allowlist, evaluated after stripping stderr redirects: the command is
    permitted only when it contains no write redirect and every segment's
    leading word is a known read-only command. Anything unrecognized is
    treated as destructive.

    **Known limit, stated rather than papered over.** This is not a shell
    parser, and arbitrary shell is not fully containable by inspection — a
    determined obfuscation (an unusual interpreter, an encoded string, an
    indirect exec) can still reach the filesystem. Blueprint I-83 anticipates
    exactly this: "Execution-substrate guard rails are defence-in-depth,
    never constitutional authority." The constitutional guarantee is the
    Mutation Coordinator (artifact 152); this hook raises the cost of the
    accidental and the casual, and it fails toward denial when unsure.
    """
    scrubbed = _STDERR_REDIRECT.sub(" ", command)

    if _WRITE_REDIRECT.search(scrubbed):
        return True

    for segment in _SEGMENT_SPLIT.split(scrubbed):
        words = segment.strip().split()
        if not words:
            continue
        head = os.path.basename(words[0]).lower()
        if head == "git":
            subcommands = [w for w in words[1:] if not w.startswith("-")]
            if subcommands and subcommands[0] in GIT_READ_ONLY_SUBCOMMANDS:
                continue
            return True
        if head not in READ_ONLY_SHELL:
            return True
    return False


def evaluate(payload: dict, root: str) -> tuple[bool, str]:
    """Decide whether the requested action must be denied.

    :returns: ``(deny, reason)``. ``reason`` is empty when allowed.

    Fails closed. Where the target cannot be resolved but the request plainly
    references the canonical zone, the action is denied: permitting an
    unreadable request risks exactly the write this hook exists to stop, and
    a false refusal costs a rephrase.
    """
    tool = payload.get("tool_name") or payload.get("toolName") or ""
    tool_input = payload.get("tool_input") or payload.get("toolInput") or {}
    if not isinstance(tool_input, dict):
        tool_input = {}
    cwd = payload.get("cwd") if isinstance(payload.get("cwd"), str) else None

    if tool in READ_TOOLS:
        return False, ""

    if tool in WRITE_TOOLS:
        for key in PATH_KEYS:
            value = tool_input.get(key)
            if isinstance(value, str) and value.strip():
                if is_inside_canon(value, root, cwd):
                    return True, _reason(value)
                return False, ""
        # A write tool with no resolvable path is ambiguous; fail closed only
        # when the request mentions the canonical zone at all.
        blob = json.dumps(tool_input, ensure_ascii=False)
        if _mentions_canon(blob):
            return True, _reason("<unresolved path in tool input>")
        return False, ""

    if tool == "Bash":
        command = tool_input.get("command")
        if not isinstance(command, str) or not command.strip():
            return False, ""
        if not _mentions_canon(command):
            return False, ""
        if _shell_touches_canon_destructively(command):
            return True, _reason("<shell command targeting canon/>")
        return False, ""

    return False, ""


def _reason(target: str) -> str:
    """The denial message. Names the boundary, never the payload."""
    return (
        f"DENIED by Artifact 022 (canon write-deny hook): {target}\n"
        "Direct writes to canon/** are prohibited. Canonical changes must "
        "traverse the governed mutation path — propose, check, Human Gate, "
        "Mutation Coordinator, changelog (Blueprint §10 Spine 2, I-83; "
        "Artifact 017 §13 rule 4). The Mutation Coordinator is Roadmap "
        "artifact 152 and is not built yet, so there is currently no legal "
        "direct-write path into canon/**. Reading canon/** is allowed."
    )


def main() -> int:
    root = repository_root()
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        if not isinstance(payload, dict):
            payload = {}
    except (ValueError, OSError) as exc:
        # Malformed input must not become an accidental permit, but it also
        # must not deny every unrelated action. Nothing is known about the
        # target here, so allow and make the environment fault visible.
        print(
            f"canon_deny: unreadable hook payload ({type(exc).__name__})",
            file=sys.stderr,
        )
        return EXIT_ALLOW

    deny, reason = evaluate(payload, root)
    if deny:
        print(reason, file=sys.stderr)
        return EXIT_DENY
    return EXIT_ALLOW


if __name__ == "__main__":
    raise SystemExit(main())
