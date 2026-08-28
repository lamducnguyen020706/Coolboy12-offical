# COOLBOY12 — Bootstrap Meta-Contract

**Artifact 031** · `docs/constitution/bootstrap_meta_contract.md` · Own: CONST · RM: n/a · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: **not a Record** · CD: no · Ph/St: P1/1a ·
Req: BR-19 · BP: §13.7 · RMS: §10.4 · H: 004,016 · S: — · LS: — · G: — ·
→ 032–038, P3 · Risk: CRITICAL · ∥: no

## 1. Purpose

This document answers one question: **what MUST a Record have in order to be a Record at all?**

It states the six elements of that minimum and nothing above them. It is deliberately small, and
its smallness is the requirement, not a limitation of the current draft: Blueprint §13.7 —
*"a bootstrap that could express the whole model would be the model."*

The contract is **sufficient** to create the first Registry entry and the first Record, and it is
**insufficient for anything more** (Blueprint §13.7, §13.6e). Everything a Record means beyond
this minimum is owned by the Record Model that holds it, or defined by Registry, and neither is
established here.

## 2. Status and Authority

| Question | Answer | Source |
|---|---|---|
| Is this a Record? | **No.** | RMS §10.4, Roadmap row 031 `Canon: not a Record` |
| What is it, then? | A **constitutional bootstrap contract standing outside the ordinary Registry Record ontology** | RMS §10.4 |
| Source-of-truth class | AUTHORITATIVE — the fact lives here and is not rebuildable | Artifact 016 §3 |
| Authority | Governing over the six elements below, and over nothing else | Roadmap row 031 |

**The content and the status were settled by two different acts, and both are recorded.**

Blueprint §13.7 settles the **content**: the six elements, permanently and by name. Blueprint
§13.6b then records the **ontological status** as an open architectural question —
*"whether the Bootstrap Meta-Contract is itself a Registry Record, a constitutional statement in
this Blueprint, or a third thing standing outside both … The meta-contract's content is settled;
its ontological status is not"* — logged as **FG-V7-05, REQUIRES AUTHOR DECISION**.

RMS v1.0 §10.4 closes it: **CLOSED `AUTHOR-DECIDED` (closes FG-V7-05)**. That is the designed
resolution path, not a contradiction of the Blueprint: the Blueprint declined to close the
question by assertion and referred it for decision, and the RMS records the decision taken.

**What this artifact is authoritative for, and what it is not.** Artifact 031 is the
AUTHORITATIVE statement of the bootstrap minimum: a reader needing to know what a Record must
have to be a Record at all reads this document. It is not the source of that decision — the
Blueprint established the six elements and the RMS ruled on the non-Record status — and it
neither amends nor overrides either. Every requirement below is traceable to a source cited with
it.

## 3. Bootstrap Position

```
CONSTITUTION
   ↓
BOOTSTRAP META-CONTRACT      (constitutional, not a Record)
   ↓
first Registry Record
   ↓
Registry definitions
   ↓
normal Record creation
```

*(RMS §10.4, reproduced. Blueprint §13.7 states the same ordering as
`Bootstrap Meta-Contract → Registry Kernel ↔ Record Kernel → Validation → Store / Mutation`,
where the Registry Kernel and the Record Kernel are built together and neither is finished ahead
of the other.)*

**There is no special "axiom Record." There is no circular self-definition requirement.** Once
Registry exists, its definitions follow normal Record semantics (RMS §10.4).

The diagram above states the meta-contract's **position**. The bootstrap **flow specification** is
Artifact 032 and is not written here (§7).

## 4. The Six Contract Elements

**EXACTLY SIX. Nothing else.**

> *"It defines only what a record must have in order to be a record at all:
> **partition · kind · identity · core envelope · provenance · Registry reference**. Nothing
> else."* — Blueprint §13.7
>
> *"…containing only: partition · kind · identity · core envelope · provenance · Registry
> reference."* — RMS §10.4

The list is stated three times across the two governing sources — Blueprint §13.6b, Blueprint
§13.7, RMS §10.4 — in identical terms and identical order, which is the order used below.
Roadmap row 031 states the same requirement in its `Val` field; that field's element list is
truncated after `partition` by the Roadmap's own `·` field separator, and the Blueprint and RMS
supply it in full.

The contract's elements are §4.1 through §4.6. No other section states one.

### 4.1 Partition

Every Record MUST have a **partition**.

There are six partitions, one per sovereign Record Model — **W** World · **E** Epistemic ·
**P** Production · **R** Registry · **V** Visual · **I** Issue. RMS §2 fixes the models at
*"exactly six sovereign Record Models"*; this artifact records that count and does not set it.

> **I-101** — *Every partition owns exactly one sovereign Record Model. No Record Model is a
> specialization of another, and no Record Model is the template for another.*

**Boundary.** The partition establishes **which Record Model is sovereign** over the Record. It
does not thereby confer meaning on the Record: what the Record *means*, what its lifecycle is,
and whether it can be canonical are model-owned (I-103, I-104, §13.7a). Placement is not
interpretation.

### 4.2 Kind

Every Record MUST have a **kind**.

**Boundary.** This contract requires *that* a Record carries a kind. It does not define kinds, and
it establishes no kind taxonomy.

> **I-106** — *A kind roster that is listed is not thereby frozen. Only the World taxonomy is
> established; every other roster names a boundary and is revisable by that model's own design
> work until it declares otherwise.*

Blueprint §13.7a states the prohibition directly: **No universal kind taxonomy** — each Record
Model owns its own (§13.11). Kind rosters are stated once, at Blueprint §13.6, and Registry
definitions govern what a kind means (I-105). None of that is established here.

### 4.3 Identity

Every Record MUST have an **identity**.

The identity **grammar** is the one deliberate universal in the Record System, and it is a grammar
rather than a semantics:

> **§13.7a (AD-1, resolved)** — *"A universal identity grammar is not a universal Record
> semantics — the grammar fixes the syntax of the name and decides nothing about the thing
> named."*

What remains model-owned is the semantic interpretation of what that grammar names: which kinds
exist, what a kind means, what constitutes the identity of a Record in that model, and what its
lifecycle, authority, and temporal meaning are (§13.7a, §13.9a, I-82).

**Boundary.** The grammar's positional specification is **Artifact 034**; its parser and formatter
are **Artifact 035**; ordinal allocation and the allocation record are **Artifact 036**. None of
the three is specified here.

### 4.4 Core envelope

Every Record MUST have a **core envelope**.

Blueprint §13.7 fixes the custody of that envelope before it fixes its contents:

> *"this blueprint owns the Record's **properties**; the Record Model Schema file owns its
> **fields**."*

and, where the two appear to conflict, *"the Record Model Schema governs on fields and the
Blueprint governs on properties."*

**Boundary.** The core envelope is one of the six elements, not a second contract nested inside
this one. Its field-level contract is **Artifact 033**, and its fields are not enumerated here.
Blueprint §13.7a states the outer limit that keeps the element small: **No Universal Record
Base** — *"The shared layer is the bootstrap contract of §13.7 and nothing above it"* — and **No
universal Record schema.**

*Blueprint §13.7 assigns field custody to a companion Record Model Schema and records that
document as unrevised (**FG-V7-01**). It is not in the supplied source set, and RMS v1.0 does not
reference it: the universal envelope's fields are carried by **RMS §4**, which is the field
source Roadmap row 033 cites. Noted because §13.7's custody sentence is quoted above; it does
not affect this element, whose subject is the envelope's existence rather than its fields.*

### 4.5 Provenance

Every Record MUST have **provenance**.

> **§13.7b** — *Provenance* answers *"Who made this, when, and **why**"*, and lives as *"an
> envelope property on the Record."*

§13.7b separates six terms that *"are not interchangeable"* — provenance · audit · history ·
revision · version · derivation. **Only provenance is an element of this contract.** History,
revision, and version are model-owned packaging (§13.7b, §13.6d, I-102).

**Boundary.** Provenance *capture* is shared infrastructure; **what provenance means in a model**
is not decided by it (§13.7a).

### 4.6 Registry reference

Every Record MUST have a **Registry reference**.

> **I-105** — *Registry is a sovereign Record Model. Its definitions are Records, not
> configuration. Registry holds semantic authority over definitions and never semantic ownership
> of another model's Records.*

The sufficiency claim in §1 belongs to the six elements together, not to this one alone
(Blueprint §13.7).

**Boundary.** What Registry *defines* is the Registry Kernel's, not this contract's (§13.7,
I-105). Reference *resolution* is shared infrastructure and decides nothing about whether a
reference is semantically legal (§13.7a, §9.4). Neither is established here.

## 5. Non-Record Boundary

**The Bootstrap Meta-Contract IS NOT A RECORD** (RMS §10.4).

It MUST NOT be treated as, or converted into, any of the following:

- a Record of any Record Model;
- a Registry Record, or the first Registry Record — it stands *before* that Record (§3);
- an axiom Record, or any special Record subtype — *"There is no special 'axiom Record'"*
  (RMS §10.4);
- a seventh Record Model, or a Bootstrap / Meta / Constitution Record Model — the six sovereign
  Record Models are unchanged and remain exactly six (RMS §2, I-101);
- a universal Record base, a universal Record schema, or a universal semantic model — Blueprint
  §13.7a prohibits all three by name;
- an ownership layer over any model's semantics — *"Shared infrastructure never confers shared
  meaning"* (I-103).

It defines no Record, holds no Record, and is defined by no Record. **There is no circular
self-definition requirement** (RMS §10.4).

Because it is not a Record, it has no partition of its own, no kind, no identity in the Record
identity grammar, no envelope, and no Registry reference. It *names* those six as requirements on
Records; it does not carry them.

## 6. Dependency Boundary

| Dependency | What it supplies to this artifact |
|---|---|
| **Artifact 004** — `CLAUDE.md` | Session conduct, the Spine, the six Record Models, AD-1, and invariants I-101…I-108 as standing operational law |
| **Artifact 016** — `docs/boundaries/source_of_truth.md` | The source-of-truth classification vocabulary under which this document is AUTHORITATIVE, and the rule that `SoT: AUTHORITATIVE` is not World Canon |

Neither dependency is amended by this document.

## 7. Downstream Handoff

This artifact establishes the minimum and stops. What is absent here is absent by ownership, not
by omission:

| Not defined here | Owned by |
|---|---|
| The bootstrap flow — §3 states position only | Artifact 032 |
| The envelope's fields | Artifact 033 |
| The identity grammar, its parser, and ordinal allocation | Artifacts 034–036 |
| Structural validation — and this contract is not a semantic validator | Artifact 037 |
| Executable proof of this contract | Artifact 038 |
| What Registry defines | Registry Kernel |

---

*Artifact 031. Sources: Blueprint §13.6b, §13.7, §13.7a, §13.7b; RMS §2, §10.4; Roadmap row 031.
This document is AUTHORITATIVE about the bootstrap minimum and is `Canon: not a Record`. It
carries no canonical data, defines no Record, and creates no Record Model.*
