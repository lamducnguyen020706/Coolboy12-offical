# COOLBOY12 Update Skill

Publish the current human-facing report with exactly:

```text
/coolboy12-update
```

No artifact ID, phase, day or week argument is accepted.

## Procedure

1. Read `reports/HTML_UPDATE_CONTRACT.md`.
2. Read `reports/progress.json` and `reports/implement-log.json`.
3. Parse `docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md` as the Roadmap authority.
4. Inspect repository evidence only as needed for exact artifact/file traceability.
5. Check `git status --short`; stop if unrelated modifications affect the canonical report or source inputs.
6. Run `python3 scripts/update_progress.py --render`.
7. Validate the resulting `reports/progressreport.html`: 19 phase IDs, 490 artifact IDs, exact ranges, current frontier, next artifact, correct percentages, Implement Log structure, exact file paths, responsive CSS and print CSS.
8. Run `git diff --check` and show `git diff --stat`.
9. Report what changed. Do not commit.

## Boundaries

The prompt hook is responsible for activity logging. This skill only publishes state into HTML. It must not append a prompt event merely because `/coolboy12-update` was typed. It must not modify Blueprint, RMS, Roadmap or repository architecture. It must not create a second report or redesign the protected editorial UI.
