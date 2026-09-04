# Artifact 042 Patch Execution Prompt — PATCH REQUIRED

## Target

A patch is required for **Artifact 042 — Record Model definition**.

The only permitted target file is:

- `docs/constitution/record_model.md`

The declared scope is a single-file artifact (`Scope kind: file`; `Multi-file entry: False`). Do not modify any other file. In particular, leave the existing unrelated changes in `reports/implement-log.json` and `reports/progress.json` untouched and do not include them in the correction.

## Authority and constraints

Read the complete target file and directly read the applicable source requirements before editing:

- Artifact 003, `docs/conventions/artifact_conventions.md`, especially C-1 and its 25-field metadata contract.
- The Roadmap manifest row for Artifact 042, including its exact `Val`, `Done`, and `Why` values.
- The relevant finding and validation condition below.
- Current `git status` and the target-scoped `git diff`.

The Blueprint, Record Model System, Roadmap, `hhtech/standards/audit-standard.md`, and `hhtech/standards/patch-standard.md` are authority sources and must not be edited. Do not change any source requirement, invent RR-06 text, or alter architecture to make the audit pass.

Apply the minimal change rule: change only what the confirmed finding requires. Preserve all content that is already compliant, including the Record Model definition, its nine ownership dimensions, boundaries, dependencies, conformance conditions, citations, and non-goals. Unrelated cleanup, refactoring, formatting churn, wording rewrites, and speculative improvements are forbidden.

## Confirmed finding

### AUD-042-01 — Severity: P2

**Requirement:** Artifact 003 Conformance Requirement C-1 requires:

> “All 25 fields are stated explicitly. None is inherited from a header or a neighbour.”

Artifact 003's metadata contract identifies `Val`, `Done`, and `Why` as three of those required fields.

**Evidence:** The metadata block at the top of `docs/constitution/record_model.md` explicitly states fields through `Risk` and `∥`, but has no explicit `Val:`, `Done:`, or `Why:` entries. The body prose does not satisfy the explicit metadata-field requirement.

**Required correction:** Add explicit, nonblank metadata entries to the target metadata block using the Artifact 042 Roadmap contract values:

```text
Val: what a Record Model owns, enumerated
Done: definition
Why: "the place where X lives" is not a definition
```

Preserve the values exactly as shown. Do not change the architectural definition or rely on body prose as implicit metadata.

The audit assigned this finding **P2**. Preserve that severity; do not promote, demote, or invent another severity classification.

## Traceability

The changed location must have this complete causal chain:

- `AUD-042-01`
- Requirement: Artifact 003 C-1 and the 25-field metadata contract require every field to be explicit.
- Correction: add explicit `Val`, `Done`, and `Why` entries with the exact Roadmap values.
- Necessary consequence: the target's own metadata block becomes complete without changing its substantive definition.
- Changed location: the metadata block at the top of `docs/constitution/record_model.md`.
- Validation: verify all 25 metadata fields are explicitly present and nonblank, and verify the three added values match the Artifact 042 Roadmap row and Artifact 003 vocabularies.

No other changed location is justified. If any additional change appears necessary, stop and report why it is a necessary consequence of `AUD-042-01`; do not make it merely for convenience.

## Required execution sequence

Follow these eight steps in order:

### 1. READ

- Read all of `docs/constitution/record_model.md`.
- Read Artifact 003's explicit 25-field contract and C-1 directly.
- Read the Artifact 042 Roadmap manifest row directly.
- Read the full `AUD-042-01` finding, including its evidence, remediation direction, and validation condition.
- Inspect `git status` and the target-file diff before editing.

### 2. VALIDATE

Independently reproduce the finding by comparing the target metadata block with the source-defined 25-field list and the Artifact 042 Roadmap row.

If the finding is not reproducible, do not patch; report exactly:

`FINDING NOT REPRODUCIBLE`

with the precise reason. If the source contradicts the finding, do not patch; report:

`FINDING CONTRADICTED BY SOURCE`

with the exact source text. If the available evidence is insufficient, do not guess; report:

`INSUFFICIENT EVIDENCE TO VALIDATE FINDING`

Do not fabricate a correction for RR-06. Preserve `Req: RR-06` exactly; its authoritative text remains unavailable and is not to be invented.

### 3. PLAN

Plan the smallest correction: add only the three missing explicit metadata fields to the existing metadata block. Keep the existing field values and ordering intact except where a minimal insertion is required for a clear, source-consistent metadata block.

Do not modify the Blueprint, RMS, Roadmap, either HHTECH standard, or any file outside the declared target scope.

### 4. PATCH

Edit only `docs/constitution/record_model.md`.

Add:

```text
Val: what a Record Model owns, enumerated
Done: definition
Why: "the place where X lives" is not a definition
```

Ensure each field is explicit and nonblank. Do not duplicate or reinterpret these values elsewhere, and do not alter compliant body content.

### 5. TEST

Because Artifact 042 is `T: doc`, do not invent code tests or unrelated test artifacts. Perform proportional structural validation:

- Confirm the target contains all 25 metadata fields required by Artifact 003.
- Confirm every field is explicit and nonblank.
- Confirm `Val`, `Done`, and `Why` exactly match the Artifact 042 Roadmap contract.
- Confirm `Req: RR-06` remains unchanged and no RR-06 text was invented.
- Confirm the nine ownership dimensions, canonicality qualifier, model boundaries, dependency declarations, and conformance conditions remain present and unchanged in substance.
- Confirm no refusal, boundary, or negative architectural statement was weakened or removed.
- Confirm no new requirement or architectural claim was introduced.

No negative test is applicable to adding documentation metadata; nevertheless, verify that the patch has not loosened the artifact's existing negative boundaries against a universal model, inheritance, a seventh model, or mechanism-as-semantics.

### 6. INSPECT DIFF

Inspect:

- `git status`
- `git diff -- docs/constitution/record_model.md`
- `git diff --check`

The final target diff must contain only the justified addition of `Val`, `Done`, and `Why` in `docs/constitution/record_model.md`.

Remove any unrelated hunk, formatting churn, temporary file, generated file, or out-of-scope modification. Do not reset, edit, or otherwise disturb the existing unrelated changes in `reports/implement-log.json` and `reports/progress.json`.

### 7. SELF-AUDIT

Walk the completed work through:

`Finding -> changed file -> changed hunk -> validation -> regression checks -> scope check -> authority check`

Confirm:

- `AUD-042-01` is addressed and no other finding was invented.
- The only changed file is the declared target.
- The only changed content is necessary for the finding.
- All previously compliant content remains compliant.
- The authority sources and standards were not modified.
- RR-06 remains preserved exactly without invented content.
- Validation was actually executed and its evidence is available.
- The patch does not claim a permanent PASS; only the independent re-audit may determine the new verdict.

If any completion condition fails, report the patch as incomplete and identify the failed condition.

### 8. HAND OFF FOR RE-AUDIT

Provide the execution result with:

- Artifact ID `042`.
- Patch status: complete or incomplete.
- Finding `AUD-042-01` addressed, or the exact non-patch disposition if validation failed.
- Changed file and its traceability justification.
- Validation commands/checks actually executed and their results.
- Test result, noting that this is a documentation artifact and no code test was applicable.
- Regression and scope results.
- Final bounded diff summary.
- Any unresolved issue, including the non-blocking unavailable RR-06 text if relevant.

Do not close the finding by assertion. Hand the patched working tree to the independent auditor for a Post-Patch Re-Audit, which must be initiated by re-running:

```text
./hhtech/audit 042
```