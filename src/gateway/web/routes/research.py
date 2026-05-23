"""Research orchestration endpoints (M41)."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

import yaml
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from gateway import nlm_registry, paths
from gateway.filter.policy import load_policy, PolicyError
from gateway.plan import ClaudeCLIPlanClient
from gateway.research import query_planner as _qp
from gateway.research.query_plan_store import QueryPlan, save as save_plan
from gateway.research.session import make_session_id
from gateway.web.schemas import (
    CreateSessionRequest,
    ExecuteSessionRequest,
    ProgressResponse,
    ProgressStep,
    ResearchPlan,
    ResearchPlanQueries,
    ResearchSessionDetail,
    ResearchSessionSummary,
    UpdatePlanRequest,
)


router = APIRouter(prefix="/api/research", tags=["research"])


_SLACK_SECONDS = 2.0


@router.get("/sessions", response_model=list[ResearchSessionSummary])
def list_sessions() -> list[ResearchSessionSummary]:
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
        if isinstance(queries, dict):
            query_count = sum(len(v or []) for v in queries.values() if isinstance(v, list))
        else:
            query_count = 0

        edited = _is_edited(path, generated_at)
        state = _derive_state(domain, session_id, edited)

        out.append(
            ResearchSessionSummary(
                session_id=session_id,
                prompt=prompt,
                domain=domain,
                state=state,
                generated_at=generated_at,
                edited=edited,
                query_count=query_count,
                sources_count=_sources_count(domain, session_id),
            )
        )

    out.sort(key=lambda s: s.generated_at, reverse=True)
    return out


def _is_edited(path: Path, generated_at: str) -> bool:
    """YAML mtime > generated_at + 2s slack."""
    if not generated_at:
        return False
    try:
        gen_dt = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    try:
        mtime_ts = path.stat().st_mtime
    except OSError:
        return False
    return mtime_ts > gen_dt.timestamp() + _SLACK_SECONDS


def _derive_state(domain: str, session_id: str, edited: bool) -> str:
    """Compute lifecycle state from registry + edit flag.

    Returns one of: plan_only | edited | done | abandoned.
    'running' detection is left to the frontend (via task_id polling on
    create/execute responses) — this helper does not look into TaskStore.
    """
    if not domain or not session_id:
        return "edited" if edited else "plan_only"
    sess = nlm_registry.get_session(domain, session_id)
    if sess is None:
        return "edited" if edited else "plan_only"
    status = sess.get("status") if isinstance(sess, dict) else None
    if status == nlm_registry.PROMOTED:
        return "done"
    if status == nlm_registry.ABANDONED:
        return "abandoned"
    return "edited" if edited else "plan_only"


def _sources_count(domain: str, session_id: str) -> int | None:
    if not domain or not session_id:
        return None
    sess = nlm_registry.get_session(domain, session_id)
    if not isinstance(sess, dict):
        return None
    val = sess.get("sources_count")
    if val is None:
        return None
    try:
        return int(val)
    except (TypeError, ValueError):
        return None


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
    if isinstance(target_counts_raw, dict):
        target_counts = {
            k: int(v) for k, v in target_counts_raw.items() if isinstance(v, (int, float))
        }
    else:
        target_counts = {}

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


@router.post("/sessions", status_code=202)
async def create_session(req: CreateSessionRequest, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("research-plan")
    prompt = req.prompt
    domain = req.domain

    def run() -> dict:
        if not prompt or not prompt.strip():
            return {
                "success": False,
                "errors": ["prompt is required"],
                "summary": "create_session failed: empty prompt",
            }
        if not domain or not domain.strip():
            return {
                "success": False,
                "errors": ["domain is required (UI does not infer)"],
                "summary": "create_session failed: empty domain",
            }
        try:
            policy = load_policy(domain)
        except PolicyError as e:
            return {
                "success": False,
                "errors": [f"no policy for domain {domain!r}: {e}"],
                "summary": "create_session failed: policy missing",
            }
        # M46-followup Fix E: this client is used for per-adapter query
        # planning only — Sonnet 4.6 is the right tier.
        from gateway.llm import model_for
        plan_client = ClaudeCLIPlanClient(model=model_for("plan_query_planner"))
        try:
            result = _qp.plan_per_adapter_queries(
                prompt,
                domain=domain,
                policy=policy,
                adapter_names=["arxiv", "youtube", "web", "pubmed"],
                plan_client=plan_client,
            )
        except Exception as e:  # noqa: BLE001
            return {
                "success": False,
                "errors": [f"planner failed: {e}"],
                "summary": "create_session failed",
            }

        session_id = make_session_id(prompt)
        plan = QueryPlan(
            session_id=session_id,
            domain=domain,
            prompt=prompt,
            generated_at=datetime.now(timezone.utc),
            queries=result.queries,
            target_counts=result.target_counts,
            plan_client_model=result.plan_client_model,
        )
        save_plan(plan)

        query_count = sum(len(v or []) for v in result.queries.values())
        return {
            "success": True,
            "summary": f"created plan for session {session_id} ({query_count} queries)",
            "session_id": session_id,
            "domain": domain,
            "query_count": query_count,
        }

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


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


@router.post("/sessions/{session_id}/execute", status_code=202)
async def execute_session(
    session_id: str, req: ExecuteSessionRequest, request: Request
) -> JSONResponse:
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    path = plans_dir / f"{session_id}.yaml"
    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"unknown session: {session_id}")

    store = request.app.state.task_store
    record = store.create("research-execute")

    captured_session_id = session_id
    captured_dry_run = req.dry_run
    captured_draft = req.draft

    def run() -> dict:
        from gateway.research import orchestrator

        result = orchestrator.research(
            None,  # prompt loaded from persisted plan via execute_session
            execute_session=captured_session_id,
            dry_run=captured_dry_run,
            draft=captured_draft,
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


# Canonical pipeline step list (in execution order).
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
    abandoned = False

    if log_path.is_file():
        text = log_path.read_text()
        for entry in _parse_research_entries(text, session_id):
            step_name = entry["fields"].get("step", "")
            if not step_name:
                continue
            if step_name == "abandon":
                abandoned = True
                continue
            adapter = entry["fields"].get("adapter")
            if step_name == "search" and adapter:
                key = f"search.{adapter}"
            else:
                key = step_name
            observed[key] = ProgressStep(
                name=key,
                status="done",
                summary=entry["summary"][:160],
                timestamp=entry["timestamp"],
            )

    out: list[ProgressStep] = []
    seen_first_unobserved = False
    for name in _PIPELINE_STEPS:
        if name in observed:
            out.append(observed[name])
        elif abandoned and not seen_first_unobserved:
            # First unobserved step after an abandon is the failure point
            out.append(ProgressStep(name=name, status="failed"))
            seen_first_unobserved = True
        else:
            out.append(ProgressStep(name=name, status="queued"))

    return ProgressResponse(steps=out)


def _parse_research_entries(text: str, session_id: str) -> list[dict]:
    """Return matching entries with op='research' and matching session_id."""
    entries: list[dict] = []
    current: dict | None = None
    summary_lines: list[str] = []
    for line in text.splitlines():
        m = _LOG_HEADER_RE.match(line)
        if m:
            if current is not None:
                current["summary"] = "\n".join(summary_lines).strip()
                if (
                    current["op"] == "research"
                    and current["fields"].get("session_id") == session_id
                ):
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
        if (
            current["op"] == "research"
            and current["fields"].get("session_id") == session_id
        ):
            entries.append(current)
    return entries
