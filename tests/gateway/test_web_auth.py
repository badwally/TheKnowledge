"""Default-deny authentication on the web API.

Product-readiness fix (260530 review, finding #1): every `/api/*` route
must require a valid bearer token EXCEPT `/api/health`. The SPA static
mount (non-`/api/` paths) stays public. A forgotten router must not be
able to slip through — the gate is middleware, so default-deny holds by
construction.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway.web import auth
from gateway.web.app import create_app


@pytest.fixture
def token(kb_root) -> str:
    return auth.add_token("test-client")


@pytest.fixture
def anon(kb_root) -> TestClient:
    """Client with NO Authorization header."""
    return TestClient(create_app())


@pytest.fixture
def authed(kb_root, token) -> TestClient:
    return TestClient(create_app(), headers={"Authorization": f"Bearer {token}"})


# --- health + static are exempt -------------------------------------------


def test_health_open_without_token(anon):
    resp = anon.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_spa_static_open_without_token(anon):
    # Non-/api path → SPA fallback (200 if build present, 404 if not), never 401.
    resp = anon.get("/")
    assert resp.status_code in (200, 404)


# --- every /api route is default-deny -------------------------------------


@pytest.mark.parametrize(
    "method,path,body",
    [
        # reads
        ("get", "/api/status", None),
        ("get", "/api/domains", None),
        ("get", "/api/sources", None),
        ("get", "/api/tasks/anything", None),
        # writes / expensive
        ("post", "/api/ops/finalize", {"page_path": "wiki/x.md", "abandon": False}),
        ("post", "/api/ops/ingest", {"input": "https://example.com"}),
        ("post", "/api/domains/x/promote", None),
        ("post", "/api/ops/query", {"question": "q"}),
    ],
)
def test_api_routes_reject_anonymous(anon, method, path, body):
    resp = getattr(anon, method)(path, json=body) if body is not None else getattr(anon, method)(path)
    assert resp.status_code == 401, f"{method.upper()} {path} should be 401 without a token"


def test_invalid_token_rejected(kb_root, token):
    bad = TestClient(create_app(), headers={"Authorization": "Bearer not-a-real-token"})
    assert bad.get("/api/status").status_code == 401


def test_malformed_authorization_header_rejected(kb_root):
    c = TestClient(create_app(), headers={"Authorization": "Basic abc"})
    assert c.get("/api/status").status_code == 401


# --- valid token passes through -------------------------------------------


def test_valid_token_allows_read(authed):
    assert authed.get("/api/status").status_code == 200


def test_valid_token_allows_write_path(authed):
    # finalize a nonexistent page → reaches the handler → 400 (not 401).
    resp = authed.post(
        "/api/ops/finalize",
        json={"page_path": "wiki/concepts/nope.md", "abandon": False},
    )
    assert resp.status_code == 400
