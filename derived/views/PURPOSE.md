# PURPOSE - `derived/views/`

| | |
|---|---|
| Directory | `derived/views/` |
| Owner | the consuming model |
| Record Model | n/a |
| Source-of-truth class | DERIVED |
| Rebuildable | Always |
| Write | rebuild process |
| Delete | Freely |
| Prohibited | anything unrebuildable |
| Introduced by phase | P8 |

## Responsibility

Hold derived views assembled for reading.

## Architectural role

A view presents; it never establishes. Rebuildable by definition.

## What belongs here

- views rebuilt from canon

## What does not belong here

- any view treated as a source
- anything unrebuildable

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
