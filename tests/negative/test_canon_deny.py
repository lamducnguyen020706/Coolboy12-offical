"""Rejection proofs for the Artifact 022 canon write-deny hook.

Artifact 022's ``Done`` condition is *"deny proven by negative test"*, and the
Roadmap treats negative testing as first-class: a prohibition asserted without
a proof of rejection does not belong in this suite. So the denial is exercised
here as a real subprocess against the real hook, not described.

The hook is invoked exactly as Claude Code invokes it — JSON payload on stdin,
exit status read back — so what these tests prove is the actual contract:
**exit 2 denies, exit 0 allows.**

No test writes anything under ``canon/**``. Artifact 017 §13 rule 9 makes an
empty ``canon/**`` legal before any canonical gate and real canonical data
before a gate illegal; the artifact under test exists to stop exactly the write
these tests must not perform. Every fixture lives in a temporary directory.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

# tests/negative/test_canon_deny.py -> parents[2] is the repository root.
# Audited against the real tree rather than assumed: parents[1] is tests/ and
# holds no hook.
REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_HOOK = REPO_ROOT / ".claude/hooks/canon_deny.py"

DENY = 2
ALLOW = 0


def build_workspace(root: Path) -> Path:
    """Lay out a repository-shaped tree and install the real hook inside it.

    The production hook derives its protected root from its own ``__file__``,
    so a test that spoofed the root through an environment variable would be
    proving a mechanism the hook no longer uses. Copying the artifact into the
    temporary tree exercises the real derivation instead.
    """
    (root / ".claude/hooks").mkdir(parents=True, exist_ok=True)
    for zone in ("world", "epistemic", "production", "registry", "visual", "issue"):
        (root / "canon" / zone).mkdir(parents=True, exist_ok=True)
    for plain in ("docs", "src", "canonical", "canon_backup"):
        (root / plain).mkdir(exist_ok=True)
    shutil.copy2(SOURCE_HOOK, root / ".claude/hooks/canon_deny.py")
    return root


@pytest.fixture(scope="module")
def workspace(tmp_path_factory):
    """An isolated repository whose installed hook guards its own canon."""
    return build_workspace(tmp_path_factory.mktemp("canon-deny-repo"))


def invoke(
    payload: dict, workspace: Path, extra_env: dict | None = None
) -> subprocess.CompletedProcess:
    """Run the workspace's own hook: JSON on stdin, exit status back.

    ``extra_env`` reaches the subprocess only, never the test process, so a
    shell-variable fixture cannot leak between tests. ``CLAUDE_PROJECT_DIR``
    is deliberately absent — the hook must not need it.
    """
    env = {"PATH": "/usr/bin:/bin", "PYTHONDONTWRITEBYTECODE": "1"}
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        [sys.executable, str(workspace / ".claude/hooks/canon_deny.py")],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=False,
        env=env,
    )


def write_payload(path: str, tool: str = "Write") -> dict:
    return {"tool_name": tool, "tool_input": {"file_path": path, "content": "x"}}


# --------------------------------------------------------------------------
# The proof Artifact 022 exists for.
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "target",
    [
        "canon/test.md",
        "canon/world/test.md",
        "canon/registry/test.json",
        "canon/epistemic/test.md",
        "canon/production/test.md",
        "canon/visual/test.md",
        "canon/issue/test.md",
    ],
)
def test_direct_write_into_canon_is_denied(target, workspace):
    """Val — a direct write to ``canon/**`` is denied, across every zone.

    Artifact 017 §4 declares the family and its six model subtrees; guarding
    the family root covers all of them, ``canon/registry/**`` included.
    """
    result = invoke(write_payload(target), workspace)

    assert result.returncode == DENY, f"{target} was not denied"
    assert "Direct writes to canon/** are prohibited" in result.stderr


@pytest.mark.parametrize("tool", ["Write", "Edit", "NotebookEdit", "MultiEdit"])
def test_every_write_tool_is_covered(tool, workspace):
    """The boundary is the path, not one particular tool."""
    assert (
        invoke(write_payload("canon/world/test.md", tool), workspace).returncode == DENY
    )


@pytest.mark.parametrize(
    "target",
    [
        "./canon/test.md",
        "./canon/world/test.md",
        "docs/../canon/test.md",
        "somewhere/../canon/test.md",
        "canon/world/../world/test.md",
        "canon//world//test.md",
    ],
)
def test_normalization_does_not_permit_a_bypass(target, workspace):
    """Traversal and redundant separators are normalized before the decision."""
    assert invoke(write_payload(target), workspace).returncode == DENY, target


def test_absolute_path_into_canon_is_denied(workspace):
    """An absolute target is resolved against the same boundary."""
    assert (
        invoke(
            write_payload(str(workspace / "canon/world/test.md")), workspace
        ).returncode
        == DENY
    )


def test_symlink_into_canon_is_denied(workspace, tmp_path):
    """A link pointing into the canonical tree is not a way in.

    realpath resolves the link, so arriving at canon under another name is
    still arriving at canon.
    """
    link = workspace / "sneaky"
    if not link.exists():
        link.symlink_to(workspace / "canon", target_is_directory=True)

    assert invoke(write_payload("sneaky/world/test.md"), workspace).returncode == DENY


def test_deletion_of_canon_is_denied(workspace):
    """Artifact 017 §13 rule 8 — filesystem deletion is not retirement."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "rm -rf canon/world/test.md"},
    }

    assert invoke(payload, workspace).returncode == DENY


@pytest.mark.parametrize(
    "command",
    [
        "echo x > canon/world/test.md",
        "echo x >> canon/registry/test.json",
        "mv somewhere canon/world/test.md",
        "cp a.md canon/world/test.md",
        "touch canon/world/test.md",
        "sed -i s/a/b/ canon/world/test.md",
        "tee canon/world/test.md",
    ],
)
def test_shell_mutation_of_canon_is_denied(command, workspace):
    """A shell redirect is a direct write like any other."""
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    [
        "cd canon && echo x > world/f.md",
        "( cd canon/world && touch f.md )",
        "python3 -c \"open('canon/world/f.md','w').write('x')\"",
        "perl -e 'open(F,\">canon/world/f\")'",
        "ruby -e 'File.write(\"canon/world/f\", 1)'",
        "node -e 'fs.writeFileSync(\"canon/world/f\")'",
        "git checkout canon/world",
        "git rm canon/world/test.md",
    ],
)
def test_shell_bypass_attempts_are_denied(command, workspace):
    """Adversarial cases found by attacking this hook, locked in as regressions.

    A blocklist of mutating verbs missed every one of these: ``cd canon &&``
    hides the path from a ``canon/`` match, and an interpreter reaches the
    filesystem without naming ``rm`` or ``mv``. The allowlist denies anything
    that is not a recognized read-only command.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


def test_resolvable_env_var_into_canon_is_denied(workspace):
    """§17 — ``cd "$CANON" && touch`` resolves into canon and is denied."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": 'cd "$CANON" && touch world/test.md'},
    }
    env = {"CANON": str(workspace / "canon")}

    assert invoke(payload, workspace, env).returncode == DENY


def test_braced_env_var_into_canon_is_denied(workspace):
    """``${CANON}`` is the same indirection in another spelling."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": 'cd "${CANON}" && echo x > test.md'},
    }
    env = {"CANON": str(workspace / "canon" / "world")}

    assert invoke(payload, workspace, env).returncode == DENY


@pytest.mark.parametrize(
    "command",
    [
        'cd "$UNKNOWN_DIR" && touch test.md',
        'cd "$(resolve_target)" && touch test.md',
        "cd `resolve_target` && touch test.md",
        'cp a.md "$DEST"',
        'rm -rf "${TARGET_DIR}"',
    ],
)
def test_unresolved_indirection_in_a_mutation_fails_closed(command, workspace):
    """§9 — unknown is unsafe.

    The hook cannot know where an undefined variable or an unexecuted command
    substitution points, so it cannot prove the target is outside canon. It
    must not resolve the unknown to empty and continue.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


def test_mutation_while_cwd_is_inside_canon_is_denied(workspace):
    """§13 — a relative mutation is not safe just because it omits "canon".

    Enforced twice over, by design: the explicit working-directory guard, and
    the fact that bare tokens resolve against ``cwd`` and so land in canon too.
    Mutation-tested — disabling either mechanism alone still denies; disabling
    both fails this test.
    """
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "touch test.md"},
        "cwd": str(workspace / "canon" / "world"),
    }

    assert invoke(payload, workspace).returncode == DENY


def test_read_while_cwd_is_inside_canon_is_allowed(workspace):
    """§14 — the distinction is mutation, not the working directory."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "cat test.md"},
        "cwd": str(workspace / "canon" / "world"),
    }

    assert invoke(payload, workspace).returncode == ALLOW


def test_opaque_interpreter_hiding_its_target_is_denied(workspace):
    """§27 — the most important regression in this file.

    The old heuristic asked "can I find a canonical path in this text?" and
    allowed the command when it could not. An interpreter defeats that
    outright: the target is assembled inside program logic the command line
    never exposes. The three-class policy denies it because the command is
    opaque, not because a canonical token was spotted.
    """
    command = (
        'python3 -c "import os;'
        "open(os.environ['CANON']+'/world/test.md','w').write('x')\""
    )
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}
    env = {"CANON": str(workspace / "canon")}

    result = invoke(payload, workspace, env)

    assert result.returncode == DENY, "interpreter bypass returned ALLOW"
    assert "opaque" in result.stderr


@pytest.mark.parametrize(
    "command",
    [
        "python3 -c \"open('/dynamic/path','w')\"",
        "python3 script.py",
        "node -e \"fs.writeFileSync('x')\"",
        "ruby -e \"File.write('x', 1)\"",
        "perl -e \"open(F,'>x')\"",
        "bash -c 'touch anything'",
        "sh -c 'touch anything'",
        "make install",
        "npm run build",
    ],
)
def test_opaque_execution_is_denied_without_naming_canon(command, workspace):
    """§7 — opacity alone is the ground for denial.

    None of these names ``canon``. The hook cannot establish what any of them
    writes without running it, so none can be proven outside the boundary.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


def test_opaque_denial_is_not_a_read_firewall(workspace):
    """The asymmetry is deliberate, and worth stating in a test.

    ``cat`` is allowed against canon because it is *recognized* read-only.
    ``python3`` is denied even when it only reads, because the hook cannot
    tell. That is a refusal to certify opaque execution, not a read block.
    """
    read = {"tool_name": "Bash", "tool_input": {"command": "cat canon/PURPOSE.md"}}
    opaque = {"tool_name": "Bash", "tool_input": {"command": "python3 reader.py"}}

    assert invoke(read, workspace).returncode == ALLOW
    assert invoke(opaque, workspace).returncode == DENY


def test_mutation_denied_when_any_of_several_targets_is_canonical(workspace):
    """§21 — one safe target does not redeem the command."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "cp src/a docs/a canon/world/a"},
    }

    assert invoke(payload, workspace).returncode == DENY


@pytest.mark.parametrize("command", ["rm -rf canon", "mv x canon"])
def test_the_canon_root_itself_is_protected(command, workspace):
    """§25 — the boundary is the family root, not only its six subtrees."""
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


def test_environment_variable_cannot_relocate_the_protected_root(tmp_path):
    """§28 — the trust boundary comes from the hook's own location.

    A decoy directory that also contains ``.claude/`` and ``canon/`` is fed in
    as ``CLAUDE_PROJECT_DIR``. The real repository's canon must stay guarded:
    an environment variable that could move the boundary would be a way to
    move the guard off the thing it guards.
    """
    real = build_workspace(tmp_path / "realrepo")
    decoy = tmp_path / "fake"
    (decoy / ".claude").mkdir(parents=True)
    (decoy / "canon").mkdir()

    # The target is absolute and inside the *real* repository's canon. A
    # relative target would prove nothing here: it lands in whichever canon
    # the hook picked, so it denies either way. Only an absolute path
    # distinguishes the two roots.
    target = str(real / "canon/world/test.md")
    result = subprocess.run(
        [sys.executable, str(real / ".claude/hooks/canon_deny.py")],
        input=json.dumps(write_payload(target)),
        text=True,
        capture_output=True,
        check=False,
        env={"PATH": "/usr/bin:/bin", "CLAUDE_PROJECT_DIR": str(decoy)},
    )

    assert result.returncode == DENY, "CLAUDE_PROJECT_DIR relocated the boundary"


@pytest.mark.parametrize(
    ("payload", "label"),
    [
        ({"tool_name": "Write", "tool_input": {"content": "x"}}, "Write without path"),
        ({"tool_name": "Edit", "tool_input": {"old": "a"}}, "Edit without path"),
        ({"tool_name": "MultiEdit", "tool_input": {}}, "MultiEdit without path"),
        ({"tool_name": "Bash", "tool_input": {}}, "Bash without command"),
        ({"tool_name": "Bash", "tool_input": {"command": "   "}}, "Bash blank command"),
    ],
)
def test_unevaluable_known_write_actions_fail_closed(payload, label, workspace):
    """§17 — a known write-capable tool with no usable target is denied."""
    assert invoke(payload, workspace).returncode == DENY, label


@pytest.mark.parametrize(
    "raw", ["", "   ", "{not json", "[1,2,3]", '"a string"', "null"]
)
def test_unevaluable_stdin_fails_closed(raw, workspace):
    """§29 — empty, malformed and non-object payloads all deny."""
    result = subprocess.run(
        [sys.executable, str(workspace / ".claude/hooks/canon_deny.py")],
        input=raw,
        text=True,
        capture_output=True,
        check=False,
        env={"PATH": "/usr/bin:/bin"},
    )

    assert result.returncode == DENY, repr(raw)
    assert "Traceback" not in result.stderr


def test_unrelated_tool_is_not_denied(workspace):
    """§18/§30 — Artifact 022 is not a general tool-authorization layer.

    A tool outside the write/read/Bash enforcement set carries no canonical
    write responsibility, and inventing a denial for it would quietly turn
    this artifact into something the Roadmap did not ask for.
    """
    payload = {
        "tool_name": "WebFetch",
        "tool_input": {"url": "https://example.invalid"},
    }

    assert invoke(payload, workspace).returncode == ALLOW


@pytest.mark.parametrize(
    "command",
    [
        "sort -o canon/world/out.txt input.txt",
        "sort --output=canon/world/out.txt input.txt",
        "git diff --output=canon/world/out.patch",
        "git diff --output canon/world/out.patch",
    ],
)
def test_read_only_command_with_output_option_is_denied(command, workspace):
    """§27 — membership in the read-only list is not enough on its own.

    ``sort`` inspects, but ``sort -o`` writes; ``git diff`` inspects, but
    ``git diff --output=`` writes. Classifying on the executable name alone
    let both through. A write-producing option makes the invocation opaque.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


def test_output_option_is_denied_even_outside_canon(workspace):
    """The refusal is of the syntax, not of the destination.

    Artifact 022 does not need to support advanced output options, so it
    declines to parse them rather than risk reading one wrong. §24 accepts
    this false refusal explicitly: avoiding false negatives is the goal.
    """
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "sort -o docs/out.txt in.txt"},
    }

    assert invoke(payload, workspace).returncode == DENY


@pytest.mark.parametrize(
    "command",
    [
        "cp --target-directory=canon/world src/a",
        "cp -t canon/world src/a",
        "install --target-directory=canon/world src/a",
        "ln --target-directory=canon/world src/a",
        "cp --target-directory=docs src/a",
    ],
)
def test_mutator_option_syntax_cannot_create_a_bypass(command, workspace):
    """§25 — an option can move where a mutator writes.

    ``--target-directory=`` and ``-t`` send the write somewhere the positional
    arguments never name, so extracting positional targets missed it entirely.
    Only plainly harmless flags keep a mutator classified; anything else is
    opaque, including the last case, whose destination is outside canon.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    [
        "install -m 644 src/a canon/world/a",
        "dd if=src/a of=canon/world/a",
        "truncate -s 0 canon/world/a",
        "chmod 777 canon/world/a",
        "chown root canon/world/a",
        "ln -s src/a canon/world/a",
        "sed -i s/a/b/ canon/world/test.md",
    ],
)
def test_option_rich_commands_are_opaque_not_mutators(command, workspace):
    """§13-§17 — commands needing a real CLI parser are deliberately opaque.

    ``dd``'s ``of=``, ``install``'s many forms and ``sed``'s in-place flag all
    require option semantics this hook has no business implementing. Removing
    them from the mutator set shrinks the classifier's attack surface; each
    now falls through to opaque and is denied.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    ["rm -rf docs/x", "mkdir -p docs/sub", "cp -a src/a docs/a", "mv src/a docs/a"],
)
def test_harmless_mutator_flags_still_classify(command, workspace):
    """The option allowlist must not turn every flag into a denial.

    Without this control, tightening option handling would quietly make the
    simple-mutation class unreachable and the policy a blanket write firewall.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


def test_sort_without_output_option_still_reads(workspace):
    """``sort input.txt`` inspects and stays allowed."""
    payload = {"tool_name": "Bash", "tool_input": {"command": "sort canon/PURPOSE.md"}}

    assert invoke(payload, workspace).returncode == ALLOW


# --------------------------------------------------------------------------
# The hook must not become a read firewall or a general write blocker.
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "target",
    [
        "docs/test.md",
        "src/test.py",
        "tests/test_x.py",
        ".claude/hooks/canon_deny.py",
        "derived/indexes/x.json",
    ],
)
def test_non_canonical_writes_are_allowed(target, workspace):
    """Artifact 022 blocks one boundary, not ordinary development."""
    assert invoke(write_payload(target), workspace).returncode == ALLOW, target


@pytest.mark.parametrize(
    "target", ["canonical/test.md", "canon_backup/test.md", "canonized.md"]
)
def test_prefix_lookalikes_are_not_inside_canon(target, workspace):
    """``canonical/`` and ``canon_backup/`` share a prefix, not a boundary.

    Guards against string-prefix logic, which would produce false denials.
    """
    assert invoke(write_payload(target), workspace).returncode == ALLOW, target


@pytest.mark.parametrize(
    "command",
    [
        "echo x > docs/test.md",
        "touch src/test.py",
        "cp a.md docs/test.md",
        "rm docs/x.md",
    ],
)
def test_shell_mutation_outside_canon_is_allowed(command, workspace):
    """§21 — the conservative policy still permits ordinary development.

    Without this control the Bash rule could degenerate into "any mutation is
    denied", which would be a general write firewall rather than Artifact 022.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


def test_traversal_out_of_canon_is_allowed(workspace):
    """``canon/../elsewhere`` normalizes to outside the zone, so it loads."""
    assert invoke(write_payload("canon/../elsewhere.md"), workspace).returncode == ALLOW


@pytest.mark.parametrize("tool", ["Read", "Glob", "Grep", "NotebookRead"])
def test_reads_of_canon_are_allowed(tool, workspace):
    """READ canon/** is allowed — Artifact 022 is not a read firewall."""
    payload = {"tool_name": tool, "tool_input": {"file_path": "canon/world/test.md"}}

    assert invoke(payload, workspace).returncode == ALLOW


@pytest.mark.parametrize(
    "command",
    [
        "cat canon/PURPOSE.md",
        "grep -r x canon/",
        "ls canon/world/",
        "find canon -type f",
        "head -5 canon/world/a.md",
        "cat canon/PURPOSE.md 2>/dev/null",
        "grep -r x canon/ 2>&1",
        "git status canon/",
        "git log -- canon/world/",
        "diff canon/world/a.md canon/world/b.md",
        "wc -l canon/PURPOSE.md",
    ],
)
def test_shell_reads_of_canon_are_allowed(command, workspace):
    """Inspecting canon from the shell stays possible.

    The stderr-redirect and read-only-git cases are regressions: an earlier
    draft treated ``2>/dev/null`` as a write redirect and ``git`` as a
    mutating verb, denying ordinary reads that Artifact 017 never prohibits.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


# --------------------------------------------------------------------------
# Failure behaviour and boundary of the artifact.
# --------------------------------------------------------------------------


def test_write_tool_with_unresolvable_path_mentioning_canon_fails_closed(workspace):
    """Ambiguity resolves toward refusing, not toward permitting a write."""
    payload = {"tool_name": "Write", "tool_input": {"target": "canon/world/test.md"}}

    assert invoke(payload, workspace).returncode == DENY


def test_malformed_payload_fails_closed(workspace):
    """A payload the hook cannot parse is denied, not permitted.

    Changed from allow to deny by the hard audit: an unevaluable target is
    exactly the case this artifact exists to stop, so *unknown* must never
    become *safe*. Still no stack trace — a policy denial is not a crash.
    """
    result = subprocess.run(
        [sys.executable, str(workspace / ".claude/hooks/canon_deny.py")],
        input="{not json",
        text=True,
        capture_output=True,
        check=False,
        env={"PATH": "/usr/bin:/bin"},
    )

    assert result.returncode == DENY
    assert "Traceback" not in result.stderr
    assert "unreadable hook payload" in result.stderr


def test_denial_message_does_not_echo_payload_content(workspace):
    """The reason names the boundary; it does not dump tool input."""
    secret = "PLACEHOLDER-NOT-A-REAL-SECRET-c3d4e5f6"
    payload = {
        "tool_name": "Write",
        "tool_input": {"file_path": "canon/world/test.md", "content": secret},
    }

    result = invoke(payload, workspace)

    assert result.returncode == DENY
    assert secret not in result.stderr


def test_hook_writes_nothing_anywhere(workspace):
    """Artifact 022 enforces; it never creates, including under canon/**."""
    before = {str(p.relative_to(workspace)) for p in workspace.rglob("*")}

    invoke(write_payload("canon/world/test.md"), workspace)
    invoke(write_payload("docs/test.md"), workspace)

    assert {str(p.relative_to(workspace)) for p in workspace.rglob("*")} == before


def test_hook_holds_no_mutation_or_registry_machinery():
    """Boundary guard: 022 is not 152, not the Human Gate, not a validator."""
    source = SOURCE_HOOK.read_text(encoding="utf-8")
    body = source.split('"""', 2)[-1]

    for forbidden in (
        "def write_canon",
        "def commit",
        "human_gate",
        "HistoryRecord",
        "wsv",
        "CreativeMemory",
    ):
        assert forbidden.lower() not in body.lower(), forbidden

    assert "import zones" not in body
    assert "zones.json" not in body
