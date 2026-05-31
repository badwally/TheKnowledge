# M42 Review Consoles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Review sidebar entry to `wiki serve` with four tabs (Drafts, Contradictions, Orphans, Filter-band). Drafts and Filter-band have inline actions; Contradictions and Orphans are read-only with click-through. Adds structured contradiction persistence (`apply_plan` writes JSONL) so Contradictions tab has a queryable data source.

**Architecture:** Reuses the M40 FastAPI + React + sync-op-endpoint foundation. New backend module `gateway.web.routes.review`. New frontend pages under `web/src/pages/review/`. M38's `apply_plan` gains one append-only JSONL write when contradictions are present. No new TaskStore use, no orchestrator changes — read + click-through only.

**Tech Stack:** Python 3.11+, FastAPI, Pydantic, pytest. React 18, TypeScript, Vite. Existing `gateway.ops.apply_plan`, `gateway.ops.finalize`, `gateway.ops.filter_correct`, `gateway.filter.policy`, `gateway.frontmatter`.

**Spec reference:** `docs/superpowers/specs/2026-05-04-m42-review-consoles-design.md`

---

### Task 1: JSONL contradiction persistence in apply_plan

**Files:**
- Create: `src/gateway/contradictions_log.py` (new helper module)
- Modify: `src/gateway/ops/apply_plan.py` (call helper inside Phase 2)
- Test: `tests/gateway/test_authorship.py` (extend with 1 new test)

- [ ] **Step 1: Write the failing test**

Append to `/Users/andrewgrant/code/knowledge/tests/gateway/test_authorship.py`:

```python
def test_apply_plan_writes_contradictions_to_jsonl(kb_root, make_source):
    """When plan.contradictions is non-empty, apply_plan appends one JSONL record per contradiction."""
    import json as _json
    from gateway import paths

    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="contradictions persistence test",
        updates=[
            _make_concept_update("jsonl-test-concept", "yt-applyTest1A"),
        ],
        contradictions=[
            Contradiction(
                existing_page="wiki/concepts/old.md",
                existing_claim="Original claim text",
                new_claim="Conflicting claim text",
                source_id="yt-applyTest1A",
                severity="major",
            ),
            Contradiction(
                existing_page="wiki/concepts/other.md",
                existing_claim="Another original claim",
                new_claim="Another conflicting claim",
                source_id="yt-applyTest1A",
                severity="minor",
            ),
        ],
    )
    result = apply_plan(plan)
    assert result.success, result.errors

    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    assert log_path.is_file()

    lines = [
        line for line in log_path.read_text().splitlines() if line.strip()
    ]
    assert len(lines) == 2
    records = [_json.loads(line) for line in lines]
    assert records[0]["source_id"] == "yt-applyTest1A"
    assert records[0]["existing_page"] == "wiki/concepts/old.md"
    assert records[0]["severity"] == "major"
    assert "recorded_at" in records[0]
    assert records[1]["severity"] == "minor"


def test_apply_plan_no_jsonl_write_when_no_contradictions(kb_root, make_source):
    """Plans without contradictions don't create the JSONL file."""
    from gateway import paths

    _seed_source(kb_root, make_source)
    plan = Plan(
        source_id="yt-applyTest1A",
        rationale="no contradictions",
        updates=[
            _make_concept_update("no-contradictions-concept", "yt-applyTest1A"),
        ],
    )
    result = apply_plan(plan)
    assert result.success

    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    # Either the file doesn't exist, or exists with no contradiction lines
    if log_path.is_file():
        lines = [l for l in log_path.read_text().splitlines() if l.strip()]
        assert lines == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_apply_plan_writes_contradictions_to_jsonl tests/gateway/test_authorship.py::test_apply_plan_no_jsonl_write_when_no_contradictions -v`

Expected: FAIL — first test fails because the JSONL file isn't written; second passes incidentally (no file, no-op).

- [ ] **Step 3: Create the contradictions_log helper**

Create `/Users/andrewgrant/code/knowledge/src/gateway/contradictions_log.py`:

```python
"""Append-only JSONL log of authorship contradictions (M42).

Each line is one Contradiction record with a `recorded_at` timestamp.
The Review console's Contradictions tab reads this log; M38's
apply_plan writes to it on every successful plan that has contradictions.

POSIX guarantees writes < PIPE_BUF (~4KB) appended via O_APPEND are
atomic; each record fits well under 4KB. No locking needed.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Iterable, TYPE_CHECKING

from gateway import paths

if TYPE_CHECKING:
    from gateway.plan import Contradiction


def log_path():
    return paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"


def append_contradictions(contradictions: "Iterable[Contradiction]") -> int:
    """Append one JSONL record per contradiction. Returns count appended."""
    items = list(contradictions)
    if not items:
        return 0

    target = log_path()
    target.parent.mkdir(parents=True, exist_ok=True)

    recorded_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with target.open("a", encoding="utf-8") as f:
        for c in items:
            record = {
                "source_id": c.source_id,
                "existing_page": c.existing_page,
                "existing_claim": c.existing_claim,
                "new_claim": c.new_claim,
                "severity": c.severity,
                "recorded_at": recorded_at,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(items)


def read_records() -> list[dict]:
    """Read all records from the log. Tolerates malformed lines (skips them).

    Returns records sorted by `recorded_at` descending (newest first).
    """
    target = log_path()
    if not target.is_file():
        return []
    out: list[dict] = []
    for line in target.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            out.append(obj)
    out.sort(key=lambda r: r.get("recorded_at", ""), reverse=True)
    return out
```

- [ ] **Step 4: Wire into apply_plan**

Modify `/Users/andrewgrant/code/knowledge/src/gateway/ops/apply_plan.py`. Add import near the existing imports (e.g., near `from gateway import frontmatter as fm`):

```python
from gateway import contradictions_log
```

Inside the `with file_lock(_LOCK_NAME):` block in Phase 2, BEFORE the existing `log.append(op="wiki-author", ...)` call, add:

```python
        # M42: persist contradictions to JSONL log for the Review console.
        if plan.contradictions:
            contradictions_log.append_contradictions(plan.contradictions)
```

The current location: in `apply_plan.py` around line 122 (between the `_record_backlinks` call and the `log.append` call). Insert the JSONL write between them, still inside the `with file_lock` block.

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_authorship.py::test_apply_plan_writes_contradictions_to_jsonl tests/gateway/test_authorship.py::test_apply_plan_no_jsonl_write_when_no_contradictions -v`

Expected: Both pass.

- [ ] **Step 6: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`

Expected: 517+ pass (515 + 2 new), no regressions.

- [ ] **Step 7: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/contradictions_log.py src/gateway/ops/apply_plan.py tests/gateway/test_authorship.py && git commit -m "feat(m42): persist authorship contradictions to .knowledge/contradictions/log.jsonl"
```

---

### Task 2: Drafts endpoint

**Files:**
- Create: `src/gateway/web/routes/review.py`
- Modify: `src/gateway/web/schemas.py`
- Modify: `src/gateway/web/app.py`
- Test: `tests/gateway/test_web_review.py` (new)

- [ ] **Step 1: Write failing tests**

Create `/Users/andrewgrant/code/knowledge/tests/gateway/test_web_review.py`:

```python
"""Tests for M42 Review console endpoints."""

from __future__ import annotations

import pytest
import yaml
from fastapi.testclient import TestClient

from gateway import frontmatter as fm
from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    return TestClient(create_app())


def _seed_draft(slug, *, type_dir, draft_started_at, claims_count=0):
    """Write a draft wiki page under wiki/<type_dir>/<slug>.md."""
    path = paths.wiki_dir() / type_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": type_dir.rstrip("s"),  # "concepts" → "concept", "entities" → "entity"
        "slug": slug,
        "draft": True,
        "draft_started_at": draft_started_at,
        "draft_unresolved_claims": claims_count,
    }
    body = f"# {slug}\n\nplaceholder\n"
    path.write_text(fm.serialize(front, body))


def test_drafts_empty_when_no_drafts(client, kb_root):
    resp = client.get("/api/review/drafts")
    assert resp.status_code == 200
    assert resp.json() == []


def test_drafts_returns_drafts_sorted_oldest_first(client, kb_root):
    _seed_draft("recent", type_dir="concepts",
                draft_started_at="2026-05-04T00:00:00Z", claims_count=2)
    _seed_draft("ancient", type_dir="synthesis",
                draft_started_at="2026-04-01T00:00:00Z", claims_count=5)
    _seed_draft("middle", type_dir="entities",
                draft_started_at="2026-04-25T00:00:00Z", claims_count=0)

    resp = client.get("/api/review/drafts")
    assert resp.status_code == 200
    drafts = resp.json()
    assert len(drafts) == 3
    # Oldest first
    assert drafts[0]["slug"] == "ancient"
    assert drafts[1]["slug"] == "middle"
    assert drafts[2]["slug"] == "recent"
    # Path includes wiki/ prefix
    assert drafts[0]["path"].startswith("wiki/synthesis/ancient")
    # age_days populated and >= 0
    assert drafts[0]["age_days"] >= drafts[1]["age_days"]


def test_drafts_skips_non_draft_pages(client, kb_root):
    # A non-draft page should not appear
    path = paths.wiki_dir() / "concepts" / "non-draft.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm.serialize(
        {"type": "concept", "slug": "non-draft"},
        "## Summary\n\nx\n",
    ))
    _seed_draft("is-draft", type_dir="concepts", draft_started_at="2026-04-01T00:00:00Z")

    resp = client.get("/api/review/drafts")
    drafts = resp.json()
    slugs = [d["slug"] for d in drafts]
    assert "is-draft" in slugs
    assert "non-draft" not in slugs
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`

Expected: 3 failures (404 — endpoint doesn't exist).

- [ ] **Step 3: Add schemas**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/schemas.py`:

```python
class DraftSummary(BaseModel):
    path: str
    type: str
    slug: str
    draft_started_at: str
    draft_unresolved_claims: int = 0
    age_days: float = 0.0
```

- [ ] **Step 4: Create review router**

Create `/Users/andrewgrant/code/knowledge/src/gateway/web/routes/review.py`:

```python
"""Review console endpoints (M42)."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter

from gateway import frontmatter as fm
from gateway import paths
from gateway.web.schemas import DraftSummary


router = APIRouter(prefix="/api/review", tags=["review"])


_DRAFT_TYPE_DIRS = ("entities", "concepts", "synthesis", "mocs")


@router.get("/drafts", response_model=list[DraftSummary])
def list_drafts() -> list[DraftSummary]:
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return []
    out: list[DraftSummary] = []
    now = datetime.now(timezone.utc)
    for type_dir in _DRAFT_TYPE_DIRS:
        d = wiki / type_dir
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            if not front.get("draft"):
                continue
            started = str(front.get("draft_started_at") or "")
            try:
                started_dt = datetime.fromisoformat(started.replace("Z", "+00:00"))
                age_days = (now - started_dt).total_seconds() / 86400
            except (ValueError, TypeError):
                age_days = 0.0
            out.append(
                DraftSummary(
                    path=str(path.relative_to(paths.knowledge_root())),
                    type=str(front.get("type") or type_dir.rstrip("s")),
                    slug=str(front.get("slug") or path.stem),
                    draft_started_at=started,
                    draft_unresolved_claims=int(front.get("draft_unresolved_claims") or 0),
                    age_days=round(age_days, 1),
                )
            )
    # Oldest first (largest age_days first)
    out.sort(key=lambda d: d.age_days, reverse=True)
    return out
```

- [ ] **Step 5: Register router**

In `/Users/andrewgrant/code/knowledge/src/gateway/web/app.py`, add to existing imports:

```python
from gateway.web.routes import review as review_routes
```

In `create_app()` after the existing `app.include_router` calls:

```python
    app.include_router(review_routes.router)
```

- [ ] **Step 6: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: 3 tests pass.

- [ ] **Step 7: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 520+ pass.

- [ ] **Step 8: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_review.py && git commit -m "feat(m42): GET /api/review/drafts endpoint"
```

---

### Task 3: Contradictions endpoint

**Files:**
- Modify: `src/gateway/web/routes/review.py`
- Modify: `src/gateway/web/schemas.py`
- Modify: `tests/gateway/test_web_review.py`

- [ ] **Step 1: Write failing test**

Append to `/Users/andrewgrant/code/knowledge/tests/gateway/test_web_review.py`:

```python
def test_contradictions_returns_empty_when_no_log(client, kb_root):
    resp = client.get("/api/review/contradictions")
    assert resp.status_code == 200
    assert resp.json() == []


def test_contradictions_returns_log_records_newest_first(client, kb_root):
    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        '{"source_id": "yt-old", "existing_page": "wiki/concepts/a.md", '
        '"existing_claim": "old claim", "new_claim": "new claim", '
        '"severity": "minor", "recorded_at": "2026-04-01T00:00:00Z"}\n'
        '{"source_id": "yt-new", "existing_page": "wiki/concepts/b.md", '
        '"existing_claim": "another old", "new_claim": "another new", '
        '"severity": "major", "recorded_at": "2026-05-04T00:00:00Z"}\n'
    )

    resp = client.get("/api/review/contradictions")
    assert resp.status_code == 200
    records = resp.json()
    assert len(records) == 2
    # Newest first
    assert records[0]["source_id"] == "yt-new"
    assert records[0]["severity"] == "major"
    assert records[1]["source_id"] == "yt-old"


def test_contradictions_skips_malformed_lines(client, kb_root):
    log_path = paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        'this is not json\n'
        '{"source_id": "yt-good", "existing_page": "wiki/concepts/x.md", '
        '"existing_claim": "a", "new_claim": "b", "severity": "moderate", '
        '"recorded_at": "2026-05-04T00:00:00Z"}\n'
        '{}\n'  # Empty object passes JSON parse but lacks expected fields; still returned as-is
    )

    resp = client.get("/api/review/contradictions")
    assert resp.status_code == 200
    records = resp.json()
    # Two valid JSON lines (empty object is JSON; non-json line skipped)
    assert len(records) == 2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: 3 new failures.

- [ ] **Step 3: Add schema**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/schemas.py`:

```python
class ContradictionRecord(BaseModel):
    source_id: str = ""
    existing_page: str = ""
    existing_claim: str = ""
    new_claim: str = ""
    severity: str = "moderate"
    recorded_at: str = ""
```

- [ ] **Step 4: Add endpoint**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/routes/review.py`:

```python
from gateway import contradictions_log
from gateway.web.schemas import ContradictionRecord


@router.get("/contradictions", response_model=list[ContradictionRecord])
def list_contradictions() -> list[ContradictionRecord]:
    records = contradictions_log.read_records()
    out: list[ContradictionRecord] = []
    for r in records:
        out.append(
            ContradictionRecord(
                source_id=str(r.get("source_id") or ""),
                existing_page=str(r.get("existing_page") or ""),
                existing_claim=str(r.get("existing_claim") or ""),
                new_claim=str(r.get("new_claim") or ""),
                severity=str(r.get("severity") or "moderate"),
                recorded_at=str(r.get("recorded_at") or ""),
            )
        )
    return out
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: All pass.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_review.py && git commit -m "feat(m42): GET /api/review/contradictions reads JSONL log"
```

---

### Task 4: Orphans endpoint

**Files:**
- Modify: `src/gateway/web/routes/review.py`
- Modify: `src/gateway/web/schemas.py`
- Modify: `tests/gateway/test_web_review.py`

- [ ] **Step 1: Write failing test**

Append to `/Users/andrewgrant/code/knowledge/tests/gateway/test_web_review.py`:

```python
def test_orphans_returns_sources_without_wiki_pages(client, kb_root, make_source):
    """A source with empty `wiki_pages` is an orphan."""
    # Seed an orphan
    orphan_text = make_source(id_="yt-orphan_AB", domains=["d-test"])
    orphan_path = paths.raw_source_path("youtube", "yt-orphan_AB")
    orphan_path.parent.mkdir(parents=True, exist_ok=True)
    orphan_path.write_text(orphan_text)

    # Seed a non-orphan (has wiki_pages populated)
    text = make_source(
        id_="yt-cited_CD",
        domains=["d-test"],
        extra_front={"wiki_pages": ["wiki/concepts/x.md"]},
    )
    cited_path = paths.raw_source_path("youtube", "yt-cited_CD")
    cited_path.write_text(text)

    resp = client.get("/api/review/orphans")
    assert resp.status_code == 200
    orphans = resp.json()
    ids = {o["source_id"] for o in orphans}
    assert "yt-orphan_AB" in ids
    assert "yt-cited_CD" not in ids


def test_orphans_empty_when_no_sources(client, kb_root):
    resp = client.get("/api/review/orphans")
    assert resp.status_code == 200
    assert resp.json() == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: 2 new failures.

- [ ] **Step 3: Add schema**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/schemas.py`:

```python
class OrphanSource(BaseModel):
    source_id: str
    source_type: str
    title: str = ""
    ingested_at: str = ""
    domains: list[str] = []
```

- [ ] **Step 4: Add endpoint**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/routes/review.py`:

```python
from gateway.web.schemas import OrphanSource


@router.get("/orphans", response_model=list[OrphanSource])
def list_orphans() -> list[OrphanSource]:
    raw = paths.raw_dir()
    if not raw.exists():
        return []
    out: list[OrphanSource] = []
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            wiki_pages = front.get("wiki_pages") or []
            if isinstance(wiki_pages, list) and len(wiki_pages) > 0:
                continue
            out.append(
                OrphanSource(
                    source_id=str(front.get("id") or path.stem),
                    source_type=str(front.get("type") or source_type),
                    title=str(front.get("title") or ""),
                    ingested_at=str(front.get("ingested_at") or ""),
                    domains=list(front.get("domains") or []),
                )
            )
    # Newest first
    out.sort(key=lambda o: o.ingested_at, reverse=True)
    return out
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: All pass.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_review.py && git commit -m "feat(m42): GET /api/review/orphans walks raw/ for empty wiki_pages"
```

---

### Task 5: Filter-band endpoint

**Files:**
- Modify: `src/gateway/web/routes/review.py`
- Modify: `src/gateway/web/schemas.py`
- Modify: `tests/gateway/test_web_review.py`

- [ ] **Step 1: Write failing test**

Append to `/Users/andrewgrant/code/knowledge/tests/gateway/test_web_review.py`:

```python
def test_filter_band_returns_sources_between_thresholds(client, kb_root, make_source):
    """A source with filter.score between threshold_review and threshold_include shows up."""
    # Seed a policy with thresholds
    policy_yaml = paths.policies_dir() / "d-band" / "policy.yaml"
    policy_yaml.parent.mkdir(parents=True, exist_ok=True)
    policy_yaml.write_text(
        "version: v1\n"
        "domain:\n"
        "  slug: d-band\n"
        "  topic: t\n"
        "  field: f\n"
        "  description: d\n"
        "filter:\n"
        "  threshold_include: 0.7\n"
        "  threshold_review: 0.5\n"
        "inclusion_criteria: [a]\nexclusion_criteria: [b]\n"
    )

    # Source in the band (score 0.6, between 0.5 and 0.7)
    in_band_text = make_source(
        id_="yt-band_AB",
        domains=["d-band"],
        extra_front={"filter": {"score": 0.6, "policy_version": "v1", "rationale": "x", "decided_at": "2026-05-01T00:00:00Z"}},
    )
    (paths.raw_source_path("youtube", "yt-band_AB")).write_text(in_band_text)

    # Source above threshold_include (score 0.9 — included, not in band)
    above_text = make_source(
        id_="yt-above_AB",
        domains=["d-band"],
        extra_front={"filter": {"score": 0.9, "policy_version": "v1", "rationale": "x", "decided_at": "2026-05-01T00:00:00Z"}},
    )
    (paths.raw_source_path("youtube", "yt-above_AB")).write_text(above_text)

    # Source below threshold_review (score 0.3 — rejected, not in band)
    below_text = make_source(
        id_="yt-below_AB",
        domains=["d-band"],
        extra_front={"filter": {"score": 0.3, "policy_version": "v1", "rationale": "x", "decided_at": "2026-05-01T00:00:00Z"}},
    )
    (paths.raw_source_path("youtube", "yt-below_AB")).write_text(below_text)

    resp = client.get("/api/review/filter-band")
    assert resp.status_code == 200
    band = resp.json()
    ids = {b["source_id"] for b in band}
    assert "yt-band_AB" in ids
    assert "yt-above_AB" not in ids
    assert "yt-below_AB" not in ids


def test_filter_band_empty_when_no_policies(client, kb_root):
    resp = client.get("/api/review/filter-band")
    assert resp.status_code == 200
    assert resp.json() == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: 2 new failures.

- [ ] **Step 3: Add schema**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/schemas.py`:

```python
class FilterBandSource(BaseModel):
    source_id: str
    source_type: str
    title: str = ""
    score: float = 0.0
    threshold_review: float = 0.0
    threshold_include: float = 0.0
    domain: str = ""
```

- [ ] **Step 4: Add endpoint**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/routes/review.py`:

```python
from gateway.filter import policy as _policy
from gateway.filter.policy import PolicyError
from gateway.web.schemas import FilterBandSource


@router.get("/filter-band", response_model=list[FilterBandSource])
def list_filter_band() -> list[FilterBandSource]:
    """Return sources with filter.score between threshold_review and threshold_include."""
    raw = paths.raw_dir()
    if not raw.exists():
        return []

    # Cache loaded policies per request
    policy_cache: dict[str, _policy.Policy | None] = {}

    def get_policy(domain: str) -> _policy.Policy | None:
        if domain not in policy_cache:
            try:
                policy_cache[domain] = _policy.load_policy(domain)
            except PolicyError:
                policy_cache[domain] = None
        return policy_cache[domain]

    out: list[FilterBandSource] = []
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            filter_block = front.get("filter") or {}
            if not isinstance(filter_block, dict):
                continue
            score = filter_block.get("score")
            if score is None:
                continue
            try:
                score = float(score)
            except (TypeError, ValueError):
                continue
            domains = front.get("domains") or []
            if not isinstance(domains, list):
                continue
            for domain in domains:
                policy = get_policy(str(domain))
                if policy is None:
                    continue
                if policy.threshold_review <= score < policy.threshold_include:
                    out.append(
                        FilterBandSource(
                            source_id=str(front.get("id") or path.stem),
                            source_type=str(front.get("type") or source_type),
                            title=str(front.get("title") or ""),
                            score=score,
                            threshold_review=policy.threshold_review,
                            threshold_include=policy.threshold_include,
                            domain=str(domain),
                        )
                    )
                    break  # one row per source, even if multi-domain
    out.sort(key=lambda b: b.score)  # ascending — most ambiguous first
    return out
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_review.py -v`
Expected: All pass.

- [ ] **Step 6: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 525+ pass.

- [ ] **Step 7: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_review.py && git commit -m "feat(m42): GET /api/review/filter-band walks raw/ filtered by policy thresholds"
```

---

### Task 6: Frontend types + api extensions

**Files:**
- Modify: `web/src/types.ts`
- Modify: `web/src/api.ts`

- [ ] **Step 1: Append types**

Append to `/Users/andrewgrant/code/knowledge/web/src/types.ts`:

```typescript
export interface DraftSummary {
  path: string;
  type: string;
  slug: string;
  draft_started_at: string;
  draft_unresolved_claims: number;
  age_days: number;
}

export interface ContradictionRecord {
  source_id: string;
  existing_page: string;
  existing_claim: string;
  new_claim: string;
  severity: string;
  recorded_at: string;
}

export interface OrphanSource {
  source_id: string;
  source_type: string;
  title: string;
  ingested_at: string;
  domains: string[];
}

export interface FilterBandSource {
  source_id: string;
  source_type: string;
  title: string;
  score: number;
  threshold_review: number;
  threshold_include: number;
  domain: string;
}
```

- [ ] **Step 2: Update api.ts imports + methods**

Open `/Users/andrewgrant/code/knowledge/web/src/api.ts`. Update the import block at the top:

```typescript
import type {
  ContradictionRecord,
  DomainSummary,
  DraftSummary,
  FilterBandSource,
  LogEntry,
  OperationResult,
  OrphanSource,
  ProgressResponse,
  ProposalSummary,
  ResearchPlanQueries,
  ResearchSessionDetail,
  ResearchSessionSummary,
  StatusResponse,
  TaskResponse,
} from "./types";
```

In the `api` object, before the closing `};`, append:

```typescript
  // Review (M42)
  listDrafts: () => request<DraftSummary[]>("/api/review/drafts"),
  listContradictions: () =>
    request<ContradictionRecord[]>("/api/review/contradictions"),
  listOrphans: () => request<OrphanSource[]>("/api/review/orphans"),
  listFilterBand: () =>
    request<FilterBandSource[]>("/api/review/filter-band"),
```

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 4: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/types.ts web/src/api.ts web/dist/ && git commit -m "feat(m42): frontend types + api client for review endpoints"
```

---

### Task 7: Review page shell + sidebar entry

**Files:**
- Create: `web/src/pages/review/Review.tsx`
- Create: `web/src/pages/review/DraftsTab.tsx` (placeholder)
- Create: `web/src/pages/review/ContradictionsTab.tsx` (placeholder)
- Create: `web/src/pages/review/OrphansTab.tsx` (placeholder)
- Create: `web/src/pages/review/FilterBandTab.tsx` (placeholder)
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create the four placeholder tab components**

Create `/Users/andrewgrant/code/knowledge/web/src/pages/review/DraftsTab.tsx`:

```typescript
export default function DraftsTab() {
  return <div style={{ padding: 12 }}>Drafts (coming soon)</div>;
}
```

Create `/Users/andrewgrant/code/knowledge/web/src/pages/review/ContradictionsTab.tsx`:

```typescript
export default function ContradictionsTab() {
  return <div style={{ padding: 12 }}>Contradictions (coming soon)</div>;
}
```

Create `/Users/andrewgrant/code/knowledge/web/src/pages/review/OrphansTab.tsx`:

```typescript
export default function OrphansTab() {
  return <div style={{ padding: 12 }}>Orphans (coming soon)</div>;
}
```

Create `/Users/andrewgrant/code/knowledge/web/src/pages/review/FilterBandTab.tsx`:

```typescript
export default function FilterBandTab() {
  return <div style={{ padding: 12 }}>Filter-band (coming soon)</div>;
}
```

- [ ] **Step 2: Create Review.tsx with tabs**

Create `/Users/andrewgrant/code/knowledge/web/src/pages/review/Review.tsx`:

```typescript
import { NavLink, Route, Routes, useLocation } from "react-router-dom";
import DraftsTab from "./DraftsTab";
import ContradictionsTab from "./ContradictionsTab";
import OrphansTab from "./OrphansTab";
import FilterBandTab from "./FilterBandTab";

const TABS = [
  { path: "drafts", label: "Drafts" },
  { path: "contradictions", label: "Contradictions" },
  { path: "orphans", label: "Orphans" },
  { path: "filter-band", label: "Filter-band" },
];

export default function Review() {
  const location = useLocation();
  const activePath = location.pathname.replace(/^\/review\/?/, "") || "drafts";

  return (
    <div>
      <h1>Review</h1>
      <p className="subtitle">Pending curation decisions across the wiki.</p>

      <div
        style={{
          display: "flex",
          gap: 0,
          borderBottom: "1px solid #ddd",
          marginBottom: 12,
        }}
      >
        {TABS.map((t) => {
          const isActive = activePath === t.path;
          return (
            <NavLink
              key={t.path}
              to={`/review/${t.path}`}
              style={{
                padding: "8px 16px",
                fontSize: 12,
                fontWeight: isActive ? 600 : 400,
                color: isActive ? "#1a4c8e" : "#666",
                borderBottom: isActive ? "2px solid #1a4c8e" : "2px solid transparent",
                marginBottom: -1,
                textDecoration: "none",
              }}
            >
              {t.label}
            </NavLink>
          );
        })}
      </div>

      <Routes>
        <Route index element={<DraftsTab />} />
        <Route path="drafts" element={<DraftsTab />} />
        <Route path="contradictions" element={<ContradictionsTab />} />
        <Route path="orphans" element={<OrphansTab />} />
        <Route path="filter-band" element={<FilterBandTab />} />
      </Routes>
    </div>
  );
}
```

- [ ] **Step 3: Wire into App.tsx**

In `/Users/andrewgrant/code/knowledge/web/src/App.tsx`, add the import:

```typescript
import Review from "./pages/review/Review";
```

In the `Sidebar` component, add a new group + entry. Find the System group label:

```typescript
      <div className="sidebar-group-label">System</div>
      <NavLink to="/system/lint">Lint</NavLink>
```

Insert BEFORE the System group:

```typescript
      <div className="sidebar-group-label">Review</div>
      <NavLink to="/review">Review</NavLink>
```

In the `<Routes>` block, add a route that includes a wildcard so the inner Routes can match tab paths:

```typescript
<Route path="/review/*" element={<Review />} />
```

Add it after the existing `/research/*` routes and before the `/system/*` routes.

- [ ] **Step 4: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 5: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/ web/dist/ && git commit -m "feat(m42): Review page shell with tabs + sidebar entry"
```

---

### Task 8: DraftsTab implementation

**Files:**
- Modify: `web/src/pages/review/DraftsTab.tsx`

- [ ] **Step 1: Replace DraftsTab.tsx**

Replace `/Users/andrewgrant/code/knowledge/web/src/pages/review/DraftsTab.tsx` with:

```typescript
import { useEffect, useState } from "react";
import { api } from "../../api";
import type { DraftSummary } from "../../types";

export default function DraftsTab() {
  const [drafts, setDrafts] = useState<DraftSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setDrafts(await api.listDrafts());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  async function finalize(path: string, abandon: boolean) {
    if (abandon && !confirm(`Permanently delete ${path}?`)) return;
    setBusy(`${abandon ? "abandon" : "finalize"}:${path}`);
    setError(null);
    try {
      await api.finalize(path, abandon);
      refresh();
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(null);
    }
  }

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 8,
        }}
      >
        <div style={{ fontSize: 12, color: "#666" }}>
          {loading ? "Loading…" : `${drafts.length} draft${drafts.length === 1 ? "" : "s"}`}
        </div>
        <button
          className="btn-secondary"
          onClick={refresh}
          disabled={loading}
          style={{ fontSize: 11 }}
        >
          Refresh
        </button>
      </div>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {!loading && drafts.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>No drafts pending.</div>
      )}

      {drafts.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Path</th>
              <th>Type</th>
              <th>Age (days)</th>
              <th>Unresolved</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {drafts.map((d) => {
              const stale = d.age_days > 7;
              return (
                <tr
                  key={d.path}
                  style={{ background: stale ? "#fffbeb" : undefined }}
                >
                  <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                    {d.path}
                  </td>
                  <td>{d.type}</td>
                  <td style={{ color: stale ? "#d97706" : undefined }}>
                    {d.age_days.toFixed(1)}
                  </td>
                  <td>{d.draft_unresolved_claims}</td>
                  <td>
                    <button
                      className="btn-secondary"
                      onClick={() => finalize(d.path, false)}
                      disabled={busy === `finalize:${d.path}`}
                      style={{ fontSize: 11, marginRight: 6 }}
                    >
                      Finalize
                    </button>
                    <button
                      className="btn-secondary"
                      onClick={() => finalize(d.path, true)}
                      disabled={busy === `abandon:${d.path}`}
                      style={{ fontSize: 11, color: "#dc2626", borderColor: "#dc2626" }}
                    >
                      Abandon
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/review/DraftsTab.tsx web/dist/ && git commit -m "feat(m42): DraftsTab with inline Finalize/Abandon"
```

---

### Task 9: ContradictionsTab implementation

**Files:**
- Modify: `web/src/pages/review/ContradictionsTab.tsx`

- [ ] **Step 1: Replace ContradictionsTab.tsx**

Replace `/Users/andrewgrant/code/knowledge/web/src/pages/review/ContradictionsTab.tsx` with:

```typescript
import { useEffect, useState } from "react";
import { api } from "../../api";
import type { ContradictionRecord } from "../../types";

const SEVERITY_STYLE: Record<string, { bg: string; color: string }> = {
  minor: { bg: "#f0f0f0", color: "#666" },
  moderate: { bg: "#fffbeb", color: "#d97706" },
  major: { bg: "#fef2f2", color: "#dc2626" },
};

export default function ContradictionsTab() {
  const [records, setRecords] = useState<ContradictionRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedIdx, setExpandedIdx] = useState<number | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setRecords(await api.listContradictions());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 8,
        }}
      >
        <div style={{ fontSize: 12, color: "#666" }}>
          {loading
            ? "Loading…"
            : `${records.length} contradiction${records.length === 1 ? "" : "s"}`}
        </div>
        <button
          className="btn-secondary"
          onClick={refresh}
          disabled={loading}
          style={{ fontSize: 11 }}
        >
          Refresh
        </button>
      </div>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {!loading && records.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>
          No contradictions recorded yet. Authorship runs with `--with-plan` populate this log when conflicts are detected.
        </div>
      )}

      {records.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Recorded</th>
              <th>Source</th>
              <th>Affected page</th>
              <th>Severity</th>
              <th>Existing claim</th>
              <th>New claim</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r, idx) => {
              const sev = SEVERITY_STYLE[r.severity] ?? SEVERITY_STYLE.moderate;
              const expanded = expandedIdx === idx;
              return (
                <>
                  <tr
                    key={`row-${idx}`}
                    onClick={() => setExpandedIdx(expanded ? null : idx)}
                    style={{ cursor: "pointer" }}
                  >
                    <td style={{ fontSize: 11 }}>{r.recorded_at}</td>
                    <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                      {r.source_id}
                    </td>
                    <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                      {r.existing_page}
                    </td>
                    <td>
                      <span
                        style={{
                          fontSize: 10,
                          padding: "2px 8px",
                          borderRadius: 3,
                          background: sev.bg,
                          color: sev.color,
                          fontWeight: 600,
                        }}
                      >
                        {r.severity}
                      </span>
                    </td>
                    <td style={{ fontSize: 11, maxWidth: 250, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {r.existing_claim}
                    </td>
                    <td style={{ fontSize: 11, maxWidth: 250, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {r.new_claim}
                    </td>
                  </tr>
                  {expanded && (
                    <tr key={`detail-${idx}`}>
                      <td colSpan={6} style={{ background: "#fafafa", padding: 12 }}>
                        <div style={{ marginBottom: 8 }}>
                          <div style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>Existing claim</div>
                          <div style={{ fontSize: 12, marginTop: 2 }}>{r.existing_claim}</div>
                        </div>
                        <div>
                          <div style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>New claim (from {r.source_id})</div>
                          <div style={{ fontSize: 12, marginTop: 2 }}>{r.new_claim}</div>
                        </div>
                        <div style={{ marginTop: 8, fontSize: 11, color: "#666" }}>
                          Resolve by editing <code>{r.existing_page}</code> in your editor; the M42 console is read-only.
                        </div>
                      </td>
                    </tr>
                  )}
                </>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly. (If TSC complains about React keys on fragments, the code uses explicit keys on each `<tr>` so this should pass.)

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/review/ContradictionsTab.tsx web/dist/ && git commit -m "feat(m42): ContradictionsTab with severity badges + accordion expand"
```

---

### Task 10: OrphansTab implementation + Query page param prefill

**Files:**
- Modify: `web/src/pages/review/OrphansTab.tsx`
- Modify: `web/src/pages/Query.tsx` (M40) — add useSearchParams prefill

- [ ] **Step 1: Replace OrphansTab.tsx**

Replace `/Users/andrewgrant/code/knowledge/web/src/pages/review/OrphansTab.tsx` with:

```typescript
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../../api";
import type { OrphanSource } from "../../types";

export default function OrphansTab() {
  const [orphans, setOrphans] = useState<OrphanSource[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setOrphans(await api.listOrphans());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 8,
        }}
      >
        <div style={{ fontSize: 12, color: "#666" }}>
          {loading
            ? "Loading…"
            : `${orphans.length} orphan source${orphans.length === 1 ? "" : "s"}`}
        </div>
        <button
          className="btn-secondary"
          onClick={refresh}
          disabled={loading}
          style={{ fontSize: 11 }}
        >
          Refresh
        </button>
      </div>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {!loading && orphans.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>
          No orphan sources. Every ingested source is cited by at least one wiki page.
        </div>
      )}

      {orphans.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Source ID</th>
              <th>Type</th>
              <th>Title</th>
              <th>Domain</th>
              <th>Ingested</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {orphans.map((o) => {
              const primaryDomain = o.domains[0] || "";
              const queryHref = `/ops/query?domain=${encodeURIComponent(primaryDomain)}&source_id=${encodeURIComponent(o.source_id)}`;
              return (
                <tr key={o.source_id}>
                  <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                    {o.source_id}
                  </td>
                  <td>{o.source_type}</td>
                  <td style={{ fontSize: 11, maxWidth: 320, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                    {o.title}
                  </td>
                  <td style={{ fontSize: 11 }}>{primaryDomain || "—"}</td>
                  <td style={{ fontSize: 11 }}>{o.ingested_at}</td>
                  <td>
                    <Link
                      to={queryHref}
                      className="btn-secondary"
                      style={{ fontSize: 11, textDecoration: "none", padding: "3px 8px" }}
                    >
                      Discharge via query
                    </Link>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Extend Query.tsx to read URL params**

Modify `/Users/andrewgrant/code/knowledge/web/src/pages/Query.tsx`. Add the import at the top:

```typescript
import { useSearchParams } from "react-router-dom";
```

Inside the `Query` component, after the existing `useState` calls, add:

```typescript
  const [searchParams] = useSearchParams();

  useEffect(() => {
    const domainParam = searchParams.get("domain");
    if (domainParam) setDomain(domainParam);
    // (We deliberately don't read source_id here — it's informational
    // context the user can paste into the question field if useful.)
  }, [searchParams]);
```

You'll need to add the `useEffect` import too. Update the existing React import line:

```typescript
import { useEffect, useState } from "react";
```

(If `useState` is already imported, just add `useEffect` to the same line.)

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 4: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/ web/dist/ && git commit -m "feat(m42): OrphansTab with discharge-via-query link + Query page domain prefill"
```

---

### Task 11: FilterBandTab implementation

**Files:**
- Modify: `web/src/pages/review/FilterBandTab.tsx`

- [ ] **Step 1: Replace FilterBandTab.tsx**

Replace `/Users/andrewgrant/code/knowledge/web/src/pages/review/FilterBandTab.tsx` with:

```typescript
import { useEffect, useState } from "react";
import { api } from "../../api";
import type { FilterBandSource } from "../../types";

export default function FilterBandTab() {
  const [items, setItems] = useState<FilterBandSource[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [modal, setModal] = useState<
    { source_id: string; decision: "include" | "exclude" } | null
  >(null);
  const [rationale, setRationale] = useState("");

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setItems(await api.listFilterBand());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  function openModal(source_id: string, decision: "include" | "exclude") {
    setModal({ source_id, decision });
    setRationale("");
  }

  async function submitCorrection() {
    if (!modal) return;
    if (!rationale.trim()) {
      setError("rationale is required");
      return;
    }
    setBusy(`${modal.decision}:${modal.source_id}`);
    setError(null);
    try {
      await api.filterCorrect(modal.source_id, modal.decision, rationale);
      setModal(null);
      refresh();
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(null);
    }
  }

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 8,
        }}
      >
        <div style={{ fontSize: 12, color: "#666" }}>
          {loading ? "Loading…" : `${items.length} source${items.length === 1 ? "" : "s"} in review band`}
        </div>
        <button
          className="btn-secondary"
          onClick={refresh}
          disabled={loading}
          style={{ fontSize: 11 }}
        >
          Refresh
        </button>
      </div>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {!loading && items.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>
          No sources in the review band (between threshold_review and threshold_include for any domain).
        </div>
      )}

      {items.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Source ID</th>
              <th>Type</th>
              <th>Title</th>
              <th>Score</th>
              <th>Domain</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {items.map((s) => (
              <tr key={s.source_id}>
                <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                  {s.source_id}
                </td>
                <td>{s.source_type}</td>
                <td style={{ fontSize: 11, maxWidth: 280, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                  {s.title}
                </td>
                <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                  {s.score.toFixed(2)}
                </td>
                <td style={{ fontSize: 11 }}>{s.domain}</td>
                <td>
                  <button
                    className="btn-secondary"
                    onClick={() => openModal(s.source_id, "include")}
                    disabled={busy === `include:${s.source_id}`}
                    style={{ fontSize: 11, marginRight: 6, color: "#0a8a3e", borderColor: "#0a8a3e" }}
                  >
                    Include
                  </button>
                  <button
                    className="btn-secondary"
                    onClick={() => openModal(s.source_id, "exclude")}
                    disabled={busy === `exclude:${s.source_id}`}
                    style={{ fontSize: 11, color: "#dc2626", borderColor: "#dc2626" }}
                  >
                    Exclude
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {modal && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "rgba(0,0,0,0.4)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 100,
          }}
          onClick={() => setModal(null)}
        >
          <div
            style={{
              background: "white",
              borderRadius: 6,
              padding: 20,
              width: 480,
              maxWidth: "90%",
              boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <h3 style={{ marginTop: 0 }}>
              {modal.decision === "include" ? "Include" : "Exclude"}{" "}
              <code style={{ fontSize: 12 }}>{modal.source_id}</code>
            </h3>
            <label style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>
              Rationale
            </label>
            <textarea
              value={rationale}
              onChange={(e) => setRationale(e.target.value)}
              placeholder="Why this decision is correct..."
              style={{
                width: "100%",
                fontSize: 12,
                padding: 6,
                border: "1px solid #ccc",
                borderRadius: 3,
                minHeight: 80,
                marginTop: 4,
                fontFamily: "inherit",
                resize: "vertical",
              }}
            />
            <div style={{ marginTop: 12, display: "flex", gap: 8, justifyContent: "flex-end" }}>
              <button
                className="btn-secondary"
                onClick={() => setModal(null)}
                disabled={!!busy}
              >
                Cancel
              </button>
              <button
                className="btn-primary"
                onClick={submitCorrection}
                disabled={!!busy || !rationale.trim()}
              >
                {busy ? "Submitting..." : "Submit"}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/review/FilterBandTab.tsx web/dist/ && git commit -m "feat(m42): FilterBandTab with rationale modal + filter-correct round-trip"
```

---

### Task 12: Hand-test + documentation

**Files:**
- Modify: `BUILD.md`
- Modify: `CLAUDE.md`
- Modify: `TUTORIAL.md`

- [ ] **Step 1: Hand-test the full flow**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/wiki serve --port 7475 &`
Wait 3 seconds, then:

```bash
echo "=== /api/review/drafts ==="
curl -s http://127.0.0.1:7475/api/review/drafts | python3 -c 'import sys,json; d=json.load(sys.stdin); print(f"{len(d)} drafts"); [print(x.get("path"), "age:", x.get("age_days")) for x in d[:5]]'
echo ""
echo "=== /api/review/orphans ==="
curl -s http://127.0.0.1:7475/api/review/orphans | python3 -c 'import sys,json; d=json.load(sys.stdin); print(f"{len(d)} orphans")'
echo ""
echo "=== /api/review/contradictions ==="
curl -s http://127.0.0.1:7475/api/review/contradictions | python3 -c 'import sys,json; d=json.load(sys.stdin); print(f"{len(d)} contradictions")'
echo ""
echo "=== /api/review/filter-band ==="
curl -s http://127.0.0.1:7475/api/review/filter-band | python3 -c 'import sys,json; d=json.load(sys.stdin); print(f"{len(d)} in-band")'
echo ""
echo "=== /review (HTML SPA route) ==="
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:7475/review
```

Open http://127.0.0.1:7475/review in a browser. Verify:
- Sidebar Review entry navigates to /review
- Drafts tab loads (likely 173+ entries given current memory state)
- Click Finalize on one draft → row removes from list
- Stale drafts (>7 days) have amber row tint
- Contradictions tab loads (likely 0 entries unless apply_plan has run with contradictions since M42)
- Orphans tab loads (likely 215+ entries per M25 memory)
- Filter-band tab loads
- Click an orphan's "Discharge via query" → Query page opens with domain prefilled

Then: `pkill -f "wiki serve"`

- [ ] **Step 2: Append BUILD.md M42 entry**

In `/Users/andrewgrant/code/knowledge/BUILD.md`, after the M41 section (before "## 11. Downstream wiki-authoring work"), add:

```markdown
### M42 — Review consoles + structured contradiction persistence

Adds a Review sidebar entry to `wiki serve` with four tabs (Drafts, Contradictions, Orphans, Filter-band). Drafts and Filter-band have inline actions (Finalize/Abandon, Include/Exclude). Contradictions and Orphans are read-only with click-through. Adds structured contradiction persistence so the Contradictions tab has a queryable data source: `apply_plan` writes JSONL records to `.knowledge/contradictions/log.jsonl` on every plan that has contradictions.

**What's new.**

- `gateway.contradictions_log` — append-only JSONL helper. `append_contradictions(records)` writes one line per record with `recorded_at`. `read_records()` returns parsed records sorted newest-first; tolerates malformed lines.
- `gateway.ops.apply_plan` — calls `contradictions_log.append_contradictions(plan.contradictions)` inside the existing Phase 2 lock when contradictions are non-empty. Backward-compatible: plans without contradictions don't touch the file.
- `gateway.web.routes.review` — four GET endpoints: `/api/review/drafts`, `/api/review/contradictions`, `/api/review/orphans`, `/api/review/filter-band`. Each derives state from existing on-disk artifacts (wiki/ frontmatter, raw/ frontmatter, .knowledge/contradictions/log.jsonl, .knowledge/policies/*/policy.yaml).
- `web/src/pages/review/` — Review page shell with 4 tabs. DraftsTab + FilterBandTab have inline actions; ContradictionsTab uses accordion-expand for claim detail; OrphansTab links to `/ops/query?domain=...` for discharge.
- `web/src/pages/Query.tsx` (M40) — extended to read `?domain=...` URL param and prefill the form on mount.

**Lifecycle / data sources.**

| Tab | Source | Sort |
|---|---|---|
| Drafts | wiki/{entities,concepts,synthesis,mocs}/*.md with `draft: true` frontmatter | oldest first (by `draft_started_at`) |
| Contradictions | `.knowledge/contradictions/log.jsonl` | newest first (by `recorded_at`) |
| Orphans | raw/<type>/*.md with empty `wiki_pages` | newest first (by `ingested_at`) |
| Filter-band | raw/<type>/*.md where `threshold_review ≤ filter.score < threshold_include` for any domain policy | score ascending |

**Tests.** ~10 new tests across `test_web_review.py` and `test_authorship.py`. Full gateway suite: 515 → 525+ tests passing.

**Out of scope (deferred to M43).**

- NLM artifact triggers (briefing, audio, slides, revise) per-domain page with confirmation modals.
- Bulk actions in review tabs (select multiple drafts, batch finalize).
- Filter/search within tabs.
- Aggregating contradictions by affected page.
- Backfill of pre-M42 contradictions from `log.md` summaries.
```

- [ ] **Step 3: Update CLAUDE.md operation table**

In `/Users/andrewgrant/code/knowledge/CLAUDE.md`, find the "Start the local web UI" row and append a parenthetical:

```
| Start the local web UI (FastAPI + React) | `wiki serve [--port 7474] [--bind 127.0.0.1]` (visit `/research` for orchestration UI; `/review` for curation queues) |
```

- [ ] **Step 4: Update TUTORIAL.md**

In `/Users/andrewgrant/code/knowledge/TUTORIAL.md` § 11 "Cheat sheet", update the `wiki serve` line:

```
wiki serve [--port 7474]                           # local browser UI; /research orchestration · /review curation queues
```

- [ ] **Step 5: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add BUILD.md CLAUDE.md TUTORIAL.md && git commit -m "docs: M42 delivery record + review consoles in operation tables"
```

---

## Self-review

**Spec coverage:**

| Spec § | Tasks |
|---|---|
| § 1 Architecture | Tasks 1-12 (cumulative) |
| § 2 Endpoints (4) | Tasks 2 (drafts), 3 (contradictions), 4 (orphans), 5 (filter-band) |
| § 2 apply_plan JSONL change | Task 1 |
| § 2 Drafts/Orphans/Filter-band data sources | Tasks 2, 4, 5 (in helpers) |
| § 2 Contradictions data source | Task 1 (writer) + Task 3 (reader) |
| § 3 Frontend layout | Tasks 6-11 |
| § 3 DraftsTab inline actions | Task 8 |
| § 3 ContradictionsTab accordion | Task 9 |
| § 3 OrphansTab + Query prefill | Task 10 |
| § 3 FilterBandTab modal | Task 11 |
| § 4 Out of scope | Documented in Task 12 BUILD.md entry |
| § 6 Acceptance criteria 1-10 | All mapped |

**Placeholder scan:** No TBDs. The Task 9 build step has a hedge ("If TSC complains about React keys on fragments") — that's a sanity check, not a placeholder; the code uses explicit keys correctly.

**Type consistency:**
- `DraftSummary`, `ContradictionRecord`, `OrphanSource`, `FilterBandSource` shapes match between Pydantic schemas (Tasks 2-5) and TS types (Task 6).
- `api.listDrafts` etc. return types match the schema return types.
- The contradictions log record shape (Task 1) matches `ContradictionRecord` schema (Task 3).
- `api.finalize(path, abandon)` signature unchanged from M40; reused in Task 8.
- `api.filterCorrect(source_id, decision, rationale)` signature unchanged from M40; reused in Task 11.

**Cross-task assumptions verified:**
- M40 `api.finalize` and `api.filterCorrect` exist and return `OperationResult` — confirmed via existing `web/src/api.ts`.
- `gateway.filter.policy.load_policy` raises `PolicyError` — confirmed during M39.
- `paths.policies_dir()` exists — confirmed during M39.
- `paths.SOURCE_TYPES` exists — confirmed during M40.
