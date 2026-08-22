# PURPOSE - `docs/models/world/`

| | |
|---|---|
| Directory | `docs/models/world/` |
| Owner | authoring layer |
| Record Model | W |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the World Record Model architecture - the model that answers, alone, whether something is true of the world.

## Architectural role

World is LOCKED at maturity Level 5. Later work is conformance and migration, never World redesign (RMS sec.7).

## What belongs here

- the seven instance-bearing World Kinds and the WSV singleton
- the World Relationship Record and World History Record architecture
- World field mutation classes and identity operations

## What does not belong here

- any field referencing an issue, tier, medium, artifact or the real world - manifestation-blindness (RMS sec.7)
- export of the World Relationship Record or World History Record to another model (I-102)
- redesign of World semantics

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
