# COOLBOY12 — Mechanism vs Semantics Boundary

**Artifact 043** · mechanism vs semantics boundary · `docs/constitution/mechanism_semantics.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P2/2a · Req: BR-20,RR-04 · BP: §13.7a · RMS: §3 ·
H: 039 · S: — · LS: — · G: — · → all · Val: nine prohibitions verbatim ·
Done: prohibitions binding · Why: **the anti-COM firewall** · Risk: CRITICAL · ∥: no

## 1. Constitutional Status

This document is the **anti-COM firewall**. It exists to stop the Record System becoming the
retired Canon Object Model under a new noun, by fixing the boundary between what the six Record
Models may **share** and what each must **own**.

It states one boundary precisely. It does not restate the Record System constitution: **Artifact
039** (`docs/constitution/record_system.md`) governs that, and this document depends on it
without amending, redefining, or duplicating it.

Blueprint §13.7a is the source of this boundary, and RMS §3 places it in the architecture:

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

The mechanism layer is real and legitimate. **What it must never acquire is meaning.**

---

## 2. The Governing Rule

> **I-103** — *"A mechanism may be shared across Record Models; a semantic may not be shared
> without evidence in each model that carries it. Shared infrastructure never confers shared
> meaning."*

Stated as the constitutional principle this document enforces, in Blueprint §13.7a's own words:

> **The Record System shares mechanisms. It does not share semantics.**

Every rule below follows from that sentence. Where this document and the Blueprint, the Record
Model System, or the Roadmap differ, **they are right and this document is wrong.**

---

## 3. Shared Mechanism — Definition

A **shared mechanism** is a technical facility that multiple Record Models may use **without any
of them agreeing about meaning** (§13.7a).

Shared mechanisms include identity minting, parsing and resolution; serialization; structural
validation; provenance capture; reference resolution; the single gated mutation path;
source-of-truth classification; and storage and repository access.

> **Sharing an implementation facility MUST NOT transfer semantic authority to that facility.**

A mechanism is permitted to be common precisely because it decides nothing. The moment a
facility begins to decide what something *means*, it has stopped being a mechanism and has
become a claim — and it is then subject to §8's test and to the prohibitions of §6.

---

## 4. Shared Semantic — Definition

A **shared semantic** is a claim about what a Record, field, Kind, state, relationship,
lifecycle, authority, canonicality, identity, history, or other model-owned concept **means**.

A semantic **MUST** remain model-owned unless the constitutional sources explicitly establish it
as universal.

Universality **MUST NOT** be inferred from any of:

- common tooling;
- common storage;
- common validation infrastructure;
- common serialization;
- common identifiers;
- common mutation infrastructure;
- similar terminology.

Each of those is a mechanism. None of them is evidence about meaning in any model.

---

## 5. The Shared-Mechanism Boundary

Every shared facility carries an explicit limit. The permitted responsibility is what the
mechanism does; the semantic boundary is what it **MUST NOT** decide (§13.7a).

| Shared mechanism | Permitted responsibility | Explicit semantic boundary |
|---|---|---|
| Identity minting / parsing / resolution | Produce, parse, and resolve stable identifiers | Does not determine what the named Record means, or what constitutes the identity of a Record in any model |
| Serialization | Render a Record durably and legibly | Does not determine what fields a Record has, or the Record schema |
| Structural validation | Check that this is a well-formed Record at all | Does not determine semantic legality — Kind legality, tier rules and relationship legality are model-owned |
| Provenance capture | Capture who, when, and why | Does not determine what provenance *means* in a model |
| Reference resolution | Resolve a reference to its target | Does not determine whether the reference is semantically legal |
| Gated mutation path | Enforce the common pipeline: propose → check → gate → commit → changelog → log | Does not determine what a model considers a legal change |
| Source-of-truth classification infrastructure | Support assignment of a source-of-truth class | Does not define model semantics, or which class a model's data belongs to |
| Storage / repository access | Provide durable persistence | Does not define the model's storage semantics |

Five distinctions this table exists to hold apart, each of which **MUST** be preserved by every
later artifact and every implementation:

```
structural validation   ≠   semantic validation
provenance capture      ≠   provenance meaning
reference resolution    ≠   reference legality
mutation mechanism      ≠   mutation semantics
storage capability      ≠   semantic authority
```

---

## 6. The Nine Prohibitions

**These nine prohibitions are the core anti-COM firewall. They are reproduced verbatim from
Blueprint §13.7a and are binding as written.** They are stated as prohibitions rather than
permissions because a list of permissions would be read as exhaustive.

1. **No Universal Record Base.** The shared layer is the bootstrap contract of §13.7 and nothing
   above it.

2. **No Universal Relationship Record.** Relationship packaging is model-owned (§13.6d, §13.9).

3. **No Universal History Record.** The P-18 obligation is universal; its packaging is
   model-owned (§13.6d).

4. **No universal lifecycle.** Two models hold Records that can never be canonical; a status
   vocabulary admitting `CANON` everywhere would be false (§13.6a, §9.4).

5. **No universal canonicality.** Six models, six meanings (§13.7c).

6. **No universal kind taxonomy.** Each model owns its own (§13.11).

7. **Identity is the one deliberate exception, and it is a *grammar*, not a semantics (AD-1,
   resolved).** The identity **grammar** `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` **is
   constitutional and universal across all six Record Models** (§13.9a, I-82). What remains
   model-owned is the **semantic interpretation** of what that grammar names: which kinds exist,
   what a kind means, what constitutes the identity of a Record in that model, and what its
   lifecycle, authority, and temporal meaning are. **A universal identity grammar is not a
   universal Record semantics** — the grammar fixes the syntax of the name and decides nothing
   about the thing named.

8. **No universal state model.** Locked / world-state / derived is a World field-mutation-class
   split and is not claimed elsewhere.

9. **No universal Record schema.**

No later artifact, schema, validator, or implementation may weaken, merge, split, or carve an
exception into any of the nine. A proposal that requires one of them to bend is a proposal to
reinstate the Canon Object Model, and is refused on that ground.

---

## 7. The Identity Exception

Identity is the single deliberate exception, and its precision matters more than its existence:
it is an exception **about syntax**, not about meaning.

| Universal — constitutional | Model-owned — semantic |
|---|---|
| The identity grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` | What a Kind means |
| Element order and syntax | Which Kinds exist |
| Parsing | What constitutes the identity of a Record in that model |
| Resolution and minting mechanisms | Lifecycle meaning |
| The uniqueness contract | Authority meaning |
| | Temporal meaning |
| | Semantic interpretation of the named object |

> **The identity grammar fixes the syntax of the name; it does not decide what the named thing
> means.**

All six Record Models bear an identity of this form (§13.9a, I-82; AD-1 resolved). That fact
establishes nothing whatever about whether their Kinds, lifecycles, authority, canonicality, or
temporal semantics resemble one another — and it **MUST NOT** be cited as if it did.

---

## 8. The Facility-or-Claim Test

This is the reusable test to apply whenever a future version proposes to share something
(§13.7a). It is the primary decision rule preventing accidental reintroduction of the Canon
Object Model.

```
                    Is this a FACILITY, or a CLAIM?
                                │
             ┌──────────────────┴──────────────────┐
             ▼                                     ▼
        A FACILITY                             A CLAIM
   it does something                    it asserts what something
   and decides nothing                          means
             │                                     │
             ▼                                     ▼
   MAY be shared, on                  MUST be proven in EACH model
   convenience                        that carries it
                                                   │
                                                   ▼
                                   A claim proven in one model and
                                   asserted in six is the exact error
                                   this architecture exists to retire
```

Applied as three binding rules:

1. If it is a facility, it **MAY** be shared.
2. If it is a semantic claim, it **MUST** have explicit evidence in every Record Model that
   carries it.
3. A claim established for one model **MUST NOT** automatically become a claim for all models.

When the answer is unclear, the construction is treated as a claim. Mistaking a claim for a
facility rebuilds the retired architecture; mistaking a facility for a claim costs only a
justification.

---

## 9. Model-Ownership Table

The right-hand column is the **semantic owner**. A shared mechanism never owns the semantic
column, and its appearance in the middle column confers nothing in the right.

| Concern | Universal mechanism? | Semantic owner |
|---|---|---|
| Identifier grammar | Yes | Constitution |
| Identity meaning | No | Each Record Model |
| Structural validation | Yes | Shared mechanism |
| Semantic validation | No | Each Record Model |
| Provenance capture | Yes | Shared mechanism |
| Provenance meaning | No | Each Record Model |
| Relationship packaging | No | Model-owned |
| History packaging | No | Model-owned |
| Lifecycle | No | Model-owned |
| Canonicality meaning | No | Model-owned |
| Kind taxonomy | No | Model-owned |
| State model | No | Model-owned |
| Record schema | No | Model-owned |
| Mutation pipeline | Yes | Shared mechanism |
| Mutation legality | No | Each Record Model |

Where the middle column reads **Yes**, the facility is common and decides nothing. Where it
reads **No**, no common facility may decide the question on a model's behalf.

---

## 10. Worked Examples

Five cases where the boundary is easiest to cross by accident.

### Example A — Structural validation

A shared validator **MAY** check:

- envelope shape;
- partition presence;
- syntactic identity form;
- structural well-formedness.

It **MUST NOT** decide:

- whether a Kind is legal in W;
- whether a Relationship is legal;
- whether a Record is canonical;
- whether a lifecycle transition is valid.

Those are semantic decisions and belong to the Record Model that owns them.

### Example B — Provenance

A shared mechanism **MAY** capture who, when, and why.

It **MUST NOT** impose one universal interpretation of provenance across W / E / P / R / V / I.
Capturing the same three facts in six models is a common facility; what those facts *mean* in
each model is six separate questions.

### Example C — Mutation

A common mutation path **MAY** enforce:

```
propose → check → gate → commit → changelog → log
```

It **MUST NOT** decide what constitutes a legal mutation for every Record Model. The pipeline is
common; legality under it is model-owned.

### Example D — Identity

All six models **MAY** use `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]`.

That does **not** imply that all six share Kind semantics, lifecycle semantics, authority
semantics, identity semantics, or temporal semantics.

### Example E — Relationship Record

One model **MAY** package relationships as a Record.

That does **not** make *Relationship Record* a universal Record System primitive. I-102 states
it directly: Relationship Record and History Record are World Record Model concepts, neither is
a Record System primitive, and neither may be required of another Record Model.

---

## 11. The Sovereign Model Boundary

The six Record Models remain sovereign. This document adds no layer above, beneath, or between
them, and the sharing it permits creates no relationship among them.

- **No model specializes another.**
- **World is not a template for the others.**
- **Shared infrastructure does not create inheritance.**
- **Shared mechanisms do not create a common semantic superclass.**
- **Common tooling does not create a common model.**

> **Common infrastructure is not common semantic ownership.**

I-101 states the sovereignty this preserves: every partition owns exactly one sovereign Record
Model; no Record Model is a specialization of another, and none is the template for another.
I-87 states the companion limit: Record is the common *architectural* data unit — **not** a
universal semantic model — and the semantics of a Record are owned by its Record Model.

**Artifact 041** (`docs/constitution/sovereignty.md`) is the sovereignty contract. This document
depends on it and does not restate it.

---

## 12. Boundary With Neighbouring Artifacts

This artifact fixes one boundary. It is not the place where the concepts it protects are
defined.

| Relationship | This artifact's position |
|---|---|
| **Artifact 039** — Record System constitution | Hard dependency (`H: 039`). Governing. Not amended, not duplicated here. |
| **Artifact 041** — six-model sovereignty contract | Referenced for sovereignty; not restated. |
| **Artifact 044** — seven architectural categories | Defines Record / Kind / Field / State / Relationship / Definition / Projection / Primitive. **This artifact defines none of them**; it establishes the boundary those definitions must respect. |

The following artifacts own contracts this document deliberately does **not** write. Each is
referenced only where the boundary requires naming it:

Artifact 048 — provenance · Artifact 049 — temporal vocabulary separation · Artifact 051 —
authority · Artifact 052 — canonicality · Artifact 054 — temporal obligation · Artifact 055 —
relationship boundary · Artifact 056 — package boundary · Artifact 057 — Kind admission ·
Artifact 058 — cross-model dependencies.

A later artifact that needs an exception to this boundary does not take one: it raises the
conflict against the Blueprint, which is the only place the boundary can change.

---

## 13. Conformance

An artifact, schema, validator, or implementation conforms to this document when all of the
following hold.

| # | Condition |
|---|---|
| C-1 | The nine prohibitions of §6 appear intact and are not weakened, merged, split, or excepted. |
| C-2 | Every shared facility it introduces states what it does **not** decide (§5). |
| C-3 | No semantic is asserted as universal without explicit evidence in each model that carries it (§4, §8). |
| C-4 | Identity is treated as a universal grammar with model-owned semantics, never as a universal identity semantics (§7). |
| C-5 | The facility-or-claim test (§8) was applied to every shared construction, and the answer is recorded. |
| C-6 | Nothing in it creates inheritance, a semantic superclass, or a seventh model (§11). |
| C-7 | It defines no concept this document reserves to Artifact 044 or to Artifacts 048–058 (§12). |

A construction that fails any condition is not a design choice to be weighed. It is the retired
architecture returning, and it is refused.

---

## 14. Non-Authority Boundary

This document is a **contract on the mechanism/semantic boundary**. It:

- **governs** what may be shared across Record Models and what must be owned by each;
- **does not** define any Record Model's semantics;
- **does not** define the architectural categories (Artifact 044);
- **does not** define provenance, temporal, authority, canonicality, relationship, packaging,
  Kind-admission, or cross-model dependency contracts (Artifacts 048–058);
- **does not** introduce implementation, schema, or code;
- **carries no canonical data** (`CD: no`) and writes nothing to `canon/**`.

`Req: BR-20,RR-04` is preserved exactly as the Roadmap states it. The authoritative requirement
register is not present in this repository; the requirement text is therefore **not** reproduced
here and **MUST NOT** be inferred.

*This document derives its authority from Blueprint §13.7a and RMS §3, and amends neither. Where
it and the Master Blueprint, the Record Model System, or the OS File Build Roadmap differ, they
are right and this document is wrong.*
