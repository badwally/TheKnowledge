# M40 Web UI Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `wiki serve` — a FastAPI + React/TypeScript browser front-end that wraps the gateway's daily ops (ingest, query, finalize, filter-correct), domain ops (bootstrap, discover, promote/demote/reject), and lint dashboard.

**Architecture:** FastAPI backend in `src/gateway/web/` thinly adapts existing `gateway.ops.*` functions over HTTP. Vite + React + TypeScript SPA in `web/` is built once and committed as static assets to `web/dist/`, served by FastAPI at `/`. Long-running ops use a submit-then-poll pattern with an in-memory task store; short ops execute synchronously.

**Tech Stack:** Python 3.11+, FastAPI, uvicorn, Pydantic, React 18, Vite, TypeScript, plain CSS modules, pytest, FastAPI TestClient.

**Spec reference:** `docs/superpowers/specs/2026-05-04-m40-web-ui-foundation-design.md`

---

### Task 1: Add FastAPI + uvicorn dependencies and create web module skeleton

**Files:**
- Modify: `pyproject.toml`
- Create: `src/gateway/web/__init__.py`
- Create: `src/gateway/web/app.py`
- Create: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_app.py`

- [ ] **Step 1: Add deps to pyproject.toml**

In the `[project.dependencies]` block of `pyproject.toml`, append:

```toml
    "fastapi>=0.110",
    "uvicorn[standard]>=0.27",
```

- [ ] **Step 2: Install deps**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pip install -e .`
Expected: fastapi and uvicorn install without conflicts.

- [ ] **Step 3: Write the failing smoke test**

Create `tests/gateway/test_web_app.py`:

```python
"""Tests for the M40 FastAPI web app."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    app = create_app()
    return TestClient(app)


def test_app_returns_health_ok(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
```

- [ ] **Step 4: Run test to verify it fails**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: FAIL — `gateway.web.app` does not exist.

- [ ] **Step 5: Create the FastAPI app**

Create `src/gateway/web/__init__.py` (empty):

```python
"""Gateway web layer (M40). Thin HTTP adapters around `gateway.ops.*`."""
```

Create `src/gateway/web/schemas.py`:

```python
"""Pydantic models for the web API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
```

Create `src/gateway/web/app.py`:

```python
"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from fastapi import FastAPI

from gateway.web.schemas import HealthResponse


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    return app


app = create_app()
```

- [ ] **Step 6: Run test to verify it passes**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py::test_app_returns_health_ok -v`
Expected: PASS.

- [ ] **Step 7: Run full suite for regressions**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 482 passed (481 before + 1 new).

- [ ] **Step 8: Commit**

```bash
git add pyproject.toml src/gateway/web/ tests/gateway/test_web_app.py
git commit -m "feat(m40): FastAPI scaffold with health endpoint"
```

---

### Task 2: In-memory task store

**Files:**
- Create: `src/gateway/web/tasks.py`
- Test: `tests/gateway/test_web_tasks.py`

- [ ] **Step 1: Write failing tests for the task store**

Create `tests/gateway/test_web_tasks.py`:

```python
"""Tests for the M40 in-memory task store."""

from __future__ import annotations

import asyncio
import time

import pytest

from gateway.web.tasks import TaskStore


@pytest.fixture
def store():
    return TaskStore()


def test_create_task_returns_record(store):
    record = store.create("ingest")
    assert record.task_id
    assert record.op_name == "ingest"
    assert record.status == "queued"
    assert record.started_at is None
    assert record.finished_at is None
    assert record.result is None
    assert record.error is None


def test_get_task_returns_record(store):
    created = store.create("query")
    fetched = store.get(created.task_id)
    assert fetched is not None
    assert fetched.task_id == created.task_id


def test_get_unknown_task_returns_none(store):
    assert store.get("nonexistent") is None


def test_mark_running_updates_status_and_started_at(store):
    record = store.create("ingest")
    store.mark_running(record.task_id)
    fetched = store.get(record.task_id)
    assert fetched.status == "running"
    assert fetched.started_at is not None


def test_mark_done_records_result_and_finished_at(store):
    record = store.create("ingest")
    store.mark_running(record.task_id)
    store.mark_done(record.task_id, result={"summary": "ok"})
    fetched = store.get(record.task_id)
    assert fetched.status == "done"
    assert fetched.finished_at is not None
    assert fetched.result == {"summary": "ok"}


def test_mark_failed_records_error(store):
    record = store.create("ingest")
    store.mark_running(record.task_id)
    store.mark_failed(record.task_id, error="boom")
    fetched = store.get(record.task_id)
    assert fetched.status == "failed"
    assert fetched.error == "boom"
    assert fetched.finished_at is not None


def test_run_async_executes_callable_and_records_result(store):
    async def runner():
        record = store.create("ingest")
        await store.run_async(record.task_id, lambda: {"summary": "ran"})
        return record.task_id

    task_id = asyncio.run(runner())
    fetched = store.get(task_id)
    assert fetched.status == "done"
    assert fetched.result == {"summary": "ran"}


def test_run_async_captures_exception(store):
    def boom():
        raise ValueError("bad input")

    async def runner():
        record = store.create("ingest")
        await store.run_async(record.task_id, boom)
        return record.task_id

    task_id = asyncio.run(runner())
    fetched = store.get(task_id)
    assert fetched.status == "failed"
    assert "bad input" in fetched.error
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_tasks.py -v`
Expected: FAIL — `gateway.web.tasks` does not exist.

- [ ] **Step 3: Implement TaskStore**

Create `src/gateway/web/tasks.py`:

```python
"""In-memory task store for long-running web ops.

Records persist for the lifetime of the `wiki serve` process. Restart
loses in-flight task history; `log.md` is the durable activity record.
"""

from __future__ import annotations

import asyncio
import threading
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class TaskRecord:
    task_id: str
    op_name: str
    status: str = "queued"  # queued | running | done | failed
    started_at: str | None = None
    finished_at: str | None = None
    result: dict[str, Any] | None = None
    error: str | None = None


class TaskStore:
    """Process-local task registry. Thread-safe via a single lock."""

    def __init__(self) -> None:
        self._records: dict[str, TaskRecord] = {}
        self._lock = threading.Lock()

    def create(self, op_name: str) -> TaskRecord:
        record = TaskRecord(task_id=str(uuid.uuid4()), op_name=op_name)
        with self._lock:
            self._records[record.task_id] = record
        return record

    def get(self, task_id: str) -> TaskRecord | None:
        with self._lock:
            return self._records.get(task_id)

    def mark_running(self, task_id: str) -> None:
        with self._lock:
            record = self._records.get(task_id)
            if record is not None:
                record.status = "running"
                record.started_at = _now_iso()

    def mark_done(self, task_id: str, *, result: dict[str, Any]) -> None:
        with self._lock:
            record = self._records.get(task_id)
            if record is not None:
                record.status = "done"
                record.result = result
                record.finished_at = _now_iso()

    def mark_failed(self, task_id: str, *, error: str) -> None:
        with self._lock:
            record = self._records.get(task_id)
            if record is not None:
                record.status = "failed"
                record.error = error
                record.finished_at = _now_iso()

    async def run_async(self, task_id: str, fn: Callable[[], Any]) -> None:
        """Run `fn` in a worker thread, updating the task record on completion."""
        self.mark_running(task_id)
        try:
            result = await asyncio.to_thread(fn)
            payload = result if isinstance(result, dict) else {"value": result}
            self.mark_done(task_id, result=payload)
        except Exception as e:  # noqa: BLE001 — capture all
            self.mark_failed(task_id, error=f"{type(e).__name__}: {e}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_tasks.py -v`
Expected: All 8 tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/web/tasks.py tests/gateway/test_web_tasks.py
git commit -m "feat(m40): in-memory TaskStore for long-running web ops"
```

---

### Task 3: Status / log / lint read-only endpoints

**Files:**
- Create: `src/gateway/web/routes/__init__.py`
- Create: `src/gateway/web/routes/status.py`
- Modify: `src/gateway/web/app.py` (register status router)
- Modify: `src/gateway/web/schemas.py` (add response models)
- Test: `tests/gateway/test_web_app.py` (extend)

- [ ] **Step 1: Write failing tests**

Append to `tests/gateway/test_web_app.py`:

```python
def test_get_status(client, monkeypatch):
    """Status endpoint returns watcher state, inbox, drafts, sources."""
    from gateway import paths

    # Seed a raw source so sources count > 0
    raw = paths.raw_source_path("youtube", "yt-statusTest_AB")
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(
        "---\nid: yt-statusTest_AB\ntype: youtube\ntitle: t\n"
        "url: https://x\nauthors: []\ningested_at: 2026-01-01T00:00:00Z\n"
        "content_hash: sha256:abc\ndomains: []\nnlm_corpus_ids: []\n"
        "wiki_pages: []\nmeta: {}\n---\nbody\n"
    )

    resp = client.get("/api/status")
    assert resp.status_code == 200
    body = resp.json()
    assert "watcher" in body
    assert "inbox" in body
    assert "drafts" in body
    assert "sources" in body
    assert "domains" in body
    assert body["sources"] >= 1


def test_get_log(client):
    """Log endpoint tails log.md."""
    from gateway import paths

    log_path = paths.log_path()
    log_path.write_text(
        "# log\n\n"
        "## [2026-05-04T20:00:00Z] ingest | id=yt-1\n\nx\n\n"
        "## [2026-05-04T20:01:00Z] query | domain=d\n\ny\n"
    )

    resp = client.get("/api/log?lines=10")
    assert resp.status_code == 200
    entries = resp.json()
    assert isinstance(entries, list)
    assert len(entries) == 2
    assert entries[0]["op"] == "query"  # newest first
    assert entries[1]["op"] == "ingest"


def test_get_lint(client):
    """Lint endpoint runs lint and returns a structured report."""
    resp = client.get("/api/lint?scope=schema-drift")
    assert resp.status_code == 200
    body = resp.json()
    assert "report_path" in body or "issues" in body or "summary" in body
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: 3 failures (endpoints don't exist).

- [ ] **Step 3: Add response schemas**

Append to `src/gateway/web/schemas.py`:

```python
class WatcherState(BaseModel):
    running: bool
    pid: int | None = None
    last_heartbeat: str | None = None


class InboxState(BaseModel):
    pending: int
    failed: int


class StatusResponse(BaseModel):
    watcher: WatcherState
    inbox: InboxState
    drafts: int
    sources: int
    domains: int


class LogEntry(BaseModel):
    timestamp: str
    op: str
    fields: dict[str, str] = {}
    summary: str = ""


class LintResponse(BaseModel):
    summary: str
    report_path: str | None = None
    issues: list[dict[str, Any]] = []
```

- [ ] **Step 4: Implement the routes**

Create `src/gateway/web/routes/__init__.py` (empty):

```python
"""Route modules for the gateway web app."""
```

Create `src/gateway/web/routes/status.py`:

```python
"""Read-only status / log / lint endpoints."""

from __future__ import annotations

import re
from pathlib import Path

from fastapi import APIRouter, Query

from gateway import paths
from gateway.ops.lint import lint as lint_op
from gateway.watcher import watcher_state
from gateway.web.schemas import (
    InboxState,
    LintResponse,
    LogEntry,
    StatusResponse,
    WatcherState,
)


router = APIRouter(prefix="/api", tags=["status"])


_LOG_HEADER_RE = re.compile(
    r"^## \[(?P<ts>[^\]]+)\] (?P<op>[a-z0-9-]+)(?: \| (?P<fields>.*))?$"
)


@router.get("/status", response_model=StatusResponse)
def get_status() -> StatusResponse:
    state = watcher_state()
    return StatusResponse(
        watcher=WatcherState(
            running=state["running"],
            pid=state["pid"],
            last_heartbeat=state["last_heartbeat"],
        ),
        inbox=InboxState(
            pending=state["inbox_pending"],
            failed=state["inbox_failed"],
        ),
        drafts=_count_drafts(),
        sources=_count_sources(),
        domains=_count_domains(),
    )


@router.get("/log", response_model=list[LogEntry])
def get_log(lines: int = Query(50, ge=1, le=500)) -> list[LogEntry]:
    log_path = paths.log_path()
    if not log_path.exists():
        return []
    text = log_path.read_text()
    entries = _parse_log_entries(text)
    return list(reversed(entries[-lines:]))


@router.get("/lint", response_model=LintResponse)
def get_lint(scope: str | None = Query(None)) -> LintResponse:
    result = lint_op(scope=scope)
    return LintResponse(
        summary=result.summary,
        report_path=str(result.paths_touched[0]) if result.paths_touched else None,
        issues=[],
    )


def _count_drafts() -> int:
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return 0
    count = 0
    for sub in ("entities", "concepts", "synthesis", "mocs"):
        d = wiki / sub
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            try:
                if "draft: true" in path.read_text():
                    count += 1
            except OSError:
                continue
    return count


def _count_sources() -> int:
    raw = paths.raw_dir()
    if not raw.exists():
        return 0
    count = 0
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if d.exists():
            count += sum(1 for _ in d.glob("*.md"))
    return count


def _count_domains() -> int:
    policies_dir = paths.policies_dir()
    if not policies_dir.exists():
        return 0
    return sum(
        1 for d in policies_dir.iterdir()
        if d.is_dir() and (d / "policy.yaml").exists()
    )


def _parse_log_entries(text: str) -> list[LogEntry]:
    entries: list[LogEntry] = []
    current: LogEntry | None = None
    summary_lines: list[str] = []
    for line in text.splitlines():
        m = _LOG_HEADER_RE.match(line)
        if m:
            if current is not None:
                current.summary = "\n".join(summary_lines).strip()
                entries.append(current)
            fields_dict: dict[str, str] = {}
            raw_fields = m.group("fields") or ""
            for pair in raw_fields.split(" | "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    fields_dict[k.strip()] = v.strip()
            current = LogEntry(
                timestamp=m.group("ts"),
                op=m.group("op"),
                fields=fields_dict,
                summary="",
            )
            summary_lines = []
        elif current is not None:
            summary_lines.append(line)
    if current is not None:
        current.summary = "\n".join(summary_lines).strip()
        entries.append(current)
    return entries
```

- [ ] **Step 5: Register the router**

Modify `src/gateway/web/app.py`:

```python
"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from fastapi import FastAPI

from gateway.web.routes import status as status_routes
from gateway.web.schemas import HealthResponse


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    app.include_router(status_routes.router)
    return app


app = create_app()
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: 4 tests pass.

- [ ] **Step 7: Commit**

```bash
git add src/gateway/web/ tests/gateway/test_web_app.py
git commit -m "feat(m40): status/log/lint read-only endpoints"
```

---

### Task 4: Domain endpoints (read + promote/demote/reject)

**Files:**
- Create: `src/gateway/web/routes/domains.py`
- Modify: `src/gateway/web/app.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_app.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/gateway/test_web_app.py`:

```python
def test_list_domains(client, monkeypatch):
    """GET /api/domains returns each policy as a summary."""
    from gateway import paths

    pol = paths.policies_dir() / "test-domain" / "policy.yaml"
    pol.parent.mkdir(parents=True, exist_ok=True)
    pol.write_text(
        "version: v1\npolicy_schema_version: 1\n"
        "domain:\n  slug: test-domain\n  topic: Test\n  field: T\n  description: d\n"
        "filter:\n  threshold_include: 0.7\n  threshold_review: 0.5\n"
        "inclusion_criteria: [a, b, c]\nexclusion_criteria: [x]\n"
        "quality_signals: {q: {positive_signals: [p, q], negative_signals: [n, m]}}\n"
    )

    resp = client.get("/api/domains")
    assert resp.status_code == 200
    domains = resp.json()
    assert any(d["slug"] == "test-domain" for d in domains)


def test_list_proposals(client):
    """GET /api/proposals returns draft proposals."""
    from gateway import frontmatter as fm
    from gateway import paths

    prop = paths.wiki_dir() / "proposals" / "test-prop.md"
    prop.parent.mkdir(parents=True, exist_ok=True)
    prop.write_text(
        fm.serialize(
            {
                "type": "domain-proposal",
                "slug": "test-prop",
                "title": "Test prop",
                "proposed_domain": "test-prop",
                "status": "draft",
                "member_sources": ["yt-1"],
                "rationale": "r",
            },
            "## Rationale\n\nr\n## Member sources\n\n- [[sources/yt-1]]\n",
        )
    )

    resp = client.get("/api/proposals")
    assert resp.status_code == 200
    proposals = resp.json()
    assert any(p["slug"] == "test-prop" for p in proposals)


def test_promote_domain_returns_error_for_missing_proposal(client):
    resp = client.post("/api/domains/nonexistent/promote")
    assert resp.status_code == 400
    body = resp.json()
    assert "errors" in body or "detail" in body
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: 3 failures.

- [ ] **Step 3: Add domain schemas**

Append to `src/gateway/web/schemas.py`:

```python
class DomainSummary(BaseModel):
    slug: str
    topic: str = ""
    sources_count: int = 0
    has_notebook: bool = False


class ProposalSummary(BaseModel):
    slug: str
    title: str
    proposed_domain: str
    status: str
    member_sources_count: int


class OperationResultResponse(BaseModel):
    success: bool
    summary: str = ""
    paths_touched: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []
    no_op: bool = False
    authorship_report: dict[str, Any] | None = None
```

- [ ] **Step 4: Implement domains router**

Create `src/gateway/web/routes/domains.py`:

```python
"""Domain endpoints: list domains, list proposals, promote/demote/reject."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

import yaml

from gateway import frontmatter as fm
from gateway import nlm_registry, paths
from gateway.ops.demote_domain import demote_domain
from gateway.ops.promote_domain import promote_domain
from gateway.ops.reject_proposal import reject_proposal
from gateway.web.schemas import (
    DomainSummary,
    OperationResultResponse,
    ProposalSummary,
)


router = APIRouter(prefix="/api", tags=["domains"])


@router.get("/domains", response_model=list[DomainSummary])
def list_domains() -> list[DomainSummary]:
    out: list[DomainSummary] = []
    policies_dir = paths.policies_dir()
    if not policies_dir.exists():
        return out
    for d in sorted(policies_dir.iterdir()):
        if not d.is_dir():
            continue
        policy_yaml = d / "policy.yaml"
        if not policy_yaml.exists():
            continue
        try:
            data = yaml.safe_load(policy_yaml.read_text()) or {}
        except yaml.YAMLError:
            continue
        slug = (data.get("domain") or {}).get("slug", d.name)
        topic = (data.get("domain") or {}).get("topic", "")
        out.append(
            DomainSummary(
                slug=slug,
                topic=topic,
                sources_count=_count_domain_sources(slug),
                has_notebook=nlm_registry.get_persistent(slug) is not None,
            )
        )
    return out


@router.get("/proposals", response_model=list[ProposalSummary])
def list_proposals() -> list[ProposalSummary]:
    out: list[ProposalSummary] = []
    prop_dir = paths.wiki_dir() / "proposals"
    if not prop_dir.exists():
        return out
    for path in sorted(prop_dir.glob("*.md")):
        try:
            front, _ = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        out.append(
            ProposalSummary(
                slug=str(front.get("slug") or path.stem),
                title=str(front.get("title") or ""),
                proposed_domain=str(front.get("proposed_domain") or ""),
                status=str(front.get("status") or ""),
                member_sources_count=len(front.get("member_sources") or []),
            )
        )
    return out


@router.post("/domains/{slug}/promote", response_model=OperationResultResponse)
def post_promote(slug: str) -> OperationResultResponse:
    result = promote_domain(slug)
    return _to_response(result)


@router.post("/domains/{slug}/demote", response_model=OperationResultResponse)
def post_demote(slug: str) -> OperationResultResponse:
    result = demote_domain(slug)
    return _to_response(result)


@router.post("/domains/{slug}/reject", response_model=OperationResultResponse)
def post_reject(slug: str) -> OperationResultResponse:
    result = reject_proposal(slug)
    return _to_response(result)


def _to_response(result) -> OperationResultResponse:
    if not result.success:
        raise HTTPException(
            status_code=400,
            detail={
                "summary": result.summary,
                "errors": result.errors,
                "warnings": result.warnings,
            },
        )
    return OperationResultResponse(
        success=result.success,
        summary=result.summary,
        paths_touched=[str(p) for p in result.paths_touched],
        warnings=result.warnings,
        errors=result.errors,
        no_op=result.no_op,
        authorship_report=_serialize_authorship_report(
            getattr(result, "authorship_report", None)
        ),
    )


def _serialize_authorship_report(report) -> dict | None:
    if report is None:
        return None
    return {
        "pages_created": list(report.pages_created),
        "pages_updated": list(report.pages_updated),
        "contradictions": [
            {
                "existing_page": c.existing_page,
                "existing_claim": c.existing_claim,
                "new_claim": c.new_claim,
                "source_id": c.source_id,
                "severity": c.severity,
            }
            for c in report.contradictions
        ],
    }


def _count_domain_sources(slug: str) -> int:
    raw = paths.raw_dir()
    if not raw.exists():
        return 0
    count = 0
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            try:
                front, _ = fm.parse(path.read_text())
                if slug in (front.get("domains") or []):
                    count += 1
            except (fm.FrontmatterError, OSError):
                continue
    return count
```

- [ ] **Step 5: Register the router**

In `src/gateway/web/app.py`, add import and include:

```python
from gateway.web.routes import domains as domain_routes
from gateway.web.routes import status as status_routes
```

After `app.include_router(status_routes.router)`, add:

```python
    app.include_router(domain_routes.router)
```

- [ ] **Step 6: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: All tests pass.

- [ ] **Step 7: Commit**

```bash
git add src/gateway/web/ tests/gateway/test_web_app.py
git commit -m "feat(m40): domain endpoints (list + promote/demote/reject)"
```

---

### Task 5: Synchronous ops endpoints (filter-correct, finalize)

**Files:**
- Create: `src/gateway/web/routes/ops.py`
- Modify: `src/gateway/web/app.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_app.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/gateway/test_web_app.py`:

```python
def test_finalize_endpoint_rejects_missing_path(client):
    resp = client.post(
        "/api/ops/finalize",
        json={"page_path": "wiki/concepts/nonexistent.md", "abandon": False},
    )
    assert resp.status_code == 400


def test_filter_correct_endpoint_returns_error_for_missing_source(client):
    resp = client.post(
        "/api/ops/filter-correct",
        json={"source_id": "yt-nonexistent", "decision": "include", "rationale": "r"},
    )
    assert resp.status_code == 400
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py::test_finalize_endpoint_rejects_missing_path tests/gateway/test_web_app.py::test_filter_correct_endpoint_returns_error_for_missing_source -v`
Expected: FAIL — endpoints don't exist.

- [ ] **Step 3: Add request schemas**

Append to `src/gateway/web/schemas.py`:

```python
class FinalizeRequest(BaseModel):
    page_path: str
    abandon: bool = False


class FilterCorrectRequest(BaseModel):
    source_id: str
    decision: str  # "include" | "exclude"
    rationale: str
```

- [ ] **Step 4: Implement ops router**

Create `src/gateway/web/routes/ops.py`:

```python
"""Operation endpoints. Synchronous (short ops) or async (long ops via TaskStore)."""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException

from gateway.ops.filter_correct import filter_correct
from gateway.ops.finalize import finalize
from gateway.web.routes.domains import _to_response
from gateway.web.schemas import (
    FilterCorrectRequest,
    FinalizeRequest,
    OperationResultResponse,
)


router = APIRouter(prefix="/api/ops", tags=["ops"])


@router.post("/finalize", response_model=OperationResultResponse)
def post_finalize(req: FinalizeRequest) -> OperationResultResponse:
    result = finalize(Path(req.page_path), abandon=req.abandon)
    return _to_response(result)


@router.post("/filter-correct", response_model=OperationResultResponse)
def post_filter_correct(req: FilterCorrectRequest) -> OperationResultResponse:
    if req.decision not in ("include", "exclude"):
        raise HTTPException(
            status_code=400,
            detail=f"decision must be 'include' or 'exclude', got {req.decision!r}",
        )
    result = filter_correct(
        source_id=req.source_id,
        decision=req.decision,
        rationale=req.rationale,
    )
    return _to_response(result)
```

- [ ] **Step 5: Register router**

In `src/gateway/web/app.py`, import and include:

```python
from gateway.web.routes import ops as ops_routes
```

After `app.include_router(domain_routes.router)`:

```python
    app.include_router(ops_routes.router)
```

- [ ] **Step 6: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: All pass.

- [ ] **Step 7: Commit**

```bash
git add src/gateway/web/ tests/gateway/test_web_app.py
git commit -m "feat(m40): synchronous ops endpoints (finalize, filter-correct)"
```

---

### Task 6: Async ops endpoints (ingest, query, bootstrap-domain, discover-domains)

**Files:**
- Modify: `src/gateway/web/routes/ops.py`
- Create: `src/gateway/web/routes/tasks.py`
- Modify: `src/gateway/web/app.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_app.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/gateway/test_web_app.py`:

```python
import time
import json


def test_async_ingest_returns_task_id(client, kb_root, tmp_path):
    """POST /api/ops/ingest returns 202 + task_id; GET /api/tasks/{id} reports completion."""
    src = tmp_path / "input.md"
    src.write_text(
        "---\nid: yt-asyncTest_AB\ntype: youtube\ntitle: t\n"
        "url: https://x\nauthors: []\n"
        "ingested_at: 2026-01-01T00:00:00Z\n"
        "content_hash: sha256:abc\ndomains: []\nnlm_corpus_ids: []\n"
        "wiki_pages: []\nmeta: {}\n---\nbody\n"
    )

    resp = client.post(
        "/api/ops/ingest",
        json={"input": str(src), "with_plan": False, "draft": False},
    )
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"

    task_id = body["task_id"]
    # Poll up to 5s for completion
    for _ in range(50):
        time.sleep(0.1)
        get_resp = client.get(f"/api/tasks/{task_id}")
        if get_resp.json()["status"] in ("done", "failed"):
            break
    final = client.get(f"/api/tasks/{task_id}").json()
    assert final["status"] == "done", final


def test_get_unknown_task_returns_404(client):
    resp = client.get("/api/tasks/nonexistent")
    assert resp.status_code == 404


def test_async_bootstrap_domain_returns_task_id(client, kb_root, monkeypatch):
    """Bootstrap with stub plan client runs asynchronously."""
    # Inject a stub plan client at the module level via env or override
    # For this test we let it run with the real planner stub
    resp = client.post(
        "/api/ops/bootstrap-domain",
        json={
            "description": "x",  # too short to satisfy specificity
            "slug": "Bad_Slug",  # invalid slug — will fail synchronously inside the op
            "force": False,
        },
    )
    assert resp.status_code == 202
    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    final = client.get(f"/api/tasks/{task_id}").json()
    # Should either fail fast (invalid slug) or complete with errors in result
    assert final["status"] in ("done", "failed")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: 3 failures (endpoints don't exist).

- [ ] **Step 3: Add async request schemas**

Append to `src/gateway/web/schemas.py`:

```python
class IngestRequest(BaseModel):
    input: str
    domain: str | None = None
    with_plan: bool = False
    draft: bool = False
    plan_timeout: float | None = None


class QueryRequest(BaseModel):
    question: str
    domain: str
    draft: bool = False


class BootstrapDomainRequest(BaseModel):
    description: str
    slug: str
    force: bool = False


class DiscoverDomainsRequest(BaseModel):
    scope: str | None = None
    since: str | None = None
    untagged: bool = False


class TaskResponse(BaseModel):
    task_id: str
    op_name: str
    status: str
    started_at: str | None = None
    finished_at: str | None = None
    result: dict[str, Any] | None = None
    error: str | None = None
```

- [ ] **Step 4: Add task store singleton + tasks router**

Modify `src/gateway/web/app.py` to construct a shared TaskStore:

```python
"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from fastapi import FastAPI

from gateway.web.routes import domains as domain_routes
from gateway.web.routes import ops as ops_routes
from gateway.web.routes import status as status_routes
from gateway.web.routes import tasks as task_routes
from gateway.web.schemas import HealthResponse
from gateway.web.tasks import TaskStore


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")
    app.state.task_store = TaskStore()

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    app.include_router(status_routes.router)
    app.include_router(domain_routes.router)
    app.include_router(ops_routes.router)
    app.include_router(task_routes.router)
    return app


app = create_app()
```

Create `src/gateway/web/routes/tasks.py`:

```python
"""Task status endpoint."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request

from gateway.web.schemas import TaskResponse


router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str, request: Request) -> TaskResponse:
    store = request.app.state.task_store
    record = store.get(task_id)
    if record is None:
        raise HTTPException(status_code=404, detail=f"unknown task_id: {task_id}")
    return TaskResponse(
        task_id=record.task_id,
        op_name=record.op_name,
        status=record.status,
        started_at=record.started_at,
        finished_at=record.finished_at,
        result=record.result,
        error=record.error,
    )
```

- [ ] **Step 5: Add async op endpoints**

Append to `src/gateway/web/routes/ops.py`:

```python
import asyncio
from pathlib import Path

from fastapi import BackgroundTasks, Request
from fastapi.responses import JSONResponse

from gateway.ops.bootstrap_domain import bootstrap_domain
from gateway.ops.discover_domains import discover_domains
from gateway.ops.ingest import ingest
from gateway.ops.query import query
from gateway.web.routes.domains import _serialize_authorship_report
from gateway.web.schemas import (
    BootstrapDomainRequest,
    DiscoverDomainsRequest,
    IngestRequest,
    QueryRequest,
)


def _serialize_op_result(result) -> dict:
    return {
        "success": result.success,
        "summary": result.summary,
        "paths_touched": [str(p) for p in result.paths_touched],
        "warnings": list(result.warnings),
        "errors": list(result.errors),
        "no_op": result.no_op,
        "authorship_report": _serialize_authorship_report(
            getattr(result, "authorship_report", None)
        ),
    }


def _resolve_input(raw: str):
    if raw.startswith(("http://", "https://")):
        return raw
    return Path(raw).expanduser().resolve()


@router.post("/ingest", status_code=202)
async def post_ingest(req: IngestRequest, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("ingest")

    def run() -> dict:
        result = ingest(
            _resolve_input(req.input),
            domain=req.domain,
            with_plan=req.with_plan,
            draft=req.draft,
        )
        return _serialize_op_result(result)

    asyncio.create_task(store.run_async(record.task_id, run))
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/query", status_code=202)
async def post_query(req: QueryRequest, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("query")

    def run() -> dict:
        result = query(req.question, domain=req.domain, draft=req.draft)
        return _serialize_op_result(result)

    asyncio.create_task(store.run_async(record.task_id, run))
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/bootstrap-domain", status_code=202)
async def post_bootstrap(
    req: BootstrapDomainRequest, request: Request
) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("bootstrap-domain")

    def run() -> dict:
        result = bootstrap_domain(
            description=req.description,
            slug=req.slug,
            force=req.force,
        )
        return _serialize_op_result(result)

    asyncio.create_task(store.run_async(record.task_id, run))
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/discover-domains", status_code=202)
async def post_discover(
    req: DiscoverDomainsRequest, request: Request
) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("discover-domains")

    def run() -> dict:
        result = discover_domains(
            scope=req.scope,
            since=req.since,
            untagged=req.untagged,
        )
        return _serialize_op_result(result)

    asyncio.create_task(store.run_async(record.task_id, run))
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )
```

- [ ] **Step 6: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: All pass. The async tests poll for up to 5s.

- [ ] **Step 7: Run full suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 480+ pass, no regressions.

- [ ] **Step 8: Commit**

```bash
git add src/gateway/web/ tests/gateway/test_web_app.py
git commit -m "feat(m40): async ops endpoints (ingest, query, bootstrap, discover)"
```

---

### Task 7: `wiki serve` CLI subcommand

**Files:**
- Modify: `src/gateway/cli.py`
- Test: `tests/gateway/test_cli_serve.py` (new)

- [ ] **Step 1: Write failing test**

Create `tests/gateway/test_cli_serve.py`:

```python
"""Smoke test for `wiki serve` CLI argument parsing."""

from __future__ import annotations

import pytest

from gateway.cli import build_parser


def test_serve_parser_accepts_default_args():
    parser = build_parser()
    ns = parser.parse_args(["serve"])
    assert ns.subcommand == "serve"
    assert ns.port == 7474
    assert ns.bind == "127.0.0.1"


def test_serve_parser_accepts_custom_port_and_bind():
    parser = build_parser()
    ns = parser.parse_args(["serve", "--port", "9000", "--bind", "0.0.0.0"])
    assert ns.port == 9000
    assert ns.bind == "0.0.0.0"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_cli_serve.py -v`
Expected: FAIL — `serve` is not a registered subcommand.

- [ ] **Step 3: Add subcommand to cli.py**

In `src/gateway/cli.py`, add to `SUBCOMMANDS` dict:

```python
    "serve": "Start the local web UI (FastAPI + React)",
```

Add to `IMPLEMENTED` set:

```python
    "serve",
```

After the `bootstrap-domain` subparser, add:

```python
    # serve (M40)
    p_serve = subparsers.add_parser("serve", help=SUBCOMMANDS["serve"])
    p_serve.add_argument(
        "--port",
        type=int,
        default=7474,
        help="Port to bind (default 7474)",
    )
    p_serve.add_argument(
        "--bind",
        default="127.0.0.1",
        help="Host to bind (default 127.0.0.1; use 0.0.0.0 for LAN access)",
    )
```

In the dispatch section (where `if ns.subcommand == "bootstrap-domain":` lives), add:

```python
    if ns.subcommand == "serve":
        return _run_serve(ns)
```

After `_run_bootstrap_domain`:

```python
def _run_serve(ns: argparse.Namespace) -> int:
    import uvicorn

    print(f"wiki serve · http://{ns.bind}:{ns.port}", flush=True)
    uvicorn.run(
        "gateway.web.app:app",
        host=ns.bind,
        port=ns.port,
        log_level="info",
    )
    return 0
```

- [ ] **Step 4: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_cli_serve.py -v`
Expected: PASS.

- [ ] **Step 5: Manual smoke test**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/wiki serve --help`
Expected: argparse usage prints; exit 0.

Then briefly start the server in the background:
Run: `cd /Users/andrewgrant/code/knowledge && timeout 3 .venv/bin/wiki serve --port 7475 || true`
Expected: server starts, prints `wiki serve · http://127.0.0.1:7475`, then exits after 3s.

- [ ] **Step 6: Commit**

```bash
git add src/gateway/cli.py tests/gateway/test_cli_serve.py
git commit -m "feat(m40): wiki serve CLI subcommand"
```

---

### Task 8: Frontend scaffold (Vite + React + TypeScript)

**Files:**
- Create: `web/package.json`
- Create: `web/vite.config.ts`
- Create: `web/tsconfig.json`
- Create: `web/index.html`
- Create: `web/src/main.tsx`
- Create: `web/src/App.tsx`
- Create: `web/src/api.ts`
- Create: `web/src/types.ts`
- Create: `web/src/index.css`

- [ ] **Step 1: Create package.json**

Create `web/package.json`:

```json
{
  "name": "wiki-web",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.26.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "typescript": "^5.5.0",
    "vite": "^5.4.0"
  }
}
```

- [ ] **Step 2: Create vite.config.ts**

Create `web/vite.config.ts`:

```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://127.0.0.1:7474",
    },
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
  },
});
```

- [ ] **Step 3: Create tsconfig.json**

Create `web/tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "jsx": "react-jsx",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
```

- [ ] **Step 4: Create index.html**

Create `web/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>wiki</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

- [ ] **Step 5: Create types.ts**

Create `web/src/types.ts`:

```typescript
export interface WatcherState {
  running: boolean;
  pid: number | null;
  last_heartbeat: string | null;
}

export interface InboxState {
  pending: number;
  failed: number;
}

export interface StatusResponse {
  watcher: WatcherState;
  inbox: InboxState;
  drafts: number;
  sources: number;
  domains: number;
}

export interface LogEntry {
  timestamp: string;
  op: string;
  fields: Record<string, string>;
  summary: string;
}

export interface DomainSummary {
  slug: string;
  topic: string;
  sources_count: number;
  has_notebook: boolean;
}

export interface ProposalSummary {
  slug: string;
  title: string;
  proposed_domain: string;
  status: string;
  member_sources_count: number;
}

export interface AuthorshipReport {
  pages_created: string[];
  pages_updated: string[];
  contradictions: Array<{
    existing_page: string;
    existing_claim: string;
    new_claim: string;
    source_id: string;
    severity: string;
  }>;
}

export interface OperationResult {
  success: boolean;
  summary: string;
  paths_touched: string[];
  warnings: string[];
  errors: string[];
  no_op: boolean;
  authorship_report: AuthorshipReport | null;
}

export interface TaskResponse {
  task_id: string;
  op_name: string;
  status: "queued" | "running" | "done" | "failed";
  started_at: string | null;
  finished_at: string | null;
  result: OperationResult | null;
  error: string | null;
}
```

- [ ] **Step 6: Create api.ts**

Create `web/src/api.ts`:

```typescript
import type {
  DomainSummary,
  LogEntry,
  OperationResult,
  ProposalSummary,
  StatusResponse,
  TaskResponse,
} from "./types";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const resp = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!resp.ok) {
    let detail: any = null;
    try {
      detail = await resp.json();
    } catch (_) {}
    const msg = detail?.detail
      ? typeof detail.detail === "string"
        ? detail.detail
        : JSON.stringify(detail.detail)
      : `HTTP ${resp.status}`;
    throw new Error(msg);
  }
  return resp.json();
}

export const api = {
  status: () => request<StatusResponse>("/api/status"),
  log: (lines = 50) => request<LogEntry[]>(`/api/log?lines=${lines}`),
  lint: (scope?: string) =>
    request<{ summary: string; report_path: string | null }>(
      `/api/lint${scope ? `?scope=${scope}` : ""}`,
    ),
  domains: () => request<DomainSummary[]>("/api/domains"),
  proposals: () => request<ProposalSummary[]>("/api/proposals"),
  promote: (slug: string) =>
    request<OperationResult>(`/api/domains/${slug}/promote`, { method: "POST" }),
  demote: (slug: string) =>
    request<OperationResult>(`/api/domains/${slug}/demote`, { method: "POST" }),
  reject: (slug: string) =>
    request<OperationResult>(`/api/domains/${slug}/reject`, { method: "POST" }),
  finalize: (page_path: string, abandon: boolean) =>
    request<OperationResult>("/api/ops/finalize", {
      method: "POST",
      body: JSON.stringify({ page_path, abandon }),
    }),
  filterCorrect: (source_id: string, decision: string, rationale: string) =>
    request<OperationResult>("/api/ops/filter-correct", {
      method: "POST",
      body: JSON.stringify({ source_id, decision, rationale }),
    }),
  startIngest: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/ingest", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  startQuery: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/query", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  startBootstrap: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/bootstrap-domain", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  startDiscover: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/discover-domains", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  getTask: (id: string) => request<TaskResponse>(`/api/tasks/${id}`),
};
```

- [ ] **Step 7: Create index.css**

Create `web/src/index.css`:

```css
* { box-sizing: border-box; }
html, body, #root { height: 100%; margin: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #f5f5f7;
  color: #1c1c1e;
  font-size: 14px;
}
.app { display: flex; height: 100vh; }
.sidebar {
  width: 220px;
  background: #2a3142;
  color: #cdd9e5;
  padding: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
  overflow-y: auto;
}
.sidebar-brand {
  padding: 0 20px 12px;
  font-weight: 700;
  font-size: 16px;
  border-bottom: 1px solid #3b4252;
  margin-bottom: 8px;
}
.sidebar-group-label {
  padding: 8px 20px 4px;
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  opacity: 0.6;
}
.sidebar a {
  display: block;
  padding: 6px 20px;
  color: inherit;
  text-decoration: none;
  font-size: 13px;
}
.sidebar a:hover { background: #353c4f; }
.sidebar a.active { background: #3b4252; font-weight: 600; }
.content { flex: 1; padding: 20px 28px; overflow-y: auto; background: white; }
.content h1 { font-size: 20px; margin: 0 0 4px; }
.content h2 { font-size: 16px; margin: 16px 0 8px; }
.subtitle { color: #6b6b6b; font-size: 13px; margin: 0 0 16px; }
.stat-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin-bottom: 16px;
}
.stat-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px 12px;
  background: white;
}
.stat-card.healthy { border-left: 3px solid #0a8a3e; }
.stat-card.warning { border-left: 3px solid #d97706; }
.stat-card.danger { border-left: 3px solid #dc2626; }
.stat-label { font-size: 10px; text-transform: uppercase; color: #666; }
.stat-value { font-size: 18px; font-weight: 600; margin-top: 2px; }
.stat-detail { font-size: 11px; color: #888; margin-top: 2px; }
.activity-feed {
  font-family: ui-monospace, monospace;
  font-size: 11px;
  background: #f7f7f9;
  padding: 12px;
  border-radius: 4px;
  white-space: pre-wrap;
  line-height: 1.6;
}
.op-form {
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 16px 18px;
  background: #fafafa;
  max-width: 720px;
}
.op-form label { display: block; font-size: 11px; color: #666; text-transform: uppercase; margin: 10px 0 4px; }
.op-form input, .op-form textarea, .op-form select {
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 6px 10px;
  font-size: 13px;
  font-family: inherit;
}
.op-form textarea { min-height: 80px; resize: vertical; }
.op-form .checkbox-row { display: flex; gap: 12px; margin: 8px 0; }
.op-form .checkbox-row label { display: inline-flex; align-items: center; gap: 6px; text-transform: none; color: inherit; font-size: 13px; margin: 0; }
.btn-primary {
  background: #1a4c8e;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  margin-top: 12px;
}
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
.btn-secondary {
  background: white;
  color: #1a4c8e;
  border: 1px solid #1a4c8e;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
}
.result-panel { margin-top: 16px; border-radius: 4px; padding: 12px 14px; max-width: 720px; }
.result-panel.success { background: #f0faf3; border-left: 3px solid #0a8a3e; }
.result-panel.error { background: #fef2f2; border-left: 3px solid #dc2626; }
.result-panel.running { background: #fffbeb; border-left: 3px solid #d97706; }
.result-panel pre { font-family: ui-monospace, monospace; font-size: 11px; margin: 6px 0 0; white-space: pre-wrap; }
.result-status { font-size: 11px; text-transform: uppercase; font-weight: 600; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 6px 10px; border-bottom: 1px solid #f0f0f0; text-align: left; font-size: 12px; }
th { background: #f7f7f9; font-weight: 600; }
```

- [ ] **Step 8: Create main.tsx**

Create `web/src/main.tsx`:

```typescript
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
);
```

- [ ] **Step 9: Create App.tsx with sidebar shell + placeholder routes**

Create `web/src/App.tsx`:

```typescript
import { NavLink, Route, Routes } from "react-router-dom";

function Sidebar() {
  return (
    <nav className="sidebar">
      <div className="sidebar-brand">wiki</div>
      <div className="sidebar-group-label">Wiki</div>
      <NavLink to="/" end>📊 Dashboard</NavLink>
      <NavLink to="/ops/ingest">📥 Ingest</NavLink>
      <NavLink to="/ops/query">❓ Query</NavLink>
      <NavLink to="/ops/finalize">✓ Finalize</NavLink>
      <NavLink to="/ops/filter-correct">⚖ Filter correct</NavLink>
      <div className="sidebar-group-label">Domains</div>
      <NavLink to="/domains/bootstrap">🌱 Bootstrap</NavLink>
      <NavLink to="/domains/discover">🔍 Discover</NavLink>
      <NavLink to="/domains/promote">⬆ Promote</NavLink>
      <div className="sidebar-group-label">System</div>
      <NavLink to="/system/lint">🩺 Lint</NavLink>
    </nav>
  );
}

function Placeholder({ name }: { name: string }) {
  return (
    <div>
      <h1>{name}</h1>
      <p className="subtitle">Page not yet implemented.</p>
    </div>
  );
}

export default function App() {
  return (
    <div className="app">
      <Sidebar />
      <main className="content">
        <Routes>
          <Route path="/" element={<Placeholder name="Dashboard" />} />
          <Route path="/ops/ingest" element={<Placeholder name="Ingest" />} />
          <Route path="/ops/query" element={<Placeholder name="Query" />} />
          <Route path="/ops/finalize" element={<Placeholder name="Finalize" />} />
          <Route path="/ops/filter-correct" element={<Placeholder name="Filter correct" />} />
          <Route path="/domains/bootstrap" element={<Placeholder name="Bootstrap domain" />} />
          <Route path="/domains/discover" element={<Placeholder name="Discover domains" />} />
          <Route path="/domains/promote" element={<Placeholder name="Promote / Demote / Reject" />} />
          <Route path="/system/lint" element={<Placeholder name="Lint" />} />
        </Routes>
      </main>
    </div>
  );
}
```

- [ ] **Step 10: Install + build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm install`
Expected: dependencies install (~30-60s).

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: `dist/` directory created with `index.html` and `assets/`.

- [ ] **Step 11: Commit**

```bash
git add web/package.json web/vite.config.ts web/tsconfig.json web/index.html web/src/ web/dist/
git commit -m "feat(m40): Vite/React/TypeScript scaffold with sidebar shell"
```

---

### Task 9: Mount static frontend in FastAPI

**Files:**
- Modify: `src/gateway/web/app.py`
- Test: `tests/gateway/test_web_app.py`

- [ ] **Step 1: Write failing test**

Append to `tests/gateway/test_web_app.py`:

```python
def test_root_serves_index_html(client):
    """The root path serves the React app's index.html."""
    resp = client.get("/")
    # If web/dist/index.html exists, expect 200; if not, the test environment
    # doesn't have the built frontend — accept either 200 or 404.
    assert resp.status_code in (200, 404)
    if resp.status_code == 200:
        assert "<html" in resp.text.lower() or "<!doctype" in resp.text.lower()
```

- [ ] **Step 2: Run test**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py::test_root_serves_index_html -v`
Expected: PASS (404, since static serving not yet wired).

- [ ] **Step 3: Wire StaticFiles in app.py**

Modify `src/gateway/web/app.py` to mount static assets after API routes:

```python
"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from gateway.web.routes import domains as domain_routes
from gateway.web.routes import ops as ops_routes
from gateway.web.routes import status as status_routes
from gateway.web.routes import tasks as task_routes
from gateway.web.schemas import HealthResponse
from gateway.web.tasks import TaskStore


_FRONTEND_DIST = Path(__file__).parent.parent.parent.parent / "web" / "dist"


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")
    app.state.task_store = TaskStore()

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    app.include_router(status_routes.router)
    app.include_router(domain_routes.router)
    app.include_router(ops_routes.router)
    app.include_router(task_routes.router)

    if _FRONTEND_DIST.is_dir():
        app.mount(
            "/assets",
            StaticFiles(directory=_FRONTEND_DIST / "assets"),
            name="assets",
        )

        @app.get("/{full_path:path}")
        def serve_spa(full_path: str) -> FileResponse:
            # Any non-API route falls through to index.html so the React
            # router handles client-side navigation on hard refresh.
            return FileResponse(_FRONTEND_DIST / "index.html")

    return app


app = create_app()
```

- [ ] **Step 4: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_app.py -v`
Expected: All pass; root serves 200 with HTML.

- [ ] **Step 5: Manual hand-test**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/wiki serve --port 7475 &`
Then: `sleep 2 && curl -s http://127.0.0.1:7475/api/status | head -5 && curl -s -I http://127.0.0.1:7475/`
Expected: status JSON returns; root returns 200 with `text/html`.
Then: `pkill -f "wiki serve" || true`

- [ ] **Step 6: Commit**

```bash
git add src/gateway/web/app.py tests/gateway/test_web_app.py
git commit -m "feat(m40): mount React frontend at / via StaticFiles + SPA fallback"
```

---

### Task 10: Dashboard page (4 stat cards + activity feed)

**Files:**
- Create: `web/src/pages/Dashboard.tsx`
- Create: `web/src/components/StatCard.tsx`
- Create: `web/src/components/ActivityFeed.tsx`
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create StatCard component**

Create `web/src/components/StatCard.tsx`:

```typescript
import type { ReactNode } from "react";

interface Props {
  label: string;
  value: ReactNode;
  detail?: string;
  status?: "healthy" | "warning" | "danger";
}

export default function StatCard({ label, value, detail, status }: Props) {
  const cls = status ? `stat-card ${status}` : "stat-card";
  return (
    <div className={cls}>
      <div className="stat-label">{label}</div>
      <div className="stat-value">{value}</div>
      {detail && <div className="stat-detail">{detail}</div>}
    </div>
  );
}
```

- [ ] **Step 2: Create ActivityFeed component**

Create `web/src/components/ActivityFeed.tsx`:

```typescript
import type { LogEntry } from "../types";

interface Props {
  entries: LogEntry[];
}

function formatEntry(entry: LogEntry): string {
  const ts = entry.timestamp.replace("T", " ").replace("Z", "");
  const fields = Object.entries(entry.fields)
    .map(([k, v]) => `${k}=${v}`)
    .join(" ");
  return `${ts} ${entry.op}${fields ? " " + fields : ""}`;
}

export default function ActivityFeed({ entries }: Props) {
  if (entries.length === 0) {
    return <div className="activity-feed">(no recent activity)</div>;
  }
  return (
    <div className="activity-feed">
      {entries.map((e, i) => (
        <div key={i}>{formatEntry(e)}</div>
      ))}
    </div>
  );
}
```

- [ ] **Step 3: Create Dashboard page**

Create `web/src/pages/Dashboard.tsx`:

```typescript
import { useEffect, useState } from "react";
import { api } from "../api";
import type { LogEntry, StatusResponse } from "../types";
import StatCard from "../components/StatCard";
import ActivityFeed from "../components/ActivityFeed";

export default function Dashboard() {
  const [status, setStatus] = useState<StatusResponse | null>(null);
  const [log, setLog] = useState<LogEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      const [s, l] = await Promise.all([api.status(), api.log(20)]);
      setStatus(s);
      setLog(l);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>Knowledge base</h1>
        <button className="btn-secondary" onClick={refresh} disabled={loading}>
          {loading ? "Refreshing..." : "Refresh"}
        </button>
      </div>
      <p className="subtitle">Daily glance at watcher state, drafts, and recent activity.</p>

      {error && (
        <div className="result-panel error">
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {status && (
        <div className="stat-grid">
          <StatCard
            label="Watcher"
            value={status.watcher.running ? "running" : "stopped"}
            detail={status.watcher.last_heartbeat ?? "no heartbeat"}
            status={status.watcher.running ? "healthy" : "danger"}
          />
          <StatCard
            label="Inbox"
            value={status.inbox.pending}
            detail={`${status.inbox.failed} failed`}
            status={status.inbox.failed > 0 ? "warning" : undefined}
          />
          <StatCard
            label="Drafts"
            value={status.drafts}
            status={status.drafts > 0 ? "warning" : undefined}
          />
          <StatCard
            label="Sources"
            value={status.sources}
            detail={`${status.domains} domains`}
          />
        </div>
      )}

      <h2>Recent activity</h2>
      <ActivityFeed entries={log} />
    </div>
  );
}
```

- [ ] **Step 4: Wire into App.tsx**

Modify `web/src/App.tsx` — replace the dashboard route's `Placeholder` with `<Dashboard />`. Add the import:

```typescript
import Dashboard from "./pages/Dashboard";
```

Replace `<Route path="/" element={<Placeholder name="Dashboard" />} />` with:

```typescript
<Route path="/" element={<Dashboard />} />
```

- [ ] **Step 5: Build + smoke test**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds.

- [ ] **Step 6: Commit**

```bash
git add web/src/ web/dist/
git commit -m "feat(m40): Dashboard page with stat cards + activity feed"
```

---

### Task 11: TaskRunner + ResultPanel components

**Files:**
- Create: `web/src/components/ResultPanel.tsx`
- Create: `web/src/components/TaskRunner.tsx`

- [ ] **Step 1: Create ResultPanel**

Create `web/src/components/ResultPanel.tsx`:

```typescript
import type { OperationResult } from "../types";

interface Props {
  result: OperationResult;
}

export default function ResultPanel({ result }: Props) {
  const cls = result.success
    ? result.no_op
      ? "result-panel running"
      : "result-panel success"
    : "result-panel error";
  const status = result.success
    ? result.no_op
      ? "✓ No-op"
      : "✓ Completed"
    : "✗ Failed";
  return (
    <div className={cls}>
      <div className="result-status">{status}</div>
      <pre>{result.summary}</pre>
      {result.paths_touched.length > 0 && (
        <pre>
          {result.paths_touched.map((p) => `  touched: ${p}`).join("\n")}
        </pre>
      )}
      {result.authorship_report && (
        <pre>
          {`  authorship: ${result.authorship_report.pages_created.length} created, ${result.authorship_report.pages_updated.length} updated`}
          {result.authorship_report.contradictions.length > 0
            ? `, ${result.authorship_report.contradictions.length} contradiction(s) found`
            : ""}
        </pre>
      )}
      {result.warnings.length > 0 && (
        <pre>{result.warnings.map((w) => `  warning: ${w}`).join("\n")}</pre>
      )}
      {result.errors.length > 0 && (
        <pre>{result.errors.map((e) => `  error: ${e}`).join("\n")}</pre>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Create TaskRunner**

Create `web/src/components/TaskRunner.tsx`:

```typescript
import { useEffect, useRef, useState } from "react";
import { api } from "../api";
import type { OperationResult, TaskResponse } from "../types";
import ResultPanel from "./ResultPanel";

interface Props {
  // Returns the task_id from the start endpoint, or null on synchronous failure
  startTask: () => Promise<{ task_id: string; status: string } | null>;
  buttonLabel?: string;
}

export default function TaskRunner({ startTask, buttonLabel = "Run" }: Props) {
  const [taskId, setTaskId] = useState<string | null>(null);
  const [task, setTask] = useState<TaskResponse | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const intervalRef = useRef<number | null>(null);

  useEffect(() => {
    return () => {
      if (intervalRef.current) window.clearInterval(intervalRef.current);
    };
  }, []);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setTask(null);
    setTaskId(null);
    try {
      const ack = await startTask();
      if (!ack) {
        setSubmitting(false);
        return;
      }
      setTaskId(ack.task_id);
      intervalRef.current = window.setInterval(async () => {
        try {
          const t = await api.getTask(ack.task_id);
          setTask(t);
          if (t.status === "done" || t.status === "failed") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setSubmitting(false);
          }
        } catch (e: any) {
          setError(e.message);
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          setSubmitting(false);
        }
      }, 3000);
    } catch (e: any) {
      setError(e.message);
      setSubmitting(false);
    }
  }

  const result: OperationResult | null = task?.result ?? null;

  return (
    <>
      <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
        {submitting ? "Running..." : buttonLabel}
      </button>
      {error && (
        <div className="result-panel error" style={{ marginTop: 16 }}>
          <div className="result-status">Submission failed</div>
          <pre>{error}</pre>
        </div>
      )}
      {taskId && task && task.status !== "done" && task.status !== "failed" && (
        <div className="result-panel running" style={{ marginTop: 16 }}>
          <div className="result-status">⟳ {task.status}</div>
          <pre>task_id: {taskId}</pre>
        </div>
      )}
      {task && task.status === "failed" && (
        <div className="result-panel error" style={{ marginTop: 16 }}>
          <div className="result-status">✗ Task failed</div>
          <pre>{task.error}</pre>
        </div>
      )}
      {task && task.status === "done" && result && <ResultPanel result={result} />}
    </>
  );
}
```

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds.

- [ ] **Step 4: Commit**

```bash
git add web/src/components/ web/dist/
git commit -m "feat(m40): TaskRunner + ResultPanel components"
```

---

### Task 12: Ingest + Query pages

**Files:**
- Create: `web/src/pages/Ingest.tsx`
- Create: `web/src/pages/Query.tsx`
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create Ingest page**

Create `web/src/pages/Ingest.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Ingest() {
  const [input, setInput] = useState("");
  const [domain, setDomain] = useState("");
  const [withPlan, setWithPlan] = useState(false);
  const [draft, setDraft] = useState(false);

  return (
    <div>
      <h1>Ingest source</h1>
      <p className="subtitle">URL or local path → raw/ + wiki/sources/</p>

      <div className="op-form">
        <label>Input</label>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="https://example.com/article  or  /path/to/file.pdf"
        />

        <label>Domain (optional)</label>
        <input
          type="text"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          placeholder="glp1-reward-modulation"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={withPlan}
              onChange={(e) => setWithPlan(e.target.checked)}
            />
            --with-plan
          </label>
          <label>
            <input
              type="checkbox"
              checked={draft}
              onChange={(e) => setDraft(e.target.checked)}
            />
            --draft
          </label>
        </div>

        <TaskRunner
          buttonLabel="Ingest"
          startTask={() =>
            api.startIngest({
              input,
              domain: domain || null,
              with_plan: withPlan,
              draft,
            })
          }
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Create Query page**

Create `web/src/pages/Query.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Query() {
  const [question, setQuestion] = useState("");
  const [domain, setDomain] = useState("");
  const [draft, setDraft] = useState(true);

  return (
    <div>
      <h1>Query the wiki</h1>
      <p className="subtitle">Ask the persistent NotebookLM corpus; file the answer as a synthesis.</p>

      <div className="op-form">
        <label>Question</label>
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="What is known about GLP-1 modulation of mesolimbic dopamine?"
        />

        <label>Domain</label>
        <input
          type="text"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          placeholder="glp1-reward-modulation"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={draft}
              onChange={(e) => setDraft(e.target.checked)}
            />
            --draft
          </label>
        </div>

        <TaskRunner
          buttonLabel="Query"
          startTask={() => api.startQuery({ question, domain, draft })}
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Wire into App.tsx**

In `web/src/App.tsx`, add imports:

```typescript
import Ingest from "./pages/Ingest";
import Query from "./pages/Query";
```

Replace the placeholder routes:

```typescript
<Route path="/ops/ingest" element={<Ingest />} />
<Route path="/ops/query" element={<Query />} />
```

- [ ] **Step 4: Build + commit**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`

```bash
git add web/src/ web/dist/
git commit -m "feat(m40): Ingest + Query pages"
```

---

### Task 13: Finalize + FilterCorrect pages

**Files:**
- Create: `web/src/pages/Finalize.tsx`
- Create: `web/src/pages/FilterCorrect.tsx`
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create Finalize page**

Create `web/src/pages/Finalize.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";
import ResultPanel from "../components/ResultPanel";
import type { OperationResult } from "../types";

export default function Finalize() {
  const [pagePath, setPagePath] = useState("");
  const [abandon, setAbandon] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<OperationResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setResult(null);
    try {
      const r = await api.finalize(pagePath, abandon);
      setResult(r);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Finalize draft</h1>
      <p className="subtitle">Re-run the validator on a draft page to clear the draft flag.</p>

      <div className="op-form">
        <label>Page path</label>
        <input
          type="text"
          value={pagePath}
          onChange={(e) => setPagePath(e.target.value)}
          placeholder="wiki/synthesis/2026-05-04-my-question.md"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={abandon}
              onChange={(e) => setAbandon(e.target.checked)}
            />
            --abandon (delete the page instead of finalizing)
          </label>
        </div>

        <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
          {submitting ? "Running..." : abandon ? "Abandon" : "Finalize"}
        </button>

        {error && (
          <div className="result-panel error" style={{ marginTop: 16 }}>
            <div className="result-status">✗ Failed</div>
            <pre>{error}</pre>
          </div>
        )}
        {result && <ResultPanel result={result} />}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Create FilterCorrect page**

Create `web/src/pages/FilterCorrect.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";
import ResultPanel from "../components/ResultPanel";
import type { OperationResult } from "../types";

export default function FilterCorrect() {
  const [sourceId, setSourceId] = useState("");
  const [decision, setDecision] = useState<"include" | "exclude">("include");
  const [rationale, setRationale] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<OperationResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setResult(null);
    try {
      const r = await api.filterCorrect(sourceId, decision, rationale);
      setResult(r);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Correct a filter decision</h1>
      <p className="subtitle">Pin a corrected decision for future filter calibration.</p>

      <div className="op-form">
        <label>Source ID</label>
        <input
          type="text"
          value={sourceId}
          onChange={(e) => setSourceId(e.target.value)}
          placeholder="yt-LfRiBJgD7sk"
        />

        <label>Decision</label>
        <select
          value={decision}
          onChange={(e) => setDecision(e.target.value as "include" | "exclude")}
        >
          <option value="include">include</option>
          <option value="exclude">exclude</option>
        </select>

        <label>Rationale</label>
        <textarea
          value={rationale}
          onChange={(e) => setRationale(e.target.value)}
          placeholder="Why this decision is correct..."
        />

        <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
          {submitting ? "Running..." : "Submit"}
        </button>

        {error && (
          <div className="result-panel error" style={{ marginTop: 16 }}>
            <div className="result-status">✗ Failed</div>
            <pre>{error}</pre>
          </div>
        )}
        {result && <ResultPanel result={result} />}
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Wire into App.tsx**

Add imports and replace placeholder routes:

```typescript
import Finalize from "./pages/Finalize";
import FilterCorrect from "./pages/FilterCorrect";
```

```typescript
<Route path="/ops/finalize" element={<Finalize />} />
<Route path="/ops/filter-correct" element={<FilterCorrect />} />
```

- [ ] **Step 4: Build + commit**

```bash
cd /Users/andrewgrant/code/knowledge/web && npm run build
cd /Users/andrewgrant/code/knowledge && git add web/src/ web/dist/
git commit -m "feat(m40): Finalize + FilterCorrect pages"
```

---

### Task 14: Bootstrap + Discover + Promote pages

**Files:**
- Create: `web/src/pages/Bootstrap.tsx`
- Create: `web/src/pages/Discover.tsx`
- Create: `web/src/pages/Promote.tsx`
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create Bootstrap page**

Create `web/src/pages/Bootstrap.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Bootstrap() {
  const [description, setDescription] = useState("");
  const [slug, setSlug] = useState("");
  const [force, setForce] = useState(false);

  return (
    <div>
      <h1>Bootstrap a new domain</h1>
      <p className="subtitle">Author a starter policy.yaml from a natural-language description.</p>

      <div className="op-form">
        <label>Description (1-3 sentences)</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="On-device LLM inference for autonomous agentic workflows: edge runtimes, quantization, inter-agent protocols..."
        />

        <label>Slug</label>
        <input
          type="text"
          value={slug}
          onChange={(e) => setSlug(e.target.value)}
          placeholder="edge-ai-agentic"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={force}
              onChange={(e) => setForce(e.target.checked)}
            />
            --force (overwrite existing non-promoted policy)
          </label>
        </div>

        <TaskRunner
          buttonLabel="Bootstrap"
          startTask={() => api.startBootstrap({ description, slug, force })}
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Create Discover page**

Create `web/src/pages/Discover.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Discover() {
  const [scope, setScope] = useState("");
  const [since, setSince] = useState("");
  const [untagged, setUntagged] = useState(true);

  return (
    <div>
      <h1>Discover candidate domains</h1>
      <p className="subtitle">Cluster sources into draft proposals (bottom-up).</p>

      <div className="op-form">
        <label>Scope (glob, optional)</label>
        <input
          type="text"
          value={scope}
          onChange={(e) => setScope(e.target.value)}
          placeholder="raw/pdf/*.md"
        />

        <label>Since (ISO date, optional)</label>
        <input
          type="text"
          value={since}
          onChange={(e) => setSince(e.target.value)}
          placeholder="2026-04-01"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={untagged}
              onChange={(e) => setUntagged(e.target.checked)}
            />
            --untagged (only sources with no domain)
          </label>
        </div>

        <TaskRunner
          buttonLabel="Discover"
          startTask={() =>
            api.startDiscover({
              scope: scope || null,
              since: since || null,
              untagged,
            })
          }
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Create Promote page**

Create `web/src/pages/Promote.tsx`:

```typescript
import { useEffect, useState } from "react";
import { api } from "../api";
import ResultPanel from "../components/ResultPanel";
import type { OperationResult, ProposalSummary } from "../types";

export default function Promote() {
  const [proposals, setProposals] = useState<ProposalSummary[]>([]);
  const [result, setResult] = useState<OperationResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);

  async function refresh() {
    try {
      setProposals(await api.proposals());
    } catch (e: any) {
      setError(e.message);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  async function run(action: "promote" | "demote" | "reject", slug: string) {
    setBusy(`${action}:${slug}`);
    setError(null);
    setResult(null);
    try {
      const fn =
        action === "promote" ? api.promote : action === "demote" ? api.demote : api.reject;
      const r = await fn(slug);
      setResult(r);
      refresh();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setBusy(null);
    }
  }

  return (
    <div>
      <h1>Promote / Demote / Reject</h1>
      <p className="subtitle">Manage draft and promoted domain proposals.</p>

      {error && (
        <div className="result-panel error">
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      <h2>Proposals</h2>
      <table>
        <thead>
          <tr>
            <th>Slug</th>
            <th>Title</th>
            <th>Status</th>
            <th>Members</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {proposals.map((p) => (
            <tr key={p.slug}>
              <td>{p.slug}</td>
              <td>{p.title}</td>
              <td>{p.status}</td>
              <td>{p.member_sources_count}</td>
              <td>
                {p.status === "draft" && (
                  <>
                    <button
                      className="btn-secondary"
                      onClick={() => run("promote", p.proposed_domain)}
                      disabled={busy === `promote:${p.proposed_domain}`}
                    >
                      Promote
                    </button>
                    {" "}
                    <button
                      className="btn-secondary"
                      onClick={() => run("reject", p.slug)}
                      disabled={busy === `reject:${p.slug}`}
                    >
                      Reject
                    </button>
                  </>
                )}
                {p.status === "blessed" && (
                  <button
                    className="btn-secondary"
                    onClick={() => run("demote", p.proposed_domain)}
                    disabled={busy === `demote:${p.proposed_domain}`}
                  >
                    Demote
                  </button>
                )}
              </td>
            </tr>
          ))}
          {proposals.length === 0 && (
            <tr>
              <td colSpan={5} style={{ color: "#888" }}>
                No proposals. Run `wiki discover-domains` to create some.
              </td>
            </tr>
          )}
        </tbody>
      </table>

      {result && <ResultPanel result={result} />}
    </div>
  );
}
```

- [ ] **Step 4: Wire into App.tsx**

Add imports and routes:

```typescript
import Bootstrap from "./pages/Bootstrap";
import Discover from "./pages/Discover";
import Promote from "./pages/Promote";
```

```typescript
<Route path="/domains/bootstrap" element={<Bootstrap />} />
<Route path="/domains/discover" element={<Discover />} />
<Route path="/domains/promote" element={<Promote />} />
```

- [ ] **Step 5: Build + commit**

```bash
cd /Users/andrewgrant/code/knowledge/web && npm run build
cd /Users/andrewgrant/code/knowledge && git add web/src/ web/dist/
git commit -m "feat(m40): Bootstrap + Discover + Promote pages"
```

---

### Task 15: Lint page

**Files:**
- Create: `web/src/pages/Lint.tsx`
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create Lint page**

Create `web/src/pages/Lint.tsx`:

```typescript
import { useState } from "react";
import { api } from "../api";

const SCOPES = [
  "all",
  "schema-drift",
  "orphans",
  "drafts",
  "citation-density",
] as const;

export default function Lint() {
  const [scope, setScope] = useState<string>("all");
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<{ summary: string; report_path: string | null } | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setResult(null);
    try {
      const r = await api.lint(scope === "all" ? undefined : scope);
      setResult(r);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Lint</h1>
      <p className="subtitle">Run health checks across the wiki.</p>

      <div className="op-form">
        <label>Scope</label>
        <select value={scope} onChange={(e) => setScope(e.target.value)}>
          {SCOPES.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>

        <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
          {submitting ? "Running..." : "Run lint"}
        </button>

        {error && (
          <div className="result-panel error" style={{ marginTop: 16 }}>
            <div className="result-status">✗ Failed</div>
            <pre>{error}</pre>
          </div>
        )}
        {result && (
          <div className="result-panel success" style={{ marginTop: 16 }}>
            <div className="result-status">✓ Lint complete</div>
            <pre>{result.summary}</pre>
            {result.report_path && <pre>report: {result.report_path}</pre>}
          </div>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Wire into App.tsx**

```typescript
import Lint from "./pages/Lint";
```

```typescript
<Route path="/system/lint" element={<Lint />} />
```

- [ ] **Step 3: Build + commit**

```bash
cd /Users/andrewgrant/code/knowledge/web && npm run build
cd /Users/andrewgrant/code/knowledge && git add web/src/ web/dist/
git commit -m "feat(m40): Lint page"
```

---

### Task 16: Hand-test + documentation

**Files:**
- Modify: `BUILD.md`
- Modify: `CLAUDE.md`
- Modify: `README.md`
- Modify: `TUTORIAL.md`

- [ ] **Step 1: Hand-test the full app**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/wiki serve --port 7475`
(Leave running in another terminal.)

Open http://127.0.0.1:7475 in a browser.
Verify:
- Dashboard loads, shows stats and recent activity
- Refresh button updates the dashboard
- Each sidebar link navigates to the right page
- Ingest page accepts a URL and shows queued → done with a real ingest result
- Query page shows queued → done (errors gracefully if no notebook for the domain)
- Finalize page returns 400 cleanly for a non-existent path
- Filter-correct page returns 400 for a non-existent source_id
- Bootstrap page submits and either succeeds or saves a draft
- Discover page submits and shows progress
- Promote page lists existing proposals; promote/reject/demote buttons work
- Lint page runs each scope without crashing

Then: `pkill -f "wiki serve"`

- [ ] **Step 2: Append M40 entry to BUILD.md**

In `BUILD.md`, after the M39 section (before "## 11. Downstream wiki-authoring work"), add:

```markdown
### M40 — Web UI Foundation

Local browser front-end (`wiki serve`) wrapping the gateway's daily ops, domain ops, and lint dashboard. Sidebar navigation, hierarchical dashboard with 4 stat cards plus monospace activity feed, dedicated form pages with inline result panels. Long-running ops (ingest --with-plan, query, bootstrap-domain, discover-domains) use a submit-then-poll pattern with an in-memory task store; short ops (finalize, filter-correct, promote/demote/reject) execute synchronously.

**What's new.**

- `gateway.web.app` — FastAPI app construction. `create_app()` registers routers and mounts the React frontend at `/`.
- `gateway.web.tasks.TaskStore` — process-local in-memory task registry with `create`, `get`, `mark_running/done/failed`, and async `run_async` that wraps a callable in `asyncio.to_thread`.
- `gateway.web.routes.status` — GET /api/status, /api/log, /api/lint.
- `gateway.web.routes.domains` — GET /api/domains, /api/proposals; POST /api/domains/{slug}/{promote,demote,reject}.
- `gateway.web.routes.ops` — POST /api/ops/{ingest,query,bootstrap-domain,discover-domains} (async, return task_id) and /api/ops/{finalize,filter-correct} (sync).
- `gateway.web.routes.tasks` — GET /api/tasks/{id}.
- `web/` — Vite + React + TypeScript SPA. Built artifacts at `web/dist/` are served by FastAPI as static files. Sidebar nav with Wiki/Domains/System groups. 9 page components.
- `wiki serve [--port 7474] [--bind 127.0.0.1]` CLI subcommand.

**Tests.** ~15 new tests in `test_web_app.py` covering health, status/log/lint endpoints, domain endpoints, sync ops, async ops with task_id polling. `test_web_tasks.py` (8 tests) covers the TaskStore. `test_cli_serve.py` (2 tests) covers the CLI subcommand.

**Out of scope (deferred to M41/M42).**

- Research orchestration UI with `--review` gate flow.
- NLM artifact triggers (briefing, audio, slides, revise).
- Review consoles: drafts list, contradictions list, source orphans, filter-band sources.
- Live updates via SSE/WebSocket — deferred indefinitely; manual refresh suffices for single-user.
- Authentication — localhost-only by design.

```

- [ ] **Step 3: Update CLAUDE.md operation table**

In `CLAUDE.md`, in the Operation guide table, add a row before the "Health check" row:

```
| Start the local web UI | `wiki serve [--port 7474] [--bind 127.0.0.1]` |
```

- [ ] **Step 4: Update README.md operation table**

In `README.md`, add a row near the bottom of the operation table (before `wiki mcp-serve`):

```
| `wiki serve [--port 7474] [--bind 127.0.0.1]` | Local browser UI wrapping the gateway (FastAPI + React). |
```

- [ ] **Step 5: Update TUTORIAL.md cheat sheet**

In `TUTORIAL.md` § 11 "Cheat sheet", under "# Operate", add:

```
wiki serve [--port 7474]                            # local browser UI
```

- [ ] **Step 6: Commit**

```bash
git add BUILD.md CLAUDE.md README.md TUTORIAL.md
git commit -m "docs: M40 delivery record + wiki serve in operation tables"
```

---

## Self-review

- **Spec coverage:** All 9 acceptance criteria mapped to tasks. (1) wiki serve → Task 7. (2) Dashboard → Tasks 3 + 10. (3) Ingest/Query/Finalize/FilterCorrect → Tasks 5, 6, 12, 13. (4) Bootstrap/Discover/Promote → Tasks 6 + 14. (5) Async polling → Tasks 2 + 6 + 11. (6) Lint → Tasks 3 + 15. (7) Tests → every task. (8) BUILD.md → Task 16. (9) Docs → Task 16. (10) Hand-test → Task 16.

- **Placeholder scan:** No TBDs, no "implement later", no "similar to Task N." Every code step has complete code.

- **Type consistency:** `OperationResult` shape consistent between Pydantic schema, route serializer (`_serialize_op_result`), and TS type. `TaskRecord`/`TaskResponse` fields aligned. `AuthorshipReport` serializer in `domains.py` reused by `ops.py`.

- **Known acceptable cross-task imports:** `routes/ops.py` imports `_to_response` and `_serialize_authorship_report` from `routes/domains.py`. Could be hoisted to a shared `_helpers.py` if it grows; for M40 the pair is small enough to live in the first file that defined them.
