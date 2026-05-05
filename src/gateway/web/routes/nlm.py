"""NLM artifact endpoints (M43)."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops import nlm as _nlm
from gateway.ops.nlm import nlm_add
from gateway.web.routes.domains import _to_response
from gateway.web.routes.ops import _serialize_op_result
from gateway.web.schemas import (
    ArtifactSummary,
    NlmAddRequest,
    NlmReviseRequest,
    NlmSyncRequest,
    NlmTopicRequest,
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
