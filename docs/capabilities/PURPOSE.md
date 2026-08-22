# PURPOSE - `docs/capabilities/`

| | |
|---|---|
| Directory | `docs/capabilities/` |
| Owner | authoring layer |
| Record Model | P |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P16 |

## Responsibility

Hold the specifications for AI coworkers, the Workflow Composer, the Context Builder and Creative Memory.

## Architectural role

A capability operates on Records and is not one. Recording a capability definition never confers modelhood (RMS sec.19, sec.10.5).

## What belongs here

- coworker role specifications and their boundary definitions
- Workflow Composer, Context Builder and memory specifications

## What does not belong here

- any capability treated as a Record Model or a Kind
- capability implementations - those belong in `src/coolboy12/capabilities/`
- any capability write path bypassing the Mutation Coordinator

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
