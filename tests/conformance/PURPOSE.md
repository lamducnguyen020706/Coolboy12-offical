# PURPOSE - `tests/conformance/`

| | |
|---|---|
| Directory | `tests/conformance/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0+ |

## Responsibility

Hold the per-phase conformance suites.

## Architectural role

Each phase exits on its conformance suite passing. No semantics before the foundation holds.

## What belongs here

- one conformance suite per phase

## What does not belong here

- canonical data
- a phase exit claimed without its suite green

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
