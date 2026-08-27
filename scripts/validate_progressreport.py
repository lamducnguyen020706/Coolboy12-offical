#!/usr/bin/env python3
from pathlib import Path
import json, re, subprocess

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'reports/progressreport.html'
STATE=ROOT/'reports/progress.json'
LOG=ROOT/'reports/implement-log.json'
CONTRACT=ROOT/'reports/HTML_UPDATE_CONTRACT.md'
html=HTML.read_text(encoding='utf-8')
state=json.loads(STATE.read_text(encoding='utf-8'))
log=json.loads(LOG.read_text(encoding='utf-8'))
def _one(pattern):
    """The single match for a pattern that must appear exactly once."""
    found = re.findall(pattern, html)
    return found[0] if len(found) == 1 else None


def frontier_consistent():
    """The report's frontier agrees with itself and with its own next artifact.

    Pinning an expected frontier here is what made this check go stale: it was
    written against 021 and could never be right again. The frontier is derived
    from repository evidence (HTML_UPDATE_CONTRACT.md, "The completion
    predicate"), so what is checkable without re-deriving it is *coherence* —
    every place the report states the frontier states the same one, the next
    artifact is the one after it, and the phase named is a real phase.
    """
    masthead = _one(r'<span>Frontier · Artifact (\d{3})</span>')
    body = re.findall(
        r'Current frontier là <strong>Artifact (\d{3})</strong>; '
        r'artifact kế tiếp là <strong>(\d{3})</strong>', html)
    phase = _one(r'COOLBOY12 đang ở Phase (P\d+) —')
    if not masthead or len(body) != 1 or not phase:
        return False
    frontier, following = body[0]
    return (masthead == frontier
            and int(following) == int(frontier) + 1
            and f'<details class="phase-card current" id="{phase}"' in html)


def progress_math_consistent():
    """Percentages are recomputed from the counts the report itself prints.

    Same reasoning as above: a literal "4.3%" only ever validated one day's
    numbers. Checking the arithmetic catches the failure the literal was there
    to catch — a percentage that has drifted from its count — on every day.
    One decimal place is the contract's rounding; two would be a redesign.
    """
    overall = _one(r'<span class="n blue">(\d+) / 490</span>')
    phase_stat = re.findall(
        r'<span class="n amber">P\d+ · (\d+) / (\d+)</span><small>[^<]*· ([\d.]+)%</small>', html)
    if not overall or len(phase_stat) != 1:
        return False
    done, total, phase_pct = phase_stat[0]
    if f'{int(overall)/490*100:.1f}%' not in html:
        return False
    if phase_pct != f'{int(done)/int(total)*100:.1f}':
        return False
    return not re.search(r'\d+\.\d\d%', html)


checks={
 'contract_v1': 'HTML_UPDATE_CONTRACT_VERSION = 1.1' in CONTRACT.read_text(encoding='utf-8'),
 'canonical_path': HTML.exists(),
 'progress_schema': state.get('version')==1 and state.get('roadmap_total')==490,
 'frontier': frontier_consistent(),
 'progress_math': progress_math_consistent(),
 'phase_ids_19': len(re.findall(r'class="phase-dot',html))==19 and len(re.findall(r'class="phase-card',html))==19,
 'artifact_ids_490': len(re.findall(r'id="artifact-\d{3}"',html))==490,
 'ranges': all(x in html for x in ['001–030','031–038','039–059','060–124','125–144','145–166','167–174','175–218','219–230','231–252','253–295','296–342','343–360','361–380','381–396','397–413','414–439','440–462','463–490']),
 'p0_open': bool(re.search(r'<details class="phase-card current" id="P0" open>',html)),
 'implement_log_schema': log.get('version')==1 and log.get('timezone')=='Asia/Ho_Chi_Minh' and isinstance(log.get('events'),list),
 'implement_log_section': '<section id="implement-log">' in html and '<h2>Implement Log</h2>' in html and 'prompt event(s) · newest date first' not in html and 'today' not in html,
 'traceability': all(x in html for x in ['ACTUAL','PLANNED','Exact Artifact files · repository-relative paths','Dependency files · supporting inputs','Directory']) and '<section id="trace">' not in html and 'Artifact 022' in html,
 'dark_default': '<html lang="vi" data-theme="dark">' in html,
 'completed_green': '.phase-card.done' in html and '.artifact-row.done' in html and '.status-done' in html,
 'title': '<title>COOLBOY12 PROGRESS</title>' in html and '<h1>COOLBOY12<br>PROGRESS</h1>' in html,
 'no_ui_controls': 'Đổi sáng/tối' not in html and 'In A4' not in html and 'toggleTheme' not in html,
 'no_removed_footer': 'Generated presentation output. Live state:' not in html and 'Generated at 2026-08-24T00:00:00+07:00' not in html,
 'no_verification_card': 'Verification fact' not in html and 'UNVERIFIED ≠ missing' not in html,
 'responsive_css': '@media(max-width:760px)' in html and '@media(max-width:500px)' in html,
 'print_css': '@media print' in html,
 'no_old_canonical_in_repo': not any(ROOT.glob('coolboy12baocaotiendo_edited-1.html')),
}
for key,value in checks.items(): print(('PASS' if value else 'FAIL'), key)
if not all(checks.values()): raise SystemExit(1)
