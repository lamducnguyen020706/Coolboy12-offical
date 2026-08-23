# COOLBOY12 — REVOLVING RESOLUTION NOTE

## Status

| | |
|---|---|
| Record | Build-governance resolution note |
| Authority | **NONE** |
| Canonical | **NO** |
| Record Model | n/a |
| Source-of-truth class | DEV-ENV (non-authoritative) |
| Roadmap artifact | **none** — this is not a numbered artifact of the 490-artifact manifest |
| Build state at issue | Artifact 001 complete · Artifact 002 complete · Artifact 003 not started |
| Primary findings | **6** — CONFLICT-A · CONFLICT-B · GAP-C · GAP-D · GAP-E.3 · GAP-F |
| Sub-resolution | **GAP-D.1**, under GAP-D |
| Open items | **none** |
| Revolving | Yes. Superseded by any formal amendment to Blueprint, RMS or Roadmap |

> **Placement note.** This file sits in `docs/conventions/` because that is the smallest
> existing location holding build-process conventions (artifact, phase, role, restart,
> rebuild). No new namespace was created for it. Roadmap PART I classes `docs/**` as
> AUTHORITATIVE (specification); this note is **not** a specification and carries no
> authority — the Status table above governs, not the directory default.

---

## Purpose

Record the four findings raised during Artifacts 001 and 002, and the build resolution
adopted for each, so that implementation can continue without any of them being decided
silently inside an artifact.

This note is a build-governance record only. It is **not** a replacement Blueprint, a
replacement RMS, a replacement Roadmap, a Record Model, canonical data, or a constitutional
amendment.

---

## Authority

```
Blueprint                 Level 1 — master architectural authority
   ↓
RMS v1.0                  Level 2 — Record Model authority
   ↓
Roadmap (REPAIRED)        Level 3 — build execution authority
   ↓
Revolving Resolution Note Level 4 — this file. Authority NONE
   ↓
Implementation
```

A resolution here binds the current implementation path and nothing above it. Where this
note and any of the three sources differ, the source governs and this note is wrong.

---

## Current Build State

Verified against the working tree, not from prior context.

| Item | Verified state |
|---|---|
| HEAD | `dfb641c` Record GAP-E.3 — pyproject implementation decisions |
| Artifacts complete | 001 · 002 · 003 · 004 · 005 · **006 COMPLETE / PASS** |
| Next artifact | **007 — NOT CREATED** |
| Working tree | clean |
| Tracked files | 72 |
| Directories | 68, matching Roadmap PART I exactly |
| Purpose-file coverage | 68 / 68 directories |
| Purpose-file name in tree | **`PURPOSE.md`** (uppercase) × 68 · lowercase `purpose.md` × 0 · `purpose.txt` × 0 |
| `README.md` | present at repository root |
| Canonical records | **0** |
| Pre-existing decision / resolution notes | none |

---

## Resolution Register

**Primary resolution entries: 6** — CONFLICT-A · CONFLICT-B · GAP-C · GAP-D · GAP-E.3 · GAP-F.
**Sub-resolution: GAP-D.1**, which sits under GAP-D and is *not* a sixth primary finding: it
settles the naming of the purpose file GAP-D introduced and has no standing apart from GAP-D.

GAP-E.3 carries three lettered parts (a, b, c) because one source silence produced three
separate packaging decisions.

| ID | Finding | Resolution | Status | Constitutional Change |
|---|---|---|---|---|
| **CONFLICT-A** | RMS P=13 vs roadmap VERDICT / P14 | P=13 frozen baseline; VERDICT is a provisional roadmap extension | **RESOLVED FOR BUILD** | None |
| **CONFLICT-B** | 25 vs 27 metadata fields | use the 25 explicitly enumerated fields | **RESOLVED FOR BUILD** | None |
| **GAP-C** | missing requirement register | build not blocked; requirement text not verified | **NON-BLOCKING — UNVERIFIED** | None |
| **GAP-D** | purpose-file convention | every directory carries a purpose file | **RESOLVED** | None |
| **GAP-E.3** | unsourced pyproject values | implementation-level resolution for Python requirement, backend, version | **RESOLVED FOR BUILD** | None |
| **GAP-F** | no dependency-lock mechanism named by any source | `uv` selected by author ruling; `uv.lock` is the single canonical lockfile | **RESOLVED FOR BUILD** | None |
| **GAP-D.1** *(sub-resolution of GAP-D)* | purpose-file **name case** — an instruction said `purpose.md`, the tree holds `PURPOSE.md` | author ruled: keep `PURPOSE.md`; no file renamed, none existed to rename | **RESOLVED** | None |

---

### CONFLICT-A — P Kind Count

**Source position 1 — RMS v1.0 (Level 2).**
§9.1: *"Final Kind taxonomy — CLOSED at thirteen `FROZEN`."* §13: *"Final counts: W 7+1 · E 7
· **P 13** · R 14 · V 3 · I 5 = 50 Kinds across six models."* Appendix A repeats 13, marked
FROZEN.

**Source position 2 — Roadmap REPAIRED (Level 3).**
Artifact 405 (`docs/models/production/kinds/verdict.md`): *"this is the **fourteenth P Kind**,
admitted here with rationale."* PART XIV G-STATIC checklist: *"Kind consistency: … **P 14
(13 RMS-frozen + VERDICT)** …"* Supporting artifacts: 398 Verdict Format specification, 399
VERDICT Kind-Definition, 406 VERDICT schema. All sit in P15.

Both statements are recorded as written. Neither is edited.

**Build resolution.**

```
P = 13 RMS-frozen baseline
  + VERDICT = roadmap-level P extension (provisional)
```

Consequences, stated so they cannot be assumed:

- RMS is **not** modified.
- It is **not** claimed that RMS contains P14. RMS contains 13.
- VERDICT is **not** removed from roadmap work. Artifacts 398, 399, 405 and 406 stand.
- VERDICT is **not** described as constitutionally frozen. It is provisional.
- VERDICT is **not** treated as a fourth source-defined authority.

**Reason.** The Blueprint/Roadmap development path provides the implementation route for the
proposed and developing Production taxonomy, while RMS remains the frozen constitutional
baseline until formal Kind admission or amendment under RMS §13.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### CONFLICT-B — Metadata Field Count

**The inconsistency.** The Roadmap states the artifact-metadata cardinality two ways:

- §0.4: *"Every manifest entry carries all **27** fields of §54 in this notation."*
- Artifact 003 `Val`: *"**27-field** metadata set fixed."*
- PART IV header: *"Every artifact states all **25** fields explicitly."*

**The enumerated set contains 25 fields:**

```
 1 ID        6 T        11 CD       16 H       21 Val
 2 Name      7 R        12 Ph/St    17 S       22 Done
 3 path      8 SoT      13 Req      18 LS      23 Why
 4 Own       9 Auth     14 BP       19 G       24 Risk
 5 RM       10 Canon    15 RMS      20 →       25 ∥
```

No source in the available set identifies two additional fields. The §54 and §50 references
in §0.1 and §0.4 point to a generation brief that is not part of the three authoritative
documents, and no fourth authority is admitted.

**Build resolution.**

```
WORKING METADATA SET = the 25 explicitly enumerated fields
```

- Fields 26 and 27 are **not** invented.
- The "27" statement is treated as a **roadmap cardinality inconsistency**, recorded here.
- Artifact 003 will formalize and freeze the metadata convention. This note supplies its
  working input, not its final decision.

**Status:** RESOLVED FOR BUILD · **Working cardinality:** 25 · **Constitutional change:** NONE

---

### GAP-C — Requirement Register · NON-BLOCKING — UNVERIFIED

The Roadmap assigns each artifact requirement IDs — Artifact 001 carries `Req: BR-98`,
Artifact 002 carries `Req: BR-02`, and the manifest cites `BR-01` through `BR-113` plus the
RMS requirement set. PART XVII places the full definitions in
`COOLBOY12_OS_FILE_BUILD_ROADMAP_DEFINITIVE_REQUIREMENT_MATRIX.md`, which is **not part of the
supplied source set**.

So: **the requirement ID is known; the authoritative document defining its full text is not
currently available.**

This is **not** an architecture conflict, and it is **not** a blocker. Nothing in the three
authoritative documents disagrees with anything else on this point — a referenced document is
simply absent. Artifacts 001, 002 and 003 are each independently supported by the Blueprint and
RMS sections their manifest entries cite, so the build proceeds.

**Two things must be held apart, and the status carries both:**

```
BUILD IS NOT BLOCKED          artifacts proceed on their Blueprint and RMS citations
        +
REQUIREMENT TEXT IS NOT       no BR-nnn definition has been read, so no artifact has
VERIFIED                      been verified against its requirement text
```

The register is **still unavailable**. This entry is therefore not closed and must not be read
as closed: it is a **standing verification dependency**, discharged only when the matrix is
supplied and each artifact's `Req:` citation is checked against it.

**Operational rule.**

- Preserve requirement IDs **exactly as written**. Never paraphrase or renumber.
- Do **not** invent requirement text.
- Do **not** claim verification against unavailable requirement text. An artifact may be
  verified against its Blueprint and RMS citations and against its own `Val` and `Done`
  conditions; its `Req:` citation is carried forward unverified and labelled as such.
- Treat the missing register as a documentation and verification gap, resolvable by supplying
  the matrix.

**Status:** NON-BLOCKING — UNVERIFIED · **Type:** INFORMATION / VERIFICATION GAP ·
**Constitutional change:** NONE

---

### GAP-D — Purpose File Convention

**The original gap.** Artifact 001's `Val` requires *"every dir has a purpose file"*, but the
term "purpose file" is defined nowhere in the Roadmap — it appears exactly once, inside that
`Val` string. Artifact 003, which would define such conventions, depends on 001 and so cannot
supply it.

**Resolved.** Every directory in the repository carries a purpose file. Coverage verified at
**68 / 68**. Each file states the directory's responsibility, its architectural role, what
belongs in it, and what does not, and each carries an explicit notice that it is structural
metadata only — not canonical data, not a Record, not an authority source, not world truth,
and not a semantic definition.

The convention is an Artifact 001 implementation convention, to be formally defined by
Artifact 003.

**Status:** RESOLVED · **Constitutional change:** NONE

#### GAP-D.1 — purpose-file name case · RESOLVED

A discrepancy was raised between an instruction and the repository:

| Source | Purpose-file name |
|---|---|
| GAP-D resolution issued before Artifact 001 | `PURPOSE.md` |
| Artifact 001 as built and committed (`bf2368e`) | `PURPOSE.md` × 68 |
| Instruction issued with the first draft of this note | `purpose.md` |

**Author ruling: keep `PURPOSE.md`.**

The convention is **`PURPOSE.md`**, uppercase. This matches the original GAP-D resolution and
Artifact 001 as built, so no change to the repository was required.

Verified at the time of the ruling, on a case-sensitive filesystem: 68 files named
byte-exactly `PURPOSE.md`, zero named `purpose.md`, and git's index tracking all 68 in
uppercase. The instruction to rename `purpose.md` to `PURPOSE.md` therefore had **no targets**
— it described a state the repository already held. **No file was renamed. Artifact 001 was
not modified.**

Artifact 003 formalizes `PURPOSE.md` as the purpose-file convention.


---

### GAP-E.3 — Unsourced pyproject Implementation Values

**The gap.** Artifact 005 (`pyproject.toml`) required three values that **no authoritative
source establishes**. Searched: Blueprint (including §9.5, the artifact's only BP citation),
RMS, Roadmap, Artifact 003, CLAUDE.md, and the repository.

The search result that governs all three: **the word "python" appears zero times in all three
authoritative documents**, and every occurrence of "wheel" in them is "flywheel". The sources
establish that the language is Python only indirectly, through `.py` paths in the Roadmap
manifest and through Artifact 005 being a `pyproject.toml` at all. They establish nothing
about its version, its packaging, or its release numbering.

Blueprint §9.5 turned out to describe the execution-environment layer — *"the environment runs
the system; it does not define it"* — and carries no packaging requirement. Blueprint §26.8
says only *"the language runtime and the audited external components of §26.3a."*

#### GAP-E.3.a — `requires-python`

**Value:** `requires-python = ">=3.11"`
**Classification:** `AUTHOR RULING`

*Superseded the original resolution, which omitted the field.* No source set establishes a
canonical project Python-version requirement — the word "python" appears in none of the three
authoritative documents — so this is a **ruling, not a derivation**, and it is not a Blueprint,
RMS or Roadmap fact.

**Why the omission could not stand.** Artifact 006 demonstrated that without a declared floor
the resolver takes one from whichever interpreter the environment offers. The same
`pyproject.toml` locked to `>=3.10`, `>=3.11`, `>=3.12` and `>=3.13` under four interpreters —
four different lockfiles from one input, which fails Artifact 006's `Val: deterministic
resolve` and the Blueprint's environment boundary, since the value came from the environment
rather than from the repository. Declaring the floor removes that dependence: the same input
now yields a byte-identical lockfile on every interpreter tested.

**Status: GAP-E.3.a — RESOLVED FOR BUILD** by author ruling. `>=3.11` is a lower bound, not a
statement that any particular interpreter is officially supported, and no new architectural
requirement is created.

#### GAP-E.3.b — build backend

**Value:** `OMITTED`
**Classification:** `NON-BLOCKING IMPLEMENTATION DECISION`

The source set does not establish a required build backend for Artifact 005. `[build-system]`
is therefore **not introduced merely from generic Python convention**. PEP 517's documented
fallback applies, and wheel and sdist build without the table, so the omission costs nothing
against `Done: builds`.

**No specific backend is architecturally required, and no build-system decision is created in
the Blueprint, the RMS, or the Roadmap.**

**Status: GAP-E.3.b — RESOLVED FOR BUILD.**

#### GAP-E.3.c — project version

**Value:** `version = "0.0.0"`
**Classification:** `AUTHOR RULING`

This is an **implementation choice**. It is explicitly:

- **not** a Blueprint fact;
- **not** an RMS fact;
- **not** a Roadmap fact;
- **not** derived from Blueprint v0.7.0;
- **not** derived from RMS v1.0.

The project's architecture documents carry their own document and version identities, but
those do not automatically define the Python distribution version. The author selected
`0.0.0` as the current package version for the greenfield build.

`[project]` must carry a version for the file to resolve or build, and no source supplies one.

**This value is not promoted into constitutional architecture.**

**Status: GAP-E.3.c — RESOLVED FOR BUILD.**

#### Combined

| Value | Current state | Classification | Architectural status |
|---|---|---|---|
| `requires-python` | `>=3.11` | author ruling | not architectural fact |
| build backend | omitted | non-blocking implementation decision | not defined by source |
| `version` | `0.0.0` | author ruling | not architectural fact |

**GAP-E.3 — Status: RESOLVED FOR BUILD — Constitutional change: NONE**

> These three values are implementation-level decisions required to complete the current
> `pyproject.toml`. They do not amend the Master Blueprint, RMS, or Roadmap. A future
> authoritative source may replace them.

They are not constitutional facts, not canonical facts, not Blueprint decisions, and not RMS
decisions. **GAP-E.3 does not create a new architectural authority source.**

#### Artifact 005 status

Recorded on the audited implementation, which `/pyproject.toml` still matches exactly:

| Check | Result |
|---|---|
| TOML | **PASS** |
| `requires-python` | intentionally omitted |
| build backend | intentionally omitted |
| `version` | `0.0.0` — author ruling |
| Scope | **PASS** |
| **Artifact 005** | **PASS** |

No runtime validation is claimed. No package installation success is claimed; installation was
not executed.

**On GAP-E.3.c.** The Blueprint's `Version | v0.7.0` is the version *of that document* — "architectural
supersession of v0.6.3". No source connects it to a package version, and the two are not
derived from one another. Blueprint version, RMS version, Roadmap version, repository version
and Python package version remain five separate things. `0.0.0` is an **author ruling**, not a
derivation, and it is consistent with the Blueprint's own record that *"Nothing in this system
has been implemented."*

**What remains open at source.** GAP-E.3.a is now settled by ruling; GAP-E.3.b remains resolved
*for the build* by omission. The underlying source silence stands in both cases — no
authoritative document has been amended. If a later artifact needs a named build backend,
artifact 007 (test runner configuration) is the first candidate, and the gap is decided there
rather than assumed from here.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### GAP-F — Dependency Lock Mechanism

**The gap.** Artifact 006 (`dependency lockfile`) requires a lock mechanism, and **no
authoritative source names one**. Searched: Blueprint, RMS, Roadmap, Artifact 003, CLAUDE.md,
Artifact 005 and the repository root. No mention of pip, poetry, uv, pdm, pipenv, conda or any
lock workflow. The Roadmap entry gives the path as `/` with no filename and no format. The only
`lockfile` occurrence in the sources is artifact 006's own name; all four `hatch` occurrences
in the Blueprint are "escape hatch".

`uv` and Poetry are both installed in the current container. **That is environment, not
repository configuration**, and selecting on that basis would breach Blueprint P-33 and §9.5 —
*the environment runs coolboy12; it does not define coolboy12*. The choice was therefore
referred rather than made.

**Author ruling: `uv`.** `uv.lock` at the repository root is the single canonical lockfile.

| | |
|---|---|
| Mechanism | `uv` |
| Lockfile | `/uv.lock`, generated by `uv lock` |
| Classification | **AUTHOR RULING** |
| Architectural status | **not an architectural fact** |

This is an implementation choice. It is not a Blueprint fact, not an RMS fact, and not a
Roadmap fact. **No dependency and no dependency tool acquires semantic authority over
coolboy12** — Blueprint P-31, *dependencies provide capability, never authority*. The lockfile
is `SoT: DEV-ENV` and carries no coolboy12 semantics.

**Standing note on scale.** Artifact 005 declares `dependencies = []`, so the lockfile records
the project itself and **zero third-party packages**. It is a valid, deterministic lock of an
empty dependency set. Integrity hashes will appear only when real dependencies are declared —
none are recorded now because none exist to record, not because integrity was skipped.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

## canon/** Handling

Verified state of `canon/**` as Artifact 001 built it:

| Path | Files present | Canonical Records / canonical data |
|---|---|---|
| `canon/` and its six partitions | 7 × `PURPOSE.md` | **0** |

`canon/**` is **not** literally empty of files, and is not required to be. It holds seven
purpose files and no canonical Records.

The distinction that governs, unchanged:

```
purpose file        = directory responsibility documentation
                      structural metadata · Authority NONE · not a Record

canonical record    = canonical data
                      minted only through the Mutation Coordinator, only after
                      that model's own canonical gate (G-CANON-W/E/P/V/I, G-REG)
```

So `canon/**` **contains no canonical Records and no canonical data at this stage**, which is
what Roadmap PART X requires before any canonical gate. The `PURPOSE.md` files inside those
directories are **structural documentation, not canonical Records and not canonical data** —
their presence does not populate the partition, and each states its own non-canonical status
in its own text.

The requirement is on canonical data, never on file count:

```
canon/** holds no canonical Record        <- the actual constraint
canon/** holds no file at all             <- NOT the constraint, and not the built state
```

**No new canon exception is introduced by this note. No canonical record is created by this
note.** The single pre-existing allowance — a purpose file inside `canon/**` — is the author's
GAP-D resolution and is not widened here.

---

## Artifact 001 Impact

| Check | Result |
|---|---|
| Artifact 001 | **COMPLETE** |
| Repository tree | **COMPLETE** — 68 directories, matching Roadmap PART I exactly |
| Purpose-file coverage | **COMPLETE** — 68 / 68 |
| Modified by this note | **No** |

One contradiction was discovered and reported rather than acted on — **GAP-D.1**, the
purpose-file name case. It has since been closed by author ruling in favour of the name
Artifact 001 already uses, so no change to Artifact 001 followed. No other contradiction was
found.

---

## Artifact 002 Impact

| Check | Result |
|---|---|
| Artifact 002 | **COMPLETE** |
| `README.md` at repository root | **Present** |
| Claims constitutional P14 | **No** — the README makes no P Kind count claim at all |
| Claims 27 metadata fields | **No** — no metadata field-count claim at all |
| Invents BR-98 meaning | **No** — no BR requirement text appears |
| Introduces COM terminology | **No** |
| Introduces a seventh model | **No** — exactly six |
| Modified by this note | **No** |

No contradiction found. Artifact 002 was not rewritten.

---

## Artifact 003 Readiness

**Artifact 003 is now unblocked.**

Its working input is the **25 explicitly enumerated metadata fields** recorded under
CONFLICT-B.

| | |
|---|---|
| Artifact | 003 · artifact + phase conventions · `docs/conventions/artifact_conventions.md` |
| Hard dependency | 001 — satisfied |
| Soft dependency | 002 — satisfied |
| Working metadata cardinality | 25 |
| Created by this note | **No** |

Artifact 003 formalizes and freezes the metadata convention; this note only supplies the
working cardinality so that 003 is not authored against a contradiction. Two items land on
003's desk: the 25-vs-27 reconciliation itself, and the GAP-D.1 purpose-file name once ruled.

---

## Non-Authority Notice

These resolutions:

- **govern the current implementation path**;
- **do not amend** the Blueprint;
- **do not amend** the Record Model System v1.0;
- **do not amend** the Roadmap;
- **may later be superseded** by a formal authoritative amendment.

No resolution in this note changes what is constitutionally true. Each records which reading
implementation proceeds under while a source-level inconsistency remains open. When a source
is amended, the corresponding entry here is retired, not reconciled — the source governs.

Nothing in this note is canonical. Nothing in this note carries authority. It is a record of
decisions taken to keep the build moving, and it revolves.
