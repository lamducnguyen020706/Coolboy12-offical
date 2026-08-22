# PURPOSE - `docs/adapters/`

| | |
|---|---|
| Directory | `docs/adapters/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P0/P17 |

## Responsibility

Hold the eleven adapter boundary contracts.

## Architectural role

A component supplies a computation; it does not supply a meaning. Every adapter names its boundary, its source-of-truth class, its degraded mode and its removal path (Blueprint sec.26.3a).

## What belongs here

- one boundary contract per adapter
- degraded modes and exit paths

## What does not belong here

- adapter implementations - those belong in `src/coolboy12/adapters/`
- any adapter holding authority

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
