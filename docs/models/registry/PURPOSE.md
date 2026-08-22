# PURPOSE - `docs/models/registry/`

| | |
|---|---|
| Directory | `docs/models/registry/` |
| Owner | authoring layer |
| Record Model | R |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the Registry Record Model architecture - the sovereign model whose Records define meaning.

## Architectural role

Registry is a sovereign Record Model, not a capability and not infrastructure (RMS sec.10, I-105). It is canon about meaning only and can never override World Truth.

## What belongs here

- the fourteen Registry definition families
- the Registry reference boundary
- the schema boundary and the constraint/validation split

## What does not belong here

- domain instances of W, E, P, V or I (RMS sec.10.3)
- schema execution - Registry defines, it does not execute (RMS sec.10.2)
- authority over World Truth

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
