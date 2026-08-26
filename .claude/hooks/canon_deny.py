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

The one question it answers
---------------------------
Artifact 022 never decides whether a mutation is *legitimate*. It decides
only whether the environment can prove, without executing anything, that a
requested filesystem mutation does not target ``canon/**``::

    proven outside canon   → allow
    proven inside canon    → deny
    cannot prove outside   → deny

The third line is the whole design. *Unknown is never safe.*

Bash policy
-----------
Every Bash command falls into exactly one of three classes.

* **Read-only** — a recognized inspecting command (``cat``, ``grep``, ``ls``,
  ``git status`` …). Allowed, including against ``canon/**`` and including
  from a working directory inside it. Artifact 017 restricts *writing* canon,
  not reading it.
* **Simple mutation** — a recognized mutator (``touch``, ``cp``, ``mv``,
  ``rm``, ``tee``, ``sed -i`` …) or a data redirect, whose filesystem targets
  can be read straight off the command line. Allowed **only** when every
  target is statically resolvable and every one resolves outside canon.
* **Opaque** — anything else: an interpreter (``python3``, ``node``,
  ``ruby``, ``perl``, ``sh -c`` …), a build tool, an unrecognized program.
  Denied. Its filesystem effects live inside program logic the command line
  does not expose, so no inspection of the text can establish them.

The opaque class is not a claim that those programs write. It is the
admission that this hook cannot tell, and a guardrail that guesses is not a
guardrail. Note the asymmetry this creates, and keep it in mind when reading
a denial: ``cat canon/foo.md`` is allowed because ``cat`` is *recognized* as
read-only, while ``python3 reader.py`` is denied even if it only reads.
**This is not a read firewall** — it is a refusal to certify opaque
execution.

Unresolved ``$VAR``, ``$(...)`` and backtick substitution in a mutating
command are denied for the same reason. Variables this process can resolve
are substituted textually first, so ``cd "$CANON" && touch f`` is judged on
where ``$CANON`` actually points. The hook never runs a shell, never expands
through one, and never interprets program source.

Trust boundary
--------------
The protected root is derived from this file's own location and from nothing
else. ``CLAUDE_PROJECT_DIR`` deliberately does **not** override it: an
environment variable that could relocate the boundary would be a way to move
the guard off the thing it guards.

What this hook is not
---------------------
Not the Mutation Coordinator, not the Human Gate, not a canonical validation
pipeline, not a transaction system, not a History Record or WSV-H writer, not
Creative Memory, and not a Registry validator. It reads no canonical content
and writes nothing anywhere. ``Auth: enforcing`` is enforcement of a
boundary, never authority over what the boundary protects (P-31; I-84).

Blueprint I-83 is explicit that a guard like this one is defence in depth:
"Execution-substrate guard rails are defence-in-depth, never constitutional
authority." A determined actor with shell access is not fully containable by
text inspection; the constitutional guarantee arrives with artifact 152. This
is a door that fails shut in the meantime.

Adjacent artifacts, and where this one stops
--------------------------------------------
* **017** ``docs/boundaries/canonical_zones.md`` — declares the canonical
  zones. This hook consumes that declaration's boundary (``canon/**``) and
  reproduces no part of its taxonomy, ownership table, or semantics.
* **021** ``src/coolboy12/bootstrap/config.py`` — not imported. A hook runs
  under a bare interpreter with no package install, so 021 is an
  architectural dependency, not a runtime one.
* **023** ``.claude/hooks/zones.json`` — Roadmap row 023 declares
  ``H: 017,022``, so 023 depends on this hook, not the reverse. No zones file
  is read here.
* **024** ``.claude/settings.json`` — registration is 024's job
  (``Val: hooks registered``); this artifact does not modify settings.

Hook contract
-------------
Confirmed from the hooks actually running in this environment rather than
assumed: a payload arrives as JSON on stdin; **exit 2 with a message on
stderr denies**; **exit 0 allows**. That is the mechanism
``~/.claude/stop-hook-git-check.sh`` uses, observed working.
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
``canon/registry/**``, and covers the root directory itself. The zone
taxonomy stays 017's; its machine-readable encoding stays 023's.
"""

WRITE_TOOLS = frozenset({"Write", "Edit", "NotebookEdit", "MultiEdit"})
READ_TOOLS = frozenset({"Read", "Glob", "Grep", "NotebookRead"})
PATH_KEYS = ("file_path", "notebook_path", "path", "filePath")

READ_ONLY_COMMANDS = frozenset(
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
        "pwd",
        "true",
        "false",
    }
)
"""Recognized inspecting commands. Deliberately small — see *Bash policy*."""

SIMPLE_MUTATORS = frozenset(
    {
        "touch",
        "cp",
        "mv",
        "rm",
        "rmdir",
        "mkdir",
        "tee",
        "sed",
        "ln",
        "install",
        "truncate",
        "dd",
        "chmod",
        "chown",
    }
)
"""Mutators whose targets are readable straight off the command line."""

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

READ_ONLY = "read_only"
SIMPLE_MUTATION = "simple_mutation"
OPAQUE = "opaque"

_ENV_VAR = re.compile(r"\$\{(\w+)\}|\$(\w+)")
_COMMAND_SUB = re.compile(r"\$\(|`")
_STDERR_REDIRECT = re.compile(r"\d*>&\d+|\d+>\s*\S+")
_WRITE_REDIRECT = re.compile(r">>?\s*(\"[^\"]*\"|'[^']*'|[^\s;&|]+)")
_SEGMENT_SPLIT = re.compile(r"\|\||&&|[;|&`]|\$\(|\)")


def repository_root() -> str:
    """The repository root, derived only from this file's own location.

    The hook lives at ``<root>/.claude/hooks/canon_deny.py``. Nothing in the
    environment may point it elsewhere — a relocatable boundary is not a
    boundary.
    """
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def is_inside_canon(target: str, root: str, cwd: str | None = None) -> bool:
    """Whether ``target`` resolves to ``<root>/canon`` or anything beneath it.

    Normalized and symlink-resolved before deciding, so ``./canon/f``,
    ``docs/../canon/f`` and a link into the tree are all recognized while
    ``canon/../elsewhere`` is not. Compared by path segment, never by string
    prefix, so ``canonical/`` and ``canon_backup/`` stay outside.
    """
    candidate = (target or "").strip()
    if not candidate:
        return False

    base = cwd if cwd and os.path.isabs(cwd) else root
    resolved = os.path.realpath(os.path.join(base, os.path.expanduser(candidate)))
    protected = os.path.realpath(os.path.join(root, CANONICAL_ROOT_NAME))
    return resolved == protected or resolved.startswith(protected + os.sep)


def _unquote(word: str) -> str:
    return word.strip().strip("\"'")


def _expand_known_env(command: str, environ: dict) -> str:
    """Substitute only the variables this process can resolve.

    Pure text substitution — no shell, no execution. An unresolvable variable
    is left in place so :func:`_has_unresolved_indirection` can still see it;
    erasing it would silently turn unknown into safe.
    """

    def substitute(match: re.Match) -> str:
        name = match.group(1) or match.group(2)
        value = environ.get(name)
        return value if value is not None else match.group(0)

    return _ENV_VAR.sub(substitute, command)


def _has_unresolved_indirection(command: str, environ: dict) -> bool:
    """Whether the command still depends on a path this hook cannot resolve."""
    if _COMMAND_SUB.search(command):
        return True
    return any(
        (match.group(1) or match.group(2)) not in environ
        for match in _ENV_VAR.finditer(command)
    )


def classify_bash(
    command: str, root: str, cwd: str | None
) -> tuple[str, list[str], str | None]:
    """Sort a command into one of the three classes.

    :returns: ``(class, targets, effective_cwd)``. ``targets`` are the paths a
        simple mutation would touch; ``effective_cwd`` accounts for any ``cd``
        the command performs first.

    ``cd`` is neither read-only nor mutating on its own — it relocates the
    directory later segments act in, which is why ``cd canon && touch f`` is
    caught even though ``touch f`` names nothing canonical.
    """
    scrubbed = _STDERR_REDIRECT.sub(" ", command)
    targets = [_unquote(m.group(1)) for m in _WRITE_REDIRECT.finditer(scrubbed)]
    kind = SIMPLE_MUTATION if targets else READ_ONLY
    effective_cwd = cwd

    for segment in _SEGMENT_SPLIT.split(_WRITE_REDIRECT.sub(" ", scrubbed)):
        words = [_unquote(word) for word in segment.split()]
        if not words:
            continue
        head = os.path.basename(words[0]).lower()
        arguments = [word for word in words[1:] if not word.startswith("-")]

        if head == "cd":
            if arguments:
                base = effective_cwd if effective_cwd else root
                effective_cwd = os.path.realpath(os.path.join(base, arguments[0]))
            continue
        if head == "git":
            if arguments and arguments[0] in GIT_READ_ONLY_SUBCOMMANDS:
                continue
            return OPAQUE, targets, effective_cwd
        if head in READ_ONLY_COMMANDS:
            continue
        if head in SIMPLE_MUTATORS:
            kind = SIMPLE_MUTATION
            targets.extend(arguments)
            continue
        return OPAQUE, targets, effective_cwd

    return kind, targets, effective_cwd


def evaluate_bash(
    command: str, root: str, cwd: str | None, environ: dict
) -> tuple[bool, str]:
    """Apply the Bash policy. Returns ``(deny, reason)``."""
    expanded = _expand_known_env(command, environ)
    kind, targets, effective_cwd = classify_bash(expanded, root, cwd)

    if kind == READ_ONLY:
        return False, ""

    if kind == OPAQUE:
        return True, _reason(
            "<opaque command; its filesystem effects cannot be established "
            "without executing it>"
        )

    if _has_unresolved_indirection(expanded, environ):
        return True, _reason("<mutation with unresolved path indirection>")

    if effective_cwd and is_inside_canon(effective_cwd, root):
        return True, _reason("<mutation from a working directory inside canon/>")

    for target in targets:
        if is_inside_canon(target, root, effective_cwd):
            return True, _reason("<mutation targeting canon/>")

    return False, ""


def evaluate(payload: dict, root: str) -> tuple[bool, str]:
    """Decide whether the requested action must be denied.

    An unrelated tool is left alone — Artifact 022 guards one boundary and is
    not a general tool-authorization layer.
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
        # A write tool with no usable target is unevaluable, and an
        # unevaluable write is exactly what must not be waved through.
        return True, _reason("<write tool with no resolvable target>")

    if tool == "Bash":
        command = tool_input.get("command")
        if not isinstance(command, str) or not command.strip():
            return True, _reason("<Bash tool with no usable command>")
        return evaluate_bash(command, root, cwd, dict(os.environ))

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


def _unevaluable(detail: str) -> int:
    """Fail closed on input the hook cannot evaluate.

    A payload the hook cannot parse is a target it cannot judge, and
    permitting an unevaluable action is the bypass this artifact exists to
    prevent. The diagnostic names the fault only — never the payload.
    """
    print(
        f"canon_deny: unreadable hook payload ({detail}). "
        "Action denied because the hook could not establish a safe decision.",
        file=sys.stderr,
    )
    return EXIT_DENY


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else None
    except (ValueError, OSError) as exc:
        return _unevaluable(type(exc).__name__)

    if not isinstance(payload, dict):
        return _unevaluable("payload is not a JSON object")

    deny, reason = evaluate(payload, repository_root())
    if deny:
        print(reason, file=sys.stderr)
        return EXIT_DENY
    return EXIT_ALLOW


if __name__ == "__main__":
    raise SystemExit(main())
