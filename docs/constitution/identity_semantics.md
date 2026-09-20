# COOLBOY12 — Identity Semantics Boundary

**Artifact 046** · identity semantics boundary · `docs/constitution/identity_semantics.md` ·
Own: CONST · RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing ·
Canon: n/a · CD: no · Ph/St: P2/2b · Req: BR-23,RR-05 · BP: §13.9a · RMS: §5 ·
H: 034,045 · S: — · LS: — · G: — · → all models ·
Val: universal grammar ≠ universal semantics, as a rule ·
Done: explicit · Why: AD-1's second half · Risk: high · ∥: no

> **On the name of the `V` partition.** Blueprint §13.9a's element table reads *"`V` Visual
> Library"*; RMS §2 and RMS §6 read **Visual**. These are two source names for one partition,
> whose code is `V`. Both are recorded and **neither source is corrected here**, because neither
> is this artifact's to amend.

## 1. Purpose

Row 046 states this artifact's reason in four words: **AD-1's second half.**

AD-1 is resolved as *one universal identity grammar, model-owned semantics*. **Artifact 034
owns the first half** — the grammar. This document owns the second: it states, as a binding rule,
that the shared grammar creates no shared semantics, and that what an identity *means* belongs to
the Record Model that owns the Record.

Blueprint §13.9a states the rule this artifact exists to make operational:

> *"**What the shared grammar does not share.** It fixes the **syntax** of a name and decides
> nothing about the thing named… Two Records may be identically well-formed and have nothing else
> in common — a `W-CH-…` and an `R-…` share a shape, not a lifecycle, an authority, a temporal
> architecture, or a package. **Universal identity grammar ≠ universal Record semantics.**"*

It adds no architecture. Every rule below is a contractual formulation of what Blueprint §13.9a,
Blueprint §13.8, RMS §5, RMS §6 and I-82 already establish.

## 2. Constitutional Status

This document is AUTHORITATIVE about **the boundary between universal identity grammar and
model-owned identity semantics**, and about nothing else. It **derives** that boundary from the
Master Blueprint and the Record Model System; it does not amend, supersede, or outrank either.

Where this document and the Master Blueprint, the Record Model System, or the OS File Build
Roadmap differ, **they are right and this document is wrong.**

It is not a Record, holds no canonical data, and is `Canon: n/a`. `SoT: AUTHORITATIVE` here means
authoritative **about architecture**, never World Canon (Blueprint §13.0, I-104).

## 3. Scope

**In scope.** That the identity grammar is universal; that identity semantics are not; which
authority owns the semantic interpretation of a Record's identity; the constitutional stability
rules that bind identity in every model; and the boundary at which semantic questions pass to the
owning Record Model.

**Out of scope.** The grammar itself, every model's concrete identity semantics, and all matters
listed in §13. This contract says **who decides what an identity means**. It does not decide it.

## 4. The Governing Identity Rule

```
                              IDENTITY
                                 │
                    ┌────────────┴────────────┐
                    │                         │
              UNIVERSAL                  MODEL-OWNED
               GRAMMAR                    SEMANTICS
                    │                         │
   [PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]      ├── W
                    │                         ├── E
         Artifact 034 · shared                ├── P
         infrastructure (§13.7a, I-82)        ├── R
                                              ├── V
                                              └── I
```

**The grammar is universal. The meaning is not.** Blueprint §13.9a: the grammar *"is universal
across all six Record Models (AD-1, resolved v0.7.0)"*, and *"the grammar, its element order, its
parsing and resolution contract, and its uniqueness contract are **shared infrastructure and
constitutional** (§13.7a, I-82)."*

The two halves are read separately and never collapsed. A Record bearing a well-formed identity
has a **name of the shared form**; it does not thereby have shared meaning, shared lifecycle,
shared authority, or shared packaging.

## 5. Universal Grammar Is Not Universal Semantics

RMS §5 fixes the split, and this contract reproduces it without amendment:

| Universal | Model-owned |
|---|---|
| syntax · positions · parsing · resolution · uniqueness · minting infrastructure | Kind meaning · Kind taxonomy · semantic interpretation · lifecycle meaning · authority meaning · identity-specific constraints |

> **UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL.** *The grammar fixes the syntax of the
> name and decides nothing about the thing named.* (RMS §5)

**This MUST NOT be read as a shared semantic identity object model.** RMS §4's nine prohibitions
are `FROZEN` and include **no universal identity *composition***, alongside no Universal Record
Base, no universal lifecycle, no universal canonicality, no universal Kind taxonomy, no universal
state model and no universal semantic schema. Nothing in this contract establishes a universal
identity object, a base identity, a shared identity parent, or any structure of which the six
models' identities are instances or specializations. The Canon Object Model is retired (RMS §2)
and is not revived here in any form.

**What sharing a grammar confers is a mechanism, never a semantic** (I-103, Artifact 043).

## 6. Identity at the Constitutional Boundary

**A Record is identity-bearing.** RMS §6.1 defines a Record as *"a persistent, identity-bearing
unit owned by exactly one Record Model."* Identity is a property of the Record, carried by it.

**Canonical identity is not an implementation handle.** It is not a filename, a storage key, a
database key, a display label, a slug, or any implementation-local identifier. Blueprint §13.9a:
an internal machine identifier *"may exist as an implementation detail — a row key, a hash, a
UUID — but it must not replace, shadow, or contradict the canonical identity. If the two ever
disagree, the canonical identity is right."*

This contract states that boundary and **defines no storage, serialization, or key architecture**
(§13).

## 7. Model-Owned Identity Semantics

**The Record Model that owns the Record owns the semantic interpretation of its identity.** RMS §6
enumerates what a Record Model owns, and **identity semantics** is among the nine; RMS §5 places
*semantic interpretation* and *identity-specific constraints* in the model-owned column.

At the constitutional boundary, the owning model — and no other authority — determines:

- what constitutes the identity of a Record in that model;
- what semantic continuity that identity carries;
- the identity-specific constraints that bind it;
- how its identity semantics relate to that model's lifecycle and authority semantics.

**This contract answers none of those four for any of W, E, P, R, V or I.** It establishes only
that the owning model answers them. Concrete answers belong to the model-owned artifacts named in
§11.

### 7.1 Equivalence is semantic, not grammatical

**Grammatical well-formedness and semantic identity equivalence are different questions.** That
two identity representations are each valid under Artifact 034's grammar **DOES NOT** establish
that they denote the same Record, or semantically equivalent Records.

**Semantic equivalence is governed by the owning Record Model's identity semantics.** This
contract defines no universal equivalence relation and no universal comparison semantics.

## 8. Identity Stability

These rules are constitutional and bind every Record Model. I-82: *"Identity is partition-first
and stable: `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]`. A rename never creates a new canonical
identity, and an internal machine identifier never replaces or contradicts the canonical one."*

| Rule | Source |
|---|---|
| A rename **MUST NOT** silently create a new canonical identity; the display name changes and the identity is untouched. | Blueprint §13.9a; I-82 |
| `SLUG` is decoration only. Nothing resolves, matches, or validates against a slug, and a drifted slug is *"untidy rather than wrong"*. It **DOES NOT** define canonical identity. | Blueprint §13.9a |
| `OBJECT_ID` is a stable ordinal, **never reused, including after retirement**, *"because history references it forever"*. | Blueprint §13.9a |
| An internal machine identifier **MUST NOT** replace, shadow, or contradict the canonical identity; where the two disagree, **the canonical identity is right**. | Blueprint §13.9a; I-82 |

These are not weakened, qualified, or made model-optional by anything in this contract.

### 8.1 Identity operations are not universalized here

Blueprint §13.9a states that *"Identity changes only through the four identity operations (Section
13.8)"*. **Section 13.8 scopes those four operations to the World Record Model**, and this
contract records that scoping rather than overriding it:

> *"(SCOPED v0.7.0. The four operations below are **World Record Model** semantics. Their
> mechanism — a gated act that preserves every history involved — is shared infrastructure and
> available to any Record Model; their **meaning** for the five other models is **OPEN** and is
> not invented here."*

Therefore:

- the **mechanism** of a gated, history-preserving identity act is shared infrastructure;
- the **meaning** of supersede, split, merge and retire is World Record Model semantics;
- for the other five models that meaning is **OPEN**, and **this contract does not invent it**;
- Issue's supersession rule (Blueprint §13.6a) is the one other model whose behaviour is already
  frozen, and the Blueprint records that it *"is a publication rule, not one of these four."*

**No universal identity-transition protocol is established here.** This contract defines no
universal semantics for supersede, split, merge, retire, convert, migrate, clone, fork, alias or
redirect. World identity operations are Artifact 205's; each other model's are its own.

## 9. Partition-First Identity

The first element of the canonical identity is the partition. Blueprint §13.9a: *"**The first
element is always the partition** — identity declares which side of a boundary a Record sits on,
and therefore which Record Model owns it, before it says anything else."*

**Read precisely.** Partition-first ordering makes the owning model **legible in the name**. It
**DOES NOT** make the grammar a semantic ontology, and it decides nothing beyond placement:

```
identity reveals which model owns the Record
        ≠
identity determines what the Record means
```

Kind occupies a defined position in the grammar, and Blueprint §13.9a is explicit that *"the kind
taxonomy and the meaning of any kind are owned by the Record Model"* (§13.11). Position is
grammar; meaning is model-owned.

Partition **ownership** itself is Artifact 045's contract and is not restated here.

## 10. Identity / Partition Consistency Boundary

Artifact 045 §12 states that it *"does not define conflict resolution between an identity
representation and a Record's declared partition; that belongs to the validation and
identity-semantics contracts."* This contract takes the semantic half of that boundary and
states its limit precisely:

| Question | Where it belongs |
|---|---|
| Is the identity representation well-formed? | structural identity tooling — Artifacts 035–037 |
| What does the identity mean, once well-formed? | **here**, at the boundary; then the owning Record Model |
| Which partition owns the Record? | Artifact 045 |
| Executable enforcement of either | Artifacts 128, 129 |

**The supplied sources do not establish a resolution order for a disagreement between a Record's
declared partition and its identity representation, and this contract does not invent one.** It
states only that such a disagreement is not resolved by grammar alone, and that **this artifact
implements no validation and adjudicates no case**. The gap is recorded, not filled.

## 11. Relationship to Neighbouring Contracts

Each row names a boundary this contract **defers to** and does not replace.

| Artifact | Owns | 046 does not replace |
|---|---|---|
| **034** | the identity grammar | grammar syntax, element rules, the grammar contract itself |
| **035–037** | parsing, formatting, resolution, ordinal allocation, structural validation | any structural or operational handling of an identity string |
| **041** | six-model sovereignty | why no model is a specialization or template of another |
| **042** | the formal Record Model definition | what a Record Model is, and the nine dimensions it owns |
| **043** | the mechanism vs semantics boundary | the nine prohibitions, and what a shared mechanism does not confer |
| **044** | the architectural categories | what a Record or a Kind *is* |
| **045** | partition ownership | which partition owns a Record, and the conversion prohibition |
| **177 · 256 · 299** | World, Epistemic and Production identity semantics | each model's own semantic realization |
| **205** | World identity operations | supersede, split, merge, retire as World semantics |
| **128** | the identity validator | executable enforcement of identity |

**On the six models and their identity artifacts.** Identity semantics are model-owned for all six
(RMS §5, §6). The Roadmap currently declares dedicated identity-semantics artifacts for **W (177),
E (256) and P (299)** — each of which names `046` in its own `H` — and declares no equivalent row
for Registry, Visual or Issue. **That absence is recorded, not filled:** identity semantics for
those three remain model-owned, and this contract does not supply them, assign them elsewhere, or
treat the missing rows as licence to decide them here.

## 12. Worked Examples

The identities below follow the Blueprint's own illustrative shapes at §13.9a. They establish no
Record, no kind roster and no ordinal.

**A — One grammar, two unrelated meanings.**

```
W-CH-001-Maximus          well-formed · World Record Model
R-<kind>-001-<slug>       well-formed · Registry Record Model
```

Both obey the universal grammar. Neither thereby shares a lifecycle, an authority, a temporal
architecture, or a package with the other — Blueprint §13.9a states exactly this of a `W-CH-…` and
an `R-…`. **Shared shape is not shared meaning.**

*The Registry kind code is written `<kind>` deliberately.* Blueprint §13.9a fixes that kind codes
are two characters and that *"the Registry owns the authoritative kind-code mapping"*; the `R`
roster is Registry content, and **this contract mints no kind code.**

**B — Rename.**

```
W-CH-001-Maximus  ──rename──▶  W-CH-001-Maximus
                               display name changes; canonical identity unchanged
```

The display name changes and the former name is retained. **The canonical identity is untouched**
— no new identity value is created, here or by the act (Blueprint §13.9a, I-82).

**C — Slug drift.**

The slug in `W-CH-001-Maximus` may come to differ from the object's current name. The identity
remains valid and continues to resolve, because `SLUG` is decoration only and *"a slug that has
drifted from the object's name is untidy rather than wrong"* (Blueprint §13.9a). No validation
behaviour is defined here.

**D — Machine identifier.**

```
canonical identity : W-CH-001-Maximus
internal row key   : an implementation detail — a row key, a hash, a UUID
```

The implementation key may exist. It **MUST NOT** replace, shadow, or contradict the canonical
identity, and **if the two disagree the canonical identity is right** (Blueprint §13.9a, I-82).

**E — Model-owned semantics, side by side.**

Two Records in different partitions, each with a correctly formed identity, are each interpreted
by **their own** Record Model's identity semantics. Those interpretations are not required to
agree, are not derived from one another, and do not merge the two models into one semantic system.
**What each interpretation actually is, this contract does not state** — it belongs to the model
(§7, §11).

## 13. Non-Goals — What This Contract Does Not Define

This contract defines the identity semantics boundary. It defines **none** of the following, and
no reader may cite it as having done so:

1. the identity grammar — **Artifact 034**
2. grammar parsing, formatting, resolution, normalization or minting — **Artifacts 035–037**
3. any universal semantic Record model or base Record model — **PROHIBITED**, RMS §4
4. any universal identity schema or universal identity *composition* — **PROHIBITED**, RMS §4
5. any universal Kind taxonomy — RMS §4; Kind meaning is model-owned, §13.11
6. universal lifecycle semantics — **PROHIBITED**, RMS §4
7. universal canonicality semantics — **Artifact 052**, I-104
8. universal authority semantics — **Artifact 051**
9. universal state semantics — **PROHIBITED**, RMS §4
10. universal relationship packaging — **Artifact 055**, I-102
11. a universal temporal mechanism — **Artifact 054**, I-90
12. any model's own identity semantics — **177, 256, 299**, and the model itself for R, V and I
13. executable validators — **Artifacts 128, 129**
14. storage architecture
15. database keys or indexes
16. runtime implementation
17. serialization format — **Artifact 033**
18. universal identity operations — **§8.1**; World's are **Artifact 205**
19. model-specific lifecycle ceremonies
20. any reintroduction of the retired Canon Object Model — retired at RMS §2

**None of these exclusions weakens the universal rules in §8.** I-82's stability rules and
Blueprint §13.9a's grammar are constitutional and bind every model; excluding a *semantic* from
this contract never excludes a *constitutional rule* that the sources state universally.

## 14. Conformance Conditions

Stated so they are checkable. **Artifact 059** owns the P2 kernel conformance suite and
**Artifact 128** is the identity validator; this document implements no test and is `T: doc`.

No `046.x` constitutional invariant is minted: the sources supply I-82 for identity stability, and
no source-backed invariant number exists for the remaining conditions, which are therefore stated
without one.

| ID | Condition | Basis |
|---|---|---|
| **C-01** | The canonical identity grammar is shared across all six Record Models. | Blueprint §13.9a; I-82; RMS §5 |
| **C-02** | The universal grammar creates no universal Record semantics. | Blueprint §13.9a; RMS §5 |
| **C-03** | The semantic meaning of a Record's identity is owned by the Record Model that owns the Record. | RMS §5, §6 |
| **C-04** | A rename does not silently create a new canonical identity. | Blueprint §13.9a; I-82 |
| **C-05** | `SLUG` does not define canonical identity. | Blueprint §13.9a |
| **C-06** | `OBJECT_ID` is stable and is not reused, including after retirement. | Blueprint §13.9a |
| **C-07** | An internal machine identifier does not replace, shadow, or contradict the canonical identity. | Blueprint §13.9a; I-82 |
| **C-08** | This contract defines no model-specific identity semantics on behalf of any of the six models. | RMS §6; §7, §11 |
| **C-09** | This contract does not redefine Artifact 034's grammar. | Roadmap row 034; §11 |
| **C-10** | This contract introduces no universal semantic identity model and no base Record model. | RMS §2, §4; §5 |

A construction satisfying all ten is conformant **to this contract**. It is not thereby conformant
to the Record System: the other P2 contracts carry their own conditions.

## 15. Source Traceability

| Rule | Source |
|---|---|
| The grammar is universal across all six Record Models | Blueprint §13.9a; I-82; RMS §5 |
| Grammar, element order, parsing/resolution and uniqueness are shared infrastructure | Blueprint §13.9a, §13.7a; I-82 |
| Universal identity grammar ≠ universal Record semantics | Blueprint §13.9a; RMS §5 |
| Partition-first ordering; identity declares which model owns the Record | Blueprint §13.9a; I-82; RMS §5 |
| Kind position is grammar; Kind meaning and taxonomy are model-owned | Blueprint §13.9a, §13.11 |
| Identity semantics are a Record Model-owned concern | RMS §5, §6 |
| A rename never creates a new canonical identity | Blueprint §13.9a; I-82 |
| `SLUG` is decoration only | Blueprint §13.9a |
| `OBJECT_ID` is stable and never reused, including after retirement | Blueprint §13.9a |
| A machine identifier never replaces or contradicts the canonical identity | Blueprint §13.9a; I-82 |
| The four identity operations are World Record Model semantics; their meaning elsewhere is OPEN | Blueprint §13.8 |
| Issue supersession is a publication rule, not one of the four | Blueprint §13.8, §13.6a |
| No universal identity composition, base, lifecycle, canonicality, Kind taxonomy, state model or semantic schema | RMS §4 nine prohibitions `FROZEN` |
| Shared mechanism confers no shared semantic | I-103; Blueprint §13.7a; Artifact 043 |
| A Record is identity-bearing and owned by exactly one Record Model | RMS §6.1 |
| Hard dependency on 034 and 045; unlocks all models | Roadmap row 046 |
| Downstream model identity semantics declared for W, E and P | Roadmap rows 177, 256, 299 |
| World identity operations are their own artifact | Roadmap row 205 |
| Executable identity enforcement is its own artifact | Roadmap row 128 |

`Req: BR-23,RR-05` is preserved exactly as the Roadmap states it. The authoritative requirement
register is not present in this repository; the requirement text is therefore **not** reproduced
here and **MUST NOT** be inferred.

---

*Artifact 046 · P2/2b · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states a contract derived from Blueprint §13.9a and §13.8, RMS §5 and §6, and invariant
I-82. It is not a Record, holds no canonical data, states no grammar, parser or validator, and
claims no identity semantics for any Record Model. Where it and the Master Blueprint, the Record
Model System, or the OS File Build Roadmap differ, they are right and this document is wrong.*
