"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from gateway.web.auth import verify_bearer
from gateway.web.routes import domains as domain_routes
from gateway.web.routes import nlm as nlm_routes
from gateway.web.routes import ops as ops_routes
from gateway.web.routes import research as research_routes
from gateway.web.routes import review as review_routes
from gateway.web.routes import status as status_routes
from gateway.web.routes import tasks as task_routes
from gateway.web.routes import cloud as cloud_routes
from gateway.web.routes import sources as sources_routes
from gateway.web.routes import today as today_routes
from gateway.web.routes import inbox as inbox_routes
from gateway.web.schemas import HealthResponse
from gateway.web.tasks import TaskStore


_FRONTEND_DIST = Path(__file__).parent.parent.parent.parent / "web" / "dist"

# Paths under /api that are reachable without a bearer token. Everything else
# under /api is default-deny. Non-/api paths (the SPA static bundle) are public
# — they ship no data, only the client app, which authenticates its own calls.
_PUBLIC_API_PATHS = frozenset({"/api/health"})


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")
    app.state.task_store = TaskStore()

    @app.middleware("http")
    async def require_bearer(request: Request, call_next):
        """Default-deny gate: any /api/* path (except the public allowlist)
        requires a valid bearer token. Enforced here as middleware rather than
        per-router so a newly added endpoint is protected by default — a
        forgotten ``dependencies=[...]`` cannot silently open a write surface.
        The resolved token name is stashed on ``request.state`` for audit use
        by downstream handlers (e.g. cloud ingest)."""
        path = request.url.path
        if path.startswith("/api/") and path not in _PUBLIC_API_PATHS:
            try:
                request.state.token_name = verify_bearer(
                    request.headers.get("authorization")
                )
            except HTTPException as exc:
                return JSONResponse(
                    status_code=exc.status_code, content={"detail": exc.detail}
                )
        return await call_next(request)

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
    app.include_router(sources_routes.router)  # TOOL-13: /api/sources
    app.include_router(today_routes.router)    # TOOL-8: /today
    app.include_router(inbox_routes.router)    # TOOL-11: /api/inbox

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
