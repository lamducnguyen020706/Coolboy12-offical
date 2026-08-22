# PURPOSE - `src/coolboy12/adapters/`

| | |
|---|---|
| Directory | `src/coolboy12/adapters/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0 |

## Responsibility

Hold the eleven adapter boundary implementations.

## Architectural role

At P0 the responsibility is that the boundary exists and is empty. Implementations arrive at P17 (artifacts 444-447). A component supplies a computation, not a meaning.

## What belongs here

- one boundary shell per adapter, each naming its boundary
- World package constructs marked World-only

## What does not belong here

- canonical data
- any adapter holding authority
- implementation before its licensing phase

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
