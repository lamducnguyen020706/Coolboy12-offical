"""Prompt construction for the two HHTECH calls: audit, and patch prompt.

Every supplied source is wrapped in a labelled block so nothing reaches the
model unlabelled and nothing loses its document identity:

    ===== SOURCE: Blueprint §10 | path: docs/sources/… | status: AVAILABLE =====
    …
    ===== END SOURCE: Blueprint §10 =====

A source recorded UNAVAILABLE is still shown — as an explicit absence, so
the auditor can neither assume its content nor claim to have read it.
"""

from __future__ import annotations

from .gitstate import GitState
from .sources import (
    STATUS_AVAILABLE,
    AuditScope,
    ResolutionResult,
    ResolvedSource,
)

MAX_BASELINE_DIFF = 20_000


def _source_block(source: ResolvedSource) -> str:
    header = (
        f"===== SOURCE: {source.label} | path: {source.path or 'n/a'}"
        f" | status: {source.status} ====="
    )
    if source.status == STATUS_AVAILABLE:
        body = source.content
    else:
        body = f"[NOT SUPPLIED — {source.status}: {source.detail or 'no detail recorded'}]"
    return f"{header}\n{body}\n===== END SOURCE: {source.label} =====\n"


def _block(label: str, body: str) -> str:
    return f"===== {label} =====\n{body}\n===== END {label} =====\n"


AUDIT_SYSTEM_PROMPT = """\
You are GPT-5.6 Luna acting as the COOLBOY12 independent auditor.

You are NOT the implementation agent. You do not patch anything.

You MUST follow hhtech/standards/audit-standard.md exactly. It is supplied
in full in this request.

AUTHORITY
Tier 1 Master Blueprint and Tier 2 Record Model System are JOINT primary
architectural authority — neither outranks the other. Tier 3 the Roadmap
governs build decomposition, order, dependency, gates and the target's
declared scope, and is subordinate to Tiers 1-2. Tier 4 the target artifact
never outranks Tiers 1-3. Tier 5 git/repository state is factual evidence of
what exists and what changed; it is NEVER evidence of architectural truth.
audit-standard.md and patch-standard.md govern PROCEDURE only and are never
architectural authority.

SOURCE SET vs AUDIT SCOPE — do not confuse these.
The SOURCE SET is what you were given to read. The AUDIT SCOPE is what is
being judged. A dependency, neighbour or conformance artifact appears in the
Source Set as CONTEXT ONLY. You MUST NOT audit it, report findings against
it, or treat it as a second target. Findings may only be raised against the
declared AUDIT SCOPE of the stated target artifact.

WHAT YOU MAY TREAT AS READ
Only the blocks supplied in this request with status AVAILABLE. A block
marked UNAVAILABLE, NOT APPLICABLE or NOT REQUIRED was NOT supplied: you
must not reconstruct it from memory, infer its content, or state that you
read it. If a mandatory condition depends on a source that was not supplied,
that condition is UNVERIFIABLE and, if it is blocking under
audit-standard.md §8.2/§13, the verdict is BLOCKED — never PASS.

Do not invent a requirement. Do not invent architecture. Do not invent an
invariant's wording. Do not manufacture the text of a requirement register
that was reported unavailable. Preserve requirement IDs exactly.

SOURCE CONFLICT
If authoritative sources genuinely conflict, do not silently pick one.
Name both documents and both exact sections, apply documented precedence
only where the project explicitly defines it, and otherwise record the
conflict per audit-standard.md §1.6 and fail closed as that section requires.

PASSES
Run the fourteen mandatory passes of audit-standard.md §6, in order, each
independently. Apply §6.2 requirement discovery: the declared citations are a
FLOOR, not a ceiling. Apply the §10 False-Positive Control checklist to every
candidate finding before you write it, and report in the False-Positive
Checks section which suspicions you downgraded.

Every finding MUST carry: a stable ID `AUD-<artifact>-<NN>` (§14.2), a
severity assigned per §9 — never invented, never inflated, an authoritative
requirement citation, evidence, the affected location, a remediation
direction where determinable, and a validation condition.

Do NOT claim that all passes passed when some were UNVERIFIABLE. Report each
pass honestly as PASS, FAILED, UNVERIFIABLE, NOT APPLICABLE or BLOCKED per
audit-standard.md's own semantics. An UNVERIFIABLE row is never PASS.

VERDICT
Apply audit-standard.md §13's decision procedure exactly:
- BLOCKED when a mandatory condition's compliance cannot be determined at
  all — including when a required source was not supplied to you.
- PATCH REQUIRED when the audit completed and an unresolved P0, P1 or
  blocking-classified P2 finding remains.
- PASS only when coverage is demonstrably full and no such finding remains.
Do not downgrade a defect to force PASS. Do not promote an INFO observation
to force PATCH REQUIRED.

OUTPUT CONTRACT
Your response MUST be the complete contents of hhtech/auditreport.md and
nothing else — no preamble, no commentary. It MUST contain all fifteen
sections of audit-standard.md §14.1, in order, each as a markdown heading:

  1. Audit Identity
  2. Target Artifact
  3. Audit Mode
  4. Source Set
  5. Scope
  6. Executive Verdict
  7. Requirement Coverage
  8. Findings
  9. Evidence
  10. Regression Analysis
  11. Diff Analysis
  12. Unverifiable Items
  13. False-Positive Checks
  14. Final Verdict
  15. Re-Audit Requirements

The Source Set section MUST list what you were actually supplied, using the
labels given in this request, and MUST distinguish supplied from not
supplied. Do not claim a section was read if it was not supplied.

The VERY LAST line of your response MUST be exactly one of:

VERDICT: PASS
VERDICT: PATCH REQUIRED
VERDICT: BLOCKED

That terminal line is the machine-read verdict. Do NOT write any other line
anywhere in the report that consists solely of `VERDICT: <value>` — refer to
a verdict in prose instead (for example "the verdict is PASS"). Nothing may
follow the terminal line.
"""


PATCH_PROMPT_SYSTEM_PROMPT = """\
You are generating hhtech/patchprompt.md — the execution prompt a Claude Code
implementation agent will follow next.

You are NOT the implementation agent, and you are NOT the auditor. You do not
re-run the audit and you do not overturn its verdict.

You MUST follow hhtech/standards/patch-standard.md, supplied in full. You
MUST NOT invent requirements, invent architecture, or modify the Blueprint,
the RMS, the Roadmap, or either HHTECH standard.

A patchprompt is an EXECUTION PROMPT, not a second audit report. Do not
reproduce the audit report. State the target, the verdict, the authority
constraints, what is allowed, what is forbidden, the required steps, the
validation, and the re-audit handoff.

The verdict decides which of three contracts you write — they are defined in
patch-standard.md §33, supplied below. Follow exactly the one named in the
TASK block, and no other.

CONTRACT A — verdict PATCH REQUIRED
Write actionable, minimal, source-grounded patch instructions:
- the artifact ID and its exact declared target scope;
- each confirmed finding by its audit ID, with the requirement it cites, the
  evidence, and a remediation direction;
- severity exactly as the audit assigned it — you never promote, demote or
  invent severity, and a P2 is blocking only if the audit classified it so;
- the minimal change rule (§8) and the preservation rule (§9): change only
  what a finding requires, preserve everything already compliant;
- authority protection (§10): the patch agent may NOT edit the Blueprint,
  RMS, Roadmap or standards to make the audit pass;
- traceability (§11): every changed location traces
  `Finding ID -> correction -> necessary consequence -> changed location ->
  validation`, with each link stated. Unrelated cleanup is forbidden.
- the eight-step sequence of patch-standard.md §21:
  READ -> VALIDATE -> PLAN -> PATCH -> TEST -> INSPECT DIFF -> SELF-AUDIT ->
  HAND OFF FOR RE-AUDIT;
- validation and negative/regression checks, diff inspection, completion
  criteria, and the handoff instruction to re-run `./hhtech/audit <ID>`.
The prompt must state plainly that a patch is required. It must NOT contain
the phrase "NO PATCH REQUIRED".

CONTRACT B — verdict PASS
Write a short prompt that forbids patching. It MUST:
- state `NO PATCH REQUIRED` explicitly;
- instruct the implementation agent NOT to modify the target artifact;
- forbid inventing a patch, and forbid weakening any source requirement to
  create work;
- state that the audit completed with PASS and the next operation is no
  artifact patch;
- note that re-running `./hhtech/audit <ID>` is how a later re-audit happens.
It MUST NOT contain remediation instructions or findings to fix.

CONTRACT C — verdict BLOCKED
Write a prompt that forbids patching the artifact to clear the block. It MUST:
- state `DO NOT PATCH` explicitly;
- state the exact reason the audit is BLOCKED;
- list each unavailable or unresolved evidence source by the label the audit
  report used;
- distinguish clearly between an audit-context/source-resolution gap and an
  actual artifact defect, and say which this is;
- state exactly what evidence or context must become available;
- require re-running `./hhtech/audit <ID>` once it is available;
- forbid modifying the target artifact merely to turn BLOCKED into PASS;
- forbid inventing source content or weakening requirements.
It MUST NOT contain a remediation plan for the target artifact and MUST NOT
contain the phrase "NO PATCH REQUIRED".

FORBIDDEN IN ALL THREE
Any reference to a file named patchreport.md — patch-standard.md §20 defines
a patch RESULT schema, not a repository file, and no such file is ever
created. Any API credential. Any instruction to edit the Blueprint, RMS,
Roadmap, audit-standard.md or patch-standard.md. Any invented requirement.
Any unrelated cleanup. Any instruction to run a second audit yourself.

Your response MUST be the complete contents of hhtech/patchprompt.md and
nothing else — no commentary before or after it.
"""


def _render_source_set(result: ResolutionResult) -> str:
    lines = ["The auditor was supplied exactly the following. Nothing else was read.\n"]
    lines.append("| # | Source label | Path | Section | Status | Why loaded |")
    lines.append("|---|---|---|---|---|---|")
    for index, source in enumerate(result.source_set.entries, start=1):
        lines.append(
            f"| {index} | {source.label} | {source.path or 'n/a'} | "
            f"{source.section or 'n/a'} | {source.status} | {source.reason} |"
        )
    return "\n".join(lines)


def _render_scope(scope: AuditScope) -> str:
    lines = [
        f"Artifact ID:      {scope.artifact_id}",
        f"Artifact name:    {scope.artifact_name}",
        f"Declared path:    {scope.declared_path}",
        f"Scope kind:       {scope.kind}",
        (
            f"Multi-file entry: {scope.multi_file} "
            "(Roadmap RULE G3: many files may be one artifact)"
        ),
        "",
        "Files in the declared AUDIT SCOPE:",
    ]
    for scoped in scope.files:
        state = "present" if scoped.exists else "DECLARED BUT NOT PRESENT ON DISK"
        lines.append(f"  - {scoped.path} — {state}")
    if not scope.files:
        lines.append("  (none resolved)")
    lines.append("")
    lines.append(
        "Findings may be raised ONLY against these paths. Every other source "
        "in this request is context."
    )
    return "\n".join(lines)


def _render_dependencies(result: ResolutionResult) -> str:
    lines = [
        (
            "Dependency and unlock fields from the target's Roadmap row, with the "
            "semantics each field carries. These are CONTEXT, not audit targets.\n"
        )
    ]
    for entry in result.dependency_context:
        declared = entry["declared"] or "—"
        lines.append(f"{entry['field']}: {declared}")
        lines.append(f"    meaning: {entry['semantics']}")
        if entry["empty"]:
            lines.append("    resolved: nothing declared")
        else:
            if entry["artifact_ids"]:
                lines.append(f"    artifact IDs: {', '.join(entry['artifact_ids'])}")
            if entry["non_artifact_tokens"]:
                lines.append(
                    "    non-artifact references (declared, resolved as text): "
                    f"{', '.join(entry['non_artifact_tokens'])}"
                )
        lines.append("")
    return "\n".join(lines)


def _render_references(result: ResolutionResult) -> str:
    refs = result.references
    lines = ["References the target artifact's own text explicitly names:"]
    for name, values in (
        ("Artifacts", refs.artifacts),
        ("Blueprint sections", refs.blueprint_sections),
        ("RMS sections", refs.rms_sections),
        ("Invariants", refs.invariants),
        ("Anti-orderings", refs.anti_orderings),
        ("Requirements", refs.requirements),
        ("Spine laws", refs.spine_laws),
    ):
        lines.append(f"  {name}: {', '.join(values) if values else '(none)'}")
    return "\n".join(lines)


def _render_git(git: GitState) -> str:
    parts = [
        f"Branch: {git.branch}",
        f"HEAD:   {git.head}",
        "",
        _block("git status --short", git.status_short or "(clean)"),
        _block("git diff --name-status (unstaged)", git.diff_name_status or "(empty)"),
        _block("git diff --stat (unstaged)", git.diff_stat or "(empty)"),
        _block("git diff --name-status (staged)", git.staged_name_status or "(empty)"),
    ]
    if git.untracked:
        parts.append(_block("untracked files", "\n".join(git.untracked)))
    return "\n".join(parts)


def _render_baselines(git: GitState) -> str:
    if not git.baselines:
        return "(no target files to baseline)"
    parts: list[str] = []
    for baseline in git.baselines:
        header = (
            f"{baseline.path}: tracked={baseline.tracked} "
            f"on_disk={baseline.exists_on_disk} "
            f"changed_since_HEAD={baseline.changed_since_head}"
        )
        if not baseline.tracked:
            parts.append(
                f"{header}\n  NEW/UNTRACKED — no committed baseline exists; an empty "
                "diff here means a new artifact, not an unchanged one."
            )
            continue
        diff = baseline.diff_vs_head or "(no change against HEAD)"
        if len(diff) > MAX_BASELINE_DIFF:
            diff = (
                diff[:MAX_BASELINE_DIFF]
                + f"\n[TRUNCATED at {MAX_BASELINE_DIFF} bytes — the remainder of this "
                "diff was NOT supplied; do not treat it as read]"
            )
        parts.append(f"{header}\n{_block(f'git diff HEAD -- {baseline.path}', diff)}")
    return "\n".join(parts)


def build_audit_user_content(
    result: ResolutionResult, git: GitState, snapshot=None
) -> str:
    scope = result.scope
    parts: list[str] = []

    parts.append("## TASK\n")
    parts.append(
        f"Perform a Full Artifact Audit (audit-standard.md §5.1) of Artifact "
        f"{scope.artifact_id} — {scope.artifact_name} — under "
        f"hhtech/standards/audit-standard.md.\n"
    )

    if snapshot is not None:
        parts.append("\n## AUDIT SNAPSHOT\n")
        parts.append(
            f"Branch: {snapshot.branch}\n"
            f"Audited HEAD: {snapshot.head}\n\n"
            "The repository was synchronized with its remote before any source "
            "below was read, and every source, diff and status in this request "
            "was read at this one commit. State this branch and commit in the "
            "Audit Identity section of your report.\n"
        )

    parts.append("## AUDIT SCOPE (what is being judged)\n")
    parts.append(_render_scope(scope))

    parts.append("\n## SOURCE SET (what you were given to read)\n")
    parts.append(_render_source_set(result))

    parts.append("\n## DEPENDENCY / UNLOCK CONTEXT\n")
    parts.append(_render_dependencies(result))

    parts.append("## REFERENCE DISCOVERY\n")
    parts.append(_render_references(result))
    parts.append(
        "\nEach reference above was resolved against the repository; the result "
        "is recorded in the Source Set with its status.\n"
    )

    parts.append("## SUPPLIED SOURCES\n")
    for source in result.source_set.entries:
        parts.append(_source_block(source))

    parts.append("## GIT STATE (Tier 5 — fact, never architecture)\n")
    parts.append(_render_git(git))

    parts.append("\n## REGRESSION BASELINE (target files vs their committed state)\n")
    parts.append(_render_baselines(git))

    parts.append("\n## GIT DIFF (working tree, unstaged)\n")
    parts.append(_block("git diff", git.diff or "(empty)"))

    if git.staged_diff.strip():
        parts.append("## GIT DIFF (staged)\n")
        parts.append(_block("git diff --cached", git.staged_diff))

    unavailable = result.source_set.unavailable
    if unavailable:
        parts.append("## SOURCES NOT SUPPLIED\n")
        parts.append(
            "The following were looked for and could NOT be supplied. Do not "
            "treat any of them as read, and do not reconstruct their content:\n"
        )
        for source in unavailable:
            parts.append(f"  - {source.label}: {source.detail}")
        parts.append(
            "\nIf a mandatory condition depends on one of these, that condition is "
            "UNVERIFIABLE, and BLOCKED is the correct verdict where "
            "audit-standard.md §13 requires it.\n"
        )

    parts.append("\n## OUTPUT CONTRACT\n")
    parts.append(
        "Return the complete contents of hhtech/auditreport.md with all fifteen "
        "§14.1 sections, ending with exactly one terminal "
        "`VERDICT: PASS` / `VERDICT: PATCH REQUIRED` / `VERDICT: BLOCKED` line "
        "as the final line, and no bare verdict line anywhere else.\n"
    )

    return "\n".join(parts)


_CONTRACT_BY_VERDICT = {
    "PATCH REQUIRED": (
        "CONTRACT A",
        (
            "Write actionable, minimal, source-grounded patch instructions for the "
            "confirmed findings. Do not include the phrase NO PATCH REQUIRED."
        ),
    ),
    "PASS": (
        "CONTRACT B",
        (
            "The audit PASSED. Write the no-patch prompt: it must state NO PATCH "
            "REQUIRED, forbid modifying the target artifact, and forbid inventing a "
            "patch. Do not include remediation instructions."
        ),
    ),
    "BLOCKED": (
        "CONTRACT C",
        (
            "The audit is BLOCKED. Write the do-not-patch prompt: it must state DO "
            "NOT PATCH, name the exact blocking reason and every unavailable source, "
            "distinguish an audit-context/source gap from an artifact defect, require "
            "the evidence to be resolved and `./hhtech/audit <ID>` re-run, and forbid "
            "patching the artifact to clear the block."
        ),
    ),
}


def build_patch_prompt_user_content(
    result: ResolutionResult, git: GitState, audit_report: str, verdict_value: str
) -> str:
    scope = result.scope
    contract_name, contract_instruction = _CONTRACT_BY_VERDICT[verdict_value]
    parts: list[str] = []

    parts.append("## TASK\n")
    parts.append(
        f"The audit of Artifact {scope.artifact_id} — {scope.artifact_name} — "
        f"returned VERDICT: {verdict_value}.\n\n"
        f"Generate hhtech/patchprompt.md following {contract_name}.\n\n"
        f"{contract_instruction}\n"
    )

    parts.append("## TARGET SCOPE (the only files a patch may touch)\n")
    parts.append(_render_scope(scope))

    parts.append("\n## AUDIT REPORT (the confirmed result you are writing from)\n")
    parts.append(_block("hhtech/auditreport.md", audit_report))

    parts.append("\n## PATCH STANDARD\n")
    patch_standard = next(
        (
            s for s in result.source_set.entries
            if s.label == "hhtech/standards/patch-standard.md"
        ),
        None,
    )
    if patch_standard is not None:
        parts.append(_source_block(patch_standard))

    parts.append("## AUDIT STANDARD (vocabulary and severity semantics)\n")
    audit_standard = next(
        (
            s for s in result.source_set.entries
            if s.label == "hhtech/standards/audit-standard.md"
        ),
        None,
    )
    if audit_standard is not None:
        parts.append(_source_block(audit_standard))

    parts.append("## SOURCE SET SUPPLIED TO THE AUDIT\n")
    parts.append(_render_source_set(result))

    parts.append("\n## CURRENT TARGET CONTENT\n")
    for scoped in scope.files:
        if scoped.exists and scoped.content is not None:
            parts.append(_block(f"FILE: {scoped.path}", scoped.content))
        else:
            parts.append(
                _block(f"FILE: {scoped.path}", "[DECLARED BUT NOT PRESENT ON DISK]")
            )

    parts.append("## GIT STATE\n")
    parts.append(f"Branch: {git.branch}\nHEAD: {git.head}\n")
    parts.append(_block("git status --short", git.status_short or "(clean)"))

    parts.append("\n## OUTPUT CONTRACT\n")
    parts.append(
        f"Return only the complete contents of hhtech/patchprompt.md, written to "
        f"{contract_name} for verdict {verdict_value}. No commentary before or "
        "after it.\n"
    )

    return "\n".join(parts)
