# COOLBOY12 — Role Conventions

**Artifact 018** · `docs/conventions/roles.md` · Own: CONST · RM: n/a · T: doc · R: CONTRACT ·
SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d · Req: BR-01 ·
BP: §7 · RMS: n/a · H: 003 · S: — · LS: — · G: — · → 013–017 · Risk: low · ∥: yes

## 1. Purpose

This document fixes the **artifact-role vocabulary** — the legal values of the `R` field in an
artifact manifest entry — so that every later artifact selects a role from a closed set instead
of inventing one.

It is a vocabulary convention. It adds no rule about what any artifact may do.

## 2. Scope — Which "Role" This Is

COOLBOY12 uses the word *role* for two unrelated things. This document governs only the first.

| | Governed here | Governed elsewhere |
|---|---|---|
| **Artifact role** | The `R` metadata field: `ARCH` · `CONTRACT` · `IMPL` · `VALID` · `PROOF` · `SURFACE` · `GOV` | — |
| **Coworker / agent role** | — | Blueprint §21 and P16; the Registry `ROLE-BOUNDARY-DEFINITION` at Roadmap artifacts 101–102 (P3); lockstep **LS-7** pairs a coworker role with its boundary definition |

**This document defines no coworker role, no agent, no "never does" boundary, no autonomy
level, no capability, and no permission.** Those belong to artifacts that do not yet exist. The
appearance of the word *role* in Blueprint §21 does not make §21 a source for this document.

## 3. Source of the Vocabulary — Stated Plainly

The seven role tokens come from **Roadmap §0.6**, which lists them without defining them:

> **Roles:** ARCH · CONTRACT · IMPL · VALID · PROOF · SURFACE · GOV.

**Artifact 018's manifest row cites `BP: §7`. Blueprint §7 is "Design Principles" and contains
none of the seven role tokens** — verified by search: each of `ARCH`, `CONTRACT`, `IMPL`,
`VALID`, `PROOF`, `SURFACE`, and `GOV` occurs **zero times** in the Blueprint. §7 supplies the
design-principle context in which artifact conventions sit; it does not define role meanings, and
no role definition below is attributed to it.

The one-line job descriptions in §4 are **reproduced from Artifact 003 §7 · `R` — Role**, which
already fixed them against Roadmap §0.6. This document does not restate the rest of Artifact 003.
Artifact 003 remains the governing artifact/phase convention; Artifact 018 specializes the `R`
(Role) field and must remain consistent with Artifact 003.

**What is source-derived, and what is working convention.** The Roadmap fixes the seven
artifact-role values, and Artifact 003 fixes the one-line job of each. The remaining columns of
§4 — when to select a role, and what selecting it does *not* imply — state this convention's
working definitions for assigning a value to an artifact's primary responsibility. They do not
create an additional authority source or a constitutional taxonomy, and no source is cited for
them because none defines them.

## 4. The Seven Artifact Roles

Exactly seven. None may be added, renamed, merged, or split.

The **Role** and **Job** columns are source-derived (Roadmap §0.6, Artifact 003). The **Select
it when** and **Not implied** columns are this convention's working definitions, per §3.

| Role | Job (Artifact 003) | Select it when *(working convention)* | Not implied *(working convention)* |
|---|---|---|---|
| **`ARCH`** | states architecture | The artifact establishes how a subsystem, model, boundary, or mechanism is organized | Not implementation; not semantic authority conferred by being architecture |
| **`CONTRACT`** | fixes a contract others must satisfy | The artifact states what must hold, what is prohibited, or what downstream artifacts must obey | Not Canon; a contract is not canonical data |
| **`IMPL`** | implements behaviour | The artifact realizes an already-defined architectural or contractual responsibility in executable or dev-environment form | Not semantic ownership of what it implements |
| **`VALID`** | checks that something holds | The artifact detects or rejects violation of an already-defined rule | Not ownership of the rule it checks; a validator does not define the invariant |
| **`PROOF`** | proves that something holds | The artifact demonstrates that a defined architecture, contract, or behaviour was exercised | Not architecture definition; not the source of truth for the behaviour it demonstrates |
| **`SURFACE`** | exposes an entry point | The artifact is an operator-facing entry point or interaction surface | Not semantic authority; not a UI architecture |
| **`GOV`** | governs a judged question | The artifact governs a judged question about the system's operation or authored process | Not mutation authority; not a permissions model or human-roles taxonomy |

The "Not implied" column exists because a role name is suggestive, and the suggestion is not the
rule. Nothing in §5–§7 may be read as weakening it.

## 5. Role Selection

**Select the role matching the artifact's primary responsibility.**

Do not select a role from: the file extension · the directory · the implementation language ·
the owner · the SoT class · how important the artifact is · whether it happens to be governing.

Where one artifact is legitimately several files under **RULE G3** (Artifact 003 — *"multiple
files may be one artifact when they share all four of: one responsibility, one lifecycle, one
owner, one validation"*), the role follows that single shared responsibility.

**Multiple roles are declared, never inferred.** Where a manifest row itself declares two roles —
for example `IMPL,VALID` or `CONTRACT,VALID` — the artifact carries both. A later artifact
carries more than one role only when its own manifest row states them; no artifact acquires a
second role by resembling one.

## 6. Role Is One Dimension Among Several

`R` is one metadata field. It answers one question and settles no other. The manifest records
`T`, `Own`, `RM`, `SoT`, `Auth`, `Canon`, and `G` separately, and each is decided on its own.

| Field | The question it answers |
|---|---|
| `T` — Type | **What is** this artifact? (`doc` · `code` · `schema` · `test` · `fixture` · `example` · `drill` · `bench` · `config`) |
| **`R` — Role** | **What job** does it do? — this document |
| `Own` — Owner | Who authors and maintains it? |
| `RM` | Which Record Model's semantics does it carry? |
| `SoT` | Where does its authority and lifecycle sit? (Artifact 016) |
| `Auth` | `none` · `governing` · `enforcing` · `gating` |
| `Canon` | Is it canonical, and about what? |
| `G` — Gate | What must pass before it may proceed? |

**Role and Type are independent, and the manifest proves it.** `doc` artifacts carry `CONTRACT`,
`ARCH`, `GOV`, and `VALID` depending on the artifact; `code` artifacts carry `VALID`, `IMPL`, and
`ARCH`; `config` artifacts carry `SURFACE`, `IMPL`, and `VALID` (§7 gives concrete examples).
There is no `doc = CONTRACT` mapping and none may be introduced.

**Role does not set SoT.** The six source-of-truth classes are Artifact 016's, not roles, and no
role implies one. An `IMPL` artifact is not authoritative because it implements; a `CONTRACT`
artifact is not `AUTHORITATIVE` because it contracts.

**Role does not set Auth.** `GOV` the *role* is not `Auth: governing`. They are different fields
with different vocabularies, and an artifact may carry either without the other.

**Role does not set Owner — and `GOV` is the trap.** `GOV` is a value in **both** the Owner
vocabulary and the Role vocabulary, and the two are unrelated. The manifest shows both
independences directly: artifacts with `Own: GOV` carry roles other than `GOV` (artifact 025 is
`SURFACE`; 146–149 are `CONTRACT`), and artifacts with `R: GOV` sit under owners other than
`GOV` (artifact 065 is `Own: R`; 422 is `Own: E`). Where an artifact happens to carry both, that
is a coincidence of two fields agreeing, never a rule. **Read `GOV` with its field name
attached.**

**Role does not set Canon, does not create a gate, and grants no filesystem or canonical write
permission.** Write authority over `canon/**` is Artifact 017's and belongs to the Mutation
Coordinator alone; no role reaches it.

## 7. Examples From the Manifest

Drawn from actual Roadmap rows. Illustrative, not exhaustive.

| Artifact | `T` | `R` | Why that role |
|---|---|---|---|
| 003 artifact + phase conventions | doc | `CONTRACT` | fixes a convention later artifacts must satisfy |
| 013–017 the five boundary declarations | doc | `CONTRACT` | each states what a layer may never do |
| 039 Record System constitution | doc | `ARCH` | states architecture rather than a rule others satisfy |
| 037 bootstrap structural validator | code | `VALID` | checks that a defined rule holds |
| 038 P1 bootstrap conformance suite | test | `PROOF` | demonstrates the phase's requirements were met |
| 025–027 `propose`, `validate`, `rebuild` commands | config | `SURFACE` | operator-facing entry points |
| 150 Human Gate specification | doc | `GOV` | governs a judged question |

Note 039 against 013–017: both are `doc`, and the role differs because the job differs — one
states architecture, the others fix boundaries.

## 8. Non-Goals

This document does not define, and must not be read as defining: coworker or AI-agent roles ·
author, operator, or reader roles · the Human Gate's or Mutation Coordinator's role in the
architecture · role capabilities, autonomy, or permissions · `ROLE-BOUNDARY-DEFINITION` · a
role-to-owner mapping · a role gate or role-admission workflow · access control · any source-of-
truth, Canon, or write rule.

It also claims nothing about enforcement. No validator, hook, Git operation, or execution
environment checks role vocabulary today, and this document does not assert that existing
artifacts already comply. Roles are manifest metadata: they are not Canon, not Registry
definitions, and not a runtime mechanism.

## 9. Standing Rules

1. The artifact-role vocabulary has exactly seven values: `ARCH` · `CONTRACT` · `IMPL` ·
   `VALID` · `PROOF` · `SURFACE` · `GOV`. No eighth may be created; none renamed, merged, or
   split.
2. Every artifact using the `R` metadata field selects from those seven.
3. Role describes the artifact's primary responsibility, not its file kind, location, language,
   owner, or importance.
4. An artifact carries more than one role only when its own manifest row declares them.
5. Role does not determine source-of-truth class.
6. Role does not determine authority — including `GOV` the role, which is not `Auth: governing`.
7. Role does not determine owner. `GOV` is a value in both vocabularies; read it with its field.
8. Role does not determine Canon status.
9. Role does not create or satisfy a gate.
10. Role grants no filesystem or canonical write permission.
11. Artifact role is not coworker or agent role, and this document governs only the former.

## 10. Boundary of This Document

This document fixes vocabulary. It implements nothing, enforces nothing, and creates no code,
test, schema, hook, gate, Registry definition, or Canon data. It defines no coworker-role
architecture and does not anticipate Roadmap artifacts 101–102 or the P16 coworker contract.

Artifact 003 remains the artifact and phase convention; this document specializes one of its
fields and is subordinate to it. Where they differ, Artifact 003 governs.

`Req: BR-01` is preserved as written. The requirement register is not currently available
(Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here; this
document is validated against Roadmap §0.6, its own manifest row, and Artifact 003 instead.
