# PURPOSE - `src/coolboy12/registry/`

| | |
|---|---|
| Directory | `src/coolboy12/registry/` |
| Owner | the implementing layer |
| Record Model | R |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P3 |

## Responsibility

Implement Registry definition management and resolution.

## Architectural role

Registry defines; it does not execute schemas (RMS sec.10.2). Definition management is the R-specific capability.

## What belongs here

- definition management
- definition resolution
- the Registry reference-boundary validator

## What does not belong here

- canonical data
- domain instances of any model
- schema execution as Registry runtime

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
