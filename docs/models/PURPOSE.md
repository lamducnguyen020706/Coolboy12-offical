# PURPOSE - `docs/models/`

| | |
|---|---|
| Directory | `docs/models/` |
| Owner | authoring layer |
| Record Model | W/E/P/R/V/I |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the architecture of the six sovereign Record Models, one subdirectory each.

## Architectural role

Semantic ownership runs on W, E, P, R, V and I only. No model is a superclass of another and nothing inherits from World (RMS sec.2, sec.30).

## What belongs here

- exactly six model subdirectories: world, epistemic, production, registry, visual, issue

## What does not belong here

- a seventh sovereign Record Model
- a Universal Record Base, Universal Relationship Record or Universal History Record (RMS sec.4)
- capability specifications - those belong in `docs/capabilities/`

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
