# PURPOSE - `tests/`

| | |
|---|---|
| Directory | `tests/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0+ |

## Responsibility

Hold the seven test suites.

## Architectural role

Testing is staged per phase, and negative testing is first-class: every anti-ordering has an artifact proving rejection (PART XI).

## What belongs here

- the seven suites named in PART I

## What does not belong here

- canonical data
- fixtures mistakable for canon

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
