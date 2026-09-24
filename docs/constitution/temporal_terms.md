# COOLBOY12 — Temporal Term Separation

**Artifact 049** · provenance/audit/history/revision/version/lineage separation ·
`docs/constitution/temporal_terms.md` · Own: CONST · RM: all · T: doc · R: CONTRACT ·
SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2b · Req: BR-21 ·
BP: §13.7b · RMS: §18 · H: 048 · S: — · LS: — · G: — · → P7,P10–P13 ·
Val: six terms separated; unqualified *lineage* retired · Done: vocabulary fixed ·
Why: one word for three senses caused prior defects · Risk: high · ∥: no

> **On the title.** The Roadmap names this artifact with the six terms as Blueprint §13.7b
> lists them, the retired word among them. That name is preserved exactly, as a proper name.
> The document's own heading does not substitute any single current term for the retired word,
> because the word has three replacements, not one (§7.3).

## 1. Purpose

Blueprint §13.7b states the defect in one sentence: *"These six were used interchangeably in
v0.6.3 and are not interchangeable."* Roadmap row 049 names the sharpest instance of it: **one
word for three senses caused prior defects.**

```
one word
   ↓
several meanings
   ↓
each reader assumes a different one
   ↓
architecture built on the wrong one
```

This artifact fixes the vocabulary so that the chain cannot start. For each of the six terms it
records the one question the term answers, what the term is not, and where the answer's
packaging belongs. For the retired word, it records the three current terms that replace it.

Blueprint §13.7b also states why the separation matters beyond vocabulary: *"Separating them is
a precondition for letting each model own its temporal architecture without importing World's."*
A shared vocabulary is what lets six Record Models talk about the same questions **without**
sharing an answer.

This document adds no architecture. Every rule below is a contractual formulation of what
Blueprint §13.7b, §13.1, §13.6a, §13.6d and §13.8, RMS §4, §18 and §19, and the invariants cited
already establish.

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the separation of these six terms**, and about nothing else.
It **derives** that separation from the Master Blueprint and the Record Model System; it does not
amend, supersede, or outrank either.

Where this document differs from the Master Blueprint, the Record Model System, or the OS File
Build Roadmap, **those governing sources are correct and this document is wrong.**

It is not a Record, holds no canonical data, and is `Canon: n/a`. `SoT: AUTHORITATIVE` here means
authoritative **about architecture**, never World Canon (Blueprint §13.0, I-104).

## 3. Scope

**In scope.** The six terms; the one question each answers; which terms are not interchangeable
and why; the retirement of the unqualified word and its three replacements; the boundary between
a shared vocabulary and model-owned packaging; illustrations of the difference; prohibitions
against using one term for another.

**Out of scope.** The temporal architecture of any Record Model; the History Record as anything
but World's mechanism; any audit, revision, version or derivation mechanism; visual asset
relationships; any graph of descent; schemas, code, storage, serialization, runtime and tests.
This contract says **which word names which question**. It does not answer any of the questions
for any model.

**Position.**

```
047  captures who / when / why                    — the provenance capture mechanism
  ↓
048  provenance meaning is model-owned            — the provenance boundary
  ↓
049  the six terms are separated                  — this contract
  ↓
     each Record Model's own temporal architecture   (Roadmap → P7, P10–P13)
```

This contract takes provenance from 047 and 048 as they stand. It does not re-specify provenance
capture or provenance meaning; §5.1 places provenance among the six terms and nothing more.

## 4. The Governing Vocabulary Rule

> **Provenance, audit, history, revision and version, and the three senses of the retired word,
> are distinct terms. They are not interchangeable. Their questions are fixed by Blueprint §13.7b. Their packaging
> and mechanisms are not fixed by this vocabulary: they remain governed by each Record Model's
> own architecture. The unqualified word *lineage* is retired, and must not be used for any of
> the three senses it once carried.**

Two readings are ruled out by that rule, one on each side.

**A shared vocabulary is not a shared mechanism.** The six terms are system-wide so that every
model can ask the same six questions. Nothing about a question being shared makes its answer
shared. I-103: *"Shared infrastructure never confers shared meaning"* — and a shared word is
weaker than shared infrastructure.

```
six terms are shared
        ↓   ✗  does not follow
six mechanisms are shared
        ↓   ✗  does not follow
all six models use the same temporal package
```

**Six terms are not six structures.** No model is required to hold six things because six words
exist. A model may answer several of these questions with one mechanism, answer one with none
that the others would recognize, or conclude that a question applies to it differently. Blueprint
§13.6d states this about packaging directly: *"a model may conclude that it needs no History
Record at all"*, or a different mechanism in its place.

## 5. The Six Terms

Each term is given as: the question it answers, where the sources place it, what it is not, and
where its packaging belongs. The question column is Blueprint §13.7b's, verbatim.

| Term | The question it answers | Where the sources place it |
|---|---|---|
| **Provenance** | Who made this, when, and **why** | An envelope property on the Record |
| **Audit** | Under what approval mode, in which session, by whose act | Recorded within each temporal entry |
| **History** | How this Record's state came to be what it is | Model-owned packaging; World uses the History Record |
| **Revision** | This Record changed, and here is the change | Model-owned |
| **Version** | This is a distinct issued state of the same thing | Model-owned; Issue versions by supersession, never by edit |
| *(retired word)* | This came *from* that | Three senses — see §5.6 and §7 |

**Only provenance is an envelope field.** RMS §4's universal envelope is `partition` · `kind` ·
`object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` — seven fields, `FROZEN`.
Provenance is the only one of the six terms among them. No audit, history, revision, version or
derivation field is universal.

### 5.1 Provenance

**Question.** *Who made this, when, and why.*

**Where it sits.** An envelope property on the Record (Blueprint §13.7b; RMS §4). Capture is
shared infrastructure, provided by Artifact 047; what provenance *means* in a model is owned by
that model, and Artifact 048 holds that boundary. `when` names Real-World Time, which Blueprint
§12.16 makes authoritative in provenance.

**What it is not.** Not audit — the approval mode and session under which an act was approved are
a different question (§5.2). Not history, not revision, not version. Not the retired word in any
of its senses.

**Packaging boundary.** Set by 047 and 048. This contract adds nothing to it.

> *Illustrative and non-normative.* A Record carries captured provenance stating who made or
> changed it, the relevant Real-World Time, and the recorded reason. That alone says nothing about
> how the Record's history, audit, revisions or versions are packaged, or whether its model has
> separate packaging for them at all.

### 5.2 Audit

**Question.** *Under what approval mode, in which session, by whose act.*

**Where it sits.** Blueprint §13.7b places it *"within each temporal entry"*, citing I-14 —
*"Approval mode is recorded, not merely the fact of approval"* — and §12.16. What constitutes a
temporal entry in a given model is that model's temporal architecture (RMS §6, I-90); this
contract does not define one.

**What it is not.** Not provenance. **Approval mode belongs to audit, not provenance. Session
belongs to audit, not provenance.** Both questions contain a *who*, and they are different
people-questions: provenance asks who **made** this; audit asks by whose **act** it was
approved. P-18 lists them separately for the same reason — *"what changed, when, why, who approved
it"*. Blueprint §12.16 corroborates the placement from the temporal side: Real-World Time is
authoritative in provenance, while Session Number is not listed as authoritative there.

Audit does not become provenance because the two are recorded at the same moment, about the same
change, or in the same place.

**Packaging boundary.** Model-owned wherever temporal packaging is model-owned (§13.6d, I-90).

> *Illustrative and non-normative.* A temporal entry records the approval mode and the session
> under which a change was approved. That answers the audit question. It does not answer, and does
> not replace, the provenance question of who made the change, when, and why.

### 5.3 History

**Question.** *How this Record's state came to be what it is.*

**Where it sits.** Model-owned packaging; **the World Record Model uses the History Record**
(Blueprint §13.7b). The History Record is World's mechanism. It is not a Record System primitive
and may not be required of another Record Model (I-102).

**What it is not.** Not revision — a revision is one change; history is the account of how the
state came to be, of which revisions may be part. Not version. Not provenance.

**Packaging boundary.** Model-owned. I-90: *"Traceable evolution (P-17, P-18) is required of
every Record Model; the mechanism is model-owned. The History Record is the World Record Model's
mechanism and is not required of any other model."* The **obligation** is universal; the
**mechanism** is not. Every Record Model must be able to account for how its Records came to be as
they are; no model must do it the way World does.

> *Illustrative and non-normative.* A World Record's History Record can explain how that Record's
> state changed over time. That establishes nothing about whether an Epistemic, Production,
> Registry, Visual or Issue Record uses a History Record, uses something else, or packages its
> account of evolution in any particular form.

### 5.4 Revision

**Question.** *This Record changed, and here is the change.*

**Where it sits.** Model-owned (Blueprint §13.7b).

**What it is not.** Not history — a revision records a change; history accounts for how the
state came to be. Not version — **a revision does not by itself constitute a new version.** Not
provenance; a revision may carry provenance, and is still a different question from it.

**Packaging boundary.** Model-owned. No universal revision numbering, revision sequence or
revision structure is established by the word.

> *Illustrative and non-normative.* A Record is modified from one state to another, and the change
> itself is recorded. That is a revision. Whether the changed state is a distinct issued state of
> the same thing is a separate question — the version question — and its answer is the owning
> model's.

### 5.5 Version

**Question.** *This is a distinct issued state of the same thing.*

**Where it sits.** Model-owned; **Issue versions by supersession, never by edit** (Blueprint
§13.7b, §13.6a). Blueprint §13.6a: *"A published artifact is immutable (Section 18.7).
Correction is a new publication with a `supersedes` relationship, never an edit."*

**What it is not.** Not revision. **Not every revision is a version**, and a model is not required
to issue distinct states at all. Not an identity operation: Blueprint §13.8 states that Issue's
supersession rule *"is a publication rule, not one of these four"* identity operations — the
same word, *supersede*, names a version rule in Issue and a derivation operation in World (§7.3).

**Packaging boundary.** Model-owned. **Issue's rule is Issue's.** Versioning by supersession is
the Issue Record Model's rule and is not the rule for any other model. No universal version
numbering or version stamp is established by the word; no version field is a universal envelope
field (RMS §4).

> *Illustrative and non-normative.* A published Issue is not edited into a different state; a
> correction is a new publication that supersedes it. That is the Issue model's version meaning.
> It is not a template for how any other model issues, or declines to issue, distinct states.

### 5.6 The retired word

**Question it carried.** *This came from that.*

**Status.** **Retired as an unqualified term** (Blueprint §13.7b; RMS §18). Blueprint §13.7b:
*"Three senses, one word."* Those three senses are not one question with three applications —
they belong to three different categories of thing, and each now has its own current term:

| Sense | What it is | Current term | Owner |
|---|---|---|---|
| Identity operations | an account of operations on Records' identities | `derivation` | World semantics; **OPEN** elsewhere (§13.8) |
| A World Kind | a structure in the fiction — *"this cross-generational hereditary or ancestral structure"* | `LINEAGE` | the World Record Model (§13.6) |
| Visual asset descent | one asset's descent from another | *visual derivation* | the Visual Record Model (RMS §19) |

§7 is the full rule.

## 6. Term Separation Rules

Only the distinctions that have caused, or would cause, real architectural confusion.

| | Not the same as | Why |
|---|---|---|
| **provenance** | **audit** | who *made* this ≠ by whose *act* it was *approved*; approval mode and session are audit (§13.7b, I-14) |
| **provenance** | **history** | who, when and why of this Record ≠ how its state came to be (§13.7b) |
| **history** | **revision** | the account of how the state came to be ≠ one change (§13.7b) |
| **revision** | **version** | a change ≠ a distinct issued state (§13.7b) |
| **History Record** | **history** | World's mechanism ≠ the universal obligation (I-90, I-102) |
| **Issue supersession** | **identity supersede** | a publication rule ≠ an identity operation (§13.8) |
| **`derivation`** | **`LINEAGE`** | derivation operations ≠ genealogy (§13.1) |
| **`LINEAGE`** | ***visual derivation*** | a World Kind ≠ Visual asset descent (§13.7b) |
| **`derivation`** | ***visual derivation*** | identity operations ≠ asset descent, and owned by different models (§13.7b, §13.8, RMS §19) |
| **unqualified *lineage*** | **any valid term** | retired (§13.7b, RMS §18) |

The following statements are **invalid** under this contract:

| Invalid | Why |
|---|---|
| "approval mode is provenance" | approval mode is audit — §5.2 |
| "session is provenance" | session is audit — §5.2 |
| "revision = version" | a revision does not by itself constitute a version — §5.4, §5.5 |
| "version = every edit" | Issue versions *never* by edit; no model is required to version at all — §5.5 |
| "the History Record is the universal temporal mechanism" | it is World's mechanism — §5.3, I-90, I-102 |
| "*lineage* = generic derivation graph" | the unqualified word is retired, and no such graph exists — §7 |
| "`LINEAGE` = visual asset derivation" | a World Kind, not a Visual relationship — §7.3 |

## 7. The Retired Word — Disambiguation

### 7.1 The historical problem

One word carried three senses. Blueprint §13.1 records the first collision and its cost:
*"v0.4 called the derivation field `lineage`, and v0.5 admits `LINEAGE` as a World kind. One word
could not carry both a hereditary structure in the fiction and the record of identity operations
on a schema, and the collision would have made every query, linter rule, and invariant statement
ambiguous."* Blueprint §13.7b records the third: *"the Visual Library separately uses
*derives-from* for asset descent. Three senses, one word."*

### 7.2 The current rule

**The unqualified word is retired.** Blueprint §13.7b: *"v0.7.0 forbids the unqualified use."*
RMS §18 carries the same rule. Current and future text that means one of the three senses uses
that sense's term. Text that uses the bare word means nothing in particular, which is the defect.

### 7.3 The replacement map

| Sense | Write | Do not write |
|---|---|---|
| Identity operations (§13.8) | **`derivation`** | the bare word; `LINEAGE`; *visual derivation* |
| The World Kind (§13.6) | **`LINEAGE`** | the bare word; `derivation` |
| Visual asset descent | ***visual derivation*** | the bare word; `LINEAGE`; unqualified `derivation` |

Three constraints keep the map from collapsing back into one word:

- **The three terms are not synonyms**, and no one of them is the general term for the others.
  Replacing every occurrence of the old word with `derivation` would reproduce the defect under a
  new spelling.
- **`derivation` is the identity-operation sense only.** Blueprint §13.1: *"`SUPERSEDES` and
  `MERGED_INTO` are derivation operations, not genealogy."* The four identity operations are World
  Record Model semantics; their meaning for the other five models is **OPEN** (§13.8). The term is
  fixed here; the operations are not universalized by it.
- **`LINEAGE` is a World Kind, not a temporal term.** It classifies a thing in the fiction —
  dynasty, clan, bloodline, with `HOUSE` as its subtype (§13.6). It says nothing about how any
  Record came to be, and it is not the name of any other model's relationship or history.

### 7.4 Enforcement principle

Any new architectural or documentary text that needs one of the three senses uses that sense's
current term. The bare word may appear only:

1. where the retirement itself is being stated or discussed, as here;
2. in a proper name the sources fix — the Roadmap's name for this artifact, and Spine law 9's
   title, *"Every Object Has Lineage"*;
3. in a verbatim quotation of a source.

It may not appear as a generic term for ancestry, descent, derivation or relationship.

### 7.5 Historical text is not rewritten

Retirement governs **current and future use**. It does not delete historical evidence and does not
authorize rewriting historical source text or earlier records to remove the word. A historical
document that uses the bare word is read in its own terms, as a record of the vocabulary it was
written in.

### 7.6 Spine law 9

Spine law 9 is **unchanged**: *"Every Object Has Lineage. Every Record traces to the decision that
created or last changed it."* Both passages that retire the word say so, and say why it is
safe — Blueprint §13.1: the law *"states a principle of traceability, and its text … reads
correctly without reference to any field name"*; Blueprint §13.7b: *"Spine law 9 is unchanged and
reads correctly without the word."*

So:

- the traceability obligation Spine law 9 states is untouched;
- the word in the law's title is a proper name, not a use of the retired term (§7.4);
- retiring the word retires an ambiguity, not an obligation;
- this contract does not amend, reinterpret or add to the Spine, and mints no replacement law.

## 8. Vocabulary Is Not Packaging

**This contract fixes vocabulary. It does not fix packaging.**

The six questions are shared by every model. The mechanisms that answer them are not:

| | Universal | Model-owned |
|---|---|---|
| The six questions and their terms | **yes** — this contract | — |
| The obligation of traceable evolution | **yes** — P-17, P-18, I-90 | — |
| Provenance capture | **yes** — Artifact 047 | — |
| How history, audit, revision and version are packaged | — | **yes** — §13.6d, I-90 |
| Whether a model has a History Record | — | **yes** — World does; no other model is required to (I-90, I-102) |
| What derivation means outside World | — | **OPEN** — §13.8 |

Blueprint §13.6d states the governing rule: *"each Record Model owns the packaging of its
Records."* Its packaging rows for E, P, R, V and I are *"MODEL-DESIGN INPUT (not a freeze)"*, and
I-107 makes the consequence binding: *"A package composition declared for a Record Model that has
not been independently designed is provisional and may not be implemented as a requirement."*
**This contract does not convert any of those rows into a requirement**, and proposes no temporal
package for any model.

### 8.1 The six models

The vocabulary applies identically across **W** World · **E** Epistemic · **P** Production ·
**R** Registry · **V** Visual · **I** Issue. How each model answers the six questions is that
model's responsibility, because:

- **I-101** — no Record Model is a specialization of another or the template for another;
- **I-103** — shared infrastructure never confers shared meaning;
- **I-90** — traceable evolution is required of every model, by a mechanism each model owns;
- **I-107** — a composition declared for an undesigned model is not a requirement.

**World is the only model whose temporal mechanism the sources describe in full. That is not a
reason to use it as the template for the other five**, and this contract does not.

## 9. Worked Examples

**Every example below is illustrative and non-normative.** It shows two terms applied to one
situation and gives two different answers. It defines no structure, field or mechanism.

### Example 1 — Provenance vs audit

A Record is changed and the change is approved.

- *Provenance* answers who made the change, when in Real-World Time, and why.
- *Audit* answers under which approval mode it was approved, in which session, by whose act.

One change, two questions. Neither answer can stand in for the other, and a model that records one
has not thereby recorded the other.

### Example 2 — History vs revision

A Record changes from one state to another.

- The *revision* is that change.
- The Record's *history* is the account of how its state came to be what it is — which may include
  that revision among much else.

Whether the owning model keeps the two together, apart, or in some other form is that model's
packaging.

### Example 3 — Revision vs version

A Record is revised. Nothing in that fact makes the new state a distinct issued state.

In Issue, a correction is not an edit at all: it is a new publication that supersedes the old
one — Issue's version rule. That rule is Issue's. It does not tell any other model that its
revisions are versions, or that they must be issued as new things.

### Example 4 — `LINEAGE`, the World Kind

The Blueprint's illustrative World identity `W-LI-001-DelPhonar` (§13.9a) names a `LINEAGE` — a
hereditary structure in the fiction. It is a World Record of a World Kind.

It is not a name for how any Record came to be, and it must not be called by the bare word when
what is meant is derivation or descent.

### Example 5 — Visual derivation

A visual asset descends from another asset.

That is *visual derivation*, and it is Visual's (RMS §19). It does not make either asset a
`LINEAGE`, and it is not an identity operation.

### Example 6 — `derivation`

In the World Record Model, two Records are merged by the identity operation *Merge* (§13.8).

The account of that operation is `derivation` — Blueprint §13.1 names `SUPERSEDES` and
`MERGED_INTO` as *"derivation operations, not genealogy."* It is not `LINEAGE`, it is not
*visual derivation*, and it is not written with the bare word. What an identity operation means in
the other five models is **OPEN** (§13.8); this example says nothing about them.

## 10. Non-Goals — What This Contract Does Not Define

This contract separates six terms. It defines **none** of the following, and no reader may cite
it as having done so:

1. a universal temporal schema or temporal object model
2. a universal History Record — the History Record is World's (I-90, I-102)
3. a universal audit record or audit schema
4. a universal revision schema, numbering or sequence
5. a universal version schema, numbering or stamp
6. any universal graph of descent, ancestry or derivation
7. the meaning of identity operations outside World — **OPEN**, §13.8
8. any model's temporal architecture or temporal package — model-owned, §13.6d, I-90
9. any conversion of a MODEL-DESIGN-INPUT packaging row into a requirement — I-107
10. provenance capture or provenance meaning — Artifacts 047 and 048
11. the temporal axes — Blueprint §12.16
12. storage, persistence, serialization or wire formats
13. runtime code, validators or tests
14. canonical data, or any Record
15. any Record Model, Kind or field
16. any constitutional invariant
17. any amendment to the Spine

## 11. Prohibited Architectural Moves

| | Move | Why prohibited |
|---|---|---|
| **A** | **Term collapse** — treating any two of the six terms as synonyms | Blueprint §13.7b |
| **B** | **History universalization** — using the World History Record as the universal temporal mechanism | I-90; I-102 |
| **C** | **Revision–version collapse** — treating every revision as a version | Blueprint §13.7b |
| **D** | **Provenance–audit collapse** — treating approval mode or session as provenance | Blueprint §13.7b; I-14 |
| **E** | **Resurrecting the retired word** — using it as a generic term for relationship, ancestry, descent or derivation | Blueprint §13.7b; RMS §18 |
| **F** | **World Kind leakage** — treating `LINEAGE` as a system-wide temporal concept | Blueprint §13.6, §13.7b |
| **G** | **Visual–World leakage** — treating *visual derivation* as `LINEAGE` | Blueprint §13.7b |
| **H** | **Derivation collapse** — treating identity-operation `derivation` and *visual derivation* as one mechanism | Blueprint §13.7b, §13.8; RMS §19 |
| **I** | **Universal temporal package** — one package, lifecycle or schema for all six models | Blueprint §13.6d; I-90; I-107 |
| **J** | **Vocabulary as schema** — citing this contract to justify fields, classes, tables, storage or wire formats | RMS §4; §8 |
| **K** | **Supersession collapse** — treating Issue's publication supersession as an identity operation, or either as a rule for other models | Blueprint §13.8, §13.6a |

## 12. Conformance Conditions

Stated so they are checkable. This document implements no test and is `T: doc`. No `049.x`
constitutional invariant is minted; the conditions are stated without one.

| ID | Condition | Basis |
|---|---|---|
| **C-01** | The six terms are named and held distinct. | Blueprint §13.7b; RMS §18 |
| **C-02** | Each term carries its source-defined question, verbatim. | Blueprint §13.7b |
| **C-03** | Approval mode and session are audit, not provenance. | Blueprint §13.7b; I-14 |
| **C-04** | History is not treated as revision or version. | Blueprint §13.7b |
| **C-05** | A revision is not by itself a version. | Blueprint §13.7b |
| **C-06** | The unqualified word is retired for current and future use. | Blueprint §13.7b; RMS §18 |
| **C-07** | `derivation`, `LINEAGE` and *visual derivation* are distinguished and are not synonyms. | Blueprint §13.1, §13.7b |
| **C-08** | No universal temporal package, lifecycle or schema is established. | Blueprint §13.6d; I-90 |
| **C-09** | The History Record is not made a universal primitive. | I-90; I-102 |
| **C-10** | Packaging stays model-owned, and no MODEL-DESIGN-INPUT row is made a requirement. | Blueprint §13.6d; I-107 |
| **C-11** | No model is the template for another's temporal architecture. | I-101 |
| **C-12** | Identity operations are not universalized beyond World. | Blueprint §13.8 |
| **C-13** | No schema, runtime, storage, Record, Kind, field or invariant is created. | RMS §4; Roadmap row 049 `T: doc` |
| **C-14** | Historical text is not rewritten; retirement governs current and future use. | Blueprint §13.7b |
| **C-15** | Spine law 9 is not amended or reinterpreted. | Blueprint §10, §13.1, §13.7b |

A construction satisfying all fifteen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 13. Source Traceability

| Rule | Source |
|---|---|
| The six terms are distinct and not interchangeable | Blueprint §13.7b; RMS §18 |
| The six questions, verbatim | Blueprint §13.7b |
| Separation lets each model own its temporal architecture without importing World's | Blueprint §13.7b |
| Provenance is an envelope property; capture shared, meaning model-owned | Blueprint §13.7b, §13.7a; RMS §4; Artifacts 047, 048 |
| Real-World Time is authoritative in provenance | Blueprint §12.16 |
| Only provenance, of the six, is a universal envelope field | RMS §4 |
| Audit = approval mode, session, by whose act; recorded within each temporal entry | Blueprint §13.7b; I-14 |
| "Who approved it" is a separate question from who, when and why | P-18; I-09 |
| History = how the Record's state came to be | Blueprint §13.7b |
| History packaging is model-owned; the History Record is World's | Blueprint §13.6d, §13.7b; I-90; I-102 |
| Traceable evolution is required of every model; the mechanism is model-owned | P-17; P-18; I-90 |
| Revision = this Record changed, and here is the change | Blueprint §13.7b |
| Version = a distinct issued state of the same thing | Blueprint §13.7b |
| Issue versions by supersession, never by edit | Blueprint §13.6a, §13.7b |
| Issue's supersession is a publication rule, not an identity operation | Blueprint §13.8 |
| The unqualified word is retired; three senses, three terms | Blueprint §13.7b; RMS §18 |
| `derivation` for identity operations; "derivation operations, not genealogy" | Blueprint §13.1, §13.7b, §13.8 |
| Identity operations are World semantics; OPEN elsewhere | Blueprint §13.8 |
| `LINEAGE` is a World Kind; `HOUSE` is its subtype | Blueprint §13.6, §13.7b |
| *Visual derivation* for asset descent; a Visual capability | Blueprint §13.7b; RMS §19 |
| Spine law 9 is unchanged and reads correctly without the word | Blueprint §10, §13.1, §13.7b |
| Packaging is model-owned; E/P/R/V/I rows are design input, not a freeze | Blueprint §13.6d |
| A composition for an undesigned model is not a requirement | I-107 |
| No Record Model is a template for another | I-101 |
| Shared infrastructure never confers shared meaning | I-103 |
| Record ≠ Canon; SoT class is not canonicality | Blueprint §13.0; I-104 |
| Hard dependency on 048; unlocks P7, P10–P13 | Roadmap row 049 |

`Req: BR-21` is preserved exactly as the Roadmap states it. The authoritative requirement register
is not present in this repository; the requirement text is therefore **not** reproduced here and
**MUST NOT** be inferred.

---

*Artifact 049 · P2/2b · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document is a vocabulary contract derived from Master Blueprint §13.7b and RMS §18, with the
model-ownership boundaries preserved from Blueprint §13.6d and I-90. It does not amend those
sources. It is not a Record, holds no canonical data, and defines no mechanism, package, schema or
invariant for any Record Model. Where it differs from the Master Blueprint, the Record Model
System, or the OS File Build Roadmap, those governing sources are correct and this document is
wrong.*
