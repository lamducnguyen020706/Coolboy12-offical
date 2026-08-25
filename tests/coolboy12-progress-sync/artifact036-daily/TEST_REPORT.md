# COOLBOY12 Synthetic Scenario — Artifact 036 / P1

## Safety

This is **synthetic test data only**. It does not advance production state and does not create Artifact 036 files.

## Scenario

The synthetic frontier advances from Artifact 021 to Artifact 036. Artifacts 022–036 are represented by exactly one completion event per calendar day, producing 15 daily Implement Log nodes.

## Expected final state

| Field | Expected |
|---|---|
| Frontier | Artifact 036 |
| Next artifact | Artifact 037 |
| Current phase | P1 · 6 / 8 |
| P0 | DONE · 30 / 30 |
| P1 | WIP · 6 / 8 |
| Cumulative | 36 / 490 · 7.3% |
| Daily nodes | 15 |
| Events per day | 1 artifact |

## Validation

| Check | Result |
|---|---|
| Synthetic labeling | PASS |
| One completion event per day | PASS |
| One artifact per event | PASS |
| Daily completion snapshots | PASS |
| Frontier and next | PASS |
| Current phase P1 | PASS |
| Dashboard P1 progress | PASS |
| Progress Table P0 done | PASS |
| Progress Table P1 WIP | PASS |
| P2 not started | PASS |
| Next artifact 037 | PASS |
| Next exact file | PASS |
| Dependency file separated | PASS |
| No blueprint/rms/roadmap as exact 031 file | PASS |
| Fifteen date nodes | PASS |
| Each day reports one artifact | PASS |
| Cumulative 36/490 | PASS |
| One-decimal percentages and no today | PASS |
| All phases and artifacts | PASS |
| Production unchanged | PASS |

## Traceability expectation

The next card for Artifact 037 shows `src/coolboy12/bootstrap/validate.py` as the **Exact Artifact file**. Its dependency files `docs/constitution/record_envelope.md` and `src/coolboy12/bootstrap/identity.py` are displayed separately under **Dependency files · supporting inputs**. The dependency list is not merged into the exact Artifact file list.

## Output

- `synthetic-progress.json`
- `synthetic-implement-log.json`
- `synthetic-progressreport.html`
- `TEST_REPORT.md`
