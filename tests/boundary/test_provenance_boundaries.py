"""Boundary proofs for the Artifact 047 provenance capture mechanism.

These are the *"what must not happen"* tests. 047's risk is not that capture
fails — it is that provenance quietly becomes universal Record semantics. Each
test below reads the module's own source and fails if a boundary was crossed.

The boundaries are source-stated, not invented here:

- Blueprint §13.7a — provenance **capture** is shared infrastructure; what
  provenance means in a model is not decided by it.
- Blueprint §13.7b / RMS §18 — provenance, audit, history, revision, version
  and derivation are six separated concepts, *"not interchangeable"*.
- RMS §4 — the universal envelope is seven fields, and the nine prohibitions
  forbid a Universal Record Base and a universal semantic schema.
- RMS §6 — provenance **meaning** is one of the nine things a Record Model
  owns.
"""

from __future__ import annotations

import inspect

import pytest

from coolboy12.kernel import provenance as module
from coolboy12.kernel.provenance import (
    PROVENANCE_DIMENSIONS,
    Provenance,
    capture_provenance,
)

SOURCE = inspect.getsource(module)
CODE = "\n".join(
    line for line in SOURCE.splitlines() if not line.lstrip().startswith("#")
)

WHO = "an author"
WHEN = "2026-09-20T12:00:00Z"
WHY = "a recorded reason"


def _executable_body() -> str:
    """The module's code with its docstrings removed.

    Boundary words appear legitimately in prose — the module docstring names
    all six §13.7b concepts precisely in order to disclaim five of them. What
    must be checked is the executable surface, so every string literal is
    stripped before scanning.
    """
    import ast

    tree = ast.parse(SOURCE)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = ""
    return ast.unparse(tree)


BODY = _executable_body()


@pytest.mark.parametrize(
    "concept",
    ["history", "audit", "revision", "version", "lineage", "derivation"],
)
def test_047_does_not_implement_a_neighbouring_concept(concept):
    """§13.7b separates six concepts; 047 implements exactly one of them."""
    assert f"def {concept}" not in BODY
    assert f"class {concept.capitalize()}" not in BODY


@pytest.mark.parametrize(
    "responsibility",
    [
        "record_history",
        "approve",
        "audit",
        "version",
        "derive",
        "resolve_cause",
        "supersede",
        "merge",
        "split",
        "retire",
    ],
)
def test_047_exposes_no_foreign_responsibility(responsibility):
    """A minimal interface: capture, render, rebuild. Nothing else."""
    assert not hasattr(module, responsibility)


def test_047_does_not_branch_on_a_partition():
    """No ``if partition == "W"`` anywhere, even accidentally.

    The mechanism is never told which model it serves, so it cannot define
    provenance meaning per model (RMS §6, Artifact 048).
    """
    for code in ("W", "E", "P", "R", "V", "I"):
        assert f'== "{code}"' not in BODY
        assert f"== '{code}'" not in BODY
    assert "partition" not in BODY


def test_047_names_no_record_model():
    """No Record Model is referenced by the executable surface."""
    for model in ("World", "Epistemic", "Production", "Registry", "Visual", "Issue"):
        assert model not in BODY


def test_047_introduces_no_universal_temporal_axis():
    """P-21's axes are not universalised into the capture mechanism."""
    for axis in ("world_time", "worldtime", "issue_ordinal", "session"):
        assert axis not in BODY


def test_047_decides_no_approval():
    """Approval belongs to the mutation/ceremony machinery, not to capture."""
    for token in (
        "approval",
        "approved",
        "approver",
        "gate_result",
        "human_gate",
        "severity",
        "ceremony",
    ):
        assert token not in BODY


def test_047_never_reads_the_clock():
    """No instant is silently invented; the caller states ``when``.

    ``datetime`` itself is permitted and used — it decides whether a supplied
    value is a real instant (I-86 draws the line at *generating* a timestamp,
    not at validating one). What must not appear is any call that produces the
    current time.
    """
    for token in ("time.time", "utcnow", ".now(", "date.today", "timestamp()"):
        assert token not in BODY


def test_047_capture_signature_has_no_optional_when():
    """There is no ``when=None`` default that a clock could fill in."""
    signature = inspect.signature(capture_provenance)
    for name, parameter in signature.parameters.items():
        assert parameter.default is inspect.Parameter.empty, (
            f"{name} acquired a default, which is how a clock gets in"
        )


def test_047_touches_no_storage_and_no_canon():
    """Capture is a value operation: no file, no network, no canon."""
    for token in ("open(", "Path(", "canon/", "requests", "urllib", "sqlite"):
        assert token not in BODY


def test_047_introduces_no_universal_base_or_global_state():
    """No Universal Record Base (RMS §4), no singleton, no mutable global."""
    assert "global " not in BODY
    assert "class Record" not in BODY
    assert "UniversalRecord" not in SOURCE
    # The only class defining state is the frozen value type itself.
    assert "@dataclass(frozen=True, slots=True)" in SOURCE


def test_the_envelope_remains_seven_fields():
    """047 carries the value of one existing field; it adds no eighth.

    RMS §4 `FROZEN`: partition · kind · object_id · slug · provenance ·
    registry_ref · sot_class.
    """
    captured = capture_provenance(who=WHO, when=WHEN, why=WHY)
    assert [f for f in Provenance.__dataclass_fields__] == list(PROVENANCE_DIMENSIONS)
    assert not hasattr(captured, "partition")
    assert not hasattr(captured, "registry_ref")
    assert not hasattr(captured, "sot_class")


def test_capture_imports_no_later_artifact():
    """047's only declared dependency is 033, which is a document.

    It must not reach forward into 048, the mutation coordinator, or any
    model package.
    """
    for forbidden in ("provenance_meaning", "mutation", "models.", "coordinator"):
        assert forbidden not in BODY
