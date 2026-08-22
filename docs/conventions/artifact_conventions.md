# COOLBOY12 — Artifact + Phase Conventions

## Status and Authority

| Field | Value |
|---|---|
| Artifact | **003** |
| Name | artifact + phase conventions |
| Own | **CONST** |
| RM | **n/a** |
| T | doc |
| R | **CONTRACT** |
| SoT | **AUTHORITATIVE** |
| Auth | **governing** |
| Canon | **n/a** |
| CD | no |
| Ph/St | P0/0a |

**What this document governs.** How artifacts are authored: their metadata, their
vocabularies, how their dependencies are declared, how phases and stages are written, and how
artifact boundaries are decided. Every later artifact in the 490-artifact manifest complies
with it.

**What this document does not do**, stated so it cannot be assumed:

- It does **not** define World Truth.
- It does **not** own any Record Model.
- It is **not** canonical data. `Canon: n/a`.
- It does **not** override the Blueprint or the Record Model System.
- It does **not** amend architecture. It fixes the *expression* of a decomposition the
  Roadmap already made.

`Auth: governing` binds authoring practice and nothing above it. A convention here can never
make an architectural statement true.

---

## Purpose

Give every artifact author one operational contract, so that the metadata gap which failed the
previous audit cannot recur. After reading this document an author knows:

```
what metadata to write
   ↓
what each field means
   ↓
what values are legal
   ↓
how to declare dependencies
   ↓
how lockstep works
   ↓
how gates work
   ↓
how phases and stages are written
   ↓
how artifact granularity is decided
```

This is an authoring reference, meant to be used directly while writing an artifact entry —
not a description of one.

---

## Source Precedence

```
Blueprint + RMS            architectural authority
   ↓
Roadmap (REPAIRED)         build decomposition and order
   ↓
Artifact + Phase Conventions   how that decomposition is expressed  ← this document
   ↓
Implementation             artifacts authored under the contract
```

**The practical rule when a later artifact meets a conflict:**

1. **Blueprint and RMS remain the architectural authority.** Neither the Roadmap nor this
   document can overrule them.
2. **The Roadmap decomposes implementation** only where it is consistent with them. Where it
   is not, the inconsistency is recorded, not silently resolved.
3. **This document defines how the decomposition is expressed** — field by field, vocabulary
   by vocabulary. It settles notation, never meaning.
4. **Implementation must not silently change any of the above.** An artifact that needs a
   different architectural reading stops and reports; it does not proceed on its own reading.

### Carried working resolution — metadata cardinality

The Roadmap states the artifact-metadata cardinality two ways. §0.4 and artifact 003's own
`Val` say **27 fields**; PART IV says **25**; the notation in §0.4 enumerates **25**. The §54
and §50 references that would settle it point to a generation brief outside the three
authoritative documents, and no fourth authority is admitted.

> **The Roadmap's "27" is a source inconsistency.** The current build convention is the
> **25 explicitly enumerated fields** frozen below. Fields 26 and 27 are not invented, and no
> false 27-field schema is preserved.

This is a **build convention, not a constitutional amendment**. The Roadmap is not modified.
It is carried from the Revolving Resolution Note (CONFLICT-B, RESOLVED FOR BUILD) and is
superseded by any formal amendment that settles the count at source.

---

## Artifact Metadata Contract

Every manifest entry states **all 25 fields, explicitly**. No field is inherited from a
section header, a block heading, a neighbouring entry, or a phase default. Block-header
inheritance is abolished.

### The 25 Fields

| # | Field | One-line meaning |
|---|---|---|
| 1 | `ID` | which artifact this is |
| 2 | `Name` | what it is called |
| 3 | `path` | where it lives |
| 4 | `Own` | which layer owns it |
| 5 | `RM` | which Record Model it belongs to or governs |
| 6 | `T` | what kind of thing it is |
| 7 | `R` | what architectural job it performs |
| 8 | `SoT` | its source-of-truth class |
| 9 | `Auth` | what authority it carries |
| 10 | `Canon` | its canonicality status |
| 11 | `CD` | whether it touches canonical data |
| 12 | `Ph/St` | which phase and stage it sits in |
| 13 | `Req` | which requirement it satisfies |
| 14 | `BP` | its Blueprint citation |
| 15 | `RMS` | its Record Model System citation |
| 16 | `H` | its hard dependencies |
| 17 | `S` | its soft dependencies |
| 18 | `LS` | its lockstep membership |
| 19 | `G` | its gate |
| 20 | `→` | what it unlocks |
| 21 | `Val` | how completion is checked |
| 22 | `Done` | what completion looks like |
| 23 | `Why` | why it exists |
| 24 | `Risk` | what is at stake |
| 25 | `∥` | whether it can be authored in parallel |

**No extra fields.** An author who believes a 26th is needed raises it rather than adding it.

### The `n/a` rule

> **A metadata field that is genuinely not applicable reads `n/a`, never blank.**

No metadata column is ever left empty. Two distinct null forms are in use and their source
semantics are preserved:

| Form | Meaning | Fields where it appears |
|---|---|---|
| `n/a` | the field does not apply to this artifact | `RM`, `RMS`, `Canon`, `Auth` |
| `—` | nothing is declared in this relational field | `H`, `S`, `LS`, `G` |

`—` in `H` means *no hard dependency is declared*, not *unknown*. Do not substitute arbitrary
text, a dash of another kind, or an empty cell for either form.

---

### Field Definitions

#### 1 · `ID`
The Roadmap artifact identifier. Three digits, `001` through `490`. Examples: `001`, `003`,
`152`, `490`. **One ID identifies exactly one manifest artifact**, and no artifact carries
two.

#### 2 · `Name`
The human-readable artifact name. It must reflect the artifact's **declared responsibility** —
a reader should be able to predict the artifact's scope from its name. Do not merge unrelated
responsibilities under one name; if the name needs an "and" joining two different jobs, the
artifact boundary is wrong and RULE G, G2 or G3 decides it.

#### 3 · `path`
The repository-relative implementation or documentation path.

- Repository-relative, always.
- It **must match the actual artifact location** on disk.
- No duplicate hidden location holding the same responsibility.
- No invented alias, shortcut, or convenience path.

Where one artifact is legitimately several files under RULE G3, `path` names the directory or
the shared prefix, and the entry states the merge explicitly.

#### 4 · `Own`
The artifact's **ownership domain** — which layer of the build is responsible for authoring
and maintaining it. Observed owners in the manifest:

`CONST` · `ADAPT` · `CAP` · `GOV` · `OPS` · `UX` · and the six Record Models `W` `E` `P` `R`
`V` `I`. Compound owners appear where two layers genuinely share it (`I,R` · `P,R` · `V,R` ·
`I,CONST`).

Do not invent new owner classes.

> **Artifact ownership is not Record Model ownership.** They are different questions and are
> answered in different fields. `Own` says who authors the artifact; `RM` says which Record
> Model's semantics it carries. So:
>
> ```
> Own: CONST
> RM:  n/a
> ```
>
> is valid and common — a constitutional artifact that carries no Record Model semantics.
> Equally, `Own: R · RM: R` and `Own: GOV · RM: P` are both legitimate.

#### 5 · `RM`
Record Model scope. Used **only** where the artifact genuinely belongs to or governs a Record
Model. The six sovereign models are exactly:

```
W   World
E   Epistemic
P   Production
R   Registry
V   Visual
I   Issue
```

`all` where an artifact serves every model; `n/a` where no Record Model applies. Compound
scopes appear where an artifact genuinely spans two (`E,I`).

**Do not derive `RM` from directory location.** A file under `docs/models/world/` is not
automatically `RM: W`, and a file outside it is not automatically `RM: n/a`. The field states
semantic scope, which the artifact's responsibility determines.

There is no seventh model, and this field never introduces one.

#### 6 · `T` — Type
What the artifact *is*. Legal values, declared at Roadmap §0.6:

`doc` · `code` · `schema` · `test` · `fixture` · `example` · `drill` · `bench` · `config`

Compound types (`doc,schema` · `code,example` · `example,test`) appear where a single
responsibility genuinely produces two forms. Do not invent new type categories.

#### 7 · `R` — Role
What architectural **job** the artifact performs. Legal values, declared at Roadmap §0.6:

| Role | Job |
|---|---|
| `ARCH` | states architecture |
| `CONTRACT` | fixes a contract others must satisfy |
| `IMPL` | implements behaviour |
| `VALID` | checks that something holds |
| `PROOF` | proves that something holds |
| `SURFACE` | exposes an entry point |
| `GOV` | governs a judged question |

> **`T` = what the artifact is. `R` = what job it does.** They are independent. A `doc` can be
> `ARCH`, `CONTRACT` or `GOV`; a `test` is usually `PROOF` but a harness is `VALID`.
>
> ```
> T: doc
> R: CONTRACT
> ```

#### 8 · `SoT` — Source-of-Truth class
Legal values, declared at Roadmap §0.6:

| Class | Meaning |
|---|---|
| `AUTHORITATIVE` | this is where the thing is true; not rebuildable; superseded, not deleted |
| `DERIVED` | recomputable from an authoritative source; freely deletable; never a source |
| `CACHED` | a discardable copy held for speed; never authoritative |
| `TEMPORARY` | short-lived working material; must never be mistaken for real content |
| `EXTERNAL` | held outside the system; enters only through a declared boundary |
| `DEV-ENV` | development and environment material; carries no COOLBOY12 semantics |

> **`AUTHORITATIVE` is not the same as canonical.** `AUTHORITATIVE` says *this file is where
> this thing is true*; it is a repository property. `Canon` says whether the content is canon
> about the world; it is an architectural property. A specification in `docs/**` is
> `AUTHORITATIVE` about architecture and `Canon: n/a`. The two fields answer different
> questions and are never collapsed.

#### 9 · `Auth` — Authority status
What authority the artifact carries. Source-backed values include:

`none` · `governing` · `defining` · `enforcing` · `gating` · `recording` · `allocating` ·
`sole writer` · and model-scoped forms such as `authoritative-world-truth`,
`authoritative-epistemic-state`, `production-state`, `publication`.

**Do not give an ordinary implementation artifact governing authority.** Most artifacts are
`Auth: none`. Authority is claimed only where the source assigns it, and it is always
domain-scoped.

#### 10 · `Canon` — Canonicality status
Source-backed values include:

`n/a` · `canonical` · `canonical-about-meaning` · `never-canon` · `not a Record` ·
`non-canonical manifestation`.

Two prohibitions:

- This field does **not** become a universal canonicality model. Canonicality is model-owned;
  this field records a per-artifact status, nothing more.
- It must never imply that Production, Visual or Issue records are automatically World Canon.
  Production is `never-canon`. Registry is `canonical-about-meaning` and never about the
  world. Issue is publication reality and never World Canon.

#### 11 · `CD` — Canonical-data flag
`yes` or `no`. Whether the artifact creates, carries or directly impacts canonical data.

`CD: yes` **does not grant authority and does not bypass a canonical gate.** An artifact
flagged `CD: yes` still may not produce canonical data before its model's own gate has passed,
and still writes only through the governed path. The flag marks the artifact for attention; it
licenses nothing.

#### 12 · `Ph/St` — Phase and stage
Written as `P<phase>/<stage>`, for example `P0/0a`, `P0/0b`, `P3/3b`, `P15/15a`.

- **Phase** identifies the Roadmap phase, `P0` through `P18`. No phase outside that range
  exists, and this field never invents one.
- **Stage** identifies the sub-position within the phase, lettered from `a`.

Stages are **roadmap-declared labels, not a dense sequence**. A phase may declare `7a` and `7c`
with no `7b`; that is the source's structure and is preserved as written rather than
renumbered. An author does not invent a stage letter that the Roadmap has not declared.

#### 13 · `Req` — Requirement ID
The Roadmap requirement identifier: `BR-01`, `BR-02`, `BR-98`, and so on.

**Preserve the exact source ID.** Never paraphrase, renumber, or normalize it.

The requirement register that defines each ID's full text is **not currently available**
(Revolving Resolution Note, GAP-C, NON-BLOCKING — UNVERIFIED). Therefore: **do not invent
requirement text**, and do not claim an artifact has been verified against a requirement
definition that has not been read. An artifact is verified against its `BP` and `RMS`
citations and its own `Val` and `Done`; its `Req` citation is carried forward unverified and
labelled as such.

#### 14 · `BP` — Blueprint citation
The precise Blueprint section reference the Roadmap assigns to the artifact, for example `§7`,
`§26.8`, `§13.7b`. `n/a` where the artifact has no Blueprint dependency.

**Do not invent a citation.** If the assigned section does not support the artifact, that is a
finding to report, not a citation to substitute.

#### 15 · `RMS` — Record Model System citation
The precise RMS section reference where one applies, for example `§2`, `§4`, `§10.3`. `n/a`
where the artifact has no RMS dependency — which is normal for foundation and environment
artifacts.

#### 16 · `H` — Hard dependency
The referenced artifact **must exist and resolve** before this artifact can be authored or
finalized. A hard dependency is a blocker.

Written as artifact IDs: `H: 001` · `H: 069,398` · `H: 001–029`. `—` where none is declared.

**Do not silently promote a soft dependency to hard.** Promotion changes the build order and
lengthens the critical path; it is a source-level change, not an authoring choice.

#### 17 · `S` — Soft dependency
Relevant or supporting context that is **not** declared a blocker. The artifact can be
authored without it, and is better for having it.

**Do not treat a soft dependency as a hard blocker** unless the source explicitly says so. A
soft dependency that is being waited on is a misread entry.

#### 18 · `LS` — Lockstep membership
Which declared lockstep system the artifact belongs to. `—` where none.

The lockstep systems are exactly these eight:

| ID | Lockstep | Shape |
|---|---|---|
| **LS-1** | Kind ↔ KIND-DEFINITION | ATOMIC-PAIR |
| **LS-2** | Field ↔ FIELD-DEFINITION | ATOMIC-PAIR |
| **LS-3** | Relationship ↔ RELATIONSHIP-TYPE-DEFINITION | ATOMIC-PAIR |
| **LS-4** | Constraint ↔ Validation-Rule ↔ Validator | ATOMIC-TRIPLE |
| **LS-5** | WSV ↔ WSVR ↔ Simulation-Model-Definition | ATOMIC-TRIPLE |
| **LS-6** | Capability ↔ Capability-Definition ↔ Implementation | ATOMIC-TRIPLE |
| **LS-7** | Coworker Role ↔ Role Boundary Definition | ATOMIC-PAIR |
| **LS-8** | Degraded Mode ↔ Mode Behaviour Contract | ATOMIC-PAIR |

> **Dependency and lockstep are different questions.**
>
> ```
> Dependency   A must exist before B can consume it.        (ordering)
> Lockstep     A and B must be authored and land together.  (simultaneity)
> ```
>
> A lockstep partner is not a predecessor. Landing one half of an ATOMIC-PAIR is a defect even
> when nothing is blocked by it.

**Do not create new lockstep groups.** Membership comes from the Roadmap's actual declaration
on the entry, not from an author's judgement that two artifacts look related. The following
were considered and **rejected as manufactured**: spec↔test, model↔example, schema↔fixture.

#### 19 · `G` — Gate
A named conformance or authorization barrier. `—` where none.

Declared gates:

| Gate | Licenses |
|---|---|
| `exit-P0` … `exit-P17` | the next phase |
| `G-REG` | Registry definitions may be consumed |
| `G-CANON-W` | World canon only |
| `G-CANON-E` | Epistemic canon only |
| `G-CANON-P` | Production State only, never world truth |
| `G-CANON-V` | Visual specifications and assets |
| `G-CANON-I` | Publication artifacts, never canon |
| `G-STATIC` | the authored set is statically complete and internally consistent |
| `G-RUNTIME` | the implemented system behaved as required |

There are **six canonical gates, not one**. A model may not write canon before its own
semantics exist and validate.

Some entries use `G` to record the artifact's *relationship* to a gate rather than a gate it
waits on — `enforces all canonical gates`, `defines G-CANON-W/E/P/R/V/I`, `gates every phase
exit`. That usage is source-declared and preserved; it is read as a statement about the
artifact's role in gating, not as a blocker on the artifact itself.

> **A dependency is not a gate.**
>
> ```
> Dependency   what must exist
> Gate         what must be passed before this may legally proceed
> ```
>
> A satisfied dependency does not open a gate, and an open gate does not supply a dependency.

**Do not invent gates.**

#### 20 · `→` — Unlocks
What this artifact enables once complete. Uses the exact Roadmap relationship, and may name:

| Form | Example |
|---|---|
| a single artifact | `→ 003` |
| an artifact range | `→ 002–030` |
| several artifacts | `→ 405,406` |
| a phase | `→ P8` |
| everything | `→ all` |

`→ all` is used only where the Roadmap declares it — a hinge artifact every later entry
depends on.

#### 21 · `Val` — Validation condition
**How completion is checked.** Must be concrete and checkable by inspection, a command, or a
deterministic test.

Good — from the manifest itself:

```
Val: tree matches PART I; every dir has a purpose file
Val: exactly 108 entries, each mapped
Val: direct write to canon/** denied
Val: R → instance rejected
```

Not acceptable: *looks correct* · *is complete* · *reads well* · *seems consistent*. A `Val`
that cannot fail is not a validation condition.

#### 22 · `Done` — Exit state
**What passing completion looks like** — the observable end state.

> ```
> Val    how completion is checked      (the procedure)
> Done   what completion looks like     (the state)
> ```
>
> Both are always present. `Val: deny proven by negative test` pairs with `Done: green`;
> `Val: tree matches PART I` pairs with `Done: tree complete`. Neither substitutes for the
> other.

#### 23 · `Why` — Rationale
A short architectural reason the artifact exists. One or two lines.

It records *why*, not *what* — Blueprint P-6, *preserve intentions, not just decisions*. It
does not duplicate the specification, and it is not a summary of the artifact's contents.

#### 24 · `Risk` — Risk classification
Source-backed values: `low` · `medium` · `high` · `CRITICAL` · `HINGE` · `CRITICAL HINGE`.
`—` where none is declared.

`HINGE` marks an artifact with very high fan-out, where an error propagates to everything
downstream. A few manifest entries carry a short risk *statement* in place of a classification
where the source wrote one; that is preserved as written.

**No numerical scoring.** Risk is a classification, never a computed score.

#### 25 · `∥` — Parallelizable
`yes` or `no`. Whether the artifact can be authored in parallel with its neighbours without
violating hard dependencies, lockstep, gates, or source-order rules.

> **No declared hard dependency does not automatically mean `∥: yes`.** An artifact can be
> unblocked and still serial — because it sits on the critical path, because it is a hinge
> every neighbour will need settled first, or because its stage is ordered. Artifact 001 has
> `H: —` and `∥: no`.

---

## Phase / Stage Conventions

| Phase | Purpose | Range |
|---|---|---|
| **P0** | Foundation | 001–030 |
| **P1** | Bootstrap | 031–038 |
| **P2** | Record System Kernel | 039–059 |
| **P3** | Registry Kernel | 060–124 |
| **P4** | Universal Validation | 125–144 |
| **P5** | Mutation / Write Boundary | 145–166 |
| **P6** | Derived-Layer Contract | 167–174 |
| **P7** | World | 175–218 |
| **P8** | Derived Layer | 219–230 |
| **P9** | World State + Simulation | 231–252 |
| **P10** | Epistemic | 253–295 |
| **P11** | Production | 296–342 |
| **P12** | Visual | 343–360 |
| **P13** | Issue | 361–380 |
| **P14** | Emergence | 381–396 |
| **P15** | Creative Governance | 397–413 |
| **P16** | Reader / Coworkers / Capabilities | 414–439 |
| **P17** | Surfaces / Orchestration / Dormancy / Extensibility | 440–462 |
| **P18** | Integration / Drills / Benchmarks / Freeze | 463–490 |

**Phase membership describes architectural build stage.** A phase boundary is the point at
which *what is legal to build* changes — which is why the phases are not merged.

**Phase membership does not imply serial authoring.** Most phases carry heavy internal
parallelism, and several phases run in parallel with each other. Whether a particular artifact
is serial is stated by its own `∥`, `H`, `LS` and `G` fields — never inferred from its phase.

An artifact's numerical position likewise implies nothing. **A later ID is not a licence to
build early**, and an earlier ID is not permission to skip a gate.

---

## Dependency Conventions

Four distinct concepts. Conflating any two of them is the most common authoring error, so each
answers a different question:

```
Dependency   "What must exist?"
Lockstep     "What must land together?"
Gate         "What must be passed before this can legally proceed?"
Unlocks      "What does finishing this enable?"
```

### Hard Dependencies — `H`
The source artifact must exist and resolve before this one can be authored or finalized. A
hard dependency blocks. It is validated by the reference resolving.

### Soft Dependencies — `S`
Supporting context that improves the artifact without blocking it. A soft dependency never
becomes a blocker by an author's judgement; promotion is a source-level change.

### Lockstep Dependencies — `LS`
Membership in one of LS-1 … LS-8. Lockstep partners land in **one authoring cycle**. An
ATOMIC-PAIR with one half landed is incomplete regardless of whether anything is blocked; an
ATOMIC-TRIPLE with two thirds landed is likewise incomplete.

The reason locksteps exist is custody: a Kind and its KIND-DEFINITION have different owners,
and shipping one without the other leaves a semantic without its definition or a definition
without its semantic.

### Gate Dependencies — `G`
A named barrier that must be passed before the artifact may legally proceed. Gates are not
dependencies and are not satisfied by them. A gate is passed by its own conformance
evidence — a phase conformance suite for `exit-Pn`, the declared criteria for `G-REG`,
`G-CANON-*`, `G-STATIC` and `G-RUNTIME`.

### Unlocks — `→`
What the completed artifact enables. Stated using the exact Roadmap relationship. Unlocks is
the inverse view of other artifacts' `H`, and the two must agree: if `002` declares `H: 001`,
then `001` declares `002` among its unlocks.

---

## Validation and Done Conventions

Every artifact states both, and they are different:

| | Question | Character |
|---|---|---|
| `Val` | How is completion checked? | a procedure — inspection, command, or test |
| `Done` | What does completion look like? | a state — observable, and either true or false |

Rules:

1. `Val` must be **concrete and checkable**. If no one could run it and get an answer, rewrite
   it.
2. `Val` must be **able to fail**. A condition nothing could violate validates nothing.
3. `Done` must be **observable**. "Complete" is not an exit state; "green", "tree complete",
   "108 placeholders, none orphaned" are.
4. Neither substitutes for the other, and neither is omitted.
5. Generating a test is not running it; generating a drill is not executing it; generating a
   benchmark is not measuring it. A `Val` that requires execution is discharged at the runtime
   boundary, not at authoring.

---

## RULE G — Specification / Schema Granularity

> **A specification and a schema are always separate artifacts.**

| | Specification | Schema |
|---|---|---|
| What it is | model-owned architecture | Registry-governed structural contract |
| Who owns it | the Record Model | Registry |
| When it changes | at Kind-admission ceremony | at field-definition revision |
| How it validates | against model semantics | against the definition it conforms to |

Four things differ — ownership, lifecycle, validation, change process — so they are two
artifacts, always. **Do not merge them.**

Applied without exception across all 49 Kinds: **98 Kind artifacts**, one specification and one
schema apiece.

---

## RULE G2 — Examples / Tests Separation

> **A model's worked examples and its tests are always separate artifacts.**

| | Example | Test |
|---|---|---|
| What it shows | the architecture being *used correctly* | the architecture being *enforced* |
| What it proves | that the architecture is usable | that the architecture cannot be violated |
| What its failure means | the architecture is awkward | the architecture is unprotected |

They concern the same concept and answer different questions. **Do not merge an example and a
test merely because they share a subject.**

---

## RULE G3 — Responsibility / Lifecycle / Ownership / Validation

> **Multiple files may be one artifact when they share all four of: one responsibility, one
> lifecycle, one owner, one validation.**

```
many files  →  one artifact        legal when all four conditions hold
```

The merge is **declared explicitly at the entry**, never left implicit. Source-backed
examples:

- **Artifact 028** — the four refusing commands `gate`, `simulate`, `render`, `brief`. One
  responsibility: *refuse until licensed*. Four files, one artifact.
- **Artifact 029** — the eleven adapter boundary shells. One responsibility: *the boundary
  exists and is empty*. Eleven files, one artifact — and it **splits at P17** (444–447) when
  the adapters gain implementations, because the responsibility changes.

**The converse binds equally.** If responsibility, lifecycle, ownership or validation
diverges, the work is separate artifacts — which is exactly why artifact 029 splits later.

**Do not merge artifacts to reduce the artifact count.** Granularity follows the four
conditions, never the total.

---

## Artifact Authoring Rules

A practical checklist. Work down it while authoring the entry.

1. Assign exactly one `ID`.
2. State all **25** metadata fields.
3. Never leave a metadata field blank.
4. Use `n/a` where genuinely not applicable, `—` where nothing is declared in a relational
   field.
5. Use only legal Types.
6. Use only legal Roles.
7. Use only legal SoT classes.
8. State `H`, `S`, `LS` and `G` explicitly — including when each is `—`.
9. State unlocks explicitly.
10. Provide a concrete, failable `Val`.
11. Provide an observable `Done`.
12. Apply RULE G, G2 and G3 **before** deciding artifact boundaries, not after.
13. Do not invent Record Models. There are six.
14. Do not invent gates.
15. Do not invent dependency classes.
16. Do not invent requirement meanings.
17. Do not silently change Blueprint or RMS architecture.
18. Do not use retired Canon Object Model terminology as current architecture.
19. Do not create a universal lifecycle, universal canonicality, or universal relationship
    model. These are model-owned.
20. Keep each artifact within its declared responsibility. Material belonging to a later
    artifact stays there, even when it is available now.

### Purpose-file convention

Every repository directory carries a purpose file named **`PURPOSE.md`**, stating the
directory's responsibility, its architectural role, what belongs in it, and what does not. It
is structural documentation: not canonical data, not a Record, not an authority source, not
world truth, and not a semantic definition. Coverage is complete at the time of writing —
68 of 68 directories.

This formalizes the convention Artifact 001 established and the Revolving Resolution Note
recorded at GAP-D and GAP-D.1.

---

## Worked Metadata Example

This document, stated under its own contract — the first real consumer of the conventions it
defines:

```
ID:     003
Name:   artifact + phase conventions
path:   docs/conventions/artifact_conventions.md
Own:    CONST
RM:     n/a
T:      doc
R:      CONTRACT
SoT:    AUTHORITATIVE
Auth:   governing
Canon:  n/a
CD:     no
Ph/St:  P0/0a
Req:    BR-01
BP:     §7
RMS:    n/a
H:      001
S:      002
LS:     —
G:      —
→:      all
Val:    every later artifact cites it; the 25-field metadata contract, legal vocabularies,
        dependency conventions, phase conventions, and RULE G/G2/G3 are explicit
Done:   all artifact + phase conventions are declared and internally consistent
Why:    the artifact authoring contract must exist before the remainder of the manifest is
        built
Risk:   HINGE
∥:      no
```

Read as prose: a constitutional-layer document carrying no Record Model semantics, which fixes
a contract rather than describing architecture, is authoritative about that contract, governs
authoring practice, is not canon and touches no canonical data, sits in the first stage of the
foundation phase, depends hard on the repository tree and softly on the README, belongs to no
lockstep and waits on no gate, unlocks everything, and is serial because everything downstream
needs it settled.

---

## Conformance Requirements

An artifact conforms to this contract when all of the following hold:

| # | Requirement |
|---|---|
| C-1 | All 25 fields are stated explicitly. None is inherited from a header or a neighbour. |
| C-2 | No field is blank. `n/a` and `—` are used per the null rule. |
| C-3 | `T`, `R` and `SoT` draw only on the legal vocabularies. |
| C-4 | `Own` draws only on established ownership vocabulary; `RM` names one of the six models, `all`, or `n/a`. |
| C-5 | `Ph/St` names a phase in P0–P18 and a Roadmap-declared stage. |
| C-6 | `Req` preserves the exact source ID; no requirement text is invented. |
| C-7 | `BP` and `RMS` cite real sections, or `n/a`. No invented citation. |
| C-8 | `H`, `S`, `LS`, `G` are each stated, and each resolves to a real artifact, lockstep, or gate. |
| C-9 | `→` agrees with the `H` declarations of the artifacts it names. |
| C-10 | `Val` is concrete and failable; `Done` is observable; both are present. |
| C-11 | Artifact boundaries were decided by RULE G, G2 and G3, and any RULE G3 merge is declared at the entry. |
| C-12 | No new Record Model, gate, dependency class, lockstep system, phase, or metadata field is introduced. |

Conformance is checked per artifact at authoring, per phase at the phase conformance suite,
and across the whole authored set at `G-STATIC`.

---

## Non-Authority Boundary

This document is a **contract on authoring practice**. It:

- **governs** how every later artifact states its metadata, declares its dependencies, and
  decides its boundaries;
- **does not amend** the Blueprint;
- **does not amend** the Record Model System;
- **does not amend** the Roadmap;
- **does not define** World Truth, own a Record Model, or hold canonical data;
- **may be superseded** by a formal authoritative amendment — most immediately, an amendment
  that settles the 25-versus-27 field count at source.

Where this document and the Blueprint or RMS differ, **they govern and this document is
wrong**. Where this document and the Roadmap differ on notation, this document governs the
notation and the Roadmap governs the decomposition. Nothing here makes an architectural
statement true.
