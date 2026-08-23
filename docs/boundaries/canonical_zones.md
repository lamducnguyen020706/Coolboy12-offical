# COOLBOY12 — Canonical Zone Declaration

**Artifact 017** · `docs/boundaries/canonical_zones.md` · Own: CONST · RM: n/a · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d ·
Req: BR-04 · BP: §9.1 · RMS: §4 · H: 016 · S: — · LS: — ·
G: precondition of every canonical gate · → 023,133 · Risk: high · ∥: no

## 1. Purpose

This document answers one question: **which parts of the repository are canonical zones, and
who may write them?**

It enumerates the canonical zones and states the write restriction over them. It enforces
nothing. Artifact 022 (`.claude/hooks/canon_deny.py`) denies direct filesystem writes, Artifact
023 (`.claude/hooks/zones.json`) encodes these zones machine-readably, and Artifact 152
(`src/coolboy12/mutation/coordinator.py`) implements the governed write path. None of the three
exists yet.

Artifact 016 answers a different question — *what source-of-truth class does a repository family
belong to* — and its taxonomy is not restated here. This document takes one fact from it,
`canon/** = AUTHORITATIVE`, and adds the dimension 016 deliberately left out: **being
AUTHORITATIVE is not permission to write.**

## 2. What a Canonical Zone Is

A **canonical zone** is a repository zone that stores the authoritative canonical Records of a
Record Model. Blueprint §9.1 fixes what that means by separating four classes of state:

| Class (§9.1) | What it holds | Rule |
|---|---|---|
| **Canon** | What is true in the world | *"Written only through the single gated path. Authoritative."* |
| **Production State** | What the author decided about *making the work* | Durable and provenanced, *"never authoritative about the world"*; changed by production ceremony, **not** the canon path |
| **Working** | Drafts, proposals, simulation deltas, emergent seeds | *"Provisional. Never authoritative. Becomes canon only through the gate."* |
| **Derived** | Indexes, dashboards, timelines, projections, published output | Recomputable from Canon + Production State + history with no loss |

Three consequences bound this document:

1. **A canonical zone is defined by what it holds and how it is written**, not by its filesystem
   permissions. A directory is canonical because the architecture says its contents are
   canonical Records, not because a tool restricts access to it.
2. **`docs/**` is not a canonical zone.** Specifications there are AUTHORITATIVE about
   architecture and hold no canonical data (`Canon: n/a` throughout, including this file).
   Artifact 017 protects `canon/**`; it does not move `docs/**` into Canon.
3. **An empty canonical zone is valid.** Roadmap PART X states that before any `G-CANON-*` gate,
   **empty `canon/**` is legal**, while *any real canonical data* is illegal. The zone and its
   write rule exist whether or not a single Record has ever been written.

## 3. The Canonical Root

```
canon/**    ← the protected canonical family
```

Roadmap PART I classifies the root:

| Path | Owner | SoT | Rebuildable | Write | Delete | Prohibited | Phase |
|---|---|---|---|---|---|---|---|
| `canon/**` | six models | AUTHORITATIVE | No | **Mutation Coordinator only** | Never (retire) | derived output, drafts, external material | P5 |

The root is one protected family and **six semantic ownership partitions**. It is not one
undifferentiated store: the protection is uniform, the canonicality is not (§5).

No zone other than the six named in §4 exists beneath the root. `canon/derived/`,
`canon/cache/`, `canon/temp/`, and `canon/config/` are not canonical zones and must not be
created — a rebuildable, disposable, or configuration artifact placed under `canon/` is
misfiled, not reclassified.

## 4. The Six Model-Owned Canonical Zones

The canonical root is owned across exactly six sovereign Record Models. There is no seventh
model and no seventh zone.

```
canon/**
├── canon/world/**        W — World
├── canon/epistemic/**    E — Epistemic
├── canon/production/**   P — Production
├── canon/registry/**     R — Registry
├── canon/visual/**       V — Visual
└── canon/issue/**        I — Issue
```

This is the complete zone inventory. Artifact 022 denies direct writes across it; Artifact 023
encodes it. Neither may add a zone, remove one, or reinterpret an owner.

## 5. Normative Zone Table

Reproduced from Roadmap PART VII, whose qualifiers are constitutional and are not paraphrased
away. **`Authoritative` here states what the zone is authoritative *about*** — it never means
"writable", and it never means "World truth".

| Zone | Owner | SoT | Authoritative — about what | Rebuildable | Write | Delete | Key prohibition |
|---|---|---|---|---|---|---|---|
| `canon/world/**` | W | AUTHORITATIVE | **Yes** world truth | No | Mutation Coordinator only | Never (retire) | derived output · drafts · external material |
| `canon/epistemic/**` | E | AUTHORITATIVE | Yes knowledge state | No | Mutation Coordinator only | Never (retire) | knowledge state is not World truth |
| `canon/production/**` | P | AUTHORITATIVE | Yes **within P only** | No | Mutation Coordinator only | Never (retire) | **No — never canon** |
| `canon/registry/**` | R | AUTHORITATIVE | Yes **about meaning** | No | Mutation Coordinator only | Never | **domain instances of W/E/P/V/I** |
| `canon/visual/**` | V | AUTHORITATIVE | **By kind** — spec yes, asset no, analysis no | No | Mutation Coordinator only | Never (retire) | asset and analysis are not canonical authority |
| `canon/issue/**` | I | AUTHORITATIVE | Yes **publication only, never canon** | No | Mutation Coordinator only | Never (retire) | publication creates no world fact |

**Canonicality is model-scoped.** Writing *"everything under `canon/**` is World Canon"* would be
false in five of six zones. PART VII's own `May influence canon` column shows how narrow each
zone's reach is: `canon/epistemic/**` **Yes (frames)** · `canon/registry/**` **Governs form;
cannot override truth** · `canon/visual/**` **Spec yes; analysis only via E** ·
`canon/production/**` **No — never canon** · `canon/issue/**` **No**.

Two of these deserve restating because they are the easiest to lose:

- **Production is authoritative within Production and is never World canon.** Blueprint §9.1:
  Production State is *"never authoritative about the world"*, and a production change's effect
  on canon is *"none, ever. A production change that would alter what is true is not a
  production change; it is a canon proposal and takes the canon path."*
- **Issue is publication only and creates no truth.** I-61: *"Shipping never creates a world
  fact."*

## 6. The Registry Canonical Boundary

`canon/registry/**` carries a prohibition no other zone carries, and it is architectural rather
than incidental. Roadmap PART I:

| Path | Owner | SoT | Write | Delete | Prohibited | Phase |
|---|---|---|---|---|---|---|
| `canon/registry/` | R | AUTHORITATIVE | Coordinator | Never | **domain instances of W/E/P/V/I** | P3 |

> **Registry defines meaning. Registry does not own domain instances.**

Registry canon **may** hold Registry-owned definition Records — semantic definitions, schema
definitions, kind definitions, field definitions, relationship-type definitions, and the other
Registry definition families. Registry canon **must not** hold World, Epistemic, Production,
Visual, or Issue domain instances.

This is a rule about **ownership, not visibility.** Registry may reference declared Record
Models, declared Kinds, and declared schemas where its own boundary permits; what it may never
do is own, hold, or become the store for another model's instances. Reducing this to "Registry
cannot access them" would be wrong in the permissive direction, and flattening
`canon/registry/**` into the generic root row would erase the distinction entirely.

Registry's authority is also bounded in the other direction: it is authoritative **about
meaning** and **cannot override truth** (PART VII). A Registry definition governs the *form* a
World Record takes; it never decides what is true of the world.

## 7. Write Authority

> **The Mutation Coordinator is the only component that writes `canon/**`.**

This is constitutional, stated three times across the sources and identically each time:

- **I-83** — *"The Mutation Coordinator is the only component that writes canon. Stages may be
  delegated to external components; the write boundary may not. Execution-substrate guard rails
  are defence-in-depth, never constitutional authority."*
- **Roadmap PART I** — `canon/**` Write: **Mutation Coordinator only**.
- **Roadmap PART X** — before any canonical gate, *any write not routed through 152* is illegal.

**Human Gate and Mutation Coordinator are not interchangeable roles**, and collapsing them is the
characteristic failure this section exists to prevent:

```
Human Gate            authorizes the mutation      (a person decides; nothing self-commits)
Mutation Coordinator  performs the governed write  (the single canonical write boundary)
```

The gate does not write. The Coordinator does not authorize. Neither substitutes for the other.

**No other actor holds canonical write authority — not by trust, position, or convenience.**
The following are named explicitly because each is a plausible mistake:

| Actor | Canonical write authority |
|---|---|
| Application code in `src/**` | **No** — DEV-ENV, non-authoritative (016) |
| The execution environment, its hooks, commands, and scripts | **No** — the environment runs coolboy12 and does not define it (014, P-33, I-100) |
| Version control — a commit, branch, tag, or merge | **No** — records that files changed, never what changed canonically (013, I-85) |
| An external service, store, adapter, or provider | **No** — I-84: no external component holds canonical semantics or adjudicates a mutation |
| Validators, tests, CI, the editor | **No** — a check reports; it does not commit |
| A Record Model itself | **No** — a model owns its semantics; the write boundary is not distributed |
| The Human Gate | **No** — it authorizes; the Coordinator writes (above) |

## 8. The Canonical Mutation Path

Roadmap PART X states the sequence for canonical writes after a model's gate opens:

```
proposal
    ↓
basis
    ↓
preflight
    ↓
Human Gate
    ↓
commit set
    ↓
changelog
```

Blueprint §12.6 and Spine law 2 give the same single path — *propose → check → human gate →
commit → changelog → log* — and make the commit atomic. This document reproduces the sequence
and defines no sub-step of it; the stages belong to §12.6 and to Artifact 152.

**Each model writes only after its own gate.** PART X: after `G-CANON-W`, World canon, Coordinator
only, on the path above; after `G-CANON-E/P/V/I`, *"that model's records, on the same path, **and
not before its own gate**."* This document does not define those gates. It is their
precondition — the zones must be declared before any gate can rely on them.

## 9. Direct-Write Prohibition

> **A direct write to `canon/**` is prohibited.**

Roadmap PART X lists it first under **ALWAYS PROHIBITED**: *direct `canon/**` writes · a second
write path · derived promoted to authority · external material without a proposal · Registry
holding domain instances · publication creating truth · Production becoming canon · popularity
becoming truth.*

The prohibition binds every actor without exception, including: application code · tests ·
scripts · CI · the editor · Git hooks · external tools · plugins · adapters · environment
commands.

**Trust is not write authority.** No actor acquires the ability to write canon by being
trusted, being internal, being convenient, being already permitted at the filesystem level, or
being the component that happens to hold the credentials. A filesystem that permits the write
is not an architecture that authorizes it.

**A second write path is a second canon** (RMS §4, Spine law 2). Any mechanism that reaches
`canon/**` other than through the Mutation Coordinator is that second path, whatever it is
called.

### Prohibited contents

Beyond the write rule, `canon/**` prohibits certain contents outright (Roadmap PART I):
**derived output · drafts · external material.**

- **Derived output** — a rebuildable projection is DERIVED and belongs in `derived/**`. Derived
  promoted to authority is on PART X's always-prohibited list.
- **Drafts** — Working state per §9.1 is *"provisional, never authoritative"* and becomes canon
  only through the gate.
- **External material** — EXTERNAL class, and per PART VII it may influence canon **only via
  proposal (386)**, never by placement. Artifact 015 carries the narrower case: secret material
  is EXTERNAL forever and enters neither Canon nor Derived, and no proposal path exists for a
  secret because a secret is not a candidate world truth.
- **Fixtures** — PART X permits *fixtures explicitly non-canonical* before a gate, and prohibits
  *any fixture mistakable for canon*. A fixture never belongs in `canon/**`.

## 10. Delete and Retire

`canon/**` is **never destructively deleted.** Roadmap PART I gives `Delete: Never (retire)` for
the root and `Never` for `canon/registry/`.

```
filesystem deletion   ≠   canonical retirement
```

A canonical Record leaves active use by being **retired or superseded through its own model's
governed mutation process**, which is itself a canonical mutation on the path in §8 — not by
being removed from disk. Deleting the file destroys the record of a decision; retiring the
Record records one.

This document defines no retirement mechanism, no lifecycle states, and no filesystem flag. Each
Record Model owns its own retirement semantics.

## 11. Interactions With the Adjacent Boundaries

Artifacts 013–016 are referenced for their canonical-zone consequences only and are not restated.

| Boundary | Consequence for canonical zones |
|---|---|
| **016 — Source of truth** | `canon/**` is AUTHORITATIVE. This document adds the dimension 016 excluded: **AUTHORITATIVE is not writable.** Both hold; neither contradicts the other. |
| **015 — Secrets** | Secret material is EXTERNAL forever and is prohibited from `canon/**`. No new secret policy is created here. |
| **014 — Environment** | Environment tooling holds no semantic authority and therefore no canonical write authority. Its guard rails — including the hook Artifact 022 will build — are defence-in-depth, never constitutional authority (I-83). Where a guard rail and the Human Gate disagree, the gate governs. |
| **013 — Version control** | A Git operation changes repository files; it never authorizes a canonical mutation. Committing a file into `canon/**` does not make its contents canonical, and does not satisfy the mutation path. |

## 12. Downstream Enforcement Boundaries

```
017  canonical zone contract          ← this document, declarative
  ↓
022  canon write-deny hook            .claude/hooks/canon_deny.py
023  zone permission configuration    .claude/hooks/zones.json
152  Mutation Coordinator             src/coolboy12/mutation/coordinator.py
```

**None of 022, 023, or 152 exists.** This document is their contract and implements no part of
any of them.

- **022** denies direct filesystem writes to the zones in §4. Its Roadmap validation is *direct
  write to `canon/**` denied*, proven by negative test. This document states the rule; it does
  not prove it, and defines no hook, syntax, or deny mechanism.
- **023** encodes the zone list machine-readably. Its Roadmap validation is *zones match 017
  exactly* — so §4 is the list it must match. No JSON, configuration syntax, or hook setting is
  created here.
- **152** implements the governed write path and is *the only component that writes `canon/**`*.
  This document states who may write and why; 152 implements how.

Artifact 017 is also, per its own Roadmap row, the **precondition of every canonical gate**. It
defines no gate. `G-CANON-W`, `G-CANON-E`, `G-CANON-P`, `G-CANON-V`, and `G-CANON-I` belong to
their own phases and are not created, described, or anticipated here.

## 13. Standing Rules

1. The canonical zones are `canon/**` and its six model subtrees — world, epistemic, production,
   registry, visual, issue. There is no seventh zone and no seventh model.
2. The Mutation Coordinator is the only component that writes `canon/**`.
3. The Human Gate authorizes; the Mutation Coordinator writes. The two are never interchangeable.
4. Every direct write to `canon/**` is prohibited, for every actor, with no exemption for trust,
   position, or convenience. A second write path is a second canon.
5. Canonicality is model-scoped. Production is never World canon; Registry governs meaning and
   cannot override truth; Visual authority is by kind; Issue is publication only and creates no
   world fact.
6. `canon/registry/**` must never hold domain instances of W, E, P, V, or I.
7. `canon/**` prohibits derived output, drafts, and external material — including secret
   material, and including any fixture mistakable for canon.
8. `canon/**` is never destructively deleted. A Record is retired through its model's governed
   process; filesystem deletion is not retirement.
9. An empty `canon/**` is legal before any canonical gate. Real canonical data before a gate is
   not.
10. `docs/**` is AUTHORITATIVE about architecture and is not a canonical zone.

## 14. Boundary of This Document

This document declares. It enforces nothing and implements nothing: no hook, no machine-readable
zone configuration, no filesystem permission system, no Mutation Coordinator, no canonical gate,
no retirement mechanism, and no test. It creates no canonical Record of any model and no fixture;
`canon/**` remains empty, which this document affirms is legal at P0.

It defines no source-of-truth taxonomy (Artifact 016), no rebuild convention (Artifact 020), and
no model schema. It reproduces no boundary document in full — 013, 014, 015, and 016 are cited
for their canonical-zone consequences only.

The Mutation Coordinator named throughout is **Roadmap artifact 152** (`P5/5a`, *sole writer*) and
**does not yet exist**. The write rules here are current operational rules whose mechanism arrives
later; nothing in this document may be read as a claim that the enforcement is in place.

`Req: BR-04` is preserved as written. The requirement register is not currently available
(Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here; this
document is validated against its Roadmap, Blueprint, and RMS citations instead.
