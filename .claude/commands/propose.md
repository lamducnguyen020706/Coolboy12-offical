# /propose

Formulate a **proposal** from the author's intent. A proposal is provisional. This command is
the entry to the mutation path and never travels it.

Blueprint §12.6 fixes one route for canon:

```text
PROPOSE  →  CHECK  →  HUMAN GATE  →  TRANSACTION (propagate · commit · changelog · log)
   ▲
   └── this command ends here
```

*"No simulation tick, no publication, and no report may write canon by any other means."*
Artifact 025 is the command-level entry into **PROPOSE** and nothing beyond it.

## Role

The author is asking the system to *work out what a change would be*. They are not authorizing
it. Producing a proposal is not approving one, and the two are never collapsed.

## Input

Plain-language intent, in the author's own words:

- `/propose Add a character who leads the eastern rebellion.`
- `/propose Change the capital's trade policy after the famine.`
- `/propose Move the publication deadline for Issue 12.`

Do not make the author name a domain, capability, coworker, validator, record type, severity, or
transaction. Intent in; the system composes. Asking the author to choose capabilities is a
failure of P-13 (§23.3). This command states an intent — it does not orchestrate; the Workflow
Composer (§23) remains the primitive that does.

## Behavior

Interpret the intent, resolve what it refers to, and set out the change it implies:

- **What is proposed** — the change, concretely enough to be checked later.
- **Why** — the author's intent, preserved rather than paraphrased away.
- **What it touches** — records, relationships and areas the change would reach, named as
  references. Reading canon is allowed; changing it is not.
- **What was assumed** — anything filled in that the intent did not settle.
- **What is unresolved** — questions a later stage or the author must answer.
- **The strongest counter-case**, when there is a real one. Do not manufacture opposition.

Offer alternatives **only when the intent admits materially different choices**, and then leave
the choice open. Do not invent alternatives for a request that has one obvious reading, and do
not silently pick for the author.

## Constraint

The proposal is provisional and stays that way.

- Never change a canonical Record, Relationship Record, History Record, WSV, WSV-H, Registry
  definition, epoch baseline, or published artifact. §26.8 is explicit that the environment
  proposes canon mutations and may never directly change them.
- Never treat a git commit as approval. Git is version control, not canonical authority.
- Never state that CHECK, the Human Gate, or a commit has happened. None of them is built.
- Never assign a severity class. Severity is CHECK's finding (§12.6), not this surface's.

This command holds `Auth: none`. It cannot approve, gate, canonicalize, or commit. The human
remains the sole authority for canonical commit (Spine law 3).

## Output

The proposal, presented in the session as ordinary prose.

There is no proposal staging area in this repository yet. §26.8 anticipates one — *"AI-assisted
work drafts into a proposal area"* — but none exists, and this artifact does not invent the
directory, the schema, or the file format for it. The proposal record itself is Artifact 146's
to define. When those exist, this surface can direct output to them; until then it does not
pretend to.

**Basis state, honestly.** P-22 requires a proposal to carry the canon revision, epoch and
objects read that it was computed against, and re-validation at the gate if canon has moved.
None of that machinery exists yet. Name the canonical references the proposal actually read so
the reasoning is legible, and do not fabricate a basis stamp or claim P-22 is enforced.

## Stop condition

Stop when the proposal is stated.

```text
IDEA → PROPOSAL → ┊ CHECK → HUMAN GATE → APPROVED → CANON
                  ┊
          this command stops here; everything right of the line
          belongs to artifacts that do not exist yet
```

Do not continue into checking, approval, or any write. If the author replies "yes, do it", that
is not a Human Gate — say so, and stop again. The governed path is the only route, and it is not
built past this point.
