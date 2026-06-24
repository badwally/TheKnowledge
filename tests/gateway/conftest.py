"""Shared pytest fixtures for gateway tests."""

import os
from datetime import datetime, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway import validator


@pytest.fixture(autouse=True)
def _restore_environ():
    """Snapshot and restore os.environ around every test.

    cli.main loads .knowledge/secrets.env by writing directly to os.environ
    (a once-per-process side effect in production). Direct writes outlive
    monkeypatch's restoration, so without this any test that invokes main
    would leak FIRECRAWL_API_KEY / WIKI_WEB_SCRAPER into sibling tests."""
    saved = os.environ.copy()
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(saved)


def make_canonical_source(
    *,
    type_: str = "youtube",
    id_: str = "yt-testABC_123",
    title: str = "Test source",
    body: str = "Body content for the test source.\n",
    url: str = "https://www.youtube.com/watch?v=testABC_123",
    authors: list[str] | None = None,
    published_at: str = "2026-01-15",
    domains: list[str] | None = None,
    meta: dict | None = None,
    extra_front: dict | None = None,
) -> str:
    """Build a valid canonical source markdown string with correct content_hash."""
    front: dict = {
        "id": id_,
        "type": type_,
        "title": title,
        "url": url,
        "authors": authors if authors is not None else ["Test Author"],
        "published_at": published_at,
        "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "content_hash": validator.compute_content_hash(body),
        "domains": domains if domains is not None else [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": meta if meta is not None else {"channel": "Test Channel", "duration_seconds": 600},
    }
    if extra_front:
        front.update(extra_front)
    return fm.serialize(front, body)


@pytest.fixture
def make_source():
    """Test helper available as a fixture."""
    return make_canonical_source


@pytest.fixture
def auth_token(kb_root) -> str:
    """Mint a bearer token in the temp knowledge root and return the plaintext."""
    from gateway.web import auth

    return auth.add_token("test-client")


@pytest.fixture
def client(kb_root, auth_token):
    """Authenticated TestClient for the web API.

    The web API is default-deny (every `/api/*` route except `/api/health`
    requires a bearer token; see `gateway.web.app.require_bearer`). The
    Authorization header is attached to every request so existing endpoint
    tests exercise the handlers rather than the auth gate. Tests that need to
    assert the gate itself construct their own unauthenticated client (see
    `test_web_auth.py`).
    """
    from fastapi.testclient import TestClient

    from gateway.web.app import create_app

    return TestClient(
        create_app(), headers={"Authorization": f"Bearer {auth_token}"}
    )
