# PURPOSE - `.claude/`

| | |
|---|---|
| Directory | `.claude/` |
| Owner | the execution environment |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV |
| Rebuildable | Yes |
| Write | authored |
| Delete | Yes |
| Prohibited | canon, secrets |
| Introduced by phase | P0 |

## Responsibility

Hold execution-environment configuration: hooks, commands and agent settings.

## Architectural role

The environment runs COOLBOY12; it does not define it (P-33, Blueprint sec.26.8). Its guard rails are defence-in-depth, never constitutional authority - where a hook and the Human Gate disagree, the gate is right and the hook is a bug.

## What belongs here

- hooks
- commands
- agent settings
- zone permission configuration

## What does not belong here

- canon
- secrets
- any COOLBOY12 semantics - the environment owns none
- any guard rail asserted as constitutional authority

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority source, not world truth, and not a semantic definition. Naming and format are an Artifact 001 implementation convention resolved by the author (GAP-D), to be formally defined by Artifact 003.*
