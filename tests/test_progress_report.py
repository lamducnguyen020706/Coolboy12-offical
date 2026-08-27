from __future__ import annotations

import copy
import importlib.util
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER_PATH = ROOT / "scripts" / "update_progress.py"
STATE_PATH = ROOT / "reports" / "progress.json"

spec = importlib.util.spec_from_file_location("coolboy12_progress_publisher", PUBLISHER_PATH)
publisher = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(publisher)

PHASES, ARTIFACTS = publisher.parse_roadmap()
TRACKED = set(publisher.tracked_files())
EVIDENCE = {artifact["id"]: publisher.evidence_for(artifact, TRACKED) for artifact in ARTIFACTS}
BASE_STATE = json.loads(STATE_PATH.read_text(encoding="utf-8"))


def render_for_completed(last_id: int, current_phase: str | None = None) -> str:
    """Render the report as if artifacts 001..last_id were complete.

    Completion now reaches the renderer through the derived-evidence dict
    rather than through ``progress.json``, so the synthetic completion set is
    passed there. The intent of these tests is unchanged — drive the renderer
    with a chosen completion set and check what it produces — and driving it
    through the real parameter is what keeps them honest.
    """
    state = publisher.repo_facts(copy.deepcopy(BASE_STATE))
    completed = [f"{number:03d}" for number in range(1, last_id + 1)]
    derived = {
        "completed": completed,
        "frontier": f"{last_id:03d}",
        "next": f"{last_id + 1:03d}",
        "reasons": {},
        "evidenced_out_of_sequence": [],
    }
    phase_of = {a["id"]: a["phase"] for a in ARTIFACTS}
    derived["phase"] = current_phase or phase_of.get(derived["frontier"], "P0")
    return publisher.render_html(state, [], PHASES, ARTIFACTS, EVIDENCE, derived)


class ProgressReportTests(unittest.TestCase):
    def test_production_next_artifact_manifest(self):
        html = render_for_completed(21)
        next_section = re.search(r'<section id="next">.*?</section>', html, re.S).group(0)
        self.assertIn("Artifact 022", next_section)
        next_row = next(a for a in ARTIFACTS if a["id"] == "022")
        self.assertIn("canon write-deny hook", next_section)
        self.assertIn("Description", next_section)
        self.assertIn("direct write to canon/ denied", next_section)
        self.assertIn("Purpose", next_section)
        self.assertIn("built in P0 so bypass is impossible", next_section)
        self.assertIn(next_row["planned_path"], next_section)
        self.assertIn(".claude/hooks/", next_section)
        self.assertIn("PLANNED", next_section)
        self.assertIn("017,021", next_section)
        self.assertIn("133", next_section)
        self.assertIn("direct write to", next_section)
        self.assertIn("deny proven by negative test", next_section)
        self.assertIn("Exact Artifact files · repository-relative paths", next_section)
        self.assertIn("Dependency files · supporting inputs", next_section)
        self.assertIn("docs/boundaries/canonical_zones.md", next_section)
        self.assertIn("src/coolboy12/bootstrap/config.py", next_section)
        self.assertIn('href="#P0">P0 detail</a>', html)
        self.assertIn('<section id="P0">', html)

    def test_phase_two_next_manifest_and_dashboard(self):
        html = render_for_completed(50)
        next_section = re.search(r'<section id="next">.*?</section>', html, re.S).group(0)
        self.assertIn("Artifact 051", next_section)
        self.assertIn("authority framework", next_section)
        self.assertIn("Description", next_section)
        self.assertIn("authority domain-scoped; Record ≠ Canon", next_section)
        self.assertIn("Purpose", next_section)
        self.assertIn("I-104 made buildable", next_section)
        self.assertIn("039", next_section)
        self.assertIn("052, all models", next_section)
        self.assertIn("authority domain-scoped", next_section)
        self.assertIn("framework", next_section)
        self.assertIn("docs/constitution/authority.md", next_section)
        self.assertIn("docs/constitution/", next_section)
        self.assertIn("Exact Artifact files · repository-relative paths", next_section)
        self.assertIn("Dependency files · supporting inputs", next_section)
        self.assertIn("PLANNED", next_section)
        self.assertIn("P2 · 12 / 21", html)
        self.assertIn("57.1%", html)
        self.assertNotIn("57.14%", html)
        self.assertIn("Artifact còn lại trong P2", html)
        self.assertIn('<td class="status-done">DONE</td><td>30 / 30</td>', html)
        self.assertIn('class="phase-card done"', html)
        self.assertIn('.artifact-row.done .artifact-copy strong', html)
        self.assertIn('<td class="status-done">DONE</td><td>8 / 8</td>', html)
        self.assertIn('<td class="status-wip">WIP</td><td>12 / 21</td>', html)
        self.assertIn('href="#P2">P2 detail</a>', html)
        self.assertIn('<section id="P2">', html)
        self.assertIn("Phase <strong>P2</strong> mở mặc định", html)
        phase_strip = re.search(r'<div class="phase-strip">(.*?)</div>', html, re.S).group(1)
        self.assertIn('<a class="phase-dot done" href="#P0">P0', phase_strip)
        self.assertIn('<a class="phase-dot done" href="#P1">P1', phase_strip)
        self.assertIn('<a class="phase-dot current" href="#P2">P2', phase_strip)
        self.assertIn('.phase-dot.done', html)

    def test_exact_artifact_files_are_separate_from_dependency_files(self):
        html = render_for_completed(36, current_phase="P1")
        artifact_031 = re.search(r'id="artifact-031".*?</details>', html, re.S).group(0)
        exact_block = re.search(r'<label>Exact Artifact files · repository-relative paths</label><span class="file-list">(.*?)</span>', artifact_031, re.S).group(1)
        dependency_block = artifact_031.split('<label>Dependency files · supporting inputs</label>', 1)[1].split('<p><label>Repository evidence', 1)[0]
        self.assertIn("docs/constitution/bootstrap_meta_contract.md", exact_block)
        self.assertNotIn("COOLBOY12_MASTER_BLUEPRINT", exact_block)
        self.assertNotIn("RECORD_MODEL_SYSTEM", exact_block)
        self.assertNotIn("ROADMAP", exact_block)
        self.assertIn("CLAUDE.md", dependency_block)
        self.assertIn("docs/boundaries/source_of_truth.md", dependency_block)
        self.assertNotIn("docs/constitution/bootstrap_meta_contract.md", dependency_block)

    def test_phase_artifact_detail_uses_description_and_purpose_schema(self):
        html = render_for_completed(50)
        artifact_051 = re.search(r'id="artifact-051".*?</details>', html, re.S).group(0)
        self.assertIn('<label>Description</label>authority domain-scoped; Record ≠ Canon', artifact_051)
        self.assertIn('<label>Purpose</label>I-104 made buildable', artifact_051)
        self.assertIn('<label>Exact Artifact files · repository-relative paths</label>', artifact_051)
        self.assertIn('<label>Dependency files · supporting inputs</label>', artifact_051)
        self.assertIn('<label>Directory</label>', artifact_051)

    def test_progress_table_has_no_false_not_started_for_completed_phase(self):
        html = render_for_completed(50)
        table = re.search(r'<section id="roadmap">.*?</section>', html, re.S).group(0)
        self.assertNotIn('<td class="status-not-started">NOT STARTED</td><td>30 / 30</td>', table)
        self.assertNotIn('<td class="status-not-started">NOT STARTED</td><td>8 / 8</td>', table)
        self.assertIn('<td class="status-done">DONE</td><td>30 / 30</td>', table)
        self.assertIn('<td class="status-done">DONE</td><td>8 / 8</td>', table)
        self.assertIn('<td class="status-wip">WIP</td><td>12 / 21</td>', table)

    def test_phase_boundary_statuses_follow_completed_set(self):
        at_boundary = render_for_completed(30, current_phase="P1")
        after_first_p1 = render_for_completed(31, current_phase="P1")
        for html in (at_boundary, after_first_p1):
            self.assertIn('href="#P1">P1 detail</a>', html)
            self.assertIn('<section id="P1">', html)
        self.assertIn('<td class="status-done">DONE</td><td>30 / 30</td>', at_boundary)
        self.assertIn('<td class="status-not-started">NOT STARTED</td><td>0 / 8</td>', at_boundary)
        self.assertIn("P1 · 0 / 8", at_boundary)
        self.assertIn('class="phase-card current" id="P1"', at_boundary)
        self.assertIn('<td class="status-done">DONE</td><td>30 / 30</td>', after_first_p1)
        self.assertIn('<td class="status-wip">WIP</td><td>1 / 8</td>', after_first_p1)
        self.assertIn('<td class="status-not-started">NOT STARTED</td><td>0 / 8</td>', after_first_p1.replace('<td class="status-wip">WIP</td><td>1 / 8</td>', ''))
        self.assertIn("P1 · 1 / 8", after_first_p1)
        self.assertIn("12.5%", after_first_p1)

    def test_removed_sections_and_log_metadata_stay_removed(self):
        html = render_for_completed(50)
        self.assertNotIn('<section id="trace">', html)
        self.assertNotIn('prompt event(s) · newest date first', html)
        self.assertNotIn('Lịch sử prompt/activity được hook ghi nhận', html)
        self.assertNotIn("Critical path", html)
        self.assertNotIn(" today", html)
        self.assertNotIn("today</", html)


class EvidenceDerivationTests(unittest.TestCase):
    """The two complaints this system was revised to fix.

    The Implement Log showed *"Prompt received"* and nothing else, and the
    frontier sat at the declared 022 while 023–027 were built and frozen. Both
    came from one cause — reading declared state and prompt telemetry instead
    of the repository — so both are locked down here.
    """

    def setUp(self):
        self.commits = publisher.artifact_commits()
        self.derived = publisher.derive_completion(ARTIFACTS, TRACKED, self.commits)

    def test_a_commit_alone_is_not_completion(self):
        """One signal never suffices — the predicate is composite.

        Fed a commit subject for an artifact with nothing tracked at its path,
        the deriver must record *why* it refused rather than count it.
        """
        unbuilt = next(a for a in ARTIFACTS if a["id"] not in self.derived["completed"])
        forged = dict(self.commits)
        forged[unbuilt["id"]] = [{
            "sha": "0" * 40, "short": "0000000",
            "subject": f'Artifact {unbuilt["id"]} — forged subject',
            "date": "2026-08-27T00:00:00+07:00",
        }]
        derived = publisher.derive_completion(ARTIFACTS, set(), forged)

        self.assertNotIn(unbuilt["id"], derived["completed"])
        self.assertIn("no tracked file", derived["reasons"][unbuilt["id"]])

    def test_a_tracked_file_alone_is_not_completion(self):
        """The other half. Every path tracked, no commit declaring it."""
        derived = publisher.derive_completion(ARTIFACTS, TRACKED, {})

        self.assertEqual(derived["completed"], [])
        self.assertIn("no commit declares", derived["reasons"]["001"])

    def test_only_the_commit_subject_declares_an_artifact(self):
        """A body that quotes the Roadmap must not build anything.

        Not hypothetical: searching whole commit messages matched a body
        quoting row 031 and reported an unbuilt artifact as finished.

        Driven against a real repository holding exactly that trap, because
        the protection is the ``git log`` format string — bodies never reach
        the pattern at all — and asserting on the pattern alone proves
        nothing: ``re.match`` anchors whether or not the pattern says so.
        """
        with tempfile.TemporaryDirectory(prefix="coolboy12-subject-") as raw:
            temp = Path(raw)
            (temp / "f.txt").write_text("x\n", encoding="utf-8")
            for command in (
                ["git", "init", "-q"],
                ["git", "config", "user.email", "audit@example.invalid"],
                ["git", "config", "user.name", "COOLBOY12 audit"],
                ["git", "add", "."],
                ["git", "commit", "-qm",
                 "Publish report\n\nQuotes the Roadmap: Artifact 031 is next."],
            ):
                subprocess.run(command, cwd=temp, check=True)
            subprocess.run(["git", "commit", "-q", "--allow-empty", "-m",
                            "Artifact 027 — /rebuild refusing stub"], cwd=temp, check=True)

            original = publisher.ROOT
            try:
                publisher.ROOT = temp
                found = publisher.artifact_commits()
            finally:
                publisher.ROOT = original

        self.assertIn("027", found)
        self.assertNotIn("031", found, "a commit body declared an artifact")

    def test_evidence_beyond_a_gap_never_advances_the_frontier(self):
        """The frontier is the longest unbroken run from 001, not a maximum."""
        gapped = {aid: rows for aid, rows in self.commits.items() if aid != "003"}
        derived = publisher.derive_completion(ARTIFACTS, TRACKED, gapped)

        self.assertEqual(derived["frontier"], "002")
        self.assertNotIn("004", derived["completed"])
        self.assertIn("004", derived["evidenced_out_of_sequence"])

    def test_file_attribution_is_scoped_to_the_declaring_commits(self):
        """Files come from the commits that declare the artifact, nothing else.

        These files are the second half of the completion predicate, so a
        commit that merely mentions an artifact in its body must not lend its
        files to it. Borrowed evidence is not evidence.
        """
        with tempfile.TemporaryDirectory(prefix="coolboy12-attrib-") as raw:
            temp = Path(raw)

            def commit(message: str, filename: str) -> None:
                (temp / filename).write_text("x\n", encoding="utf-8")
                subprocess.run(["git", "add", filename], cwd=temp, check=True)
                subprocess.run(["git", "commit", "-qm", message], cwd=temp, check=True)

            for command in (
                ["git", "init", "-q"],
                ["git", "config", "user.email", "audit@example.invalid"],
                ["git", "config", "user.name", "COOLBOY12 audit"],
            ):
                subprocess.run(command, cwd=temp, check=True)
            commit("Artifact 027 — the real one", "owned.txt")
            commit("Unrelated work\n\nSee Artifact 027 for context.", "borrowed.txt")

            original = publisher.ROOT
            try:
                publisher.ROOT = temp
                declaring = [c["sha"] for c in publisher.artifact_commits()["027"]]
                tracked = set(publisher.tracked_files())
                files = publisher.artifact_commit_files("027", tracked, declaring)
            finally:
                publisher.ROOT = original

        self.assertEqual(files, ["owned.txt"])

    def test_the_log_records_builds_and_never_prompt_events(self):
        events = publisher.build_events(ARTIFACTS, self.commits, self.derived, TRACKED)
        html = publisher.timeline_html(events, self.derived)

        self.assertTrue(events)
        self.assertNotIn("Prompt received", html)
        for event in events:
            self.assertRegex(event["artifact"], r"^\d{3}$")
            self.assertTrue(event["commit"])
        self.assertIn("event-files", html)

    def test_file_chips_have_their_own_styling(self):
        """Added markup without styling is a redesign by omission.

        The contract protects typography and spacing, so the classes the log
        emits must be defined rather than inheriting whatever is nearest.
        """
        html = render_for_completed(27)

        for rule in (".event-files{", ".event-files .more{", ".log-event code{"):
            self.assertIn(rule, html, rule)


if __name__ == "__main__":
    unittest.main(verbosity=2)
