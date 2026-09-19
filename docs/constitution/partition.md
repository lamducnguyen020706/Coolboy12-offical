# COOLBOY12 — Partition Ownership

**Artifact 045** · partition ownership · `docs/constitution/partition.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P2/2b · Req: BR-17 · BP: §13.6 · RMS: §2 ·
H: 039 · S: — · LS: — · G: — · → 046 ·
Val: exactly one partition per Record; conversion prohibited ·
Done: stated · Why: I-16 · Risk: medium · ∥: yes

> **On the name of the `V` partition.** I-16 names it **Visual Library**; RMS §2 and RMS §6 name
> it **Visual**; Blueprint §13.6 heads its row *"Visual Library `V`"*. These are two names used by
> the sources for **one** partition, whose code is `V` and whose sovereign Record Model is the
> Visual Record Model. Both names are recorded here and **neither source is silently corrected**,
> because neither is this artifact's to amend.

> **On the scope of the conversion prohibition.** I-16 states it without qualification —
> *"Cross-partition conversion is prohibited"* — and Blueprint §13.6 restates it without
> qualification: *"**Cross-partition conversion is prohibited** (Section 12.13)."* Blueprint
> §12.13's `Convert` row names a subset in parentheses — *"Conversions across partitions (World ↔
> Production ↔ Epistemic) are prohibited — those are a retire-and-create"* — and states no
> restriction to those three. This artifact implements the **unqualified** rule that I-16 and
> §13.6 both state, and records §12.13's parenthesis as illustrative rather than as a limiting
> enumeration. The discrepancy is recorded, not resolved here.

## 1. Purpose

Row 045 states this artifact's reason in three characters: **I-16.**

> **I-16** *(amended v0.6.1; amended in wording v0.7.0)* — *"Every Record carries exactly one
> partition — World, Epistemic, Production, Registry, Visual Library, or Issue — and every
> partition owns exactly one sovereign Record Model. Cross-partition conversion is prohibited."*
> (Blueprint §13.6, §13.6a, §13.6c, §13.2)

Artifact 041 made the **first** clause of I-16 buildable as a sovereignty rule — one partition
owns exactly one sovereign Record Model — and explicitly deferred the remainder: *"The partition
ownership contract is **Artifact 045**. Cross-partition conversion, partition mechanics, storage,
schema, and operational transitions are its to state — including the remainder of I-16"*
(Artifact 041 §9). This document states that remainder as a contract: explicit rules, an explicit
prohibition, and conditions that can be checked.

It adds no architecture. Every rule below is a contractual formulation of what Blueprint §13.6,
Blueprint §12.13, RMS §2, RMS §6.1 and I-16 already establish.

## 2. Constitutional Status

This document is AUTHORITATIVE about **partition ownership of a Record** and about nothing else.
It **derives** that rule from the Master Blueprint and the Record Model System; it does not amend,
supersede, or outrank either.

Where this document and the Master Blueprint, the Record Model System, or the OS File Build
Roadmap differ, **they are right and this document is wrong.**

It is not a Record, holds no canonical data, and is `Canon: n/a`. `SoT: AUTHORITATIVE` here means
authoritative **about architecture**, never World Canon (Blueprint §13.0, I-104).

## 3. Scope

**In scope.** Which partition owns a Record; that the number of owning partitions is exactly one;
that each partition owns exactly one sovereign Record Model; that the Record's semantic ownership
follows from that model; that a Record does not convert across a partition boundary; and that a
reference or dependency across a boundary transfers no ownership.

**Out of scope.** Everything a Record Model owns about its Records, plus all matters listed in
§16. This contract says **which model owns a Record**. It says nothing about what that model then
does with it.

## 4. The Governing Rule

```
Record  ──belongs to──▶  EXACTLY ONE partition  ──owns──▶  EXACTLY ONE sovereign Record Model
```

Blueprint §13.6, stated at source:

> *"**The correction: every record coolboy12 holds is a Record, every Record belongs to exactly
> one partition, and every partition owns exactly one sovereign Record Model.** A Record Model is
> not a specialization of a universal model and does not inherit from one."*

RMS §6.1 states the same chain from the category side: a **Record** is *"a persistent,
identity-bearing unit owned by exactly one Record Model."*

The chain is read in one direction and has no second reading. A Record does not belong to two
partitions; it does not belong to none; it does not belong to a partition weakly, by convention,
by convenience, or by where it happens to be stored. **The partition is a required property of
every Record, and it names which Record Model owns that Record** (Blueprint §13.1, §13.6).

## 5. The Six Partitions

Exactly six, per RMS §2: *"Exactly **six sovereign Record Models**: **W** World · **E** Epistemic ·
**P** Production · **R** Registry · **V** Visual · **I** Issue. No model is a superclass of
another. World is not a template."*

| Partition | Sovereign Record Model | The question it alone answers (RMS §6) |
|---|---|---|
| **`W`** | World Record Model | What is true of the world? |
| **`E`** | Epistemic Record Model | Who knows, believes, suspects, or has been shown what? |
| **`P`** | Production Record Model | What is intended, planned, coordinated, and in production? |
| **`R`** | Registry Record Model | What does the system mean, and how are Record semantics defined? |
| **`V`** | Visual Record Model | How is World Truth visually specified and represented? |
| **`I`** | Issue Record Model | What was published, and how is that publication composed? |

**Six at v1.0.** At v1.0 the Record System consists of exactly these six sovereign partitions —
W, E, P, R, V and I — and RMS §25 concludes: *"**NO SEVENTH SOVEREIGN RECORD MODEL IS REQUIRED AT
v1.0.**"* No partition is a specialization of another (I-101, Artifact 041).

**That is a statement of the v1.0 architecture, not a claim about every future revision.** The
sources scope it that way and this contract does not extend them: RMS §25 says *required at v1.0*,
and whether the architecture is ever amended is a matter for the constitutional amendment
ceremony, not for this contract. What binds now is the six at v1.0 and the sovereignty rule that
governs them.

**The partitions do not collapse.** Blueprint §13.6 states the partition test — *"If every record
in this partition vanished, what would be lost?"* — and its conclusion: *"Only the first is the
world, and that asymmetry is why the partitions cannot be collapsed."*

This table names the six and their models. It does **not** restate any model's kind roster: those
are stated once, at Blueprint §13.6, and each roster is its model's own (I-106).

## 6. The Ownership Model

**Ownership is semantic.** Artifact 041 §9 fixes this reading: *"Partition ownership here is
**semantic** ownership only: it makes no claim that a partition is one implementation class,
schema, file, table, or store."* This contract carries that reading forward unchanged and extends
it to the Record.

What the owning partition's Record Model owns about a Record is what Artifact 042 enumerates — its
Kind taxonomy, identity semantics, state and lifecycle, relationship packaging, temporal
architecture, provenance meaning, canonicality meaning (if any), semantic validation, and package
composition (RMS §6). **This contract determines *which* model that is, and determines none of
those nine things.**

**Ownership is exclusive.** One owner, always. A second model does not become a co-owner of a
Record by referencing it, by depending on it, by deriving from it, by publishing it, by
describing it, or by sharing a mechanism with the model that owns it (I-103, Artifact 043).

## 7. Ownership Invariants

These five are the normative core of this contract.

| ID | Invariant | Basis |
|---|---|---|
| **045.1** | Every Record **MUST** have **exactly one** owning partition. | I-16; Blueprint §13.6, §13.1; RMS §6.1 |
| **045.2** | Every partition **MUST** own **exactly one** sovereign Record Model. | I-16, I-101; Blueprint §13.6; RMS §2 |
| **045.3** | A Record's semantic **ownership** **MUST** belong to its owning partition's sovereign Record Model. Another model's authority over a definition **DOES NOT TRANSFER OWNERSHIP** of that Record. | Blueprint §13.6, §36 (I-105); RMS §6; Artifact 042 |
| **045.4** | Cross-partition conversion of a Record **MUST NOT** occur. It is **PROHIBITED**. | I-16; Blueprint §13.6, §12.13 |
| **045.5** | Referencing or depending on a Record held in another partition **MUST NOT** transfer ownership of that Record. | Blueprint §13.6a rule 2 |

**045.1** admits no Record with two partitions, no Record with none, and no Record whose partition
is derived at read time from its location, its kind, its content, or its history. The partition is
carried by the Record (Blueprint §13.1) and is checked (Blueprint §13.6: *"A partition remains a
required property of every Record, checked by the linter"*).

**The condition is structural, not temporal.** **A Record without exactly one owning partition
is non-conformant to this contract** — there is no conformant state in which a Record has no
partition, or has more than one. Blueprint §36 states the conformance reading directly: *"every
Record carries exactly one partition and is owned by that partition's Record Model (I-16,
I-101)."* This contract states no creation, admission or registration timing, and names no
component: **when a partition comes to be established, and by what, is not this contract's to
say.**

**045.2** is Artifact 041's S-1, restated here because 045.1 and 045.3 have no meaning without it.
It is not re-derived; Artifact 041 owns the sovereignty contract.

**045.3** is the consequence that makes 045.1 load-bearing. The partition is not a label on a
Record; it is the statement of **which model semantically owns it**. A Record in `R` is owned by
the Registry Record Model because it is in `R` — not because it resembles a definition, and not
because some other model would find Registry semantics convenient for it.

**Ownership and definitional authority are two questions, and 045.3 answers only the first.**
Registry is a sovereign Record Model whose Records define what terms mean, and the rest of the
system resolves against those definitions. That authority is real and this contract does not
narrow it: Blueprint §36 states that Registry *"governs definitions without owning another model's
Records (I-105)."* So a World Record may resolve against a Registry definition, and be governed by
it as a definition, while remaining **World-owned throughout**. The converse binds equally: no
model acquires ownership of a Registry Record by depending on its definitions.

```
Record ownership          ─▶  exactly one owning partition / sovereign Record Model
Registry authority        ─▶  what a definition means
                              — and never ownership of the Record that resolves against it
```

**045.4** is stated as a prohibition, not as a preference. See §8.

**045.5** states a **non-transfer of ownership** and nothing more. Which cross-partition references
and dependencies are *legal* is **Artifact 058's** matrix, not this contract's (§11, §14).

## 8. The Cross-Partition Conversion Prohibition

**PROHIBITED.** A Record owned by one partition **MUST NOT** be converted into a Record of another
partition. Separately creating a Record in another partition is not a conversion of the original
Record, and the original's ownership is unchanged by it (§15 example E).

The rule is normative and unconditional. It is not a default, not a guideline, not a strong
preference, and not a thing that is merely unexpected. I-16: *"Cross-partition conversion is
prohibited."* Blueprint §13.6: *"**Cross-partition conversion is prohibited** (Section 12.13): a
production record never becomes a world record by promotion — the author creates the world record
and records the relationship."*

**What is prohibited, stated exactly.** A Record **MUST NOT** cross a partition boundary while
remaining the same conceptual Record. A Record does not migrate, promote, demote, graduate, get
re-partitioned, or get reclassified into another partition and remain the same Record.

**The prohibition is independent of any model-specific `Convert` semantics.** Blueprint §12.13
defines `Convert` — *"An object changes `kind`"*, with the identity rule *"Identity persists"* —
inside its own Canonical Refactoring context. This contract neither redefines that operation nor
exports it: **nothing here requires that every Record Model implement a `Convert` operation, or
that any model inherit another's identity-operation semantics** (I-103, Artifact 043). The rule
this contract states is the constitutional one, and it binds whatever the model calls the act:
**where a source-defined operation preserves identity, that operation cannot be used to cross a
partition boundary.**

**Every ordered pair, without exception.** The prohibition is directionless and pairwise complete
across the six:

```
W ─✗→ E      E ─✗→ W      P ─✗→ R      R ─✗→ E
W ─✗→ P      P ─✗→ W      V ─✗→ I      I ─✗→ P
… and every other ordered pair of the six partitions.
```

No pair is exempt. No pair is exempt because the two models share a mechanism (I-103), because one
references the other (§9), because one depends on the other (§11), because the two rosters contain
similar-sounding kinds, or because the conversion would be convenient.

**What the sources name in its place, and how far that naming reaches.** For the cross-partition
conversion case it names, Blueprint §12.13 states the remedy in five words: *"those are a
retire-and-create."* Blueprint §13.6 states it for the World/Production case: *"the author creates
the world record and records the relationship."*

**Those are source-explicit examples, not a universal transition mechanism.** The global
constitutional rule is the prohibition; retire-and-create is what the Blueprint explicitly
describes for the cases it addresses. **This contract does not promote that example into a
required protocol for every ordered partition pair**, and no reader may cite it as having done so.

What this contract does state about any second Record is only its ownership: a Record created in
another partition is a Record of **its own** partition, owned by that partition's sovereign Record
Model, carrying its own identity and its own lifecycle. It is not the first Record relocated, and
the first Record is unchanged in its ownership by the second's existence.

**This contract defines none of the mechanics of that act** — not which Record is retired first,
not the gate it passes, not the provenance it carries, not the identity it is given, and not the
relationship that records it. Those belong to the governed mutation path, to Blueprint §12.13's
refactoring governance, and to the owning models.

## 9. Ownership Is Not Reference

A reference is a handle. Ownership is a property of the referenced Record, and a reference
**DOES NOT TRANSFER OWNERSHIP**.

Blueprint §13.6a states it for the partition where the temptation is strongest:

> *"**Issue references; it never owns.** An `EVENT` may be referenced by many issues across many
> eras. **That never makes an issue the owner of the event.** Ownership is a World-partition
> property, and a reference from a lower partition confers nothing."*

A Record referenced by one, ten, or every other partition remains owned by its own. Cardinality
confers nothing; direction confers nothing; frequency confers nothing.

**The Publishing Firewall is the same rule at constitutional scale.** Spine law 5: published
artifacts *"reference canon one-directionally; they never become canon."* Blueprint §13.6a rule 1:
*"Nothing in an issue is true because it is printed."* A World Record referenced by an Issue Record
is not thereby an Issue Record, and the Issue Record is not thereby World Truth.

**Which references are permitted is a different question**, answered elsewhere. Blueprint §13.6a
rule 3 states the Issue direction rule; RMS §4 states that *"Resolution is mechanical; **legality**
is model/Registry-owned"*; Artifact 058 owns the matrix. This section states only that a permitted
reference, like a forbidden one, moves no ownership.

## 10. Ownership Is Not Storage

Partition ownership is an **architectural ownership** fact about a Record: it identifies which
sovereign Record Model owns the Record semantically, and it **does not thereby define every
semantic dimension of that Record** — those are the owning model's, enumerated at §6. It is
**not** a statement about filesystem location, directory, package, table, process, cache, index,
deployment, shard, service, or runtime.

Artifact 041 §9 fixes this: partition ownership *"makes no claim that a partition is one
implementation class, schema, file, table, or store."* RMS §4 puts the storage question on the
other side of the line: storage and migration contracts are shared mechanism, and *"Storage shape
is model-owned within the contract."* Blueprint §13.9 leaves an implementation free to hold a
package as *"one file, three files, or a table apiece."*

Two consequences, and this section claims no third:

- **Co-location owns nothing.** Two Records sharing a file, table, index, or store do not thereby
  share a partition.
- **Separation owns nothing.** One partition's Records spread across many stores are not thereby
  many partitions.

## 11. Ownership Is Not Dependency

A Record in one partition may depend on a Record in another. That dependency **DOES NOT TRANSFER
OWNERSHIP** in either direction (045.5): the depending Record stays owned by its partition, and the
depended-upon Record stays owned by its.

**Which dependencies are legal is Artifact 058's, and is not decided here.** Row 058 states its
`Val` as *"allowed/forbidden edges; publication firewall; manifestation-blindness"* and its `Done`
as *"matrix normative"*; row 058's `H` names 045, which is why the ordering runs this way. This
contract supplies the ownership fact that 058's matrix is written against; 058 supplies the matrix.

Nothing in this section may be read as declaring any edge legal or illegal.

## 12. Ownership Is Not Identity Grammar

Ownership is not the identity string, and the identity string is not the ownership rule.

The grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` is **partition-first** (AD-1, RMS §5, Artifact
034), so the owning partition is legible in the name. That is a property of the **grammar** and
proves nothing about identity semantics. RMS §5:

> **UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL.** *The grammar fixes the syntax of the
> name and decides nothing about the thing named.*

This contract therefore **does not** define, redefine, or constrain: the identity grammar or its
syntax · `OBJECT_ID` composition, radix, padding or bounds · slug grammar, case, or normalization ·
parsing, formatting, or resolution · identity equivalence or stability · what an identity *means* in
a model. Artifact 034 owns the grammar; Artifacts 035–037 operationalise it; **Artifact 046** owns
the identity semantics boundary, which row 045 names as this artifact's unlock (`→ 046`).

This contract does not define identity parsing, formatting, or identity semantics, and it does not
define conflict resolution between an identity representation and a Record's declared partition;
that belongs to the validation and identity-semantics contracts. **045 defines only the ownership
rule itself.**

## 13. Ownership Is Not Kind

A Kind is *"a class of Record within one model"* (RMS §6.1, Artifact 044). Kind therefore lives
**inside** a partition and cannot reach across one.

**A Kind does not override, qualify, or redirect partition ownership.** A Record is not owned by
some other partition because its kind resembles that partition's kinds, because two rosters use
similar words, or because a kind code is shared in form. Blueprint §13.6a states the structural
reason: *"kinds live inside partitions and the question here is which side of a boundary a record
sits on."*

Kind taxonomies, kind admission, kind retirement, and kind rosters are not this contract's:
Artifact 044 owns the categories, Artifact 057 owns the admission test, Blueprint §13.6 states the
rosters, and I-106 holds that a listed roster is not thereby frozen.

## 14. Relationship to Neighbouring Contracts

Each row names a boundary this contract **defers to** and does not anticipate.

| Artifact | What it owns | What 045 therefore does not state |
|---|---|---|
| **039** | the Record System constitution | the six-model architecture, COM's retirement, the v1.0 model roster |
| **041** | the six-model sovereignty contract | why no model is a specialization or template of another |
| **042** | the formal Record Model definition | what a Record Model *is*, and the nine dimensions it owns |
| **043** | the mechanism vs semantics boundary | the nine prohibitions, and what sharing a mechanism does not confer |
| **044** | the architectural categories | what a Record, Kind, Field, State, Relationship, Definition, Projection or Primitive *is* |
| **046** | the identity semantics boundary | what an identity means in a model; universal grammar ≠ universal semantics |
| **058** | the cross-model dependency rules | which cross-partition edges are legal or forbidden |

Stated as a division of labour, so that no reader mistakes one contract's job for another's:

```
041  establishes the sovereignty of the six models
045  supplies the ownership fact — which partition owns a Record, and the conversion prohibition
046  defines identity semantics
058  decides which cross-partition dependency edges are legal
129  enforces the partition invariant in executable form
```

Artifact 039 §11 lists all twenty P2 kernel boundaries and assigns this one to 045 as
*"partition ownership"*. This contract claims that boundary and no adjacent one, and duplicates no
neighbouring contract.

## 15. Worked Examples

The identity below follows the Blueprint's own illustrative shape at §13.9a, whose World kind
table gives `W-CH-001-Maximus` as the `CHARACTER` example. It establishes no Record, no kind
roster, and no ordinal.

**A — A World Record is World-owned.**

```
W-CH-001-arthur                     partition: W → World Record Model
```

An Epistemic Record records what a character knows about `W-CH-001-arthur`, and references it. The
Epistemic Record is `E`-owned; `W-CH-001-arthur` remains `W`-owned. Blueprint §13.6a rule 2: the
reference *"confers nothing."*

**B — A Production reference is not a conversion.**

A Production Record — a plan for how `W-CH-001-arthur` will be used — references it. No conversion
occurs. The Production Record is `P`-owned and is *"never authoritative about the world"*
(Blueprint §13.6); `W-CH-001-arthur` remains `W`-owned and is untouched by the plan's existence.

**C — A Visual reference transfers nothing.**

A canonical visual specification in `V` describes how `W-CH-001-arthur` looks. The specification is
`V`-owned. `W-CH-001-arthur` remains `W`-owned. Blueprint §13.6c: *"V holds the objects. It does not
hold the authority."*

**D — Publication does not re-own.**

An Issue Record — a page, an article — references `W-CH-001-arthur`. The Issue Record is `I`-owned
and is *"Not Canon"*; `W-CH-001-arthur` is not thereby an Issue Record. Blueprint §13.6a: *"a World
object never becomes an Issue object by being published."*

**E — The prohibited conversion.**

```
W-CH-001-arthur  ──✗ PROHIBITED ✗──▶  a Production Record
```

There is no operation that turns `W-CH-001-arthur` into a Production Record. No identity-preserving
operation may cross the boundary, whatever the owning model calls it (§8).

A Production Record about Arthur may of course exist. It is a **distinct Record**, separately
created, `P`-owned from the moment it exists, governed by Production semantics, and carrying its
own identity. It is **not** `W-CH-001-arthur` relocated, and `W-CH-001-arthur` is unchanged in its
ownership by it. Blueprint §13.6: *"the author creates the world record and records the
relationship"* — stated there in the opposite direction, and reading identically in this one.

**This example demonstrates the constitutional prohibition. It is not a transition protocol**, and
the mechanics of that separate creation are not defined here — not the order of acts, not the
gate, not the provenance, not the identity, and not the relationship that records it (§8).

## 16. Non-Goals — What This Contract Does Not Define

This contract defines partition ownership. It defines **none** of the following, and no reader may
cite it as having done so:

1. the identity grammar — **Artifact 034**
2. identity semantics — **Artifact 046**
3. any Kind taxonomy or roster — Blueprint §13.6, each model, I-106
4. field schemas for any Record
5. package schemas or package composition — **Artifact 056**, I-107
6. relationship schema or relationship legality — **Artifact 055**
7. lifecycle rules for any Record Model
8. state semantics or any state vocabulary
9. canonicality semantics — **Artifact 052**, I-104
10. the cross-model dependency matrix — **Artifact 058**
11. storage architecture, layout, or location
12. runtime architecture
13. validators, linters, or any executable code — **Artifact 129** is the partition validator
14. migration tooling or migration procedure
15. database behaviour, transactions, or indexing
16. serialization format or envelope contents — **Artifact 033**
17. any universal semantic base model — **PROHIBITED** by RMS §4's nine prohibitions and
    Artifact 043
18. universal `Convert` semantics, or any requirement that a Record Model implement one — §8
19. universal retire-and-create mechanics, or a transition protocol for any partition pair — §8
20. Registry's semantic-authority model — Registry is sovereign over its definitions (I-105);
    this contract states only that such authority transfers no Record ownership — §7
21. how a disagreement between a Record's declared partition and its identity representation is
    resolved — §12
22. Mutation Coordinator behaviour, or any part of the governed mutation path — §8

**On 17 in particular.** Nothing in this contract establishes a universal Record base, a universal
semantic parent, a shared ancestor of the six, or World as a base from which the others
specialize. RMS §2: *"No model is a superclass of another. World is not a template."* A rule that
every Record has exactly one partition is a rule about **ownership**, and is not a claim that all
Records are instances of one semantic object model. The Canon Object Model is retired (RMS §2) and
is not revived here in any form.

**Record System ≠ Record Model.** The chain this contract states runs:

```
Record System
      └─▶ six sovereign partitions
                └─▶ each partition owns exactly one sovereign Record Model
                          └─▶ each Record belongs to exactly one partition
```

The Record System is the architecture within which the six coexist; a Record Model is one of the
six. Neither term may be substituted for the other.

## 17. Conformance Conditions

Stated here so they are checkable. **Artifact 059** owns the P2 kernel conformance suite and
**Artifact 129** is the partition validator; this document implements no test and is `T: doc`.

| ID | Condition | Invariant |
|---|---|---|
| **C-01** | Every Record declares exactly one owning partition, drawn from the six. | 045.1 |
| **C-02** | A Record with zero owning partitions, or with two or more, is non-conformant to this contract. | 045.1 |
| **C-03** | Each of the six partitions owns exactly one sovereign Record Model, and no model is owned by two partitions. | 045.2 |
| **C-04** | A Record is semantically owned by its owning partition's Record Model and by no other; another model's authority over a definition the Record resolves against does not make that model the Record's owner. | 045.3 |
| **C-05** | No operation converts a Record from one partition to another. | 045.4 |
| **C-06** | No cross-partition reference or dependency changes the owning partition of either Record. | 045.5 |
| **C-07** | At v1.0, the Record System contains exactly the six sovereign partitions W, E, P, R, V and I; no partition is a specialization of another. | §5, I-101 |

A construction satisfying all seven is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 18. Source Traceability

| Rule | Source |
|---|---|
| Every Record carries exactly one partition | I-16; Blueprint §13.6, §13.1; RMS §6.1 |
| Every partition owns exactly one sovereign Record Model | I-16, I-101; Blueprint §13.6; RMS §2 |
| At v1.0, exactly six sovereign partitions / Record Models — W, E, P, R, V, I; no seventh sovereign Record Model is required at v1.0 | RMS §2, §25; Blueprint §13.6 |
| Partition names which Record Model owns the Record | Blueprint §13.1, §13.6 |
| Ownership is semantic, not storage | Artifact 041 §9; RMS §4; Blueprint §13.9 |
| Cross-partition conversion is prohibited | I-16; Blueprint §13.6, §12.13 |
| An identity-preserving operation cannot be used to cross a partition boundary; `Convert` is defined in Blueprint §12.13's own context and is not universalized here | Blueprint §12.13; I-103 |
| Blueprint §12.13 explicitly describes retire-and-create for the cross-partition conversion case it names; 045 defines no universal cross-partition transition mechanism | Blueprint §12.13, §13.6 |
| Registry governs definitions without owning another model's Records | Blueprint §36 (I-105) |
| A Record without exactly one owning partition is non-conformant | Blueprint §36 (I-16, I-101); §13.6 |
| Reference confers no ownership | Blueprint §13.6a rule 2 |
| Publication creates no ownership and no truth | Spine law 5; Blueprint §13.6a rules 1 and 3 |
| Kinds live inside partitions | Blueprint §13.6a; RMS §6.1 |
| Grammar is partition-first and decides no semantics | AD-1; RMS §5; Blueprint §13.9a |
| No universal semantic base model | RMS §2, §4; Blueprint §13.7a |
| The partitions cannot be collapsed | Blueprint §13.6, the partition test |

`Req: BR-17` is preserved exactly as the Roadmap states it. The authoritative requirement register
is not present in this repository; the requirement text is therefore **not** reproduced here and
**MUST NOT** be inferred.

---

*Artifact 045 · P2/2b · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states a contract derived from Blueprint §13.6 and §12.13, RMS §2, and invariant I-16. It
is not a Record, holds no canonical data, states no validator, and creates no architecture of its
own. Where it and the Master Blueprint, the Record Model System, or the OS File Build Roadmap
differ, they are right and this document is wrong.*
