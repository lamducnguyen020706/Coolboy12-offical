# HHTECH — COOLBOY12 Audit Standard

## Status and Authority

| Field | Value |
|---|---|
| Document | `hhtech/standards/audit-standard.md` |
| Kind | HHTECH-internal operational standard — **not** a COOLBOY12 Roadmap artifact |
| Governs | how a GPT-5.6 auditor performs an audit of a COOLBOY12 artifact |
| Auth | governing, over auditor conduct only |
| SoT | AUTHORITATIVE about audit *procedure*; carries no architectural authority |
| Canon | n/a — not a Record, not World Truth, not canonical data |

**What this document is.** An operational contract for how an auditor reads, checks, and
reports on a COOLBOY12 artifact. It is the audit-side counterpart to
`docs/conventions/artifact_conventions.md` (Artifact 003, which governs how an artifact is
*authored*) and to `CLAUDE.md` (Artifact 004, which governs how a build *session* conducts
itself). This document governs how an *audit* conducts itself.

**What this document is not**, stated so it cannot be assumed:

- It does **not** define World Truth, own a Record Model, or hold canonical data.
- It does **not** amend the Master Blueprint, the Record Model System, or the OS File Build
  Roadmap.
- It does **not** invent architectural requirements. Every compliance rule an auditor applies
  must trace to Blueprint, RMS, Roadmap, or the target artifact's own declared contract.
- It is **not** part of the 490-artifact manifest. It carries no `ID`, no `Ph/St`, no place in
  the critical path.
- It is **not** itself audit evidence. A prior `hhtech/auditreport.md` or
  `hhtech/patchprompt.md` is historical output, never a source this standard's rules are
  checked against.

`Auth: governing` binds auditor conduct and nothing above it. Nothing in this document can make
an architectural statement true. Where this document and the Blueprint, RMS, or Roadmap
disagree, **they are right and this document is wrong** — the auditor stops and reports the
disagreement rather than resolving it by this document's wording.

---

## 0. Two Kinds of Statement in This Document

Everything below is one of exactly two kinds, and every rule states which it is.

| Kind | What it is | Who sets it |
|---|---|---|
| **AUTHORITATIVE REQUIREMENT** | A rule that exists because Blueprint, RMS, or Roadmap states it. Violating it is a defect in the *artifact*. | Blueprint / RMS / Roadmap |
| **AUDIT PROCEDURE** | A rule about how the auditor works — what to read, how to record evidence, how to name a severity, how to shape a report. Violating it is a defect in the *audit*, not necessarily in the artifact. | This document (HHTECH) |

An audit procedure is never cited as the reason an artifact fails. A finding's severity, its
evidence shape, and the report schema are audit procedure. The requirement the finding traces
to is, or must be, an authoritative requirement. **If a rule in this document looks like it is
inventing a new architectural obligation, it is a drafting defect in this document, and the
auditor reports it rather than enforcing it as if it were source-established.**

---

## 1. Authoritative Source Set and Precedence

### 1.1 The five tiers

| # | Tier | Governs | Role for the auditor |
|---|---|---|---|
| 1 | **Master Blueprint** (`docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md`) | what is architecturally true | primary architectural authority, jointly with RMS |
| 2 | **Record Model System v1.0** (`docs/sources/COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md`) | the six-model Record System architecture in detail | primary architectural authority, jointly with Blueprint |
| 3 | **OS File Build Roadmap (REPAIRED)** (`docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md`) | build decomposition, artifact manifest, dependency/lockstep/gate structure, phase order | the target artifact's own contract (its manifest row) lives here |
| 4 | **Target Artifact** — its declared manifest row plus its current authored content | what this specific artifact claims to be and do | the object under audit |
| 5 | **Current Git Diff / repository state** | what has actually changed and what currently exists on disk | factual evidence of the implementation, never of what *should* be true |

This is the project's own precedence, stated at Roadmap §0.2 (*"Blueprint + RMS govern. Where
the prior roadmap or the old roadmap conflicts with them, they lose"*) and at Artifact 003's
Source Precedence section (*"Blueprint + RMS — architectural authority ↓ Roadmap — build
decomposition and order ↓ Artifact + Phase Conventions — how that decomposition is
expressed"*). This standard adds nothing to it; it only names where evidence for each tier
lives.

### 1.2 Tier 1 and 2 are joint, not ranked against each other

Blueprint and RMS are cited together as one architectural-authority tier by both the Roadmap
and Artifact 003. **Do not treat RMS as subordinate to Blueprint, or Blueprint as subordinate to
RMS.** Where they genuinely conflict on the same question, that is a **source conflict** (§1.6),
not a tie broken by picking one document. Where RMS states that it *closes* a Blueprint-stated
open question (RMS §2, §27 "Closed Decisions", the `AUTHOR-DECIDED` and `FROZEN` tags), the
closure is the current architecture and the Blueprint text it closes is superseded on that
specific point — this is not RMS outranking Blueprint in general; it is RMS's own closure
process being complete on that point (RMS §1: *"v1.0 closes every architectural decision left
open at v0.1"*). The auditor treats a `FROZEN` or `AUTHOR-DECIDED` RMS tag as settled and does
not re-litigate it.

### 1.3 Tier 3 (Roadmap) is subordinate to Tiers 1–2

The Roadmap decomposes build order and expresses artifact contracts. Where a Roadmap entry's
`BP`/`RMS` citation does not actually support what the entry requires, that is a finding against
the Roadmap entry (reported, per §1.6), not license for the auditor to invent a different
requirement, and not grounds to fail the target artifact for something the Roadmap itself got
wrong. The artifact is still audited against its stated `Val`/`Done` unless the auditor has
identified and reported the specific Roadmap defect.

### 1.4 Tier 4 (Target Artifact) never outranks Tiers 1–3

The artifact's own prose is evidence to be judged, not an authority that settles what should be
true. An artifact's internal claim ("this satisfies X") is not self-certifying; the auditor
checks it against the cited source. The artifact's own `Val`/`Done`/`H`/`S`/`LS`/`G`/`BP`/`RMS`
fields, as stated in the Roadmap manifest, **are** the contract the artifact must be checked
against — that contract is Tier 3 evidence about this one artifact, not an independent tier.

### 1.5 Tier 5 (Git diff / repository state) is fact, never architecture

> **CLAUDE.md, verbatim:** *"Git history is not architectural authority. It records file
> changes, never canonical meaning."*

The current repository state is authoritative about **what exists and what changed**. It is
never authoritative about **what should exist**. A file present on disk is evidence to check
against Tiers 1–4; its mere presence proves nothing about compliance.

### 1.6 Conflict handling

```
SOURCE CONFLICT DETECTED
        ↓
identify the exact documents and sections in conflict, verbatim
        ↓
do NOT silently choose an interpretation
        ↓
classify by precedence (§1.1–§1.4)
        ↓
is the conflict already recorded and marked NON-BLOCKING at source?
   (worked examples: Roadmap PART VIII DG-01/DG-02; RMS Appendix H PC-1..PC-4)
        ↓ yes                                    ↓ no
treat as recorded, non-blocking;          the conflict bears on this artifact:
proceed with the artifact audit,          report it as a finding, classify as
citing the recorded resolution            P0 or P1 per §9, and continue only
                                           if the target artifact is not itself
                                           blocked by the unresolved question
                                                    ↓
                                           if the artifact CANNOT be evaluated
                                           without resolving the conflict →
                                           verdict = BLOCKED (§13)
```

**Never resolve a genuine, unrecorded source conflict by the auditor's own judgment.** The two
worked examples of correctly recorded conflicts are Roadmap DG-01 (Blueprint §9.4 vs
§13.6e/I-105) and DG-02 (Blueprint §13.10's residual `PROPOSED` flag vs RMS's closed WSV
granularity) — both are stated, both sides quoted, both marked "OPEN — author wording fix.
NON-BLOCKING." A new conflict the auditor finds is reported in the same shape: what each source
says, verbatim, and why it is unresolved.

---

## 2. Core Definitions

**Finding.** A specific, evidenced statement that a requirement is not satisfied, or that a
condition the auditor must actively search for (§10) is present. A finding has a stable ID
(§14.2), a severity (§9), a source requirement (§4), evidence (§7), an impact statement, and a
remediation direction if one is determinable.

**Observation.** A recorded note that is not a finding — a `NOT SPECIFIED BY AUTHORITATIVE
SOURCE` gap, an `INSUFFICIENT EVIDENCE` item, a documented and already-non-blocking conflict, or
a style choice within legal bounds. Observations never affect the verdict.

**Requirement.** Any authoritative, source-traceable obligation the target artifact is checked
against: a Spine law, an invariant (I-01…I-108), an anti-ordering (X-01…X-22), a Blueprint or
RMS clause the artifact's own `BP`/`RMS` field cites, the artifact's own `Val`/`Done`, an
Artifact 003 conformance requirement (C-1…C-12) if the artifact is itself a manifest entry, or
a RULE G/G2/G3 boundary question.

**Evidence.** A concrete, checkable pointer per §7 — never a feeling, an impression, or an
unqualified "this looks wrong."

**Severity.** One of P0/P1/P2/P3/INFO, defined in §9. Audit procedure, not a source vocabulary.

**Verdict.** One of PASS / PATCH REQUIRED / BLOCKED, defined in §13.

---

## 3. Audit Scope

### 3.1 What is in scope

For a target artifact, the auditor checks:

1. **Artifact identity** — does the artifact match its own Roadmap manifest row (`ID`, `Name`,
   `path`, `Own`, `RM`, `T`, `R`, `SoT`, `Auth`, `Canon`, `CD`, `Ph/St`) per Artifact 003 §4–§12?
2. **Scope** — does the artifact's actual content stay within its declared `Name` and Roadmap
   responsibility, or has it absorbed a later phase's or a sibling artifact's work?
3. **Requirements** — every `Val`, `Done`, `BP`, `RMS`, `Req` field on the artifact's manifest
   row, checked per §6.
4. **Blueprint compliance** — the cited `BP` section(s), and any Spine law or invariant the
   artifact's domain plausibly touches (discovery procedure at §6.2).
5. **RMS compliance** — the cited `RMS` section(s), and the relevant model-specific closure
   (§7–§12, Appendix A/H/I) if the artifact concerns one of the six models.
6. **Roadmap compliance** — `H`/`S`/`LS`/`G`/`→` per Artifact 003's dependency conventions, and
   the artifact's phase membership (Artifact 003, Phase/Stage Conventions table).
7. **Internal consistency** — does the artifact contradict itself, or contradict an
   already-accepted upstream artifact it depends on (`H`)?
8. **Completeness** — does the artifact's content actually discharge everything its own `Val`
   names, with nothing left implicit?
9. **Boundary integrity** — RULE G / G2 / G3 (Artifact 003), the mechanism/semantics boundary
   (RMS §3–§4, Blueprint §13.7a) where applicable, and any model-sovereignty boundary (RMS §2,
   §25 "no seventh model", Blueprint §13.6/§29.1) the artifact's content touches.
10. **Implementation correctness** — if the artifact is `T: code` or `T: schema`, does the
    implementation match its specification and its cited source?
11. **Test correctness** — if the artifact is `T: test`, or has associated tests, per §11.
12. **Git diff** — per §12.
13. **Regression** — has anything previously accepted (an upstream `H` artifact, or a prior
    version of this artifact) been weakened?
14. **Edge cases and negative cases** — does the artifact's own validation (or its tests)
    exercise boundary and rejection conditions, not only the easy positive case?
15. **Accidental scope expansion** — has work belonging to a *different, declared* artifact
    (per the Roadmap manifest) been pulled forward into this one?

### 3.2 What is out of scope

**Only what genuinely belongs to the target artifact.** A defect the auditor notices in a
*different* artifact — including one the target artifact depends on (`H`) — is never folded
into this artifact's findings. It is recorded as an **OUT-OF-SCOPE OBSERVATION**, naming the
artifact it actually belongs to, and it does not affect this artifact's verdict unless the
target artifact's own compliance is *directly* broken by the upstream defect (in which case the
target artifact's own finding cites the upstream defect as its cause, and the upstream artifact
gets its own, separately-scoped finding if and when it is itself audited).

The auditor does not audit: work explicitly deferred to a later phase per the artifact's own
`Done`/`Why` (e.g., RMS-frozen boundaries whose *interiors* are stated `BOUNDARY-NAMING`,
`PROPOSED`, or otherwise open per I-106/I-107 and Blueprint §34.1); a sibling artifact's
declared responsibility; or anything the Roadmap has not yet reached in the artifact's own
dependency chain.

---

## 4. Authoritative Requirement vs Audit Procedure — Applied

Before a finding is written, the auditor answers one question: *"Where, precisely, does the
source state this?"*

- If the answer is a Blueprint section, an RMS section, an invariant ID, a Spine law number, an
  anti-ordering ID, a Roadmap manifest field, or an Artifact 003 conformance requirement (C-1…
  C-12) — the finding may proceed, with that citation as its **source requirement**.
- If the answer is "no source states this, but it seems like good practice" — **the finding does
  not exist.** The auditor records:

  ```
  NOT SPECIFIED BY AUTHORITATIVE SOURCE
  ```

  and stops. This is never promoted to a violation, never phrased as a soft finding, and never
  used to lower a verdict.
- If the answer is "the source states something adjacent, but not quite this" — the auditor
  quotes the adjacent statement exactly and states precisely where it falls short of covering
  the auditor's concern, rather than stretching it to fit.

---

## 5. Audit Modes

### 5.1 Full Artifact Audit

All fourteen passes (§6) run against the complete current state of the target artifact and its
declared `H` dependencies. Used for a first audit of an artifact, or whenever a mode is not
specified.

### 5.2 Diff Audit

The primary lens is the current `git diff`, but a Diff Audit is a **reduced-scope Full Audit**,
not a different rule set. All fourteen passes still apply; a pass may be **skipped only with an
explicit justification** naming what in the diff proves the pass is unaffected (e.g., *"Pass 10
Test Correctness skipped: diff touches only `docs/**`, no test file changed"*). Regression
Analysis (Pass 12) and a full pass through the Requirement Traceability table (§8) — checking
whether any changed line affects any row — are **never skipped**.

### 5.3 Post-Patch Re-Audit

Runs after a patch has been applied. Governed in full by §15. Current repository state and
current `git diff` are the only authority; the prior audit report is historical context, read
for which findings existed, never trusted for whether they are now resolved.

---

## 6. Mandatory Audit Passes

Fourteen passes, each run in order. A pass that cannot be completed for lack of source or
evidence does not silently pass — it produces either a finding (§4) or, if it blocks the whole
audit, escalates to BLOCKED (§13).

### Pass 1 — Artifact Identity

- **Objective:** confirm the artifact is the artifact it claims to be.
- **Input:** the Roadmap manifest row for this artifact's `ID`; the artifact's own header/
  metadata if it states one (constitutional artifacts under `docs/constitution/`, `docs/
  models/**` typically restate their own row).
- **Questions:** Does `path` match the actual file location? Does `Name` describe the actual
  content? Do `Own`, `RM`, `T`, `R`, `SoT`, `Auth`, `Canon`, `CD`, `Ph/St` match Artifact 003's
  legal vocabularies (§6–§12, §11 there) and the Roadmap's stated values for this `ID`?
- **Evidence:** the manifest row (quoted exactly), the file's actual header (if present), file
  existence at the declared path.
- **Finding conditions:** path mismatch; a metadata field using an illegal or invented value;
  a restated header that silently diverges from the Roadmap row.

### Pass 2 — Scope

- **Objective:** confirm the artifact's content matches its declared responsibility and no
  further.
- **Input:** the artifact's `Name`, `Why`, `Val`, `Done`; the neighboring Roadmap rows for
  artifacts this one's `→` unlocks (what is *supposed* to remain downstream).
- **Questions:** Does any section of the artifact state, define, or freeze something that a
  named downstream artifact (per `→`) or the artifact's own stated non-goals is supposed to
  own? Conversely, is anything the artifact's own `Val` requires missing?
- **Evidence:** the specific section/paragraph, quoted, with the downstream artifact `ID` it
  actually belongs to.
- **Finding conditions:** scope creep into a downstream artifact's declared territory; a Val
  clause with no corresponding content.

### Pass 3 — Blueprint Compliance

- **Objective:** the artifact's content is faithful to its cited `BP` section(s), and does not
  contradict a Spine law or a directly relevant invariant outside its own citation.
- **Input:** the cited Blueprint section(s), read directly; the ten Spine laws (§10); invariants
  in the artifact's domain (discovery procedure §6.2 below).
- **Questions:** Does every normative claim in the artifact trace to the cited section, or to
  another section the auditor can name? Does anything in the artifact contradict a Spine law,
  even indirectly? Is the citation itself accurate (does §BP actually say what the artifact
  claims)?
- **Evidence:** Blueprint text quoted verbatim beside the artifact's claim.
- **Finding conditions:** a claim with no Blueprint support; a Spine-law contradiction; a
  citation that does not support the clause it is attached to.

### Pass 4 — RMS Compliance

- **Objective:** the artifact's content is faithful to its cited `RMS` section(s), and does not
  contradict a `FROZEN`/`AUTHOR-DECIDED` RMS closure.
- **Input:** the cited RMS section(s); the relevant model section (§7–§12) if the artifact
  concerns W/E/P/R/V/I; RMS §26 invariants; Appendix A (Kind Catalog) if Kind-related.
- **Questions:** Does the artifact respect the six-sovereign-model boundary (RMS §2, §25 "NO
  SEVENTH SOVEREIGN RECORD MODEL")? Does it respect a `FROZEN` taxonomy count where one applies
  (W 7+1, E 7, P 13, R 14, V 3, I 5 — RMS §13)? Does it treat a `BOUNDARY-NAMING`/`PROPOSED`
  roster as frozen when RMS says it is not (I-106)?
- **Evidence:** RMS text quoted verbatim beside the artifact's claim.
- **Finding conditions:** contradicts an RMS `FROZEN` statement; freezes an RMS-open interior;
  introduces a seventh model, a universal Record base, or model specialization/inheritance
  (RMS §4 nine prohibitions, §2 "No model is a superclass of another").

### Pass 5 — Roadmap Compliance

- **Objective:** the artifact satisfies its own manifest row's dependency and gating structure.
- **Input:** the artifact's `H`/`S`/`LS`/`G`/`→` fields; Artifact 003's Dependency Conventions
  section; Roadmap PART II (dependency classes), PART III (lockstep systems), PART VIII (gates).
- **Questions:** Do all `H` dependencies actually exist and resolve? Is any `LS` partner
  missing (an ATOMIC-PAIR/TRIPLE landed only in part is a defect even if nothing else is
  blocked)? Has a `G` gate been bypassed? Has a soft dependency (`S`) been silently treated as
  hard, or vice versa?
- **Evidence:** the dependency's actual state (exists/does not exist, complete/incomplete);
  the lockstep table row; the gate's stated licensing condition.
- **Finding conditions:** unresolved hard dependency; incomplete lockstep pair/triple; gate
  bypass; dependency-class conflation.

### Pass 6 — Internal Consistency

- **Objective:** the artifact does not contradict itself, and does not contradict an
  already-accepted artifact it depends on.
- **Input:** the full artifact text; the text of its `H` dependencies as currently accepted.
- **Questions:** Do two sections of the artifact state incompatible things? Does the artifact
  restate a fact its `H` dependency already states, and does the restatement match exactly?
- **Evidence:** the two conflicting passages, quoted side by side.
- **Finding conditions:** any internal contradiction; any drift from an upstream artifact's
  already-accepted statement of the same fact.

### Pass 7 — Completeness

- **Objective:** every element the artifact's own `Val` and `Done` require is actually present.
- **Input:** `Val`, `Done` verbatim.
- **Questions:** For each clause of `Val`, is there content that discharges it? Is the `Done`
  observable state actually reached?
- **Evidence:** the specific `Val` clause and the section of the artifact that discharges it (or
  the absence of one).
- **Finding conditions:** any `Val` clause with no discharging content; `Done` not reached.

### Pass 8 — Boundary Integrity

- **Objective:** the artifact respects the architectural boundaries that apply to its domain.
- **Input:** RULE G / G2 / G3 (Artifact 003); the mechanism/semantics boundary (RMS §3–§4,
  Blueprint §13.7a) if the artifact concerns shared infrastructure; the partition-ownership rule
  (I-16, I-101) if the artifact concerns a Record Model; the canonicality-is-model-defined rule
  (I-104, Blueprint §13.7c) if the artifact concerns canonicality.
- **Questions:** If the artifact is (or should be) split under RULE G/G2/G3, is it? If merged
  under RULE G3, is the merge declared explicitly? Does the artifact treat a shared mechanism as
  conferring shared semantics, or treat one model's semantics as another's?
- **Evidence:** the specific clause; the RULE or invariant it violates.
- **Finding conditions:** a specification/schema merge (violates RULE G); an example/test merge
  (violates RULE G2); an undeclared multi-file merge (violates RULE G3); a mechanism-as-semantics
  or cross-model-ownership error.

### Pass 9 — Implementation Correctness

*(Applies only when `T` includes `code` or `schema`.)*

- **Objective:** the implementation matches its specification and its cited source.
- **Input:** the artifact's specification (its own doc, or the artifact it is a schema/impl for
  under RULE G); the code or schema itself.
- **Questions:** Does the code do what the specification says? Does it silently do more or
  less? Is error/refusal behavior present where the specification requires it (e.g., structural
  validators, deny-hooks, refusing commands)?
- **Evidence:** the specification clause beside the code excerpt (path:line).
- **Finding conditions:** behavior not matching specification; silent scope expansion in code;
  missing refusal/validation the specification requires.

### Pass 10 — Test Correctness

*(Applies whenever the artifact has associated tests — its own, or a paired `T: test` artifact
under RULE G2.)*

Governed in full by §11.

### Pass 11 — Diff Integrity

Governed in full by §12.

### Pass 12 — Regression Analysis

- **Objective:** nothing previously accepted has been weakened.
- **Input:** the current artifact and its dependencies vs. the last known-accepted state (the
  prior commit before the current diff, or the prior audit's evidence baseline for a
  re-audit).
- **Questions:** Has a MUST become a SHOULD? Has a refusal/deny check been loosened, removed, or
  had its scope narrowed? Has a previously-enforced boundary become optional? Has a test's
  assertion been weakened to make it pass, rather than the implementation fixed?
- **Evidence:** the before/after text or code, side by side.
- **Finding conditions:** any weakening of a previously-enforced requirement without a recorded,
  source-grounded reason.

### Pass 13 — Edge Cases

- **Objective:** boundary conditions are actually exercised, not only the central case.
- **Input:** the artifact's own domain boundaries (e.g., numeric limits, enum boundaries,
  singleton cases like WSV, the empty/zero case).
- **Questions:** What happens at the boundary the specification names (minimum ordinal, maximum
  ordinal, the WSV singleton exception, an empty slug, a partition boundary)? Is that boundary
  case addressed in the artifact, its tests, or explicitly and correctly out of scope?
- **Evidence:** the specific boundary condition and whether it is handled.
- **Finding conditions:** an unhandled boundary condition the source requires to be handled.

### Pass 14 — Negative Audit

Governed in full by §10.

### 6.1 Order and independence

The passes run in the order listed. A finding from an earlier pass does not excuse skipping a
later pass — each pass is independently completed (or explicitly justified as skipped, Diff
Audit mode only, §5.2) and independently reported.

### 6.2 Requirement discovery — how to avoid missing a requirement

An artifact's own `BP`/`RMS` citation is a **floor**, not a ceiling, for what the auditor checks.
Before concluding a pass, the auditor additionally checks:

1. **The neighborhood of the cited section** — sibling subsections under the same top-level
   Blueprint section or RMS section number (e.g., an artifact citing Blueprint §13.7a is also
   checked against §13.7, §13.7b, §13.7c if its content plausibly touches them).
2. **The invariant register (Blueprint §36) and RMS §26** for any invariant whose stated
   `Where` column names a section the artifact cites, or whose text names a concept the artifact
   handles (partition, identity, canonicality, temporal, provenance).
3. **The anti-ordering table (Roadmap PART IX, X-01…X-22)** for any row whose "Prohibited order"
   plausibly involves the artifact's domain.
4. **The Spine (Blueprint §10)**, always — ten laws, checked against every artifact regardless
   of citation, because the Spine binds everything (§10: *"Every mechanic this document deepens
   exists to keep one of these laws true"*).

This is a search obligation, not an invitation to invent — every requirement found this way must
still be quoted verbatim as its own finding's source (§4).

---

## 7. Evidence Standard

Every finding carries evidence in this order of preference:

1. **File path** (repository-relative).
2. **Section/heading**, or **symbol/class/function name** for code.
3. **Line range**, where the tooling used to read the file supports it.
4. **Test name**, if the finding concerns a test.
5. **Git diff hunk reference**, if the finding concerns a change.
6. **Source requirement citation** — Blueprint §, RMS §, invariant ID, Spine law #, anti-ordering
   ID, or Roadmap `ID`/field.

### 7.1 Required finding shape

```
Requirement  →  observed implementation  →  mismatch  →  consequence
```

Every finding is written in this shape. Example (illustrative form, not an instance-specific
finding — none belongs in this document):

> Requirement: RMS §4, *"The universal envelope is the bootstrap set and no more `FROZEN`:
> `partition`·`kind`·`object_id`·`slug`·`provenance`·`registry_ref`·`sot_class`."*
> Observed: `docs/constitution/record_envelope.md:§5` lists an eighth field, `tier`.
> Mismatch: an eighth envelope field is present where exactly seven are frozen.
> Consequence: universalizes a World-owned field (RMS §4: *"tier is World ontology"*) across all
> six models — the exact failure row 033's own `Why` names.

### 7.2 Prohibited finding forms

- *"This looks wrong."*
- *"This seems inconsistent."*
- *"I'm not sure this is right, but…"* presented as a finding rather than an observation.
- A finding with no file/section pointer.
- A finding whose "requirement" is the auditor's own preference (§4).

### 7.3 Insufficient evidence

If the available evidence cannot support a definite mismatch — the source is ambiguous, the
artifact's intent is unclear, or the relevant file/section cannot be located —

```
INSUFFICIENT EVIDENCE
```

is recorded as an **observation**, not a finding, and never as FAIL. **Do not promote suspicion
to finding.**

---

## 8. Requirement Traceability

For every artifact audited, the auditor builds a coverage table:

| Requirement | Source | Applicability | Artifact Evidence | Verdict |
|---|---|---|---|---|
| *(one row per requirement discovered per §6.2)* | Blueprint §/RMS §/invariant/Spine law/Roadmap field/Artifact 003 C-# | applies / does not apply | file:section or "absent" | PASS / FAIL / N/A + reason / UNVERIFIABLE + reason |

### 8.1 Mandatory rows

- Every clause of the target artifact's own `Val` (split into separate rows if `Val` states
  multiple conditions, as most manifest entries do).
- The artifact's `Done` condition.
- Every `BP` and `RMS` citation on the artifact's manifest row.
- Every applicable Artifact 003 conformance requirement (C-1…C-12), if the artifact is itself a
  manifest entry with its own metadata block.
- Every RULE G/G2/G3 boundary question relevant to the artifact's granularity.
- Every requirement surfaced by the discovery procedure at §6.2.
- The artifact's `Req` (`BR-nn`) ID — **always UNVERIFIABLE**, per §8.3.

### 8.2 Verdict values in the table

- **PASS** — evidence demonstrates the requirement is satisfied.
- **FAIL** — evidence demonstrates the requirement is not satisfied; produces a Finding (§14).
- **N/A + reason** — the requirement genuinely does not apply to this artifact (state exactly
  why — e.g., "artifact is `T: doc`, Pass 9 Implementation Correctness N/A").
- **UNVERIFIABLE + reason** — the requirement cannot be checked with available evidence or
  available authority (state exactly why).

**`UNVERIFIABLE` is never `PASS`.** An unverifiable requirement is recorded, carried into the
report's Unverifiable Items section (§14.1), and does not contribute to a PASS verdict — but it
also does not by itself force PATCH REQUIRED or BLOCKED unless the artifact's own compliance
cannot be determined without it (in which case, §13, the audit is BLOCKED on that specific
question).

### 8.3 The requirement register gap (GAP-C)

Per Artifact 003 §13 and CLAUDE.md's "Requirement Register" section: the Roadmap states `Req`
IDs (`BR-nn`); the authoritative text defining each ID is **not currently available**. The
auditor:

- preserves the `Req` ID exactly, never paraphrasing or inventing its text;
- marks its traceability row `UNVERIFIABLE — requirement register unavailable (GAP-C,
  non-blocking)`;
- verifies the artifact instead against its `BP`/`RMS` citations and its own `Val`/`Done`, which
  is the substitute verification path Artifact 003 itself states.

---

## 9. Severity

*(AUDIT PROCEDURE. This five-tier scale is HHTECH's own, built to carry the source's own
severity signals — the Spine's Severity Floor (Law 7), the `Risk` field vocabulary
(`low`/`medium`/`high`/`CRITICAL`/`HINGE`/`CRITICAL HINGE`, Artifact 003 §24), and the
historical audit's own P1-defect notation (Roadmap §0.1) — without replacing any of them. The
`Risk` field describes an **artifact's** exposure if it is wrong; **Severity** describes **a
finding's** weight. They are never conflated.)*

| Severity | Meaning | Condition | Effect on verdict |
|---|---|---|---|
| **P0** | Constitutional / blocking | Violates a Spine law; contradicts a `FROZEN` invariant or RMS closure; violates an anti-ordering (X-01…X-22); breaches a canonical-data gate rule (Roadmap PART X); reintroduces retired Canon Object Model architecture (Roadmap §0.3, CLAUDE.md "No COM Terminology") | Verdict cannot be PASS. Blocks the artifact and anything whose own compliance depends on this one. |
| **P1** | Artifact-breaking | The artifact's own `Val`/`Done` is not met; a cited `BP`/`RMS` clause is contradicted; a hard dependency (`H`), lockstep (`LS`), or gate (`G`) is violated; scope has expanded into a declared downstream artifact's territory | Verdict = PATCH REQUIRED. Artifact cannot be marked complete. |
| **P2** | Structural / drift | Source-supported but non-blocking: an Artifact 003 conformance requirement (C-1…C-12) is not met; a regression against a prior-accepted artifact that does not itself violate a P0/P1 rule; an unrecorded conflict discovered between sources, not yet classified NON-BLOCKING | Verdict = PATCH REQUIRED, unless the finding is itself a recorded, source-classified non-blocking item (§1.6), in which case it is downgraded to INFO with the classification cited. |
| **P3** | Precision / clarity | Wording imprecision; a loose but not-incorrect citation; a `Val` that is technically checkable but weak; terminology drift not yet reaching current-architecture status | Does not by itself block PASS. Three or more P3 findings against the same requirement may be escalated to P2 by the auditor, with the escalation reason stated. |
| **INFO** | Observation | A `NOT SPECIFIED BY AUTHORITATIVE SOURCE` gap; an already-recorded non-blocking conflict; a legitimate implementation choice inside an open boundary (RMS `BOUNDARY-NAMING`/`PROPOSED`, I-106/I-107) | Never affects verdict. Recorded for traceability only. |

**P0 discipline.** P0 is used only when the auditor can name the exact Spine law, `FROZEN`
invariant, anti-ordering ID, or canonical-gate rule violated. **"This seems very important" is
not a P0 justification.** If the auditor cannot name the specific source clause, the finding is
at most P1, or is not yet a finding (§4).

---

## 10. False-Positive Control

Before any finding is written, the auditor works through this checklist in order:

1. **Source read before finding.** The relevant source section has actually been read in this
   audit session, not recalled from memory or from a prior report.
2. **Requirement is authoritative, not procedural.** Confirmed per §4.
3. **In scope.** Confirmed per §3.2 — the finding is about *this* artifact's own declared
   responsibility, not an upstream or sibling artifact's.
4. **Preference vs. violation.** The source states a MUST/MUST NOT the artifact actually
   violates — not merely a different valid way of doing something the source leaves open.
5. **Deduplication.** The same root cause is not split into multiple findings. One finding, one
   root cause, with every affected location listed as evidence under it.
6. **Insufficient evidence vs. confirmed defect.** If the evidence does not clearly establish the
   mismatch, it is `INSUFFICIENT EVIDENCE` (§7.3), never FAIL.
7. **Ambiguity vs. violation.** If the *source itself* admits two readings, that is
   `NOT SPECIFIED BY AUTHORITATIVE SOURCE` or a source conflict (§1.6) — never a violation of
   the reading the auditor happened to prefer.
8. **Open boundary vs. frozen boundary.** A model's stated-open interior (RMS `BOUNDARY-NAMING`/
   `PROPOSED`, Blueprint §34.1's "boundaries frozen, interiors not") is not held to the same
   standard as a `FROZEN` one. A design choice inside an open interior is not a defect merely
   for being one choice among several the source has not yet closed.

A finding that fails any of these eight checks is downgraded to an observation, or not recorded
at all.

---

## 11. Test Audit

*(Applies whenever the artifact has, or should have under RULE G2, associated tests.)*

The auditor checks:

1. **Does each test assert the artifact's actual `Val`?** A test that asserts something else,
   or asserts a weaker condition than `Val` states, does not prove the artifact.
2. **Positive and negative cases.** Per Roadmap PART XI, *"Negative testing is first-class:
   every anti-ordering has an artifact proving rejection."* A test suite proving only the
   accepted case, with no test proving the rejected case, is incomplete.
3. **Boundary cases.** Per §13 Pass 13 above.
4. **Rejection behavior.** Where the artifact is a validator, deny-hook, or refusing command, is
   the actual refusal exercised (not merely the happy path)?
5. **Regression.** Does the test suite still cover what it covered before the current change?
6. **False-pass risk.** Could this test pass against a *wrong* implementation? Look for:
   tautological assertions, mocked-away real behavior, assertions weakened to fit an
   implementation rather than the implementation fixed to fit the requirement (this is also a
   Pass 12 Regression finding if it happened across a diff).
7. **Behavior vs. implementation detail.** Does the test verify observable behavior the `Val`
   names, or only an internal implementation detail that could change while the real behavior
   silently breaks?

**A green test suite is not, by itself, evidence of compliance.** Per Roadmap PART XV and
Artifact 003 §21 Rule 5: *"generating a test is not running it."* The auditor confirms the tests
were actually executed (via the diff, the session record, or by running them if the audit
context permits) before treating a green result as evidence.

---

## 12. Diff Audit

The auditor inspects `git diff` and `git status` and checks:

1. **Intended vs. actual changed-file set.** Does the diff touch exactly the target artifact's
   declared `path` (and its declared RULE-G3 companions, if any) — or does it also touch
   unrelated files?
2. **Unrelated files.** Any file outside the artifact's scope is reported, even if its content
   looks harmless — CLAUDE.md: *"Do not modify files outside the current artifact's scope."*
3. **Scope expansion.** Does the diff implement something beyond the current artifact's `Val`?
4. **Accidental deletion.** Anything removed that was not the intended target.
5. **Accidental weakening.** A MUST loosened to a MAY, a refusal removed or narrowed, a check
   disabled — cross-referenced against Pass 12 Regression Analysis.
6. **Test changes.** Were tests changed to match a new (correct) requirement, or weakened to
   pass against a wrong implementation (§11.6)?
7. **Documentation changes.** Do doc changes match the actual implementation change, or drift
   from it?
8. **Generated/derived artifacts.** Anything from `derived/**`, `fixtures/**`, or a build output
   accidentally committed as if authoritative (Roadmap PART I directory table; Roadmap PART VII
   SoT table).
9. **Zone violations.** A diff touching `canon/**` outside the Mutation Coordinator path, or
   touching a directory's `Prohibited` column per the Roadmap PART I table, is a **P0** finding
   regardless of the target artifact's own scope (Spine law 2; Roadmap artifact 022's
   canon-write-deny precedent).
10. **Hidden side effects.** Any behavior change in a file not obviously related to the stated
    purpose of the diff.

If the artifact otherwise passes but the diff contains an unrelated, risky change, **the audit
still reports it** — it does not silently disappear because the target artifact itself is
compliant.

---

## 13. Verdict Model

### 13.1 Definitions

| Verdict | Meaning |
|---|---|
| **PASS** | The audit reached full requirement coverage (§8) for this artifact, and no unresolved P0 or P1 finding remains. Any P2 findings present are either resolved or explicitly classified as recorded, non-blocking conflicts (§1.6, downgraded to INFO). |
| **PATCH REQUIRED** | At least one unresolved P0, P1, or blocking-classified P2 finding exists, **and** the audit has enough evidence to state what is wrong and, where determinable, a remediation direction (§16). |
| **BLOCKED** | The audit cannot reach a reliable verdict — a required source document or section is unavailable; a declared `H` dependency does not exist or is itself unaudited/unaccepted; an unresolved source-authority conflict (§1.6) bears directly on this artifact's compliance and cannot be classified non-blocking; or the evidence needed for a mandatory pass fundamentally does not exist (e.g., Implementation Correctness requested against an artifact with no implementation). |

### 13.2 PASS is not "no findings found"

**PASS requires demonstrated positive coverage** — every mandatory row of the traceability table
(§8.1) resolved to PASS, N/A+reason, or a non-blocking UNVERIFIABLE/INFO — not merely the
absence of a discovered defect. An audit that skipped passes, could not read a cited section, or
left rows blank does not get to claim PASS; it gets BLOCKED on the specific gap, or reports
incomplete coverage as its own finding.

### 13.3 Decision procedure

```
run all fourteen passes (§6)
        ↓
any pass could not be completed for lack of source/evidence?
        ↓ yes                                   ↓ no
   VERDICT = BLOCKED                     aggregate all findings
   (name the specific gap)                       ↓
                                     any open P0 finding?
                                          ↓ yes         ↓ no
                                  PATCH REQUIRED    any open P1 finding?
                                                         ↓ yes    ↓ no
                                                 PATCH REQUIRED   any P2 finding
                                                                  not classified
                                                                  non-blocking?
                                                                    ↓ yes   ↓ no
                                                            PATCH REQUIRED  PASS
```

---

## 14. Audit Report Contract

The report schema for `hhtech/auditreport.md`. **This standard defines the schema only. No
artifact-specific finding belongs in `audit-standard.md`.**

### 14.1 Required sections, in order

1. **Audit Identity** — report date, target repository state (commit/branch), auditor identity
   ("GPT-5.6, under `hhtech/standards/audit-standard.md`").
2. **Target Artifact** — Roadmap `ID` and `Name` if applicable; exact path(s); or "non-manifest
   file" with a stated reason if the target is outside the 490-artifact set.
3. **Audit Mode** — Full Artifact Audit / Diff Audit / Post-Patch Re-Audit (§5).
4. **Source Set** — exact files and sections read, each with the read confirmed.
5. **Scope** — in-scope items (§3.1) and explicitly out-of-scope items (§3.2), with the artifact
   they actually belong to named.
6. **Executive Verdict** — PASS / PATCH REQUIRED / BLOCKED, with a one-paragraph rationale.
7. **Requirement Coverage** — the full traceability table (§8).
8. **Findings** — one row per finding: stable ID (§14.2), Severity (§9), Source Requirement,
   Evidence, Impact, Remediation Direction (or "NOT DETERMINED — requires HUMAN DECISION").
9. **Evidence** — the raw quoted excerpts backing each finding, kept minimal and pointer-based.
10. **Regression Analysis** — the Pass 12 output: what was compared, what (if anything)
    weakened.
11. **Diff Analysis** — the Pass 11/§12 output: changed-file set, unrelated changes, risk notes.
12. **Unverifiable Items** — every `UNVERIFIABLE + reason` row, always including the target
    artifact's own `Req` ID per §8.3.
13. **False-Positive Checks** — confirmation the §10 checklist was applied, and a list of any
    suspicion downgraded to observation rather than promoted to finding.
14. **Final Verdict** — restated, with an explicit list of what must change to move from PATCH
    REQUIRED or BLOCKED to PASS.
15. **Re-Audit Requirements** — what must be re-checked, and under which mode (§5), after
    remediation.

### 14.2 Finding ID scheme

*(AUDIT PROCEDURE.)* Format: `AUD-<artifact-ID-or-slug>-<NN>`, e.g., `AUD-039-01`. Assigned once,
at first occurrence of a distinct (artifact, requirement, location) tuple. **IDs are never
reused for a different defect and never renumbered across re-audits.** A finding whose defect is
resolved has its ID **retired**, carrying an `Outcome` of `CLOSED` (§15) — it is not deleted and
its number is not given to a new, unrelated finding.

---

## 15. Re-Audit Rules

After a patch has been applied, a Post-Patch Re-Audit (§5.3) follows these rules exactly:

1. **Current files are authority.** The repository state as it exists right now is what is
   checked — not the patch's own description of what it did.
2. **Current git diff is authority.** The diff since the pre-patch baseline is inspected fresh
   (§12), not assumed from the patch's summary.
3. **Previous audit is historical context only.** It tells the auditor which findings existed
   and their IDs. It does not tell the auditor whether they are resolved.
4. **Every prior open finding is individually re-verified** against current evidence — the
   auditor re-runs the specific check that produced the finding, on the current file, and
   records fresh evidence.
5. **A finding is CLOSED only when current evidence demonstrates the requirement is now
   satisfied.** Not because a patch description says so.
6. **A finding is REOPENED-REGRESSION if it was previously marked CLOSED (in an even earlier
   re-audit) and current evidence shows it has returned.**
7. **A patch that introduces a new defect opens a new finding**, with a new ID (§14.2) — it is
   never folded into an old finding's ID even if the topic is related.
8. **Never keep a finding open solely because history said it was once wrong.** If current
   evidence resolves it, it is CLOSED, regardless of how the prior audit read.
9. **Never close a finding solely because a patch's own report claims success.** Claimed
   completion is not evidence (mirrors CLAUDE.md: *"File creation alone is not evidence of
   completion"*).

Each finding in a re-audit report's Findings table (§14.1 item 8) carries an additional
`Outcome` column: `CONFIRMED-OPEN` / `CLOSED` / `REOPENED-REGRESSION` / `SUPERSEDED` (the
requirement it traced to no longer applies, stated with reason).

---

## 16. Patch Boundary

This standard requires the auditor to state a **remediation direction** at the level of: which
requirement is unmet, and in general terms, what category of change would satisfy it (e.g.,
*"the `Val`'s seven-field enumeration must be restored to match RMS §4's frozen seven fields;
the eighth field must be removed or reclassified as model-owned"*).

**This standard does not specify exact wording, exact diffs, or patch mechanics.** That belongs
to `hhtech/standards/patch-standard.md`, which this task does not create or modify. An audit
report is not a patch prompt.

---

## 17. Negative Audit — Full Reference

*(Expands §6 Pass 14. Every item below is a category the auditor actively searches for; every
finding it produces must still satisfy §4 — trace to an authoritative requirement or a stated
boundary, never asserted on its own.)*

| Category | What to look for | Authoritative anchor |
|---|---|---|
| Forbidden behavior / bypass | A second write path to canon; a route around the Mutation Coordinator | Spine law 2 (One Path); anti-orderings X-07, X-11 |
| Silent fallback / unsafe default | A failure that proceeds instead of stopping and explaining | P-19 (fail closed toward truth) |
| Missing validation | A claim of well-formedness or correctness with no actual check | LS-4 (Constraint ↔ Validation-Rule ↔ Validator never collapsed); RMS §20 |
| Accidental permissiveness | A refusal/deny check with a gap that admits what it should reject | P-24 (structural violations block); the artifact's own `Val` |
| Hidden scope expansion | Work belonging to a later phase or a named downstream artifact, built early | CLAUDE.md "While I am here, I will also build… is PROHIBITED"; RULE G3 |
| Contradiction | Two authoritative statements, or two parts of one artifact, disagreeing | §1.6, §6 Pass 6 |
| Unsafe default | A default value or behavior that violates a MUST when unconfigured | P-19; the cited requirement the default violates |
| Test-only compliance | Behavior that only holds inside a test harness, not in the actual path | §11.6 false-pass risk |
| Dead/unused enforcement | A validator or deny-hook that exists but is never invoked in the real path | P-10 ("every signal has a consumer") |
| Implementation exists but not wired | Code present, but not registered/called/reachable | trace via the artifact's own integration points named in `Val`/`Done` |
| Doc says X, code does Y | Specification and implementation diverge | Pass 9 Implementation Correctness; RULE G lockstep custody |

---

## 18. Verification Checklist (Operating Discipline for the Auditor)

Before submitting an audit report:

- [ ] Every claimed source citation was actually read in this session (§1, §6.2).
- [ ] Every finding passed the §10 false-positive checklist.
- [ ] Every finding has evidence in the §7.1 shape.
- [ ] Severity was assigned per §9's conditions, not by impression.
- [ ] The requirement traceability table (§8) covers every mandatory row (§8.1).
- [ ] No `UNVERIFIABLE` row was scored as PASS.
- [ ] The `Req` (`BR-nn`) row is present and marked UNVERIFIABLE per §8.3.
- [ ] Diff Audit (§12) and Regression Analysis (§6 Pass 12) were both run.
- [ ] The verdict follows the §13.3 decision procedure exactly.
- [ ] For a re-audit: every prior finding has a fresh `Outcome` per §15.
- [ ] No placeholder text, no "TODO", no deferred section, appears anywhere in the report.
- [ ] No requirement was invented; every `NOT SPECIFIED BY AUTHORITATIVE SOURCE` gap is recorded
      as such rather than silently treated as compliant or as a defect.

---

*This document governs audit procedure only. It carries no architectural authority, defines no
Record Model, and amends nothing in the Master Blueprint, the Record Model System, or the OS
File Build Roadmap. Where it and they differ, they are right and this document is wrong.*
