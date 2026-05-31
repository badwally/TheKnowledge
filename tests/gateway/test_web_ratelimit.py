"""Per-token rate limiting (260530 review, finding #2).

A token bucket per identity caps the rate of mutating/expensive requests so a
credentialed caller cannot drain paid LLM/NotebookLM quota with a flood. Reads
are not limited by this component (the middleware only consults it for
non-GET requests).
"""

from __future__ import annotations

import pytest

from gateway.web.ratelimit import TokenBucketLimiter


def test_allows_up_to_capacity_then_blocks():
    # Deterministic clock so the test does not depend on wall time.
    now = {"t": 1000.0}
    limiter = TokenBucketLimiter(rate_per_min=60, clock=lambda: now["t"])

    # burst == capacity == rate; the 60th passes, the 61st is blocked.
    for i in range(60):
        assert limiter.allow("token-a") is True, f"request {i} should pass"
    assert limiter.allow("token-a") is False


def test_refills_over_time():
    now = {"t": 0.0}
    limiter = TokenBucketLimiter(rate_per_min=60, clock=lambda: now["t"])

    for _ in range(60):
        assert limiter.allow("token-a") is True
    assert limiter.allow("token-a") is False

    # One second later, 1 token has refilled (60/min == 1/s).
    now["t"] += 1.0
    assert limiter.allow("token-a") is True
    assert limiter.allow("token-a") is False


def test_buckets_are_per_identity():
    now = {"t": 0.0}
    limiter = TokenBucketLimiter(rate_per_min=2, clock=lambda: now["t"])

    assert limiter.allow("token-a") is True
    assert limiter.allow("token-a") is True
    assert limiter.allow("token-a") is False
    # A different token has its own independent bucket.
    assert limiter.allow("token-b") is True


def test_zero_or_negative_rate_disables_limiting():
    limiter = TokenBucketLimiter(rate_per_min=0)
    for _ in range(1000):
        assert limiter.allow("token-a") is True


# --- HTTP-level enforcement (finding #2) ----------------------------------


def _authed_app(kb_root, **overrides):
    from fastapi.testclient import TestClient

    from gateway.web import auth
    from gateway.web.app import create_app

    token = auth.add_token("limit-test")
    app = create_app()
    for name, value in overrides.items():
        setattr(app.state, name, value)
    client = TestClient(app, headers={"Authorization": f"Bearer {token}"})
    return client


def test_mutating_request_rate_limited_returns_429(kb_root):
    # Capacity 1: the first mutating POST passes (and 400s on the missing
    # page); the second is blocked by the limiter before reaching the route.
    client = _authed_app(kb_root, rate_limiter=TokenBucketLimiter(rate_per_min=1))
    first = client.post(
        "/api/ops/finalize", json={"page_path": "wiki/x.md", "abandon": False}
    )
    assert first.status_code == 400
    second = client.post(
        "/api/ops/finalize", json={"page_path": "wiki/x.md", "abandon": False}
    )
    assert second.status_code == 429


def test_get_requests_not_rate_limited(kb_root):
    # Even with capacity 1, repeated GETs are never limited (reads/polling).
    client = _authed_app(kb_root, rate_limiter=TokenBucketLimiter(rate_per_min=1))
    for _ in range(5):
        assert client.get("/api/status").status_code == 200


def test_task_capacity_returns_503(kb_root):
    from gateway.web.tasks import TaskStore

    # A task store with no free slots: any task-spawning POST → 503.
    client = _authed_app(kb_root, task_store=TaskStore(max_concurrent=0))
    resp = client.post("/api/ops/query", json={"question": "q", "domain": "d"})
    assert resp.status_code == 503
