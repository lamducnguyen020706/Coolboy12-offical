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


class ClaudeCodeIntegrationTests(unittest.TestCase):
    def test_render_is_read_only_for_live_json_and_roadmap(self):
        protected = [ROOT / "reports/progress.json", ROOT / "reports/implement-log.json", ROADMAP]
        before = {path: sha256(path) for path in protected}
        result = run(["python3", str(PUBLISHER), "--render"], ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, {path: sha256(path) for path in protected})
        self.assertIn("Overall: 21 / 490 · 4.3%", result.stdout)
        self.assertIn("No commit created.", result.stdout)

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
