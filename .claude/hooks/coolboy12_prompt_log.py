"""Claude Code UserPromptSubmit hook for COOLBOY12.

The hook records one activity event per user prompt and may advance only the
contiguous next artifact when a strong freeze/commit signal and Roadmap-backed
repository evidence are both present. Roadmap parsing is delegated to the
repository publisher helper; artifact definitions are never duplicated here.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TZ = dt.timezone(dt.timedelta(hours=7))


def find_root() -> Path:
    for key in ("CLAUDE_PROJECT_DIR", "CLAUDE_PROJECT_ROOT"):
        value = os.environ.get(key)
        if value:
            candidate = Path(value).expanduser().resolve()
            if (candidate / ".claude").is_dir() and (candidate / "reports").is_dir():
                return candidate
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / ".claude").is_dir() and (candidate / "reports").is_dir():
            return candidate
    return here.parents[2]


ROOT = find_root()
PROGRESS = ROOT / "reports" / "progress.json"
LOG = ROOT / "reports" / "implement-log.json"
PUBLISHER = ROOT / "scripts" / "update_progress.py"


def load_roadmap():
    spec = importlib.util.spec_from_file_location("coolboy12_update_progress", PUBLISHER)
    if spec is None or spec.loader is None:
        raise RuntimeError("Roadmap helper could not be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parse_roadmap(), module


def atomic_json(path: Path, data: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    tmp = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        json.loads(tmp.read_text(encoding="utf-8"))
        return tmp
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def atomic_pair_write(log_data: dict, progress_data: dict) -> None:
    log_tmp = atomic_json(LOG, log_data)
    progress_tmp = atomic_json(PROGRESS, progress_data)
    log_backup = LOG.with_suffix(LOG.suffix + ".bak")
    progress_backup = PROGRESS.with_suffix(PROGRESS.suffix + ".bak")
    try:
        if LOG.exists():
            shutil.copy2(LOG, log_backup)
        if PROGRESS.exists():
            shutil.copy2(PROGRESS, progress_backup)
        log_tmp.replace(LOG)
        progress_tmp.replace(PROGRESS)
    except Exception:
        if log_backup.exists():
            log_backup.replace(LOG)
        if progress_backup.exists():
            progress_backup.replace(PROGRESS)
        raise
    finally:
        log_tmp.unlink(missing_ok=True)
        progress_tmp.unlink(missing_ok=True)
        log_backup.unlink(missing_ok=True)
        progress_backup.unlink(missing_ok=True)


def payload_from_stdin() -> dict:
    try:
        raw = sys.stdin.read()
        value = json.loads(raw) if raw.strip() else {}
        return value if isinstance(value, dict) else {}
    except Exception as exc:
        print(f"COOLBOY12 hook warning: malformed payload ignored: {exc}", file=sys.stderr)
        return {}


def prompt_text(payload: dict) -> str:
    for key in ("prompt", "user_prompt", "message", "text"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, dict):
            for nested in ("content", "text", "prompt"):
                if isinstance(value.get(nested), str) and value[nested].strip():
                    return value[nested].strip()
    return ""


def received_timestamp(payload: dict) -> str:
    for key in ("prompt_received_at", "received_at", "timestamp"):
        value = payload.get(key)
        if isinstance(value, str):
            try:
                parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=TZ)
                return parsed.astimezone(TZ).isoformat(timespec="seconds")
            except ValueError:
                pass
    return dt.datetime.now(TZ).isoformat(timespec="seconds")


def summarize(prompt: str) -> str:
    if not prompt:
        return "Prompt received"
    first = re.sub(r"\s+", " ", re.split(r"\n+", prompt.strip())[0].strip())
    first = re.sub(r"^[-*#>\s]+", "", first)
    artifact = re.search(r"\bartifact\s+(\d{3})\b", first, re.I)
    aid = artifact.group(1) if artifact else ""
    if re.search(r"\b(draft|soạn thảo|tạo bản nháp)\b", first, re.I) and aid:
        return f"Draft artifact {aid}"
    if re.search(r"\b(patch|sửa|vá)\b", first, re.I) and aid:
        return f"Patch artifact {aid}"
    if re.search(r"\b(freeze|đóng băng)\b", first, re.I) and re.search(r"\b(commit|ghi commit)\b", first, re.I):
        return f"Freeze and commit {aid}".strip()
    phase = re.search(r"\bwhole\s+(p\d+)\b", first, re.I)
    if re.search(r"\b(audit|kiểm toán)\b", first, re.I) and phase:
        return f"Audit whole {phase.group(1).upper()}"
    for term, label in (("review", "Review activity"), ("rà soát", "Review activity"), ("test", "Validation activity"), ("validation", "Validation activity"), ("refactor", "Refactor activity"), ("research", "Research activity")):
        if re.search(rf"\b{term}\b", first, re.I):
            return label
    return "Prompt received"


def infer_artifact(prompt: str, artifacts: list[dict]) -> str | None:
    match = re.search(r"\bartifact\s+(\d{3})\b", prompt, re.I)
    aid = match.group(1) if match else None
    valid = {a["id"] for a in artifacts}
    return aid if aid in valid else None


def artifact_phase(artifact: str | None, artifacts: list[dict]) -> str | None:
    if not artifact:
        return None
    return next((a["phase"] for a in artifacts if a["id"] == artifact), None)


def strong_completion_signal(prompt: str, artifact: str | None) -> bool:
    if not artifact:
        return False
    negative = re.search(r"\b(?:do not|don't|never|not|chưa|không)\b.{0,48}\b(?:freeze|commit|complete|completed|finish|finished|xong|hoàn tất)\b", prompt, re.I)
    if negative:
        return False
    has_freeze = bool(re.search(r"\b(freeze|đóng băng)\b", prompt, re.I))
    has_commit = bool(re.search(r"\b(commit|committed|ghi commit)\b", prompt, re.I))
    has_artifact = bool(re.search(rf"\bartifact\s+{re.escape(artifact)}\b", prompt, re.I))
    return has_freeze and has_commit and has_artifact


def working_files() -> set[str]:
    return {str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts}


def expected_next(progress: dict, artifacts: list[dict]) -> str:
    completed = progress.get("completed_artifacts", [])
    completed_set = set(completed)
    for artifact in artifacts:
        if artifact["id"] not in completed_set:
            return artifact["id"]
    return "freeze"


def evidence_supports_completion(artifact: str | None, progress: dict, artifacts: list[dict], publisher) -> bool:
    if not artifact or artifact != expected_next(progress, artifacts):
        return False
    row = next((a for a in artifacts if a["id"] == artifact), None)
    if row is None:
        return False
    tracked = set(publisher.tracked_files())
    present = tracked | working_files()
    planned = (row.get("planned_path") or "").strip().strip("`")
    actual = set(publisher.evidence_for(row, tracked).get("actual_files", []))
    if planned and planned not in {"/", "coolboy12/"}:
        if planned.endswith("/"):
            actual |= {path for path in present if path.startswith(planned)}
        elif planned in present:
            actual.add(planned)
    return bool(actual)


def recalculate_phases(progress: dict, phases: list[dict], artifacts: list[dict]) -> None:
    completed = set(progress.get("completed_artifacts", []))
    phase_state = progress.setdefault("phases", {})
    for phase in phases:
        phase_state[phase["id"]] = {
            "start": phase["start"],
            "end": phase["end"],
            "completed": sum(a["id"] in completed for a in artifacts if a["phase"] == phase["id"]),
        }


def stable_event_id(payload: dict, prompt: str) -> str:
    for key in ("event_id", "message_id", "id"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    session = str(payload.get("session_id") or payload.get("sessionId") or os.environ.get("CLAUDE_SESSION_ID") or "")
    return hashlib.sha256(f"{session}|{prompt}".encode("utf-8")).hexdigest()[:24]


def main() -> int:
    payload = payload_from_stdin()
    prompt = prompt_text(payload)
    timestamp = received_timestamp(payload)
    try:
        (phases, artifacts), publisher = load_roadmap()
        progress = json.loads(PROGRESS.read_text(encoding="utf-8"))
        log = json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else {"version": 1, "timezone": "Asia/Ho_Chi_Minh", "events": []}
        event_id = stable_event_id(payload, prompt)
        if any(event.get("event_id") == event_id for event in log.get("events", [])):
            return 0
        artifact = infer_artifact(prompt, artifacts)
        phase = artifact_phase(artifact, artifacts)
        summary = summarize(prompt)
        event = {"event_id": event_id, "timestamp": timestamp, "summary": summary, "artifact": artifact, "phase": phase, "type": "prompt", "source": "UserPromptSubmit", "completion_recorded": False}
        advanced = strong_completion_signal(prompt, artifact) and evidence_supports_completion(artifact, progress, artifacts, publisher)
        if advanced:
            next_id = expected_next(progress, artifacts)
            completed = progress.setdefault("completed_artifacts", [])
            if artifact != next_id or artifact in completed:
                advanced = False
            else:
                completed_before = len(completed)
                completed.append(artifact)
                progress["current_frontier"] = artifact
                following = expected_next(progress, artifacts)
                progress["next_artifact"] = following
                next_phase = artifact_phase(following if following != "freeze" else None, artifacts)
                progress["current_phase"] = next_phase or phase or progress.get("current_phase")
                event["completed_before"] = completed_before
                event["completed_after"] = len(completed)
                event["frontier_after"] = artifact
        event["completion_recorded"] = advanced
        log.setdefault("version", 1)
        log.setdefault("timezone", "Asia/Ho_Chi_Minh")
        log.setdefault("events", []).append(event)
        progress["last_updated_at"] = timestamp
        progress["current_activity"] = {"timestamp": timestamp, "summary": summary, "artifact": artifact, "phase": phase, "event_id": event_id, "completion_recorded": advanced}
        recalculate_phases(progress, phases, artifacts)
        atomic_pair_write(log, progress)
    except Exception as exc:
        print(f"COOLBOY12 hook warning: state update failed: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
