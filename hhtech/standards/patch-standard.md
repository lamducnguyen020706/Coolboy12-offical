# HHTECH — COOLBOY12 Patch Standard

## Status and Authority

| Field | Value |
|---|---|
| Document | `hhtech/standards/patch-standard.md` |
| Kind | HHTECH-internal operational standard — **not** a COOLBOY12 Roadmap artifact |
| Governs | how an implementation agent performs a patch after `hhtech/auditreport.md` has identified findings against a target artifact |
| Auth | governing, over patch-agent conduct only |
| SoT | AUTHORITATIVE about patch *procedure*; carries no architectural authority |
| Canon | n/a — not a Record, not World Truth, not canonical data |

**What this document is.** The patch-side counterpart to `hhtech/standards/audit-standard.md`
(which governs how an *audit* conducts itself), to Artifact 004 / `CLAUDE.md` (which governs how
a build *session* conducts itself), and to Artifact 003 (which governs how an artifact is
*authored*). This document governs how a *patch* conducts itself, once an audit has already
identified findings against one target artifact.

**What this document is not:**

- It is **not** an artifact-specific patch prompt. That is generated later, per artifact, from
  `hhtech/auditreport.md` + this standard + current source context — see §21.
- It is **not** an audit report. It consumes one; it does not produce one.
- It is **not** a patch execution log. §20 defines the *schema* a patch result must follow; no
  artifact-specific result belongs in this file.
- It is **not** a replacement for the Master Blueprint, the Record Model System, or the OS File
  Build Roadmap. It amends none of them.
- It is **not** a Claude Code instruction tied to one specific artifact. It is reusable across
  Artifacts 001–490.

**What a patch is**, for the purposes of this document: a minimal, traceable, source-grounded
correction to a target artifact — and, only when explicitly justified (§3), its declared
companion files — that resolves a confirmed audit finding without changing anything the finding
does not require.

**What a patch is not:** a redesign; a rewrite; an opportunity to also fix something unrelated
that was merely noticed along the way; a way to make an audit "pass" by weakening the
requirement instead of correcting the artifact; and — stated once here because the category
error is easy to make — **not a canonical-data mutation**. Spine law 2's `propose → check →
human gate → commit → changelog → log` path (Blueprint §10, §12.6) governs changes to World
canon inside `canon/**`. This document governs changes to repository *artifacts*. The two are
never the same operation, and this standard grants no authority to write canonical data (§3,
§10).

`Auth: governing` binds patch-agent conduct and nothing above it. Where this document and the
Blueprint, RMS, Roadmap, or `audit-standard.md` disagree, **they are right and this document is
wrong** — the patch agent stops and reports the disagreement rather than resolving it by this
document's wording.

---

## 0. Two Kinds of Statement in This Document

The same split `audit-standard.md` §0 establishes, applied to patching.

| Kind | What it is | Who sets it |
|---|---|---|
| **AUTHORITATIVE REQUIREMENT** | A rule that exists because Blueprint, RMS, Roadmap, the target artifact's own contract, or a confirmed audit finding states it. Failing to satisfy it is a defect in the *artifact*. | Blueprint / RMS / Roadmap / `hhtech/auditreport.md` (confirmed findings only) |
| **PATCH PROCEDURE** | A rule about how the patch agent works — what to read first, how much to change, how to validate, how to report. Violating it is a defect in the *patch process*, not necessarily in the artifact. | This document (HHTECH) |

A patch procedure is never cited as the reason a *change* was architecturally required. If a
rule in this document appears to grant new architectural authority, that is a drafting defect in
this document, and it is reported rather than acted on as if it were source-established (§10).

---

## 1. Purpose

`patch-standard.md` governs the process an implementation agent follows to correct findings that
`hhtech/auditreport.md` has raised against one target artifact.

**When it applies.** After an audit has produced a report containing at least one finding that
requires correction (any P0, any P1, a blocking-classified P2 per `audit-standard.md` §9/§1.6,
or a P3 a human has explicitly directed to be addressed), or when a human explicitly directs a
patch operation citing specific findings.

**Relationship to `audit-standard.md`.** That document defines how a finding is discovered,
evidenced, and classified. This document takes those findings as *unverified input* (§6) and
defines how a confirmed one becomes a correction. **This document does not redefine severity,
verdict, or evidence vocabulary — it imports `audit-standard.md`'s exactly, everywhere (§4).**

**Relationship to `patchprompt.md`.** `patchprompt.md` is generated later, per artifact, from
`hhtech/auditreport.md` + this standard + the current source context. It is not created by this
document, and this document does not become obsolete once one exists — §21 states the contract
a generated `patchprompt.md` is expected to carry.

---

## 2. Authoritative Inputs

Seven inputs are available to a patch operation. Their authority order extends
`audit-standard.md` §1.1's five tiers; it does not replace them.

| # | Input | Role | Authority |
|---|---|---|---|
| 1 | **Master Blueprint** | architectural truth | Tier 1 — primary, jointly with RMS |
| 2 | **Record Model System v1.0** | six-model architecture in detail | Tier 2 — primary, jointly with Blueprint |
| 3 | **OS File Build Roadmap (REPAIRED)** | build order, the target artifact's own manifest row (`Val`/`Done`/`BP`/`RMS`/`H`/`S`/`LS`/`G`/`→` and every other field) | Tier 3 |
| 4 | **Target artifact** — current authored content | the object being patched | Tier 4 |
| 5 | **`hhtech/auditreport.md`** | evidence that a problem exists | **not a tier** — see below |
| 6 | **Current git diff / repository state** | fact of what exists and what changed | Tier 5 — never architecture |
| 7 | **Relevant dependency/context** | facts a finding or the artifact directly relies on | inspected only as needed — `audit-standard.md` §5.1's `H`-dependency rule applies here unchanged: never full-audited, never recursively inspected |

**An audit finding is evidence of a problem. It does not outrank Tiers 1–4.** A finding's
severity, its evidence, and its stated remediation direction (`audit-standard.md` §16) are
themselves subject to independent verification (§6) before they license any change. **If an
audit finding conflicts with Tiers 1–4 — misreads a citation, names a requirement that does not
exist, or contradicts the artifact's own correctly-scoped `Val`/`Done` — the patch agent MUST
NOT blindly implement it.** It is handled per §6 and §16: not patched, and reported.

Tier 5 (git diff / repository state) is fact, never architecture — `CLAUDE.md`, verbatim: *"Git
history is not architectural authority. It records file changes, never canonical meaning."*

---

## 3. Patch Scope

**The normal boundary is the target artifact's own declared path**, plus any file its own
manifest entry declares as a RULE-G3 merge (Artifact 003, RULE G3). Nothing else is in scope by
default.

**Another file may be modified only when both conditions hold:**

1. the confirmed correction (§6) is impossible without it, **and**
2. the additional file's modification is itself required by Tiers 1–3 — a declared RULE-G3
   companion, or a file the finding's own source citation directly implicates.

Every such file is named with an explicit justification in the patch report (§20). A file that
fails either condition is out of scope, however convenient touching it would be.

**Prohibited scope expansion**, stated with the standard's own example: if Artifact 042 has a
validator bug, the patch corrects the validator — it does not redesign the validation
subsystem, because nothing in Tiers 1–3 requires that redesign to fix this bug. `CLAUDE.md`'s
rule binds identically here: *"While I am here, I will also build…" is PROHIBITED.* An
unrelated correction is not smuggled into a patch because it is nearby, because it looks easy,
or because the implementation is already understood.

**Never in scope, under any finding:**

- **`canon/**`.** No finding — including one that claims a canonical Record is wrong — licenses
  a canonical write. `CLAUDE.md`: *"No direct canonical writes. Never write canonical Records
  directly. All canonical mutation passes through the governed Mutation Coordinator path
  (Spine law 2) once that architecture exists."* And: *"No bypass — not for convenience,
  tests, speed, or development ease."* The Mutation Coordinator
  is Roadmap P5 (artifacts 145–166) and is **not yet built**; a finding about canonical content
  is reported, never patched, until it exists. Roadmap anti-orderings X-01, X-07, X-11, X-12
  name the same prohibition from the build-order side.
- **The Master Blueprint, the Record Model System, or the Roadmap.** §10.
- **A sibling or downstream artifact's own declared territory** (RULE G/G2/G3;
  `audit-standard.md` §3.2's out-of-scope rule) — even where patching it would be simpler than
  patching the target.

---

## 4. Finding Intake

A finding consumed from `hhtech/auditreport.md` carries, per `audit-standard.md` §14.1 item 8:
finding ID (`AUD-<artifact>-<NN>`, §14.2), severity, affected location, source requirement,
evidence, expected behavior, actual behavior, a remediation direction where one was
determinable, and a validation condition — the observable state that would demonstrate the
finding is resolved.

**Severity handling is `audit-standard.md` §9's vocabulary, unmodified, with the patch-side
action stated for each:**

| Severity | `audit-standard.md` §9 condition (unmodified) | Patch-agent action |
|---|---|---|
| **P0** | Spine-law/`FROZEN`/anti-ordering violation; canonical-gate breach; COM reintroduction | Highest priority (§7). If genuinely not patchable at the artifact's own level — e.g. it requires infrastructure not yet built — report as such (§16) rather than fabricate a correction. |
| **P1** | Artifact's own `Val`/`Done` unmet; cited `BP`/`RMS` contradicted; `H`/`LS`/`G` violated; scope has expanded into a downstream artifact | Resolved per the artifact's own `Val`/`Done` and `BP`/`RMS` citation. Blocks completion (§17) until resolved. |
| **P2** | Source-supported, non-blocking structural drift; not itself resolved to INFO by a recorded non-blocking classification (`audit-standard.md` §1.6) | Resolved if source-supported and not itself dependent on unbuilt infrastructure. A P2 already downgraded to INFO by `audit-standard.md` §1.6/§9 is **not** patched. |
| **P3** | Wording imprecision, loose citation, weak-but-checkable `Val`, terminology drift | Patched when the correction is safe and minimal. May be explicitly deferred with a stated reason (§20) — never silently dropped. |
| **INFO** | `NOT SPECIFIED BY AUTHORITATIVE SOURCE`; recorded non-blocking conflict; legitimate choice inside an open boundary | **Never patched.** `audit-standard.md` defines INFO as never affecting verdict; correcting it is prohibited scope expansion (§3). |
| **UNVERIFIABLE** (a traceability-table value, not a severity) | The requirement could not be checked with available evidence or authority (`audit-standard.md` §8.2) | Not "patched into PASS." If UNVERIFIABLE because the artifact itself is missing content that is its own declared responsibility, supplying that content is a legitimate patch. If UNVERIFIABLE because of a gap outside the artifact (e.g. GAP-C's absent requirement register), there is nothing to patch — it stays UNVERIFIABLE and is reported (`audit-standard.md` §13.3 rule 4). |
| **BLOCKED** (a verdict, not a per-finding severity) | The audit itself could not determine mandatory-condition compliance (`audit-standard.md` §13.1) | Not a patch target. The patch agent cannot patch its way out of a BLOCKED verdict caused by unavailable source or an unresolved upstream dependency. Reported for human/authorial resolution. |

**Four categories, routed differently, never merged:**

```
confirmed defect              → patch (§7–§9)
unresolved / unverifiable     → do not patch; report (§16)
disputed finding              → do not patch; report the contradiction (§6, §16)
informational observation     → never patched; not a defect at all
```

---

## 5. Pre-Patch Analysis

**No editing begins before all eight steps are complete:**

1. Read the full target artifact — not the excerpt the finding quotes.
2. Read the Tier 1–3 section(s) the finding cites, directly. Never trust the finding's paraphrase
   of a source; read the source (`audit-standard.md` §1's own evidence discipline; `CLAUDE.md`
   "Read First").
3. Read the relevant finding(s) in full — evidence, requirement citation, remediation direction.
4. Inspect current `git diff`/`git status` (Tier 5) to establish the actual starting point.
   `CLAUDE.md`'s git discipline: *"`git status` before work → work → `git diff` / `git status`
   after work."*
5. Locate the exact implementation or specification location the finding names.
6. Determine the smallest valid correction (§8).
7. Identify possible regressions the correction could cause (§15).
8. Determine whether the finding is actually patchable at this artifact's own level, or whether
   it requires unbuilt infrastructure, belongs to a different artifact, or is itself disputable
   (§16).

---

## 6. Finding Validation

**The patch agent independently verifies every finding before patching it. It does not blindly
trust the audit output.**

```
audit finding
      ↓
locate the claimed defect at its stated location
      ↓
compare directly against the authoritative source (Tiers 1–3)
      ↓
confirm the defect actually exists, as claimed
      ↓
determine the correction
      ↓
patch
```

`audit-standard.md`'s own §10 (False-Positive Control) exists because a finding can fail those
checks; the patch agent re-derives the mismatch from Tiers 1–4, as if performing a miniature
audit of that one requirement, before touching any file.

**If the finding cannot be reproduced or is contradicted by the authoritative source, the agent
does exactly one of the following — never a fourth option, never a guess:**

- **`FINDING NOT REPRODUCIBLE`** — the claimed defect is not present at the cited location.
  State the exact reason. Do not patch. Do not guess at a different location. Leave the finding
  open for the auditor to re-examine.
- **`FINDING CONTRADICTED BY SOURCE`** — the authoritative source, read directly, does not say
  what the finding claims. Quote the source text exactly. Do not patch. Do not silently agree
  with the audit merely because it is the audit.
- **`INSUFFICIENT EVIDENCE TO VALIDATE FINDING`** — the available evidence does not clearly
  establish the finding either way. Do not patch; never guess (mirrors
  `audit-standard.md` §7.3's `INSUFFICIENT EVIDENCE` discipline, applied on the patch side).

---

## 7. Patch Order

**Severity order, exactly `audit-standard.md` §9's, with no reinvention:**

```
P0  →  P1  →  P2  →  P3
```

An artifact whose constitutional boundary (P0) is wrong cannot be usefully corrected for
completeness (P2/P3) first — the boundary decides what "complete" even means. `audit-standard.md`
P0 itself: *"Blocks the artifact and anything whose own compliance depends on this one."*

**Within one severity, in this order:**

1. constitutional / authority issues
2. boundary issues
3. correctness
4. completeness
5. tests
6. documentation
7. minor cleanup

**Low-priority cleanup must never obscure an unresolved blocking finding.** A diff burying an
open P0 under a dozen P3 wording fixes is a defect in the patch, not a stylistic choice — the
patch report (§20) lists P0/P1 status first, regardless of the diff's own ordering.

---

## 8. Minimal Change Rule

**Mandatory: the patch is the smallest change that completely resolves the confirmed finding,
and no more.**

**Explicitly prohibited, none of them excusable by "it was already broken" or "it's cleaner
this way":**

- unrelated refactors
- style rewrites
- renaming without necessity
- architectural redesign the finding does not require
- cleanup unrelated to the finding
- speculative improvements

**Worked example.** If a target artifact is missing one required field, the patch adds that
field and the validation it needs — it does not rewrite the artifact's surrounding
specification, and it does not restructure sections the finding never touched. The correction's
size is set by what the finding requires, never by what would look more complete.

---

## 9. Preservation Rule

**Anything already compliant remains compliant.** The patch preserves:

- existing valid behavior
- constitutional constraints
- artifact boundaries
- required interfaces
- existing passing tests
- unrelated functionality

**A patch that resolves one finding while introducing another defect is not complete** (§15,
§17). "The named finding is fixed" is never sufficient by itself.

---

## 10. Authority Protection

**A hard firewall.** The patch agent MUST NOT modify the Master Blueprint, the Record Model
System, or the Roadmap merely to eliminate a finding — not by a word, not by a footnote.

`CLAUDE.md`'s "No Silent Architecture Changes" section states the governing rule of this
section, verbatim: *"If architecture needs to change: stop → identify the source conflict →
report it → do not patch architecture locally."*

**Stated as the worked example this standard is built around:** if a target artifact violates an
RMS requirement, the patch agent may patch the target artifact. **The patch agent MUST NOT
"fix" the problem by silently rewriting the RMS requirement.** The same holds one level down: if
the Roadmap requires a particular artifact boundary, the patch agent cannot expand the artifact
merely because a different boundary would be more convenient to implement.

**If the authoritative source itself appears internally inconsistent** — not an artifact defect,
but a genuine Tier 1–3 contradiction — the patch agent does not adjudicate it. It follows
`CLAUDE.md`'s Conflict Handling procedure, verbatim in shape:

```
SOURCE CONFLICT
        ↓
identify exact documents / sections
        ↓
do not silently choose an interpretation
        ↓
follow source authority precedence
        ↓
if unresolved, report the conflict
        ↓
continue only if the current artifact is not blocked
```

Classification of
whether such a conflict is recorded-non-blocking, a new P0/P1/P2 finding, or grounds for a
BLOCKED verdict is `audit-standard.md` §1.6's job, not this document's or the patch agent's own
judgment.

**The canon firewall restated from §3 applies here too:** a patch never writes to `canon/**` to
"resolve" a finding about canonical correctness. That path does not exist yet.

---

## 11. Traceability

```
Finding ID  →  Requirement  →  Source location  →  Changed location  →  Validation
```

The patch report (§20) carries this mapping explicitly, one row per changed location. **A
changed line that cannot be justified by a finding, or by an explicitly necessary consequence of
one, is suspicious scope expansion** — flagged in the self-audit (§18) and removed before the
patch is reported complete, not explained away after the fact.

---

## 12. Diff Firewall

After patching, inspect `git status`, `git diff`, and `git diff --check`. This is the
producer-side mirror of `audit-standard.md` §12's Diff Audit, which the re-audit will run
independently.

**Categories the inspection must catch, and remove before completion:**

- unexpected file changes outside the traceability map (§11)
- unrelated hunks inside an otherwise-justified file
- generated or derived artifacts accidentally committed as authored (`derived/**`,
  `fixtures/**` — Roadmap PART I/PART VII SoT table; `audit-standard.md` §12 point 8)
- temporary files
- debugging changes
- accidental formatting churn

**The final diff contains only justified changes.** Anything else found here is removed before
the patch is reported complete — it does not wait for the re-audit to catch it.

---

## 13. Implementation Validation

**Proportional to the finding, and to the artifact's own `T` value** — `audit-standard.md` §6
Pass 9's own scoping is reused rather than reinvented: implementation-correctness checks apply
*"only when `T` includes `code` or `schema`"*; a `T: doc` constitutional artifact has no syntax
to validate in that sense, and this document does not manufacture one.

**Where applicable, in this order:**

1. syntax / import validation, for `T: code` or `T: schema` artifacts
2. the targeted test(s) that exercise the finding's own requirement
3. the artifact's relevant regression tests (§15)
4. structural validation, where the artifact is itself a schema/validator or has a RULE-G
   companion
5. negative tests, where rejection is a requirement the finding touches (§14)
6. diff inspection (§12)

Requiring a test that is impossible or irrelevant to the artifact is itself a defect in the
patch process, not a stricter standard — the validation strategy is chosen to match the
finding, never omitted for convenience.

**Generating a check is not running it.** Roadmap PART XV, verbatim: *"Generating tests ≠
running them. Generating drills ≠ executing them. Generating benchmarks ≠ measuring them."*
`CLAUDE.md` states the same rule for this session directly. A patch report (§20) that claims
tests passed without evidence they were actually executed does not satisfy this section.

---

## 14. Negative Validation

Roadmap PART XI, verbatim: *"Negative testing is first-class: every anti-ordering has an
artifact proving rejection."*

**Where the finding touches a rejection requirement, the patch demonstrates both:**

```
valid input    →  accepted
invalid input  →  still rejected
```

**A patch is not accepted merely because the happy path works.** If the correction could
plausibly have loosened a refusal, deny-check, or validation boundary while fixing the named
defect, the negative case is exercised and its result recorded in the patch report (§20), not
assumed.

---

## 15. Regression Control

At minimum, inspected against the pre-patch baseline (§5 step 4):

- existing tests
- neighboring behavior
- artifact boundary
- dependency assumptions
- public / required interfaces
- serialization/deserialization behavior, where relevant
- failure behavior, where relevant

**These are `audit-standard.md` §6 Pass 12's own questions, reused rather than reinvented**,
because they are exactly what the Post-Patch Re-Audit will independently re-run: *"Has a MUST
become a SHOULD? Has a refusal/deny check been loosened, removed, or had its scope narrowed? Has
a previously-enforced boundary become optional? Has a test's assertion been weakened to make it
pass, rather than the implementation fixed?"* The patch agent checks these
before the re-audit does, not instead of it.

---

## 16. Disputed / Unverifiable Findings

**A patch agent MUST NOT fabricate a correction for an unverifiable issue.**

If evidence is insufficient (§6):

- do not invent behavior;
- do not broaden scope to "cover" the uncertainty;
- do not change an authoritative requirement to make the uncertainty disappear;
- record the issue, using the exact reporting form from §6
  (`FINDING NOT REPRODUCIBLE` / `FINDING CONTRADICTED BY SOURCE` /
  `INSUFFICIENT EVIDENCE TO VALIDATE FINDING`), for audit/human review.

**If a finding is demonstrably false**, per §6's comparison against Tiers 1–4: do not patch
merely because the audit report says so; document precisely why it is not patchable, quoting the
contradicting source.

**No second vocabulary.** A finding the patch agent could not validate is reported using
`audit-standard.md`'s own terms — `UNVERIFIABLE`, `NOT SPECIFIED BY AUTHORITATIVE SOURCE`,
`INSUFFICIENT EVIDENCE` — never a new term invented for the same concept.

---

## 17. Patch Completion Criteria

**A patch is complete only when every condition below holds:**

| # | Condition | Governed by |
|---|---|---|
| 1 | Every patchable blocking finding (P0/P1, and any blocking-classified P2) is resolved | §7, §8 |
| 2 | Required non-blocking findings are resolved per what the audit result actually required | §4 |
| 3 | Authoritative constraints remain intact | §9, §10 |
| 4 | No unjustified scope expansion occurred | §3, §11 |
| 5 | Tests/validation actually ran and passed | §13 |
| 6 | Negative/rejection behavior remains correct | §14 |
| 7 | `git diff` is clean and bounded | §12 |
| 8 | Every changed location is traceable to a finding | §11 |
| 9 | No unrelated modification remains | §12 |

**If any condition fails, the patch is not complete.** The patch agent reports exactly which
condition failed and why, and does not claim completion — `CLAUDE.md`: *"File creation alone is
not evidence of completion."* Completion is these conditions, never mere activity.

---

## 18. Post-Patch Self-Audit

Before declaring completion, the patch agent walks its own work through the same chain the
re-audit will independently re-run:

```
Findings  →  Changed files  →  Changed hunks  →  Tests  →  Regression checks  →  Scope check  →  Authority check
```

**This self-audit does not replace the independent HHTECH/GPT re-audit.**
`audit-standard.md` §15 states exactly why, and it is quoted here rather than restated: *"Never
close a finding solely because a patch's own report claims success."* Claimed completion is not
evidence — the self-audit is the patch agent's own diligence check; it carries no authority to
close a finding.

---

## 19. Re-Audit Handoff

**What the patch operation leaves behind, for the next audit:** the traceability map (§11), the
inspected diff (§12), the validation results with evidence of actual execution (§13), and the
patch report (§20). This is what lets a Post-Patch Re-Audit (`audit-standard.md` §5.3, §15)
independently re-verify every prior open finding and assign it a fresh `Outcome` —
`CONFIRMED-OPEN` / `CLOSED` / `REOPENED-REGRESSION` / `SUPERSEDED`.

**The implementation agent MUST NOT declare an artifact permanently PASS.** `audit-standard.md`
§13's Verdict Model is something an *audit* reaches, through its own decision procedure (§13.3
there) — never something a patch operation self-issues, no matter how confident the self-audit
(§18) was.

---

## 20. Patch Report Contract

The schema for an artifact-specific patch execution result. **This section defines the schema
only — no artifact-specific result belongs in this document**, matching
`audit-standard.md` §14's own framing of its report schema.

**At minimum, a patch report states:**

1. artifact ID
2. patch status (complete / incomplete, per §17)
3. findings addressed
4. findings not addressed, with reason (§4, §16)
5. files changed
6. reason for each changed file (the traceability entry, §11)
7. validation performed, with evidence it was actually executed (§13)
8. test results
9. unresolved issues
10. final diff summary (§12)

---

## 21. Universal Patch Execution Contract

The deterministic sequence this standard defines, stated once, concisely, for later embedding
into a generated `patchprompt.md`:

```
READ  →  VALIDATE  →  PLAN  →  PATCH  →  TEST  →  INSPECT DIFF  →  SELF-AUDIT  →  HAND OFF FOR RE-AUDIT
```

| Step | Governed by |
|---|---|
| READ | §5 Pre-Patch Analysis |
| VALIDATE | §6 Finding Validation |
| PLAN | §7 Patch Order, §8 Minimal Change Rule |
| PATCH | §8, §9 Preservation Rule, §10 Authority Protection |
| TEST | §13 Implementation Validation, §14 Negative Validation |
| INSPECT DIFF | §12 Diff Firewall |
| SELF-AUDIT | §18 Post-Patch Self-Audit |
| HAND OFF FOR RE-AUDIT | §19 Re-Audit Handoff, §20 Patch Report Contract |

A generated `patchprompt.md` is expected to instantiate this eight-step sequence with the
specific findings and target artifact filled in. This document does not itself generate that
file, and creating it is explicitly out of this document's own scope (§1).

---

## Consistency Verification

Checked against `audit-standard.md`, the Blueprint, RMS, and the Roadmap before this document
was considered complete:

- **Severity terminology** (P0–P3, INFO) — imported from `audit-standard.md` §9 verbatim,
  nowhere redefined (§4, §7).
- **`UNVERIFIABLE` and `BLOCKED` semantics** — imported from `audit-standard.md` §8.2/§13
  verbatim, including the blocking/non-blocking split (§4, §16).
- **Authority hierarchy** — extends `audit-standard.md` §1.1's five tiers rather than
  restating or reordering them (§2).
- **Scope rules** — the `H`-dependency inspection-only rule is imported from
  `audit-standard.md` §5.1/§3.2 unchanged (§2, §3).
- **Re-audit semantics** — `audit-standard.md` §15's re-audit rules (CLOSED only on current
  evidence; claimed completion is not evidence) are cited, not duplicated with different
  wording (§18, §19).
- **Canonical-data boundary** — grounded in `CLAUDE.md`'s Canonical Data Safety section and
  Spine law 2; the Mutation Coordinator's non-existence is stated exactly as `CLAUDE.md` states
  it (§3, §10).
- **No section grants authority the source documents do not grant.** Every MUST/MUST NOT in
  this document traces to a Blueprint, RMS, Roadmap, `CLAUDE.md`, Artifact 003, or
  `audit-standard.md` citation stated inline.

No source contradiction was found that bears on this document. Where a citation's own precision
is worth a reader's caution — none arose during drafting — it would be recorded here rather than
silently resolved.

---

*This document governs patch procedure only. It carries no architectural authority, defines no
Record Model, and amends nothing in the Master Blueprint, the Record Model System, the OS File
Build Roadmap, or `hhtech/standards/audit-standard.md`. Where it and they differ, they are right
and this document is wrong.*
