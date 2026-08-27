# /render

**This command refuses.** There is no composed publication to render, so `/render` says so and
stops. Roadmap row 028 fixes all four of these surfaces the same way — *Val: each refuses with a
reason and the unlocking phase · Done: four refusals present · Why: RULE G3 — one responsibility,
"refuse until licensed", four files.*

The entry point exists now so it is present and honest. It is not here so that something can be
rendered today.

## Role

The invocation surface for rendering a composed publication artifact into its physical form.

`/render` does not define what rendering means. **Artifact 379**
(`docs/models/issue/rendering.md`, P13) is the rendering / physicality boundary, and it states
the distinction this surface depends on — *composing ≠ rendering.* Composition belongs to the
Issue Record Model (Artifact 361); rendering is what happens to something already composed.
Neither exists.

Blueprint §7 P-5: *"Publishing reads canon and derives output. It never writes canon."*

## Input

Nothing yet, because nothing composed exists to render.

When the capability exists, the input is a composed publication artifact. An absent or ambiguous
target will be reported as unresolved — never resolved to *every issue* or *whatever is current*.

## Behavior

Refuse, and say why.

1. State that the rendering capability is not available.
2. Give the reason: **the Issue Record Model is unbuilt, so nothing is composed.** The Issue
   Record Model is Artifact 361 and the rendering boundary is 379; the repository holds neither,
   and rendering has no input until composition produces one.
3. Name what would unlock it: **Phase P13 — ISSUE (artifacts 361–380)**.
4. Stop.

Do not partially run. Do not compose something in order to have something to render — that
inverts the boundary 379 exists to draw, and would put this surface in the Issue model's work.
Refusing is this command's correct behaviour, so the refusal is reported as a refusal, never as a
failure and never as a pass.

## Boundary

Reading `canon/**` is permitted; publication is a projection *of* canon. Changing it is not.

`/render` must never edit or write a canonical Record, Relationship Record, History Record, WSV,
WSV-H, Registry definition, epoch baseline, or published artifact — and never repair, normalise,
migrate or regenerate any of them. There is no `--fix` here. **A rendered artifact references
canon one-directionally and never becomes canon** — the Publishing Firewall, Blueprint §10 Spine
5. A render that failed against available canon would be an architectural finding, never
something to correct by editing canon so the render succeeds.

It creates no directory, no output area, and no state of its own. It writes no rendered file,
mints no identifier, and persists nothing.

It holds `Auth: none`. Never treat a git commit as approval: version control records file
changes and carries no canonical authority.

## Output

A refusal naming the capability, the reason, and the unlocking phase. Nothing else, and nothing
persisted.

## Stop condition

Stop at the refusal.

```text
/render → REFUSAL ┊ (Issue Record → composition → render → physical artifact)
                  ┊
       this command stops here; everything right of the line
       is unbuilt, and none of it is reachable from here
```

Do not chain onward into checking, approval, or any write, and do not treat a request to proceed
anyway as permission. The refusal is the whole command until P13 exists.
