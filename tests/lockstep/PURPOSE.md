# PURPOSE - `tests/lockstep/`

| | |
|---|---|
| Directory | `tests/lockstep/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0+ |

## Responsibility

Hold lockstep tests for LS-1 through LS-8.

## Architectural role

A lockstep pair or triple must land in one authoring cycle; an unpaired half is a defect (PART III).

## What belongs here

- tests proving each lockstep set is complete

## What does not belong here

- canonical data
- manufactured locksteps - spec-to-test, model-to-example and schema-to-fixture are rejected (PART III)

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
