# COOLBOY12 — Authority Framework

**Artifact 051** · authority framework · `docs/constitution/authority.md` · Own: CONST · RM: all ·
T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P2/2c · Req: BR-22,RR-30 · BP: §13.7c · RMS: §17 · H: 039 · S: — · LS: — · G: — ·
→ 052, all models · Val: authority domain-scoped; Record ≠ Canon · Done: framework ·
Why: I-104 made buildable · Risk: high · ∥: no

## 1. Purpose

Row 051 states this artifact's reason in four words: **I-104 made buildable.**

I-104: *"Record and Canon are not synonyms. Canonicality is a status property whose meaning is
defined by each Record Model that has one, and two models hold Records that are never
canonical."* RMS §17 states the rule this artifact exists to make operational, in full:

> *"**Record ≠ Canon.** All authority is domain-scoped."*

Those two sentences are the whole of the source architecture's authority rule. This contract
makes them usable: it fixes what "authority" refers to, holds the one constitutional commit
position apart from every other use of the word, and states the boundaries that stop authority
collapsing into Record, Canon, canonicality, source-of-truth class, provenance, model ownership
or infrastructure permission.

Artifact 042 already names the question this document answers: *"Semantic ownership is not
change authority. Who may commit a change, and under what ceremony, is Artifact 051."* This
contract answers it at the level of the framework. It does not write any model's ceremony.

It adds no architecture. Every rule below is a contractual formulation of what the Spine,
Blueprint §10.1, §12.1, §12.6, §13.0, §13.6, §13.6c, §13.7a, §13.7c and §26.2a, RMS §6 and §17,
and the invariants cited already establish.

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the authority framework boundary**, and about nothing
else. It **derives** that boundary from the Master Blueprint and the Record Model System; it does
not amend, supersede, or outrank either.

Where this document differs from the Master Blueprint, the Record Model System, or the OS File
Build Roadmap, **those governing sources are correct and this document is wrong.**

It is not a Record, holds no canonical data, and is `Canon: n/a`. `SoT: AUTHORITATIVE` here means
authoritative **about architecture**, never World Canon (Blueprint §13.0, I-104). `Auth: governing`
binds how later artifacts treat this boundary; it confers no power to commit anything.

`Req: BR-22,RR-30` is preserved exactly as the Roadmap states it. The authoritative requirement
register is not present in this repository; the requirement text is therefore **not** reproduced
here and **MUST NOT** be inferred.

## 3. Scope

**In scope.** What the word *authority* refers to; the one constitutional commit position and its
rules; that every other authority is scoped to a domain; the separation of authority from Record,
Canon, canonicality, source-of-truth class, provenance, model ownership and infrastructure; the
relationship of the Authority to the Human Gate and the Mutation Coordinator; delegation,
absence and succession, as the sources state them.

**Out of scope.** What canonical means in any model (Artifact 052); any model's own authority
semantics or ceremony (each model's own contract); canonical gates (Artifact 145); the Human
Gate's implementation; the Mutation Coordinator's implementation; cross-model dependency
legality (Artifact 058); roles, permissions, credentials, identities, schemas, fields, code and
tests.

**Position.**

```
039  Record System constitution
  ↓
041  six-model sovereignty
  ↓
051  authority framework                          ← this contract
  ↓
052  canonicality framework
  ↓
     each model's own authority and canonicality, and its canonical gate

050  source-of-truth classification ─┐
                                     └─ related to 051 (§9), and not owned by it
```

The arrows state dependency and nothing else. No downstream artifact inherits semantics from
this one; each defines its own within the boundary stated here.

## 4. Terms Kept Apart

Each term keeps its own source and owner. This table assigns no new meaning; it records where
each meaning already lives, so that none is read as another.

| Term | What it is, per its source | Source | Owner |
|---|---|---|---|
| **Authority** | The one constitutional position that commits canon — *"a position, not a person"* | Spine law 3; Blueprint §10.1; I-03 | the Spine |
| **authority** | Legitimate power within a domain. *"All authority is domain-scoped."* | RMS §17 | this contract (the framework); each model (its own domain) |
| **Record** | *"The architectural unit: a persistent semantic unit owned by exactly one Record Model"* | Blueprint §13.0 | Artifact 039 |
| **Record Model** | *"The partition-owned semantic model that owns Records"* | Blueprint §13.0; RMS §6 | Artifacts 041, 042 |
| **Canon** | *"A governance and truth concept: the committed record, and the authority that commits it"* | Blueprint §13.0, §12.1 | the Spine |
| **canonicality** | *"A status property whose meaning is defined by each Record Model that has one"* | Blueprint §13.0, §13.7c; I-104 | Artifact 052; each model |
| **source-of-truth class** | Where a fact lives — one of five classes | Blueprint §29.6a | Artifact 050 |
| **Human Gate** | The stage of the one path at which the author confirms, modifies or rejects a change | Spine law 2; Blueprint §12.6 | the Spine |
| **Mutation Coordinator** | *"the only thing in coolboy12 that writes canon"* | Blueprint §12.6; I-83 | the Spine; its implementation elsewhere |
| **`Auth:` metadata** | An artifact metadata field: *"What authority the artifact carries"*, and *"always domain-scoped"* | Artifact 003, field 9 | Artifact 003 |

**On capitalization.** This document writes **Authority**, capitalized, for the constitutional
position of §10.1, and **authority**, lowercase, for domain-scoped authority generally. That is
this document's convention, adopted so the two cannot be confused in the text below. It is not a
source rule, and the sources themselves are not rewritten to follow it.

## 5. The Governing Authority Rule

> **Authority is legitimate only within its domain. The constitutional Authority is the one human
> position that commits canon, through the one path. Every other authority is scoped to the domain
> its source gives it, and extends no further. Authority is not Record, not Canon, not
> canonicality, not source-of-truth class, not provenance, not model ownership, and not
> infrastructure permission.**

```
                        CONSTITUTIONAL AUTHORITY
                   one human position · commits canon
                                  │
                                  │  is NOT, and does not become
                                  ▼
   ┌──────────┬──────────┬──────────────┬──────────┬────────────┬────────────────┐
   │  Record  │  Canon   │ canonicality │ SoT class│ provenance │ infrastructure │
   │          │          │              │          │            │                │
   │ architec-│governance│  model-owned │ where a  │ who, when, │   capability · │
   │ tural    │ + truth  │  status      │ fact     │ why        │ defence-in-    │
   │ unit     │          │  (052)       │ lives    │ (047, 048) │ depth          │
   │ (039)    │ (Spine)  │              │ (050)    │            │ (I-83, I-84)   │
   └──────────┴──────────┴──────────────┴──────────┴────────────┴────────────────┘
                     each remains distinct from the others
```

## 6. The One Constitutional Authority

Spine law 3: *"Only the human commits canon. No AI output, no simulation result, no deadline, no
report is canonical until the human gates it."* Blueprint §10.1 defines what "the human" means:

> *"the definition is a position, not a person: there is exactly one **Authority** at any moment,
> it is always held by a human, and it is never held by two parties simultaneously."*

I-03: *"Only the Authority commits, and there is exactly one Authority at a time."*

Stated as rules:

1. **At any moment there is exactly one Authority, or there is none.** There is never more than
   one.
2. **The Authority is always a human.** An AI role may never hold it (§10.1).
3. **Only the Authority commits canon** (Spine law 3; I-03).
4. **It is a position, not a person, and not a software principal.** It is not a role object, an
   account, a process, a service, a credential or a committee.
5. **No automation, schedule or default may ever exercise it** in the Authority's absence
   (§10.1).

**The Authority is scoped too.** Applied to the Authority, RMS §17's rule means this: what §10.1
grants the position is the commit of canon, through the one path of Spine law 2, and that is its
domain. It does not make the Authority the owner of any model's Records — semantic ownership stays
with each Record Model (RMS §6), and Artifact 042 already records that *"Semantic ownership is not
change authority."*

## 7. Domain-Scoped Authority

RMS §17: *"All authority is domain-scoped."* A statement that something is authoritative is
therefore incomplete until its domain is known, and it is never a statement about any other
domain.

```
    an authority claim
           ↓
    the domain its source gives it
           ↓
    that domain's boundary
           ↓
    nothing beyond it                     ✗  "authoritative"  →  "authoritative everywhere"
```

**The sources already show it.** Three places, each reading correctly only when authority is
scoped:

- **Blueprint §13.7c** records, per Record Model, what authorizes its state: the Human Gate for
  World and for Epistemic; Production ceremony for Production; Registry change (§9.4) for
  Registry; a gate per kind for Visual; publication for Issue. Six models, not one authorizing
  act. What those mean is not stated here — the table is Artifact 052's, and each model's meaning
  is its own.

  One consequence is fixed, because the Spine fixes it: wherever a model's Records are canonical,
  canon changes only through the one path (Spine law 2) and only the Authority commits it (I-03).
  How a model's own authorizing act sits within that path — for example, how a Registry change
  (§9.4) meets the Human Gate — the sources do not restate, and this contract does not decide. It
  is each model's own contract's, and the canonical-gate framework's (Artifact 145).
- **Blueprint §29.6a** lists *"Production State about the plan"* as AUTHORITATIVE, while
  **Blueprint §13.6** says Production State is *"never authoritative about the world"*. Both hold
  because each is scoped: about the plan, and about the world.
- **Blueprint §13.6c**: *"V holds the objects. It does not hold the authority."* Holding a Record is
  not holding authority over what it is about.

**No universal taxonomy of domains is established here.** This contract states that authority is
scoped; it does not enumerate the scopes, rank them, or assume the six models share one authority
semantics. It creates no authority levels, weights, ranks, inheritance chains or escalation paths.
The canon tiers of Blueprint §12.2 rank canonical statements against each other; they are not an
authority hierarchy, and are not read as one here.

**Source condition recorded, not resolved.** RMS §17 places the authority matrix *"in Appendix E
and Deliverable H"*. Appendix E of the RMS reads only *"Authority Matrix → Deliverable H"*, and
**Deliverable H is not present in this repository.** The matrix is therefore unavailable, and this
contract does not reconstruct it. The framework rule — that authority is domain-scoped — stands
without it; the per-domain enumeration it would carry belongs to that deliverable and to each
model's own authority contract.

## 8. Authority and the Canon Boundary

**A Record is not Canon.** Blueprint §13.0 names *"Three statements the blueprint must never make"*:
*every Record is Canon* · *every Record is canonical* · *Canon = Record*. It holds the two words
apart: *"**`Record` is architectural. `Canon` is governance.**"*

Operationally:

- A Record does not become Canon by existing, by being stored, or by being valid.
- Blueprint §12.1: *"Canon is exactly the committed record"*. Canon is reached through the one path
  and the Authority's commit — never by storage, by repetition, or by any component's assertion.
- **Authority over something is not canonicality of it.** Being authoritative within a domain does
  not make a Record canonical, and it does not make it World Canon. Whether and how a model treats
  its Records as canonical is that model's (I-104), within the framework of Artifact 052.
- Two models hold Records that are never canonical at all (I-104). Their authority, where they
  have one, is real within their domain and confers no canonicality.

## 9. Authority and Source-of-Truth Classification

Artifact 050 classifies where a fact lives: `AUTHORITATIVE` · `DERIVED` · `CACHED` · `TEMPORARY` ·
`EXTERNAL` (§29.6a). This contract concerns who or what holds legitimate power within a domain.

**They share a word and nothing else.**

| | Source-of-truth class `AUTHORITATIVE` | Authority / authority |
|---|---|---|
| Answers | *"This is where the fact lives"* (§29.6a) | who may commit canon; what power holds within a domain |
| Applies to | a data class | a position, or a domain |
| Owner | Artifact 050 | the Spine; this contract; each model |

A Record may be the `AUTHORITATIVE` source for its domain's fact. That does not make the Record the
constitutional Authority, does not give it authority over anything outside its domain, and does not
make it World Canon. Conversely, the constitutional Authority is not a source-of-truth class.

This contract does not modify, re-specify or duplicate Artifact 050.

## 10. Authority and Canonicality

Authority answers who or what holds legitimate power within a defined scope. Canonicality answers
whether, and how, a Record Model treats a Record as canonical under its own semantics (§13.7c,
I-104).

None of the following holds, in any model, by virtue of this framework:

```
authoritative   ⇒  canonical              ✗
authority       ⇒  canonicality           ✗
canonical       ⇒  universal authority    ✗
```

The canonicality framework is **Artifact 052**, which depends on this one (`051 → 052`). No
canonicality meaning, table or gate is stated here.

## 11. The Human Gate and the Mutation Coordinator

Three things, separate and connected:

```
the Authority              — the one human position (§10.1)
      ↓   acts at
the Human Gate             — the stage of the one path (Spine law 2, §12.6)
      ↓   enforced by
the Mutation Coordinator   — "the only thing in coolboy12 that writes canon" (§12.6, I-83)
      ↓
a canonical commit         — atomic, with its changelog and its reason (§12.6)
```

- Spine law 2: canon changes *"only through propose → check → human gate → commit → changelog →
  log. No other route; the commit is atomic"*.
- The Mutation Coordinator's responsibilities include *"enforce the Human Gate"* (§12.6). It
  enforces the gate; it does not hold the Authority.
- §12.6 names the Coordinator *"so that the path cannot be assembled out of parts that each hold a
  piece of the authority."*
- *"External components may implement individual stages … **None of them may redefine
  authority.** A stage may be delegated; the boundary may not."* (§12.6; I-83)

This contract states the relationship only. The Human Gate's form and the Mutation Coordinator's
interfaces, transactions and behaviour belong to their own artifacts.

## 12. Delegation

Blueprint §10.1: *"Delegation is not possible — the Authority may take advice from anyone and may
not lend the commit."*

| May be delegated | May not be delegated |
|---|---|
| advice, analysis, critique, audit | the commit |
| generating proposals, drafts, simulation deltas | the gate decision |
| implementing a stage of the path (§12.6) | the write boundary (§12.6) |

Spine law 6: *"Every AI proposal, simulation delta, and emergent seed is provisional until gated.
Every AI action is advisory unless explicitly approved."* An AI role may generate, advise, question,
critique, audit and propose. It never holds the Authority, and approval of its output is the
Authority's act, not a transfer of the position.

There is no temporary, proxy, emergency, deputy or agent Authority in the sources, and none is
created here.

## 13. Absence and Succession

**Absence.** Blueprint §10.1: *"If there is no Authority, the descending current is closed (P-19)
and the ascending current continues in reduced mode."* On unavailability *"the system enters
**read-only** … and remains there: canon, history, replay, search, and every projection stay fully
available, and nothing commits."*

```
no Authority  →  nothing commits  →  the descending current is closed
```

**Succession.** Blueprint §10.1, stated as rules:

- Transfer is possible, and is a **Foundational-ceremony act** recording *"who held it, who holds it
  now, from when, and why."*
- **Succession happens outside the system** — *"by whatever personal, legal, or organizational
  arrangement the author has made"*.
- It is recognized *within* the system **on the first act of the new Authority**, which records who
  succeeded whom, from when, and on what basis.
- **The system never appoints, infers, or elects an Authority.**
- Succession creates no boundary in canon or in the authoring sequence; a predecessor's decisions
  bind the successor *"exactly as canon binds anyone"*; a successor changes them only *"by the
  ordinary means and no others"*; and a returning Authority is recognized by the same act.

This contract states those consequences and specifies no mechanism for them. Runtime read-only
behaviour belongs to its own artifacts, and the recording of a transfer is as §10.1 states it —
this contract does not redesign temporal packaging (Artifact 049; I-90).

## 14. Model Sovereignty

The framework is shared by all six Record Models — **W** · **E** · **P** · **R** · **V** · **I**.
The authority semantics are not.

```
shared constitutional framework          — this contract
        ↓
domain-scoped authority                  — RMS §17
        ↓
model-owned semantics                    — each Record Model (RMS §6)
        ↓
no leakage across models                 — I-101, I-103
```

- **I-101** — no Record Model is a specialization of another or the template for another. World is
  the most mature model and is not the authority template for E, P, R, V or I.
- **I-103** — *"Shared infrastructure never confers shared meaning."* A shared framework is not a
  shared authority semantics.
- **I-105** — Registry *"holds semantic authority over definitions and never semantic ownership of
  another model's Records."* Registry is not a super-authority.
- No model inherits another's authority semantics, and none is required to share an authority
  lifecycle, field or structure with another.

## 15. Infrastructure and External Components

Blueprint §26.2a: *"**Repositories provide capabilities. They do not define coolboy12 semantics.**"*
I-84: no external component *"holds canonical semantics, defines a kind, owns a relationship,
adjudicates a mutation, or is the only place a canonical fact exists."*

Guard rails are defence-in-depth, never the Authority. Blueprint §12.6:

> *"Where an execution substrate offers its own guard rails — permission scopes, pre-write hooks,
> tool allowlists — those are welcome and are **defence-in-depth, never the constitutional
> authority** … If the two ever disagree about whether something may be committed, the gate is
> right and the guard rail is a bug."*

I-83 carries the same rule. So none of the following is the Authority, or confers it:

- a repository hook — including this repository's own canon write-deny hook (Artifact 022), which
  blocks direct writes to `canon/**` and is defence-in-depth in exactly this sense. Its metadata
  reads `Auth: enforcing`: an artifact's domain-scoped metadata (Artifact 003), not the Authority;
- an operating-system, database or API permission;
- a tool allowlist or an AI tool restriction;
- a validator, adapter, repository or index;
- an AI coworker role.

**Source condition recorded, not resolved.** The quoted §12.6 passage cites *"Section 26.5"* for
this rule. The current Blueprint has no Section 26.5 heading. The rule is cited here to §12.6,
where its text stands, and to I-83; the dangling cross-reference is the Blueprint's, and is not
corrected here.

## 16. Provenance

Provenance answers *"Who made this, when, and why"* (Blueprint §13.7b); Artifacts 047 and 048 hold
its capture and its meaning boundary. **A recorded `who` is evidence, not authorization.** It
records who acted; it does not grant anyone the power to act, and it does not identify the
Authority by being filled in. The same holds for audit's *"by whose act"* (Artifact 049): a record
of an act, not the source of its legitimacy.

## 17. Temporal Vocabulary

This contract introduces no temporal term, clock, axis, epoch or versioning of its own. Where
Authority transfer and succession are mentioned, §10.1's words are preserved. The separation of
provenance, audit, history, revision, version and the retired word is Artifact 049's.

## 18. Prohibited Architectural Moves

| | Move | Why prohibited |
|---|---|---|
| **A** | **Universal authority semantics** — one meaning of authority for all six models | RMS §17; I-103 |
| **B** | **Universal authority boolean** — a true/false authority flag on Records | RMS §17; Blueprint §13.7a |
| **C** | **Universal authority schema** — an authority field, level, status or scope on every Record | Blueprint §13.7a; RMS §4 |
| **D** | **Record = authority** — treating a Record's existence or storage as authority | RMS §17; Blueprint §13.6c |
| **E** | **Record = Canon** | Blueprint §13.0; I-104 |
| **F** | **Authority = canonicality** | Blueprint §13.7c; I-104 |
| **G** | **SoT class = the Authority** — reading `AUTHORITATIVE` as the constitutional position | Blueprint §29.6a, §10.1 |
| **H** | **World as authority template** | I-101; Blueprint §13.6 |
| **I** | **Registry as super-authority** | I-105 |
| **J** | **AI as the Authority** | Blueprint §10.1; Spine laws 3, 6 |
| **K** | **Delegated commit** — lending, proxying or deputizing the commit | Blueprint §10.1 |
| **L** | **Dual Authority** — two parties holding the position at once | Blueprint §10.1; I-03 |
| **M** | **Automatic succession** — the system appointing, inferring or electing an Authority | Blueprint §10.1 |
| **N** | **External-component authority** — a component adjudicating a mutation or holding canonical semantics | Blueprint §26.2a; I-84 |
| **O** | **Guard rail as authority** — a hook, permission or allowlist treated as constitutional | Blueprint §12.6; I-83 |
| **P** | **Provenance as authorization** — a recorded `who` granting power | Blueprint §13.7b; §16 |
| **Q** | **Authority inheritance across models** | I-101; I-103 |
| **R** | **Universal authority lifecycle** | Blueprint §13.7a |
| **S** | **A model's authority meaning defined here** | RMS §6; §3 |
| **T** | **Framework as access control** — this contract read as roles, permissions, credentials or an access-control system | Blueprint §10.1, §12.6; §3 |

## 19. Worked Examples

**Every example below is illustrative and non-normative.** It shows where a boundary falls. It
defines no model's authority, canonicality, schema or ceremony.

### Example A — A World Record

A World CHARACTER Record is authoritative within World's domain, as World defines it. That makes the
Record neither the Authority nor Canon in any other model: a change to it becomes canon only through
the one path, at the Human Gate, written by the Mutation Coordinator. And World's arrangement is not
a template — no other model's authority is read from it (I-101).

### Example B — A Registry definition

A Registry definition is authoritative about the meaning it defines. I-105 draws the line: Registry
*"holds semantic authority over definitions and never semantic ownership of another model's
Records."* A World Record that resolves that definition remains World's Record; the Registry's
authority over the definition gives it none over the World instance.

### Example C — An Epistemic Record

An Epistemic Record belongs to the model that answers *"Who knows, believes, suspects, or has been
shown what?"* (RMS §6) — not *"What is true of the world?"*, which is World's question. Whatever
authority E defines over its own subject matter, it reaches E's question and not World's, and it is
not inherited from World. What E's authority means is E's to state.

### Example D — Production, Issue and Visual

- **Production.** Production State is `AUTHORITATIVE` *"about the plan"* (§29.6a) and *"never
  authoritative about the world"* (§13.6). The same Record is authoritative in one domain and not in
  another, and Production is never canonical (I-104).
- **Issue.** An Issue Record is authoritative about the published artifact and is *"Not Canon"*
  (§13.6): *"a World object never becomes an Issue object by being published"* (§13.6), and nothing
  is true because it is printed (Spine law 5).
- **Visual.** *"V holds the objects. It does not hold the authority."* (§13.6c). A Visual Record's
  existence confers no authority over what it depicts.

In each case the Record exists, is held by its model, and may be authoritative within its domain —
and none of that makes it World Canon.

## 20. Conformance Conditions

Stated so they are checkable. **Artifact 059** owns the P2 kernel conformance suite; this document
implements no test and is `T: doc`. These are conditions of this contract, not Blueprint invariants;
no `051.x` invariant is minted.

| ID | Condition | Basis |
|---|---|---|
| **C-01** | Where an Authority exists, there is exactly one at a time. | Blueprint §10.1; I-03 |
| **C-02** | The Authority is a human position, never an AI, automation, schedule or default. | Blueprint §10.1; Spine law 3 |
| **C-03** | Only the Authority commits canon. | Spine law 3; I-03 |
| **C-04** | The commit is not delegable; advice is. | Blueprint §10.1 |
| **C-05** | With no Authority, nothing commits. | Blueprint §10.1; P-19 |
| **C-06** | The system never appoints, infers or elects an Authority. | Blueprint §10.1 |
| **C-07** | Every authority claim is scoped to a domain and does not extend beyond it. | RMS §17 |
| **C-08** | A Record is not Canon. | Blueprint §13.0; I-104 |
| **C-09** | Authority does not imply canonicality. | Blueprint §13.7c; I-104 |
| **C-10** | Source-of-truth class `AUTHORITATIVE` is not the Authority. | Blueprint §29.6a, §10.1 |
| **C-11** | No model's authority semantics are the template for another's. | I-101 |
| **C-12** | Registry's authority over definitions confers no ownership of another model's Records. | I-105 |
| **C-13** | No infrastructure, external component or guard rail is the Authority. | Blueprint §12.6, §26.2a; I-83; I-84 |
| **C-14** | A recorded provenance `who` confers no authority. | Blueprint §13.7b; §16 |
| **C-15** | No universal authority field, boolean, schema, level or lifecycle is defined. | Blueprint §13.7a; RMS §4 |
| **C-16** | No model's authority meaning or ceremony is defined here. | RMS §6 |
| **C-17** | No canonicality meaning, table or gate is defined here. | Roadmap rows 052, 145 |
| **C-18** | The document contains no executable content and mints no Record, Kind, field or invariant. | Roadmap row 051 `T: doc` |

A construction satisfying all eighteen is conformant **to this contract**. It is not thereby
conformant to the Record System: the other P2 contracts carry their own conditions.

## 21. Source Traceability

| Rule or boundary | Source |
|---|---|
| Record ≠ Canon; all authority is domain-scoped | RMS §17 |
| Record and Canon are not synonyms; canonicality is model-defined | I-104; Blueprint §13.0 |
| Only the human commits canon | Spine law 3 |
| One Authority, human, never two; a position, not a person | Blueprint §10.1; I-03 |
| Delegation impossible; advice from anyone | Blueprint §10.1 |
| No AI, automation, schedule or default exercises the Authority | Blueprint §10.1 |
| No Authority → descending current closed; read-only | Blueprint §10.1; P-19 |
| Succession outside the system; recognized on first act; never appointed | Blueprint §10.1 |
| Canon changes only through the one atomic path | Spine law 2; Blueprint §12.6 |
| Canon is exactly the committed record | Blueprint §12.1 |
| Canon tiers rank canonical statements, not authority | Blueprint §12.2 |
| The Mutation Coordinator is the only writer; enforces the Human Gate | Blueprint §12.6; I-83 |
| A stage may be delegated; the boundary may not; none may redefine authority | Blueprint §12.6; I-83 |
| Guard rails are defence-in-depth, never constitutional authority | Blueprint §12.6; I-83 |
| Repositories provide capabilities, not semantics | Blueprint §26.2a |
| No external component holds canonical semantics or adjudicates a mutation | I-84 |
| AI output is provisional and advisory | Spine law 6 |
| Per-model authorizing acts differ | Blueprint §13.7c |
| Wherever Records are canonical, the one path and the one committer apply | Spine law 2; I-03; Blueprint §13.6 |
| Artifact metadata `Auth:` is domain-scoped and is not the Authority | Artifact 003, field 9 |
| Production State authoritative about the plan, never about the world | Blueprint §29.6a, §13.6 |
| V holds the objects, not the authority | Blueprint §13.6c |
| Issue is not Canon; publication does not make canon | Blueprint §13.6, §13.6a; Spine law 5 |
| Registry holds authority over definitions, never ownership of others' Records | I-105 |
| No model is a template for another | I-101 |
| Shared infrastructure never confers shared meaning | I-103 |
| Model-owned Record semantics | RMS §6 |
| Semantic ownership is not change authority | Artifact 042 |
| Source-of-truth classification | Blueprint §29.6a; Artifact 050 |
| Provenance captured and bounded | Blueprint §13.7b; Artifacts 047, 048 |
| Temporal vocabulary | Artifact 049 |
| Hard dependency on 039; unlocks 052 and all models | Roadmap row 051 |
| Canonicality framework depends on this one | Roadmap row 052 |
| Cross-model dependency rules depend on this one | Roadmap row 058 |

Downstream, `051 → 052`, `051 → 058`, and each model's own authority contract depend on this
framework. None has yet defined its semantics, and none inherits semantics from this document.

---

*Artifact 051 · P2/2c · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the authority boundary derived from the Spine, Master Blueprint §10.1, §12.6,
§13.0 and §13.7c, and RMS §17. It does not amend them. It is not a Record, holds no canonical data,
and defines no model's authority, no canonicality, no schema, no role and no permission. Where it
differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those
governing sources are correct and this document is wrong.*
