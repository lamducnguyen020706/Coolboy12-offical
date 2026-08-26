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
        "touch canon/world/file.txt",
        "mkdir canon/world/newdir",
        "mv src/a canon/world/a",
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
        "git checkout canon/world",
        "git rm canon/world/test.md",
    ],
)
def test_shell_bypass_attempts_are_denied(command, workspace):
    """Adversarial cases found by attacking this hook, locked in as regressions.

    A blocklist of mutating verbs missed every one of these: ``cd canon &&``
    hides the path from a ``canon/`` match, and ``git checkout``/``git rm``
    name the destination positionally after a subcommand that is not
    read-only. Each is caught by shell-level position, not by pattern.

    ``git checkout``/``git rm`` name their destination positionally after a
    subcommand that rewrites working-tree files, which is why those two are
    read as targets while ``git commit -m '… canon/world'`` is not.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    [
        "python3 -c \"open('canon/world/f.md','w').write('x')\"",
        "ruby -e 'File.write(\"canon/world/f\", 1)'",
        "node -e 'fs.writeFileSync(\"canon/world/f\")'",
        "perl -e 'open(F,\">canon/world/f\")'",
    ],
)
def test_interpreter_source_naming_canon_is_residual_risk(command, workspace):
    """The cost of removing the false positives, asserted rather than hidden.

    These write into ``canon/**`` and are **allowed**. The canonical path sits
    inside a quoted argument, and this hook does not inspect quoted arguments
    — that is precisely what stops ``python3 -c "print('canon/world/x.md')"``,
    ``echo "canon/world/x.md"`` and ``git commit -m '… canon/world'`` from
    being denied. Separating ``open(…, 'w')`` from ``print(…)`` inside that
    string requires interpreting the program, which Artifact 022 must not do.

    This is a real reduction in depth against a determined actor with shell
    access, and I-83 already scopes that: "execution-substrate guard rails are
    defence-in-depth, never constitutional authority". The constitutional
    guarantee is artifact 152 plus the Human Gate.

    The ``perl`` case joined this set when redirect detection became
    quote-aware. Its ``>`` sits inside the quoted program, so it was only ever
    caught by reading program text as shell syntax — the same confusion that
    made ``echo 'a > b'`` look like a write.

    Asserted as ALLOW deliberately. If a future change denies these, that is
    an improvement — re-point this test rather than deleting it.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


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


def test_interpreter_computing_its_own_path_is_documented_residual_risk(workspace):
    """CONFLICT-D — the boundary of what static inspection can establish.

    An interpreter assembles its target inside program logic the command line
    never exposes. The retired policy caught this by denying every opaque
    command, which also denied ``pytest``, ``git commit`` and ``ruff`` and
    halted the build (CONFLICT-D). Route 3 moved the decision axis to
    canonical reachability, and this construction establishes none.

    Recorded here as the honest limit of the guard rail rather than left as a
    silent gap.
    """
    command = (
        'python3 -c "import os;'
        "open(os.environ['CANON']+'/world/test.md','w').write('x')\""
    )
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}
    env = {"CANON": str(workspace / "canon")}

    result = invoke(payload, workspace, env)

    # RESIDUAL RISK, asserted deliberately rather than wished away.
    #
    # The canonical path here is assembled *inside Python source* at run time:
    # `os.environ['CANON']` is not shell syntax, so no textual expansion
    # reaches it, and no word of the command resolves under canon/. Proving
    # the target would mean interpreting arbitrary Python, which this hook
    # must never do. It therefore ALLOWS — and that gap is exactly what I-83
    # and I-100 describe as defence-in-depth's limit: "execution-substrate
    # guard rails are defence-in-depth, never constitutional authority". The
    # constitutional guarantee is artifact 152, not this file.
    #
    # The shell-variable form of the same attack IS caught — see
    # `test_resolvable_env_var_into_canon_is_denied`. This test
    # exists so that the boundary between the two is recorded and cannot be
    # narrowed by accident.
    assert result.returncode == ALLOW, (
        "the residual-risk contract changed; if this now denies, the fix is "
        "real and this test should be re-pointed at the new boundary"
    )


@pytest.mark.parametrize(
    "command",
    [
        "python3 -c \"open('/dynamic/path','w')\"",
        "python -c \"open('/dynamic/path','w')\"",
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
def test_opaque_execution_naming_no_canonical_path_is_allowed(command, workspace):
    """CONFLICT-D — opacity alone is **no longer** a ground for denial.

    None of these names a canonical path, so none establishes a write into
    ``canon/**``. Denying them was the rule that made ``pytest``, ``git
    commit`` and ``ruff`` unrunnable and blocked the build; Blueprint §26.8
    lists command execution *including tests* among the facilities the
    environment legitimately provides.

    This is the assertion that inverted under the approved Route 3 amendment.
    It is inverted deliberately, not relaxed to make a suite pass: the same
    commands aimed at a canonical path are still denied, one test below.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


@pytest.mark.parametrize(
    "command",
    [
        "sed -i s/a/b/ canon/world/test.md",
        "dd if=src/a of=canon/world/a",
        "chmod 644 canon/world/test.md",
        "chown root canon/world/test.md",
        "install src/a canon/world/test.md",
        "ln -s src/a canon/world/test.md",
        "truncate -s 0 canon/world/test.md",
        "python3 build.py > canon/world/out.txt",
        "python3 build.py 1>canon/world/out.txt",
        "some-tool --output=canon/world/out.txt",
        "some-tool -o canon/world/out.txt",
    ],
)
def test_opaque_command_writing_to_canon_is_denied(command, workspace):
    """The half that must not move: opaque, but the destination is visible.

    Each of these hands a canonical path to a command in a position that
    makes it a destination — a positional argument of a command that writes
    where it is pointed, a redirect, or a modelled output option. Dropping
    the blanket opaque denial must not let ``sed -i``, ``dd of=`` or
    ``chmod`` write canon unchallenged, and it does not.

    Their option grammars are still not modelled; only the destination is
    read. That is the difference from the commands below, whose positional
    paths are inputs.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    [
        "echo x > canon/world/f.md",
        "echo x >> canon/world/f.md",
        "echo x 1> canon/world/f.md",
        "echo x 1>> canon/world/f.md",
        "echo x 1>canon/world/f.md",
        "echo x 1>>canon/world/f.md",
        "echo x &> canon/world/f.md",
        "echo x > canon/world/f.md 2>&1",
        "cat a | tee -a canon/world/f.md",
    ],
)
def test_stdout_redirect_into_canon_is_denied(command, workspace):
    """The numeric-redirect bypass, fixed and pinned.

    The retired stderr pattern was ``\\d+>\\s*\\S+``. It matched
    ``1>canon/world/f.md`` exactly as readily as ``2>/dev/null`` and stripped
    it from the command before the write scan ran, so an explicit stdout
    redirect into canon returned ALLOW. A real bypass, and the reason
    descriptor handling is now explicit rather than pattern-matched.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    [
        "echo x 1> docs/f.md",
        "echo x 1>> docs/f.md",
        "echo x 1>docs/f.md",
        "echo x &> docs/f.md",
        "echo x > docs/out 2>&1",
        "cat canon/world/f.md 2>/dev/null",
        "cat canon/world/f.md 2>&1",
        "cat canon/world/f.md 2>&-",
        "grep x canon/world/f.md 2>/dev/null",
        "grep x canon/world/f.md 2>>/dev/null",
        "ls canon/world >&2",
    ],
)
def test_descriptor_handling_does_not_over_or_under_deny(command, workspace):
    """The counterpart: descriptor 2 and duplications are not destinations.

    Fixing the bypass must not make every ``2>/dev/null`` on a canonical read
    look like a canonical write. Descriptor 2 is diagnostics; ``>&1``,
    ``>&2`` and ``2>&-`` duplicate or close a descriptor and name no file at
    all. Stdout redirects that point outside canon stay allowed regardless of
    how they are spelled.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


@pytest.mark.parametrize(
    "command",
    [
        "pytest canon/world",
        "pytest --rootdir=canon",
        "python3 canon/world/script.py",
        "python3 script.py canon/world/test.md",
        "node canon/world/s.js",
        "ruby canon/world/s.rb",
        "make install canon/world/out",
        "cargo run canon/world",
    ],
)
def test_opaque_command_reading_a_canonical_path_is_allowed(command, workspace):
    """A path handed to a command is not thereby a place it writes.

    This is the false-positive class that a bare "any positional argument is
    a target" rule produced: a test path, a script to execute, a directory to
    search. None of them is a destination, and denying them would block
    ordinary work on the repository for no protective gain.

    The distinction is which command receives the path, not how the path
    looks. ``sed -i canon/world/f`` writes where it is pointed and is denied
    one test above; ``python3 canon/world/f`` executes what it is pointed at
    and is allowed here.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


def test_reads_of_canon_stay_allowed_however_they_are_spelled(workspace):
    """Artifact 017 restricts *writing* canon, not reading it.

    The retired policy denied an opaque command even when it only read, and
    an interim one denied any opaque command that merely named a canonical
    path — which came to the same thing for a reader. Both are gone: reading
    canon is allowed whether the reader is recognized (``cat``) or not
    (``python3``), and whether the path is an argument or the program itself.

    What still denies is a canonical *destination*, which is asserted in the
    two tests above rather than repeated here.
    """
    for command in (
        "cat canon/PURPOSE.md",
        "python3 reader.py",
        "python3 reader.py canon/PURPOSE.md",
        "python3 canon/world/reader.py",
        "cat canon/PURPOSE.md 2>/dev/null",
    ):
        payload = {"tool_name": "Bash", "tool_input": {"command": command}}
        assert invoke(payload, workspace).returncode == ALLOW, command


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
        "sort --output canon/world/out.txt input.txt",
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


def test_output_option_outside_canon_is_allowed(workspace):
    """The refusal is of the destination, not of the syntax.

    This inverted under Route 3. The retired rule denied ``sort -o`` wherever
    it pointed, because unparsed option syntax was itself the ground for
    denial. Blueprint §26.8 makes derived stores and proposals freely
    writable, so a write demonstrably outside ``canon/**`` has no reason to be
    refused. The canonical form of the same command is still denied, in the
    parametrized test directly above.
    """
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "sort -o docs/out.txt in.txt"},
    }

    assert invoke(payload, workspace).returncode == ALLOW


@pytest.mark.parametrize(
    "command",
    [
        "cp --target-directory=canon/world src/a",
        "cp -t canon/world src/a",
        "install --target-directory=canon/world src/a",
        "ln --target-directory=canon/world src/a",
    ],
)
def test_mutator_option_syntax_cannot_create_a_bypass(command, workspace):
    """§25 — an option can move where a mutator writes.

    ``--target-directory=`` and ``-t`` send the write somewhere the positional
    arguments never name, so extracting positional targets missed it entirely.
    Each is still denied under Route 3: the option's value names a path under
    ``canon/**``, which establishes the target even though the option grammar
    itself is not modelled.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


def test_mutator_option_pointing_outside_canon_is_allowed(workspace):
    """The counterpart, and the reason the case above is not vacuous.

    ``cp --target-directory=docs`` was denied under the retired policy purely
    for carrying an unrecognized option. It establishes no canonical target,
    so Route 3 allows it — which is what makes the canonical cases above a
    test of the boundary rather than of option syntax.
    """
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "cp --target-directory=docs src/a"},
    }

    assert invoke(payload, workspace).returncode == ALLOW


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
    [
        "rm -rf docs/x",
        "mkdir -p docs/sub",
        "cp -a src/a docs/a",
        "mv src/a docs/a",
        "cp src/a docs/a",
        "mkdir docs/newdir",
        "touch docs/file.txt",
    ],
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
        "git status",
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


@pytest.mark.parametrize(
    "command",
    [
        r"grep -e 'a\|b' file",
        'grep -e "a|b" file',
        r"grep -E 'foo\|bar' canon/world/f.md",
        "echo 'a; touch canon/world/x'",
        'echo "a; touch canon/world/x"',
        "echo 'a && touch canon/world/x'",
        'echo "she said \\"hi\\" and left"',
        'python3 -c "x=\\"canon/world/f.md\\"; print(x)"',
        r"grep -e 'a\|b' 'canon/world/notes.md'",
    ],
)
def test_quoted_separators_are_not_shell_syntax(command, workspace):
    """The quoted-pipe defect, fixed and pinned.

    The retired splitter was a regex over ``|``, ``;`` and ``&`` that could
    not see quoting, so ``grep -e 'a\\|b' file`` was cut at the quoted pipe
    into fragments whose first word was not ``grep``. Those fragments read as
    unknown commands and the search was denied.

    The last three cases matter more than they look: a quoted ``touch
    canon/...`` is an argument to ``echo``, and a real shell would print it
    rather than run it. Denying them would be a false positive; splitting on
    the quoted separator is what produced one.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


@pytest.mark.parametrize(
    "command",
    [
        "echo 'a'; touch canon/world/x",
        'echo "a" && touch canon/world/x',
        "true | touch canon/world/x",
        "true || touch canon/world/x",
        "(touch canon/world/x)",
        "cat f `touch canon/world/x`",
        "python3 -c 'import os' && rm -rf canon/world",
    ],
)
def test_unquoted_separators_still_split(command, workspace):
    """The other half — fixing the false positive must not lose real ones.

    Every separator here is genuine shell syntax, so the canonical mutation
    in the later segment really would run. A quote-aware splitter that
    stopped splitting altogether would pass the test above and open a bypass;
    this is the test that would catch it.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == DENY, command


@pytest.mark.parametrize(
    "command",
    [
        "touch docs/sentinel.txt",
        "mkdir docs/sentinel_dir",
        "python3 -c \"open('docs/sentinel.txt','w').write('x')\"",
        "echo x > docs/sentinel.txt",
    ],
)
def test_classifying_a_command_never_executes_it(command, workspace):
    """§17 — the hook decides by inspection, never by running the command.

    Each of these is ALLOWED by the policy, which is exactly what makes the
    test meaningful: an allow verdict must still leave the filesystem
    untouched. A hook that learned a command's effect by performing it would
    create the sentinel and fail here.
    """
    before = {str(p.relative_to(workspace)) for p in workspace.rglob("*")}

    invoke({"tool_name": "Bash", "tool_input": {"command": command}}, workspace)

    assert {str(p.relative_to(workspace)) for p in workspace.rglob("*")} == before


def test_hook_never_shells_out_to_classify():
    """§17 — classification is static. No subprocess, no eval, no exec.

    Checked against the executable body rather than the docstring, which
    discusses these names in prose.
    """
    body = SOURCE_HOOK.read_text(encoding="utf-8").split('"""', 2)[-1]

    for forbidden in (
        "subprocess",
        "os.system",
        "os.popen",
        "eval(",
        "exec(",
        "shell=True",
        "importlib",
    ):
        assert forbidden not in body, forbidden


@pytest.mark.parametrize(
    "command",
    [
        'git commit -m "deny writes to canon/world"',
        "git commit -m 'deny writes to canon/world'",
        "python3 -c \"print('canon')\"",
        "python3 -c \"print('canon/world/example.md')\"",
        'echo "canon/world/example.md"',
        "echo 'see canon/world/example.md for details'",
        "pytest --rootdir=canon",
        "grep -e 'canon/world/example.md' file.txt",
        "grep -rn canon docs/",
        "git commit -F -",
    ],
)
def test_mentioning_a_canonical_path_is_not_writing_one(command, workspace):
    """§13 — a textual mention is not a filesystem write.

    This is the false-positive class the Route-3 cleanup removed. The earlier
    implementation scanned every path-shaped run inside every word of an
    opaque command, so a message, a search pattern, a printed string or an
    unmodelled option's value all read as canonical targets. ``git commit -m``
    denying on its own commit message was the case that surfaced it.

    A path now counts only from shell-level position, so each of these is
    allowed while the positional forms — ``sed -i … canon/world/f.md``,
    ``dd of=canon/world/f.md`` — remain denied.

    The first two matter most: quote tracking spans whitespace, so the whole
    quoted message is one word. Splitting on whitespace first would leave
    ``canon/world"`` looking like a bare path argument, which is the exact
    bug this fixes.
    """
    payload = {"tool_name": "Bash", "tool_input": {"command": command}}

    assert invoke(payload, workspace).returncode == ALLOW, command


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
