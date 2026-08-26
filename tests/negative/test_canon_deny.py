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
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOK = REPO_ROOT / ".claude/hooks/canon_deny.py"

DENY = 2
ALLOW = 0


@pytest.fixture(scope="module")
def workspace(tmp_path_factory):
    """An isolated repository-shaped tree with an empty canonical zone.

    Mirrors the real layout so the hook resolves a root the same way it does
    in production, without any test touching the real ``canon/**``.
    """
    root = tmp_path_factory.mktemp("canon-deny-repo")
    (root / ".claude/hooks").mkdir(parents=True)
    for zone in ("world", "epistemic", "production", "registry", "visual", "issue"):
        (root / "canon" / zone).mkdir(parents=True)
    (root / "docs").mkdir()
    (root / "src").mkdir()
    (root / "canonical").mkdir()
    (root / "canon_backup").mkdir()
    return root


def invoke(
    payload: dict, workspace: Path, extra_env: dict | None = None
) -> subprocess.CompletedProcess:
    """Run the hook the way Claude Code runs it: JSON on stdin, status back.

    ``extra_env`` is handed to the subprocess only, never exported into the
    test process, so a shell-variable fixture cannot leak between tests.
    """
    env = {
        "CLAUDE_PROJECT_DIR": str(workspace),
        "PATH": "/usr/bin:/bin",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        [sys.executable, str(HOOK)],
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
        [sys.executable, str(HOOK)],
        input="{not json",
        text=True,
        capture_output=True,
        check=False,
        env={"CLAUDE_PROJECT_DIR": str(workspace), "PATH": "/usr/bin:/bin"},
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
    source = HOOK.read_text(encoding="utf-8")
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
