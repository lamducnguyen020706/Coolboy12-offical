# PURPOSE - `src/coolboy12/epistemic/`

| | |
|---|---|
| Directory | `src/coolboy12/epistemic/` |
| Owner | the implementing layer |
| Record Model | E |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P10 |

## Responsibility

Implement Epistemic Record Model behaviour.

## Architectural role

Authoritative over epistemic state, never over truth (RMS sec.8.2).

## What belongs here

- the seven E Kinds
- the tracking test and selective materialization
- evidence and epistemic transitions

## What does not belong here

- canonical data
- any assertion of world truth
- materialization of untracked knowledge

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
