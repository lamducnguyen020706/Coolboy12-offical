# COOLBOY12 — Derived-State Discipline

**Artifact 053** · derived-state discipline · `docs/constitution/derived_state.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P2/2c · Req: BR-107 · BP: §29 · RMS: §4 · H: 050 ·
S: 020 · LS: — · G: — · → P8 · Val: derived is rebuildable and never authoritative ·
Done: discipline · Why: precedes the derived layer by six phases · Risk: high · ∥: yes

## 1. Purpose

This contract answers one question: **when is a piece of state actually Derived, and when has
authoritative or authored state been placed in a rebuildable-looking container?**

The answer, compactly restated from the sources in §3 below and adding nothing to them:

```
Derived  =  recomputable from authoritative inputs
         +  with no loss
         +  never authoritative itself
```

Each line is the Blueprint's, not this contract's: P-26 and I-19 give the first two, Blueprint
§12.4 the third. The restatement is not a formula, a test procedure or an invariant.

Row 053's reason for existing now is *"precedes the derived layer by six phases"*: the discipline
is fixed at P2 so that the P6 derived-layer contracts (Artifacts 167–174) and the P8 derived layer
(Artifacts 219–230) inherit a settled rule instead of inventing one.

**This artifact adds discipline, not architecture.**

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the derived-state discipline**: what qualifies as Derived,
what never does, and what a rebuild may never lose. It is authoritative about architectural
discipline, not about the world; it is not World Canon, not a Record, and holds no canonical data.

It creates no Record Model — there is no Derived Record Model and no seventh model — and no Record,
Kind, field, class or invariant. It derives the discipline from the Master Blueprint and the Record
Model System; it does not amend, supersede, or outrank either. Where this document differs from the
Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those governing sources
are correct and this document is wrong.**

`Req: BR-107` is preserved exactly as the Roadmap states it. The authoritative requirement register
is not present in this repository; the requirement text is **not** reproduced and **MUST NOT** be
inferred.

**In scope.** The definition of Derived; the authored-state firewall; the no-loss test as a
classification test; the boundaries Derived ≠ AUTHORITATIVE, ≠ CACHED, ≠ Record, ≠ external
holder of meaning; that the discipline is shared while derived semantics stay model-owned.

**Out of scope.** Source-of-truth classification itself (Artifact 050); the rebuild convention
(Artifact 020); the derived-layer architecture (Artifact 167); indexes, projections, views, caches,
the rebuild contract and staleness (Artifacts 158, 168–173); the P6 proof (Artifact 174); every
implementation (Artifacts 219–230). §15 below states each boundary.

## 3. The Derived-State Core Rule

> **Derived state is exactly what can be recomputed from its authoritative inputs with no loss,
> and it is never authoritative. State that cannot be so recomputed is not Derived — it was
> misfiled — and state that records an authorial act is never Derived.**

Every clause is a source's:

| Clause | Source, verbatim |
|---|---|
| Recomputable with no loss | P-26: *"Derived state is exactly and only what can be recomputed from Canon, Production State, and history with no loss."* |
| Otherwise misfiled | I-19: *"Derived state is exactly what can be recomputed with no loss; if it cannot be, it was misfiled."* |
| Never authoritative | §12.4, Derived row: *"Never authoritative; if it disagrees with canon, it is wrong."* |
| Authorial acts are not Derived | I-18: *"Any state recording an authorial act is Production State and survives every rebuild."* |
| The cost of getting it wrong | P-26: *"Filing authored state as derived is data loss with a delay."* |

**No loss** means no semantic information loss: nothing the deleted representation held may be
absent from what its authoritative inputs can reproduce. A representation that is *usually*,
*approximately* or *mostly* recomputable is not recomputable with no loss.

## 4. Source-of-Truth Classification Boundary

**Artifact 050 owns source-of-truth classification.** This contract depends on it (`H: 050`) and
does not replace, restate or re-implement it.

```
050  source-of-truth classification   — which class a data class carries; exactly one of five
  ↓
053  derived-state discipline          ← this contract: what must be true when that class is DERIVED
  ↓
167  derived-layer architecture        — how Derived artifacts are built, declared and held
```

050's own module records the split: *"This module may say a value is DERIVED. Whether it really is
— whether it can be rebuilt with no loss — is 053's question and the rebuild drill's (§29.8)."*

The five classes are Blueprint §29.6a's, and their meanings are quoted here only so the Derived
boundary can be drawn. This contract does not redefine them, add a sixth, or rank them.

| Class | §29.6a meaning, verbatim | Why it matters to the Derived boundary |
|---|---|---|
| **AUTHORITATIVE** | *"This is where the fact lives."* | A Derived value's inputs; never its output (§8 below). |
| **DERIVED** | *"Recomputable with no loss from authoritative sources."* | The class this contract disciplines. |
| **CACHED** | *"Recomputable and disposable, held only for speed."* | Also recomputable, and still not DERIVED (§9 below). |
| **TEMPORARY** | *"Exists within one workflow and does not outlive it."* | Working state, not Derived, and not authored Production State. |
| **EXTERNAL** | *"Lives outside coolboy12 entirely."* | Not a store coolboy12 runs; such stores are DERIVED or CACHED (§11 below). |

§29.6a fixes where a class comes from: *"the classification is part of its definition rather than
a property of how it happens to be stored."* A value is not Derived because it sits in `derived/**`,
in an index, or in a projection, and it is not AUTHORITATIVE because it sits in `canon/**`. The
Roadmap's per-directory table sets what each zone may hold — for `derived/**`, class DERIVED and
prohibited *"anything unrebuildable"* — which constrains placement; placing a value there does not
make it Derived.

The Roadmap also uses `DEV-ENV`, in its artifact metadata and its per-directory table, for
repository and implementation artifacts. This contract does not treat `DEV-ENV` as a sixth runtime
or data source-of-truth class; the five data classes remain those Blueprint §29.6a defines.

## 5. Authored State Is Not Derived

### 5.1 The rule

P-26 names the protected state: *"Any state that records an authorial act — a dismissal, a
deferral, a schedule, a plan, a preference — is Production State (Section 12.4): durable,
provenanced, and never destroyed by a rebuild."*

Blueprint §9.1 gives the reason the rule exists. Such state is *"not a fact about the world and
cannot be recomputed"*, and *"filing it as Derived destroys it the first time a projection is
rebuilt."* Its Production State row lists *"arcs, schedules, opportunity dispositions, debt
ledgers, style guides, workflow state, standards configuration"*, with the rule *"never destroyed
by a rebuild, never authoritative about the world"*. §12.4's Production row: *"Never rebuilt,
never inferred, never canon."*

**Filing authored state as Derived is data loss with a delay.** No wording in this contract
softens that. The constitutional point is narrower than a definition of rebuilding: any rebuild
operation that regenerates or discards Derived representations must not destroy authored
Production State. This contract does not define the taxonomy or mechanics of rebuild operations.

### 5.2 Contents may be Derived; dispositions never are

Blueprint §16.5 draws the line inside a single surface: *"The queue's contents are discovered from
canon and are therefore Derived — rebuildable, disposable, recomputed whenever the world moves.
Its dispositions are authored and are therefore Production State"*. Filing the dispositions as
Derived *"means the first queue rebuild silently discards years of authorial judgment"*.

The same line runs through every surface that shows authored state: **a Derived representation
may display an authorial act; it may never be that act's only record.**

### 5.3 The decision test

Applied to any state declared DERIVED. The test does not assign classes — the class is declared in
the data class's definition (§29.6a) and its value is validated by Artifact 050 — and it does not
choose which Record Model an authoritative value belongs to.

```
Q1  Does the state record an authorial act — a decision about making the work?
      YES → Production State: durable, provenanced, survives every rebuild. NOT Derived.
      NO  ↓
Q2  Does it live outside coolboy12 entirely, or exist only within one workflow?
      YES → EXTERNAL or TEMPORARY. NOT Derived.
      NO  ↓
Q3  Can it be recomputed from authoritative inputs with no loss?
      NO  → NOT Derived. It was misfiled (I-19): it holds something that lives only there.
            Identify the authoritative home that must hold it.
      YES ↓
Q4  Is it held only for speed?
      YES → CACHED. Recomputable, and still not Derived (§9 below).
      NO  → the DERIVED declaration survives this test.
```

Q1 comes first so that no later question can route authored state away from Production State:
workflow state, which Blueprint §9.1 lists as Production State, is settled at Q1 before Q2 asks
about workflows.

A DERIVED declaration stopped at Q1 or Q3 is a **classification failure**, not an operational
one. At Q3, Blueprint §9.1 names the case P-26 exists for — *"If it cannot be, it is Production
State that was misfiled"* — and §29.6a states the general form: *"A `DERIVED` value that cannot
actually be rebuilt is a misfiled `AUTHORITATIVE` value (P-26)"*. The two agree: §29.6a lists
*"Production State about the plan"* among its AUTHORITATIVE entries. Which authoritative home a
misfiled value belongs in is decided by the Record Model concerned, not here.

Working state — *"Drafts, proposals, simulation deltas, emergent seeds"* (Blueprint §9.1) — is
neither Production State nor Derived. §29.6a places it in TEMPORARY.

## 6. What Counts as Derived

The sources name Derived things by example. None of these lists is a Kind roster.

| Source | Named as Derived |
|---|---|
| Blueprint §9.1 | *"Indexes, dashboards, timelines, projections, published output."* |
| Blueprint §12.4 | adds **relationship back-references** |
| Blueprint §29.6a | *"Indexes · search projections · graph projections · analytics · materialised views · generated publication projections · relationship back-references"* |
| RMS §4 | indexing: *"Never authoritative; indexes are derived"* |
| RMS §6.1 | **Projection** — *"Derived, rebuildable output"*, *"Never authoritative (§29.6a)"* |

What makes each Derived is not its name. **An index, projection, view or analytic is Derived only
while it passes §5.3 above.** A store called an index that has acquired one authored value is not
Derived: §29.8 describes exactly that drift — *"A store acquires one authored value, then a
second, and remains nominally derived for years until the day it is deleted and something is
missing."*

## 7. Rebuildability and the No-Loss Test

### 7.1 The test

> **If the Derived representation is deleted, can the same semantic result be reconstructed from
> its authoritative inputs without needing anything that existed only in the deleted
> representation?**

**NO** means the deleted representation held information that was not Derived. The classification
was wrong, and was wrong before the deletion: the deletion only revealed it. This is what §29.8
means by *"If the rebuild does not complete, the deleted store was not derived"* and by *"Failure
is a finding, not a catastrophe."*

§26.2d gives the same test for stores: *"A store that cannot be deleted and rebuilt has become part
of the canon whether or not anyone intended it."*

### 7.2 What a successful rebuild shows — and what it does not

A successful delete-and-rebuild demonstrates, under the applicable rebuild contract, that the
representation can be reconstructed without relying on information that existed only in the
deleted representation. It is evidence of conformance, not more: it does not make the result
authoritative, does not establish that it is fresh, and does not by itself distinguish DERIVED
from CACHED. A rebuild that does not complete remains what §29.8 says it is — a finding that the
deleted store was not derived.

The evidence has to be produced, not assumed. §29.6a: *"the way to find out is to rebuild it on a
schedule rather than to assume."* §29.8: *"A derived store that has never been deleted is a store
whose classification is an assumption."* This contract runs nothing; the drill and the engine are
downstream (§15 below).

Artifact 020 owns the rebuild convention, including the requirement to declare a rebuild method.
Artifact 167 owns the concrete SOURCE declaration and derived-layer contract. Artifact 172 owns the
full rebuild contract. This contract establishes none of those mechanisms; it establishes the
constitutional meaning of Derived and the no-loss requirement.

### 7.3 Source condition recorded, not resolved — the inputs of a rebuild

The sources state the inputs of Derived state in two forms:

| Form | Source |
|---|---|
| *"Canon, Production State, and history"* | P-26; likewise Blueprint §9.1 and §12.4 |
| *"canonical records alone"* | §29.8 drill; Roadmap rows 172 and 226 read *"full rebuild from canon alone"* |

The two formulations are not identical on their face: P-26 names Production State among the
inputs, and Production State is never canonical (RMS §9.2). This contract records both and does not
resolve the operational relationship between them. It takes P-26 — a named principle, restated as
I-19 — as the conceptual definition of Derived, and notes that §29.8 describes itself as an
operational drill; it does not decide what a full rebuild may read. **Artifact 172 owns the full
rebuild contract** and must preserve the governing-source relationship rather than silently collapse
one formulation into the other. The P8 implementation and the P18 drills are further downstream. No
mechanism is introduced here.

## 8. Derived ≠ Authoritative

```
DERIVED  →  never authoritative
```

A Derived artifact may summarize, index, project, materialize, accelerate retrieval, expose a
shaped view, compute an analytic, or provide a back-reference. **None of these makes it
authoritative.** The authoritative source stays upstream.

| A Derived value is not made authoritative by being… | Source |
|---|---|
| stored | §13.7c: *"a projection does not become authoritative by being stored"* |
| indexed | RMS §4: *"Never authoritative; indexes are derived"* |
| consulted, however often, as though it were the record | §12.11: *"A capability that reads a back-reference as though it were the record is making a Derived source authoritative, which is the failure P-26 exists to catch."* |
| cached | RMS §9.1: *"cached ≠ authoritative"* |
| generated automatically, or the most recent thing available | §12.4: *"Never authoritative; if it disagrees with canon, it is wrong."* · Artifact 020 §10 |
| consumed by a surface | Roadmap row 170 Val: *"views are shaped for surfaces, never for canon"* |
| held by an external system | §26.2d: *"There is no configuration in which one is `AUTHORITATIVE`."* |

**Disagreement.** §12.4 states the canon case: if a Derived value disagrees with canon, *"it is
wrong"*; §12.11 calls a projection *"wrong-by-definition when it disagrees with canon"*. Because
Derived is never authoritative, it cannot prevail over any authoritative input it is computed from:
the authoritative source wins and the Derived value is wrong or stale. I-26 allows that *"derived
recomputation may be eventual and is stale-marked"*; how staleness is marked and propagated is
Artifacts 158 and 173's, not this contract's. The Roadmap forbids the reverse edge outright:
`derived → authoritative` (PART II §2.4).

**Three words, three meanings.** None collapses into another.

| Term | Meaning | Owner |
|---|---|---|
| `AUTHORITATIVE` | a source-of-truth class: where a fact lives | Blueprint §29.6a; Artifact 050 |
| `Auth: governing` | an artifact metadata value: the document's governance role | Artifact 003 |
| Authority | the constitutional Authority and domain-scoped authority | Artifact 051 |

Derived is none of the three. This contract restates none of 051.

**Not extended here.** §29.6a rules that *"nothing in the `CACHED`, `TEMPORARY`, or `EXTERNAL`
classes may ever premise a canonical commit."* The rule does not name DERIVED. This contract
neither extends it to DERIVED nor reads the omission as permission; what may premise a canonical
commit belongs to the mutation path (Artifacts 145–166).

## 9. Derived ≠ Cached

### 9.1 The distinction

Both are recomputable. **Recomputability alone therefore cannot tell them apart**, and treating it
as sufficient would turn every cache into Derived state.

| | DERIVED | CACHED |
|---|---|---|
| §29.6a meaning | *"Recomputable with no loss from authoritative sources."* | *"Recomputable and disposable, held only for speed."* |
| §29.6a examples | indexes, projections, analytics, materialised views, back-references | *"Query results · rendering caches · asset-processing caches"* |
| Concrete architecture | governed downstream by the derived-layer and rebuild contracts (Artifacts 167, 172) | governed downstream by the cache contract (Artifact 171) |
| Authoritative? | never | never — RMS §9.1: *"cached ≠ authoritative"* |

What §29.6a gives CACHED and not DERIVED is the purpose clause: *held only for speed*. A cache is
there to make something faster and may be discarded for that reason alone. A Derived artifact is
not defined by speed, and must still pass the no-loss test. Which class a data class carries is
declared in its definition and validated by Artifact 050. **Derived = Cache** is a prohibited
collapse (§14 below). This contract defines no cache architecture; Artifact 171 does.

### 9.2 Source condition recorded, not resolved — the drill's word *derived*

§29.8's drill deletes *"every derived store"* and lists among them *"every rendering cache"*;
§29.6a classifies rendering caches as CACHED. This contract does not read §29.8 as reclassifying
rendering caches as DERIVED, nor as excluding CACHED stores from the drill. Carrying the drill's
scope falls to the rebuild contract (Artifact 172), the rebuild engine (Artifact 226) and the P18
drills (Artifacts 472, 473), not to this contract.

## 10. Derived ≠ Record

Derived is a source-of-truth discipline, not a Record Model and not a semantic object type.

- RMS §6.1 separates the categories. A **Record** is *"A persistent, identity-bearing unit owned by
  exactly one Record Model"*; a **Projection** is *"Derived, rebuildable output"*.
- RMS §9.1: *"Derived/rebuildable output → not an authoritative Record"*.
- RMS §4 prohibits a Universal Record Base, a universal lifecycle, a universal state model and a
  universal semantic schema; Blueprint §13 repeats the first two.

A Derived artifact may reference, read or project Records. This contract establishes **no universal
Derived Record, no universal Derived Kind, no universal Derived lifecycle, and no universal Derived
schema.**

**Words that look alike.** Three neighbouring terms are not this contract's DERIVED:

| Term | Meaning | Owner |
|---|---|---|
| World field mutation class *derived* | one of *"locked / world-state / derived"* — *"a World classification, not a universal state model"* | RMS §7; the World Record Model |
| `derivation` | identity operations | Artifact 049 |
| *visual derivation* | one visual asset's descent from another | Artifact 049; the Visual Record Model |

## 11. External-System Boundary

§29.6a states the rule that makes the classification worth having: *"an external system must never
be the only place where a canonical semantic exists. If deleting a component would lose a meaning
rather than a convenience, that meaning was misfiled"*.

I-84 fixes the class of every external store: *"Every external store is DERIVED or CACHED, never
AUTHORITATIVE, and the system remains fully recoverable if it is deleted."* §26.2d fixes the
direction — canonical records to builder to external store, *"and never"* external store to canon
— and the test: *"The system must remain fully recoverable if the external store is deleted."*

An external store is therefore a place the Derived discipline applies, not an exception to it. It
may hold projections, indexes, caches and operational convenience. It may never be the only holder
of a semantic, and the no-loss test (§7 above) is how that is verified. **An external store is not
the EXTERNAL class**: EXTERNAL is what lives outside coolboy12 entirely; a store coolboy12 builds
and runs is DERIVED or CACHED. This contract designs no adapter and no external store.

## 12. Model Sovereignty

This contract is cross-model (`RM: all`) because source-of-truth classification is constitutional:
RMS §4 lists it among the universal mechanisms, marked *"Constitutional"*. The discipline is
shared; derived semantics are not.

```
shared discipline  ≠  shared model semantics
```

- **I-103.** *"Shared infrastructure never confers shared meaning."* The no-loss test is shared;
  what a model's Derived output means is not.
- **§13.7c.** *"each Record Model owns the meaning of its own authoritative state"* — and so which
  authoritative inputs its Derived artifacts read.
- **I-101.** No Record Model is a template for another. World's back-reference projection (§12.11)
  is World's; it is not the pattern for other models' Derived state.

The models already apply the discipline in their own terms, and those applications stay theirs:
RMS §9.1 makes Context *"a DERIVED PRODUCTION ARTIFACT"*; RMS §11.1 rules that *"A rebuildable
derivative is a derived projection. A durable derivative requiring identity becomes a VISUAL-ASSET
with subtype and provenance."* This contract implies no universal Derived semantic model, no
universal package, no universal Record schema, and no model as template.

## 13. Worked Examples

**Every example below is illustrative and non-normative.** Names are invented. No example defines a
schema, field, structure or mechanism.

| | Authoritative | Candidate | Verdict |
|---|---|---|---|
| **A** back-reference | *Character A LOVES Character B*, stored in the owning endpoint's Relationship Record — A's, say (World) | B's view: *loved by Character A* | **Derived.** Rebuildable from the owning Relationship Record (§12.11). Reading it as the record is the failure P-26 exists to catch. |
| **B** index | the Records of Characters A, B and C | an index of Characters by name | **Derived.** Deleting it loses no Character; it is rebuilt by re-indexing. |
| **C** analytic | the ARC and THREAD records (Production State) and the World Records they reference | *number of open threads by arc* | **Derived**, and recomputable from Canon and Production State — the case §7.3 above records. |
| **D** dismissal | the author dismisses an opportunity | — | **Production State, NOT Derived.** An authorial act; survives every rebuild (§16.5; I-18). |
| **E** schedule | the author schedules a fact to be revealed in Issue 14 | a calendar view of upcoming reveals | **The decision is Production State; the calendar view may be Derived.** The view is rebuilt from the schedule; the schedule is never rebuilt from the view. |
| **F** rendering | the inputs to query Q | a stored render of Q's result | **CACHED**, not automatically Derived: held for speed and regenerated on demand. A durable image requiring identity is a different thing — a VISUAL-ASSET in V (RMS §11.1). |

## 14. Explicit Prohibitions

1. Treating authored Production State as Derived.
2. Treating an authoritative fact as Derived because it is stored in a projection, index or view.
3. Making a Derived artifact the only surviving copy of a semantic fact.
4. Using a Derived artifact as authority when the authoritative source disagrees.
5. Creating a universal Derived Record type.
6. Creating a universal Derived lifecycle.
7. Creating a universal Derived schema.
8. Creating a universal derived manager or engine as a constitutional primitive.
9. Letting an external component become the sole holder of a semantic.
10. Using this contract to define indexes, projections, views, caches or a rebuild runtime.
11. Treating recomputability alone as sufficient to distinguish DERIVED from CACHED.
12. Storing an authorial act only in a Derived representation.
13. Rebuilding authored state from a Derived representation of itself.
14. Classifying a value by its location — `derived/**`, an index, an external store — rather than
    by its definition.
15. The collapse **Derived = Cache**.
16. The collapse **Derived = non-canonical.** Non-canonical is not Derived: Production State and
    Issue records are never canonical and are AUTHORITATIVE (§29.6a; Artifact 052). The
    distinctions that matter are source-of-truth class and rebuildability.

## 15. Dependency and Ownership

| Artifact | Owns | Relationship to 053 |
|---|---|---|
| **050** `src/coolboy12/kernel/sot.py` | source-of-truth classification: exactly one of five classes | hard dependency (`H: 050`); 053 does not replace, redefine or duplicate it, and adds no second source-of-truth system |
| **020** `docs/conventions/rebuild.md` | the rebuild convention; the rebuild-method declaration — row 020 Val *"every derived thing declares a rebuild method"* | soft dependency (`S: 020`); 053 fixes what qualifies as Derived and what a rebuild may never lose, and restates none of 020 |
| **051 · 052** | authority · canonicality | separate questions; 053 decides neither |
| **048 · 049** | provenance meaning · temporal terms | 053 defines neither; §10 above cites 049 only to keep its terms apart |
| **158** `docs/constitution/stale_derived.md` | stale-derived-state policy | downstream; names 053 as a hard dependency |
| **167** `docs/constitution/derived_layer.md` | derived-layer architecture; the concrete SOURCE declaration — Val *"every derived artifact declares SOURCE"*, Done *"six-field contract"* | downstream; names 053 as a hard dependency |
| **168 · 169 · 170 · 171** | index · projection · view · cache contracts | downstream applications of this discipline |
| **172** `docs/constitution/rebuild_contract.md` | the full rebuild contract | downstream; carries the source condition of §7.3 above |
| **173** `docs/constitution/staleness.md` | staleness propagation | downstream |
| **174** `tests/conformance/p6.py` | proof of the P6 contracts, gate `exit-P6` | downstream |
| **219–230** | the P8 derived layer: engine, rebuild, staleness, validator, proof | downstream (row 053 `→ P8`) |
| **472 · 473** `docs/drills/` | the P18 clean-rebuild and derived deletion/rebuild drills | downstream; they specify drills of the kind §29.8 describes |

```
050  Source-of-Truth Classification
  ↓
053  Derived-State Discipline          ← this contract
  ↓
167  Derived-Layer Architecture
  ↓
168–173  Concrete Derived Contracts
  ↓
174  P6 Proof
```

053 states the constitutional rule. 167 owns the architecture, 172 the full rebuild contract, 173
staleness propagation, and 174 the proof. None of them exists, and none is implemented here.

## 16. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number.

| ID | Condition | Source |
|---|---|---|
| **C-053-01** | Derived state is recomputable from authoritative inputs with no loss. | P-26; I-19; §29.6a |
| **C-053-02** | Any state recording an authorial act is Production State, never Derived. | P-26; I-18 |
| **C-053-03** | Such state survives every rebuild; no rebuild destroys it. | I-18; Blueprint §9.1 |
| **C-053-04** | Derived state is never authoritative; where it disagrees with an authoritative source, the source prevails and the Derived value is wrong or stale. | §12.4; §12.11 |
| **C-053-05** | No Derived representation is the only place a semantic fact exists. | §29.6a; I-84 |
| **C-053-06** | A DERIVED value that cannot be recomputed with no loss is a classification defect — misfiled — not an operational fault. | §29.6a; §29.8; I-19 |
| **C-053-07** | A DERIVED classification is demonstrated by deleting and rebuilding, not assumed; the rebuild contract and the drills that do so are downstream, not this contract's. | §29.6a; §29.8; Roadmap rows 172, 472–473 |
| **C-053-08** | Recomputable, disposable state held only for speed is CACHED, not thereby Derived. | §29.6a |
| **C-053-09** | No Derived value becomes authoritative by being stored, indexed, consulted, cached, generated, consumed by a surface or held externally. | §13.7c; §12.11; Roadmap PART II §2.4 |
| **C-053-10** | Every external store is DERIVED or CACHED, and none is the sole holder of a semantic. | §26.2d; I-84 |
| **C-053-11** | Artifact 050 remains the owner of source-of-truth classification; the five classes are not redefined and no sixth is added. | Roadmap row 053 `H: 050`; RMS §4 |
| **C-053-12** | No universal Derived Record, Kind, schema, lifecycle or engine is created. | RMS §4, §6.1; Blueprint §13 |
| **C-053-13** | Model-specific derived semantics remain with the owning Record Model. | I-101; I-103; §13.7c |
| **C-053-14** | The collapses Derived = Cache and Derived = non-canonical are refused. | §29.6a; Artifact 052 |
| **C-053-15** | No P6 or P8 architecture is defined; 158, 167–174, 219–230 and the drills 472–473 remain downstream. | Roadmap rows 158, 167–174, 219–230, 472–473 |
| **C-053-16** | The rebuild-input formulations (§7.3 above) and the drill's rendering-cache wording (§9.2 above) are recorded for downstream handling, not constitutionally resolved here. | Roadmap rows 172, 226, 472–473 |
| **C-053-17** | The document contains no executable content, defines no runtime component, and mints no Record, Kind, field, class or invariant. | Roadmap row 053 `T: doc` |

A construction satisfying all seventeen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 17. Source Traceability

| Rule | Source |
|---|---|
| Four classes of state; Derived recomputable from Canon + Production State + history | Blueprint §9.1 |
| Authored state is not Derived; filing it so is data loss with a delay | P-26 |
| Authorial acts are Production State and survive every rebuild | P-26; I-18; Blueprint §9.1 |
| Derived is recomputable with no loss; otherwise misfiled | P-26; I-19 |
| Derived is never authoritative; wrong when it disagrees with canon | Blueprint §12.4, §12.11 |
| Queue contents Derived; dispositions Production State | Blueprint §16.5 |
| Source-of-truth taxonomy; class is part of the definition, not the storage | Blueprint §29.6a; RMS §4; Artifact 050 |
| A DERIVED value that cannot be rebuilt is a misfiled AUTHORITATIVE value | Blueprint §29.6a |
| External system never the only place a canonical semantic exists | Blueprint §29.6a; I-84 |
| Every external store DERIVED or CACHED; recoverable if deleted | Blueprint §26.2d; I-84 |
| Rebuild drill; failure is a finding | Blueprint §29.8 |
| A projection does not become authoritative by being stored | Blueprint §13.7c |
| Staleness is eventual and marked | I-26 |
| Projection is a category distinct from Record | RMS §6.1 |
| Derived output is not an authoritative Record | RMS §9.1 |
| No universal Record base, lifecycle, state model or semantic schema | RMS §4; Blueprint §13 |
| Model sovereignty; no model a template | I-101; Blueprint §13 |
| Shared infrastructure does not create shared semantics | I-103 |
| Each model owns the meaning of its own authoritative state | Blueprint §13.7c |
| Model-owned applications: Context; visual derivative | RMS §9.1, §11.1 |
| World field mutation class *derived* is World's | RMS §7 |
| `derivation` and *visual derivation* | Artifact 049 |
| Forbidden edge `derived → authoritative` | Roadmap PART II §2.4 |
| Rebuild convention; rebuild-method declaration | Artifact 020; Roadmap row 020 |
| Concrete SOURCE declaration; derived-layer architecture | Artifact 167; Roadmap row 167 |
| Full rebuild contract | Artifact 172; Roadmap row 172 |
| Hard dependency on 050; soft dependency on 020; unlocks P8 | Roadmap row 053 |
| P6 derived-layer contracts, P8 derived layer and P18 rebuild drills downstream | Roadmap rows 158, 167–174, 219–230, 472–473 |
| Inputs stated two ways — recorded, not resolved | P-26; Blueprint §9.1, §12.4, §29.8; Roadmap rows 172, 226 |
| The drill's *derived store* includes rendering caches — recorded, not resolved | Blueprint §29.8, §29.6a |
| `DEV-ENV` used for repository and implementation artifacts, not as a data class | Roadmap §0.6, PART I; Blueprint §29.6a |

## 18. What This Contract Does Not Define

1. Artifact 050's implementation.
2. A rebuild engine or its implementation.
3. Derived artifact schemas.
4. The SOURCE metadata of the P6 derived-layer contract.
5. Index architecture.
6. Projection architecture.
7. View architecture.
8. Cache architecture.
9. Staleness marking or propagation mechanics.
10. Storage architecture, zones or layout.
11. Runtime APIs, services or managers.
12. Per-model derived semantics beyond the constitutional discipline.
13. Any universal Record type.
14. Any universal lifecycle or state machine.
15. Any new domain, primitive or Record Model.
16. Any canonicality semantics (Artifact 052).
17. Any authority ceremony (Artifact 051).
18. Any provenance semantics (Artifacts 047, 048).

**This artifact adds discipline, not architecture.**

---

*Artifact 053 · P2/2c · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the derived-state discipline — what is Derived, what never is, and what no rebuild
may lose — derived from Master Blueprint P-26, §9.1, §12.4, §29.6a and §29.8, and RMS §4. It does
not amend them. It is not a Record, holds no canonical data, and defines no layer, store, schema,
engine or lifecycle. Where it differs from the Master Blueprint, the Record Model System, or the OS
File Build Roadmap, those governing sources are correct and this document is wrong.*
