# COOLBOY12 — RELATIONSHIP-TYPE-DEFINITION Specification

**Artifact 079** · RELATIONSHIP-TYPE-DEFINITION spec · `docs/registry/relationship_type.md` ·
Own: R · RM: R · T: doc · R: ARCH · SoT: AUTHORITATIVE · Auth: defining ·
Canon: canonical-about-meaning · CD: yes · Ph/St: P3/3b · Req: RR-16 · BP: §9.4 · RMS: §10.1 ·
H: 064 · S: — · LS: LS-1 · G: — · → 080 · Val: definition resolves; versionable; references only
declared entities (063) · Done: participant roles **and owning role** declared · Why: LS-3 partner ·
Risk: high · ∥: yes

> **Effective status of this file.** The line above transcribes Roadmap row 079 field by field, as
> Artifact 003 requires (§2). Its `Canon: canonical-about-meaning` and `CD: yes` are copied manifest
> values; they do not declare this Markdown file to be a materialized Registry Record. This file is
> an AUTHORITATIVE architecture specification under `docs/**` — Roadmap PART VII gives `docs/**`
> specs *"Yes architecture"* authority and no right to write canon. It holds no canonical data and
> licenses no canonical write and no write path (Roadmap §0.8; Artifact 003: `CD`
> *"licenses nothing"*). The difference between row 079's `Canon` value and Artifact 003's
> convention for a `docs/**` specification is tracked for its owner at SC-079-J; §2, SC-079-J and
> the footer repeat this status and do not change it.

## 1. Purpose

This specification answers one question — **how does the Registry define a relationship type,
declare its participant roles and designate the one role that owns the edge, without becoming the
owner of any actual relationship, and without imposing World's Relationship Record on any other
Record Model?**

COOLBOY12 keeps apart six things that are easy to merge. Shown for *Character A MEMBER_OF
Organization B* (Blueprint §13.9):

```
RELATIONSHIP-TYPE-DEFINITION, the Kind   Kind 6 of RMS §10.1's fourteen; admission rationale in
                                         Artifact 064 §13
a RELATIONSHIP-TYPE-DEFINITION Record    an R-partition Registry Record: the governed definition of
                                         one relationship type — here MEMBER_OF
the relationship type it defines         its meaning; its participant roles — the member, and the
                                         organization the member belongs to; its owning role, the
                                         member
an actual relationship of that type      Character A MEMBER_OF Organization B — owned by the model
                                         whose mechanism holds it, World here
World's Relationship Record              Character A's, because A occupies the owning role
                                         (Blueprint §13.9; I-73)
the back-reference Organization B sees   a Derived projection, never authoritative (§13.9)
```

The rule this document exists to state:

> **A `RELATIONSHIP-TYPE-DEFINITION` declares its participant roles and designates exactly one of
> them as the owning role. Wherever Relationship Records are used, the endpoint that occupies that
> role holds the edge authoritatively, and the other endpoint's view is Derived. The Registry owns
> the rule; the Record Model owns the edge.**

`RELATIONSHIP-TYPE-DEFINITION` already exists. It is Kind 6 of RMS §10.1's *"Final Kind taxonomy —
CLOSED at fourteen"*, and Artifact 064 §13 records its admission rationale. This document specifies
the family; it admits nothing. Its sources are direct: the Registry holds *"relationship-type
definitions with their participant roles and ownership rule"* (Blueprint §9.4); it owns *"The
definition of a relationship type and its owning role"* while each Record Model owns *"Whether it
uses Relationship Records at all"* (Blueprint §13.6e); and *"The relationship type definition in
the Registry declares which participant role owns the edge."* (Blueprint §13.9).

## 2. Status and Roadmap Identity

Row 079 of the repaired Roadmap, reproduced field by field:

| Field | Exact value |
|---|---|
| ID | 079 |
| Name | RELATIONSHIP-TYPE-DEFINITION spec |
| Path | `docs/registry/relationship_type.md` |
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
| → | 080 |
| Val | definition resolves; versionable; references only declared entities (063) |
| Done | participant roles **and owning role** declared |
| Why | LS-3 partner |
| Risk | high |
| ∥ | yes |

This document is the AUTHORITATIVE specification of the `RELATIONSHIP-TYPE-DEFINITION` Registry
definition family, under the Record System. It is authoritative about that family and about no
World Truth and no model's actual edges. Its effective status is the one stated under the header;
the bullets below spell it out. It is:

- **not a Record.** It carries no envelope, no `object_id`, no provenance value and no
  `registry_ref`. No `RELATIONSHIP-TYPE-DEFINITION` Record is created by it.
- **not the structural schema of the family.** How a `RELATIONSHIP-TYPE-DEFINITION` Record is
  structurally represented is Artifact 080's (`docs/registry/relationship_type.schema`, `H: 079`).
- **not a set of relationship types.** It defines no concrete type — no World, Epistemic,
  Production, Visual or Issue type; those sets are rows 198, 277, 338, 356 and 366.
- **not a Relationship Record specification.** World's is rows 197–199.
- **not an implementation.** It defines no validator, resolver, graph store, projection, API or
  service, and executes nothing.
- **not a canonicalization source.** Roadmap §0.8 names the canonicalization sources — rows 075,
  085, 105, 106, 107 — and row 079 is not one of them.
- **not canonical data.** It lies outside `canon/**`. Registry Records are committed only through
  the Mutation Coordinator (row 152), after G-CANON-R (Roadmap §0.8).

`Req: RR-16` is carried exactly; its text is not available (SC-079-K).

**Evidence classes.** Statements that matter are labelled by where they come from:

| Class | Meaning |
|---|---|
| **SOURCE FACT** | stated by the Blueprint, the RMS, the Roadmap or a frozen upstream artifact |
| **REQUIRED SYNTHESIS** | a conclusion that several source facts force together; not a quotation |
| **079 FAMILY INTERPRETATION** | a bounded statement of what this family means, adding no semantics the sources lack |
| **SOURCE GAP** | not established by current sources, and not filled here |

**Evidence levels.** An evidence class says where a statement comes from. How far an obligation
has been carried is a separate question, with four levels that are never merged:

| Level | Meaning | For this family |
|---|---|---|
| **SPECIFIED** | this document states the obligation | §5–§16 |
| **SOURCE-CHECKED** | its quotations, citations and row metadata were compared with the repository copies of the sources in §4 when this revision was authored | mechanically: the header and §2 against row 079, and every `*"…"*` quotation against its source; by authoring review only, pending human review: the other CROSS-SOURCE conditions of §20 |
| **MECHANISM** | a structural contract or an implementation row supplies it | **pending** — 080, 108–115 and the model rows do not yet exist |
| **DEMONSTRATED** | an executable test or a run shows the behaviour | **pending** — 112, 116, 123, 124 |

A promise that a later row will supply a mechanism is not evidence that it exists. §22 reports each
item of row 079 at the level it has reached.

**Open decisions.** Two questions this family depends on are answered by no current source:
OD-079-1, what a relationship type's cardinality bounds, and OD-079-2, what the owning role governs
outside Relationship Records (§19.1). Each names its owner, the work it blocks and the condition
that closes it. An open decision is not a Roadmap `G` gate — row 079 carries `G: —`, and Artifact
003 says *"Do not invent gates."* — and nothing here reports either as resolved.

Where this document differs from the Master Blueprint, the Record Model System or the OS File Build
Roadmap, those sources are correct and this document is wrong.

## 3. Scope and Non-Goals

**Artifact 079 owns** the family-level semantic contract of a `RELATIONSHIP-TYPE-DEFINITION`:

- what a `RELATIONSHIP-TYPE-DEFINITION` Record is, and why it is a distinct Kind (§5);
- the separation of a relationship type from its instances, storage, projection and history (§6);
- what a participant role is, and the obligation to declare the roles (§7);
- the owning role: its mandatory, unambiguous designation as a condition of definition validity,
  and its application where Relationship Records are used (§8);
- the type semantics Blueprint §13.3 attaches — direction, cardinality, legality — without
  inventing their representation (§9);
- the boundary with the reification criterion, with each model's relationship architecture, and
  with fields, references, composition and dependencies (§10–§12);
- the consequences for World's Relationship Record, stated and not implemented (§13);
- the identity, resolution, versionability and reference obligations of row 079's `Val` (§14–§15);
- the family rules (§16), examples (§17), prohibited inferences (§18), open decisions and source
  conditions (§19), conformance conditions (§20) and the handoff to 080 (§21).

**Artifact 079 does not own, and does not pre-build:**

| Not decided here | Owner |
|---|---|
| the Registry Kind taxonomy and the Kind's admission | 064 (`H`); 057; new Kinds 459 |
| the structural representation of a `RELATIONSHIP-TYPE-DEFINITION` Record | 080 |
| the reification criterion's application; the Relationship Record's World scope | 055 (RMS §15); each model's relationship architecture |
| packaging; the temporal obligation; cross-model dependency | 056; 054; 058 |
| World's Relationship Record specification, type set and schema | 197; 198; 199 |
| the back-reference and graph projection | 224 |
| Epistemic, Production, Visual and Issue relationship architectures and type sets | 276, 277; 338; 356; 366 |
| definition evolution; versioning and pinning; supersession and deprecation | 108; 109; 110 |
| who may propose, approve or deprecate a definition | 065 |
| Registry dependency direction, asymmetry and cycles | 111 |
| the reference validator; the validation suite | 112; 116 |
| create/resolve/version operations; consumer resolution by id+version | 114; 115 |
| identity binding and Registry kind codes | 117 |
| lockstep tests; P3 conformance | 123; 124 |
| the canonical gates; the sole canonical writer | 145; 152 |

**Non-goals.** No concrete relationship type, participant-role code or grammar, role list
serialization, owning-role field, direction token, cardinality value or notation, eligibility
matrix, ambiguity classifier, reference carrier, version mechanism, dependency edge, new Kind,
validator or Relationship Record is created.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where stated
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done; §0.7 and §0.8 author rulings
        ↓
Artifact 064 (H)              the Kind and its admission answers, consumed unchanged
        ↓
Artifact 079                  the RELATIONSHIP-TYPE-DEFINITION family
```

| Source | What it gives this specification | Role |
|---|---|---|
| Roadmap row 079 | identity, `Val`, `Done`, `H: 064`, `LS: LS-1`, `Why: LS-3 partner`, `→ 080` | build authority |
| **Artifact 064** (`docs/models/registry/kinds.md`) §5, §6, §7, §13, §23, §27 | Kind 6, its fourteen admission answers, F-1 to F-7, the downstream family boundary | **the only hard dependency** |
| RMS §4; §5; §6.1; §7; §10; §10.1; §10.3; §15 | the envelope and the nine prohibitions; identity; *"Governs; never instantiates"*; World's package; Registry sovereign; fourteen Kinds; the reference boundary; the relationship architecture | constitutional |
| Blueprint §9.4; §12.11; §13.2; §13.3; §13.5; §13.6d; §13.6e; §13.7a; §13.9; I-73, I-74, I-88, I-90, I-102 | the Registry layer; Derived discipline; definition dependencies; relationship semantics; current-only; packaging; definition vs ownership; no universal Relationship Record; ownership by role | constitutional |
| Roadmap PART III (LS-1, LS-3); §0.7; §0.8; rows 197–199, 224, 276, 277, 338, 356, 366, 108–117, 123, 124, 152 | lockstep systems; self-hosting; authoring vs canonical materialization; downstream owners | build authority |
| Artifact 055 (`docs/constitution/relationship_boundary.md`) | the reification criterion, type vs instance, the three ownership questions, World scope | constraint, not `H` |
| Artifacts 060, 061, 062, 063 | Registry model; authority table (§7 row 3); layers (L1 1b); the reference boundary | constraint, not `H` |
| Artifacts 039, 044, 054, 056, 057, 058 | Record System; categories; temporal obligation; packaging; admission; cross-model dependency | constraint, not `H` |
| Artifacts 003, 033, 052 | conventions; the envelope; Registry canonicality | context, not `H` |
| Artifact 077 (`docs/registry/schema_definition.schema`) | `occurrence.cardinality`, a field-occurrence cardinality | contrast only (§9.3), not `H` |
| Revolving Resolution Note | GAP-C; CONFLICT-F (AD-REG-AUTHORING-SPLIT) | a record of build resolutions; cited as record, never as authority |

**Precedence.** Blueprint and RMS govern; where earlier Blueprint wording and a later explicit RMS
correction differ, the correction governs (SC-079-A, SC-079-B, SC-079-R). The Roadmap governs
decomposition and order. Artifact 064 is consumed unchanged. Artifact 055 is the most important
supporting contract, and it is not a hard dependency of row 079; reading it, or any supporting
artifact, does not promote it into `H`.

Citations are to the repository copies in `docs/sources/`: the Blueprint is
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md`, the RMS `COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`, the
Roadmap `COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`. The ownership paragraph cited as §13.9
follows the §13.9a heading in the Blueprint file; it is cited as §13.9, as the Blueprint and
Artifact 055 §7 cite it.

## 5. RELATIONSHIP-TYPE-DEFINITION Identity

### 5.1 Inherited from Artifact 064

Artifact 064 is consumed unchanged. Its §13 is the Kind-level boundary this family stays inside.

| 064 §13 | Inherited fact | Basis |
|---|---|---|
| responsibility | *"What a relationship type is and which role owns it"*; *"Relationship definitions; never runtime relationship ownership"* | §13.6e; RMS §15 |
| Q1 | *"the governed definition of a relationship type, with its participant roles and owning role"* | §13.6e; row 079 |
| Q2 | *"what is this relationship type, and which role owns it?"* | §13.6e |
| Q3 | each type is shared meaning that models resolve against, needing identity and provenance (F-1) | F-1; LS-3 |
| Q4 | persistent state is *"the type's meaning, participant roles and owning role"* | row 079 |
| Q5 | Registry-owned definition evolution (F-4); versioning and supersession are 108–110's | F-4 |
| Q6 | *"definition authority only; the model decides whether it uses Relationship Records and owns the edges its Records hold"* | F-3; 061 §7 row 3; RMS §15 |
| Q7 | what references it is *"not established"*; LS-3 is lockstep, not a reference | LS-3; RMS §15 |
| Q8–Q12 | not a field, a state, a relationship instance, a subtype or a projection | F-1, F-2, F-5–F-7 |
| Q13 | reduction targets `FIELD-DEFINITION` and `SCHEMA-DEFINITION`: they *"describe one Record's own meaning and structure"*; the relational category would be lost | §13.6e; LS-3 |
| Q14 | without the Kind, *"LS-3 has no Registry partner; owning roles go undeclared"* | LS-3; row 079 |

The name is RMS §10.1's. Blueprint §13.6's `RELATIONSHIP-TYPE-DEF` is a source alias, not a further
Kind (064 §5). No Registry kind code is minted here; identity binding is row 117's.

The table's quotations were compared with Artifact 064 as it stands in the repository at this
revision. That establishes that 064 exists at its Roadmap path and says what is quoted. It does not
establish 064's review or approval status, which is a human record and not this document's (§22).

### 5.2 What a RELATIONSHIP-TYPE-DEFINITION is

**SOURCE FACT.** A Registry definition is *"A Registry Record specifying meaning"* that *"Governs;
never instantiates"* (RMS §6.1). *"Registry definitions are Records"* (Blueprint §13.6e). Its
category is *"Relational definition"*: *"What a relationship type is and which role owns it"*
(§13.6e).

**Definition.** A `RELATIONSHIP-TYPE-DEFINITION` is an R-partition Registry Record that governs the
definition of one relationship type: what relationships of that type mean, the participant roles
they have, and which of those roles owns the edge. It is authoritative about that meaning. It
holds no relationship, and executes nothing.

| Level | What it is | Owner |
|---|---|---|
| the Kind `RELATIONSHIP-TYPE-DEFINITION` | one of RMS §10.1's fourteen Registry Kinds | Registry, by its Kind architecture (064) |
| a `RELATIONSHIP-TYPE-DEFINITION` Record | one governed definition of one relationship type, with its own identity | Registry |
| the relationship type defined | meaning, participant roles, owning role, and the type semantics of §9 | defined by the Record; not a separate owner |
| an actual relationship of that type | one connection between actual Records | the Record Model whose mechanism holds it |
| the mechanism that holds it | World's Relationship Record; another model's own mechanism | that Record Model (§13.6e; RMS §15) |
| a non-owning view of it | a back-reference or graph assembled from owned edges | Derived — nobody's authority (§13.9) |

**What a `RELATIONSHIP-TYPE-DEFINITION` is not.** Not a relationship instance; not a collection of
edges; not a Relationship Record, of World or any model; not a History Record; not a graph object;
not a field, a reference or a dependency; not a `FIELD-DEFINITION` or a `SCHEMA-DEFINITION`; not a
validator; not a constant, configuration entry or runtime table — Registry Records are *"not
configuration, not code constants, not metadata, not a catalog, not runtime"* (RMS §10).

### 5.3 What every RELATIONSHIP-TYPE-DEFINITION answers

**SOURCE FACT + REQUIRED SYNTHESIS** from row 079's `Done`, 064 §13 Q4 and RMS §6.1:

1. **the type's meaning** — what a relationship of this type says (RMS §6.1; 064 Q4);
2. **its participant roles** — declared, not inferred (§7; row 079 `Done`);
3. **its owning role** — exactly one of those roles (§8; row 079 `Done`; §13.9).

These three are mandatory semantic obligations of every Record of the family. They are conditions
of **definition validity**: a definition meets them or fails them by its own content, whichever
model uses the type. What a declared owning role does to actual connections is **application**, a
separate question (§8.5). Blueprint §13.3 also attaches direction, cardinality and legality
constraints to the type of a relationship; §9 states how far that reaches. **Obligation is not a
field inventory.** How each obligation is carried —
which elements, names, shapes or notations — is Artifact 080's, within this specification.

## 6. Relationship Type versus Relationship Instance

**SOURCE FACT.** Blueprint §13.3 describes a relationship as *"a typed, directional,
temporally-valid, provenanced connection with its own stable identity and its own definition in the
Registry"*. Some of those properties belong to the type, some to each instance. Artifact 055 §6
keeps the two apart.

| Concern | Belongs to | Owner | Source |
|---|---|---|---|
| definition meaning | the type | Registry (`RELATIONSHIP-TYPE-DEFINITION`) | §13.6e; RMS §6.1 |
| participant-role declaration | the type | Registry | §13.3; §9.4; row 079 |
| owning-role declaration | the type | Registry | §13.9; §13.6e; row 079 |
| permitted participant categories — *"which kinds may stand at each end"* | the type | Registry, naming declared Kinds only (§15) | §13.3; RMS §10.3 |
| actual participant instances | each relationship | the Records' own Record Models | I-105; §13.6e |
| actual edge identity — *"its own stable identity"* | each relationship | the model whose mechanism holds it | §13.3; §13.9 |
| actual authoritative storage | each relationship | the owning endpoint's Relationship Record, in World; another model's mechanism elsewhere | I-73; RMS §15 |
| actual temporal validity — *"from"* and *"until"*, *"in world-time"* | each relationship | World, for World; no other model is given World Time | §13.3; Artifact 055 §12 |
| actual history | each relationship's owning object | the owning object's temporal mechanism — World's History Record | I-74; §13.5; Artifact 054 |
| actual back-reference projection | each relationship | Derived; built downstream (row 224) | §13.9; §12.11 |
| actual provenance of an edge | each relationship | the model that holds it | §13.3 |
| runtime validation | checks against definitions | shared validation and model-owned semantic validation, not this family | RMS §10.6, §20; 061 §7 row 4 |

**Three ownership questions, never collapsed** (Artifact 055 §6):

| Question | Answer | Source |
|---|---|---|
| **definition authority** — who defines what this relationship type means, and which role owns it? | the Registry | §13.6e; §9.4 |
| **Record Model ownership** — which model owns the mechanism that holds the edge, and the edge? | the relevant Record Model — World for the Relationship Record | §13.6e; §13.6d; RMS §15 |
| **endpoint ownership** — which endpoint holds this edge authoritatively? | where Relationship Records are used, the one occupying the type's owning role | I-73; §13.9 |

No single phrase such as *relationship owner* is used here for all three.

## 7. Participant Roles

**SOURCE FACT.** The type carries *"its participant roles"* (Blueprint §13.3); the Registry holds
*"relationship-type definitions with their participant roles"* (§9.4); row 079's `Done` requires
them to be *"declared"*.

**079 FAMILY INTERPRETATION — what a participant role is.** A participant role is a position that a
participant occupies in every relationship of the type. Its meaning is part of the type's meaning:
in `MEMBER_OF`, one role is the member and the other is the organization the member belongs to. A
participant *occupies* a role in an actual relationship; the role is not the participant.

**Obligations.**

- **Declared.** Every `RELATIONSHIP-TYPE-DEFINITION` declares its participant roles. They are not
  inferred from a relationship's name, an example, a Kind or an instance.
- **Distinguishable.** REQUIRED SYNTHESIS: the owning role must designate exactly one role (§8), so
  each declared role must be distinguishable from the others within the type. How roles are named
  or identified is 080's.
- **Held by the definition.** A role's meaning is stated in the definition, never taken from an
  actual participant (RMS §10.3; §15).

**What a participant role is not.** Not a Record, a Kind, a subtype or a field; not an actual
participant or its identifier; not a Registry Kind of its own; and not a Record with identity of its
own. A role is part of one type's definition.

**Arity.** For World, Blueprint §13.9 states *"An edge joins two objects."*, and §13.3 places the
legality constraints at *"each end"*. REQUIRED SYNTHESIS: a World relationship type has two
participant positions, one at each end. For the other models' relationship types, current sources
state no count (SC-079-E). This specification neither rejects a non-binary type as impossible nor
admits arbitrary arity, and fixes no maximum.

**No universal role grammar.** Roles are named by what the type means — the member, the located
thing, the descendant, the causing event — not by a universal *source*/*target* pair. No global role
code, role-identity grammar, role Record, role-list serialization or role ordering is defined.

**Names used here.** *"the member"*, *"the located thing"*, *"the descendant"* and *"the causing
event"* are Blueprint §13.9's words for owning roles. The names used for the other end — *the
organization*, *the location*, *the ancestor*, *the caused event* — are illustrative.

## 8. Owning Role

### 8.1 Source facts

- Blueprint §13.9: *"If both endpoints' Relationship Records held it authoritatively there would be
  two sources of truth for one edge — a direct violation of Spine law 1. Exactly one endpoint owns
  it"*, and *"The relationship type definition in the Registry declares which participant role owns
  the edge."* Its examples: *"MEMBER_OF is owned by the member; LOCATED_IN by the located thing;
  DESCENDS_FROM by the descendant; CAUSED by the causing event."*
- §13.9: *"This rule is deterministic, requires no tie-breaking, and does not depend on creation
  order or on which object the author happened to be editing."*
- I-73: *"Wherever a Record Model uses Relationship Records, a relationship is authoritative in
  exactly one Relationship Record, determined by the Registry type definition's owning role."*
- I-90: *"Package composition is owned by each Record Model; the relationship-ownership rule is
  not."*
- Roadmap PART III, LS-3: *"Relationship ↔ Relationship-Type-Definition — including the owning-role
  declaration. ATOMIC-PAIR."* Row 079 `Done`: *"participant roles and owning role declared"*.

### 8.2 The obligation

1. **Mandatory.** Every `RELATIONSHIP-TYPE-DEFINITION` designates an owning role. A definition
   without one does not meet this family (§17 Example G).
2. **Exactly one.** REQUIRED SYNTHESIS from *"Exactly one endpoint owns it"* and *"declares which
   participant role owns the edge"*: a type designates one owning role, never two and never none.
3. **One of its own roles.** The owning role is one of the participant roles the same type
   declares. It cannot name a role the type does not declare (§17 Example F).
4. **Stated, not inferred.** The designation is part of the definition. It is not derived from the
   type's direction, from the order in which roles are written, from which participant is
   mentioned first, from creation order, from the object being edited or inspected, or from any
   tie-breaker.
5. **Not an instance.** The owning role names a role, never a particular Record. *MEMBER_OF —
   owning role: the member* identifies no Character.

### 8.3 Owning role, owning endpoint, owning model

| Question | Responsibility |
|---|---|
| What relationship type exists? | the Registry definition |
| What are its participant roles? | the Registry definition |
| Which participant role is the owning role? | the Registry definition |
| Which actual endpoint occupies that role in a given relationship? | the actual relationship, under its Record Model |
| Which actual Record holds the authoritative edge? | where Relationship Records are used, the Relationship Record of the endpoint occupying the owning role (I-73) |
| Who owns the relationship instance? | the applicable Record Model |
| Who produces the non-owning endpoint's Derived view? | the downstream projection — row 224 for World |
| Who records relationship changes? | the owning object's temporal mechanism — World's History Record for World (I-74) |

The table states responsibilities. It is not an algorithm, and none is implemented.

### 8.4 Deterministic application

**REQUIRED SYNTHESIS** from §13.9 and I-73. Where Relationship Records are used, the owning endpoint
of an edge is the participant that occupies the type's owning role — and nothing else decides it.
Because the rule *"requires no tie-breaking"*, exactly one endpoint of each edge must occupy the
owning role. How World types a relationship whose two endpoints would stand in the same role is
World's own work (rows 197–198; SC-079-Q); this specification neither forbids such a relationship
nor supplies a tie-breaker for it.

The ownership rule is not model-owned (I-90): a model that uses Relationship Records does not pick a
different endpoint from the one the type's owning role names.

### 8.5 Definition validity and application

Two questions stay apart: whether a definition is valid against this family, and what its declared
owning role does to actual connections. Four statements answer them, at different evidence levels.

- **A — definition validity, every Record of the family.** SOURCE FACT + REQUIRED SYNTHESIS. Every
  Record of Kind `RELATIONSHIP-TYPE-DEFINITION` declares its type's meaning, its participant roles
  and exactly one owning role among them (§5.3; row 079 `Done`; the Registry owns *"The definition
  of a relationship type and its owning role"*, §13.6e). Validity is decided by the definition's
  own content. It does not depend on which model uses the type or on whether that model holds
  Relationship Records; a type defined for a model without them is not exempt.
- **B — the model's relationship architecture.** SOURCE FACT. Each Record Model decides how its own
  connections are represented: Relationship Records where its architecture establishes them; its
  references, dependencies or workflow transitions; knowledge relationships *"within
  KNOWLEDGE-STATE"*; composition (RMS §15; each model owns *"Whether it uses Relationship Records at
  all"*, §13.6e). These mechanisms are not equivalent, and the family's existence reclassifies none
  of them. Blueprint §13.3 gives every relationship in its sense a Registry-defined type; it does
  not make every connection such a relationship (§10). Which of a model's other connections, if
  any, a `RELATIONSHIP-TYPE-DEFINITION` governs is that model's architecture to state (rows 197,
  276, 338, 356, 366).
- **C — application where Relationship Records are used: source-established.** I-73 applies
  *"Wherever a Record Model uses Relationship Records"*; it is not limited to World. There §8.2 to
  §8.4 apply: the participant occupying the declared role is the endpoint that holds the edge; the
  edge is authoritative in exactly one Relationship Record; the non-owning endpoint's view is
  Derived; and no creation-order, editing-context, role-order or direction-based tie-breaker
  replaces the declared role (§13.9; I-73). The §13.3 scoping note places *"the Relationship
  Record, its ownership rule, and its boundedness"* in World Record Model architecture, and I-90
  keeps the rule from being model-owned: a model that adopts Relationship Records on its own
  evidence (§11) applies the owning role as I-73 states it, not a variant of it.
- **D — application elsewhere: open (OD-079-2).** Where a model holds no Relationship Records —
  Production by RMS §15, Epistemic by row 276, and Visual and Issue unless their own architectures
  adopt them — no source states what a declared owning role governs. The
  declaration stands, and nothing further is inferred: no storage mechanism, endpoint-ownership
  algorithm or World Relationship Record is required, and the declaration does not by itself
  change who holds a reference or a workflow transition. OD-079-2 records the decision, its owners
  and what it blocks (§19.1).

**Prerequisites per model.** REQUIRED SYNTHESIS from I-73's scope condition and RMS §15's rows.
Before a model's type set can give a declared owning role an effect outside Relationship Records,
that model's architecture has to answer the questions below. They are questions, not answers: the
table states what is not yet established and supplies no effect.

| Model | Mechanism (RMS §15) | What its architecture must state first | Rows |
|---|---|---|---|
| **W** | *"World Relationship Record — reified; Registry declares the owning role"* | nothing further: I-73 and §13.9 apply | 197, 198 |
| **E** | *"EVIDENCE first-class; knowledge relationships represented within KNOWLEDGE-STATE"* | which of its connections this family types; for each, what the owning role selects within KNOWLEDGE-STATE or EVIDENCE, and whether the other participant's view is Derived | 276, then 277 |
| **P** | *"References · dependencies · workflow transitions. No Relationship Record"* | which of these this family types; for each, whether the owning role must be the side that holds the reference or transition (044 §8), and what follows where it is not | 338 |
| **V** | *"represents · derived-from · variant-of — model-owned"* | its mechanism for each — if it holds any in Relationship Records, I-73 applies there; otherwise, what the owning role selects in that mechanism | 356 |
| **I** | *"Composition · placement · credit · supersession references"* | which of its references this family types — composition is *"composition, not relationship"* (§13.6d) — and, for each, whether it is held in Relationship Records (then I-73 applies) or what the owning role selects instead | 366 |
| **R** | *"Relationship definitions; never runtime relationship ownership"* | none: no Registry type set exists, and definition dependencies are *"not owned edges"* (§13.2), governed by row 111 | — |

> **The owning-role declaration is a condition of validity for every `RELATIONSHIP-TYPE-DEFINITION`
> Record. Its application is source-established wherever Relationship Records are used (I-73;
> Blueprint §13.9) and open elsewhere (OD-079-2). It does not require every connection in every
> Record Model to be represented by such a definition: whether a reference, dependency, workflow
> transition, composition link or other connection is governed by a relationship-type definition is
> decided by the governing sources and that model's relationship architecture.**

## 9. Direction, Cardinality and Legality

### 9.1 Source facts

Blueprint §13.3: *"Every relationship has a Registry-defined type carrying its participant roles,
its direction, its cardinality, and its legality constraints (which kinds may stand at each end)."*
Its scoping note makes the principle — *"a relationship is a modelled thing with a type, a
direction, a temporal validity, and provenance, rather than a field"* — *"a Record System principle
available to every model"*. Artifact 055 §6 lists the type as *"meaning, participant roles,
direction, cardinality, legality, owning role"*.

**REQUIRED SYNTHESIS.** A `RELATIONSHIP-TYPE-DEFINITION` that types a relationship in §13.3's sense
governs its direction, cardinality and legality constraints as type semantics, beside its roles and
owning role. Whether all three apply to the types of a model's connections that are not reified —
Production's references, for example — and whether such connections are typed by this family at
all, is that model's architecture to state (§8.5; SC-079-H; OD-079-2).

### 9.2 Direction

Direction is a semantic concern of the type: how a relationship of the type reads from one role to
another — illustratively, `MEMBER_OF` reads from the member to the organization. It is stated by the
definition and holds for every relationship of the type.

Direction and owning role are separate declarations. In each of §13.9's four examples the owning
role happens to be the role the type's name reads from; no source makes that a rule, and none
derives the owning role from direction or direction from the owning role. No direction token,
default, reversal rule, inverse type or *source*/*target* serialization is defined (SC-079-F).

### 9.3 Cardinality

**SOURCE FACT.** Cardinality is part of the Registry-defined type of a relationship in §13.3's
sense (§9.1), and is governed definition content of such a type. It is distinct from:

- participant-role arity — how many participant positions a type has (§7);
- field-occurrence cardinality — how many values a field occurrence may carry in a schema. Artifact
  077's `occurrence.cardinality` is that, and is not thereby a representation of this cardinality;
- Record cardinality — how many Records of a Kind exist for a key, as RMS §8.1 states for
  KNOWLEDGE-STATE and REVEAL-STATE (*"No per-knower multiplication."*) and row 259 rules;
- edge count — how many actual relationships an object currently holds;
- definition count — how many `RELATIONSHIP-TYPE-DEFINITION` Records exist;
- the cardinality of any Registry reference a definition carries;
- a universal binary-relationship grammar.

**SOURCE GAP — open decision OD-079-1.** No inspected source states what a type's cardinality
bounds, what values it admits, whether it has a default or a notation, or whether its meaning is
the same in every model. The readings the sources leave open include a bound per participant role, a
bound per participant, a bound on the relationship as a whole, and a model-owned meaning. They are
listed to show what the decision must settle; this specification adopts none and rejects none. No
value, *one-to-one*/*one-to-many* enumeration, syntax or cross-model policy is defined (SC-079-F;
§19.1).

**A carrier does not settle meaning.** A schema carrier cannot itself settle the meaning of the
value it carries. Its shape presupposes an answer: a value attached to each role presumes a per-role
bound; one value per type presumes a bound on the type as a whole; an enumeration presumes a value
set; a default presumes that an unstated cardinality has a meaning. Choosing any of these to make a
schema complete would decide OD-079-1 by representation.

**The boundary for Artifact 080 while OD-079-1 is open.**

| 080 may | 080 may not |
|---|---|
| meet its own `Val` and `Done`, neither of which names cardinality | give cardinality a value set, enumeration, default or notation presented as source semantics |
| record that §13.3 makes cardinality type content and that its meaning is open (OD-079-1) | choose a carrier whose shape presupposes what cardinality bounds — per role, per participant, per relationship — or a one-to-one/one-to-many scheme |
| make a representation choice that presupposes no answer to OD-079-1, recorded as its own; whether a given choice presupposes none is for 080 to show, not to assume | define a check of a type's cardinality against actual relationships |
| leave cardinality unrepresented, recording that the omission defers §13.3 and does not deny it | reuse field-occurrence cardinality (077) as relationship-type cardinality |

**What OD-079-1 blocks.** Until it closes: no type set — rows 198, 277, 338, 356, 366 — can state a
cardinality with a checkable meaning; rows 112 and 116 cannot validate one; and no model's
mechanism can enforce one on actual relationships. It blocks neither row 079's `Val` nor its
`Done`, and neither of 080's, none of which names cardinality.

### 9.4 Legality — participant eligibility

**SOURCE FACT.** The type carries *"its legality constraints (which kinds may stand at each end)"*
(§13.3). RMS §10.3 lets a Registry definition reference *"declared Kinds"* and *"declared Record
Models"*, and forbids domain instances.

**079 FAMILY INTERPRETATION.** A type may state, for each participant role, which Kinds may stand
in it — the source's *"which kinds may stand at each end"* — each a declared Kind of a declared
Record Model. Then:

- a Kind named as eligible is a declared Kind of its owning Record Model; naming it does not admit
  it (Artifact 057 §9) or create it, and an undetermined Kind is not legal (063 RB-6; RF-079-1);
- as this specification states eligibility — by naming the Kind itself — it is a declaration
  reference, not an R → R reference to the Kind's `KIND-DEFINITION` (063 §8.3), and it does not, by
  itself, establish a semantic dependency on the Kind's semantics (062 D-9). Both hold for that
  statement only. If Artifact 080 carries eligibility by referring to a `KIND-DEFINITION` Record,
  that carrier is an R → R reference (063 §8.1), and whether it is also a semantic dependency is
  062's and row 111's to decide; this specification does not decide it in advance (§15 RF-079-1,
  RF-079-7);
- a type's eligibility does not override the cross-model dependency rules (Artifact 058) or a
  model's own constraints — World is manifestation-blind: *"no World field may reference an issue,
  tier, medium, artifact, or the real world"* (RMS §7);
- semantic legality is not its checking: the check is a validation concern (RMS §10.6, §20), not
  executed by the definition.

No universal allowed-Kind matrix, cross-model permission scheme or automatic eligibility of every
Kind of every partition is defined (SC-079-G).

### 9.5 Mandatory and permitted, summarized

| Concern | Status for every definition | Basis | Representation |
|---|---|---|---|
| meaning | mandatory — definition validity | RMS §6.1; 064 Q4 | 080 |
| participant roles | mandatory — definition validity | row 079 `Done`; §13.3 | 080 |
| owning role | mandatory — definition validity: exactly one, one of its roles; application source-established where Relationship Records are used, open elsewhere (OD-079-2) | row 079 `Done`; §13.9; I-73; LS-3 | 080 |
| direction | type semantics where the type is of a §13.3 relationship | §13.3 | 080; SC-079-F |
| cardinality | type semantics where the type is of a §13.3 relationship; what it bounds, its values, default and notation are open (OD-079-1) | §13.3 | 080, within §9.3's boundary |
| legality — eligibility per role | type semantics where the type is of a §13.3 relationship; declared entities only | §13.3; RMS §10.3 | 080; SC-079-G |
| an instance's identity, endpoints, validity, provenance, history | never in the definition | §13.3; I-74; RMS §10.3 | — |

## 10. Reification Boundary

**SOURCE FACT.** RMS §15 (`FROZEN`): *"reify only when no endpoint can own the edge without
ambiguity"*. RMS §6.1: a Relationship is *"A connection between Records"*, *"First-class only when
no endpoint can own it"*. Artifact 055 §5 states the test and records that no source defines when
ownership is *ambiguous*.

**Two questions, kept apart** (Artifact 055 §5.2: *"Two uses of "own""*):

| Question | Decided by | Basis |
|---|---|---|
| **A — reification:** can one endpoint own this connection without ambiguity, as a field or as a reference held by the owning side? If so it is not a first-class Relationship. | the owning model's relationship architecture, applying RMS §15's criterion (rows 197, 276, 338, 356, 366) | RMS §15, §6.1; Artifact 044 §8; 055 §5 |
| **B — owning role:** for a relationship that is held in Relationship Records, which participant's Record holds the edge? | the type's owning role, declared by this family | §13.9; I-73 |

- The reification decision does not choose a type's owning role.
- The owning-role declaration does not reify a connection, does not make every connection a
  Relationship Record, and does not bring every connection under this family (§8.5).
- A type definition existing for a model is no evidence that the model uses Relationship Records:
  row 338 pairs Production's relationship architecture — *"References · dependencies · workflow
  transitions. No Relationship Record"* (RMS §15) — with type definitions.

**The tension, stated.** Read with a single sense of *own*, two sources collide. RMS §15 reifies a
connection *"only when no endpoint can own the edge without ambiguity"*. Blueprint §13.9 says of a
World edge *"Exactly one endpoint owns it"*, and §8.2 makes an owning role mandatory for every type.
If *own* meant the same in both, every typed edge would have an unambiguous owner, the criterion
would never be met, and nothing could be reified — contradicting RMS §15's own World row,
*"World Relationship Record — reified; Registry declares the owning role"*.

**Reconciliation.** REQUIRED SYNTHESIS from RMS §15, Artifact 044 §8, Blueprint §13.9 and Artifact
055 §5.2. The criterion's *own* is ownership *"as a field, or as a reference held by the owning
side"* (044 §8), asked before reification. §13.9's *own* is custody: which endpoint's Relationship
Record holds an edge that has already qualified. RMS §15's World row states the two in that order,
and 055 §5.2 reads them as two steps and adds no third test. On that reading the sources are
consistent, and this specification follows it: Question A uses the first sense, Question B the
second.

**Residual.** Neither the RMS nor the Blueprint states the two senses in its own text; the
reconciliation rests on 044's wording, the order of RMS §15's World row and 055's reading. This
specification does not amend either source to make it explicit, and it registers the wording for
the Blueprint/RMS author (SC-079-S). The residual blocks nothing here: Question B applies only to an
edge already held in Relationship Records, whichever way Question A was answered for it.

**SOURCE GAP.** No quantitative threshold, score, decision tree, classifier or list of connections
that must be reified is defined (SC-079-D). Applying the criterion is each model's work.

## 11. Six-Model Sovereignty

**SOURCE FACT.** RMS §15: *"Model relationships are not identical and are never made so."* RMS §4
prohibits a *"Universal Relationship Record"*. I-102: *"Relationship Record and History Record are
World Record Model concepts. Neither is a Record System primitive, and neither may be required of
another Record Model."* Blueprint §13.7a: *"The Record System shares mechanisms. It does not share
semantics."*

| Model | RMS §15 mechanism (quoted) | What this family is to it | World Relationship Record required? | Its rows | Not decided here |
|---|---|---|---|---|---|
| **W** | *"World Relationship Record — reified; Registry declares the owning role"* | defines World's relationship types; the owning role decides which Relationship Record holds each edge | World's own construct | 197, 198, 199 | which types exist; the causal and pressure families (row 198) |
| **E** | *"EVIDENCE first-class; knowledge relationships represented within KNOWLEDGE-STATE"* | defines E's relationship types (row 277: *"evidence-for, contradicts, supersedes"*) | no — row 276: *"no Relationship Record"* | 276, 277 | what the owning role governs within KNOWLEDGE-STATE (OD-079-2) |
| **P** | *"References · dependencies · workflow transitions. No Relationship Record"* | defines the types row 338 pairs with P's architecture | no | 338 | what the owning role governs for references and transitions (OD-079-2) |
| **R** | *"Relationship definitions; never runtime relationship ownership"* | is the family; R's own definition connections are *"dependencies under a downward-only rule"*, *"not owned edges"* (§13.2) | no | 079, 080 | — |
| **V** | *"represents · derived-from · variant-of — model-owned"* | defines V's relationship types (row 356) | not imposed | 356 | V's mechanism and the owning role's effect in it (OD-079-2) |
| **I** | *"Composition · placement · credit · supersession references"* | defines I's relationship types (row 366) | not imposed; composition is not relationship | 366 | I's mechanism and the owning role's effect in it (OD-079-2) |

The mechanism column is RMS §15's. No model is required to use a Relationship Record, and none is
barred from adopting a structure of the same shape on its own evidence (§13.9; Artifact 055 §8.3),
and the family requires no model to type every connection through it (§8.5). Blueprint §13.6d's
package rows for non-World models are *"MODEL-DESIGN INPUT (not a freeze)"* and are not imposed.
Shared definition infrastructure imposes no common instance kind, storage, lifecycle, canonicality,
temporal schema, package or relationship-type roster.

## 12. Relationship versus Field, Reference, Composition and Dependency

| Concept | What it is | Owner | Not to be confused with |
|---|---|---|---|
| `RELATIONSHIP-TYPE-DEFINITION` | governs a type's meaning, participant roles and owning role | Registry | an edge |
| relationship instance | one actual connection under the applicable model's architecture | the owning Record Model | its type |
| World Relationship Record | World's mechanism holding an object's current authoritative edges | World | a universal construct |
| `FIELD-DEFINITION` | the meaning and domain of one field | Registry | relationship meaning |
| `SCHEMA-DEFINITION` | a governed schema definition | Registry | relationship meaning |
| reference | a pointer held by the owning side | the holding Record's model | a first-class relationship |
| composition | part-of structure a model expresses as such | that model | a Relationship Record |
| dependency | a governed dependency — between Registry definitions, under the downward-only rule | the relevant architecture (111 for Registry) | a relationship instance |
| back-reference projection | the non-owning endpoint's view of an owned edge | Derived | a second authoritative edge |
| history / temporal account | how relationships came to be as they are | the owning object's model — World's History Record | the current edge |

- **Field.** *"A relationship is not a field and not an attribute."* (§13.3). A pointer an endpoint
  can own without ambiguity stays a field (055 §5.3); a field ending in `_ref` is not thereby a
  relationship.
- **Reference.** A reference held by the owning side is the default (Artifact 044 §8). A Record
  referring to another does not create an independently authoritative edge, and a Registry
  definition naming a declared Model or Kind defines no instance relationship.
- **Composition.** Issue's interior is *"composition, not relationship"* (§13.6d); page and spread
  composition is not a Relationship Record and no universal relationship implementation.
- **Dependency.** *"A registry definition's connections are dependencies under a downward-only rule
  (Section 9.4), not owned edges"* (§13.2). A type naming a participant Kind does not, by itself,
  establish a semantic dependency (062 D-9; §15); whether a concrete relation 080 carries is also a
  dependency, and its mechanics, are row 111's.

## 13. World Relationship Record Consequences

These follow from the owning-role declaration and are stated so that the family's effect is clear.
None is implemented here; rows 197–199 and 224 own them.

- **One authoritative edge.** An edge is authoritative in exactly one Relationship Record — the one
  of the endpoint occupying the owning role (I-73; §13.9). *"An edge appearing authoritatively in
  two Relationship Records is a structurally decidable violation and is blocked by the linter"*
  (§13.9).
- **Derived non-owner.** The other endpoint *"sees a back-reference, which is a Derived
  projection"*, *"rebuildable from the owning Relationship Records, marked stale like any other, and
  never authoritative"* (§13.9). *"A capability that reads a back-reference as though it were the
  record is making a Derived source authoritative"* (§12.11). Row 224 builds it: *"back-references
  derived, never stored on the record"*.
- **Current only.** *"A Relationship Record holds an object's current relationships and nothing
  else."* (§13.5); row 199: *"current relationships only; history lives in the History Record"*.
- **History elsewhere.** *"Every relationship change is recorded in the owning object's history"*
  (I-74). A type definition carries no edge, no edge's past states, no participant identifiers, no
  snapshots and no graph data.
- **World Time is World's.** A World relationship holds *"from"* and *"until"*, *"in world-time"*
  (§13.3). That is a property of World instances. A definition's versionability (§14) is not an
  instance's temporal validity, and no relationship timestamp grammar is defined.
- **WSV.** Recorded at SC-079-M; no WSV rule is part of this family.

## 14. Identity, Resolution and Versionability

Row 079 `Val`: *"definition resolves"*.

| ID | Obligation |
|---|---|
| **RS-079-1** | A `RELATIONSHIP-TYPE-DEFINITION` is a Registry Record with independent identity (064 Q3; F-1). Once materialized it carries ordinary Record identity under the universal grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` and the seven-field envelope — `partition` · `kind` · `object_id` · `slug` · `provenance` · `registry_ref` · `sot_class` (RMS §4, §5). No eighth field. |
| **RS-079-2** | That identity is the R Record's own. It is not the type's name (`MEMBER_OF` is a name, not an identity), not a role's name, not a participant's identity, not an edge's identity and not a Relationship Record's identity. The slug is decoration only (RMS §5). No kind code or `object_id` is minted. |
| **RS-079-3** | Three identities stay apart: the definition's (one governed type); an actual relationship's (*"its own stable identity"*, §13.3, where the model makes it first-class); a Relationship Record's (a World Record, or another model's construct). |
| **RS-079-4** | A consumer must be able to resolve a materialized definition; reference resolution is universal and mechanical (RMS §4). Create, resolve and version are row 114's; consumer resolution by id+version row 115's. No resolver, lookup, minting or registration is defined here, and resolvable ≠ legal (063 §11). |
| **RS-079-5** | Resolving a type definition returns a definition; it creates no edge, assigns no endpoint and transfers nothing. |

Row 079 `Val`: *"versionable"*.

| ID | Obligation |
|---|---|
| **VS-079-1** | A `RELATIONSHIP-TYPE-DEFINITION` participates in governed Registry definition evolution under rows 108–110 (064 F-4). Every version stays bound by this specification. Its temporal account is the Registry's: *"temporal account without a World History Record"* (row 108; I-102). |
| **VS-079-2** | **Not defined here ≠ forbidden.** No version field, identifier syntax, supersession, deprecation, migration, matching or compatibility rule is defined, and none is prevented. Future governed revisions of a type's meaning are not forbidden. |
| **VS-079-3** | A definition's version history is not edge history. Evolving a type changes a definition; it does not by itself move, rewrite, re-own or revalidate any edge. Whether a revision that changes a type's owning role, roles or eligibility has consequences for existing edges is not established by any inspected source; it is left to rows 108–110 and the owning model, and is not decided here in either direction. |

## 15. Reference Boundary

Row 079 `Val`: *"references only declared entities (063)"*. RMS §10.3: *"Registry MAY reference:
other Registry definitions · declared Record Models · declared Kinds · declared schemas · declared
semantic contracts."* · *"Registry MAY NOT: own domain instances · depend on runtime instances ·
mutate domain instances · use domain instances as semantic authority."* Artifact 063 §22 leaves to
each family *"which concrete reference relations each family carries"*.

| ID | Rule | Basis |
|---|---|---|
| **RF-079-1** | **Eligibility names declared entities.** Where a type states participant eligibility, any Kind it names is a declared Kind of its owning, declared Record Model, whose declared status is that model's Kind architecture's to establish. As stated here — naming the Kind itself — this is a declaration reference, not a reference to a `KIND-DEFINITION` or `MODEL-DEFINITION` Record. That classification is of the statement, not of a carrier: if 080 carries eligibility by referring to a `KIND-DEFINITION` or `MODEL-DEFINITION` Record, the carrier is an R → R reference (063 §8.1, §8.2), still bounded by the declared-Kind rule. Whether eligibility may be stated at Model level without a Kind is not established (SC-079-G). An undetermined target is not legal. This is the family's one source-grounded concrete reference relation; its form is 080's. | §13.3; RMS §10.3; Artifact 063 §7 rows 2–3, §8.1–§8.3, RB-1, RB-6 |
| **RF-079-2** | **No domain instance.** No actual Record — a Character, an Organization, any Record of W, E, P, V or I — defines a role, is a participant of the definition, or is its semantic authority. No actual edge or Relationship Record is a target. | RMS §10.3; Artifact 063 §7 row 6 |
| **RF-079-3** | **No domain state.** No current value of any model is the semantic authority of a type. | Artifact 063 §7 row 7 |
| **RF-079-4** | **No runtime instance.** No graph store, projection process, validator, service or session is a target, a dependency or an authority; I-84: no external component *"owns a relationship"*. | RMS §10.3; I-84; Artifact 063 §7 row 8 |
| **RF-079-5** | **Admissible category ≠ family relation.** Other Registry definitions are admissible targets; that obliges no type to reference any. No reference to a `FIELD-DEFINITION`, `SCHEMA-DEFINITION`, `CONTROLLED-VOCABULARY`, `CONSTRAINT-DEFINITION`, `VALIDATION-RULE` or another type is created here. Not created ≠ forbidden later. | Artifact 063 RB-5, §22 |
| **RF-079-6** | **No carrier invented.** No participant, owner, edge, Relationship Record, type or endpoint reference element is defined; Artifact 080 owns the structure. | row 080 |
| **RF-079-7** | **Layer: L1 peer semantics.** Artifact 062 places *"relationship type and participant-role semantics"* in L1 stratum 1b, which may depend on RFS and must not depend on L2–L5 (D-8). Naming a declared Kind as eligible is a declaration reference that does not, by itself, establish a semantic dependency (D-9). Should a concrete relation that 080 carries also be a semantic dependency, D-8 forbids it to run upward from the type's meaning to Kind, subtype, instance or derived semantics, and row 111 governs it; this specification does not classify a carrier it does not define. | Artifact 062 §6, §7 D-8, D-9; row 111 |
| **RF-079-8** | **Reference ≠ dependency.** No role declaration or eligibility statement is a dependency-graph edge by itself. Where a concrete relation is also a semantic dependency, row 111's direction, asymmetry and cycle rules apply. | Artifact 062 D-9; Artifact 063 RB-5; row 111 |
| **RF-079-9** | **Resolvable ≠ legal; no transfer.** A target that resolves may still be illegal. A legal reference transfers no ownership, mutation authority, semantic authority, admission, canonicality or source-of-truth class. | Artifact 063 §11, §12 |

How an actual relationship identifies its type — what references a `RELATIONSHIP-TYPE-DEFINITION`
— is *"not established"* (064 Q7); LS-3 is lockstep, not a reference, and this specification creates
no inbound reference (SC-079-P).

The Blueprint's older wording — *"A Registry definition may never reference a kind, a subtype, or
an instance"* — is not current law for reference legality; RMS §10.3 corrects it (SC-079-R).
Domain instances stay forbidden.

## 16. Normative Family Rules

The IDs below are this specification's, not pre-existing constitutional identifiers.

| ID | Rule | Basis | Evidence |
|---|---|---|---|
| **RT-079-01** | **Registry Kind.** A `RELATIONSHIP-TYPE-DEFINITION` is an R Registry definition Record of Kind 6 of RMS §10.1's frozen fourteen. No Kind is created, renamed or merged. | RMS §10.1; 064 §6, §13 | SOURCE FACT |
| **RT-079-02** | **One type.** Each Record governs one relationship type's meaning; it is not a relationship instance or a set of edges. | §13.6e; RMS §6.1; 064 Q1 | SOURCE FACT |
| **RT-079-03** | **Participant roles.** Each type declares its participant roles, each distinguishable within the type; they are not inferred. | §13.3; §9.4; row 079 `Done` | SOURCE FACT + REQUIRED SYNTHESIS |
| **RT-079-04** | **Owning role.** Each type designates exactly one owning role. | §13.9; §13.6e; LS-3; row 079 `Done` | SOURCE FACT + REQUIRED SYNTHESIS |
| **RT-079-05** | **Role membership.** The owning role is one of the participant roles the same type declares. | §13.9; row 079 `Done` | REQUIRED SYNTHESIS |
| **RT-079-06** | **Unambiguous ownership.** No type carries two owning roles, two competing designations, or a designation giving both endpoints independent authority over one edge. | §13.9; Spine law 1; I-73 | SOURCE FACT |
| **RT-079-07** | **Deterministic application.** Wherever a Record Model uses Relationship Records, World or another, the endpoint occupying the owning role holds the edge authoritatively; exactly one endpoint occupies it; no tie-breaker is used. A model does not choose another endpoint. Application outside Relationship Records is OD-079-2. | §13.9; I-73; I-90; §8.5 | SOURCE FACT + REQUIRED SYNTHESIS |
| **RT-079-08** | **No order or context.** The owning role is not chosen by creation order, editing context, inspection, direction or role order. | §13.9 (*"declares"*; not creation order or editing context) | SOURCE FACT + REQUIRED SYNTHESIS |
| **RT-079-09** | **Derived non-owner.** In World's Relationship Record architecture the non-owning endpoint's view is Derived and never authoritative. | §13.9; §12.11; I-73 | SOURCE FACT |
| **RT-079-10** | **Model-owned instances.** The Registry owns the definition, never a relationship instance, its storage or its history. | §13.6e; RMS §15; I-88; 061 §7 row 3 | SOURCE FACT |
| **RT-079-11** | **Model-owned packaging.** The family requires no Relationship Record of E, P, R, V or I, and forbids no model's own source-authorized mechanism. | I-102; §13.6e; RMS §15 | SOURCE FACT |
| **RT-079-12** | **Reification apart.** The reification criterion and the owning role answer separate questions and use separate senses of *own* — as a field or reference, and custody of a reified edge; neither decides the other, and a type definition reifies nothing. The sources' wording of the two senses is registered upstream (SC-079-S). | RMS §15; 044 §8; 055 §5.2; §13.9; §10 | REQUIRED SYNTHESIS |
| **RT-079-13** | **Direction.** Direction is type semantics where the type is of a §13.3 relationship; it is declared separately from the owning role; no representation is invented. | §13.3 | SOURCE FACT + 079 FAMILY INTERPRETATION |
| **RT-079-14** | **Cardinality.** Cardinality is governed type content where the type is of a §13.3 relationship, distinct from arity, field-occurrence cardinality, Record cardinality, edge count and definition count. What it bounds, its values, default and notation are open decision OD-079-1; a carrier cannot settle them, and 080 works within §9.3's boundary until OD-079-1 closes. | §13.3; §9.3; SC-079-F; §19.1 | SOURCE FACT; detail SOURCE GAP |
| **RT-079-15** | **Participant eligibility.** Eligibility names declared Kinds of declared Models only, admits nothing, and overrides neither 058 nor a model's own constraints. | §13.3; RMS §10.3; 057 §9; 058; RMS §7 | SOURCE FACT + REQUIRED SYNTHESIS |
| **RT-079-16** | **Not an instance.** A definition holds no actual endpoint, edge identity, temporal validity, provenance, history or graph data. | §13.3; I-74; RMS §10.3 | REQUIRED SYNTHESIS |
| **RT-079-17** | **Not a field or a reference.** A relationship type is neither a field nor a reference, and makes no field or reference a relationship. | §13.3; RMS §6.1; 044 §8 | SOURCE FACT |
| **RT-079-18** | **Not a dependency by itself.** Declaring roles, an owning role or eligibility establishes no dependency edge by itself; as L1 peer semantics the type's meaning may not depend upward on Kind, subtype, instance or derived semantics. Whether a concrete relation 080 carries is also a semantic dependency is row 111's, under D-8. | §13.2; 062 §6, D-8, D-9; row 111 | SOURCE FACT + REQUIRED SYNTHESIS |
| **RT-079-19** | **Independent identity.** The definition has its own R Record identity, distinct from the type's name, any edge and any Relationship Record. | RMS §4, §5; RS-079-1 to RS-079-3 | SOURCE FACT |
| **RT-079-20** | **Versionability.** The definition evolves under rows 108–110, not by mechanics invented here, and its version history is not edge history. | 064 F-4; rows 108–110; VS-079 | SOURCE FACT |
| **RT-079-21** | **Reference legality.** Every concrete reference the family carries obeys Artifact 063. | RMS §10.3; 063; RF-079 | SOURCE FACT |
| **RT-079-22** | **No execution.** The definition creates, moves, mutates, projects or validates no relationship. | RMS §6.1; §13.6e; I-84 | SOURCE FACT |
| **RT-079-23** | **No universalization.** No Universal Relationship Record, Universal History Record, universal relationship schema or package, or universal role grammar is introduced. | RMS §4; §13.7a; I-102 | SOURCE FACT |
| **RT-079-24** | **Structural handoff.** Artifact 080 receives the semantic obligations of §21 and no mandatory field inventory. | row 080 | 079 FAMILY INTERPRETATION |
| **RT-079-25** | **Validity apart from application.** The owning role is declared for every Record of the family, including types of models that hold no Relationship Record; that is definition validity. Its application is source-established where Relationship Records are used and open elsewhere (OD-079-2), with the per-model prerequisites of §8.5. The obligation brings no model-owned connection under the family. | row 079 `Done`; §13.3; §13.6e; I-73; RMS §15; SC-079-H | SOURCE FACT + SOURCE GAP |

## 17. Worked Examples

Every example is **schematic**. No Record is created, no identifier is minted, and no type below is
a committed Registry Record. The four World types are Blueprint §13.9's illustrations; World's
concrete type set is row 198's.

**A. Legal — MEMBER_OF.** *Character A MEMBER_OF Organization B.* Participant roles: the member;
the organization. Owning role: the member. In World's Relationship Record architecture Character A
is the owning endpoint and holds the edge; Organization B has a Derived back-reference. The
Registry defines the rule; World owns the edge.

**B. Legal — LOCATED_IN.** *Character A LOCATED_IN Location B.* The located thing is the owning
role (§13.9), so the edge is held by Character A's Relationship Record. No cardinality, identity or
temporal interval is asserted.

**C. Legal — DESCENDS_FROM.** The descendant is the owning role (§13.9); the descendant's
Relationship Record holds the edge. No inheritance, parentage or lineage constraint is added.

**D. Legal — CAUSED.** The causing event is the owning role (§13.9). Four things stay apart: what
the causal role means (the type); the actual causal edge (World's); the Record holding it (the
causing event's Relationship Record); the edge's change history (that event's History Record).
Simulation may walk causal edges as *"first-class structure rather than inference"* (§13.3);
walking an edge is not owning it, and no simulation engine or causal graph schema is defined.

**E. Illegal — dual ownership.** Character A's and Organization B's Relationship Records both hold
*A MEMBER_OF B* authoritatively. Rejected: *"two sources of truth for one edge — a direct violation
of Spine law 1"* (§13.9); I-73.

**F. Illegal — owning role outside the roles.** A type declares the roles *member* and
*organization* and designates *observer* as owning role. Rejected: the owning role must be one of
the type's own roles (RT-079-05).

**G. Illegal — no owning role.** A type declares its participant roles and designates no owning
role. Rejected against this family: row 079's `Done` requires the owning role (RT-079-04).

**H. Boundary — a Production reference or workflow dependency.** A Production Record references
another Record as part of a workflow dependency. Invalid inference: because the Registry has a
relationship-type family, the dependency must become a World-style Relationship Record, or must be
given a `RELATIONSHIP-TYPE-DEFINITION`. Rejected: Production has *"References · dependencies ·
workflow transitions. No Relationship Record"* (RMS §15), and the family's existence reclassifies
no connection (§8.5). How the dependency is represented is Production's architecture's (row 338).
If that architecture does govern a relationship type through a `RELATIONSHIP-TYPE-DEFINITION`, the
definition still declares its participant roles and exactly one owning role — that is definition
validity — and what that role governs inside Production's mechanism is open (OD-079-2; SC-079-H)
until row 338 answers §8.5's prerequisites for P. No Production Kind, type name or type roster is
given here.

**I. Boundary — a Registry dependency.** A Registry definition refers to another Registry definition
where a family contract establishes the relation. That makes the Registry the owner of no runtime
edge: such connections are *"not owned edges"* (§13.2), and the reference satisfies Artifact 063.

**J. Boundary — an Epistemic relationship.** Epistemic knowledge relationships live *"within
KNOWLEDGE-STATE"* (RMS §15), and row 276 records *"no Relationship Record"*. The family's existence
requires no World-style Relationship Record of Epistemic. A type row 277 defines still declares one
owning role; what it selects within KNOWLEDGE-STATE or EVIDENCE is OD-079-2's, for row 276 to state.
Row 277's types are not anticipated here.

**K. Deferred — richer participant semantics.** A future type needs more than two participant
roles, or roles richer than the examples show. SOURCE GAP for its arity and representation
(SC-079-E): not rejected as constitutionally impossible, not admitted as arbitrary arity. Its own
model's architecture, within this family, decides.

**L. Illegal — a domain instance as authority.** A type definition cites a particular Character
Record, written schematically as `W-CH-…-<slug>`, as the definition of what *the member* means.
Rejected: a domain instance is never a Registry reference target or semantic authority (RMS §10.3;
RF-079-2), however well it resolves.

**M. Illegal while OD-079-1 is open — cardinality settled by a carrier.** A schema gives every
participant role a minimum and a maximum, defaulting to *zero* and *many*, so that each definition
has a complete cardinality element. Whether *Character A LOCATED_IN Location B* allows A to stand
in more than one location at once would then be answered by the schema's shape and default, not by
any source. Rejected: the carrier presumes a per-role bound, a value set and a default, which is
deciding OD-079-1 by representation (§9.3; PI-40, PI-43). Nothing here says what the right answer
is.

## 18. Prohibited Inferences

| # | Invalid inference | Correct reading | Basis |
|---|---|---|---|
| PI-01 | A `RELATIONSHIP-TYPE-DEFINITION` is a Relationship Record | a definition, not an edge holder | §5.2; RMS §15 |
| PI-02 | The Registry owns relationship instances because it defines their types | definition authority only | §13.6e; RMS §15; 061 §7 row 3 |
| PI-03 | The Registry stores current domain edges | edges live in their model's mechanism | RMS §15; I-73 |
| PI-04 | The Registry stores relationship history | history is the owning object's | I-74; §13.5 |
| PI-05 | A relationship type is merely a field | *"A relationship is not a field and not an attribute."* | §13.3 |
| PI-06 | A reference is automatically a first-class relationship | the reference held by the owning side is the default | Artifact 044 §8; 055 §5.4 |
| PI-07 | A dependency is automatically a first-class relationship | Registry dependencies are *"not owned edges"* | §13.2 |
| PI-08 | Composition is automatically a Relationship Record | *"composition, not relationship"* | §13.6d |
| PI-09 | Every Record Model must use World's Relationship Record | World-only; never required of another model | I-102 |
| PI-10 | Every connection must be reified | only when no endpoint can own it | RMS §15 |
| PI-11 | Declaring a type creates an edge | a definition *"Governs; never instantiates"* | RMS §6.1 |
| PI-12 | Declaring a participant role creates a domain Record | a role is part of a definition | §7 |
| PI-13 | The owning role identifies a particular Record | it names a role | §8.2 |
| PI-14 | The first participant is always the owner | the owning role is declared | §8.2; §13.9 |
| PI-15 | The participant on the left is always the owner | the owning role is declared | §8.2; §9.2 |
| PI-16 | A role named *source* is always the owner | no universal source/target pair | §7; §9.2 |
| PI-17 | The most recently created participant becomes owner | ownership *"does not depend on creation order"* | §13.9 |
| PI-18 | Both endpoints may be authoritative for one edge | *"Exactly one endpoint owns it"* | §13.9; I-73 |
| PI-19 | A Derived back-reference is authoritative | *"never authoritative"* | §13.9; §12.11 |
| PI-20 | The type stores actual endpoint identifiers as its roles | roles are positions, not participants | §7; RF-079-2 |
| PI-21 | All relationship types have the same cardinality | cardinality is per type | §13.3 |
| PI-22 | All relationship types use the same directional representation | no representation is fixed | §9.2; SC-079-F |
| PI-23 | All relationship types are binary across all models | binary is stated for World edges only | §7; SC-079-E |
| PI-24 | A type may name undeclared Kinds as legal participants | declared Kinds only | RMS §10.3; RF-079-1 |
| PI-25 | A legal target category authorizes every concrete reference | category ≠ relation | Artifact 063 RB-5 |
| PI-26 | A resolvable reference is legal | resolvable ≠ legal | Artifact 063 §11 |
| PI-27 | A reference is a Registry semantic dependency | not by itself | Artifact 062 D-9 |
| PI-28 | Definition version history is edge history | separate temporal accounts | §14 VS-079-3; row 108 |
| PI-29 | World-time validity applies to every model | written for World | §13.3; Artifact 055 §12 |
| PI-30 | The definition executes relationship validation | definitions execute nothing | RMS §10.6, §20 |
| PI-31 | The family creates new Registry Kinds | fourteen, closed | RMS §10.1 |
| PI-32 | A model's relationship architecture can be replaced by a universal schema | *"never made so"* | RMS §15; RMS §4 |
| PI-33 | LS-3 implies one definition Record per edge | a type governs every relationship of it; lockstep is not instance pairing | §13.3; 064 Q7; SC-079-I |
| PI-34 | 079 creates 080's schema elements | the structure is 080's | row 080 |
| PI-35 | 079 implements World's relationship-type data | row 198's | row 198 |
| PI-36 | The Blueprint's ten-item Registry roster overrides RMS §10.1 | historical state | 064 §5; SC-079-B |
| PI-37 | The Blueprint's *capability* classification overrides Registry sovereignty | stale wording | RMS §10; SC-079-A |
| PI-38 | Every model-owned connection — reference, dependency, workflow transition, composition link — must be typed by a `RELATIONSHIP-TYPE-DEFINITION` | the family types what each model's architecture brings under it; its existence reclassifies nothing | RMS §15; §8.5 |
| PI-39 | Because every definition declares an owning role, every model that uses the family must hold Relationship Records | the declaration is mandatory; Relationship Records are not | I-102; §8.5 |
| PI-40 | A schema's need to represent cardinality authorizes deciding what it bounds, its values or its default | a representation choice is not a semantic decision | §9.3; SC-079-F |
| PI-41 | Field-occurrence cardinality and relationship-type cardinality are interchangeable | separate concerns | §9.3 |
| PI-42 | Because I-73 fixes what the owning role does where Relationship Records are used, the same effect applies within KNOWLEDGE-STATE, to Production's references or to Issue's placement | I-73 is scoped to Relationship Records; elsewhere the effect is open | I-73; §8.5; OD-079-2 |
| PI-43 | A carrier that gives cardinality a per-role shape, a default or a value set merely represents it | the shape presupposes what cardinality bounds | §9.3; §17 M; OD-079-1 |
| PI-44 | Record cardinality — how many Records of a Kind exist per key — is relationship-type cardinality | separate concerns | RMS §8.1; row 259; §9.3 |
| PI-45 | Every typed edge has an owning role, so no endpoint is ever ambiguous and nothing can be reified | the criterion and §13.9 use two senses of *own* | RMS §15; 044 §8; 055 §5.2; §10 |
| PI-46 | Whatever carrier 080 chooses for eligibility is a declaration reference and never a dependency | the classification is of this specification's statement; a carrier referring to a `KIND-DEFINITION` is an R → R reference, and its dependency status is 111's | 063 §8.1, §8.3; 062 D-9; RF-079-1 |
| PI-47 | Row 079's copied `Canon` and `CD` values make this file a Registry Record or license a canonical write | copied manifest values; the effective status is stated under the header | Roadmap §0.8, PART VII; 003; SC-079-J |
| PI-48 | OD-079-1 and OD-079-2 are Roadmap gates on 080 or on the type sets | open decisions, not `G` gates; no gate is invented | rows 079, 080 `G: —`; 003 |

## 19. Source-Condition Register

### 19.1 Open decisions

An open decision is a question this family depends on, that no current source answers, and that
this specification may not answer. Each entry states its owner, what it blocks and does not block,
and the condition that closes it. Neither is a Roadmap gate (§2). Neither is closed by a schema, a
type set, a validator or a revision of this document that assumes an answer.

#### OD-079-1 — what a relationship type's cardinality bounds — OPEN

| | |
|---|---|
| **Question** | What does a type's cardinality bound — per participant role, per participant, the relationship as a whole, or otherwise? What values does it admit? Is there a default? Is its meaning the same in every Record Model, or model-owned? |
| **Sources** | Blueprint §13.3 (the type carries *"its cardinality"*); Artifact 055 §6; no other inspected source states anything about it |
| **Established** | cardinality is type content of a §13.3 relationship, distinct from arity and from field-occurrence, Record, edge, definition and reference cardinality (§9.3) |
| **Owner** | the Blueprint/RMS author. No Roadmap row is assigned it (SC-079-T); the author may assign one. If the author rules that the meaning is model-owned, each model's relationship-architecture row (197, 276, 338, 356, 366) answers within that ruling. |
| **Blocks** | in 080: a value set, enumeration, default or notation presented as source semantics, or a carrier whose shape presupposes the answer (§9.3); in rows 198, 277, 338, 356, 366: a cardinality with a checkable meaning; in rows 112 and 116: validating one; in each model's mechanism: enforcing one on actual relationships |
| **Does not block** | row 079's `Val` and `Done`; row 080's `Val` and `Done`; the participant-role and owning-role obligations |
| **Closes when** | an authoritative source — a Blueprint or RMS text, or an author ruling recorded in the Roadmap as §0.7 and §0.8 are — states what cardinality bounds, its value set or the rule for one, whether there is a default, and whether the meaning is uniform or model-owned; and the answer is cited where this specification records the gap |

#### OD-079-2 — what the owning role governs outside Relationship Records — OPEN

| | |
|---|---|
| **Question** | Where a model holds no Relationship Records, what does a declared owning role select or govern? Which of that model's connections does this family type at all? |
| **Sources** | row 079 `Done`; Blueprint §13.6e; I-73 and I-90 (*"Wherever a Record Model uses Relationship Records"*); the §13.3 scoping note; RMS §15 rows E, P, V, I; rows 276, 277, 338, 356, 366 |
| **Established** | the declaration is a condition of definition validity for every Record of the family; its application wherever Relationship Records are used (§8.5 C); the obligation brings no connection under the family |
| **Owner** | each model's relationship architecture: row 276 for E, consumed by 277; 338 for P; 356 for V; 366 for I. If a model's architecture finds that a declared owning role can have no source-consistent effect in its mechanism, that is a source conflict for the Blueprint/RMS author, because it bears on row 079's `Done` and on §13.6e's assignment of an owning role to every type definition. |
| **Blocks** | for that model: type definitions whose owning role has a stated effect (277, 338, 356, 366); any check of that effect, in row 116 or a model validator; any Derived view built on it |
| **Does not block** | row 079's `Val` and `Done`; row 080 representing the declaration; World (197–199), where I-73 and §13.9 apply |
| **Closes when** | for each model separately, its architecture row answers §8.5's prerequisites for that model consistently with I-73 and I-102, and the answer is cited where this specification records the gap. Closure for one model closes nothing for another. |

### 19.2 Source conditions

Each entry gives the sources, the condition, what is established, what remains undecided, whether
this artifact owns its resolution, the owner where one is established, and whether it blocks row
079's `Val` or `Done`.

#### SC-079-A — Registry classification — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* RMS §10: *"COLLISION-1 — CLOSED"* — *"Registry is a sovereign Record Model"*; RMS Appendix H PC-1; Roadmap DG-01 |
| **Established** | Registry is a sovereign Record Model; this family defines Registry Record semantics, not a capability |
| **079 owns?** | no; no Blueprint edit is made |
| **Blocks?** | no |

#### SC-079-B — Registry Kind roster — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §13.6's ten-item roster, with `RELATIONSHIP-TYPE-DEF`; RMS §10.1 *"CLOSED at fourteen"*; 064 SC-064-A |
| **Established** | `RELATIONSHIP-TYPE-DEFINITION` is Kind 6; no fifteenth Kind |
| **079 owns?** | no |
| **Blocks?** | no |

#### SC-079-C — relationship principle against packaging — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §13.3 and its scoping note; RMS §15; I-102; Artifact 055 §4 |
| **Established** | the principle is *"available to every model"*; the Relationship Record, its ownership rule and its boundedness are World architecture; World's edge identity and history are World's |
| **079 owns?** | no |
| **Blocks?** | no |

#### SC-079-D — reification ambiguity — SOURCE GAP

| | |
|---|---|
| **Sources** | RMS §15 (frozen criterion); Artifact 055 §5.2: *"No governing source defines when ownership is ambiguous."* |
| **Established** | the criterion's *own* and §13.9's *own* are two senses, reconciled in §10; the residual wording is SC-079-S |
| **Undecided** | when ownership is ambiguous |
| **079 owns?** | no — each model's relationship architecture applies the criterion (rows 197, 276, 338, 356, 366) |
| **Blocks?** | no |

#### SC-079-E — participant-role arity and representation — SOURCE GAP

| | |
|---|---|
| **Sources** | Blueprint §13.9 *"An edge joins two objects."*; §13.3 *"each end"*; RMS §15 |
| **Established** | roles are declared and distinguishable; a World type has two participant positions |
| **Undecided** | arity for other models' types; how roles are named or represented |
| **079 owns?** | no — representation is 080's; other models' arity is their architecture's |
| **Blocks?** | no |

#### SC-079-F — direction and cardinality: meaning and representation — SOURCE GAP

| | |
|---|---|
| **Sources** | Blueprint §13.3 |
| **Established** | direction and cardinality are type semantics of a §13.3 relationship's type; cardinality is distinct from arity and from field-occurrence, Record, edge and definition cardinality (§9.3) |
| **Undecided** | cardinality's meaning — what it bounds, its value set, default and notation — is OD-079-1 (§19.1); carriers, tokens, defaults and notation for direction |
| **079 owns?** | no — OD-079-1's owner is the Blueprint/RMS author; representation is 080's, within §9.3's boundary. A representation choice does not resolve the semantic gap: any choice 080 makes beyond the sources is recorded as its own and not presented as source semantics |
| **Blocks?** | row 079's `Val` or `Done`: no — neither names cardinality, and the conceptual responsibility is stated (§9). Downstream: yes, as OD-079-1 states |

#### SC-079-G — participant eligibility and cross-model types — SOURCE GAP

| | |
|---|---|
| **Sources** | Blueprint §13.3 (*"which kinds may stand at each end"*); RMS §10.3; Artifact 058; RMS §7 |
| **Established** | declared Kinds of declared Models only; naming admits nothing; 058 and model constraints are not overridden |
| **Undecided** | any complete Model/Kind compatibility matrix; whether eligibility may be stated at Model level without a Kind; whether and how one type's roles may be occupied by Records of different models |
| **079 owns?** | no — cross-model edges are 058's; each model's types are its rows' |
| **Blocks?** | no |

#### SC-079-H — the owning role where no Relationship Record is used — SOURCE GAP

| | |
|---|---|
| **Sources** | row 079 `Done`; I-73 and I-90 (*"Wherever a Record Model uses Relationship Records"*); RMS §15 rows E, P, V, I; rows 276, 277, 338, 356, 366 |
| **Established** | the declaration is a condition of definition validity for every Record of the family; its application wherever Relationship Records are used, in any model (I-73); the obligation brings no model-owned connection under the family (§8.5) |
| **Undecided** | what a declared owning role governs inside a mechanism with no Relationship Record, and which of a model's connections, if any, this family types — together OD-079-2 (§19.1), with §8.5's per-model prerequisites; whether §13.3's direction, cardinality and legality apply to those models' typed connections |
| **079 owns?** | no — each model's relationship architecture (rows 276, 338, 356, 366), escalating to the Blueprint/RMS author as OD-079-2 states |
| **Blocks?** | row 079's `Val` or `Done`: no — the declaration does not wait on its application. Downstream: yes, as OD-079-2 states |

#### SC-079-I — `LS: LS-1` against `Why: LS-3 partner` — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 079 `LS: LS-1`, `Why: LS-3 partner`; Roadmap PART III: LS-1 *"every Kind spec ↔ its Registry KIND-DEFINITION"*, LS-3 *"Relationship ↔ Relationship-Type-Definition — including the owning-role declaration"*; Artifact 003: *"A lockstep partner is not a predecessor."* |
| **Condition** | the declared label and the role the row describes name different lockstep systems; a family specification is neither a Kind spec nor a `KIND-DEFINITION` |
| **Treatment** | both values preserved; no LS-1 pair (079 ↔ 080 or other) is invented; the family's role is described as LS-3's, as the row's `Why` says; LS-3 pairs a model's relationships with their type definitions and does not mean one Record per edge (cf. 072 SC-072-D; 076 SC-076-H). Route: ROADMAP ISSUE. |
| **079 owns?** | no — the Roadmap author's |
| **Blocks?** | no |

#### SC-079-J — `Canon` metadata on a docs path — RECORDED, NOT RESOLVED

| | |
|---|---|
| **Sources** | row 079 `T: doc · Canon: canonical-about-meaning · CD: yes`; Artifact 003: *"A specification in `docs/**` is `AUTHORITATIVE` about architecture and `Canon: n/a`"*; `CD` *"licenses nothing"*; Artifact 003's `Canon` vocabulary: *"Registry is `canonical-about-meaning` and never about the world"*; Roadmap §0.8 and PART VII; the Revolving Resolution Note, CONFLICT-F, records the same inconsistency for row 066 (SC-066-H) and for the rows AD-REG-AUTHORING-SPLIT moved under `docs/registry/` |
| **Condition** | the row gives this `docs/**` specification the `Canon` value Artifact 003 associates with Registry, while 003's general value for a `docs/**` specification is `Canon: n/a`. The Roadmap outranks Artifact 003, and neither says which value describes this file |
| **Treatment** | the values are copied exactly in the header and the §2 table and are not changed. Their effective status is stated once, under the header, and §2 and the footer repeat it: this file is an AUTHORITATIVE specification, not a Registry Record; it holds no canonical data and licenses no canonical write or write path. Reading `canonical-about-meaning` as naming the canonicality of the Records this family governs, rather than of this file, is a 079 reading, not a resolution. Route: ROADMAP / CONVENTION ISSUE. |
| **079 owns?** | no — the Roadmap author's |
| **Blocks?** | no |

#### SC-079-K — requirement text RR-16 — NON-BLOCKING, UNVERIFIED

| | |
|---|---|
| **Sources** | row 079 `Req: RR-16`; the Revolving Resolution Note, GAP-C (*"missing requirement register"*). A search of the repository at this revision found RR-16 only as a `Req` value in the Roadmap and in artifacts that carry or discuss that value; none defines it. The search shows what this repository contains, not that no definition exists elsewhere. |
| **Treatment** | the ID is carried exactly; no text is stated, and no compliance with RR-16 is claimed at any evidence level (§22) |
| **Blocks?** | no — GAP-C is recorded as non-blocking; that is a record of a build resolution, not a verification of RR-16 |

#### SC-079-L — layer placement — ESTABLISHED

| | |
|---|---|
| **Sources** | Artifact 062 §6: L1 stratum 1b, *"relationship type and participant-role semantics"*, depends on RFS, must not depend on L2–L5; downstream content *"relationship types 079–080"*; D-8, D-9 |
| **Established** | the family sits in L1 peer semantics; naming declared Kinds is a declaration reference, not an upward dependency (RF-079-7) |
| **Undecided** | concrete dependency direction, asymmetry and cycles between definitions |
| **079 owns?** | no — row 111 |
| **Blocks?** | no |

#### SC-079-M — WSV — RECORDED

| | |
|---|---|
| **Sources** | Blueprint §13.10, headed PROPOSED: *"WSV owns no edges"*; RMS Appendix H PC-2; Roadmap DG-02; RMS §7 (World, `SOURCE-ESTABLISHED`): *"WSV takes Record + WSV-H, no Relationship Record (indicators are keys, not objects — WSV is always the non-owning endpoint)"*; Artifact 055 §9.3 records the §13.10 reading as PROPOSED |
| **Condition** | the Blueprint statement remains flagged PROPOSED while RMS §7 states WSV's package and its non-owning position |
| **Treatment** | no WSV exception is a rule of this family, and no flag is lifted. How WSV's position bears on the owning roles of World's pressure-edge types is World's (rows 197–198). |
| **079 owns?** | no |
| **Blocks?** | no |

#### SC-079-N — the Blueprint examples are not a roster — RECORDED

| | |
|---|---|
| **Sources** | Blueprint §13.9's four examples; row 198 (*"each type declares its owning participant role; causal and pressure families named"*); RMS Appendix C: *"Relationship Catalog → Deliverable F"*, which is not in the source set |
| **Treatment** | the examples illustrate role-based ownership; they are not committed Registry data and not the World set |
| **Blocks?** | no |

#### SC-079-O — Roadmap unlocks against downstream `H` — ROADMAP ISSUE, RECORDED

| | |
|---|---|
| **Sources** | row 080 `→ 177,277,338,352,375`; rows 277 and 338 list 080 in `H`, rows 177, 352 and 375 do not; rows 198, 356 and 366 list 080 in `H` without appearing in 080's `→`; row 197 lists 079 in `H` while 079's `→` names 080 only |
| **Treatment** | an unlock is not a hard dependency, and neither is inferred from the other; no row is edited |
| **079 owns?** | no — the Roadmap author's |
| **Blocks?** | no |

#### SC-079-P — what references a RELATIONSHIP-TYPE-DEFINITION — SOURCE GAP

| | |
|---|---|
| **Sources** | 064 §13 Q7: *"not established — LS-3 pairs each relationship with its type definition (lockstep); runtime relationship ownership stays with the model"* |
| **Undecided** | how an actual relationship, or a model's Relationship Record, identifies its type |
| **079 owns?** | no — each model's relationship-record and type rows (e.g. 199) |
| **Blocks?** | no |

#### SC-079-Q — a World relationship whose endpoints stand in the same role — SOURCE GAP

| | |
|---|---|
| **Sources** | Blueprint §13.9: exactly one endpoint owns an edge; the rule *"requires no tie-breaking"* |
| **Established** | the owning role must pick out exactly one endpoint of each edge (§8.4) |
| **Undecided** | how World types a relationship that reads the same from both ends |
| **079 owns?** | no — World's type set and Relationship Record (rows 197–198) |
| **Blocks?** | no |

#### SC-079-R — older Blueprint reference wording — CLOSED BY SOURCE

| | |
|---|---|
| **Sources** | Blueprint §9.4 and §13.6e: *"a Registry definition may never reference a kind, a subtype, or an instance"*; RMS §10.3: *"v0.1 stated the boundary too bluntly"*; Artifact 063 |
| **Established** | declared Kinds may be named; domain instances may not |
| **079 owns?** | no |
| **Blocks?** | no |

#### SC-079-S — the two senses of *own* in the reification criterion — UPSTREAM FINDING, RECORDED

| | |
|---|---|
| **Sources** | RMS §15: *"reify only when no endpoint can own the edge without ambiguity"*, and its World row *"reified; Registry declares the owning role"*; Blueprint §13.9: *"Exactly one endpoint owns it"*; Artifact 044 §8; Artifact 055 §5.2 (*"Two uses of "own""*) |
| **Condition** | read with one sense of *own*, the criterion could never be met by a type with an owning role, and every type has one (§8.2); RMS §15's World row shows that is not meant |
| **Established** | the two-step reading of §10, which 044's wording, the order of RMS §15's World row and 055 §5.2 support; this specification follows it |
| **Undecided** | nothing about the architecture. The residual is wording: neither the RMS nor the Blueprint states the two senses in its own text |
| **Treatment** | no source is amended; the finding is for the Blueprint/RMS author, who may make the two senses explicit. Route: SOURCE WORDING, for the author |
| **079 owns?** | no |
| **Blocks?** | no |

#### SC-079-T — no row owns the meaning of relationship-type cardinality — ROADMAP ISSUE, RECORDED

| | |
|---|---|
| **Sources** | Blueprint §13.3; rows 079 and 080 (`Val` and `Done` name no cardinality); rows 198, 277, 338, 356, 366 (type sets); rows 112, 116 (validation) |
| **Condition** | the type carries cardinality, but no Roadmap row is assigned to decide what it means; the type-set rows that would state it all list 080 in `H`, and 080's own `Val` and `Done` do not reach it |
| **Treatment** | recorded as OD-079-1, with the Blueprint/RMS author as owner. No row is edited and none is assigned here. Route: ROADMAP ISSUE |
| **079 owns?** | no — the Roadmap author's |
| **Blocks?** | row 079: no. Downstream: as OD-079-1 states |

## 20. Conformance Conditions

Class: **STATIC** — checked by reading this document; **CROSS-SOURCE** — checked against the cited
sources; **REPOSITORY** — checked against the repository's actual changes.

The class says how a condition is to be checked. It does not record that the check has been made.
At this revision, C-079-01 and every quotation have been compared mechanically with the repository
copies of the sources; the REPOSITORY conditions were checked against the working tree for this
change and hold only of that change; every other condition has been checked by authoring review
only and awaits human review. No condition is at MECHANISM or DEMONSTRATED level (§2).

| ID | Condition | Class | Where |
|---|---|---|---|
| **C-079-01** | The header and the §2 table reproduce current Roadmap row 079 exactly, emphasis included. | CROSS-SOURCE | header; §2 |
| **C-079-02** | The only hard dependency is 064; 055, 060–063 and every other supporting artifact stay supporting. | CROSS-SOURCE | §4 |
| **C-079-03** | No soft dependency and no gate is introduced. | CROSS-SOURCE | §4; §22 |
| **C-079-04** | `RELATIONSHIP-TYPE-DEFINITION` remains Registry Kind 6 of fourteen. | CROSS-SOURCE | §5; RT-079-01 |
| **C-079-05** | The definition and a relationship instance remain separate. | CROSS-SOURCE | §6; RT-079-02, RT-079-16 |
| **C-079-06** | Participant roles are declared, not inferred. | CROSS-SOURCE | §7; RT-079-03 |
| **C-079-07** | Exactly one owning role is declared for every type. | CROSS-SOURCE | §8.2; RT-079-04, RT-079-25 |
| **C-079-08** | The owning role belongs to the type's declared roles. | STATIC | §8.2; RT-079-05 |
| **C-079-09** | The owning role is unambiguous. | CROSS-SOURCE | §8.2; RT-079-06 |
| **C-079-10** | Owner selection is independent of creation order, editing context, direction and role order. | CROSS-SOURCE | §8.2; RT-079-08 |
| **C-079-11** | Where Relationship Records apply, one edge has one authoritative owner. | CROSS-SOURCE | §8.4, §13; RT-079-07 |
| **C-079-12** | The non-owning World view is Derived. | CROSS-SOURCE | §13; RT-079-09 |
| **C-079-13** | The Registry never owns relationship instances by defining their type. | CROSS-SOURCE | §6; RT-079-10 |
| **C-079-14** | World's Relationship Record is not universal. | CROSS-SOURCE | §11; RT-079-11 |
| **C-079-15** | No model's relationship mechanism is silently overwritten. | CROSS-SOURCE | §11 |
| **C-079-16** | The reification criterion is distinct from the owning-role designation. | CROSS-SOURCE | §10; RT-079-12 |
| **C-079-17** | Direction is stated as a semantic concern, separate from the owning role. | CROSS-SOURCE | §9.2; RT-079-13 |
| **C-079-18** | Cardinality is stated as a semantic concern whose meaning is open as OD-079-1; no value set, notation, default or presupposing carrier shape is invented, and §9.3 states the boundary for 080. | CROSS-SOURCE | §9.3; §19.1; RT-079-14 |
| **C-079-19** | Participant eligibility is bounded by declarations and admits nothing. | CROSS-SOURCE | §9.4; RT-079-15; RF-079-1 |
| **C-079-20** | No universal role or arity grammar is invented. | STATIC | §7; RT-079-23 |
| **C-079-21** | The definition holds no actual endpoint instances. | CROSS-SOURCE | §6, §7; RT-079-16; RF-079-2 |
| **C-079-22** | The seven-field universal envelope is preserved. | CROSS-SOURCE | §14 RS-079-1 |
| **C-079-23** | Independent Registry identity is preserved and kept apart from edge and Relationship Record identity. | CROSS-SOURCE | §14 RS-079-1 to RS-079-3 |
| **C-079-24** | The definition remains versionable without mechanics being invented. | CROSS-SOURCE | §14 VS-079 |
| **C-079-25** | Every concrete reference obeys 063. | CROSS-SOURCE | §15 |
| **C-079-26** | Reference does not imply dependency. | CROSS-SOURCE | §15 RF-079-8 |
| **C-079-27** | No schema carrier is pre-built for 080. | STATIC | §15 RF-079-6; §21 |
| **C-079-28** | No concrete relationship-type Record is created. | REPOSITORY | §2; §17 |
| **C-079-29** | No runtime validator or resolver is created. | STATIC | §3; RT-079-22 |
| **C-079-30** | No Universal Relationship Record or History Record is introduced. | CROSS-SOURCE | §11; RT-079-23 |
| **C-079-31** | No Registry Kind is invented, for a role or anything else. | CROSS-SOURCE | §5, §7; RT-079-01 |
| **C-079-32** | `LS: LS-1` and `Why: LS-3 partner` are preserved without an invented pairing. | CROSS-SOURCE | SC-079-I |
| **C-079-33** | Source gaps are recorded, not resolved. | STATIC | §19 |
| **C-079-34** | The World examples remain illustrative. | STATIC | §17; SC-079-N |
| **C-079-35** | The direct handoff is exactly 080. | CROSS-SOURCE | §21 |
| **C-079-36** | No downstream `Val` or `Done` is enlarged. | CROSS-SOURCE | §21 |
| **C-079-37** | Row 079's `Val` is traced clause by clause at the evidence level each clause has reached; none is reported at MECHANISM or DEMONSTRATED. | STATIC | §14, §15; §22 |
| **C-079-38** | Row 079's `Done` is traced at its evidence level, with the owning role's application outside Relationship Records reported as open (OD-079-2). | STATIC | §7, §8; §22 |
| **C-079-39** | Only `docs/registry/relationship_type.md` is created by this artifact. | REPOSITORY | row 079 |
| **C-079-40** | No canonical data is written. | REPOSITORY | §2 |
| **C-079-41** | The owning role picks out exactly one endpoint of each edge, with no tie-breaker. | CROSS-SOURCE | §8.4; SC-079-Q |
| **C-079-42** | The family's L1 placement is respected: eligibility naming a declared Kind is not a semantic dependency. | CROSS-SOURCE | §15 RF-079-7; SC-079-L |
| **C-079-43** | Roadmap unlock and hard-dependency mismatches are recorded, not repaired. | CROSS-SOURCE | SC-079-O |
| **C-079-44** | The owning-role obligation is scoped to `RELATIONSHIP-TYPE-DEFINITION` Records: every such Record declares exactly one owning role, and the obligation neither reclassifies a model-owned connection nor requires every reference, dependency, composition link or workflow transition to be typed by this family. | CROSS-SOURCE | §8.5; RT-079-25; PI-38, PI-39; SC-079-H |
| **C-079-45** | Relationship-type cardinality stays distinct from participant-role arity, field-occurrence cardinality, edge count and definition count, and no cardinality interpretation, value set, notation, default or schema obligation the sources do not establish is imposed on Artifact 080. | CROSS-SOURCE | §9.3, §21; RT-079-14; PI-40, PI-41; SC-079-F |
| **C-079-46** | Row 079's copied `Canon` and `CD` values and this file's effective status are stated consistently in the note under the header, §2, SC-079-J and the footer; no section treats this file as a Registry Record or as licensing a canonical write. | CROSS-SOURCE | header; §2; SC-079-J; footer; PI-47 |
| **C-079-47** | OD-079-1 and OD-079-2 each state an owner, what they block and do not block, and a closing condition; neither is presented as a Roadmap gate or as resolved. | STATIC | §2; §19.1; PI-48 |
| **C-079-48** | Definition validity stays apart from application: the owning-role declaration is a condition of validity for every definition; its application is stated only where Relationship Records are used; the per-model prerequisites are questions, not answers. | CROSS-SOURCE | §5.3; §8.5; RT-079-25; PI-42 |
| **C-079-49** | The reification criterion and Blueprint §13.9 are reconciled through two senses of *own*, and the residual wording is registered for the source author, not amended. | CROSS-SOURCE | §10; RT-079-12; SC-079-S; PI-45 |
| **C-079-50** | Classifying eligibility as a declaration reference, and as no dependency by itself, is qualified as a statement about this specification's wording, not about a carrier 080 may define. | CROSS-SOURCE | §9.4; §12; §15 RF-079-1, RF-079-7; RT-079-18; PI-46 |
| **C-079-51** | Evidence levels are never merged: nothing is reported at MECHANISM or DEMONSTRATED, and SOURCE-CHECKED is claimed only for what was compared. | STATIC | §2; §20; §22 |

## 21. Downstream Handoff

**To 080** (`RELATIONSHIP-TYPE-DEFINITION` schema, `docs/registry/relationship_type.schema`; `H:
079`; `Val`: *"definition resolves; versionable; references only declared entities (063)"*;
`Done`: *"schema"*; `Why`: *"LS-3"*). 080 may take from this specification, without redesign:

1. **Meaning.** A `RELATIONSHIP-TYPE-DEFINITION` is an R Record governing one relationship type
   (§5; RT-079-01, RT-079-02).
2. **Participant roles.** Declared and distinguishable within the type (§7; RT-079-03).
3. **Owning role.** Exactly one, one of the declared roles, stated not inferred, for every type —
   a condition of definition validity, not an instruction to reclassify any model's connections.
   Its application is source-established where Relationship Records are used and open elsewhere
   (OD-079-2); 080 represents the declaration and does not encode an application (§8, §8.5;
   RT-079-04, RT-079-05, RT-079-25).
4. **Type semantics.** Direction, cardinality and per-role eligibility as §13.3 attaches them, and
   only that far (§9); cardinality within §9.3's boundary while OD-079-1 is open.
5. **Definition, not instance.** No endpoint, edge, validity, provenance or history in the Record
   (§6; RT-079-16).
6. **Declared participant categories.** Only declared Kinds of declared Models (§15 RF-079-1,
   RF-079-7). This specification states eligibility as naming the Kind itself; if 080 instead
   carries it by referring to a `KIND-DEFINITION` or `MODEL-DEFINITION` Record, 080 records that the
   carrier is an R → R reference and leaves its dependency status to row 111.
7. **Reference legality.** RF-079-1 to RF-079-9.
8. **Resolution and versionability.** Ordinary R Record identity; nothing that obstructs 108–110
   (§14).
9. **No runtime ownership.** No element claims an edge, a Relationship Record or execution (§13;
   RT-079-10, RT-079-22).

**080 is not asked** to fix anything this specification leaves open, and this specification decides
none of 080's choices: no schema grammar, element names, role-list representation, owning-role
syntax, direction tokens, cardinality notation, defaults, reference-carrier structure, version
fields, parser logic, validator interface, storage or materialized values. Where 080 must make a
representation choice the sources do not settle, it records it as its own. 080's `Val` and `Done`
are not enlarged.

**Cardinality, specifically.** 080 inherits the source fact that cardinality is a relationship-type
semantic concern within §13.3's scope. It does not inherit an interpretation of what cardinality
bounds, a permitted-value enumeration, a default or a notation, because none is established
(OD-079-1; SC-079-F). §9.3 states what 080 may and may not do while OD-079-1 is open. A carrier
cannot itself settle what it carries, so 080 does not choose a shape, value set or default merely
to complete the schema; it keeps any representation choice distinct from a source-established
rule, records it as its own, and leaves the semantic requirement explicit.

**Open decisions 080 inherits.** 080 can meet its own `Val` and `Done` with OD-079-1 and OD-079-2
open, and it cannot close either: OD-079-1 belongs to the Blueprint/RMS author and OD-079-2 to each
model's relationship architecture (§19.1). Neither is a gate on 080.

**080 does not assume** that every model connection is a relationship instance or needs a type
definition, that every model uses Relationship Records, that the owning role's effect outside
Relationship Records is known, that the owning role is the first participant or follows direction,
universal binary arity, one multiplicity model or fixed cardinality values or defaults, that
relationship-type cardinality is field-occurrence or Record cardinality, that a carrier it chooses
inherits this specification's classification of eligibility as a declaration reference, or that a
definition creates or owns an edge (PI-09, PI-11, PI-14, PI-15, PI-23, PI-38 to PI-46; §15).

**Unlock is not dependency.** Row 079's `→` names 080 only. Row 197 lists 079 in its own `H` and
consumes it through that `H`. Row 080's `→` and the `H` of the rows downstream of it do not match
(SC-079-O); neither is inferred from the other.

**Other downstream rows, preserved and not implemented:**

| Row | Keeps | `Val` |
|---|---|---|
| 197 | World Relationship Record specification (`H: 055,079`) | *"World-only; reification criterion satisfied; owning role from Registry"* |
| 198 | World relationship type definitions (`H: 197,080`) | *"each type declares its owning participant role; causal and pressure families named"* |
| 199 | World Relationship Record schema | *"current relationships only; history lives in the History Record"* |
| 224 | back-reference and graph projection | *"back-references derived, never stored on the record"* |
| 276; 277 | E relationship architecture; E type definitions | *"no Relationship Record"*; *"evidence-for, contradicts, supersedes"* |
| 338 | P relationship architecture and type definitions | *"references"* |
| 356 | V relationship architecture and type definitions | *"represents"* |
| 366 | I composition architecture and field/relationship definitions | its own row |
| 108–110; 111; 112; 114; 115; 116; 117; 123; 124; 152 | evolution and versioning; dependency direction; reference validator; kernel; resolution; validation suite; identity binding; lockstep tests; P3 conformance; the sole canonical writer | their own rows |

## 22. Roadmap Completion Trace

Each item is reported at the evidence level it has reached (§2), and what it has not reached is
stated beside it. MECHANISM and DEMONSTRATED are reached by no item: neither 080 nor any of rows
108–124 exists in the repository at this revision.

| Row 079 | Reached | Not reached | Where |
|---|---|---|---|
| `Val`: *"definition resolves"* | **SPECIFIED** — independent R Record identity under the universal grammar and envelope, kept apart from type names, edges and Relationship Records; resolvable ≠ legal. **SOURCE-CHECKED** — the RMS §4 and §5 statements it rests on | MECHANISM: structure (080), create/resolve/version (114), consumer resolution (115), identity binding (117). DEMONSTRATED: 116, 123, 124. No definition Record exists to resolve | §14 RS-079 |
| `Val`: *"versionable"* | **SPECIFIED** — Registry-owned evolution under 108–110; not defined ≠ forbidden; version history is not edge history. **SOURCE-CHECKED** — 064 F-4 and row 108 | MECHANISM: 108–110. DEMONSTRATED: none scheduled before 116, 123, 124 | §14 VS-079 |
| `Val`: *"references only declared entities (063)"* | **SPECIFIED** — for the relation this specification states: eligibility names declared Kinds of declared Models; no domain instance, state or runtime target; reference ≠ dependency. **SOURCE-CHECKED** — RMS §10.3 and Artifact 063 | MECHANISM: the carrier (080) and the reference validator (112). DEMONSTRATED: 112's negative test, 116. A carrier 080 defines is classified by 080, not here (RF-079-1, RF-079-7) | §15 RF-079 |
| `Done`: *"participant roles **and owning role** declared"* | **SPECIFIED** — the obligation that every definition declare its participant roles and exactly one owning role among them, stated not inferred; its application where Relationship Records are used. **SOURCE-CHECKED** — §13.9, §13.6e, I-73 and LS-3 | MECHANISM: 080's representation; no definition declaring roles exists until the type sets (198, 277, 338, 356, 366). The application outside Relationship Records is open (OD-079-2). Whether SPECIFIED is the level row 079's `Done` requires is for human review | §7, §8; RT-079-03 to RT-079-09, RT-079-25 |
| `Why`: *"LS-3 partner"* | **SPECIFIED** — the family is described as the Registry side of LS-3, *"including the owning-role declaration"* | DEMONSTRATED: no LS-3 pair exists; lockstep tests are row 123's | §8.1; SC-079-I |
| `H: 064` | **PRESENT** — Artifact 064 exists at its Roadmap path; §5.1's quotations of it are SOURCE-CHECKED | its review or approval status is a human record, not established by this document | §5.1 |
| `S: —` | **PRESERVED** | — | §4 |
| `LS: LS-1` | **PRESERVED** — label kept; no pair invented; tension recorded | resolution is the Roadmap author's | SC-079-I |
| `G: —` | **PRESERVED** — no gate introduced; OD-079-1 and OD-079-2 are open decisions, not gates | — | §2; §19.1 |
| `→ 080` | **SPECIFIED** — the handoff is stated; 080's `Val` and `Done` are unchanged | 080 does not exist yet | §21 |
| `Req: RR-16` | **CARRIED** — the ID only; text unavailable (GAP-C) | no compliance claimed at any level | SC-079-K |
| open decisions | **RECORDED** — OD-079-1 and OD-079-2, each with owner, scope and closing condition | both OPEN | §19.1 |

Whether SPECIFIED and SOURCE-CHECKED are sufficient for row 079 to proceed is a human review
decision; this document does not make it. No relationship type, relationship, Relationship Record,
schema, validator or Registry Record is created.

---

*Artifact 079 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining. Row 079's `Canon` and `CD`
values are copied in the header and do not make this file a Registry Record (SC-079-J). A Registry
definition-family specification under `docs/**`: it holds no canonical data and licenses no
canonical write, creates no `RELATIONSHIP-TYPE-DEFINITION` Record and no relationship type, defines
no structural schema, and implements nothing. Where it differs from the Master Blueprint, the
Record Model System, the OS File Build Roadmap, or Artifact 064, those sources are correct and this
document is wrong.*
