# COOLBOY12 — Standing Instructions

## Artifact Identity

```
ID:     004
Name:   CLAUDE.md standing instructions
path:   /CLAUDE.md
Own:    CONST
RM:     n/a
T:      doc
R:      CONTRACT
SoT:    AUTHORITATIVE
Auth:   governing
Canon:  n/a
CD:     no
Ph/St:  P0/0a
Req:    BR-01,BR-07,BR-17
BP:     §7,§10,§13
RMS:    §2
H:      003
S:      —
LS:     —
G:      —
→:      all
Val:    carries ten Spine laws, six models, AD-1, Record≠Canon, RR/HR World-only, I-101…I-108
Done:   cold session reads correct law
Why:    every session's only guaranteed input
Risk:   HINGE
∥:      no
```

Twenty-five fields, per Artifact 003. No inheritance, no blank field, no hidden metadata.

---

## What This File Governs

**CLAUDE.md governs HOW A SESSION WORKS.** Nothing more.

| Source | Governs |
|---|---|
| Blueprint + RMS | **what is true** |
| Repaired Roadmap | **what gets built when** |
| Artifact + Phase Conventions (003) | **how an artifact is expressed** |
| CLAUDE.md | **how a session conducts itself** |

> **`Auth: governing` on CLAUDE.md binds session conduct. It grants no authority over the
> Blueprint or RMS.**

Read this file first in every session. It is the only guaranteed input.

---

## Authority Hierarchy

```
Master Blueprint + RMS
        ↓                architectural authority
Repaired Roadmap
        ↓                build decomposition and order
Artifact + Phase Conventions
        ↓                artifact expression rules
CLAUDE.md
        ↓                standing operational instructions
implementation
```

This file MUST NEVER override a layer above it. Where it and they differ, **they are right and
this file is wrong.**

---

## Read First

Before any architectural work, read:

1. the current **Master Blueprint**
2. the current **Record Model System (RMS)**
3. the current **Repaired Roadmap**
4. **Artifact + Phase Conventions** — [`docs/conventions/artifact_conventions.md`](docs/conventions/artifact_conventions.md)
5. the artifact's own declared dependencies and any relevant existing artifact

**Do NOT reread all 490 manifest entries every session.** The rule is:

```
read the governing source relevant to the task
        ↓
read Artifact 003
        ↓
read the current artifact's H / S / LS / G
        ↓
inspect relevant existing artifacts
        ↓
inspect repository state
        ↓
implement only declared scope
        ↓
validate against Val / Done
        ↓
inspect git diff / git status
        ↓
report exact result
```

---

## Source of Truth and Authority

- **Blueprint / RMS** decide what is true of the system. Architectural authority.
- **Roadmap** decides what gets built when. Build decomposition and order.
- **Artifact 003** decides how a manifest entry is written. Expression only.
- **CLAUDE.md** decides how a session conducts itself. Conduct only.

### The Spine — ten laws, unamended

The frozen constitutional core (Blueprint §10). A session MUST NOT violate any of them.

| # | Law | Rule |
|---|---|---|
| 1 | **One Canon** | Exactly one canonical truth about the universe. No parallel canon, no duplicate truth, no second source. |
| 2 | **One Path** | Canon changes only through *propose → check → human gate → commit → changelog → log*. No other route; the commit is atomic. |
| 3 | **One Authority** | Only the human commits canon. No AI output, simulation result, deadline, or report is canonical until the human gates it. |
| 4 | **The Foundation Lock** | Foundation truths are immutable except through deliberate ceremony. If generated content contradicts a Foundation truth, the content is wrong. |
| 5 | **The Publishing Firewall** | Published artifacts are in-world manifestations. They reference canon one-directionally; they never become canon. |
| 6 | **Provisional by Default** | Every AI proposal, simulation delta, and emergent seed is provisional until gated. Every AI action is advisory unless explicitly approved. |
| 7 | **The Severity Floor** | Changes to a Foundation truth, relationship topology, a load-bearing mystery, or the Spine can never be treated as trivial. |
| 8 | **Every Event Propagates** | A confirmed canon change runs its consequences through the dependency graph. Propagation follows explicit relationships, not heuristics. |
| 9 | **Every Object Has Lineage** | Every Record traces to the decision that created or last changed it. A change with no recorded reason is an audit flag. |
| 10 | **Nothing Bypasses the Composer** | Every action is a composed, logged workflow. No side door. The Composer routes work *to* the human gate; it never replaces it. |

---

## Repository / Artifact Rules

### Artifact-First Build Discipline

Work from the Roadmap artifact manifest. Do not improvise scope.

```
identify artifact
        ↓
read its exact manifest entry
        ↓
check H / S / LS / G
        ↓
read cited Blueprint / RMS sections
        ↓
inspect existing artifacts
        ↓
build only that artifact
        ↓
validate against Val / Done
```

> **"While I am here, I will also build…" is PROHIBITED.**

An unrelated artifact MUST NOT be built early because it is nearby, because its dependencies
appear satisfied, because it is convenient, because the implementation is already understood,
or because the current file references it. **Scope is governed by the Roadmap.**

### Purpose-File Convention

Every repository directory carries **`PURPOSE.md`**. Current coverage: **68 / 68 directories**.

`PURPOSE.md` is: structural documentation · a directory responsibility declaration.
`PURPOSE.md` is NOT: canonical data · a Record · an authority source · World Truth · a
semantic definition.

**PROHIBITED:** `purpose.md`, `purpose.txt`, or any alternate naming. Do not rename existing
`PURPOSE.md` files without an explicit author instruction acknowledging that it changes a
completed artifact.

---

## Build Workflow

1. Identify the artifact.
2. Inspect its manifest entry.
3. Verify dependencies (`H` / `S` / `LS` / `G`).
4. Read the authoritative source sections it cites.
5. Inspect repository state.
6. Implement only the declared scope.
7. Validate against `Val` and `Done`.
8. Inspect `git diff` / `git status`.
9. Report the exact result.

---

## Metadata and Artifact Conventions

Read **Artifact 003** for the full convention:
[`docs/conventions/artifact_conventions.md`](docs/conventions/artifact_conventions.md).
Do not duplicate it here.

- Every manifest entry states **all 25 fields**.
- **No metadata inheritance** from a header, block, or neighbour.
- **No blank fields.** Use `n/a` (not applicable) and `—` (nothing declared) per Artifact 003.
- Type / Role / SoT vocabularies come from Artifact 003.
- `H` / `S` / `LS` / `G` / `→` rules come from Artifact 003.
- **RULE G / G2 / G3** govern artifact boundaries: specification ≠ schema · example ≠ test ·
  many files → one artifact only when responsibility, lifecycle, ownership, and validation are
  all shared.

**Current resolution: 25 fields.** The Roadmap contains both 27 and 25 references; Artifact 003
froze the build convention at the 25 explicitly enumerated fields. Do not invent fields 26 or
27. This is a build convention; it does not amend the Roadmap, and a future source-level
amendment may supersede it.

### Dependency / Gate Discipline

| Symbol | Meaning |
|---|---|
| `H` | **hard dependency** — must exist before this can be authored or finalized |
| `S` | **soft dependency** — supporting context, not a blocker |
| `LS` | **lockstep** — must land together in one authoring cycle |
| `G` | **gate** — must be passed before this may legally proceed |
| `→` | **unlocks** — what becomes possible after completion |

> **Dependency ≠ Gate. Unlock ≠ Gate.**

MUST NOT: treat a satisfied dependency as permission to bypass a gate · treat an unlock as
permission to ignore a gate · invent a gate · invent a lockstep system · promote a soft
dependency to hard.

---

## Record Model Boundaries

Exactly **six sovereign Record Models**:

| Code | Model | The question it alone answers |
|---|---|---|
| **W** | World | What is true of the world? |
| **E** | Epistemic | Who knows, believes, suspects, or has been shown what? |
| **P** | Production | What is intended, planned, coordinated, and in production? |
| **R** | Registry | What does the system mean, and how are Record semantics defined? |
| **V** | Visual | How is World Truth visually specified and represented? |
| **I** | Issue | What was published, and how is that publication composed? |

MUST NOT: create a seventh model · treat any model as a superclass of another · inherit
anything from World · move a responsibility between models for convenience · universalize
model-owned semantics.

This is an operational boundary reminder. Full architecture is in the Blueprint and RMS.

### RR / HR are World-only

**Relationship Record and History Record are World Record Model concepts.** Neither is a
Record System primitive, and neither may be required of another Record Model (I-102). Do not
export them. Each other model defines its own temporal and relationship mechanism.

### AD-1 — one identity grammar, model-owned semantics

```
[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]
```

Partition-first · two-character kind codes · ordinals never reused, including after
retirement · slug is decoration only.

**Universal:** syntax, positions, parsing, resolution, uniqueness, minting.
**Model-owned:** Kind meaning, Kind taxonomy, semantic interpretation, lifecycle, authority.

> **UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL.** The grammar fixes the syntax of
> the name and decides nothing about the thing named.

### Record System invariants I-101 … I-108

| ID | Invariant |
|---|---|
| **I-101** | Every partition owns exactly one sovereign Record Model. No Record Model is a specialization of another, and none is the template for another. |
| **I-102** | Relationship Record and History Record are World Record Model concepts. Neither is a Record System primitive, and neither may be required of another Record Model. |
| **I-103** | A mechanism may be shared across Record Models; a semantic may not be shared without evidence in each model that carries it. Shared infrastructure never confers shared meaning. |
| **I-104** | Record and Canon are not synonyms. Canonicality is a status property whose meaning is defined by each Record Model that has one, and two models hold Records that are never canonical. |
| **I-105** | Registry is a sovereign Record Model. Its definitions are Records, not configuration. It holds semantic authority over definitions and never semantic ownership of another model's Records. |
| **I-106** | A kind roster that is listed is not thereby frozen. Only the World taxonomy is established; every other roster names a boundary and is revisable by that model's own design work until it declares otherwise. |
| **I-107** | A package composition declared for a Record Model that has not been independently designed is provisional and may not be implemented as a requirement. |
| **I-108** | No Record carries a WSV attribute by default. An indicator definition is a Registry Record; an indicator value is World-state; neither is a universal field. |

---

## Authority ≠ Canonicality ≠ SoT

Three separate questions. Never collapse them.

```
authority              who may commit / what a Record governs
canonicality           whether something is canon, and about what — model-defined
source-of-truth class  where the thing is held:
                       AUTHORITATIVE / DERIVED / CACHED / TEMPORARY / EXTERNAL / DEV-ENV
```

- **`SoT: AUTHORITATIVE` ≠ World Canon.** A specification in `docs/**` is authoritative about
  architecture and `Canon: n/a`.
- **`SoT: DEV-ENV` ≠ architecturally irrelevant.**
- **Record ≠ automatically Canon** (I-104, Blueprint §13.0).

Otherwise a later session will collapse repository location, authority, and canon into one
concept. See Blueprint §13.0 and Artifact 003's `SoT` / `Auth` / `Canon` definitions.

---

## Canonical Data Safety

- **No direct canonical writes.** Never write canonical Records directly. All canonical
  mutation passes through the governed Mutation Coordinator path (Spine law 2) once that
  architecture exists.
- **No bypass** — not for convenience, tests, speed, or development ease. Do not weaken or
  disable canonical-write restrictions.
- **No implementation files inside canonical zones.** `canon/**` is the canonical-data zone
  plus its established `PURPOSE.md` documentation. Nothing else, and nothing before that
  model's own canonical gate.

**The Mutation Coordinator is NOT yet implemented.** It is Roadmap P5 (artifacts 145–166). The
rules above are current operational rules; the mechanism arrives later. Do not claim it exists.

---

## Conflict Handling

```
SOURCE CONFLICT
        ↓
identify exact documents / sections
        ↓
do not silently choose an interpretation
        ↓
follow source authority precedence
        ↓
if unresolved, report the conflict
        ↓
continue only if the current artifact is not blocked
```

Blueprint/RMS remain architectural authority · Roadmap is build decomposition and order ·
Artifact 003 governs artifact expression · CLAUDE.md governs session conduct.

**This file is not a decision log.** Current build resolutions live in
[`docs/conventions/revolving_resolution_note.md`](docs/conventions/revolving_resolution_note.md).

---

## No Invention

When a source does not define something:

```
identify the gap
        ↓
check whether another authoritative source defines it
        ↓
if not → report it
```

MUST NOT fill gaps with: generic architecture assumptions · common software patterns ·
invented field definitions · invented requirement meanings · invented gate semantics ·
invented lockstep relationships · invented canonicality · invented model ownership.

### Requirement Register

The Roadmap states requirement IDs (`BR-nn`); the authoritative requirement register is **not
currently available**.

- Preserve requirement IDs exactly.
- Do not invent requirement text.
- Do not claim verification against unavailable requirement definitions.
- GAP-C does not currently block the build. Status: missing · non-blocking · unverified.

### No Silent Architecture Changes

Agents MUST NOT: change Blueprint semantics · change RMS semantics · silently reinterpret
Roadmap architecture · invent missing definitions · invent requirement meanings · create a new
Record Model · create a new gate · create a new lockstep group · invent a new metadata field ·
revive retired terminology as current architecture.

If architecture needs to change: **stop → identify the source conflict → report it → do not
patch architecture locally.**

### No COM Terminology as Current Architecture

The governing architecture is the Record System. MUST NOT use as **current** architecture:
Canon Object Model · COM · universal Canon Object · universal lifecycle · universal
canonicality · universal relationship semantics · universal history semantics.

Historical Blueprint text may still contain historical terminology. **Do not rewrite historical
source documents to remove it.** This rule applies to current implementation language.

---

## Validation and Git Discipline

Validate every artifact against: its own `Val` · its own `Done` · Artifact 003 conventions ·
the cited Blueprint/RMS sections · actual repository state.

> **File creation alone is not evidence of completion.**

**Documentation artifacts** — validate required sections, required terminology, required links,
metadata, source citations, scope boundary.
**Code / config artifacts** — execute the checks the artifact defines.

```
generating a test      ≠  running the test
generating a drill     ≠  executing the drill
generating a benchmark ≠  measuring the benchmark
```

Do not claim runtime validation unless runtime validation actually occurred.

**Git:** `git status` before work → work → `git diff` / `git status` after work.

- Do not modify files outside the current artifact's scope.
- Do not commit unless explicitly instructed.
- Git history is not architectural authority. It records file changes, never canonical meaning.

---

## Current Build Resolutions

| Area | Current resolution |
|---|---|
| Metadata | 25-field working convention |
| Purpose files | `PURPOSE.md`, every directory |
| Production taxonomy | 13 RMS-frozen baseline + VERDICT as provisional roadmap extension, pending formal RMS admission |
| Requirement register | missing · non-blocking · unverified |

**These are build resolutions, not constitutional amendments.** Detailed reasoning stays in the
Revolving Resolution Note.

---

## What Not to Do

MUST NOT put into this file: complete Blueprint text · complete RMS text · the complete
490-artifact Roadmap · Record Model schemas · Registry schemas · detailed World Truth · the
detailed mutation protocol · detailed validation implementation · API documentation · generated
source code · canonical Records · a temporary decision presented as constitutional truth ·
invented requirement definitions · future artifacts represented as already complete.

Summarize a boundary; point deeper architecture back to the authoritative source.

---

## Current Foundation Status

```
001  repository tree
002  README.md
003  artifact + phase conventions
004  CLAUDE.md   ← this file
```

Nothing after Artifact 004 exists unless repository inspection proves it. There is **no
runtime**, **no executed test suite**, **no operational system**, and **no completed later
phase**. Artifact 004 is the standing operational layer, not the runtime.
