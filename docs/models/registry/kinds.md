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
(C-057-01). This contract records the source-frozen roster and, for each Kind, an answer to every
one of the fourteen questions — question 13 under the `AUTHOR-DECIDED` Registry application of
Artifact 057 §5.4, never as an RMS statement (SC-064-I):

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
| Blueprint §9.4; §13.6; §13.6e; §13.9a | the Registry layer; the earlier ten-item roster; Registry definition categories and the WSV attribute table; FG-V7-07 OPEN; identity grammar. §13.10 is flagged PROPOSED and is not relied on (SC-064-K) |
| Roadmap row 064; PART III (LS-1 to LS-6); rows 065–117, 459 | this artifact's metadata; the lockstep pairs; each family's assigned responsibility |
| Artifact 057 | the fourteen questions bound to R (C-057-01); classification ≠ admission; `KIND-DEFINITION` ≠ admission (C-057-08); no sufficiency rule (§5.3); no non-World ceremony (§8); question 13's Registry application, `AUTHOR-DECIDED` (§5.4, AD-057-R13) |
| Artifact 003 — Registry LS-1 self-hosting exception; Roadmap §0.7, rows 074–075 | `AUTHOR-DECIDED` (AD-LS1-R-BOOTSTRAP): the ordering of the Registry's own fourteen LS-1 pairs, and the rows that own the Registry `KIND-DEFINITION` set (SC-064-D) |
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

| # | Kind | Source-established responsibility | Admission rationale | Related downstream rows |
|---|---|---|---|---|
| 1 | `MODEL-DEFINITION` | governed meaning about a declared Record Model; closes FG-V7-07 | §8 — 14 questions answered; Q13 under Artifact 057 §5.4 | 066–067 |
| 2 | `KIND-DEFINITION` | what a Kind means; the Registry partner of every Kind spec (LS-1) | §9 — 14 questions answered; Q13 under Artifact 057 §5.4 | 068–069 |
| 3 | `SUBTYPE-DEFINITION` | what one specialization of a Kind means | §10 — 14 questions answered; Q13 under Artifact 057 §5.4 | 070–071 |
| 4 | `FIELD-DEFINITION` | what a field means (LS-2) | §11 — 14 questions answered; Q13 under Artifact 057 §5.4 | 072–073; 078 |
| 5 | `SCHEMA-DEFINITION` | a schema's definition; Registry does not execute it | §12 — 14 questions answered; Q13 under Artifact 057 §5.4 | 076–077; 078 |
| 6 | `RELATIONSHIP-TYPE-DEFINITION` | what a relationship type is and which role owns it (LS-3) | §13 — 14 questions answered; Q13 under Artifact 057 §5.4 | 079–080 |
| 7 | `CONTROLLED-VOCABULARY` | what a value or term means; per-kind value sets | §14 — 14 questions answered; Q13 under Artifact 057 §5.4 | 081–082 |
| 8 | `IDENTITY-GRAMMAR` | the grammar's roster and its per-partition kind codes | §15 — 14 questions answered; Q13 under Artifact 057 §5.4 | 085; 117 |
| 9 | `WSVR-INDICATOR-DEFINITION` | what a world-state indicator means (LS-5) | §16 — 14 questions answered; Q13 under Artifact 057 §5.4 | 086–087 |
| 10 | `VALIDATION-RULE` | a mechanism or procedure for checking a condition (LS-4) | §17 — 14 questions answered; Q13 under Artifact 057 §5.4 | 090–091 |
| 11 | `CONSTRAINT-DEFINITION` | a condition that must hold (LS-4) | §18 — 14 questions answered; Q13 under Artifact 057 §5.4 | 088–089 |
| 12 | `CAPABILITY-DEFINITION` | a capability's semantic contract (LS-6) | §19 — 14 questions answered; Q13 under Artifact 057 §5.4 | 092–093 |
| 13 | `DERIVATION-RULE` | what may be recomputed, and how derived state is computed | §20 — 14 questions answered; Q13 under Artifact 057 §5.4 | 096–097 |
| 14 | `SIMULATION-MODEL-DEFINITION` | what a simulation model is; how an indicator behaves (LS-5) | §21 — 14 questions answered; Q13 under Artifact 057 §5.4 | 098–099; 100 |

**Count: fourteen.** R 14 is also RMS §13's final count. The last column lists related Roadmap rows
whose own `Val`, `Done` or name concerns that Kind; it grants them nothing beyond their own rows,
and a row's name is not the Kind's name (§23). **Rationale status:** every question is answered for
every Kind — 196 of 196 cells. Question 13's answers apply Artifact 057 §5.4, an `AUTHOR-DECIDED`
rule, not an RMS statement (SC-064-I).

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
- **Question 7 records only references.** *What references it* is answered only by an incoming
  reference relation a source establishes. Lockstep (LS-1 to LS-8), a Roadmap `→` unlock, a build
  dependency, semantic consumption and an admissible target category (Artifact 063) are not
  reference evidence. Where no incoming reference is source-established, the row says so and leaves
  the relation to the applicable family.
- **Question 13 is not rewritten.** RMS §13 asks every Kind *why not a Registry definition*, and
  Artifact 057 §5.1 carries it unchanged. For Registry candidates, Artifact 057 §5.4 applies it as
  a reducibility test (`AUTHOR-DECIDED`, AD-057-R13): could the candidate be represented faithfully
  as a Record of an existing Registry Kind? Each row names its reduction targets and the
  distinction that reduction would collapse. The rule is an author decision, not an RMS statement,
  and an answer is documentation, not a score (SC-064-I).

**Shared source facts.** Several answers rest on facts that hold for every Registry Kind. They are
named once and cited by label; each row still states its own answer.

| Label | Fact | Source |
|---|---|---|
| **F-1** | Registry definitions are Records: *"A kind definition is not a constant in source code"*; they *"needed identity, provenance, history, a gate, and a linter, and calling them infrastructure meant they were governed by convention instead of by rule"*. | §13.6e |
| **F-2** | Registry Records are semantic-definition Records — *"not configuration, not code constants, not metadata, not a catalog, not runtime."* | RMS §10 |
| **F-3** | *"Registry governs the definitions. Each Record Model owns its Records."* Registry owns its own R Records; it never owns another model's Records. | §13.6e; I-105; Artifact 061 §7 |
| **F-4** | Registry definitions share the obligation to have *"a governed change path, and a temporal account"*. Rows 108–110 define the Registry evolution, versioning, supersession and deprecation model downstream (*"temporal account without a World History Record"*; *"consumers pin a version"*; *"deprecated ≠ deleted"*). This contract defines no per-Kind lifecycle states. | §13.6e; rows 108–110 |
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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry governs the definition; the model's sovereignty is constitutional and neither granted nor held by the Record | F-3; Artifact 061 §7 row 7; RMS §2 |
| 7 | what references it | not established — declared Record Models are admissible targets and `MODEL-DEFINITION` Records are R → R targets (Artifact 063 §8.2), but naming a model is not referencing its `MODEL-DEFINITION`; concrete incoming references are the families' | RMS §10.3; Artifact 063 §8.2 |
| 8 | why not a field | a model definition is a governed Record, not a field or a constant | F-1; F-2 |
| 9 | why not a state | it is a definition, not a state of any Record | F-6 |
| 10 | why not a relationship | it defines one subject; it is not an edge between Records | F-7 |
| 11 | why not a subtype | RMS §10.1 lists it as its own Kind; it defines a model, not a specialization of a Kind | RMS §10.1 |
| 12 | why not a projection | it is authoritative definition content, not recomputed output | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `KIND-DEFINITION`, `SCHEMA-DEFINITION`. A Record Model is a partition-owned semantic architecture owning a whole Kind taxonomy; a Kind is a class of Record within one model, and a schema names its *applicable Model* as something it refers to. Either reduction collapses the model level into the Kind or structure level — the gap FG-V7-07 recorded and RMS §27 closed | RMS §6, §6.1, §10.2, §27; §13.6e (FG-V7-07) |
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
| 3 | why independent identity | each Kind's meaning is a distinct governed subject with its own provenance and change path | F-1; §13.6e |
| 4 | what persistent state | the defined meaning of one Kind; content is 068's | F-1; row 068 |
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | definition authority only: the owning model keeps its taxonomy, admission and Records; a `KIND-DEFINITION` is not admission | F-3; Artifact 061 §7 row 1; C-057-08 |
| 7 | what references it | not established — LS-1 pairs each Kind spec with its `KIND-DEFINITION` as an authoring obligation, not a reference edge; any concrete reference is the family's | LS-1; Artifact 003 (`LS`) |
| 8 | why not a field | *"A kind definition is not a constant in source code"* | F-1 |
| 9 | why not a state | a definition, not a state value | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | Kind meaning and subtype meaning are separate source rows (§9.4) and separate Kinds (RMS §10.1) | §9.4; RMS §10.1 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `MODEL-DEFINITION`, `SUBTYPE-DEFINITION`. Kind meaning — what is true of every record of one kind — is neither a model's architecture nor one specialization: §9.4 keeps *Kind semantics* and *Subtype semantics* as separate rows with separate dependencies, and LS-1 pairs each Kind with a `KIND-DEFINITION` specifically | §9.4; RMS §6, §6.1; LS-1 |
| 14 | what breaks if it is not first-class | LS-1 has no Registry partner (LS-1: *"every Kind spec ↔ its Registry KIND-DEFINITION"*); Kind meaning returns to convention | LS-1; F-1 |

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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry governs the definition; the owning model keeps the domain semantics of its Records using the subtype | F-3; Artifact 062 §4.3 |
| 7 | what references it | not established — §9.4 makes instances and projections depend on subtype semantics — a dependency, not a Record reference; row 071's `→` is an unlock | §9.4; row 071 |
| 8 | why not a field | a governed definition, not a field or constant | F-1; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | it defines subtypes; it is not itself a specialization of `KIND-DEFINITION` — the sources keep the two rows and the two Kinds apart | §9.4; RMS §10.1 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction target `KIND-DEFINITION`. A subtype depends on *"Registry, its kind"*; carrying it as a Kind definition would make each specialization a Kind, which row 070 rules out (*"V asset forms are subtypes, not Kinds"*) and the ladder forbids | §9.4; row 070; RMS §11.1; P-7 |
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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry governs the definition; the model owns the values its Records carry | F-3; Artifact 061 §7 row 2 |
| 7 | what references it | not established — LS-2 pairs model field architecture with `FIELD-DEFINITION` (lockstep); whether that architecture carries a concrete reference is downstream | LS-2 |
| 8 | why not a field | the definition of a field is not itself a field of the Records that carry it | §13.6e; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | a subtype specializes a Kind; a field definition specializes no Kind — it defines field meaning shared across kinds | §9.4 (RFS and *Subtype semantics* rows) |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction target `SCHEMA-DEFINITION`. A field definition *"owns meaning and domain"*; a schema composes field definitions and *"owns cardinality/required/order"*. Carried inside schemas, one field's meaning would be restated per schema and could diverge — the overlap PC-3 records and row 078 resolves without merging the Kinds | row 078; RMS PC-3; §9.4 |
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
| 7 | what references it | not established — row 077's `→` *"all model schemas"* is an unlock; the *"validation references"* RMS §10.2 lists are references a schema defines, not references to it | row 077; RMS §10.2 |
| 8 | why not a field | a schema composes fields and owns cardinality, requiredness and order; it is not one field | row 078 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; not a specialization of `FIELD-DEFINITION` (row 078 separates them) | RMS §10.1; row 078 |
| 12 | why not a projection | authoritative definition content; the runtime that executes it is not a Record | F-5; RMS §10.2 |
| 13 | why not a Registry definition (057 §5.4) | reduction target `FIELD-DEFINITION`. A schema holds composition — required fields, cardinality, constraints, applicable Model and Kind — across many fields; a field definition holds one field's meaning. Reducing it would lose the structure that row 078 assigns to schemas alone | RMS §10.2; row 078 |
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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | definition authority only; the model decides whether it uses Relationship Records and owns the edges its Records hold | F-3; Artifact 061 §7 row 3; RMS §15 |
| 7 | what references it | not established — LS-3 pairs each relationship with its type definition (lockstep); runtime relationship ownership stays with the model | LS-3; RMS §15 |
| 8 | why not a field | a type definition with roles is a governed Record, not a field | F-1; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | it defines relationship types; it is not a relationship instance, and a Relationship Record is World's | F-7; RMS §15 |
| 11 | why not a subtype | its own Kind in RMS §10.1 and its own §13.6e category | RMS §10.1; §13.6e |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `FIELD-DEFINITION`, `SCHEMA-DEFINITION`. A relationship type defines participant roles and an owning role between Records; field and schema definitions describe one Record's own meaning and structure. The relational category, and LS-3's pairing of relationships with this Kind, would be lost | §13.6e; row 079; LS-3; RMS §15 |
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
| 5 | what lifecycle | participates in Registry's definition evolution — the roster *"extends by ordinary Registry change"*; per-Kind lifecycle detail is 108–110's | §13.6e; F-4 |
| 6 | what authority | Registry governs the vocabulary; the model decides which value its Records carry | F-3; Artifact 061 §7 row 9 |
| 7 | what references it | not established — PC-4 orders the Visual subtype vocabulary before V artifacts (sequencing); row 082's `→` is an unlock | PC-4; row 082 |
| 8 | why not a field | a vocabulary is shared meaning that many Records' fields use; it is not one Record's field | §9.4; F-2 |
| 9 | why not a state | it defines values; it is not a state of a Record, and `status` stays World-owned | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind and its own §13.6e category (*Semantic definition*) | RMS §10.1; §13.6e |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction target `FIELD-DEFINITION`. A field's structure is shared across kinds while its value vocabulary is per-kind and may diverge; one field definition cannot carry several divergent value sets without the forced enum union §9.4 prohibits | §9.4; row 081 |
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
| 5 | what lifecycle | the recorded grammar participates in Registry's definition evolution (F-4); the grammar itself is constitutional (AD-1) and is not changed here | F-4; §13.9a |
| 6 | what authority | Registry records and governs the mapping; each model owns its Kind taxonomy and meaning — *"the kind taxonomy and the meaning of any kind are owned by the Record Model"* | §13.9a; Artifact 061 §7 row 12 |
| 7 | what references it | not established — row 117 binds the parser to the recorded grammar — enforcement, not a Record reference | row 117 |
| 8 | why not a field | the grammar is shared by every Record's identity; it is not one Record's field | §13.9a |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind and its own §13.6e category (*Identity definition*) | RMS §10.1; §13.6e |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `MODEL-DEFINITION`, `KIND-DEFINITION`, `FIELD-DEFINITION`. Each of those defines one model, one Kind or one field; the grammar and its per-partition kind codes span all six partitions and bind the parser (row 117). No single-subject definition carries that cross-partition roster | §13.6e; §13.9a; rows 085, 117 |
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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry owns indicator meaning; World owns the current value | RMS §10.7; Artifact 061 §7 row 5 |
| 7 | what references it | not established — Blueprint §13.10 says WSVR is reached from each indicator's registry reference, but §13.10 is flagged PROPOSED, an indicator is not a Record, and RMS §10.7 does not restate the reference; LS-5 is lockstep and adds none | §13.10 (PROPOSED); RMS §10.7; SC-064-K |
| 8 | why not a field | *"not a field of the Record carrying the value"* | §13.6e |
| 9 | why not a state | the current value is World state; the definition is not | RMS §10.7; I-108 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; meaning and behaviour are kept apart from `SIMULATION-MODEL-DEFINITION` | RMS §10.1, §10.7 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `FIELD-DEFINITION`, `SIMULATION-MODEL-DEFINITION`. An indicator definition is *"not a field of the Record carrying the value"* — indicators are not fields — and §13.6e keeps what an indicator means apart from how it behaves; either reduction erases the World/Registry boundary row 086 locates here | §13.6e; RMS §10.7; row 086 |
| 14 | what breaks if it is not first-class | indicator meaning falls back into code or into the Record carrying the value, and the World/Registry split row 086 names is lost | §13.6e; RMS §10.7; row 086 `Why` |

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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry owns the definition; runtime validators implement validation; each model owns its own semantic validation | RMS §10.6; Artifact 061 §7 row 4 |
| 7 | what references it | not established — LS-4 is lockstep; row 113's binder later establishes how a constraint resolves to a rule, and this contract grants no reference in either direction | LS-4; row 113 |
| 8 | why not a field | a governed mechanism definition, not a field | F-1; F-2 |
| 9 | why not a state | a definition, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | RMS §10.6 forbids collapsing it with the condition; it is its own Kind | RMS §10.6 |
| 12 | why not a projection | authoritative definition content; implementation validation is runtime | F-5; RMS §20 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `CONSTRAINT-DEFINITION`, `DERIVATION-RULE`. A checking procedure is not the condition it checks — *"These are never collapsed."* — and not a rule for what may be recomputed (§13.6e) | RMS §10.6, §20; §13.6e |
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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry owns the definition; a constitutional invariant stays the Blueprint's tier | RMS §20; F-3 |
| 7 | what references it | not established — LS-4 is lockstep; row 113's binder (*"a constraint resolves to exactly one rule"*) establishes that relation later, not here | LS-4; row 113 |
| 8 | why not a field | a governed condition, not a field | F-1; F-2 |
| 9 | why not a state | a condition is not a state value | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; never collapsed with `VALIDATION-RULE` | RMS §10.6 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction target `VALIDATION-RULE`. A condition that must hold is not the mechanism that checks it; RMS §10.6 and §20 keep them as separate tiers, and LS-4 pairs them rather than merging them | RMS §10.6, §20; LS-4 |
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
| 3 | why independent identity | each capability's contract is a governed subject distinct from its runtime implementation, which is not a Record | RMS §10.5 |
| 4 | what persistent state | the contract; never runtime state | RMS §10.5; row 092 |
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here; the implementation's lifecycle is runtime, not a Record's | F-4; RMS §10.5 |
| 6 | what authority | Registry governs the contract; no runtime control and no modelhood | Artifact 061 §7 row 10; RMS §10.5, §19 |
| 7 | what references it | not established — LS-6 pairs capability, definition and implementation (lockstep); the implementation is not a Record | LS-6; RMS §10.5 |
| 8 | why not a field | a governed contract, not a field | F-1; F-2 |
| 9 | why not a state | a contract, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | a subtype specializes a Kind; a capability contract specializes no Kind and is its own definition subject | §9.4; RMS §10.5 |
| 12 | why not a projection | authoritative definition content | F-5 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `MODEL-DEFINITION`, `KIND-DEFINITION`. *"No capability becomes a Record Model or a Kind"*: carrying a capability's contract as a model or Kind definition would confer the modelhood RMS §10.5 forbids, and its implementation is runtime, not a Record | RMS §10.5, §19; row 092 |
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
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry governs the rule; derived output is never authoritative | row 096; F-5 |
| 7 | what references it | not established — row 096's *"the derived layer resolves against it"* states consumption, not a Record reference | row 096 |
| 8 | why not a field | a governed rule, not a field | F-1; F-2 |
| 9 | why not a state | a rule, not a state | F-6 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; §13.6e pairs it with `VALIDATION-RULE` in one category without merging them | RMS §10.1; §13.6e |
| 12 | why not a projection | the rule is authoritative; what it computes is the projection | F-5; row 096 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `VALIDATION-RULE`, `CONSTRAINT-DEFINITION`. §13.6e separates what must hold from what may be recomputed: a derivation rule says how derived state is computed, which is neither a condition nor a check, and its output stays non-authoritative | §13.6e; RMS §10.6; row 096 |
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
| 3 | why independent identity | behaviour is held apart from meaning and value — how an indicator behaves is a `SIMULATION-MODEL-DEF`, an R Record — and each definition is governed (F-1) | §13.6e; F-1 |
| 4 | what persistent state | the defined behaviour; never values | RMS §10.7; row 098 |
| 5 | what lifecycle | participates in Registry's model-owned definition evolution (F-4); per-Kind lifecycle states, versioning and supersession are 108–110's and are not invented here | F-4 |
| 6 | what authority | Registry governs the definition; World owns the values; no Simulation Record Model | RMS §10.7; Artifact 061 §7 row 11; row 098 |
| 7 | what references it | not established — LS-5 is lockstep; the sources set an authority split — meaning, behaviour, value — not a reference graph | LS-5; §13.6e; RMS §10.7 |
| 8 | why not a field | a governed R Record, not a field of the World Record holding the values | §13.6e; RMS §10.7 |
| 9 | why not a state | behaviour, not state: World owns the current values | §13.6e; RMS §10.7 |
| 10 | why not a relationship | a semantic object, not an edge | F-7 |
| 11 | why not a subtype | its own Kind; kept apart from `WSVR-INDICATOR-DEFINITION` | RMS §10.1, §10.7 |
| 12 | why not a projection | authoritative definition content; a simulation run is not a Registry Record | F-5; row 098 |
| 13 | why not a Registry definition (057 §5.4) | reduction targets `MODEL-DEFINITION`, `WSVR-INDICATOR-DEFINITION`. A simulation model defines behaviour and is not a Record Model — row 098: *"no Simulation Record Model"* — so a model definition would misread it as a seventh model; carried as an indicator definition, behaviour would merge with meaning, which §13.6e keeps apart | RMS §10.7; row 098; §13.6e |
| 14 | what breaks if it is not first-class | behaviour has no governed home and falls into World state or code, or a Simulation Record Model is invented | RMS §10.7; row 098 |

## 22. LS-1 and the Kind vs KIND-DEFINITION Boundary

**A Kind is not its `KIND-DEFINITION`.** `KIND-DEFINITION` is one of the fourteen Kinds; a Record of
that Kind defines what some Kind means. The World Kind `CHARACTER` and a `KIND-DEFINITION` Record
describing `CHARACTER` are two objects. Classification, a roster entry, a `KIND-DEFINITION` and
admission are four statements that this contract does not equate (Artifact 057 §4, C-057-08).
Definition authority is not admission authority (Artifact 057 §9).

**LS-1 — resolved in decomposition; partners not yet landed.** Row 064 carries `LS: LS-1`.
Roadmap PART III: *"every Kind spec ↔ its Registry KIND-DEFINITION. ATOMIC-PAIR."* Artifact 003
keeps the default rule — *"An ATOMIC-PAIR with one half landed is incomplete regardless of whether
anything is blocked"* — and records one ordering exception, `AUTHOR-DECIDED` as
AD-LS1-R-BOOTSTRAP: the Registry's own fourteen pairs, because the generic `KIND-DEFINITION`
mechanism (068–069) cannot exist before the taxonomy that makes it meaningful, and RMS §10.4
holds that *"There is no circular self-definition requirement."* Under that exception:

- this contract finalises the taxonomy half;
- row 074 specifies, and row 075 materialises, the fourteen concrete `KIND-DEFINITION` Records,
  one per Kind of §6, conforming to 069 — the Registry's counterpart of rows 178, 257, 300, 345
  and 364;
- the partner obligation is not waived: row 123's lockstep tests reject a missing or mismatched
  partner, and exit-P3 and G-REG (row 124) cannot pass until row 075 has landed.

This contract is `T: doc`, `CD: no`, `Canon: n/a`, creates no `KIND-DEFINITION` Record, and does
not claim the fourteen partners exist. How Registry's own definitions begin is RMS §10.4's:
*"Once Registry exists, its definitions follow normal Record semantics."* (SC-064-D).

## 23. Downstream Family Boundary

RMS §10.1 closes the Registry taxonomy at fourteen. Rows 066–107 name further definition artifacts.
**An artifact name is not evidence of a Kind**, and neither is a row's `LS` field. This contract
infers no Kind from a filename, row name, the word *DEFINITION* or `LS: LS-1`:

| Row(s) | Artifact name | Row `LS` | Status under this contract |
|---|---|---|---|
| 074–075 | Registry self-Kind definition set contract; Registry Kind-Definition set | LS-1 | not Kinds: the contract and the set of fourteen `KIND-DEFINITION` Records partnering §6's Kinds (§22) |
| 083–084 | `IDENTITY-DEFINITION` | LS-1 | not a Registry Kind; representation not established; row 085 records `IDENTITY-GRAMMAR` |
| 094–095 | `DERIVATION-DEFINITION` | LS-1 | not a Registry Kind; representation not established; `DERIVATION-RULE` is rows 096–097 |
| 101–102 | `ROLE-BOUNDARY-DEFINITION` | LS-7 | not a Registry Kind; representation not established |
| 103–104 | `DEGRADED-MODE-DEFINITION` | LS-8 | not a Registry Kind; representation not established |
| 105 | `DIAGNOSTIC-VOCABULARY` | LS-1 | not a Registry Kind; row 105 states its content as *"recorded as a controlled vocabulary"* |
| 106 | `SIGNAL-CLASS` | LS-1 | not a Registry Kind; representation not stated beyond `H: 081` |
| 107 | `READER-ARCHETYPE` | LS-1 | not a Registry Kind; row 107 states its content *"as a controlled vocabulary"* |
| 078; 100 | schema–field boundary note; simulation 22-component contract | LS-1 | contracts on existing Kinds, not Kinds |

Rows 074–075 formerly named a `SEMANTIC-DEFINITION` family, which corresponds to no RMS §10.1 Kind;
the Roadmap revision of §0.7 withdrew it (SC-064-E). Where a row's representation under the
fourteen is not established, that row resolves its own representation; this contract invents no
mapping. The remaining non-roster rows carrying `LS: LS-1` are recorded at SC-064-J and not
repaired here.

## 24. Prohibited Inferences

| # | Prohibited inference | Basis |
|---|---|---|
| 1 | The Registry taxonomy may exceed fourteen because the Blueprint calls Registry content extensible. | §5; RMS §10.1 |
| 2 | The Blueprint's ten-item roster is still the current roster. | §5; SC-064-A |
| 3 | `MODEL-DEFINITION` remains OPEN. | RMS §10.1, §27 |
| 4 | Every downstream artifact whose name ends in *DEFINITION* is a Registry Kind. | §23 |
| 5 | `SEMANTIC-DEFINITION` is a fifteenth Kind. | §23; Roadmap §0.7 |
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
| 29 | Lockstep is a reference edge. | §7; Artifact 003 (`LS`) |
| 30 | A Roadmap `→` is a semantic or Record reference. | §7 |
| 31 | A downstream consumer thereby references a Registry definition Record. | §7 |
| 32 | An admissible Registry target category creates a concrete reference relation. | Artifact 063 RB-5 |
| 33 | Naming a declared Record Model is referencing its `MODEL-DEFINITION`. | §8 Q7; Artifact 063 §8.2 |
| 34 | This contract may rewrite RMS §13's question 13 for Registry Kinds. | §7; Artifact 057 §5.4 |
| 35 | A half-landed LS-1 pair is complete. | Artifact 003; SC-064-D |
| 36 | `LS: LS-1` on a non-roster row makes that row's subject a Kind. | SC-064-J |
| 37 | Every row of 066–107 must define fields, references, constraints and cardinality. | §27 |
| 38 | A statement in a Blueprint subsection flagged PROPOSED is settled architecture. | SC-064-K |
| 39 | A Registry Kind passes question 13 because RMS lists it. | Artifact 057 §5.4; C-057-17 |
| 40 | The Registry application of question 13 changes RMS's wording. | Artifact 057 §5.4; C-057-13 |
| 41 | The self-hosting exception waives the Registry's fourteen `KIND-DEFINITION` partners. | Artifact 003; §22 |
| 42 | The self-hosting exception applies to W, E, P, V or I. | Artifact 003 |
| 43 | Row 068 is itself the concrete `KIND-DEFINITION` for every Kind in the system. | Roadmap row 068; §0.7 |
| 44 | Row 069 contains all Kind definitions. | Roadmap row 069 |
| 45 | This contract materialises the fourteen Registry definitions. | §2; §22 |
| 46 | The "+1" in RMS §13's W 7+1 is an eighth World Kind. | SC-064-G; RMS §7 |
| 47 | The Registry Kind-Definition set is a Kind. | §23 |

## 25. Source Conditions and Gaps

### SC-064-A — Blueprint Registry roster vs RMS §10.1 — RESOLVED

Blueprint: a ten-item *"currently declared roster"*; FG-V7-07 OPEN; content extensible. RMS §10.1:
*"Final Kind taxonomy — CLOSED at fourteen"*, `FROZEN`, with `MODEL-DEFINITION`. Row 064: *"exactly
fourteen Kinds"*. **Treatment:** the RMS fourteen are the current taxonomy; the Blueprint roster is
historical state, not a parallel taxonomy (§5).

### SC-064-B — sufficiency of an answer — BOUNDED

RMS §13 and Artifact 057 require an answer to all fourteen questions and define no rule for judging
one (057 §5.3). **Treatment:** all fourteen are answered for every Kind; no score or threshold is
invented. Where the sources answer a question for Registry definitions as a whole — chiefly
lifecycle (F-4) — the answer says so, and Kind-specific detail is left to 108–110 and the family
rows. Artifact 057 §5.4 settles what question 13 means for a Registry Kind, not what makes an
answer sufficient.

### SC-064-C — non-World admission ceremony — DEFERRED TO 459

Artifact 057 §8: no source defines the ceremony by which a Kind joins a closed non-World roster.
**Treatment:** this contract defines none and performs no admission act; row 459 (`H: 057,064`)
states how a new Kind is added — *"each through its own ceremony, never through a generic
abstraction"*.

### SC-064-D — Registry taxonomy LS-1 self-hosting — RESOLVED

| | |
|---|---|
| **Source facts** | Row 064 carries `LS: LS-1`; PART III makes LS-1 an ATOMIC-PAIR of Kind spec and `KIND-DEFINITION`; RMS §10.4 rejects a circular self-definition requirement. |
| **Authorial build resolution** | AD-LS1-R-BOOTSTRAP, `AUTHOR-DECIDED`, recorded in Artifact 003 (*Registry LS-1 self-hosting exception*) and Roadmap §0.7. The Registry's own fourteen pairs receive a narrow ordering exception; row 074 specifies, and row 075 materialises, the fourteen concrete `KIND-DEFINITION` Records; rows 068–069 provide the generic family and schema. |
| **What it does not do** | Waive the partners; apply to W, E, P, V or I; weaken LS-1 or any other lockstep. |
| **Treatment here** | The taxonomy is finalised before the partners land, under that exception. The partners are not claimed to exist; exit-P3 and G-REG cannot pass until row 075 lands and row 123's lockstep tests pass. |

### SC-064-E — downstream *DEFINITION* artifacts and unmapped semantics

Rows 066–107 name definition artifacts that RMS §10.1 does not list. Artifact 060 §16 pointed the
correspondence to row 064's `Val`. **Treatment:** this contract settles their Kind status — none is
a Kind — and records that their representation under the fourteen is not established by current
sources; it invents no mapping (§23). The `SEMANTIC-DEFINITION` family formerly at rows 074–075 is
withdrawn by Roadmap §0.7; semantic material no RMS §10.1 Kind maps remains unmapped until its
owning contract resolves it. Artifact 062 §14.2 likewise records that change-and-operation
semantics corresponds to no RMS §10.1 Kind; this contract admits none for it.

### SC-064-F — semantic-layer placement — NOT INVENTED

Artifact 062 does not place most Registry Kinds in a layer and assigns that placement to no
artifact. **Treatment:** this contract does not place them.

### SC-064-G — LS-1's count — CLARIFIED

LS-1 is stated as *"49 pairs"*. Artifact 003 and Roadmap §0.7 record that the 49 are actual Kinds —
W 7 · E 7 · P 13 · R 14 · V 3 · I 5 — and that the "+1" in RMS §13's *"W 7+1"* is the WSV singleton,
which is not a Kind (RMS §7) and has no `KIND-DEFINITION` pair. This is a build reconciliation, not
a taxonomy rule; R stays fourteen, and the P 13 / VERDICT question remains CONFLICT-A's.

### SC-064-H — I-106 and the RMS closure

I-106: a listed non-World roster *"is revisable by that model's own design work until it declares
otherwise"*. RMS §10.1 records the Registry roster as *"CLOSED"*. Artifact 057 §8 does not decide
whether the RMS closures are the declarations I-106 anticipates. **Treatment:** this contract states
the current roster as RMS §10.1 fixes it and does not decide that question; any future change is row
459's to govern.

### SC-064-I — RMS §13 question 13 on Registry Kinds — RESOLVED

| | |
|---|---|
| **Literal question** | *why not a Registry definition* — unchanged (RMS §13; Artifact 057 §5.1). |
| **Resolution owner** | Artifact 057 §5.4, `AUTHOR-DECIDED` (AD-057-R13): for a Registry candidate, question 13 is applied as reducibility to an already-admitted Registry Kind. It is not attributed to RMS or the Blueprint. |
| **Treatment here** | Each of the fourteen question-13 rows names the existing Registry Kind or Kinds the subject could be reduced to and the source-established distinction that reduction would lose. None rests on roster membership. |

### SC-064-J — non-roster rows carrying LS-1 — RECORDED, NON-BLOCKING

| | |
|---|---|
| **Source A** | RMS §10.1 freezes the Registry at exactly fourteen Kinds. |
| **Source B** | Roadmap PART III defines LS-1 as Kind ↔ `KIND-DEFINITION`. |
| **Source C** | Rows whose subjects are not RMS §10.1 Kinds carry `LS: LS-1`: 078 schema–field boundary note, 083–084 `IDENTITY-DEFINITION`, 094–095 `DERIVATION-DEFINITION`, 100 simulation 22-component contract, 105 `DIAGNOSTIC-VOCABULARY`, 106 `SIGNAL-CLASS`, 107 `READER-ARCHETYPE`. Rows 101–102 and 103–104 carry LS-7 and LS-8, not LS-1. Rows 074–075 now carry LS-1 as the Registry's own partner set (§22). |
| **Conflict** | Their LS-1 metadata cannot be read as evidence that their subjects are Registry Kinds without contradicting RMS §10.1. |
| **Treatment** | The fourteen-Kind taxonomy stands; RMS §10.1 governs the taxonomy over Roadmap decomposition. These rows are not promoted to Kinds, and their metadata is neither repaired nor reinterpreted here. |
| **Route** | ROADMAP ISSUE — outside this artifact; non-blocking. |

### SC-064-K — Blueprint §13.10 is PROPOSED

Blueprint §13.10 is headed **PROPOSED**: *"This subsection records a resolution that is PROPOSED,
not settled."* The Roadmap keeps the flag open (DG-02), and RMS Appendix H records it as PC-2; RMS
§10.7 closes WSV granularity but does not restate §13.10's other statements. **Treatment:** no
answer in this contract rests on §13.10. Its statement that WSVR is reached from each indicator's
registry reference is recorded in `WSVR-INDICATOR-DEFINITION`'s question 7 and not relied on; the
WSV-family answers rest on §13.6e's WSV attribute table, RMS §10.7 and rows 086 and 098.

## 26. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-064-01** | The normative roster contains exactly fourteen entries. | RMS §10.1; row 064 |
| **C-064-02** | All fourteen names exactly match RMS §10.1, in its order. | RMS §10.1 |
| **C-064-03** | No fifteenth Kind is introduced. | RMS §10.1 |
| **C-064-04** | `MODEL-DEFINITION` is present and not treated as OPEN. | RMS §10.1, §27 |
| **C-064-05** | Each of the fourteen has an admission-rationale table covering all fourteen questions. | row 064 `Val` |
| **C-064-06** | Every rationale cell is answered from source, with question 13 applied under Artifact 057 §5.4. | RMS §13; C-057-01; Artifact 057 §5.4 |
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
| **C-064-32** | This contract's own changes are confined to `docs/models/registry/kinds.md`. | row 064 |
| **C-064-33** | Roadmap `Val` — *"exactly fourteen Kinds, each with admission rationale"* — is satisfied. | §28 |
| **C-064-34** | Roadmap `Done` — *"fourteen"* — is satisfied. | §28 |
| **C-064-35** | The fourteen Registry Kinds are not a universal Kind taxonomy, and no envelope field is added. | RMS §4 |
| **C-064-36** | A question-7 answer asserts a concrete reference only where a source establishes that reference relation. | §7 |
| **C-064-37** | Lockstep is not counted as reference evidence. | §7; Artifact 003 (`LS`) |
| **C-064-38** | A Roadmap `→` unlock is not counted as reference evidence. | §7 |
| **C-064-39** | Naming a declared Record Model is not treated as referencing its `MODEL-DEFINITION`. | §8; Artifact 063 §8.2 |
| **C-064-40** | RMS §13's question 13 is not rewritten; its Registry application is Artifact 057 §5.4's. | Artifact 057 §5.4 |
| **C-064-41** | The fourteen Registry `KIND-DEFINITION` partners are not claimed to exist before row 075 lands. | SC-064-D |
| **C-064-42** | This contract does not enlarge any 066–107 row's own `Val` or `Done`. | §27 |
| **C-064-43** | Non-roster rows carrying LS-1 metadata are not promoted into Registry Kinds. | SC-064-J |
| **C-064-44** | No answer rests on Blueprint §13.10 while it is flagged PROPOSED. | SC-064-K |
| **C-064-45** | Structural question coverage (196 rows) and source-resolved answers are reported separately and never merged into one count. | §6; §28 |
| **C-064-46** | Every question-13 cell names an existing Registry Kind it could reduce to and the source-established distinction that reduction would lose; none rests on roster membership alone. | Artifact 057 §5.4; C-057-17 |
| **C-064-47** | No question-13 source gap remains. | SC-064-I |
| **C-064-48** | The Registry's LS-1 self-hosting ordering is resolved by AD-LS1-R-BOOTSTRAP, and only for the Registry's own fourteen pairs. | Artifact 003; SC-064-D |
| **C-064-49** | A named downstream artifact — row 075, specified by row 074 — owns the fourteen Registry `KIND-DEFINITION` partner Records. | Roadmap rows 074, 075 |
| **C-064-50** | Exit-P3 and G-REG remain blocked until row 075 lands and row 123's lockstep tests pass. | Artifact 003; rows 123, 124 |

## 27. Downstream Handoff

| Artifact | May assume from 064 | Must still define |
|---|---|---|
| **065** governance (`H: 064`; row 064's `→` does not name it) | the frozen fourteen-Kind taxonomy | who may propose, approve, deprecate a definition |
| **066–107** definition-family rows | the exact fourteen-Kind taxonomy; the source-established responsibility boundary of the relevant Kind; Kind ≠ `KIND-DEFINITION`; the no-fifteenth-Kind rule; the lockstep constraints the Roadmap actually assigns each row | exactly the specification or schema responsibilities, `Val` and `Done` the Roadmap and governing sources assign each row. This contract adds no common checklist of fields, references, versions, cardinality or constraints. |
| **074–075** Registry self-Kind definition set | the fourteen Kinds of §6, in RMS order, as the subjects of the fourteen `KIND-DEFINITION` Records | the set contract (074) and the fourteen Records (075), per their own rows |
| **108–110** evolution | that Registry definitions share a governed change path and temporal account (F-4) | the evolution, versioning, supersession and deprecation model |
| **123–124** lockstep and P3 conformance | that the Registry's LS-1 partners are owed by row 075 | the lockstep proof and exit-P3, per their own rows |
| **459** extensibility | that the current Registry taxonomy is exactly fourteen | how a new Kind is added |

## 28. Roadmap Completion Trace

| Row 064 | Status | Where it is met |
|---|---|---|
| `Val`: *"exactly fourteen Kinds"* | **SATISFIED** | §6; C-064-01 to C-064-04 |
| `Val`: *"each with admission rationale"* | **SATISFIED** — 196 rationale cells represented and 196 answered from source; question 13 applied under Artifact 057 §5.4 | §8–§21; C-064-05, C-064-06, C-064-46, C-064-47 |
| `Done`: *"fourteen"* | **SATISFIED** | §6 |
| `H: 060,057` | **SATISFIED** — sovereignty and the admission test consumed unchanged | §2, §7, §22 |
| `LS: LS-1` | **SOURCE/DECOMPOSITION RESOLVED** — ordering by AD-LS1-R-BOOTSTRAP (Artifact 003, RMS §10.4); the concrete partners are owned by row 075 and are **not yet landed**; they are mandatory before exit-P3 and G-REG | §22; SC-064-D |
| `→ 066–107` | **SATISFIED** — handoff stated without enlarging any row | §27 |

No schema created. No Registry data created. No governance implemented. No future extension
ceremony defined. No fifteenth Kind admitted. The fourteen `KIND-DEFINITION` partners are owed by
row 075; this artifact does not claim they exist.

---

*Artifact 064 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This document
states the Registry Kind taxonomy from Record Model System §10.1 and §13, Master Blueprint §9.4,
§13.6 and §13.6e, and Roadmap row 064, with each Kind's admission rationale under Artifact 057. It
is not a Registry Record, holds no canonical data, defines no schema, field, validator or algorithm,
and implements nothing. Where it differs from the Master Blueprint, the Record Model System, or the
OS File Build Roadmap, those governing sources are correct and this document is wrong.*
