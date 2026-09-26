# COOLBOY12 — Canonicality Framework

**Artifact 052** · canonicality framework · `docs/constitution/canonicality.md` · Own: CONST ·
RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P2/2c · Req: BR-22 · BP: §13.7c · RMS: §17 · H: 051 · S: — · LS: — · G: — ·
→ 145, all models · Val: six meanings tabulated; P and I never canonical ·
Done: per-model meaning fixed · Why: **a universal boolean here reintroduces COM** ·
Risk: CRITICAL · ∥: no

## 1. Purpose

This artifact answers one question: **what "canonical" constitutionally means in each of the six
sovereign Record Models, and what canonicality is not.** The detailed semantics within each model
remain that model's.

Row 052 states why the answer must be fixed per model: *"a universal boolean here reintroduces
COM"* — the retired Canon Object Model, whose defining error was one canonical flag over every
object. Blueprint §13.7c is the source this contract makes operational:

> *"**Canonicality is a status property whose meaning is defined by the Record Model that has one.
> It is not a universal boolean and not a property every Record carries.**"*

This contract adds no architecture. Every rule below is a contractual formulation of what Blueprint
§13.0, §13.6, §13.6a, §13.6c and §13.7c, Spine law 5, RMS §4, §6, §8–§12 and §17, and the
invariants cited already establish.

## 2. Constitutional Scope

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the constitutional canonicality framework**: the six meanings
fixed by Blueprint §13.7c, and the boundaries that keep those meanings from being universalized. It
is not the detailed semantic owner of any model's canonicality. Each Record Model remains sovereign
over the detailed semantics and model-specific realization of canonicality within its own model,
subject to the constitutional meanings fixed here and by the governing sources (§10 below).

It derives the framework from the Master Blueprint and the Record Model System; it does not amend,
supersede, or outrank either. Where this document differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those governing sources are
correct and this document is wrong.** It is not a Record and holds no canonical data.

`Req: BR-22` is preserved exactly as the Roadmap states it. The authoritative requirement register
is not present in this repository; the requirement text is **not** reproduced and **MUST NOT** be
inferred.

**In scope.** The constitutional meaning of canonical in W, E, P, R, V and I; that P and I are
never canonical; that V is canonical by kind; what canonicality is not; that canonicality does not
cross model boundaries on its own.

**Owned by each model, not here.** The detailed semantics and realization of canonicality within
that model, subject to the meanings fixed here.

**Out of scope.** Who commits canon, and the Authority (Artifact 051); how a Record becomes
canonical in any model — its gate, ceremony, lifecycle or transitions (Artifact 145 and each model's
own contract); source-of-truth classification (Artifact 050); provenance (Artifacts 047, 048);
temporal vocabulary (Artifact 049); cross-model dependency legality (Artifact 058); schemas, fields,
storage, code and tests.

**Position.**

```
051  authority framework
  ↓
052  canonicality framework            ← this contract: what canonical MEANS, per model
  ↓
     each model's own canonicality contract
  ↓
145  canonical-gate framework          — how a model's Records BECOME canonical
```

## 3. The Canonicality Core Rule

> **Canonicality is model-defined. Each Record Model that has canonicality owns what canonical means
> for its Records; two models have none. No Record is canonical because it is a Record, because it
> is stored, because it has provenance, because it is classified `AUTHORITATIVE`, because it is
> published, or because a human or an AI made it. Canonicality does not cross a model boundary on
> its own.**

```
                         CANONICALITY
                   meaning owned per model
                              │
      ┌──────────────┬────────┼────────┬──────────────┬──────────────┐
      │              │        │        │              │              │
      W              E        R        V              P              I
   true of the   what is   meaning  by kind:      NEVER          NEVER
   world         known,    records  specification canonical     canonical
                 believed, resolve  is canonical
                 revealed  against
                 — not
                 that it
                 is true
```

## 4. Record ≠ Canon

Blueprint §13.0 names *"Three statements the blueprint must never make"*: *every Record is Canon* ·
*every Record is canonical* · *Canon = Record*. It holds the words apart:

| Term | What it is | What it is not |
|---|---|---|
| **Record** | *"The architectural unit: a persistent semantic unit owned by exactly one Record Model"* | Not a synonym for canon; not inherently canonical |
| **Canon** | *"A governance and truth concept: the committed record, and the authority that commits it"* | Not a data class; not a Record Model |
| **Canonicality** | *"A status property whose meaning is defined by each Record Model that has one"* | Not a universal boolean; not a property every Record carries |

I-104: *"Record and Canon are not synonyms. Canonicality is a status property whose meaning is
defined by each Record Model that has one, and two models hold Records that are never canonical."*

So:

- A Record is not canonical by being a Record.
- Canon is not a seventh Record Model and not a Record type. There is no canonical Record class to
  specialize, and no inheritance around canonicality (I-101).
- RMS §6 assigns each Record Model *"canonicality meaning (if any)"*. The qualifier is binding:
  canonicality is a property only of models that have one.
- **The artifact metadata field `Canon:`** records a per-artifact status (Artifact 003, field 10),
  which *"does **not** become a universal canonicality model"*. It is not a Record's canonicality.

## 5. The Six Meanings

Each meaning is Blueprint §13.7c's, verbatim, with the corroborating RMS text. How a Record comes to
be canonical is not stated for any model; see §2 above.

### 5.1 World

**Canonical.** *"This is true of the world"* (§13.7c).

A canonical World Record states what is true of the world. The Record is a unit of data; its
canonicality is the status that, in the World model, means *this is true of the world*. Canonicality
is not the Record itself, and World is one model of six: *"World Truth is what the `W` partition
holds, and it is one model of six"* (§13.6).

### 5.2 Epistemic

**Canonical.** *"This is authoritatively what is known, believed, or revealed — **not** that the
proposition is true"* (§13.7c).

Epistemic canonicality is about epistemic state, never about truth. RMS §8: *"W holds the fact; E
holds every *view* of it, possibly partial or wrong."* A canonical Epistemic Record establishes what
is known, believed or revealed — including what is believed falsely — and establishes nothing about
whether the proposition holds in the world.

### 5.3 Production

**Never canonical.** *"Production State is committed intent, never world truth"* (§13.7c). RMS §9:
*"**Canonicality: NEVER.** Production never becomes World Canon by any route."*

Never canonical does not mean unimportant, invalid or unprovenanced. RMS §9 describes Production
State as *"authored, durable, provenanced, and never rebuilt; and it is explicitly not canon about
the world."* It is committed intent (§13.7c), and it has no canonical status.

### 5.4 Registry

**Canonical, about meaning.** *"This definition is the authoritative meaning records resolve
against"* (§13.7c).

Registry canonicality is about meaning and never about the world. Blueprint §13.6: *"Canon *about
meaning*, never about the world. **Registry owns meaning, not World Truth**"*. A canonical Registry
definition fixes what records mean when they resolve against it; it establishes no fact of the
world, and confers no canonical status on the Records of other models (§8 below).

### 5.5 Visual

**By kind.** *"A specification is canonical; an asset is a manifestation; an analysis is an
observation"* (§13.7c). Visual canonicality is decided per Kind, not for the model as a whole. For
the currently frozen Visual Kinds identified by RMS §11.1:

| Visual Kind, as identified by RMS §11.1 | Canonicality | Source |
|---|---|---|
| **CANONICAL-VISUAL-SPECIFICATION** | **Canonical.** *"This carries canonical visual truth."* | RMS §11.1; Blueprint §13.6c |
| **VISUAL-ASSET** | **A manifestation.** *"An external image file never does"* carry canonical visual truth; *"Never authoritative"* | RMS §11.1; Blueprint §13.6c |
| **VISUAL-ANALYSIS** | **An observation.** *"Observation, never truth."* | Blueprint §13.6c; RMS §11.2 |

The governing principle is Blueprint §18.6: *"canonical visual identity is the description, not the
file."* (§18.6's location wording is recorded as a source inconsistency in §10 below; the principle
is unaffected.) An asset rendered from a canonical specification does not become canonical by being
rendered from it; a divergence between them *"is a continuity finding against the asset"* (§13.6c).

The Visual Kind taxonomy is RMS §11.1's. This contract introduces no Kind, ratifies none, and does
not restate the taxonomy beyond what the canonicality meaning needs.

### 5.6 Issue

**Never canonical.** *"Nothing is true because it is printed"* (§13.7c; Spine law 5). RMS §12.2:
*"**Issue never becomes World Canon.** Issue references but never owns W/E/P/V semantics."*

An Issue Record is durable publication reality. That an issue was printed is itself recorded; what
it printed is not made true by printing it. Spine law 5: published artifacts *"reference canon
one-directionally; they never become canon. *That* the magazine printed X is a fact of the world;
*whether* X is true is a separate, canon-governed question."*

## 6. The Canonicality Table

The central table of this contract. Columns two and three are Blueprint §13.7c's.

| Record Model | Canonical? | What "canonical" means there |
|---|---|---|
| **World** `W` | Yes | This is true of the world |
| **Epistemic** `E` | Yes | This is authoritatively what is known, believed, or revealed — **not** that the proposition is true |
| **Production** `P` | **Never** | Production State is committed intent, never world truth |
| **Registry** `R` | Yes, **about meaning** | This definition is the authoritative meaning records resolve against |
| **Visual** `V` | **By kind** | A specification is canonical; an asset is a manifestation; an analysis is an observation |
| **Issue** `I` | **Never** | Nothing is true because it is printed |

**What is deliberately omitted.** Blueprint §13.7c's table has a fourth column, naming what
authorizes each model's state. That column is authority, not canonicality. Artifact 051 states that
each model's authority semantics and ceremony belong to that model's own contract, and this contract
does not reproduce it.

**Why no universal boolean may carry this table.** The objection is not that a boolean cannot be
stored; it is architectural. A universal boolean would impose one shared canonicality vocabulary,
and one shared status semantics, on six models whose canonicality meanings differ — and on two
models for which canonicality does not exist as a status at all. It is also incompatible with Visual
as a model, because Visual's canonicality is decided by Kind. That is semantic universalization: the
retired Canon Object Model's error (row 052), and what Blueprint §13.7c forbids — canonicality *"is
not a universal boolean and not a property every Record carries."* §13.7c draws the same consequence
for status vocabularies: *"A `status` vocabulary admitting `CANON` in every partition would be false
in two of six"*.

## 7. Canonicality Boundaries

### 7.1 Canonicality ≠ Authority

The constitutional Authority is the one human position that commits canon (Spine law 3, Blueprint
§10.1). Canonicality is the status, defined per model, of what counts as canonical. **Authority is
not canonicality**, and the constitutional Authority is not itself a canonicality semantic.

This contract establishes no universal implication between authority or authorization and
canonicality — in either direction. It does not say that authorization makes a Record canonical,
and it does not say that authorization never does. A model-specific authorizing act may participate
in establishing canonical state under that model's own contract and canonical gate; those rules are
outside this contract, and belong to Artifact 145 and the model's own contract.

The authority framework is Artifact 051, and this contract does not restate it.

### 7.2 Canonicality ≠ Source-of-Truth Class

Artifact 050 classifies where a fact lives (§29.6a). A class is not a canonical status. Blueprint
§29.6a lists *"Production State about the plan"* and *"Issue records about the artifact"* as
`AUTHORITATIVE` — and both are never canonical (§5.3, §5.6 above). A Record may be the authoritative
source of its fact while that classification alone determines nothing about its canonicality.

### 7.3 Canonicality ≠ Provenance

Provenance answers *"Who made this, when, and why"* (Blueprint §13.7b; Artifacts 047, 048).
Canonicality answers what status a Record has in its model. Production State is *"provenanced"* and
never canonical (§5.3 above). A complete provenance establishes that an act is recorded, never that
its result is canonical.

### 7.4 Canonicality ≠ Persistence

Storing a Record does not make it canonical. Blueprint §13.7c: *"a projection does not become
authoritative by being stored"*, and *"each Record Model owns the meaning of its own authoritative
state."* Production State is *"durable"* and never canonical; an Issue is *"durable"* and never
canonical.

### 7.5 Canonicality ≠ Publication

Printing, publishing, distributing, rendering, exporting and displaying are acts on an artifact.
None confers canonicality. Spine law 5: published artifacts *"never become canon."* §13.6: *"a World
object never becomes an Issue object by being published"*. A rendered image is an asset, however
faithful to its specification (§5.5 above).

### 7.6 Canonicality ≠ Authorship

Being made by a human does not make a Record canonical, and being made by an AI does not decide the
question either way. Blueprint §9.1: working state — *"Drafts, proposals, simulation deltas,
emergent seeds"* — is *"Provisional. Never authoritative. Becomes canon only through the gate."*
Spine law 6: *"Every AI proposal, simulation delta, and emergent seed is provisional until gated."*
And Production State is authored by the author and is never canonical (§5.3 above).

### 7.7 Canonicality ≠ Version, Revision or History

The vocabulary is Artifact 049's. A latest version is not thereby a canonical version: a corrected
Issue is *"a new Issue that supersedes the previous Issue"* (RMS §12.2), and it is no more canonical
than the one it supersedes. P-17: *"History is never a second canon and never a second source of
truth."*

## 8. Cross-Model Canonicality Boundary

**Canonicality does not transfer across a Record Model boundary on its own.** A Record canonical in
one model makes nothing canonical in another. The sources state it model by model:

| From | Does not become | Source |
|---|---|---|
| Production State | World Canon — *"by any route"* | RMS §9.2 |
| An Issue | World Canon | RMS §12.2; Spine law 5 |
| A Visual analysis | World Truth — *"merely by existing"*; *"Visual never mutates World"* | RMS §11.2 |
| An Epistemic state | World truth — E→W is *"reference; mutation only via the governed path"* | RMS §8.2 |
| A Registry definition | World Truth, or ownership of another model's Records | Blueprint §13.6; I-105 |
| A canonical Visual specification | a canonical asset | Blueprint §13.6c; RMS §11.1 |

A change in another model happens only through that model's own governed path; it is never implied
by canonicality elsewhere. This contract states the boundary and designs no projection, reference or
dependency mechanism across it; cross-model dependency rules are Artifact 058's.

## 9. Explicit Prohibitions

This contract establishes none of the following, and no later artifact may cite it as having done
so:

| | Prohibited | Why |
|---|---|---|
| 1 | A universal canonical Record type or class | Blueprint §13.0, §13.7a; I-101 |
| 2 | A universal canonical boolean on Records | Blueprint §13.7c; Roadmap row 052 |
| 3 | A universal canonical enum or status vocabulary | Blueprint §13.7c |
| 4 | A universal canonical lifecycle | Blueprint §13.7a; RMS §4 |
| 5 | A universal canonical gate | Roadmap row 145 |
| 6 | A universal canonical authority over the six models | Blueprint §13.7a; Artifact 051 |
| 7 | Canonicality inferred from provenance | this contract, §7.3 |
| 8 | Canonicality inferred from source-of-truth class | this contract, §7.2 |
| 9 | Canonicality inferred from persistence | this contract, §7.4 |
| 10 | Canonicality inferred from publication | this contract, §7.5; Spine law 5 |
| 11 | Canonicality inferred from authorship | this contract, §7.6 |
| 12 | Canonicality transferred across models by default | this contract, §8 |
| 13 | Record = Canon | Blueprint §13.0; I-104 |
| 14 | Canon as a seventh Record Model | Blueprint §13.0; I-101 |
| 15 | A universal canonical service, manager or engine | Blueprint §13.7a; I-103 |
| 16 | One model's canonicality specializing, or templating, another's | I-101 |
| 17 | The Mutation Coordinator's implementation | Blueprint §12.6 |
| 18 | The Human Gate's implementation | Spine law 2; Artifact 145 |
| 19 | Authority succession or its implementation | Blueprint §10.1; Artifact 051 |
| 20 | A universal or shared storage representation of canonical status across Record Models — a common field, schema or persistence layer. Model-specific representation and storage are not prohibited; they are downstream and out of scope. | RMS §4; Blueprint §13.7a |

## 10. Dependency and Ownership

| Concern | Owner |
|---|---|
| The constitutional framework: the six meanings of §13.7c and the boundaries that keep them from being universalized | **This contract** |
| Detailed canonicality semantics and realization within one model — elaboration, permitted terminology, representation | The owning Record Model |
| How a Record becomes canonical — gate, ceremony, lifecycle, transitions | Artifact 145 and each model's own contract |
| Who commits canon; the Authority | Artifact 051 |
| Source-of-truth class | Artifact 050 |
| Provenance capture and meaning | Artifacts 047, 048 |
| Temporal vocabulary | Artifact 049 |
| Cross-model dependency legality | Artifact 058 |

This contract depends on 051 (row 052 `H: 051`) and on the earlier constitutional artifacts it
cites. It does not depend on Artifact 145 or on any model contract; they depend on it (`→ 145, all
models`).

**Two layers, not one.** This contract fixes the constitutional meanings; each Record Model remains
sovereign over the detailed semantics and model-specific realization of canonicality within its own
model, subject to those meanings and to the governing sources. A model **may** elaborate its own
canonicality. It **may not** contradict the meaning fixed here, turn a *Never* into a *Yes*, apply
another model's canonicality meaning to itself, or apply its own to another model.

**Source condition recorded, not resolved.** A source inconsistency remains in the current
Blueprint. §18.6 still contains wording that places the canonical visual specification as a World
record — it *"is a World record, gated like any other canon"* — while Blueprint §13.6c and RMS §11
(`FROZEN`) place the canonical visual specification in the Visual Record Model.

This contract records the inconsistency. It does not amend, supersede or resolve the Blueprint, and
it holds no authority to. For the six-model canonicality contract here, the Visual meaning (§5.5
above) follows the six-model placement currently established in §13.6c and RMS §11. The
inconsistency remains an upstream matter, and this artifact does not repair it.

The principle that canonical visual identity is the description — the specification — and not the
rendered asset or file (§18.6) remains applicable, and is unaffected by the inconsistency.

## 11. Conformance Conditions

Stated so they are checkable. **Artifact 059** owns the P2 kernel conformance suite; this document
implements no test and is `T: doc`. These are conditions of this contract; no invariant is minted.

| ID | Condition | Basis |
|---|---|---|
| **C-052-01** | All six Record Models have an explicit canonicality meaning. | Blueprint §13.7c |
| **C-052-02** | World canonicality means *this is true of the world*. | Blueprint §13.7c |
| **C-052-03** | Epistemic canonicality is about what is known, believed or revealed, not truth. | Blueprint §13.7c; RMS §8 |
| **C-052-04** | Production is never canonical. | Blueprint §13.7c; RMS §9.2 |
| **C-052-05** | Registry canonicality is about meaning, never about the world. | Blueprint §13.7c, §13.6 |
| **C-052-06** | Visual canonicality is by kind; of the Kinds RMS §11.1 identifies, the specification is canonical. | Blueprint §13.7c, §13.6c; RMS §11.1 |
| **C-052-07** | Issue is never canonical. | Blueprint §13.7c; RMS §12.2; Spine law 5 |
| **C-052-08** | Record ≠ Canon. | Blueprint §13.0; I-104 |
| **C-052-09** | Canonicality is not a property every Record carries. | Blueprint §13.7c; RMS §6 |
| **C-052-10** | No universal canonical boolean, enum, status vocabulary, field or shared storage representation is established. | Blueprint §13.7c; Roadmap row 052 |
| **C-052-11** | Canonicality does not transfer across Record Model boundaries on its own. | RMS §§8.2, 9.2, 11.2, 12.2; I-105 |
| **C-052-12** | Authority remains Artifact 051's. | Roadmap row 052 `H: 051` |
| **C-052-13** | Source-of-truth class remains Artifact 050's and does not determine canonicality. | Blueprint §29.6a |
| **C-052-14** | Provenance remains Artifacts 047 and 048's and does not determine canonicality. | Blueprint §13.7b |
| **C-052-15** | No canonical gate, lifecycle or transition is defined. | Roadmap row 145 |
| **C-052-16** | No Record Model is a specialization or template of another. | I-101 |
| **C-052-17** | The document contains no executable content and mints no Record, Kind, field or invariant. | Roadmap row 052 `T: doc` |

A construction satisfying all seventeen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 12. Worked Examples

**Every example below is illustrative and non-normative.** Names are invented. No example defines a
structure, field, gate or mechanism.

| Model | Example Record | What its canonicality means — and does not |
|---|---|---|
| **W** | *The capital of Kingdom A is City B.* | If canonical: true of the world. |
| **E** | *Archivist C believes the capital is City B.* | If canonical: that is authoritatively what C believes. Not that it is true — C may be wrong about the world, and that would not make the E Record non-canonical. |
| **P** | An arc planning to tell the fall of House D across three issues | Never canonical. RMS §9: *"An arc is a plan for telling, not a fact of the universe; the events it plans to tell are canon, the plan is not."* The fall may be World canon; the arc is not. |
| **R** | *Relationship type LOVES: an affective relationship from one party toward another.* | If canonical: the authoritative meaning records resolve against. No fact of the world, and no ownership of the World Records that use it. |
| **V** | *Character A has a scar over the left eyebrow* (specification) · `render_001.png` (asset) · *the render shows no scar* (analysis) | The specification is canonical. The asset is a manifestation, and its missing scar is a continuity finding against the asset. The analysis is an observation. |
| **I** | *Issue #12 was printed and distributed, reporting that City B is the capital.* | Never canonical. That #12 printed it is recorded; whether it is true is W's question. A later correcting issue is no more canonical. |

## 13. Source Traceability

| Rule | Source |
|---|---|
| Canonicality is model-defined; not a universal boolean; not on every Record | Blueprint §13.7c |
| The six meanings | Blueprint §13.7c |
| Record ≠ Canon | RMS §17; Blueprint §13.0; I-104 |
| Canonicality meaning *(if any)* is model-owned | RMS §6; Artifact 042 |
| The six meanings are fixed constitutionally; detailed semantics and realization stay with each model | Blueprint §13.7c; RMS §6 |
| No universal canonicality | RMS §4; Blueprint §13.7a |
| World Truth is one model of six | Blueprint §13.6 |
| E holds every view of the fact, possibly partial or wrong | RMS §8 |
| Production never canonical, never World Canon by any route; authored, durable, provenanced | RMS §9, §9.2 |
| Registry canonical about meaning, never about the world | Blueprint §13.6, §13.7c |
| Visual, for the Kinds RMS §11.1 identifies: specification canonical; asset a manifestation; analysis an observation | RMS §11.1, §11.2; Blueprint §13.6c |
| Canonical visual identity is the description, not the file | Blueprint §18.6 |
| §18.6's location wording differs from §13.6c and RMS §11 — recorded, not resolved | Blueprint §18.6, §13.6c; RMS §11 |
| Issue never canonical; never World Canon; references, never owns | RMS §12.2; Blueprint §13.7c |
| Published artifacts never become canon | Spine law 5 |
| A status vocabulary admitting CANON everywhere is false in two of six | Blueprint §13.7c |
| A projection does not become authoritative by being stored | Blueprint §13.7c |
| Working state becomes canon only through the gate | Blueprint §9.1 |
| AI output is provisional until gated | Spine law 6 |
| History is never a second canon | P-17 |
| Source-of-truth classes; P and I records `AUTHORITATIVE` | Blueprint §29.6a; Artifact 050 |
| Provenance answers who, when, why | Blueprint §13.7b; Artifacts 047, 048 |
| Authority framework | Artifact 051; Spine law 3; Blueprint §10.1 |
| No model a template for another; shared infrastructure confers no meaning | I-101; I-103 |
| Registry never owns another model's Records | I-105 |
| Artifact metadata `Canon:` is not a universal canonicality model | Artifact 003, field 10 |
| Hard dependency on 051; unlocks 145 and all models | Roadmap row 052 |
| Canonical gates are downstream | Roadmap row 145 |

---

*Artifact 052 · P2/2c · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the constitutional canonicality framework — the six meanings and their boundaries —
derived from Master Blueprint §13.7c and RMS §17 with the model sections that corroborate them. It
does not amend them, and it leaves each model's detailed semantics to that model. It is not a
Record, holds no canonical data, and defines no gate, lifecycle, field or schema. Where it differs
from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those governing
sources are correct and this document is wrong.*
