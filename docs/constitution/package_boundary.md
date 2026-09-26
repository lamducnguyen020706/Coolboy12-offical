# COOLBOY12 — Package Boundary Specification

**Artifact 056** · package boundary specification · `docs/constitution/package_boundary.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a ·
CD: no · Ph/St: P2/2d · Req: BR-18 · BP: §13.6d · RMS: §7 · H: 055 · S: — · LS: — · G: — ·
→ models · Val: packaging model-owned; W established; E/P/V/I model-owned; R Registry-owned ·
Done: no universal package · Why: I-107 · Risk: high · ∥: no

## 1. Purpose

This contract answers one question: **how is package composition governed across the six sovereign
Record Models without creating a universal Record package?**

The answer is Blueprint §13.6d's governing rule: *"each Record Model owns the packaging of its
Records."* World's package is established; Epistemic, Production, Visual and Issue own theirs;
Registry owns its own; and no Record Model package composition is universal. Row 056's reason is
*"I-107"*: a package declared for a model that has not been independently designed is provisional
and may not be implemented as a requirement.

**This contract adds no architecture.** Every rule restates Blueprint §13.6d, §13.6e, §13.7,
§13.7a and §13.9, RMS §4, §6 and §7, and I-72, I-90, I-101, I-102, I-103, I-105 and I-107.

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the package boundary**: who owns package composition, and
what is not universal. It is not World Canon, not a Record, not a schema, and holds no authority
over any Record Model's package design.

It derives the contract from the Master Blueprint and the Record Model System; it does not amend,
supersede, or outrank either, and amends no invariant. Where this document differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those governing sources are
correct and this document is wrong.**

`Req: BR-18` is preserved exactly as the Roadmap states it. This contract does not reproduce,
reconstruct or infer its requirement text, and creates no new requirement under it.

## 3. Scope

**In scope.** Who owns package composition in each of the six models; World's established package;
the status of §13.6d's package rows for E, P, R, V and I; Registry's ownership of its own package;
the difference between package shape and package authority.

**Out of scope.** The temporal obligation (Artifact 054); the relationship boundary and the World
scope of the Relationship Record (055); Kind admission (057); cross-model dependency (058); every
model's actual package (Artifacts 060, 202, 237, 279, 340, and the Visual and Issue model
architectures); schemas, fields, storage, code and tests.

```
054  temporal obligation         — what every model must be able to account for
055  relationship boundary       — the Relationship Record is World's
056  package boundary            ← this contract: who owns package composition
  ↓
     each model's package        — W 202, 237 · E 279 · P 340 · R 060 · V, I: their own architecture
```

## 4. The Governing Package Rule

> **Package composition is owned by the Record Model that owns the Records. World's package is
> established, and it is World's. Epistemic, Production, Visual and Issue own their package
> architectures. Registry owns the package architecture of Registry Records. No Record Model
> package composition is universal, and a package row declared for a model not yet independently
> designed is provisional and is not a requirement.**

| Clause | Source |
|---|---|
| Each model owns the packaging of its Records | Blueprint §13.6d; RMS §6; I-90 |
| World's package established | Blueprint §13.6d, §13.9; RMS §7; I-72 |
| E, P, V, I model-owned; R Registry-owned | Blueprint §13.6d |
| No universal package | Blueprint §13.7a; RMS §4 |
| Undesigned-model rows provisional, not requirements | I-107; Blueprint §13.6d |

## 5. What "Package Composition" Means

RMS §6 lists what a Record Model owns: *"its Kind taxonomy, identity semantics, state and
lifecycle, relationship packaging, temporal architecture, provenance meaning, canonicality meaning
(if any), semantic validation, and package composition."* Package composition is the architectural
determination of which Record constructs constitute a model's package — for World, *"a package of
three records with one identity between them"* (§13.9).

The package is architectural, not physical. §13.9: *"The package is logical and semantic. An
implementation may store, index, or project the three differently — one file, three files, or a
table apiece — provided the semantics survive."* RMS §4 keeps storage apart: *"Storage shape is
model-owned within the contract"*.

Package composition is **not** a field schema, a field list, a table design, an API, a
serialization or storage format, a lifecycle, or a validator. This contract defines none of them.

## 6. Universal Obligations vs Model-Owned Package Composition

### 6.1 Universal — established elsewhere, cited here

| Universal | Source |
|---|---|
| Six sovereign Record Models; every Record in exactly one partition | I-16; I-101 |
| The universal envelope, and no more: seven fields | RMS §4 |
| Shared infrastructure never confers shared meaning | I-103; §13.7a |
| The P-17/P-18 temporal obligation | Artifact 054; I-90 |
| Wherever a Relationship Record exists, one authoritative edge in one Relationship Record | I-90; §13.6d; Artifact 055 |

These are system-level obligations relevant to model construction; they do not, by themselves,
determine package composition or become universal package members. The temporal obligation is not a
universal History Record, and the relationship-ownership rule is not a universal Relationship
Record.

### 6.2 Model-owned

Package composition. I-90: *"Package composition is owned by each Record Model"*. §13.6d:
*"a model may conclude that it needs no History Record at all, or needs a versioning, lineage,
event-log, or supersession mechanism instead"*.

### 6.3 Package shape ≠ package authority

Two models MAY independently choose shapes that look alike. The resemblance creates nothing
universal: §13.6d, *"the fact that other models currently adopt structures of the same shape does
not make those structures universal primitives"*; §13.9, *"Where another model adopts a structure
of the same shape, it does so on its own evidence and owns the result."* Authority comes from each
model's own architecture, not from similarity of shape. A similar shape is not semantic
inheritance (I-101, I-103).

## 7. World's Established Package

§13.6d marks the W rows **`ESTABLISHED`**: *"The World Record Model is designed and its package is
in use throughout this document"*. I-72 and RMS §7 (`LOCKED`) state the package:

| World | Package |
|---|---|
| Seven instance-bearing Kinds | `Record + Relationship Record + History Record` |
| WSV | `Record + WSV-H` |

World's package is established because World is independently designed (RMS §7: *"Not
redesigned. Normalization only."*), not because the other models should resemble it. The
Relationship Record and the History Record are World Record Model concepts (I-102; Artifacts 054,
055). World's actual package specification is Artifacts 202 and 237.

**World maturity ≠ World template.** World being the most completely specified model grants it no
architectural authority over any other model. I-101: *"No Record Model is a specialization of
another, and no Record Model is the template for another."*

**WSV.** This contract states only WSV's package, as I-72 and RMS §7 give it. It decides nothing
about WSV's edges, relationships or entry granularity, and does not touch §13.10, whose `PROPOSED`
flag stands (RMS Appendix H, PC-2; Artifact 055 §9.3).

## 8. The Six-Model Ownership Rule

| Record Model | Package status | Package authority |
|---|---|---|
| **W** | Established | World |
| **E** | Model-owned | Epistemic |
| **P** | Model-owned | Production |
| **R** | Registry-owned | Registry |
| **V** | Model-owned | Visual |
| **I** | Model-owned | Issue |

§13.6d's governing table: W *"Established — the World Record package (§13.9)"*; E, P, V, I
*"Model-owned — each establishes its own"*; R *"Registry-owned — Registry establishes its own, as
the model whose Records are definitions (§13.6e)"*.

**For E, P, V and I, each model owns its own package architecture. For R, Registry owns the
package architecture of Registry Records. None of these package decisions is frozen by this
contract.**

## 9. Interpreting §13.6d's Package Table — MODEL-DESIGN INPUT

§13.6d marks the E, P, R, V and I rows *"MODEL-DESIGN INPUT (not a freeze)"*: *"Each row is
evidence for that model's future design work, not a constraint on it."* And: *"A
MODEL-DESIGN-INPUT row is not a freeze and must not be implemented as one."* I-107 makes the
consequence binding.

Therefore:

1. A row's presence in the Blueprint does not create a constitutional requirement.
2. This contract promotes no row to a requirement and treats none as an implementation instruction.
3. The model's own architecture establishes and owns the package decision.
4. The model's own architecture may confirm, revise, reduce or replace the design input represented
   by its row: *"a model closing its schema may confirm or revise its row"* (§13.6d).
5. This contract performs no model's package design.

**How a model changes its shape.** §13.6d: *"A Record Model changing its own packaging is a schema
change at Foundational ceremony, recorded in both documents in the same cycle (§13.7)"*, and
*"What it explicitly does not require is any other model's agreement."* §13.7's lockstep rule
covers *"the package model"*. This contract cites the ceremony and defines none.

**SOURCE STATUS / NON-NORMATIVE DESIGN INPUT.**

| Model | §13.6d row status | §13.6d package (as written) | 056 interpretation |
|---|---|---|---|
| W instance-bearing | `ESTABLISHED` | `Record + Relationship Record + History Record` | established World package |
| W WSV | `ESTABLISHED` | `Record + WSV-H` | established World package |
| E | MODEL-DESIGN INPUT | `Record + Relationship Record + History Record` | not frozen; E-owned |
| P | MODEL-DESIGN INPUT | `Record + History Record`, Relationship Record optional | not frozen; P-owned |
| R | MODEL-DESIGN INPUT | `Record + History Record`, no Relationship Record | not frozen; Registry-owned |
| V | MODEL-DESIGN INPUT | `Record + Relationship Record + History Record` for specifications; `Record + History Record` for assets and analyses | not frozen; V-owned |
| I | MODEL-DESIGN INPUT | `Record + History Record`, no Relationship Record | not frozen; I-owned |

**These rows are recorded as source design input and are not requirements imposed by Artifact
056.**

**Source condition recorded, not resolved.** RMS §15 (`FROZEN`) records relationship mechanisms for
E and P that differ from their rows above — E's knowledge relationships *"within KNOWLEDGE-STATE"*,
P with *"No Relationship Record"* — as Artifact 055 §8.3 records. This contract decides nothing
between them; each model's own architecture does (documented in 279 and 340).

## 10. Registry's Own Package

Registry is *"a sovereign Record Model, not a lookup table"* (§13.6e), and I-105: *"Registry is a
sovereign Record Model. Its definitions are Records, not configuration."* §13.6d gives R's package
architecture to Registry: *"Registry-owned — Registry establishes its own"*. Its specification is
Artifact 060.

Registry's package ownership covers **Registry's own Records** and nothing else. I-105: Registry
*"never semantic ownership of another model's Records"*; §13.6e gives each model *"Whether it uses
Relationship Records at all (§13.6d)"*. No Registry package decision is a requirement for any other
model.

## 11. Relationship to Artifact 054

054 answers *what every model must be able to account for temporally*: the obligation universal,
the mechanism model-owned. 056 answers *who owns the package that results*. 054 remains the owner
of the temporal obligation. This contract defines no History Record semantics, temporal entry,
lifecycle, versioning, revision chain or temporal schema.

## 12. Relationship to Artifact 055

055 establishes the World scope of the named Relationship Record and the relationship boundary;
056 establishes who owns package composition in all six models. This contract does not reopen the
reification criterion, the Relationship Record's meaning, edge ownership, the Registry
owning-role rule, WSV relationship questions or any relationship schema.

## 13. The Central Anti-Pattern

```
✗  World has  Record + Relationship Record + History Record
   →  therefore E, P, R, V, I have  Record + Relationship Record + History Record

✓  World has an established package because World owns its package architecture.
   E, P, V and I meet their constitutional obligations through package architectures each owns.
   Registry owns the package architecture of Registry Records.
```

The first line is invalid on three separate grounds:

- **§13.6d** establishes that the E, P, R, V and I package rows are *"MODEL-DESIGN INPUT (not a
  freeze)"*: *"No downstream artifact may treat Record + History Record — or any other composition
  below — as a settled requirement for E, P, R, V, or I."*
- **I-107** prohibits implementing provisional package composition as a requirement: *"A package
  composition declared for a Record Model that has not been independently designed is provisional
  and may not be implemented as a requirement."*
- **I-101** preserves model sovereignty: *"No Record Model is a specialization of another, and no
  Record Model is the template for another."*

In §13.6d, *below* is its package table. So no downstream artifact may treat any package
composition shown for E, P, R, V or I in §13.6d as a settled implementation requirement unless and
until that model's own architecture establishes it.

## 14. Prohibited Architectural Moves

| # | Prohibited | Source |
|---|---|---|
| 1 | A universal package composition | §13.7a; RMS §4 |
| 2 | World's package as a universal template | I-101; §13.6d |
| 3 | A model inheriting package architecture from another | I-101; I-90 |
| 4 | Treating a MODEL-DESIGN-INPUT row as a frozen requirement | I-107; §13.6d |
| 5 | Treating a similar package shape as semantic inheritance | I-101; I-103; §13.9 |
| 6 | Treating shared infrastructure as evidence of a universal package | I-103; §13.7a |
| 7 | Defining a package schema here | Roadmap row 056 `T: doc` |
| 8 | Designing any model's package here | §13.6d; Roadmap rows 060, 202, 279, 340 |
| 9 | Reopening the temporal obligation | Artifact 054 |
| 10 | Reopening the Relationship Record's scope | Artifact 055 |
| 11 | A universal History Record | §13.7a; I-102 |
| 12 | A universal Relationship Record | §13.7a; I-102 |
| 13 | A universal lifecycle or package mechanism | §13.7a; RMS §4 |
| 14 | Registry package ownership read as ownership of another model's package | I-105; §13.6e |

## 15. What This Contract Does Not Define

1. Record schema. 2. A universal Record subtype. 3. A universal Relationship Record. 4. A universal
History Record. 5. Temporal implementation. 6. Temporal schema. 7. Lifecycle. 8. Provenance
semantics. 9. Authority. 10. Canonicality. 11. Source-of-truth classification. 12. Kind admission.
13. Cross-model dependency rules. 14. The Registry relationship-type schema. 15. The World
Relationship Record schema. 16. E, P, V or I model architecture. 17. Runtime code. 18. Validators.
19. Storage. 20. APIs. 21. Serialization or wire formats. 22. New constitutional invariants.
23. A Blueprint amendment. 24. A Roadmap amendment.

## 16. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number.

| ID | Condition | Source |
|---|---|---|
| **C-056-01** | Package composition is owned by the Record Model that owns the Records. | §13.6d; RMS §6; I-90 |
| **C-056-02** | World's package is recognized as established for World only. | §13.6d; I-72; RMS §7 |
| **C-056-03** | E, P, V and I package architecture remains owned by those models. | §13.6d |
| **C-056-04** | R package architecture is Registry-owned. | §13.6d; §13.6e |
| **C-056-05** | No universal package is established. | §13.7a; RMS §4 |
| **C-056-06** | No Record Model is a package template for another. | I-101 |
| **C-056-07** | A MODEL-DESIGN-INPUT row is not a requirement. | §13.6d |
| **C-056-08** | I-107's provisionality rule is preserved. | I-107 |
| **C-056-09** | A similar package shape does not imply semantic inheritance or a universal primitive. | I-101; I-103; §13.6d; §13.9 |
| **C-056-10** | Artifact 055's Relationship Record scope is not widened. | I-102; Artifact 055 |
| **C-056-11** | Artifact 054's temporal obligation is not redefined. | Artifact 054 |
| **C-056-12** | No package schema, field, storage or implementation is created. | Source facts: Roadmap row 056 — `T: doc` · `R: CONTRACT`; Roadmap PART I per-directory rules — `docs/**` prohibits *"implementation detail"*; Roadmap §0.5 RULE G — *"A specification and a schema are always separate artifacts"*; Blueprint §13.9 — *"The package is logical and semantic"*. Effect: 056 is a contract document and defines none of them. |
| **C-056-13** | No invariant is minted or amended. | Blueprint §36, §10.4; P-28; I-15 |
| **C-056-14** | Each model's own architecture establishes and retains its package decision. | §13.6d; I-107 |
| **C-056-15** | No Registry package decision is exported as another model's requirement. | I-105; §13.6e |

A construction satisfying all fifteen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 17. Worked Examples

> **Illustrative and non-normative.** None is a schema or a downstream design decision.

**Example 1 — World.** A World CHARACTER is packaged as its Record, its Relationship Record and its
History Record. That shows World's ownership of World's package, nothing more.

**Example 2 — Epistemic.** E's package artifact (279) concludes that E's Records need a package
resembling World's. That is E's decision; it imports no World semantics (I-101, I-103).

**Example 3 — Production.** P's architecture concludes that its package has no Relationship Record.
That is a valid Production decision if P's own architecture supports it. 056 does not decide it.

**Example 4 — Registry.** Registry decides how its definition Records are packaged (060). That
decision gives Registry no say over the package of any World, E, P, V or I Record.

**Example 5 — Visual.** V's architecture uses a structure resembling a Relationship Record for its
specifications. It is a Visual construct, not World's Relationship Record and not a universal one
(§13.9; Artifact 055).

**Example 6 — the anti-pattern.** An implementer reads World's package and copies it to E, P, R, V
and I. **Invalid** (§13 above).

## 18. Source Traceability

| Rule | Source |
|---|---|
| Each model owns its packaging | Blueprint §13.6d; I-90; RMS §6 |
| Package is logical, not storage | Blueprint §13.9; RMS §4 |
| World package established | Blueprint §13.6d, §13.9; I-72; RMS §7 |
| E, P, V, I model-owned; R Registry-owned | Blueprint §13.6d |
| Model sovereignty; no template | I-101 |
| Shared infrastructure ≠ shared semantics | I-103; Blueprint §13.7a |
| Design-input rows provisional; not a freeze | I-107; Blueprint §13.6d |
| Changing a package: Foundational ceremony, both documents, no other model's agreement | Blueprint §13.6d, §13.7 |
| Relationship Record and History Record World-only | I-102; Artifact 055 |
| No universal package, History Record, Relationship Record, lifecycle | Blueprint §13.7a; RMS §4 |
| Registry sovereign; owns its own package; not others' Records | Blueprint §13.6d, §13.6e; I-105 |
| Invariants are the Blueprint's; changed only by Constitutional Amendment | Blueprint §36, §10.4; P-28; I-15 |
| Temporal obligation | Artifact 054 |
| Relationship boundary | Artifact 055 |
| Commit-set shape follows the owning model's packaging | Roadmap row 153 |
| Acceptance | Roadmap row 056 |
| Downstream package artifacts | Roadmap rows 060, 202, 237, 279, 340 |

## 19. Downstream Boundaries

| Artifact | Specifies |
|---|---|
| **054** | the temporal obligation and model-owned temporal mechanism |
| **055** | the relationship boundary and the World-scoped Relationship Record |
| **056** | the package ownership boundary — this contract |
| **057** | Kind admission |
| **058** | cross-model dependency rules |
| **153** | the commit set — row 153: *"commit-set shape follows the owning model's packaging"* |
| **202 · 237** | World's package and the WSV package rule |
| **279** | E's package — row 279: *"E-owned, declared by E"* |
| **340** | P's package — row 340: *"package P-owned"* |
| **060** | the Registry Record Model, including its own package |
| V and I model architectures | their own packages |

**Roadmap condition recorded, not resolved.** Rows 060, 153, 202, 279 and 340 name 056 as a hard
dependency. No Roadmap row names a Visual or Issue package artifact. V's and I's package decisions
remain theirs (§13.6d); this contract names no artifact for them and adds no dependency edge.

## 20. Final Contract Statement

Package architecture is owned by the Record Model that owns the Records. World's established
package is World-specific. Registry owns the packaging of Registry Records. Epistemic, Production,
Visual and Issue own their own package architectures. No package composition is universal merely
because it exists in World, appears in a Blueprint design-input row, or is shared by several
models. A MODEL-DESIGN-INPUT row for a model not yet independently designed is provisional and may
not be implemented as a requirement. This contract defines the package boundary only; it defines
no model's concrete schema.

---

*Artifact 056 · P2/2d · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the package boundary — packaging model-owned, World established, Registry
Registry-owned, no universal package — derived from Blueprint §13.6d and §13.9, RMS §6 and §7, and
I-72, I-90, I-101, I-103, I-105 and I-107. It does not amend them and defines no schema. Where it
differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those
governing sources are correct and this document is wrong.*
