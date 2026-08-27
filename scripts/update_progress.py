#!/usr/bin/env python3
"""Publish the COOLBOY12 living report from repository-native state.

The Roadmap is read-only authority for artifact metadata. progress.json is live
build state; implement-log.json is append-oriented prompt history. This script
never treats a prompt, file, or commit alone as VERIFIED.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
STATE_PATH = REPORTS_DIR / "progress.json"
LOG_PATH = REPORTS_DIR / "implement-log.json"
CONTRACT_PATH = REPORTS_DIR / "HTML_UPDATE_CONTRACT.md"
ROADMAP_PATH = ROOT / "docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md"
HTML_PATH = REPORTS_DIR / "progressreport.html"
REPO_URL = "https://github.com/lamducnguyen020706/Coolboy12-offical"

PHASE_PURPOSES = {
    "P0":"Foundation: tree, boundaries, conventions, hooks and the invariant register before semantics.",
    "P1":"Bootstrap: the meta-contract, envelope and identity grammar that make Records well-formed.",
    "P2":"Kernel: Record constitution, ownership, authority, provenance and temporal boundaries.",
    "P3":"Registry: the sovereign semantic vocabulary and definition families used by consumers.",
    "P4":"Validation: universal structural checks with model-owned semantics kept separate.",
    "P5":"Mutation: model gates and the sole legal write path into canonical state.",
    "P6":"Derived contract: projection and rebuild contracts without turning derived data into source.",
    "P7":"World: World Model kinds, relationships and the World State Vector boundary.",
    "P8":"Derived layer: indexes, projections and rebuild process from canon.",
    "P9":"World state: the WSV singleton and simulation-state boundary.",
    "P10":"Epistemic: knowledge, evidence, reveal and epistemic cardinality.",
    "P11":"Production: intent, arcs, workflow, taste and art-direction state.",
    "P12":"Visual: visual specification, assets and authority split.",
    "P13":"Issue: publication reality, composition and the publication firewall.",
    "P14":"Emergence: proposal-only emergence without direct canon writes.",
    "P15":"Creative Governance: quality, review and verdict architecture.",
    "P16":"Reader, Coworkers and Capabilities: simulation, roles and capability boundaries.",
    "P17":"Surfaces, Dormancy and Extensibility: surfaces, recovery and adapter contracts.",
    "P18":"Integration and Freeze: drills, benchmarks, conformance, runtime boundary and freeze.",
}
FIELD_NAMES = "Own|RM|T|R|SoT|Auth|Canon|CD|Ph/St|Req|BP|RMS|H|S|LS|G|→|Val|Done|Why|Risk|∥"
FIELD_RE = re.compile(rf"(?P<key>{FIELD_NAMES}):\s*(?P<value>.*?)(?=\s+·\s+(?:{FIELD_NAMES}):|$)")
UNLOCK_RE = re.compile(r"(?:^|\s+·\s+)→\s*(?P<value>.*?)(?=\s+·\s+Val:|$)")
ARTIFACT_RE = re.compile(r"^\*\*(?P<id>\d{3})\*\* · (?P<name>.*?) · `(?P<path>.*?)` · (?P<rest>.*)$")
PHASE_RE = re.compile(r"^## PHASE (?P<id>P\d+) — (?P<name>.*?) \((?P<start>\d{3})–(?P<end>\d{3})\) · (?P<count>\d+) artifacts")


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()


def clean(value: str) -> str:
    return re.sub(r"\*\*|`", "", value or "").strip()


def parse_roadmap() -> tuple[list[dict], list[dict]]:
    phases, artifacts = [], []
    for raw in ROADMAP_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        pm = PHASE_RE.match(line)
        if pm:
            phases.append({"id":pm["id"],"name":pm["name"],"start":pm["start"],"end":pm["end"],"count":int(pm["count"]),"purpose":PHASE_PURPOSES.get(pm["id"],pm["name"])})
            continue
        am = ARTIFACT_RE.match(line)
        if not am:
            continue
        fields = {m["key"]:m["value"].strip() for m in FIELD_RE.finditer(am["rest"])}
        unlock_match = UNLOCK_RE.search(am["rest"])
        if unlock_match:
            fields["→"] = unlock_match["value"].strip()
        stage = fields.get("Ph/St", "")
        phase = stage.split("/")[0] if stage else next((p["id"] for p in phases if p["start"] <= am["id"] <= p["end"]), "")
        artifacts.append({"id":am["id"],"name":am["name"].strip(),"planned_path":am["path"],"phase":phase,"fields":fields,"description":fields.get("Val",""),"purpose":fields.get("Why",""),"validation":fields.get("Val",""),
"done_condition":fields.get("Done",""),"dependencies":fields.get("H","—"),"unlocks":fields.get("→","—"),"blueprint":fields.get("BP","n/a"),"rms":fields.get("RMS","n/a")})
    if len(phases) != 19 or len(artifacts) != 490 or [a["id"] for a in artifacts] != [f"{i:03d}" for i in range(1,491)]:
        raise RuntimeError("Roadmap parse refused: expected 19 phases and exact artifact sequence 001–490")
    return phases, artifacts


def tracked_files() -> set[str]:
    return set(run("git","ls-files").splitlines())


def artifact_commit_files(aid: str, tracked: set[str], shas: list[str] | None = None) -> list[str]:
    """Tracked files added or changed by the commits that declare *aid*.

    ``shas`` comes from :func:`artifact_commits`, which reads subject lines
    only. Grepping the whole message here — as this did — searched bodies too,
    so a commit that merely *quotes* the Roadmap contributed its files to an
    artifact it had nothing to do with. That mattered beyond cosmetics: these
    files are the second half of the completion predicate, and borrowed
    evidence is not evidence.

    The fallback grep remains for callers with no subject-derived shas to
    hand, and it is why every result is intersected with ``tracked``.
    """
    if shas is None:
        shas = run("git","log","--all","--format=%H","--grep",f"^Artifact {aid}\\b").splitlines()
    files = set()
    for sha in shas:
        try:
            out = run("git","show","--format=","--name-only","--diff-filter=ACMRT",sha)
        except subprocess.CalledProcessError:
            continue
        files.update(p.strip() for p in out.splitlines() if p.strip() in tracked)
    return sorted(files)


ARTIFACT_SUBJECT_RE = re.compile(r"^Artifact\s+(\d{3})\b")


def artifact_commits() -> dict[str, list[dict]]:
    """Commits whose *subject* declares an artifact, newest first.

    Anchored to the subject line and to the repository's own commit
    convention, ``Artifact NNN — description``. Searching the whole message
    was tried and is wrong: one commit body quotes the Roadmap and mentions
    "Artifact 031", which made an unbuilt artifact look finished.

    A commit is a claim its author made about which artifact they were
    building. It is evidence, not proof, which is why
    :func:`derive_completion` never acts on it alone.
    """
    raw = run("git", "log", "--all", "--date=iso-strict", "--format=%H%x1f%s%x1f%ad%x1e")
    found: dict[str, list[dict]] = {}
    for record in raw.split("\x1e"):
        parts = record.strip().split("\x1f")
        if len(parts) != 3:
            continue
        sha, subject, when = parts
        match = ARTIFACT_SUBJECT_RE.match(subject.strip())
        if match:
            found.setdefault(match.group(1), []).append(
                {"sha": sha, "short": sha[:7], "subject": subject.strip(), "date": when}
            )
    return found


def derive_completion(artifacts: list[dict], tracked: set[str], commits: dict[str, list[dict]]) -> dict:
    """Completion read from the repository, not from declared state.

    The contract already ranks *repository evidence* above
    ``reports/progress.json``; this makes the renderer honour that ordering
    instead of trusting a hand-maintained list that only advanced once.

    An artifact counts as complete on a **composite** of two independent
    signals, never one alone:

    1. a commit whose subject declares that artifact, and
    2. a tracked file attributable to it — its declared Roadmap path when it
       names an exact file, otherwise a tracked file that artifact's commits
       actually touched.

    Neither suffices by itself: a commit can name work it did not finish, and
    a file can appear for any reason.

    The frontier is then the **longest unbroken run from 001**. A later
    artifact with evidence does not count while an earlier one lacks it, so a
    stray match can never skip the sequence.
    """
    complete: list[str] = []
    reasons: dict[str, str] = {}
    for artifact in artifacts:
        aid = artifact["id"]
        if aid not in commits:
            reasons[aid] = "no commit declares this artifact"
            continue
        exact = [path for path in exact_files_for(artifact) if path in tracked]
        touched = artifact_commit_files(aid, tracked, [c["sha"] for c in commits[aid]])
        if exact:
            reasons[aid] = f"declared path tracked, {len(commits[aid])} commit(s)"
        elif touched:
            reasons[aid] = f"{len(touched)} tracked file(s) from {len(commits[aid])} commit(s)"
        else:
            reasons[aid] = "commit declares the artifact but no tracked file resulted"
            continue
        complete.append(aid)

    unbroken: list[str] = []
    for artifact in artifacts:
        if artifact["id"] in complete:
            unbroken.append(artifact["id"])
        else:
            break
    frontier = unbroken[-1] if unbroken else None
    following = next((a["id"] for a in artifacts if a["id"] not in unbroken), "freeze")

    # Current phase is the frontier's — except at a phase boundary. When the
    # frontier finishes its phase, the work in front of the author is the next
    # phase, and the report should already say so.
    phase_of = {a["id"]: a["phase"] for a in artifacts}
    phase = phase_of.get(frontier) or (artifacts[0]["phase"] if artifacts else "")
    if frontier:
        members = [a["id"] for a in artifacts if a["phase"] == phase]
        if all(aid in unbroken for aid in members) and following != "freeze":
            phase = phase_of.get(following, phase)

    return {
        "completed": unbroken,
        "frontier": frontier,
        "next": following,
        "phase": phase,
        "reasons": reasons,
        "evidenced_out_of_sequence": sorted(set(complete) - set(unbroken)),
    }


def evidence_for(a: dict, tracked: set[str]) -> dict:
    aid, planned = a["id"], a["planned_path"]
    if aid == "001":
        actual = sorted(tracked)
    else:
        actual = artifact_commit_files(aid, tracked)
        if planned and planned not in {"/","coolboy12/","tests/",".claude/commands/"} and planned in tracked:
            actual = sorted(set(actual) | {planned})
        if planned == "tests/":
            actual = sorted(set(actual) | {p for p in tracked if p.startswith("tests/")})
        if planned == ".claude/commands/":
            actual = sorted(set(actual) | {p for p in tracked if p.startswith(".claude/commands/")})
    dirs = sorted({(str(Path(p).parent) if str(Path(p).parent) != "." else ".") + "/" for p in actual})
    return {"actual_files":actual,"directories":dirs}


def exact_files_for(artifact: dict) -> list[str]:
    path = clean(artifact.get("planned_path", ""))
    if not path or path.startswith("(") or "directory" in path.lower() or "multi-file" in path.lower() or "…" in path:
        return []
    return [path.lstrip("/")]


def dependency_files_for(artifact: dict, artifacts_by_id: dict[str, dict]) -> list[str]:
    paths = []
    for dependency_id in re.findall(r"\b\d{3}\b", clean(artifact.get("dependencies", ""))):
        dependency = artifacts_by_id.get(dependency_id)
        if not dependency:
            continue
        paths.extend(exact_files_for(dependency))
    return list(dict.fromkeys(paths))


def directory_for(artifact: dict, exact_files: list[str]) -> str:
    if exact_files:
        return ", ".join(dict.fromkeys((str(Path(path).parent) if str(Path(path).parent) != "." else "") + "/" for path in exact_files)).replace("//", "/")
    planned = clean(artifact.get("planned_path", ""))
    if planned and not planned.startswith("("):
        return planned.rstrip("/") + "/"
    return "UNRESOLVED"


def load_state() -> dict:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if state.get("roadmap_total") != 490:
        raise RuntimeError("progress.json refused: roadmap_total must be 490")
    completed = state.get("completed_artifacts", [])
    if completed != [f"{i:03d}" for i in range(1,len(completed)+1)]:
        raise RuntimeError("progress.json refused: completed_artifacts must be contiguous from 001")
    if state.get("current_frontier") != (completed[-1] if completed else None):
        raise RuntimeError("progress.json refused: current_frontier must equal the last completed artifact")
    return state


def validate_state_against_roadmap(state: dict, artifacts: list[dict]) -> dict:
    """Reject a state whose next_artifact or current_phase contradicts the Roadmap.

    load_state proves the completed set is well-formed on its own terms. It
    cannot prove next_artifact or current_phase are right, because both are
    claims about the Roadmap. A hand-edited state naming next_artifact 099 or
    current_phase P7 passed every earlier check, so both are checked here.
    """
    completed = set(state.get("completed_artifacts", []))
    expected_next = next((a["id"] for a in artifacts if a["id"] not in completed), "freeze")
    if state.get("next_artifact") != expected_next:
        raise RuntimeError(
            f"progress.json refused: next_artifact must be {expected_next}, "
            f"got {state.get('next_artifact')!r}"
        )
    phase_by_id = {a["id"]: a["phase"] for a in artifacts}
    legal = {phase_by_id.get(state.get("current_frontier")), phase_by_id.get(expected_next)}
    legal.discard(None)
    if legal and state.get("current_phase") not in legal:
        raise RuntimeError(
            f"progress.json refused: current_phase must be one of {sorted(legal)}, "
            f"got {state.get('current_phase')!r}"
        )
    return state


def load_log() -> dict:
    data = json.loads(LOG_PATH.read_text(encoding="utf-8"))
    if not isinstance(data.get("events"), list):
        raise RuntimeError("implement-log.json refused: events must be an array")
    return data


def atomic_json(path: Path, data: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    json.loads(tmp.read_text(encoding="utf-8"))
    tmp.replace(path)


def esc(s: object) -> str:
    return html.escape(str(s), quote=True)


def repo_facts(state: dict) -> dict:
    state["repository_branch"] = run("git","branch","--show-current") or "detached"
    state["repository_commit"] = run("git","rev-parse","HEAD")
    state["commit_count"] = int(run("git","rev-list","--count","--all"))
    files = run("git","ls-files").splitlines()
    state["file_count"] = len(files)
    state["test_file_count"] = len([p for p in files if p.startswith("tests/") and p.endswith((".py",".md"))])
    return state


def event_dt(event: dict) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(event.get("timestamp", ""))
    except (TypeError, ValueError):
        return None


def build_events(
    artifacts: list[dict], commits: dict[str, list[dict]], derived: dict, tracked: set[str]
) -> list[dict]:
    """The Implement Log: what was built, not that a prompt arrived.

    Every event is one artifact-declaring commit, carrying the artifact's
    Roadmap name, the commit subject and hash, and the files it touched. The
    log previously rendered ``UserPromptSubmit`` events, so every row read
    "Prompt received" — an accurate record of a keystroke and a useless record
    of the build.

    Prompt telemetry is not deleted; it simply stops being what this surface
    displays. ``reports/implement-log.json`` keeps it, and the hook keeps
    writing it.
    """
    named = {a["id"]: clean(a.get("name", "")) for a in artifacts}
    phase_of = {a["id"]: a["phase"] for a in artifacts}
    complete = set(derived["completed"])
    events: list[dict] = []
    for aid, records in commits.items():
        for record in records:
            events.append(
                {
                    "timestamp": record["date"],
                    "artifact": aid,
                    "phase": phase_of.get(aid, ""),
                    "summary": record["subject"],
                    "artifact_name": named.get(aid, ""),
                    "commit": record["short"],
                    "files": artifact_commit_files(aid, tracked, [c["sha"] for c in records]) if aid in complete else [],
                    "counts": aid in complete,
                }
            )
    return sorted(events, key=lambda e: e["timestamp"], reverse=True)


def timeline_html(events: list[dict], derived: dict) -> str:
    groups = defaultdict(list)
    for event in events:
        parsed = event_dt(event)
        if parsed:
            groups[parsed.date().isoformat()].append((parsed, event))
    if not groups:
        return '<div class="empty-log"><strong>Chưa có artifact commit nào được ghi nhận.</strong><br>Implement Log dựng từ commit khai báo artifact; không tái tạo lịch sử khi chưa có bằng chứng.</div>'
    completed = set(derived["completed"])
    # The day each completed artifact first landed, so cumulative counts an
    # artifact once no matter how many commits it took.
    landed: dict[str, str] = {}
    for event in events:
        aid = event.get("artifact")
        parsed = event_dt(event)
        if aid in completed and parsed:
            day = parsed.date().isoformat()
            landed[aid] = min(landed.get(aid, day), day)
    days = []
    for date_key in sorted(groups, reverse=True):
        rows = sorted(groups[date_key], key=lambda pair: pair[0], reverse=True)
        day_dt = rows[0][0]
        # Daily delta counts the artifacts that reached completion that day —
        # distinct artifact IDs, so several commits on one artifact still count
        # once, and prompt/event counts are never used.
        daily_ids = {event["artifact"] for _, event in rows if event.get("counts")}
        daily_completed = len(daily_ids)
        daily_pct = daily_completed / 490 * 100
        cumulative = sum(1 for aid, day in landed.items() if day <= date_key)
        event_rows = []
        for parsed, event in rows:
            summary = esc(event.get("summary") or "")
            meta = [f'Artifact {esc(event["artifact"])}']
            if event.get("artifact_name"):
                meta.append(esc(event["artifact_name"]))
            if event.get("phase"):
                meta.append(esc(event["phase"]))
            if event.get("commit"):
                meta.append(f'<code>{esc(event["commit"])}</code>')
            files = event.get("files") or []
            shown = " · ".join(f'<code>{esc(p)}</code>' for p in files[:4])
            if len(files) > 4:
                shown += f' <span class="more">+{len(files)-4} more</span>'
            file_line = f'<small class="event-files">{shown}</small>' if shown else ""
            event_rows.append(
                f'<div class="log-event"><time>{parsed.astimezone(dt.timezone(dt.timedelta(hours=7))).strftime("%H:%M:%S")}</time>'
                f'<span class="event-dot">●</span><div><strong>{summary}</strong>'
                f'<small>{" · ".join(meta)}</small>{file_line}</div></div>'
            )
        # <details> has no "closed" attribute; absence of "open" is closed.
        # The newest day is the one that opens.
        newest = " open" if date_key == sorted(groups, reverse=True)[0] else ""
        days.append(f'<details class="day-node"{newest}><summary><span class="day-date">{day_dt.strftime("%d %b %Y").upper()}</span><span class="day-count">{daily_completed} artifact{"s" if daily_completed != 1 else ""} completed · <b>+{daily_pct:.1f}%</b></span><span class="day-overall">Overall {cumulative} / 490 · {cumulative/490*100:.1f}%</span></summary><div class="day-events">{"".join(event_rows)}</div></details>')
    return "".join(days)


def phase_html(phases: list[dict], artifacts: list[dict], derived: dict, evidence: dict[str,dict], commit: str) -> str:
    completed = set(derived["completed"])
    artifacts_by_id = {artifact["id"]: artifact for artifact in artifacts}
    current = derived.get("phase", "P0")
    next_id = derived["next"]
    out=[]
    for p in phases:
        members=[a for a in artifacts if a["phase"]==p["id"]]
        done=sum(a["id"] in completed for a in members)
        status="WIP" if done and done < p["count"] else "DONE" if done == p["count"] else "NOT STARTED"
        items=[]
        for a in members:
            aid=a["id"]; ev=evidence[aid]; is_done=aid in completed; is_next=aid==next_id
            label="DONE · FRONTIER" if is_done and aid==derived["frontier"] else "DONE" if is_done else "NEXT" if is_next else "NOT STARTED"
            cls="done" if is_done else "next" if is_next else "plan"
            exact_files=exact_files_for(a)
            exact_actual=[path for path in exact_files if path in ev["actual_files"]]
            kind="ACTUAL" if is_done and exact_actual else "PLANNED" if exact_files else "UNRESOLVED"
            exact_links="".join(f'<a class="file" href="{REPO_URL}/blob/{commit}/{esc(path)}">{esc(path)}</a>' for path in exact_actual)
            exact_links += "".join(f'<span class="file planned">{esc(path)}</span>' for path in exact_files if path not in exact_actual)
            if not exact_links: exact_links='<span class="file planned">UNRESOLVED</span>'
            dependency_files=dependency_files_for(a, artifacts_by_id)
            dependency_links="".join(f'<span class="file dependency">{esc(path)}</span>' for path in dependency_files) or '<span class="file dependency">None declared</span>'
            evidence_summary=", ".join(ev["actual_files"][:3]) if ev["actual_files"] else "none"
            if len(ev["actual_files"])>3: evidence_summary += f' · +{len(ev["actual_files"])-3} supporting files'
            directory=directory_for(a, exact_files)
            items.append(f'<details class="artifact-row {cls}" id="artifact-{aid}"><summary><span class="aid">{aid}</span><span class="artifact-copy"><strong>{esc(a["name"])}</strong><small>{esc(clean(a["purpose"]))}</small></span><span class="artifact-status"><b>{label}</b><small>{len(exact_actual)} exact file(s) · {esc(evidence_summary)}</small></span></summary><div class="artifact-detail"><div class="detail-grid"><div><label>Status</label><span>{label}</span></div><div><label>Manifest</label><span>{kind}</span></div><div><label>Roadmap</label><span>{p["id"]} / {aid}</span></div><div><label>Dependencies</label><span>{esc(clean(a["dependencies"]))}</span></div><div><label>Unlocks</label><span>{esc(clean(a["unlocks"]))}</span></div><div><label>Verification</label><span>UNVERIFIED</span></div></div><p><label>Description</label>{esc(clean(a["description"]))}</p><p><label>Purpose</label>{esc(clean(a["purpose"]))}</p><p><label>Exact Artifact files · repository-relative paths</label><span class="file-list">{exact_links}</span></p><p><label>Directory</label><code>{esc(directory)}</code></p><p><label>Dependency files · supporting inputs</label><span class="file-list">{dependency_links}</span></p><p><label>Repository evidence · not exact Artifact files</label><span class="file-list"><span class="file dependency">{esc(evidence_summary)}</span></span></p><p><label>Validation / exit</label>{esc(clean(a["validation"]))} · {esc(clean(a["done_condition"]))}</p><p><label>Blueprint · RMS</label>{esc(clean(a["blueprint"]))} · {esc(clean(a["rms"]))}</p></div></details>')
        out.append(f'<details class="phase-card {"current" if p["id"]==current else "done" if status=="DONE" else ""}" id="{p["id"]}" {"open" if p["id"]==current else ""}><summary><span class="phase-key">{p["id"]}</span><span><strong>{esc(p["name"])}</strong><small>{esc(p["purpose"])}</small></span><span class="phase-progress"><b>{done} / {p["count"]}</b><small>{done/p["count"]*100:.1f}% · {status}</small></span><span class="range">{p["start"]}–{p["end"]}</span></summary><div class="phase-body"><p class="phase-note">{esc(p["purpose"])} Dependencies are enforced by the Roadmap; phase exit remains separate from file existence.</p>{"".join(items)}</div></details>')
    return "".join(out)


def render_html(state: dict, events: list[dict], phases: list[dict], artifacts: list[dict], evidence: dict[str,dict], derived: dict) -> str:
    completed_set=set(derived["completed"])
    completed=len(completed_set); total=state["roadmap_total"]
    current_phase_id=derived.get("phase") or phases[0]["id"]
    current_phase=next(p for p in phases if p["id"]==current_phase_id)
    current_done=sum(a["id"] in completed_set for a in artifacts if a["phase"]==current_phase["id"])
    current_phase_note=f'{current_phase["id"]} hiện có {current_done}/{current_phase["count"]} artifacts theo repository evidence; phase exit vẫn là formal condition riêng.'
    def phase_table_row(p):
        done=sum(a["id"] in completed_set for a in artifacts if a["phase"]==p["id"])
        status="DONE" if done==p["count"] else "WIP" if done else "NOT STARTED"
        return f'<tr><td><strong>{p["id"]}</strong><br>{esc(p["name"])}</td><td>{esc(p["purpose"])}</td><td><code>{p["start"]}–{p["end"]}</code></td><td class="status-{status.lower().replace(" ","-")}">{status}</td><td>{done} / {p["count"]}</td></tr>'
    phase_table="".join(phase_table_row(p) for p in phases)
    def phase_dot(p):
        done = sum(a["id"] in completed_set for a in artifacts if a["phase"] == p["id"])
        status_class = "done" if done == p["count"] else "current" if p["id"] == current_phase_id else ""
        return f'<a class="phase-dot {status_class}" href="#{p["id"]}">{p["id"]}<small>{done/p["count"]*100:.1f}%</small></a>'
    strip="".join(phase_dot(p) for p in phases)
    log_html=timeline_html(events,derived); phases_html=phase_html(phases,artifacts,derived,evidence,state["repository_commit"])
    commit=state["repository_commit"]
    if derived["next"] == "freeze":
        next_trace = '<p><label>Manifest</label><strong>FREEZE</strong></p><p>Không còn artifact kế tiếp trong Roadmap.</p>'
    else:
        next_row=next(a for a in artifacts if a["id"]==derived["next"])
        planned_path=clean(next_row.get("planned_path",""))
        next_kind="PLANNED" if planned_path else "UNRESOLVED"
        next_links=f'<span class="file planned">{esc(planned_path or "UNRESOLVED")}</span>'
        next_directory=directory_for(next_row, exact_files_for(next_row))
        next_dependency_files=dependency_files_for(next_row, {artifact["id"]: artifact for artifact in artifacts})
        next_dependency_links="".join(f'<span class="file dependency">{esc(path)}</span>' for path in next_dependency_files) or '<span class="file dependency">None declared</span>'
        next_trace=f'<p><label>Artifact</label><strong>{esc(clean(next_row.get("name","")))}</strong></p><p><label>Description</label>{esc(clean(next_row.get("description",next_row.get("validation",""))))}</p><p><label>Purpose</label>{esc(clean(next_row.get("purpose","")))}</p><p><label>Manifest</label><strong>{next_kind}</strong></p><p><label>Exact Artifact files · repository-relative paths</label><span class="file-list">{next_links}</span></p><p><label>Directory</label><code>{esc(next_directory)}</code></p><p><label>Dependency files · supporting inputs</label><span class="file-list">{next_dependency_links}</span></p><p><label>Dependencies · unlocks</label>{esc(clean(next_row.get("dependencies","—")))} · {esc(clean(next_row.get("unlocks","—")))}</p><p><label>Validation / done condition</label>{esc(clean(next_row.get("validation","")))} · {esc(clean(next_row.get("done_condition","")))}</p>'
    template=HTML_TEMPLATE
    replacements={"__UPDATED__":esc(state.get("last_updated_at",state.get("updated_at",""))),"__FRONTIER__":esc(derived["frontier"] or "—"),"__NEXT__":esc(derived["next"]),"__COMPLETED__":str(completed),"__TOTAL__":str(total),"__OVERALL__":f"{completed/total*100:.1f}%","__CURRENT_PHASE__":esc(current_phase["id"]),"__CURRENT_PHASE_NAME__":esc(current_phase["name"]),"__CURRENT_PHASE_DONE__":str(current_done),"__CURRENT_PHASE_COUNT__":str(current_phase["count"]),"__CURRENT_PHASE_PCT__":f"{current_done/current_phase['count']*100:.1f}%","__CURRENT_PHASE_LEFT__":str(current_phase["count"]-current_done),"__CURRENT_PHASE_NOTE__":esc(current_phase_note),"__STRIP__":strip,"__PHASE_TABLE__":phase_table,"__PHASES__":phases_html,"__LOG__":log_html,"__NEXT_TRACE__":next_trace,"__BRANCH__":esc(state["repository_branch"]),"__COMMIT__":esc(commit),"__COMMITS__":str(state["commit_count"]),"__FILES__":str(state["file_count"]),"__TESTS__":str(state["test_file_count"]),"__LOG_COUNT__":str(len(events)),"__REPO__":REPO_URL}
    for key,value in replacements.items(): template=template.replace(key,value)
    return template


HTML_TEMPLATE='''<!doctype html><html lang="vi" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>COOLBOY12 PROGRESS</title><style>
:root{--bg:#f5f6f8;--paper:#fff;--soft:#edf0f4;--ink:#17202b;--muted:#637080;--line:#d5dae2;--blue:#3159c7;--green:#2e7a52;--amber:#a96f10;--red:#b0453e}:root[data-theme=dark]{--bg:#14181e;--paper:#1c222a;--soft:#252c35;--ink:#edf1f5;--muted:#a5b0bd;--line:#343d49;--blue:#90a8ff;--green:#70ca97;--amber:#e5ad51;--red:#ed9186}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}.wrap{max-width:900px;margin:auto;padding:0 24px 72px}h1,h2,h3{font-family:Georgia,"Times New Roman",serif;letter-spacing:-.025em}h1{font-size:clamp(2.5rem,7vw,4.55rem);line-height:.98;margin:0 0 17px}h2{font-size:clamp(1.65rem,4vw,2.4rem);line-height:1.12;margin:58px 0 15px;padding-top:24px;border-top:1px solid var(--line)}h3{font-size:1.2rem;line-height:1.25;margin:0 0 7px}p{max-width:75ch;margin:0 0 14px}a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}code,.mono,.file{font:12px/1.45 ui-monospace,SFMono-Regular,Consolas,monospace}.mast{padding:42px 0 26px;border-bottom:2px solid var(--ink);display:flex;justify-content:space-between;align-items:flex-end;gap:22px}.eyebrow{display:flex;gap:16px;flex-wrap:wrap;color:var(--muted);font:600 10px/1.3 ui-monospace;letter-spacing:.1em;text-transform:uppercase}.dek{color:var(--muted);max-width:70ch;font-size:1.06rem}.tools{display:flex;gap:7px;flex-shrink:0}button{border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:4px;padding:8px 10px;cursor:pointer;font:600 10px ui-monospace}.toc{position:sticky;top:0;z-index:4;display:flex;gap:7px;overflow:auto;white-space:nowrap;padding:10px 0;background:color-mix(in srgb,var(--bg) 93%,transparent);backdrop-filter:blur(7px);border-bottom:1px solid var(--line)}.toc a{background:var(--paper);border:1px solid var(--line);padding:5px 8px;border-radius:3px;font:600 10px ui-monospace;color:var(--muted)}.stats{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:5px;overflow:hidden;margin:24px 0 15px}.stat{background:var(--paper);padding:16px;min-height:102px}.n{display:block;font:750 clamp(1.5rem,4.5vw,2.3rem)/1.05 ui-monospace;letter-spacing:-.05em}.stat small{display:block;color:var(--muted);font-size:12px;line-height:1.4;margin-top:8px}.blue{color:var(--blue)}.amber{color:var(--amber)}.green{color:var(--green)}.callout,.card{background:var(--paper);border:1px solid var(--line);border-radius:5px;padding:17px;box-shadow:0 12px 30px -24px #111}.callout{border-left:4px solid var(--amber);background:color-mix(in srgb,var(--paper) 78%,#f5d99d);margin-bottom:20px}.label,label{display:block;color:var(--muted);font:700 10px/1.3 ui-monospace;letter-spacing:.1em;text-transform:uppercase;margin-bottom:5px}.phase-strip{display:grid;grid-template-columns:repeat(19,1fr);gap:4px;margin:19px 0}.phase-dot{background:var(--paper);border:1px solid var(--line);border-radius:3px;padding:8px 2px 6px;text-align:center;color:var(--muted);font:700 10px ui-monospace}.phase-dot.current{color:var(--amber);border-color:var(--amber);background:#fbefd5;box-shadow:inset 0 -5px var(--amber)}.phase-dot.done{color:var(--green);border-color:var(--green);background:color-mix(in srgb,var(--paper) 82%,var(--green));box-shadow:inset 0 -5px var(--green)}.phase-dot small{display:block;font-size:8px;margin-top:5px}.position,.two{display:grid;grid-template-columns:1.15fr 1fr;gap:13px}.card{border-top:4px solid var(--blue)}.card.current{border-top-color:var(--amber)}.card p{color:var(--muted);font-size:14px}.architecture{display:grid;gap:0;margin:18px 0 22px}.arch{display:grid;grid-template-columns:140px 22px 1fr;gap:12px;align-items:center;background:var(--paper);border:1px solid var(--line);border-bottom:0;padding:13px 15px}.arch:first-child{border-radius:5px 5px 0 0}.arch:last-child{border-bottom:1px solid var(--line);border-radius:0 0 5px 5px}.arch b{font:750 11px ui-monospace;color:var(--blue);letter-spacing:.1em}.arch p{margin:0;color:var(--muted);font-size:13.5px}.models{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}.model{background:var(--paper);border:1px solid var(--line);border-top:3px solid var(--blue);padding:12px;border-radius:4px}.model b{font:750 1.7rem ui-monospace;color:var(--blue)}.model strong{display:block;margin:5px 0;font-family:Georgia}.model small{color:var(--muted);font-size:11.5px;line-height:1.35}.report-table{width:100%;border-collapse:collapse;background:var(--paper);border:1px solid var(--line);font-size:13px}.report-table th,.report-table td{padding:10px 11px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.report-table th{background:var(--soft);font:700 10px ui-monospace;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}.report-table tr:last-child td{border-bottom:0}.spine{max-width:390px;margin:16px auto}.spine div{background:var(--paper);border:1px solid var(--line);border-bottom:0;text-align:center;padding:8px;font:750 12px ui-monospace;color:var(--blue)}.spine div:last-child{border-bottom:1px solid var(--line)}.repo{border-top:3px solid var(--green)}.foot{margin-top:60px;border-top:2px solid var(--ink);padding-top:20px;color:var(--muted);font-size:12.5px}.phase-card{background:var(--paper);border:1px solid var(--line);border-radius:5px;margin:9px 0;overflow:hidden}.phase-card.current{border-left:4px solid var(--amber)}.phase-card.done{border-left:4px solid var(--green)}.phase-card.done .phase-key,.phase-card.done summary strong,.phase-card.done .phase-progress{color:var(--green)}.phase-card>summary{display:grid;grid-template-columns:46px 1fr auto auto;gap:12px;align-items:center;padding:14px;cursor:pointer;list-style:none}.phase-card>summary::-webkit-details-marker,.artifact-row>summary::-webkit-details-marker,.day-node>summary::-webkit-details-marker{display:none}.phase-key{font:750 12px ui-monospace;color:var(--blue)}.phase-card summary strong{font-family:Georgia;font-size:1.07rem}.phase-card summary small{display:block;color:var(--muted);font-size:11.5px;line-height:1.35;margin-top:3px}.phase-progress{text-align:right;white-space:nowrap}.phase-progress b{font:750 12px ui-monospace}.range{color:var(--muted);font:700 11px ui-monospace;white-space:nowrap}.phase-body{border-top:1px solid var(--line);padding:12px 14px 15px}.phase-note{color:var(--muted);font-size:13px;margin-bottom:12px}.artifact-row{border-top:1px solid var(--line);margin-top:6px}.artifact-row>summary{display:grid;grid-template-columns:42px 1fr auto;gap:10px;align-items:center;cursor:pointer;list-style:none;padding:10px 0}.artifact-row.next{border-left:3px solid var(--amber);padding-left:8px}.artifact-row.plan{opacity:.78}.aid{font:750 12px ui-monospace;color:var(--blue)}.artifact-copy strong{display:block;font-size:13.5px}.artifact-copy small,.artifact-status small{display:block;color:var(--muted);font-size:11.5px;line-height:1.35;margin-top:2px}.artifact-status{text-align:right}.artifact-status b{font:750 10px ui-monospace;color:var(--green)}.artifact-row.next .artifact-status b{color:var(--amber)}.artifact-row.plan .artifact-status b{color:var(--muted)}.artifact-row.done .artifact-status b{color:var(--green)}.artifact-row.done .aid,.artifact-row.done .artifact-copy strong{color:var(--green)}.report-table .status-done{color:var(--green);font-weight:700}.artifact-detail{background:var(--soft);border-radius:4px;padding:12px;margin:0 0 10px}.detail-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:7px;margin-bottom:12px}.detail-grid>div{background:var(--paper);padding:8px;border-radius:3px}.detail-grid span{font-size:12px;line-height:1.35}.file-list{display:flex;flex-wrap:wrap;gap:5px}.file{display:inline-block;background:var(--paper);border:1px solid var(--line);padding:4px 6px;border-radius:3px;overflow-wrap:anywhere}.file.planned{color:var(--amber)}.file.dependency{color:var(--muted);border-style:dashed}.empty-log{background:var(--paper);border:1px dashed var(--line);padding:22px 18px;color:var(--muted);border-radius:5px}.day-node{border-bottom:1px solid var(--line);padding:17px 0}.day-node>summary{display:grid;grid-template-columns:160px 1fr auto;gap:14px;align-items:baseline;cursor:pointer;list-style:none}.day-date{font:750 14px Georgia;color:var(--ink);letter-spacing:.04em}.day-count{color:var(--muted);font-size:13px}.day-count b{color:var(--green);font-weight:700}.day-overall{color:var(--muted);font:11px ui-monospace;white-space:nowrap}.day-events{border-left:2px solid var(--line);margin:14px 0 0 10px;padding-left:18px}.log-event{display:grid;grid-template-columns:68px 22px 1fr;gap:7px;align-items:start;min-height:42px;position:relative}.log-event time{font:700 11px ui-monospace;color:var(--muted);padding-top:1px}.event-dot{color:var(--blue);font-size:14px;line-height:1}.log-event strong{font-size:14px;font-weight:700}.log-event small{display:block;color:var(--muted);font-size:11px;margin-top:2px}.log-event code{background:var(--soft);border:1px solid var(--line);border-radius:3px;padding:1px 4px;overflow-wrap:anywhere}.event-files{margin-top:5px;line-height:1.85}.event-files .more{color:var(--muted);font:10px ui-monospace;letter-spacing:.06em;white-space:nowrap}.implement-note{color:var(--muted);font-size:13px;max-width:72ch}.event-pill{display:inline-block;padding:3px 7px;border:1px solid var(--line);border-radius:3px;color:var(--muted);font:10px ui-monospace}@media print{.tools,.toc{display:none!important}body{background:#fff}.phase-card,.artifact-row,.card,.day-node{break-inside:avoid}}@media(max-width:760px){.mast,.position,.two{display:block}.tools{margin-top:16px}.stats{grid-template-columns:repeat(2,1fr)}.phase-strip{grid-template-columns:repeat(10,1fr)}.models{grid-template-columns:repeat(3,1fr)}.detail-grid{grid-template-columns:repeat(2,1fr)}.phase-card>summary{grid-template-columns:40px 1fr auto}.range{grid-column:2;grid-row:2}.phase-progress{grid-column:3;grid-row:1/3}.day-node>summary{grid-template-columns:1fr}.day-overall{white-space:normal}.day-events{margin-left:0;padding-left:12px}}@media(max-width:500px){.wrap{padding:0 14px 60px}.stats{grid-template-columns:1fr 1fr}.phase-strip{grid-template-columns:repeat(5,1fr)}.models{grid-template-columns:repeat(2,1fr)}.phase-card>summary{grid-template-columns:37px 1fr}.phase-progress,.range{grid-column:2;text-align:left;grid-row:auto}.artifact-row>summary{grid-template-columns:37px 1fr}.artifact-status{grid-column:2;text-align:left}.detail-grid{grid-template-columns:1fr}.day-events{padding-left:9px}.log-event{grid-template-columns:58px 16px 1fr}.log-event strong{font-size:13px}.event-files{line-height:2}}
</style></head><body><div class="wrap" id="top"><header class="mast"><div><div class="eyebrow"><span>COOLBOY12 · Living Progress Report</span><span>Updated __UPDATED__</span><span>Frontier · Artifact __FRONTIER__</span></div><h1>COOLBOY12<br>PROGRESS</h1><p class="dek">Báo cáo editorial về <strong>tiến độ xây dựng</strong>, kiến trúc và đường trace từ artifact tới file. Progress state là nguồn live; Blueprint, RMS, Roadmap và repository giữ vai trò nguồn sự thật tương ứng.</p></div></header><nav class="toc"><a href="#progress">Tiến độ</a><a href="#architecture">Kiến trúc</a><a href="#roadmap">Roadmap</a><a href="#__CURRENT_PHASE__">__CURRENT_PHASE__ detail</a><a href="#next">Tiếp theo</a><a href="#repo">Evidence</a><a href="#implement-log">Implement Log</a></nav>
<section id="progress"><div class="stats"><div class="stat"><span class="n blue">__COMPLETED__ / __TOTAL__</span><small>Artifact hoàn tất theo repository evidence</small></div><div class="stat"><span class="n blue">__OVERALL__</span><small>Tiến độ toàn roadmap</small></div><div class="stat"><span class="n amber">__CURRENT_PHASE__ · __CURRENT_PHASE_DONE__ / __CURRENT_PHASE_COUNT__</span><small>__CURRENT_PHASE_NAME__ · __CURRENT_PHASE_PCT__</small></div><div class="stat"><span class="n amber">__CURRENT_PHASE_LEFT__</span><small>Artifact còn lại trong __CURRENT_PHASE__</small></div></div><div class="callout"><span class="label">Where are we?</span><p><strong>COOLBOY12 đang ở Phase __CURRENT_PHASE__ — __CURRENT_PHASE_NAME__.</strong> Current frontier là <strong>Artifact __FRONTIER__</strong>; artifact kế tiếp là <strong>__NEXT__</strong>. __CURRENT_PHASE_NOTE__</p></div><div class="phase-strip">__STRIP__</div><div class="position"><article class="card current"><span class="label">Current frontier</span><h3>Artifact __FRONTIER__</h3><p>Completion is derived from repository evidence — an artifact commit and a tracked file at its Roadmap path — not from declared state. That is evidence of build, not a verification claim; formal exit proof is shown separately below.</p></article><article class="card"><span class="label">Next target</span><h3>Artifact __NEXT__</h3><p>The next artifact may advance only after sequential validation, implementation evidence and required checks pass.</p></article></div></section>
<section id="architecture"><h2>COOLBOY12 được xây như thế nào?</h2><p>Đọc đúng tiến độ cần giữ năm lớp khác nhau. <strong>Blueprint</strong> định nghĩa điều phải đúng; <strong>RMS</strong> chia semantic ownership; <strong>Roadmap</strong> đặt construction order; <strong>Artifact</strong> là build unit; <strong>Repository</strong> cho biết điều gì vật lý tồn tại.</p><div class="architecture"><div class="arch"><b>BLUEPRINT</b><span>↓</span><p><strong>What must be true?</strong> Vision, Spine, Canon boundary và các luật của hệ thống.</p></div><div class="arch"><b>RMS</b><span>↓</span><p><strong>How is ownership divided?</strong> Sáu Record Models sovereign, không có model thứ bảy.</p></div><div class="arch"><b>ROADMAP</b><span>↓</span><p><strong>What gets built and in what order?</strong> __TOTAL__ artifacts, 19 phases, dependencies, gates, validation và exit conditions.</p></div><div class="arch"><b>ARTIFACT</b><span>↓</span><p><strong>What concrete unit gets built?</strong> Name, purpose, path, dependency và điều kiện hoàn tất.</p></div><div class="arch"><b>REPOSITORY</b><span>·</span><p><strong>What physically exists?</strong> Actual paths, directory footprint, commit evidence và verification state.</p></div></div><div class="callout"><span class="label">Fact / plan / evidence</span><p>Roadmap nói Artifact __NEXT__ phải tồn tại <strong>không có nghĩa</strong> Artifact __NEXT__ đã tồn tại. File tồn tại <strong>không có nghĩa</strong> artifact đã VERIFIED. Report giữ ba lớp này tách biệt.</p></div><h3>Sáu Record Models theo RMS</h3><div class="models"><div class="model"><b>W</b><strong>World</strong><small>What is true of the world?</small></div><div class="model"><b>E</b><strong>Epistemic</strong><small>Who knows, believes or has been shown what?</small></div><div class="model"><b>P</b><strong>Production</strong><small>What is intended, planned and in production?</small></div><div class="model"><b>R</b><strong>Registry</strong><small>What does the system mean?</small></div><div class="model"><b>V</b><strong>Visual</strong><small>How is World Truth represented?</small></div><div class="model"><b>I</b><strong>Issue</strong><small>What was published?</small></div></div></section>
<section id="roadmap"><h2>Roadmap · 19 phases, __TOTAL__ artifacts</h2><p>Roadmap là construction order, không phải progress state. Nó ràng buộc dependencies, gates, validation và exit conditions. Phase table giữ range chính xác, còn drill-down được generate cho đủ toàn bộ __TOTAL__ artifact.</p><div style="overflow:auto"><table class="report-table"><thead><tr><th>Phase</th><th>Purpose</th><th>Artifact range</th><th>Status</th><th>Progress</th></tr></thead><tbody>__PHASE_TABLE__</tbody></table></div></section>
<section id="__CURRENT_PHASE__"><h2>Phase drill-down · click to reveal</h2><p>Phase <strong>__CURRENT_PHASE__</strong> mở mặc định vì là current phase; các phase còn lại đóng mặc định. Mỗi phase chứa đúng range Roadmap tương ứng. Artifact details chỉ mở khi cần để giữ progress-first.</p>__PHASES__</section>
<section id="next"><h2>Tiếp theo · Artifact __NEXT__</h2><div class="card current"><span class="label">NEXT · chưa được tính là completed</span><h3>Artifact __NEXT__</h3><p>Progress advances only through the live state and safe validation workflow. A user prompt creates activity; it does not create completion.</p>__NEXT_TRACE__<p><strong>One publishing command:</strong> <code>/coolboy12-update</code>. It reads progress state, implement log, Roadmap and repository evidence, then regenerates this HTML without an artifact argument and without committing.</p></div></section>
<section id="repo"><h2>Repository evidence · supporting context</h2><div class="two"><article class="card repo"><span class="label">Repository fact</span><h3><a href="__REPO__/tree/__COMMIT__">coolboy12-offical</a></h3><p>Branch <code>__BRANCH__</code><br>Commit <code>__COMMIT__</code><br>__COMMITS__ commits · __FILES__ tracked files · __TESTS__ test files</p></article></div></section>
<section id="implement-log"><h2>Implement Log</h2><div class="timeline">__LOG__</div></section>
</div></body></html>'''


def main() -> int:
    ap=argparse.ArgumentParser(description="Publish COOLBOY12 progress report from live state")
    ap.add_argument("--render", action="store_true", help="publish HTML without advancing completion")
    ap.add_argument("--html", default=str(HTML_PATH), help="canonical report path")
    args=ap.parse_args()
    if not CONTRACT_PATH.exists() or "HTML_UPDATE_CONTRACT_VERSION = 1.1" not in CONTRACT_PATH.read_text(encoding="utf-8"):
        raise RuntimeError("Pre-flight refused: reports/HTML_UPDATE_CONTRACT.md version 1.1 is required")
    phases, artifacts=parse_roadmap()
    state=repo_facts(validate_state_against_roadmap(load_state(), artifacts))
    load_log()  # pre-flight: refuses a malformed implement-log.json, not a render input
    tracked=tracked_files()
    evidence={a["id"]:evidence_for(a,tracked) for a in artifacts}
    commits=artifact_commits()
    derived=derive_completion(artifacts,tracked,commits)
    events=build_events(artifacts,commits,derived,tracked)
    if not args.render:
        print("Use /coolboy12-update or scripts/update_progress.py --render to publish the report; no artifact argument is accepted.", file=sys.stderr)
        return 2
    output_path = Path(args.html)
    if output_path != HTML_PATH:
        raise RuntimeError(f"Refused: canonical HTML must be {HTML_PATH}")
    HTML_PATH.write_text(render_html(state,events,phases,artifacts,evidence,derived), encoding="utf-8")
    completed=len(derived["completed"])
    phase_of={a["id"]:a["phase"] for a in artifacts}
    phase_id=phase_of.get(derived["frontier"],"P0")
    phase_done=sum(1 for aid in derived["completed"] if phase_of.get(aid)==phase_id)
    print("COOLBOY12 report updated.")
    print(f"Current frontier: Artifact {derived['frontier'] or '—'}  (repository evidence)")
    print(f"Overall: {completed} / 490 · {completed/490*100:.1f}%")
    print(f"Current phase: {phase_id} · {phase_done} artifacts")
    print(f"Implement Log: {len(events)} artifact commit(s) across {len(commits)} artifact(s)")
    # progress.json no longer decides completion; when it disagrees, say so
    # rather than letting two numbers circulate unexplained.
    declared=state.get("completed_artifacts",[])
    if len(declared)!=completed or state.get("current_frontier")!=derived["frontier"]:
        print(f"Note: reports/progress.json declares frontier {state.get('current_frontier')} "
              f"({len(declared)} complete); the report renders repository evidence.")
    if derived["evidenced_out_of_sequence"]:
        print(f"Note: evidence out of sequence, not counted: {', '.join(derived['evidenced_out_of_sequence'])}")
    print("No commit created.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
