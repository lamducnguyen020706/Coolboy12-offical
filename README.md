# COOLBOY12

**A Single-Author Universe Operating System.**

COOLBOY12 is the operating system a single author uses to build, simulate, govern, and
manifest one living fictional universe across many media and many years — keeping the
universe coherent while it becomes richer, deeper in time, and truer to its own causality.

The author expresses *what* they want. The system composes the work, advances the world
through time, and surfaces the story material that movement produced. Nothing becomes true
without the author's word.

---

## What is COOLBOY12?

It is designed for **one creator**, a staff of AI reasoning roles, and a **multi-decade**
universe. Its core is not a content pipeline but a world: canon-governed, causally
simulated, and able to separate cleanly what is *true* from what is *known*, and by whom.

The number of manifestations — magazines, games, films, forms not yet invented — can grow
without limit while the number of *truths* stays exactly one.

Two properties follow, and they explain most of the architecture:

- **One canon, one path, one authority.** There is exactly one canonical truth about the
  universe. It changes only through *propose → check → human gate → commit → changelog →
  log*, and only a human commits it. No AI output, simulation result, or deadline is
  canonical until it passes that gate.
- **Published work never becomes truth.** A published artifact references canon in one
  direction only. *That* the magazine printed something is a fact of the world; *whether*
  it is true is a separate, canon-governed question.

---

## The Record System

The **Record System** is the governing architecture of COOLBOY12.

A **Record** is a persistent, identity-bearing unit owned by exactly one Record Model. It
has independent identity, its own lifecycle, and a defined authority. Records are the
architectural unit of the system: what the system holds, it holds as Records.

Beneath the models sits a **thin universal mechanism layer** — identity, addressing,
parsing, resolution, structural validation, serialization, provenance capture, reference
resolution, and the single governed write path. Above it sit six sovereign Record Models,
each owning its own meaning.

The rule that separates those two layers is the one to carry away first:

> **A mechanism may be shared; a semantic may not be shared without evidence in each model
> that carries it.**

So all six models share one identity grammar — and share nothing about what the named thing
*means*. A universal identity grammar is not a universal semantic model. Each model owns its
own Kinds, its own lifecycle, its own temporal mechanism, its own relationship
representation, and its own state vocabulary. These are deliberately **not** the same across
models, and the architecture does not permit them to be quietly unified.

One more distinction does a great deal of work: **a Record is not automatically canon.**
Authority is domain-scoped. A Production Record is authoritative about production and about
nothing else; an Issue Record is authoritative about what was published and about nothing
else. Only World confers World Truth, and only at the human gate.

---

## The Six Record Models

There are exactly six. No model is a superclass of another, and nothing inherits from World.

| Code | Model | The question it alone answers |
|---|---|---|
| **W** | World | What is true of the world? |
| **E** | Epistemic | Who knows, believes, suspects, or has been shown what? |
| **P** | Production | What is intended, planned, coordinated, and in production? |
| **R** | Registry | What does the system mean, and how are Record semantics defined? |
| **V** | Visual | How is World Truth visually specified and represented? |
| **I** | Issue | What was published, and how is that publication composed? |

### W — World
Holds what is true. World Truth is conferred at the human gate. World is **manifestation-
blind**: no World field may reference an issue, a medium, a published artifact, or the real
world. It is the most mature model, and later work conforms to it rather than redesigning it.

### E — Epistemic
Holds every *frame* upon a world-fact — what the author knows, what the world knows, what a
character knows, what the reader knows. World holds the fact; Epistemic holds every view of
it, which may be partial or simply wrong. E is authoritative over epistemic state and
**never over truth**.

### P — Production
Holds intent, plan, coordination, and production reality — arcs, schedules, debt, personas,
workflows, art direction. The defining sentence: *an arc is a plan for telling, not a fact of
the universe; the events it plans to tell are canon, the plan is not.* Production State is
authored and durable, changes at production ceremony rather than at the human gate, and
**never becomes World Canon by any route**.

### R — Registry
Holds meaning as Records — model, Kind, field, schema, vocabulary, constraint, validation and
capability *definitions*. Registry is a sovereign Record Model, not configuration and not
runtime. It may reference other Registry definitions, declared models, Kinds and schemas; it
may **never own or depend on domain instances** of the other models, and it can never override
World Truth. It defines schemas; it does not execute them.

### V — Visual
Holds visual specification and representation of World Truth. The decisive rule: **canonical
visual identity is the description, not the file.** If a character's canonical appearance were
a generated image, replacing the image generator would change canon. So the structured
description carries canonical visual truth and an image file never does. Visual never mutates
World; an observation that makes a claim about the world becomes Epistemic evidence first.

### I — Issue
Holds what was published and how that publication is composed. Issue is durable publication
reality. It **references but never owns** World, Epistemic, Production or Visual semantics,
and it never becomes World Canon. Correction is not an edit — it is a new Issue that
supersedes the previous one.

---

## How the System Fits Together

```
COOLBOY12
   ↓
Record System                       constitution + thin universal mechanism layer
   ↓
Six Record Models                   W · E · P · R · V · I
   ↓
model-owned Records                 each model owns its own Kinds and semantics
   ↓
governed interactions               cross-model references; one gated write path
   ↓
authoritative state                 world · epistemic · production · registry ·
                                    visual · issue — each authoritative in its own
                                    domain and in no other
```

The ownership boundaries this is meant to fix in a new reader's head:

- **W** owns World Truth.
- **E** owns epistemic state and knowledge and reveal structures — not truth itself.
- **P** owns production reality — not World Canon.
- **R** owns semantic definitions and Record semantics — not domain instances.
- **V** owns visual specification and representation — not World Truth generally.
- **I** owns publication composition and publication reality.

---

## The Creative Flywheel

Everything exists to serve one loop. The architecture is organized around it.

```
AUTHOR       makes decisions and states intent
   ↓
UNIVERSE     changes — canon updates, gated
   ↓
SIMULATION   advances the world through time
   ↓
EMERGENCE    surfaces story material
   ↓
CANON        updates transactionally
   ↓
EDITORIAL    decides what to tell, in what form, and when
   ↓
ARTIFACTS    are produced — issue, cover, and other manifestations
   ↓
READERS      experience the universe; knowledge-state advances
   ↓
AUTHOR       learns, and decides again
```

The loop runs as **two currents**, and which current a thing sits on determines what it is
allowed to do:

- **Descending current** — *intent → proposal → check → gate → commit → propagate.* Moves
  toward canon. **Fails closed.** Transactional. Everything is provisional until the gate.
- **Ascending current** — *canon → emergence → editorial → studio → artifact → reader.*
  Moves away from canon toward experience. **Fails open**: if an input is missing, work
  continues in a reduced mode and says so. It **reads canon and never writes it** — the
  prohibition is structural, not a policy.

Most creative work lives in the ascending current and never touches canon. That is why
publication is a projection that writes nothing, and why what readers know returns to the
system as a gated proposal on the descending current rather than as an inferred write. A
reader signal is never, by itself, a truth.

---

## Status

The architecture is specified; the system is being built. This repository is at the start of
its build — the foundation phase. Directories exist for work that has not been authored yet.
Each directory carries a `PURPOSE.md` stating what belongs in it and what does not, so an
empty directory is still a declared responsibility rather than a guess.

---

## Where to Read Next

Read in this order. Each layer assumes the one above it.

1. **Constitutional and governing material** — the Record System constitution, the boundaries
   the system may never cross, and the build conventions.
   See [`docs/constitution/`](docs/constitution/PURPOSE.md),
   [`docs/boundaries/`](docs/boundaries/PURPOSE.md) and
   [`docs/conventions/`](docs/conventions/PURPOSE.md).
2. **Model architecture** — one directory per Record Model.
   [`world`](docs/models/world/PURPOSE.md) ·
   [`epistemic`](docs/models/epistemic/PURPOSE.md) ·
   [`production`](docs/models/production/PURPOSE.md) ·
   [`registry`](docs/models/registry/PURPOSE.md) ·
   [`visual`](docs/models/visual/PURPOSE.md) ·
   [`issue`](docs/models/issue/PURPOSE.md).
3. **Authoritative state** — [`canon/`](canon/PURPOSE.md) holds the Records of the six models
   and is written only through the governed path. [`derived/`](derived/PURPOSE.md) holds
   rebuildable output and can be deleted in its entirety and rebuilt from canon.
4. **Implementation** — [`src/coolboy12/`](src/coolboy12/PURPOSE.md), layered in the order the
   architecture is built.
5. **Validation** — [`tests/`](tests/PURPOSE.md), including the constitutional invariant
   register and the negative tests that prove prohibited actions are refused.

The Master Blueprint and the Record Model System are the authorities behind everything above.
Where this README and those documents differ, they are right and this file is wrong: this is
an orientation layer, not a specification.
