# COOLBOY12 HTML Update Contract

`HTML_UPDATE_CONTRACT_VERSION = 1.0`

## Purpose

This contract protects the approved editorial report from silent redesign. **Data changes frequently; design changes only by explicit decision.** The canonical published report is `reports/progressreport.html`.

## Source hierarchy

Blueprint → RMS → Roadmap → repository evidence → `reports/progress.json` / `reports/implement-log.json` → `reports/progressreport.html`.

The HTML is presentation output only. It is never a source of truth and must not write JSON state from browser JavaScript.

## Protected UX

The publisher must preserve the progress dashboard, overall percentage, current frontier, next artifact, phase strip, phase navigation, phase-to-artifact drill-down, artifact details, separate artifact Description and Purpose fields, exact repository-relative file paths, dependency IDs and dependency files as distinct supporting inputs, directory information, dependencies, unlocks, validation and exit information, Blueprint and RMS references, repository evidence, critical path, responsive/mobile behavior, print CSS, typography, spacing, color system, editorial hierarchy and existing navigation. The report remains dark by default and retains the single Implement Log surface.

The report must retain all 19 phases and all 490 artifact entries with exact IDs and Roadmap ranges. P0 opens by default; later phases remain collapsible.

## Allowed changes during `/coolboy12-update`

A normal update may change live progress values, artifact status when supported by state/evidence, current frontier, next artifact, current phase, repository evidence, generated timestamp, Implement Log contents, daily progress and cumulative progress. It must not redesign the report or introduce a second report, application, database, API or analytics surface.

## Invariants

The renderer must keep the Roadmap total at 490 unless the Roadmap explicitly changes. It must not invent artifact IDs or phase IDs, infer completion from a prompt, file, commit or tool call alone, skip sequence, advance independently of validated state, modify `progress.json` or `implement-log.json`, rewrite historical log events, remove required sections, or corrupt daily percentage calculations. Exact Artifact files come from the artifact’s own Roadmap path; dependency files come only from declared dependency artifact IDs and must never be merged into the exact-file list. Daily progress is completed-artifact delta divided by 490; prompt count and tool count are never used.

## Pre-flight and post-flight

Before publishing, read this contract, both JSON state files and the Roadmap, inspect repository evidence, and stop if unrelated uncommitted modifications affect the canonical report. After publishing, validate HTML structure, 19 phases, 490 artifact IDs, current frontier, next artifact, percentages, Implement Log grouping/order, exact paths, responsive CSS, print CSS and absence of unintended redesign. Never auto-commit; report the diff for user review.
