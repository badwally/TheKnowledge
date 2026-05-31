"""Operation endpoints. Synchronous (short ops) or async (long ops via TaskStore)."""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from gateway.ops.bootstrap_domain import bootstrap_domain
from gateway.ops.discover_domains import discover_domains
from gateway.ops.filter_correct import filter_correct
from gateway.ops.finalize import finalize
from gateway.ops.ingest import ingest
from gateway.ops.query import query
from gateway.web.ingest_input import validate_remote_url
from gateway.web.routes.domains import _serialize_authorship_report, _to_response
from gateway.web.schemas import (
    BootstrapDomainRequest,
    DiscoverDomainsRequest,
    FilterCorrectRequest,
    FinalizeRequest,
    IngestRequest,
    OperationResultResponse,
    QueryRequest,
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
        req.source_id,
        decision=req.decision,
        rationale=req.rationale,
    )
    return _to_response(result)


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


@router.post("/ingest", status_code=202)
def post_ingest(req: IngestRequest, request: Request) -> JSONResponse:
    # Reject local-path inputs synchronously (finding #3); only http(s) URLs
    # are ingestable over the API. Validates before the 202 so the caller
    # sees a 400 rather than a background-task failure.
    url = validate_remote_url(req.input)
    store = request.app.state.task_store
    record = store.create("ingest")

    def run() -> dict:
        result = ingest(
            url,
            domain=req.domain,
            with_plan=req.with_plan,
            draft=req.draft,
        )
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/query", status_code=202)
def post_query(req: QueryRequest, request: Request) -> JSONResponse:
    store = request.app.state.task_store
    record = store.create("query")

    def run() -> dict:
        result = query(req.question, domain=req.domain, draft=req.draft)
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/bootstrap-domain", status_code=202)
def post_bootstrap(
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

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )


@router.post("/discover-domains", status_code=202)
def post_discover(
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

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )
