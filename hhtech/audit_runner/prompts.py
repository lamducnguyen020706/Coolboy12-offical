"""Prompt construction for the two HHTECH calls: audit, and patch-prompt
generation. BUILD spec §7, §14, §19.

Every source file included in the request is wrapped in a labeled block so
nothing is sent unlabeled:

    ===== FILE: <path> =====
    ...
    ===== END FILE =====
"""

from __future__ import annotations

from .gitstate import GitState
from .roadmap import ManifestRow, TargetScope
from .sources import SourceBundle

_FILE_OPEN = "===== FILE: {path} ====="
_FILE_CLOSE = "===== END FILE ====="


def _file_block(path: str, content: str) -> str:
    return f"{_FILE_OPEN.format(path=path)}\n{content}\n{_FILE_CLOSE}\n"


def _missing_block(path: str, note: str) -> str:
    return f"{_FILE_OPEN.format(path=path)}\n[{note}]\n{_FILE_CLOSE}\n"


AUDIT_SYSTEM_PROMPT = """\
You are GPT-5.6 Luna acting as the COOLBOY12 independent auditor.

You are NOT the implementation agent.

You MUST follow hhtech/standards/audit-standard.md exactly.

You MUST NOT invent architectural requirements. You MUST NOT use your own
preference as a requirement.

Blueprint + RMS are the primary architectural authority. The Roadmap defines
build decomposition and the target artifact's declared contract. The target
artifact's own current content is Tier 4. Git state is factual evidence
only, never architecture.

audit-standard.md and patch-standard.md are HHTECH-internal *procedure*
documents, not architectural authority — they govern how you conduct the
audit, not what is architecturally true. Where they and the Blueprint/RMS/
Roadmap would ever disagree, the Blueprint/RMS/Roadmap are right.

Perform the required audit passes. Perform full requirement traceability.
Perform Diff Audit / Regression Analysis as required. Check unexpected
scope expansion, comparing the actual changed files against the target's
Roadmap-declared scope. Do not silently ignore unrelated changes.

Every finding must:
- have a stable ID (AUD-<artifact>-<NN>);
- have a severity assigned per audit-standard.md §9 — never invented;
- cite an authoritative requirement;
- identify evidence;
- identify the affected location;
- give a remediation direction where determinable;
- include a validation condition.

If evidence is insufficient, do not invent a finding. If a requirement is
unavailable, classify it according to audit-standard.md (UNVERIFIABLE is
never PASS). The final verdict MUST follow audit-standard.md §13 exactly.

Do not tell yourself to "find something wrong." Do not bias toward PATCH
REQUIRED. Do not bias toward PASS. The audit must be genuinely independent.

Your response MUST be the complete contents of hhtech/auditreport.md,
following audit-standard.md's own report contract (§14.1): Audit Identity,
Target Artifact, Audit Mode, Source Set, Scope, Executive Verdict,
Requirement Coverage, Findings, Evidence, Regression Analysis, Diff
Analysis, Unverifiable Items, False-Positive Checks, Final Verdict,
Re-Audit Requirements.

Your response MUST end with exactly one line, at the very end, in this
exact form and no other:

VERDICT: PASS
VERDICT: PATCH REQUIRED
VERDICT: BLOCKED

Exactly one such line. Do not include more than one candidate verdict line.
Do not put explanatory text after it.
"""

PATCH_PROMPT_SYSTEM_PROMPT = """\
You are generating an artifact-specific implementation prompt for Claude
Code.

You are NOT the implementation agent. You are producing the instructions
the implementation agent will follow.

You MUST use hhtech/standards/patch-standard.md. You MUST NOT invent
requirements. You MUST NOT change the Blueprint, RMS, Roadmap, or either
HHTECH standard. You MUST independently validate the findings in the
supplied audit report are still supported by the supplied source content
before writing any instruction that depends on them — do not generate a
prompt for a false finding.

Use audit-standard.md's vocabulary exactly. Respect patch-standard.md's
severity and scope rules exactly: severity is whatever audit-standard.md
already assigned in the supplied audit report; you do not promote, demote,
or invent a severity, and a P2 is blocking only if the audit report itself
did not downgrade it to INFO. Do not expand scope merely because another
change would be convenient. Every changed location not directly named by a
finding must carry an explicit necessary-consequence chain (Finding ID ->
direct correction -> necessary consequence -> additional changed location
-> validation) with every link stated.

The generated prompt must tell Claude Code exactly: the task, the target
artifact, the audit verdict, the confirmed findings, finding-by-finding
remediation, the exact target files, the scope boundary, the authority
constraints, what must NOT be changed, implementation requirements,
necessary-consequence rules, validation requirements, negative/regression
checks, diff verification, completion criteria, and re-audit handoff. It
must be actionable without the runner explaining anything further.

It must NOT contain: a reference to a file named patchreport.md, session or
runner instructions, any API credential, invented architecture, or
unrelated cleanup.

Your response MUST be the complete contents of hhtech/patchprompt.md, and
nothing else — no commentary before or after it.
"""


def build_audit_user_content(
    artifact_id: str,
    row: ManifestRow,
    scope: TargetScope,
    sources: SourceBundle,
    git: GitState,
    dependency_context: dict[str, str],
) -> str:
    parts: list[str] = []

    parts.append("## PROJECT AUTHORITY\n")
    parts.append(
        "Blueprint + RMS are joint primary architectural authority. Roadmap "
        "is build decomposition and this artifact's declared contract. The "
        "target artifact is Tier 4. Git state is Tier 5, factual evidence "
        "only. audit-standard.md and patch-standard.md are HHTECH audit/"
        "patch *procedure*, not architectural authority.\n"
    )

    parts.append("## AUDIT STANDARD\n")
    parts.append(_file_block("hhtech/standards/audit-standard.md", sources.audit_standard))

    parts.append("## PATCH STANDARD (for context on what a later patch would need)\n")
    parts.append(_file_block("hhtech/standards/patch-standard.md", sources.patch_standard))

    parts.append("## BLUEPRINT CONTEXT\n")
    if sources.blueprint_sections:
        for section in sources.blueprint_sections:
            if section.found:
                parts.append(_file_block(f"Blueprint §{section.citation}", section.body))
            else:
                parts.append(_missing_block(
                    f"Blueprint §{section.citation}",
                    "SOURCE SECTION NOT LOCATED — do not assume its content",
                ))
    else:
        parts.append("[no BP citation on this artifact's manifest row]\n")

    parts.append("## RMS CONTEXT\n")
    if sources.rms_sections:
        for section in sources.rms_sections:
            if section.found:
                parts.append(_file_block(f"RMS §{section.citation}", section.body))
            else:
                parts.append(_missing_block(
                    f"RMS §{section.citation}",
                    "SOURCE SECTION NOT LOCATED — do not assume its content",
                ))
    else:
        parts.append("[no RMS citation on this artifact's manifest row]\n")

    parts.append("## ROADMAP CONTEXT\n")
    parts.append(_file_block(f"Roadmap manifest row for artifact {artifact_id}", row.raw))
    parts.append(
        f"\nDeclared scope descriptor: `{scope.declared_path}` "
        f"(glob={scope.is_glob}, directory={scope.is_directory})\n"
        f"Files currently matching that declared scope "
        f"({len(scope.matched_files)}):\n"
        + "".join(f"  - {p}\n" for p in scope.matched_files)
        + ("  (none exist yet)\n" if not scope.matched_files else "")
    )

    if dependency_context:
        parts.append("\n## HARD-DEPENDENCY CONTEXT (H) — existence/state only, not full-audited\n")
        for dep_id, dep_raw in dependency_context.items():
            parts.append(_file_block(f"Roadmap manifest row for H-dependency {dep_id}", dep_raw))

    parts.append("## TARGET ARTIFACT CONTENT\n")
    for path, content in sources.target_files.items():
        if content is None:
            parts.append(_missing_block(path, "FILE DOES NOT EXIST ON DISK"))
        else:
            parts.append(_file_block(path, content))

    parts.append("## GIT STATE\n")
    parts.append(f"Branch: {git.branch}\nHEAD: {git.head}\n")
    parts.append(_file_block("git status --short", git.status_short or "(clean)"))
    parts.append(_file_block("git diff --name-status", git.diff_name_status or "(empty)"))
    parts.append(_file_block("git diff --stat", git.diff_stat or "(empty)"))
    if git.untracked:
        parts.append(_file_block("untracked files", "\n".join(git.untracked)))

    parts.append("## GIT DIFF\n")
    parts.append(_file_block("git diff", git.diff or "(empty — new or unchanged artifact)"))

    if sources.unavailable:
        parts.append("## SOURCE-READ EVIDENCE — GAPS\n")
        parts.append(
            "The following cited sections could not be located and were "
            "NOT supplied. Do not treat them as read or as available:\n"
            + "".join(f"  - {c}\n" for c in sources.unavailable)
        )

    parts.append("## TASK\n")
    parts.append(
        f"Perform a Full Artifact Audit of Artifact {artifact_id} "
        f"(`{row.name}`) under hhtech/standards/audit-standard.md.\n"
    )

    parts.append("## OUTPUT CONTRACT\n")
    parts.append(
        "Return the complete contents of hhtech/auditreport.md per "
        "audit-standard.md §14.1, ending with exactly one "
        "`VERDICT: PASS` / `VERDICT: PATCH REQUIRED` / `VERDICT: BLOCKED` line.\n"
    )

    return "\n".join(parts)


def build_patch_prompt_user_content(
    artifact_id: str,
    row: ManifestRow,
    scope: TargetScope,
    sources: SourceBundle,
    git: GitState,
    audit_report: str,
) -> str:
    parts: list[str] = []

    parts.append("## PROJECT AUTHORITY\n")
    parts.append(
        "Same hierarchy as the audit call: Blueprint + RMS joint primary "
        "authority, Roadmap next, target artifact Tier 4, git state Tier 5 "
        "fact-only. patch-standard.md is procedure, not architecture.\n"
    )

    parts.append("## AUDIT STANDARD\n")
    parts.append(_file_block("hhtech/standards/audit-standard.md", sources.audit_standard))

    parts.append("## PATCH STANDARD\n")
    parts.append(_file_block("hhtech/standards/patch-standard.md", sources.patch_standard))

    parts.append("## AUDIT REPORT (this call's confirmed-findings input)\n")
    parts.append(_file_block("hhtech/auditreport.md", audit_report))

    parts.append("## BLUEPRINT CONTEXT\n")
    for section in sources.blueprint_sections:
        if section.found:
            parts.append(_file_block(f"Blueprint §{section.citation}", section.body))

    parts.append("## RMS CONTEXT\n")
    for section in sources.rms_sections:
        if section.found:
            parts.append(_file_block(f"RMS §{section.citation}", section.body))

    parts.append("## ROADMAP CONTEXT\n")
    parts.append(_file_block(f"Roadmap manifest row for artifact {artifact_id}", row.raw))
    parts.append(
        f"\nDeclared scope: `{scope.declared_path}`; "
        f"files currently in scope: {', '.join(scope.matched_files) or '(none)'}\n"
    )

    parts.append("## TARGET ARTIFACT CONTENT\n")
    for path, content in sources.target_files.items():
        if content is None:
            parts.append(_missing_block(path, "FILE DOES NOT EXIST ON DISK"))
        else:
            parts.append(_file_block(path, content))

    parts.append("## GIT STATE\n")
    parts.append(f"Branch: {git.branch}\nHEAD: {git.head}\n")
    parts.append(_file_block("git status --short", git.status_short or "(clean)"))

    parts.append("## GIT DIFF\n")
    parts.append(_file_block("git diff", git.diff or "(empty)"))

    parts.append("## TASK\n")
    parts.append(
        f"The audit above returned VERDICT: PATCH REQUIRED for Artifact "
        f"{artifact_id} (`{row.name}`). Generate the complete contents of "
        f"hhtech/patchprompt.md: a self-contained Claude Code execution "
        f"prompt that resolves the confirmed findings under "
        f"patch-standard.md.\n"
    )

    parts.append("## OUTPUT CONTRACT\n")
    parts.append(
        "Return only the complete contents of hhtech/patchprompt.md. No "
        "commentary before or after it.\n"
    )

    return "\n".join(parts)
