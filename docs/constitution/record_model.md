# COOLBOY12 — Record Model Definition

**Artifact 042** · `docs/constitution/record_model.md` · Own: CONST · RM: all · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a ·
Req: RR-06 · BP: §13 · RMS: §6 · H: 039 · S: — · LS: — · G: — ·
→ 040 · Risk: medium · ∥: no

## 1. Purpose

Row 042 states the failure this artifact exists to prevent: **"the place where X lives" is not
a definition.**

A Record Model is not the folder a Record sits in, the schema it validates against, or the
partition it carries. Those are consequences. This document states what a Record Model **is**,
by stating what it **owns** — which is what row 042's `Val` requires: *what a Record Model owns,
enumerated.*

Nine dimensions of semantic ownership are enumerated in §4. They are RMS §6's, unaltered.

## 2. Scope

This document defines the **category** *Record Model*. It specifies no particular model.

It answers: what qualifies something as a Record Model, and what does a Record Model own? It
does not answer what World's kinds are, what Issue's lifecycle is, or what Registry validates —
those belong to each model's own design work, and to the artifacts named in §10.

> **A common definition of a category is not a common semantic parent.** Defining what a Record
> Model *is* creates no model above, beneath, or between the six. Artifact 041 forbids that, and
> this document introduces nothing that would evade it.

## 3. Formal Definition

> **RMS §6** — *"A **Record Model** is a partition-owned semantic architecture that answers a
> distinct class of question and owns: its Kind taxonomy, identity semantics, state and
> lifecycle, relationship packaging, temporal architecture, provenance meaning, canonicality
> meaning (if any), semantic validation, and package composition."*

Blueprint §13 states the same definition in its own words, and adds the boundary clause: a
Record Model is *"a partition-owned semantic model that defines, **for its own partition and no
other**"*, what kinds of Records exist, what identity means, how state and lifecycle work, how
relationships are represented and packaged, how temporal and version semantics work, how
provenance and authority are represented, and how its Records are stored and validated.

Three elements, each necessary:

```
Record Model = partition-owned
             + answers a distinct class of question
             + owns the nine semantic dimensions of §4
```

**RMS §6 adds the reading that governs all three:** *"This is semantic ownership, not
categorization."* A Record Model is not a bucket that Records are sorted into. It is the
architecture that decides what its Records mean.

## 4. The Nine Ownership Dimensions

RMS §6's enumeration, in its own order. Each is a **semantic** dimension: a claim about meaning,
not a facility. Each belongs to the Record Model because meaning cannot be shared without
evidence in each model that carries it (I-103).

**What this section does and does not do.** It states *what* a Record Model owns. It does not
state *how* any model designs that ownership — that is each model's own work, bounded by the
artifact named in the table's third column.

| # | Dimension | What the Record Model owns | Not specified here — owner |
|---|---|---|---|
| 1 | **Kind taxonomy** | which Kinds exist within the model, and what each means | any model's concrete Kind roster — the model's own design work; the admission test is **057** |
| 2 | **Identity semantics** | what constitutes the identity of a Record in that model | the identity grammar (**034**) and the identity semantics boundary (**046**) |
| 3 | **State and lifecycle** | the model's state vocabulary and what its transitions mean | any concrete state machine — the model's own design work |
| 4 | **Relationship packaging** | how the model represents and packages relationships among its Records | relationship legality — **055** |
| 5 | **Temporal architecture** | the model's own account of time, history, and version | the temporal vocabulary (**049**) and the temporal obligation (**054**) |
| 6 | **Provenance meaning** | what provenance *means* in that model | provenance capture, which is a mechanism — **047**; the meaning boundary — **048** |
| 7 | **Canonicality meaning (if any)** | what canonical means in that model, **for models that have canonicality at all** | the canonicality framework — **052**; authority — **051** |
| 8 | **Semantic validation** | which of its Records are meaningful, beyond well-formed | structural validation, which is a mechanism (**037**); the split — **043** |
| 9 | **Package composition** | how the model composes its Records into packages | the package boundary — **056** |

**Dimension 7 carries a qualifier that MUST NOT be dropped.** RMS §6 writes *"canonicality
meaning (if any)"*. A Record Model owns the meaning of canonicality **if that model has
canonicality**; it is not the case that every Record Model has one. I-104 states why: *"Record
and Canon are not synonyms. Canonicality is a status property whose meaning is defined by each
Record Model that has one, and two models hold Records that are never canonical."* Which models
those are, and what canonical means where it applies, is **Artifact 052**.

**Dimensions 6 and 8 each name a meaning whose mechanism is shared.** Provenance *capture* and
*structural* validation are common facilities; provenance *meaning* and *semantic* validation
are model-owned. §7 states the general rule; **Artifact 043** owns the full split.

**Owning a dimension does not freeze its contents.** A model owns its Kind taxonomy whether that
taxonomy is settled or still being designed — I-106: *"A kind roster that is listed is not
thereby frozen."* This document establishes ownership, and freezes nothing inside any model.

## 5. What "Owns" Means

**Ownership here is semantic authority over meaning within the model.** It is not filesystem
ownership, source-code ownership, storage ownership, database ownership, or implementation
ownership. Blueprint §13 fixes the boundary in one phrase: a Record Model defines these things
**"for its own partition and no other"**.

Two consequences, both source-stated:

- **Ownership is bounded by the model.** A Record Model's authority reaches its own Records and
  stops. Registry is the case where this matters most: I-105 states that Registry *"holds
  semantic authority over definitions and never semantic ownership of another model's Records"*.
  A World Record that resolves a Registry definition remains World's Record, semantically.
- **Ownership is not authority in general.** Who may commit a change, and under what ceremony,
  is **Artifact 051**. This document says only that the semantics of a model's Records are that
  model's.

## 6. Record Model and Record

A **Record** and a **Record Model** are different architectural things, and Blueprint §13.0
exists because collapsing them is the error the Record System was rebuilt to prevent.

```
Record Model  ──owns the semantics of──▶  Record
```

- A **Record** is *"a persistent semantic unit owned by exactly one Record Model"* (Blueprint
  §13, §13.0).
- A **Record Model** owns what its Records mean.

A Record Model is **not** a collection of Records, and not the place its Records are kept.
I-87 states the distinction this document must not lose: *"Record is the common **architectural**
data unit of the Record System — not a universal semantic model. Every Record belongs to exactly
one of six partitions; **the semantics of a Record are owned by its Record Model**"*.

That one invariant carries the whole shape of §2's warning: Record is architecturally common
across the six; meaning is not.

## 7. Record Model and Shared Mechanism

**A Record Model MUST NOT acquire semantic ownership of a mechanism merely by using it.**

> **I-103** — *a mechanism may be shared; a semantic may not be shared without evidence in each
> model that carries it.*

Identity, addressing, serialization, structural validation, provenance capture, reference
resolution, storage, indexing and mutation coordination are common to the six (Artifact 039 §6).
Using them changes nothing about what a model's Records mean, and conversely, a model's
ownership of a dimension in §4 makes no claim on the facility beneath it.

**Artifact 043** owns the mechanism/semantics boundary in full. This document states only the
consequence for the definition.

## 8. Record Model and Kind

```
Record Model  ──owns──▶  Kind taxonomy  ──contains──▶  Kinds
```

A **Kind** is a class of Record within one model (RMS §6.1). A Kind is **not** a Record Model,
not a smaller Record Model, and not a unit of sovereignty: the sovereign party is the model, and
a model's Kinds are one of the nine things it owns. **Artifact 044** owns the architectural
categories, and each model's roster is its own.

## 9. The Six Sovereign Record Models

Six models are governed by this definition — **W** World · **E** Epistemic · **P** Production ·
**R** Registry · **V** Visual · **I** Issue (RMS §2). Each is identified in **Artifact 040**;
their sovereignty is contracted in **Artifact 041**. Neither is restated here.

**They are not specializations of this definition.** A definition of a category creates no
parent to specialize. Artifact 041 S-6 and S-7 prohibit semantic specialization between models,
and RMS §2 states that *"No model is a superclass of another"* — this document creates no
exception, and no seventh model.

Two examples, which introduce no rule:

- **World** owns its own Kind taxonomy, lifecycle and temporal architecture. It owns them
  because it is a Record Model, not because it is the model others are shaped from — *"World is
  not a template"* (RMS §2), and *"Nothing inherits from World"* (RMS §30).
- **Registry** owns the semantics of its own Records and its definitions. A World Record that
  resolves a Registry definition does not thereby become Registry's semantically (I-105).

## 10. Boundary and Non-Goals

This document defines the category and enumerates the ownership. It does **not** define:

| Not defined here | Owner |
|---|---|
| any model's concrete Kind roster | that model's own design work; admission test **057** |
| concrete schemas and fields | model-specific design work |
| lifecycle state machines | model-specific design work |
| identity semantics in detail | **046** (grammar: **034**) |
| relationship legality | **055** |
| the temporal contract | **049**, **054** |
| provenance meaning in detail | **048** (capture mechanism: **047**) |
| the canonicality and authority frameworks | **052**, **051** |
| package structure | **056** |
| the mechanism/semantics boundary in full | **043** |
| the architectural categories | **044** |
| partition ownership in detail | **045** |
| cross-model dependency rules | **058** |
| conformance implementation | **059** |

Nothing above is anticipated here, and this document may not be cited as having settled any of
it.

## 11. Conformance Conditions

Conditions derivable from the definition and from the already-contracted sovereignty boundary.
They are stated here; **Artifact 059** owns the P2 kernel conformance suite, and this document
implements no test.

| ID | Condition | Basis |
|---|---|---|
| **RM-C01** | A Record Model is partition-owned. | RMS §6, Blueprint §13, I-16 |
| **RM-C02** | A Record Model answers a distinct class of question. | RMS §6 |
| **RM-C03** | A Record Model owns all nine dimensions of §4. | RMS §6 |
| **RM-C04** | The canonicality dimension is qualified *(if any)* and is not required of every Record Model. | RMS §6, I-104 |
| **RM-C05** | A Record Model's semantic ownership is distinct from the mechanisms it uses. | I-103, Blueprint §13.7a |
| **RM-C06** | A Record Model does not derive its semantic identity from another Record Model. | Artifact 041 S-3, I-101 |
| **RM-C07** | This definition introduces no universal semantic Record Model and no additional Record Model. | Artifact 041 S-9, I-87, RMS §2 |

## 12. Dependencies and Downstream Ownership

| | |
|---|---|
| Hard dependency | **039** — the Record System constitution |
| Soft dependency | — (row 042) |
| Unlocks | **040** (row 042, `→ 040`) |

Upstream, this document relies on **039** for the Record System architecture and on **041** for
the sovereignty boundary it must not evade; it restates neither.

**On the unlock.** Row 042 declares `→ 040` while row 040 declares `H: 039, S: —`. The two are
consistent under the project's own reading — an unlock is not a dependency — and the ordering
consequence is simply that this definition governs the six stubs rather than gating them. It is
recorded here for traceability, and this document does not reinterpret either row.

---

*Artifact 042 · P2/2a · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the definition established by RMS §6 and Blueprint §13, with invariants I-87,
I-103, I-104, I-105 and I-106. It is not a Record, holds no canonical data, and creates no
architecture of its own.*
