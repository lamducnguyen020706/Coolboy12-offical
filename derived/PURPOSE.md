# PURPOSE - `derived/`

| | |
|---|---|
| Directory | `derived/` |
| Owner | the consuming model |
| Record Model | n/a |
| Source-of-truth class | DERIVED |
| Rebuildable | Always |
| Write | rebuild process |
| Delete | Freely |
| Prohibited | anything unrebuildable |
| Introduced by phase | P8 |

## Responsibility

Hold rebuildable output derived from canon.

## Architectural role

This directory can be deleted in its entirety and rebuilt from canon alone (Blueprint sec.29.8). Nothing here is ever authoritative.

## What belongs here

- output that can be rebuilt from canon alone

## What does not belong here

- anything unrebuildable
- any authority claim - a derived thing promoted to authority is X-02
- anything whose loss would lose information

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
