# PURPOSE - `docs/registry/registry_kinds/`

| | |
|---|---|
| Directory | `docs/registry/registry_kinds/` |
| Owner | authoring layer |
| Record Model | R |
| Source-of-truth class | AUTHORITATIVE (canonicalization source) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | committed Registry Records; implementation detail |
| Introduced by phase | P3 |

## Responsibility

Hold Artifact 075, the Registry Kind-Definition set: the authored canonicalization source of the
fourteen `KIND-DEFINITION`s, one per Registry Kind of Artifact 064, specified by Artifact 074 and
conforming to Artifact 069 (Roadmap row 075, §0.7, §0.8).

## What belongs here

- `registry_kind_definitions.md` — the fourteen member sources

## What does not belong here

- committed Registry Records - those are minted into `canon/registry/registry_kinds/`, only through
  the Mutation Coordinator after G-CANON-R
- any `KIND-DEFINITION` of a W, E, P, V or I Kind (rows 178, 257, 300, 345, 364)
- a fifteenth member of any kind

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source,
not world truth, not a semantic definition, and not a member of the set. Naming and format are an
Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by
Artifact 003.*
