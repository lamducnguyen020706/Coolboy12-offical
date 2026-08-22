# PURPOSE - `docs/reader/`

| | |
|---|---|
| Directory | `docs/reader/` |
| Owner | authoring layer |
| Record Model | E |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P16 |

## Responsibility

Hold the reader-simulation specifications.

## Architectural role

Reader signal never becomes truth, and simulated reader response never re-enters as canon (X-19, X-20).

## What belongs here

- reader model and reader-simulation specifications

## What does not belong here

- reader signal treated as truth
- simulated reader response re-entering as canon
- popularity becoming truth

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
