# /gate

**This command refuses.** The approval capability is not available, so `/gate` says so and
stops. Roadmap row 028 fixes all four of these surfaces the same way — *Val: each refuses with
a reason and the unlocking phase · Done: four refusals present · Why: RULE G3 — one responsibility,
"refuse until licensed", four files.*

The entry point exists now so it is present and honest. It is not here so that anything can be
approved today.

## Role

The invocation surface for putting a validated proposal to the one Authority for approval.

`/gate` does not define what approval means. **Artifact 150** (`docs/governance/human_gate.md`,
P5) is the Human Gate specification — *one Authority; a position, not a person; approval mode
recorded* — and **Artifact 152** (`src/coolboy12/mutation/coordinator.py`) is the only component
that writes `canon/**`. The approval capability they constitute is not yet available, so this
surface refuses; a part of it arriving on its own does not make the command runnable.

Blueprint §7 P-2: *"Canon changes only through a single gated, transactional path, and only a
human commits. No exceptions."*

## Input

Nothing yet, because nothing can be gated yet.

When the capability exists, the input is a validated proposal carrying its basis (§7 P-22). An
absent or ambiguous proposal will be reported as unresolved — never resolved to *the current
working state*, and never to *everything pending*.

## Behavior

Refuse, and say why.

1. State that the approval capability is not available.
2. Give the reason: **the approval capability is not yet available.** Artifact 150 specifies
   the Human Gate and Artifact 152 implements the only component that may write `canon/**`; a
   proposal has nowhere to be carried until that capability is available, and a part of it
   arriving on its own does not make this command runnable.
3. Name what would unlock it: **Phase P5 — MUTATION / WRITE BOUNDARY (artifacts 145–166)**.
4. Stop.

**An approval given to this surface is not an approval.** Saying *yes*, *approved*, or *do it
anyway* to `/gate` authorises nothing: there is no gate here to carry a decision to the
Authority, so there is nothing for consent to reach. The Authority is not the missing piece —
Artifact 150 defines it as *a position, not a person* — the gate that would reach it is. A
surface that accepted consent and then acted would *be* that gate, built here, unspecified and
unrecorded, which is the substitution Blueprint §10 Spine 3 forbids.

Do not partially run. Do not stage, queue, or hold a decision for later. Refusing is this
command's correct behaviour, so the refusal is reported as a refusal, never as a failure and
never as a pass.

## Boundary

Reading `canon/**` is permitted. Changing it is not.

`/gate` must never edit or write a canonical Record, Relationship Record, History Record, WSV,
WSV-H, Registry definition, epoch baseline, or published artifact — and never repair, normalise,
migrate or regenerate any of them. There is no `--fix` here.

It creates no directory, no output area, and no state of its own. It records no decision, mints
no identifier, and persists nothing.

It holds `Auth: none`. Blueprint §7 P-3 — every AI output is provisional until a human gate
confirms it — and this surface is not that gate. Never treat a git commit as approval: version
control records file changes and carries no canonical authority.

## Output

A refusal naming the capability, the reason, and the unlocking phase. Nothing else, and nothing
persisted.

## Stop condition

Stop at the refusal.

```text
/gate → REFUSAL ┊ (proposal → preflight → Authority → commit → changelog)
                ┊
     this command stops here; everything right of the line
     is not reachable from here
```

Do not chain onward into checking, approval, or any write, and do not treat a request to proceed
anyway as permission. The refusal is the whole command until P5 exists.
