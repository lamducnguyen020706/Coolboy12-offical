#!/usr/bin/env python3
"""COOLBOY12 hard audit — three independent B.AI auditors over one frozen context.

Runs standalone. It does not call Claude Code, does not depend on it, and does not
patch, format, stage, or commit anything. Its only writes are the audit report and
its own temporary payloads.

    coolboy12-audit            # target from repository state, verified
    coolboy12-audit 033        # explicit artifact
    coolboy12-audit --help

**Fail-closed.** Every path that cannot complete an audit ends at BLOCKED. A missing
key, an unreachable API, an unknown model, a malformed response, an ambiguous target
or a mutated artifact are all BLOCKED — never PASS. Exit codes: 0 PASS, 1 FAIL,
2 BLOCKED.

Repository conventions reused rather than reinvented:

* artifact identity is the Roadmap row (``**NNN** · name · `path` · …``) cross-checked
  against the artifact document's own ``**Artifact NNN**`` header — Artifact 003's
  convention, not a filename guess;
* the governing sources for a target are the ones *its own row cites* (``BP:``,
  ``RMS:``, ``H:``), so context selection is derived from the Roadmap, not chosen here;
* tooling lives in ``scripts/`` beside the existing progress-sync scripts;
* generated output lives under ``reports/``, which carries no architectural authority.

Artifact 015 governs the credential: the environment *"may load or access external
secret material for operational use, pass operational credentials to tools it
invokes"*, and *"a credential is not mutation authority."* The key is read from
``BAI_API_KEY`` and never written to a file, a report, a log line, or git.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ROADMAP = REPO_ROOT / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"
BLUEPRINT = REPO_ROOT / "docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md"
RMS = REPO_ROOT / "docs/sources/COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md"
PROGRESS = REPO_ROOT / "reports/progress.json"
REPORT_DIR = REPO_ROOT / "reports/audits"

ENDPOINT = os.environ.get("BAI_ENDPOINT", "https://api.b.ai/v1/chat/completions")
TIMEOUT = int(os.environ.get("BAI_TIMEOUT", "180"))

AUDITORS = (
    ("GLM", "BAI_AUDIT_MODEL_1", "glm-5.3-flash", "hard"),
    ("QWEN", "BAI_AUDIT_MODEL_2", "qwen3.8-flash", "independent"),
    ("MIMO", "BAI_AUDIT_MODEL_3", "mimo-v2.5", "adversarial"),
)

SEVERITIES = ("P0", "P1", "P2", "P3", "INFO")
BLOCKING = ("P0", "P1")


class Blocked(Exception):
    """Any condition under which an audit cannot be completed truthfully."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


# ---------------------------------------------------------------------------
# Repository state
# ---------------------------------------------------------------------------


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )
    return proc.stdout


def digest(path: Path) -> str | None:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Phase 2 — target resolution.  Deterministic or BLOCKED; never a guess.
# ---------------------------------------------------------------------------

ROW = re.compile(r"^\*\*(\d{3})\*\* · (.+?) · `([^`]+)`(.*)$", re.MULTILINE)


def roadmap_rows() -> dict[str, dict]:
    if not ROADMAP.is_file():
        raise Blocked("SOURCE_UNAVAILABLE", f"Roadmap not found at {ROADMAP}")
    rows: dict[str, dict] = {}
    for match in ROW.finditer(ROADMAP.read_text(encoding="utf-8")):
        artifact, name, path, tail = match.groups()
        fields = {}
        for part in tail.split(" · "):
            if ": " in part:
                key, _, value = part.partition(": ")
                fields[key.strip()] = value.strip()
        rows[artifact] = {
            "id": artifact, "name": name.strip(), "path": path.strip(),
            "fields": fields, "row": match.group(0),
        }
    if not rows:
        raise Blocked("SOURCE_UNAVAILABLE", "Roadmap parsed to zero artifact rows")
    return rows


def declared_paths(row: dict) -> list[Path]:
    """Files the row declares.

    Three shapes appear in the Roadmap and each is resolved as written, never widened:

    * a plain path — ``docs/constitution/record_envelope.md``;
    * a glob — ``docs/models/*/model.md``, matched with :meth:`Path.glob` against the
      pattern itself;
    * an elided range — ``src/coolboy12/adapters/a01_…a11_``, matched as a filename
      prefix inside the directory the row names.

    A bare ``/`` declares no filename (author's ruling, GAP-G) and yields nothing.
    Resolution never falls back to a parent directory: a mis-derived parent would
    sweep in every neighbouring file and audit something the row does not declare.
    """
    declared = row["path"]
    if declared in ("/", ""):
        return []
    relative = declared.lstrip("/")

    if "…" in relative:
        # An ordinal range: `a01_…a11_` means every member of the series, so match on
        # the series' alphabetic lead plus an ordinal, not on the first member alone.
        prefix = relative.split("…")[0]
        directory = (REPO_ROOT / prefix).parent
        stem = Path(prefix).name
        lead = re.match(r"^([^\d]*)", stem).group(1)
        if not directory.is_dir():
            return []
        series = re.compile(rf"^{re.escape(lead)}\d+")
        candidates = sorted(
            p for p in directory.iterdir() if p.is_file() and series.match(p.name)
        )
    elif "*" in relative:
        candidates = sorted(REPO_ROOT.glob(relative))
    else:
        candidates = [REPO_ROOT / relative]
    return [p for p in candidates if p.is_file()]


def header_declares(path: Path, artifact: str) -> bool:
    """The artifact document's own identity header, per Artifact 003."""
    if path.suffix != ".md":
        return True  # code/config artifacts carry no markdown header
    head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    return bool(re.search(rf"\*\*Artifact {artifact}\*\*", head))


def resolve_target(argument: str | None, rows: dict[str, dict]) -> dict:
    """Explicit argument first, then verified repository state. Otherwise BLOCKED.

    Never "newest file", never "recently modified", never a filename guess: an audit
    that picks its own target can pick an easy one.
    """
    if argument:
        artifact = argument.strip().lstrip("#")
        if not re.fullmatch(r"\d{1,3}", artifact):
            # Allow a path, resolved back to the row that declares it.
            candidate = (REPO_ROOT / argument).resolve()
            owners = [
                key for key, row in rows.items()
                if candidate in {p.resolve() for p in declared_paths(row)}
            ]
            if len(owners) != 1:
                raise Blocked(
                    "TARGET_AMBIGUOUS",
                    f"{argument!r} is declared by {len(owners)} Roadmap rows: {owners or 'none'}",
                )
            artifact = owners[0]
        artifact = artifact.zfill(3)
        if artifact not in rows:
            raise Blocked("TARGET_UNKNOWN", f"no Roadmap row for artifact {artifact}")
        source = "explicit argument"
    else:
        artifact, source = target_from_state(rows)

    row = rows[artifact]
    files = declared_paths(row)
    if not files:
        raise Blocked(
            "TARGET_NOT_BUILT",
            f"artifact {artifact} declares {row['path']!r} and no such file exists — "
            "there is nothing to audit",
        )
    mismatched = [
        str(p.relative_to(REPO_ROOT)) for p in files if not header_declares(p, artifact)
    ]
    if mismatched:
        raise Blocked(
            "TARGET_IDENTITY_MISMATCH",
            f"file(s) {mismatched} do not carry the '**Artifact {artifact}**' identity header",
        )
    return {
        "id": artifact,
        "name": row["name"],
        "declared_path": row["path"],
        "files": files,
        "fields": row["fields"],
        "row": row["row"],
        "discovery": source,
    }


def target_from_state(rows: dict[str, dict]) -> tuple[str, str]:
    """Repository state, but only where the state proves itself.

    ``reports/progress.json`` is the progress-sync system's output and is known to
    drift (GAP-L). It is used only when it names an artifact whose declared file
    exists and carries the matching identity header; otherwise the caller is asked
    for an explicit target rather than audited against a guess.
    """
    if not PROGRESS.is_file():
        raise Blocked("TARGET_AMBIGUOUS", "no explicit target and no reports/progress.json")
    try:
        state = json.loads(PROGRESS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise Blocked("TARGET_AMBIGUOUS", f"reports/progress.json is not valid JSON: {error}")

    named = (state.get("current_activity") or {}).get("artifact") or state.get("current_frontier")
    if not named:
        raise Blocked(
            "TARGET_AMBIGUOUS",
            "reports/progress.json names no current artifact — pass one explicitly, "
            "e.g. `coolboy12-audit 033`",
        )
    artifact = str(named).zfill(3)
    if artifact not in rows:
        raise Blocked("TARGET_AMBIGUOUS", f"repository state names artifact {artifact}, "
                                          "which has no Roadmap row")
    files = declared_paths(rows[artifact])
    if not files or any(not header_declares(p, artifact) for p in files):
        raise Blocked(
            "TARGET_AMBIGUOUS",
            f"repository state names artifact {artifact}, but its declared file is absent or "
            "carries no matching identity header — state is stale. Pass a target explicitly",
        )
    return artifact, "reports/progress.json, verified against Roadmap and identity header"


# ---------------------------------------------------------------------------
# Phase 3/4 — context, assembled from the target's own citations, then frozen.
# ---------------------------------------------------------------------------


def section(document: Path, reference: str, span: int = 120) -> str | None:
    """A cited section of a source document, located by its own heading."""
    if not document.is_file():
        return None
    text = document.read_text(encoding="utf-8").splitlines()
    number = reference.lstrip("§").strip()
    pattern = re.compile(rf"^#+\s*{re.escape(number)}[\s.]")
    for index, line in enumerate(text):
        if pattern.match(line):
            end = index + 1
            while end < len(text) and end - index < span:
                if re.match(r"^#+\s", text[end]) and not text[end].startswith("#" * 6):
                    break
                end += 1
            return "\n".join(text[index:end])
    return None


def cited_sections(field_value: str, document: Path, label: str) -> dict[str, str]:
    found = {}
    for reference in re.findall(r"§[\w.]+", field_value or ""):
        body = section(document, reference, span=140)
        if body:
            found[f"{label} {reference}"] = body
    return found


@dataclass
class Context:
    target: dict
    artifact_text: dict[str, str]
    requirements: dict[str, str]
    dependencies: dict[str, str]
    git_status: str
    git_diff: str
    head: str
    hashes: dict[str, str] = field(default_factory=dict)
    fingerprint: str = ""

    def freeze(self) -> None:
        payload = json.dumps(
            {
                "target": self.target["id"],
                "files": sorted(self.artifact_text),
                "artifact_text": self.artifact_text,
                "requirements": sorted(self.requirements),
                "head": self.head,
            },
            sort_keys=True,
        )
        self.fingerprint = hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def render(self) -> str:
        parts = [f"# AUDIT TARGET\n\nArtifact {self.target['id']} — {self.target['name']}\n",
                 f"Roadmap row, verbatim:\n\n```\n{self.target['row']}\n```\n"]
        parts.append("# ARTIFACT UNDER AUDIT\n")
        for name, body in sorted(self.artifact_text.items()):
            parts.append(f"## FILE: {name}\n\n```\n{body}\n```\n")
        parts.append("# GOVERNING SOURCE REQUIREMENTS\n")
        for name, body in sorted(self.requirements.items()):
            parts.append(f"## {name}\n\n```\n{body}\n```\n")
        if self.dependencies:
            parts.append("# DECLARED DEPENDENCIES (context only — not under audit)\n")
            for name, body in sorted(self.dependencies.items()):
                parts.append(f"## {name}\n\n```\n{body}\n```\n")
        parts.append(f"# REPOSITORY STATE\n\nHEAD: {self.head}\n")
        parts.append(f"## git status --short\n\n```\n{self.git_status or '(clean)'}\n```\n")
        parts.append(f"## git diff for the target\n\n```\n{self.git_diff or '(no diff)'}\n```\n")
        return "\n".join(parts)


def build_context(target: dict) -> Context:
    artifact_text = {}
    hashes = {}
    for path in target["files"]:
        relative = str(path.relative_to(REPO_ROOT))
        artifact_text[relative] = path.read_text(encoding="utf-8", errors="replace")
        hashes[relative] = digest(path) or ""

    fields = target["fields"]
    requirements: dict[str, str] = {}
    requirements |= cited_sections(fields.get("BP", ""), BLUEPRINT, "Blueprint")
    requirements |= cited_sections(fields.get("RMS", ""), RMS, "RMS")

    missing = []
    for label, value, document in (("Blueprint", fields.get("BP", ""), BLUEPRINT),
                                   ("RMS", fields.get("RMS", ""), RMS)):
        for reference in re.findall(r"§[\w.]+", value or ""):
            if f"{label} {reference}" not in requirements:
                missing.append(f"{label} {reference}")
    if missing:
        raise Blocked(
            "CONTEXT_INCOMPLETE",
            "the target's cited sections could not be located in the sources: "
            + ", ".join(missing)
            + " — an auditor cannot verify a requirement it was not shown",
        )

    dependencies = {}
    rows = roadmap_rows()
    for dependency in re.findall(r"\d{3}", fields.get("H", "") or ""):
        row = rows.get(dependency)
        if not row:
            continue
        for path in declared_paths(row)[:1]:
            dependencies[f"Artifact {dependency} — {path.relative_to(REPO_ROOT)}"] = (
                path.read_text(encoding="utf-8", errors="replace")
            )

    relative_paths = [str(p.relative_to(REPO_ROOT)) for p in target["files"]]
    context = Context(
        target=target,
        artifact_text=artifact_text,
        requirements=requirements,
        dependencies=dependencies,
        git_status=git("status", "--short").strip(),
        git_diff=git("diff", "HEAD", "--", *relative_paths).strip(),
        head=git("rev-parse", "HEAD").strip() or "(no HEAD)",
        hashes=hashes,
    )
    context.freeze()
    return context


# ---------------------------------------------------------------------------
# Phase 5 — B.AI transport.  Every failure mode is named and ends at BLOCKED.
# ---------------------------------------------------------------------------

SCHEMA = """Reply with ONE JSON object and nothing else. No prose, no markdown fence.

{
  "verdict": "PASS" | "FAIL" | "BLOCKED",
  "summary": "<two or three sentences>",
  "findings": [
    {
      "finding_id": "<auditor>-01",
      "severity": "P0" | "P1" | "P2" | "P3" | "INFO",
      "requirement": "<the rule, quoted or precisely named>",
      "source_reference": "<Blueprint §x / RMS §y / Roadmap row NNN field>",
      "evidence": "<quoted text from the artifact or the source>",
      "observed_behavior": "<what the artifact actually does>",
      "failure_reason": "<why that violates the requirement>",
      "confidence": "HIGH" | "MEDIUM" | "LOW",
      "verification_status": "VERIFIED" | "UNVERIFIED"
    }
  ]
}

Rules that bind you:
- Every finding carries evidence quoted from the material you were given. A finding
  with no quotable evidence is UNVERIFIED, not a violation.
- Severity follows the requirement, never your impression. P0 is a constitutional or
  hard-boundary violation; P1 a mandatory requirement violation; P2 a significant
  correctness or conformance issue; P3 minor; INFO an observation.
- Do not speculate about files you were not shown. If a check needs material absent
  from the context, emit an UNVERIFIED finding saying exactly what is missing.
- Do not invent requirements. If the sources do not state a rule, it is not a rule.
- An empty findings list is a real answer, but reach it by checking, not by assuming.
"""

ROLES = {
    "hard": (
        "You are the PRIMARY HARD AUDITOR. Assume the artifact is wrong until its "
        "compliance is demonstrated from the sources given to you. Check: Blueprint "
        "compliance, Roadmap row compliance (every declared field, Val and Done "
        "especially), Record Model System compliance, structure, required sections and "
        "fields, invariants, boundaries, prohibited behaviour, forbidden dependencies, "
        "scope expansion beyond the row's declaration, contract-versus-content mismatch, "
        "and false compliance — wording that claims conformance the content does not "
        "deliver. Do not look for reasons to pass it."
    ),
    "independent": (
        "You are an INDEPENDENT SECOND AUDITOR. You are auditing from scratch. No other "
        "auditor's findings or verdict have been shown to you, and you must not assume "
        "any exist. Work the requirements yourself and report what you find. Pay "
        "particular attention to requirements that are easy to skip: negative cases, "
        "failure behaviour, boundary conditions, internal contradictions between one "
        "part of the artifact and another, and claims made without evidence."
    ),
    "adversarial": (
        "You are the ADVERSARIAL / EDGE-CASE AUDITOR. Try to prove this artifact fails. "
        "Attack: edge cases, malformed or missing metadata, invalid references, illegal "
        "state transitions, boundary bypass, fail-open behaviour, unsafe fallback, "
        "authority leakage, derived material presented as authoritative, provenance and "
        "version inconsistency, hidden dependencies, scope leakage, regression, and any "
        "path by which this artifact could report success while being wrong. "
        "Discipline: an attack you cannot evidence is UNVERIFIED, not a finding. Do not "
        "promote speculation to a violation."
    ),
    "judge": (
        "You are the FINAL JUDGE. Three auditors worked the same frozen context "
        "independently. You are not counting votes: a single evidenced finding outranks "
        "two unevidenced agreements. Verify each finding against the quoted evidence, "
        "separate fact from interpretation, collapse duplicates, reject unsupported "
        "findings, and resolve disputes on the evidence. Then decide.\n\n"
        "PASS only if no P0 and no P1 finding survives verification and the mandatory "
        "requirements are positively evidenced. FAIL if evidence establishes a violation. "
        "BLOCKED if compliance cannot be determined from the material available. "
        "Unverified is never a pass."
    ),
}


def call_bai(model: str, system: str, user: str, api_key: str) -> dict:
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0,
        "response_format": {"type": "json_object"},
    }).encode("utf-8")

    request = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            raw = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:400]
        if error.code == 401:
            raise Blocked("API_UNAUTHORIZED", f"{model}: BAI_API_KEY rejected (401)")
        if error.code == 404:
            raise Blocked("MODEL_UNAVAILABLE", f"{model}: not found at the endpoint (404) — {detail}")
        if error.code == 429:
            raise Blocked("API_RATE_LIMITED", f"{model}: rate limited (429)")
        raise Blocked("API_ERROR", f"{model}: HTTP {error.code} — {detail}")
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise Blocked("API_UNREACHABLE", f"{model}: {error}")

    try:
        envelope = json.loads(raw)
    except json.JSONDecodeError as error:
        raise Blocked("MALFORMED_RESPONSE", f"{model}: response is not JSON ({error})")

    if isinstance(envelope, dict) and envelope.get("error"):
        raise Blocked("API_ERROR", f"{model}: {str(envelope['error'])[:300]}")

    try:
        content = envelope["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise Blocked("MALFORMED_RESPONSE", f"{model}: no choices[0].message.content")
    if not content or not content.strip():
        raise Blocked("EMPTY_RESPONSE", f"{model}: model returned empty content")

    return parse_audit(model, content)


def parse_audit(model: str, content: str) -> dict:
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n", "", text)
        text = re.sub(r"\n?```\s*$", "", text)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise Blocked("MALFORMED_RESPONSE", f"{model}: content holds no JSON object")
        try:
            parsed = json.loads(match.group(0))
        except json.JSONDecodeError as error:
            raise Blocked("MALFORMED_RESPONSE", f"{model}: unparseable JSON ({error})")

    if not isinstance(parsed, dict):
        raise Blocked("MALFORMED_RESPONSE", f"{model}: top level is {type(parsed).__name__}, not an object")
    verdict = str(parsed.get("verdict", "")).upper()
    if verdict not in ("PASS", "FAIL", "BLOCKED"):
        raise Blocked("MALFORMED_RESPONSE", f"{model}: verdict {verdict!r} is not PASS/FAIL/BLOCKED")
    findings = parsed.get("findings")
    if findings is None:
        findings = []
    if not isinstance(findings, list):
        raise Blocked("MALFORMED_RESPONSE", f"{model}: findings is not a list")
    return {"verdict": verdict, "summary": str(parsed.get("summary", "")).strip(), "findings": findings}


# ---------------------------------------------------------------------------
# Phases 6-8 — normalization and cross-auditor comparison.
# ---------------------------------------------------------------------------


def normalize(auditor: str, report: dict) -> list[dict]:
    normalized = []
    for index, raw in enumerate(report["findings"], start=1):
        if not isinstance(raw, dict):
            continue
        severity = str(raw.get("severity", "")).upper()
        if severity not in SEVERITIES:
            severity = "INFO"
        evidence = str(raw.get("evidence", "")).strip()
        status = str(raw.get("verification_status", "")).upper()
        if status not in ("VERIFIED", "UNVERIFIED"):
            status = "VERIFIED" if evidence else "UNVERIFIED"
        if not evidence:
            status = "UNVERIFIED"
        normalized.append({
            "finding_id": str(raw.get("finding_id") or f"{auditor}-{index:02d}"),
            "auditor": auditor,
            "severity": severity,
            "requirement": str(raw.get("requirement", "")).strip(),
            "source_reference": str(raw.get("source_reference", "")).strip(),
            "evidence": evidence,
            "observed_behavior": str(raw.get("observed_behavior", "")).strip(),
            "failure_reason": str(raw.get("failure_reason", "")).strip(),
            "confidence": str(raw.get("confidence", "")).upper() or "MEDIUM",
            "verification_status": status,
        })
    return normalized


def signature(finding: dict) -> str:
    text = f"{finding['requirement']} {finding['source_reference']}".lower()
    return re.sub(r"[^a-z0-9§. ]+", "", text).strip()[:90]


def cross_compare(findings: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {}
    for finding in findings:
        buckets.setdefault(signature(finding) or finding["finding_id"], []).append(finding)

    classified = {k: [] for k in
                  ("AGREED", "SINGLE_AUDITOR", "DISPUTED", "FALSE_POSITIVE_CANDIDATE", "UNVERIFIED")}
    for group in buckets.values():
        auditors = {f["auditor"] for f in group}
        verified = [f for f in group if f["verification_status"] == "VERIFIED"]
        entry = {"finding": group[0], "group": group, "auditors": sorted(auditors)}
        if not verified:
            classified["UNVERIFIED"].append(entry)
        elif not any(f["evidence"] for f in verified):
            classified["FALSE_POSITIVE_CANDIDATE"].append(entry)
        elif len(auditors) >= 2:
            severities = {f["severity"] for f in group}
            classified["DISPUTED" if len(severities) > 1 else "AGREED"].append(entry)
        else:
            classified["SINGLE_AUDITOR"].append(entry)
    return classified


def local_verdict(classified: dict[str, list[dict]]) -> tuple[str, list[dict]]:
    """The tool's own fail-closed reading, independent of the judge model."""
    mandatory = [
        entry["finding"]
        for key in ("AGREED", "SINGLE_AUDITOR", "DISPUTED")
        for entry in classified[key]
        if entry["finding"]["severity"] in BLOCKING
        and entry["finding"]["verification_status"] == "VERIFIED"
    ]
    if mandatory:
        return "FAIL", mandatory
    unverified_blocking = [
        entry["finding"] for entry in classified["UNVERIFIED"]
        if entry["finding"]["severity"] in BLOCKING
    ]
    if unverified_blocking:
        return "BLOCKED", unverified_blocking
    return "PASS", []


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def finding_block(finding: dict) -> str:
    return (
        f"- **{finding['finding_id']}** · `{finding['severity']}` · {finding['auditor']} · "
        f"{finding['verification_status']} · confidence {finding['confidence']}\n"
        f"  - requirement: {finding['requirement'] or '—'}\n"
        f"  - source: {finding['source_reference'] or '—'}\n"
        f"  - evidence: {finding['evidence'][:600] or '—'}\n"
        f"  - observed: {finding['observed_behavior'][:400] or '—'}\n"
        f"  - why it fails: {finding['failure_reason'][:400] or '—'}\n"
    )


def write_report(context: Context, reports: dict, classified: dict, verdict: str,
                 judge: dict | None, models: dict, blocked: list[str],
                 mutation: str | None) -> Path:
    target = context.target
    stamp = dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"audit-{target['id']}-{stamp}.md"

    lines = [
        f"# COOLBOY12 HARD AUDIT — Artifact {target['id']}",
        "",
        "## 1. Target",
        "",
        "| | |", "|---|---|",
        f"| artifact | {target['id']} — {target['name']} |",
        f"| declared path | `{target['declared_path']}` |",
        f"| files audited | {', '.join(str(p.relative_to(REPO_ROOT)) for p in target['files'])} |",
        f"| phase / stage | {target['fields'].get('Ph/St', '—')} |",
        f"| discovery | {target['discovery']} |",
        "",
        "Roadmap row, verbatim:",
        "", "```", target["row"], "```", "",
        "## 2. Audit Metadata",
        "",
        f"- timestamp: {dt.datetime.now(dt.UTC).isoformat()}",
        f"- git HEAD: `{context.head}`",
        f"- working tree: {'clean' if not context.git_status else 'dirty'}",
        f"- context fingerprint: `{context.fingerprint}`",
        "- target file digests:",
    ]
    lines += [f"  - `{name}` — `{value}`" for name, value in sorted(context.hashes.items())]
    lines += [
        "",
        "## 3. Source Requirements",
        "",
        "Selected from the fields of the target's own Roadmap row, not chosen by this tool:",
        "",
        f"- `BP:` {target['fields'].get('BP', '—')}",
        f"- `RMS:` {target['fields'].get('RMS', '—')}",
        f"- `H:` {target['fields'].get('H', '—')}",
        f"- `Val:` {target['fields'].get('Val', '—')}",
        f"- `Done:` {target['fields'].get('Done', '—')}",
        "",
        "Sections placed in the audit context:",
        "",
    ]
    lines += [f"- {name}" for name in sorted(context.requirements)] or ["- (none)"]
    lines += [
        "",
        "## 4. Frozen Audit Context",
        "",
        (f"All auditors received one identical context, fingerprint "
         f"`{context.fingerprint}`. No auditor saw another auditor's output before "
         f"completing its own audit."),
        "",
        "## 5. Auditor Configuration",
        "",
        "| role | model | status |", "|---|---|---|",
    ]
    for name, _, _, role in AUDITORS:
        state = "completed" if name in reports else "BLOCKED"
        lines.append(f"| {role} | `{models[name]}` | {state} |")
    lines += [
        (f"| final judge | `{models.get('JUDGE', '—')}` | "
         f"{'completed' if judge else 'not reached'} |"),
        "",
        f"Endpoint: `{ENDPOINT}` · credential: `BAI_API_KEY` (value never recorded).",
        "",
    ]

    for name, _, _, role in AUDITORS:
        lines += [f"## 6.{name} — {role} audit (`{models[name]}`)", ""]
        report = reports.get(name)
        if not report:
            lines += ["**BLOCKED — this auditor did not return a usable audit.**", ""]
            continue
        lines += [f"Auditor verdict: **{report['verdict']}**", "", report["summary"] or "_no summary_", ""]
        normalized = normalize(name, report)
        lines += [finding_block(f) for f in normalized] or ["_no findings_", ""]
        lines.append("")

    lines += ["## 7. Cross-Auditor Findings", ""]
    for key in ("AGREED", "SINGLE_AUDITOR"):
        lines += [f"### {key}", ""]
        entries = classified.get(key, [])
        lines += [finding_block(e["finding"]) for e in entries] or ["_none_", ""]
        lines.append("")

    lines += ["## 8. Disputed Findings", ""]
    lines += [finding_block(e["finding"]) for e in classified.get("DISPUTED", [])] or ["_none_", ""]
    lines += ["", "## 9. Unverified Findings", ""]
    lines += [finding_block(e["finding"]) for e in classified.get("UNVERIFIED", [])] or ["_none_", ""]
    lines += ["", "### False-positive candidates", ""]
    lines += [finding_block(e["finding"]) for e in
              classified.get("FALSE_POSITIVE_CANDIDATE", [])] or ["_none_", ""]

    mandatory = [
        e["finding"] for key in ("AGREED", "SINGLE_AUDITOR", "DISPUTED")
        for e in classified.get(key, [])
        if e["finding"]["severity"] in BLOCKING and e["finding"]["verification_status"] == "VERIFIED"
    ]
    lines += ["", "## 10. Mandatory Violations (P0/P1, verified)", ""]
    lines += [finding_block(f) for f in mandatory] or ["_none_", ""]

    lines += ["", "## 11. Final Verdict", "", f"# {verdict}", ""]
    if blocked:
        lines += ["Blocking conditions:", ""] + [f"- {b}" for b in blocked] + [""]
    if mutation:
        lines += [f"- **{mutation}**", ""]
    if judge:
        lines += ["### Final judge", "", f"Judge verdict: **{judge['verdict']}**", "",
                  judge["summary"] or "_no summary_", ""]
        if judge["verdict"] != verdict:
            lines += [
                (f"> The judge returned **{judge['verdict']}** while this tool's "
                 f"fail-closed reading of the evidence is **{verdict}**. The stricter "
                 f"of the two is reported as the verdict; the disagreement is recorded "
                 f"rather than resolved silently."),
                "",
            ]

    lines += ["## 12. Minimal Required Corrections", ""]
    if mandatory:
        lines += [
            ("Stated as what must change and why. This tool does not patch, and no "
             "correction below has been applied."),
            "",
        ]
        for finding in mandatory:
            lines.append(
                f"- **{finding['finding_id']}** — {finding['failure_reason'] or finding['requirement']}\n"
                f"  - required by: {finding['source_reference'] or '—'}"
            )
    elif verdict == "BLOCKED":
        lines.append("None stated: the audit did not complete, so no correction is established.")
    else:
        lines.append("None. No verified mandatory violation survived cross-auditor comparison.")

    lines += [
        "", "---", "",
        ("*Generated by `coolboy12-audit`. This report is generated output under "
         "`reports/`; it carries no architectural authority, is not a Record, and "
         "approves nothing. The tool is read-only: it patched nothing and committed "
         "nothing.*"),
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def resolve_models() -> dict[str, str]:
    models = {name: os.environ.get(env, default) for name, env, default, _ in AUDITORS}
    models["JUDGE"] = os.environ.get("BAI_FINAL_MODEL", models["GLM"])
    empty = [name for name, value in models.items() if not value or not value.strip()]
    if empty:
        raise Blocked("MODEL_UNAVAILABLE", f"model name is empty for: {', '.join(empty)}")
    return models


def run(argument: str | None, dry_run: bool) -> int:
    print("COOLBOY12 hard audit")
    rows = roadmap_rows()
    target = resolve_target(argument, rows)
    print(f"  target      Artifact {target['id']} — {target['name']}")
    print(f"  files       {', '.join(str(p.relative_to(REPO_ROOT)) for p in target['files'])}")
    print(f"  discovery   {target['discovery']}")

    context = build_context(target)
    before = dict(context.hashes)
    print(f"  context     frozen, fingerprint {context.fingerprint[:16]}…")
    print(f"  sources     {len(context.requirements)} cited section(s)")

    models = resolve_models()
    for name, _, _, role in AUDITORS:
        print(f"  {role:<12}{models[name]}")
    print(f"  judge       {models['JUDGE']}")

    if dry_run:
        print("\n--dry-run: context assembled and frozen, no API call made.")
        return 2

    api_key = os.environ.get("BAI_API_KEY", "").strip()
    if not api_key:
        raise Blocked("API_KEY_MISSING", "BAI_API_KEY is not set in the environment")

    rendered = context.render()
    reports: dict[str, dict] = {}
    blocked: list[str] = []

    print("\n  auditing in parallel over one frozen context…")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {
            pool.submit(
                call_bai, models[name],
                f"{ROLES[role]}\n\n{SCHEMA}",
                rendered, api_key,
            ): name
            for name, _, _, role in AUDITORS
        }
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            try:
                reports[name] = future.result()
                print(f"    {name:<6} {reports[name]['verdict']:<8} "
                      f"{len(reports[name]['findings'])} finding(s)")
            except Blocked as error:
                blocked.append(f"{name}: {error.code} — {error.detail}")
                print(f"    {name:<6} BLOCKED  {error.code}")

    findings = [f for name, report in reports.items() for f in normalize(name, report)]
    classified = cross_compare(findings)
    verdict, _ = local_verdict(classified)

    judge = None
    if reports and not blocked:
        judge_input = (
            rendered
            + "\n\n# AUDITOR REPORTS\n\n"
            + json.dumps({name: reports[name] for name in reports}, indent=2)
            + "\n\n# NORMALIZED FINDINGS\n\n"
            + json.dumps(findings, indent=2)
            + "\n\n# CROSS-AUDITOR CLASSIFICATION\n\n"
            + json.dumps({k: len(v) for k, v in classified.items()}, indent=2)
        )
        try:
            judge = call_bai(models["JUDGE"], f"{ROLES['judge']}\n\n{SCHEMA}", judge_input, api_key)
            print(f"    JUDGE  {judge['verdict']}")
        except Blocked as error:
            blocked.append(f"JUDGE: {error.code} — {error.detail}")
            print(f"    JUDGE  BLOCKED  {error.code}")

    # Fail closed: any auditor that did not complete blocks the audit, and the
    # stricter of (tool reading, judge verdict) is the verdict that stands.
    if blocked or len(reports) < len(AUDITORS):
        verdict = "BLOCKED"
    elif judge and judge["verdict"] == "FAIL":
        verdict = "FAIL"
    elif judge and judge["verdict"] == "BLOCKED" and verdict == "PASS":
        verdict = "BLOCKED"

    after = {name: digest(REPO_ROOT / name) for name in before}
    mutation = None
    if after != before:
        changed = [name for name in before if before[name] != after[name]]
        mutation = f"UNEXPECTED_MUTATION_DETECTED — target file(s) changed during the audit: {changed}"
        verdict = "BLOCKED"
        print(f"\n  {mutation}")

    report_path = write_report(context, reports, classified, verdict, judge, models,
                               blocked, mutation)
    print(f"\n  report      {report_path.relative_to(REPO_ROOT)}")
    print(f"  VERDICT     {verdict}")
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[verdict]


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="coolboy12-audit",
        description="Hard-audit a COOLBOY12 artifact with three independent B.AI auditors.",
        epilog=(
            "Environment: BAI_API_KEY (required) · BAI_AUDIT_MODEL_1/2/3 · BAI_FINAL_MODEL · "
            "BAI_ENDPOINT · BAI_TIMEOUT.  Read-only: never patches, stages or commits. "
            "Exit 0 PASS, 1 FAIL, 2 BLOCKED."
        ),
    )
    parser.add_argument("artifact", nargs="?",
                        help="artifact id (e.g. 033) or a path it declares; "
                             "omitted, the target is taken from verified repository state")
    parser.add_argument("--dry-run", action="store_true",
                        help="resolve the target and freeze the context, then stop before any API call")
    args = parser.parse_args()

    try:
        return run(args.artifact, args.dry_run)
    except Blocked as error:
        print(f"\n  VERDICT     BLOCKED\n  reason      {error.code} — {error.detail}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
