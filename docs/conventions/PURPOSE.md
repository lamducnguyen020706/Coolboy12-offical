# PURPOSE - `docs/conventions/`

| | |
|---|---|
| Directory | `docs/conventions/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P0 |

## Responsibility

Hold the artifact, phase, role, rebuild and restart conventions the whole build cites.

## Architectural role

Conventions fix vocabulary and procedure before they are used. Artifact 003 fixes the artifact metadata set here.

## What belongs here

- artifact and phase conventions
- role conventions
- restart and recovery conventions
- rebuild conventions

## What does not belong here

- boundary declarations - those belong in `docs/boundaries/`
- the architecture of any Record Model

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
