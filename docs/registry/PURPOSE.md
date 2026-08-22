# PURPOSE - `docs/registry/`

| | |
|---|---|
| Directory | `docs/registry/` |
| Owner | authoring layer |
| Record Model | R |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P3 |

## Responsibility

Hold the specifications for the fourteen Registry definition families.

## Architectural role

This directory specifies each definition family. `docs/models/registry/` holds the Registry Record Model architecture; this holds the family-by-family specifications derived from it.

## What belongs here

- one specification per Registry definition family

## What does not belong here

- Registry Records themselves - those are minted into `canon/registry/`
- domain instances of any other model

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
