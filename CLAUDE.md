# COOLBOY12 — Standing Instructions

**Artifact 004 · `CLAUDE.md` standing instructions · `/CLAUDE.md`**
Own: CONST · RM: n/a · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P0/0a · Req: BR-01,BR-07,BR-17 · BP: §7,§10,§13 · RMS: §2 ·
H: 003 · S: — · LS: — · G: — · → all · Risk: HINGE · ∥: no

This file is every session's only guaranteed input. Read it before touching the project.

**This document is operational, not architectural.** It governs how a session begins work,
not what is true. `Auth: governing` binds *session conduct*; it grants no authority over the
Blueprint or RMS, and nothing here can override them.

```
Master Blueprint + RMS      architectural authority
        ↓
Repaired Roadmap            build decomposition and order
        ↓
Artifact + Phase Conventions   how an artifact entry is expressed (Artifact 003)
        ↓
CLAUDE.md                   standing operational instructions   ← this file
        ↓
implementation
```

---

## Read First

Before any architectural work, check:

1. the current **Master Blueprint**
2. the current **Record Model System (RMS)**
3. the current **Repaired Roadmap**
4. **Artifact + Phase Conventions** (Artifact 003, `docs/conventions/artifact_conventions.md`)
5. the artifact's own **declared dependencies** and any relevant existing artifact

This is not a mandate to reread all 490 manifest entries every session. Read the governing
source relevant to the task, then the artifact's declared dependencies, then the repository,
then implement, then validate:

```
read governing source for the task
   ↓
read the artifact's declared dependencies (H/S/LS/G)
   ↓
inspect the repository
   ↓
implement
   ↓
validate
```

---

## Source of Truth and Authority

Blueprint and RMS are architectural authority. The Roadmap decomposes implementation from
them. Artifact 003 fixes how that decomposition is expressed. This file is standing
operational instruction beneath all four.

- **Blueprint / RMS = architectural authority.** They decide what is true of the system.
- **Roadmap = build decomposition and order.** It decides what gets built when.
- **Artifact 003 = artifact authoring convention.** It decides how a manifest entry is written.
- **CLAUDE.md = standing operational instructions.** It decides how a session conducts itself.

If a conflict is found between sources: **do not silently reinterpret it, do not "fix" the
architecture locally, report the conflict, and preserve source authority** — see Conflict
Handling below.

---

## Repository / Artifact Rules

### Artifact-first build discipline

Work from the Roadmap artifact manifest. Do not improvise scope.

```
identify artifact
   ↓
read its exact manifest entry
   ↓
check H / S / LS / G
   ↓
read the cited Blueprint / RMS sections
   ↓
inspect existing artifacts
   ↓
build only that artifact
   ↓
validate against Val / Done
```

**"While I am here, I will also build..." is not permitted.** An unrelated later artifact is
not built early because it happens to be convenient, related, or already understood.

### Purpose-file convention

Every repository directory carries a purpose file named **`PURPOSE.md`**. This is the
convention Artifact 001 established, and the Revolving Resolution Note records at GAP-D and
GAP-D.1 (author ruling: keep `PURPOSE.md`). Coverage is complete: 68 of 68 directories at the
time of writing. Do not introduce `purpose.md`, `purpose.txt`, or any alternative naming, and
do not rename existing `PURPOSE.md` files without an explicit author instruction that
acknowledges it changes a completed artifact.

---

## Build Workflow

1. Identify the artifact.
2. Inspect its manifest entry.
3. Verify dependencies (`H`/`S`/`LS`/`G`).
4. Read the authoritative source sections it cites.
5. Inspect repository state.
6. Implement only the declared scope.
7. Validate against `Val` and `Done`.
8. Inspect `git diff` / `git status`.
9. Report the exact result.

Do not report completion from file creation alone. For a documentation artifact, validate
required sections, required terminology, required links, metadata, source citations, and
scope boundaries. For a code or config artifact, run the checks the artifact itself defines.
Generating a test is not running it; generating a drill is not executing it; generating a
benchmark is not measuring it — do not claim runtime validation an artifact has not received.

---

## Metadata and Artifact Conventions

Every manifest entry states **all 25 fields** defined by Artifact 003 — no inheritance from a
header or neighbour, no blank field. Use `n/a` where a field is genuinely not applicable and
`—` where a relational field declares nothing, per Artifact 003's null rule. Full field
definitions, legal vocabularies, and worked examples live in
[`docs/conventions/artifact_conventions.md`](docs/conventions/artifact_conventions.md); they
are not restated here.

**Current build resolution: 25 explicit fields.** The Roadmap states 27 in one place and 25 in
another; the enumerated set contains 25. This is a build convention carried from the Revolving
Resolution Note, not a constitutional amendment to the Roadmap. Do not invent fields 26 or 27.

### Artifact granularity

Artifact boundaries are governed by Artifact 003's RULE G, G2 and G3:

- **specification ≠ schema** — different owner, lifecycle, validation; always two artifacts.
- **example ≠ test** — an example shows correct use; a test proves enforcement; always two
  artifacts.
- **many files → one artifact** only when responsibility, lifecycle, ownership, and validation
  are all shared, and the merge is declared explicitly at the entry.

Do not reproduce Artifact 003 here. Read it.

### Dependency / gate discipline

```
H   hard dependency    must exist before this can be authored or finalized
S   soft dependency    supporting context, not a blocker
LS  lockstep           must land together in one authoring cycle (LS-1 … LS-8)
G   gate               must be passed before this may legally proceed
→   unlocks            what this artifact enables once complete
```

- Do not promote a soft dependency to hard.
- Do not invent a lockstep group. Membership comes from the Roadmap's declaration.
- Do not invent a gate.
- **Do not bypass a gate because dependencies are satisfied** — a dependency answers "what
  must exist," a gate answers "what must be passed." They are never substitutes for each
  other.
- **Do not treat an unlock as permission to ignore a gate.** `→` says what becomes possible,
  not what becomes legal without its own gate.

---

## Record Model Boundaries

There are exactly **six sovereign Record Models**. No model is a superclass of another and
nothing inherits from World.

| Code | Model | The question it alone answers |
|---|---|---|
| **W** | World | What is true of the world? |
| **E** | Epistemic | Who knows, believes, suspects, or has been shown what? |
| **P** | Production | What is intended, planned, coordinated, and in production? |
| **R** | Registry | What does the system mean, and how are Record semantics defined? |
| **V** | Visual | How is World Truth visually specified and represented? |
| **I** | Issue | What was published, and how is that publication composed? |

- **Do not create a seventh Record Model.**
- Do not move a responsibility between models for convenience. Ownership is architectural, not
  a filing choice.
- **Do not universalize model-owned semantics.** Lifecycle, temporal mechanism, relationship
  representation, and state vocabulary are deliberately not the same across models.

This is a boundary reminder, not the specification. Full architecture is in the Blueprint and
RMS; per-model detail is docs/models/**.

### Authority ≠ canonicality ≠ source-of-truth class

Three different questions, never collapsed into one:

```
authority              who may commit / what a Record governs
canonicality           whether content is canon, and about what — model-defined
source-of-truth class  where a thing is held: AUTHORITATIVE / DERIVED / CACHED /
                        TEMPORARY / EXTERNAL / DEV-ENV — a repository property
```

`SoT: AUTHORITATIVE` does **not** mean World Canon — a specification in `docs/**` is
authoritative about architecture and `Canon: n/a`. `SoT: DEV-ENV` does **not** mean the
artifact lacks architectural weight — this file is `SoT: AUTHORITATIVE`, `Auth: governing`,
and `Canon: n/a`, all three true at once. **Record is not automatically Canon.** See
Blueprint §13.0 and Artifact 003's field definitions for `SoT`, `Auth`, `Canon`.

---

## Canonical Data Safety

- **Do not write canonical records directly.** Every canonical write passes through the
  governed Mutation Coordinator path — there is no second write path.
- **Do not bypass the governed mutation path** for convenience, speed, or because "it's just a
  test."
- **Do not weaken or disable canonical-write restrictions** to make development easier. A
  restriction that is inconvenient is a restriction working as designed.
- **Do not place implementation artifacts into canonical-data zones.** `canon/**` holds
  canonical Records once each model's own canonical gate has passed, and its `PURPOSE.md`
  files — nothing else, and nothing before the gate.

This file does not define the mutation protocol. The authoritative mutation and canonical-
boundary artifacts do, when built (Roadmap P5, artifacts 145–166).

---

## Conflict Handling

```
SOURCE CONFLICT
      ↓
identify the exact documents / sections in conflict
      ↓
do not silently choose an interpretation
      ↓
follow the established authority precedence
      ↓
if unresolved, report the conflict
      ↓
continue only where the artifact at hand is not blocked by it
```

This file is not a decision log. Current build resolutions are recorded in the
**Revolving Resolution Note**
([`docs/conventions/revolving_resolution_note.md`](docs/conventions/revolving_resolution_note.md)),
not here.

---

## No Invention

When a source does not define something, do not fill the gap with generic architecture
knowledge or assumed convention.

```
identify the gap
   ↓
check whether another authoritative source defines it
   ↓
if not, report it
```

Especially for: requirements, metadata, Kind taxonomy, gates, lockstep, dependencies,
canonicality, and model ownership. **Do not invent a value merely because an artifact needs
one to proceed.**

### Requirement register

Requirement IDs (`BR-nn`) are stated in the Roadmap and are preserved exactly. The requirement
register defining their full text is **not currently available** — this is GAP-C in the
Revolving Resolution Note, status NON-BLOCKING — UNVERIFIED. Do not invent requirement text.
Do not claim an artifact has been verified against requirement text that has not been read.

### No silent architecture changes

Agents must not: change Blueprint semantics · change RMS semantics · silently reinterpret
Roadmap architecture · invent missing definitions · invent requirement meanings · create a new
Record Model · create a new gate · create a new lockstep group · invent a new metadata field ·
revive retired terminology as current architecture.

### No COM terminology as current architecture

The governing architecture is the Record System — six sovereign Record Models, no universal
object. Do not use, as **current** architecture: Canon Object Model · COM · universal Canon
Object · universal lifecycle · universal canonicality · universal relationship semantics ·
universal history semantics. Where a historical document uses this terminology, it is
historical context, not current architecture — and historical source documents are never
rewritten to remove it.

---

## Validation and Git Discipline

Validate every artifact against: its own `Val` and `Done` · Artifact 003's metadata
conventions · the Blueprint/RMS sections it cites · actual repository state. File creation
alone is not evidence of completion.

**Git:**

- Inspect `git status` before and after work.
- Do not modify a file outside the current artifact's declared scope.
- Do not commit unless explicitly instructed.
- Git history is not an architectural source of truth. It records that files changed, never
  what canonically changed.

---

## Current Build Resolutions

Full reasoning lives in the Revolving Resolution Note. Summary only:

| | Current resolution |
|---|---|
| **Metadata** | 25-field working convention (Artifact 003) |
| **Purpose files** | `PURPOSE.md`, every directory |
| **Production Kind count** | 13 RMS-frozen baseline + VERDICT as a provisional roadmap-level extension, pending formal RMS admission |
| **Requirement register** | missing · non-blocking · unverified (GAP-C) |

None of these is a constitutional amendment. Each is superseded by whatever formally resolves
it at source.

---

## What Not to Do

Do not put into this file: the complete Blueprint · the complete RMS · the 490-artifact
Roadmap · Record Model schemas · Registry schemas · detailed World Truth · the detailed
mutation protocol · detailed validation implementation · API documentation · generated source
code · canonical records · a temporary decision presented as constitutional truth · invented
requirement text · a future artifact described as already built.

**Current completed foundation, as of this artifact:**

```
001  repository tree
002  README.md
003  artifact + phase conventions
004  this file
```

Nothing at 005 or beyond exists unless repository inspection proves otherwise. Nothing here
claims a runtime, a test suite executed, or a system operational — none of that exists yet.

This file is the standing operational layer. It is smaller than, and subordinate to, the
Blueprint and the RMS. Where it and they differ, they are right and this file is wrong.
