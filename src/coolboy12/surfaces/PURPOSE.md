# PURPOSE - `src/coolboy12/surfaces/`

| | |
|---|---|
| Directory | `src/coolboy12/surfaces/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P17 |

## Responsibility

Implement the two surfaces.

## Architectural role

Surface 1 is the operator environment; Surface 2 is a publication viewer, not an application. They share a universe and share nothing else (Blueprint sec.27.5).

## What belongs here

- operator surface implementation
- publication surface implementation

## What does not belong here

- canonical data
- operator-surface content in the publication surface (X-21)
- any interaction that creates truth

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
