# PURPOSE - `docs/`

| | |
|---|---|
| Directory | `docs/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P0+ |

## Responsibility

Hold the authored architecture of COOLBOY12 - specifications, contracts, boundary declarations and conventions.

## Architectural role

The authoring layer. A specification here is authoritative about architecture, is never rebuilt, and is superseded rather than deleted (PART I).

## What belongs here

- architecture specifications
- contracts
- boundary declarations
- conventions

## What does not belong here

- implementation detail - that belongs in `src/`
- canonical Records - those belong in `canon/`
- rebuildable output - that belongs in `derived/`

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
