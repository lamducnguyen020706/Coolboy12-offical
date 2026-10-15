# COOLBOY12 — FIELD-DEFINITION Specification

**Artifact 072** · FIELD-DEFINITION spec · `docs/registry/field_definition.md` · Own: R · RM: R ·
T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining · Canon: canonical-about-meaning · CD: yes ·
Ph/St: P3/3b · Req: RR-16,RR-27 · BP: §9.4 · RMS: §10.1 · H: 064 · S: — · LS: LS-1 · G: — ·
→ 073 · Val: definition resolves; versionable; references only declared entities (063) ·
Done: fields definable · Why: LS-2 partner for all field architecture · Risk: HINGE · ∥: yes

## 1. Purpose

This specification answers one question — **what must one Registry `FIELD-DEFINITION` mean so that
a field has one governed meaning and an explicit domain, takes part in the field architecture of the
six Record Models, resolves and evolves as a Registry definition, and forms the Registry side of
field lockstep — without making every field universal, taking schema-owned structure, collapsing
field meaning into a value vocabulary, or owning any domain Record?**

COOLBOY12 keeps apart five things that are easy to merge. Shown for World's `status`:

```
status, a World field                a field of World's field architecture — World-owned,
                                     not universal (RMS §14, Appendix B)
status in a World Record schema      a field occurrence: structure, the schema's (Blueprint §9.4)
FIELD-DEFINITION of status           an R-partition Registry Record governing what the field
                                     means and over what domain (Artifact 064 §11)
the values a World Record carries    World's: "The values its Records carry" (Blueprint §13.6e)
status's value set for each Kind     a per-Kind value set, free to diverge (Blueprint §9.4)
```

`FIELD-DEFINITION` already exists. It is Kind 4 of RMS §10.1's *"Final Kind taxonomy — CLOSED at
fourteen"*, and Artifact 064 §11 records its admission rationale. Row 072's `Why` — *"LS-2 partner
for all field architecture"* — names the job: every model's field architecture is paired with
Registry field definitions, and this family is what each of those definitions is.

```
EACH RECORD MODEL — W · E · P · R · V · I
    ├── its field architecture establishes which fields it has and their domains (rows 179, 274,
    │   301, 355, 366); its schemas decide where each field occurs, how often, in what order
    └── it owns the values its Records carry
                ⇅  LS-2 — model field architecture ↔ Registry FIELD-DEFINITION (PART III)
REGISTRY FIELD-DEFINITION
    ├── governs what ONE field means, and over what domain (064 §11)
    ├── sits in L1, shared field semantics (Artifact 062)
    ├── is not schema, not a vocabulary, not a constraint, not a validation rule
    ├── resolves as a Registry definition and is versionable
    └── obeys Artifact 063's reference boundary
            ↓
Artifact 073 — encodes this family structurally
Artifact 078 — closes the schema/field overlap (H: 076,072)
```

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: ARCH` · `SoT: AUTHORITATIVE` about the `FIELD-DEFINITION`
family · `Auth: defining` · `Canon: canonical-about-meaning` · `CD: yes`. This document is a family
specification. It is **not** a `FIELD-DEFINITION` Record: it mints no identity, holds no Registry
data, defines no concrete field, field inventory, schema or vocabulary, and writes nothing under
`canon/` (SC-072-J). The `Canon` and `CD` values are row 072's metadata for this artifact; they do
not turn a `T: doc` specification into a Registry Record. Where it differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources are right and
this document is wrong.**

`Req: RR-16,RR-27` is reproduced from row 072. The requirement register is not in the supplied
source set, so both IDs are carried forward unverified and no requirement text is stated for
either (GAP-C; SC-072-C).

Statements below are labelled where it matters: **source fact** (stated by the Blueprint, the RMS,
the Roadmap or a frozen artifact), **required synthesis** (a conclusion several source facts force
together; not a quotation), **reading** (an interpretation, recorded as one), and **source gap**
(not established, and not filled here).

## 3. Scope

**In scope.** What a `FIELD-DEFINITION` is; what a field's meaning is; what its domain is, as far as
the sources establish it; the three field tiers; why one generic family does not make every field
universal; the seven universal fields; why `tier` and `status` are not universal; Registry
definition authority against model ownership of Records and field architecture; shared field
semantics as the base semantic layer; the boundaries with field occurrence, `SCHEMA-DEFINITION`,
`CONTROLLED-VOCABULARY`, `CONSTRAINT-DEFINITION` and `VALIDATION-RULE`; the LS-2 role and the row's
`LS` metadata; the resolution, versionability and reference obligations; the universal boundaries;
the handoffs to 073 and 078; the source conditions.

**Out of scope, by owner.**

| Not defined here | Owner |
|---|---|
| the Registry's fourteen Kinds and their admission rationale | 064 (consumed, §5) |
| the schema encoding of the obligations established here | 073 |
| `SCHEMA-DEFINITION`, and how a schema composes field definitions | 076–077 |
| the final schema/field overlap — cardinality, requiredness, order, and any edge still open | 078 |
| `CONTROLLED-VOCABULARY`, and any value set it governs | 081–082 |
| `CONSTRAINT-DEFINITION`; `VALIDATION-RULE` | 088–089; 090–091 |
| who may propose, approve or deprecate a definition | 065 |
| evolution, versioning, supersession, deprecation | 108, 109, 110 |
| concrete definition-dependency rules | 111 |
| reference validator; constraint binder; kernel; resolution service; validation suite | 112; 113; 114; 115; 116 |
| committing any `FIELD-DEFINITION` Record to `canon/registry/` | 152, after G-CANON-R (Roadmap §0.8) |
| each model's field architecture, its field domains and its concrete field definitions | 179–180 (W); 274–275 (E); 301–302 (P); 355 (V); 366 (I) |
| each model's Record schemas — which fields occur where | that model's schema rows |
| the universal envelope and the role of each of its seven fields | RMS §4, §5; Artifact 033 |
| how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added | 459 |

No field, field inventory, schema, vocabulary, constraint, validator, Record, fixture, test or
runtime behaviour is created, and no field is declared, admitted, renamed or retired.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where it says so
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done, handoffs; §0.7 and §0.8 rulings
        ↓
frozen artifacts; Artifact 003 conventions
        ↓
Artifact 072
```

| Source | What it gives this specification |
|---|---|
| RMS §4; §5; §14; Appendix B | the universal envelope, *"the bootstrap set and no more"*; `tier` and `status` not universal; provenance meaning and Kind meaning model-owned; the three field tiers; the field catalog summary |
| RMS §10; §10.1; §10.2; §10.3; §10.6; §20; Appendix H (PC-3) | Registry sovereign; `FIELD-DEFINITION` is Kind 4; what a `SCHEMA-DEFINITION` may define; the reference boundary; constraint vs validation; the schema/field overlap |
| RMS §3 (I-103); §26 | a semantic may not be shared without evidence in each model that carries it |
| Blueprint §9.4 | *"shared field definitions"*; the Registry is not schema; shared field semantics (RFS) as the base layer; *"Shared structure, independent vocabulary"*; architecture frozen, content extensible |
| Blueprint §13.6e; §13.7; §13.7a | the definition categories; *"The definition of a field"* against *"The values its Records carry"*; field custody and the lockstep of Registry definitions with their concrete expression; shared mechanism is not shared semantic |
| Blueprint P-7; §12.15 realization note; §26.3b | *"field before schema"*; JSON Schema and LinkML as realization choices |
| Roadmap row 072; PART III (LS-1, LS-2); §0.7; §0.8 | this artifact's identity; the lockstep systems; Registry self-hosting; authoring vs canonical materialization |
| Roadmap rows 073, 076–078, 081–082, 088–091, 108–116, 123, 152, 179–181, 184, 186, 217, 260, 274–275, 301–302, 355, 366, 459 | neighbours' and consumers' responsibilities |
| Artifact 064 (`H: 064`) | Kind 4; its responsibility and fourteen admission answers; *"content is 072's"* |
| Artifacts 033, 043, 057, 061, 062, 063, 065 | the envelope fields; mechanism vs semantics; the field rung of the ladder; the authority table; L1 placement; the reference boundary; governance |
| Artifacts 003, 052, 068–071 | the `LS`, `Canon` and `CD` conventions; Registry canonical about meaning; the `KIND-DEFINITION` and `SUBTYPE-DEFINITION` families, for comparison only |

Artifacts 003, 033, 043, 052, 057, 061, 062, 063, 065 and 068–071 are consumed as frozen
constraints. They are not declared dependencies of row 072 and are not added to `H` or `S`.
Artifacts 073, 076–078, 081–082 and 088–091 do not yet exist in the repository; their Roadmap rows
are cited, not their content.

Citations are to the repository copies in `docs/sources/`: the Blueprint is
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md` (revision header v0.7.0), the RMS
`COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`, the Roadmap `COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`.

## 5. Inherited Contract from Artifact 064

`H: 064` is consumed unchanged.

- **Fourteen Kinds.** `FIELD-DEFINITION` is Kind 4 of RMS §10.1. It is not renamed, not merged into
  `SCHEMA-DEFINITION`, `CONTROLLED-VOCABULARY`, `CONSTRAINT-DEFINITION` or `VALIDATION-RULE`, and no
  fifteenth Kind is introduced. Blueprint §13.6's `FIELD-DEF` is a source alias of the RMS name, not
  a further Kind (064 §5).
- **Responsibility.** 064 §6 row 4: *"what a field means (LS-2)"*.
- **Semantic object and question.** 064 §11: *"the governed definition of what a field means"*;
  *"what does this field mean, and over what domain?"*
- **Identity.** 064 §11 question 3: *"each field definition is shared meaning that must be governed
  once, not restated per Record"* — carried at §19.
- **Persistent state.** 064 §11 question 4: *"one field's meaning and domain; content is 072's"* —
  specified at §6 to §8.
- **Lifecycle.** 064 §11 question 5 and F-4: the family participates in Registry's model-owned
  definition evolution; versioning and supersession are 108–110's — carried at §20.
- **Authority.** 064 §11 question 6: *"Registry governs the definition; the model owns the values
  its Records carry"*.
- **What references it.** 064 §11 question 7: *"not established — LS-2 pairs model field
  architecture with FIELD-DEFINITION (lockstep); whether that architecture carries a concrete
  reference is downstream"*. This document establishes no inbound reference either; what a
  `FIELD-DEFINITION` itself references is settled at §21.
- **Not a field.** 064 §11 question 8: *"the definition of a field is not itself a field of the
  Records that carry it"*.
- **Not a subtype.** 064 §11 question 11: *"a subtype specializes a Kind; a field definition
  specializes no Kind — it defines field meaning shared across kinds"*. Read with RMS §14, which
  also has a Kind tier, this explains why the family is not a specialization of a Kind; it does not
  make every field's meaning shared by every Kind (SC-072-F).
- **Not a schema.** 064 §11 question 13 names `SCHEMA-DEFINITION` as the reduction target: carried
  inside schemas, *"one field's meaning would be restated per schema and could diverge — the overlap
  PC-3 records and row 078 resolves without merging the Kinds"*.
- **Why first-class.** 064 §11 question 14: *"LS-2 has no Registry partner"* without it.
- **`status` is World's.** 064 F-6: *"`status` is World-owned and not universal"*.
- **What 064 leaves open.** 064 does not define what *domain* covers beyond row 078's wording, nor a
  relation between field definitions and controlled vocabularies; both are drawn here only as far
  as the sources allow (§8, §12; SC-072-G, SC-072-H).
- **No common family checklist.** 064 §27 hands each row of 066–107 *"exactly the specification or
  schema responsibilities, `Val` and `Done` the Roadmap and governing sources assign each row"*.

## 6. What a FIELD-DEFINITION Is

**Source facts.**

- Blueprint §9.4: the Registry holds reusable semantics, *"shared field definitions"* among them.
  *"The Registry is not schema."* Schema defines the structure of a Record — *"fields, types,
  required-ness, defaults"* — and the Registry *"defines the shared meaning those fields carry
  across kinds"*. *"A field's existence is schema"*; what a field means is Registry.
- Blueprint §13.6e: the Registry owns *"The definition of a field"*; each Record Model owns *"The
  values its Records carry"*. `FIELD-DEF` sits in the category *"Structural definition"*, which
  governs *"What a Record of a kind is"*, beside `KIND-DEF` and `SUBTYPE-DEF`.
- A *Definition* is *"A Registry Record specifying meaning"*; its test is *"Governs; never
  instantiates"* (RMS §6.1). Registry Records are semantic-definition Records — *"not
  configuration, not code constants, not metadata, not a catalog, not runtime"* (RMS §10).
- Artifact 064 §11: the semantic object is *"the governed definition of what a field means"*; the
  persistent state is *"one field's meaning and domain; content is 072's"*.
- Row 078 `Done`: *"a field definition owns meaning and domain"*.

**Definition (synthesis).** A `FIELD-DEFINITION` is a Registry semantic-definition Record that
governs what one field means and the domain over which that meaning holds. It governs that meaning
and never instantiates it: it creates no field occurrence in any schema, no Record and no value,
and transfers to the Registry neither the field's structure nor any Record that carries the field.
Where the field occurs, how often, whether it is required and in what order are decided by the
schemas that compose it, within the model's field architecture (row 078; §10, §11).

**Content (synthesis — the part 064 §11 assigns here).** The family's persistent content is one
field's meaning and its domain (§7, §8) and nothing else. It is not:

- the field's occurrence in any schema, its requiredness, cardinality or order (§10, §11; FD-8,
  FD-9);
- the field's name as structure — field structure is held by schema, not by the Registry
  (Blueprint §9.4, §13.7; §10);
- a value set or vocabulary of allowed values, for any Kind (§12; FD-10, FD-11);
- a condition that must hold, or a mechanism for checking one (§13; FD-12, FD-13);
- any Record, any value a Record carries, or any current state (FD-16);
- the owning model's field architecture, its domain semantics, state, lifecycle, provenance meaning
  or canonicality (§15; FD-14).

The *Structural definition* label of §13.6e names the governed subject — what a Record of a kind is,
here through the meaning of its fields. It does not make a `FIELD-DEFINITION` the structure of any
Record: *"The Registry is not schema."* (Blueprint §9.4). This is recorded as a reading.

## 7. Field Meaning

**Meaning** is the governed semantic content of one field: what the field says about the Record that
carries it, stated once so that every Record carrying the field means the same thing by it within
its domain. Blueprint §9.4 gives the reason the meaning is held once and not per document or per
Record: *"Three different documents were therefore free to define the same term differently, and
did."*

**Meaning is not the value.** The Registry owns the definition of a field; the model owns *"The
values its Records carry"* (Blueprint §13.6e), and the Registry never infers *"ownership of any
value carried under that field"* (Artifact 061 §7 row 2).

**Meaning is not presence.** That a field exists in a Record is schema (Blueprint §9.4). A meaning
can be defined before any schema uses the field, and defining it places the field in no schema
(§10).

**Meaning is not the value set.** A field's meaning is stated once; its allowed values may differ
from Kind to Kind (§12).

**Meaning at the universal tier is bounded by the constitution.** For the seven envelope fields the
governing sources already fix each field's existence and universal role (RMS §4, §5; Artifact 033 —
for example *"slug is decoration only"*). A `FIELD-DEFINITION` of such a field may govern only the
meaning those sources establish as universal. It cannot redefine the field's presence or role, and
it cannot absorb meaning the sources leave model-owned: RMS §4 makes provenance capture universal
but *"Provenance meaning is model-owned"*, and RMS §5 makes Kind meaning model-owned (required
synthesis; SC-072-L).

**One field semantic per definition.** A `FIELD-DEFINITION` governs the meaning of one field. It is
never a bundle of unrelated fields, and a field name alone does not identify the semantic: the same
name used by two models names two fields unless the sources establish that each model shares the
meaning (I-103; Artifact 043 §4 — universality is never inferred from *"similar terminology"*).

## 8. Field Domain and the Three Tiers

**Source facts.**

- Artifact 064 §11: the semantic question is *"what does this field mean, and over what domain?"*;
  row 078 `Done`: *"a field definition owns meaning and domain"*.
- RMS §14: *"Three tiers: universal (the bootstrap set, seven fields) · model · Kind."* and *"tier
  and status are World-owned, not universal."*
- RMS Appendix B: *"Universal (7)"* — the envelope fields — and, *"World-owned, not universal:"*
  `tier` · `status` · mutation-class fields.
- The model field-architecture rows 179, 274 and 301 each carry `Done`: *"field domains"*; row 179's
  `Val` includes *"`tier` and `status` World-owned"* and its `Why` *"where `tier`/`status` are
  correctly confined"*; row 274's `Val`: *"no `tier`, no World `status`"*.
- RMS §10.2: a `SCHEMA-DEFINITION` may define, among other things, *"applicable Model · applicable
  Kind"*.

**Required synthesis — the minimum the sources establish.** A field's domain is at least the scope
over which its meaning holds, placed at one of RMS §14's three tiers:

| Tier | Domain | What the sources name | Source |
|---|---|---|---|
| **Universal** | every Record, in all six models | exactly the seven envelope fields: `partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` | RMS §4, §14, Appendix B; Artifact 033 |
| **Model** | the Records of one Record Model | World's `tier`, `status` and mutation-class fields | RMS §14, Appendix B; rows 179, 181 |
| **Kind** | the Records of one Kind of one model | no source names a field as Kind-tier; the Blueprint's per-Kind classification fields — `lineage_type` and the other `<kind>_type` fields — are the nearest source examples, and their tier is World's field architecture to state (row 179) | RMS §14; Blueprint §13.1, §13.6 |

RMS §14 names these three tiers and no other. A field whose meaning several models share without
being universal would fit none of them; no source establishes one, and this family creates none
(I-103).

**Who establishes a domain (reading).** The model field-architecture rows deliver *"field domains"*,
and row 078 assigns domain to the field definition rather than to the schema. Read together: a
field's domain is not schema's, and it is stated in LS-2 lockstep — the model's field architecture
establishes the field and its domain, and the `FIELD-DEFINITION` carries the domain over which the
meaning it governs holds (§16). This document states that a definition carries its domain; it
assigns no field to any domain.

**Source gap — what else "domain" covers.** Whether *domain* also means a value or type domain — a
data type, range, unit or format — is not established. Blueprint §9.4 lists *"types"* and
*"defaults"* among schema's structure; RMS §10.2's list for schema does not name them; RMS §10.7
gives an indicator definition *"type, unit, range, constraints, semantics"*, but an indicator is
*"not a field of the Record carrying the value"* (Blueprint §13.6e). This document claims no value
or type domain for the family, and the edge goes to row 078 (SC-072-G).

**Domain is not the schema's applicability.** RMS §10.2 lets a `SCHEMA-DEFINITION` define its
*"applicable Model · applicable Kind"*: the scope a schema applies to. A field's domain is the scope
its meaning holds over. How the two relate at the edge is row 078's (SC-072-E, SC-072-G).

## 9. Universal Fields vs Model and Kind Fields

**The universal set is closed.** *"The universal envelope is the bootstrap set and no more"* (RMS
§4): exactly seven fields. A `FIELD-DEFINITION` adds none, and no model or Kind field becomes
universal by being defined in the Registry.

**`tier` and `status` are World's.** RMS §4: *"tier and status are NOT universal envelope fields"*,
closing FG-V7-03; *"other models define their own state vocabularies"*. Blueprint §13.7: *"Neither
is a universal envelope property."* The Roadmap confirms the confinement: row 179 (World), row 274
(*"no `tier`, no World `status`"*), row 301 (*"`status` never admits CANON"*). A `FIELD-DEFINITION`
may govern what `status` means within World; no E, P, R, V or I Record is required to carry it, and
no universal status lifecycle arises. If another model's field architecture establishes a field of
the same name — row 301's `Val` speaks of `status` in Production's field architecture — that is that
model's own field, defined in its own domain, not World `status` made common (RMS §4: *"other models
define their own state vocabularies"*; §7; Artifact 043 §4).

**A generic family is not universal applicability.** One `FIELD-DEFINITION` family serves all six
models' field architectures. That is shared definition infrastructure, not a shared semantic:
*"The Record System shares mechanisms. It does not share semantics."* (Blueprint §13.7a). Artifact
043 §4: *"A semantic MUST remain model-owned unless the constitutional sources explicitly establish
it as universal."*, and universality is never inferred from common tooling, validation
infrastructure, identifiers or *"similar terminology"*. *Shared field semantics* names a Registry
semantic layer (§14); it licenses no field's meaning across models without evidence in each model
that carries it (I-103).

**The field rung.** P-7: *"A new concept becomes a field, then a kind, then a status, and only then
— rarely — a new structure."* A field is the lowest rung of the ladder; defining it creates no Kind,
and a Kind-tier field belongs to an existing declared Kind (Artifact 057 §6).

## 10. FIELD-DEFINITION vs Field Occurrence

**Source facts.** *"A field's existence is schema"* (Blueprint §9.4). Blueprint §13.7: *"this
blueprint owns the Record's properties; the Record Model Schema file owns its fields."*, and as the
two expand together *"The Record Model Schema defines how those contracts appear in concrete
records."* — *"Each new Registry definition has a corresponding Record Model Schema expression,
authored in the same act."* The Roadmap decomposes that concrete side into each model's field
architecture and Kind schemas (for example rows 179, 184, 186; row 186's `Val`: *"conforms to its
KIND-DEFINITION and to the World field definitions"*).

**Required synthesis.**

- A `FIELD-DEFINITION` does not make its field appear in any Record. Which Records carry the field
  is decided by the model's field architecture and schemas.
- A schema that carries the field conforms to the field's definition; the definition does not
  conform to, compose or execute the schema.
- Defining a field changes no existing Record and validates none at runtime.
- The field's structure — its name in a Record, its place, its occurrence — is held on the schema
  side (Blueprint §13.7), not in this family (§6).

The companion Record Model Schema document is not in the supplied source set and has not been
revised by the current Blueprint (FG-V7-01); the Roadmap's field-architecture and schema rows carry
that side here (SC-072-E).

## 11. FIELD-DEFINITION vs SCHEMA-DEFINITION

This is the highest-risk boundary.

**Source facts.**

- Blueprint §9.4: schema defines the structure of a Record — *"fields, types, required-ness,
  defaults"*; the Registry defines the meaning those fields carry.
- RMS §10.2: *"Registry may define: required fields · cardinality · constraints · version ·
  supersession · applicable Model · applicable Kind · relationships · validation references."* —
  of a `SCHEMA-DEFINITION` — and *"Registry does not execute schemas."*
- RMS Appendix H, PC-3: *"Registry SCHEMA-DEFINITION and FIELD-DEFINITION overlap at the edges (a
  schema is partly a set of field definitions)"* — *"Future extension — resolve during Registry
  schema design; no architectural contradiction"*.
- Row 078 `Done`: *"overlap resolved — a schema composes field definitions and owns
  cardinality/required/order; a field definition owns meaning and domain"*; its `Why`: *"audit DG-03
  closed here, not deferred"*; its `H`: 076, 072.
- Artifact 064 §11 question 13 and §12 question 13 keep the two Kinds apart by that same split.

**What this document establishes — the field side only.** A `FIELD-DEFINITION` holds one field's
meaning and its domain as far as §8 establishes it. It does not define how a schema composes field
definitions, and it holds no cardinality, requiredness or order, no field type and no default.

**What it leaves to row 078.** The final overlap contract, including any edge the sources leave
open: whether a field's type or default belongs with the field or the schema (Blueprint §9.4 places
both with schema; RMS §10.2 does not list them), and how a field's domain relates to a schema's
applicable Model and Kind (SC-072-E, SC-072-G).

> **Artifact 078 owns final overlap closure. Artifact 072 does not preempt it.**

## 12. FIELD-DEFINITION vs CONTROLLED-VOCABULARY

**Source facts.**

- RMS §10.1 lists `FIELD-DEFINITION` (Kind 4) and `CONTROLLED-VOCABULARY` (Kind 7) as separate
  Kinds. Blueprint §9.4 lists *"shared field definitions"* and *"controlled value sets"* as separate
  Registry content, and §13.6e places them in different categories: *"Structural definition"* and
  *"Semantic definition"* — *"What a value or term means"*.
- Blueprint §9.4: *"Shared structure, independent vocabulary"* — a field's value vocabulary *"is
  per-kind and may legitimately diverge"*; `status` *"means the same kind of thing everywhere and
  enumerates different values for a CHARACTER, an ORGANIZATION, and a CONCEPT."* *"Divergent
  per-kind value sets are the intended design, not a defect to be unified"*, and *"a forced enum
  union across kinds is prohibited"*. Row 081's `Done` repeats the rule for the vocabulary family.
- Artifact 064 §14 question 13 names `FIELD-DEFINITION` as the vocabulary's reduction target and
  rejects it: *"one field definition cannot carry several divergent value sets without the forced
  enum union §9.4 prohibits"*.

**Required synthesis.** Neither family is the other. A `FIELD-DEFINITION` governs what one field
means. A `CONTROLLED-VOCABULARY` governs a set of values or terms and their meaning, where one is
used. A field whose values differ by Kind keeps one meaning; its value sets are not part of its
definition, and nothing here pools them. The §9.4 `status` example sits inside `status`'s own
domain: `CHARACTER`, `ORGANIZATION` and `CONCEPT` are all World Kinds, so it shows one World field
with divergent per-Kind value sets, not a field shared across models (§9).

**Source gap.** No current source states the cardinality, identity or reference relation between a
field definition and a vocabulary. This document asserts none of: one vocabulary per field; one
vocabulary shared across Kinds; a required vocabulary reference in every `FIELD-DEFINITION`; any
mandatory R → R edge between the two. Where a later source establishes a relation for a particular
field, it belongs to that field's own definition, not to a rule invented here (SC-072-H).

## 13. FIELD-DEFINITION vs Constraint and Validation Rule

**Source facts.** RMS §10.6: `CONSTRAINT-DEFINITION` is *"a condition that must hold"*;
`VALIDATION-RULE` is *"a mechanism/procedure for checking a condition"*; *"These are never
collapsed."* RMS §20 names four tiers: constitutional invariant, `CONSTRAINT-DEFINITION`,
`VALIDATION-RULE`, and implementation validation, which is runtime. Rows 088 and 090 own the two
families; row 113 binds a constraint to its rule.

**Required synthesis.** Field meaning, a condition, a check and its execution are four different
things. A field's meaning can make a later constraint intelligible — a condition about `status` is
stated in terms of what `status` means — but stating that meaning states no condition and runs no
check. This family defines no range, pattern or format check, no validator function, no constraint
execution and no field validator. The Blueprint's Canon Linter, a structural checker, checks
*"status legality, tier legality"* (Blueprint §12.15); that is checking, not field meaning.

## 14. Shared Field Semantics and L1 Placement

**Source facts.** Blueprint §9.4's base layer is *Shared field semantics (RFS)*: *"Reusable field
meaning across every kind: identity, naming, classification, temporal, provenance, status, metadata,
references"*, depending on *"Nothing"* and depended on by *"Everything below"*. Artifact 062 groups
RFS as stratum 1a of L1 — *"L1 is Registry's own definition domain: shared field meaning and the
peer semantic authorities."* — and its layer matrix places *"field definitions: 072–073"* in that
row. D-2: *"RFS depends on nothing."*

**Consequences (source-confirmed).**

- Field semantics are upstream of Kind, subtype, instance and projection semantics: lower layers may
  depend on them (Artifact 062 §5, §6).
- Field semantics never take meaning from instance data or derived output (Artifact 062 D-3, D-5),
  and L1 does not depend on L2 to L5 (D-8).
- A declaration reference — naming a declared Record Model or Kind as a field's domain — is not by
  itself a semantic dependency (Artifact 062 D-9). Naming a field's domain therefore makes its
  meaning depend on no model's or Kind's semantics.
- The layers order meaning. They set no loading, evaluation or resolution order (Artifact 062 §7).

**Source gap.** Artifact 062 places the family in RFS, whose row reads *"across every kind"*, while
RMS §14 also has model and Kind tiers. How a model- or Kind-tier definition sits in L1, and whether
its meaning may draw on its Kind's semantics, is not established. This document asserts no
dependency on L2 and no exemption from D-8; concrete dependency rules are row 111's (SC-072-I).

## 15. Authority, Ownership and Canonicality

**Source fact.** *"Registry governs the definitions. Each Record Model owns its Records."*
(Blueprint §13.6e; I-105).

| Registry governs | The owning Record Model governs | Registry never infers | Source |
|---|---|---|---|
| the `FIELD-DEFINITION` Record and the field meaning it carries, within its domain | the values its Records carry | ownership of any value carried under the field | Blueprint §13.6e; Artifact 061 §7 row 2 |
| — | its field architecture: which fields it has, their domains, and which Records carry them | a field for any model, or a change to a model's field architecture without that model's side of LS-2 | rows 179, 274, 301; PART III (LS-2) |
| — | its Kind taxonomy and its Records | any Kind, Record or roster change through a field definition | I-105; I-106; RMS §6 |
| — | its state, lifecycle, provenance meaning, canonicality and semantic validation | any of those, for any model | RMS §4, §6; Blueprint §13.6e |

**Applied.** A `FIELD-DEFINITION` of World `status` governs what `status` means in World. It gives
the Registry no World Record and no value of `status`, does not decide which World Records carry the
field, and makes no other model carry it. Registry authority is domain-scoped: *"All authority is
domain-scoped."* (RMS §17). The Registry is owner of, and authority for, *"Registry Records — and
no other model's"* (Artifact 061 §8).

**Canonical about meaning.** Row 072 carries `Canon: canonical-about-meaning` as this artifact's
metadata (SC-072-J). A committed `FIELD-DEFINITION` is canonical about meaning as Registry
definitions are — *"This definition is the authoritative meaning records resolve against"*
(Blueprint §13.7c; Artifact 052 §5.4) — and never World Truth: *"Registry is canon about meaning
only; it can never override World Truth"* (RMS §24). Canonicality is not universalized (I-104).

## 16. The LS-2 Role

**Source facts.** Roadmap PART III: *"LS-2 Field ↔ Field-Definition — model field architecture ↔
Registry FIELD-DEFINITION. ATOMIC-PAIR."* Row 072's `Why`: *"LS-2 partner for all field
architecture"*; row 073's `Why`: *"LS-2"*. Rows carrying `LS-2` include the model field
architectures (179, 274, 301), the Registry field-definition sets (180, 275, 302), the combined
Visual and Issue rows (355, 366) and Kind schemas (for example 184, 186, 260). Row 180's `Val`:
*"every World field has a FIELD-DEFINITION"*; row 217's `Val`:
*"no unpaired Kind/field/relationship"*. Blueprint §13.7 is the architectural ground: *"Each new
Registry definition has a corresponding Record Model Schema expression, authored in the same act."*

**The two halves (required synthesis).**

```
MODEL SIDE      the model's field architecture: which fields the model and its Kinds have, their
                domains, and the model-owned semantics of their values
REGISTRY SIDE   a FIELD-DEFINITION per field: the field's governed meaning over its domain
```

Each concrete field has both halves, landing together. This family defines what every Registry-side
half is; the concrete halves are authored by the model rows and the Registry field-definition sets
listed above, not here.

**What LS-2 is not.** *"A lockstep partner is not a predecessor."* (Artifact 003). LS-2 is no
reference: 064 §11 question 7 leaves any concrete reference downstream. It is no semantic dependency
by itself, no runtime link, and no subordination of a model to the Registry, and it creates no
universal field roster.

## 17. LS Metadata Condition

Row 072 carries `LS: LS-1`, preserved exactly. Its `Why` reads *"LS-2 partner for all field
architecture"*, and PART III defines LS-2 as *"model field architecture ↔ Registry
FIELD-DEFINITION"* and LS-1 as *"every Kind spec ↔ its Registry KIND-DEFINITION"*. Row 073 shows the
same pattern: `LS: LS-1`, `Why: LS-2`. Artifact 003: *"Membership comes from the Roadmap's actual
declaration on the entry, not from an author's judgement that two artifacts look related."*

- **The label is preserved.** This document does not change `LS: LS-1` to `LS: LS-2`, and does not
  treat the inconsistency as resolved.
- **The role follows the sources that describe it.** The field-lockstep role this family serves is
  LS-2's, as row 072's `Why` and PART III state it (§16). That statement describes the family; it
  declares no membership.
- **Nothing is invented.** No LS-1 reading is attached to a field family, no new lockstep class is
  created, and no pair, dependency, reference or commit atomicity follows from either label.

Which label row 072 is meant to carry, and whether the generic family row is itself an LS-2 member
or the definition whose Records the concrete LS-2 sets hold, is not stated by any source. It is
recorded, not resolved (SC-072-D).

## 18. Family Rules

FD-1 to FD-22 follow the order of the obligations this family carries. FD-18 to FD-20 summarize the
resolution, versionability and reference contracts of §19 to §21.

| ID | Rule | Basis |
|---|---|---|
| **FD-1** | **One field semantic.** A `FIELD-DEFINITION` governs the meaning of exactly one field over one domain. It is never a bundle of unrelated fields, and a field name alone does not identify the semantic. How the subject is encoded is 073's. | 064 §11 questions 1–4; I-103; Artifact 043 §4; synthesis |
| **FD-2** | **Meaning.** The definition governs what the field means — the governed semantic content every Record carrying the field shares within its domain. | Blueprint §9.4, §13.6e; 064 §11 |
| **FD-3** | **Domain.** The definition carries the domain over which that meaning holds — at least its scope at one field tier. Whether domain also covers a value or type domain is not established; representation is 073's. | row 078 `Done`; 064 §11 question 2; RMS §14; SC-072-G |
| **FD-4** | **Field tier.** Every domain is compatible with RMS §14's three tiers — universal, model, Kind — and with no other. | RMS §14 |
| **FD-5** | **No universalization.** A generic family across six models does not make any field universal or any field's meaning shared across models without evidence in each model that carries it. | I-103; Blueprint §13.7a; Artifact 043 §4 |
| **FD-6** | **Universal envelope closed.** Only the seven bootstrap fields are universal. A definition at that tier governs only the meaning the constitution establishes as universal and redefines no field's presence or role. | RMS §4, §5, §14; Artifact 033 |
| **FD-7** | **World-only semantics stay World-only.** `tier` and `status` are World-owned and not universal; no other model is required to carry them. | RMS §4, §14, Appendix B; Blueprint §13.7; rows 179, 274 |
| **FD-8** | **Definition ≠ occurrence.** A definition does not cause its field to appear in any Record schema or Record. | Blueprint §9.4, §13.7 |
| **FD-9** | **Definition ≠ schema.** The family owns no schema composition, cardinality, requiredness, order, type or default; row 078 owns the final boundary. | Blueprint §9.4; RMS §10.2, PC-3; row 078 |
| **FD-10** | **Definition ≠ vocabulary.** Field meaning is distinct from any allowed-value vocabulary. No cardinality, identity or reference rule between them is invented. | RMS §10.1; Blueprint §9.4, §13.6e; 064 §14; SC-072-H |
| **FD-11** | **Per-Kind vocabulary divergence.** One field's value sets may differ by Kind; no forced enum union across Kinds is created. | Blueprint §9.4; row 081 `Done` |
| **FD-12** | **Definition ≠ constraint.** A field's meaning is not a condition that must hold. | RMS §10.6, §20; row 088 |
| **FD-13** | **Definition ≠ validator.** A field's meaning is not a checking mechanism or runtime validation, and the family defines no check. | RMS §10.6, §20; row 090 |
| **FD-14** | **Registry/model custody split.** The Registry governs the definition Record; each Record Model owns its Records, their values, and its field architecture. | Blueprint §13.6e; I-105; Artifact 061 §7 row 2 |
| **FD-15** | **L1 semantics.** Field semantics sit in L1 (RFS) and follow Artifact 062's downward-only law; naming a domain is not a semantic dependency. | Blueprint §9.4; Artifact 062 §4.3, §6, D-2, D-8, D-9 |
| **FD-16** | **No instance authority.** No domain Record, value or state defines what a field means. | RMS §10.3; Artifact 063 §9; Artifact 062 D-3 |
| **FD-17** | **No runtime authority.** No running service, process, linter or validator defines what a field means. | RMS §10.3; Artifact 063 §13 |
| **FD-18** | **Resolution.** A materialized definition is identity-bearing and must be resolvable; the mechanics are downstream (§19). | row 072 `Val`; RMS §4; rows 114, 115 |
| **FD-19** | **Versionability.** A definition is versionable; the mechanics are 108–110's (§20). | row 072 `Val`; 064 F-4; rows 108–110 |
| **FD-20** | **Reference legality.** Every concrete reference the family carries obeys Artifact 063 (§21). | row 072 `Val`; RMS §10.3; Artifact 063 |
| **FD-21** | **LS-2 role.** The family is the Registry field-definition side of model field architecture, per row 072's `Why` and PART III; the row's `LS: LS-1` stays recorded as declared. | PART III; row 072; Artifact 003; SC-072-D |
| **FD-22** | **No direct canon write.** This specification creates no Registry Record and no canonical data; a `FIELD-DEFINITION` Record reaches `canon/registry/` only through row 152, after G-CANON-R. | Roadmap §0.8; Artifact 003 (`CD`); Spine law 2; SC-072-J |

## 19. Resolution Contract

Row 072 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-072-1** | A `FIELD-DEFINITION` is a Registry definition Record, shared meaning governed once (064 §11 question 3). Once materialized it carries ordinary Record identity under the universal grammar and envelope (RMS §4, §5) — the baseline identity later Registry-definition resolution requires. That identity is an R Record's: it is not the field's name, not the field's domain, and not a field occurrence. The slug is decoration only and never the basis of resolution (RMS §5). |
| **RS-072-2** | A consumer must be able to resolve a materialized `FIELD-DEFINITION`. Reference resolution is universal and mechanical (RMS §4); *"Reference resolution is not Registry work."* (Blueprint §9.4). Registry definition resolution by id and version is row 115's (*"consumer resolves by id+version"*); create, resolve and version operations are row 114's (*"create/resolve/version a definition"*). This document does not supply the complete id+version representation; version representation is 108–110's. |
| **RS-072-3** | Successful resolution does not establish reference legality: *"Resolvable ≠ legal."* (Artifact 063 §11). |
| **RS-072-4** | Resolution transfers nothing. Resolving a `FIELD-DEFINITION` places the field in no schema, admits nothing, and gives the Registry no Record and no value. |
| **RS-072-5** | No resolver, lookup, index, cache, storage path, fallback, version-selection logic or field-name lookup is defined here; how a consumer finds the definition of a given field is not defined here (114; 115; 073). |

## 20. Versionability Boundary

Row 072 `Val`: *"versionable"*.

**Source facts.** A Registry definition has *"a governed change path, and a temporal account"*
(Blueprint §13.6e; 064 F-4). Row 108 owns the evolution model (`Val`: *"version"*; `Done`:
*"temporal account without a World History Record"*); row 109 owns versioning (*"consumers pin a
version"*); row 110 owns supersession and deprecation (*"deprecated ≠ deleted"*).

| ID | Obligation |
|---|---|
| **VS-072-1** | A `FIELD-DEFINITION` participates in governed Registry definition evolution and must be capable of carrying versioned meaning under the model rows 108–110 define. Every version stays bound by FD-1 to FD-22. The Registry's temporal account is its own: no World History Record is used or required (row 108; I-102). |
| **VS-072-2** | **Not defined here ≠ forbidden.** That this document defines no version mechanism is not a decision that a `FIELD-DEFINITION` carries no version, supersession or deprecation information. Rows 108–110 keep their authority to establish the Registry-owned representation, and nothing here asks 073 to close it. Whatever they establish stays Registry-owned: it adds no field to the universal envelope and is not a version, lifecycle or state model shared by W, E, P, V or I (RMS §4, §16, §19). |

**Not decided here** (108–110): a version field or identifier; numbering; revision identifiers;
*latest* semantics; pin representation; supersession, replacement or deprecation representation;
effective dates; migration; compatibility; retention; deletion. Who may propose, approve or
deprecate a definition is 065's. How a field change is made on the model side is that model's field
architecture's, and how a new field is added is row 459's.

## 21. Reference Boundary

Row 072 `Val`: *"references only declared entities (063)"*. Artifact 063 binds this family as a
constraint; it is not added to `H`. Artifact 063 §22 leaves to each family *"which concrete
reference relations each family carries"*; for this family the answer is below.

| ID | Rule | Basis |
|---|---|---|
| **RF-072-1** | **Domain scope names only declared entities.** A model-tier domain names a declared Record Model; a Kind-tier domain names a declared Kind of one declared model, with declared status established by that model's Kind architecture; a universal-tier domain names neither. This is the one concrete reference obligation the family establishes. It fixes no closed count of carriers, defines no proof formula, and an undetermined target is not legal; its structural encoding is 073's. | Artifact 063 §7 rows 2–3, §8, RB-1, RB-6; FD-3, FD-4 |
| **RF-072-2** | **No declared-field category.** RMS §10.3 names no field category, and Artifact 063: *"The matrix has no row for declared subtypes, fields, relationship types, vocabularies, validators or capabilities as categories of their own: those are reached as Registry definitions (row 1)."* A field is reached through its `FIELD-DEFINITION`; another Registry definition that names it makes an R → R reference, where that family's own contract carries one. | RMS §10.3; Artifact 063 §7, §8.1 |
| **RF-072-3** | **Declared Model ≠ `MODEL-DEFINITION`; declared Kind ≠ `KIND-DEFINITION`.** Naming a model or Kind as a domain is a declaration reference; a relation to its definition Record would be an R → R reference. Which form a domain takes is 073's; no URI, handle, string syntax or discriminator is invented here. | Artifact 063 §8.2, §8.3, SC-063-G |
| **RF-072-4** | **No invented concrete references.** Schemas, vocabularies, constraints, validation rules, other definitions and declared semantic contracts are admissible categories; that obliges no `FIELD-DEFINITION` to reference any of them. No reference list, schema reference, vocabulary reference, model reference, Kind reference or dependency list is defined. A structural reference may encode only an obligation established here — the domain scope — or representation a named downstream owner establishes (§20), adds no semantic relation or authority of its own, and must satisfy Artifact 063. Admissible category ≠ concrete family relation. | Artifact 063 RB-5, §22 |
| **RF-072-5** | **No domain instance.** No Record of W, E, P, V or I — a Record that carries the field, or one that shows a typical value — and no domain state, such as a current value, is a reference target, a dependency or the semantic authority of a `FIELD-DEFINITION`. | RMS §10.3; Artifact 063 §9, SC-063-A |
| **RF-072-6** | **No runtime instance.** No running service, worker, session, process, plugin instance, linter run, schema engine, validator process or live object is a target, a dependency or the semantic authority of a `FIELD-DEFINITION`. | RMS §10.3; Blueprint §9.4; Artifact 063 §13 |
| **RF-072-7** | **Resolvable ≠ legal.** A target that resolves mechanically may still be illegal, and a target that cannot be established is not legal either. | Artifact 063 §11 |
| **RF-072-8** | **No transfer through reference.** A legal reference transfers no ownership, mutation authority, semantic authority, admission, canonicality or source-of-truth class. | Artifact 063 §12 |
| **RF-072-9** | **Reference ≠ dependency.** Naming a declared model or Kind as a domain is not by itself a semantic dependency, and the named model or Kind is not semantic authority for the field's meaning. Concrete definition-dependency rules are row 111's. | Artifact 062 D-9; Artifact 063 RB-5; row 111; SC-072-I |

Blueprint §9.4's older wording — *"A Registry definition may never reference a kind, a subtype, or
an instance"* — is not current law for reference legality. RMS §10.3 corrects it (*"v0.1 stated the
boundary too bluntly"*), and Artifact 063 applies the correction (SC-072-B).

## 22. Envelope and Universal-Semantics Boundary

Once materialized, a `FIELD-DEFINITION` carries the universal envelope unchanged — `partition` ·
`kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4) — in partition
R. The envelope's `kind` names the Record's own Kind, `FIELD-DEFINITION`; it is not the field's
domain. No family concept — the field tier, the domain, a type, requiredness, a default,
cardinality, a vocabulary, `status`, a lifecycle, a version, a validator or an owner — becomes a
universal field. How the obligations of this document are structurally encoded is 073's.

None of RMS §4's nine prohibited universal semantics is introduced. For this family that means: no
universal field roster and no Universal Record Base made of fields; no universal semantic schema
assembled from field definitions; no universal state model or lifecycle through `status`, `tier` or
the World mutation classes; no universal canonicality; no universal Kind taxonomy or identity
composition from a field's domain; and no Relationship Record or History Record arising from a field
or its versions.

## 23. Field Definability

Row 072 `Done`: *"fields definable"*.

**Required synthesis.**

1. Every field sits at one of RMS §14's three tiers, and every model- or Kind-tier field belongs to
   a declared model or Kind — an admissible Registry reference category (RMS §10.3; §21).
2. The family requires nothing model-specific (FD-1 to FD-22): no Relationship Record or History
   Record (I-102), no `status` or `tier` (RMS §4), and none of a model's own lifecycle, temporal
   architecture, canonicality or package (RMS §6).
3. The Registry *"must not require the complete semantic implementation of every other Record Model
   in order to define them"* (Blueprint §13.6e; Artifact 062 D-7).

Therefore a field that a model's field architecture establishes, at any of the three tiers, is
definable by this family with no per-model variant, as long as its meaning and domain can be stated
without breaking model sovereignty, the tier boundaries, Registry reference legality or schema
ownership. The family does not itself establish that any field exists.

Row 072's *"fields definable"* does not mean that every field has been enumerated, that any model's
field architecture exists, that any `FIELD-DEFINITION` Record has been created, that schemas,
cardinalities, validators or vocabularies exist, that resolution runs, or that a field-addition
ceremony exists. *"Not every future Registry entry needs authoring now"* (Blueprint §9.4).

## 24. Worked Examples

All examples are **schematic**: no identifier is minted, no field is defined, and nothing here is
Registry data.

**A. Universal field — `registry_ref`.** Its presence in every Record is constitutional (RMS §4),
and its universal role is stated: it *"Carries the Record's reference into the Registry"*, and
*"Reference resolution is not Registry work."* (Artifact 033; Blueprint §9.4). A `FIELD-DEFINITION`
of `registry_ref` could govern only that established meaning: it does not redefine the field's
presence, attach a referent, or define resolver behaviour, which stays with the resolution mechanism
(RMS §4). Which row would author such a definition is not stated (SC-072-L).

**B. Model-owned field — `status`.** The Blueprint uses `status` as its example of reusable field
meaning; RMS §14 makes it World-owned and not universal. A `FIELD-DEFINITION` can govern what
`status` means within World. E, P, R, V and I Records are not required to carry it; its value sets
may differ between World Kinds; no universal lifecycle arises.

**C. Model-owned field — `tier`.** World-owned (RMS §4, §14); not an eighth envelope field; *"its
applicability elsewhere"* is closed by RMS §4, and no applicability outside World is invented here.

**D. Legal — one field, divergent values across Kinds.** Inside World, `status` *"means the same
kind of thing everywhere and enumerates different values for a CHARACTER, an ORGANIZATION, and a
CONCEPT."* One meaning; per-Kind value sets that may differ; no forced enum union (Blueprint §9.4).

**E. Illegal — a definition creating occurrence.** *Because the Registry defines `status`, every
Record schema must contain `status`* — rejected: *"A field's existence is schema"* (Blueprint §9.4),
and which Records carry a field is the model's field architecture's (FD-8).

**F. Illegal — universalizing a World field.** *`status` belongs in the seven-field universal
envelope* — rejected: the envelope is *"the bootstrap set and no more"*, and `status` is
World-owned (RMS §4, §14; FD-6, FD-7).

**G. Illegal — schema ownership theft.** A `FIELD-DEFINITION` family that defines requiredness,
order or per-schema cardinality for its fields is rejected: those belong to schema composition
(row 078; FD-9).

**H. Illegal — a global enum.** Merging every Kind's `status` values into one union for convenience
is rejected (Blueprint §9.4; FD-11).

**I. Boundary — field vs vocabulary.** What `status` means is this family's subject; which values
each Kind allows, where a vocabulary governs them, is `CONTROLLED-VOCABULARY`'s. Whether that field
references a vocabulary, and how many, is not established and is not decided here (SC-072-H).

**J. Boundary — field vs constraint.** What `status` means is the kind of statement a field
definition makes; this document states no such meaning. That a Record's `status` is legal is a
condition about the field — the Blueprint's Canon Linter checks *"status legality"* (Blueprint
§12.15). Stating such a condition is a `CONSTRAINT-DEFINITION`'s, and checking it is a
`VALIDATION-RULE`'s and implementation validation's (RMS §10.6, §20). The field definition states
neither.

**K. Deferred — a new field.** Once a model's field architecture establishes a new field, this
family can define its meaning and domain. How the field is added is row 459's (*"each through its
own ceremony, never through a generic abstraction"*), with governance under Artifact 065; no
ceremony is invented here, and no new field name is proposed.

## 25. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | A `FIELD-DEFINITION` makes a field appear in every Record | occurrence is schema's | Blueprint §9.4; FD-8 |
| 2 | Registry owning field meaning means Registry owns domain Records | definition authority ≠ Record ownership | Blueprint §13.6e; Artifact 061 §7 row 2; FD-14 |
| 3 | A generic family means universal field applicability | shared mechanism ≠ shared semantic | Blueprint §13.7a; Artifact 043 §4; FD-5 |
| 4 | `status` is universal | World-owned, not universal | RMS §4, §14; FD-7 |
| 5 | `tier` is universal | World-owned, not universal | RMS §4, §14; FD-7 |
| 6 | Every field belongs to every model | three tiers; only seven fields are universal | RMS §14; FD-4, FD-6 |
| 7 | A model-scoped field must become a universal field | the envelope is closed | RMS §4; FD-6 |
| 8 | A Kind-scoped field creates a new Kind | a field is a lower rung | P-7; Artifact 057 §6; FD-4 |
| 9 | Field meaning is its allowed-value vocabulary | distinct Kinds and categories | RMS §10.1; Blueprint §13.6e; FD-10 |
| 10 | All per-Kind vocabularies of a field must be unioned | forced enum union prohibited | Blueprint §9.4; FD-11 |
| 11 | `FIELD-DEFINITION` is `SCHEMA-DEFINITION` | separate Kinds; row 078 separates them | RMS §10.1; row 078; FD-9 |
| 12 | `FIELD-DEFINITION` owns schema composition | a schema composes field definitions | row 078 `Done`; FD-9 |
| 13 | `FIELD-DEFINITION` universally owns cardinality, requiredness or order | they are schema's | row 078 `Done`; Blueprint §9.4; FD-9 |
| 14 | `FIELD-DEFINITION` is `CONSTRAINT-DEFINITION` | meaning ≠ condition | RMS §10.6; FD-12 |
| 15 | `FIELD-DEFINITION` is `VALIDATION-RULE` | meaning ≠ check | RMS §10.6, §20; FD-13 |
| 16 | A runtime validator defines field semantics | runtime is never semantic authority | RMS §10.3, §20; FD-17 |
| 17 | A domain Record instance defines field meaning | instances are never semantic authority | RMS §10.3; FD-16 |
| 18 | An admissible target category creates a mandatory reference | category ≠ concrete relation | Artifact 063 RB-5; RF-072-4 |
| 19 | A reference transfers ownership or authority | it transfers nothing | Artifact 063 §12; RF-072-8 |
| 20 | Resolvable means legal | resolvable ≠ legal | Artifact 063 §11; RS-072-3 |
| 21 | *Versionable* lets 072 invent version fields | the mechanics are 108–110's | §20 |
| 22 | `Canon: canonical-about-meaning` authorizes a direct `canon/**` write | it is per-artifact metadata | Artifact 003 (`Canon`); FD-22; SC-072-J |
| 23 | `CD: yes` authorizes canonical materialization | the flag *"licenses nothing"* | Artifact 003 (`CD`); Roadmap §0.8; FD-22 |
| 24 | `LS: LS-1` proves row 072 is a Kind ↔ `KIND-DEFINITION` pair | LS-1 is Kind spec ↔ `KIND-DEFINITION`; this is a field family | Roadmap PART III; §17 |
| 25 | `Why: LS-2` authorizes rewriting the row's metadata | the label is preserved and recorded | Artifact 003 (`LS`); §17; SC-072-D |
| 26 | 072 may pre-build 073 | the encoding is 073's | row 073; §28 |
| 27 | 072 may pre-close row 078 | the overlap is 078's | row 078; §11 |
| 28 | 072 may author World, E, P, V or I field inventories | they are the model rows' | rows 179–180, 274–275, 301–302, 355, 366 |
| 29 | Shared field semantics may be imposed without evidence in each model | a semantic is shared only with that evidence | I-103; Artifact 043 §4 |
| 30 | A shared mechanism implies shared meaning | mechanism ≠ semantic | Blueprint §13.7a; I-103 |
| 31 | Two models' fields with the same name are one field | similar terminology is no evidence of shared meaning | Artifact 043 §4; §7, §9 |
| 32 | Naming a model or Kind as a field's domain makes its meaning depend on that model or Kind | a declaration reference is not by itself a dependency | Artifact 062 D-9; RF-072-9 |
| 33 | A `FIELD-DEFINITION` may redefine an envelope field's universal role — make the slug identity, say | the role is constitutional | RMS §4, §5; Artifact 033; FD-6 |
| 34 | The Blueprint's JSON Schema and LinkML realization makes this family a JSON Schema or LinkML artifact | realization is not authority; 072 is `T: doc` | Blueprint §12.15, §26.3b; SC-072-K |
| 35 | An indicator definition's type, unit and range show that every field definition carries a type and range | an indicator is not a field | RMS §10.7; Blueprint §13.6e; SC-072-G |

## 26. Source Conditions and Gaps

Each entry gives the two source statements (or the missing source), the condition, whether this
artifact owns its resolution, and the treatment.

### SC-072-A — stale Registry classification — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* |
| **Source B** | RMS §10, COLLISION-1: *"Registry is a sovereign Record Model"*; the §9.4 line is *"stale and requires a Blueprint wording fix"*; RMS Appendix H carries that fix as PC-1. |
| **Condition** | The Blueprint line classifies the Registry as a capability; the RMS makes it a sovereign Record Model. |
| **Owner** | Not this artifact — closed at source by the RMS; any Blueprint wording fix is the author's act. |
| **Treatment** | The Registry is a sovereign Record Model and a `FIELD-DEFINITION` is a Record of it. No Blueprint text is edited. |

### SC-072-B — older reference prohibition vs RMS §10.3 — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §9.4 and §13.6e: *"a Registry definition may never reference a kind, a subtype, or an instance"*. |
| **Source B** | RMS §10.3: *"v0.1 stated the boundary too bluntly"*. Artifact 063 SC-063-A applies the correction for reference legality. |
| **Condition** | The older text forbids naming a kind; RMS §10.3 admits declared Record Models and Kinds and keeps domain instances forbidden. |
| **Owner** | Not this artifact — closed at source by RMS §10.3 and applied by Artifact 063. |
| **Treatment** | §21 applies RMS §10.3 and Artifact 063; domain instances stay forbidden; the two texts are not averaged; no Blueprint text is edited. |

### SC-072-C — RR-16 and RR-27 text unavailable — SOURCE GAP

| | |
|---|---|
| **Source A** | Row 072: `Req: RR-16,RR-27`. |
| **Source B** | Missing — the requirement register is not in the source set (GAP-C). |
| **Gap** | Neither requirement's text can be read. |
| **Owner** | Not this artifact. |
| **Treatment** | Both IDs are carried exactly; no requirement text is stated and no compliance with unread requirement text is claimed. This artifact is validated against row 072's `Val` and `Done`, its cited sources and the frozen contracts. Non-blocking (GAP-C). |

### SC-072-D — `LS: LS-1` against the LS-2 role — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Source A** | Row 072 carries `LS: LS-1`; row 073 carries `LS: LS-1`. Artifact 003: membership *"comes from the Roadmap's actual declaration on the entry"*. |
| **Source B** | Row 072's `Why`: *"LS-2 partner for all field architecture"*; row 073's `Why`: *"LS-2"*. PART III defines LS-2 as *"model field architecture ↔ Registry FIELD-DEFINITION"* and LS-1 as *"every Kind spec ↔ its Registry KIND-DEFINITION"*. The concrete field rows (179–180, 274–275, 301–302, 355, 366) carry LS-2. Row 123, the Registry lockstep tests (`H: 066–107`), declares `LS: LS-1,4,5,6,7,8` — not LS-2. |
| **Condition** | The declared label and the role the same row describes name different lockstep systems, and no source says which the row means, or whether the generic family row is itself an LS-2 member or the definition whose Records the concrete LS-2 sets hold. |
| **Owner** | Not this artifact; the Roadmap author's. How row 123 treats row 072's label is row 123's. |
| **Treatment** | `LS: LS-1` is reproduced exactly; the family's field-lockstep role is described as LS-2's because the sources describe it so (§16, §17); no LS-1 meaning, new class, pair, dependency, reference or atomicity is invented; the Roadmap is not edited. Route: ROADMAP ISSUE, non-blocking for row 072's `Val` and `Done`. |

### SC-072-E — the SCHEMA-DEFINITION / FIELD-DEFINITION overlap — DEFERRED TO 078

| | |
|---|---|
| **Source A** | Blueprint §9.4: schema is *"fields, types, required-ness, defaults"*; Blueprint §13.7 gives field custody to the Record Model Schema, a companion document not in the source set and not revised by the current Blueprint (FG-V7-01). RMS §10.2 lists what a `SCHEMA-DEFINITION` may define, naming neither type nor default. |
| **Source B** | RMS PC-3: the two *"overlap at the edges"* — *"resolve during Registry schema design"*. Row 078 (`H: 076,072`) is assigned the closure: a schema composes field definitions and *"owns cardinality/required/order"*; a field definition *"owns meaning and domain"*. |
| **Condition** | Composition, cardinality, requiredness and order are placed; type, default, and the relation between a field's domain and a schema's applicable Model and Kind are not settled by every source alike. |
| **Owner** | Row 078, after 076. |
| **Treatment** | This document defines the field side only — meaning, and domain as far as §8 establishes it — and claims no type or default. It is an input to row 078, not its replacement (§11). |

### SC-072-F — broad Blueprint field wording vs RMS field tiers — PARTLY CLOSED; READING RECORDED

| | |
|---|---|
| **Source A** | Blueprint §9.4's RFS row: *"Reusable field meaning across every kind: identity, naming, classification, temporal, provenance, status, metadata, references"*; what `status` means *"everywhere it appears"* is Registry. Blueprint §13.7: `tier`'s *"applicability elsewhere is OPEN (FG-V7-03)"*. Artifact 064 §11 question 11: the family *"defines field meaning shared across kinds"*. |
| **Source B** | RMS §4: *"tier and status are NOT universal envelope fields"* (*"closes FG-V7-03"*); both World-owned; *"Provenance meaning is model-owned"*. RMS §14: three tiers, `tier` and `status` World-owned. I-103. |
| **Condition** | Read literally, the older wording would make `status` and provenance meaning reusable across every kind of every model; the RMS confines `tier` and `status` to World and keeps provenance meaning model-owned. |
| **Owner** | Not this artifact for `tier` and `status` — the RMS closes them. |
| **Treatment** | The RMS governs: no universal `status` or `tier`. *Shared field semantics* is read as the Registry's base semantic layer, not as universal applicability: a field's meaning is shared across the Kinds and models its domain covers, and across models only where the sources establish it in each (§9, §14). The §9.4 `status` example is read inside World, where its three Kinds sit. This reading is recorded as one. |

### SC-072-G — what "domain" covers — SOURCE GAP

| | |
|---|---|
| **Source A** | Row 078: a field definition *"owns meaning and domain"*; Artifact 064 §11: *"over what domain?"*; RMS §14's three tiers; rows 179, 274, 301 deliver *"field domains"*. |
| **Source B** | No source defines *domain* further. Blueprint §9.4 places types and defaults with schema; RMS §10.2 gives schemas an *"applicable Model · applicable Kind"*; RMS §10.7's *"type, unit, range"* belongs to indicators, which are not fields. |
| **Gap** | Whether a field's domain is only its applicability scope, or also a value or type domain; and how domain ownership between row 078's field definition and the model rows' *"field domains"* is divided. |
| **Owner** | Not this artifact: row 078 for the schema edge; each model's field architecture for its fields' domains. |
| **Treatment** | Only the minimum is stated: a domain is at least a scope at one RMS §14 tier, established in LS-2 lockstep with the model side (§8). No value or type domain and no field-domain ontology is invented. Non-blocking: meaning and scope are definable without it. |

### SC-072-H — FIELD-DEFINITION and CONTROLLED-VOCABULARY — SOURCE GAP

| | |
|---|---|
| **Source A** | Distinct RMS §10.1 Kinds; distinct §9.4 content and §13.6e categories; per-Kind value sets may diverge; 064 §14 rejects carrying divergent value sets in one field definition. |
| **Source B** | No source fixes how a field definition and a vocabulary relate. |
| **Gap** | Cardinality, identity and reference between field definitions and vocabularies. |
| **Owner** | Not this artifact: rows 081–082 own the vocabulary family; each field's concrete definition owns any relation a later source establishes. |
| **Treatment** | The families stay distinct (§12; FD-10). No one-vocabulary-per-field rule, shared cross-Kind vocabulary, mandatory vocabulary reference or R → R edge is invented. Non-blocking. |

### SC-072-I — L1 placement against model and Kind domains — SOURCE GAP

| | |
|---|---|
| **Source A** | Artifact 062 places field definitions (072–073) in L1 RFS — *"reusable field meaning across every kind"* — with D-2 *"RFS depends on nothing."* and D-8: L1 does not depend on L2. |
| **Source B** | RMS §14 has model and Kind tiers, whose fields hold meaning over one model or one Kind. |
| **Gap** | How a model- or Kind-tier definition sits in a layer described as reusable across every kind, and whether its meaning may draw on its Kind's semantics. |
| **Owner** | Not this artifact: concrete definition-dependency rules are row 111's; Artifact 062 is frozen. |
| **Treatment** | Domain and dependency are kept apart: naming a domain is a declaration reference, not a dependency (D-9; RF-072-9). No dependency on L2 and no exemption from D-8 is asserted. Non-blocking. |

### SC-072-J — Roadmap `Canon` metadata vs Artifact 003's docs-specification convention

| | |
|---|---|
| **Source fact — Roadmap row 072** | Row 072 assigns `T: doc` · `Canon: canonical-about-meaning` · `CD: yes`. These values are preserved exactly. |
| **Source fact — Artifact 003** | `Canon` *"records a per-artifact status, nothing more"*, and *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`."* `CD` marks whether an artifact *"creates, carries or directly impacts canonical data"* and *"licenses nothing"*. |
| **Source fact — directory** | `docs/registry/PURPOSE.md` excludes Registry Records: *"those are minted into `canon/registry/`, only through the Mutation Coordinator after G-CANON-R"*. |
| **Inconsistency** | Row 072's explicit `Canon` value differs from Artifact 003's general docs-specification value, and no source explains why. |
| **Owner** | Not this artifact; a Roadmap or convention fix is the author's. |
| **Treatment** | Row 072's metadata is preserved; Artifact 003 is not changed; the inconsistency is **recorded, not resolved**. This document remains a specification, creates no canonical data and performs no canonical write; `CD: yes` licenses nothing (FD-22). Route: ROADMAP / CONVENTION ISSUE, non-blocking. |

### SC-072-K — realization technology in the Blueprint — BOUNDED

| | |
|---|---|
| **Source A** | Blueprint §12.15 realization note: JSON Schema (ADOPT) for structural validation, with LinkML (ADAPT) *"used to author Registry vocabularies and field definitions in legible YAML and generate the validators from them"*; Blueprint §26.3b's normalized component metadata lists LinkML with *"none — Registry owns meaning"*. |
| **Source B** | Row 072 is `T: doc`; the structural contract is row 073's; validators are rows 112–116's. |
| **Condition** | A realization choice could be read as making this family a LinkML or JSON Schema artifact. |
| **Owner** | Not this artifact: realization belongs to the implementation rows. |
| **Treatment** | No serialization, schema language or generated validator is adopted here; a realization choice is not authority over meaning or over downstream work. Non-blocking. |

### SC-072-L — the universal tier's field definitions — SOURCE GAP

| | |
|---|---|
| **Source A** | RMS §14 has a universal tier of seven fields; RMS §14 points to *"Appendix B and Deliverable E"* for the full catalog; Artifact 033 states each envelope field's universal role. |
| **Source B** | No Roadmap row names `FIELD-DEFINITION` Records for the seven universal fields — the field-definition rows are per model (180, 275, 302, 355, 366) — and Deliverable E is not in the source set. |
| **Gap** | Whether the seven universal fields receive `FIELD-DEFINITION` Records, which row would author them, and what the full field catalog says. |
| **Owner** | Not this artifact; the Roadmap author's. |
| **Treatment** | The family can define a universal-tier field within the limits of §7 and FD-6; no such Record is scheduled or authored here. Non-blocking. |

### SC-072-M — downstream rows citing 072 without 073 — RECORDED, NON-BLOCKING

| | |
|---|---|
| **Source A** | Rows 180, 275 and 302, the World, Epistemic and Production field-definition sets, list 073 in their `H`. |
| **Source B** | Rows 355 and 366, which also author field definitions (`canon/registry/visual_fields/`, `canon/registry/issue_fields/`), list 072 but not 073. |
| **Condition** | Two field-definition rows do not list the structural contract their Records would conform to. |
| **Owner** | Not this artifact; the Roadmap author's. |
| **Treatment** | `→ 073` is preserved; this document assigns rows 355 and 366 nothing beyond their own rows. Route: ROADMAP ISSUE. |

## 27. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-072-01** | **Family identity.** `FIELD-DEFINITION` is stated to be Kind 4 of the frozen fourteen-Kind Registry taxonomy; no fifteenth Kind is introduced. | RMS §10.1; §5 |
| **C-072-02** | **Meaning ownership.** Field meaning is assigned to `FIELD-DEFINITION`. | §6, §7; FD-2 |
| **C-072-03** | **Domain ownership.** A field's domain is assigned to `FIELD-DEFINITION` only as far as the sources establish it — a scope at one tier — and no value or type domain is claimed. | §8; FD-3; SC-072-G |
| **C-072-04** | **Three-tier compatibility.** The universal, model and Kind tiers are preserved, and no other tier is created. | §8; FD-4 |
| **C-072-05** | **Universal envelope.** The universal field set remains exactly seven. | §9, §22; FD-6 |
| **C-072-06** | **`tier` and `status`.** Neither is universalized, and no other model is required to carry either. | §9; FD-7 |
| **C-072-07** | **No occurrence authority.** A field definition makes no field structurally present in any Record or schema. | §10; FD-8 |
| **C-072-08** | **No cardinality, requiredness or order theft.** Nothing that row 078 reserves to schema composition is taken. | §11; FD-9 |
| **C-072-09** | **No vocabulary collapse.** `FIELD-DEFINITION` is kept distinct from `CONTROLLED-VOCABULARY`, and no relation between them is invented. | §12; FD-10; SC-072-H |
| **C-072-10** | **No forced enum union.** Per-Kind value sets may diverge. | §12; FD-11 |
| **C-072-11** | **No constraint collapse.** `FIELD-DEFINITION` is kept distinct from `CONSTRAINT-DEFINITION`. | §13; FD-12 |
| **C-072-12** | **No validation collapse.** `FIELD-DEFINITION` is kept distinct from `VALIDATION-RULE` and runtime validation, and no check is defined. | §13; FD-13 |
| **C-072-13** | **Ownership.** Registry governs definitions; each model keeps its Records, their values and its field architecture. | §15; FD-14 |
| **C-072-14** | **Semantic layer.** Field semantics follow Artifact 062's L1 and downward-only rules. | §14; FD-15 |
| **C-072-15** | **Reference legality.** Every concrete reference the family establishes obeys Artifact 063: the domain scope names only declared entities, no declared-field category is created, and no mandatory relation is invented. | §21 |
| **C-072-16** | **No domain-instance authority.** No W, E, P, V or I Record, value or state supplies semantic authority. | RF-072-5; FD-16 |
| **C-072-17** | **No runtime authority.** No running process, service, plugin, linter or validator supplies semantic authority. | RF-072-6; FD-17 |
| **C-072-18** | **Resolution.** The resolution obligation is stated without resolver mechanics and without claiming the complete id+version representation. | §19 |
| **C-072-19** | **Versionability.** Versionability is stated without 108–110's mechanics, and their representation is not prohibited. | §20 |
| **C-072-20** | **LS metadata.** `LS: LS-1` is reproduced exactly while the LS-2 role inconsistency is recorded, not silently fixed. | §17; SC-072-D |
| **C-072-21** | **Handoff.** 073 receives semantic obligations for structural encoding; no schema is authored here. | §28 |
| **C-072-22** | **078 boundary.** The final schema/field boundary is not redefined in advance. | §11; SC-072-E |
| **C-072-23** | **No canon write.** No concrete `FIELD-DEFINITION`, field inventory or canonical data is authored, and nothing is written under `canon/**`. | §2; FD-22 |
| **C-072-24** | **Requirement IDs.** The text of RR-16 and RR-27 is not invented. | SC-072-C |
| **C-072-25** | **File scope.** This artifact's changes are confined to `docs/registry/field_definition.md`. | row 072 |
| **C-072-26** | **Row metadata.** The header reproduces row 072's metadata exactly. | row 072 |
| **C-072-27** | **064 consumed.** Kind 4's name, responsibility and admission answers are consumed unchanged, and the family is merged with no other Kind. | §5 |
| **C-072-28** | **Universal-tier meaning bounded.** No envelope field's presence or constitutional role is redefined, and no model-owned meaning — provenance meaning, Kind meaning — is absorbed. | §7; FD-6 |
| **C-072-29** | **Name ≠ semantic.** A field name alone is not treated as identifying one semantic across models. | §7, §9; FD-1 |
| **C-072-30** | **No field assigned.** No concrete field is placed at a tier or in a domain beyond what the sources state. | §8, §23 |
| **C-072-31** | **Realization bounded.** No serialization, schema language or generated validator is adopted. | SC-072-K |

## 28. Concept Separation and Handoff to 073

| Concept | What it is | Not to be confused with |
|---|---|---|
| field | an element of a Record's structure, at one of three tiers (RMS §14) | its definition |
| field occurrence | the field present in a schema or Record — structure | the field's meaning |
| field meaning | what the field says about the Record that carries it | its values or value set |
| field domain | at least the scope its meaning holds over (§8) | a schema's applicable Model and Kind |
| `FIELD-DEFINITION` | the Registry Kind whose Records govern one field's meaning and domain | a schema, a vocabulary, a constraint, a validator |
| `SCHEMA-DEFINITION` | the Registry Kind whose Records define a schema, composing field definitions | field meaning |
| `CONTROLLED-VOCABULARY` | the Registry Kind governing a set of values or terms and their meaning | field meaning |
| a Record carrying the field | a domain Record owned by its model | a field definition |
| Artifact 072 — this document | the authoritative family specification | a concrete Record, inventory or schema |
| Artifact 073 | the structural contract for `FIELD-DEFINITION` Records | the schema of any domain Record |
| Artifact 078 | the schema/field boundary contract | this family |

**To 073** (`H: 072`; `Val`: *"definition resolves; versionable; references only declared entities
(063)"*; `Done`: *"schema"*; `Why`: *"LS-2"*). 073 may derive from this document, without redesign:

- the family's identity — Kind 4, partition R (§5, §22);
- one field semantic per Record: one field's meaning over one domain (§6; FD-1 to FD-3);
- the domain obligation, as far as established — a scope at one of the three tiers, naming a
  declared model or Kind where the tier requires it (§8; FD-3, FD-4; RF-072-1);
- the universal-tier limits and the closed seven-field envelope (§7, §9, §22; FD-6, FD-7);
- no universalization of model or Kind fields (FD-5);
- the custody and ownership split (§15; FD-14);
- the resolution and versionability obligations (§19, §20);
- the reference rules RF-072-1 to RF-072-9;
- the L1 constraints (§14; FD-15).

073 chooses the structural encoding these require. This document prescribes none of 073's element
names, serialization, schema notation, carrier shape, cardinality syntax, nullability or default
values, reference-carrier shape, domain representation or field-name representation, and defines no
parser or validator behaviour. 073 encodes only the structural consequences of the obligations
established here; nothing here asks 073 to close representation rows 108–110 own (§20) or the edge
row 078 owns (§11). Not delegated to 073: a value or type domain, a vocabulary relation, field
composition, cardinality, requiredness or order, a field inventory, field admission, Registry
governance, evolution and versioning design, and validator or resolver implementation. Row 073's own
`Val` and `Done` are not enlarged.

## 29. Handoff to 078 and Other Downstream Owners

**To 078** (`H: 076,072`; `Done`: *"overlap resolved — a schema composes field definitions and owns
cardinality/required/order; a field definition owns meaning and domain"*). 078 may take from this
document: field meaning belongs to `FIELD-DEFINITION`; field domain belongs to it as far as §8
establishes; the family holds no composition, cardinality, requiredness, order, type or default.
078 still owns how schemas compose field definitions, the semantics of schema cardinality,
requiredness and order, any edge still open — type, default, and the relation of a field's domain to
a schema's applicable Model and Kind — and anything else not source-closed. Row 078's `Val` and
`Done` are not enlarged.

| Other downstream owner | Keeps |
|---|---|
| 076; 077 | the `SCHEMA-DEFINITION` family and schema |
| 081; 082 | the `CONTROLLED-VOCABULARY` family and schema |
| 088–089; 090–091 | `CONSTRAINT-DEFINITION`; `VALIDATION-RULE` |
| 065 | who may propose, approve and deprecate a definition |
| 108; 109; 110 | evolution; versioning and pinning; supersession and deprecation |
| 111 | concrete definition-dependency rules |
| 112; 113; 114; 115; 116 | reference validator (*"rejects any definition referencing a domain instance"*); constraint binder; kernel; Registry definition resolution; validation suite |
| 152 | committing `FIELD-DEFINITION` Records, after G-CANON-R |
| 179–180; 274–275; 301–302; 355; 366 | each model's field architecture and field domains, and its concrete field definitions |
| 459 | how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added — *"each through its own ceremony, never through a generic abstraction"* |

## 30. Roadmap Completion Trace

The statuses below assess Artifact 072 as a documentation specification (`T: doc`, `R: ARCH`).
**SPECIFICATION OBLIGATION SATISFIED** means the required semantic rule is stated, mandatory, and
bounded by its governing sources. It does not claim that downstream schemas, field inventories,
vocabularies, validators, version mechanisms, kernels or resolution services have been implemented,
executed or tested.

| Row 072 | Status | Where it is met |
|---|---|---|
| `Val`: *"definition resolves"* | **SPECIFICATION OBLIGATION SATISFIED** — a materialized `FIELD-DEFINITION` carries baseline Registry Record identity and must be resolvable; resolution is universal, not Registry work; resolvable ≠ legal; id+version resolution is 115's and version representation 108–110's | §19 (RS-072-1 to RS-072-5) |
| `Val`: *"versionable"* | **SPECIFICATION OBLIGATION SATISFIED** — participation in governed Registry definition evolution is required; mechanics and representation stay with 108–110 and are not prohibited | §20 (VS-072-1, VS-072-2) |
| `Val`: *"references only declared entities (063)"* | **SPECIFICATION OBLIGATION SATISFIED** — a domain names only a declared model or Kind; no declared-field category; domain and runtime instances excluded; no mandatory relation; resolvable ≠ legal; no validator run is claimed | §21 (RF-072-1 to RF-072-9) |
| `Done`: *"fields definable"* | **SPECIFICATION OBLIGATION SATISFIED** — a field established by a model's field architecture, at any of the three tiers, is definable with no per-model variant; no field is enumerated or authored, and the family establishes none | §8, §23 |
| `Why`: *"LS-2 partner for all field architecture"* | **SPECIFICATION OBLIGATION SATISFIED** — the Registry side of model field architecture is defined; the row's `LS: LS-1` is preserved and the inconsistency recorded | §16, §17; SC-072-D |
| `H: 064` | **SATISFIED** — Kind 4, its responsibility and its admission answers consumed unchanged | §5 |
| `LS: LS-1` | **PRESERVED** — label kept; no pair, class or meaning invented; relation to LS-2 recorded | §17; SC-072-D |
| `→ 073` | **SATISFIED** — semantic contract handed off; no schema built | §28 |

No field, field inventory, schema, vocabulary, constraint, validator or Registry Record created. No
field placed at a tier or in a domain beyond what the sources state.

---

*Artifact 072 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. This document specifies the `FIELD-DEFINITION` family chiefly from
Record Model System §4, §5, §6.1, §10–§10.3, §10.6, §14, Appendix B and Appendix H, Master Blueprint
§9.4, §13.6e, §13.7 and §13.7a, and Roadmap rows 072 and 078, with Artifact 064 as its input. It is
not a Registry Record, holds no canonical data, defines no schema, field, vocabulary, validator or
algorithm, and implements nothing. Where it differs from the Master Blueprint, the Record Model
System, or the OS File Build Roadmap, those governing sources are correct and this document is
wrong.*
