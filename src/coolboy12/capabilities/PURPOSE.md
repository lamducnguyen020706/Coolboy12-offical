# PURPOSE - `src/coolboy12/capabilities/`

| | |
|---|---|
| Directory | `src/coolboy12/capabilities/` |
| Owner | the implementing layer |
| Record Model | P |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P16 |

## Responsibility

Implement capabilities - AI coworker roles, the Workflow Composer and Creative Memory.

## Architectural role

A capability operates on Records and is not one (RMS sec.19). No capability writes canon except through the Mutation Coordinator (X-11).

## What belongs here

- coworker role implementations bounded by their role boundary definitions
- Workflow Composer
- Creative Memory

## What does not belong here

- canonical data
- any capability write path bypassing the Mutation Coordinator
- unattended autonomous canon writes (X-12)

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
