# COOLBOY12 — Source-of-Truth Boundary

**Artifact 016** · `docs/boundaries/source_of_truth.md` · Own: CONST · RM: n/a · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d ·
Req: BR-04,BR-107,BR-108 · BP: §9.1,§29,§29.6a · RMS: §4 · H: 003 · S: — · LS: — · G: — ·
→ 017, PART VII · Risk: HINGE · ∥: no

## 1. Purpose

This document answers one question: **what is the source-of-truth class of any artifact in this
repository, and what follows from that class?**

It fixes the classification vocabulary, reproduces the two normative source tables, and states
what each class licenses and forbids. It classifies; it does not enforce. Artifact 017 declares
the canonical zones and their write restrictions, Artifact 020 defines rebuild conventions, and
Artifact 050 implements the record-level classification mechanism. None of those is built here.

## 2. Two Levels of Classification — Read This First

The sources classify source-of-truth at **two distinct levels**, and conflating them is the
first mistake this document exists to prevent.

| Level | Governing source | Classifies | Class count |
|---|---|---|---|
| **Record / data class** | Blueprint §29.6a, RMS §4 | *"Every **data class** in the system"* — Records, indexes, caches, working state, external services | **five** |
| **Repository artifact class** | Roadmap PART VII, PART I | *"**Artifact class**"* — repository paths and directory families | **six** |

Blueprint §29.6a names five classes — AUTHORITATIVE, DERIVED, CACHED, TEMPORARY, EXTERNAL —
and the Blueprint records that scheme as **Frozen** at *"Five classes; every external store is
DERIVED or CACHED."* RMS §4 lists it identically: *"Source-of-truth classification | §29.6a —
five classes | Constitutional,"* and carries `sot_class` as one of the seven FROZEN universal
envelope fields.

The Roadmap's PART VII table adds a sixth, **DEV-ENV**, and assigns it to `src/**`, `tests/**`,
`benchmarks/**`, and `.claude/**` — repository zones that hold no data class at all.

> **DEV-ENV is Roadmap-only.** The string `DEV-ENV` appears **zero times in the Blueprint and
> zero times in the RMS**. This document does not claim Blueprint authority for it, and no
> reader may cite this document as evidence that the Blueprint recognises six classes.

**How the two levels stand together.** §29.6a scopes itself to *data classes* and its examples
are all data. PART VII's own column header is *Artifact class*, and DEV-ENV covers exactly the
zones that carry no data class. The two tables therefore answer different questions and neither
is overruled by the other. **This document does not resolve the discrepancy beyond stating it**;
it is recorded in the Revolving Resolution Note as CONFLICT-C. Where a record-level class is
required, the Blueprint's five govern (§13); where a repository path must be classified, the
Roadmap's six govern (§3–§6).

## 3. The Six Repository Source-of-Truth Classes

Exactly six, for repository artifact classification. No seventh exists, none may be added here,
and no alias — SOURCE, SYSTEM, RUNTIME, LOCAL, CONFIG, SECRET, GENERATED, IMPLEMENTATION,
CANONICAL — is a source-of-truth class.

| Class | Meaning |
|---|---|
| **AUTHORITATIVE** | This is where the fact lives (§29.6a). Not rebuildable; the fact exists nowhere else. |
| **DERIVED** | Recomputable with no loss from authoritative sources (§29.6a). |
| **CACHED** | Recomputable and disposable, held only for speed (§29.6a). |
| **TEMPORARY** | Exists within one workflow and does not outlive it (§29.6a). |
| **EXTERNAL** | Lives outside coolboy12 entirely (§29.6a). |
| **DEV-ENV** | Roadmap PART VII only; no Blueprint or RMS definition. Applied to development and environment zones — `src/**`, `tests/**`, `benchmarks/**`, `.claude/**`. Non-authoritative. |

**Only AUTHORITATIVE is authoritative.** The other five classes are not five alternative sources
of truth; they are five ways of being *non*-authoritative. This document must never be read as
establishing multiple sources of truth.

**Secret material is EXTERNAL** (Artifact 015). `SECRET` is not a source-of-truth class, and
secret material is not DEV-ENV merely because the environment uses it operationally.

## 4. Normative Classification Table — Roadmap PART VII

Reproduced from Roadmap PART VII. This table is normative; its qualifiers are constitutional
constraints and are not to be paraphrased away.

| Artifact class | SoT | Authoritative | Rebuildable | Deletable | May influence canon | May write canon |
|---|---|---|---|---|---|---|
| `canon/world/**` | AUTHORITATIVE | **Yes** world truth | No | No | — | No |
| `canon/epistemic/**` | AUTHORITATIVE | Yes knowledge state | No | No | Yes (frames) | No |
| `canon/production/**` | AUTHORITATIVE | Yes **within P only** | No | No | **No — never canon** | No |
| `canon/registry/**` | AUTHORITATIVE | Yes **about meaning** | No | No | Governs form; **cannot override truth** | No |
| `canon/visual/**` | AUTHORITATIVE | **By kind** — spec yes, asset no, analysis no | No | No | Spec yes; analysis only via E | No |
| `canon/issue/**` | AUTHORITATIVE | Yes **publication only, never canon** | No | No | **No** | No |
| `derived/**` | DERIVED | **No** | Always | Freely | No | No |
| `derived/caches/**` | CACHED | No | Always | Freely | No | No |
| `docs/**` specs | AUTHORITATIVE | Yes architecture | No | Supersede only | Yes governs | No |
| `src/**`, `tests/**`, `benchmarks/**` | DEV-ENV | No | Yes | Yes | No | **Only 152** |
| `fixtures/**` | TEMPORARY | No | Yes | Yes | **No** | No |
| `examples/**` | DERIVED | No | Yes | Yes | No | No |
| external material | EXTERNAL | No | n/a | n/a | **Only via proposal (386)** | No |

**"Only 152"** names the Mutation Coordinator (`src/coolboy12/mutation/coordinator.py`, Roadmap
artifact 152, *"the only component that writes `canon/**`"*). It is a statement about one
component, **not** a permission granted to `src/**` as a zone. See §8.

## 5. Per-Directory Rules — Roadmap PART I

Reproduced from Roadmap PART I. Artifact 016's Done criterion makes this table normative.

| Path | Owner | SoT | Rebuildable | Write | Delete | Prohibited | Phase |
|---|---|---|---|---|---|---|---|
| `canon/**` | six models | AUTHORITATIVE | No | **Mutation Coordinator only** | Never (retire) | derived output, drafts, external material | P5 |
| `canon/registry/` | R | AUTHORITATIVE | No | Coordinator | Never | **domain instances of W/E/P/V/I** | P3 |
| `derived/**` | consuming model | DERIVED | **Always** | rebuild process | **Freely** | anything unrebuildable | P8 |
| `derived/coverage/`, `derived/health/` | P/GOV | DERIVED | Always | rebuild | Freely | authority claims | P14/P15 |
| `docs/**` | authoring layer | AUTHORITATIVE (spec) | No | authored | supersede only | implementation detail | P0+ |
| `src/**` | layer | DEV-ENV | Yes | authored | Yes | canonical data | P0+ |
| `tests/**`, `benchmarks/**` | layer | DEV-ENV | Yes | authored | Yes | canonical data | P0+ |
| `fixtures/**` | layer | TEMPORARY | Yes | authored | Yes | **anything resembling real canon** | P3+ |
| `examples/**` | model | DERIVED | Yes | authored | Yes | authority claims | P7+ |
| `.claude/**` | env | DEV-ENV | Yes | authored | Yes | canon, secrets | P0 |

## 6. Reading the Two Tables Together

The tables have different coverage and neither is a subset of the other. PART VII names the six
`canon/` model subtrees, `derived/caches/**`, and external material; PART I names
`canon/registry/`, `derived/coverage/`, `derived/health/`, and `.claude/**`. Both are normative.

**Directory-family precedence.** Where a more specific family is classified, the specific
classification governs its subtree; the general family governs everything else beneath it. This
is a reading rule for the source tables, not a new taxonomy:

```
derived/**          DERIVED
  └ derived/caches/**   CACHED        ← more specific; governs its own subtree
canon/**            AUTHORITATIVE
  └ per-model qualifications apply    ← PART VII names each model's authority scope
```

**No file escapes its directory's class.** A file's classification is its containing family's
classification unless the source names a more specific family that contains it. Placing a file
in a directory does not exempt it from that directory's class, and a misplaced file is a
violation to correct, not a reclassification.

**Coverage.** Every directory presently in the repository falls under a source-named family:
`canon/` and its six model subtrees · `derived/` and its subtrees, with `derived/caches/`
distinct · `docs/` and its subtrees · `src/` and its subtrees · `tests/` and its subtrees ·
`benchmarks/` · `fixtures/` · `examples/` · `.claude/`. No directory requires a class the
sources do not supply, and none is unclassified.

## 7. Authority Is Not Source-of-Truth, and Neither Is Canon

Three questions that this document must keep apart:

```
source-of-truth class   where the artifact's authority and lifecycle live
authority               what the artifact governs, and who may change it
canonicality            whether it is canon, and about what — model-defined
```

**AUTHORITATIVE does not mean "is Canon."** `docs/**` specifications are AUTHORITATIVE about
architecture and are not canonical data at all (`Canon: n/a` throughout). This document is
itself AUTHORITATIVE and holds no World Truth.

**AUTHORITATIVE does not mean "writable."** Every `canon/**` row in PART VII reads
`May write canon: No`. Authority over content is not permission to write it.

**AUTHORITATIVE is not one undifferentiated authority.** PART VII qualifies each canon subtree
separately, and those qualifiers are load-bearing:

| Subtree | Authoritative — exactly what |
|---|---|
| `canon/world/**` | World truth |
| `canon/epistemic/**` | Knowledge state — never truth itself |
| `canon/production/**` | **Within P only** · **never canon** |
| `canon/registry/**` | **About meaning** · governs form, **cannot override truth** |
| `canon/visual/**` | **By kind** — specification yes, asset no, analysis no |
| `canon/issue/**` | **Publication only, never canon** |

A reader who flattens these into "everything under `canon/` is canonical truth" has broken the
Production boundary, the Registry boundary, the Visual authority split, and the Publishing
Firewall in one step.

## 8. Canon Influence and Write Authority

**The Mutation Coordinator is the only component that writes canon** (Roadmap 152; Blueprint
§12.6; I-83). Nothing in this document's classification grants a write.

PART VII's `May write canon` column reads `No` for every row except the `src/**`, `tests/**`,
`benchmarks/**` row, which reads **`Only 152`**. That entry does not make the DEV-ENV zone a
canon writer. It records that the single component permitted to write canon happens to live in
that zone as source code. DEV-ENV remains non-authoritative, and every other file in it is as
unable to write canon as any file anywhere else.

The `May influence canon` column is likewise narrow and qualified:

- `canon/epistemic/**` — **Yes (frames)**
- `canon/registry/**` — **Governs form; cannot override truth**
- `canon/visual/**` — **Spec yes; analysis only via E**
- `canon/production/**` — **No — never canon**
- `canon/issue/**` — **No**
- external material — **Only via proposal (386)**
- `derived/**`, `derived/caches/**`, `examples/**`, `fixtures/**`, `src/**`, `tests/**`,
  `benchmarks/**` — **No**

## 9. Rebuildability

Rebuildability is a property of the class, and it is not a synonym for DERIVED — four separate
classes are rebuildable and they remain four separate classes.

| Class | Rebuildable (per PART VII / PART I) |
|---|---|
| AUTHORITATIVE | **No** — for `docs/**` and every `canon/` subtree alike |
| DERIVED | **Always** |
| CACHED | **Always** |
| TEMPORARY | Yes |
| DEV-ENV | Yes |
| EXTERNAL | **n/a** — not classified by rebuildability |

Blueprint §29.6a states the consequence: *"A `DERIVED` value that cannot actually be rebuilt is
a misfiled `AUTHORITATIVE` value (P-26)."* §29.8's rebuild-from-canon drill is how that is
tested — *"a derived store that has never been deleted is a store whose classification is an
assumption."* This document classifies; **Artifact 020 defines the rebuild conventions** and no
rebuild method, dependency graph, command, staleness rule, or cache-invalidation mechanic is
defined here.

## 10. Deletability

| Class | Deletable (per PART VII / PART I) |
|---|---|
| AUTHORITATIVE — `canon/**` | **No** · **Never (retire)** |
| AUTHORITATIVE — `docs/**` | **Supersede only** |
| DERIVED | **Freely** |
| CACHED | **Freely** |
| TEMPORARY | Yes |
| DEV-ENV | Yes |
| EXTERNAL | **n/a** |

`Never (retire)` and `Supersede only` are the two non-deletion rules and they differ: canon is
retired in place, a specification is superseded by a later one. No deletion guarantee beyond
these is stated by the sources, and none is added here.

## 11. CACHED, TEMPORARY, and DERIVED Are Three Classes

They share non-authority and rebuildability, and the sources still keep them apart. Collapsing
any two would discard a distinction later artifacts rely on.

| Class | What distinguishes it | Repository instance |
|---|---|---|
| **DERIVED** | Recomputable **with no loss** from authoritative sources | `derived/**`, `examples/**` |
| **CACHED** | Recomputable and **disposable, held only for speed** | `derived/caches/**` |
| **TEMPORARY** | **Exists within one workflow and does not outlive it** | `fixtures/**` |

`fixtures/**` is TEMPORARY, not DERIVED, and its PART I prohibition is **anything resembling
real canon**. Reclassifying fixtures as DERIVED would be a source error.

## 12. Boundary Interactions

Artifacts 013, 014, and 015 are not restated here. Only their source-of-truth consequences:

| Boundary | Source-of-truth consequence |
|---|---|
| **Version control** (013) | Repository file history is not a source-of-truth class for canon and confers no semantic authority. Version control records that files changed; it never determines what changed canonically. No SoT class is created for it. |
| **Environment** (014) | The execution environment's zones are DEV-ENV — non-authoritative. The environment runs coolboy12 and does not define it; classification grants it nothing. `.claude/**` is DEV-ENV, prohibited from holding canon or secrets. |
| **Secrets** (015) | Secret material is **EXTERNAL**, and is never AUTHORITATIVE, DERIVED, CACHED, or DEV-ENV. No secret enters `canon/**` or `derived/**`. Operational use by the environment does not reclassify it. |

## 13. Record-Level Classification Boundary

Directory classification is **not** the whole source-of-truth architecture.

Blueprint §29.6a classifies data classes; RMS §4 places source-of-truth classification in the
universal mechanism layer and carries **`sot_class`** as one of the seven FROZEN universal
envelope fields. A Record's class travels in its envelope; it is not inferred from where the
file sits.

This document defines no record-level mechanism, no envelope field, no validator, and no
universal Record schema. **Artifact 050** (`src/coolboy12/kernel/sot.py`, `Val: every record
carries exactly one class`, `BP: §29.6a`) implements that mechanism against the Blueprint's five
data classes. Per §2, DEV-ENV is a repository-level class and carries no Blueprint definition;
whether it is admissible as a record-level `sot_class` value is **not decided here** and is not
this artifact's to decide.

## 14. Downstream Implementation Boundary

```
016  source-of-truth contract        ← this document
  ↓
017  canonical zones                 docs/boundaries/canonical_zones.md
020  rebuild conventions             docs/conventions/rebuild.md
050  SoT classification mechanism    src/coolboy12/kernel/sot.py
```

**None of 017, 020, or 050 exists yet.** This document supplies their contract and implements
none of them.

- **017** declares which zones are canonical and what write restrictions apply. This document
  states classes, not zone permissions or a write-deny target list.
- **020** defines rebuild conventions — how a derived thing declares its rebuild method. This
  document states *that* DERIVED is rebuildable, never *how*.
- **050** enforces that every record carries exactly one class. This document states the
  vocabulary; it enforces nothing.

## 15. Standing Rules

1. Exactly six classes classify repository artifacts: AUTHORITATIVE, DERIVED, CACHED,
   TEMPORARY, EXTERNAL, DEV-ENV. No seventh may be created, none merged, none renamed.
2. Only AUTHORITATIVE is authoritative. The other five are five ways of not being authoritative.
3. AUTHORITATIVE never means "is Canon" and never means "may write Canon".
4. Each `canon/` subtree carries its own authority qualification. Production is authoritative
   within P only and never canon; Registry governs meaning and cannot override truth; Visual
   authority is by kind; Issue is publication only.
5. The Mutation Coordinator is the only component that writes `canon/**`. `Only 152` names that
   component, never its zone.
6. DERIVED, CACHED, and TEMPORARY are three classes, not one. A derived thing that cannot be
   rebuilt is a misfiled authoritative thing (P-26).
7. `canon/**` is never deleted, only retired. `docs/**` is superseded, never deleted.
8. Secret material is EXTERNAL, always, and enters neither Canon nor Derived.
9. DEV-ENV is Roadmap-only and non-authoritative. It appears in no Blueprint or RMS text.
10. A file carries its containing family's class unless the source names a more specific family
    containing it. Misplacement is a violation, not a reclassification.

## 16. Boundary of This Document

This document classifies. It enforces nothing, implements nothing, and creates no code, hook,
schema, validator, Record field, or Record Model. It declares no canonical zone permission list
(017), no rebuild method (020), and no classification mechanism (050). It creates no Canon data
and no Derived data.

The Mutation Coordinator named throughout is Roadmap artifact 152 and **does not yet exist**;
the write rules stated here are current operational rules whose mechanism arrives later.

One source discrepancy is recorded rather than resolved: the Blueprint and RMS state **five**
source-of-truth classes for data classes, while the Roadmap states **six** for repository
artifact classes, the sixth being DEV-ENV with no Blueprint or RMS basis. See §2 and the
Revolving Resolution Note, CONFLICT-C.

`Req: BR-04,BR-107,BR-108` is preserved as written. The requirement register is not currently
available (Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here;
this document is validated against its Roadmap, Blueprint, and RMS citations instead.
