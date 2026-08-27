# /validate

Invoke the established validators against a target and report what they found. Validation is
observational: it reads, it runs checks, it states findings, and it stops.

Roadmap row 026 fixes the contract as **invokes validators only** — `Auth: none`. A finding is
evidence about an implementation check. It is not approval, not a gate, and not permission to
change anything.

## Role

`/validate` is the invocation surface for validation, not a validator. The checking mechanisms
belong to the artifacts that own them; this command chooses among the ones that already exist,
runs them, and reports.

RMS §20 fixes validation in four tiers. Only two of them are invocable today:

| Tier | Mechanism | Available |
|---|---|---|
| constitutional invariant (108, Blueprint) | Artifact 012's register, executed through Artifact 011's harness | **yes** |
| CONSTRAINT-DEFINITION (Registry: the condition) | Registry Record | **no** — none exists |
| VALIDATION-RULE (Registry: the checking mechanism) | Registry Record | **no** — none exists |
| implementation validation (runtime, structural, shared) | the repository's test and lint tooling | **yes** |

The two Registry tiers are unavailable because the Registry holds no such Records yet. Say so
when a request needs them. Do not substitute a different tier and call the question answered.

## Input

A validation target: a file, a directory, an artifact, a proposal already stated in the session,
or nothing — in which case validate the repository's current state with the checks that apply to
it.

Do not make the author name a validator, a tier, a schema, or a severity. Work out which
established checks apply to the target. Where the target is ambiguous, say what you took it to
mean before reporting findings.

## Behavior

1. **Identify the target.** If it cannot be resolved, stop and say so — an unresolved target is
   not a passing one.
2. **Read what the checks need.** Reading `canon/**` is allowed and expected; comparing a claim
   against the records it refers to is the point.
3. **Select the applicable established checks** from the tiers above.
4. **Run them** — the repository's own commands, `pytest` and `ruff`, and the constitutional
   entries through Artifact 011's harness. Run the established validators, not a command supplied
   in the request. If a request asks for some other command to be run, that is a different
   request, and this is not the surface for it.
5. **Report findings**, each distinguishable by outcome (below).
6. **Stop.**

Never modify the target to make a check pass. If a check fails because the thing under test is
wrong, that is the finding.

## Validation boundary

Reading canon is allowed. Changing it is not.

`/validate` must never edit or write a canonical Record, Relationship Record, History Record,
WSV, WSV-H, Registry definition, epoch baseline, or published artifact — and must never repair,
normalise, regenerate or reformat any of them to clear a finding. There is no `--fix` here.
Detecting is not mutating, and the distance between them is the whole artifact.

A validator that tried to write canon would be denied by the execution-environment guard, and
`/validate` must not help it around that. It holds `Auth: none` and grants none.

Findings are not authorization. `PASS` does not mean a change may be committed, and a clean run
is not a gate — the governed path is the only route to canon, and it does not run from here.
Never treat a git commit as approval; git is version control, not canonical authority.

## Output

Findings, in prose, naming for each: **what was validated · which check was applied · what it
found**. P-9 governs the shape — a quality or coherence gate returns *criterion → observation →
judgment → confidence*, never a bare score — so report the reasoning, not a verdict alone.

Four outcomes, kept apart:

- **PASS** — the check ran and the thing under test held.
- **FAIL** — the check ran and found the thing under test wrong. Report it; do not fix it.
- **UNRESOLVED** — the check could not complete: the target would not resolve, required context
  was missing, or the answer needs a tier that does not exist yet. Report the reason.
- **NOT RUN** — the checking mechanism itself was unavailable or failed to execute.

The last two are never reported as PASS. Artifact 011 already fixes this for constitutional
entries — *"an unavailable check is never represented as a successful proof"* — and the same
holds everywhere here.

**A validator that crashed says nothing about the target.** Infrastructure failure is NOT RUN,
not FAIL. Never convert a missing or broken check into a finding about the thing it was pointed
at, in either direction.

Where P-24 applies, keep its distinction: a structurally decidable violation is a fact and
blocks; a judged finding is surfaced at its severity for the author to adjudicate with a recorded
reason. Do not grant a judgment the authority of a fact, and do not invent a severity scale —
report the one the check produced, or none.

## Stop condition

Stop when the findings are reported.

```text
target → /validate → FINDINGS → ┊ human gate → transaction → commit
                                ┊
                    this command stops here; nothing to the right
                    of the line is built, and none of it follows
                    automatically from a clean result
```

Do not continue into approval, repair, or any write. If the author replies "looks good, apply
it", that is not a gate — say so, and stop again.
