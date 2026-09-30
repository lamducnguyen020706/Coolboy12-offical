# COOLBOY12 — Registry Authority Boundary

**Artifact 061** · Registry authority boundary · `docs/models/registry/authority.md` · Own: R ·
RM: R · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P3/3a · Req: RR-15 · BP: §9.4 · RMS: §10 · H: 060 · S: 051 · LS: — · G: — · → 062 ·
Val: *Registry governs definitions; each model owns its Records* · Done: boundary table ·
Why: stops Registry becoming a super-model · Risk: CRITICAL · ∥: no

## 1. Purpose

This contract answers one question — **what authority does Registry hold because it owns
definitions, and exactly where does that authority stop, before it becomes semantic ownership of
another Record Model's Records?**

Registry owns the `KIND-DEFINITION` that defines `CHARACTER`. World owns which Character Records
exist, what they mean in World's domain, and the values they carry. Registry's authority over
`CHARACTER` as a definition never reaches `W-CH-<ordinal>-Maximus`, or any other World Record.
Row 061 names the reason this contract exists: it *"stops Registry becoming a super-model"*.

Artifact 060 established what Registry is. This contract makes one of 060's statements —
*Registry governs definitions; each model owns its Records* (060 §7) — binding and tabular. It adds
no architecture: every rule below restates Blueprint §9.4, §13.6e, §13.7a, §13.7c and §13.9a,
RMS §4–§6.1, §10, §15, §17, §19, §20, §24 and §30, and the invariants cited.

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE **about the Registry authority boundary**, and about nothing else.
It derives that boundary from the Master Blueprint and the Record Model System and does not amend,
supersede, or outrank either. Where it differs from the Master Blueprint, the Record Model System,
or the OS File Build Roadmap, **those sources are right and this document is wrong.**

An authoritative architecture contract, a Registry Record, and canonical Registry data are three
different things. This file is the first. It is not a Registry Record, holds no Registry data, and
is `Canon: n/a`. `Auth: governing` binds how later artifacts treat this boundary; it confers no
power to commit anything (Artifact 051 §2).

`Req: RR-15` is reproduced from row 061. The requirement register is not in the supplied source
set; the ID is carried forward unverified and no requirement text is stated for it (GAP-C).

It specializes the authority framework of **Artifact 051** (`S: 051`) to the Registry domain. It
does not restate that framework, and nothing here overrides it.

## 3. Scope

**In scope.** What *Registry authority* refers to; where it stops at every definition subject the
sources name; the six-model ownership boundary; the consequences for references, World Truth and
the other models' semantics; the separation of Registry authority from Record ownership, the
constitutional Authority, canonicality, change governance, source-of-truth class, provenance,
storage, shared mechanism and software permission.

**Out of scope, by owner.** The five semantic layers (062); the reference boundary and its matrix
(063); the Registry Kind taxonomy (064); who may propose, approve or deprecate a definition (065);
the definition families (066–107); evolution, versioning, supersession and deprecation (108–110);
dependency direction (111); the reference validator and constraint binder (112, 113); the Registry
implementation (114–117); canonicality mechanics (052, and Registry's own later artifacts). No
schema, field, Registry data, code, permission model or test is created.

## 4. Governing Rule

> **Registry governs the definitions. Each Record Model owns its Records.** (Blueprint §13.6e)

I-105 states it as an invariant: Registry *"holds semantic authority over definitions and never
semantic ownership of another model's Records."* Blueprint §13.6e draws the consequence:
*"Therefore: semantic **authority** over definitions is not semantic **ownership** of domain
Records."*

```
Registry authority                      Record Model ownership
        ↓                                       ↓
definitions — what a thing means        Records — which exist, what they carry,
                                        what they mean in the model's domain

✗  Registry defines X   →   Registry owns every Record that uses X
```

This sentence controls the whole document. No rule below weakens it, and any reading of a rule
below that would weaken it is the wrong reading.

**What "Registry authority" means here.** Registry authority is **semantic authority over Registry
definitions**, scoped to the Registry domain (RMS §17: *"All authority is domain-scoped."*). It
covers:

- what a definition means, and which semantic contract it expresses;
- the meaning that consumers resolve against when they use a definition;
- Registry's own Records and Registry-domain semantics (§13.6e: *"Registry-domain semantics and its
  own Records"*).

It does not cover, for any other model: its domain instances, its domain truth, its lifecycle, its
canonicality, its temporal mechanism, its package composition, its provenance meaning, or its
semantic validation (§13.6e; I-105; RMS §6).

**Both halves hold.** Registry is not a model that only defines things for others. It is a
sovereign Record Model with real R-partition Records, and it owns those (060 §3, §5). It owns only
those.

## 5. Authority Terms Kept Apart

Artifact 051 §4 keeps the general terms apart. For Registry, four questions are routinely run
together, and each has a different answer:

| Question | Concept | Answered by | Source |
|---|---|---|---|
| What does this definition mean? | **Registry semantic authority** | Registry | Blueprint §13.6e; I-105 |
| Which Record Model owns this Record? | **Record ownership** | the Record's partition and its sovereign model — never the model whose definition it uses | I-16; I-101; Artifact 045 |
| Is this Record canonical, and what does canonical mean in its model? | **canonicality** | the owning model; for Registry, *"Yes, **about meaning**"* | Blueprint §13.7c; I-104; Artifact 052 |
| Who may propose, approve, deprecate or otherwise change a definition? | **change authority / governance** | Artifact 065 | Roadmap row 065 |

**Registry authority is not the Authority.** Artifact 051 writes **Authority** for the one
constitutional commit position — *"a position, not a person"*, *"always held by a human"*
(Blueprint §10.1) — and **authority** for domain-scoped authority. Registry holds the second kind
only. Registry is not a human position, a Registry Record does not hold the Authority, and no
Registry definition commits canon (Spine law 3; I-03). This contract creates no *Registry
Authority*, no definition-owner position, and no authority hierarchy (051 §7).

Three further separations, each already fixed by 051 and restated only for Registry:

- **Source-of-truth class is not authority.** A Registry definition classed `AUTHORITATIVE` is
  where a meaning lives (§29.6a). That class gives Registry no authority outside its domain
  (051 §9; Artifact 050).
- **Provenance is not authority.** A Registry Record's provenance records who, when and why. It
  does not establish what Registry has authority over (051 §16; Artifact 048).
- **Software permission is not authority.** Authority here is semantic and architectural: not a
  role, an access-control list, an account, a file permission or a service permission. A runtime
  role is not the constitutional Authority, and a write permission on a Registry store is not
  semantic authority (051 §15; Blueprint §12.6).

## 6. Definition Authority vs Record Ownership

RMS §6.1 gives the test that separates them:

| Category | Definition | Test |
|---|---|---|
| **Definition** | *"A Registry Record specifying meaning"* | *"Governs; never instantiates"* |
| **Record** | *"A persistent, identity-bearing unit owned by exactly one Record Model"* | *"Has independent identity, lifecycle, and authority"* |

A definition **governs**: it fixes the meaning a Record resolves against. It **never instantiates**:
it does not become, contain or hold the Records that use it. Blueprint §9.4: *"The Registry holds no
instances. It defines what a `LINEAGE` is; it never holds a lineage. A registry entry that names a
specific thing in the world is a misfiled Record."*

**The apparent tension, explained.** Registry governs semantic definitions that the system resolves
against, and each model owns its own Record semantics (RMS §6). These do not conflict, because they
are different questions. Registry owns *what `CHARACTER` means as a governed definition*; World owns
*which Characters exist and what is true of them*. §13.6e: *"Registry defines what a `CHARACTER` is;
it never holds a character, and it never adjudicates what is true of one (§9.4, I-88)."* Registry
does not define all semantics; it owns *"Registry-domain semantics and the definition layer the
wider system resolves against — and nothing else"* (§13.6e).

**Owning a definition is not admitting a Kind.** Which Kinds a model has is that model's taxonomy
(RMS §6; I-106). Artifact 057 §9 records that the sources give Registry the definition of a kind and
do not give it authority to admit another model's Kind. This contract assigns no admission
authority either.

## 7. Normative Boundary Table

This is the boundary row 061's `Done` requires. Rows 1–6 carry Blueprint §13.6e's own table; rows
7–12 apply the same rule to the definition subjects RMS §10 and Blueprint §13.9a name. Each row is
binding in both directions: Registry holds its column, and never the column beside it.

| # | Definition subject | Registry governs | The owning Record Model governs | Registry never infers | Source |
|---|---|---|---|---|---|
| 1 | **Kind** | the definition of a kind (`KIND-DEFINITION`) | which Records of that kind exist, and what they mean in its domain; its own Kind taxonomy | ownership of the Kind's instances; the model's roster; admission of the Kind | §13.6e; RMS §6; I-106; 057 §9 |
| 2 | **Field** | the definition of a field (`FIELD-DEFINITION`) | the values its Records carry | ownership of any value carried under that field | §13.6e |
| 3 | **Relationship type** | the definition of a relationship type and its owning role (`RELATIONSHIP-TYPE-DEFINITION`) | whether it uses Relationship Records at all; its relationship mechanism; the edges its Records actually hold | ownership of any edge or relationship instance; runtime relationship ownership | §13.6e; §13.9; RMS §15 |
| 4 | **Validation rule** | the definition of a validation rule (`VALIDATION-RULE`) and of a constraint (`CONSTRAINT-DEFINITION`) | its own semantic validation beyond structure | that Registry validates every model, executes validation, or owns any model's semantic validation | §13.6e; RMS §10.6, §20 |
| 5 | **Indicator** | what an indicator means — type, unit, range, constraints, semantics (`WSVR-INDICATOR-DEFINITION`) | the indicator's current value (World, in WSV) | any World-state authority | §13.6e; RMS §10.7 |
| 6 | **Registry domain** | Registry-domain semantics and its own Records | its own lifecycle, authority, canonicality and temporal architecture | any of those four for another model | §13.6e; RMS §6 |
| 7 | **Model** | a `MODEL-DEFINITION` Record: governed meaning about a declared Record Model | its sovereignty, which is constitutional and is neither granted nor held by a Registry Record | creation, abolition or ownership of a Record Model; a seventh model; a partition reassignment | RMS §2, §10.1; I-101; Artifact 039 §4 |
| 8 | **Schema** | the definition of a schema (`SCHEMA-DEFINITION`) | the Records that conform to it | ownership of conforming Records; execution of the schema | RMS §10.2 |
| 9 | **Controlled vocabulary** | the vocabulary definition (`CONTROLLED-VOCABULARY`), which may diverge per kind | which value its Records carry | ownership of the consuming Record; a forced union across kinds | §9.4; §13.6e; §13.7c; row 081 |
| 10 | **Capability** | the capability's semantic contract (`CAPABILITY-DEFINITION`) | — (the implementation is runtime, and not a Record) | runtime control; executing the capability; modelhood for it | RMS §10.5, §19 |
| 11 | **Behaviour of an indicator** | what a simulation model is and how an indicator behaves (`SIMULATION-MODEL-DEFINITION`) | the current values (World) | ownership of simulation state or of World values | §13.6e; RMS §10.7, §25 |
| 12 | **Identity grammar** | the authoritative kind-code mapping and the recorded grammar (`IDENTITY-GRAMMAR`) | its identity semantics: Kind meaning, identity-specific constraints | ownership of any Record's identity; re-deciding AD-1 | §13.9a; RMS §5; row 083 |

**The column the table does not have.** No row gives Registry ownership of a Record in partition
W, E, P, V or I. There is no such row, and adding one would be an amendment of I-105, not an
application of this contract.

## 8. Six-Model Ownership Boundary

| Model | Registry may govern | The model remains the owner of, and the authority for |
|---|---|---|
| **W** World | definitions World Records resolve against | World Records; World Truth (*"Registry owns meaning, not World Truth"*, §13.6) |
| **E** Epistemic | definitions of epistemic terms and vocabularies | Epistemic Records and states (RMS §24: *"R defines the terms; E owns the states"*) |
| **P** Production | definitions of production terms | Production Records: intent, plans, workflow, production reality |
| **R** Registry | Registry definitions | Registry Records — and no other model's |
| **V** Visual | definitions of visual vocabularies, subtypes and contracts, where the sources establish them | Visual Records and Visual semantics |
| **I** Issue | definitions of publication terms | Issue Records: what was published and how it is composed |

The table states the boundary only. It establishes no model's authority ceremony, and no model's
own authority semantics, which remain that model's (051 §7, §14).

## 9. Authority by Definition Family — Worked Examples

Identifiers are schematic. Registry kind codes are Registry content not minted here (Blueprint
§13.9a; Artifact 046 §12), and no ordinal is allocated.

**A — Kind.**

```
R-<kind>-<ordinal>-<slug>     KIND-DEFINITION for CHARACTER     Registry owns this Record
W-CH-<ordinal>-Maximus        a Character                       World owns this Record
```

Registry decides the governed definition of `CHARACTER`. World decides which Character Records
exist, what is true of them, their World lifecycle, their World relationships and their World
temporal account.

**B — Indicator.** `WSVR-INDICATOR-DEFINITION` says what an indicator means; WSV holds its current
value. RMS §10.7: *"World owns current values. Registry owns meaning."* Definition authority is not
value authority.

**C — Relationship type.** A `RELATIONSHIP-TYPE-DEFINITION` defines the type, its participant roles
and its owning role: *"The relationship **type definition** in the Registry declares which
participant role owns the edge"* (§13.9). The edge itself is held by the owning model under its own
architecture — in World, in the owning endpoint's Relationship Record. RMS §15 gives Registry
*"Relationship **definitions**; never runtime relationship ownership"*. No universal Relationship
Record is implied, and Registry holds no cross-model edges.

**D — Validation.** Three layers, kept apart:

```
VALIDATION-RULE              Registry Record — defines a checking mechanism
validator implementation     runtime — performs the check; not a Record
semantic validity            the owning model — whether its own Record is meaningful
```

RMS §10.6: *"Registry owns definitions for both; runtime validators implement validation."* §13.6e
leaves each model *"Its own semantic validation beyond structure"*. Structural validation is a
shared mechanism (RMS §4) and is nobody's semantic authority.

**E — Model definition.** A `MODEL-DEFINITION` Record for World does not mean Registry created
World. World's sovereignty is constitutional (RMS §2; I-101). Registry records governed meaning
about the declared model and holds no constitutional ownership of it (060 §7).

## 10. Authority Does Not Transfer Through Reference

Every Record carries `registry_ref` (RMS §4). A Record's reference to a Registry definition:

- **transfers no ownership.** The Record stays in its partition and with its model: *"a reference
  DOES NOT TRANSFER OWNERSHIP"* (Artifact 045 §9); the field *"makes the Registry no owner of the
  Record that carries it"* (Artifact 058 §11). Referencing a definition does not convert a W, E, P,
  V or I Record into an R Record.
- **grants Registry no domain authority** over the referring Record, its values, its lifecycle or
  its truth.

**No domain instance is Registry's semantic authority.** RMS §10.3: Registry *"MAY NOT … use domain
instances as semantic authority."* A definition's meaning is not established by treating a
particular W, E, P, V or I Record as its authority. One Character Record cannot become the authority
for what `CHARACTER` means; the definition stays Registry-governed.

These are the authority consequences only. What Registry may and may not reference, the reference
matrix and its enforcement are **063**, **111** and **112**.

## 11. Registry vs World Truth

Blueprint §13.6: *"Registry owns meaning, not World Truth"*. RMS §24: *"Registry is canon about
meaning only; it can never override World Truth"*. I-88: *"A registry definition never asserts a
fact about the world, and no world record is resolved by reading one as though it were."*

Registry may define what `CHARACTER` means. It cannot declare that Maximus died in a given year and
thereby make it World Truth. That belongs to World, through the one path (Spine law 2).

## 12. Registry vs Other Model Semantics

- **Epistemic.** Registry may define an epistemic term or vocabulary. It does not own who knows,
  believes or has been shown what, or what has been revealed: those are E Records (RMS §24).
- **Production.** Registry may define production terms. It does not own plans, intent, workflow
  state or production reality. P consuming a definition does not make it Production authority.
- **Visual.** Registry may define visual vocabularies, subtypes and semantic contracts where the
  sources establish them — for example the VISUAL-ASSET subtype vocabulary (RMS Appendix H, PC-4).
  It does not own Visual Records or Visual semantics. The W → V source conflict is Artifact 058's
  and is outside this contract.
- **Issue.** Registry may define publication terms. It does not own what was published, issue
  composition, or Issue Records.

**Shared mechanism is not Registry authority** (I-103: *"Shared infrastructure never confers shared
meaning"*). The identity resolver, shared validation infrastructure, the Mutation Coordinator and
indexing do not become Registry-owned because Registry defines terms they use, and Registry defining
their semantic contracts does not make it their executor (RMS §10.5, §19).

**Storage location is not authority.** Registry authority follows the constitutional and model
boundaries, not physical placement: a path under `canon/registry/`, a document under `docs/`, a
table or a filesystem owner confers none (051 §15; Blueprint §26.2a).

## 13. Authority vs Canonicality

Registry is canonical *"about meaning"*: *"This definition is the authoritative meaning records
resolve against"*, with authority *"Registry change (§9.4)"* (Blueprint §13.7c; Artifact 052 §5.4).
That is Registry's canonicality, and it is stated here only to keep it apart from authority:

```
Registry semantic authority over a definition   ⇏   the definition's canonicality mechanism
Registry canonical about meaning                 ⇏   Registry owns World Truth
Registry canonicality                            ⇏   canonicality for any other model
```

No canonical status vocabulary, gate, field, transition or lifecycle is defined here, and no
universal canonical flag is introduced (052; RMS §4).

## 14. Authority vs Governance and Change

This contract states **what** Registry has authority over. **Artifact 065** states **how**
Registry definitions are governed: row 065's `Val` is *"who may propose, approve, deprecate a
definition"*. Authority over meaning does not itself define the ceremony by which meaning changes.
No approver role, ceremony, change state or deprecation approval is defined here.

Definition evolution and Record evolution are distinct. A definition's lifecycle is not the
lifecycle of the Records that use it; versioning, supersession and deprecation of definitions are
**108–110**.

**Source gap recorded.** RMS §21 places Registry governance in *"Appendix F / Deliverable I"*, and
RMS §17 places the authority matrix in *"Appendix E and Deliverable H"*. Neither deliverable is in
this repository (051 §7 records the second). Neither is reconstructed here: this contract's table is
the Registry boundary row 061 asks for, not Deliverable H.

## 15. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | Registry defines a Kind → Registry owns that Kind's instances | the model owns which Records of the kind exist | §13.6e |
| 2 | Registry defines a field → Registry owns the values in it | the model owns the values its Records carry | §13.6e |
| 3 | Registry defines a relationship type → Registry owns the edges | relationship definitions only; never runtime relationship ownership | RMS §15; §13.6e |
| 4 | Registry defines a validation rule → Registry owns model validation | each model owns semantic validation beyond structure | §13.6e; RMS §10.6 |
| 5 | Registry defines an indicator → Registry owns its current value | World owns current values | RMS §10.7 |
| 6 | Registry defines a model → Registry owns that Record Model | sovereignty is constitutional | RMS §2; I-101 |
| 7 | A Record references Registry → Registry owns that Record | a reference transfers no ownership | I-105; Artifact 045 §9 |
| 8 | Registry is canonical about meaning → Registry owns World Truth | canon about meaning only | RMS §24; §13.6; I-88 |
| 9 | Registry governance → universal semantic authority | all authority is domain-scoped | RMS §17; I-105 |
| 10 | Shared Registry definitions → models inherit from Registry | no model is a superclass of another | RMS §2; I-101 |
| 11 | Registry's `AUTHORITATIVE` class → Registry controls everything | a source-of-truth class is not authority | §29.6a; 051 §9 |
| 12 | Registry stores, indexes or resolves it → Registry owns it | shared mechanism confers no meaning; storage confers no authority | I-103; §9.4 |
| 13 | A domain instance → Registry's semantic authority | Registry may not use domain instances as semantic authority | RMS §10.3 |
| 14 | Registry semantic authority → the constitutional Authority | one human position commits canon | Spine law 3; §10.1; I-03 |

**Valid direction.** A Registry definition governs meaning; a consumer resolves against that
meaning; the consuming Record stays owned by its partition's model; Registry's canonicality stays
about meaning; each model's authority stays within its own semantic domain.

## 16. Downstream Ownership

| Artifact | Owns | 061 supplies |
|---|---|---|
| **062** | the five semantic layers and the downward-only rule | a settled authority scope: 062 organizes Registry semantics and need not decide whether Registry owns other models' Records |
| **063** | the Registry reference boundary | the authority consequences of reference (§10) |
| **064** | the fourteen Registry Kinds | the boundary each Kind's definition authority stays within |
| **065** | governance: who may propose, approve, deprecate | the scope of what is governed |
| **108–110** | definition evolution, versioning, supersession, deprecation | that definition evolution is not Record evolution |
| **111–113** | dependency direction; reference validator; constraint/validation binder | nothing executable |
| **114–117** | the Registry implementation | the boundary it must not cross |

None is pre-implemented. The Blueprint's older downward-only wording versus RMS §10.3 (060 §10,
058 §11) is not resolved here.

## 17. Conformance Conditions

Contract conditions, checkable against this document and against constructions built on it. They
are not invariants and mint no invariant number.

| ID | Condition | Source |
|---|---|---|
| **C-061-01** | Registry semantic authority is limited to definitions and Registry's own Records. | §13.6e; I-105 |
| **C-061-02** | Each Record Model retains ownership of its Records. | §13.6e; I-16; I-101 |
| **C-061-03** | Owning a definition never transfers ownership of an instance. | RMS §6.1; I-105 |
| **C-061-04** | Kind-definition authority confers no authority over the Kind's instances, roster or admission. | §13.6e; I-106; 057 §9 |
| **C-061-05** | Field-definition authority confers no authority over Record values. | §13.6e |
| **C-061-06** | Relationship-type definition authority confers no runtime relationship ownership. | RMS §15; §13.6e |
| **C-061-07** | Validation-rule definition authority does not replace model-owned semantic validation. | §13.6e; RMS §10.6 |
| **C-061-08** | Indicator-definition authority confers no authority over World indicator values. | RMS §10.7 |
| **C-061-09** | A `MODEL-DEFINITION` confers no constitutional ownership of a Record Model. | RMS §2; I-101 |
| **C-061-10** | A reference to Registry never transfers ownership to Registry. | I-105; 045 §9; 058 §11 |
| **C-061-11** | No domain instance becomes semantic authority for a Registry definition. | RMS §10.3 |
| **C-061-12** | Registry authority never overrides World Truth. | RMS §24; §13.6; I-88 |
| **C-061-13** | Registry authority becomes no other model's canonicality, lifecycle, package, temporal or provenance authority. | §13.6e; I-104; I-107 |
| **C-061-14** | Registry authority is distinct from the constitutional Authority. | Spine law 3; §10.1; 051 §6 |
| **C-061-15** | Registry authority is distinct from change governance, canonicality and source-of-truth class. | 051 §9–§10; row 065 |
| **C-061-16** | The normative boundary table (§7) exists and covers the source-established subjects. | Roadmap row 061 `Done` |
| **C-061-17** | This contract implements none of 062, 063, 064 or 065. | Roadmap rows 062–065 |
| **C-061-18** | Frozen P0, P1 and P2 architecture is unchanged, and their conformance suites stay green. | Artifact 004; rows 030, 038, 059 |

## 18. Completion and Handoff

| Row 061 | Where it is met |
|---|---|
| `Val`: *"Registry governs definitions; each model owns its Records"* | §4; §7; §8; C-061-01, C-061-02 |
| `Done`: *"boundary table"* | §7 (with §8); C-061-16 |
| `Why`: *"stops Registry becoming a super-model"* | §6, §10–§15; C-061-03 to C-061-15 |

After this contract, Registry's authority scope is settled: it governs definitions and owns only its
own Records. Artifact 062 organizes Registry semantics into layers without deciding again whether
Registry owns another model's Records.

---

*Artifact 061 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This contract
states the Registry authority boundary, derived from Master Blueprint §9.4 and §13.6e and the Record
Model System §10 and §17, and specializes Artifact 051 to the Registry domain. It is not a Registry
Record, holds no canonical data, defines no schema, permission or process, and implements nothing.
Where it differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap,
those governing sources are correct and this document is wrong.*
