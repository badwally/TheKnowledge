# M43 NLM Artifacts UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wrap existing `wiki nlm-{add,sync,briefing,audio,slides,revise}` ops in HTTP endpoints; add an Artifacts page under the Domains sidebar with confirmation modals on every LLM-calling op (per the artifact-generation-is-opt-in memory rule).

**Architecture:** Reuses M40 FastAPI + React + TaskStore + TaskRunner. New backend module `gateway.web.routes.nlm`. New page `web/src/pages/domains/Artifacts.tsx`. No changes to existing nlm op functions in `gateway/ops/nlm.py` — endpoints are thin adapters.

**Tech Stack:** Python 3.11+, FastAPI, Pydantic, pytest. React 18, TypeScript, Vite. Existing `gateway.ops.nlm.*` functions.

**Spec reference:** `docs/superpowers/specs/2026-05-04-m43-nlm-artifacts-ui-design.md`

---

### Task 1: Sync nlm-add endpoint + artifacts list endpoint

**Files:**
- Create: `src/gateway/web/routes/nlm.py`
- Modify: `src/gateway/web/schemas.py`
- Modify: `src/gateway/web/app.py`
- Test: `tests/gateway/test_web_nlm.py` (new)

- [ ] **Step 1: Write failing tests**

Create `/Users/andrewgrant/code/knowledge/tests/gateway/test_web_nlm.py`:

```python
"""Tests for M43 NLM artifacts endpoints."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway import frontmatter as fm
from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    return TestClient(create_app())


def _seed_artifact(slug, *, artifact_type, domain, created_at, title="t"):
    """Write an artifact wiki page under wiki/artifacts/<artifact_type>/<slug>.md."""
    # Live filesystem uses 'briefing' (singular), not 'briefings'.
    type_dir = artifact_type
    path = paths.wiki_dir() / "artifacts" / type_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "artifact",
        "artifact_type": artifact_type,
        "slug": slug,
        "title": title,
        "domain": domain,
        "created_at": created_at,
        "nlm_artifact_url": f"https://notebooklm.google.com/notebook/x/artifact/{slug}",
    }
    body = f"# {title}\n\nplaceholder\n"
    path.write_text(fm.serialize(front, body))


def test_nlm_add_returns_error_for_unknown_source(client, kb_root):
    """nlm-add wraps the existing op; missing source → 400."""
    resp = client.post(
        "/api/nlm/domains/d-test/add",
        json={"source_id": "yt-nonexistent"},
    )
    assert resp.status_code == 400


def test_artifacts_list_empty_when_no_artifacts(client, kb_root):
    resp = client.get("/api/nlm/domains/d-test/artifacts")
    assert resp.status_code == 200
    assert resp.json() == []


def test_artifacts_list_filters_by_domain(client, kb_root):
    _seed_artifact("alpha-slides", artifact_type="slides",
                   domain="d-test", created_at="2026-05-01T00:00:00Z", title="alpha")
    _seed_artifact("beta-briefing", artifact_type="briefing",
                   domain="d-test", created_at="2026-05-04T00:00:00Z", title="beta")
    _seed_artifact("other-domain", artifact_type="slides",
                   domain="d-other", created_at="2026-05-02T00:00:00Z", title="other")

    resp = client.get("/api/nlm/domains/d-test/artifacts")
    assert resp.status_code == 200
    artifacts = resp.json()
    slugs = {a["slug"] for a in artifacts}
    assert slugs == {"alpha-slides", "beta-briefing"}
    # Newest first
    assert artifacts[0]["slug"] == "beta-briefing"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_nlm.py -v`
Expected: 3 failures (404 — endpoints don't exist).

- [ ] **Step 3: Append schemas**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/schemas.py`:

```python
class NlmAddRequest(BaseModel):
    source_id: str


class ArtifactSummary(BaseModel):
    slug: str
    type: str  # "briefing" | "audio" | "slides"
    title: str
    domain: str
    created_at: str
    nlm_artifact_url: str | None = None
```

- [ ] **Step 4: Create the nlm router**

Create `/Users/andrewgrant/code/knowledge/src/gateway/web/routes/nlm.py`:

```python
"""NLM artifact endpoints (M43)."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.nlm import nlm_add
from gateway.web.routes.domains import _to_response
from gateway.web.schemas import (
    ArtifactSummary,
    NlmAddRequest,
    OperationResultResponse,
)


router = APIRouter(prefix="/api/nlm", tags=["nlm"])


_ARTIFACT_DIRS = ("briefing", "audio", "slides")


@router.post("/domains/{slug}/add", response_model=OperationResultResponse)
def post_nlm_add(slug: str, req: NlmAddRequest) -> OperationResultResponse:
    """Synchronous: add a single source to the domain's NotebookLM corpus."""
    result = nlm_add(slug, req.source_id)
    return _to_response(result)


@router.get("/domains/{slug}/artifacts", response_model=list[ArtifactSummary])
def list_artifacts(slug: str) -> list[ArtifactSummary]:
    """List wiki/artifacts/* pages where frontmatter domain == slug."""
    artifacts_dir = paths.wiki_dir() / "artifacts"
    if not artifacts_dir.exists():
        return []
    out: list[ArtifactSummary] = []
    for type_dir in _ARTIFACT_DIRS:
        d = artifacts_dir / type_dir
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            if str(front.get("domain") or "") != slug:
                continue
            out.append(
                ArtifactSummary(
                    slug=str(front.get("slug") or path.stem),
                    type=str(front.get("artifact_type") or type_dir),
                    title=str(front.get("title") or ""),
                    domain=str(front.get("domain") or ""),
                    created_at=str(front.get("created_at") or ""),
                    nlm_artifact_url=front.get("nlm_artifact_url"),
                )
            )
    out.sort(key=lambda a: a.created_at, reverse=True)
    return out
```

- [ ] **Step 5: Register the router**

Modify `/Users/andrewgrant/code/knowledge/src/gateway/web/app.py`. Add to existing imports:

```python
from gateway.web.routes import nlm as nlm_routes
```

In `create_app()` after the existing `app.include_router` calls:

```python
    app.include_router(nlm_routes.router)
```

- [ ] **Step 6: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_nlm.py -v`
Expected: 3 tests pass.

- [ ] **Step 7: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 530+ pass.

- [ ] **Step 8: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_nlm.py && git commit -m "feat(m43): nlm-add endpoint + per-domain artifacts list"
```

---

### Task 2: Async endpoints — sync, briefing, audio, slides, revise

**Files:**
- Modify: `src/gateway/web/schemas.py`
- Modify: `src/gateway/web/routes/nlm.py`
- Modify: `tests/gateway/test_web_nlm.py`

- [ ] **Step 1: Append failing tests**

Append to `/Users/andrewgrant/code/knowledge/tests/gateway/test_web_nlm.py`:

```python
import time


def test_briefing_returns_task_id(client, kb_root, monkeypatch):
    """POST /api/nlm/domains/{slug}/briefing returns 202 + task_id."""
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    def fake_briefing(domain, **kwargs):
        return OperationResult(success=True, summary=f"stubbed briefing for {domain}")

    monkeypatch.setattr(_nlm, "nlm_briefing", fake_briefing)

    resp = client.post("/api/nlm/domains/d-test/briefing", json={})
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"


def test_audio_takes_topic(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    captured = {}

    def fake_audio(domain, topic, **kwargs):
        captured["domain"] = domain
        captured["topic"] = topic
        return OperationResult(success=True, summary="stub")

    monkeypatch.setattr(_nlm, "nlm_audio", fake_audio)

    resp = client.post(
        "/api/nlm/domains/d-test/audio",
        json={"topic": "endurance training"},
    )
    assert resp.status_code == 202

    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    assert captured["domain"] == "d-test"
    assert captured["topic"] == "endurance training"


def test_slides_takes_topic(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    def fake_slides(domain, topic, **kwargs):
        return OperationResult(success=True, summary=f"stubbed slides {domain}/{topic}")

    monkeypatch.setattr(_nlm, "nlm_slides", fake_slides)

    resp = client.post(
        "/api/nlm/domains/d-test/slides",
        json={"topic": "test topic"},
    )
    assert resp.status_code == 202


def test_sync_takes_optional_args(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    captured = {}

    def fake_sync(domain, *, dry_run=False, limit=None, **kwargs):
        captured["domain"] = domain
        captured["dry_run"] = dry_run
        captured["limit"] = limit
        return OperationResult(success=True, summary="stub sync")

    monkeypatch.setattr(_nlm, "nlm_sync", fake_sync)

    resp = client.post(
        "/api/nlm/domains/d-test/sync",
        json={"dry_run": True, "limit": 10},
    )
    assert resp.status_code == 202

    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    assert captured["domain"] == "d-test"
    assert captured["dry_run"] is True
    assert captured["limit"] == 10


def test_revise_takes_artifact_slug_and_instructions(client, kb_root, monkeypatch):
    from gateway.ops import nlm as _nlm
    from gateway.core import OperationResult

    captured = {}

    def fake_revise(artifact_slug, instructions, **kwargs):
        captured["slug"] = artifact_slug
        captured["instructions"] = instructions
        return OperationResult(success=True, summary="stub revise")

    monkeypatch.setattr(_nlm, "nlm_revise", fake_revise)

    resp = client.post(
        "/api/nlm/artifacts/some-slides/revise",
        json={"instructions": ["slide 2: tighten the mechanism diagram"]},
    )
    assert resp.status_code == 202

    task_id = resp.json()["task_id"]
    for _ in range(20):
        time.sleep(0.1)
        if client.get(f"/api/tasks/{task_id}").json()["status"] in ("done", "failed"):
            break
    assert captured["slug"] == "some-slides"
    assert captured["instructions"] == ["slide 2: tighten the mechanism diagram"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_nlm.py -v`
Expected: 5 failures (404 — async endpoints don't exist).

- [ ] **Step 3: Append schemas**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/schemas.py`:

```python
class NlmSyncRequest(BaseModel):
    dry_run: bool = False
    limit: int | None = None


class NlmTopicRequest(BaseModel):
    """Used for audio + slides — both take a topic string."""
    topic: str


class NlmReviseRequest(BaseModel):
    instructions: list[str]
```

(Note: `NlmBriefingRequest` would be empty; we use a bare `{}` body and skip the schema.)

- [ ] **Step 4: Append async endpoints**

Append to `/Users/andrewgrant/code/knowledge/src/gateway/web/routes/nlm.py`:

```python
import asyncio

from fastapi import Request
from fastapi.responses import JSONResponse

from gateway.ops import nlm as _nlm
from gateway.web.routes.ops import _serialize_op_result
from gateway.web.schemas import (
    NlmReviseRequest,
    NlmSyncRequest,
    NlmTopicRequest,
)


@router.post("/domains/{slug}/sync", status_code=202)
async def post_sync(slug: str, req: NlmSyncRequest, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("nlm-sync")

    def run() -> dict:
        result = _nlm.nlm_sync(slug, dry_run=req.dry_run, limit=req.limit)
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/domains/{slug}/briefing", status_code=202)
async def post_briefing(slug: str, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("nlm-briefing")

    def run() -> dict:
        result = _nlm.nlm_briefing(slug)
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/domains/{slug}/audio", status_code=202)
async def post_audio(
    slug: str, req: NlmTopicRequest, request: Request
) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("nlm-audio")

    def run() -> dict:
        result = _nlm.nlm_audio(slug, req.topic)
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/domains/{slug}/slides", status_code=202)
async def post_slides(
    slug: str, req: NlmTopicRequest, request: Request
) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("nlm-slides")

    def run() -> dict:
        result = _nlm.nlm_slides(slug, req.topic)
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/artifacts/{slug}/revise", status_code=202)
async def post_revise(
    slug: str, req: NlmReviseRequest, request: Request
) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("nlm-revise")

    def run() -> dict:
        result = _nlm.nlm_revise(slug, req.instructions)
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )
```

Note: `_serialize_op_result` is defined in `gateway/web/routes/ops.py` (the M40 async ops route) — same helper that wraps OperationResult into a dict for the task payload.

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_nlm.py -v`
Expected: All 8 tests pass.

- [ ] **Step 6: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 535+ pass.

- [ ] **Step 7: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_nlm.py && git commit -m "feat(m43): async nlm endpoints (sync, briefing, audio, slides, revise)"
```

---

### Task 3: Frontend types + api client extensions

**Files:**
- Modify: `web/src/types.ts`
- Modify: `web/src/api.ts`

- [ ] **Step 1: Append types**

Append to `/Users/andrewgrant/code/knowledge/web/src/types.ts`:

```typescript
export interface ArtifactSummary {
  slug: string;
  type: string;
  title: string;
  domain: string;
  created_at: string;
  nlm_artifact_url: string | null;
}
```

- [ ] **Step 2: Update api.ts**

Open `/Users/andrewgrant/code/knowledge/web/src/api.ts`. Update the import block at the top to include `ArtifactSummary` (add it in alphabetical order to the existing list):

```typescript
import type {
  ArtifactSummary,
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
  // NLM artifacts (M43)
  nlmAdd: (slug: string, source_id: string) =>
    request<OperationResult>(`/api/nlm/domains/${slug}/add`, {
      method: "POST",
      body: JSON.stringify({ source_id }),
    }),
  nlmSync: (slug: string, body: { dry_run?: boolean; limit?: number } = {}) =>
    request<{ task_id: string; status: string }>(
      `/api/nlm/domains/${slug}/sync`,
      { method: "POST", body: JSON.stringify(body) },
    ),
  nlmBriefing: (slug: string) =>
    request<{ task_id: string; status: string }>(
      `/api/nlm/domains/${slug}/briefing`,
      { method: "POST", body: JSON.stringify({}) },
    ),
  nlmAudio: (slug: string, topic: string) =>
    request<{ task_id: string; status: string }>(
      `/api/nlm/domains/${slug}/audio`,
      { method: "POST", body: JSON.stringify({ topic }) },
    ),
  nlmSlides: (slug: string, topic: string) =>
    request<{ task_id: string; status: string }>(
      `/api/nlm/domains/${slug}/slides`,
      { method: "POST", body: JSON.stringify({ topic }) },
    ),
  nlmRevise: (artifact_slug: string, instructions: string[]) =>
    request<{ task_id: string; status: string }>(
      `/api/nlm/artifacts/${artifact_slug}/revise`,
      { method: "POST", body: JSON.stringify({ instructions }) },
    ),
  listArtifacts: (slug: string) =>
    request<ArtifactSummary[]>(`/api/nlm/domains/${slug}/artifacts`),
```

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 4: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/types.ts web/src/api.ts web/dist/ && git commit -m "feat(m43): frontend types + api client for nlm endpoints"
```

---

### Task 4: Artifacts page + sidebar entry

**Files:**
- Create: `web/src/pages/domains/Artifacts.tsx`
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create Artifacts.tsx**

Create `/Users/andrewgrant/code/knowledge/web/src/pages/domains/Artifacts.tsx`:

```typescript
import { useEffect, useRef, useState } from "react";
import { api } from "../../api";
import type {
  ArtifactSummary,
  DomainSummary,
  OperationResult,
  TaskResponse,
} from "../../types";

interface ConfirmModalProps {
  title: string;
  body: string;
  onConfirm: () => void;
  onCancel: () => void;
}

function ConfirmModal({ title, body, onConfirm, onCancel }: ConfirmModalProps) {
  return (
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
      onClick={onCancel}
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
        <h3 style={{ marginTop: 0 }}>{title}</h3>
        <p style={{ fontSize: 13, color: "#444" }}>{body}</p>
        <div style={{ marginTop: 12, display: "flex", gap: 8, justifyContent: "flex-end" }}>
          <button className="btn-secondary" onClick={onCancel}>
            Cancel
          </button>
          <button className="btn-primary" onClick={onConfirm}>
            Confirm & generate
          </button>
        </div>
      </div>
    </div>
  );
}

interface ReviseModalProps {
  artifactSlug: string;
  onConfirm: (instructions: string[]) => void;
  onCancel: () => void;
}

function ReviseModal({ artifactSlug, onConfirm, onCancel }: ReviseModalProps) {
  const [rows, setRows] = useState<Array<{ slide: string; text: string }>>([
    { slide: "", text: "" },
  ]);

  function addRow() {
    setRows((r) => [...r, { slide: "", text: "" }]);
  }

  function update(i: number, field: "slide" | "text", value: string) {
    setRows((r) => r.map((row, idx) => (idx === i ? { ...row, [field]: value } : row)));
  }

  function submit() {
    const instructions = rows
      .filter((r) => r.slide.trim() && r.text.trim())
      .map((r) => `slide ${r.slide.trim()}: ${r.text.trim()}`);
    if (instructions.length === 0) return;
    onConfirm(instructions);
  }

  return (
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
      onClick={onCancel}
    >
      <div
        style={{
          background: "white",
          borderRadius: 6,
          padding: 20,
          width: 560,
          maxWidth: "90%",
          boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <h3 style={{ marginTop: 0 }}>
          Revise <code style={{ fontSize: 12 }}>{artifactSlug}</code>
        </h3>
        {rows.map((r, i) => (
          <div key={i} style={{ marginBottom: 8, display: "flex", gap: 6, alignItems: "flex-start" }}>
            <span style={{ fontSize: 11, paddingTop: 6 }}>Slide</span>
            <input
              type="text"
              value={r.slide}
              onChange={(e) => update(i, "slide", e.target.value)}
              placeholder="N"
              style={{ width: 60, fontSize: 12, padding: 6, border: "1px solid #ccc", borderRadius: 3 }}
            />
            <textarea
              value={r.text}
              onChange={(e) => update(i, "text", e.target.value)}
              placeholder="instructions for this slide…"
              style={{
                flex: 1,
                fontSize: 12,
                padding: 6,
                border: "1px solid #ccc",
                borderRadius: 3,
                minHeight: 40,
                fontFamily: "inherit",
                resize: "vertical",
              }}
            />
          </div>
        ))}
        <button
          onClick={addRow}
          style={{ fontSize: 11, color: "#1a4c8e", background: "none", border: "none", cursor: "pointer", padding: "4px 0" }}
        >
          + Add another revision
        </button>
        <div style={{ marginTop: 12, display: "flex", gap: 8, justifyContent: "flex-end" }}>
          <button className="btn-secondary" onClick={onCancel}>
            Cancel
          </button>
          <button className="btn-primary" onClick={submit}>
            Confirm & revise
          </button>
        </div>
      </div>
    </div>
  );
}

interface AsyncOpState {
  taskId: string | null;
  status: "queued" | "running" | "done" | "failed" | null;
  result: OperationResult | null;
  error: string | null;
}

const INITIAL_OP: AsyncOpState = { taskId: null, status: null, result: null, error: null };

function useAsyncOp(): [AsyncOpState, (start: () => Promise<{ task_id: string; status: string }>) => Promise<void>] {
  const [state, setState] = useState<AsyncOpState>(INITIAL_OP);
  const intervalRef = useRef<number | null>(null);

  useEffect(() => {
    return () => {
      if (intervalRef.current) window.clearInterval(intervalRef.current);
    };
  }, []);

  async function trigger(start: () => Promise<{ task_id: string; status: string }>) {
    setState({ taskId: null, status: "queued", result: null, error: null });
    try {
      const ack = await start();
      setState((s) => ({ ...s, taskId: ack.task_id }));
      intervalRef.current = window.setInterval(async () => {
        try {
          const t: TaskResponse = await api.getTask(ack.task_id);
          if (t.status === "done") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setState({ taskId: ack.task_id, status: "done", result: t.result, error: null });
          } else if (t.status === "failed") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setState({ taskId: ack.task_id, status: "failed", result: null, error: t.error });
          } else {
            setState((s) => ({ ...s, status: t.status }));
          }
        } catch (e) {
          setState((s) => ({
            ...s,
            status: "failed",
            error: e instanceof Error ? e.message : String(e),
          }));
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
        }
      }, 3000);
    } catch (e) {
      setState({
        taskId: null,
        status: "failed",
        result: null,
        error: e instanceof Error ? e.message : String(e),
      });
    }
  }

  return [state, trigger];
}

function OpStatus({ label, state }: { label: string; state: AsyncOpState }) {
  if (!state.status) return null;
  if (state.status === "queued" || state.status === "running") {
    return (
      <div className="result-panel running" style={{ marginTop: 8 }}>
        <div className="result-status">⟳ {label}: {state.status}</div>
      </div>
    );
  }
  if (state.status === "failed") {
    return (
      <div className="result-panel error" style={{ marginTop: 8 }}>
        <div className="result-status">✗ {label} failed</div>
        <pre>{state.error ?? ""}</pre>
      </div>
    );
  }
  if (state.status === "done" && state.result) {
    return (
      <div className="result-panel success" style={{ marginTop: 8 }}>
        <div className="result-status">✓ {label} done</div>
        <pre>{state.result.summary}</pre>
        {state.result.paths_touched.length > 0 && (
          <pre>{state.result.paths_touched.map((p) => `  touched: ${p}`).join("\n")}</pre>
        )}
      </div>
    );
  }
  return null;
}

export default function Artifacts() {
  const [domains, setDomains] = useState<DomainSummary[]>([]);
  const [selectedSlug, setSelectedSlug] = useState<string>("");
  const [artifacts, setArtifacts] = useState<ArtifactSummary[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loadingDomains, setLoadingDomains] = useState(true);

  // Add-source form
  const [sourceId, setSourceId] = useState("");
  const [addBusy, setAddBusy] = useState(false);
  const [addResult, setAddResult] = useState<OperationResult | null>(null);

  // Topic inputs
  const [audioTopic, setAudioTopic] = useState("");
  const [slidesTopic, setSlidesTopic] = useState("");

  // Async ops
  const [syncState, runSync] = useAsyncOp();
  const [briefingState, runBriefing] = useAsyncOp();
  const [audioState, runAudio] = useAsyncOp();
  const [slidesState, runSlides] = useAsyncOp();
  const [reviseState, runRevise] = useAsyncOp();

  // Confirm modals
  const [confirm, setConfirm] = useState<
    | { kind: "sync" | "briefing" | "audio" | "slides"; title: string; body: string; onConfirm: () => void }
    | null
  >(null);

  // Revise modal
  const [reviseTarget, setReviseTarget] = useState<string | null>(null);

  async function loadDomains() {
    setLoadingDomains(true);
    setError(null);
    try {
      const all = await api.domains();
      const withNotebook = all.filter((d) => d.has_notebook);
      setDomains(withNotebook);
      if (!selectedSlug && withNotebook.length > 0) {
        setSelectedSlug(withNotebook[0].slug);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoadingDomains(false);
    }
  }

  async function loadArtifacts(slug: string) {
    if (!slug) {
      setArtifacts([]);
      return;
    }
    try {
      setArtifacts(await api.listArtifacts(slug));
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    }
  }

  useEffect(() => {
    loadDomains();
  }, []);

  useEffect(() => {
    loadArtifacts(selectedSlug);
  }, [selectedSlug]);

  async function addSource() {
    if (!sourceId.trim() || !selectedSlug) return;
    setAddBusy(true);
    setAddResult(null);
    setError(null);
    try {
      const r = await api.nlmAdd(selectedSlug, sourceId.trim());
      setAddResult(r);
      setSourceId("");
      loadArtifacts(selectedSlug);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setAddBusy(false);
    }
  }

  function confirmSync() {
    setConfirm({
      kind: "sync",
      title: `Sync all sources for ${selectedSlug}?`,
      body: `Adds every raw source tagged with ${selectedSlug} to its NotebookLM corpus. Idempotent. May take minutes for large domains.`,
      onConfirm: () => {
        setConfirm(null);
        runSync(() => api.nlmSync(selectedSlug));
      },
    });
  }

  function confirmBriefing() {
    setConfirm({
      kind: "briefing",
      title: `Generate briefing for ${selectedSlug}?`,
      body: "Calls NotebookLM and may take 1-5 minutes. Confirm to proceed.",
      onConfirm: () => {
        setConfirm(null);
        runBriefing(() => api.nlmBriefing(selectedSlug));
      },
    });
  }

  function confirmAudio() {
    if (!audioTopic.trim()) return;
    setConfirm({
      kind: "audio",
      title: `Generate audio for ${selectedSlug}?`,
      body: `Topic: "${audioTopic.trim()}". Calls NotebookLM and may take 1-5 minutes.`,
      onConfirm: () => {
        setConfirm(null);
        runAudio(() => api.nlmAudio(selectedSlug, audioTopic.trim()));
      },
    });
  }

  function confirmSlides() {
    if (!slidesTopic.trim()) return;
    setConfirm({
      kind: "slides",
      title: `Generate slides for ${selectedSlug}?`,
      body: `Topic: "${slidesTopic.trim()}". Calls NotebookLM and may take 1-5 minutes.`,
      onConfirm: () => {
        setConfirm(null);
        runSlides(() => api.nlmSlides(selectedSlug, slidesTopic.trim()));
      },
    });
  }

  function submitRevise(instructions: string[]) {
    if (!reviseTarget) return;
    const target = reviseTarget;
    setReviseTarget(null);
    runRevise(() => api.nlmRevise(target, instructions));
  }

  return (
    <div>
      <h1>Artifacts</h1>
      <p className="subtitle">
        Manage a domain's NotebookLM corpus and generate briefings, audio overviews, and slide decks.
      </p>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      <div style={{ marginBottom: 16 }}>
        <label style={{ fontSize: 11, textTransform: "uppercase", color: "#666" }}>
          Domain
        </label>
        <select
          value={selectedSlug}
          onChange={(e) => setSelectedSlug(e.target.value)}
          disabled={loadingDomains}
          style={{
            display: "block",
            marginTop: 4,
            fontSize: 13,
            padding: "5px 8px",
            border: "1px solid #ccc",
            borderRadius: 3,
            minWidth: 320,
          }}
        >
          {domains.length === 0 && <option value="">(no domains with NotebookLM corpus)</option>}
          {domains.map((d) => (
            <option key={d.slug} value={d.slug}>
              {d.slug} — {d.topic}
            </option>
          ))}
        </select>
      </div>

      {selectedSlug && (
        <>
          <h2>Add source to corpus</h2>
          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Source ID</label>
            <input
              type="text"
              value={sourceId}
              onChange={(e) => setSourceId(e.target.value)}
              placeholder="yt-LfRiBJgD7sk"
            />
            <div style={{ marginTop: 8, display: "flex", gap: 8, alignItems: "center" }}>
              <button className="btn-primary" onClick={addSource} disabled={addBusy}>
                {addBusy ? "Adding…" : "Add"}
              </button>
              <button className="btn-secondary" onClick={confirmSync}>
                Sync all sources for this domain
              </button>
            </div>
            {addResult && (
              <div
                className={addResult.success ? "result-panel success" : "result-panel error"}
                style={{ marginTop: 8 }}
              >
                <div className="result-status">{addResult.success ? "✓ Added" : "✗ Failed"}</div>
                <pre>{addResult.summary}</pre>
              </div>
            )}
            <OpStatus label="Sync" state={syncState} />
          </div>

          <h2>Generate artifact</h2>
          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Briefing (no topic — uses corpus-wide context)</label>
            <button
              className="btn-primary"
              onClick={confirmBriefing}
              disabled={briefingState.status === "queued" || briefingState.status === "running"}
              style={{ marginTop: 4 }}
            >
              Generate briefing
            </button>
            <OpStatus label="Briefing" state={briefingState} />
          </div>

          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Audio overview — Topic</label>
            <input
              type="text"
              value={audioTopic}
              onChange={(e) => setAudioTopic(e.target.value)}
              placeholder="e.g., reward circuit primer"
            />
            <button
              className="btn-primary"
              onClick={confirmAudio}
              disabled={!audioTopic.trim() || audioState.status === "queued" || audioState.status === "running"}
              style={{ marginTop: 8 }}
            >
              Generate audio
            </button>
            <OpStatus label="Audio" state={audioState} />
          </div>

          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Slide deck — Topic</label>
            <input
              type="text"
              value={slidesTopic}
              onChange={(e) => setSlidesTopic(e.target.value)}
              placeholder="e.g., alcohol use disorder evidence"
            />
            <button
              className="btn-primary"
              onClick={confirmSlides}
              disabled={!slidesTopic.trim() || slidesState.status === "queued" || slidesState.status === "running"}
              style={{ marginTop: 8 }}
            >
              Generate slides
            </button>
            <OpStatus label="Slides" state={slidesState} />
          </div>

          <h2>Existing artifacts</h2>
          {artifacts.length === 0 && (
            <div style={{ color: "#888", fontSize: 12 }}>No artifacts for this domain yet.</div>
          )}
          {artifacts.length > 0 && (
            <table>
              <thead>
                <tr>
                  <th>Slug</th>
                  <th>Type</th>
                  <th>Title</th>
                  <th>Created</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {artifacts.map((a) => (
                  <tr key={a.slug}>
                    <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                      {a.slug}
                    </td>
                    <td>{a.type}</td>
                    <td style={{ fontSize: 11, maxWidth: 280, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {a.title}
                    </td>
                    <td style={{ fontSize: 11 }}>{a.created_at}</td>
                    <td>
                      {a.type === "slides" && (
                        <button
                          className="btn-secondary"
                          onClick={() => setReviseTarget(a.slug)}
                          style={{ fontSize: 11, marginRight: 6 }}
                        >
                          Revise
                        </button>
                      )}
                      {a.nlm_artifact_url && (
                        <a
                          href={a.nlm_artifact_url}
                          target="_blank"
                          rel="noreferrer"
                          className="btn-secondary"
                          style={{ fontSize: 11, textDecoration: "none", padding: "3px 8px" }}
                        >
                          Open in NotebookLM
                        </a>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
          <OpStatus label="Revise" state={reviseState} />
        </>
      )}

      {confirm && (
        <ConfirmModal
          title={confirm.title}
          body={confirm.body}
          onConfirm={confirm.onConfirm}
          onCancel={() => setConfirm(null)}
        />
      )}

      {reviseTarget && (
        <ReviseModal
          artifactSlug={reviseTarget}
          onConfirm={submitRevise}
          onCancel={() => setReviseTarget(null)}
        />
      )}
    </div>
  );
}
```

- [ ] **Step 2: Wire into App.tsx**

In `/Users/andrewgrant/code/knowledge/web/src/App.tsx`, add the import:

```typescript
import Artifacts from "./pages/domains/Artifacts";
```

In the `Sidebar` component, find the existing Domains group:

```typescript
      <div className="sidebar-group-label">Domains</div>
      <NavLink to="/domains/bootstrap">Bootstrap</NavLink>
      <NavLink to="/domains/discover">Discover</NavLink>
      <NavLink to="/domains/promote">Promote</NavLink>
```

Append a new entry:

```typescript
      <NavLink to="/domains/artifacts">Artifacts</NavLink>
```

In the `<Routes>` block, alongside the existing `/domains/*` routes:

```typescript
<Route path="/domains/artifacts" element={<Artifacts />} />
```

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 4: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/ web/dist/ && git commit -m "feat(m43): Artifacts page with confirmation modals + revise modal"
```

---

### Task 5: Hand-test + documentation

**Files:**
- Modify: `BUILD.md`
- Modify: `CLAUDE.md`
- Modify: `TUTORIAL.md`

- [ ] **Step 1: Hand-test the endpoints**

Run: `cd /Users/andrewgrant/code/knowledge && pkill -f "wiki serve" 2>/dev/null; sleep 1; .venv/bin/wiki serve --port 7475 &`
Wait 3 seconds, then verify each endpoint returns the expected status:

```bash
echo "=== /api/nlm/domains/cycling-and-fitness/artifacts ==="
curl -s http://127.0.0.1:7475/api/nlm/domains/cycling-and-fitness/artifacts | python3 -c 'import sys,json; d=json.load(sys.stdin); print(len(d), "artifacts")'

echo "=== /domains/artifacts (HTML) ==="
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:7475/domains/artifacts

pkill -f "wiki serve"
```

Open http://127.0.0.1:7475/domains/artifacts in a browser. Verify:
- Domain dropdown lists domains with `has_notebook=true`
- Selecting a domain loads its existing artifacts
- Clicking "Generate briefing" opens a confirmation modal (do NOT submit — would burn NLM quota)
- Slide-deck row's Revise button opens the revise modal (do NOT submit)
- Add-source form is visible

Skip live NLM generation in the hand-test — round-trip tests with stubs cover the API contract.

- [ ] **Step 2: Append BUILD.md M43 entry**

In `/Users/andrewgrant/code/knowledge/BUILD.md`, after the M42 section (before "## 11. Downstream wiki-authoring work"), add:

```markdown
### M43 — NLM Artifacts UI

Adds a new Artifacts page under the Domains sidebar group at `/domains/artifacts`. Wraps the existing `wiki nlm-{add,sync,briefing,audio,slides,revise}` ops in HTTP endpoints. Confirmation modal before every LLM-calling op (per the artifact-generation-is-opt-in memory rule). Async generation via M40's TaskStore + 3s polling.

**What's new.**

- `gateway.web.routes.nlm` — 7 endpoints: nlm-add (sync); sync/briefing/audio/slides/revise (async, return 202+task_id); GET artifacts list per domain.
- `web/src/pages/domains/Artifacts.tsx` — single page with domain dropdown, add-source form, sync button, three artifact-generation cards (briefing/audio/slides), per-row revise on slide-deck artifacts. Confirmation modal before every async op.
- Sidebar gains an "Artifacts" entry under the Domains group.
- No changes to underlying `gateway.ops.nlm.*` functions — endpoints are thin adapters that reuse `_serialize_op_result` from M40 and `_to_response` from M40 domains route.

**Tests.** 8 new tests in `test_web_nlm.py` covering: artifacts list (empty, multi-domain filter, sort), nlm-add error path, async briefing/audio/slides/sync (with stubbed ops), revise (artifact-slug routing). Full gateway suite: 527 → 535+ tests passing.

**Hand-test.** Started server on port 7475, verified `/api/nlm/domains/cycling-and-fitness/artifacts` returns the existing on-disk artifacts; `/domains/artifacts` SPA route serves React HTML at 200. Live NLM generation skipped to avoid burning quota — TestClient stubs cover the contract.

**Out of scope (M44+).**

- Bulk actions on review tabs.
- Filter/search within review tabs.
- Obsidian:// deep-links for synthesis pages.
- Custom artifact types beyond what NotebookLM exposes.
- Artifact deletion from the UI (delete the wiki page directly).
- In-browser audio playback or slide-deck rendering.
```

- [ ] **Step 3: Update CLAUDE.md operation table**

In `/Users/andrewgrant/code/knowledge/CLAUDE.md`, find the existing `wiki serve` row:

```
| Start the local web UI (FastAPI + React) | `wiki serve [--port 7474] [--bind 127.0.0.1]` (visit `/research` for orchestration UI; `/review` for curation queues) |
```

Replace with:

```
| Start the local web UI (FastAPI + React) | `wiki serve [--port 7474] [--bind 127.0.0.1]` (visit `/research`, `/review`, `/domains/artifacts`) |
```

- [ ] **Step 4: Update TUTORIAL.md**

In `/Users/andrewgrant/code/knowledge/TUTORIAL.md` § 11 "Cheat sheet", update the wiki serve line:

```
wiki serve [--port 7474]                           # local browser UI; /research · /review · /domains/artifacts
```

- [ ] **Step 5: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add BUILD.md CLAUDE.md TUTORIAL.md && git commit -m "docs: M43 delivery record + Artifacts page in operation tables"
```

---

## Self-review

**Spec coverage:**

| Spec § | Tasks |
|---|---|
| § 1 Architecture | Tasks 1-5 cumulative |
| § 2 Endpoints (7) | Tasks 1 (add+artifacts list), 2 (sync, briefing, audio, slides, revise) |
| § 2 Pydantic schemas | Tasks 1-2 |
| § 3 Frontend page layout | Task 4 |
| § 3 Confirmation modals | Task 4 (`ConfirmModal`) |
| § 3 Revise modal | Task 4 (`ReviseModal`) |
| § 3 TaskRunner reuse | Task 4 (`useAsyncOp` hook + `OpStatus`) |
| § 4 Async pattern | Task 2 + Task 4 polling |
| § 5 Out of scope | Documented in Task 5 BUILD.md entry |
| § 7 Acceptance criteria 1-8 | All mapped to tasks |

**Placeholder scan:** No TBDs. The hand-test step in Task 5 is explicit about which buttons to click and which to avoid (don't burn NLM quota).

**Type consistency:**
- `ArtifactSummary` shape matches between Pydantic (Task 1) and TS types (Task 3).
- `NlmTopicRequest` is shared between audio + slides — same shape, different endpoints.
- `_to_response` (M42) and `_serialize_op_result` (M40) are reused from existing M40/M42 routes — no new helpers introduced.
- `useAsyncOp` hook (Task 4) is local to `Artifacts.tsx` — not a shared component, since the existing `<TaskRunner>` is form-bound and doesn't fit the multi-button page layout.

**Cross-task assumptions verified during plan-writing:**
- `gateway.ops.nlm.{nlm_add,nlm_sync,nlm_briefing,nlm_audio,nlm_slides,nlm_revise}` exist with the documented signatures (verified via grep).
- `wiki/artifacts/` actually uses `briefing` (singular), not `briefings` — the spec's plural was wrong; this plan corrects to singular in `_ARTIFACT_DIRS`.
- `_to_response` lives in `gateway/web/routes/domains.py` (M40); `_serialize_op_result` lives in `gateway/web/routes/ops.py` (M40). Both are cross-imported.
- `api.domains()` exists (M40) and returns `DomainSummary[]` with `has_notebook` field used to filter the dropdown.
