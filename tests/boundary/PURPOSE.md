# PURPOSE - `tests/boundary/`

| | |
|---|---|
| Directory | `tests/boundary/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0+ |

## Responsibility

Hold boundary tests.

## Architectural role

A boundary that is not tested is a boundary that erodes.

## What belongs here

- tests of declared boundaries and forbidden edges

## What does not belong here

- canonical data
- tests of internal behaviour rather than boundaries

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
