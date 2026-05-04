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
        req.source_id,
        decision=req.decision,
        rationale=req.rationale,
    )
    return _to_response(result)
