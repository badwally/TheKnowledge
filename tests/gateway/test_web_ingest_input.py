"""Network ingest accepts only http(s) URLs or sandboxed multipart uploads.

Product-readiness review (260530) finding #3: `_resolve_input` treated any
non-http(s) input as a local filesystem path and read it server-side, so an
API caller could ingest `/etc/passwd`, `~/.ssh/id_rsa`, etc. and surface the
contents through the wiki. Local-file ingest is operator-only via the
`wiki ingest` CLI (not network-exposed); the HTTP surface must reject local
paths and accept only http(s) URLs or a multipart upload (written to a
server-controlled temp file).
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from gateway.web import auth
from gateway.web.app import create_app


@pytest.fixture
def token(kb_root) -> str:
    return auth.add_token("ingest-test")


@pytest.fixture
def client(kb_root, token) -> TestClient:
    return TestClient(create_app(), headers={"Authorization": f"Bearer {token}"})


@pytest.mark.parametrize(
    "path",
    ["/etc/passwd", "~/.ssh/id_rsa", "../../secret", "/tmp/x.md", "file:///etc/passwd"],
)
def test_ops_ingest_rejects_local_path(client, path):
    resp = client.post("/api/ops/ingest", json={"input": path})
    assert resp.status_code == 400, resp.text


@pytest.mark.parametrize("path", ["/etc/passwd", "file:///etc/passwd", "../x"])
def test_cloud_ingest_rejects_local_path(client, path):
    resp = client.post("/api/ingest", json={"url": path})
    assert resp.status_code == 400, resp.text


def test_ops_ingest_accepts_http_url(client):
    # Validation passes synchronously → 202 queued (the fetch happens in the
    # background task; we only assert the input cleared validation).
    resp = client.post("/api/ops/ingest", json={"input": "https://example.com/x"})
    assert resp.status_code == 202, resp.text


def test_cloud_ingest_accepts_http_url(client):
    resp = client.post("/api/ingest", json={"url": "https://example.com/x"})
    assert resp.status_code == 202, resp.text


def test_cloud_multipart_upload_still_works(client, make_source):
    # The sanctioned file-ingest path: multipart upload → server temp file.
    content = make_source(id_="yt-uploadTest_AB")
    resp = client.post(
        "/api/ingest",
        files={"file": ("upload.md", content, "text/markdown")},
    )
    assert resp.status_code == 202, resp.text
