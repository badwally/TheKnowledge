"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from fastapi import FastAPI

from gateway.web.routes import domains as domain_routes
from gateway.web.routes import ops as ops_routes
from gateway.web.routes import status as status_routes
from gateway.web.routes import tasks as task_routes
from gateway.web.schemas import HealthResponse
from gateway.web.tasks import TaskStore


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
    return app


app = create_app()
