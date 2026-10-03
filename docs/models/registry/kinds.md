# COOLBOY12 — Registry Kind Taxonomy

**Artifact 064** · Registry kind taxonomy · `docs/models/registry/kinds.md` · Own: R · RM: R ·
T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P3/3a · Req: RR-16 · BP: §9.4 · RMS: §10.1 · H: 060,057 · S: — · LS: LS-1 · G: — ·
→ 066–107 · Val: exactly fourteen Kinds, each with admission rationale · Done: fourteen ·
Why: required by its phase responsibility · Risk: high · ∥: no

## 1. Purpose

This contract answers one question — **which fourteen Kinds does the Registry Record Model have, and
why does each hold first-class Kind status under the Kind Admission Test?**

The roster is not discovered here. RMS §10.1 already states it: *"Final Kind taxonomy — CLOSED at
fourteen"*, `FROZEN`. Artifact 057 binds RMS §13's fourteen questions to every Registry Kind
(C-057-01). This contract records the source-frozen roster and, for each Kind, a source-grounded
answer to each of the fourteen questions:

```
RMS §10.1 roster (fourteen, FROZEN)  +  Artifact 057 / RMS §13 (fourteen questions)  =  064
```

It does not answer what fields a Kind has, how its schema works, who approves a definition, how
definitions evolve, how references resolve or depend, how validation runs, or how a future Kind
is added (§3).

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: ARCH` · `SoT: AUTHORITATIVE` about the Registry Kind taxonomy ·
`Auth: governing` · `Canon: n/a` · `CD: no`. This document is not a Registry Record, holds no
Registry data, creates no `KIND-DEFINITION` or other Record, and defines no schema. Where it
differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those
sources are right and this document is wrong.**

`Req: RR-16` is reproduced from row 064. The requirement register is not in the supplied source set,
so the ID is carried forward unverified and no requirement text is stated for it (GAP-C; Revolving
Resolution Note).

## 3. Scope

**In scope.** The fourteen Registry Kinds, by their RMS §10.1 names and in RMS §10.1 order; the
source-established responsibility of each; each Kind's answers to the fourteen questions; the
boundary between a Kind and the `KIND-DEFINITION` that defines it; the LS-1 obligation; the boundary
between the fourteen Kinds and the definition-family artifact names in rows 066–107.

**Out of scope, by owner.** Kind admission as a test (057); Registry sovereignty and authority
(060, 061); the semantic layers and their direction (062), including any Kind's layer placement;
reference legality (063); governance — who proposes, approves, deprecates (065); each definition
family's specification and schema, fields, references and cardinality (066–107); evolution,
versioning, supersession and deprecation (108–110); dependency rules (111); validators, binder,
kernel, resolution, identity binding (112–117); fixtures, examples and tests (118–124); how a new
Kind is added (459). No schema, field, Registry data, validator, algorithm or test is created.

## 4. Governing Sources and Frozen Inputs

| Source | What it gives this contract |
|---|---|
| RMS §10.1 | the fourteen Kinds, *"CLOSED at fourteen"*, `FROZEN`; `MODEL-DEFINITION` *"closes FG-V7-07 — the Kind exists"* |
| RMS §13; RMS §6.1 | the Kind Admission Test's fourteen questions; a Kind is *"A class of Record within one model"*; final counts R 14 |
| RMS §10, §10.2, §10.4–§10.7, §19; RMS §27 | definition Records are not configuration; schema, bootstrap, capability, constraint/validation, WSV/WSVR boundaries; *"MODEL-DEFINITION is a Registry Kind"* |
| Blueprint §9.4; §13.6; §13.6e; §13.9a; §13.10 | the Registry layer; the earlier ten-item roster; Registry definition categories; FG-V7-07 OPEN; identity grammar; the WSV family |
| Roadmap row 064; PART III (LS-1 to LS-6); rows 065–117, 459 | this artifact's metadata; the lockstep pairs; each family's assigned responsibility |
| Artifact 057 | the fourteen questions bound to R (C-057-01); classification ≠ admission; `KIND-DEFINITION` ≠ admission (C-057-08); no sufficiency rule (§5.3); no non-World ceremony (§8) |
| Artifact 060 | Registry is sovereign; definitions are Records; the roster is 064's |
| Artifact 061 §7 | the boundary table: what Registry governs, and what the owning model keeps, per definition subject |
| Artifacts 062, 063 | context only (`H` is 060 and 057): layers carry no placement for most Kinds; Registry reference legality |

## 5. Source Condition — Blueprint Roster vs RMS Final Roster

Blueprint §13.6 lists ten Registry kinds — `KIND-DEF` · `SUBTYPE-DEF` · `RELATIONSHIP-TYPE-DEF` ·
`FIELD-DEF` · `CONTROLLED-VOCABULARY` · `IDENTITY-GRAMMAR` · `WSVR-INDICATOR-DEF` ·
`VALIDATION-RULE` · `DERIVATION-RULE` · `SIMULATION-MODEL-DEF` — and §13.6e says *"The currently
declared roster is at §13.6 and extends by ordinary Registry change (§9.4)."* §13.6e records
*"OPEN — Registry's own taxonomy."*: whether a Record Model definition Kind exists is *"not
established by any source"* (FG-V7-07). §9.4: *"Registry architecture is frozen; Registry content
is extensible."*

RMS §10.1 later states the *"Final Kind taxonomy — CLOSED at fourteen"*, `FROZEN`, adding
`MODEL-DEFINITION` (*"closes FG-V7-07 — the Kind exists"*), `SCHEMA-DEFINITION`,
`CONSTRAINT-DEFINITION` and `CAPABILITY-DEFINITION`; RMS §27 records *"MODEL-DEFINITION is a
Registry Kind"*. Row 064 requires *"exactly fourteen Kinds"* and cites RMS §10.1.

**Treatment.** This contract uses the RMS §10.1 roster as the current Registry taxonomy. The
Blueprint's ten-item roster is historical state, not a parallel taxonomy; its abbreviations
(`KIND-DEF`, `SUBTYPE-DEF`, `FIELD-DEF`, `RELATIONSHIP-TYPE-DEF`, `WSVR-INDICATOR-DEF`,
`SIMULATION-MODEL-DEF`) are source aliases of the RMS names, not further Kinds. `MODEL-DEFINITION`
is not OPEN. *"Registry content is extensible"* lets definition content grow within the
architecture; it does not let this contract add a fifteenth Kind. How a future Kind could be added
is row 459's, not this contract's (SC-064-A, SC-064-C).

## 6. Normative Fourteen-Kind Roster

Exactly fourteen rows, in RMS §10.1 order. No other row is a Registry Kind.

| # | Kind | Source-established responsibility | Admission rationale | Detailed downstream owner |
|---|---|---|---|---|
| 1 | `MODEL-DEFINITION` | governed meaning about a declared Record Model; closes FG-V7-07 | §8 — 14 of 14 answered | 066–067 |
| 2 | `KIND-DEFINITION` | what a Kind means; the Registry partner of every Kind spec (LS-1) | §9 — 14 of 14 answered | 068–069 |
| 3 | `SUBTYPE-DEFINITION` | what one specialization of a Kind means | §10 — 14 of 14 answered | 070–071 |
| 4 | `FIELD-DEFINITION` | what a field means (LS-2) | §11 — 14 of 14 answered | 072–073; 078 |
| 5 | `SCHEMA-DEFINITION` | a schema's definition; Registry does not execute it | §12 — 14 of 14 answered | 076–077; 078 |
| 6 | `RELATIONSHIP-TYPE-DEFINITION` | what a relationship type is and which role owns it (LS-3) | §13 — 14 of 14 answered | 079–080 |
| 7 | `CONTROLLED-VOCABULARY` | what a value or term means; per-kind value sets | §14 — 14 of 14 answered | 081–082 |
| 8 | `IDENTITY-GRAMMAR` | the grammar's roster and its per-partition kind codes | §15 — 14 of 14 answered | 085; 117 |
| 9 | `WSVR-INDICATOR-DEFINITION` | what a world-state indicator means (LS-5) | §16 — 14 of 14 answered | 086–087 |
| 10 | `VALIDATION-RULE` | a mechanism or procedure for checking a condition (LS-4) | §17 — 14 of 14 answered | 090–091 |
| 11 | `CONSTRAINT-DEFINITION` | a condition that must hold (LS-4) | §18 — 14 of 14 answered | 088–089 |
| 12 | `CAPABILITY-DEFINITION` | a capability's semantic contract (LS-6) | §19 — 14 of 14 answered | 092–093 |
| 13 | `DERIVATION-RULE` | what may be recomputed, and how derived state is computed | §20 — 14 of 14 answered | 096–097 |
| 14 | `SIMULATION-MODEL-DEFINITION` | what a simulation model is; how an indicator behaves (LS-5) | §21 — 14 of 14 answered | 098–099; 100 |

**Count: fourteen.** R 14 is also RMS §13's final count. The downstream column names the family
rows whose `Val`, `Done` or name assigns that Kind's detail; it grants them nothing beyond their own
rows.

## 7. Admission Method

Each Kind answers the fourteen questions of RMS §13, as Artifact 057 §5.1 numbers them. The answers
are documentation grounded in the sources, not a new admission algorithm:

- **No score.** RMS §13 requires an answer to each question and states no rule for judging one
  (Artifact 057 §5.3). This contract invents no score, threshold, weighting or classifier.
- **No ceremony.** No source defines the act by which a Kind joins a closed non-World roster
  (Artifact 057 §8). The fourteen are already closed by RMS §10.1; this contract performs no
  admission act and invents none (SC-064-C).
- **Where an answer is model-level.** Some questions — chiefly lifecycle — are answered by the
  sources for Registry definitions as a whole, not per Kind. Those answers say so, and the
  per-Kind detail is left to its named owner rather than invented (SC-064-B).
- **Question 13, read for Registry Kinds.** Every Registry Kind is a class of Registry definition
  Records, so *why not a Registry definition* is read here as: why does this subject need its own
  Kind rather than being carried as Records of another Registry Kind? This is a reading, recorded
  as one (SC-064-I).

**Shared source facts.** Several answers rest on facts that hold for every Registry Kind. They are
named once and cited by label; each row still states its own answer.

| Label | Fact | Source |
|---|---|---|
| **F-1** | Registry definitions are Records: *"A kind definition is not a constant in source code"*; they *"needed identity, provenance, history, a gate, and a linter, and calling them infrastructure meant they were governed by convention instead of by rule"*. | §13.6e |
| **F-2** | Registry Records are semantic-definition Records — *"not configuration, not code constants, not metadata, not a catalog, not runtime."* | RMS §10 |
| **F-3** | *"Registry governs the definitions. Each Record Model owns its Records."* Registry owns its own R Records; it never owns another model's Records. | §13.6e; I-105; Artifact 061 §7 |
| **F-4** | A definition has *"a governed change path, and a temporal account"*. Evolution, versioning, supersession and deprecation are rows 108–110 (*"temporal account without a World History Record"*; *"consumers pin a version"*; *"deprecated ≠ deleted"*). | §13.6e; rows 108–110 |
| **F-5** | Definitions are authoritative about meaning; Registry is canon about meaning, never about the world. Derived output is recomputed and never authoritative. | §13.6; Artifact 052 §5.4; §29.6a; Artifact 053 |
| **F-6** | `status` is World-owned and not universal; a definition is not a state value of another Record. | RMS §4 |
| **F-7** | Relationship Record and History Record are World concepts; a Registry definition is a semantic object, not an edge between Records. | I-102; Artifact 055 |

## 8. MODEL-DEFINITION

**Source-established responsibility.** RMS §10.1 lists it first, *"(closes FG-V7-07 — the Kind
exists)"*; RMS §27: *"MODEL-DEFINITION is a Registry Kind"*. Artifact 061 §7 row 7: Registry governs
a `MODEL-DEFINITION` Record — governed meaning about a declared Record Model — and never the model's
sovereignty. Row 066: *"six models definable"*.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of one declared Record Model | RMS §10.1; Artifact 061 §7 row 7 |
| 2 | what semantic question | what is this Record Model, as the Registry defines it? | RMS §6 (R's question); row 066 |
| 3 | why independent identity | each model's definition is a distinct definition with its own identity and provenance (F-1); the six are definable one by one | F-1; row 066 `Done` |
| 4 | what persistent state | the governed meaning about one declared model; family content is 066's | F-1; row 066 |
| 5 | what lifecycle | the Registry definition lifecycle — governed change, temporal account; Kind-specific detail is 108–110's | F-4 |
| 6 | what authority | Registry governs the definition; the model's sovereignty is constitutional and neither granted nor held by the Record | F-3; Artifact 061 §7 row 7; RMS §2 |
| 7 | what references it | Registry definitions that name a model (an R → R reference, Artifact 063 §8.2); concrete relations are the families' | RMS §10.3; Artifact 063 |
| 8 | why not a field | a model definition is a governed Record, not a field or a constant | F-1; F-2 |
| 9 | why not a state | it is a definition, not a state of any Record | F-6 |
| 10 | why not a relationship | it defines one subject; it is not an edge between Records | F-7 |
| 11 | why not a subtype | RMS §10.1 lists it as its own Kind; it defines a model, not a specialization of a Kind | RMS §10.1 |
| 12 | why not a projection | it is authoritative definition content, not recomputed output | F-5 |
| 13 | why not a Registry definition (§7 reading) | no other Kind defines a Record Model; §13.6e left this exact Kind OPEN because none of its categories covered it, and RMS closes it as a Kind | §13.6e; RMS §10.1, §27 |
| 14 | what breaks if it is not first-class | FG-V7-07 reopens; the six models have no governed definition (row 066 `Why`: *"closes FG-V7-07"*) | RMS §27; row 066 |

## 9. KIND-DEFINITION

**Source-established responsibility.** §13.6e category *"What a Record of a kind is"* (with
`SUBTYPE-DEF` and `FIELD-DEF`); Artifact 061 §7 row 1: Registry governs *the definition of a kind*,
the owning model keeps which Records exist and what they mean. LS-1: *"every Kind spec ↔ its
Registry KIND-DEFINITION"*. Row 068: *"every Kind definable"*. Artifact 057: a `KIND-DEFINITION` is
not admission.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of what one Kind means | §13.6e; Artifact 057 §4 |
| 2 | what semantic question | what is a Record of this Kind? | §13.6e category table |
| 3 | why independent identity | each Kind has its own definition, paired one-to-one with its Kind spec (LS-1); a definition needs identity and provenance (F-1) | LS-1; F-1 |
| 4 | what persistent state | the defined meaning of one Kind; content is 068's | F-1; row 068 |
| 5 | what lifecycle | the Registry definition lifecycle; Kind-specific detail is 108–110's | F-4 |
| 6 | what authority | definition authority only: the owning model keeps its taxonomy, admission and Records; a `KIND-DEFINITION` is not admission | F-3; Artifact 061 §7 row 1; C-057-08 |
| 7 | what references it | its Kind spec, by lockstep (LS-1) | LS-1 |
| 8 | why not a field | *"A kind definition is not a constant in source code"* | F-1 |
| 9 | why not a state | a definition, not a state value | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | Kind meaning and subtype meaning are separate source rows (§9.4) and separate Kinds (RMS §10.1) | §9.4; RMS §10.1 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | it is the one Kind whose subject is a Kind's meaning; LS-1 pairs every Kind with a `KIND-DEFINITION` specifically | LS-1; row 068 `Why` |
| 14 | what breaks if it is not first-class | LS-1 has no Registry partner (row 068 `Why`: *"LS-1 partner for all 49 Kinds"*); Kind meaning returns to convention | LS-1; F-1 |

## 10. SUBTYPE-DEFINITION

**Source-established responsibility.** §13.6e category *"What a Record of a kind is"*; §9.4's
*Subtype semantics* row. Row 070: *"subtypes definable"*; its `Why`: *"V asset forms are subtypes,
not Kinds"*. Artifact 062: Registry governs the `SUBTYPE-DEFINITION`; the owning model keeps the
domain semantics of its Records that use the subtype.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of one specialization of a Kind | §9.4; §13.6e |
| 2 | what semantic question | what is true of this specialization of a Kind? | §9.4 *Subtype semantics* row |
| 3 | why independent identity | each subtype definition is distinct and must be governed and provenanced (F-1) | F-1; row 070 |
| 4 | what persistent state | the defined meaning of one subtype; content is 070's | row 070 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry governs the definition; the owning model keeps the domain semantics of its Records using the subtype | F-3; Artifact 062 §4.3 |
| 7 | what references it | Records of the owning model that use the subtype; concrete relations are the families' | §9.4; row 071 `→` |
| 8 | why not a field | a governed definition, not a field or constant | F-1; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | it defines subtypes; it is not itself a specialization of `KIND-DEFINITION` — the sources keep the two rows and the two Kinds apart | §9.4; RMS §10.1 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | subtype meaning is a distinct source layer from Kind meaning; RMS lists a separate Kind for it | §9.4; RMS §10.1 |
| 14 | what breaks if it is not first-class | specializations have no governed home and are pushed up into Kinds — row 070's *"V asset forms are subtypes, not Kinds"* fails | row 070 `Why`; P-7 ladder (Artifact 057 §6) |

## 11. FIELD-DEFINITION

**Source-established responsibility.** §13.6e: Registry owns *the definition of a field*; the model
owns *the values its Records carry* (Artifact 061 §7 row 2). LS-2: *"model field architecture ↔
Registry FIELD-DEFINITION"*. Row 078: *"a field definition owns meaning and domain"*.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of what a field means | §13.6e; Artifact 061 §7 row 2 |
| 2 | what semantic question | what does this field mean, and over what domain? | row 078 `Done` |
| 3 | why independent identity | each field definition is shared meaning that must be governed once, not restated per Record (F-1; §9.4's three documents that *"define the same term differently"*) | F-1; §9.4 |
| 4 | what persistent state | one field's meaning and domain; content is 072's | row 078; row 072 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry governs the definition; the model owns the values its Records carry | F-3; Artifact 061 §7 row 2 |
| 7 | what references it | each model's field architecture, by lockstep (LS-2) | LS-2 |
| 8 | why not a field | the definition of a field is not itself a field of the Records that carry it | §13.6e; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind in RMS §10.1; not a specialization of another definition Kind | RMS §10.1 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | field meaning is distinct from schema composition: *"a field definition owns meaning and domain"*, a schema *"composes field definitions"* | row 078; RMS PC-3 |
| 14 | what breaks if it is not first-class | LS-2 has no Registry partner (row 072 `Why`: *"LS-2 partner for all field architecture"*) | LS-2; row 072 |

## 12. SCHEMA-DEFINITION

**Source-established responsibility.** RMS §10.2: *"SCHEMA-DEFINITION is a Registry Record. Schema
implementation is not Registry runtime."* and *"Registry does not execute schemas."* Row 076:
*"Registry **defines** schemas; **does not execute** them"*. Artifact 061 §7 row 8.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of a schema | RMS §10.2 |
| 2 | what semantic question | what structure does this schema define — required fields, cardinality, constraints, applicable Model and Kind? | RMS §10.2 |
| 3 | why independent identity | a schema definition is a Registry Record with its own version and supersession | RMS §10.2; F-1 |
| 4 | what persistent state | the schema's defined content; detail is 076's | RMS §10.2; row 076 |
| 5 | what lifecycle | RMS §10.2 names version and supersession; their rules are 108–110's | RMS §10.2; F-4 |
| 6 | what authority | Registry defines the schema; the Records that conform stay with their model; no execution authority | F-3; Artifact 061 §7 row 8; RMS §10.2 |
| 7 | what references it | model schemas (row 077 `→` *"all model schemas"*); concrete relations are the families' | row 077 |
| 8 | why not a field | a schema composes fields and owns cardinality, requiredness and order; it is not one field | row 078 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; not a specialization of `FIELD-DEFINITION` (row 078 separates them) | RMS §10.1; row 078 |
| 12 | why not a projection | authoritative definition content; the runtime that executes it is not a Record | F-5; RMS §10.2 |
| 13 | why not a Registry definition (§7 reading) | composition is a distinct subject from field meaning: *"Registry SCHEMA-DEFINITION and FIELD-DEFINITION overlap at the edges"*, resolved by row 078 without merging them | RMS PC-3; row 078 |
| 14 | what breaks if it is not first-class | schema meaning falls back into runtime or configuration — row 076's *"schema/runtime ambiguity"* reopens | RMS §10.2; row 076 `Why` |

## 13. RELATIONSHIP-TYPE-DEFINITION

**Source-established responsibility.** §13.6e: *"What a relationship type is and which role owns
it"*; Artifact 061 §7 row 3. RMS §15: *"Relationship definitions; never runtime relationship
ownership"*. LS-3, *"including the owning-role declaration"*. Row 079: *"participant roles **and
owning role** declared"*.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of a relationship type, with its participant roles and owning role | §13.6e; row 079 |
| 2 | what semantic question | what is this relationship type, and which role owns it? | §13.6e category table |
| 3 | why independent identity | each type is shared meaning that models resolve against; it needs identity and provenance (F-1) | F-1; LS-3 |
| 4 | what persistent state | the type's meaning, participant roles and owning role | row 079 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | definition authority only; the model decides whether it uses Relationship Records and owns the edges its Records hold | F-3; Artifact 061 §7 row 3; RMS §15 |
| 7 | what references it | each model's relationships, by lockstep (LS-3) | LS-3 |
| 8 | why not a field | a type definition with roles is a governed Record, not a field | F-1; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | it defines relationship types; it is not a relationship instance, and a Relationship Record is World's | F-7; RMS §15 |
| 11 | why not a subtype | its own Kind in RMS §10.1 and its own §13.6e category | RMS §10.1; §13.6e |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | relational meaning is its own §13.6e category (*Relational definition*), distinct from structural and semantic definitions | §13.6e |
| 14 | what breaks if it is not first-class | LS-3 has no Registry partner; owning roles go undeclared (row 079 `Why`: *"LS-3 partner"*) | LS-3; row 079 |

## 14. CONTROLLED-VOCABULARY

**Source-established responsibility.** §13.6e: *"What a value or term means"*. §9.4: *"Divergent
per-kind value sets are the intended design, not a defect to be unified"*; *"a forced enum union
across kinds is prohibited"*. Row 081: *"per-kind value sets may diverge; forced enum union
prohibited"*. Artifact 061 §7 row 9.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | a governed set of values or terms and their meaning | §13.6e |
| 2 | what semantic question | what does this value or term mean, for this Kind? | §13.6e; §9.4 |
| 3 | why independent identity | value sets are per-kind and may diverge, so each set is a distinct governed object | §9.4; row 081 |
| 4 | what persistent state | one vocabulary's values and their meaning; content is 081's | row 081 |
| 5 | what lifecycle | the Registry definition lifecycle — *"extends by ordinary Registry change"*; detail is 108–110's | §13.6e; F-4 |
| 6 | what authority | Registry governs the vocabulary; the model decides which value its Records carry | F-3; Artifact 061 §7 row 9 |
| 7 | what references it | Kinds whose values it governs; for example the Visual asset forms (*"a Registry-governed subtype vocabulary"*, RMS §11.1; PC-4) | RMS §11.1; PC-4; row 082 `→` |
| 8 | why not a field | a vocabulary is shared meaning that many Records' fields use; it is not one Record's field | §9.4; F-2 |
| 9 | why not a state | it defines values; it is not a state of a Record, and `status` stays World-owned | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind and its own §13.6e category (*Semantic definition*) | RMS §10.1; §13.6e |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | value meaning is a distinct category from field meaning, which owns the field, not its per-kind values (§9.4: *"Shared structure, independent vocabulary"*) | §9.4; §13.6e |
| 14 | what breaks if it is not first-class | terms are defined in several places and diverge — *"Three different documents were therefore free to define the same term differently, and did."* — or are forced into one union | §9.4 |

## 15. IDENTITY-GRAMMAR

**Source-established responsibility.** §13.6e: *"The grammar's roster and its per-partition kind
codes"*. Artifact 061 §7 row 12: the authoritative kind-code mapping and the recorded grammar; never
re-deciding AD-1. Row 085: *"the six-partition grammar recorded as a Registry Record"*; its `Why`:
*"the grammar is governed, not hard-coded"*. The grammar itself is constitutional and unchanged
here (§13.9a; Artifact 034).

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the recorded identity grammar, with its partition roster and per-partition kind codes | §13.6e; row 085 |
| 2 | what semantic question | what grammar, partitions and kind codes does identity use? | §13.6e; §13.9a |
| 3 | why independent identity | the grammar is governed as a Record, not hard-coded (row 085 `Why`) | row 085; F-1 |
| 4 | what persistent state | the recorded grammar and the kind-code mapping | §13.6e; Artifact 061 §7 row 12 |
| 5 | what lifecycle | the Registry definition lifecycle for the recorded grammar; the grammar itself is constitutional (AD-1) and is not changed here | F-4; §13.9a |
| 6 | what authority | Registry records and governs the mapping; each model owns its Kind taxonomy and meaning — *"the kind taxonomy and the meaning of any kind are owned by the Record Model"* | §13.9a; Artifact 061 §7 row 12 |
| 7 | what references it | the identity parser, which must enforce the recorded grammar (row 117 `Val`) | row 117 |
| 8 | why not a field | the grammar is shared by every Record's identity; it is not one Record's field | §13.9a |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind and its own §13.6e category (*Identity definition*) | RMS §10.1; §13.6e |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | the grammar and kind-code roster are their own §13.6e category, distinct from the meaning of any one Kind | §13.6e |
| 14 | what breaks if it is not first-class | the grammar is hard-coded, and record and code drift (row 117 `Why`: *"prevents grammar drift between record and code"*) | rows 085, 117 |

## 16. WSVR-INDICATOR-DEFINITION

**Source-established responsibility.** RMS §10.7: *"defines what an indicator means: type, unit,
range, constraints, semantics"*; *"World owns current values. Registry owns meaning. Never one
Record per indicator."* §13.6e: *"An indicator definition is a Registry Record."* LS-5. Row 086
`Why`: *"the W/R boundary lives here"*. WSV itself is a World Record, not a Registry Kind.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed meaning of a world-state indicator | RMS §10.7; §13.6e |
| 2 | what semantic question | what does this indicator mean — type, unit, range, constraints, semantics? | RMS §10.7 |
| 3 | why independent identity | meaning is held apart from the value: *"It is not an arbitrary property embedded in source code and not a field of the Record carrying the value."* | §13.6e |
| 4 | what persistent state | type, unit, range, constraints and semantics; never values | RMS §10.7; row 086 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry owns indicator meaning; World owns the current value | RMS §10.7; Artifact 061 §7 row 5 |
| 7 | what references it | each indicator in WSV, *"reached from each indicator's registry reference"*; LS-5 | §13.10; LS-5 |
| 8 | why not a field | *"not a field of the Record carrying the value"* | §13.6e |
| 9 | why not a state | the current value is World state; the definition is not | RMS §10.7; I-108 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; meaning and behaviour are kept apart from `SIMULATION-MODEL-DEFINITION` | RMS §10.1, §10.7 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | indicator meaning is its own §13.6e category; the WSV family holds meaning, behaviour and value in three places, each of which *"Never holds"* the others | §13.6e; §13.10 |
| 14 | what breaks if it is not first-class | indicator meaning moves into WSV — *"the state record has started becoming the model"* | §13.10 |

## 17. VALIDATION-RULE

**Source-established responsibility.** RMS §10.6: *"a mechanism/procedure for checking a
condition"*; *"These are never collapsed."* Row 090: *"a **mechanism for checking** a
condition"*; its `Why`: *"separate from 088 by constitution"*. LS-4. Artifact 061 §7 row 4.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of a checking mechanism or procedure | RMS §10.6 |
| 2 | what semantic question | how is a condition checked? | RMS §10.6; row 090 |
| 3 | why independent identity | it is a separate tier from the condition it checks and from the runtime that runs it | RMS §10.6, §20 |
| 4 | what persistent state | the defined checking mechanism; content is 090's | row 090 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry owns the definition; runtime validators implement validation; each model owns its own semantic validation | RMS §10.6; Artifact 061 §7 row 4 |
| 7 | what references it | LS-4 (constraint ↔ rule ↔ validator); row 113's binder resolves a constraint to a rule | LS-4; row 113 |
| 8 | why not a field | a governed mechanism definition, not a field | F-1; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | RMS §10.6 forbids collapsing it with the condition; it is its own Kind | RMS §10.6 |
| 12 | why not a projection | authoritative definition content; implementation validation is runtime | F-5; RMS §20 |
| 13 | why not a Registry definition (§7 reading) | it cannot be carried as a `CONSTRAINT-DEFINITION`: *"These are never collapsed."* | RMS §10.6 |
| 14 | what breaks if it is not first-class | the check collapses into the condition or into code — LS-4 loses a member | RMS §10.6; LS-4 |

## 18. CONSTRAINT-DEFINITION

**Source-established responsibility.** RMS §10.6: *"a condition that must hold"*. Row 088: *"a
**condition that must hold**"*; its `Why`: *"RMS §10.6 forbids collapsing it into the check"*. LS-4.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of a condition that must hold | RMS §10.6 |
| 2 | what semantic question | what must hold? | RMS §10.6; §13.6e |
| 3 | why independent identity | the condition is a separate tier from the mechanism that checks it | RMS §10.6, §20 |
| 4 | what persistent state | the defined condition; content is 088's | row 088 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry owns the definition; a constitutional invariant stays the Blueprint's tier | RMS §20; F-3 |
| 7 | what references it | LS-4; row 113's binder (*"a constraint resolves to exactly one rule"*) | LS-4; row 113 |
| 8 | why not a field | a governed condition, not a field | F-1; F-2 |
| 9 | why not a state | a condition is not a state value | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; never collapsed with `VALIDATION-RULE` | RMS §10.6 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | it cannot be carried as a `VALIDATION-RULE`: *"These are never collapsed."* | RMS §10.6 |
| 14 | what breaks if it is not first-class | the condition collapses into the check (row 088 `Why`) | RMS §10.6; row 088 |

## 19. CAPABILITY-DEFINITION

**Source-established responsibility.** RMS §10.5: *"CAPABILITY-DEFINITION is a Registry Record — a
semantic contract. CAPABILITY-IMPLEMENTATION is a runtime mechanism and is not a Record."* and
*"Recording a capability's definition never makes that capability a Record Model."* RMS §19: *"No
capability becomes a Record Model or a Kind."* LS-6. Row 092: *"semantic contract only;
implementation is runtime"*.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the semantic contract of one capability | RMS §10.5 |
| 2 | what semantic question | what is this capability's contract? | RMS §10.5; row 092 |
| 3 | why independent identity | each capability has a definition distinct from its runtime implementation (LS-6) | RMS §10.5; LS-6 |
| 4 | what persistent state | the contract; never runtime state | RMS §10.5; row 092 |
| 5 | what lifecycle | the Registry definition lifecycle; the implementation's lifecycle is runtime and not a Record's | F-4; RMS §10.5 |
| 6 | what authority | Registry governs the contract; no runtime control and no modelhood | Artifact 061 §7 row 10; RMS §10.5, §19 |
| 7 | what references it | its implementation, by lockstep (LS-6) | LS-6 |
| 8 | why not a field | a governed contract, not a field | F-1; F-2 |
| 9 | why not a state | a contract, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind in RMS §10.1 | RMS §10.1 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (§7 reading) | no other Kind holds a capability's semantic contract; RMS adds it as a Kind distinct from the implementation it is paired with | RMS §10.1, §10.5 |
| 14 | what breaks if it is not first-class | the capability is defined only by its code, or recording it confers modelhood (row 092 `Why`: *"recording a capability must not confer modelhood"*) | RMS §10.5; row 092 |

## 20. DERIVATION-RULE

**Source-established responsibility.** §13.6e category *"What must hold, and what may be
recomputed"* (with `VALIDATION-RULE`). Row 096: *"how derived state is computed; derived never
authoritative"*; its `Why`: *"the derived layer resolves against it"*. `DERIVATION-DEFINITION`
(rows 094–095) is not an RMS §10.1 Kind (SC-064-E).

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed rule by which derived state is computed | row 096; §13.6e |
| 2 | what semantic question | how is this derived state computed? | row 096 |
| 3 | why independent identity | the derived layer resolves against it, so it must be a stable governed object | row 096 `Why`; F-1 |
| 4 | what persistent state | the rule; never the derived output | row 096; F-5 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry governs the rule; derived output is never authoritative | row 096; F-5 |
| 7 | what references it | the derived layer (row 096 `Why`) | row 096 |
| 8 | why not a field | a governed rule, not a field | F-1; F-2 |
| 9 | why not a state | a rule, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; §13.6e pairs it with `VALIDATION-RULE` in one category without merging them | RMS §10.1; §13.6e |
| 12 | why not a projection | the rule is authoritative; what it computes is the projection | F-5; row 096 |
| 13 | why not a Registry definition (§7 reading) | what may be recomputed is a distinct subject from what must hold or how it is checked | §13.6e; RMS §10.6 |
| 14 | what breaks if it is not first-class | the derived layer has nothing governed to resolve against (row 096 `Why`) | row 096 |

## 21. SIMULATION-MODEL-DEFINITION

**Source-established responsibility.** RMS §10.7: *"defines behaviour"*. §13.6e: *"What a
simulation model is"*; how an indicator behaves — dependencies, equations, thresholds — is a
`SIMULATION-MODEL-DEF`, an R Record. LS-5. Row 098: *"defines behaviour; **no Simulation Record
Model**"*; its `Why`: *"simulation is definition + consumption"*.

| # | 057 question | Source-grounded answer | Source basis |
|---|---|---|---|
| 1 | what semantic object | the governed definition of a simulation model | RMS §10.7; §13.6e |
| 2 | what semantic question | how does an indicator behave — dependencies, equations, thresholds? | §13.6e |
| 3 | why independent identity | behaviour is held apart from meaning and value; each model definition is governed (F-1) | §13.10; F-1 |
| 4 | what persistent state | the defined behaviour; never values | §13.10; row 098 |
| 5 | what lifecycle | the Registry definition lifecycle; detail is 108–110's | F-4 |
| 6 | what authority | Registry governs the definition; World owns the values; no Simulation Record Model | RMS §10.7; Artifact 061 §7 row 11; row 098 |
| 7 | what references it | WSV and WSVR by lockstep (LS-5); the simulation that consumes it | LS-5; row 098 `Why` |
| 8 | why not a field | a governed definition, not a field of WSV | §13.10 (*"Do not put model definitions into WSV"*) |
| 9 | why not a state | behaviour, not state | §13.10 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; kept apart from `WSVR-INDICATOR-DEFINITION` | RMS §10.1, §10.7 |
| 12 | why not a projection | authoritative definition content; a simulation run is not a Registry Record | F-5; row 098 |
| 13 | why not a Registry definition (§7 reading) | behaviour is its own §13.6e category (*Model definition*), distinct from indicator meaning | §13.6e; §13.10 |
| 14 | what breaks if it is not first-class | model definitions go into WSV, or a Simulation Record Model is invented | §13.10; row 098 |

## 22. LS-1 and the Kind vs KIND-DEFINITION Boundary

**A Kind is not its `KIND-DEFINITION`.** `KIND-DEFINITION` is one of the fourteen Kinds; a Record of
that Kind defines what some Kind means. The World Kind `CHARACTER` and a `KIND-DEFINITION` Record
describing `CHARACTER` are two objects. Classification, a roster entry, a `KIND-DEFINITION` and
admission are four statements that this contract does not equate (Artifact 057 §4, C-057-08).
Definition authority is not admission authority (Artifact 057 §9).

**LS-1.** Row 064 carries `LS: LS-1` — *"every Kind spec ↔ its Registry KIND-DEFINITION.
ATOMIC-PAIR."* The fourteen Registry Kinds are subject to it. This contract records that obligation
and creates no `KIND-DEFINITION` Record, canonical file, schema or directory: row 064 is `T: doc`,
`CD: no`, `Canon: n/a`, and the Roadmap assigns this artifact no Kind-definition set. The generic
`KIND-DEFINITION` architecture is rows 068 and 069. How Registry's own definitions begin is RMS
§10.4's: *"There is no circular self-definition requirement."* and *"Once Registry exists, its
definitions follow normal Record semantics."* (SC-064-D).

## 23. Downstream Family Boundary

RMS §10.1 closes the Registry taxonomy at fourteen. Rows 066–107 name further definition artifacts.
**An artifact name is not evidence of a Kind**, and this contract infers no Kind from a filename,
row name or the word *DEFINITION*:

| Row(s) | Artifact name | Kind status under this contract |
|---|---|---|
| 074–075 | `SEMANTIC-DEFINITION` | not a Registry Kind; representation under the fourteen not established |
| 083–084 | `IDENTITY-DEFINITION` | not a Registry Kind; representation not established; row 085 records `IDENTITY-GRAMMAR` |
| 094–095 | `DERIVATION-DEFINITION` | not a Registry Kind; representation not established; `DERIVATION-RULE` is rows 096–097 |
| 101–102 | `ROLE-BOUNDARY-DEFINITION` | not a Registry Kind; representation not established |
| 103–104 | `DEGRADED-MODE-DEFINITION` | not a Registry Kind; representation not established |
| 105 | `DIAGNOSTIC-VOCABULARY` | not a Registry Kind; row 105 states its content as *"recorded as a controlled vocabulary"* |
| 106 | `SIGNAL-CLASS` | not a Registry Kind; representation not stated beyond `H: 081` |
| 107 | `READER-ARCHETYPE` | not a Registry Kind; row 107 states its content *"as a controlled vocabulary"* |
| 078; 100 | schema–field boundary note; simulation 22-component contract | contracts on existing Kinds, not Kinds |

Where a row's representation under the fourteen is not established, that row resolves its own
representation; this contract invents no mapping (SC-064-E).

## 24. Prohibited Inferences

| # | Prohibited inference | Basis |
|---|---|---|
| 1 | The Registry taxonomy may exceed fourteen because the Blueprint calls Registry content extensible. | §5; RMS §10.1 |
| 2 | The Blueprint's ten-item roster is still the current roster. | §5; SC-064-A |
| 3 | `MODEL-DEFINITION` remains OPEN. | RMS §10.1, §27 |
| 4 | Every downstream artifact whose name ends in *DEFINITION* is a Registry Kind. | §23 |
| 5 | `SEMANTIC-DEFINITION` is a fifteenth Kind. | §23 |
| 6 | `IDENTITY-DEFINITION` is a fifteenth Kind. | §23 |
| 7 | `DERIVATION-DEFINITION` is a fifteenth Kind. | §23 |
| 8 | `ROLE-BOUNDARY-DEFINITION` is a fifteenth Kind. | §23 |
| 9 | `DEGRADED-MODE-DEFINITION` is a fifteenth Kind. | §23 |
| 10 | A Kind and its `KIND-DEFINITION` Record are the same thing. | §22 |
| 11 | Creating a `KIND-DEFINITION` admits the Kind. | C-057-08 |
| 12 | Registry definition authority implies admission authority over another model's Kind. | Artifact 057 §9 |
| 13 | `MODEL-DEFINITION` creates a sovereign Record Model. | §8; RMS §2; Artifact 061 §7 row 7 |
| 14 | `SCHEMA-DEFINITION` executes schemas. | §12; RMS §10.2 |
| 15 | `RELATIONSHIP-TYPE-DEFINITION` owns runtime domain relationships. | §13; RMS §15 |
| 16 | `CAPABILITY-DEFINITION` makes a runtime capability a Record. | §19; RMS §10.5 |
| 17 | `CAPABILITY-DEFINITION` creates another Record Model. | §19; RMS §10.5, §19 |
| 18 | `WSVR-INDICATOR-DEFINITION` owns current WSV values. | §16; RMS §10.7 |
| 19 | `SIMULATION-MODEL-DEFINITION` creates a Simulation Record Model. | §21; row 098 |
| 20 | `IDENTITY-GRAMMAR` lets this contract rewrite the universal identity grammar. | §15; §13.9a |
| 21 | `CONTROLLED-VOCABULARY` permits a universal status enum. | §14; §9.4; RMS §4 |
| 22 | `DERIVATION-RULE` makes derived output authoritative. | §20; F-5 |
| 23 | This contract owns the family schemas of 066–107. | §3 |
| 24 | This contract owns Registry governance (065). | §3 |
| 25 | This contract defines the future Kind-extension ceremony. | §7; SC-064-C |
| 26 | This contract must place every Registry Kind in an Artifact 062 layer. | SC-064-F |
| 27 | LS-1 authorizes this contract to create unlisted canonical files. | §22; SC-064-D |
| 28 | The fourteen Registry Kinds are a universal Kind taxonomy that W, E, P, V or I inherit. | RMS §4 nine prohibitions |

## 25. Source Conditions and Gaps

### SC-064-A — Blueprint Registry roster vs RMS §10.1

Blueprint: a ten-item *"currently declared roster"*; FG-V7-07 OPEN; content extensible. RMS §10.1:
*"Final Kind taxonomy — CLOSED at fourteen"*, `FROZEN`, with `MODEL-DEFINITION`. Row 064: *"exactly
fourteen Kinds"*. **Treatment:** the RMS fourteen are the current taxonomy; the Blueprint roster is
historical state, not a parallel taxonomy (§5).

### SC-064-B — sufficiency of an answer

RMS §13 and Artifact 057 require an answer to all fourteen questions and define no rule for judging
one (057 §5.3). **Treatment:** all fourteen are answered from source for every Kind; no score or
threshold is invented. Where the sources answer a question for Registry definitions as a whole —
chiefly lifecycle (F-4) — the answer says so, and Kind-specific detail is left to 108–110 and the
family rows.

### SC-064-C — non-World admission ceremony

Artifact 057 §8: no source defines the ceremony by which a Kind joins a closed non-World roster.
**Treatment:** this contract defines none and performs no admission act; row 459 (`H: 057,064`)
states how a new Kind is added — *"each through its own ceremony, never through a generic
abstraction"*.

### SC-064-D — LS-1 concrete Registry pairs

Row 064 carries LS-1; Artifact 057: every Kind has a definition in lockstep. The Roadmap gives this
artifact no Registry Kind-definition set of fourteen Records. **Treatment:** the obligation is
recorded; no file or Record is created. Which artifact authors the fourteen concrete
`KIND-DEFINITION` Records for the Registry's own Kinds is not established by current sources and is
assigned to none here.

### SC-064-E — downstream *DEFINITION* artifacts and unmapped semantics

Rows 066–107 name definition artifacts that RMS §10.1 does not list. Artifact 060 §16 pointed the
correspondence to row 064's `Val`. **Treatment:** this contract settles their Kind status — none is
a Kind — and records that their representation under the fourteen is not established by current
sources; it invents no mapping (§23). Artifact 062 §14.2 likewise records that change-and-operation
semantics corresponds to no RMS §10.1 Kind; this contract admits none for it.

### SC-064-F — semantic-layer placement

Artifact 062 does not place most Registry Kinds in a layer and assigns that placement to no
artifact. **Treatment:** this contract does not place them.

### SC-064-G — LS-1's count

LS-1 is stated as *"49 pairs"*; the Roadmap does not break the count down by model. This contract
derives nothing from the number and does not decide whether the fourteen Registry Kinds are counted
in it. The fourteen are subject to LS-1 by row 064's own `LS` field.

### SC-064-H — I-106 and the RMS closure

I-106: a listed non-World roster *"is revisable by that model's own design work until it declares
otherwise"*. RMS §10.1 records the Registry roster as *"CLOSED"*. Artifact 057 §8 does not decide
whether the RMS closures are the declarations I-106 anticipates. **Treatment:** this contract states
the current roster as RMS §10.1 fixes it and does not decide that question; any future change is row
459's to govern.

### SC-064-I — question 13 for Registry Kinds

RMS §13 asks every Kind *why not a Registry definition*. For Registry Kinds the question is read as:
why this subject needs its own Kind rather than being carried as Records of another Registry Kind.
**This is a reading, recorded as one**; Artifact 057 does not interpret the question. Each answer
cites the source separation it rests on.

## 26. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-064-01** | The normative roster contains exactly fourteen entries. | RMS §10.1; row 064 |
| **C-064-02** | All fourteen names exactly match RMS §10.1, in its order. | RMS §10.1 |
| **C-064-03** | No fifteenth Kind is introduced. | RMS §10.1 |
| **C-064-04** | `MODEL-DEFINITION` is present and not treated as OPEN. | RMS §10.1, §27 |
| **C-064-05** | Each of the fourteen has an admission rationale. | row 064 `Val` |
| **C-064-06** | Each rationale answers all fourteen questions of RMS §13 / Artifact 057. | RMS §13; C-057-01 |
| **C-064-07** | No admission score or sufficiency threshold is invented. | Artifact 057 §5.3 |
| **C-064-08** | No non-World admission ceremony is created. | Artifact 057 §8 |
| **C-064-09** | A Kind is not its `KIND-DEFINITION` Record. | Artifact 057 §4 |
| **C-064-10** | A `KIND-DEFINITION` is not admission. | C-057-08 |
| **C-064-11** | Definition authority is not admission authority. | Artifact 057 §9 |
| **C-064-12** | Registry governs definitions; each model keeps ownership of its Records. | §13.6e; I-105 |
| **C-064-13** | No downstream definition artifact becomes a Kind because its name ends in *DEFINITION*. | §23 |
| **C-064-14** | `SEMANTIC-DEFINITION` is not in the roster. | §23 |
| **C-064-15** | `IDENTITY-DEFINITION` is not in the roster. | §23 |
| **C-064-16** | `DERIVATION-DEFINITION` is not in the roster. | §23 |
| **C-064-17** | `ROLE-BOUNDARY-DEFINITION` is not in the roster. | §23 |
| **C-064-18** | `DEGRADED-MODE-DEFINITION` is not in the roster. | §23 |
| **C-064-19** | `SCHEMA-DEFINITION` remains definition, not schema execution. | RMS §10.2 |
| **C-064-20** | `CONSTRAINT-DEFINITION` and `VALIDATION-RULE` remain distinct Kinds. | RMS §10.6 |
| **C-064-21** | `CAPABILITY-DEFINITION` remains distinct from its runtime implementation. | RMS §10.5 |
| **C-064-22** | `WSVR-INDICATOR-DEFINITION` owns meaning, not the World's current value. | RMS §10.7 |
| **C-064-23** | `SIMULATION-MODEL-DEFINITION` creates no Simulation Record Model. | row 098 |
| **C-064-24** | `MODEL-DEFINITION` creates no sovereign model. | RMS §2; Artifact 061 §7 row 7 |
| **C-064-25** | `IDENTITY-GRAMMAR` does not reopen Artifact 034 or AD-1. | §13.9a; Artifact 061 §7 row 12 |
| **C-064-26** | No Registry Kind is placed in an Artifact 062 layer where the sources are silent. | SC-064-F |
| **C-064-27** | LS-1 is recorded without creating unassigned canonical files. | SC-064-D |
| **C-064-28** | None of 065's governance is implemented. | row 065 |
| **C-064-29** | None of 066–107's family specifications or schemas is implemented. | rows 066–107 |
| **C-064-30** | None of 108–117's evolution or implementation work is implemented. | rows 108–117 |
| **C-064-31** | No future Kind-extension ceremony owned by 459 is implemented. | row 459 |
| **C-064-32** | Only `docs/models/registry/kinds.md` is changed by this artifact. | row 064 |
| **C-064-33** | Roadmap `Val` is satisfied. | §28 |
| **C-064-34** | Roadmap `Done` is satisfied. | §28 |
| **C-064-35** | The fourteen Registry Kinds are not a universal Kind taxonomy, and no envelope field is added. | RMS §4 |

## 27. Downstream Handoff

| Artifact | May assume from 064 | Must still define |
|---|---|---|
| **065** governance (`H: 064`; row 064's `→` does not name it) | the frozen fourteen-Kind taxonomy | who may propose, approve, deprecate a definition |
| **066–107** families | the roster, each Kind's responsibility boundary and rationale, the no-fifteenth-Kind rule, Kind ≠ `KIND-DEFINITION`, LS-1 | each family's specification and schema: fields, references, versioning, constraints, cardinality; the representation of rows §23 lists |
| **108–110** evolution | that every Kind's lifecycle is the Registry definition lifecycle (F-4) | evolution, versioning, supersession and deprecation |
| **459** extensibility | that the current Registry taxonomy is exactly fourteen | how a new Kind is added |

## 28. Roadmap Completion Trace

| Row 064 | Status | Where it is met |
|---|---|---|
| `Val`: *"exactly fourteen Kinds"* | **SATISFIED** | §6; C-064-01 to C-064-04 |
| `Val`: *"each with admission rationale"* | **SATISFIED** — fourteen Kinds × fourteen questions | §8–§21; C-064-05, C-064-06 |
| `Done`: *"fourteen"* | **SATISFIED** | §6 |
| `H: 060,057` | **SATISFIED** — sovereignty and the admission test consumed unchanged | §2, §7, §22 |
| `LS: LS-1` | **RECORDED** — obligation stated; no Record created | §22; SC-064-D |
| `→ 066–107` | **SATISFIED** — handoff stated | §27 |

No schema created. No Registry data created. No governance implemented. No future extension
ceremony defined. No fifteenth Kind admitted.

---

*Artifact 064 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This document
states the Registry Kind taxonomy from Record Model System §10.1 and §13, Master Blueprint §9.4,
§13.6 and §13.6e, and Roadmap row 064, with each Kind's admission rationale under Artifact 057. It
is not a Registry Record, holds no canonical data, defines no schema, field, validator or algorithm,
and implements nothing. Where it differs from the Master Blueprint, the Record Model System, or the
OS File Build Roadmap, those governing sources are correct and this document is wrong.*
