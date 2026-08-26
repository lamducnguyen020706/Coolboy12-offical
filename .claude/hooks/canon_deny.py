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
* **Simple mutation** — one of seven mutators (``touch``, ``cp``, ``mv``,
  ``rm``, ``rmdir``, ``mkdir``, ``tee``) or a data redirect, invoked with
  plainly positional targets. Allowed **only** when every target is
  statically resolvable and every one resolves outside canon.
* **Opaque** — everything else. An interpreter (``python3``, ``node``,
  ``ruby``, ``perl``, ``sh -c`` …), a build tool, an unrecognized program —
  and also a *recognized* command invoked in a form this hook does not
  understand. **Allowed unless it establishes a canonical target.** Opacity
  is not itself grounds for denial (CONFLICT-D; see *Decision axis*).

Membership in a list is never enough on its own, because option syntax can
move where a command writes:

* A read-only command carrying a write-producing option is opaque.
  ``sort input.txt`` inspects; ``sort -o out.txt input.txt`` writes, and so
  does ``git diff --output=out.patch``. Both are denied rather than parsed —
  this hook does not need to support advanced output syntax, and refusing is
  cheaper than getting it subtly wrong.
* A mutator carrying an option this hook does not recognize is opaque.
  ``cp src dst`` has readable targets; ``cp --target-directory=canon/world
  src`` writes somewhere the positional arguments never name. Only a small
  set of plainly harmless flags (``-r``, ``-f``, ``-p``, ``-v``, ``-a``,
  ``-n``, ``-d`` and their long forms) keeps a mutator classified.
* ``sed``, ``ln``, ``install``, ``dd``, ``chmod``, ``chown`` and ``truncate``
  are deliberately **not** mutators here. Each has option-rich semantics that
  would need a real CLI parser to judge, so each is opaque. That is a smaller
  attack surface for the classifier, not a gap.

The opaque class is not a claim that those programs write. It is the
admission that this hook cannot tell.

Decision axis — canonical reachability, not command provability
---------------------------------------------------------------
This artifact once denied every opaque command outright. That rule was an
implementation hardening choice, not a source requirement: searched across
the Blueprint, the RMS and the Roadmap, *opaque* never appears as a command
policy at all. Blueprint §26.8 scopes the boundary by **path** — "a hook
that denies direct writes to **those paths** is the deterministic expression
of Spine law 2" — while the same section lists command execution *including
tests* as a facility the environment legitimately provides, and states that
derived stores and proposals are freely writable. Denying every command
whose effects could not be proven denied all three of those grants, which is
how registering this hook halted the build (CONFLICT-D).

So the question asked here is **"does this invocation establish a write
target under canon/**?"** — never "is this command safe?". A command that
establishes no canonical target is allowed however little this hook
understands it. ``pytest``, ``git commit``, ``ruff``, ``make`` and
``sed -n`` all run.

The asymmetry that remains is narrower and worth reading a denial against:
``cd canon && python3 anything.py`` is denied because a relative write from
that directory lands in canon, while ``python3 reader.py`` from the root is
allowed.

Unresolved ``$VAR``, ``$(...)`` and backtick substitution in a *simple
mutation* stay denied — there the command is known to write and only the
destination is missing, so the canonical target cannot be ruled out.
Variables this process can resolve are substituted textually first, so
``cd "$CANON" && touch f`` is judged on where ``$CANON`` actually points.
The hook never runs a shell, never expands through one, and never interprets
program source.

Residual risk, stated rather than papered over
-----------------------------------------------
An opaque command that computes its own path writes into canon unseen —
``python3 -c "…open(os.environ['CANON'] + '/f.md','w')…"`` names no
canonical path in its text, and ``sed -i … canon/world/f.md`` is opaque
because sed's option grammar is not modelled here. Establishing either would
mean interpreting arbitrary program source, which this hook must not do.
That residual is what I-83 and I-100 already anticipate: "execution-substrate
guard rails are defence-in-depth, **never constitutional authority**". The
constitutional guarantee is the Mutation Coordinator and the Human Gate
(artifact 152), not this file. §26.8 says the same from the other side — "if
the hook and the Human Gate ever disagree, the gate is right and the hook is
a bug".

The error runs the other way too, and one case is common enough to name:
``git commit -m "… canon/** …"`` is **denied**, because a canonical path in
the message is indistinguishable from one in an argument. Denying a commit
is not a canonical write, so this errs to the safe side; ``git commit -F``
or a heredoc passes the message on stdin, where the hook never sees it.

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

SIMPLE_MUTATORS = frozenset({"touch", "cp", "mv", "rm", "rmdir", "mkdir", "tee"})
"""The only mutators whose targets are readable straight off the command line.

Seven, deliberately. ``sed``, ``ln``, ``install``, ``dd``, ``chmod``, ``chown``
and ``truncate`` are absent on purpose: judging them needs option semantics
this hook has no business implementing, so they fall through to opaque.
"""

SAFE_SHORT_MUTATOR_FLAGS = frozenset("rRfpvand")
SAFE_LONG_MUTATOR_FLAGS = frozenset(
    {"recursive", "force", "parents", "verbose", "no-clobber", "dir", "archive"}
)
"""Flags that plainly do not move where a mutator writes.

Any other option makes the invocation opaque. This is an allowlist because an
unrecognized option can redirect the destination (``-t``,
``--target-directory``), and ignoring what it cannot read is how a classifier
turns unknown into safe.
"""

WRITE_PRODUCING_OPTIONS = frozenset({"-o", "--output", "-t", "--target-directory"})
WRITE_PRODUCING_PREFIXES = ("--output=", "--target-directory=", "--out-file=")
"""Options that make an otherwise read-only command write a file."""

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

_SEGMENT_SEPARATORS = ";|&`()"

_PATH_RUNS = re.compile(r"[\w./~+@-]+")
"""Maximal runs of path characters, used to find a target inside a token.

Deliberately not a path *validator* — it over-collects (``open``, ``w`` and
``.write`` are all runs) and every candidate is then resolved properly by
:func:`is_inside_canon`. Over-collecting is safe here; missing an embedded
literal is not.
"""


def _split_segments(command: str) -> list[str]:
    """Split a command on its *unquoted* separators.

    Not a shell parser, and deliberately not grown into one. It tracks one
    thing — whether the cursor is inside a quoted run — because that is the
    single fact the previous regex lacked: ``grep -e 'a\\|b' file`` was split
    at the quoted pipe, leaving fragments whose first word was not ``grep``,
    and the invocation was misread as a pipeline of unknown commands. A false
    denial on a read-only search, not a bypass, but the classifier was reading
    text that was never shell syntax.

    Genuine pipelines still split: ``cat f | grep x`` yields two segments.
    """
    segments: list[str] = []
    current: list[str] = []
    quote: str | None = None
    index = 0

    while index < len(command):
        char = command[index]
        if char == "\\" and index + 1 < len(command) and quote != "'":
            # A backslash escapes the next character everywhere except inside
            # single quotes, where shell treats it literally.
            current.append(char)
            current.append(command[index + 1])
            index += 2
            continue
        if quote:
            if char == quote:
                quote = None
            current.append(char)
        elif char in "\"'":
            quote = char
            current.append(char)
        elif char in _SEGMENT_SEPARATORS:
            segments.append("".join(current))
            current = []
        else:
            current.append(char)
        index += 1

    segments.append("".join(current))
    return segments


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


def _has_write_producing_option(words: list[str]) -> bool:
    """Whether a read-only invocation carries an option that writes a file."""
    return any(
        word in WRITE_PRODUCING_OPTIONS or word.startswith(WRITE_PRODUCING_PREFIXES)
        for word in words
    )


def _mutator_options_are_understood(words: list[str]) -> bool:
    """Whether every option on a mutator is one that cannot move the target."""
    for word in words:
        if not word.startswith("-") or word == "--":
            continue
        if word.startswith("--"):
            if word[2:].split("=", 1)[0] not in SAFE_LONG_MUTATOR_FLAGS:
                return False
        elif any(flag not in SAFE_SHORT_MUTATOR_FLAGS for flag in word[1:]):
            return False
    return True


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
    opaque = False
    opaque_words: list[str] = []

    # Every segment is scanned, including those after an opaque one. Returning
    # early on the first opaque head would abandon the rest of the command, so
    # `python3 build.py && touch canon/world/f` would have its canonical target
    # collected only if the interpreter came second.
    for segment in _split_segments(_WRITE_REDIRECT.sub(" ", scrubbed)):
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
            read_only_subcommand = (
                arguments and arguments[0] in GIT_READ_ONLY_SUBCOMMANDS
            )
            if read_only_subcommand and not _has_write_producing_option(words):
                continue
            opaque = True
            opaque_words.extend(words)
            continue
        if head in READ_ONLY_COMMANDS:
            if _has_write_producing_option(words):
                opaque = True
                opaque_words.extend(words)
            continue
        if head in SIMPLE_MUTATORS:
            if not _mutator_options_are_understood(words):
                opaque = True
                opaque_words.extend(words)
                continue
            kind = SIMPLE_MUTATION
            targets.extend(arguments)
            continue
        opaque = True
        opaque_words.extend(words)

    if opaque and kind != SIMPLE_MUTATION:
        return OPAQUE, targets, effective_cwd, opaque_words
    return kind, targets, effective_cwd, opaque_words


def evaluate_bash(
    command: str, root: str, cwd: str | None, environ: dict
) -> tuple[bool, str]:
    """Apply the Bash policy. Returns ``(deny, reason)``."""
    expanded = _expand_known_env(command, environ)
    kind, targets, effective_cwd, opaque_words = classify_bash(expanded, root, cwd)

    if kind == READ_ONLY:
        return False, ""

    for word in opaque_words:
        # An opaque command naming a canonical path establishes canonical
        # reachability even though its option grammar is not modelled here.
        # This is what keeps `sed -i … canon/world/f.md`, `dd of=canon/…`,
        # `chmod … canon/…` and `cp --target-directory=canon/world` denied
        # now that opacity alone no longer denies.
        #
        # Scanned as path-shaped runs rather than whole words, because a
        # literal target is routinely embedded in a larger token: the whole
        # word of `python3 -c "open('canon/world/f.md','w')…"` is not a path,
        # while the run `canon/world/f.md` inside it plainly is.
        for candidate in _PATH_RUNS.findall(word):
            if is_inside_canon(candidate, root, effective_cwd):
                return True, _reason("<command naming a path inside canon/>")

    if kind == SIMPLE_MUTATION and _has_unresolved_indirection(expanded, environ):
        # A known write whose destination is missing: canon cannot be ruled
        # out. This is not the old opacity rule — the command is established
        # to write, and only where is unknown.
        return True, _reason("<mutation with unresolved path indirection>")

    if effective_cwd and is_inside_canon(effective_cwd, root):
        # Reached only when the command is not read-only, so a relative write
        # would land in canon. `cd canon && cat f` never gets here.
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
