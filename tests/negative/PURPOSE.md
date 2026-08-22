# PURPOSE - `tests/negative/`

| | |
|---|---|
| Directory | `tests/negative/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0+ |

## Responsibility

Hold negative tests - the proofs of rejection.

## Architectural role

Negative testing is first-class. Every anti-ordering X-01 through X-22 has an artifact proving rejection (PART XI).

## What belongs here

- proofs that prohibited actions are refused

## What does not belong here

- canonical data
- a prohibition asserted without a proof of rejection

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
