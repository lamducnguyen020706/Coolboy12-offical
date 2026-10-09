# COOLBOY12 — SUBTYPE-DEFINITION Specification

**Artifact 070** · SUBTYPE-DEFINITION spec · `docs/registry/subtype_definition.md` · Own: R ·
RM: R · T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining · Canon: canonical-about-meaning ·
CD: yes · Ph/St: P3/3b · Req: RR-16 · BP: §9.4 · RMS: §10.1 · H: 064 · S: — · LS: LS-1 · G: — ·
→ 071 · Val: definition resolves; versionable; references only declared entities (063) ·
Done: subtypes definable · Why: V asset forms are subtypes, not Kinds · Risk: medium · ∥: yes

## 1. Purpose

This specification answers one question — **what must a `SUBTYPE-DEFINITION` mean about one
specialization of one parent Kind, so that subtype semantics are governed, resolvable, versionable
and legally referenced, without promoting the subtype to a Kind, owning a domain instance,
collapsing subtype meaning into a controlled vocabulary, inventing a subtype-admission ceremony,
or pre-building Artifact 071?**

COOLBOY12 keeps apart four things that are easy to merge:

```
LINEAGE                            a World Kind — the broad Record class (RMS §6.1, §7)
HOUSE within LINEAGE               a specialization — a classification within that Kind
                                   (Blueprint §9.4, §13.6)
SUBTYPE-DEFINITION about HOUSE     an R-partition Registry Record governing what that
                                   specialization means
a Lineage classified as a house    a World Record of Kind LINEAGE — still a Lineage
```

Row 070's `Why` — *"V asset forms are subtypes, not Kinds"* — names the case that makes the family
necessary. RMS §11.1 keeps Visual at three Kinds and places its production forms under
`VISUAL-ASSET`: *"Production forms are a Registry-governed subtype vocabulary, not Kinds"*. Without
a governed subtype family, Artifact 064 records what breaks: *"specializations have no governed
home and are pushed up into Kinds"* (064 §10, question 14).

`SUBTYPE-DEFINITION` already exists. It is Kind 3 of RMS §10.1's *"Final Kind taxonomy — CLOSED at
fourteen"*, and Artifact 064 §10 records its admission rationale. This document does not decide
whether the Kind exists; it specifies what a valid `SUBTYPE-DEFINITION` means, so that row 070's
`Done` — *"subtypes definable"* — holds.

```
OWNING RECORD MODEL — one of W · E · P · R · V · I
    ├── declares the parent Kind in its own taxonomy; keeps its Records and domain semantics
    └── its Records carry the classification as kind + <kind>_type (Blueprint §13.6)

REGISTRY SUBTYPE-DEFINITION
    ├── governs the meaning of ONE specialization within ONE declared parent Kind
    ├── depends semantically on "Registry, its kind" — the L3 layer (Artifact 062)
    ├── is not a Kind, a KIND-DEFINITION, a controlled vocabulary or an instance
    ├── resolves as a Registry definition and is versionable
    └── obeys Artifact 063's reference boundary
            ↓
Artifact 071 — encodes this family structurally
```

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: ARCH` · `SoT: AUTHORITATIVE` about the `SUBTYPE-DEFINITION`
family · `Auth: defining` · `Canon: canonical-about-meaning` · `CD: yes`. This document is a family
specification. It is **not** a `SUBTYPE-DEFINITION` Record: it mints no identity, holds no
Registry data, defines no subtype vocabulary, admits no Kind or subtype, and writes nothing under
`canon/` (SC-070-I). The `Canon` and `CD` values are row 070's metadata for this artifact; they do
not turn a `T: doc` specification into a Registry Record. Where it differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources are right and
this document is wrong.**

`Req: RR-16` is reproduced from row 070. The requirement register is not in the supplied source
set, so the ID is carried forward unverified and no requirement text is stated for it (GAP-C;
SC-070-C).

Statements below are labelled where it matters: **source fact** (stated by the Blueprint, the RMS,
the Roadmap or a frozen artifact), **required synthesis** (a conclusion several source facts force
together; not a quotation), **reading** (an interpretation, recorded as one), and **source gap**
(not established, and not filled here).

## 3. Scope

**In scope.** What a specialization is in COOLBOY12, and what a `SUBTYPE-DEFINITION` means as a
Registry definition family; how parent-Kind semantics, subtype semantics and instance data relate;
why a subtype is not a Kind, a subtype definition not an instance, not a `KIND-DEFINITION` and not
a controlled vocabulary; how subtype meaning stays scoped to its parent Kind; how the frozen
`kind` + `<kind>_type` representation relates to subtype semantics; per-Kind vocabulary
divergence; the Visual production-form case; the resolution, versionability and reference
obligations; ownership; the universal boundaries; the `LS` label; the handoff to 071.

**Out of scope, by owner.**

| Not defined here | Owner |
|---|---|
| the Registry's fourteen Kinds and their admission rationale | 064 (consumed, §5) |
| the Kind Admission Test; the admission of any Kind | 057; the owning model |
| each model's Kind taxonomy, Kind specifications, field architecture and Record schemas — including the field that carries a Kind's classification | that model's own rows |
| the schema encoding of the semantic obligations established here | 071 |
| `KIND-DEFINITION` | 068–069 |
| `CONTROLLED-VOCABULARY`, and any value set it governs | 081–082 |
| the concrete VISUAL-ASSET subtype vocabulary | 350 |
| who may propose, approve or deprecate a definition | 065 |
| evolution, versioning, supersession, deprecation | 108, 109, 110 |
| concrete definition-dependency rules | 111 |
| reference validator; constraint binder; kernel; resolution service; validation suite | 112; 113; 114; 115; 116 |
| committing any `SUBTYPE-DEFINITION` Record to `canon/registry/` | 152, after G-CANON-R (Roadmap §0.8) |
| how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added | 459 |

No Kind, subtype, vocabulary, field, schema, Record, fixture, test or runtime behaviour is created,
and no Kind or subtype is declared, admitted, renamed or retired.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where it says so
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done, handoffs; §0.7 and §0.8 rulings
        ↓
frozen artifacts; Artifact 003 conventions
        ↓
Artifact 070
```

| Source | What it gives this specification |
|---|---|
| RMS §6; §6.1 | *Kind* — *"A class of Record within one model"*; *Definition* — *"A Registry Record specifying meaning"*, test *"Governs; never instantiates"*; what a Record Model owns |
| RMS §2; §4; §5 | six sovereign models; the universal envelope and the nine prohibitions; Kind meaning and Kind taxonomy model-owned |
| RMS §10; §10.1; §10.3; §10.4 | Registry sovereign; `SUBTYPE-DEFINITION` is Kind 3; the reference boundary; bootstrap closed |
| RMS §11.1; §13; Appendix A; Appendix H (PC-4); Final Freeze Gate | Visual's three Kinds and its production-form subtypes; *"why not a subtype"*; `VISUAL-DERIVATIVE` *"(projection or subtype)"*; the VISUAL-ASSET subtype vocabulary as a CONTROLLED-VOCABULARY; *"Visual asset production forms are subtypes"* |
| Blueprint §9.4 | Registry holds *"kind definitions, subtype definitions"*; the *Subtype semantics* row; per-Kind vocabularies and the forced-union prohibition; resolution is not Registry work; architecture frozen, content extensible |
| Blueprint §13.1; §13.6; §12.13 | `<kind>_type` *"Registry-defined"*; the frozen `kind` + `<kind>_type` rule (O-02); the re-homing map; Reclassify (World) |
| Blueprint §13.6e; §13.7; §13.7c | the definition categories; the definition-versus-ownership boundary; the lockstep rule; canonical about meaning |
| Roadmap row 070; PART III (LS-1); §0.7; §0.8 | this artifact's identity; LS-1; Registry self-hosting; authoring vs canonical materialization |
| Roadmap rows 071, 081, 082, 108–116, 152, 346–350, 459 | neighbours' responsibilities |
| Artifact 064 (`H: 064`) | Kind 3; its responsibility and fourteen admission answers; *"content is 070's"* |
| Artifacts 057, 061, 062, 063, 065 | the ladder and its subtype rung; the authority boundary; L3 placement; the reference boundary, under which subtypes are reached as Registry definitions; governance |
| Artifacts 003, 052, 068 | the `Canon`, `CD` and `LS` conventions; Registry canonical about meaning; the `KIND-DEFINITION` family, for comparison only |

Artifacts 057, 061, 062, 063, 065, 003, 052 and 068 are consumed as frozen constraints. They are
not declared dependencies of row 070 and are not added to `H` or `S`. Artifacts 071, 081 and 082
do not yet exist in the repository; their Roadmap rows are cited, not their content.

Citations are to the repository copies in `docs/sources/`: the Blueprint is
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md` (revision header v0.7.0), the RMS
`COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`, the Roadmap `COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`.

## 5. Inherited Contract from Artifact 064

`H: 064` is consumed unchanged.

- **Fourteen Kinds.** `SUBTYPE-DEFINITION` is Kind 3 of RMS §10.1. It is not renamed, merged into
  `KIND-DEFINITION` or `CONTROLLED-VOCABULARY`, or replaced, and no fifteenth Kind is introduced.
  Blueprint §13.6's `SUBTYPE-DEF` is a source alias of the RMS name, not a further Kind (064 §5).
- **Responsibility.** 064 §6 row 3: *"what one specialization of a Kind means"*.
- **Semantic object and question.** 064 §10: *"the governed definition of one specialization of a
  Kind"*; *"what is true of this specialization of a Kind?"*
- **Identity.** 064 §10 question 3: *"each subtype definition is distinct and must be governed and
  provenanced"* — carried at §16.
- **Persistent state.** 064 §10 question 4: *"the defined meaning of one subtype; content is
  070's"* — specified at §6.
- **Lifecycle.** 064 §10 question 5: the family *"participates in Registry's model-owned
  definition evolution"*; versioning and supersession *"are 108–110's"* — carried at §17.
- **Authority.** 064 §10 question 6: *"Registry governs the definition; the owning model keeps the
  domain semantics of its Records using the subtype"*.
- **What references it.** 064 §10 question 7: *"not established — §9.4 makes instances and
  projections depend on subtype semantics — a dependency, not a Record reference; row 071's `→` is
  an unlock"*. This document establishes no inbound reference either. What a `SUBTYPE-DEFINITION`
  itself references is settled at §18.
- **Neighbouring Kinds.** 064 §10 question 11: *"it defines subtypes; it is not itself a
  specialization of `KIND-DEFINITION` — the sources keep the two rows and the two Kinds apart"*.
  Question 13 names `KIND-DEFINITION` as the reduction target: *"carrying it as a Kind definition
  would make each specialization a Kind, which row 070 rules out"*.
- **Admission not reopened.** 064 §10 answers the fourteen questions for this Kind; this
  specification does not revisit them.
- **What 064 leaves open.** 064 does not state the boundary between `SUBTYPE-DEFINITION` and
  `CONTROLLED-VOCABULARY`; it is drawn here only as far as the sources allow (§11; SC-070-E).
- **No common family checklist.** 064 §27 hands each row of 066–107 *"exactly the specification or
  schema responsibilities, `Val` and `Done` the Roadmap and governing sources assign each row"*.

## 6. What a SUBTYPE-DEFINITION Is

**Source facts.**

- Blueprint §9.4: the Registry holds reusable semantics — *"kind definitions, subtype
  definitions"* among them — and its *Subtype semantics* row holds *"What is true of one
  specialization (e.g. `HOUSE` within `LINEAGE`)"*, depending on *"Registry, its kind"* and depended
  on by *"Instances, projections"*.
- A *Definition* is *"A Registry Record specifying meaning"*; its test is *"Governs; never
  instantiates"* (RMS §6.1). Registry Records are semantic-definition Records — *"not
  configuration, not code constants, not metadata, not a catalog, not runtime"* (RMS §10).
- Blueprint §13.6e places `SUBTYPE-DEF` in the category *"Structural definition"*, which governs
  *"What a Record of a kind is"*, beside `KIND-DEF` and `FIELD-DEF`.
- Artifact 064 §10: the semantic object is *"the governed definition of one specialization of a
  Kind"*; the persistent state is *"the defined meaning of one subtype; content is 070's"*.

**Definition (synthesis).** A `SUBTYPE-DEFINITION` is a Registry semantic-definition Record that
governs the meaning of one specialization within the scope of one declared parent Kind: what is
true of that specialization, as a specialization of what is true of every Record of the parent
Kind. It governs that meaning and never instantiates it — it creates no Kind and no Record, and
transfers neither the parent Kind nor its Records to the Registry.

**Content (synthesis — the part 064 §10 assigns here).** The family's persistent content is the
meaning of the specialization and nothing else. It is not:

- the parent Kind's meaning, which is the parent's `KIND-DEFINITION`'s (§7; SD-8);
- the value set of a classification — a Registry-owned, per-Kind vocabulary (Blueprint §13.6),
  for `VISUAL-ASSET` a `CONTROLLED-VOCABULARY` (PC-4) — (§11; SD-9);
- any Record of the parent Kind, any value such a Record carries, or what is true of one (SD-4);
- the field, schema or validation that carries or checks the classification on Records (§9; SD-11);
- the parent Kind's place in a taxonomy, or its admission (SD-2);
- the owning model's domain semantics of the Records that use the subtype — including, for a
  Visual asset, its actual provenance and Visual's provenance meaning (SD-7; §12).

The *Structural definition* label of §13.6e names the governed subject — what a Record of a kind
is. It does not make a `SUBTYPE-DEFINITION` the structure of any Record: *"The Registry is not
schema."* (Blueprint §9.4). This is recorded as a reading.

## 7. Subtype vs Kind vs Instance vs KIND-DEFINITION

> **A subtype is not a Kind; its `SUBTYPE-DEFINITION` is neither the Kind, nor the Kind's
> `KIND-DEFINITION`, nor any Record.**

Shown for World's `HOUSE` within `LINEAGE`:

| Object | What it is | Owner | Source |
|---|---|---|---|
| `LINEAGE` | a World Kind — *"this cross-generational hereditary or ancestral structure"* | World, in its taxonomy | Blueprint §13.6; RMS §7 |
| `HOUSE` | a specialization of `LINEAGE` — *"A house is one form of hereditary structure among several — dynasty, clan, bloodline. Subtype is exactly sufficient."* | its meaning is governed by the Registry; it is carried on World Records as a classification | Blueprint §9.4, §13.6 |
| the `KIND-DEFINITION` about `LINEAGE` | the Registry Record governing the definition of the Kind | Registry | Artifact 068 |
| the `SUBTYPE-DEFINITION` about `HOUSE` | the Registry Record governing what the specialization means | Registry | Blueprint §9.4; 064 §10 |
| the value set of `LINEAGE`'s classification | a Registry-owned, per-Kind vocabulary | Registry | Blueprint §13.6 |
| a Lineage that is a house | one World Record of Kind `LINEAGE`, schematically `W-LI-<ordinal>-<slug>` | World | RMS §7; I-16 |

A `SUBTYPE-DEFINITION` does **not**: create a `HOUSE` Kind or Kind code; admit anything to World's
taxonomy; create, hold or own a Lineage Record; decide which houses exist or what is true of one;
or serve as the parent Kind's `KIND-DEFINITION`. A particular house — one dynasty in the world — is
a World `LINEAGE` Record, never Registry content: *"A registry entry that names a specific thing in
the world is a misfiled Record."* (Blueprint §9.4).

**Subtype is a rung, not a Kind.** P-7's ladder runs both ways — *"an existing kind that a subtype
or field could carry is walked back down it (Section 13.6)"* (Artifact 057 §6) — and §13.11's
refusal *"names the correct rung: field, subtype, relationship, Concept, or Registry entry"*
(Artifact 057 §7). RMS §13 asks every Kind *"why not a subtype"*. A concept a subtype can carry is
therefore not a Kind, and receiving a `SUBTYPE-DEFINITION` does not make it one.

## 8. Parent Kind and Model Scope

**Required synthesis.**

- A specialization is a specialization of its Kind: the *Subtype semantics* row depends on
  *"Registry, its kind"* (Blueprint §9.4), and `<kind>_type` is *"domain classification within the
  kind, Registry-defined"* (Blueprint §13.1). A Kind is a class of Record within exactly one model
  (RMS §6.1; C-057-04). Every `SUBTYPE-DEFINITION` is therefore scoped to exactly one parent Kind of
  exactly one owning Record Model.
- The parent must be a declared Kind, with declared status established by the owning model's own
  Kind architecture (Artifact 063 §7 row 3, §8). A `SUBTYPE-DEFINITION` neither declares nor admits
  its parent Kind.
- There is no free-floating subtype. Because each `<kind>_type` vocabulary is per-Kind (Blueprint
  §13.6) and subtype semantics depend on their own Kind (Blueprint §9.4), the same word under two
  Kinds names two specializations, each scoped to its own Kind; no subtype spans Kinds or models.
- Classification changes no Record's partition or Kind: a Lineage classified as a house is still a
  World `LINEAGE` Record (§9).
- Whether subtype semantics may depend on a Kind other than their own is not established (Artifact
  062 §6; SC-070-M). How parent-Kind scope is encoded is 071's (Artifact 063 SC-063-G).

## 9. The `kind` + `<kind>_type` Representation

**Source facts.** The current Blueprint revision lists among its closures *"O-02 `kind` +
`<kind>_type`"*. Blueprint §13.6, under *How a specialization is recorded (frozen)*: *"A kind is
the broad Record class; a `<kind>_type` is the domain classification within it."* and *"There is
one classification field, not two"*. *"A subtype relationship still exists conceptually"*; *"What
changed is only how the record expresses it"* — `kind: LINEAGE` + `lineage_type: house`. *"The
vocabulary of each `<kind>_type` is Registry-owned and per-kind"*. Older open-item lists that still
carry the question as undecided are historical (SC-070-K).

**Semantic consequence (synthesis).**

- The subtype relationship is conceptual. A Record expresses it through its Kind and one
  classification value; the `SUBTYPE-DEFINITION` governs what that classification means.
- A classified Record remains a Record of its parent Kind. Classification mints no Kind, and the
  classification is no part of the identity grammar, which carries partition, Kind, ordinal and
  slug (RMS §5). In World this is explicit: Reclassify — *"An object changes its `<kind>_type`
  within its kind."* — keeps identity: *"Identity persists; recorded as an ordinary revision with
  its reason."*, *"a classification change rather than a kind conversion"* (Blueprint §12.13). That
  is World's identity rule; identity semantics are model-owned and it is not extended to other
  models here (RMS §6).
- There is one classification, not a second specialization field; this family adds none.

**What 070 does not define.** The classification field's name in any model, its type, cardinality,
serialization or validation. Fields are universal, model or Kind tier (RMS §14); `<kind>_type` is
not a universal field and no universal subtype field exists (RMS §4). The field belongs to the
owning model's field architecture. For `VISUAL-ASSET` the field name is not established by current
sources, so examples here write it schematically as `<kind>_type` (SC-070-L).

## 10. Subtype Semantics and Layer Placement

**Source fact.** Artifact 062 §4.3: *"L3 — Subtype semantics. Registry holds the governed
`SUBTYPE-DEFINITION` where one applies."* and *"The owning Record Model keeps the domain semantics
of its Records that use the subtype."* Artifact 062 §5: L3 depends on L1 and its own Kind in L2.

| | |
|---|---|
| **May depend on** | L1 — shared field semantics and the peer semantic authorities; L2 — its own Kind (Artifact 062 §6) |
| **Must not depend on** | L4 instance data, L5 derived output (Artifact 062 D-3, D-8) |
| **May be depended on by** | L4 instances, L5 projections (Blueprint §9.4; Artifact 062 §6) |
| **Ownership at L3** | the Registry governs the `SUBTYPE-DEFINITION`; the owning model keeps the domain semantics of its Records that use the subtype (Artifact 062 §4.3) |

**Consequences.**

- Subtype semantics specialize their Kind's semantics and never redefine them. Meaning is defined
  above and specialized downward, and no layer takes defining semantic authority from a
  higher-numbered layer (Artifact 062 §5, D-1, D-8). A `SUBTYPE-DEFINITION` cannot invalidate or
  override what is true of every Record of its parent Kind.
- Subtype semantics are not instance truth. Records depend on them; they do not depend on Records
  (Artifact 062 D-3).
- The dependency on *"its kind"* is semantic and source-established; no representation choice
  creates or removes it. A declaration reference is not by itself a semantic dependency (Artifact
  062 D-9). How parent-Kind scope is structurally carried — naming the declared Kind, or an R → R
  reference to its `KIND-DEFINITION` — is 071's (RF-070-3); concrete definition-dependency rules
  are row 111's. A `SUBTYPE-DEFINITION` that depends on its parent's `KIND-DEFINITION` does not own
  it, and *"a domain Kind or subtype is not an R Record"* (Artifact 062 §8).
- The layers order meaning. They set no evaluation, loading or resolution order, and create no
  edge between Record Models (Artifact 062 §7).

## 11. SUBTYPE-DEFINITION vs CONTROLLED-VOCABULARY

**Source facts.**

- RMS §10.1 lists `SUBTYPE-DEFINITION` (Kind 3) and `CONTROLLED-VOCABULARY` (Kind 7) as separate
  Kinds. Blueprint §9.4 lists *"subtype definitions"* and *"controlled value sets"* as separate
  Registry content. Blueprint §13.6e places them in different categories: *"Structural definition"*
  and *"Semantic definition"* — *"What a value or term means"*.
- Artifact 064: a `SUBTYPE-DEFINITION` asks *"what is true of this specialization of a Kind?"*; a
  `CONTROLLED-VOCABULARY` is *"a governed set of values or terms and their meaning"* and asks
  *"what does this value or term mean, for this Kind?"* (064 §10, §14).
- RMS §11.1 calls the production forms *"a Registry-governed subtype vocabulary"*, and RMS
  Appendix H, PC-4: *"VISUAL-ASSET subtype vocabulary must be created as a Registry
  CONTROLLED-VOCABULARY before V artifacts are built"*.
- Row 350, the VISUAL-ASSET subtype vocabulary, carries `H: 348,071,082` — it is built on both this
  family's schema and the controlled-vocabulary schema.

**Required synthesis.** Neither family is the other. A `SUBTYPE-DEFINITION` governs what is true of
one specialization of a Kind. A `CONTROLLED-VOCABULARY` governs a set of values or terms and their
meaning — for `VISUAL-ASSET`, the governed value set of its production forms (PC-4). A vocabulary
that lists a value does not thereby define the specialization's semantics, and a
`SUBTYPE-DEFINITION` does not thereby create or govern a value set.

**Source gap.** No current source states the cardinality, identity or reference relation between
the two, and their semantic questions overlap where a vocabulary value names a specialization. This
document asserts none of the following: one `SUBTYPE-DEFINITION` per vocabulary value; one
vocabulary per parent Kind; a required vocabulary reference in every `SUBTYPE-DEFINITION`; any
mandatory R → R edge between them. Row 350 builds the concrete VISUAL-ASSET vocabulary on both
schemas and owns that combination (SC-070-E).

**Both families keep per-Kind divergence.** Blueprint §9.4: *"Shared structure, independent
vocabulary"* — a value vocabulary *"is per-kind and may legitimately diverge"*; *"Divergent per-kind
value sets are the intended design, not a defect to be unified"*, and *"a forced enum union across
kinds is prohibited"*. That structure/vocabulary split belongs to the Registry architecture that
*"is settled and changes only by amendment"* (Blueprint §9.4). Row 081's `Done` repeats the rule
for the vocabulary family: *"per-kind value sets may diverge; forced enum union prohibited"*.
Subtypes of different Kinds are never pooled into one universal subtype enum or taxonomy (SD-10).

## 12. The Visual Production-Form Case

**Source facts.** RMS §11.1: `VISUAL-ASSET` is *"a manifestation of a specification"*, one of
Visual's three Kinds; *"Production forms are a Registry-governed subtype vocabulary, not Kinds"*;
*"They differ by provenance of production, not semantic role."* The RMS Final Freeze Gate records
*"V taxonomy closed at three primary Kinds"* and *"Visual asset production forms are subtypes"*.

| Form | Status | Source |
|---|---|---|
| `GENERATED-IMAGE` · `PHOTOGRAPH` · `ILLUSTRATION` · `COVER-IMAGE` | production-form subtypes of `VISUAL-ASSET` | RMS §11.1 |
| `DERIVATIVE` | a subtype of `VISUAL-ASSET` *"where a durable derivative requires identity"* | RMS §11.1 |
| `VISUAL-DERIVATIVE` | rejected as a standalone Kind: *"A rebuildable derivative is a derived projection."*; *"A durable derivative requiring identity becomes a VISUAL-ASSET with subtype and provenance."* | RMS §11.1, §13 |
| `VISUAL-REFERENCE` | rejected as a standalone Kind — *"field / provenance / reference structure"*; not among the production forms | RMS §11.1 |

**What the case proves.** The RMS keeps the production forms out of Visual's Kind taxonomy — they
differ *"by provenance of production, not semantic role"* — yet each still has a meaning that needs
a governed home. That is exactly what this family provides. A production form is a possible
`SUBTYPE-DEFINITION` subject whose value sits in the VISUAL-ASSET subtype vocabulary (PC-4; row
350); it is never a fourth Visual Kind.

**Reading — provenance.** Because the forms *"differ by provenance of production"*, a
`SUBTYPE-DEFINITION` for one of them says what that production form is. It does not record any
asset's actual provenance, which the Visual Record carries, and it does not define provenance
meaning, which is Visual's (RMS §6). Provenance capture is a shared mechanism; provenance meaning is
model-owned (RMS §4).

**Not done here.** None of the five forms is authored as a Record, made canonical or listed as
Registry data; the concrete vocabulary is row 350's. A definition of `GENERATED-IMAGE` owns no
`VISUAL-ASSET` instance and makes no asset canonical: Visual canon is the description, never the
asset (RMS §11.1). The Blueprint's older Visual roster, which lists the forms as kinds, is
superseded for this purpose (SC-070-J).

## 13. Family Rules

| ID | Rule | Basis |
|---|---|---|
| **SD-1** | **One definition, one specialization, one parent Kind.** A `SUBTYPE-DEFINITION` governs the meaning of exactly one specialization within exactly one parent Kind of exactly one owning Record Model. It is never a free-floating or global subtype, and never spans Kinds or models. How the subject and its scope are encoded is 071's. | Blueprint §9.4 (*"its kind"*), §13.1, §13.6; RMS §6.1; 064 §10 question 1; synthesis |
| **SD-2** | **The parent Kind is declared first.** The parent must already be a declared Kind of its owning model, with declared status established by that model's own Kind architecture. The definition neither declares nor admits the parent Kind, and writing, approving or committing it does not make a candidate a Kind. | Artifact 063 §7 row 3, §8, RB-1, RB-6; C-057-02, C-057-08 |
| **SD-3** | **A subtype is not a Kind.** A specialization receives no Kind code, Kind identity, Kind admission or place in a Kind taxonomy because it has governed meaning. | RMS §11.1; RMS §13; 064 §10 questions 13–14; Artifact 057 §6, §7 |
| **SD-4** | **Governs; never instantiates.** The definition is semantic. It is not a Record of the parent Kind, creates no such Record, contains or owns none, and carries no executable behaviour. | RMS §6.1; RMS §10; Blueprint §9.4 |
| **SD-5** | **Classified Records stay Records of their Kind.** Records carry a specialization as classification within their Kind (`kind` + `<kind>_type`). Classification creates no new Kind, partition, Record Model or Kind identity. | Blueprint §13.6; §12.13 (World); RMS §4 |
| **SD-6** | **Subtype semantics specialize the parent and never redefine it.** They depend on *"Registry, its kind"*, may be depended on by instances and projections, never depend on instances or derived output, and cannot invalidate or override the parent Kind's semantics. They are not instance truth. | Blueprint §9.4; Artifact 062 §5, D-1, D-3, D-8 |
| **SD-7** | **The model keeps its Records and domain semantics.** Registry owns the `SUBTYPE-DEFINITION` Record. The owning model keeps its taxonomy, its Records, which Records carry which classification, the domain semantics of its Records that use the subtype, and its identity, state, lifecycle, temporal, provenance, canonicality and package semantics. | Blueprint §13.6e; I-105; 064 §10 question 6; Artifact 062 §4.3, §8 |
| **SD-8** | **Not a `KIND-DEFINITION`.** A `SUBTYPE-DEFINITION` defines one specialization of a Kind; it is not a specialization of `KIND-DEFINITION` and does not define the Kind itself. | 064 §10 questions 11, 13; RMS §10.1 |
| **SD-9** | **Not a `CONTROLLED-VOCABULARY`.** Specialization meaning and a governed value set are held by different Registry Kinds. Neither is collapsed into the other, and no cardinality, identity or reference rule between them is invented. | RMS §10.1; Blueprint §9.4, §13.6e; RMS Appendix H PC-4; 064 §10, §14; SC-070-E |
| **SD-10** | **Per-Kind divergence; no forced union.** Classification vocabularies may differ between Kinds. No universal subtype enum, global subtype taxonomy or cross-Kind subtype superclass is created. | Blueprint §9.4, §13.6; RMS §4; row 081 `Done` |
| **SD-11** | **No field or schema here.** The record-level representation is the frozen `kind` + `<kind>_type`; this family defines no field name, type, cardinality, serialization or validation, and no universal subtype or `<kind>_type` field. | Blueprint §13.6; RMS §4, §14 |
| **SD-12** | **No addition ceremony here.** How a new subtype — including a new visual subtype — is added is not defined here. Registry content, `<kind>_type` vocabularies included, extends by ordinary Registry change; row 459 owns how a visual subtype is added, and Artifact 065 owns who may propose, approve or deprecate a definition. | Blueprint §9.4; row 459; Artifact 065; SC-070-F |
| **SD-13** | **Committed only through the governed path.** A `SUBTYPE-DEFINITION` Record reaches `canon/registry/` only through row 152, after G-CANON-R. This specification creates none, and neither its `Canon` nor its `CD` value licenses a write. | Roadmap §0.8; Artifact 003 (`CD`); Spine law 2; SC-070-I |

## 14. Subtype Definability

Row 070 `Done`: *"subtypes definable"*.

**Required synthesis.**

1. Every specialization is a specialization of one Kind (Blueprint §9.4, §13.1), and every Kind
   belongs to exactly one of the six models (RMS §2, §6.1).
2. The parent is a declared Kind, an admissible Registry reference category whatever its model
   (RMS §10.3; Artifact 063 §7 row 3).
3. The family requires nothing model-specific (SD-1 to SD-13): no Relationship Record or History
   Record (I-102), no `status` or `tier` (RMS §4), and none of a model's own lifecycle, temporal
   architecture, canonicality or package (RMS §6).
4. The Registry *"must not require the complete semantic implementation of every other Record Model
   in order to define them"* (Blueprint §13.6e; Artifact 062 D-7).

Therefore a specialization that the sources, or the owning model's own design work, establish for a
declared Kind of any of the six models is definable by this family, with no per-model variant. The
family does not itself establish that any specialization exists.

| Model | Parent Kind | Specializations the sources attest | Source |
|---|---|---|---|
| **W** | `LINEAGE` | `HOUSE` | Blueprint §9.4, §13.6 |
| **W** | `ORGANIZATION` | `POLITY` | Blueprint §13.6 |
| **W** | `CONCEPT` | `CULTURE` · `TECHNOLOGY` · `SYMBOL` · `FORCE`; `THEME` where world-internal | Blueprint §13.6 |
| **W** | `EVENT` | `SIGNAL` | Blueprint §13.6 |
| **V** | `VISUAL-ASSET` | `GENERATED-IMAGE` · `PHOTOGRAPH` · `ILLUSTRATION` · `COVER-IMAGE` · `DERIVATIVE` | RMS §11.1 |
| **E · P · R · I** | — | none attested by current sources; the family applies once a model establishes one, and none is invented here | — |

The table cites examples to show the family applies; it is not a subtype roster, admits nothing,
mints no Record or value, and is not Registry data. `ERA` is not listed: the Blueprint records it
as an `EVENT` subtype *"accepted with reservation"* and lists its classification as *"REMAINING
OPEN"*. `VISUAL-REFERENCE` is not listed: the RMS makes it a *"field / provenance / reference
structure"*.

Row 070's *"subtypes definable"* does not mean that every subtype is authored now — *"Not every
future Registry entry needs authoring now"* (Blueprint §9.4) — nor that any vocabulary is
materialized, that an addition ceremony exists, that the schema exists, or that resolution runs.

## 15. Authority, Ownership and Canonicality

**Source fact.** *"Registry governs the definitions. Each Record Model owns its Records."*
(Blueprint §13.6e; I-105).

| Registry governs | The owning Record Model governs | Registry never infers | Source |
|---|---|---|---|
| the `SUBTYPE-DEFINITION` Record and the specialization meaning it carries | its Kind taxonomy and the parent Kind's admission | a Kind for the subtype; admission authority; a change to any model's roster | Blueprint §13.6e; Artifact 057 §9; I-106 |
| — | which Records exist, which classification each carries, and what they mean in its domain | ownership of any Record of the parent Kind | Blueprint §13.6e; I-105; RMS §10.3 |
| — | the domain semantics of its Records that use the subtype | any of those semantics through a definition | Artifact 062 §4.3; 064 §10 question 6 |
| — | its identity, state, lifecycle, temporal, provenance, canonicality and package semantics, and its Record schemas | any of those, for any model | RMS §6; SD-7 |

**Applied.** The `SUBTYPE-DEFINITION` about `HOUSE` governs what the specialization means. It does
not create a `HOUSE` Kind or a Lineage Record, own World Records, decide which houses exist, or make
the Registry the World model. The definition of `GENERATED-IMAGE` owns no `VISUAL-ASSET` instance.
Artifact 061 §8 lets the Registry define *"definitions of visual vocabularies, subtypes and
contracts, where the sources establish them"*, while Visual keeps its Records and Visual semantics.
Registry authority is domain-scoped: *"All authority is domain-scoped."* (RMS §17).

**Canonical about meaning.** Row 070 carries `Canon: canonical-about-meaning` as this artifact's
metadata (SC-070-I). A committed `SUBTYPE-DEFINITION` is canonical about meaning as Registry
definitions are — *"This definition is the authoritative meaning records resolve against"*
(Blueprint §13.7c; Artifact 052 §5.4) — and never World Truth: *"Registry is canon about meaning
only; it can never override World Truth"* (RMS §24). It makes no Visual asset canonical.
Canonicality is not universalized (I-104).

## 16. Resolution Contract

Row 070 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-070-1** | A `SUBTYPE-DEFINITION` is a Registry definition Record, distinct, governed and provenanced (064 §10 question 3). Once materialized it carries ordinary Record identity under the universal grammar and envelope (RMS §4, §5) — the baseline identity later Registry-definition resolution requires. That identity is an R Record's: it is neither the parent Kind, nor the specialization's classification value, nor a Kind code. The slug is decoration only and never the basis of resolution (RMS §5). |
| **RS-070-2** | A consumer must be able to resolve a materialized `SUBTYPE-DEFINITION`. Reference resolution is universal and mechanical (RMS §4); *"Reference resolution is not Registry work."* (Blueprint §9.4). Registry definition resolution by id and version is row 115's (*"consumer resolves by id+version"*); create, resolve and version operations are row 114's (*"create/resolve/version a definition"*). This document does not supply the complete id+version representation; version representation is 108–110's. |
| **RS-070-3** | Successful resolution does not establish reference legality: *"Resolvable ≠ legal."* (Artifact 063 §11). |
| **RS-070-4** | Resolution transfers nothing. Resolving a `SUBTYPE-DEFINITION` creates no Kind, admits nothing, and gives the Registry no Record of the parent Kind. |
| **RS-070-5** | No resolver, lookup, index, cache, storage path, fallback, version-selection logic or classification-value lookup is defined here; how a consumer finds the definition of a given specialization is not defined here (114; 115; 071). |

## 17. Versionability Boundary

Row 070 `Val`: *"versionable"*.

**Source facts.** A Registry definition has *"a governed change path, and a temporal account"*
(Blueprint §13.6e). Artifact 064 §10 question 5: the family *"participates in Registry's
model-owned definition evolution"*. Row 108 owns the evolution model (`Val`: *"version"*; `Done`:
*"temporal account without a World History Record"*); row 109 owns versioning (*"consumers pin a
version"*); row 110 owns supersession and deprecation (*"deprecated ≠ deleted"*).

| ID | Obligation |
|---|---|
| **VS-070-1** | A `SUBTYPE-DEFINITION` participates in governed Registry definition evolution and must be capable of carrying versioned meaning under the model rows 108–110 define. Every version stays bound by SD-1 to SD-13. The Registry's temporal account is its own: no World History Record is used or required (row 108; I-102). |
| **VS-070-2** | **Not defined here ≠ forbidden.** That this document defines no version mechanism is not a decision that a `SUBTYPE-DEFINITION` carries no version, supersession or deprecation information. Rows 108–110 keep their authority to establish the Registry-owned representation, and nothing here asks 071 to close it. Whatever they establish stays Registry-owned: it adds no field to the universal envelope and is not a version, lifecycle or state model shared by W, E, P, V or I (RMS §4, §16, §19). |

**Not decided here** (108–110): a version field or identifier; numbering; revision identifiers;
*latest* semantics; pin representation; supersession, replacement or deprecation representation;
effective dates; migration; compatibility; retention; deletion. Who may propose, approve or
deprecate a definition is 065's.

## 18. Reference Boundary

Row 070 `Val`: *"references only declared entities (063)"*. Artifact 063 binds this family as a
constraint; it is not added to `H`. Artifact 063 §22 leaves to each family *"which concrete
reference relations each family carries"*; for this family the answer is below.

| ID | Rule | Basis |
|---|---|---|
| **RF-070-1** | **Parent-Kind scope is required.** Every `SUBTYPE-DEFINITION` is scoped to one parent Kind, which must be a declared Kind of its owning model; declared status is established by that model's Kind architecture, this family defines no proof formula, and an undetermined parent is not legal. This is one required scope obligation; it does not fix a closed count of concrete reference relations or of structural carriers, and its structural encoding is 071's. | Artifact 063 §7 row 3, §8, RB-1, RB-6; SD-1, SD-2 |
| **RF-070-2** | **No declared-subtype category.** RMS §10.3 names no subtype category, and Artifact 063: *"The matrix has no row for declared subtypes, fields, relationship types, vocabularies, validators or capabilities as categories of their own: those are reached as Registry definitions (row 1)."* A specialization is reached through its `SUBTYPE-DEFINITION`; another Registry definition that names it makes an R → R reference, where that family's own contract carries one. This family invents no subtype declaration target. | RMS §10.3; Artifact 063 §7, §8.1, SC-063-A; SC-070-H |
| **RF-070-3** | **Parent Kind ≠ its `KIND-DEFINITION`.** Naming the parent Kind is a declaration reference; a relation to the parent's `KIND-DEFINITION` is an R → R reference (Artifact 063 §8.3). Which form carries parent-Kind scope is 071's; no URI, handle, string syntax or discriminator is invented here. | Artifact 063 §8.3, SC-063-G |
| **RF-070-4** | **No invented concrete references.** Other Registry definitions — a `KIND-DEFINITION` or a `CONTROLLED-VOCABULARY` among them — declared Record Models, declared schemas and declared semantic contracts are admissible categories; that obliges no `SUBTYPE-DEFINITION` to reference any of them. No reference list, vocabulary reference, schema reference, model reference or dependency list is defined. A structural reference may encode only an obligation established here — the parent-Kind scope — or representation a named downstream owner establishes (§17), adds no semantic relation or authority of its own, and must satisfy Artifact 063. Admissible category ≠ concrete family relation. | Artifact 063 RB-5, §22 |
| **RF-070-5** | **No domain instance.** No Record of W, E, P, V or I — a particular Lineage, a particular `VISUAL-ASSET` — and no domain state is the subject, a reference target, a dependency or the semantic authority of a `SUBTYPE-DEFINITION`. Blueprint §9.4's *"a kind may never reference an instance"* stands in full. | RMS §10.3; Artifact 063 §9, SC-063-A |
| **RF-070-6** | **No runtime instance.** No running service, worker, session, process, plugin instance, image generator, schema engine, validator process or live object is the subject, a reference target, a dependency or the semantic authority of a `SUBTYPE-DEFINITION`. What `GENERATED-IMAGE` means is not taken from any generator that produced an asset. | RMS §10.3; Blueprint §9.4; Artifact 063 §13 |
| **RF-070-7** | **Resolvable ≠ legal.** A target that resolves mechanically may still be illegal, and a target that cannot be established is not legal either. | Artifact 063 §11 |
| **RF-070-8** | **No transfer through reference.** A legal reference transfers no ownership, mutation authority, semantic authority, admission, canonicality or source-of-truth class. | Artifact 063 §12 |
| **RF-070-9** | **Reference ≠ dependency.** Subtype semantics depend semantically on their own Kind (Blueprint §9.4; Artifact 062 §5). A declaration reference is not by itself a semantic dependency; how parent-Kind scope is structurally carried is 071's (RF-070-3), and concrete definition-dependency rules are row 111's. Records' dependence on subtype semantics is *"a dependency, not a Record reference"* (064 §10 question 7). | Artifact 062 D-9; Artifact 063 RB-5; 064 §10; row 111 |

Blueprint §9.4's older wording — *"A Registry definition may never reference a kind, a subtype, or
an instance"* — is not current law for reference legality. RMS §10.3 corrects it (*"v0.1 stated the
boundary too bluntly"*), and Artifact 063 applies the correction (SC-070-B).

## 19. Envelope and Universal-Semantics Boundary

Once materialized, a `SUBTYPE-DEFINITION` carries the universal envelope unchanged — `partition` ·
`kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4) — in partition
R. The envelope's `kind` names the Record's own Kind, `SUBTYPE-DEFINITION`; it is not the parent
Kind and not the specialization. No family concept — the subtype, the parent Kind, a classification
value, a vocabulary, a version, a status, a lifecycle, a deprecation flag or an authority — becomes
a universal field. How the obligations of this document are structurally encoded is 071's.

None of RMS §4's nine prohibited universal semantics is introduced. For this family that means:
subtyping is no universal superclass system and no Universal Record Base; there is no universal
subtype identity grammar or identity composition; there is no global subtype taxonomy and no forced
universal subtype enum (no universal Kind taxonomy); a `SUBTYPE-DEFINITION` is no universal schema
inherited by domain Records (no universal semantic schema); and no model's state or lifecycle
semantics move into the Registry (no universal state model or lifecycle). No Relationship Record or
History Record, and no universal canonicality, arises from a specialization.

## 20. LS-1 Metadata Condition

Row 070 carries `LS: LS-1`, preserved exactly. Roadmap PART III defines LS-1 as *"every Kind spec ↔
its Registry KIND-DEFINITION. ATOMIC-PAIR."* A specialization is not a Kind, and a
`SUBTYPE-DEFINITION` is neither a Kind specification nor a `KIND-DEFINITION`. PART III's eight
lockstep systems include no subtype pair.

- **No pair is invented.** This document creates no subtype ↔ `SUBTYPE-DEFINITION` pair, no new
  lockstep class, no hard dependency, no Record reference and no commit atomicity from the label.
- **Lockstep is not a reference** and not, by itself, a hard dependency: *"A lockstep partner is
  not a predecessor."* (Artifact 003).
- **The Registry's own pairs stand.** Under AD-LS1-R-BOOTSTRAP (Roadmap §0.7; Artifact 003) the
  Registry's fourteen Kind ↔ `KIND-DEFINITION` pairs are 064 ↔ 075; one of row 075's fourteen
  concerns the Kind `SUBTYPE-DEFINITION`. Nothing here replaces that.

How row 070's label relates to PART III and to the 064 ↔ 075 resolution is not stated by any
source; it is recorded, not resolved (SC-070-D).

## 21. Worked Examples

All examples are **schematic**: no identifier is minted, no Kind code or field name is chosen, and
nothing here is Registry data.

**A. Legal — World subtype semantics.** `HOUSE` within `LINEAGE`. `LINEAGE` stays the World Kind;
house is a classification within it, written by the Blueprint as `kind: LINEAGE` +
`lineage_type: house`. A `SUBTYPE-DEFINITION` may govern what that specialization means. A
concrete Lineage remains a World Record, and this document creates no field or schema for it.

**B. Legal — a Visual production form.** `GENERATED-IMAGE` within `VISUAL-ASSET`. `VISUAL-ASSET`
stays one of Visual's three Kinds; `GENERATED-IMAGE` is a production-form subtype whose value
belongs to the VISUAL-ASSET subtype vocabulary (PC-4; row 350). A `SUBTYPE-DEFINITION` may govern
what the form means; Visual owns every asset Record, written schematically as `kind: VISUAL-ASSET`
with its classification in a `<kind>_type`-style field. The difference between forms is provenance
of production, not semantic role.

**C. Illegal — promoting a subtype to a Kind.** The claim that `GENERATED-IMAGE` is a fourth
Visual Kind is rejected: production forms are *"a Registry-governed subtype vocabulary, not Kinds"*
(RMS §11.1; SD-3). So is treating `PHOTOGRAPH` as a separate sovereign Record class because it is a
production form, and so is a standalone `VISUAL-DERIVATIVE` Kind.

**D. Illegal — a domain instance as authority.** A `SUBTYPE-DEFINITION` that takes what
`GENERATED-IMAGE` means from one particular `VISUAL-ASSET` Record is rejected: a domain instance is
never semantic authority (RF-070-5).

**E. Illegal — a free-floating global subtype.** A "house" subtype defined with no parent Kind, or
meant to apply to every Kind that has a house-like classification, is rejected: a specialization is
always within one Kind (SD-1).

**F. Illegal — a forced global enum.** Merging `lineage_type`, `organization_type` and the
VISUAL-ASSET production forms into one universal subtype enum for convenience is rejected (SD-10;
Blueprint §9.4).

**G. Boundary — definition vs vocabulary.** The VISUAL-ASSET subtype vocabulary is a
`CONTROLLED-VOCABULARY` (PC-4); what `GENERATED-IMAGE` means as a specialization is this family's
subject. Whether every value of that vocabulary has its own `SUBTYPE-DEFINITION`, and how the two
connect, is not established and is not decided here (SC-070-E).

**H. Boundary — derivatives.** A thumbnail rebuilt on demand is a derived projection, not a Record
and not a subtype. A durable derivative that needs identity is a `VISUAL-ASSET` carrying the
`DERIVATIVE` subtype and its provenance (RMS §11.1).

**I. Deferred — a new visual subtype.** This family can define the meaning of a further production
form once one is added. How it is added is row 459's (*"each through its own ceremony, never
through a generic abstraction"*); no ceremony is invented here, and no new subtype name is proposed.

## 22. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | A subtype is a Kind | subtypes are a lower rung; production forms are *"not Kinds"* | RMS §11.1; Artifact 057 §6; SD-3 |
| 2 | A `SUBTYPE-DEFINITION` creates or admits a Kind | it governs meaning; admission is not a definition's | RMS §6.1; C-057-08; SD-2, SD-4 |
| 3 | A `SUBTYPE-DEFINITION` owns Records of the parent Kind | *"Each Record Model owns its Records."* | Blueprint §13.6e; I-105; SD-7 |
| 4 | Registry ownership of subtype meaning transfers model ownership | definition authority ≠ Record ownership | 064 §10 question 6; Artifact 062 §8 |
| 5 | `<kind>_type` is a new universal envelope field | the envelope stays seven fields | RMS §4, §14; §19 |
| 6 | All subtype vocabularies must share one enum | per-Kind divergence is intended; forced union prohibited | Blueprint §9.4, §13.6; SD-10 |
| 7 | A `SUBTYPE-DEFINITION` is the same thing as a controlled vocabulary | distinct Kinds and categories | RMS §10.1; Blueprint §13.6e; SD-9 |
| 8 | A controlled vocabulary that lists a value thereby defines that specialization's meaning | listing a value is not defining subtype semantics | §11; SD-9 |
| 9 | An admissible target category creates a mandatory reference | category ≠ concrete relation | Artifact 063 RB-5; RF-070-4 |
| 10 | A reference transfers ownership or authority | it transfers nothing | Artifact 063 §12; RF-070-8 |
| 11 | A resolvable target is automatically legal | resolvable ≠ legal | Artifact 063 §11; RS-070-3 |
| 12 | A domain instance may establish what a subtype means | instances are never semantic authority | RMS §10.3; RF-070-5 |
| 13 | A running generator, service or validator may be semantic authority | runtime instances are excluded | RMS §10.3; RF-070-6 |
| 14 | *Versionable* lets 070 invent version fields | the mechanics are 108–110's | §17 |
| 15 | `Canon: canonical-about-meaning` authorizes a direct `canon/**` write | it is per-artifact metadata | Artifact 003 (`Canon`); SD-13; SC-070-I |
| 16 | `CD: yes` licenses canonical materialization | the flag *"licenses nothing"* | Artifact 003 (`CD`); Roadmap §0.8; SD-13 |
| 17 | `LS: LS-1` proves a subtype-specific lockstep pair exists | LS-1 is Kind spec ↔ `KIND-DEFINITION`; no subtype pair exists | Roadmap PART III; §20 |
| 18 | 070 may define 071's schema because 071 is its successor | the encoding is 071's | row 071; §25 |
| 19 | 070 may define the visual subtype ceremony because Visual motivates it | the ceremony is row 459's | row 459; SD-12 |
| 20 | The five RMS production forms are five new Visual Kinds | Visual is closed at three Kinds | RMS §11.1; Final Freeze Gate |
| 21 | Every vocabulary value has exactly one `SUBTYPE-DEFINITION` | no source fixes that cardinality | SC-070-E |
| 22 | Because 070 defines no version mechanism, a `SUBTYPE-DEFINITION` can never carry version information | not defined here ≠ forbidden | VS-070-2 |
| 23 | RMS §10.3 lets a Registry definition reference a "declared subtype" category | no such category exists; subtypes are reached as Registry definitions | Artifact 063 §7; RF-070-2 |
| 24 | Subtype semantics may override the parent Kind's semantics | they specialize downward and cannot invalidate L2 | Artifact 062 §5, D-8; SD-6 |
| 25 | A subtype definition is the parent Kind's `KIND-DEFINITION` | distinct Kinds at distinct levels | 064 §10 question 11; SD-8 |
| 26 | Classifying a Record changes its Kind, Record Model or partition, or writes the classification into its identity | classification stays within the Kind; the identity grammar carries the Kind, not the classification | Blueprint §13.6; RMS §5; SD-5 |
| 27 | The specialization-field vs `<kind>_type` question is still open | the current revision closed it | Blueprint O-02; SC-070-K |
| 28 | Blueprint §9.4's *"Classification: capability"* is current architecture | stale; RMS §10 COLLISION-1 | SC-070-A |
| 29 | Blueprint §9.4's blanket reference prohibition overrides RMS §10.3 | RMS §10.3 corrects it | SC-070-B |
| 30 | A `SUBTYPE-DEFINITION` for a production form records or defines an asset's provenance | the asset carries its provenance; provenance meaning is Visual's | RMS §4, §6; §12 |

## 23. Source Conditions and Gaps

Each entry gives the two source statements (or the missing source), the condition, whether this
artifact owns its resolution, and the treatment.

### SC-070-A — stale Registry classification — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* |
| **Source B** | RMS §10, COLLISION-1: *"Registry is a sovereign Record Model"*; the §9.4 line is *"stale and requires a Blueprint wording fix"* (RMS Appendix H, PC-1). |
| **Condition** | The Blueprint line classifies the Registry as a capability; the RMS makes it a sovereign Record Model. |
| **Owner** | Not this artifact — closed at source by the RMS; any Blueprint wording fix is the author's act. |
| **Treatment** | The Registry is a sovereign Record Model and a `SUBTYPE-DEFINITION` is a Record of it. No Blueprint text is edited. |

### SC-070-B — older reference prohibition vs RMS §10.3 — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §9.4 and §13.6e: *"a Registry definition may never reference a kind, a subtype, or an instance"*. |
| **Source B** | RMS §10.3: *"v0.1 stated the boundary too bluntly"*. Artifact 063 SC-063-A applies the correction for reference legality and adds: *"Subtypes are reached as Registry definitions (§8.1)."* |
| **Condition** | The older text forbids naming a kind or a subtype; RMS §10.3 admits declared Kinds and other Registry definitions and keeps domain instances forbidden. |
| **Owner** | Not this artifact — closed at source by RMS §10.3 and applied by Artifact 063. |
| **Treatment** | §18 applies RMS §10.3 and Artifact 063; domain instances stay forbidden; the two texts are not averaged; no Blueprint text is edited. |

### SC-070-C — RR-16 text unavailable — SOURCE GAP

| | |
|---|---|
| **Source A** | Row 070: `Req: RR-16`. |
| **Source B** | Missing — the requirement register is not in the source set (GAP-C). |
| **Gap** | The requirement's text cannot be read. |
| **Owner** | Not this artifact. |
| **Treatment** | The ID is carried exactly; no requirement text is stated and no compliance with unread requirement text is claimed. This artifact is validated against row 070's `Val` and `Done`, its cited sources and the frozen contracts. Non-blocking (GAP-C). |

### SC-070-D — LS-1 on row 070 — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Source A** | Row 070 carries `LS: LS-1`. |
| **Source B** | Roadmap PART III defines LS-1 as *"every Kind spec ↔ its Registry KIND-DEFINITION. ATOMIC-PAIR."*, with the *Why* *"custody split (BP §13.7)"*; the Registry's own pairs are 064 ↔ 075 (AD-LS1-R-BOOTSTRAP). Blueprint §13.7's lockstep rule makes a change to *"kinds, `<kind>_type` vocabularies, or the package model"* that lands in only one of its two custody documents a defect. |
| **Condition** | A `SUBTYPE-DEFINITION` is not a Kind specification or a `KIND-DEFINITION`, and no source states how row 070's label relates to PART III's pairs, or whether §13.7's mention of `<kind>_type` vocabularies is meant to reach LS-1. |
| **Owner** | Not this artifact; reconciling the label is the Roadmap author's. |
| **Treatment** | The label is preserved exactly; no subtype pair, lockstep class, dependency or reference is invented; 064 ↔ 075 stands (§20). Route: ROADMAP ISSUE, non-blocking for row 070's `Val` and `Done`. |

### SC-070-E — SUBTYPE-DEFINITION and CONTROLLED-VOCABULARY — SOURCE GAP

| | |
|---|---|
| **Source A** | Distinct RMS §10.1 Kinds; distinct §9.4 content and §13.6e categories; 064 §10 and §14 give overlapping semantic questions. |
| **Source B** | RMS PC-4 makes the VISUAL-ASSET subtype vocabulary a CONTROLLED-VOCABULARY; row 350 builds it on both 071 and 082. |
| **Gap** | No source fixes the cardinality, identity or reference relation between subtype definitions and vocabulary values, or draws the exact line where a vocabulary value names a specialization. 064 §10 names only `KIND-DEFINITION` as the reduction target. |
| **Owner** | Not this artifact: rows 081–082 own the vocabulary family and row 350 the concrete VISUAL-ASSET vocabulary. |
| **Treatment** | The families stay distinct (§11; SD-9). No one-to-one pairing, mandatory vocabulary reference or R → R edge is invented. Non-blocking: subtype meaning is definable without the mapping. |

### SC-070-F — how a subtype comes to exist — DEFERRED, NOT INVENTED

| | |
|---|---|
| **Source A** | Blueprint §9.4: Registry content — `<kind>_type` vocabularies among it — *"extends by ordinary Registry change"*. Blueprint §13.6: the vocabulary is *"Registry-owned and per-kind"*, and a kind in a boundary-naming roster may be *"demoted to a subtype by the model's own design work"*. Artifact 065 governs who may propose, approve and deprecate a definition. Row 459 covers *"how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added"* — *"each through its own ceremony, never through a generic abstraction"*. |
| **Source B** | Missing — no current source defines a generic subtype admission test or a subtype declaration act, or states how ordinary Registry change and row 459's ceremony relate for a subtype. |
| **Gap** | How a specialization comes to exist, and is added, before it is defined. |
| **Owner** | Not this artifact: row 459 owns the extensibility contract, Artifact 065 governance, and each model its own design work. |
| **Treatment** | This family owns subtype meaning, not addition mechanics; none is invented (SD-12). Non-blocking: meaning is definable once a specialization exists. |

### SC-070-G — 071's unlock and the Visual vocabulary rows — RECORDED, NON-BLOCKING

| | |
|---|---|
| **Source A** | Row 070 `→ 071`; row 071 `→ 347`. |
| **Source B** | Row 347, the CANONICAL-VISUAL-SPECIFICATION schema, carries `H: 346` only. Row 350, the VISUAL-ASSET subtype vocabulary, carries `H: 348,071,082`, yet row 071's `→` does not name it; row 082's `→ 347,400` shows the same pattern. |
| **Condition** | Row 071's declared unlock does not match the row that actually depends on it. |
| **Owner** | Not this artifact; Roadmap repair is the author's. |
| **Treatment** | `→ 071` is preserved; 070 does not claim to unlock 350, does not rewrite row 071, and assigns row 347 nothing. Route: ROADMAP ISSUE, non-blocking. |

### SC-070-H — no "declared subtype" reference category — SETTLED BY FROZEN CONTRACT

| | |
|---|---|
| **Source A** | RMS §10.3 lists other Registry definitions and declared Record Models, Kinds, schemas and semantic contracts; it names no subtype category. |
| **Source B** | Artifact 063 §7: subtypes have no category of their own; they are *"reached as Registry definitions (row 1)"*. |
| **Condition** | Whether a specialization is itself a declared reference target. |
| **Owner** | Settled by Artifact 063, a frozen contract; nothing is left for this artifact to resolve. |
| **Treatment** | The parent Kind is the only declaration-level target this family requires; the specialization is reached through its `SUBTYPE-DEFINITION`; no subtype declaration category is invented (RF-070-1, RF-070-2). |

### SC-070-I — Roadmap `Canon` metadata vs Artifact 003's docs-specification convention

| | |
|---|---|
| **Source fact — Roadmap row 070** | Row 070 assigns `T: doc` · `Canon: canonical-about-meaning` · `CD: yes`. These values are preserved exactly. |
| **Source fact — Artifact 003** | `Canon` *"records a per-artifact status, nothing more"*, and *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`."* `CD` marks whether an artifact *"creates, carries or directly impacts canonical data"* and *"licenses nothing"*. |
| **Source fact — directory** | `docs/registry/PURPOSE.md` excludes Registry Records: *"those are minted into `canon/registry/`, only through the Mutation Coordinator after G-CANON-R"*. |
| **Inconsistency** | Row 070's explicit `Canon` value differs from Artifact 003's general docs-specification value, and no source explains why. |
| **Owner** | Not this artifact; a Roadmap or convention fix is the author's. |
| **Treatment** | Row 070's metadata is preserved; Artifact 003 is not changed; the inconsistency is **recorded, not resolved**. This document remains a specification, creates no canonical data and performs no canonical write; `CD: yes` licenses nothing (SD-13). Route: ROADMAP / CONVENTION ISSUE, non-blocking. |

### SC-070-J — the Blueprint's Visual roster vs RMS §11.1 — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §13.6 lists Visual kinds including `GENERATED-IMAGE`, `PHOTOGRAPH`, `ILLUSTRATION`, `COVER-IMAGE`, `VISUAL-REFERENCE` and `VISUAL-DERIVATIVE`, and marks that roster *"BOUNDARY-NAMING / PROPOSED"* — a kind in that state may be *"demoted to a subtype by the model's own design work"*. |
| **Source B** | RMS §11.1 closes Visual at three Kinds and makes the production forms subtypes; the Final Freeze Gate records *"Visual asset production forms are subtypes"*. |
| **Condition** | The older roster lists as kinds what the RMS makes subtypes or rejects. |
| **Owner** | Not this artifact — closed at source by the RMS. |
| **Treatment** | RMS §11.1 governs; the older roster is not used as a current taxonomy. |

### SC-070-K — the specialization-field question — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Older Blueprint open-item lists show *"Structural specialization field vs the `<kind>_type` classification field"* as *"REQUIRES DECISION"*. |
| **Source B** | The current revision closes it — *"O-02 `kind` + `<kind>_type`"* — and §13.6 states the frozen rule. |
| **Condition** | Historical open-item wording beside a current closure. |
| **Owner** | Not this artifact — closed at source. |
| **Treatment** | The closure governs; the older entries are historical; the question is not reopened (§9). |

### SC-070-L — the classification field outside World — SOURCE GAP

| | |
|---|---|
| **Source A** | Blueprint §13.6's `<kind>_type` examples are World's. |
| **Source B** | For `VISUAL-ASSET` the RMS says *"VISUAL-ASSET with subtype and provenance"* and names no field; fields are universal, model or Kind tier (RMS §14). |
| **Gap** | No current source names the field that carries the `VISUAL-ASSET` classification. |
| **Owner** | Not this artifact: each model's field architecture owns its fields. |
| **Treatment** | This document names no Visual field and writes the classification schematically. Non-blocking. |

### SC-070-M — subtype dependence on another Kind — NOT ESTABLISHED

| | |
|---|---|
| **Source A** | Blueprint §9.4: subtype semantics depend on *"Registry, its kind"*; Artifact 062 §5: L3 depends on L1 and its own Kind in L2. |
| **Source B** | Artifact 062 §6: the layer table does not say *"whether a Subtype may depend on a kind other than its own"*. |
| **Gap** | Dependence of subtype semantics on a Kind other than its own is not established. |
| **Owner** | Not this artifact: concrete definition-dependency rules are row 111's. |
| **Treatment** | Each `SUBTYPE-DEFINITION` is scoped to one parent Kind (SD-1); no dependency on another Kind is established or invented. Non-blocking. |

## 24. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-070-01** | **Family identity.** `SUBTYPE-DEFINITION` is stated to be Kind 3 of the frozen fourteen-Kind Registry taxonomy; no fifteenth Kind is introduced. | RMS §10.1; §5 |
| **C-070-02** | **One specialization context.** A conforming definition governs one specialization within one parent Kind of one model; no free-floating, global or cross-Kind subtype is defined. | SD-1 |
| **C-070-03** | **Parent Kind.** The parent must be a declared Kind; the definition neither creates, declares nor admits it. | SD-2; RF-070-1 |
| **C-070-04** | **Subtype is not a Kind.** A subtype receives no Kind code, Kind identity or Kind admission. | SD-3 |
| **C-070-05** | **Instance classification.** Classified Records remain Records of the parent Kind; no new Kind identity, partition or Record Model arises from classification. | SD-5 |
| **C-070-06** | **Current representation.** The frozen `kind` + `<kind>_type` rule is preserved, and no field name, type, cardinality or universal field is defined. | §9; SD-11 |
| **C-070-07** | **Per-Kind vocabulary independence.** Classification vocabularies may diverge by Kind; no forced global enum or global subtype taxonomy is introduced. | SD-10 |
| **C-070-08** | **Definition vs vocabulary.** `SUBTYPE-DEFINITION` is not collapsed into `CONTROLLED-VOCABULARY`, and no cardinality, identity or reference rule between them is invented. | §11; SD-9; SC-070-E |
| **C-070-09** | **No domain-instance authority.** No domain Record or domain state is accepted as subject, target, dependency or semantic authority. | RF-070-5 |
| **C-070-10** | **No runtime-instance authority.** No runtime instance is accepted as subject, target, dependency or semantic authority. | RF-070-6 |
| **C-070-11** | **Ownership.** Registry governs the definition; the owning model keeps its Records and model-owned semantics. | SD-7; §15 |
| **C-070-12** | **Resolution.** The resolution obligation is stated without resolver mechanics and without claiming the complete id+version representation. | §16 |
| **C-070-13** | **Versionability.** Versionability is stated without 108–110's mechanics, and their representation is not prohibited. | VS-070-1, VS-070-2 |
| **C-070-14** | **Reference legality.** Every concrete relation the family establishes complies with Artifact 063: one required parent-Kind scope, no closed carrier count, no invented mandatory relation, no declared-subtype category. | §18 |
| **C-070-15** | **Resolvable ≠ legal.** Mechanical resolution never substitutes for legality. | RS-070-3; RF-070-7 |
| **C-070-16** | **Visual proof case.** `GENERATED-IMAGE` is treated as a `VISUAL-ASSET` production-form subtype, not a Visual Kind. | §12 |
| **C-070-17** | **Derivative boundary.** A rebuildable derivative is a derived projection; a durable identity-bearing derivative is a `VISUAL-ASSET` with subtype and provenance. | §12; RMS §11.1 |
| **C-070-18** | **No subtype extension ceremony.** No subtype addition ceremony, admission test or governance workflow is invented. | SD-12; SC-070-F |
| **C-070-19** | **No direct canon write.** No Registry Record, subtype vocabulary or canonical data is created, and nothing is written under `canon/**`. | §2; §12; SD-13 |
| **C-070-20** | **Handoff.** 071 receives semantic obligations only; no field, serialization, schema language or reference-carrier shape is authored. | §25 |
| **C-070-21** | **LS metadata bounded.** `LS: LS-1` is preserved without inventing a subtype lockstep pair. | §20; SC-070-D |
| **C-070-22** | **Universal boundaries.** The seven-field envelope is unchanged, and none of RMS §4's nine prohibited universal semantics is introduced. | §19 |
| **C-070-23** | **Row metadata.** The header reproduces row 070's metadata exactly. | row 070 |
| **C-070-24** | **Not a `KIND-DEFINITION`.** `SUBTYPE-DEFINITION` is kept distinct from `KIND-DEFINITION`. | SD-8 |
| **C-070-25** | **Layer placement.** Subtype semantics are placed at L3, specialize the parent Kind's semantics, and do not depend on instances or derived output. | §10; SD-6 |
| **C-070-26** | **Reference ≠ dependency.** Reference and semantic dependency are kept distinct. | RF-070-9 |
| **C-070-27** | **Row metadata authorizes nothing.** `Canon` and `CD` remain exact per-artifact metadata, authorize no write, and their inconsistency with Artifact 003 is recorded, not resolved. | SC-070-I; SD-13 |
| **C-070-28** | **Requirement text.** RR-16's text is not invented. | SC-070-C |
| **C-070-29** | **File scope.** This artifact's changes are confined to `docs/registry/subtype_definition.md`. | row 070 |

## 25. Concept Separation and Downstream Handoff

| Concept | What it is | Not to be confused with |
|---|---|---|
| Kind | a class of Record within one model (RMS §6.1) | a subtype of it |
| specialization (subtype) | a classification within one Kind | a Kind; a Registry Record |
| classification value | how a Record carries the specialization (`<kind>_type`) | the specialization's meaning |
| `SUBTYPE-DEFINITION` | the Registry Kind whose Records govern the meaning of one specialization of one Kind | the Kind, its `KIND-DEFINITION`, a vocabulary, a Record of the Kind |
| `KIND-DEFINITION` | the Registry Kind whose Records govern the definition of one declared Kind | a subtype definition |
| `CONTROLLED-VOCABULARY` | the Registry Kind governing a set of values or terms and their meaning | specialization meaning |
| a Record of the parent Kind | a domain Record owned by its model | a subtype definition |
| Artifact 070 — this document | the authoritative family specification | a concrete Record, vocabulary or schema |
| Artifact 071 | the structural contract for `SUBTYPE-DEFINITION` Records | the schema of any domain Kind or vocabulary |
| row 350 | the VISUAL-ASSET subtype vocabulary | this family |

**To 071** (`H: 070`; `Val`: *"definition resolves; versionable; references only declared entities
(063)"*; `Done`: *"schema"*; `Why`: *"LS-1"*). 071 may derive from this document, without redesign:

- the semantic object represented — the governed meaning of one specialization of one Kind (§6);
- exactly one specialization and one parent-Kind scope, the parent a declared Kind of one owning
  model (SD-1, SD-2; RF-070-1);
- subtype ≠ Kind, ≠ instance, ≠ `KIND-DEFINITION`, ≠ controlled vocabulary (§7, §11; SD-3, SD-4,
  SD-8, SD-9);
- the authority and ownership split (SD-7; §15);
- L3 placement and the semantic dependency on the parent Kind (§10; SD-6);
- the resolution obligation (§16; RS-070-1 to RS-070-5) and the versionability obligation (§17;
  VS-070-1, VS-070-2);
- the reference rules RF-070-1 to RF-070-9;
- the `kind` + `<kind>_type` constraint and what 071 must not make universal (§9, §19).

071 chooses the structural encoding these require. This document prescribes none of 071's field
names, serialization, schema notation, cardinality syntax, parent-Kind or specialization
representation, reference-carrier shape, nullability or default values, and defines no parser or
validator behaviour. 071 encodes only the structural consequences of the obligations established
here; nothing here asks 071 to close representation rows 108–110 own (§17). Not delegated to 071:
new semantic relations, a vocabulary or vocabulary linkage, Kind or subtype admission, Registry
governance, evolution and versioning design, reference-validator and resolver implementation, and
any concrete subtype set. Row 071's own `Val` and `Done` are not enlarged, and its `→ 347` is its
own metadata (SC-070-G).

| Other downstream owner | Keeps |
|---|---|
| 081; 082 | the `CONTROLLED-VOCABULARY` family and schema |
| 350 | the concrete VISUAL-ASSET subtype vocabulary |
| 065 | who may propose, approve and deprecate a definition |
| 108; 109; 110 | evolution; versioning and pinning; supersession and deprecation |
| 111 | concrete definition-dependency rules |
| 112; 113; 114; 115; 116 | reference validator (*"rejects any definition referencing a domain instance"*); constraint binder; kernel; Registry definition resolution; validation suite |
| 152 | committing `SUBTYPE-DEFINITION` Records, after G-CANON-R |
| 459 | how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added — *"each through its own ceremony, never through a generic abstraction"* |

## 26. Roadmap Completion Trace

The statuses below assess Artifact 070 as a documentation specification (`T: doc`, `R: ARCH`).
**SPECIFICATION OBLIGATION SATISFIED** means the required semantic rule is stated, mandatory, and
bounded by its governing sources. It does not claim that downstream schemas, vocabularies,
validators, version mechanisms, kernels or resolution services have been implemented, executed or
tested.

| Row 070 | Status | Where it is met |
|---|---|---|
| `Val`: *"definition resolves"* | **SPECIFICATION OBLIGATION SATISFIED** — a materialized `SUBTYPE-DEFINITION` carries baseline Registry Record identity and must be resolvable; resolution is universal, not Registry work; resolvable ≠ legal; id+version resolution is 115's and version representation 108–110's | §16 (RS-070-1 to RS-070-5) |
| `Val`: *"versionable"* | **SPECIFICATION OBLIGATION SATISFIED** — participation in governed Registry definition evolution is required; mechanics and representation stay with 108–110 and are not prohibited | §17 (VS-070-1, VS-070-2) |
| `Val`: *"references only declared entities (063)"* | **SPECIFICATION OBLIGATION SATISFIED** — one required parent-Kind scope, the parent a declared Kind; no declared-subtype category; domain and runtime instances excluded; resolvable ≠ legal; no validator run is claimed | §18 (RF-070-1 to RF-070-9); SD-2 |
| `Done`: *"subtypes definable"* | **SPECIFICATION OBLIGATION SATISFIED** — a specialization established for a declared Kind of any of the six models is definable, with no per-model variant; source-attested cases in W and V shown; no subtype is authored, and the family establishes none | §14 |
| `Why`: *"V asset forms are subtypes, not Kinds"* | **SPECIFICATION OBLIGATION SATISFIED** — the Visual production forms are treated as `VISUAL-ASSET` subtypes, never Kinds | §12; C-070-16 |
| `H: 064` | **SATISFIED** — Kind 3 and its responsibility consumed unchanged | §5 |
| `LS: LS-1` | **PRESERVED** — label kept; no subtype pair invented; 064 ↔ 075 untouched; relation recorded | §20; SC-070-D |
| `→ 071` | **SATISFIED** — semantic contract handed off; no schema built | §25 |

No Kind or subtype created, declared or admitted. No Registry data, vocabulary, schema, field,
resolver or version mechanism created.

---

*Artifact 070 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. This document specifies the `SUBTYPE-DEFINITION` family chiefly
from Record Model System §2, §4–§6.1, §10–§10.4, §11.1, §13 and Appendix H, Master Blueprint §9.4,
§12.13, §13.1, §13.6, §13.6e, §13.7 and §13.7c, and Roadmap row 070, with Artifact 064 as its
input. It is not a Registry Record, holds no canonical data, defines no schema, field, vocabulary,
validator or algorithm, and implements nothing. Where it differs from the Master Blueprint, the
Record Model System, or the OS File Build Roadmap, those governing sources are correct and this
document is wrong.*
