"""Boundary proofs for the Artifact 029 adapter shells.

Roadmap row 029 verbatim:

    **029** · eleven adapter boundary shells ·
    `src/coolboy12/adapters/a01_…a11_` · Own: ADAPT · RM: n/a · T: code ·
    R: CONTRACT · SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no ·
    Ph/St: P0/0e · Req: BR-97 · BP: §26.3a · RMS: n/a · H: 001,008 · S: — ·
    LS: — · G: — · → 030,444 · Val: every shell empty; every boundary named;
    **World package constructs marked World-only** · Done: eleven shells ·
    Why: **RULE G3 at P0 — the responsibility is "the boundary exists and is
    empty"; splits at P17 when adapters gain implementations (444–447)** ·
    Risk: medium · ∥: yes

``Val`` names three things and this file proves each: the shells are empty,
the boundaries are named, and the World package constructs are marked
World-only. The eleven identities come from Blueprint §26.3a, which is the
authoritative roster — they are not invented here.

**Emptiness is a P0 condition, not a permanent prohibition.** Artifact 445
implements these adapters, and when it does the emptiness assertions below
are expected to be revisited rather than worked around. Testing the condition
now is what keeps 029 from quietly acquiring an implementation before its
licensing phase; it is not a claim that these files must stay empty forever.

**SOURCE-REQUIRED** — the eleven identities, the A-numbering, the directory,
emptiness at P0, and the World-only marking. These come from row 029 and
Blueprint §26.3a.

**IMPLEMENTATION-QUALITY** — filenames, docstring wording and section order.
The filenames follow the repository's own convention (Artifact 001's tree and
the ``a01_…a11_`` stem the Roadmap gives); the prose is asserted only where a
check needs an anchor.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTERS = REPO_ROOT / "src/coolboy12/adapters"

# Blueprint §26.3a, rows A-1 … A-11, in source order: the names are the
# Blueprint's own and the module stems follow the Roadmap's `a01_…a11_`.
# (shell number, Blueprint row label, canonical boundary name). The row
# label is stored rather than derived from the shell number: deriving "A-1"
# from "A-01" took a pair of string replacements that happened to work and
# would have broken on the next numbering that did not fit them.
BOUNDARIES = {
    "a01_deconstruction": ("A-01", "A-1", "Deconstruction adapter"),
    "a02_vision_analysis": ("A-02", "A-2", "Vision analysis adapter"),
    "a03_visual_index": ("A-03", "A-3", "Visual index adapter"),
    "a04_search_index": ("A-04", "A-4", "Search index adapter"),
    "a05_causal_graph_traversal": ("A-05", "A-5", "Causal-graph traversal adapter"),
    "a06_simulation_numerics": ("A-06", "A-6", "Simulation numerics adapter"),
    "a07_sensitivity_calibration": ("A-07", "A-7", "Sensitivity and calibration adapter"),
    "a08_rendering": ("A-08", "A-8", "Rendering adapter"),
    "a09_index_query_store": ("A-09", "A-9", "Index/query store adapter"),
    "a10_public_viewer": ("A-10", "A-10", "Public viewer adapter"),
    "a11_version_control": ("A-11", "A-11", "Version-control adapter"),
}

STEMS = sorted(BOUNDARIES)

# Concrete components §26 discusses as possible later realizations. Naming one
# here would collapse "the boundary exists" into "the provider is chosen",
# which is the distinction Artifact 029 exists to hold open.
PROVIDERS = (
    "docling", "surya", "openclip", "faiss", "networkx", "simpy", "pysd",
    "imagemagick", "openseadragon", "hugo", "sqlite", "duckdb", "salib",
)

# Two families, both forbidden for the same reason. The universal-record names
# would generalize World package constructs into Record System primitives
# (I-102); the adapter-framework names would turn a mechanism boundary into a
# shared semantic layer (I-103). Neither is required by row 029.
FORBIDDEN_ABSTRACTIONS = (
    "UniversalRecord", "UniversalRelationship", "UniversalHistory",
    "UniversalState", "UniversalKind", "UniversalCanonicalRecord",
    "BaseRecord", "BaseWorldRecord", "BaseAdapterMeaning", "SemanticAdapter",
    "CommonDomainRecord", "AdapterBase", "AdapterRegistry", "AdapterManager",
    "AdapterFactory", "AdapterProtocol", "AdapterContext", "AdapterRuntime",
    "AdapterService",
)


def path_for(stem: str) -> Path:
    return ADAPTERS / f"{stem}.py"


def text(stem: str) -> str:
    return path_for(stem).read_text(encoding="utf-8")


def tree(stem: str) -> ast.Module:
    return ast.parse(text(stem))


# --------------------------------------------------------------------------
# Done — eleven shells.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


def test_the_adapter_package_exists():
    assert ADAPTERS.is_dir()


def test_exactly_eleven_boundary_modules_exist():
    """``Done: eleven shells``. Eleven, and no twelfth.

    Scoped to this directory because the directory *is* the artifact: row 029
    owns `src/coolboy12/adapters/a01_…a11_` and nothing else, so an extra
    module here is 029 growing rather than a later artifact arriving
    elsewhere.
    """
    present = sorted(path.stem for path in ADAPTERS.glob("*.py"))

    assert present == STEMS, set(present) ^ set(STEMS)


@pytest.mark.parametrize("stem", STEMS)
def test_boundary_module_exists(stem):
    assert path_for(stem).is_file()
    assert text(stem).strip()


def test_the_package_carries_no_second_architecture():
    """No ``__init__.py``, no subpackages, no vendor workspace.

    The repository configures implicit namespace packages
    (``[tool.setuptools.packages.find] namespaces = true``) and carries no
    ``__init__.py`` anywhere in ``src/`` — ``coolboy12.bootstrap.config``
    imports without one. Adding one here would depart from that convention
    and give the package a second place to accumulate architecture.
    """
    assert not (ADAPTERS / "__init__.py").exists()

    subdirectories = [
        path.name for path in ADAPTERS.iterdir()
        if path.is_dir() and path.name != "__pycache__"
    ]
    assert not subdirectories, subdirectories

    non_python = sorted(
        path.name for path in ADAPTERS.iterdir() if path.is_file() and path.suffix != ".py"
    )
    assert non_python == ["PURPOSE.md"], non_python


# --------------------------------------------------------------------------
# Val — every boundary is named.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("stem", STEMS)
def test_boundary_declares_its_number_and_canonical_name(stem):
    """*Empty* is not *unnamed*.

    Later contracts and implementations attach to a known boundary, so the
    identity has to be stable and self-describing now. ``adapter1.py`` with an
    empty docstring would satisfy "eleven shells" and defeat the artifact.
    """
    number, _, name = BOUNDARIES[stem]

    assert text(stem).startswith(f'"""{number} — {name} boundary.')


@pytest.mark.parametrize("stem", STEMS)
def test_boundary_cites_its_blueprint_row(stem):
    """§26.3a is the roster these eleven come from; each shell points back."""
    row = BOUNDARIES[stem][1]

    assert "§26.3a" in text(stem)
    assert f"row {row}" in text(stem), row


@pytest.mark.parametrize("stem", STEMS)
def test_boundary_states_what_it_does_not_own(stem):
    """A boundary that only says what it takes is half a boundary.

    §26.3a gives every row a *does not supply* column, and it is the half that
    protects against implementation-first drift: a component supplies a
    computation, never a meaning.
    """
    body = text(stem)

    assert "must not" in body, stem


@pytest.mark.parametrize("stem", STEMS)
def test_boundary_states_that_implementation_is_deferred(stem):
    body = text(stem)

    assert "Artifact 029 establishes the boundary only" in body
    assert "444" in body and "445" in body


# --------------------------------------------------------------------------
# Val — every shell is empty.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("stem", STEMS)
def test_shell_is_a_docstring_and_nothing_else(stem):
    """Parsed, not grepped: the module's whole body is one string expression.

    This is the strongest form of "empty" available without reading prose —
    anything executable at all, of any shape, adds a second statement.
    """
    body = tree(stem).body

    assert len(body) == 1, [type(node).__name__ for node in body]
    assert isinstance(body[0], ast.Expr)
    assert isinstance(body[0].value, ast.Constant)
    assert isinstance(body[0].value.value, str)


@pytest.mark.parametrize("stem", STEMS)
def test_shell_imports_nothing(stem):
    """No external dependency, and no coolboy12 import either.

    An import of a World Record class would be the quiet route to the
    generalization I-102 forbids.
    """
    imports = [
        node for node in ast.walk(tree(stem))
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ]

    assert not imports, [ast.unparse(node) for node in imports]


@pytest.mark.parametrize("stem", STEMS)
def test_shell_defines_no_function_or_class(stem):
    """No placeholder that pretends to be an implementation.

    Row 029's ``Why`` is explicit that the responsibility is *the boundary
    exists and is empty*; a stub class with ``connect()`` would make the file
    look complete and the artifact wrong.
    """
    definitions = [
        node.name for node in ast.walk(tree(stem))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    ]

    assert not definitions, definitions


@pytest.mark.parametrize("stem", STEMS)
def test_shell_names_no_provider(stem):
    """*Boundary exists* is not *provider chosen*.

    §26 discusses possible realizations; 029 is before implementation, and
    naming one here would collapse the two.
    """
    lowered = text(stem).lower()
    named = [provider for provider in PROVIDERS if provider in lowered]

    assert not named, named


def test_no_store_index_or_asset_was_created():
    """The adapter directory is a boundary location, not a storage location.

    ``__pycache__`` is excluded: it is interpreter output, appears the moment
    anything imports the package, and is git-ignored. Counting it as a stray
    made this test fail on its own import-sanity check — a false positive that
    said nothing about the boundary.
    """
    strays = [
        path.name for path in ADAPTERS.rglob("*")
        if path.is_file()
        and path.suffix not in (".py", ".md")
        and "__pycache__" not in path.parts
    ]

    assert not strays, strays


# --------------------------------------------------------------------------
# Val — World package constructs marked World-only.  SOURCE-REQUIRED.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("stem", STEMS)
def test_shell_marks_world_package_constructs_as_world_only(stem):
    """The marking row 029 asks for by name.

    Adapter boundaries are shared infrastructure; World package semantics are
    not universal. Recording that distinction at the boundary is what stops a
    later reader treating WSV or the History Record as something every Record
    Model has.
    """
    body = text(stem)

    flowed = " ".join(body.split())

    for construct in ("World Record", "World Relationship Record",
                      "World History Record", "WSV", "WSV-H"):
        assert construct in body, construct

    # The marking itself, not just the roster. Listing the five constructs and
    # saying they are "not universal" leaves out the half that matters: *whose*
    # they are. Deleting "are World Record Model constructs" left every other
    # assertion here green while the World-only claim was gone.
    assert "are World Record Model constructs" in flowed
    assert "not be assumed as universal" in flowed
    assert "I-102" in body


@pytest.mark.parametrize("stem", STEMS)
def test_shell_introduces_no_universal_or_framework_abstraction(stem):
    """Mechanism may be shared; semantics may not (I-103).

    The eleven boundaries are deliberately eleven separate names. A base class
    unifying them would be exactly the elegance that turns a mechanism
    boundary into a semantic layer.
    """
    body = text(stem)
    found = [name for name in FORBIDDEN_ABSTRACTIONS if name in body]

    assert not found, found


@pytest.mark.parametrize("stem", STEMS)
def test_shell_references_no_canonical_write_path(stem):
    """``Canon: n/a``, ``Auth: none``. The boundary has no canonical authority.

    Checked as a path reference rather than the word "canon", which A-09 and
    A-11 must use to say what they may not touch — a prohibition contains the
    words it prohibits.
    """
    assert "canon/" not in text(stem)
