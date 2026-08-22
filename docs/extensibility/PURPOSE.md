# PURPOSE - `docs/extensibility/`

| | |
|---|---|
| Directory | `docs/extensibility/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P17 |

## Responsibility

Hold the extension and contraction contracts.

## Architectural role

An extension attaches at a declared contract; it never acquires authority.

## What belongs here

- extension contracts
- contraction contracts

## What does not belong here

- any extension holding authority over canon
- extension implementations - those belong in `src/coolboy12/extensibility/`

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
