# COOLBOY12 — Registry Reference Boundary

**Artifact 063** · Registry reference boundary · `docs/models/registry/references.md` · Own: R ·
RM: R · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P3/3a · Req: RR-18 · BP: §9.4 · RMS: §10.3 · H: 062 · S: — · LS: — · G: gates P3 exit ·
→ 064, PART IX · Val: **R may reference other Registry definitions, declared Models, declared
Kinds, declared schemas; R may NOT own, depend on, mutate, or take authority from domain
instances** · Done: rule stated in spec, matrix, governance, examples, impl notes · Why: the audit
found the prior phrasing too blunt · Risk: CRITICAL · ∥: no

## 1. Purpose

This contract answers one question — **what may a Registry definition legally reference, what must
it never reference, and what does a legal reference not imply?**

RMS §10.3 (`FROZEN`) gives the rule: *"R → R definitions = ALLOWED. R → domain instances =
FORBIDDEN."* This contract states that rule so that the definition families (066–107), the
dependency rules (111), the reference validator (112) and the negative proofs (121) can apply it
without reinterpreting it. The central case:

```
CHARACTER              a declared Kind          admissible target category
W-CH-000001-Maximus    a World Record           FORBIDDEN Registry reference target
```

*(`W-CH-000001-Maximus` is schematic throughout: an illustration, not a Record.)* The Registry may
define what `CHARACTER` means. It may not reference a particular Character, and no particular
Character may become the authority for what `CHARACTER` means.

Six questions are kept apart, and this contract answers only the second:

```
Can the target be resolved?                         shared mechanism (RMS §4)
May a Registry definition reference it?             THIS CONTRACT
May the definition semantically depend on it?       062 (layers); 111 (concrete rules)
Does the definition own it?                         no — I-105; Artifact 045
May the definition mutate it?                       no — RMS §10.3; Spine law 2
May the definition take semantic authority from it? never, for a domain instance — RMS §10.3
```

## 2. Constitutional Status

`Own: R` · `R: CONTRACT` · `SoT: AUTHORITATIVE` about the Registry reference boundary ·
`Auth: governing` · `Canon: n/a`. This document is not a Registry Record, holds no Registry data,
and creates no Kind, field, schema, Record or validator. Where it differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources are right and this
document is wrong.**

`Req: RR-18` is reproduced from row 063. The requirement register is not in the supplied source set,
so the ID is carried forward unverified and no requirement text is stated for it (GAP-C; Revolving
Resolution Note). `G: gates P3 exit` is carried as row 063 states it; this contract defines no gate,
and the exit-P3 gate sits at row 124. `→ PART IX` is the Roadmap's anti-ordering register; the
entries that bear on this boundary are X-05 and X-09 (§18).

## 3. Scope

**In scope.** The admissible categories of Registry reference target; the forbidden category; the
test that separates a declaration from a domain instance; the runtime boundary as the sources state
it; what a legal reference does not transfer (ownership, mutation authority, semantic authority,
canonicality, source-of-truth class); the separation of resolution from legality; governance
constraints; worked examples; implementation notes for 112 and 121; the resolution of the
reference-wording conflict that 058, 060 and 062 handed to this artifact.

**Out of scope, by owner.** The Registry Kind roster and admission rationale (064); governance
actors and process (065); definition-family content and schemas, including which concrete targets
each family may name (066–107); definition evolution, versioning, supersession and deprecation
(108–110); concrete definition-dependency rules — direction between definitions, asymmetry, cycles,
same-layer dependency (111); validator code (112); the binder, kernel, resolution service,
validation suite and identity binding (113–117); fixtures, examples and tests (118–124);
cross-model edges between the six Record Models (058). No schema, field, Registry data, validator,
algorithm or test is created.

## 4. Governing Sources and Frozen Inputs

| Source | What it gives this contract |
|---|---|
| RMS §10.3 | the controlling rule: the five admissible categories, the four prohibitions, *"R → R definitions = ALLOWED. R → domain instances = FORBIDDEN."*, and where the distinction must appear |
| RMS §10.2, §10.4, §10.5, §10.7 | schema definition ≠ schema implementation; the bootstrap meta-contract is not a Record; capability definition ≠ implementation; World owns current values |
| RMS §4; RMS §5 | a resolvable ID is the cross-model handle; resolution is mechanical and legality is model/Registry-owned; the seven-field envelope; the nine prohibitions; the partition-first grammar |
| Blueprint §9.4 | *"The Registry holds no instances."*; a registry entry naming a specific thing in the world is misfiled; *"Reference resolution is not Registry work."*; the older reference wording (§20) |
| Blueprint §13.6e; I-75; I-88; I-105 | *"Registry governs the definitions. Each Record Model owns its Records."*; the asymmetry; the older wording restated |
| Roadmap row 063; rows 066–107, 111, 112, 121, 122, 124; PART I; §2.4; PART IX | this artifact's metadata; *"references only declared entities (063)"*; the enforcement and proof chain; *"domain instances of W/E/P/V/I"*; the forbidden edge `R → domain instance`; X-05, X-09 |
| Artifact 058 §6, §8.2, §10, §11 | resolving is not permission; `registry_ref` creates no edge; reference grants no mutation; the Registry boundary recorded and handed here |
| Artifact 060 §10, §15 | the model-level rule; the definition-vs-runtime boundary |
| Artifact 061 §7, §10 | the authority boundary table; authority does not transfer through reference |
| Artifact 062 §7, §14.1, §16 | D-1 to D-9, settled; *dependency ≠ reference*; the wording conflict handed here as a reference question |
| Artifacts 033, 045, 050, 052, 055, 057 | the envelope; ownership is not reference; SoT class; canonicality; the relationship boundary; Kind admission |

## 5. Governing Reference Rule

RMS §10.3, `FROZEN`, stated as the source states it:

> *"Registry MAY reference: other Registry definitions · declared Record Models · declared Kinds ·
> declared schemas · declared semantic contracts."*
>
> *"Registry MAY NOT: own domain instances · depend on runtime instances · mutate domain instances ·
> use domain instances as semantic authority."*
>
> *"R → R definitions = ALLOWED. R → domain instances = FORBIDDEN."*

Row 063's `Val` restates it: *"R may reference other Registry definitions, declared Models,
declared Kinds, declared schemas; R may NOT own, depend on, mutate, or take authority from domain
instances"*.

**The rule as this contract binds it.**

| ID | Rule | Source |
|---|---|---|
| **RB-1** | A Registry definition may reference a target only if the target falls within one of the five admissible categories of §8 and is declared. The categories are closed: a target in none of them is not a legal Registry reference target. | RMS §10.3; rows 066–107 *"references only declared entities (063)"* |
| **RB-2** | A Registry definition never references a domain instance. | RMS §10.3; Roadmap §2.4; row 112 |
| **RB-3** | A Registry definition never owns, mutates, or takes semantic authority from a domain instance, whatever field, label or purpose carries the citation. | RMS §10.3; I-105; Blueprint §9.4 |
| **RB-4** | A Registry definition never depends on a runtime instance, and a runtime instance is not a legal Registry reference target. | RMS §10.3; row 121; RB-1 |
| **RB-5** | An admissible category is a necessary condition for a reference, not a sufficient one: the definition family, 062's layer law and 111's dependency rules may narrow it further. | rows 066–107, 111; Artifact 062 §7 |
| **RB-6** | Where a target cannot be shown to fall within an admissible category, the reference is not legal. Undetermined is not permitted. | RB-1 |

**Fail-closed.** RB-1 and RB-6 make the boundary closed at the category level: *"references only
declared entities"* is the Roadmap's own wording for every definition family. Nothing is legal
because it exists, resolves, or is not named in a prohibition. This is a rule about Registry
definitions only; it is not a rule about cross-model edges, where Artifact 058 §7 adopts neither a
closed nor an open default.

## 6. Declaration vs Domain Instance

This distinction is the centre of the contract.

**A declaration-level target** identifies governed system meaning, not a fact or a state of any
domain. The five admissible categories (§8) are all declaration-level:

- a Registry definition — an R Record;
- a declared Record Model;
- a declared Kind — the Kind itself, not a Record of that Kind;
- a declared schema;
- a declared semantic contract.

**A domain instance** is a Record of the W, E, P, V or I Record Model. The Roadmap names the class
in its directory rules — `canon/registry/` prohibits *"domain instances of W/E/P/V/I"* — and
Blueprint §9.4 states the consequence: *"A registry entry that names a specific thing in the world
is a misfiled Record."* Every Record carries exactly one partition (I-16), and the identity grammar
is partition-first (RMS §5), so whether a Record is a domain instance is fixed by its partition, not
by its Kind, its content, or how declarative its content reads. A Production `STYLE-GUIDE` Record is
a domain instance, however much it reads like a contract.

**Domain state** — the values a domain instance carries — is not a target either. The current WSV
indicator values are World state: *"WSV — World-owned singleton, one Record, current indicator
values"* (RMS §10.7).

**The test, applied to a proposed target:**

```
1. Is the target a Record of W, E, P, V or I?          yes → FORBIDDEN (RB-2)
2. Is it a runtime instance?                           yes → FORBIDDEN (RB-4)
3. Is it in one of the five categories of §8?          no  → not legal (RB-1, RB-6)
4. Is it declared?                                     no  → not legal (RB-1)
5. Category admissible and declared                        → admissible at the category level;
                                                             family spec, 062 and 111 decide
                                                             the particular relation (RB-5)
```

**Registry's own Records are not domain instances for this boundary.** Registry definitions are R
Records (RMS §10; I-105; Artifact 060 §5). RMS §10.3 allows *"R → R definitions"*; reading
*"R → domain instances = FORBIDDEN"* as forbidding a reference to another Registry Record would
contradict the sentence it stands in. The prohibited class is the domain instances of W, E, P, V and
I (SC-063-C).

**This is a Registry reference distinction**, not a new architectural category. It adds no Kind, no
universal class of declarations, and no field.

## 7. Normative Reference Matrix

This is the matrix row 063's `Done` requires. *ADMISSIBLE* means an admissible target category,
subject to the target being declared (RB-1), the definition family permitting the relation (RB-5),
062's layer law, 111's dependency rules, and the other models' boundaries. It never means
unrestricted. *FORBIDDEN* is absolute: no family, approval or label lifts it.

| # | Target category | Registry reference | Conditions | Ownership consequence | Dependency consequence | Authority consequence | Downstream enforcement |
|---|---|---|---|---|---|---|---|
| 1 | **Other Registry definition** (an R Record) | **ADMISSIBLE** | the target is a Registry definition Record and is declared; the family spec permits the relation | none: each Record stays R-owned and separately governed | not decided by 063: whether a given R → R reference is a semantic dependency, and its legality if so, is 062 D-1 to D-9 and 111 (*"downward-only; asymmetric; no cycles"*) | none: neither definition becomes the other's authority by reference alone | families 066–107; 111; 112; 121 |
| 2 | **Declared Record Model** | **ADMISSIBLE** | the target is one of the six constitutionally established models (RMS §2; I-101) | none: no model, partition or Record of that model passes to Registry | no dependency on the model's domain semantics: Registry depends on the other models *"for nothing"* (§13.6e) | no sovereignty conferred or held: a `MODEL-DEFINITION` neither creates nor grants a model (Artifact 061 §7 row 7) | 066–067; 112 |
| 3 | **Declared Kind** — the Kind, not a Record of it | **ADMISSIBLE** | the Kind is declared in its owning model's taxonomy; naming it is not admitting it (Artifact 057 §9) | none: the Kind's taxonomy, admission and instances stay with the owning model | not a semantic dependency on L2 or L3 (062 D-9) | the named Kind is not semantic authority for the definition that names it (062 D-9) | 068–069; 079–080; 112; 121 |
| 4 | **Declared schema** | **ADMISSIBLE** | the schema is declared; schema definition and schema implementation stay apart (RMS §10.2) | none: no ownership of the Records that conform to it | not decided by 063 (111) | no execution authority: *"Registry does not execute schemas."* (RMS §10.2); conformance makes no Record a legal target | 076–078; 112 |
| 5 | **Declared semantic contract** | **ADMISSIBLE** | the contract is declared; the sources name one instance — `CAPABILITY-DEFINITION` (RMS §10.5), itself a Registry definition — and enumerate no others (SC-063-F) | none | not decided by 063 (111) | no runtime control and no modelhood (RMS §10.5, §19) | 092–093; 112 |
| 6 | **Domain instance** — any Record of W, E, P, V or I | **FORBIDDEN** | always: whether or not it resolves, whatever its Kind, content or label | Registry never owns it (RMS §10.3; I-105) | Registry never depends on it (row 063 `Val`; 062 D-3) | never semantic authority; never mutated through the reference (RMS §10.3) | 112 (*"rejects any definition referencing a domain instance"*); 121; 122; X-09 |
| 7 | **Domain state used as semantic authority** — e.g. a current WSV indicator value | **FORBIDDEN** as semantic authority | always | the value stays World-owned: *"World owns current values. Registry owns meaning."* (RMS §10.7) | a definition's meaning never depends on a current value (062 D-3) | never establishes what an indicator, Kind or field means | 086–087; 112; 121 |
| 8 | **Runtime instance** — a live process, worker, service instance or session | **FORBIDDEN** | always; RMS §10.3 states the prohibition as dependency, row 121 as rejection, and RB-1 excludes it as a target (SC-063-D) | none | Registry *"MAY NOT … depend on runtime instances"* (RMS §10.3) | a capability's implementation is not its definition (RMS §10.5) | 112; 121 (*"R→runtime rejected"*) |

**No other row.** The matrix has no row for declared subtypes, fields, relationship types,
vocabularies, validators or capabilities as categories of their own: those are reached as Registry
definitions (row 1). It has no row for cross-model edges between the six models; those are 058's.

## 8. Admissible Registry Reference Categories

**8.1 Other Registry definitions.** *"R → R definitions = ALLOWED"*. A `SUBTYPE-DEFINITION` may name
the `KIND-DEFINITION` of its Kind; a `SCHEMA-DEFINITION` may name the `FIELD-DEFINITION`s it
composes (row 078); a `CONSTRAINT-DEFINITION` and a `VALIDATION-RULE` may name one another, kept
distinct (RMS §10.6). Each example shows the category only. Which pairwise relations each family
permits is the family's (066–107); whether a relation is a semantic dependency, its direction,
asymmetry, cycles and same-layer dependency are 062's and 111's. *"R → R definitions = ALLOWED"*
does not allow cycles.

**8.2 Declared Record Models.** A Registry definition may name a declared Record Model — for
example, a `KIND-DEFINITION` for `CHARACTER` naming the World Record Model. A declared Record Model
is not the same thing as a `MODEL-DEFINITION`: a reference to a `MODEL-DEFINITION` is an R → R
reference (§8.1); a reference to a declared Record Model is a declaration reference. Neither creates
the model, grants it sovereignty, or gives Registry any of its Records: the six models are
constitutionally established (RMS §2; I-101).

**8.3 Declared Kinds.** A Registry definition may name a declared Kind — a
`RELATIONSHIP-TYPE-DEFINITION` may name `CHARACTER` as a participant Kind. A declared Kind is not
the same thing as a `KIND-DEFINITION`: the `KIND-DEFINITION` is an R Record (§8.1); the Kind
belongs to the owning model's taxonomy. Naming a Kind does not admit it, and this contract decides
no Kind's existence: Kind admission is Artifact 057's and the owning model's, Registry's own
fourteen Kinds are 064's, and a listed roster is not thereby frozen (I-106).

**8.4 Declared schemas.** A Registry definition may name a declared schema. *"SCHEMA-DEFINITION is
a Registry Record. Schema implementation is not Registry runtime."* (RMS §10.2). Naming a schema
gives no authority to execute it, and a Record that conforms to a schema is not thereby a legal
target.

**8.5 Declared semantic contracts.** RMS §10.3 names the category; RMS §10.5 names one member:
*"CAPABILITY-DEFINITION is a Registry Record — a semantic contract."* The sources give no exhaustive
list, and this contract adds none. It does not classify constitutional documents, the Bootstrap
Meta-Contract, runtime APIs, adapter protocols, source-code interfaces or governance procedures as
declared semantic contracts. RMS §10.4 places the Bootstrap Meta-Contract outside the ordinary
Registry Record ontology — *"The Bootstrap Meta-Contract is NOT a Record."* and *"There is no
circular self-definition requirement."* — and nothing here draws it into the Registry reference
graph (SC-063-F).

**Being declared is a precondition, not a process.** A target must be declared before a reference
to it is legal; the Roadmap lists the reverse order as an anti-ordering — X-05, *"Consumer before
provider"*: *"Resolving definitions that do not exist"*. Two readings are applied here, each
labelled as a reading: the six Record Models, constitutionally established (RMS §2; I-101), are
declared Record Models; and a Kind standing in its owning model's roster is a declared Kind — the
Blueprint speaks of *"The currently declared roster"* (§13.6e). Declared is not frozen (I-106), and
admission is Artifact 057's. How a schema or semantic contract acquires declared status, and who
proposes, approves or deprecates any declaration, are not established here (065; 108–110;
SC-063-H).

## 9. Forbidden Domain-Instance Boundary

**A Registry definition MUST NOT reference a domain instance.** RMS §10.3; Roadmap §2.4
(`R → domain instance` among the forbidden edges); row 112 (*"rejects any definition referencing a
domain instance"*); row 121 (*"R→instance rejected"*). Schematic cases, every one FORBIDDEN:

| Registry definition | references | Partition | Result |
|---|---|---|---|
| any Registry definition | `W-CH-000001-Maximus`, a World `CHARACTER` Record | W | **FORBIDDEN** |
| any Registry definition | a particular Epistemic Record, e.g. one `KNOWLEDGE-STATE` | E | **FORBIDDEN** |
| any Registry definition | a particular Production Record, e.g. one `STYLE-GUIDE` | P | **FORBIDDEN** |
| any Registry definition | a particular Visual Record, e.g. one `VISUAL-ASSET` | V | **FORBIDDEN** |
| any Registry definition | a particular Issue Record, e.g. one `ISSUE` | I | **FORBIDDEN** |
| `WSVR-INDICATOR-DEFINITION` | the WSV singleton or a current indicator value | W | **FORBIDDEN** |

Kind codes outside World are not frozen; the E, P, V and I cases name Kinds and no identifiers.

**The ban is semantic, not cosmetic.** A definition does not escape it by calling the citation an
example, evidence, a sample, a prototype or a hint. RMS §10.3 forbids *"use domain instances as
semantic authority"*: if a domain instance helps establish what a definition means, the boundary is
violated, whatever the field is called. One Character Record cannot become the authority for what
`CHARACTER` means (Artifact 061 §10).

**A domain instance is never upstream.** A domain instance may motivate a later proposal to change a
definition; that makes it neither a reference target nor semantic authority (Artifact 062 §7). How
such a change is governed is 065's.

**A documentation example is not a reference.** This contract names a schematic Character to show
its rejection. The mention makes no Registry definition able to reference it.

## 10. Reference vs Semantic Dependency

Artifact 062 settled the layer direction (D-1 to D-9) and the separation: *dependency ≠
reference*. D-9: *"A declaration reference that RMS §10.3 permits and Artifact 063 bounds — for
example a Registry definition naming a declared Kind — is not a semantic dependency on L2 or L3."*

This contract decides reference legality only. A reference legal under §7 is not thereby a semantic
dependency, and the named target does not thereby become the definition's semantic authority.
Whether a particular relation between definitions is a dependency, and whether its direction is
legal, is 062's at the layer level and 111's at the concrete level. Nothing here restates or relaxes
D-1 to D-9.

**No universal theory.** Artifact 058 records that the sources use *reference* and *dependency*
without one definition of the difference across the Record System. This contract states the
Registry-specific separation that 062 already binds, and defines nothing for W, E, P, V or I.

## 11. Resolution vs Legality

> **Resolvable ≠ legal.**

RMS §4: *"Reference resolution | Cross-model references must resolve uniformly | Resolution is
mechanical; legality is model/Registry-owned"*. Blueprint §9.4: *"Reference resolution is not
Registry work."* and *"The Registry defines the reference field; it does not perform or own
resolution."* Artifact 058 §6: *"Resolving is not permission."*

- A resolver answers whether a target exists and resolves. It does not answer whether a Registry
  definition may reference it.
- `W-CH-000001-Maximus` may resolve perfectly through the shared mechanism. As a Registry reference
  target it is still FORBIDDEN, because it is a domain instance.
- An unresolvable target is not legal either: a definition that names what does not exist is the
  X-05 anti-ordering. Resolution is necessary for use and never sufficient for legality.

**Handle, not semantics.** Where a target is a Record, the handle is a resolvable ID: *"A resolvable
ID is the only legal cross-model handle"* (RMS §4). This contract adds no embedded object, pointer,
path, runtime memory reference or Registry-only addressing, and does not decide how a reference
names a declaration that is not a Record (SC-063-G).

## 12. Ownership, Mutation, Authority, Canonicality and SoT

A legal Registry reference transfers none of the following.

- **Ownership.** A reference *"DOES NOT TRANSFER OWNERSHIP"* (Artifact 045 §9). A `KIND-DEFINITION`
  naming the World Kind `CHARACTER` gives Registry no World Record: *"Registry governs the
  definitions. Each Record Model owns its Records."* (§13.6e; I-105).
- **Mutation authority.** Registry *"MAY NOT … mutate domain instances"* (RMS §10.3), and a
  permitted reference grants no mutation (Artifact 058 §10). Naming the World Record Model gives
  Registry no write to any World Record. Canonical change follows Spine law 2; the Mutation
  Coordinator is not described here.
- **Semantic authority.** No domain instance is the authority for a definition's meaning (§9). In
  the other direction, *"The Registry owns meaning, never world truth."* (I-88), and *"Registry is
  canon about meaning only; it can never override World Truth"* (RMS §24).
- **Canonicality.** Canonicality is model-defined (I-104; Artifact 052). A Registry definition is
  canonical about meaning where the sources establish it (Artifact 052 §5.4); a reference adds no
  canonicality to it, takes none from its target, and creates no reference-derived canonicality.
- **Source-of-truth class.** The referencing definition's SoT class and its target's are
  independent (§29.6a; Artifact 050). A reference neither transfers nor infers `AUTHORITATIVE`,
  `DERIVED`, `CACHED`, `TEMPORARY` or `EXTERNAL`.

## 13. Runtime Boundary

RMS §10.3 states the runtime prohibition as dependency: Registry *"MAY NOT … depend on runtime
instances"*. Row 121 requires the proof *"R→instance rejected; R→runtime rejected"*. And a runtime
instance is not in any admissible category (RB-1). This contract states all three and claims no more
(SC-063-D).

The definition-vs-runtime boundary is RMS's: *"CAPABILITY-DEFINITION is a Registry Record — a
semantic contract. CAPABILITY-IMPLEMENTATION is a runtime mechanism and is not a Record."* and
*"Recording a capability's definition never makes that capability a Record Model."* (RMS §10.5); RMS
§19: *"Capabilities have Registry definitions; that never confers modelhood."* A
`CAPABILITY-DEFINITION` for the Context Builder is a legal subject. One live Context Builder
process, worker, service instance or session is not a legal reference target and is never the
definition's semantic authority. What counts as a runtime instance for testing is 121's to fix.

## 14. `registry_ref` and the Universal Mechanism Boundary

Every Record carries `registry_ref` (RMS §4); Artifact 033: it *"Carries the Record's reference into
the Registry"*. That is the reverse direction — a Record pointing at Registry — and it is not
governed here. The existence of `registry_ref` on a Record gives Registry no ownership of it
(Artifact 058 §11; Artifact 061 §10), and it is not evidence that any reference from a Registry
definition to a domain instance is legal.

This contract adds no envelope field — no `reference_type`, `target_kind`, `target_partition`,
`reference_mode` or `dependency_mode`. The universal envelope stays at seven fields (RMS §4). It
creates no `REFERENCE` Record, Registry-reference Record or reference-edge Record: RMS §10.1 closes
Registry's taxonomy at fourteen, and RMS §4 prohibits a Universal Relationship Record. A Registry
definition's reference is not a World Relationship Record (I-102; Artifact 055 §10). Fields that
future definition schemas need are theirs (066–107).

## 15. Governance Constraints

RMS §10.3 requires the distinction to appear in *"the governance matrix"*. Row 065 owns governance:
*"who may propose, approve, deprecate a definition"*. This contract states only what every
governance act must respect:

| ID | Constraint | Source |
|---|---|---|
| **GC-1** | No governance act may approve a Registry reference that §7 forbids or that falls outside the admissible categories. | RMS §10.3; RB-1 |
| **GC-2** | No approval role may waive the domain-instance prohibition. Lifting it would be an amendment of RMS §10.3, which is `FROZEN`, not an act of Registry governance. | RMS §10.3; Blueprint §9.4 |
| **GC-3** | A reference becomes legal only once its target is declared. | RB-1; X-05 |
| **GC-4** | A changed reference target is judged afresh against this boundary; legality is not inherited from the reference it replaces. | RB-1 |
| **GC-5** | Approval makes no domain instance into a declaration and no current value into a definition's meaning. | RMS §10.3, §10.7 |

Not defined here: who proposes, who approves, quorum, roles, workflow states, deprecation ceremony
(065; 108–110). How a reference behaves when its target is superseded or deprecated is 108–110's.

## 16. Worked Positive Examples

**Example A — declared Record Model.** A `KIND-DEFINITION` for `CHARACTER` names the World Record
Model. Declaration reference; admissible target category (row 2). Registry gains no World Record and
confers no sovereignty.

**Example B — declared Kind, against the instance.** A `RELATIONSHIP-TYPE-DEFINITION` names
`CHARACTER` as a participant Kind: admissible target category (row 3). The same definition naming
`W-CH-000001-Maximus`: FORBIDDEN (row 6). The first names meaning; the second names one Record.

**Example C — indicator meaning.** A `WSVR-INDICATOR-DEFINITION` names the declarations the family
spec (086–087) permits — for example the World Record Model: admissible. It never takes its meaning
from the current WSV value: *"World owns current values. Registry owns meaning."* (RMS §10.7;
I-108).

**Example D — schema.** A `KIND-DEFINITION` or `SCHEMA-DEFINITION` names a declared schema, where
the family contract permits it: admissible (row 4). One Record that happens to conform to that
schema is not thereby a legal target; it is a domain instance (row 6).

**Example E — R → R.** A `SUBTYPE-DEFINITION` names the `KIND-DEFINITION` of its Kind: the category
*"R → R definitions = ALLOWED"* (row 1). Whether that relation is a dependency, and the rules on its
direction and on cycles, are 062's and 111's; the example decides neither.

**Example F — capability.** A `CAPABILITY-DEFINITION` names another Registry definition or a
declared semantic contract, where the family (092–093) permits it: admissible (rows 1, 5). It
never takes its meaning from one live process, worker, service instance or session (row 8).

## 17. Worked Negative Examples

| Case | Result | Why |
|---|---|---|
| A Registry definition → a W Record (`W-CH-000001-Maximus`) | **FORBIDDEN** | domain instance (RB-2) |
| A Registry definition → an E Record (one `KNOWLEDGE-STATE`) | **FORBIDDEN** | domain instance (RB-2) |
| A Registry definition → a P Record (one `STYLE-GUIDE`) | **FORBIDDEN** | domain instance, however contract-like (RB-2) |
| A Registry definition → a V Record (one `VISUAL-ASSET`) | **FORBIDDEN** | domain instance (RB-2) |
| A Registry definition → an I Record (one `ISSUE`) | **FORBIDDEN** | domain instance (RB-2) |
| A `KIND-DEFINITION` for `CHARACTER` that cites `W-CH-000001-Maximus` as evidence of what a Character is | **FORBIDDEN** | domain instance as semantic authority (RB-3) |
| A `WSVR-INDICATOR-DEFINITION` whose range is set from the current WSV value | **FORBIDDEN** | domain state as semantic authority (row 7) |
| A `CAPABILITY-DEFINITION` → one running Context Builder session | **FORBIDDEN** | runtime instance (RB-4) |
| A Registry definition → a target in no admissible category | **not legal** | closed categories (RB-1, RB-6) |
| A Registry definition → a definition not yet declared | **not legal** | X-05 (GC-3) |

**Resolution does not rescue it.** `W-CH-000001-Maximus` resolves through the shared mechanism. The
reference is still FORBIDDEN: resolution answered *does it exist*; this boundary answers *may a
Registry definition name it*, and the answer is no.

## 18. Implementation Notes

No code is written here. These are the requirements this contract places on later artifacts.

**Resolver** (the shared mechanism, RMS §4; the Registry resolution service, row 115). It answers
*does the target resolve*. It does not answer *is the reference legal*, and no component may treat
resolution success as legality.

**Reference validator — row 112** (*"rejects any definition referencing a domain instance"*). Input:
a Registry definition and one reference target. It decides:

```
1. does the target exist and resolve?           shared mechanism; failure → reject (X-05)
2. is the target a Record of W, E, P, V or I?   yes → reject (RB-2), although step 1 succeeded
3. is it a runtime instance?                    yes → reject (RB-4)
4. is it in an admissible category, declared?   no or undetermined → reject (RB-1, RB-6)
5. do the family spec and 111 permit it?        no → reject (RB-5)
                                                otherwise → legal
```

Steps 2–4 are this contract's. Step 5 is the family specs' (066–107) and 111's. Row 112 implements
the combination (`H: 063,111`). Because a Record's identity is partition-first (RMS §5; Artifact
034) and every Record carries exactly one partition (I-16), a target that resolves to a Record whose
partition is W, E, P, V or I is a domain instance; the validator needs no Kind roster to decide
step 2. How step 1 applies to a declaration that is not a Record follows its reference form
(SC-063-G). Exact error mechanics are 112's.

**Dependency rules — row 111.** A target that passes this contract is not thereby a legal
dependency. Direction, asymmetry, cycles and same-layer dependency stay 111's (*"downward-only;
asymmetric; no cycles"*).

**Family specs — rows 066–107.** Each carries *"references only declared entities (063)"*. Each may
narrow which admissible targets its definitions name; none may widen §7.

**Negative proof — row 121** (*"R→instance rejected; R→runtime rejected"*; *"proves rejection, not
absence"*). The suite must show rejection of each FORBIDDEN row of §7, including a target that
resolves. **Boundary tests — row 122** (*"Registry does not own domain semantics"*). **P3
conformance — row 124** (*"boundaries enforced"*). **Anti-orderings — PART IX:** X-05 and X-09
(*"Registry becomes a super-model"*), both statically tested by 112.

None of these tests or validators is created here.

## 19. Prohibited Inferences

| # | Prohibited inference | Why | Basis |
|---|---|---|---|
| 1 | A resolvable target is a legal Registry reference. | resolution ≠ legality | §11; RMS §4 |
| 2 | A Kind code that parses or resolves is thereby a declared Kind. | declaration is the owning model's | §8.3; Artifact 057 |
| 3 | An admissible category makes every pairwise reference legal. | necessary, not sufficient | RB-5 |
| 4 | A reference is a semantic dependency. | dependency ≠ reference | §10; 062 D-9 |
| 5 | A reference transfers Record ownership. | it transfers none | §12; Artifact 045 §9 |
| 6 | A reference transfers or confers canonicality. | canonicality is model-defined | §12; I-104 |
| 7 | A reference transfers or infers an SoT class. | classes are independent | §12; Artifact 050 |
| 8 | A reference grants mutation authority. | Registry never mutates a domain instance | §12; RMS §10.3 |
| 9 | A domain instance becomes semantic authority by being cited, as evidence or otherwise. | the ban is semantic | §9; RMS §10.3 |
| 10 | Registry may reference a Character because it defines `CHARACTER`. | defining a Kind is not referencing its instances | §6; Blueprint §9.4 |
| 11 | A `WSVR-INDICATOR-DEFINITION` may use current WSV values to establish meaning. | World owns current values | §9; RMS §10.7 |
| 12 | *"R → R definitions = ALLOWED"* allows dependency cycles. | cycles are 111's | §8.1; row 111 |
| 13 | A declaration reference makes Registry a super-model. | Registry owns definitions only | I-105; X-09 |
| 14 | `registry_ref` makes every Record Registry-owned. | it confers no ownership | §14; Artifact 058 §11 |
| 15 | A reference to a declared Kind means Registry admitted that Kind. | naming ≠ admission | §8.3; Artifact 057 §9 |
| 16 | A reference to a declared Record Model means Registry created that model. | the six are constitutional | §8.2; RMS §2 |
| 17 | A reference to a declared schema means Registry executes the schema. | definition ≠ implementation | §8.4; RMS §10.2 |
| 18 | A capability definition may reference a live implementation instance as authority. | runtime ≠ definition | §13; RMS §10.5 |
| 19 | A Registry Record is a forbidden domain instance. | R → R is allowed | §6; SC-063-C |
| 20 | Every document, contract or interface is a declared semantic contract. | the category is not enumerated | §8.5; SC-063-F |
| 21 | 063 defines universal reference semantics for all six models. | Registry-only | §10; Artifact 058 |
| 22 | The Blueprint's older wording still forbids naming a declared Kind. | narrowed by RMS §10.3 | SC-063-A |

## 20. Source-Condition and Conflict Register

### SC-063-A — the older reference wording: RESOLVED HERE

| | |
|---|---|
| **Source A** | Blueprint §9.4: *"The one rule the contract exists to enforce: dependency runs downward only. A Registry definition may never reference a kind, a subtype, or an instance; a kind may never reference an instance."* Restated at §13.6e; I-75: *"Registry dependency runs downward only: a Registry definition never references a kind, a subtype, or an instance; a kind never references an instance."* |
| **Source B** | RMS §10.3 (`FROZEN`, *"corrects v0.1"*): *"v0.1 stated the boundary too bluntly"* — quoting *"may never reference a kind"* — and states the precise rule (§5). |
| **Conflict** | Read literally as a rule of reference, Source A forbids naming a declared Kind; Source B allows it. On domain instances they agree. |
| **Handoff** | Artifacts 058 §11, 060 §10 and 062 §14.1 recorded the condition without reconciling it and handed it to row 063. Row 063's `Val` restates Source B; its `Why` is *"the audit found the prior phrasing too blunt"*. |
| **Resolution** | **For the reference legality of Registry definitions, RMS §10.3 controls.** A Registry definition may reference a declared Kind, a declared Record Model, a declared schema, a declared semantic contract and another Registry definition (§8). It may never reference a domain instance (§9), and a `KIND-DEFINITION` may never reference one — Source A's *"a kind may never reference an instance"* stands in full. |
| **Grounds** | (1) RMS §10.3 is the frozen, explicit statement of the precise rule, and identifies the wording Source A carries as too blunt. (2) Source A states its sentence as the content of the dependency rule — *"dependency runs downward only"*; I-75 is headed *"Registry dependency runs downward only"*. That dependency rule is kept whole by Artifact 062 (D-1 to D-9); this resolution narrows nothing in it. (3) Row 063 adopts Source B as the build rule for this boundary. (4) The author's instruction for this artifact directs that the conflict be closed here on RMS §10.3. |
| **Effect** | The Blueprint text is not modified; any wording fix is the author's act, as for PC-1. Subtypes are reached as Registry definitions (§8.1). Downstream artifacts (064–124) apply this boundary and do not reopen the conflict. |

### SC-063-B — reference vs dependency

Artifact 058 records that the sources use both words without one Record System-wide definition of
the difference. This contract invents none (§10). Artifact 062's Registry-specific separation (D-9)
binds. **Recorded; nothing to resolve here.**

### SC-063-C — Registry Record vs domain instance

A Registry definition Record is an R Record and is not a domain instance. Otherwise *"R → R
definitions = ALLOWED"* could not hold. The forbidden class is *"domain instances of W/E/P/V/I"*
(Roadmap PART I). **Settled by the sources' own wording.**

### SC-063-D — runtime wording

RMS §10.3 says *"depend on runtime instances"*. Row 063's `Val` adds *"depend on … domain
instances"*. Row 121 says *"R→runtime rejected"*. This contract states each as written: Registry
never depends on a runtime instance (RMS), never depends on a domain instance (row 063; 062 D-3),
and a runtime instance is not an admissible target (RB-1; row 121). It does not widen the RMS
sentence into a separate prohibition; the reference-level rejection rests on RB-1 and row 121.
Which runtime objects 121 must exercise is 121's.

### SC-063-E — four categories in `Val`, five in RMS

Row 063's `Val` names four admissible categories; RMS §10.3 names five, adding *"declared semantic
contracts"*. The `Val` does not say *only*, so the two do not conflict. RMS governs; all five are
stated.

### SC-063-F — semantic contracts not enumerated

The sources name one declared semantic contract (`CAPABILITY-DEFINITION`, RMS §10.5) and give no
list. **Not established by current sources:** whether anything that is not a Registry definition
counts as one, and whether a Registry definition may name the Bootstrap Meta-Contract. This contract
classifies neither and assigns neither to an artifact.

### SC-063-G — the form of a declaration reference

How a Registry definition names a declaration that is not a Record — a declared Model or Kind
directly, or through its R definition — is not established by current sources. The definition
schemas (067, 069, 077, 080) and the validator (112) meet it. This contract fixes legality, not
form.

### SC-063-H — acquiring declared status

How a schema or semantic contract becomes declared, and who acts, is not established here; 065 and
108–110 hold governance and evolution.

## 21. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-063-01** | A Registry definition may reference another Registry definition (R → R): admissible category. | RMS §10.3 |
| **C-063-02** | A declared Record Model is an admissible target category. | RMS §10.3 |
| **C-063-03** | A declared Kind is an admissible target category. | RMS §10.3; SC-063-A |
| **C-063-04** | A declared schema is an admissible target category. | RMS §10.3 |
| **C-063-05** | A declared semantic contract is an admissible target category. | RMS §10.3 |
| **C-063-06** | A domain instance — any Record of W, E, P, V or I — is a forbidden target. | RMS §10.3; Roadmap §2.4, PART I |
| **C-063-07** | Registry acquires no ownership through a reference. | RMS §10.3; I-105; Artifact 045 §9 |
| **C-063-08** | Registry cannot mutate a domain instance through a reference. | RMS §10.3 |
| **C-063-09** | A domain instance never becomes Registry semantic authority, under any label. | RMS §10.3 |
| **C-063-10** | Registry never depends on a runtime instance, and a runtime instance is not an admissible target. | RMS §10.3; row 121; RB-1 |
| **C-063-11** | Resolvability does not imply legality. | RMS §4; Blueprint §9.4 |
| **C-063-12** | Reference legality does not imply semantic dependency. | Artifact 062 D-9 |
| **C-063-13** | An admissible category does not make every pairwise relation legal. | RB-5; rows 066–107, 111 |
| **C-063-14** | Artifact 062's downward-only layer law remains binding and is not restated or relaxed. | Artifact 062 §7 |
| **C-063-15** | Row 111 owns concrete dependency direction, asymmetry, cycles and same-layer dependency. | row 111 |
| **C-063-16** | Row 112 owns mechanical reference validation. | row 112 |
| **C-063-17** | Row 121 owns the negative proof. | row 121 |
| **C-063-18** | Row 065 owns governance actors and process; only constraints are stated here. | row 065 |
| **C-063-19** | Row 064 owns the Registry fourteen-Kind roster. | row 064 |
| **C-063-20** | Registry's own R Records are legitimate R → R targets and not domain instances. | RMS §10.3; SC-063-C |
| **C-063-21** | `registry_ref` transfers no ownership and legitimizes no R → domain-instance reference. | Artifacts 033, 058 §11, 061 §10 |
| **C-063-22** | No universal reference semantics across the six models is defined. | Artifact 058; RMS §4 |
| **C-063-23** | Resolver success is not semantic legality. | RMS §4; §11 |
| **C-063-24** | A schema declaration reference implies no schema execution. | RMS §10.2 |
| **C-063-25** | A Model declaration reference confers no model sovereignty. | RMS §2; I-101 |
| **C-063-26** | A Kind declaration reference confers no Kind admission. | Artifact 057 §9 |
| **C-063-27** | No domain Record instance is used to define Registry meaning. | RMS §10.3; I-88 |
| **C-063-28** | The admissible categories are closed; a target in none of them, or whose category cannot be established, is not legal. | RB-1, RB-6; rows 066–107 |
| **C-063-29** | The older Blueprint wording is narrowed by RMS §10.3 for reference legality; the downward-only dependency rule and the instance prohibition stand in full. | SC-063-A |
| **C-063-30** | No envelope field, Kind, Record category or reference Record is added. | RMS §4, §10.1 |

## 22. Downstream Handoff

| Artifact | May assume from 063 | Must still define |
|---|---|---|
| **064** Kind taxonomy | the reference boundary its fourteen Kinds are subject to | the fourteen Kinds and each admission rationale |
| **065** governance | GC-1 to GC-5 | who may propose, approve, deprecate a definition |
| **066–107** families | the five admissible categories, the forbidden class, RB-1 to RB-6 | which admissible targets each family names; the field form of each reference (SC-063-G) |
| **108–110** evolution | GC-4 | how references behave across versions, supersession and deprecation |
| **111** dependency | that legality and dependency are separate; R → R is admissible at the category level | concrete direction, asymmetry, cycles, same-layer dependency |
| **112** reference validator | the check of §18 (steps 2–4) and the matrix of §7 | the code; error mechanics; the combination with 111 |
| **121** negative tests | the FORBIDDEN rows of §7 and §17's cases, including a resolving forbidden target | the tests, and which runtime objects they exercise |
| **122** boundary tests | §12's non-transfers | the tests |
| **124** P3 conformance | that the reference boundary is stated | *"boundaries enforced"* — the suite |

## 23. Roadmap Completion Trace

| Row 063 | Status | Where it is met |
|---|---|---|
| `Val`: *"R may reference other Registry definitions, declared Models, declared Kinds, declared schemas"* | **SATISFIED** — all four, plus RMS §10.3's declared semantic contracts (SC-063-E) | §5, §7 rows 1–5, §8; C-063-01 to C-063-05 |
| `Val`: *"R may NOT own, depend on, mutate, or take authority from domain instances"* | **SATISFIED** | §7 rows 6–7, §9, §12; C-063-06 to C-063-09, C-063-27 |
| `Done`: *"rule stated in spec"* | **SATISFIED** | §5 RB-1 to RB-6, §6 |
| `Done`: *"matrix"* | **SATISFIED** | §7 |
| `Done`: *"governance"* | **SATISFIED** — constraints only | §15 |
| `Done`: *"examples"* | **SATISFIED** | §16, §17 |
| `Done`: *"impl notes"* | **SATISFIED** | §18 |
| `Why`: *"the audit found the prior phrasing too blunt"* | **SATISFIED** — the older wording is narrowed, not left open | §20 SC-063-A |
| `H: 062` | **SATISFIED** — D-1 to D-9 consumed, not reopened | §10; C-063-12, C-063-14 |
| `→ 064, PART IX` | **SATISFIED** — handoffs stated; X-05 and X-09 bound | §18, §22 |

---

*Artifact 063 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This contract
states the Registry reference boundary from Record Model System §10.3, Master Blueprint §9.4 and
§13.6e, and Roadmap row 063. It is not a Registry Record, holds no canonical data, defines no
schema, field, validator or algorithm, and implements nothing. Where it differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, those governing sources are
correct and this document is wrong.*
