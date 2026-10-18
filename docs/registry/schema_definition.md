# COOLBOY12 — SCHEMA-DEFINITION Specification

**Artifact 076** · SCHEMA-DEFINITION spec · `docs/registry/schema_definition.md` · Own: R · RM: R ·
T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining · Canon: canonical-about-meaning · CD: yes ·
Ph/St: P3/3b · Req: RR-17 · BP: §9.4 · RMS: §10.1 · H: 064 · S: — · LS: LS-1 · G: — · → 077 ·
Val: definition resolves; versionable; references only declared entities (063) · Done: Registry
**defines** schemas; **does not execute** them · Why: closes the schema/runtime ambiguity ·
Risk: high · ∥: yes

## 1. Purpose

This specification answers one question — **what is a Registry `SCHEMA-DEFINITION` Record, what may
its definition govern, and how can consumers resolve and evolve that definition without turning the
Registry into the component that executes schemas?**

COOLBOY12 keeps five things apart that are easy to merge. Shown for the World Kind `CHARACTER`:

```
SCHEMA-DEFINITION, the Kind         Kind 5 of RMS §10.1's fourteen; its admission rationale is
                                    Artifact 064 §12
a SCHEMA-DEFINITION Record          an R-partition Registry Record: the governed definition of one
                                    schema (RMS §10.2; 064 §12 question 1)
the schema it defines               structure and applicability — "required fields, cardinality,
                                    constraints, applicable Model and Kind" (064 §12 question 2)
Records the schema applies to       owned by their own Record Model — a Character Record is World's
                                    (Artifact 061 §7 row 8; I-105)
schema implementation               the runtime that checks Records against a schema — shared
                                    structural validation, not Registry runtime (RMS §10.2, §4, §20)
```

The rule this document exists to state is Row 076's `Done`, and RMS §10.2's:

> **Registry defines schemas. Registry does not execute schemas.**

`SCHEMA-DEFINITION` already exists. It is Kind 5 of RMS §10.1's *"Final Kind taxonomy — CLOSED at
fourteen"*, and Artifact 064 §12 records its admission rationale. This document specifies the
family; it admits nothing.

## 2. Constitutional Status

This document is the AUTHORITATIVE specification of the `SCHEMA-DEFINITION` Registry definition
family, under the Record System. It is:

- **not a Record.** It carries no envelope, no `object_id`, no provenance value and no
  `registry_ref`. No `SCHEMA-DEFINITION` Record is created, materialized or committed by it.
- **not the structural schema of the family.** How a `SCHEMA-DEFINITION` Record is structurally
  represented is Artifact 077's (`docs/registry/schema_definition.schema`, `H: 076`).
- **not a schema.** It defines no schema for any Kind, and states no field list, requiredness or
  cardinality for any Record of W, E, P, V or I.
- **not an implementation.** It defines no validator, parser, resolver, schema engine, API or
  service, and no Registry runtime.
- **not a canonicalization source.** Roadmap §0.8 names the canonicalization sources — rows 075,
  085, 105, 106, 107 — and row 076 is not one of them. Its AD-REG-SOURCE-ENVELOPE source-projection
  rule therefore does not apply to this file.
- **not canonical data.** It lies outside `canon/**`. Committed Registry Records are written only by
  the Mutation Coordinator (row 152), the sole writer of `canon/**`, after G-CANON-R (Roadmap §0.8).

Row 076's `Canon: canonical-about-meaning` and `CD: yes` are preserved exactly; how they sit beside
Artifact 003's docs-specification convention is recorded, not resolved (SC-076-M).

Where this document differs from the Master Blueprint, the Record Model System or the OS File Build
Roadmap, those sources are correct and this document is wrong.

## 3. Scope

**Artifact 076 owns** the family-level semantic contract of a `SCHEMA-DEFINITION`:

- what a `SCHEMA-DEFINITION` Record is, and how it differs from its Kind, the schema it defines,
  the Records the schema applies to and the schema's implementation (§6);
- what a schema definition may govern, and how far each permission reaches (§7);
- the schema side of the schema/field split, as far as current sources establish it (§8);
- the definition/execution boundary, stated in testable terms (§9);
- the resolution, versionability and reference obligations of row 076's `Val` (§10–§12);
- the ownership, canonicality and envelope boundaries the family must hold (§13–§14);
- the family rules (§16), worked cases (§17), prohibited inferences (§18), source conditions (§19)
  and conformance conditions (§20), and the handoff to 077 (§21).

**Artifact 076 does not own, and does not pre-build:**

| Not decided here | Owner |
|---|---|
| The Registry Kind taxonomy and `SCHEMA-DEFINITION`'s admission | 064 (`H`); Kind admission 057; new Kinds 459 |
| The structural representation of a `SCHEMA-DEFINITION` Record | 077 |
| Final closure of the `SCHEMA-DEFINITION` / `FIELD-DEFINITION` overlap | 078 (`H: 076,072`) |
| Field meaning and domain | 072 (FIELD-DEFINITION spec), 073 |
| Definition evolution, versioning, supersession, deprecation | 108, 109, 110 |
| Who may propose, approve or deprecate a definition | 065 |
| Registry dependency direction, asymmetry and cycles | 111 |
| The Registry reference validator | 112 |
| Constraint–rule binding | 113 |
| Create/resolve/version operations; consumer resolution by id+version | 114; 115 |
| Registry validation suite; lockstep tests; P3 conformance | 116; 123; 124 |
| Canonical gates; the sole canonical writer | 145; 152 |
| Any model's own schemas and Records | that Record Model's rows (e.g. 182–196 for World) |

## 4. Governing Sources and Precedence

**Precedence.** Blueprint and RMS are architectural authority; where the Blueprint's earlier wording
and a later explicit RMS correction differ, the correction governs (SC-076-A, SC-076-B). The
Roadmap, including its author revisions in §0.7 and §0.8, governs decomposition and order. Frozen
artifacts are consumed within their own responsibilities. This document amends none of them.

| Source | What it gives this specification | Role |
|---|---|---|
| Roadmap row 076 | identity, `Val`, `Done`, `H: 064`, `LS: LS-1`, `→ 077` | build authority |
| **Artifact 064** (`docs/models/registry/kinds.md`) §6, §12 | the Kind `SCHEMA-DEFINITION` and its fourteen-question admission rationale | **the only hard dependency** |
| RMS §10.1; §10.2 | the fourteen Kinds; the schema boundary | constitutional |
| RMS §4; §5; §6; §6.1 | universal mechanisms, the seven-field envelope and nine prohibitions; the identity grammar; model ownership; *"Definition … Governs; never instantiates"* | constitutional |
| RMS §10.3; §10.6; §15; §19; §20; Appendix H PC-3 | the reference boundary; constraint vs validation; Registry relationship definitions; shared validation; the four validation tiers; the schema/field overlap | constitutional |
| Blueprint §9.4; §13.6e; §13.7 | schema structure vs shared meaning; Registry definitions are Records; definition vs ownership; lockstep custody | constitutional |
| Blueprint §12.6; §12.15; §26.3b | external engines may run schema checks without redefining authority; JSON Schema verdicts are DERIVED | constitutional |
| Roadmap §0.7; §0.8; PART III; rows 077, 078, 108–116, 182–196 | self-hosting; authoring vs canonical materialization; LS-1; downstream owners; model-owned schemas | build authority |
| Artifacts 060, 061, 062, 063 | Registry model; authority table (§7 row 8); layers; reference boundary | constraint, not `H` |
| Artifacts 072, 073 | the field side of the schema/field split | constraint, not `H` |
| Artifacts 003, 033, 052, 057, 065, 068, 070 | conventions; envelope; canonicality; admission; governance; family-spec precedent | context, not `H` |

Reading a source here does not promote it into `H`. Artifact 063 binds the reference boundary
through row 076's `Val`; Artifact 072 binds the field side through row 078's `H`. Neither becomes a
hard dependency of 076.

## 5. Inherited Contract from Artifact 064

Artifact 064 is consumed unchanged. Its §12 is the Kind-level boundary this family stays inside;
this document does not reopen admission, re-answer the fourteen questions, or change the roster.

| 064 §12 | Inherited fact | Basis |
|---|---|---|
| Q1 | the semantic object is *"the governed definition of a schema"* | RMS §10.2 |
| Q2 | the semantic question is *"what structure does this schema define — required fields, cardinality, constraints, applicable Model and Kind?"* | RMS §10.2 |
| Q3 | *"a schema definition is a Registry Record with its own version and supersession"* | RMS §10.2; F-1 |
| Q4 | persistent state is *"the schema's defined content; detail is 076's"* | RMS §10.2; row 076 |
| Q5 | version and supersession apply; *"their rules are 108–110's"* | RMS §10.2; F-4 |
| Q6 | *"Registry defines the schema; the Records that conform stay with their model; no execution authority"* | F-3; Artifact 061 §7 row 8 |
| Q7 | what references it is *"not established"*; the *"validation references"* RMS §10.2 lists *"are references a schema defines, not references to it"* | row 077; RMS §10.2 |
| Q8 | *"a schema composes fields and owns cardinality, requiredness and order; it is not one field"* | row 078 |
| Q9–Q12 | not a state, not an edge, not a subtype of `FIELD-DEFINITION`, not a projection — *"the runtime that executes it is not a Record"* | F-5–F-7; RMS §10.1, §10.2 |
| Q13 | not reducible to `FIELD-DEFINITION`: a schema holds composition across many fields; a field definition holds one field's meaning | RMS §10.2; row 078 |
| Q14 | without the Kind, *"schema meaning falls back into runtime or configuration"* — row 076's *"schema/runtime ambiguity"* | row 076 `Why` |

Q4 hands this document *"detail"*; this document takes the semantic detail and leaves the
structural detail to 077.

## 6. What a SCHEMA-DEFINITION Is

**SOURCE FACT.** *"SCHEMA-DEFINITION is a Registry Record. Schema implementation is not Registry
runtime."* (RMS §10.2). A Registry definition is *"A Registry Record specifying meaning"* that
*"Governs; never instantiates"* (RMS §6.1). Registry definitions *"are Records"* with *"identity
under the universal grammar (§13.9a), provenance, a governed change path, and a temporal account"*
(Blueprint §13.6e).

**Definition.** A `SCHEMA-DEFINITION` is an R-partition Registry Record that governs the definition
of one schema: the structure the schema defines and the scope to which that structure applies (064
§12 questions 1–2). Any applicable Record Model or Kind it identifies is a declared one. How many it
may identify, and whether both are always present, is not established (SC-076-N). It is
authoritative about that definition. It is not executable.

**Five levels, never collapsed.**

| Level | What it is | Owner |
|---|---|---|
| the Kind `SCHEMA-DEFINITION` | one of RMS §10.1's fourteen Registry Kinds | Registry, by its own Kind architecture (064) |
| a `SCHEMA-DEFINITION` Record | one governed definition of one schema, with its own identity | Registry |
| the schema defined | structure and applicability, as the Record defines them | defined by the Record; not a separate owner |
| the Records the schema applies to | Records of the applicable model, e.g. Character Records | that Record Model (World for `CHARACTER`) |
| the schema's implementation | the runtime that checks Records against the schema | shared structural validation (RMS §4, §19, §20); not a Record |

**What a `SCHEMA-DEFINITION` is not.**

- not the Kind it applies to, and not that Kind's `KIND-DEFINITION`: what a Record of a Kind *is*
  is `KIND-DEFINITION`'s (064 §9); what structure applies to it is the schema's;
- not a `FIELD-DEFINITION` and not a collection that replaces field meaning (§8);
- not a Record of the applicable Kind, and the creator of none;
- not the Kind's admission: a schema applicable to a Kind neither admits nor declares that Kind;
- not the schema's implementation, a validator, a parser or a check run (§9);
- not Artifact 077. 077 is an authored structural contract for `SCHEMA-DEFINITION` Records
  (Roadmap §0.8 lists it among the structural contracts); it is not itself a `SCHEMA-DEFINITION`
  Record. The same holds for the other Registry structural contracts — 069 says of itself that it is
  *"not a SCHEMA-DEFINITION Record, not the schema of any defined Kind's Records"* (069 STATUS).

**Model-owned schemas.** The Roadmap also carries model-owned schema artifacts — row 184
*CHARACTER schema*, `canon/world/character.schema`, `Own: W`, `Canon: canonical`, `G: G-CANON-W`.
Whether such a schema is described by, declared through or independent of a Registry
`SCHEMA-DEFINITION` Record is not established by any source, and this document does not decide it
(SC-076-I). What is established holds either way: a Registry `SCHEMA-DEFINITION` never makes a
model's Records, or that model's own schema artifacts, Registry-owned (§13).

## 7. What a Schema Definition Governs

RMS §10.2: *"Registry may define: required fields · cardinality · constraints · version ·
supersession · applicable Model · applicable Kind · relationships · validation references."*

**Permission is not a mandatory element.** *"may define"* states what a `SCHEMA-DEFINITION` is
permitted to govern. It does not make each listed category a separate, required element of every
`SCHEMA-DEFINITION` Record. How each is carried, and which are required, is 077's to encode within
this specification; version and supersession representation is 108–110's (§11).

**What every `SCHEMA-DEFINITION` answers.** REQUIRED SYNTHESIS from 064 §12 question 2 and RMS
§10.2: every `SCHEMA-DEFINITION` states the structure its schema defines and the declared scope it
applies to. A schema definition that applied to nothing, or defined no structure, would not answer
its Kind's semantic question.

| Category | Source | What it means at family level | Not decided here |
|---|---|---|---|
| **Applicable Model · applicable Kind** | RMS §10.2; 064 §12 Q2 | the scope whose Records the schema applies to, stated through the applicable-Model and applicable-Kind categories; any Model or Kind named is declared and is named by declaration reference (§12, RF-076-1) | how many Models or Kinds one schema may name; whether both are always present; whether a schema may apply at Model level without a Kind; the structural form (SC-076-N) |
| **Required fields** | RMS §10.2; Blueprint §9.4 (*"A field's existence is schema"*) | which fields occur in the structure and which are required; the composition respects the meaning and domain each field's `FIELD-DEFINITION` governs (§8; RF-076-2) | how a schema identifies the fields it composes — no reference carrier is fixed (077); final composition semantics (078) |
| **Cardinality** | RMS §10.2; 064 §12 Q8 | how many values a field occurrence may carry in the structure | its representation (077) |
| **Requiredness** | Blueprint §9.4 (*"required-ness"*); RMS §10.2; 064 §12 Q8 | whether a field occurrence is mandatory in the structure | its representation (077) |
| **Order** | 064 §12 Q8; row 078 `Done` | assigned to the schema side by row 078's closure target | whether and how order is carried — 078 closes it, 077 encodes it |
| **Types · defaults** | Blueprint §9.4 (*"fields, types, required-ness, defaults"*) | schema-side structure, never a field definition's (072) | whether a `SCHEMA-DEFINITION` Record carries them — RMS §10.2 does not list them (SC-076-K) |
| **Constraints** | RMS §10.2; RMS §10.6, §20 | conditions the structure states for its Records | whether a schema's constraints are its own content or references to `CONSTRAINT-DEFINITION` Records (SC-076-J) |
| **Relationships** | RMS §10.2; RMS §15, row R (*"Relationship definitions; never runtime relationship ownership"*) | relationship structure the schema states, as definition content | what *relationships* denotes in RMS §10.2 and what, if anything, it references (SC-076-J) |
| **Validation references** | RMS §10.2; 064 §12 Q7 (*"references a schema defines, not references to it"*) | references the schema definition carries to how its structure is to be checked | the target family and form (SC-076-J) |
| **Version · supersession** | RMS §10.2; 064 §12 Q3, Q5 | the definition is versionable and supersedable | all representation and mechanics (108–110; §11) |

Every row is a definition. None is an instruction executed by the Registry (§9).

## 8. SCHEMA-DEFINITION vs FIELD-DEFINITION

**SOURCE FACTS.**

- Blueprint §9.4: *"Schema defines the structure of a record — fields, types, required-ness,
  defaults. The Registry defines the shared meaning those fields carry across kinds. A field's
  existence is schema; what "status" means everywhere it appears is Registry."*
- RMS §10.2 makes `SCHEMA-DEFINITION` a Registry Record, so structure is also Registry-governed —
  as a definition, never as execution (SC-076-C).
- RMS Appendix H, PC-3: *"Registry SCHEMA-DEFINITION and FIELD-DEFINITION overlap at the edges (a
  schema is partly a set of field definitions)"* — *"Future extension — resolve during Registry
  schema design; no architectural contradiction"*.
- Row 078 `Done`: *"overlap resolved — a schema composes field definitions and owns
  cardinality/required/order; a field definition owns meaning and domain"*; its `Why`: *"audit DG-03
  closed here, not deferred"*; its `H`: 076, 072.
- Artifact 072 §11 holds the field side: a `FIELD-DEFINITION` holds one field's meaning and domain,
  and no cardinality, requiredness, order, type or default.

**The minimum split, as current sources establish it.**

| Concern | Responsible | Basis |
|---|---|---|
| What a field means | `FIELD-DEFINITION` | Blueprint §9.4; 064 §11; 072 |
| The domain over which that meaning holds | `FIELD-DEFINITION` | 064 §11; row 078; 072 §8 |
| Which fields a schema's structure contains | `SCHEMA-DEFINITION` | Blueprint §9.4; RMS §10.2 |
| Requiredness and cardinality within a schema | `SCHEMA-DEFINITION` | RMS §10.2; Blueprint §9.4; row 078 |
| Field order within a schema | schema side, by row 078's closure | row 078; 064 §12 Q8 |
| Field type and default | schema-side structure | Blueprint §9.4; 072 SC-072-E; SC-076-K |
| Applicable Model and Kind | `SCHEMA-DEFINITION` | RMS §10.2 |
| Runtime enforcement of any of these | neither: shared structural validation | RMS §4, §20 |

**What this document establishes — the schema side only.** A `SCHEMA-DEFINITION` defines a
structure that contains fields; it does not define what any field means. Composing a field into a
schema leaves that field's `FIELD-DEFINITION` the sole holder of its meaning and domain, and a
schema definition does not redefine, narrow or restate field meaning by containing the field.

**What it leaves to row 078.** Final overlap closure is 078's, exactly as its row assigns it. This
document does not declare PC-3 closed. It adds nothing to row 078's exit criterion. It does not
decide how a field's semantic domain relates to a schema's applicable Model and Kind — Artifact 072
records that relation as unstated (SC-072-G), and it stays unstated here (SC-076-D).

> **Artifact 078 owns final overlap closure. Artifact 076 does not preempt it.**

## 9. Definition vs Execution

**SOURCE FACTS.**

- RMS §10.2: *"Schema implementation is not Registry runtime."* · *"Registry does not execute
  schemas."*
- RMS §4: structural validation is a universal mechanism — *"Well-formedness precedes meaning"*;
  *"Semantic validation is model-owned"*.
- RMS §19: validation is a *shared* capability; *"definition management"* is Registry's.
- RMS §20: four tiers — constitutional invariant · `CONSTRAINT-DEFINITION` · `VALIDATION-RULE` ·
  *"implementation validation (runtime, structural, shared)"*.
- RMS §6.1: a Definition *"Governs; never instantiates"*.
- Blueprint §9.4: *"The Registry holds no commands and no runtime behavior."*
- Blueprint §12.6: *"a validation engine may run schema checks … None of them may redefine
  authority."*
- Blueprint §12.15 and §26.3b: structural validation is realized by JSON Schema; the components
  *"validate structure"*, and their output is a *"DERIVED verdict"*.
- Artifact 061 §7 row 8: Registry never infers *"execution of the schema"*; Artifact 060 §15 places
  *"the code that validates or executes against the schema"* outside the Registry Record.

**The boundary, in testable terms.** A `SCHEMA-DEFINITION`, and the Registry through it, does not:

1. parse, load or apply a schema to a Record;
2. run a structural check, or produce or hold a check's verdict;
3. accept, reject or block a Record;
4. create, instantiate, mutate, repair or migrate any Record;
5. hold runtime validator state, configuration, sessions or caches;
6. own or schedule the process that loads or applies the schema;
7. admit, declare or create a Kind or a Record Model;
8. confer canonical status, validity or authority on a conforming Record;
9. become the Mutation Coordinator, a gate or a write path.

A check that runs against a schema is implementation validation (RMS §20), performed by a shared
mechanism (RMS §4, §19). Its verdict is DERIVED (§26.3b): it is never Registry content and never
authoritative about the schema's meaning. Where a schema definition carries a validation reference
(§7), the reference states which checking is meant; it grants no authority to execute it.

| Case | Legal? | Why |
|---|---|---|
| a `SCHEMA-DEFINITION` states that a field is required in Records of a declared Kind | yes | a definition of structure (RMS §10.2) |
| a structural validator reads that definition and checks a Record | yes — outside the Registry Record | shared implementation validation (RMS §4, §20) |
| the validator's verdict is stored as a property of the `SCHEMA-DEFINITION` | no | a verdict is DERIVED (§26.3b); the definition holds no runtime state |
| a `SCHEMA-DEFINITION` carries code that rewrites non-conforming Records | no | *"Registry does not execute schemas"*; Registry may not mutate domain instances (RMS §10.3) |
| a validation engine's behaviour is treated as what the schema means | no | external components may run checks but *"None of them may redefine authority"* (§12.6) |

## 10. Identity and Resolution

Row 076 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-076-1** | A `SCHEMA-DEFINITION` is a Registry Record with independent identity (064 §12 Q3). Once materialized it carries ordinary Record identity under the universal grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` and the seven-field envelope (RMS §4, §5) — the baseline identity that later Registry-definition resolution requires. |
| **RS-076-2** | That identity is the R Record's own. It is not the schema's name or label, not a field name, not the identity of the applicable Kind or of any of its Records, not a file name, and not the identity of any implementation that checks the schema. The slug is decoration only and never the basis of resolution (RMS §5). No Registry Kind code is minted or assumed: identity binding is row 117's. |
| **RS-076-3** | A consumer must be able to resolve a materialized `SCHEMA-DEFINITION`. Reference resolution is universal and mechanical (RMS §4), and *"Reference resolution is not Registry work"* (Blueprint §9.4). Create, resolve and version operations are row 114's (*"create/resolve/version a definition"*); consumer resolution by id and version is row 115's (*"consumer resolves by id+version"*). This document does not supply the complete id+version representation; version representation is 108–110's. |
| **RS-076-4** | **Resolvable ≠ legal.** A `SCHEMA-DEFINITION` that resolves is not thereby a legal reference target for every referrer, and a target that the definition names is not legal because it resolves (Artifact 063 §11; §12). |
| **RS-076-5** | **Resolution is not execution.** Resolving a `SCHEMA-DEFINITION` returns a definition; it runs no check, applies the schema to nothing, and transfers no Record, authority or canonicality. |
| **RS-076-6** | No resolver, lookup function, index, cache, store path, fallback, version-selection logic, resolver API or runtime reference evaluation is defined here; how a consumer finds the schema definition that applies to a given Kind is not defined here (114, 115, 077). |

## 11. Versionability Boundary

Row 076 `Val`: *"versionable"*.

**SOURCE FACTS.** RMS §10.2 lists *"version · supersession"* among what Registry may define for a
schema. 064 §12 Q3: *"a schema definition is a Registry Record with its own version and
supersession"*; Q5: *"their rules are 108–110's"*. Registry definitions have *"a governed change
path, and a temporal account"* (Blueprint §13.6e). Row 108 owns the evolution model (`Val`:
*"version"*; `Done`: *"temporal account without a World History Record"*); row 109 owns versioning
(*"consumers pin a version"*); row 110 owns supersession and deprecation.

| ID | Obligation |
|---|---|
| **VS-076-1** | A `SCHEMA-DEFINITION` participates in governed Registry definition evolution and must be capable of being versioned and superseded under the model rows 108–110 define. Every version stays bound by this specification. Its temporal account is the Registry's own: no World History Record is used or required (row 108; I-102). |
| **VS-076-2** | **Not defined here ≠ forbidden.** That this document defines no version mechanism is not a decision that a `SCHEMA-DEFINITION` carries no version, supersession or deprecation information. Rows 108–110 keep their authority to establish the Registry-owned representation, and nothing here asks 077 to close it. Whatever they establish stays Registry-owned: it adds no field to the universal envelope and is not a version, lifecycle or state model shared by W, E, P, V or I (RMS §4, §16). |
| **VS-076-3** | Evolving a `SCHEMA-DEFINITION` changes a definition, not Records. Changing or superseding a schema definition does not by itself migrate, rewrite or revalidate any Record of any model. Any later model-owned or governed response to the change is outside Artifact 076 and remains subject to the applicable contracts; this document neither requires nor forbids one. |

**Not decided here** (108–110): a version field or identifier; numbering; revision identifiers;
*latest* semantics; pin representation; supersession, replacement or deprecation representation;
deprecation states; effective dates; compatibility; migration procedures; version selection;
retention; deletion. Who may propose, approve or deprecate a schema definition is 065's.

## 12. Reference Boundary

Row 076 `Val`: *"references only declared entities (063)"*. RMS §10.3: *"Registry MAY reference:
other Registry definitions · declared Record Models · declared Kinds · declared schemas · declared
semantic contracts."* · *"Registry MAY NOT: own domain instances · depend on runtime instances ·
mutate domain instances · use domain instances as semantic authority."* Artifact 063 binds this
family as a constraint and leaves to each family *"which concrete reference relations each family
carries"* (063 §22). For this family the answer is below.

| ID | Rule | Basis |
|---|---|---|
| **RF-076-1** | **Named applicability targets are declared.** Any applicable Record Model a schema definition identifies is a declared Record Model; any applicable Kind it identifies is a declared Kind of its owning model, whose declared status is established by that model's own Kind architecture. These are declaration-level targets (063 §8.2, §8.3) — not domain instances, and not automatically references to `MODEL-DEFINITION` or `KIND-DEFINITION` Records. This is the family's one source-established concrete relation. It does not determine how many such targets a schema may identify, or whether every definition names both categories (SC-076-N); it defines no declaration state or proof format; an undetermined target is not legal (063 RB-6). Its structural form is 077's. | RMS §10.2, §10.3; 064 §12 Q2; Artifact 063 §7 rows 2–3, RB-1, RB-6 |
| **RF-076-2** | **Governed field composition, without an invented reference carrier.** A schema definition describes the fields its structure contains, and that composition respects the meaning and domain each field's `FIELD-DEFINITION` governs: *"A schema that carries the field conforms to the field's definition"* (072 §10); row 078: *"a schema composes field definitions"*. A field occurrence is a structural element of the schema; it is not thereby a concrete Record reference, and no source fixes how a schema identifies its fields. Where a schema definition does carry a concrete reference to a field, RMS §10.3 has no declared-field category and 063 §7 says such targets *"are reached as Registry definitions (row 1)"*: the reference is an R → R reference to a `FIELD-DEFINITION` Record, its target must actually be one (063 RB-1, RB-6), and the relation must satisfy Artifact 063. R → R references are permitted, not required (RMS §10.3). Final composition is 078's; structural representation is 077's. | RMS §10.2, §10.3; Blueprint §9.4; Artifact 072 §10; Artifact 063 §7, §8.1, RB-1, RB-5, RB-6; row 078 |
| **RF-076-3** | **Validation references, where carried, target admissible categories only.** RMS §10.2 permits them, and 064 §12 Q7 makes them references the schema defines. A `VALIDATION-RULE` is a Registry definition (an admissible R → R target, 063 row 1); a runtime validator, validator process or engine never is (063 row 8). Which family a validation reference targets is not stated by any source (SC-076-J). | RMS §10.2, §10.6, §20; Artifact 063 §7 rows 1, 8 |
| **RF-076-4** | **Constraints and relationships carry no invented reference.** If a schema's constraints or relationships are expressed as references, each target must lie in an admissible category (e.g. a `CONSTRAINT-DEFINITION` or `RELATIONSHIP-TYPE-DEFINITION` is an R Record, 063 row 1). Whether they are references at all is not established (SC-076-J); none is created here. | RMS §10.2, §10.6, §15; Artifact 063 RB-5 |
| **RF-076-5** | **Declared ≠ definition Record.** A declared schema (RMS §10.3) is not automatically the same referent as a `SCHEMA-DEFINITION` Record; a declared Model is not a `MODEL-DEFINITION`; a declared Kind is not a `KIND-DEFINITION`; a field is not its `FIELD-DEFINITION`; a Record conforming to a schema is not a schema declaration. How a schema acquires declared status is not established (063 §8.4; SC-076-I). No reference field is invented for any of these distinctions. | Artifact 063 §8.2–§8.4; RMS §10.3 |
| **RF-076-6** | **Admissible category ≠ family relation.** Other Registry definitions, declared schemas and declared semantic contracts are admissible categories; that obliges no `SCHEMA-DEFINITION` to reference any of them. No reference to a `MODEL-DEFINITION`, a `KIND-DEFINITION`, another `SCHEMA-DEFINITION`, a `CONTROLLED-VOCABULARY` or any other definition, and no schema inheritance, inclusion or extension relation, is created here. Not created here ≠ forbidden later. | Artifact 063 RB-5, §22 |
| **RF-076-7** | **No domain instance.** No Record of W, E, P, V or I — a Character Record, an Epistemic knowledge-state Record, a Production planning Record, a Visual asset Record, an Issue publication Record — and no Record that conforms to the schema or illustrates it, is a reference target, a dependency or the semantic authority of a `SCHEMA-DEFINITION`. A Record's successful validation never licenses a reference to it. | RMS §10.3; Artifact 063 §7 row 6, §9 |
| **RF-076-8** | **No domain state.** No current World-state value (e.g. a WSV indicator value) is the semantic authority of a schema definition. | RMS §10.7; Artifact 063 §7 row 7 |
| **RF-076-9** | **No runtime instance.** No live schema engine, validator process, check run, session, worker or service is a target, a dependency or the semantic authority of a `SCHEMA-DEFINITION`. | RMS §10.3; Artifact 063 §7 row 8, §13 |
| **RF-076-10** | **Resolvable ≠ legal; no transfer.** A target that resolves mechanically may still be illegal, and an undetermined target is not legal. A legal reference transfers no ownership, mutation authority, semantic authority, admission, canonicality or source-of-truth class. | Artifact 063 §11, §12 |
| **RF-076-11** | **Reference ≠ dependency.** Naming a declared Model or Kind as applicability is not by itself a semantic dependency; nor is a concrete Registry-definition reference, such as one to a `FIELD-DEFINITION` where it is carried. Neither target becomes semantic authority for the schema definition. A relation established as both a reference and a semantic dependency must also satisfy the dependency rules; concrete direction, asymmetry and cycles are row 111's. `SCHEMA-DEFINITION`'s layer placement is not established (Artifact 062 §6), so no layer-based dependency rule is applied or assigned here. | Artifact 062 D-9, §6; Artifact 063 RB-5; row 111; SC-076-L |

Blueprint §9.4's older wording — *"A Registry definition may never reference a kind, a subtype, or
an instance"* — is not current law for reference legality. RMS §10.3 corrects it (*"v0.1 stated the
boundary too bluntly"*), and Artifact 063 applies the correction (SC-076-B). Domain instances remain
forbidden.

## 13. Authority, Ownership and Canonicality

**Six sovereign Record Models, unchanged.** W · E · P · R · V · I. Registry is R: *"Registry governs
the definitions. Each Record Model owns its Records."* (Blueprint §13.6e; I-105).

| Registry governs | The applicable Record Model keeps | Registry never infers | Source |
|---|---|---|---|
| the definition of a schema (`SCHEMA-DEFINITION`) | the Records that conform to it; their identity, values, lifecycle, authority, canonicality and semantic validation | ownership of conforming Records; execution of the schema | Artifact 061 §7 row 8; RMS §6, §10.2; §13.6e |

- **No transfer by applicability.** A schema definition applicable to World Records gives the
  Registry no World Record, and the same holds for E, P, V and I. Applicability is a declaration
  reference (RF-076-1), not an ownership claim.
- **No transfer by conformance.** A Record that conforms to a schema stays its model's. Conforming
  is not belonging, and failing to conform gives the Registry no authority over the Record.
- **Meaning, never world truth.** *"The Registry owns meaning, never world truth."* (I-88). A schema
  definition asserts no fact of the world.
- **Canonicality.** A committed Registry definition is canonical about meaning: *"This definition is
  the authoritative meaning records resolve against"* (Artifact 052 §5.4). It *"confers no canonical
  status on the Records of other models"* (052 §5.4). Canonicality is model-defined (I-104); a
  schema definition neither grants nor removes it.
- **Authored specification ≠ committed Record.** This document is a P3 family specification. A
  concrete `SCHEMA-DEFINITION` Record exists only when committed through the Mutation Coordinator
  after G-CANON-R (Roadmap §0.8; row 152), on the governed path of Spine law 2. No concrete schema
  definition, and no materialization value of one, is authored here.

## 14. Envelope and Universal-Semantics Boundary

Once materialized, a `SCHEMA-DEFINITION` carries the universal envelope unchanged — `partition` ·
`kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4) — in partition
R. Its envelope `kind` names the Record's own Kind, `SCHEMA-DEFINITION`; it is never the Kind the
schema applies to. The schema definition's own envelope is not the structure it defines for another
model's Records.

No concept in this document — applicability, a field occurrence, requiredness, cardinality, order,
type, default, constraint, relationship, validation reference, version, `status`, `tier`, a
lifecycle or a validator — becomes a universal envelope field. `tier` and `status` are World-owned
and not universal (RMS §4).

None of RMS §4's nine prohibited universal semantics is introduced. For this family that means:

- **no universal semantic schema** — the existence of `SCHEMA-DEFINITION` does not create one schema
  for all six models, and no schema definition becomes a Record schema for W, E, P, R, V and I
  together merely because every model can resolve definitions from the Registry;
- no Universal Record Base assembled from schema structure;
- no Universal Relationship Record arising from the schema's *relationships*;
- no Universal History Record for schema versions;
- no universal lifecycle, state model or `status` arising from a field a schema contains;
- no universal canonicality conferred by conformance;
- no universal Kind taxonomy arising from applicability;
- no universal identity composition from a schema's name or applicability.

## 15. LS-1 and Gate Metadata

Row 076 carries `LS: LS-1`, preserved exactly. Roadmap PART III defines LS-1 as *"every Kind spec ↔
its Registry KIND-DEFINITION. ATOMIC-PAIR."*; Artifact 003 lists it as *Kind ↔ KIND-DEFINITION*. A
`SCHEMA-DEFINITION` family specification is neither a Kind specification nor a `KIND-DEFINITION`.

- **No pair is invented.** 076 ↔ 077 is not an LS-1 pair because one is a specification and the
  other a schema. No new lockstep class, hard dependency, reference or commit atomicity follows from
  the label.
- **The Registry's own pairs stand.** Under AD-LS1-R-BOOTSTRAP (Roadmap §0.7; Artifact 003) the
  Registry's fourteen Kind ↔ `KIND-DEFINITION` pairs are 064 ↔ 075; one of row 075's fourteen
  concerns the Kind `SCHEMA-DEFINITION`. Nothing here replaces that.
- **Lockstep is not sequence and not a reference** (Blueprint §13.7; Artifact 003).

How row 076's label relates to PART III and to 064 ↔ 075 is not stated by any source; it is
recorded, not resolved (SC-076-H).

**Gate and parallelism.** Row 076 carries `G: —`; no gate is introduced. `∥: yes` permits parallel
authoring and waives no hard dependency: 064 exists and is consumed unchanged.

## 16. Family Rules

| ID | Rule | Basis | Evidence |
|---|---|---|---|
| **SD-1** | **Governed schema definition.** A `SCHEMA-DEFINITION` is a Registry Record that governs the definition of one schema. It is not the schema's runtime implementation. | RMS §10.2, §6.1; 064 §12 Q1 | SOURCE FACT |
| **SD-2** | **Independent identity.** Each schema definition is identity-bearing as an R Record. Its identity is not the schema's name, a field name, the applicable Kind's identity, a conforming Record's identity, or an implementation file. | 064 §12 Q3; RMS §4, §5; RS-076-1, RS-076-2 | SOURCE FACT |
| **SD-3** | **Structure, not field meaning.** The family governs structural composition and applicability; field meaning and domain stay `FIELD-DEFINITION`'s. | Blueprint §9.4; 064 §11, §12; 072; §8 | SOURCE FACT |
| **SD-4** | **Declared applicability.** Every schema definition states the scope it applies to, through the applicable-Model and applicable-Kind categories of RMS §10.2. Any Model or Kind it names is declared and named by declaration reference. Applicability creates no Model or Kind, admits nothing, and leaves the model's sovereignty and Kind taxonomy its own. No cardinality is fixed, and whether both categories are always present is not established. | RMS §10.2, §10.3; 064 §12 Q2; RF-076-1; SC-076-N | REQUIRED SYNTHESIS |
| **SD-5** | **Fields, requiredness and cardinality.** The family may express which fields a structure contains, whether each is required, and its cardinality — as structure, not as field meaning. The composition respects each field's governed meaning and domain; no field-reference carrier is required by this rule (RF-076-2). | RMS §10.2; Blueprint §9.4; Artifact 072 §10; row 078; RF-076-2 | SOURCE FACT + REQUIRED SYNTHESIS |
| **SD-6** | **Constraints and validation references, kept apart.** A schema definition may express constraints and validation references. `CONSTRAINT-DEFINITION` (what must hold), `VALIDATION-RULE` (how a condition is checked) and implementation validation (the running check) are never collapsed into the schema definition or into each other. No validator architecture is defined. | RMS §10.2, §10.6, §20; RF-076-3; SC-076-J | SOURCE FACT |
| **SD-7** | **Relationships as definition content.** A schema definition may express relationships. That creates no Relationship Record, no runtime relationship ownership, no arbitrary Registry reference and no mandatory relationship-definition list. | RMS §10.2, §15; RF-076-4; SC-076-J | SOURCE FACT |
| **SD-8** | **No execution.** A schema definition governs a definition; it executes nothing (§9 items 1–9). | RMS §10.2, §4, §20; Blueprint §9.4, §12.6 | SOURCE FACT |
| **SD-9** | **No transfer of ownership.** Applicability and conformance transfer no Record, authority or canonicality to the Registry. | RMS §10.2, §10.3; I-105; 061 §7 row 8; §13 | SOURCE FACT |
| **SD-10** | **Registry-domain evolution.** Schema definitions are versionable and supersedable under Registry-owned rules (108–110), not under a lifecycle shared with other Record Models. | RMS §10.2, §16; 064 §12 Q3, Q5; §11 | SOURCE FACT |
| **SD-11** | **No new Registry Kind.** Creating a schema definition creates no Kind and does not extend the Registry Kind taxonomy. | RMS §10.1; 064; row 459 | SOURCE FACT |
| **SD-12** | **No universal Record schema.** The family creates no universal semantic schema for W, E, P, R, V and I. | RMS §4; §14 | SOURCE FACT |
| **SD-13** | **Legal, not merely resolvable.** Every reference a schema definition carries lies in an admissible 063 category and in a relation this family or its downstream owner establishes; no domain instance, domain state or runtime instance is ever a target or authority. | RMS §10.3; Artifact 063 RB-1–RB-6; §12 | SOURCE FACT |
| **SD-14** | **Permission ≠ required element.** RMS §10.2's *"may define"* list is a permission set; no category becomes a required structural element of every Record by this document. | RMS §10.2; §7 | REQUIRED SYNTHESIS |

## 17. Worked Examples

Every example is **schematic**. No `SCHEMA-DEFINITION` Record is committed, no identifier is
minted, and no concrete schema content is asserted. Identifiers are written schematically: the
Registry Kind code is `<kind>` because none is bound (row 117).

**A. Legal — a schema definition applicable to a declared World Kind.** A `SCHEMA-DEFINITION`
Record `R-<kind>-…` states that its schema applies to the declared Record Model W and the declared
World Kind `CHARACTER`, and defines some structure for Character Records — which fields occur and
which are required. Registry holds the structural definition. World owns every Character Record,
its values and its canonicality. No check runs inside the definition: a shared structural validator
may read the definition and check a Character Record, and its verdict is DERIVED. Nothing here says
what the structure is, how many Models or Kinds a schema may name (SC-076-N), or that this Record
is, or replaces, row 184's World-owned *CHARACTER schema* (SC-076-I).

**B. Illegal — a schema definition acting as a validator.** A Registry definition is made to load a
Character Record, check it, and rewrite the Record's fields where they fail. Rejected: *"Registry
does not execute schemas"* (RMS §10.2); Registry *"MAY NOT … mutate domain instances"* (RMS §10.3);
the check is implementation validation, a shared runtime tier (RMS §20); and the Character Record is
World's (I-105).

**C. Boundary — schema, field, vocabulary and value.** World's `status` field (Blueprint §9.4;
RMS §4: World-owned, not universal). Four responsibilities stay apart:

- **World** owns the `status` value each Character Record carries (§13.6e: *"The values its Records
  carry"*) and its own state semantics: *"each Record Model owns the meaning of its own
  authoritative state"* (Blueprint §13.7c).
- **Registry** governs the applicable `CONTROLLED-VOCABULARY` definition — the per-Kind set of
  permitted terms and what each means: *"the vocabulary is a Registry-owned controlled vocabulary"*
  (§13.7c); *"Registry governs the vocabulary; the model decides which value its Records carry"*
  (064 §14 Q6). Per-Kind sets may diverge, and a forced union is prohibited (§9.4; row 081).
  Governing the vocabulary gives Registry no World Record, state machine or lifecycle.
- The field's **`FIELD-DEFINITION`** governs what `status` means and over what domain (072).
- The **`SCHEMA-DEFINITION`** governs whether `status` occurs in its structure, whether it is
  required and with what cardinality.

Nothing here says `status` is required in any schema or universal anywhere, and no schema →
vocabulary reference is created.

**D. Deferred — a versioned schema definition.** A `SCHEMA-DEFINITION` must be able to evolve: a
later version may change the structure it defines. How versions are identified, how consumers pin
one, how supersession and deprecation are represented, and how resolution chooses a version are
108–110's and 114–115's. No version value, format, history mechanism or migration algorithm is given
here, and a schema definition's change does not by itself rewrite any Character Record (VS-076-3).

**E. Illegal — a domain instance as semantic authority.** A `SCHEMA-DEFINITION` cites
`W-CH-000001-Maximus` as the model of what a Character Record's structure should be. Rejected even
though the identifier resolves perfectly: a domain instance is never a Registry reference target or
semantic authority (RMS §10.3; 063 §7 row 6, §11). *Resolvable ≠ legal.*

**F. Admissible category, unestablished relation.** A `SCHEMA-DEFINITION` is given a reference to a
`CONTROLLED-VOCABULARY` Record. The target is a Registry definition, an admissible category (063
row 1). This family establishes no schema → vocabulary relation, so the category alone does not make
the reference part of the family: admissible category ≠ family relation (063 RB-5; RF-076-6).
Whether such a relation is ever carried is for a governing source to establish.

## 18. Prohibited Inferences

| # | Incorrect conclusion | Correct reading | Basis |
|---|---|---|---|
| 1 | Registry defines a schema, therefore Registry executes it | definition ≠ execution; checks are shared implementation validation | RMS §10.2, §4, §20; §9 |
| 2 | A schema applicable to World makes the Registry owner of World Records | conforming Records stay World's | 061 §7 row 8; I-105; §13 |
| 3 | A `SCHEMA-DEFINITION` is a `FIELD-DEFINITION` | two distinct Registry Kinds | RMS §10.1; 064 §11, §12 |
| 4 | Schema structure and field meaning are interchangeable | structure is the schema's; meaning and domain are the field definition's | Blueprint §9.4; row 078; §8 |
| 5 | A schema definition creates the Kind it applies to | any Kind named as applicability is a declared one; applicability admits or creates nothing | RMS §10.3; 057; §6 |
| 6 | A schema definition creates Records that conform to it | a Definition *"Governs; never instantiates"* | RMS §6.1 |
| 7 | A declared schema is automatically its `SCHEMA-DEFINITION` Record | not established; distinct referents unless a source says otherwise | 063 §8.4; RF-076-5 |
| 8 | A resolvable reference is legal | resolvable ≠ legal | 063 §11; RS-076-4 |
| 9 | Every admissible reference category is a required schema-definition reference | admissible category ≠ family relation | 063 RB-5; RF-076-6 |
| 10 | Applicability transfers authority to the Registry | a declaration reference transfers nothing | 063 §12; SD-9 |
| 11 | Every RMS §10.2 category must be a required structural element in 077 | *"may define"* is a permission | RMS §10.2; SD-14 |
| 12 | Versionability requires 076 to invent a versioning mechanism | mechanics are 108–110's; not defined ≠ forbidden | §11 |
| 13 | A versionable Registry definition needs a World History Record | Registry's temporal account is its own | row 108; I-102 |
| 14 | A Registry schema definition is one universal schema for all six models | no universal semantic schema | RMS §4; SD-12 |
| 15 | A field a schema contains — `status`, a lifecycle — becomes universal | `status` and `tier` are World-owned | RMS §4; §14 |
| 16 | 076 and 077 are an LS-1 pair because one is a spec and one a schema | no pair is invented; 064 ↔ 075 stand | PART III; §0.7; §15 |
| 17 | 076 closes the schema/field overlap assigned to 078 | 078 owns final closure | row 078; §8 |
| 18 | 076 implements validation or Registry resolution | 112–116's | §9, §10 |
| 19 | Artifact 077, or any Registry structural contract, is itself a `SCHEMA-DEFINITION` Record | authored structural contracts are not Records | Roadmap §0.8; §6 |
| 20 | A validator's verdict is part of the schema definition | verdicts are DERIVED and never Registry content | Blueprint §26.3b; §9 |
| 21 | A model-owned schema (e.g. row 184) is Registry-owned, or is a `SCHEMA-DEFINITION` Record | not established; never Registry-owned by inference | row 184; SC-076-I |
| 22 | `SCHEMA-DEFINITION` sits in a known Registry layer | its layer placement is not established | 062 §6; SC-076-L |
| 23 | World owns a `CONTROLLED-VOCABULARY` definition because its Records carry the values | Registry governs the vocabulary definition; World owns the values its Records carry | Blueprint §13.7c; 064 §14 Q6; 061 §7 row 9 |
| 24 | Every field occurrence in a schema is a concrete R → R reference to a `FIELD-DEFINITION` | a field occurrence is structure; a reference exists only where carried, and then satisfies 063 | RF-076-2; RMS §10.3 |
| 25 | Every schema definition names exactly one Model and exactly one Kind | the count and the presence of each category are not established | SC-076-N |

## 19. Source Conditions and Gaps

### SC-076-A — Historical Registry classification — CLOSED

| | |
|---|---|
| **Sources** | Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* RMS §10: *"COLLISION-1 — CLOSED"* — *"Registry is a sovereign Record Model. The §9.4 line is stale and requires a Blueprint wording fix"*; RMS Appendix H PC-1. |
| **Issue** | an older Blueprint line contradicts Registry's sovereignty |
| **Owner / treatment** | closed by RMS §10. This document uses sovereign Record Model R; the Blueprint is not modified. Does not block `Val` or `Done`. |

### SC-076-B — Historical Registry reference prohibition — CLOSED

| | |
|---|---|
| **Sources** | Blueprint §9.4 and §13.6e: *"A Registry definition may never reference a kind, a subtype, or an instance."* RMS §10.3: *"v0.1 stated the boundary too bluntly"* and permits declared Models, Kinds, schemas, semantic contracts and other Registry definitions. |
| **Owner / treatment** | closed by RMS §10.3 and Artifact 063. The two formulations are not averaged; domain instances stay forbidden (§12). Does not block. |

### SC-076-C — "The Registry is not schema" against RMS §10.2 — RECONCILED

| | |
|---|---|
| **Sources** | Blueprint §9.4: *"The Registry is not schema. Schema defines the structure of a record…"* RMS §10.2: *"SCHEMA-DEFINITION is a Registry Record."* |
| **Issue** | whether Registry may hold schema definitions at all |
| **Treatment** | REQUIRED SYNTHESIS, not a contradiction: RMS §10.2 makes the authoritative definition of a schema's structure a Registry Record while keeping schema implementation out of Registry runtime; §9.4's distinction between structure and shared field meaning survives inside the Registry as `SCHEMA-DEFINITION` vs `FIELD-DEFINITION` (§8). Does not block. |

### SC-076-D — SCHEMA/FIELD overlap — DEFERRED TO 078

| | |
|---|---|
| **Sources** | RMS Appendix H PC-3 (*"Future extension — resolve during Registry schema design"*); row 078 `Done` and `Why`; Artifact 072 §11, SC-072-G |
| **Issue** | the final edge between composition and field meaning, including how a field's domain relates to a schema's applicability |
| **Owner / treatment** | row 078. This document states the schema side only (§8) and does not declare PC-3 closed. Does not block. |

### SC-076-E — Versionability without version mechanics — DEFERRED TO 108–110

| | |
|---|---|
| **Sources** | RMS §10.2 (*"version · supersession"*); 064 §12 Q3, Q5; rows 108–110 |
| **Owner / treatment** | the obligation is stated (§11); representation and mechanics are 108–110's. Not defined ≠ forbidden. Does not block. |

### SC-076-F — Requirement text RR-17 — NON-BLOCKING — UNVERIFIED

| | |
|---|---|
| **Sources** | row 076 `Req: RR-17`; Artifact 003 and the Revolving Resolution Note, GAP-C. The current checkout contains no requirement register: `RR-17` appears only in the Roadmap. |
| **Treatment** | `RR-17` is carried exactly; its text is not stated or claimed met. Row 076's `Val` and `Done` are satisfied on their own terms (§22). |

### SC-076-G — Structural representation left to 077 — HANDED OFF

| | |
|---|---|
| **Sources** | row 077 (`H: 076`; `Done: schema`); 064 §12 Q4 (*"detail is 076's"*) |
| **Treatment** | no structural element name, serialization, cardinality, requiredness rule or schema language is defined here; 077 encodes the semantic obligations of §21 within its own `Val`. Does not block. |

### SC-076-H — LS-1 on row 076 — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 076 `LS: LS-1`; PART III LS-1 *"every Kind spec ↔ its Registry KIND-DEFINITION"*; Artifact 003; Roadmap §0.7 (064 ↔ 075) |
| **Issue** | a family specification is neither a Kind spec nor a `KIND-DEFINITION`; no source states how row 076's label relates to PART III's pairs (cf. SC-070-D, SC-072-D, SC-064-J) |
| **Owner / treatment** | the Roadmap author's. The label is preserved; no pair is invented (§15). Route: ROADMAP ISSUE. Does not block. |

### SC-076-I — Model-owned schemas and declared schemas against `SCHEMA-DEFINITION` — SOURCE GAP

| | |
|---|---|
| **Sources** | row 184 *CHARACTER schema* (`canon/world/character.schema`, `Own: W`, `Canon: canonical`, `G: G-CANON-W`) and rows 186–196; row 077 `→ all model schemas`, while no model-schema row lists 077 in its `H`; RMS §10.3 *"declared schemas"*; Artifact 063 §8.4 (*"How they acquire declared status is not established here"*); Blueprint §13.7 (the Record Model Schema custody) |
| **Issue** | whether a model-owned schema artifact is described by, declared through, or independent of a Registry `SCHEMA-DEFINITION` Record; and what makes a schema *declared* |
| **Owner / treatment** | not established by any source, and no current source assigns it to an artifact. This document decides neither question, and holds what is established either way: no model-owned schema or Record becomes Registry-owned, and a declared schema is not assumed to be its `SCHEMA-DEFINITION` (§6, RF-076-5). Route: SOURCE GAP. Does not block 076's `Val` or `Done`. |

### SC-076-J — Constraints, relationships and validation-reference targets — SOURCE GAP

| | |
|---|---|
| **Sources** | RMS §10.2 (*"constraints · … · relationships · validation references"*); RMS §10.6, §20 (`CONSTRAINT-DEFINITION`, `VALIDATION-RULE`); RMS §15; 064 §12 Q7 |
| **Issue** | whether a schema's constraints are its own content or references to `CONSTRAINT-DEFINITION` Records; what *relationships* denotes in a schema; which family a validation reference targets |
| **Owner / treatment** | not stated by any source. This document keeps the tiers apart (SD-6), requires any reference to lie in an admissible category (RF-076-3, RF-076-4) and creates none. 077 encodes no relation the sources do not establish. Does not block. |

### SC-076-K — Types and defaults — SOURCE GAP

| | |
|---|---|
| **Sources** | Blueprint §9.4: schema structure is *"fields, types, required-ness, defaults"*; RMS §10.2 lists neither types nor defaults; Artifact 072 SC-072-E keeps them off `FIELD-DEFINITION`; row 078 `Done` names *"cardinality/required/order"* only |
| **Issue** | whether a `SCHEMA-DEFINITION` Record carries field types and defaults |
| **Owner / treatment** | not established. Types and defaults are schema-side structure and never a field definition's; this document neither requires nor forbids a `SCHEMA-DEFINITION` to express them. Does not block. |

### SC-076-L — Layer placement — SOURCE GAP

| | |
|---|---|
| **Sources** | Artifact 062 §6: *"the §9.4 rows do not place … SCHEMA-DEFINITION … Their layer placement is not established by current sources, and this contract assigns it to no artifact"* |
| **Treatment** | no layer is assigned and no layer-based dependency rule is applied; concrete dependency rules are row 111's (RF-076-11). Does not block. |

### SC-076-M — Row 076 `Canon` metadata on a docs path — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 076 `T: doc · Canon: canonical-about-meaning · CD: yes`; Artifact 003: *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`"*; `CD` *"licenses nothing"* |
| **Owner / treatment** | the Roadmap / convention author's (cf. SC-072-J, SC-066-H). The metadata is preserved; this document creates no canonical data and performs no canonical write. Route: ROADMAP / CONVENTION ISSUE. Does not block. |

### SC-076-N — Cardinality and form of applicability — SOURCE GAP

| | |
|---|---|
| **Sources** | RMS §10.2 (*"applicable Model · applicable Kind"*); 064 §12 Q2 |
| **Issue** | how many Models and Kinds one schema definition may name; whether both categories are always present; whether a schema may apply at Model level without a Kind; how applicability is structurally expressed |
| **Owner / treatment** | not established, and no source assigns it — not to 078, whose closure is the schema/field boundary. This document requires any named Model or Kind to be declared (RF-076-1), keeps applicability meaningful (SD-4), fixes no count and decides no presence rule. If 077 needs a cardinality to encode, it records that choice as its own source condition rather than presenting it as constitutional. Does not block. |

## 20. Conformance Conditions

Class: **STATIC** — checked by reading this document; **CROSS-SOURCE** — checked against the cited
sources; **REPOSITORY** — checked by repository inspection, not provable from this text.

| ID | Condition | Class | Where |
|---|---|---|---|
| **C-076-01** | The header reproduces current Roadmap row 076 exactly. | CROSS-SOURCE | header |
| **C-076-02** | The document is a family specification — not a schema, a Record or an implementation. | STATIC | §2 |
| **C-076-03** | `SCHEMA-DEFINITION` remains one of RMS §10.1's fourteen Registry Kinds. | CROSS-SOURCE | §1, §5 |
| **C-076-04** | No Kind is admitted, created or reclassified. | STATIC | §5, §6; SD-11 |
| **C-076-05** | A `SCHEMA-DEFINITION` is defined as a Registry Record governing the definition of a schema. | CROSS-SOURCE | §6; SD-1 |
| **C-076-06** | Structural meaning and field meaning stay separate. | CROSS-SOURCE | §8; SD-3 |
| **C-076-07** | Any Model or Kind named as applicability is declared and named by declaration reference; no applicability cardinality or presence rule is invented; no ownership transfers. | CROSS-SOURCE | §6, §7, §12, §13; SD-4, RF-076-1, SC-076-N |
| **C-076-08** | Required fields, cardinality and constraints are addressed at the permitted semantic level. | CROSS-SOURCE | §7; SD-5, SD-6 |
| **C-076-09** | RMS §10.2's permissions are not turned into invented mandatory structural elements. | STATIC | §7; SD-14 |
| **C-076-10** | Registry schema execution is explicitly prohibited. | CROSS-SOURCE | §9; SD-8 |
| **C-076-11** | No runtime validator implementation is defined. | STATIC | §9 |
| **C-076-12** | Independent Record identity and resolvability are required without a resolver being implemented. | CROSS-SOURCE | §10 |
| **C-076-13** | Versionability is preserved without version mechanics being chosen. | CROSS-SOURCE | §11 |
| **C-076-14** | Every reference a schema definition actually carries obeys RMS §10.3 and Artifact 063; no reference relation or carrier is invented. | CROSS-SOURCE | §12 |
| **C-076-15** | No domain instance, domain state or runtime instance becomes a target or semantic authority. | CROSS-SOURCE | §12 RF-076-7–9 |
| **C-076-16** | Reference legality is distinguished from mechanical resolution. | STATIC | §10 RS-076-4; §12 RF-076-10 |
| **C-076-17** | Artifact 072's field meaning and domain are preserved, and schema composition respects them without a mandated reference carrier. | CROSS-SOURCE | §7, §8; RF-076-2, SD-5 |
| **C-076-18** | Final schema/field overlap closure stays with 078. | CROSS-SOURCE | §8; SC-076-D |
| **C-076-19** | No universal semantic schema and no forbidden universal field is created. | CROSS-SOURCE | §14; SD-12 |
| **C-076-20** | No canonical Registry Record is written, and no materialization value is authored. | REPOSITORY | §2, §13 |
| **C-076-21** | Artifact 077 receives the complete family-level semantic obligations. | STATIC | §21 |
| **C-076-22** | No downstream implementation or structural schema is pre-built. | REPOSITORY | §3, §21 |
| **C-076-23** | Source gaps are recorded without fabricated solutions. | STATIC | §19 |
| **C-076-24** | Row 076's `Val` and `Done` are each mapped to evidence. | STATIC | §22 |
| **C-076-25** | Only `docs/registry/schema_definition.md` is created by this artifact. | REPOSITORY | row 076 |
| **C-076-26** | `LS: LS-1` is preserved without inventing a lockstep pair; no gate is introduced. | CROSS-SOURCE | §15; SC-076-H |
| **C-076-27** | Every example is schematic: no identifier is minted and no Kind code is invented. | STATIC | §17 |

## 21. Handoff

**To 077** (`SCHEMA-DEFINITION` schema, `docs/registry/schema_definition.schema`; `H: 076`; `Val`:
*"definition resolves; versionable; references only declared entities (063)"*; `Done`: *"schema"*).
077 may take from this document, without redesign:

1. **Meaning.** A `SCHEMA-DEFINITION` Record is an R Record governing the definition of one schema
   (§6; SD-1).
2. **Definition vs implementation.** No element of a `SCHEMA-DEFINITION` executes, checks, holds a
   verdict or mutates anything (§9; SD-8).
3. **What a definition can express.** RMS §10.2's categories at the reach §7 gives each, with
   *"may define"* read as permission (SD-14).
4. **Applicability.** Every definition states the scope it applies to; any Model or Kind it names
   is declared and named by declaration reference. How many, and whether both are always present,
   is not established: if 077 must encode a cardinality, it records that choice as its own source
   condition (SD-4; RF-076-1; SC-076-N).
5. **Composition vs meaning.** Composition respects each field's governed meaning and domain; no
   element carries field meaning or domain; no field-reference carrier is mandated, and any
   concrete reference 077 carries must satisfy Artifact 063 (§8; RF-076-2).
6. **Resolution.** Ordinary R Record identity under the universal grammar and envelope; no resolver
   (§10).
7. **Versionability.** Nothing in 077 may obstruct the representation 108–110 will define; 077 is
   not asked to define it (§11; VS-076-2).
8. **Reference legality.** Only the relations RF-076-1 to RF-076-4 describe, each where carried;
   nothing else is created; no domain or runtime target (§12).
9. **Sovereignty.** No element claims ownership of a conforming Record or of a model-owned schema
   (§13; SD-9).
10. **Envelope.** The universal envelope is unchanged; envelope `kind` is `SCHEMA-DEFINITION`, never
    the applicable Kind (§14).

**077 is not asked** to define a schema engine, validation services, the versioning model, the
schema/field closure, constraint or validation-reference targets (SC-076-J), or the relation to
model-owned schemas (SC-076-I). 077's `Val` and `Done` are not enlarged.

**To 078** (`H: 076,072`). Row 076's own `→` names 077 only; 078 consumes 076 through its separately
declared `H`. 078 receives the schema side of the split (§8); 072 supplies the field side; 078
closes the overlap.

**Other downstream boundaries, preserved and not implemented:** 108–110 evolution and versioning;
111 dependency direction; 112 reference validator; 114 kernel; 115 resolution service; 116
validation suite; 123 lockstep tests; 124 P3 conformance; 145 and 152 canonical gates and the sole
writer. No row's `Val` or `Done` is enlarged.

## 22. Roadmap Completion Trace

| Row 076 | Status | Where |
|---|---|---|
| `Val`: *"definition resolves"* | **SATISFIED** — independent R Record identity under the universal grammar and envelope is required; resolution is mechanical and 114/115's; resolvable ≠ legal | §10 |
| `Val`: *"versionable"* | **SATISFIED** — participation in Registry-owned evolution under 108–110; not defined ≠ forbidden; no World History Record | §11 |
| `Val`: *"references only declared entities (063)"* | **SATISFIED** — any applicability target named is a declared Model or Kind (RF-076-1); field composition respects governed field definitions, and any concrete R → R reference carried satisfies 063 (RF-076-2); all other relations are admissible only and none is created; domain and runtime targets are forbidden | §12 |
| `Done`: *"Registry **defines** schemas; **does not execute** them"* | **SATISFIED** — definition stated (§6, §7); execution prohibited in nine testable items and a legal/illegal table | §6, §7, §9 |
| `Why`: *"closes the schema/runtime ambiguity"* | **ADDRESSED** — 064 §12 Q14's ambiguity is closed by §9 | §9 |
| `H: 064` | **SATISFIED** — consumed unchanged; §12 inherited; no Kind reopened | §5 |
| `LS: LS-1` | **PRESERVED** — label kept; no pair invented; 064 ↔ 075 untouched; relation recorded | §15; SC-076-H |
| `G: —` | **PRESERVED** — no gate introduced | §15 |
| `→ 077` | **HANDED OFF** | §21 |
| `Req: RR-17` | **CARRIED** — text unavailable (GAP-C) | SC-076-F |

---

*Artifact 076 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. A Registry definition-family specification, not a Registry Record:
it creates no `SCHEMA-DEFINITION` Record, defines no structural schema and implements nothing. Where
it differs from the Master Blueprint, the Record Model System, the OS File Build Roadmap, or
Artifact 064, those sources are correct and this document is wrong.*
