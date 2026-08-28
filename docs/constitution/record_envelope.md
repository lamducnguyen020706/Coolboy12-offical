# COOLBOY12 — Universal Record Envelope Contract

**Artifact 033** · `docs/constitution/record_envelope.md` · Own: CONST · RM: all · T: schema ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P1/1a ·
Req: BR-20 · BP: §13.7a · RMS: §4 · H: 031 · S: — · LS: — · G: — ·
→ 034–038, P2 · Risk: CRITICAL · ∥: no

## 1. Purpose

This document states the universal Record envelope: **exactly seven fields**, common to all six
sovereign Record Models, and no eighth.

Row 033 names the reason it is CRITICAL: *"the historical failure point — any eighth field
universalizes a semantic."* An envelope field binds every Record in every model. A field added
for one model's convenience makes a claim about the other five, and that claim is not proven
anywhere. The contract is therefore stated as a closed set, not a starting set.

## 2. Status and Authority

| | |
|---|---|
| Role | CONTRACT · Type: schema (row 033) |
| Source-of-truth class | AUTHORITATIVE (Artifact 016 §3) |
| Canon | `n/a` — row 033. This document is not a Record and holds no canonical data |
| Hard dependency | **Artifact 031** only (`H: 031`) |
| Unlocks | 034–038, P2 |

The seven fields are not established here. **RMS §4** freezes them, and row 033's `Val` states
the same seven in the same order. This document is the AUTHORITATIVE statement of the contract
for readers and downstream artifacts; it amends neither source and adds nothing to either.

## 3. Scope

Artifact 031 names **core envelope** as one of the six bootstrap elements — that a Record has
one. This document states what that envelope contains. The dependency runs 031 → 033 and not the
reverse, and the six bootstrap elements are not restated here.

Artifact 032 places the envelope's step in the bootstrap order. This document does not repeat the
flow and does not depend on any runtime bootstrap.

## 4. The Universal Envelope Rule

> **RMS §4** — *"The universal envelope is the bootstrap set and no more"* `FROZEN`:
> `partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class`.

**EXACTLY SEVEN. There is no eighth.**

The set is closed. It is not extended by an implementation, an adapter, an external provider, or
a downstream artifact. Blueprint §13.7a states the governing principle the closure serves:
*"The Record System shares mechanisms. It does not share semantics."* A mechanism may be common
to six models without any of them agreeing about meaning; a claim about what a Record *is* binds
every model that carries it, and must be proven in each (I-103).

Where the envelope may evolve at all, it evolves as the constitutional architecture does — by
the governed process that produced RMS §4 — never by addition at the point of use.

## 5. The Seven Fields

| # | Field | Universal role | Does not own |
|---|---|---|---|
| 1 | `partition` | Names the partition the Record belongs to | The model's semantics |
| 2 | `kind` | Carries the Record's kind | What that kind means |
| 3 | `object_id` | Carries the object identity component | Identity grammar, parsing, allocation |
| 4 | `slug` | Decoration only | Canonical identity |
| 5 | `provenance` | Captures provenance | What provenance means in a model |
| 6 | `registry_ref` | Carries the Record's reference into the Registry | What it resolves to; resolution |
| 7 | `sot_class` | Carries the source-of-truth class | Canonicality |

Each field's **existence and universality** is established by RMS §4 and RMS Appendix B, for all
seven alike (§9). Each field's **role** below is stated only as far as the sources establish it.

### 5.1 `partition`

Names the partition the Record belongs to. There are six, one per sovereign Record Model — W, E,
P, R, V, I (RMS §2) — and identity is partition-first (I-82).

**Does not own.** I-101: *"Every partition owns exactly one sovereign Record Model."* That fixes
which model is sovereign and nothing further; what the Record means, and whether it can be
canonical, are model-owned (I-103, I-104). Naming the partition is not a second ownership axis.

### 5.2 `kind`

Carries the Record's kind.

**Does not own.** Blueprint §13.7a prohibits a **universal Kind taxonomy**; each model owns its
own (§13.11), and Registry definitions govern what a kind means (I-105). No kind roster is
enumerated here, and none is frozen by this contract (I-106).

### 5.3 `object_id`

Carries the object identity component of the Record's identity.

**Does not own.** The identity **grammar** is Artifact 034's, its parser and formatter Artifact
035's, and ordinal allocation Artifact 036's. This contract states that the envelope carries the
field; it states no positional grammar. Blueprint §13.7a also prohibits a universal identity
**composition** — *what constitutes the identity of a Record in that model* stays model-owned,
which the universal grammar does not touch.

### 5.4 `slug`

> **RMS §5** — *"slug is decoration only."*

**Does not own.** The slug is not canonical identity, not a stable key, and not meaning-bearing.
I-82: *"A rename never creates a new canonical identity."*

### 5.5 `provenance`

Captures provenance — §13.7b: *"Who made this, when, and **why**"*, held as *"an envelope
property on the Record."*

**Does not own.** Blueprint §13.7a lists provenance **capture** as shared infrastructure while
*"what provenance means in a model"* is not decided by it. §13.7b separates six terms that *"are
not interchangeable"* — provenance · audit · history · revision · version · derivation. Only
provenance is an envelope field. History packaging is model-owned, and §13.7a prohibits a
**Universal History Record**.

### 5.6 `registry_ref`

Carries the Record's reference into the Registry — the definitional layer holding reusable
semantics (§9.4). The field's existence in the universal envelope is RMS §4's, `FROZEN`, and
Blueprint §13.7 names *"a Registry reference"* among what a record must have to be a record at
all.

**Does not own — and the referent is deliberately not stated here.**

> **Blueprint §9.4** — **Reference resolution is not Registry work.** What an `_ref` field
> *resolves to*, and the mechanics of resolving it, belong to a Record resolver. The Registry
> defines the reference *field*; it does not perform or own resolution.

So this contract states that the envelope carries the field, and states no referent, no
resolution rule and no legality rule. Resolution is shared infrastructure, and §13.7a is
explicit that it does not decide whether a reference is semantically legal. I-105 holds the
outer bound: Registry *"holds semantic authority over definitions and never semantic ownership
of another model's Records."* No Registry definition, kind or vocabulary is stated here.

### 5.7 `sot_class`

Carries the Record's source-of-truth class.

At the record level the classes are the Blueprint's **five** — AUTHORITATIVE · DERIVED · CACHED ·
TEMPORARY · EXTERNAL (§29.6a; RMS §4: *"Source-of-truth classification | §29.6a — five classes |
Constitutional"*). Artifact 016 governs which set applies: *"Where a record-level class is
required, the Blueprint's five govern."* The Roadmap's sixth repository-artifact class, DEV-ENV,
classifies repository paths and is not a record-level value (Artifact 016 §2, CONFLICT-C).

**Does not own.** `sot_class` says where the fact lives. It is **not** canonicality. I-104:
*"Record and Canon are not synonyms. Canonicality is a status property whose meaning is defined
by each Record Model that has one, and two models hold Records that are never canonical."*
Blueprint §13.7a prohibits **universal canonicality**. Reading `sot_class` as a canonicality flag
would universalize a meaning that six models define six ways.

**Types, defaults, nullability and serialization are not established by the supplied
authoritative sources** for any of the seven fields, and none is invented here. This is a
contract about which fields exist and what they are for.

## 6. Explicit Exclusions

**The universal envelope contains exactly the seven fields in §5. It does not contain `tier`, it
does not contain `status`, and it carries no model-specific field.**

> **RMS §4** — *"`tier` and `status` are NOT universal envelope fields"* `AUTHOR-DECIDED`
> (closes FG-V7-03). *"`tier` is World ontology; `status` admits `CANON`, which Production and
> Issue can never reach. Both are **World-owned**; other models define their own state
> vocabularies."*

The exclusion is of the **semantics**, not of two spellings. A universal field carrying a
lifecycle or state vocabulary, a rank or quality judgment, or a canonicality flag is the excluded
thing whatever it is named. Blueprint §13.7a and RMS §4 name the prohibitions this serves: no
Universal Record Base · no Universal Relationship Record · no Universal History Record · no
universal lifecycle · no universal canonicality · no universal Kind taxonomy · no universal
identity composition · no universal state model · no universal semantic schema.

No World field belongs here, and a World-purposed field does not become universal by being given
a generic name. Relationship Record and History Record are World Record Model concepts and *"may
not be required of another Record Model"* (I-102).

## 7. Envelope vs Model-Owned Record Content

The envelope is not the whole Record.

```
UNIVERSAL RECORD ENVELOPE
┌──────────────────────────────┐
│ partition                    │
│ kind                         │
│ object_id                    │
│ slug                         │
│ provenance                   │
│ registry_ref                 │
│ sot_class                    │
└──────────────────────────────┘
              +
   MODEL-OWNED RECORD CONTENT
              ↓
         complete Record
```

> **I-87** — *"Record is the common **architectural** data unit of the Record System — not a
> universal semantic model. Every Record belongs to exactly one of six partitions; **the
> semantics of a Record are owned by its Record Model**; and Record is not synonymous with World
> Truth."*

A Record may require content beyond these seven fields. That content is its model's, is defined
through Registry (I-105), and does not enter the envelope by being needed.

## 8. Downstream Ownership

| Not defined here | Owned by |
|---|---|
| That a Record has a core envelope, and the other five bootstrap elements | Artifact 031 |
| The bootstrap order | Artifact 032 |
| Identity grammar, parser and formatter, ordinal allocation | Artifacts 034–036 |
| What structural validation checks | Artifact 037 |
| Executable proof of this contract | Artifact 038 |
| Kind definitions, field definitions, vocabularies | Registry |
| Each model's own record content and semantics | the six sovereign Record Models |

## 9. Source Traceability

**Field existence and universality** — one source for all seven, and it is the same one each
time: **RMS §4**, which names them inside *"The universal envelope is the bootstrap set and no
more"* `FROZEN`, and **RMS Appendix B**, whose Field Catalog lists them under
*"Universal (7):"* and in the same breath sorts `tier` · `status` · mutation-class fields under
*"World-owned, not universal:"* Roadmap row 033's `Val` restates the same seven; it records the contract and does
not originate it.

The rows below cite what establishes each field's **role and boundary**. They are not the
authority for its existence, and must not be read as such.

| Element | Role / boundary source |
|---|---|
| `partition` | RMS §2 (six models), I-82 (partition-first), I-101 (partition ↔ sovereign model) |
| `kind` | Blueprint §13.7a (no universal Kind taxonomy), §13.11, I-105, I-106 |
| `object_id` | Blueprint §13.7a (AD-1: grammar universal, composition model-owned), I-82 |
| `slug` | RMS §5 (*"slug is decoration only"*), I-82 |
| `provenance` | Blueprint §13.7b (envelope property; the six-term separation), §13.7a (capture ≠ meaning) |
| `registry_ref` | Blueprint §13.7 (*"a Registry reference"* in the meta-contract), §9.4 (Registry is the definitional layer; *"the Registry defines the reference field; it does not perform or own resolution"*), §13.7a, I-105 |
| `sot_class` | Blueprint §29.6a (five classes), Artifact 016 §2–§3 (record-level vs repository-artifact), I-104 (not canonicality) |
| `tier` and `status` excluded | RMS §4 (`AUTHOR-DECIDED`, closes FG-V7-03); RMS Appendix B; Roadmap row 033 |
| No eighth field; no universalized semantic | Blueprint §13.7a, RMS §4 nine prohibitions, I-103, I-87 |
| Envelope ≠ complete Record | I-87, I-103 |

---

*Artifact 033. This document is AUTHORITATIVE about the universal Record envelope and is
`Canon: n/a`. It carries no canonical data, defines no Record, creates no Record Model, states no
type, default or serialization rule, and admits no eighth field.*
