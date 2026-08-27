# /brief

**This command refuses.** The Return Briefing capability is not available, so `/brief` says so
and stops. Roadmap row 028 fixes all four of these surfaces the same way — *Val: each refuses
with a reason and the unlocking phase · Done: four refusals present · Why: RULE G3 — one
responsibility, "refuse until licensed", four files.*

The entry point exists now so it is present and honest. It is not here so that a briefing can be
given today.

## Role

The invocation surface for the Return Briefing — reconstructing where the author left off after a
dormancy.

`/brief` does not define what a briefing is. **Artifact 456**
(`src/coolboy12/operations/return_briefing.py`, P17) is the Return Briefing, and its validation
fixes both what it draws on and what it may not do: it *reconstructs where the author left off
from Creative Memory + Context Builder + canon — **never from a stored summary treated as
truth**.* The Return Briefing capability is not yet available, so this surface refuses; a
reconstruction source arriving on its own does not make the command runnable.

Blueprint §7 P-11: the system is resumable after a dormancy of up to three years — *"Dormancy is
expected, not failure."*

## Input

Nothing yet, because the capability that would consume an input is not available.

When the capability exists, the input is the dormancy to return from; the briefing is
reconstructed rather than retrieved. An absent or ambiguous target will be reported as
unresolved — never resolved to *the last session* or *everything since the beginning*.

## Behavior

Refuse, and say why.

1. State that the Return Briefing capability is not available.
2. Give the reason: **the Return Briefing capability is not yet available.** Artifact 456
   reconstructs from Creative Memory (Artifact 433), the Context Builder (437) and canon. The
   reason is that unavailability, not the contents of `canon/**` — a populated canon, and the
   reconstruction sources alongside it, would still leave nothing that reconstructs a briefing
   from them.
3. Name what would unlock it: **Phase P17 — SURFACES · ORCHESTRATION · DORMANCY ·
   EXTENSIBILITY (artifacts 440–462)**.
4. Stop.

**Do not write a summary and call it a briefing.** This is the specific failure Artifact 456's
validation names — a stored summary treated as truth — and it is available at any moment, because
a plausible account of recent work can always be assembled from session history or commit
messages. Such an account would be a description of the repository, not a reconstruction of the
author's position, and presenting it as a briefing would establish exactly the substitute source
456 exists to forbid.

Do not partially run. Refusing is this command's correct behaviour, so the refusal is reported as
a refusal, never as a failure and never as a pass.

## Boundary

Reading `canon/**` is permitted; a briefing reconstructs *from* canon. Changing it is not.

`/brief` must never edit or write a canonical Record, Relationship Record, History Record, WSV,
WSV-H, Registry definition, epoch baseline, or published artifact — and never repair, normalise,
migrate or regenerate any of them. There is no `--fix` here.

It creates no directory, no output area, and no state of its own. It stores no briefing, mints no
identifier, and persists nothing — a briefing that were stored and re-served would become the
stored summary its own specification rules out.

It holds `Auth: none`. A briefing describes where work stands and decides nothing about what may
proceed. Never treat a git commit as approval: version control records file changes and carries
no canonical authority.

## Output

A refusal naming the capability, the reason, and the unlocking phase. Nothing else, and nothing
persisted.

## Stop condition

Stop at the refusal.

```text
/brief → REFUSAL ┊ (Creative Memory + Context Builder + canon → reconstruction → briefing)
                 ┊
      this command stops here; everything right of the line
      is not reachable from here
```

Do not chain onward into checking, approval, or any write, and do not treat a request to proceed
anyway as permission. The refusal is the whole command until P17 exists.
