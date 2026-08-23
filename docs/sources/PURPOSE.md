# PURPOSE - `docs/sources/`

| | |
|---|---|
| Directory | `docs/sources/` |
| Owner | authoring layer |
| Record Model | n/a |
| Source-of-truth class | AUTHORITATIVE |
| Rebuildable | No |
| Write | authored (external) |
| Delete | supersede only |
| Prohibited | modified source text, implementation detail, a fourth authority |
| Introduced by phase | n/a — not a Roadmap-numbered artifact |

## Responsibility

Hold verbatim reference copies of the three authoritative source documents that govern the
entire COOLBOY12 build: the Master Blueprint, the Record Model System, and the OS File Build
Roadmap.

## Architectural role

These three documents are the sources every artifact's `BP:`, `RMS:`, and Roadmap-row citations
point to. This directory holds them so a session can cite a stable in-repository path instead of
a session-external upload location. It does not interpret them, summarize them, or amend them —
that is every other artifact's job, working from these copies.

**Authority order is unchanged by this directory's existence:** Blueprint > RMS > Roadmap >
Artifact 003 conventions > CLAUDE.md > Resolution Note > implementation, exactly as CLAUDE.md
states it. Placing these files under `docs/**` does not make `docs/sources/` a fourth authority,
and does not change any of the three documents' own precedence relative to each other.

## What belongs here

- an exact, unmodified copy of the current Master Blueprint
- an exact, unmodified copy of the current Record Model System
- an exact, unmodified copy of the current OS File Build Roadmap

## What does not belong here

- artifact-derived interpretation of these documents — that belongs in `docs/constitution/`,
  `docs/conventions/`, `docs/boundaries/`, or the relevant `docs/models/**` subtree
- a modified, reworded, or excerpted version of any source document
- any document that is not one of the three named authorities
- implementation detail

## Placement note

No Blueprint, RMS, or Roadmap section specifies a repository location for the source documents
themselves — they are external inputs to the build, not artifacts in the 490-artifact manifest.
This directory's existence and naming are therefore an author-resolved placement decision, not a
Roadmap requirement, recorded in the Revolving Resolution Note. It does not add a Roadmap
artifact, does not change any artifact's dependencies, and is not a target of any artifact's
`H:`, `S:`, or `G:` field.

---

*Structural metadata only. This file is not canonical data, not a Record, not an authority
source, not world truth, and not a semantic definition. This directory was not created by
Artifact 001 and is not part of the 68-directory PART I tree; its placement is a session-level
author decision, recorded in the Revolving Resolution Note.*
