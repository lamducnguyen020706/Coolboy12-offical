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
Deliverable J."* **Deliverable J is not in this repository** (§8.3 below). This contract therefore
states every cross-model edge the Blueprint, the RMS and the Roadmap state, records the conflicts
among them, and marks every other edge as not established. It completes no edge from inference.

**This contract adds no architecture.** Every rule restates Blueprint §11, §13.6a, §13.6b, §13.6c
and Spine law 5; RMS §4, §6.1, §7, §8.1, §8.2, §10.3, §11.2, §12.2 and §24; Roadmap §2.4 and rows
058 and 465; and I-16, I-17, I-89, I-102, I-104 and I-107.

## 2. Status and Authority

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the cross-model edges the governing sources state**. It is
not World Canon, not a Record, not a schema and not a resolver. It owns no Record Model's semantics.

It derives the contract from the Master Blueprint, the Record Model System and the OS File Build
Roadmap; it does not amend, supersede, or outrank any of them, and mints or amends no invariant.
Where this document differs from the Master Blueprint, the Record Model System, or the OS File
Build Roadmap, **those governing sources are correct and this document is wrong.**

`Req: RR-35` is preserved exactly as the Roadmap states it. This contract does not reproduce,
reconstruct or infer the requirement text, and creates no new requirement under it.

Hard dependencies: **045** (partition ownership — I-16, *"Cross-partition conversion is
prohibited."*) and **051** (authority framework — RMS §17, *"All authority is domain-scoped."*).

## 3. Scope

**In scope.** References whose source Record and target Record belong to different Record Models,
among the six: W · E · P · R · V · I (RMS §2). The cross-model handle; the split between resolution
and legality; every edge the sources state; the publication firewall and manifestation-blindness as
they bear on edges; the Registry's reference boundary.

**Out of scope.** References within one Record Model — each model owns its relationship mechanism
(RMS §15: *"Model relationships are not identical and are never made so."*). Package composition
(056); Kind admission (057); temporal obligation and mechanism (054); the World Relationship Record
(055); the canonical write path (Artifact 152, Roadmap P5); resolvers, schemas, fields, storage,
APIs and code.

**Homonym.** Blueprint §15.18–§15.19 and I-93 use *"cross-model"* for **simulation** models
(Section 15). They are not Record Models and are not governed here. Nor is the Canon dependency
graph along which a confirmed change propagates (Spine law 8; I-67): that is propagation, not the
legality of a reference between Record Models.

```
051 authority · 045 partition
          ↓
058  cross-model edges      ← this contract
          ↓
PART IX anti-orderings · 134 validator (forbidden edges rejected) · 463/465 integration
```

## 4. Definitions

| Term | Meaning | Source |
|---|---|---|
| **Cross-model reference** | a reference from a Record of one Record Model to a Record, or a declared definition, of another | RMS §4, §8.2, §10.3 |
| **Edge `A → B`** | A references B, as the RMS writes *"E → W (reference; …)"*; the arrow runs from the referencing model to the referenced one | RMS §8.2; Blueprint §13.6a rule 3 |
| **Legal cross-model handle** | a resolvable ID | RMS §4 |
| **Resolution** | mechanical; uniform across models | RMS §4 |
| **Legality** | whether an edge is permitted; *"model/Registry-owned"* | RMS §4 |
| **Domain instance** | RMS §10.3's term, set against *"Registry definitions"*; the RMS defines it no further, and this contract uses it only as §10.3 does | RMS §10.3 |

**Reference and dependency.** The sources use both words — RMS §8.2 calls E → I a *"reference"*
and *"the only sanctioned Issue dependency"*; RMS §9.2 lists *"references, dependencies, workflow
transitions."*; RMS §10.3 separates *"depend on runtime instances"* from reference. **SOURCE GAP:**
no available source defines the difference. This contract uses each word only where its source does.

## 5. Dependency Authority

RMS §4: *"Reference resolution | Cross-model references must resolve uniformly | Resolution is
mechanical; legality is model/Registry-owned"*.

- **Resolution** is a universal mechanism (RMS §3–§4). It is not decided here.
- **Legality** is model/Registry-owned (RMS §4). This contract states the cross-model edges the
  constitutional sources fix, and records where they stop. It does not take legality from the
  models or the Registry, and fills no cell they would fill.
- **Authority** over what a Record means stays with the model that owns it (RMS §6.1: a Record is
  *"owned by exactly one Record Model"*; RMS §17). An edge moves none of it.

## 6. The Cross-Model Handle

RMS §4: *"Record addressing | A resolvable ID is the only legal cross-model handle | Per-model
addressing needs N² resolvers"*. The identity grammar is AD-1's (`[PARTITION]-[KIND]-[OBJECT_ID]-
[SLUG]`, RMS §5; Artifact 034).

```
cross-model reference
   ├── handle      — a resolvable ID (RMS §4); resolution is mechanical and uniform
   └── legality    — whether the edge is permitted: §7–§9 below; otherwise model/Registry-owned
```

**Resolving is not permission.** An ID that resolves makes no edge legal, and an edge's legality
creates no handle. This contract adds no handle, address, path, pointer or resolver.

## 7. Dependency Legality

The sources state edges in three forms, and this contract keeps them apart:

1. **Stated as allowed** — the sources state the reference and its condition.
2. **Stated as forbidden** — the sources prohibit it.
3. **Not established** — no available source states it. **Not established is not forbidden, and
   not allowed.** The one closed rule in the sources is for Issue: E → I is *"the only sanctioned
   Issue dependency"* (RMS §8.2), which leaves every other model's references to I Records
   unsanctioned; the Registry's references to declarations are governed by RMS §10.3 (§11 below).
   No source states a closed rule for any other target.

Where sources conflict, the conflict is recorded with its sources and their precedence (Blueprint
and RMS above Roadmap); it is not silently decided.

## 8. Dependency Matrix

### 8.1 Edges stated by the sources

| Edge | Status | Condition | Source |
|---|---|---|---|
| **E → W** | allowed | reference; *"mutation only via the governed path"* | RMS §8.2; Blueprint §13.6b |
| **E → I** | allowed | *"reference for reveal ordering — the only sanctioned Issue dependency"* | RMS §8.2; Blueprint §13.6a rule 3; Roadmap §2.4 |
| **E → P** | allowed, for reader models | Blueprint §11: E records *"may reference reader models"*; this contract reads *reader models* as the P Kind READER-MODEL (RMS §9.1) — an identification, not a source statement | Blueprint §11; RMS §9.1 |
| **I → W, I → E, I → P** | allowed | reference, never ownership | Blueprint §13.6a rules 2–3; RMS §12.2 |
| **I → V** | allowed | reference, never ownership: *"Issue references but never owns W/E/P/V semantics."* | RMS §12.2 |
| **E → V, P → V, I → V** | allowed | *"Every Record may reference visual objects."* | Blueprint §13.6c |
| **V → W** | allowed as reference; never as mutation | *"Visual never mutates World."* | Roadmap row 465 `Val`; RMS §11, §11.2 |
| **any → R** | allowed | every Record carries the universal `registry_ref` (RMS §4); Artifact 033: it *"Carries the Record's reference into the Registry"* | RMS §4; Artifact 033 |
| **R → R definitions** | ALLOWED | within R; listed because RMS §10.3 states it with the cross-model rule | RMS §10.3 |
| **R → declared Record Models, Kinds, schemas, semantic contracts** | allowed | *"Registry MAY reference"* them | RMS §10.3 |
| **R → domain instances** | FORBIDDEN | *"own domain instances · depend on runtime instances · mutate domain instances · use domain instances as semantic authority"* are all excluded | RMS §10.3; Roadmap §2.4 |
| **W → I** | forbidden, absolutely | *"No World record may reference an issue — that is manifestation-blindness, and it is absolute (Section 11)."* | Blueprint §13.6a rule 3, §11; I-17; RMS §7; Roadmap §2.4 |
| **P → I, V → I** | forbidden | E → I is the only sanctioned Issue dependency; Roadmap §2.4: `any → I` except `E → I` | RMS §8.2; Roadmap §2.4 |
| **W → E, W → P** | forbidden | Roadmap §2.4: `W → E/P/V/I` (manifestation-blindness) | Roadmap §2.4 |

Every allowed edge carries the handle rule (§6) and confers no ownership (§12).

### 8.2 Source conflicts — recorded, not resolved here

| Edge | One source | Other source | Precedence and effect |
|---|---|---|---|
| **W → V** | Blueprint §13.6c: *"Every Record may reference visual objects."* | Roadmap §2.4 forbids `W → E/P/V/I`; RMS §7 and I-17 forbid a World field referencing an *"artifact"* | The Blueprint outranks the Roadmap, so the Roadmap's W → V prohibition is not adopted here. Whether a World reference to a given visual object is a reference to an *"artifact"* under RMS §7 and I-17 is not settled by the sources. **W → V is unresolved.** |
| **P → I** | Roadmap row 465 `Val`: *"E→W, P→all, V→W, I→all, R→none"* | RMS §8.2 (E → I the only sanctioned Issue dependency); Roadmap §2.4 | The RMS outranks the Roadmap: P → I is not sanctioned (§8.1). Row 465 is not read as sanctioning it. |
| **R → other models** | Roadmap row 465 `Val`: *"R→none"* | RMS §10.3: R MAY reference declared Record Models, Kinds, schemas and semantic contracts | The RMS governs the Registry cells (§8.1, §11). |

Where the visual reference is carried is not decided here: Blueprint §13.1 lists `visual_refs` in
its envelope, and RMS §4 fixes the universal envelope at the bootstrap set *"and no more"*.

### 8.3 SOURCE GAP — Deliverable J and the unestablished edges

RMS §22–23 and Appendix G delegate the dependency matrix to Deliverable J, which is not in this
repository. RMS §10.3 confirms such a matrix exists: its rule *"appears in the Registry section,
the dependency matrix, the governance matrix, the examples, and the implementation notes."* Without
it, these edges are **not established** — neither allowed nor forbidden by this contract:

| Edge | What the sources say |
|---|---|
| **P → W, P → E** | Roadmap row 465 `Val` lists *"P→all"*; no Blueprint or RMS statement establishes either edge |
| **P → R** | only the universal `registry_ref` (§8.1) |
| **E → P**, other than reader models | nothing |
| **V → E** | RMS §11.2 states a chain — a visual analysis whose claim concerns World Truth becomes E evidence — and states no edge direction |
| **V → P** | nothing |

Row 058's `Done` is *"matrix normative"*. The cells in §8.1 are normative here; the matrix as a
whole is **source-blocked** until Deliverable J, or an equivalent authoritative source, is
available (§19).

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
  path"*; its mechanism is Artifact 152's (Roadmap P5). Roadmap §2.3 and §2.4 name the Mutation
  Coordinator `133`; row 133 is the temporal validator and row 152 the Mutation Coordinator. This
  contract cites row 152 and records the mismatch.
- **V → W.** *"Visual never mutates World."* (RMS §11.2). I-89: *"Vision produces observations and
  proposals, never canonicalization."*
- **R → domain instances.** Registry *"MAY NOT"* mutate domain instances (RMS §10.3).
- **I → anything.** Issue *"references but never owns"* (RMS §12.2); publication writes nothing to
  canon (§12 below).

A permitted reference therefore grants no mutation.

## 11. Registry Boundary

RMS §10.3 (`FROZEN`, correcting v0.1's *"may never reference a kind"*):

- **Registry MAY reference:** *"other Registry definitions · declared Record Models · declared Kinds
  · declared schemas · declared semantic contracts."*
- **Registry MAY NOT:** *"own domain instances · depend on runtime instances · mutate domain
  instances · use domain instances as semantic authority."*
- *"R → R definitions = ALLOWED. R → domain instances = FORBIDDEN."*

The prohibition is on **domain instances**, not on the domain models: the Registry may reference
declared Record Models and Kinds. Nor does referencing a declaration give the Registry any domain
instance. RMS §24: *"Registry is canon about meaning only; it can never override World Truth"*;
*"R defines the terms; E owns the states"*.

Every other model references the Registry through `registry_ref` (§8.1). That reference makes the
referencing Record no part of the Registry, and the Registry no owner of it.

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
| **152** Mutation Coordinator | the canonical write path; referenced in §10, not defined |
| **134** validator · **463** · **465** | downstream: 134's `Val` is *"forbidden edges rejected"* |

## 14. Prohibited Dependency Patterns

Only prohibitions the sources state:

| # | Prohibited | Source |
|---|---|---|
| 1 | A cross-model handle other than a resolvable ID | RMS §4 |
| 2 | Treating an ID's resolution as the edge's legality | RMS §4 |
| 3 | A World record referencing an issue; a World field referencing an issue, tier, medium, artifact, or the real world | Blueprint §13.6a rule 3, §11; I-17; RMS §7 |
| 4 | A W, P or V Record referencing an I Record; E referencing I other than for reveal ordering | RMS §8.2; Roadmap §2.4 |
| 5 | W → E or W → P | Roadmap §2.4 |
| 6 | E mutating W other than via the governed path | RMS §8.2 |
| 7 | Visual mutating World | RMS §11.2 |
| 8 | Registry owning, depending on, mutating, or taking semantic authority from domain instances | RMS §10.3 |
| 9 | A reference conferring ownership of the referenced Record | RMS §6.1; I-16; Blueprint §13.6a rule 2 |
| 10 | A published artifact becoming canon through its references | Spine law 5; RMS §12.2 |

## 15. What This Contract Does Not Define

1. The edges Deliverable J holds (§8.3) — no available source states them.
2. The W → V conflict (§8.2) — the sources conflict.
3. The difference between *reference* and *dependency* (§4) — undefined in the sources.
4. RMS §8.2's *"the governed path"* (§10) — the RMS names it at §8.2 without defining it.
5. A cycle rule, a transitive rule, or a dependency-chain rule (§9) — stated by no source.
6. Reveal ordering — E's, under 054.
7. Package composition (056) and Kind admission (057) — owned there.
8. The World Relationship Record (055) — World-only.
9. Resolution, resolvers, schemas, fields, storage, APIs, serialization and code — resolution is a
   universal mechanism (RMS §3–§4); the rest is implementation.
10. Where a visual reference is carried (§8.2).
11. Any new constitutional invariant.

## 16. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number. They bind only the edges §8.1 states; no condition treats an edge in §8.2 or §8.3
as allowed or forbidden.

| ID | Condition | Source |
|---|---|---|
| **C-058-01** | Every cross-model reference uses a resolvable ID as its handle. | RMS §4 |
| **C-058-02** | An edge is not treated as legal because its target resolves. | RMS §4 |
| **C-058-03** | No World record references an issue, and no World field references an issue, tier, medium, artifact, or the real world. | Blueprint §13.6a rule 3, §11; I-17; RMS §7 |
| **C-058-04** | No W, P or V Record references an I Record; E references I only for reveal ordering. | RMS §8.2; Roadmap §2.4 |
| **C-058-05** | No World record references an E or P Record. | Roadmap §2.4 |
| **C-058-06** | An E → W edge is a reference; any mutation of W arising from E happens only via the governed path. | RMS §8.2 |
| **C-058-07** | V never mutates W. | RMS §11.2; I-89 |
| **C-058-08** | No Registry Record owns, depends on, mutates, or takes semantic authority from a domain instance; its references to Registry definitions and to declared Record Models, Kinds, schemas and semantic contracts are allowed. | RMS §10.3 |
| **C-058-09** | A cross-model reference changes no Record's owning Record Model or partition. | RMS §6.1; I-16; Blueprint §13.6a rule 2; RMS §12.2 |
| **C-058-10** | No Issue reference makes anything canon. | Spine law 5; Blueprint §13.6a rule 1; RMS §12.2; I-04 |
| **C-058-11** | A cross-model reference is not required to be, and is not treated as, a World Relationship Record. | I-102; Artifact 055 |
| **C-058-12** | A cross-model edge decides no package composition and admits no Kind. | I-107; RMS §6, §6.1, §13; Artifacts 056, 057 |
| **C-058-13** | No invariant is minted or amended. | Blueprint §36, §10.4; P-28; I-15 |

A construction satisfying all thirteen is conformant **to this contract**. That is not conformance
to the dependency matrix, which is source-blocked (§8.3).

## 17. Worked Examples

> **Illustrative and non-normative.** Each rests on the source cited; none decides an edge.

**Example A — E → W.** An E `MYSTERY` references the World truth it concerns. RMS §8.1: it *"never
contains or owns it."* The reference uses a resolvable ID (§6). Any change to that World truth goes
via the governed path (RMS §8.2); the reference makes none.

**Example B — E → I.** A `REVEAL-STATE` is ordered for the readership by issue ordinal (RMS §8.2).
That reference to I is the only sanctioned Issue dependency. A P `SCHEDULE` referencing an `ISSUE`
is not sanctioned (§8.1).

**Example C — Registry.** A `KIND-DEFINITION` may reference the declared Kind `CHARACTER` (RMS
§10.3). It may not reference, depend on, or take its meaning from a particular `W-CH-…` Record.

**Example D — I → W.** An `ARTICLE` references a World `EVENT`. Blueprint §13.6a: *"That never
makes an issue the owner of the event."* Whatever the article asserts, *"Nothing in an issue is true
because it is printed."* (Spine law 5; Blueprint §13.6a rule 1).

**Example E — not established.** A P `ARC` referencing a World `EVENT` is listed by Roadmap row
465's *"P→all"* and stated by no Blueprint or RMS text available here. This contract neither allows
nor forbids it (§8.3).

**Example F — conflict.** A World `CHARACTER` referencing its `CANONICAL-VISUAL-SPECIFICATION`:
Blueprint §13.6c says every Record may reference visual objects; Roadmap §2.4 forbids W → V. This
contract records the conflict (§8.2) and decides nothing.

## 18. Source Traceability

| Rule | Source |
|---|---|
| Resolvable ID the only legal cross-model handle | RMS §4 |
| Resolution mechanical and uniform; legality model/Registry-owned | RMS §4 |
| Matrix delegated to Deliverable J | RMS §22–23, Appendix G, §10.3 |
| E → W, E → I | RMS §8.2; Blueprint §13.6a rule 3, §13.6b |
| E → P (reader models) | Blueprint §11; RMS §9.1 |
| I → W, E, P, V; references never own | Blueprint §13.6a rules 2–3; RMS §12.2 |
| Any Record → V | Blueprint §13.6c |
| V → W; Visual never mutates World | Roadmap row 465; RMS §11, §11.2; I-89 |
| Any → R via `registry_ref` | RMS §4; Artifact 033 |
| Registry reference boundary | RMS §10.3, §24 |
| Manifestation-blindness | Blueprint §11, §13.6a rule 3; I-17; RMS §7 |
| Forbidden edges | Roadmap §2.4 |
| Direction of reference frozen | Blueprint §13.6a rule 3, §13.6b |
| Publication firewall | Spine law 5; Blueprint §13.6a rule 1; RMS §12.2; I-04, I-104 |
| One owning model; no conversion | RMS §6.1; I-16 |
| Relationship mechanisms model-owned; RR World-only | RMS §15; I-102 |
| Packaging model-owned | I-107 |
| Invariants are the Blueprint's | Blueprint §36, §10.4; P-28; I-15 |
| Identity and acceptance | Roadmap row 058 |

## 19. Final Contract Statement

A cross-model reference uses a resolvable ID; that it resolves does not make it legal. E references
W, mutating it only via the governed path, and references I for reveal ordering — the only
sanctioned Issue dependency. I references W, E, P and V and owns none of them; nothing becomes canon
by being published. No World record references an issue, and World references nothing in E or P.
The Registry references definitions and declarations, never domain instances. No reference changes
who owns a Record. W → V is in conflict between the sources, and the edges Deliverable J would hold
are not established; this contract decides neither, and the matrix as a whole is source-blocked.

---

*Artifact 058 · P2/2d · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the cross-model edges the Blueprint, the RMS and the Roadmap establish. It does not
amend them, defines no resolver, schema or matrix cell they leave undefined, and treats no unstated
edge as forbidden. Where it differs from the Master Blueprint, the Record Model System, or the OS
File Build Roadmap, those governing sources are correct and this document is wrong.*
