# COOLBOY12 — Rebuild Conventions

**Artifact 020** · `docs/conventions/rebuild.md` · Own: CONST · RM: n/a · T: doc · R: CONTRACT ·
SoT: AUTHORITATIVE · Auth: governing · Canon: n/a · CD: no · Ph/St: P0/0d · Req: BR-107 ·
BP: §29 · RMS: §4 · H: 016 · S: — · LS: — · G: — · → P8 · Risk: medium · ∥: yes

## 1. Purpose

This document answers one question: **how must a DERIVED thing be able to return from nothing
but its authoritative source(s)?**

It fixes one obligation — every DERIVED artifact declares its authoritative source and how it is
rebuilt from that source — and the consequences that follow. It is a convention. It builds no
engine, defines no algorithm, and creates no derived data.

## 2. Scope

Artifact 016 fixed the six source-of-truth classes. This document adds the operational
consequence of exactly one of them: **DERIVED**. It does not restate 016's taxonomy.

| Question | Artifact |
|---|---|
| What source-of-truth class is this? | **016** |
| Which zones are canonical, and who may write them? | **017** |
| When do we return to an operational state? | **019** |
| **How must a DERIVED thing be rebuildable from its source?** | **020 — this document** |

The formal derived-layer architecture, the full rebuild contract, staleness machinery, the
engine, and the proof all sit downstream and are enumerated in §14.

## 3. Rebuildability Is Constitutional

Blueprint §29.6a classifies **DERIVED** as *"Recomputable with no loss from authoritative
sources."* P-26 states the same rule from the other direction, and states the penalty for
getting it wrong:

> **P-26 — Authored state is not derived state.** *"Derived state is exactly and only what can
> be recomputed from Canon, Production State, and history with no loss. Filing authored state as
> derived is data loss with a delay."*

§29.6a draws the consequence explicitly: *"A `DERIVED` value that cannot actually be rebuilt is
a misfiled `AUTHORITATIVE` value (P-26)."*

This is not advisory. A derived artifact that *should* be rebuildable, or is *normally*
rebuildable, or can *usually* be regenerated, is not classified DERIVED — it is misclassified
and the classification is the defect.

## 4. The Obligation

> **Every DERIVED artifact declares its authoritative source(s) and the method by which it is
> rebuilt from them.**

This is Artifact 020's whole normative content. Everything below states what the obligation
means, what satisfies it, and what does not.

**A derived artifact with no declared source has no defensible rebuild direction, and therefore
no valid DERIVED classification.** Source declaration is not optional and is not deferred to
runtime.

## 5. What a Declaration States

Every DERIVED artifact declares at least these four things. This is a convention for how a
derived artifact is described, **not** a schema, a field list, or a machine-readable format —
Artifact 167 owns the formal derived-artifact contract.

| | |
|---|---|
| **Source** | The authoritative input(s) from which it can be rebuilt. |
| **Method** | The transformation that reconstructs it, expressed as a capability. |
| **Output** | The derived artifact produced. |
| **Failure** | What constitutes a failed rebuild, and what that failure means (§11). |

**The Method is stated as a capability, not as a command.** §29.7 fixes what passing looks like:
sections describe *"capabilities, contracts, and boundaries"*, and its own worked instance is
*"an index that can be rebuilt from canonical records"* (P-31). A rebuild method written as *"run
the current tool's command"* fails that test the moment the tool changes. Write *"re-index the
authoritative Records into the search projection"* — a description a future implementation can
satisfy with different tooling. Tool-specific invocation belongs to implementation artifacts, not
here.

P-27 is a separate requirement, and it is about the *records*: Canon, History Record, Production
State, and Creative Memory must stay interpretable *"without the application that produced them"*.
It constrains the stored state, not how a rebuild method is phrased.

## 6. Authoritative Sources

P-26 names what derived state may be recomputed from: **Canon, Production State, and history.**
The declared source must be the authoritative input this particular artifact actually depends
on, matching its owning architecture — not `canon/**` by reflex.

Two limits on that list:

- **History is not a generic rebuild source.** History may be an authoritative source where a
  model's architecture uses it that way. The History Record is a World Record Model concept and is
  not a Record System primitive (I-102); WSV is a *"World-owned singleton"* (RMS §10.7) and WSV-H
  is its history. Traceable evolution is required of every Record Model, but *"the mechanism is
  model-owned"* (I-90). Nothing here universalizes World's mechanism across the other five models.
- **Authored state is never rebuilt.** Schedules, plans, dismissals, deferrals, preferences and
  other authorial acts are Production State — *"durable, provenanced, and never destroyed by a
  rebuild"* (P-26). A derived representation of an authorial act is never treated as that act's
  source. This is the main protection against a lossy rebuild.

**Model ownership is preserved.** The rebuildability principle, the source declaration, the
non-authority of output, and the rebuild direction are universal, and RMS §4 supports that half
directly: it places source-of-truth classification among the universal mechanisms and marks it
*"Constitutional"* — explicitly **not** model-owned — and it lists indexing as universal with the
note *"Never authoritative; indexes are derived."* What that machinery is applied to does not
follow from it. A semantic is not shared across Record Models without evidence in each model that
carries it (I-103), and RMS §4 draws that same line where it splits structural from semantic
validation and provenance capture from provenance meaning. So *which* authoritative inputs a
particular derived artifact depends on, what its output *means*, and the semantics of the
transformation are settled by the Record Model concerned and not here. This document creates no
universal derived semantic model.

**What RMS §4 does not say.** RMS §4 contains no occurrence of *rebuild*, *derived artifact*, or
*transformation*, and states no rebuild rule. The model-ownership line above rests on I-103 and on
RMS §4's own mechanism/semantic split, not on a derivation clause in §4. RMS §4's classification
row also reads *"§29.6a — five classes"* where this document follows Artifact 016's six; that
discrepancy is CONFLICT-C in the Revolving Resolution Note and is not resolved here.

## 7. Direction of Derivation

§26.2d fixes the direction and states the prohibition in the same breath:

```
canonical records  →  projection / index builder  →  external store
```

*"and never:"*

```
external store  →  canon
```

Generalized to every derived artifact, the only permitted direction is:

```
AUTHORITATIVE  →  rebuild  →  DERIVED
```

Four directions are therefore prohibited, and each is a real failure mode:

| Prohibited | Why |
|---|---|
| `DERIVED → "repair" → AUTHORITATIVE` | §26.2d: *never* `external store → canon`. Derived output never becomes the source. |
| `EXTERNAL TOOL → "truth" → DERIVED` | Invalid where the tool is the only place the semantic input exists (I-84, P-27). |
| `Git history → DERIVED` | Artifact 013: a commit records that a file changed, never what changed canonically. Git supplies operational file-version information, never the semantic source. |
| `previous derived store → DERIVED` | A rebuild that needs the artifact it is rebuilding has proven nothing. |

**A rebuild method may not secretly depend on** the previous derived store, an undeclared cache,
Git history, external service state as the only semantic source, an undocumented mutable file,
operator memory, or a hidden database. If deleting any of those loses the meaning, that thing was
authoritative and the classification is wrong.

## 8. Full Rebuild and Incremental Rebuild Are Not the Same Thing

| | |
|---|---|
| **Full rebuild** | The target derived store is discarded and recreated entirely from authoritative inputs. This is the constitutional requirement and the strongest proof of rebuildability. |
| **Incremental rebuild** | Only affected derived material is updated after an authoritative change. This is a performance optimization. |

**An incremental strategy never replaces the requirement for a valid full-rebuild path.**
Incremental optimization is not a source of truth, and a system that can only update
incrementally has not demonstrated that its derived store is derived. This document defines no
incremental algorithm; Artifact 227 later implements staleness propagation.

## 9. Dependency Chains Bottom Out in Authoritative Sources

A derived artifact may mechanically consume another derived artifact during normal operation,
provided its authoritative dependency chain is declared and reconstructable. What matters is
where the chain *ends*.

```
Canon  →  index  →  search view
```

A search view may read the index in normal operation. Its declared rebuild chain must still
resolve to the authoritative source without requiring the deleted view or the deleted index as
irreplaceable semantic state. **Distinguish the direct dependency from the ultimate authoritative
source**; only the latter satisfies §4.

No dependency-graph mechanism is defined here.

## 10. Staleness and Rebuild

```
authoritative change
        ↓
dependent DERIVED may become stale
        ↓
stale output is still non-authoritative
        ↓
rebuild restores freshness
```

A stale derived artifact does not become authoritative by being stale, and does not become
authoritative by being the most recent thing available. This document states the relationship
only. The stale-derived-state policy is **Artifact 158**, the staleness propagation contract is
**Artifact 173**, and the implementation is **Artifact 227**.

## 11. Failure Is a Finding

§29.8 states this outright: *"Failure is a finding, not a catastrophe. The rebuild that fails has
identified a misfiled authoritative value (P-26) — which is exactly what it was run to find, and
considerably cheaper to find this way than the other way."*

So when a DERIVED artifact cannot be rebuilt although its declared source is available:

```
rebuild failure
        ↓
architectural finding
        ↓
the classification or the declared method is wrong
```

**The failure is evidence, never a licence.** None of the following is a permitted response:
promoting the derived artifact to Canon; making a cache authoritative; copying the missing data
into the derived store; adding an undeclared external source; or relaxing the rebuild rule for
that artifact.

**A missing authoritative value is a data or architecture problem, not something a rebuild
convention may silently repair.** A rebuild never invents authored or canonical state to fill a
gap.

## 12. Delete-and-Rebuild Is the Proof

§29.8 gives the test in one sentence:

> **"Delete every derived store — every index, every embedding set, every search structure,
> every graph projection, every rendering cache — and rebuild them from canonical records alone.
> If the rebuild does not complete, the deleted store was not derived."**

The conceptual shape:

```
delete the derived store
        ↓
retain the authoritative sources
        ↓
run the declared rebuild method
        ↓
the derived store returns
```

§29.8 explains why a drill rather than a rule: *"A derived store that has never been deleted is a
store whose classification is an assumption."* It operationalizes three things that would
otherwise be assertions — the direction-of-derivation rule (§26.2d), the source-of-truth
classification (§29.6a), and the Exit Invariant (P-27).

**This document states the principle. It does not run the drill.** No derived store is deleted
here, and none exists to delete — the repository holds no derived data at P0, and this artifact
creates none. Artifact 229 later proves delete-and-rebuild; Artifact 230 is the P8 conformance
suite.

## 13. Class Boundaries and Adjacent Contracts

**The rebuild-method obligation in §4 targets DERIVED.** The neighbouring classes are not
collapsed into it.

| Class | Rebuild-relevant consequence |
|---|---|
| **DERIVED** | Recomputable with no loss from authoritative sources. **Declares Source and Method.** Non-authoritative, disposable. Examples per §29.6a: indexes, search and graph projections, analytics, materialised views. |
| **CACHED** | *"Recomputable and disposable, held only for speed"* (§29.6a) — query results, rendering caches, asset-processing caches. Non-authoritative and disposable like DERIVED, but governed by its own cache semantics (**Artifact 171**), not by §4's declaration. A cache may consume a derived artifact and still remain CACHED. |
| **TEMPORARY** | *"Exists within one workflow and does not outlive it"* (§29.6a) — working state, simulation timelines before the gate, draft proposals. Being re-creatable does not make it DERIVED, and it acquires no rebuild obligation by ending. |
| **EXTERNAL** | May supply capability for a rebuild; may never be the only place the semantic source exists. §26.2d: *"every external store is `DERIVED` or `CACHED`. There is no configuration in which one is `AUTHORITATIVE`."* |
| **AUTHORITATIVE** | Never rebuilt from DERIVED. Rebuild reads it and never writes it. |

No seventh class is created. `REBUILDABLE`, `RECOVERABLE`, `GENERATED`, `PROJECTED`, `INDEX`, and
`CACHE` are not source-of-truth classes — some name kinds of derived artifact, and the six
classes remain Artifact 016's.

**Rebuild never writes Canon.** It reads authoritative data and produces non-authoritative
output. It does not modify Canon, promote its output to Canon, bypass the Mutation Coordinator,
or constitute a canonical mutation (I-83, Artifact 017). **No rebuild output ever becomes a
source of truth** (I-84, P-26).

**Secrets stay out.** A rebuild places no secret material into a derived artifact, and a secret
value is never an authoritative rebuild source. Where a derived artifact needs operational access
to a secret-bearing external service, the secret remains EXTERNAL and outside the output
(Artifact 015).

**Restart is not rebuild.** Artifact 019 may call for rebuilding derived state on return from
dormancy; the method it calls for is this document's. Neither defines the other, and no restart,
recovery, or checkpoint state is created here.

## 14. Downstream Boundary

```
020  rebuild convention              ← this document
  ↓
158  stale-derived-state policy      docs/constitution/stale_derived.md
167  derived layer architecture      docs/constitution/derived_layer.md      (ARCH)
168  index contract · 169 projection contract · 170 view contract
171  cache policy                    docs/constitution/caches.md
172  rebuild contract                docs/constitution/rebuild_contract.md
173  staleness propagation contract  docs/constitution/staleness.md
174  P6 conformance suite
  ↓
226  rebuild engine                  src/coolboy12/kernel/rebuild.py         (IMPL)
227  staleness propagation           src/coolboy12/kernel/staleness.py
228  derived-layer validator         src/coolboy12/validation/derived.py     (VALID)
229  derived tests + worked example · 230  P8 conformance suite              (PROOF)
```

**None of these exists.** This document is upstream of all of them and implements no part of any.
Artifact 167 owns the formal derived-artifact contract and validates *"every derived artifact
declares SOURCE"*; Artifact 172 owns the formal rebuild contract and validates *"full rebuild
from canon alone."* Artifact 020 establishes the conceptual obligation at P0 so that neither has
to invent it.

## 15. A Conceptual Example

Illustrative only. Not an implementation specification, and no such artifact exists in the
repository.

```
authoritative Records
        ↓  re-index
search projection  (DERIVED)
```

| | |
|---|---|
| **Source** | the authoritative Records the projection indexes |
| **Method** | re-index the current authoritative Records into the projection |
| **Output** | the search projection |
| **Authority** | none — the projection is consulted for retrieval, never as truth |
| **Failure** | rebuild incomplete → the projection stays unavailable or stale. It does not become authority, and the incompleteness is a finding under §11. |

No search engine, index format, or storage technology is named. §29.7's anonymisation test
applies to this document as it does to the Blueprint: the convention describes capability,
source, method, output, and failure, and stays meaningful when every dependency name is removed.

## 16. Standing Rules

1. Every DERIVED artifact declares its authoritative source(s) and its rebuild method.
2. A derived artifact with no declared source has no valid DERIVED classification.
3. The only permitted direction is AUTHORITATIVE → rebuild → DERIVED.
4. A rebuild method may not depend on the previous derived store, an undeclared cache, Git
   history, operator memory, or an external service that is the only place the semantic source
   exists.
5. Rebuild output is never authoritative, and never becomes a source of truth.
6. Rebuild never writes Canon and never bypasses the Mutation Coordinator.
7. Authored state is never rebuilt from a derived representation of itself.
8. History is an authoritative rebuild source only where a Record Model's own architecture makes
   it one; World's mechanism is not universalized.
9. A valid full-rebuild path is required; an incremental strategy never substitutes for it.
10. A stale derived artifact is still non-authoritative.
11. A rebuild that fails with its source available is an architectural finding — the
    classification or the method is wrong — never grounds for creating hidden authority.
12. Delete-and-rebuild is the proof of genuine rebuildability; an untested classification is an
    assumption.
13. CACHED and TEMPORARY are not DERIVED, and no seventh source-of-truth class is created.

## 17. Boundary of This Document

This document states a convention. It implements no rebuild engine, no derived layer, no
staleness propagation, no validator, no cache, no index, and no runtime API. It defines no
schema, no field format, and no dependency graph. It creates no derived data, no canonical data,
no test, and no dependency, and it selects no vendor or tool.

It does not restate Artifact 016's taxonomy, does not redefine Artifact 019's restart contract,
and does not reach into the derived-layer contracts (158, 167–174) or the P8 implementation and
proof layer (226–230).

`Req: BR-107` is preserved as written. The requirement register is not currently available
(Revolving Resolution Note, GAP-C), so no requirement text is quoted or inferred here; this
document is validated against Blueprint §29, §29.6a, §29.8, §26.2d, P-26, P-27, RMS §4, and
Artifact 016 instead.
