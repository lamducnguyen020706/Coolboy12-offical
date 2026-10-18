# COOLBOY12 — SCHEMA vs FIELD Boundary Note

**Artifact 078** · SCHEMA vs FIELD boundary note · `docs/registry/schema_field_boundary.md` ·
Own: R · RM: R · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning · CD: yes · Ph/St: P3/3b · Req: RR-17,RR-27 · BP: §9.4 ·
RMS: §10.1 · H: 076,072 · S: — · LS: LS-1 · G: — · → 108 · Val: definition resolves;
versionable; references only declared entities (063) · Done: overlap resolved — a schema
*composes* field definitions and owns cardinality/required/order; a field definition owns meaning
and domain · Why: **audit DG-03 closed here, not deferred** · Risk: medium · ∥: yes

## 1. Purpose

This note answers one question — **when a schema uses a governed field, which responsibilities
belong to the schema, which belong to the field's `FIELD-DEFINITION`, and how do the two work
together without either owning or redefining what is the other's?**

The question exists because RMS Appendix H records it as a future extension: *"Registry
SCHEMA-DEFINITION and FIELD-DEFINITION overlap at the edges (a schema is partly a set of field
definitions)"* — *"Future extension — resolve during Registry schema design; no architectural
contradiction"* (PC-3). Artifact 064 names the risk the overlap carries: carried inside schemas,
*"one field's meaning would be restated per schema and could diverge — the overlap PC-3 records
and row 078 resolves without merging the Kinds"* (064 §11 question 13). Row 078 states the result
to be reached — *"overlap resolved — a schema composes field definitions and owns
cardinality/required/order; a field definition owns meaning and domain"* — and why it is reached
here: *"audit DG-03 closed here, not deferred"*. Both hard dependencies hand the closure to this
row and do not preempt it: *"Artifact 078 owns final overlap closure. Artifact 076 does not preempt
it."* (076 §8) and *"Artifact 078 owns final overlap closure. Artifact 072 does not preempt it."*
(072 §11).

> **The schema/field ownership split is closed. A schema composes field definitions into the
> structure it defines and owns composition, requiredness, cardinality and order; a
> `FIELD-DEFINITION` owns meaning and domain. Current sources do not establish how a schema
> identifies the `FIELD-DEFINITION` that governs one of its occurrences, or how a field's domain is
> matched against a schema's applicability. Those questions are bounded here (§9.5, SC-078-D,
> SC-078-E) and do not reopen the split.**

```
FIELD-DEFINITION              governs what one field means, and the domain over which that
      │                       meaning holds (Artifact 072; row 078)
      │   governed field semantics
      ▼
SCHEMA-DEFINITION             composes fields into a structure: which fields occur, whether each
      │                       is required, how many values each carries, and any order the
      │                       schema makes meaningful (Artifact 076; row 078)
      │   defined structure and applicability
      ▼
Records of the applicable     carry the actual values; owned by their own Record Model
Record Model                  (Blueprint §13.6e; I-105)
```

The arrows show responsibility, not mechanism. None of them is a Registry Record reference, a
dependency-graph edge, a runtime call or a mandatory representation (§7.4, §7.5).

## 2. Status and Roadmap Identity

Row 078 of the repaired Roadmap, reproduced field by field:

| Field | Exact value |
|---|---|
| ID | 078 |
| Name | SCHEMA vs FIELD boundary note |
| Path | `docs/registry/schema_field_boundary.md` |
| Own | R |
| RM | R |
| T | doc |
| R | CONTRACT |
| SoT | AUTHORITATIVE |
| Auth | defining |
| Canon | canonical-about-meaning |
| CD | yes |
| Ph/St | P3/3b |
| Req | RR-17,RR-27 |
| BP | §9.4 |
| RMS | §10.1 |
| H | 076,072 |
| S | — |
| LS | LS-1 |
| G | — |
| → | 108 |
| Val | definition resolves; versionable; references only declared entities (063) |
| Done | overlap resolved — a schema *composes* field definitions and owns cardinality/required/order; a field definition owns meaning and domain |
| Why | **audit DG-03 closed here, not deferred** |
| Risk | medium |
| ∥ | yes |

This document is the AUTHORITATIVE boundary contract between the `SCHEMA-DEFINITION` and
`FIELD-DEFINITION` definition families, under the Record System. `Auth: defining` means it defines
that boundary. It is:

- **not a Record.** It carries no envelope, no `object_id`, no provenance value and no
  `registry_ref`. No `SCHEMA-DEFINITION` or `FIELD-DEFINITION` Record is created by it.
- **not a schema and not a structural contract.** It creates no `.schema` file and changes neither
  Artifact 073 nor Artifact 077.
- **not a family specification.** Each family is specified by its own row — 076 and 072. This note
  closes the edge between them and redesigns neither.
- **not an implementation.** It defines no validator, schema engine, resolver, lookup, binder,
  parser, API or service, and performs no check and no mutation.
- **not a canonicalization source.** Roadmap §0.8 names the canonicalization sources — rows 075,
  085, 105, 106, 107 — and row 078 is not one of them.
- **not canonical data.** It lies outside `canon/**`. Registry Records are committed only through
  the Mutation Coordinator (row 152), after G-CANON-R (Roadmap §0.8).

Row 078's `Canon: canonical-about-meaning` and `CD: yes` are preserved exactly; how they sit beside
Artifact 003's docs-specification convention is recorded, not resolved (SC-078-P). `Req:
RR-17,RR-27` is carried exactly; the requirement text is not available (SC-078-Q).

**Evidence classes.** Statements that matter are labelled:

| Class | Meaning |
|---|---|
| **SOURCE FACT** | stated by the Blueprint, the RMS, the Roadmap or a frozen upstream artifact |
| **REQUIRED SYNTHESIS** | a conclusion that several source facts force together; not a quotation |
| **078 CLOSURE** | a normative statement inside the schema/field overlap that row 078 assigns to this artifact |
| **SOURCE GAP** | not decided by current sources, and not filled here |

**Boundary statuses** (§13.1): **CLOSED BY SOURCE** — a governing source already settles it;
**CLOSED BY 078** — this note closes it inside its assigned overlap; **SOURCE GAP** — undecided;
**DEFERRED TO NAMED OWNER** — a Roadmap row owns the mechanism or decision.

Where this document differs from the Master Blueprint, the Record Model System or the OS File Build
Roadmap, those sources are correct and this document is wrong.

## 3. Scope and Non-Goals

**Artifact 078 owns** the boundary between schema structure and field semantics:

- the ownership of composition, requiredness, cardinality and order on the schema side, and of
  meaning and domain on the field side (§6, §8, §9);
- what it means for a schema to compose a field, in which direction, and what composition does not
  transfer (§7);
- the separation of field domain from schema applicability, as far as current sources establish it
  (§9.3–§9.5);
- how the adjacent responsibilities — types and defaults, controlled vocabularies, constraints and
  validation — stand against the split (§10);
- how the split preserves the universal envelope, model sovereignty and row 078's `Val` (§11);
- the boundary rules (§12), matrices (§13), examples (§14), prohibited inferences (§15), source
  conditions (§16), the DG-03 closure certificate (§17), conformance conditions (§18) and the
  handoff to 108 (§19).

**Artifact 078 does not own, and does not pre-build:**

| Not decided here | Owner |
|---|---|
| the `SCHEMA-DEFINITION` family; its structural representation | 076; 077 |
| the `FIELD-DEFINITION` family; its structural representation | 072; 073 |
| the Registry Kind taxonomy and the admission of any Kind | 064 (RMS §10.1); 057; new Kinds 459 |
| the `CONTROLLED-VOCABULARY` family and its schema | 081; 082 |
| `CONSTRAINT-DEFINITION`; `VALIDATION-RULE` | 088–089; 090–091 |
| definition evolution; versioning and pinning; supersession and deprecation | 108; 109; 110 |
| who may propose, approve or deprecate a definition | 065 |
| Registry dependency direction, asymmetry and cycles | 111 |
| the Registry reference validator; the constraint/validation binder | 112; 113 |
| create/resolve/version operations; consumer resolution by id+version | 114; 115 |
| the Registry validation suite; lockstep tests; P3 conformance | 116; 123; 124 |
| the canonical gates; the sole canonical writer | 145; 152 |
| each model's field architecture and field domains | 179 (W), 274 (E), 301 (P), 355 (V), 366 (I) |
| each model's own schemas | that model's rows (e.g. 184 for World `CHARACTER`) |
| the universal envelope and the role of each of its seven fields | RMS §4, §5; Artifact 033 |
| how a new Kind, field or definition is added | 459 |

**Non-goals.** This note invents no field-reference carrier, no field-definition lookup, no
field-name grammar, no domain/applicability matching rule, no order syntax or position element, no
type or default element, no vocabulary relation, no applicability cardinality, no version
mechanism, no dependency edge, no new Kind and no validator. Where a source is silent, the silence
is recorded (§16).

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS          architecture; RMS v1.0 closes stale Blueprint wording where stated
        ↓
Roadmap (REPAIRED)              decomposition, metadata, Val, Done; §0.7 and §0.8 author rulings
        ↓
Artifacts 076 and 072 (H)       the schema side and the field side, consumed unchanged
        ↓
Artifact 078                    the closed boundary between them
```

| Source | What it gives this note | Role |
|---|---|---|
| Roadmap row 078 | identity, `Val`, `Done`, `Why`, `H: 076,072`, `LS: LS-1`, `G: —`, `→ 108` | build authority |
| **Artifact 076** (`docs/registry/schema_definition.md`) | the schema side: §7, §8, SD-1–SD-14, RF-076-1–RF-076-11, RS-076, VS-076, §21 | **hard dependency** |
| **Artifact 072** (`docs/registry/field_definition.md`) | the field side: §7–§12, FD-1–FD-22, RF-072-1–RF-072-9, RS-072, VS-072, §29 | **hard dependency** |
| RMS §4; §5; §6.1; §14 | the seven-field envelope and nine prohibitions; the identity grammar; *"Governs; never instantiates"*; the three field tiers | constitutional |
| RMS §10.1; §10.2; §10.3; §10.6; §20; Appendix H PC-3 | fourteen Kinds; the schema boundary; the reference boundary; constraint vs validation; the validation tiers; the overlap | constitutional |
| Blueprint §9.4; §12.6; §13.6e; §13.7; §13.7a; §26.3b | schema structure vs shared meaning; external engines redefine no authority; definition vs ownership; schema custody; shared mechanism ≠ shared semantic; DERIVED verdicts | constitutional |
| Roadmap §0.7; §0.8; PART III; PART VIII; rows 108–116, 123, 124, 152, 179, 184 | self-hosting; authoring vs canonical materialization; LS-1 and LS-2; the decision gates; downstream owners | build authority |
| Artifacts 061, 062, 063, 064 | authority table; layers and D-9; the reference boundary; the Kind admission answers | constraint, not `H` |
| Artifacts 073, 077 | the current structural carriers of each family | supporting context, not `H` |
| Artifacts 003, 033, 052 | conventions; the envelope; Registry canonicality | context, not `H` |

**Precedence.** Blueprint and RMS govern; where earlier Blueprint wording and a later explicit RMS
correction differ, the correction governs (SC-078-A). The Roadmap governs decomposition and order.
Artifacts 076 and 072 govern their own families and are consumed unchanged. Reading a supporting
source does not promote it into `H`: 073 and 077 are read so that this note contradicts neither,
and their notation is not treated as semantic law here.

Citations are to the repository copies in `docs/sources/`: the Blueprint is
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md`, the RMS `COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`, the
Roadmap `COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`.

## 5. Source-Established Responsibilities

### 5.1 The schema side — Artifact 076 (`H`)

| 076 | Inherited obligation | Used at |
|---|---|---|
| §8 | *"Composing a field into a schema leaves that field's FIELD-DEFINITION the sole holder of its meaning and domain, and a schema definition does not redefine, narrow or restate field meaning by containing the field."* | §7.3; SF-078-03 |
| §8 table | the minimum split: meaning and domain `FIELD-DEFINITION`'s; which fields occur, requiredness and cardinality `SCHEMA-DEFINITION`'s; order *"schema side, by row 078's closure"*; type and default schema-side; applicability `SCHEMA-DEFINITION`'s; enforcement neither's | §6 |
| §7 | order: *"whether and how order is carried — 078 closes it, 077 encodes it"* | §8.3 |
| SD-3 | structure, not field meaning | SF-078-03 |
| SD-4; RF-076-1 | applicability names declared Models and Kinds; no applicability cardinality | §9.3; SC-078-I |
| SD-5 | fields, requiredness and cardinality as structure; composition respects meaning and domain | SF-078-05, SF-078-06 |
| SD-6; SD-7 | constraints, validation references and relationships kept apart and executing nothing | §10.3 |
| SD-8; SD-9 | no execution; no ownership transfer | SF-078-13, SF-078-14 |
| SD-11; SD-12 | no new Kind; no universal semantic schema | SF-078-19 |
| SD-13; RF-076-2 | every reference carried is legal under 063; no field-reference carrier is mandated | §7.4; SF-078-11, SF-078-12 |
| SD-14 | *"may define"* is a permission, not a required element | §6 |
| RF-076-11 | reference ≠ dependency | §7.5 |
| RS-076-1, RS-076-2; VS-076-1 | independent R Record identity; versionable under 108–110 | §11.3, §11.4 |
| SC-076-D | the overlap, *"including how a field's domain relates to a schema's applicability"*, deferred to 078 | §9; SC-078-D |
| §21 | *"078 receives the schema side of the split (§8); 072 supplies the field side; 078 closes the overlap."* | this note |

### 5.2 The field side — Artifact 072 (`H`)

| 072 | Inherited obligation | Used at |
|---|---|---|
| FD-1; FD-2 | one field semantic per definition; the definition governs what the field means | SF-078-08 |
| FD-3; FD-4; §8 | the definition carries its domain — *"at least its scope at one field tier"*; three tiers only | SF-078-09 |
| §8 | *"Domain is not the schema's applicability."*; their relation is unstated | SF-078-10 |
| FD-6; FD-7 | universal envelope closed; `tier` and `status` World-owned | §11.1 |
| FD-8 | *"A definition does not cause its field to appear in any Record schema or Record."* | SF-078-04 |
| FD-9 | *"The family owns no schema composition, cardinality, requiredness, order, type or default."* | SF-078-05–SF-078-07, SF-078-16 |
| §10 | *"A schema that carries the field conforms to the field's definition; the definition does not conform to, compose or execute the schema."* | SF-078-02 |
| FD-10; FD-11; §12 | definition ≠ vocabulary; per-Kind divergence; no invented relation | SF-078-17 |
| FD-12; FD-13 | definition ≠ constraint; definition ≠ validator | SF-078-18 |
| FD-14 | Registry governs the definition; each model owns its Records, values and field architecture | SF-078-13 |
| RF-072-1; RF-072-2; RF-072-9 | domain names only declared entities; no declared-field category; reference ≠ dependency | §7.4, §11.5 |
| RS-072-1, RS-072-5; VS-072-1 | independent identity; no field-name lookup defined; versionable | §11.3, §11.4 |
| SC-072-E | type and default schema-side; the overlap deferred to 078 | §10.1 |
| SC-072-G | what *domain* covers and its relation to applicability — a source gap passed as input | §9.5; SC-078-D, SC-078-N |
| SC-072-H | the field/vocabulary relation is a source gap | SC-078-H |
| §29 | 078 takes the field side; *"Type and default are not handed to 078 as open ownership questions"*; the domain/applicability relation *"is passed as input, not as a new exit criterion"* | §9.5, §10.1 |

### 5.3 Supporting context — not hard dependencies

- **Artifact 064.** §12 question 8: *"a schema composes fields and owns cardinality, requiredness
  and order; it is not one field"*; §11 question 13 places the overlap with row 078, *"without
  merging the Kinds"*.
- **Artifacts 062 and 063.** D-9 separates a declaration reference from a semantic dependency;
  063 §7 and RB-1 to RB-6 bound every Registry reference.
- **Artifact 073.** A `FIELD-DEFINITION` Record carries its subject, its domain and its meaning
  through the carriers `subject_field`, `domain_tier`, `domain_model`, `domain_kind` and
  `definition`. They are 073's structural choices, not envelope fields, and this note redefines
  none of them.
- **Artifact 077.** A `SCHEMA-DEFINITION` Record carries `applicability`, `occurrence` and
  `definition`; each occurrence names a field (`occurrence.field`) and states
  `occurrence.required` and `occurrence.cardinality`. 077 names fields by name — a 077 CHOICE — and
  mandates no Registry Record reference. Its SC-077-D passes two questions to this row: which
  `FIELD-DEFINITION` governs a named field within a schema's scope, and whether field order is
  significant. Both are answered at §8.3 and §9.5.

### 5.4 What the two hard dependencies leave to 078

1. closing PC-3's edge, without merging the Kinds (076 §8; 072 §11; 064 §11 question 13);
2. what *compose* means and in which direction it runs (row 078 `Done`; 072 §10);
3. order — *"078 closes it, 077 encodes it"* (076 §7);
4. the domain/applicability relation — as input, not as a new exit criterion (072 §29; SC-076-D).

Artifacts 076 and 072 are consumed unchanged. No rule of either is reopened, narrowed or extended.

## 6. The Closed Ownership Matrix

**Schema side.** Blueprint §9.4 allocates structure to schema as such: *"Schema defines the
structure of a record — fields, types, required-ness, defaults."* RMS §10.2 makes the definition of
a schema a Registry Record. The Roadmap also carries model-owned schema artifacts, such as row 184's
*CHARACTER schema*; whether one is described by, declared through or independent of a
`SCHEMA-DEFINITION` Record is not established (SC-076-I; SC-078-L). The allocation below holds
against `FIELD-DEFINITION` either way, and this note changes no model's schema custody.

| Concern | Schema side (`SCHEMA-DEFINITION`) | Field side (`FIELD-DEFINITION`) | Basis | Status |
|---|---|---|---|---|
| Field meaning | does not own; respects it | **owns** | Blueprint §9.4; row 078; 072 FD-2; 076 §8 | CLOSED BY SOURCE |
| Field domain | does not own; does not expand it | **owns** | row 078; 072 FD-3, §8; §9.4 here | CLOSED BY SOURCE; non-expansion CLOSED BY 078 |
| Field occurrence — composition | **owns** which fields occur in the structure it defines | does not create an occurrence | Blueprint §9.4; RMS §10.2; row 078; 072 FD-8 | CLOSED BY SOURCE; direction CLOSED BY 078 |
| Requiredness | **owns** whether an occurrence is required | does not own | Blueprint §9.4; RMS §10.2; row 078; 072 FD-9 | CLOSED BY SOURCE |
| Cardinality | **owns** how many values an occurrence may carry | does not own | RMS §10.2; row 078; 072 FD-9 | CLOSED BY SOURCE |
| Order | **owns**, where the schema makes order meaningful | does not own | row 078; 064 §12 Q8; 072 FD-9 | CLOSED BY SOURCE; scope CLOSED BY 078 |
| Type | schema-side under Blueprint §9.4; carriage in a `SCHEMA-DEFINITION` not established | does not own | Blueprint §9.4; 072 FD-9; SC-076-K | CLOSED BY SOURCE; carriage SOURCE GAP |
| Default | schema-side under Blueprint §9.4; carriage in a `SCHEMA-DEFINITION` not established | does not own | Blueprint §9.4; 072 FD-9; SC-076-K | CLOSED BY SOURCE; carriage SOURCE GAP |
| Applicable Model and Kind | **owns** the scope the schema applies to | does not own (its domain is a different concept) | RMS §10.2; 076 SD-4; 072 §8 | CLOSED BY SOURCE |
| Actual Record values | does not own | does not own | Blueprint §13.6e; 061 §7 row 2 | owned by the Record's own model |
| The domain Records themselves | does not own | does not own | Blueprint §13.6e; I-105; 076 SD-9; 072 FD-14 | owned by the Record's own model |
| Runtime validation | does not execute | does not execute | RMS §10.2, §10.6, §20; 076 §9; 072 FD-13 | shared implementation validation |

**Definition ownership is not Record ownership.** Every row above allocates a responsibility
between two kinds of Registry definition. None of them makes the Registry owner of a domain Record,
a value, a model's field architecture or a model-owned schema (§11.2).

**Allocation is not a mandatory element.** That the schema side owns a concern does not make it a
required element of every `SCHEMA-DEFINITION` Record: RMS §10.2's *"may define"* is a permission
(076 SD-14), and how each concern is carried is 077's.

## 7. Composition Contract

### 7.1 What composition is

**078 CLOSURE**, from row 078 `Done`, Blueprint §9.4 and 076 §7–§8. *To compose a field* is for a
schema to state, as part of the structure it defines, that the field occurs in the Records the
schema applies to, and, for that occurrence, whether it is required, how many values it may carry
and, where the schema makes order meaningful, where it stands. What the field means, and over what
domain, the schema does not state: those are the governing `FIELD-DEFINITION`'s. A *field
occurrence* is that structural presence — *"the field present in a schema or Record — structure"*
(072 §28).

For a schema applicable to the declared World Kind `CHARACTER`, conceptually:

1. the schema identifies a field occurrence in the structure it defines;
2. the field's meaning and domain are those its governing `FIELD-DEFINITION` holds;
3. the schema states whether the occurrence is required;
4. the schema states how many values the occurrence may carry;
5. the schema states any order it makes meaningful;
6. a Character Record carries a value under World's ownership;
7. no step changes what the field means, or the domain over which that meaning holds;
8. no step gives the Registry ownership of the Character Record or its value.

This is an account of responsibilities, not a procedure. Nothing here looks up a definition,
resolves a reference, applies a schema or checks a Record.

### 7.2 Direction

**SOURCE FACT.** Row 078: *"a schema composes field definitions"*. 072 §10: *"A schema that
carries the field conforms to the field's definition; the definition does not conform to, compose
or execute the schema."* 072 FD-8: *"A definition does not cause its field to appear in any Record
schema or Record."*

**078 CLOSURE**, on those facts. Composition runs one way: from the schema, over governed fields.
A `FIELD-DEFINITION` composes no schema, produces no occurrence, and prescribes no occurrence in
any schema — every schema that could use its meaning included. A field can be defined before any
schema uses it, and its definition places it in none (072 §7).

### 7.3 Composition is not embedding

PC-3's parenthesis — *"a schema is partly a set of field definitions"* — describes the edge, not
the architecture. **078 CLOSURE:** a schema is a structure of field occurrences, each of whose
meaning and domain is held by a `FIELD-DEFINITION`. It is not a set of `FIELD-DEFINITION` Records,
contains no such Record or its content, and is not *"a collection that replaces field meaning"*
(076 §6).

| | Composition | Embedding — not permitted |
|---|---|---|
| what the schema states about the field | that it occurs, its requiredness, its cardinality, any meaningful order | what the field means, or the domain over which it means it |
| where the field's meaning is held | in its `FIELD-DEFINITION` only | in the schema as well, as a second authoritative account |
| many schemas composing one field | many structural contexts, one meaning | one meaning per schema, free to diverge — the risk 064 §11 question 13 names |

A schema states no field meaning: it does not define, redefine, narrow or restate it (076 §8). Text
in a schema definition that purports to say what a composed field means carries no authority as
field meaning; where it contradicts the governing definition, the composition is not legal (§14
Example B). Respecting a field's governed meaning (RF-076-2) is an obligation on the schema; it
gives the `FIELD-DEFINITION` no structural authority. Whether a particular structure respects a
particular meaning is judged against the governing definition, outside both Records — 077 marks
the check EXTERNAL (O-08) — and this note defines no test for it.

### 7.4 Composition is not a reference representation

**SOURCE FACT.** 076 RF-076-2: *"A field occurrence is a structural element of the schema; it is
not thereby a concrete Record reference, and no source fixes how a schema identifies its fields."*
Where a schema definition does carry a concrete reference to a field, RMS §10.3 has no
declared-field category, and 063 §7 says such targets *"are reached as Registry definitions (row
1)"*: the reference is an R → R reference to a `FIELD-DEFINITION` Record and must satisfy Artifact
063, including RB-1 and RB-6.

Composition is a semantic relation between a schema's structure and a field's governed meaning. Its
representation is not fixed here:

- **no carrier is mandated.** A field occurrence does not need a direct `FIELD-DEFINITION` Record
  identifier, and this note adds none to 073 or 077;
- **a name is not an identifier.** A field name is not a Registry Record identifier, and no
  universal field-name grammar exists (SC-078-E);
- **077's form is current, not constitutional.** 077 names the field by name (`occurrence.field`),
  a 077 CHOICE following 073's `subject_field`. That is the current structural representation of
  `SCHEMA-DEFINITION` Records; it is not the only representation the constitution permits, and
  this note neither requires nor forbids a governed change of it;
- **absence of a carrier is not absence of meaning.** The governed meaning of a composed field
  stands whether or not its occurrence carries a reference.

### 7.5 Composition is not a dependency edge

**SOURCE FACT.** Artifact 062 D-9: *"A declaration reference that RMS §10.3 permits and Artifact
063 bounds — for example a Registry definition naming a declared Kind — does not, by itself,
establish a semantic dependency."* Artifact 063 RB-5: *"A reference that is not a semantic
dependency is not made subject to 111 merely because it is a reference."* 076 RF-076-11 applies
both to schema definitions. `SCHEMA-DEFINITION`'s layer placement is not established (062 §6;
SC-076-L).

Composing a field, and any reference that represents it, is not by itself a dependency-graph edge.
No schema-to-field dependency edge, layer placement or cycle exception is created here. Where a
concrete relation is also established as a semantic dependency, row 111's direction, asymmetry and
cycle rules apply to it.

### 7.6 Composition-effect matrix

| When a governed field is composed into a schema … | Answer | Basis |
|---|---|---|
| does its meaning change? | **No** | 076 §8; SF-078-03 |
| does its domain expand to the schema's applicability? | **No** | §9.4; SF-078-09 |
| does the `FIELD-DEFINITION` begin to own the schema? | **No** | 072 §10; SF-078-02 |
| does the `SCHEMA-DEFINITION` own the domain Records? | **No** | 076 SD-9; SF-078-13 |
| can the schema state the occurrence? | **Yes**, within the constitution and the model's field architecture | Blueprint §9.4; RMS §10.2; SF-078-02 |
| can the schema state requiredness? | **Yes**, within the same limits — an envelope field cannot be made optional | SF-078-05, SF-078-15 |
| can the schema state cardinality? | **Yes**, within the same limits — an envelope field carries exactly one value | SF-078-06, SF-078-15 |
| can the schema state meaningful ordering? | **The schema side owns that concern**; no schema is required to have one | SF-078-07 |
| does composition create an R → R Record reference? | **Not established** — none is required; any carried obeys 063 | RF-076-2; SF-078-11 |
| does composition create a semantic dependency? | **Not by itself** | 062 D-9; SF-078-12 |
| does composition run a validator? | **No** | RMS §10.2; SF-078-14 |
| does composition admit a Kind, or create one? | **No** | RMS §10.1; SF-078-19 |

## 8. Cardinality, Requiredness and Order

### 8.1 Requiredness — schema side

**SOURCE FACT.** Blueprint §9.4 places *"required-ness"* in schema structure; RMS §10.2 lets a
`SCHEMA-DEFINITION` define *"required fields"*; row 078 places *"required"* with the schema; 072
FD-9 gives the field side none.

Requiredness is a property of an occurrence in one schema: whether the field must occur in the
structure that schema defines. A `FIELD-DEFINITION` does not make its field mandatory in every
schema that could use its meaning, or in any. Two schemas composing the same governed field may
state different requiredness; that produces no second meaning. The schema's statement is bounded by
the constitution — a universal envelope field cannot be made optional (§8.4) — and by the model:
*"Which Records carry the field is decided by the model's field architecture and schemas."* (072
§10).

### 8.2 Cardinality — schema side

**SOURCE FACT.** RMS §10.2 lists *"cardinality"*; row 078 gives it to the schema; 076 §7 reads it
as *"how many values a field occurrence may carry in the structure"*; 072 FD-9 gives the field side
none.

Value cardinality is a property of an occurrence in one schema. A `FIELD-DEFINITION` sets no
cardinality for its field across schemas. Two schemas may state different cardinalities for one
governed field where the governing architecture permits it; the difference describes structural
participation, not meaning. Artifact 077's `L..U` notation is a 077 representation choice. It is
not a constitutional field type and not a requirement on any model's schemas.

### 8.3 Order — schema side

**SOURCE FACT.** Row 078 gives *"order"* to the schema; 064 §12 question 8 agrees (*"owns
cardinality, requiredness and order"*); 076 §7 hands the closure here (*"078 closes it, 077 encodes
it"*); 072 FD-9 gives the field side none.

**078 CLOSURE.**

1. Field order is a schema-side concern, and only a schema-side concern.
2. It is a concern only where a schema makes order meaningful in the structure it defines.
3. No `FIELD-DEFINITION` states a position or an order for its field, in any schema.
4. No schema is required to be order-sensitive.
5. A sequence in a representation is not, by itself, a semantic order. 077: *"The sequence in which
   occurrences are written carries no meaning defined here."* This note gives it none either.
6. No order syntax, position element or ordering algorithm is defined here. How a significant order
   would be encoded in a `SCHEMA-DEFINITION` Record is 077's (*"077 encodes it"*).

Two inferences are rejected: that because order is schema-owned every schema must declare an
order (PI-23), and that because a representation is a list its sequence is a semantic order
(PI-24).

**SOURCE GAP.** No source names a case in which field order is significant, or a criterion for
when it is (SC-078-F). That leaves the ownership closed and the conditions unstated; it is not a
deferral of ownership. **Answer to SC-077-D, on order:** ownership is closed on the schema side;
this closure requires no change to Artifact 077, since it makes no schema order-sensitive and fixes
no syntax; whether 077 should later encode significant order is 077's, through its own governed
change.

### 8.4 The universal envelope

**SOURCE FACT.** The envelope is *"the bootstrap set and no more"* (RMS §4): `partition` · `kind` ·
`object_id` · `slug` · `provenance` · `registry_ref` · `sot_class`. *"An envelope field binds every
Record in every model."* (Artifact 033). The Registry structural contracts give each of the seven
the cardinality exactly-one — 077 §2, as Artifacts 067, 069, 071 and 073 do — and 077 states the
consequence: the *"envelope carries each of its seven fields exactly once"*.

**REQUIRED SYNTHESIS.** Where a schema describes the occurrence of an envelope field, it cannot
contradict that obligation: it cannot make the field optional, give it any count but one, or
change its universal role — *"slug is decoration only"* (RMS §5) stays true in every schema. 077
expresses this for a listed envelope field as `occurrence.required` yes and
`occurrence.cardinality` 1..1 (077 O-07). That is 077's representation of an envelope constraint,
cited as an example of a higher governing constraint, not a rule this note adds. Whether a schema
lists the envelope fields at all is not established (SC-077-M; SC-078-K), and this note requires no
schema to enumerate them.

## 9. Meaning and Domain

### 9.1 Meaning — field side

**SOURCE FACT.** Blueprint §9.4: *"The Registry defines the shared meaning those fields carry
across kinds. A field's existence is schema; what "status" means everywhere it appears is
Registry."* Row 078: *"a field definition owns meaning"*. 072 FD-2: the definition governs what the
field means.

A `FIELD-DEFINITION` is authoritative for what its field means within its domain. Meaning is not
the value a Record carries (Blueprint §13.6e: *"The values its Records carry"* are the model's), not
the field's presence (that is schema), and not a value set (§10.2). One definition governs one field
semantic; a shared field name alone does not establish one semantic across models (072 §7; I-103).
No schema holds field meaning, whether or not it composes the field.

### 9.2 Domain — field side

**SOURCE FACT.** Row 078: a field definition *"owns meaning and domain"*. 072 §8: a domain is
*"at least the scope over which its meaning holds, placed at one of RMS §14's three tiers"* — RMS
§14: *"Three tiers: universal (the bootstrap set, seven fields) · model · Kind."*

The domain is the field side's. A schema neither sets, narrows nor widens it. Two questions about
domain lie outside this overlap and stay as Artifact 072 left them: whether *domain* carries any
further value-domain concept beyond scope (SC-072-G; SC-078-N), and how domain is shared between a
`FIELD-DEFINITION` and the model field architecture that delivers *"field domains"* in LS-2
lockstep (072 §8, a reading; SC-078-N).

### 9.3 Domain is not applicability

**SOURCE FACT.** 072 §8: *"Domain is not the schema's applicability."* RMS §10.2 gives a schema
definition its *"applicable Model · applicable Kind"*.

| | Field domain | Schema applicability |
|---|---|---|
| what it scopes | where one field's governed meaning holds | which Records one schema's structure applies to |
| owner | the `FIELD-DEFINITION` | the `SCHEMA-DEFINITION` |
| form | at least a scope at one of RMS §14's three tiers (072 §8) | declared Models and Kinds; count and presence not established (076 SD-4; SC-076-N) |
| current carriers (context) | 073 `domain_tier`, `domain_model`, `domain_kind` | 077 `applicability`, `applicability.model`, `applicability.kind` |
| what it decides about the other | nothing | nothing |

The two concepts are related, because a schema composes fields whose meanings hold over some domain,
but they are not one concept, and neither is derived from the other.

### 9.4 Composition does not expand a domain

**REQUIRED SYNTHESIS**, from 072 §8 (a domain is the scope over which a meaning holds), 072 FD-3,
076 §8 (a schema does not redefine, narrow or restate field meaning) and I-103 (a semantic is not
shared without evidence in each model that carries it):

- composing a field does not extend its governing definition's meaning to Records outside that
  definition's domain, whatever the schema's applicability;
- a World-scoped field meaning does not become universal, or reach another model's Records, because
  a schema with a broader applicability names the field;
- an incompatibility with an established domain is not made valid by placing the field in a schema.

What this does not decide: whether an occurrence outside a definition's domain is governed by some
other `FIELD-DEFINITION`, or is not a legal composition at all. Composition settles neither, and no
source does (SC-078-D). No automatic permission to use World field definitions in other models, and
no automatic prohibition of every cross-model structural reuse, follows from this rule.

### 9.5 What remains unestablished — bounded

**SOURCE GAP.** No current source establishes:

- how a schema's applicability is matched against a field's domain — no tier-to-applicability
  matrix, compatibility predicate or matching service (SC-072-G; SC-076-D; SC-078-D);
- which `FIELD-DEFINITION` governs a named occurrence within a schema's scope, how a field name is
  resolved to a definition, or which of several definitions sharing a name is meant — no lookup,
  default choice or global field-name uniqueness (RS-072-5; RS-076-6; SC-078-E);
- a proof format showing that a composition lies within a domain.

What holds meanwhile: the governed meaning of a composed field is respected; where the governing
definition, or whether its domain covers the schema's applicability, cannot be established, no
complete semantic conformity of the composition is claimed. 077 already treats that judgement as
EXTERNAL (O-08), and under its §0 a Record with an EXTERNAL check not yet established is at best
PENDING_EXTERNAL, never CONFORMS.

**Answer to SC-077-D, on field identification:** whichever `FIELD-DEFINITION` governs an occurrence
holds its meaning and domain, and the schema holds neither — that is closed; how it is identified
is a source gap that no row is assigned, and consumer resolution by id and version stays row 115's.

## 10. Adjacent Responsibilities

### 10.1 Types and defaults

**SOURCE FACT.** Blueprint §9.4: schema structure is *"fields, types, required-ness, defaults"*.
072 FD-9 excludes type and default from `FIELD-DEFINITION`, and 072 §29 states that *"Type and
default are not handed to 078 as open ownership questions"*. RMS §10.2 lists neither, and whether a
`SCHEMA-DEFINITION` Record carries them is not established (SC-076-K; SC-077-F).

Types and defaults are schema-side and never a field definition's. This note restates that
assignment; it does not add it to row 078's `Done`. It creates no type or default element, decides
no serialization, designs no type system, and implies no schema needs a default. Carriage stays a
source gap (SC-078-G).

### 10.2 Controlled vocabularies

**SOURCE FACT.** `FIELD-DEFINITION` is Kind 4 and `CONTROLLED-VOCABULARY` Kind 7 (RMS §10.1).
Blueprint §9.4: *"Shared structure, independent vocabulary"*; per-Kind value sets may diverge, and
*"a forced enum union across kinds is prohibited"*.

Three responsibilities and a value stay apart:

- the `FIELD-DEFINITION` governs what a field means over its domain;
- a `CONTROLLED-VOCABULARY` governs a set of permitted terms and what each means, where one is used;
- the schema governs the field's structural occurrence;
- the owning model's Record carries the value.

For World's `status` (World-owned, not universal; RMS §14): World owns each Character Record's
`status` value and its own state semantics; the Registry governs the applicable definitions;
per-Kind vocabularies may differ; a schema states whether `status` occurs, is required and how many
values it carries; no forced enum union arises. No `FIELD-DEFINITION` ↔ `CONTROLLED-VOCABULARY`
reference or cardinality is created (SC-072-H; SC-078-H). 081 and 082 are not implemented here.

### 10.3 Constraints and validation

**SOURCE FACT.** RMS §10.6: *"CONSTRAINT-DEFINITION = a condition that must hold. VALIDATION-RULE
= a mechanism/procedure for checking a condition. Registry owns definitions for both; runtime
validators implement validation. These are never collapsed."*

Field meaning, schema composition, a condition, a check and its execution are five different things.
A schema may express constraints (RMS §10.2); whether they are its own content or references to
`CONSTRAINT-DEFINITION` Records is not established (SC-076-J; SC-078-M). A field's meaning states no
condition (072 FD-12). No validation code, mandatory validation-rule reference or constraint
binding is defined; the binder is row 113's.

### 10.4 Execution

**SOURCE FACT.** RMS §10.2: *"Registry does not execute schemas."* Blueprint §9.4: *"The Registry
holds no commands and no runtime behavior."* RMS §20 places implementation validation in a shared
runtime tier, and Blueprint §26.3b makes its verdict DERIVED.

A `SCHEMA-DEFINITION` does not become executable because it defines structure, and a
`FIELD-DEFINITION` validates no Record because it governs a field's meaning. This note defines no
validator, processor, mutation function or execution procedure.

## 11. Universal Envelope, Sovereignty and the Val Properties

### 11.1 Universal envelope and universal semantics

The seven envelope fields are unchanged (§8.4). No concept of this note — field occurrence,
requiredness, cardinality, order, domain, applicability, type, default, vocabulary, constraint,
`status`, `tier`, a lifecycle, a version or a validator — becomes an envelope field. *"tier and
status are World-owned, not universal."* (RMS §14).

None of RMS §4's nine prohibited universal semantics is introduced by composition: no Universal
Record Base assembled from composed fields; no Universal Relationship Record or Universal History
Record arising from a schema/field relation or its versions; no universal lifecycle, state model or
canonicality through a composed field; no universal Kind taxonomy or identity composition through
applicability or domain; and no universal semantic schema — composing the same field into schemas
of several models makes neither a schema nor a field meaning universal.

### 11.2 Sovereignty

**SOURCE FACT.** *"Registry governs the definitions. Each Record Model owns its Records."*
(Blueprint §13.6e; I-105). The six sovereign Record Models are W · E · P · R · V · I.

- Composition transfers nothing: a Character Record whose structure a Registry schema definition
  governs stays World's, with its identity, values, lifecycle, canonicality and semantic validation.
- Conformance transfers nothing: conforming is not belonging (076 §13).
- A field definition's meaning gives the Registry no value of that field (061 §7 row 2).
- No new Registry Kind arises. RMS §10.1 is *"CLOSED at fourteen"*. A field occurrence is a
  structural concept; it does not thereby require a Record identity of its own, and no Kind is
  created for field occurrences, for bindings between schemas and fields, or for compositions.

### 11.3 Row 078 `Val`: *"definition resolves"*

- `SCHEMA-DEFINITION` and `FIELD-DEFINITION` Records keep their own independent R Record identities
  under the universal grammar and envelope (RS-076-1, RS-076-2; RS-072-1).
- Composition replaces neither identity with a schema-local identity, and creates no composite
  identity for a field-in-a-schema.
- A field name is not a Registry Record identifier; a schema's applicability is not its identity.
- Resolution mechanics stay downstream: create/resolve/version is row 114's, consumer resolution by
  id+version row 115's. Neither is implemented here, and resolvable ≠ legal (063 §11).

### 11.4 Row 078 `Val`: *"versionable"*

Both families are versionable under rows 108–110 (VS-076-1; VS-072-1). **REQUIRED SYNTHESIS** —
every version stays bound by its family's rules (*"Every version stays bound by this
specification."*, VS-076-1; *"Every version stays bound by FD-1 to FD-22."*, VS-072-1), so the
closure is a stable allocation that every version stays inside: a later `SCHEMA-DEFINITION` version
cannot acquire field meaning or domain, and a later `FIELD-DEFINITION` version cannot acquire
composition, requiredness, cardinality, order, type or default. No version field, numbering,
supersession graph, compatibility rule, pinning procedure, deprecation policy or migration is
created, and none is prevented.

### 11.5 Row 078 `Val`: *"references only declared entities (063)"*

- Composition requires no reference (§7.4).
- Any concrete field reference carried is R → R to a `FIELD-DEFINITION` Record, and must lie in a
  relation the family establishes and satisfy 063 RB-1 to RB-6 (RF-076-2; RF-072-2).
- Any Model or Kind a schema names as applicability, or a field definition names as domain, is a
  declared one (RF-076-1; RF-072-1).
- An admissible target category is not a concrete relation (063 RB-5): nothing here authorizes a
  schema → vocabulary, field → vocabulary or schema → schema relation.
- No domain instance, domain state or runtime instance becomes a target or the semantic authority of
  either definition (RMS §10.3; §14 Example I).
- A reference is not by itself a dependency (§7.5).

## 12. Normative Boundary Rules

The IDs below are this note's. They are not pre-existing constitutional identifiers.

| ID | Rule | Basis | Evidence | Proven by |
|---|---|---|---|---|
| **SF-078-01** | **Separate Kinds.** `SCHEMA-DEFINITION` (Kind 5) and `FIELD-DEFINITION` (Kind 4) remain distinct Registry Kinds with separate identities and responsibilities. Closing the overlap merges nothing. | RMS §10.1; 064 §11 Q13; 076 SD-2; 072 RS-072-1 | SOURCE FACT | C-078-05 |
| **SF-078-02** | **One-way composition.** A schema composes governed fields into the structure it defines. A `FIELD-DEFINITION` composes no schema and prescribes no occurrence in any schema. | row 078 `Done`; 072 §10, FD-8; Blueprint §9.4 | SOURCE FACT; direction 078 CLOSURE | C-078-06 |
| **SF-078-03** | **Composition is not embedding.** Composing a field creates no second authoritative meaning or domain. A schema does not define, redefine, narrow or restate field meaning; schema text that purports to define a composed field's meaning has no authority as meaning, and a schema that contradicts the governing meaning is not a legal composition. | 076 §6, §8, SD-3; 064 §11 Q13; PC-3 | SOURCE FACT + 078 CLOSURE | C-078-07 |
| **SF-078-04** | **Definition is not occurrence.** A `FIELD-DEFINITION`'s existence places its field in no schema and no Record. | 072 FD-8, §7; Blueprint §9.4 | SOURCE FACT | C-078-08 |
| **SF-078-05** | **Requiredness.** Whether a field occurs as required belongs to the schema occurrence. A `FIELD-DEFINITION` states no requiredness, for any schema. | Blueprint §9.4; RMS §10.2; row 078; 072 FD-9 | SOURCE FACT | C-078-09 |
| **SF-078-06** | **Cardinality.** How many values an occurrence may carry belongs to the schema, within the constitution and the model's field architecture. A `FIELD-DEFINITION` states no cardinality, for any schema. | RMS §10.2; row 078; 076 §7; 072 FD-9 | SOURCE FACT | C-078-10 |
| **SF-078-07** | **Order.** Field order belongs to the schema side, where a schema makes it meaningful. No `FIELD-DEFINITION` imposes a position; no schema is required to be order-sensitive; a representation's sequence is not by itself semantic order. | row 078; 064 §12 Q8; 076 §7; 072 FD-9 | SOURCE FACT + 078 CLOSURE | C-078-11 |
| **SF-078-08** | **Meaning.** The `FIELD-DEFINITION` is authoritative for what its field means within its domain. | Blueprint §9.4; row 078; 072 FD-2 | SOURCE FACT | C-078-12 |
| **SF-078-09** | **Domain, not expanded.** The `FIELD-DEFINITION` holds the domain over which its meaning holds. A schema does not set, narrow or widen it, and composing the field does not extend its meaning to Records outside it. | row 078; 072 FD-3, §8; 076 §8; I-103 | SOURCE FACT + REQUIRED SYNTHESIS | C-078-13 |
| **SF-078-10** | **Domain is not applicability.** Field domain and schema applicability are separate concepts with separate owners. Their correspondence is not established, and no matching rule, matrix or lookup is invented. | 072 §8, SC-072-G; RMS §10.2; 076 SD-4, SC-076-D | REQUIRED SYNTHESIS; correspondence SOURCE GAP | C-078-14, C-078-15 |
| **SF-078-11** | **No implicit Record reference.** Composition does not require a concrete R → R reference to a `FIELD-DEFINITION`, and a field name is not a Registry identifier. No carrier is added to 073 or 077. | 076 RF-076-2; RMS §10.3 | SOURCE FACT | C-078-16 |
| **SF-078-12** | **Reference legality; reference ≠ dependency.** Any concrete reference actually carried satisfies Artifact 063; an admissible category is not a relation; a reference is not by itself a semantic dependency; dependency rules are 111's. | 063 §7, §11, RB-1, RB-5, RB-6; 062 D-9; 076 RF-076-11; 072 RF-072-9 | SOURCE FACT | C-078-17, C-078-18 |
| **SF-078-13** | **No ownership transfer.** Applicability, composition and conformance transfer no domain Record, value, field architecture, model semantics or canonicality to the Registry. | Blueprint §13.6e; I-105; 076 SD-9; 072 FD-14 | SOURCE FACT | C-078-22 |
| **SF-078-14** | **No execution.** Neither family executes a schema, a validation rule or a Record mutation, and this note implements none. | RMS §10.2, §20; Blueprint §9.4; 076 SD-8; 072 FD-13 | SOURCE FACT | C-078-21 |
| **SF-078-15** | **Universal envelope first.** No schema occurrence or field definition contradicts the seven-field envelope: an envelope field cannot be made optional, given another count or a changed role. No schema is required to list the envelope fields. | RMS §4, §5; Artifact 033; 072 FD-6 | SOURCE FACT + REQUIRED SYNTHESIS | C-078-23 |
| **SF-078-16** | **Types and defaults.** Schema-side under Blueprint §9.4 and never a field definition's; their carriage in a `SCHEMA-DEFINITION` Record is not decided here. | Blueprint §9.4; 072 FD-9, §29; SC-076-K | SOURCE FACT; carriage SOURCE GAP | C-078-19 |
| **SF-078-17** | **Vocabulary apart.** `CONTROLLED-VOCABULARY` stays separate from field meaning and from schema occurrence; per-Kind value sets may diverge; no relation or cardinality between field and vocabulary is invented. | RMS §10.1; Blueprint §9.4; 072 FD-10, FD-11, SC-072-H | SOURCE FACT | C-078-20 |
| **SF-078-18** | **Constraint and validation apart.** Field meaning and schema composition are neither a `CONSTRAINT-DEFINITION` nor a `VALIDATION-RULE`, and the two stay uncollapsed. | RMS §10.6, §20; 072 FD-12, FD-13; 076 SD-6 | SOURCE FACT | C-078-21 |
| **SF-078-19** | **No new Kind; no universal semantic schema.** The boundary creates no Registry Kind and no universal schema, field roster, `status` or `tier`. | RMS §4, §10.1, §14; 076 SD-11, SD-12; 072 FD-5, FD-7 | SOURCE FACT | C-078-24, C-078-25 |
| **SF-078-20** | **Closure complete.** The allocation of composition, requiredness, cardinality and order to the schema side and of meaning and domain to the field side is complete as row 078 assigns it. Unresolved representation, lookup, matching or other semantic questions do not reopen it. | row 078 `Done`, `Why`; PC-3 | 078 CLOSURE | C-078-04, C-078-28, C-078-37 |

## 13. Boundary Status and Decision Matrices

### 13.1 Boundary-status matrix

| Question | Status | Owner / where |
|---|---|---|
| who owns field meaning | CLOSED BY SOURCE | row 078; Blueprint §9.4; SF-078-08 |
| who owns field domain | CLOSED BY SOURCE | row 078; 072 §8; SF-078-09 |
| who owns composition — which fields occur | CLOSED BY SOURCE | row 078; Blueprint §9.4; SF-078-02 |
| the direction of composition | CLOSED BY 078 | §7.2; SF-078-02 |
| who owns requiredness; cardinality | CLOSED BY SOURCE | row 078; RMS §10.2; SF-078-05, SF-078-06 |
| who owns order | CLOSED BY SOURCE | row 078; SF-078-07 |
| order only where meaningful; no field-side position; sequence ≠ order | CLOSED BY 078 | §8.3; SF-078-07 |
| PC-3's edge — *"a schema is partly a set of field definitions"* | CLOSED BY 078 | §7.3; SF-078-03 |
| a schema stating its own meaning for a composed field | CLOSED BY 078 — not permitted | §7.3; SF-078-03 |
| a field definition stating requiredness, cardinality or order | CLOSED BY SOURCE — not permitted | 072 FD-9; SF-078-05–SF-078-07 |
| composition expanding a field's domain | CLOSED BY 078 — it does not | §9.4; SF-078-09 |
| who owns type and default | CLOSED BY SOURCE | Blueprint §9.4; SF-078-16 |
| whether a `SCHEMA-DEFINITION` carries type and default | SOURCE GAP | SC-078-G |
| how domain and applicability correspond | SOURCE GAP | SC-078-D |
| which `FIELD-DEFINITION` governs a named occurrence; field-name grammar | SOURCE GAP | SC-078-E |
| a concrete field-reference carrier | SOURCE GAP — none required; legality CLOSED BY SOURCE where one is carried | SC-078-E; SF-078-11, SF-078-12 |
| when field order is significant | SOURCE GAP | SC-078-F |
| how significant order is encoded | DEFERRED TO NAMED OWNER | 077 (076 §7) |
| resolution by id+version | DEFERRED TO NAMED OWNER | 114; 115 |
| version, supersession and deprecation mechanics | DEFERRED TO NAMED OWNER | 108; 109; 110 |
| dependency direction, asymmetry, cycles | DEFERRED TO NAMED OWNER | 111 |
| constraint/validation binding | DEFERRED TO NAMED OWNER | 113 |
| reference validator; validation suite | DEFERRED TO NAMED OWNER | 112; 116 |
| constraint, relationship and validation-reference targets | SOURCE GAP | SC-078-M |
| the field/vocabulary relation | SOURCE GAP | SC-078-H (families 081–082) |
| applicability cardinality and presence | SOURCE GAP — not 078's | SC-078-I |
| zero occurrences | SOURCE GAP — not 078's | SC-078-J |
| whether a schema lists the envelope fields | SOURCE GAP | SC-078-K |
| a listed envelope field's presence and count | CLOSED BY SOURCE | RMS §4; Artifact 033; SF-078-15 |
| model-owned schemas against `SCHEMA-DEFINITION` | SOURCE GAP | SC-078-L |
| what *domain* covers beyond scope; domain between definition and model field architecture | SOURCE GAP — outside this overlap | SC-078-N |
| committing either family's Records | DEFERRED TO NAMED OWNER | 152, after G-CANON-R |

No row is marked closed because a representation can carry it.

### 13.2 Decision matrix

| Case | Outcome | Rule |
|---|---|---|
| a schema composes a governed field and states its requiredness and cardinality | LEGAL, as far as this boundary decides; external checks still apply | SF-078-02, SF-078-05, SF-078-06 |
| two schemas compose one field with different requiredness or cardinality | LEGAL at the boundary; one meaning | SF-078-03, SF-078-05, SF-078-06 |
| a schema states that a composed field means something else | ILLEGAL | SF-078-03 |
| a schema stores its own copy of a field's meaning as authoritative | ILLEGAL | SF-078-03 |
| a field definition requires its field in every schema | ILLEGAL | SF-078-04, SF-078-05 |
| a field definition fixes its field's cardinality or position for every schema | ILLEGAL | SF-078-06, SF-078-07 |
| a schema makes an envelope field optional, or gives it two values | ILLEGAL | SF-078-15 |
| a schema lists no envelope field | not decided by this boundary | SC-078-K |
| a schema claims a World-scoped meaning as universal because it names the field | ILLEGAL — the claimed expansion | SF-078-09 |
| a schema composes a field whose governing definition cannot be identified | UNRESOLVED — no complete semantic conformity claimed | SF-078-10; SC-078-E |
| a schema's applicability reaches Records outside a field's domain | that definition's meaning does not reach them; the rest UNRESOLVED | SF-078-09; SC-078-D |
| an occurrence names its field by name, with no Record reference | LEGAL as current representation (077) | SF-078-11 |
| an occurrence carries an R → R reference to a `FIELD-DEFINITION` Record | LEGAL at the boundary where carried as RF-076-2 describes — its target actually a `FIELD-DEFINITION`, 063 satisfied; 077 currently defines no element for one | SF-078-12 |
| a schema cites a domain Record as authority for a field's meaning | ILLEGAL | SF-078-12; RMS §10.3 |
| a schema that makes order meaningful states it | LEGAL; encoding 077's | SF-078-07 |
| a reader treats 077's occurrence sequence as semantic order | ILLEGAL inference | SF-078-07 |
| a version of a field definition adds requiredness | ILLEGAL | SF-078-05; §11.4 |
| a schema definition runs a check, or rewrites a Record | ILLEGAL | SF-078-14 |
| how versions are pinned or superseded | DEFERRED | 108–110 |

## 14. Worked Examples

Every example is **schematic**. No Record is created, no identifier is minted, no field is defined,
and nothing here is Registry data. Placeholders in angle brackets stand for undecided particulars.

**A. Legal — conceptual composition.** A `SCHEMA-DEFINITION` applicable to the declared Record
Model W and the declared World Kind `CHARACTER` composes World's `status` with requiredness `<r>`
and cardinality `<c>`. The schema owns that `status` occurs in its structure, and its requiredness
and cardinality. The `FIELD-DEFINITION` of `status` keeps what `status` means and over what domain.
The applicable `CONTROLLED-VOCABULARY` definition, where one governs, stays separate. World owns
every Character Record's `status` value. No Registry definition runs a check. Nothing here says
what `<r>` or `<c>` is, adds a `status` value, or makes `status` universal.

**B. Illegal — semantic redefinition.** A schema composes a governed field and states that, in its
structure, the field means something its `FIELD-DEFINITION` contradicts. Rejected: composition
cannot redefine governed meaning (SF-078-03; 076 §8). No change to the field definition is implied:
what is wrong is the schema's statement, not the definition.

**C. Illegal — field-side requiredness.** A `FIELD-DEFINITION` states that its field is mandatory
in every schema that might use it. Rejected: requiredness belongs to schema structure (SF-078-05;
072 FD-9). That every envelope field is present in every Record is a separate, constitutional
obligation (RMS §4); it is not a requiredness the field's definition imposes.

**D. Legal — different structural contexts.** Two schematic schemas compose the same governed field
`<field>`, one stating it required and single-valued, the other optional and many-valued. The
field's meaning is unchanged, and the structural difference is each schema's own (SF-078-03,
SF-078-05, SF-078-06). This does not show that any real field admits either shape.

**E. Illegal — domain expansion.** A schema treats a World-scoped field meaning as if it governed
Records of every model because the schema names the field in a broader context. The claimed
expansion is rejected: composition does not extend a meaning beyond its domain (SF-078-09). This
example invents no compatibility rule for other domain and applicability shapes (SC-078-D).

**F. Boundary — an envelope field.** A schema lists `slug`. It cannot make `slug` identity-bearing
(*"slug is decoration only"*, RMS §5), make it optional, or give it any count but one (SF-078-15).
077 writes that as required yes and 1..1 (O-07). It does not follow that every schema must list all
seven envelope fields (SC-078-K).

**G. Legal as current representation — no reference carrier.** Artifact 077 names an occurrence by
field name rather than by a Registry Record reference. That is legal as the current structural
representation, subject to 077's EXTERNAL checks and the source gaps recorded here. The absence of
a carrier does not remove the field's governed meaning (§7.4). Field-name lookup and domain
compatibility are not thereby resolved (SC-078-D, SC-078-E).

**H. Order.** A schematic schema composes `<field-a>`, `<field-b>` and `<field-c>`. If the schema
makes their order meaningful, that order is the schema's (SF-078-07). None of the three
`FIELD-DEFINITION`s imposes a position on any schema, and if the schema makes no order meaningful,
the sequence in which they are written carries none. No ordering algorithm or position element is
introduced.

**I. Illegal — a domain instance as authority.** A schema definition cites a particular Character
Record, written schematically as `W-CH-…-<slug>`, as the authority for what `status` means.
Rejected: a domain instance is never a Registry reference target or semantic authority (RMS §10.3;
063 §7 row 6; 076 RF-076-7), however well the identifier resolves — *"Resolvable ≠ legal."* (063
§11).

## 15. Prohibited Inferences

| # | Invalid inference | Correct reading | Basis |
|---|---|---|---|
| PI-01 | A schema is a `FIELD-DEFINITION` Record containing many fields | a schema composes occurrences; field meaning stays in each field's definition | 076 §6, §8; §7.3 |
| PI-02 | A `FIELD-DEFINITION` is a field occurrence | a definition governs meaning; an occurrence is structure | 072 §10, §28; SF-078-04 |
| PI-03 | Defining a field inserts it into every applicable schema | a definition places its field in no schema | 072 FD-8; SF-078-04 |
| PI-04 | Composing a field transfers its meaning to the schema | the definition stays the sole holder | 076 §8; SF-078-03 |
| PI-05 | A schema can redefine a field's domain | domain is the field side's and is not expanded | row 078; SF-078-09 |
| PI-06 | One field name is the same governed semantic across models | a name alone establishes no shared semantic | 072 §7; I-103 |
| PI-07 | `FIELD-DEFINITION` owns requiredness | the schema does | row 078; 072 FD-9; SF-078-05 |
| PI-08 | `FIELD-DEFINITION` owns cardinality | the schema does | row 078; 072 FD-9; SF-078-06 |
| PI-09 | `FIELD-DEFINITION` owns order | the schema side does, where meaningful | row 078; 072 FD-9; SF-078-07 |
| PI-10 | `FIELD-DEFINITION` owns type or default | schema-side | Blueprint §9.4; 072 FD-9; SF-078-16 |
| PI-11 | `SCHEMA-DEFINITION` owns the values domain Records carry | the owning model does | Blueprint §13.6e; SF-078-13 |
| PI-12 | Composition creates a mandatory R → R reference | none is required | 076 RF-076-2; SF-078-11 |
| PI-13 | A legal reference establishes a semantic dependency | not by itself | 062 D-9; SF-078-12 |
| PI-14 | A resolvable reference is legal | resolvable ≠ legal | 063 §11; §11.3 |
| PI-15 | A declaration reference is a reference to a Registry definition Record | declared Model ≠ `MODEL-DEFINITION`; declared Kind ≠ `KIND-DEFINITION` | 063 §8.2, §8.3; 076 RF-076-5 |
| PI-16 | A schema applicable to a Kind admits that Kind | applicability names a declared Kind and admits nothing | 076 SD-4; RMS §10.1 |
| PI-17 | A schema applicable to World owns World Records | conforming Records stay World's | 076 SD-9; SF-078-13 |
| PI-18 | Schema definition is schema execution | *"Registry does not execute schemas."* | RMS §10.2; SF-078-14 |
| PI-19 | A field definition is a controlled vocabulary | Kind 4 ≠ Kind 7 | RMS §10.1; SF-078-17 |
| PI-20 | A vocabulary's value set must be identical across Kinds | per-Kind sets may diverge; no forced union | Blueprint §9.4; SF-078-17 |
| PI-21 | A schema may override the universal envelope | the envelope binds every schema | RMS §4; SF-078-15 |
| PI-22 | Every schema must enumerate the envelope fields | not established | SC-077-M; SC-078-K |
| PI-23 | Every schema must impose a meaningful field order | order is owned where meaningful, required nowhere | §8.3; SF-078-07 |
| PI-24 | A list carrier establishes semantic order | sequence ≠ semantic order | §8.3; SF-078-07 |
| PI-25 | Closing DG-03 requires a new Registry Kind | no Kind is created | RMS §10.1; SF-078-19 |
| PI-26 | 078 must add reference-carrier fields to 073 or 077 | no carrier is added; both unchanged | 076 RF-076-2; §7.4 |
| PI-27 | The schema/field boundary licenses a universal semantic schema | prohibited universal semantic | RMS §4; SF-078-19 |
| PI-28 | Closing DG-03 resolves every domain-compatibility question | ownership is closed; correspondence is a source gap | §9.5; SC-078-D |
| PI-29 | Closing DG-03 implements Registry versioning | 108–110's | §11.4; §19 |
| PI-30 | Closing DG-03 changes model-owned schema custody | not established; unchanged | Blueprint §13.7; SC-078-L |
| PI-31 | 077's by-name occurrence is the only representation the constitution permits | current representation, a 077 CHOICE | §7.4 |
| PI-32 | DG-03 is a gate this row introduces or must pass | row 078 carries `G: —`; DG-03 is not in PART VIII's decision gates | SC-078-C |

## 16. Source-Condition Register

Each entry gives the source statements, the question, what is established, what is undecided,
whether this artifact owns its resolution, the owner where one is established, and whether it
blocks.

### SC-078-A — "The Registry is not schema" against RMS §10.2 — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4: *"The Registry is not schema."* RMS §10.2: *"SCHEMA-DEFINITION is a Registry Record. Schema implementation is not Registry runtime."* |
| **Question** | whether the Registry may hold schema definitions at all |
| **Established** | a schema's definition is a Registry Record; the Registry does not execute it; within the Registry, field meaning stays `FIELD-DEFINITION`'s and structure `SCHEMA-DEFINITION`'s (076 SC-076-C) |
| **Undecided** | nothing for this boundary |
| **078 owns?** | no — reconciled by RMS §10.2 and 076. The older categorical reading is not revived, and the Blueprint is not edited. |
| **Blocks?** | no |

### SC-078-B — PC-3 and DG-03 — CLOSED BY 078

| | |
|---|---|
| **Sources** | RMS Appendix H PC-3; row 078 `Done` and `Why`; 076 §8, SC-076-D; 072 §11, SC-072-E; 064 §11 Q13 |
| **Question** | where the edge between schema composition and field meaning lies |
| **Established** | the split row 078 states (§6) |
| **Closed here** | composition's direction (§7.2), composition ≠ embedding (§7.3), order's scope (§8.3), non-expansion of domain (§9.4), and SF-078-01 to SF-078-20 |
| **078 owns?** | **yes** — its assigned closure; certified at §17 |
| **Blocks?** | no |

### SC-078-C — DG-03's audit text; DG-03 is not a decision gate — RECORDED

| | |
|---|---|
| **Sources** | row 078 `Why`: *"audit DG-03 closed here, not deferred"*; Roadmap PART VIII *Decision gates*, which lists DG-01 and DG-02 only; Roadmap §0.2 cites *"PART VIII DG-01/DG-02"* |
| **Question** | what audit text DG-03 carries, and whether DG-03 is a gate |
| **Established** | DG-03 occurs in the repository only in row 078 and in documents quoting it; row 078 carries `G: —` |
| **Undecided** | the wording of the audit item behind the label |
| **Treatment** | DG-03's content is taken from row 078's own `Done` and from PC-3 — no other text is invented for it. DG-03 is treated as the label row 078 gives the overlap it closes; no gate is introduced, and PART VIII is not edited. |
| **078 owns?** | the closure, yes; the audit text, no — the Roadmap author's |
| **Blocks?** | no |

### SC-078-D — field domain against schema applicability — SOURCE GAP

| | |
|---|---|
| **Sources** | 072 §8, SC-072-G (*"how a field's domain relates to a schema's applicable Model and Kind"*); 076 SC-076-D; RMS §10.2; RMS §14 |
| **Question** | how a schema's applicability is matched against the domain of a field it composes |
| **Established** | the two are distinct and separately owned (SF-078-10); composition does not expand a domain (SF-078-09) |
| **Undecided** | any correspondence rule, compatibility matrix or proof; whether an occurrence outside a domain is governed by another definition or is not legal |
| **078 owns?** | ownership, yes — closed; the correspondence, no. 072 passed it *"as input, not as a new exit criterion"*. |
| **Owner** | none established |
| **Blocks?** | no — the ownership split is complete without it |

### SC-078-E — identifying the governing FIELD-DEFINITION — SOURCE GAP

| | |
|---|---|
| **Sources** | 076 RF-076-2, RS-076-6; 072 RS-072-5 (*"how a consumer finds the definition of a given field is not defined here"*); 077 SC-077-D; RMS §10.3; 063 §7 |
| **Question** | which `FIELD-DEFINITION` governs a named occurrence; how a field name is resolved to a definition; what carrier, if any, an occurrence holds |
| **Established** | no carrier is required (SF-078-11); any carried is R → R and obeys 063 (SF-078-12); whichever definition governs holds meaning and domain |
| **Undecided** | a field-name grammar, uniqueness rule, lookup, default choice among same-name definitions, and any carrier |
| **078 owns?** | no |
| **Owner** | none established for the mapping; resolution by id+version is 115's, create/resolve/version 114's |
| **Blocks?** | no |

### SC-078-F — when field order is significant — SOURCE GAP

| | |
|---|---|
| **Sources** | row 078 `Done`; 064 §12 Q8; 076 §7 (*"078 closes it, 077 encodes it"*); 077 SC-077-D |
| **Established** | order is schema-side, only where meaningful; no field-side position; sequence ≠ order (SF-078-07) |
| **Undecided** | any case in which, or criterion by which, field order is significant |
| **078 owns?** | ownership, yes — closed; the criterion, no |
| **Owner** | encoding: 077; criterion: none established |
| **Blocks?** | no |

### SC-078-G — carriage of types and defaults — SOURCE GAP

| | |
|---|---|
| **Sources** | Blueprint §9.4; RMS §10.2 (lists neither); 072 FD-9, SC-072-E, §29; 076 SC-076-K; 077 SC-077-F |
| **Established** | schema-side, never a field definition's (SF-078-16) |
| **Undecided** | whether, and how, a `SCHEMA-DEFINITION` Record carries them |
| **078 owns?** | no — 072 §29 did not hand them over as open ownership questions |
| **Owner** | none established |
| **Blocks?** | no |

### SC-078-H — FIELD-DEFINITION and CONTROLLED-VOCABULARY — SOURCE GAP

| | |
|---|---|
| **Sources** | RMS §10.1; Blueprint §9.4; 072 FD-10, FD-11, SC-072-H |
| **Established** | distinct Kinds and responsibilities; per-Kind divergence; no forced union (SF-078-17) |
| **Undecided** | any cardinality, identity or reference relation between a field definition and a vocabulary |
| **078 owns?** | no |
| **Owner** | the vocabulary family is 081–082's; no owner is established for the relation |
| **Blocks?** | no |

### SC-078-I — applicability cardinality and presence — SOURCE GAP

| | |
|---|---|
| **Sources** | 076 SD-4, SC-076-N (*"not established, and no source assigns it — not to 078"*); 077 SC-077-C |
| **Undecided** | how many Models and Kinds one schema may name; whether Model-only or several-target applicability is legal |
| **078 owns?** | no — it is not part of the schema/field overlap |
| **Owner** | none established |
| **Blocks?** | no |

### SC-078-J — zero field occurrences — SOURCE GAP

| | |
|---|---|
| **Sources** | 077 SC-077-O, O-01, O-10; 076 §7, SD-14 |
| **Undecided** | whether a schema definition with no field occurrence is admissible |
| **078 owns?** | no — 077 records that 078's closure *"is the schema/field overlap, not this"* |
| **Owner** | none established |
| **Blocks?** | no |

### SC-078-K — envelope fields as occurrences — SOURCE GAP

| | |
|---|---|
| **Sources** | RMS §4; Artifact 033; 077 SC-077-M, O-07 |
| **Established** | a listed envelope field cannot be optional or other than one (SF-078-15) |
| **Undecided** | whether a schema lists the envelope fields |
| **078 owns?** | no |
| **Blocks?** | no |

### SC-078-L — model-owned schemas against SCHEMA-DEFINITION — SOURCE GAP

| | |
|---|---|
| **Sources** | row 184 *CHARACTER schema* (`canon/world/character.schema`, `Own: W`); Blueprint §13.7; 076 SC-076-I; 077 SC-077-G |
| **Established** | the schema/field allocation holds on the schema side either way (§6); no model-owned schema becomes Registry-owned |
| **Undecided** | whether a model-owned schema is described by, declared through or independent of a `SCHEMA-DEFINITION` Record |
| **078 owns?** | no — schema custody is unchanged |
| **Blocks?** | no |

### SC-078-M — constraint, relationship and validation-reference targets — SOURCE GAP

| | |
|---|---|
| **Sources** | RMS §10.2, §10.6, §15; 076 SC-076-J; 077 SC-077-E |
| **Established** | the tiers stay apart (SF-078-18) |
| **Undecided** | whether a schema's constraints are content or references; their target families |
| **078 owns?** | no |
| **Owner** | binding: 113; form: none established |
| **Blocks?** | no |

### SC-078-N — what "domain" covers, and how it is shared with field architecture — SOURCE GAP

| | |
|---|---|
| **Sources** | 072 §8, SC-072-G; rows 179, 274, 301 (`Done`: *"field domains"*); Roadmap PART III LS-2 |
| **Established** | a domain is at least a scope at one of three tiers, held by the `FIELD-DEFINITION` (SF-078-09) |
| **Undecided** | any value-domain concept beyond scope; how domain is divided between a field definition and the model field architecture that delivers *"field domains"* |
| **078 owns?** | no — neither is a schema/field question |
| **Owner** | each model's field-architecture row for its fields' domains (072 SC-072-G) |
| **Blocks?** | no |

### SC-078-O — `LS: LS-1` on row 078 — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 078 `LS: LS-1`; Roadmap PART III: *"LS-1 Kind ↔ Kind-Definition — every Kind spec ↔ its Registry KIND-DEFINITION. ATOMIC-PAIR."*; Roadmap §0.7 (the Registry's pairs are 064 ↔ 075); Artifact 003 |
| **Question** | how a boundary note — neither a Kind specification nor a `KIND-DEFINITION` — relates to LS-1 |
| **Treatment** | the label is preserved; no pair, lockstep class, dependency, reference or commit atomicity is invented (cf. 076 SC-076-H; 072 SC-072-D). Route: ROADMAP ISSUE. |
| **078 owns?** | no — the Roadmap author's |
| **Blocks?** | no |

### SC-078-P — row 078 `Canon` metadata on a docs path — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 078 `T: doc · Canon: canonical-about-meaning · CD: yes`; Artifact 003: *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`"*; `CD` *"licenses nothing"* |
| **Treatment** | the metadata is preserved; this note writes no canonical data and authorizes no canonical Registry write (cf. 076 SC-076-M). Route: ROADMAP / CONVENTION ISSUE. |
| **078 owns?** | no |
| **Blocks?** | no |

### SC-078-Q — requirement text RR-17, RR-27 — NON-BLOCKING, UNVERIFIED

| | |
|---|---|
| **Sources** | row 078 `Req: RR-17,RR-27`; the Revolving Resolution Note, GAP-C (*"missing requirement register"*). The IDs occur only in the Roadmap and in Registry artifacts carrying them as their own `Req`; nowhere in the checkout is either defined. |
| **Treatment** | both IDs are carried exactly; no requirement text is stated and no compliance with it is claimed. Row 078 is validated against its `Val`, `Done` and cited sources. |
| **Blocks?** | no (GAP-C) |

### SC-078-R — `docs/registry/PURPOSE.md` and a boundary note — RECORDED

| | |
|---|---|
| **Sources** | `docs/registry/PURPOSE.md` lists family specifications, structural contracts and canonicalization sources as what belongs here; row 078 assigns this path |
| **Treatment** | a boundary note between two families is not named in that list. The Roadmap row assigns the path, and `PURPOSE.md` is structural documentation, not an authority source; it is not edited. |
| **Blocks?** | no |

## 17. DG-03 Closure Certificate

**The five responsibilities row 078 assigns, and where each is closed:**

| Responsibility | Owner | Closed at | Rules |
|---|---|---|---|
| 1 composition | schema side | §7.1–§7.3 | SF-078-02, SF-078-03, SF-078-04 |
| 2 cardinality | schema side | §8.2 | SF-078-06 |
| 3 requiredness | schema side | §8.1 | SF-078-05 |
| 4 order | schema side, where meaningful | §8.3 | SF-078-07 |
| 5 meaning and domain | `FIELD-DEFINITION` | §9.1–§9.4 | SF-078-08, SF-078-09, SF-078-10 |

| ID | Claim | Proven by | Source |
|---|---|---|---|
| **DG-03-A** | **Distinct objects.** `SCHEMA-DEFINITION` and `FIELD-DEFINITION` remain separate Registry Kinds with separate identities and responsibilities. | SF-078-01; §11.3 | RMS §10.1; 064 §11 Q13; RS-076-1; RS-072-1 |
| **DG-03-B** | **Composition direction.** A schema composes governed fields into structure; field definitions compose no schema and produce no occurrence by themselves. | SF-078-02, SF-078-04; §7.2 | row 078; 072 §10, FD-8 |
| **DG-03-C** | **Schema-owned obligations.** Composition, cardinality, requiredness and order belong to schema structure. | SF-078-02, SF-078-05, SF-078-06, SF-078-07; §8 | row 078; Blueprint §9.4; RMS §10.2 |
| **DG-03-D** | **Field-owned obligations.** Meaning and domain belong to `FIELD-DEFINITION`. | SF-078-08, SF-078-09; §9 | row 078; 072 FD-2, FD-3 |
| **DG-03-E** | **No semantic duplication.** Composing a field creates no competing authoritative meaning or domain. | SF-078-03, SF-078-09; §7.3, §9.4 | 076 §8; 064 §11 Q13 |
| **DG-03-F** | **No unauthorized representation.** No mandatory `FIELD-DEFINITION` reference carrier, lookup protocol, field-name grammar or identity format is invented. | SF-078-10, SF-078-11, SF-078-12; §7.4 | 076 RF-076-2; 063 §7 |
| **DG-03-G** | **No authority transfer.** Composition and conformance transfer no domain Record, value or model semantics. | SF-078-13; §11.2 | Blueprint §13.6e; I-105; 076 SD-9 |
| **DG-03-H** | **Execution separate.** Neither family executes schema validation or Record mutation. | SF-078-14, SF-078-18; §10.4 | RMS §10.2, §10.6, §20 |
| **DG-03-I** | **Residual questions bounded.** The unresolved questions concern mechanisms — identification, matching, encoding, carriage — or questions outside the overlap; none concerns who owns composition, requiredness, cardinality, order, meaning or domain. | §13.1; §16; SF-078-20 | 072 §29; 076 SC-076-N |
| **DG-03-J** | **Final result.** The overlap PC-3 records and row 078 assigns is closed, within that scope. | DG-03-A to DG-03-I | row 078 `Done`, `Why` |

**Why the overlap is resolved.** PC-3's edge was the possibility that a schema, being *"partly a
set of field definitions"*, would hold field meaning too. §7.3 rules that out, §6 assigns every
concern on the edge to exactly one side, and §13.1 shows no ownership question left open.

**Why the closure stays inside its authority.** It merges no Kind, adds no element to 073 or 077,
creates no relation, edge or gate, and decides none of the source gaps of §16. Each unresolved
entry in §16 is a question of mechanism, encoding or another family's semantics; none of them is a
question of which side owns what.

## 18. Conformance Conditions

Class: **STATIC** — checked by reading this document; **CROSS-SOURCE** — checked against the cited
sources; **REPOSITORY** — checked against the repository's actual changes, not provable from this
text. No runtime execution is needed to prove a textual ownership boundary, and none is claimed.

| ID | Condition | Class | Where |
|---|---|---|---|
| **C-078-01** | The header and the §2 table reproduce current Roadmap row 078 exactly. | CROSS-SOURCE | header; §2 |
| **C-078-02** | The hard dependencies are exactly 076 and 072; 073, 077 and every other supporting artifact stay supporting context. | CROSS-SOURCE | §4; §5 |
| **C-078-03** | The document is a documentation CONTRACT — not a schema, a structural contract, a family specification, a Record or an implementation. | STATIC | §2 |
| **C-078-04** | The schema/field overlap is explicitly closed. | STATIC | §1; §17; SF-078-20 |
| **C-078-05** | `SCHEMA-DEFINITION` and `FIELD-DEFINITION` remain distinct Kinds. | CROSS-SOURCE | SF-078-01 |
| **C-078-06** | The direction of composition is stated: schema over fields, never the reverse. | STATIC | §7.2; SF-078-02 |
| **C-078-07** | Composition neither copies nor redefines field meaning. | CROSS-SOURCE | §7.3; SF-078-03 |
| **C-078-08** | A `FIELD-DEFINITION` creates no field occurrence. | CROSS-SOURCE | §7.2; SF-078-04 |
| **C-078-09** | Requiredness is schema-owned. | CROSS-SOURCE | §8.1; SF-078-05 |
| **C-078-10** | Cardinality is schema-owned. | CROSS-SOURCE | §8.2; SF-078-06 |
| **C-078-11** | Order is schema-owned where meaningful; no schema is required to be order-sensitive; sequence is not semantic order. | CROSS-SOURCE | §8.3; SF-078-07 |
| **C-078-12** | `FIELD-DEFINITION` owns meaning. | CROSS-SOURCE | §9.1; SF-078-08 |
| **C-078-13** | `FIELD-DEFINITION` owns domain, and composition does not expand it. | CROSS-SOURCE | §9.2, §9.4; SF-078-09 |
| **C-078-14** | Schema applicability does not itself redefine field domain. | CROSS-SOURCE | §9.3; SF-078-10 |
| **C-078-15** | No universal domain/applicability matching algorithm is invented. | STATIC | §9.5; SC-078-D |
| **C-078-16** | No mandatory field-definition Record reference is invented. | CROSS-SOURCE | §7.4; SF-078-11 |
| **C-078-17** | Any reference actually carried obeys Artifact 063. | CROSS-SOURCE | §11.5; SF-078-12 |
| **C-078-18** | Reference and dependency stay distinct. | CROSS-SOURCE | §7.5; SF-078-12 |
| **C-078-19** | Type and default ownership follows Blueprint §9.4, with no carrier invented. | CROSS-SOURCE | §10.1; SF-078-16 |
| **C-078-20** | Controlled vocabulary stays a distinct responsibility, with no relation invented. | CROSS-SOURCE | §10.2; SF-078-17 |
| **C-078-21** | No runtime validator or schema engine is introduced; constraint and validation rule stay apart. | STATIC | §10.3, §10.4; SF-078-14, SF-078-18 |
| **C-078-22** | Domain Record ownership stays with the owning model. | CROSS-SOURCE | §11.2; SF-078-13 |
| **C-078-23** | The seven-field universal envelope is unchanged and no schema may contradict it. | CROSS-SOURCE | §8.4, §11.1; SF-078-15 |
| **C-078-24** | No universal `status`, `tier` or semantic schema is introduced. | CROSS-SOURCE | §11.1; SF-078-19 |
| **C-078-25** | No fifteenth Registry Kind is introduced. | CROSS-SOURCE | §11.2; SF-078-01, SF-078-19 |
| **C-078-26** | Resolution is preserved without implementation. | CROSS-SOURCE | §11.3 |
| **C-078-27** | Versionability is preserved without implementing 108–110. | CROSS-SOURCE | §11.4 |
| **C-078-28** | The DG-03 closure is supported by an explicit rule matrix. | STATIC | §12; §17 |
| **C-078-29** | Residual source gaps are accurately classified. | CROSS-SOURCE | §13.1; §16 |
| **C-078-30** | `LS: LS-1` is preserved without an invented pairing. | CROSS-SOURCE | SC-078-O |
| **C-078-31** | No gate is introduced, and DG-03 is not treated as one. | CROSS-SOURCE | SC-078-C; PI-32 |
| **C-078-32** | The direct downstream handoff is exactly 108. | CROSS-SOURCE | §19 |
| **C-078-33** | No downstream `Val` or `Done` is enlarged. | CROSS-SOURCE | §19 |
| **C-078-34** | No concrete Registry Record is authored or committed. | REPOSITORY | §2 |
| **C-078-35** | Only `docs/registry/schema_field_boundary.md` is created by this artifact. | REPOSITORY | row 078 |
| **C-078-36** | Row 078's `Val` is mapped clause by clause to evidence. | STATIC | §11.3–§11.5; §20 |
| **C-078-37** | Row 078's `Done` is proven, not merely asserted. | STATIC | §6–§9; §17; §20 |
| **C-078-38** | Source gaps are not presented as constitutional decisions. | STATIC | §16 |

## 19. Downstream Handoff

**To 108** (definition evolution model, `docs/models/registry/evolution.md`; `H: 064,078`; `S:
065`; `Val`: *"version"*; `Done`: *"temporal account without a World History Record"*). 108 may
take from this note, as a stable input to Registry evolution:

1. **the closed allocation** — composition, requiredness, cardinality and order on the schema side;
   meaning and domain on the field side (§6; SF-078-20);
2. **its permanence across versions** — a version of either family stays inside its own side of the
   split (§11.4);
3. **two separate identities** — each family's Records evolve as their own R Records; a composition
   has no identity of its own to version (§11.3);
4. **no relation is created** — this note creates no reference, edge or relation between a schema
   and a field definition along which a change would be carried, and decides nothing about how a
   change on one side reaches the other.

108 is not asked to decide, and this note does not decide: a version identifier format, consumer
pinning, supersession representation, deprecation, migration, compatibility-version matching, a
temporal implementation, or any World History Record. 108's `Val` and `Done` are not enlarged.

**Other downstream owners, preserved and not implemented:**

| Row | Keeps | `Val` |
|---|---|---|
| 109 | definition versioning rules | *"consumers pin a version"* |
| 110 | supersession and deprecation | *"deprecated ≠ deleted"* |
| 111 | Registry dependency direction | *"downward-only; asymmetric; no cycles"* |
| 112 | Registry reference validator | *"rejects any definition referencing a domain instance"* |
| 113 | constraint/validation binder | *"a constraint resolves to exactly one rule"* |
| 114 | Registry implementation kernel | *"create/resolve/version a definition"* |
| 115 | Registry resolution service | *"consumer resolves by id+version"* |
| 116 | Registry validation suite | *"definitions well-formed and legal"* |
| 123 | Registry lockstep tests | *"no unpaired lockstep member"* |
| 124 | P3 Registry conformance | its own exit criteria, unchanged |
| 152 | Mutation Coordinator | the sole writer of `canon/**` |

These rows are downstream context, not hard dependencies of row 078, and no dependency graph is
created among them. 076 and 072 keep their families; 077 and 073 keep their structural carriers.
Each model's field-architecture and schema rows keep their fields, domains and schemas.

## 20. Roadmap Completion Trace

**BOUNDARY OBLIGATION SATISFIED** means the required boundary rule is stated, binding and bounded by
its sources. It does not claim that any schema, field definition, resolver, version mechanism or
validator exists, has run or has been tested.

| Row 078 | Status | Where |
|---|---|---|
| `Val`: *"definition resolves"* | **BOUNDARY OBLIGATION SATISFIED** — both families keep independent R Record identity; composition creates no schema-local or composite identity; a field name is not an identifier; resolution stays 114's and 115's | §11.3 |
| `Val`: *"versionable"* | **BOUNDARY OBLIGATION SATISFIED** — every version of either family stays inside its side of the split; no mechanism created or prevented | §11.4 |
| `Val`: *"references only declared entities (063)"* | **BOUNDARY OBLIGATION SATISFIED** — no reference required; any carried is R → R and obeys 063; applicability and domain targets declared; no domain or runtime instance; reference ≠ dependency | §7.4, §7.5, §11.5 |
| `Done`: *"a schema composes field definitions"* | **SATISFIED** — composition defined, one-way, not embedding, not a reference | §7; SF-078-02–SF-078-04 |
| `Done`: *"owns cardinality/required/order"* | **SATISFIED** — each assigned to the schema side, with its limits | §8; SF-078-05–SF-078-07 |
| `Done`: *"a field definition owns meaning and domain"* | **SATISFIED** — both assigned; domain not expanded by composition; distinct from applicability | §9; SF-078-08–SF-078-10 |
| `Done`: *"overlap resolved"* | **SATISFIED** — certified | §17 |
| `Why`: *"audit DG-03 closed here, not deferred"* | **SATISFIED** — closed, not deferred; the audit text is unavailable and recorded | §17; SC-078-C |
| `H: 076,072` | **SATISFIED** — both consumed unchanged | §5 |
| `S: —` | **PRESERVED** — no soft dependency added | §4 |
| `LS: LS-1` | **PRESERVED** — label kept; no pair invented | SC-078-O |
| `G: —` | **PRESERVED** — no gate introduced | SC-078-C |
| `→ 108` | **HANDED OFF** — 108's `Val` and `Done` unchanged | §19 |
| `Req: RR-17,RR-27` | **CARRIED** — text unavailable (GAP-C) | SC-078-Q |

---

*Artifact 078 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. A Registry boundary contract between the `SCHEMA-DEFINITION` and
`FIELD-DEFINITION` families, not a Registry Record: it creates no Record, defines no structural
schema, adds no element to Artifacts 073 or 077, and implements nothing. Where it differs from the
Master Blueprint, the Record Model System, the OS File Build Roadmap, or Artifacts 076 and 072,
those sources are correct and this document is wrong.*
