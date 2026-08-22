# PURPOSE - `docs/models/production/`

| | |
|---|---|
| Directory | `docs/models/production/` |
| Owner | authoring layer |
| Record Model | P |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the Production Record Model architecture - intent, plan, coordination and production reality.

## Architectural role

An arc is a plan for telling, not a fact of the universe. Production State changes at production ceremony, never at the Human Gate, and never becomes World Canon (RMS sec.9).

## What belongs here

- the Production Kinds. RMS sec.9.1 freezes this taxonomy at thirteen; Roadmap artifact 405 admits VERDICT as a fourteenth at P15. That is a recorded source conflict and Artifact 001 does not decide it
- production ceremony, authored revision and workflow transition semantics

## What does not belong here

- any claim to World Canon by any route
- a generic ARTIFACT Kind (RMS sec.9.1)
- a CONTEXT Kind - context is a derived production artifact (RMS sec.9.1)

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
