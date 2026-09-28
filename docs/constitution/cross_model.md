# COOLBOY12 — Cross-Model Dependency Rules

**Artifact 058** · cross-model dependency rules · `docs/constitution/cross_model.md` · Own: CONST ·
RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P2/2d · Req: RR-35 · BP: §13.6a · RMS: §§22,23 · H: 045,051 · S: — · LS: — · G: — ·
→ PART IX · Val: allowed/forbidden edges; publication firewall; manifestation-blindness ·
Done: matrix normative · Why: the dependency law · Risk: CRITICAL · ∥: no

## 1. Purpose

This contract answers one question: **which references between Records of different Record Models
do the governing sources allow, which do they forbid, and which do they leave unstated?**

Row 058 calls it *"the dependency law"* and asks for *"allowed/forbidden edges; publication
firewall; manifestation-blindness"*. The RMS places the rules at §22–23: *"Cross-Model Dependency
& Reference Rules — Appendix G / Deliverable J."* Appendix G reads only *"Dependency Matrix →
Deliverable J."*

**Deliverable J.** It is named only in the RMS, at §22–23 and Appendix G. Neither the Blueprint nor
the Roadmap names it, and the Roadmap assigns it to no artifact. Row 058 cites RMS §§22,23 and sets
`Done` to *"matrix normative"*; it does not say that 058 is Deliverable J. Deliverable J is not in
this repository. **The sources therefore do not establish that 058 is Deliverable J, and do not
establish that it is not.** This contract states the edges the Blueprint, the RMS and the Roadmap
state; it does not reconstruct Deliverable J.

**Acceptance target and current status.**

- **Acceptance target** (Roadmap row 058 `Done`, preserved unchanged): *"matrix normative"*.
- **Current status: NOT COMPLETE.** The rows of §8.1 bind, through §16; the matrix is not complete
  (§8.4), and this contract does not claim the target met.

**This contract adds no architecture.** Every normative rule in it is either (a) directly
established by an authoritative source, or (b) an explicitly identified **synthesis** whose
component source statements jointly establish it — one rule, E → P[READER-MODEL] (§8.1). The
sources are Blueprint §11, §13.1, §13.6, §13.6a, §13.6b, §13.6c and Spine law 5; RMS §4, §6.1,
§7, §8.1, §8.2, §9.1, §10.3, §11.2, §12.2 and §24; Roadmap §0.2, §2.4 and row 058; and I-16, I-17,
I-89, I-102, I-104 and I-107.

## 2. Status and Authority

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the cross-model edges the governing sources state**
(row 058: `Auth: governing`). It is not World Canon, not a Record, not a schema and not a resolver.
It owns no Record Model's semantics, and it does not own legality, which RMS §4 gives to the models
and the Registry (§5).

It derives the contract from the Master Blueprint, the Record Model System and the OS File Build
Roadmap; it does not amend, supersede, or outrank any of them, and mints or amends no invariant.
Where this document differs from the Master Blueprint, the Record Model System, or the OS File
Build Roadmap, **those governing sources are correct and this document is wrong.**

**Precedence among the sources.** Roadmap §0.2: *"Blueprint + RMS govern. Where the prior roadmap
or the old roadmap conflicts with them, they lose."* It adds that *"Two unresolved source conflicts
are recorded, not silently decided"*. §0.2 states the consequence of a conflict expressly for the
prior and old roadmaps; it does not state in terms what follows when this Roadmap conflicts with
the Blueprint or RMS. No source ranks the Blueprint and the RMS against each other. This contract
therefore records a conflict among the sources and decides it only where a source states the
outcome.

`Req: RR-35` is preserved exactly as the Roadmap states it. This contract does not reproduce,
reconstruct or infer the requirement text, and creates no new requirement under it.

Hard dependencies: **045** (partition ownership — I-16, *"Cross-partition conversion is
prohibited."*) and **051** (authority framework — RMS §17, *"All authority is domain-scoped."*).

## 3. Scope

**In scope.** References whose source Record and target Record belong to different Record Models,
among the six: W · E · P · R · V · I (RMS §2). The cross-model handle; the split between resolution
and legality; every edge the sources state; the publication firewall and manifestation-blindness as
they bear on edges; the Registry's reference boundary, including its references to Registry
definitions and to declarations (§11), which RMS §10.3 states with the cross-model rule and which
are not edges between Record Models.

**Out of scope.** References within one Record Model — each model owns its relationship mechanism
(RMS §15: *"Model relationships are not identical and are never made so."*). Package composition
(056); Kind admission (057); temporal obligation and mechanism (054); the World Relationship Record
(055); the canonical write path (the Mutation Coordinator, Roadmap P5); resolvers, schemas, fields,
storage, APIs and code.

**Homonym.** Blueprint §15.18–§15.19 and I-93 use *"cross-model"* for **simulation** models
(Section 15). They are not Record Models and are not governed here. Nor is the Canon dependency
graph along which a confirmed change propagates (Spine law 8; I-67): that is propagation, not the
legality of a reference between Record Models.

```
051 authority · 045 partition
          ↓
058  cross-model edges      ← this contract
          ↓
PART IX anti-orderings · downstream validation (134)
```

## 4. Definitions

| Term | Meaning | Source |
|---|---|---|
| **Cross-model reference** | a reference from a Record of one Record Model to a Record, or a declared definition, of another | RMS §4, §8.2, §10.3 |
| **Edge `A → B`** | A references B, as the RMS writes *"E → W (reference; …)"*; the arrow runs from the referencing model to the referenced one. As the sources use it, an edge concerns references from A's Records to B's Records (see below) | RMS §8.2; Blueprint §13.6a rule 3; Roadmap §2.4 |
| **Legal cross-model handle** | a resolvable ID | RMS §4 |
| **Resolution** | mechanical; uniform across models | RMS §4 |
| **Legality** | whether an edge is permitted; *"model/Registry-owned"* | RMS §4 |
| **Domain instance** | RMS §10.3's term, set against *"Registry definitions"*; the RMS defines it no further, and this contract uses it only as §10.3 does | RMS §10.3 |

**Reference and dependency.** The sources use both words — RMS §8.2 calls E → I a *"reference"*
and *"the only sanctioned Issue dependency"*; RMS §9.2 lists *"references, dependencies, workflow
transitions."*; RMS §10.3 separates *"depend on runtime instances"* from reference. **SOURCE GAP:**
no available source defines the difference. This contract uses each word only where its source does.

**Edges and Record references.** The sources state edges as rules about Records' references: RMS
§8.2 writes *"E → W (reference; …)"*; Roadmap §2.4 gives `W → E/P/V/I` the ground
*"(manifestation-blindness)"*, which RMS §7 states of a World field and Blueprint §13.6a rule 3 of
a World record; and §2.4's `E → I` *"(reveal ordering)"* is RMS §8.2's reference. A Record-level
statement is therefore not itself a matrix row, but it can govern the same references as an edge.

## 5. Dependency Authority

RMS §4: *"Reference resolution | Cross-model references must resolve uniformly | Resolution is
mechanical; legality is model/Registry-owned"*.

- **Resolution** is a universal mechanism (RMS §3–§4). It is not decided here.
- **Legality** is model/Registry-owned (RMS §4). The edges the sources fix are stated in model
  sections — W at RMS §7, E at §8.2, R at §10.3, V at §11.2, I at §12.2 — in the Blueprint's
  partition sections (§11, §13.6a, §13.6b, §13.6c) and Spine law 5, and in the Roadmap's forbidden
  edges (§2.4). This contract **collects** them at the constitutional level and adds none. It does
  not take legality from the models or the Registry, and decides no edge the sources leave to them.
- **Two levels, kept apart.** *Stating the edges the sources fix* is this contract's, as a
  governing CONST contract (row 058). *Owning legality, and the semantics of each model's Records*,
  is the models' and the Registry's (RMS §4, §6.1). This contract owns no model semantics, no
  Registry semantics, no Kind admission (057), no package composition (056), no temporal semantics
  (054) and no Relationship Record semantics (055).
- **Authority** over what a Record means stays with the model that owns it (RMS §6.1: a Record is
  *"owned by exactly one Record Model"*; RMS §17). An edge moves none of it.

## 6. The Cross-Model Handle

RMS §4: *"Record addressing | A resolvable ID is the only legal cross-model handle | Per-model
addressing needs N² resolvers"*. The identity grammar is AD-1's (`[PARTITION]-[KIND]-[OBJECT_ID]-
[SLUG]`, RMS §5; Artifact 034).

```
cross-model reference
   ├── handle      — a resolvable ID (RMS §4); resolution is mechanical and uniform
   └── legality    — whether the edge is permitted: §7–§9 and §11 below
```

**Resolving is not permission.** An ID that resolves makes no edge legal, and an edge's legality
creates no handle. This contract adds no handle, address, path, pointer or resolver.

## 7. Dependency Legality

**The source model.** The sources define no general rule for edges they do not state: neither a
closed-world rule, in which only listed edges are legal, nor an open-world one, in which unlisted
edges are legal. What they state is:

1. **Delegation** — legality is *"model/Registry-owned"* (RMS §4).
2. **Explicit permissions** — edges the sources state as allowed, with their conditions (§8.1);
   one of them, E → P[READER-MODEL], is an identified synthesis of two source statements.
3. **Explicit prohibitions** — edges the sources forbid (§8.1), including the Roadmap's list,
   headed *"Forbidden edges"* (§2.4).
4. **Issue** — **RMS §8.2 establishes E → I**, for reveal ordering, and calls it *"the only
   sanctioned Issue dependency"*. **Roadmap §2.4 separately prohibits** `any → I` except `E → I`:
   the prohibition on W → I, P → I and V → I is the Roadmap's (for W, Blueprint §13.6a rule 3 also
   states it). The RMS wording is consistent with the Roadmap's prohibition and is not relied on
   as its source. The Registry is governed by RMS §10.3 (§11 below).

**An edge omitted from this contract** is not thereby granted or forbidden by this contract. Its
treatment follows whatever the governing sources actually establish; where those sources expressly
delegate legality to the model or the Registry (RMS §4), that delegation applies. This contract
adopts neither *unlisted = forbidden* nor *unlisted = allowed*. Whether Deliverable J would close
the matrix is not known.

Where sources conflict, the conflict is recorded with its sources; it is decided only where a
source states the outcome (§2).

## 8. Dependency Matrix

### 8.1 Edges stated by the sources

**Scope of the matrix.** Rows are Record Model → Record Model edges only. Registry references —
to Registry definitions, to declarations, and to domain instances — are the Registry reference
boundary (§11) and are not rows here. Record-level statements are §8.2's.

| Source Model | Target Model | Target Scope | Status | Constraint | Source |
|---|---|---|---|---|---|
| **E** | **W** | W Records | ALLOWED | reference; *"mutation only via the governed path"* | RMS §8.2; Blueprint §13.6b (E's *"interface to World is by reference"*) |
| **E** | **I** | I Records | CONDITIONAL | *"reference for reveal ordering — the only sanctioned Issue dependency"* | RMS §8.2; Blueprint §13.6a rule 3 (*"Epistemic records may reference issues"*) |
| **E** | **P** | P Records of Kind READER-MODEL only — `P[READER-MODEL]` | CONDITIONAL — **synthesis** | the target P Record MUST be of Kind READER-MODEL; **no general E → P permission is established** | Blueprint §11, §13.6; RMS §9.1 |
| **I** | **W** | W Records | ALLOWED | *"Issue records may reference World, Epistemic, and Production records."*; never ownership: *"Issue references; it never owns."* | Blueprint §13.6a rules 2–3 |
| **I** | **E** | E Records | ALLOWED | as for I → W: reference, never ownership | Blueprint §13.6a rules 2–3 |
| **I** | **P** | P Records | ALLOWED | as for I → W: reference, never ownership | Blueprint §13.6a rules 2–3 |
| **W** | **I** | I Records | FORBIDDEN | absolute: *"No World record may reference an issue — that is manifestation-blindness, and it is absolute (Section 11)."* | Blueprint §13.6a rule 3, §11; I-17; RMS §7; Roadmap §2.4 |
| **P** | **I** | I Records | FORBIDDEN | Roadmap §2.4 lists `any → I` except `E → I` among its forbidden edges; RMS §8.2's *"the only sanctioned Issue dependency"* is consistent with it | Roadmap §2.4 |
| **V** | **I** | I Records | FORBIDDEN | as for P → I | Roadmap §2.4 |
| **W** | **E** | E Records | FORBIDDEN | Roadmap §2.4 lists `W → E/P/V/I` (manifestation-blindness) among its forbidden edges. The prohibition is the Roadmap's: the Blueprint and RMS state no W → E rule, and their manifestation-blindness texts name an issue, tier, medium, artifact or the real world, not E | Roadmap §2.4 |
| **W** | **P** | P Records | FORBIDDEN | as for W → E; the Blueprint and RMS state no W → P rule | Roadmap §2.4 |
| **W** | **V** | V Records | UNRESOLVED SOURCE CONFLICT | Blueprint §13.6c and §13.1 permit every Record, World included, to reference into the V partition; Roadmap §2.4 forbids `W → V`; Roadmap §0.2 does not decide it; 058 has no authority to (§8.3) | Blueprint §13.1, §13.6c; I-16; Roadmap §2.4, §0.2 |
| **V** | **W** | W Records — **reference** | NOT ESTABLISHED | no available source states whether a V Record may reference a W Record | — |
| **V** | **W** | W Records — **mutation** | FORBIDDEN | *"Visual never mutates World."* A mutation prohibition; it says nothing of reference | RMS §11.2; I-89 |

**E → P[READER-MODEL], derived.** Blueprint §11 states that Epistemic records *"may reference
reader models"*, and §11 also states *"The reader model is a `READER-MODEL` in Production"*; §13.6
and RMS §9.1 list READER-MODEL among the P Kinds. Neither statement alone is the edge; together
they state it, for READER-MODEL only. **No general E → P permission is established**, and no
source states any other E → P reference.

**Issue and Visual semantics.** RMS §12.2: *"Issue references but never owns W/E/P/V semantics."*
For V, the RMS states this at the level of semantics. The Blueprint's Record-level statement
(§8.2) lets every Record, an I Record included, reference into the V partition. Neither is stated
as an I → V edge, and this contract does not expand either into one: **no I → V Record Model edge
is established**, and the matrix has no I → V row.

Every allowed edge carries the handle rule (§6) and confers no ownership (§12).

### 8.2 Record-level references — not model edges

Two source statements concern what a **Record** may carry, not an edge between Record Models. This
contract records them at that level and derives no matrix row from either.

- **`registry_ref`.** Every Record carries it (RMS §4, the universal envelope); Artifact 033: it
  *"Carries the Record's reference into the Registry"*. The field's meaning and resolution are 033's
  and the Registry's. **The existence of `registry_ref` on a Record does not by itself create a
  cross-Record-Model edge in this matrix.**
- **Visual references.** Blueprint §13.6c: *"Every Record may reference visual objects."* The
  Blueprint carries them in `visual_refs` (§13.1, §13.6c), which §13.1 describes as *"References
  into the V partition"*; RMS §4 fixes the universal envelope at the bootstrap set *"and no more"*;
  and the Blueprint records which kinds must carry `visual_refs` as *"REQUIRES DECISION"*. The
  statement stands at the Record level: every Record may reference visual objects. Where the
  reference is carried is not decided here. This contract does not expand the statement into
  per-model rows — no E → V, P → V or I → V row is added. Where a model-level statement governs
  the same references, the two meet: Roadmap §2.4 forbids W → V (§8.3).

### 8.3 W → V — source conflict

| | Statement | Level |
|---|---|---|
| **Source A** — Blueprint §13.6c, §13.1 | *"Every Record may reference visual objects."*; `visual_refs` are *"References into the V partition"*; *"Every Record has a defined relationship to the Visual Library, whether or not an asset exists (v0.6.3)."*; a `REQUIRED` policy means *"A canonical depiction must exist before the object may reach CANON status"* | Record: every Record, World included, referencing into the V partition |
| **Source B** — Roadmap §2.4 | lists `W → E/P/V/I` (manifestation-blindness) among its forbidden edges | Record Model: an edge from W to V |
| **Source C** — RMS §7; I-17; Blueprint §11 | *"no World field may reference an issue, tier, medium, artifact, or the real world"*; World records *"know nothing of magazines, covers, tiers, or issues"* | field of a World Record |

**Why this is a conflict, not a difference of level.** Source A is Record-level and is not a
matrix row (§8.2). It names its target: *"References into the V partition"*, and each partition
owns exactly one Record Model (I-16); so it permits a World Record to reference a V Record. Source
B is a model edge, and as the sources use edges it concerns the references of W's Records (§4:
§2.4 grounds `W → E/P/V/I` in manifestation-blindness, which RMS §7 states of a World field). So
Source B forbids the reference Source A permits. The bridge between the two levels is the sources'
own, and the two sources disagree about the same reference. Source C forbids a World field
referencing an *"artifact"* and names *"covers"*; RMS §9.1 speaks of *"Visual artifact/asset →
V."*, and no source says whether a visual object is an artifact, or a cover, in Source C's sense.

**Authority treatment.** Roadmap §0.2 states that *"Blueprint + RMS govern"*, and states the
consequence of a conflict expressly for the prior and old roadmaps (§2); it does not state in terms
the outcome of a conflict between this Roadmap's §2.4 and the Blueprint. A and C are both governing
and no source ranks them. This contract adopts neither the Roadmap's W → V prohibition nor the
Blueprint's permission for World Records. Whether a World Record may reference a visual object —
and whether that differs between a `CANONICAL-VISUAL-SPECIFICATION` and a `VISUAL-ASSET` — is
**unresolved by the current sources**. No source assigns its resolution to 058, and **Artifact 058
has no authority to resolve it**: this contract describes the sources' cross-model consequences; it
does not choose between conflicting source statements.

**058 treatment.** The W → V row reads UNRESOLVED SOURCE CONFLICT; no condition binds it.
C-058-03 binds Source C's words and does not decide whether any visual object is an *"artifact"*.

### 8.4 SOURCE GAP — Deliverable J and the edges not stated

RMS §22–23 and Appendix G delegate the dependency matrix to Deliverable J, which is not in this
repository. RMS §10.3 confirms such a matrix exists: its rule *"appears in the Registry section,
the dependency matrix, the governance matrix, the examples, and the implementation notes."*

No available source states these as Record Model edges. This contract neither grants nor forbids
them as edges; RMS §4's delegation of legality to the model or the Registry applies as the RMS
states it:

| Record Model edges not stated |
|---|
| E → R · E → P other than P[READER-MODEL] |
| P → W · P → E · P → R |
| V → W (reference) · V → E · V → P · V → R |
| W → R · I → R |
| E → V · P → V · I → V — as model edges; the Record-level statement of §8.2 applies at its own level |

For V → E, RMS §11.2 states a chain — a visual analysis whose claim concerns World Truth becomes E
evidence — and states no edge direction. For every → R edge, see `registry_ref` (§8.2).

Row 058's `Done`, *"matrix normative"*, is not met by this contract; §8.1 is the part the sources
support.

## 9. Directional Rules

- **Direction is frozen.** Blueprint §13.6b: *"What is frozen for both: the boundary, the direction
  of reference, and the rule that neither may become canon by any route."*
- **Issue.** Blueprint §13.6a rule 3: *"Reference runs one way."* I references W, E and P; no
  World record references I; E references I *"because who-was-told-what-and-when is exactly what
  they are about."*
- **World.** Manifestation-blindness (§8.1, W rows). Blueprint §11: World records *"know nothing of
  magazines, covers, tiers, or issues, and no field on them may mention one."*
- **Allowed in one direction is not allowed in the other.** E → I does not make I → E follow from
  it; each is stated separately (§8.1).

**Not stated by any source:** a rule on dependency cycles, on transitive or indirect dependency,
or on dependency chains between Record Models. This contract adds none (§15).

## 10. Reference vs Mutation

The sources separate referencing a Record from changing it:

- **E → W.** Reference; *"mutation only via the governed path"* (RMS §8.2). The RMS does not define
  *"the governed path"* at §8.2 and this contract does not define it. Canon changes only through
  Spine law 2's path, and RMS §4 names the Mutation Coordinator *"Spine 2 — sole canonical write
  path"*.
- **V → W.** *"Visual never mutates World."* (RMS §11.2). I-89: *"Vision produces observations and
  proposals, never canonicalization."* This is a mutation prohibition only; whether a V Record may
  reference a W Record is not established (§8.1), and neither follows from the other.
- **R → domain instances.** Registry *"MAY NOT"* mutate domain instances (RMS §10.3).
- **Issue.** Issue *"references but never owns"* (RMS §12.2); publication writes nothing to canon
  (§12 below).

A permitted reference therefore grants no mutation.

## 11. Registry Boundary

RMS §10.3 (`FROZEN`, correcting v0.1's *"may never reference a kind"*):

- **Registry MAY reference:** *"other Registry definitions · declared Record Models · declared Kinds
  · declared schemas · declared semantic contracts."*
- **Registry MAY NOT:** *"own domain instances · depend on runtime instances · mutate domain
  instances · use domain instances as semantic authority."*
- *"R → R definitions = ALLOWED. R → domain instances = FORBIDDEN."*

**Three categories, kept apart.**

- **Registry declaration references** — to declared Record Models, Kinds, schemas and semantic
  contracts: allowed (RMS §10.3). RMS §10.3 does not state them as edges from R to the Records of
  another model, and this contract does not place them in the matrix (§8.1).
- **Registry-internal references** — R → R definitions: *"ALLOWED"* (RMS §10.3). Within R; not a
  cross-model edge.
- **Registry → domain instances** — *"FORBIDDEN"* (RMS §10.3); Roadmap §2.4 also lists
  `R → domain instance` among its forbidden edges. The Registry may not reference, own or mutate a
  domain instance, depend on a runtime instance, or use a domain instance as semantic authority.
  This is the Registry reference boundary; it is stated here and not repeated as a matrix row.

The prohibition is on **domain instances**, not on the domain models: the Registry may reference
declared Record Models and Kinds. Nor does referencing a declaration give the Registry any domain
instance. RMS §24: *"Registry is canon about meaning only; it can never override World Truth"*;
*"R defines the terms; E owns the states"*.

Every Record carries `registry_ref` (§8.2). The existence of `registry_ref` on a Record does not
by itself create a cross-Record-Model edge in this matrix, and the field makes the Registry no owner
of the Record that carries it.

## 12. Model Sovereignty and the Publication Firewall

**An edge transfers nothing.** Every Record is *"owned by exactly one Record Model"* (RMS §6.1), and
*"Cross-partition conversion is prohibited."* (I-16). The sources state it edge by edge:

- **Issue.** Blueprint §13.6a rule 2: *"That never makes an issue the owner of the event."*
  *"Ownership is a World-partition property, and a reference from a lower partition confers
  nothing."*
- **Epistemic.** RMS §8.1: *"A mystery references the relevant World truth but never contains or
  owns it."* RMS §24: *"W holds the fact; E holds frames upon it"*.
- **Visual.** I-89: *"The Visual Library is never independently a truth authority."* Blueprint
  §13.6c: *"V holds the objects. It does not hold the authority."*

**Publication firewall.** Spine law 5: *"Published artifacts are in-world manifestations. They
reference canon one-directionally; they never become canon."* Blueprint §13.6a rule 1: *"Nothing in
an issue is true because it is printed."* RMS §12.2: *"Issue never becomes World Canon."* An I → W
reference makes nothing canon; I-104 keeps Record and Canon apart.

## 13. Boundaries with Adjacent Artifacts

| Artifact | Boundary |
|---|---|
| **045** partition ownership | hard dependency; a reference converts no Record between partitions (I-16) |
| **051** authority framework | hard dependency; authority stays domain-scoped (RMS §17); an edge confers none |
| **054** temporal obligation | E → I serves reveal ordering, and *"reader-facing revelation is ordered by issue ordinal"* (RMS §8.2). The ordering is E's temporal mechanism under 054; this contract defines none of it |
| **055** relationship boundary | a cross-model reference is not a World Relationship Record, and no model is required to carry one (I-102) |
| **056** package boundary | an edge places nothing in any model's package; composition stays model-owned (I-107) |
| **057** Kind admission | an edge admits no Kind; 057's question 7, *what references it*, stays part of admission |
| **Mutation Coordinator** (Roadmap P5) | the canonical write path; referenced in §10, not defined |
| **134** validator | downstream consumer of §8.1; not a source for this contract |

## 14. Prohibited Dependency Patterns

Only prohibitions the sources state:

| # | Prohibited | Source |
|---|---|---|
| 1 | A cross-model handle other than a resolvable ID | RMS §4 |
| 2 | Treating an ID's resolution as the edge's legality | RMS §4 |
| 3 | A World record referencing an issue; a World field referencing an issue, tier, medium, artifact, or the real world | Blueprint §13.6a rule 3, §11; I-17; RMS §7 |
| 4 | A W → I, P → I or V → I edge; an E → I edge other than for reveal ordering | Roadmap §2.4; RMS §8.2; Blueprint §13.6a rule 3 |
| 5 | W → E or W → P | Roadmap §2.4 |
| 6 | E mutating W other than via the governed path | RMS §8.2 |
| 7 | Visual mutating World | RMS §11.2 |
| 8 | Registry referencing, owning or mutating a domain instance, depending on a runtime instance, or using a domain instance as semantic authority | RMS §10.3 |
| 9 | A reference conferring ownership of the referenced Record | RMS §6.1; I-16; Blueprint §13.6a rule 2 |
| 10 | A published artifact becoming canon through its references | Spine law 5; RMS §12.2 |

## 15. What This Contract Does Not Define

1. The edges Deliverable J holds (§8.4) — no available source states them.
2. W → V (§8.3) — the governing sources conflict.
3. The difference between *reference* and *dependency* (§4) — undefined in the sources.
4. RMS §8.2's *"the governed path"* (§10) — the RMS names it at §8.2 without defining it.
5. A cycle rule, a transitive rule, or a dependency-chain rule (§9) — stated by no source.
6. Reveal ordering — E's, under 054.
7. Package composition (056) and Kind admission (057) — owned there.
8. The World Relationship Record (055) — World-only.
9. The meaning of `registry_ref` or `visual_refs`, and where a visual reference is carried (§8.2).
10. Resolution, resolvers, schemas, fields, storage, APIs, serialization and code — resolution is a
    universal mechanism (RMS §3–§4); the rest is implementation.
11. Any new constitutional invariant — an authoring constraint on this document (§2), not a
    conformance condition.

## 16. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number. They bind the allowed, conditional and forbidden rows of §8.1, the Registry
reference boundary of §11, and the general rules of §6 and §12. None binds the unresolved W → V
row, a Record-level statement of §8.2, the Issue–V semantic statement, or an edge in §8.4.

| ID | Condition | Source |
|---|---|---|
| **C-058-01** | Every cross-model reference uses a resolvable ID as its handle. | RMS §4 |
| **C-058-02** | An edge is not treated as legal because its target resolves. | RMS §4 |
| **C-058-03** | No World record references an issue, and no World field references an issue, tier, medium, artifact, or the real world. | Blueprint §13.6a rule 3, §11; I-17; RMS §7 |
| **C-058-04** | There is no W → I, P → I or V → I edge (Roadmap §2.4; for W also Blueprint §13.6a rule 3, I-17, RMS §7). An E → I edge serves reveal ordering only (RMS §8.2, which sanctions E → I; it is not the source of the prohibition on the others). | Roadmap §2.4; RMS §8.2; Blueprint §13.6a rule 3; I-17; RMS §7 |
| **C-058-05** | No World record references an E or P Record. | Roadmap §2.4 |
| **C-058-06** | An E → W edge is a reference; any mutation of W arising from E happens only via the governed path. | RMS §8.2 |
| **C-058-07** | V never mutates W. The condition binds mutation only; whether a V Record may reference a W Record is not established and no condition binds it. | RMS §11.2; I-89 |
| **C-058-08** | No Registry Record references, owns or mutates a domain instance, depends on a runtime instance, or uses a domain instance as semantic authority. | RMS §10.3 |
| **C-058-09** | A cross-model reference changes no Record's owning Record Model or partition. | RMS §6.1; I-16; Blueprint §13.6a rule 2; RMS §12.2 |
| **C-058-10** | No Issue reference makes anything canon. | Spine law 5; Blueprint §13.6a rule 1; RMS §12.2; I-04 |
| **C-058-11** | A cross-model reference is not required to be, and is not treated as, a World Relationship Record. | I-102; Artifact 055 |
| **C-058-12** | A cross-model edge decides no package composition. | I-107; RMS §6; Artifact 056 |
| **C-058-13** | A cross-model edge is not Kind admission and admits no Kind. | RMS §6.1, §13; Artifact 057 |

A construction satisfying all thirteen is conformant **to this contract**. That is not conformance
to a complete dependency matrix, which the available sources do not supply (§8.4).

## 17. Worked Examples

> **Illustrative and non-normative.** Each rests on a verified rule in §8.1 or §11; none decides
> an edge.

**Example A — E → W.** An E `MYSTERY` references the World truth it concerns. RMS §8.1: it *"never
contains or owns it."* The reference uses a resolvable ID (§6). Any change to that World truth goes
via the governed path (RMS §8.2); the reference makes none.

**Example B — E → I.** An E Record references an `ISSUE` for reveal ordering; RMS §8.2:
*"reader-facing revelation is ordered by issue ordinal"*. A P `SCHEDULE` referencing an `ISSUE` is
a P → I edge, which Roadmap §2.4 forbids (§8.1).

**Example C — Registry.** A `KIND-DEFINITION` may reference the declared Kind `CHARACTER` — a
Registry declaration reference (RMS §10.3; §11). It may not reference a particular `W-CH-…`
Record, a domain instance, or take its meaning from one.

**Example D — I → W.** An `ARTICLE` references a World `EVENT`. Blueprint §13.6a: *"That never
makes an issue the owner of the event."* Whatever the article asserts, *"Nothing in an issue is true
because it is printed."* (Spine law 5; Blueprint §13.6a rule 1).

**Example E — resolvable, not legal.** A World `CHARACTER` Record carrying the ID of an `ISSUE`
Record: the ID is well-formed and resolves (RMS §4), and the reference is still forbidden
(Blueprint §13.6a rule 3; C-058-03). Resolution identified the target; it did not permit the edge.

**Example F — no package, no Kind.** An `ARTICLE`'s reference to a World `EVENT` (I → W, §8.1)
places the `EVENT` in no Issue package (056; C-058-12) and admits no Kind (057; C-058-13).

## 18. Source Traceability

| Rule | Source |
|---|---|
| Resolvable ID the only legal cross-model handle | RMS §4 |
| Resolution mechanical and uniform; legality model/Registry-owned | RMS §4 |
| Precedence: Blueprint + RMS govern; conflict consequence stated for the prior and old roadmaps | Roadmap §0.2 |
| Edges concern Records' references (the sources' own bridge) | RMS §8.2, §7; Roadmap §2.4; Blueprint §13.6a rule 3 |
| Matrix delegated to Deliverable J; Deliverable J named only in the RMS | RMS §22–23, Appendix G, §10.3 |
| E → W, E → I | RMS §8.2; Blueprint §13.6a rule 3, §13.6b |
| E → P[READER-MODEL] — **synthesis** of Blueprint §11 (*may reference reader models*) and Blueprint §11, §13.6 (READER-MODEL is Production); no general E → P | Blueprint §11, §13.6; RMS §9.1 |
| I → W; I → E; I → P (three rows) | Blueprint §13.6a rules 2–3 |
| V → W: reference not established; mutation forbidden | RMS §11.2; I-89 |
| Issue references V semantics; no I → V edge established | RMS §12.2 |
| E → I the only sanctioned Issue dependency (RMS); W/P/V → I forbidden (Roadmap) | RMS §8.2; Roadmap §2.4; Blueprint §13.6a rule 3 |
| W → E, W → P forbidden | Roadmap §2.4 |
| Visual never mutates World | RMS §11.2; I-89 |
| Registry declaration references; R → domain instances forbidden | RMS §10.3, §24 |
| Record-level `registry_ref`; Record-level visual references | RMS §4; Artifact 033; Blueprint §13.1, §13.6c |
| W → V unresolved: Blueprint Record-level permission into the V partition vs Roadmap W → V prohibition | Blueprint §13.1, §13.6c; Roadmap §2.4, §0.2; RMS §7, §9.1; I-17 |
| Manifestation-blindness | Blueprint §11, §13.6a rule 3; I-17; RMS §7 |
| Direction of reference frozen | Blueprint §13.6a rule 3, §13.6b |
| Publication firewall | Spine law 5; Blueprint §13.6a rule 1; RMS §12.2; I-04, I-104 |
| One owning model; no conversion | RMS §6.1; I-16 |
| Relationship mechanisms model-owned; RR World-only | RMS §15; I-102 |
| Packaging model-owned | I-107; RMS §6 |
| Kind admission separate | RMS §6.1, §13; Artifact 057 |
| Identity and acceptance target | Roadmap row 058 |

## 19. Final Contract Statement

A cross-model reference uses a resolvable ID; that it resolves does not make it legal, and legality
is model/Registry-owned. The sources state these edges: E references W, mutating it only via the
governed path; E references I for reveal ordering — the only sanctioned Issue dependency — and,
by synthesis of two Blueprint statements, P Records of Kind READER-MODEL — no general E → P; I
references W, E and P Records and owns none of them, and references V semantics without any
I → V Record edge being established; no World record references an issue; the Roadmap forbids
W → E, W → P, P → I and V → I; V never mutates W. The Registry references definitions and
declarations, never domain instances (§11). Nothing becomes canon by being published, and no
reference changes who owns a Record. W → V is in conflict between the governing sources, and the
edges Deliverable J would hold are not stated; this contract decides neither. Row 058's acceptance
target is *"matrix normative"*; its current status is NOT COMPLETE.

---

*Artifact 058 · P2/2d · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the cross-model edges the Blueprint, the RMS and the Roadmap establish. It does not
amend them, defines no resolver, schema or matrix cell they leave undefined, and grants or forbids
no edge they do not state. Where it differs from the Master Blueprint, the Record Model System, or
the OS File Build Roadmap, those governing sources are correct and this document is wrong.*
