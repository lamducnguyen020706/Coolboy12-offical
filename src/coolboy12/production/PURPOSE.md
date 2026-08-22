# PURPOSE - `src/coolboy12/production/`

| | |
|---|---|
| Directory | `src/coolboy12/production/` |
| Owner | the implementing layer |
| Record Model | P |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P11 |

## Responsibility

Implement Production Record Model behaviour, including the Context Builder.

## Architectural role

Context is a derived production artifact and the Context Builder is a Production capability (RMS sec.9.1). Context bypassing Production is anti-ordering X-10.

## What belongs here

- behaviour for the admitted P Kinds
- the Context Builder
- Workflow Composer state

## What does not belong here

- canonical data
- any route by which Production becomes World Canon
- context treated as authoritative

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
