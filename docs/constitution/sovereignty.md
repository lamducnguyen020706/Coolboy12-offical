# COOLBOY12 — Six-Model Sovereignty Contract

**Artifact 041** · `docs/constitution/sovereignty.md` · Own: CONST · RM: all · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a ·
Req: BR-17,RR-02 · BP: §13.6 · RMS: §2 · H: 039 · S: 040 · LS: — · G: — ·
→ all models · Risk: high · ∥: no

## 1. Purpose

Row 041 states this artifact's reason in four words: **I-101 made buildable.**

> **I-101** — *"Every partition owns exactly one sovereign Record Model. No Record Model is a
> specialization of another, and no Record Model is the template for another."*
> (Blueprint §13, §13.2)

Artifact 039 states sovereignty as a constitutional principle. This document states it as a
**contract**: explicit rules, explicitly prohibited constructions, and conditions that can be
checked. It adds no architecture. The rules below are source-grounded contractual formulations of
the sovereignty requirements established by I-101, RMS §2 and Blueprint §13/§13.6, together
with the supporting invariants each rule cites.

## 2. Scope

This contract governs **the constitutional relationship among the six sovereign Record
Models** — how they coexist without collapsing into one another.

It does **not** govern what any one model contains. Artifact 040 establishes the six model
identities and the question each alone answers; this document takes those six as given and
does not restate them. What a Record Model *is*, formally, is Artifact 042.

```
039  Record System architecture
  ↓
040  six model identities and their semantic questions
  ↓
041  the sovereignty contract among those six      ← here
  ↓
042  the formal Record Model definition
```

## 3. The Sovereign Record Models

Exactly six, named as RMS §2 names them:

| | Model |
|---|---|
| **W** | World |
| **E** | Epistemic |
| **P** | Production |
| **R** | Registry |
| **V** | Visual |
| **I** | Issue |

Each is identified, with the question it alone answers, in **Artifact 040**. This contract
names them only to identify the six parties it binds.

**There is no seventh.** No additional semantic Record Model MAY be introduced above, below,
between, or alongside the six — whether described as a base model, sub-model, family,
meta-model, abstract model, or by any other name. The test is what a construction *does*:
a naming or grouping convention that owns no semantics is not a Record Model and is not
prohibited here.

## 4. Sovereignty Rule

**S-1.** Every partition MUST own exactly one sovereign Record Model, and every Record MUST
carry exactly one partition (I-16, I-101).

**S-2.** Each Record Model MUST own its own semantics. Blueprint §13.6 states what sovereignty
covers, and this contract adopts that statement without extension: what the six *"do not share
is ontology, kind taxonomy, identity semantics, relationship packaging, temporal architecture,
lifecycle, or canonicality."*

**S-3.** No Record Model MAY derive its semantic identity from another Record Model. Each
model's semantics are its own.

**S-4.** No Record Model MAY be treated as a configuration, variant, mode, profile, or
parameterization of another Record Model. Blueprint §13 states the same in the negative: the
six are *"sovereign, not six configurations of one model"*.

**S-5.** Sovereignty MUST survive shared mechanism. A model that uses common identity,
validation, serialization, or storage machinery remains a distinct semantic owner (§8).

## 5. Non-Specialization Rule

**S-6.** **No sovereign Record Model is a semantic specialization of another sovereign Record
Model.** This is I-101 and RMS §2 (*"No model is a superclass of another"*), and it holds in
both directions between any two models and through any chain of models. What is prohibited is
a construction in which one model's *meaning* is a case, refinement, or restriction of
another's; the words used to describe it do not decide the question.

**S-7.** No Record Model MAY inherit semantics from another. Blueprint §13.6: *"A Record Model
is not a specialization of a universal model and does not inherit from one."*

### Prohibited constructions

Each of these is forbidden by S-6 and S-7, in this or any equivalent form:

```
FORBIDDEN                          FORBIDDEN                 FORBIDDEN
UniversalRecord                    World                     WorldModel
  └── WorldRecord                    └── Epistemic             ├── ProductionModel
        ├── EpistemicRecord                                    └── VisualModel
        ├── ProductionRecord
        ├── RegistryRecord
        ├── VisualRecord
        └── IssueRecord
```

### What S-6 does not prohibit

**S-6 is a rule about semantic sovereignty, not about software.** Implementation reuse is not
semantic inheritance. Common utilities, shared libraries, a shared parser, a shared base class
in code — none of these is prohibited by this contract, and none of them makes two models one
model. What is prohibited is a claim that one model's *meaning* derives from another's.

```
implementation reuse   ≠   semantic inheritance
shared mechanism       ≠   shared model sovereignty
interaction            ≠   specialization
reference              ≠   inheritance
dependency             ≠   superclass
```

### Relationship matrix

| Relation | Allowed | Basis |
|---|---|---|
| Any model semantically specializes any other model, in any direction | **NO** | S-6, I-101, RMS §2 |
| World is the base, parent, or template of another model | **NO** | S-8, I-101, RMS §2, §30 |
| A universal semantic Record Model above, beneath, or between the six | **NO** | S-9, RMS §4 |
| An additional semantic Record Model, introduced under another name | **NO** | §3, RMS §2, §25 |
| Two models share a mechanism | **YES**, sovereignty unaffected | S-5, I-103, Blueprint §13.7a |
| Two models share implementation code | **YES**, unless the shared construction establishes semantic inheritance, semantic ownership, or specialization between models | S-6 |
| A Record converts from one partition to another | **Deferred** — Artifact 045 | not decided here |
| One model references another | **Deferred** — Artifacts 055 and 058 | not decided here |

The deferred rows are deferred deliberately. Reference legality between models is Artifact
055's and Artifact 058's to decide, and partition conversion is Artifact 045's; this contract
neither permits nor forbids either, and a downstream artifact MUST NOT read silence here as
either answer.

## 6. World Is Not a Template

**S-8.** **World is not a template.** No Record Model MAY be derived from World, shaped to
World, or defaulted to World's structure. RMS §2 states it; RMS §30 states the consequence —
*"Nothing inherits from World"*; I-101 binds it as an invariant.

World MUST NOT be treated as any of the following:

- a universal template;
- a base or parent Record Model;
- a universal Record shape;
- the default semantic structure from which the other models derive;
- the model whose properties another model inherits by omission.

**Maturity confers no authority over another model.** World is the most mature of the six, and
Blueprint §13.6 states that this is precisely not a licence: *"No model is the template for
another, and World — the most mature of the six — is explicitly not the template"*. Blueprint
§13.2 records why the one-model argument was sound within World and wrong when *"extended past
its evidence."*

## 7. No Universal Semantic Record Model

**S-9.** No universal semantic Record Model MAY exist above, beneath, or between the six.
RMS §4 freezes the prohibition first among its nine: *"no Universal Record Base"*. Blueprint
§13 states the reason in one sentence — *"The Record System is not the Record Model Schema
under a new noun."* The nine prohibitions in full, verbatim and binding, are **Artifact 043**;
this contract states only the one that sovereignty rests on.

Prohibited in this or any equivalent form: a universal Record carrying the semantics of all six;
a base Record acting as semantic parent; one object whose type field selects W/E/P/R/V/I; one
model with per-model flags, modes, or profiles; World in any of those roles.

**S-10.** The prohibition is on a universal **semantic** model, and on nothing else. A shared
structural envelope or a shared mechanism does not thereby constitute a universal semantic
Record Model: a structure common to six models makes no claim about what any of them means.
The envelope is Artifact 033's and the mechanism layer is Artifact 043's; neither is
authorized, defined, or bounded here.

## 8. Shared Mechanisms Do Not Transfer Sovereignty

This section applies **S-5**, because it is the rule most easily lost: **a mechanism may be
shared; sovereignty is not shared with it.**

> **I-103** — *a mechanism may be shared; a semantic may not be shared without evidence in each
> model that carries it.*

Identity machinery, addressing, structural validation, serialization, provenance capture,
reference resolution, indexing, storage, and mutation coordination are common to the six
(Artifact 039 §6). None of them makes two models one model, and none of them gives one model
standing over another.

**This contract states the sovereignty consequence only.** Which facilities are shared, what
each does not decide, and where the mechanism/semantics line falls in each case is **Artifact
043**. This document does not restate it.

## 9. Partition and Model Ownership

**S-1** restated with its source. I-16 establishes that *"every partition owns exactly one
sovereign Record Model"*, and that clause is the whole of what sovereignty needs from it.

```
one partition  ──owns──▶  exactly one sovereign Record Model
```

**What S-1 is not.** Partition ownership here is **semantic** ownership only: it makes no claim
that a partition is one implementation class, schema, file, table, or store.

**What this document does not define.** The partition ownership contract is **Artifact 045**.
Cross-partition conversion, partition mechanics, storage, schema, and operational transitions
are its to state — including the remainder of I-16 — and none of them is decided here.

## 10. Conformance Conditions

The conditions this contract must be checkable against. They are stated here; **Artifact 059**
owns the P2 kernel conformance suite, and this document implements no test.

| ID | Condition | Basis |
|---|---|---|
| **C-01** | There are exactly six sovereign Record Models — W, E, P, R, V, I — and no additional semantic Record Model. | RMS §2, §25 |
| **C-02** | No Record Model is a semantic specialization of another, in any direction. | S-6, I-101 |
| **C-03** | World is not a template, base, or parent for any Record Model, and nothing inherits from World. | S-8, RMS §2, §30 |
| **C-04** | No universal semantic Record Model exists above, beneath, or between the six. | S-9, RMS §4 |
| **C-05** | No Record Model derives its semantic ownership from another Record Model. | S-3 |
| **C-06** | Shared mechanisms create no shared semantic sovereignty. | S-5, I-103 |
| **C-07** | Every partition owns exactly one sovereign Record Model. | S-1, I-101, I-16 |

**What C-07 does not carry.** Conformance for the rest of I-16 — that every Record carries
exactly one partition, and that no Record converts between partitions — is deferred to
**Artifact 045**. One conformance condition must not silently import a downstream contract.

A construction that satisfies every condition above is conformant **to this contract**. It is
not thereby conformant to the Record System: the other P2 contracts carry their own conditions.

## 11. Non-Goals and Boundary

**This contract establishes sovereignty only.** It does not define, for any Record Model, its
internal schema, Kind taxonomy, identity semantics, lifecycle, canonicality, authority, temporal
architecture, provenance meaning, relationship legality, package structure, or conformance
implementation. Each of those has an owner named in Artifact 039 §11, and none of them is
anticipated here.

**Sovereignty is frozen; the models' interiors are not.** This distinction is load-bearing and
must not be collapsed in either direction:

```
the sovereignty contract          FROZEN — this document
each model's internal design      per-model state — not this document's to declare
```

Blueprint §13.6 assigns each model its own kind-taxonomy status, and I-106 states that *"A kind
roster that is listed is not thereby frozen."* Nothing in this contract freezes any model's
interior, and nothing in it may be cited as having done so.

**The Bootstrap Meta-Contract is untouched by this contract.** It is constitutional and is not a
Record (RMS §10.4, Artifact 031); it is therefore not one of the six, not a seventh, and not
subject to rules written for Record Models. Artifact 039 §8 states its position.

## 12. Dependencies and Downstream Ownership

| | |
|---|---|
| Hard dependency | **039** — the Record System constitution |
| Soft dependency | **040** — the six model identities this contract binds |
| Unlocks | all models (row 041, `→ all models`) |

Downstream owners this contract defers to, and does not anticipate: **042** the formal Record
Model definition · **043** the mechanism/semantics boundary · **045** partition ownership ·
**055** relationship boundary · **058** cross-model dependency rules · **059** the P2 kernel
conformance suite.

Artifact 042 can define a Record Model formally without reference to anything decided here;
this contract binds the relationship among six models and defines none of them.

---

*Artifact 041 · P2/2a · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states a contract derived from Blueprint §13.6, RMS §2, and invariants I-16, I-101 and
I-103. It is not a Record, holds no canonical data, and creates no architecture of its own.*
