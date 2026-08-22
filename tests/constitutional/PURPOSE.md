# PURPOSE - `tests/constitutional/`

| | |
|---|---|
| Directory | `tests/constitutional/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0 |

## Responsibility

Hold the constitutional test harness and the invariant register.

## Architectural role

Invariants precede everything. The register carries I-01 through I-108 and gates every phase exit.

## What belongs here

- the constitutional harness
- the 108-entry invariant register
- invariant tests

## What does not belong here

- canonical data
- an invariant marked tested without evidence
- an orphaned register entry

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
