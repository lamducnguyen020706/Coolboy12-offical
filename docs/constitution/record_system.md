# COOLBOY12 — Record System Constitution

**Artifact 039** · `docs/constitution/record_system.md` · Own: CONST · RM: all · T: doc ·
R: ARCH · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2a ·
Req: BR-17,RR-01 · BP: §13 · RMS: §§2,3 · H: 031,033 · S: — · LS: — · G: — ·
→ 040–059 · Risk: HINGE · ∥: no

## 1. Constitutional Status

This document is the governing statement of the Record System architecture. It is
AUTHORITATIVE about that architecture and about nothing else. It establishes no new
architecture; it states what the Master Blueprint and the Record Model System have already
established, in one place, so that Artifacts 040–059 can build without redefining the
foundation.

Five constitutional facts, each stated at source and restated here without amendment:

1. **The Record System is the governing architecture.** Blueprint §13: *"The governing
   architecture is the Record System."*
2. **There are exactly six sovereign Record Models** — **W** World · **E** Epistemic ·
   **P** Production · **R** Registry · **V** Visual · **I** Issue (RMS §2).
3. **There is no seventh Record Model.** RMS §2 states the set as *"Exactly **six sovereign
   Record Models**"*, and RMS §25's missing-model audit concluded that no seventh is
   required.
4. **The Canon Object Model is retired.** RMS §2 states it *"fully superseded and retired as
   current architecture"*, and that the Record System governs in its place.
5. **No model is a superclass of another. World is not a template** (RMS §2, I-101).

This document does not amend the Blueprint, the Record Model System, or the Roadmap. Where it
and they differ, **they are right and this document is wrong.**

## 2. Purpose

The Record System is the architecture under which six sovereign semantic models coexist. This
document establishes that architecture as the starting point from which the P2 kernel contracts
derive, and its purpose is exactly two things: **architectural orientation** and
**constitutional authority**.

It is **not** a schema catalog, **not** a runtime specification, **not** a semantic
implementation, and **not** a substitute for the contracts listed in §11. Each of those
contracts owns a boundary that is named here and specified there. A reader who needs the rule
rather than the architecture is in the wrong document, and §11 says which one is right.

## 3. Governing Architecture

RMS §3 states the architecture. It is reproduced here as the structure this constitution
governs:

```
RECORD SYSTEM
├── CONSTITUTION (Blueprint, Spine, invariants)
│     └── BOOTSTRAP META-CONTRACT  ← constitutional, NOT a Record
├── Universal mechanism layer
│     identity · addressing · parsing · resolution · structural validation ·
│     serialization · provenance capture · Mutation Coordinator ·
│     reference resolution · indexing · storage/migration contracts
└── Six sovereign Record Models — each owning its own semantics
      W · E · P · R · V · I
```

Three layers, and the relationship between them is the whole architecture:

```
shared mechanisms  +  six sovereign semantic models  ≠  one universal semantic model
```

**Shared mechanisms are not shared semantics.** Blueprint §13.7a states the distinction: *"A
**shared mechanism** is a technical facility that six models may use without any of them
agreeing about meaning. A **shared semantic** is a claim about what a Record *is*, and it binds
every model that carries it. **The Record System shares mechanisms. It does not share
semantics.**"*

The mechanism layer is deliberately thin. Blueprint §13.7 states why the bootstrap layer is
small: *"a bootstrap that could express the whole model would be the model."* The universal
envelope is *"the bootstrap set and no more"* (RMS §4), and Artifact 033 states it.

## 4. The Six Sovereign Record Models

Six models, each answering a distinct class of question. RMS §6 states the questions, and they
are the reason the models remain separate:

| Model | The question it alone answers |
|---|---|
| **W** World | What is true of the world? |
| **E** Epistemic | Who knows, believes, suspects, or has been shown what? |
| **P** Production | What is intended, planned, coordinated, and in production? |
| **R** Registry | What does the system mean, and how are Record semantics defined? |
| **V** Visual | How is World Truth visually specified and represented? |
| **I** Issue | What was published, and how is that publication composed? |

**This is semantic ownership, not categorization** (RMS §6). Blueprint §13 states the same in
the negative: the six models are *"sovereign, not six configurations of one model"*.

**The set is exactly six. There is no seventh Record Model.** RMS §25's missing-model audit
classified every candidate — Context, Context Builder, Workflow Composer, Reader State, Policy,
Simulation definition, Simulation state, Memory, Lineage, Manifestation, Governance, Session,
Decision, Analytics — into the existing six, into a primitive, or into a projection, and
concluded that no seventh is required.

**These are not additional Record Models**, and none of them may be treated as one:

| Not a Record Model | Where it belongs | Source |
|---|---|---|
| Universal mechanisms | The mechanism layer of §3 | RMS §3, §4 |
| Registry definitions | Records of the **R** model | RMS §6.1, I-105 |
| Relationship Record | A World Record Model concept, not a Record System primitive | I-102, Blueprint §13.9 |
| History Record | A World Record Model concept, not a Record System primitive | I-102, Blueprint §13.9 |
| Projections | Derived, rebuildable output; never authoritative | RMS §6.1 |
| Primitives / capabilities | System capabilities that operate on Records | RMS §6.1 |
| Bootstrap Meta-Contract | Constitutional, and not a Record at all | RMS §10.4, §8 below |

A seventh Record Model is an architectural change at source. It is not something an
implementation, a downstream artifact, or a session may introduce.

## 5. Semantic Sovereignty

Each Record Model is sovereign over its own semantic domain.

- Each is **partition-owned** — one partition, one sovereign Record Model (I-16, I-101).
- Each **answers a distinct class of question** (RMS §6, §4 above).
- Each **owns its own semantics**. RMS §6: a Record Model owns *"its Kind taxonomy, identity
  semantics, state and lifecycle, relationship packaging, temporal architecture, provenance
  meaning, canonicality meaning (if any), semantic validation, and package composition."*
- **No model is a superclass of another** (RMS §2, I-101).
- **World is not a template** (RMS §2). RMS §30 states the consequence: *"Nothing inherits from
  World."*

That is the constitutional principle and the whole of what 039 establishes about it. **Artifact
041** is the six-model sovereignty contract; it states the detailed rules, and this document
does not anticipate them. Detailed inheritance rules, cross-model dependency rules, the
publishing firewall, manifestation-blindness, relationship legality, and per-model ownership
matrices are **not** stated here — each belongs to the artifact named in §11.

## 6. Shared Mechanisms

Common mechanisms remain common. RMS §3 and §4 name them:

identity minting, parsing and resolution · Record addressing · serialization envelope ·
structural validation · reference resolution · provenance **capture** · the Mutation
Coordinator · source-of-truth classification · indexing · storage and migration contracts.

Each is a facility. None of them is a claim about what a Record means.

> **Governing rule** `SOURCE-ESTABLISHED` (Blueprint §13.7a, I-103) —
> *a mechanism may be shared; a semantic may not be shared without evidence in each model that
> carries it.*

**Sharing an implementation mechanism does not merge semantic ownership.** RMS §4 states the
split for each mechanism, and the pattern is constant: structural validation is universal while
**semantic validation is model-owned**; provenance *capture* is universal while provenance
*meaning* is model-owned; reference *resolution* is mechanical while reference *legality* is
model- or Registry-owned; storage contracts are universal while storage *shape* is model-owned
within them.

Blueprint §13.7a states the test to apply whenever something new is proposed for sharing:
*"Is this a facility, or a claim? A facility may be shared on convenience. A claim must be
proven in each model that carries it, and a claim proven in one model and asserted in six is the
exact error v0.7.0 exists to retire."*

This section names the mechanisms. It defines no API, no class, no schema, and no storage
layout. **Artifact 043** owns the mechanism/semantics boundary as a binding contract.

## 7. Record, Record Model, and Canon

Four words, kept apart. Blueprint §13.0 states them, *"because every error this revision exists
to prevent is a collapse of two of these four words into one."*

| Term | What it is | What it is not |
|---|---|---|
| **Record** | A persistent semantic unit owned by exactly one Record Model | Not a synonym for canon; not inherently canonical |
| **Record Model** | The partition-owned semantic model that owns Records, their kinds, identity, relationships, temporality, and validation | Not a schema; not a specialization of a universal model |
| **Canon** | A governance and truth concept: the committed record, and the authority that commits it | Not a data class; not the noun for the object |
| **Canonicality** | A status property whose meaning is defined by each Record Model that has one | Not a universal boolean; not a property every Record carries |

**`Record` is architectural. `Canon` is governance** (Blueprint §13.0, I-104).

Three statements this constitution never makes: *every Record is Canon* · *every Record is
canonical* · *Canon = Record*. The vocabulary must be able to refuse all three, which is what
keeping the four words apart is for.

**Canonicality is model-defined** (Blueprint §13.7c, I-104). What canonical *means* in each
model, and which models have the property at all, is **Artifact 052**. Authority is **Artifact
051**. Neither framework is stated here, and no part of either is anticipated here; only the
separation that keeps them statable.

## 8. Bootstrap Meta-Contract

**The Bootstrap Meta-Contract is constitutional, and it is NOT a Record.**

RMS §10.4 closes this `AUTHOR-DECIDED` (FG-V7-05): *"**The Bootstrap Meta-Contract is NOT a
Record.** It is a **constitutional bootstrap contract standing outside the ordinary Registry
Record ontology**"*, containing only the six bootstrap elements Artifact 031 states. RMS §3
places it inside the constitution and outside the models, and RMS §30 describes the
architecture as follows: *"A thin universal mechanism layer beneath six sovereign
models, with a constitutional bootstrap contract that is not itself a Record."*

It exists to establish the initial conditions of the Record System before ordinary Registry
semantics exist. Blueprint §13.7 states its content and its deliberate smallness: it defines
*"only what a record must have in order to be a record at all"*, and is *"sufficient to create
the first Registry entry and the first Record, and it is not sufficient for anything more"*.

**Artifact 031** is the specification. No Record type is created for it: there is no Axiom
Record, no Constitution Record, and no seventh model holding the constitution.

## 9. What the Record System Explicitly Does Not Have

The Record System does not collapse the six models into a universal semantic object
architecture. RMS §4 freezes the point as **nine prohibitions**:

no Universal Record Base · no Universal Relationship Record · no Universal History Record ·
no universal lifecycle · no universal canonicality · no universal Kind taxonomy · no universal
identity *composition* · no universal state model · no universal semantic schema.

Blueprint §13 states the same in one sentence: *"The Record System is not the Record Model
Schema under a new noun."*

Two boundaries around this section, both deliberate:

- **The identity grammar is the one deliberate exception, and it is a grammar, not a
  semantics.** Blueprint §13.7a (AD-1, resolved): the grammar
  `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` *"is constitutional and universal across all six
  Record Models"*, while the semantic interpretation of what it names remains model-owned. RMS
  §5 states the same boundary: *"UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL."* This
  is why the frozen prohibition reads *identity composition* and not *identity grammar*.
  Blueprint §13's preamble list still reads *identity grammar*; §13.7a and RMS §§4–5 govern.
- **This section is a constitutional summary, not the binding test.** **Artifact 043** makes the
  nine prohibitions verbatim and testable, and owns the firewall against the retired
  architecture. Nothing here narrows, widens, or pre-empts it.

## 10. The Canon Object Model Is Retired

**The Canon Object Model is retired. The Record System governs in its place.**

RMS §2 states it without qualification — the retired model is *"fully superseded and retired as
current architecture"* and *"The **Record System** governs."* Blueprint §13 records what was
retired and why: v0.6.1's claim that *"every record coolboy12 holds is a Canon Object"*
asserted that *"a registry definition, a published page, a belief, and a character are the
same kind of thing, differing by a `kind` field. **They are not.**"*

The two architectures do not coexist, and four readings are prohibited. The Record System
must not be treated as a renamed Canon Object Model. It must not be treated as COM v2.
It must not be treated as an extension of COM. And COM must not be revived as a universal
base underneath the Record System. Blueprint §13 states the retirement in the form that
matters: *"six models, one set of shared mechanisms, and no universal object."*

**Historical terminology remains historical.** RMS §2: *"CO/COR/COH are historical terms only."*
Historical source text that uses them describes the retired architecture and is preserved as
such. It is never read as current architecture, and it is never rewritten to remove
the terminology.

What the supersession did **not** do, stated at Blueprint §13 so that it is not overread: it did
not redesign World, did not invent schemas for the five other models, and did not resolve what
earlier versions marked OPEN. *"The supersession is architectural; the migration is not
performed here."*

## 11. Downstream Boundary Documents

This constitution is the starting point for the P2 kernel contracts. Each owns a boundary named
above and specified there. **None of them is duplicated here**, and this document does not
anticipate their content.

| Artifact | Boundary it owns |
|---|---|
| 040 | six Model Definition stubs |
| 041 | six-model sovereignty contract |
| 042 | Record Model definition |
| 043 | mechanism vs semantics boundary — the nine prohibitions, verbatim and binding |
| 044 | seven architectural categories |
| 045 | partition ownership |
| 046 | identity semantics boundary |
| 047 | provenance capture mechanism |
| 048 | provenance meaning boundary |
| 049 | provenance/audit/history/revision/version/lineage separation |
| 050 | source-of-truth classification mechanism |
| 051 | authority framework |
| 052 | canonicality framework |
| 053 | derived-state discipline |
| 054 | temporal obligation specification |
| 055 | relationship boundary specification |
| 056 | package boundary specification |
| 057 | Kind admission test |
| 058 | cross-model dependency rules |
| 059 | P2 kernel conformance suite |

The bootstrap layer beneath this constitution is already stated: **031** the Bootstrap
Meta-Contract, **033** the universal envelope, **034** the identity grammar. This document
restates none of them.

## 12. Constitutional Summary

```
                    RECORD SYSTEM — the governing architecture
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
  constitutional            thin universal              six sovereign
  bootstrap contract        mechanism layer             Record Models
  (NOT a Record)            (shared facilities)         W · E · P · R · V · I
        │                           │                           │
        └───────────────────────────┴───────────────────────────┘
                                    │
                    no universal semantic object model
```

The Record System governs. Six sovereign Record Models — **W** · **E** · **P** · **R** · **V** ·
**I** — each answer a distinct class of question and own their own semantics. Mechanisms are
shared; semantics are not shared without evidence in each model that carries them. The Bootstrap
Meta-Contract is constitutional and is not a Record. There is no universal Record base, no
universal relationship, history, lifecycle, canonicality, Kind taxonomy, identity composition,
state model, or semantic schema. The Canon Object Model is retired, and CO/COR/COH are historical
terms only. **No model is a superclass of another. World is not a template. Nothing
inherits from World. There is no seventh Record Model.**

---

*Artifact 039 · P2/2a · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states architecture established by the Master Blueprint §13 and the Record Model System
§§2–6, 25, 30. It is not a Record, holds no canonical data, and creates no architecture of its
own.*
