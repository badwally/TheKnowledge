"""FastAPI app construction for `wiki serve`."""

from __future__ import annotations

from fastapi import FastAPI

from gateway.web.schemas import HealthResponse


def create_app() -> FastAPI:
    app = FastAPI(title="wiki gateway", version="0.1.0")

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    return app


app = create_app()
