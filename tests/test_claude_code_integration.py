from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = ROOT / "scripts" / "update_progress.py"
ROADMAP = ROOT / "docs" / "sources" / "COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], cwd: Path, *, stdin: str | None = None, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, input=stdin, text=True, capture_output=True, env=env or os.environ.copy())


def build_fixture_repo(temp: Path) -> None:
    """Copy the system into an isolated git repository.

    Every test that runs the publisher or the hook uses one of these. Running
    them against the real checkout would rewrite the tracked canonical report,
    which is a committed deliverable, not scratch space.

    implement-log.json is reset to an empty events list rather than copied
    live: the real file accumulates genuine UserPromptSubmit activity as the
    session runs, so a test asserting an exact event count against the copied
    file is not deterministic across time. progress.json is copied as-is —
    the declared build frontier is fixture input, not activity history.
    """
    shutil.copytree(ROOT / ".claude", temp / ".claude")
    shutil.copytree(ROOT / "reports", temp / "reports")
    (temp / "reports/implement-log.json").write_text(
        json.dumps({"version": 1, "timezone": "Asia/Ho_Chi_Minh", "events": []}, indent=2) + "\n",
        encoding="utf-8",
    )
    (temp / "scripts").mkdir()
    shutil.copy2(PUBLISHER, temp / "scripts/update_progress.py")
    (temp / "docs/sources").mkdir(parents=True)
    shutil.copy2(ROADMAP, temp / "docs/sources" / ROADMAP.name)
    subprocess.run(["git", "init", "-q"], cwd=temp, check=True)
    subprocess.run(["git", "config", "user.email", "audit@example.invalid"], cwd=temp, check=True)
    subprocess.run(["git", "config", "user.name", "COOLBOY12 audit"], cwd=temp, check=True)
    subprocess.run(["git", "add", "."], cwd=temp, check=True)
    subprocess.run(["git", "commit", "-qm", "audit fixture"], cwd=temp, check=True)


class ClaudeCodeIntegrationTests(unittest.TestCase):
    def test_render_is_read_only_for_live_json_and_roadmap(self):
        with tempfile.TemporaryDirectory(prefix="coolboy12-render-") as raw:
            temp = Path(raw)
            build_fixture_repo(temp)
            protected = [temp / "reports/progress.json", temp / "reports/implement-log.json", temp / "docs/sources" / ROADMAP.name]
            before = {path: sha256(path) for path in protected}
            result = run(["python3", str(temp / "scripts/update_progress.py"), "--render"], temp)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(before, {path: sha256(path) for path in protected})
            self.assertIn("Overall: 21 / 490 · 4.3%", result.stdout)
            self.assertIn("No commit created.", result.stdout)

    def test_suite_never_rewrites_the_tracked_canonical_report(self):
        """The canonical report is a committed deliverable, not test output.

        Regression guard: an earlier version of the read-only test invoked the
        real publisher against the real checkout, which rewrote
        reports/progressreport.html and dirtied the working tree on every run.
        """
        canonical = ROOT / "reports/progressreport.html"
        before = sha256(canonical)
        with tempfile.TemporaryDirectory(prefix="coolboy12-isolation-") as raw:
            temp = Path(raw)
            build_fixture_repo(temp)
            result = run(["python3", str(temp / "scripts/update_progress.py"), "--render"], temp)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotEqual(sha256(temp / "reports/progressreport.html"), "")
        self.assertEqual(sha256(canonical), before, "test run modified the tracked canonical report")

    def test_state_contradicting_the_roadmap_is_refused(self):
        """next_artifact and current_phase are claims about the Roadmap.

        Regression guard for a state that satisfied every load_state check yet
        named an impossible next artifact and an unrelated phase.
        """
        with tempfile.TemporaryDirectory(prefix="coolboy12-badstate-") as raw:
            temp = Path(raw)
            build_fixture_repo(temp)
            state_path = temp / "reports/progress.json"
            for field, value in (("next_artifact", "099"), ("current_phase", "P7")):
                state = json.loads(state_path.read_text())
                state[field] = value
                state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
                result = run(["python3", str(temp / "scripts/update_progress.py"), "--render"], temp)
                self.assertNotEqual(result.returncode, 0, f"{field}={value} was accepted")
                self.assertIn(field, result.stderr)
                state[field] = json.loads((ROOT / "reports/progress.json").read_text())[field]
                state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    def test_publisher_rejects_missing_render_and_noncanonical_output(self):
        missing_render = run(["python3", str(PUBLISHER)], ROOT)
        self.assertEqual(missing_render.returncode, 2)
        self.assertIn("no artifact argument is accepted", missing_render.stderr)
        wrong_path = run(["python3", str(PUBLISHER), "--render", "--html", "/tmp/not-canonical.html"], ROOT)
        self.assertNotEqual(wrong_path.returncode, 0)
        self.assertIn("canonical HTML", wrong_path.stderr + wrong_path.stdout)

    def test_user_prompt_hook_logs_deduplicates_and_advances_only_valid_frontier(self):
        with tempfile.TemporaryDirectory(prefix="coolboy12-claude-audit-") as raw:
            temp = Path(raw)
            shutil.copytree(ROOT / ".claude", temp / ".claude")
            shutil.copytree(ROOT / "reports", temp / "reports")
            (temp / "scripts").mkdir()
            shutil.copy2(PUBLISHER, temp / "scripts/update_progress.py")
            (temp / "docs/sources").mkdir(parents=True)
            shutil.copy2(ROADMAP, temp / "docs/sources" / ROADMAP.name)
            canon_file = temp / ".claude/hooks/canon_deny.py"
            canon_file.write_text("# audit fixture\n", encoding="utf-8")
            (temp / "reports/implement-log.json").write_text(
                json.dumps({"version": 1, "timezone": "Asia/Ho_Chi_Minh", "events": []}, indent=2) + "\n",
                encoding="utf-8",
            )

            subprocess.run(["git", "init", "-q"], cwd=temp, check=True)
            subprocess.run(["git", "config", "user.email", "audit@example.invalid"], cwd=temp, check=True)
            subprocess.run(["git", "config", "user.name", "COOLBOY12 audit"], cwd=temp, check=True)
            subprocess.run(["git", "add", "."], cwd=temp, check=True)
            subprocess.run(["git", "commit", "-qm", "audit fixture"], cwd=temp, check=True)
            hook_command = json.loads((ROOT / ".claude/settings.json").read_text())["hooks"]["UserPromptSubmit"][0]["hooks"][0]["command"]
            env = {**os.environ, "CLAUDE_PROJECT_DIR": str(temp), "PYTHONDONTWRITEBYTECODE": "1"}

            def submit(event_id: str, prompt: str, timestamp: str) -> subprocess.CompletedProcess[str]:
                payload = {"event_id": event_id, "prompt": prompt, "prompt_received_at": timestamp}
                return subprocess.run(["sh", "-c", hook_command], cwd=temp, input=json.dumps(payload), text=True, capture_output=True, env=env)

            self.assertEqual(submit("e1", "Review Artifact 022", "2026-08-25T09:00:00+07:00").returncode, 0)
            state_path = temp / "reports/progress.json"
            log_path = temp / "reports/implement-log.json"
            self.assertEqual(json.loads(state_path.read_text())["current_frontier"], "021")
            self.assertFalse(json.loads(log_path.read_text())["events"][-1]["completion_recorded"])
            self.assertEqual(submit("e1", "Review Artifact 022", "2026-08-25T09:00:00+07:00").returncode, 0)
            self.assertEqual(len(json.loads(log_path.read_text())["events"]), 1)

            self.assertEqual(submit("e2", "Freeze and commit Artifact 024", "2026-08-25T10:00:00+07:00").returncode, 0)
            self.assertEqual(json.loads(state_path.read_text())["next_artifact"], "022")
            self.assertEqual(submit("e-neg", "Do not freeze and commit Artifact 022", "2026-08-25T10:30:00+07:00").returncode, 0)
            self.assertEqual(json.loads(state_path.read_text())["current_frontier"], "021")
            self.assertFalse(json.loads(log_path.read_text())["events"][-1]["completion_recorded"])
            self.assertEqual(submit("e3", "Freeze and commit Artifact 022", "2026-08-25T11:00:00+07:00").returncode, 0)
            state = json.loads(state_path.read_text())
            event = json.loads(log_path.read_text())["events"][-1]
            self.assertEqual((state["current_frontier"], state["next_artifact"], state["current_phase"]), ("022", "023", "P0"))
            self.assertTrue(event["completion_recorded"])
            self.assertEqual((event["completed_before"], event["completed_after"]), (21, 22))

    def test_untracked_file_is_not_completion_evidence(self):
        """A prompt plus a stray untracked file must not fabricate a completion.

        Regression guard: the evidence check previously unioned tracked files
        with every file on disk, so creating an untracked file at the planned
        path and saying "freeze and commit" advanced the frontier with no
        commit at all.
        """
        with tempfile.TemporaryDirectory(prefix="coolboy12-untracked-") as raw:
            temp = Path(raw)
            build_fixture_repo(temp)
            hook_command = json.loads((ROOT / ".claude/settings.json").read_text())["hooks"]["UserPromptSubmit"][0]["hooks"][0]["command"]
            env = {**os.environ, "CLAUDE_PROJECT_DIR": str(temp), "PYTHONDONTWRITEBYTECODE": "1"}
            state_path = temp / "reports/progress.json"

            # Artifact 022 now exists in the real repository, so the fixture
            # copy carries it as tracked evidence. Remove and commit that
            # removal first, so the fixture genuinely starts with no evidence
            # for the next artifact — otherwise this test asserts nothing.
            (temp / ".claude/hooks/canon_deny.py").unlink(missing_ok=True)
            subprocess.run(["git", "add", "-A"], cwd=temp, check=True)
            subprocess.run(["git", "commit", "-qm", "remove 022 evidence"], cwd=temp, check=True)

            # Untracked file at Artifact 022's planned path, never staged.
            (temp / ".claude/hooks/canon_deny.py").write_text("# untracked\n", encoding="utf-8")
            payload = {"event_id": "untracked", "prompt": "Freeze and commit Artifact 022", "prompt_received_at": "2026-08-26T10:00:00+07:00"}
            subprocess.run(["sh", "-c", hook_command], cwd=temp, input=json.dumps(payload), text=True, capture_output=True, env=env)
            self.assertEqual(json.loads(state_path.read_text())["current_frontier"], "021", "untracked file advanced the frontier")

            # Staging the same file makes it tracked evidence, and it advances.
            subprocess.run(["git", "add", ".claude/hooks/canon_deny.py"], cwd=temp, check=True)
            payload = {"event_id": "tracked", "prompt": "Freeze and commit Artifact 022", "prompt_received_at": "2026-08-26T11:00:00+07:00"}
            subprocess.run(["sh", "-c", hook_command], cwd=temp, input=json.dumps(payload), text=True, capture_output=True, env=env)
            self.assertEqual(json.loads(state_path.read_text())["current_frontier"], "022")

    def test_claude_settings_command_and_skill_are_consistent(self):
        settings = json.loads((ROOT / ".claude/settings.json").read_text())
        hook = settings["hooks"]["UserPromptSubmit"][0]["hooks"][0]
        self.assertEqual(hook["type"], "command")
        self.assertIn("coolboy12_prompt_log.py", hook["command"])
        self.assertEqual(hook["timeout"], 5)
        command_doc = (ROOT / ".claude/commands/coolboy12-update.md").read_text()
        skill_doc = (ROOT / ".claude/skills/coolboy12-update/SKILL.md").read_text()
        for document in (command_doc, skill_doc):
            self.assertIn("scripts/update_progress.py --render", document)
            self.assertIn("commit", document.lower())
            self.assertIn("artifact", document.lower())
        self.assertNotIn("--artifact", command_doc)


if __name__ == "__main__":
    unittest.main(verbosity=2)


__all__ = ["ClaudeCodeIntegrationTests"]

# This module is intentionally stdlib-only and uses temporary repositories for hook writes.
