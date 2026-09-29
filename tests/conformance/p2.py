"""Artifact 059 — P2 kernel conformance suite. The exit-P2 gate.

Roadmap row 059 verbatim:

    **059** · P2 kernel conformance suite · `tests/conformance/p2.py` ·
    Own: CONST · RM: all · T: test · R: PROOF · SoT: DEV-ENV · Auth: none ·
    Canon: n/a · CD: no · Ph/St: P2/2e · Req: BR-17…BR-22 · BP: §13 ·
    RMS: §§2–6 · H: 039–058 · S: — · LS: — · G: **exit-P2** · → P3 ·
    Val: nine prohibitions hold; no universal RR/HR/lifecycle/canonicality ·
    Done: green · Why: kernel correctness gates Registry · Risk: low · ∥: no

What this gate proves
---------------------
Exactly the two clauses row 059's ``Val`` states, read back out of the Roadmap::

    nine prohibitions hold
    no universal RR/HR/lifecycle/canonicality

A prohibition "holds" here on three signals together: the governing source
states it; the P2 artifact that owns it still states it; and no P2 artifact
makes a positive claim that contradicts it.

What this gate does **not** prove
---------------------------------
It owns none of the rules it checks. Artifacts 039–058 own the P2 kernel, the
Blueprint and the RMS govern them, and this suite only puts them side by side.
The nine prohibitions are parsed from RMS §4 and the six models from RMS §2;
the suite holds no copy of either. It does not decide the W → V edge that
Artifact 058 records as an unresolved source conflict, and it does not decide
whether 058 is the RMS's Deliverable J. It proves nothing at runtime, and
nothing about the Kinds, schemas, lifecycles or packages later phases design.

Implementation decision: every check is static, deterministic, offline and
read-only. It reads repository text and imports nothing from ``coolboy12``.

The regression scan is a guard, not a parser of meaning. It flags a statement
that names a prohibited universal structure with no negation in the statement,
in the lead-in of its list, or in its section heading. A contrary claim that
also carries an unrelated negation can pass it; the positive checks exist for
that reason.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ROADMAP = REPO_ROOT / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"
BLUEPRINT = REPO_ROOT / "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md"
RMS = REPO_ROOT / "docs/sources/COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md"

UNRESOLVED_OWNED_CHECKS: dict[str, str] = {}
"""Checks this suite owns and could not run. A skip is not a proof. Empty."""


# ---------------------------------------------------------------------------
# Reading the repository
# ---------------------------------------------------------------------------


def _read(path: Path) -> str:
    """A required file, as text. A missing file fails; it is never skipped."""
    assert path.is_file(), (
        f"required P2 source is missing: {path.relative_to(REPO_ROOT)}"
    )
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _roadmap_row(number: str) -> str:
    """The Roadmap row for an artifact, as written."""
    match = re.search(rf"^\*\*{number}\*\* · .*?$", _read(ROADMAP), re.MULTILINE)
    assert match, f"Roadmap row {number} not found"
    return match.group(0)


def _field(number: str, name: str, following: str) -> str:
    """One field of a Roadmap row, bounded by the field that follows it."""
    match = re.search(rf"· {name}: (.*?) · {following}:", _roadmap_row(number))
    assert match, f"Roadmap row {number}: {name} field not found, or changed shape"
    return match.group(1)


def _val_of(number: str) -> str:
    return _field(number, "Val", "Done")


def _dependencies() -> list[str]:
    """Row 059's ``H:`` range, expanded. The suite holds no list of its own."""
    match = re.fullmatch(r"(\d{3})–(\d{3})", _field("059", "H", "S"))
    assert match, "row 059's H field is no longer a single range"
    first, last = (int(n) for n in match.groups())
    return [f"{n:03d}" for n in range(first, last + 1)]


def _artifact_files(number: str) -> list[Path]:
    """The files at an artifact's Roadmap path. Missing files fail."""
    path = re.search(r"· `([^`]+)` ·", _roadmap_row(number))
    assert path, f"row {number}: path field not found"
    files = sorted(REPO_ROOT.glob(path.group(1)))
    assert files, f"artifact {number} is absent from its Roadmap path {path.group(1)}"
    return files


def _artifact(number: str) -> str:
    return "\n".join(_read(path) for path in _artifact_files(number))


def _doc_artifacts() -> dict[str, str]:
    """The P2 dependencies that are documents, keyed by artifact number."""
    return {
        number: _artifact(number)
        for number in _dependencies()
        if all(path.suffix == ".md" for path in _artifact_files(number))
    }


def _flat(text: str) -> str:
    """Markdown emphasis, quote markers and line breaks removed."""
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)
    text = text.replace("**", "").replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def _section(text: str, title: str) -> str:
    """The body of the heading that begins with ``title``, to the next peer."""
    heading = re.search(
        rf"^(#{{1,6}}) +{re.escape(title)}.*$", text, flags=re.MULTILINE
    )
    assert heading, f"section {title!r} not found"
    level = len(heading.group(1))
    end = re.compile(rf"^#{{1,{level}}} ", flags=re.MULTILINE)
    rest = end.search(text, heading.end())
    return text[heading.start() : rest.start() if rest else len(text)]


def _says(text: str, phrase: str) -> bool:
    return _flat(phrase) in _flat(text)


def _nine_prohibitions() -> list[str]:
    """RMS §4's frozen list, as the RMS states it."""
    section = _section(_read(RMS), "4. Universal Record Architecture")
    line = re.search(r"Nine prohibitions[^:]*:(.*)", section)
    assert line, "RMS §4 no longer states its nine prohibitions"
    items = [_flat(item).rstrip(".") for item in line.group(1).split("·")]
    return [re.sub(r"^no ", "", item, flags=re.IGNORECASE).lower() for item in items]


def _six_models() -> list[tuple[str, str]]:
    """RMS §2's six sovereign Record Models, as partition and name."""
    section = _section(_read(RMS), "2. Constitutional Status")
    return re.findall(r"\*\*([A-Z])\*\* ([A-Z][a-z]+)", section)


# ---------------------------------------------------------------------------
# The regression scan: a positive claim a P2 artifact must not make
# ---------------------------------------------------------------------------

PROHIBITION_ALIASES = {
    # The two governing sources name two of the nine in different words. Keys
    # are RMS §4's labels as parsed; every alias is a governing source's own
    # wording, recognised so a claim cannot pass by using the other source's.
    #
    # RMS §4: "universal semantic schema".
    # Blueprint §13.7a and §13 intro: "No universal Record schema."
    "universal semantic schema": ("universal record schema",),
    # RMS §4: "universal identity *composition*".
    # Blueprint §13.7a, §13.9a: "a universal identity grammar is not a
    #   universal Record semantics"; RMS §5: "UNIVERSAL IDENTITY GRAMMAR ≠
    #   UNIVERSAL SEMANTIC MODEL"; Blueprint §13 and RMS §6 name "identity
    #   semantics" as what the six models do not share and each model owns.
    #
    # "universal identity grammar" is deliberately absent: RMS §5 and
    # Blueprint §13.7a and §13.9a make the grammar universal (AD-1, resolved).
    # The Blueprint's §13 intro still lists "no universal identity grammar";
    # that source-internal inconsistency is reported, not decided here.
    "universal identity composition": (
        "universal record semantics",
        "universal semantic model",
        "universal identity semantics",
    ),
}

# "unless" is not here: a qualified universal ("... unless overridden") still
# asserts the universal as the default architecture.
NEGATION = re.compile(
    r"\b(no|not|never|nor|none|nothing|without|neither|cannot|anti"
    r"|prohibit\w*|forbid\w*|refus\w*|reject\w*|retire\w*|reintroduc\w*"
    r"|reinstat\w*|resurrect\w*|revive\w*|rather than|instead of)\b|≠",
    re.IGNORECASE,
)
# A negation governs only its own clause. A prose statement is split here so a
# "no" in one clause cannot excuse a universal claimed in the next.
CLAUSE_BREAK = re.compile(
    r";|\s[—–]\s|,?\s+\b(?:but|however|although|though|whereas|while|yet)\b",
    re.IGNORECASE,
)
NEGATIVE_HEADING = re.compile(
    r"prohibit|non-goal|anti-pattern|forbidden|does not|do not|not define"
    r"|not establish|explicitly does not",
    re.IGNORECASE,
)
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def _statements(section: str) -> list[tuple[str, bool]]:
    """A section's statements, each flagged ``True`` if it is a table row:
    table rows, list items with their lead-in, and prose sentences. A list
    inherits the sentence that introduces it."""
    blocks: list[list[str]] = [[]]
    for line in section.splitlines()[1:]:
        if line.strip():
            blocks[-1].append(line)
        elif blocks[-1]:
            blocks.append([])
    statements: list[tuple[str, bool]] = []
    lead = ""
    for block in (b for b in blocks if b):
        if all(line.lstrip().startswith("|") for line in block):
            statements += [(_flat(line), True) for line in block]
            lead = ""
        elif LIST_ITEM.match(block[0]):
            items: list[list[str]] = []
            for line in block:
                if LIST_ITEM.match(line) or not items:
                    items.append([])
                items[-1].append(line)
            statements += [
                (_flat(lead + " " + " ".join(item)), False) for item in items
            ]
        else:
            sentences = re.split(r"(?<=[.!?])\s+", _flat(" ".join(block)))
            statements += [(sentence, False) for sentence in sentences]
            lead = sentences[-1] if sentences[-1].endswith(":") else ""
    return statements


def _unnegated(text: str, pattern: re.Pattern[str]) -> list[str]:
    """Clauses that name ``pattern`` with no negation governing that clause.

    A negation counts only inside the clause that names the claim, inside the
    lead-in of the list the claim sits in, or in the section heading. A table
    row is judged whole, because its verdict (``NO``, ``Never``, ``≠``) sits in
    a cell of its own.
    """
    found = []
    for section in re.split(r"(?m)^(?=#{1,3} )", text):
        heading = section.splitlines()[0] if section.strip() else ""
        if NEGATIVE_HEADING.search(heading):
            continue
        for statement, is_row in _statements(section):
            clauses = [statement] if is_row else CLAUSE_BREAK.split(statement)
            found += [
                clause
                for clause in clauses
                if pattern.search(clause) and not NEGATION.search(clause)
            ]
    return found


def _prohibition_names(label: str) -> tuple[str, ...]:
    """RMS §4's label for one prohibition, and its source-grounded aliases."""
    return (label, *PROHIBITION_ALIASES.get(label, ()))


def _prohibited_pattern(labels: list[str] | None = None) -> re.Pattern[str]:
    """The claims RMS §4 prohibits, under either governing source's name."""
    names = [
        name
        for label in (labels or _nine_prohibitions())
        for name in _prohibition_names(label)
    ]
    assert set(PROHIBITION_ALIASES) <= set(_nine_prohibitions()), (
        "an alias names no RMS §4 prohibition"
    )
    return re.compile(
        "|".join(rf"\b{re.escape(name)}\b" for name in names), re.IGNORECASE
    )


def _contrary_claims(pattern: re.Pattern[str]) -> list[str]:
    return [
        f"{number}: {claim[:160]}"
        for number, text in _doc_artifacts().items()
        for claim in _unnegated(text, pattern)
    ]


# ---------------------------------------------------------------------------
# Val clause 1 — nine prohibitions hold
# ---------------------------------------------------------------------------


def test_p2_nine_prohibitions_hold():
    """Row 059 ``Val``: *nine prohibitions hold*.

    RMS §4 freezes the nine. Artifact 043 §6 owns them and says it reproduces
    them verbatim from Blueprint §13.7a; Artifact 039 §9 summarises them. The
    three are compared, and then every P2 document is scanned for a positive
    claim naming any of the nine.
    """
    nine = _nine_prohibitions()
    assert len(nine) == 9, f"RMS §4 no longer states nine prohibitions: {nine}"

    owned = _section(_artifact("043"), "6. The Nine Prohibitions")
    assert _says(owned, "reproduced verbatim from Blueprint §13.7a and are binding"), (
        "043 §6 no longer binds the nine as Blueprint §13.7a's verbatim text"
    )
    items: list[list[str]] = []
    for line in owned.splitlines():
        if re.match(r"^\d+\. ", line):
            items.append([line])
        elif items and line.startswith("   "):
            items[-1].append(line)
    stated = [_flat(re.sub(r"^\d+\. ", "", " ".join(item))) for item in items]
    assert len(stated) == len(nine), (
        f"043 §6 states {len(stated)} prohibitions; RMS §4 freezes {len(nine)}"
    )

    # Blueprint §13.7a's own list of the nine, in its own order.
    listed = _section(_read(BLUEPRINT), "13.7a").split("What is *not* shared", 1)
    assert len(listed) == 2, "Blueprint §13.7a lost its list of what is not shared"
    bullets: list[list[str]] = []
    for line in listed[1].splitlines():
        if line.startswith("- **"):
            bullets.append([line])
        elif bullets and line.strip() and not line.startswith(("- ", "**")):
            bullets[-1].append(line)
        elif bullets and line.startswith("**"):
            break
    blueprint = [_flat(" ".join(bullet)[2:]) for bullet in bullets]
    assert stated == blueprint, (
        "043 §6 no longer reproduces Blueprint §13.7a item for item.\n"
        + "\n".join(
            f"  {n}: 043 {a[:60]!r} / Blueprint {b[:60]!r}"
            for n, (a, b) in enumerate(zip(stated, blueprint), 1)
            if a != b
        )
    )

    # Rule for rule: RMS §4's n-th prohibition is the Blueprint's n-th, named
    # in either source's words (PROHIBITION_ALIASES).
    misaligned = [
        f"{n}: RMS {label!r} / Blueprint {text[:70]!r}"
        for n, (label, text) in enumerate(zip(nine, blueprint), 1)
        if not any(name in text.lower() for name in _prohibition_names(label))
    ]
    assert not misaligned, "\n  ".join(
        ["RMS §4 and Blueprint §13.7a / 043 §6 no longer align rule for rule:"]
        + misaligned
    )

    summary = _section(_artifact("039"), "9. What the Record System")
    roster = next(
        (p for p in summary.split("\n\n") if p.count("·") == len(nine) - 1), ""
    )
    summarised = [
        re.sub(r"^no ", "", _flat(item).rstrip("."), flags=re.IGNORECASE).lower()
        for item in roster.split("·")
    ]
    assert summarised == nine, (
        f"039 §9 no longer summarises RMS §4 rule for rule.\n"
        f"  RMS §4: {nine}\n  039 §9: {summarised}"
    )

    contrary = _contrary_claims(_prohibited_pattern())
    assert not contrary, "\n  ".join(
        ["P2 kernel regression: a P2 artifact claims a prohibited universal:"]
        + contrary
    )


# ---------------------------------------------------------------------------
# Val clause 2 — no universal RR/HR/lifecycle/canonicality
# ---------------------------------------------------------------------------


def test_p2_relationship_record_is_world_only():
    """No universal Relationship Record (I-102; row 055 ``Val``)."""
    assert _says(
        _read(BLUEPRINT),
        "Relationship Record and History Record are World Record Model concepts. "
        "Neither is a Record System primitive",
    ), "Blueprint I-102 no longer scopes the Relationship Record to World"
    assert "Relationship Record declared **World-only**" in _val_of("055")
    assert _says(_artifact("055"), "Relationship Record declared World-only"), (
        "055 no longer declares the Relationship Record World-only"
    )
    table = _section(_artifact("039"), "4. The Six Sovereign Record Models")
    assert _says(
        table,
        "| Relationship Record | A World Record Model concept, not a Record System "
        "primitive |",
    ), "039 no longer excludes the Relationship Record from the Record System"


def test_p2_history_record_is_world_only():
    """No universal History Record (I-102; row 054 ``Val``)."""
    assert "no universal History Record" in _val_of("054")
    split = _section(_artifact("054"), "6. Universal Obligation vs Model-Owned")
    assert _says(split, "Whether the model has any structure shaped like a History"), (
        "054 §6 no longer leaves the History Record shape to each model"
    )
    assert _says(
        _artifact("054"), "| Universal obligation | ≠ universal History Record |"
    )
    table = _section(_artifact("039"), "4. The Six Sovereign Record Models")
    assert _says(
        table,
        "| History Record | A World Record Model concept, not a Record System "
        "primitive |",
    ), "039 no longer excludes the History Record from the Record System"
    assert _says(_read(RMS), "The World History Record is World-only"), (
        "RMS §17 (AD-11) no longer scopes the History Record to World"
    )


def test_p2_lifecycle_is_model_owned():
    """No universal lifecycle (RMS §4–§6; Blueprint §13.7a; Artifact 043)."""
    rms = _read(RMS)
    owned = _section(rms, "5. Universal Identity Grammar")
    assert _says(
        owned,
        "Model-owned: Kind meaning · Kind taxonomy · semantic "
        "interpretation · lifecycle meaning",
    ), "RMS §5 no longer makes lifecycle meaning model-owned"
    assert _says(rms, "other models define their own state vocabularies"), (
        "RMS §4 no longer leaves state vocabularies to each model"
    )
    prohibitions = _section(_artifact("043"), "6. The Nine Prohibitions")
    assert _says(prohibitions, "No universal lifecycle."), (
        "043 §6 no longer prohibits a universal lifecycle"
    )


def test_p2_canonicality_is_model_defined():
    """No universal canonicality (I-104; rows 052 ``Val`` and ``Why``)."""
    assert _says(
        _read(BLUEPRINT),
        "Record and Canon are not synonyms. Canonicality is a status property whose "
        "meaning is defined by each Record Model that has one",
    ), "Blueprint I-104 no longer makes canonicality model-defined"
    assert "P and I never canonical" in _val_of("052")
    assert "a universal boolean here reintroduces COM" in _field("052", "Why", "Risk")
    canonicality = _artifact("052")
    assert _section(canonicality, "5. The Six Meanings"), "052 lost its six meanings"
    assert _says(canonicality, "It is not a universal boolean"), (
        "052 no longer refuses canonicality as a universal boolean"
    )


def test_p2_no_universal_rr_hr_lifecycle_canonicality():
    """Row 059 ``Val``: *no universal RR/HR/lifecycle/canonicality*.

    The clause names four structures, and each has its own proof above so a
    failure names the one that broke. This proof runs all four.
    """
    for proof in (
        test_p2_relationship_record_is_world_only,
        test_p2_history_record_is_world_only,
        test_p2_lifecycle_is_model_owned,
        test_p2_canonicality_is_model_defined,
    ):
        proof()


# ---------------------------------------------------------------------------
# The gate
# ---------------------------------------------------------------------------

VAL_CLAUSES = {
    "nine prohibitions hold": test_p2_nine_prohibitions_hold,
    "no universal RR/HR/lifecycle/canonicality": (
        test_p2_no_universal_rr_hr_lifecycle_canonicality
    ),
}


def test_exit_p2_gate_covers_its_val_and_carries_no_unresolved_check():
    """The gate itself. ``G: exit-P2`` — and a skip is not a proof.

    Built to the shape of exit-P0 and exit-P1. The clause names are read back
    out of row 059's own ``Val``, in both directions, so the mapping cannot
    drift from the Roadmap; each proof must be this module's live definition;
    and each is called here, so a failing clause fails exit-P2.

    **Gate and suite.** The named exit gate directly invokes only the clauses
    declared in row 059's ``Val``. Supporting tests remain part of ``Done:
    green``, because pytest must report the entire Artifact 059 suite green;
    they are not thereby Roadmap gate clauses.
    """
    val = _val_of("059")

    undeclared = [clause for clause in VAL_CLAUSES if clause not in val]
    assert not undeclared, f"exit-P2 gates clauses row 059 does not state: {undeclared}"
    stated = {clause.strip() for clause in val.split(";") if clause.strip()}
    ungated = sorted(stated - set(VAL_CLAUSES))
    assert not ungated, f"row 059 states clauses exit-P2 does not gate: {ungated}"

    live = {
        name: value
        for name, value in globals().items()
        if callable(value) and name.startswith("test_p2_")
    }
    detached = [
        clause
        for clause, proof in VAL_CLAUSES.items()
        if live.get(proof.__name__) is not proof
    ]
    assert not detached, f"a gated clause names a proof not defined here: {detached}"
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
        ["exit-P2 cannot be GREEN — a Val clause is unproven:"] + failed
    )

    assert not UNRESOLVED_OWNED_CHECKS, "\n  ".join(
        ["exit-P2 cannot be GREEN — checks this suite owns could not run:"]
        + [f"{check}: {why}" for check, why in sorted(UNRESOLVED_OWNED_CHECKS.items())]
    )


# ---------------------------------------------------------------------------
# Supporting conformance — six sovereign models and the retired architecture
# ---------------------------------------------------------------------------


def test_p2_exactly_six_sovereign_record_models_agree_across_rms_039_040_041():
    """RMS §2 names six; 039 §4, 040's six stubs and 041 §3 must name the same."""
    models = _six_models()
    assert len(models) == 6 and len({p for p, _ in models}) == 6, (
        f"RMS §2 no longer names six sovereign Record Models: {models}"
    )

    table = _section(_artifact("039"), "4. The Six Sovereign Record Models")
    in_039 = re.findall(r"^\| \*\*([A-Z])\*\* ([A-Z][a-z]+) \|", table, re.MULTILINE)
    rows = _section(_artifact("041"), "3. The Sovereign Record Models")
    in_041 = re.findall(r"^\| \*\*([A-Z])\*\* \| ([A-Z][a-z]+) \|", rows, re.MULTILINE)
    stubs = re.findall(
        r"^\| Model \| \*\*([A-Z])\*\* — ([A-Z][a-z]+) \|",
        _artifact("040"),
        re.MULTILINE,
    )

    for name, found in (("039 §4", in_039), ("041 §3", in_041), ("040", stubs)):
        assert sorted(found) == sorted(models), (
            f"{name} disagrees with RMS §2 on the six Record Models.\n"
            f"  RMS §2: {sorted(models)}\n  {name}: {sorted(found)}"
        )


def test_p2_no_seventh_record_model_and_the_canon_object_model_is_retired():
    """RMS §2, §25; 039 §4, §10; 041 §3."""
    rms = _read(RMS)
    assert _says(
        rms,
        "The Canon Object Model is fully superseded and retired as "
        "current architecture",
    )
    assert _says(rms, "NO SEVENTH SOVEREIGN RECORD MODEL IS REQUIRED AT v1.0")
    record_system = _artifact("039")
    assert _says(record_system, "no seventh Record Model is required at v1.0"), (
        "039 no longer closes the model set at six"
    )
    assert _section(record_system, "10. The Canon Object Model Is Retired")
    assert _says(_artifact("041"), "There is no seventh."), (
        "041 no longer refuses a seventh Record Model"
    )


def test_p2_no_model_is_a_superclass_and_world_is_not_a_template():
    """RMS §2; I-101; 041 S-6 and S-8 — and no P2 text says otherwise."""
    assert _says(
        _read(RMS), "No model is a superclass of another. World is not a template."
    )
    assert _says(
        _read(BLUEPRINT),
        "No Record Model is a specialization of another, "
        "and no Record Model is the template for another.",
    )
    sovereignty = _artifact("041")
    assert _says(
        sovereignty,
        "S-6. No sovereign Record Model is a semantic "
        "specialization of another sovereign Record Model.",
    )
    assert _says(sovereignty, "S-8. World is not a template.")

    contrary = _contrary_claims(re.compile(r"\b(superclass|template)\b", re.I))
    assert not contrary, "\n  ".join(
        ["P2 kernel regression: World or a model made a template or superclass:"]
        + contrary
    )


# ---------------------------------------------------------------------------
# Supporting conformance — partition, mechanism, identity
# ---------------------------------------------------------------------------


def test_p2_one_record_one_partition_one_owning_model_no_conversion():
    """Row 045 ``Val``; I-16; 045 §4, §8, §9."""
    assert _val_of("045") == "exactly one partition per Record; conversion prohibited"
    assert _says(_read(BLUEPRINT), "Cross-partition conversion is prohibited.")
    partition = _artifact("045")
    assert _says(
        partition,
        "Record ──belongs to──▶ EXACTLY ONE partition ──owns──▶ "
        "EXACTLY ONE sovereign Record Model",
    )
    assert _section(partition, "8. The Cross-Partition Conversion Prohibition")
    assert _says(
        _section(partition, "9. Ownership Is Not Reference"),
        "a reference DOES NOT TRANSFER OWNERSHIP",
    ), "045 §9 no longer holds that a reference transfers no ownership"


def test_p2_shared_mechanism_is_not_shared_semantics():
    """Blueprint §13.7a; RMS §3 (I-103); 043 §2, §8."""
    assert _section(
        _read(BLUEPRINT), "13.7a Shared Infrastructure Is Not Shared Semantics"
    )
    assert _says(
        _read(RMS),
        "a mechanism may be shared; a semantic may not be shared "
        "without evidence in each model that carries it",
    )
    mechanism = _artifact("043")
    assert _says(
        _section(mechanism, "2. The Governing Rule"),
        "The Record System shares mechanisms. It does not share semantics.",
    )
    assert _section(mechanism, "8. The Facility-or-Claim Test")


def test_p2_universal_identity_grammar_is_not_universal_identity_semantics():
    """RMS §5; 043 §7; 046 §5. The grammar is universal; its meaning is not."""
    rms = _section(_read(RMS), "5. Universal Identity Grammar")
    grammar = "[PARTITION]-[KIND]-[OBJECT_ID]-[SLUG]"
    assert grammar in rms, "RMS §5 no longer states the universal identity grammar"
    assert _says(rms, "UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL")

    exception = _section(_artifact("043"), "7. The Identity Exception")
    assert grammar in exception
    assert _says(
        exception,
        "The identity grammar fixes the syntax of the name; it "
        "does not decide what the named thing means.",
    )
    assert _section(_artifact("046"), "5. Universal Grammar Is Not Universal Semantics")


def test_p2_universal_envelope_is_the_bootstrap_set_and_no_more():
    """RMS §4; Blueprint §13.7a. A guard, not a second envelope validator."""
    rms = _read(RMS)
    assert _says(rms, "The universal envelope is the bootstrap set and no more")
    assert _says(rms, "tier and status are NOT universal envelope fields")
    assert _says(_section(_read(BLUEPRINT), "13.7a"), "No universal Record schema.")


# ---------------------------------------------------------------------------
# Supporting conformance — three of the nine, each proven on its own
# ---------------------------------------------------------------------------


def _claims_of(label: str) -> list[str]:
    """Contrary claims naming one RMS §4 prohibition, under either name."""
    assert label in _nine_prohibitions(), f"RMS §4 names no prohibition {label!r}"
    return _contrary_claims(_prohibited_pattern([label]))


def test_p2_no_universal_kind_taxonomy():
    """Blueprint §13.7a, I-106; RMS §5, §6; 044 §15; 057 §2, §4.

    Each model owns its taxonomy; only World's is established; and World's
    §13.11 admission treatment stays World's own, not a rule for every model.
    """
    assert _says(
        _section(_read(BLUEPRINT), "13.7a"),
        "No universal kind taxonomy. Each model owns its own",
    )
    assert _says(
        _read(BLUEPRINT),
        "Only the World taxonomy is established; every other roster names a boundary",
    )
    rms = _read(RMS)
    assert _says(rms, "owns: its Kind taxonomy")
    assert _says(
        _section(rms, "5. Universal Identity Grammar"),
        "Model-owned: Kind meaning · Kind taxonomy",
    )
    assert _says(
        _artifact("044"),
        "| That Kind means a class of Records within one "
        "model | Which Kinds exist in a model, and what each means |",
    )
    admission = _artifact("057")
    assert _says(admission, "It admits no Kind and decides no model's roster")
    assert _says(
        admission,
        "For World, Blueprint §13.11 separately defines an "
        "eight-question admission treatment",
    )

    contrary = _claims_of("universal kind taxonomy")
    assert not contrary, "\n  ".join(
        ["P2 kernel regression: a universal Kind taxonomy is claimed:"] + contrary
    )


def test_p2_no_universal_state_model():
    """Blueprint §13.7a; RMS §4, §7; 044 §15. World's mutation classes are
    World's; every other model defines its own state vocabulary."""
    assert _says(
        _section(_read(BLUEPRINT), "13.7a"),
        "No universal state model. "
        "Locked / world-state / derived is a World field-mutation-class "
        "split and is not claimed elsewhere.",
    )
    rms = _read(RMS)
    assert _says(
        rms,
        "Field mutation classes: locked / world-state / derived — a "
        "World classification, not a universal state model.",
    )
    assert _says(rms, "other models define their own state vocabularies")
    assert _says(
        _artifact("044"),
        "| That State is a category | The actual states, "
        "and the transitions between them |",
    )

    contrary = _claims_of("universal state model")
    assert not contrary, "\n  ".join(
        ["P2 kernel regression: a universal state model is claimed:"] + contrary
    )


def test_p2_no_universal_semantic_record_schema():
    """RMS §4 and Blueprint §13.7a name one prohibition in two words — semantic
    schema, Record schema. The seven-field envelope is its ceiling, not a
    universal schema; 043 §6 and 039 §9 carry the prohibition."""
    rms = _read(RMS)
    assert _says(rms, "The universal envelope is the bootstrap set and no more")
    assert _says(rms, "universal semantic schema")
    blueprint = _read(BLUEPRINT)
    assert _says(_section(blueprint, "13.7a"), "No universal Record schema.")
    assert _says(blueprint, "It is not a universal Record schema"), (
        "Blueprint §13.1 no longer denies that the World envelope is universal"
    )
    assert _says(
        _section(_artifact("043"), "6. The Nine Prohibitions"),
        "No universal Record schema.",
    )
    assert _says(_artifact("039"), "no universal semantic schema")

    contrary = _claims_of("universal semantic schema")
    assert not contrary, "\n  ".join(
        ["P2 kernel regression: a universal semantic/Record schema is claimed:"]
        + contrary
    )


# ---------------------------------------------------------------------------
# Supporting conformance — provenance, temporal, package, authority, Kind
# ---------------------------------------------------------------------------


def test_p2_provenance_capture_is_shared_and_meaning_is_model_owned():
    """Row 048 ``Val``; 048 §4, §10."""
    assert _val_of("048") == "capture shared, meaning model-owned"
    provenance = _artifact("048")
    assert _says(
        provenance,
        "Provenance capture is shared infrastructure. Provenance "
        "meaning is owned by the Record Model",
    )
    assert _section(provenance, "10. Provenance Is Not a Universal Schema")


def test_p2_temporal_terms_stay_separate_and_unqualified_lineage_is_retired():
    """Row 049 ``Val``; 049 §5, §7; RMS §18; 054 §6."""
    assert "six terms separated" in _val_of("049")
    terms = _artifact("049")
    assert _section(terms, "5. The Six Terms")
    assert _says(terms, "The unqualified word is retired.")
    assert _says(_read(RMS), "Unqualified lineage is retired")
    assert _section(
        _artifact("054"), "6. Universal Obligation vs Model-Owned Mechanism"
    )


def test_p2_package_composition_is_model_owned_and_world_package_is_worlds():
    """Row 056 ``Done``; 056 §4, §7, §13 — the World package is not universal."""
    assert _field("056", "Done", "Why") == "no universal package"
    package = _artifact("056")
    assert _says(
        _section(package, "4. The Governing Package Rule"),
        "No Record Model package composition is universal",
    )
    assert _section(package, "7. World's Established Package")
    anti_pattern = _section(package, "13. The Central Anti-Pattern")
    assert _says(
        anti_pattern,
        "✗ World has Record + Relationship Record + History "
        "Record → therefore E, P, R, V, I have",
    ), "056 no longer names the World-package-for-all anti-pattern as invalid"


def test_p2_record_is_not_canon_and_authority_is_domain_scoped():
    """RMS §17; row 051 ``Val``; 052 §4."""
    assert _says(_read(RMS), "Record ≠ Canon. All authority is domain-scoped.")
    assert _val_of("051") == "authority domain-scoped; Record ≠ Canon"
    assert _says(_artifact("051"), "All authority is domain-scoped.")
    assert _section(_artifact("052"), "4. Record ≠ Canon")


def test_p2_kind_admission_boundary_is_intact():
    """RMS §13's fourteen questions carried whole by 057; classification ≠ admission.

    The fourteen include *why not a field / state / relationship / projection /
    Registry definition*, so the category boundaries are checked as the RMS
    states them rather than restated here.
    """
    rms = _section(_read(RMS), "13. Kind Architecture")
    questions = re.search(r"every Kind must answer:(.*?)\n", rms)
    assert questions, "RMS §13 no longer states the Kind Admission Test"
    frozen = [_flat(q).rstrip(".") for q in questions.group(1).split("·")]

    table = _section(_artifact("057"), "5.1 The fourteen questions")
    carried = re.findall(r"^\| \d+ \| (.+?) \|$", table, re.MULTILINE)
    assert carried == frozen, (
        f"057 §5.1 no longer carries RMS §13's test.\n  RMS: {frozen}\n  057: {carried}"
    )
    assert _says(_artifact("057"), "FIELD → KIND → STATUS → STRUCTURE")
    assert _says(_artifact("044"), "Classification here is not admission.")


# ---------------------------------------------------------------------------
# Supporting conformance — Artifact 058, consumed and not replaced
# ---------------------------------------------------------------------------


def test_p2_cross_model_resolution_is_not_legality():
    """058 §5, §6. A resolvable ID is the handle; resolving is not permission."""
    cross = _artifact("058")
    assert _says(
        _section(cross, "6. The Cross-Model Handle"),
        "A resolvable ID is the only legal cross-model handle",
    )
    assert _says(cross, "Resolving is not permission.")
    assert _says(
        _section(cross, "5. Dependency Authority"), "legality is model/Registry-owned"
    )


def test_p2_cross_model_reference_transfers_no_ownership():
    """058 §12 agrees with 045 §9: a reference moves nothing."""
    assert _says(_artifact("058"), "An edge transfers nothing.")
    assert _says(_artifact("045"), "a reference DOES NOT TRANSFER OWNERSHIP")


def test_p2_cross_model_publication_firewall_and_registry_boundary_hold():
    """058 §8.1, §11, §12 — Spine law 5, manifestation-blindness, RMS §10.3."""
    cross = _artifact("058")
    assert _says(
        cross, "They reference canon one-directionally; they never become canon."
    )
    assert _says(
        _section(cross, "11. Registry Boundary"), "R → domain instances = FORBIDDEN."
    )
    matrix = _section(cross, "8.1 Edges stated by the sources")
    assert re.search(
        r"^\| \*\*W\*\* \| \*\*I\*\* \|[^\n]*\| FORBIDDEN \|", matrix, re.MULTILINE
    ), "058 no longer forbids W → I (manifestation-blindness)"


def test_p2_w_to_v_conflict_is_recorded_and_not_arbitrated_here():
    """058 records W → V as an unresolved source conflict. This suite neither
    allows nor forbids it: it checks that 058 records it honestly, claims no
    authority to decide it, and binds no condition on it."""
    cross = _artifact("058")
    matrix = _section(cross, "8.1 Edges stated by the sources")
    row = re.search(r"^\| \*\*W\*\* \| \*\*V\*\* \|.*$", matrix, re.MULTILINE)
    assert row and "UNRESOLVED SOURCE CONFLICT" in row.group(0), (
        "058 no longer records W → V as an unresolved source conflict"
    )
    conflict = _section(cross, "8.3 W → V")
    assert _says(conflict, "Source A") and _says(conflict, "Source B")
    assert _says(conflict, "Artifact 058 has no authority to resolve it")

    conditions = _section(cross, "16. Conformance Conditions")
    bound = [
        line
        for line in conditions.splitlines()
        if line.startswith("| **C-058-") and "W → V" in line
    ]
    assert not bound, f"a 058 condition now binds W → V as settled: {bound}"


def test_p2_deliverable_j_identity_is_left_open():
    """058 §1: the sources neither establish nor exclude 058 = Deliverable J.
    This suite asserts only that 058 says so, and settles nothing itself."""
    assert _says(
        _artifact("058"),
        "The sources therefore do not establish that 058 is "
        "Deliverable J, and do not establish that it is not.",
    )


# ---------------------------------------------------------------------------
# The suite's own boundary — PROOF, not ARCH
# ---------------------------------------------------------------------------


def test_p2_hard_dependencies_exist_where_the_roadmap_places_them():
    """``H: 039–058``. A gate over absent artifacts proves nothing."""
    dependencies = _dependencies()
    assert dependencies[0] == "039" and dependencies[-1] == "058"
    for number in dependencies:
        _artifact_files(number)


def _module_tree() -> ast.Module:
    return ast.parse(Path(__file__).read_text(encoding="utf-8"))


def test_p2_the_suite_is_proof_and_owns_no_rule_it_checks():
    """Row 059 is ``R: PROOF`` · ``SoT: DEV-ENV``. The suite imports nothing from
    ``coolboy12`` and holds no roster of models, prohibitions or questions: every
    such list is parsed from the governing source when a check runs."""
    assert _field("059", "R", "SoT") == "PROOF"
    assert _field("059", "SoT", "Auth") == "DEV-ENV"

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
    assert imported <= {"__future__", "ast", "re", "pathlib"}, (
        f"the suite imports past a static proof: {sorted(imported)}"
    )

    def strings(node: ast.AST) -> int:
        if isinstance(node, ast.Dict):
            elements = [*node.keys, *node.values]
        elif isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            elements = node.elts
        else:
            return 0
        return sum(
            isinstance(e, ast.Constant) and isinstance(e.value, str) for e in elements
        )

    # A literal collection of six or more strings is the shape a copied roster
    # takes — six models, nine prohibitions, fourteen questions. Scoped to
    # literals at their own level; it is a guard, not a proof of intent.
    rosters = [node.lineno for node in ast.walk(tree) if strings(node) >= 6]
    assert not rosters, f"the suite holds its own roster at lines {rosters}"


def test_p2_regression_scan_catches_a_planted_contrary_claim():
    """The scan is only worth its green if it can go red."""
    pattern = _prohibited_pattern()
    planted = "## 3. Scope\n\nEvery Record Model shares a universal lifecycle.\n"
    assert _unnegated(planted, pattern), "the scan missed a positive universal claim"
    negated = "## 3. Scope\n\nNo Record Model shares a universal lifecycle.\n"
    assert not _unnegated(negated, pattern), "the scan flagged a negated statement"
    listed = "## 3. Scope\n\nWorld MUST NOT be treated as:\n\n- a universal template;\n"
    assert not _unnegated(listed, re.compile("template")), (
        "the scan lost a list item's negating lead-in"
    )
    template = "## 3. Scope\n\nWorld is the template for every model.\n"
    assert _unnegated(template, re.compile(r"\btemplate\b")), (
        "the scan missed World made a template"
    )


def _scan(sentence: str) -> list[str]:
    """The scan applied to one sentence set in an ordinary section."""
    return _unnegated(f"## 3. Scope\n\n{sentence}\n", _prohibited_pattern())


# Each case pairs a prohibited universal with a clause that is negative or
# qualified but says nothing against it — the false-negative paths of a
# sentence-wide negation test.
ADVERSARIAL_CASES = (
    (
        "universal lifecycle + unrelated negation",
        "All Record Models share a universal lifecycle, but no universal History "
        "Record exists.",
    ),
    (
        "universal canonicality + unless",
        "All Records share universal canonicality unless otherwise specified.",
    ),
    ("universal Record schema", "Every model uses one universal Record schema."),
    (
        "universal identity semantics",
        "All six Record Models share universal identity semantics.",
    ),
    (
        "universal state model + unrelated negation",
        "Every model shares one universal state model, but no model may bypass "
        "validation.",
    ),
    (
        "universal Kind taxonomy + unrelated clause",
        "Every model uses one universal Kind taxonomy, although no model owns another.",
    ),
    (
        "universal canonicality + although",
        "Universal canonicality applies to every Record, although publication "
        "never creates World canon.",
    ),
)

# Each control negates the prohibited claim itself, and must stay clean.
NEGATIVE_CONTROLS = (
    ("no universal lifecycle", "There is no universal lifecycle."),
    ("prohibited canonicality", "Universal canonicality is prohibited."),
    ("no Record schema", "No universal Record schema is permitted."),
    (
        "grammar is not semantics",
        "Universal identity grammar does not create universal identity semantics.",
    ),
    ("no state model", "The architecture has no universal state model."),
    (
        "no Kind taxonomy",
        "No universal Kind taxonomy exists; each model owns its own.",
    ),
    ("not permitted", "A universal lifecycle is not permitted."),
    (
        "no model inherits",
        "No Record Model inherits a universal canonicality model.",
    ),
)


def test_p2_scan_finds_a_prohibited_universal_beside_an_unrelated_negation():
    """Negation governs its own clause, and ``unless`` qualifies a universal
    without denying it. Every case here must be caught."""
    missed = [name for name, sentence in ADVERSARIAL_CASES if not _scan(sentence)]
    assert not missed, f"the scan let a prohibited universal pass: {missed}"


def test_p2_scan_accepts_a_prohibited_universal_that_is_negated():
    """The same scan must not flag a claim its own clause negates."""
    flagged = [
        f"{name}: {_scan(sentence)}"
        for name, sentence in NEGATIVE_CONTROLS
        if _scan(sentence)
    ]
    assert not flagged, f"the scan flagged a negated statement: {flagged}"


def test_p2_identity_grammar_is_universal_and_identity_semantics_is_not():
    """RMS §5: *UNIVERSAL IDENTITY GRAMMAR ≠ UNIVERSAL SEMANTIC MODEL*.

    Sharing the grammar is the architecture and must pass; sharing identity
    semantics is the prohibition and must fail — under RMS §4's label or the
    Blueprint's wording alike."""
    grammar = _read(RMS).split("`FROZEN` (AD-1, §13.9a, I-82): **`", 1)[1]
    grammar = grammar.split("`", 1)[0]
    assert grammar.startswith("[PARTITION]-"), "RMS §5 lost its identity grammar"
    assert not _scan(
        f"All six Record Models share the universal identity grammar {grammar}."
    ), "the scan flagged the universal grammar itself"
    for claim in (
        "All six Record Models share universal identity semantics.",
        "All six Record Models share a universal identity composition.",
        "The grammar gives all six a universal Record semantics.",
    ):
        assert _scan(claim), f"the scan missed a universal identity semantics: {claim}"


def test_p2_every_val_clause_is_independently_gated():
    """Break one clause and the gate names that clause."""
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
                test_exit_p2_gate_covers_its_val_and_carries_no_unresolved_check()
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


def test_p2_the_gate_is_deterministic():
    """The same repository, the same verdict — and the mapping follows row 059."""
    before = dict(VAL_CLAUSES)
    for _ in range(3):
        test_exit_p2_gate_covers_its_val_and_carries_no_unresolved_check()
    assert VAL_CLAUSES == before, "the gate mutated its own clause mapping"

    stated = [c.strip() for c in _val_of("059").split(";") if c.strip()]
    assert list(VAL_CLAUSES) == stated, (
        f"the gate's clause order no longer follows row 059's Val.\n"
        f"  row 059: {stated}\n  gate: {list(VAL_CLAUSES)}"
    )
