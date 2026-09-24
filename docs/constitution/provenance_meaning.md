# COOLBOY12 — Provenance Meaning Boundary

**Artifact 048** · provenance meaning boundary · `docs/constitution/provenance_meaning.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P2/2b · Req: BR-21 · BP: §13.7b · RMS: §18 ·
H: 047 · S: — · LS: — · G: — · → models ·
Val: capture shared, meaning model-owned ·
Done: boundary · Why: prevents a universal provenance schema · Risk: medium · ∥: yes

## 1. Purpose

Row 048 states this artifact's reason in six words: **prevents a universal provenance schema.**

Provenance capture is one of the mechanisms the Record System legitimately shares across all six
Record Models. Sharing a mechanism is the exact condition under which a shared *meaning* gets
assumed — the failure Blueprint §13.7a exists to retire. This document is the provenance-specific
application of that firewall.

Two artifacts, two questions:

| Artifact | Question |
|---|---|
| **047** | How does the system **capture** provenance? |
| **048** | Who decides what captured provenance **means**? |

The answer to the second is: **the Record Model that owns the Record.**

This document adds no architecture. Every rule below is a contractual formulation of what
Blueprint §13.7a, Blueprint §13.7b, RMS §4, RMS §6, RMS §18 and I-103 already establish.

## 2. Constitutional Status

This document is AUTHORITATIVE about **the boundary between shared provenance capture and
model-owned provenance meaning**, and about nothing else. It **derives** that boundary from the
Master Blueprint and the Record Model System; it does not amend, supersede, or outrank either.

Where this document and the Master Blueprint, the Record Model System, or the OS File Build
Roadmap differ, **they are right and this document is wrong.**

It is not a Record, holds no canonical data, and is `Canon: n/a`. `SoT: AUTHORITATIVE` here means
authoritative **about architecture**, never World Canon (Blueprint §13.0, I-104).

## 3. Scope

**In scope.** That provenance capture is shared infrastructure; that provenance meaning is not;
which authority owns the semantic interpretation of a captured provenance value; and the boundary
at which every remaining provenance question passes to the owning Record Model.

**Out of scope.** The capture mechanism itself (**047**), the separation of the six temporal terms
(**049**), every model's own provenance semantics, and all matters listed in §14. This contract
says **who decides what provenance means**. It does not decide it.

## 4. The Governing Provenance Rule

> **Provenance capture is shared infrastructure. Provenance meaning is owned by the Record Model
> that carries the Record. A shared capture mechanism does not establish shared semantic
> interpretation.**

```
                            PROVENANCE
                                 │
                    ┌────────────┴────────────┐
                    │                         │
               UNIVERSAL                 MODEL-OWNED
                CAPTURE                    MEANING
                    │                         │
          who · when · why                    ├── W
                    │                         ├── E
        Artifact 047 · shared                 ├── P
        infrastructure (§13.7a, §13.7b)       ├── R
                                              ├── V
                                              └── I
```

The rule is stated in the sources twice, in both governing documents.

Blueprint §13.7a, in the shared-infrastructure table:

> | Provenance capture | Records who, when, why | What provenance *means* in a model (§13.7b) |

RMS §4, in the universal-architecture table:

> | Provenance **capture** | Spine 9 binds all six | Provenance **meaning** is model-owned (§13.7b) |

RMS §6 then names provenance meaning as one of the things a Record Model owns outright: a Record
Model *"owns: its Kind taxonomy, identity semantics, state and lifecycle, relationship packaging,
temporal architecture, **provenance meaning**, canonicality meaning (if any), semantic validation,
and package composition."*

**The two halves are read separately and never collapsed.** There is no third position between
them, and no reading in which the shared layer owns a portion of the meaning.

## 5. Capture Is Not Meaning

Blueprint §13.7a supplies the general form of the distinction, and Artifact 043 states it as the
system-wide firewall. Applied to provenance:

**Shared mechanism.** The system provides a common facility that records provenance values. Six
models may use it without any of them agreeing about meaning.

**Model-owned semantics.** The Record Model that owns the Record decides what that provenance
means within the domain of that Record.

**Constitutional consequence.** Using the same mechanism does not establish the same semantic
interpretation. I-103 states this without qualification: *"A mechanism may be shared across Record
Models; a semantic may not be shared without evidence in each model that carries it. Shared
infrastructure never confers shared meaning."*

Blueprint §13.7a supplies the test to apply whenever a future version proposes to share something
further: *"Is this a facility, or a claim? A facility may be shared on convenience. A claim must be
proven in each model that carries it, and a claim proven in one model and asserted in six is the
exact error v0.7.0 exists to retire."*

**Provenance capture is a facility. Provenance meaning is a claim.**

## 6. The Shared Capture Contract

What the universal layer legitimately provides, and no more.

The capture dimensions are source-fixed. Blueprint §13.7b states that provenance answers *"Who
made this, when, and **why**"*, held as *"an envelope property on the Record"*. RMS §18 lists the
same three. Artifact 033 §5.5 names `provenance` as one of the seven envelope fields. Artifact 047
implements the capture.

| | |
|---|---|
| **Dimensions** | `who` · `when` · `why` — the capture dimensions named by the governing sources |
| **Why universal** | Spine law 9 binds all six models (RMS §4) |
| **Shared facility** | provides the provenance capture mechanism established by Artifact 047 |
| **What the layer may not do** | decide what that value means inside any Record Model |

The shared layer is **model-agnostic**. It does not take a partition, a Kind, a Record or a Record
Model as input, and it therefore cannot branch on one. A mechanism that inspected the owning model
in order to interpret a provenance value would be deciding meaning, which is the one thing it may
not do.

This contract acknowledges the existence of the shared capture facility and states the boundary
around it. **It grants that facility nothing further** — no storage, persistence, serialization,
transport or indexing architecture is established, permitted or assigned here, and package
composition remains model-owned (§13.6d, I-107).

### 6.1 The three dimensions are captured terms, not a semantic vocabulary

`who`, `when` and `why` are the source terminology and are preserved exactly. They name **what is
captured**. They do not constitute a universal semantic vocabulary, and nothing below the shared
layer may treat them as one.

**On `why`.** The captured reason is text the caller supplies. This contract establishes **no**
universal causal meaning for it. `why` is not a causal graph, not a derivation edge, not a
universal event taxonomy, and not the History answer to *how this Record came to be what it is* —
Blueprint §13.7b assigns that question to history, whose packaging is model-owned (§13.6d, I-90).
What a recorded reason means inside a given Record Model is that model's to define.

**On `when`.** Blueprint §12.16 names Real-World Time as authoritative in provenance, and P-21
requires every temporal statement to name its axis. That is the whole of what this contract takes
from the temporal architecture. **048 creates no provenance clock and no provenance-specific
temporal system.** A model's temporal architecture is one of the things RMS §6 assigns to that
model, and capturing an instant does not give the shared layer any part of it.

**On `who`.** The captured value records provenance and is not renamed, re-typed or given a
constitutional synonym here. What the recorded `who` signifies inside a given Record Model — and
whether that model draws distinctions the shared layer cannot see — is model-owned.

### 6.2 047 is the mechanism, not a constitution

Artifact 047 is the capture mechanism this contract refers to. Its internal representation is an
implementation of capture and is **not** constitutionalized here.

Nothing in Artifact 047's current implementation — its class structure, field spellings, mapping
representation, serialization helpers, error codes, instant format, validation implementation, or
module layout — becomes a constitutional provenance schema by being referenced in this document.
No source establishes a universal provenance schema or wire format, and Artifact 047 says so
itself. A later authorial act may revise any of those without touching this boundary.

**This contract does not modify, re-specify, or duplicate Artifact 047.**

## 7. Model-Owned Provenance Meaning

The owning Record Model is the **semantic authority** for provenance on its own Records.

Within its own architecture, and subject to the Spine and the constitutional boundaries above it,
a Record Model establishes what the captured provenance means for the Records it owns — including
the semantic role provenance plays in that model, how it participates in that model's own
lifecycle, temporal architecture, authority and validation, and which of that model's actions and
decisions are provenance-bearing.

**This contract does not perform that work for any model, and does not constrain its outcome
beyond the constitutional rules the sources already state universally.**

Where a model has not yet done that work, the meaning is **open to that model**, not filled in by
default from another model, from the shared layer, or from this document. A composition declared
for a model that has not been independently designed is provisional and may not be implemented as
a requirement (I-107).

## 8. The Six Models

The rule binds all six sovereign Record Models identically:

| Code | Model |
|---|---|
| **W** | World |
| **E** | Epistemic |
| **P** | Production |
| **R** | Registry |
| **V** | Visual |
| **I** | Issue |

**All six may use the shared provenance capture mechanism.** Spine law 9 binds every model
(RMS §4), and capture is the facility by which the obligation is met.

**No model inherits provenance semantics from another.** I-101: *"No Record Model is a
specialization of another, and no Record Model is the template for another."*

**No model's interpretation of provenance becomes another model's semantics by way of the shared
mechanism.** Two Records may carry identically captured provenance and have nothing else in
common.

### 8.1 World is not the template

The World Record Model is the most mature of the six and the only one whose architecture the
Blueprint describes in full. **That maturity confers nothing.**

World's provenance semantics are World's. They are not the default, the baseline, the reference
implementation, or the starting point for E, P, R, V or I. A model defines its provenance semantics
within its own Record Model architecture, subject to the higher constitutional rules that already
bind it (§13.6d, I-101).

The Blueprint states the same caution about the packaging table at §13.6d: overlapping answers
record *"that six models were asked the same question and four gave overlapping answers"*, and
never that one model's answer governs the others.

## 9. What the Shared Layer May Not Decide

The shared capture layer may carry the provenance value. It **MUST NOT** become the semantic
authority for it. Specifically, the shared layer does not decide, for any Record Model:

1. **model-specific semantic meaning** — what provenance means for that model's Records;
2. **model-specific event or action classification** — which acts in that model are
   provenance-bearing;
3. **model-specific lifecycle semantics** — how provenance participates in that model's lifecycle;
4. **model-specific temporal or history packaging** — model-owned (§13.6d, I-90, I-102);
5. **model-specific authority meaning** — what provenance establishes about authority there;
6. **model-specific canonicality implications** — canonicality is model-defined (§13.7c, I-104);
7. **model-specific causal or derivational interpretation** — what a recorded reason implies;
8. **model-specific schema composition** — package composition is model-owned (§13.6d, I-107);
9. **model-specific Record semantics** — what the Record itself is in that model.

These are boundary examples drawn from what the sources already assign to the models. They are
**not** a design of any model, and they are **not** an exhaustive list of what a model owns —
RMS §6 is.

## 10. Provenance Is Not a Universal Schema

The central anti-universalization rule of this artifact, stated explicitly so that *"provenance is
shared"* can never be read as *"provenance semantics are shared."*

**This contract does not define, and may not be cited as having defined:**

| | |
|---|---|
| 1 | a universal provenance object schema |
| 2 | a universal Record Model provenance schema |
| 3 | a universal provenance database, table, or persistence model |
| 4 | a universal set of provenance fields beyond the source-established capture dimensions |
| 5 | a universal provenance lifecycle |
| 6 | a universal provenance state machine |
| 7 | a universal provenance ontology |
| 8 | a universal provenance event taxonomy |
| 9 | a universal provenance relationship graph |
| 10 | a universal provenance wire format, JSON or YAML |
| 11 | a universal interpretation of any captured text |
| 12 | a universal model-specific metadata package |

RMS §4's nine prohibitions `FROZEN` close the same door from the other side, ending with **no
universal semantic schema**. Artifact 043 carries those nine verbatim; this document does not
restate them and does not weaken them.

## 11. Worked Examples

**These examples are illustrative and non-normative.** They demonstrate the boundary. They
prescribe no schema, design no model, and define no field. Where an example names a model, it
states only that the model decides — never what it decides.

### Example A — World

A World Record is changed through the governed path and carries provenance.

The shared mechanism captures `who`, `when` and `why`. **The World Record Model decides what that
provenance means within World semantics.** The capture mechanism decides none of it, and this
contract states none of it: World's provenance meaning is World's own artifact to author.

### Example B — Epistemic

An Epistemic Record also carries provenance, captured by the same universal facility.

**E owns the meaning of that provenance in the epistemic context.** The E interpretation is not
inherited from W, is not derived from W, and does not require W's agreement. That both Records
went through the same capture call establishes nothing about how the two models read the result.

### Example C — Production

A Production Record carries provenance, captured by the same facility again.

**Production owns the meaning of that provenance in Production State.** Production State is
explicitly not canon about the world; identical capture does not make a Production Record
semantically comparable to a World Record. Same mechanism, two models, two questions, two owners.

### Example D — Registry, Visual, Issue

R, V and I follow the same boundary without variation. Each may use the shared capture mechanism;
each owns the meaning of the result for its own Records; none inherits that meaning from another
model or receives it from the shared layer.

**No fields, no attributes and no schemas for these three are stated here**, and their absence
from this document is not a finding about them. It is the boundary working.

### What every example shows

```
same capture mechanism  →  different model-owned semantic interpretation
```

## 12. Boundary With Neighbouring Concerns

Blueprint §13.7b and RMS §18 separate provenance from neighbouring concerns; they *"are not
interchangeable."*

Two consequences bind here, and only two:

1. **Provenance is not a universal substitute for any of them.**
2. **The presence of provenance does not create, define, or replace any such concern.**

**Artifact 049 owns the vocabulary separation among those terms. This document does not perform
that work**, defines none of them, and must not be read as a substitute for it.

## 13. Dependencies and Position

```
033  the envelope names `provenance` as one of seven fields
  ↓
047  capture who / when / why                    — the mechanism
  ↓
048  what provenance MEANS is model-owned        — this contract
  ↓
     each Record Model defines its own provenance semantics
```

| Relation | Artifact | What it owns that this does not |
|---|---|---|
| **H: 047** | provenance capture mechanism | the capture implementation |
| upstream | **033** universal Record envelope | the `provenance` field's place in the envelope |
| upstream | **043** mechanism vs semantics | the system-wide firewall and its nine prohibitions |
| downstream | **049** temporal terms | the six-term vocabulary separation |
| consumers | the six Record Models | their own provenance semantics |

Each Record Model establishes the meaning of provenance for its own Records (RMS §6). This
document names no artifact by which any model must do so.

## 14. Non-Goals — What This Contract Does Not Define

This contract defines the provenance meaning boundary. It defines **none** of the following, and
no reader may cite it as having done so:

1. the provenance capture mechanism — **Artifact 047**
2. the `provenance` envelope field and the seven-field envelope — **Artifact 033**
3. the six-term vocabulary separation — **Artifact 049**
4. any model's own provenance semantics — each Record Model's own work, RMS §6
5. any universal provenance schema, ontology, or semantic model — **PROHIBITED**, RMS §4
6. any Universal Record Base — **PROHIBITED**, RMS §4
7. universal lifecycle semantics — **PROHIBITED**, RMS §4
8. universal canonicality semantics — canonicality is model-defined, I-104, §13.7c
9. universal authority semantics — authority is domain-scoped, RMS §17
10. a universal temporal mechanism — temporal architecture is model-owned, §13.6d, I-90
11. universal history, revision, or version packaging — model-owned, §13.6d, I-90
12. universal relationship packaging — I-102
13. the temporal axes — Blueprint §12.16
14. audit semantics, approval mode, or session — **audit, not provenance**, §13.7b, I-14
15. executable validators, linters, or conformance suites
16. storage architecture, persistence, database keys, or indexes
17. serialization format, transport representation, or storage implementation
18. runtime implementation of any kind
19. any reintroduction of the retired Canon Object Model — retired at RMS §2

**None of these exclusions weakens the universal rules in §4 and §6.** Spine law 9 and the
capture obligation are constitutional and bind every model; excluding a *semantic* from this
contract never excludes a *constitutional rule* that the sources state universally.

## 15. Prohibited Architectural Moves

Stated as prohibitions because a list of permissions would be read as exhaustive.

| | Move | Why prohibited |
|---|---|---|
| **A** | **Universal provenance semantics** — treating a shared capture mechanism as a universal provenance meaning | I-103; §13.7a |
| **B** | **Universal provenance schema** — imposing one provenance schema on all six models because capture is shared | RMS §4 nine prohibitions |
| **C** | **World-as-template** — making World provenance semantics the implicit template for E/P/R/V/I | I-101; §13.6d |
| **D** | **Kernel semantic authority** — the shared kernel becoming semantic authority for model-owned provenance | §13.7a; RMS §4 |
| **E** | **Model inheritance** — a Record Model inheriting provenance semantics from another model | I-101 |
| **F** | **Hidden semantic coupling** — a shared field name, class, serializer or helper silently defining cross-model meaning | I-103 |
| **G** | **Schema leakage** — this document defining fields or structures for downstream model schemas | RMS §6; §13.6d |
| **H** | **Neighbouring-concept collapse** — using provenance as a universal substitute for audit, history, revision, version or derivation | §13.7b; RMS §18 |
| **I** | **Universal lifecycle** — establishing one provenance lifecycle across all six models | RMS §4; §13.7a |
| **J** | **Universal authority or canonicality by provenance** — the existence of provenance itself determining canonicality or authority meaning in every model | I-104; §13.7c |

## 16. Capture vs Meaning — Ownership Table

The right-hand column is the **owner**. Appearance in the left column confers nothing in the right.

| Concern | Owner |
|---|---|
| Capturing `who` / `when` / `why` | Shared infrastructure — **Artifact 047** |
| Meaning of provenance inside a Record Model | **The owning Record Model** |
| Which of a model's actions are provenance-bearing | The owning Record Model |
| Model-specific semantic validation of provenance | The owning Record Model |
| Model-specific lifecycle | The owning Record Model |
| Model-specific temporal and history packaging | The owning Record Model |
| Model-specific authority interpretation | The owning Record Model |
| Model-specific canonicality interpretation | The owning Record Model, where it has one |
| The boundary between the two columns | **This contract** |

This contract owns the **boundary** and nothing in either column. It states no capture
implementation and no model semantics.

## 17. Conformance Conditions

Stated so they are checkable. This document implements no test and is `T: doc`.

No `048.x` constitutional invariant is minted: the sources supply I-103 for the mechanism/semantic
rule and I-101 for model sovereignty, and no source-backed invariant number exists for the
remaining conditions, which are therefore stated without one.

| ID | Condition | Basis |
|---|---|---|
| **C-01** | Provenance capture is shared infrastructure, available to all six Record Models. | Blueprint §13.7a; RMS §3, §4 |
| **C-02** | Provenance meaning is owned by the Record Model that carries the Record. | Blueprint §13.7a, §13.7b; RMS §4, §6 |
| **C-03** | A shared capture mechanism establishes no shared semantic interpretation. | I-103; Blueprint §13.7a |
| **C-04** | The rule applies identically to W, E, P, R, V and I. | I-101; RMS §6 |
| **C-05** | No Record Model is the template or semantic parent of another for provenance. | I-101; §13.6d |
| **C-06** | No universal provenance schema, ontology, lifecycle or wire format is defined here. | RMS §4 nine prohibitions; §10 |
| **C-07** | No universal causal meaning is assigned to `why`. | Blueprint §13.7b; §6.1 |
| **C-08** | No provenance-specific temporal system or clock is created. | Blueprint §12.16; RMS §6 |
| **C-09** | Artifact 047's implementation details are not constitutionalized by this document. | §6.2; Roadmap rows 047, 048 |
| **C-10** | This contract does not modify or re-specify Artifact 047. | Roadmap row 048 `H: 047` |
| **C-11** | This contract states no model-specific provenance semantics on behalf of any model. | RMS §6; §7, §11 |
| **C-12** | Provenance is not used as a substitute for a neighbouring concern. | Blueprint §13.7b; RMS §18 |
| **C-13** | The vocabulary separation among those terms is left to Artifact 049. | Roadmap row 049; §12 |
| **C-14** | This document contains no executable content and mints no Record. | Roadmap row 048 `T: doc`, `Canon: n/a` |

A construction satisfying all fourteen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 18. Source Traceability

| Rule | Source |
|---|---|
| Provenance capture is shared infrastructure | Blueprint §13.7a; RMS §3, §4 |
| What provenance *means* in a model is not decided by the shared layer | Blueprint §13.7a |
| Provenance answers who, when and why; it is an envelope property | Blueprint §13.7b; RMS §18 |
| Provenance **capture** is universal because Spine 9 binds all six | RMS §4; Blueprint §10 law 9 |
| Provenance **meaning** is model-owned | RMS §4; Blueprint §13.7b |
| A Record Model owns provenance meaning among its nine owned concerns | RMS §6 |
| A mechanism may be shared; a semantic may not, without evidence in each model | I-103; Blueprint §13.7a |
| The facility-or-claim test | Blueprint §13.7a |
| No Record Model is a specialization or template of another | I-101 |
| Record packaging and temporal architecture are model-owned | Blueprint §13.6d; I-90 |
| History packaging is model-owned; the History Record is World's mechanism | I-90; I-102; Blueprint §13.6d |
| Canonicality is model-defined | Blueprint §13.7c; I-104 |
| A composition declared for an undesigned model is provisional | I-107; Blueprint §13.6d |
| Real-World Time is authoritative in provenance; every temporal claim names its axis | Blueprint §12.16 |
| Approval mode and session are audit, not provenance | Blueprint §13.7b; I-14 |
| Six terms separated; unqualified *lineage* retired | Blueprint §13.7b; RMS §18 |
| No universal Record base, lifecycle, canonicality, Kind taxonomy, state model or semantic schema | RMS §4 nine prohibitions `FROZEN` |
| `provenance` is one of the seven envelope fields | Artifact 033 §5.5; RMS §4 |
| Record ≠ Canon; SoT class is not canonicality | Blueprint §13.0; I-104 |
| Hard dependency on 047; unlocks the models | Roadmap row 048 |
| The vocabulary separation is its own artifact | Roadmap row 049 |

`Req: BR-21` is preserved exactly as the Roadmap states it. The authoritative requirement register
is not present in this repository; the requirement text is therefore **not** reproduced here and
**MUST NOT** be inferred.

---

*Artifact 048 · P2/2b · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states a contract derived from Blueprint §13.7a and §13.7b, RMS §4, §6 and §18, and
invariants I-101 and I-103. It is not a Record, holds no canonical data, states no capture
mechanism, defines no provenance schema, and claims no provenance semantics for any Record Model.
Where it and the Master Blueprint, the Record Model System, or the OS File Build Roadmap differ,
they are right and this document is wrong.*
