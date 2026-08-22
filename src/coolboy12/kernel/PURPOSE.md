# PURPOSE - `src/coolboy12/kernel/`

| | |
|---|---|
| Directory | `src/coolboy12/kernel/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P2 |

## Responsibility

Implement the universal mechanism layer - identity, addressing, parsing, resolution, serialization, provenance capture.

## Architectural role

A mechanism may be shared; a semantic may not be shared without evidence in each model that carries it (RMS sec.3, I-103).

## What belongs here

- identity minting, parsing and resolution
- the serialization envelope
- reference resolution and provenance capture

## What does not belong here

- canonical data
- any model semantic
- an eighth universal envelope field - the envelope is seven fields (RMS sec.4)

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
