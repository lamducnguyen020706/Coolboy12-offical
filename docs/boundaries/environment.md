# COOLBOY12 — Environment Boundary

**Artifact 014** · `docs/boundaries/environment.md` · Own: CONST · RM: n/a · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d ·
Req: BR-06 · BP: §9.5 · RMS: n/a · H: 003 · S: — · LS: — · G: — · → 015 · Risk: low · ∥: yes

## 1. Purpose

This document answers one question: **what may the execution environment do, and what may it
never own?**

It exists because leaving the answer unstated is what allows tooling to be mistaken for
structure (§9.5). A future implementer reading only this file MUST be able to tell which side
of the boundary any given capability falls on.

This is a boundary contract. It defines no Record Model, no schema, no kind roster, and no
mutation mechanism. Where this document and the Blueprint differ, the Blueprint governs.

## 2. Governing Rule

> **P-33 — The environment runs the system; it does not define it.**

I-100 states the same rule as an invariant:

> The execution environment runs coolboy12 and does not define it. It is not a domain,
> partition, engine, or primitive, and it owns no coolboy12 semantics. Its guard rails are
> defence-in-depth; where a guard rail and the Human Gate disagree, the gate governs. The
> architecture must remain valid when the environment is replaced.

Four prohibitions follow (§9.5), and all four are constitutional:

1. **The environment is not a domain.** It fails the Domain Admission Criterion (§9.3) at
   question 1: it owns no question about the world or the work.
2. **The environment is not a partition, an engine, or a primitive.** Partitions classify
   records; the environment holds none. Primitives are constitutionally fixed at two, and both
   are coolboy12's own.
3. **The environment owns no semantics.** It MAY *execute* a validator; it MUST NOT *define*
   validity.
4. **The environment is replaceable.** See §15.

The environment MUST NEVER be described as a domain, a partition, an engine, a primitive, a
Record Model, or a semantic authority. There is no "Environment Model" and no environment
Record.

## 3. Environment Position

The ordering is fixed (§9.5). Read downward, each layer serves the one below; read upward,
each layer is *constrained* by the one above.

```
AUTHOR
  ↓  states intent, decides, gates
AI-ASSISTED DEVELOPMENT
  ↓  proposes, drafts, implements, tests
EXECUTION ENVIRONMENT
  ↓  filesystem, commands, runtime, version control, role-scoped reasoning
COOLBOY12 SYSTEM
  ↓  the nine domains, six partitions, two primitives, ten laws
EXTERNAL CAPABILITY COMPONENTS  (behind adapters, §26.3a)
```

The environment sits **above** coolboy12 and **outside** it. **It is the workshop, not the
building.** Any design that inverts this ordering has made the tooling the architecture (P-33).

## 4. What the Environment Provides

The following ten facilities are what §26.8 establishes. No further constitutional facility
exists, and none MAY be added here.

| Facility | It MAY | It MUST NOT |
|---|---|---|
| **Workspace / repository** | Hold the project tree: native source, Registry definitions in legible files, canonical records, adapters, prompts, tests, configuration | Make a path's location the source of its authority |
| **Filesystem access** | Read and write project files under the permission boundary | Turn a write permission into canonical authority (§10) |
| **Command execution** | Run validators, index builds, simulation runs, rendering, and tests | Define what makes a canonical Record valid |
| **Runtime and packages** | Provide the language runtime and the audited external components of §26.3a | Let any package hold semantics (§12) |
| **Version control** | Record file history, rollback, commit identity, integrity | Become a second History or a canonical truth system (§11) |
| **Code generation and editing** | Produce AI-assisted implementation of native coolboy12 code | Make generated code authoritative because it was generated |
| **Role-scoped reasoning** | Execute the AI coworker roles of §21 as configured contexts under the single-substrate rule (P-15) | Give a role authority the author has not gated |
| **Hooks** | Enforce deterministic pre-action checks | Act as constitutional authority (§13) |
| **Commands** | Provide repeatable entry points for recurring work: propose, validate, simulate, render, rebuild | Constitute a second write path |
| **Persistent files** | Carry project conventions, invariants, and standing instructions across sessions | Become canon by persisting |

**The workspace layout follows the architecture, not the tooling** (§26.8). Canonical records
live in legible files organised by partition; derived stores live where they can be deleted in
their entirety and rebuilt; adapters sit at named boundaries. A reader opening the tree without
the environment can still read the world (P-27).

**Local-first, on demand.** Nothing runs unattended. There is **no scheduler, no daemon, and no
background advance of the world** (§26.8, §28 AC-2). The system is operated in sessions. This
contract admits no autonomous, always-on, or unattended operation.

## 5. What the Environment May Write

The environment **MAY write**, as ordinary development activity (§26.8):

- native source
- tests
- adapters
- prompt and role files
- staged proposals
- development and configuration files within their own ownership boundaries

**These are development writes. They create no semantic authority.** Writing a file that
describes a Record does not make the file a Record. Writing a validator does not make the
validator's opinion true.

Under the permission boundary (§26.8): canonical records and Registry definitions are
write-protected against direct edit; derived stores are freely writable because they are
rebuildable by definition; proposals are freely writable because nothing in a proposal area is
canon until it passes the gate.

## 6. What the Environment May Propose

The environment **MAY propose** (§26.8): canon mutations · issue plans · drafts · material
specifications · simulation scenarios.

> **Propose is not commit.**

The environment MUST NEVER be described as the authority that canonizes a proposal. Every
proposal carries a basis stamp naming the canonical state it was computed against (P-22), and
every canonization remains subject to the Human Gate and the mutation path of §9. The author
**must review** every canonization, every Registry change, every reality anchor, every promoted
simulation result, and every published artifact (§26.8).

## 7. What the Environment Must Never Own

Stated in the Blueprint's own terms (§26.8), and not to be softened into generic language about
tooling and business logic. The environment NEVER owns:

- **Canon**
- **the Registry**
- **Simulation semantics**
- **Epistemic semantics**
- **Production semantics**
- **Visual Library semantics**
- **Issue semantics**
- **Governance semantics**
- **the mutation boundary**
- **the Human Gate**

**The environment runs coolboy12; it does not define coolboy12** (P-33). Every one of those is
native by construction (§26.2).

Separately, and specifically as **canonical or semantic mutation**, the environment **may never
directly change** any Record · Relationship Record · History Record · WSV · WSV-H · Registry
definition · epoch baseline · or published artifact (§26.8). It MAY assist with the
implementation and the execution that surround those objects. It MAY NOT bypass the governed
path that changes them.

## 8. Six Record Models

The Record System holds **six sovereign Record Models — not six configurations of one model**
(§13.0). The environment owns the semantics of none of them.

| Code | Model | The question it alone answers |
|---|---|---|
| **W** | World | What is true of the world? |
| **E** | Epistemic | Who knows, believes, suspects, or has been shown what? |
| **P** | Production | What is intended, planned, coordinated, and in production? |
| **R** | Registry | What does the system mean, and how are Record semantics defined? |
| **V** | Visual | How is World Truth visually specified and represented? |
| **I** | Issue | What was published, and how is that publication composed? |

These six are the complete roster. There is **no seventh model**, no universal model above
them, and no model that is a specialization of another (I-101).

They MUST NOT be described as modules of an editor, plugin types, folders owned by tooling,
configurations of one universal object, or environment-managed schemas. The environment
provides only the facilities in which their implementation is developed and executed.

This section lists the six to establish what the environment does not own. It defines no
schema, no kind roster, and no field list for any of them.

## 9. Canonical Mutation Path

> **The Mutation Coordinator is the only thing in coolboy12 that writes canon** (§12.6, I-83).

The canonical write path, in the Blueprint's own terms:

```
PROPOSAL  (author intent, carrying its basis stamp — P-22)
    ↓
validation
    ↓
Human Gate
    ↓
Mutation Coordinator
    ↓
canon
```

Spine law 2 states the same path as its full stage sequence: *propose → check → human gate →
commit → changelog → log*. No other route exists, and the commit is atomic (§12.6).

What this means for the environment:

| The environment | Status |
|---|---|
| MAY generate and edit implementation | permitted |
| MAY create proposals | permitted |
| MAY execute the Mutation Coordinator | permitted |
| MAY NOT bypass the Mutation Coordinator | **prohibited** |
| MAY NOT directly mutate Canon | **prohibited** |
| MAY NOT directly mutate Registry definitions | **prohibited** |
| MAY NOT directly alter History Records | **prohibited** |
| MAY NOT replace the Human Gate | **prohibited** |

**External components may implement individual stages** — a validation engine may run schema
checks, an indexer may rebuild projections, a version-control system may record the commit.
**None of them may redefine authority. A stage may be delegated; the boundary may not** (§12.6).

## 10. Filesystem vs Semantic Authority

These two are different things and MUST NEVER be conflated:

| | |
|---|---|
| **Filesystem write capability** | A mechanical permission. The operating system will let the bytes land. |
| **Canonical mutation authority** | A constitutional status. Only the Mutation Coordinator holds it, and only past the Human Gate. |

The environment MAY hold permission to write a file at the filesystem level. That does **NOT**
give it authority to make that file a canonical Record. A file's path, its permissions, and its
presence in the repository decide nothing about its authority, its canonicality, or its
source-of-truth class — those are three separate questions, and none of them is answered by the
filesystem.

Write-protection of canonical paths is the deterministic expression of Spine law 2 (§26.8). It
is a safeguard against accident, not the reason canon is canon.

## 11. Version Control Boundary

Artifact 013 governs this boundary in full — see [`version_control.md`](version_control.md).
It is not restated here. The part that binds the environment:

Version control records **that files changed**, commit identity, repository history, and
rollback and integrity information. It does **NOT** determine what changed canonically, whether
a canon mutation is valid, semantic truth, Record authority, or canonical History.

The environment provides version control as a facility (§4). Providing it grants the
environment nothing that version control itself does not hold — which, semantically, is nothing
(§26.2e, I-85).

The boundary chain is: **013 version control → 014 environment → 015 secrets and
configuration.** Artifact 015 is not defined here.

## 12. External Dependency Boundary

> **P-31 — Dependencies provide capability, never authority.**

No external component — database, index, graph store, search engine, workflow engine, renderer,
or version-control system — may hold canonical semantics, define a kind, own a relationship,
adjudicate a mutation, or be the only place a canonical fact exists (P-31). Every external
component sits behind an adapter, declares an exit path, and is deletable. Every external store
is DERIVED or CACHED, never AUTHORITATIVE (I-84).

As a practical rule:

| The component | Provides | Does not decide |
|---|---|---|
| A storage engine | storage and retrieval | what a World Record means |
| A version-control system | repository history | what canonical History is |
| A test runner | execution of a check | whether the invariant is true |
| An index or search engine | lookup over derived data | what is canonically the case |
| A renderer | page images from the artifact model | what was published, or what it composes |

**The architecture must remain meaningful when every dependency name is removed from it**
(§29.7). A rule phrased in a component's vocabulary rather than coolboy12's has already failed
that test.

## 13. Hooks and Guard Rails

The environment's own guard rails are used, and are used as **defence-in-depth, never as
constitutional authority** (§26.8, §12.6, I-83).

Hooks **MAY**: deny direct writes to protected paths · enforce deterministic checks · prevent
accidental violations · provide operational safeguards.

```
Hook ≠ Constitution
Hook ≠ Human Gate
Hook ≠ Mutation authority
```

A guard rail can be misconfigured, bypassed, or removed by whoever holds the configuration.
**The Human Gate cannot, because it is a person** (§12.6).

> **If a hook and the Human Gate disagree, the gate is right and the hook is a bug.**

This is not a tie between two authorities. It is one authority and one safeguard. The safeguard
loses.

## 14. Recovery and Rebuild

The environment may be rebuilt. After dormancy or failure (§26.8):

```
runtime and packages   →  reinstalled
derived stores         →  rebuilt from canon (§29.8)
parked workflows       →  resumed with every basis revalidated (§23.4)
```

The architectural point:

```
the environment may disappear
        ↓
derived environment state is rebuilt
        ↓
canon survives
```

**Canon requires no recovery, because it was never held anywhere that could fail** (§26.8,
P-27). The environment MUST NEVER be described as the durable owner of canonical state. Nothing
that can only be recovered by restoring the environment was canonical to begin with.

## 15. Replaceability Test

The test, applied to this layer (§9.5 point 4, §26.8, §29.7):

> **The environment is replaceable.** coolboy12 could be built in a different environment, or by
> hand over a longer period, and the blueprint would be unchanged. That is the test — and it is
> the anonymisation test (§29.7) applied one layer up.

Restated for this document: if the execution environment were replaced, coolboy12's architecture
and semantic ownership would remain valid. Run it by removing the environment's name from the
architecture. What must still stand:

- the six Record Models — W, E, P, R, V, I
- Canon
- the Registry
- the Mutation Coordinator
- the Human Gate
- semantic authority
- source-of-truth boundaries

All seven survive, because none of them is defined by the environment. The environment may be
replaced by a different development and execution environment, or the system built by hand over
a longer period, and the architecture would be unchanged (§9.5).

The Blueprint names a current execution environment because one exists today. **That naming is
descriptive, not architectural.** It MUST NEVER be read as "this environment is architecturally
required", and no environment MAY be made a semantic dependency of coolboy12.

## 16. Forbidden Inversions

Each of these is a real failure mode, and each is prohibited.

**Inversion A — treating the environment as the definer of Canon.**

```
WRONG     execution environment  →  defines Canon
CORRECT   execution environment  →  implements and operates  →  coolboy12 Canon authority
```

**Inversion B — treating repository history as canonical History.**

```
WRONG     version-control history  →  defines canonical History
CORRECT   coolboy12 canonical History  →  exists under its own semantic authority
          version control             →  records file and repository changes only
```

**Inversion C — treating filesystem access as mutation authority.**

```
WRONG     filesystem access  →  canonical mutation authority
CORRECT   filesystem access     →  mechanical capability
          Mutation Coordinator  →  canonical mutation path
```

**Inversion D — treating an external component as the definer of meaning.**

```
WRONG     external database  →  defines Record meaning
CORRECT   Record Model  →  defines meaning
          database      →  stores and retrieves mechanically
```

## 17. Validation and Acceptance

This document is accepted when every answer below holds on inspection of the document itself.

| # | Question | Required | Where |
|---|---|---|---|
| 1 | Can the execution environment define a Record Model? | **NO** | §2, §8 |
| 2 | Can it create canonical truth by editing a file? | **NO** | §5, §10 |
| 3 | Can version control define canonical History? | **NO** | §11 |
| 4 | Can a database define Record semantics? | **NO** | §12 |
| 5 | Can a hook override the Human Gate? | **NO** | §13 |
| 6 | Can an external dependency become semantic authority? | **NO** | §12 |
| 7 | Can the architecture survive replacement of the environment? | **YES** | §15 |

The Roadmap's own criteria for Artifact 014:

- **Val** — *names what the environment may never own* — §7.
- **Done** — *six models + mutation path listed* — §8 and §9.

## Boundary of This Document

This document declares a boundary. It implements nothing: no hook, no permission code, no
Mutation Coordinator, and no runtime. The Mutation Coordinator named throughout is Roadmap P5
and **does not yet exist**; the rules here are current operational rules and the mechanism
arrives later. Nothing here defines a Record Model, a schema, a kind roster, or a mutation
mechanism, and nothing here creates a new domain, partition, layer, or model.

`Req: BR-06` is preserved as written. The requirement register is not currently available
(Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here; this
document is validated against its Blueprint citations instead.
