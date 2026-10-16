# COOLBOY12 — Registry Kind-Definition Set

**Artifact 075** · Registry Kind-Definition set · `docs/registry/registry_kinds/` · Own: **R** ·
RM: R · T: schema · R: CONTRACT · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning · CD: **yes** · Ph/St: P3/3b · Req: RR-16 · BP: §9.4 · RMS: §10.1 ·
H: 074,069 · S: — · LS: **LS-1** · G: — · → 114,123 · Val: exactly fourteen KIND-DEFINITIONs, one
per Registry Kind of 064; all conform to 069; names match the RMS §10.1 roster exactly; no extra
definition implies a fifteenth Kind; authored here as the canonicalization source of
`canon/registry/registry_kinds/`, committed only through 152 after G-CANON-R (§0.8) · Done:
fourteen · Why: **LS-1 partner — the Registry half of the Registry's own taxonomy
(AD-LS1-R-BOOTSTRAP, §0.7)** · Risk: HINGE · ∥: no

## 0. How to Read This File

**What this is.** The authored canonicalization source of the Registry's fourteen
`KIND-DEFINITION`s — the definition side of the Registry's own LS-1 pairs, 064 ↔ 075 (Roadmap
§0.7). Artifact 074 fixes the set; Artifact 069 fixes each member's structure; Artifact 064 bounds
each member's meaning. *"An authored source is not a Record and is not canon."* (Roadmap §0.8). No
member below is a committed Registry Record. Committed Registry Records are written to
`canon/registry/registry_kinds/` only through the Mutation Coordinator (row 152), the sole writer
of `canon/**`, after G-CANON-R.

**Packaging — an Artifact 075 local representation choice.** No source and no existing repository
convention fixes how this directory is packaged (074 SC-074-M). This artifact uses one file holding
all fourteen members, so that the set can be counted and compared in one place, plus the
directory's `PURPOSE.md`, which is non-member metadata. Neither the file name, the file count, nor
the order of members is architecture. The members appear in RMS §10.1 order for audit only; that
order is not identity, version, or a creation, load, commit or resolution order (074 RKS-074-21).

**Member blocks.** Each member is one fenced block from `MEMBER` to `END MEMBER`. The semantic
member count is the number of such blocks — exactly fourteen. Nothing outside a block is a member:
headings, tables, the source conditions and this section are non-member text.

**What 069 requires.** Artifact 069 (`docs/registry/kind_definition.schema`) defines ten elements of
*"a materialized Record"* (069 NOTATION, STATUS), each `REQUIRED yes` and `exactly-one` (069 §2,
§3):

```
ENVELOPE  partition · kind · object_id · slug · provenance · registry_ref · sot_class
FAMILY    subject_model · subject_kind · definition
```

069 itself defines no separate source representation. Its MATERIALIZATION boundary says row 075
authors the fourteen *"as canonicalization sources conforming to 069"* (069 §5).

**How a source conforms — Roadmap §0.8, *Source envelope* (AD-REG-SOURCE-ENVELOPE).** Roadmap
§0.8 (`docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`) carries two author decisions.
AD-REG-AUTHORING-SPLIT (audit trail CONFLICT-F) separates P3 authoring from canonical
materialization: an authored source is not a Record and is not canon, and row 152 alone commits
to `canon/**` after G-CANON-R. AD-REG-SOURCE-ENVELOPE (its *Source envelope* bullet, added by
author direction in commit `be6a2c1`) makes a canonicalization source a pre-Record
representation. It carries the **source-owned** elements — `partition`, `kind`,
`slug` and the family elements. The **commit-owned** elements — `object_id`, `provenance`,
`registry_ref`, `sot_class` — are absent and are assigned on the commit path when row 152 commits
the Record. Where a row requires its source to conform to a structural contract, *"the source
conforms when each source-owned element appears exactly once and is valid under that contract and
no commit-owned element appears"*. Full conformance of the committed Record is checked on the
commit path before the Human Gate. The audit trail is the Revolving Resolution Note, CONFLICT-G.

**Artifact 074 is synchronized with that rule.** 074 originally predated the amendment and
required the seven-field envelope on every member. It now applies 069 in two stages (074 §6
*Two stages, one contract*, §16 *Envelope*, RKS-074-05, C-074-06). The authored source carries
the source-owned elements and no commit-owned element. Every committed member carries all ten 069
elements, with no variant. The source envelope is not a second or relaxed schema (074 §6 *No
variant*). Both hard dependencies therefore agree with the source as authored here (SC-075-G).

**What each block carries.** The six source-owned elements, in 069's order: `partition`,
`kind`, `slug`, `subject_model`, `subject_kind`, `definition`. The four commit-owned elements are
absent under Roadmap §0.8.

**Element status.**

| Element | Representation here | Basis | Status under Roadmap §0.8 |
|---|---|---|---|
| `partition` | `R` | the committed `KIND-DEFINITION` Record this source is for belongs to the Registry partition (069 §2 `partition`; RMS §10.1) | CONFORMING |
| `kind` | `KIND-DEFINITION`, symbolic | 069 checks the Kind symbolically until row 117 binds codes (069 §2 `kind`, SC-069-C) | CONFORMING |
| `object_id` | absent | commit-owned (Roadmap §0.8): allocated by Artifact 036 on the commit path, never at authoring. 069 requires it of the committed Record (069 §2; C-069-09) | ABSENT AS REQUIRED |
| `slug` | the subject's name with `-` written `_` | source-owned (Roadmap §0.8). 069 §2 `slug`: *"decoration only; never identity"*, one value. Each value passes Artifact 035's slug rule; deriving it from `subject_kind` is an Artifact 075 representation choice | CONFORMING |
| `provenance` | absent | commit-owned (Roadmap §0.8): captured by the shared mechanism (047) at commit; 069 requires it of the committed Record | ABSENT AS REQUIRED |
| `registry_ref` | absent | commit-owned (Roadmap §0.8). 069 attaches no referent and Artifact 033 leaves it unresolved; §0.8 requires it fixed before 152 may commit | ABSENT AS REQUIRED |
| `sot_class` | absent | commit-owned (Roadmap §0.8). 069 fixes no value; §0.8 requires the record-level class fixed before 152 may commit | ABSENT AS REQUIRED |
| `subject_model` | `R` | every subject is a Registry Kind (074 RKS-074-04) | CONFORMING |
| `subject_kind` | one RMS §10.1 name | exact spelling; one per member (074 §8, §9) | CONFORMING |
| `definition` | authored here | the governed Kind-level meaning of the subject (069 §3), bounded by its 064 section | CONFORMING |

**No identity-bearing or commit-owned value is invented here.** No `object_id`, Registry Kind code,
provenance value, `registry_ref` referent or `sot_class` value appears, and no placeholder or
marker stands in for one. Each `slug` is derived from `subject_kind` and carries no identity
(069 §2; Artifact 034).

**069 conformance, as Roadmap §0.8 defines it for a source.** Every member carries each
source-owned element exactly once, valid under 069, and no commit-owned element. That is the
whole of what 075 claims. It is not evidence that any commit-owned value exists: the authored
source is not a committed Registry Record, no committed Record is claimed here, ten-element
conformance of each committed Record is checked on the commit path, and nothing here is written to
`canon/**`.

## 1. The Set

| RMS §10.1 | `subject_model` | `subject_kind` | Semantic source | Member |
|---|---|---|---|---|
| 1 | R | `MODEL-DEFINITION` | 064 §8 | §2.1 |
| 2 | R | `KIND-DEFINITION` | 064 §9 | §2.2 |
| 3 | R | `SUBTYPE-DEFINITION` | 064 §10 | §2.3 |
| 4 | R | `FIELD-DEFINITION` | 064 §11 | §2.4 |
| 5 | R | `SCHEMA-DEFINITION` | 064 §12 | §2.5 |
| 6 | R | `RELATIONSHIP-TYPE-DEFINITION` | 064 §13 | §2.6 |
| 7 | R | `CONTROLLED-VOCABULARY` | 064 §14 | §2.7 |
| 8 | R | `IDENTITY-GRAMMAR` | 064 §15 | §2.8 |
| 9 | R | `WSVR-INDICATOR-DEFINITION` | 064 §16 | §2.9 |
| 10 | R | `VALIDATION-RULE` | 064 §17 | §2.10 |
| 11 | R | `CONSTRAINT-DEFINITION` | 064 §18 | §2.11 |
| 12 | R | `CAPABILITY-DEFINITION` | 064 §19 | §2.12 |
| 13 | R | `DERIVATION-RULE` | 064 §20 | §2.13 |
| 14 | R | `SIMULATION-MODEL-DEFINITION` | 064 §21 | §2.14 |

Fourteen members; fourteen distinct subjects; the subject set equals the RMS §10.1 roster; every
`subject_model` is R; no subject appears twice; none is missing; none lies outside the roster
(074 §9). Declared status of every subject is established by RMS §10.1 and Artifact 064 §6, the
Registry's own Kind architecture (069 §6 decision case; 074 §6).

## 2. The Fourteen Members

Each `definition` answers one question for its subject Kind: **what is a Record of this Kind?**

### 2.1 MODEL-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           MODEL_DEFINITION
subject_model  R
subject_kind   MODEL-DEFINITION
definition     A Record of the Kind MODEL-DEFINITION is the Registry's governed definition of
               one declared Record Model: it states what that Record Model is, as the Registry
               defines it. Its subject is one of the six sovereign Record Models, named and not
               created by it. It carries governed meaning about the model and nothing else. It
               does not declare, create or admit a Record Model, and it neither grants nor holds
               the model's sovereignty, which is constitutional. The model's Kind taxonomy, its
               Records and their meaning stay with the model; what each of its Kinds means is a
               KIND-DEFINITION's, and any schema a SCHEMA-DEFINITION's. Defining a model never
               adds a seventh Record Model.
END MEMBER
```

### 2.2 KIND-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           KIND_DEFINITION
subject_model  R
subject_kind   KIND-DEFINITION
definition     A Record of the Kind KIND-DEFINITION is the Registry's governed definition of
               what one declared Kind means: it states what a Record of that Kind is — what
               holds of every Record of the Kind. Its subject is exactly one Kind already declared
               by exactly one Record Model's own taxonomy. It defines the Kind; it does not
               declare, admit or approve it, carry its admission rationale, or place it in a
               taxonomy. The owning model keeps its taxonomy, which Records of the Kind exist and
               what they mean in its domain. It is not the Kind, not the model's Kind
               specification and not the schema of the Kind's Records; it creates no Record of
               the Kind, and it carries no subtype, field, schema, relationship-type, vocabulary
               or model meaning. All of this holds unchanged when the subject Kind is
               KIND-DEFINITION itself.
END MEMBER
```

### 2.3 SUBTYPE-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           SUBTYPE_DEFINITION
subject_model  R
subject_kind   SUBTYPE-DEFINITION
definition     A Record of the Kind SUBTYPE-DEFINITION is the Registry's governed definition of
               one specialization of one declared Kind of one Record Model: it states what is
               true of that specialization, as a specialization of what is true of every Record
               of its Kind. A specialization is not a Kind: defining one creates no Kind,
               overrides nothing that holds of every Record of the parent Kind, and governs no
               value set. The owning model keeps the parent Kind, its Records and the domain
               semantics of the Records that use the specialization.
END MEMBER
```

### 2.4 FIELD-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           FIELD_DEFINITION
subject_model  R
subject_kind   FIELD-DEFINITION
definition     A Record of the Kind FIELD-DEFINITION is the Registry's governed definition of
               what one field means and the domain over which that meaning holds, stated once
               rather than restated per Record or per schema. It places the field in no schema
               and no Record, and it holds none of the field's type, default, cardinality,
               requiredness or order, which are the schema's; it carries no value set and is
               neither a condition nor a check. The owning model keeps its field architecture
               and the values its Records carry. A field name alone does not make one meaning
               shared across models.
END MEMBER
```

### 2.5 SCHEMA-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           SCHEMA_DEFINITION
subject_model  R
subject_kind   SCHEMA-DEFINITION
definition     A Record of the Kind SCHEMA-DEFINITION is the Registry's governed definition of a
               schema: it states the structure the schema defines — its required fields,
               cardinality, constraints, and applicable Model and Kind — composing field
               definitions, each of which keeps its own field's meaning. It is a definition, not
               an execution: the Registry does not execute schemas, and schema implementation is
               not Registry runtime. The Records that conform to a schema stay with their model.
END MEMBER
```

### 2.6 RELATIONSHIP-TYPE-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           RELATIONSHIP_TYPE_DEFINITION
subject_model  R
subject_kind   RELATIONSHIP-TYPE-DEFINITION
definition     A Record of the Kind RELATIONSHIP-TYPE-DEFINITION is the Registry's governed
               definition of one relationship type: it states what the type is, its participant
               roles, and which role owns it. It defines the type and is not a relationship
               instance, an edge or a Relationship Record, which is a World concept. It owns no
               relationship at runtime: each model decides whether it uses Relationship Records
               and owns the edges its own Records hold.
END MEMBER
```

### 2.7 CONTROLLED-VOCABULARY

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           CONTROLLED_VOCABULARY
subject_model  R
subject_kind   CONTROLLED-VOCABULARY
definition     A Record of the Kind CONTROLLED-VOCABULARY is a governed set of values or terms
               and the meaning of each, for the Kind it serves. Value sets are per Kind and may
               legitimately diverge; no vocabulary forms a forced union of values across Kinds,
               and none makes a universal status enumeration. The Registry governs what each
               value or term means; the owning model decides which value its Records carry. A
               vocabulary is governed value or term meaning, used where the owning contracts
               establish it; it is not itself a field or a domain Record.
END MEMBER
```

### 2.8 IDENTITY-GRAMMAR

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           IDENTITY_GRAMMAR
subject_model  R
subject_kind   IDENTITY-GRAMMAR
definition     A Record of the Kind IDENTITY-GRAMMAR is the recorded identity grammar: it states
               which grammar, partition roster and per-partition kind codes identity uses, so
               that the grammar is governed rather than hard-coded. It records the grammar and
               the kind-code mapping; it does not re-decide the grammar, which is constitutional,
               and it gives no kind code meaning: each model owns its Kind taxonomy and what its
               Kinds mean. This KIND-DEFINITION member itself records no identity grammar and
               binds no kind code.
END MEMBER
```

### 2.9 WSVR-INDICATOR-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           WSVR_INDICATOR_DEFINITION
subject_model  R
subject_kind   WSVR-INDICATOR-DEFINITION
definition     A Record of the Kind WSVR-INDICATOR-DEFINITION is the Registry's governed meaning
               of one world-state indicator: its type, unit, range, constraints and semantics. It
               holds meaning and never a value: World owns the indicator's current value, and the
               definition is not a field of the Record that carries that value. How the indicator
               behaves is a SIMULATION-MODEL-DEFINITION's, not this definition's. It creates no
               World state.
END MEMBER
```

### 2.10 VALIDATION-RULE

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           VALIDATION_RULE
subject_model  R
subject_kind   VALIDATION-RULE
definition     A Record of the Kind VALIDATION-RULE is the Registry's governed definition of a
               mechanism or procedure for checking a condition: it states how a condition is
               checked. It is not the condition it checks, which is a CONSTRAINT-DEFINITION's,
               and the two are never collapsed; it is not the runtime validation that implements
               the check, and each model keeps its own semantic validation. It is not a rule for
               what may be recomputed.
END MEMBER
```

### 2.11 CONSTRAINT-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           CONSTRAINT_DEFINITION
subject_model  R
subject_kind   CONSTRAINT-DEFINITION
definition     A Record of the Kind CONSTRAINT-DEFINITION is the Registry's governed definition of
               a condition that must hold: it states what must hold. It is not the mechanism that
               checks the condition, which is a VALIDATION-RULE's, nor any runtime validator that
               implements a check; the two Kinds are separate tiers and are never collapsed. A
               constitutional invariant stays at its own, constitutional tier.
END MEMBER
```

### 2.12 CAPABILITY-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           CAPABILITY_DEFINITION
subject_model  R
subject_kind   CAPABILITY-DEFINITION
definition     A Record of the Kind CAPABILITY-DEFINITION is the semantic contract of one
               capability: it states what that capability's contract is. It is not the
               capability's implementation, which is a runtime mechanism and not a Record, and it
               holds no runtime state and controls no runtime behaviour. Recording a capability's
               contract never makes the capability a Record Model or a Kind.
END MEMBER
```

### 2.13 DERIVATION-RULE

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           DERIVATION_RULE
subject_model  R
subject_kind   DERIVATION-RULE
definition     A Record of the Kind DERIVATION-RULE is the Registry's governed rule by which one
               derived state is computed: it states what may be recomputed and how. The rule is
               authoritative; what it computes is derived output, which is never authoritative
               and never becomes canon by being computed. A derivation rule is neither a
               condition that must hold nor a mechanism for checking one.
END MEMBER
```

### 2.14 SIMULATION-MODEL-DEFINITION

```
MEMBER
partition      R
kind           KIND-DEFINITION
slug           SIMULATION_MODEL_DEFINITION
subject_model  R
subject_kind   SIMULATION-MODEL-DEFINITION
definition     A Record of the Kind SIMULATION-MODEL-DEFINITION is the Registry's governed
               definition of a simulation model: it states how an indicator behaves — its
               dependencies, equations and thresholds. It defines behaviour only: what the
               indicator means is a WSVR-INDICATOR-DEFINITION's, and its values are World's. It
               creates no Simulation Record Model, and a simulation run is not a Registry Record.
END MEMBER
```

## 3. Set Rules Applied

- **The self-hosted member.** §2.2 is the one member whose `subject_kind` is `KIND-DEFINITION`.
  It is an ordinary member under the same 069 contract as the other thirteen: no special schema,
  no relaxed rule, no added element, and no prior `KIND-DEFINITION` Record is required. RMS §10.4:
  *"There is no circular self-definition requirement."* No axiom, bootstrap or meta member is
  added, and the Bootstrap Meta-Contract, which is not a Record, is not a member. RMS §10.4 does
  not identify which ordinary Registry Record is its first Registry Record; this artifact neither
  identifies nor excludes any member as first, and sets no creation, load, commit or resolution
  order (074 §11, §12).
- **No extra member.** No member concerns `SEMANTIC-DEFINITION`, `IDENTITY-DEFINITION`,
  `DERIVATION-DEFINITION`, `ROLE-BOUNDARY-DEFINITION`, `DEGRADED-MODE-DEFINITION`,
  `DIAGNOSTIC-VOCABULARY`, `SIGNAL-CLASS`, `READER-ARCHETYPE`, this set, a Blueprint alias, or a
  bootstrap Kind (074 §17). No member's definition implies a fifteenth Kind. How a Kind or a
  definition could later be added is row 459's.
- **No relations invented.** No member carries a reference list, a dependency, a version,
  supersession or deprecation element, or a lifecycle. Naming a subject Kind is a declaration
  reference and not a semantic dependency (074 SC-074-K; row 111); evolution is rows 108–110's
  (074 SC-074-L).
- **LS-1.** This set is the definition side of the Registry's fourteen LS-1 pairs, 064 ↔ 075. 074
  ↔ 075 and 068 ↔ 069 are not pairs. The pairing is an authoring obligation, not a reference, an
  admission or an ownership transfer, and it commits nothing. The ordering exception that let 064
  precede this set changes order only (Artifact 003).

## 4. Source Conditions

| ID | Condition | Treatment |
|---|---|---|
| **SC-075-A** | `Req: RR-16` — the requirement register is not in the source set (GAP-C). | The ID is carried exactly; no requirement text is stated or claimed met. |
| **SC-075-B** | Blueprint §13.6's ten-item roster and aliases against RMS §10.1's fourteen. | Closed at source: the RMS §10.1 names are used exactly; aliases are not subjects (074 SC-074-C, SC-074-G). |
| **SC-075-C** | Blueprint FG-V7-05 — Registry's own `KIND-DEF` without a prior one. | Closed by RMS §10.4: an ordinary self-hosted member; no axiom Record; no first-Record decision (074 SC-074-B). |
| **SC-075-D** | The withdrawn `SEMANTIC-DEFINITION` family. | No member; no catch-all; unmapped semantic material stays with its owning contract (Roadmap §0.7). |
| **SC-075-E** | Packaging of the directory. | Not established by any source (074 SC-074-M). One member file plus `PURPOSE.md` is an Artifact 075 local representation choice. |
| **SC-075-F** | Authored source against committed Record. | *"An authored source is not a Record and is not canon."* (Roadmap §0.8). Row 152 commits after G-CANON-R; nothing here is written to `canon/**`. |
| **SC-075-G** | Pre-canon envelope realization against required 069 values. **Source A:** row 075 `Val` *"all conform to 069"*. **Source B:** 069 defines ten elements of a materialized Record, each `REQUIRED yes`, `exactly-one` (069 §2, §3; C-069-09), and names row 075's sources as conforming (069 §5 MATERIALIZATION); it defines no deferred-value marker. **Source C:** 074 consumes 069 unchanged and, synchronized to Source D, requires the source-owned elements at authoring and all ten on the committed Record, with no variant (074 §6, §16; RKS-074-05; C-074-06). **Source D:** Roadmap §0.8 — AD-REG-AUTHORING-SPLIT (CONFLICT-F: an authored source is not a Record; row 152 sole writer after G-CANON-R) and AD-REG-SOURCE-ENVELOPE (*Source envelope*, audit trail CONFLICT-G: the four commit-owned elements are absent from a source, and a source conforms on its source-owned elements). **Resolution:** Source D governs the source; Source B governs the committed Record; Source C applies both, so the members satisfy 069 and 074 at the authoring stage. | Source-owned elements authored; `object_id`, `provenance`, `registry_ref`, `sot_class` absent as §0.8 requires; no value, marker or placeholder stands in for them. Open as preconditions on the commit, not on this source (§0.8): the `registry_ref` referent and the record-level `sot_class`. |
| **SC-075-H** | Set identity across Registry evolution. | Rows 108–110 own it; no version element and no future-count rule is set (074 SC-074-L). |
| **SC-075-I** | Whether Records of an L1 family's Kind depend on their Kind's `KIND-DEFINITION`. | Not decided; row 111 owns dependency rules; no dependency is encoded (074 SC-074-K). |
| **SC-075-J** | Support files against the member count. | `PURPOSE.md`, this file's headings, tables and sections are non-member text; the count is the number of `MEMBER` blocks. |

## 5. Conformance Conditions

| ID | Condition | Where |
|---|---|---|
| **C-075-01** | Exactly fourteen `MEMBER` blocks. | §2 |
| **C-075-02** | Exactly fourteen distinct `subject_kind` values. | §1, §2 |
| **C-075-03** | The subject set equals the RMS §10.1 / 064 roster exactly. | §1 |
| **C-075-04** | Every `subject_model` is R. | §2 |
| **C-075-05** | Every member's `kind` is `KIND-DEFINITION` and `partition` is R. | §2 |
| **C-075-06** | **069 conformance gate, under Roadmap §0.8 *Source envelope*.** Every member carries each source-owned 069 element (`partition`, `kind`, `slug`, `subject_model`, `subject_kind`, `definition`) exactly once, valid under 069, in 069's order, and no commit-owned element (`object_id`, `provenance`, `registry_ref`, `sot_class`). **PASS** — the rule is the Roadmap's (§0.8), and the check parses the fourteen blocks. Ten-element conformance of the committed Record is a later commit-path check and is not claimed here. This is also what 074 requires of an authored member (074 §6; C-074-06). | §0, §2; SC-075-G |
| **C-075-07** | No Registry Kind is missing. | §1 |
| **C-075-08** | No Registry Kind is duplicated. | §1 |
| **C-075-09** | No subject lies outside the roster. | §1, §3 |
| **C-075-10** | RMS names are used, not Blueprint aliases. | §2; SC-075-B |
| **C-075-11** | One ordinary self-hosted `KIND-DEFINITION` member exists. | §2.2, §3 |
| **C-075-12** | No bootstrap, axiom or meta member. | §3 |
| **C-075-13** | No `SEMANTIC-DEFINITION`. | §3; SC-075-D |
| **C-075-14** | No definition implies a fifteenth Kind. | §2, §3 |
| **C-075-15** | No write to `canon/**`. | §0; SC-075-F |
| **C-075-16** | The source lies under `docs/registry/registry_kinds/` only. | §0 |
| **C-075-17** | No Registry Kind code is invented. | §0; SC-075-G |
| **C-075-18** | No roster ordinal is used as identity or as an operational order. | §0 |
| **C-075-19** | This set is the LS-1 definition side of 064 ↔ 075. | §3 |
| **C-075-20** | No version, dependency, resolver or gate behaviour is implemented. | §3 |
| **C-075-21** | Support files are not counted; the member count is fourteen. | §0; SC-075-J |
| **C-075-22** | Every `definition` is non-empty, grounded in its subject's 064 section, and merges no other Kind's responsibility. | §1, §2 |
| **C-075-23** | Only files under `docs/registry/registry_kinds/` are created. | row 075 |

C-075-15, C-075-16 and C-075-23 are normative conditions on the repository. This text cannot
prove them; the evidence for each change is repository inspection (`git diff --name-only`,
`git status`).

## 6. Handoff

**To 114** (Registry kernel; `Val`: *"create/resolve/version a definition"*) and **123**
(Registry lockstep tests; `Val`: *"no unpaired lockstep member"*): a complete fourteen-member
authored set, one `KIND-DEFINITION` per Registry Kind, the 064 ↔ 075 pairing, the ordinary
self-hosted member, and the concrete definition bodies, conforming to 069 as Roadmap §0.8
defines it for a source and 074 §6 applies it. Both hard dependencies are satisfied (SC-075-G).
Commit-owned values arrive only with the committed Records. Nothing here implements the kernel,
resolution, the lockstep tests, row 124's G-REG, G-CANON-R or row 152, and neither row's `Val` or
`Done` is enlarged.

## 7. Roadmap Completion Trace

| Row 075 | Status | Where |
|---|---|---|
| `Val`: *"exactly fourteen KIND-DEFINITIONs, one per Registry Kind of 064"* | **SATISFIED** — fourteen `MEMBER` blocks, one-to-one with the 064 / RMS §10.1 roster; checked by counting blocks and comparing subjects | §1, §2 |
| `Val`: *"all conform to 069"* | **SATISFIED for the authored source** under Roadmap §0.8 *Source envelope*. Committed-Record conformance remains a mandatory commit-path check and is not claimed by Artifact 075 | §0; SC-075-G; C-075-06 |
| `Val`: *"names match the RMS §10.1 roster exactly"* | **SATISFIED** — compared against RMS §10.1 itself | §1 |
| `Val`: *"no extra definition implies a fifteenth Kind"* | **SATISFIED** | §3 |
| `Val`: canonicalization source, *"committed only through 152 after G-CANON-R"* | **SATISFIED** for authoring — authored source only; no write to `canon/**`, shown by repository inspection. The commit itself is row 152's, after G-CANON-R | §0; SC-075-F |
| `Done`: *"fourteen"* | **SATISFIED** | §2 |
| `H: 074,069` | **074: SATISFIED** — exact set, subjects, self-hosting and the authored-source application of 069, synchronized to Roadmap §0.8 (074 §6, §16; RKS-074-05). **069: SATISFIED at the authored-source stage** under Roadmap §0.8; committed-Record conformance is deferred to the commit path | §0–§2; SC-075-G |
| `LS: LS-1` | **SATISFIED** as authoring-cycle atomicity (Roadmap §0.8 *Lockstep*) — the fourteen definition-side partners of 064 ↔ 075 are authored | §3 |
| `→ 114,123` | **HANDED OFF** — both hard dependencies are satisfied and every `Val` clause above holds at the authoring stage | §6 |

**Overall authoring state: COMPLETE — handoff to 114 and 123 allowed.** The authored source is
complete and both hard dependencies are satisfied. This does not mean the fourteen are committed
or canonical. They become Registry Records only when row 152 commits them after G-CANON-R, once
the `registry_ref` referent and the record-level `sot_class` are fixed (Roadmap §0.8). Ten-element
069 conformance is checked then, on the commit path.

---

*Artifact 075 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. Authored canonicalization source, not committed Registry Records:
the fourteen are committed only through the Mutation Coordinator after G-CANON-R. Where this file
differs from the Master Blueprint, the Record Model System, the OS File Build Roadmap, or Artifacts
064, 069 and 074, those sources are correct and this file is wrong.*
