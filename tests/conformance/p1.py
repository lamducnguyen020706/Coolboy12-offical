"""Artifact 038 — P1 bootstrap conformance suite. The exit-P1 gate.

Roadmap row 038 verbatim:

    **038** · P1 bootstrap conformance suite · `tests/conformance/p1.py` ·
    Own: CONST · RM: n/a · T: test · R: PROOF · SoT: DEV-ENV · Auth: none ·
    Canon: n/a · CD: no · Ph/St: P1/1c · Req: BR-19,BR-20,BR-23 ·
    BP: §13.7,§13.9a · RMS: §§4,5,10.4 · H: 031–037 · S: — · LS: — ·
    G: **exit-P1** · → P2 · Val: envelope is 7 fields; identity parses six
    partitions; meta-contract declared non-Record · Done: green ·
    Why: bootstrap correctness gates the kernel · Risk: low · ∥: no

What this gate proves
---------------------
Exactly the three clauses row 038's ``Val`` states, and nothing else::

    envelope is 7 fields
    identity parses six partitions
    meta-contract declared non-Record

Source establishes all three. They are not derived, extended or supplemented
here, and the gate reads its own clause names back out of the Roadmap so the
mapping below cannot quietly stop describing the row it claims to gate.

What this gate does **not** prove
---------------------------------
It owns none of the rules it checks. Each clause is a *conformance* question —
does the implementation match what the source says? — answered by putting the
source and the implementation side by side::

    033  envelope contract          owns which seven fields
    034  identity grammar           owns the shape of a name
    035  parse · format             owns what a well-formed component is
    036  allocation                 owns which ordinal comes next
    037  structural validation      owns whether a structure is well-formed
    038  exit-P1                    owns only the decision  ← here

So this suite defines no partition set, no envelope schema, no parser and no
allocator. Where it needs to know a rule it asks the artifact that owns it, and
where it needs to know what the rule *should* be it reads the source document.
That is the whole architecture: a gate that restated the rules could pass while
the artifacts beneath it were wrong.

It also proves nothing semantic. Artifact 037 refuses semantic ownership by
design (row 037: *"well-formedness only — nothing semantic"*), and a gate built
on top of it does not acquire what it gates.

Implementation decision: every check here is deterministic, offline and
read-only — it reads repository files and calls pure functions. No clock, no
network, no filesystem writes, no allocator state, no global mutable state.
``H: 031–037`` is a build-order dependency, and this suite reaches only what a
conformance check needs: Artifact 035 and Artifact 037 as code, and the source
documents plus Artifact 031 as text.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

from coolboy12.bootstrap.identity import PARTITIONS, parse_identity
from coolboy12.bootstrap.validate import (
    ENVELOPE_FIELDS,
    validate_envelope,
    validate_identity,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
ROADMAP = REPO_ROOT / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"
BLUEPRINT = REPO_ROOT / "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md"
RMS = REPO_ROOT / "docs/sources/COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md"
META_CONTRACT = REPO_ROOT / "docs/constitution/bootstrap_meta_contract.md"

UNRESOLVED_OWNED_CHECKS: dict[str, str] = {}
"""Checks this suite owns and could not run. A skip is not a proof.

Empty today. Row 038's ``Req: BR-19,BR-20,BR-23`` is not listed here: a row's
``Req:`` is that artifact's own citation rather than a clause it gates, the
requirement register is unavailable (GAP-C), and row 038's ``Val`` — which is
what 038 gates — names three clauses and no requirement. This is the same
correction recorded in the exit-P0 gate.
"""


def _roadmap_row(number: str) -> str:
    """The Roadmap row for an artifact, as written."""
    text = ROADMAP.read_text(encoding="utf-8")
    match = re.search(rf"^\*\*{number}\*\* · .*?$", text, re.MULTILINE)
    assert match, f"Roadmap row {number} not found"
    return match.group(0)


def _val_of(number: str) -> str:
    """The ``Val`` field of a Roadmap row."""
    match = re.search(r"· Val: (.*?) · Done:", _roadmap_row(number))
    assert match, f"Roadmap row {number}: Val field not found, or changed shape"
    return match.group(1)


# ---------------------------------------------------------------------------
# Val clause 1 — envelope is 7 fields
# ---------------------------------------------------------------------------


def test_p1_envelope_is_seven_fields():
    """Row 038 ``Val``: *envelope is 7 fields*.

    Artifact 033 owns the contract and row 033's ``Val`` states it in the
    Roadmap: *"exactly seven fields — `partition`,`kind`,`object_id`,`slug`,
    `provenance`,`registry_ref`,`sot_class`; **`tier` and `status` absent**"*.
    Artifact 037 carries the roster in code.

    The gate puts those two side by side. It does not hold a third copy of the
    list — a copy here could agree with neither and still pass — so the seven
    names are extracted from the Roadmap row and compared with 037's, and the
    behaviour is then exercised through 037 rather than reimplemented.
    """
    val = _val_of("033")

    # Row 033's Val states the roster and the exclusion in two halves, split by
    # a semicolon: the seven fields, then "**`tier` and `status` absent**".
    # Reading the whole field would sweep the excluded names into the roster.
    roster, _, exclusion = val.partition(";")
    stated = re.findall(r"`([a-z_]+)`", roster)

    assert stated, f"row 033's Val no longer states field names: {val!r}"
    assert tuple(stated) == ENVELOPE_FIELDS, (
        f"Artifact 037's envelope roster does not match row 033's Val.\n"
        f"  row 033: {stated}\n  artifact 037: {list(ENVELOPE_FIELDS)}"
    )
    assert len(ENVELOPE_FIELDS) == 7

    # The other half of row 033's Val, and the reason it is CRITICAL.
    assert re.findall(r"`([a-z_]+)`", exclusion) == ["tier", "status"], (
        f"row 033's Val no longer names the excluded fields: {exclusion!r}"
    )
    assert "absent" in exclusion
    assert "tier" not in ENVELOPE_FIELDS
    assert "status" not in ENVELOPE_FIELDS

    # And the contract holds in use, judged by its owner.
    envelope = dict.fromkeys(ENVELOPE_FIELDS, None) | {
        "partition": "W",
        "kind": "CH",
        "object_id": "000001",
        "slug": "Maximus",
    }
    assert validate_envelope(envelope).valid, "the seven-field envelope is refused"

    for absent in ENVELOPE_FIELDS:
        short = {k: v for k, v in envelope.items() if k != absent}
        assert not validate_envelope(short).valid, (
            f"six fields accepted, missing {absent}"
        )

    for eighth in ("tier", "status"):
        assert not validate_envelope(envelope | {eighth: "x"}).valid, (
            f"an eighth field was accepted: {eighth}"
        )


# ---------------------------------------------------------------------------
# Val clause 2 — identity parses six partitions
# ---------------------------------------------------------------------------


def test_p1_identity_parses_six_partitions():
    """Row 038 ``Val``: *identity parses six partitions*.

    Blueprint §13.9a states the enum, and its correction is the reason this
    clause is gated at all: *"the v0.6.3 row still listed four, having never
    been updated when v0.6.1 promoted Registry and Visual to partitions."*
    Artifact 034's ``Why`` names the failure the same way — *"a four-partition
    enum would make R and V unnameable."*

    So the gate reads the six codes out of the Blueprint's own table and
    requires Artifact 035's enum to match, then parses and validates an
    identity in each. Every one must be exercised: a gate that checked one
    representative partition would pass on exactly the defect this clause
    exists to catch.
    """
    row = re.search(
        r"^\| `PARTITION` \| (.*?)$",
        BLUEPRINT.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    assert row, "Blueprint §13.9a partition row not found, or changed shape"
    stated = tuple(re.findall(r"`([A-Z])`", row.group(1)))

    assert len(stated) == 6, (
        f"Blueprint §13.9a no longer states six partitions: {stated}"
    )
    assert stated == PARTITIONS, (
        f"Artifact 035's partition enum does not match Blueprint §13.9a.\n"
        f"  blueprint: {list(stated)}\n  artifact 035: {list(PARTITIONS)}"
    )

    exercised = []
    for partition in PARTITIONS:
        raw = f"{partition}-XX-000001-Example"
        identity = parse_identity(raw)
        assert identity.partition == partition
        assert validate_identity(identity).valid, f"{raw} is not well-formed"
        exercised.append(identity.partition)

    assert tuple(exercised) == PARTITIONS, (
        f"not every partition was exercised: {exercised}"
    )
    assert len(set(exercised)) == 6


# ---------------------------------------------------------------------------
# Val clause 3 — meta-contract declared non-Record
# ---------------------------------------------------------------------------


def test_p1_meta_contract_is_declared_not_a_record():
    """Row 038 ``Val``: *meta-contract declared non-Record*.

    A declaration rather than a behaviour, and gated because it is the one
    bootstrap fact nothing in code can enforce. RMS §10.4 closes it
    ``AUTHOR-DECIDED``: *"**The Bootstrap Meta-Contract is NOT a Record.** It
    is a constitutional bootstrap contract standing outside the ordinary
    Registry Record ontology."* Row 031 carries it as ``Canon: not a Record``,
    and Artifact 031 states it in the repository.

    All three must agree. If the RMS says one thing and the artifact another,
    the bootstrap layer has acquired an ontology it was built to avoid, and the
    gate is where that surfaces.
    """
    assert "Canon: **not a Record**" in _roadmap_row("031"), (
        "row 031 no longer declares the meta-contract a non-Record"
    )

    rms = RMS.read_text(encoding="utf-8")
    assert "**The Bootstrap Meta-Contract is NOT a Record.**" in rms, (
        "RMS §10.4's non-Record ruling is not present as stated"
    )

    assert META_CONTRACT.exists(), f"Artifact 031 is missing: {META_CONTRACT}"
    artifact = META_CONTRACT.read_text(encoding="utf-8")
    assert "not a Record" in artifact, (
        "Artifact 031 does not declare the meta-contract a non-Record"
    )
    assert "Canon: **not a Record**" in artifact, (
        "Artifact 031's metadata no longer carries `Canon: not a Record`"
    )


# ---------------------------------------------------------------------------
# The gate
# ---------------------------------------------------------------------------

VAL_CLAUSES = {
    "envelope is 7 fields": test_p1_envelope_is_seven_fields,
    "identity parses six partitions": test_p1_identity_parses_six_partitions,
    "meta-contract declared non-Record": test_p1_meta_contract_is_declared_not_a_record,
}


def test_exit_p1_gate_covers_its_val_and_carries_no_unresolved_check():
    """The gate itself. ``G: exit-P1`` — and a skip is not a proof.

    Built to the shape Artifact 030 established for exit-P0, for the same
    reasons. The clause names are read back out of row 038's own ``Val``, so
    the mapping cannot drift from the Roadmap; each proof is checked to be this
    module's live definition, so a reference cannot detach from the function it
    names; and each is **called** here, so a failing clause fails exit-P1
    whatever else this file does.

    Running them a second time is deliberate and cheap: every P1 check is
    deterministic, offline and read-only, so a second call is the same call. No
    pytest runs inside pytest and nothing is shelled out — these are plain
    functions, invoked as functions.

    **What is not gated.** Only these three. The other tests in this file
    support them and fail on their own merits; exit-P1 does not silently
    acquire a clause for living in the same module.
    """
    val = _val_of("038")

    undeclared = [clause for clause in VAL_CLAUSES if clause not in val]
    assert not undeclared, (
        f"exit-P1 gates clauses row 038's Val does not state: {undeclared} — "
        f"Val reads: {val!r}"
    )

    # And the converse, which matters more: a clause the Roadmap states must be
    # gated. Checking only the direction above lets a clause be deleted from the
    # mapping while exit-P1 stays green — the gate would then be silent about
    # precisely the condition it was added to enforce.
    stated = {clause.strip() for clause in val.split(";") if clause.strip()}
    ungated = sorted(stated - set(VAL_CLAUSES))
    assert not ungated, (
        f"row 038's Val states clauses exit-P1 does not gate: {ungated} — "
        f"gated: {sorted(VAL_CLAUSES)}"
    )

    live = {
        name: value
        for name, value in globals().items()
        if callable(value) and name.startswith("test_p1_")
    }
    detached = [
        clause
        for clause, proof in VAL_CLAUSES.items()
        if live.get(proof.__name__) is not proof
    ]
    assert not detached, (
        f"a gated clause names a proof this module does not define: {detached}"
    )
    assert len(set(VAL_CLAUSES.values())) == len(VAL_CLAUSES), (
        "two clauses share one proof, so one of them is not independently gated"
    )

    failed = []
    for clause, proof in sorted(VAL_CLAUSES.items()):
        try:
            proof()
        except AssertionError as error:
            failed.append(f"{clause} — {proof.__name__} failed: {error}")

    assert not failed, "\n  ".join(
        ["exit-P1 cannot be GREEN — a Val clause is unproven:"] + failed
    )

    assert not UNRESOLVED_OWNED_CHECKS, "\n  ".join(
        ["exit-P1 cannot be GREEN — checks this suite owns could not run:"]
        + [
            f"{check}: {reason}"
            for check, reason in sorted(UNRESOLVED_OWNED_CHECKS.items())
        ]
    )


# ---------------------------------------------------------------------------
# Supporting conformance checks — not gated, and failing on their own merits
# ---------------------------------------------------------------------------


def test_p1_every_val_clause_is_independently_gated():
    """Break one clause and the gate names that clause, not merely 'something'.

    Substituting a failing proof for each clause in turn proves two things the
    gate would otherwise only assert: that the clause is reached at all, and
    that its failure is attributed to it rather than absorbed into a neighbour.

    The substitute is installed in the module globals as well as in the
    mapping, deliberately. An earlier version of this check replaced only the
    mapping entry, so the gate's own "does this proof detach from its name"
    assertion fired first and the test passed without the broken proof ever
    being called — green for the wrong reason, and blind to a gate that had
    stopped executing its clauses at all.
    """
    original_clauses = dict(VAL_CLAUSES)
    original_globals = {
        proof.__name__: globals()[proof.__name__] for proof in original_clauses.values()
    }

    try:
        for clause, proof in original_clauses.items():
            name = proof.__name__

            def broken():
                raise AssertionError("deliberately broken for this check")

            broken.__name__ = name
            VAL_CLAUSES[clause] = broken
            globals()[name] = broken
            try:
                test_exit_p1_gate_covers_its_val_and_carries_no_unresolved_check()
            except AssertionError as error:
                assert "a Val clause is unproven" in str(error), (
                    f"the gate failed for the wrong reason on {clause}: {error}"
                )
                assert clause in str(error), f"the gate did not name {clause}"
            else:
                raise AssertionError(f"the gate stayed green with {clause} broken")
            VAL_CLAUSES[clause] = proof
            globals()[name] = proof
    finally:
        VAL_CLAUSES.clear()
        VAL_CLAUSES.update(original_clauses)
        globals().update(original_globals)


def test_p1_bootstrap_artifacts_exist_where_the_roadmap_places_them():
    """``H: 031–037``. A gate over artifacts that are absent proves nothing."""
    missing = []
    for number in ("031", "032", "033", "034", "035", "036", "037"):
        path = re.search(r"· `([^`]+)` ·", _roadmap_row(number))
        assert path, f"row {number}: path field not found"
        if not (REPO_ROOT / path.group(1)).exists():
            missing.append(f"{number}: {path.group(1)}")

    assert not missing, f"hard dependencies of row 038 are absent: {missing}"


def _module_tree() -> ast.Module:
    """This file, parsed. Prose is not code, and only code can do anything."""
    return ast.parse(Path(__file__).read_text(encoding="utf-8"))


def _referenced_names() -> set[str]:
    """Every name and attribute this file actually references."""
    tree = _module_tree()
    return {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} | {
        n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)
    }


def test_p1_the_gate_owns_no_rule_it_checks():
    """Composition, not duplication — the architectural claim, made checkable.

    This suite must hold no partition set, no envelope roster and no grammar of
    its own. Every such value is imported from the artifact that owns it or
    read from a source document, so a rule here cannot be satisfied by a third
    copy that agrees with neither.

    Checked against the parse tree rather than the text: the docstrings above
    name the rules in order to say who owns them, and a substring search finds
    that prose rather than any behaviour.
    """
    import coolboy12.bootstrap.identity as identity_module
    import coolboy12.bootstrap.validate as validate_module

    tree = _module_tree()
    assigned = {
        target.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    assert "PARTITIONS" not in assigned, "the gate defines its own partition set"
    assert "ENVELOPE_FIELDS" not in assigned, "the gate defines its own envelope roster"

    defined = {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    assert not [
        name
        for name in defined
        if name.startswith(("parse_", "format_", "validate_", "allocate"))
    ], "the gate is reimplementing a rule it should be delegating"

    # The values it uses are the artifacts' own objects, not lookalikes.
    assert PARTITIONS is identity_module.PARTITIONS
    assert ENVELOPE_FIELDS is validate_module.ENVELOPE_FIELDS


def test_p1_the_gate_reaches_no_allocator_and_no_semantics():
    """037 refuses semantic ownership; a gate on top of it acquires none.

    Artifact 036 is not a dependency of row 038 at all — ``S: —`` — and
    allocation history has no bearing on whether the bootstrap foundation is
    conformant. An unallocated, unregistered but well-formed identity passes,
    which is the behavioural half of the same boundary.
    """
    tree = _module_tree()
    imported = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    } | {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }

    assert {name for name in imported if name.startswith("coolboy12")} == {
        "coolboy12.bootstrap.identity",
        "coolboy12.bootstrap.validate",
    }, f"the gate imports past its scope: {sorted(imported)}"

    referenced = _referenced_names()
    assert not [
        name
        for name in referenced
        if any(word in name.lower() for word in ("ordinal", "allocat", "frontier"))
    ], "the gate reaches the allocator"

    envelope = dict.fromkeys(ENVELOPE_FIELDS, None) | {
        "partition": "R",
        "kind": "ZZ",
        "object_id": "654321",
        "slug": "Never_Allocated_And_Not_Registered",
    }
    assert validate_envelope(envelope).valid


def test_p1_the_gate_is_deterministic():
    """The same repository, the same verdict — every time.

    Repeating the gate is the check: every P1 clause is offline and read-only,
    so a second run that disagreed with the first would mean the gate depends
    on something outside the repository. The snapshot comparison is the other
    half — the gate must leave its own mapping exactly as it found it, or a run
    could be influenced by the run before it.
    """
    before = {clause: proof for clause, proof in VAL_CLAUSES.items()}

    for _ in range(5):
        test_exit_p1_gate_covers_its_val_and_carries_no_unresolved_check()

    assert VAL_CLAUSES == before, (
        "the gate mutated its own clause mapping, so runs are not independent"
    )

    # Anchored to the Roadmap rather than to a snapshot taken here. A snapshot
    # only catches a mapping that changes *during* this test, and the gate has
    # already run several times by then — a reordering that had settled before
    # the snapshot would be invisible to it. Row 038's Val cannot settle.
    stated = [clause.strip() for clause in _val_of("038").split(";") if clause.strip()]
    assert list(VAL_CLAUSES) == stated, (
        f"the gate's clause order no longer follows row 038's Val.\n"
        f"  row 038: {stated}\n  gate: {list(VAL_CLAUSES)}"
    )
