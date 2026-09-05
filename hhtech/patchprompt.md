# Artifact 043 — mechanism vs semantics boundary

## Verdict: BLOCKED

**DO NOT PATCH.**

The audit is **BLOCKED** because the declared target artifact,
`docs/constitution/mechanism_semantics.md`, is not present on disk and no complete target
content was supplied. Consequently, mandatory compliance cannot be determined for the artifact’s
identity and metadata, the nine prohibitions required verbatim by the Roadmap, their binding
status, Blueprint §13.7a and RMS §3–§4 compliance, internal consistency, negative and boundary
coverage, diff integrity, or regression state.

This is primarily an **audit-context/source-resolution gap**: the evidence needed to evaluate the
target is unavailable. The target’s absence is also the confirmed artifact defect recorded by the
audit as `AUD-043-01`, but this BLOCKED verdict must not be cleared by inventing or authoring a
target patch under this prompt.

## Exact target scope

- **Artifact ID:** 043
- **Artifact name:** mechanism vs semantics boundary
- **Declared path:** `docs/constitution/mechanism_semantics.md`
- **Scope kind:** file
- **Multi-file entry:** False
- **Declared audit scope:** only `docs/constitution/mechanism_semantics.md`

Do not modify any file merely to turn the BLOCKED verdict into PASS. Do not modify the target
artifact, create replacement content, or apply a remediation plan while the audit-context gap
remains unresolved.

## Unavailable evidence sources

The audit report used these unavailable source labels:

1. **TARGET docs/constitution/mechanism_semantics.md** —
   `docs/constitution/mechanism_semantics.md` is declared but not present on disk. No target
   header, authored content, nine prohibitions, binding completion state, baseline, or target diff
   is available. This is the blocking source-resolution gap.
2. **Requirement BR-20** — the authoritative requirement register entry is unavailable. The audit
   classified this as `UNVERIFIABLE — requirement register unavailable (GAP-C, non-blocking)`;
   it does not independently cause the BLOCKED verdict.
3. **Requirement RR-04** — the authoritative requirement register entry is unavailable. The audit
   classified this as `UNVERIFIABLE — requirement register unavailable (GAP-C, non-blocking)`;
   it does not independently cause the BLOCKED verdict.
4. **Artifact 004 (content)** — `/CLAUDE.md` is unavailable because the file does not exist in
   the repository. This was context only, not a target requirement, and does not independently
   cause the BLOCKED verdict.

## Required evidence resolution

Before any artifact patching decision is made, the blocking target evidence must become
available: the complete authored content for
`docs/constitution/mechanism_semantics.md` at its exact declared path, or an equivalent complete
target-content submission that can be inspected as the current target. The current repository
state and target diff/baseline must also be available for the audit to evaluate the mandatory
diff and regression conditions.

The authoritative requirement-register entries for **BR-20** and **RR-04** may remain unavailable
as the audit classified them as non-blocking GAP-C items; do not invent or paraphrase their
requirement text. Do not invent any other source content.

Once the blocking evidence is available, require a fresh full artifact audit by re-running:

```text
./hhtech/audit 043
```

The re-audit must determine the outcome of `AUD-043-01` from current evidence. Do not run a
second audit as part of this prompt or claim that the artifact passes.

## Authority and conduct restrictions

- Do not patch the artifact to clear the BLOCKED verdict.
- Do not invent source content, target content, requirements, metadata, or validation evidence.
- Do not weaken, rewrite, or reinterpret any Blueprint, RMS, Roadmap, or standards requirement.
- Do not modify the Master Blueprint, Record Model System, Roadmap,
  `hhtech/standards/audit-standard.md`, or `hhtech/standards/patch-standard.md`.
- Do not modify any out-of-scope artifact or unrelated file.
- Do not perform unrelated cleanup.
- Do not treat the available Artifact 039 dependency or neighboring artifacts as substitutes for
  the missing target.
- Do not declare PASS or close `AUD-043-01` based on an agent claim; only the re-audit may assign
  the current outcome.

The next operation is evidence resolution, followed by re-running `./hhtech/audit 043`; it is
not an artifact patch.