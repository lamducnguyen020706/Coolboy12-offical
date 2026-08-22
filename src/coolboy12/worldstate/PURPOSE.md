# PURPOSE - `src/coolboy12/worldstate/`

| | |
|---|---|
| Directory | `src/coolboy12/worldstate/` |
| Owner | the implementing layer |
| Record Model | W |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P9 |

## Responsibility

Implement WSV and simulation consumption.

## Architectural role

World owns current indicator values; Registry owns their meaning. WSV is one Record, never one per indicator (RMS sec.10.7).

## What belongs here

- the WSV singleton
- WSV-H entries, one per committed world-state mutation
- simulation consumption

## What does not belong here

- canonical data
- a Record per indicator (X-15)
- indicator meaning, which is Registry-owned

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
