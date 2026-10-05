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
boundary and exact reference legality (063); the Kind roster and admission (064); governance (065);
definition-family content (066–107); evolution (108–110); detailed definition-dependency rules —
same-layer dependency, asymmetry, cycle prohibition and concrete dependency-graph constraints
(111, whose `Val` is *"downward-only; asymmetric; no cycles"*), which apply the layer direction
settled here and do not reopen it; enforcement and implementation (112–117); cross-model edges
(058). No schema, field, Registry data, validator, algorithm or test is created.

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

Read that way, every count in the table holds. **The five conceptual layers of this contract
are:**

| Layer | Source rows | Name used here |
|---|---|---|
| **L1** | 1a Shared field semantics (RFS) · 1b Peer semantic authorities | Registry semantic layer |
| **L2** | Kind semantics | Kind semantics |
| **L3** | Subtype semantics | Subtype semantics |
| **L4** | Instance data | Instance data |
| **L5** | Derived / projection | Derived / projection |

**Source presentation note — five layers, six table rows.**

- *Blueprint fact.* §9.4 calls the contract *"five layers"*, and renders it as six table rows.
- *Contract normalization.* This contract groups RFS and the peer semantic authorities as two
  internal strata, 1a and 1b, of one conceptual layer, L1. It does so to keep both the stated
  five-layer count and every table row. The Blueprint does not use the word *strata* or number its
  layers; the grouping is this contract's source-consistent normalization, derived from the
  explicit five-layer count and from the table's own arithmetic: Kind semantics depends on
  *"Registry"*, Instance data on *"All three above"*, and Derived / projection on *"All four
  above"*. It is not a new semantic rule.
- *No row-level dependency is altered.* Within L1, Peer semantic authorities depend on RFS, and
  RFS depends on nothing. Every rule below is taken from the table's columns row by row.
- *The alternative is excluded.* Five layers ending at Instance data, with Derived outside the
  contract, would make Instance data's *"All three above"* false.

**The five-layer grouping is normative.** C-062-01 and C-062-02 bind it. The labels L1–L5, 1a and
1b are this document's presentation and carry no meaning beyond the table's.

### 4.3 Which layers hold Registry content

**L1–L3 are the definition-bearing portion of the contract.** §9.4 lists what the Registry holds:
*"kind definitions, subtype definitions, relationship-type definitions with their participant roles
and ownership rule (Section 13), shared field definitions, controlled value sets,
change-and-operation semantics, and indicator semantics for world-state."* Where the current
Registry taxonomy provides an admitted Registry Kind, the governed definitions represented in L1–L3
are Registry Records (RMS §10, §10.1; I-105). This contract infers no new Registry Kind or
definition family for semantic material the current taxonomy does not map. In particular, §9.4
names change-and-operation semantics within the peer semantic authorities, but neither RMS §10.1
nor the current Roadmap establishes a dedicated Registry Kind or definition-family mapping for it:
that mapping is not established by current sources (§14.2).

- **L1** is Registry's own definition domain: shared field meaning and the peer semantic
  authorities.
- **L2 — Kind semantics.** At the Registry-definition boundary, L2 is represented by the governed
  `KIND-DEFINITION` that specifies what a Kind means. Registry governs that definition. The owning
  Record Model governs the Kind in its domain: its Kind taxonomy, the Kind's domain semantics, which
  Records of it exist, and what they mean (§13.6e; RMS §6; I-106; Artifact 061 §7).
- **L3 — Subtype semantics.** Registry holds the governed `SUBTYPE-DEFINITION` where one applies.
  The owning Record Model keeps the domain semantics of its Records that use the subtype.

Holding a `KIND-DEFINITION` or `SUBTYPE-DEFINITION` transfers none of the owning model's Kind or
subtype domain semantics, taxonomy, admission, instances, lifecycle, authority, canonicality or
package architecture to Registry (Artifact 061 §4, §7; Artifact 057 §9).

**L4 — ownership follows the Record.** L4 denotes one Record's actual values (*"One record's actual
values"*). Ownership at L4 stays with the Record Model that owns that Record (I-16; Artifact 045).
A W, E, P, V or I Record that resolves against Registry definitions gives Registry no ownership of
it (RMS §10.3; I-105; Artifact 061 §7). Registry's own definition Records are Records and
remain R-owned (RMS §10; Artifacts 060, 061). §9.4's *"The Registry holds no instances"* predates
Registry's promotion to a Record Model (§13.6e). This contract reads it, as RMS §10.3 bounds it, to
mean that Registry holds none of the domain instances its definitions describe — Registry defines
`CHARACTER` and never holds a World Character. It is not read to deny that Registry has Records of
its own, and this contract does not decide whether or how Registry's own Records occupy L4.

**L5 — not Registry definition content.** Derived / projection is recomputed and never authoritative
(§12.4; §29.6a; Artifact 053). It is not Registry definition content merely because it depends on
Registry semantics.

L4 and L5 appear in the contract because they depend on the definitions, and the rule of the
contract binds that dependency (§7). Semantic dependency transfers no Record ownership to
Registry.

## 5. Layer Ordering

**Notation.** *A* DEPENDS-ON *B* means that *A* takes semantic meaning or constraint from *B*. In
the diagram below, the vertical ↓ reads *governs and constrains*: each layer shown above constrains
the layers below it. No arrow in this document states a layer dependency: `→` appears only in
Roadmap metadata, the artifact chain, a quotation, and cross-model edge notation (Artifact 058).

```
L1  Registry semantic layer
      1a  Shared field semantics (RFS)     DEPENDS-ON  nothing
      1b  Peer semantic authorities        DEPENDS-ON  RFS
 ↓
L2  Kind semantics                         DEPENDS-ON  L1 (the source: "Registry")
 ↓
L3  Subtype semantics                      DEPENDS-ON  L1; its own kind in L2
 ↓
L4  Instance data                          DEPENDS-ON  L1, L2, L3 (the source: "All three above")
                                           owned by the Record Model that owns the Record
 ↓
L5  Derived / projection                   DEPENDS-ON  L1–L4 (the source: "All four above")
                                           non-authoritative; nothing DEPENDS-ON L5
```

**What "downward-only" means.** Meaning is defined at L1 and specialized downward: *"adding,
refining, or splitting a Registry definition changes meaning for everything below it … and cannot
invalidate anything above it"* (§9.4). A layer may consume semantics from the lower-numbered
layers that its source row lists — not only from the one immediately before it; a layer nearer L5
DEPENDS-ON applicable layers nearer L1. **No layer takes defining semantic authority from a
higher-numbered layer.**

## 6. Layer Responsibility Matrix

| Layer | Semantic responsibility | May depend on | Must not depend on | May be depended on by | Registry definition responsibility | Domain ownership | Downstream content |
|---|---|---|---|---|---|---|---|
| **L1** 1a RFS | reusable field meaning across every kind | nothing | any other row | everything below | shared field definitions | Registry definition domain | field definitions: 072–073 |
| **L1** 1b Peer semantic authorities | relationship type and participant-role semantics; change and operation semantics; indicator semantics | RFS | L2–L5 | everything below | relationship-type and indicator definitions; change-and-operation semantics — Registry Kind/family mapping not established | Registry definition domain; relationship instances and indicator values stay with their owning model (RMS §15, §10.7) | relationship types 079–080; indicators 086–087 |
| **L2** Kind semantics | what is true of every Record of one kind | L1 | L3, L4, L5 | L3, L4, L5 | the governed `KIND-DEFINITION` | the owning Record Model: its Kind taxonomy, the Kind's domain semantics, its instances | kind definitions 068–069; roster 064 |
| **L3** Subtype semantics | what is true of one specialization of a kind | L1; its own kind in L2 | L4, L5 | L4, L5 | the governed `SUBTYPE-DEFINITION`, where applicable | the owning Record Model: the domain semantics of its Records that use the subtype | subtype definitions 070–071 |
| **L4** Instance data | one Record's actual values | L1, L2, L3 | L5 | L5 | none — semantic dependency transfers no Record ownership | the Record Model that owns the Record; Registry acquires no ownership of another model's Record, and its own R Records remain R-owned | each model's own specification |
| **L5** Derived / projection | recomputed views | L1–L4 | — | nothing | none implied | inputs owned by their models; the projection itself non-authoritative | Artifact 053; P6/P8 derived layer |

**Cells the source does not fill are not filled here.** The table does not say whether a
definition may depend on another definition *in the same layer* (other than Peer on RFS), or whether
a Subtype may depend on a kind other than its own. RMS §10.3 allows *"R → R definitions"* in
general. Same-layer dependency and cycles are **not established here**; row 111 owns *"no cycles"*.

**Which Registry Kinds sit in which layer.** The L1–L3 rows name their own contents (§4.1, §4.3),
and the downstream columns above follow those names. RMS §10.1 freezes fourteen Registry Kinds; the
§9.4 rows do not place `MODEL-DEFINITION`, `SCHEMA-DEFINITION`, `CONTROLLED-VOCABULARY`,
`IDENTITY-GRAMMAR`, `VALIDATION-RULE`, `CONSTRAINT-DEFINITION`, `CAPABILITY-DEFINITION`,
`DERIVATION-RULE` or `SIMULATION-MODEL-DEFINITION`. Their layer placement is **not established by
current sources**, and this contract assigns it to no artifact (§14.2).

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
| **D-8** | L1 does not semantically depend on L2, L3, L4 or L5; L2 does not depend on L3, L4 or L5; L3 does not depend on L4 or L5. | §9.4; row 062 `Val` |
| **D-9** | A declaration reference that RMS §10.3 permits and Artifact 063 bounds — for example a Registry definition naming a declared Kind — does not, by itself, establish a semantic dependency. Naming or referencing a declared Model, Kind, schema, semantic contract or Registry definition does not make that target semantic authority for the referencing definition merely because the reference is legal. Where the applicable definition-family contract establishes that the same concrete relation is also a semantic dependency, D-1 to D-8 and Artifact 111's rules apply to that dependency. | RMS §10.3; §9.4; row 062 `Val`; Artifact 063 RB-5 |

**Semantic dependency is settled here; reference legality is not decided here.** D-1 to D-9 close
the layer question that row 062's `Val` — *"downward-only"* — assigns to this contract. Which
declaration references a Registry definition may carry is a different question. RMS §10.3 states
the current precise boundary — references to other Registry definitions and to declared Record
Models, Kinds, schemas and semantic contracts — and Artifact 063 applies it (§9, §14.1).

**An instance is never upstream.** A domain instance may motivate a later proposal to change a
definition. That makes the instance neither an upstream semantic dependency nor semantic authority
for the definition (RMS §10.3). How such a change is governed is Artifact 065's.

**What the rule is not.**

- **Not a runtime order.** The layers order meaning. They set no evaluation, loading, resolution or
  execution order. Generic Record and `_ref` resolution is not Registry work: *"Reference resolution
  is not Registry work"* (§9.4), and reference resolution is a universal mechanism (RMS §4).
  Resolving a Registry definition by id and version is a separate service, row 115's (§12).
- **Not a cross-model rule.** D-6 states the only cross-model fact the contract carries — instances
  depend on definitions. It creates no edge between Record Models (§9).
- **Not package composition or storage layout.** The layers say nothing about how any model
  packages or stores its Records; package composition is model-owned (Artifact 056), and storage
  shape is model-owned within the storage contract (RMS §4).

## 8. Dependency vs Ownership

```
A depends semantically on B     ≠     A owns B
```

- A `SUBTYPE-DEFINITION` that semantically depends on the relevant `KIND-DEFINITION` does not own
  that definition. Both definition Records are Registry Records, owned by the Registry Record Model
  (Artifact 061 §4). The owning Record Model keeps the Kind's and the subtype's domain semantics,
  its taxonomy and admission where they apply, and its domain Records; a domain Kind or subtype is
  not an R Record (§4.3).
- A Record at L4 depends on definitions in L1–L3. The dependency gives Registry no ownership of it:
  *"Registry governs the definitions. Each Record Model owns its Records."* (§13.6e; I-105; 061 §4)
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
- **A dependency does not, by itself, establish reference legality.** What Registry may reference
  is Artifact 063's (row 063 `Val`), enforced by 112.
- **A legal reference is not, by legality alone, a semantic dependency.** A Registry definition may
  name a declared Kind where RMS §10.3 and Artifact 063 permit it, without that Kind becoming
  semantic authority for the definition (D-9).
- **Separate predicates, not exclusive ones.** Reference legality and semantic dependency are
  separate predicates. Neither implies the other by category, and a concrete relation may satisfy
  both. Whether a concrete relation exists is the applicable definition-family contract's to
  establish (Artifact 063 RB-5):

  | The concrete relation is | Governed by |
  |---|---|
  | a legal reference only | 063 |
  | a semantic dependency only | 062 (layer direction) and 111 (concrete rules) |
  | both | 063 for the reference; 062 and 111 for the dependency |
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

**No Record gains a field.** The universal envelope stays *"the bootstrap set and no more"*:
`partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4).
No *layer*, *status*, *tier*, *schema* or other field is added to it or to any Record. Shared field
semantics define the meaning of a field where a model's Records carry that field; they do not make
any field present anywhere.

**`status` in the RFS row.** Blueprint §9.4 uses `status` in its older RFS example, and says that
what `status` *"means everywhere it appears is Registry"*. RMS §4 later closes the current Record
System boundary: `tier` and `status` are World-owned and are not universal envelope fields, and
other models define their own state vocabularies (FG-V7-03). This contract therefore establishes no
`status` field outside World and no universal state vocabulary. Registry may govern an applicable
definition or controlled vocabulary where the governing sources assign one (§13.7c); that does not
make `status` universal and creates no universal lifecycle or state model.

**Identity in the RFS row.** RFS lists *identity* field meaning. The identity grammar is universal
and its semantics are model-owned (RMS §5: *"UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC
MODEL"*; Artifact 046). An identity field definition in L1 does not give Registry any Record's
identity semantics.

## 11. Authority, Canonicality and Source-of-Truth Class

Layer position is not a ranking of anything else:

| Layer order does not mean | Why | Source |
|---|---|---|
| a layer nearer L1 is more authoritative | authority is domain-scoped; order measures dependency only | RMS §17; Artifact 051 §7 |
| a layer nearer L1 is more canonical, or closer to World Truth | Registry is canonical *"about meaning"*, never about the world | Blueprint §13.7c; I-88; Artifact 052 |
| a layer nearer L5 is less authoritative | L2–L4 are not ranked by it | Artifact 061 §11 |
| a layer nearer L5 is Derived | only L5 is Derived, by its own source rule | §9.4; §29.6a; Artifact 053 |
| a layer's position assigns a source-of-truth class | no position assigns `AUTHORITATIVE`, `DERIVED`, `CACHED`, `TEMPORARY` or `EXTERNAL`; a Record's class is assigned independently | §29.6a; RMS §4; Artifact 050 |
| constitutional superiority | the Spine and the one Authority are untouched by it | Spine law 3; Artifact 051 §6 |

Layer ordering creates no authority ranking, no canonicality ranking and no source-of-truth
ranking. A Record's source-of-truth class is assigned independently, under Artifact 050,
Blueprint §29.6a and RMS §4; L4 membership assigns none. L5's non-authoritative character is a
specific source rule for Derived / projection — §9.4's *"Nothing — non-authoritative"*, and
Artifact 053's discipline that Derived is never authoritative — not an inference from its being
the last layer.

## 12. Definition-Family Handoffs

| Layer | Family content, where the source names it | Owner |
|---|---|---|
| L1 RFS | shared field definitions | 072–073 |
| L1 Peer | relationship-type and participant-role definitions; indicator definitions; change-and-operation semantics | 079–080; 086–087; change-and-operation semantics — no family row names it (§14.2) |
| L2 | kind definitions | 068–069; the roster 064 |
| L3 | subtype definitions | 070–071 |
| — | controlled value sets (*"structure/vocabulary split"*) | 081–082 |
| — | generic Record and `_ref` resolution — what a reference resolves to, and the mechanics of resolving it | not Registry-owned: *"belong to a Record resolver"* (§9.4); reference resolution is a universal mechanism (RMS §4). The implementation artifact is not assigned here |
| — | Registry definition resolution — a consumer resolves a Registry definition by id and version | 115, Registry resolution service (row 115 `Val`: *"consumer resolves by id+version"*) |

This contract writes none of their schemas, fields, lifecycles or semantics.

## 13. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | Registry's layers are universal Record layers | they order Registry definitions; no model inherits them | I-101; RMS §2, §4 |
| 2 | A layer owns a layer it depends on, or one that depends on it | dependency is not ownership | §13.6e; I-105 |
| 3 | Semantic dependency transfers Record ownership | Records stay with their partition's model | I-16; 045 §9 |
| 4 | Semantic dependency permits a Record reference | references are 063's | row 063 |
| 5 | Semantic dependency permits a cross-model edge | edges are 058's | Artifact 058 |
| 6 | A layer nearer L1 is more authoritative or more canonical | order is dependency only | RMS §17; §13.7c |
| 7 | A layer nearer L5 is Derived | only L5 is Derived | §9.4; §29.6a |
| 8 | Every Record has a layer field | no field is added; the envelope is fixed | RMS §4 |
| 9 | Every Record has `status` | `status` is World-owned, not universal | RMS §4 (FG-V7-03) |
| 10 | Registry owns a model because it resolves against Registry | definitions are governed; Records are owned | I-105; 061 §4 |
| 11 | Registry defines a Kind, so owns its instances, taxonomy or domain semantics | Registry holds the `KIND-DEFINITION`; the owning model keeps the Kind in its domain | §9.4; §13.6e; 061 §7 |
| 12 | Registry defines relationship types, so owns relationship instances | definitions only; never runtime relationship ownership | RMS §15 |
| 13 | Registry defines validation rules, so executes all validation | runtime validators implement validation | RMS §10.6 |
| 14 | Registry owns a universal semantic schema | no universal semantic schema exists | RMS §4 |
| 15 | The layer order is an execution or resolution order | resolution is not Registry work | §9.4; RMS §4 |
| 16 | A definition's dependency is a Relationship Record | dependencies, not owned edges | §13.2; I-102 |
| 17 | A legal declaration reference is, by legality alone, an upward semantic dependency | reference legality and semantic dependency are separate predicates | D-9; RMS §10.3 |
| 18 | A semantic dependency is automatically a Record reference | dependency establishes no reference field and no legality | §9; row 063 |
| 19 | Reference and semantic dependency are mutually exclusive; one relation cannot be both | a family contract may establish a concrete relation that is both; 063, 062 and 111 then all apply | §9; Artifact 063 RB-5 |
| 20 | A declared Kind named by a Registry definition becomes semantic authority for that definition | naming is not authority | D-9; RMS §10.3 |
| 21 | Blueprint's older *"may never reference a kind"* wording overrides RMS §10.3 | RMS §10.3 corrects it and is the current precise rule | RMS §10.3; §14.1 |
| 22 | The Blueprint/RMS reference wording is still an unresolved conflict | RMS §10.3 explicitly corrects the older wording; 063 applies it | §14.1 |
| 23 | Artifact 115 is the generic Record resolver | 115 resolves Registry definitions by id and version | row 115; §12 |
| 24 | Registry owns `_ref` resolution because it defines reference semantics | *"Reference resolution is not Registry work"* | §9.4; RMS §4 |
| 25 | Registry-definition resolution and generic Record-reference resolution are one mechanism | no source unifies them | §9.4; RMS §4; row 115 |
| 26 | A domain subtype is a Registry Record | the `SUBTYPE-DEFINITION` is; the subtype's domain semantics stay with the owning model | §4.3, §8 |
| 27 | A domain Kind is its `KIND-DEFINITION` | the definition is a Registry Record; the Kind stays in its model's taxonomy | §4.3; Artifact 057 §4 |

## 14. Source Conditions and Deferred Matters

### 14.1 Historical reference wording — resolved by RMS §10.3

| | |
|---|---|
| **Source A — older Blueprint wording** | Blueprint §9.4: *"A Registry definition may never reference a kind, a subtype, or an instance; a kind may never reference an instance."* Restated at §13.6e and as I-75. |
| **Source B — current precise rule** | RMS §10.3, `FROZEN`, headed *"Reference boundary"* and marked as correcting v0.1: *"v0.1 stated the boundary too bluntly"*. *"Registry MAY reference: other Registry definitions · declared Record Models · declared Kinds · declared schemas · declared semantic contracts."* *"Registry MAY NOT: own domain instances · depend on runtime instances · mutate domain instances · use domain instances as semantic authority."* |
| **Status** | **RESOLVED for reference legality** by RMS §10.3, which is the current precise reference boundary. It is no longer treated as an unresolved conflict. |
| **Owner** | Artifact 063 applies the RMS §10.3 boundary (row 063 `Val`). This contract owns only semantic dependency direction. |
| **Effect on this contract** | Source A remains historical context for why upward semantic authority and instance dependence are prohibited — where A and B agree. It is not used to re-impose the obsolete absolute prohibition on referencing a Kind or a subtype. D-1 to D-9 are unchanged. |

### 14.2 Source gaps

- **Layer placement of Kinds the rows do not name** (§6) — **not established by current sources.**
  No source or Roadmap row places them. This contract assigns the placement to no artifact: row
  064's `Val` is *"exactly fourteen Kinds, each with admission rationale"*, and row 111's is
  *"downward-only; asymmetric; no cycles"*; neither names layer placement.
- **Change-and-operation semantics** (Peer row) corresponds to no RMS §10.1 Kind and no family row.
  Recorded; the roster is 064's.
- **Same-layer dependency and cycles** — not established by §9.4; row 111 owns *"no cycles"*. This
  is not the question of whether L1 may depend on L2, which D-8 closes.

## 15. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-062-01** | There are exactly five conceptual layers. All six source rows are preserved; L1 comprises RFS (1a) and the peer semantic authorities (1b) as distinct internal strata. | §9.4 |
| **C-062-02** | The order is L1, L2, L3, L4, L5. Inside L1, RFS depends on nothing within this contract, and Peer semantic authorities DEPEND-ON RFS. | §9.4 |
| **C-062-03** | A layer depends only on the layers its source row lists, all above it: Kind semantics on L1; Subtype semantics on L1 and its own kind; Instance data on L1–L3; Derived / projection on L1–L4. | §9.4; §13.6e |
| **C-062-04** | No conceptual layer semantically depends on a higher-numbered layer; L1 does not depend on L2, L3, L4 or L5. | §9.4; I-75; row 062 `Val` |
| **C-062-05** | No Registry definition depends on, or takes its meaning from, a domain instance. | §9.4; RMS §10.3 |
| **C-062-06** | Derived / projection is terminal and non-authoritative: nothing depends on L5. | §9.4; §12.4 |
| **C-062-07** | Semantic dependency transfers no Record ownership. | §13.6e; I-105; I-16 |
| **C-062-08** | Semantic dependency alone establishes neither a Record reference nor reference legality, and reference legality alone establishes no semantic dependency; a family contract may establish a concrete relation that satisfies both predicates. | row 063; Artifact 063 RB-5 |
| **C-062-09** | Semantic dependency establishes no cross-model edge. | Artifact 058 |
| **C-062-10** | Layer position is not an authority ranking. | RMS §17; 051 |
| **C-062-11** | Layer position is not a canonicality ranking. | §13.7c; 052 |
| **C-062-12** | Layer position does not determine source-of-truth classification; a Record's class is assigned independently. L5 Derived / projection is non-authoritative by its own source rule, not by position. | §29.6a; RMS §4; 050; 053 |
| **C-062-13** | The layers do not apply as a semantic architecture to W, E, P, V or I. | I-101; RMS §2 |
| **C-062-14** | The universal envelope remains exactly seven fields; no field — layer, `status`, `tier`, schema or other — is added to it or to any Record, and shared field semantics imply no universal field presence. | RMS §4 |
| **C-062-15** | `status` remains World-owned and is not universalized; no universal state vocabulary or lifecycle is created. | RMS §4 (FG-V7-03) |
| **C-062-16** | Registry holds the governed `KIND-DEFINITION` and `SUBTYPE-DEFINITION`; that transfers no model's Kind taxonomy, Kind or subtype domain semantics, or instances. | §9.4; §13.6e; RMS §10; I-105; Artifact 061 |
| **C-062-17** | L4 ownership remains with the Record Model that owns the Record: no semantic dependency transfers it to Registry, W, E, P, V and I retain their Records, and Registry's own R Records remain R-owned. | §13.6e; I-16; I-105; Artifacts 060, 061 |
| **C-062-18** | No Relationship Record arises from a layer dependency. | §13.2; I-102 |
| **C-062-19** | Runtime validation, generic Record and `_ref` resolution, and Registry definition resolution (115) stay outside the layers; generic Record resolution is not Registry-owned and is not 115's. | §9.4; RMS §4, §10.6; row 115 |
| **C-062-20** | Artifact 064 owns the exact fourteen-Kind roster and admission rationale. Layer placement for Registry Kinds not placed by Blueprint §9.4 is not established by this contract and is not assigned to 064, or to any artifact, here. | row 064; §9.4 |
| **C-062-21** | Governance is not decided here (065). | row 065 |
| **C-062-22** | Exact reference legality is not decided here (063). | row 063 |
| **C-062-23** | The five-layer downward-only semantic direction is settled by this contract. Artifact 111 owns detailed Registry-definition dependency rules — same-layer dependency, asymmetry, cycle prohibition and concrete dependency-graph constraints — and does not reopen the layer order. | row 062 `Val`; row 111 |
| **C-062-24** | The older Blueprint reference wording is retained only as historical context; RMS §10.3 explicitly corrects it and is the current precise reference boundary, which Artifact 063 applies. This contract does not reopen reference legality. | §9.4; RMS §10.3; row 063 |
| **C-062-25** | Frozen P0, P1 and P2 architecture is unchanged, and their suites stay green. | Artifact 004; rows 030, 038, 059 |
| **C-062-26** | A declaration reference permitted by RMS §10.3 and Artifact 063 does not, by legality alone, create a semantic dependency or semantic authority from its target; where the applicable family contract establishes that the same concrete relation is a semantic dependency, it obeys D-1 to D-8 and Artifact 111. | RMS §10.3; D-9; Artifact 063 RB-5 |

## 16. Downstream Handoff

| Artifact | May assume from 062 | Must still define |
|---|---|---|
| **063** reference boundary | the five-layer order and downward-only semantic direction; no definition depends on or takes meaning from an instance; reference legality and semantic dependency are separate predicates — legality alone establishes no dependency, and a concrete relation may be both where the family contract says so (D-9) | the exact current reference boundary under RMS §10.3: admissible target categories, forbidden targets, declaration qualification, domain-instance and runtime rejection |
| **064** Kind taxonomy | that 062's five-layer contract exists; which contents the §9.4 rows name | the exact fourteen Kinds and each admission rationale. It inherits from 062 no obligation to place every Kind in a layer. |
| **065** governance | that layers carry no authority ranking | who may propose, approve, deprecate |
| **111** dependency direction | the five layers and their downward-only direction, settled (D-1 to D-9) | asymmetry and no-cycle rules; same-layer dependency; concrete dependency-graph constraints |
| **112–117** | the contract they enforce and implement | validation, binding, kernel, identity binding, and Registry definition resolution by id and version (115); generic Record and `_ref` resolution is not assigned to 115 |

## 17. Roadmap Completion Trace

| Row 062 | Status | Where it is met |
|---|---|---|
| `Val`: *"five semantic layers"* | **SATISFIED** — five conceptual layers are fixed; the six source rows are kept through L1's internal strata | §4; C-062-01, C-062-02 |
| `Val`: *"downward-only"* | **SATISFIED** — no layer takes defining semantic authority from a higher-numbered layer; exact reference legality is a separate question, owned by 063 | §5, §7; C-062-03 to C-062-06, C-062-23, C-062-26 |
| `Done`: *"contract"* | **SATISFIED** — layer responsibilities, the dependency law, the ownership boundary, the reference distinction and the handoffs are normative | §6–§13, §16; C-062-01 to C-062-26 |
| `Why`: *"Blueprint's own Registry layering"* | **SATISFIED** — the layers are §9.4's | §3, §4.1 |
| `H: 061` | **SATISFIED** — every rule respects the authority boundary | §4.3, §8, §11, §13 |
| `→ 063` | **SATISFIED** — the direction is settled; reference legality stays 063's, under RMS §10.3 | §9, §14.1, §16 |

---

*Artifact 062 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This contract
states the Registry semantic layers and their downward-only dependency, derived from Master
Blueprint §9.4 and §13.6e and the Record Model System §10. It is not a Registry Record, holds no
canonical data, defines no schema, field, validator or algorithm, and implements nothing. Where it
differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those
governing sources are correct and this document is wrong.*
