"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from fastapi import FastAPI

from gateway.web.routes import domains as domain_routes
from gateway.web.routes import status as status_routes
from gateway.web.schemas import HealthResponse


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    app.include_router(status_routes.router)
    app.include_router(domain_routes.router)
    return app


app = create_app()
