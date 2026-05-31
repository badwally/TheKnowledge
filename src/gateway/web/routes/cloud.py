"""K3 (M48): cloud-shim ingest endpoint with bearer-token auth.

`POST /api/ingest` is the remote-capture endpoint. Mirrors the
existing `/api/ops/ingest` async pattern (TaskStore daemon thread,
202 + task_id, poll via `/api/tasks/{task_id}`). Per D4 the call is
sync via TaskStore so the iOS Shortcut sees real success/failure.

Accepted body shapes:

- JSON: `{"url": "<https://...>", "domain"?, "draft"?, "with_plan"?}`
- Multipart form: `file` (binary upload) + optional `domain`, `draft`,
  `with_plan` form fields. v1 multipart writes to a temp path then
  hands that path to `ingest()`. iOS Shortcut v1 sends JSON (URL +
  text from Share Sheet); multipart-file path is for future browser-ext.

Bearer-token authentication is enforced via the
`gateway.web.auth.verify_bearer` FastAPI dependency. Audit: the
token name (not the secret) ends up in log.md via downstream
`ingest()` invocation context.
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from gateway import log as log_mod
from gateway.ops.ingest import ingest


router = APIRouter(prefix="/api", tags=["cloud"])


class CloudIngestRequest(BaseModel):
    url: str
    domain: str | None = None
    with_plan: bool = False
    draft: bool = False


def _resolve_input(raw: str):
    if raw.startswith(("http://", "https://")):
        return raw
    return Path(raw).expanduser().resolve()


def _serialize_op_result(result) -> dict[str, Any]:
    return {
        "success": result.success,
        "no_op": result.no_op,
        "summary": result.summary,
        "paths_touched": [str(p) for p in result.paths_touched],
        "errors": list(result.errors),
        "warnings": list(result.warnings),
    }


@router.post("/ingest", status_code=202)
async def post_ingest(
    request: Request,
    # multipart form fields (all optional; presence indicates form-data mode)
    file: UploadFile | None = File(default=None),
    domain: str | None = Form(default=None),
    draft: bool = Form(default=False),
    with_plan: bool = Form(default=False),
) -> JSONResponse:
    """Authenticated single-source ingest. Returns 202 + task_id.

    The bearer token is verified by the app-level ``require_bearer``
    middleware (see ``gateway.web.app``); the resolved token name is read
    from ``request.state`` for audit logging.
    """
    store = request.app.state.task_store
    token_name = getattr(request.state, "token_name", "unknown")

    # Branch on body type. If a file came through multipart, we ingest from
    # the temp file; otherwise we expect a JSON body with `url`.
    if file is not None:
        # Save the upload to a tmp file (delete=False so the worker can
        # read it after this handler returns).
        contents = await file.read()
        suffix = Path(file.filename or "upload").suffix or ""
        tmp = tempfile.NamedTemporaryFile(
            delete=False, suffix=suffix, dir=tempfile.gettempdir()
        )
        try:
            tmp.write(contents)
        finally:
            tmp.close()
        input_value: str | Path = Path(tmp.name)
    else:
        # JSON body. FastAPI doesn't bind Form() and BaseModel together
        # cleanly; parse JSON manually.
        try:
            payload = await request.json()
        except Exception:  # noqa: BLE001
            return JSONResponse(
                status_code=400,
                content={"error": "provide either multipart `file` or JSON body"},
            )
        req = CloudIngestRequest.model_validate(payload)
        input_value = _resolve_input(req.url)
        domain = req.domain
        draft = req.draft
        with_plan = req.with_plan

    record = store.create("cloud_ingest")
    log_mod.append(
        op="cloud-ingest",
        fields={"auth": token_name, "task": record.task_id},
        summary=f"cloud ingest queued via token {token_name!r}",
    )

    def run() -> dict[str, Any]:
        result = ingest(
            input_value,
            domain=domain,
            with_plan=with_plan,
            draft=draft,
        )
        return _serialize_op_result(result)

    store.run_in_thread(record.task_id, run)
    return JSONResponse(
        status_code=202,
        content={"task_id": record.task_id, "status": "queued"},
    )
