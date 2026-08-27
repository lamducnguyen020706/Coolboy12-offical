# /rebuild

**This command refuses.** There is no derived layer to rebuild yet, so `/rebuild` states that
plainly and stops. Roadmap row 027 fixes it as a stub — *Val: refuses until the derived layer
exists · Done: stub refuses cleanly · Why: honest refusal beats a broken command.*

The command exists now so the entry point is present and honest, not so that something can be
rebuilt today.

## Role

The invocation surface for the rebuild capability, held open and closed.

`/rebuild` does not define what rebuilding means. **Artifact 020**
(`docs/conventions/rebuild.md`, `SoT: AUTHORITATIVE`, `Auth: governing`) is the rebuild contract:
every DERIVED artifact declares its authoritative sources and its own rebuild method, and the
method is *"stated as a capability, not as a command."* This surface would invoke declared
methods; it never authors one.

Blueprint §29.8 states the drill those methods serve — *"Delete every derived store … and rebuild
them from canonical records alone. If the rebuild does not complete, the deleted store was not
derived."*

## Input

Nothing yet, because nothing is rebuildable yet.

When the capability exists, the input is a rebuild target: a derived artifact or store that has
declared a rebuild method. An unresolved or absent target will not be treated as *rebuild
everything* — it will be reported as unresolved. Do not accept a command to run in place of a
target; this surface invokes declared methods, not supplied ones.

## Behavior

Refuse, and say why.

1. State that the rebuild capability is not available.
2. Give the reason: **the repository holds no derived data.** Artifact 020 records the same
   condition — *"none exists to delete — the repository holds no derived data at P0."*
3. Name what would unlock it: derived artifacts that exist and declare their rebuild methods per
   Artifact 020's obligation. The drill's specification is Artifact 173 and its implementation is
   Artifact 227; neither is built.
4. Stop.

Do not partially run. Do not simulate a rebuild. Do not report a rebuild that did not happen, and
do not report success for a no-op — a missing capability is not a clean result. Refusing is this
command's correct behaviour, so the refusal is reported as a refusal, never as a failure and
never as a pass.

## Boundary

Reading `canon/**` is permitted; a rebuild derives *from* canonical records. Changing it is not.

`/rebuild` must never edit or write a canonical Record, Relationship Record, History Record, WSV,
WSV-H, Registry definition, epoch baseline, or published artifact — and must never repair,
normalise, migrate or regenerate any of them. There is no `--fix` here. **A rebuild reconstructs
derived state from source truth; it never rewrites source truth to make a rebuild succeed.** That
inversion is precisely the misfiling §29.8 exists to catch: when a rebuild fails although its
declared source is available, that is an architectural finding, not something to correct by
editing canon.

Nor does it write anywhere else today. When the capability exists it would write only the derived
destinations those artifacts declare; this stub creates no directory, no output area, and no
rebuild state of its own.

It holds `Auth: none`. A rebuild is not approval, not a gate, and not a commit — a completed
rebuild would say nothing about whether any canonical change may proceed, and this command never
enters that path. Never treat a git commit as approval.

## Output

A refusal naming the capability, the reason, and the unlocking condition. Nothing else, and
nothing persisted — no rebuild record, no status store, no identifiers.

## Stop condition

Stop at the refusal.

```text
/rebuild → REFUSAL ┊ (derived layer → declared methods → rebuild → result)
                   ┊
        this command stops here; everything right of the line
        is unbuilt, and none of it is reachable from here
```

Do not chain onward into validation, approval, or any write, and do not treat a request to
proceed anyway as permission. The refusal is the whole command until the derived layer exists.
