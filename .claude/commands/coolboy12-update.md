# /coolboy12-update

Publish the current COOLBOY12 living progress report. This is the only user-facing update command.

Run it with no arguments:

```bash
python3 scripts/update_progress.py --render
```

The publisher must:

1. Read `reports/HTML_UPDATE_CONTRACT.md`.
2. Read `reports/progress.json`.
3. Read `reports/implement-log.json`.
4. Parse `docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md` without modifying it.
5. Inspect repository evidence needed for exact artifact/file traceability.
6. Recalculate the displayed progress and date-grouped Implement Log.
7. Regenerate exactly `reports/progressreport.html`.
8. Validate the output and review `git diff --stat` and `git diff --check`.
9. Report the current frontier, overall progress, current phase, Implement Log summary and diff summary.

Do not pass an artifact ID. Do not add `daily` or `weekly` modes. Do not update progress merely because a prompt was received. Do not auto-commit. The hook records prompt activity; this command only publishes current state into the canonical HTML.

Expected report format:

```text
COOLBOY12 report updated.
Current frontier: Artifact <N>
Overall: <completed> / 490 · <percent>%
Current phase: <phase> · <phase progress>
Implement Log: <date/event summary>
Diff: <concise git diff --stat>
No commit created.
```
