# COOLBOY12 — The Architectural Categories

**Artifact 044** · seven architectural categories · `docs/constitution/categories.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P2/2b · Req: RR-07 · BP: §13 · RMS: §6.1 ·
H: 039 · S: — · LS: — · G: — · → 057, all Kind work ·
Val: Record/Kind/Field/State/Relationship/Definition/Projection/Primitive each with a test ·
Done: eight terms, eight tests · Why: stops every noun becoming a Kind · Risk: high · ∥: no

> **On the count.** RMS §6.1 is headed *"The Seven Architectural Categories"* and its `FROZEN`
> table defines **eight**: Record, Kind, Field, State, Relationship, Definition, Projection,
> Primitive. The Roadmap row for this artifact reproduces all eight in `Val` and states
> `Done: eight terms, eight tests`. This artifact implements the **frozen content**, which is
> eight. The discrepancy is in the two headings only; it is recorded here and **not silently
> corrected in either source**, because neither source is this artifact's to amend.

## 1. Purpose

The system needs a fixed way to say what category a named thing belongs to, so that **not every
noun becomes a Kind.**

A new noun appears — a name, a status, a timeline, a parser — and the cheapest move is to make
it a Kind. Taken often enough, that move produces an ontology nobody can hold in mind and a
taxonomy that no longer says anything. This document supplies the classification that stops it.

Promotion to Kind is **exceptional and separately governed**: this artifact says what a Kind
*is*; **Artifact 057** owns the admission test that decides whether a particular proposal
becomes one.

Scope, kept distinct from its dependency: **Artifact 039** states what the Record System *is*.
This artifact states **what kinds of architectural things can appear inside it.** It does not
restate the six-model architecture, the retirement of the Canon Object Model, or the sovereignty
boundaries; 039 governs all three and is not amended here.

## 2. Constitutional Rule

The Record System recognizes exactly these **eight architectural categories** (RMS §6.1,
`FROZEN`):

```
1. Record        5. Relationship
2. Kind          6. Definition
3. Field         7. Projection
4. State         8. Primitive
```

These are **architectural classifications, not a universal semantic schema.** Sharing a
category name across models says how a thing is classified. It says nothing about what that
thing means in any model, and confers no shared semantics of any sort (Artifact 043, I-103).

There is no ninth category. A thing that fits none of the eight is routed to architectural
review (§12), never accommodated by inventing one.

## 3. Category Table

The definitions and tests are RMS §6.1's, preserved exactly.

| Category | Definition | Test | COOLBOY12 example |
|---|---|---|---|
| **Record** | A persistent, identity-bearing unit owned by exactly one Record Model | Has independent identity, lifecycle, and authority | a particular World character, `W-CH-000001-…` |
| **Kind** | A class of Record within one model | Passes the Kind Admission Test (§13) | `CHARACTER` `CH`, a World Kind |
| **Field** | An attribute of a Record | Has no independent identity | a character's name |
| **State** | A value in a defined lifecycle | Enumerable; transitions are governed | a World field's mutation class: locked / world-state / derived |
| **Relationship** | A connection between Records | First-class only when no endpoint can own it | a World causal edge neither endpoint owns cleanly |
| **Definition** | A Registry Record specifying meaning | Governs; never instantiates | `KIND-DEFINITION`, `FIELD-DEFINITION` |
| **Projection** | Derived, rebuildable output | Never authoritative (§29.6a) | an index, a search projection, a materialised view |
| **Primitive** | A system capability | Operates on Records; is not one | identity parsing and resolution; structural validation |

## 4. Record

A **Record** is persistent, identity-bearing, and owned by **exactly one** Record Model. Its
test is threefold and conjunctive: independent **identity**, independent **lifecycle**,
independent **authority**. A thing that borrows any of the three from another object is not a
Record; it is an attribute, a state, or a connection of that object.

Example: a particular World character is a Record. It bears its own identity
(`W-CH-000001-…`), begins, changes and ends on its own lifecycle, and carries its own authority.

Three things a Record is **not**, and the vocabulary must be able to refuse all three
(Blueprint §13.0, I-104; Artifact 039 §7):

- **Record ≠ Canon.** `Record` is architectural; `Canon` is governance.
- **Record ≠ canonical.** Canonicality is a status property whose meaning each model defines,
  and which not every model has at all. Artifact 052 owns that framework; nothing of it is
  anticipated here.
- **Record ≠ a universal schema.** What fields a Record carries, and what they mean, is owned by
  the Record Model that owns the Record.

## 5. Kind

A **Kind** is a **class of Record within one model** — never an individual Record, and never a
class spanning models. Its test is: **passes the Kind Admission Test (§13).**

Example: `CHARACTER` `CH` is a World Kind. A particular character is a **Record instance** of
that Kind. The two are different categories and are never used interchangeably.

**The admission decision is not made here.** Blueprint §13.11 states the test and **Artifact
057** owns it as a binding artifact. This document establishes only the boundary the test
operates on: a proposal must first be a class of Records within one model to be a Kind
*candidate* at all. No alternative admission rule, and no additional admission question, is
created here.

Each model owns its own Kind roster. There is no universal Kind taxonomy (Artifact 043,
prohibition 6).

## 6. Field

A **Field** is an attribute of a Record. Its test is: **has no independent identity.**

Example: a character's `name` is a Field. It is meaningful, it is queried constantly, and it is
still a Field — because it has no identity of its own, no lifecycle of its own, and no authority
of its own.

**Importance is not identity.** That content matters, appears everywhere, or is central to how
people talk about the world is not evidence that it should be promoted. The test asks one
question, and mattering is not it.

## 7. State

A **State** is a value in a defined lifecycle. Its test is twofold: **enumerable**, and
**transitions are governed.** A value that can take any shape, or that changes without governed
transitions, is not a State.

Example, taken from the source and deliberately: World's field mutation classes —
**locked / world-state / derived** — are, in RMS §7's own words, *"a **World** classification,
not a universal state model."*

That example is chosen to make the boundary unmissable: **State is a category; the actual states
and their transitions are model-owned.** Naming State as a shared category creates no shared
status vocabulary, and no model's lifecycle is evidence about another's. Two models hold Records
that can never be canonical, so a status vocabulary admitting `CANON` everywhere would be false
(Artifact 043, prohibition 4).

## 8. Relationship

A **Relationship** is a connection between Records. Its test is restrictive by design:
**first-class only when no endpoint can own it.**

The default is that a connection is owned by one of its endpoints — as a field, or as a
reference held by the owning side. A Relationship becomes a first-class thing only when that
ownership cannot be assigned cleanly to either end.

Example: in World, a causal edge whose meaning belongs to neither participant alone is a
Relationship rather than a field on either participant.

> **Hard warning.** This category establishes **no universal Relationship Record.** Relationship
> packaging is model-owned (Blueprint §13.6d, §13.9). Relationship Record and History Record are
> **World** Record Model concepts: neither is a Record System primitive, and neither may be
> required of another Record Model (I-102; Artifact 043, prohibitions 2 and 3). World is where
> Relationship Records are explicitly realized; that fact is about World and is not exportable.

The relationship boundary itself is **Artifact 055**. Its contract is not designed here.

## 9. Definition

A **Definition** is a **Registry Record specifying meaning.** Its test is: **governs; never
instantiates.**

Examples, using the Registry's own frozen Kind names: `KIND-DEFINITION`, `FIELD-DEFINITION`,
`RELATIONSHIP-TYPE-DEFINITION`.

A Definition **is** a Record — it has identity, lifecycle, and authority — and its architectural
**role** is Definition. Those two facts sit together without tension, and neither cancels the
other. Having identity does **not** convert a Definition into an instance-bearing domain Record:
a `KIND-DEFINITION` governs what a Kind means; it never becomes an instance of that Kind.

The boundary that keeps this safe: **Registry governs definitions; each Record Model owns its
Records** (I-105). Registry holds semantic authority over definitions and never semantic
ownership of another model's Records. Naming Definition as a category does not make Registry a
super-model, and does not give Definition semantic authority anywhere outside Registry.

## 10. Projection

A **Projection** is derived, rebuildable output. Its test is absolute: **never authoritative**
(§29.6a).

Examples, from the Blueprint's own `DERIVED` class: an index, a search projection, a graph
projection, analytics, a materialised view.

A Projection is **never a substitute for its authoritative source.** It may be deleted and
rebuilt without loss; that is what makes it a Projection. The rule that gives the classification
its force, in the Blueprint's words: *"an external system must never be the only place where a
canonical semantic exists."* If deleting a thing would lose a meaning rather than a convenience,
it was never a Projection and is misfiled.

This category does not declare that every derived artifact is a Projection. Source-of-truth
classification (§29.6a) distinguishes `DERIVED` from `CACHED`, `TEMPORARY` and `EXTERNAL`, and
that classification is not restated or extended here.

## 11. Primitive

A **Primitive** is a system capability. Its test states both halves: **operates on Records; is
not one.**

Examples, restricted to facilities the sources establish as shared mechanisms: identity minting,
parsing and resolution; structural validation; serialization; storage and repository access.

This category exists because a capability may operate over Records across every model **without
becoming a Record, and without acquiring authority over what those Records mean.** A Primitive
that begins deciding meaning has stopped being a Primitive; Artifact 043 §8's facility-or-claim
test governs that moment. A Primitive never acquires a Record schema, universal or otherwise.

## 12. The Category Decision Test

When a new noun appears, classify before designing:

```
1. Persistent, identity-bearing unit, with its own identity,
   lifecycle and authority?                        → Record
2. A class of Records within one model?            → Kind candidate  (→ 057 decides)
3. Merely an attribute, with no identity?          → Field
4. An enumerable value in a governed lifecycle?    → State
5. A connection no endpoint can cleanly own?       → Relationship
6. A Registry Record that governs meaning?         → Definition
7. Derived, rebuildable, never authoritative?      → Projection
8. A capability operating on Records, not a Record? → Primitive

None fits  →  do NOT invent a ninth category.
              Route the case to architectural review.
```

**This procedure is a classification aid. It does not replace the Kind Admission Test.** Reaching
step 2 makes a proposal a Kind *candidate* and nothing more; Artifact 057 decides admission.

## 13. Anti-Noun-Proliferation Rule

**A noun appearing in the system does not deserve a Kind by appearing.** Before proposing one,
establish that the thing is not already a Field, a State, a Relationship, a Definition, a
Projection, or a Primitive. Only then does the Kind question arise, and it is then answered by
Artifact 057.

| Tempting Kind | Because | Correct category |
|---|---|---|
| `Name` | names are important | **Field** — no independent identity |
| `Status` | status is queried constantly | **State** — enumerable, governed transitions |
| `Timeline` | a timeline is visible and used | **Projection** — derived, rebuildable, never authoritative |
| `Parser` | parser behaviour is critical | **Primitive** — operates on Records, is not one |

The source's own worked case: **WSV is World state, not an eighth instance-bearing Kind.** It
carries identity and is durable, and it was still deliberately not made a Kind. That is the
discipline this section asks for, applied by the Blueprint to itself.

## 14. Boundary Rules

Non-equivalences, binding rather than stylistic:

```
Record                  ≠  Canon
Record                  ≠  canonicality
Kind                    ≠  an individual Record
Field                   ≠  Record
State                   ≠  a universal lifecycle
Relationship            ≠  a universal Relationship Record
Definition              ≠  an instantiated domain object
Projection              ≠  authority
Primitive               ≠  Record
architectural category  ≠  universal semantic schema
```

## 15. Sovereignty and the Anti-COM Boundary

The **category vocabulary is common architecture**. The **meaning** carried by Records remains
owned by the Record Model that owns them.

| Shared | Model-owned |
|---|---|
| That `Record` is a recognized architectural category | What qualifies as a concrete World Record, what its lifecycle means, what authority it carries |
| That `Kind` means a class of Records within one model | Which Kinds exist in a model, and what each means |
| That `State` is a category | The actual states, and the transitions between them |
| That `Relationship` is a category | Whether and how a model packages relationships |

Shared categories therefore authorize **none** of: a universal schema · a universal lifecycle ·
universal canonicality · universal relationships · a universal Kind taxonomy. Each is separately
prohibited by Artifact 043, whose nine prohibitions bind this document without being restated
here.

Classifying two things into the same category is an **architectural** statement. It is never
evidence that they mean the same thing, and never permission to universalize a model-owned
semantic (I-103).

## 16. Conformance

| # | Requirement |
|---|---|
| C-1 | Every later Kind proposal **MUST** first classify the proposed thing against these eight categories. |
| C-2 | A proposal that classifies as Field, State, Relationship, Definition, Projection or Primitive **MUST NOT** proceed as a Kind proposal. |
| C-3 | A proposal that classifies as a Kind candidate **MUST** then undergo the separate Kind Admission Test (Artifact 057). Classification here is not admission. |
| C-4 | A later artifact **MUST** be able to cite this document when explaining why something is a Kind rather than one of the other seven categories. |
| C-5 | No later artifact may introduce a ninth category, or use these categories to assert a universal schema, lifecycle, canonicality, relationship packaging, or Kind taxonomy. |

## 17. Non-Authority Boundary

This document is a **contract on architectural classification**. It:

- **governs** which architectural categories exist and how a named thing is classified;
- **does not** define any Record Model's Kinds, fields, states, or schemas;
- **does not** state or modify the Kind Admission Test (Artifact 057);
- **does not** define the relationship boundary (Artifact 055), authority (051), canonicality
  (052), provenance meaning (048), or any other artifact's contract;
- **does not** restate the Record System constitution (Artifact 039) or the mechanism/semantics
  boundary (Artifact 043), and contradicts neither;
- **does not** introduce implementation, schema, or code;
- **carries no canonical data** (`CD: no`) and writes nothing to `canon/**`.

`Req: RR-07` is preserved exactly as the Roadmap states it. The authoritative requirement
register is not present in this repository; the requirement text is therefore **not** reproduced
here and **MUST NOT** be inferred.

*This document derives its authority from Blueprint §13 and RMS §6.1, and amends neither. Where
it and the Master Blueprint, the Record Model System, or the OS File Build Roadmap differ, they
are right and this document is wrong.*
