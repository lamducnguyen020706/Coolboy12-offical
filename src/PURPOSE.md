# PURPOSE - `src/`

| | |
|---|---|
| Directory | `src/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P0+ |

## Responsibility

Hold the native COOLBOY12 implementation.

## Architectural role

Code realizes architecture; it never decides it. Implementation before architecture is anti-ordering X-04.

## What belongs here

- the `coolboy12` package

## What does not belong here

- canonical data
- architecture decisions not first authored in `docs/`

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
