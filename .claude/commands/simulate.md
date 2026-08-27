# /simulate

**This command refuses.** There is no world state to simulate over and no simulation model to
run, so `/simulate` says so and stops. Roadmap row 028 fixes all four of these surfaces the same
way — *Val: each refuses with a reason and the unlocking phase · Done: four refusals present ·
Why: RULE G3 — one responsibility, "refuse until licensed", four files.*

The entry point exists now so it is present and honest. It is not here so that something can be
simulated today.

## Role

The invocation surface for running a declared simulation model over world state.

`/simulate` does not define what a simulation is. **Artifact 241**
(`docs/models/world/simulation.md`, P9) is the simulation architecture, and it settles the shape
of this capability: *no Simulation Record Model; simulation is definition + consumption.*
**Artifact 250** (`docs/constitution/sim_runtime.md`) draws the line this surface sits on —
*defining a model ≠ running it.* Neither is built.

Blueprint §7 P-16: simulation is a temporal reasoning system *"and its output is always
provisional until gated."*

## Input

Nothing yet, because no simulation model exists to name.

When the capability exists, the input is a declared simulation model and its horizon. An absent
or ambiguous target will be reported as unresolved — never resolved to *every model* or *the
whole world state*. Do not accept a model supplied inline in place of a declared one; this
surface would run declared models, not authored ones.

## Behavior

Refuse, and say why.

1. State that the simulation capability is not available.
2. Give the reason: **the simulation layer is unbuilt.** The capability is constituted by the
   World State Vector (Artifact 232), the simulation architecture (241) and the runtime boundary
   (250), and it is not available until they are. The reason is that absence, not today's world
   state — world state arriving first would give a model something to read and still leave
   nothing declared to run against it, so a partly built P9 does not make this command runnable.
3. Name what would unlock it: **Phase P9 — WORLD STATE + SIMULATION (artifacts 231–252)**.
4. Stop.

Do not partially run. Do not produce an illustrative, approximate, or hand-reasoned result in
place of a simulation — a narrative account of what *might* happen is not a simulation output,
and offering one here would put an unlabelled guess where a provisional, gated artefact belongs.
Refusing is this command's correct behaviour, so the refusal is reported as a refusal, never as a
failure and never as a pass.

## Boundary

Reading `canon/**` is permitted; a simulation reads world state. Changing it is not.

`/simulate` must never edit or write a canonical Record, Relationship Record, History Record,
WSV, WSV-H, Registry definition, epoch baseline, or published artifact — and never repair,
normalise, migrate or regenerate any of them. There is no `--fix` here. **A simulation result is
provisional and never becomes canon by being produced** (§7 P-3); the route from any result to
canon runs through the gate, which is itself unbuilt.

It creates no directory, no output area, and no state of its own. It stores no run, mints no
identifier, and persists nothing.

It holds `Auth: none`. Never treat a git commit as approval: version control records file
changes and carries no canonical authority.

## Output

A refusal naming the capability, the reason, and the unlocking phase. Nothing else, and nothing
persisted.

## Stop condition

Stop at the refusal.

```text
/simulate → REFUSAL ┊ (world state → declared model → run → provisional result)
                    ┊
         this command stops here; everything right of the line
         is unbuilt, and none of it is reachable from here
```

Do not chain onward into checking, approval, or any write, and do not treat a request to proceed
anyway as permission. The refusal is the whole command until P9 exists.
