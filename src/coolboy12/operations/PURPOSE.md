# PURPOSE - `src/coolboy12/operations/`

| | |
|---|---|
| Directory | `src/coolboy12/operations/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P17 |

## Responsibility

Implement dormancy, degraded modes and recovery.

## Architectural role

The system fails closed. Proceeding silently when a required check is unavailable is anti-ordering X-22.

## What belongs here

- dormancy and wake handling
- degraded-mode behaviour
- recovery and return briefing

## What does not belong here

- canonical data
- silent continuation past an unavailable check
- any scheduler or background world advance

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
