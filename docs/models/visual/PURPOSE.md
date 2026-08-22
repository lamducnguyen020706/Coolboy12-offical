# PURPOSE - `docs/models/visual/`

| | |
|---|---|
| Directory | `docs/models/visual/` |
| Owner | authoring layer |
| Record Model | V |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the Visual Record Model architecture - the visual specification and representation of World Truth.

## Architectural role

Canonical visual identity is the description, not the file. An external image file never carries canonical visual truth (RMS sec.11, Blueprint sec.18.6).

## What belongs here

- the three V Kinds
- the analysis-to-evidence chain
- represents / derived-from / variant-of relationship semantics

## What does not belong here

- a generic file repository or media manager
- any mutation of World - Visual never mutates World (RMS sec.11.2)
- VISUAL-DERIVATIVE or VISUAL-REFERENCE as standalone Kinds

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
