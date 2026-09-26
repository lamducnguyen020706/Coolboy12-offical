# COOLBOY12 — Kind Admission Test

**Artifact 057** · Kind admission test · `docs/constitution/kind_admission.md` · Own: CONST ·
RM: all · T: doc · R: CONTRACT · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no ·
Ph/St: P2/2d · Req: BR-25,RR-26 · BP: §13.11 · RMS: §13 · H: 044 · S: — · LS: — · G: — ·
→ every Kind artifact · Val: fourteen questions; ladder both directions · Done: test binding ·
Why: every Kind must justify itself · Risk: HINGE · ∥: no

## 1. Purpose

This contract answers one question: **what must a proposed Kind answer before it is a Kind, and in
which directions does the ladder run?**

RMS §6.1 defines a Kind as *"A class of Record within one model"*, and its test as *"Passes the
Kind Admission Test (§13)"*. RMS §13 states that test. This contract binds it to the Kind
artifacts — row 057's `→` is *"every Kind artifact"* and its `Done` is *"test binding"* — except
where World's relation to §13.11 is unresolved (§7 below), and states the ladder in both directions.
Row 057's reason: *"every Kind must justify itself"*.

**This contract adds no architecture.** Every rule restates RMS §6.1 and §13, Blueprint P-7, P-25,
§13.6, §13.6e, §13.7, §13.11 and §29.4, I-71, I-84 and I-106, and Artifact 044.

## 2. Constitutional Status

`Own: CONST` · `RM: all` · `T: doc` · `R: CONTRACT` · `SoT: AUTHORITATIVE` · `Auth: governing` ·
`Canon: n/a`.

This document is AUTHORITATIVE about **the Kind admission test and its binding**. It is not World
Canon, not a Record, not a Kind roster and not a schema. It admits no Kind and decides no model's
roster.

It derives the contract from the Master Blueprint and the Record Model System; it does not amend,
supersede, or outrank either, and mints or amends no invariant. Where this document differs from
the Master Blueprint, the Record Model System, or the OS File Build Roadmap, **those governing
sources are correct and this document is wrong.**

`Req: BR-25,RR-26` is preserved exactly as the Roadmap states it. This contract does not reproduce,
reconstruct or infer the requirement text, and creates no new requirement under it.

## 3. Scope

**In scope.** The fourteen questions of RMS §13 and their binding on the E, P, R, V and I Kinds; the
ladder, upward and downward; World's §13.11 admission test and ceremony, as §13.11 states them; what
the sources say about the Registry's part; the source conditions that bear on admission.

**Out of scope.** Classification against the eight architectural categories (Artifact 044); any
model's Kind roster (Artifacts 064, 176, 255, 298, 344, 363); the `KIND-DEFINITION` specification
and schema (Artifacts 068, 069); package composition (056); cross-model dependency (058); the
temporal obligation (054); the relationship boundary (055); the mechanics of any ceremony; schemas,
fields, storage, code and tests.

```
044  architectural categories   — is it a Kind candidate at all? ("→ 057 decides")
057  Kind admission test        ← this contract: the fourteen questions; the ladder
  ↓
     every Kind artifact        — 064 R · 176 W · 255 E · 298 P · 344 V · 363 I
```

## 4. Definitions

| Term | Meaning | Source |
|---|---|---|
| **Kind** | *"A class of Record within one model"* | RMS §6.1; Artifact 044 §5 |
| **Kind candidate** | a proposal classified as a class of Records within one model, before admission | Artifact 044 §7 |
| **Kind Admission Test** | the fourteen questions every Kind must answer | RMS §13 |
| **Admission** | the source-defined act by which a candidate becomes a Kind: for E, P, R, V and I, RMS §6.1 ties Kind status to passing the test; for World, §13.11 states that admission is *"a schema change at Foundational ceremony"* | RMS §6.1, §13; Blueprint §13.11 |
| **`KIND-DEFINITION`** | the Registry Record that defines what a Kind means | Blueprint §13.6e; Roadmap LS-1 |

This contract infers no ceremony mechanics beyond those statements and resolves no relationship
the sources leave unresolved (§7 below).

Classification is not admission. Artifact 044: *"Classification here is not admission."* A Kind
existing in a roster, a Kind being defined in the Registry, and a Kind being admitted are three
statements; this contract equates none of them.

## 5. The Kind Admission Test

### 5.1 The fourteen questions

RMS §13 (`FROZEN`): *"every Kind must answer:"*

| # | Question |
|---|---|
| 1 | what semantic object |
| 2 | what semantic question |
| 3 | why independent identity |
| 4 | what persistent state |
| 5 | what lifecycle |
| 6 | what authority |
| 7 | what references it |
| 8 | why not a field |
| 9 | why not a state |
| 10 | why not a relationship |
| 11 | why not a subtype |
| 12 | why not a projection |
| 13 | why not a Registry definition |
| 14 | what breaks if it is not first-class |

The numbering is this contract's, for reference; RMS §13 lists the questions in this order.

### 5.2 Binding

RMS §13 states that **every Kind** must answer the fourteen questions, and RMS §6.1 makes passing
the test what a Kind is. For the E, P, R, V and I Kinds, the fourteen bind, and a candidate that has
not answered all fourteen has not passed. For World, how RMS §13 relates to §13.11 is unresolved by
the current sources (§7 below), and this contract binds neither test to World on its own reading.

Row 057's `→` reads *"every Kind artifact"*; the Roadmap does not define the term. This contract
reads it as the concrete downstream artifacts currently identified as declaring Kinds: the six model
Kind taxonomy artifacts, rows 064, 176, 255, 298, 344 and 363. It does not extend the phrase beyond
what the governing sources establish. A Kind taxonomy artifact is not a Record instance and not a
runtime object.

### 5.3 SOURCE GAP — what makes an answer sufficient

RMS §13 requires an answer to each question and states no rule for judging one. This contract adds
none. For World, §13.11 supplies eight yes/no questions and a refusal rule (§7 below); for the
other models, judging an answer is the model's own design work (§8 below).

## 6. The Ladder — Both Directions

RMS §13: *"FIELD → KIND → STATUS → STRUCTURE, and the reverse when a Kind no longer justifies its
structural cost."*

**Upward.** P-7: *"A new concept becomes a field, then a kind, then a status, and only then —
rarely — a new structure."* A concept enters at the lowest rung that carries it.

**Downward.** P-7: *"The ladder runs downward as well as upward: an existing kind that a subtype or
field could carry is walked back down it (Section 13.6)."* Blueprint §13.6 records the one time it
was done: the ten retired World kinds were each *"walked down P-7's ladder to the lowest rung that
carries it"*.

**Retirement.** A Kind walked back down the ladder is no longer a Kind; §13.6 calls the ten World
kinds so walked down *"the ten retired kinds"*. P-25 makes retirement first-class: *"Every extension
point that admits also retires."* §29.4 states the universal rule: retirement *"applies to
everything admission does"*, including object kinds, and existing records are *"never deleted"*.
§13.11 states it for World kinds: *"existing records remain valid, readable, and historically
reachable forever; new records of that kind are refused by the linter."* This contract defines no
retirement procedure.

**SOURCE GAP — the upper rungs.** The sources name STATUS and STRUCTURE as rungs and do not define
them. This contract does not define them.

## 7. World — The §13.11 Test and Ceremony

World's taxonomy is established (Blueprint §13.6) and closed (I-71). §13.11: *"Closed does not mean
permanent; it means an eighth kind is an event, not a convenience."*

**Eight questions.** Blueprint §13.11 independently states the following World-specific
admission requirements. This contract records those source requirements but does not establish
their relationship to RMS §13. §13.11: *"A proposed World kind must answer all eight"*:

1. independent canonical identity;
2. an independent lifecycle;
3. meaningful independent history;
4. relationships that cannot be represented cleanly on an existing kind;
5. a subtype would be insufficient;
6. `CONCEPT` would be insufficient;
7. a Registry classification would be insufficient;
8. promotion avoids ontology bloat.

§13.11 states the refusal rule: a no on any of them *"refuses the promotion and names the
correct rung: field, subtype, relationship, Concept, or Registry entry."*

**Ceremony.** §13.11: *"Admission is a schema change at Foundational ceremony and lands in both
documents in the same cycle (Section 13.7)."* I-71 states the same for an eighth instance-bearing
kind. §13.7: *"A change to kinds … that lands in only one of the two documents is a defect"*.
This contract cites the ceremony and defines none of its mechanics.

**World status — source-blocked.**

- **Recorded:** RMS §13 states that *"every Kind must answer"* the fourteen questions.
- **Recorded:** Blueprint §13.11 states that *"A proposed World kind must answer all eight"*, with
  its refusal rule and Foundational ceremony.
- **UNRESOLVED BY CURRENT SOURCES:** the governing sources do not establish how the two relate for
  World.
- **Not invented here:** this contract neither merges them, maps one onto the other, orders them,
  nor chooses between them.
- **Conformance:** no condition below binds either question set to World, and none presents the
  relation as resolved. C-057-06 binds only World's ceremony, which does not depend on it.

## 8. The Other Record Models

**Source condition recorded, not resolved.** The sources state the status of non-World rosters two
ways:

| Source | Statement |
|---|---|
| Blueprint §13.6, I-106 | non-World rosters are boundary-naming; a kind in that state *"may be renamed, split, merged, promoted from a field, or demoted to a subtype by the model's own design work without invoking §13.11's admission ceremony — because that ceremony governs an established taxonomy and only World has one"*; I-106: revisable *"until it declares otherwise"* |
| RMS §8.1, §9.1, §10.1, §11.1, §12.1 | each roster recorded as a final taxonomy, *"CLOSED"* — E at seven, P at thirteen, R at fourteen, V at three, I at five |

This contract does not decide whether the RMS closures are the declarations I-106 anticipates.

**SOURCE GAP — the non-World admission act.** No source defines the ceremony by which a Kind is
admitted to a non-World roster once it is closed. RMS §9.1 names one requirement — *"A future
non-public production object requiring identity must pass a Kind Admission amendment rather than
reuse a generic bucket"* — without defining the amendment. Roadmap row 459, the extensibility
contract (`H: 057,064`), is to state how a new Kind is added — *"each through its own ceremony,
never through a generic abstraction"*. This contract defines no ceremony and anticipates none of
459's. The fourteen questions bind regardless (§5.2 above).

**Model-specific criteria.** A model may carry its own admission criterion alongside the test.
RMS §12.1 gives Issue's: *"a publication component is first-class when it is independently
referenced, independently credited, or independently placed"*. Such criteria are the model's; this
contract binds the fourteen questions and adds no model criterion.

## 9. The Registry's Part

What the sources establish:

- **Registry defines a Kind; the model owns its Records.** §13.6e: the Registry owns *"The
  definition of a kind"*; each Record Model owns *"Which Records of that kind exist, and what they
  mean in its domain"*.
- **Every Kind has a definition, in lockstep.** Roadmap LS-1: *"every Kind spec ↔ its Registry
  KIND-DEFINITION"*, an atomic pair.
- **Registry's own Kind taxonomy depends on this test.** Row 064: *"exactly fourteen Kinds, each
  with admission rationale"*, with `H: 060,057`.
- **No external component defines a kind.** I-84: *"No external component … defines a kind"*.
  I-84 governs external components; it assigns neither definition ownership nor admission.

Definition authority and admission authority are separate questions. The Registry owns the
definition of a kind (§13.6e), and I-105 gives it *"semantic authority over definitions and never
semantic ownership of another model's Records"*. Neither source speaks to admission. The sources do
not establish that the Registry admits another model's Kind, and **this contract does not define
or assign the Registry authority to admit another model's Kind.** A `KIND-DEFINITION` is not that
Kind's admission: admission is the act §4 above states (RMS §6.1, §13; Blueprint §13.11).

## 10. Relationship to Artifacts 056 and 058

**056.** Admitting a Kind decides no package. Package composition remains owned as Artifact 056
states it; the test's questions about identity, state and lifecycle do not select a package. A
package change is itself a schema change at Foundational ceremony (§13.6d), and a separate decision.

**058.** Question 7 asks *what references it*, and the answer is part of admission. This contract
establishes no general cross-model dependency or reference legality: that is Artifact 058's, under
RMS §22–23 (row 058: *"allowed/forbidden edges"*). 058 does not own the admission test.

## 11. Prohibited Architectural Moves

| # | Prohibited | Source |
|---|---|---|
| 1 | Treating a candidate as a Kind before it has been admitted | RMS §6.1, §13; Blueprint §13.11 |
| 2 | Treating classification as admission | Artifact 044 C-3 |
| 3 | A Kind spanning more than one Record Model | RMS §6.1; Artifact 044 §5 |
| 4 | A universal Kind taxonomy | RMS §4; Blueprint §13.7a |
| 5 | An external component defining a kind | I-84 |
| 6 | Admitting a World kind outside Foundational ceremony, or in one document only | §13.11; §13.7; I-71 |
| 7 | Retiring a Kind by deleting its records | §13.11; §29.4 |
| 8 | Reading a `KIND-DEFINITION` as the Kind's admission | §13.6e; Artifact 044 C-3 |
| 9 | Treating Kind admission as a package decision | §13.6d; Artifact 056 |
| 10 | Treating Kind admission as a cross-model dependency rule | Roadmap row 058 |

## 12. What This Contract Does Not Define

1. Any model's Kind roster. 2. Any Kind's meaning. 3. The `KIND-DEFINITION` specification or schema.
4. The ceremony for admitting a non-World Kind. 5. The mechanics of Foundational ceremony. 6. A rule
for judging an answer sufficient. 7. The STATUS and STRUCTURE rungs. 8. A retirement procedure.
9. Package composition or ownership. 10. Cross-model dependency rules. 11. The temporal obligation.
12. Relationship Record scope. 13. Schemas, fields, storage, APIs, serialization or code.
14. Any new constitutional invariant.

## 13. Conformance Conditions

Contract conditions, checkable against a construction. They are not invariants and mint no
invariant number. A construction satisfying all applicable conditions below is conformant to this
contract. World remains source-blocked to the extent described in §7: no condition binds either
question set to World.

| ID | Condition | Source |
|---|---|---|
| **C-057-01** | Every Kind declared in the E, P, R, V or I Kind taxonomy (rows 255, 298, 064, 344, 363) answers each of the fourteen questions. | RMS §13, §6.1; Roadmap row 057 `→`, `Done` |
| **C-057-02** | No candidate is treated as a Kind before it has been admitted. | RMS §6.1, §13; Blueprint §13.11 |
| **C-057-03** | Classification under Artifact 044 is not treated as admission. | Artifact 044 C-3 |
| **C-057-04** | Every Kind is a class of Record within exactly one Record Model. | RMS §6.1 |
| **C-057-05** | The architecture supports movement through the ladder in both directions, including downward movement when a Kind no longer justifies its structural cost. | RMS §13; P-7 |
| **C-057-06** | Admission of a World kind is a schema change at Foundational ceremony, landing in both documents in the same cycle. | Blueprint §13.11, §13.7; I-71 |
| **C-057-07** | Retiring a Kind deletes none of its records. | Blueprint §29.4 (*"everything admission does"*; *"never deleted"*); P-25 |
| **C-057-08** | A `KIND-DEFINITION` is not read as admission. This contract does not define or assign the Registry authority to admit another model's Kind. | RMS §6.1, §13; Blueprint §13.6e |
| **C-057-09** | No external component defines a kind. The condition is I-84's, at I-84's scope — external components — and is not a rule of definition ownership or admission. | I-84 |
| **C-057-10** | Admission decides no package composition, and this contract establishes no general cross-model dependency or reference legality, which Artifact 058 governs. | Blueprint §13.6d; Roadmap rows 056, 058 |
| **C-057-12** | No invariant is minted or amended. | Blueprint §36, §10.4; P-28; I-15 |

Conformance to this contract is not conformance to the Record System: the other P2 contracts
carry their own conditions.

## 14. Worked Examples

> **Illustrative and non-normative.** Each verdict below is the source's; none is decided here.

**Example A — admitted.** `SPECIES`, World. §13.11 runs its eight questions and records *"Eight of
eight. Admitted."* — among them: a species is not a property of its members (identity), and a
Registry classification *"carries no state, history, or relationships"*. The record shows §13.11's
test only; it does not settle how that test relates to RMS §13's fourteen questions.

**Example B — a state, not a Kind.** `BELIEF`. RMS §13 rejects it as *"a state"* (question 9, why
not a state); row 255 makes it *"explicitly not a Kind"* in E.

**Example C — derived, not a Kind.** `CONTEXT`. RMS §13 rejects it as *"derived"* (question 12, why
not a projection).

**Example D — composition, not a Kind.** `SECTION`, `PAGE`, `SPREAD`. RMS §13 rejects them as
*"composition"*.

**Example E — projection or subtype.** `VISUAL-DERIVATIVE`. RMS §13: *"projection or subtype"*
(questions 11 and 12).

**Example F — identity without a Kind.** WSV carries identity and is durable, and is *"World state,
not an instance-bearing Kind"* (RMS §7). Passing some questions is not passing the test.

## 15. Source Traceability

| Rule | Source |
|---|---|
| Kind: a class of Record within one model; passes the test | RMS §6.1 |
| The fourteen questions; every Kind must answer | RMS §13 |
| The ladder, both directions | RMS §13; Blueprint P-7, §13.6 |
| Admission obliges retirement | Blueprint P-25, §29.4 |
| Retirement never deletes records | Blueprint §13.11, §29.4 |
| World: eight questions, refusal names the rung, Foundational ceremony, both documents | Blueprint §13.11, §13.7; I-71 |
| World taxonomy established and closed | Blueprint §13.6; I-71 |
| Non-World rosters: boundary-naming, revisable by the model | Blueprint §13.6; I-106 |
| Non-World rosters: recorded CLOSED | RMS §8.1, §9.1, §10.1, §11.1, §12.1 |
| Kind Admission amendment for a future P object | RMS §9.1 |
| Issue's model-specific criterion | RMS §12.1 |
| Registry defines a kind; the model owns its Records | Blueprint §13.6e; I-105 |
| Kind ↔ KIND-DEFINITION lockstep | Roadmap LS-1 |
| No external component defines a kind | I-84 |
| No universal Kind taxonomy | RMS §4; Blueprint §13.7a |
| Classification is not admission | Artifact 044 |
| Rejections used as examples | RMS §13, §7; Blueprint §13.11; Roadmap row 255 |
| Invariants are the Blueprint's | Blueprint §36, §10.4; P-28; I-15 |
| Identity and acceptance | Roadmap row 057 |

## 16. Downstream and Adjacent Boundaries

| Artifact | Relationship to 057 |
|---|---|
| **044** architectural categories | hard dependency (`H: 044`); 044's C-3 sends a Kind candidate to *"the separate Kind Admission Test (Artifact 057)"*; row 044's `→` names *"057, all Kind work"* |
| **064 · 176 · 255 · 298 · 344 · 363** Kind taxonomies (R, W, E, P, V, I) | each names 057 as a hard dependency; E, P, R, V and I apply the fourteen questions to their own rosters; World's relation to §13.11 is §7's |
| **068 · 069** `KIND-DEFINITION` specification and schema | define a Kind's meaning in the Registry; not admission |
| **459** extensibility contract | names 057 as a hard dependency; states how a new Kind is added, each through its own ceremony |
| **054** temporal obligation | unaffected |
| **055** relationship boundary | unaffected; question 10 asks *why not a relationship*, and 055 owns the Relationship boundary |
| **056** package boundary | unaffected; admission decides no package |
| **058** cross-model dependency | unaffected; governs general cross-model dependency legality; question 7 remains part of admission |

## 17. Acceptance

| Roadmap row 057 | Where |
|---|---|
| `Val`: *"fourteen questions"* | §5; C-057-01, C-057-02 |
| `Val`: *"ladder both directions"* | §6; C-057-05 |
| `Done`: *"test binding"* | §5.2; C-057-01 |
| `→`: *"every Kind artifact"* | §5.2; §16 |

**Test binding is satisfied for E, P, R, V and I; World remains source-blocked because the
governing sources do not establish the relationship between RMS §13 and Blueprint §13.11** (§7).
This contract does not claim acceptance-completeness for World.

## 18. Final Contract Statement

Every E, P, R, V and I Kind answers the fourteen questions of RMS §13 before it is a Kind.
The ladder runs up and down: a concept enters at the lowest rung that carries it, and a Kind that
no longer justifies its structural cost is walked back down, deleting no records. A World kind is
admitted at Foundational ceremony in both documents; how RMS §13 and §13.11 relate for World is
unresolved by the current sources and is not decided here.
This contract admits no Kind, decides no roster or package, establishes no general cross-model
reference legality, does not define or assign the Registry authority to admit another model's
Kind, and defines no ceremony the sources leave undefined.

---

*Artifact 057 · P2/2d · Own: CONST · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a. This
document states the Kind admission test and its binding, derived from RMS §6.1 and §13 and
Blueprint §13.11, P-7 and P-25. It does not amend them and defines no roster, schema or ceremony.
Where it differs from the Master Blueprint, the Record Model System, or the OS File Build Roadmap,
those governing sources are correct and this document is wrong.*
