"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from gateway.web.routes import domains as domain_routes
from gateway.web.routes import nlm as nlm_routes
from gateway.web.routes import ops as ops_routes
from gateway.web.routes import research as research_routes
from gateway.web.routes import review as review_routes
from gateway.web.routes import status as status_routes
from gateway.web.routes import tasks as task_routes
from gateway.web.routes import cloud as cloud_routes
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
    app.include_router(research_routes.router)
    app.include_router(review_routes.router)
    app.include_router(nlm_routes.router)
    app.include_router(cloud_routes.router)  # K3: /api/ingest (bearer-token)

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
