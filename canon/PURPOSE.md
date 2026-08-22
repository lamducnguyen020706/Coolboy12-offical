# PURPOSE - `canon/`

| | |
|---|---|
| Directory | `canon/` |
| Owner | the six Record Models |
| Record Model | W/E/P/R/V/I |
| Source-of-truth class | AUTHORITATIVE |
| Rebuildable | No |
| Write | Mutation Coordinator only |
| Delete | Never - a Record is retired, not deleted |
| Prohibited | derived output, drafts, external material |
| Introduced by phase | P5 |

## Responsibility

Hold the authoritative Records of the six sovereign Record Models, one partition each.

## Architectural role

The only authoritative store in the repository. Every write passes through the Mutation Coordinator - a second write path is a second canon (Spine law 2).

## What belongs here

- canonical Records of W, E, P, R, V and I, each only after that model's own canonical gate

## What does not belong here

- any write not routed through the Mutation Coordinator
- any canonical data before that model's canonical gate (PART X)
- derived output, drafts or external material
- deletion of a Record - a Record is retired, never removed

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
