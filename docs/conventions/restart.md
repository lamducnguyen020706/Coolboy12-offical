# COOLBOY12 — Restart / Recovery Conventions

**Artifact 019** · `docs/conventions/restart.md` · Own: OPS · RM: n/a · T: doc · R: CONTRACT ·
SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d · Req: BR-104 ·
BP: §28.1 · RMS: n/a · H: 003 · S: — · LS: — · G: — · → 454 · Risk: medium · ∥: yes

## 1. Purpose

This document answers one question: **the system has been dormant for a long time — what must
happen before work can safely resume?**

It fixes the P0 cold-restart contract: an end-to-end, source-faithful sequence for returning
from dormancy, and the guarantees that make the sequence trustworthy. It is a convention, not a
mechanism. Nothing here runs.

## 2. Scope

This document governs **the restart contract only**. It is deliberately upstream of, and
narrower than, the operational architecture the Roadmap builds at P17:

| Roadmap artifact | What it owns | Relationship to 019 |
|---|---|---|
| **454** system dormancy specification | the full P17 dormancy model — what persists, what expires, what must be reconstructed | specializes this contract; not built here |
| **455** recovery snapshot model | the snapshot schema and lifecycle | not built here; no schema is defined in this document |
| **456** the Return Briefing | the actual briefing, reconstructed from Creative Memory + Context Builder + canon | not built here; §28.2's briefing order is named, not implemented |
| **457 / 458** degraded modes | the mode taxonomy and its enforcement | not built here; this document never defines a mode |
| **477** drill — restart after dormancy | the operational proof that restart works | not built here; this is the convention it will exercise |

RMS is `n/a` for this artifact and is not cited as an authority below.

## 3. Dormancy Is Expected

> **P-11 — Recoverable after years.** The system is resumable after a dormancy of up to three
> years within a handful of sessions. Dormancy is expected, not failure.

Blueprint §28 restates the same posture: *"Dormancy is expected, not failure (P-11)."* Nothing
in this document treats a long absence as an error condition. This does not prohibit later
artifacts from defining specific failure conditions encountered during restart or recovery.

## 4. The Cold-Restart Guarantee

Blueprint §28.1 states the problem precisely: over three years *"the reasoning substrate will
have changed or vanished, adapters will have broken, formats will have aged."* The question a
returning session must answer is not *what was I doing* but **does this still run, and is my
universe still readable.**

Three guarantees answer it, reproduced from §28.1 without weakening:

1. **Canon survives the system** (P-27, §26.3) — canon, History Record, WSV-H, Production
   State, and Creative Memory are legible without the application, so the worst case is a
   rebuild of tooling around an intact universe — never a lost world.
2. **Every adapter has a declared exit path**, so a discontinued service is a migration, not a
   catastrophe.
3. **No guarantee depends on the substrate** (P-20).

## 5. "Cold Restart" — the Operational Term

The Blueprint does not use the exact phrase *"cold restart."* Roadmap row 019 requires one
("cold restart described end-to-end"), so this document fixes the operational meaning the term
must carry to satisfy that requirement — stated as an interpretation, not a constitutional term
the source coined.

**A cold restart is a restart in which the previous in-memory or runtime process state is
assumed gone**, and the environment and tooling must be re-established from durable, persisted
project state. Concretely:

```
previous runtime memory     — NOT trusted; assumed absent
durable authoritative state — trusted, according to its own architecture
```

This document does not require an OS reboot, a container semantics, a process model, or a
specific package command. Those are Artifact 014's territory (environment) and are not repeated
here.

## 6. End-to-End Cold Restart Sequence

This satisfies the Roadmap's Val, *"cold restart described end-to-end."* Every step traces to a
cited source; no step is a later artifact's responsibility performed early.

```
1.  Re-establish an executable environment
        (Artifact 014 — the environment is recreated; it defines nothing)
        ↓
2.  Verify authoritative persisted state is readable
        (P-27: canon, History Record, WSV-H, Production State, Creative Memory
         are legible without the application)
        ↓
3.  Re-establish available external dependencies through their adapters
        (§28.1: every adapter has a declared exit path — a missing one is a
         migration, never a lost zone; Artifact 015 — no secret persists through
         this step)
        ↓
4.  Rebind the reasoning substrate currently available
        (P-15: exactly one substrate bound at a time; P-20: no guarantee depends
         on which one)
        ↓
5.  Rebuild rebuildable Derived state as required
        (Artifact 016 — DERIVED/CACHED are rebuilt from AUTHORITATIVE sources;
         §29.8's rebuild-from-canon drill is the operational form of this rule.
         Artifact 020 owns the rebuild method itself)
        ↓
6.  Identify parked or unfinished workflows
        (§23.4: a workflow parked in March is resumable in September)
        ↓
7.  Revalidate every required basis before resuming anything
        (P-22 basis stamps; §23.4: "every basis re-validated on resumption,
         anything stale marked before the author is asked to continue")
        ↓
8.  Resume only what a valid basis permits; report the rest as unresumable
        (§23.4: "a workflow that cannot be re-validated is reported as
         unresumable, with what changed, rather than continued on stale ground")
        ↓
9.  Surface the resulting operational state honestly
        (§28.2: "the system reports its own decay honestly: which adapters no
         longer respond, which projections are stale, and which capabilities
         are running reduced." The actual report format is Artifact 456's)
```

Nothing past step 9 is defined here. §28.2's continuity snapshot, epoch baseline, and Return
Briefing are the next layer, and Artifact 019 does not reach into them.

## 7. Canon Survives the System

Recovery runs in one direction only:

```
intact, readable canonical state
        ↓
rebuild or replace the tooling around it
        ↓
resume operations
```

**Never the reverse.** Restart is not *"restore the application, then restore the universe."*
P-27 requires canon, History Record, WSV-H, Production State, and Creative Memory to remain
human-interpretable *without* the application that produced them — *"no external dependency may
hold any of them in a form the system cannot fully recover"* (§26.3). If the application, the
environment, or the reasoning substrate is gone, canon is not endangered by that fact alone.

## 8. Rebuilding Derived State — Not the Same Contract

**Restart is not synonymous with rebuild.** Restart returns the operational system from
dormancy to a usable state; rebuild regenerates non-authoritative stores from authoritative
input. A cold restart *includes* rebuilding whatever Derived state is needed (§6 step 5) and
*includes* revalidating parked-workflow bases (§6 step 7) — but the rebuild method itself,
staleness rules, and cache-invalidation mechanics belong to **Artifact 020**, not here.

## 9. Adapter Exit and Substrate Replacement

A discontinued reasoning substrate, image service, retrieval service, renderer, or other
external dependency is a **migration problem, not a loss of universe** — §28.1's second
guarantee, stated plainly. This document does not select a vendor, define an adapter API, or
specify a migration procedure; those are §26.3's adapter architecture and each
adapter's own declared exit path.

**Substrate rebinding must be possible, and must change nothing about Canon.** P-15 requires
exactly one substrate bound at a time; the *identity* of the bound substrate is *"an adapter
binding... not a constitutional fact"* (P-15). Therefore, on restart:

- rebinding to a different substrate is permitted and expected where the prior one is
  unavailable;
- substrate disappearance never implies loss of Canon;
- changing substrate never redefines semantic authority, creates a new canon, or changes
  historical truth (P-20: *"No canonical guarantee may depend on model determinism"*).

This document does not create a fallback-model architecture or a second simultaneous
substrate — P-15 permits exactly one.

## 10. Parked Workflow Resumption

> **"The graph is durable: pausable at any node, resumable with re-validated bases, abandonable
> by Operational Rollback."** (§25.4, rule 5)

§23.4 gives the same rule for the workflow record itself: a workflow parked in March is
resumable in September, *"with every basis re-validated on resumption and anything stale marked
before the author is asked to continue."*

```
parked workflow
        ↓
revalidate its basis
        ↓
   fresh & valid  → eligible to resume
   stale          → stop, re-reason, or report unresumable — never silently continued
```

This document invents no workflow-status vocabulary beyond what §23.4 already states
(*composed → running → awaiting-author → paused → resumed → completed → abandoned*) and no
workflow-state database. It states the restart-time consequence of the rule that already exists.

## 11. No Silent Continuation

A restart must not silently continue work whose assumptions changed. This follows directly from:

- **P-19** — fail closed toward truth, fail open toward artifacts: *"nothing is committed,
  assumed, or partially applied"* when work cannot complete correctly;
- **P-22** — every proposal declares its basis, and a stale one is re-validated, never
  silently reused;
- **§15.14** — once a transition is marked stale, it is *"re-reasoned or dropped, never
  committed on the old basis."*

If a required basis is stale on restart: it is not treated as valid, it is not silently reused,
and no Canon is committed from it.

## 12. Simulation Is Not Reproducible — And Restart Does Not Require It

§15.15 states this as a property of the instrument, not a defect:

1. A simulation is not reproducible, and the system never claims it is; two runs of the same
   intent will differ.
2. A record *is* reproducible — Historical Replay reads committed history and returns identical
   results forever.
3. *"No canonical guarantee depends on reproducibility. Canon's validity rests on the gate and
   the record, not on the ability to regenerate the proposal that produced it."*

**Cold restart is not rerunning every historical simulation, and it is not reconstructing Canon
by regenerating proposals.** The system recovers authoritative state and re-establishes
operational capability; it does not require, and never claims, identical simulation outputs.

**For this artifact, the Roadmap's `Done: reproducible` criterion is satisfied by making the
documented cold-restart procedure repeatable** — the same documented sequence (§6) brings the
same authoritative persisted state back into operation, and does not depend on the identity of
any specific transient substrate. This is an implementation interpretation of the Roadmap's Done
criterion, not a constitutional definition of *reproducible* supplied by the Blueprint. It does
not mean deterministic simulation.

## 13. What Restart Must Never Do

Each of these is a real failure mode this document exists to foreclose.

- **Restart does not restore Canon from Derived.** Derived is rebuilt from Canon (§8); the
  reverse direction is not a recovery path. If Derived state is lost, it is rebuilt. If Canon is
  intact, there is no semantic recovery of Canon to perform.
- **Restart does not restore Canon from Git.** Artifact 013: a commit records that a file
  changed, never what changed canonically. Repository history may be used as operational
  file-version information; it is never a substitute for History Record or WSV-H.
- **Restart does not bypass the canonical gate or the Mutation Coordinator.** No dormancy
  duration and no urgency to resume operations creates a second write path (Artifact 017).
- **Restart does not persist secrets.** Artifact 015: secrets are EXTERNAL forever. No restart
  file, snapshot, recovery state, log, or Derived store may hold a secret value. Where this
  document mentions re-establishing external credentials at all (§6 step 3), the statement is
  deliberately generic — no provider, vault, keychain, or environment-variable schema is
  specified here.
- **For the constitutional workflow path, restart is not implemented as a permanently-running
  worker, daemon, scheduler, or background advance.** §23.4 rejects that outright: *"a
  permanently-running worker contradicts P-11 and §28... No daemon, no scheduler, no background
  advance."* This artifact does not define an unattended restart mechanism.
- **Restart does not reclassify anything.** The six source-of-truth classes (Artifact 016) are
  unchanged by dormancy: AUTHORITATIVE remains authoritative; DERIVED and CACHED are rebuilt or
  deleted and rebuilt; TEMPORARY may simply have expired; EXTERNAL is reattached as external
  capability; DEV-ENV is reinstalled as needed. No seventh class — `RESTART`, `RECOVERY`,
  `CHECKPOINT` — is created.
- **Restart does not create a new artifact role.** Artifact 018's seven roles are unchanged;
  there is no `RESTART` or `RECOVERY` role, and this artifact's own role remains `CONTRACT`
  under owner `OPS` — two independent fields, not a mapping.

## 14. Interaction With Artifacts 013–018

None of the following is restated in full; only the restart-relevant consequence is drawn.

| Boundary | Consequence for restart |
|---|---|
| **013 — Version control** | Repository history is operational file-version information only, never canonical history (§13 above). |
| **014 — Environment** | Re-establishing the environment is a prerequisite to operating again, not a semantic recovery authority (§5–6 above). A different editor, runtime, package set, substrate, or adapter must not change Canon semantics. |
| **015 — Secrets** | No secret persists through restart in any form (§13 above). |
| **016 — Source of truth** | The six classes govern what "recovers" means for each zone; restart introduces no seventh (§13 above). |
| **017 — Canonical zones** | The Mutation Coordinator remains canon's sole writer through and after restart; no urgency created by dormancy grants a bypass (§13 above). |
| **018 — Role conventions** | This artifact's own role is `CONTRACT`, owner `OPS`; no new role is introduced by this document (§13 above). |

## 15. A Long-Dormancy Scenario

Conceptual only — not a drill. Artifact 477 later proves this operationally.

```
Day 0
        ↓  system stops (P-11: expected, not failure)
Years later
        ↓  runtime changed · adapters changed · formats aged · substrate changed
Cold restart (§6)
        ↓  canonical state remains readable (§7 — never in question)
        ↓  tooling and substrate re-established (§9)
        ↓  Derived state rebuilt (§8)
        ↓  parked workflows' bases revalidated (§10–11)
        ↓  valid work resumes; stale or unavailable work is surfaced, not
           silently continued (§12–13)
```

## 16. Standing Rules

1. Dormancy itself is not treated as failure under P-11. This does not prohibit later artifacts
   from defining specific failure conditions encountered during restart or recovery.
2. Canon, History Record, WSV-H, Production State, and Creative Memory survive independently of
   the application, the environment, and the reasoning substrate (P-27, §28.1).
3. Every adapter has a declared exit path; a discontinued external dependency is a migration,
   never a lost universe (§28.1).
4. No restart guarantee depends on which reasoning substrate is bound (P-20).
5. Restart is not rebuild. Rebuild's method belongs to Artifact 020.
6. Parked-workflow bases are revalidated before any resumption; a stale basis is never silently
   reused (§23.4, P-22).
7. Simulation reproducibility is never claimed as a restart requirement (§15.15).
8. Canon is never reconstructed from Derived state or from Git history.
9. Restart never bypasses the canonical gate or the Mutation Coordinator.
10. No secret persists through restart, in any form.
11. Restart is on-demand and session-oriented; no daemon, scheduler, or background advance.
12. Restart introduces no seventh source-of-truth class and no new artifact role.
13. This document defines the P0 contract only; the full dormancy specification (454), snapshot
    model (455), Return Briefing (456), degraded modes (457–458), and drill (477) are downstream
    and unimplemented here.

## 17. Boundary of This Document

This document is a convention. It implements no recovery code, no snapshot mechanism, no
dormancy engine, no return briefing, and no degraded-mode behavior. It creates no Python file,
no CLI, no hook, no test, no database, no checkpoint format, and no dependency.

It does not define the continuity snapshot or epoch baseline that §28.2 names as the primary
recovery artifact, does not define Canon Health's report format, and does not define the Return
Briefing's actual reconstruction — all of that is Artifacts 454–456. It does not name or define
any degraded mode (Full, Reduced, Read-only, Manual ceremony, Recovery) — that taxonomy is
Artifacts 457–458, cited nowhere above as this artifact's own content.

`Req: BR-104` is preserved as written. The requirement register is not currently available
(Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here; this
document is validated against its Blueprint and Roadmap citations instead.
