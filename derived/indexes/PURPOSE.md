# PURPOSE - `derived/indexes/`

| | |
|---|---|
| Directory | `derived/indexes/` |
| Owner | the consuming model |
| Record Model | n/a |
| Source-of-truth class | DERIVED |
| Rebuildable | Always |
| Write | rebuild process |
| Delete | Freely |
| Prohibited | anything unrebuildable |
| Introduced by phase | P8 |

## Responsibility

Hold mechanical retrieval indexes.

## Architectural role

Indexing is a shared mechanism and is never authoritative (RMS sec.4). An index may be deleted and rebuilt; a canon may not.

## What belongs here

- retrieval indexes rebuilt from canon

## What does not belong here

- any index treated as a source
- anything unrebuildable

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
