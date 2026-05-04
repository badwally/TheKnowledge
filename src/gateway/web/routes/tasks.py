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
