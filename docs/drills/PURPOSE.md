# PURPOSE - `docs/drills/`

| | |
|---|---|
| Directory | `docs/drills/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P18 |

## Responsibility

Hold the drill specifications.

## Architectural role

Generating a drill is not executing it. Execution is deferred to G-RUNTIME (Roadmap PART XV).

## What belongs here

- drill specifications

## What does not belong here

- drill results or execution evidence
- any claim that a specified drill has been run

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
