# PURPOSE - `docs/constitution/`

| | |
|---|---|
| Directory | `docs/constitution/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P1 |

## Responsibility

Hold the Record System constitution and the Bootstrap Meta-Contract.

## Architectural role

The constitutional layer standing above the six sovereign Record Models. The Bootstrap Meta-Contract is constitutional and is NOT a Record (RMS sec.10.4).

## What belongs here

- the Record System constitution
- the Bootstrap Meta-Contract specification

## What does not belong here

- Record Model semantics - those belong in `docs/models/`
- Registry definition Records - those belong in `canon/registry/`
- any treatment of the Bootstrap Meta-Contract as a Record

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
