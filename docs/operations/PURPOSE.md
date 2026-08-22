# PURPOSE - `docs/operations/`

| | |
|---|---|
| Directory | `docs/operations/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P17 |

## Responsibility

Hold dormancy, degraded-mode and recovery specifications.

## Architectural role

Nothing runs unattended. The system is operated in sessions and must survive dormancy (Blueprint sec.26.8, sec.28).

## What belongs here

- dormancy behaviour
- degraded modes and their behaviour contracts
- recovery and return-briefing specifications

## What does not belong here

- proceeding silently when a required check is unavailable - the system fails closed (X-22)
- any scheduler, daemon or background advance of the world

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
