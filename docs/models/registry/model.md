# COOLBOY12 — Registry Record Model Specification

**Artifact 060** · Registry Record Model specification · `docs/models/registry/model.md` ·
Own: R · RM: R · T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P3/3a · Req: RR-15 · BP: §9.4 · RMS: §10 · H: 032,039,056 · S: 040 · LS: — · G: — ·
→ 061–124, all models · Val: sovereign model; definitions are **Records**; not
runtime/config/catalog/lookup · Done: sovereignty + boundaries · Why: every model resolves
definitions here · Risk: CRITICAL HINGE · ∥: no

| | |
|---|---|
| Model | **R** — Registry |
| Partition | **R** |
| Semantic question | *What does the system mean, and how are Record semantics defined?* |
| Status | Registry Record Model specification — succeeds the Artifact 040 stub at this path |

## 1. Purpose

This specification answers one question: **what is the Registry Record Model, what semantic
domain does it own, what are its Records, and what constitutional boundaries keep it from becoming
runtime infrastructure or a super-model over the other five?**

The answer, compactly, from the sources cited throughout:

> **Registry is one of six sovereign Record Models. Its Records are semantic-definition Records.
> It governs definitions; each Record Model owns its Records.** (RMS §10, §30; Blueprint §13.6e;
> I-105)

One example carries the whole boundary. A Registry Record may define what the World Kind
`CHARACTER` means. The Character `W-CH-<ordinal>-Maximus` is a World Record. Registry governs the
definition of `CHARACTER`; it never owns Maximus because Maximus is a Record of that Kind, and it
never adjudicates what is true of him (Blueprint §9.4, §13.6e; I-88).

**Succession.** Roadmap rows 040 and 060 share this path. Artifact 060 replaces the Artifact 040
Registry identity stub in place; §3 carries forward every identity fact 040 established.

## 2. Constitutional Status

| | |
|---|---|
| Role | `R: ARCH` — the architecture of one Record Model (row 060) |
| Source-of-truth class | `AUTHORITATIVE` about Registry architecture |
| Canon | `n/a` (row 060). This document is **not a Registry Record**, holds no Registry data, and is not canonical about meaning |
| Hard dependencies | **032** bootstrap flow · **039** Record System constitution · **056** package boundary |
| Soft dependency | **040** — the identity stub this document succeeds |
| Unlocks | 061–124, and every model that resolves definitions (row 060 `→`) |

This document derives the Registry model from Master Blueprint §9.4, §13.6, §13.6d, §13.6e, §13.7,
§13.7a–§13.7c and the invariants they cite, from RMS §2–§6.1, §10, §15, §19, §20 and §24, and from
the frozen P0–P2 contracts. It does not amend, supersede, or outrank any of them. Where it differs
from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources
are right and this document is wrong.**

`Req: RR-15` is reproduced from row 060. The requirement register is not in the supplied source
set, so the ID is carried forward unverified and no requirement text is stated for it (GAP-C).

An authoritative *architecture document* about Registry and canonical *Registry data* are
different things. The first is this file. The second is Registry Records, written only through
the governed path once it exists (Spine law 2; Roadmap P5).

## 3. Model Identity

The identity Artifact 040 anchored at this path is preserved without change:

- **Model:** **R** — Registry.
- **Partition:** **R**. Every Registry Record belongs to partition R, and partition R is owned by
  the Registry Record Model alone (I-16, I-101; Artifact 045).
- **Semantic question:** *"What does the system mean, and how are Record semantics defined?"*
  (RMS §6). It is the whole of what distinguishes this model from the other five.

**Registry is a peer.** RMS §2 fixes exactly six sovereign Record Models — **W** World ·
**E** Epistemic · **P** Production · **R** Registry · **V** Visual · **I** Issue — and states:
*"No model is a superclass of another. World is not a template."* Registry is not a template
either: no model inherits from it, and it inherits from none (I-101). It is not a meta-model above
the six, a seventh layer of semantic ownership, a universal base, or a global owner of Records.
Its semantic authority over definitions creates no inheritance and no ownership (I-105).

**What it shares with the other five is the mechanism layer, not semantics** (RMS §3;
Blueprint §13.7a; I-103; Artifact 043).

## 4. Semantic Domain

Blueprint §13.6e: Registry *"is the Record Model whose domain is definition and governance: it
records, defines, governs, and manages the semantic definitions the rest of the Record System
resolves against."* Blueprint §13.6 gives the same domain in two words — *"What things mean"* —
and bounds it: *"Registry owns meaning, not World Truth"*.

Registry's domain is therefore **definitions, semantic contracts, and governed system meaning**.
It is not the domain of the instances those definitions describe.

| The Registry question | The owning model's question |
|---|---|
| What does `CHARACTER` mean? | Which Character Records exist, and what is true of them? — **W** |
| What does this relationship type mean, and which role owns an edge of it? | Which edges exist between which Records, under that model's own mechanism — **the owning model** |
| What does this WSV indicator mean — type, unit, range, constraints? | What is its current value? — **W** (WSV) |
| What does this term for an epistemic state mean? | Who is in that state now? — **E** (RMS §24: *"R defines the terms; E owns the states"*) |

I-88: *"A registry definition never asserts a fact about the world, and no world record is
resolved by reading one as though it were."* RMS §24: Registry *"can never override World Truth"*.

## 5. Registry Definitions Are Records

**Registry definitions are Records.** Not pseudo-Records, configuration, enum constants, metadata
blobs, entries in a passive catalog, or runtime objects.

- RMS §10: *"Its Records are **semantic-definition Records**"*.
- I-105: *"Its definitions are Records, not configuration."*
- Blueprint §13.6e: *"A kind definition is not a constant in source code; it is a Registry Record
  with identity under the universal grammar (§13.9a), provenance, a governed change path, and a
  temporal account."*
- RMS §6.1 fixes the category: a **Definition** is *"A Registry Record specifying meaning"*, and
  its test is *"Governs; never instantiates"*.

**Why a Record Model and not infrastructure.** Blueprint §13.6: *"A Registry definition carries
meaning that canon resolves against; if it changes, canonical readings change."* Such a thing
needs identity, provenance, a temporal account, a gate, and validation — what every Record needs —
and calling it infrastructure meant it was *"governed by convention instead of by rule"*
(§13.6e).

**After bootstrap, definitions follow normal Record semantics** (RMS §10.4). They are
R-partition Records and carry the universal envelope, *"the bootstrap set and no more"*:
`partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class`
(RMS §4; Artifact 033).

**Registry's Kinds.** RMS §10.1 closes the Registry Kind taxonomy at fourteen (`FROZEN`), among
them `MODEL-DEFINITION`, `KIND-DEFINITION`, `SCHEMA-DEFINITION`, `CAPABILITY-DEFINITION`,
`CONSTRAINT-DEFINITION`, `VALIDATION-RULE` and `WSVR-INDICATOR-DEFINITION`. The roster, and each
Kind's admission against RMS §13's fourteen questions (Artifact 057), is **Artifact 064's**. This
document names Kinds only as examples of the domain and admits none.

## 6. What Registry Is Not

Row 060's `Val` names four exclusions — *runtime, config, catalog, lookup* — and the sources name
the rest. Each is a thing the Registry has been, or could be mistaken for, and is not.

| Registry is not | Why | Source |
|---|---|---|
| a **capability** | Registry is a sovereign Record Model; §9.4's *"Classification: capability"* is stale (§16) | RMS §10 (COLLISION-1); Blueprint §13.6e; I-105 |
| **runtime** | *"The Registry holds no commands and no runtime behavior."* Registry defines; runtime executes (§15) | Blueprint §9.4; RMS §10, §10.2 |
| **configuration** | definitions are Records with identity, provenance and a governed change path; a configuration file has none of them | RMS §10; I-105; Blueprint §13.6e |
| **code constants** | *"A kind definition is not a constant in source code"* | Blueprint §13.6e; RMS §10 |
| a **passive catalog** | Registry governs and manages definitions; a catalog only lists them | Blueprint §13.6e; RMS §10 |
| a **lookup table** | *"Registry is a sovereign Record Model, not a lookup table."* Resolution is a shared mechanism, not Registry work (§9) | Blueprint §13.6e, §9.4 |
| generic **metadata** or a metadata service | both sources name it as an exclusion: *"not metadata"*; *"not a metadata service"* | RMS §10; Blueprint §13.6e |
| a runtime storage abstraction for the other five | *"The Registry holds no instances."* | Blueprint §13.6e, §9.4 |
| a super-model over the other five | peer sovereignty; no model is a superclass of another | RMS §2; I-101 |
| the owner of every Record | *"never semantic ownership of another model's Records"* | I-105 |

**What it is instead.** Registry is the sovereign Record Model whose Records define the governed
meaning of the system — a model with Records, not a facility beside the models.

## 7. Definition Ownership vs Instance Ownership

> **Registry governs the definitions. Each Record Model owns its Records.** (Blueprint §13.6e;
> RMS §30)

I-105 states the same as an invariant: Registry *"holds semantic authority over definitions and
never semantic ownership of another model's Records."* Definition ownership and instance ownership
are different architectural categories (RMS §6.1: *Definition* — *"Governs; never instantiates"*;
*Record* — *"owned by exactly one Record Model"*). The detailed boundary table is **Artifact 061's**
(row 061 `Done`); this section states the rule and the examples that show it.

**Example A — Kind definition vs instance.**

```
R-<kind>-<ordinal>-<slug>      a KIND-DEFINITION for CHARACTER   Registry owns this Record
W-CH-<ordinal>-Maximus         a Character                        World owns this Record
```

Registry owns the Record that defines `CHARACTER`. World owns every `W-CH-…` Record: which exist,
what they mean in its domain, and what is true of them. The instance does not move to Registry by
being of a Kind Registry defines. *Identifiers are schematic: the Registry kind code is written
`<kind>` because the R roster's codes are Registry content not minted here (Blueprint §13.9a;
Artifact 046 §12), and no ordinal is allocated.*

**Example B — Model definition vs model.** `MODEL-DEFINITION` is a Registry Kind (RMS §10.1;
FG-V7-07 closed, RMS §27). A Registry Record defining a Record Model records governed meaning. It
does not create, own or reconstitute that model. Blueprint §9.4 lists *"model definitions"* among
the Registry content that *"extends by ordinary Registry change"*; what extends is the set of
definitions, not the set of models. RMS §2 fixes *"Exactly six sovereign Record Models"*, and
Artifact 039 §4 records that a seventh *"cannot be established by a downstream artifact"* — nor,
therefore, by a Registry Record.

**Example C — WSV meaning vs value.** RMS §10.7: `WSVR-INDICATOR-DEFINITION` is Registry-owned and
defines *"what an indicator means: type, unit, range, constraints, semantics"*; WSV is
*"World-owned singleton, one Record, current indicator values."* *"World owns current values.
Registry owns meaning."*

**The inference that must not be drawn.** Every model consumes Registry definitions; it does not
follow that Registry owns every model. Registry's definition authority confers none of the
following over another model: lifecycle authority · canonicality authority · ownership of its
Kinds' instances · ownership of its relationships · ownership of its provenance meaning · ownership
of its package composition · semantic validation authority over its Records (Blueprint §13.6e;
I-105; RMS §6; Artifacts 041, 051). **Registry definition authority is domain-scoped** (RMS §17):
authoritative about meaning, and about nothing that World, Epistemic, Production, Visual or Issue
owns.

## 8. Registry Model Responsibilities

RMS §6 gives every Record Model nine ownership dimensions; Artifact 042 states them. For Registry,
**owning a decision and specifying it here are different things.** Most of these decisions are
Registry's and are completed by later P3 artifacts, not by this one.

| Dimension (RMS §6) | Owned by Registry | What 060 establishes | Completed by |
|---|---|---|---|
| Kind taxonomy | yes | fourteen Kinds, `FROZEN` at RMS §10.1 | **064** (roster and admission rationale) |
| Identity semantics | yes | universal grammar, partition R; meaning is Registry's (§13) | no dedicated Roadmap row (§16.6); grammar recorded by **083–085**, bound by **117** |
| State and lifecycle | yes | none beyond ownership | **065** governance; **110** supersession and deprecation |
| Relationship packaging | yes | RMS §15: *"Relationship **definitions**; never runtime relationship ownership"* | **062**, **111** (dependency among definitions); **079–080** (relationship-type definitions) |
| Temporal architecture | yes | the P-18 obligation binds; the mechanism is Registry's (§14) | **108–110** |
| Provenance meaning | yes | capture is universal; meaning is Registry's (§13) | not assigned a dedicated row |
| Canonicality meaning (if any) | yes | Registry has one, about meaning (Blueprint §13.7c) | **065** (who changes a definition) |
| Semantic validation | yes | Registry's own Records only (§15) | **112**, **113**, **116** |
| Package composition | yes | ownership, and the facts of §12 | §12 records what remains open |

**Canonicality, stated only as the sources state it.** Blueprint §13.7c: Registry is canonical
*"Yes, **about meaning**"* — *"This definition is the authoritative meaning records resolve
against"* — with authority *"Registry change (§9.4)"*; Blueprint §13.6: *"Canon about meaning,
never about the world."* Artifact 052 §5.4 carries this. No canonicality mechanism, status value,
gate or ceremony is designed here, and no model's canonicality is copied to Registry.

## 9. Shared Mechanisms vs Registry Semantics

RMS §3 places a universal mechanism layer beneath all six models: identity, addressing, parsing,
resolution, structural validation, serialization, provenance capture, the Mutation Coordinator,
reference resolution, indexing, and storage/migration contracts. Registry uses these mechanisms
like every other model.

**Using a mechanism confers no semantic ownership** (I-103: *"Shared infrastructure never confers
shared meaning"*; Artifact 043). Two consequences, one in each direction:

- Registry does not become the owner of what the mechanisms carry for other models. In particular,
  *"Reference resolution is not Registry work"*: *"The Registry defines the reference field; it
  does not perform or own resolution"* (Blueprint §9.4). Resolution is mechanical and uniform;
  legality is model/Registry-owned (RMS §4; Artifact 058 §5).
- A Registry definition of a mechanism does not turn the mechanism into Registry semantics or into
  a Record. RMS §19 names *"definition management"* as Registry's model-specific capability and
  states: *"Capabilities have Registry **definitions**; that never confers modelhood."*

## 10. Reference and Dependency Boundary

RMS §10.3 (`FROZEN`) fixes the boundary at model level:

- **Registry MAY reference:** other Registry definitions · declared Record Models · declared Kinds
  · declared schemas · declared semantic contracts.
- **Registry MAY NOT:** own domain instances · depend on runtime instances · mutate domain
  instances · use domain instances as semantic authority.

> **R → R definitions = ALLOWED. R → domain instances = FORBIDDEN.** (RMS §10.3)

Referencing a *declaration* is not depending on an *instance*. A definition may name the declared
Kind `CHARACTER`; it may not reference a particular `W-CH-…` Record, or take its meaning from one.

**The dependency is asymmetric.** Blueprint §13.6e: *"The five other models depend on Registry
**for definitions**; Registry depends on them **for nothing**."* Other models consuming Registry
definitions makes Registry neither their owner nor their base. And Registry *"must not require the
complete semantic implementation of every other Record Model in order to define them"* (§13.6e):
it defines structure and meaning, which is available before a model's domain design is complete.

**Source condition recorded, not resolved — the Blueprint's older wording.** RMS §10.3 corrects
RMS v0.1's *"may never reference a kind"*. Blueprint §9.4 and §13.6e still carry the older form —
*"a Registry definition may never reference a kind, a subtype, or an instance"* — and I-75
restates it. Read literally, that forbids the declared-Kind references RMS §10.3 allows. This
document states RMS §10.3 as RMS §10.3 states it, as Artifact 058 §11 does, and does not reconcile
the two wordings. Rows 062 (*"five semantic layers; downward-only"*), 063 (the reference boundary,
whose `Val` restates RMS §10.3) and 111 (*"downward-only; asymmetric; no cycles"*) hold that
work. The sources agree on domain instances.

**Not stated here:** the reference matrix, its enforcement, and the edge rules between Registry
layers — **063**, **112** and **062**. Registry's place among cross-model edges is **058**'s.

## 11. Bootstrap Position

Artifact 032 states the order, from RMS §10.4, and this document consumes it unchanged:

```
CONSTITUTION
   ↓
BOOTSTRAP META-CONTRACT      (constitutional, not a Record)
   ↓
first Registry Record
   ↓
Registry definitions
   ↓
normal Record creation
```

- **The Bootstrap Meta-Contract is not a Record** (RMS §10.4; Artifact 031). It stands outside the
  Registry Record ontology and is not a Registry Kind.
- **The first Registry Record is a Record** (Artifact 032 §4.3).
- **Once Registry exists, its definitions follow normal Record semantics** (RMS §10.4).
- *"There is no special 'axiom Record.' There is no circular self-definition requirement."*
  (RMS §10.4). No bootstrap Record, bootstrap Record Model, or constitutional Record exists.

**Not established, and not invented here:** the first Registry Record's Kind, identity, fields and
payload. Artifact 032 §4.3 records them as *"Not established by the supplied authoritative
sources"*. This document does not assign them to `MODEL-DEFINITION`, `KIND-DEFINITION`, or any
other Kind.

**Two views, kept apart.** Blueprint §13.7 also gives a build-order view —
`Registry Kernel ↔ Record Kernel`, built together, then validation, then store and mutation.
Artifact 032 §4.6 records that no source states how that view maps onto the chain above, and
merges neither. This document does not merge them either.

## 12. Package Ownership

**Registry owns the package composition of Registry Records** (Blueprint §13.6d:
*"Registry-owned — Registry establishes its own, as the model whose Records are definitions"*;
I-107; Artifact 056 §10). That ownership covers Registry's own Records and nothing else; no Registry
package decision is a requirement for any other model (C-056-15).

What the sources establish about that package:

1. **Its unit is the Registry Record** — definitions are Records (§5).
2. **No World package component becomes Registry architecture by inheritance** (I-101, I-102). The
   Relationship Record and the History Record are World Record Model concepts, and neither may be
   required of Registry.
3. **Its relationship mechanism is relationship definitions** (RMS §15), never runtime relationship
   ownership. No Registry Relationship Record is created for symmetry.
4. **Its temporal account is Registry's own.** The P-18 obligation binds it (Artifact 054 §7.4);
   row 108's `Done` reads *"temporal account without a World History Record"*.

**§13.6d's R row is design input, not a freeze.** It reads `Record + History Record`, *no
Relationship Record*, and §13.6d marks it *"MODEL-DESIGN INPUT (not a freeze)"*: *"No downstream
artifact may treat `Record + History Record` … as a settled requirement"* (FG-V7-06; I-107;
Artifact 056 §9). This document does not adopt it as mandatory.

**Source gap recorded — the remainder of the composition.** Artifact 056 names 060 as the place
Registry's package is specified. The sources supply the four facts above and no concrete
composition beyond them: which temporal structure Registry uses is decided by 108–110, and no
source or Roadmap row fixes anything further. The remainder is **not established**; it is not
inferred by symmetry with World or with §13.6d. §13.6d fixes the bar for later change: a model
changing its own packaging makes *"a schema change at Foundational ceremony"*.

## 13. Identity and Provenance

**Identity.** Registry Records are named by the universal grammar,
`[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]`, with partition **R** (AD-1; RMS §5; I-82; Artifact 034).
The grammar is universal; its semantics are not (*"UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC
MODEL"*, RMS §5). Registry owns what an R-Record's identity means, its Kinds' meaning, and its
identity-specific constraints (RMS §5; Artifact 046). Blueprint §13.9a assigns Registry *"the
authoritative kind-code mapping"*; the grammar is recorded as a Registry definition by rows
083–085 (row 083: *"records the grammar Registry governs; does not re-decide AD-1"*). This
document re-decides nothing about AD-1 and mints no kind code.

**Provenance.** Every Registry Record carries provenance under the universal capture obligation
(Spine law 9; Artifact 047). What provenance *means* for a Registry Record is Registry's
(Blueprint §13.7b; Artifact 048). No Registry provenance schema is defined here.

## 14. Temporal and Evolution Ownership

Registry owns its temporal architecture (RMS §6, §16; I-90). The obligation is universal: a Registry
definition that changed without a record breaks P-18 as a World Record would (Blueprint §13.6d).
The mechanism is Registry's, and it is designed by **108** (evolution model), **109** (versioning
rules; *"consumers pin a version"*) and **110** (supersession and deprecation; *"deprecated ≠
deleted"*).

This document adds no History Record, version syntax, supersession mechanic or deprecation state,
and imports none of World's identity operations — supersede, split, merge and retire are World
semantics (Artifact 205).

## 15. Definition-vs-Runtime Boundary

Registry defines; runtime executes. The sources state the boundary four times, each for a
different Kind:

| Registry Record (a definition) | Not a Registry Record (runtime) | Source |
|---|---|---|
| `SCHEMA-DEFINITION` — required fields, cardinality, constraints, applicable Model and Kind | the code that validates or executes against the schema — *"Registry does not execute schemas"* | RMS §10.2 |
| `CAPABILITY-DEFINITION` — a semantic contract | `CAPABILITY-IMPLEMENTATION` — e.g. the Context Builder, the Workflow Composer, validators, the identity resolver, migration utilities | RMS §10.5 |
| `CONSTRAINT-DEFINITION` — *"a condition that must hold"*; `VALIDATION-RULE` — *"a mechanism/procedure for checking a condition"* | the runtime validators that implement validation | RMS §10.6, §20 |
| `WSVR-INDICATOR-DEFINITION`, `SIMULATION-MODEL-DEFINITION` | the current indicator value (a World Record) and the simulation that runs | RMS §10.7 |

*"Recording a capability's definition never makes that capability a Record Model"* (RMS §10.5),
and *"These are never collapsed"* (RMS §10.6). RMS §20 keeps four tiers apart: constitutional
invariant · `CONSTRAINT-DEFINITION` · `VALIDATION-RULE` · implementation validation.

**Registry's own implementation is not the Registry.** Rows 114–117 build a kernel, a resolution
service, a validation suite and an identity binding (`R: IMPL` and `R: VALID`). They operate on
Registry Records; none of them is a Registry Record, and none holds a definition's meaning.

## 16. Source Conditions Recorded

Each is recorded, not resolved, and none blocks this document.

1. **COLLISION-1 — Blueprint §9.4's classification.** §9.4 still reads *"**Classification:**
   capability (Section 29.1), owned by Canon"*. RMS §10 closes the collision `AUTHOR-DECIDED`:
   *"Registry is a sovereign Record Model"*, and the §9.4 line is *"stale and requires a Blueprint
   wording fix"* (logged as PC-1). §13.6e and I-105 already state sovereignty. This document takes
   §9.4's definition and layer concepts and not its classification, and does not modify the
   Blueprint.
2. **FG-V7-05 — bootstrap status.** Blueprint §13.6e still marks the meta-contract's ontological
   status *"OPEN"*; RMS §10.4 closes it `AUTHOR-DECIDED` (not a Record). Artifacts 031 and 032
   carry the closure (§11).
3. **FG-V7-07 — `MODEL-DEFINITION`.** Blueprint §13.6e records as OPEN whether Registry needs a
   Record Model definition Kind, and its §13.6 and §13.6e rosters list ten Registry Kinds. RMS §27
   closes FG-V7-07 — *"MODEL-DEFINITION is a Registry Kind"* — and RMS §10.1 freezes fourteen. The
   roster is **064**'s.
4. **Downward-only wording** (§10 above; Artifact 058 §11). Held by 062, 063 and 111.
5. **Roadmap definition families vs RMS §10.1.** Rows 066–107 specify families that do not map
   one-to-one onto the fourteen Kinds: `IDENTITY-DEFINITION` (083), `DERIVATION-DEFINITION` (094),
   `ROLE-BOUNDARY-DEFINITION` (101) and `DEGRADED-MODE-DEFINITION` (103) are not RMS §10.1 names.
   Rows 074–075 formerly named a `SEMANTIC-DEFINITION` family; the Roadmap's `AUTHOR-DECIDED`
   AD-LS1-R-BOOTSTRAP revision (its §0.7) repurposed them into the Registry self-Kind definition
   set contract and the concrete Kind-Definition set. Row 064's `Val` — *"exactly fourteen Kinds,
   each with admission rationale"* — is where the correspondence is settled. Not settled here.
6. **Registry identity semantics has no dedicated row.** Artifact 046 §11 records that the Roadmap
   declares identity-semantics artifacts for W, E and P only. Registry's remain Registry-owned; no
   artifact is assigned them here.
7. **Package composition beyond §12's facts** is not established (§12).

## 17. Downstream Ownership

| Artifact | Owns | 060 supplies |
|---|---|---|
| **061** | the Registry authority boundary — the boundary table | the rule: Registry governs definitions; each model owns its Records |
| **062** | the five semantic layers and their downward-only rule | that layering is Registry's, and not stated here |
| **063** | the Registry reference boundary (gates P3 exit) | RMS §10.3 at model level |
| **064** | the fourteen Kinds and each admission rationale | the count and the domain |
| **065** | governance: who may propose, approve, deprecate a definition | canonicality about meaning, stated as sourced |
| **066–107** | each definition family's specification, schema or definition | examples only |
| **108–110** | evolution, versioning, supersession and deprecation | the temporal ownership and the P-18 obligation |
| **111** | dependency direction: downward-only, asymmetric, no cycles | the asymmetry of §10 |
| **112 · 113** | the reference validator; the constraint/validation binder | the boundaries they enforce |
| **114–117** | kernel, resolution service, validation suite, identity binding | the definition-vs-runtime boundary |
| **118–123** | fixtures, worked example, unit, negative, boundary and lockstep tests | nothing executable |
| **124** | the P3 conformance suite — `exit-P3` | the model boundary it will check |

None of these is pre-implemented here: no boundary table, layer rule, reference matrix, Kind
rationale, governance process, family field list or schema, version syntax, dependency graph,
validator, service, fixture or test.

## 18. Prohibited Architectural Moves

| # | Prohibited move | Source |
|---|---|---|
| 1 | Registry classified as a capability rather than a Record Model | RMS §10 (COLLISION-1); I-105 |
| 2 | Registry as a lookup table | Blueprint §13.6e |
| 3 | Registry as configuration | RMS §10; I-105 |
| 4 | Registry as a generic metadata service or passive catalog | RMS §10; Blueprint §13.6e |
| 5 | Registry as runtime, or holding commands and runtime behaviour | Blueprint §9.4; RMS §10, §10.2 |
| 6 | Registry as a superclass, base or super-model over the other five | RMS §2; I-101 |
| 7 | Registry owning another model's Records | I-105; Blueprint §13.6e |
| 8 | Registry depending on domain or runtime instances, or using them as semantic authority | RMS §10.3 |
| 9 | Registry mutating domain instances | RMS §10.3 |
| 10 | Registry adopting World's package by inheritance | I-101; I-102; I-107; Blueprint §13.6d |
| 11 | A universal Relationship Record, or one given to Registry by symmetry | RMS §4; I-102 |
| 12 | A universal History Record, or one given to Registry by symmetry | RMS §4; I-90; I-102 |
| 13 | A universal lifecycle | RMS §4 |
| 14 | Universal canonicality, or World's canonicality copied to Registry | RMS §4; Blueprint §13.7c |
| 15 | A universal semantic schema | RMS §4 |
| 16 | The Bootstrap Meta-Contract turned into a Record or a Registry Kind | RMS §10.4 |
| 17 | A special axiom Record, or circular self-definition | RMS §10.4 |
| 18 | Registry definitions held only as code constants | Blueprint §13.6e; RMS §10 |
| 19 | Definition ownership read as instance ownership | I-105; RMS §6.1 |
| 20 | A seventh Record Model created by a Registry Record | RMS §2, §10.5; Artifact 039 §4 |
| 21 | Detailed P3 architecture frozen here ahead of its owning artifact | Roadmap rows 061–124 |

## 19. Conformance Conditions

Contract conditions, checkable against this document and against constructions built on it. They
are not invariants and mint no invariant number.

| ID | Condition | Source |
|---|---|---|
| **C-060-01** | Registry is one of exactly six sovereign Record Models, a peer of the other five. | RMS §2; I-101, I-105 |
| **C-060-02** | Every Registry Record is in partition R, and partition R is owned by the Registry Record Model. | I-16; I-101; Artifact 040 |
| **C-060-03** | Registry's semantic question is *"What does the system mean, and how are Record semantics defined?"* | RMS §6; Artifact 040 |
| **C-060-04** | Registry definitions are Records. | RMS §10; I-105; Blueprint §13.6e |
| **C-060-05** | Registry is treated as none of: runtime, configuration, catalog, lookup table, generic metadata. | Roadmap row 060 `Val`; RMS §10; Blueprint §13.6e |
| **C-060-06** | Registry definition authority never becomes ownership of another model's Records. | I-105 |
| **C-060-07** | Registry is neither a superclass of another model nor a model any other inherits from. | RMS §2; I-101 |
| **C-060-08** | No Registry Record depends on, mutates, or takes semantic authority from a domain or runtime instance. | RMS §10.3 |
| **C-060-09** | The Bootstrap Meta-Contract remains constitutional and not a Record. | RMS §10.4; Artifact 031 |
| **C-060-10** | The first Registry Record's Kind, identity, fields and payload are not asserted beyond source. | Artifact 032 §4.3 |
| **C-060-11** | Registry package composition is Registry-owned and takes no component from World by inheritance. | Blueprint §13.6d; I-107; Artifact 056 |
| **C-060-12** | Registry introduces no universal Relationship Record, History Record, lifecycle, canonicality or semantic schema. | RMS §4; I-90, I-102 |
| **C-060-13** | Authority, semantic-layer, reference, taxonomy and governance detail stays with 061–065. | Roadmap rows 061–065 |
| **C-060-14** | Definition-family detail stays with 066–107. | Roadmap rows 066–107 |
| **C-060-15** | Registry implementation stays with 114–117, and none of it is a Registry Record. | Roadmap rows 114–117; RMS §10.5 |
| **C-060-16** | The frozen P0, P1 and P2 conformance suites stay green after this same-path succession. | Artifact 004; Roadmap rows 030, 038, 059 |

A construction satisfying all sixteen conforms **to this specification**. That is not conformance
to the Registry Kernel, which rows 061–124 complete.

## 20. Completion and Handoff

| Row 060 | Where it is met |
|---|---|
| `Val`: *"sovereign model"* | §3, §6, §7, §16.1; C-060-01, C-060-07 |
| `Val`: *"definitions are **Records**"* | §5, §11; C-060-04 |
| `Val`: *"not runtime/config/catalog/lookup"* | §6, §9, §15; C-060-05, C-060-15 |
| `Done`: *"sovereignty + boundaries"* | §3–§15, §17, §18; C-060-06 to C-060-14 |

**Final statement.** Registry is the sovereign Record Model of partition R. It answers *what the
system means and how Record semantics are defined*; its Records are semantic-definition Records,
governed like any other Record after bootstrap. It governs definitions and owns no other model's
Records; it may reference definitions and declarations and never depends on, mutates, or takes
authority from a domain instance; it defines schemas, capabilities, constraints, validation rules
and indicators and executes none of them. Its taxonomy, authority table, layers, reference
contract, governance, definition families, evolution and implementation are owned by rows 061–124
and are not decided here.

---

*Artifact 060 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This document
specifies the Registry Record Model, succeeding the Artifact 040 stub at this path, derived from
Master Blueprint §9.4, §13.6, §13.6d, §13.6e, §13.7, §13.7a–§13.7c and the Record Model System §10.
It is not a Registry Record, holds no canonical data, defines no schema, and implements nothing.
Where it differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap,
those governing sources are correct and this document is wrong.*
