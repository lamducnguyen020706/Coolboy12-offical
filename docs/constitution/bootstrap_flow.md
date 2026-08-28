# COOLBOY12 — Bootstrap Flow Specification

**Artifact 032** · `docs/constitution/bootstrap_flow.md` · Own: CONST · RM: n/a · T: doc ·
R: ARCH · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P1/1a ·
Req: BR-19 · BP: §13.7 · RMS: §10.4 · H: 031 · S: — · LS: — · G: — ·
→ 060 · Risk: high · ∥: no

## 1. Purpose

Artifact 031 states **what** a Record must have to be a Record at all. This document states
**how** the bootstrap proceeds: the order of the steps, what each one requires of its
predecessor, and where the sequence stops being bootstrap.

It specifies ordering. It defines no Record, no definition, no field, no identity, no validator
and no write path — every one of those is owned downstream (§6).

Roadmap row 032 states the reason: *"closes FG-V7-05 in build terms."* The architectural
question — whether the Bootstrap Meta-Contract is itself a Record — was closed by author
decision at RMS §10.4 and is recorded in Artifact 031 §2. **This artifact does not reopen it and
does not close it again.** What it closes is the build-side question: given that ruling, in what
order does the system come into existence.

## 2. Status and Authority

| | |
|---|---|
| Role | ARCH — an architecture document, per row 032 (`R: ARCH`) |
| Source-of-truth class | AUTHORITATIVE (Artifact 016 §3) |
| Canon | `n/a` — row 032. This document is not a Record and holds no canonical data |
| Hard dependency | **Artifact 031** only (`H: 031`). Row 032 declares no other |
| Unlocks | **060**, the Registry Record Model specification (P3) |

Artifact 032 is authoritative for the **order** of bootstrap. It is not the source of that order:
RMS §10.4 states the chain and Blueprint §13.7 states the build-order view. This document
reproduces both and adds no step to either.

## 3. Preconditions

Bootstrap presupposes exactly one artifact: **Artifact 031**, the Bootstrap Meta-Contract, which
states the six-element minimum. Those six elements are not restated here; 031 owns them.

Nothing else is a precondition of the flow. In particular, no Record, no Registry definition and
no validator exists before the flow begins — that is the condition the flow exists to resolve.

## 4. Bootstrap Sequence

### The chain — RMS §10.4, and row 032's `Val`

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

This is the normative flow. Row 032's `Val` field states the same five steps
(*CONSTITUTION → META-CONTRACT → first Registry Record → definitions → normal Records*), and
Artifact 031 §3 reproduces the diagram to state the meta-contract's position within it.

**The chain is one-way.** Each step's predecessor must exist before it. No step reaches back to
constitute a step above it — see §5.

### 4.1 Constitution

The governing architecture: the Blueprint, the Spine, the invariant register. It is in place
before bootstrap begins and is not produced by it.

### 4.2 Bootstrap Meta-Contract

The six-element minimum, stated by Artifact 031 and **not a Record** (RMS §10.4).

Its role in the flow is exactly its sufficiency claim: Blueprint §13.7 — *"It is sufficient to
create the first Registry entry and the first Record, and it is not sufficient for anything
more."* That is what makes the next step possible and what stops it doing more.

### 4.3 First Registry Record

**The first Registry Record is a Record. The Bootstrap Meta-Contract is not.** This is the
distinction the whole flow turns on: the step that admits the first Record is preceded by
something that is not one, which is why no Record is required in order for the first Record to
become possible.

Its position is the first application of the meta-contract. Its content is not specified here —
not its kind, its identity value, its fields, or its payload. *Not established by the supplied
authoritative sources*, and Registry's own roster and categories are §13.6/§13.6e and Roadmap
P3, not this artifact.

### 4.4 Registry definitions

> **RMS §10.4** — *"Once Registry exists, its definitions follow normal Record semantics."*

That sentence is the whole of what this step establishes here. Registry definitions are Records
(I-105, §13.6e), and **what** they define — kinds, vocabularies, fields, relationships,
validation rules, visual reference policies, semantic constraints (§13.7) — is the Registry
Kernel's, reached through row 032's unlock of artifact 060. This document places the step; it
does not fill it.

### 4.5 Normal Record creation

The end of the flow, and the point at which the flow stops being special. Nothing distinguishes
Record creation after this step from ordinary system operation.

### 4.6 The Blueprint's build-order view

Blueprint §13.7 states a second, coarser view of the same transition:

```
Bootstrap Meta-Contract
        ↓
Registry Kernel  ↔  Record Kernel      built together
        ↓
Validation
        ↓
Store / Mutation
```

**`↔` is the source's notation and is preserved.** Blueprint §13.7 is explicit about what it
means: *"Lockstep does not mean sequence"*; the Record Model Schema *"is **not** a standalone
document that must be completed and frozen before Registry work may begin"*; *"Each new Registry
definition has a corresponding Record Model Schema expression, authored in the same act"*; and
**"Neither document is ever 'finished' ahead of the other, and neither blocks the other."** An
ordering in which either kernel is completed first would contradict the source.

**Validation** sits after the paired kernels, and **Store / Mutation** after validation. This
artifact places them and states nothing about their content: what structural validation checks is
Artifact 037, and the mutation path is Roadmap P5.

> **Gap — the correspondence between the two diagrams is not established.** The two views share a
> starting point, the Bootstrap Meta-Contract, and §13.7 states the meta-contract is sufficient to
> create *"the first Registry entry and the first Record"* — the two things the paired kernels
> concern. Whether `Registry Kernel ↔ Record Kernel` is the same transition as
> `first Registry Record → Registry definitions`, expressed at a coarser grain, is **not stated by
> any supplied source**: the phrase appears exactly once across the Blueprint, RMS and Roadmap,
> inside the diagram above, with no prose relating it to the RMS chain.
>
> This artifact therefore reproduces both views and merges neither. A single combined diagram
> would require arrows no source states. Row 032's `Val` names the RMS chain, so that chain is the
> normative flow; §4.6 is the Blueprint's build-order view of the same period and is recorded
> beside it, not folded into it.

## 5. Bootstrap Invariants

Row 032's `Done` field names the first two.

1. **No circular self-definition.** The flow MUST NOT require a Record to exist in order to
   establish the conditions under which the first Record can exist. RMS §10.4:
   *"There is no circular self-definition requirement."* The chain satisfies this structurally —
   §4.2 precedes §4.3 and is not a Record.
2. **No special axiom Record.** RMS §10.4: *"There is no special 'axiom Record.'"* No bootstrap
   Record, meta Record, constitutional Record or system Record is introduced by this flow.
3. **No seventh Record Model.** The bootstrap layer is not a Record Model. RMS §2 fixes the count
   at *"exactly six sovereign Record Models"*, and bootstrap does not change it.
4. **The flow orders construction; it does not own meaning.** What a Record of any model *means*,
   its lifecycle, its relationship and history packaging, and whether it can be canonical are
   model-owned (I-101, I-102, I-104, §13.7a). Registry holds *"semantic authority over
   definitions and never semantic ownership of another model's Records"* (I-105). Being early in
   the sequence confers no semantic authority — *"Shared infrastructure never confers shared
   meaning"* (I-103).
5. **Neither kernel is finished ahead of the other** (§13.7, quoted at §4.6).

**Failure forms.** The sources name three things the flow must not become — circular
self-definition, a special axiom Record, and semantic overreach beyond the shared layer
(§13.7a). They are stated above as invariants. No other bootstrap failure branch is established
by the supplied sources, and none is invented here; this is not an error-handling specification.

## 6. Non-Goals and Ownership Boundaries

What is absent here is absent by ownership:

| Not defined here | Owned by |
|---|---|
| The six-element minimum | Artifact 031 |
| The universal Record envelope and its fields | Artifact 033 |
| Identity grammar, parser and formatter, ordinal allocation | Artifacts 034–036 |
| What structural validation checks | Artifact 037 |
| Record Model schemas and semantics | each sovereign Record Model |
| Registry definition content, kinds and vocabularies | Registry Kernel (via 060) |
| Mutation implementation and canonical write policy | Roadmap P5 |
| Adapters and runtime infrastructure | later phases |

This document authorises no canonical write. It contains no Record, no example payload and no
canonical data.

## 7. Completion Condition

The source establishes one transition and no finer predicate:

> **RMS §10.4** — *"Once Registry exists, its definitions follow normal Record semantics."*

Bootstrap is complete when the chain in §4 has reached **normal Record creation** — the last step
of row 032's `Val`. From that point Record creation is ordinary, and nothing in this document
governs it.

**No precise completion predicate — a checkable condition naming what must exist and hold — is
established by the supplied authoritative sources.** None is invented here. An executable
statement of P1 completion is Artifact 038's, and structural checking is Artifact 037's.

**Bootstrap complete does not mean the system is complete.** Blueprint §13.7 bounds the
meta-contract as *"sufficient to create the first Registry entry and the first Record, and … not
sufficient for anything more"*, and states that neither the Registry nor the Record Model Schema
is ever *"finished"*. Reaching the end of this flow therefore does not imply that Registry
definitions are complete, that validation is in place, that adapters exist, or that any runtime
service is available.

## 8. Downstream Handoff

Row 032 declares one unlock: **060**, the Registry Record Model specification (P3), whose own row
records `H: 032`. The flow's later steps are populated there and in the artifacts listed at §6.

---

*Artifact 032. Sources: Blueprint §13.7 (and §13.6b, §13.6e, §13.7a for the boundaries cited);
RMS §2, §10.4; Roadmap rows 032 and 060; Artifact 031. Metadata reproduced from Roadmap row 032.
This document specifies ordering only, is `Canon: n/a`, carries no canonical data, defines no
Record, and creates no Record Model.*
