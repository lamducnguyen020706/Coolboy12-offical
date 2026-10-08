# COOLBOY12 — KIND-DEFINITION Specification

**Artifact 068** · KIND-DEFINITION spec · `docs/registry/kind_definition.md` · Own: R · RM: R ·
T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining · Canon: canonical-about-meaning · CD: yes ·
Ph/St: P3/3b · Req: RR-16 · BP: §9.4 · RMS: §10.1 · H: 064 · S: — · LS: LS-1 · G: — · → 069 ·
Val: definition resolves; versionable; references only declared entities (063) · Done: every Kind
definable · Why: **defines the KIND-DEFINITION family every LS-1 Kind-Definition set uses** ·
Risk: HINGE · ∥: yes

## 1. Purpose

This specification answers one question — **what must a `KIND-DEFINITION` mean about one
already-declared Kind so that the Kind has governed, resolvable, versionable definition meaning,
without the Registry admitting the Kind, owning its Records, or becoming the model that owns it?**

COOLBOY12 keeps apart two things that are easy to merge:

```
CHARACTER                          a World Kind — a class of World Record (RMS §6.1, §7)
KIND-DEFINITION about CHARACTER    an R-partition Registry Record that governs the definition
                                   of CHARACTER
```

They are two objects with two owners (Artifact 064 §22). This document specifies the semantic
family contract that makes the second possible for every legitimate Kind — row 068's `Done`,
*"every Kind definable"* — and, in its `Why`'s words, the family *"every LS-1 Kind-Definition set
uses"*.

`KIND-DEFINITION` already exists. It is Kind 2 of RMS §10.1's *"Final Kind taxonomy — CLOSED at
fourteen"*, and Artifact 064 §9 records its admission rationale. This document does not decide
whether the Kind exists; it specifies what a valid `KIND-DEFINITION` means.

```
OWNING RECORD MODEL — one of W · E · P · R · V · I
    ├── declares the Kind in its own taxonomy; admission is the model's question,
    │   never a Registry definition's
    ├── owns which Records of the Kind exist, and what they mean in its domain
    └── keeps its own model-owned semantics
            ↕   LS-1 — custody split; one authoring cycle; not a reference, not a dependency
REGISTRY KIND-DEFINITION
    ├── governs the definition of ONE declared Kind
    ├── resolves as a Registry definition
    ├── is versionable
    ├── obeys Artifact 063's reference boundary
    └── never admits the Kind, owns its Records, or becomes its model
            ↓
Artifact 069 — encodes this family structurally
            ↓
075 · 178 · 257 · 300 · 345 · 364 — the concrete Kind-Definition sets
```

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: ARCH` · `SoT: AUTHORITATIVE` about the `KIND-DEFINITION`
family · `Auth: defining` · `Canon: canonical-about-meaning` · `CD: yes`. This document is a family
specification. It is **not** a `KIND-DEFINITION` Record: it mints no identity, holds no Registry
data, admits no Kind and writes nothing under `canon/` (SC-068-G). The `Canon` and `CD` values are
row 068's metadata for this artifact; they do not turn a `T: doc` specification into a Registry
Record. Where it differs from the Master Blueprint, the Record Model System, or the OS File Build
Roadmap, **those sources are right and this document is wrong.**

`Req: RR-16` is reproduced from row 068. The requirement register is not in the supplied source
set, so the ID is carried forward unverified and no requirement text is stated for it (GAP-C;
SC-068-F).

Statements below are labelled where it matters: **source fact** (stated by the Blueprint, the RMS,
the Roadmap or a frozen artifact), **required synthesis** (a conclusion several source facts force
together; not a quotation), **reading** (an interpretation, recorded as one), and **source gap**
(not established, and not filled here).

## 3. Scope

**In scope.** What a `KIND-DEFINITION` is and what it carries; its semantic subject — one declared
Kind of one Record Model; how it differs from the Kind, the Kind's specification, the Kind's schema
and the Kind's admission; why every Kind of the six models is definable; the authority and
ownership the family never acquires; what *"definition resolves"* and *"versionable"* mean as
obligations; Artifact 063's reference boundary as it applies to this family; the family's
semantic-layer placement; what LS-1 means for it; the handoff to 069.

**Out of scope, by owner.**

| Not defined here | Owner |
|---|---|
| the Registry's fourteen Kinds and their admission rationale | 064 (consumed, §6) |
| the Kind Admission Test; the admission act as the sources state it | 057; the owning model |
| each model's Kind taxonomy and Kind specifications | that model's rows: 064 (R), 176 (W), 255 (E), 298 (P), 344 (V), 363 (I), and their Kind specifications |
| the schema encoding of the semantic obligations established here: field names, serialization, cardinality syntax, schema language, the representation of the Kind subject | 069 |
| the schema of the Records of any Kind — for example `canon/world/character.schema` | the owning model's schema rows (row 184, `Own: W`) |
| the Registry self-Kind definition set contract; the fourteen Registry `KIND-DEFINITION`s | 074; 075 |
| the W, E, P, V and I Kind-Definition sets | 178; 257; 300; 345; 364 — and 399 for VERDICT (SC-068-J) |
| `SUBTYPE-DEFINITION`, `FIELD-DEFINITION`, `MODEL-DEFINITION` and the other Registry families | their own rows, 066–107 |
| who may propose, approve or deprecate a definition | 065 |
| evolution, versioning, supersession, deprecation | 108, 109, 110 |
| concrete definition-dependency rules | 111 |
| reference validator; constraint binder; kernel; resolution service; validation suite | 112; 113; 114; 115; 116 |
| lockstep tests; P3 conformance | 123; 124 |
| committing any `KIND-DEFINITION` Record to `canon/registry/` | 152, after G-CANON-R (Roadmap §0.8) |
| how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added | 459 |

No Kind, Record Model, partition, field, schema, Record, fixture, test or runtime behaviour is
created, and no Kind is declared, admitted, renamed or retired.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where it says so
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done, handoffs; §0.7 and §0.8 rulings
        ↓
frozen artifacts; Artifact 003 conventions
        ↓
Artifact 068
```

| Source | What it gives this specification |
|---|---|
| RMS §6; §6.1 | what a Record Model owns, *"its Kind taxonomy"* among it; *Kind* — *"A class of Record within one model"*; *Definition* — *"A Registry Record specifying meaning"*, test *"Governs; never instantiates"* |
| RMS §2; §4; §5 | six sovereign models, none a superclass; the universal envelope and the nine prohibitions; *"UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL."*, with Kind meaning and Kind taxonomy model-owned |
| RMS §7, §8.1, §9.1, §10.1, §11.1, §12.1; §13; Appendix A | the six Kind rosters and their counts; the Kind Admission Test; the rejected candidates |
| RMS §10; §10.3; §10.4 | Registry sovereign; the reference boundary; bootstrap closed |
| Blueprint §9.4 | Registry holds *"kind definitions"*; holds no instances; is not schema; resolution is not Registry work; the *Kind semantics* row |
| Blueprint §13.6e | definitions are Records; the definition-versus-ownership boundary; dependency direction; FG-V7-05 (SC-068-H) |
| Blueprint §13.7c; §13.9a | Registry canonical about meaning; Kind meaning owned by the Record Model (SC-068-K) |
| Roadmap row 068; PART III (LS-1); §0.5 RULE G; §0.7 (AD-LS1-R-BOOTSTRAP); §0.8 (AD-REG-AUTHORING-SPLIT) | this artifact's identity; LS-1 and its count; specification ≠ schema; Registry self-hosting; authoring vs canonical materialization |
| Roadmap rows 069, 074, 075, 108–116, 123, 124, 152, 459; Kind-Definition sets 178, 257, 300, 345, 364, 399; taxonomies 176, 255, 298, 344, 363; rows 183, 184, 405 | neighbours' responsibilities |
| Artifact 064 (`H: 064`) | the fourteen Kinds; `KIND-DEFINITION`'s responsibility and admission rationale; Kind ≠ `KIND-DEFINITION`; the self-hosting resolution |
| Artifact 057 | the Kind Admission Test; definition ≠ admission (C-057-08); every Kind within exactly one model (C-057-04) |
| Artifacts 061, 062, 063, 065 | the Kind row of the authority boundary; L2 placement and the layer law; the reference boundary; governance constraints |
| Artifacts 003, 052 | the `Canon`, `CD` and `LS` conventions and the self-hosting exception; Registry canonical about meaning |

Artifacts 057, 061, 062, 063, 065, 003 and 052 are consumed as frozen constraints. They are not
declared dependencies of row 068 and are not added to `H` or `S`. Artifacts 066 and 067 are a
precedent for form only; nothing here is derived from the `MODEL-DEFINITION` family.

## 5. What a KIND-DEFINITION Is

**Source facts.**

- A Kind is *"A class of Record within one model"* (RMS §6.1); a Record Model owns *"its Kind
  taxonomy"* (RMS §6).
- A *Definition* is *"A Registry Record specifying meaning"*; its test is *"Governs; never
  instantiates"* (RMS §6.1). Registry Records are semantic-definition Records — *"not
  configuration, not code constants, not metadata, not a catalog, not runtime"* (RMS §10).
- *"A kind definition is not a constant in source code; it is a Registry Record with identity under
  the universal grammar (§13.9a), provenance, a governed change path, and a temporal account."*
  (Blueprint §13.6e).
- Blueprint §9.4's *Kind semantics* row holds *"What is true of every record of one kind"*.
  Artifact 062 §4.3: *"At the Registry-definition boundary, L2 is represented by the governed
  `KIND-DEFINITION` that specifies what a Kind means."*
- Artifact 064 §9: the semantic object is *"the governed definition of what one Kind means"*; the
  semantic question is *"what is a Record of this Kind?"*; the persistent state is *"the defined
  meaning of one Kind; content is 068's"*.

**Definition (synthesis).** A `KIND-DEFINITION` is a Registry definition Record carrying the
governed, Kind-level meaning of one declared Kind of one Record Model: what a Record of that Kind
is — what holds of every Record of the Kind. It governs that meaning, which the Kind's Records and
the model's Kind artifacts resolve against, and it never instantiates the Kind.

**Content (synthesis — the part 064 §9 assigns here).** The family's persistent content is that
Kind-level meaning and nothing else. It is not:

- the Kind's admission rationale, or a record of the Kind Admission Test (§8; KD-7);
- the owning model's Kind taxonomy, or the Kind's place in it (KD-4, KD-8);
- any Record of the Kind, any value such a Record carries, or what is true of one (KD-3);
- the structural schema of the Kind's Records (KD-6);
- the content of another Registry family — a subtype, field, schema, relationship-type, vocabulary
  or model definition (KD-9);
- the owning model's identity semantics, state and lifecycle, relationship packaging, temporal
  architecture, provenance meaning, canonicality meaning, semantic validation or package
  composition (RMS §6; KD-10).

The question 064 assigns — *"what is a Record of this Kind?"* — is answered as the Registry's
governed definition that consumers resolve against. It does not hand the Registry the owning
model's domain (§11).

**Envelope — obligation only.** Once materialized, a `KIND-DEFINITION` carries the universal
envelope unchanged — `partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` ·
`sot_class` (RMS §4) — in partition R. No family concept — the subject Kind, its owning model, a
version, a status, a tier, a lifecycle, a deprecation flag or an authority — becomes a universal
field. None of RMS §4's nine prohibited universal semantics is introduced: no universal Record
base, Relationship Record, History Record, lifecycle, canonicality, Kind taxonomy, identity
composition, state model or semantic schema. How the obligations of this document are structurally
encoded is 069's; representation this document defers stays with its named owner (§13, §21).

## 6. Inherited Contract from Artifact 064

`H: 064` is consumed unchanged.

- **Fourteen Kinds.** `KIND-DEFINITION` is Kind 2 of RMS §10.1's *"Final Kind taxonomy — CLOSED
  at fourteen"*. It is not renamed, merged into `SUBTYPE-DEFINITION`, `FIELD-DEFINITION`,
  `SCHEMA-DEFINITION` or `MODEL-DEFINITION`, or replaced, and no fifteenth Kind is introduced.
  Blueprint §13.6's `KIND-DEF` is a source alias of the RMS name, not a further Kind (064 §5).
- **Responsibility.** 064 §6 row 2: *"what a Kind means; the Registry partner of every Kind spec
  (LS-1)"*.
- **Authority.** 064 §9 question 6: *"definition authority only: the owning model keeps its
  taxonomy, admission and Records; a `KIND-DEFINITION` is not admission"*.
- **References.** 064 §9 question 7: LS-1 pairs each Kind spec with its `KIND-DEFINITION` *"as an
  authoring obligation, not a reference edge"*; the concrete reference is left to this family
  (§14).
- **Admission not reopened.** 064 §9 answers the fourteen questions for this Kind; this
  specification does not revisit them.
- **Kind ≠ `KIND-DEFINITION`.** 064 §22: *"The World Kind `CHARACTER` and a `KIND-DEFINITION`
  Record describing `CHARACTER` are two objects."*
- **Self-hosting.** 064 §22 and SC-064-D: the Registry's own pairs are 064 ↔ 075, and *"rows
  068–069 provide the generic family and schema"* (§16).
- **No common family checklist.** 064 §27 hands each row of 066–107 *"exactly the specification or
  schema responsibilities, `Val` and `Done` the Roadmap and governing sources assign each row"*.
  Nothing here is required of another family, and nothing beyond row 068's `Val` and `Done` is
  claimed for this one.

## 7. Kind vs KIND-DEFINITION

> **A Kind is not its `KIND-DEFINITION`, its specification, or its schema.**

Five objects, kept apart — shown for World's `CHARACTER`:

| Object | What it is | Owner | Source |
|---|---|---|---|
| `CHARACTER` | a World Kind: a class of World Record | World — in its taxonomy, row 176 | RMS §6.1, §7 |
| CHARACTER spec, row 183 | World's architecture statement about its Kind, with *"admission rationale present"* | World (`Own: W`) | row 183; RULE G |
| CHARACTER schema, row 184 | World's structural contract for Character Records; `Val`: *"conforms to 178"* | World (`Own: W`) | row 184; RULE G |
| `KIND-DEFINITION` about `CHARACTER` | the Registry Record governing the definition of `CHARACTER` — one of row 178's seven | Registry (`Own: R`) | §13.6e; row 178 |
| a Character | one World Record, schematically `W-CH-<ordinal>-<slug>` | World | RMS §7; I-16 |

A `KIND-DEFINITION` does **not**: create `CHARACTER`; declare or admit it; place it in World's
taxonomy; hold or own a Character Record; decide what is true of any Character; serve as
`CHARACTER`'s schema; or execute anything. Blueprint §9.4: *"It defines what a `LINEAGE` is; it
never holds a lineage."*

**Artifact 069 is not a Kind's schema.** Row 069, `docs/registry/kind_definition.schema`, is
*"the schema every concrete KIND-DEFINITION Record conforms to"* — the structural contract of the
Registry `KIND-DEFINITION` Records themselves. It is not the schema of `CHARACTER`,
`ORGANIZATION`, `ARC` or any other Kind's Records, which stay with their models.

**Conformance is not ownership.** Downstream model rows conform to their Kind-Definition set — row
184: *"conforms to 178"*; rows 185, 189 and 195: *"admission rationale present; conforms to 178"*;
row 406: *"conforms to 399"*. That shows which governed definition those artifacts resolve against
(§11). It makes the Registry the owner of neither the specification, the schema, nor any conforming
Record (Artifact 061 §7 rows 1 and 8).

**Reading — *Structural definition*.** Blueprint §13.6e groups `KIND-DEF` with `SUBTYPE-DEF` and
`FIELD-DEF` under the category *"Structural definition"*, which governs *"What a Record of a kind
is"*. The label names the governed subject. It does not make a `KIND-DEFINITION` the schema of the
Kind's Records: *"The Registry is not schema."* (§9.4); a schema's definition is
`SCHEMA-DEFINITION`'s (RMS §10.2); and RULE G keeps a Kind's specification and schema as separate
model artifacts. This is recorded as a reading.

## 8. Definition vs Admission

**Source facts.** Artifact 057 §4: *"A Kind existing in a roster, a Kind being defined in the
Registry, and a Kind being admitted are three statements; this contract equates none of them."*
C-057-08: *"A `KIND-DEFINITION` is not read as admission."* Artifact 057 §9: the sources give the
Registry *"The definition of a kind"* and do not establish that it admits another model's Kind.
Artifact 063 §8: that a Kind *"has a `KIND-DEFINITION` is not by itself made proof of declared
status"*. Artifact 065 §12: *"Approving a `KIND-DEFINITION` admits no Kind"*.

```
CORRECT      the owning model declares the Kind     →   a KIND-DEFINITION may govern its definition
             (its taxonomy; admission as the sources state it)

INCORRECT    a KIND-DEFINITION is written           →   the Kind becomes declared or admitted
```

**What a `KIND-DEFINITION` never does.** It does not admit a candidate, approve a promotion to Kind,
add a Kind to a taxonomy, satisfy or record the Kind Admission Test, run or stand in for a
ceremony, or close an admission decision. For a World Kind, admission is *"a schema change at
Foundational ceremony"* (Artifact 057 §4, from §13.11); for E, P, R, V and I, no source defines the
ceremony for a closed roster, and row 459 owns how a new Kind is added (Artifact 057 §8;
SC-064-C). This document defines no ceremony.

**Admission evidence lives on the model side.** The admission rationale belongs to the Kind
taxonomy and the Kind specification — row 064 for R (*"each with admission rationale"*), row 183's
*"admission rationale present"* for a World Kind. RMS §13's fourteen questions are not required
content of a `KIND-DEFINITION`: no current source makes them part of this family (KD-7).

**Declared first, in the build order too.** Every concrete Kind-Definition set the Roadmap assigns
follows its model's Kind taxonomy: row 075 (`H: 074,069`, with row 074 `H: 064,069`), 178
(`H: 069,176`), 257 (`H: 069,255`), 300 (`H: 069,298`), 345 (`H: 069,344`) and 364
(`H: 069,363`). The one row that does not — VERDICT's, row 399 — is recorded at SC-068-J.

## 9. Family Rules

| ID | Rule | Basis |
|---|---|---|
| **KD-1** | **One definition, one declared Kind.** A `KIND-DEFINITION` defines governed meaning about exactly one declared Kind. It is never a definition of several Kinds, of a group of Kinds, or of a Kind-like class no model has declared. How the subject is encoded is 069's. | §13.6e (*"The definition of a kind"*); RMS §6.1; 064 §9 questions 1–2; LS-1; Artifact 063 §7 row 3; synthesis |
| **KD-2** | **The subject is declared first.** The definition causes no declaration and no admission. Its subject must already be a declared Kind of its owning model, with declared status established by that model's own Kind architecture (Artifact 063 §8). A candidate is not a legal subject, and writing, approving or committing a `KIND-DEFINITION` does not make it one. | C-057-02; Artifact 057 §4, §9; Artifact 063 §8, RB-1, RB-6; §8 above |
| **KD-3** | **Governs; never instantiates.** The definition is semantic. It is not a Record of the Kind it defines, creates no such Record, contains or owns none, and carries no executable behaviour — no factory, registration service, validator or runtime object. | RMS §6.1; RMS §10; Blueprint §9.4 |
| **KD-4** | **The Kind stays with its model.** Registry owns the `KIND-DEFINITION` Record. The owning Record Model keeps the Kind's place in its taxonomy, its declaration and admission as the sources state them, which Records of the Kind exist, what they mean in its domain, and its model-owned semantics. For a Registry Kind the owning model is Registry itself, which holds those by its own sovereignty as R — the ordinary rule, not an exception — and never because a `KIND-DEFINITION` conferred them. | §13.6e; I-105; Artifact 061 §7 row 1; Artifact 057 §9; Artifact 062 §4.3 |
| **KD-5** | **One owning model.** The defined Kind is a class of Record within exactly one of W, E, P, R, V and I. The subject is the Kind as that model declares it — never an unscoped label, a class spanning models, or a Kind of no model. How model scope is expressed is 069's. | RMS §6.1; C-057-04; Artifact 057 §11 row 3; RMS §5 |
| **KD-6** | **Definition ≠ specification ≠ schema.** A `KIND-DEFINITION` governs Kind meaning. It is not the owning model's Kind specification and not the schema of the Kind's Records; those are separate model artifacts. Row 069 is the schema of `KIND-DEFINITION` Records, not of any defined Kind. | §0.5 RULE G; rows 069, 183, 184; Blueprint §9.4; RMS §10.2; Artifact 061 §7 row 8 |
| **KD-7** | **Definition ≠ admission evidence.** Neither the definition nor its LS-1 pairing is the admission act, the admission ceremony, the admission rationale or proof of declared status. RMS §13's fourteen questions are not family content. | C-057-08; Artifact 057 §11 row 8; Artifact 063 §8; 064 §9 question 7 |
| **KD-8** | **No universal Kind taxonomy.** One generic family used across six models merges no rosters, creates no cross-model Kind or Kind identity, and makes no Kind a superclass, template or shared interior of another. | RMS §4 (nine prohibitions); RMS §2; RMS §5; I-106; Artifact 057 §11 row 4 |
| **KD-9** | **Kind level only.** A `KIND-DEFINITION` carries Kind-level meaning. It does not carry or replace a `SUBTYPE-DEFINITION`, `FIELD-DEFINITION`, `SCHEMA-DEFINITION`, `RELATIONSHIP-TYPE-DEFINITION`, `CONTROLLED-VOCABULARY` or `MODEL-DEFINITION`; subtype, field, structure, relationship-type, vocabulary and model meaning are those families'. | RMS §10.1; Blueprint §9.4 (*Kind semantics* and *Subtype semantics* rows); 064 §9 questions 11 and 13; Artifact 062 §4.3 |
| **KD-10** | **Model-owned semantics stay with the model.** The definition does not supply, override or standardize the owning model's identity semantics, state and lifecycle, relationship packaging, temporal architecture, provenance meaning, canonicality meaning, semantic validation or package composition, and decides no instance truth. | RMS §6; RMS §4; §13.6e (the authority table) |

## 10. Every-Kind Definability

Row 068 `Done`: *"every Kind definable"*.

**Required synthesis.**

1. Every Kind is a class of Record within exactly one Record Model (RMS §6.1; C-057-04), and the
   models are exactly the six of RMS §2.
2. A declared Kind is an admissible Registry reference target whatever its model: RMS §10.3 names
   *"declared Kinds"* without restricting them to a model, and Artifact 063 §7 row 3 applies it.
3. The family requires nothing model-specific of its subject (KD-1 to KD-10): no Relationship
   Record or History Record (I-102), no `status` or `tier` (RMS §4), and none of a model's own
   lifecycle, temporal architecture, canonicality or package (RMS §6).
4. Registry *"must not require the complete semantic implementation of every other Record Model in
   order to define them"* (§13.6e; Artifact 062 D-7): a declared Kind is definable before its
   model's domain design is complete.

Therefore every declared Kind of every one of the six models is a legal `KIND-DEFINITION` subject,
and the family needs no per-model variant.

| Model | Roster (source) | Current Kinds | Example Kind | Concrete Kind-Definition set | Family applies |
|---|---|---|---|---|---|
| **R** | RMS §10.1; row 064 | 14 | `KIND-DEFINITION` itself | row 075, specified by row 074 | yes — including to `KIND-DEFINITION` itself (§16) |
| **W** | RMS §7; row 176 | 7 — the WSV singleton is not counted | `CHARACTER` | row 178 | yes |
| **E** | RMS §8.1; row 255 | 7 | `EVIDENCE` | row 257 | yes |
| **P** | RMS §9.1; row 298 | 13 — the RMS-frozen baseline (CONFLICT-A) | `ARC` | row 300 | yes |
| **V** | RMS §11.1; row 344 | 3 | `VISUAL-ASSET` | row 345 | yes |
| **I** | RMS §12.1; row 363 | 5 | `ARTICLE` | row 364 | yes |
| **Total** | | **49** — LS-1's *"49 pairs"* | | | |

The rosters are the models' own; RMS Appendix A lists them. They are cited here, not restated, not
owned and not frozen by this document (I-106). The matrix proves the family's applicability. It is
not a taxonomy, admits nothing, instantiates no Record, assigns no identifier or Kind code, and is
not Registry data.

**Not subjects.** None of the following is a declared Kind, so none is a `KIND-DEFINITION`
subject:

- **the WSV singleton** — *"World state, not an instance-bearing Kind"* (RMS §7); Roadmap PART III:
  *"the WSV singleton is not a Kind and has no pair"*. Indicator meaning is
  `WSVR-INDICATOR-DEFINITION`'s (RMS §10.7) (SC-068-I);
- **rejected candidates** — *"BELIEF · ARTIFACT · CONTEXT · VISUAL-DERIVATIVE · VISUAL-REFERENCE ·
  SECTION · PAGE · SPREAD · PUBLICATION-METADATA · EDITION · REISSUE"* (RMS Appendix A);
- **subtypes** — for example Visual's production forms, *"a Registry-governed subtype vocabulary,
  not Kinds"* (RMS §11.1), whose definitions are `SUBTYPE-DEFINITION`s (row 070: *"V asset forms
  are subtypes, not Kinds"*);
- **non-roster Registry artifact subjects** — `IDENTITY-DEFINITION`, `DERIVATION-DEFINITION`,
  `ROLE-BOUNDARY-DEFINITION`, `DEGRADED-MODE-DEFINITION` and the others Artifact 064 §23 lists;
- **VERDICT**, while it is a provisional roadmap extension rather than a declared P Kind
  (CONFLICT-A; SC-068-I, SC-068-J). The family applies to it unchanged once its declared status is
  established; this document does not establish it.

## 11. Authority, Ownership and Canonicality

**Source fact.** *"Registry governs the definitions. Each Record Model owns its Records."*
(Blueprint §13.6e; I-105). §13.6e's first boundary row gives the Registry *"The definition of a
kind"* and each Record Model *"Which Records of that kind exist, and what they mean in its
domain"*; and *"Registry defines what a `CHARACTER` is; it never holds a character, and it never
adjudicates what is true of one"*.

| Registry governs | The owning Record Model governs | Registry never infers | Source |
|---|---|---|---|
| the `KIND-DEFINITION` Record and the governed definition it carries | the Kind's place in its taxonomy; the Kind's declaration and admission as the sources state them | admission authority over another model's Kind; a change to any model's roster | §13.6e; Artifact 057 §9; I-106 |
| — | which Records of the Kind exist, and what they mean in its domain | ownership of any Record of the Kind | §13.6e; I-105; RMS §10.3 |
| — | its identity semantics, state and lifecycle, relationship packaging, temporal architecture, provenance and canonicality meaning, semantic validation and package composition | any of those, for any model, through a definition | RMS §6; §13.6e; KD-10 |
| — | the Kind's specification and the schema of its Records | ownership of either because it conforms to the definition | RULE G; rows 183, 184; Artifact 061 §7 row 8 |

Applied to `CHARACTER` (Artifact 061 §9 example A, schematic):

```
R-<kind>-<ordinal>-<slug>     KIND-DEFINITION about CHARACTER     Registry owns this Record
W-CH-<ordinal>-Maximus        a Character                         World owns this Record
```

The Registry decides the governed definition of `CHARACTER`. World decides which Characters exist
and what is true of each — whether one is alive, for instance — together with World's own
lifecycle, relationships and History Record. Who knows or believes what about a Character is
Epistemic's (RMS §8). Whether `CHARACTER` remains in World's taxonomy is World's, at World's own
ceremony (§13.11; Artifact 057 §7).

**Registry is not a super-model.** Defining a Kind of W, E, P, V or I gives the Registry none of
that model's Records and no authority over its taxonomy, admission, lifecycle, canonicality,
temporal design, package architecture or semantic validation. Registry semantic authority is
authority over definition meaning: *"All authority is domain-scoped."* (RMS §17). For a Registry
Kind, the Registry owns the Kind, its Records and its `KIND-DEFINITION` because it is the sovereign
R model (KD-4).

**Canonical about meaning.** Row 068 carries `Canon: canonical-about-meaning` as this artifact's
metadata (SC-068-G). A committed `KIND-DEFINITION` is canonical about meaning as Registry
definitions are: *"This definition is the authoritative meaning records resolve against"*
(Blueprint §13.7c; Artifact 052 §5.4). It is never World Truth: *"Registry is canon about meaning
only; it can never override World Truth"* (RMS §24). A `KIND-DEFINITION` about `CHARACTER` decides
nothing that is true of any Character, and one about `ARC` makes no arc canon (RMS §9.2).
Canonicality is not universalized across the six models (I-104).

**Reading — two custodians of Kind meaning.** RMS §5 lists *"Kind meaning"* as model-owned, and
Blueprint §13.9a says *"the meaning of any kind"* is owned by the Record Model; §13.6e gives the
Registry *"The definition of a kind"*. The sources keep both statements, and the mechanism they
give for holding both is custody: LS-1's *Why* is *"custody split (BP §13.7)"*, and Artifact 003
states that *"a Kind and its KIND-DEFINITION have different owners, and shipping one without the
other leaves a semantic without its definition or a definition without its semantic"*. This
document gives neither side the other's custody and decides no precedence between them beyond what
the sources state (SC-068-K).

## 12. Resolution Contract

Row 068 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-068-1** | A `KIND-DEFINITION` is a Registry definition Record. Once materialized it carries ordinary Record identity under the universal grammar and envelope (RMS §4, §5; §13.6e: *"identity under the universal grammar"*). That identity is an R Record's: it is neither the defined Kind nor the Kind's code (§7). The slug is decoration only and never the basis of resolution (RMS §5). |
| **RS-068-2** | A consumer must be able to resolve a materialized `KIND-DEFINITION` through the shared resolution mechanism. Reference resolution is universal and mechanical (RMS §4); *"Reference resolution is not Registry work"* (Blueprint §9.4). Registry definition resolution by id and version is row 115's (*"consumer resolves by id+version"*); create, resolve and version operations are row 114's. |
| **RS-068-3** | Successful resolution does not establish reference legality: *"Resolvable ≠ legal"* (Artifact 063 §11). |
| **RS-068-4** | Resolution transfers nothing. Resolving a `KIND-DEFINITION` declares or admits no Kind and gives the Registry no Record of the Kind, and the resolved definition is not the Kind (§7). |
| **RS-068-5** | No resolver, lookup function, storage path, index, cache, model-name lookup, Kind-name or Kind-code lookup, version-resolution algorithm or special Kind resolver is defined here. How a consumer finds the definition of a given Kind is likewise not defined here (114; 115; 069). |

## 13. Versionability Boundary

Row 068 `Val`: *"versionable"*.

**Source facts.** A kind definition has *"a governed change path, and a temporal account"*
(Blueprint §13.6e). Row 108 owns the evolution model (`Val`: *"version"*; `Done`: *"temporal
account without a World History Record"*); row 109 owns versioning (*"consumers pin a version"*);
row 110 owns supersession and deprecation (*"deprecated ≠ deleted"*). Row 115 resolves *"by
id+version"*.

**Obligation.** A `KIND-DEFINITION` participates in governed Registry definition evolution and must
be capable of carrying versioned meaning under the model rows 108–110 define. Every version stays
bound by KD-1 to KD-10. The Registry's temporal account is its own: no World History Record is used
or required (row 108; I-102).

**Not decided here** (108–110): a version field or identifier; integer or semantic numbering;
*latest* semantics; pin representation; supersession or replacement representation; deprecation
state or representation; compatibility; retention; deletion. Who may change, supersede or deprecate
a definition is 065's.

**Not defined here ≠ forbidden.** That this document defines no version mechanism is not a decision
that a `KIND-DEFINITION` carries no version, supersession or deprecation information. Rows 108–110
keep their authority to establish the Registry-owned representation, and nothing here asks 069 to
close it. Whatever they establish stays Registry-owned: it adds no field to the universal envelope
and is not a version, lifecycle or state model shared by W, E, P, V or I (RMS §4; §5 above).

**Kind retirement is a separate act.** A Kind's retirement by its owning model (Artifact 057 §6)
and the deprecation of its `KIND-DEFINITION` (row 110) are different acts with different owners.
How they relate is not established (SC-068-M).

## 14. Reference Boundary

Row 068 `Val`: *"references only declared entities (063)"*. Artifact 063 binds this family as a
constraint; it is not added to `H`. Artifact 063 §22 leaves to each family *"which concrete
reference relations each family carries"*; for this family the answer is below.

| ID | Rule | Basis |
|---|---|---|
| **RF-068-1** | **The one required relation is the subject.** Each `KIND-DEFINITION` carries exactly one source-required concrete relation: to the one declared Kind it defines (KD-1). That Kind's declared status must be established by the owning model's Kind architecture; this family defines no proof formula, and undetermined status is not legal. | Artifact 063 §7 row 3, §8, RB-1, RB-6, SC-063-H |
| **RF-068-2** | **The Kind itself, not one of its Records.** The subject is *"a declared Kind — the Kind itself, not a Record of that Kind"*. | Artifact 063 §6 |
| **RF-068-3** | **Declared Kind ≠ its `KIND-DEFINITION`.** Naming the subject Kind is a declaration reference, not an R → R reference to a `KIND-DEFINITION` Record, and it is neither an owned edge nor a Relationship Record. The form of that declaration reference is 069's; no URI, handle, string syntax or discriminator is invented here. | Artifact 063 §8.3, SC-063-G; I-102; Artifact 064 F-7 |
| **RF-068-4** | **No invented concrete references.** Other Registry definitions, declared Record Models, declared schemas and declared semantic contracts are admissible categories; that obliges no `KIND-DEFINITION` to reference any of them, and the family defines no reference list, dependency list or schema reference. Model scope (KD-5) belongs to identifying the subject: whether 069 expresses it within the subject's form or through a separate declared-Model reference is 069's, and this family requires no second relation. Admissible category ≠ concrete family relation. | Artifact 063 RB-5, SC-063-G |
| **RF-068-5** | **No domain instance.** No Record of W, E, P, V or I — and no domain state, such as a current WSV indicator value — is the subject, a reference target, a dependency or the semantic authority of a `KIND-DEFINITION`. Blueprint §9.4's *"a kind may never reference an instance"* stands in full. | RMS §10.3; Artifact 063 §9, SC-063-A |
| **RF-068-6** | **No runtime instance.** No running service, worker, session, process, plugin instance, schema engine, validator process or live object is a dependency, target or authority. | RMS §10.3; Artifact 063 §13 |
| **RF-068-7** | **Resolvable ≠ legal.** A target that resolves mechanically may still be illegal, and a target that cannot be established is not legal either. | Artifact 063 §11 |
| **RF-068-8** | **No transfer through reference.** A legal reference — the subject relation included — transfers no ownership, mutation authority, semantic authority, admission, canonicality or source-of-truth class. | Artifact 063 §12 |
| **RF-068-9** | **Reference ≠ dependency.** The subject relation is a declaration reference. This family does not establish it as a semantic dependency: naming a declared Kind *"does not, by itself, establish a semantic dependency"*, and the named Kind is not semantic authority for the definition. Any semantic dependency a `KIND-DEFINITION` has sits at L2 under Artifact 062's layer law (§15); concrete dependency rules are row 111's. | Artifact 062 D-9; Artifact 063 §7 row 3, RB-5; row 111 |

Blueprint §9.4's older blanket wording — *"A Registry definition may never reference a kind, a
subtype, or an instance"* — is not current law for reference legality. RMS §10.3 corrects it
(*"v0.1 stated the boundary too bluntly"*), and Artifact 063 applies the correction (SC-068-B).

## 15. Semantic-Layer Placement

**Source fact.** Artifact 062 §4.3: *"At the Registry-definition boundary, L2 is represented by the
governed `KIND-DEFINITION` that specifies what a Kind means."* L2 is Blueprint §9.4's *Kind
semantics* row — *"What is true of every record of one kind"* — and depends on *"Registry"*, which
Artifact 062 §4.2 reads as L1.

`KIND-DEFINITION` is placed at L2, and this document does not move it.

| | |
|---|---|
| **May depend on** | L1 — shared field semantics and the peer semantic authorities (Artifact 062 §6) |
| **Must not depend on** | L3 subtype semantics, L4 instance data, L5 derived output (Artifact 062 D-3, D-4, D-8) |
| **May be depended on by** | L3, L4, L5 (Artifact 062 §6) |
| **Ownership at L2** | the Registry governs the definition; the owning model governs its Kind taxonomy, the Kind's domain semantics, which Records exist and what they mean (Artifact 062 §4.3) |

**Consequences.** A `KIND-DEFINITION` never takes its meaning from a `SUBTYPE-DEFINITION`, from a
Record of the Kind, or from derived output. *"Holding a `KIND-DEFINITION` or `SUBTYPE-DEFINITION`
transfers none of the owning model's Kind or subtype domain semantics, taxonomy, admission,
instances, lifecycle, authority, canonicality or package architecture to Registry"* (Artifact 062
§4.3). The layers order meaning; they set no evaluation, loading or resolution order and create no
edge between Record Models (Artifact 062 §7). Which L1 definitions, if any, a `KIND-DEFINITION`
depends on is not established here (RF-068-4; row 111).

The Registry's own Kinds leave one question open. Records of an L1 family's Kind — for example
`FIELD-DEFINITION` — are L1 content, the `KIND-DEFINITION` about that Kind sits at L2, and L1 does
not depend on L2 (Artifact 062 D-8). Whether such Records semantically depend on their Kind's
definition is not established; it is recorded at SC-068-L and not decided.

## 16. LS-1 and Registry Self-Hosting

Row 068 carries `LS: LS-1`, preserved exactly. Roadmap PART III: *"every Kind spec ↔ its Registry
KIND-DEFINITION. ATOMIC-PAIR."*, with the *Why* *"custody split (BP §13.7)"*.

```
Kind spec — the model side                    ↔   KIND-DEFINITION — the Registry side
the owning model's architecture of its Kind,       the governed definition of that Kind,
with its taxonomy and admission rationale          Registry-owned
```

- **Both halves are required.** Artifact 003: *"a Kind and its KIND-DEFINITION have different
  owners, and shipping one without the other leaves a semantic without its definition or a
  definition without its semantic"*.
- **Lockstep is authoring atomicity.** The pair lands in *"one authoring cycle"* (Artifact 003);
  Roadmap §0.8: *"LS atomicity is authoring-cycle atomicity"*, and *"Commit atomicity is row
  153's."*
- **Lockstep is not a reference** (064 §9 question 7) and not, by itself, a hard dependency:
  *"A lockstep partner is not a predecessor."* (Artifact 003).
- **Lockstep is not admission.** Pairing a Kind specification with its definition neither admits
  the Kind nor makes the Registry the admitting authority (KD-7).

**Generic family, concrete sets.**

| What | Where | Role |
|---|---|---|
| the generic `KIND-DEFINITION` semantic family | 068 — this document | what every `KIND-DEFINITION` means |
| the generic structural contract | 069 | *"the schema every concrete KIND-DEFINITION Record conforms to"* |
| the concrete Kind-Definition sets — the Registry halves of LS-1 | 075 · 178 · 257 · 300 · 345 · 364 (VERDICT: 399) | one `KIND-DEFINITION` per Kind of each model |

Row 068's `LS: LS-1` is read through its own `Why` — *"defines the KIND-DEFINITION family every
LS-1 Kind-Definition set uses"* — and through Roadmap §0.7, under which rows 068 and 069 *"now
distinguish the generic family and schema from the concrete sets"*. 068 ↔ 069 is not a Kind ↔
`KIND-DEFINITION` pair, and neither row is the Registry partner of any one Kind.

**The Registry's own pairs.** Under AD-LS1-R-BOOTSTRAP (Roadmap §0.7; Artifact 003) the Registry's
fourteen Kind ↔ `KIND-DEFINITION` pairs are 064 ↔ 075. Row 074 specifies the set and is not a pair
member; row 075 authors the fourteen `KIND-DEFINITION`s — one of which concerns the Kind
`KIND-DEFINITION` itself — as their canonicalization source, committed only through 152 after
G-CANON-R (§0.8). The ordering exception exists because *"Their generic KIND-DEFINITION mechanism
(068–069) cannot exist before the taxonomy that makes KIND-DEFINITION meaningful (064)"* (Artifact
003). The partners are not waived: row 123 rejects a missing or mismatched partner, and exit-P3
cannot pass without them.

**No regress.** The `KIND-DEFINITION` about the Kind `KIND-DEFINITION` is an ordinary Registry
Record of row 075's set, conforming to 069 like the other thirteen. It is not an axiom Record and
needs no prior definition of a definition. RMS §10.4: *"There is no circular self-definition
requirement."* and *"Once Registry exists, its definitions follow normal Record semantics."* This
document and 069 are authored sources, not Records, so no Record-level regress runs through them
(SC-068-H).

**Nothing replaces it.** This document creates no `KIND-DEFINITION` Record, no fifteenth Kind, no
second self-hosting mechanism and no alternate 068 ↔ 069 pair, and does not stand in for row 074 or
row 075. The Bootstrap Meta-Contract stays constitutional and not a Record (RMS §10.4).

## 17. Worked Examples

All examples are **schematic**: no identifier is minted, no Kind code is chosen, and nothing here
is Registry data.

**Legal — a World Kind.** `CHARACTER` is a declared World Kind (RMS §7; row 176). A
`KIND-DEFINITION` about it — one of row 178's seven — governs the definition of `CHARACTER`. World
keeps `CHARACTER` in its taxonomy, owns every Character Record, and decides what is true of each.

**Legal — a Registry Kind, and self-hosting.** `KIND-DEFINITION` is itself one of R's fourteen
Kinds (RMS §10.1), so a `KIND-DEFINITION` about the Kind `KIND-DEFINITION` is one of row 075's
fourteen, specified by row 074 and conforming to 069. It is an ordinary Registry Record — no axiom
Record and no recursion (§16).

**Legal — another model, no merged taxonomy.** `ARC` is a declared Production Kind (RMS §9.1). A
`KIND-DEFINITION` about `ARC` — one of row 300's thirteen — belongs to the same family as the one
about `CHARACTER`, yet `ARC` stays in Production's taxonomy and `CHARACTER` in World's. The two
definitions share a family, not a taxonomy, a lifecycle or a canonicality. Production keeps its
arcs: *"An arc is a plan for telling, not a fact of the universe"* (RMS §9).

**Illegal — a domain instance.** A `KIND-DEFINITION` whose subject, or whose semantic authority for
what a Character is, is the World Record `W-CH-…-Maximus` is rejected: that is a domain instance
(RF-068-2, RF-068-5; Artifact 063 §17).

**Illegal — an undeclared candidate.** A `KIND-DEFINITION` written for `BELIEF` does not make
`BELIEF` a Kind. RMS §8.1 rejects it — *"BELIEVED is a state in the KNOWLEDGE-STATE lifecycle"* —
and no candidate becomes a legal subject because a definition is written for it (KD-2).

**Illegal — admission by definition.** A Registry approval of a `KIND-DEFINITION` for a proposed
Kind, read as admitting that Kind to its model's taxonomy, is rejected: *"Approving a
`KIND-DEFINITION` admits no Kind"* (Artifact 065 §12; KD-7).

**Illegal — a subtype or a singleton as a Kind.** `GENERATED-IMAGE` is a Visual production form — a
subtype, not a Kind (RMS §11.1); its definition is a `SUBTYPE-DEFINITION`. The WSV singleton is not
a Kind and has no `KIND-DEFINITION` pair (Roadmap PART III).

**Boundary — definition vs schema.** The `KIND-DEFINITION` about `CHARACTER` is not
`canon/world/character.schema` (row 184, `Own: W`), and row 069 is not that schema either (KD-6).

**Boundary — LS-1.** Pairing row 183's CHARACTER specification with its `KIND-DEFINITION` in row
178 is an authoring obligation. It creates no Record reference and no semantic dependency (§16).

**Deferred — versions.** The definition of `CHARACTER` must be versionable; how its versions are
represented, pinned, superseded or deprecated is 108–110's (§13).

**Deferred — encoding.** How the subject `CHARACTER` and its World scope are written in a
`KIND-DEFINITION` Record is 069's (§21).

## 18. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | A `KIND-DEFINITION` admits its Kind | definition ≠ admission | C-057-08; KD-2, KD-7 |
| 2 | The Registry admits or approves another model's Kind because it governs that Kind's definition | no admission authority is assigned to the Registry | Artifact 057 §9; Artifact 061 §6 |
| 3 | A Kind is declared because a `KIND-DEFINITION` exists for it | a definition is not proof of declared status | Artifact 063 §8; KD-2 |
| 4 | The Registry owns a Kind's Records because it owns the Kind's definition | *"Each Record Model owns its Records."* | §13.6e; I-105; KD-4 |
| 5 | A `KIND-DEFINITION` is the Kind | Kind ≠ definition | 064 §22; §7 |
| 6 | A `KIND-DEFINITION` is the model's Kind specification | specification and definition have different owners | RULE G; LS-1; KD-6 |
| 7 | A `KIND-DEFINITION` is the schema of the Kind's Records | *"The Registry is not schema."* | Blueprint §9.4; RMS §10.2; KD-6 |
| 8 | Row 069 is the schema of every domain Kind | 069 is the schema of `KIND-DEFINITION` Records | row 069; §7 |
| 9 | §13.6e's *Structural definition* label makes Kind definitions schemas | the label names the governed subject | §7 (reading) |
| 10 | Every declared Kind belongs to one universal taxonomy | taxonomies are model-owned | RMS §4, §5; I-106; KD-8 |
| 11 | One generic family across six models gives their Kinds a common interior | the family is shared; meaning is per Kind and per model | RMS §2; KD-8 |
| 12 | A Kind may belong to two models, or to none | a Kind is a class within one model | RMS §6.1; C-057-04; KD-5 |
| 13 | LS-1 is a Record reference | lockstep ≠ reference | Artifact 003; 064 §9 question 7; §16 |
| 14 | LS-1 is a hard dependency | *"A lockstep partner is not a predecessor."* | Artifact 003 |
| 15 | 068 ↔ 069 is the concrete LS-1 pair of some Kind | they are the generic family and schema | row 068 `Why`; Roadmap §0.7 |
| 16 | Row 068 is itself the concrete `KIND-DEFINITION` for every Kind | the concrete sets are 075, 178, 257, 300, 345 and 364 | 064 §24 row 43; §16 |
| 17 | A resolvable target is automatically legal | resolvable ≠ legal | Artifact 063 §11; RS-068-3; RF-068-7 |
| 18 | A domain instance may establish what its Kind means | domain instances are never semantic authority | RMS §10.3; Artifact 063 §9; RF-068-5 |
| 19 | An admissible target category must be referenced by every `KIND-DEFINITION` | category ≠ concrete relation | Artifact 063 RB-5; RF-068-4 |
| 20 | Naming the declared subject Kind is a semantic dependency | reference ≠ dependency | Artifact 062 D-9; RF-068-9 |
| 21 | *Versionable* lets 068 invent version fields or numbering | the mechanics are 108–110's | §13 |
| 22 | Because 068 defines no version mechanism, a `KIND-DEFINITION` can never carry version information | not defined here ≠ forbidden | §13 |
| 23 | A Registry version representation becomes a universal envelope field | the envelope stays seven fields | RMS §4; §5, §13 |
| 24 | Because Registry content is extensible, 068 may add a Kind | content ≠ roster; how a Kind is added is 459's | Blueprint §9.4; 064 §5; SC-064-C |
| 25 | The WSV singleton is a Kind with a `KIND-DEFINITION` | it is not a Kind and has no pair | Roadmap PART III, §0.7; SC-068-I |
| 26 | A rejected candidate or a subtype is a legal subject | neither is a declared Kind | RMS Appendix A, §11.1; KD-2 |
| 27 | RMS §13's fourteen admission questions are required content of every `KIND-DEFINITION` | no source makes them family content | §8; KD-7 |
| 28 | Blueprint §9.4's *"Classification: capability"* is current architecture | stale; RMS §10 COLLISION-1 | SC-068-A |
| 29 | Blueprint §9.4's blanket reference prohibition overrides RMS §10.3 | RMS §10.3 corrects it | SC-068-B |
| 30 | The Registry's own `KIND-DEFINITION` needs an axiom Record or a prior definition | no circular self-definition requirement | RMS §10.4; SC-068-H |
| 31 | This document is a `KIND-DEFINITION` Record because its metadata says `canonical-about-meaning` | it is a specification | SC-068-G |
| 32 | `CD: yes` licenses a direct write into `canon/**` | the flag *"licenses nothing"* | Artifact 003 (`CD`); Roadmap §0.8 |
| 33 | A `KIND-DEFINITION` about a World Kind decides World Truth | canon about meaning only | RMS §24; §11 |
| 34 | VERDICT is a declared P Kind because a VERDICT Kind-Definition row exists | a definition is not proof of declared status; VERDICT is provisional | CONFLICT-A; SC-068-J |
| 35 | The subject's model scope requires a separate Model reference field | the form is 069's | RF-068-4; SC-063-G |
| 36 | Governing a Kind's definition gives the Registry the model's own Kind meaning or taxonomy | two custodians; LS-1 keeps them apart | §11; SC-068-K |

## 19. Source Conditions and Gaps

### SC-068-A — stale Registry classification — CLOSED AT SOURCE

Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* RMS §10,
COLLISION-1: the line is *"stale and requires a Blueprint wording fix"*. **Treatment:** the
Registry is a sovereign Record Model and a `KIND-DEFINITION` is a Record of it; the stale line is
not current law. No Blueprint text is edited.

### SC-068-B — older reference prohibition vs RMS §10.3 — CLOSED AT SOURCE

Blueprint §9.4 and §13.6e: *"a Registry definition may never reference a kind, a subtype, or an
instance"*. RMS §10.3: *"v0.1 stated the boundary too bluntly"*, and declared Kinds are an
admissible category. Artifact 063 SC-063-A resolves the condition for reference legality in RMS
§10.3's favour. **Treatment:** the declared Kind subject is legal (RF-068-1); domain instances stay
forbidden, and *"a kind may never reference an instance"* stands (RF-068-5); the downward-only
dependency law survives as Artifact 062's (§15). The two texts are not averaged.

### SC-068-C — definition vs admission — SETTLED BY FROZEN CONTRACT

Artifact 057 §4 and §9 and C-057-08 separate roster presence, Registry definition and admission,
and assign the Registry no authority to admit another model's Kind; Artifact 063 §8 makes a
`KIND-DEFINITION` no proof of declared status. **Treatment:** a `KIND-DEFINITION` requires an
already-declared Kind and infers no admission authority (KD-2, KD-7; §8).

### SC-068-D — Registry LS-1 self-hosting — RESOLVED BY AUTHOR DECISION

Roadmap §0.7 and Artifact 003 (AD-LS1-R-BOOTSTRAP) assign the Registry's fourteen concrete
`KIND-DEFINITION`s to row 075, specified by row 074, with 064 ↔ 075 as the Registry's pairs.
**Treatment:** 068 stays the generic family specification and 069 the generic schema; no competing
pair or mechanism is invented, and the partners are not waived (§16).

### SC-068-E — versionability required before its mechanics exist

Row 068 requires *"versionable"*; rows 108–110 own the mechanism. **Treatment:** the obligation is
stated (§13) and no representation or algorithm is defined. Nothing in this document prohibits the
representation 108–110 later establish. This is a downstream boundary, not permission to pre-build
108–110.

### SC-068-F — RR-16 text unavailable

`Req: RR-16` is carried exactly. Its text is not in the source set (GAP-C). No compliance with
unread requirement text is claimed; this artifact is validated against row 068's `Val` and `Done`,
its cited sources and the frozen contracts.

### SC-068-G — Roadmap `Canon` metadata vs Artifact 003's docs-specification convention

| | |
|---|---|
| **Source fact — Roadmap row 068** | Row 068 explicitly assigns this artifact `T: doc` · `Canon: canonical-about-meaning` · `CD: yes`. These values are preserved exactly. |
| **Source fact — Artifact 003** | `Canon` *"records a per-artifact status, nothing more"*, and, as a general convention, *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`."* `CD` marks whether an artifact *"creates, carries or directly impacts canonical data"* and *"licenses nothing"*. |
| **Source fact — directory** | `docs/registry/PURPOSE.md` holds family specifications and excludes Registry Records: *"those are minted into `canon/registry/`, only through the Mutation Coordinator after G-CANON-R"*. |
| **Convention / decomposition inconsistency** | Artifact 068 is a documentation specification under `docs/registry/`, yet row 068 assigns it `Canon: canonical-about-meaning` rather than Artifact 003's general docs-specification value, `Canon: n/a`. |
| **Source gap** | No current source explains why row 068 carries the non-default `Canon` value. No rationale is invented. |
| **Treatment** | Row 068's explicit metadata governs Artifact 068's identity and is preserved exactly; Artifact 003 remains the general convention and is not changed. This artifact has no authority to reconcile the two: the inconsistency is **recorded, not resolved**. Artifact 068 remains `T: doc` and a specification, not a Registry Record; it creates no canonical data and performs no canonical write; `CD: yes` licenses nothing. Route: ROADMAP / CONVENTION ISSUE, non-blocking — this artifact's own metadata is explicit and its `Val` and `Done` remain evaluable. |

### SC-068-H — the Registry's own KIND-DEF without a prior KIND-DEF — CLOSED AT SOURCE

Blueprint §13.6e leaves OPEN *"how Registry's own KIND-DEF is defined without a prior KIND-DEF"*
(FG-V7-05, *"REQUIRES AUTHOR DECISION"*). RMS §10.4 closes FG-V7-05 (`AUTHOR-DECIDED`): the
Bootstrap Meta-Contract is constitutional and not a Record; *"There is no circular self-definition
requirement."* **Treatment:** the `KIND-DEFINITION` about the Kind `KIND-DEFINITION` is an ordinary
Registry Record of row 075's set; no axiom Record and no regress are introduced (§16).

### SC-068-I — Kind counts, the WSV singleton and the P roster — RESOLVED FOR BUILD

| | |
|---|---|
| **Source facts** | RMS §13: *"W 7+1 · E 7 · P 13 · R 14 · V 3 · I 5 = 50 Kinds across six models"*. RMS §7: WSV is *"World state, not an instance-bearing Kind"*. Roadmap PART III: LS-1 *"49 pairs"*, and *"the WSV singleton is not a Kind and has no pair"*; §0.7 calls this *"a build reconciliation, not a taxonomy rule"*. RMS §9.1 closes P at thirteen; row 405 states *"this is the fourteenth P Kind, admitted here with rationale"*. |
| **Build resolution** | Roadmap §0.7 and Artifact 003 (the 49); the Revolving Resolution Note, CONFLICT-A: P is the thirteen RMS-frozen Kinds, with VERDICT a provisional roadmap extension. |
| **Treatment** | §10 counts 49 Kinds. WSV is not counted and has no `KIND-DEFINITION`. P counts its thirteen RMS-frozen Kinds; VERDICT is not counted while it is provisional, and the family applies to it unchanged once its declared status is established. CONFLICT-A is not reopened, and no taxonomy rule is made here. |

### SC-068-J — VERDICT's Kind-Definition precedes VERDICT's admission — RECORDED, NON-BLOCKING

| | |
|---|---|
| **Source facts** | Row 399, VERDICT Kind-Definition: `H: 069,398` · `LS: LS-1` · `G: G-CANON-R`. Row 405, VERDICT Record spec: `H: 398–404,298` · `LS: LS-1`, with *"this is the fourteenth P Kind, admitted here with rationale"*. Row 398 is the Verdict Format specification. Row 298, the P taxonomy, requires *"exactly thirteen"*. |
| **Condition** | The Roadmap orders VERDICT's `KIND-DEFINITION` before the row that admits VERDICT, and row 399's `H` names no artifact that declares VERDICT a P Kind. KD-2 requires a declared subject; LS-1 makes 399 and 405 one authoring cycle (Roadmap §0.8). |
| **Source gap** | Whether that shared authoring cycle satisfies KD-2's order for VERDICT is not established. |
| **Treatment** | KD-2 is stated as the sources require it. No row is reordered or repaired. Under Artifact 063 RB-6, a VERDICT `KIND-DEFINITION` is not a legal definition while VERDICT's declared status cannot be established. Route: ROADMAP ISSUE, with CONFLICT-A; non-blocking for this artifact — row 399 is P15, and no current `Val` or `Done` of row 068 depends on it. |

### SC-068-K — Kind meaning has two custodians — READING RECORDED

| | |
|---|---|
| **Source facts** | RMS §5 lists *"Kind meaning"* and *"Kind taxonomy"* as model-owned. Blueprint §13.9a: *"the kind taxonomy and the meaning of any kind are owned by the Record Model"*. Blueprint §13.6e gives the Registry *"The definition of a kind"*; Artifact 064 §9 makes a `KIND-DEFINITION` *"the governed definition of what one Kind means"*. Rows 184, 185, 189, 195 and 406 require model artifacts to conform to their Kind-Definition set. |
| **Reading** | RMS §5 and §13.9a state what the shared identity grammar does not decide — a Kind's meaning is not universal and not the grammar's — while §13.6e states the definition-versus-ownership boundary. The sources' own mechanism for holding both is the LS-1 custody split (Roadmap PART III; Artifact 003). |
| **Source gap** | Which side yields if a model's Kind specification and its `KIND-DEFINITION` diverge is not established beyond LS-1, which makes a one-sided landing incomplete, and the conformance `Val`s of the rows above. |
| **Treatment** | Neither side receives the other's custody (KD-4, KD-10). No precedence rule is invented. Route: SOURCE GAP, non-blocking — row 068's `Val` and `Done` are evaluable without it. |

### SC-068-L — the Registry's own L1-family Kinds and the layer law — RECORDED, NON-BLOCKING

| | |
|---|---|
| **Source facts** | Artifact 062 places `KIND-DEFINITION` at L2 (§4.3) and field, relationship-type and indicator definitions at L1 (§6); L1 does not depend on L2 (D-8). Row 075 must author a `KIND-DEFINITION` for each Registry Kind, including those L1 families. Artifact 062 §4.3 *"does not decide whether or how Registry's own Records occupy L4"*. |
| **Source gap** | Whether a Record of an L1 family's Kind semantically depends on that Kind's `KIND-DEFINITION`, and how such a dependency would stand with D-8, is not established. |
| **Treatment** | This document places `KIND-DEFINITION` at L2 as Artifact 062 does, asserts no such dependency, and invents no exemption from D-8. RMS §10.4 rules out a circular self-definition requirement. Route: row 074 (*"self-hosting follows RMS §10.4"*) and row 111 (*"downward-only; asymmetric; no cycles"*); non-blocking. |

### SC-068-M — Kind retirement vs definition deprecation — SOURCE GAP

A retired Kind's records *"remain valid, readable, and historically reachable forever; new records
of that kind are refused by the linter"* (§13.11, via Artifact 057 §6), and row 110 holds
*"deprecated ≠ deleted"*. No source states what happens to a retired Kind's `KIND-DEFINITION`.
**Treatment:** not decided here; it falls to row 110, the owning model and row 459. Non-blocking.

## 20. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-068-01** | The header reproduces row 068's metadata exactly. | row 068 |
| **C-068-02** | `KIND-DEFINITION` is stated to be an existing Registry Kind — Kind 2 of RMS §10.1 — not proposed or open, and no fifteenth Kind is introduced. | RMS §10.1; §6 |
| **C-068-03** | Every `KIND-DEFINITION` defines governed meaning about exactly one declared Kind. | KD-1; RF-068-1 |
| **C-068-04** | The subject must be declared before it is defined; a `KIND-DEFINITION` declares, admits and creates no Kind. | KD-2, KD-3; §8 |
| **C-068-05** | The owning model retains the Kind's taxonomy, declaration, admission, Records and domain meaning; for a Registry Kind, Registry's ownership is stated to come from its own sovereignty, not from the definition. | KD-4; §11 |
| **C-068-06** | Every defined Kind is a Kind of exactly one Record Model; no cross-model, unscoped or modelless subject is admitted. | KD-5 |
| **C-068-07** | The family is shown applicable to the current Kinds of all six models — R 14, W 7, E 7, P 13, V 3, I 5, totalling 49 — and to no non-Kind. | §10 |
| **C-068-08** | The WSV singleton is not counted as a Kind and is given no `KIND-DEFINITION`. | §10; SC-068-I |
| **C-068-09** | P is counted at its RMS-frozen thirteen; VERDICT is not counted while provisional; CONFLICT-A is not reopened. | SC-068-I |
| **C-068-10** | No universal Kind taxonomy, no Kind shared across models and no seventh Record Model is introduced. | KD-8 |
| **C-068-11** | Kind, `KIND-DEFINITION`, Kind specification and Kind schema are kept distinct. | §7; KD-6 |
| **C-068-12** | Row 069 is stated to be the schema of `KIND-DEFINITION` Records, not of any defined Kind. | §7; KD-6 |
| **C-068-13** | Definition is not admission: no admission authority is assigned to the Registry, and the admission questions are not family content. | §8; KD-7 |
| **C-068-14** | No W, E, P, V or I domain instance, and no domain state, is accepted as subject, target or semantic authority. | RF-068-2, RF-068-5 |
| **C-068-15** | No runtime instance is accepted as dependency, target or authority. | RF-068-6 |
| **C-068-16** | The resolution obligation is stated without resolver, lookup or storage mechanics. | §12 |
| **C-068-17** | Versionability is stated without 108–110's mechanics, and the representation they own is not prohibited. | §13 |
| **C-068-18** | Artifact 063's boundary is applied: one source-required subject relation; admissible categories are not mandatory relations; resolvable ≠ legal; a reference transfers nothing. | §14 |
| **C-068-19** | The subject relation is not treated, by itself, as a semantic dependency. | RF-068-9; Artifact 062 D-9 |
| **C-068-20** | `KIND-DEFINITION` stays at L2, with no dependency on L3, L4 or L5. | §15 |
| **C-068-21** | LS-1 is treated as authoring atomicity — not a reference, not by itself a hard dependency, not admission. | §16 |
| **C-068-22** | The 064 ↔ 075 self-hosting resolution is not replaced or bypassed; no axiom Record and no 068 ↔ 069 pair is introduced. | §16; SC-068-D, SC-068-H |
| **C-068-23** | The seven-field universal envelope is unchanged, and no family concept becomes a universal field. | §5; RMS §4 |
| **C-068-24** | None of RMS §4's nine prohibited universal semantics is introduced. | §5; RMS §4 |
| **C-068-25** | No field name, serialization, cardinality syntax, schema language or Kind-subject or Kind-code representation belonging to 069 is designed. | §21 |
| **C-068-26** | No concrete Kind-Definition set — 074, 075, 178, 257, 300, 345, 364 or 399 — is authored, and no `KIND-DEFINITION` Record, identifier or Kind code is minted. | §3; §16 |
| **C-068-27** | None of 065's governance, 111's dependency rules, 112–116's validator, binder, kernel, resolver or validation suite, or 123–124's tests is designed. | §3 |
| **C-068-28** | `Canon: canonical-about-meaning` and `CD: yes` remain exact per-artifact metadata; neither makes this document a Registry Record or authorizes a canonical write; the inconsistency with Artifact 003's convention is recorded, not resolved. | SC-068-G |
| **C-068-29** | RR-16's text is not invented. | SC-068-F |
| **C-068-30** | The Blueprint's stale Registry classification and its older reference wording are recorded with their RMS corrections and not averaged. | SC-068-A, SC-068-B |
| **C-068-31** | This artifact's changes are confined to `docs/registry/kind_definition.md`. | row 068 |

## 21. Concept Separation and Downstream Handoff

| Concept | What it is | Not to be confused with |
|---|---|---|
| Kind | a class of Record within one model (RMS §6.1) | its Registry definition |
| Kind specification | the owning model's architecture of its Kind (RULE G) | the Registry definition of the Kind |
| Kind schema | the owning model's structural contract for the Kind's Records | the Kind's definition; row 069 |
| `KIND-DEFINITION` | the Registry Kind whose Records govern the definition of one declared Kind | the Kind, its admission or its Records |
| `SUBTYPE-DEFINITION` | the definition of one specialization of a Kind | a Kind's definition |
| `MODEL-DEFINITION` | governed meaning about one declared Record Model | a Kind's definition |
| `SCHEMA-DEFINITION` | the definition of a schema's structure | Kind meaning |
| Artifact 068 — this document | the authoritative family specification | a concrete Registry Record or set |
| Artifact 069 | the structural contract every concrete `KIND-DEFINITION` Record conforms to | the schema of any defined Kind |
| 075 · 178 · 257 · 300 · 345 · 364 | the concrete Kind-Definition sets | the generic family |

**To 069** (`H: 068`; `Val`: *"definition resolves; versionable; references only declared entities
(063)"*; `Done`: *"schema"*; `Why`: *"LS-1 — the schema every concrete KIND-DEFINITION Record
conforms to"*). 069 may derive from this document, without redesign:

- the semantic object represented — the governed, Kind-level definition of one declared Kind (§5);
- exactly one declared Kind subject (KD-1; RF-068-1), declared before it is defined (KD-2);
- that the subject is the Kind as one owning Record Model declares it — model scope at the semantic
  level (KD-5);
- definition ≠ admission, ≠ specification, ≠ schema (§7, §8; KD-6, KD-7);
- the Registry / model authority split (KD-4, KD-10; §11);
- L2 placement (§15);
- the resolution obligation (§12) and the versionability obligation (§13);
- the reference rules RF-068-1 to RF-068-9;
- LS-1 semantics and the separation of the generic family from the concrete sets, including the
  Registry's self-hosting (§16);
- the envelope boundary (§5).

069 chooses the structural encoding these require. This document prescribes none of 069's field
names, serialization, schema notation, cardinality syntax, Kind-subject or Kind-code
representation, nullability or default values, and defines no parser or validator behaviour. 069
encodes only the structural consequences of the obligations established here; what this document
defers stays with the owners named below, and nothing here asks 069 to close representation that
rows 108–110 own (§13). Row 069's own `Val` and `Done` are not enlarged, and its `→` — *"all Kind
schemas, 074, 075"* — is its own metadata.

| Other downstream owner | Keeps |
|---|---|
| 074; 075 | the Registry self-Kind definition set contract; the fourteen Registry `KIND-DEFINITION`s |
| 178; 257; 300; 345; 364 (399) | the W, E, P, V and I Kind-Definition sets (VERDICT: SC-068-J) |
| 065 | who may propose, approve and deprecate a definition |
| 108; 109; 110 | evolution; versioning and pinning; supersession and deprecation |
| 111 | concrete definition-dependency rules |
| 112; 113; 114; 115; 116 | reference validator; constraint binder; kernel; Registry definition resolution; validation suite |
| 123; 124 | lockstep tests; P3 conformance |
| 152 | committing `KIND-DEFINITION` Records, after G-CANON-R |
| 459 | how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added — *"each through its own ceremony, never through a generic abstraction"* |

## 22. Roadmap Completion Trace

| Row 068 | Status | Where it is met |
|---|---|---|
| `Val`: *"definition resolves"* | **SATISFIED** — resolution obligation stated; resolvable ≠ legal; mechanics left to the shared mechanism, 114 and 115 | §12 (RS-068-1 to RS-068-5) |
| `Val`: *"versionable"* | **SATISFIED** — obligation stated; mechanics and representation left to 108–110, and not prohibited | §13; SC-068-E |
| `Val`: *"references only declared entities (063)"* | **SATISFIED** — one declared-Kind subject; Artifact 063's boundary applied, with domain-instance and runtime rejection | §14 (RF-068-1 to RF-068-9); KD-2 |
| `Done`: *"every Kind definable"* | **SATISFIED** — all 49 Kinds of the six models covered; non-Kinds excluded | §10 |
| `Why`: *"defines the KIND-DEFINITION family every LS-1 Kind-Definition set uses"* | **SATISFIED** — the generic family is specified; the concrete sets stay with their rows | §5, §9, §16 |
| `H: 064` | **SATISFIED** — the taxonomy and `KIND-DEFINITION`'s responsibility consumed unchanged | §6 |
| `LS: LS-1` | **PRESERVED** — read through row 068's `Why`; the 064 ↔ 075 resolution untouched; no partner invented | §16; SC-068-D |
| `→ 069` | **SATISFIED** — semantic contract handed off; no schema built | §21 |

No Kind created, declared or admitted. No Registry data created. No schema, field, resolver,
version mechanism or concrete `KIND-DEFINITION` created.

---

*Artifact 068 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. This document specifies the `KIND-DEFINITION` family from Record
Model System §2, §4–§6.1, §10–§10.4 and §13, Master Blueprint §9.4, §13.6e, §13.7c and §13.9a, and
Roadmap row 068, with Artifact 064 as its input. It is not a Registry Record, holds no canonical
data, defines no schema, field, validator or algorithm, and implements nothing. Where it differs
from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those governing
sources are correct and this document is wrong.*
