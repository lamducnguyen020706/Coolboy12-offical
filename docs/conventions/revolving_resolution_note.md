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
| Primary findings | **13** — CONFLICT-A · CONFLICT-B · CONFLICT-C · GAP-C · GAP-D · GAP-E.3 · GAP-F · GAP-G · GAP-H · GAP-I · GAP-J · GAP-K · GAP-L |
| Sub-resolution | **GAP-D.1**, under GAP-D |
| Open items | **CONFLICT-C** — SoT class count, unresolved at source; non-blocking for 016/017/020, potentially blocking for 050. **GAP-L** — progress-sync system's Roadmap standing, unresolved, disclosed not resolved |
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
| HEAD | `1c2efed` Record UserPromptSubmit activity from live Claude Code session |
| Artifacts complete | 001 … 021 · **022 RE-FROZEN** (`.claude/hooks/canon_deny.py`, canon write-deny hook; CONFLICT-D amendment) · **023** (`.claude/hooks/zones.json`, zone configuration) · **024** (`.claude/settings.json`, hook registration) |
| Next artifact | **025 — NOT CREATED** (`propose` command, `.claude/commands/propose.md`, `H: 024`) |
| Artifact 024 registration | **LIVE** — `PreToolUse`, `matcher: ""`, invoking `canon_deny.py`. Verified in-session: a canonical write denies, `pytest`/`git`/`ruff`/`sed` run |
| Working tree | clean apart from `reports/**` hook telemetry |
| Tracked files | 136 |
| Directories | 81 tracked — 68 matching Roadmap PART I exactly, plus `docs/sources/` (GAP-K) and 12 carrying the GAP-L progress-sync system |
| Purpose-file coverage | 69 / 69 Roadmap-governed directories (the 12 GAP-L directories carry none and are not PART I directories) |
| Purpose-file name in tree | **`PURPOSE.md`** (uppercase) × 69 · lowercase `purpose.md` × 0 · `purpose.txt` × 0 |
| `README.md` | present at repository root |
| Canonical records | **0** |
| Pre-existing decision / resolution notes | none |

---

## Resolution Register

**Primary resolution entries: 14** — CONFLICT-A · CONFLICT-B · CONFLICT-C · CONFLICT-D · GAP-C · GAP-D · GAP-E.3 · GAP-F · GAP-G · GAP-H · GAP-I · GAP-J · GAP-K · GAP-L.
**Sub-resolution: GAP-D.1**, which sits under GAP-D and is *not* a sixth primary finding: it
settles the naming of the purpose file GAP-D introduced and has no standing apart from GAP-D.

GAP-E.3 carries three lettered parts (a, b, c) because one source silence produced three
separate packaging decisions.

| ID | Finding | Resolution | Status | Constitutional Change |
|---|---|---|---|---|
| **CONFLICT-A** | RMS P=13 vs roadmap VERDICT / P14 | P=13 frozen baseline; VERDICT is a provisional roadmap extension | **RESOLVED FOR BUILD** | None |
| **CONFLICT-B** | 25 vs 27 metadata fields | use the 25 explicitly enumerated fields | **RESOLVED FOR BUILD** | None |
| **CONFLICT-C** | Blueprint/RMS state **five** SoT classes (§29.6a); Roadmap PART VII states **six**, adding DEV-ENV | recorded, not resolved — the two tables classify different objects (data classes vs repository artifact classes); DEV-ENV is Roadmap-only | **RECORDED — UNRESOLVED AT SOURCE** | None |
| **CONFLICT-D** | Artifact 022's unconditional `OPAQUE` deny cannot coexist with Artifact 024 registering it at `PreToolUse` across Bash | Route 3 approved by the author: 022 unfrozen under control, decision axis moved from command provability to canonical reachability, re-frozen | **RESOLVED FOR BUILD · AUTHORIAL RULING — SOURCE UNCHANGED** | None |
| **GAP-C** | missing requirement register | build not blocked; requirement text not verified | **NON-BLOCKING — UNVERIFIED** | None |
| **GAP-D** | purpose-file convention | every directory carries a purpose file | **RESOLVED** | None |
| **GAP-E.3** | unsourced pyproject values | implementation-level resolution for Python requirement, backend, version | **RESOLVED FOR BUILD** | None |
| **GAP-F** | no dependency-lock mechanism named by any source | `uv` selected by author ruling; `uv.lock` is the single canonical lockfile | **RESOLVED FOR BUILD** | None |
| **GAP-G** | no test runner named by any source | `pytest` selected by author ruling; configured in `pyproject.toml` | **RESOLVED FOR BUILD** | None |
| **GAP-H** | no linter or formatter named by any source | `ruff` selected by author ruling, one tool for both roles | **RESOLVED FOR BUILD** | None |
| **GAP-I** | no editor named by any source | EditorConfig chosen as the editor-agnostic mechanism; no editor made a project requirement | **RESOLVED FOR BUILD** | None |
| **GAP-J** | Artifact 010's exit condition already satisfied by Artifact 001 | roadmap overlap recorded; 010 verified rather than rebuilt, zero repository delta | **RESOLVED FOR BUILD** | None |
| **GAP-K** | no source names a repository location for the three source documents themselves | author-decided: `docs/sources/`, exact unmodified copies, MD5-verified | **RESOLVED FOR BUILD** | None |
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

### CONFLICT-C — Source-of-Truth Class Count

**The finding.** The three authoritative documents do not agree on how many source-of-truth
classes exist.

| Source | Statement | Count |
|---|---|---|
| Blueprint §29.6a | table of AUTHORITATIVE · DERIVED · CACHED · TEMPORARY · EXTERNAL, scoped to *"Every **data class** in the system"* | **five** |
| Blueprint §7 change register | *"Five classes; every external store is DERIVED or CACHED"* — marked **Frozen** | **five** |
| Blueprint §13 capability table | *"Assigns one of five classes (§29.6a)"* | **five** |
| RMS §4 | row reads: Source-of-truth classification · *"§29.6a — five classes"* · Constitutional | **five** |
| Roadmap PART VII | table headed *"**Artifact class**"*, adding **DEV-ENV** for `src/**`, `tests/**`, `benchmarks/**`, `.claude/**` | **six** |
| Roadmap row 016 | `Val: six SoT classes; every directory classified` | **six** |

**Verified by search.** The string `DEV-ENV` occurs **zero times in the Master Blueprint** and
**zero times in the RMS**. It is a Roadmap-only class.

**Affected artifacts.** 016 (this finding's origin) · 017 · 020 · 050 · Roadmap PART VII and
PART I · every later artifact carrying a `SoT:` field, since `SoT: DEV-ENV` appears throughout
the manifest.

**Architectural consequence.** If DEV-ENV were admitted as a *record-level* `sot_class` value,
it would extend a scheme the Blueprint and RMS both record as frozen at five, and RMS §4 carries
`sot_class` among the seven FROZEN universal envelope fields. If it is confined to *repository
artifact* classification, no Blueprint statement is contradicted, because §29.6a scopes itself
to data classes and PART VII's own column header is *Artifact class*.

**Why this is recorded and not decided.** The two-level reading is textually available — the
sources literally classify different objects — but it is an inference, and the source-precedence
rule (Blueprint > RMS > Roadmap) would otherwise put a frozen five-class Blueprint scheme against
a six-class Roadmap Val. **No session may resolve this by choosing an interpretation.** It needs
an authorial ruling or a source amendment.

**What Artifact 016 did with it.** 016 classifies repository directories using the Roadmap's six,
because its own Val and Done are directory-scoped and PART VII is the Roadmap's own normative
table. It states the split explicitly in its §2, labels DEV-ENV as Roadmap-only with no Blueprint
basis, and explicitly declines to decide whether DEV-ENV is admissible as a record-level class —
routing that question to Artifact 050 and to this entry.

**Build impact.** Not blocking for 016, 017, or 020, all of which are directory-scoped.
**Potentially blocking for Artifact 050**, whose `Val` is *"every record carries exactly one
class"* against `BP: §29.6a` — the five-class table. 050 will have to know whether DEV-ENV is a
legal record-level value.

**Status:** RECORDED — UNRESOLVED AT SOURCE · **Constitutional change:** NONE

---

### CONFLICT-D — Artifact 022's Deny-On-Opacity vs Artifact 024's Registration

**The finding.** Artifact 022 classifies every Bash command as `READ_ONLY`, `SIMPLE_MUTATION`, or
`OPAQUE`, and denies the `OPAQUE` class unconditionally — opacity is itself grounds for denial.
That policy is correct and was hardened deliberately across four rounds. Artifact 024's job is to
register that hook at `PreToolUse`. The two cannot both hold across Bash: `python`, `pytest`,
`git add`, `git commit`, `git push`, `git branch`, `sed`, `make`, and `npm` are all `OPAQUE`, so
registering the hook across Bash denies the repository's own test, lint, and commit path.

**Demonstrated, not predicted.** The registration was applied during the Artifact 024 build and
took effect mid-session — Claude Code re-reads `.claude/settings.json` per tool call, proven
because reverting the file restored Bash immediately. While it was active:

| Command | Result |
|---|---|
| `.venv/bin/python -m pytest …` | **DENIED** |
| `sed -n '…p' <file>` | **DENIED** |
| `git branch --show-current` | **DENIED** |
| `git status` · `git log` · `git diff` · `cat` · `grep` | allowed |

**Why this blocks the artifact rather than merely inconveniencing it.** Roadmap row 024 declares
`Val: hooks registered` and `Done: active`. Establishing either by execution requires a test
runner, and the registration denies the test runner. Artifact 024 cannot evidence its own exit
condition while it is in force. Artifacts 025–028, which row 024 unlocks, inherit the same block.

**The source tension.** Blueprint I-83: *"Execution-substrate guard rails are defence-in-depth,
never constitutional authority."* Registered across Bash, the guard stops being defence-in-depth
and becomes the primary control over the shell — roughly thirty read-only commands plus seven
mutators is the whole remaining surface. Roadmap row 024 also carries `Auth: none`, so 024 is not
the place to resolve this by narrowing what 022 enforces.

**What was done about it.** Nothing was registered. `.claude/settings.json` is at its pre-024
baseline, carrying only the GAP-L `UserPromptSubmit` hook. Artifact 022 was not modified — it is
frozen, and the fix, if any, is a source-level decision rather than an implementation patch.

**What is verified and what is not.** A matcher scoped to `Write|Edit|MultiEdit|NotebookEdit` was
observed to *exclude* Bash. Whether it correctly *selects* those four tools, rather than selecting
nothing, is **unverified** — proving it needs either a write into `canon/**` or a Bash-scoped
matcher probe, and neither was authorised. Any future session choosing that route must establish
inclusion before treating the boundary as enforced.

**Adjacent defect, patched under the same unfreeze.** Artifact 022's `_SEGMENT_SPLIT` split on `|`
without respecting quoting, so `grep -e 'a\|b'` — a pipe inside quotes — was misclassified
`OPAQUE` and denied. A false-positive denial, not a bypass.

---

#### Resolution

**SOURCE FACT.** Blueprint §26.8 scopes the boundary by **path**: *"a hook that denies direct
writes to **those paths** is the deterministic expression of Spine law 2."* The same section lists
command execution *including tests* among the facilities the environment legitimately provides,
and states that derived stores and proposals are **freely writable**. Searched across all three
sources, *opaque* never appears as a command policy — the Blueprint's two hits concern opaque
*data stores* (AC-4), the Roadmap's four are `RULE G3` adapter *shells*, and the RMS has none.
`OPAQUE → DENY` was therefore an implementation hardening decision, never a source requirement,
and it denied three things §26.8 explicitly grants.

**AUTHORIAL RULING.** Route 3 approved: controlled unfreeze of Artifact 022 to move the decision
axis from *command provability* to *canonical reachability*, then re-freeze. Routes 1 and 2 were
rejected — Route 1 denies granted facilities and its "run tooling outside Claude Code" escape
hatch is itself unguarded; Route 2 was **experimentally disproven**, a fabricated canonical Record
was written into `canon/world/` through Bash in an isolated sandbox while the hook was never
invoked.

**Matcher inclusion — now PROVEN.** This entry previously recorded it unproven. An isolated probe
project with a harmless logging hook, driven by the `claude` CLI, resolved it: with
`matcher: "Write|Edit|MultiEdit|NotebookEdit"` the probe logged `Write` only; with `matcher: ""`
the same prompt and tools logged `Write` **and** `Bash`. Alternation matcher syntax is supported
and selects by exact tool name, and the control proves Bash can fire `PreToolUse`.

**IMPLEMENTATION CONSEQUENCE.** Artifact 022 now denies an identifiable write into `canon/**` from
any tool — redirects, the seven mutators, write-producing options, a canonical working directory,
resolvable variables expanding into canon, and opaque commands that name a canonical path. Opacity
alone no longer denies, so `pytest`, `git`, `ruff`, `make` and `sed -n` run. The quoted-pipe
defect is fixed by a quote-aware splitter that is not a shell parser. Suite: 158 tests, all
passing.

**Residual risk — stated, not solved.** *(Revised by the Route-3 cleanup patch; the earlier
wording described an interim implementation.)* A path counts as a write target only from its
**shell-level position** — a redirect destination, a mutator's positional argument, the value of
a modelled write-producing option, a bare positional word of an opaque command, or any of those
resolved against a working directory inside canon. A path inside a **quoted** argument is not
inspected. The consequence is stated plainly rather than hidden: an interpreter one-liner can
write into canon unseen, and this now includes the **literal**-path form
`python3 -c "open('canon/world/f.md','w').write('x')"`, not only the computed
`os.environ['CANON']` form. Separating that from `python3 -c "print('canon/world/x.md')"`
requires interpreting the program, which Artifact 022 must not do.

That is a real reduction in depth against a determined actor with shell access, accepted because
I-83 and I-100 already scope it — *"execution-substrate guard rails are defence-in-depth, never
constitutional authority"* — with the constitutional guarantee remaining artifact 152 plus the
Human Gate. Every shell-level form of the same write stays denied, including `sed -i`, `dd of=`,
`chmod`, `install`, `ln`, `truncate`, `cp -t`, `sort -o` and `git diff --output=`.

**The over-denial recorded here earlier is fixed, not surviving.** It was that any canonical path
anywhere in a command string denied — `git commit -m "… canon/world"` denied on its own message,
which blocked the Artifact 024 commit. Quote-aware tokenisation now keeps a quoted message whole,
so it is no longer read as a bare path argument. The note that only `git commit -F <file>` worked
around it, and the observation that a heredoc does **not** (the Bash tool submits the whole
command string, heredoc body included), are both retained here as history; neither is now a live
constraint. Artifact 022's docstring sentence stating that constraint was removed in the same
patch.

**Standing.** Artifact 022 is **RE-FROZEN**. Artifact 024 **remains deferred** — nothing is
registered, and `.claude/settings.json` is still at its pre-024 baseline. The source was not
amended; the implementation was brought into line with it.

**Status:** RESOLVED FOR BUILD · AUTHORIAL RULING — SOURCE UNCHANGED · **Constitutional change:**
NONE

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

#### GAP-C.1 — `Req:` on row 030 is a citation, not a gating obligation · AUTHORIAL RULING

**What happened.** Artifact 030's first implementation read row 030's `Req: BR-01…BR-07` as
seven requirements the exit-P0 gate must *prove*, and failed the gate while BR-03 and BR-05
lacked a P0 carrier. BR-03 is carried by no Roadmap row at all; BR-05's only carrier is
artifact 062, in P3.

**Why that was wrong.** Every row's `Req:` is that artifact's own citation — row 022's
`Req: BR-07` does not mean 022 gates BR-07 — and row 030's `Val`, which states what 030
validates, names *tree, boundaries, hooks, 108-register present* plus a fifth clause requiring
that current architecture carry none of the retired object-model vocabulary. It names no
requirement at all. Treating the range as a gating obligation invented a requirement the
Roadmap never states, which is precisely what GAP-C's operational rule forbids.

**Ruling (author, this session).** All seven citations on row 030 are carried forward
unverified and labelled, exactly as GAP-C already directs for every `Req:` in the build.
Artifact 030 gates its `Val`. BR-03 and BR-05 are not P0 obligations and do not block exit-P0.

**What this does not do.** It invents no text for BR-03 or BR-05, closes nothing, and changes
no source document. GAP-C remains open and unverified for all 113 requirements; this only
settles how row 030's own citation is read. The verification dependency is still discharged
only by supplying the requirement matrix.

**Retained.** The principle that an unavailable check is never a pass survives where it
belongs: Artifact 030 records any check *it owns* and cannot run, and fails the gate on it,
because a pytest skip does not change an exit status.

**Status:** RESOLVED FOR BUILD · **Type:** READING OF AN EXISTING FIELD ·
**Constitutional change:** NONE · **Supersedes:** nothing — refines GAP-C's application

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

**Status: GAP-E.3.b — RESOLVED FOR BUILD, and now confirmed by execution.**

**Confirmed at Artifact 021.** Artifact 021 is the first artifact to place importable Python in
`src/**`, so it is the first that could test the omission rather than reason about it. It was
tested: `uv pip install -e .` against the repository's `.venv` resolved, built, and installed
`coolboy12==0.0.0`, and `from coolboy12.bootstrap.config import load_config` then succeeded. PEP
517's fallback plus Artifact 005's existing `[tool.setuptools.packages.find]` is sufficient, and
no `[build-system]` table was added. The prediction recorded here held; the omission cost
nothing.

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

### GAP-G — Test Runner

**The gap.** Artifact 007 (`test runner configuration`) requires a runner, and **no
authoritative source names one**. Searched Blueprint, RMS, Roadmap, Artifact 003, CLAUDE.md and
the repository for pytest, unittest, nose, nox and tox: the single `test runner` occurrence in
all three documents is artifact 007's own manifest name.

One weak signal exists and is recorded as **INFERENCE, not evidence**: artifact 007's
`Val: collects zero tests without error` uses *collect*, which is pytest's term for the
discovery phase. That is suggestive; it is not a naming.

**Author ruling: `pytest`.**

| | |
|---|---|
| Runner | `pytest` |
| Declared at | `[dependency-groups] dev = ["pytest"]` in `/pyproject.toml` |
| Configured at | `[tool.pytest.ini_options] testpaths = ["tests"]` |
| Classification | **AUTHOR RULING** |
| Architectural status | **not an architectural fact** |

**Boundary.** pytest is DEV-ENV tooling under Blueprint §9.5 and P-33 — the environment runs
coolboy12 and does not define it. Under P-31, *dependencies provide capability, never
authority*: the runner may execute a validator and report that a check failed, but it does not
define validity, and it is never a Canon, Registry, Record Model or mutation authority.

**Two deliberate restraints.**

- **No version floor is declared.** `pytest` is unconstrained in `pyproject.toml` so that
  Artifact 006 (`uv.lock`) does the pinning — currently `pytest 9.1.1`. Declaring a floor here
  would invent a second unsourced value alongside GAP-E.3.a.
- **Runtime dependencies stay empty.** pytest sits in a dev dependency group, so
  `[project].dependencies` remains `[]` exactly as Artifact 005 declares it.

**On the exit code.** With no test suite yet, pytest exits **5**, its dedicated
`NO TESTS COLLECTED` status. That is not an error and is not suppressed: configuration error is
4, collection error is 2, internal error is 3, and a failing test is 1. All four were
demonstrated separately, and 5 is reachable only by zero-collected. Artifact 007's
`Val: collects zero tests without error` is therefore met by a runner that starts, reads its
config, discovers the declared root, and reports zero — not by a placeholder test or a wrapper
masking a failure.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### GAP-H — Linter / Formatter

**The gap.** Artifact 008 requires a linter and a formatter, and **no authoritative source
names either**. Searched Blueprint, RMS, Roadmap, Artifact 003, CLAUDE.md and the repository
for ruff, black, flake8, isort, pylint, mypy, pyright, yapf and autopep8: **zero occurrences
across all three documents**.

**Author ruling: `ruff`.** One tool covering both roles, so no second competing linter or
formatter is introduced. Declared at `[dependency-groups] dev = ["pytest", "ruff"]`, configured
at `[tool.ruff]` in `/pyproject.toml`. Resolved version `ruff 0.16.4`, pinned by Artifact 006.

| | |
|---|---|
| Linter and formatter | `ruff` |
| Classification | **AUTHOR RULING** |
| Architectural status | **not an architectural fact** |

#### The word "linter" means two different things — do not conflate them

This is the collision most likely to cause a later error, so it is recorded explicitly.

| | Blueprint's linter | Artifact 008's linter |
|---|---|---|
| What it is | a **coolboy12 structural-validation mechanism** | a **Python code-quality tool** |
| Source | Blueprint §12 — *"Linter findings block. The linter is deliberately dumb and deliberately fast"*; everything requiring interpretation goes to Governance (P-24) | no source; author ruling |
| What it decides | whether a structurally decidable violation blocks — unaxised temporal claims (P-21), missing basis state (P-22), empty anchor transformation (P-29) | unused imports, whitespace, line length |
| Owned by | the **P4 validation artifacts (125–144)** | DEV-ENV tooling, Artifact 008 |

**ruff must never be made to implement the Blueprint's linter.** Under P-31, *dependencies
provide capability, never authority*: ruff can report an unused variable; it cannot decide that
a Record is canonical, that a fact is true, or that a mutation is authorized.

#### Three values deliberately not set

Each would have duplicated something that already exists, creating a drift hazard:

| Not set | Why | Verified |
|---|---|---|
| `target-version` | ruff derives it from `[project].requires-python` | ruff reports `target_version = 3.11`, matching Artifact 005 |
| version floor | Artifact 006 pins the concrete version | `ruff 0.16.4` in `uv.lock` |
| exclusions | ruff's defaults already cover `.venv`, `.git`, `__pycache__`, `build`, `dist` | confirmed in ruff's resolved `file_resolver.exclude` |

Rule selection is ruff's default set — **413 rules enabled**, not a disabled-everything
configuration. The clean result comes from the repository containing **zero `.py` files**, not
from suppression.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### GAP-I — Editor / Tooling

**The gap.** Artifact 009 requires editor/tooling configuration, and **no authoritative source
names an editor**. Searched Blueprint, RMS, Roadmap, Artifact 003, CLAUDE.md and the repository
for VS Code, Visual Studio, PyCharm, IntelliJ, JetBrains, Vim, Neovim, Emacs, Sublime and
EditorConfig: **zero occurrences across all three documents**. The repository contained no
`.vscode/`, no `.idea/`, no `.editorconfig` and no workspace file.

**Resolution: EditorConfig, one file — `/.editorconfig`.**

Chosen because it is **editor-agnostic**. A `.vscode/` directory would have made VS Code a de
facto project requirement on no evidence; EditorConfig reduces drift without naming an editor
at all. Recorded as a **TECHNICAL IMPLEMENTATION DECISION**, not an architectural fact.

#### The word "Editor" means two different things — do not conflate them

The second such collision in this build, after GAP-H's "linter".

| | Blueprint's Editor | Artifact 009's editor |
|---|---|---|
| What it is | the **Editor-in-Chief**, an AI coworker role | a **text editor** |
| Source | Blueprint §21 — *"The Editor-in-Chief recommends what to tell and when"* | no source; implementation decision |
| What it decides | what is worth telling, in what form, at what time | indentation and newlines |
| Owned by | the **P16 coworker artifacts** | DEV-ENV, Artifact 009 |

#### Every value measured, none invented

Artifact 008 owns lint and format policy; Artifact 009 mirrors it and defines nothing. The two
Python settings were read from ruff's own resolved settings and verified equal:

| `.editorconfig` | ruff | Match |
|---|---|---|
| `indent_size = 4` | `formatter.indent_width = 4` | yes |
| `max_line_length = 88` | `formatter.line_width = 88` | yes |
| `indent_style = space` | `formatter.indent_style = space` | yes |

The generic settings — `charset`, `end_of_line`, `insert_final_newline`,
`trim_trailing_whitespace`, `indent_style` — describe conventions **all 74 tracked files
already follow**: zero CRLF, zero missing final newlines, zero trailing whitespace, zero
tab-indented files, zero non-UTF-8. Adopting the file changed nothing.

**Coupling note.** `indent_size` and `max_line_length` duplicate Artifact 008, because no editor
derives them from ruff. If 008's formatter policy is ever changed, this file must change with
it. That duplication is the artifact's purpose, not an oversight — unlike GAP-H's
`target-version`, which ruff derives and which was therefore deliberately *not* duplicated.

**Replaceability, per Blueprint §9.5.** Verified by removing the file: `ruff check`,
`ruff format --check` and `pytest` returned identical results with and without it. It governs
nothing and coolboy12's architecture is unchanged by its absence.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### GAP-J — Artifact 010 Overlaps Artifact 001

**The finding.** Artifact 010 (`test suite scaffolding`) required **no new files**. Its exit
condition —
*"constitutional/unit/integration/negative/boundary/lockstep/conformance exist"* — was already
satisfied, correctly and by roadmap mandate, when Artifact 001 was built.

**Why this is an overlap and not an error.** Roadmap PART I line 83 lists
`tests/{constitutional,unit,integration,negative,boundary,lockstep,conformance}/` as part of the
repository tree, and Artifact 001's Val is *"tree matches PART I; every dir has a purpose file"*.
Artifact 001 was therefore **required** to create all seven, and did. Artifact 010 names the same
seven directories as its own exit condition. Both entries are internally correct; the roadmap
simply assigns the same seven directories twice.

**Resolution: verify, do not rebuild.** Per the artifact brief — *"do not blindly recreate seven
existing directories if they already exist"* — Artifact 010 was executed as a verification pass.
Nothing was created, renamed, duplicated or deleted. **Repository delta: zero.**

Artifact 010's remaining obligation was its Val, *"seven suites discoverable"*, which is a
verification duty. It was discharged: pytest accepts each of the seven individually (exit 5,
no tests collected — not exit 4 config error or exit 2 collection error), and a scratch mirror
with one probe per suite collected 7/7.

#### Downstream constraint discovered — unique test-file basenames

Recorded because it will bite Artifact 011 onward.

The suite directories are **not Python packages** — no `__init__.py`, correctly, since none is
required by pytest and none is mandated by any source. Under pytest's default import mode this
means **test files in different suites must have unique basenames**.

Demonstrated in scratch:

| Probe naming | Result |
|---|---|
| `test_probe.py` in all seven suites | **6 collection errors**, 1 collected |
| `test_probe_<suite>.py`, unique per suite | **7 collected, 0 errors** |

This is a property of the scaffold as the sources require it to be, not a defect. It is **not
resolved here**, because the two available remedies — adding `__init__.py` to each suite, or
changing pytest's import mode — are both outside Artifact 010's scope and neither is required
by any source. It becomes actionable when real test files appear.

Artifact 011's `harness.py` is unaffected: it is not a `test_*.py` file and is not collected.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### GAP-K — Source Document Repository Placement

**The finding.** No Blueprint, RMS, or Roadmap section specifies a repository location for the
three authoritative source documents themselves. They are external inputs to the build, not
artifacts in the 490-artifact manifest, and every artifact built so far has cited them from a
session-external upload path rather than an in-repository one.

**The request.** The author asked to commit the Master Blueprint, the Record Model System, and
the OS File Build Roadmap into the repository, without specifying a location.

**The resolution.** Author-decided: `docs/sources/`, holding exact, unmodified copies of the
three documents under their original filenames —
`COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md` · `COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md` ·
`COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`. Byte-identity to the uploaded originals verified
by MD5 before commit.

**Why this location.** `docs/**` is already the AUTHORITATIVE (specification) zone (PART I).
`docs/constitution/` was considered and rejected: its own `PURPOSE.md` scopes it to *"the Record
System constitution and the Bootstrap Meta-Contract"*, introduced at Artifact 031 (P1), and its
"what does not belong here" list already excludes anything that isn't that constitutional
artifact. `docs/sources/` is a new subdirectory, not a new top-level namespace, named for exactly
what it holds.

**What this is not.** Not a new Roadmap artifact — no artifact ID, no `H:`/`S:`/`G:` target, no
Val/Done criterion is attached to it. Not a change to authority order: Blueprint > RMS > Roadmap
> Artifact 003 > CLAUDE.md > Resolution Note is unchanged, and `docs/sources/` does not become a
fourth authority — it holds copies of the first three, unmodified. Not canonical data, not a
Record.

**Consequence for future sessions.** A session may now cite `docs/sources/<filename>` as a
stable in-repository path. If any of the three source documents is revised, the superseding copy
replaces the file here (`Delete: supersede only`) and this entry should be updated to name the
new revision.

**Status:** RESOLVED FOR BUILD · **Constitutional change:** NONE

---

### GAP-L — Progress-Sync System Arrived Outside the Artifact Process

**The finding.** Between the Artifact 021 patch and the Artifact 022 build, three commits
(`480584b`, `dfadd18`, `84272be`, later followed by `49458f4`, `bd50991`) landed on
`claude/coolboy12-build-31qwm0` from outside this session — pulled after an explicit
authorization check per commit, not authored here. They add: `.claude/settings.json`,
`.claude/hooks/coolboy12_prompt_log.py`, `.claude/commands/coolboy12-update.md`,
`.claude/skills/coolboy12-update/SKILL.md`, `docs/COOLBOY12_GPT_HARD_AUDIT_QUICKSTART.md`,
`reports/**` (`HTML_UPDATE_CONTRACT.md`, `progress.json`, `implement-log.json`,
`progressreport.html`), `scripts/update_progress.py`, `scripts/validate_progressreport.py`,
`tests/test_progress_report.py`, `tests/test_claude_code_integration.py`,
`tests/coolboy12-progress-sync/**`, and `.gitignore`.

**Why this is a finding, not silently absorbed.** None of these paths carries a Roadmap artifact
ID. `scripts/`, `reports/`, `.claude/hooks/`, `.claude/commands/`, and `.claude/skills/` are not
among the 68 Roadmap PART I directories. CLAUDE.md's artifact-first build discipline states that
new repository infrastructure enters through a numbered artifact off the Roadmap manifest, and
this system entered through direct commits instead.

**What was done about it.** Not reverted — the user authorized each pull after an explicit
sync-diagnosis exchange, and reverting authorized work is not this note's role. A full adversarial
audit was run against it (separately from the Artifact 022 work): one **CRITICAL** defect
(`scripts/update_progress.py` had a `SyntaxError` on this repository's own declared Python floor,
`>=3.11`, breaking the publisher and silently disabling the hook's completion-gate path) and one
**HIGH** defect (the completion gate accepted an *untracked* file as evidence, letting a single
prompt fabricate a completion with no commit) were found, fixed, and regression-tested. Both fixes
and the audit trail are recorded in git history, not in this note, since they patch code outside
any Roadmap artifact's scope.

**Standing rule for future sessions.** `.claude/hooks/coolboy12_prompt_log.py` is a live
`UserPromptSubmit` hook: it logs one activity event per prompt to `reports/implement-log.json` and
may advance `reports/progress.json`'s declared frontier only under a strict evidence gate (see the
audit trail in git history for what that gate now requires). **It has never advanced the frontier
in this repository** — every event recorded so far carries `completion_recorded: false` — and its
presence does not change how artifacts are built: the nine-phase artifact-first workflow in
CLAUDE.md remains the only route by which an artifact is built and accepted. `reports/**` is
descriptive telemetry about session activity, not an authority source, and is never cited as one.

**What this is not.** Not a fourth authority. Not a Roadmap artifact — no artifact ID is claimed
or should be assigned to it retroactively without an authorial ruling. Not a change to the
authority order.

**Open item.** Whether this system should be formally admitted to the Roadmap as one or more
numbered artifacts, relocated, or removed is an authorial decision this note does not make.
Flagged here so it is not mistaken for governed build output in a future session.

**Status:** DISCLOSED, NOT RESOLVED · **Constitutional change:** NONE

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
