# COOLBOY12 — Constitutional Invariant Register

**Artifact 012** · `tests/constitutional/register.md` · Own: CONST · RM: n/a · T: test ·
R: VALID · SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0c ·
Req: BR-113 · BP: §36 · RMS: §26 · H: 011 · S: 004 · LS: — · G: gates every phase exit ·
→ all phases · Risk: HINGE · ∥: no

## Source and Authority

Every entry below is reproduced from **Master Blueprint v0.7.0 §36, Invariant Register**. The
register stands at **one hundred and eight** invariants: all 100 carried forward, none retired,
six amended in wording, and eight added (I-101–I-108).

The Blueprint governs. §36 states its own standing, and it applies to this file too:

> This section adds no new rule — it is an index, and where it appears to differ from the
> defining section, the defining section governs.

This file is the repository's register **of** that source. It is authoritative as the register —
downstream artifacts cite these IDs — and it is not a second constitution. It adds no invariant,
retires none, renumbers none, and reworders none. Where this file and the Blueprint differ, the
Blueprint is right and this file is wrong.

Cross-checked against **RMS v1.0 §26**, which names a subset (I-16, I-71, I-72, I-82, I-87,
I-90, I-101–I-108) as system-wide. RMS names fewer than the Blueprint; that is a subset, not a
contradiction, and the full Blueprint register is preserved here.

## Register Scope

This file records **what the invariants are**. It records no execution outcome.

No entry here carries PASS, FAIL, or not-yet-testable. Those are results, produced when a check
runs, and the mechanism for producing them is Artifact 011
([`harness.py`](harness.py) — `run_check(entry, check)` and
`not_yet_testable(entry, reason)`). The presence of an invariant below is not evidence that the
implementation satisfies it.

Entry IDs are canonical and stable in exactly one form — `I-01` … `I-108` — so a downstream test
can reference an entry without rewriting this register.

**Ordering follows the Blueprint.** §36 groups invariants into thematic and by-revision
subsections rather than one ascending run, so I-101–I-108 appear under §36.3a/§36.3b between
§36.3 and §36.4, exactly as the source places them. The `Where` column is the Blueprint's own
mapping for each entry, reproduced unchanged.

---


## Blueprint §36.1 — Truth and Authority

| # | Invariant | Where |
|---|---|---|
| I-01 | Exactly one canonical truth exists; nothing else is authoritative about the world. | Spine 1 |
| I-02 | Canon changes only through propose → check → gate → commit → changelog → History Record → memory, atomically. | Spine 2, §12.6 |
| I-03 | Only the Authority commits, and there is exactly one Authority at a time. | Spine 3, §10.1 |
| I-04 | Nothing becomes canon by inference, publication, simulation, import, or automation. | Spine 6, §20.4 |
| I-05 | Foundation truths change only by Foundation ceremony; a Foundational change is never batched. | Spine 4, P-23 |
| I-06 | Published artifacts never become canon; publication writes nothing to canon. | Spine 5, §20.4 |
| I-07 | An unresolved same-tier conflict becomes CONTESTED; recency never decides truth. | §12.2 |
| I-08 | Current canonical state is authoritative; history explains it and never establishes it. | P-17, §12.9 |

## Blueprint §36.2 — Traceability and History

| # | Invariant | Where |
|---|---|---|
| I-09 | Every canonical state answers: what changed, when, why, who approved it, what caused it. | P-18 |
| I-10 | Authorial intent is a valid terminal cause; fabricated causality is a violation. | §5.2, §15.13 |
| I-11 | **(scope flagged v0.7.0 — AD-11)** Every **World** Record has exactly one logical history record, append-only and owned by Canon — the History Record for the seven instance-bearing kinds, WSV-H for WSV. Every Record Model must satisfy P-18 in full; the packaging of its temporal account is model-owned (§13.6d). | §12.9, §13.10, §13.6d |
| I-12 | Compaction may remove detail, never the existence of a revision, and never the P-18 answers. | §12.9, §12.14 |
| I-13 | No history is ever orphaned: every predecessor history is reachable from its successors. | §13.8 |
| I-14 | Approval mode is recorded, not merely the fact of approval. | P-23, §12.7 |
| I-15 | Amendments to this blueprint satisfy P-18 at a ceremony above Foundational. | P-28, §10.4 |

## Blueprint §36.3 — Classification and Boundaries

| # | Invariant | Where |
|---|---|---|
| I-16 | **(amended v0.6.1; amended in wording v0.7.0)** Every Record carries exactly one partition — World, Epistemic, Production, Registry, Visual Library, or Issue — and every partition owns exactly one sovereign Record Model. Cross-partition conversion is prohibited. | §13.6, §13.6a, §13.6c, §13.2 |
| I-17 | World records are manifestation-blind absolutely; no field may reference an issue, tier, medium, or artifact. | §11, §13.6 |
| I-18 | Any state recording an authorial act is Production State and survives every rebuild. | P-26, §9.1 |
| I-19 | Derived state is exactly what can be recomputed with no loss; if it cannot be, it was misfiled. | §12.4 |
| I-20 | Every capability declares its current; failure posture follows from it. | P-19, §8.4 |
| I-21 | Every cross-cutting capability has exactly one owning domain. | §9.2 |
| I-22 | Nothing is admitted as a domain that does not pass all five domain tests. | §9.3 |

## Blueprint §36.3a — Rules Added by v0.7.0

| # | Invariant | Where |
|---|---|---|
| I-101 | Every partition owns exactly one sovereign Record Model. No Record Model is a specialization of another, and no Record Model is the template for another. | §13, §13.2 |
| I-102 | Relationship Record and History Record are World Record Model concepts. Neither is a Record System primitive, and neither may be required of another Record Model. | §13.9, §13.6d |
| I-103 | A mechanism may be shared across Record Models; a semantic may not be shared without evidence in each model that carries it. Shared infrastructure never confers shared meaning. | §13.7a |
| I-104 | Record and Canon are not synonyms. Canonicality is a status property whose meaning is defined by each Record Model that has one, and two models hold Records that are never canonical. | §13.0, §13.7c |

## Blueprint §36.3b — Rules Added by the v0.7.0 Constitutional Revision

| # | Invariant | Where |
|---|---|---|
| I-105 | Registry is a sovereign Record Model. Its definitions are Records, not configuration. Registry holds semantic authority over definitions and never semantic ownership of another model's Records. | §13.6e, §9.4 |
| I-106 | A kind roster that is listed is not thereby frozen. Only the World taxonomy is established; every other roster names a boundary and is revisable by that model's own design work until it declares otherwise. | §13.6, §13.6a, §13.11 |
| I-107 | A package composition declared for a Record Model that has not been independently designed is provisional and may not be implemented as a requirement. | §13.6d, FG-V7-06 |
| I-108 | No Record carries a WSV attribute by default. An indicator definition is a Registry Record; an indicator value is World-state; neither is a universal field. | §13.6e, §13.10, I-91 |

## Blueprint §36.4 — Change, Time, and Scale

| # | Invariant | Where |
|---|---|---|
| I-23 | Every proposal declares its basis state and is re-validated if canon has moved. | P-22, §12.6 |
| I-24 | Every acceptance is causally closed or explicitly re-caused. | §15.13 |
| I-25 | **(amended v0.5)** Every temporal statement names its axis; unaxised temporal claims block. | P-21, §12.16 |
| I-26 | Canonical consequence commits atomically; derived recomputation may be eventual and is stale-marked. | §10.2 |
| I-27 | A retcon is at least Structural, dispositions every dependent, and never rewrites artifacts or history. | §12.12 |
| I-28 | Refactoring never changes what is true, never orphans history, never leaves a dangling reference. | §12.13 |
| I-29 | Operational Rollback, Canonical Reversion, and Historical Replay are never named or implemented as one thing; there is no undo. | §12.10.1 |
| I-30 | Epochs never delete history and never reset canon. Compaction may compress detail but never removes a revision's existence or a causal link's identity. | §12.9, §12.14 |

## Blueprint §36.5 — Knowledge and Reading

| # | Invariant | Where |
|---|---|---|
| I-31 | Truth and knowledge-about-truth are separate records, connected by reference, never merged. | §14, §13.6 |
| I-32 | Every epistemic transition has an evidence path or an authored decision. | §14.6, §14.7 |
| I-33 | Reader knowledge changes canon only through a gated Reader Knowledge Proposal. | §20.4 |
| I-34 | Epistemic tracking is selective, criterion-recorded, and budgeted. | §14.17 |
| I-35 | Modelled reader state is an assumption and is labelled as one everywhere it is shown. | §20.6, §27.2 |
| I-36 | Withheld canon is excluded from every role context by default; inclusion is justified and recorded. | §24.7 |
| I-37 | Leakage of hidden canon is a structural violation and blocks where determinable from structure alone; where establishing it requires interpreting prose or an image, it is a judged finding at high severity. | §14.16, §24.7, P-24 |

## Blueprint §36.6 — Operation and Survival

| # | Invariant | Where |
|---|---|---|
| I-38 | Fail closed toward truth; fail open toward artifacts; reduced output is marked reduced. | P-19 |
| I-39 | No canonical guarantee depends on model determinism; replaying a record is not re-running a simulation. | P-20, §15.15 |
| I-40 | Canon, history, Production State, and Memory remain legible without the running system. | P-27, §26.3 |
| I-41 | No external dependency holds any of them in an unrecoverable form; every adapter declares an exit path. | §26.3 |
| I-42 | The universe is always readable, in every degraded mode. | §28.3 |
| I-43 | A role that cannot obtain sufficient context says so and stops; it never substitutes recollection. | §21.7, §24.6 |
| I-44 | Autonomous work may compute, never commit, and always declares its basis. | §21.5 |
| I-45 | Structural violations block with no override; judged findings are adjudicated and recorded. | P-24, §19.1 |
| I-46 | Every extension point that admits also retires; nothing is deleted, only frozen, migrated, or converted. | P-25, §29.4 |
| I-47 | Every override is dated and reviewed at the next epoch transition. | §29.4 |
| I-48 | Every standing signal, check, and projection has a named consumer or is retired. | P-10, §29.5 |

## Blueprint §36.7 — Rules Added by the v0.4 Constitutional Repair

| # | Invariant | Where |
|---|---|---|
| I-49 | The convictions resolve in a fixed precedence: II → V → I → IV → III. | §5.1 |
| I-50 | A violation is structurally decidable only if determinable from structure alone, without interpreting prose, image, or narrative meaning. | P-24 |
| I-51 | A batch is performed at its highest member severity; Structural members are individually reviewed within it; Foundational members are never batched. | P-23, §12.7 |
| I-52 | Production ceremony mutates Production State only: no severity, no gate queue, no history entry, no propagation, freely reversible, and never any effect on canon. | §9.1 |
| I-53 | Replay reconstructs past states read-only and always Derived; current canonical state is never reconstructed. Replay never promises granularity it cannot evidence. | §12.10.1 |
| I-54 | A CONTESTED fact may not be cited as settled, may not premise a commit, a simulation, or a publication, and propagates to dependents as a marked dependency rather than as contestation. | §12.2 |
| I-55 | A pending Reader Knowledge Proposal may inform planning marked provisional and may never premise a simulation, a publication, or a canonical commit. | §20.4 |
| I-56 | Query order is binding: Canon for what is true, history for what happened, Creative Memory for why — and every capability reading them declares its order. | §22.5 |
| I-57 | Creative Memory has exactly two write classes — committed and standalone — identical in authority and both append-only. | §22.5.1 |
| I-58 | A rejected antecedent whose dependents were accepted under re-causation is recorded with its reason. | §15.13 |
| I-59 | Context is never silently truncated: what was dropped is recorded and the output is marked reduced. | §24.7 |
| I-60 | Primitives are fixed at two; a third requires Constitutional Amendment. | §9.3 |

## Blueprint §36.8 — Rules Added by the Round 2 Repair

| # | Invariant | Where |
|---|---|---|
| I-61 | Publication has three planes: the artifact and publication history are Production State; the in-world act is canon and exists only when the author proposes it. Shipping never creates a world fact. | §17.7.1, §12.4, §20.4 |
| I-62 | **(amended v0.5)** Evidence comes in two classes: reader evidence (artifact source, tier reach, **issue ordinal**) for outside-world knowers; world evidence (in-world occurrence, in-world reach, world-time) for in-world knowers. Neither serves the other's knowers, and crossing between them is authored. | §14.7 |
| I-63 | In-world knowledge changes by an ordinary gated canon proposal; outside-world reader knowledge changes only by a gated Reader Knowledge Proposal. | §14.7, §20.4 |
| I-64 | An unavailable substrate closes the descending current; Manual Ceremony is a composition and is unavailable without a substrate. | §10.3, §28.3 |
| I-65 | An aggregate approval is one transaction: all members land or none. Exclusions happen before the gate and are recorded; after the gate there is no partial commit. | §12.7 |
| I-66 | Authoring-time is a single monotonic ordering across all epochs; epoch boundaries partition the record, never the ordering. | §12.16 |
| I-67 | CONTESTED marks direct dependents and does not propagate transitively; the premise block reaches any depth; a contested object remains canon, marked. | §12.2 |
| I-68 | A replayed state may be an input to reasoning and may never be a proposal's basis. | §12.10.1, P-22 |
| I-69 | A published artifact is corrected only by a superseding publication; the original is never edited and a production record is never retconned. | §18.7 |
| I-70 | Succession creates no boundary in canon or history; a successor holds the same powers as the predecessor, no more and no fewer. | §10.1 |

## Blueprint §36.9 — Rules Added by v0.5

| # | Invariant | Where |
|---|---|---|
| I-71 | **(amended v0.6)** The World kind taxonomy is closed at seven instance-bearing kinds, beside which WSV is a singleton and not a kind. An eighth instance-bearing kind passes all eight admission questions, at Foundational ceremony, and lands in the Blueprint and the Record Model Schema in the same cycle. | §13.6, §13.11, §13.7 |
| I-72 | **(scoped v0.7.0)** Every **World** Record is a package: `Record + Relationship Record + History Record` for the seven instance-bearing kinds, `Record + WSV-H` for WSV. No World Record exists whose relationships or history cannot be located from it, and none exists orphaned. Packaging in the other five Record Models is model-owned (§13.6d). | §13.9, §13.10, §13.6d |
| I-73 | **(scoped v0.7.0)** Wherever a Record Model uses Relationship Records, a relationship is authoritative in exactly one Relationship Record, determined by the Registry type definition's owning role. The non-owning endpoint's view is Derived and never authoritative; an edge authoritative in two Relationship Records is a structural violation. | §13.9 |
| I-74 | **(scoped v0.7.0)** Wherever a Record Model uses Relationship Records, a Relationship Record holds current relationships only. Every relationship change is recorded in the owning object's history; a Relationship Record that grows with relationship history has been implemented wrongly. | §13.5, §13.9 |
| I-75 | Registry dependency runs downward only: a Registry definition never references a kind, a subtype, or an instance; a kind never references an instance. | §9.4 |
| I-76 | Every Reality Anchor carries a non-empty transformation, checked structurally. Real-world sources are authoring provenance only; no World record may reference the real world in any field a reader could reach. | §11.1, P-29 |
| I-77 | No capability delivers canon to a reader as canon. The public surface's exposure set is closed — published artifacts and their content, nothing else — with no discretionary inclusion path. | §5.3, P-30, §27.5, §24.7 |
| I-78 | No belief, theory, published claim, reader signal, or popularity changes what is true except by an authored change through the gate with a recorded reason. | §14.19, §20.8 |
| I-79 | A quantity has exactly one canonical home — an object's world-state fields or WSV, never both. Simulation holds no state that survives the gate. | §15.16 |
| I-80 | World causality lives in `EVENT` and in causal and pressure edges. History records that the *record* changed and is never read to establish causality about the world. | §13.12, §12.9 |

## Blueprint §36.10 — Rules Added by v0.6

| # | Invariant | Where |
|---|---|---|
| I-81 | Issue is not Canon. Nothing is true because it was published. An issue may reference a World record; it never owns one, and no World record may reference an issue. | §13.6a, §11 |
| I-82 | Identity is partition-first and stable: `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]`. A rename never creates a new canonical identity, and an internal machine identifier never replaces or contradicts the canonical one. | §13.9a |
| I-83 | The Mutation Coordinator is the only component that writes canon. Stages may be delegated to external components; the write boundary may not. Execution-substrate guard rails are defence-in-depth, never constitutional authority. | §12.6 |
| I-84 | No external component holds canonical semantics, defines a kind, owns a relationship, adjudicates a mutation, or is the only place a canonical fact exists. Every external store is DERIVED or CACHED, never AUTHORITATIVE, and the system remains fully recoverable if it is deleted. | P-31, §26.2a, §26.2d, §29.6a |
| I-85 | **(scoped v0.7.0)** Version control records that files changed; a Record Model's own temporal mechanism — the History Record and WSV-H in World — records what canonically changed and why. Semantic history is never reconstructed from a commit log. Correlation may be recorded in one direction only, from history entry to commit. | §26.2e |
| I-86 | A timestamp produced by an external system is operational metadata. It becomes World Time, Session Number, or Real-World Time only by being recorded as such through the mutation path — never by having been generated by a tool. | §12.16, §26.2e |

## Blueprint §36.11 — Rules Added by v0.6.1

| # | Invariant | Where |
|---|---|---|
| I-87 | **(amended v0.7.0)** Record is the common **architectural** data unit of the Record System — not a universal semantic model. Every Record belongs to exactly one of six partitions; **the semantics of a Record are owned by its Record Model**; and Record is not synonymous with World Truth. | §13, §13.6, I-101 |
| I-88 | The Registry owns meaning, never world truth. A registry definition never asserts a fact about the world, and no world record is resolved by reading one as though it were. | §13.6, §9.4 |
| I-89 | The Visual Library is never independently a truth authority. A canonical visual specification is canon; an asset is a manifestation; an analysis is an observation. Vision produces observations and proposals, never canonicalization. | §13.6c, §18.11 |
| I-90 | **(amended v0.7.0)** Package composition is owned by each Record Model; the relationship-ownership rule is not. Wherever a Relationship Record exists, exactly one authoritative edge lives in exactly one Relationship Record, declared by its relationship type. **Traceable evolution (P-17, P-18) is required of every Record Model; the mechanism is model-owned. The History Record is the World Record Model's mechanism and is not required of any other model.** | §13.6d, §13.9, §13.7a |
| I-91 | Indicator meaning lives in the Registry, indicator behaviour in a Simulation Model definition, current value in WSV, and transitions in WSV-H. No two of these may hold the other's content, and WSV is never a general analytics store. | §13.10, §15.17 |
| I-92 | Every committed world-state transition can name the model, dependency, driver, and causal chain that produced it. A transition that cannot is a P-18 failure and does not commit. | §15.20, §13.12 |
| I-93 | Unresolved model conflict is surfaced, never averaged. Where declared dependency, ordering, coupling, convergence, and precedence do not settle a conflict, simulation stops and reports it with its contributing chains. | §15.18 |
| I-94 | Real-world calibration is evidence about a model's internal coherence, never authority over the world's behaviour. A calibration finding never overrides an authored world fact. | §15.21 |
| I-95 | Taste criteria, the taste corpus, writer personas, and art direction are Production. None asserts anything about the world, and real-world material reaches the world only through a recorded anchor transformation. | §17.17, §17.18, §17.19, §18.12 |
| I-96 | A capability is admitted at the lowest rung that carries it and creates no domain, engine, or subsystem; and no capability is dropped in order to reduce architectural labels. | P-32, §9.3 |

## Blueprint §36.12 — Rules Added by v0.6.2

| # | Invariant | Where |
|---|---|---|
| I-97 | A taste criterion is editorial guidance and is never canon. It constrains how the work is made, asserts nothing about the world, and enters governance as a judged finding that the author may override with a recorded reason. | §17.17, §19 |
| I-98 | A Writer Persona never redefines Character canon. A persona describes how someone writes; what is true of that person is a World record, and a persona's claims about its own author are Production, not fact. | §17.19, §13.6 |
| I-99 | Public Sphere state and Reader Knowledge are never derived from one another in either direction. What the world's public believes is a simulated in-world condition; what a reader tier knows is an out-of-world epistemic state reached only through published artifacts. Neither is evidence for the other. | §15.17, §14.7 |

## Blueprint §36.13 — Rules Added by v0.6.3

| # | Invariant | Where |
|---|---|---|
| I-100 | The execution environment runs coolboy12 and does not define it. It is not a domain, partition, engine, or primitive, and it owns no coolboy12 semantics. Its guard rails are defence-in-depth; where a guard rail and the Human Gate disagree, the gate governs. The architecture must remain valid when the environment is replaced. | P-33, §9.5, §26.8 |

