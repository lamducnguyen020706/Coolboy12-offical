# PURPOSE - `derived/projections/`

| | |
|---|---|
| Directory | `derived/projections/` |
| Owner | the consuming model |
| Record Model | n/a |
| Source-of-truth class | DERIVED |
| Rebuildable | Always |
| Write | rebuild process |
| Delete | Freely |
| Prohibited | anything unrebuildable |
| Introduced by phase | P8 |

## Responsibility

Hold derived, rebuildable projections.

## Architectural role

A projection is derived output and is never authoritative (RMS sec.6.1). Suspicion, readiness, coverage, forecast, heatmap and knowledge-debt views are projections, not Records.

## What belongs here

- projections rebuilt from canon

## What does not belong here

- any projection treated as a Record
- any authority claim

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
