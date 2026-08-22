# PURPOSE - `src/coolboy12/validation/`

| | |
|---|---|
| Directory | `src/coolboy12/validation/` |
| Owner | the implementing layer |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canonical data |
| Introduced by phase | P4 |

## Responsibility

Implement the universal validation framework and structural validation.

## Architectural role

Structural validation is universal; semantic validation is model-owned. A universal semantic validator is anti-ordering X-17.

## What belongs here

- the validation framework and its plug-in contract
- structural, well-formedness validation

## What does not belong here

- canonical data
- a universal semantic validator
- collapsing a constraint into its check (RMS sec.10.6)

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
