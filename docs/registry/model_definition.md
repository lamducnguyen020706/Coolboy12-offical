# COOLBOY12 — MODEL-DEFINITION Specification

**Artifact 066** · MODEL-DEFINITION spec · `docs/registry/model_definition.md` · Own: R · RM: R ·
T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining · Canon: canonical-about-meaning · CD: yes ·
Ph/St: P3/3b · Req: RR-16 · BP: §9.4 · RMS: §10.1 · H: 064 · S: — · LS: LS-1 · G: — · → 067 ·
Val: definition resolves; versionable; references only declared entities (063) · Done: six
models definable · Why: closes FG-V7-07 · Risk: high · ∥: yes

## 1. Purpose

This specification answers one question — **what must a `MODEL-DEFINITION` mean about one of
COOLBOY12's six already-declared sovereign Record Models, so that it resolves, is versionable, and
obeys the Registry reference boundary without creating, owning or reconstituting that model?**

`MODEL-DEFINITION` already exists. RMS §10.1 lists it first among the Registry's fourteen Kinds,
*"(closes FG-V7-07 — the Kind exists)"*, and RMS §27 records *"MODEL-DEFINITION is a Registry
Kind"*. This document does not decide whether the Kind exists. It specifies what a valid
`MODEL-DEFINITION` means, so that row 066's `Done` — *"six models definable"* — holds and row 066's
`Why` — *"closes FG-V7-07"* — is completed on the family side.

```
CONSTITUTION
    └── exactly six sovereign Record Models already exist:  W · E · P · R · V · I
            ↓
Registry MODEL-DEFINITION
    ├── defines governed meaning about ONE declared model
    ├── resolves as a Registry definition
    ├── is versionable
    ├── obeys Artifact 063's reference boundary
    └── never creates or owns the model
            ↓
Artifact 067 — encodes this semantic contract as a schema
```

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: ARCH` · `SoT: AUTHORITATIVE` about the `MODEL-DEFINITION`
family · `Auth: defining` · `Canon: canonical-about-meaning` · `CD: yes`. This document is a family
specification. It is **not** a `MODEL-DEFINITION` Record, mints no Registry data, and writes nothing
under `canon/` (SC-066-H). The `Canon` and `CD` values apply to Artifact 066 as declared metadata;
they do not change its `T: doc` artifact type into a Registry Record. Where it differs from the
Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources are right
and this document is wrong.**

`Req: RR-16` is reproduced from row 066. The requirement register is not in the supplied source
set, so the ID is carried forward unverified and no requirement text is stated for it (GAP-C;
SC-066-F).

Statements below are labelled where it matters: **source fact** (stated by the Blueprint, the RMS,
the Roadmap or a frozen artifact), **required synthesis** (a conclusion several source facts force
together; not a quotation), and **source gap** (not established, and not filled here).

## 3. Scope

**In scope.** What a `MODEL-DEFINITION` is; the semantic subject it defines; how it differs from
the Record Model it describes; what it means for exactly the six Record Models to be definable; the
identity and meaning obligations that follow from ordinary Registry Record semantics; what
*"definition resolves"* and *"versionable"* mean as obligations; the reference restrictions of
Artifact 063; the authority and ownership the family never acquires; the handoff to 067.

**Out of scope, by owner.**

| Not defined here | Owner |
|---|---|
| the fourteen-Kind taxonomy and admission rationale | 064 (consumed, §6) |
| the schema: field names, serialization, cardinality syntax, schema language | 067 |
| concrete `MODEL-DEFINITION` Records, or any file under `canon/registry/` | not assigned to this artifact |
| `KIND-DEFINITION` and the Registry's own Kind-Definition set | 068–069; 074–075 |
| who proposes, approves or deprecates a definition | 065 |
| evolution, versioning, supersession, deprecation | 108, 109, 110 |
| concrete definition-dependency rules | 111 |
| reference validator, kernel, resolution service | 112, 114, 115 |
| each model's Kind taxonomy, lifecycle, packaging and other owned semantics | each model's own artifacts |
| how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added | 459 |

No Record Model, partition, Kind, field, schema, Record, fixture, test or runtime behaviour is
created.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where it says so
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done, handoffs
        ↓
frozen artifacts; Artifact 003 conventions
        ↓
Artifact 066
```

| Source | What it gives this specification |
|---|---|
| RMS §2 | exactly six sovereign Record Models; *"No model is a superclass of another. World is not a template."* |
| RMS §6; §6.1 | what a Record Model is and the question each answers; *Definition* — *"A Registry Record specifying meaning"*, test *"Governs; never instantiates"* |
| RMS §4 | the universal envelope; the nine prohibited universal semantics; reference resolution as a shared mechanism |
| RMS §10; §10.1; §10.3; §10.4; §27 | Registry sovereign; fourteen Kinds with `MODEL-DEFINITION` first; the reference boundary; bootstrap closed; FG-V7-07 closed |
| Blueprint §9.4 | Registry holds reusable semantics; *"model definitions"* are extensible content; no runtime; resolution is not Registry work |
| Blueprint §13.6e | definitions are Records with *"a governed change path, and a temporal account"*; FG-V7-07 historically OPEN (SC-066-B) |
| Roadmap row 066; PART III (LS-1); rows 064, 065, 067, 074–075, 108–115, 459 | identity and neighbours' responsibilities |
| Artifact 064 (`H: 064`) | the fourteen Kinds; `MODEL-DEFINITION`'s source-grounded responsibility |
| Artifacts 061, 062, 063 | the model row of the authority boundary; layer placement not established; the reference boundary |
| Artifacts 052, 003 | Registry canonical about meaning; the `Canon`, `CD` and `LS` conventions and AD-LS1-R-BOOTSTRAP |

Artifacts 061, 062, 063 and 003 are consumed as frozen constraints. They are not declared
dependencies of row 066 and are not added to `H` or `S`.

## 5. What a MODEL-DEFINITION Is

**Source facts.**

- A Record Model *"is a partition-owned semantic architecture that answers a distinct class of
  question and owns: its Kind taxonomy, identity semantics, state and lifecycle, relationship
  packaging, temporal architecture, provenance meaning, canonicality meaning (if any), semantic
  validation, and package composition"* (RMS §6).
- A *Definition* is *"A Registry Record specifying meaning"*; its test is *"Governs; never
  instantiates"* (RMS §6.1).
- Registry Records are semantic-definition Records — *"not configuration, not code constants, not
  metadata, not a catalog, not runtime"* (RMS §10).
- Artifact 064 §8: a `MODEL-DEFINITION` is *"the governed definition of one declared Record
  Model"*, whose semantic question is *"what is this Record Model, as the Registry defines it?"*

**Definition (synthesis).** A `MODEL-DEFINITION` is a Registry definition Record carrying the
governed meaning of one declared sovereign Record Model, at the model level: the partition-owned
semantic architecture and the distinct class of question that model answers. It governs that
meaning and never instantiates the model.

## 6. Inherited Contract from Artifact 064

`H: 064` is consumed unchanged.

- **Fourteen Kinds.** `MODEL-DEFINITION` is Kind 1 of RMS §10.1's *"Final Kind taxonomy — CLOSED
  at fourteen"*. It is not renamed, merged into `KIND-DEFINITION` or `SCHEMA-DEFINITION`, or
  replaced; no fifteenth Kind is introduced.
- **FG-V7-07 closed.** The Kind is settled current architecture, not proposed, optional or open
  (SC-066-B).
- **Responsibility.** 064 §8 row 6: *"Registry governs the definition; the model's sovereignty is
  constitutional and neither granted nor held by the Record"*.
- **Admission not reopened.** 064 §8 answers the fourteen admission questions for this Kind. This
  specification does not revisit them.
- **No common family checklist.** 064 §27 hands each row of 066–107 *"exactly the specification or
  schema responsibilities, `Val` and `Done` the Roadmap and governing sources assign each row"*.
  No standard definition object is invented here.

## 7. Model vs MODEL-DEFINITION

> **A Record Model is not its `MODEL-DEFINITION`.**

```
World                       = sovereign Record Model W, constitutionally established (RMS §2)
MODEL-DEFINITION about W    = a Registry definition carrying governed meaning about W

a MODEL-DEFINITION does NOT:   create W · own W · grant W sovereignty · assign partition W ·
                               instantiate W · own any W Record
```

The same holds for E, P, R, V and I. World exists constitutionally whether or not a Registry
definition of World has been considered; the definition describes governed meaning about World and
does not constitute it (Artifact 061 §7 row 7; Artifact 061 example E: *"A MODEL-DEFINITION Record
for World does not mean Registry created World."*).

## 8. Family Rules

| ID | Rule | Basis |
|---|---|---|
| **MD-1** | **One definition, one declared model subject.** A `MODEL-DEFINITION` defines governed meaning about exactly one declared sovereign Record Model. Today that subject is one of W, E, P, R, V, I. How the subject is encoded is 067's. | 064 §8 row 1; RMS §2; synthesis |
| **MD-2** | **The subject is declared first.** The definition causes no declaration. The order is *declared sovereign Record Model → a `MODEL-DEFINITION` may define its governed meaning*, never *`MODEL-DEFINITION` exists → a Record Model is created*. | RMS §2; Artifact 063 §8.2 |
| **MD-3** | **Governs; never instantiates.** The definition is semantic. It is not a model object, a runtime model, a partition, a model factory, a registration service or an instance container, and carries no executable behaviour. | RMS §6.1; RMS §10; Blueprint §9.4 |
| **MD-4** | **No creation or transfer of sovereignty or Record ownership.** A `MODEL-DEFINITION` neither grants sovereignty nor creates or transfers Record ownership. The defined Record Model keeps the semantics and Records it owns by virtue of its own sovereign status. For W, E, P, V and I, Registry owns the `MODEL-DEFINITION` Record and none of those models' domain Records. For R, Registry already owns R-partition Records because it is itself the sovereign R Record Model — the ordinary sovereignty rule, not an exception — and that ownership exists independently of, and is not conferred by, the `MODEL-DEFINITION`. | 064 §8 row 6; I-16; I-105; 061 §7 row 7 |
| **MD-5** | **No common parent.** The six models are sovereign peers. The family establishes no base model, template model or inheritance between models, and no definition is a superclass of another. | RMS §2; I-101 |
| **MD-6** | **Model level is not Kind or schema level.** A model owns a whole partition-level semantic architecture; a Kind is *"A class of Record within one model"*; a schema defines structure. `MODEL-DEFINITION`, `KIND-DEFINITION` and `SCHEMA-DEFINITION` are not collapsed. | RMS §6, §6.1, §10.2; 064 §8 row 13 |
| **MD-7** | **A simulation model is not a Record Model.** `SIMULATION-MODEL-DEFINITION` is a different Registry Kind. A simulation model definition is neither a seventh Record Model nor a `MODEL-DEFINITION`; row 098: *"no Simulation Record Model"*. | RMS §10.1, §10.7; row 098 |
| **MD-8** | **Model-owned semantics stay with the model.** The definition may state the model's distinct question and model-level meaning. It does not supply, override or standardize the model's Kind taxonomy, identity semantics, lifecycle, relationship packaging, temporal architecture, provenance meaning, canonicality meaning, semantic validation or package composition. | RMS §6; RMS §4 |

## 9. Six-Model Definability

**Required synthesis.** A `MODEL-DEFINITION` defines one declared Record Model (MD-1); the declared
Record Models are exactly the six of RMS §2; a declared Record Model is an admissible Registry
reference target (RMS §10.3; Artifact 063 §8.2). Therefore the legal subjects are exactly W, E, P,
R, V and I, and each is definable.

| Code | Model | Its question (RMS §6, verbatim) | Definable by a `MODEL-DEFINITION` | Not done by the definition |
|---|---|---|---|---|
| **W** | World | *What is true of the world?* | yes — governed meaning about declared model W | creates no World, owns no World Record, decides no World Truth |
| **E** | Epistemic | *Who knows, believes, suspects, or has been shown what?* | yes — governed meaning about declared model E | grants no sovereignty; owns no E Record |
| **P** | Production | *What is intended, planned, coordinated, and in production?* | yes — governed meaning about declared model P | grants no sovereignty; owns no P Record |
| **R** | Registry | *What does the system mean, and how are Record semantics defined?* | yes — governed meaning about declared model R | is not a bootstrap mechanism (RMS §10.4); does not constitute Registry or grant it sovereignty. Registry already owns R-partition Records as the sovereign R model, independently of this definition |
| **V** | Visual | *How is World Truth visually specified and represented?* | yes — governed meaning about declared model V | grants no sovereignty; owns no V Record |
| **I** | Issue | *What was published, and how is that publication composed?* | yes — governed meaning about declared model I | grants no sovereignty; owns no I Record |

**Six, and only six.** No other subject is a legal `MODEL-DEFINITION` subject as a sovereign Record
Model; RMS §25: *"NO SEVENTH SOVEREIGN RECORD MODEL IS REQUIRED AT v1.0."* This table proves
definability; it instantiates no Record and is not Registry data.

## 10. Resolution Contract

Row 066 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-1** | A `MODEL-DEFINITION` is a Registry definition Record. Once materialized it carries ordinary Record identity under the universal identity grammar and envelope (RMS §4, §5). |
| **RS-2** | A consumer must be able to resolve a materialized `MODEL-DEFINITION` through the shared resolution mechanism. Reference resolution is universal and mechanical (RMS §4); *"Reference resolution is not Registry work"* (Blueprint §9.4). |
| **RS-3** | Successful resolution does not establish reference legality: *"Resolvable ≠ legal"* (Artifact 063 §11). |
| **RS-4** | Successful resolution grants no model sovereignty, and the resolved definition is not the Record Model (§7). |
| **RS-5** | No resolver, lookup function, storage path, index, model-name lookup or special Model resolver is defined here. Registry definition resolution by id and version is row 115's; generic Record resolution is the shared mechanism's (Artifact 062 §12). |

## 11. Versionability Boundary

Row 066 `Val`: *"versionable"*.

**Source facts.** A Registry definition has *"a governed change path, and a temporal account"*
(Blueprint §13.6e). Row 108 owns the evolution model (*"temporal account without a World History
Record"*); row 109 owns versioning (*"consumers pin a version"*); row 110 owns supersession and
deprecation (*"deprecated ≠ deleted"*).

**Obligation.** A `MODEL-DEFINITION` participates in governed Registry definition evolution and must
be capable of carrying versioned meaning under the model rows 108–110 define. Every version remains
a definition of governed model-level meaning about the same kind of subject (§8).

**Not decided here** (108–110): version field or identifier syntax; integer or semantic numbering;
latest-version semantics; pin representation; supersession or replacement; deprecation state;
compatibility; retention; deletion. Who may change or deprecate a definition is 065's.

## 12. Reference Boundary

Row 066 `Val`: *"references only declared entities (063)"*. Artifact 063 binds this family as a
constraint; it is not added to `H`.

| ID | Rule | Basis |
|---|---|---|
| **RF-1** | **The model subject is a declared Record Model.** W, E, P, R, V and I are declared constitutionally (RMS §2); no declaration ceremony is invented. | Artifact 063 §8.2; RMS §10.3 |
| **RF-2** | **Declared Model ≠ `MODEL-DEFINITION`.** Naming World as a definition's subject is a declaration reference, not an R → R reference to a `MODEL-DEFINITION` Record. | Artifact 063 §8.2 |
| **RF-3** | **No invented concrete references.** RMS §10.3 makes other Registry definitions, declared Kinds, declared schemas and declared semantic contracts admissible categories. That does not oblige any `MODEL-DEFINITION` to reference them, and this family defines no Kind, schema, contract or dependency reference lists. Admissible category ≠ concrete family relation. | Artifact 063 RB-5 |
| **RF-4** | **No domain instance.** No Record of W, E, P, V or I may be a reference target or the semantic authority of a `MODEL-DEFINITION`. | RMS §10.3; Artifact 063 §9 |
| **RF-5** | **No runtime instance.** No running service, worker, session, process or live object is a dependency or authority. | RMS §10.3; Artifact 063 §13 |
| **RF-6** | **Resolvable ≠ legal.** A target that resolves mechanically may still be illegal. | Artifact 063 §11 |
| **RF-7** | **No transfer through reference.** A legal reference transfers no ownership, mutation authority, semantic authority, canonicality or source-of-truth class. | Artifact 063 §12 |

Blueprint §9.4's older blanket prohibition on referencing a kind, a subtype or an instance is not
current law; RMS §10.3 corrects it (SC-066-C).

## 13. Authority, Ownership and Canonicality

**Source fact.** *"Registry governs the definitions. Each Record Model owns its Records."*
(Blueprint §13.6e; I-105). Artifact 061 §7 row 7: Registry governs *"a `MODEL-DEFINITION` Record:
governed meaning about a declared Record Model"*; the model keeps *"its sovereignty, which is
constitutional and is neither granted nor held by a Registry Record"*.

A `MODEL-DEFINITION` creates and transfers no ownership. Defining another model gives Registry no
ownership of that model or of its Records, and no authority over its lifecycle, Kind admission,
canonicality, temporal design, package architecture or semantic validation. When the defined model
is Registry itself, Registry's ownership of R Records comes from Registry sovereignty, not from the
`MODEL-DEFINITION`. Defining World does not make World subordinate to Registry. Registry
semantic authority is authority over definition meaning (RMS §17: *"All authority is
domain-scoped."*).

**Canonical about meaning.** Row 066 carries `Canon: canonical-about-meaning`. A committed
`MODEL-DEFINITION` is the authoritative meaning Records resolve against (Blueprint §13.7c; Artifact
052 §5.4) — governed meaning, not World Truth, and not model sovereignty. A `MODEL-DEFINITION` for
World may state the governed meaning of the declared World model; it decides nothing about what is
true of the world. Canonicality is not universalized across the six models (I-104).

## 14. Envelope and Universal-Semantics Boundary

Once materialized, a `MODEL-DEFINITION` carries the universal envelope unchanged: `partition` ·
`kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4). No family
concept — a model code, a semantic question, a version, a status, a lifecycle, an approver, a
deprecation flag, a schema reference or an authority — becomes a universal field. How family
information is represented is 067's.

None of RMS §4's prohibited universal semantics is introduced: no universal Record base,
Relationship Record, History Record, lifecycle, canonicality, Kind taxonomy, identity composition,
state model or semantic schema. In particular the family does not become a universal parent of the
six models, impose one lifecycle or status vocabulary on them, impose one schema for model-owned
semantics, or create a universal Kind taxonomy (MD-5, MD-8). RMS §6's nine ownership dimensions
describe what a Record Model is; they are not nine universal fields.

## 15. LS-1 and Registry Self-Hosting

Row 066 carries `LS: LS-1`, preserved exactly. Roadmap PART III defines LS-1 as *"every Kind spec ↔
its Registry KIND-DEFINITION. ATOMIC-PAIR."*

- **Lockstep is not a dependency and not a reference.** `LS: LS-1` adds no hard dependency to
  066 and creates no Record reference (Artifact 003 `LS`).
- **The self-hosting resolution stands.** Under AD-LS1-R-BOOTSTRAP (Artifact 003; Roadmap §0.7) the
  Registry's own fourteen Kind ↔ `KIND-DEFINITION` pairs are 064 ↔ 075: row 074 specifies the set,
  row 075 authors the fourteen `KIND-DEFINITION` Records — one of which concerns the Kind
  `MODEL-DEFINITION` — as their canonicalization source, committed only through 152 after
  G-CANON-R (Roadmap §0.8).
- **Nothing replaces it.** This specification creates no `KIND-DEFINITION` Record, does not stand
  in for row 075, and does not treat 067's schema as a `KIND-DEFINITION` Record.

How the LS-1 labels on rows 066 and 067 relate to the 064 ↔ 075 resolution is not stated by any
source; it is recorded, not resolved (SC-066-I).

## 16. Worked Examples

All examples are **schematic**: no ID is minted, and nothing here is Registry data.

**Legal — World.** A `MODEL-DEFINITION` defines governed meaning about declared model W — World. It
may state the source-established question *"What is true of the world?"* It does not create World
or own any World Record.

**Legal — Registry.** A `MODEL-DEFINITION` may define R — Registry, which is itself one of the six
sovereign Record Models. Registry already owns its R Records as that sovereign model; the
definition neither constitutes Registry nor confers that ownership. This is not a bootstrap
mechanism: RMS §10.4 closes bootstrap separately — *"There is no circular self-definition
requirement."* — and no *axiom* definition is implied.

**Illegal — a seventh Record Model.** A proposed `MODEL-DEFINITION` whose subject is *S —
Simulation*, claiming to create a seventh sovereign Record Model, is invalid: the six are closed
(RMS §2), and `SIMULATION-MODEL-DEFINITION` is a different Kind that creates no Record Model (MD-7).

**Illegal — a domain instance as meaning.** A `MODEL-DEFINITION` for World that establishes what
World means by referencing a particular World Character Record (schematically `W-CH-…-Maximus`) is
rejected: the Character is a domain instance (RF-4).

**Boundary — model vs definition.** World is constitutional before any Registry definition of it
is considered. The definition describes World's governed meaning and does not constitute World
(§7).

**Deferred — versions.** A `MODEL-DEFINITION` must be versionable. How its version is represented
or pinned is 108–110's (§11).

**Deferred — schema.** This document fixes the semantic contract. How it is represented
structurally is 067's (§19).

## 17. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | A `MODEL-DEFINITION` creates a Record Model | definitions govern; never instantiate | RMS §6.1; MD-2, MD-3 |
| 2 | Another `MODEL-DEFINITION` creates a seventh sovereign model | the six are closed | RMS §2, §25 |
| 3 | Registry owns a Record Model because it owns that model's Registry definition | model sovereignty exists independently of its Registry definition | 061 §7 row 7; MD-4 |
| 4 | Registry gains ownership of another model's Records because it defines that model | W, E, P, V and I retain their Records; Registry owns R Records because it is independently the sovereign R model, not because it defines itself | §13.6e; I-16; I-105; MD-4 |
| 5 | A Record Model is its `MODEL-DEFINITION` | model ≠ definition | §7 |
| 6 | `MODEL-DEFINITION` is a specialization of `KIND-DEFINITION` | distinct Kinds at distinct levels | RMS §10.1; MD-6 |
| 7 | `MODEL-DEFINITION` is a schema | a schema defines structure | RMS §10.2; MD-6 |
| 8 | `MODEL-DEFINITION` and `SIMULATION-MODEL-DEFINITION` define the same kind of model | a simulation model is not a Record Model | row 098; MD-7 |
| 9 | A resolved definition is a legal reference | resolvable ≠ legal | Artifact 063 §11; RS-3 |
| 10 | An admissible target category must be referenced by every `MODEL-DEFINITION` | category ≠ concrete relation | Artifact 063 RB-5; RF-3 |
| 11 | Naming a declared Record Model references its `MODEL-DEFINITION` | declaration reference ≠ R → R reference | Artifact 063 §8.2; RF-2 |
| 12 | A domain instance may define model meaning because it is representative | instances are forbidden | RMS §10.3; RF-4 |
| 13 | The six models inherit semantics from one universal model definition | no superclass | RMS §2; MD-5 |
| 14 | World is a template for E, P, R, V and I | *"World is not a template."* | RMS §2 |
| 15 | RMS §6's nine ownership dimensions are nine universal fields | they are model-owned semantics | RMS §6; §14 |
| 16 | *Versionable* lets 066 invent version fields or numbering | mechanics are 108–110's | §11 |
| 17 | `LS: LS-1` is a semantic reference | lockstep ≠ reference | Artifact 003; §15 |
| 18 | `LS: LS-1` lets 066 create the Registry's concrete `KIND-DEFINITION` partners | they are row 075's | AD-LS1-R-BOOTSTRAP; §15 |
| 19 | This document is a `MODEL-DEFINITION` Record because its metadata says `canonical-about-meaning` | it is a specification | SC-066-H |
| 20 | `CD: yes` licenses direct writes into `canon/**` | the flag *"licenses nothing"* | Artifact 003 (`CD`) |
| 21 | Registry's canonicality about meaning is World Truth | meaning, never the world | §13.7c; 052 §5.4 |
| 22 | FG-V7-07 is still OPEN | RMS §27 closes it | SC-066-B |
| 23 | Blueprint §9.4's *"Classification: capability"* is current architecture | stale; RMS §10 COLLISION-1 | SC-066-A |
| 24 | Blueprint §9.4's blanket reference prohibition overrides RMS §10.3 | RMS §10.3 corrects it | SC-066-C |
| 25 | Because Registry content including *"model definitions"* is extensible, the model roster is extensible | content ≠ constitutional roster | SC-066-D |
| 26 | Registry owns no R Records because R is the subject of a `MODEL-DEFINITION` | R owns R Records by its own sovereignty | MD-4; I-16 |
| 27 | Registry owns its R Records because a `MODEL-DEFINITION` grants that ownership | a definition grants no ownership | MD-4 |
| 28 | Artifact 066's `Canon` and `CD` fields are metadata of the `MODEL-DEFINITION` family rather than of Artifact 066 | artifact metadata applies to the artifact; no alternative reading is invented | Artifact 003; SC-066-H |
| 29 | Artifact 459 owns every possible extension | it owns the categories its row names | row 459 |
| 30 | Artifact 003's general *docs specification → `Canon: n/a`* convention lets Artifact 066 overwrite its Roadmap value | the explicit row 066 value is preserved; the inconsistency is recorded | SC-066-H |

## 18. Source Conditions and Gaps

### SC-066-A — stale Registry classification — CLOSED AT SOURCE

Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* RMS §10, COLLISION-1:
the line is *"stale and requires a Blueprint wording fix"*. **Treatment:** Registry is a sovereign
Record Model; the stale line is not current law.

### SC-066-B — FG-V7-07 OPEN in the Blueprint, CLOSED in the RMS

Blueprint §13.6e: *"OPEN — Registry's own taxonomy."* — whether Registry needs a Record Model
definition Kind *"is not established by any source"* (FG-V7-07). RMS §10.1 and §27 close it:
*"MODEL-DEFINITION is a Registry Kind"*. **Treatment:** the Kind exists; this artifact specifies its
family contract and does not reopen FG-V7-07.

### SC-066-C — older reference prohibition vs RMS §10.3 — CLOSED AT SOURCE

Blueprint §9.4 and I-75 forbid referencing a kind, a subtype or an instance. RMS §10.3: *"v0.1
stated the boundary too bluntly"*. **Treatment:** RMS §10.3 and Artifact 063 govern (§12); domain
instances stay forbidden; declared categories are admissible; the two rules are not averaged.

### SC-066-D — extensible model definitions, closed model roster

Blueprint §9.4 lists *"model definitions"* among Registry content that *"extends by ordinary
Registry change"*. RMS §2 fixes exactly six sovereign Record Models. **Treatment:** what may evolve
is the content of Registry definitions about the six, not the constitutional roster. No definition
creates a seventh model.

### SC-066-E — versionability required before its mechanics exist

Row 066 requires *"versionable"*; rows 108–110 own the mechanism. **Treatment:** the obligation is
stated (§11) and no representation or algorithm is defined. This is a downstream boundary, not
permission to pre-build 108–110.

### SC-066-F — RR-16 text unavailable

`Req: RR-16` is carried exactly. Its text is not in the source set (GAP-C). No compliance with
unread requirement text is claimed; this artifact is validated against row 066's `Val` and `Done`,
its cited sources and the frozen contracts.

### SC-066-G — semantic-layer placement — SOURCE GAP

Artifact 062 §6 records that Blueprint §9.4's layer rows do not place `MODEL-DEFINITION`, and that
its placement is *"not established by current sources"*. **Treatment:** no layer is assigned here.

### SC-066-H — Roadmap `Canon` metadata vs Artifact 003's docs-specification convention

| | |
|---|---|
| **Source fact — Roadmap row 066** | Row 066 explicitly assigns this artifact `T: doc` · `Canon: canonical-about-meaning` · `CD: yes`. These values are preserved exactly. |
| **Source fact — Artifact 003** | `Canon` *"records a per-artifact status, nothing more"*, and, as a general convention, *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`."* `CD` marks whether an artifact *"creates, carries or directly impacts canonical data"* and *"licenses nothing"*. |
| **Source fact — directory** | `docs/registry/PURPOSE.md` holds family specifications and excludes Registry Records: *"those are minted into `canon/registry/`"*. |
| **Convention / decomposition inconsistency** | Artifact 066 is a documentation specification under `docs/registry/`, yet row 066 assigns it `Canon: canonical-about-meaning` rather than Artifact 003's general docs-specification value, `Canon: n/a`. The artifact's explicit Roadmap metadata and Artifact 003's general convention do not align. |
| **Source gap** | No current source explains why row 066 carries the non-default `Canon` value. No rationale is invented. |
| **Treatment** | Row 066's explicit manifest metadata governs Artifact 066's identity, and is preserved exactly; Artifact 003 remains the general convention and is not changed. This artifact has no authority to reconcile the two: the inconsistency is **recorded, not resolved**. Artifact 066 remains `T: doc` and a specification, not a `MODEL-DEFINITION` Registry Record; it creates no concrete Registry Record and performs no canonical write; `CD: yes` grants no write authority. Route: ROADMAP / CONVENTION ISSUE, non-blocking for this artifact, whose own metadata is explicit and whose `Val` and `Done` remain evaluable. |

### SC-066-I — LS-1 on rows 066–067 and the 064 ↔ 075 self-hosting resolution

Rows 066 and 067 carry `LS: LS-1`, and row 067's `Why` reads *"LS-1 partner"*. AD-LS1-R-BOOTSTRAP
assigns the Registry's own fourteen Kind ↔ `KIND-DEFINITION` pairs to 064 ↔ 075. No source states
how the 066 and 067 labels relate to that resolution. **Treatment:** the label is preserved; no
competing pair is invented; 066 and 067 are not claimed to replace row 075; 067's schema is not a
`KIND-DEFINITION` Record. Route: ROADMAP ISSUE, non-blocking for this artifact's `Val` and `Done`.

## 19. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-066-01** | The header reproduces row 066's metadata exactly. | row 066 |
| **C-066-02** | `MODEL-DEFINITION` is stated to be an existing Registry Kind, not proposed or open. | RMS §10.1, §27; §6 |
| **C-066-03** | The family defines governed meaning about exactly one declared Record Model. | MD-1 |
| **C-066-04** | All six, and only the six, constitutionally established Record Models — W, E, P, R, V, I — are shown definable. | §9 |
| **C-066-05** | The specification creates, admits, abolishes, reassigns or grants sovereignty to no Record Model. | MD-2 to MD-4 |
| **C-066-06** | No seventh sovereign Record Model is introduced. | RMS §2; §9 |
| **C-066-07** | A Record Model is stated to be distinct from its `MODEL-DEFINITION`. | §7 |
| **C-066-08** | `MODEL-DEFINITION` authority grants or transfers no Record ownership. Every model retains ownership derived from its own sovereignty; in the R case, Registry's ownership of R Records is stated to be independent of its `MODEL-DEFINITION`. | §9; §13; MD-4 |
| **C-066-09** | The six RMS §6 questions are reproduced verbatim, and no model-owned semantic is given a universal implementation. | §9; MD-8 |
| **C-066-10** | `MODEL-DEFINITION`, `KIND-DEFINITION`, `SCHEMA-DEFINITION` and `SIMULATION-MODEL-DEFINITION` are not collapsed. | MD-6, MD-7; §20 |
| **C-066-11** | The resolution obligation is stated without resolver mechanics. | §10 |
| **C-066-12** | Versionability is stated without version numbering, pinning, supersession or deprecation mechanics. | §11 |
| **C-066-13** | Reference targets obey Artifact 063's declared-category boundary. | §12 |
| **C-066-14** | No W, E, P, V or I domain instance is permitted as a reference target or semantic authority. | RF-4 |
| **C-066-15** | No runtime instance is used as a semantic dependency or authority. | RF-5 |
| **C-066-16** | Naming a declared Record Model is not treated as referencing its `MODEL-DEFINITION`. | RF-2 |
| **C-066-17** | Admissible target categories are not treated as mandatory concrete references. | RF-3 |
| **C-066-18** | The seven-field universal envelope is unchanged. | §14; RMS §4 |
| **C-066-19** | No universal lifecycle, canonicality, Kind taxonomy, identity composition, state model, semantic schema, Relationship Record or History Record is introduced. | §14; RMS §4 |
| **C-066-20** | No semantic layer is assigned to `MODEL-DEFINITION`. | SC-066-G |
| **C-066-21** | No schema field or serialization format belonging to 067 is designed. | §3; §20 |
| **C-066-22** | No evolution, version, supersession or deprecation mechanics belonging to 108–110 are designed. | §11 |
| **C-066-23** | No reference validator, resolver or kernel belonging to 112, 114 or 115 is designed. | §10 |
| **C-066-24** | `LS: LS-1` is preserved and not treated as a reference or a hard dependency. | §15 |
| **C-066-25** | The Registry self-hosting resolution through 064, 074 and 075 is not replaced or bypassed. | §15; SC-066-I |
| **C-066-26** | `Canon: canonical-about-meaning` and `CD: yes` remain exact per-artifact Roadmap metadata; neither is reinterpreted as metadata of the `MODEL-DEFINITION` family, neither makes this document a Registry Record, and neither authorizes a canonical write. The inconsistency between row 066's `Canon` value and Artifact 003's general docs-specification convention is recorded and not silently resolved. | SC-066-H; Artifact 003 |
| **C-066-27** | RR-16's text is not invented. | SC-066-F |
| **C-066-28** | This artifact's changes are confined to `docs/registry/model_definition.md`. | row 066 |

## 20. Concept Separation and Downstream Handoff

| Concept | What it is | Not to be confused with |
|---|---|---|
| Record Model | a sovereign, partition-owned semantic architecture (RMS §6) | its Registry definition |
| `MODEL-DEFINITION` | the Registry Kind whose Records carry governed meaning about one declared Record Model | the model's creation |
| `KIND-DEFINITION` | the definition of one Kind within one model | the definition of a whole model |
| `SCHEMA-DEFINITION` | the definition of a schema's structure | model sovereignty or model meaning |
| `SIMULATION-MODEL-DEFINITION` | the definition of a simulation model's behaviour | a Record Model or its definition |
| Artifact 066 (this document) | the authoritative family specification | a concrete Registry Record |
| Artifact 067 | the schema encoding this contract | a resolver, runtime or model factory |

**To 067** (`H: 066`; `Val`: *"definition resolves; versionable; references only declared entities
(063)"*; `Done`: *"schema matches spec"*). 067 may derive from this document, without redesign:
the semantic object represented (§5); that its subject is one declared Record Model (MD-1); that
the legal subjects are the six sovereign models (§9); that defining a model creates none and
sovereignty stays constitutional (MD-2 to MD-4, §13); the resolution obligation (§10); the
versionability obligation (§11); the reference rules RF-1 to RF-7; and the separations above. This
document prescribes none of 067's field names, serialization, cardinality syntax, schema language
or validator. Row 067's `→ 114` is 067's own metadata; Roadmap §0.8 replaced a backward
`→ 040`.

| Other downstream owner | Keeps |
|---|---|
| 065 | who may propose, approve and deprecate a definition |
| 068–069; 074–075 | `KIND-DEFINITION`; the Registry's own Kind-Definition set |
| 108, 109, 110 | evolution; versioning; supersession and deprecation |
| 111 | concrete definition-dependency rules |
| 112, 114, 115 | reference validator; kernel; Registry definition resolution |
| 459 | how a new Kind, field, definition, simulation model, visual subtype, or publication structure is added — *"each through its own ceremony, never through a generic abstraction"* |

## 21. Roadmap Completion Trace

| Row 066 | Status | Where it is met |
|---|---|---|
| `Val`: *"definition resolves"* | **SATISFIED** — resolution obligation stated; resolvable ≠ legal; mechanics left to the shared mechanism and 115 | §10 (RS-1 to RS-5) |
| `Val`: *"versionable"* | **SATISFIED** — obligation stated; mechanics left to 108–110 | §11; SC-066-E |
| `Val`: *"references only declared entities (063)"* | **SATISFIED** — Artifact 063's boundary applied, with domain-instance and runtime rejection | §12 (RF-1 to RF-7) |
| `Done`: *"six models definable"* | **SATISFIED** — W, E, P, R, V and I each covered, and only they | §9 |
| `Why`: *"closes FG-V7-07"* | **SATISFIED** — the source-closed Kind's family meaning is specified; FG-V7-07 not reopened | §1, §6; SC-066-B |
| `H: 064` | **SATISFIED** — taxonomy and responsibility consumed unchanged | §6 |
| `LS: LS-1` | **PRESERVED** — label kept; the 064 ↔ 075 resolution untouched; no partner invented; relation recorded | §15; SC-066-I |
| `→ 067` | **SATISFIED** — semantic contract handed off; no schema built | §20 |

No Record Model created. No Registry data created. No schema, field, resolver, version mechanism
or `KIND-DEFINITION` created.

---

*Artifact 066 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning. This document specifies the `MODEL-DEFINITION` family from Record
Model System §2, §6, §10.1, §10.3 and §27, Master Blueprint §9.4 and §13.6e, and Roadmap row 066,
with Artifact 064 as its input. It
is not a Registry Record, holds no canonical data, defines no schema, field, validator or algorithm,
and implements nothing. Where it differs from the Master Blueprint, the Record Model System, or the
OS File Build Roadmap, those governing sources are correct and this document is wrong.*
