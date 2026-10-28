# COOLBOY12 — CONTROLLED-VOCABULARY Specification

**Artifact 081** · CONTROLLED-VOCABULARY spec · `docs/registry/controlled_vocabulary.md` · Own: R ·
RM: R · T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining · Canon: canonical-about-meaning ·
CD: yes · Ph/St: P3/3b · Req: RR-16 · BP: §9.4 · RMS: §10.1 · H: 064 · S: — · LS: LS-1 · G: — ·
→ 082 · Val: definition resolves; versionable; references only declared entities (063) · Done:
per-kind value sets may diverge; forced enum union prohibited · Why: §9.4's explicit rule ·
Risk: medium · ∥: yes

> **Effective status of this file.** The line above transcribes Roadmap row 081 field by field, as
> Artifact 003 requires (§0). Its `Canon: canonical-about-meaning` and
> `CD: yes` are copied manifest values; they do not make this Markdown file a Registry Record. It
> is an AUTHORITATIVE architecture specification under `docs/**`, authored before canonical
> materialization as Roadmap §0.8 provides. It holds no canonical data, no vocabulary and no
> value, and licenses no canonical write (SC-081-J).

## 0. Roadmap Identity and Constitutional Status

Row 081 of the repaired Roadmap held in this repository, reproduced field by field:

| Field | Exact value |
|---|---|
| ID | 081 |
| Name | CONTROLLED-VOCABULARY spec |
| Path | `docs/registry/controlled_vocabulary.md` |
| Own | R |
| RM | R |
| T | doc |
| R | ARCH |
| SoT | AUTHORITATIVE |
| Auth | defining |
| Canon | canonical-about-meaning |
| CD | yes |
| Ph/St | P3/3b |
| Req | RR-16 |
| BP | §9.4 |
| RMS | §10.1 |
| H | 064 |
| S | — |
| LS | LS-1 |
| G | — |
| → | 082 |
| Val | definition resolves; versionable; references only declared entities (063) |
| Done | per-kind value sets may diverge; forced enum union prohibited |
| Why | §9.4's explicit rule |
| Risk | medium |
| ∥ | yes |

This document is the AUTHORITATIVE specification of the `CONTROLLED-VOCABULARY` Registry definition
family. It is authoritative about that family's meaning and about no World Truth, no model's Records
and no concrete vocabulary. It is:

- **not a Record.** It carries no envelope, no `object_id`, no provenance and no `registry_ref`, and
  it creates no `CONTROLLED-VOCABULARY` Record.
- **not the family's schema.** How a `CONTROLLED-VOCABULARY` Record is structurally represented is
  Artifact 082's (`docs/registry/controlled_vocabulary.schema`, `H: 081`) — row 082's path in the
  repository Roadmap, as §0.8 set it (SC-081-P).
- **not a vocabulary.** It lists no value of any vocabulary — no `status` value of any Kind, no
  anchor category, no diagnostic phrase, no reader archetype.
- **not an implementation.** It defines no enum, validator, resolver, store or service.
- **not a canonicalization source.** Roadmap §0.8 names those — rows 075, 085, 105, 106, 107 — and
  row 081 is not one of them.

`Req: RR-16` is carried exactly; its text is not available (SC-081-I).

**Evidence classes.** Statements that matter are labelled by where they come from:

| Class | Meaning |
|---|---|
| **SOURCE FACT** | stated by the Blueprint, the RMS, the Roadmap or an upstream artifact |
| **REQUIRED SYNTHESIS** | a conclusion that several source facts force together; not a quotation |
| **SOURCE GAP** | not established by current sources, and not filled here |

**Evidence levels.** How far an obligation has been carried is a separate question:

| Level | Meaning | For this family |
|---|---|---|
| **SPECIFIED** | this document states the obligation | §4–§11 |
| **SOURCE-CHECKED** | its quotations and row metadata were compared with the repository's copies of the sources | the header, §0 and every `*"…"*` quotation, by the author's mechanical comparison; other claims by authoring review. Author-reported: no verification record is kept in the repository |
| **MECHANISM** | a structural contract or implementation row supplies it | **pending** — 082, 108–115 and 117 do not yet exist |
| **DEMONSTRATED** | an executable test or a run shows the behaviour | **pending** — 112, 116, 120–124 |

The levels do not imply one another, and none is approval. SPECIFIED is not implemented;
SOURCE-CHECKED is not approved; MECHANISM is not DEMONSTRATED; a DEMONSTRATED result would still
not be acceptance. A check this document reports as run is author-reported until a reviewer repeats
it; acceptance is a human record kept outside this file (§16, §18).

**Open decision.** One question this family depends on is answered by no current source: how a
vocabulary is associated with the field, Kind or other subject whose values it governs — its
cardinality, identity and reference (OD-081-1, §15.1). It is not a Roadmap `G` gate; row 081
carries `G: —`, and Artifact 003 says *"Do not invent gates."* Nothing here reports it as resolved,
and nothing here decides in advance whether it blocks any particular Artifact 082 design (§17).

Where this document differs from the Master Blueprint, the Record Model System or the Roadmap,
those sources are correct and this document is wrong.

## 1. Purpose

This specification answers one question — **how does the Registry define and govern controlled
value sets without forcing different Kinds or Record Models to share values that mean different
things or apply in different places?**

Blueprint §9.4 states the rule this document exists to carry:

> *"Shared structure, independent vocabulary."* A field's structure is shared across kinds; *"its
> value vocabulary is per-kind and may legitimately diverge"*. *"Divergent per-kind value sets are
> the intended design, not a defect to be unified"* — *"a forced enum union across kinds is
> prohibited"*.

Schematically, for World's `status` field:

```
FIELD-DEFINITION        what `status` means                      Registry (072–073)
        ┆
        ├┄┄ CHARACTER    its value set for CHARACTER Records      Registry — a CONTROLLED-VOCABULARY
        ├┄┄ ORGANIZATION its value set for ORGANIZATION Records   Registry — a CONTROLLED-VOCABULARY
        └┄┄ CONCEPT      its value set for CONCEPT Records        Registry — a CONTROLLED-VOCABULARY

the `status` value one Character Record carries                   World
```

The dotted lines are not references, not a dependency graph and not a schema: how a vocabulary is
associated with a field and a Kind is OD-081-1. No value of any of these sets is given here.

> **Primary invariant.** Per-Kind controlled value sets may diverge; a forced enum union across
> Kinds is prohibited. A shared field keeps one meaning; it does not oblige its Kinds to share one
> value set.

## 2. Scope and Non-Goals

**Artifact 081 owns** the family-level semantic contract of a `CONTROLLED-VOCABULARY`:

- what a `CONTROLLED-VOCABULARY` Record is, and what it governs (§4);
- the shared-structure, independent-vocabulary rule and the forced-union prohibition (§5);
- the obligation that a vocabulary's applicability be determinable, without inventing its form (§6);
- the boundary with field meaning, schema composition and subtype definition (§7);
- what Registry governs and what the owning Record Model keeps (§8);
- the identity, resolution, versionability and reference obligations of row 081's `Val` (§9–§10);
- the rules (§11), boundary matrix (§12), examples (§13), prohibited inferences (§14), source
  conditions (§15), conformance conditions (§16) and the handoff to 082 (§17).

**Artifact 081 does not own, and does not pre-build:**

| Not decided here | Owner |
|---|---|
| the Registry Kind taxonomy and the Kind's admission | 064 (`H`); 057 |
| the structural representation of a `CONTROLLED-VOCABULARY` Record | 082 |
| field meaning and domain; the field definition schema | 072; 073 |
| schema definition; its schema; the schema/field boundary | 076; 077; 078 |
| subtype definition and its schema | 070; 071 |
| who may propose, approve or deprecate a definition | 065 |
| definition evolution; versioning and pinning; supersession and deprecation | 108; 109; 110 |
| Registry dependency direction, asymmetry and cycles | 111 |
| the reference validator; the validation suite | 112; 116 |
| create/resolve/version operations; consumer resolution by id+version | 114; 115 |
| identity binding and Registry kind codes | 117 |
| concrete vocabulary content | 105, 107 and the other rows that author vocabularies (§17) |
| vocabulary growth rules for authoring surfaces | 450 |
| the VISUAL-ASSET subtype vocabulary; the epistemic vocabulary map | 350; 282 |
| Registry tests; P3 conformance | 120–123; 124 |
| the canonical gates; the sole canonical writer; commit atomicity | 145; 152; 153 |

**Non-goals.** No vocabulary, value, label, alias, ordering, default, value identifier, field
binding, Kind binding, enum, union rule, reference carrier, version mechanism, governance procedure,
validator, Record or fixture is created.

## 3. Governing Sources

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where stated
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done; §0.7 and §0.8 author rulings
        ↓
Artifact 064 (H)              the Kind and its admission answers, consumed unchanged
        ↓
Artifact 081                  the CONTROLLED-VOCABULARY family
```

| Source | What it gives this specification | Role |
|---|---|---|
| Roadmap row 081 | identity, `Val`, `Done`, `H: 064`, `LS: LS-1`, `→ 082` | build authority |
| **Artifact 064** (`docs/models/registry/kinds.md`) §6, §7, §14, §23 | Kind 7, its fourteen admission answers, F-1 to F-7, the mapping of rows 105–107 | **the only hard dependency** |
| Blueprint §9.4 | *"controlled value sets"*; shared structure, independent vocabulary; forced-union prohibition; architecture frozen, content extensible; the Registry holds no instances | constitutional |
| Blueprint §11.1; §12.15; §13.6; §13.6e; §13.7; §13.7c; §19.3; §33; §35 (O-8) | anchor categories as a Registry controlled vocabulary; the Canon Linter's `<kind>_type` check; `<kind>_type` vocabularies; *"What a value or term means"*; `status` World-owned; per-partition `status` vocabulary; the diagnostic phrases; extension at the Registry; the open Registry-expansion item | constitutional |
| RMS §4; §10; §10.1; §10.3; §11.1; §24; Appendix H PC-4 | `status` World-owned; Registry sovereign; fourteen Kinds; reference boundary; the VISUAL-ASSET subtype vocabulary; *"R defines the terms; E owns the states"* | constitutional |
| Roadmap §0.7; §0.8; rows 082, 105–107, 282, 350, 450, 065, 108–117, 124, 152 | authoring vs canonical materialization; downstream owners | build authority |
| Artifacts 061 (§7 row 9, §8), 062 (§6, §12), 063 (§7, §8, RB-1 to RB-6) | authority, layers, reference boundary | constraint, not `H` |
| Artifacts 070 (§11, SC-070-E), 072 (§12, FD-10, FD-11, SC-072-H), 076 (§17 C, F), 078 (§10.2, SC-078-H) | the neighbouring families' boundaries with this one | constraint, not `H` |
| Artifact 075 (§2.7) | the authored `KIND-DEFINITION` member for this Kind | context, not `H` (SC-081-F) |
| Artifacts 003, 033, 052 | conventions; the envelope; Registry canonicality | context, not `H` |
| Revolving Resolution Note | GAP-C; CONFLICT-F | a record of build resolutions, never authority |

**Precedence.** Blueprint and RMS govern; where earlier Blueprint wording and a later explicit RMS
correction differ, the correction governs (SC-081-A, SC-081-H, SC-081-N). The Roadmap governs
decomposition and order. Artifact 064 is consumed unchanged. Reading a supporting artifact does not
promote it into `H`.

Citations are to the repository copies in `docs/sources/`: the Blueprint is
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md`, the RMS `COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`, the
Roadmap `COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`. The Roadmap copy carries two author
revisions the original upload lacks, §0.7 and §0.8; every Roadmap citation here, row 082's path
included, is to the repository copy (SC-081-P).

## 4. The CONTROLLED-VOCABULARY Definition Family

### 4.1 Inherited from Artifact 064

Artifact 064 §14 is the Kind-level boundary this family stays inside. It is consumed unchanged.

| 064 §14 | Inherited fact |
|---|---|
| responsibility | §13.6e: *"What a value or term means"*; row 081: *"per-kind value sets may diverge; forced enum union prohibited"* |
| Q1 | *"a governed set of values or terms and their meaning"* |
| Q2 | *"what does this value or term mean, for this Kind?"* |
| Q3 | *"value sets are per-kind and may diverge, so each set is a distinct governed object"* |
| Q4 | persistent state is *"one vocabulary's values and their meaning; content is 081's"* |
| Q5 | Registry-owned definition evolution; per-Kind lifecycle detail is 108–110's (F-4) |
| Q6 | *"Registry governs the vocabulary; the model decides which value its Records carry"* |
| Q7 | what references it is *"not established"* |
| Q8–Q12 | not a field, not a state (`status` stays World-owned), not a relationship, not a subtype, not a projection |
| Q13 | reduction target `FIELD-DEFINITION`, rejected: *"one field definition cannot carry several divergent value sets without the forced enum union §9.4 prohibits"* |
| Q14 | without the Kind, terms are defined in several places and diverge, or are forced into one union |

Q2 reads "for this Kind". Some vocabularies the sources name are not scoped to a Kind's field —
anchor categories, diagnostic phrases, reader archetypes (§6). This document does not rewrite Q2; it
reads it as the Kind-scoped case of the family and records the wider scopes the sources show
(SC-081-F).

These quotations were compared with Artifact 064 as it stands in the repository. That establishes
what 064 says, not its review or approval status, which is a human record (§18).

### 4.2 What a CONTROLLED-VOCABULARY is

**SOURCE FACT.** A Registry definition is a semantic-definition Record — *"not configuration, not
code constants, not metadata, not a catalog, not runtime"* (RMS §10). Its category is *"Semantic
definition"*: *"What a value or term means"* (Blueprint §13.6e). The Registry holds *"controlled
value sets"* (§9.4).

**Definition.** A `CONTROLLED-VOCABULARY` is an R-partition Registry Record that governs one
vocabulary: a set of values or terms, what each means, and where the set applies. It is
authoritative about that meaning. It holds no Record that carries one of its values, and executes
nothing.

| Level | What it is | Owner |
|---|---|---|
| the Kind `CONTROLLED-VOCABULARY` | Kind 7 of RMS §10.1's fourteen | Registry, by its Kind architecture (064) |
| a `CONTROLLED-VOCABULARY` Record | the governed definition of one vocabulary, with its own identity | Registry |
| the vocabulary it defines | its values or terms, what each means, and its applicability | defined by the Record; not a separate owner |
| a value or term of it | one member of that governed set | defined by the Record |
| a field whose values it governs, where there is one | a field with its own meaning and domain | Registry, by `FIELD-DEFINITION` (072) |
| the value a Record actually carries | data of that Record | the Record's own model (§13.6e; 064 Q6) |

**What a `CONTROLLED-VOCABULARY` is not.** Not a field definition, a schema, a subtype definition, a
constraint or a validation rule; not an enum compiled into code; not a free-text list; not a state
of any Record; not a lifecycle; not a Record of any model other than R; not the Records that use it.

### 4.3 What every CONTROLLED-VOCABULARY answers

**SOURCE FACT + REQUIRED SYNTHESIS** from 064 Q1–Q4, §13.6e and §9.4:

1. **its values or terms** — the governed set (064 Q1, Q4); a set, so its members are distinct;
2. **what each value or term means** — values are not meaningless strings (§13.6e: *"What a value
   or term means"*; 064 Q2, Q4);
3. **its applicability** — where the set applies, determinably, so that value sets which may diverge
   stay apart (§9.4; 064 Q3; §6.2).

These three are semantic obligations of every Record of the family. They are not a field inventory:
how each is carried — which elements, names, shapes or notations — is Artifact 082's, within this
specification (§17).

**One vocabulary per Record.** 064 Q3 makes each per-kind value set *"a distinct governed object"*,
and Q4 gives a Record *"one vocabulary's values"*. REQUIRED SYNTHESIS: one `CONTROLLED-VOCABULARY`
Record governs one vocabulary; it is not a container of several independently governed sets, and
not a catalog of every value in the system.

That synthesis fixes the unit of Registry definition identity: one `CONTROLLED-VOCABULARY` Record,
one governed vocabulary definition. It does not establish how many fields, Kinds, partitions,
subtypes or other subjects may be associated with that vocabulary, nor how many vocabularies any
such subject may use. 064 Q3 and Q4 establish what one governed object is; neither states how many
subjects one vocabulary may serve or how many vocabularies one subject may use, and no inspected
source states an association cardinality (SC-072-H; SC-078-H). Those questions remain OD-081-1.
One vocabulary per Record does not imply one field, or one Kind, per vocabulary.

**Value-level semantics beyond meaning.** A vocabulary's own governing source may give its values
more than a meaning — row 106's *"five signal classes with their differing authority"*, for example.
No current source gives every vocabulary such attributes, and none is made universal here (SC-081-E,
SC-081-F).

## 5. Shared Structure and Independent Vocabulary

### 5.1 Source facts

- Blueprint §9.4: *"Shared structure, independent vocabulary. A field's structure is shared across
  kinds; its value vocabulary is per-kind and may legitimately diverge. `status` means the same kind
  of thing everywhere and enumerates different values for a `CHARACTER`, an `ORGANIZATION`, and a
  `CONCEPT`. Divergent per-kind value sets are the intended design, not a defect to be unified"* —
  *"a forced enum union across kinds is prohibited"*.
- Blueprint §13.6: *"The vocabulary of each `<kind>_type` is Registry-owned and per-kind, and per
  §9.4 those vocabularies may legitimately diverge between kinds — a forced union across kinds is
  prohibited."*
- Row 081 `Done`: *"per-kind value sets may diverge; forced enum union prohibited"*. Artifact 061 §7
  row 9: Registry never infers *"a forced union across kinds"*.

### 5.2 What a forced enum union is

**REQUIRED SYNTHESIS.** A forced enum union is a single enumeration assembled from the value sets of
several Kinds and imposed on each of them, so that a value belonging to one Kind's set becomes
admissible for another Kind only because the two share a field. If CHARACTER's `status` set held
values *a* and *b*, and ORGANIZATION's held *b* and *c* (schematic letters, not values), a forced
union would make *c* admissible for a Character and *a* for an Organization. That is prohibited.

What the prohibition does not say:

- it does not require two Kinds' sets to differ — sets *may* diverge; identical sets are not a
  defect either;
- it does not forbid a value spelled the same way in two sets; spelling is not shared meaning
  (§8; I-103);
- it does not settle whether two Kinds may use one vocabulary Record when their sets are genuinely
  the same — that is part of OD-081-1;
- it does not decide whether a field's values must come from a vocabulary at all — that is the
  field's, the schema's and the model's question, not this family's (§7).

### 5.3 Divergence is design

A field definition keeps one meaning across the Kinds that carry the field (072 §12). The value sets
are not part of that meaning, and nothing pools them: 064 Q13 rejects carrying divergent sets in one
field definition because that would be *"the forced enum union §9.4 prohibits"*. Divergence between
Kinds is therefore never a schema defect, a data-quality finding or an inconsistency to be repaired.

## 6. Applicability and Scope Boundaries

### 6.1 Scopes the sources show

**SOURCE FACT.** The sources name vocabularies at several scopes:

| Scope | Source | Example (no value given) |
|---|---|---|
| a field's values for one Kind | Blueprint §9.4 | World `status` for CHARACTER, ORGANIZATION, CONCEPT |
| a Kind's classification | Blueprint §13.6 | the `<kind>_type` vocabulary of a Kind |
| one partition's values | Blueprint §13.7c: *"legitimately per-partition"* | a state vocabulary that cannot admit `CANON` where a model never reaches it |
| a Kind's production forms | RMS §11.1: *"Production forms are a Registry-governed subtype vocabulary, not Kinds"*; PC-4 | the VISUAL-ASSET subtype vocabulary, row 350 |
| a set of categories | Blueprint §11.1: *"The set is a Registry controlled vocabulary (Section 9.4), extensible by ordinary Registry change, not by amendment."* | anchor categories |
| a set of governed phrases or archetypes | rows 105 and 107; 064 §23 | §19.3's diagnostic phrases; §20.1's four readers |
| a model's terms | Artifact 061 §8, RMS §24 | epistemic terms; row 282's epistemic vocabulary map |

### 6.2 The obligation

**REQUIRED SYNTHESIS.** Because value sets may diverge by Kind and by partition (§9.4; §13.7c), a
vocabulary is meaningful only together with where it applies: two sets that may differ must be
distinguishable by their applicability, not only by their values. Every `CONTROLLED-VOCABULARY`
therefore makes its applicability determinable (§4.3 item 3): the scope it governs is never left
ambiguous.

**A semantic obligation, not a schema element.** Applicability is an obligation of the
`CONTROLLED-VOCABULARY` definition family, not a prescribed element. This specification requires no
element named `applicability`, no particular reference carrier and no fixed association
cardinality. 081 fixes what must be knowable; 082 fixes how the schema represents it, subject to
source authority; neither may invent a general association rule to complete the representation.
The obligation is checkable at the contract level: for a vocabulary a representation carries, the
scope it governs can be determined without assuming an association cardinality or reference rule
the sources do not state. Where a representation can show that scope only by assuming such a rule,
that part rests on OD-081-1 and is not source-established.

**Vocabulary-side, not consumer-side.** The obligation runs from the vocabulary: given a vocabulary
definition, the scope it governs can be determined. It does not by itself establish the reverse — a
general mechanism by which a consuming Record, field, Kind or partition selects the vocabulary that
governs it — and none is defined here. A source may require a consumer-side check for a particular
field: Blueprint §12.15 lists *"`<kind>_type` legality against its kind"* among the Canon Linter's
structural rules, and §13.6 speaks of *"The vocabulary of each `<kind>_type`"* as per-kind, so there
the legal values must be determinable from the consuming Record's Kind. That check is the Linter's,
not this family's. How it locates the vocabulary, and by what reference, is not stated, and that
one field's case sets no rule for other fields or subjects; both remain OD-081-1.

- **Not narrowed to Kinds.** The family is not confined to per-Kind field values; §6.1's other
  scopes are source-established.
- **Not a closed list of scopes.** §6.1 records what the sources show. It is not a scope taxonomy,
  and no new scope is admitted or excluded by it.
- **Not universal.** No vocabulary applies to every Kind or every model by default, and no universal
  vocabulary, enum, lifecycle or status set is defined (RMS §4).
- **Declared entities only.** Where applicability names a Record Model or a Kind, it names a
  declared one (§10 RF-081-1).

How applicability is represented — whether as a declared Model and Kind, a field, a combination or
something else — is 082's, within §17's boundary. What a vocabulary is associated with as a general
rule — a field, a Kind, a field within a Kind or another subject — with what cardinality, how many
vocabularies a subject may have, and by what reference, is OD-081-1.

### 6.3 `status` beyond World

RMS §4: *"tier and status are NOT universal envelope fields"*; both are World-owned, and *"other
models define their own state vocabularies"*. Blueprint §13.7c calls a `status` vocabulary
*"legitimately per-partition"*. REQUIRED SYNTHESIS, with RMS §4 governing (SC-081-N): no `status`
field exists outside World because of this family; another model's state vocabulary is that model's
own, and a `CONTROLLED-VOCABULARY` governs it only where that model's sources establish one.

### 6.4 Row 106

Row 106 names *"five signal classes with their differing authority"* and lists 081 in `H`. Artifact
064 §23 records its representation as not established: *"`H: 081` is a dependency, not a
representation"*. This document does not map row 106 onto this family (SC-081-F).

## 7. Relationship to FIELD-DEFINITION, SCHEMA-DEFINITION and SUBTYPE-DEFINITION

**SOURCE FACT.** RMS §10.1 lists `FIELD-DEFINITION` (Kind 4), `SCHEMA-DEFINITION` (Kind 5),
`SUBTYPE-DEFINITION` (Kind 3) and `CONTROLLED-VOCABULARY` (Kind 7) as separate Kinds. §13.6e places
field and subtype definitions under *"Structural definition"* and this family under *"Semantic
definition"*. Blueprint §9.4: *"Schema defines the structure of a record — fields, types,
required-ness, defaults."*

| Concern | Owner | Not this family |
|---|---|---|
| what a field means, over what domain | `FIELD-DEFINITION` (072 FD-10) | — |
| whether a field occurs in a structure, is required, how many values it carries, its default | `SCHEMA-DEFINITION` (076; 078; §9.4) | a vocabulary sets no requiredness, occurrence count or default |
| what is true of one specialization of a Kind | `SUBTYPE-DEFINITION` (070) | a vocabulary value naming a specialization does not define it |
| a governed set of values or terms and what each means, where it applies | `CONTROLLED-VOCABULARY` | — |
| the value one Record carries | that Record's model | — |

Consumed unchanged from the neighbouring families:

- **Field.** *"A field whose values differ by Kind keeps one meaning; its value sets are not part of
  its definition"* (072 §12). No cardinality, identity or reference relation between a field
  definition and a vocabulary is established (SC-072-H; SC-078-H). That gap is handed to this
  family; this family cannot close it from the sources and records it as OD-081-1.
- **Schema.** A schema → vocabulary relation is not established; an admissible category is not a
  family relation (076 §17 F). A default value is schema-side (§9.4), never a vocabulary's.
- **Subtype.** For VISUAL-ASSET the production forms are a vocabulary (PC-4) built on both 071 and
  082 (row 350). No pairing between subtype definitions and vocabulary values is established
  (SC-070-E); row 350 owns that combination.

No universal vocabulary-reference field, one-vocabulary-per-field rule, one-vocabulary-per-Kind
rule, field-to-vocabulary map, enum inheritance, override or composition algorithm, cross-Kind union
rule, default vocabulary or global value namespace is defined.

## 8. Registry Authority and Model Sovereignty

**SOURCE FACT.** Artifact 061 §7 row 9: Registry governs *"the vocabulary definition
(`CONTROLLED-VOCABULARY`), which may diverge per kind"*; the owning model governs *"which value its
Records carry"*; Registry never infers *"ownership of the consuming Record; a forced union across
kinds"*. 064 Q6: *"Registry governs the vocabulary; the model decides which value its Records
carry"*. RMS §24: *"R defines the terms; E owns the states"*.

```
Registry       defines the vocabulary: its values, their meaning, its applicability
   ↓ used by
owning model   decides which value its Records carry, and what that state means for it
   ↓
its Records    carry the value
```

- **No ownership transfer.** Defining a value set for a Kind gives the Registry no Record of that
  Kind, no World Truth and no say over which value a given Record carries.
- **No shared state semantics.** Two models whose vocabularies contain similarly spelled values do
  not thereby share state semantics: *"A mechanism may be shared across Record Models; a semantic
  may not be shared without evidence in each model that carries it."* (I-103).
- **Authoritative about meaning.** A vocabulary is canonical about meaning once committed, never
  about the world (Blueprint §13.7c: Registry *"Yes, about meaning"*).
- **No instances.** *"The Registry holds no instances."* — *"A registry entry that names a specific
  thing in the world is a misfiled Record."* (§9.4). A vocabulary value is a governed term, never a
  Record of any model.

## 9. Identity, Resolution and Versionability

Row 081 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-081-1** | A `CONTROLLED-VOCABULARY` is a Registry Record with independent identity (064 Q3; F-1). Once materialized it carries ordinary Record identity under the universal grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` and the seven-field envelope — `partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4, §5). No eighth field. |
| **RS-081-2** | That identity is the R Record's own. It is not a value's spelling, a vocabulary's name, a field's name, a Kind's name or a consuming Record's identity. The slug is decoration only (RMS §5). No kind code or `object_id` is minted. |
| **RS-081-3** | A consumer must be able to resolve a materialized vocabulary definition — by the definition's identity (row 115: *"consumer resolves by id+version"*), which is not selection of a vocabulary from a consuming context (§6.2). Create, resolve and version are row 114's; consumer resolution by id+version row 115's; identity binding row 117's. No resolver, lookup or registration is defined here, and resolvable ≠ legal (063 §11). |
| **RS-081-4** | Resolving a vocabulary returns a definition. It sets no value in any Record, validates no Record and transfers nothing. |

Row 081 `Val`: *"versionable"*.

| ID | Obligation |
|---|---|
| **VS-081-1** | A `CONTROLLED-VOCABULARY` participates in governed Registry definition evolution under rows 108–110 (064 F-4). Its temporal account is the Registry's, *"temporal account without a World History Record"* (row 108). |
| **VS-081-2** | **Content is extensible.** *"Registry architecture is frozen; Registry content is extensible."* The content — including *"controlled values"* — *"extends by ordinary Registry change, at any time, without touching this blueprint"* (§9.4). A governed change may add or refine a vocabulary's values without a Blueprint amendment; §33 records that *"adding or refining a definition changes meaning below it"*. Whether a value may be withdrawn, and how, is not established here (SC-081-E; 110). |
| **VS-081-3** | **Extensible ≠ ungoverned.** A change to a vocabulary is a Registry definition change, made through Registry governance (065), evolution and versioning (108–110) and, for authoring surfaces, row 450's growth rules (*"new terms enter through a governed vocabulary, not ad hoc"*). None of those procedures is defined here. |
| **VS-081-4** | **Not defined here ≠ forbidden.** No version field, syntax, numbering, supersession link, value-level deprecation, migration or compatibility rule is defined, and none is prevented. Changing a vocabulary does not by itself rewrite or revalidate any Record that carries one of its values; any consequence is 108–110's and the owning model's. Three things stay apart: that the definition is versionable (this document); the versioning mechanism — how versions are identified, stored, resolved, pinned or superseded (108–110, 114, 115); and the semantic-compatibility policy — how a change of meaning bears on existing consumers, which rows 109 (*"consumers pin a version"*) and 110 (*"history of meaning is preserved"*) address. No compatibility guarantee, migration duty or automatic revalidation is created here. |

## 10. Reference Legality

Row 081 `Val`: *"references only declared entities (063)"*. RMS §10.3: *"Registry MAY reference:
other Registry definitions · declared Record Models · declared Kinds · declared schemas · declared
semantic contracts."* · *"Registry MAY NOT: own domain instances · depend on runtime instances ·
mutate domain instances · use domain instances as semantic authority."* Artifact 063: vocabularies
are not a target category of their own; *"those are reached as Registry definitions (row 1)"*.

| ID | Rule | Basis |
|---|---|---|
| **RF-081-1** | **Applicability names declared entities.** Where a vocabulary's applicability names a Record Model or a Kind, it names a declared Model, or a declared Kind of its declared owning Model whose declared status that model's Kind architecture establishes. Naming it is a declaration reference to the Model or Kind itself, not a reference to a `MODEL-DEFINITION` or `KIND-DEFINITION` Record, and admits nothing. An undetermined target is not legal: *"Undetermined is not permitted."* This classifies the statement; a carrier 082 chooses is classified by 082. | RMS §10.3; 063 §7 rows 2–3, §8.2, §8.3, RB-1, RB-6; 057 §9 |
| **RF-081-2** | **No domain instance.** No Record of W, E, P, V or I is a value, a scope, a target or the semantic authority of a vocabulary. A vocabulary is not defined as *the values Character Maximus uses*. | RMS §10.3; §9.4; 063 §7 row 6 |
| **RF-081-3** | **No domain state.** No current value carried by any model's Records is the authority for a vocabulary's content; a vocabulary is not *whatever statuses Characters currently have*. | 063 §7 row 7 |
| **RF-081-4** | **No runtime instance.** No validator, enum class, service or session is a target, dependency or authority. | RMS §10.3; 063 §7 row 8 |
| **RF-081-5** | **Values are not references.** A value or term is a member of the governed set; it is not a reference to a Record, a Kind or a definition merely because it is spelled like one. | §4.2; 063 RB-1 |
| **RF-081-6** | **Admissible category ≠ family relation.** Other Registry definitions are admissible targets. That establishes no concrete relation: no vocabulary → field, vocabulary → schema, vocabulary → subtype or vocabulary → vocabulary relation is created here, and none is forbidden later (OD-081-1). | 063 RB-5, §22; SC-072-H; SC-078-H; SC-070-E |
| **RF-081-7** | **Reference ≠ dependency.** A reference does not by itself establish a semantic dependency. The family's layer placement is not established (062 §6), so no layer-based dependency rule is applied; concrete dependency rules are row 111's. | 062 D-9; 063 RB-5; row 111 |
| **RF-081-8** | **Resolvable ≠ legal; no transfer.** A target that resolves may still be illegal. A legal reference transfers no ownership, mutation authority, semantic authority, admission, canonicality or source-of-truth class. | 063 §11, §12 |

The Blueprint's older wording — *"A Registry definition may never reference a kind, a subtype, or an
instance"* — is not current law for reference legality; RMS §10.3 corrects it (SC-081-H). Domain
instances stay forbidden. What references a `CONTROLLED-VOCABULARY` is *"not established"* (064 Q7);
nothing here creates an inbound reference.

## 11. Normative Rules

The IDs below are this specification's, not pre-existing constitutional identifiers.

| ID | Rule | Basis | Evidence |
|---|---|---|---|
| **CV-081-01** | **Registry Kind.** A `CONTROLLED-VOCABULARY` is an R Registry definition Record of Kind 7 of RMS §10.1's frozen fourteen. No Kind is created, renamed or merged. | RMS §10.1; 064 §6, §14 | SOURCE FACT |
| **CV-081-02** | **Authoritative about meaning.** A vocabulary definition is authoritative about what its values or terms mean, never about the truth of any domain Record. | RMS §10; §13.7c; 064 F-5 | SOURCE FACT |
| **CV-081-03** | **One vocabulary.** Each Record governs one vocabulary — one governed set of values or terms; it is not a catalog of several independently governed sets. This fixes the unit of definition identity, not association cardinality: how many fields, Kinds, partitions, subtypes or other subjects one vocabulary serves, and how many vocabularies one subject uses, is OD-081-1. | 064 Q1, Q3, Q4 | REQUIRED SYNTHESIS |
| **CV-081-04** | **Values with meaning.** Each value or term of a vocabulary has a stated meaning; values are not bare strings. | §13.6e; 064 Q1, Q2, Q4 | SOURCE FACT + REQUIRED SYNTHESIS |
| **CV-081-05** | **Independent value sets.** Value sets may differ between the Kinds a vocabulary family serves. Divergence is the intended design, not a defect. | §9.4; §13.6; row 081 `Done` | SOURCE FACT |
| **CV-081-06** | **No forced union.** A field shared across Kinds never forces the union of their value sets into one enumeration imposed on each. | §9.4; §13.6; row 081 `Done`; 061 §7 row 9 | SOURCE FACT |
| **CV-081-07** | **Shared structure stays possible.** Independent value sets require no duplication or split of the shared field's meaning. | §9.4; 072 §12 | SOURCE FACT + REQUIRED SYNTHESIS |
| **CV-081-08** | **Applicability determinable.** Where every vocabulary applies is determinable, so that sets which may diverge stay distinguishable. This is a semantic obligation, not a prescribed element: no element named `applicability`, no reference carrier and no association cardinality is required (§6.2). It is vocabulary-side: it establishes no general mechanism for selecting a vocabulary from a consuming context. The family is not narrowed to per-Kind field values, and no closed list of scopes is defined. | §9.4; §13.7c; §11.1; RMS §11.1; rows 105, 107 | REQUIRED SYNTHESIS |
| **CV-081-09** | **Nothing universal.** No universal vocabulary, enum, `status` set, lifecycle, Kind taxonomy or semantic schema is defined; no vocabulary applies to every Kind or model by default. | RMS §4; §13.7a; I-106 | SOURCE FACT |
| **CV-081-10** | **Model sovereignty.** Registry governs the vocabulary; the owning model decides which value its Records carry and owns those Records. | 061 §7 row 9; 064 Q6; §13.6e; I-105 | SOURCE FACT |
| **CV-081-11** | **No shared semantics by spelling.** Similarly spelled values in vocabularies of different Kinds or models share no meaning by that fact. | I-103; §5.2 | REQUIRED SYNTHESIS |
| **CV-081-12** | **Distinct from neighbours.** A vocabulary is not a `FIELD-DEFINITION`, `SCHEMA-DEFINITION` or `SUBTYPE-DEFINITION`, and none of those is a vocabulary; requiredness, occurrence and defaults are schema-side. | RMS §10.1; §9.4; 064 Q13; 070 §11; 072 §12 | SOURCE FACT |
| **CV-081-13** | **No invented association.** No cardinality, identity or reference rule between a vocabulary and a field, Kind, partition, subtype, schema or other subject is defined beyond what the sources state (OD-081-1). Neither CV-081-03 nor CV-081-08 supplies one. | SC-072-H; SC-078-H; SC-070-E | SOURCE GAP |
| **CV-081-14** | **Reference legality.** Every reference the family carries obeys Artifact 063; applicability names declared entities only; no domain instance, domain state or runtime object is a target or authority. | RMS §10.3; 063; §10 | SOURCE FACT |
| **CV-081-15** | **No instances.** A vocabulary value is a governed term, never a domain Record; it is content of the vocabulary Record, not a Registry Record of its own. | §9.4; RMS §10.3; 064 Q3, Q4 | SOURCE FACT + REQUIRED SYNTHESIS |
| **CV-081-16** | **Independent identity.** The definition has its own R Record identity under the universal grammar and envelope, distinct from any value, field, Kind or consuming Record. | RMS §4, §5; RS-081-1, RS-081-2 | SOURCE FACT |
| **CV-081-17** | **Resolvable, not resolved here.** A materialized definition must be resolvable by consumers, by its identity; resolution is 114's and 115's. | row 081 `Val`; rows 114, 115 | SOURCE FACT |
| **CV-081-18** | **Versionable.** The definition evolves under rows 108–110, not by mechanics invented here. | 064 F-4; rows 108–110; VS-081 | SOURCE FACT |
| **CV-081-19** | **Content extensible under governance.** Values may be added or refined by ordinary, governed Registry change, without amendment; extensibility licenses no ungoverned change. | §9.4; §11.1; §33; rows 065, 108–110, 450 | SOURCE FACT |
| **CV-081-20** | **No execution.** A vocabulary validates, rewrites or sets no value in any Record and is no runtime enum. | RMS §10; §9.4 | SOURCE FACT |
| **CV-081-21** | **Structural handoff.** Artifact 082 receives the semantic obligations of §17 and no mandatory field inventory. | row 082 | REQUIRED SYNTHESIS |

## 12. Boundary Matrix

| Concern | Owner | Source |
|---|---|---|
| that `CONTROLLED-VOCABULARY` is a Registry Kind | RMS §10.1; 064 | RMS §10.1 |
| what a vocabulary definition means and must answer | 081 | row 081 |
| its structural representation | 082 | row 082 |
| a vocabulary's concrete values | the row that authors it (e.g. 105, 107, 350, 282) | rows 105, 107, 282, 350 |
| what a field means | 072–073 | row 072 |
| whether a field occurs, is required, its count, its default | 076–078 | §9.4; row 078 `Done` |
| what a specialization of a Kind means | 070–071 | row 070 |
| the value a Record carries; its state semantics | the owning Record Model | §13.6e; 064 Q6; §13.7c |
| who may propose, approve or deprecate a vocabulary | 065 | row 065 |
| evolution, versioning, supersession, deprecation | 108–110 | rows 108–110 |
| growth rules for terms entering through authoring surfaces | 450 | row 450 |
| dependency direction and cycles | 111 | row 111 |
| reference validation; definition validation | 112; 116 | rows 112, 116 |
| create/resolve/version; consumer resolution | 114; 115 | rows 114, 115 |
| runtime enforcement of a field's allowed values | shared and model-owned validation, not this family | RMS §10.6, §20; Blueprint §12.15 |
| canonical commit of any vocabulary Record | 152, after G-CANON-R | Roadmap §0.8 |
| the field/vocabulary association | not established — OD-081-1 | §15.1 |

## 13. Worked Examples

Every example is **schematic**. No Record is created, no identifier minted, and no value given.

**A. Legal — Kind-specific divergence.** World's `status` field has one meaning. A vocabulary
applicable to CHARACTER and another applicable to ORGANIZATION each state their own values. The two
sets may differ, overlap or coincide; nothing makes them equal. Their contents are not given here
(§9.4; CV-081-05).

**B. Illegal — forced union.** A developer merges the CHARACTER, ORGANIZATION and CONCEPT `status`
sets into one universal enumeration because the field name is shared, so every value becomes
admissible for every Kind. **Prohibited** — *"a forced enum union across kinds is prohibited"*
(§9.4; CV-081-06).

**C. Legal — Registry and World apart.** Registry defines the CHARACTER `status` vocabulary and what
each value means. World owns every Character Record and decides which value each carries. Registry
owns no Character (061 §7 row 9; CV-081-10).

**D. Illegal — an instance as authority.** A vocabulary is defined as the set of values that the
Character Record `W-CH-000001-Maximus` currently uses, or cites that Record as what a value means.
**Forbidden**, however well the identifier resolves (RMS §10.3; 063 §7 rows 6–7; RF-081-2,
RF-081-3).

**E. Deferred — representation.** 081 requires that a vocabulary state its values and their
meaning, and that its applicability be determinable. Which elements carry them is not fixed by any
source. The semantic obligation is here; the structure is 082's, within §17 (CV-081-21).

**F. Legal — content growth.** A governed Registry change adds a value to a vocabulary. The frozen
architecture is untouched and no Blueprint amendment is needed (§9.4). The change goes through the
Registry's governance and evolution rows (065, 108–110); no approval step is defined here
(VS-081-3).

**G. Legal — a vocabulary that is not per-Kind.** Anchor categories are *"a Registry controlled
vocabulary"* (§11.1). Their applicability is not a Kind's field; the family covers them as it covers
per-Kind sets (CV-081-08).

**H. Legal — per-partition values.** A state vocabulary for a model that can never reach `CANON`
does not admit `CANON`: *"A `status` vocabulary admitting `CANON` in every partition would be false
in two of six"* (§13.7c). That model's vocabulary is its own; it is not World's `status` (RMS §4;
§6.3).

**I. Boundary — a subtype vocabulary.** VISUAL-ASSET's production forms are *"a Registry-governed
subtype vocabulary, not Kinds"* (RMS §11.1). The vocabulary lists them; each form's meaning as a
specialization is a `SUBTYPE-DEFINITION`'s. How the two relate is row 350's to build (SC-070-E).

**J. Boundary — signal classes.** Row 106's five signal classes list 081 in `H`, but their
representation is not established (064 §23). Treating them as a `CONTROLLED-VOCABULARY`, or as not
one, would decide what 064 leaves open; neither is done here.

**K. Illegal — a value naming a world thing.** A vocabulary value stands for one particular
Organization in the world. *"A registry entry that names a specific thing in the world is a misfiled
Record."* (§9.4; CV-081-15).

**L. Deferred — field binding.** Whether the CHARACTER `status` vocabulary is bound to the `status`
field, to the CHARACTER Kind, to both, or by some other association — and whether one vocabulary may
serve several fields or Kinds — is OD-081-1. No binding is chosen here.

## 14. Prohibited Inferences

| # | Invalid inference | Correct reading | Basis |
|---|---|---|---|
| PI-01 | A shared field name means identical allowed values | per-Kind sets may diverge | §9.4 |
| PI-02 | A shared field structure requires a universal enum | forced union prohibited | §9.4 |
| PI-03 | Different per-Kind values show an inconsistency | divergence is the intended design | §9.4 |
| PI-04 | A vocabulary definition owns the Records that use it | the model owns its Records | 061 §7 row 9; 064 Q6 |
| PI-05 | A legal target category makes every reference relation legal | category ≠ relation | 063 RB-5 |
| PI-06 | A resolvable reference is legal | resolvable ≠ legal | 063 §11 |
| PI-07 | Content extensibility permits ungoverned change | changes go through governance and evolution | §9.4; rows 065, 108–110, 450 |
| PI-08 | A controlled vocabulary is a hard-coded runtime enum | a governed Registry Record, *"not code constants"* | RMS §10 |
| PI-09 | Every vocabulary is attached to exactly one field | not established | OD-081-1 |
| PI-10 | Every Kind has exactly one vocabulary | not established | OD-081-1 |
| PI-11 | `CONTROLLED-VOCABULARY` creates a new Registry Kind | it is Kind 7 of fourteen | RMS §10.1 |
| PI-12 | 081 may implement 082 | the schema is 082's | row 082 |
| PI-13 | Versionability requires version syntax here | 108–110 own it | rows 108–110 |
| PI-14 | This file is a canonical Registry Record because its row carries `CD: yes` | copied metadata; an authored spec | Roadmap §0.8; 003; SC-081-J |
| PI-15 | Every vocabulary is per-Kind | per-partition, category and phrase vocabularies are source-established | §13.7c; §11.1; rows 105, 107 |
| PI-16 | A vocabulary applies to every Kind unless restricted | no vocabulary applies everywhere by default | RMS §4; CV-081-09 |
| PI-17 | Two Kinds whose sets coincide must share one Record | not established | OD-081-1 |
| PI-18 | Two Kinds must never share one vocabulary | not established either | OD-081-1 |
| PI-19 | A vocabulary sets a field's default or requiredness | schema-side | §9.4; 078 |
| PI-20 | A vocabulary value is a reference to the Record it names | values are terms, not references | RF-081-5; §9.4 |
| PI-21 | Similarly spelled values in two models share semantics | shared mechanism, not shared meaning | I-103 |
| PI-22 | `status` exists in every model because a status vocabulary is per-partition | `status` is World-owned | RMS §4; §6.3 |
| PI-23 | Row 106's signal classes are a `CONTROLLED-VOCABULARY` because they list 081 in `H` | a dependency, not a representation | 064 §23 |
| PI-24 | Every value carries the same attributes as row 106's classes | no universal value-level attribute set | §4.3; SC-081-E |
| PI-25 | An open decision is a Roadmap gate | open decisions are not `G` gates | row 081 `G: —`; 003 |
| PI-26 | One vocabulary per Record means one field, or one Kind, per vocabulary | definition identity, not association cardinality | §4.3; CV-081-03; OD-081-1 |
| PI-27 | Applicability requires an element named `applicability`, or a particular reference carrier | a semantic obligation; its form is 082's | §6.2; CV-081-08 |
| PI-28 | OD-081-1 cannot affect any 082 schema design or conformance claim | not decided here; assessed against the actual design | §15.1; §17 |
| PI-29 | A vocabulary whose applicability is determinable can be selected from any consuming context by a general mechanism | vocabulary-side determinability only; no general consumer-side selection is established | §6.2; OD-081-1 |
| PI-30 | A value's spelling is its identity or its meaning, so differently spelled values must mean different things | meaning is stated, not read from spelling; how values are identified is 082's | CV-081-04; CV-081-11; SC-081-E |
| PI-31 | Every value has a stated meaning, so a vocabulary must have at least one value — or, since nothing forbids it, may have none | neither follows; whether a vocabulary may be empty is not established | CV-081-04; SC-081-E |

## 15. Source-Condition Register

### 15.1 Open decision

#### OD-081-1 — how a vocabulary is associated with what it governs — OPEN

| | |
|---|---|
| **Question** | What is a vocabulary associated with — a field, a Kind, a field within a Kind, a partition, a subtype, a governance or authoring use? With what cardinality: one vocabulary per field per Kind, several, or one shared across fields or Kinds when their sets coincide? By what reference, if any? |
| **Sources** | Blueprint §9.4 (*"its value vocabulary is per-kind"*); §12.15; §13.6; §13.7c; RMS §11.1; rows 105, 107, 282, 350; 072 SC-072-H and 078 SC-078-H (no field/vocabulary relation established; the family is 081–082's); 070 SC-070-E; Artifact 075 §2.7 (*"used where the owning contracts establish it"*) |
| **Established** | vocabularies are distinct from fields, schemas and subtypes; per-Kind and per-partition sets may diverge; no forced union; every vocabulary's applicability is determinable from the vocabulary side (§6.2); one Record governs one vocabulary definition, which fixes definition identity and not association cardinality (§4.3); for `<kind>_type`, §13.6 speaks of *"The vocabulary of each `<kind>_type`"*, per-kind, and §12.15 checks its legality against the Record's Kind — one field's case, which states no reference and sets no rule for other fields or subjects |
| **Owner** | the Blueprint/RMS author for any general rule. No Roadmap row is assigned one. Absent a general rule, a concrete association belongs to the row that authors the vocabulary or the field, where a governing source establishes it — for example row 350 for the VISUAL-ASSET subtype vocabulary |
| **Cannot be treated as source-established** | any part of a design or check that requires an association rule the sources do not state: in 082, a field-binding or Kind-binding carrier whose shape presupposes a cardinality — one-per-field, one-per-Kind, shared (§17 Case C); in row 116, checking that a vocabulary's association is well formed against a rule this family does not have; in shared and model-owned validation (RMS §10.6, §20), checking a Record's value against "its" vocabulary by such a rule — where a source requires the check, as §12.15 does for `<kind>_type`, the check is that source's, and the rule by which it locates the vocabulary is still not stated |
| **Unaffected** | row 081's `Val` and `Done`; the per-Kind divergence and forced-union obligations; the obligations 082 takes under §17 Case A — all hold whatever the association |
| **Not decided here** | whether OD-081-1 blocks any particular 082 schema design or conformance claim against 082's `Val` and `Done`. OD-081-1 does not invalidate this specification's obligations, and 082 may carry work that does not depend on it; whether a given design depends on it is assessed against that design and 082's exit criteria, which are not changed (§17) |
| **Closes when** | an authoritative source states how vocabularies are associated with the subjects they govern, or a concrete row's governing source establishes it for that row; and the answer is cited where this document records the gap |

### 15.2 Source conditions

Each entry gives the sources, what is established, what remains undecided, whether 081 owns its
resolution, and whether it blocks row 081's `Val` or `Done`.

#### SC-081-A — Registry classification — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* RMS §10: *"Registry is a sovereign Record Model."* and *"COLLISION-1 — CLOSED"* (`AUTHOR-DECIDED`) |
| **Established** | the Registry is a sovereign Record Model; the §9.4 line is stale |
| **Treatment** | RMS §10 governs; the Blueprint is not edited |
| **Blocks?** | no |

#### SC-081-B — per-Kind divergence and forced union — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4; §13.6; row 081 `Done` |
| **Established** | per-Kind value sets may diverge; a forced enum union across Kinds is prohibited — a normative requirement, not a preference |
| **Blocks?** | no |

#### SC-081-C — exact representation — DEFERRED TO 082

| | |
|---|---|
| **Sources** | no inspected source prescribes the elements of a `CONTROLLED-VOCABULARY` Record |
| **Established** | the semantic obligations of §4.3 |
| **Undecided** | element names, shapes, value identification, ordering, notation |
| **Owner** | 082, within §17 — except what OD-081-1 holds open |
| **Blocks?** | row 081: no. A representation choice that depends on OD-081-1 is treated as §17 Case C states |

#### SC-081-D — association cardinality — SOURCE GAP

| | |
|---|---|
| **Sources** | as OD-081-1 |
| **Undecided** | one vocabulary per Kind or several; one per field or several fields sharing one; reuse across Kinds; the same questions for partitions, subtypes and other subjects |
| **Treatment** | recorded as OD-081-1 (§15.1); no cardinality is chosen; one vocabulary per Record (§4.3) is definition identity and does not settle it |
| **Blocks?** | row 081: no. Downstream: not decided here; as OD-081-1 states |

#### SC-081-E — value-level detail beyond meaning — SOURCE GAP

| | |
|---|---|
| **Sources** | none states any of these for vocabulary values in general. A default is schema-side (§9.4). Row 106 gives its classes *"differing authority"*, for that row only |
| **Established** | values are distinct members of a set with stated meaning (§4.3) |
| **Undecided** | how values are identified; labels; aliases; ordering; hierarchy; value-level deprecation; value-level provenance; whether a vocabulary may be empty |
| **Treatment** | none is made a universal requirement; how values are identified within a vocabulary is a representation question for 082, which may not make spelling an identity or a meaning across vocabularies (CV-081-11). CV-081-04's meaning obligation holds of each value present and settles nothing about whether there may be none: emptiness is neither admitted nor rejected here, and neither 082's structure nor row 116's well-formedness check may present either answer as source-established. An answer would come from the Blueprint/RMS author, or from a vocabulary's own governing source for that vocabulary |
| **Blocks?** | no |

#### SC-081-F — scope beyond per-Kind fields — ESTABLISHED, WITH ONE ROW UNMAPPED

| | |
|---|---|
| **Sources** | Blueprint §11.1, §13.6, §13.7c, §19.3; RMS §11.1, PC-4; rows 105, 107, 282, 350; 064 §14 Q2 (*"for this Kind"*), §23; Artifact 075 §2.7, whose `KIND-DEFINITION` member carries the same Kind-scoped wording (*"for the Kind it serves"*) |
| **Established** | the family covers per-Kind, per-partition, subtype, category and governed-phrase vocabularies (§6.1); rows 105 and 107 are controlled-vocabulary content (064 §23) |
| **Undecided** | whether row 106's signal classes are this family's content — 064 §23: not established |
| **Treatment** | 064 Q2 is read as the Kind-scoped case, not rewritten; 075 §2.7 is read the same way and not edited — whether its wording should name the wider scopes is a question for 075, reported, not resolved here; the family is neither narrowed to `status` nor given a closed scope list; row 106 is not mapped |
| **Blocks?** | no |

#### SC-081-G — content extensibility — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4 (architecture frozen, content extensible); §11.1; §33; rows 065, 108–110, 450 |
| **Established** | vocabulary content grows by ordinary, governed Registry change, without amendment |
| **Treatment** | no governance, approval, deprecation or migration procedure is defined (VS-081-3) |
| **Blocks?** | no |

#### SC-081-H — older Blueprint reference wording — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4: *"A Registry definition may never reference a kind, a subtype, or an instance"*; RMS §10.3: *"v0.1 stated the boundary too bluntly"*; Artifact 063 |
| **Established** | declared Models and Kinds may be named; domain instances may not |
| **Blocks?** | no |

#### SC-081-I — requirement text RR-16 — NON-BLOCKING, UNVERIFIED

| | |
|---|---|
| **Sources** | row 081 `Req: RR-16`; Revolving Resolution Note GAP-C (*"missing requirement register"*). A search of this repository found RR-16 only as a `Req` value and in artifacts that carry it; none defines it |
| **Treatment** | the ID is carried exactly; no text is stated, and no compliance with RR-16 is claimed |
| **Blocks?** | no — GAP-C records it as non-blocking |

#### SC-081-J — authored spec against canonical materialization — RECORDED

| | |
|---|---|
| **Sources** | row 081 `T: doc · Canon: canonical-about-meaning · CD: yes`; Artifact 003: *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`"*, and `CD` *"licenses nothing"*; Roadmap §0.8 (AD-REG-AUTHORING-SPLIT): *"P3 authors Registry family contracts, structural contracts and canonicalization source material outside `canon/**`; canonical Registry Records are committed only through 152, after G-CANON-R."* |
| **Condition** | the row gives a `docs/**` specification the `Canon` value Artifact 003 associates with Registry. The labels differ; §0.8 does not change them, and no source reconciles them |
| **Established** | by §0.8: this file is an authored family contract, not a Registry Record, and licenses no canonical write; vocabulary Records are committed only through row 152 after G-CANON-R |
| **Treatment** | the values are copied exactly and not normalized. Unresolved: whether row 081's `Canon` and `CD` should read as Artifact 003's convention does — the Roadmap author's. Route: ROADMAP / CONVENTION ISSUE |
| **Blocks?** | no |

#### SC-081-K — `LS: LS-1` on a family specification — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 081 `LS: LS-1`; Roadmap PART III: LS-1 *"every Kind spec ↔ its Registry KIND-DEFINITION"* and *"The Registry's own fourteen pairs are 064 ↔ 075"*; §0.7 (AD-LS1-R-BOOTSTRAP): *"Registry's own pairs are 064 ↔ 075"*; Artifact 003: *"A lockstep partner is not a predecessor."* |
| **Condition** | a family specification is neither a Kind specification nor a `KIND-DEFINITION`; Kind 7's LS-1 pair is 064 ↔ 075 (075 §2.7), which names neither 081 nor 082, though row 082 also carries `LS: LS-1` |
| **Treatment** | the label is preserved; no 081 ↔ 082 or other pair is invented (as 064 SC-064-J records for the non-roster rows) |
| **Blocks?** | no |

#### SC-081-L — layer placement — NOT ESTABLISHED

| | |
|---|---|
| **Sources** | Artifact 062 §6: the §9.4 rows *"do not place"* `CONTROLLED-VOCABULARY`; §12 lists controlled value sets outside the layers |
| **Treatment** | no layer is assigned and no layer-based dependency rule applied; concrete dependency rules are row 111's |
| **Blocks?** | no |

#### SC-081-M — unlocks against dependents — ROADMAP ISSUE, RECORDED

| | |
|---|---|
| **Sources** | row 081 `→ 082`; rows 082, 105, 106, 107 and 450 list 081 in `H`; row 082 `→ 347,400`, while row 347 carries `H: 346` and row 400 `H: 105,398`; rows 282 and 350 list 082 in `H` without appearing in 082's `→` |
| **Treatment** | an unlock is not a hard dependency, and neither list is rewritten |
| **Blocks?** | no |

#### SC-081-N — `status` beyond World — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | RMS §4 (`AUTHOR-DECIDED`): `tier` and `status` World-owned; *"other models define their own state vocabularies"*. Blueprint §13.7c: a `status` vocabulary is *"legitimately per-partition"*; §9.4's older RFS example uses `status` |
| **Established** | `status` is World's; other models' state vocabularies are their own (§6.3) |
| **Treatment** | RMS §4 governs; no `status` outside World and no universal state vocabulary is created |
| **Blocks?** | no |

#### SC-081-O — Blueprint O-8 — RECORDED

| | |
|---|---|
| **Sources** | Blueprint §35: *"Registry expansion — indicator semantics, controlled vocabularies"*, status OPEN |
| **Treatment** | this specification defines the family; it does not author vocabularies and does not close O-8 |
| **Blocks?** | no |

#### SC-081-P — the Roadmap copy, its §0.7 and §0.8, and row 082's path — CLOSED BY AUTHOR REVISION

| | |
|---|---|
| **Sources** | the repository Roadmap: §0.7, *"Author revisions after the in-repository copy"* (`AUTHOR-DECIDED`, AD-LS1-R-BOOTSTRAP), and §0.8 (`AUTHOR-DECIDED`, AD-REG-AUTHORING-SPLIT), which lists row 082 among the structural contracts that *"move to `docs/registry/<family>.schema`"*; Revolving Resolution Note GAP-K: *"The Roadmap copy is no longer byte-identical to the original upload."*, with CONFLICT-E and CONFLICT-F as the audit trail; git history: the original copy (commit `d68927f`) has no §0.7 or §0.8 and gives row 082 as `canon/registry/controlled_vocabulary.schema` |
| **Established** | row 082's manifest path in the repository Roadmap is `docs/registry/controlled_vocabulary.schema`; no other source sets a different path; row 081's path is the same in both copies; no file exists at either 082 path |
| **Condition** | an audit made against the original upload finds row 082 under `canon/registry/` and no §0.7 or §0.8. That difference is these two author revisions, not an error in either copy |
| **Treatment** | every Roadmap citation here is to the repository copy, as §3 states. The author confirmed both revisions as their rulings on 2026-10-28, when this condition was raised. Nothing is moved, and 082 is not created |
| **Owner** | the Roadmap author |
| **Blocks?** | no |

## 16. Conformance Conditions

Each row states an obligation (*Condition*), the procedure that checks it (*Class*) and where in
this document the obligation is carried (*Where*). The class names the evidence a check needs:
**STATIC** — this document alone; **CROSS-SOURCE** — the repository copies of the sources cited in
the section under *Where* (§3), which are its reproducible anchors; **REPOSITORY** — the git history
of the commits that create or change this file, and the contents of `canon/**`. No condition needs
a test framework.

A class says how a condition is checked, not that it has been. Results are recorded here only as
the author's report: when this text was last changed, the author compared C-081-18 and every
`*"…"*` quotation mechanically, checked C-081-08 and C-081-19 against git, and reviewed the rest by
reading. Those results are author-reported until a reviewer repeats them, and a passing check is
not acceptance, which is a human record (§18).

| ID | Condition | Class | Where |
|---|---|---|---|
| **C-081-01** | `CONTROLLED-VOCABULARY` is identified as an existing Registry Kind — Kind 7 of RMS §10.1, per Artifact 064. | CROSS-SOURCE | §4.1; CV-081-01 |
| **C-081-02** | No new Registry Kind is created, and row 106's name is not promoted into one. | CROSS-SOURCE | §6.4; CV-081-01 |
| **C-081-03** | Divergent per-Kind value sets are explicitly permitted. | CROSS-SOURCE | §5; CV-081-05 |
| **C-081-04** | Forced enum union across Kinds is explicitly prohibited, and what it is is stated. | CROSS-SOURCE | §5.2; CV-081-06 |
| **C-081-05** | Shared field meaning is distinguished from controlled values. | CROSS-SOURCE | §7; CV-081-07, CV-081-12 |
| **C-081-06** | No statement asserts that all Kinds share the same `status` values. | STATIC | §5; §13 A–B |
| **C-081-07** | Registry definition authority is separated from domain Record ownership. | CROSS-SOURCE | §8; CV-081-10 |
| **C-081-08** | No canonical Registry Record is created. | REPOSITORY | §0 |
| **C-081-09** | Artifact 082's schema is not implemented: no element inventory, notation or carrier is fixed. | STATIC | §4.3; §17 |
| **C-081-10** | Identity and resolution obligations are stated without a resolver. | CROSS-SOURCE | §9 RS-081 |
| **C-081-11** | Versionability is preserved without versioning or supersession mechanics. | CROSS-SOURCE | §9 VS-081 |
| **C-081-12** | Every permitted reference stays within Artifact 063's boundary. | CROSS-SOURCE | §10 |
| **C-081-13** | No domain instance or domain state is admitted as a value, target or authority. | CROSS-SOURCE | §10 RF-081-2, RF-081-3 |
| **C-081-14** | No universal lifecycle, `status` vocabulary, enum or Kind taxonomy is created. | CROSS-SOURCE | §6.2; CV-081-09 |
| **C-081-15** | Unresolved association cardinality is recorded as OD-081-1, not decided. | STATIC | §15.1; CV-081-13 |
| **C-081-16** | The semantic contract is handed to Artifact 082 with its boundary. | STATIC | §17 |
| **C-081-17** | No downstream row's `Val` or `Done` is expanded. | CROSS-SOURCE | §17 |
| **C-081-18** | The header and §0 reproduce row 081 exactly. | CROSS-SOURCE | header; §0 |
| **C-081-19** | Only `docs/registry/controlled_vocabulary.md` is created or changed by this artifact's commits. | REPOSITORY | row 081 |
| **C-081-20** | Row 081's `Done` is reported at the level it reaches, and no higher. | STATIC | §18 |
| **C-081-21** | The family is neither narrowed to per-Kind field values nor given a closed list of scopes. | CROSS-SOURCE | §6; CV-081-08 |
| **C-081-22** | Every vocabulary is required to state its values and their meaning, and to make its applicability determinable. | CROSS-SOURCE | §4.3; CV-081-03, CV-081-04, CV-081-08 |
| **C-081-23** | Content extensibility is stated together with governance, and no procedure is invented. | CROSS-SOURCE | §9 VS-081-2, VS-081-3 |
| **C-081-24** | `status` stays World-owned; no `status` exists elsewhere because of this family. | CROSS-SOURCE | §6.3; SC-081-N |
| **C-081-25** | Defaults, requiredness and occurrence counts are left schema-side. | CROSS-SOURCE | §7; CV-081-12 |
| **C-081-26** | `H: 064` is the only hard dependency; supporting artifacts are not promoted. | CROSS-SOURCE | §3 |
| **C-081-27** | Stale Blueprint wording corrected by the RMS is identified as closed, not reopened. | CROSS-SOURCE | SC-081-A, SC-081-H, SC-081-N |
| **C-081-28** | No statement declares OD-081-1 unconditionally non-blocking for Artifact 082; independent obligations, representation choices and association-dependent work are distinguished, and whether OD-081-1 blocks a given 082 design is left to the assessment of that design. | STATIC | §15.1; §17 |
| **C-081-29** | One vocabulary per Record is stated as the unit of definition identity and is not used to fix association cardinality. | STATIC | §4.3; CV-081-03; SC-081-D |
| **C-081-30** | Applicability is a semantic obligation; no element name, reference carrier or association cardinality is prescribed for it, and vocabulary-side determinability is not presented as a consumer-side selection mechanism. | STATIC | §6.2; CV-081-08; PI-29 |
| **C-081-31** | No section admits or rejects an empty vocabulary; the meaning obligation is not read as a minimum size. | STATIC | SC-081-E; PI-31 |
| **C-081-32** | Value spelling is not made a value's identity or meaning, and values are not made Registry Records of their own. | STATIC | CV-081-11; CV-081-15; PI-30 |
| **C-081-33** | Versionability is kept apart from the versioning mechanism and from semantic-compatibility policy, and neither is defined here. | CROSS-SOURCE | §9 VS-081-2, VS-081-4 |
| **C-081-34** | Row 082's path and every Roadmap §0.7 and §0.8 citation match the repository Roadmap, and how that copy differs from the original upload is recorded. | CROSS-SOURCE | §0; §3; §17; SC-081-P |

## 17. Downstream Handoff

**To 082** (`CONTROLLED-VOCABULARY` schema, `docs/registry/controlled_vocabulary.schema` per
SC-081-P; `H: 081`;
`Val`: *"definition resolves; versionable; references only declared entities (063)"*; `Done`:
*"schema"*). 082 may take from this specification, without redesign:

1. **Meaning.** An R Record governing one vocabulary — the unit of definition identity, not an
   association cardinality (§4; CV-081-01, CV-081-03).
2. **Content.** Its values or terms, each with a stated meaning, as distinct members of one set
   (§4.3; CV-081-04).
3. **Applicability.** Determinable for every vocabulary, so that divergent sets stay apart, without
   a closed list of scopes, a prescribed element or a fixed carrier (§6.2; CV-081-08).
4. **Divergence and no union.** Nothing in the structure pools the value sets of different Kinds or
   partitions, and nothing requires them to differ (§5; CV-081-05, CV-081-06).
5. **Declared entities.** Where applicability names a Model or Kind, a declared one, by declaration
   reference unless 082 records another carrier as its own (§10 RF-081-1).
6. **Reference legality.** RF-081-1 to RF-081-8.
7. **Identity and versionability.** Ordinary R Record identity; nothing that obstructs 108–110 (§9).
8. **Not schema-side.** No requiredness, occurrence count or default (§7; CV-081-12).

**The boundary for 082 while OD-081-1 is open.** Three cases are kept apart:

| Case | What it covers | 082's position |
|---|---|---|
| **A — independent obligations** | properties the sources establish without OD-081-1: the definition's identity; its values or terms and their meaning; that its applicability is determinable from the vocabulary side (§6.2); versionability; reference legality (items 1–8 above) | 082 may represent them. They are semantic obligations, not a list of mandatory elements |
| **B — representation choices** | within 082's schema responsibility: element names, shapes and notation; how values are identified within a vocabulary, without making spelling an identity or a meaning across vocabularies (CV-081-11); the form that makes applicability determinable, where the sources do not fix it | 082 may make them, recorded as its own choices. A choice may not establish a semantic rule: no shape may force one vocabulary per field, per Kind, or one shared across Kinds, unless a governing source establishes it |
| **C — association-dependent** | any part of a design that requires an association rule — cardinality, identity, reference — the sources do not state, including a general mechanism for selecting a vocabulary from a consuming context | 082 preserves the question, holding such a shape as unresolved rather than accepted or rejected, or escalates it to the owner OD-081-1 names. It does not invent the answer, and that part is not source-established until the relevant authority resolves it |

In every case, 082 may not:

- fix one vocabulary per field, per Kind, or a shared vocabulary across Kinds, by the shape of a
  carrier;
- give a field-binding or Kind-binding element a cardinality the sources do not state;
- add value labels, aliases, ordering, hierarchy, defaults or value-level deprecation as universal
  requirements;
- merge, inherit or override value sets across vocabularies;
- present an empty vocabulary as admitted, or as rejected, as though a source settled it
  (SC-081-E).

**Whether OD-081-1 blocks 082 is not decided here.** OD-081-1 does not invalidate the obligations
082 takes from this specification, and 082 may carry Case A and Case B work without it. Artifact
081 does not determine in advance whether OD-081-1 blocks any particular 082 schema design or
conformance claim; that is assessed against the actual design and 082's `Val` and `Done`. An
unspecified carrier is not evidence that the association question is resolved.

**082 is not asked** to fix anything this specification leaves open, and this specification decides
none of 082's representation choices. 082's `Val` and `Done` are not enlarged.

**Other dependents, preserved and not implemented:**

| Row | Relation to 081 | Keeps |
|---|---|---|
| 105 | `H: 081` | the diagnostic vocabulary's content, *"recorded as a controlled vocabulary"* |
| 106 | `H: 081` | the signal classes; representation not established (064 §23) |
| 107 | `H: 081` | the reader archetypes, *"as a controlled vocabulary"* |
| 450 | `H: 448,081` | vocabulary growth rules: *"new terms enter through a governed vocabulary, not ad hoc"* |
| 282; 350 | `H` lists 082 | the epistemic vocabulary map; the VISUAL-ASSET subtype vocabulary |
| 347; 400 | named in 082's `→`, not in their own `H` (SC-081-M) | their own rows |
| 065; 108–117; 124; 152 | adjacent owners | their own rows |

**Unlock is not dependency.** Row 081's `→` names 082 only. Rows 105, 106, 107 and 450 consume 081
through their own `H`; that relation is theirs and is not rewritten here (SC-081-M).

## 18. Roadmap Completion Trace

Each item is reported at the level it has reached (§0). MECHANISM and DEMONSTRATED are reached by
none: 082 and rows 108–124 do not exist in the repository at this revision.

| Row 081 | Reached | Not reached | Where |
|---|---|---|---|
| `Val`: *"definition resolves"* | **SPECIFIED** — independent R Record identity under the universal grammar and envelope, distinct from values, fields and Kinds; resolvable ≠ legal. **SOURCE-CHECKED** — RMS §4, §5 | MECHANISM: 082, 114, 115, 117. DEMONSTRATED: 116, 124 | §9 RS-081 |
| `Val`: *"versionable"* | **SPECIFIED** — governed evolution under 108–110; content extensible by governed change; not defined ≠ forbidden; versionability kept apart from mechanism and compatibility policy. **SOURCE-CHECKED** — §9.4, §33, 064 F-4, rows 108–110 | MECHANISM: 108–110 | §9 VS-081 |
| `Val`: *"references only declared entities (063)"* | **SPECIFIED** — applicability names declared Models and Kinds; no domain instance, state or runtime target; values are not references; category ≠ relation. **SOURCE-CHECKED** — RMS §10.3, 063 | MECHANISM: 082's representation, 112. DEMONSTRATED: 112's negative test, 116 | §10 RF-081 |
| `Done`: *"per-kind value sets may diverge; forced enum union prohibited"* | **SPECIFIED** — both stated as rules (CV-081-05, CV-081-06), with what a forced union is (§5.2) and its examples (§13 A, B). **SOURCE-CHECKED** — §9.4, §13.6 | no concrete vocabulary yet exists to show it; whether SPECIFIED is the level `Done` requires is for human review | §5; §11; §13 |
| `Why`: *"§9.4's explicit rule"* | **SPECIFIED** — §9.4's rule is the family's primary invariant (§1) | — | §1; §5 |
| `H: 064` | **PRESENT** — Artifact 064 exists at its path; §4.1's quotations of it are SOURCE-CHECKED | its review status is a human record | §4.1 |
| `S: —` | **PRESERVED** | — | §3 |
| `LS: LS-1` | **PRESERVED** — label kept; no pair invented | resolution is the Roadmap author's | SC-081-K |
| `G: —` | **PRESERVED** — no gate introduced; OD-081-1 is not a gate | — | §0; §15.1 |
| `→ 082` | **SPECIFIED** — the handoff is stated, with Cases A–C kept apart; 082's `Val` and `Done` unchanged | 082 does not exist yet; whether OD-081-1 blocks any 082 design is not decided here | §17 |
| `Req: RR-16` | **CARRIED** — ID only | no compliance claimed | SC-081-I |
| open decision | **RECORDED** — OD-081-1 with owner, scope and closing condition | OPEN; its effect on 082 is assessed against 082's actual design | §15.1; §17 |

Whether SPECIFIED and SOURCE-CHECKED suffice for row 081 to proceed is a human review decision; this
document does not make it. No vocabulary, value, Record, schema, validator or canonical data is
created.

---

*Artifact 081 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining. Row 081's `Canon` and `CD`
values are copied in the header and do not make this file a Registry Record (SC-081-J). A Registry
definition-family specification under `docs/**`: it holds no canonical data, no vocabulary and no
value, and licenses no canonical write. Where it differs from the Master Blueprint, the Record Model
System, the OS File Build Roadmap, or Artifact 064, those sources are correct and this document is
wrong.*
