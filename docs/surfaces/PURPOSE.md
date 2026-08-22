# PURPOSE - `docs/surfaces/`

| | |
|---|---|
| Directory | `docs/surfaces/` |
| Owner | authoring layer |
| Record Model | P |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P17 |

## Responsibility

Hold single-author UX principles and the Two Surfaces contract.

## Architectural role

There are two products sharing a universe and sharing nothing else. Conflating them is the single most likely way the artifact ambition fails (Blueprint sec.27.5).

## What belongs here

- UX principles
- the Two Surfaces contract and its exposure set

## What does not belong here

- operator-surface content appearing in the publication surface (X-21)
- surface implementations - those belong in `src/coolboy12/surfaces/`

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
