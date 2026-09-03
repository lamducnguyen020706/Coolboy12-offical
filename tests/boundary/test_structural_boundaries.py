"""Boundary proofs for Artifact 037 — what the validator refuses to ask.

Row 037's ``Done`` is not *omits* semantic checks but **refuses** them, and its
``Why`` says why that distinction matters: *"scope creep here creates a
universal semantic owner."* A refusal that is only described in a docstring is
a claim; this suite makes it a property::

    033  envelope contract       ← the seven fields, read not restated
    034  grammar, frozen         ← not restated here
    035  parse · format          ← the only parser; 037 delegates to it
    036  allocate · never reuse  ← never consulted
    037  well-formedness only    ← this module
    038  exit-P1 gate            ← consumes this

Each boundary is proved behaviourally where it can be and statically against
the module's own source where it cannot. The static checks are not a lint pass;
they name the specific things Artifact 037 must not contain.
"""

from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from coolboy12.bootstrap import identity as identity_module
from coolboy12.bootstrap import validate as validate_module
from coolboy12.bootstrap.identity import MAX_ORDINAL, Identity, parse_identity
from coolboy12.bootstrap.validate import (
    ENVELOPE_FIELDS,
    ValidationCode,
    validate_envelope,
    validate_identity,
)

SOURCE = Path(inspect.getsourcefile(validate_module)).read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)


def _code_literals() -> set[str]:
    """Every string literal in the module except its docstrings.

    The docstrings quote the sources that establish the boundaries — including
    the words the code must not act on — so a raw substring search over the
    file finds them in prose written to keep them out. Only a literal the code
    uses can do anything.
    """
    docstrings = set()
    for node in ast.walk(TREE):
        if isinstance(
            node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            first = node.body[0] if node.body else None
            if (
                isinstance(first, ast.Expr)
                and isinstance(first.value, ast.Constant)
                and isinstance(first.value.value, str)
            ):
                docstrings.add(id(first.value))

    return {
        node.value
        for node in ast.walk(TREE)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and id(node) not in docstrings
    }


def envelope(**overrides):
    base = {
        "partition": "W",
        "kind": "CH",
        "object_id": "000001",
        "slug": "Maximus",
        "provenance": None,
        "registry_ref": None,
        "sot_class": None,
    }
    base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# 035 — one parser, and it is not this one
# ---------------------------------------------------------------------------


def test_the_validator_does_not_parse_raw_strings():
    """A raw identity is Artifact 035's input, never this module's."""
    assert not validate_identity("W-CH-000001-Maximus").valid
    assert not [n for n in dir(validate_module) if n.startswith("parse")]
    assert "def parse" not in SOURCE


def test_the_validator_restates_no_grammar_rule():
    """No second copy of the frozen rules, which is what could drift.

    The partition set, the kind width, the object-identity width and the slug
    character set all live in Artifact 035. If any were restated here, one of
    these would appear as data in this module.
    """
    literals = _code_literals()

    assert not [t for t in literals if len(t) == 1 and t in "WEPRVI"]
    assert not [t for t in literals if len(t) == 2 and t.isascii() and t.isupper()]
    assert not [t for t in literals if "999999" in t or "000000" in t]
    assert not [
        n
        for n in ast.walk(TREE)
        if isinstance(n, ast.Constant) and n.value in (MAX_ORDINAL, 6)
    ]
    for token in ("A-Za-z", "re.compile", "isupper", "isalpha", "zfill"):
        assert token not in SOURCE, f"{token} restates a rule 035 owns"


def test_the_validator_delegates_by_constructing_through_035():
    """The delegation is real: 035's own error code comes back in the finding."""
    finding = validate_envelope(envelope(kind="ch")).findings[0]

    assert finding.origin == "INVALID_KIND"

    called = {
        node.func.id
        for node in ast.walk(TREE)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert "Identity" in called


def test_the_validator_does_not_format():
    assert not [n for n in dir(validate_module) if n.startswith("format")]
    assert "format_identity" not in SOURCE
    assert "format_object_id" not in SOURCE


# ---------------------------------------------------------------------------
# 036 — allocation is never consulted
# ---------------------------------------------------------------------------


def test_an_unallocated_ordinal_is_still_well_formed():
    """Whether ``000123`` was ever allocated is Artifact 036's question.

    A structurally valid identity does not become invalid because no allocator
    has issued it — nothing here has an allocation record to consult, and there
    is no allocator in this test at all.
    """
    assert validate_envelope(envelope(object_id="000123")).valid
    assert validate_envelope(envelope(object_id="999999")).valid
    assert validate_identity(parse_identity("W-CH-654321-Example")).valid


def test_the_module_takes_no_forbidden_dependency():
    """Static half of the architectural boundary.

    This names the dependencies Artifact 037 must not acquire, rather than
    freezing the ones it happens to have. An exact import list would fail the
    next time a harmless standard-library import is added, which protects
    nothing and teaches the next reader to loosen the test.

    The project dependency is the one that matters: 035 and nothing else.
    Row 037's ``S: 036`` is a *soft* dependency, and a soft dependency the
    validator never takes is the correct outcome — asking the allocator
    anything would make well-formedness depend on allocation history.
    """
    imported = set()
    for node in ast.walk(TREE):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)

    project = {name for name in imported if name.startswith("coolboy12")}
    assert project == {"coolboy12.bootstrap.identity"}

    forbidden_modules = (
        "ordinal", "registry", "world", "epistemic", "production", "visual",
        "issue", "mutation", "os", "pathlib", "json", "sqlite3", "socket",
        "urllib", "http", "subprocess", "time", "datetime", "random",
    )  # fmt: skip
    assert not [
        name
        for name in imported
        if any(name == m or name.startswith(f"{m}.") for m in forbidden_modules)
    ]

    # The docstrings name the allocator to say it is never consulted, so the
    # check is on what the code references, not on what the prose mentions.
    referenced = {node.id for node in ast.walk(TREE) if isinstance(node, ast.Name)} | {
        node.attr for node in ast.walk(TREE) if isinstance(node, ast.Attribute)
    }
    forbidden_names = ("ordinal", "allocat", "frontier", "ledger", "reuse", "registry")

    assert not [n for n in referenced if any(w in n.lower() for w in forbidden_names)]
    assert not [t for t in _code_literals() if "ordinal" in t.lower()]


# ---------------------------------------------------------------------------
# Registry, Record, lifecycle, canonicality — the refusals
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("kind", ["ZZ", "QQ", "XY", "AB"])
def test_an_unknown_kind_code_is_well_formed(kind):
    """Registry owns kind meaning (Blueprint §13.11, §9.4).

    A two-character code the Registry has never defined is still well-formed.
    Deciding otherwise would make this module the universal kind taxonomy that
    §13.7a prohibits.
    """
    assert validate_envelope(envelope(kind=kind)).valid
    assert validate_identity(
        Identity(partition="W", kind=kind, object_id="000001", slug="Example")
    ).valid


def test_the_module_holds_no_kind_roster():
    """Static half of the Registry boundary — no code appears as data."""
    for node in ast.walk(TREE):
        if isinstance(node, ast.Dict):
            keys = [k.value for k in node.keys if isinstance(k, ast.Constant)]
            assert not [k for k in keys if isinstance(k, str) and len(k) == 2]
    assert not [
        t for t in _code_literals() if len(t) == 2 and t.isascii() and t.isupper()
    ]


def test_any_slug_that_is_well_formed_is_accepted():
    """Blueprint §13.9a: *nothing resolves, matches, or validates against a slug.*

    Two identities differing only in slug are both well-formed. The validator
    has no notion of a correct name and no way to acquire one.
    """
    for slug in ("Maximus", "OtherName", "Z", "a", "Record123", "A1_B2"):
        assert validate_envelope(envelope(slug=slug)).valid


def test_no_lifecycle_or_canonicality_question_is_asked():
    """Six models, six meanings (§13.7c); none of them is universal."""
    for word in ("canonical", "retired", "archived", "published", "draft", "active"):
        assert not [t for t in _code_literals() if word in t.lower()]
    assert not [
        n
        for n in ast.walk(TREE)
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and "canon" in n.name.lower()
    ]


def test_no_envelope_value_beyond_the_identity_is_inspected():
    """Artifact 033 §5.7: it *declares the field, it does not create the vocabulary*.

    Every source-of-truth class name, valid or invented, passes — because the
    validator never looks. Choosing is model-owned (§13.7a).
    """
    for value in ("AUTHORITATIVE", "DERIVED", "NOT-A-CLASS", "", None, 7):
        assert validate_envelope(envelope(sot_class=value)).valid
        assert validate_envelope(envelope(provenance=value)).valid
        assert validate_envelope(envelope(registry_ref=value)).valid


def test_a_valid_result_means_structure_and_nothing_else():
    """What a successful 037 result asserts, stated as behaviour.

    The envelope below is structurally impeccable and semantically absurd: a
    provenance that records nothing, a registry reference pointing at a thing
    no Registry defines, and a source-of-truth class that is not one of the
    five. It validates — and that is the whole point.

    A ``valid`` result means the supplied structure satisfies the envelope and
    identity well-formedness checks this layer owns. It does **not** mean the
    Record exists, is registered, is canonical, is active, was allocated, or
    means anything at all. Those are six different questions with six different
    owners, and 037 is not any of them.
    """
    nonsense = envelope(
        kind="ZZ",
        object_id="654321",
        slug="Not_The_Name_Of_Anything",
        provenance="nobody, never, for no reason",
        registry_ref="R-XX-999999-Defines_Nothing",
        sot_class="NOT-A-SOURCE-OF-TRUTH-CLASS",
    )

    assert validate_envelope(nonsense).valid


def test_no_record_or_storage_is_reached():
    """No Record lookup, no filesystem, no network, no clock."""
    for token in (
        "open(",
        "Path(",
        "os.",
        "json",
        "sqlite",
        "urllib",
        "socket",
        "time.",
    ):
        assert token not in SOURCE, f"{token} appears in the module"  # fmt: skip


def test_the_seven_fields_are_a_roster_not_a_schema():
    """§13.7a: no Universal Record Base, and no universal Record schema.

    The envelope is inspected as a mapping. Nothing here defines a Record type
    for six models to inherit, and no field carries a declared type or default.
    """
    assert isinstance(ENVELOPE_FIELDS, tuple)
    classes = {n.name for n in ast.walk(TREE) if isinstance(n, ast.ClassDef)}
    assert classes == {"ValidationCode", "Finding", "ValidationResult"}
    assert "Record" not in classes
    assert "Envelope" not in classes


def test_the_envelope_input_contract_is_a_mapping():
    """037 DECISION: the annotation and the runtime check say the same thing.

    An earlier revision probed for ``keys`` and ``__getitem__`` while promising
    a ``Mapping``, so an object that merely resembled one was accepted. Any
    real ``Mapping`` is accepted; anything that is not one is refused, however
    convincingly it imitates the interface.
    """
    from collections import OrderedDict
    from collections.abc import Mapping
    from types import MappingProxyType

    class LooksLikeAMapping:
        """Has the methods, is not a Mapping, and is refused for that reason."""

        def keys(self):
            return envelope().keys()

        def __getitem__(self, key):
            return envelope()[key]

    for accepted in (envelope(), OrderedDict(envelope()), MappingProxyType(envelope())):
        assert isinstance(accepted, Mapping)
        assert validate_envelope(accepted).valid

    imitation = LooksLikeAMapping()
    assert not isinstance(imitation, Mapping)
    assert validate_envelope(imitation).codes == (ValidationCode.INVALID_INPUT_TYPE,)


# ---------------------------------------------------------------------------
# Purity
# ---------------------------------------------------------------------------


def test_validation_mutates_nothing_and_repeats_exactly():
    """Row 037 is ``Auth: none``: it decides nothing and changes nothing."""
    identity = parse_identity("W-CH-000001-Maximus")
    subject = envelope(tier=4, partition="w")
    before = dict(subject)

    first = [str(validate_envelope(subject)) for _ in range(5)]
    second = [str(validate_identity(identity)) for _ in range(5)]

    assert len(set(first)) == 1
    assert len(set(second)) == 1
    assert subject == before
    assert identity == parse_identity("W-CH-000001-Maximus")


def test_the_module_holds_no_mutable_state():
    """Nothing at module level can accumulate between calls."""
    mutable = {
        name: value
        for name, value in vars(validate_module).items()
        if not name.startswith("__") and isinstance(value, (list, dict, set, bytearray))
    }

    assert mutable == {}


def test_the_module_performs_no_normalization():
    """035 owns every input decision; a validator that corrected would be a
    second parser with a different answer."""
    called = {
        node.func.attr
        for node in ast.walk(TREE)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    forbidden = ("upper", "lower", "casefold", "strip", "replace", "normalize", "title")

    assert not [name for name in called if any(w in name.lower() for w in forbidden)], (
        f"the module calls a normalizing method: {sorted(called)}"
    )


# ---------------------------------------------------------------------------
# 035 ↔ 037 integration
# ---------------------------------------------------------------------------


def test_the_two_layers_cooperate_in_one_direction():
    """raw string → 035.parse_identity → Identity → 037.validate_identity."""
    identity = parse_identity("W-CH-000002-Maximus_The_Great")

    assert isinstance(identity, Identity)
    assert validate_identity(identity).valid

    # 035 does not import 037, so the direction cannot invert.
    identity_source = Path(inspect.getsourcefile(identity_module)).read_text(
        encoding="utf-8"
    )
    assert "validate" not in identity_source.lower().replace("validates", "").replace(
        "validated", ""
    ).replace("validation", "").replace("validator", "")


def test_what_035_parses_is_what_037_validates():
    """Anti-drift: the two layers agree on every probe, in both directions."""
    from coolboy12.bootstrap.identity import IdentityParseError

    probes = [
        "W-CH-000001-Maximus", "E-XX-000123-Example", "I-QQ-000001-Example",
        "W-WS-000000-WorldStateVariables", "w-CH-000001-Maximus",
        "W-ch-000001-Maximus", "W-CH-000000-Maximus", "W-CH-1-Maximus",
        "W-CH-000001-_Maximus", "W-CH-000001-Maximus!",
    ]  # fmt: skip

    for raw in probes:
        try:
            identity = parse_identity(raw)
        except IdentityParseError:
            parses = False
        else:
            parses = validate_identity(identity).valid

        partition, _, rest = raw.partition("-")
        kind, _, rest = rest.partition("-")
        object_id, _, slug = rest.partition("-")
        validates = validate_envelope(
            envelope(partition=partition, kind=kind, object_id=object_id, slug=slug)
        ).valid

        assert parses is validates, f"{raw} disagrees between 035 and 037"
