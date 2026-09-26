# COOLBOY12 — Temporal Obligation Specification

**Artifact 054** · temporal obligation specification · `docs/constitution/temporal_obligation.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a ·
CD: no · Ph/St: P2/2d · Req: BR-15,RR-29 · BP: §12.9 · RMS: §16 · H: 049 · S: — · LS: — · G: — ·
→ P7,P10–P13 · Val: obligation universal, **mechanism model-owned**; no universal History Record ·
Done: split stated · Why: I-90 made buildable · Risk: CRITICAL · ∥: no

## 1. Purpose

This contract answers one question: **what temporal obligation binds all six Record Models, and
who owns the mechanism that satisfies it?**

The answer is Blueprint P-17's, in its own words:

> *"The obligation is universal; the mechanism is model-owned"*

Row 054's reason is *"I-90 made buildable"*. I-90 states the rule; this contract makes it
checkable — what every model's temporal account MUST be able to answer, what stays with each model,
and what is World's alone — without prescribing how any model builds its account.

**This contract adds no architecture.** Every rule below restates P-17, P-18, I-09, I-11, I-90,
I-101, I-102, I-103, I-107, Blueprint §12.9, §12.16, §13.6d, §13.7a and §13.7b, and RMS §16 and
AD-11.

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the temporal obligation contract and the boundary between
universal obligation and model-owned mechanism**. It is not World Canon, not a Record, not a
temporal database, not a schema, not a model implementation, and holds no authority over the
internal semantic design of any Record Model.

It derives the contract from the Master Blueprint and the Record Model System; it does not amend,
supersede, or outrank either, and it amends no Spine law and no invariant. Where this document
differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those
governing sources are correct and this document is wrong.**

`Req: BR-15,RR-29` is preserved exactly as the Roadmap states it. The authoritative requirement
register is not present in this repository; the requirement text is **not** reproduced and **MUST
NOT** be inferred.

**Source gap.** RMS §16 places the temporal matrix in *"Appendix D and Deliverable G"*; Appendix D
reads only *"Temporal Matrix → Deliverable G"*, and Deliverable G is not in this repository. This
contract does not reconstruct it and MUST NOT be read as a substitute for it.

## 3. Scope

**In scope.** That the P-17/P-18 obligation binds W, E, P, R, V and I; the five P-18 questions as
the checkable content of that obligation; that the mechanism satisfying it is model-owned; that
the History Record is World's; the axis, causality and approval boundaries the obligation carries.

**Model-owned, not here.** Every Record Model's temporal package, entries, structures, lifecycle,
ceremony and storage — whether it has anything shaped like a History Record, and where each of the
five answers lives.

**Out of scope.** Temporal vocabulary (Artifact 049); provenance capture and meaning (Artifacts
047, 048); source-of-truth class (050); authority (051); canonicality (052); temporal-axis
semantics (Blueprint §12.16); enforcement (Artifact 133); schemas, fields, code and tests.

```
P-17 · P-18 · I-09             the obligation                    — Blueprint
049  temporal vocabulary        what the terms mean               — frozen
054  temporal obligation        ← this contract: who must answer what; who owns how
  ↓
     each model's temporal architecture                           — the mechanism
133  temporal validator         — Val: "each model's obligation satisfied by its own mechanism"
```

## 4. Governing Temporal Obligation

> **The universal temporal requirement is not a universal temporal mechanism. Every Record Model
> MUST satisfy P-18 in full. Each Record Model owns the mechanism by which it does so. The
> obligation is universal. The mechanism is model-owned.**

| | |
|---|---|
| Universal obligation | ≠ universal package |
| Universal obligation | ≠ universal History Record |
| Universal obligation | ≠ universal schema |
| Universal obligation | ≠ universal lifecycle |
| Universal obligation | ≠ universal temporal object |

The sources state the rule four times, from four directions:

- **P-17**: *"Every Record is covered by a complete, traceable account of its authoritative
  evolution, by the mechanism its Record Model defines — the World Record Model uses the History
  Record; no other model is required to."*
- **Blueprint §13.6d**: *"Every partition must be able to answer the P-18 questions"* — *"That
  obligation is constitutional (Spine law 9, I-09) and is not negotiable for any model."* And:
  *"The obligation is shared. The mechanism is model-owned."*
- **I-90**: *"Traceable evolution (P-17, P-18) is required of every Record Model; the mechanism is
  model-owned. The History Record is the World Record Model's mechanism and is not required of any
  other model."*
- **RMS §16**: *"Universal obligation (P-17/P-18, I-09); model-owned mechanism (I-90)."*

Spine law 9 is unchanged. Its v0.3.1 reading is the reach this obligation serves: *"the guarantee
that an object's entire evolutionary path remains recoverable and explainable for the life of the
universe"* (Blueprint §10).

## 5. The P-17 / P-18 Obligation

P-18: *"No canonical state may exist that cannot be explained by its evolution. For any canonical
state the system must always be able to answer: what changed, when, why, who approved it, and what
caused it. A state that cannot answer these is an audit finding, not an acceptable state."* I-09
restates it: *"Every canonical state answers: what changed, when, why, who approved it, what caused
it."*

The five questions are the content of the obligation. They are kept as five, in P-18's words, and
are **not** remapped onto Artifact 049's six terms: provenance, audit, history, revision and
version are vocabulary for concepts a mechanism may use to answer them, not a replacement for them.

| P-18 question | Universal? | What the obligation requires | Mechanism owner |
|---|---|---|---|
| **what changed** | yes | the change is explainable | the owning Record Model |
| **when** | yes | the change is placed in time, on a named axis | the owning Record Model |
| **why** | yes | the reason is recoverable | the owning Record Model |
| **who approved it** | yes | the approving act is traceable | the owning Record Model |
| **what caused it** | yes | the cause is traceable, and true | the owning Record Model |

**This table defines obligations, not schema.** No row is a field, and no column is a structure.

### 5.1 What changed

The account MUST make the change explainable. How a change is represented — a prior and resulting
state, a diff, a new version, a superseding Record — IS MODEL-OWNED. Blueprint §12.9's description
of a History Record entry is World's answer, not the form of the answer (§6.4 below).

### 5.2 When

The account MUST place the change in time, and the placement MUST name its axis: §12.16, P-21,
*"every temporal statement, query, ordering, projection, and history entry names its axis."* Which
axis a model records, and where, IS MODEL-OWNED; axis meaning is §12.16's (§9 below).

### 5.3 Why

The account MUST make the reason recoverable. Blueprint §13.7b gives provenance the question *who
made this, when, and why*; a model MAY answer P-18's *why* through provenance or through another
mechanism it owns. Provenance capture alone DOES NOT ESTABLISH the whole temporal account (§8
below).

### 5.4 Who approved it

The account MUST make the approving act traceable. This is not provenance's *who*: Blueprint §13.7b
gives audit the question *"Under what approval mode, in which session, by whose act"*, and I-14
requires that *"Approval mode is recorded, not merely the fact of approval."* Artifact 049 §5.2
keeps the two apart. The Human Gate and the Authority framework remain Spine-owned constitutional
mechanisms (Spine law 3; Artifact 051) and are not assigned to a Record Model by this contract. A
Record Model may own additional model-specific approval semantics or approval ceremony where its
governing model architecture provides them. How the approving act is represented in that model's
temporal account IS MODEL-OWNED.

### 5.5 What caused it

The account MUST make the cause traceable, and the cause MUST be true. P-18: *"Authorial intent is a
valid terminal answer to what caused it (Section 5.2); a fabricated world-internal cause is a
violation."* I-10: *"Authorial intent is a valid terminal cause; fabricated causality is a
violation."* How a cause is represented IS MODEL-OWNED (§10 below).

### 5.6 What "in full" means

A model satisfies P-18 **in full** when, for every change to state its Records hold
authoritatively, all five questions are answerable from that model's own temporal account — and
when no answer rests on a fabricated cause or an unaxised time. The five answers MAY be held in one
structure or distributed across several; the obligation judges answerability, not packaging. A
state whose account cannot answer them is, in P-18's words, *"an audit finding, not an acceptable
state."*

### 5.7 Source condition recorded, not resolved — "canonical state"

P-18 and I-09 are worded for *canonical state*. P-17, §13.6d, I-11, I-90 and RMS AD-11 bind the
obligation to every Record Model, and Production and Issue Records are never canonical (I-104;
Artifact 052). This contract applies the obligation to all six models, as P-17, §13.6d, I-90 and
AD-11 direct. It does not read P-18's wording as making any Production or Issue Record canonical,
nor as exempting either model; §13.6d names *"a published issue whose publication left no trace"*
as a breach of P-18. What P-18's *canonical state* denotes in a model without canonicality is left
to that model's temporal architecture, under Artifact 052.

## 6. Universal Obligation vs Model-Owned Mechanism

### 6.1 Universal

| Universal | Source |
|---|---|
| The obligation of a complete, traceable account of authoritative evolution | P-17; I-90 |
| The five questions, answerable in full | P-18; I-09 |
| Every temporal statement names its axis | P-21; §12.16 |
| Authorial intent is a valid terminal cause; fabricated causality is a violation | P-18; I-10 |
| History explains current state and is never a second canon or source of truth | P-17 |
| Semantic history is never reconstructed from version control | I-85 |

### 6.2 Model-owned

| Model-owned | Source |
|---|---|
| The packaging of the temporal account | §13.6d; §13.7a; I-90 |
| Whether the model has any structure shaped like a History Record | §13.6d; I-102 |
| What a temporal entry is, and where audit sits within it | §13.7b; Artifact 049 §5.2 |
| Revision and version semantics | §13.7b |
| The meaning of identity operations outside World | **OPEN** — §13.8 |

### 6.3 The firewall

Four constitutional rules keep the obligation from turning into a shared mechanism:

- **I-101** — *"No Record Model is a specialization of another, and no Record Model is the template
  for another."*
- **I-103** — *"Shared infrastructure never confers shared meaning."*
- **I-90** — the obligation is required of every model; the mechanism is model-owned.
- **I-107** — *"A package composition declared for a Record Model that has not been independently
  designed is provisional and may not be implemented as a requirement."*

| Statement | Verdict |
|---|---|
| *All models use History Records.* | **INVALID** — I-90, I-102 |
| *Each model must implement the World temporal package.* | **INVALID** — I-101, I-107 |
| *All temporal entries have the same universal schema.* | **INVALID** — §13.7a, I-103 |
| *Every Record Model MUST satisfy P-18 in full through its own mechanism.* | **VALID** — P-17, I-90 |

### 6.4 The World History Record boundary

**The History Record IS WORLD-SCOPED.** I-102: *"Relationship Record and History Record are World
Record Model concepts. Neither is a Record System primitive, and neither may be required of another
Record Model."* §13.7a: *"No Universal History Record. The P-18 obligation is universal; its
packaging is model-owned (§13.6d)."*

**I-11 is read as World-scoped.** I-11 carries the flag *"scope flagged v0.7.0 — AD-11"* and binds
*"Every World Record"* to *"exactly one logical history record"*, with WSV-H for WSV. Blueprint
§13.6d adopted the World reading and recorded the ambiguity; RMS AD-11 closed it: *"I-11 is a World
invariant. The World History Record is World-only; the universal survivor is the P-17/P-18
traceability obligation, which binds all six models through their own mechanisms."* This contract
does not reopen AD-11 and does not amend I-11. I-11's own second sentence carries the universal
half: *"Every Record Model must satisfy P-18 in full; the packaging of its temporal account is
model-owned (§13.6d)."*

**Why the universal reading was retired.** §13.6d: v0.6.1's claim that the History Record is
universal *"stated a mechanism where a requirement was meant"*, and read as universal, I-11
*"constrains five models' temporal architecture before those models exist."* A mechanism proven
for one model would have bound six.

**What §13.6d's package table is.** Its E, P, R, V and I rows record `Record + History Record`
shapes as *"MODEL-DESIGN INPUT (not a freeze)"*; *"a model may conclude that it needs no History
Record at all"*, or declare *"an event log, a revision chain, a version lineage, or a publication
provenance stamp — provided the P-18 obligation is met in full."* A model that chooses a structure
of the same shape does so as its own design decision; it is not thereby using World's History
Record, and no other model is bound by the choice.

## 7. The Six Record Models

Every model is bound by the obligation. No model's mechanism is prescribed here.

| Model | Bound by P-18 in full | Mechanism | Status | Downstream temporal work (Roadmap) |
|---|---|---|---|---|
| **W** World | yes | History Record; WSV-H for WSV | **ESTABLISHED** — I-11, §12.9, §13.9 | 200, 201, 203 |
| **E** Epistemic | yes | model-owned | DOWNSTREAM MODEL SPECIFICATION | 278 |
| **P** Production | yes | model-owned | DOWNSTREAM MODEL SPECIFICATION | 339 |
| **R** Registry | yes | Registry-owned (§13.6d) | DOWNSTREAM MODEL SPECIFICATION | 108–110 |
| **V** Visual | yes | model-owned | DOWNSTREAM MODEL SPECIFICATION | 357 |
| **I** Issue | yes | model-owned | DOWNSTREAM MODEL SPECIFICATION | 377, 378 |

### 7.1 World

World's mechanism is described here only to fix the boundary: one logical History Record per World
Record, append-only, WSV-H for WSV (I-11, §12.9). Its specification is Artifacts 200–203. World is
the only model whose mechanism the Blueprint establishes, and it is not a template (I-101).

### 7.2 Epistemic

MODEL-OWNED. Row 278's Val reads *"model-owned epistemic transitions"* and *"no World History
Record"*. Those words are row 278's; this contract adds nothing to them.

### 7.3 Production

MODEL-OWNED. Blueprint §9.1 changes Production State by production ceremony, not the canon path;
its temporal account is Production's to design (Artifact 339). No ceremony, transition, revision or
decision-history structure is prescribed here.

### 7.4 Registry

REGISTRY-OWNED (§13.6d). Row 108's Done reads *"temporal account without a World History Record"*.
No Registry history, revision or version packaging is defined here.

### 7.5 Visual

MODEL-OWNED. Row 357's Val reads *"specification revision"*. No specification revision, asset
variant or *visual derivation* rule is defined here.

### 7.6 Issue

MODEL-OWNED. Issue *"versions by supersession, never by edit"* (§13.7b). That is Issue's rule and
is not a rule for any other model (I-101).

**Roadmap condition recorded, not resolved.** Rows 200, 203, 278, 339 and 357 name 054 as a hard
dependency. The Registry's temporal contracts (108–110) and the Issue temporal contract (378) do
not, and row 054's `→` names P7 and P10–P13 but not P3. The obligation binds R and I regardless
(§13.6d, I-90, AD-11). This contract adds no dependency edge to any row.

## 8. Relationship to Neighbouring Constitutional Artifacts

| Artifact | Owns | Relationship to 054 |
|---|---|---|
| **047** provenance capture | the shared capture mechanism: who, when, why | 054 does not redefine it. Capture is one input to a temporal account, not the account. |
| **048** provenance meaning | what provenance means, per model | 054 does not redefine it. |
| **049** temporal terms | the six terms and their questions; the retired word | hard dependency (`H: 049`). 054 defines no term and reopens no retirement. |
| **050** source-of-truth classification | which class a data class carries | a temporal account determines no class. |
| **051** authority | who may commit; what a Record governs | a temporal account confers no authority. |
| **052** canonicality | what canonical means, per model | a temporal account confers no canonicality. |

```
P-18   = the obligation
049    = the vocabulary separation
model temporal architecture = the mechanism
133    = the enforcement
```

054 is none of the last three.

**Provenance is not the temporal obligation.** Provenance answers who made a Record, when and why
(§13.7b). It DOES NOT ESTABLISH audit, history, revision, version or `derivation`, and it does not
answer *who approved it*, which §13.7b gives to audit. A model whose only temporal mechanism is
provenance capture has not thereby satisfied P-18.

**History does not establish current state.** P-17: *"current state is authoritative, history
explains how it came to exist. History is never a second canon and never a second source of
truth."* For World, I-08: *"Current canonical state is authoritative; history explains it and never
establishes it."* Where a model's current state is authoritative is that model's (Artifacts 050,
052); a temporal account does not make it so.

## 9. Temporal Axis Boundary

Axis meaning is Blueprint §12.16's. Its three canonical axes are World Time, Session Number and
Real-World Time; *"The issue ordinal is a sequence, not a temporal axis."* Its rule binds every
temporal account: every history entry *"names its axis"*, and *"no axis is derivable from
another"*. A tool timestamp is not an axis: *"None of those is automatically World Time, Session
Number, or Real-World Time"*.

**Source note.** §12.16's axis table names where Session Number and Real-World Time are
authoritative — among them *"History Record, WSV-H"*. That column names World's mechanisms. This
contract does not read it as requiring a History Record of any other model (I-90, I-102); where a
non-World model records either axis IS MODEL-OWNED.

054 defines no timestamp field, temporal datatype, clock, ordering algorithm, time object or
serialization.

## 10. Causality and Approval Boundary

**Causality.** Three answers, and only two are legitimate:

| Answer to *what caused it* | Status | Source |
|---|---|---|
| a recorded cause — for World, a simulated or world-internal one | legitimate | Blueprint §5.2 |
| authorial intent, as a terminal cause | legitimate | P-18; I-10; Blueprint §5.2 |
| a cause invented after the fact to satisfy the question | **violation** | P-18; I-10 |

Blueprint §5.2: *"Requiring a world-internal cause for every change would produce fabricated
causality, which is worse than none."* Both kinds of cause are valid; *"neither may be invented to
satisfy an audit."* Blueprint §15.13 shows the honest form in World: a consequence accepted without
its simulated cause is recorded with an authorial cause instead. 054 defines no causal graph,
causal-edge taxonomy, causal record or inference mechanism.

**Approval.** *Who approved it* is audit's question, not provenance's (§5.4 above; §13.7b; I-14;
Artifact 049 §5.2). 054 defines no audit record and no approval field.

## 11. What 054 Does Not Define

1. A universal History Record.
2. A universal temporal Record.
3. A temporal schema or temporal field list.
4. Temporal data types.
5. Timestamp or clock implementation.
6. Temporal storage or a history database.
7. A universal audit record.
8. A universal revision object.
9. A universal version object.
10. A universal lifecycle.
11. A universal causality graph.
12. A universal `derivation` graph, or any graph for the retired word's senses.
13. A universal temporal API.
14. A temporal validator implementation (Artifact 133).
15. Any model's temporal architecture.
16. Record Model design or Kind design.
17. Canonicality (052), authority (051), source-of-truth semantics (050), provenance semantics
    (047, 048).
18. Implementation details of any kind.

## 12. Prohibited Architectural Moves

Each is prohibited because it breaks the sovereignty I-90, I-101, I-103 and I-107 establish.

1. A universal History Record.
2. A universal temporal Record.
3. A universal history-entry object.
4. A universal revision object.
5. A universal version object.
6. A universal audit object.
7. A universal temporal package.
8. A universal lifecycle.
9. A universal temporal schema.
10. A universal temporal database table.
11. Universal temporal fields beyond the governing envelope.
12. A universal temporal API.
13. A universal temporal validator that owns semantics.
14. World's temporal architecture as a template for any other model.
15. Any model inheriting temporal semantics from another.
16. Reconstructing semantic history from a commit log (I-85).
17. Satisfying *what caused it* with a fabricated cause (P-18, I-10).
18. Treating an unaxised temporal claim as an answer to *when* (P-21).

**The anti-pattern, stated once.**

```
✗  World has a History Record  →  therefore E, P, R, V, I use a History Record

✓  World has a History Record  →  World satisfies the obligation through it
   E, P, R, V, I               →  satisfy the same obligation through mechanisms they own
```

## 13. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number.

| ID | Condition | Source |
|---|---|---|
| **C-054-01** | The P-17/P-18 temporal obligation applies to all six Record Models. | P-17; §13.6d; I-90; RMS AD-11 |
| **C-054-02** | Each Record Model satisfies P-18 in full: all five questions answerable for every change. | P-18; I-09; I-11; §13.6d |
| **C-054-03** | The mechanism satisfying the obligation is owned by the Record Model. | P-17; I-90; §13.6d |
| **C-054-04** | The World History Record is not a Record System primitive and is required of no other model. | I-102; §12.9; §13.7a |
| **C-054-05** | I-11 is read as World-scoped under the closed AD-11 decision. | I-11; RMS AD-11 |
| **C-054-06** | No Record Model inherits temporal architecture from another. | I-101; I-107 |
| **C-054-07** | No universal temporal schema, package or lifecycle is established. | §13.7a; RMS §4 |
| **C-054-08** | 054 does not redefine the six temporal terms fixed by 049. | Roadmap row 054 `H: 049` |
| **C-054-09** | 054 does not redefine provenance capture or provenance meaning. | §13.7a; Artifacts 047, 048 |
| **C-054-10** | Temporal-axis meaning remains §12.16's; every temporal claim names its axis. | §12.16; P-21 |
| **C-054-11** | Approval and audit do not collapse into provenance. | §13.7b; I-14 |
| **C-054-12** | Current state is not made authoritative because a temporal account exists. | P-17; I-08 |
| **C-054-13** | No Record, Kind, field, schema, runtime mechanism or storage structure is created. | Roadmap row 054 `T: doc` |
| **C-054-14** | Examples are non-normative. | — this contract, §14 |
| **C-054-15** | Downstream model temporal architectures remain owned by their models. | §13.6d; I-90 |
| **C-054-16** | Semantic history is never reconstructed from version control. | I-85 |

A construction satisfying all sixteen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 14. Worked Examples

**Every example below is illustrative and non-normative.** No example defines a structure, field,
entry or mechanism.

**Example A — same obligation, different mechanisms.** A World Record's change is answered by its
History Record. A Production Record's change might be answered by an authored revision, the
production ceremony that approved it, and a decision record. The two share no representation. Both
can satisfy P-18.

**Example B — one structure or several.** Model A holds all five answers in one temporal entry.
Model B distributes them: *what changed* and *when* in a revision chain, *who approved it* in an
approval record, *why* and *what caused it* in provenance and a decision note. Both are potentially
conformant. The constitution judges answerability, not whether the packaging matches.

**Example C — the six models.**

| Model | Illustrative mechanism | Owner |
|---|---|---|
| W | the World History Record | World — established |
| E | epistemic transitions, evidence and provenance | E — as E defines later |
| P | authored production evolution | P — as P defines later |
| R | definition evolution | R — as R defines later |
| V | specification and asset evolution | V — as V defines later |
| I | publication and supersession | I — as I defines later |

**Example D — causality.** A World change accepted from a simulation, without the simulated cause
the author rejected, is recorded with the author's decision as its cause (§15.13). Recording the
rejected cause, or inventing a new world-internal one, would be fabricated causality.

**Example E — provenance is not enough.** A Registry definition carries provenance: who made it,
when, why. If nothing records who approved the change or what the definition was before, the
definition *"changed without a record"* in §13.6d's sense, and P-18 is not satisfied.

## 15. Source Traceability

| Rule | Source |
|---|---|
| The obligation is universal; the mechanism is model-owned | P-17; §13.6d; I-90; RMS §16 |
| Every model satisfies P-18 | §13.6d; I-11; I-90; RMS AD-11 |
| The five questions; audit finding if unanswerable | P-18; I-09 |
| Spine law 9's reach: the entire evolutionary path | Blueprint §10 |
| History Record is World-specific, not a primitive | I-102; §12.9; §13.7a; I-90 |
| I-11 is World-scoped | I-11; §13.6d; RMS §17 AD-11, §27 |
| Why universalization was retired | §13.6d |
| Packaging is model-owned; package rows are design input | §13.6d; I-107 |
| No model is another's template | I-101 |
| Shared mechanism does not create shared semantics | I-103; §13.7a |
| Temporal vocabulary belongs to 049 | Blueprint §13.7b; Artifact 049 |
| Provenance capture shared; meaning model-owned | Blueprint §13.7a; Artifacts 047, 048 |
| Axis rule; issue ordinal not an axis; tool timestamps not axes | Blueprint §12.16; P-21 |
| Approval mode belongs to audit | Blueprint §13.7b; I-14 |
| Authorial intent terminal; fabricated causality a violation | P-18; I-10; Blueprint §5.2, §15.13 |
| History does not establish current state | P-17; I-08; §12.9 |
| Version control is not a temporal mechanism | I-85 |
| Identity operations' meaning outside World is OPEN | §13.8 |
| Production and Issue never canonical | I-104; Artifact 052 |
| Downstream temporal work | Roadmap rows 108–110, 133, 200, 201, 203, 278, 339, 357, 377, 378 |
| Hard dependency on 049; unlocks P7, P10–P13 | Roadmap row 054 |
| Temporal matrix absent | RMS §16, Appendix D |

## 16. Downstream Obligations

- **Each model's temporal architecture** (W 200–203, E 278, P 339, R 108–110, V 357, I 377–378)
  MUST show how its own mechanism answers each of the five P-18 questions, and owns everything
  about how. It MUST NOT adopt World's History Record as a requirement it did not design (I-107).
- **Artifact 133**, the temporal validator, enforces the obligation — row 133's Val: *"each model's
  obligation satisfied by its own mechanism"*. It checks answerability against each model's own
  declared mechanism; it does not supply one.
- **Open questions stay open.** What identity operations mean outside World is **OPEN** (§13.8).
  How I-12 and I-13 apply to a non-World mechanism is **OPEN OUTSIDE 054**: this contract neither
  extends nor limits them. The P-18 answers themselves are protected for every model by P-18.

---

*Artifact 054 · P2/2d · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the temporal obligation contract — the obligation universal, the mechanism
model-owned — derived from Blueprint P-17, P-18, §12.9 and §13.6d, and RMS §16 and AD-11. It does
not amend them, reopens no decision, and defines no Record, field, schema, package or lifecycle.
Where it differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap,
those governing sources are correct and this document is wrong.*
