# PURPOSE - `src/coolboy12/mutation/`

| | |
|---|---|
| Directory | `src/coolboy12/mutation/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P5 |

## Responsibility

Implement the Mutation Coordinator - the sole canonical write path.

## Architectural role

A second write path is a second canon (Spine law 2). Every canonical write in the system passes through this layer.

## What belongs here

- the Mutation Coordinator
- proposal, basis, preflight, gate and commit-set handling

## What does not belong here

- canonical data
- any alternative write path
- any bypass of the Human Gate

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
