# COOLBOY12 — Registry Self-Kind Definition Set Contract

**Artifact 074** · Registry self-Kind definition set contract ·
`docs/registry/registry_kind_definition_set.md` · Own: R · RM: R · T: doc · R: ARCH ·
SoT: AUTHORITATIVE · Auth: defining · Canon: n/a · CD: no · Ph/St: P3/3b · Req: RR-16 · BP: §9.4 ·
RMS: §§10.1,10.4 · H: 064,069 · S: — · LS: — · G: — · → 075 · Val: the concrete Registry
self-definition set is specified as exactly fourteen KIND-DEFINITION Records, one for each Kind of
064; self-hosting follows RMS §10.4; no extra Kind is created · Done: contract · Why: **specifies
the Registry half of the Registry's own LS-1 pairs — AUTHOR-DECIDED revision AD-LS1-R-BOOTSTRAP
(§0.7)** · Risk: HINGE · ∥: no

## 1. Purpose

This contract answers one question — **what exact set of Registry `KIND-DEFINITION` Records must
exist so that each of the Registry's fourteen frozen Kinds has its Registry-side LS-1 partner,
including the Kind `KIND-DEFINITION` itself, without an axiom Record, a circular bootstrap
requirement, a fifteenth Kind, a new definition family, or any Record authored here?**

The answer is one sentence: **the set is exactly fourteen `KIND-DEFINITION` Records with
`subject_model` R, in one-to-one correspondence with the fourteen Kinds of Artifact 064, each
conforming to Artifact 069.**

```
Artifact 064   the Registry's frozen fourteen-Kind taxonomy            taxonomy half of LS-1
      ↓
Artifact 074   specifies the fourteen-member KIND-DEFINITION set       this contract · LS: —
      ↓
Artifact 075   authors the fourteen KIND-DEFINITION sources            definition half · LS: LS-1
      ↓
row 152        commits them to canon/registry/registry_kinds/, only after G-CANON-R

The Registry's own LS-1 pairs:   064 ↔ 075        (not 068 ↔ 069, not 074 ↔ 075)
```

Artifact 074 is a **set contract**. It says which members must exist and what each must satisfy.
It does not say what the `KIND-DEFINITION` family means (068), what shape a `KIND-DEFINITION` Record
has (069), or what any member's definition says (075).

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: ARCH` · `SoT: AUTHORITATIVE` about the Registry self-definition
set · `Auth: defining` · `Canon: n/a` · `CD: no`. This document is a contract. It is **not** a
`KIND-DEFINITION` Record, not a member of the set it specifies, and not a Record of any Kind: it
carries no universal envelope, mints no identifier, holds no Registry data, authors no member
source, and writes nothing under `docs/registry/registry_kinds/` or `canon/**`. Where it differs
from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources
are right and this document is wrong.**

`Req: RR-16` is reproduced from row 074. The requirement register is not in the supplied source set,
so the ID is carried forward unverified and no requirement text is stated for it (GAP-C;
SC-074-F).

Statements below are labelled where it matters: **source fact** (stated by the Blueprint, the RMS,
the Roadmap or a frozen artifact), **required synthesis** (a conclusion several source facts force
together; not a quotation), **reading** (an interpretation, recorded as one), and **source gap**
(not established, and not filled here).

## 3. Scope

**In scope.** The membership of the Registry self-definition set; its cardinality; the one-to-one
correspondence between members and Registry Kinds; the subject-model rule; the requirement that
every member conform to Artifact 069; the semantic source each member's definition must stay within;
the self-hosted member whose subject is `KIND-DEFINITION`; the RMS §10.4 bootstrap boundary; the
LS-1 role of rows 064, 074 and 075; the split between this contract and row 075; the
canonicalization boundary; the exclusions; the handoff to row 075.

**Out of scope, by owner.**

| Not defined here | Owner |
|---|---|
| the fourteen Registry Kinds, their responsibilities and admission rationale | 064 (consumed, §5) |
| what the `KIND-DEFINITION` family means | 068 |
| the structural shape of every `KIND-DEFINITION` Record | 069 (consumed, §6) |
| the fourteen concrete member sources and every member's `definition` content | 075 |
| how the members are packaged — files, names, count of files, layout, a manifest | 075 |
| committing any member to `canon/registry/registry_kinds/` | 152, after G-CANON-R (Roadmap §0.8) |
| lockstep validation; exit-P3 and G-REG | 123; 124 |
| Registry create, resolve and version operations; consumer resolution | 114; 115 |
| evolution, versioning, supersession, deprecation | 108, 109, 110 |
| concrete definition-dependency rules | 111 |
| Registry Kind codes and identity binding | 117 |
| who may propose, approve or deprecate a definition | 065 |
| how a Kind is admitted, or a new Kind added | 057; 459 |
| the other models' Kind-Definition sets | 178 (W), 257 (E), 300 (P), 345 (V), 364 (I); VERDICT 399 |

No Record, member source, schema, field, identifier, Kind code, test, fixture or runtime behaviour
is created, and no Kind is declared, admitted, renamed or retired.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where it says so
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done; §0.7 and §0.8 author rulings
        ↓
frozen artifacts; Artifact 003 conventions
        ↓
Artifact 074
```

| Source | What it gives this contract |
|---|---|
| RMS §10; §10.1 | the Registry is a sovereign Record Model; *"Final Kind taxonomy — CLOSED at fourteen"*, with the fourteen names in order |
| RMS §10.4 | the Bootstrap Meta-Contract is not a Record; no axiom Record; no circular self-definition requirement |
| RMS §4; §10.3 | the universal envelope and the nine prohibited universal semantics; the reference boundary |
| Blueprint §9.4; §13.6; §13.6e | the Registry layer; the earlier ten-item roster; FG-V7-05 and FG-V7-07 as historically OPEN |
| Roadmap row 074; §0.7 (AD-LS1-R-BOOTSTRAP); §0.8 (AD-REG-AUTHORING-SPLIT); PART III (LS-1) | this artifact's identity; the self-hosting revision; authoring vs canonical materialization; the lockstep pair |
| Roadmap rows 075, 114, 123, 124, 152; 178, 257, 300, 345, 364, 399 | the consumer and the gates; the other models' sets, for comparison only |
| Artifact 064 (`H: 064`) | the fourteen Kinds, their responsibilities and fourteen-question answers; Kind ≠ `KIND-DEFINITION`; the non-roster rows |
| Artifact 069 (`H: 069`) | the structure every member must have |
| Artifact 003 | the lockstep conventions and the *Registry LS-1 self-hosting exception* |
| Artifacts 057, 060, 061, 062, 063, 068 | admission ≠ definition; Registry sovereignty; the authority table; layers; the reference boundary; the family |

Artifacts 003, 057, 060, 061, 062, 063 and 068 are consumed as frozen constraints. They are not
declared dependencies of row 074 and are not added to `H` or `S`. Row 075 does not yet exist in the
repository; its Roadmap row is cited, not its content.

Citations are to the repository copies in `docs/sources/`: the Blueprint is
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md` (revision header v0.7.0), the RMS
`COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`, the Roadmap `COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`.

## 5. Hard Dependency — Artifact 064, the Taxonomy

`H: 064` is consumed unchanged. Artifact 064 is the authoritative source of set membership.

- **The roster.** Exactly fourteen Kinds, by their RMS §10.1 names and in RMS §10.1 order (064 §6).
  The Registry is one sovereign Record Model; its Kind taxonomy is its own.
- **What each Kind is.** Each Kind's source-established responsibility and its answers to the
  fourteen questions (064 §8 to §21). §10 cites them per member.
- **Kind ≠ `KIND-DEFINITION`.** *"A Kind is not its `KIND-DEFINITION`."* (064 §22). A definition is
  not admission (C-057-08).
- **The handoff.** 064 §27 gives rows 074–075 *"the fourteen Kinds of §6, in RMS order, as the
  subjects of the fourteen `KIND-DEFINITION` Records"*.
- **Names are not Kinds.** *"An artifact name is not evidence of a Kind"* (064 §23).
- **The self-hosting resolution.** 064 §22 and SC-064-D already assign the set to rows 074 and 075
  and the pairs to 064 ↔ 075. This contract specifies; it does not reopen.

Membership is never inferred from a filename, a neighbouring Roadmap row, the Blueprint's earlier
roster, symmetry with other models, or a name ending in *-DEFINITION*. A label that is not one of
064's fourteen Kinds is not a subject of this set.

## 6. Hard Dependency — Artifact 069, the Member Structure

`H: 069` is consumed unchanged. Every member conforms to Artifact 069, the generic structural
contract for every `KIND-DEFINITION` Record. Under 069 a member carries ten elements:

```
ENVELOPE  partition · kind · object_id · slug · provenance · registry_ref · sot_class
FAMILY    subject_model · subject_kind · definition
```

For this set, 069's constraints take these values. None is a new rule; each is 069's own constraint
applied to the Registry's subjects.

| 069 element | Value or rule for every member of this set | 069 check |
|---|---|---|
| `partition` | R | NATIVE |
| `kind` | the Registry Kind `KIND-DEFINITION`, symbolically — the member's own Kind | NATIVE |
| `object_id`, `slug`, `provenance`, `registry_ref`, `sot_class` | as 069 requires; nothing fixed here | NATIVE (presence) |
| `subject_model` | R | NATIVE |
| `subject_kind` | exactly one of the fourteen names of §8, as RMS §10.1 writes it | NATIVE (form) · EXTERNAL (declared status) |
| `definition` | present, single, non-empty; the governed Kind-level meaning of the subject | NATIVE · EXTERNAL (content limits) |

**Declared status of the subjects.** 069 checks a subject Kind's declared status EXTERNALLY, with
the proof supplied by the owning model's Kind architecture (069 §3; SC-069-F). For this set the
owning model is the Registry, and its Kind architecture is RMS §10.1 and Artifact 064 §6. 069's own
decision case for the self-hosted member names that evidence: *"declared status: RMS §10.1; 064"*.

**No variant.** There is no self-hosting schema, no bootstrap variant of `KIND-DEFINITION`, no
relaxed rule for any member and no added element. The same 069 contract applies to all fourteen,
including the member whose subject is `KIND-DEFINITION` (§11). If 069's live representation and
this table differ, 069 governs.

## 7. AD-LS1-R-BOOTSTRAP — the Binding Author Revision

**Source fact.** Roadmap §0.7: *"Rows 064 to 069 left the Registry's own fourteen Kinds without the
concrete KIND-DEFINITION partners LS-1 requires; every other model has a Kind-Definition set (178,
257, 300, 345, 364)."* Rows 074 and 075 now own that partner: *"074 specifies the Registry
self-definition set and is not itself an LS-1 member"*, and 075 *"authors the fourteen
KIND-DEFINITIONs"* and is the LS-1 partner, *"so the Registry's own pairs are 064 ↔ 075"*.

Preserved exactly:

1. Rows 064 to 069 left the Registry's own fourteen Kinds without concrete partners.
2. Rows 074 and 075 were reassigned to close that gap.
3. Row 074 specifies the set, is not an LS-1 member, and carries `LS: —`.
4. Row 075 authors the fourteen `KIND-DEFINITION`s and carries `LS: LS-1`.
5. The Registry's own LS-1 pairs are **064 ↔ 075**.
6. Row 068 remains the generic `KIND-DEFINITION` family.
7. Row 069 remains the generic schema every concrete `KIND-DEFINITION` Record conforms to.
8. 068 ↔ 069 is not a Registry Kind ↔ `KIND-DEFINITION` pair.
9. 074 ↔ 075 is not an LS-1 pair.
10. The ordering exception *"changes order only"* (Artifact 003; Roadmap §0.7).
11. The fourteen partners remain mandatory, *"as authored sources, before exit-P3 and G-REG
    (rows 123, 124)"* (Roadmap §0.7).
12. *"No Kind is added"* (Roadmap §0.7).
13. *"SEMANTIC-DEFINITION is withdrawn as a family"* (Roadmap §0.7), and is not resurrected (§17).

The live Roadmap matches this record; no difference was found.

## 8. The Fourteen-Member Roster

**Source fact.** RMS §10.1 and Artifact 064 §6. Exact spelling, capitalization and hyphenation; RMS
order.

| # | Required `subject_kind` | Blueprint §13.6 alias, where one exists (not a further member) |
|---|---|---|
| 1 | `MODEL-DEFINITION` | — (FG-V7-07; closed by RMS §10.1) |
| 2 | `KIND-DEFINITION` | `KIND-DEF` |
| 3 | `SUBTYPE-DEFINITION` | `SUBTYPE-DEF` |
| 4 | `FIELD-DEFINITION` | `FIELD-DEF` |
| 5 | `SCHEMA-DEFINITION` | — |
| 6 | `RELATIONSHIP-TYPE-DEFINITION` | `RELATIONSHIP-TYPE-DEF` |
| 7 | `CONTROLLED-VOCABULARY` | `CONTROLLED-VOCABULARY` |
| 8 | `IDENTITY-GRAMMAR` | `IDENTITY-GRAMMAR` |
| 9 | `WSVR-INDICATOR-DEFINITION` | `WSVR-INDICATOR-DEF` |
| 10 | `VALIDATION-RULE` | `VALIDATION-RULE` |
| 11 | `CONSTRAINT-DEFINITION` | — |
| 12 | `CAPABILITY-DEFINITION` | — |
| 13 | `DERIVATION-RULE` | `DERIVATION-RULE` |
| 14 | `SIMULATION-MODEL-DEFINITION` | `SIMULATION-MODEL-DEF` |

The members' subjects are written with the RMS §10.1 names. The Blueprint aliases are source
aliases of those names (064 §5), never further subjects, and a member is not written with an alias
in place of its RMS name. Where the Blueprint's earlier ten-item roster lacks a Kind — rows 1, 5,
11 and 12 — RMS §10.1 governs (SC-074-C, SC-074-G).

## 9. Set Cardinality and the One-to-One Correspondence

**Required synthesis.** Call *R-Kinds* the fourteen names of §8 and *the set* the `KIND-DEFINITION`
Records row 075 authors as the Registry's partners. Each member has exactly one `subject_kind`
(069 C-069-03). The set conforms only when all of the following hold together:

| # | Invariant |
|---|---|
| 1 | the set has exactly fourteen members |
| 2 | the members have exactly fourteen distinct `subject_kind` values |
| 3 | the set of `subject_kind` values equals R-Kinds exactly |
| 4 | every R-Kind is the subject of exactly one member — none twice, none missing |
| 5 | no member's subject lies outside R-Kinds |
| 6 | every member has `subject_model` R |
| 7 | every member is a `KIND-DEFINITION` Record (partition R, `kind` `KIND-DEFINITION`) |
| 8 | every member conforms to Artifact 069 |

Together these make the map from member to subject a one-to-one correspondence onto R-Kinds: each
Registry Kind has exactly one member and each member defines exactly one Registry Kind.

**Count alone proves nothing.** Fourteen members with a duplicate subject and a missing Kind have
the right count and the wrong set; so do thirteen correct members plus one about an invented Kind.
Invariants 2 to 5 are what make the count meaningful. A set of thirteen or fifteen fails invariant 1
before any other is examined.

**What the set is.** The set is the Registry's LS-1 partner set as row 075 authors it. How a later
revision of one member is represented — and whether it is a new Record — is rows 108–110's; this
contract neither counts a revision as a further member nor decides that it is not (SC-074-L).

## 10. Per-Member Contract Matrix

Each row is an **obligation**, not a Record. *Semantic source* names where Artifact 064 states what
a Record of the subject Kind is: its section, question 1 (semantic object) and question 2 (semantic
question). Each member's `definition` must express what a Record of its subject Kind is — the
`KIND-DEFINITION` family's content (069 §3) — within that source. Every row's structural contract is
Artifact 069, and every row's 075 obligation is the same: **author exactly one member with this
subject.**

| # | `subject_model` | `subject_kind` | Semantic source in 064 — Q1 · Q2 |
|---|---|---|---|
| 1 | R | `MODEL-DEFINITION` | §8 — *"the governed definition of one declared Record Model"* · *"what is this Record Model, as the Registry defines it?"* |
| 2 | R | `KIND-DEFINITION` | §9 — *"the governed definition of what one Kind means"* · *"what is a Record of this Kind?"* |
| 3 | R | `SUBTYPE-DEFINITION` | §10 — *"the governed definition of one specialization of a Kind"* · *"what is true of this specialization of a Kind?"* |
| 4 | R | `FIELD-DEFINITION` | §11 — *"the governed definition of what a field means"* · *"what does this field mean, and over what domain?"* |
| 5 | R | `SCHEMA-DEFINITION` | §12 — *"the governed definition of a schema"* · *"what structure does this schema define — required fields, cardinality, constraints, applicable Model and Kind?"* |
| 6 | R | `RELATIONSHIP-TYPE-DEFINITION` | §13 — *"the governed definition of a relationship type, with its participant roles and owning role"* · *"what is this relationship type, and which role owns it?"* |
| 7 | R | `CONTROLLED-VOCABULARY` | §14 — *"a governed set of values or terms and their meaning"* · *"what does this value or term mean, for this Kind?"* |
| 8 | R | `IDENTITY-GRAMMAR` | §15 — *"the recorded identity grammar, with its partition roster and per-partition kind codes"* · *"what grammar, partitions and kind codes does identity use?"* |
| 9 | R | `WSVR-INDICATOR-DEFINITION` | §16 — *"the governed meaning of a world-state indicator"* · *"what does this indicator mean — type, unit, range, constraints, semantics?"* |
| 10 | R | `VALIDATION-RULE` | §17 — *"the governed definition of a checking mechanism or procedure"* · *"how is a condition checked?"* |
| 11 | R | `CONSTRAINT-DEFINITION` | §18 — *"the governed definition of a condition that must hold"* · *"what must hold?"* |
| 12 | R | `CAPABILITY-DEFINITION` | §19 — *"the semantic contract of one capability"* · *"what is this capability's contract?"* |
| 13 | R | `DERIVATION-RULE` | §20 — *"the governed rule by which derived state is computed"* · *"how is this derived state computed?"* |
| 14 | R | `SIMULATION-MODEL-DEFINITION` | §21 — *"the governed definition of a simulation model"* · *"how does an indicator behave — dependencies, equations, thresholds?"* |

**What the source obligation means (required synthesis).** For every member, row 075's
`definition`:

- expresses the governed Kind-level meaning of exactly its subject Kind — what a Record of that Kind
  is — and of no other Kind;
- stays within the responsibility and answers Artifact 064 freezes for that Kind (§8 to §21),
  including the family boundaries that section's question 13 draws against the other Kinds;
- obeys the `KIND-DEFINITION` family boundary of 068 as 069 encodes it — it is not admission
  rationale, not the subject Kind's schema, not runtime behaviour, and not another family's content
  (069 §3 `definition`; 068 KD-3, KD-6, KD-7, KD-9);
- does not merge another Registry Kind's semantics into its subject, and does not redefine the
  Registry taxonomy.

**What it does not mean.** The matrix quotes 064; it is not the definition. This contract writes no
member's `definition` and supplies no text for 075 to copy. 064's answers are the boundary 075's
content stays within, not the content itself (SC-074-I).

## 11. The Self-Hosted Member — `KIND-DEFINITION` About `KIND-DEFINITION`

The set contains exactly one member whose `subject_model` is R and whose `subject_kind` is
`KIND-DEFINITION`.

**Two roles, one value.** The member's envelope `kind` is `KIND-DEFINITION`, because every member
is a `KIND-DEFINITION` Record. Its `subject_kind` is `KIND-DEFINITION`, because the Kind it defines
is Registry Kind 2. The two elements hold the same value in different roles. 069 §1: *"Their values
coincide only in the one KIND-DEFINITION whose subject is the Kind KIND-DEFINITION itself"*.

```
KIND-DEFINITION                                   = Registry Kind 2 (RMS §10.1; 064 §9)
a KIND-DEFINITION Record about KIND-DEFINITION   = one Registry Record, a member of this set,
                                                    whose subject is Registry Kind 2
```

The Kind and the Record are two objects (064 §22). Both are the Registry's, because R is
sovereign; that does not make them one.

**An ordinary member (required synthesis).**

- It conforms to 069 exactly as the other thirteen do. No special schema, relaxed rule or added
  element applies.
- It is not an axiom Record, not a meta-Record outside the Registry, and not a first or root Record
  of any kind. RMS §10.4: there is *"no circular self-definition requirement"*.
- It needs no prior `KIND-DEFINITION` Record. What defines the `KIND-DEFINITION` family is Artifact
  068, and what gives its Records their shape is Artifact 069 — both authored sources, not Records:
  *"This document and 069 are authored sources, not Records, so no Record-level regress runs
  through them"* (068 §16).
- It involves no recursion at runtime. Self-hosting here is a constitutional bootstrap question,
  closed by RMS §10.4 — not a recursive semantic evaluation. No member is evaluated by evaluating
  another member.

Rejected as additions: `AXIOM`, `AXIOM-RECORD`, `BOOTSTRAP-KIND-DEFINITION`,
`META-KIND-DEFINITION`, an untyped first definition, a fifteenth Registry Kind, a relaxed schema for
the first definition, and a chain of definitions of definitions (§17).

## 12. The RMS §10.4 Bootstrap Boundary

**Source fact.** RMS §10.4, *"Bootstrap — CLOSED"* `AUTHOR-DECIDED`, closes FG-V7-05:

- *"The Bootstrap Meta-Contract is NOT a Record."* It is a constitutional bootstrap contract
  *"standing outside the ordinary Registry Record ontology"*, containing only partition · kind ·
  identity · core envelope · provenance · Registry reference.
- There is no special axiom Record, and *"There is no circular self-definition requirement."*
- *"Once Registry exists, its definitions follow normal Record semantics."*

**Use here.** This contract uses RMS §10.4 for one purpose: to establish that the self-hosted member
of §11 is an ordinary Record and that no prior definition, axiom or extra member is needed. The
Bootstrap Meta-Contract is not a member of this set, not a fifteenth Record, not a Registry Record
of any Kind, and not this document. This contract defines no schema for it, enlarges none of its
content, and specifies no bootstrap algorithm, sequence or runtime behaviour.

**Not decided here.** RMS §10.4's chain runs *constitution → Bootstrap Meta-Contract → first
Registry Record → Registry definitions → normal Record creation*. Which Record is the first Registry
Record, and in what order the members are created, committed or resolved, is not stated by any
source and is not decided here; it is not implied by the roster order (§16; SC-074-B).

**History.** Blueprint §13.6e left the question OPEN as FG-V7-05 — *"how Registry's own KIND-DEF is
defined without a prior KIND-DEF"*. RMS §10.4 closes it. The two are not averaged, and FG-V7-05 is
not reopened (SC-074-B).

## 13. LS-1 Role — 064 ↔ 075

**Source fact.** Roadmap PART III: *"every Kind spec ↔ its Registry KIND-DEFINITION. ATOMIC-PAIR."*
For the Registry, the author revision fixes the pairs: 064 ↔ 075 (§7).

| Row | Role | `LS` |
|---|---|---|
| 064 | the taxonomy half — the Kind specification for all fourteen Registry Kinds | `LS-1` |
| 074 | this contract — specifies what the 075 half must contain | `—` |
| 075 | the definition half — the fourteen `KIND-DEFINITION` sources | `LS-1` |
| 068; 069 | the generic family; the generic schema | `LS-1`, read as the family and schema every set uses (Roadmap §0.7) |

**What this contract is not.** It is no lockstep partner and none of the fourteen pairs; it makes
neither 068 nor 069 a pair member; it creates no dependency, reference or new lockstep class.
Lockstep is not a reference edge, not Kind admission and not an ownership transfer, and it does not
make 075 a canonical writer (Artifact 003; 064 §7).

**The ordering exception, order only.** Artifact 003 lets 064 precede 075 because the generic
`KIND-DEFINITION` mechanism cannot exist before the taxonomy that makes `KIND-DEFINITION`
meaningful. *"The partner obligation is not waived."* *"No other LS-1 pair, and no other lockstep,
receives this exception. It changes order only; it does not allow lockstep partners to land whenever
convenient."* It does not mean that a Registry Kind may lack its definition, that LS-1 is optional
for R, that a Kind may generally be declared without a definition, that any other model receives a
bootstrap exception, that row 075 may be skipped, or that this contract stands in for the missing
partners. Row 123 — *"no unpaired lockstep member"* — and row 124 cannot pass until row 075 lands.

## 14. The Split Between 074 and 075

| | Artifact 074 — this contract | Artifact 075 |
|---|---|---|
| what it is | the set contract | the fourteen `KIND-DEFINITION` sources |
| path | `docs/registry/registry_kind_definition_set.md` | `docs/registry/registry_kinds/` |
| `T` · `R` | doc · ARCH | schema · CONTRACT |
| `Canon` · `CD` | n/a · no | canonical-about-meaning · yes |
| `H` | 064, 069 | 074, 069 |
| `LS` | — | LS-1 |
| owns | membership, cardinality, correspondence, subject model, 069 conformance requirement, semantic source per member, exclusions | each member's concrete content, including its `definition`; how the members are packaged |
| writes | this file only | its own sources only — never `canon/**` |

Example: this contract states that exactly one member's subject is `CONTROLLED-VOCABULARY`, that
its `subject_model` is R, that it conforms to 069, and that its definition stays within 064 §14.
Row 075 writes that member. This contract does not.

**Packaging is 075's.** Row 075 targets a directory. No source fixes whether its fourteen members
are fourteen files or fewer, what they are named, what extension they carry, how they are ordered or
whether a manifest accompanies them; no repository convention for such a set exists yet. This
contract imposes none (SC-074-M).

## 15. Canonicalization and Mutation Boundary

**Source fact.** Roadmap §0.8 (AD-REG-AUTHORING-SPLIT): P3 authors *"canonicalization source
material outside `canon/**`"*; canonicalization sources, row 075 among them, *"move to
`docs/registry/`"*; *"its Records are committed through 152 after G-CANON-R, before any canonical
Record resolves against them (X-05). An authored source is not a Record and is not canon."* Row
124's G-REG licenses consumption: *"no canonical Registry write is licensed (G-CANON-R)"*.

- **This contract** is `Canon: n/a` and `CD: no`: not canonical-about-meaning content, no
  canonicalization source, no member, no identifier, nothing under `canon/**` or
  `docs/registry/registry_kinds/`.
- **Row 075** is `Canon: canonical-about-meaning` and `CD: yes`. It authors the members as the
  canonicalization source of `canon/registry/registry_kinds/`. An authored member is not yet a
  committed Registry Record and is not canon.
- **Row 152**, the Mutation Coordinator, is the only writer of `canon/**`. It commits the members
  only after G-CANON-R.

Neither row 075's metadata nor the members' eventual canonicality changes this contract's
`Canon: n/a` or `CD: no`.

## 16. Reference, Envelope and Universal Boundaries

**References.** Row 074's own `Val` is set-level and is not rewritten to add Artifact 063's wording.
Every member, however, conforms to 069, and through it to 069's reference rules: `subject_kind` is
a declaration reference to a declared Kind of the Registry (Artifact 063 §7 row 3, §8.3) — never a
domain instance, a runtime object, a Registry Record identifier, a subtype or a field; no generic
reference list is carried; a legal reference creates no dependency and transfers no ownership or
authority; resolution does not prove legality (069 §5; Artifact 063 §11, §12). This contract adds no
reference requirement to 069 and is not a reference schema.

**Envelope.** This document is not a Record and has no envelope. Each member carries the universal
seven-field envelope because 069 requires it. No set-level, bootstrap or ordinal field is added to
the members or to the envelope (RMS §4).

**Order.** The tables follow RMS §10.1 order for auditability. The roster position is presentation
order only: it is not a member's `object_id`, not a version, not a file name, not a load, creation,
resolution or commit order, and not a priority. Each member's identity is its own, under 069 and the
universal grammar.

**Universal prohibitions.** None of RMS §4's nine prohibited universal semantics is introduced. The
fourteen Registry Kinds are the Registry's model-owned taxonomy, not a universal Kind taxonomy that
W, E, P, V or I inherit; the set makes the Registry no superclass or super-model; it adds no
universal Record base, Relationship Record, History Record, lifecycle, canonicality, identity
composition, state model or semantic schema.

**Definition boundaries still hold.** Every member defines one already-declared Registry Kind; it
does not declare or admit that Kind, is not the Kind, is not the Kind's schema or specification,
creates no Record of the Kind, owns no domain or runtime instance, transfers no taxonomy ownership,
and creates no executable behaviour (068; 069 §3; 064 §22).

## 17. No Fifteenth Kind — Prohibited Additions

**Source fact.** Row 074: *"no extra Kind is created"*. RMS §10.1 closes the taxonomy at fourteen.
Artifact 064 §23: *"An artifact name is not evidence of a Kind"*.

None of the following is a member or a subject of this set:

| Excluded | Why |
|---|---|
| a fifteenth `subject_kind` of any name | RMS §10.1; 064 §6 |
| `SEMANTIC-DEFINITION` | corresponds to no RMS §10.1 Kind; withdrawn as a family by Roadmap §0.7 |
| `IDENTITY-DEFINITION` (083–084), `DERIVATION-DEFINITION` (094–095), `ROLE-BOUNDARY-DEFINITION` (101–102), `DEGRADED-MODE-DEFINITION` (103–104) | Roadmap artifact names, not Kinds (064 §23) |
| `DIAGNOSTIC-VOCABULARY` (105), `SIGNAL-CLASS` (106), `READER-ARCHETYPE` (107) | Roadmap artifact names, not Kinds (064 §23) |
| the Registry Kind-Definition set itself (075) | a set of Records, not a Kind (064 §23) |
| a Blueprint alias such as `KIND-DEF` written as a second subject | an alias of an RMS name (064 §5) |
| a subtype, a field, a capability name other than `CAPABILITY-DEFINITION` | not a Registry Kind |
| `AXIOM`, `AXIOM-RECORD`, `BOOTSTRAP-KIND-DEFINITION`, `META-KIND-DEFINITION`, an untyped first definition | RMS §10.4 |
| the Bootstrap Meta-Contract | constitutional, not a Record (RMS §10.4) |
| a Kind of W, E, P, V or I | outside `subject_model` R; that model's own set owns it (178, 257, 300, 345, 364) |

*"Registry architecture is frozen; Registry content is extensible."* (Blueprint §9.4) lets
definition content grow within the architecture. It does not let this contract add a member or a
Kind (064 §5). How a Kind could ever be added is row 459's.

**`SEMANTIC-DEFINITION`.** It is not a Registry Kind, not a fifteenth definition, and not the
subject of any member. This document is not a `SEMANTIC-DEFINITION` specification and row 075 is
not a `SEMANTIC-DEFINITION` schema. *"SEMANTIC-DEFINITION is withdrawn as a family; semantic
material no RMS §10.1 Kind maps remains unmapped until its owning contract resolves it."* (Roadmap
§0.7). No replacement family is invented.

## 18. Set Contract Rules

| ID | Rule | Basis |
|---|---|---|
| **RKS-074-01** | **Exact roster.** The set's subjects are exactly the fourteen Registry Kinds of Artifact 064 and RMS §10.1, written with their RMS names. | RMS §10.1; 064 §6; row 074 `Val` |
| **RKS-074-02** | **Exact cardinality.** The set has exactly fourteen `KIND-DEFINITION` members. | row 074 `Val`; row 075 `Val` |
| **RKS-074-03** | **One-to-one.** Each Registry Kind is the subject of exactly one member, and each member defines exactly one Registry Kind. | row 074 `Val` (*"one for each Kind of 064"*); 069 C-069-03; synthesis |
| **RKS-074-04** | **Registry scope.** Every member has `subject_model` R. | 064 §6; 069 §3 |
| **RKS-074-05** | **Structural conformance.** Every member conforms to Artifact 069, with no variant, relaxation or added element. | row 074 `H`; row 075 `Val`; 069 |
| **RKS-074-06** | **Record family.** Every member is a `KIND-DEFINITION` Record — partition R, `kind` `KIND-DEFINITION` — never a Record of its subject Kind. | 069 §2; 064 §22 |
| **RKS-074-07** | **No extra Kind.** No subject lies outside the fourteen, and no member creates or implies a fifteenth Kind. | row 074 `Val`; RMS §10.1; 064 §23 |
| **RKS-074-08** | **No duplicate, no missing subject.** Count alone does not satisfy the set; membership must be complete and unique. | §9; synthesis |
| **RKS-074-09** | **Self member.** Exactly one member defines the Registry Kind `KIND-DEFINITION`. | 064 §6 row 2; §11 |
| **RKS-074-10** | **Ordinary self-hosting semantics.** The member about `KIND-DEFINITION` follows ordinary 069 semantics. | RMS §10.4; 069 §1, §6; 068 §16 |
| **RKS-074-11** | **No axiom Record.** No bootstrap, axiom, meta or root Record joins the set. | RMS §10.4 |
| **RKS-074-12** | **Bootstrap Meta-Contract not a member.** It is constitutional, not a Record, and not one of the fourteen. | RMS §10.4 |
| **RKS-074-13** | **074 not LS-1.** This contract is not a lockstep member and carries `LS: —`. | Roadmap §0.7; row 074 |
| **RKS-074-14** | **The Registry pairs.** The taxonomy side is 064; the definition side is 075. | Roadmap §0.7, PART III; Artifact 003 |
| **RKS-074-15** | **No `SEMANTIC-DEFINITION`.** The withdrawn family is excluded and not replaced. | Roadmap §0.7 |
| **RKS-074-16** | **Semantic source.** Each member's definition stays within the responsibility and answers 064 freezes for its subject Kind. | 064 §8–§21; §10 |
| **RKS-074-17** | **No definition content here.** This contract specifies obligations; row 075 authors every member's content. | row 074 `Done`; row 075 |
| **RKS-074-18** | **No canonical write.** This contract creates no canonical data, no canonicalization source and no member. | row 074 `Canon`, `CD`; Roadmap §0.8 |
| **RKS-074-19** | **075 authoring split.** Row 075's members are committed only through 152 after G-CANON-R. | Roadmap §0.8; row 075 `Val` |
| **RKS-074-20** | **No packaging invented.** The set's semantics imply no file name, file count, extension, layout or manifest. | §14; row 075 |
| **RKS-074-21** | **No ordinal identity.** RMS roster order is not Record identity, version, load, creation, resolution or commit order. | §16 |
| **RKS-074-22** | **Hard dependencies preserved.** 064 and 069 are consumed unchanged, and no `H` or `S` edge is added. | row 074 |
| **RKS-074-23** | **No dependency asserted.** A member's existence creates no semantic dependency of its subject Kind's Records on it; whether one exists is not decided here. | SC-068-L; SC-069-J; row 111; SC-074-K |

## 19. Worked Examples

All examples are **schematic**: no identifier is minted, no Kind code is chosen, no definition text
is supplied, and nothing here is Registry data.

**A. Legal — the self-hosted member.** A member with envelope `kind` `KIND-DEFINITION`,
`subject_model` R, `subject_kind` `KIND-DEFINITION`, and a `definition` carrying the governed
meaning of Registry Kind 2 within 064 §9. It is an ordinary 069 Record: no prior axiom Record, no
special schema, no recursion at runtime (§11).

**B. Legal — `MODEL-DEFINITION`.** `subject_model` R, `subject_kind` `MODEL-DEFINITION`. It is a
member because RMS §10.1 lists it first — *"closes FG-V7-07 — the Kind exists"* — whatever the
Blueprint's earlier roster says. Defining `MODEL-DEFINITION` creates no seventh Record Model (064
§24 inference 13).

**C. Legal — `SIMULATION-MODEL-DEFINITION`.** `subject_model` R, `subject_kind`
`SIMULATION-MODEL-DEFINITION`, Registry Kind 14 and the fourteenth member. Its definition creates no
Simulation Record Model (064 §21; C-064-23).

**D. Illegal — duplicate and missing.** Fourteen members, two with `subject_kind` `KIND-DEFINITION`
and none with `FIELD-DEFINITION`. Rejected: invariants 2, 3 and 4 fail although the count is
fourteen (RKS-074-08).

**E. Illegal — a fifteenth subject.** A fifteenth member with `subject_kind`
`SEMANTIC-DEFINITION`. Rejected: not in the RMS §10.1 roster, withdrawn by Roadmap §0.7, and a
fifteenth member (RKS-074-02, RKS-074-07, RKS-074-15).

**F. Illegal — an axiom Record.** An `AXIOM-RECORD` added to *solve* self-hosting. Rejected: RMS
§10.4 — there is no axiom Record and no circular self-definition requirement (RKS-074-11).

**G. Illegal — the wrong subject model.** `subject_model` W, `subject_kind` `KIND-DEFINITION`.
Rejected from this set: every member's `subject_model` is R (RKS-074-04); and `KIND-DEFINITION` is
not a declared World Kind, which 069's EXTERNAL check rejects in any set.

**H. Illegal — a Record as the subject.** `subject_kind` written as a Registry Record identifier,
`R-<kind>-…`. Rejected: the subject is a Kind, not a Record — 069 rejects it NATIVE.

**I. Boundary — 074 and 075.** This contract states that one member, with `subject_model` R, has
`subject_kind` `CONTROLLED-VOCABULARY`, conforms to 069, and keeps its definition within 064 §14.
Row 075 authors that member's source. This contract writes none of it (§14).

**J. Boundary — order.** The tables list `MODEL-DEFINITION` first because RMS §10.1 does. That gives
its member no ordinal identity, no `object_id` 1, no priority and no obligation to be created,
committed or resolved first (§16).

## 20. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | Artifact 074 is itself a `KIND-DEFINITION` Record | it is a contract with no envelope | §2 |
| 2 | Artifact 074 is a member of the Registry self-definition set | it specifies the set | §2; Roadmap §0.7 |
| 3 | Artifact 074 is `LS: LS-1` | row 074 reads `LS: —` | row 074; §13 |
| 4 | 074 ↔ 075 is an LS-1 pair | the pairs are 064 ↔ 075 | Roadmap §0.7; §13 |
| 5 | 068 ↔ 069 is an LS-1 Kind pair | they are the generic family and schema | Roadmap §0.7; §7 |
| 6 | The Registry may omit its fourteen definitions because of bootstrap | the partners are not waived | Artifact 003; §13 |
| 7 | The ordering exception waives LS-1 | it changes order only | Artifact 003; §13 |
| 8 | `KIND-DEFINITION` needs a prior `KIND-DEFINITION` Record | 068 and 069 are authored sources, not Records | RMS §10.4; 068 §16; §11 |
| 9 | A special axiom Record is required | none exists | RMS §10.4 |
| 10 | The Bootstrap Meta-Contract is a Registry Record | it is NOT a Record | RMS §10.4 |
| 11 | The Bootstrap Meta-Contract is the fifteenth member | it is no member | RMS §10.4; §12 |
| 12 | `SEMANTIC-DEFINITION` is still a Registry Kind | withdrawn; no RMS §10.1 Kind | Roadmap §0.7; §17 |
| 13 | A name ending in *-DEFINITION* is a Registry Kind | a name is not evidence of a Kind | 064 §23 |
| 14 | The Blueprint's shorter roster overrides RMS §10.1 | RMS §10.1 is the final roster | 064 §5; SC-074-C |
| 15 | Registry content extensibility lets 074 add a fifteenth Kind | content grows within a frozen architecture | Blueprint §9.4; 064 §5 |
| 16 | Fourteen files prove the set correct | count alone proves nothing | §9 |
| 17 | Duplicate subjects are legal if the count stays fourteen | each Kind appears exactly once | §9; RKS-074-08 |
| 18 | A `KIND-DEFINITION` creates or adopts its subject Kind | definition is not admission | C-057-08; 064 §22 |
| 19 | A `KIND-DEFINITION` Record and the Kind it defines are one object | two objects | 064 §22; §11 |
| 20 | Defining the Registry's own Kinds grants the Registry its sovereignty | sovereignty is constitutional | RMS §10; Artifact 060 |
| 21 | The self member uses a special schema | ordinary 069 | §11; RKS-074-10 |
| 22 | A member may ignore 069 because it defines the Registry itself | every member conforms to 069 | RKS-074-05 |
| 23 | Roster ordinal is object identity | identity is each Record's own | §16; RKS-074-21 |
| 24 | Roster order is runtime load order | presentation order only | §16; RKS-074-21 |
| 25 | 074 may mint object IDs | it mints none | §2 |
| 26 | `Canon: n/a` may become canonical-about-meaning because the members eventually are | row metadata is preserved | row 074; §15 |
| 27 | `CD: no` may become yes because row 075 is `CD: yes` | row metadata is preserved | row 074; §15 |
| 28 | 074 may write `docs/registry/registry_kinds/` | that is 075's path | row 075; §14 |
| 29 | 074 may write `canon/registry/registry_kinds/` | only 152 writes `canon/**` | Roadmap §0.8; §15 |
| 30 | 075's authored source is canonical before 152 and G-CANON-R | an authored source is not a Record and is not canon | Roadmap §0.8; §15 |
| 31 | Lockstep is a reference edge | it is an authoring obligation | 064 §7; Artifact 003 |
| 32 | Lockstep transfers ownership | it transfers nothing | §13 |
| 33 | Concrete definition prose belongs in 074 | it is 075's | RKS-074-17 |
| 34 | 074 may redesign 069's elements | 069 is consumed unchanged | RKS-074-22 |
| 35 | Every Registry-definition-like Roadmap artifact joins the fourteen | membership is 064 equality | §17; 064 §23 |
| 36 | A member's existence makes Records of its subject Kind depend on it | not established; row 111 owns dependency rules | SC-074-K |
| 37 | The self member is RMS §10.4's *first Registry Record* | which Record is first is not decided | §12; SC-074-B |
| 38 | The ordering exception extends to W, E, P, V or I | Registry pairs only | Artifact 003 |

## 21. Source Conditions and Gaps

Each entry gives the source statements (or the missing source), the condition, whether this
artifact owns its resolution, and the treatment.

### SC-074-A — stale Registry classification — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* |
| **Source B** | RMS §10, COLLISION-1: *"Registry is a sovereign Record Model"*; the §9.4 line is *"stale and requires a Blueprint wording fix"*. |
| **Condition** | The Blueprint line classifies the Registry as a capability; the RMS makes it a sovereign Record Model. |
| **Owner** | Not this artifact — closed at source. |
| **Treatment** | The RMS governs: the members are Records of a sovereign Record Model. No Blueprint text is edited. |

### SC-074-B — Blueprint FG-V7-05 against RMS §10.4 — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §13.6e, *The bootstrap problem*: OPEN — *"how Registry's own KIND-DEF is defined without a prior KIND-DEF"*, recorded as FG-V7-05. |
| **Source B** | RMS §10.4, *"Bootstrap — CLOSED"* `AUTHOR-DECIDED`: the Bootstrap Meta-Contract is NOT a Record; no axiom Record; *"There is no circular self-definition requirement."* |
| **Condition** | The Blueprint left the question open; the RMS closes it. RMS §10.4 names a *first Registry Record* without saying which Record it is. |
| **Owner** | Not this artifact — closed at source. Which Record is first, and any creation order, is not this contract's. |
| **Treatment** | The self-hosted member is an ordinary member (§11, §12). The texts are not averaged; FG-V7-05 is not reopened; no first Record, creation order or bootstrap sequence is chosen. |

### SC-074-C — Blueprint FG-V7-07 and the earlier roster against RMS §10.1 — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §13.6 lists ten Registry kinds; §13.6e: *"OPEN — Registry's own taxonomy."* — a Record Model definition Kind *"not established by any source"* (FG-V7-07). |
| **Source B** | RMS §10.1: *"Final Kind taxonomy — CLOSED at fourteen"*, with `MODEL-DEFINITION` *"closes FG-V7-07 — the Kind exists"*; Artifact 064 §5 consumes it. |
| **Condition** | The Blueprint roster lacks `MODEL-DEFINITION`, `SCHEMA-DEFINITION`, `CONSTRAINT-DEFINITION` and `CAPABILITY-DEFINITION`. |
| **Owner** | Not this artifact — closed at source. |
| **Treatment** | The set follows the RMS and 064 fourteen. `MODEL-DEFINITION` is a member. The two rosters are not merged into a larger one. |

### SC-074-D — AD-LS1-R-BOOTSTRAP — CLOSED BY AUTHOR DECISION

| | |
|---|---|
| **Source A** | Roadmap PART III: LS-1 pairs every Kind specification with its Registry `KIND-DEFINITION`; the earlier decomposition gave the Registry no concrete partners (Roadmap §0.7; Revolving Resolution Note, CONFLICT-E). |
| **Source B** | Roadmap §0.7 and Artifact 003: row 074 specifies the set (`LS: —`); row 075 authors the fourteen (`LS: LS-1`); the pairs are 064 ↔ 075; the exception changes order only. |
| **Condition** | — |
| **Owner** | The author; decided. |
| **Treatment** | Preserved exactly (§7, §13). |

### SC-074-E — `SEMANTIC-DEFINITION` — WITHDRAWN AT SOURCE

| | |
|---|---|
| **Source A** | Rows 074–075 formerly described a `SEMANTIC-DEFINITION` specification and schema corresponding to no RMS §10.1 Kind. |
| **Source B** | Roadmap §0.7: *"SEMANTIC-DEFINITION is withdrawn as a family"*. |
| **Condition** | — |
| **Owner** | The author; decided. |
| **Treatment** | Not a member and not a Kind; not resurrected; no replacement family is invented; unmapped semantic material stays with its owning contract (§17). |

### SC-074-F — RR-16 text unavailable — SOURCE GAP

| | |
|---|---|
| **Source A** | Row 074: `Req: RR-16`. |
| **Source B** | Missing — the requirement register is not in the source set (GAP-C). |
| **Gap** | The requirement's text cannot be read. |
| **Owner** | Not this artifact. |
| **Treatment** | The ID is carried exactly; no requirement text is stated and no compliance with unread text is claimed. Non-blocking. |

### SC-074-G — Blueprint aliases — CLOSED AT SOURCE

| | |
|---|---|
| **Source A** | Blueprint §13.6 writes `KIND-DEF`, `SUBTYPE-DEF`, `FIELD-DEF`, `RELATIONSHIP-TYPE-DEF`, `WSVR-INDICATOR-DEF`, `SIMULATION-MODEL-DEF`. |
| **Source B** | RMS §10.1 names; Artifact 064 §5: the abbreviations *"are source aliases of the RMS names, not further Kinds"*; row 075 `Val`: *"names match the RMS §10.1 roster exactly"*. |
| **Condition** | Two spellings for one Kind. |
| **Owner** | Not this artifact — closed by 064. |
| **Treatment** | Members are written with the RMS names; an alias is never a second subject (§8). |

### SC-074-H — authoring against canonical materialization — CLOSED BY AUTHOR DECISION

| | |
|---|---|
| **Source A** | Row 075 is `Canon: canonical-about-meaning` · `CD: yes`, the canonicalization source of `canon/registry/registry_kinds/`. |
| **Source B** | Roadmap §0.8: *"An authored source is not a Record and is not canon."*; 152 commits after G-CANON-R. |
| **Condition** | — |
| **Owner** | The author; decided. |
| **Treatment** | This contract writes no member; row 075's source is not a committed Record; 152 commits after G-CANON-R (§15). |

### SC-074-I — per-member definition content — BOUNDED

| | |
|---|---|
| **Source A** | Artifact 064 §8–§21 gives each Kind's responsibility and answers; Artifact 069 gives the structure; row 075 authors the members. |
| **Source B** | No source states the final definition text of any member. |
| **Condition** | The content each member must carry is bounded but not written by any current source. |
| **Owner** | Row 075. |
| **Treatment** | §10 hands row 075 the semantic source per member; no definition text is written here. Non-blocking. |

### SC-074-J — non-roster definition-like artifacts — CLOSED BY 064

| | |
|---|---|
| **Source A** | Rows 083–084, 094–095, 101–107 carry definition-like or vocabulary-like names outside RMS §10.1. |
| **Source B** | Artifact 064 §23 and SC-064-E: none is a Kind; their representation is their own rows'. |
| **Condition** | — |
| **Owner** | Not this artifact. |
| **Treatment** | None is added to the set (§17). Their metadata is not repaired here (SC-064-J). |

### SC-074-K — L1-family Records and their Kind's KIND-DEFINITION — SOURCE GAP, ROUTED HERE

| | |
|---|---|
| **Source A** | Artifact 062 places `KIND-DEFINITION` at L2 and field, relationship-type and indicator definitions at L1; L1 does not depend on L2 (D-8). This set includes members whose subjects are those L1 families. |
| **Source B** | 068 SC-068-L and 069 SC-069-J record as not established whether a Record of an L1 family's Kind semantically depends on that Kind's `KIND-DEFINITION`, and route the question to row 074 (*"self-hosting follows RMS §10.4"*) and row 111 (*"downward-only; asymmetric; no cycles"*). |
| **Gap** | Whether such a dependency exists, and how it would stand with D-8. |
| **Owner** | The answer is row 111's; the RMS §10.4 part is this contract's. |
| **Treatment** | This contract's part: RMS §10.4 makes every member an ordinary Record and requires no circular self-definition, so the set itself needs no dependency of any Record on any member (§11, §12). This contract asserts no dependency, invents no exemption from D-8, and places no member in a layer beyond 062. Whether a dependency exists is row 111's. Non-blocking for row 074's `Val` and `Done`. |

### SC-074-L — set identity across Registry evolution — SOURCE GAP

| | |
|---|---|
| **Source A** | Rows 074 and 075 specify and author exactly fourteen members. |
| **Source B** | Rows 108–110 own Registry evolution, versioning, supersession and deprecation; no representation exists yet. |
| **Gap** | Whether a later revision of a member is a new Record, and whether it then counts toward the fourteen. |
| **Owner** | Rows 108–110. |
| **Treatment** | The set is specified as row 075 authors it. No version, revision or supersession rule is decided here, in either direction (§9). Non-blocking. |

### SC-074-M — packaging of the set — NOT ESTABLISHED

| | |
|---|---|
| **Source A** | Row 075 targets the directory `docs/registry/registry_kinds/`. |
| **Source B** | No source and no existing repository convention fixes file count, names, extensions, ordering or a manifest for an authored set of definitions. |
| **Condition** | — |
| **Owner** | Row 075. |
| **Treatment** | No packaging is imposed (§14; RKS-074-20). Non-blocking. |

## 22. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-074-01** | **Exact member count.** The specified set has exactly fourteen members. | §9; RKS-074-02 |
| **C-074-02** | **Exact distinct-subject count.** It has exactly fourteen distinct subject Kinds. | §9 |
| **C-074-03** | **Exact roster equality.** The subject set equals the RMS §10.1 / 064 roster exactly, in exact spelling. | §8; RKS-074-01 |
| **C-074-04** | **Subject model.** Every member's `subject_model` is R. | §6; RKS-074-04 |
| **C-074-05** | **Member family.** Every member is a `KIND-DEFINITION` Record. | §6; RKS-074-06 |
| **C-074-06** | **069 conformance.** Every member must conform to the current Artifact 069. | §6; RKS-074-05 |
| **C-074-07** | **No missing Kind.** Every 064 Kind has one member. | §9 |
| **C-074-08** | **No duplicate Kind.** No 064 Kind has more than one member. | §9; RKS-074-08 |
| **C-074-09** | **No extra subject.** No subject outside the 064 roster is present. | §9, §17; RKS-074-07 |
| **C-074-10** | **`MODEL-DEFINITION` included**, whatever the earlier Blueprint roster says. | §8; SC-074-C |
| **C-074-11** | **Self member included.** One ordinary member about `KIND-DEFINITION` is required. | §11; RKS-074-09, RKS-074-10 |
| **C-074-12** | **No axiom Record.** No bootstrap or axiom member exists. | §11; RKS-074-11 |
| **C-074-13** | **Bootstrap Meta-Contract excluded.** It is constitutional, not a Record and not a member. | §12; RKS-074-12 |
| **C-074-14** | **No fifteenth Kind** is implied or adopted. | §17 |
| **C-074-15** | **No `SEMANTIC-DEFINITION`.** | §17; RKS-074-15 |
| **C-074-16** | **074 LS metadata.** This artifact remains `LS: —`. | header; §13 |
| **C-074-17** | **The Registry LS-1 pairing** is 064 ↔ 075. | §7; §13 |
| **C-074-18** | **Generic family and schema separated.** 068 and 069 remain the generic family and schema, not pair members. | §7; §13 |
| **C-074-19** | **No concrete data.** No member Record or source is authored. | §2; §14 |
| **C-074-20** | **Canon and CD.** This artifact remains `Canon: n/a`, `CD: no`. | header; §15 |
| **C-074-21** | **Downstream handoff.** Row 075 receives exact membership and the semantic source of every member. | §10; §23 |
| **C-074-22** | **No packaging invented.** No file naming, count or layout is imposed on 075. | §14; SC-074-M |
| **C-074-23** | **Source gaps preserved.** RR-16's text and every other open condition are recorded, not invented away. | §21 |
| **C-074-24** | **Mutation scope.** Only `docs/registry/registry_kind_definition_set.md` is created by this artifact. | row 074 |
| **C-074-25** | **Header.** The header reproduces row 074's metadata exactly. | row 074 |
| **C-074-26** | **Dependencies consumed.** 064 and 069 are consumed unchanged; no `H` or `S` edge is added. | §5; §6; RKS-074-22 |
| **C-074-27** | **No ordinal identity.** Roster order is not identity, version or any operational order. | §16; RKS-074-21 |
| **C-074-28** | **No universal taxonomy.** The fourteen stay the Registry's own taxonomy; none of RMS §4's nine prohibited universal semantics is introduced. | §16 |
| **C-074-29** | **No dependency asserted.** The L1 dependency question routed by 068 and 069 is recorded, not decided. | SC-074-K; RKS-074-23 |
| **C-074-30** | **Ordering exception bounded.** The exception changes order only and applies to the Registry's fourteen pairs only. | §13 |

## 23. Handoff to 075

Row 075: *"exactly fourteen KIND-DEFINITIONs, one per Registry Kind of 064; all conform to 069;
names match the RMS §10.1 roster exactly; no extra definition implies a fifteenth Kind"*, authored
as the canonicalization source of `canon/registry/registry_kinds/` and *"committed only through 152
after G-CANON-R"*; `Done`: *"fourteen"*.

Row 075 may take from this contract, without redesign:

- the exact fourteen subject names, in RMS spelling (§8);
- `subject_model` R for every member (§6; RKS-074-04);
- the one-to-one correspondence and its eight invariants (§9);
- conformance to 069 for every member, with no variant (§6; RKS-074-05);
- the semantic source of each member's definition (§10);
- the self-hosted member as an ordinary member (§11);
- no axiom Record, no Bootstrap Meta-Contract member, no fifteenth Kind, no `SEMANTIC-DEFINITION`
  (§11, §12, §17);
- the authoring and canonical-materialization boundary (§15).

**Not handed on.** No file name, file count, layout, object ID, Kind code, load, creation or commit
order, version field, reference list, test, or definition beyond the fourteen is required by this
contract. Row 075 does not have to implement a resolver, create version history, write `canon/**`,
add a bootstrap definition, add a separate `MODEL-DEFINITION` set, define the Registry's fields,
schemas or vocabularies, or add a dependency its row does not list. Row 075's `Val` and `Done` are
not enlarged. Rows 114, 123, 124 and 152 consume the result under their own rows; nothing here
builds them.

## 24. Roadmap Completion Trace

The statuses below assess Artifact 074 as a documentation contract (`T: doc`, `R: ARCH`).
**SPECIFICATION OBLIGATION SATISFIED** means the required rule is stated, mandatory, and bounded by
its governing sources. It does not claim that row 075's members exist or that any lockstep or
conformance test has run.

| Row 074 | Status | Where it is met |
|---|---|---|
| `Val`: *"the concrete Registry self-definition set is specified as exactly fourteen KIND-DEFINITION Records"* | **SPECIFICATION OBLIGATION SATISFIED** — fourteen members; the eight invariants of §9 | §8, §9; RKS-074-01 to RKS-074-08 |
| `Val`: *"one for each Kind of 064"* | **SPECIFICATION OBLIGATION SATISFIED** — one-to-one onto 064's roster; `subject_model` R; semantic source per member | §9, §10; RKS-074-03, RKS-074-16 |
| `Val`: *"self-hosting follows RMS §10.4"* | **SPECIFICATION OBLIGATION SATISFIED** — ordinary self member; Bootstrap Meta-Contract not a Record and not a member; no axiom Record; no circular self-definition | §11, §12; RKS-074-09 to RKS-074-12 |
| `Val`: *"no extra Kind is created"* | **SPECIFICATION OBLIGATION SATISFIED** — no fifteenth subject; non-roster names, aliases, `SEMANTIC-DEFINITION` and bootstrap Records excluded | §17; RKS-074-07, RKS-074-15 |
| `Done`: *"contract"* | **SATISFIED** — the set contract exists at its Roadmap path | this document |
| `H: 064,069` | **SATISFIED** — membership from 064, structure from 069, both consumed unchanged | §5, §6 |
| `LS: —` | **PRESERVED** — not a lockstep member; the pairs are 064 ↔ 075 | §7, §13 |
| `Why`: *"specifies the Registry half of the Registry's own LS-1 pairs"* | **SATISFIED** — the Registry definition-side set is specified for row 075 | §1, §13, §23 |
| `→ 075` | **SATISFIED** — handoff stated without enlarging row 075 | §23 |

No member, Record, identifier, Kind code, schema or canonical data created. No Kind added. The
fourteen `KIND-DEFINITION` partners are owed by row 075; this contract does not claim they exist.

---

*Artifact 074 · P3/3b · Own: R · SoT: AUTHORITATIVE · Auth: defining · Canon: n/a. This document
specifies the Registry self-definition set from Record Model System §10.1 and §10.4, Roadmap row
074, §0.7 and §0.8, and Artifacts 064 and 069. It is not a Registry Record, holds no canonical data,
authors no member, defines no schema or algorithm, and implements nothing. Where it differs from the
Master Blueprint, the Record Model System, or the OS File Build Roadmap, those governing sources are
correct and this document is wrong.*
