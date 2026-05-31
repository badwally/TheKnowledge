# M41 Research Orchestration UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Research sidebar entry to `wiki serve` that exposes the existing `wiki research` orchestrator with a sessions-list + detail layout, structured per-adapter plan editor, and per-step execute progress sourced from filtered `log.md`.

**Architecture:** Reuses the M40 FastAPI + Vite/React + TaskRunner foundation. New backend module `src/gateway/web/routes/research.py`. New frontend pages under `web/src/pages/research/`. The orchestrator gains six new `log.append("research", step=...)` calls so the progress endpoint can render every named pipeline stage. No new persistence — sessions are derived from existing on-disk state (`nlm/query_plans/*.yaml` + `nlm_registry` + `log.md`).

**Tech Stack:** Python 3.11+, FastAPI, Pydantic, pytest. React 18, TypeScript, Vite. Existing `gateway.research.orchestrator`, `gateway.research.query_plan_store`, `gateway.research.query_planner`, `gateway.nlm_registry`.

**Spec reference:** `docs/superpowers/specs/2026-05-04-m41-research-orchestration-ui-design.md`

---

### Task 1: Canonicalize orchestrator log step names

**Files:**
- Modify: `src/gateway/research/orchestrator.py`
- Test: `tests/gateway/test_research_orchestrator.py` (extend)

**Why this comes first:** the M41 progress endpoint parses `log.md` for `op="research"` entries and maps `step` field values to UI rows. The orchestrator currently emits log entries for `start`, `plan`, `search`, `merge`, `filter`, `source_add`, `abandon`, and `promoted`, but is silent for materialize / nlm_persistent / nlm_session / source_map / analysis / apply_plan. M41 adds explicit log entries for those steps so the progress UI can light them up.

- [ ] **Step 1: Identify the gaps**

Read `src/gateway/research/orchestrator.py` around lines 825-1080 (the main `research()` function). Confirm the named steps that emit `log.append("research", ...)` calls. Currently:

- `start` (entry, with effective_domain) — line ~828
- `plan` (after planner) — lines ~679, ~852
- `search` (per adapter, after fan-out) — lines ~160, ~190
- `merge` (after dedup) — line ~881
- `filter` (after filter) — line ~903
- `source_add` (after pushing all sources) — line ~996
- `abandon` (on failure) — line ~1063
- `promoted` (on full success) — line ~1073

Missing log entries (silent steps):
- `materialize` (after `_materialize` returns) — line ~915
- `nlm_persistent` (after fetching/creating persistent notebook) — line ~944
- `nlm_session` (after creating session notebook) — line ~956
- `source_map` (after `build_source_map`) — line ~1011
- `analysis` (after `_analysis.analyze`) — line ~1024
- `apply_plan` (after `apply_plan`) — line ~1038

- [ ] **Step 2: Write a failing test for the new log entries**

Append to `tests/gateway/test_research_orchestrator.py` (or wherever the orchestrator tests live — find via `grep -l "def test.*research" tests/gateway/`):

```python
def test_orchestrator_emits_canonical_step_log_entries(kb_root, monkeypatch):
    """Every named pipeline stage emits log.append('research', step=<name>)."""
    from gateway import paths
    from gateway.research import orchestrator as _orch

    # Capture every log.append call
    captured: list[tuple[str, dict, str]] = []
    real_append = _orch.log.append

    def capturing(op, fields=None, summary=""):
        captured.append((op, fields or {}, summary))
        return real_append(op, fields=fields, summary=summary)

    monkeypatch.setattr(_orch.log, "append", capturing)

    # Find the existing dry-run-style orchestrator test setup; reuse its fixture.
    # If this test runs end-to-end with a mocked plan client + filter client +
    # nlm client + adapter, we can assert the full step set.
    # This test asserts the SET of steps observed, not the order or summary.
    expected_steps = {
        "start", "plan", "search", "merge", "filter",
        "materialize", "nlm_persistent", "nlm_session",
        "source_add", "source_map", "analysis", "apply_plan",
        "promoted",
    }

    # Run a minimal end-to-end research call; details depend on existing test
    # fixtures — adapt to whatever stub clients the existing M37 tests use.
    # Pass dry_run=False so the full pipeline runs.
    # ... (test body — adapt to existing fixture pattern in test_research_orchestrator.py)

    research_steps = {
        f["step"] for op, f, _ in captured if op == "research" and "step" in f
    }
    missing = expected_steps - research_steps
    assert not missing, f"missing canonical steps: {missing}"
```

If the existing test file has a working end-to-end fixture, base the new test on it. If not, this task is harder to test in isolation — proceed by adding the log entries (Step 3) and running the existing M37 orchestrator tests; manually verify by triggering one research run via CLI and grepping log.md.

- [ ] **Step 3: Add the missing log.append calls**

In `src/gateway/research/orchestrator.py`:

After `materialized = _materialize(accepted, session_id=session_id)` (line ~916), before the `if not materialized:` block, add:

```python
    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "materialize",
            "n": len(materialized),
        },
        summary=f"materialized {len(materialized)} source(s) to raw/",
    )
```

After `persistent_id = nlm_client.notebook_create(...)` and the `nlm_registry.register(effective_domain, persistent_id)` block (around line ~944), add (handle both create and reuse cases):

```python
    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "nlm_persistent",
            "notebook_id": persistent_id,
        },
        summary=f"persistent notebook {persistent_id}",
    )
```

After `nlm_registry.register_session(effective_domain, session_id, session_nb_id, query=prompt)` (line ~957), add:

```python
    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "nlm_session",
            "notebook_id": session_nb_id,
        },
        summary=f"created session notebook {session_nb_id}",
    )
```

After `smap = _source_map.build_source_map(session_nb_id, client=nlm_client)` (line ~1011), add:

```python
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "source_map",
                "n": len(smap or {}),
            },
            summary=f"built source map ({len(smap or {})} entries)",
        )
```

After `analysis_result = _analysis.analyze(...)` (line ~1024), add:

```python
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "analysis",
                "branches": len(getattr(analysis_result, "branches", []) or []),
            },
            summary=f"analysis complete ({len(getattr(analysis_result, 'branches', []) or [])} branch(es))",
        )
```

After `plan_result = apply_plan(plan, draft=draft)` and the success check (line ~1042), add:

```python
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "apply_plan",
                "pages": len(plan_result.paths_touched),
            },
            summary=f"applied plan: {plan_result.summary}",
        )
```

- [ ] **Step 4: Run existing orchestrator tests for regressions**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_research_orchestrator.py -v`
Expected: All tests still pass (the new log entries are additive).

If a test asserts a specific count of `log.append` calls, update it to match the new count.

- [ ] **Step 5: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 504+ pass, no regressions.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/research/orchestrator.py tests/gateway/test_research_orchestrator.py && git commit -m "feat(m41): canonicalize research orchestrator log step names

Adds log.append('research', step=<name>) calls for materialize,
nlm_persistent, nlm_session, source_map, analysis, apply_plan so the
M41 progress endpoint can render every named pipeline stage."
```

---

### Task 2: Sessions list endpoint

**Files:**
- Create: `src/gateway/web/routes/research.py`
- Modify: `src/gateway/web/schemas.py` (append session models)
- Modify: `src/gateway/web/app.py` (register router)
- Test: `tests/gateway/test_web_research.py` (new)

- [ ] **Step 1: Write failing test**

Create `tests/gateway/test_web_research.py`:

```python
"""Tests for M41 research orchestration UI endpoints."""

from __future__ import annotations

import pytest
import yaml
from fastapi.testclient import TestClient

from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    return TestClient(create_app())


def _seed_query_plan(session_id: str, *, domain: str, prompt: str, queries: dict | None = None):
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    plans_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "version": 1,
        "session_id": session_id,
        "domain": domain,
        "prompt": prompt,
        "generated_at": "2026-05-01T12:00:00Z",
        "plan_client_model": None,
        "target_counts": {"arxiv": 8, "youtube": 20, "web": 15, "pubmed": 5},
        "queries": queries or {"arxiv": ["q1", "q2"], "youtube": [], "web": [], "pubmed": []},
    }
    (plans_dir / f"{session_id}.yaml").write_text(yaml.safe_dump(data, sort_keys=False))


def test_list_sessions_returns_empty_when_no_plans(client):
    resp = client.get("/api/research/sessions")
    assert resp.status_code == 200
    assert resp.json() == []


def test_list_sessions_returns_plan_only_state(client, kb_root):
    _seed_query_plan("2026-05-01-test-session", domain="d-test", prompt="x")
    resp = client.get("/api/research/sessions")
    assert resp.status_code == 200
    sessions = resp.json()
    assert len(sessions) == 1
    s = sessions[0]
    assert s["session_id"] == "2026-05-01-test-session"
    assert s["state"] == "plan_only"
    assert s["domain"] == "d-test"
    assert s["query_count"] == 2  # 2 arxiv, 0 youtube/web/pubmed


def test_list_sessions_sorted_newest_first(client, kb_root):
    _seed_query_plan("2026-05-01-old", domain="d-test", prompt="x")
    # Newer generated_at
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    new_plan = plans_dir / "2026-05-04-new.yaml"
    data = yaml.safe_load(new_plan.parent.glob("*.yaml").__next__().read_text())
    data["session_id"] = "2026-05-04-new"
    data["generated_at"] = "2026-05-04T12:00:00Z"
    new_plan.write_text(yaml.safe_dump(data, sort_keys=False))

    resp = client.get("/api/research/sessions")
    sessions = resp.json()
    assert sessions[0]["session_id"] == "2026-05-04-new"
    assert sessions[1]["session_id"] == "2026-05-01-old"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: FAIL — `/api/research/sessions` endpoint doesn't exist (returns 404).

- [ ] **Step 3: Add session schemas**

Append to `src/gateway/web/schemas.py`:

```python
class ResearchSessionSummary(BaseModel):
    session_id: str
    prompt: str
    domain: str
    state: str  # plan_only | edited | running | done | abandoned
    generated_at: str
    edited: bool = False
    query_count: int = 0
    sources_count: int | None = None
```

- [ ] **Step 4: Create research router**

Create `src/gateway/web/routes/research.py`:

```python
"""Research orchestration endpoints (M41)."""

from __future__ import annotations

from pathlib import Path

import yaml
from fastapi import APIRouter

from gateway import nlm_registry, paths
from gateway.web.schemas import ResearchSessionSummary


router = APIRouter(prefix="/api/research", tags=["research"])


_SLACK_SECONDS = 2.0


@router.get("/sessions", response_model=list[ResearchSessionSummary])
def list_sessions(request_app=None) -> list[ResearchSessionSummary]:
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    if not plans_dir.is_dir():
        return []

    out: list[ResearchSessionSummary] = []
    for path in plans_dir.glob("*.yaml"):
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict):
            continue
        session_id = str(data.get("session_id") or path.stem)
        domain = str(data.get("domain") or "")
        prompt = str(data.get("prompt") or "")
        generated_at = str(data.get("generated_at") or "")

        queries = data.get("queries") or {}
        query_count = sum(len(v or []) for v in queries.values()) if isinstance(queries, dict) else 0

        edited = _is_edited(path, generated_at)
        state = _derive_state(domain, session_id, edited)
        sources_count = _sources_count(domain, session_id)

        out.append(
            ResearchSessionSummary(
                session_id=session_id,
                prompt=prompt,
                domain=domain,
                state=state,
                generated_at=generated_at,
                edited=edited,
                query_count=query_count,
                sources_count=sources_count,
            )
        )

    out.sort(key=lambda s: s.generated_at, reverse=True)
    return out


def _is_edited(path: Path, generated_at: str) -> bool:
    """YAML mtime > generated_at + 2s slack."""
    if not generated_at:
        return False
    from datetime import datetime, timezone

    try:
        gen_dt = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    try:
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    except OSError:
        return False
    return mtime.timestamp() > gen_dt.timestamp() + _SLACK_SECONDS


def _derive_state(domain: str, session_id: str, edited: bool) -> str:
    """Compute lifecycle state from registry + edit flag.

    Returns one of: plan_only | edited | running | done | abandoned.
    'running' is detected at the route level via task_store; this helper
    ignores it. Callers should override to 'running' if a task is active.
    """
    if not domain or not session_id:
        return "edited" if edited else "plan_only"
    sess = nlm_registry.get_session(domain, session_id)
    if sess is None:
        return "edited" if edited else "plan_only"
    status = getattr(sess, "status", None) or sess.get("status") if isinstance(sess, dict) else None
    if status == "promoted":
        return "done"
    if status == "abandoned":
        return "abandoned"
    return "edited" if edited else "plan_only"


def _sources_count(domain: str, session_id: str) -> int | None:
    if not domain or not session_id:
        return None
    sess = nlm_registry.get_session(domain, session_id)
    if sess is None:
        return None
    if isinstance(sess, dict):
        return sess.get("sources_count")
    return getattr(sess, "sources_count", None)
```

Verify the `nlm_registry.get_session` signature matches by reading `src/gateway/nlm_registry.py`. If the function returns a different shape, adjust `_derive_state` and `_sources_count` accordingly.

- [ ] **Step 5: Register router**

In `src/gateway/web/app.py`, add the import and `include_router` call alongside the existing routers:

```python
from gateway.web.routes import research as research_routes
```

```python
    app.include_router(research_routes.router)
```

- [ ] **Step 6: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: 3 tests pass.

- [ ] **Step 7: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_research.py && git commit -m "feat(m41): GET /api/research/sessions endpoint with state derivation"
```

---

### Task 3: Session detail endpoint

**Files:**
- Modify: `src/gateway/web/routes/research.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_research.py` (extend)

- [ ] **Step 1: Append failing tests**

Append to `tests/gateway/test_web_research.py`:

```python
def test_get_session_returns_full_plan(client, kb_root):
    _seed_query_plan(
        "2026-05-04-detail",
        domain="d-test",
        prompt="detail test prompt",
        queries={"arxiv": ["a1", "a2"], "youtube": ["y1"], "web": [], "pubmed": []},
    )
    resp = client.get("/api/research/sessions/2026-05-04-detail")
    assert resp.status_code == 200
    body = resp.json()
    assert body["session_id"] == "2026-05-04-detail"
    assert body["domain"] == "d-test"
    assert body["prompt"] == "detail test prompt"
    assert body["plan"]["queries"]["arxiv"] == ["a1", "a2"]
    assert body["plan"]["queries"]["youtube"] == ["y1"]
    assert body["state"] == "plan_only"


def test_get_unknown_session_returns_404(client):
    resp = client.get("/api/research/sessions/nonexistent")
    assert resp.status_code == 404
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: 2 new failures (404 not registered).

- [ ] **Step 3: Append schemas**

Append to `src/gateway/web/schemas.py`:

```python
class ResearchPlanQueries(BaseModel):
    arxiv: list[str] = []
    youtube: list[str] = []
    web: list[str] = []
    pubmed: list[str] = []


class ResearchPlan(BaseModel):
    queries: ResearchPlanQueries
    target_counts: dict[str, int] = {}


class ResearchSessionDetail(BaseModel):
    session_id: str
    prompt: str
    domain: str
    state: str
    generated_at: str
    edited: bool = False
    plan: ResearchPlan
    sources_count: int | None = None
```

- [ ] **Step 4: Add endpoint**

Append to `src/gateway/web/routes/research.py`:

```python
from fastapi import HTTPException

from gateway.web.schemas import ResearchPlan, ResearchPlanQueries, ResearchSessionDetail


@router.get("/sessions/{session_id}", response_model=ResearchSessionDetail)
def get_session(session_id: str) -> ResearchSessionDetail:
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    path = plans_dir / f"{session_id}.yaml"
    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"unknown session: {session_id}")

    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as e:
        raise HTTPException(status_code=500, detail=f"invalid plan YAML: {e}")
    if not isinstance(data, dict):
        raise HTTPException(status_code=500, detail="plan YAML is not a mapping")

    domain = str(data.get("domain") or "")
    prompt = str(data.get("prompt") or "")
    generated_at = str(data.get("generated_at") or "")
    queries_raw = data.get("queries") or {}
    if not isinstance(queries_raw, dict):
        queries_raw = {}

    queries = ResearchPlanQueries(
        arxiv=list(queries_raw.get("arxiv") or []),
        youtube=list(queries_raw.get("youtube") or []),
        web=list(queries_raw.get("web") or []),
        pubmed=list(queries_raw.get("pubmed") or []),
    )
    target_counts_raw = data.get("target_counts") or {}
    target_counts = {
        k: int(v) for k, v in target_counts_raw.items() if isinstance(v, (int, float))
    } if isinstance(target_counts_raw, dict) else {}

    edited = _is_edited(path, generated_at)
    state = _derive_state(domain, session_id, edited)

    return ResearchSessionDetail(
        session_id=session_id,
        prompt=prompt,
        domain=domain,
        state=state,
        generated_at=generated_at,
        edited=edited,
        plan=ResearchPlan(queries=queries, target_counts=target_counts),
        sources_count=_sources_count(domain, session_id),
    )
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: All pass.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_research.py && git commit -m "feat(m41): GET /api/research/sessions/{session_id} detail endpoint"
```

---

### Task 4: Create session endpoint (planner via TaskStore)

**Files:**
- Modify: `src/gateway/web/routes/research.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_research.py`

- [ ] **Step 1: Append failing test**

Append to `tests/gateway/test_web_research.py`:

```python
def test_create_session_returns_task_id(client, kb_root, monkeypatch):
    """POST /api/research/sessions starts a planner task and returns 202."""
    # Stub the query planner to avoid real Claude calls.
    from gateway.research import query_planner

    def fake_plan(*args, **kwargs):
        return {
            "arxiv": ["stubbed query 1"],
            "youtube": [],
            "web": [],
            "pubmed": [],
        }

    monkeypatch.setattr(query_planner, "plan_per_adapter_queries", fake_plan)

    resp = client.post(
        "/api/research/sessions",
        json={"prompt": "test prompt", "domain": "d-test"},
    )
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "queued"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py::test_create_session_returns_task_id -v`
Expected: FAIL — POST endpoint doesn't exist.

- [ ] **Step 3: Append schemas**

Append to `src/gateway/web/schemas.py`:

```python
class CreateSessionRequest(BaseModel):
    prompt: str
    domain: str | None = None
    max_results: int = 50
    include_local: list[str] | None = None
    trust_local: bool = False
```

- [ ] **Step 4: Implement create endpoint**

Append to `src/gateway/web/routes/research.py`:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

from gateway.research import query_plan_store as _qps
from gateway.research import query_planner as _qp
from gateway.research.session import make_session_id
from gateway.web.schemas import CreateSessionRequest


@router.post("/sessions", status_code=202)
async def create_session(req: CreateSessionRequest, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("research-plan")

    def run() -> dict:
        # Resolve domain (infer if not provided is out of scope for the
        # planner direct call; the orchestrator handles inference for full
        # research runs. For UI sessions we require explicit domain or
        # default to the prompt-token domain match if user left blank.)
        domain = req.domain
        if not domain:
            return {
                "success": False,
                "errors": ["domain is required when creating a session via the UI; "
                           "use the CLI's `wiki research <prompt>` to leverage domain inference"],
            }

        # Build session_id consistent with the orchestrator
        session_id = make_session_id(req.prompt)

        # Run the per-adapter planner
        plan = _qp.plan_per_adapter_queries(
            prompt=req.prompt,
            domain=domain,
            policy_excerpt=None,
            adapter_names=["arxiv", "youtube", "web", "pubmed"],
            target_counts=None,
            history=None,
        )

        # Persist plan to nlm/query_plans/<session_id>.yaml
        _qps.save(
            session_id=session_id,
            domain=domain,
            prompt=req.prompt,
            queries=plan,
            target_counts=None,
            plan_client_model=None,
        )

        return {
            "success": True,
            "summary": f"created plan for session {session_id}",
            "session_id": session_id,
            "domain": domain,
            "query_count": sum(len(v or []) for v in plan.values()),
        }

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )
```

Note: verify `query_planner.plan_per_adapter_queries` and `query_plan_store.save` signatures by reading their files. The arg names above are best-guesses from the spec; adjust to match the real signatures.

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: All pass.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_research.py && git commit -m "feat(m41): POST /api/research/sessions creates plan via TaskStore"
```

---

### Task 5: Update plan endpoint (PUT)

**Files:**
- Modify: `src/gateway/web/routes/research.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_research.py`

- [ ] **Step 1: Append failing test**

```python
def test_put_plan_updates_yaml(client, kb_root):
    _seed_query_plan(
        "2026-05-04-update",
        domain="d-test",
        prompt="x",
        queries={"arxiv": ["original"], "youtube": [], "web": [], "pubmed": []},
    )
    resp = client.put(
        "/api/research/sessions/2026-05-04-update/plan",
        json={
            "queries": {
                "arxiv": ["updated 1", "updated 2"],
                "youtube": ["new"],
                "web": [],
                "pubmed": [],
            },
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["plan"]["queries"]["arxiv"] == ["updated 1", "updated 2"]
    assert body["plan"]["queries"]["youtube"] == ["new"]


def test_put_plan_unknown_session_returns_404(client, kb_root):
    resp = client.put(
        "/api/research/sessions/nonexistent/plan",
        json={"queries": {"arxiv": [], "youtube": [], "web": [], "pubmed": []}},
    )
    assert resp.status_code == 404
```

- [ ] **Step 2: Run tests to verify they fail**

Expected: 2 failures.

- [ ] **Step 3: Append schemas**

Append to `src/gateway/web/schemas.py`:

```python
class UpdatePlanRequest(BaseModel):
    queries: ResearchPlanQueries
```

- [ ] **Step 4: Implement endpoint**

Append to `src/gateway/web/routes/research.py`:

```python
from gateway.web.schemas import UpdatePlanRequest


@router.put("/sessions/{session_id}/plan", response_model=ResearchSessionDetail)
def put_plan(session_id: str, req: UpdatePlanRequest) -> ResearchSessionDetail:
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    path = plans_dir / f"{session_id}.yaml"
    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"unknown session: {session_id}")

    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as e:
        raise HTTPException(status_code=500, detail=f"invalid plan YAML: {e}")
    if not isinstance(data, dict):
        raise HTTPException(status_code=500, detail="plan YAML is not a mapping")

    data["queries"] = {
        "arxiv": list(req.queries.arxiv),
        "youtube": list(req.queries.youtube),
        "web": list(req.queries.web),
        "pubmed": list(req.queries.pubmed),
    }

    path.write_text(yaml.safe_dump(data, sort_keys=False))

    # Return the refreshed detail
    return get_session(session_id)
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: All pass.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_research.py && git commit -m "feat(m41): PUT /api/research/sessions/{id}/plan persists query edits"
```

---

### Task 6: Execute endpoint

**Files:**
- Modify: `src/gateway/web/routes/research.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_research.py`

- [ ] **Step 1: Append failing test**

```python
def test_execute_returns_task_id(client, kb_root, monkeypatch):
    """POST /api/research/sessions/{id}/execute returns 202 + task_id."""
    _seed_query_plan(
        "2026-05-04-exec",
        domain="d-test",
        prompt="x",
        queries={"arxiv": ["q"], "youtube": [], "web": [], "pubmed": []},
    )

    # Stub the orchestrator's research() to avoid real network calls.
    from gateway.research import orchestrator
    from gateway.core import OperationResult

    def fake_research(prompt, *, domain=None, **kwargs):
        return OperationResult(
            success=True,
            summary=f"stubbed research for {prompt}",
            paths_touched=[],
        )

    monkeypatch.setattr(orchestrator, "research", fake_research)

    resp = client.post(
        "/api/research/sessions/2026-05-04-exec/execute",
        json={"dry_run": False, "draft": False},
    )
    assert resp.status_code == 202
    body = resp.json()
    assert "task_id" in body
```

- [ ] **Step 2: Run test to verify it fails**

Expected: FAIL.

- [ ] **Step 3: Append schemas**

Append to `src/gateway/web/schemas.py`:

```python
class ExecuteSessionRequest(BaseModel):
    dry_run: bool = False
    draft: bool = False
```

- [ ] **Step 4: Implement endpoint**

Append to `src/gateway/web/routes/research.py`:

```python
from gateway.web.schemas import ExecuteSessionRequest


@router.post("/sessions/{session_id}/execute", status_code=202)
async def execute_session(
    session_id: str, req: ExecuteSessionRequest, request: Request
) -> JSONResponse:
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    path = plans_dir / f"{session_id}.yaml"
    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"unknown session: {session_id}")

    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as e:
        raise HTTPException(status_code=500, detail=f"invalid plan YAML: {e}")

    prompt = str(data.get("prompt") or "")
    domain = str(data.get("domain") or "")
    if not prompt or not domain:
        raise HTTPException(status_code=400, detail="plan is missing prompt or domain")

    store = request.app.state.task_store
    record = store.create("research-execute")

    def run() -> dict:
        from gateway.research import orchestrator

        result = orchestrator.research(
            prompt,
            domain=domain,
            execute_session=session_id,
            dry_run=req.dry_run,
            draft=req.draft,
        )
        return {
            "success": result.success,
            "summary": result.summary,
            "paths_touched": [str(p) for p in result.paths_touched],
            "warnings": list(result.warnings),
            "errors": list(result.errors),
            "no_op": result.no_op,
        }

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )
```

Verify the orchestrator's `research()` signature accepts `execute_session=session_id` (this is the existing CLI flag for resuming a persisted plan). Adjust if the kwarg name differs.

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: All pass.

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_research.py && git commit -m "feat(m41): POST /api/research/sessions/{id}/execute kicks off pipeline"
```

---

### Task 7: Progress endpoint

**Files:**
- Modify: `src/gateway/web/routes/research.py`
- Modify: `src/gateway/web/schemas.py`
- Test: `tests/gateway/test_web_research.py`

- [ ] **Step 1: Append failing test**

```python
def test_progress_returns_step_states(client, kb_root):
    """Progress endpoint parses log.md for the session and returns step states."""
    _seed_query_plan("2026-05-04-prog", domain="d-test", prompt="x")

    # Seed log entries simulating a partially-complete run
    log_path = paths.log_path()
    log_path.write_text(
        "# log\n\n"
        "## [2026-05-04T12:00:00Z] research | session_id=2026-05-04-prog | step=start | domain=d-test\n\n"
        "started\n\n"
        "## [2026-05-04T12:00:05Z] research | session_id=2026-05-04-prog | step=search | adapter=arxiv | n=10\n\n"
        "arxiv: 10 candidates\n\n"
        "## [2026-05-04T12:00:10Z] research | session_id=2026-05-04-prog | step=search | adapter=youtube | n=20\n\n"
        "youtube: 20 candidates\n\n"
        "## [2026-05-04T12:00:15Z] research | session_id=2026-05-04-prog | step=merge | n=28\n\n"
        "deduped\n\n"
    )

    resp = client.get("/api/research/sessions/2026-05-04-prog/progress")
    assert resp.status_code == 200
    body = resp.json()
    assert "steps" in body
    steps = {s["name"]: s["status"] for s in body["steps"]}
    assert steps["start"] == "done"
    assert steps["search.arxiv"] == "done"
    assert steps["search.youtube"] == "done"
    assert steps["merge"] == "done"
    # Steps not yet observed remain queued
    assert steps["filter"] == "queued"
    assert steps["materialize"] == "queued"


def test_progress_unknown_session_returns_empty(client, kb_root):
    """Unknown session returns 200 with all steps queued (not 404)."""
    resp = client.get("/api/research/sessions/nonexistent/progress")
    assert resp.status_code == 200
    body = resp.json()
    assert all(s["status"] == "queued" for s in body["steps"])
```

- [ ] **Step 2: Run tests to verify they fail**

Expected: 2 failures.

- [ ] **Step 3: Append schemas**

Append to `src/gateway/web/schemas.py`:

```python
class ProgressStep(BaseModel):
    name: str
    status: str  # queued | running | done | failed
    summary: str = ""
    timestamp: str | None = None


class ProgressResponse(BaseModel):
    steps: list[ProgressStep]
```

- [ ] **Step 4: Add progress endpoint**

Append to `src/gateway/web/routes/research.py`:

```python
import re

from gateway.web.schemas import ProgressResponse, ProgressStep


# Canonical pipeline step list (in order).
_PIPELINE_STEPS = [
    "start",
    "plan",
    "search.arxiv",
    "search.youtube",
    "search.web",
    "search.pubmed",
    "merge",
    "filter",
    "materialize",
    "nlm_persistent",
    "nlm_session",
    "source_add",
    "source_map",
    "analysis",
    "apply_plan",
    "promoted",
]


_LOG_HEADER_RE = re.compile(
    r"^## \[(?P<ts>[^\]]+)\] (?P<op>[a-z0-9-]+)(?: \| (?P<fields>.*))?$"
)


@router.get("/sessions/{session_id}/progress", response_model=ProgressResponse)
def get_progress(session_id: str) -> ProgressResponse:
    log_path = paths.log_path()
    observed: dict[str, ProgressStep] = {}

    if log_path.is_file():
        text = log_path.read_text()
        for entry in _parse_research_entries(text, session_id):
            step_name = entry["fields"].get("step", "")
            if not step_name:
                continue
            # Adapter-specific step name for searches
            adapter = entry["fields"].get("adapter")
            if step_name == "search" and adapter:
                key = f"search.{adapter}"
            else:
                key = step_name
            # `abandon` step → mark current pipeline as failed (will surface
            # by leaving downstream as queued; the session itself is in
            # 'abandoned' state, handled by the list/detail endpoints).
            observed[key] = ProgressStep(
                name=key,
                status="done" if step_name != "abandon" else "failed",
                summary=entry["summary"][:160],
                timestamp=entry["timestamp"],
            )

    # Fill in queued steps for ones not observed
    out: list[ProgressStep] = []
    for name in _PIPELINE_STEPS:
        if name in observed:
            out.append(observed[name])
        else:
            out.append(ProgressStep(name=name, status="queued"))

    return ProgressResponse(steps=out)


def _parse_research_entries(text: str, session_id: str) -> list[dict]:
    """Yield matching entries with op='research' and matching session_id."""
    entries: list[dict] = []
    current: dict | None = None
    summary_lines: list[str] = []
    for line in text.splitlines():
        m = _LOG_HEADER_RE.match(line)
        if m:
            if current is not None:
                current["summary"] = "\n".join(summary_lines).strip()
                if current["op"] == "research" and current["fields"].get("session_id") == session_id:
                    entries.append(current)
            fields_dict: dict[str, str] = {}
            raw_fields = m.group("fields") or ""
            for pair in raw_fields.split(" | "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    fields_dict[k.strip()] = v.strip()
            current = {
                "timestamp": m.group("ts"),
                "op": m.group("op"),
                "fields": fields_dict,
            }
            summary_lines = []
        elif current is not None:
            summary_lines.append(line)
    if current is not None:
        current["summary"] = "\n".join(summary_lines).strip()
        if current["op"] == "research" and current["fields"].get("session_id") == session_id:
            entries.append(current)
    return entries
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_web_research.py -v`
Expected: All pass.

- [ ] **Step 6: Run full gateway suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: 510+ pass, no regressions.

- [ ] **Step 7: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add src/gateway/web/ tests/gateway/test_web_research.py && git commit -m "feat(m41): GET /api/research/sessions/{id}/progress parses log.md per session"
```

---

### Task 8: Frontend types + api client extensions

**Files:**
- Modify: `web/src/types.ts`
- Modify: `web/src/api.ts`

- [ ] **Step 1: Append types**

Append to `web/src/types.ts`:

```typescript
export interface ResearchPlanQueries {
  arxiv: string[];
  youtube: string[];
  web: string[];
  pubmed: string[];
}

export interface ResearchPlan {
  queries: ResearchPlanQueries;
  target_counts: Record<string, number>;
}

export interface ResearchSessionSummary {
  session_id: string;
  prompt: string;
  domain: string;
  state: "plan_only" | "edited" | "running" | "done" | "abandoned";
  generated_at: string;
  edited: boolean;
  query_count: number;
  sources_count: number | null;
}

export interface ResearchSessionDetail {
  session_id: string;
  prompt: string;
  domain: string;
  state: "plan_only" | "edited" | "running" | "done" | "abandoned";
  generated_at: string;
  edited: boolean;
  plan: ResearchPlan;
  sources_count: number | null;
}

export interface ProgressStep {
  name: string;
  status: "queued" | "running" | "done" | "failed";
  summary: string;
  timestamp: string | null;
}

export interface ProgressResponse {
  steps: ProgressStep[];
}
```

- [ ] **Step 2: Append api functions**

Append to the `api` object in `web/src/api.ts`:

```typescript
  // Research (M41)
  listSessions: () => request<ResearchSessionSummary[]>("/api/research/sessions"),
  getSession: (id: string) =>
    request<ResearchSessionDetail>(`/api/research/sessions/${id}`),
  createSession: (body: object) =>
    request<{ task_id: string; status: string }>("/api/research/sessions", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  updatePlan: (id: string, queries: ResearchPlanQueries) =>
    request<ResearchSessionDetail>(`/api/research/sessions/${id}/plan`, {
      method: "PUT",
      body: JSON.stringify({ queries }),
    }),
  executeSession: (id: string, body: object = {}) =>
    request<{ task_id: string; status: string }>(
      `/api/research/sessions/${id}/execute`,
      { method: "POST", body: JSON.stringify(body) },
    ),
  getProgress: (id: string) =>
    request<ProgressResponse>(`/api/research/sessions/${id}/progress`),
```

Make sure to also add the new types to the import block at the top of `api.ts`:

```typescript
import type {
  // existing imports...
  ProgressResponse,
  ResearchPlanQueries,
  ResearchSessionDetail,
  ResearchSessionSummary,
} from "./types";
```

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: TSC compiles cleanly.

- [ ] **Step 4: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/types.ts web/src/api.ts web/dist/ && git commit -m "feat(m41): frontend types + api client for research endpoints"
```

---

### Task 9: Research page shell + sidebar entry

**Files:**
- Create: `web/src/pages/research/Research.tsx`
- Create: `web/src/pages/research/SessionsList.tsx` (placeholder)
- Create: `web/src/pages/research/SessionDetail.tsx` (placeholder)
- Modify: `web/src/App.tsx`

- [ ] **Step 1: Create page shell**

Create `web/src/pages/research/Research.tsx`:

```typescript
import { useParams } from "react-router-dom";
import SessionsList from "./SessionsList";
import SessionDetail from "./SessionDetail";

export default function Research() {
  const { sessionId } = useParams();
  return (
    <div style={{ display: "flex", height: "100%", gap: 0 }}>
      <div style={{ width: "42%", borderRight: "1px solid #eee", overflow: "auto" }}>
        <SessionsList selectedId={sessionId ?? null} />
      </div>
      <div style={{ flex: 1, overflow: "auto", padding: "0 4px" }}>
        {sessionId ? <SessionDetail sessionId={sessionId} /> : (
          <div style={{ padding: 20, color: "#888" }}>
            <p className="subtitle">Select a session on the left, or click "+ New" to start one.</p>
          </div>
        )}
      </div>
    </div>
  );
}
```

Create placeholders so the build passes. We'll fill them in later tasks.

Create `web/src/pages/research/SessionsList.tsx`:

```typescript
interface Props { selectedId: string | null }
export default function SessionsList(_: Props) {
  return <div style={{ padding: 12 }}>Sessions list (coming soon)</div>;
}
```

Create `web/src/pages/research/SessionDetail.tsx`:

```typescript
interface Props { sessionId: string }
export default function SessionDetail({ sessionId }: Props) {
  return <div style={{ padding: 12 }}>Detail for {sessionId}</div>;
}
```

- [ ] **Step 2: Wire into App.tsx + sidebar**

In `web/src/App.tsx`, add the import:

```typescript
import Research from "./pages/research/Research";
```

In the `Sidebar` component, add a new group + entry between Wiki and Domains:

```typescript
      <div className="sidebar-group-label">Research</div>
      <NavLink to="/research" end>Research</NavLink>
```

Add routes:

```typescript
<Route path="/research" element={<Research />} />
<Route path="/research/:sessionId" element={<Research />} />
```

- [ ] **Step 3: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds.

- [ ] **Step 4: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/ web/dist/ && git commit -m "feat(m41): Research page shell + sidebar entry"
```

---

### Task 10: SessionsList component

**Files:**
- Modify: `web/src/pages/research/SessionsList.tsx`

- [ ] **Step 1: Implement SessionsList**

Replace `web/src/pages/research/SessionsList.tsx` with:

```typescript
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../../api";
import type { ResearchSessionSummary } from "../../types";
import NewSessionForm from "./NewSessionForm";

interface Props {
  selectedId: string | null;
}

const STATE_LABELS: Record<string, { color: string; label: string }> = {
  plan_only: { color: "#666", label: "plan" },
  edited: { color: "#1a4c8e", label: "edited" },
  running: { color: "#d97706", label: "running" },
  done: { color: "#0a8a3e", label: "done" },
  abandoned: { color: "#dc2626", label: "abandoned" },
};

export default function SessionsList({ selectedId }: Props) {
  const [sessions, setSessions] = useState<ResearchSessionSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showNewForm, setShowNewForm] = useState(false);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setSessions(await api.listSessions());
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
      <div
        style={{
          padding: "12px 12px 8px",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderBottom: "1px solid #eee",
        }}
      >
        <div style={{ fontSize: 13, fontWeight: 600 }}>Sessions</div>
        <button
          className="btn-secondary"
          onClick={() => setShowNewForm((v) => !v)}
          style={{ fontSize: 11, padding: "3px 8px" }}
        >
          {showNewForm ? "Cancel" : "+ New"}
        </button>
      </div>

      {showNewForm && (
        <NewSessionForm
          onCreated={() => {
            setShowNewForm(false);
            refresh();
          }}
          onCancel={() => setShowNewForm(false)}
        />
      )}

      {error && (
        <div style={{ padding: 12, color: "#dc2626", fontSize: 12 }}>
          {error}
        </div>
      )}

      {loading && !sessions.length && (
        <div style={{ padding: 12, color: "#888", fontSize: 12 }}>Loading…</div>
      )}

      {!loading && sessions.length === 0 && (
        <div style={{ padding: 12, color: "#888", fontSize: 12 }}>
          No sessions yet. Click "+ New" to start one.
        </div>
      )}

      <div>
        {sessions.map((s) => {
          const isSelected = s.session_id === selectedId;
          const state = STATE_LABELS[s.state] ?? { color: "#888", label: s.state };
          return (
            <Link
              key={s.session_id}
              to={`/research/${s.session_id}`}
              style={{
                display: "block",
                padding: "8px 12px",
                borderBottom: "1px solid #f0f0f0",
                background: isSelected ? "#f0f4fa" : "white",
                borderLeft: isSelected ? "3px solid #1a4c8e" : "3px solid transparent",
                textDecoration: "none",
                color: "inherit",
              }}
            >
              <div style={{ fontSize: 11, fontWeight: 600, marginBottom: 2 }}>
                {s.session_id}
              </div>
              <div style={{ fontSize: 10, color: "#666", marginBottom: 2 }}>
                {s.prompt.slice(0, 80)}
                {s.prompt.length > 80 ? "…" : ""}
              </div>
              <div style={{ fontSize: 10, display: "flex", gap: 8 }}>
                <span style={{ color: state.color, fontWeight: 600 }}>● {state.label}</span>
                <span style={{ color: "#888" }}>{s.domain}</span>
                <span style={{ color: "#888" }}>
                  {s.sources_count != null
                    ? `${s.sources_count} sources`
                    : `${s.query_count} queries`}
                </span>
              </div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Note: NewSessionForm doesn't exist yet — the build will fail. Skip the build for now and proceed to Task 11.

If you want to verify SessionsList in isolation, temporarily comment out the `NewSessionForm` import + usage. Restore after Task 11.

- [ ] **Step 3: Commit (deferred until Task 11 lands NewSessionForm)**

This task's commit happens at the end of Task 11, since the two files build together.

---

### Task 11: NewSessionForm component

**Files:**
- Create: `web/src/pages/research/NewSessionForm.tsx`

- [ ] **Step 1: Implement form**

Create `web/src/pages/research/NewSessionForm.tsx`:

```typescript
import { useEffect, useRef, useState } from "react";
import { api } from "../../api";

interface Props {
  onCreated: () => void;
  onCancel: () => void;
}

export default function NewSessionForm({ onCreated, onCancel }: Props) {
  const [prompt, setPrompt] = useState("");
  const [domain, setDomain] = useState("");
  const [maxResults, setMaxResults] = useState(50);
  const [advanced, setAdvanced] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [taskId, setTaskId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const intervalRef = useRef<number | null>(null);

  useEffect(() => {
    return () => {
      if (intervalRef.current) window.clearInterval(intervalRef.current);
    };
  }, []);

  async function onSubmit() {
    if (!prompt.trim() || !domain.trim()) {
      setError("prompt and domain are both required");
      return;
    }
    setSubmitting(true);
    setError(null);
    try {
      const ack = await api.createSession({
        prompt,
        domain,
        max_results: maxResults,
      });
      setTaskId(ack.task_id);
      intervalRef.current = window.setInterval(async () => {
        try {
          const t = await api.getTask(ack.task_id);
          if (t.status === "done") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setSubmitting(false);
            onCreated();
          } else if (t.status === "failed") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setError(t.error ?? "task failed");
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
      }, 2000);
    } catch (e: any) {
      setError(e.message);
      setSubmitting(false);
    }
  }

  return (
    <div style={{ padding: 12, background: "#fafafa", borderBottom: "1px solid #eee" }}>
      <label style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>Prompt</label>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="On-device RAG with proprietary data..."
        style={{
          width: "100%",
          fontSize: 12,
          padding: 6,
          border: "1px solid #ccc",
          borderRadius: 3,
          minHeight: 60,
          marginTop: 2,
          fontFamily: "inherit",
          resize: "vertical",
        }}
        disabled={submitting}
      />

      <label style={{ fontSize: 10, textTransform: "uppercase", color: "#666", marginTop: 8 }}>Domain</label>
      <input
        type="text"
        value={domain}
        onChange={(e) => setDomain(e.target.value)}
        placeholder="edge-ai-agentic"
        style={{
          width: "100%",
          fontSize: 12,
          padding: "5px 8px",
          border: "1px solid #ccc",
          borderRadius: 3,
          marginTop: 2,
        }}
        disabled={submitting}
      />

      <button
        onClick={() => setAdvanced((v) => !v)}
        style={{
          fontSize: 11,
          color: "#1a4c8e",
          background: "none",
          border: "none",
          cursor: "pointer",
          padding: "8px 0 0",
        }}
      >
        {advanced ? "▾ Hide advanced" : "▸ Advanced"}
      </button>

      {advanced && (
        <div>
          <label style={{ fontSize: 10, textTransform: "uppercase", color: "#666", marginTop: 4 }}>
            Max results per adapter
          </label>
          <input
            type="number"
            value={maxResults}
            onChange={(e) => setMaxResults(parseInt(e.target.value) || 50)}
            style={{
              width: 100,
              fontSize: 12,
              padding: "4px 6px",
              border: "1px solid #ccc",
              borderRadius: 3,
              marginTop: 2,
            }}
          />
        </div>
      )}

      {error && (
        <div style={{ marginTop: 8, color: "#dc2626", fontSize: 11 }}>
          {error}
        </div>
      )}

      {taskId && submitting && (
        <div style={{ marginTop: 8, fontSize: 11, color: "#d97706" }}>
          ⟳ Generating per-adapter queries... (~12s)
        </div>
      )}

      <div style={{ marginTop: 10, display: "flex", gap: 8 }}>
        <button
          className="btn-primary"
          onClick={onSubmit}
          disabled={submitting}
          style={{ fontSize: 11, padding: "5px 14px" }}
        >
          {submitting ? "Creating..." : "Create plan"}
        </button>
        <button
          className="btn-secondary"
          onClick={onCancel}
          disabled={submitting}
          style={{ fontSize: 11, padding: "5px 14px" }}
        >
          Cancel
        </button>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds (Tasks 10 + 11 commit together).

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/research/SessionsList.tsx web/src/pages/research/NewSessionForm.tsx web/dist/ && git commit -m "feat(m41): SessionsList + NewSessionForm components"
```

---

### Task 12: PlanEditor component

**Files:**
- Create: `web/src/pages/research/PlanEditor.tsx`

- [ ] **Step 1: Implement editor**

Create `web/src/pages/research/PlanEditor.tsx`:

```typescript
import { useState } from "react";
import { api } from "../../api";
import type { ResearchPlanQueries, ResearchSessionDetail } from "../../types";

interface Props {
  session: ResearchSessionDetail;
  onSaved: (updated: ResearchSessionDetail) => void;
}

const ADAPTERS: Array<keyof ResearchPlanQueries> = ["arxiv", "youtube", "web", "pubmed"];

export default function PlanEditor({ session, onSaved }: Props) {
  const [queries, setQueries] = useState<ResearchPlanQueries>(session.plan.queries);
  const [original] = useState<ResearchPlanQueries>(session.plan.queries);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function isEdited(adapter: keyof ResearchPlanQueries, idx: number): boolean {
    const orig = original[adapter];
    return orig[idx] !== queries[adapter][idx];
  }

  function isAdded(adapter: keyof ResearchPlanQueries, idx: number): boolean {
    return idx >= original[adapter].length;
  }

  function updateQuery(adapter: keyof ResearchPlanQueries, idx: number, value: string) {
    setQueries((prev) => ({
      ...prev,
      [adapter]: prev[adapter].map((q, i) => (i === idx ? value : q)),
    }));
  }

  function addQuery(adapter: keyof ResearchPlanQueries) {
    setQueries((prev) => ({
      ...prev,
      [adapter]: [...prev[adapter], ""],
    }));
  }

  function removeQuery(adapter: keyof ResearchPlanQueries, idx: number) {
    setQueries((prev) => ({
      ...prev,
      [adapter]: prev[adapter].filter((_, i) => i !== idx),
    }));
  }

  async function save() {
    setSaving(true);
    setError(null);
    try {
      // Strip empty rows
      const cleaned: ResearchPlanQueries = {
        arxiv: queries.arxiv.filter((q) => q.trim()),
        youtube: queries.youtube.filter((q) => q.trim()),
        web: queries.web.filter((q) => q.trim()),
        pubmed: queries.pubmed.filter((q) => q.trim()),
      };
      const updated = await api.updatePlan(session.session_id, cleaned);
      onSaved(updated);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSaving(false);
    }
  }

  return (
    <div>
      {ADAPTERS.map((adapter) => (
        <div key={adapter} style={{ marginBottom: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 4 }}>
            <div style={{ fontSize: 11, fontWeight: 600, textTransform: "uppercase" }}>
              {adapter} ({queries[adapter].length})
            </div>
            <button
              onClick={() => addQuery(adapter)}
              style={{ fontSize: 11, color: "#1a4c8e", background: "none", border: "none", cursor: "pointer" }}
            >
              + add
            </button>
          </div>
          {queries[adapter].length === 0 && (
            <div style={{ fontSize: 11, color: "#999", fontStyle: "italic" }}>
              (no queries)
            </div>
          )}
          {queries[adapter].map((q, idx) => {
            const edited = isEdited(adapter, idx) || isAdded(adapter, idx);
            return (
              <div
                key={idx}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 6,
                  marginBottom: 3,
                  background: edited ? "#fffbeb" : "#f7f7f9",
                  border: edited ? "1px dashed #d97706" : "1px solid transparent",
                  borderRadius: 3,
                  padding: 2,
                }}
              >
                <input
                  type="text"
                  value={q}
                  onChange={(e) => updateQuery(adapter, idx, e.target.value)}
                  style={{
                    flex: 1,
                    border: "none",
                    background: "transparent",
                    padding: "4px 8px",
                    fontSize: 12,
                    fontFamily: "inherit",
                  }}
                />
                <button
                  onClick={() => removeQuery(adapter, idx)}
                  style={{ background: "none", border: "none", color: "#888", cursor: "pointer", fontSize: 14, padding: "0 6px" }}
                  title="Remove"
                >
                  ×
                </button>
              </div>
            );
          })}
        </div>
      ))}

      {error && (
        <div style={{ color: "#dc2626", fontSize: 12, marginTop: 8 }}>{error}</div>
      )}

      <div style={{ marginTop: 12, display: "flex", gap: 8 }}>
        <button className="btn-primary" onClick={save} disabled={saving}>
          {saving ? "Saving..." : "Save plan"}
        </button>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds.

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/research/PlanEditor.tsx web/dist/ && git commit -m "feat(m41): PlanEditor structured per-adapter editor"
```

---

### Task 13: ProgressView component

**Files:**
- Create: `web/src/pages/research/ProgressView.tsx`

- [ ] **Step 1: Implement progress view**

Create `web/src/pages/research/ProgressView.tsx`:

```typescript
import { useEffect, useRef, useState } from "react";
import { api } from "../../api";
import type { ProgressStep } from "../../types";

interface Props {
  sessionId: string;
  onTerminal?: () => void;  // called when status is done/failed
}

const STATUS_GLYPH: Record<string, { glyph: string; color: string }> = {
  queued: { glyph: "○", color: "#999" },
  running: { glyph: "⟳", color: "#d97706" },
  done: { glyph: "✓", color: "#0a8a3e" },
  failed: { glyph: "✗", color: "#dc2626" },
};

export default function ProgressView({ sessionId, onTerminal }: Props) {
  const [steps, setSteps] = useState<ProgressStep[]>([]);
  const [error, setError] = useState<string | null>(null);
  const intervalRef = useRef<number | null>(null);
  const onTerminalRef = useRef(onTerminal);

  useEffect(() => {
    onTerminalRef.current = onTerminal;
  }, [onTerminal]);

  useEffect(() => {
    let active = true;

    async function poll() {
      try {
        const resp = await api.getProgress(sessionId);
        if (!active) return;
        setSteps(resp.steps);
        const hasFailed = resp.steps.some((s) => s.status === "failed");
        const isDone = resp.steps.some((s) => s.name === "promoted" && s.status === "done");
        if (hasFailed || isDone) {
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          onTerminalRef.current?.();
        }
      } catch (e: any) {
        setError(e.message);
      }
    }

    poll();
    intervalRef.current = window.setInterval(poll, 3000);

    return () => {
      active = false;
      if (intervalRef.current) {
        window.clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
    };
  }, [sessionId]);

  if (error) {
    return (
      <div className="result-panel error">
        <div className="result-status">Progress poll failed</div>
        <pre>{error}</pre>
      </div>
    );
  }

  return (
    <div
      style={{
        background: "#f7f7f9",
        borderRadius: 4,
        padding: 12,
        fontFamily: "ui-monospace, monospace",
        fontSize: 11,
        lineHeight: 1.7,
      }}
    >
      {steps.map((s) => {
        const g = STATUS_GLYPH[s.status] ?? { glyph: "?", color: "#888" };
        return (
          <div key={s.name} style={{ color: g.color }}>
            <span style={{ display: "inline-block", width: 16 }}>{g.glyph}</span>
            <span style={{ display: "inline-block", width: 200 }}>{s.name}</span>
            <span style={{ color: "#666" }}>{s.summary}</span>
          </div>
        );
      })}
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds.

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/research/ProgressView.tsx web/dist/ && git commit -m "feat(m41): ProgressView with 3s polling of /progress"
```

---

### Task 14: SessionDetail with phase routing

**Files:**
- Modify: `web/src/pages/research/SessionDetail.tsx`

- [ ] **Step 1: Implement SessionDetail**

Replace `web/src/pages/research/SessionDetail.tsx` with:

```typescript
import { useEffect, useState } from "react";
import { api } from "../../api";
import type { ResearchSessionDetail } from "../../types";
import PlanEditor from "./PlanEditor";
import ProgressView from "./ProgressView";

interface Props {
  sessionId: string;
}

export default function SessionDetail({ sessionId }: Props) {
  const [session, setSession] = useState<ResearchSessionDetail | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [executing, setExecuting] = useState(false);

  async function refresh() {
    setError(null);
    try {
      setSession(await api.getSession(sessionId));
    } catch (e: any) {
      setError(e.message);
    }
  }

  useEffect(() => {
    refresh();
  }, [sessionId]);

  async function execute() {
    if (!session) return;
    setExecuting(true);
    try {
      await api.executeSession(session.session_id);
      // Optimistically transition to running by re-fetching
      refresh();
    } catch (e: any) {
      setError(e.message);
      setExecuting(false);
    }
  }

  if (error) {
    return (
      <div style={{ padding: 16 }}>
        <div className="result-panel error">
          <div className="result-status">Failed to load session</div>
          <pre>{error}</pre>
        </div>
      </div>
    );
  }

  if (!session) {
    return <div style={{ padding: 16, color: "#888" }}>Loading…</div>;
  }

  const showPlanEditor = session.state === "plan_only" || session.state === "edited";
  const showProgress = session.state === "running" || executing;
  const showDone = session.state === "done";
  const showAbandoned = session.state === "abandoned";

  return (
    <div style={{ padding: 16 }}>
      <div style={{ marginBottom: 12 }}>
        <div style={{ fontSize: 14, fontWeight: 600, marginBottom: 2 }}>
          {session.session_id}
        </div>
        <div style={{ fontSize: 11, color: "#666", marginBottom: 4 }}>
          {session.prompt}
        </div>
        <div style={{ fontSize: 10, color: "#888" }}>
          {session.domain} · {session.state}
          {session.edited && " · edited"}
        </div>
      </div>

      {showPlanEditor && (
        <>
          <PlanEditor session={session} onSaved={(s) => setSession(s)} />
          <div style={{ marginTop: 12 }}>
            <button className="btn-primary" onClick={execute} disabled={executing}>
              Execute →
            </button>
          </div>
        </>
      )}

      {showProgress && (
        <ProgressView sessionId={session.session_id} onTerminal={refresh} />
      )}

      {showDone && (
        <div className="result-panel success" style={{ marginTop: 12 }}>
          <div className="result-status">Promoted</div>
          <pre>
            {`${session.sources_count ?? "?"} source(s) added to ${session.domain} corpus`}
          </pre>
          <pre style={{ marginTop: 8, fontSize: 11 }}>
            Synthesis pages live under wiki/synthesis/{session.session_id}-*.md{"\n"}
            Open in Obsidian: obsidian:// links not yet wired (M41 follow-up).
          </pre>
        </div>
      )}

      {showAbandoned && (
        <div className="result-panel error" style={{ marginTop: 12 }}>
          <div className="result-status">Abandoned</div>
          <pre>
            Session was abandoned during execute. Check the activity feed on
            Dashboard or the per-step progress in log.md for the failure cause.
          </pre>
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Build**

Run: `cd /Users/andrewgrant/code/knowledge/web && npm run build`
Expected: build succeeds.

- [ ] **Step 3: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add web/src/pages/research/SessionDetail.tsx web/dist/ && git commit -m "feat(m41): SessionDetail phase router (plan/running/done/abandoned)"
```

---

### Task 15: Hand-test + documentation

**Files:**
- Modify: `BUILD.md`
- Modify: `CLAUDE.md`
- Modify: `README.md`
- Modify: `TUTORIAL.md`

- [ ] **Step 1: Hand-test the full flow**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/wiki serve --port 7475`

Open http://127.0.0.1:7475/research in a browser. Verify:
- Sessions list shows existing plans (3 from `nlm/query_plans/`)
- Click an existing session → detail pane renders the plan editor
- Edit a query, save → mtime bump triggers `edited: true` on next reload
- "+ New" form opens, submit a small prompt with an existing domain → planner runs ~12s → new session appears
- Click "Execute →" on a session with a real domain → progress view renders
- Watch progress (search per adapter → merge → filter → materialize → ...) update over the run
- On completion, detail pane shows `done` state with sources count

Then: `pkill -f "wiki serve"`

- [ ] **Step 2: Append BUILD.md M41 entry**

In `BUILD.md`, after the M40 section (before "## 11. Downstream wiki-authoring work"), add:

```markdown
### M41 — Research orchestration UI

Adds a Research sidebar entry to `wiki serve` that exposes the existing `wiki research` orchestrator (M37/M37.1) over HTTP. The page uses a sessions-list + detail two-pane layout. Each session walks through three phases: prompt+domain → query plan (structured per-adapter editor) → execute. Long-running execution shows per-step progress sourced from filtered `log.md` entries.

**What's new.**

- `gateway.web.routes.research` — six endpoints: list sessions, get session detail, create session (planner via TaskStore), update plan (PUT YAML), execute (orchestrator via TaskStore), get progress (parses log.md).
- `gateway.research.orchestrator` — six new `log.append("research", step=<name>)` calls (materialize, nlm_persistent, nlm_session, source_map, analysis, apply_plan) so the progress endpoint can render every named pipeline stage.
- `web/src/pages/research/` — 7 components: Research (page shell), SessionsList, NewSessionForm, SessionDetail (phase router), PlanEditor (per-adapter structured editor with × delete + add), ProgressView (3s polling, 16 steps).
- Sidebar gains a Research group with one entry. State derivation reads `nlm/query_plans/` + `nlm_registry` + TaskStore — no new persistence layer.

**Lifecycle states (derived):** `plan_only` (YAML exists, not edited, not executed) · `edited` (YAML mtime > generated_at + 2s) · `running` (active task) · `done` (registry session.status == promoted) · `abandoned` (registry session.status == abandoned).

**Tests.** ~15 new tests in `test_web_research.py` covering all six endpoints, plus orchestrator regressions for the new log.append calls. Full gateway suite: 504 → 519+ passing.

**Out of scope (deferred to M42).**

- NLM artifact triggers (briefing, audio, slides, revise) per-domain page.
- Review consoles (drafts list, contradictions, source orphans, filter-band sources).
- `obsidian://` deep-link for synthesis pages on done sessions — basic display only in M41.
- Session deletion / cleanup ops.
- `--queries` external YAML import — CLI-only.
```

- [ ] **Step 3: Update CLAUDE.md operation table**

In `CLAUDE.md`, find the Operation guide table and add a row near the research/multi-adapter row:

```
| Open the local web UI's research page | `wiki serve` then visit http://127.0.0.1:7474/research |
```

- [ ] **Step 4: Update README.md**

No new CLI commands — `wiki serve` is already in the table from M40. Optionally add a note in the Status section that the web UI now covers research orchestration.

- [ ] **Step 5: Update TUTORIAL.md**

In TUTORIAL.md § 11 "Cheat sheet", under the existing `wiki serve` line, add a comment:

```
wiki serve [--port 7474]                           # local browser UI; /research for orchestration
```

- [ ] **Step 6: Commit**

```bash
cd /Users/andrewgrant/code/knowledge && git add BUILD.md CLAUDE.md README.md TUTORIAL.md && git commit -m "docs: M41 delivery record + research UI in operation tables"
```

---

## Self-review

**Spec coverage:**

| Spec § | Tasks |
|---|---|
| § 1 Architecture | Tasks 2 (router) + 9 (page shell) |
| § 2 Lifecycle states | Task 2 (`_derive_state` helper) |
| § 3 Endpoints (6) | Tasks 2-7 (one per endpoint) |
| § 4 Frontend layout | Tasks 9-14 |
| § 5 Per-step progress data flow | Tasks 1 (orchestrator log entries) + 7 (parser) + 13 (UI) |
| § 6 New-session form | Task 11 |
| § 7 Out of scope | Documented in Task 15 BUILD.md entry |
| § 9 Acceptance criteria 1-11 | All mapped to tasks |

**Placeholder scan:** No TBDs. The Task 1 test (Step 2) does say "adapt to existing fixture pattern" — that's a deliberate hedge because the actual fixture style depends on what already exists in `test_research_orchestrator.py`. Acceptable for a plan; the implementer reads the existing test file and chooses the right pattern.

**Type consistency:** `ResearchPlanQueries` shape (4 adapter arrays) is used in types.ts (Task 8), schemas.py (Task 3), and PlanEditor (Task 12). `state` enum (`plan_only | edited | running | done | abandoned`) is consistent across types.ts and SessionDetail's phase routing. `ProgressStep.status` (queued | running | done | failed) consistent across schemas, types, and ProgressView.

**Known signature-verification points** (implementer should read source first):
- `nlm_registry.get_session(domain, session_id)` — return shape
- `query_planner.plan_per_adapter_queries(...)` — kwarg names
- `query_plan_store.save(...)` — kwarg names
- `orchestrator.research(...)` — `execute_session` kwarg name (matches CLI flag)

These are flagged inline; the plan tells the implementer to verify, not guess.
