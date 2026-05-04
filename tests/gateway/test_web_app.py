"""Tests for the M40 FastAPI web app."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway.web.app import create_app


@pytest.fixture
def client(kb_root):
    app = create_app()
    return TestClient(app)


def test_app_returns_health_ok(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
