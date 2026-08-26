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
Artifact 022 never decides whether a mutation is *legitimate*, and it does
not decide whether a command is safe. It answers exactly one question, by
static inspection, without executing anything::

    does this invocation establish a write target under canon/** ?

        identifiable write into canon/**        → deny
        identifiable write outside canon/**     → allow
        recognized read-only operation          → allow
        known mutation, destination unresolved  → deny
        no canonical write established          → allow
        malformed or unevaluable write request  → deny

**This hook denies identifiable writes into ``canon/**``. It does not deny a
command merely because it cannot fully understand that command's internal
semantics.**

Two of those lines look similar and are not. A **known mutation with an
unresolved destination** — ``cp "$UNKNOWN" "$DEST"`` — is denied because the
command is established to write and only *where* is missing, so canon cannot
be ruled out. A command that establishes **no canonical write** is allowed;
the accurate phrasing for that outcome is *no canonical write established by
this hook*, never *safe*. The hook has not certified the command, and is not
asked to.

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
  does ``git diff --output=out.patch``. The option's value is read as the
  destination, so each is judged on where it points rather than refused for
  its syntax.
* A mutator carrying an option this hook does not recognize is opaque.
  ``cp src dst`` has readable targets; ``cp --target-directory=canon/world
  src`` writes somewhere the positional arguments never name. Only a small
  set of plainly harmless flags (``-r``, ``-f``, ``-p``, ``-v``, ``-a``,
  ``-n``, ``-d`` and their long forms) keeps a mutator classified.
* ``sed``, ``ln``, ``install``, ``dd``, ``chmod``, ``chown`` and ``truncate``
  are deliberately **not** mutators here. Each has option-rich semantics that
  would need a real CLI parser to judge, so each is opaque — and each is
  still denied when it names a canonical destination positionally, which is
  the form all of them use.

The opaque class is not a claim that those programs write. It is the
admission that this hook cannot tell, which is why the class alone decides
nothing.

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

What counts as a write target
------------------------------
A path earns target status from its **shell-level position**, never from
appearing somewhere in the text:

* a **redirect destination** — ``>``, ``>>``, ``1>``, ``1>>``, ``&>``. File
  descriptor 2 is diagnostics, and ``>&1`` duplicates a descriptor, so
  neither is a destination;
* a **positional argument of one of the seven mutators**;
* the value of a **modelled write-producing option** — ``-o``, ``--output``,
  ``-t``, ``--target-directory``, in either spelling — on any command;
* a **positional argument of a command known to write where it is pointed**:
  :data:`POSITIONAL_WRITERS` (``sed``, ``ln``, ``install``, ``dd``,
  ``chmod``, ``chown``, ``truncate``) and git's working-tree subcommands
  (:data:`GIT_WRITE_SUBCOMMANDS`). Their option grammars stay unmodelled and
  they stay opaque; only the destination is read;
* any of the above resolved against a working directory inside canon.

Everything else is an input, not a destination. A positional path given to a
command that is **not** on those lists is not a target: ``pytest
canon/world``, ``python3 canon/world/script.py`` and ``node
canon/world/s.js`` all name a canonical path and none of them writes one. Nor
does an unmodelled option or a value joined to one — ``pytest
--rootdir=canon``.

**Quoting is not part of this decision.** Quotes set word boundaries and are
then discarded, so ``touch "canon/world/f.md"`` is judged exactly as
``touch canon/world/f.md`` is, and ``sort --output="canon/world/out"`` as
``sort --output=canon/world/out``. Treating a quoted word as automatically
safe was a real bypass: every :data:`POSITIONAL_WRITERS` command and every
git working-tree subcommand could be handed a quoted canonical path and pass.
What keeps ``python3 -c "print('canon/world/x.md')"``, ``echo
"canon/world/x.md"``, ``grep -e 'canon/world/x.md' f`` and ``git commit -m
'deny writes to canon/world'`` allowed is that none of those commands writes
where it is pointed — the command decides, not the quotes.

Residual risk, stated rather than papered over
-----------------------------------------------
The cost of that precision is stated plainly: **a canonical path inside a
quoted argument is not inspected, so an interpreter one-liner can write into
canon unseen.** ``python3 -c "open('canon/world/f.md','w').write('x')"`` is
allowed, and so is the ``os.environ['CANON']`` form that computes the path at
run time. Separating that from ``print('canon/world/x.md')`` requires
interpreting the program, and this hook must not interpret program source —
so it does not pretend to. The shell-level forms of the same write are all
caught.

That residual is what I-83 and I-100 already anticipate: "execution-substrate
guard rails are defence-in-depth, **never constitutional authority**". The
constitutional guarantee is the Mutation Coordinator and the Human Gate
(artifact 152), not this file. §26.8 says the same from the other side — "if
the hook and the Human Gate ever disagree, the gate is right and the hook is
a bug".

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
POSITIONAL_WRITERS = frozenset(
    {"sed", "ln", "install", "dd", "chmod", "chown", "truncate"}
)
"""Opaque commands that write to the paths they are handed positionally.

Deliberately **not** promoted into :data:`SIMPLE_MUTATORS`: their option
grammars stay unmodelled and they remain in the opaque class. This set says
only that a positional path given to one of them is a destination, which is
what keeps ``sed -i … canon/world/f.md`` and ``chmod … canon/world/f.md``
denied while ``pytest canon/world`` and ``python3 canon/world/s.py`` — whose
positional paths are inputs — are not.
"""

GIT_WRITE_SUBCOMMANDS = frozenset({"rm", "mv", "checkout", "restore", "clean", "apply"})
"""Git subcommands that rewrite working-tree files at the paths they name."""


def extract_write_redirect_targets(command: str) -> tuple[list[str], str]:
    """Pull file-write redirect destinations out of a command.

    :returns: ``(destinations, remainder)`` — the remainder is the command
        with those redirects removed, so a destination is never also read as
        a positional argument.

    Replaces two regexes that could not tell a file descriptor from a
    destination. The old stderr pattern was ``\\d+>\\s*\\S+``, which matched
    ``1>canon/world/f.md`` as readily as ``2>/dev/null`` and stripped it
    before the write scan ran — a real bypass, not a false positive.

    What counts here is the descriptor being redirected:

    * ``>`` ``>>`` ``1>`` ``1>>`` ``&>`` — a file destination;
    * ``2>`` ``2>>`` — diagnostics, not a destination this hook guards;
    * ``>&1`` ``2>&1`` ``2>&-`` — descriptor duplication or close, no file.

    Quote-aware, so a ``>`` inside a quoted argument is text, not syntax.
    Not a shell parser: it understands redirection and nothing else.
    """
    targets: list[str] = []
    kept: list[str] = []
    quote: str | None = None
    index = 0
    length = len(command)

    while index < length:
        char = command[index]

        if quote:
            kept.append(char)
            if char == quote:
                quote = None
            index += 1
        elif char == "\\" and index + 1 < length:
            kept.extend(command[index : index + 2])
            index += 2
        elif char in "\"'":
            quote = char
            kept.append(char)
            index += 1
        elif char == ">":
            descriptor = ""
            while kept and kept[-1].isdigit():
                descriptor = kept.pop() + descriptor
            if kept and kept[-1] == "&":  # &> — both streams to one file
                kept.pop()
            index += 1
            if index < length and command[index] == ">":
                index += 1
            while index < length and command[index] in " \t":
                index += 1
            if index < length and command[index] == "&":
                index += 1  # >&1, 2>&1, 2>&- : a descriptor, never a file
                while index < length and (command[index].isdigit() or command[index] == "-"):
                    index += 1
                continue
            target, inner = [], None
            while index < length:
                char = command[index]
                if inner:
                    if char == inner:
                        inner = None
                    else:
                        target.append(char)
                elif char in "\"'":
                    inner = char
                elif char.isspace() or char in ";|&()":
                    break
                else:
                    target.append(char)
                index += 1
            destination = "".join(target)
            if destination and descriptor != "2":
                targets.append(destination)
        else:
            kept.append(char)
            index += 1

    return targets, "".join(kept)

_SEGMENT_SEPARATORS = ";|&`()"

def _tokenize(segment: str) -> list[str]:
    """Split one segment into words, respecting quotes and dropping them.

    Quote-aware for the same reason :func:`_split_segments` is, one level
    down: a quoted run holds together across whitespace, so
    ``-m 'deny writes to canon/world'`` is two words rather than five.

    Quoting affects **word boundaries only**. It deliberately does not mark a
    word as non-target: ``touch "canon/world/f.md"`` writes exactly where
    ``touch canon/world/f.md`` does, and the shell's quotes are parsing
    syntax, not a change of meaning. Which arguments are destinations is
    decided by command context in :func:`identify_canonical_write_targets`.
    """
    tokens: list[str] = []
    current: list[str] = []
    quote: str | None = None
    started = False

    index = 0
    while index < len(segment):
        char = segment[index]
        if char == "\\" and index + 1 < len(segment) and quote != "'":
            # Escapes everywhere except inside single quotes, matching
            # _split_segments so both layers read the same string the same way.
            current.append(segment[index + 1])
            started = True
            index += 2
            continue
        index += 1
        if quote:
            if char == quote:
                quote = None
            else:
                current.append(char)
        elif char in "\"'":
            quote, started = char, True
        elif char.isspace():
            if started:
                tokens.append("".join(current))
            current, started = [], False
        else:
            current.append(char)
            started = True

    if started:
        tokens.append("".join(current))
    return tokens


def identify_canonical_write_targets(tokens: list[str]) -> list[str]:
    """Write targets visible at the *shell* level in one opaque invocation.

    Answers only "which paths does this invocation hand a command as a
    destination?" — never "what might this program do?". The hook does not
    parse Python, JavaScript, or any command's full option grammar, so an
    argument earns target status only from shell-level position:

    * the value of a **modelled** write-producing option (``-o``,
      ``--output``, ``-t``, ``--target-directory``), in both the separated
      and ``=``-joined spellings, on any command;
    * a **positional** word — not an option — when the command is one that
      writes where it is pointed: :data:`POSITIONAL_WRITERS`, or git with a
      :data:`GIT_WRITE_SUBCOMMANDS` subcommand. The right-hand side of an
      unprefixed ``key=value`` counts too, which is how ``dd if=… of=…``
      names its destination.

    Everything else is an input rather than a destination:

    * a positional word of any **other** command. ``pytest canon/world``,
      ``python3 canon/world/script.py`` and ``node canon/world/s.js`` each
      name a canonical path; none writes to it.
    * an **unmodelled option**, and any value joined to it. ``pytest
      --rootdir=canon`` selects a directory to search, not one to write.

    **Quoting decides nothing here.** Quotes are word boundaries, stripped by
    :func:`_tokenize` before this runs, so ``chmod 644 "canon/world/f.md"``
    is read exactly as its unquoted twin. An earlier version treated a quoted
    word as automatically non-target, which let every positional writer and
    every git working-tree subcommand through on a quoted path.

    The residual this leaves is program-internal: ``python3 -c
    "open('canon/world/x','w')"`` hands ``python3`` one argument that this
    hook does not interpret, and ``python3`` is not a positional writer.
    """
    targets: list[str] = []
    if not tokens:
        return targets

    head = os.path.basename(tokens[0]).lower()
    arguments = [text for text in tokens[1:] if not text.startswith("-")]
    writes_positionally = head in POSITIONAL_WRITERS or (
        head == "git" and arguments and arguments[0] in GIT_WRITE_SUBCOMMANDS
    )
    expect_value = False

    for text in tokens[1:]:  # [0] is the program name
        if expect_value:
            targets.append(text)
            expect_value = False
        elif text in WRITE_PRODUCING_OPTIONS:
            expect_value = True
        elif text.startswith(WRITE_PRODUCING_PREFIXES):
            targets.append(text.split("=", 1)[1])
        elif text.startswith("-"):
            continue
        elif writes_positionally:
            targets.append(text.split("=", 1)[-1])

    return targets


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
) -> tuple[str, list[str], str | None, list[str]]:
    """Sort a command into one of the three classes.

    :returns: ``(class, targets, effective_cwd)``. ``targets`` are the paths a
        simple mutation would touch; ``effective_cwd`` accounts for any ``cd``
        the command performs first.

    ``cd`` is neither read-only nor mutating on its own — it relocates the
    directory later segments act in, which is why ``cd canon && touch f`` is
    caught even though ``touch f`` names nothing canonical.
    """
    targets, remainder = extract_write_redirect_targets(command)
    kind = SIMPLE_MUTATION if targets else READ_ONLY
    effective_cwd = cwd
    opaque = False
    opaque_targets: list[str] = []

    # Every segment is scanned, including those after an opaque one. Returning
    # early on the first opaque head would abandon the rest of the command, so
    # `python3 build.py && touch canon/world/f` would have its canonical target
    # collected only if the interpreter came second.
    for segment in _split_segments(remainder):
        words = _tokenize(segment)
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
            opaque_targets.extend(identify_canonical_write_targets(words))
            continue
        if head in READ_ONLY_COMMANDS:
            if _has_write_producing_option(words):
                opaque = True
                opaque_targets.extend(identify_canonical_write_targets(words))
            continue
        if head in SIMPLE_MUTATORS:
            if not _mutator_options_are_understood(words):
                opaque = True
                opaque_targets.extend(identify_canonical_write_targets(words))
                continue
            kind = SIMPLE_MUTATION
            targets.extend(arguments)
            continue
        opaque = True
        opaque_targets.extend(identify_canonical_write_targets(words))

    if opaque and kind != SIMPLE_MUTATION:
        return OPAQUE, targets, effective_cwd, opaque_targets
    return kind, targets, effective_cwd, opaque_targets


def evaluate_bash(
    command: str, root: str, cwd: str | None, environ: dict
) -> tuple[bool, str]:
    """Apply the Bash policy. Returns ``(deny, reason)``."""
    expanded = _expand_known_env(command, environ)
    kind, targets, effective_cwd, opaque_targets = classify_bash(expanded, root, cwd)

    if kind == READ_ONLY:
        return False, ""

    for target in opaque_targets:
        # A destination handed to a command whose option grammar is not
        # modelled here: `sed -i … canon/world/f.md`, `dd of=canon/…`,
        # `chmod … canon/…`, `cp --target-directory=canon/world`. Shell-level
        # position makes these targets; a canonical path merely *mentioned*
        # in a quoted argument is not one.
        if is_inside_canon(target, root, effective_cwd):
            return True, _reason("<command writing to a path inside canon/>")

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
