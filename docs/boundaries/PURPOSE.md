# PURPOSE - `docs/boundaries/`

| | |
|---|---|
| Directory | `docs/boundaries/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P0 |

## Responsibility

Declare the boundaries the system may never cross: version control, environment, secrets, source of truth, and canonical zones.

## Architectural role

A boundary declaration states what a layer may never own. It governs; it does not enforce - enforcement is code.

## What belongs here

- the version-control boundary
- the environment boundary
- the secrets and configuration boundary
- the source-of-truth boundary
- the canonical zone declaration

## What does not belong here

- conventions - those belong in `docs/conventions/`
- enforcement code - that belongs in `src/` or `.claude/`
- secrets themselves, which are EXTERNAL forever

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
