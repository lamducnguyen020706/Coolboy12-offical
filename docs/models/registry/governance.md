# COOLBOY12 — Registry Governance Model

**Artifact 065** · Registry governance model · `docs/models/registry/governance.md` · Own: R ·
RM: R · T: doc · R: GOV · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P3/3a · Req: RR-34 · BP: §9.4 · RMS: §21 · H: 064 · S: — · LS: — · G: — · → 108 ·
Val: who may propose, approve, deprecate a definition · Done: model · Why: definitions are canon
about meaning · Risk: high · ∥: no

## 1. Purpose

This model answers one question — **who may propose, approve and deprecate a Registry definition?**

Registry definitions are not inert configuration. They are Registry Records carrying the meaning
other Records resolve against, so a change to one is a governed semantic change. Row 065's `Why`
states the reason: *"definitions are canon about meaning"*. This document turns row 065's `Val` —
*"who may propose, approve, deprecate a definition"* — into decision rights that later work can
apply without guessing:

```
who may originate a proposed change        §8
who checks it, and what a check can do     §7, §9
who approves or rejects it                 §9
who may propose and authorize deprecation  §10
who merely writes the approved change      §7, §9
who defines the temporal mechanics         §18 (108–110)
```

It keeps apart: proposing, checking, approving at the gate, Registry semantic authority, the
constitutional Authority, the mechanism that writes an approved change, deprecation authorization,
and the downstream semantics of evolution, versions, supersession and deprecation.

## 2. Constitutional Status

`Own: R` · `RM: R` · `T: doc` · `R: GOV` · `SoT: AUTHORITATIVE` about Registry governance ·
`Auth: governing` · `Canon: n/a` · `CD: no`. This document is not a Registry Record, holds no
Registry data, and creates no definition, role, field or Record. Where it differs from the Master
Blueprint, the Record Model System, or the OS File Build Roadmap, **those sources are right and
this document is wrong.**

`Req: RR-34` is reproduced from row 065. The requirement register is not in the supplied source
set, so the ID is carried forward unverified and no requirement text is stated for it (GAP-C;
Revolving Resolution Note; SC-065-G).

## 3. Scope

**In scope.** Who may originate a proposal to create or change a Registry definition; a proposal's
standing before approval; who may approve or reject it; who may propose and who may authorize
deprecation; the separation between the approving Authority and the mechanism that writes the
approved change; the relation between Registry semantic authority and the constitutional
Authority; why a check cannot become approval; why direct edits are not a governance route; the
boundary between ordinary Registry content change and architectural amendment; the constraints
governance inherits from references, ownership, sovereignty and the fourteen-Kind taxonomy; the
handoff to 108.

**Out of scope, by owner.**

| Not defined here | Owner |
|---|---|
| the fourteen Registry Kinds and their admission rationale | 064 (consumed, §6) |
| definition-family meaning, fields, schemas and content | 066–107 |
| definition evolution and its temporal account | 108 |
| version syntax, pinning, lookup | 109 |
| what supersession and deprecation mean and how they behave | 110 |
| concrete definition-dependency rules | 111 |
| reference validation and the Registry validation suite | 112, 116 |
| the proposal model and its basis requirement | 146, 147 |
| the six model-specific canonical gates, including the Registry's | 145 |
| the Mutation Coordinator | 152 |
| how a new Kind, field or definition class is added | 459 |

No schema, field, enum, role object, Registry data, validator, algorithm or test is created.

## 4. Governing Sources and Precedence

```
Master Blueprint + RMS        architecture; RMS v1.0 closes stale Blueprint wording where it says so
        ↓
Roadmap (REPAIRED)            decomposition, metadata, Val, Done, handoffs
        ↓
frozen artifacts; Artifact 003 conventions
        ↓
Artifact 065
```

| Source | What it gives this model |
|---|---|
| Blueprint §10 (Spine laws 2, 3, 6); §10.1 | the one path; only the human commits canon; AI output provisional; the Authority is one human position; delegation of the commit is not possible |
| Blueprint §12.6; I-03; I-83 | the Mutation Coordinator writes canon and enforces the Human Gate; no stage may redefine authority |
| Blueprint §9.4 | architecture frozen, content extensible; architecture *"changes only by amendment"* |
| Blueprint §13.6e; I-105 | Registry definitions are Records with *"a governed change path"*; *"Registry governs the definitions. Each Record Model owns its Records."* |
| Blueprint §13.7c | Registry canonical *"about meaning"*; its authority column reads *"Registry change (§9.4)"* (SC-065-H) |
| Blueprint §26.8 | Registry definitions write-protected against direct edit; proposals freely writable; the author must review every Registry change |
| Blueprint P-22 | a proposal declares its basis and returns re-validated, *"never as approved"* |
| RMS §10, COLLISION-1; §10.1; §10.3 | Registry sovereign; fourteen Kinds `FROZEN`; the current reference boundary |
| RMS §17; §19; §25 | authority is domain-scoped; definition management is R's; governance is classified *"Spine/R"* |
| RMS §21; Appendix F | the pointer to Deliverable I, which is not present (SC-065-D) |
| Roadmap rows 064, 065, 108–112, 145–147, 152, 459 | this artifact's identity and its neighbours' responsibilities |
| Artifact 064 (`H: 064`) | the frozen fourteen-Kind taxonomy |
| Artifacts 051, 052, 060, 061, 063 | the one Authority and delegation; Registry canonicality; Registry as a sovereign model; the authority boundary; governance constraints GC-1 to GC-5 |

Each statement below is marked as a **source fact** or as **required synthesis** — a conclusion
this Roadmap artifact draws from source facts together. Synthesis creates no new entity.

## 5. Governance Terms Kept Apart

| Term | Meaning here | Is not |
|---|---|---|
| **proposal** | a provisional request to create, change or deprecate a Registry definition | a write, an approval, canon |
| **check** | the *check* stage of the one path: validation, reference legality, constraint and conformance checks | approval |
| **Human Gate** | the stage of the one path at which the decision is made | a person, a service, a Record |
| **the Authority** | the one human position that commits canon (§10.1) | a role object, account, committee, Record or software principal |
| **Registry semantic authority** | Registry's domain-scoped authority over definition meaning (RMS §17; I-105) | the Authority; change authority; ownership of other models' Records |
| **Mutation Coordinator** | the sole writer of canon, which enforces the gate (§12.6) | an approver |
| **Registry change** | the Registry-domain change path named by §9.4 and §13.7c | a second Authority (SC-065-H) |
| **deprecation authorization** | the decision that a definition is to be deprecated | deprecation mechanics (110) |
| **amendment** | the change mechanism for frozen architecture | an ordinary Registry change |

## 6. Inherited Frozen Inputs

**From Artifact 064 (`H: 064`).** RMS §10.1 and Artifact 064 close the Registry taxonomy:
*"Final Kind taxonomy — CLOSED at fourteen"*. This model adds, removes and renames no Kind, creates
no governance Kind, and defines no admission ceremony. A Kind is not its `KIND-DEFINITION` (064
§22). Artifact 064 hands this model *"who may propose, approve, deprecate a definition"* (064 §27)
and leaves evolution, versioning, supersession and deprecation to 108–110 (064 §3).

**Registry is a sovereign Record Model** (source fact, RMS §10): its Records are
*"semantic-definition Records — not configuration, not code constants, not metadata, not a
catalog, not runtime"*. Blueprint §9.4's *"Classification: capability"* is stale (RMS §10,
COLLISION-1; SC-065-A).

**Registry definitions are Records with a governed change path** (source fact, Blueprint §13.6e):
a definition is *"a Registry Record with identity under the universal grammar (§13.9a), provenance,
a governed change path, and a temporal account"*, promoted because definitions were otherwise
*"governed by convention instead of by rule"*. This model governs who may change them, not their
Record shape.

**Registry is canonical about meaning** (source fact, Blueprint §13.7c; Artifact 052 §5.4): *"This
definition is the authoritative meaning records resolve against"*; *"Registry owns meaning, not
World Truth"* (Blueprint §13.6). Approval authorizes a proposed definition change to proceed
through the governed write path; the committed Registry definition is the authoritative meaning
Records resolve against. That meaning is never a fact of the world.

**Authority boundary** (source fact, §13.6e; I-105; Artifact 061): *"Registry governs the
definitions. Each Record Model owns its Records."*

## 7. The Core Governance Rule

> **A Registry definition is created, changed or deprecated only through the one path. A proposal
> may be originated or drafted by source-supported proposal-producing actors: the sources
> explicitly support human-originated proposals and AI-assisted or delegated proposal generation,
> and this model creates no exhaustive proposer-role taxonomy. A proposal carries no authority.
> Checks constrain what may be approved and never approve. The current human Authority approves or
> rejects at the Human Gate; approval authorizes the governed write and is not itself committed
> state. The Mutation Coordinator writes the approved change and approves nothing. The committed
> Registry definition carries the authoritative meaning; Registry semantic authority governs that
> meaning, is not the Authority, and decides no gate.**

```
Registry definition
     │  proposed change — human-originated or AI-assisted
     ▼
proposal ........................ provisional; not a write; not canon
     │
     ▼
checks .......................... constrain legality; never approve
     │
     ▼
the current human Authority, at the Human Gate
     ├── reject, or return as changed
     └── approve ................ authorizes the mutation; not yet committed state
             │
             ▼
     Mutation Coordinator ....... the governed write; approves nothing
             │
             ▼
     committed Registry definition
             │
             ▼
     authoritative meaning Records resolve against
```

**Source facts.** Spine law 2: canon changes only through *"propose → check → human gate → commit →
changelog → log. No other route; the commit is atomic"*. Spine law 3: *"Only the human commits
canon."* Blueprint §26.8: *"Canonical records and Registry definitions are write-protected against
direct edit. Every canonical write goes through the Mutation Coordinator."*, and the author *"must
review every canonization, every Registry change"*. RMS §25 classifies governance as *"Spine/R"*.

**Synthesis.** Registry definitions are canonical about meaning and write-protected, and every
Registry change requires the author's review; the Spine fixes one path and one human commit
position. Registry governance is therefore that path applied to Registry definitions — not a
second path, and not a second Authority.

## 8. Proposal Rights

**Source facts.**

- Proposal is the first stage of the one path (Spine law 2).
- Blueprint §26.8: *"Proposals are freely writable. AI-assisted work drafts into a proposal area;
  nothing there is canon until it passes the gate."* The environment *"proposes canon mutations"*
  and *"may never directly change"* any *"Registry definition"*.
- Spine law 6: *"Every AI proposal, simulation delta, and emergent seed is provisional until gated.
  Every AI action is advisory unless explicitly approved."*
- Blueprint §10.1: *"the Authority may take advice from anyone and may not lend the commit."*
- Blueprint P-22: a proposal *"records the canonical state it was computed against"*; if canon has
  moved it is re-validated, and if that changes it materially it *"returns to the author as
  changed, never as approved"*.

**Rules (synthesis).**

| ID | Rule |
|---|---|
| **PR-1** | A human may originate a proposal to create, change or deprecate a Registry definition. |
| **PR-2** | AI-assisted, proposal-producing work may draft such a proposal. Its draft is provisional and advisory (Spine law 6). |
| **PR-3** | Proposing requires no semantic, approval or commit authority, and grants none. A proposal is not a write, not canon, and not Registry meaning. |
| **PR-4** | A proposal's author gains nothing from authorship: an AI author may not gate it, and a human author may not edit the definition directly. |
| **PR-5** | PR-1 and PR-2 identify source-established proposer cases; they are not an exhaustive proposer-role taxonomy. No closed list of proposer roles exists in the sources, and none is created. No persistent *proposer* role, Record or field is introduced. |
| **PR-6** | A proposal's form, its basis and evidence are 146's and 147's; this model states only who may propose. |

## 9. Approval and Rejection Rights

**Source facts.**

- Spine law 3; I-03: *"Only the Authority commits, and there is exactly one Authority at a time."*
- Blueprint §10.1: the human is *"a position, not a person: there is exactly one Authority at any
  moment, it is always held by a human, and it is never held by two parties simultaneously"*;
  *"An AI role may never hold it, and no automation, schedule, or default may ever exercise it in
  the Authority's absence."*
- Blueprint §26.8: the author must review *"every Registry change"*.
- Blueprint §12.6: *"The Mutation Coordinator is the only thing in coolboy12 that writes canon."*;
  its responsibilities include *"enforce the Human Gate"*; external components may implement
  stages, and *"None of them may redefine authority."*
- RMS §17: *"All authority is domain-scoped."* Artifact 051 §6 keeps the Authority and
  domain-scoped authority apart.

**Rules (synthesis).**

| ID | Rule |
|---|---|
| **AP-1** | Approval or rejection of a Registry-definition change is a human governance decision made by the current constitutional Authority at the Human Gate. |
| **AP-2** | No AI, Registry Record, validator, schema, reference, semantic layer, runtime component or service approves in the Authority's place. |
| **AP-3** | A check that passes leaves the proposal a proposal; a check that fails constrains what may be approved. Check results inform the decision and are never the decision. |
| **AP-4** | The Mutation Coordinator performs the approved write and enforces the gate. It holds no approval right; being the writer confers none. |
| **AP-5** | Registry holds semantic authority over the meaning carried by the committed Registry definition. Approval authorizes the proposed change to proceed through the governed write path; approval alone does not create authoritative Registry state. Registry semantic authority decides no gate and is not change authority (Artifact 061 §14). |
| **AP-6** | The decision may not be delegated: the Authority may take advice from anyone and may not lend the commit (§10.1; Artifact 051 §12). |
| **AP-7** | With no Authority, no Registry definition changes: nothing commits (§10.1; Artifact 051 §13). |
| **AP-8** | No second approver exists: no Registry Authority, definition authority, committee, hierarchy or quorum. The sources create none. Nor does any source require that proposer and approver be different people; none is created. |
| **AP-9** | An approval cannot make a check-forbidden change legal. A change that frozen architecture forbids needs amendment, not approval (§11). |

What the Human Gate requires of a Registry proposal before it may pass — the Registry's canonical
gate — is row 145's (*"six model-specific canonical gates defined; no single universal gate"*), and
its enforcement is 152's. This model names who decides, not the gate's form.

## 10. Deprecation Authorization Boundary

Row 065 assigns *"deprecate"* to this model. Row 110 assigns what deprecation means:
*"deprecated ≠ deleted"*.

**Synthesis.** For authority purposes a deprecation is a Registry change: it alters the governed
standing of a definition that Records resolve against, and the author must review every Registry
change (§26.8). Therefore:

| ID | Rule |
|---|---|
| **DP-1** | Deprecation may be proposed by anyone who may propose under §8, on the same terms. |
| **DP-2** | A deprecation proposal deprecates nothing. |
| **DP-3** | Only the current human Authority, at the Human Gate, may authorize a definition's deprecation. |
| **DP-4** | The authorized change is written only by the governed write path. |
| **DP-5** | Deprecation is not deletion (row 110), and deprecation authorization is not deprecation mechanics. |

Not defined here: deprecation states, fields or lifecycle values; version numbering; replacement
selection; supersession; retention or tombstones; whether references to a deprecated definition
still resolve; deletion rules; compatibility policy. Those are 108–110's.

## 11. Architecture vs Content Change

**Source fact.** Blueprint §9.4: *"Registry architecture is frozen; Registry content is
extensible."* The architecture *"is settled and changes only by amendment"*; the content *"extends
by ordinary Registry change, at any time, without touching this blueprint"*.

```
ordinary Registry definition / content change    →  this governance model applies
frozen Registry or Record System architecture    →  that architecture's amendment mechanism
                                                     never an ordinary Registry proposal
```

**Rule (synthesis).** Ordinary Registry governance governs Registry content. An approval at the
Human Gate under this model cannot amend frozen architecture; labelling an architectural change a
Registry proposal does not make it ordinary. The following are not legalized by this model:

- creating a seventh Record Model (RMS §2; I-101);
- letting Registry own World instances, or any other model's Records (I-105);
- adding a universal lifecycle, canonicality, status or state model (RMS §4);
- bypassing the RMS §10.3 reference boundary (Artifact 063 GC-2);
- changing the fourteen-Kind Registry taxonomy (RMS §10.1; Artifact 064; SC-065-C);
- turning Registry into runtime (RMS §10);
- letting AI hold the Authority (§10.1);
- adding a second canonical write path (Spine law 2; I-83).

Which amendment mechanism applies to which frozen rule is not defined here. Spine law 7 — certain
changes *"can never be treated as trivial"* — applies wherever its subjects are touched.

## 12. Constraints Inherited from References and Ownership

**References** (Artifact 063 §15; RMS §10.3). Governance may not approve a reference outside the
admissible target categories (GC-1); may not waive the domain-instance prohibition (GC-2); may not
treat a target as declared before its declared status is established (GC-3); judges a changed
target afresh (GC-4); and turns no domain instance into a declaration and no current value into
meaning (GC-5). Blueprint §9.4's older blanket *"may never reference a kind"* wording is not current
law: RMS §10.3 corrects it (SC-065-B).

**Ownership and sovereignty** (§13.6e; I-105; Artifact 061). An approved definition gives Registry
no ownership of domain instances, no authority over domain state, and no other model's lifecycle,
canonicality, temporal mechanism or Kind taxonomy. Approving a `KIND-DEFINITION` admits no Kind
(Artifact 057 C-057-08).

**Domain scope** (RMS §17). Registry governance is Registry-domain governance. It is not a
governance model W, E, P, V or I inherit, and their own ceremonies are theirs.

**Envelope** (RMS §4). The universal envelope stays `partition` · `kind` · `object_id` · `slug` ·
`provenance` · `registry_ref` · `sot_class`. No approval, reviewer, governance status, version,
deprecation, lifecycle, authority or canonical field is added to it or to any Record.

## 13. Decision-Rights Matrix

| Question | Answer | Basis |
|---|---|---|
| Who owns a definition Record? | the Registry Record Model | RMS §10; I-105; 060 |
| Who holds semantic authority over a definition? | Registry, within its domain | RMS §17; I-105; 061 |
| Who may originate or draft a proposal? | source-supported proposal-producing actors: explicitly, a human may originate, and AI-assisted or delegated work may draft or generate, a proposal. These are established cases, not a closed proposer-role taxonomy; proposing grants no authority | §8 (PR-1 to PR-5); Artifact 051 §12 |
| Who checks legality and conformance? | the check stage, through the mechanisms assigned elsewhere (112, 116, 145, 147); checks constrain, never approve | §9 (AP-3) |
| Who approves or rejects? | the current human Authority, at the Human Gate | §9 (AP-1, AP-2) |
| Who writes an approved change? | the Mutation Coordinator; it approves nothing | §9 (AP-4); row 152 |
| Who may propose deprecation? | anyone who may propose under §8 | §10 (DP-1) |
| Who may authorize deprecation? | the current human Authority, at the Human Gate | §10 (DP-3) |
| Who defines deprecation mechanics? | 108–110, chiefly 110 | rows 108–110 |
| Who owns the domain Records a definition describes? | their own Record Model; never Registry | §13.6e; I-105 |
| Who may change frozen architecture? | its amendment mechanism, not this model | §11 |

## 14. Worked Examples

All examples are **schematic**: no ID is minted, and nothing here is Registry data.

**Legal — AI-assisted proposal.** AI-assisted work drafts a correction to a
`CONTROLLED-VOCABULARY` definition into the proposal area. The draft is provisional. The applicable
checks run. The current human Authority reviews it at the Human Gate and approves or rejects it.
Only after approval does the Mutation Coordinator write the change. *Drafting is not approval.*

**Legal — human-originated proposal.** The person who currently holds the Authority originates a
change to a `FIELD-DEFINITION`. It still passes check and the Human Gate, and is still written by
the Mutation Coordinator. *Proposal authorship and approval authority are distinct even when the
same person holds both;* no source requires a second person, and none is required here.

**Illegal — automatic approval.** A validator returns GREEN and a service then commits the
definition. The service has taken the gate decision. *Illegal:* a check is not approval (AP-3), and
no automation may exercise the Authority (§10.1).

**Illegal — a Record as approver.** One Registry definition states that another is approved.
*Insufficient and illegal as governance authority:* a Record does not hold the Authority because
Registry owns meaning (AP-2; Artifact 051 §9).

**Illegal — direct edit.** A runtime tool or session edits a governed Registry definition in place.
*Illegal path:* Registry definitions are *"write-protected against direct edit"* (§26.8), and a
direct write substitutes for no stage of propose → check → Human Gate → governed write.

**Illegal — approved reference to an instance.** A proposal makes a definition reference a specific
World Character, and the Authority approves it. *Still illegal:* governance cannot waive the
domain-instance prohibition (GC-2); lifting it would be an amendment of RMS §10.3.

**Boundary — deprecation.** Proposal: deprecate definition X. This model answers who may propose it
(§8) and who may authorize it (the Authority, DP-3). It does not answer what replaces X, whether
references to X still resolve, how long X persists, how supersession is represented, or how a
consumer pins a version — 108–110's.

**Deferred — a fifteenth Registry Kind.** Proposal: add a fifteenth Registry Kind. This is not an
ordinary definition-content proposal: RMS §10.1 freezes the taxonomy at fourteen (064). How a new
Kind is added belongs to row 459 — *"each through its own ceremony, never through a generic
abstraction"* — not to this model.

## 15. Prohibited Inferences

| # | Invalid inference | Why it fails | Source |
|---|---|---|---|
| 1 | Registry governs definitions, so Registry owns domain instances | definitions are governed; Records are owned by their model | §13.6e; I-105 |
| 2 | Registry is canonical about meaning, so Registry is the constitutional Authority | the Authority is one human position | §10.1; I-03 |
| 3 | A Registry Record is authoritative, so it may approve changes | a Record holds no Authority | Artifact 051 §9 |
| 4 | `SoT: AUTHORITATIVE` confers approval authority | source-of-truth class is not authority | Artifact 050; 051 §9 |
| 5 | A legal reference transfers ownership or authority | references transfer neither | RMS §10.3; Artifact 063 §12 |
| 6 | A validator passes, so the proposal is approved | checks constrain; they never approve | AP-3 |
| 7 | A schema validates, so the definition may commit automatically | no automation exercises the Authority | §10.1; AP-2 |
| 8 | AI authored the proposal, so AI may gate it | AI never holds the Authority | Spine law 6; §10.1 |
| 9 | A human authored the proposal, so direct editing is permitted | definitions are write-protected | §26.8; PR-4 |
| 10 | The Mutation Coordinator writes the commit, so it is the approver | it enforces the gate; it does not hold it | §12.6; AP-4 |
| 11 | A deprecated definition is deleted | *"deprecated ≠ deleted"* | row 110 |
| 12 | Because 065 authorizes deprecation, 065 owns deprecation mechanics | mechanics are 108–110's | §10; rows 108–110 |
| 13 | Registry content is extensible, so 065 may add a fifteenth Kind | the taxonomy is closed at fourteen; extension is 459's | RMS §10.1; 064; row 459 |
| 14 | A higher semantic layer carries greater governance authority | layer order is not authority | Artifact 062 §11 |
| 15 | Approving a definition makes every target it references declared or legal | legality is judged against the reference boundary | GC-1, GC-3 |
| 16 | Registry governance is a universal governance model for W, E, P, V and I | authority is domain-scoped | RMS §17; RMS §4 |
| 17 | *"Registry change"* in §13.7c is a second Authority | it names the Registry change path, on the one path | SC-065-H |
| 18 | The Authority may approve an architectural change as an ordinary Registry proposal | architecture changes only by amendment | §9.4; §11 |
| 19 | A proposer, approver or reviewer role, Record or field exists because governance exists | no source creates one | PR-5; AP-8 |
| 20 | The Authority approved the proposal, so the proposed definition is already authoritative before the governed commit | approval authorizes the mutation; authoritative Registry meaning is carried by the committed Registry definition | §6; §7; AP-5 |

## 16. Source Conditions and Gaps

### SC-065-A — stale Registry classification — CLOSED AT SOURCE

Blueprint §9.4: *"Classification: capability (Section 29.1), owned by Canon."* RMS §10,
COLLISION-1: the line is *"stale and requires a Blueprint wording fix"*; Registry is a sovereign
Record Model. **Treatment:** the RMS closure is used; the stale line is not repeated as current
architecture.

### SC-065-B — older Registry reference wording — CLOSED AT SOURCE

Blueprint §9.4 and I-75 state a blanket prohibition on referencing a kind, a subtype or an
instance. RMS §10.3: *"v0.1 stated the boundary too bluntly"*, and *"R → R definitions = ALLOWED.
R → domain instances = FORBIDDEN."* **Treatment:** RMS §10.3 and Artifact 063 govern; governance
cannot waive them (§12).

### SC-065-C — taxonomy extensibility wording — CLOSED FOR THE CURRENT ROSTER

Blueprint §9.4 and §13.6e let the Registry roster extend *"by ordinary Registry change"*. RMS §10.1
closes the taxonomy at fourteen, `FROZEN`, and Artifact 064 states it. **Treatment:** this model
authorizes no fifteenth Kind through ordinary governance. How a new Kind is added is row 459's.

### SC-065-D — RMS §21 is a pointer — SOURCE GAP

RMS §21 reads *"Registry Governance — Appendix F / Deliverable I."*, and Appendix F reads
*"Registry Governance → Deliverable I."* Deliverable I is not in this repository (Artifact 061 §14
records the same). **Treatment:** it is not reconstructed or quoted. This model is built from the
source facts present. Committee composition, quorum, a named Registry reviewer, reviewer count,
separation of duties and escalation are not established, and none is invented.

### SC-065-E — row 064 does not list 065 as an unlock — DECOMPOSITION INCONSISTENCY

Row 065 declares `H: 064`; row 064's `→` is *"066–107"* and does not name 065. Artifact 003 expects
hard dependencies and unlocks to agree. **Treatment:** `H: 064` is kept as declared and 064 is
consumed (§6). The Roadmap is not edited here. Artifact 064 §27 records the same omission. Route:
ROADMAP ISSUE, non-blocking.

### SC-065-F — row 065 `→ 108` against row 108 `S: 065` — DECOMPOSITION INCONSISTENCY

Row 065 unlocks 108; row 108 lists 065 as a soft dependency (`H: 064,078 · S: 065`), not a hard
one. **Treatment:** both Roadmap declarations are preserved exactly. This artifact keeps `→ 108`;
row 108 remains `S: 065`, not `H: 065`. Under Artifact 003's dependency/unlock convention this is a
Roadmap/decomposition inconsistency, recorded as a non-blocking ROADMAP ISSUE. This artifact does
not repair the Roadmap and does not promote the soft dependency; 065's output is governance context
that 108 consumes, and 108 is not described as hard-blocked by 065.

### SC-065-G — requirement text unavailable

`Req: RR-34` is carried forward exactly. Its text is not in the source set (GAP-C). No compliance
with unread requirement text is claimed; this model is validated against row 065's `Val` and
`Done`, its BP and RMS citations, and the frozen artifacts it consumes.

### SC-065-H — §13.7c names *"Registry change"* as Registry's canonicality authority

Blueprint §13.7c's table gives World and Epistemic the authority *"The Human Gate"* and gives
Registry *"Registry change (§9.4)"*. **Treatment:** the entry names the Registry-domain change path,
not a second Authority. Spine law 3 binds all canon; §26.8 requires the author's review of *"every
Registry change"*; Registry definitions are write-protected and written only by the Mutation
Coordinator. Read together, *Registry change* runs on the one path and its decision is the
Authority's at the Human Gate (§7, AP-1). No other reading is available without creating a second
Authority, which §10.1 and I-03 forbid.

## 17. Conformance Conditions

| ID | Condition | Source |
|---|---|---|
| **C-065-01** | The header reproduces row 065's metadata exactly. | row 065 |
| **C-065-02** | The document states who may originate or draft a Registry-definition proposal, and that proposing carries no approval or commit authority; the source-supported human and AI-assisted or delegated proposer cases are documented without being presented as an exhaustive proposer-role taxonomy. | §7; §8 (PR-1 to PR-5); §13 |
| **C-065-03** | AI-assisted proposal work is stated to be provisional and advisory, and unable to approve or commit. | §8 (PR-2, PR-4); Spine law 6 |
| **C-065-04** | The current human constitutional Authority at the Human Gate is stated to be the approval and rejection authority for Registry-definition changes. | §9 (AP-1) |
| **C-065-05** | No Registry-specific Authority, committee, software principal, Record, semantic layer, validator or service is created as an approver. | §9 (AP-2, AP-8) |
| **C-065-06** | The Mutation Coordinator is kept distinct from the approval decision; approval authorizes a Registry-definition mutation but does not itself establish authoritative Registry state, and authoritative meaning is carried by the committed definition after the governed write. | §6; §7; §9 (AP-4, AP-5) |
| **C-065-07** | The document states who may propose deprecation and who may authorize it. | §10 (DP-1, DP-3) |
| **C-065-08** | No versioning, supersession, deletion, retention, lifecycle state or deprecation representation is designed; 108–110 receive it. | §10; §18 |
| **C-065-09** | Registry governs definition meaning without ownership of, or authority over, another model's Records. | §12 |
| **C-065-10** | No rule lets governance approve away the RMS §10.3 / Artifact 063 reference boundary. | §12; GC-1 to GC-5 |
| **C-065-11** | Ordinary Registry governance is stated to be unable to amend frozen Registry or Record System architecture. | §11 |
| **C-065-12** | No fifteenth Registry Kind and no governance Kind is introduced. | §6; RMS §10.1 |
| **C-065-13** | No universal lifecycle, canonicality, status vocabulary, state model, semantic schema, Relationship Record or History Record is introduced. | §12; RMS §4 |
| **C-065-14** | No approval field, deprecation field, role schema, access list, quorum, committee, governance Record or lifecycle enum is defined. | §8 (PR-5); §9 (AP-8); §12 |
| **C-065-15** | The missing Deliverable I, the unavailable RR-34 text and the 064/065 and 065/108 relational inconsistencies are recorded, not filled or rewritten. | §16 |
| **C-065-16** | 108–110, 111, 112, 145–147, 152 and 459 keep their Roadmap responsibilities. | §3; §18 |
| **C-065-17** | This artifact's changes are confined to `docs/models/registry/governance.md`. | row 065 |

## 18. Downstream Handoff

| Artifact | May assume from 065 | Must still define |
|---|---|---|
| **108** evolution (`S: 065` — soft context, not a hard dependency) | who may propose a definition change and who approves or rejects it; who may propose and who authorizes deprecation; proposal, approval and the write mechanism are distinct; Registry semantic authority is Registry-domain authority | the evolution model and its temporal account, per row 108 |
| **109** versioning | that no version is created by a proposal, only by an approved, governed write | versioning rules: *"consumers pin a version"* |
| **110** supersession + deprecation | that deprecation is authorized only by the Authority at the Human Gate | what deprecation and supersession mean and do: *"deprecated ≠ deleted"* |
| **111** dependency rules | that no approval relaxes the dependency direction | concrete definition-dependency rules |
| **112, 116** validation | that a check constrains approval and never grants it | the reference validator and the validation suite |
| **145–147, 152** | that Registry governance uses the one path and one Authority | the Registry canonical gate, the proposal model, the basis requirement, the Mutation Coordinator |
| **459** extensibility | that ordinary Registry governance adds no Kind | how a new Kind, field or definition is added |

No predesigned version, lifecycle or deprecation model is handed to 108.

## 19. Roadmap Completion Trace

| Row 065 | Status | Where it is met |
|---|---|---|
| `Val`: *"who may propose, approve, deprecate a definition"* | **SATISFIED** — propose: PR-1 to PR-6; approve: AP-1 to AP-9; deprecate: DP-1 to DP-5; one decision-rights matrix | §8–§10, §13 |
| `Done`: *"model"* | **SATISFIED** — the core rule, the three rule sets, the architecture/content boundary, inherited constraints and the matrix together answer every decision right | §7–§13; C-065-01 to C-065-17 |
| `Why`: *"definitions are canon about meaning"* | **SATISFIED** — Registry canonicality about meaning is the reason changes are governed, and stays about meaning | §1, §6 |
| `H: 064` | **SATISFIED** — the fourteen-Kind taxonomy is consumed unchanged; no Kind is added or governed into being | §6; §11; SC-065-C |
| `→ 108` | **SATISFIED** — the governance decisions are handed off; no evolution, version or deprecation mechanics are built | §18; SC-065-F |

No schema created. No Registry data created. No role, field or Record created. No gate or
mutation mechanism implemented. No version, supersession or deprecation mechanics defined.

---

*Artifact 065 · P3/3a · Own: R · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This document
states who may propose, approve and deprecate a Registry definition, from Master Blueprint §9.4,
§10, §12.6, §13.6e, §13.7c and §26.8, Record Model System §10, §17 and §21, and Roadmap row 065,
with Artifact 064's taxonomy as its input. It is not a Registry Record, holds no canonical data,
defines no schema, field, role, validator or algorithm, and implements nothing. Where it differs
from the Master Blueprint, the Record Model System, or the OS File Build Roadmap, those governing
sources are correct and this document is wrong.*
