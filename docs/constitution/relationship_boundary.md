# COOLBOY12 — Relationship Boundary Specification

**Artifact 055** · relationship boundary specification ·
`docs/constitution/relationship_boundary.md` · Own: CONST · RM: all · T: doc · R: CONTRACT ·
SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P2/2d · Req: RR-28 ·
BP: §13.3 · RMS: §15 · H: 039 · S: — · LS: — · G: — · → P7,P10–P13 ·
Val: reification criterion; Relationship Record declared **World-only** ·
Done: criterion + scope · Why: I-102 made buildable · Risk: CRITICAL · ∥: no

## 1. Purpose

This contract has two jobs, and only two:

- **A.** State the source-backed criterion for when a connection between Records is a first-class
  Relationship rather than a field, a reference, a composition or a projection.
- **B.** Declare the named Relationship Record a **World** Record Model construct, not a Record
  System primitive.

Row 055's reason is *"I-102 made buildable"*. I-102 states the scope; this contract makes it, and
the criterion beside it, checkable. Everything else below exists to make those two boundaries
precise.

**This contract adds no architecture.** Every rule restates RMS §6.1 and §15, Artifact 044 §8,
Blueprint §9.4, §12.4, §12.11, §13.3, §13.5, §13.6d, §13.6e, §13.7a, §13.9 and §13.10, and I-72,
I-73, I-74, I-84, I-88, I-90, I-101, I-102, I-103 and I-107.

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the relationship boundary**: the reification criterion, the
edge-ownership rule's reach, and the scope of the Relationship Record. It is not World Canon, not a
Record, not a schema, and holds no authority over any Record Model's relationship design.

It derives the contract from the Master Blueprint and the Record Model System; it does not amend,
supersede, or outrank either, and amends no invariant. Where this document differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those governing sources are
correct and this document is wrong.**

`Req: RR-28` is preserved exactly as the Roadmap states it. The authoritative requirement register
is not present in this repository; the requirement text is **not** reproduced and **MUST NOT** be
inferred.

## 3. Scope

**In scope.** The reification criterion; Relationship against field, reference, composition,
dependency and projection; relationship type against relationship instance; the single-owner rule
and the owning role; the Derived back-reference; the Relationship Record's World scope, its
current-state rule and the WSV source status; the Registry, authority and temporal boundaries.

**Out of scope.** The package boundary (Artifact 056); cross-model dependency (058); the temporal
obligation (054); relationship-type definition and schema (079, 080); the World Relationship Record
specification, type set and schema (197, 198, 199); every other model's relationship architecture
(276, 277, 338, 356, 366); the back-reference projection's implementation (224).

```
039  Record System constitution      — Relationship Record is a World concept; no universal one
044  architectural categories        — Relationship: first-class only when no endpoint can own it
055  relationship boundary           ← this contract: the criterion applied; the Record's scope
056  package boundary                — packaging model-owned
  ↓
197–199  World Relationship Record   ·   276/277 E · 338 P · 356 V · 366 I   — each model's own
```

## 4. The Governing Relationship Rule

> **A connection between Records is a first-class Relationship only when no endpoint can own it
> without ambiguity. A Relationship's meaning is defined by a Registry relationship type. Wherever
> Relationship Records are used, each edge is authoritative in exactly one of them — the one its
> type's owning role names — and the non-owning endpoint's view is Derived. The named Relationship
> Record is a World Record Model construct, not a Record System primitive.**

| Clause | Source |
|---|---|
| First-class only when no endpoint can own it | RMS §15; RMS §6.1; Artifact 044 §8 |
| Meaning defined by a Registry relationship type | Blueprint §13.3, §9.4, §13.6e |
| Exactly one authoritative Relationship Record per edge, by owning role | I-73; I-90; Blueprint §13.9 |
| Non-owning view Derived | I-73; Blueprint §13.9, §12.11 |
| Relationship Record World-scoped, not a primitive | I-102; Blueprint §13.9, §13.7a |

**Relationship ≠ Relationship Record.** The first is a semantic category; the second is World's
packaging. §13.3: the principle that a relationship is a modelled thing *"is a Record System
principle available to every model"*, while *"The packaging — the Relationship Record, its
ownership rule, and its boundedness — is World Record Model architecture (§13.9, I-102)."* That
the Relationship Record is World-only does **not** make relationships World-only.

## 5. The Reification Criterion

### 5.1 Source basis

| Source | What it establishes |
|---|---|
| RMS §15 (`FROZEN`) | *"reify only when no endpoint can own the edge without ambiguity"*, citing Blueprint §13.3 and §13.8 |
| RMS §6.1 (`FROZEN`) | Relationship: *"A connection between Records"*; test: *"First-class only when no endpoint can own it"* |
| Artifact 044 §8 | *"The default is that a connection is owned by one of its endpoints — as a field, or as a reference held by the owning side. A Relationship becomes a first-class thing only when that ownership cannot be assigned cleanly to either end."* |
| Blueprint §13.3 | What a first-class relationship is: *"A relationship is not a field and not an attribute. It is a typed, directional, temporally-valid, provenanced connection with its own stable identity and its own definition in the Registry."* |
| Artifact 039 | That the Relationship Record is *"A World Record Model concept, not a Record System primitive"*, and that there is no Universal Relationship Record. 039 does not itself state the criterion. |

**Source note.** The criterion's wording is RMS §15's and RMS §6.1's. The Blueprint sections RMS
§15 cites for it, §13.3 and §13.8, do not contain that wording; they give its reason — RMS §15:
*"v0.4 made relationships objects with their own history and reversed it, because it orphaned edge
histories with no successor."* This contract takes the wording from the RMS and the reason from the
Blueprint, and invents neither.

### 5.2 The test

```
Q1  Is it a connection between Records?
      NO  → not a Relationship. An attribute with no independent identity is a Field.
      YES ↓
Q2  Can one endpoint own it without ambiguity — as a field, or as a reference held by
    the owning side?
      YES → not a first-class Relationship: a Field or a reference on the owning side.
      NO  → a first-class Relationship.
```

Where the governing model architecture already classifies a connection as composition,
dependency, or another non-Relationship mechanism (§5.5 below), that source-defined classification
is preserved; this test does not reclassify it merely because it is not represented as a field or
reference. The test applies to connections the governing sources have not already classified.

A connection that qualifies carries what §13.3 attaches to a Relationship: a stable identity; a
Registry-defined type *"carrying its participant roles, its direction, its cardinality, and its
legality constraints"*; temporal validity; and provenance. 044 §8 gives the World case: *"a causal
edge whose meaning belongs to neither participant alone is a Relationship rather than a field on
either participant."*

**SOURCE GAP — "ambiguity".** No governing source defines when ownership is ambiguous. This
contract does not define it. Applying the criterion to a concrete connection is the owning model's
relationship-architecture work: row 197's Val requires *"reification criterion satisfied"* for
World, and rows 276, 338, 356 and 366 carry it for E, P, V and I.

**Two uses of "own".** The criterion asks whether an endpoint can own a connection *as a field or
as a reference* (044 §8). The ownership rule of §7 below decides which endpoint's Relationship
Record holds an edge that has already qualified. RMS §15's World row joins the two in that order —
*"reified; Registry declares the owning role"* — and this contract reads them as two steps. It adds
no third test.

### 5.3 Relationship vs field

A Field is *"An attribute of a Record"* with *"no independent identity"* (RMS §6.1). A Relationship
has *"its own stable identity"* (§13.3). §13.3: *"A relationship is not a field and not an
attribute."* A pointer held on one endpoint that the endpoint can own without ambiguity stays a
field.

### 5.4 Relationship vs reference

A reference held by the owning side is the default, not a Relationship (044 §8). Issue shows the
boundary: *"Issue references; it never owns"*, and *"a reference from a lower partition confers
nothing"* (§13.6a). RMS §15 gives Production *"References · dependencies · workflow transitions"*.
**A references B** therefore does not entail **A relates to B** as a first-class Relationship.

### 5.5 Relationship vs composition and dependency

A model may express connection as composition or as dependency. §13.3: *"Issue expresses connection
as composition and Registry as dependency, and both honour the principle without a Relationship
Record (§13.6d)."* §13.6d's Issue row: *"Its internal structure is composition, not relationship: a
page belongs to a spread the way a paragraph belongs to an article."* Registry's definition
dependencies are *"governed by the downward-only rule (Section 9.4), not by edge ownership."*
**A contains B** does not entail a Relationship Record.

### 5.6 Relationship vs projection

A Projection is *"Derived, rebuildable output"*, *"Never authoritative (§29.6a)"* (RMS §6.1). A
back-reference on the non-owning endpoint is a projection of an owned edge, not a second
Relationship (§7.3 below). A graph assembled from edges is a projection: §12.5 records that an
edge *"is stored in the Relationship Record of exactly one owning endpoint"*, and AC-1 (§26.7) that
a graph capability *"may compute; it may not hold."*

## 6. Relationship Type vs Relationship Instance

| Term | What it is | Owner | Source |
|---|---|---|---|
| **Relationship** | the semantic category: a connection no endpoint can own | — (category) | RMS §6.1; Artifact 044 |
| **Relationship type** | the definition: meaning, participant roles, direction, cardinality, legality, owning role | Registry (`RELATIONSHIP-TYPE-DEFINITION`) | §13.3; §9.4; §13.6e; Artifacts 079, 080 |
| **Relationship instance (edge)** | one actual connection between actual Records | the owning endpoint, where Relationship Records are used | I-73; §13.9 |
| **Relationship Record** | World's packaging of an object's current edges | World | §13.9; I-72; I-102 |
| **Back-reference** | the non-owning endpoint's view of an edge | Derived — no one's authority | §13.9; §12.11; I-73 |
| **Reference** | a pointer held by the owning side | the holding Record's model | Artifact 044 §8 |
| **Composition** | part-of structure a model expresses as such | the model | §13.3; §13.6d |
| **History / temporal account** | how the edge came to be as it is | the owning object's temporal mechanism | I-74; §13.5; Artifact 054 |

**Three ownership questions, never collapsed:**

| Question | Answer | Source |
|---|---|---|
| Who defines what this relationship type means? | Registry | §13.6e; §9.4 |
| Which Record Model owns the mechanism that holds the edge? | the relevant Record Model — World for the Relationship Record | §13.6e; §13.6d; §13.9 |
| Which endpoint holds this edge authoritatively? | the one the type's owning role names | I-73; §13.9 |

## 7. Relationship Ownership

### 7.1 Exactly one authoritative owner

§13.9: *"If both endpoints' Relationship Records held it authoritatively there would be two sources
of truth for one edge — a direct violation of Spine law 1."* I-73: *"an edge authoritative in two
Relationship Records is a structural violation."* The rule is not model-owned. I-90: *"Package
composition is owned by each Record Model; the relationship-ownership rule is not."* §13.6d:
*"Specialization changes whether a partition uses Relationship Records, never how they work."*

### 7.2 The Registry-declared owning role

§13.9: *"The relationship type definition in the Registry declares which participant role owns the
edge."* Its examples: *"MEMBER_OF is owned by the member"*, with `LOCATED_IN`, `DESCENDS_FROM` and
`CAUSED` likewise. The rule *"is deterministic, requires no tie-breaking, and does not depend on
creation order or on which object the author happened to be editing."* §9.4 places
*"relationship-type definitions with their participant roles and ownership rule"* in the Registry.

### 7.3 The non-owning endpoint's view is Derived

The non-owning endpoint *"sees a back-reference, which is a Derived projection"* — *"rebuildable
from the owning Relationship Records, marked stale like any other, and never authoritative"*
(§13.9). §12.11: *"A capability that reads a back-reference as though it were the record is making
a Derived source authoritative, which is the failure P-26 exists to catch."* Row 224 builds the
projection downstream: *"back-references derived, never stored on the record"*. The Derived
discipline itself is Artifact 053's.

**Citation note.** The ownership paragraph quoted in §7.1–§7.3 above is the one I-73 and §13.6d cite
as Section 13.9; in the Blueprint file it follows the §13.9a heading. It is cited here as §13.9,
as the Blueprint cites it.

## 8. Relationship Record Scope

### 8.1 World-only

§13.9: *"These are World Record Model concepts. They are not Record System primitives."* I-102:
*"Relationship Record and History Record are World Record Model concepts. Neither is a Record
System primitive, and neither may be required of another Record Model."* I-72 packages every
instance-bearing World Record as `Record + Relationship Record + History Record`.

### 8.2 Not a Record System primitive

§13.7a: *"No Universal Relationship Record. Relationship packaging is model-owned (§13.6d,
§13.9)."* RMS §4 names *"Universal Relationship Record"* among its nine prohibitions. The
Relationship Record is not part of the universal envelope, which RMS §4 fixes at seven fields
without it.

### 8.3 Other Record Models remain sovereign

§13.9: *"A Relationship Record is not a universal component, and a History Record is not a
universal component. Where another model adopts a structure of the same shape, it does so on its
own evidence and owns the result."* §13.6e gives each model *"Whether it uses Relationship Records
at all (§13.6d)"*. I-101, I-103 and I-107 forbid treating World's package as a template, a shared
semantic, or a requirement for a model not yet designed.

055 neither requires nor forbids another model's relationship mechanism. If a model adopts a
structure of the same shape, it is that model's construct, and I-73 and I-74 — each stated
*"Wherever a Record Model uses Relationship Records"* — govern it.

**Source condition recorded, not resolved.** §13.6d's package rows, marked *"MODEL-DESIGN INPUT
(not a freeze)"*, list a Relationship Record for E, optionally for P, and for V specifications. RMS
§15 (`FROZEN`) records E's knowledge relationships *"within KNOWLEDGE-STATE"* and P with *"No
Relationship Record"*, and row 276 reads *"no Relationship Record"* for E. This contract imposes
none of these rows and decides nothing between them; each model's own architecture does.

## 9. World Relationship Record Boundary

### 9.1 Current relationships only

§13.5: *"A Relationship Record holds an object's current relationships and nothing else."* I-74:
*"a Relationship Record that grows with relationship history has been implemented wrongly."* §13.9
makes it *"Authoritative for the edges it owns; never a history ledger"*.

### 9.2 History remains separate

§13.5: *"Every relationship change — formed, retimed, re-pointed, ended — is recorded in that
object's History Record, never accumulated in the Relationship Record."* The Relationship Record
holds current state; World's History Record holds its evolution (§13.9). Neither is the other.

### 9.3 WSV

**Source status.** Blueprint §13.10 currently records a `PROPOSED` reading in which *"WSV owns no
edges"* — a pressure edge targeting an indicator is owned by the other endpoint, so *"WSV is always
the non-owning endpoint"* — and WSV has no Relationship Record. I-72 states WSV's package as
`Record + WSV-H`, and §13.6d's W WSV row carries the same reading. §13.10's `PROPOSED` flag remains,
recorded by RMS Appendix H as PC-2.

**Contract effect.** Because that reading remains explicitly `PROPOSED`, this contract records it
and does not make it a conformance requirement, does not resolve the underlying source conflict,
and does not lift the flag.

## 10. Registry Boundary

> *"Registry governs the definitions. Each Record Model owns its Records."* (§13.6e)

The Registry owns *"The definition of a relationship type and its owning role"*; the model owns
*"Whether it uses Relationship Records at all"* (§13.6e). RMS §15 gives Registry *"Relationship
definitions; never runtime relationship ownership"*. I-88: *"The Registry owns meaning, never world
truth."*

So: the Registry does not hold relationship instances because it defines their types, and a
Relationship Record does not define what a relationship means. The definition and its schema are
Artifacts 079 and 080; the pairing of each model's relationships with their type definitions is
lockstep LS-3 (*"Relationship ↔ Relationship-Type-Definition"*). None of that is designed here.

## 11. Authority, Canonicality and Source-of-Truth Boundary

Edge ownership answers **where the authoritative edge lives**. It does not answer who may commit a
change (Artifact 051), what counts as canonical (052), or which source-of-truth class a value
carries (050). A World Relationship Record is *"Mutated only through the gated path"* (§13.9); the
path is the mutation boundary's, not this contract's. §13.3 places topology changes at *"always at
least Structural severity"*; severity is not defined here.

**External components.** I-84: *"No external component holds canonical semantics, defines a kind,
owns a relationship, adjudicates a mutation, or is the only place a canonical fact exists."* AC-1
(§26.7) rejects a graph database as the relationship store because *"Relationship Record would
become a projection of it"*. A graph store may hold at most a Derived or Cached projection
(§26.2d).

**Simulation.** §13.3 names causal and pressure edges so that Simulation can *"walk causality and
accumulating force as first-class structure rather than inference"*. Walking an edge is not owning
it; the edge's meaning is its Registry type's, and its home is its owning Record.

## 12. Temporal Boundary

A relationship change belongs to the owning object's temporal account: I-74, *"Every relationship
change is recorded in the owning object's history"*. The temporal obligation and its model-owned
mechanism are Artifact 054's.

For World, that account is the History Record (§13.5), and validity is stated on World Time: a
relationship *"holds from and until, in world-time"* (§13.3). That bullet is written for World.
This contract imposes World Time on no other model, and defines no relationship timestamp,
relationship history object or relationship temporal schema.

## 13. The Six Record Models

| Model | RMS §15 mechanism (quoted) | Status in 055 | Relationship Record | Downstream |
|---|---|---|---|---|
| **W** | *"World Relationship Record — reified; Registry declares the owning role"* | established | World's named construct | 197, 198, 199 |
| **E** | *"EVIDENCE first-class; knowledge relationships represented within KNOWLEDGE-STATE"* | model-owned | not imposed by 055 | 276, 277 |
| **P** | *"References · dependencies · workflow transitions. No Relationship Record"* | model-owned | not imposed by 055 | 338 |
| **R** | *"Relationship definitions; never runtime relationship ownership"* | Registry defines types; its own packaging is its own | not imposed by 055 | 079, 080 |
| **V** | *"represents · derived-from · variant-of — model-owned"* | model-owned | not imposed by 055 | 356 |
| **I** | *"Composition · placement · credit · supersession references"* | model-owned | not imposed by 055 | 366 |

RMS §15: *"Model relationships are not identical and are never made so."* The mechanism column is
RMS §15's, not this contract's. No model is barred from relationships, required to have them, or
required to use a Relationship Record; World is no model's template (I-101).

## 14. Prohibited Architectural Moves

| # | Prohibited | Source |
|---|---|---|
| 1 | A Universal Relationship Record | §13.7a; RMS §4 |
| 2 | The Relationship Record as a Record System primitive | I-102; §13.9 |
| 3 | World's Relationship Record as a template for another model | I-101; I-107 |
| 4 | Treating every reference as a Relationship | RMS §15; Artifact 044 §8; §13.6a |
| 5 | Treating every field as a Relationship | RMS §6.1; §13.3 |
| 6 | Treating every composition as a Relationship | §13.3; §13.6d |
| 7 | Treating a tool's graph edge as relationship truth | I-84; AC-1 |
| 8 | Two authoritative owners of one edge | Spine law 1; I-73; §13.9 |
| 9 | The Registry owning relationship instances because it defines their types | §13.6e; RMS §15; I-88 |
| 10 | A non-owning back-reference becoming authoritative | I-73; §12.11; §13.9 |
| 11 | A Relationship Record becoming a history ledger | I-74; §13.5 |
| 12 | A history mechanism becoming the current relationship state | §13.5; §13.9 |
| 13 | An external component as relationship authority | I-84; AC-1 |
| 14 | Simulation as relationship authority | §13.3; §13.9 |
| 15 | Shared infrastructure read as shared relationship semantics | I-103; §13.7a |
| 16 | A model inheriting relationship packaging from another | I-90; I-101; §13.9 |
| 17 | A universal relationship schema | §13.7a; RMS §4 |
| 18 | A universal relationship Record subtype or Kind | RMS §4; I-102 |
| 19 | Designing the World Relationship Record's schema here | Roadmap rows 197–199 |
| 20 | Reopening the retired Canon Object Model | Blueprint §13.6d; Artifact 039 |
| 21 | A reification criterion not in RMS §15, RMS §6.1 or Artifact 044 | this contract, §5.1 |

## 15. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number.

| ID | Condition | Source |
|---|---|---|
| **C-055-01** | The reification decision uses the criterion of RMS §15 and §6.1 as Artifact 044 §8 states it. | RMS §15, §6.1; Artifact 044 |
| **C-055-02** | A field, reference, composition or Derived projection is not thereby a first-class Relationship. | RMS §6.1; Artifact 044 §8; §13.3; §13.6d |
| **C-055-03** | A relationship type definition and a relationship instance are distinct. | §13.3; §13.6e |
| **C-055-04** | Wherever Relationship Records are used, each edge has exactly one authoritative owner. | I-73; I-90; §13.9 |
| **C-055-05** | The Registry-defined owning role determines which endpoint owns an edge. | I-73; §13.9 |
| **C-055-06** | The non-owning endpoint's view is Derived and never authoritative. | I-73; §12.11; §13.9 |
| **C-055-07** | The named Relationship Record is World-scoped and not a Record System primitive. | I-102; §13.9; §13.7a |
| **C-055-08** | World's Relationship Record holds current relationships only. | I-74; §13.5 |
| **C-055-09** | Relationship evolution is recorded in the owning object's temporal account, not the Relationship Record. | I-74; §13.5 |
| **C-055-10** | *Withdrawn.* The WSV reading of Blueprint §13.10 is `PROPOSED`; it is recorded in §9.3 above and is not a condition of this contract. | Blueprint §13.10 |
| **C-055-11** | E, P, R, V and I are not required by 055 to adopt World's Relationship Record. | I-102; I-107; §13.6e |
| **C-055-12** | No Record Model is a template for another's relationship packaging. | I-101; I-90 |
| **C-055-13** | The Registry defines relationship-type meaning and owning role and holds no relationship instance. | §13.6e; RMS §15; I-88 |
| **C-055-14** | No external component owns relationship semantics or instances. | I-84; AC-1 |
| **C-055-15** | No relationship schema, field list, Record, Kind, API, runtime, storage or validator is created. | Roadmap row 055 `T: doc` |
| **C-055-16** | No invariant is created or amended. | — this contract, §2 |
| **C-055-17** | Artifacts 054, 056 and 058 are not redefined. | Roadmap rows 054, 056, 058 |
| **C-055-18** | The absence of a source definition of *ambiguity* stays disclosed and is not filled. | this contract, §5.2 |

A construction satisfying all seventeen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 16. Worked Examples

> **Illustrative and non-normative.** Names are invented. No example defines a schema, field,
> structure or relationship type.

**Example A — a World relationship.** *Character A MEMBER_OF Organization B.* The type
`MEMBER_OF` declares the member as owning role (§13.9), so Character A's Relationship Record holds
the edge; Organization B sees a Derived back-reference.

**Example B — a reference.** *Issue 12 references Event C.* Issue references and never owns
(§13.6a). Nothing in the reference makes it a first-class Relationship; the criterion decides, and
Issue's own architecture (366) applies it.

**Example C — a composition.** *A page belongs to a spread.* §13.6d calls Issue's interior
*"composition, not relationship"*. It is not a Relationship Record.

**Example D — dual authority.** Character A's and Organization B's Relationship Records both hold
*A MEMBER_OF B* authoritatively. Invalid: two sources of truth for one edge (Spine law 1; I-73),
and blocked by the linter (§12.15).

**Example E — current state and history.** A's Relationship Record holds *A MEMBER_OF B, from year
890*. When A leaves in 902, the edge is ended in the Relationship Record and the change is entered
in A's History Record (§13.5). The Relationship Record does not keep the past membership.

**Example F — model sovereignty.** World uses the Relationship Record. Epistemic, per RMS §15 and
row 276, holds knowledge relationships within KNOWLEDGE-STATE. Neither is the other's template, and
055 decides neither.

## 17. Source Traceability

| Rule | Source |
|---|---|
| Artifact identity and acceptance | Roadmap row 055 |
| Reification criterion | RMS §15, §6.1; Artifact 044 §8 |
| Reason for the criterion | RMS §15; Blueprint §13.3, §12.5 |
| What a first-class relationship carries | Blueprint §13.3 |
| Relationship as an architectural category | RMS §6.1; Artifact 044 |
| Relationship principle available to every model; packaging World's | Blueprint §13.3 |
| Field has no independent identity | RMS §6.1 |
| Reference is the default; Issue references and never owns | Artifact 044 §8; Blueprint §13.6a |
| Composition and dependency honour the principle without a Relationship Record | Blueprint §13.3, §13.6d |
| Exactly one edge owner | Spine law 1; I-73; I-90; Blueprint §13.9, §13.6d |
| Registry declares the owning role | Blueprint §13.9, §9.4, §13.6e; Artifact 079 |
| Non-owning back-reference is Derived | Blueprint §13.9, §12.4, §12.11; I-73 |
| Relationship Record is World-only, not a primitive | I-102; Blueprint §13.9, §13.7a; Artifact 039 |
| World package | I-72; Blueprint §13.9 |
| WSV reading (no Relationship Record) — `PROPOSED` in §13.10; recorded, not adjudicated | I-72; Blueprint §13.10, §13.6d; RMS Appendix H PC-2 |
| Current relationships only; changes in history | I-74; Blueprint §13.5, §13.9 |
| Model sovereignty; no template | I-101 |
| Shared infrastructure ≠ shared semantics | I-103; Blueprint §13.7a |
| Package composition model-owned; ownership rule not | I-90; Blueprint §13.6d |
| Provisional design input | I-107; Blueprint §13.6d |
| Registry owns meaning, not instances | I-88; Blueprint §13.6e; RMS §15 |
| External component cannot own a relationship | I-84; Blueprint §26.2d, §26.7 AC-1 |
| Relationship changes in the temporal account | I-74; Blueprint §13.5; Artifact 054 |
| Per-model relationship mechanisms | RMS §15 |
| Concrete World implementation downstream | Roadmap rows 197–199 |
| Other models' relationship architectures downstream | Roadmap rows 276, 277, 338, 356, 366 |
| Relationship ↔ type-definition lockstep | Roadmap LS-3 |

## 18. Downstream Boundaries

| Artifact | Owns | Relationship to 055 |
|---|---|---|
| **039** | the Record System constitution | hard dependency (`H: 039`); 055 applies its World-scoping of the Relationship Record |
| **044** | the architectural categories | 055 applies the Relationship test; it adds no category |
| **054** | the temporal obligation | relationship changes belong to the temporal account; 055 designs no temporal mechanism |
| **056** | the package boundary | 055 sets only the Relationship Record's scope; 056 owns packaging |
| **058** | cross-model dependency rules | not decided here |
| **079 · 080** | Registry relationship-type definition and schema | 055 names the owning-role rule; 079/080 define it |
| **197 · 198 · 199** | World Relationship Record specification, type set, schema | 055 is their boundary; row 197: *"World-only; reification criterion satisfied; owning role from Registry"* |
| **224** | back-reference and graph projection | implementation of the Derived view |
| **276 · 277 · 338 · 356 · 366** | E, P, V and I relationship architectures | each applies the criterion to its own connections |

---

*Artifact 055 · P2/2d · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the reification criterion — first-class only when no endpoint can own the
connection — and declares the Relationship Record World-only, derived from RMS §6.1 and §15,
Artifact 044, Blueprint §13.3 and §13.9, and I-102. It does not amend them, and defines no Record,
field, schema, type or mechanism. Where it differs from the Master Blueprint, the Record Model
System, or the OS File Build Roadmap, those governing sources are correct and this document is
wrong.*
