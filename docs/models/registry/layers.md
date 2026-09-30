# COOLBOY12 — Registry Semantic-Layer Contract

**Artifact 062** · Registry semantic-layer contract · `docs/models/registry/layers.md` · Own: R ·
RM: R · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P3/3a · Req: BR-05 · BP: §9.4 · RMS: §10 · H: 061 · S: — · LS: — · G: — · → 063 ·
Val: five semantic layers; downward-only · Done: contract · Why: Blueprint's own Registry
layering · Risk: high · ∥: no

## 1. Purpose

This contract answers one question — **how is Registry meaning organized into semantic layers, and
in what direction may those layers depend on one another?**

Row 062 names its source: *"Blueprint's own Registry layering"*. That layering is Blueprint §9.4's
*semantic dependency contract*: *"five layers, with a rule for each about what may depend on
what"*, and *"The one rule the contract exists to enforce: dependency runs downward only."* §9.4
declares that architecture settled: *"the five layers, the downward-only rule, the
structure/vocabulary split, the resolver boundary — is settled and changes only by amendment."*

This contract states that layering exactly, fixes what "downward" means, and fixes what a layer
dependency does **not** mean: ownership, reference legality, cross-model legality, authority,
canonicality, source-of-truth class, or runtime order. It adds no layer, Kind, field or rule.

## 2. Scope

**In scope.** The five layers and the six rows that present them; their order; what each may depend
on and be depended on by; which dependencies are forbidden; the boundaries between layer
dependency and Record ownership, Record reference, cross-model legality, authority, canonicality,
source-of-truth class and runtime; the handoffs this implies.

**Out of scope, by owner.** Registry authority (061, frozen here as a constraint); the reference
boundary (063); the Kind roster and admission (064); governance (065); definition-family content
(066–107); evolution (108–110); dependency direction rules — *"downward-only; asymmetric; no
cycles"* (111); enforcement and implementation (112–117); cross-model edges (058). No schema, field,
Registry data, validator, algorithm or test is created.

`Own: R` · `SoT: AUTHORITATIVE` about the Registry layer architecture · `Canon: n/a`. This document
is not a Registry Record and holds no Registry data. Where it differs from the Master Blueprint, the
Record Model System, or the OS File Build Roadmap, **those sources are right and this document is
wrong.** `Req: BR-05` is reproduced from row 062; the requirement register is not in the supplied
source set, so the ID is carried forward unverified and no requirement text is stated for it
(GAP-C; Revolving Resolution Note).

## 3. Governing Sources and Dependencies

| Source | What it gives this contract |
|---|---|
| Blueprint §9.4 | the semantic dependency contract: the layer table, the downward-only rule, the frozen architecture, *"The Registry holds no instances"*, *"Reference resolution is not Registry work"* |
| Blueprint §13.6e | the rule restated for the Registry Record Model: *"Downward only, and the direction is asymmetric by design"*; the circularity Registry must not create |
| Blueprint §13.6d | the R package row reads a definition's relationships as *"its dependencies"*, governed by the downward-only rule — design input, not a freeze (Artifact 060 §12) |
| Blueprint §12.4; §29.6a | Derived output is never authoritative |
| RMS §10, §10.3 | Registry is sovereign; its reference boundary, which corrects *"may never reference a kind"* |
| RMS §4; I-103 | the nine prohibitions; shared mechanism is not shared meaning |
| Artifact 060 | what Registry is (H chain: 060 → 061 → 062) |
| Artifact 061 | the authority boundary (`H: 061`), frozen as a constraint on every rule below |
| Artifacts 045, 050, 052, 053, 055, 058 | partition ownership, SoT class, canonicality, derived state, the relationship boundary, cross-model edges |

§13.6e records why §9.4 is read this way: §9.4 *"specifies the Registry **layer** — its five
semantic layers and its downward-only dependency rule — and was written when Registry was
infrastructure."* The layer architecture stands; §9.4's *"Classification: capability"* does not
(RMS §10, COLLISION-1; Artifact 060 §16.1).

## 4. The Registry Semantic-Layer Model

### 4.1 The source table

Blueprint §9.4 presents the contract as one table. Its six rows, with their own column values:

| Row | Holds | Depends on | May be depended on by |
|---|---|---|---|
| **Shared field semantics (RFS)** | *"The base layer. Reusable field meaning across every kind: identity, naming, classification, temporal, provenance, status, metadata, references"* | *"Nothing"* | *"Everything below"* |
| **Peer semantic authorities** | *"Meaning that is shared but is **not** a field-definition module"*: relationship type and participant-role semantics, change and operation semantics, indicator semantics for world-state | *"RFS"* | *"Everything below"* |
| **Kind semantics** | *"What is true of every record of one kind"* | *"Registry"* | *"Subtypes, instances, projections"* |
| **Subtype semantics** | *"What is true of one specialization"* | *"Registry, its kind"* | *"Instances, projections"* |
| **Instance data** | *"One record's actual values"* | *"All three above"* | *"Projections"* |
| **Derived / projection** | *"Recomputed views"* | *"All four above"* | *"Nothing — non-authoritative (Section 12.4)"* |

### 4.2 Five layers, six rows

The prose says **five layers**; the table has **six rows**. This contract does not call all six rows
layers, and it does not drop one. The table's own counts decide the grouping:

1. **Instance data** depends on *"All three above"*, and **Derived / projection** on *"All four
   above"*. Four rows stand above Instance data, so *"three"* counts the first two rows as one.
   Five rows stand above Derived, so *"four"* counts them as one again.
2. **Kind semantics** depends on *"Registry"*, not on either of the first two rows by name, so the
   table names those two rows together as the layer a Kind depends on.
3. The second row is named **peer** semantic authorities: peers of the base, meaning *"shared but …
   not a field-definition module"*.

Read that way, every count in the table holds, and the five layers are:

| Layer | Rows | Name used here |
|---|---|---|
| **L1** | Shared field semantics (RFS); Peer semantic authorities | the Registry base |
| **L2** | Kind semantics | Kind semantics |
| **L3** | Subtype semantics | Subtype semantics |
| **L4** | Instance data | Instance data |
| **L5** | Derived / projection | Derived / projection |

**Within L1 the two rows are ordered.** Peer semantic authorities depend on RFS; RFS depends on
nothing. The grouping changes no dependency the table states. The labels L1–L5 are this document's
presentation and carry no meaning beyond the table's.

**Reading, and its standing.** The source does not number its layers or say in words which rows
form which layer. The grouping above is the only one under which the table's own counts hold. The
alternative — five layers ending at Instance data, with Derived outside the contract — would make
Instance data's *"All three above"* wrong, and is not adopted. The reading is recorded here for
review (§14.2); it alters no dependency rule, because every rule below is taken from the table's
columns row by row.

### 4.3 Which layers hold Registry content

**L1–L3 are Registry definitions.** §9.4 lists what the Registry holds: *"kind definitions, subtype
definitions, relationship-type definitions with their participant roles and ownership rule (Section
13), shared field definitions, controlled value sets, change-and-operation semantics, and indicator
semantics for world-state."* They are Registry Records (RMS §10; I-105).

**L4 and L5 are not Registry content.** *"The Registry holds no instances"* (§9.4): L4 is held by
the Record Models whose Records use the definitions — W, E, P, V, I — and never by Registry
(RMS §10.3; I-105; Artifact 061 §7). L5 is Derived: recomputed and never authoritative (§12.4;
§29.6a; Artifact 053). They appear in the contract because they depend on the definitions, and the
rule of the contract binds that dependency (§7). Appearing in it makes neither of them Registry's.

## 5. Layer Ordering

```
L1  Registry base      RFS  ←  Peer semantic authorities
 ↓
L2  Kind semantics
 ↓
L3  Subtype semantics
 ↓
L4  Instance data                 held by the owning Record Model, never by Registry
 ↓
L5  Derived / projection          non-authoritative; nothing depends on it
```

**What "downward" means.** An arrow points from what is depended on to what depends on it.
Meaning is defined at L1 and specialized downward: *"adding, refining, or splitting a Registry
definition changes meaning for everything below it … and cannot invalidate anything above it"*
(§9.4). A layer depends only on layers above it. **Nothing depends on a layer below itself.**

## 6. Layer Responsibility Matrix

| Layer | Semantic responsibility | May depend on | Must not depend on | May be depended on by | Held by | Downstream content |
|---|---|---|---|---|---|---|
| **L1** RFS | reusable field meaning across every kind | nothing | any other row | everything below | Registry | field definitions: 072–073 |
| **L1** Peer semantic authorities | relationship type and participant-role semantics; change and operation semantics; indicator semantics | RFS | L2–L5 | everything below | Registry | relationship types 079–080; indicators 086–087 |
| **L2** Kind semantics | what is true of every Record of one kind | L1 | L3, L4, L5 | L3, L4, L5 | Registry | kind definitions 068–069; roster 064 |
| **L3** Subtype semantics | what is true of one specialization of a kind | L1; its own kind in L2 | L4, L5 | L4, L5 | Registry | subtype definitions 070–071 |
| **L4** Instance data | one Record's actual values | L1, L2, L3 | L5 | L5 | the owning Record Model — never Registry | each model's own specification |
| **L5** Derived / projection | recomputed views | L1–L4 | — | nothing | not authoritative; the derived layer | Artifact 053; P6/P8 derived layer |

**Cells the source does not fill are not filled here.** The table does not say whether a
definition may depend on another definition *in the same layer* (other than Peer on RFS), or whether
a Subtype may depend on a kind other than its own. RMS §10.3 allows *"R → R definitions"* in
general. Same-layer dependency and cycles are **not established here**; row 111 owns *"no cycles"*.

**Which Registry Kinds sit in which layer.** The L1–L3 rows name their own contents (§4.1, §4.3),
and the downstream columns above follow those names. RMS §10.1 freezes fourteen Registry Kinds; the
§9.4 rows do not place `MODEL-DEFINITION`, `SCHEMA-DEFINITION`, `CONTROLLED-VOCABULARY`,
`IDENTITY-GRAMMAR`, `VALIDATION-RULE`, `CONSTRAINT-DEFINITION`, `CAPABILITY-DEFINITION`,
`DERIVATION-RULE` or `SIMULATION-MODEL-DEFINITION`. Their layer placement is **not established
here** (§14.3).

## 7. Dependency Rules

| ID | Rule | Source |
|---|---|---|
| **D-1** | Semantic dependency runs downward only: a layer depends only on the layers its row lists, all of which are above it. | §9.4; §13.6e |
| **D-2** | RFS depends on nothing. | §9.4 |
| **D-3** | No definition in L1–L3 depends on L4: a Registry definition never depends on, or takes its meaning from, an instance. | §9.4; RMS §10.3 |
| **D-4** | Kind semantics (L2) never depends on an instance (L4): *"a kind may never reference an instance"*. | §9.4; I-75 |
| **D-5** | Nothing depends on L5. Derived output is never the source of meaning for anything. | §9.4; §12.4 |
| **D-6** | L4 depends on the definitions above it and never the reverse: *"The five other models depend on Registry **for definitions**; Registry depends on them **for nothing**."* | §13.6e; §9.4 |
| **D-7** | Registry must not require *"the complete semantic implementation of every other Record Model in order to define them"*. | §13.6e |

**D-1 to D-7 answer only what the table and §13.6e state.** Whether an L1 definition may
*reference* a declared Kind (L2) is the conflict of §14.1 and is not decided by them.

**What the rule is not.**

- **Not a runtime order.** The layers order meaning. They set no evaluation, loading, resolution or
  execution order: *"Reference resolution is not Registry work"* (§9.4), and resolution is a shared
  mechanism (RMS §4).
- **Not a cross-model rule.** D-6 states the only cross-model fact the contract carries — instances
  depend on definitions. It creates no edge between Record Models (§9).

## 8. Dependency vs Ownership

```
A depends semantically on B     ≠     A owns B
```

- A Subtype that depends on its Kind does not own the `KIND-DEFINITION`. Both remain Registry
  Records, owned by the Registry Record Model as its own Records (Artifact 061 §4).
- An instance in L4 depends on definitions in L1–L3. Registry thereby owns no L4 Record: *"Registry
  governs the definitions. Each Record Model owns its Records."* (§13.6e; I-105; 061 §4)
- The dependency transfers no W, E, P, V or I Record to Registry, and no R Record to any other model
  (I-16; Artifact 045 §9).

A definition's dependencies are not owned edges and are not Relationship Records: *"A registry
definition's connections are dependencies under a downward-only rule (Section 9.4), not owned
edges"* (§13.2). The Relationship Record remains a World Record Model concept (I-102; Artifact 055).
No Relationship Record, universal or Registry-owned, arises from a layer dependency.

## 9. Dependency vs Reference

```
semantic dependency    ≠    Record reference    ≠    cross-model reference legality
```

- **A dependency is not a reference field.** That a Kind depends on RFS establishes no field on any
  Record pointing at an RFS definition. Every Record carries `registry_ref` (RMS §4); what the field
  carries is Artifact 033's and the Registry's, and this contract adds no field to any Record.
- **A dependency is not reference legality.** What Registry may reference is Artifact 063's (row 063
  `Val`), enforced by 112.
- **A dependency is not a cross-model edge.** Instance data depending on definitions (D-6) does not
  establish W → R, E → R, P → R, V → R or I → R as a Record-level edge, and establishes no other
  edge. Cross-model edges are Artifact 058's, and this contract reinterprets none of 058's rows,
  conditions or unresolved items.

## 10. Registry vs Other Record Models

The layers are **Registry's architecture for its definitions**. They are not a semantic hierarchy of
the six Record Models:

- W, E, P, V and I do not organize their Records into these layers, and do not inherit them (I-101;
  RMS §2: *"No model is a superclass of another."*).
- L4 names where their Records stand *relative to* Registry definitions — as instances that depend
  on them — and nothing about how they are designed. Their Kinds, lifecycles, relationships,
  temporal accounts, canonicality and validation remain theirs (RMS §6; Artifact 061 §7).
- The layers are not a universal semantic model. The nine prohibitions of RMS §4 stand: no universal
  Record base, Relationship Record, History Record, lifecycle, canonicality, Kind taxonomy, identity
  composition, state model or semantic schema is created by them.

**No Record gains a field.** No *layer* field, no *status* field and no *schema* field is added to
any Record; the universal envelope stays *"the bootstrap set and no more"* (RMS §4).

**`status` in the RFS row.** RFS lists *status* among the reusable field meanings, and §9.4 says
that what `status` *"means everywhere it appears is Registry"*. RMS §4 closes that `status` is not a
universal envelope field and is World-owned, other models defining their own state vocabularies
(FG-V7-03); §13.7c makes the status vocabulary a Registry-owned controlled vocabulary that is
legitimately per-partition. Read together — a reading of the three statements, adding no rule —
RFS may hold the meaning of a status field **where such a field appears**. It does not make
`status` appear anywhere it does not, and it creates no universal lifecycle or state model.

**Identity in the RFS row.** RFS lists *identity* field meaning. The identity grammar is universal
and its semantics are model-owned (RMS §5: *"UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC
MODEL"*; Artifact 046). An identity field definition in L1 does not give Registry any Record's
identity semantics.

## 11. Authority, Canonicality and Source-of-Truth Class

Layer position is not a ranking of anything else:

| Layer order does not mean | Why | Source |
|---|---|---|
| a lower layer (nearer L1) is more authoritative | authority is domain-scoped; order measures dependency only | RMS §17; Artifact 051 §7 |
| a lower layer is more canonical, or closer to World Truth | Registry is canonical *"about meaning"*, never about the world | Blueprint §13.7c; I-88; Artifact 052 |
| a higher layer (nearer L5) is less authoritative | L2–L4 are not ranked by it | Artifact 061 §11 |
| a later layer is Derived | only L5 is Derived; L4 is the owning model's authoritative data | §9.4; §29.6a; Artifact 053 |
| an earlier layer is `AUTHORITATIVE` for that reason | source-of-truth class is set per data class | §29.6a; Artifact 050 |
| constitutional superiority | the Spine and the one Authority are untouched by it | Spine law 3; Artifact 051 §6 |

The one class the contract states is L5's: *"Nothing — non-authoritative"*.

## 12. Definition-Family Handoffs

| Layer | Family content, where the source names it | Owner |
|---|---|---|
| L1 RFS | shared field definitions | 072–073 |
| L1 Peer | relationship-type and participant-role definitions; indicator definitions; change-and-operation semantics | 079–080; 086–087; change-and-operation semantics — no family row names it (§14.3) |
| L2 | kind definitions | 068–069; the roster 064 |
| L3 | subtype definitions | 070–071 |
| — | controlled value sets (*"structure/vocabulary split"*) | 081–082 |
| — | the resolver boundary | the shared resolution mechanism; the Registry resolution service 115 |

This contract writes none of their schemas, fields, lifecycles or semantics.

## 13. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | Registry's layers are universal Record layers | they order Registry definitions; no model inherits them | I-101; RMS §2, §4 |
| 2 | A higher layer owns a lower layer, or the reverse | dependency is not ownership | §13.6e; I-105 |
| 3 | Semantic dependency transfers Record ownership | Records stay with their partition's model | I-16; 045 §9 |
| 4 | Semantic dependency permits a Record reference | references are 063's | row 063 |
| 5 | Semantic dependency permits a cross-model edge | edges are 058's | Artifact 058 |
| 6 | A layer nearer L1 is more authoritative or more canonical | order is dependency only | RMS §17; §13.7c |
| 7 | A layer nearer L5 is Derived | only L5 is Derived | §9.4; §29.6a |
| 8 | Every Record has a layer field | no field is added; the envelope is fixed | RMS §4 |
| 9 | Every Record has `status` | `status` is World-owned, not universal | RMS §4 (FG-V7-03) |
| 10 | Registry owns a model because it resolves against Registry | definitions are governed; Records are owned | I-105; 061 §4 |
| 11 | Registry defines a Kind, so owns its instances | L2 is held by Registry; L4 is not | §9.4; §13.6e |
| 12 | Registry defines relationship types, so owns relationship instances | definitions only; never runtime relationship ownership | RMS §15 |
| 13 | Registry defines validation rules, so executes all validation | runtime validators implement validation | RMS §10.6 |
| 14 | Registry owns a universal semantic schema | no universal semantic schema exists | RMS §4 |
| 15 | The layer order is an execution or resolution order | resolution is not Registry work | §9.4; RMS §4 |
| 16 | A definition's dependency is a Relationship Record | dependencies, not owned edges | §13.2; I-102 |

## 14. Unresolved and Deferred Matters

### 14.1 UNRESOLVED SOURCE CONFLICT — *"may never reference a kind"*

| | |
|---|---|
| **Source A** | Blueprint §9.4: *"A Registry definition may never reference a kind, a subtype, or an instance; a kind may never reference an instance."* Restated at §13.6e and as I-75. |
| **Source B** | RMS §10.3 (`FROZEN`): *"Registry MAY reference: other Registry definitions · declared Record Models · declared Kinds · declared schemas · declared semantic contracts"*; it states that v0.1 put the boundary *"too bluntly"*. |
| **The conflicting propositions** | Under A, an L1 definition may not reference a Kind (L2) or a Subtype (L3). Under B, a Registry definition may reference a declared Kind. |
| **Impact on 062** | Rows 062 and 111 both carry *"downward-only"*, and §9.4 states the rule partly in terms of *reference*. Whether an L1 definition naming a declared Kind is a forbidden upward dependency is not settled by any source. |
| **What 062 establishes safely** | Everything both sources agree on: the layer order (§5); the Depends-on columns (§6); D-2 to D-7; no dependency on, or authority taken from, an instance (A and B agree). |
| **What 062 leaves open** | Whether, and in what sense, a definition in L1 may reference or depend on a declared Kind or Subtype. |
| **Downstream owners** | Row 063 (reference boundary; its `Val` restates RMS §10.3) and row 111 (*"downward-only; asymmetric; no cycles"*). Artifacts 058 §11 and 060 §10 record the same condition. |

### 14.2 The five-layer grouping — for review

§4.2's grouping of RFS and the peer semantic authorities as one layer is read from the table's own
counts. No source states it in words. It changes no dependency rule, and every row keeps its own
columns. It is recorded for the author's confirmation.

### 14.3 Source gaps

- **Layer placement of Kinds the rows do not name** (§6). No source or Roadmap row places them. Row
  064 (the roster) and row 111 (direction) are the nearest owners; neither is assigned it here.
- **Change-and-operation semantics** (Peer row) corresponds to no RMS §10.1 Kind and no family row.
  Recorded; the roster is 064's.
- **Same-layer dependency and cycles** — not established by §9.4; row 111 owns *"no cycles"*.

## 15. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-062-01** | The contract has exactly five layers, presented in six source rows; L1 comprises RFS and the peer semantic authorities. | §9.4 |
| **C-062-02** | The order is L1 → L2 → L3 → L4 → L5, with Peer after RFS inside L1. | §9.4 |
| **C-062-03** | A layer depends only on the layers its row lists, all above it. | §9.4; §13.6e |
| **C-062-04** | No layer depends on a layer below it. | §9.4; I-75 |
| **C-062-05** | No Registry definition depends on, or takes its meaning from, a domain instance. | §9.4; RMS §10.3 |
| **C-062-06** | Nothing depends on L5. | §9.4; §12.4 |
| **C-062-07** | Semantic dependency transfers no Record ownership. | §13.6e; I-105; I-16 |
| **C-062-08** | Semantic dependency establishes no Record reference and no reference legality. | row 063 |
| **C-062-09** | Semantic dependency establishes no cross-model edge. | Artifact 058 |
| **C-062-10** | Layer position is not an authority ranking. | RMS §17; 051 |
| **C-062-11** | Layer position is not a canonicality ranking. | §13.7c; 052 |
| **C-062-12** | Layer position is not a source-of-truth class; only L5 is stated non-authoritative. | §29.6a; 050; 053 |
| **C-062-13** | The layers do not apply as a semantic architecture to W, E, P, V or I. | I-101; RMS §2 |
| **C-062-14** | No field — layer, `status`, schema or other — is added to any Record. | RMS §4 |
| **C-062-15** | `status` is not made universal. | RMS §4 (FG-V7-03) |
| **C-062-16** | L1–L3 are Registry definitions; Registry holds no L4 instance. | §9.4; RMS §10; I-105 |
| **C-062-17** | W, E, P, V and I retain their Records. | §13.6e; I-105 |
| **C-062-18** | No Relationship Record arises from a layer dependency. | §13.2; I-102 |
| **C-062-19** | Runtime validation and resolution stay outside the layers. | §9.4; RMS §4, §10.6 |
| **C-062-20** | The Kind roster and Kind layer placement are not decided here (064). | row 064 |
| **C-062-21** | Governance is not decided here (065). | row 065 |
| **C-062-22** | The reference boundary is not decided here (063). | row 063 |
| **C-062-23** | Dependency direction rules, cycles and asymmetry rules are not decided here (111). | row 111 |
| **C-062-24** | The conflict of §14.1 remains recorded and unresolved. | §9.4; RMS §10.3 |
| **C-062-25** | Frozen P0, P1 and P2 architecture is unchanged, and their suites stay green. | Artifact 004; rows 030, 038, 059 |

## 16. Downstream Handoff

| Artifact | May assume from 062 | Must still define |
|---|---|---|
| **063** reference boundary | the layer order; no definition depends on or takes meaning from an instance; dependency ≠ reference | what R may and may not reference; the §14.1 conflict as a reference question |
| **064** Kind taxonomy | the layers; which contents the §9.4 rows name | the fourteen Kinds, their admission rationale, and any layer placement the rows do not give |
| **065** governance | that layers carry no authority ranking | who may propose, approve, deprecate |
| **111** dependency direction | downward-only (D-1–D-7); the §14.1 conflict | asymmetry and no-cycle rules; same-layer dependency; the §14.1 conflict as a dependency question |
| **112–117** | the contract they enforce and implement | validation, binding, resolution, kernel |

## 17. Roadmap Completion Trace

| Row 062 | Where it is met |
|---|---|
| `Val`: *"five semantic layers"* | §4 (five layers, six rows); C-062-01, C-062-02 |
| `Val`: *"downward-only"* | §5, §7; C-062-03 to C-062-06; §14.1 for the part the sources leave open |
| `Done`: *"contract"* | §6–§13; C-062-01 to C-062-25 |
| `Why`: *"Blueprint's own Registry layering"* | §3, §4.1 — the layers are §9.4's |
| `H: 061` | §8, §11, §13 — every rule respects the authority boundary |
| `→ 063` | §9, §14.1, §16 |

---

*Artifact 062 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This contract
states the Registry semantic layers and their downward-only dependency, derived from Master
Blueprint §9.4 and §13.6e and the Record Model System §10. It is not a Registry Record, holds no
canonical data, defines no schema, field, validator or algorithm, and implements nothing. Where it
differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those
governing sources are correct and this document is wrong.*
