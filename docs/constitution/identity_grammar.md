# COOLBOY12 — Identity Grammar Specification

**Artifact 034** · `docs/constitution/identity_grammar.md` · Own: CONST · RM: all · T: doc ·
R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P1/1b ·
Req: BR-23 · BP: §13.9a · RMS: §5 · H: 031 · S: 033 · LS: — · G: — ·
→ 035–037 · Risk: CRITICAL · ∥: no

## 1. Purpose

This document states what a COOLBOY12 identity is allowed to look like: its elements, their
order, and the rules each element carries. It is a grammar. It says nothing about what any
named thing means.

Row 034's `Why` states what the grammar's partition element is for: *"a four-partition enum
would make R and V unnameable."* An identity that cannot express a partition cannot name a
Record in it.

## 2. Status and Authority

| | |
|---|---|
| Role | CONTRACT · Type: doc (row 034) |
| Source-of-truth class | AUTHORITATIVE (Artifact 016 §3) |
| Canon | `n/a` — row 034. This document is not a Record and holds no canonical data |
| Hard dependency | **Artifact 031** (`H: 031`) |
| Soft dependency | **Artifact 033** (`S: 033`) |
| Unlocks | 035–037 |

The grammar is not established here. Blueprint §13.9a states it and RMS §5 freezes it
(`FROZEN`, AD-1, I-82). This document is the AUTHORITATIVE statement of the contract for
readers and for Artifacts 035–037; it amends neither source and adds no rule to either.

## 3. Scope

Artifact 033 carries `object_id` as one of the seven universal envelope fields and states no
positional grammar. This document supplies that grammar. It does not restate the envelope, and
the envelope's other six fields are not identity components (§4.2).

Everything below is **syntax**. The distinction is the point of the artifact and row 034's
`Done` names it — *grammar + syntax/semantics split*:

> **RMS §5** — *"**UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL.** The grammar fixes
> the syntax of the name and decides nothing about the thing named."*

## 4. Identity Grammar

### 4.1 Canonical form

> **Blueprint §13.9a** · **RMS §5** `FROZEN`
>
> ```
> [PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]
> ```

Four elements, in that order, separated by `-`. **The first element is always the partition**
(§13.9a): identity declares which side of a boundary a Record sits on, and therefore which
Record Model owns it, before it says anything else.

> **Blueprint §13.9a** — **This grammar is universal across all six Record Models (AD-1,
> resolved v0.7.0).** A World Record, an Epistemic Record, a Production Record, a Registry
> Record, a Visual Record, and an Issue Record all bear an identity of this form.

The grammar, its element order, its parsing and resolution contract, and its uniqueness
contract are shared infrastructure and constitutional (§13.7a, I-82).

### 4.2 Components

| Position | Element | Form | Source |
|---|---|---|---|
| 1 | `PARTITION` | one of six single-letter codes (§4.3) | Blueprint §13.9a |
| 2 | `KIND` | a **two-character** kind code within that partition (§4.4) | Blueprint §13.9a, §13.11; RMS §5 |
| 3 | `OBJECT_ID` | a stable ordinal (§4.5) | Blueprint §13.9a |
| 4 | `SLUG` | human-readable, decoration only (§4.6) | Blueprint §13.9a; RMS §5 |

No other element participates. `provenance`, `registry_ref` and `sot_class` are envelope
fields (Artifact 033) and are not identity components; `tier` and `status` are neither.

### 4.3 Partition representation

The Blueprint states the six codes directly, and they are **single characters**:

| Partition | Code |
|---|---|
| World | `W` |
| Epistemic | `E` |
| Production | `P` |
| Registry | `R` |
| Visual Library | `V` |
| Issue | `I` |

*(Blueprint §13.9a, which records the correction: "the v0.6.3 row still listed four, having
never been updated when v0.6.1 promoted Registry and Visual to partitions.")*

**All six, and no seventh.** The enum covers every sovereign Record Model (RMS §2, I-101). A
partition code outside this set is not a legal identity.

> **The two-character rule is a rule about `KIND`, not about `PARTITION`.** Blueprint §13.9a
> gives the partition codes as the single letters above; RMS §5 says *"two-character kind
> codes"*; Blueprint §13.11 says *"Kind codes are two characters, frozen."* No source states a
> two-character partition code, and the phrase "partition code" appears in none of them. The
> Blueprint's own example `W-CH-…` shows the shape: one character, then two.

### 4.4 Kind component

> **Blueprint §13.9a** — The kind code **within that partition**. It is a kind code, never the
> word "Canon".
>
> **Blueprint §13.11** — **Kind codes are two characters, frozen.** Every Record kind in every
> partition uses a two-character code.

The Blueprint records why: single-character codes were considered and rejected because they do
not disambiguate — *"`C` would serve both Character and Concept, `L` both Lineage and
Location."*

**The rule is frozen in the Blueprint; the roster is not this artifact's.**

> **Blueprint §13.11** — **The Registry owns the authoritative kind-code mapping** (`R`
> partition, §9.4). Codes for the E, P, R, V, and I partitions follow the same two-character
> rule and are Registry entries like any other — the *rule* is frozen here; the *roster*
> extends through ordinary Registry change (§14 below).

No kind roster is enumerated in this document, and none is frozen by it. A universal kind
taxonomy is prohibited (§13.7a); each Record Model owns its own (§13.11, I-106).

### 4.5 Object identity component

> **Blueprint §13.9a** — *"Stable ordinal. Never reused, including after retirement, because
> history references it forever."*

The source states the element's nature — an ordinal — and its permanence. It states no width,
padding, radix or upper bound, and none is invented here.

> **RMS §5, accommodated variance** — *"WSV bears no per-instance ordinal — the grammar already
> admits a singleton."*

### 4.6 Slug component

> **Blueprint §13.9a** — *"Human-readable. **Decoration only** — nothing resolves, matches, or
> validates against a slug, and a slug that has drifted from the object's name is untidy rather
> than wrong."*
>
> **RMS §5** — *"slug is decoration only."*

The slug occupies the fourth position and carries no authority. It is not canonical identity,
not a stable key, and nothing validates against it.

## 5. Identity Invariants

### 5.1 Partition coverage

The partition enum covers all six sovereign Record Models. A grammar that named fewer would
leave Records unnameable in the partitions it omitted, which is the defect row 034 exists to
prevent.

### 5.2 Ordinal permanence

**An ordinal is never reused, including after retirement** (Blueprint §13.9a). Retiring a
Record does not return its ordinal to circulation; the Blueprint gives the reason — *"history
references it forever."*

This is the identity-level rule. **How ordinals are allocated, and how non-reuse is enforced
durably, is Artifact 036** — no allocator, counter, persistence or concurrency rule appears
here.

### 5.3 Rename behavior

> **Blueprint §13.9a** — *"**A rename must not silently create a new canonical identity.**
> Renaming changes the display name and retains the former name; the identity is untouched."*
>
> **I-82** — *"A rename never creates a new canonical identity, and an internal machine
> identifier never replaces or contradicts the canonical one."*

Because the slug is decoration (§4.6), changing it changes no identity. A rename is not an
identity operation.

*Scope note, stated rather than widened.* §13.9a continues *"Identity changes only through the
four identity operations (Section 13.8)"*, and §13.8 is scoped at v0.7.0 as **World Record
Model semantics**, its gated-act mechanism shared infrastructure available to any Record Model
while its meaning is World's. This artifact therefore carries the rename rule, which §13.9a and
I-82 state universally, and does not extend §13.8's four operations to the other five models.

### 5.4 Internal identifiers

> **Blueprint §13.9a** — **An internal machine identifier may exist as an implementation
> detail** — a row key, a hash, a UUID — but it must not replace, shadow, or contradict the
> canonical identity. If the two ever disagree, the canonical identity is right.

## 6. What This Grammar Does Not Define

**Not semantics.** The grammar fixes the syntax of a name and decides nothing about the thing
named. Blueprint §13.9a: *"Two Records may be identically well-formed and have nothing else in
common — a `W-CH-…` and an `R-…` share a shape, not a lifecycle, an authority, a temporal
architecture, or a package."* RMS §5 divides it explicitly:

| Universal | Model-owned |
|---|---|
| syntax · positions · parsing · resolution · uniqueness · minting infrastructure | Kind meaning · Kind taxonomy · semantic interpretation · lifecycle meaning · authority meaning · identity-specific constraints |

Blueprint §13.7a prohibits a universal identity **composition**: what constitutes the identity
of a Record *in a model* stays model-owned. Two identities matching this grammar are two
well-formed names, not two things of one nature.

**Not established by the supplied authoritative sources**, and therefore not stated here:

- character sets for any element, beyond `KIND` being two characters;
- length, padding, radix or bound for `OBJECT_ID`;
- case rules, normalization, or case folding;
- whitespace, escaping, or the behaviour of a `-` appearing inside a `SLUG`;
- any regular expression for any element.

Artifact 035 will need several of these to parse an arbitrary string; where they remain
unestablished they are an authorial decision, not an implementation choice to be made silently.

## 7. Downstream Ownership

| Not defined here | Owned by |
|---|---|
| Parsing, formatting, resolution | Artifact 035 |
| Ordinal allocation and its durable non-reuse mechanism | Artifact 036 |
| Structural validation of an identity string | Artifact 037 |
| The authoritative kind-code mapping and every kind roster | Registry (`R` partition, §9.4) |
| What an identity *means* in a model | that Record Model (e.g. World identity semantics, P7) |

## 8. Source Traceability

| Rule | Source |
|---|---|
| Grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` | Blueprint §13.9a; RMS §5 `FROZEN`; I-82; row 034 `Val` |
| Element order, partition-first | Blueprint §13.9a; RMS §5; I-82 |
| Six partitions, single-letter codes | Blueprint §13.9a table; RMS §2 |
| `KIND` is two characters | RMS §5; Blueprint §13.11 |
| Kind roster and mapping are Registry's | Blueprint §13.11, §9.4; I-105, I-106 |
| `OBJECT_ID` is a stable ordinal | Blueprint §13.9a |
| Ordinals never reused, including after retirement | Blueprint §13.9a; RMS §5; row 034 `Val` |
| WSV singleton admitted by the grammar | RMS §5 |
| Slug is decoration only | Blueprint §13.9a; RMS §5 |
| Rename does not create a new canonical identity | Blueprint §13.9a; I-82 |
| Internal machine identifier subordinate to canonical identity | Blueprint §13.9a; I-82 |
| Grammar ≠ semantics; no universal identity composition | Blueprint §13.7a, §13.9a; RMS §5 |

*Illustrative shape, from the Blueprint's own example table at §13.11: `W-CH-001-Maximus` — one
partition character, a two-character kind code, an ordinal, a decorative slug. Reproduced to
show the form; this document establishes no identity, no kind roster and no ordinal.*

---

*Artifact 034. This document is AUTHORITATIVE about identity **syntax** and is `Canon: n/a`. It
carries no canonical data, defines no Record, states no parser, formatter, allocator or
validator, and claims no semantic identity for any Record Model.*
