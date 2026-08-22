# PURPOSE - `derived/caches/`

| | |
|---|---|
| Directory | `derived/caches/` |
| Owner | the consuming model |
| Record Model | n/a |
| Source-of-truth class | CACHED |
| Rebuildable | Always |
| Write | rebuild process |
| Delete | Freely |
| Prohibited | anything unrebuildable; any authority claim |
| Introduced by phase | P8 |

## Responsibility

Hold caches.

## Architectural role

Cached is not authoritative. Caching is an implementation matter (RMS sec.9.1) and its source-of-truth class is CACHED (PART VII).

## What belongs here

- caches that can be discarded at any moment

## What does not belong here

- any cached value treated as authoritative
- anything not reproducible from its source

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
