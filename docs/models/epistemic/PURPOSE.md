# PURPOSE - `docs/models/epistemic/`

| | |
|---|---|
| Directory | `docs/models/epistemic/` |
| Owner | authoring layer |
| Record Model | E |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the Epistemic Record Model architecture - every frame upon a world-fact except the fact itself.

## Architectural role

E is authoritative over epistemic state and never over truth (RMS sec.8.2). W holds the fact; E holds every view of it.

## What belongs here

- the seven E Kinds
- the two distinct cardinalities - KNOWLEDGE-STATE keyed by (fact, knower), REVEAL-STATE keyed by fact
- model-owned epistemic transitions and evidence

## What does not belong here

- world truth - that belongs to W
- a BELIEF Kind - BELIEVED is a state in KNOWLEDGE-STATE (RMS sec.8.1)
- use of the World History Record (RMS sec.8.2)
- collapsing the two cardinalities into one

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
