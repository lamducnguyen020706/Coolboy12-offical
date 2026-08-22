# PURPOSE - `src/coolboy12/world/`

| | |
|---|---|
| Directory | `src/coolboy12/world/` |
| Owner | the implementing layer |
| Record Model | W |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P7 |

## Responsibility

Implement World Record Model behaviour.

## Architectural role

World is locked at Level 5; this layer conforms to it rather than redesigning it (RMS sec.7).

## What belongs here

- World Kind behaviour
- World Relationship Record and World History Record behaviour
- World identity operations - supersede, merge, split, retire

## What does not belong here

- canonical data
- export of World mechanisms to another model (X-08)
- any reference to an issue, tier, medium, artifact or the real world

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
