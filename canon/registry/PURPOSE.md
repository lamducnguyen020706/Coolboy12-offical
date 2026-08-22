# PURPOSE - `canon/registry/`

| | |
|---|---|
| Directory | `canon/registry/` |
| Owner | R - Registry |
| Record Model | R |
| Source-of-truth class | AUTHORITATIVE |
| Rebuildable | No |
| Write | Mutation Coordinator only |
| Delete | Never - a Record is retired, not deleted |
| Prohibited | domain instances of W/E/P/V/I |
| Introduced by phase | P3 |

## Responsibility

Hold Registry Records - the semantic-definition Records that fix what the system means.

## Architectural role

Canon about meaning only. Registry may reference other Registry definitions, declared Models, Kinds and schemas; it may never reference domain instances (RMS sec.10.3). Licensed by G-REG.

## What belongs here

- Records of the fourteen Registry definition families

## What does not belong here

- domain instances of W, E, P, V or I (X-09)
- any Registry Record overriding World Truth
- runtime schema execution

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
