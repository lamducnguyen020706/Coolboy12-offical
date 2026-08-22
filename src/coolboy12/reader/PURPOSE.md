# PURPOSE - `src/coolboy12/reader/`

| | |
|---|---|
| Directory | `src/coolboy12/reader/` |
| Owner | the implementing layer |
| Record Model | E |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P16 |

## Responsibility

Implement reader simulation.

## Architectural role

Reader signal never becomes truth (X-19); simulated response never re-enters as canon (X-20).

## What belongs here

- reader models
- reader simulation

## What does not belong here

- canonical data
- any path from reader signal to truth
- popularity treated as truth

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
