"""TOOL-11: /api/inbox — inbox triage web view."""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from gateway import paths
from gateway.web.app import create_app


@pytest.fixture
def client(kb_root: Path) -> TestClient:
    return TestClient(create_app())


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


def _inbox_dir(kb_root: Path) -> Path:
    d = paths.raw_dir() / "inbox"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _failed_dir(kb_root: Path) -> Path:
    d = paths.raw_dir() / "inbox" / "_failed"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _write_pending(kb_root: Path, name: str, *, frontmatter: str = "") -> Path:
    inbox = _inbox_dir(kb_root)
    p = inbox / name
    content = frontmatter if frontmatter else "# pending file\n"
    p.write_text(content)
    return p


def _write_failed(kb_root: Path, name: str, reason: str = "") -> Path:
    failed = _failed_dir(kb_root)
    p = failed / name
    p.write_text("# failed file\n")
    if reason:
        p.with_suffix(p.suffix + ".reason.txt").write_text(reason + "\n")
    return p


# --------------------------------------------------------------------------- #
# GET /api/inbox                                                               #
# --------------------------------------------------------------------------- #


def test_inbox_empty_when_no_dirs(client: TestClient, kb_root: Path) -> None:
    resp = client.get("/api/inbox")
    assert resp.status_code == 200
    data = resp.json()
    assert data["pending"] == []
    assert data["failed"] == []


def test_inbox_pending_file_listed(client: TestClient, kb_root: Path) -> None:
    _write_pending(kb_root, "test-source.md")
    resp = client.get("/api/inbox")
    assert resp.status_code == 200
    pending = resp.json()["pending"]
    assert len(pending) == 1
    assert pending[0]["filename"] == "test-source.md"
    assert pending[0]["size_bytes"] >= 0
    assert "modified_at" in pending[0]


def test_inbox_sniffs_frontmatter(client: TestClient, kb_root: Path) -> None:
    fm = "---\ntype: web\ntitle: My Article\nurl: https://example.com\n---\n"
    _write_pending(kb_root, "article.md", frontmatter=fm)
    resp = client.get("/api/inbox")
    item = resp.json()["pending"][0]
    assert item["sniffed_type"] == "web"
    assert item["sniffed_title"] == "My Article"
    assert item["sniffed_url"] == "https://example.com"


def test_inbox_failed_file_listed(client: TestClient, kb_root: Path) -> None:
    _write_failed(kb_root, "20260101T120000Z-bad-source.md", reason="ingest failed: timeout")
    resp = client.get("/api/inbox")
    failed = resp.json()["failed"]
    assert len(failed) == 1
    assert failed[0]["original_name"] == "bad-source.md"
    assert "2026" in failed[0]["failed_at"]
    assert failed[0]["reason"] == "ingest failed: timeout"


def test_inbox_failed_no_reason_file(client: TestClient, kb_root: Path) -> None:
    _write_failed(kb_root, "20260101T120000Z-no-reason.md")
    resp = client.get("/api/inbox")
    failed = resp.json()["failed"]
    assert failed[0]["reason"] == ""


def test_inbox_ignores_non_md_in_inbox(client: TestClient, kb_root: Path) -> None:
    inbox = _inbox_dir(kb_root)
    (inbox / "not-markdown.txt").write_text("not md")
    resp = client.get("/api/inbox")
    assert resp.json()["pending"] == []


def test_inbox_ignores_subdirs_in_pending(client: TestClient, kb_root: Path) -> None:
    inbox = _inbox_dir(kb_root)
    (inbox / "_failed").mkdir(exist_ok=True)  # _failed is a subdir, not a file
    resp = client.get("/api/inbox")
    assert resp.json()["pending"] == []


# --------------------------------------------------------------------------- #
# POST /api/inbox/retry/{filename}                                             #
# --------------------------------------------------------------------------- #


def test_retry_moves_file_to_inbox(client: TestClient, kb_root: Path) -> None:
    _write_failed(kb_root, "20260101T120000Z-retry-me.md", reason="network error")
    resp = client.post("/api/inbox/retry/20260101T120000Z-retry-me.md")
    assert resp.status_code == 200
    data = resp.json()
    assert data["ok"] is True
    assert "retry-me.md" in data["message"]
    # File should now be in inbox
    inbox = paths.raw_dir() / "inbox" / "retry-me.md"
    assert inbox.exists()
    # Failed file should be gone
    assert not (_failed_dir(kb_root) / "20260101T120000Z-retry-me.md").exists()


def test_retry_removes_reason_file(client: TestClient, kb_root: Path) -> None:
    _write_failed(kb_root, "20260101T120000Z-clean.md", reason="old error")
    reason_path = _failed_dir(kb_root) / "20260101T120000Z-clean.md.reason.txt"
    assert reason_path.exists()
    client.post("/api/inbox/retry/20260101T120000Z-clean.md")
    assert not reason_path.exists()


def test_retry_404_for_missing_file(client: TestClient, kb_root: Path) -> None:
    resp = client.post("/api/inbox/retry/nonexistent.md")
    assert resp.status_code == 404


def test_retry_409_if_already_pending(client: TestClient, kb_root: Path) -> None:
    _write_pending(kb_root, "conflict.md")
    _write_failed(kb_root, "20260101T120000Z-conflict.md")
    resp = client.post("/api/inbox/retry/20260101T120000Z-conflict.md")
    assert resp.status_code == 409
