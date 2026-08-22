# PURPOSE - `docs/models/issue/`

| | |
|---|---|
| Directory | `docs/models/issue/` |
| Owner | authoring layer |
| Record Model | I |
| Source-of-truth class | AUTHORITATIVE (specification) |
| Rebuildable | No |
| Write | authored |
| Delete | supersede only |
| Prohibited | implementation detail |
| Introduced by phase | P2+ |

## Responsibility

Hold the Issue Record Model architecture - what was published and how that publication is composed.

## Architectural role

Issue is publication reality. Publication creates no truth, and correction is a new Issue that supersedes the previous one (RMS sec.12.2).

## What belongs here

- the five I Kinds
- composition, placement, credit and supersession references

## What does not belong here

- any claim that publication creates World Canon - the Publishing Firewall
- SECTION, PAGE or SPREAD as Record Kinds - they are composition (RMS sec.12.1)
- ownership of W/E/P/V semantics, which Issue references but never owns

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
