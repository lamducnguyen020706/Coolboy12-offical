# coolboy12 v0.7.0

### A Single-Author Universe Operating System
#### Complete Architectural Blueprint · v0.7.0 · Canon Object Model → Record System

> **v0.7.0 supersedes v0.6.3 at the architectural level.** The **Canon Object Model is superseded and retired** as the governing architecture. The **Record System** is the governing architecture, under which **six sovereign Record Models** — World, Epistemic, Production, Registry, Visual, Issue — coexist without any being a specialization of a universal object. **World remains the most mature model** and its valid semantics are preserved and re-expressed, not redesigned. v0.6.3 remains historically valid as the predecessor document.
>
> **What this revision does not do, stated so that it cannot be assumed.** Implementation migration is **not** performed. Artifacts **001–032 have not been audited**; implementation impact remains to be established by the subsequent repository audit. The **Roadmap has not been revised**. **Artifact 033 has not been finalized.** The companion **Record Model Schema** (formerly the Canon Object Model file) **has not been revised**, leaving the §13.7 lockstep in a known-outstanding state (FG-V7-01). Detailed schemas for the five non-World models remain **OPEN** exactly where v0.6.3 left them.
>
> **Amendment status.** This revision is a Constitutional Amendment under §10.4 in respect of the governing object architecture. The Spine remains **ten laws, unamended**. No invariant is retired; two are amended in wording (I-11 scope, I-16); eight are added (I-101–I-108); Registry is established as a sovereign Record Model (§13.6e). One invariant-scope ambiguity is recorded rather than resolved (**AD-11**, §36.2).

| Parameter               | Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System name             | coolboy12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Version                 | v0.7.0 (architectural supersession of v0.6.3; constitutional core still frozen; Canon Object Model retired; Record System governing; six sovereign Record Models) · *predecessor:* v0.6.3 (evolution of v0.6.2; constitutional core still frozen; capabilities realized against named external components behind adapters; the Claude Code execution environment made explicit; Simulation model architecture specified in depth)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Class                   | Single-Author Universe Operating System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Designed for            | One creator · a proactive AI staff of reasoning roles · a multi-decade living universe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Reasoning substrate     | Exactly one, bound at the adapter layer (Section 26.1). Every coworker is a role it executes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Informed by             | v4.2 (The Overtone), TOOS V7 FINAL, superman00053 vNext2.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Organizing idea         | The Creative Flywheel — optimize the loop, not the tools                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Canonical language      | English (source of truth)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Implementation status   | **Nothing in this system has been implemented.** coolboy12 is at the master-blueprint stage. No partition, engine, registry, or schema described here exists as running code, stored data, or a deployed artifact. A blueprint may be complete before an implementation exists, and this one is written to be.                                                                                                                                                                                                                                                                                                                                                         |
| Blueprint status        | The Spine and the truth substrate remain **frozen**. **This revision supersedes the governing object architecture and changes nothing that does not follow from it.** Forensic audit performed and its findings repaired; **AD-1 resolved — one universal identity grammar, model-owned semantics**. The Canon Object Model is retired; the Record System governs; six Record Models are sovereign; Relationship Record and History Record are World Record Model concepts and are not universal primitives; shared infrastructure is separated from shared semantics (§13.7a); Canon and Record are held apart (§13.0). Prior status, carried:  Identity kind codes are frozen at two characters; `kind` + `<kind>_type` replaces the unresolved specialization question; visual reference policy is Registry-defined; WSV-H is one entry per simulation tick; epistemic state is subject-relative; the Registry and Record Model Schema are built in lockstep from a bootstrap contract rather than sequentially; the worked example now traverses all six partitions; and repository integration metadata is normalized. No section added, renumbered, or reorganized. |
| Audit compliance        | Carries forward all v0.3.1, v0.4, and Round-2 adversarial audit resolutions (maps: Sections 35.2–35.4) and records the v0.4.2 → v0.5 audit and decision resolution (Section 35.5).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Closed in this revision | **O-01** two-character kind codes · **O-02** `kind` + `<kind>_type` · **O-03** Registry-defined visual reference policy · **O-05** one WSV-H entry per tick · **O-06** subject-relative epistemic state · **O-07** Department as stable editorial identity · **F-01** normalized repository metadata · **F-03** six-partition worked example · **F-08** Registry/COM lockstep with a bootstrap contract · capability count reconciled to 104.                                                                                                                                                                                                                          |
| Carried from v0.6.2     | Adapter contract specifications · the integration compatibility rule · five recorded architectural conflicts · Mystery as an Epistemic structure · the rebuild-from-canon drill · I-97–I-99.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Carried from v0.6.1     | Six partitions · package specialization, reclassified at v0.7.0 as model-owned packaging · WSVR in Registry · the Simulation Model architecture · editorial taste, writer persona, and visual intelligence · P-32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Carried from v0.6       | The Issue partition · seven instance-bearing World kinds plus the WSV singleton · partition-first identity grammar · the Mutation Coordinator · source-of-truth classification · external dependency boundaries · the anonymisation test · P-31.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Carried from v0.5       | The World taxonomy consolidation and its re-homing map · the World Record package model (Record / Relationship Record / History Record, rescoped to World at v0.7.0) · the canonical temporal axes · the Registry layer · Reality Anchoring · Historical Divergence · Species and the chapter trajectory · Pseudo-Science Governance · the Publication Artifact Model · the two-surface boundary · P-29 and P-30.                                                                                                                                                                                                                                                                                                                                 |

> coolboy12 v0.3 changes nothing about *what may not be violated* and deepens almost everything about *how the world is reasoned through*. The universe is the source; the magazine is the primary lens; the author expresses intent, and the system composes the work; and nothing becomes true without the author's word.
>
> coolboy12 v0.3.1 adds one clause to that sentence and nothing else: the world's *current* truth is authoritative, and the world's *evolution* toward that truth must always remain explainable.
>
> coolboy12 v0.4 changes no law and adds no domain. It closes the places where the document contradicted itself, decides the constitutional questions it had left open, and gives the author the instruments the system had described but not yet provided.
>
> coolboy12 v0.5 changes no law and adds no domain either, and it is the first version to get *smaller* where it counts. The World ontology contracts from eighteen kinds to eight, not by deletion but by finding each retired kind its correct home as a subtype, a field, or a Concept — and the contraction is a gain, because the kinds that leave were the ones straining hardest against their partition. The four clocks become three. In exchange, v0.5 architects the half of the project the earlier versions described only in passing: how a world anchored in real history diverges from it, how a society reveals itself through the ordinary artifacts it produces, and how a magazine that never physically existed can be handed to a reader as though it had been printed, bound, and scanned.
>
> coolboy12 v0.6 changes no law and adds no domain either. It makes one structural admission and one correction, and spends the rest of its length on a boundary the earlier versions never had to draw. The admission is **Issue**: the concrete published artifact — its sections, articles, pages, advertisements and visual material — is not the plan that produced it and is not the world it describes, and giving it its own partition stops the magazine from slowly becoming a second canon database. The correction is that the World Canon has **seven instance-bearing kinds**, and WSV is a singleton world-state record rather than an eighth kind — v0.5 had already built it that way and had not said so plainly. The boundary is the one that matters for everything that comes after this document: the system will eventually be built out of components it did not write, and this version fixes, in advance, what those components may do. They may provide capability. They may never hold authority. An index may be deleted and rebuilt; a canon may not.
>
> coolboy12 v0.6.1 changes no law and adds no domain, and it is the version in which the object model finally becomes what its name always claimed. A **Canon Object** is not a world-truth record that other things sit beside; it is the universal data abstraction, and everything the system holds is one — across six partitions. *(Historical statement, preserved as written. **This claim was superseded at v0.7.0** — the Canon Object Model is retired and the Record System governs; see §13 and §35.11.)* Registry and Visual Library stop being infrastructure the architecture mentions and become partitions the architecture governs, which matters because a definition and an image both carry meaning, both have provenance, both have history, and both were previously governed by convention rather than by rule. Alongside that, Simulation stops being an engine of change and becomes a **model architecture**: named model families that feed each other, disagree with each other, and must be calibrated, observed, and reconciled. And the publication layer acquires the faculties a magazine actually needs — taste learned from real publications, writers with voices that evolve, and a visual library that can tell you whether this month's drawing of a character contradicts last year's. **Nothing from v0.6 is dropped.** The rule that governs all of it is the one the version had to state twice: a capability is not an engine, and the inventory grows without the architecture growing with it.
>
> coolboy12 v0.6.2 is the version that was allowed to change nothing. Its job was to take an audited set of external capabilities — extraction, embeddings, indexes, graph traversal, simulation numerics, rendering, viewers — and specify how each attaches without any of them acquiring authority. The interesting output is therefore not what was integrated but what was **refused**: five candidate components would each have required a semantic change to fit, and all five were recorded as architectural conflicts and declined rather than accommodated. What was integrated attaches at an adapter, carries a source-of-truth class, declares a degraded mode and an exit path, and is deletable. The one substantive addition is unrelated to any component: **Mystery** finally has an explicit structure in the Epistemic partition, which is where v0.5 put it and where it had since lived without a specification.
>
> coolboy12 v0.6.3 is where the blueprint stops being purely conceptual without becoming an implementation. Three things change, and none of them is architectural. Every capability that a component can realize now **names** that component and fixes the boundary it sits behind — no more "a vector index" and "an OCR library", but the actual thing, with its disposition, its input and output contract, its source-of-truth class, its failure mode, and the path by which it can be removed. The **execution environment** becomes explicit: coolboy12 is built and operated inside Claude Code, and the blueprint says exactly what that means and — more carefully — what it does not. And **Simulation** finally gets the specification the rest of the system has had since v0.5: a model is a structured definition with indicators, dependencies, equations, thresholds, feedback loops, and mappings, and there are thirty-seven families of them.
>
> The ordering that governs the whole version, and the one thing a reader should carry away from it: **the author builds coolboy12 with AI assistance inside Claude Code; coolboy12 uses external components behind adapters.** Claude Code runs coolboy12. It does not define it. A component supplies a computation. It does not supply a meaning.

---

## 1. One-Line Definition

**coolboy12 is the operating system a single author uses to build, simulate, govern, and manifest one living fictional universe across many media and many years — keeping the universe coherent while it becomes richer, deeper in time, and truer to its own causality.**

The author expresses *what* they want; the Workflow Composer turns it into work; Simulation makes the world move through time like a world; and the single human gate is the only path by which anything becomes true.

---

## 2. Vision

A single author, working with AI as a staff of specialist reasoning roles rather than a set of tools, can build and sustain a living fictional universe of civilization scale — and can project it into magazines, games, ARGs, films, novels, podcasts, sites, and forms not yet invented — **without ever fragmenting the world, eroding its coherence, or losing the thread of why it became what it is.**

Beneath the author sits a system whose core is not a content pipeline but a *world*: a canon-governed, causally simulated universe that can be advanced across centuries or steered toward an intended end-state, that generates its own story material, that separates cleanly what is true from what is known and by whom, and that remembers why every decision was made. The number of manifestations can grow without limit while the number of *truths* stays exactly one.

**The far ambition (v0.5).** The measure of success is not a well-organized fictional universe; it is a **cultural artifact** — a publication that reads as though a society produced it, accessible to a casual reader on its surface and inexhaustible to an obsessive one underneath. That ambition constrains the architecture rather than decorating it: a system that can only deliver the world *explained* cannot produce an artifact anyone would mistake for real. The architecture below is judged by whether a reader could encounter its output cold, with no lore, and find it worth reading anyway.

---

## 3. Mission

To keep one creator in a state of **sustained, high-quality, long-horizon creation** by doing seven things they should never have to hold in their head at once:

1. **Compose** the author's intent into the right multi-domain workflow, so the author expresses *what*, never *how*.
2. **Simulate** the world through time — forward across a span, or toward an intended end-state — so consequences unfold with real causality.
3. **Surface** the story material the moving world has produced, so the author discovers rather than invents.
4. **Decide**, at the editorial layer, *what should be told, in what form, and at what time* — and what should wait.
5. **Govern** canon and quality mechanically, so coherence is enforced and taste is diagnosed with reasons.
6. **Manifest** the world into any medium from a single source, so nothing fragments.
7. **Remember** every decision, intention, rejected path, and lesson, so the intelligence behind the work compounds while the work is published.

Everything in coolboy12 serves those verbs. Anything that serves none of them does not belong.

---

## 4. North Star

**A richer, deeper, more causally honest universe — and a lighter author.**

Every decision is judged by one compound question: *does this make the universe deeper and more coherent while making it easier — not harder — for one person to operate over a decade?* v0.3 adds a temporal clause: *and does it make the world's movement through time more believable without asking the author to track more?* Depth that costs comprehension is off-mission. Realism that costs operability is off-mission. The intersection is narrow on purpose.

As a test, every feature, mechanic, object kind, or rule must answer **yes** to all seven questions or it does not ship:

1. Does this make a **richer universe**?
2. Does this **reduce cognitive load**?
3. Does this improve **long-term coherence**?
4. Does this help **creative discovery**?
5. Does this improve **editorial quality**?
6. Does this improve **AI collaboration**?
7. Does this help the author **return after months or years**?

A "no" on any single question is a strong signal the thing should not exist. This is invoked throughout as **the North Star Test**.

### 4.1 The Cost Test (v0.4)

The seven questions measure only benefit. A system that can admit but cannot decline on cost ratchets in one direction and, over a decade, becomes heavy by accumulation of individually justified additions. Every feature, mechanic, kind, or rule must therefore also answer three questions about what it *costs*:

8. **What does this cost to operate, every week, forever?** Not to build — to keep. A capability with a standing weekly cost must return a standing weekly benefit.
9. **Is this reversible?** Can it be retired without corrupting canon, orphaning history, or stranding an author mid-arc? Irreversible additions require the ceremony their permanence deserves (Section 29.4).
10. **What does it oblige the author to do that they were not already doing?** A capability that adds a recurring obligation has spent the scarcest resource in the system: one person's attention.

An idea passing all seven benefit questions and failing question 9 is not admitted at all; an idea failing question 8 or 10 is admitted only with a named consumer (P-10) and a retirement path (P-25).

### 4.2 Periodic Re-Justification

Passing the test once does not confer permanence. At each **epoch transition** (Section 12.14) the standing capability inventory is re-asked the North Star Test *as it is used today*, not as it was proposed. Anything that no longer earns its place is retired through the contraction path (Section 29.4) rather than left running. This is the only mechanism the system has for getting smaller, and a system that cannot get smaller will eventually get unusable.

**v0.5 is the first exercise of this clause at ontology scale.** The World kind taxonomy was re-asked the North Star Test as used, not as proposed, and ten of eighteen kinds failed question 2 or question 8 — they added a discriminator the author had to hold in mind and returned no capability a subtype could not. Section 13.6 records the contraction and where each concept went. Nothing was deleted; the ladder was walked downward instead of upward, which is what P-7 always intended and what no prior version had ever actually done.

---

## 5. Core Philosophy

Five convictions. Everything downstream is a mechanical form of one or more of them; v0.3 deepens their mechanics without touching the convictions.

**I. Universe First.** The world precedes and generates all story. You never design around an artifact. You make a decision about the world — or advance the world through time — and story falls out of the change. A system that starts from the artifact drifts, over a decade, into a pile of artifacts with no world beneath them.

**II. Canon Is Sovereign.** There is exactly one canonical truth, it lives in one place, and it changes through one gated, transactional path with the author's explicit confirmation. No duplicate truths, no parallel canon, no AI-authored canon. Coherence at civilization scale cannot be maintained by diligence; it must be enforced.

**III. The Loop Is the Product.** coolboy12 optimizes one loop — the Creative Flywheel (Section 8). A thing that spins the flywheel faster is on-mission; a thing that produces output without spinning it is off-mission. The health of the loop is the health of the system.

**IV. Intelligence Compounds; Artifacts Depreciate.** A published issue begins losing value the moment it ships. The reasoning behind it — the alternatives weighed, the decision made, the intention held, the path rejected — appreciates, if it is kept. coolboy12 treats the intelligence about the work as the appreciating asset and the work as its derivation.

**V. The Author Decides; The System Calculates.** AI is a proactive staff — it recommends, questions, challenges, critiques, simulates, and warns without being asked. But it owns no truth. Authority over the world is human, final, and non-delegable. The staff proposes; the author disposes; the system computes the consequences of what the author chose.

**A clarification on Convictions II and IV (v0.3.1).** The convictions are unchanged; one consequence of holding them together is now stated explicitly, because it was assumed rather than written. Canon Is Sovereign means the *current* canonical state is the single authority about the world. Intelligence Compounds means the reasoning behind that state is the appreciating asset. Read together they entail a third thing: **coolboy12 does not merely preserve canonical truth — it preserves the explainable evolution of canonical truth.** Current state and evolutionary history are separate logical concerns. Current state is authoritative; history explains how the current state came to exist. Neither substitutes for the other, and history never becomes a second source of truth.

### 5.1 Precedence Among the Convictions (v0.4)

The convictions are not co-equal in a conflict, and pretending otherwise leaves the resolution to whoever is implementing that week. The binding order, highest first:

**II (Canon Is Sovereign) → V (The Author Decides) → I (Universe First) → IV (Intelligence Compounds) → III (The Loop Is the Product).**

The reasoning is failure asymmetry. A violation of II corrupts everything downstream and is often undetectable for years. A violation of V produces a world its author did not choose, which is the one outcome that makes the whole project pointless. A violation of I produces artifact-driven drift, recoverable but expensive. A violation of IV loses reasoning, which is painful but survivable. A violation of III costs throughput, which is recoverable in a week.

**The Universe-First / Loop-First tension, named.** Conviction I says the world precedes the artifact; Conviction III says the loop is the product. They collide constantly and predictably: deeper world simulation, richer epistemics, and stricter governance all make the world truer *and* the loop slower. The precedence order resolves it — depth wins over speed — but the resolution is bounded by the North Star's operability clause: **depth that stops the loop is not depth, it is paralysis.** In practice this means world-truth is never traded for throughput, while *instrumentation* of world-truth (checks, dashboards, reviews) is always fair game for trimming when it slows the loop without protecting canon. Section 29.4 is where that trimming is legal.

**A second named tension: IV against the anti-formula duty.** Intelligence compounds — and compounding intelligence, left alone, converges on imitating itself (Section 19.5). The convictions do not resolve this; Governance does, structurally, by treating a hardened pattern as a finding rather than an asset. Where accumulated intelligence and creative freshness conflict, freshness is a *quality* judgment the author owns, never a correctness rule the system enforces.

### 5.2 Failure Posture and Authorial Cause (v0.4)

Two things implicit in the convictions are now stated, because both were being decided ad hoc.

**Failure has a direction.** When something cannot complete — a check cannot run, an adapter is unreachable, the reasoning substrate is unavailable, a context is insufficient — the system's behavior is determined by which current the work is on: the descending current toward canon **fails closed** (nothing is committed, nothing is assumed, the work stops and says why); the ascending current toward artifacts **fails open** (work degrades to a reduced but honest mode and is marked as reduced). This is P-19, and it is the rule every future subsystem inherits.

**Authorial intent is a terminal cause.** P-18 requires every canonical state to answer *what caused it*. Most canon changes are caused by an author deciding, and that is a complete and legitimate answer — "the author wanted this, for this reason" terminates the causal chain. Requiring a world-internal cause for every change would produce fabricated causality, which is worse than none. Simulation-originated changes carry world-internal causes (a threshold crossing, a causal edge); authored changes carry authorial ones. Both are valid; neither may be invented to satisfy an audit.

### 5.3 The Artifact Principle (v0.5)

A sixth consequence, entailed by Convictions I and IV together and never before written down, because until v0.5 the system had no architecture that could violate it.

**Do not give the reader the world directly. Give the reader artifacts produced by a world that appears to genuinely exist.**

Universe First says the world precedes the artifact. It does not say the world should be *handed over*. A universe delivered as explanation — a wiki, a codex, an article whose purpose is to describe canon — converts the appreciating asset into a depreciating one at the moment of publication, because an explanation can only be read once. An artifact produced *by* the world can be read many times and yields differently each time, because the reader is reconstructing rather than receiving.

The full chain the architecture must support:

```
World → Canon → History → Society → Knowledge/Belief → Events → Culture
      → Editorial Production → Magazine → Page → Visual Artifact → Reader → Interpretation
```

Three consequences bind downstream design. **Society is a required layer, not an optional one** (Section 11.3): the world reaches the reader through what its people made, said, sold, and argued about, and a system that can go from Canon straight to Article has skipped the layer that makes the world feel inhabited. **Epistemic distribution is what makes indirect lore possible** (Section 14): an artifact can only reveal obliquely if the system knows who inside the world knows what. And **the reader's inference is the product** — which means an artifact that leaves nothing to infer has failed a quality standard, not merely a stylistic preference (Section 19).

This is a conviction-level statement and therefore not a rule the system enforces mechanically. Its enforcement is P-30, its editorial expression is the over-explanation finding (Section 19), and its structural support is the three-partition model (Section 13.6).

---

## 6. What coolboy12 Is, and Is Not

**coolboy12 is** a universe operating system whose core is a living, canon-governed, causally simulated world; an intent-driven instrument that composes goals into work; a coherence engine that keeps one truth intact, atomically, while the world grows and manifests; a temporal reasoning system that can move the world across centuries or toward an intended end-state; a discovery instrument that surfaces the story material the moving world produces; a manifestation platform that projects one universe into any medium from a single source; a compounding memory of decisions and intentions; a staff of specialist AI reasoning roles with hard boundaries; an orchestrator of best-in-class external tools; and a single-person instrument, operable and recoverable by one human.

**coolboy12 is not** a productivity system, an enterprise platform, an AI framework, a documentation system, a prompt library, a knowledge-management tool, a content generator, magazine software, or a pile of engines. It is **not multi-model orchestration** — exactly one reasoning substrate is bound at a time (P-15; the current binding is in Section 26.1), and the coworkers are roles it executes, not separate models. It stays a small set of domains, one thin spine, and two primitives by classifying every idea before admitting it (Section 29).

**Designed exclusions, stated as properties (v0.4).** The list above rejects product categories. These reject *architectural properties*, which is what future proposals will actually test. Each is a deliberate choice with a named cost, not an oversight:

- **Single-authority by design.** Exactly one authority position exists. It may be held by a person and may be transferred by ceremony (Section 10.2), but it is never held by two parties at once, and there is no permission model, no role-based access, and no concurrent-writer resolution. *Cost:* the system cannot become a studio tool without an amendment. *Benefit:* the entire severity, ceremony, and gate model stays comprehensible to one mind.
- **Dormancy-tolerant by design.** The system assumes long silences and is measured on recovery, not uptime. Nothing depends on continuous operation, background schedules, or an always-running process. *Cost:* no real-time behaviors. *Benefit:* a three-year absence is a supported state (Section 28).
- **Substrate-independent by design.** Canon, history, and memory must remain legible without the running system (P-27). *Cost:* constrains storage formats. *Benefit:* the universe outlives its software.
- **Non-deterministic in reasoning, deterministic in record.** The reasoning layer is a model and will not reproduce; the record is a record and always will (P-20). No guarantee may rest on model reproducibility.
- **Bounded-attention by design.** The author's attention is the system's scarcest resource and is treated as a budget, not an assumption (Section 12.7, Section 15.13). A capability that spends it without returning it is a defect regardless of its output quality.
- **Not a multiplayer world, not a live service, not a simulation for its own sake.** The world moves when the author asks it to. Nothing advances unattended.
- **Exposition-averse by design (v0.5).** The system has no capability whose purpose is to render canon as explanation for a reader, and will not acquire one. There is no public lore browser, no canon export, no reader-facing entity page, and no "about this world" surface. *Cost:* the reader is never told directly, so some readers will not follow. *Benefit:* the artifact stays an artifact (Section 5.3, P-30, Section 27.5). Internal, operator-facing exposition is unrestricted and is a different surface entirely.

---

## 7. Design Principles

Where the Core Philosophy states convictions, these state operating rules. They govern all design and override creative preference when they conflict. v0.3 adds two rules (P-15, P-16). v0.3.1 adds two further rules (P-17, P-18). **v0.4 adds ten (P-19 through P-28), each of which decides a question the earlier versions left open. v0.5 corrects one rule and adds two.** P-21 is corrected: it named four clocks where the architecture needs three canonical axes and one production metadatum, and a constitution should not carry a temporal axis nothing canonical orders by (Section 12.16, Decision D-05). P-29 and P-30 are added because the Reality Anchoring and indirect-lore architecture introduced in v0.5 creates two new ways to be wrong that no existing principle catches.

| # | Principle | Rule |
|---|---|---|
| P-1 | **Optimize the flywheel, not the tool** | Improve the loop's throughput and integrity; never optimize a component at the loop's expense. |
| P-2 | **One canon, one path, one authority** | Canon changes only through a single gated, transactional path, and only a human commits. No exceptions. |
| P-3 | **Provisional by default** | Every AI output, simulation delta, and emergent seed is provisional until a human gate confirms it. If it lacks that status, it was produced wrong. |
| P-4 | **The world is mutable; the Foundation is not** | Ordinary canon evolves through workflow. Foundation truths change only through deliberate ceremony. |
| P-5 | **Publish is a projection, never a mutation** | Publishing reads canon and derives output. It never writes canon. In-world journalism is not canonical fact. |
| P-6 | **Preserve intentions, not just decisions** | Record *why*, not only *what*. Future-you must understand past-you. |
| P-7 | **Schema before file, field before schema** | A new concept becomes a field, then a kind, then a status, and only then — rarely — a new structure. Reject structural sprawl. **The ladder runs downward as well as upward: an existing kind that a subtype or field could carry is walked back down it (Section 13.6).** |
| P-8 | **Address by meaning, never by ID** | The creator navigates by name and intent, never by internal identifiers, folders, or layer codes. |
| P-9 | **Gates explain themselves** | A quality or coherence gate returns *criterion → observation → judgment → confidence*, never a bare score. |
| P-10 | **Every signal has a consumer** | A report, metric, or artifact no one reads and acts on is deleted. |
| P-11 | **Recoverable after years** | The system is resumable after a dormancy of up to three years within a handful of sessions. Dormancy is expected, not failure. |
| P-12 | **Complexity only where it buys creativity** | Complexity is permitted only where it directly makes the universe richer or protects canon. Everywhere else, simplicity wins. |
| P-13 | **Intent over implementation** | The author expresses goals; the Workflow Composer (Section 23) translates them into execution. The author never chooses, combines, or sequences capabilities. |
| P-14 | **Every token must justify its existence** | Context is built, not dumped. The Context Builder (Section 24) assembles only the smallest sufficient context for each step. Token economy is a law. |
| P-15 | **One reasoning substrate, many roles** | Exactly one reasoning substrate is bound at a time. Coworkers are specialist roles it executes through role-scoped context and structured outputs. The system is role-based, never model-based. *The identity of the bound substrate is an adapter binding recorded in Section 26.1, not a constitutional fact — the invariant is the "exactly one," not the name.* |
| P-16 | **Time is a first-class dimension** | The world is reasoned through time, not only through single decisions. Simulation is a temporal reasoning system with horizons, resolution, pressure, and thresholds — and its output is always provisional until gated. |
| P-17 | **Canonical truth evolves, and its evolution is canonically traceable** | **(scoped v0.7.0)** Every Record is covered by a complete, traceable account of its authoritative evolution, **by the mechanism its Record Model defines** — the World Record Model uses the History Record; no other model is required to. The obligation is universal; the mechanism is model-owned (§13.6d, §13.7a). Current canonical state and historical evolution are separate logical concerns: current state is authoritative, history explains how it came to exist. History is never a second canon and never a second source of truth. |
| P-18 | **No canonical state without an explainable path** | No canonical state may exist that cannot be explained by its evolution. For any canonical state the system must always be able to answer: *what changed, when, why, who approved it, and what caused it.* A state that cannot answer these is an audit finding, not an acceptable state. Authorial intent is a valid terminal answer to *what caused it* (Section 5.2); a fabricated world-internal cause is a violation. |
| P-19 | **Fail closed toward truth, fail open toward artifacts** | When work cannot complete correctly, the descending current stops and explains — nothing is committed, assumed, or partially applied. The ascending current degrades to a reduced mode and is *marked* as reduced. Every capability declares its current and inherits its failure posture (Section 8.4). |
| P-20 | **Canon is model-independent** | Canon, history, and memory must remain valid, interpretable, and auditable regardless of which reasoning substrate produced any proposal. No canonical guarantee may depend on model determinism. Replaying the *record* is deterministic; re-running a *simulation* is not, and the two are never called the same thing (Section 12.10). |
| P-21 | **Every temporal statement names its axis** *(corrected v0.5)* | The system carries three canonical axes — **world-time** (in-fiction), **authoring sequence** (when the record changed, subdivided by **session**), and **issue ordinal** (discrete reader progression, authoritative in the Epistemic partition only). Every date, ordering, query, projection, and history entry declares which axis it is in. An unaxised temporal claim is a defect. **Publication-time is production metadata, not a canonical axis** (Section 12.16). |
| P-22 | **Every proposal declares its basis** | A proposal records the canonical state it was computed against. If canon has moved when the proposal reaches the gate, the proposal is re-validated before it may commit; if re-validation changes it materially, it returns to the author as changed, never as approved (Section 12.6). |
| P-23 | **Authority does not aggregate silently** | A batch may contain mixed severities. It is performed at the ceremony of its **highest-severity member**; every member at Structural severity or above is **individually reviewed** within that batch; no batch may contain a Foundational change. Every batch records its *scope of approval* (Section 12.7). |
| P-24 | **Structure blocks; judgment is adjudicated** | A violation is **structurally decidable** when it can be determined by inspecting *structure alone* — references, fields, statuses, tiers, partitions, axes, provenance, and declared metadata — **without interpreting the meaning of any prose, image, or narrative content**. A structurally decidable violation blocks with no override. A *judged* finding is surfaced at its severity and adjudicated by the author with a recorded reason. The system never grants a judgment the authority of a fact (Section 19.1). |
| P-25 | **Retirement is first-class** | Every extension point that admits also retires. Adding a kind, capability, manifestation, reader model, coworker role, or standard obliges a defined path for removing it: recorded, ceremonied, and traceable. A system that can only grow will eventually be abandoned rather than maintained (Section 29.4). |
| P-26 | **Authored state is not derived state** | Any state that records an authorial act — a dismissal, a deferral, a schedule, a plan, a preference — is **Production State** (Section 12.4): durable, provenanced, and never destroyed by a rebuild. Derived state is exactly and only what can be recomputed from Canon, Production State, and history with no loss. Filing authored state as derived is data loss with a delay. |
| P-27 | **Legible without the system** | Canon, History Record, Production State, and Creative Memory must remain interpretable by a human reading them directly, without the application that produced them. No external dependency may hold any of them in a form the system cannot fully recover (Section 26.3). |
| P-28 | **The constitution binds itself** | Amendments to this blueprint and to the Spine satisfy P-17 and P-18 exactly as canon does: what changed, when, why, who authorized it, what caused it — recorded, at a ceremony above Foundational (Section 10.4). |
| **P-29** | **Anchor by transformation, never by reference** *(new v0.5)* | Real-world material may enter the world only through a recorded **anchor** carrying a stated divergence: what the source was, what changed, and why the change matters in-world (Section 11.1). An in-universe element that is a real element renamed is a defect, not an homage. The test is structural at the record level — an anchor with an empty transformation field is blocked — and judged at the content level, where the standard is *"this feels strangely familiar,"* never *"this is that thing with a different name."* |
| **P-30** | **The reader receives artifacts, never the world** *(new v0.5)* | No capability on the ascending current may deliver canon to a reader as canon. Everything a reader receives is an artifact produced inside the world by someone inside the world, with that someone's limits, interests, and errors attached (Section 5.3). Canon reaches the reader only by being *implied* by an artifact. A proposed reader-facing capability that would explain rather than depict is refused at admission (Section 29.3), and an artifact that explains rather than depicts is an over-explanation finding at Governance (Section 19). |
| **P-31** | **Dependencies provide capability, never authority** *(new v0.6)* | No external component — database, index, graph store, search engine, workflow engine, renderer, or version-control system — may hold canonical semantics, define a kind, own a relationship, adjudicate a mutation, or be the only place a canonical fact exists. Every external component sits behind an adapter (Section 26.3), declares an exit path, and is deletable: if it vanished, canon must remain readable and the capability must be replaceable. The test is stated at Section 29.7 — **the architecture must remain meaningful when every dependency name is removed from it.** |
| **P-32** | **A capability is not an engine** *(new v0.6.1)* | The hierarchy is **Domain → Capability → Model / Service / Workflow / Tool → State / Artifact**, and a new capability enters at the lowest rung that carries it. Naming a capability — economic dynamics, editorial taste, visual similarity, writer voice — creates **no domain, no engine, and no subsystem**. The nine domains are closed (Section 9.3) and the two primitives are constitutionally fixed. The converse binds equally: **a capability is never dropped to keep the architecture looking small.** The target is maximum capability with minimum redundant architecture, and the way to miss it is to confuse the inventory with the structure. |
| **P-33** | **The environment runs the system; it does not define it** *(new v0.6.3)* | coolboy12 is built and operated inside an AI-assisted execution environment (§26.8). That environment provides filesystem access, command execution, code generation, test invocation, and role-scoped reasoning. It is **not a domain, not a partition, not an engine, and not a primitive**, and it owns no coolboy12 semantics — not Canon, Registry, Simulation, Epistemic, Production, Visual, Issue, or Governance. The ordering is fixed: **author → AI-assisted development → execution environment → coolboy12 → external components behind adapters** (§9.5). Any design that inverts it has made the tooling the architecture. |

---

## 8. The Creative Flywheel

Everything in coolboy12 exists to serve one loop. The architecture is organized around it, not around a file taxonomy.

```
                    ┌─────────────────────────────────────────────┐
                    │                                             │
                    ▼                                             │
              ┌───────────┐                                       │
              │  AUTHOR   │  makes decisions & states intent      │
              └─────┬─────┘  (composed into multi-domain work)    │
                    ▼                                             │
            ┌───────────────┐                                     │
            │   UNIVERSE     │  changes (canon updates, gated)    │
            └───────┬───────┘                                     │
                    ▼                                             │
            ┌───────────────┐                                     │
            │  SIMULATION    │  advances the world through TIME    │
            └───────┬───────┘  (across a span, or toward an end)  │
                    ▼                                             │
            ┌───────────────┐                                     │
            │  EMERGENCE     │  surfaces story material            │
            └───────┬───────┘                                     │
                    ▼                                             │
            ┌───────────────┐                                     │
            │    CANON       │  updates transactionally (true)    │
            └───────┬───────┘                                     │
                    ▼                                             │
            ┌───────────────┐                                     │
            │  EDITORIAL     │  decides what/when/what-form to tell│
            └───────┬───────┘                                     │
                    ▼                                             │
            ┌───────────────┐                                     │
            │  ARTIFACTS     │  are produced (issue, cover, game…) │
            └───────┬───────┘                                     │
                    ▼                                             │
            ┌───────────────┐                                     │
            │   READERS      │  experience the universe            │
            └───────┬───────┘  (knowledge-state advances)          │
                    ▼                                             │
              ┌───────────┐                                       │
              │  AUTHOR    │  learns ───────────────────────────► │
              └───────────┘  (and decides again)
```

**The loop, in one paragraph.** The author makes a decision or states an intent. It enters canon through the single gated path, and the universe changes. Simulation advances the world through time — computing consequences by walking the dependency graph across a horizon. Emergence reads the new world-state and surfaces story seeds, tensions, and opportunities. Canon absorbs whatever the author confirms, as one atomic transaction. Editorial decides what is worth telling, in what form, and at what time. The Creative Studio produces the artifacts. Readers experience the universe, and their knowledge-state advances. The author watches how the world moved and how readers now know it, learns, and decides again.

**Two currents, unchanged.** A **descending current** carries a decision *down* into canon — decision → propagation → simulation → commit — fail-closed and transactional. An **ascending current** carries canon *up* into experience — canon → emergence → editorial → artifact → reader — fail-open, reading canon and deriving from it, never mutating what it reads. Most creative work lives in the ascending current and never touches canon.

**Design consequence.** Because the flywheel is the architecture, coolboy12 is organized by the **nine domains** that carry the loop (Section 9), driven through **two primitives** (Sections 23–24), held by a thin **Spine** of inviolable laws (Section 10), and executed by **one model** in many roles (P-15). The author thinks in flywheel stages — never in prefixes, IDs, protocols, or models.

### 8.1 The Two Currents Are a Rule, Not a Description (v0.4)

In v0.3.1 the two currents were prose. They are now binding, because they are how every future capability derives its failure behavior without asking.

**Descending current** — *author intent → proposal → check → gate → commit → propagate.* Moves toward canon. **Fails closed** (P-19). Transactional. Every step is provisional until the gate. Every capability on this current must declare a basis state (P-22), must be causally closed before acceptance (Section 15.12), and must be reversible only by a *new* gated change, never by an undo (Section 12.10).

**Ascending current** — *canon → emergence → editorial → studio → artifact → reader.* Moves away from canon toward experience. **Fails open** (P-19): if an input is unavailable, the work continues in a reduced mode and says so. Reads canon; never writes it. Every capability on this current is forbidden a write path to canon by construction, not by policy.

**Every capability in this document declares which current it is on.** A capability that appears to be on both is misclassified and must be split — this is exactly the defect v0.4 corrects in Reader Simulation (Section 20.4).

### 8.2 Two Review Points Added to the Loop

The v0.3.1 loop had one moment of judgment — the gate — which meant the author learned the cost of a decision only after the system had done the work. v0.4 adds two capabilities to the loop itself. Neither is a domain; both are capabilities invoked by the Composer (Section 23).

- **Preflight Impact Prediction** (descending, before the gate). Before a change is presented for approval, the system walks the dependency graph and reports what the change *would* touch: the blast radius by object count and severity class, which mysteries and arcs it disturbs, which knowledge-states it would move, which published artifacts asserted the affected facts, and its estimated review load. The author sees the cost of a decision before making it, not after. A change whose predicted blast radius exceeds its declared severity is a finding: severity was misjudged (Section 12.7).
- **Critique / Counter-Case** (both currents, before every consequential gate). The strongest genuine argument against the proposal, produced by a role that did not author it, or an explicit "none exists" (Section 19.6). This existed in v0.3 as coworker behavior; v0.4 makes it a *stage of the loop* so it cannot be skipped by a workflow that forgot to ask.

### 8.3 The Reader Knowledge Return Path

The v0.3.1 loop showed readers advancing knowledge-state and the author learning — but the mechanism was a canonical write triggered by publication, which breached the Publishing Firewall (Section 20.4). The corrected return path: **publication is a projection and writes nothing.** Reading produces a **Reader Knowledge Proposal** on the descending current — a provisional, basis-stamped delta to the epistemic record that the author gates like any other proposal, usually in one batched Trivial-severity act per issue. What each tier now knows is therefore *authored*, not *inferred and silently written*.

### 8.4 Every Capability Declares Its Current

The declaration is a one-word property with three consequences: failure posture (P-19), write authority (descending capabilities may propose; ascending capabilities may not), and degraded-mode behavior (Section 28.3). Where this document introduces a capability, its current is stated. Where a future capability is added, stating it is a condition of admission (Section 29.3).

### 8.5 The Indirect Path Through the Ascending Current (v0.5)

The loop diagram shows Canon → Editorial → Artifacts → Readers, and that ordering is correct and unchanged. What it does not show is *what the ascending current is supposed to carry*, and the omission has a predictable failure mode: an editorial stage that reads canon and writes an article about canon. The diagram permits it; Section 5.3 forbids it; nothing in v0.4 made the difference operational.

The expanded reading of the ascending current, which adds no stage and changes no ordering:

```
CANON            what is true
  ↓
SOCIETY          what the world's people made of it — institutions, commerce,
                 fashion, argument, habit, the ordinary residue of a truth
  ↓
EPISTEMIC        who inside the world knows it, believes it, gets it wrong,
DISTRIBUTION     or has never heard of it (Section 14)
  ↓
EDITORIAL        which of that a particular publication would notice, care
                 about, and be able to print (Section 17)
  ↓
ARTIFACT         the thing itself, with its author's limits attached
  ↓
READER           inference (Section 20)
```

**The rule this makes operational.** An artifact derives from the *third and fourth* rows, never the first. An editorial capability that reaches past Society and Epistemic Distribution to read Canon directly is structurally permitted — Canon is readable by the whole ascending current — but produces exposition by construction, and is caught as an over-explanation finding at Governance (Section 19) rather than at the linter, because whether a piece explains or depicts is a judged question (P-24).

**Why Society is a row and not a domain.** It fails the Domain Admission Criterion (Section 9.3) on questions 2 and 3: it has no standing state of its own and no authority boundary — everything in it is already a Record of some kind, mostly `ORGANIZATION`, `CONCEPT`, and `EVENT`. Society is a *reading* of canon, not a store. Section 11.3 specifies it.

---

## 9. Overall Architecture

coolboy12 has three strata plus two primitives, executed by one model. A thin **Spine** holds the inviolable laws; **nine Domains** carry the flywheel; **Creative Memory** runs beneath everything and remembers why; the **Workflow Composer** and **Context Builder** are the two primitives through which the author drives all of it; and a **single bound reasoning substrate** (Section 26.1) executes every reasoning role.

```
┌──────────────────────────────────────────────────────────────────────┐
│  THE SPINE  — the inviolable laws (Section 10) · FROZEN                 │
│  one canon · one path · one authority · Foundation Lock · Publishing   │
│  Firewall · provisional-by-default · severity floor · every event      │
│  propagates · every Record has derivation · nothing bypasses the Composer    │
└──────────────────────────────────────────────────────────────────────┘
        │  governs everything below; never touched in daily work
        ▼
┌──────────────────────────────────────────────────────────────────────┐
│  THE NINE DOMAINS  — the flywheel, made operational                    │
│   1. UNIVERSE      the living world (source of everything)             │
│   2. CANON         the single sovereign truth (a dependency graph)     │
│   3. SIMULATION    temporal reasoning — consequence & evolution over time│
│   4. EMERGENCE     discovery of story material                         │
│   5. EDITORIAL     what to tell, in what form, at what time            │
│   6. CREATIVE      production — writing, visuals, publishing assets     │
│      STUDIO                                                             │
│   7. CREATIVE      Studio Standards — coherence, quality, reader sim    │
│      GOVERNANCE                                                         │
│   8. AI COWORKERS  specialist reasoning roles (one model, Section 21)   │
│   9. ECOSYSTEM     adapter-first orchestration of external tools        │
└──────────────────────────────────────────────────────────────────────┘
        │  driven through the two primitives (Sections 23–24):
        │  the Workflow Composer (intent → multi-domain workflow graph)
        │  and the Context Builder (smallest sufficient context per step)
        │  — both executed by the single bound substrate (P-15, §26.1)
        ▼
┌──────────────────────────────────────────────────────────────────────┐
│  CREATIVE MEMORY  — decisions · rationale · rejected paths · intentions │
│  · debt history · continuity intelligence. Append-only. (Section 22)   │
└──────────────────────────────────────────────────────────────────────┘
```

**One substrate, many roles.** Every reasoning act in coolboy12 — a simulation pass, an editorial recommendation, a governance verdict, a coworker's counter-case — is the single bound substrate (Section 26.1) executing a *role* with role-scoped context. There is no model routing, no multi-LLM committee, no model sprawl. Roles differ by their context, their remit, and their output contract, not by their model. This keeps the system simple to reason about and cheap to operate, and it means capability improves whenever the single model does.

**What the author sees.** Not this diagram. The author sees a workspace organized by what they are trying to do — *the universe, the current issue, a mystery, a decision, a timespan to simulate, the publish button* — and, above all, a place to state intent in plain language and watch the system compose the work.

### 9.1 The Four Classes of State (v0.4)

v0.3.1 recognized three classes of state — Canon, Working, Derived — and had nowhere to put a fourth kind that the system had been producing since v0.2: **state the author created that is not a fact about the world and cannot be recomputed.** An arc's pacing decision, a dismissed opportunity, a deferred beat, a payoff schedule, a visual style guide, a workflow in progress: none is world-truth, none is a draft, and none survives a rebuild if filed as Derived. Filing it as Canon makes the sovereign record of the world contain the plan for telling about the world; filing it as Derived destroys it the first time a projection is rebuilt.

v0.4 names it. Four classes, each with one rule:

| Class | What it holds | Rule |
|---|---|---|
| **Canon** | What is true in the world. | Written only through the single gated path. Authoritative. |
| **Production State** | What the author decided about *making the work*: arcs, schedules, opportunity dispositions, debt ledgers, style guides, workflow state, standards configuration. | Durable, provenanced, append-aware, **never destroyed by a rebuild**, never authoritative about the world. Changed by authorial act, at ceremony proportional to consequence — but not through the canon path, because it is not canon. |
| **Working** | Drafts, proposals, simulation deltas, emergent seeds. | Provisional. Never authoritative. Becomes canon only through the gate. |
| **Derived** | Indexes, dashboards, timelines, projections, published output. | Recomputable from Canon + Production State + history **with no loss**. If it cannot be, it is Production State that was misfiled (P-26). |

**Production ceremony (v0.4).** Production State changes by **production ceremony**, defined here once and used everywhere: *who* — the Authority, or an AI role acting under an explicit standing disposition the Authority recorded; *what it mutates* — Production State only, never Canon, never History Record; *what it records* — what changed, when (authoring sequence, P-21), why, and by whom, on the production record's own provenance, plus a Creative Memory entry where the decision is consequential; *how it differs from canon ceremony* — no severity classification, no Severity Floor, no gate queue, no History Record entry, no propagation; *reversibility* — freely reversible by an ordinary later act, because production state is the plan and plans change: it is **not** corrected-forward, and Canonical Reversion (Section 12.10.1) has no application to it; *effect on canon* — **none, ever**. A production change that would alter what is true is not a production change; it is a canon proposal and takes the canon path.

Production State is **not a domain, not a primitive, and not a new Record kind at the top level** — it is a classification, in the sense of Section 29.1, that every existing domain already needed. Its Records live in the **Production Record Model** — a sovereign Record Model with its own kind roster (Section 13.6), not a state of a universal object *(REVISED v0.7.0: this sentence read "the one object model with the one `kind` discriminator," which was the retired Canon Object Model claim)*; what changes is that they are *marked* as production records and are governed by production ceremony rather than canon ceremony. The Truth Model (Section 12.4) gains one row; the mutation path gains nothing.

### 9.2 Ownership of Cross-Cutting Capabilities

A capability with no owning domain is an orphan, and orphans acquire owners by accident. Every cross-cutting capability in this blueprint is owned:

| Capability | Owning domain | Current |
|---|---|---|
| History Record, Epochs, Canonical Reversion, Historical Replay | **Canon** (Section 12) | Descending (History Record is written by the commit); Replay is read-only |
| Production State custody and ceremony | **Canon** (rules) · originating domain (content) | Authored |
| Creative Memory | **Creative Memory** stratum (Section 22) | Written inside the commit |
| Preflight Impact Prediction | **Canon** (graph walk) invoked by the **Composer** | Descending |
| Canon Refactoring, Canon Linter, Canon Search, Canon Health | **Canon** (Section 12.13, 12.15) surfaced by **Governance** | Mixed; each declared in place |
| Knowledge modelling, forecasting, fair-play validation | **Knowledge-State** (Section 14), evaluated by **Governance** | Ascending except gated proposals |
| Workflow durability and resumption | **Workflow Composer** (Section 23.4) | Both; declared per node |
| Degraded-mode behavior | **Ecosystem** (detection) · every domain (response) | Both |
| **The Registry** (kind, subtype, relationship-type, field and controlled-value definitions) *(v0.5)* | **Canon** (Section 9.4) | Neither — it is definitional, not operational |
| **Reality Anchoring and Historical Divergence** *(v0.5)* | **Universe** (Section 11.1–11.2), applied by **Emergence** and **Editorial** | Descending (an anchor is canon) |
| **Publication Artifact Model** *(v0.5)* | **Creative Studio** (Section 18), consumed by the publication surface (Section 27.5) | Ascending |

### 9.3 Domain Admission Criterion

"No new domains" was previously enforced by fiat; the top rung of the classification ladder (Section 29.1) was circular. A domain — and there are nine, and v0.5 adds none — must satisfy **all five**:

1. It owns a distinct **question about the world or the work** that no existing domain owns. *(Not a distinct mechanism — a distinct question.)*
2. It has **standing state** that outlives any single workflow.
3. It has an **authority boundary**: things it may decide and things it may never decide.
4. It appears in the **flywheel** as a stage, not as a helper to one.
5. Removing it would leave a question **unanswerable**, not merely inconvenient.

Anything satisfying fewer than five is a capability, a workflow, a behavior, a state, a metric, or an artifact — and is admitted at that weight or not at all. Every capability introduced in v0.4 and v0.5 was tested against this and none passed, which is why neither version adds a domain. The v0.5 candidates and their failures are recorded for the next author who proposes one: **Society** fails 2 and 3 (Section 8.5); **Registry** fails 4 — it is definitional infrastructure that appears nowhere in the loop (Section 9.4); **Publication** fails 1 — its question, *what should the reader receive and in what form*, is already Editorial's.

**The v0.6.1 candidates, recorded for the same reason (P-32).** Every one of the following was proposed as a domain or an engine during this version and every one was admitted as a **capability** instead: Economic Dynamics · Media Dynamics · Public Opinion · Demography · Editorial Taste · Writer Persona · Visual Analysis · Visual Similarity · Art Direction · Research Intelligence · Trend Detection · Simulation Calibration · Sensitivity Analysis · Model Conflict Resolution. **Fourteen capability families, zero new domains, zero new engines.** Each failed the criterion at the same place — none owns a distinct *question* that an existing domain does not already own. Economic dynamics is Simulation asking its own question about a different subject. Editorial taste is Editorial asking its own question with better evidence. Visual similarity is an index.

**Primitives are constitutionally fixed at two.** A **primitive** is a mechanism through which *all* work passes — not a mechanism many things use, but one nothing may avoid. Exactly two satisfy this: the **Workflow Composer** (nothing happens un-composed, Spine law 10) and the **Context Builder** (no reasoning step receives context by any other means). **No third primitive may be admitted without Constitutional Amendment** (Section 10.4), and the test any candidate must pass is universality, not importance: an Epoch, a History Record, a dependency graph, and the Registry are each foundational and each avoidable by some work, and are therefore capabilities. This closes the primitive rung of the classification ladder (Section 29.1).

### 9.4 The Registry Layer (v0.5)

v0.4 had controlled vocabularies and no word for where they lived. Relationship types were "a closed vocabulary" in Section 11.5; kind definitions were prose in Section 13; field semantics were implicit in the then Canon Object Model file (the **Record Model Schema** since v0.7.0). Three different documents were therefore free to define the same term differently, and did. v0.5 names the layer.

**Definition.** The **Registry** is the definitional layer that holds reusable semantics: kind definitions, subtype definitions, relationship-type definitions with their participant roles and ownership rule (Section 13), shared field definitions, controlled value sets, change-and-operation semantics, and indicator semantics for world-state. **Classification:** capability (Section 29.1), owned by Canon.

**What the Registry is not, stated as three hard boundaries.**

- **The Registry holds no instances.** It defines what a `LINEAGE` is; it never holds a lineage. A registry entry that names a specific thing in the world is a misfiled Record.
- **The Registry is not schema.** Schema defines the *structure* of a record — fields, types, required-ness, defaults. The Registry defines the *shared meaning* those fields carry across kinds. A field's existence is schema; what "status" means everywhere it appears is Registry.
- **The Registry holds no commands and no runtime behavior.** How a mutation executes is the mutation path (Section 12.6) and the Composer (Section 23). The Registry defines what a mutation *means*.

**The semantic dependency contract (v0.5).** The Registry is, at the time of writing, incomplete, and v0.5 explicitly declines to freeze it. What v0.5 freezes instead is the **contract**: five layers, with a rule for each about what may depend on what.

| Layer | Holds | Depends on | May be depended on by |
|---|---|---|---|
| **Shared field semantics (RFS)** | The base layer. Reusable field meaning across every kind: identity, naming, classification, temporal, provenance, status, metadata, references | Nothing | Everything below |
| **Peer semantic authorities** | Meaning that is shared but is *not* a field-definition module: **relationship type and participant-role semantics**, **change and operation semantics**, **indicator semantics** for world-state | RFS | Everything below |
| **Kind semantics** | What is true of every record of one kind | Registry | Subtypes, instances, projections |
| **Subtype semantics** | What is true of one specialization (e.g. `HOUSE` within `LINEAGE`) | Registry, its kind | Instances, projections |
| **Instance data** | One record's actual values | All three above | Projections |
| **Derived / projection** | Recomputed views | All four above | Nothing — non-authoritative (Section 12.4) |

**Shared structure, independent vocabulary.** A field's *structure* is shared across kinds; its *value vocabulary* is per-kind and may legitimately diverge. `status` means the same kind of thing everywhere and enumerates different values for a `CHARACTER`, an `ORGANIZATION`, and a `CONCEPT`. **Divergent per-kind value sets are the intended design, not a defect to be unified** — a forced enum union across kinds is prohibited.

**Reference resolution is not Registry work.** What an `_ref` field *resolves to*, and the mechanics of resolving it, belong to a Record resolver. The Registry defines the reference *field*; it does not perform or own resolution.

**Registry architecture is frozen; Registry content is extensible.** These are different things and conflating them would either freeze vocabularies that must grow or leave the contract negotiable. The **architecture** — the five layers, the downward-only rule, the structure/vocabulary split, the resolver boundary — is settled and changes only by amendment. The **content** — kinds, `<kind>_type` vocabularies, relationship types, field definitions, controlled values, visual reference policies, indicator semantics, model definitions — extends by ordinary Registry change, at any time, without touching this blueprint. **Not every future Registry entry needs authoring now**; what needed settling was how the Registry can grow without forcing an ontology rewrite, and the downward-only rule is that answer.

**The one rule the contract exists to enforce:** *dependency runs downward only.* A Registry definition may never reference a kind, a subtype, or an instance; a kind may never reference an instance. This is what allows the Registry to evolve after v0.5 without forcing an ontology rewrite — adding, refining, or splitting a Registry definition changes meaning for everything below it, which is the point, and cannot invalidate anything above it, because there is nothing above it.

**Per-kind semantic dependency maps exist for eight of nine audited artifacts.** 825 fields across CHARACTER, LINEAGE, ORGANIZATION, LOCATION, CONCEPT, EVENT, WSV, Relationship Record and History Record carry a classified dependency. The aggregate profile is **74.4% inline Canon data, 14.1% Record reference, 8.6% Registry reference** — Registry dependency is a strict minority, which is the intended shape (Section 29). **`SPECIES` has no schema and therefore no map**; producing one by analogy to a sibling kind would be inference, not evidence, and is not done.

### 9.5 The Execution Environment Layer (v0.6.3)

*(ADDED. Source: authorial decision. Architectural consequence: **none** — this describes where the architecture runs, not what it is. It is recorded here because leaving it unstated is what allows tooling to be mistaken for structure.)*

```
AUTHOR
  ↓  states intent, decides, gates
AI-ASSISTED DEVELOPMENT
  ↓  proposes, drafts, implements, tests
EXECUTION ENVIRONMENT  (Claude Code)
  ↓  filesystem, commands, runtime, version control, role-scoped reasoning
COOLBOY12 SYSTEM
  ↓  the nine domains, six partitions, two primitives, ten laws
EXTERNAL CAPABILITY COMPONENTS  (behind adapters, §26.3a)
```

**Read it downward and each layer serves the one below it.** Read it upward and each layer is *constrained* by the one above. The layer that matters for this section is the third: the execution environment sits **above** coolboy12 and **outside** it. It is the workshop, not the building.

**Four things follow, and all four are prohibitions.**

1. **The environment is not a domain.** It fails the Domain Admission Criterion (§9.3) at question 1: it owns no question about the world or the work. It is where questions get answered, not a thing that answers one.
2. **The environment is not a partition, an engine, or a primitive.** Partitions classify records; the environment holds none. Primitives are constitutionally fixed at two (§9.3) and both are coolboy12's own.
3. **The environment owns no semantics.** Not Canon, not the Registry, not Simulation, Epistemic, Production, Visual, Issue, or Governance semantics. It may *execute* a validator; it does not *define* validity.
4. **The environment is replaceable.** coolboy12 could be built in a different environment, or by hand over a longer period, and the blueprint would be unchanged. That is the test — and it is the anonymisation test (§29.7) applied one layer up.

**What the environment legitimately provides** is specified at §26.8, in the Ecosystem section where every other external capability is specified, and deliberately not in a section of its own.


---

## 10. The Spine — The Frozen Constitutional Core

The Spine is the smallest set of laws that cannot be broken, and it is **frozen**: unchanged since v0.2, changeable only by extraordinary amendment ceremony. It is short — ten laws, not a constitution — because a single author must hold all of it in mind at once. Every mechanic this document deepens exists to keep one of these laws true.

1. **One Canon.** Exactly one canonical truth about the universe. No parallel canon, no duplicate truth, no second source.
2. **One Path.** Canon changes only through *propose → check → human gate → commit → changelog → log*. No other route; the commit is atomic (Section 12.6).
3. **One Authority.** Only the human commits canon. No AI output, no simulation result, no deadline, no report is canonical until the human gates it.
4. **The Foundation Lock.** Foundation truths (cosmology, prime mechanics, fixed identities, the ultimate shape of the world) are immutable except through deliberate ceremony. If generated content contradicts a Foundation truth, the content is wrong and the Foundation is right.
5. **The Publishing Firewall.** Published artifacts are in-world manifestations. They reference canon one-directionally; they never become canon. *That* the magazine printed X is a fact of the world; *whether* X is true is a separate, canon-governed question.
6. **Provisional by Default.** Every AI proposal, simulation delta, and emergent seed is provisional until gated. Every AI action is advisory unless explicitly approved.
7. **The Severity Floor.** Certain changes — to a Foundation truth, to relationship topology, to a load-bearing mystery, or to the Spine itself — can never be treated as trivial. What counts as "small" cannot be quietly redefined downward.
8. **Every Event Propagates.** A confirmed canon change runs its consequences through the dependency graph (Section 12.5); nothing commits in isolation. Propagation follows explicit relationships, not heuristics.
9. **Every Object Has Lineage.** Every Record traces to the decision that created or last changed it. No anonymous canon; a change with no recorded reason is an audit flag.
10. **Nothing Bypasses the Composer.** Every action is a composed, logged workflow (Section 23). There is no side door by which work happens un-orchestrated. The Composer routes work *to* the human gate; it never replaces it.

Everything else in this document is *how*. The Spine is *what may never be violated* — and v0.5 violates none of it.

**Reading of law 9 (v0.3.1, clarification — not an eleventh law).** *Every Object Has Lineage* has always been the Spine's traceability law. v0.3.1 states its full reach without amending it: lineage is not merely a pointer to the last decision but the guarantee that an object's **entire evolutionary path** remains recoverable and explainable for the life of the universe. The Spine remains ten laws. Canonical Evolution (Section 12.9) is the mechanic that keeps law 9 true at civilization scale; it adds no law, no authority, and no truth source.

### 10.1 Reading of Law 3 — What "the Human" Means (v0.4)

Law 3 says only the human commits canon. Over a decade "the human" needs a definition, and the definition is a *position*, not a person: there is exactly one **Authority** at any moment, it is always held by a human, and it is never held by two parties simultaneously. Transfer is possible and is a Foundational-ceremony act recorded in Creative Memory and History Record: who held it, who holds it now, from when, and why. Delegation is not possible — the Authority may take advice from anyone and may not lend the commit. An AI role may never hold it, and no automation, schedule, or default may ever exercise it in the Authority's absence. If there is no Authority, the descending current is closed (P-19) and the ascending current continues in reduced mode.

**Succession (v0.4).** If the Authority becomes unavailable, the system enters **read-only** (Section 28.3) and remains there: canon, history, replay, search, and every projection stay fully available, and nothing commits. **Succession happens outside the system** — by whatever personal, legal, or organizational arrangement the author has made — and is recognized *within* the system on the first act of the new Authority, which records who succeeded whom, from when, and on what basis, at Foundational ceremony. The system therefore never appoints, infers, or elects an Authority. A universe with no living Authority is a readable universe that does not change, and that is the intended behavior rather than a failure of one.

Four consequences follow, and they are stated rather than left to be discovered. **Succession creates no boundary in canon or History Record**: canon is continuous across it, authoring sequence keeps its single ordering (Section 12.16), and no epoch is opened or closed by it. **A predecessor's decisions bind the successor exactly as canon binds anyone.** **A successor may change any of it, by the ordinary means and no others**: Canonical Reversion at the severity of what is reverted (Section 12.10.1), retcon governance where a fact must become false (Section 12.12). **A returning Authority is recognized the same way anyone is**: there is only ever one position, so a predecessor who returns takes it back by the same recognition act, recorded the same way.

### 10.2 Reading of Law 8 — The Propagation Boundary (v0.4)

Law 8 says every event propagates. At millions of objects, "propagate everything inside one atomic transaction" is bounded only by graph connectivity, and an unbounded requirement is one that gets quietly abandoned under load — which is how a spine erodes. v0.4 draws the boundary explicitly, amending nothing:

- **Canonical consequence is atomic.** Any delta that changes what is *true* — a dependent fact invalidated, a relationship retimed, a status changed, a locked-field implication — commits inside the same transaction as its cause, or the transaction rolls back entirely. This is law 8 in full force and is not negotiable at any scale.
- **Derived recomputation is eventual and explicitly stale-marked.** Indexes, dashboards, search structures, heatmaps, coverage maps, and projections may reconcile after the commit. Until reconciled they are marked stale and are, as always, non-authoritative (Section 12.4). A stale projection is a known state, never a silent one.
- **Blast radius is predicted before the gate, not discovered during the commit.** Preflight Impact Prediction (Section 8.2) reports the canonical-consequence set and its severity distribution while the author can still decide. A change whose canonical consequence set cannot be computed does not proceed — fail closed.

### 10.3 Reading of Law 10 — The Front Door and the Locked-Door Case (v0.4)

Law 10 says nothing bypasses the Composer. A law forbidding all side doors must say what happens when the front door is stuck, or an undocumented side door will be built and it will be the least governed path in the system. The reading: **there is no side door, and there is a degraded mode.** When the Composer cannot compose — an unrecognized intent, a partial failure mid-graph, an unresolvable decomposition — the system enters **Manual Ceremony** (Section 28.3). **An unavailable substrate is not a Manual Ceremony trigger**: composition itself runs on the substrate, so without it there is no degenerate composition to perform, and the system is in read-only with the descending current closed. Manual Ceremony is a **degenerate composition, not a bypass**: the Composer still opens, records, and provenances a one-node workflow (Section 23.4), and the author supplies by hand the decomposition the Composer could not produce. Such a proposal receives *more* ceremony rather than less — full severity classification, explicit basis state (P-22), mandatory recorded reason, and an audit flag marking it as composed-by-hand. Nothing reaches canon un-orchestrated.

### 10.4 The Amendment Ceremony (P-28)

The Spine and this blueprint are changed only by **Constitutional Amendment**, a ceremony above Foundational:

1. **Statement of defect** — what the current text makes impossible, contradictory, or unsafe. An amendment must be motivated by a defect, never by preference.
2. **Impact analysis** — which sections, invariants (Section 36), capabilities, and existing canon depend on the text being changed.
3. **Counter-case** — the strongest genuine argument for leaving it alone (Section 19.6).
4. **Authorization** — by the Authority, explicitly, never as part of another act.
5. **Record** — what changed, when (authoring sequence), why, who authorized it, what caused it, and what was rejected: written to Creative Memory and to the blueprint's own changelog (Section 35).
6. **Re-audit obligation** — an amendment to the Spine triggers a full invariant review (Section 36) before the next epoch transition.

Amending the *ten laws* additionally requires that no other resolution exists. v0.3.1 declined to add an eleventh law, v0.4 declined again, and **v0.5 declines a third time**: the ontology contraction, the temporal correction, and the entire publication-artifact architecture were each resolvable within the existing laws — two of them by a Reading, which is the mechanism that exists precisely so that a law can be *applied* to a new situation without being *rewritten*.

**A note on the pre-implementation condition (v0.5).** Step 2 of this ceremony ordinarily includes a migration plan for existing canon. **No canon exists.** Nothing described in this blueprint has been implemented; there are no records, no store, and nothing to migrate. The migration obligation is therefore vacuous for every v0.5 amendment and is recorded as satisfied-by-absence. The other five steps are not relaxed, and the obligation returns in full the moment the first canonical record is written.

### 10.5 Reading of Law 7 — The Severity Floor's Referents (v0.5)

Law 7 names four things that can never be treated as trivial: a Foundation truth, relationship topology, **a load-bearing mystery**, and the Spine itself. Three of those four still name something the object model contains. The third no longer does: v0.5 retires `MYSTERY` as a World kind (Section 13.6), and a law whose referent has no home is a law that will be quietly skipped.

The reading, which amends nothing:

> **A load-bearing mystery is not a record. It is a *condition* holding across a World record and the Epistemic records that govern its disclosure.** A fact is load-bearing-mysterious when its reveal-state is `HIDDEN` or `AMBIGUOUS` for at least one reader tier, or when at least one open Question or planted Evidence chain depends on it remaining undisclosed (Section 14).

Three consequences. **The floor now binds a wider surface than before**, because it catches every deliberately withheld fact rather than only those the author remembered to file as a `MYSTERY` record. **The test is structurally decidable** (P-24) — reveal-state and evidence linkage are fields, so the floor blocks rather than merely advising. And **the floor follows the fact, not the filing**: changing a `CHARACTER`'s locked field is Structural-floor if that field is what a mystery turns on, which is the behavior law 7 always described and which the kind-based reading never actually delivered.

This is the second of two places where v0.5's ontology contraction improves the Spine's reach rather than eroding it. The first is that relationship topology — law 7's second referent — becomes easier to identify, not harder, under the Relationship Record ownership rule (Section 13).

---

## 11. Universe Architecture

The Universe is the domain the entire system serves: the living world, held as structured canon, from which all story derives. It is *manifestation-blind* — it does not know what a magazine is; it knows only what the world is. This blindness is what lets one universe feed a magazine, a game, and a film without the world's logic ever depending on the medium.

The Universe spans cosmology and physical law; the succession of ages; **characters** and their trajectories; **lineages** — the hereditary and dynastic structures, of which a house is one form; **organizations** — the purpose-built institutions, of which a polity is one; **locations**; **species**, and with them the possibility of a civilization that is not one people; **events**, the occurrences that move the world; **concepts** — the ideas, technologies, cultures, faiths, symbols, themes, and forces that a civilization believes, builds, argues over, and is shaped by; and **world state**, the live evolving values of the variables Simulation moves through time. Each is a **Record** (Section 13), not prose. Prose is a manifestation; the world itself is structured.

Two things the Universe is not. It is not the Canon record — the Universe is the world being modeled; Canon is the sovereign *record* of that world (Section 12), and the gap between them is where creation and the Draft Lifecycle live. And it is not the sum of its artifacts — a thousand issues are a thousand projections; delete every artifact and the universe still exists in canon, delete canon and no quantity of artifacts could reconstitute it.

At the Universe's center sits the **Foundation** — the locked axioms from which the whole world derives (Spine, law 4). The Foundation is the anchor a decade of model changes, medium changes, and creative pivots cannot move, and it is the outer boundary of what Simulation may ever propose. Under the v0.5 taxonomy, a prime mechanic is a `CONCEPT` at **Foundation tier** (Section 13.6): what makes it immutable is its tier, never its kind, which is the correct location for that property and always was.

**Where manifestation-blindness ends (v0.4).** The Universe is manifestation-blind; **the Canon store is not, and this is by design.** The distinction was implicit and produced a real contradiction: the object-kind list contains `ARC`, `MANIFESTATION`, `ARTIFACT`, `PERSONA`, and `READER-MODEL`, none of which is a fact about the world. The resolution is a partition, not a second store (Section 13.6):

- **World records (W)** — characters, organizations, lineages, species, events, concepts, locations, the world-state record, and the relationships among them. These *are* the Universe. They know nothing of magazines, covers, tiers, or issues, and no field on them may mention one. This is where manifestation-blindness is absolute.
- **Epistemic records (E)** — knowledge-state, reveal-state, belief, evidence, misconception. These are *about* the world and about who apprehends it. They are canonical, and they may reference reader models, because who-knows-what is a real property of a world that is being told.
- **Production records (P)** — arcs, threads-as-plans, schedules, opportunity dispositions, debt, personas, style guides, manifestations. These are facts about **the telling** — what the author is constructing, editing, and preparing — not about the world. They are **Production State** (Section 9.1), they live in the same object model, and they are explicitly *not* canon about the universe.
- **Issue records (I)** *(new v0.6)* — the concrete publication artifact: issue identity and number, title, publication and editorial context, sections, articles, pages, advertisements, visual assets, contributor and publication metadata. **Issue is not Canon.** It is the container through which Production becomes something a reader can hold. An `EVENT` may be referenced by many issues; that never makes an issue the owner of the event (Section 13.6a).

**Why this matters operationally.** Delete every production record and the universe is intact — you have lost the plan, not the world. Delete the world records and no quantity of plans could reconstitute it. That asymmetry is the test for which partition a record belongs in.

**World state versus production state.** Both evolve, and they are easy to confuse because both change constantly. World state is the condition of the world's systems and is advanced by Simulation and confirmed at the gate (Tier 4, Section 12.2). Production state is the condition of the *work* and is changed by authorial act at production ceremony. A character's current allegiance is world state. The decision to reveal that allegiance in issue 12 is production state. The reader's knowledge of it is an epistemic record. All three concern the same fact and none of them is the others.

### 11.1 Reality Anchoring (v0.5)

The world deliberately borrows from the real one. This has always been true of the project and was never architecture, which meant it had no rule, no record, and no failure mode — and an unarchitected borrowing converges on either reference-dumping or accidental plagiarism of tone.

**Definition.** A **Reality Anchor** is a recorded, canonical link from a real-world source to an in-universe counterpart, carrying an explicit statement of what was transformed. **Classification:** capability (Section 29.1), owned by Universe. **Current:** descending — an anchor is canon, proposed and gated like any other canonical fact.

**The pipeline, and every stage is a recorded field:**

```
REAL-WORLD SOURCE      what is being drawn on, named plainly and honestly
        ↓
ANCHOR                 the recorded link, with its category
        ↓
TRANSFORMATION         what was changed, and — the load-bearing part — why the
                       change matters in-world rather than merely disguising the source
        ↓
IN-UNIVERSE            an ordinary Record of an ordinary kind. It has no special
COUNTERPART            status, obeys every ordinary rule, and can be simulated,
                       contradicted, and retconned like anything else.
        ↓
EDITORIAL              how the counterpart shows up in what the world publishes
MANIFESTATION          (Section 17) — usually obliquely, per Section 5.3
```

**Anchor categories.** Historical Events · Historical People · Mythology · Folklore · Conspiracy Theories · Memes · Pop Culture · Current Events · Scientific History · Cultural Trends · Internet Culture. The set is a Registry controlled vocabulary (Section 9.4), extensible by ordinary Registry change, not by amendment.

**Four rules.**

1. **The anchor is canon; the source is not.** *That the world contains a counterpart* is canonical. The real-world source is recorded as provenance — it is a fact about the authoring, not about the world. No World record may reference the real world in any field a reader could reach.
2. **Transformation is mandatory and structurally checked (P-29).** An anchor with an empty transformation field does not commit. This catches the renamed-meme failure at the linter, before it reaches the world.
3. **The counterpart is an ordinary object.** It is not a special kind, does not carry a badge, and is not exempt from anything. Once created, it is simply part of the world, and the anchor is a fact about where it came from.
4. **Resonance is judged, not enforced.** Whether a transformation achieves *"this feels strangely familiar"* rather than *"this is that thing renamed"* is a judged finding at Governance (Section 19), adjudicated by the author with a recorded reason (P-24). The system can block an empty field; it cannot block a lazy one.

**In-universe trends versus real trends.** A real-world trend entering the world is an anchor like any other and produces an *in-universe* trend with its own causes, its own carriers, and its own arc, which will diverge — a trend that tracks its real counterpart move for move has not been anchored, it has been copied.

### 11.2 Historical Divergence (v0.5)

A specialization of Reality Anchoring, separated because it has a structure the general case does not: it produces a **branch point** with downstream consequences that Simulation must be able to walk.

```
REAL HISTORICAL        the actual event or person, recorded as provenance
REFERENCE
        ↓
DIVERGENCE POINT       the moment the two histories separate, stamped in world-time,
                       with what differed and — required — what caused the difference
        ↓
ALTERNATE IN-UNIVERSE  ordinary EVENT, CHARACTER, or ORGANIZATION records
HISTORY
        ↓
DOWNSTREAM             ordinary propagation (Spine law 8). A divergence is not a
CONSEQUENCES           special causal system; it is a normal causal chain whose first
                       link happens to be an anchor.
        ↓
IN-UNIVERSE            what the world remembers, misremembers, disputes, and
HISTORICAL MEMORY      mythologizes about it — Epistemic records (Section 14)
        ↓
EDITORIAL              how a publication of some later era treats it (Section 17)
REPRESENTATION
```

**Three constraints.**

- **A divergence point is a `CONCEPT` at Structural tier or above, and its consequences are ordinary records.** No new kind, no parallel timeline, no second causal engine. Section 13's anti-duplication rule applies with full force: causality lives in relationships and Event, and nowhere else.
- **Divergent history coexists with wholly invented history without marking.** The world does not know which of its past is anchored. A reader encountering a divergent event and an invented one should have no structural means of telling them apart, and the system provides none on the ascending current.
- **In-universe historical memory is where the interest is.** The divergence itself is usually the least interesting artifact it produces. What a society believes happened, how that belief is wrong, who benefits from the error, and what a magazine of a later era prints about it — those are Epistemic and Editorial, and they are the reason the divergence is worth recording at all.

### 11.3 Society as the Generative Layer (v0.5)

Section 5.3 requires that the world reach the reader through what its people made. Section 8.5 places Society in the ascending current. This subsection specifies what it *is*, given that it is deliberately not a domain and not a kind.

**Society is a reading of the World partition, not a store.** Everything it comprises is already a Record: institutions and commerce are `ORGANIZATION`; class, custom, fashion, ideology, language, and taste are `CONCEPT`; the people are `CHARACTER` and `LINEAGE`; the pressures are world-state. Society adds no record. What it adds is a **question**, asked of existing canon: *given that this is true, what would ordinary life look like, and what would ordinary people make?*

**The generative rule — worldbuilding by residue.** A canonical truth is most convincing when it reaches the reader as the *residue* it would leave rather than as the truth itself. An advertisement reveals an economy, a technology level, a set of social norms, a class structure, and a vocabulary — without asserting any of them. A music review reveals politics, cultural memory, species relations, and ideology. A gossip column reveals hierarchy and institutional power. A weather notice reveals the consequences of a catastrophe it never mentions.

**The consequence for canon coverage.** A world that can only be read through its residue must have residue to read, which means the World partition needs breadth in ordinary things — commerce, food, transport, entertainment, complaint — and not only in load-bearing ones. Emergence's coverage analysis (Section 15) therefore treats *ordinary-life thinness* as a finding: a world where every canonical fact is plot-critical produces a magazine where every page is plot-critical, and that magazine reads as a briefing.

**Cosmic scale without losing social scale.** As the world expands past a single planet (Section 11.4), the temptation is to widen the lens to match, and it must be resisted structurally rather than by taste. The rule: **the publication is always produced by a particular society, institution, and editorial culture, situated somewhere specific**, however large the universe around it grows. An encyclopedia of a galaxy has no editorial position and therefore no voice; a provincial magazine on one world, reporting a galaxy it half-understands, has both. The architecture supports this by making publication identity a `PERSONA`-and-`ORGANIZATION` matter (Section 17) rather than a scale matter.

### 11.4 Species and the Chapter Trajectory (v0.5)

The project's stated long-term trajectory runs Chapter 1 (Earth-scale, human, a hidden world) → Chapter 2 (beyond the galaxy, multi-species civilization) → Chapter 3 (reality, ontology, the universe as experience). The architectural obligation is precise and limited: **build nothing of Chapter 3 now, and close no door that Chapter 2 or 3 will need open.**

**`SPECIES` is a first-class World kind** (Section 13.6), admitted on the Section 13 admission test rather than on trajectory alone. The short form of its justification: a species has canonical identity independent of any member, a lifecycle independent of any member (emergence, spread, decline, extinction), history that is meaningfully its own, and relationships — inter-species relations, origin relations, symbiosis, descent — that no `ORGANIZATION` or `LINEAGE` edge represents without distortion. `CONCEPT` is insufficient because a species is a population, not an idea about one; a Registry classification is insufficient because a classification carries no state, history, or relationships.

**What Species is deliberately not.** It is not a race, a culture, or a faction — those are `CONCEPT` and `ORGANIZATION`, and conflating them produces a world where biology explains sociology, which is both bad architecture and bad fiction. A species may contain many cultures; a culture may span many species. The relationship types distinguishing these are Registry work and are `OPEN`.

**What Chapter 2 requires that v0.5 provides.** Species-level history and state; locations that are not on a planet; organizations spanning species; events at civilizational scale; world-state indicators that are not Earth-indexed.

**What Chapter 3 requires that v0.5 must not foreclose.** The Chapter 3 direction contemplates a universe that experiences itself, a terminal transformation of reality, a publication that continues past it, and an intentional ambiguity between the fictional universe, the artifact, and the reader's own reality. v0.5 builds none of this and forecloses none of it. Three properties are what keep the door open, and each is noted here so that a future version does not remove them for tidiness:

- **The Foundation is amendable by ceremony, not immutable by construction.** A cosmology that could never change could never reach a terminal transformation. Law 4 locks the Foundation against *casual* change, never against authored change.
- **The publication artifact is a Production record with no dependency on the world persisting.** Nothing in the artifact model requires that the world it came from still exist — which is what allows the magazine to continue past an ending.
- **The reader model is a `READER-MODEL` in Production, and the boundary between reader and world is a partition rule rather than an ontological claim.** Making the medium part of the ontology later is a Production-and-Epistemic change, not a rewrite of what the world is.

**One boundary that is not soft.** Reader interpretation never becomes canon (Section 20, Section 36). Whatever ambiguity Chapter 3 introduces at the level of *story* is introduced by authored canonical acts, never by the architecture losing track of which side of the boundary something is on.

### 11.5 Pseudo-Science and In-Universe Truth (v0.5)

The world may bend real science. The constraint is that the bend must be *systematic*: real science may be distorted, redirected, or extended, but the fictional system that results must remain internally logical, constraint-based, and consequence-driven. A world where the physics is merely convenient has no stakes, because nothing can be impossible in it.

The distinction the architecture must hold is between **authorial truth** — what is actually the case in the world, canon, in the World partition — and **in-universe scientific belief** — what the world's researchers currently think is the case, which is Epistemic and is frequently wrong. A fictional science is interesting exactly to the degree that those two diverge and the divergence has consequences.

The governance of controlled deviation — how a fictional theory is derived from a real basis, how competing interpretations are held, how evidence accumulates and forces revision — is Emergence's, and is specified at Section 16.4a. It is noted here because the *result* is Universe: a fictional scientific model is a `CONCEPT`, its consequences are ordinary world facts, and its contested status is an Epistemic record.

---

## 12. Canon Architecture

Canon is the spine of truth: the single sovereign record of the universe, the committed state every domain reads from and only the human gate writes to. Two properties make the guarantee real — canon is structured as a **dependency graph** (Section 12.5), so relationships are traversed rather than guessed; and canon changes are **transactional** (Section 12.6), so the world is never left half-updated. v0.5 leaves all of this frozen and changes only what the object-package model (Section 13.9) requires.

### 12.1 What Canon Is

Canon is exactly the committed record — nothing else is authoritative. Not a draft, not a simulation delta, not a report, not a published artifact, not an AI's confident assertion. Indexes, dashboards, timelines, and published output are *views* of canon; when any disagrees with canon, it is wrong and is rebuilt. One source of truth, one path to change it, one authority who commits it, and — beneath every object — a derivation and a history that explain why it exists.

### 12.2 The Canon Hierarchy

Not all truth is equal in weight. Five tiers, most to least binding; when two canonical statements conflict, the higher tier wins.

| Tier | Layer | What it holds | Mutability |
|---|---|---|---|
| 1 | **Foundation** | Cosmology, prime mechanics, fixed identities, the ultimate shape and unresolved core of the world. Prime mechanics are `CONCEPT` records held at this tier (Section 13.6). | Immutable except by ceremony (Foundation Lock). |
| 2 | **Structural Canon** | Load-bearing scaffolding: the roster of lineages and organizations, the shape of the timeline, the species inventory, the institutions everything references. | Changed only through the gated path, high ceremony. |
| 3 | **World Canon** | Confirmed facts: characters, events, locations, concepts, and the ordinary substance of the world. | Changed through the gated path, normal ceremony. |
| 4 | **World State** | The current, evolving condition of the world's systems — the indicators Simulation moves through time, held in WSV (Section 13.10). | Advanced by Simulation, confirmed by the author at light ceremony. |
| 5 | **In-World Belief** | What characters, factions, and the in-world publication believe — including what is false or partial. | Recorded as belief *about* the world, never as the world itself. |

**Conflict resolution.** Foundation beats everything. Between same-tier statements: an explicit authorial decision beats an unadjudicated one; a confirmed object beats a provisional one.

**When none of those decides it (v0.4).** v0.3.1's final tiebreaker was recency — the more recently confirmed statement won. That is a *drift mechanism* wearing the clothes of a rule: it means the newest assertion silently wins by default, which is precisely how canon erodes one reasonable decision at a time (Section 12.7). Recency is therefore no longer a tiebreaker. An unresolved same-tier conflict enters the explicit **CONTESTED** state: both statements remain in canon, both are marked contested, neither may be cited as settled truth, the conflict appears as a standing Canon Health finding (Section 12.15), and dependent work is blocked or proceeds only on facts not in contention. CONTESTED is resolved the only way anything is resolved here — by an authorial decision through the gate, with a recorded reason. **A contradiction the system cannot resolve is surfaced, never silently arbitrated.** Recency is admissible as *evidence* the author may weigh; it is not admissible as authority.

**Consequences of CONTESTED (v0.4), stated minimally.** A contested fact **may not be cited as settled truth** by any role or capability. It **blocks any new canonical commit that depends on it** as a premise (fail closed, P-19) while leaving unrelated changes to the same object free. **Simulation may not use it as a premise**, and a run that requires it stops and says so. **Publication may not assert it**, in the artifact or in any claim derived from it. It **may feed projections and Canon Health, always marked contested**, and it remains fully readable for search, replay, debugging, and audit — visibility is never the thing restricted. It **propagates to dependents as a marked dependency, not as contestation, and it does not propagate transitively**: a *direct* dependent is flagged as resting on a contested fact and remains itself usable and un-contested; that flag is not inherited by the dependent's own dependents, so a single unresolved conflict cannot cascade a region of the graph into unusability. What *does* travel to any depth is the premise rule: **any commit, simulation, or publication that reaches the contested fact through any chain of premises is blocked**, whether it is one hop away or six. A dependent that can establish itself through a different premise proceeds freely. A contested object remains canon — it is canon *marked contested*, never a fourth state class and never outside canon — and the mark is cleared, on the object and on every direct dependent, in the transaction that resolves it.

### 12.3 Canon Status

Independent of tier, every object carries a **status** tracking its lifecycle: **SEED** (captured, not developed; not citable), **PROVISIONAL** (proposed, under review; citable with caveat; ages out for a promote/demote decision), **CANON** (confirmed, authoritative), **SPECULATIVE** (deliberate exploration — alternates, roads not taken; kept, explicitly not true), **RETIRED** (formerly canon, removed by deliberate retcon; kept in history). These five are the visible tail of the Draft Lifecycle (Section 18.5). One orthogonal **flag**, not a sixth status: **CONTESTED** (Section 12.2) may be set on an object of any status, marking that it participates in an unresolved conflict; it constrains citation and raises a health finding, and it is cleared only by an authorial resolution.

### 12.4 The Truth Model

The hardest thing a world-with-a-magazine must never confuse is *what kind of true* a statement is. Seven kinds; only one is canonical.

| Kind | What it is | Authority |
|---|---|---|
| **Canon** | The committed truth of the universe. | The only authority about the world. |
| **World-Reality** | The deliberately uncommitted world — designed ambiguity, load-bearing unknowns. | Governed negative space. Never a second canon. |
| **Belief** | What characters, factions, and the magazine believe (may be wrong). | Canonical *that* it is believed; not that it is true. |
| **Editorial** | What a published artifact says — and, separately, two records of the act of publishing it. | Two records, never merged. **The in-world act** — *that the magazine printed X* — is a fact of the world and is canon (Spine, law 5), gated like any other world event and created only by an author's proposal, never by the act of shipping (Section 17.7.1). **Publication history** — that the real artifact shipped, when, and against which canon basis — is **Production State** (Section 20.4): authoritative about the work, never about the world. The truth of the *content* is never canon (Firewall); an artifact's assertion about the world is **Belief**. |
| **Working** | Drafts, simulation deltas, emergent seeds, proposals. | Provisional. Never canon until gated. |
| **Production** | What the author decided about *making the work*: arcs, schedules, opportunity dispositions, debt, style guides, workflow state (Section 12.16). | Authored and durable. Authoritative about **the work**, never about the world. Never rebuilt, never inferred, never canon. |
| **Derived** | Indexes, dashboards, timelines, published output, **relationship back-references** (Section 13.9). | Rebuildable **with no loss** from Canon + Production + history. Never authoritative; if it disagrees with canon, it is wrong. |

Seven kinds, unchanged in number since v0.4. Two of these boundaries are enforced mechanically by the single path; the two that require reading *meaning* — that a sentence asserts a world-fact, that a record is being mistaken for the whole world — are held by review and human judgment, and the author is told which two rest on their attention. The Truth Model is the coarse grid; the fine grid — *who knows what, when* — is the Knowledge-State Architecture (Section 14).

### 12.5 The Dependency Graph

Canon is not a filing cabinet of isolated facts; it is a **graph**. Within the **World Record Model**, every Record is a node and every relationship is a typed, directional, temporally-valid, provenanced edge with its own stable identity. *(SCOPED v0.7.0: this describes World's relationship packaging. Other Record Models connect their Records by references, containment, dependency, derivation, or transitions as their own semantics require — Sections 13.6d, 13.7a.)* *This lineage is allied with that organization, since this event. This event caused that one. This pressure pushes that indicator toward that threshold. This concept constrains that reveal.* The sum of these edges is the truth substrate the entire descending current runs on, and the substrate Simulation walks to compute consequences across time.

**Where the edges live (v0.5).** An edge has first-class *semantics* — identity, type, roles, direction, validity, provenance — and is *stored* in the **Relationship Record** of exactly one owning endpoint, with its history in that endpoint's History Record (Section 13.9). This is a change in packaging, not in the graph. The graph is exactly as connected, exactly as traversable, and exactly as authoritative as it was in v0.4; what changed is that an edge is no longer a free-standing object with a history of its own, which removes a class of orphan the four identity operations had to work around.

The graph is traversed, not drawn, for six operations: **propagation** (consequences found by walking edges, never guessed), **impact analysis** (the exact blast radius of a change), **consistency checking** (contradictions found where edges meet and disagree), **opportunity detection** (Emergence walks the graph for tensions and rich clusters), **continuity support** (a returning author and the Context Builder reconstruct *how things connect* without reading everything), and **temporal reasoning** (Simulation walks causal and pressure edges forward through time). If a consequence is not reachable along an edge, the graph does not invent it; if a real dependency exists but no edge records it, that missing edge is a Canon-Health finding. Changing the graph's *topology* is always at least Structural severity (Severity Floor) — and under the ownership rule that determination became easier, not harder, because every edge now has exactly one Relationship Record the linter can find it in.

### 12.6 The Single, Transactional Mutation Path

Canon changes by exactly one route, and the change lands whole or not at all.

```
PROPOSE   →   CHECK        →   HUMAN GATE   →  ┌ TRANSACTION ───────────────────┐
(a change)    (integrity +     (the author     │  PROPAGATE  (walk the graph;   │
              coherence +      confirms,       │             prepare all deltas)│
              severity)        modifies, or    │  COMMIT     (change + all deltas│
                               rejects)        │             as ONE atomic unit)│
                                               │  CHANGELOG  (record the mutation)│
                                               │  LOG        (decision + reason  │
                                               │             + intention → Memory)│
                                               └────────────────────────────────┘
                                                (any step inconsistent → full
                                                 rollback; the universe untouched)
```

If any part cannot complete consistently — a delta conflicts, an integrity check fails mid-commit, a write is interrupted — the whole transaction rolls back and the universe returns to its exact prior state. There is no half-fallen house, no character updated for an event that did not land, no canon written without its changelog and its reason. The atomicity adds no cognitive load — the author still just confirms at the gate — and it buys the one thing a decade-long solo project cannot survive without: **the world is always coherent when you come back to it.** No simulation tick, no publication, and no report may write canon by any other means.

**PROPOSE carries a basis state (P-22).** Every proposal records the canonical state it was computed against — a basis stamp naming the canon revision, the epoch, and the objects read. A proposal computed against state S and gated against state S′ is not committed as though nothing had moved: at the gate, the basis is compared to current canon; if any object the proposal *read* has changed, the proposal is **re-validated** before it may commit. If re-validation changes it materially, it returns to the author marked *changed since you last saw this*, with the diff — never silently approved. If re-validation is impossible, the proposal is rejected, not guessed. This is fail-closed (P-19).

**CHECK runs Preflight Impact Prediction (Section 8.2)** and separates its findings by class (P-24): structurally decidable violations block; judged findings are surfaced with severity and adjudicated by the author with a recorded reason. The check reports the canonical-consequence set before the gate, so severity is a prediction the author can see rather than a discovery the commit makes.

**COMMIT writes the commit set (v0.5).** v0.4 said "four records," which was correct while a relationship was its own object and became imprecise once it was not. The commit set is:

1. **The canonical mutation** — one or more **Record** records, plus any companion records the owning Record Model's packaging defines. *(SCOPED v0.7.0: the World Record Model's packaging is described here because it is the model with companion records. A change that alters a World Record's state touches its Record; a change that alters its relationships touches its **Relationship Record**; a change that does both touches both, in the same transaction. A Record Model whose packaging has no Relationship Record — Registry and Issue as currently declared, §13.6d — commits the Record alone. **The atomicity rule is universal; the commit set's shape follows the model's packaging.**)*
2. **The changelog** entry.
3. **The History Record entry for every object touched** (Section 12.9) — including where only its Relationship Record changed, because a relationship change is a change to that object's canonical situation and is recorded in that object's history. For WSV, the corresponding record is **WSV-H** (Section 13.10).
4. **The Creative Memory entry** — reason and intention (Section 22).

All of it lands inside the transaction or none does. Production State changes made by the same act — an arc advanced, a schedule updated — are written in the same transaction but are *marked as production*, never as canon (Section 9.1).

**The Mutation Coordinator (v0.6).** *(ADDED — naming a component the architecture already required. Source: authorial decision. Architectural consequence: none to the path; implementation consequence: substantial, because it fixes what may not be distributed.)*

The path above is a sequence of stages, and stages invite implementation by whatever component happens to be convenient for each. **v0.6 names the single native component that owns the canonical write boundary**, so that the path cannot be assembled out of parts that each hold a piece of the authority.

> **The Mutation Coordinator is the only thing in coolboy12 that writes canon.**

Its responsibilities, and it holds all of them together or the boundary is not a boundary: validate proposals · check current state · enforce semantic invariants · enforce partition boundaries · enforce the Human Gate · apply canonical transactions atomically · append History Record and WSV-H · record provenance · trigger rebuilds of derived projections.

**What it is not.** It is not a workflow engine, not a queue, not a scheduler, and not a service. It is the write boundary, and it is **BUILD-NATIVE** without qualification (Section 26.2): it encodes coolboy12's own semantics, and a component that encodes those semantics is coolboy12 whoever wrote it.

**External components may implement individual stages** — a validation engine may run schema checks, an indexer may rebuild projections, a version-control system may record the commit. **None of them may redefine authority.** A stage may be delegated; the boundary may not.

**Defence-in-depth is not authority.** Where an execution substrate offers its own guard rails — permission scopes, pre-write hooks, tool allowlists — those are welcome and are **defence-in-depth, never the constitutional authority** (Section 26.5). A guard rail can be misconfigured, bypassed, or removed by whoever holds the configuration. The Human Gate cannot, because it is a person. If the two ever disagree about whether something may be committed, the gate is right and the guard rail is a bug.

**Degraded mode.** If the reasoning substrate, an adapter, or a required check is unavailable, the descending current stops and says which check could not run. Canon is never committed on an unverified path. The one exception is Manual Ceremony (Section 10.3), which is heavier, not lighter, and audit-flagged.

### 12.7 Severity and Ceremony

Severity is derived from what a change touches; ceremony scales to match, never to zero for a canon change and never below the Severity Floor. **Trivial** (a world-state indicator, a minor detail) → a one-line recorded confirmation, batchable. **Standard** (an ordinary World Canon object) → confirmation plus the coherence check it answered. **Structural** (Structural Canon, relationship topology, a load-bearing mystery as defined by the Reading of Law 7 at Section 10.5) → full ceremony: options, impact review, recorded reasoning. **Foundational** (a Foundation truth or the Spine) → extraordinary ceremony: deliberation, full impact analysis, explicit rationale. Canon is rarely corrupted by a dramatic violation; it is corrupted by a long chain of individually reasonable, individually gated decisions that quietly lower what the world's truths are worth. The Severity Floor makes the reductions everywhere else safe.

**Aggregate ceremony (v0.4, P-23).** Severity was defined per change, which was adequate while changes arrived one at a time. They no longer do: an accepted simulation timeline can commit thousands of objects from a single act of approval, and every one of those objects then records "who approved it: the Authority" — an answer that is technically true and practically worthless. Provenance that inflates is provenance that dies.

Five rules make aggregate approval mean something:

1. **A batch carries the maximum severity of its members.** A batch may contain mixed severities; it is performed at the ceremony of its highest-severity member, so a batch containing one Structural change is a Structural ceremony however many Trivial changes surround it.
2. **Structural members are individually reviewed inside the batch; Foundational members may not be batched at all.** *Individual ceremony* means the change is presented, reasoned, and confirmed **on its own terms** — its own statement, severity, and recorded reason — and is not satisfied by inclusion in an accepted set. It does not require a separate transaction. Foundation is always its own act, in its own transaction.
3. **A batch is one transaction.** An aggregate approval commits atomically: all members land or none do (Section 12.6). Composition of the set happens *before* the gate and is where every exclusion occurs — an **invalid member** (a structural violation, P-24) is removed from the set and shown to the author, never silently dropped; a **rejected member** is removed and the remainder is re-checked for causal closure (Section 15.13) before the gate; a **judged finding** on a member is adjudicated in place. **Partial acceptance is a pre-gate operation only**: once the gate is passed, there is no partial commit.
4. **Every aggregate approval records its Scope of Approval**: what class of change was authorized, on what basis, which members were individually reviewed, which were accepted in aggregate, and what sample (if any) was inspected. This record is written to History Record for every member object.
5. **Lineage records the mode of approval, not merely the fact of it.** *Individually reviewed*, *accepted in aggregate*, *sampled*, and *auto-applied under a standing scope* are different facts, and an audit that cannot distinguish them cannot detect a rubber stamp.

**Review load is a first-class quantity.** Preflight (Section 8.2) estimates the number of decisions a proposal will require before it is offered. A proposal exceeding the author's declared review budget is not refused — it is *restructured*: segmented into reviewable stages, or offered with a proposed scope of approval the author can narrow. The system never resolves an attention problem by asking for less attention silently.

### 12.8 Continuity Snapshots

At long-running scale, canon becomes too large to hold in mind. coolboy12 takes a **continuity snapshot** at regular milestones — a compressed, indexed state record of active unknowns and their progress, active arcs and their pacing, current world-state, the window's canon decisions, and what each reader tier now knows. A creator reading a snapshot should reconstruct the operational state of the universe in one sitting. Snapshots are immutable once written; a discovered error is noted forward, never edited in place. They are the backbone of return-after-dormancy (Section 28) and a primary source the Context Builder draws on to reconstitute long-horizon context cheaply.

### 12.9 Canonical Evolution and the History Record

Canon models the world's truth. It must also model, explicitly, **how that truth came to be** — otherwise a decade-old universe is a set of assertions no one, including its author, can account for.

> **Canonical Evolution.** Every Record is covered by a complete, traceable account of its evolution, by the mechanism its Record Model defines (P-17, §13.6d). Current Canon State and Historical Evolution are separate logical concerns. **Current state is authoritative. History explains how the current state came to exist** (P-17).

The concern is separated because the two answer different questions and carry different authority. Asking *what is true?* is answered by the Record and only by the Record. Asking *how did this become true?* is answered by that Record's temporal record — in the World Record Model, its **History Record**.

**History Record.** Every **World** Record has **exactly one logical History Record**, which records changes to that Record and its Relationship Record alike (Section 13.9). *(SCOPED v0.7.0. The obligation to answer the P-18 questions is universal and binds all six Record Models; the History Record is World's mechanism for meeting it, not a Record System primitive — Sections 13.6d, 13.7a, and AD-11 at §36.2.)* Its constitutional properties:

- **Append-only.** Entries are added, never edited, reordered, or deleted — including for RETIRED and retconned objects. A correction is a new entry, never a rewrite.
- **It records canonical revisions.** Each entry corresponds to a change that passed the single gated path (Section 12.6) and answers the P-18 questions: *what changed, when, why, who approved it, what caused it.* Each entry carries the previous state, the resulting state, the change semantics that applied, and the **session** in which it was introduced (Section 12.16).
- **It exists outside the Record.** The object carries its current state; the history is a distinct logical record referenced by that object, not accumulated inside it (Section 13.5). An object that has changed ten thousand times is no heavier to read than one that has changed once. **This is what keeps Relationship Record bounded**: relationship churn goes to History Record, so a Relationship Record holds current relationships and never becomes a ledger.
- **The Record remains the current authoritative state.** Nothing is read from history to establish what is true.

What History Record explicitly **is not**, so that the Spine is unambiguous:

- **Not another Canon.** There is exactly one canon (Spine, law 1). History Record holds no independent truth about the world and cannot contradict canon; where they appear to differ, canon is the world and History Record is the account of how canon got there.
- **Not another truth source.** No domain — Simulation, Editorial, Governance, the Context Builder, Emergence — may resolve a question of world-fact by reading History Record.
- **Not a world primitive.** History Record is not a Record kind, not a domain, and not an entity in the universe. Nothing in the fiction is a History Record; the author never addresses one (P-8).
- **Not a mutation route.** History Record is written *by* the single gated path as a consequence of a commit. It is never written directly, and nothing becomes true by being written to it.

History Record is a **constitutional capability for traceability** (Section 29.1). This blueprint states that it must exist and what it must guarantee; it deliberately specifies no storage form, no schema, no serialization, no indexing, and no persistence strategy — those belong to implementation stages, not to the constitution.

**Ownership.** History Record is owned by the **Canon domain**. Canon defines what a revision is, what must be recorded, when an entry is written (inside the commit transaction, Section 12.6), and what may never be removed. No other domain writes to History Record, and no domain reads it to establish world-truth.

**The compaction invariant (v0.4).** History Record is append-only and, over a decade at civilization scale, unbounded. An unbounded permanent record with no compaction rule produces one of two failures: implementations never compact, and the system becomes unoperable; or they compact freely, and the traceability guarantee dies quietly. The constitution therefore sets a floor and refuses the mechanism:

> **History may be summarized, tiered, archived, or moved to cold storage by any implementation — but only if, for every canonical state, the P-18 questions remain answerable: what changed, when, why, who approved it, what caused it. Compaction is itself a recorded act. No compaction may make a canonical state unexplainable, and none may remove the existence of a revision, only the detail of it.**
>
> **Causal links survive every layer (v0.4).** Because *what caused it* is frequently a chain across objects — a threshold crossing in one object causing a transition in another — every compacted layer retains the **identity of each causal link** (which revision of which object caused which), even where the narrative detail of the cause is compressed away. Detail may be summarized; **the edges of the causal graph may not**. A compaction that preserves per-object answers while losing the chain between them satisfies the letter of this invariant and violates it, and is prohibited.

The concrete mechanism by which v0.4 satisfies this at scale is the **Epoch** (Section 12.14), which is a readability and retrieval structure, not a deletion mechanism.

### 12.10 Temporal Observability

Because canonical truth evolves, the world must be **observable through time**, not only in its present state:

- **Revision history** — the ordered account of how any object, or any region of the graph, reached its current state.
- **Comparison** — the ability to set two canonical moments against each other and see what differs and why.
- **Historical Replay** — the ability to walk an evolutionary path forward in the order it actually occurred, including the propagations each commit produced (Spine, law 8). Read-only, always.
- **Reversion** — the ability to return a canonical state to a prior one, as a new gated change. Never an undo.
- **Audit** — the ability to ask of any canonical state whether it satisfies P-18, and to receive a finding rather than an assurance.
- **Monitoring** — the ability to observe evolutionary activity across the universe over a window of time.

These are capabilities the architecture must support. This blueprint defines **no user interfaces and no APIs** for them; surfaces are governed by Section 27 and remain out of constitutional scope.

#### 12.10.1 Three Concepts, Three Words (v0.4)

One word was doing the work of three operations with completely different authority, and a word that ambiguous will be implemented as a destructive undo by someone, eventually, under deadline. The three are permanently distinct, and **no surface, document, or capability may use one word for more than one of them**:

| Concept | What it does | Touches canon? | Authority | Failure posture |
|---|---|---|---|---|
| **Operational Rollback** | Cancels work that never became canon: an abandoned workflow, a rejected proposal, a discarded simulation timeline, an unaccepted draft. | **No.** Operates only on Working state. | No gate required. Workflow provenance records that it happened and why (Section 23.4). | Free and safe. |
| **Canonical Reversion** | Returns canon to a state equivalent to an earlier one, because the author judges the later state wrong. | **Yes** — as a **new, forward change** on the single path, with its own proposal, checks, gate, commit, changelog, History Record entry, and reason. | Full ceremony at the severity of what is being reverted, never lower. Reverting a published change additionally invokes retcon governance (Section 12.12). | Fails closed. Never partial. |
| **Historical Replay** | Reconstructs an earlier canonical state read-only, or watches an evolutionary path unfold, without changing anything. | **No.** Read-only by construction; produces a Derived view. | None. Available always, including during degraded operation. | Fails open. A replay that cannot reach archived detail says so. |

**What replay can actually read (v0.4).** Replay reconstructs a past state from an **epoch baseline** (Section 12.14) or a **continuity snapshot** (Section 12.8), advanced forward through the History Record entries after it. **Read-only reconstruction is permitted and is always Derived; reconstruction is never a path to current truth.** Current canonical state is *read from canon*, never rebuilt; past states are *rebuilt for reading*, never authoritative. Replay granularity is **commit-boundary within an epoch, and baseline granularity across sealed epochs whose detail has been compressed** — and a replay that can only reach digest granularity says so rather than interpolating. **An epoch baseline is a complete origin; a continuity snapshot is a partial one**, so a replay originating from a snapshot is bounded to what that snapshot covered and declares the bound.

**Replay and P-22.** A proposal's **basis state is always a current canonical state** (P-22). A replayed state may be an *input* the author or a role reasons about, but it may **never** be a proposal's basis, because a basis exists to be re-validated against canon at the gate and a historical state cannot be. Reconstruction informs; only canon authorizes.

**Three anti-patterns, permanently rejected.** (1) *Undo.* There is no operation that removes a committed canonical change from having happened. Canon is corrected forward, always. (2) *Replay-as-mutation.* Viewing an earlier state never restores it. (3) *Rollback-as-a-button.* Canonical Reversion is never one click, never batched with unrelated work, and never available at lower ceremony than the change it reverses.

**Bounds on Canonical Reversion.** It may not cross a **Foundation ceremony** without Foundational authorization of its own. It may not un-publish: an artifact that asserted the reverted fact remains published, and the world simply now contains an in-world publication that was mistaken. It may not remove the reverted state from history. And it may not be performed by any role other than the Authority.

### 12.11 World Monitoring Projections

Many Record Histories may be **projected together** into world-level views: daily activity, a world timeline, major world events, ripple chains, revision heatmaps, and the evolution of a single object over its lifetime.

Every such view is a **projection** and is classified as **Derived** truth (Section 12.4): rebuildable, never authoritative, and wrong-by-definition when it disagrees with canon. Projections are **not truth, not Canon, not storage, and not additional world entities** — they introduce no object kinds, no tiers, and no domains. They read; they never write. Each must have a named consumer or it is deleted (P-10).

**One projection is now load-bearing and is named here (v0.5):** the **relationship back-reference**. Because an edge is stored in exactly one endpoint's Relationship Record (Section 13.9), the non-owning endpoint's view of its own relationships is a projection — rebuildable from the owning Relationship Records, never authoritative, and marked stale like any other. A capability that reads a back-reference as though it were the record is making a Derived source authoritative, which is the failure P-26 exists to catch.

### 12.12 Retroactive Change (Retcon) Governance

**Definition.** A **retcon** is any canonical change that makes a previously canonical fact false, rather than making it *change*. The distinction is exact and load-bearing: *"the house fell in year 900"* superseding *"the house stands"* is evolution; *"the house never existed"* superseding *"the house was founded in year 400"* is retcon. Evolution moves world-time forward. Retcon edits the past.

**Governance.** Every retcon:

1. **Is at least Structural severity**, never Trivial or Standard, regardless of how small the fact looks. If it touches Foundation, it is Foundational.
2. **Requires a dependent disposition.** Preflight (Section 8.2) computes every object that depends on the retconned fact, and each dependent must be explicitly dispositioned before the commit: **re-based**, **retired**, **preserved-as-contested**, or **preserved-as-independent**, with a recorded reason. No dependent may be left implicitly orphaned. This is the single most important rule in this subsection: retcons do not fail because the fact was changed, they fail because something three hops away still assumed it.
3. **Never rewrites published artifacts.** An artifact that asserted the retconned fact stays exactly as published. The world now contains an in-world publication that was mistaken, which the Publishing Firewall has always permitted (Spine, law 5). The retcon records the affected artifacts as a **publication divergence set** so the author knows precisely which issues now say something the world denies — and can decide, as a *narrative* matter, whether that mistake is invisible, is quietly ignored, or becomes a story.
4. **Never erases history.** The retconned object moves to RETIRED and its History Record is intact and permanently readable. Historical Replay before the retcon still shows the old world exactly as it was believed. *The universe changed its mind; it did not lose it.*
5. **Carries a mandatory reason and counter-case.** Why the old fact must be false rather than merely superseded, and the strongest argument for leaving it alone (Section 19.6).
6. **Triggers a knowledge-state reconciliation.** Every epistemic record referencing the retconned fact — what the world knew, what characters believed, what each reader tier has been told — is surfaced for disposition (Section 14.17). Readers cannot un-read; that is the point.

**Anti-pattern.** The *silent retcon* — quietly editing a canonical body so the past reads differently — is structurally impossible by construction: canon changes only through the path, and every change writes a History Record entry. Note that *classifying* a change as a retcon requires reading meaning and is therefore a **judged** determination under P-24: the checker raises the retcon question at high severity and the author answers it, with the answer recorded. What is structural, and therefore unavoidable, is that the change is visible at all.

### 12.13 Canonical Refactoring

Over a decade the *shape* of canon becomes wrong even when every fact in it is right: one character was really two, two lineages were always the same institution under different names, a location grew into a region that deserves its own object, a `kind` or `subtype` chosen in year one no longer fits. Without a governed way to change shape, an author does it by hand — creating orphans, breaking derivation, and severing history. Refactoring is therefore a **first-class, gated canonical capability**, owned by Canon, on the descending current.

| Operation | Meaning | Identity rule |
|---|---|---|
| **Rename** | The display name changes. | Identity unchanged; name is state (Section 13.4). Never an identity operation. |
| **Split** | One object becomes two or more. | The original is **superseded**; each successor records the split and inherits the relevant derivation; the original's History Record remains reachable from every successor. Its Relationship Record is partitioned among successors in the same transaction. |
| **Merge** | Two or more objects become one. | All sources are superseded; the survivor records the merge and carries **all** source histories; no source history is discarded. The survivor's Relationship Record is the union of the sources', de-duplicated in the same transaction. |
| **Extract** | A part of an object becomes its own object. | The parent persists with a recorded reduction; the extracted object records its origin. |
| **Reclassify** *(v0.5)* | An object changes its `<kind>_type` within its kind. | Identity persists; recorded as an ordinary revision with its reason. **Standard severity.** This is the operation the contracted taxonomy makes common and the eighteen-kind taxonomy could not express — moving a `LINEAGE` from `lineage_type: house` to `lineage_type: clan` is a classification change rather than a kind conversion. |
| **Convert** | An object changes `kind`. | Identity persists; the kind change is recorded as a revision with its reason. **Structural severity**, because with seven instance-bearing kinds a conversion is a genuine reclassification of what a thing *is*. Conversions across partitions (World ↔ Production ↔ Epistemic) are prohibited — those are a retire-and-create. |
| **Re-point** | A relationship's endpoint moves. | A mutation of the owning object's Relationship Record (Section 13.9), recorded in that object's History Record. Always at least Structural severity (topology change, Severity Floor). Where the re-point changes *which* endpoint owns the edge, the edge moves between Relationship Records inside one transaction and both objects' History Record entries it. |

**Invariants for every refactoring.** No history is ever orphaned — every superseded object's History Record remains reachable from its successors, forever. No reference is ever left dangling — dependents are re-pointed inside the same transaction or the refactoring does not commit. No refactoring changes what is *true*; if the facts change too, that is a separate gated change, proposed separately, so the author never approves a shape change and a truth change as one act. And every refactoring is preceded by Preflight (Section 8.2), because shape changes have the largest and least intuitive blast radius in the system.

### 12.14 Epochs

**The problem.** History Record must be complete, and completeness at civilization scale becomes unreadable and expensive. The compaction invariant (Section 12.9) forbids solving this by forgetting. Epochs solve it by *structuring* rather than discarding.

**Definition.** An **Epoch** is a named, bounded stretch of **authoring sequence** — not world-time — that partitions the system's history into an immutable archive and a live working set. Epochs are a readability, retrieval, and performance structure. They are not a narrative device, not a world entity, not a second canon, and not a deletion mechanism. Classification: **capability** (Section 29.1), owned by Canon.

**The five parts.**

- **Epoch Baseline.** At an epoch's start, a complete, immutable, self-contained statement of current canonical state: every object as it then stood, Record and Relationship Record alike, plus the WSV state (Section 13.10). The baseline is not a summary — it is the full state, and it is what makes everything after it compressible without loss of meaning.
- **Epoch Transition.** A deliberate, gated act that closes the current epoch and opens the next: baseline written, epoch summary produced, the closed epoch sealed immutable, standing capabilities re-justified (Section 4.2), open findings triaged, Manual Ceremony log reviewed. Transitions are authored events, never automatic and never time-triggered.
- **Epoch Archive.** A sealed epoch's full History Record, permanently retained, permanently readable, immutable. **Archived history is never deleted, never rewritten, and never summarized *away* — it is summarized *alongside*.**
- **Epoch Compression.** For an archived epoch, the system produces layered representations of the same history: the **full record** (unchanged, always retained), a **revision digest** per object, and an **epoch summary**. Compression adds layers; it removes nothing.
- **Current-Epoch History Record.** The live, uncompressed, fully detailed history of the epoch in progress — the only layer most work ever touches.

**Hierarchical retrieval.** Every history question is answered at the cheapest sufficient layer, in this order: **current-epoch History Record → epoch summaries → revision digests → full archive.** The Context Builder (Section 24.5) selects the layer by the question, not by habit. The layer used is recorded in the answer's provenance.

**Epochs and sessions (v0.5).** A **session** (Section 12.16) is a smaller unit inside an epoch: many sessions compose one epoch, and no session crosses an epoch boundary. Sessions are the granularity at which the author asks *"what did I change last time?"*; epochs are the granularity at which the author asks *"what happened over that stretch of the project?"* Neither replaces the other, and both order by authoring sequence.

**What an epoch does not do.** It does not reset canon. It does not reset identity, derivation, or Creative Memory. It does not reduce traceability: the P-18 questions remain answerable for every canonical state in every epoch, forever. It does not partition the world — epochs are a fact about the *record*, not about the fiction.

### 12.15 Canon Health, Linting, and Search

**Canon Health is a standing invariant of the system, not a duty of a coworker.** The health set includes: unresolved CONTESTED conflicts, dangling references, objects with missing or broken derivation, canonical states failing P-18, orphaned dependents from an incomplete retcon, relationship-topology anomalies, thin regions of the graph, **ordinary-life thinness** (Section 11.3), overdue narrative debt (Section 17.3), knowledge-state inconsistencies (Section 14.16), stale projections, **`CONCEPT` records with no conceptual content** (Section 13.6), and Manual Ceremony entries awaiting review. Health findings are **findings**, not blocks — except where the underlying violation is structurally decidable (P-24), in which case the block was already applied at the gate. The **Canon Health Dashboard** is the projection of this set and is the single surface a returning author reads first.

**Realization (v0.6.3).** Structural field validation is supplied by **JSON Schema** — **ADOPT** — with **LinkML** — **ADAPT** — used to author Registry vocabularies and field definitions in legible YAML and generate the validators from them. **SHACL is DEFERRED** and would only become relevant if the Registry ever went RDF-native, which it need not. The components validate *structure*; the Registry's semantic rules, the downward-only dependency contract, the partition rules, and every relationship and authority check are **native**. Failure posture: if structural validation cannot run, the **descending current closes** (P-19) — canon is never committed on an unverified path.

**The Canon Linter** is the structural checker: the set of rules that meet the structural-decidability criterion of P-24 — reference integrity, status legality, tier legality, `<kind>_type` legality against its kind, locked-field protection, firewall violations, partition violations, relationship-ownership violations (an edge appearing authoritatively in two Relationship Records, Section 13.9), missing required provenance, empty Reality Anchor transformation fields (P-29), unaxised temporal claims (P-21), and basis-state absence (P-22). Linter findings **block**. The linter is deliberately dumb and deliberately fast: everything requiring interpretation belongs to Governance (Section 19), and the boundary between them is the boundary between fact and judgment.

**Realization (v0.6.3).** The derived index is **SQLite** (public domain) — **ADOPT** — with **FTS5** for full-text, behind adapter A-4/A-9; **DuckDB** (MIT) — **ADOPT** — supplies analytical projections where columnar aggregation is wanted. **Tantivy** (`quickwit-oss/tantivy`, MIT) is the embedded-search alternative if FTS5 proves insufficient. **Meilisearch is REJECTED** — a permanently-running server contradicts §28. **A browsable database surface is legitimate on the operator surface and prohibited on the public one** (§27.5, AC-3). Source-of-truth class: **DERIVED**, deletable and rebuilt from canon (§29.8). The components supply indexing and ranking; coolboy12 supplies the author vocabulary, the provenance semantics, and the rule that a synthesized answer is never returned without its sources.

**Canon Search** is the author's ability to ask canon structural questions in the author's own vocabulary (P-8) — *"which lineages have no relationship to any open question," "what changed about the northern provinces in the last epoch," "which facts does the investigator tier already suspect," "what depends on this character."* Search is a **capability over the graph, History Record, and epistemic records**, not a query language the author must learn. It returns objects, paths, and provenance — never a synthesized answer presented as truth without its sources. Search is read-only, ascending, and fails open.

### 12.16 Temporal Axes

v0.4 carried four clocks. Three of them were canonical in the sense that matters — something authoritative ordered by them — and the fourth was not, which meant the constitution was protecting an axis nothing depended on while a genuinely needed unit, the **session**, had no constitutional standing at all. v0.5 corrects both.

**Three canonical temporal axes, and one ordinal that is not a clock.** *(CLARIFIED — v0.5 carried an ordering as though it were a measurement, and the Issue partition makes the distinction unavoidable.)*

| Axis | Measures | Moved by | Authoritative in | Example |
|---|---|---|---|---|
| **World Time** | In-fiction chronology. | Simulation, authored events. | Canon, Simulation | *"The house fell in the year 902."* |
| **Session Number** | The authoring/construction sequence — which sitting of work a change belongs to. | Every commit. | History Record, WSV-H, changelogs, Creative Memory | *"That was revised in session 214."* |
| **Real-World Time** | The operational clock at which a canonical action occurred. | Every commit. | History Record, WSV-H, provenance | *"Session 214 ran last March."* |

**Session Number and Real-World Time are two resolutions of one ordering, not two orderings.** Session is the coarse ordinal the author actually thinks in; real-world time is the fine stamp beneath it. Session numbers are strictly monotonic in real-world time, never overlap, never run backwards, and never cross an epoch boundary — so the two can be read against each other but can never disagree. This is why naming both is safe where naming two independent clocks over the same events would not be (P-21).

**The issue ordinal is a sequence, not a temporal axis.** *"As of issue 14"* states a **position in a published series**, not a moment in time. v0.5 filed it among the temporal frames and then had to argue it into canonical standing; the argument was sound and the filing was a category error. An issue ordinal measures publication order, and publication order is a property of the **Issue partition** (Section 13.6a), which owns the issue series and is authoritative about it.

**This resolves rather than weakens the epistemic mechanics.** Reader knowledge decay (§14.10), knowledge-debt escalation (§14.14), Knowledge Replay (§14.15), and reader-evidence reach (I-62) continue to order by issue ordinal exactly as before. What changed is what they are ordering *by*: an authoritative ordinal owned by a peer partition, referenced the way any partition references another's authoritative value — not a temporal frame, and not production metadata. **There is no circular authority here**: the Issue partition is not canon *about the world*, and it is fully authoritative *about the artifact series*, which is all the epistemic records ever needed from it.

**Publication-time remains operational metadata.** *When a real artifact shipped in wall-clock terms* is recorded on the issue's publication record and nothing canonical orders by it. External systems — a version-control commit stamp, a file mtime, a build timestamp — will record further technical timestamps of their own. **None of those is automatically World Time, Session Number, or Real-World Time** (Section 26.6). A timestamp acquires a canonical axis by being recorded as one through the mutation path, never by being produced by a tool.

**The rule (P-21): every temporal statement, query, ordering, projection, and history entry names its axis.** An unaxised temporal claim is a linter-blocking defect. Cross-axis relationships are themselves recorded facts — that issue 14 was published in June and covered world-year 902 is a recorded fact, not an inference — and no axis is derivable from another.

**The authoring sequence is globally ordered.** Session Number and Real-World Time together form a single monotonic ordering across the entire life of the universe. **Epoch boundaries partition the record, never the ordering**: a History Record entry in epoch 2 always follows every entry in epoch 1, and replay, comparison, causal traversal, retcon disposition, reversion, and continuity snapshots all order by this one sequence regardless of how many boundaries they cross. Session numbers inherit this ordering. No other axis is globally ordered — World Time may run in any direction, and the issue ordinal is ordered only within its own series.

---

## 13. The Record System

*(SUPERSEDED AND REPLACED at v0.7.0. The Record Model Schema is retired as the governing architecture. Its valid mechanics are preserved and re-expressed; its universal-object claim is not.)*

**The governing architecture is the Record System.** A **Record** is a persistent semantic unit owned by exactly one **Record Model**. A **Record Model** is a partition-owned semantic model that defines, for its own partition and no other: what kinds of Records exist, what identity means, how state and lifecycle work, how relationships are represented and packaged, how temporal and version semantics work, how provenance and authority are represented, and how its Records are stored and validated. The **Record System** is the architecture under which six such models coexist, exchange governed references, consume shared definitions and shared mechanisms, and remain semantically sovereign.

**The six Record Models are sovereign, not six configurations of one model:**

```
RECORD SYSTEM
├── World Record Model
├── Epistemic Record Model
├── Production Record Model
├── Registry Record Model
├── Visual Record Model
└── Issue Record Model
```

**What v0.7.0 retires, stated precisely.** v0.6.1 generalized "Canon Object" into a universal data abstraction and said *every record coolboy12 holds is a Canon Object*. That claim did real work — it stopped Registry definitions and visual assets from being governed by convention — and it carried a cost the architecture then had to keep paying: a single noun asserting that a registry definition, a published page, a belief, and a character are the same kind of thing, differing by a `kind` field. **They are not.** v0.6.1 itself began the retreat at Section 13.6d, where package specialization admitted that *"forcing World topology onto a registry definition or a published page would be a uniformity that costs more than it returns."* v0.7.0 completes that retreat and names what was actually true: **six models, one set of shared mechanisms, and no universal object.**

**What v0.7.0 does not do.** It does not redesign World. Every World semantic that v0.6.3 froze is preserved and re-expressed under the World Record Model. It does not invent schemas for the five other models. It does not resolve what earlier versions marked OPEN. **The supersession is architectural; the migration is not performed here.**

**The one thing that must not be misread.** The Record System is not the Record Model Schema under a new noun. There is **no Universal Record Base, no Universal Relationship Record, no Universal History Record, no universal lifecycle, no universal kind taxonomy, no universal identity grammar, no universal canonicality, and no universal Record schema.** A mechanism shared by six models is shared infrastructure; a *semantic* shared by six models must be proven in each, and is otherwise partition-specific. This distinction is the whole content of the change, and Section 13.2 states the reasoning.

### 13.0 Record, Record Model, and Canon — Kept Apart

*(ADDED v0.7.0. Stated first because every error this revision exists to prevent is a collapse of two of these four words into one.)*

| Term | What it is | What it is not |
|---|---|---|
| **Record** | The architectural unit: a persistent semantic unit owned by exactly one Record Model | Not a synonym for canon. Not inherently canonical. Not "the new name for Record" |
| **Record Model** | The partition-owned semantic model that owns Records, their kinds, identity, relationships, temporality, and validation | Not a schema. Not a specialization of a universal model |
| **Canon** | A governance and truth concept: the committed record, and the authority that commits it (Section 12) | Not a data class. Not the noun for the object |
| **Canonicality** | A status property whose meaning is defined by each Record Model that has one | Not a universal boolean. Not a property every Record carries |

**Three statements the blueprint must never make, and does not:** *every Record is Canon* · *every Record is canonical* · *Canon = Record*. **`Record` is architectural. `Canon` is governance.** Three of the six models hold Records that are never canonical in the world-truth sense, and one — Issue — holds Records that are never canonical at all (Section 13.6a). A vocabulary that could not express that would be the vocabulary that produced the error.

### 13.1 The Record

*(REVISED v0.7.0. The v0.6.3 text of this section enumerated three partitions and their kinds inline, which had been stale since v0.6.1 promoted Registry and Visual and v0.6 added Issue. The enumeration is removed rather than extended: **kind rosters belong to each Record Model and are stated once, at Section 13.6.** The illustrative shape below is the **World Record** envelope. It is not a universal Record schema, and Section 13.7a forbids reading it as one.)*

> **Recorded contradiction — FG-V7-02, not resolved here.** The v0.6.3 text of this section listed `ARTIFACT` among Production kinds. §13.6's Production roster does not contain it, while §13.6's own re-homing table still reads *"A specific made thing remains Production `ARTIFACT`."* §13.6a records that v0.6 moved the published artifact from Production to the Issue partition, which explains the roster but leaves the re-homing sentence unreconciled. **The available evidence does not settle whether Production retains an `ARTIFACT` kind for made things that are not publications.** Per §13.11 a kind roster changes only by the admission or retirement ceremony, and neither has been performed. The contradiction is documented and referred to the Authority.

```yaml
# A World Record. The author never types this; tools maintain it.
# The author addresses it by name and meaning (P-8).

id:            # canonical identity (Section 13.9a):
               #   [PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]
               # Stable for life. A rename never creates a new identity.
partition:     # W | E | P | R | V | I — required on every Record, and it names
               # which Record Model owns this Record (Section 13.6)
kind:          # The kind, drawn from THIS Record Model's own taxonomy.
               # Each Record Model owns its roster; see Section 13.6 for all six.
               # WORLD: CHARACTER | ORGANIZATION | LINEAGE | SPECIES |
               #        EVENT | CONCEPT | LOCATION  (+ the WSV singleton,
               #        which is not an instance-bearing kind — Section 13.10)
<kind>_type:   # domain classification within the kind, Registry-defined.
               # e.g. kind: LINEAGE + lineage_type: house
               #      kind: ORGANIZATION + organization_type: military
name:          # the display name — how the author refers to it
tier:          # FOUNDATION | STRUCTURAL | WORLD | WORLD-STATE | BELIEF
               # OPEN (FG-V7-03): these tiers are World-ontology terms. Whether
               # tier applies at all in R, V, or I — and what it would mean —
               # is unstated by any source and is not invented here.
status:        # SEED | PROVISIONAL | CANON | SPECULATIVE | RETIRED
               # plus the orthogonal CONTESTED flag (Section 12.3)

body:          # the actual content, in plain language

# --- fields split by mutation class ---
locked_fields:      # identity: what defines this object and cannot drift
world_state_fields: # the evolving condition Simulation may propose changes to,
                    # each with a value, a valid range, and its dynamics
                    # (momentum, inertia, thresholds — Section 15.5)
derived_fields:     # non-authoritative, rebuildable, marked stale when stale

# --- relationships live in the Relationship Record, not here (Section 13.9) ---
visual_refs:        # optional. References into the V partition, each with a
                    # declared role: canonical_depiction | reference | evidence |
                    # editorial_manifestation | generated_candidate (Section 13.6c)
cor_ref:            # reference to this object's Relationship Record record,
                    # where the partition carries one (Section 13.6d)
depends_on:         # what this rests on — especially Foundation/cosmology

# --- knowledge & reader epistemics (Section 14) ---
knowledge_state:    # DERIVED convenience projection only. The authoritative
                    # epistemic record is always a separate Epistemic object.

# --- provenance, derivation, history ---
derivation:         # the identity operations that produced this object —
                    # SUPERSEDES, SPLIT_FROM, MERGED_INTO, EXTRACTED_FROM
                    # (Section 13.8). Renamed from `lineage` in v0.5 to free
                    # that word for the World kind; Spine law 9 is unchanged.
provenance:         # who/what created it, when, and WHY → Creative Memory
coh_ref:            # NOTE (v0.7.0): `cor_ref` and `coh_ref` are FIELD names, and
                    # field names are Record Model Schema custody (13.7), not
                    # Blueprint custody. They are unchanged here deliberately;
                    # renaming them is the companion document's act (FG-V7-01).
coh_ref:            # reference to this object's History Record
version:            # current version stamp
```

**On the rename.** v0.4 called the derivation field `lineage`, and v0.5 admits `LINEAGE` as a World kind. One word could not carry both a hereditary structure in the fiction and the record of identity operations on a schema, and the collision would have made every query, linter rule, and invariant statement ambiguous. `derivation` is also the more accurate name: `SUPERSEDES` and `MERGED_INTO` are derivation operations, not genealogy. **Spine law 9 — *Every Object Has Lineage* — is unchanged**; it states a principle of traceability, and its text (*"every Record traces to the decision that created or last changed it"*) reads correctly without reference to any field name.

### 13.2 Why Six Models

*(REVISED v0.7.0. The v0.6.3 text argued for one model. The argument was sound within World and was then extended past its evidence.)*

**What the one-model argument got right, and keeps.** Within the World Record Model, a character, an event, and a species *are* records that differ by kind and by which fields matter. One model there makes relationships uniform, makes propagation uniform (Spine law 8), makes temporal reasoning uniform, and keeps the author's mental model one thing instead of twenty. **None of that is retracted. All of it is now scoped to World**, where the evidence for it actually lies.

**Where the argument failed.** It was extended to a registry definition, a published page, a rendered asset, and a knowledge state — records for which its premises are false. A definition does not have world-state fields for Simulation to move. A published page does not relate to arbitrary objects; it *contains* its parts. A registry definition's connections are dependencies under a downward-only rule (Section 9.4), not owned edges. A knowledge state is ordered by issue ordinal, not world-time. **Uniformity across those cases was never a simplification; it was a claim that four different questions had one shape.**

**Why six models is the smaller architecture, not the larger one.** The count that matters is not how many models exist but how many things must be true at once for any one of them to be correct. Under one universal object, every change to the object's envelope had to be checked against six partitions' semantics, and every partition inherited properties it could never populate. Under six models, each is answerable in its own terms, and the shared layer is small enough to state in one line. **The old model's cost was hidden in its exceptions; Section 13.6d was already a list of them.**

**What is genuinely shared stays shared.** Identity minting and parsing, serialization, structural validation, provenance capture, reference resolution, source-of-truth classification, and the single gated mutation path are **mechanisms**, and they remain common to all six (Section 13.7a). New *kinds* are still added rarely and deliberately (P-7), and each Record Model owns its own kind taxonomy (Section 13.11).

### 13.3 Relationship Semantics Are First-Class

*(SCOPED v0.7.0. Two claims live in this section and they have different reach. **The principle** — that a relationship is a modelled thing with a type, a direction, a temporal validity, and provenance, rather than a field — is a Record System principle available to every model. **The packaging** — the Relationship Record, its ownership rule, and its boundedness — is **World Record Model** architecture (§13.9, I-102). A model adopting the principle does not thereby adopt the packaging: Issue expresses connection as composition and Registry as dependency, and both honour the principle without a Relationship Record (§13.6d).)*

A relationship is not a field and not an attribute. It is a typed, directional, temporally-valid, provenanced connection with its own stable identity and its own definition in the Registry. v0.4 expressed this by making a relationship a Record with a History Record of its own; v0.5 keeps every semantic property and changes the packaging (Section 13.9), because an edge with its own independent history produced a class of orphan that the four identity operations had to work around and that nothing in the system benefited from.

What remains true, unchanged and constitutional:

- **Every relationship has a stable identity.** It can be addressed, referenced, re-pointed, and reasoned about individually.
- **Every relationship has a Registry-defined type** carrying its participant roles, its direction, its cardinality, and its legality constraints (which kinds may stand at each end).
- **Every relationship is temporally valid.** It holds *from* and *until*, in world-time.
- **Two edge families are named explicitly** for temporal reasoning: **causal edges** (*this event caused / enables / delays that one*) and **pressure edges** (*this condition pushes that indicator toward that threshold*). Naming them lets Simulation walk causality and accumulating force as first-class structure rather than inference (Section 15.6).
- **Changing relationship topology is always at least Structural severity** (Severity Floor, Spine law 7).

### 13.4 Locked vs. World-State Fields

*(SCOPED v0.7.0: the locked / world-state / derived split is a **World Record Model** field-mutation classification. No other model is required to classify its fields this way, and §13.7a forbids reading it as a universal state model.)*

Within the World Record Model, the most useful distinction on a Record is between what is **locked** (identity — a character's nature, an institution's founding, a species' origin) and what is **world state** (the evolving condition — a character's current allegiance, an institution's current power). Simulation may propose changes to world-state fields at light ceremony; locked fields change only through high-ceremony gates. This is what lets the world *evolve* while identity stays *stable*.

**Immutability is enforced at the mutation path, not at the store.** A locked-field write is a structurally decidable violation (P-24) and is blocked by the linter before the gate. There is no privileged route past it, including for Simulation, including for the Authority — the Authority changes a locked field by proposing that change at its proper severity, not by bypassing the check.

### 13.5 History Is Referenced, Not Contained (World Record Model)

*(SCOPED v0.7.0. This section states World Record Model mechanics under a generic title. The **principle** — that a Record presents current state and references rather than accumulates its past — is available to any Record Model; the **mechanism** below, including `coh_ref` and the single History Record, is World's and is not required of E, P, R, V, or I (§13.6d, I-90, I-107).)*

In the **World Record Model**, the envelope's `derivation`, `provenance`, and `coh_ref` fields are the Record's **reference into its one History Record** (Section 12.9) — the traceability contract, not a growing archive carried on the object itself. A Record always presents *what is true now*, at a size set by the world and not by how eventful its past has been, while its complete evolutionary account remains recoverable in full.

**The same rule governs Relationship Record, and this is what keeps it bounded.** A Relationship Record holds an object's *current* relationships and nothing else. Every relationship change — formed, retimed, re-pointed, ended — is recorded in that object's History Record, never accumulated in the Relationship Record. A Relationship Record whose size grows with the object's relationship *history* rather than its current relationship *count* has been implemented wrongly. This is the structural answer to the requirement that relationship history be recoverable without Relationship Record becoming a history dump.

### 13.6 The Six Record Models and Their Kind Taxonomies (v0.5, RETITLED v0.7.0)

*(RETITLED. The v0.6.3 heading read "The Three Partitions and the Kind Taxonomy" — stale since v0.6 added Issue and v0.6.1 promoted Registry and Visual, and stale in its singular "Taxonomy" since each model owns its own. The section's content had been correct for six for two versions; only its title had not.)*

**Six Record Models, one store, one mutation path** — six partitions distinguished by what a Record is *about*, each owning its own model. *(REVISED v0.7.0: v0.6.3 opened this section with "one object model." That is the claim this revision retires. The store and the mutation path remain single; the model does not.)* A partition remains a required property of every Record, checked by the linter — and it now additionally names which Record Model owns that Record.

**The roster of models, and what each owns.** Each row below is a sovereign Record Model. The kind rosters, governance, and boundaries in the table that follows are **carried forward from v0.6.3 unchanged in content**; what changes is that they are now read as each model's own declarations rather than as six configurations of one object.

**Kind taxonomy status, stated per model (v0.7.0).** *(ADDED. A roster that is listed is not thereby frozen, and v0.6.3 did not say which of the six were which. §13.6a already stated the governing reading for one of them — the kinds it lists "**name the boundary, not a frozen schema**" — and that reading is now applied to each model on its own evidence.)*

| Record Model | Kind taxonomy status | Evidence |
|---|---|---|
| **World** | **ESTABLISHED / FROZEN** — closed at seven instance-bearing kinds plus the WSV singleton; an eighth passes the eight-question admission test at Foundational ceremony | I-71, §13.11; the v0.5 contraction was performed and recorded |
| **Epistemic** | **BOUNDARY-NAMING / PROPOSED** — the roster names what E is about; field sets and reveal-state cardinality are **OPEN** | §13.6b: *"boundary defined, schema OPEN"* |
| **Production** | **BOUNDARY-NAMING / PROPOSED** — roster names the domain; most field sets **OPEN**; `ARTIFACT` unresolved | §13.6b; **FG-V7-02** |
| **Registry** | **ARCHITECTURE FROZEN / CONTENT EXTENSIBLE** — the five-layer contract and downward-only rule are settled; the roster below is the currently declared set and extends by ordinary Registry change | §9.4: *"Registry architecture is frozen; Registry content is extensible"* |
| **Visual** | **BOUNDARY-NAMING / PROPOSED** — the authority split (specification / asset / reference / analysis / derivative) is frozen; the kind roster is not | §13.6c freezes authority, not taxonomy |
| **Issue** | **BOUNDARY-NAMING / DEFERRED** — explicitly *"the boundary, not a frozen schema"* | §13.6a |

**What this status table forbids.** A roster in the **BOUNDARY-NAMING** state may not be treated as a frozen taxonomy by any downstream artifact, schema, or implementation, and a kind in that state may be renamed, split, merged, promoted from a field, or demoted to a subtype **by the model's own design work** without invoking §13.11's admission ceremony — because that ceremony governs an established taxonomy and only World has one. **OPEN does not mean empty: it means the model must be independently researched before its semantics are frozen.**

**Every partition owns a Record Model (v0.7.0).** *(SUPERSEDES the v0.6.1 "Canon Object is the universal abstraction" paragraph.)* v0.6.1 was correct that registry definitions, visual assets, and issue pages must be governed by rule rather than convention — they need identity, provenance, a temporal account, validation, and a mutation path, and leaving them outside the model left them ungoverned. It drew the wrong conclusion from a right observation: that because all six need *governance*, all six are one *kind of thing*. **They need the same mechanisms; they do not have the same semantics.**

**The correction: every record coolboy12 holds is a Record, every Record belongs to exactly one partition, and every partition owns exactly one sovereign Record Model.** A Record Model is not a specialization of a universal model and does not inherit from one. What the six share is the shared-mechanism layer (Section 13.7a) and the constitutional boundaries (the Spine, Section 10); what they do not share is ontology, kind taxonomy, identity semantics, relationship packaging, temporal architecture, lifecycle, or canonicality.

**World Truth is what the `W` partition holds, and it is one model of six.** No model is the template for another, and World — the most mature of the six — is explicitly not the template (Section 13.2).

**Why R and V are partitions and not infrastructure.** A Registry definition carries meaning that canon resolves against; if it changes, canonical readings change. A canonical visual specification carries what a character *looks like*; if it changes, canon changes. Both therefore need exactly what the world records needed all along — identity, provenance, history, a gate, and a linter — and the cheapest way to give them that is to stop treating them as exceptions.

| Partition | Kinds | About | Governance |
|---|---|---|---|
| **World** `W` | **Seven instance-bearing kinds:** CHARACTER · ORGANIZATION · LINEAGE · SPECIES · EVENT · CONCEPT · LOCATION — **plus the WSV singleton**, which is a world-state record and not an instance-bearing kind (Section 13.10). | What is canonically true in the world. | Canon. Manifestation-blind absolutely: no field may reference an issue, tier, medium, artifact, or the real world. |
| **Epistemic** `E` | KNOWLEDGE-STATE · REVEAL-STATE · BELIEF · EVIDENCE · MISCONCEPTION · QUESTION · THEORY · **MYSTERY** (Sections 14, 14.20) | What is known, believed, inferred, disputed, misunderstood, hidden, or revealed — by the world, by characters, and by readers. | Canon. May reference reader models and issues, because that is what they are about. Ordered by issue ordinal (Section 12.16). **Implementation schema incomplete — Section 13.6b.** |
| **Production** `P` | ARC · THREAD · SCHEDULE · OPPORTUNITY-DISPOSITION · DEBT · STYLE-GUIDE · PERSONA · WRITER-PERSONA · READER-MODEL · MANIFESTATION · WORKFLOW · TASTE-CRITERION · ART-DIRECTION | What the author is constructing, editing, and preparing. | **Production State** (Section 9.1): durable, provenanced, never rebuilt, never authoritative about the world. **Implementation schema incomplete — Section 13.6b.** |
| **Registry** `R` *(promoted v0.6.1)* | KIND-DEF · SUBTYPE-DEF · RELATIONSHIP-TYPE-DEF · FIELD-DEF · CONTROLLED-VOCABULARY · IDENTITY-GRAMMAR · WSVR-INDICATOR-DEF · VALIDATION-RULE · DERIVATION-RULE · SIMULATION-MODEL-DEF | **What things mean.** The semantic and structural definitions the rest of the system resolves against. | Canon *about meaning*, never about the world. **Registry owns meaning, not World Truth** (Section 9.4). |
| **Visual Library** `V` *(promoted v0.6.1)* | VISUAL-ASSET · VISUAL-REFERENCE · GENERATED-IMAGE · PHOTOGRAPH · ILLUSTRATION · COVER-IMAGE · CANONICAL-VISUAL-SPECIFICATION · VISUAL-ANALYSIS · VISUAL-DERIVATIVE | Visual data and visual knowledge, with their provenance, continuity information, and analyses. | Mixed by kind: a **canonical visual specification** is Canon (Section 18.6); an **asset** is a manifestation; an **analysis** is observation. **The Visual Library is never independently a truth authority** (Section 13.6c). |
| **Issue** `I` | ISSUE · SECTION · ARTICLE · PAGE · SPREAD · ADVERTISEMENT · VISUAL-PLACEMENT · CONTRIBUTOR-CREDIT · PUBLICATION-METADATA | The concrete published artifact a reader receives. | **Not Canon.** Immutable once published. May reference W/E/P/V objects; **a World object never becomes an Issue object by being published** (Section 13.6a). |

**The partition test.** *If every record in this partition vanished, what would be lost?* World: the universe. Epistemic: every unknown's mechanics. Production: the plan. Only the first is the world, and that asymmetry is why the partitions cannot be collapsed. **Cross-partition conversion is prohibited** (Section 12.13): a production record never becomes a world record by promotion — the author creates the world record and records the relationship.

**The World taxonomy is closed at seven instance-bearing kinds.** v0.4's World partition listed seventeen and described the list as *"illustrative, not exhaustive"* — an open taxonomy with an admission test and no counter-pressure, which over a decade produces a kind for every noun the author found interesting. v0.5 contracted it, and counted **WSV** among the kinds; that count was a naming error rather than a design error, because v0.5 had already specified WSV as a singleton with no instances, no Relationship Record, and a history record of its own. **v0.6 states it correctly: seven instance-bearing kinds, plus one world-state singleton that is not a kind.** *(CLARIFIED — no record, field, relationship, or rule changes; only the count and the word.)* The admission test for an eighth instance-bearing kind is unchanged (Section 13.11).

**The seven, and what each claims:**

| Kind | Identity claim |
|---|---|
| `CHARACTER` | this distinct individual, with continuity of identity |
| `ORGANIZATION` | this institution, constituted around a purpose or function |
| `LINEAGE` | this cross-generational hereditary or ancestral structure |
| `SPECIES` | this distinct population, with its own origin and trajectory |
| `EVENT` | this one occurrence, grounded in world-time |
| `CONCEPT` | this abstract canonical entity — an idea, technology, culture, faith, symbol, theme, or force of the world |
| `LOCATION` | this specific place |

**And, beside them, not among them: `WSV`** — the world's tracked state. It sits in the World partition, it is canon, and it is **not an instance-bearing kind**: there is exactly one, it has no object instances, and it takes no `Record + Relationship Record + History Record` package (Section 13.10). A kind is a category of which there may be many; WSV is one record. Counting it as a kind invited exactly the error the linter would then have to catch — a `W-WS-001-…` instance that must never exist.

**Where the ten retired kinds went.** Nothing was deleted. Each concept was walked *down* P-7's ladder to the lowest rung that carries it, which is what P-7 always specified and what no prior version had ever performed.

| v0.4 kind | v0.5 home | Reasoning |
|---|---|---|
| `HOUSE` | **subtype of `LINEAGE`** | A house is one form of hereditary structure among several — dynasty, clan, bloodline. Subtype is exactly sufficient. |
| `POLITY` | **subtype of `ORGANIZATION`** | A polity is an institution constituted around a purpose. It needs no field an organization lacks. |
| `RELIGION` | **SPLIT** — the tradition → `CONCEPT`; the institution → `ORGANIZATION` | These were always two things under one name, and the conflation was load-bearing in the wrong direction: a faith outliving its church, or a church abandoning its faith, could not previously be expressed. |
| `CULTURE` | **subtype of `CONCEPT`** | Not purpose-constituted, so not an organization; carries no lifecycle independent of its bearers. |
| `TECHNOLOGY` | **subtype of `CONCEPT`** | A capability or artefact-class of the world is an abstract entity. A specific made thing remains Production `ARTIFACT`. |
| `SYMBOL` | **subtype of `CONCEPT`** | The symbol as a thing in the world is conceptual; its *use* in an artifact was already Production. |
| `THEME` | **subtype of `CONCEPT`** where world-internal; **Production** where it is a craft intention | v0.4 already drew this line; v0.5 keeps the line and drops the kind. |
| `FORCE` | **subtype of `CONCEPT`, at Foundation tier** | Prime mechanics are made immutable by their *tier*, never by their kind. This was always the correct location. |
| `ERA` | **subtype of `EVENT`** — an occurrence with extended world-time duration | The weakest of the ten. Independent identity: yes. Independent lifecycle: marginal. Recorded as accepted-with-reservation; the alternative — a Registry-backed temporal classification — remains a live v0.6 question (Section 33). |
| `WORLD-FACT` | **no successor kind** | It was the escape hatch: *"the facts that fit no richer kind."* Removing it is the one place v0.5 accepts a real risk rather than eliminating one (below). |
| `MYSTERY` | **dissolved by design** | The solution is an ordinary World record of whatever kind it naturally is; the unknown-ness is entirely Epistemic. See below. |
| `SIGNAL` | **subtype of `EVENT`** | A detected indication in the world is an occurrence. Distinct from Epistemic `EVIDENCE`, which is a thing that moves a knower — that distinction survives intact. |
| `RELATIONSHIP` | **not a kind** — packaged in Relationship Record (Section 13.9) | Semantics preserved in full (Section 13.3). |

**How a specialization is recorded (frozen).** A kind is the broad Record class; a `<kind>_type` is the domain classification within it. **There is one classification field, not two** — the earlier open question between a *specialization* field and a *classification* field is closed in favour of the single `<kind>_type`, because a second structural field would have carried the same information under a different name and invited the two to disagree.

```
kind: CHARACTER        character_type: ruler
kind: ORGANIZATION     organization_type: military
kind: LINEAGE          lineage_type: house
kind: SPECIES          species_type: human
```

**A subtype relationship still exists conceptually** — a house *is* a kind of lineage, and the re-homing table below reads correctly as a subtype map. What changed is only how the record expresses it: `kind: LINEAGE` + `lineage_type: house`. The vocabulary of each `<kind>_type` is Registry-owned and per-kind, and per §9.4 those vocabularies may legitimately diverge between kinds — a forced union across kinds is prohibited.

**Two of these deserve their reasoning stated rather than tabled, because they cut in opposite directions.**

***`MYSTERY`'s dissolution is a gain.*** The Roadmap flagged `MYSTERY` as one of two early irreversible traps: it was filed as World while carrying reveal windows and tier visibility, which are Epistemic properties. That trap cannot now be sprung. A withheld truth is an ordinary `CHARACTER`, `EVENT`, or `CONCEPT`; what makes it *mysterious* is its reveal-state, its open Questions, and its planted Evidence — all Epistemic, all already specified in Section 14. The Severity Floor follows the fact rather than the filing, which is what Spine law 7 always described and what the kind-based reading never delivered (Section 10.5). Nothing about the mystery machinery is weakened; it is relocated to the partition that was always doing the work.

***`WORLD-FACT`'s removal is an accepted risk.*** Contracting a taxonomy and removing its escape hatch in the same version raises the pressure to misfile atomic facts into `CONCEPT`, and `CONCEPT` is broad enough to absorb them without complaint. v0.5 accepts this rather than retaining an eleventh kind, and mitigates it structurally: **Canon Health carries a standing finding for a `CONCEPT` record with no conceptual content** — no ontological relations, no acceptance or dispute status, no research status — which is what a misfiled atomic fact looks like. The finding is judged, not blocking (P-24). Recorded as a monitored risk, reviewed at the first epoch transition (Section 4.2).

**Kinds deliberately absent.** `EPOCH` — an authoring sequence structure over the record, not an entity in the world; making it a kind would put a fact about the archive inside the archive. `History Record` and `Relationship Record` — companion records, not kinds; nothing in the fiction is a History Record. `CONFLICT` — contestation is a flag plus a health finding. `PROPOSAL`, `TRANSACTION`, `GATE` — events in the *process*, recorded in History Record and the changelog. `SOCIETY` — a reading of the World partition, not a store (Section 11.3). `ANCHOR` — a property of the object it produced, not an object (Section 11.1).

### 13.6a The Issue Partition and Its Boundary (v0.6)

*(ADDED. Source: authorial decision. Consequence: architectural and implementation. Frozen at the boundary; substructure OPEN.)*

v0.5 filed the published artifact under Production, alongside the arcs, schedules, and debt ledgers that planned it. That was defensible while an artifact was a thin record of *what shipped*. It stopped being defensible once Section 18.9 gave the artifact a real interior — spreads, pages, regions, elements, a material vocabulary, an era. A publication with that much structure filed next to the plan will, over a decade, be queried like a database, cross-referenced like a database, and eventually trusted like one. **Issue is partitioned to prevent the magazine becoming a second canon.**

**What Issue holds.** Issue identity and number; title; publication context; editorial context; sections; articles; pages; advertisements; visual assets; contributor metadata; publication metadata. It is the container through which Production becomes a readable artifact.

**Four rules.**

1. **Issue is not Canon.** Nothing in an issue is true because it is printed. An article asserting a world-fact is **Belief** (Section 12.4); the world-fact itself lives in the World partition or nowhere. This is the Publishing Firewall (Spine, law 5) expressed as a partition rather than a policy.
2. **Issue references; it never owns.** An `EVENT` may be referenced by many issues across many eras. **That never makes an issue the owner of the event.** Ownership is a World-partition property, and a reference from a lower partition confers nothing.
3. **Reference runs one way.** Issue records may reference World, Epistemic, and Production records. **No World record may reference an issue** — that is manifestation-blindness, and it is absolute (Section 11). Epistemic records may reference issues, because who-was-told-what-and-when is exactly what they are about.
4. **Issue is durable and provenanced, never rebuilt.** A published artifact is immutable (Section 18.7). Correction is a new publication with a `supersedes` relationship, never an edit.

**Why a partition and not a kind.** The partition test (below) answers it: delete every issue record and the world is intact, the plan is intact, and what is lost is *the artifacts* — a third distinct loss, which is what a partition marks. A kind cannot express that, because kinds live inside partitions and the question here is which side of a boundary a record sits on.

**Why a partition and not a domain.** Issue fails the Domain Admission Criterion (Section 9.3) on question 1: its question — *what should the reader receive, and in what form* — is Editorial's, and Editorial already owns it. Issue is where the answer is *stored*, not a second place where it is decided.

**OPEN — Issue substructure.** The kinds listed at Section 13.6 name the boundary, not a frozen schema. Their field sets, the section/department relationship (Section 17.12), and how page-level records relate to the artifact model (Section 18.9) are **DEFERRED**. The boundary is what v0.6 freezes; the interior is not invented here.

### 13.6b Partitions That Are Not Yet Fully Built (v0.6)

*(CLARIFIED. Stated because a blueprint that reads as uniformly complete will be implemented as though it were.)*

Two partitions have architecture and do not have finished implementation schemas, and v0.6 declines to pretend otherwise.

**Epistemic (E) — boundary defined, schema OPEN.** What is settled: the partition exists; it is Canon; it holds knowledge-state, reveal-state, belief, evidence, and misconception; its mechanics are specified at Section 14 across eighteen subsections; its interface to World is by reference to a World record whose apprehension it describes; its interface to Issue is by reference to the artifact that carried the evidence. What is **OPEN**: reveal-state cardinality (one record per fact, or per fact × knower); the field sets of all five kinds; whether Epistemic and Production share one index or separate ones. **No external component's convenience may close these** — a store that wants a schema is not a reason to freeze one (Section 26.4).

**Production (P) — boundary defined, schema OPEN.** What is settled: the partition exists; it is Production State, never canon; it holds the plan; it changes at production ceremony (Section 9.1). What is **OPEN**: field sets for most Production kinds; the department taxonomy (Section 17.12); the artifact model's typed field list (Section 18.9).

**What is frozen for both:** the boundary, the direction of reference, and the rule that neither may become canon by any route. That is enough to build against, and it is all v0.6 claims.

### 13.6c The Visual Library Partition (v0.6.1)

*(ADDED. Source: authorial decision. Architectural consequence: a sixth partition; implementation consequence: substantial; migration: none.)*

Visual material was previously split awkwardly — a **canonical visual identity** was a World record (Section 18.6), an **asset** was Production, and analyses had nowhere to live at all. That split was correct about authority and wrong about location: all three are visual objects with visual provenance, visual continuity relationships, and visual history, and separating them by partition made the one question anyone actually asks — *what do we have of this character, and does it agree with itself?* — a cross-partition join.

**V holds the objects. It does not hold the authority.** The distinction is exact and is the reason V can exist without becoming a second canon:

| Visual object | What it is | Authority |
|---|---|---|
| **Canonical Visual Specification** | The structured description of how a thing looks and what it means — features, proportions, palette, materials, bearing, ageing rules | **Canonical.** Gated like any canon. This is the thing that is true. |
| **Visual Asset** | A rendered instance — generated image, photograph, illustration, cover | A **manifestation** of a specification. Never authoritative; a divergence from the specification is a continuity finding against the asset (Section 18.6). |
| **Visual Reference** | Material gathered as reference, including real-world material | Authoring provenance. Never a world fact (P-29). |
| **Visual Analysis** | What image understanding observed in an asset | **Observation, never truth.** See below. |
| **Visual Derivative** | Crops, treatments, scan renderings, thumbnails | Derived. Rebuildable. |

**The rule that keeps V honest:** *vision analysis is observation or proposal, never canonicalization.* A model reading an image and reporting that a character's coat is green produces an **observation**. If that contradicts canon, it produces a **proposal** (Section 18.11), which travels the ordinary mutation path and meets the Human Gate like anything else. **No image, and no reading of an image, becomes true by being looked at.**

**Every Record has a defined relationship to the Visual Library, whether or not an asset exists (v0.6.3).** This is a statement about the *model*, not a requirement that every object be illustrated. Every kind declares, through Registry semantics, which visual roles are permitted for it, which (if any) are expected, and what a missing canonical depiction means for that kind. An object with no assets has a defined and empty relationship — not an undefined one. The difference matters when the question is *have we never drawn this, or does this not get drawn?*

**Every Record may reference visual objects.** The envelope carries `visual_refs` (Section 13.1), and each reference declares its **role**: `canonical_depiction` · `reference` · `evidence` · `editorial_manifestation` · `generated_candidate`. The role is what prevents a generated candidate from being read as a canonical depiction by anything downstream.

**Visual reference policy is Registry-defined, frozen.** Every Record kind carries a Registry-defined **`visual_ref_policy`** with exactly one value:

| Policy | Meaning |
|---|---|
| `REQUIRED` | A canonical depiction must exist before the object may reach CANON status |
| `OPTIONAL` | Visual references are permitted and not expected |
| `NOT_APPLICABLE` | This kind is not the sort of thing that is depicted |

**`visual_ref_policy` and `visual_ref_role` are separate concerns and must not be conflated.** The *policy* is a property of the **kind**, held in the Registry, and answers *does this sort of thing get depicted?* The *role* is a property of an individual **reference**, held on the object, and answers *what is this particular image to this particular object?* — `canonical_depiction` · `reference` · `evidence` · `manifestation` · `generated_candidate`.

**This does not mean every object must have an image.** A kind whose policy is `OPTIONAL` and which has no assets has a **defined and empty** visual relationship — which is exactly the distinction §13.6c exists to draw. The roster of which kinds take which policy is Registry content and extends by ordinary Registry change (§9.4); the *rule* that every kind has one is frozen here.

### 13.6d Record Packaging Is Model-Owned (v0.6.1, RECLASSIFIED v0.7.0)

*(RECLASSIFIED. v0.6.1 wrote this section as a set of *exceptions* to a universal package. v0.7.0 reads it as what it always was: the first evidence that packaging belongs to each model. The table below is unchanged in content and changed in status — these are not deviations from a norm, they are six models' own answers.)*

**The governing rule at v0.7.0:** *each Record Model owns the packaging of its Records.* The table below is **retained as architectural evidence, not as a freeze** — it records the partition-level reasoning available at v0.6.1, which is **design input** to each model's own work. A model may later declare differently for its own reasons, without reference to any other model and without amending this section's rule.

**Status of the rows below (v0.7.0).** *(ADDED. The table was authored at v0.6.1, before any of the five non-World models had been independently researched. Its reasoning is stated and sound as far as it goes; what it cannot be is evidence of a design that has not yet been done.)*

| Row | Status | Why |
|---|---|---|
| **W** instance-bearing, **W** WSV | **ESTABLISHED** | The World Record Model is designed and its package is in use throughout this document |
| **E · P · R · V · I** | **MODEL-DESIGN INPUT** *(not a freeze)* | Authored from partition-level reasoning, not from model-specific design. Each row is **evidence for** that model's future design work, not a constraint on it. The governing principle is that **package architecture is model-owned** — Registry-owned for R — and each model establishes its own (I-107) |

**A MODEL-DESIGN-INPUT row is not a freeze and must not be implemented as one.** No downstream artifact may treat `Record + History Record` — or any other composition below — as a settled requirement for E, P, R, V, or I. In particular, **a model may conclude that it needs no History Record at all**, or needs a versioning, lineage, event-log, or supersession mechanism instead; §13.7a and I-90 permit that outcome and this table does not overrule them. *(Recorded as **FG-V7-06**.)*

**The governing principle, stated so that the table cannot be read as overriding it:**

| Record Model | Package architecture |
|---|---|
| **W** | **Established** — the World Record package (§13.9) |
| **E · P · V · I** | **Model-owned** — each establishes its own |
| **R** | **Registry-owned** — Registry establishes its own, as the model whose Records are definitions (§13.6e) |

**How a model declines or changes a shape (v0.7.0).** A Record Model changing its own packaging is a **schema change at Foundational ceremony**, recorded in both documents in the same cycle (§13.7) — the same bar as kind admission (§13.11), and for the same reason: packaging is how a model's semantics are stored, and a model that could change it quietly could change its meaning quietly. **What it explicitly does not require is any other model's agreement.** Five of the six rows below are declarations against schemas that are still **OPEN** (§13.6a, §13.6b); a model closing its schema may confirm or revise its row.

**Legacy reading, stated once.** In v0.6.3 the columns below read `CO`, `COR`, and `COH` — Canon Object, Canon Object Relationship, and Canon Object History. `CO` is now simply the Record. `COR` and `COH` are now the **Relationship Record** and the **History Record**, and both are the **World Record Model's** Relationship Record and History Record (Section 13.9), and the fact that other models currently adopt structures of the same shape does not make those structures universal primitives — it records that six models were asked the same question and four gave overlapping answers.

| Partition | Package | Why |
|---|---|---|
| **W** instance-bearing | `Record + Relationship Record + History Record` | Full package. Unchanged. |
| **W** WSV singleton | `Record + WSV-H` | No Relationship Record — indicators are keys, not objects, so WSV is always the non-owning endpoint (Section 13.10). |
| **E** | `Record + Relationship Record + History Record` | Epistemic records relate heavily — evidence to fact, belief to knower, question to evidence chain — and their history is the reveal history. Full package. |
| **P** | `Record + History Record`, **Relationship Record optional** | Most production records relate to few things and by reference. Where a production record genuinely owns relationships — a writer persona's attachment to a character and a publication role — it carries a Relationship Record. Where it does not, an empty Relationship Record is ceremony without content. |
| **R** | `Record + History Record`, **no Relationship Record** | A definition's "relationships" are its *dependencies*, and those are governed by the downward-only rule (Section 9.4), not by edge ownership. Registry history is essential and frequently consulted: *when did this vocabulary change, and what did records mean before it?* |
| **V** | `Record + Relationship Record + History Record` for specifications; `Record + History Record` for assets and analyses | A canonical visual specification owns relationships — *depicts*, *supersedes*, *derives-from*. An asset's links are references, not owned edges. |
| **I** | `Record + History Record`, **no Relationship Record** | A published issue is **immutable**, so its History Record has exactly one substantive entry — publication — plus any supersession. Its internal structure is composition, not relationship: a page belongs to a spread the way a paragraph belongs to an article. |

**The invariant this preserves:** wherever a Relationship Record exists, the ownership rule holds without exception — one authoritative edge, in one Relationship Record, declared by the relationship type (Section 13.9). Specialization changes *whether* a partition uses Relationship Records, never *how* they work.

**Traceability is universal; the History Record is World's answer to it (REVISED v0.7.0).** Every partition must be able to answer the P-18 questions — *what changed, when, why, who approved it, what caused it* — and a registry definition that changed without a record, or a published issue whose publication left no trace, would each break P-18 in the same way a world record would. **That obligation is constitutional (Spine law 9, I-09) and is not negotiable for any model.**

**What v0.7.0 changes is the claim one rung above it.** v0.6.1 wrote *"History Record is universal,"* which stated a *mechanism* where a *requirement* was meant. Each Record Model owns the packaging of its temporal account: World uses the **History Record** (Section 13.9); the five other models currently adopt a structure of the same shape, and each may later declare a different one — an event log, a revision chain, a version lineage, or a publication provenance stamp — provided the P-18 obligation is met in full. **The obligation is shared. The mechanism is model-owned.**

> **REQUIRES AUTHOR DECISION — AD-11.** I-11 as written binds *"every Record"* to *"exactly one logical history record."* Read as a World invariant it is unaffected by this revision; read as a universal invariant it constrains five models' temporal architecture before those models exist. v0.7.0 adopts the **World reading** and records the ambiguity rather than resolving it silently. The invariant register carries the flag (Section 36.2).

### 13.6e The Registry Record Model (v0.7.0)

*(ADDED. Structural addition justified: §9.4 specifies the Registry **layer** — its five semantic layers and its downward-only dependency rule — and was written when Registry was infrastructure. It does not specify Registry as a **Record Model with its own Records**, which is what v0.6.1's promotion made it and what the Record System requires. The distinction could not be expressed by revising §9.4 in place without conflating the layer with the model.)*

**Registry is a sovereign Record Model, not a lookup table.** It is not a metadata service, a configuration file, a passive catalog, a generic capability layer, or a runtime storage abstraction for the other five models. **It is the Record Model whose domain is definition and governance**: it records, defines, governs, and manages the semantic definitions the rest of the Record System resolves against.

**Registry definitions are Records.** A kind definition is not a constant in source code; it is a Registry Record with identity under the universal grammar (§13.9a), provenance, a governed change path, and a temporal account. **This is the point of the v0.6.1 promotion** — those definitions needed identity, provenance, history, a gate, and a linter, and calling them infrastructure meant they were governed by convention instead of by rule (§13.6).

**Registry Record categories.** The currently declared roster is at §13.6 and extends by ordinary Registry change (§9.4). Grouped by what they govern:

| Category | Governs | Declared kinds |
|---|---|---|
| **Structural definition** | What a Record of a kind is | KIND-DEF · SUBTYPE-DEF · FIELD-DEF |
| **Semantic definition** | What a value or term means | CONTROLLED-VOCABULARY |
| **Relational definition** | What a relationship type is and which role owns it | RELATIONSHIP-TYPE-DEF |
| **Identity definition** | The grammar's roster and its per-partition kind codes | IDENTITY-GRAMMAR |
| **Constraint and rule** | What must hold, and what may be recomputed | VALIDATION-RULE · DERIVATION-RULE |
| **Indicator definition** | What a world-state indicator means | WSVR-INDICATOR-DEF |
| **Model definition** | What a simulation model is | SIMULATION-MODEL-DEF |

**OPEN — Registry's own taxonomy.** Whether Registry additionally needs a **Record Model definition** kind — a definition of a Record Model as such — is **not established by any source** and is not invented here. It is the natural completion of a definition library that governs six models, and it is exactly the kind of thing that must be designed rather than inferred from symmetry. *(Recorded as **FG-V7-07**.)*

#### The authority boundary — definition versus ownership

**This is the distinction that keeps Registry from becoming a universal super-model, and it must not be blurred.**

> **Registry governs the definitions. Each Record Model owns its Records.**

| Registry owns | Each Record Model owns |
|---|---|
| The definition of a kind | Which Records of that kind exist, and what they mean in its domain |
| The definition of a field | The values its Records carry |
| The definition of a relationship type and its owning role | Whether it uses Relationship Records at all (§13.6d) |
| The definition of a validation rule | Its own semantic validation beyond structure |
| The definition of an indicator | The indicator's current value (World/WSV) |
| Registry-domain semantics and its own Records | Its own lifecycle, authority, canonicality, and temporal architecture |

**Therefore: semantic *authority* over definitions is not semantic *ownership* of domain Records.** Registry defines what a `CHARACTER` is; it never holds a character, and it never adjudicates what is true of one (§9.4, I-88). World owns World Record semantics; Epistemic owns Epistemic Record semantics; Production, Visual, and Issue likewise. **Registry owns Registry-domain semantics and the definition layer the wider system resolves against — and nothing else.**

#### Dependency direction

**Downward only, and the direction is asymmetric by design** (§9.4): a Registry definition may never reference a kind, a subtype, or an instance; a kind may never reference an instance. The five other models depend on Registry **for definitions**; Registry depends on them **for nothing**.

**The circularity that must not be created:** Registry must not require the complete semantic implementation of every other Record Model in order to define them. It defines *structure and meaning*, which is available before a model's domain design is complete — which is why Registry can be built while E, P, V, and I schemas remain OPEN.

#### The bootstrap problem — stated, not solved

**If Registry records the definitions used by the Record System, and Registry is itself a Record Model whose Records have kinds and fields, what defines Registry's own kinds?**

The blueprint has a partial answer and does not have a complete one, and v0.7.0 declines to invent the remainder.

**What is established** (§13.7): a **Bootstrap Meta-Contract** exists, is deliberately small, and defines only what a Record must have to be a Record at all — *partition · kind · identity · core envelope · provenance · Registry reference*, **nothing else**. It is explicitly sufficient to create the first Registry entry and the first Record and insufficient for anything more, *"because a bootstrap that could express the whole model would be the model."* The Registry Kernel and the Record Model Schema are then built **together**, neither finished ahead of the other.

**What is OPEN:** whether the Bootstrap Meta-Contract is itself a Registry Record, a constitutional statement in this Blueprint, or a third thing standing outside both; and how Registry's own KIND-DEF is defined without a prior KIND-DEF. The meta-contract's *content* is settled; its *ontological status* is not. **This is a genuine architectural question, not an omission, and closing it by assertion would be the error the meta-contract exists to prevent.** *(Recorded as **FG-V7-05** — REQUIRES AUTHOR DECISION.)*

#### WSV attribute definitions

**Three things are distinct and are routinely conflated** (§13.10, I-91):

| Concept | Where it lives | Which model owns it |
|---|---|---|
| **What an indicator means** — type, unit, valid range, lifecycle, derivation, validation | `WSVR-INDICATOR-DEF`, an **R** Record | **Registry** |
| **How an indicator behaves** — dependencies, equations, thresholds | `SIMULATION-MODEL-DEF`, an **R** Record | **Registry** |
| **What an indicator currently is** — its value | WSV, a **W** Record | **World** |

**An indicator definition is a Registry Record.** It is not an arbitrary property embedded in source code and not a field of the Record carrying the value. **And it is not a universal semantic field of every Record**: indicators are World-state quantities, sub-addressable within WSV, and *"not a Canon Object"* in v0.6.3's terms — they have no identity, status, or tier of their own (§13.10). Nothing in the other five models carries a WSV attribute by default, and no reading of this section may make one universal.

### 13.7 Envelope Custody

Two documents cannot own one schema; they diverge, and they already had. The rule: **this blueprint owns the Record's *properties*; the Record Model Schema file owns its *fields*.**

*(RENAMED v0.7.0. The companion document formerly titled the **Canon Object Model** is the **Record Model Schema**. The rename is of the document's title and governing subject, not of its custody: the custody split below is unchanged, and the lockstep obligation is unchanged. **The companion document has not been revised by this revision** — until it is, it remains the authoritative source on fields under its former title, and the lockstep rule below is in a known-outstanding state. Recorded as **FG-V7-01**.)*

The Blueprint states, permanently — **for the World Record Model, whose architecture these describe** (§§13.3–13.5, I-102): identity is separate from state; fields are split by mutation class (locked / world-state / derived); relationship semantics are first-class and relationship storage is Relationship Record-owned; history is referenced, not contained; every Record has a partition, a kind, provenance, and a Registry reference — **the bootstrap set, and no more than that** (§13.7 above, §13.7a). *`tier` and `status` are World Record Model properties: `tier`'s vocabulary is World ontology and its applicability elsewhere is **OPEN** (FG-V7-03), and `status` admits `CANON`, which two models can never reach (§13.7c). Neither is a universal envelope property.* Knowledge-state on a World Record is a **derived, non-authoritative convenience projection** — the authoritative epistemic record is always a separate object in the Epistemic partition (Section 14). The Record Model Schema states the field names, types, required-ness, defaults, the Canon ID grammar, and schema-evolution ceremony. **Where the two appear to conflict, the Record Model Schema governs on fields and the Blueprint governs on properties.** The YAML in Section 13.1 is illustrative of the properties and is not the schema.

**The lockstep rule.** A change to kinds, `<kind>_type` vocabularies, or the package model that lands in only one of the two documents is a defect regardless of which one it lands in. The custody split at this section is what prevents divergence, and a custody split is only as good as the discipline of updating both sides together.

**Lockstep does not mean sequence.** The Record Model Schema is **not** a standalone document that must be completed and frozen before Registry work may begin — that reading would require the field-level schema of six partitions to be authored before the semantics those fields express exist, which is backwards. The correct order is:

```
Bootstrap Meta-Contract
        ↓
Registry Kernel  ↔  Record Kernel      built together
        ↓
Validation
        ↓
Store / Mutation
```

**The Bootstrap Meta-Contract is deliberately small.** It defines only what a record must have in order to be a record at all: **partition · kind · identity · core envelope · provenance · Registry reference**. Nothing else. It is sufficient to create the first Registry entry and the first Record, and it is not sufficient for anything more — which is the point, because a bootstrap that could express the whole model would be the model.

**From there the two expand together.** The Registry defines kinds, `<kind>_type` vocabularies, field definitions, relationship definitions, validation rules, visual reference policies, and semantic constraints. The Record Model Schema defines how those contracts appear in concrete records. Each new Registry definition has a corresponding Record Model Schema expression, authored in the same act. **Neither document is ever "finished" ahead of the other**, and neither blocks the other.

### 13.7a Shared Infrastructure Is Not Shared Semantics (v0.7.0)

*(ADDED. This section exists to stop the Record System becoming the Canon Object Model under a new noun. It is the boundary that the retired architecture did not have.)*

**The distinction.** A **shared mechanism** is a technical facility that six models may use without any of them agreeing about meaning. A **shared semantic** is a claim about what a Record *is*, and it binds every model that carries it. **The Record System shares mechanisms. It does not share semantics.**

**What is shared infrastructure — technical, model-agnostic, and legitimately common:**

| Mechanism | What it does | What it does not decide |
|---|---|---|
| Identity minting, parsing, resolution | Produces, reads, and resolves stable identifiers | What constitutes the identity of a Record in any model |
| Serialization | Renders a Record as legible durable text (§26.3) | What fields a Record has |
| Structural validation | Is this a well-formed Record at all | Kind legality, tier rules, relationship legality — all semantic |
| Provenance capture | Records who, when, why | What provenance *means* in a model (§13.7b) |
| Reference resolution | Resolves an `_ref` to its target (§9.4) | Whether the reference is semantically legal |
| The single gated mutation path | Propose → check → gate → commit → changelog → log | What a model considers a legal change |
| Source-of-truth classification | Assigns one of five classes (§29.6a) | Which class a model's data belongs to |
| Storage and repository access | Puts durable bytes somewhere | The model's storage semantics |

**What is *not* shared, stated as prohibitions because a list of permissions would be read as exhaustive:**

- **No Universal Record Base.** The shared layer is the bootstrap contract of §13.7 and nothing above it.
- **No Universal Relationship Record.** Relationship packaging is model-owned (§13.6d, §13.9).
- **No Universal History Record.** The P-18 obligation is universal; its packaging is model-owned (§13.6d).
- **No universal lifecycle.** Two models hold Records that can never be canonical; a status vocabulary admitting `CANON` everywhere would be false (§13.6a, §9.4).
- **No universal canonicality.** Six models, six meanings (§13.7c).
- **No universal kind taxonomy.** Each model owns its own (§13.11).
- **Identity is the one deliberate exception, and it is a *grammar*, not a semantics (AD-1, resolved).** The identity **grammar** `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` **is constitutional and universal across all six Record Models** (§13.9a, I-82). What remains model-owned is the **semantic interpretation** of what that grammar names: which kinds exist, what a kind means, what constitutes the identity of a Record in that model, and what its lifecycle, authority, and temporal meaning are. **A universal identity grammar is not a universal Record semantics** — the grammar fixes the syntax of the name and decides nothing about the thing named.
- **No universal state model.** Locked / world-state / derived is a World field-mutation-class split and is not claimed elsewhere.
- **No universal Record schema.**

**The test to apply when a future version proposes to share something.** *Is this a facility, or a claim?* A facility may be shared on convenience. A claim must be proven in each model that carries it, and a claim proven in one model and asserted in six is the exact error v0.7.0 exists to retire.

### 13.7b Provenance, Audit, History, Revision, Version, and Lineage (v0.7.0)

*(ADDED. These six were used interchangeably in v0.6.3 and are not interchangeable. Separating them is a precondition for letting each model own its temporal architecture without importing World's.)*

| Concept | What it answers | Where it lives |
|---|---|---|
| **Provenance** | Who made this, when, and **why** | An envelope property on the Record (§13.1) |
| **Audit** | Under what approval mode, in which session, by whose act | Recorded within each temporal entry (I-14, §12.16) |
| **History** | How this Record's state came to be what it is | Model-owned packaging; World uses the History Record |
| **Revision** | This Record changed, and here is the change | Model-owned |
| **Version** | This is a distinct issued state of the same thing | Model-owned; Issue versions by supersession, never by edit (§13.6a) |
| **Lineage** | This came *from* that | **Ambiguous and now disambiguated** — see below |

**Lineage is retired as an unqualified term.** v0.5 already renamed the envelope field from `lineage` to `derivation` to free the word for the World kind `LINEAGE` (§13.1), and the Visual Library separately uses *derives-from* for asset descent. Three senses, one word. **v0.7.0 forbids the unqualified use:** write `derivation` for identity operations (§13.8), `LINEAGE` for the World kind, and *visual derivation* for asset descent. Spine law 9 is unchanged and reads correctly without the word.

### 13.7c Canonicality Is Model-Defined (v0.7.0)

*(ADDED. v0.6.3 already assigned different governance to each partition at §13.6; v0.7.0 states the consequence that assignment implies.)*

**Canonicality is a status property whose meaning is defined by the Record Model that has one. It is not a universal boolean and not a property every Record carries.**

| Record Model | Canonical? | What "canonical" means there | Authority |
|---|---|---|---|
| **World** | Yes | This is true of the world | The Human Gate (Spine law 3) |
| **Epistemic** | Yes | This is authoritatively what is known, believed, or revealed — **not** that the proposition is true | The Human Gate |
| **Production** | **Never** | Production State is committed intent, never world truth (§9.1) | Production ceremony |
| **Registry** | Yes, **about meaning** | This definition is the authoritative meaning records resolve against | Registry change (§9.4) |
| **Visual** | **By kind** | A specification is canonical; an asset is a manifestation; an analysis is an observation (§13.6c) | Gate, per kind |
| **Issue** | **Never** | Nothing is true because it is printed (§13.6a, Spine law 5) | Publication |

**Two consequences.** A `status` vocabulary admitting `CANON` in every partition would be false in two of six — the vocabulary is a Registry-owned controlled vocabulary and is legitimately per-partition (§9.4, which already prohibits a forced enum union). And **a projection does not become authoritative by being stored** (§12.4, §29.6a); each Record Model owns the meaning of its own authoritative state.

### 13.8 Identity Operations

*(SCOPED v0.7.0. The four operations below are **World Record Model** semantics. Their mechanism — a gated act that preserves every history involved — is shared infrastructure and available to any Record Model; their **meaning** for the five other models is **OPEN** and is not invented here. Issue's supersession rule (§13.6a) is the one other model whose behaviour is already frozen, and it is a publication rule, not one of these four.)*

Identity questions — *is this the same thing?* — are answered, **in the World Record Model**, by four operations and nothing else. Each is a gated canonical act (Section 12.13) that writes to History Record and preserves every history involved.

- **Supersede.** Object A is replaced by object B; A's identity ends, B records what it succeeded, and A's history remains reachable from B.
- **Split.** One identity becomes several; every successor references the origin and the origin's full History Record.
- **Merge.** Several identities become one; the survivor carries **all** predecessor histories, and none is discarded, summarized away, or preferred.
- **Retire.** Identity ends without a successor, by retcon or by world-event. History is retained in full, forever, and the retirement records which.

**Invariant.** An object's history is never orphaned: from any current object, every history that flowed into it is reachable; from any retired object, its successors (if any) are reachable. This is what makes *"why is this the way it is?"* answerable after ten years of restructuring.

**Why these four became simpler in v0.5.** When a relationship was its own object with its own history, every identity operation had to dispose of the edges' independent histories as well as the nodes' — and a merge of two objects with overlapping edges could orphan an edge history with no successor to attach it to. Under Relationship Record ownership an edge's history is already inside an endpoint's History Record, so it travels with that endpoint automatically. The operations lost a special case and gained nothing to compensate for, which is the shape of a correct simplification.

### 13.9 The World Record Package — Record, Relationship Record, History Record (v0.5, RESCOPED v0.7.0)

*(RESCOPED. Content preserved in full; scope narrowed from "every Record" to the World Record Model, which is where the evidence for it lies. Other models' packaging is their own (Section 13.6d).)*

**These are World Record Model concepts. They are not Record System primitives.** A Relationship Record is not a universal component, and a History Record is not a universal component. Where another model adopts a structure of the same shape, it does so on its own evidence and owns the result.

Every **World** Record is a package of three records with one identity between them.

| Record | Holds | Mutability | Authority |
|---|---|---|---|
| **Record** — Record | Identity, classification, current state, current in-world temporal context, body | Locked fields immutable; world-state fields advanced by Simulation at light ceremony; derived fields rebuildable | **Authoritative** for what this object is and how it currently stands |
| **Relationship Record** — Relationship Record | This object's **current** relationships, each with its type, roles, direction, temporal validity, and provenance | Mutated only through the gated path; every mutation writes History Record | **Authoritative** for the edges it owns; never a history ledger |
| **History Record** — History Record | The complete evolutionary record of changes to this object's Record **and** Relationship Record: what changed, previous state, resulting state, change semantics, world-time context where relevant, authoring sequence, and session | **Append-only.** Never edited, never reordered, never deleted | **Never authoritative about the world.** Explains how the Record came to be as it is (Section 12.9) |

**The three identities are linked by suffix**, so all three are findable from any one:

```
W-CH-001-Maximus        the Record
W-CH-001-Maximus-R      its Relationship Record
W-CH-001-Maximus-H      its History Record
```

**The package is logical and semantic.** An implementation may store, index, or project the three differently — one file, three files, or a table apiece — provided the semantics survive. What it may **not** do is collapse relationship semantics into arbitrary fields in a way that destroys identity, provenance, or history (Section 26.4). No Record may exist whose relationships or history cannot be located from it, and none may exist orphaned from a Record.

### 13.9a Identity Grammar (v0.6)

*(CLARIFIED. Source: authorial decision. v0.5 fixed the shape; v0.6 fixes the form and states it in the Blueprint rather than leaving it entirely to the companion document, because partition-first identity is an architectural property and not merely a field format.)*

```
[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]
```

**This grammar is universal across all six Record Models (AD-1, resolved v0.7.0).** A World Record, an Epistemic Record, a Production Record, a Registry Record, a Visual Record, and an Issue Record all bear an identity of this form. The grammar, its element order, its parsing and resolution contract, and its uniqueness contract are **shared infrastructure and constitutional** (§13.7a, I-82).

**What the shared grammar does not share.** It fixes the **syntax** of a name and decides nothing about the thing named. **Kind occupies a defined position in the grammar; the kind taxonomy and the meaning of any kind are owned by the Record Model** (§13.11). Two Records may be identically well-formed and have nothing else in common — a `W-CH-…` and an `R-…` share a shape, not a lifecycle, an authority, a temporal architecture, or a package. **Universal identity grammar ≠ universal Record semantics.**

| Element | Rule |
|---|---|
| `PARTITION` | `W` World · `E` Epistemic · `P` Production · `R` Registry · `V` Visual Library · `I` Issue. *(CORRECTED v0.7.0: the v0.6.3 row still listed four, having never been updated when v0.6.1 promoted Registry and Visual to partitions.)* **The first element is always the partition** — identity declares which side of a boundary a Record sits on, and therefore which Record Model owns it, before it says anything else. |
| `KIND` | The kind code **within that partition**. It is a kind code, never the word "Canon". |
| `OBJECT_ID` | Stable ordinal. Never reused, including after retirement, because history references it forever. |
| `SLUG` | Human-readable. **Decoration only** — nothing resolves, matches, or validates against a slug, and a slug that has drifted from the object's name is untidy rather than wrong. |

**A rename must not silently create a new canonical identity.** Renaming changes the display name and retains the former name; the identity is untouched. Identity changes only through the four identity operations (Section 13.8), each of which is a recorded, gated act.

**An internal machine identifier may exist as an implementation detail** — a row key, a hash, a UUID — but it must not replace, shadow, or contradict the canonical identity. If the two ever disagree, the canonical identity is right.

**Kind codes are two characters, frozen.** Every Record kind in every partition uses a two-character code. Single-character codes were considered and rejected: with seven instance-bearing World kinds they do not disambiguate — `C` would serve both Character and Concept, `L` both Lineage and Location.

| World kind | Code | Example |
|---|---|---|
| CHARACTER | `CH` | `W-CH-001-Maximus` |
| CONCEPT | `CO` | `W-CO-001-Democracy` |
| ORGANIZATION | `OR` | `W-OR-001-Empire` |
| LINEAGE | `LI` | `W-LI-001-DelPhonar` |
| SPECIES | `SP` | `W-SP-001-Human` |
| EVENT | `EV` | `W-EV-001-WarOfTheNorthernPasses` |
| LOCATION | `LO` | `W-LO-001-Rome` |
| WSV *(singleton)* | `WS` | `W-WS-001-<world>` |

**The Registry owns the authoritative kind-code mapping** (`R` partition, §9.4). Codes for the E, P, R, V, and I partitions follow the same two-character rule and are Registry entries like any other — the *rule* is frozen here; the *roster* extends through ordinary Registry change (§14 below).

**One disambiguation, resolved v0.7.0.** v0.6.3 had to warn that the kind code `CO` (Concept, in the second position of an identity) was not the abbreviation `CO` (Canon Object). **The abbreviation no longer exists** — the current-state record of a World package is simply the Record (§13.9) — so the collision is gone rather than managed. `CO` now means Concept and nothing else. *(Recorded because the retirement of an abbreviation is the kind of change that otherwise leaves a stale warning in place for a decade.)*

**Ownership: which Relationship Record holds an edge.** An edge joins two objects. If both endpoints' Relationship Records held it authoritatively there would be two sources of truth for one edge — a direct violation of Spine law 1. Exactly one endpoint owns it:

> **The relationship *type definition* in the Registry declares which participant role owns the edge.** `MEMBER_OF` is owned by the member; `LOCATED_IN` by the located thing; `DESCENDS_FROM` by the descendant; `CAUSED` by the causing event.

This rule is deterministic, requires no tie-breaking, and does not depend on creation order or on which object the author happened to be editing. The **non-owning endpoint sees a back-reference**, which is a **Derived** projection (Section 12.4, Section 12.11): rebuildable from the owning Relationship Records, marked stale like any other, and never authoritative. An edge appearing authoritatively in two Relationship Records is a structurally decidable violation and is blocked by the linter (Section 12.15).

**What is tracked by session.** Every History Record entry — for a Record change or a Relationship Record change alike — records the session that introduced it (Section 12.16). This is how *"which session introduced this relationship change"* is answered without a second history system: there is one history mechanism, and session is one of the things each entry records.

**Where projection is allowed.** Three places, all marked Derived and none authoritative: relationship back-references on the non-owning endpoint; `knowledge_state` on a Record (the authoritative record is always an Epistemic object); and every world-monitoring view (Section 12.11). Everywhere else, a value is either canonical or it does not exist.

### 13.10 WSV — The World State Record (v0.5) · **PROPOSED**

> **This subsection records a resolution that is PROPOSED, not settled.** Two supplied sources conflict: one states that WSV takes the ordinary Record/Relationship Record/History Record package with WSV-H additionally; the other states that WSV is a single record holding the indicators, with only a WSV history. The reading below reconciles them, and one consequential question (entry granularity) remains **OPEN**. This flag is removed only by an explicit authorial decision.

**WSV is one record, not many.** Unlike the other seven World kinds, WSV does not have per-instance records. There is one WSV holding the world's tracked indicators — the quantities Simulation moves through time, each with its value, its valid range, and its dynamics (momentum, inertia, thresholds; Section 15.5). An individual indicator is **sub-addressable** within the WSV — Simulation must be able to say *which* indicator crossed a threshold, and a pressure edge must be able to name a specific endpoint — but an indicator is **not a Record** and has no identity, status, or tier of its own.

**WSV's package is `Record + WSV-H`.**

- **Record** — the WSV record itself: the current value of every tracked indicator, with its dynamics. Authoritative for world state. Tier 4 (Section 12.2).
- **No Relationship Record.** WSV owns no edges. This follows from indicators not being objects: a pressure edge *targets* an indicator, so under the ownership rule (Section 13.9) the edge is owned by the *other* endpoint — the condition doing the pushing. WSV is always the non-owning endpoint, and its view of what pushes it is a back-reference projection like any other.
- **WSV-H** — the history. **WSV-H *is* WSV's History Record**, specialized because its change semantics differ: it records indicator value transitions rather than field mutations. It is not an additional history alongside a History Record; WSV has exactly one history record, as every Record does (Section 12.9), and WSV-H is its name. This is what prevents the duplication of state truth that a parallel History Record-and-WSV-H arrangement would create.

**What WSV is authoritative for, and what it is not.** WSV is authoritative for the *current value* of a tracked indicator. It is **not** authoritative for why the value is what it is — that is causality, and causality lives in `EVENT` and in causal edges (Section 13.12). It is **not** a metrics or analytics store: a quantity is admitted to WSV only if the world's causality depends on it, and a quantity that exists to be *reported on* is Derived (Section 12.11). The distinction matters because an indicator in WSV must be gated to change, and a system that files analytics as world state will either gate trivia or stop gating.

**Historical world reconstruction.** The state of the world at a past moment is reconstructed the same way any past state is (Section 12.10.1): from an **epoch baseline**, which includes the full WSV state, advanced forward through WSV-H entries. This is a **read-only Derived reconstruction** and is never a path to current truth.

**WSV-H granularity is frozen: one simulation tick is one world-state transition is one WSV-H entry.** A tick that moves twelve indicators produces **one** entry containing twelve deltas, not twelve entries.

```
Tick 120 — one WSV-H entry
    population          10,000,000 → 9,980,000
    food_price_index           110 → 123
    unemployment               5.2 → 6.1
    public_trust                61 → 57
```

**Why the tick and not the indicator.** A tick is the causal unit: those four movements happened *together*, for related reasons, and splitting them into four entries would scatter one world-state transition across four records that could then be read, replayed, or compacted independently of each other. The entry names the model, dependency, driver, and causal chain once (§15.20) — which it could not do coherently if the chain were shared across twelve records.

**Per-indicator history remains answerable** by traversing tick entries; it is a query, not a storage shape.

**The WSV family is three artifacts.** **WSV** holds current indicator values (Record, World). **WSV-H** holds indicator value transitions and *is* WSV's history record. **WSVR** holds indicator *meaning* — value type, unit, valid range, lifecycle behaviour, allowed mutation path, dependency behaviour, derivation rules, validation constraints, and whether the indicator is canonical or derived. **WSVR is an `R` partition object** (Section 13.6), reached from each indicator's registry reference.

**The three-way separation, stated because conflating any two of them is the standing temptation (v0.6.1):**

| Holds | Where | Never holds |
|---|---|---|
| **What an indicator means** | `R` / WSVR | Values, behaviour, or history |
| **How an indicator behaves** — dependencies, rules, equations, transitions | `R` / Simulation Model definition (Section 15.17) | Values or meaning |
| **What an indicator currently is** | `W` / WSV | Meaning, behaviour, or history |
| **How an indicator got there** | `W` / WSV-H | Meaning or behaviour |

**WSV must stay lean.** A worked illustration of the boundary:

```
WSV holds only current values:
    population        = 18,420,000
    inflation         = 4.8
    public_trust      = 41
    unemployment      = 7.2

The Simulation Model holds everything about them:
    definitions · dependencies · equations · thresholds
    · transitions · feedback loops · units · assumptions

WSVR holds what each one means:
    type · unit · valid range · lifecycle · derivation · validation
```

**Do not turn WSV into a model encyclopaedia.** The moment a definition, an equation, or a threshold appears in WSV, the state record has started becoming the model, and the four-way separation above collapses into one place that answers every question badly.

**Three prohibitions follow.** *Do not put model definitions into WSV* — a model is a definition and belongs in Registry. *Do not put indicator semantics into WSV* — meaning belongs in WSVR. *Do not use WSV as a general analytics store* — a quantity enters WSV only if the world's causality depends on it (Section 15.5), and a quantity that exists to be reported on is Derived.

**OPEN — indicator semantic content.** The authority is settled and its ownership is not in question; what does not yet exist is WSVR's content. Recorded as a Registry requirement with a named owner, not invented here.

### 13.11 Kind Admission and Retirement (v0.5)

The taxonomy is closed at seven instance-bearing kinds. Closed does not mean permanent; it means an eighth kind is an event, not a convenience.

**Admission test.** A proposed World kind must answer all eight:

1. Does it require **independent canonical identity**?
2. Does it have an **independent lifecycle** — can it begin, change, and end without reference to any other object's lifecycle?
3. Does it have **meaningful independent history**?
4. Does it require **relationships** that cannot be represented cleanly as relationships on an existing kind?
5. Would a **subtype** be insufficient?
6. Would **`CONCEPT`** be insufficient?
7. Would a **Registry classification** be insufficient?
8. Does promoting it **avoid ontology bloat** — is the world genuinely poorer without it?

A "no" on any question refuses the promotion and names the correct rung: field, subtype, relationship, Concept, or Registry entry. Admission is a schema change at Foundational ceremony and lands in both documents in the same cycle (Section 13.7).

**`SPECIES` is recorded here as the worked example**, because it is the only kind v0.5 admits and a future author will want to see the test actually run. Independent identity: a species is not a property of its members. Independent lifecycle: emergence, spread, decline, extinction, none of which tracks any individual. Independent history: species-level history is the Chapter 2 substrate (Section 11.4). Relationships an existing kind cannot carry: inter-species relations, descent, symbiosis — an `ORGANIZATION` edge distorts every one. Subtype of what? No parent kind fits. `CONCEPT` insufficient: a species is a population, not an idea about one. Registry classification insufficient: a classification carries no state, history, or relationships. Bloat: one kind serving an entire chapter of the trajectory. **Eight of eight. Admitted.**

**Retirement.** Retiring a kind never deletes records of that kind. It is recorded as *"kind K is retired as of schema version N"*; existing records remain valid, readable, and historically reachable forever; new records of that kind are refused by the linter. Retirement follows the contraction path (Section 29.4), requires a stated destination for the concept — the rung it descends to — and is itself a recorded, dated act reviewed at the next epoch transition (P-25).

### 13.12 Event, Causality, and State Transition (v0.5)

Four systems in this blueprint can express a consequence: `EVENT`, causal edges, WSV dynamics, and History Record. Without an explicit assignment, causality gets represented in all four, disagrees with itself, and no single reading of the world is authoritative. The assignment:

| Concern | Owner | Not owned by |
|---|---|---|
| **That something happened** | `EVENT` — the occurrence, its world-time, its participants, its location | Not History Record. History Record entries that the *record* changed, never that the *world* did. |
| **That one thing led to another** | **Causal edges** in Relationship Record (Section 13.3), owned by the causing endpoint | Not Simulation. Simulation *walks* causal edges; it does not constitute them. |
| **That a condition accumulates toward a threshold** | **Pressure edges** in Relationship Record, owned by the pushing condition; the threshold itself is WSV dynamics | Not `EVENT`. A pressure is not an occurrence. |
| **That world state changed value** | **WSV**, with the transition in WSV-H | Not `EVENT`. An event may *cause* a transition; it is not the transition. |
| **That the record changed** | **History Record / WSV-H** | Not canon about the world. |

**The chain, stated once and referenced everywhere:**

```
EVENT              an occurrence, in world-time
  ↓ causal edge    (in the causing endpoint's Relationship Record)
CONSEQUENCE        another EVENT, or a change to a Record's world-state fields,
                   or a WSV indicator transition
  ↓
COMMIT             one transaction (Section 12.6)
  ↓
History Record / WSV-H        the record of what changed, from what, to what, in which
                   session, caused by which revision of which object
```

**Three rules this makes enforceable.**

1. **An `EVENT` does not contain its consequences.** It is connected to them by causal edges. An event record that enumerates its own downstream effects as content has duplicated the graph into prose, and the prose will drift.
2. **A WSV transition always names its cause** — a causal or pressure edge, or an authorial act (Section 5.2, authorial intent is a terminal cause). An unattributed transition is a P-18 failure and a Canon Health finding.
3. **The blueprint-level assignment stands; the Registry-level authority is frozen.** Which concern belongs to which owner is settled above. The *shared semantics* of causal and consequence types — a Registry authority — are deliberately frozen until the world-state history and indicator-registry schemas are complete, because a causal vocabulary designed before the state model it describes would have to be redesigned. This is an intentional freeze, not an omission.
4. **History Record is never read to establish causality about the world.** History Record says *this revision was caused by that revision*, which is a fact about the record. The world's causality is in the edges. The two are parallel and must not be conflated — this is the same distinction as Section 12.9's *"History Record is not another truth source,"* applied to the specific case most likely to violate it.

---

## 14. Knowledge-State Architecture

*(Record System note, v0.7.0: this section specifies the **mechanics** of the Epistemic Record Model. E is a **sovereign Record Model** (§13, I-101) — not World truth carrying knowledge fields, and not World semantics with epistemic additions. Its identity grammar is the universal one (§13.9a); everything else — its kinds, its temporal architecture, its packaging, its authority — is its own. Its detailed schema remains **OPEN** (§13.6b) and nothing below closes it.)*

The Truth Model (Section 12.4) answers *what kind of true* a statement is. The Knowledge-State Architecture answers the finer, equally load-bearing question: **who knows it, to what degree, and as of when.** Separating truth from knowledge is what makes mystery, dramatic irony, unreliable narration, and staged revelation mechanically possible rather than something the author must track by hand. It is the substrate every mystery and every multi-issue reveal runs on.

**Its role widened in v0.5 without any of its mechanics changing.** v0.4 had a World kind called `MYSTERY` alongside this architecture; v0.5 retires that kind and locates the whole of mystery here (Section 13.6). A withheld truth is now an ordinary World record of whatever kind it naturally is, and everything that makes it *mysterious* — its reveal-state, the questions it holds open, the evidence planted toward it — is an Epistemic record in this section. Nothing below was added to absorb that; the machinery was always here, and the kind was the redundant part.

### 14.1 The Knowledge Frames

A single world-fact is seen through distinct frames, and coolboy12 keeps them separate:

- **What is true** — the canonical world-truth (Canon). The ground floor; everything else is a *view* of it, possibly partial or wrong.
- **What the author knows** — the creator's own knowledge, which is total by construction (the author may know a truth no character or reader does, and may deliberately withhold it).
- **What the world knows** — the public, in-world common knowledge: what is openly established within the fiction.
- **What a character knows** — per-character knowledge, tracked for load-bearing characters: what they know, believe (possibly falsely), suspect, and are ignorant of.
- **What the reader knows** — per reader tier (casual / engaged / investigator / conspiracy theorist), what the published artifacts have actually conveyed.

A fact can be true, unknown to the world, believed-falsely by a character, suspected by the investigator-tier reader, and deliberately withheld from the casual reader — all at once, all recorded, none in conflict.

### 14.2 Reveal-State

Independent of who knows it, every load-bearing fact carries a **reveal-state** relative to the readership: **HIDDEN** (true, not yet conveyed), **AMBIGUOUS** (deliberately clued but unresolved — designed negative space), or **REVEALED** (conveyed and now part of reader knowledge). Reveal-state transitions are authored moments (never automatic), and moving a fact to REVEALED is a gated editorial act, because it is irreversible for the reader.

**Reveal-state is what makes a fact load-bearing-mysterious (v0.5).** The Reading of Law 7 (Section 10.5) defines a load-bearing mystery as a *condition*: a fact whose reveal-state is HIDDEN or AMBIGUOUS for at least one tier, or on which an open Question or planted Evidence chain depends. Because reveal-state and evidence linkage are fields, that condition is structurally decidable (P-24) and the Severity Floor blocks on it rather than advising. This is a strictly wider net than the retired `MYSTERY` kind cast, which caught only what the author remembered to file as one.

**Epistemic state is subject-relative. Frozen.** There is no single global reveal-state for a fact. Every epistemic state is held *by a knower*, and one fact carries as many states as there are knowers who have a relationship to it.

```
Fact X
├── Character A   → KNOWS
├── Character B   → SUSPECTS
├── Character C   → BELIEVES_FALSE
├── The public    → UNAWARE
└── Reader tier 3 → KNOWS
```

**This closes the cardinality question by dissolving it.** The earlier formulation asked whether reveal-state was one record per fact or one per fact × knower; the answer is that a reveal-state *without a knower is not a well-formed epistemic statement*. The implementation schema may still be elaborated progressively (§13.6b), but the semantic rule is frozen and no schema may contradict it.

**The distinctions of §14.19 are preserved and must not collapse into a generic knowledge record:** knowledge · belief · rumour · theory · conspiracy · misconception · evidence · interpretation · prediction · surprise · reveal-state. Each is a different relationship between a knower and a fact, and flattening them would lose exactly the structure that makes staged revelation possible.

### 14.3 The Clue Economy

Mysteries run on a **clue economy** — the managed budget of what has been planted, what it points to, and what it costs to redeem. Each clue is a graph edge from an artifact (or planned artifact) to the hidden fact it hints at, carrying its strength (how much it reveals), its tier-visibility (which readers can perceive it), and its status (planted / reinforced / redeemed). The economy tracks three balances: **planted vs. redeemed** (clues owed a payoff), **reveal readiness** (whether enough has been planted that a reveal will land as earned rather than arbitrary), and **reader suspicion** (the estimated degree to which each tier already suspects the answer). A reveal fired before reveal-readiness feels arbitrary; a reveal fired long after the investigator tier has solved it feels overdue. Both are findings Governance and Editorial surface.

### 14.4 Knowledge Progression Across Issues

Because reader knowledge advances only through published artifacts, it moves in discrete steps — one per issue. coolboy12 models a **knowledge trajectory** per tier: what each tier knows after each issue, and therefore what a planned issue must add, withhold, or complicate. This is what lets Editorial pace a revelation across five covers (Section 25) with confidence that the casual reader still has a complete surface experience while the investigator is being fed a real, redeemable chain. Reader-state transitions over time are first-class: the system reasons about *the reader as of issue N*, not the reader in the abstract.

### 14.5 Deliberate Withholding

Withholding is a design act, not an absence. When the author holds a truth back, that is recorded — the fact is HIDDEN or AMBIGUOUS *on purpose*, with an intended reveal window (an issue, an arc milestone, or "indefinitely"). This keeps the negative space governed (Section 12.4, World-Reality) and stops the staff from ever "helpfully" resolving something the author is deliberately keeping open, and stops a returning author from forgetting that an ambiguity was intentional.

---

**The Reader Knowledge Model.** Sections 14.6–14.19 deepen this architecture substantially, because a reader is not a log of what they were told. A real reader believes things that are wrong, forgets things that were true, infers things never stated, predicts what comes next, notices what was withheld, and builds theories out of noise. A system that models only transmitted facts will consistently mistime every reveal it plans. Everything below is a **capability of the Knowledge-State architecture** — not a domain, not a primitive, and not an engine.

### 14.6 The Epistemic Lifecycle

A fact, per knower, occupies exactly one epistemic state:

**UNKNOWN** (no exposure) → **WITHHELD** (deliberately prevented from knowing — Section 14.5; distinct from UNKNOWN because it is *designed*) → **HINTED** (evidence exists but has not been assembled) → **SUSPECTED** (a hypothesis is live, unconfirmed) → **BELIEVED** (held as true — and *may be false*, Section 14.9) → **KNOWN** (true, held, and confirmed by the work) → **MISREMEMBERED** (once known, now held in distorted form) → **FORGOTTEN** (once known, no longer retrievable without reinforcement).

Three rules govern the lifecycle. Transitions are **evidenced**: nothing moves state without a cause recorded in the Evidence Graph (14.7) — in the class of evidence appropriate to that knower — or an authored decision. Transitions are **non-monotonic**: knowledge can go backwards, which is the single most important correction v0.4 made to the model. And the lifecycle applies to *every* knower — world, character, reader tier — with the same vocabulary, so a mystery can be reasoned about across all of them at once.

### 14.7 The Evidence Graph

Knowledge is not asserted; it is **caused**. Every epistemic transition traces to **evidence**, and because the system has two kinds of knower it has **two classes of evidence**. Both are first-class epistemic records (Section 13.6) connecting a *source* to a *target* (the canonical fact it bears on), and both carry **strength** (how much it moves a knower), **direction** (toward the truth, or toward a misconception — evidence can mislead, deliberately or accidentally), and **status** (planted / reinforced / redeemed / contradicted). They differ in source, in reach, and in axis:

- **Reader evidence** serves **outside-world knowers** — the reader tiers and divergent segments (Sections 20.1, 14.18). Its source is a published or planned **artifact**: a scene, a line, an image, an omission. Its reach is **tier visibility** (which readers can perceive it at all). Its axis stamp is **issue ordinal** (P-21, Section 12.16). *When the artifact shipped in wall-clock terms is production metadata on the artifact record, not a stamp on the evidence.*
- **World evidence** serves **in-world knowers** — the world's public knowledge and individual characters (Section 14.1). Its source is an **in-world occurrence**: an event, a witnessed act, a document or object found, a statement made, testimony passed on, or an **in-world publication** (Section 17.7.1). Its reach is **in-world reach** — who was present, told, or able to learn of it. Its axis stamp is **world-time**.

Neither class serves the other's knowers. A published artifact of ours does not, by existing, tell any character anything; an in-world event does not, by occurring, tell any reader anything. **What crosses between them is authored, never automatic**: the author decides that an in-world event is depicted in an artifact, and that decision produces reader evidence in addition to the world evidence, never instead of it.

The Evidence Graph subsumes and generalizes the clue economy (§14.3): a clue is evidence pointing at a hidden fact. It gives the system the one thing the clue economy lacked — the ability to answer *why* a knower believes something, by naming the evidence chain that produced the belief. An epistemic state with no evidence path **in its own class** is a defect of the same class as a canonical state with no derivation (P-18).

**The two epistemic routes.** Both kinds of knowledge are canonical (Epistemic partition, Section 13.6) and both reach canon through the single gated path, but they enter it differently and must not be confused:

| | **In-world knowledge** (world, characters) | **Outside-world reader knowledge** (tiers, divergent segments) |
|---|---|---|
| Evidence class | World evidence | Reader evidence |
| Changed by | An **ordinary gated canon proposal**, like any other world fact — usually as part of the event that caused it, so a witnessed act and who witnessed it commit together | A **Reader Knowledge Proposal** (Section 20.4), gated per issue |
| Axis | World-time | Issue-index |
| Caused by publication | Only by an **in-world publication act** (Section 17.7.1), and only for those with in-world reach | Only by an artifact actually published to readers |
| Withholding | The author may keep a fact from a character (Section 14.5) | The author may keep a fact from a tier (Section 14.5) |

Sections 14.8–14.16 apply to both classes of knower with the same vocabulary — confidence, dependencies, misconception, forgetting, inference, divergence, and leakage are all knower-agnostic. Section 14.10's decay curves, 14.11's surprise forecasting, 14.12's question and theory models, 14.13's fair-play validation, 14.14's knowledge debt, and 14.15's forecasts and heatmaps are **outside-world instruments**: they exist to time a reveal for readers, and they do not apply to characters, who are not being told a story.

### 14.8 Confidence and Knowledge Dependencies

**Confidence** is carried per knower per fact, in honest coarse bands — *certain / confident / suspicious / vague / absent* — never as false-precision numbers. Confidence is what distinguishes "the investigator has worked it out" from "the investigator would nod if told," and reveal timing depends on the difference.

**Knowledge dependencies** are prerequisite edges between facts: a reader cannot meaningfully know *why the succession failed* without knowing *who the claimants were*. Dependencies make three things computable that were previously guesswork: whether a planned reveal will *land* (its prerequisites are held), whether it will *confuse* (prerequisites are missing), and what minimum set of prior knowledge an issue must establish before a payoff can be attempted. A reveal fired against unmet dependencies is a **Governance finding**, not a taste question — the reader literally cannot assemble it.

### 14.9 The Misconception Model

Readers believe wrong things, and in a world with unreliable in-world publications, propaganda, and mistaken characters, they are *supposed* to. Misconceptions are tracked as first-class epistemic records: the false proposition, who holds it, the evidence that produced it, whether it was **authored** (planted deliberately), **emergent** (an honest misreading), or **accidental** (a craft failure), and its **correction path** — what evidence would dissolve it and whether the author intends to supply it.

The distinction between authored and accidental is the whole value: an authored misconception is a designed asset (dramatic irony, a red herring, an unreliable narrator paying off later); an accidental one is a defect. Without the model, both look identical from inside the system, and the second is discovered only when a reader complains.

**This model carries most of the magazine's weight (v0.5).** A publication that can be wrong, biased, propagandistic, or deceived (Section 17) generates authored misconceptions as its normal output, not as an exception. The Overtone printing something false is not a defect to be corrected; it is the mechanism by which a society reveals itself. What must never happen is the *reverse* — a published claim moving canon (Section 14.19).

### 14.10 The Forgetting Model

Reader knowledge decays. A fact established in issue 3 is not reliably held in issue 40, and long-form series fail routinely by assuming otherwise — either re-explaining what readers remember (condescension) or relying on what they have lost (incoherence). Forgetting is modelled per tier as a function of **salience** (how load-bearing the fact was when established), **reinforcement** (how often it has recurred since), **elapsed issue ordinal** (P-21 — never wall-clock time), and **tier** (an investigator rereads; a casual reader does not).

Its consumers are concrete: an issue plan reports which prerequisite facts have decayed below the confidence a planned beat requires, and Editorial can schedule **reinforcement** — a line, an image, a recurrence — instead of exposition. Reinforcement is evidence (14.7) and is planned like any other. *Reinforcement rather than exposition is also how the Artifact Principle (Section 5.3) survives contact with a long series: the alternative to re-explaining is not silence, it is recurrence.*

### 14.11 Inference, Prediction, and Surprise

Three capabilities that model what a reader *does* with what they have, rather than what they were given.

- **Inference.** What follows from a tier's current knowledge without further evidence. Inferable facts are treated as *effectively known* for pacing purposes, which is how the system stops explaining what the engaged reader has already worked out.
- **Prediction.** What a tier expects to happen next. This is the model of anticipation — the thing that makes a payoff satisfying or obvious. Predictions carry confidence and are tracked as they resolve.
- **Surprise forecast.** Before an issue is produced, the system estimates how each tier will experience each beat on two axes: **unexpectedness** (was it predicted?) and **retrospective inevitability** (does it feel earned given prior evidence?). The valuable quadrant is unexpected *and* inevitable. Unexpected and unsupported reads as arbitrary; expected and inevitable reads as flat. A beat forecast into a weak quadrant for its target tier is a Governance finding with a named axis to fix.

### 14.12 Theories and Reader Questions

**The Question Model** tracks the questions each tier is actively holding — *who killed him, what is under the northern ice, why does the symbol recur* — with the issue at which each opened, its evidence, and whether it is being fed, starved, or ignored. A question starved too long converts to disengagement; a question over-fed converts to impatience. Open questions are the ascending-current mirror of narrative debt (Section 17.3).

**The Theory Model** tracks the *hypotheses* a tier is likely to be entertaining, including wrong ones, with the evidence supporting each. It exists for two purposes: knowing whether the investigator tier has already solved a mystery (a reveal fired long after solution feels overdue), and modelling the conspiracy tier honestly. That tier's contract (Section 20.1) is to find real ore occasionally while not having nonsense validated; the Theory Model is where the system checks whether an unintended pattern is accidentally confirming a theory the world does not hold.

**Reader theory is never canon, and the direction of that rule is absolute (v0.5).** The chain runs *Canon → Artifact → Reader interpretation → Theory*, never *Theory → Canon*. A theory is an epistemic record about what a tier believes; it is canonical *that the tier believes it* and never canonical that it is true — the same rule that governs an in-world character's belief, applied to an out-of-world knower. Reader signal may legitimately inform *production* decisions (**FG-V7-04** — this cross-reference read "Section 37" in v0.6.3 and v0.7.0; **there is no Section 37**, the document ends at 36. Candidate intended targets are §17 Editorial Architecture and §20.8 The Reader Flywheel. Resolving it requires authorial intent and is not guessed here): a theory the author finds better than their own plan is a legitimate reason to *author* a change through the ordinary gate, and that is an authorial act with the author's reason recorded, not the theory propagating into canon. What the architecture forbids is popularity acquiring truth-authority by any automatic route.

### 14.13 Revelation Planning and the Fair-Play Validator

**Revelation Planning** turns a hidden truth plus a target issue into a *plan*: the evidence that must be planted, in what order, at what strength, visible to which tiers, with which prerequisites established first, and with the reveal-readiness curve that results. It is composed by the Composer from existing capabilities (Section 25), not a new engine.

**The Fair-Play Validator** answers one question before a reveal is produced: **could a reader of this tier, in principle, have assembled this answer from what they were actually given?** It walks the Evidence Graph backward from the revealed fact and reports what a reader would have needed, what they were given, and the gap. Its verdict classes are exact: *fair* (assemblable by the target tier), *fair-with-effort* (assemblable by a higher tier only), *unfair* (required evidence was never published), and *transparent* (assemblable long ago — the reveal is late). Unfairness is a **judged finding**, not a block (P-24): a deliberate unfair reveal is a legitimate authorial choice, made deliberately and recorded, rather than discovered by readers.

### 14.14 Knowledge Debt and the Completion Analyzer

**Knowledge debt** is the epistemic counterpart to narrative debt (§17.3): facts the reader has been promised, questions opened, evidence planted, and prerequisites established for payoffs not yet delivered. It accrues automatically when evidence is planted, escalates by age in issue ordinal, and is discharged only by a delivered payoff — or explicitly **written off** by the author (Section 17.8), which is a recorded decision, not a silent expiry.

**The Knowledge Completion Analyzer** asks the converse: given everything published, what does each tier *not yet have* that they will need for the arcs currently in flight — and what has been established that no plan currently uses? The second finding is as valuable as the first: unused establishment is either an opportunity (Section 16) or dead weight the reader is still carrying.

### 14.15 Forecast, Heatmap, and Knowledge Replay

Three projections (Derived, Section 12.11), each with a named consumer:

- **Knowledge Forecast** — the projected epistemic state of each tier at issue N+1, N+3, N+6 under the current plan, so Editorial can see where a plan leads before producing it.
- **Knowledge Heatmap** — a map over canon showing, per region and per tier, how much is known, suspected, believed-falsely, or withheld. It shows at a glance where the world is dark to readers, **where it is over-explained**, and where a mystery is thinner than it looks. The over-explained finding is the heatmap's contribution to P-30 and is read alongside Governance's own (Section 19).
- **Knowledge Replay** — a read-only walk through what a given tier knew, believed, and suspected as of any past issue (Historical Replay, Section 12.10.1, ordered by issue ordinal). This is what lets the author answer *"what did the reader actually have, back then?"* — the question every retrospective coherence dispute reduces to.

### 14.16 Multi-Perspective Divergence and Leakage Detection

**Divergence** is the deliberate condition where knowers hold incompatible pictures of the same fact: the world believes one thing, a character another, the casual reader a third, the investigator a fourth. Divergence is a designed state and is tracked as such, with its intended shape and its intended resolution point. Undesigned divergence — the same fact quietly presented two ways to two tiers with no intent behind it — is a **continuity defect** and appears in Canon Health (Section 12.15).

**Information Leakage Detection** watches the opposite failure: a truth reaching a knower it was never meant to reach. Leakage sources are enumerable and all mechanical: an artifact revealing more than its editorial intent allowed, a visual containing a detail the text withheld, a persona knowing something their knowledge-state says they do not, an index or projection exposing a hidden object, a Context Builder view placing a hidden solution in a role that should not hold it (Section 24.3), or a search result surfacing withheld canon. Under the P-24 criterion, leakage is **structurally decidable** where it is determinable from structure alone — a hidden object present in a context, projection, or index — and therefore *blocks*; where establishing it requires interpreting prose or an image, it is a **judged** finding at high severity.

**The public surface is the highest-consequence leakage boundary (v0.5).** Section 27.5 forbids the publication surface from exposing canon, schema, pipeline, metadata, authoring controls, or internal epistemic state. That prohibition is enforced here: the publication surface is a knower with a defined exposure set, and anything reaching it outside that set is leakage of the structurally decidable kind. A leak to a reader tier costs a reveal; a leak to the public surface costs the illusion the entire product rests on.

### 14.17 Bounded Epistemic Cardinality

Epistemic records multiply as facts × knowers and are the largest object-count multiplier in the system.

**Epistemic tracking is selective by design, and the selection criterion is recorded.** A fact is tracked per-knower only when it meets at least one **consumer test** (P-10): it is load-bearing for an active or planned mystery, arc, or reveal; a divergence about it is designed; it is a prerequisite for a planned beat; or the author has explicitly marked it tracked. Everything else falls to **frame defaults** — the world's public knowledge, and each tier's default exposure — which are computed, not stored per fact.

Three consequences. Promotion from default to tracked is automatic when a fact enters a plan, and is recorded. Demotion happens at **epoch transition** (Section 12.14), where facts no longer serving any active plan return to defaults, with their tracked history retained in the archive. And the tracked set has a declared budget the author can see: when epistemic tracking grows faster than the work, that is a finding, not a fact of life.

**Retcon reconciliation.** When a canonical fact is retconned (Section 12.12), every epistemic record referencing it is surfaced for disposition. Readers cannot un-read, and the model must not pretend otherwise: the tier's state becomes MISREMEMBERED or BELIEVED-falsely relative to new canon — which is honest, is often a story opportunity, and is never resolved by silently editing what readers were told.

### 14.18 Reader Segmentation and Tier Extensibility

The four readers (Section 20.1) are the **current roster**, not a law. The constitutional invariant is: *reader models are a finite, named, extensible set; each carries an explicit attention contract (what it is owed and what it may be asked to do); each is a Production record (Section 13.6); and each participates in every capability in this section identically.* Adding a tier — a listener for an audio manifestation, a player for a game, a first-time reader entering at issue 40 — is a Production State change with a named consumer, not an amendment. Retiring a tier follows the contraction path (Section 29.4), and its historical epistemic records are retained, never rewritten.

**Segmentation** additionally permits *cross-cutting* segments that are not tiers, and they come in two kinds that must not be confused:

- **Organizing segments** re-cut knowledge the model already holds — recency, engagement depth, attention profile. These are analytical views over existing tiers and **add no epistemic records of their own**.
- **Divergent segments** have a genuinely different exposure history and therefore a genuinely different knowledge set — **entry point** (started at issue 1 vs. issue 40) and **medium** (magazine-only vs. cross-media) are the two the system supports. A reader who began at issue 40 was never given what issues 1–39 established; that state cannot be derived from a full-exposure tier by any view. Divergent segments are therefore **knowers in their own right**, carry their own epistemic records, and count against the tracking budget of Section 14.17 exactly as tiers do.

Because divergent segments multiply cardinality, they are admitted like any other knower: with a named consumer (P-10) and under the selective-tracking criterion.

### 14.19 The Epistemic Vocabulary Map (v0.5)

The project's requirements name ten distinctions the architecture must hold apart: canonical truth, knowledge, belief, rumor, theory, conspiracy, misconception, unknown, evidence, and interpretation. All ten are already expressible; none requires a new kind. They are mapped here once so that no future subsystem invents a parallel vocabulary for a distinction this section already carries.

| Term | Where it lives | Note |
|---|---|---|
| **Canonical truth** | World partition (Section 13.6) | The only authority about the world. |
| **Knowledge** | Epistemic lifecycle state `KNOWN` (§14.6) | True, held, confirmed. |
| **Belief** | `BELIEVED` (§14.6) + `BELIEF` record | Canonical *that* it is held; never that it is true. |
| **Rumor** | `BELIEF` with an in-world knower, low confidence (§14.8), world evidence of weak strength and wide reach | Not a separate mechanism — a rumor is a widely-held, poorly-evidenced belief, which is what the fields already say. |
| **Theory** | `BELIEF` at `SUSPECTED`, held by a knower who is reasoning rather than reporting (§14.12) | Applies identically to an in-world researcher and an out-of-world reader tier. |
| **Conspiracy** | A theory whose evidence chain is dominated by evidence with `direction: toward misconception` (§14.7) | The conspiracy *tier* (Section 20.1) is a knower; a conspiracy *theory* is this. |
| **Misconception** | `MISCONCEPTION` record (§14.9) | Carries authored / emergent / accidental and a correction path. |
| **Unknown** | `UNKNOWN` (no exposure) vs `WITHHELD` (designed) (§14.6) | The distinction is the whole point: an absence and a decision are not the same state. |
| **Evidence** | `EVIDENCE` record, in one of two classes (§14.7) | Reader evidence and world evidence never serve each other's knowers. |
| **Interpretation** | A reader-side theory or inference (§14.11, §14.12) | Never canon; see the direction rule at §14.12. |

**The one rule that governs all ten.** *An epistemic record never mutates canon.* No belief, however widely held; no theory, however popular; no published claim, however authoritative-sounding in-world; no reader interpretation, however good, changes what is true by any automatic route. The only path from any of these into canon is an author proposing a canonical change through the gate, with their own reason recorded (Spine laws 1–3). This is the epistemic statement of the Publishing Firewall, and it is the reason the magazine can be wrong without the world becoming wrong.

### 14.20 Mystery as an Epistemic Structure (v0.6.2)

*(ADDED. **Post-v0.6 decision** — v0.6 relocated mystery to the Epistemic partition via the Reading of Law 7 (§10.5) and never gave it a structure. This supplies one. It is **not** a new domain, **not** a new partition, **not** a World Record, and **not** an engine.)*

v0.5 retired `MYSTERY` as a World kind on the finding that its truth was an ordinary world record and its unknown-ness was entirely epistemic. That was right, and it left a gap: a mystery has an **identity** — it is a thing the author plans, paces, and eventually resolves — and after v0.5 there was no record carrying that identity. Reveal-states and evidence chains existed; the mystery that organised them did not.

**A `MYSTERY` is an Epistemic object that organises a withheld truth, its disclosure, and its manifestations.** It holds no world facts and asserts none.

| Property | Specification |
|---|---|
| **Identity** | An `E` partition Record with a stable identity, per the identity grammar (§13.9a). It is addressable, referenced by plans, and survives renaming. |
| **References** | To **W** — the world record(s) that are the answer, by reference only. To **E** — the reveal-states, evidence chains, and open questions that constitute its unknown-ness. To **I** — the issues in which it was seeded, reinforced, or resolved. To **P** — the arc that paces it. **It owns none of them.** |
| **Lifecycle** | `posed` → `seeded` → `developing` → `reveal-ready` → `resolving` → `resolved`, or → `deliberately-unresolved`, or → `abandoned` (discharging its debt explicitly, §17.10). |
| **Deliberate unresolution** | A first-class terminal state, not a failure. A mystery may be designed never to resolve (§14.5), and recording that is what stops a returning author from mistaking an intention for a loose end. |
| **Author intent** | The reason it exists and what it is for, in Creative Memory. Intent is authorial and is never inferred from the evidence chain. |
| **Resolution** | An authored act. The answer becomes known to a knower by reveal-state transition (§14.2); the mystery's own state follows. **Resolving a mystery never changes what is true** — the truth was always true; what changed is who knows it. |
| **Reader-knowledge relation** | Through the evidence graph and reveal-state (§§14.2, 14.7), per knower. A mystery is not a reader-state; it is the structure the reader-states hang from. |
| **Queryability** | *What is open? What is reveal-ready? What has been seeded and never redeemed? Which mysteries does this world record answer?* All by reference traversal, no special mechanism. |
| **Provenance** | Ordinary (§13.1). Created by an authorial act, gated, recorded. |

**Three constraints.**

1. **The answer lives in W; the mystery lives in E.** A `MYSTERY` that carried its own answer would be a second place where a world fact is true — Spine law 1. It **references** the answer.
2. **Severity follows the Reading of Law 7 unchanged** (§10.5). A load-bearing mystery is still a *condition* — a reveal-state of HIDDEN or AMBIGUOUS, or a dependent evidence chain — and the Severity Floor binds on that condition whether or not a `MYSTERY` record happens to exist. **The record is an organising convenience; the floor does not depend on it.** This is deliberate: the v0.5 finding was that a kind-based reading caught only what the author remembered to file, and reintroducing a record must not reintroduce that gap.
3. **Existing mechanics are unchanged.** Clue economy, reveal-readiness, fair-play validation, knowledge debt, and revelation planning (§§14.3, 14.13, 14.14) operate exactly as before. A `MYSTERY` gives them a shared referent; it replaces none of them.


---

## 15. Simulation Architecture

Simulation is the domain that makes the world **react like a world and move like a world**: a full temporal reasoning system that can advance the world across a span, or steer it toward an intended end-state, always by walking the dependency graph and always producing *provisional deltas* that only the human gate can commit. The frozen rule is absolute and unchanged:

> **Simulation produces provisional deltas. It never writes Canon directly.**

Everything below is *how* Simulation reasons; none of it relaxes that rule.

### 15.1 The Two Questions, Restated

Simulation answers two questions — *"what does this decision do to the world?"* (the **Ripple**) and *"what does the world do on its own?"* (the **Tick**) — as operations of one temporal engine, with two directed modes that compose them across a horizon: **timespan-directed** and **intent-directed** simulation.

### 15.2 Timespan-Directed Simulation

The author gives a time window; the system advances the world through it.

- *"Simulate 300 years."* → the engine runs a sequence of Ticks across the horizon, at a chosen resolution, letting pressures accumulate, thresholds fire, and consequences propagate — producing a **timeline** of provisional state-transitions and events.
- *"Advance the succession crisis naturally."* → a bounded timespan simulation scoped to the objects and pressures around the crisis, run until the crisis reaches a stable resolution or the author's horizon ends.

Timespan-directed runs are **exploratory and provisional by construction**: they generate a candidate future the author reviews, not a committed one. The author can accept the whole timeline, accept a prefix of it, accept individual events, or discard it — each acceptance flows through the single gated path.

### 15.3 Intent-Directed Simulation

The author gives a desired end-state or trajectory; the system reasons out a coherent temporal path *to* it and recommends the timespan. It is **goal-conditioned temporal planning**: it plans a route through world-state space.

- *"Simulate until this empire collapses."* → the engine treats collapse as a target state, identifies the pressures and thresholds whose crossing would produce it, and proposes the shortest *causally honest* path — the chain of accumulating pressures, threshold crossings, and events that get there without violating canon or Foundation. It recommends a horizon.
- *"I want this civilization to become a maritime power."* → the engine works backward from the end-state to the enabling conditions, forward from the present to check feasibility, and proposes a path plus the pressures that would have to build.

**Where the end-state is not reachable without breaking canon, it says so and explains why.** This is the load-bearing sentence of the subsection and is stated as a rule rather than a behavior: **intent-directed simulation never fabricates a path that contradicts the world, and never silently relaxes a constraint to reach a target.** An unreachable intent returns *unreachable, and here is the constraint in the way* — which is information the author needs and which a system eager to satisfy intent will quietly destroy. It never asserts a route is the only one, and it never commits it; it proposes a path and a horizon, with alternatives and a counter-case (Section 21), for the author to gate.

### 15.4 The Temporal Primitives

Both directed modes are built from three temporal controls:

- **Horizon** — how far ahead the simulation reasons. Bounded explicitly (a span) or derived (intent-directed, until a target state is reached). No unbounded runs.
- **Resolution** — the granularity of a step: year, decade, generation, era. High resolution for volatile periods; low resolution for stable stretches. Resolution is chosen per segment, not globally.
- **Compression / Expansion** — the engine *compresses* stable periods and *expands* volatile ones. This keeps a 300-year run reviewable: the author sees a few dozen meaningful transitions, not three hundred annual reports. Compression is a reasoning economy and a token economy at once (P-14).

### 15.5 World Dynamics — How the World Moves

The world moves because its world-state carries **dynamics**, and Simulation reasons over them:

- **Pressure** — accumulating force pushing a value toward change, carried on pressure edges (Section 13.3). Pressures build over time.
- **Momentum** — a trend's tendency to continue once moving.
- **Inertia** — resistance to change. High-inertia structures (institutions, cultures, Foundation-adjacent facts) absorb pressure before they yield; they change late and hard.
- **Thresholds** — tipping points. When accumulated pressure exceeds a threshold against its inertia, a **state transition** fires: a war begins, an institution falls, a technology diffuses. A threshold crossing *is* an event, and it propagates.
- **Constraints** — the bounds within which all of this must stay: Foundation (Spine, law 4), Structural Canon, and any authored withholding (Section 14.5). Simulation may push a value to a threshold; it may never push the world past a constraint.

This gives the world causal honesty: things change *because pressure crossed a threshold against inertia*, not because a die was rolled. The author can read *why* a collapse happened, not merely *that* it did.

**Where world state lives, stated exactly (v0.5).** World state exists in two places and they are not interchangeable:

- **On the object** — a Record's own `world_state_fields` (Section 13.1): *this* character's standing, *this* organization's power, *this* location's condition. Scoped to one object, moved with that object, recorded in that object's History Record.
- **In WSV** — world-scale indicators that belong to no single object (Section 13.10): the state of an economy, a climate, a diffusion, a legitimacy. Recorded in WSV-H.

Both are Tier 4, both carry dynamics, both are advanced by Simulation and confirmed at light ceremony. The test for which: *does this quantity belong to a thing, or to the world?* A quantity recorded in both places is duplicated truth and is a Canon Health finding — see Section 15.16.

### 15.6 Causal Propagation and Delayed Consequences

When a state transition fires, its consequences propagate along **causal edges** — and crucially, some consequences are **delayed**. A decision now can seed a crisis decades later: a treaty signed in one era plants a pressure edge that only crosses its threshold two generations on. Simulation carries these delayed causal links forward across the horizon, so a 300-year run can surface a late crisis whose root the author set in motion at year 5. Delayed consequences are what make a simulated history feel *earned* rather than episodic. Every propagated consequence is provisional and enters the timeline for review.

### 15.7 Branching, Uncertainty, and Convergence

Where the future is genuinely open, Simulation does not pretend to certainty:

- **Branching** — at a threshold whose outcome is contested, the engine proposes **branches**, each with the conditions that select it and an honest, coarse likelihood (a qualitative *likely / plausible / unlikely* with its reasoning, never a false-precision number).
- **Uncertainty** — carried explicitly and surfaced, never hidden. A low-confidence transition is marked as such, with what would resolve it.
- **Convergence** — the engine identifies outcomes that *many branches share* — **robust futures** the world tends toward regardless of the coin-flips along the way. Convergence tells the author which developments are structurally inevitable (safe to plan around) versus contingent (a genuine choice point). Intent-directed simulation leans on convergence to find the most causally-robust path to a target.

### 15.8 The Timeline Graph

The output of any directed simulation is a **timeline graph**: provisional events and state-transitions across the horizon, linked by causal edges, branch points, and their pressures — a reviewable projection of a candidate future. It is a *view* (Derived truth), never canon, until the author gates parts of it. The author can accept the whole, accept a prefix, accept or reject individual transitions, or steer a branch and re-run. Accepted transitions become confirmed events that commit transactionally and propagate (Spine, law 8).

### 15.9 Ripple, Tick, and Event Chains

A **Ripple** is the immediate, single-step consequence of one confirmed decision — a horizon of zero. A **Tick** is one resolution-step of world-time. An **event chain** is what a directed run produces: a causally-linked sequence of threshold-fired events across the horizon. All three produce only provisional deltas; all three pass the gate; none self-commit.

### 15.10 Simulation as a Draft State

Exploration is not a separate engine. When the author explores "what would happen if…?", the proposal enters the **SIMULATION state of the Draft Lifecycle** (Section 18.5) and runs this same domain against it — producing a timeline the author sees without committing anything. There is no separate what-if simulator and no sandbox engine; there is a draft state that runs Simulation. This is where a world-first system earns its keep: the author sees a decision's consequences, across time, *before* making it.

### 15.11 What Simulation May Never Do

It may never write canon (only the gate does). It may never move a fact's reveal-state to REVEALED or close an arc on its own — those are authored moments (Section 14.2). It may never push the world past a Foundation or Structural constraint. It may never present a contested future as inevitable (it branches and states the counter-case). And it may never resolve deliberately-withheld negative space (Section 14.5) without the author. Simulation is the world's physics of change; authorship is still the author's.

### 15.12 Large-Scale Simulation and Evolutionary Traceability

A major run may, once gated, modify **thousands of Records** in a single accepted timeline. Scale of this kind is expected, not exceptional, and it is precisely where an unexplainable world is created quietly: not by one bad commit, but by ten thousand reasonable ones no one can afterwards account for.

The architecture must therefore support **monitoring, auditing, replay, inspection, and explainability at that scale — without bloating individual Records.** This is the load Canonical Evolution carries (Section 12.9): because history lives outside the object, a run touching five thousand objects leaves five thousand traceable evolutionary paths and no heavier world. Every transition accepted at the gate remains answerable to P-18 — what changed, when, why, who approved it, and *what caused it*, that last answer being the causal edge or threshold crossing the run walked.

### 15.13 Causal Closure of Acceptance

§15.8 permits the author to accept a prefix of a timeline, or individual transitions from it. Unconstrained, this produces canonical states whose recorded causes were never committed — a transition accepted while the threshold crossing that caused it was rejected. That is precisely the corruption P-18 exists to prevent, produced by the review mechanism the system most encourages.

**The rule: every acceptance is causally closed, or explicitly re-caused.**

At acceptance, the system computes the **causal closure** of the selected set: every transition in the timeline that the selection depends on. Three outcomes, and only three:

1. **Closed** — the selection already contains its antecedents. It commits.
2. **Closable** — the missing antecedents are identified and offered; the author accepts them too, and the set commits closed.
3. **Re-caused** — the author wants the consequence without its simulated cause. This is legitimate and common (*"the revolt happens, but not because of the famine"*), and it is handled honestly: the accepted transition is committed with an **authorial cause** (Section 5.2) replacing the simulated one, recorded as such in History Record. The world says *the author decided this*, which is true, rather than *the famine caused this*, which is now false.

**Rejected antecedents leave a trace.** A rejected transition whose dependents were accepted under re-causation is recorded in Creative Memory as a rejected branch with its reason (Section 22.1).

**Anti-pattern.** Accepting a set and letting propagation "figure out" the missing causes. Propagation walks relationships that exist; it does not invent the ones the author declined.

### 15.14 Basis Stamps, Aggregate Approval, and Review Load

- **Basis stamps (P-22).** A timeline records the canonical state it was computed against. A 300-year run reviewed across three sessions is re-validated against current canon at the gate; anything the run *read* that has since changed marks the affected transitions as **stale**, and stale transitions are re-reasoned or dropped, never committed on the old basis.
- **Aggregate approval (P-23).** Accepting a timeline is an aggregate act and carries the maximum severity of its members; it records its Scope of Approval; and it may not contain a Foundational change at all. A run that would touch Foundation stops before the gate and says so.
- **Bounded review load.** A run's review cost is estimated *before* it is offered (Section 8.2). A timeline exceeding the author's declared budget is segmented into reviewable stages at natural causal joints — branch points, era boundaries, threshold crossings — rather than presented whole and skimmed. **The system never reduces review load by reducing what the author is told; it reduces it by structuring what the author is asked.**

### 15.15 Determinism, Reproducibility, and Model-Independence

Simulation is executed by a reasoning substrate that is non-deterministic and will change repeatedly across a decade (P-15, P-20).

1. **A simulation is not reproducible, and the system never claims it is.** Two runs of the same intent will differ. This is a property of the instrument, not a defect.
2. **A record *is* reproducible.** Historical Replay walks committed history and returns identical results forever, because it reads rather than reasons. **Replaying history and re-running a simulation are never called the same thing.**
3. **No canonical guarantee depends on reproducibility.** Canon's validity rests on the gate and the record, not on the ability to regenerate the proposal that produced it. A run records its **reasoning provenance** — the substrate binding, the basis state, the intent, the constraints applied — so the *conditions* of a past proposal are explainable even though its output could not be regenerated. That is explanation, which P-18 requires; not reproduction, which nothing requires.

### 15.16 Simulation, WSV, and the No-Duplication Rule (v0.5)

Four systems in this blueprint can hold something that looks like state: a Record's world-state fields, WSV, an `EVENT`, and a simulation timeline. Without an explicit rule, the same truth ends up in more than one, they drift, and no reading of the world is authoritative. Section 13.12 assigns causality; this assigns *state*.

| Holds | Owner | Explicitly does not hold |
|---|---|---|
| A quantity belonging to one object | That object's `world_state_fields` | World-scale indicators |
| A quantity belonging to the world | **WSV** (Section 13.10) | Anything scoped to a single object |
| That a transition occurred, and when | **`EVENT`** | The value itself — an event does not carry state, it causes a change to it |
| A *candidate* future value | **The timeline graph** — Working truth, never canon until gated | Anything authoritative |

**Three rules follow.**

1. **A quantity has exactly one canonical home.** The same value recorded both on an object and in WSV is duplicated truth and is a Canon Health finding (Section 12.15), not a convenience.
2. **Simulation holds no state of its own.** It reads current state, proposes deltas, and holds those deltas in a timeline graph that is Working truth until gated. There is no simulation-side store that survives the gate. A "simulation state" that persists independently of canon is a second world, and Spine law 1 forbids it.
3. **A committed transition writes state and history in one transaction** (Section 12.6): the new value to its owner — the object's Record or WSV — and the transition to that owner's history — History Record or WSV-H. Neither without the other.

### 15.17 The Simulation Model Architecture (v0.6.1)

*(ADDED. Source: authorial decision. Architectural consequence: Simulation gains an internal structure; **no new domain and no new engine**. Implementation consequence: substantial. Migration: none.)*

v0.6's Simulation had the *physics* — pressure, momentum, inertia, thresholds, constraints, causal and pressure edges, branching, convergence, timeline graphs — and no *subject matter*. It could move a quantity through time without saying what kind of quantity it was or what governed it. That is sufficient for a world with a dozen indicators and insufficient for a civilization.

**A Simulation Model is a Registry definition, not a component.** This is the load-bearing sentence of the subsection. A model declares which indicators it governs, what depends on what, what rules or equations relate them, what transitions it can produce, and what constraints it must respect. It is an `R` partition object (Section 13.6), versioned and gated like any definition. **The Simulation domain executes models; it does not contain them.**

**A Simulation Model definition has a fixed structure (v0.6.3).** A model is a Registry object (`R`), versioned and gated. Its definition carries twenty-two components, and the reason to enumerate them is that a model missing any one of them is a model whose output cannot be explained:

| Component | Holds |
|---|---|
| **identity** | Stable Registry identity per the identity grammar (§13.9a) |
| **domain** | Which model family it belongs to |
| **purpose** | What question about the world it exists to answer |
| **indicators** | Which WSV indicators it reads and which it may propose changes to |
| **variables** | Internal quantities that are not world state and never reach WSV |
| **definitions** | What each internal term means within this model |
| **units** | Declared per indicator and per variable; a unitless quantity is a defect |
| **dependencies** | Which other models' outputs it consumes, declared not discovered (§15.18) |
| **equations / functions** | The relations among its quantities |
| **rules** | Discrete logic that equations cannot express |
| **thresholds** | The tipping points at which a transition fires |
| **constraints** | Bounds it may never violate — Foundation, Structural Canon, authored withholding |
| **transitions** | The state changes it can produce |
| **causal relationships** | Which of its outputs cause which effects, mapped to causal edges |
| **pressure relationships** | Which conditions accumulate toward which thresholds |
| **feedback loops** | Declared, with sign and expected damping — an undeclared loop is how a model becomes unstable in a way no one predicted |
| **temporal behaviour** | Resolution, lag, and how the model behaves under compression (§15.4) |
| **calibration** | What it has been validated against, and what that validation does *not* establish (§15.21) |
| **uncertainty** | Where its outputs are confident and where they are not |
| **assumptions** | What must be true for this model to be meaningful — the field most often omitted and most often needed |
| **WSV input mappings** | Indicator → model variable |
| **WSV output mappings** | Model variable → proposed indicator delta |
| **provenance** | Who authored it, when, why (§13) |

**The generic Model Contract is closed; the 37 family specifications are not.** The twenty-two components above **are** the contract, and it is frozen: any model of any family is expressed through it. What remains deliberately open is the *content* of each family — which indicators, which equations, which thresholds. **This is not 37 engines and never becomes 37 engines** (P-32); it is one contract instantiated 37 ways, and there is no Simulation partition.

**None of this lives in WSV.** WSV holds current values (§13.10). A model definition that has migrated into WSV has turned the state record into an encyclopaedia, and the separation at §13.10 exists precisely to prevent it.

**Realization (v0.6.3).** Model *execution* is supplied behind adapter A-6 by **Mesa** (`projectmesa/mesa`, Apache-2.0) — **ADAPT** — for agent-based families; **PySD** — **ADAPT/COMPOSE** — for system-dynamics families, at the cost of a dependency on its source model dialects; and **SimPy** (MIT) — **ADOPT** — for discrete-event families. Mesa's bundled visualization server is not used and must never become a second surface. **The components execute; they do not define.** Model *definitions* are Registry objects (above), and cross-model ordering, conflict resolution, and observability are native (§§15.18, 15.20). Output is a timeline graph — **TEMPORARY**, Working truth until gated. Degraded mode: the affected family cannot run, other families continue, and the run reports what it could not compute. Exit: definitions are Registry records; re-implement execution.

**Model families.** The inventory below is a taxonomy of *capabilities*, and it is deliberately long. Per P-32, **none of these is an engine, a domain, or a subsystem.** Thirty-seven families, grouped by what they are about:

```
SOCIETY AND POPULATION
├── Population                  size, structure, vital rates
├── Demography                  births, deaths, migration, cohorts
├── Households                  formation, dissolution, composition
├── Family                      kinship, dependency, inheritance
├── Social Structure            stratification, institutions, networks
├── Social Mobility             movement between strata, and its blockage
└── Class / Status              material position and perceived position

ECONOMY AND WORK
├── Economy                     production, prices, scarcity, trade
├── Labor                       employment, wages, skill, bargaining
├── Commerce                    markets, exchange, credit, supply
└── Consumer Life               what ordinary people buy, want, and cannot afford

POWER AND ORDER
├── Government                  administration, capacity, revenue
├── Politics                    power, legitimacy, faction, succession
├── Law / Justice               rules, enforcement, adjudication
├── Security                    policing, surveillance, control
├── Military / Conflict         tension, escalation, violence, settlement
└── Crime / Informal Economy    what happens outside the law, and who depends on it

PUBLIC SPHERE AND MEDIA
├── Public Sphere               (specified below)
├── Media                       (specified below)
├── Public Opinion              what is broadly believed, and how strongly
├── Information Diffusion       how a claim travels, and how fast
├── Propaganda                  deliberately shaped belief
└── Censorship                  deliberately suppressed belief

BELIEF AND KNOWLEDGE
├── Religion / Belief           practice, authority, schism
├── Education                   transmission, access, literacy
├── Science                     inquiry, consensus, revision
└── Technology                  capability, diffusion, obsolescence

LIFE AND CULTURE
├── Health                      morbidity, epidemic, care, mortality
├── Culture                     custom, taste, aesthetic change
├── Entertainment               leisure, performance, popular form
├── Language                    usage, drift, register, borrowing
└── Everyday Life               food, transport, habit, complaint, the ordinary residue (§11.3)

PLACE AND SYSTEM
├── Infrastructure              transport, communication, utilities
├── Urbanization / Settlement   density, growth, decay
├── Environment / Ecology       climate, land, yield, hazard
├── Resource Systems            extraction, depletion, allocation
└── Institutional Change        how institutions form, harden, and fail
```

**Everyday Life is in the list on purpose.** §11.3 requires ordinary residue for the publication to reveal the world indirectly, and §16.6 raises ordinary-life thinness as a finding. A simulation that models only the load-bearing systems will produce a world with nothing mundane in it, and the magazine will read as a briefing.

### 15.17a The Public Sphere, Specified (v0.6.3)

| Capability | Models |
|---|---|
| **Public opinion** | What is broadly believed, by whom, how strongly, and how it moves |
| **Discourse** | What is being argued, in what terms, and which terms are unsayable |
| **Attention** | The scarcest resource in any public sphere; what is being crowded out |
| **Rumour** | Low-evidence belief with wide reach and fast propagation |
| **Scandal** | The rapid conversion of belief into consequence |
| **Propaganda** | Deliberately shaped belief, with a shaper who has an interest |
| **Censorship** | Deliberately suppressed belief, and what the suppression reveals |
| **Misinformation** | Belief that is wrong without anyone intending it |
| **Petitions** | Formalized collective demand |
| **Protest** | Collective action, its triggers, and its suppression or success |
| **Civic reaction** | How a population responds to an event it did not choose |
| **Information cascades** | Where a small signal produces a disproportionate collective shift |

**Four boundaries, and each prevents a specific collapse.**

- **Public Sphere ≠ Reader Knowledge.** In-world belief is simulated; reader knowledge is reached only through published artifacts. Neither is derived from the other in either direction (**I-99**). This is the collapse most likely to happen by accident, because both are "what someone believes".
- **Public Sphere ≠ Belief.** A `BELIEF` record is an Epistemic state — *what a knower holds*. The Public Sphere models *how belief moves*. State and dynamic; committed result and process.
- **Public Sphere ≠ Media.** The media ecosystem is the set of institutions that carry claims; the public sphere is what happens to claims once carried. A publication can print something the public sphere ignores entirely, which is often the interesting case.
- **Public Sphere ≠ Politics.** Political models handle power, office, and policy; public sphere models handle belief and attention. They feed each other constantly and are not the same system.

### 15.17b The Media Ecosystem, Specified (v0.6.3)

| Capability | Models |
|---|---|
| **Publications** | Titles, format, cadence, market position |
| **Publishers** | Who prints, and what else they own |
| **Editors** | Who decides, and what they will not run |
| **Journalists** | Who writes, their access, their exposure |
| **Audiences** | Who reads, and what they expect |
| **Circulation** | Reach, distribution, geography |
| **Reputation** | What a publication is trusted for, and by whom |
| **Ownership** | Who holds it, and what that costs the coverage |
| **Editorial stance** | What it argues, and what it will not say |
| **Advertising** | Who pays, and what that constrains |
| **Competition** | Rivals, imitation, differentiation, market share |
| **Censorship** | External suppression, and the internal kind |
| **Influence** | What the publication actually changes, and what it only appears to |

**The Overtone exists inside this ecosystem, and its records are already partitioned for it (§17.16):** `W` the in-world institution · `P` the production and editorial operation · `I` the published issues · `V` the visual artifacts · `E` the public knowledge and perception of it. The ecosystem models supply what a publication needs in order to be an institution rather than a delivery mechanism — rivals it defines itself against, a market it is winning or losing, an owner whose interests cost it something, and a reputation it can spend.

**Why Public Sphere and Media are Simulation and not Epistemic.** Epistemic records *who knows what* — a state. These families model *how belief moves* — a dynamic. A rumour's spread is a simulated process whose committed result is an epistemic state, exactly as a famine is a simulated process whose committed result is a world-state value. The two are the same relationship at different subject matter.

**Why the Media Ecosystem matters more than its size suggests.** The Overtone is a publication inside a media landscape (Section 17.16). A magazine with no competitors, no rivals it defines itself against, and no market it is losing or winning is not an institution — it is a delivery mechanism. Modelling the ecosystem is what makes the publication's own choices legible as choices.

### 15.18 Cross-Model Feedback and Conflict Resolution (v0.6.1)

*(ADDED. The reason a model architecture is worth having at all.)*

Models that cannot feed each other are separate simulations sharing a clock. The architecture requires chains that cross families:

```
Environment → Agriculture → Food Prices → Household Stress → Public Opinion → Political Pressure
```

Every arrow is a **dependency declared in the model definitions**, not an ad-hoc coupling written into an implementation. The chain above is walkable, and therefore explainable, because each link is a declared dependency between two indicator sets.

**Model conflict is expected and must be resolved by rule, not by ordering accident.** Three models will routinely propose opposite movements of the same indicator:

```
Economic Model     → inflation ↑
Political Model    → policy → inflation ↓
Environment Model  → food shortage → inflation ↑
```

The architecture requires each of the following to be **declared**, not discovered at run time: **dependency** (which model's output is another's input) · **ordering** (what resolves first where dependency does not settle it) · **coupling** (whether models interact per step or per run) · **convergence** (how iteration terminates, and what happens if it does not) · **precedence** (which model governs an indicator where genuine conflict remains).

**Unresolved model conflict is a finding, not an average.** Where the declared rules do not settle a conflict, Simulation **stops and reports the conflict with its contributing chains** rather than blending the proposals into a number no model actually predicted. An averaged result that no model produced is the simulation equivalent of an unadjudicated CONTESTED fact (Section 12.2), and it is handled the same way — surfaced, never silently arbitrated.

### 15.19 The Cross-Model Causal Graph (v0.6.1)

The declared dependencies across all active models form a single traversable graph. It is a **projection** (Derived, Section 12.11) and it is what makes the rest of this section auditable rather than aspirational: it is how the system answers *what does climate actually reach?* before a run, and *what actually reached this?* after one.

**Realization (v0.6.3).** Traversal is supplied by **NetworkX** (BSD-3-Clause) — **ADOPT** — behind adapter A-5, operating on a graph **rebuilt from Relationship Record and Registry model definitions**. **rustworkx** (Apache-2.0) is the benchmark-gated alternative where traversal performance demands it. **Embedded graph databases are REJECTED as edge stores** (AC-1): an edge store would hold relationship authority, inverting §13.9. The graph is **DERIVED** and rebuildable; the edges live in Relationship Record and nowhere else.

Its consumers are named (P-10): conflict detection (§15.18), observability (§15.20), sensitivity analysis (§15.21), and Preflight Impact Prediction (§8.2).

### 15.20 Simulation Observability (v0.6.1)

*(ADDED. The requirement that makes simulated history explainable rather than merely produced.)*

> **For every committed WSV transition, the system must be able to answer: this indicator moved from X to Y — *why?* — and return the model, the dependency, the driver, and the causal chain.**

This is P-18 applied to simulation output. A transition whose chain cannot be produced is not a mysterious result to be investigated later; it is a **P-18 failure at the moment of commit**, and the commit does not proceed (Section 13.12, rule 2). The chain is recorded in WSV-H as part of the entry's `cause`, and the Cross-Model Causal Graph is what makes it walkable afterwards.

**Why this is stricter than it sounds.** A 300-year run produces thousands of transitions. Requiring every one to carry its chain is what stops a large run from becoming an unexplainable world produced by ten thousand individually reasonable steps — the exact failure §15.12 was written to prevent, now enforced at the level of the individual value rather than the accepted timeline.

### 15.21 Calibration, Sensitivity, and Stability (v0.6.1)

*(ADDED. Three capability families, and — per P-32 — **not three engines.**)*

**Calibration.** A model is validated against known historical patterns where appropriate, authored test worlds, synthetic scenarios, edge cases, threshold tests, and conservation or constraint tests. **The warning attached to this capability is the important part: real-world calibration does not establish fictional-world correctness.** A model tuned until it reproduces a real economy is a model tuned to a world that is not this one. Real-world fit is *evidence about the model's internal coherence*, never authority over the world's behaviour, and a calibration finding never overrides an authored world fact.

**Sensitivity and stability.** Sensitivity analysis · parameter sweeps · threshold stress tests · instability detection · runaway feedback detection · oscillation detection · convergence checking. These exist because a coupled model architecture can be individually plausible and collectively unstable, and the author needs to know that *before* a 300-year run rather than by reading its output.

**Realization (v0.6.3).** Sensitivity and sweep numerics are supplied by **SALib** (`SALib/SALib`, MIT) — **ADOPT**, behind the sensitivity adapter (A-7). Input: a model plus parameter ranges. Output: sensitivity indices and stability findings, classified **DERIVED** and advisory. SALib supplies the *methods*; it does not supply which findings matter, and it may never override an authored world fact (I-94). Degraded mode: findings unavailable, runs proceed unadvised. Exit: findings are records; swap the method library. Version policy: pin the minor; re-verify licence at adoption.

**All of it is advisory.** Calibration and stability findings are **judged** (P-24): they inform the author and never block a run, because a world is permitted to behave in ways a model finds surprising. What they may not do is pass silently.


### 15.22 The Simulation → WSV Commit Path (v0.6.3)

*(CLARIFIED. The path was implicit across §§12.6, 13.12, 15.16 and 15.20; stating it once in one place removes the possibility of an implementation assembling it wrongly from three.)*

```
Current Canon / WSV
        ↓                    read — never held, never cached as a second world
Simulation Models  (R)
        ↓                    definitions, not code paths; executed, not contained
Simulation Run
        ↓                    produces a timeline graph — Working truth
Candidate State Deltas
        ↓                    proposals, each carrying its basis stamp (P-22)
Validation
        ↓                    structural checks block; judged findings surface
Human Gate as required
        ↓                    the author decides; nothing self-commits
Mutation Coordinator
        ↓                    the single canonical write boundary (§12.6)
WSV′
        ↓                    new current values
WSV-H
                             the committed transitions, each naming model,
                             dependency, driver, and causal chain (§15.20)
```

**The tick is atomic.** One tick commits everything it produces, or nothing:

```
Read current Canon / WSV
        ↓
Run applicable Simulation Models
        ↓
Produce candidate state changes
        ↓
Validate
        ↓
Commit valid changes ATOMICALLY
        ├── Record changes
        ├── Relationship Record changes
        ├── WSV changes
        └── other governed canonical changes
        ↓
Write history
        ├── affected History Record entries
        └── ONE WSV-H entry for the tick
        ↓
Refresh derived projections
```

**Three histories, never merged.** **History Record** is the history of Record changes. **WSV-H** is the history of world-state transitions. **Version control** is the history of the repository's files (§26.2e). They answer three different questions and a system that merges any two of them has lost the ability to answer at least one.

**The rule this path exists to enforce:** *simulation never maintains a competing persistent canonical world state.* A run reads current state, computes candidates, and holds them in a timeline graph that is Working truth until gated. **Nothing simulation-side survives the gate.** A persistent simulation state that outlives a run is a second world, and Spine law 1 forbids it (I-79).

**Three checks along the path.** A delta with **no basis stamp** cannot be validated and does not proceed (P-22). A delta whose **causal antecedents were rejected** must be explicitly re-caused with an authorial cause or dropped (§15.13). A transition that **cannot name its causal chain** does not commit at all (I-92) — not deferred, not committed-with-a-note.


---

## 16. Emergence Architecture

Emergence closes the gap between *a world that has moved* and *an author who needs something to make*. It enforces *Emergence Before Artifact*: material is discovered before it is planned.

### 16.1 What Emergence Does

Emergence reads the simulated, canonical world — recent Ripples, accumulated Tick pressures, the events of a gated timeline, open questions, active threads — by walking the dependency graph, and **discovers** the material the world now contains: events worth telling, tensions between factions or systems, openings for a cover or a reveal, unknowns the new world-state has raised, thematic evolution, and concrete plantable seeds. It does not invent; it surfaces. After a long simulated span, Emergence is especially valuable: a 300-year run produces far more material than any single issue needs, and Emergence is what ranks it.

### 16.2 The Opportunity Queue

Discoveries land in the **Opportunity queue** — a living, prioritized list of what the world is *offering*. Each entry carries what it is, where in canon it came from (traceable through the graph), which unknowns/threads/arcs it touches, its urgency, and how long it stays fresh. The queue is the author's answer to *"what should I make next?"* — not because the system decided, but because the world produced it. Editorial (Section 17) reads this queue to decide what is told and when.

### 16.3 Emergence Is Manifestation-Blind

A tension between two lineages is a story seed whether it becomes a magazine cover, a game questline, or a podcast episode. Emergence discovers *world material*; Editorial decides *what medium it becomes*. This separation is what lets one universe feed a magazine and a game without the discovery logic knowing the difference. Emergent seeds are Working truth — candidates, never canon — until the author acts on them through the gate.

### 16.4 Reality Derivation — The Discovery End of the Anchor Pipeline (v0.5)

Reality Derivation is where a real-world pattern is *noticed*; Reality Anchoring (Section 11.1) is where the resulting counterpart becomes canon. v0.4 described the first without the second, which left the pipeline with a beginning and no recorded end. The two are now one pipeline with a partition boundary in the middle, and this subsection owns only the ascending half.

When the author engages it, a real-world pattern is **observed**, its **structural shape extracted**, all real-world **specifics stripped**, the shape **translated** into the world's own terms, and its **resonance** checked against active unknowns and threads via the graph. The output is an Opportunity queue entry like any other — a candidate, never canon.

Four properties, unchanged: only structure crosses over; **nothing becomes canon automatically**; it is bounded per cycle; and it is **off unless the author turns it on**. *Reality inspires; it never replaces.*

**The handoff to Section 11.1.** If the author acts on a derived opportunity, the resulting record is created through the ordinary gate as a **Reality Anchor**: the counterpart is an ordinary Record, the real-world source is recorded as authoring provenance rather than as a world fact, and the **transformation field is mandatory and structurally checked** (P-29). Reality Derivation may therefore *propose* freely; what it may never do is deliver a real-world specific into the World partition, because the anchor record is where a specific would have to be declared and the linter blocks an anchor that has nothing to declare.

### 16.5 The Opportunity Queue Is Production State

The queue's *contents* are discovered from canon and are therefore Derived — rebuildable, disposable, recomputed whenever the world moves. Its **dispositions are authored** and are therefore **Production State** (Section 9.1, P-26): what the author dismissed and why, what they deferred and until when, what they promoted into a plan, what they marked as never-this. Filing those as Derived means the first queue rebuild silently discards years of authorial judgment and re-offers every idea the author has already declined — which is not a data-loss bug so much as an insult delivered repeatedly.

So: **discoveries are Derived; dispositions are durable.** Every disposition records what, when (authoring sequence, P-21), why, and by whom — and dismissal reasons feed recommendation calibration (Section 32), so declining an idea teaches the staff instead of merely removing a row.

### 16.6 The Narrative Coverage Map

A projection over canon and the Evidence Graph showing, per region of the world, **how much of it has ever reached a reader** — and at what depth. It answers the question a decade-long world eventually poses and cannot otherwise answer: *what have I built and never used?* Its findings:

- **Dark regions** — canon rich in structure, never manifested. Pure opportunity.
- **Thin regions** — frequently referenced, structurally shallow. Development debt, and a contradiction risk because thin canon gets improvised over.
- **Saturated regions** — heavily used; further material there risks repetition (Section 19.5).
- **Ordinary-life thinness (v0.5)** — a region whose canon is *entirely* load-bearing: every fact plot-critical, nothing mundane. This is a finding rather than a virtue. A world with no ordinary residue cannot be revealed indirectly (Section 11.3), because there is nothing to reveal it *through* — every artifact must then carry plot, and a magazine in which every page carries plot reads as a briefing rather than a publication. The finding names the region and the kind of ordinary material it lacks: commerce, food, transport, entertainment, complaint, habit.

Derived, ascending, named consumer: Emergence ranking and Editorial selection.

### 16.7 Opportunity Derivation and Freshness

Opportunities derive from **structural conditions in canon**, not from prose impression, and each records the condition that produced it so the author can see *why the world is offering this*: an unresolved pressure near a threshold; a relationship contradiction; a reveal-readiness that has matured (Section 14.13); a knowledge divergence approaching its designed resolution point; a dark or ordinary-thin region adjacent to an active arc; narrative or knowledge debt approaching mandatory. **Freshness** is a property of the condition, not of the row: an opportunity whose generating condition no longer holds is retired automatically, with its disposition history retained. A queue that only grows is a queue nobody reads.

### 16.8 Pseudo-Science Governance (v0.5)

The world may bend real science (Section 11.5). Without governance, a bent science degrades in one of two directions: toward incoherence, where the rules change to suit each story, or toward mere relabeling, where real physics wears a costume. This subsection governs the deviation. **Classification:** capability, owned by Emergence, applied by Editorial. **Current:** the derivation is ascending; the resulting canon is descending like anything else.

**The pipeline:**

```
REAL SCIENTIFIC BASIS      recorded as authoring provenance, never as a world fact
        ↓
CONTROLLED DEVIATION       exactly what was changed, stated as a rule rather than
                           an effect — "signals propagate through X, not through Y"
        ↓
FICTIONAL THEORY           a CONCEPT record. What the world's researchers currently hold.
        ↓
IN-UNIVERSE MODELS         the systems built on the theory — technologies, institutions,
                           practices. Ordinary Records.
        ↓
COMPETING INTERPRETATIONS  rival CONCEPTs, with their holders. Epistemic (Section 14).
        ↓
EVIDENCE                   world evidence accumulating for and against (Section 14.7)
        ↓
REVISION                   the theory is revised, superseded, or defended — a gated act
        ↓
CONSEQUENCES               ordinary propagation (Spine, law 8)
```

**Three rules.**

1. **A deviation is a constraint, not a permission.** The recorded deviation states what is *now impossible* as well as what is now possible. A deviation that only adds capability has no stakes, and a fictional science with no impossibilities cannot generate a plot — every problem dissolves. A deviation record with no stated limit is a Governance finding.
2. **Authorial truth and in-universe belief are separate records, always.** What is actually the case is a World record; what the world's researchers think is the case is Epistemic. **The interesting configuration is divergence** — a working theory that is wrong in a way that has consequences — and it is unreachable if the two collapse into one record. This is Section 14.19's rule applied to science specifically.
3. **Consequences propagate or the deviation is decorative.** A bent science that changes no institution, no economy, no practice, and no career has not been integrated into the world; it has been announced. Emergence surfaces this as a coverage finding (Section 16.6): a `CONCEPT` at Foundation or Structural tier with no downstream dependents is either new or ornamental, and the author is told which it looks like.

**What this subsection does not do.** It does not check that the fictional science is *good*. Internal coherence across a body of fictional theory is a judged property (P-24), evaluated at Governance (Section 19), and is the author's to adjudicate — the system can find an unstated limit and an undeveloped consequence, and it cannot find an idea that is merely uninspired.

### 16.9 Research Intelligence (v0.6.1)

*(ADDED as an **Emergence capability**. Off by default, like Reality Derivation, and for the same reason.)*

Formalises external research the author already does by hand: historical · cultural · scientific · publication · trend · visual-reference · contemporary-material research, and source comparison.

**Every output is an Opportunity queue entry** (§16.2) — a candidate, never canon. Research reaches the World partition only through a Reality Anchor with a recorded, non-empty transformation (§11.1, P-29), and reaches Production as taste evidence (§17.17). **Research findings are `EXTERNAL` in the source-of-truth classification** (§29.6a).

### 16.10 Trend Detection and Cultural Resonance (v0.6.1)

**Trend detection** runs the anchor pipeline on live cultural material:

```
real-world trend → analysis → candidate pattern → transformation → in-universe trend
```

An in-universe trend has its own carriers, causes, and arc, and **will diverge** — one that tracks its real counterpart move for move has been copied, not anchored (§11.1).

**Cultural resonance analysis** is the judged evaluation P-29 always needed and §19.11 could only assert. It classifies an anchor or an editorial reference as: **too literal** · **too derivative** · **too generic** · **culturally recognizable** · **strangely familiar** · **transformed effectively**. Only the last two are targets. It applies to Reality Anchors and editorial references alike, and it feeds the Resonance Standard (§19.11).

**Humour and pop-culture analysis** handles the layered case:

```
surface joke → cultural reference → world implication → deep lore connection
```

A joke that works only at the surface is thin; one that works at all four layers is the format at its best (§17.15). The capability distinguishes **transformed resonance** from **overly literal copying or parody**, and parody drift is already a named finding (§19.11).


---

## 17. Editorial Architecture

*(Record System note, v0.7.0: where this section produces durable records, they belong to the **Production Record Model** — a sovereign Record Model (§13, I-101), never World truth by any route (§13.6b), and never a mere state of a universal object. Production field sets remain **OPEN** (§13.6b).)*

Editorial is the newsroom — the system's **narrative decision layer**. It is the domain that answers one question:

> **"Given the world material, what should be told, in what form, and at what time — and why now?"**

Editorial reports on a world that already moved (Simulation, Emergence) and hands finished plans to the Creative Studio (production). It reads canon and the Opportunity queue; it never rewrites canon.

**One thing Editorial must be able to decide, stated here because the rest of the section assumes it (v0.5):** that a piece of material is worth publishing *because it shows what the society is like*, and for no other reason. An advertisement, a recipe, a complaint letter, a review of a bad concert — these carry no plot and are not premature, thin, or off-mission. They are the mechanism by which the Artifact Principle (Section 5.3) is actually executed. A selection layer that can only rank material by its narrative load will starve the publication of everything that makes it read like a publication.

### 17.1 Story Selection and Readiness

Not everything the world produces is ready to tell. Editorial evaluates each candidate from the Opportunity queue for **narrative readiness**: is there enough clued material (Section 14.3) for a reveal to land? Does the reader knowledge-state (Section 14.4) support this beat now, or would it confuse the casual tier or bore the investigator? Is the emotional and thematic groundwork laid? A candidate can be *canonically true and available* yet *narratively premature* — and Editorial's job is to tell the difference, selecting what is ripe and parking what is not.

**Readiness applies to load-bearing material only.** Ordinary-life material has no readiness gate, because it makes no promise and opens no question. It is selected on a different axis entirely: does it reveal something about the society, and does the issue need texture here? Applying reveal-readiness to a fashion column is a category error that produces a magazine with nothing in it but plot.

### 17.2 Event-to-Story Transformation

A world-event is not yet a story. Editorial decides what **form** an event should take: a full issue, a single cover, a hidden fact to be seeded, a character piece, an in-world timeline, a map, a document — or another manifestation entirely. The same collapse of an empire might become a cover this month, a five-issue arc next year, and a background fact in a third medium. The transformation is a decision with reasons, recorded, not a default.

**The oblique transformation is a first-class option and usually the better one (v0.5).** An event may be told by depicting its *residue* rather than the event: a shipping notice that reveals a blockade, an obituary that reveals a purge, a change in what a magazine no longer prints. Section 8.5's rule applies here concretely — the artifact derives from Society and Epistemic Distribution, not from Canon. An event that has only ever been told directly is a Governance finding (Section 19.11), not because directness is forbidden but because a publication that only reports is not a publication anyone in the world would read.

### 17.3 Timing Logic and Narrative Debt

Editorial owns *when*. It reasons about pacing — the rhythm of revelation and rest — and about **narrative debt**: the payoffs the readership is owed for what has been planted. Debt accrues when a clue is planted, a hidden fact advanced, or a thread raised; it is redeemed when a payoff lands. Editorial tracks debt per arc and per tier, escalates overdue payoffs through a flag system until a payoff becomes **mandatory** in the next issue, and schedules foreshadowing so future payoffs will feel earned. Timing logic is where the clue economy (Section 14.3) meets the calendar.

### 17.4 Arc Mechanics

A multi-issue story is a first-class **Arc** object with a **type** (institutional, revelation-culmination, character, signal/event, historical-transition, thematic), a **lifecycle** (seeded → active → building → climax-ready → resolved → closed), a **pacing** (sprint / medium / slow-burn), a **payoff schedule** (what each tier receives, how often), and a **progression score** (author awareness, never an autonomous trigger). All of an arc's hidden facts, threads, characters, and themes are linked as graph edges, so Editorial can see at a glance what a beat will touch.

### 17.5 Saturation Control

Reader attention is finite. Editorial caps the number of arcs simultaneously in the *building* state; beyond the cap, the author must advance one to climax, deliberately pause one, or hold off opening a new one. This prevents the arc-noise that destroys long-form series, and it is enforced as a finding, not a lock: the author may override with a recorded reason.

### 17.6 Medium and Form Selection

Because the core is manifestation-blind, Editorial is where *medium* first enters. It selects the medium-appropriate form for a piece of world-material — what belongs on a cover versus in a longform feature versus in a game — and passes that decision, with its reasons, to the Studio. Publication strategy (the long shape of the run: cadence, medium mix, what next) lives here too.

### 17.7 The Publishing Firewall in Editorial

Editorial is where the Publishing Firewall (Spine, law 5) is exercised. Every planned article carries an **Editorial Truth Classification** — verified reporting, ordinary reporting, editorial opinion, disputed claim, or in-world propaganda — marking its epistemic status *within the world*. This is not a claim about canonical truth; it is a claim about how the in-world publication presents it. The magazine may be partial, mistaken, or deliberately misleading in-world — design space, not corruption — because *that the magazine printed X* and *whether X is true* stay permanently separate.

**The full space this opens, stated so no downstream capability treats it as an edge case.** A publication in this system may be wrong, biased, propagandistic, credulous, sensational, or deliberately deceptive; it may repeat a rumour, misunderstand a science, misread a history, or reveal a truth partially and by accident. Each of these produces an **authored misconception** (Section 14.9) in whichever knowers received it — which is a designed asset. What is forbidden is the reverse direction: a published claim moving canon. **Canon Truth ≠ Published Claim**, in both directions and permanently.

### 17.7.1 The Three Planes of Publication

Publication is not one event and must never be classified as one. Every act of publishing has up to three planes, and each plane has its own owner, its own trigger, and its own consequence:

| Plane | What it is | Owner | Trigger | Consequence |
|---|---|---|---|---|
| **The artifact and its production** | The issue, cover, or page itself, and the work that made it | **Production State** (Sections 13.6, 18.7) | Studio production | Immutable once published; carries its canon basis (Section 20.5) |
| **Publication history** | That *this* artifact shipped, at what issue ordinal, on what date, and against which canon basis | **Production State** (Section 20.4). *The date is production metadata; the issue ordinal is the canonical epistemic axis (Section 12.16).* | The act of shipping | None on canon, none on the world; the record of the work |
| **The in-world publication act** | That, *inside the fiction*, this publication occurred — the magazine was printed and circulated | **Canon**, World partition — an `EVENT` (Section 13.6) | **A gated canon proposal, never the act of shipping** | A world event with world evidence (Section 14.7): those with in-world reach may come to know what it carried |

**When each plane applies.** The first two apply to **every** published artifact, always. The third applies **only when the artifact exists inside the fiction**, and even then **only when the author proposes it**. For The Overtone — an in-world publication — the in-world act is proposed as a step of the issue's publication workflow (Section 31) and is ordinarily a Trivial- or Standard-severity commit. For an artifact with **no in-world counterpart** the third plane simply does not exist. **Publishing never creates a world fact by itself; the author proposes one, or there is none.**

**What each plane does to knowledge.** Publication history does nothing to anyone's knowledge. The artifact produces **reader evidence** and therefore a Reader Knowledge Proposal (Section 20.4). The in-world act produces **world evidence** and therefore in-world knowledge changes, proposed as canon like any other world consequence. These are three different consequences of one act and are never derived from one another.

### 17.8 Editorial State Is Production State

Everything Editorial owns — arcs, payoff schedules, debt ledgers, publication strategy, saturation state, selection dispositions, the issue plan, the department roster — is **Production State** (Section 9.1). It is authored, durable, provenanced, and never rebuilt; and it is explicitly **not canon about the world**. An arc is a plan for telling, not a fact of the universe; the events it plans to tell are canon, the plan is not.

Two consequences, both practical. Editorial state changes at **production ceremony** — recorded, reasoned, reversible by ordinary authorial act — rather than at canon ceremony, so planning stays light while truth stays heavy. And deleting Editorial state costs the *plan*, never the *world*.

### 17.9 Temporal Axis Tagging in Editorial

Editorial is where the axes meet, and it is where confusing them does the most damage. Every editorial artifact declares its axes explicitly: an issue has an **issue ordinal** and a publication date; the material it covers has a **world-time**; the decisions about it have an **authoring sequence** and a session. The mapping between them — *issue 14 covers world-year 902* — is a **recorded production fact**, never an inference.

**Pacing reasoning must name its axis.** "Slow-burn" over twelve issues (issue ordinal) is not "slow-burn" over three centuries (world-time), and a system that blurs them will pace a century like a season. This is the single most common editorial error the axes exist to prevent.

**The correction carried from v0.5, completed in v0.6.** v0.4 required four frame stamps on every editorial artifact, one of which — publication-time — nothing canonical ever ordered by; v0.6 additionally recognises the issue ordinal as a sequence owned by the Issue partition rather than a temporal axis (Section 12.16). An issue's **date** is now production metadata on its publication record, carried because it is genuinely useful to a human reading the archive and because a real calendar constrains real production, but no epistemic or canonical reasoning resolves against it. Everything that used to order by publication-time orders by issue ordinal (Section 12.16).

### 17.10 Debt Lifecycle and Write-Off

Narrative debt (§17.3) and knowledge debt (§14.14) accrue automatically and previously had no exit but redemption — which means a decade accumulates permanent obligations to abandoned arcs and retired tiers. The lifecycle has five states: **accrued** (planted) → **escalating** (aging past its window) → **mandatory** (must be addressed in the next issue) → **redeemed** (payoff delivered) or **written off**.

**Write-off is an authored act, never an expiry.** It records what was owed, to which tier, why it will not be paid — *arc abandoned, thread superseded, retconned out, deliberately left open as designed ambiguity* — and whether readers were ever told. Written-off debt remains visible in history and appears once in the return briefing (Section 28.2). **Arc abandonment** is the same act at arc scale: an arc may be closed as *resolved*, *superseded*, or *abandoned*, and abandonment discharges its dependent debt explicitly, with its evidence and open questions dispositioned (Section 14.12).

### 17.11 Publication Timing as First-Class Mechanics

Cadence, slot, sequence, and lead time are production mechanics, and treating them as scheduling trivia is how a plan becomes undeliverable. Editorial holds: the **publication calendar** (what ships when — a Production record), the **issue plan** (what each slot must establish, redeem, plant, and reinforce), **lead-time constraints** from the Studio (Section 18), and the **commitment horizon** — how far ahead the plan is fixed versus provisional. Debt escalation, knowledge forecasts (§14.15), and reveal windows all resolve against **issue ordinal**, which is what makes "overdue" a computable fact rather than a feeling.

### 17.12 The Issue as a Structured Artifact (v0.5, re-partitioned v0.6)

v0.4 treated an issue as a unit of publication and said nothing about its interior. That was tolerable while the magazine was a lens on canon; it is not tolerable now that the magazine is the product. An issue with no internal structure is planned as a list of articles, and a list of articles is not a magazine.

**An issue is an Issue-partition record with an ordered interior.** *(RESTRICTED in v0.6 — the structure is unchanged; what changed is which partition holds it. v0.5 filed the artifact under Production, next to the plan that produced it; Section 13.6a separates them, because a plan may still change and a published artifact may not.)* Its structure, from largest to smallest:

| Level | What it is | Notes |
|---|---|---|
| **Publication** | The Overtone itself — a continuous institution with a history, a masthead, and a voice | Distinct from any one issue. Also an in-world `ORGANIZATION` (Section 13.6) — the two are separate records on separate planes. |
| **Issue** | One bounded, numbered, dated publication event | Carries issue ordinal, date, cover, theme-or-not, and its department allocation |
| **Department** | A recurring editorial category — the standing furniture of the magazine | See below |
| **Piece** | One article, column, review, interview, brief, advertisement, classified, or visual essay | The unit Editorial selects and Studio produces |
| **Spread / Page** | The physical unit the reader turns | Owned by Studio (Section 18.9); Editorial specifies extent, not layout |

**Where the boundary falls.** The *department roster*, the *issue plan*, and the *decision* to run a piece are Production — they are what the author is preparing. The *issue as published*, with its sections, articles, pages, advertisements, and visual assets, is Issue. The plan is how the artifact came to exist; the artifact is what a reader holds. Editorial owns both decisions and stores them on opposite sides of a line.

**The Issue hierarchy is frozen at exactly this level, and no deeper:**

```
I — Issue
├── Issue Identity
├── Editorial Context
├── Departments
├── Articles / Pieces
├── Pages / Spreads
├── Ads
├── Visual Assets
└── Publication Metadata
```

**Production owns editorial and production planning; Issue owns the published artifact.** Records referenced by an issue do not become Issue-owned (I-81). Field sets beneath this hierarchy are Production and Issue implementation work — **the schema is deliberately not over-frozen**, because an issue's interior is where editorial practice will teach the most and a premature freeze would cost that.

**Departments are the structuring concept, and they do the indirect-lore work.** A department is a standing commitment to cover a *kind* of thing every issue, which is what forces the publication to keep reporting on ordinary life even when the plot is elsewhere — a fashion page must run whether or not the empire is falling, and what it runs *while* the empire is falling is precisely the oblique signal (Section 8.5). The department *roster* is Production State, added and retired by production ceremony; a department *as it appears in a published issue* is an Issue record.

**A Department is a stable editorial identity. Frozen at the architectural level.** A department is a standing commitment the publication makes to cover a *kind* of thing, and it persists across issues.

**Topic, theme, subject, and genre are metadata and do not create a department.** An issue heavy with drought coverage does not thereby acquire a Drought department; it has a fashion page, a review section, and classifieds that happen to be full of drought. This is the distinction that stops the roster from growing one entry per interesting month.

**The roster itself is Registry content, not architecture**, and is completed during Production and Issue implementation. Freezing an arbitrarily large roster now would fix editorial decisions that have not been made. What is frozen is the *rule*: a department has a stable identity, appears across issues, and is added or retired by production ceremony.

**Advertising is a department, not a decoration.** An advertisement is the highest-yield indirect artifact the format offers: it asserts nothing about the plot, is trusted by no one, and reveals an economy, a technology level, a class structure, a set of anxieties, and a vocabulary in half a page. Ads are planned, selected, and evaluated like any other piece, and an issue with no commercial culture in it is a magazine nobody in that world was paying for.

### 17.13 The Publication as a Living Institution (v0.5)

The Overtone must be able to behave like a magazine that has existed for a while, which means it accumulates properties no single issue can express.

- **Recurring columns and editorial personalities.** A column is a standing piece with a persistent author-persona (`PERSONA`, Production; and where the writer exists in the world, a `CHARACTER`, World — two records, two planes, never merged). A persona has a register, habits, blind spots, and opinions that can be *wrong*, which is what makes a column readable and what makes it a vehicle for authored misconception (Section 14.9).
- **Institutional vocabulary.** A publication develops its own words — house style, recurring epithets, in-jokes, the phrase it always uses for a thing. This is a `STYLE-GUIDE` (Production) and accretes deliberately; a reader who recognises the vocabulary is a reader who has been reading.
- **Visual tradition.** Recurring formats, a masthead that changes rarely and meaningfully, a column that always looks the same way. Owned by Studio (Section 18.9–18.10), specified as Production.
- **Institutional history.** The magazine has a past: former editors, a change of ownership, an issue it is embarrassed about, a period when it was censored or captured. This is **canon** — the publication is an `ORGANIZATION` in the world with an ordinary history — and it is one of the richest indirect-lore surfaces available, because a magazine's institutional history is a compressed history of the society that permitted it.
- **Reaction and topicality.** The publication responds to world events, reflects trends (Section 11.1), makes jokes, and prints things that turn out to be wrong. Its reaction time and its blind spots are characterisation.

**The rule this section exists to state:** *not every page is lore delivery.* A magazine designed so that every item carries plot has no institutional life, and a publication with no institutional life is a delivery mechanism wearing a cover. Governance evaluates this directly (Section 19.11).

### 17.14 Archival and Period Issues (v0.5)

The publication may run issues set in other periods — a reconstructed issue from 200 BC, from 938, from 1945, from a future the current run has not reached. These are legitimate first-class editorial forms, and they are among the most efficient lore surfaces available, because a period issue reveals a whole era's assumptions in its *format* before it says anything at all.

**Four constraints.**

1. **A period issue is an artifact of its period, not a modern issue with an old date.** Its format, departments, register, typography, subject matter, prejudices, and blind spots belong to that period. A period issue that reads like the current issue has spent its entire budget and bought nothing.
2. **Its epistemic state is the period's, not ours.** What it knows, believes, and gets wrong is what a publication *then* would have known — which is usually far less, and wrong in specific, recoverable ways. This makes period issues a natural home for authored misconception (Section 14.9) and for historical divergence surfacing as memory (Section 11.2).
3. **Issue-index and world-time diverge sharply, and both are declared** (Section 17.9). A period issue published at issue ordinal 40 may cover world-year −200. The reader-knowledge effect is measured at issue ordinal 40 — the readers who receive it are today's readers — while the in-world content sits in its own world-time. Conflating the two is the specific error this form invites.
4. **The in-world publication act, if proposed, is dated in world-time.** *That a publication existed in 938 and printed this* is a world fact of 938, gated like any other (Section 17.7.1). Whether the in-world Overtone is the same institution across that span, a predecessor, or an unrelated publication the modern one is pastiching, is an authorial choice with real consequences for §17.13's institutional history.

### 17.15 Layered Discoverability (v0.5)

The product serves several reader depths at once, and the architecture must make that a design property rather than an accident of density.

| Depth | Receives | Owed |
|---|---|---|
| **Casual** | Surface meaning. A complete, satisfying read with no prior knowledge. | Must never be *required* to notice anything. |
| **Interested** | Secondary references, recurring names, the sense that things connect. | Rewarded for attention, not required to sustain it. |
| **Lore** | Deeper connections across issues; the evidence chains. | Enough to assemble real answers (Section 14.13). |
| **Obsessive** | Rabbit holes, hidden continuity, the things planted years ago. | Real ore, occasionally; never validated nonsense (Section 14.12). |

**The rule: complexity is discoverable, never mandatory.** Every artifact must work completely at the casual depth. Depth is *added underneath* a complete surface, never *extracted from* an incomplete one — an artifact that only works if you already know something has failed the casual contract, and that failure is a Governance finding rather than a compliment to the attentive.

This is what makes *high accessibility and high niche density* compatible rather than opposed, and it is the reader-facing statement of the same principle Section 5.3 states at the world-facing end. The attention contract per tier (Section 14.18) is where each depth's entitlement is actually recorded.

### 17.16 The Overtone as an In-World Institution (v0.6.1)

*(CLARIFIED. v0.5 §17.13 established the publication as an institution; v0.6.1 states where its records actually live, because the answer spans five partitions and was previously implicit.)*

| Aspect | Partition | Holds |
|---|---|---|
| The Overtone as an institution in the world | **W** — `ORGANIZATION` | Founding, ownership, editors as `CHARACTER`s, institutional history, its position in the media ecosystem (§15.17) |
| The editorial operation | **P** | Editorial decisions, issue plans, department roster, taste criteria, writer personas, art direction |
| Published issues | **I** | The artifacts themselves (§13.6a) |
| Visual assets and identity | **V** | Covers, illustrations, the publication's visual specification (§13.6c) |
| Public knowledge and perception | **E** | What the world believes about The Overtone; theories about its ownership; its reputation |

**The distinction this makes operable.** *That The Overtone is a respected paper of record* is an Epistemic fact about what the world believes. *That it is owned by a particular house* is a World fact. *That it will run a piece next month* is Production. *That it ran one last month* is Issue. Four different truths about one institution, and no two of them may be resolved from each other.

### 17.17 Editorial Taste and the Criteria Board (v0.6.1)

*(ADDED as a **capability of Editorial** — not a domain, not a board of agents, not an engine. P-32.)*

Governance can already tell the author that a piece is derivative, over-explained, or flat (§19.3). What it could not do is say what *this publication's* standard is, as opposed to a general standard — because the system had no representation of taste beyond the author's own corrections.

**The pipeline:**

```
Real-world publications  →  research / ingestion  →  magazine analysis
                                                          ↓
                                              content and layout analysis
                                                          ↓
                                              observed characteristics
                                                          ↓
                                              interpretation  →  TASTE CRITERION (P)
                                                          ↓
                                              evaluation of coolboy12's own work
```

**What the pipeline extracts**, and the distinction that keeps it honest — **measurable signals** are counted, **editorial judgments** are authored:

| Measurable signal | Editorial judgment |
|---|---|
| Article mix and length distribution | Editorial principles |
| Pacing and density across a run | Editorial confidence |
| Headline behaviour and length | Humour and seriousness, and their ratio |
| Visual rhythm and image-to-text ratio | Cultural texture |
| Typographic inventory | Novelty versus imitation |
| Advertising placement and share | Publication identity |

The left column can be extracted. The right column can only be *proposed* from the left and confirmed by the author. A system that treats the right column as extractable has decided that taste is a measurement, which is the failure this whole capability exists to avoid.

**A Taste Criterion is a Production record**, authored or author-confirmed, stating something the publication is trying to do — a standard for openings, a register, a relationship between image and caption, a length discipline. Criteria are **derived from evidence and confirmed by the author**; an observation about a real magazine never becomes a criterion by being observed.

**Three constraints.**

1. **Taste is Production, never Canon.** A criterion is a fact about how the author wants the work made. It says nothing about the world.
2. **Criteria are evidence for judgment, not rules that block.** They enter Governance as **judged** findings (P-24) and are overridable with a recorded reason. A taste standard that blocked would be a style guide with a gun.
3. **Real publications are anchored, not copied** (P-29). An observed characteristic of a real magazine enters as a **transformed** criterion with its transformation recorded, exactly as a Reality Anchor does. *"Do what that magazine does"* is not a criterion; *"openings should arrive mid-situation, because this publication distrusts preamble"* is.

### 17.18 The Taste Corpus and Magazine Deconstruction (v0.6.1)

*(ADDED as an Editorial capability. **Reference material, never canon, never Registry.**)*

**The Taste Corpus** holds real publications for analysis: publication · issue · page · article · visual · layout · editorial pattern · observed characteristic · interpretation. It is a Production reference store. It is **EXTERNAL/reference in the source-of-truth classification** (§29.6a) — no world fact, no canonical semantic, and no registry definition may ever be sourced from it.

**Magazine Deconstruction** is the pipeline that populates it:

```
PDF / scan / image → OCR → document understanding → page segmentation
→ layout analysis → article extraction → visual extraction → typographic analysis
→ editorial pattern extraction → observed characteristics
```

**Realization (v0.6.3).** **Docling** (`docling-project/docling`, MIT, LF AI & Data Foundation) — **ADAPT** — supplies document parsing, OCR, layout analysis, reading order, and table/article extraction behind the Magazine Deconstruction adapter (A-1). **Surya** (`datalab-to/surya`) — **WRAP** — may serve as an alternate OCR and layout stage; its **code is Apache-2.0 but its model weights are non-free** (CC-BY-NC-SA with a revenue/funding waiver and a competitive-use restriction), and it spawns a local server on first use, so it is wrapped to run on demand only and its licence must be checked against the deployment. Output from either is stamped **EXTERNAL** and may not reach `W` or `R` by any path.

**What the components do not supply, and coolboy12 does:** typographic *interpretation*, editorial pattern extraction, comparative analysis across publications, Criteria Board semantics, and Taste semantics. The components read a page; they do not know what a publication is *for*. Degraded mode: corpus ingestion halts, the existing corpus stays fully usable, and no other capability blocks. Exit: outputs are plain structured records — swap the parser and re-ingest.

**Why this is worth the machinery.** §18.9 requires that the artifact's physicality be *authored* rather than generated — a specified paper, a specified press, a specified era. Specifying those credibly requires having looked closely at real ones. Deconstruction is how the author's eye is scaled without the author reading four hundred magazines twice.

**The hard boundary.** Everything in the corpus is **real-world material**. It informs Production. It reaches the World partition only through a Reality Anchor with a recorded, non-empty transformation (§11.1, P-29), and it reaches the reader only as something the world made for itself.

### 17.19 Writer Persona, Voice, and Evolution (v0.6.1)

*(ADDED. A Writer Persona is a **Production record**, and emphatically **not an AI model** — it is a described way of writing, not a thing that writes.)*

```
CHARACTER (W)  →  writer role  →  WRITER PERSONA (P)  →  writing context
```

A persona is attached to an in-world `CHARACTER` where the writer exists in the world, and to a Production role where they do not. It carries register, habits, preoccupations, blind spots, opinions that may be wrong, and the things this writer will not say.

**A Writer Persona describes**, and each of these is a field the Context Builder can act on: **voice** · **syntax** · **vocabulary** · **rhythm** · **humour** · **expertise** · **worldview** · **biases** · **blind spots** · **interests** · **rhetorical patterns** · **knowledge boundaries** — what this writer does not know, which is what makes them wrong in character — · **professional experience** · **evolution**. The path is `CHARACTER (W) → writer role → WRITER PERSONA (P) → Context Builder (§24) → writing context → draft`. **There is no Writer Engine**; the persona is a record and the drafting is the bound substrate executing a role (P-15, P-32).

**Voice analysis** derives a **voice profile** from existing work — sentence rhythm, vocabulary, syntactic habit, characteristic move, register range — and feeds persona refinement. It is **descriptive**: it reports what a voice *has been*, which is how drift is detected (§18.3), and it never prescribes what a voice must be.

**Persona evolution** is the capability that makes a decade-long publication readable:

```
career → events and experiences → belief changes → editorial conflicts → voice change
```

**A writer who has not changed in ten years is a defect, not a constant.** A persona's evolution is authored through the ordinary path, is recorded in Creative Memory with its reason, and is exactly the sort of thing a returning author needs told back to them (§28.2).

**The epistemic point, which is the reason this is architecture and not styling.** A persona with genuine blind spots produces **authored misconceptions** (§14.9) as its normal output. A columnist who is wrong about something, consistently and in character, is one of the most efficient indirect-lore instruments the publication has — and it only works if the wrongness is specified rather than accidental.

### 17.20 Issue Intelligence (v0.6.1)

*(ADDED as an Editorial capability — an analysis over a planned issue, advisory, with a named consumer.)*

Reports, for an issue in preparation: content balance · department balance · topic diversity · serious/light rhythm · lore density · **ordinary-life coverage** (§16.6) · visual rhythm · advertising realism · reader-depth coverage (§17.15) · debt discharge.

It **never blocks and never prescribes**. It reports, in the same register as the Story Balance Analyzer (§19.10), and its consumer is the author at the point of issue planning (§31, step 2a).


---

## 18. Creative Studio Architecture

*(Record System note, v0.7.0: visual records belong to the **Visual Record Model** — a sovereign Record Model (§13, I-101), never independently a truth authority (§13.6c, I-89), and never metadata on a World Record. A specification is canon; an asset is a manifestation; an analysis is an observation.)*

The Creative Studio is the **manifestation layer**: it turns Editorial's decisions into finished artifacts, driven by canon and editorial intent. It is emphatically *not a content factory* — it does not decide what to make or invent world-facts; it renders what the world and Editorial have already determined, to a professional standard, and hands provisional drafts to the gate.

### 18.1 What the Studio Produces

Writing (articles, columns, features, fiction, in-world documents, advertisements, classifieds, each in a defined voice); visual direction (covers, interior art, illustration briefs); **layout, typography, and the page** (the artifact's physical design language — Section 18.9); symbolism (the recurring marks and motifs that accumulate meaning across issues); image-generation prompts (the briefs handed to external visual tools through an adapter, Section 26); and publishing assets (the assembled artifact, its metadata, its export).

### 18.2 Production Constraints from Canon and Editorial

Every production decision is *bounded*: by canon (a character's established appearance, a location's essence, a symbol's meaning), by the knowledge-state (what this artifact may reveal to which tier, Section 14), and by Editorial's form and timing decisions (Section 17). The Studio does not get to contradict the world to make a better picture; a visual that breaks canon is a contradiction to resolve, not a creative liberty.

### 18.3 Visual, Voice, and Symbolic Continuity

Three continuities are the Studio's standing responsibility. **Visual continuity** — a character, place, or object looks consistent across artifacts and across time (aging where the timeline demands it). **Voice consistency** — each in-world persona keeps its register, habits, and blind spots; a persona that drifts is flagged. **Symbolic continuity** — a motif means the same thing each time it appears, and accrues meaning deliberately. Once canonical, visual identity carries the *same authority and the same gated path as text* (visual canon is canon); a disagreement between a visual asset and prose is a contradiction, not a precedence question.

### 18.4 Medium Translation

When the same world-material must appear in more than one medium, the Studio performs **medium translation** — expressing one canonical truth in the grammar of each medium without any medium becoming a second source of truth. Translation reads canon; it never edits it.

### 18.5 The Draft Lifecycle

Exploration, sandboxing, and "what if I did this?" are stages in the life of a draft, not separate systems:

```
IDEA → PROPOSAL → SIMULATION → WORKING → REVIEW → APPROVED → CANON
```

**IDEA** (captured, commits nothing) → **PROPOSAL** (given concrete shape) → **SIMULATION** (run through the temporal engine, Section 15, to see its consequences *without* committing) → **WORKING** (developed into finished form) → **REVIEW** (Studio Standards evaluates; the staff critiques; alternatives and the counter-case surface) → **APPROVED** (the author confirms at the gate) → **CANON** (committed transactionally). Only APPROVED becomes canon. A killed draft leaves its reasoning in Creative Memory, so a superseded idea is retired on the record rather than silently forgotten and accidentally re-proposed. Two tempting engines (what-if, sandbox) become zero engines and one honest set of states.

**Where Operational Rollback lives.** Abandoning a draft at any state before APPROVED is **Operational Rollback** (Section 12.10.1): nothing canonical is touched, no gate is required, and the abandonment is recorded with its reason. This is the cheap, safe, encouraged operation — and naming it precisely is what keeps the expensive one from being reached for casually.

### 18.6 Canonical Visual Identity vs. Asset Instance

A contradiction sat between two correct statements: visual canon is canon (§18.3), and every external tool is replaceable behind an adapter (§26). If a character's canonical appearance *is* a generated image file, then replacing the image generator changes canon — which is absurd, and would make the world hostage to a vendor.

The resolution: **canonical visual identity is the *description*, not the file.** What is canonical is the structured, human-readable specification of how a character, place, object, or symbol looks and what it means — features, proportions, palette, materials, bearing, aging rules, the motif's significance. That specification is a World record, gated like any other canon, and legible without any tool (P-27). An **asset** is a *manifestation* of that identity: a Production record, produced by an adapter, versioned, content-addressed, and provenanced with the prompt, the brief, the tool binding, and the canonical identity it renders.

**Regeneration is therefore not a canon change.** Re-rendering a character years later with a different tool produces a new asset instance of the same canonical identity; if it *diverges* from the specification, that is a continuity finding against the asset, not a mutation of the world. Only editing the specification changes canon.

### 18.7 Asset Lifecycle

Assets are the largest storage class in the system and the one most likely to be silently orphaned. Their lifecycle: **briefed** → **generated** (candidates, Working state) → **selected** (one instance chosen, with the others retained as rejected candidates and their reasons) → **bound** (attached to the artifact it serves and to the canonical identities it renders) → **published** (immutable thereafter) → **superseded** or **retired**.

**Correction is a new publication, never an edit.** The system allows exactly one form of correction: a **correction artifact** — an erratum, a corrected reissue, or a superseding piece — published as a new artifact with its own publication history, its own canon basis, and a recorded **supersedes** relationship to the original. The original stays exactly as published: immutable, still bound to the artifacts and issues that used it, still what readers were actually given. A production record is **never retconned** — retcon is a canon operation and has no application to Production State, whose errors are corrected forward. Where the artifact exists in-world, a correction is a new **in-world publication act** (Section 17.7.1) and is proposed as such: in the fiction, a retraction is an event, and often an interesting one.

Four invariants. Every asset records its provenance chain. Every published asset is immutable. No asset is authoritative about the world; the specification is. And no asset is deleted while an artifact references it.

### 18.8 Prompt, Layout, and Export as Governed Workflows

Three Studio workflows, each composed by the Composer, each on the ascending current, each failing open. **Prompt construction** derives from canonical identity plus editorial intent plus continuity constraints — never from an author's free recollection — so a brief that contradicts canon is caught before generation rather than after. **Layout** carries the artifact's design language as a Production record, versioned, so a decade of issues has a traceable visual lineage. **Export** assembles the artifact and its metadata, stamps it with the **canon basis** it was derived from (Section 20.5), and hands it to publication. All three are reduced-mode capable: without an image adapter, the Studio still produces briefs, layout, and export manifests, and marks the visual stage as incomplete rather than blocking the issue.

### 18.9 The Publication Artifact Model (v0.5)

There is no physical magazine. The public surface must nonetheless make a reader feel that **each page was printed and scanned** — that they are handling an object that exists, produced by a society that exists. This is not styling applied at the end; it is a model the Studio produces and the publication surface renders (Section 27.5), and it must be architected or it will be improvised per issue and drift within a year.

**Classification:** capability, owned by Creative Studio. **Current:** ascending. **State class:** Production.

**The artifact hierarchy.** `Publication → Issue → Spread → Page → Region → Element`, where a **region** is a bounded area of a page (a column, a plate, an ad slot, a margin) and an **element** is a piece placed in it. Pages are **ordered and numbered**, spreads are **paired**, and the sequence is meaningful: what faces what is a compositional decision, and a reader turning from one page to the next is the smallest unit of pacing the format has.

**The material vocabulary.** The model carries the properties that make a page read as a printed object: page dimensions and proportion; paper character and tone; ink behaviour and registration; typography and its era; margins, gutters, and rules; page numbering and folios; image treatment and halftone character; printing imperfection — misregistration, show-through, ink density variation; physical wear and handling; editorial marks; and the scan itself as a mediating layer.

**OPEN — the specific field list.** The vocabulary above names the *concept space*; the enumerated, typed field set is not settled and is not invented here. It is Registry work (Section 9.4) and needs an authorial pass on which properties are per-publication, per-era, per-issue, and per-page. Carried forward as an open item.

**Realization (v0.6.3).** Layout and pagination are supplied by a CSS Paged Media engine behind adapter A-8; image operations by **Pillow** (HPND) — **ADOPT** — and **scikit-image** (BSD-3-Clause) — **ADOPT** — with **ImageMagick/Wand** **WRAP**ped for effects better expressed as CLI operations, and a halftone module **FORK**ed and vendored if used. Note that some page-rendering engines carry copyleft network licences that must be reviewed against the deployment (§26.2g). The components **render**; the material specification is authored and is a coolboy12 record. Source-of-truth class: **DERIVED**. Exit: the specification is a record — re-render under a different engine.

**Three rules.**

1. **Physicality is authored, not random.** Imperfection that is generated noise reads as a filter. Imperfection that is *specified* — this publication's paper, this era's press, this issue's water damage — reads as an object with a history. The material properties are Production records with provenance, not a post-process.
2. **The artifact model is era-bearing.** A period issue (Section 17.14) uses its period's material vocabulary. This is most of what makes a period issue work before a word is read.
3. **The public surface is a publication viewer, not an application.** Stated fully at Section 27.5. The consequence for the Studio: the export (Section 18.8) must carry the artifact model, not a web layout, because the surface's job is to present the object rather than to re-flow it.

### 18.10 Art Direction as World Information (v0.5)

Visual decisions are not decoration applied to information; they *are* information, and the architecture should treat them as a channel with the same seriousness as prose.

A page's visual language can carry: **culture** (what this society finds beautiful, formal, cheap, or vulgar); **technology** (what the press can do, what images can be made and how); **class** (who this publication is for, legible in paper stock and typeface before a word is read); **era** (the strongest and fastest signal available); **species** (proportion, ergonomics, colour assumptions, what a page even is for a reader who is not human — Section 11.4); **politics** (what may be depicted, what is euphemised, whose face appears); **institutions** (house style as an institutional fingerprint); **geography and materials** (what this place makes paper and ink from); and **historical memory** (a motif that means something because of what happened).

**Two consequences for the architecture.**

- **Visual specifications are canon where they describe the world** (Section 18.6) and Production where they describe the publication's taste. A society's aesthetic conventions are a `CONCEPT` in the World partition; The Overtone's house style is a `STYLE-GUIDE` in Production. The distinction matters when the magazine's taste is *unrepresentative* of its society — which is often the interesting case.
- **The visual channel is subject to P-30 and to leakage detection.** An image can over-explain exactly as prose can, and an image can leak a withheld fact more easily than prose because it is harder to audit (Section 14.16). Both are evaluated at Governance (Section 19.11).

### 18.11 Visual Intelligence (v0.6.1)

*(ADDED as **Studio capabilities** over the `V` partition (§13.6c). Four capabilities, **no engines**, P-32.)*

**Image understanding — realized by OpenCLIP.** **OpenCLIP** (`mlfoundations/open_clip`, MIT code) — **ADAPT** — supplies image and text embeddings and zero-shot classification behind adapter A-2. Output is a `VISUAL-ANALYSIS` record: **an observation, never a fact about the world** (I-89). coolboy12 owns the observation→discrepancy→proposal→gate path; the model owns none of it. Note that pretrained weight licences vary by training set and must be checked separately from the code licence. Degraded mode: analysis unavailable, continuity checks fall back to manual, assets and specifications unaffected. Exit: observations are records; re-analyse under a new model.

For an asset, analyse what it contains: characters · species · location · objects · clothing · architecture · technology · symbols · era · composition · palette · medium · mood. Output is a `VISUAL-ANALYSIS` record in `V`. **It is an observation about an image, never a fact about the world.**

**Visual continuity.** The capability the Studio most needed and least had:

```
visual asset + canonical visual specification + prior visual references + timeline
                                    ↓
                        visual continuity analysis
```

It detects: divergence from the canonical specification · contradiction with earlier depictions · **ageing inconsistency against world-time** · symbol drift (§18.3) · unexplained change. Findings are **judged** (P-24) and land against the *asset*, never against canon — because the specification is what is true and the asset is what was made (§18.6).

**Visual similarity and retrieval — realized by FAISS.** **FAISS** (`facebookresearch/faiss`, MIT) — **ADOPT** — supplies the derived embedding index behind adapter A-3. Input: embeddings produced by the vision adapter. Output: ranked nearest-neighbour candidates. **Authority: none.** Source-of-truth class: **DERIVED** — deletable and rebuilt from V (§29.8). coolboy12 owns visual identity and meaning; FAISS owns nothing. **LanceDB** is a COMPOSE alternative where on-disk persistence of the derived index without a server is wanted, at the cost of format lock-in. **Qdrant is REJECTED** — a permanently-running server contradicts §28. Degraded mode: retrieval falls back to enumeration over V. Exit: delete and rebuild.

Answers *all images of Character X* · *all depictions of Location Y* · *all images containing Symbol Z* · *similar composition* · *likely duplicate* · *the previous depiction of this object*. **This is derived indexing and never a second source of truth** (§29.6a) — an index that disagrees with the Visual Library is wrong and is rebuilt.

**Visual-to-canon proposal.** The one path by which looking at an image can change the world, and it is the ordinary path:

```
image → observation → potential discrepancy or new information → PROPOSAL
      → validation → Human Gate → Mutation Coordinator → canon
```

**Vision never canonicalizes.** An analysis that contradicts canon raises a discrepancy; a discrepancy becomes a proposal; a proposal meets the gate. The most common correct outcome is that **the image is wrong and canon stands** — the asset carries a continuity finding and the world is untouched.

### 18.12 Art Direction and Publication Identity (v0.6.1)

*(ADDED. Two Production capabilities, closely coupled.)*

**Art Direction Intelligence** composes canon + editorial intent + taste criteria (§17.17) + writer and publication identity + the Visual Library into a **brief**: what this piece should look like, why, which prior visual language it continues, and what it must not resemble. It produces a Production record and hands it to the ordinary prompt-construction path (§18.8). It **decides nothing** — it assembles the constraints a decision needs.

**Publication Identity** is the persistent `STYLE-GUIDE` record of what The Overtone *is*, visually and editorially: editorial voice · visual language · typography · recurring departments · recurring personalities · graphic motifs · advertising style · cover philosophy · photography style · paper and press character (§18.9).

**It is versioned and it evolves.** A publication that looked identical across forty years never existed. Identity change is authored, recorded with its reason, and is itself a signal to a reader who has been paying attention — a masthead that changes in issue 60 is a story about the institution (§17.16).

### 18.13 Period and Archival Issue Intelligence (v0.6.1)

*(ADDED. The capability that makes §17.14 executable rather than aspirational.)*

A period issue is not a modern issue with an old date. Producing one requires a coherent set of period constraints, and the capability assembles them: era-specific language · editorial norms · **knowledge limits** · available technology · typography · advertising conventions · cultural assumptions · material vocabulary (§18.9) · what could not be depicted · what would not have been questioned.

**The knowledge-limit constraint is the one that does the work.** A period issue must not know what its period did not know, and that is an **Epistemic** constraint (§14) resolved at the issue's world-time rather than the present. A 938 issue confidently asserting something discovered in 1200 is not an anachronism of style; it is a leak (§14.16).


---

## 19. Creative Governance — Studio Standards

Creative Governance is the quality layer, and its framework is **Studio Standards**. Its one job is to tell the author, with reasons, **whether the work is coherent and whether it is good** — and it never generates, never recommends creative direction, and never commits canon. *The staff recommends; Studio Standards validate; the author decides.*

### 19.1 Correctness vs. Quality — Two Registers

Studio Standards evaluates in two registers and treats them completely differently:

- **Correctness is fact. It is enforced mechanically and fails closed.**
- **Quality is judgment. It returns a recorded verdict the author may override with a reason.**

*A factual contradiction is blocked; a weak execution is diagnosed and decided.* This line is the whole reason quality can be strict without becoming a tyrant.

**The correction v0.4 made (P-24).** Not everything filed under "correctness" is mechanically decidable. A dangling reference is; a semantic contradiction between two paragraphs of prose is not — it is a judgment produced by the same non-deterministic substrate that wrote the prose. Granting that judgment unappealable blocking authority hands a model final say over the author on a matter of interpretation, which inverts Conviction V.

Correctness therefore splits in two, and quality is unchanged:

| Class | What it is | Examples | Authority |
|---|---|---|---|
| **Structural violation** | Decidable without interpretation, by the Canon Linter (Section 12.15). | Dangling reference · locked-field write · status or tier illegality · subtype illegal for its kind · publishing-firewall breach · partition violation · edge authoritative in two Relationship Records · empty anchor transformation (P-29) · missing basis state · unaxised temporal claim · missing provenance · a hidden object present in a projection or in the public surface's exposure set. | **Blocks. No override.** The record is malformed; there is nothing to adjudicate. |
| **Judged contradiction** | Requires reading meaning. High severity, still a judgment. | "This passage implies the house still stands" · "this portrayal contradicts her established nature" · "this image suggests a fact the text withheld." | **Surfaced at high severity; adjudicated by the author** with a recorded reason. Blocks *by default*; the author may proceed, and the fact that they did is permanent. |
| **Quality judgment** | Taste. | Timing, freshness, affect, indirectness, resonance, whether a reveal lands. | Diagnosed, never blocks; overridable with a reason. |

The distinction is not a softening. A judged contradiction blocks by default and is loud; what changed is that the author can *answer* it, and the answer is recorded.

### 19.1.1 The Appeal Protocol

When the author proceeds over a judged contradiction: the finding, the author's reason, and the state of the record at that moment are written to Creative Memory and to History Record. The overridden finding **does not disappear** — it is marked *adjudicated*, remains visible in Canon Health, and is re-surfaced if the same contradiction is later implicated in a new change. Repeated overrides of the same finding class are themselves a finding: either the standard is wrong, or the world is drifting, and the system says which it suspects. A structural violation has no appeal, because there is nothing to appeal to — fix the record.

### 19.2 The Verdict Format

Every quality verdict reads in four parts, never as a bare score:

```
CRITERION   — the specific standard being applied, in words
OBSERVATION — what the work actually does against it
JUDGMENT    — pass / flag / block, and why the observation meets or misses the criterion
CONFIDENCE  — how sure the reviewer is, and what would change it
```

A verdict that cannot be understood cannot be inherited, contested, or improved.

### 19.3 The Diagnostic Vocabulary

Governance separates *kinds* of problem that a bare score would blur:

- *"Canonically correct, but narratively premature"* — accurate, but the reader knowledge-state isn't ready for this beat.
- *"Structurally sound, but the reveal is too early"* — the clue economy hasn't reached reveal-readiness.
- *"Coherent, but derivative"* — it passes correctness but repeats a pattern the corpus already has (§19.5).
- *"Accurate, but emotionally flat"* — correct and unmoving.
- *"This payoff needs more foreshadowing to land"* — narrative debt is being redeemed before it was properly accrued.
- **"Over-explained"** *(v0.5)* — the piece states what it should have implied. The world is delivered rather than depicted (§19.11).
- **"Anchored but not transformed"** *(v0.5)* — the real-world source is legible through the counterpart; this reads as reference rather than resonance (§19.11).
- **"Plot-saturated"** *(v0.5)* — every item in this issue carries narrative load; the publication has no ordinary life in it (§17.13).

Each is a *quality* verdict (overridable with a reason), and each names the specific axis so the author knows exactly what to weigh.

### 19.4 The Evaluation Set

Studio Standards evaluates, at minimum: canon coherence, timeline coherence, unknown-and-reveal health, arc health, editorial balance and timing, narrative readiness, novelty, creativity, world richness, reader accessibility, voice consistency, visual consistency, symbolic continuity, artifact fitness, medium fitness, contradiction risk, and publishing readiness — and, from v0.5: **indirectness** (§19.11), **anchor resonance** (§19.11), **ordinary-life presence** (§17.13), **artifact physicality fitness** (does this page read as an object of its publication and era? §18.9), and **layer integrity** (does the casual surface work completely on its own? §17.15).

The health dimensions are standing analyses with named consumers (P-10). **Publishing readiness** is the composite ship gate: blocked only by open critical or major *correctness* failures; everything else is a judgment the author may override with a reason.

### 19.5 The Anti-Formula Duty

A decades-long system creates one hazard *by working correctly*: it accumulates its own patterns, retrieves them, produces work shaped by what it retrieved, and deposits those patterns back — so retrieval finds them more readily next time. Left alone, a decade of correct operation yields work that is coherent, defensible, and a competent recombination of its own past. So Governance owns the question **"does this repeat us?"** — answered as taste, not metric. It is enforced in three places: every standard can fail a piece for being a competent rerun; the consistency audit scans the corpus for self-repetition; and a pattern hardened into a template is treated as a *finding*, never an asset.

### 19.6 Counter-Case Reasoning and the Positive Channel

For any consequential proposal, Governance produces the strongest genuine **counter-case** — the best argument against it — or states honestly that none exists; it never fabricates one. And because every other signal it produces is a deficit, Governance runs a **positive channel**: when work meets or exceeds a standard, it records *what worked and why*, attributed to the piece that proved it (→ Creative Memory). Over years the system acquires a memory of its own successes — the raw material of taste, and the only non-deficit thing it can ever say.

### 19.7 Standards Rise Over Time

A standard is not fixed. Three bands: **acceptable** (meets the threshold), **excellent** (does something the standard could name but did not require), **world-class** (does something the standard *could not* have required — which then teaches the standard, raising the bar for every future piece). The third band is recursive on purpose, so it can never become a checkbox to optimize toward.

### 19.8 The Verdict Record

The four-part verdict gains three fields: **class** (structural / judged / quality), **severity** (blocking / high / advisory), and **evidence** (the specific Records, evidence-graph paths, or corpus instances the verdict rests on). The evidence field is what makes the anti-formula duty honest: *"coherent but derivative"* is an assertion until it names the three prior instances it resembles, at which point it becomes a finding the author can weigh or dismiss. A verdict without evidence is an opinion offered as a result, and Governance does not issue those.

### 19.9 Automatic Continuity Review

A standing, composed review — not a role's habit — run before every gate and at every epoch transition. It walks: canon coherence over the affected region; visual, voice, and symbolic continuity (§18.3); knowledge-state consistency and leakage (§14.16); timeline coherence across all three axes (§12.16); evidence-graph integrity (planted-but-never-redeemed, redeemed-but-never-planted); and debt state. Its output is a verdict set in the §19.8 format, classified per P-24. Making it standing rather than role-owned is the point: a behavior disappears when a role is redefined, and continuity is not something the system should be able to stop doing by accident.

### 19.10 The Story Balance Analyzer

A standing analysis, advisory only, over the corpus and the plan: distribution of attention across regions of the world, across characters, across arc types, across registers (political / personal / mysterious / atmospheric / **ordinary**), across departments, and across tiers served. It reports imbalance, never prescribes correction — *"eleven of the last fourteen issues centre the same three lineages; the northern material has appeared twice in two years"* — and it feeds Emergence ranking (§16.6) and Editorial selection (§17.1). It never blocks, and per P-10 it exists only because Editorial selection consumes it.

### 19.11 The Indirectness and Resonance Standards (v0.5)

v0.5 adds two design principles that can be violated in ways nothing else catches. Both are **judged**, never structural, because both turn entirely on reading meaning — and both are stated as standards here so that P-29 and P-30 have an enforcement home rather than remaining aspirations.

**The Indirectness Standard (P-30).** *Does this artifact depict, or does it explain?*

The finding is **"over-explained"**, and it is raised when a piece states a canonical fact that its own material would have implied. Its evidence field names the fact stated and the implication available. Three sub-findings, each with a different fix:

- **Exposition without a speaker.** A passage asserts a world-fact in no one's voice. In a publication every sentence has an author with interests; a sentence with none is the system talking.
- **Canon-derived rather than society-derived.** The piece was built from the World partition directly rather than through Society and Epistemic Distribution (Section 8.5). Diagnosable from the derivation chain the Composer recorded, which makes this the one part of the standard with structural evidence behind a judged verdict.
- **Nothing left to infer.** The artifact closes every question it opens. This is the failure that looks most like competence.

**The counter-finding matters as much.** *Under-implied* — the artifact leaves so much unstated that no reader at the target depth can assemble anything — is the same standard failing in the other direction, and is caught by the Fair-Play Validator (§14.13) and the layer-integrity axis (§17.15). Obliquity is not a virtue in itself; obliquity *that a reader can penetrate* is.

**The Resonance Standard (P-29).** *Is this anchored, or is it borrowed?*

The finding is **"anchored but not transformed"**. The linter has already blocked anchors with an empty transformation field; what remains is the judgment the linter cannot make — whether the transformation is *meaningful*. The standard names the target explicitly: the reader should feel *"this is strangely familiar,"* never *"this is that thing renamed."* Its evidence field names the real-world source and the transformation claimed, so the author is weighing a specific assertion rather than a vague discomfort.

Two sub-findings: **reference-dumping** (anchors appearing in density, each carrying nothing, so the work reads as a catalogue of recognitions) and **parody drift** (the counterpart is funny *about* its source rather than functional in the world — a legitimate choice occasionally, a fatal one as a default).

Both standards are quality verdicts. The author may override either with a recorded reason, and the override is permanent and re-surfaced (§19.1.1). *The system can tell the author that a page explains rather than depicts. It cannot tell them that explaining was wrong here — sometimes it is exactly right, and only the author knows when.*

---

## 20. Reader Simulation

The system must know how the universe *lands* — before publication and after. Reader Simulation belongs to the Studio Standards family (evaluative, never generative) and runs directly on the Knowledge-State Architecture (Section 14): it reasons about each reader tier *as of the current issue*, not the reader in the abstract.

### 20.1 The Four Readers

- **Casual** — reads individual issues for atmosphere; notices events, not patterns. Must receive a complete, satisfying surface encounter with no prior context required.
- **Engaged** — reads across issues; notices recurring names and patterns; perceives arcs before they are named. Must be rewarded for attention.
- **Investigator** — reads as a puzzle; tracks clue chains; maintains hypotheses; rereads. Must be rewarded with *genuine* depth — real structure that repays investigation, never manufactured complexity.
- **Conspiracy theorist** — over-reads; builds theories from noise; connects what was not meant to connect. Must find enough consistency that over-reading occasionally strikes real ore, and enough discipline that the world does not accidentally validate nonsense.

These four are the roster, not the law (§14.18), and they map onto the four discoverability depths of §17.15 — the tiers are the *knowers*, the depths are what each is *owed*.

### 20.2 What It Evaluates

Per tier, for a given artifact: **comprehension** (what they understand after reading), **curiosity** (what questions it raises), **confusion** (where they get lost, and whether that hurts surface enjoyment), **payoff satisfaction** (whether rewards land for this tier's attention), **theory generation** (what theories form — and, for the conspiracy theorist, whether the world survives being over-read), and **suspicion** (how close each tier now is to a hidden answer, feeding reveal-readiness in Section 14.3).

### 20.3 The Simultaneity Principle and Reader-State Tracking

The architecture must work for **all tiers simultaneously**: an issue that rewards investigators at the casual reader's expense has failed its editorial function. Every issue must be a complete surface encounter with depth that rewards additional attention (§17.15). After publication, Reader Simulation advances the **knowledge trajectory** (Section 14.4) — updating what each tier now knows, what threads are open, and what payoff debt is owed — so the next issue is planned against an accurate reader-state. The minimal consequences of reading are recorded in canon; readers are experienced, not surveilled.

### 20.4 The Firewall Correction

Epistemic records are canonical (Section 13.6). Publication therefore appeared to *write canon* — contradicting P-5 and Spine law 5 — and the worked example in Section 31 described the write as happening "transactionally" with no gate at all, which additionally breached laws 2 and 3. Read literally, publishing was a side door into canon. The resolution:

1. **Publication writes nothing.** It reads canon, derives an artifact, and records — as **Production State** — that the artifact was published, at what **issue ordinal**, on what date (production metadata, Section 12.16), and what canon basis it was derived from (Section 20.5). This record is **publication history**: authoritative about the work, never about the world, and never canon. Where the issue also exists *inside the fiction*, the in-world act of publication is a separate world fact on its own plane, proposed and gated like any other (Section 17.7.1) — never created by the act of shipping. The Firewall is intact and absolute.
2. **Reading produces a proposal, not a write.** Reader Simulation computes what each tier now knows, believes, suspects, misremembers, and is owed, and emits a **Reader Knowledge Proposal**: provisional, basis-stamped (P-22), on the descending current, carrying its evidence chain (Section 14.7).
3. **The author gates it.** Ordinarily as one batched Trivial-severity act per issue, with Scope of Approval recorded (P-23) — under a minute of attention, not a chore. Anything the proposal implies at higher severity (a reveal-state moving to REVEALED, a designed divergence collapsing, a leakage finding) is separated out and gated individually, because those are authored moments and always were.
4. **Until gated, reader-state is Working.** Planning may read it, clearly marked provisional. Nothing downstream may treat an ungated epistemic delta as established.

**Proposal lifecycle.** *Pending* — Working state; **may inform planning**, marked provisional; **may not** be a simulation premise, may not be published against, and may not serve as the basis for a canonical commit. *Accepted* — canonical; the epistemic record moves and the proposal closes. *Rejected* — recorded with its reason; canon stands unchanged, and the divergence between what readers were demonstrably given and what canon says they know becomes a standing Canon Health finding rather than a silent gap. *Stale* — a pending proposal whose basis has moved, or against which a further issue has published. *Superseded* — the next issue's proposal subsumes an unaccepted predecessor, so proposals never queue up unboundedly. **A pending proposal is never a third source of truth.**

**What this costs and what it buys.** It costs one small recurring gate act per issue. It buys the Firewall's integrity, an author who *decides* what readers now know rather than discovering it was inferred and written on their behalf, and an epistemic record that satisfies P-18 like everything else in canon.

### 20.5 Artifact–Canon Binding

Every published artifact records the **canon basis** it was derived from: the canon revision and epoch, and the specific objects it asserted. Without it the published corpus and canon drift apart with no recorded relationship — which becomes acute at the first retcon (Section 12.12), when the system must answer *which issues now say something the world denies*. With the binding, that is a query. Without it, it is an archaeology project. The binding is a Production record, immutable once published.

### 20.6 Breaking the Self-Confirming Loop

Reader Simulation estimates what readers know, plans the next issue against its own estimate, publishes, and updates the estimate from its own plan. Nothing in that loop touches an actual reader. Over a decade the model can drift arbitrarily far from reality while remaining perfectly self-consistent — and the same structure afflicts the anti-formula duty (§19.5), which judges the corpus's repetitiveness using the substrate that wrote it.

Two rules, both constitutional in force:

- **Assumption or measurement, declared.** Every model of an external reality declares which it is. A simulated reader-state is an **assumption**, labelled as such everywhere it is surfaced, and is never presented with the confidence of an observation. Only inputs derived from outside the system may be labelled **measurement**.
- **A correction channel is required for anything labelled measurement.** Actual reader signal enters through an ordinary adapter (Section 26), as evidence about the *reader model* (Production State), never as evidence about the world. It updates confidence and misconception records (§14.9) and it is explicitly optional: a system with no channel keeps operating on declared assumptions, which is honest, rather than on unlabelled ones, which is not.

**The reader-model drift check.** At each epoch transition, where real signal exists, the model's past forecasts are compared against it and the divergence is reported. A model that has never been checked against anything is reported as such. *A model nobody has ever contradicted is not a validated model; it is an unexamined one.*

### 20.7 Curiosity, Misunderstanding, Forgetting, and Theory

The evaluation set of §20.2 is extended to run on the full Reader Knowledge Model (Sections 14.6–14.16), per tier, per issue: **curiosity** (which questions this artifact opens, feeds, or starves); **misunderstanding** (what a tier will plausibly get *wrong*, and whether that misreading is authored or accidental); **forgetting** (which prerequisites have decayed below the confidence this beat requires, and what reinforcement would restore them); **prediction and surprise**; and **theory formation** (what hypotheses this artifact makes available, and whether any unintended pattern is confirming a theory the world does not hold). Each output is advisory, tier-labelled, and an assumption unless a correction channel says otherwise.

### 20.8 The Reader Flywheel and the Signal Classes (v0.5)

Section 20.6 establishes that real reader signal may enter the system. This subsection governs what it may *do* once inside — because the failure mode is specific, common in published work, and fatal here: **a flywheel that turns popularity into truth.**

**Five signal classes, each with a different authority.** They are named separately because they arrive mixed and are easy to average into a single "what readers want," which is exactly the collapse to prevent.

| Class | What it is | May influence | May never influence |
|---|---|---|---|
| **Raw analytics** | Counts and behaviour: what was opened, how long, what was returned to | Nothing on its own. It is an input to the reader model, not a verdict. | Editorial selection directly; canon by any route |
| **Reader signal** | What readers said: letters, questions, corrections, complaints | The **reader model** (Production) — confidence, misconception, comprehension | Canon; what is true |
| **Editorial signal** | What the publication learned about its own craft: what landed, what confused | **Production State** — standards, style, pacing, department mix | Canon |
| **Quality signal** | Governance verdicts and the positive channel (§19.6) | Standards over time (§19.7) | Canon |
| **Theory signal** | What readers believe, including wrong things (§14.12) | The **epistemic record** of what that tier believes — which is canonical *that they believe it* | What is true. Never. |

**The three rules.**

1. **Signal moves the model of the reader, never the model of the world.** Every class above lands in Production State or in the Epistemic partition's record of *what a knower holds*. None lands in the World partition. This is the same one-directional rule as Section 14.19, stated for the specific case where commercial and emotional pressure to break it is highest.
2. **Popularity is not evidence about the world.** That many readers believe a thing raises its `confidence` on *their* epistemic record and changes nothing else. A widely-held reader theory and a lone crank's theory are the same kind of record with different reach.
3. **The author may act on any of it — through the gate, with a reason.** If a reader theory is better than the plan, adopting it is an ordinary authored canon change (Section 12.6) whose recorded reason happens to be *"a reader thought of something better."* That is legitimate, honest, and traceable. What is forbidden is the same outcome arriving without an author, a gate, or a reason.

**The measurement obligation runs the other way too.** Signal that is never acted on accumulates as noise and eventually trains the author to ignore the channel. Per P-10, each signal class must have a named consumer or the channel is closed — and closing a channel is a legitimate, recorded decision, not a failure.

---

## 21. AI Coworker Architecture

The AI is not a tool that waits for prompts. It is a **staff** — a set of proactive specialist reasoning roles — that operates the domains on the author's behalf, working *ahead* of the author.

> **There is one reasoning substrate. Every coworker is a role executed by it** (P-15; the current binding is recorded in Section 26.1).

The staff is **role-based, not model-based**. There is no model routing, no multi-LLM committee, no autonomous agent swarm. A "coworker" is a remit plus a role-scoped context (from the Context Builder) plus a structured output contract. This keeps the system simple, cheap, and coherent, and it means every role improves whenever the single model does.

### 21.1 What Coworkers Do

Within their remit, coworkers **analyze**; **propose alternatives** (never a single unopposed option); **state their reasoning**; **state the counter-case** (the strongest genuine argument against their own proposal, or an honest "none exists"); **recommend next steps**; **surface missing material, narrative debt, opportunities, and risks**; **review**; **summarize**; and **warn**. Proactivity is the point: at the start of a session, the health checks have already run, the overdue payoff is already flagged, and two issue directions are already drafted. The author arrives to *decisions to make*, not a blank page.

### 21.2 The Staff

| Coworker (role) | Reasons like | Proactively does | Never does |
|---|---|---|---|
| **Editor-in-Chief** | The person who runs the magazine | Selects from the Opportunity queue; owns timing, pacing, payoff scheduling; owns the department mix and the issue's ordinary-life balance (§17.12). | Publishes without the author; commits canon. |
| **Creative Director** | The person who owns look and feel | Directs visual identity, covers, symbolism; owns the publication artifact model and its era vocabulary (§18.9–18.10). | Makes visual canon without the gate. |
| **Research Director** | The person who grounds the world | Sources evidence for plausibility; runs Reality Derivation when asked (§16.4); proposes anchors and their transformations (§11.1). | Lets real-world specifics become canon directly. |
| **Canon Keeper** | The world's librarian and lawyer | Runs coherence and canon-health checks; recommends reconciliations; flags contradictions, drift, missing graph edges, and misfiled `CONCEPT` records (§13.6). | Rules on or commits canon. |
| **Narrative Designer** | The story architect | Manages arcs, hidden facts, threads, clue economy, payoff economy; proposes structure; watches saturation and reveal-readiness. | Moves a reveal-state or closes an arc without the author. |
| **World Analyst** | The world's political scientist and economist | Runs Simulation; computes consequences; recommends pressures and opportunities; surfaces thin and ordinary-thin regions (§16.6). | Advances or commits world-state as canon. |
| **Producer** | The person who ships | Runs production; assembles artifacts; recommends sequencing; tracks what is done and owed. | Mutates canon during publication. |
| **Quality Reviewer** | The demanding editor | Runs Studio Standards; returns explained verdicts; produces counter-cases; enforces anti-formula, indirectness, and resonance (§19.11). | Overrides the author; blocks a judgment (only facts block); recommends creative direction. |

### 21.3 The Authority Model

Every coworker operates in one of three modes, never above it: **Generative** (may create *Working* content within a scoped context; never canon), **Advisory** (may recommend, question, challenge, discover; never canon, never override the author), **Audit** (may read everything and report; never create, modify, or rule on canon). No coworker may expand its own authority. No coworker's output is canonical until the human gates it. These boundaries are enforced partly by the Context Builder: a coworker cannot reason over canon that was never placed in its role-scoped context (Section 24.3).

### 21.4 Collaboration Without Bureaucracy

When roles collaborate, five guarantees hold: **authority** (final decisions are the author's, non-delegable), **provenance**, **review**, **accountability**, **ownership**. Disagreement between roles is *surfaced to the author intact*, not resolved internally, because it marks exactly where the author's judgment is most needed. This is a newsroom, not a committee.

**Unadjudicated disagreement is a state, not a silence.** Where roles disagree and the author does not resolve it, the disagreement persists as a recorded open question against the object in dispute, appears in Canon Health, and blocks nothing. It is never resolved internally, averaged, or dropped because a workflow ended.

### 21.5 Bounded Autonomous Work

Four bounds:

- **Compute, never commit.** Autonomous work may analyze, draft, simulate, check, and prepare. It may never gate, publish, or alter Production State that represents an authorial decision. It may create Working state freely.
- **Declare the basis (P-22).** Every precomputed proposal carries the canon state, epoch, and reader-state it was computed against, plus its authoring sequence and session. At the session start, anything whose basis has moved is marked **stale** and is re-validated or discarded before it is offered.
- **Budgeted.** Autonomous work runs within a declared budget of effort and context (P-14), and the budget is visible.
- **Attributable and dismissible.** Every autonomous output records which role produced it, why, and what signal triggered it. Dismissal is one act and teaches recommendation calibration (Section 32).

### 21.6 Roles Are Operational, the Authority Model Is Constitutional

The eight-role roster is the **current operating configuration**, not constitutional law: roles are added, merged, split, or retired as Production State with a recorded reason, following the contraction path when removed. What is constitutional is the **authority model**: three modes, no self-expansion, no canonical output without the gate, and scope enforced by context. New *behaviors* are welcome; new *models* are not (P-15). A role that would require its own reasoning substrate is not a role — it is model sprawl, and is rejected.

### 21.7 Degraded-Mode Behavior for Roles

When a role cannot get what it needs, it does not improvise. It reports **what it could not obtain, what it did anyway, and what its output should not be trusted for**, and its output is marked *reduced*. On the descending current a reduced output may not reach the gate at all (P-19). On the ascending current it may proceed, marked. **A role that silently substitutes its own recollection for missing context is producing fabrication with the appearance of provenance**, which is the most dangerous single failure available to an AI staff and is treated as a defect of the highest severity.

---

## 22. Creative Memory

Creative Memory is the layer beneath every domain that remembers not only *what* was decided but *why* — and what was *not* chosen, and why not. It is the mechanical form of *Intelligence Compounds; Artifacts Depreciate*.

### 22.1 What It Preserves

**Decisions** · **Rationale** (the options considered and the trade-offs weighed) · **Rejected paths, and why** · **Intentions** (why a character was created, why a reveal was delayed, why an arc was paced slowly) · **Opportunity history** · **Narrative-debt history** · **Author preferences and past trade-offs** · **Prior workflow outcomes** · **What worked** (the positive-channel deposits from Governance).

**Added in v0.6.1:** **taste evolution** — how the publication's standards changed and why (§17.17) · **publication evolution** — how its identity changed (§18.12) · **successful and failed patterns**, both recorded, because a failed pattern prevents a repeat and an unrecorded failure guarantees one · **persona evolution rationale** (§17.19) · **model calibration history** (§15.21).

**Added in v0.5:** **anchor rationale** — for every Reality Anchor (§11.1), the real-world source, what was transformed, and *why the transformation matters in-world*. This is authoring provenance and belongs here rather than in the World partition, where a real-world reference would be a manifestation-blindness violation. It is also the record a future author needs most: an anchor whose point has been forgotten is indistinguishable from a coincidence.

### 22.2 How It Works, and Why It Is Not a Second Canon

**Realization (v0.6.3): the pattern, not a platform.** Tamper-evidence is provided by a **Merkle / hash-chained append-only structure implemented natively** over the legible record — the data structure, not a transparency-log server. Server-based transparency platforms are **REJECTED**: they require a permanently-running service and an opaque backing store, contradicting §28 and P-27. Inclusion and consistency proofs over a large log are small; the value was always the structure. **Source-of-truth class: AUTHORITATIVE** — one of the few boundaries with nothing external behind it at all (AC-5).

Creative Memory is **append-only** and **tamper-evident**. Every commit through the mutation path writes a memory entry automatically, and the author can annotate intention at any time. It is addressable by meaning. It keeps two scopes that never mix: a **canon ledger** (everything that happened to this universe's canon — IP-local, sovereign) and a **craft ledger** (reusable taste, patterns, and method — de-canonized, carrying *how* and never the world's specific *what*).

Crucially: **Canon is what is true; Creative Memory is why decisions were made.** Memory records decisions *about* the world; it is never a source of truth *about* the world.

### 22.3 The Compounding Function

Because Memory is where rationale, rejected paths, and preferences accrue, it is what makes long-horizon coherence possible: a decision made in year eight can be checked against the reasoning of year one; a returning author can recover not just *what* the world is but *why* it became so.

### 22.4 Creative Memory and the Temporal Record

*(SCOPED v0.7.0. This section paired Creative Memory against the **History Record** as though every Record had one. Creative Memory sits opposite whatever temporal mechanism a Record Model defines — the History Record in World, and whatever E, P, R, V, and I each establish (§13.6d, I-90, I-107). **The pairing is constitutional; the World mechanism named in it is not.**)*

**A Record Model's temporal record** — the History Record in the World Record Model — is the canonical revision record of a Record: *what changed, when, who approved it, what caused it.* **Creative Memory** is the record of authorial reasoning: *why it was decided, what else was considered, what was rejected and why.* One is the trace of the world's evolution; the other is the trace of the author's thinking. Every commit writes to both, from the same single gated path, and neither is derivable from the other.

### 22.5 Precedence, Non-Duplication, and Query Order

**Precedence.** **A Record's temporal record governs what happened** — the History Record where the model uses one. **Creative Memory governs why.** **Canon governs what is true now**, and outranks both about the world. A disagreement between the temporal record and Memory about a *fact of change* is resolved in the temporal record's favor and raises a health finding.

**Non-duplication.** Neither record is the source of the other's content. Where Memory needs to refer to a change it **references** the History Record entry rather than restating it — a restatement is a copy, and copies drift.

**Query order.** *What is true?* → Canon, and stop. *What changed, when, who approved it, what caused it?* → History Record (or WSV-H, §13.10). *Why, what else was considered, what was rejected?* → Memory. Any capability reading these records declares its order and is bound by it — including the Context Builder, whose provenance must show which record an assembled context drew on.

### 22.5.1 The Two Write Classes

- **Committed entries** are written *inside* the canon transaction: the reason and intention behind a change that became canon. They land with the commit or not at all.
- **Standalone entries** are written by their own act, outside any transaction: rejected simulation branches, abandoned drafts and workflows, dismissed opportunities, production decisions of consequence, adjudications and overrides, and annotations. These record work that deliberately did *not* become canon — which is the most valuable content Memory holds, and it must not require a commit to exist.

Every entry declares its class, its authoring sequence, and its session (§12.16). The classes differ only in *when* they are written, never in authority.

### 22.6 Annotation Rules

An annotation is **additive** (it never edits an existing entry); it is **stamped** with its own authoring sequence, so *"I thought this in year one"* and *"I decided in year six that year one was wrong"* are never confused; and it may **contradict** an earlier entry, which is legitimate and valuable — a changed mind is a real event and is recorded as one, with both positions preserved and the later marked as superseding.

**The craft-ledger judgment is reviewable.** De-canonizing a lesson into transferable method is a judgment made by a role, and any judgment can be wrong in the direction that leaks world-specifics into a supposedly de-canonized ledger. Craft-ledger entries are reviewable and correctable-forward, and the craft ledger is linted for world-specific references at each epoch transition.

---

## 23. The Workflow Composer

The Workflow Composer is the front door for author intent — the primitive that turns a plain-language goal into a **multi-domain workflow graph**. It is not a task router that "picks a coworker." It remains a primitive; **nothing bypasses it** (Spine, law 10); and it **never commits canon**.

### 23.1 What the Composer Does

Given an intent, the Composer performs, invisibly:

1. **Interpret intent** — parse the goal; resolve what it refers to in canon; classify the kind of work.
2. **Decompose the goal** — break a composite intent into sub-goals.
3. **Extract constraints** — canon and Foundation limits, knowledge-state rules, saturation caps, authored withholding, recorded preferences.
4. **Determine required outcomes.**
5. **Identify required capabilities** — and no others.
6. **Resolve dependencies** — simulate the truth *before* scheduling its reveal.
7. **Build the workflow graph** — nodes are capability invocations; edges are data and sequence dependencies; branch points are the author's decision gates.
8. **Create a context plan** — hand the graph to the Context Builder so each node gets the smallest sufficient context.
9. **Sequence and route.**
10. **Preserve decision points** — surface every gate and genuine choice plainly; hide only the orchestration.

### 23.2 Intent In, Workflow Graph Out

| Author says | Composer composes (illustrative graph) |
|---|---|
| *"Simulate until this empire collapses."* | interpret → intent-directed Simulation (§15.3): identify pressures/thresholds → propose path + horizon + branches → timeline graph → author gates the accepted transitions. |
| *"Tell one mystery across five consecutive covers."* | decompose → Simulation (fix the hidden truth) → Editorial (5-cover arc + reveal schedule) → Knowledge-State (per-tier trajectory) → Studio (visual continuity plan) → Governance (per-cover readiness) → five gated production sub-workflows (§25). |
| *"Advance the succession crisis naturally."* | bounded timespan Simulation scoped to the crisis → Emergence surfaces resulting material → Editorial frames what to tell → gate. |
| *"Prepare the next issue."* | Editorial selects from the Opportunity queue and recommends → arc milestones loaded → department allocation (§17.12) → coherence precheck → Studio drafts → Governance evaluates → Reader Simulation → gate. |

The author chose none of the steps or their order.

### 23.3 What the Composer Never Does

It never asks the author to choose capabilities (if it does, it has failed P-13). It never commits canon. It never runs work off the record. It never hides a decision point. And it is not an engine — a new composite intent adds a new *mapping*, never a new domain.

### 23.4 Durable Workflows

A workflow is a **durable Production record** with an identity, a lifecycle, and provenance.

**Lifecycle:** *composed* → *running* → *awaiting-author* → *paused* → *resumed* → *completed* → *abandoned* (Operational Rollback, with a recorded reason).

**What a workflow record holds:** the originating intent in the author's own words; the composed graph and why it was composed that way; each node's status, outputs, and basis state (P-22); the decisions the author has already made inside it; the context plan; the accumulated Workflow State; and — **new in v0.5** — the **derivation chain**: for each produced artifact, which partition and which records the material was drawn from, in order.

**Why the derivation chain is recorded.** It is what makes §19.11's *canon-derived rather than society-derived* finding evidential rather than impressionistic. A piece whose chain reads *World → artifact* skipped Society and Epistemic Distribution (§8.5); a piece whose chain reads *World → Society → Epistemic → artifact* did not. Governance still renders a judged verdict — whether the result explains or depicts is a matter of meaning — but it renders it with a fact behind it, which is the §19.8 standard for any verdict at all.

**Realization (v0.6.3): the durable-execution pattern, native.** Persisted steps, replay from a durable record, and resumption with basis revalidation are implemented **natively and invoked on demand**. Durable-workflow platforms — those requiring a persistent server, worker fleet, or scheduler — are **REJECTED** for the constitutional workflow path (AC-2): a permanently-running worker contradicts P-11 and §28, and an engine owning retries and state transitions becomes a second thing that can advance canon. **No daemon, no scheduler, no background advance.**

**Resumption is by design, not by luck:** a workflow parked in March is resumable in September — with every basis re-validated on resumption and anything stale marked before the author is asked to continue. A workflow that cannot be re-validated is reported as unresumable, with what changed, rather than continued on stale ground.

### 23.5 Graph Contracts

Nodes exchange **structured Workflow State through the Context Builder**, and nothing else. Each node declares: its **inputs**, its **outputs**, its **current** (P-19), its **failure posture**, and whether it is a **gate**. A node that cannot obtain its declared inputs fails according to its current — it does not proceed on partial input and does not substitute assumptions.

### 23.6 Degraded Composition

In order: **retry** at reduced scope; **partial composition** (compose the ascending portion, park the descending portion, and say so); **manual ceremony** (the author supplies the decomposition by hand, at *higher* ceremony, audit-flagged); or **stop**, with a plain statement of what could not be composed. **An unavailable substrate is a different condition entirely**: it closes the descending current and none of these four paths is available, because all four are compositions. A Composer that cannot compose never guesses, and it never silently narrows an intent to something it can handle — that is a failure disguised as success.

---

## 24. The Context Builder

Context is expensive, and the system spends it deliberately. The Context Builder is the primitive that assembles, for every node of every workflow graph, **the smallest sufficient context** for that reasoning step — and nothing else (P-14).

### 24.1 The Structure

- **Shared Context Bundle** — the canonical facts, the workflow goal, and the constraints common to every step. Assembled once, from canon, the relevant continuity snapshot, and Creative Memory.
- **Derived Views** — role- and domain-scoped *projections* of the Shared Bundle, computed rather than re-fetched: an **Editorial View**, a **Reader View**, a **Studio View**, a **Governance View**, a **Simulation View**. Each is the minimum a role needs, derived from the shared bundle, so a fact is loaded once and projected many times.
- **Stage Deltas** — per-step, only the *change* in context since the previous step.
- **Workflow State** — the accumulating structured state passed between steps.

### 24.2 Minimum Sufficient Context, and Its Provenance

For each step the Builder assembles the relevant Derived View + the Stage Delta + the compact Workflow State — and records **provenance**: what was loaded and *why*. A fact in a step's context with no reason to be there is a defect, the same way a dangling graph edge is a defect.

### 24.3 Role-Scoped Context Is a Boundary

Because each role receives only its Derived View, a coworker *cannot* reason over canon outside its authority — not by policy alone, but because that canon was never placed in its context. Scope (Section 21.3) is enforced by what is loaded. The Canon Keeper's view holds the graph and contradictions; a persona-writer's view holds the brief, the voice, and the assigned clues — **and not the hidden solution**, unless the step legitimately needs it.

### 24.4 Why This Matters

**Less token waste** · **less cognitive drift** · **better reasoning** · **fewer context failures** · **more stable long workflows**. The rule: **build the smallest sufficient context for each reasoning step.**

### 24.5 Epoch-Aware and Task-Scoped Retrieval

Retrieval proceeds at the **cheapest sufficient layer** and stops there: **current task** → **current issue / current arc** → **current session** → **current epoch** → **epoch summaries** → **revision digests** → **full archive**. Deep layers are reached only when the question requires them, and the layer reached is recorded in the context's provenance — so an answer assembled from a summary is never mistaken for one assembled from the record. *Session is a retrieval layer as well as a history ordinal (§12.16): "what did I change last time" is the most frequent long-gap question the author asks, and it should cost one layer, not six.*

### 24.6 The Sufficiency Invariant Is Two-Sided

> **Including a fact the step did not need is a defect. Omitting a fact material to the step is a defect of the same class, and the burden of the judgment lies with the Builder.**

Three mechanisms make it operable. The Builder keeps an **exclusion log**: what was considered and deliberately left out, and on what basis. Every step's context carries **two-sided provenance**. And a role that finds its context insufficient **says so and stops** rather than reasoning around the hole — an insufficiency report is a normal, expected, non-embarrassing output, and treating it as a failure is what trains a system to guess.

### 24.7 Context Budget and Scope Integrity

**Budget.** Each step carries a declared context budget (P-14). Exceeding it is not solved by silent truncation but by *restructuring*: deeper derivation, a narrower view, or splitting the step. Truncation that drops content without recording what it dropped is prohibited.

**Scope integrity.** Withheld and hidden canon is **excluded by default** for every role, and inclusion requires an explicit, recorded justification naming the step that needs it — the default is closed, so a silent failure of judgment excludes rather than leaks. And every context assembly is checked for **leakage** (Section 14.16) against the epistemic record before it is handed to a role: a persona-writer's view containing a hidden solution is a **structural violation** (P-24), not a judgment call, and it blocks.

**The publication surface has an exposure set, and the Builder enforces it (v0.5).** What reaches the public surface (§27.5) is assembled by the same primitive under the same discipline, with the narrowest view in the system: the artifact and nothing else. Canon, schema, pipeline state, internal metadata, and epistemic records are excluded by default and cannot be justified in, because no step on that surface legitimately needs them. This is the one Derived View with no discretionary inclusion path at all.

---

## 25. Multi-Domain Workflow Orchestration

The most demanding author intents require many domains working together. coolboy12 handles them not with a new engine but by **composition**.

### 25.1 The Principle

A composite intent is decomposed into sub-goals, each mapped to existing capabilities, wired by their data and sequence dependencies, and punctuated by the author's decision gates. The domains do not know about each other's internals; they exchange **structured Workflow State** through the Context Builder. Orchestration is the Composer arranging capabilities; it is not a capability of its own, and it adds no domain.

### 25.2 Worked Case — *"Tell one mystery through the covers of five consecutive issues."*

```
INTENT: "one mystery, five consecutive covers"
   │  Workflow Composer decomposes → sub-goals, constraints, dependencies
   ▼
[1] SIMULATION ──────► fix the HIDDEN WORLD-TRUTH and its causal chain, so the
    (Section 15)        answer is real and consistent before any clue is planted.
                        Output: the true solution — an ordinary World record whose
                        reveal-state is HIDDEN (§13.6, §14.2).
   ▼
[2] EDITORIAL ───────► design the 5-cover ARC: what each cover tells, delays,
    (Section 17)        and foreshadows; the payoff schedule; the reveal on
                        cover five. Output: arc + per-cover editorial intent.
   ▼
[3] KNOWLEDGE-STATE ─► schedule the READER TRAJECTORY per tier across the five
    (Section 14)        issues; the clue economy and reveal-readiness curve.
                        Output: per-issue knowledge deltas + clue plan.
   ▼
[4] CREATIVE STUDIO ─► plan VISUAL CONTINUITY across the five covers: the motif
    (Section 18)        that recurs and accrues meaning, the symbol that only
                        resolves on cover five. Output: visual + symbolic plan.
   ▼
[5] (loop covers 1–5) each cover is a gated production sub-workflow:
        STUDIO produces the cover  →  GOVERNANCE checks correctness and quality
        →  READER SIMULATION estimates what each tier now knows  →  AUTHOR GATES.
   ▼
[6] CREATIVE MEMORY ─► records the arc's design, the rejected reveal timings,
    (Section 22)        and the intention, so the five-issue thread survives a
                        gap and the payoff isn't lost.
```

Every arrow is structured Workflow State moving through the Context Builder; every gate is the author's; nothing commits to canon except through the single transactional path. The hidden truth is fixed *once* (step 1) and never drifts; the reader trajectory (step 3) guarantees the casual reader gets a complete cover each month while the investigator gets a real, redeemable chain; visual continuity (step 4) makes the fifth cover's reveal land as *earned*. **Note what step 1 no longer does:** it does not create a `MYSTERY` object. It establishes a world fact and sets its reveal-state, which is what the work always was (§13.6).

### 25.3 Other Composite Pairings

**Simulation + editorial** · **editorial + reader-modeling** · **reader-modeling + visual continuity** · **visual continuity + studio production** · **governance + author decision points** · and, new in v0.5, **research + anchoring + editorial** (derive a real-world pattern, transform it into a counterpart with its recorded divergence, then decide how the publication would notice it). None of these is a new engine.

### 25.4 The Multi-Domain Execution Contract

1. **State moves only as structured Workflow State through the Context Builder.** No domain reads another's internals.
2. **Every node declares its current, inputs, outputs, and failure posture** (P-19).
3. **Every gate is the author's**, and gates are never batched across unrelated sub-goals.
4. **Every canonical write is a separate gated act** on the single path.
5. **The graph is durable**: pausable at any node, resumable with re-validated bases, abandonable by Operational Rollback.
6. **Partial completion is a legitimate end state.** A five-cover arc stopped after cover three leaves three published artifacts, a parked workflow, an accurate debt ledger, and a recorded reason — not an inconsistent world.

**Worked case, revisited under current rules.** The five-cover mystery additionally: fixes the hidden truth with a basis stamp (P-22); validates each cover's clue plan against the Fair-Play Validator before production; emits a Reader Knowledge Proposal after each issue rather than writing reader-state directly; binds each published cover to its canon basis; records its derivation chain per cover (§23.4); and survives a four-month pause with every basis re-validated on resumption. The composition is unchanged. What changed is that it can now be interrupted, audited, and trusted.

---

## 26. Ecosystem and Adapter Architecture

coolboy12 **orchestrates best-in-class infrastructure; it does not rebuild it.** Every external dependency is reached through an **adapter** with a stable contract. What coolboy12 owns is the *discipline* — what is authoritative, how it mutates, how it is provenanced, where the truth boundary sits.

### 26.1 One Reasoning Substrate, and Its Current Binding

The reasoning layer is not a marketplace of models. **Exactly one reasoning substrate is bound**, and the current binding is recorded here rather than in the constitution, because the identity is an adapter-level fact with a far shorter expected life than the document. P-15 fixes the *invariant* (exactly one substrate, no routing, no committee, no fallback); this section fixes the *identity*. Rebinding is an ordinary adapter change with a recorded reason — not a constitutional amendment — and it changes no canon, no history, and no guarantee (P-20). Roles are differentiated by *context and contract*, not by *model*.

### 26.2 The External Capabilities

| External capability | What it provides | What coolboy12 keeps |
|---|---|---|
| **Agentic execution & reasoning** | The reasoning runtime and workflow execution | The intent model, the Composer, the gates, the provenance — and the sole-substrate discipline |
| **Versioning / integrity** | Append-only, hash-chained history and recovery | The transactional mutation path and the ledger discipline |
| **Canon store** | Durable storage of the record and the graph | What is authoritative and how it mutates |
| **Read / navigate surface** | A place to browse the vault | The rule that a hand-edit is *not* a canon mutation |
| **Image generation** | Visual asset rendering | The prompt framework, the visual canon, the continuity rules |
| **Asset storage** | Versioned binary storage of media | Content hashing, provenance, which asset serves which canon |
| **Publication rendering** *(v0.5)* | Presentation of the artifact model on the public surface | The artifact model itself (§18.9), and the exposure set (§27.5) |
| **Research tools** (optional) | Retrieval of external evidence | What is indexed, boundary enforcement, result provenance |

This blueprint names no providers, no products, and no formats for any row. Selecting them is implementation work and is out of scope by construction.

**What coolboy12 never delegates:** enforcement, human authority, provenance discipline, epistemic discipline, and the truth boundary. Those are the core, and the core is not for sale to a plugin.

### 26.2a Repository Compatibility — The Governing Principle (v0.6)

*(ADDED. Source: authorial decision. Architectural consequence: none — this constrains implementation, not architecture. That is the point.)*

> **Repositories provide capabilities. They do not define coolboy12 semantics.**

The system will eventually be built largely out of components it did not write, and the failure mode is not that a component is bad — it is that a component is *good*, and the architecture quietly reshapes itself around what that component finds natural. A graph store makes relationships cheap and edge ownership invisible; a document store makes nesting cheap and partitions optional; a content system makes pages cheap and the firewall inconvenient. Each of those is a fine tool and a bad constitution.

**Every serious candidate is assessed on eleven axes before adoption:** capability · architectural location · integration boundary · input contract · output contract · source-of-truth status · replacement strategy · licence · maintenance risk · semantic leakage risk · exit strategy. And on one question that outranks the other eleven: **does this component change the architecture, or serve it?** A component that changes it is rejected however well it works.

**Every candidate receives exactly one disposition:** `ADOPT` · `ADAPT` · `WRAP` · `COMPOSE` · `FORK` · `BUILD-NATIVE` · `DEFER` · `REJECT`.

**Two rules on how those dispositions are reached.** *A component is never marked `ADOPT` merely because it works* — working is the entry requirement, not the argument. And *a component is never forced into the architecture if the architecture becomes worse for it* — the correct response to a good tool that does not fit is to not use it.

### 26.2b Build-Native Boundary (v0.6)

**coolboy12 stays native wherever a capability contains coolboy12-specific semantics.** Not because native code is better, but because these are the places where an external component would have to be *told* what the system means, and a component that has been told what things mean has become the definition.

**Native, without qualification:** the Record System and its six Record Models · the Record envelope · identity grammar · **the World Record package — Record, Relationship Record, History Record, WSV, WSV-H** *(World Record Model constructs, §13.9; an adapter must not assume them in another model)* · Registry semantics and the definition–ownership boundary (§13.6e) · mutation rules · the Human Gate · canonization · World Time semantics · partition boundaries · Issue semantics · publication semantics · the provenance model · the Mutation Coordinator (Section 12.6).

**Externalisable where safe, behind an adapter:** graph traversal · image processing · rendering and layout · indexing · querying · validation engines · numerical computation · file processing · version control · full-text search.

The line between the two lists is not effort and is not maturity. It is whether the thing being computed *is* a coolboy12 meaning or merely *operates on* one. Traversing a graph is generic. Deciding which endpoint owns an edge is not.

### 26.2c The Adapter Rule (v0.6)

Every external component sits behind an adapter, always, including where direct use would be simpler:

```
coolboy12 interface
        ↓
     adapter        translates data structures · identifiers ·
        ↓           error handling · lifecycle · capability boundaries
external component
```

**The adapter must not silently redefine semantics.** Where a component's model and coolboy12's disagree, the adapter translates and — if the translation is lossy — **says so** rather than choosing a lossy reading and proceeding. An adapter that quietly resolves a semantic mismatch has moved the definition into the adapter, which is the same failure as moving it into the component, with an extra layer of concealment.

### 26.2d The External Store Rule (v0.6)

Where an external database, index, graph store, or search engine is used, the direction of derivation is fixed:

```
canonical records  →  projection / index builder  →  external store
```

and never:

```
external store  →  canon
```

**The system must remain fully recoverable if the external store is deleted.** That is the operative test, and it is not a disaster-recovery provision — it is how the boundary is *verified*. A store that cannot be deleted and rebuilt has become part of the canon whether or not anyone intended it.

**Consequence for the source-of-truth classification (Section 29.6):** every external store is `DERIVED` or `CACHED`. There is no configuration in which one is `AUTHORITATIVE`.

### 26.2e The Version-Control Boundary (v0.6)

*(CLARIFIED — stated because the overlap is real and the conflation is inviting.)*

A version-control system genuinely provides: repository versioning · rollback · commit identity · implementation history · integrity of file contents. Those are valuable and coolboy12 should use them.

**It does not provide, and must never be treated as providing:** History Record · WSV-H · semantic history · canon state.

The distinction is not about capability, it is about *subject*. A commit records **that a file changed**; a History Record entry records **what canonically changed, why, at whose approval, caused by what, in which session** (Section 12.9). A commit history can tell you a character's file was edited eleven times. Only History Record can tell you which of those eleven were canonical revisions, which were formatting, which were reverted, and what the world was before each.

**Where useful, History Record and WSV-H entries may reference commit or session information** — a correlation, recorded deliberately, in that direction. The reverse — reconstructing semantic history by reading the commit log — is prohibited, because it would make the record of the *files* into the record of the *world*.

### 26.2f Dependency Exit Test (v0.6)

Every external dependency answers five questions before adoption, and the answers are recorded in its adapter contract (Section 26.3):

1. If this component disappeared tomorrow, **what breaks?**
2. **What remains?**
3. **Can canon still be read?**
4. **Can the capability be replaced?**
5. **How difficult is the migration?**

**A `CRITICAL` semantic dependency — one where the honest answer to question 3 is "no" — is not adopted.** Not mitigated, not accepted with a plan: not adopted. This is the Exit Invariant (P-27) applied at selection time rather than discovered at failure time.

### 26.2g Benchmark and Licence Requirements (v0.6)

**BENCHMARK REQUIRED.** Where several components provide an equivalent capability, the choice is made against **actual coolboy12 workloads**, not against general reputation or published benchmarks on unrelated shapes. The workloads that decide it: Record retrieval · Relationship Record traversal · History Record history queries · WSV reads · WSV-H history · Registry validation · temporal queries · search · indexing · publication generation · asset processing · Issue assembly. **A choice is never frozen because a tool is popular.**

**LICENCE REVIEW REQUIRED.** Every serious dependency is reviewed for: licence · commercial compatibility · modification requirements · distribution implications · network-service implications where relevant · plugin obligations · fork implications · long-term maintenance. **Open source does not automatically mean safe** — copyleft reach, source-availability licences with future conversion dates, and abandoned-but-permissive components each carry a different risk, and all three are common.

**MAINTENANCE IS A SELECTION CRITERION, NOT A FOOTNOTE.** This system is designed to run for decades under one author. A component that is unmaintained, recently archived, or dependent on a single sponsor's continued interest is a liability proportional to how deeply it sits in the stack — which is another argument for keeping semantics native and dependencies shallow.

### 26.2h The Integration Compatibility Rule (v0.6.2)

*(ADDED. The rule under which v0.6.2 was written, stated before its results so the results can be checked against it.)*

```
COOLBOY12 contract  →  adapter boundary  →  external capability
```

**The architecture remains upstream.** An adapter translates *toward* the component; it never translates the architecture *toward* the component's model.

> **If an external component requires a semantic change to coolboy12, that change is not made. The requirement is recorded as an ARCHITECTURAL CONFLICT and resolved as OPEN, REJECT, or BUILD-NATIVE — never as a silent accommodation.**

This is stricter than the adapter rule (§26.2c), which governs translation of *data*. This governs translation of *meaning*, and forbids it. The five conflicts this rule caught in v0.6.2 are recorded at §26.7 — they are the most useful output of the exercise, because a conflict refused is a semantic the system still owns.

### 26.3a Adapter Contract Specifications (v0.6.2)

Every external capability attaches at exactly one boundary, and every boundary declares the same eight things: **what coolboy12 requires · what the component supplies · what it does not supply · its source-of-truth class · its input and output contract · its degraded mode · its exit path · its benchmark gate.**

| # | Boundary | coolboy12 requires | Component supplies | Does **not** supply | Class | Degraded mode | Exit path |
|---|---|---|---|---|---|---|---|
| A-1 | **Deconstruction adapter** (§17.18) | Real publications → structured observations | Document parsing, OCR, layout analysis, reading order, table and article extraction | Typographic interpretation, editorial pattern extraction, taste semantics — all native | **EXTERNAL** | Corpus ingestion stops; existing corpus fully usable; no other capability blocked | Outputs are plain structured records; replace the parser, re-ingest |
| A-2 | **Vision analysis adapter** (§18.11) | Image → observation record in V | Embeddings, classification, similarity vectors, described content | Visual canon, continuity judgment, the proposal path — all native | **DERIVED** | Visual analysis unavailable; continuity checks fall back to manual; assets and specifications unaffected | Observations are records; re-analyse under a new model |
| A-3 | **Visual index adapter** (§18.11) | "All depictions of X"; likely duplicate; prior depiction | Vector index, nearest-neighbour retrieval | Which depiction is canonical — that is the specification | **DERIVED** | Retrieval degrades to enumeration over V | Delete and rebuild from V |
| A-4 | **Search index adapter** (§12.15) | Structural questions in the author's vocabulary, returning objects, paths, and provenance | Full-text and structural indexing, ranking | Author vocabulary, provenance semantics, the no-synthesized-answer rule — all native | **DERIVED** | Search degrades to direct traversal; nothing blocks | Delete and rebuild from canon |
| A-5 | **Causal-graph traversal adapter** (§15.19) | Traverse declared model dependencies; find paths, cycles, reachability | Graph algorithms | The edges — those are Relationship Record and Registry model definitions | **DERIVED** | Traversal degrades to direct Relationship Record walk | Rebuild the graph from Relationship Record and model definitions |
| A-6 | **Simulation numerics adapter** (§15.17) | Execute a Registry-defined model over a horizon | Agent-based, system-dynamics, and discrete-event execution | Model **definitions**, cross-model ordering, conflict resolution, observability — all native | **TEMPORARY** (Working) | The affected model family cannot run; other families continue; the run reports what it could not compute | Definitions are Registry records; re-implement execution |
| A-7 | **Sensitivity and calibration adapter** (§15.21) | Sweeps, sensitivity indices, stability findings | Numerical methods | Which findings matter, and what they may not override (I-94) | **DERIVED** | Advisory findings unavailable; runs proceed unadvised | Findings are records; swap the method library |
| A-8 | **Rendering adapter** (§18.9) | Artifact model + authored material specification → page images | Layout, pagination, rasterisation, image operations | The material specification, which is authored (§18.9 rule 1) | **DERIVED** | Rendering unavailable; the issue plan and artifact model are unaffected | Specification is a record; re-render under a new engine |
| A-9 | **Index/query store adapter** (§12.15) | Fast lookup and analytical projection over canonical records | Query execution, indexing, aggregation | Canonical state — it is read from canon, never from the index | **DERIVED** | Read-only degradation to direct canon reads | **Delete the store and rebuild (§29.8)** |
| A-10 | **Public viewer adapter** (§27.5) | Page-by-page presentation of published artifacts, and nothing else | Deep-zoom image presentation, static page delivery | Everything else — see the exposure set | **DERIVED** | The surface serves static pages without zoom | Artifacts are images; replace the viewer |
| A-11 | **Version-control adapter** (§26.2e) | File versioning, rollback, commit identity, integrity | Repository history | History Record, WSV-H, semantic history, canon state (I-85) | **AUTHORITATIVE for files, never for meaning** | Versioning unavailable; canon remains readable and mutable | Canon is plain records; the repository is not the record |

**Two contract obligations apply to every row.** A component that cannot supply its declared output **says so and stops** rather than supplying a degraded output silently (§21.7). And every boundary's exit path is **tested, not asserted** — the rebuild drill at §29.8 is where that happens.

### 26.3b Normalized Component Metadata (revised)

*(ADDED by revision. The realization blocks in §§12.15, 15.17, 15.19, 15.21, 17.18, 18.9, 18.11, 22, 23.4 and 27.5 carry each component's contract in prose; this table normalizes the fields that were unevenly present, so that no component is missing a version policy, an authority statement, or a benchmark status. **No repository was added, removed, or re-dispositioned.**)*

| Repository | Capability | Disp. | Purpose | Input | Output | Adapter | Authority | SoT class | Failure mode | Version policy | Exit / replacement | Benchmark |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Docling | 66 deconstruction | ADAPT | Document parsing, OCR, layout, article/table extraction | Publication file | Structured observations | A-1 | **none** | EXTERNAL | Ingestion halts; corpus usable | Pin minor; re-verify licence at adoption | Outputs are plain records; swap parser, re-ingest | Required — pages/min, layout accuracy, CPU-only |
| Surya | 66 alt OCR | WRAP | Alternate OCR/layout stage | Page image | OCR + layout | A-1 | **none** | EXTERNAL | Falls back to primary parser | Pin exact; **re-check weight licence and on-demand server** | Drop; primary parser continues | Required — same suite |
| OpenCLIP | 73 image understanding | ADAPT | Image/text embeddings, zero-shot labels | Visual asset | `VISUAL-ANALYSIS` record | A-2 | **none — observation only** | DERIVED | Analysis unavailable; manual continuity | Pin model + code separately; weight licences vary | Re-analyse under new model | Required — observation quality vs author judgment |
| FAISS | 75 visual retrieval | ADOPT | Derived embedding index | Embeddings | Ranked candidates | A-3 | **none** | DERIVED | Falls back to enumeration | Pin minor | Delete and rebuild from V | Required — recall@k, latency, rebuild time |
| LanceDB | 75 alternative | COMPOSE | On-disk derived index | Embeddings + metadata | Ranked candidates | A-3 | **none** | DERIVED | As FAISS | Pin exact; **format lock-in risk** | Rebuild from V into another index | Conditional — only if FAISS insufficient |
| SQLite + FTS5 | 1–7, 88 index/search | ADOPT | Derived index, full-text and structural | Canonical records | Indexed projections | A-4 / A-9 | **none** | DERIVED | Read-only degradation to direct canon reads | Track stable; no pin needed | **Rebuild drill §29.8** | Required — Record retrieval, Relationship Record traversal, History Record queries |
| DuckDB | 1–7 analytics | ADOPT | Analytical projections | Canonical records | Aggregations | A-9 | **none** | DERIVED | Analytics unavailable | Pin minor | Delete and rebuild | Required — projection build time |
| Tantivy | 88 alternative | ADOPT-alt | Embedded full-text | Canonical records | Ranked results | A-4 | **none** | DERIVED | As FTS5 | Pin minor | Delete and rebuild | Conditional — only if FTS5 insufficient |
| NetworkX | 43 graph traversal | ADOPT | Traversal over the rebuilt causal graph | Graph from Relationship Record + model defs | Paths, cycles, reachability | A-5 | **none — edges live in Relationship Record** | DERIVED | Falls back to direct Relationship Record walk | Pin minor | Rebuild graph; swap library | Required — path latency; **engine-switch threshold** |
| rustworkx | 43 alternative | ADOPT-alt | Faster traversal | As NetworkX | As NetworkX | A-5 | **none** | DERIVED | As NetworkX | Pin minor | Swap back | Conditional — gated on the threshold |
| Mesa | 38–40 ABM | ADAPT | Agent-based model execution | Registry model def + state | Candidate deltas | A-6 | **none — definitions are Registry** | TEMPORARY | Family cannot run; others continue | Pin minor; **bundled viz server unused** | Definitions persist; re-implement execution | Required — wall-clock/simulated year |
| PySD | 38–40 SD | ADAPT/COMPOSE | System-dynamics execution | Registry model def + state | Candidate deltas | A-6 | **none** | TEMPORARY | As Mesa | Pin exact; **source-dialect dependency** | Re-implement in native SD | Required — same suite |
| SimPy | 38–40 DES | ADOPT | Discrete-event execution | Registry model def + state | Candidate deltas | A-6 | **none** | TEMPORARY | As Mesa | Pin minor | Re-implement | Required — same suite |
| SALib | 45–46 sensitivity | ADOPT | Sobol/Morris/sweeps | Model + parameter ranges | Sensitivity indices | A-7 | **none — advisory** | DERIVED | Findings unavailable; runs proceed | Pin minor | Swap method library | Required — method agreement on a known model |
| Pillow | 81 image ops | ADOPT | Image I/O and manipulation | Page raster | Processed raster | A-8 | **none** | DERIVED | Rendering unavailable | Pin minor | Swap library | Required — render time/page |
| scikit-image | 81 image ops | ADOPT | Filters, morphology, restoration | Raster | Processed raster | A-8 | **none** | DERIVED | As Pillow | Pin minor | Swap library | Required — fidelity to spec |
| ImageMagick / Wand | 81 effects | WRAP | CLI-expressed print effects | Raster | Processed raster | A-8 | **none** | DERIVED | Effect unavailable; page still renders | Pin exact | Reimplement effect natively | Optional |
| halftone module | 81 halftone | FORK | Halftone effect | Raster | Halftoned raster | A-8 | **none** | DERIVED | Effect unavailable | **Vendored — no upstream dependency** | Already vendored | Optional |
| JSON Schema | 15–17, 86 validation | ADOPT | Structural field validation | Records + schema | Verdicts | — | **structural only** | DERIVED verdict | **Descending current closes** (P-19) | Track spec version | Swap validator | Required — validations/sec |
| LinkML | 15–17 registry authoring | ADAPT | Author vocabularies in legible YAML; generate validators | Registry definitions | Generated schemas | — | **none — Registry owns meaning** | DERIVED artifact | Hand-author schemas | Pin minor | Definitions remain legible YAML | Required — expressiveness gaps logged |
| OpenSeadragon | 101 public viewer | ADAPT | Deep-zoom page presentation | Page images / tiles | Rendered view | A-10 | **none** | DERIVED | Static pages without zoom | Pin minor; **library affordances disabled** | Replace viewer; artifacts are images | Required — **exposure-set audit** |
| Hugo | 101 static delivery | ADOPT | Emit published page artifacts | Page images + manifest | Static site | A-10 | **none** | DERIVED | Manual static delivery | Pin minor; **no taxonomies, no search index** | Swap generator | Required — exposure-set audit |
| Eleventy | 101 alternative | ADOPT-alt | Static delivery | As Hugo | As Hugo | A-10 | **none** | DERIVED | As Hugo | Pin minor | Swap generator | Conditional |
| Version control | 26 file history | ADOPT | File versioning, rollback, integrity | Canonical files | Commit history | **A-11** | **files only, never meaning** (I-85) | AUTHORITATIVE for files | Canon remains readable and mutable | Document version and hash mode | Canon is plain records | Required — **History Record-independence check** |

**Rejected, recorded so they are not re-proposed:** server-based vector stores · server-based search · embedded graph databases as edge stores · durable-workflow platforms · server-based transparency logs · any browsable database surface on the public side (§26.7).

### 26.7 Architectural Conflicts Recorded and Refused (v0.6.2)

*(ADDED. Five candidate components would each have required a semantic change. Each is recorded here with the change it wanted and the resolution, per §26.2h.)*

| # | The component wanted | Which semantic it would have taken | Resolution |
|---|---|---|---|
| **AC-1** | An embedded graph database as the relationship store, holding edges natively with its own edge model | **Relationship authority.** Edges would live in the store; Relationship Record would become a projection of it, inverting §13.9's ownership rule and making the store the answer to *what relates to what* | **REJECT.** Graph capability is adopted as **traversal over a graph rebuilt from Relationship Record** (A-5). The store may compute; it may not hold. *(Independently reinforced by the audit's maintenance finding on the leading candidate — but the refusal stands on the semantics, not on the abandonment.)* |
| **AC-2** | A durable-workflow engine with a persistent server, worker fleet, and scheduler | **Mutation authority and dormancy.** A workflow engine that owns retries and state transitions becomes a second thing that can advance canon; a permanently-running worker contradicts P-11 and §28 | **REJECT → BUILD-NATIVE.** The *durable-execution pattern* — persisted steps, replay from a durable record, resumption with basis revalidation — is adopted as a pattern in §23.4 and implemented natively, invoked on demand. No daemon, no scheduler, no background advance. |
| **AC-3** | A search or database browsing surface exposed publicly | **The exposure set.** Table views, per-record URLs, faceted search, and metadata are precisely what §27.5 enumerates as forbidden | **REJECT.** Such tools are legitimate on the **operator** surface (A-4, A-9) and prohibited on the public one. The boundary is not a configuration option. |
| **AC-4** | A vector or document store holding canonical records natively, as the primary store | **Source of truth and legibility.** Canon would live in an opaque format, readable only through the component, violating P-27 and the deletability requirement | **REJECT.** All such stores are **DERIVED**, rebuilt from legible canonical records (A-3, A-9). Canon remains legible without the running system. |
| **AC-5** | A retrieval or agent framework owning memory, context assembly, and role state | **Creative Memory and the Context Builder.** Both are primitives with constitutional obligations — two-sided provenance, an exclusion log, no silent truncation, one bound substrate (P-15, I-59) | **BUILD-NATIVE.** A thin retrieval library may sit behind the Context Builder; the assembly, provenance, and exclusion semantics are coolboy12's and stay so. |

**What these five have in common.** None was refused for being immature, unmaintained, or slow. Each was refused because adopting it would have moved a *meaning* out of coolboy12 — which is the only refusal criterion §26.2h recognises, and the reason the audit's maintenance findings, however useful, were never the deciding argument.

### 26.3 Adapter Contracts and the Exit Invariant

Every adapter contract declares five things: **what it provides**, **what it may never decide**, **its degraded mode**, **its exit path**, and **its volatility class**.

> **The Exit Invariant (P-27): no external dependency may hold canon, History Record, Production State, or Creative Memory in a form the system cannot fully recover without that dependency.**

**Substrate-independent legibility.** Canon and its records must be readable by a human, directly, without the application — structured text a person can open in ten years and understand. A single-author archive whose contents are hostage to its own software has failed at the one thing the whole system exists for. Derived projections are exempt; they are rebuildable by definition. Assets are exempt from legibility but not from recovery.

**Volatility ranking.** The most volatile dependency is the reasoning substrate, then image generation, then publication rendering, then retrieval; the least volatile is the canon store. Contract thinness follows volatility — the substrate's contract is the thinnest in the system, which is what makes rebinding cheap.

### 26.8 The Claude Code Execution Environment (v0.6.3)

*(ADDED. Placed in the Ecosystem section, where every other external capability is specified, and deliberately **not** given a section of its own — a top-level section would imply architectural standing that P-33 denies.)*

coolboy12 is built and operated inside **Claude Code**. This subsection states what that provides, what it must never own, and how the constitutional boundaries survive contact with it.

**What the environment provides.**

| Facility | Used for |
|---|---|
| **Workspace / repository** | The coolboy12 project tree: native source, Registry definitions in legible files, canonical records, adapters, prompts, tests, and configuration |
| **Filesystem access** | Reading and writing project files under the permission boundary below |
| **Command execution** | Running validators, index builds, simulation runs, rendering, and tests |
| **Runtime and packages** | The language runtime and the audited external components of §26.3a |
| **Version control** | File history, rollback, commit identity, integrity — **and nothing semantic** (§26.2e, I-85) |
| **Code generation and editing** | AI-assisted implementation of native coolboy12 code |
| **Role-scoped reasoning** | The AI coworker roles of §21, executed as configured contexts under the single-substrate rule (P-15) |
| **Hooks** | Deterministic pre-action enforcement — see the permission boundary |
| **Commands** | Repeatable entry points for recurring work: propose, validate, simulate, render, rebuild |
| **Persistent files** | Project conventions, invariants, and standing instructions that survive between sessions |

**The workspace layout follows the architecture, not the tooling.** Canonical records live in legible files organised by partition (`W`, `E`, `P`, `R`, `V`, `I`); Registry definitions are legible and versioned; derived stores live in a directory that can be **deleted in its entirety** and rebuilt (§29.8); adapters sit at named boundaries matching §26.3a. A reader opening the tree without the environment can still read the world (P-27).

**The permission boundary.** The environment's own guard rails are used, and are used as **defence-in-depth, never as constitutional authority** (§12.6).

- **Canonical records and Registry definitions are write-protected against direct edit.** Every canonical write goes through the Mutation Coordinator. A hook that denies direct writes to those paths is the deterministic expression of Spine law 2 — and if the hook and the Human Gate ever disagree, **the gate is right and the hook is a bug**.
- **Derived stores are freely writable**, because they are rebuildable by definition.
- **Proposals are freely writable.** AI-assisted work drafts into a proposal area; nothing there is canon until it passes the gate.

**What the environment writes, proposes, and may never change.** It **writes** native source, tests, adapters, prompt and role files, and staged proposals. It **proposes** canon mutations, issue plans, drafts, material specifications, and simulation scenarios. It **may never directly change** any Record, Relationship Record, History Record, WSV, WSV-H, Registry definition, epoch baseline, or published artifact. The author **must review** every canonization, every Registry change, every reality anchor, every promoted simulation result, and every published artifact.

**Local-first, on demand, dormancy-tolerant.** Nothing runs unattended. There is no scheduler, no daemon, no background advance of the world (§28, AC-2). The system is operated in sessions, and **session** is already a canonical ordinal (§12.16) — the environment's working sessions and the blueprint's authoring sessions are the same unit seen from two sides, which is why the vocabulary needed no addition.

**Recovery and rebuild.** After dormancy: the runtime and packages are reinstalled, derived stores are rebuilt from canon (§29.8), parked workflows are resumed with every basis revalidated (§23.4), and the return briefing is produced (§28.2). **Canon requires no recovery, because it was never held anywhere that could fail** — this is P-27 doing the work it exists for.

**What the environment must never own.** Canon · the Registry · Simulation semantics · Epistemic semantics · Production semantics · Visual Library semantics · Issue semantics · Governance semantics · the mutation boundary · the Human Gate. **The environment runs coolboy12; it does not define coolboy12** (P-33). Every one of those is native by construction, and the test that it has stayed that way is §29.7: remove the environment's name from this blueprint and the architecture must still stand.


---

## 27. Single-Author UX Principles

The system is worthless if one person cannot operate it. UX is a first-rank concern, peer to canon integrity. The two primitives make this real: the author holds *intent*, and the Composer and Context Builder hold *everything else*.

### 27.1 The Author's Vocabulary

The author thinks — and the surface speaks — in exactly these terms: **Universe · Canon · Issue · Mystery · Character · Decision · Timespan · Publish.** The author never thinks in, and the surface never exposes, protocols, registries, layers, internal IDs, severity codes, adapters, Composer internals, or models. The author addresses the world by meaning, navigates by intent, and drives work by goal.

**A note on "Mystery" (v0.5).** The word stays in the author's vocabulary even though `MYSTERY` is no longer an object kind (§13.6). This is deliberate and is exactly what §27.1 is for: the author says *"the succession mystery"* and the system resolves it to a world fact plus its reveal-state and evidence chain. **A vocabulary term is a way of addressing the world, not a schema entity**, and the two were never required to match. Removing the word because the kind went would be the tail wagging the dog.

### 27.2 The Binding Principles

- **Truth first.** Every surface's first duty is to show the true state of canon, provenance, and uncertainty. A draft is never rendered as canon; a belief never as world-truth; a published claim never as canonical fact; a simulated timeline never as committed history.
- **Show the epistemics — and the knowledge-state.** The surface keeps the kinds of truth distinct *and* makes knowledge-state legible: what is true vs. what the world, a character, or a reader tier knows.
- **Progressive disclosure.** The default view is the minimum that lets the author act correctly; depth is on demand.
- **Interaction never creates truth.** No click, command, or conversation makes anything canon. Every write is a gate approval on the single path; the surface originates nothing.
- **Recoverable always.** Canon is fixed by a new gated change, never a destructive undo.
- **Explainable always.** Any state, verdict, recommendation, or simulated transition traces to its source and reasoning.
- **Evolution is observable.** Any canonical state can be asked how it came to be, and the answer is drawn from history, never mistaken for current truth.
- **Rollback is a gated change, never an undo.**
- **The human decides.** The surface presents options, timelines, and challenges; it never decides on the author's behalf.
- **Assumptions are labelled.** Anything the system estimated rather than observed — above all reader-state (§20.6) — is shown as an assumption.
- **Reduced is shown as reduced.**

### 27.3 Vocabulary Growth

**A capability the author cannot name does not exist for them.** Adding an author-facing capability obliges either a vocabulary term or an explicit statement that it is staff-facing only.

The vocabulary, with v0.4's three additions and v0.5's one: **Universe · Canon · Issue · Mystery · Character · Decision · Timespan · Publish · History · Epoch · Review · Session.**

*History* covers everything in §§12.9–12.11 — the author says "show me the history of this" and never says History Record, replay, revision digest, or reversion-versus-rollback. *Epoch* is a word the author must learn, and it earns its place because they choose when one ends. *Review* covers preflight, continuity review, verdicts, and health. **Session** *(v0.5)* is added because the author already thinks in work-sittings and now asks the system in them — *"what did I change last session"* is the most common return question there is, and it had no word (§12.16, §24.5). Everything else — basis states, causal closure, partitions, Relationship Records, derivation chains, anchors — is machinery beneath the vocabulary and is never exposed as jargon.

### 27.4 Legible State

At any moment the author can see, in their own vocabulary: what is true (canon), what is proposed and awaiting them (the gate queue with its severities and scopes), what is running or parked (durable workflows), what is wrong (Canon Health), what is owed (narrative and knowledge debt), what each tier knows (labelled as an assumption), and where they are in the epoch and the session. This is the whole system's state in seven readings, and it is the only dashboard the constitution requires.

### 27.5 The Two Surfaces (v0.5)

There are two products, and conflating them is the single most likely way the entire artifact ambition fails. They share a universe and share nothing else.

| | **Surface 1 — coolboy12** | **Surface 2 — The Overtone** |
|---|---|---|
| Who it is for | The author, alone | The public |
| What it is | An operator and authoring environment | A publication artifact, presented |
| Governed by | §§27.1–27.4 | This subsection and §18.9 |
| Shows | Canon, provenance, uncertainty, health, the gate queue, epistemics, machinery | The artifact. Nothing else. |
| Success looks like | One person operating a decade-scale world without drowning | A reader forgetting there is a system at all |

**Surface 2 is a publication viewer, not an application.** This is a design constraint, not a stylistic preference. Conventional application affordances — navigation chrome, search over content, filters, entity pages, related-links, infinite scroll, a database made browsable — are all mechanisms for delivering *information about* a corpus, and every one of them converts an artifact back into a database with a skin. What the surface renders is the artifact model (§18.9): pages in order, spreads that face each other, an object with a physical character, turned rather than queried.

**The exposure set.** Surface 2 sees exactly one thing: published artifacts and their in-artifact content. Enumerated because a prohibition that is not enumerated is a prohibition that erodes — Surface 2 must never expose:

- the canon database, or any query over it;
- internal schemas, kinds, partitions, or IDs;
- the production pipeline, workflow state, or plans;
- hidden metadata of any kind;
- authoring controls, gates, or proposals;
- **internal epistemic state** — reveal-states, evidence chains, knowledge trajectories, what is withheld and from whom;
- implementation architecture.

The last is the sharpest. A surface that exposed reveal-state would tell a reader which facts are load-bearing, which is precisely the information the entire Knowledge-State Architecture exists to control the release of. This is enforced by the Context Builder as a structural violation (§24.7), not by policy — the public surface's view has **no discretionary inclusion path**, which is the only way a prohibition of this consequence survives a decade of feature requests.

**Realization (v0.6.3).** **OpenSeadragon** (`openseadragon/openseadragon`, BSD-3-Clause) — **ADAPT** — supplies deep-zoom page presentation behind adapter A-10, **with its library-style affordances disabled**: no manifests, no collection browse, no navigator metadata, no page-turner chrome. **Hugo** (Apache-2.0) — **ADOPT** — emits the static pages, configured to produce **only** published page artifacts: no taxonomy pages, no client-side search index, no feeds of internal content. **Eleventy** (MIT) is the alternative. Library and archive viewers that expose manifests, tables, or search are **REJECTED** for this surface regardless of quality (AC-3) — the exposure set is not a configuration option.

**One-directional, always.** Surface 2 reads published artifacts. It writes nothing anywhere. Reader signal, where a channel exists at all, enters through an ordinary adapter and lands in Production State (§20.8) — never through this surface into anything.

**Why the boundary is here and not in a section of its own.** The two-surface distinction is a *UX* fact about who is being served, not a new domain (§9.3: Publication fails the admission criterion because its question — *what should the reader receive and in what form* — is already Editorial's). Placing it here keeps it next to the author-facing principles it is defined against, and prevents the public surface from acquiring an architecture of its own, which is how it would drift back into being an application.

---

## 28. Return After Dormancy and Continuity Intelligence

Dormancy is expected, not failure (P-11). On return, the latest **continuity snapshot** reconstructs the operational state of the universe in one sitting; **Creative Memory** answers *why* the world is the way it is and *what was rejected and why*; the **changelogs** answer *how* it got here in sequence; and the AI staff produces a **return briefing**.

The knowledge-state model means a returning author instantly sees what each reader tier currently knows — so they never accidentally re-reveal or contradict. The Creative Memory debt-history means outstanding narrative debt is explicit. And because the Context Builder reconstitutes long-horizon context from snapshots and memory rather than from full history, the return briefing is cheap to produce. A three-year absence should cost a handful of sessions to recover from, not weeks.

### 28.1 System Dormancy

Over three years the machine will not be waiting as it was left: the reasoning substrate will have changed or vanished, adapters will have broken, formats will have aged. The harder recovery question is not *what was I doing* but **does this still run, and is my universe still readable.**

Three guarantees answer it. **Canon survives the system** (P-27, §26.3): canon, History Record, WSV-H, Production State, and Creative Memory are legible without the application, so the worst case is a rebuild of tooling around an intact universe — never a lost world. **Every adapter has a declared exit path**, so a discontinued service is a migration, not a catastrophe. And **no guarantee depends on the substrate** (P-20).

### 28.2 Recovery Snapshots and the Return Briefing

The **epoch baseline** is the primary recovery artifact. Continuity snapshots remain the finer-grained operational record within an epoch, and **session** is the finest (§12.16).

The return briefing is read in this order: **where the world stands** (baseline plus everything since); **what happened while you were away** (epoch summary — major transitions, retcons, reversions, refactorings); **what is unfinished** (parked workflows with their re-validated bases); **what is owed** (narrative and knowledge debt, including anything written off in your absence); **what is wrong** (Canon Health, including anything that went stale or unresumable); **what readers know** (per tier, labelled as assumption); **what was deliberately left open** (§14.5, so an intentional ambiguity is never mistaken for a loose end); and **the highest-leverage next moves**. Long absences are also when the system reports its own decay honestly: which adapters no longer respond, which projections are stale, and which capabilities are running reduced.

### 28.3 Degraded Modes, Named

| Mode | Trigger | Descending current | Ascending current |
|---|---|---|---|
| **Full** | Everything available. | Normal. | Normal. |
| **Reduced** | A non-essential adapter or check is unavailable. | Proceeds if all *required* checks ran; otherwise stops. | Proceeds, marked reduced, with what was missing. |
| **Read-only** | Substrate unavailable, or no Authority present (§10.1). | **Closed.** Nothing commits, and **Manual Ceremony is unavailable** — it is a composition, and composition needs the substrate. | Canon, history, replay, search, and dashboards all remain fully available. |
| **Manual ceremony** | The Composer cannot compose (§10.3). | Author-composed proposals at *higher* ceremony, audit-flagged. | Normal or reduced. |
| **Recovery** | Post-dormancy, or after a substrate or adapter change. | Closed until integrity checks pass and bases are re-validated. | Read-only until baseline verification completes. |

**The invariant across all five: the universe is always readable, and canon is never written on an unverified path.** Fail closed toward truth, fail open toward artifacts (P-19).

**The public surface is unaffected by every mode above.** Published artifacts are immutable Production records; a system in read-only, recovery, or total absence still serves every issue ever shipped. *The magazine does not stop existing because the operator's tooling is down* — which is both correct engineering and the right relationship between an artifact and the machine that made it.

---

## 29. Anti-Bloat and Architectural Classification

Bloat, not missing features, kills long-lived solo systems. coolboy12 is disciplined against it by constitution, and its first defense is to classify *what kind of thing* any idea is before admitting it. v0.4 added considerable capability and no domain and no primitive. **v0.5 is the first version to also subtract**, and §29.6 records what that taught.

### 29.1 Architectural Classification

Before anything is admitted, it is classified as exactly one kind of thing, in descending weight:

```
ARCHITECTURE  (a domain or spine — an independent area of responsibility)
     ↓
WORKFLOW      (a coordinated, multi-step process the Composer can run)
     ↓
CAPABILITY    (a reusable function; a primitive)
     ↓
BEHAVIOR      (a behavior belonging to a coworker role)
     ↓
STATE         (a temporary condition of something)
     ↓
METRIC        (a measurement)
     ↓
ARTIFACT      (a generated output)
```

The rule, as prohibitions: **never promote a State into an engine; never promote a Metric into a domain; never promote a Behavior into a system.**

**The v0.5 classifications, recorded for the same reason the earlier ones were.** **Reality Anchoring** and **Historical Divergence** are *capabilities* of the Universe domain — an anchor is a record with a mandatory field, not an engine. **Society** is a *reading* of the World partition — not a domain, not a store, not a kind (§11.3). **The Registry** is a **sovereign Record Model** (§13.6e, I-105), not a capability and not infrastructure. *(REVISED v0.7.0: this entry read "a *capability* — definitional infrastructure," which was accurate before v0.6.1 promoted Registry to a partition and is not accurate now. Registry holds **Records** — kind, field, relationship-type, vocabulary, identity-grammar, validation, derivation, indicator, and model definitions — each with identity, provenance, and a governed change path.)* **It appears nowhere in the flywheel because it is upstream of it**: the flywheel turns on domains acting on Records, and Registry defines what those Records mean before any of them turns (§9.4). **The Publication Artifact Model** is a *capability* of the Studio producing *artifacts* — the page is an artifact, the model that describes it is a capability, and neither is a domain. **Pseudo-Science Governance** is a *capability* with a pipeline, not a science engine. **The two surfaces** are *UX facts*, not architecture (§27.5). **Departments** are *Production State*. **Session** is an *ordinal on an existing axis*, not a fourth axis (§12.16). Deep new capability, zero new architecture, for the third version running.

### 29.2 Explicit Rejections

Rejected outright: module explosion; protocol explosion; registry explosion (one Record model with a `kind`); engine-after-engine accumulation; **multi-substrate orchestration**; enterprise bureaucracy; unnecessary constitutional language; redundant abstractions (one term per concept); AI-first design (the human is the center); build-guide, file-tree, and stack sprawl (this is a blueprint, not an implementation); and any feature that fails the North Star Test.

Rejected in v0.4: **canon reconstruction from a log as a source of current truth**; **epochs as world entities**; **destructive undo in any form**; **inferred canonical writes**; **silent truncation of context**; **a permissions or multi-contributor model**; **automatic epoch transitions**, **automatic debt write-off**, and **automatic reveals**; **a central recommender**; **a Monitoring domain**; **a second reasoning substrate for any role whatsoever**; and **an eleventh Spine law**.

Rejected in v0.3.1: **history as a second canon**; **history as a world primitive**; **event sourcing as an architecture**; **history accumulating inside Records**; **destructive rollback**; and **monitoring views promoted to entities**.

**Rejected in v0.5**, each because it was genuinely considered and each because it would have cost more than it returned:

- **An open World kind taxonomy.** A list described as "illustrative, not exhaustive" with an admission test and no counter-pressure grows a kind for every interesting noun (§13.6).
- **A `SOCIETY` domain, kind, or store** — it fails the Domain Admission Criterion on standing state and authority boundary (§9.3).
- **A `PUBLICATION` domain** — its question is already Editorial's (§9.3).
- **A fourth temporal axis.** Publication-time is operational metadata, and the issue ordinal is a sequence rather than a clock. An axis nothing canonical orders by is metadata (§12.16).
- **A relationship as an independently-historied Record** — the packaging cost a special case in every identity operation and bought nothing (§13.9).
- **A parallel WSV history alongside History Record** — WSV-H *is* the history; two would duplicate state truth, which §15.16 forbids outright.
- **A public lore browser, canon export, or reader-facing entity page**, in any form, ever (§6, §27.5).
- **A reader-signal path into canon** that does not pass through an author, a gate, and a recorded reason (§20.8).
- **An eleventh Spine law**, for the third version running.

### 29.3 The Admission Test, Override, and Non-Negotiable Core

Every proposed structure must pass: *What failure does this prevent that would hurt the universe? Can it be a field, then a kind, then a status, before a new structure (P-7)? Will it still earn its place in Year 5, with one user? Does it reduce daily friction? Does it have a named consumer (P-10)?* The **Solo-Author Override** lets the author simplify or suspend any part that costs more than it returns, with a one-line recorded reason. The **Non-Negotiable Core** is exempt from override because its failure accumulates silently: the single mutation path and its human gate, the Spine and the transactional commit, coherence and canon-health checking, the Publishing Firewall, and derivation on canon.

**The Non-Negotiable Core, extended (v0.4).** **The basis-state requirement** (P-22), **causal closure of acceptance** (§15.13), **the structural-violation block** (P-24), **the Exit Invariant** (P-27), and **the partition rule** (§13.6).

**Extended again (v0.5), by exactly two.** **The public surface's exposure set** (§27.5) — a leak there is unrecoverable, because a reader cannot un-see the machinery, and the failure is silent until the illusion is already gone. And **the one-directional epistemic rule** (§14.19, §20.8) — a belief, theory, or published claim acquiring truth-authority is undetectable from inside the system and corrupts everything downstream. Note what is *still* not added: nothing about anchoring, departments, the artifact model, or the Registry. Those are negotiable, and should be.

### 29.4 The Contraction Path

**Retirement applies to everything admission does:** capabilities, object kinds, subtypes, manifestation kinds, reader models, coworker roles, standards, projections, adapters, departments, and vocabulary terms. The path: **propose** (what is retired, why it no longer earns its place under the North Star Test and the Cost Test) → **impact** (what depends on it — including canon, Production State, and history) → **disposition** (what happens to existing records: retained-and-frozen, migrated, or converted — **never deleted**) → **authorize** (the Authority, at the severity of what it touches) → **record** (Creative Memory and, where canon is implicated, History Record).

**Retiring never rewrites history.** A retired reader tier's past epistemic records remain and remain readable; a retired object kind's existing objects are frozen, not converted; a retired capability's outputs remain valid artifacts of their time. Contraction removes the *future* obligation, never the *past* record.

**The override budget.** Every override is **dated, reasoned, and reviewed at the next epoch transition**, where exactly three outcomes are available: *reinstate*, *retire*, or *extend* (with a fresh reason, recorded). An override may not be extended silently, and the standing set of active overrides is part of Canon Health — because the honest description of a long-lived unreviewed override is not "a simplification," it is an undocumented fork of the architecture.

### 29.5 Anti-Bloat Applies to Anti-Bloat

The governance apparatus is subject to its own charter. Every check, dashboard, health finding, review stage, verdict class, and ceremony must have a named consumer (P-10), must pass the Cost Test, and is re-justified at each epoch transition. **Governance that costs more attention than the failures it prevents is bloat wearing a badge.** If a capability — including any added in v0.5 — is not being read and acted on by year two, it should not survive year three.

### 29.6a Source-of-Truth Classification (v0.6)

*(ADDED. Every data class in the system carries exactly one of these, and the classification is part of its definition rather than a property of how it happens to be stored.)*

| Class | Meaning | Rule |
|---|---|---|
| **AUTHORITATIVE** | This is where the fact lives. | Record · Relationship Record · History Record · WSV · WSV-H · Registry definitions once frozen · Issue records about the artifact · Production State about the plan |
| **DERIVED** | Recomputable with no loss from authoritative sources. | Indexes · search projections · graph projections · analytics · materialised views · generated publication projections · relationship back-references |
| **CACHED** | Recomputable and disposable, held only for speed. | Query results · rendering caches · asset-processing caches |
| **TEMPORARY** | Exists within one workflow and does not outlive it. | Working state · simulation timelines before the gate · draft proposals |
| **EXTERNAL** | Lives outside coolboy12 entirely. | Third-party services, retrieved sources, real-world material |

**The rule that makes the classification worth having:** *an external system must never be the only place where a canonical semantic exists.* If deleting a component would lose a meaning rather than a convenience, that meaning was misfiled — it belongs in an authoritative record and the component should hold only a projection of it.

**Two consequences.** A `DERIVED` value that cannot actually be rebuilt is a misfiled `AUTHORITATIVE` value (P-26), and the way to find out is to rebuild it on a schedule rather than to assume. And nothing in the `CACHED`, `TEMPORARY`, or `EXTERNAL` classes may ever premise a canonical commit.

### 29.7 The Anonymisation Test (v0.6)

*(ADDED. The single check that keeps the implementation from becoming the architecture.)*

> **Remove every external component name from this blueprint. If the document no longer makes sense, the document is too coupled to its tools.**

This is a test to be *run*, not a sentiment. It is run at each epoch transition (Section 4.2) alongside the standing capability re-justification, and it is run before any dependency is adopted into a section of this document.

**What passing looks like.** Sections describe *capabilities, contracts, and boundaries* — "an index that can be rebuilt from canonical records", "a layout engine that consumes the artifact model and emits page images", "a validation engine that enforces the Registry's constraints". Each names what must be true, what goes in, what comes out, and what happens when it is gone. A reader who has never heard of any specific tool can still build the system, and a future author replacing every component keeps the whole document.

**What failing looks like.** A section that cannot be read without knowing a particular product's data model; a rule phrased in a component's vocabulary rather than coolboy12's; a boundary drawn where a tool happens to have a seam rather than where the architecture has one.

**Why this sits in the anti-bloat section rather than the ecosystem section.** Tool coupling is a form of bloat — it is capability the system did not choose, acquired by adjacency, and it accumulates exactly the way feature bloat does: one reasonable decision at a time, each locally sensible. Section 29 is where the system says no, and this is one of the things it says no to.

### 29.8 The Rebuild-From-Canon Drill (v0.6.2)

*(ADDED. The anonymisation test (§29.7) checks that the *document* is not coupled to its tools. This checks that the *system* is not.)*

> **Delete every derived store — every index, every embedding set, every search structure, every graph projection, every rendering cache — and rebuild them from canonical records alone. If the rebuild does not complete, the deleted store was not derived.**

Run at each epoch transition (§4.2) and before any dependency is adopted. It is the operational form of three separate invariants that would otherwise be assertions: the direction-of-derivation rule (§26.2d), the source-of-truth classification (§29.6a), and the Exit Invariant (P-27).

**Why a drill rather than a rule.** Every one of those three is easy to state and easy to violate gradually. A store acquires one authored value, then a second, and remains nominally derived for years until the day it is deleted and something is missing. **A derived store that has never been deleted is a store whose classification is an assumption.** The drill converts the assumption into a fact, on a schedule, at a moment the author chose.

**Failure is a finding, not a catastrophe.** The rebuild that fails has identified a misfiled authoritative value (P-26) — which is exactly what it was run to find, and considerably cheaper to find this way than the other way.

### 29.6 What the First Contraction Taught (v0.5)

§4.2 has required periodic re-justification since v0.4 and had never once been exercised at structural scale. v0.5 exercised it, contracting the World taxonomy from eighteen kinds to eight (§13.6). Four findings are recorded here because the next author to attempt a contraction will need them, and because a charter that describes contraction without ever having done one is a charter making a promise it has not tested.

1. **The ladder runs downward, and almost nothing had ever descended it.** P-7 has always specified *field → kind → status → structure*, upward. Ten of eighteen kinds descended to a subtype, a tier, or a `CONCEPT` with no loss of expressiveness whatever. The taxonomy had not grown because each kind was necessary; it had grown because promotion was the only direction anyone had implemented.
2. **The weakest kinds were the ones straining against their partition.** `MYSTERY` carried Epistemic properties in a World record. `THEME` was half craft-intention. `FORCE` was a tier wearing a kind. Contraction found them by asking the partition question again, which suggests the routine diagnostic: *a kind that needs a caveat about which partition it belongs to is a kind that is about to be a subtype.*
3. **Removing an escape hatch is the one move that costs something.** `WORLD-FACT` existed to catch what nothing else fit. Removing it and contracting the taxonomy in the same version raises misfiling pressure, which is why §13.6 accepts it as a **monitored risk** with a named health finding rather than declaring the contraction free. **A contraction that claims no cost has not been examined.**
4. **Contraction improved the Spine's reach rather than eroding it.** The Severity Floor now catches every withheld fact instead of only those filed as a `MYSTERY` (§10.5), and relationship topology became easier to identify under Relationship Record ownership (§13.9). This is the outcome to aim for and the test to apply: *if a contraction weakens a guarantee, it is a deletion wearing a contraction's name.*

---

## 30. Worked Example — *"Simulate until this empire collapses."*

1. **Compose.** The Composer classifies this as intent-directed Simulation and builds the graph: Simulation → author review of the timeline → gated acceptance.
2. **Plan the path.** The World Analyst treats collapse as a target state, identifies the pressure edges whose thresholds would produce it (legitimacy decay, fiscal strain, a restive periphery), and reasons a *causally honest* path — where each transition is a threshold crossing against inertia, not a coin flip. It recommends a horizon: *"~90 years, with a branch point at the eastern revolt."*
3. **Branch and converge.** At the revolt it proposes branches (revolt succeeds → fast collapse; crushed → slow rot; stalemate → fracture), each with its selecting conditions, a qualitative likelihood, and a counter-case. It flags a **convergent** outcome: in every branch, the central institution loses its monopoly within a century — a robust future the author can plan around.
4. **Compress and expand.** The 90 years are delivered as a few dozen meaningful transitions, expanding year-by-year around the revolt and compressing the stable decades — reviewable in one sitting, and token-lean by construction.
5. **Review at the gate.** The author accepts the path up to the revolt, steers the branch (chooses "stalemate → fracture," recorded reason: *"more story in a fractured aftermath"*), rejects one late famine transition (*"want the collapse political, not ecological"*), and re-runs the tail.
6. **Commit.** Accepted transitions become confirmed events, committing transactionally and propagating (Spine, law 8). *The author decided; the system calculated a believable century; nothing committed without the author; and a year later, "why did the empire fall this way?" has a recorded answer.*

**Under v0.4 rules, three things happen that did not before.** At step 5, rejecting the late famine while keeping the collapse triggers a **causal closure check** (§15.13): the famine was an antecedent of two accepted transitions, so the system offers the choice — accept the famine, drop its dependents, or **re-cause** them. The author re-causes: the two transitions commit with an *authorial cause* rather than a famine that no longer exists, and History Record entries exactly that. The run is also **re-validated against its basis** (P-22) — composed three sessions ago, two objects it read have changed, so those transitions are marked stale and re-reasoned before the gate. And the acceptance records its **Scope of Approval** (P-23): 1,840 objects accepted in aggregate at Standard severity, eleven transitions individually reviewed, one branch steered, one re-caused.

**What v0.5 changes here.** The legitimacy and fiscal indicators the run moves live in **WSV** (§13.10), not on the empire's own record — they are world-scale quantities, and §15.16's test assigns them accordingly. Each accepted transition therefore writes its new value to WSV and its transition to **WSV-H**, in the same transaction as the `EVENT` that caused it and the History Record entries of every object the propagation touched. The recorded causal chain — *pressure edge → threshold → EVENT → indicator transition* — is the §13.12 chain, walked once and recorded once, in exactly one place.

---

## 31. Worked Example — *"Prepare the next issue."*

1. **Compose & select.** The Composer runs the editorial workflow. The Editor-in-Chief has already read the Opportunity queue and recommends three directions; the author picks the strongest — a faction tension a recent Tick produced.
2. **Frame & structure.** The author frames the issue's argument; the Narrative Designer maps it to the active arc, proposes clue placements against the reveal-readiness curve, and flags an investigator-tier payoff as **overdue — mandatory this issue**.
2a. **Allocate the departments (v0.5).** The Editor-in-Chief lays the issue out across its standing departments (§17.12) and reports the balance: the faction tension takes the lead feature and two briefs, but the fashion page, the classifieds, and the music review still run — and what *they* run this month, under a faction tension nobody in the magazine is naming directly, is where most of the issue's real work happens (§17.2). The Story Balance Analyzer notes that ordinary-life material has been under-allocated for three issues (§19.10).
3. **Precheck (facts block).** Governance runs coherence: an asserted detail contradicts confirmed canon — a hard stop. The author resolves it at the gate, then production proceeds.
4. **Produce (bounded).** The Studio drafts under the Draft Lifecycle, bounded by canon, knowledge-state, and Editorial's form decisions; each in-world claim is tagged with its Editorial Truth Classification. The **artifact model** (§18.9) supplies the issue's material character — this publication's paper, this era's press, this issue's physical wear.
5. **Diagnose (judgments decided).** Governance returns verdicts as *criterion → observation → judgment → confidence*, catches that the cover is *"coherent but derivative,"* and the author varies it. It also raises **"over-explained"** against the lead feature: the derivation chain (§23.4) shows the piece was built straight from the World partition, and a paragraph states outright what the shipping notice on the facing page already implies (§19.11). The author cuts the paragraph. What worked is deposited to Memory.
6. **Reader simulation.** The four tiers are run; the overdue payoff lands for the investigator, the casual reader gets a complete surface (§17.15), and the knowledge trajectory advances.
7. **Gate & publish.** The author confirms; the Producer assembles; **publication is a projection and writes nothing** — it records, as Production State, that the artifact shipped, at what issue ordinal, on what date, and the **canon basis** it was derived from (§20.5).
7a. **The in-world act, proposed.** Because this magazine exists inside the fiction, the author proposes the in-world publication as a world `EVENT` (§17.7.1) — ordinarily one Trivial-severity commit — which carries **world evidence**: the characters with in-world reach may now learn what the issue carried. Had the artifact no in-world counterpart, this step would not exist.
8. **Reader knowledge, gated.** Reader Simulation emits a **Reader Knowledge Proposal** (§20.4): what each tier now knows, believes, suspects, and is owed, with its evidence chain. The author accepts it as one batched Trivial-severity act — except the one reveal-state moving to REVEALED, which is separated out and gated individually because it is an authored moment and irreversible for the reader. *The author's attention went to selection and judgment; they reached it all by saying four words; and no fact about the world was written by an act of publishing.*

### 31.0 Worked Example — *"Create an issue about the consequences of a major drought."* (revised)

The purpose of this example is narrow: to demonstrate that the **already-existing** architecture composes across all six partitions. It introduces no capability.

**1 · Author intent.** *"Create an issue about the consequences of a major drought."* The Composer decomposes it (§23).

**2 · R — Registry.** The environment/agriculture and economy **Simulation Model definitions** are resolved (§15.17), along with the WSVR indicator definitions for `rainfall_index`, `harvest_yield`, `food_price_index`, and `public_trust`, and the `<kind>_type` vocabularies the run will write against. **Nothing here is a world fact** — the Registry supplies meaning and behaviour, not state.

**3 · Simulation → W.** The models run over the horizon. The environment model's rainfall deficit propagates along a declared dependency chain into agriculture, then prices, then household stress, then public opinion (§15.18). Where two models propose opposite movements of `food_price_index`, the declared precedence resolves it — and where it does not, the run **stops and reports the conflict** rather than averaging (I-93).

**4 · W — the commit.** Candidate deltas pass validation and the Human Gate, and the Mutation Coordinator commits **one atomic tick** (§15.22): a famine `EVENT` (`W-EV-042-…`) is created; the affected `LOCATION` and `ORGANIZATION` records take world-state changes; **Relationship Record** changes record the new causal edges from the drought event to its consequences, owned by the causing endpoint (§13.9); **WSV** takes the four indicator movements; **History Record** entries are written for every object touched; and **one WSV-H entry** is written for the tick, naming model, dependency, driver, and chain (I-92, O-05).

**5 · E — subject-relative epistemic state.** Who knows what is not uniform. A provincial governor **KNOWS** the granary reserves are gone; the capital's ministry **BELIEVES_FALSE** that they are adequate, because the governor's report was suppressed; the public is **UNAWARE** and will learn from the issue itself. A **MYSTERY** (§14.20) organises the withheld truth of *why* the report was suppressed: its answer is an ordinary `W` record, its unknown-ness is these `E` records, and its reveal-state is HIDDEN for every reader tier.

**6 · P — editorial planning.** Editorial selects from the Opportunity queue, allocates the issue across departments (§17.12), and applies **taste criteria** (§17.17) — this publication opens mid-situation and distrusts preamble. The **Writer Persona** for the agriculture columnist is loaded (§17.19): she has genuine expertise, a standing grudge against the ministry, and a blind spot about provincial administration — so her piece will be *right about the harvest and wrong about the cause*, which is an authored misconception (§14.9), not a defect.

**7 · V — Visual Library.** The art-direction brief (§18.12) assembles canon, editorial intent, taste, and publication identity. **Visual continuity** (§18.11) checks a proposed depiction of the affected region against its canonical visual specification and flags a divergence — the drawing shows a river that ran dry two world-years earlier. The finding lands **against the asset**, not against canon. Correcting it is an asset revision; had the analysis instead suggested canon was wrong, it would have produced a **proposal** through the ordinary gate, never a canonical write (I-89).

**8 · I — Issue assembly.** The issue is assembled as an `I` record (§13.6a): sections, articles, pages, spreads, advertisements, visual placements, publication metadata. The advertisements do heavy lifting — a notice for grain futures reveals an economy, a class structure, and a set of anxieties without asserting a single plot fact (§17.12).

**9 · Publication.** The artifact is rendered to page images with its authored material specification (§18.9). **Publication writes nothing to canon** (I-06). Publication history is recorded as production metadata; the *in-world* act of The Overtone printing this issue is a separate world `EVENT`, proposed and gated like any other (§17.7.1).

**10 · Reader.** Readers experience the issue and their knowledge advances — as a **Reader Knowledge Proposal** the author gates (§20.4), never as an automatic write. Reader theories about the suppression form and are recorded as `E` records about what a tier believes. **No theory becomes true by being popular** (I-78).

**What the example demonstrates, and nothing more.** All six partitions participated; each stayed in its lane; the Registry supplied meaning and no facts; the Visual Library observed and proposed and did not canonicalize; the Issue referenced world records without owning any; and neither publication nor readership mutated canon by any route.

### 31.1 Worked Example — *"I was wrong about the founding."*

The author decides, in year four, that a lineage's founding date and founder are wrong — not changed by events, but **never true**. This is a retcon (§12.12).

1. **Classify.** The checker classifies it as a retcon, not an evolution, because it inverts a prior fact rather than moving world-time forward. Severity: at least Structural, automatically.
2. **Preflight.** The dependency walk returns 214 dependent objects, three active arcs, one withheld fact whose solution assumed the old date — which the Severity Floor catches as load-bearing under the Reading of Law 7 (§10.5) rather than because anything was ever filed as a `MYSTERY` — and **nine published issues** that asserted it (the publication divergence set, computable only because of artifact–canon binding, §20.5).
3. **Disposition every dependent.** Each of the 214 is re-based, retired, preserved-as-contested, or preserved-as-independent, with reasons. Two are left CONTESTED because the author wants a week to think; those two are blocked from citation until resolved.
4. **Do not touch the artifacts.** The nine published issues stand exactly as printed. The world now contains an in-world publication that was mistaken — permitted by the Firewall, and, the author decides, *useful*: the mistake becomes a story about who benefited from the false founding.
5. **Reconcile knowledge.** Every epistemic record referencing the old fact is surfaced (§14.17). Readers cannot un-read: the casual tier now BELIEVES something false, the investigator tier's theory model is re-scored, and the divergence is marked **authored** rather than accidental — because it now is.
6. **Commit and record.** One transaction: the retcon, its 214 dispositions, the History Record entries — including on every object whose **Relationship Record** changed, because re-pointing a founding relationship is a change to that object's canonical situation (§13.9) — and the Creative Memory entry with the reason and the counter-case for leaving it alone. **Query order afterward** (§22.5): *what is true?* → canon. *What changed and who approved it?* → History Record. *Why?* → Memory. Historical Replay before the retcon still shows the old world exactly as it was believed — the universe changed its mind, and did not lose it.

### 31.2 Worked Example — *"Close the epoch."*

After two years and roughly nine hundred commits across some two hundred sessions, the author ends an epoch (§12.14).

1. **Baseline.** A complete, immutable statement of current canonical state is written — not a summary — including the full WSV state (§13.10). Canon at this instant is reconstructable from it alone, with no history traversal.
2. **Compress, never discard.** The closing epoch's History Record is retained in full and gains two layers alongside it: a revision digest per object and an epoch summary (major transitions, ripple chains, one retcon, two reversions, four refactorings).
3. **Re-justify.** Every standing capability faces the North Star Test and the Cost Test as it is *actually used* (§4.2). Two dashboards nobody has read in a year are retired through the contraction path; their outputs remain valid artifacts of their time. **The `WORLD-FACT` monitored risk is reviewed** (§13.6): the Canon Health finding for `CONCEPT` records with no conceptual content has fired eleven times, nine of which were genuine misfiles — so the finding is working, and the escape hatch is not reinstated.
4. **Review the exceptions.** Active overrides are reinstated, retired, or extended with fresh reasons. Three Manual Ceremony entries are reviewed. Adjudicated judged findings are re-examined: one has been overridden four times, so the standard — not the world — is what is wrong, and it is amended.
5. **Demote epistemic tracking.** Facts no longer serving any active plan return to frame defaults, their tracked history retained in the archive. The tracked set shrinks by a third.
6. **Open the next epoch.** Retrieval now answers most questions from the live epoch alone. *Nothing was deleted. The history got easier to read.*

---

## 32. Recommendations — Coworker Behavior

Recommendation is not a separate engine; it is a native behavior of the AI staff (Section 21), produced *by specialty* — by the role whose remit a recommendation falls in. There is no central recommender. The Editor-in-Chief recommends what to tell and when, and how the issue's departments are balanced; the Creative Director recommends visual form and the artifact's material character; the Research Director recommends anchors and their transformations; the Narrative Designer recommends structure, clue placement, and payoff timing; the World Analyst recommends pressures, simulated paths, and thin regions to develop; the Canon Keeper recommends reconciliations; the Producer recommends sequencing; the Quality Reviewer recommends corrections framed as evaluations, never as creative direction.

Recommendations are present at the start of a session, ranked by leverage, each naming the signal it drew on and the canon that justifies it, each offering alternatives where the situation is open, and each advisory only (Spine, law 6). The division of labor is exact: *the staff recommends; Studio Standards validate; the author decides.*

---

## 33. Future Extensibility

coolboy12 grows *by amendment*, not accretion. **The core stays small and the world grows large.**

- **New manifestations attach at the Studio, not the core.** The Universe, Canon, Simulation, Emergence, the dependency graph, and the primitives never change — they are manifestation-blind.
- **New intents attach at the Composer.** A new kind of work is a new intent-to-workflow mapping. No domain changes; the author simply gains a new thing to *ask for*.
- **New simulation dynamics extend the temporal engine.** A new pressure type, threshold behavior, or branching heuristic is a dynamic on world-state, not a new domain.
- **New external tools attach behind adapters.** The reasoning layer stays single-substrate, and rebinding it is an adapter change, never an amendment.
- **New observability views attach as projections, not as truth.**
- **New object kinds, gates, and reader models extend existing families** — each classified first (§29.1), with a named consumer. **A ninth World kind additionally passes the eight-question admission test at Foundational ceremony and lands in both documents in the same cycle** (§13.7, §13.11).
- **New subtypes, relationship types, anchor categories, controlled values, and indicator semantics attach at the Registry** *(v0.5)* — the cheapest extension point in the system, and the one v0.5 deliberately left most room in. Because Registry dependency runs downward only (§9.4), adding or refining a definition changes meaning below it and can invalidate nothing above it.
- **New departments attach at Editorial** *(v0.5)*, as Production State. **New era vocabularies for the artifact model attach at the Studio** (§18.9).
- **The amendment discipline governs the OS itself.** The system evolves the way canon does: deliberately, provenanced, never by drift.

**Every extension point also retires (P-25).** A manifestation kind is retired at the Studio (its published artifacts remain, its canonical identities are frozen); an intent mapping is retired at the Composer (parked workflows using it are reported unresumable, not silently broken); a simulation dynamic is retired at the temporal engine; an adapter is retired through its exit path; **an object kind is retired by freezing its existing objects, never converting them, with a stated destination for the concept** (§13.11); a department, reader model, or coworker role is retired as Production State with its records retained. **All of it runs through the contraction path (§29.4), and none of it ever rewrites history.**

**Extension contracts are versioned.** Every attachment point declares a contract — what it accepts, what it guarantees, what it forbids — carrying a version. An extension built against version N keeps working, or is explicitly reported as incompatible; it never fails silently.

**The contraction rule, stated plainly.** *The system must be able to get smaller.* v0.5 is the first version to demonstrate this rather than assert it (§29.6). A blueprint that only ever adds is a blueprint whose tenth year is unusable, however elegant its first.

**The chapter trajectory is an extensibility constraint, not a roadmap** *(v0.5)*. Chapter 2 (multi-species, beyond one world) is served by the current architecture (§11.4). Chapter 3 (reality, ontology, the universe as experience) is deliberately unbuilt and deliberately un-foreclosed: the Foundation is amendable by ceremony rather than immutable by construction; the publication artifact has no dependency on the world persisting; and the reader/world boundary is a partition rule rather than an ontological claim. **A future version must not remove these three properties for tidiness.**

---

## 34. Final Synthesis

coolboy12 is a **Single-Author Universe Operating System**: an instrument for one person, working with one model in many roles, to build, simulate, govern, and manifest one living fictional universe across many media and many years — without ever fragmenting the world, eroding its coherence, or losing the thread of why it became what it is.

Its architecture is one loop turning around a thin, frozen Spine, carried by nine domains, driven through two primitives, executed by one substrate, and remembered by Creative Memory.

What v0.3 deepened is *how the world is reasoned through*: Simulation as a temporal reasoning system; Editorial as the layer that decides what to tell, in what form, and at what time; Governance able to say not just *wrong* but *canonically correct yet narratively premature*; knowledge-state separating cleanly what is true from what the world, a character, and each reader tier knows.

What v0.4 changed was narrower and, in its way, more important: it made the document *true*. Publication no longer writes canon; the system no longer claims mechanical certainty where it holds an opinion; authored production state has a home; acceptance must be causally closed; approval does not aggregate silently; every proposal declares the ground it was computed on. And the operations a decade-old universe actually performs — retconning, refactoring, reverting, replaying, epoching, retiring — became governed rather than improvised.

**What v0.5 changes is the direction.** Every prior version added. v0.5 is the first to subtract, and the subtraction is the point: eighteen World kinds become eight, four temporal frames become three canonical axes, and a relationship stops being an object with a history of its own. Nothing was deleted — every retired kind descended P-7's ladder to a subtype, a tier, or a Concept, which is where the ladder always pointed and where nothing had ever actually gone. The contraction made two guarantees *stronger* rather than weaker: the Severity Floor now catches every deliberately withheld fact instead of only those someone remembered to file as a mystery, and relationship topology became easier to identify rather than harder. That is the test v0.5 leaves behind for the next author who proposes to remove something: *if a contraction weakens a guarantee, it is a deletion wearing a contraction's name.*

Alongside the subtraction, v0.5 architects the half of the project the earlier versions described only in passing — the half where the reader actually is. A world anchored in real history, diverging from it at recorded points, for stated reasons. A society whose ordinary residue — its advertisements, its fashion pages, its complaints — is the mechanism by which the world reaches anyone at all. A magazine that is an institution with a past, a house style, columnists who are sometimes wrong, and departments that keep running while the empire falls. A page that reads as a printed object with a history rather than a web layout with a filter. And a public surface with exactly one thing on it.

Beneath it sits the principle the earlier versions implied and none of them wrote down: **do not give the reader the world directly; give the reader artifacts produced by a world that appears to genuinely exist.** Everything v0.5 adds is a consequence of taking that seriously — and everything it removes is something that had quietly made it harder.

The guarantees are unchanged and hard. One canon, one path, one authority, one human gate. Canon changes are atomic; propagation runs on real relationships; every Record has derivation, every mutation a changelog, every important choice a recorded reason and a preserved counter-case. There is one reasoning substrate, and rebinding it costs nothing canonical. The core stays small; the world grows large.

coolboy12 does not optimize for architecture. It optimizes for **sustained, long-horizon creativity** — for the creator who wants to make a great, coherent, living universe for decades, and who should be able to say a few words, watch the world move through time, and make a good decision.

*The universe is the source. Artifacts are manifestations. The magazine is the primary lens — never the universe itself.*

---

### 34.1 Conformance (v0.7.0)

*(ADDED v0.7.0. Stated because five of six Record Models have open schemas, and a blueprint that does not say what conforming to it means will be read as claiming more than it has.)*

**Two kinds of conformance, and they are not the same thing.**

**Architectural conformance** — what this document can be conformed to today. An implementation conforms architecturally when: the Spine's ten laws hold; the 108 invariants hold; every Record carries exactly one partition and is owned by that partition's Record Model (I-16, I-101); the identity grammar `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` is used across all six models (I-82, §13.9a); shared mechanisms are shared and semantics are not (I-103, §13.7a); Relationship Record and History Record appear only where a Record Model declares them (I-102, §13.6d); canonicality carries its model's meaning and no other (I-104, §13.7c); the Mutation Coordinator is the only writer of canon (I-83); Registry holds meaning and neither instances, schema, nor runtime (I-75, I-88), and governs definitions without owning another model's Records (I-105); and nothing becomes true by being published (Spine 5, I-81).

**Implementation readiness** — what this document explicitly does **not** certify:

- **No implementation exists.** Nothing described here is running code, stored data, or a deployed artifact.
- **Artifacts 001–032 have not been audited.** Their compatibility with the Record System is **unestablished**, not asserted in either direction.
- **The Roadmap has not been revised** against v0.7.0.
- **Artifact 033 has not been finalized**, and no property or field set for it is fixed here.
- **The Record Model Schema has not been revised**; the §13.7 lockstep is outstanding (**FG-V7-01**).
- **Kind rosters outside World are not frozen** (I-106), and **package compositions outside World are provisional** (I-107). Neither may be implemented as a requirement.
- **Five Record Models have open schemas.** Conformance cannot be claimed for the detailed internal design of E, P, R, V, or I, because that design does not exist. Their **boundaries** are frozen; their **interiors** are not.

**The rule between them:** *architectural conformance is claimable now; implementation conformance is not claimable until the audits this document defers have been performed.* A component, document, or artifact claiming conformance must say which one it means.

---

## 35. Changelog

### 35.0 Changelog — v0.2 → v0.3

**Nature of the release.** A frozen-core deepening pass. No redesign, no new primitives, no new top-level domains, no build guide. The Spine and truth substrate are unchanged; mechanics around them are deepened.

**What remained frozen (unchanged, by mandate).** One Canon · One Path · One Authority · the Human Gate · the Publishing Firewall · the Foundation Lock · the ten-law Spine as the constitutional core · the Canon dependency graph as the truth substrate · the single Record model · the single transactional mutation path · the Workflow Composer and Context Builder as the only two primitives · the nine-domain system · manifestation-blind core · adapter-first external tooling · single-author operability · low cognitive load above cleverness.

**What was deepened.**
- **Simulation (Section 15)** — recast from decision-consequence + time-passing into a full temporal reasoning system: timespan-directed and intent-directed modes; horizon, resolution, compression/expansion; pressure, momentum, inertia, thresholds, constraints; causal propagation and delayed consequences; branching, uncertainty, convergence; the timeline graph as author-review surface. The frozen rule (provisional deltas only, never writes canon) is preserved.
- **Workflow Composer (Section 23)** — formalized as the intent-to-workflow *composition* layer that builds multi-domain workflow graphs, not a task router.
- **Context Builder (Section 24)** — made explicitly token-efficient with a four-part structure: Shared Context Bundle, Derived Views, Stage Deltas, Workflow State — smallest sufficient context per step, with provenance.
- **Editorial (Section 17)** — deepened into the narrative decision layer: story selection and readiness, event-to-story transformation, timing logic, narrative debt, medium/form selection.
- **Creative Studio (Section 18)** — deepened as the manifestation layer: production constraints, visual/voice/symbolic continuity, medium translation.
- **Creative Governance (Section 19)** — sharpened the correctness-vs-quality split and added a diagnostic vocabulary ("canonically correct but narratively premature," "coherent but derivative," etc.); facts block, judgments are overridable with a recorded reason.
- **AI Coworkers (Section 21)** — deepened reasoning behavior (analysis, alternatives, counter-cases, risk/debt/opportunity surfacing) and made the single-model, role-based nature explicit.
- **Creative Memory (Section 22)** — deepened into long-horizon continuity intelligence: rejected paths and why, opportunity and debt history, preferences, prior workflow outcomes.
- **Reader / Knowledge-State (Sections 14, 20)** — added a dedicated Knowledge-State Architecture separating what is true from what the author, world, characters, and each reader tier know; reveal-state, clue economy, reveal-readiness, reader suspicion, knowledge progression across issues, deliberate withholding.
- **Multi-domain orchestration (Section 25)** — made explicit that composite intents (e.g. one mystery across five covers) are handled by composing existing capabilities into a workflow graph — not a new engine.

**What was newly clarified without redesign.**
- **Single-LLM commitment (P-15, Sections 9, 21, 26)** — Claude Code is the only model; coworkers are roles it executes; no multi-LLM orchestration exists.
- **Time as a first-class dimension (P-16)** — stated as a principle and threaded through Simulation.
- **Causal and pressure edges (Section 13.3)** — named as first-class relationship families so temporal reasoning walks structure rather than inference.

**What was intentionally left unchanged.** The convictions, the North Star, the flywheel shape, the domain roster, the UX vocabulary, the anti-bloat charter, the arc mechanics, the four-reader model, and the adapter model — all preserved and, where deepened, deepened in place rather than replaced.

**What v0.3 is not.** Not an implementation roadmap, not a file tree, not a stack proposal, not a prompt library, not a new architecture. It is the deepened, frozen-core blueprint of the same system.

*— coolboy12 v0.3*

### 35.1 Addendum — v0.3 → v0.3.1 (Constitutional Additive Revision)

**Nature of the release.** A constitutional additive revision. One missing capability — the explainable evolution of canonical truth — is stated as principle. No section was replaced, renumbered, or removed; no terminology was changed; no architecture was redesigned.

**What remained frozen.** Everything listed above as frozen in v0.3, plus: the ten-law Spine (still ten laws), the Record model and its envelope, the five tiers, the five statuses, the six-kind Truth Model, the four severities, the single transactional mutation path, the two primitives, the nine domains, Simulation, Ripple and Tick, Emergence, Editorial, Studio, Governance, Knowledge-State, Creative Memory, the Publishing Firewall, and the Foundation Lock.

**What was added (additive only).**
- **Core Philosophy (Section 5)** — one clarifying paragraph on Convictions II and IV; the five convictions themselves untouched.
- **Design Principles (Section 7)** — **P-17 Canonical Evolution** and **P-18 No canonical state without an explainable path**; P-1 through P-16 unchanged.
- **The Spine (Section 10)** — one clarification paragraph reading law 9 in full. **No eleventh law.**
- **Canon Architecture (Section 12)** — three new subsections appended after 12.8: **12.9 Canonical Evolution and History Record**, **12.10 Temporal Observability**, **12.11 World Monitoring Projections**. Sections 12.1–12.8 unchanged.
- **Record Model Schema (Section 13)** — **13.5 History Is Referenced, Not Contained**. The object envelope is unchanged.
- **Simulation (Section 15)** — **15.12 Large-Scale Simulation and Evolutionary Traceability**. Sections 15.1–15.11 unchanged, including the frozen rule.
- **Creative Memory (Section 22)** — **22.4 Creative Memory and History Record**, delimiting the two append-only records.
- **UX Principles (Section 27.2)** — two binding principles: *Evolution is observable*; *Rollback is a gated change, never an undo*.
- **Anti-Bloat (Section 29)** — the v0.3.1 additions classified (capability, workflows, artifacts) and six new explicit rejections.
- **Future Extensibility (Section 33)** — one bullet: observability views attach as projections.
- **Final Synthesis (Section 34)** — one paragraph stating the philosophy.

**What v0.3.1 does not do.** It introduces no second canon, no second truth source, no world primitive, no new object kind, no new domain, no new primitive, and no event-sourcing architecture. It designs no storage, no schema, no serialization, no indexing, no transactions, no persistence, and no optimization — and no interfaces or APIs. Those remain implementation-stage concerns, unchanged in their ownership.

*— coolboy12 v0.3.1*

### 35.2 Changelog — v0.3.1 → v0.4

**Nature of the release.** An evolution, not a rewrite. The Spine is unchanged (ten laws, still ten). No top-level domain was added. No new primitive was added. Every addition was classified before admission (§29.1), and the classification of every v0.4 addition is **capability, workflow, behavior, state, metric, artifact, or classification** — never domain, never primitive, never engine.

**What remained frozen.** One Canon · One Path · One Authority · the Human Gate · the Publishing Firewall · the Foundation Lock · Provisional by Default · one reasoning substrate, many roles · no multi-model orchestration · the ten-law Spine · the Canon dependency graph · the single Record model · the single transactional mutation path · the Workflow Composer and Context Builder as the only two primitives · the nine domains · manifestation-blindness of the Universe · adapter-first tooling · single-author operability · Simulation's rule that it never writes canon.

**Audit resolution map.** Every mandatory and high-severity finding of the v0.3.1 constitutional audit, and where it is resolved:

| Audit finding | Severity | Resolved in |
|---|---|---|
| R-01 Publication mutates canon (Firewall breach) | Critical | §20.4, §20.5, §31 step 7–8, §8.3 |
| R-02 No home for authored non-world state | Critical | §9.1 (Production State), §12.4, §11, §13.6, §16.5, §17.8 |
| R-03 Atomic propagation unbounded at scale | Critical | §10.2 (canonical consequence atomic; derived recomputation eventual) |
| R-26 "Mechanical" correctness includes model judgment | Critical | P-24, §19.1, §19.1.1, §12.15 (linter) |
| R-24 Four temporal frames, one word | Critical | P-21, §12.16, §17.9 |
| R-17 Approval does not aggregate; lineage claims it does | Critical | P-23, §12.7, §15.14 |
| R-23 Partial acceptance breaks causal closure | Critical | §15.13, §30 addendum |
| R-05 Retcon ungoverned | High | §12.12, §31.1 |
| R-04 Model non-determinism unacknowledged | High | P-20, §15.15, §26.1 |
| R-18 No compaction invariant for History Record | High | §12.9 (invariant), §12.14 (epochs) |
| R-15 Proposal basis-state unrecorded | High | P-22, §12.6, §15.14, §21.5 |
| R-07 Constitution exempt from its own traceability | High | P-28, §10.4 |
| R-35 No substrate-independent legibility | High | P-27, §26.3, §28.1 |
| R-10 Vendor name in the constitution | High | P-15 rewritten; binding moved to §26.1 |
| R-38 Artifact–canon binding absent | High | §20.5 |
| R-37 No retirement path at extension points | High | P-25, §29.4, §33 |
| R-27 Self-confirming reader model | High | §20.6 (assumption/measurement, correction channel, drift check) |
| R-30 Workflows not durable | High | §23.4, §25.4 |
| R-31 Context sufficiency one-sided | High | §24.6, §24.7 |
| R-21 Epistemic cardinality unbounded | High | §14.17 |
| R-16 Recency tiebreaker | High | §12.2 (CONTESTED), §12.3 |
| R-11 Authority undefined as person-or-role | High | §10.1, §6 (designed exclusions) |
| R-06 No failure/degraded-mode principle | High | P-19, §8.1, §8.4, §10.3, §21.7, §23.6, §28.3 |
| R-08 History Record unowned | Medium | §12.9 (Canon owns it), §9.2 (ownership map) |
| R-09 Circular domain criterion | Medium | §9.3 (five tests) |
| R-12 No conviction precedence | Medium | §5.1 |
| R-13 No periodic re-justification | Low | §4.2 |
| R-14 P-18 assumes non-authorial cause | Medium | P-18 amended, §5.2 |
| R-19 Rollback policy undefined | High | §12.10.1 (three concepts, bounds, ownership) |
| R-20 Envelope custody | High | §13.7 |
| R-22 Reader tiers / roster over-specified | Medium | §14.18, §21.6 |
| R-25 Asset identity across regeneration | Medium | §18.6, §18.7 |
| R-28 Autonomous work unbounded | Medium | §21.5 |
| R-29 History Record / Memory precedence | Medium | §22.5, §22.6 |
| R-32 Interface contract hidden in an example | Medium | §23.5, §25.4 |
| R-33 No adapter exit invariant | High | §26.3 |
| R-34 Vocabulary lagging capability | Medium | §27.3 |
| R-36 Overrides unbounded in time | Medium | §29.4 (override budget) |
| R-39 Canon Health as a role behavior | Medium | §12.15 (standing invariant) |
| R-49 / R-50 (rejected by the audit) | — | Rejected again: no Engine Architecture document, no eleventh Spine law (§29.2) |

**Capabilities added.** Preflight Impact Prediction · Critique/Counter-Case as a loop stage · Canon Refactoring (rename, split, merge, extract, convert, re-point) · Identity operations (supersede, split, merge, retire) · Epochs (baseline, transition, archive, compression, summary, hierarchical retrieval) · Operational Rollback / Canonical Reversion / Historical Replay · Canon Health, Canon Linter, Canon Search · Narrative Coverage Map · Story Balance Analyzer · Automatic Continuity Review · durable and resumable workflows · exclusion logs and two-sided context provenance · debt lifecycle and write-off · asset lifecycle and canonical visual identity · the Reader Knowledge Model (epistemic lifecycle, evidence graph, confidence, dependencies, misconceptions, forgetting, inference, prediction, surprise forecast, theories, questions, revelation planning, fair-play validation, knowledge debt, completion analysis, forecast, heatmap, knowledge replay, divergence, leakage detection, bounded cardinality, extensible segmentation) · degraded modes · the Invariant Register.

**Principles added.** P-19 through P-28. P-15 corrected (invariant retained, vendor binding moved to §26.1). P-18 amended to admit authorial intent as a terminal cause.

**Structural additions.** One new top-level section: **§36 Invariant Register** — a consolidated normative list, added because implementers need one place to check conformance and because scattering invariants across thirty-five sections is how they get missed. No section was removed, renamed, or renumbered.

**What v0.4 is not.** Not an implementation, not a schema, not a storage design, not a runtime design, not an API. Not a rewrite. Not a new architecture. It is the same system, one audit and one year of hard questions later.

*— coolboy12 v0.4*

### 35.3 Constitutional Repair Record (P-28)

**Nature of the change.** Not a version increment. A repair pass applying the findings of the full constitutional audit of v0.4, recorded here because P-28 requires the constitution to trace its own changes. Twelve defects were addressed and eleven fully closed — the published-fact split was correct in classification and left the in-world act without a trigger, which Section 35.4 closes; no section was added, removed, renamed, or reordered; no law, principle, or capability was introduced.

**Statement of defect.** Six contradictions (aggregate approval; published-fact classification; a seven-row table headed "six kinds"; law 10 versus Manual Ceremony; a replay promise with no supporting mechanism; an undefined production ceremony) and six under-specifications (structural decidability; Authority succession; Creative Memory's write paths; reader segments; CONTESTED's consequences; the Reader Knowledge Proposal lifecycle), plus an ungoverned primitive rung and an incomplete Invariant Register.

**Resolutions adopted.** Batches carry the highest member severity with Structural members individually reviewed inside them. The in-world act of publication is canon; publication history is Production State. Manual Ceremony is a degenerate composition, not a bypass — law 10 stands verbatim. Replay reconstructs past states read-only and Derived; current state is never reconstructed. Production ceremony is defined in §9.1. Structural decidability means determinable from structure alone. Succession happens outside the system; the system waits in read-only. Creative Memory has two declared write classes. Divergent reader segments are knowers; organizing segments are views. CONTESTED blocks premises, not visibility. Pending proposals may inform planning and premise nothing.

**What was rejected.** An eleventh Spine law, a third primitive, an in-system succession mechanism, automatic or delegated authority, and any change to the two-current model, the three rollback concepts, the four frames, the four state classes, or the partitions.

*— coolboy12 v0.4, constitutional repair*

### 35.4 Second Constitutional Repair Record (P-28)

**Nature of the change.** A second repair pass applying the Round 2 adversarial audit. Again not a version increment, and again no section added, removed, renamed, or reordered; no law, principle, domain, primitive, or capability introduced.

**Statement of defect.** Two contradictions (an unavailable substrate both permitting Manual Ceremony and closing the descending current; an invariant claiming answerability that the compression model could not support), one regression from the first repair (the in-world publication act introduced as canon with no trigger and no worked example), and six under-specifications (in-world knowledge had no evidence path though the lifecycle claimed to serve it; batch atomicity; cross-epoch ordering of authoring sequence; CONTESTED transitivity; artifact correction; succession edge cases).

**Resolutions adopted.** Evidence splits into two classes — reader evidence and world evidence — and in-world knowledge changes by ordinary gated canon proposal while reader knowledge changes only by a gated Reader Knowledge Proposal. Publication has three planes, and the in-world act exists only where the author proposes it. An unavailable substrate closes the descending current; Manual Ceremony needs a substrate. A batch is one transaction with all exclusions taken before the gate. Compaction must preserve causal-link identity, and I-30 now states what the body guarantees. Authoring-time is globally ordered across epochs. CONTESTED marks direct dependents only; the premise block reaches any depth. Corrections are superseding publications, never edits. Succession creates no boundary and confers no special power.

**What was rejected.** An eleventh Spine law, a fourth state class, a separate in-world epistemic domain, transitive contestation, editable published artifacts, retconnable production records, and any in-system succession mechanism.

*— coolboy12 v0.4, second constitutional repair*

---

### 35.5 v0.4.2 → v0.5 — Ontology Consolidation and the Publication Artifact

**What this version is.** The first contraction, plus the architecture for the reader-facing half of the project. No Spine law was added, amended, or removed. No domain was added. No primitive was added. **Three things got smaller and one large area got built.**

**What contracted.**

| Change | From | To | §|
|---|---|---|---|
| World kind taxonomy | 18 kinds, "illustrative, not exhaustive" | **8 kinds, closed**, with an eight-question admission test for a ninth | 13.6, 13.11 |
| Temporal model | 4 frames | **3 canonical axes** + session as an authoring sequence ordinal; publication-time demoted to production metadata | 12.16, P-21 |
| Relationship model | A Record with its own History Record | **First-class semantics, Relationship Record-owned packaging**, Registry-declared ownership rule | 13.3, 13.9 |
| WSV | One object per tracked variable | **A singleton with sub-addressable indicators**, `Record + WSV-H` | 13.10 |

**What was added.** `SPECIES` as a World kind (the only admission, on eight of eight). The Record/Relationship Record/History Record package model. The Registry layer and its five-layer dependency contract. Reality Anchoring and Historical Divergence. Society as a named reading of the World partition. Pseudo-Science Governance. The issue's internal structure and departments. The publication as a living institution. Archival and period issues. Layered discoverability. The Publication Artifact Model. Art direction as world information. The Indirectness and Resonance standards. The Reader Flywheel signal classes. The two-surface boundary. **P-29** (anchor by transformation) and **P-30** (the reader receives artifacts). **§5.3, the Artifact Principle.** Ten invariants (I-71–I-80).

**What was decided that had been open.** The kind taxonomy question and the relationship-ownership question — the two collisions the v0.5 audit left unresolved — are both closed. The `LINEAGE`/`HOUSE` question is closed: `HOUSE` is a subtype. The `lineage` envelope field is renamed `derivation` to free the word for the kind; **Spine law 9 is unchanged.**

**What was rejected.** An open kind taxonomy · a `SOCIETY` domain or kind · a `PUBLICATION` domain · a fourth temporal axis · relationships as independently-historied objects · a parallel WSV history alongside History Record · a public lore browser or canon export in any form · a reader-signal path into canon that bypasses an author, a gate, and a reason · **an eleventh Spine law**, for the third version running.

**What remains OPEN, and must be decided before the next freeze.**

| # | Open item | § | Why it is not decided here |
|---|---|---|---|
| O-1 | **WSV package model** — the reconciliation at §13.10 is **PROPOSED**, not settled | 13.10 | Two supplied sources conflicted; the reading given reconciles them and needs authorial confirmation |
| O-2 | **WSV-H entry granularity** | 13.10 | *(Historical — this was open at v0.5. **CLOSED by the v0.6.3 revision:** one simulation tick is one world-state transition is one WSV-H entry, §13.10.)* |
| O-3 | **`derivation` rename** — **PROPOSED**; the alternative is renaming the kind | 13.1 | Touches Spine terminology adjacent to law 9 |
| O-4 | **Department taxonomy** — the roster, the per-issue count, era variation | 17.12 | Authorial, and the sources do not resolve it |
| O-5 | **Artifact model field list** — the enumerated, typed properties | 18.9 | Registry work; needs a pass on per-publication vs per-era vs per-issue scope |
| O-6 | **Reveal-state cardinality** — one record per fact, or per (fact × tier) | 14.2 | Interacts with the §14.17 tracking budget |
| O-7 | **Per-kind semantic dependency maps** — all eight | 9.4 | The Phase-2 dependency matrix was not available; `SPECIES` has no schema at all |
| O-8 | **`ERA` as an `EVENT` subtype** — accepted with reservation | 13.6 | Independent lifecycle is marginal; a Registry temporal classification remains live |
| O-9 | **Indicator semantics** — unit, scale, comparability, valid-range | 13.10 | Registry work that does not yet exist |

**Deferred to v0.6.** The `WORLD-FACT` monitored risk review (first epoch transition, §13.6). Whether `ERA` survives as a subtype (O-8). Registry maturation generally. Anything the open items above surface once decided.

**Conformance note.** v0.5 changes schema-level architecture and therefore requires its lockstep companion, `coolboy12_canon_object_model_v0_5.md` (§13.7). **A v0.5 blueprint without a v0.5 Record Model Schema is not v0.5; it is a divergence.**

---

### 35.6 v0.5 → v0.6 — The Issue Partition and Implementation Compatibility

**What this version is.** One structural admission, one correction, and one boundary. No Spine law added, amended, or removed — the fourth consecutive version to decline an eleventh. No domain added. No primitive added.

| # | Change | Class | Why | Source | Architectural consequence | Implementation consequence | Migration | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | **Issue admitted as a fourth partition** (§13.6, §13.6a) | **ADDED** | A published artifact with a real interior, filed beside the plan that produced it, becomes queryable and then trusted — a second canon by accretion | Authorial decision | Four partitions; reference runs one way into Issue; Issue never owns a World record | Issue records stored and validated separately; partition check extended | None — no records exist | **Boundary frozen; substructure OPEN** |
| 2 | **Seven instance-bearing kinds + WSV singleton** (§13.6) | **CLARIFIED** | v0.5 counted WSV among eight kinds while specifying it as a singleton with no instances. The count was wrong, not the design | Authorial decision | None — no record, field, relationship, or rule changes | Linter must reject any `W-WS-nnn-…` instance | None | **Frozen** |
| 3 | **Partition-first identity grammar** (§13.9a) | **CLARIFIED** | Identity should declare which side of a boundary a record sits on before anything else | Authorial decision | Identity is partition-first; `-R`/`-H` package suffixes | ID parser, resolver, and linter | None | **Frozen except kind-code width — REQUIRES DECISION** |
| 4 | **Temporal model restated** (§12.16) | **RESOLVED** | The issue ordinal is a position in a series, not a measurement of time. v0.5 filed it as a temporal frame and then had to argue it into canonical standing | Authorial decision + internal audit | Three axes: World Time, Session Number, Real-World Time. Issue ordinal owned by the Issue partition | Temporal fields declare an axis; issue ordinal resolves to Issue | None | **Frozen** |
| 5 | **Mutation Coordinator named** (§12.6) | **ADDED** | The path was a sequence of stages, and stages invite assembly from parts that each hold a piece of the authority | Authorial decision | None to the path — it names the component that owns the write boundary | BUILD-NATIVE; no stage may be substituted for the boundary | None | **Frozen** |
| 6 | **External dependency boundaries** (§§26.2a–26.2g) | **RESTRICTED** | The system will be built from components it did not write; the constraints must exist before the components do | Authorial decision | None — constrains implementation, not architecture | Adapter rule, external-store rule, version-control boundary, exit test, benchmark and licence requirements | None | **Frozen** |
| 7 | **Source-of-truth classification** (§29.6a) | **ADDED** | Every data class must declare where its fact lives, so that no external system becomes the only place a semantic exists | Authorial decision | None | Five classes; every external store is DERIVED or CACHED | None | **Frozen** |
| 8 | **Anonymisation test** (§29.7) | **ADDED** | Tool coupling is bloat acquired by adjacency | Authorial decision | Standing test at each epoch transition | Run before any dependency enters this document | None | **Frozen** |
| 9 | **P-31 — dependencies provide capability, never authority** (§7) | **ADDED** | The other eight changes need one principle they all descend from | Authorial decision | Thirty-one principles | Every adapter declares an exit path | None | **Frozen** |
| 10 | **Issue structure re-partitioned** (§17.12) | **RESTRICTED** | The plan may still change; the artifact may not | Consequence of change 1 | Department roster is Production; published departments are Issue | Storage split at the boundary | None | **Frozen** |
| 11 | **Epistemic and Production declared incomplete** (§13.6b) | **DEFERRED** | A blueprint that reads as uniformly complete will be implemented as though it were | Internal audit | Boundaries frozen, schemas explicitly OPEN | Reserved interfaces; no premature freezing | None | **OPEN by design** |

**What was rejected.** An external component as semantic authority, in any configuration · version control as a substitute for History Record or WSV-H · reconstructing semantic history from a commit log · a `WSV` instance-bearing kind · per-variable WSV object IDs · WSV forced into the Record/Relationship Record/History Record package · Issue as a domain, a kind, or a canon partition · a World record referencing an issue · freezing the Epistemic or Production schema to satisfy an implementation component · an eleventh Spine law.

**What remains OPEN, DEFERRED, or REQUIRES DECISION.**

| # | Item | § | Status |
|---|---|---|---|
| O-1 | **Kind-code width** — single-letter codes collide (`C`: Character/Concept; `L`: Lineage/Location) | 13.9a | **REQUIRES DECISION** |
| O-2 | Structural specialization field vs the `<kind>_type` classification field | 13.6 | **REQUIRES DECISION** |
| O-3 | The `derivation` envelope field rename | 13.1 | **PROPOSED** |
| O-4 | WSV-H entry granularity — per tick or per indicator | 13.10 | **OPEN — blocked upstream** |
| O-5 | Issue substructure — field sets, section/department relation, page-to-artifact-model relation | 13.6a, 18.9 | **DEFERRED** |
| O-6 | Epistemic implementation schema, incl. reveal-state cardinality | 13.6b, 14.2 | **OPEN** |
| O-7 | Production implementation schema, incl. department taxonomy | 13.6b, 17.12 | **OPEN** |
| O-8 | Registry expansion — indicator semantics, controlled vocabularies | 9.4, 13.10 | **OPEN** |
| O-9 | Detailed Simulation implementation | 15 | **DEFERRED** |
| O-10 | Publication renderer selection | 18.9 | **BENCHMARK REQUIRED** |
| O-11 | Query and index engine selection | 12.15, 26.2d | **BENCHMARK REQUIRED** |
| O-12 | Whether Epistemic and Production share one index or separate ones | 13.6b | **OPEN** |
| O-13 | `ERA` as an `EVENT` specialization — accepted with reservation | 13.6 | **OPEN** |

### 35.7 Final Contradiction Audit (v0.6)

Run before delivery. Each line is a check, not a claim.

| Check | Result |
|---|---|
| `W` = World, `E` = Epistemic, `P` = Production, `I` = Issue | ✅ §13.6, §13.9a |
| Second identity component is the **kind code**, never "Canon" | ✅ §13.9a |
| Exactly seven instance-bearing World kinds | ✅ §13.6 |
| Every instance-bearing object has Record, Relationship Record, History Record | ✅ §13.9, I-72 |
| WSV: only WSV and WSV-H · no instances · no Record/Relationship Record/History Record package | ✅ §13.10, §13.6 |
| History Record is object history · WSV-H is world-state history · version control is repository history | ✅ §12.9, §13.10, §26.2e |
| World Time ≠ Session Number ≠ Real-World Time | ✅ §12.16 |
| World ≠ Epistemic ≠ Production ≠ Issue | ✅ §13.6, §13.6a |
| Epistemic and Production not presented as fully built | ✅ §13.6b |
| Issue is a publication artifact boundary, is not Canon, does not own world truth | ✅ §13.6a |
| No external component becomes semantic authority | ✅ P-31, §26.2a, §29.6a |
| No simulation, agent, database, or component silently becomes canon authority | ✅ Spine 2–3, §12.6, §15.16 |
| Canonical state recoverable without external indexes | ✅ P-27, §26.2d |
| v0.6 preserves v0.5 structure | ✅ 36 sections, order and hierarchy unchanged |

**One contradiction remains unresolved and is reported rather than solved: O-1, the kind-code width.** The identity grammar's worked examples use single-letter kind codes; seven instance-bearing kinds cannot be distinguished by single letters. The grammar is otherwise frozen. This is recorded at §13.9a and requires an authorial decision.

---

### 35.8 v0.6 → v0.6.1 — Six Partitions and Capability Expansion

**What this version is.** A generalisation, a deepening, and an expansion. No Spine law added, amended, or removed — the fifth consecutive version to decline an eleventh. **No domain added. No engine added. No v0.6 capability dropped.**

| # | Change | Class | Consequence | Status |
|---|---|---|---|---|
| 1 | Canon Object generalised to the universal abstraction over **six partitions** (W·E·P·R·V·I) *(historical; superseded v0.7.0)* | **GENERALIZED** | R and V governed by rule rather than convention; Record ≠ World Truth | Frozen |
| 2 | **Registry** promoted to a partition | **MODIFIED** | Definitions gain identity, provenance, history, gate, linter | Frozen |
| 3 | **Visual Library** promoted to a partition | **ADDED** | Specification / asset / reference / analysis / derivative separated by authority | Frozen; `visual_refs` requirement per kind **OPEN** |
| 4 | **Package specialization by partition** | **CLARIFIED** | History Record universal; Relationship Record only where edges are owned; ownership rule unchanged | Frozen |
| 5 | **WSVR relocated to Registry**; three-way meaning/behaviour/value/history split | **CLARIFIED** | Model definitions and indicator semantics both leave WSV | Frozen |
| 6 | **Simulation Model architecture** — model families, Society Dynamics, Public Sphere, Media Ecosystem | **ADDED** | Models are Registry definitions; Simulation executes, never contains | Frozen; family field sets **DEFERRED** |
| 7 | **Cross-model feedback, conflict resolution, causal graph** | **ADDED** | Dependency, ordering, coupling, convergence, precedence declared; unresolved conflict surfaced, never averaged | Frozen |
| 8 | **Simulation observability** | **ADDED** | Every committed transition names model, dependency, driver, chain, or does not commit | Frozen |
| 9 | **Calibration, sensitivity, stability** | **ADDED** | Advisory; real-world fit never overrides authored world fact | Frozen |
| 10 | **The Overtone across five partitions** | **CLARIFIED** | Institution / operation / issues / visuals / perception separated | Frozen |
| 11 | **Editorial Taste & Criteria Board**, **Taste Corpus**, **Magazine Deconstruction** | **ADDED** | Taste is Production evidence, judged never blocking; corpus is EXTERNAL | Frozen; corpus schema **DEFERRED** |
| 12 | **Writer Persona**, voice analysis, persona evolution | **ADDED** | Production record, not a model; blind spots produce authored misconception | Frozen |
| 13 | **Visual intelligence** — understanding, continuity, similarity, visual-to-canon proposal | **ADDED** | Vision observes and proposes; never canonicalizes | Frozen |
| 14 | **Art Direction Intelligence**, **Publication Identity**, **Period Issue Intelligence** | **ADDED** | Assemble constraints; decide nothing | Frozen |
| 15 | **Issue Intelligence** | **ADDED** | Advisory analysis over a planned issue | Frozen |
| 16 | **Research Intelligence**, trend detection, cultural resonance, humour analysis | **ADDED** | Off by default; outputs are Opportunity candidates | Frozen |
| 17 | **Creative Memory extension** — taste and publication evolution, successful *and* failed patterns | **ADDED** | A failed pattern unrecorded is a failure repeated | Frozen |
| 18 | **P-32 — a capability is not an engine** | **ADDED** | 14 candidates admitted as capabilities; zero domains | Frozen |

**Preserved without change.** Every v0.6 capability is intact, including: Preflight Impact Prediction · Critique/Counter-Case · Canon Refactoring · Identity Operations · Epochs · Operational Rollback · Canonical Reversion · Historical Replay · Canon Health · Canon Linter · Canon Search · Narrative Coverage Map · Story Balance Analyzer · Automatic Continuity Review · durable and resumable workflows · context exclusion logs · two-sided provenance · debt lifecycle and write-off · Asset Lifecycle · Canonical Visual Identity · the full Reader Knowledge Model — epistemic lifecycle, evidence graph, confidence, dependencies, misconceptions, forgetting, inference, prediction, surprise forecast, theories, questions, revelation planning, fair-play validation, knowledge debt, completion analysis, knowledge forecast, knowledge heatmap, knowledge replay, divergence, leakage detection, bounded epistemic cardinality, extensible reader segmentation · degraded modes · the Invariant Register.

**What was rejected.** Fourteen proposed domains and engines, each admitted as a capability instead (§9.3) · vision as a canonicalization path · taste criteria as blocking rules · the taste corpus as a canon or registry source · WSV as an analytics store · model definitions inside WSV · averaging unresolved model conflict · real-world calibration as authority over the world · an eleventh Spine law.

**Open, deferred, and unresolved after v0.6.1.** Carried from v0.6: kind-code width (**REQUIRES DECISION**) · specialization-vs-classification field (**REQUIRES DECISION**) · `derivation` rename (**PROPOSED**) · WSV-H granularity · Issue substructure · Epistemic schema · Production schema · Registry expansion · renderer and query-engine selection (**BENCHMARK REQUIRED**) · `ERA` subtype. New in v0.6.1: which kinds must carry `visual_refs` (**REQUIRES DECISION**) · model-family field sets (**DEFERRED**) · convergence and precedence rules per model pair (**DEFERRED**) · taste-corpus schema (**DEFERRED**) · voice-profile representation (**OPEN**) · visual-similarity representation (**DEFERRED to Step 2 benchmark**).

---

### 35.9 v0.6.1 → v0.6.2 — Implementation Compatibility

**What this version is.** An integration pass that changed no architecture. No Spine law added — sixth consecutive version. No domain, no engine, no capability dropped, **and no semantic surrendered.**

| # | Change | Class | Trigger | Status |
|---|---|---|---|---|
| 1 | **Integration compatibility rule** (§26.2h) | ADDED | Needed before any integration, so results could be checked against it | Frozen |
| 2 | **Eleven adapter contract specifications** (§26.3a) | ADDED | Audit identified eleven boundaries where external capability attaches | Frozen |
| 3 | **Five architectural conflicts recorded and refused** (§26.7) | ADDED | AC-1 relationship authority · AC-2 mutation authority + dormancy · AC-3 exposure set · AC-4 source of truth + legibility · AC-5 memory and context primitives | Frozen |
| 4 | **Mystery as an Epistemic structure** (§14.20) | ADDED — **post-v0.6 decision** | v0.5 relocated mystery to E and never specified it | Frozen; not a domain, partition, World kind, or engine |
| 5 | **Rebuild-from-canon drill** (§29.8) | ADDED | Three invariants were assertions with no operational test | Frozen |
| 6 | **I-97, I-98, I-99** (§36.12) | ADDED | Thirteen proposed, ten redundant and mapped to existing rules | Frozen |

**What did NOT change, and this is the result rather than an omission.** §13 Record Model Schema · partition contracts · §14 Epistemic mechanics (§14.20 adds a structure, changes no mechanic) · §15 Simulation semantics · §17 Editorial · §18 Creative Studio · §19 Governance · §21 AI Coworkers · §23 Workflow Composer · §24 Context Builder · §27 UX · §29 Classification. **The audit produced integration consequences at exactly one section — §26 — and everything else was left alone**, which is what §26.2h predicts when the rule is actually followed.

**What must not happen — verified.** No eleventh Spine law ✅ · no engine per capability ✅ (P-32; fourteen candidates admitted as capabilities) · no Economy/Politics/Media/Mystery domains ✅ · no second canon ✅ · no second persistent simulation world ✅ (I-79: simulation holds no state past the gate) · no external component owning semantics ✅ (§26.7, five refusals) · publication cannot mutate canon ✅ (I-81, I-06) · reader popularity never truth ✅ (I-78) · visual analysis never automatic canon ✅ (I-89) · Writer Persona never overrides Character canon ✅ (**I-98, added for this**) · WSV semantics not duplicated into models ✅ (I-91) · no model definitions inside WSV ✅ (I-91) · version control never confused with History Record/WSV-H ✅ (I-85) · no invented schemas for OPEN areas ✅ · **no OPEN decision silently frozen** ✅ — the open register below is unchanged in status except where an authorial decision was recorded, and none was.

**Open, deferred, and unresolved after v0.6.2.** Unchanged from v0.6.1, and deliberately so. **REQUIRES DECISION:** kind-code width · specialization vs `<kind>_type` · which kinds must carry `visual_refs`. **PROPOSED:** `derivation` field rename. **OPEN:** WSV-H granularity (blocked upstream) · reveal-state cardinality · Epistemic schema · Production schema · Registry expansion · voice-profile representation · `ERA` subtype. **DEFERRED:** Issue substructure · model-family field sets · per-pair convergence and precedence rules · taste-corpus schema · visual-similarity representation. **BENCHMARK REQUIRED:** renderer selection · query-engine selection · graph-traversal engine · visual index at library scale.

---

### 35.10 v0.6.2 → v0.6.3 — Technology Realization and Execution Environment

**What this version is.** A realization pass. No architecture redesigned, no section renumbered, no capability dropped, no semantic surrendered. Seventh consecutive version with ten Spine laws.

| # | Change | Class | § | Consequence |
|---|---|---|---|---|
| 1 | **Execution environment layer** and **P-33** | ADDED | 9.5, 7 | Fixes the ordering author → AI-assisted development → environment → coolboy12 → components. Architectural consequence: none |
| 2 | **Claude Code operating model** | ADDED | 26.8 | Workspace layout, permission boundary, write/propose/never-change split, local-first and dormancy behaviour, recovery |
| 3 | **Simulation Model definition structure** — 22 components | ADDED | 15.17 | A model definition is a Registry object with indicators, dependencies, equations, thresholds, feedback loops, assumptions, and WSV mappings |
| 4 | **37 model families** | EXPANDED | 15.17 | From 26 named families to 37, grouped by subject. Still capabilities, still zero engines (P-32) |
| 5 | **Public Sphere specified** — 12 capabilities | EXPANDED | 15.17a | Four boundaries stated: not Reader Knowledge, not Belief, not Media, not Politics |
| 6 | **Media Ecosystem specified** — 13 capabilities | EXPANDED | 15.17b | The Overtone's five-partition presence made operable inside a simulated landscape |
| 7 | **Simulation → WSV commit path** | CLARIFIED | 15.22 | Stated once in one place; three checks along it |
| 8 | **WSV lean rule** with worked illustration | CLARIFIED | 13.10 | Values in WSV; definitions in models; meaning in WSVR; history in WSV-H |
| 9 | **Named repository realizations, inline** | ADDED | 12.15, 15.17, 15.19, 15.21, 17.18, 18.9, 18.11, 22, 23.4, 27.5 | Each names the component, disposition, contract, source-of-truth class, what it does *not* supply, degraded mode, and exit |
| 10 | **Editorial Taste pipeline** with signal/judgment split | EXPANDED | 17.17, 17.18 | Measurable signals are extracted; editorial judgments are authored |
| 11 | **Writer Persona deepened** — 14 described properties | EXPANDED | 17.19 | No Writer Engine; the persona is a record and the drafting is a role |
| 12 | **Universal Record ↔ Visual Library relationship** | ADDED | 13.6c | Every kind declares its permitted visual roles; an empty relationship is defined, not undefined |
| 13 | **I-100** | ADDED | 36.13 | The environment boundary made an invariant |

**Realizations recorded, by disposition.** ADOPT: SALib, FAISS, SimPy, Pillow, scikit-image, SQLite + FTS5, DuckDB, JSON Schema, Hugo, NetworkX. ADAPT: Docling, OpenCLIP, Mesa, PySD, LinkML, OpenSeadragon. WRAP: Surya, ImageMagick/Wand. COMPOSE: LanceDB (conditional), PySD. FORK: a halftone module if used. BUILD-NATIVE with nothing behind the boundary: Creative Memory integrity, durable workflow execution, the Mutation Coordinator, the Context Builder. REJECT: server-based vector stores, server-based search, embedded graph databases as edge stores, durable-workflow platforms, server-based transparency logs, and any browsable database surface on the public side.

**The rule every realization obeys.** *A component supplies a computation; it never supplies a meaning.* Each realization states what the component does **not** provide, and that column is the one that matters — it is where the native semantics are enumerated by exclusion.

**Preservation check.** The complete 104-capability inventory remains visible and explicit; **P-32 was not answered by deleting capabilities.** All 36 sections, order and hierarchy unchanged. All prior invariants carried.

**Open after this revision.** **CLOSED by revision:** kind-code width (two characters) · specialization vs `<kind>_type` (`kind` + `<kind>_type`) · `visual_refs` policy (Registry-defined, three values) · WSV-H granularity (one entry per tick) · reveal-state cardinality (dissolved — epistemic state is subject-relative) · department taxonomy (architectural rule frozen, roster deferred to implementation) · `derivation` field name (retained) · Registry/COM sequencing (bootstrap + lockstep). **REMAINING OPEN:** Epistemic and Production implementation schemas (§13.6b, open by design) · Registry *content* (extensible by design) · Issue field sets beneath the frozen hierarchy · the 37 model-family specifications (generic contract closed) · taste-corpus schema · voice-profile representation · `ERA` classification · four benchmark-gated component selections. **No open item was silently frozen, and none was silently reopened.**

---

### 35.11 v0.6.3 → v0.7.0 — Canon Object Model Superseded by the Record System

*(Constitutional Amendment under §10.4 in respect of the governing object architecture. The Spine remains ten laws, unamended — a fourth successive version declines to add an eleventh.)*

**Statement of defect (§10.4 step 1).** v0.6.1 generalized "Canon Object" into a universal data abstraction and asserted that every record the system holds is one, differing by a `kind` field. The assertion could not be maintained, and v0.6.1 itself began abandoning it in the same version: §13.6d had to specialize packages per partition, conceding that *"forcing World topology onto a registry definition or a published page would be a uniformity that costs more than it returns."* By v0.6.3 the universal object survived only as a name over a list of exceptions, while continuing to impose properties on partitions that could never populate them and a single vocabulary on six models with different semantics. **The defect is not that the model was wrong about World. It is that a claim proven in World was asserted in six places.**

**Impact analysis (step 2).** Sections 12.9, 13 (throughout), 13.6, 13.6d, 13.7, 13.9, 13.9a, and the invariant register are affected. **No canon exists** — the migration obligation remains satisfied-by-absence exactly as recorded at §10.4, and returns in full when the first canonical record is written. The companion Record Model Schema, the Roadmap, and artifacts 001–032 are **not** revised or audited here.

**Counter-case (step 3), recorded because it is genuine.** *Leave it alone.* §13.6d already delivered the practical benefit — packaging was already model-owned in substance — so the remaining defect was arguably vocabulary, and vocabulary change across a live lockstep group carries real cost and no runtime benefit. **Why it was not accepted:** a name that asserts what the architecture denies does not stay inert. It had already produced the error twice — once in v0.6.1's own generalization, and once in a downstream research package that read the universal object as literal and proposed to redesign six models around it. The counter-case correctly identifies the cost and underestimates the recurrence.

**What changed:**

- **Canon Object Model superseded and retired** as the governing architecture (§13).
- **Record System established** as the governing architecture, with **six sovereign Record Models** (§13, §13.0).
- **Record, Record Model, Canon, and Canonicality explicitly held apart** (§13.0). The blueprint no longer states, and now forbids, *every Record is Canon* · *every Record is canonical* · *Canon = Record*.
- **`COR` → Relationship Record** and **`COH` → History Record**, both **scoped to the World Record Model** and explicitly declared **not** Record System primitives (§13.9).
- **"COH is universal" replaced** by the correct claim: the **P-18 obligation** is universal; the **packaging** of a temporal account is model-owned (§13.6d).
- **§13.6d reclassified** from a list of exceptions to a universal package into the statement that packaging is model-owned.
- **§13.7a added** — shared infrastructure is separated from shared semantics, with nine explicit prohibitions against a universal Record base, relationship, history, lifecycle, canonicality, kind taxonomy, identity grammar, state model, or schema.
- **§13.7b added** — provenance, audit, history, revision, version, and lineage separated; the unqualified word *lineage* retired.
- **§13.7c added** — canonicality is model-defined, with six distinct meanings tabulated.
- **The `CO` abbreviation retired**, which dissolves rather than manages the `CO`(Concept) collision v0.6.3 had to warn about (§13.9a).
- **Companion document renamed** Canon Object Model → **Record Model Schema** (§13.7). **It has not been revised** — FG-V7-01.
- **Invariants:** I-11 scope flagged (AD-11), I-16 amended in wording, I-72 scoped, **I-101–I-104 added**. None retired. Register stands at **104**.
- **Repair pass (post-forensic-audit).** A forensic audit of the first v0.7.0 draft found that the invariant register still encoded the retired v0.6.1 architecture. Corrected: **I-87** amended — Record is the common *architectural* unit, not a universal semantic model, and Record semantics are owned by the Record Model. **I-90** amended — the claim *"History Record is universal across all six partitions"* is **removed**; traceable evolution is required of every model and the mechanism is model-owned. **I-73, I-74, I-85** scoped conditionally. **P-17** separated into a universal obligation and a model-owned mechanism.
- **AD-1 resolved — the identity grammar is universal.** `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]` is constitutional across all six Record Models (§13.9a, I-82). §13.7a's draft prohibition on a universal identity grammar was **wrong and is removed**; the correct boundary is that a universal identity *grammar* is not a universal Record *semantics*. §13.9a's partition row, which had listed four partitions since v0.6.1, is corrected to six.
- **Historical accuracy restored.** The v0.6.1 prologue, the v0.6.1 changelog row, §13.6d's legacy note, and two attribution sentences had been mechanically re-termed by the migration, making them describe the *retired* claim in the *new* vocabulary. All now read "Canon Object" where they describe v0.6.x and are marked as superseded.
- **Conformance stated (§34.1)** — architectural conformance separated from implementation readiness, with the deferrals enumerated.
- **Registry established as a sovereign Record Model (§13.6e, new).** Registry definitions are **Records**, not configuration. The authority boundary is stated: *Registry governs the definitions; each Record Model owns its Records.* Dependency direction confirmed downward-only and asymmetric. **WSV attribute definitions** distinguished three ways — Registry-owned definition, World-owned value, universal field of nothing. **The bootstrap problem is stated and not solved** (FG-V7-05).
- **Kind taxonomy status stated per model (§13.6).** Only **World** is ESTABLISHED/FROZEN. Registry is ARCHITECTURE FROZEN / CONTENT EXTENSIBLE. E, P, V, and I are **BOUNDARY-NAMING** — a listed roster is not a frozen taxonomy, on §13.6a's own reading.
- **§13.6d package rows marked PROVISIONAL for the five non-World models** (FG-V7-06). A provisional row may not be implemented as a requirement, and a model may conclude it needs no History Record at all.
- **Invariants added: I-105–I-108** — Registry sovereignty, roster non-freeze, package provisionality, no default WSV attribute. Register **108**.
- **Registry demotion removed (§29.1).** The domain-vs-capability list still read *"**The Registry** is a *capability* — definitional infrastructure"* — accurate before v0.6.1 promoted Registry to a partition, false after. Registry is a **sovereign Record Model** (I-105); it appears nowhere in the flywheel because it is **upstream** of it.
- **§26 adapter-native list scoped.** Record, Relationship Record, History Record, WSV and WSV-H were listed as unqualified natives; they are now marked **World Record package constructs** that an adapter must not assume in another model.
- **§13.6d package rows reclassified PROVISIONAL → MODEL-DESIGN INPUT**, with the governing principle tabulated: W established, E/P/V/I model-owned, **R Registry-owned**. The v0.6.1 table is retained as evidence, not as a freeze.
- **Generic sections carrying World mechanics scoped (§§13.3, 13.4, 13.5, 13.7).** §13.5's *"one History Record"* and `coh_ref`, §13.4's locked/world-state/derived split, §13.3's Relationship Record packaging, and §13.7's *"every object has a partition, a kind, a tier, a status, provenance, and derivation"* were all stated under generic headings. Each is now scoped to the **World Record Model**, with the general **principle** separated from the World **mechanism** where one exists. The universal envelope is the bootstrap set and no more.
- **§13.6 retitled.** The heading read *"The Three Partitions and the Kind Taxonomy"* — stale since v0.6 and v0.6.1. Its content had been correct for six models for two versions; only its title had not.
- **Openness preserved and extended:** `tier` applicability outside W/E flagged **FG-V7-03**; the four identity operations scoped to World with the other five models' meaning left OPEN.

**What deliberately did not change.** The Spine. The six partitions and their boundaries. The World taxonomy of seven instance-bearing kinds plus the WSV singleton. All six kind rosters. Identity partition-first with two-character kind codes. Manifestation-blindness, the Publishing Firewall, the single gated mutation path, the Registry's three boundaries, source-of-truth classification, and the §13.7 custody split. **Every OPEN item in v0.6.3 remains OPEN** — §13.6a's Issue interior, §13.6b's Epistemic and Production schemas, §13.10's WSV resolution flag, and §13.12's frozen causal vocabulary. v0.7.0 closes none of them, because closing an OPEN question to make a document look complete is the failure §13.6b was written to prevent.

**Deferred by this revision, explicitly.** Implementation impact remains to be established by the subsequent repository audit. Roadmap revision is a subsequent phase derived from Blueprint v0.7.0 and the 001–032 audit. Artifact 033 and the subsequent artifact sequence will be re-derived after v0.7.0 is accepted and 001–032 are audited.

---

## 36. Invariant Register

The blueprint's normative claims, consolidated. **This section adds no new rule** — it is an index, and where it appears to differ from the defining section, the defining section governs.

**v0.5 re-check result: all 70 v0.4 invariants carried forward, none retired, two amended in wording (I-25, I-62), ten added (I-71–I-80).**

**v0.7.0 re-check result: all 100 carried forward. **None retired.** Six amended — I-11 (scope flagged, AD-11), I-16 (wording, Record Models), I-72 (scoped to World), I-73/I-74 (conditional on the model using Relationship Records), I-85 (model's own temporal mechanism), plus **I-87** (architectural unit, not universal semantic model) and **I-90** (universal History Record removed). **Eight added (I-101–I-108).** The register stands at one hundred and eight.** The Spine remains ten laws — a fourth successive version declines to add an eleventh.

**v0.6.3 re-check result: all 99 carried forward. None retired. None amended. **One added (I-100).** The register stands at one hundred.**

**v0.6.2 re-check result: all 96 carried forward. None retired. None amended. **Three added (I-97–I-99)** after auditing thirteen proposals, ten of which were redundant. The register stands at ninety-nine.**

**v0.6.1 re-check result: all 86 carried forward. None retired. One amended in wording only — I-16 (six partitions). **Ten added (I-87–I-96).** The register stands at ninety-six.**

**v0.6 re-check result: all 80 carried forward. None retired. Three amended in wording only — I-16 (four partitions), I-25 (axis naming), I-62 (issue ordinal) — none changing meaning. **Six added (I-81–I-86).** The register stands at eighty-six.**

### 36.1 Truth and Authority

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

### 36.2 Traceability and History

> **REQUIRES AUTHOR DECISION — AD-11 (recorded v0.7.0).** I-11 as written at v0.6.3 binds *"every Canon Object"* to exactly one logical history record. Read as a **World** invariant it is unaffected by the Record System supersession; read as a **universal** invariant it constrains the temporal architecture of five Record Models before those models exist, which §13.7a forbids. **v0.7.0 adopts the World reading and records the ambiguity rather than resolving it silently.** The universal obligation that survives either reading is P-18 (I-09), which binds all six.

| # | Invariant | Where |
|---|---|---|
| I-09 | Every canonical state answers: what changed, when, why, who approved it, what caused it. | P-18 |
| I-10 | Authorial intent is a valid terminal cause; fabricated causality is a violation. | §5.2, §15.13 |
| I-11 | **(scope flagged v0.7.0 — AD-11)** Every **World** Record has exactly one logical history record, append-only and owned by Canon — the History Record for the seven instance-bearing kinds, WSV-H for WSV. Every Record Model must satisfy P-18 in full; the packaging of its temporal account is model-owned (§13.6d). | §12.9, §13.10, §13.6d |
| I-12 | Compaction may remove detail, never the existence of a revision, and never the P-18 answers. | §12.9, §12.14 |
| I-13 | No history is ever orphaned: every predecessor history is reachable from its successors. | §13.8 |
| I-14 | Approval mode is recorded, not merely the fact of approval. | P-23, §12.7 |
| I-15 | Amendments to this blueprint satisfy P-18 at a ceremony above Foundational. | P-28, §10.4 |

### 36.3 Classification and Boundaries

| # | Invariant | Where |
|---|---|---|
| I-16 | **(amended v0.6.1; amended in wording v0.7.0)** Every Record carries exactly one partition — World, Epistemic, Production, Registry, Visual Library, or Issue — and every partition owns exactly one sovereign Record Model. Cross-partition conversion is prohibited. | §13.6, §13.6a, §13.6c, §13.2 |
| I-17 | World records are manifestation-blind absolutely; no field may reference an issue, tier, medium, or artifact. | §11, §13.6 |
| I-18 | Any state recording an authorial act is Production State and survives every rebuild. | P-26, §9.1 |
| I-19 | Derived state is exactly what can be recomputed with no loss; if it cannot be, it was misfiled. | §12.4 |
| I-20 | Every capability declares its current; failure posture follows from it. | P-19, §8.4 |
| I-21 | Every cross-cutting capability has exactly one owning domain. | §9.2 |
| I-22 | Nothing is admitted as a domain that does not pass all five domain tests. | §9.3 |

### 36.3a Rules Added by v0.7.0

| # | Invariant | Where |
|---|---|---|
| I-101 | Every partition owns exactly one sovereign Record Model. No Record Model is a specialization of another, and no Record Model is the template for another. | §13, §13.2 |
| I-102 | Relationship Record and History Record are World Record Model concepts. Neither is a Record System primitive, and neither may be required of another Record Model. | §13.9, §13.6d |
| I-103 | A mechanism may be shared across Record Models; a semantic may not be shared without evidence in each model that carries it. Shared infrastructure never confers shared meaning. | §13.7a |
| I-104 | Record and Canon are not synonyms. Canonicality is a status property whose meaning is defined by each Record Model that has one, and two models hold Records that are never canonical. | §13.0, §13.7c |

### 36.3b Rules Added by the v0.7.0 Constitutional Revision

| # | Invariant | Where |
|---|---|---|
| I-105 | Registry is a sovereign Record Model. Its definitions are Records, not configuration. Registry holds semantic authority over definitions and never semantic ownership of another model's Records. | §13.6e, §9.4 |
| I-106 | A kind roster that is listed is not thereby frozen. Only the World taxonomy is established; every other roster names a boundary and is revisable by that model's own design work until it declares otherwise. | §13.6, §13.6a, §13.11 |
| I-107 | A package composition declared for a Record Model that has not been independently designed is provisional and may not be implemented as a requirement. | §13.6d, FG-V7-06 |
| I-108 | No Record carries a WSV attribute by default. An indicator definition is a Registry Record; an indicator value is World-state; neither is a universal field. | §13.6e, §13.10, I-91 |

### 36.4 Change, Time, and Scale

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

### 36.5 Knowledge and Reading

| # | Invariant | Where |
|---|---|---|
| I-31 | Truth and knowledge-about-truth are separate records, connected by reference, never merged. | §14, §13.6 |
| I-32 | Every epistemic transition has an evidence path or an authored decision. | §14.6, §14.7 |
| I-33 | Reader knowledge changes canon only through a gated Reader Knowledge Proposal. | §20.4 |
| I-34 | Epistemic tracking is selective, criterion-recorded, and budgeted. | §14.17 |
| I-35 | Modelled reader state is an assumption and is labelled as one everywhere it is shown. | §20.6, §27.2 |
| I-36 | Withheld canon is excluded from every role context by default; inclusion is justified and recorded. | §24.7 |
| I-37 | Leakage of hidden canon is a structural violation and blocks where determinable from structure alone; where establishing it requires interpreting prose or an image, it is a judged finding at high severity. | §14.16, §24.7, P-24 |

### 36.6 Operation and Survival

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

### 36.7 Rules Added by the v0.4 Constitutional Repair

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

### 36.8 Rules Added by the Round 2 Repair

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

### 36.9 Rules Added by v0.5

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

### 36.10 Rules Added by v0.6

| # | Invariant | Where |
|---|---|---|
| I-81 | Issue is not Canon. Nothing is true because it was published. An issue may reference a World record; it never owns one, and no World record may reference an issue. | §13.6a, §11 |
| I-82 | Identity is partition-first and stable: `[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]`. A rename never creates a new canonical identity, and an internal machine identifier never replaces or contradicts the canonical one. | §13.9a |
| I-83 | The Mutation Coordinator is the only component that writes canon. Stages may be delegated to external components; the write boundary may not. Execution-substrate guard rails are defence-in-depth, never constitutional authority. | §12.6 |
| I-84 | No external component holds canonical semantics, defines a kind, owns a relationship, adjudicates a mutation, or is the only place a canonical fact exists. Every external store is DERIVED or CACHED, never AUTHORITATIVE, and the system remains fully recoverable if it is deleted. | P-31, §26.2a, §26.2d, §29.6a |
| I-85 | **(scoped v0.7.0)** Version control records that files changed; a Record Model's own temporal mechanism — the History Record and WSV-H in World — records what canonically changed and why. Semantic history is never reconstructed from a commit log. Correlation may be recorded in one direction only, from history entry to commit. | §26.2e |
| I-86 | A timestamp produced by an external system is operational metadata. It becomes World Time, Session Number, or Real-World Time only by being recorded as such through the mutation path — never by having been generated by a tool. | §12.16, §26.2e |

### 36.11 Rules Added by v0.6.1

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

### 36.12 Rules Added by v0.6.2

**Thirteen invariants were proposed for this version. Ten were found redundant and are mapped to the existing register rather than duplicated; three were genuinely new.** Duplicating an invariant is worse than omitting one — a register with two statements of one rule invites them to drift apart.

| Proposed | Disposition |
|---|---|
| WSV stores values, not model definitions | **Redundant** → I-91 |
| Indicator semantics belong to Registry | **Redundant** → I-91 |
| Simulation Model semantics belong to models, not WSV | **Redundant** → I-91 |
| An indicator has exactly one canonical home | **Redundant** → I-79 |
| Simulation may propose deltas but not bypass the mutation path | **Redundant** → I-04, I-83 |
| Cross-model dependencies must be explicit | **Redundant** → I-93 (declared dependency is what makes conflict resolvable) |
| A Record may reference V without V becoming a source of truth | **Redundant** → I-89 |
| Visual analysis does not become canon without governed mutation | **Redundant** → I-89 |
| External tools cannot own semantic authority | **Redundant** → I-84 |
| Published Issue records cannot mutate World Canon | **Redundant** → I-81 |
| Taste criteria are guidance, not canon | **Partly redundant** → I-95; sharpened as **I-97** |
| Writer Persona does not redefine Character Canon | **New** → **I-98** |
| Public Sphere state ≠ Reader Knowledge, in both directions | **New** → **I-99** |

| # | Invariant | Where |
|---|---|---|
| I-97 | A taste criterion is editorial guidance and is never canon. It constrains how the work is made, asserts nothing about the world, and enters governance as a judged finding that the author may override with a recorded reason. | §17.17, §19 |
| I-98 | A Writer Persona never redefines Character canon. A persona describes how someone writes; what is true of that person is a World record, and a persona's claims about its own author are Production, not fact. | §17.19, §13.6 |
| I-99 | Public Sphere state and Reader Knowledge are never derived from one another in either direction. What the world's public believes is a simulated in-world condition; what a reader tier knows is an out-of-world epistemic state reached only through published artifacts. Neither is evidence for the other. | §15.17, §14.7 |

### 36.13 Rules Added by v0.6.3

| # | Invariant | Where |
|---|---|---|
| I-100 | The execution environment runs coolboy12 and does not define it. It is not a domain, partition, engine, or primitive, and it owns no coolboy12 semantics. Its guard rails are defence-in-depth; where a guard rail and the Human Gate disagree, the gate governs. The architecture must remain valid when the environment is replaced. | P-33, §9.5, §26.8 |

**Conformance.** An implementation conforms to coolboy12 v0.6.3 when all one hundred invariants hold, **and when the Record Model Schema holds alongside it in lockstep** (§13.7) — which means at the same version for every contract either document expresses, not that either must be complete before the other begins. **Additionally: the anonymisation test (§29.7) and the rebuild-from-canon drill (§29.8) must both pass, and no external component may appear in an AUTHORITATIVE role in the source-of-truth classification (§29.6a).** Where an invariant cannot be satisfied, that is a constitutional finding requiring an amendment (§10.4) — not an implementation shortcut, and never a silent one.
