# PURPOSE - `src/coolboy12/bootstrap/`

| | |
|---|---|
| Directory | `src/coolboy12/bootstrap/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P1 |

## Responsibility

Implement configuration loading and the bootstrap sequence.

## Architectural role

The Bootstrap Meta-Contract is constitutional and is not a Record; this layer implements the sequence beneath it (RMS sec.10.4).

## What belongs here

- configuration loading
- bootstrap sequence implementation

## What does not belong here

- canonical data
- any treatment of the meta-contract as a Record
- secrets

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
