# COOLBOY12 — Secrets and Configuration Boundary

**Artifact 015** · `docs/boundaries/secrets.md` · Own: CONST · RM: n/a · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d ·
Req: BR-06 · BP: §9.5 · RMS: n/a · H: 003 · S: — · LS: — · G: — · → 021 · Risk: medium · ∥: yes

## 1. Purpose

This document answers one question: **what counts as secret material, and what may never
happen to it?**

The Roadmap states the rule directly, at Artifact 015's own row: **no secret may enter canon or
derived**, because **secrets are EXTERNAL forever**. This is a source-of-truth classification,
not a security recommendation, and it does not soften with age, repetition, or operational
necessity.

This document is a boundary contract. It defines no secret manager, no configuration loader, no
credential store, and no secret-handling implementation. Artifact 021
(`src/coolboy12/bootstrap/config.py`) implements the configuration loader that must obey this
boundary; it is not built here.

## 2. A Note on Source Coverage

Blueprint §9.5 — the section this artifact cites — never uses the word "secret" or
"credential." **The word "secret" appears in the Blueprint zero times.** The specific
secret/configuration boundary is stated by the Roadmap, not the Blueprint: at this artifact's
own row, at the repository tree (`boundaries/` holds "VCS, environment, secrets, SoT"), and at
the `.claude/**` permission row (`Prohibited: canon, secrets`).

What the Blueprint provides is the *general architecture* this boundary must remain inside:
external components hold no canonical authority (P-31), the environment runs coolboy12 without
defining it (P-33), and the Mutation Coordinator is canon's only writer (§12.6, I-83, I-84,
I-100). Every rule below is either a direct Roadmap statement or a direct application of one of
those Blueprint rules — never an invented secret-management practice.

## 3. The Boundary

```
secret material
        ↓
EXTERNAL
        ↓
never Canon · never Derived
```

Secrets are classified **EXTERNAL** under the Roadmap's source-of-truth system (PART VII).
Externality here is not a filesystem location; it is a permanent status. A secret does not stop
being EXTERNAL by being used, referenced, persisted, or needed. There is no operation that
promotes a secret out of this class.

## 4. What Counts as Secret Material

The Roadmap does not enumerate secret types. What it does state, at the `.claude/**` permission
row, is a bare pairing: **"canon, secrets"** — named together as the two things a
DEV-ENV-classified, environment-owned directory must never hold. No taxonomy is given beyond
that pairing.

Absent a source-defined taxonomy, this document uses the ordinary sense of the term rather than
inventing a classification scheme: material whose disclosure grants or exposes operational
access or authority — credentials, tokens, API keys, private keys, passwords, and connection
material carrying such data. This is descriptive, not an authoritative COOLBOY12 taxonomy; no
Registry `CONTROLLED-VOCABULARY` for secret classes exists, and none is created here.

**Secret ≠ all configuration.** Ordinary configuration — feature flags, local tool settings,
paths, non-sensitive environment selection, deterministic development settings — carries no
such disclosure risk and is not secret material. It may be `DEV-ENV` source-of-truth where the
Roadmap's PART VII classifies it so (`src/**`, `tests/**`, and similar are `DEV-ENV`). This
document does not reclassify ordinary configuration; it draws the line between the two
categories so Artifact 021 does not have to invent one.

## 5. Source-of-Truth Classification

The Roadmap's PART VII names six source-of-truth classes: AUTHORITATIVE, DERIVED, CACHED,
TEMPORARY, EXTERNAL, DEV-ENV. Its own row for external material:

| Artifact class | SoT | Authoritative | Rebuildable | Deletable | May influence canon | May write canon |
|---|---|---|---|---|---|---|
| external material | EXTERNAL | No | n/a | n/a | Only via proposal (386) | No |

Secret material is external material. It carries the same non-authoritative, non-canonical
status as any other external input.

**One narrowing applies specifically to secrets.** PART VII's "may influence canon: only via
proposal" describes the general path by which *observations of external reality* may become
World Truth candidates — an image, a document, a fact learned outside the system. A secret is
not a candidate world truth. It is operational access material, not a claim about the fictional
universe. **No proposal path exists for a secret to influence canon**, because a secret has
nothing to propose. Where general external material has one narrow door toward canon, secrets
have none.

**Secrets are never `DEV-ENV`.** The development environment may hold or use secret material
operationally, but that use does not reclassify the secret as environment-owned configuration
data. `DEV-ENV` in PART VII describes rebuildable, environment-authored material (`src/**`,
`tests/**`); a secret is neither authored by the environment nor rebuildable from it. It remains
EXTERNAL regardless of where in the environment it is used.

## 6. Prohibited Destinations

The Roadmap's PART I permission table states this directly, per directory:

| Path | Prohibited (per Roadmap PART I) |
|---|---|
| `canon/**` | derived output, drafts, **external material** |
| `derived/**` | anything unrebuildable |
| `.claude/**` | **canon, secrets** |

Two consequences follow, stated as this artifact's own rule:

> **No secret becomes Canon. No secret becomes Derived.**

This is the Roadmap's own Val for Artifact 015: *no secret may enter canon or derived.* It
applies without exception and without a size, duration, or rebuild-status carve-out:

- **No exception for caches, indexes, or projections.** `derived/**` and `derived/caches/**`
  are both DERIVED-class per PART VII; secret material entering either is the same violation.
- **No exception for reports, coverage, or health files.** `derived/coverage/`,
  `derived/health/` are DERIVED; "diagnostic" is not an exemption category.
- **No exception for generated docs or debug output.** Being machine-generated does not change
  a destination's source-of-truth class.
- **A derived artifact that needs to indicate a secret exists must not copy the secret.** It may
  record that a value was supplied, was valid, or was used — never the value itself.

## 7. Secret ≠ Canonical Data

A secret does not become canonical because it is persistent, used repeatedly, required for
startup, referenced by code, written into a configuration file, needed to execute a mutation, or
associated with a canonical operation. None of those properties is the property that makes
something canon. Canon is conferred at the Human Gate, through the Mutation Coordinator, on a
proposal about the fictional universe (§12.6). A secret is never such a proposal, no matter how
operationally necessary it is.

**Even a manual placement under `canon/**` is a boundary violation, not an exception.** PART I
already prohibits external material from `canon/**` explicitly; a secret placed there by mistake
or by hand does not thereby become canonical. It is a violation to be corrected, not a fact to
be normalized because it was committed.

## 8. Secret ≠ Derived Data

Likewise, a derived system never absorbs secret material merely because it is generated. Every
one of the following is a prohibited pattern:

```
secret  →  generated index        PROHIBITED
secret  →  health report          PROHIBITED
secret  →  projection             PROHIBITED
secret  →  cached artifact        PROHIBITED
```

"Automatically generated," "rebuildable," "cache," and "health report" are not exemptions.
`derived/**`'s own PART I prohibition — *anything unrebuildable* — already excludes secret
material by construction: a secret is not derivable from canonical Records, so anything that
depends on the secret to reproduce cannot be rebuilt by the rebuild process alone, and does not
belong in a directory whose entire content must be freely regenerable.

## 9. Environment and Mutation Boundary Compatibility

Artifact 014 establishes that the environment runs coolboy12 and does not define it. This
artifact does not restate that boundary; it applies it to secret material specifically:

The environment **may**: load or access external secret material for operational use, pass
operational credentials to tools it invokes, and configure runtime capabilities using such
material.

The environment **may never**: treat the existence, validity, or content of a secret as a
source of semantic truth, or let secret possession substitute for constitutional authority.

**A credential is not mutation authority.** An API credential may authorize an external
component to perform an operation; it does not authorize a canonical write. The canonical
mutation path is unchanged by whether a secret is present (§12.6, I-83):

```
proposal → validation → Human Gate → Mutation Coordinator → canon
```

Concretely:

```
secret-bearing external service → capability / adapter → proposal
    → validation → Human Gate → Mutation Coordinator → canon      PERMITTED PATH

secret → external service → direct canon write                    NEVER
```

**I-84 governs the general case and secrets are not an exception to it:** no external component
— which includes anything a secret authorizes — holds canonical semantics, defines a kind, owns
a relationship, adjudicates a mutation, or is the only place a canonical fact exists. Possessing
or supplying a valid credential changes nothing about that.

## 10. Version-Control Boundary Compatibility

Artifact 013 establishes that Git records file changes, never semantic history. This artifact
adds one narrow point of contact and does not restate 013's contract:

A secret appearing in Git history by accident is not the secret becoming Canon. Git recording a
commit is not the secret acquiring authority. The two failures are independent: a secret
committed to version control is a version-control incident (leaked external material); a secret
placed under `canon/**` is a boundary violation under this document. Neither failure is cured by
the other's absence, and fixing one does not fix the other.

## 11. Secret Provenance

A secret's origin — environment variable, local configuration, external system, credential
provider — is never recorded as canonical provenance. Provenance, in the constitutional sense,
traces a Record to the decision that created or last changed it (Spine law 9). A secret is never
a Record, so it has no canonical provenance to trace. Where a proposal or mutation used a secret
operationally, the proposal's own provenance may note that an external credential was used; the
credential's origin is never itself the thing being traced. No provenance mechanism is created
here.

## 12. Secret References

Internal configuration may need to refer to a secret without containing it. Where that
distinction is drawn:

```
secret reference  ≠  secret value
```

A reference (a name, a key, a pointer to where the value lives) is not itself secret material
and is not bound by this document's prohibitions the way the value it points to is. This
document states the distinction; it defines no reference object, schema, or syntax. If Artifact
021 requires one, it is 021's implementation choice, not a constitutional requirement fixed
here.

## 13. Configuration Loader Boundary — What Artifact 021 Inherits

Artifact 021 (`src/coolboy12/bootstrap/config.py`, `H: 005,015`, `Val: refuses secrets in canon
paths`) implements the configuration loader. This document gives it the following contract,
without designing its implementation:

| Rule | Status |
|---|---|
| Secrets remain EXTERNAL, regardless of how the loader obtains them | binding |
| The loader MAY consume external secret material for runtime use | permitted |
| The loader MUST NOT write secret material to any `canon/**` path | binding |
| The loader MUST NOT write secret material to any `derived/**` path | binding |
| Supplying a secret to the loader never grants semantic mutation authority | binding |
| A secret's presence in configuration does not make that configuration canon | binding |

**Not fixed here, because the source does not fix them:** the exact secret source (environment
variable, file, external provider), any specific storage product, an encryption algorithm, a
reference syntax, or a rotation policy. These are Artifact 021's implementation choices, made
inside the boundary this document draws — not constitutional requirements invented in advance of
that artifact.

## 14. Non-Goals

This document does not:

- select or require a secret storage product (no Vault, no cloud secret manager, no keychain
  integration — none is named because none is source-required, and naming one here would make
  the boundary depend on a specific vendor, which P-31 already forbids for any external
  component);
- define an encryption algorithm, rotation interval, or secret file format;
- define a machine-readable secret policy, JSON Schema, validator, or scanner;
- implement `src/coolboy12/bootstrap/config.py` or any part of Artifact 021;
- restate Artifact 013's version-control boundary or Artifact 014's environment boundary in
  full;
- create a Registry `CONTROLLED-VOCABULARY` for secret classes;
- add, modify, or reference any real secret, credential, or environment variable.

## 15. Standing Rules

1. Secrets are EXTERNAL. Nothing reclassifies them as AUTHORITATIVE, DERIVED, CACHED, or
   DEV-ENV.
2. No secret may enter `canon/**`. A secret found there is a boundary violation, not a
   precedent.
3. No secret may enter `derived/**`, including caches, indexes, projections, coverage, and
   health reports. Being generated automatically is not an exemption.
4. Possessing, supplying, or operationally requiring a secret never grants semantic mutation
   authority. The mutation path is unchanged: proposal → validation → Human Gate → Mutation
   Coordinator → canon.
5. A secret's origin is never canonical provenance.
6. A secret reference is not a secret value, and may be handled differently by the downstream
   loader.
7. A secret leaking into version control is a version-control incident, not a canon event; the
   two are independent failures with independent fixes.
8. This document defines the boundary. Artifact 021 implements the loader inside it.

## 16. Boundary of This Document

This document declares a boundary. It implements no loader, no manager, no validator, no scanner,
and no policy engine. It creates no new environment variable, storage product, or file. It
contains no real secret; every illustrative value in this document, where one appears, is a
placeholder such as `<SECRET>`, never production-shaped material.

`Req: BR-06` is preserved as written. The requirement register is not currently available
(Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here; this
document is validated against its Roadmap and Blueprint citations instead.
