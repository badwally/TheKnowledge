"""QUAL-1: link-rot poller + lint check tests."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.link_rot import run as lint_run
from gateway.pollers.link_rot import LinkRotPoller, check_url


# --- helpers ----------------------------------------------------------------


def _make_raw_web(kb_root: Path, source_id: str, url: str, **extra) -> Path:
    p = paths.raw_dir() / "web" / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "type": "web",
        "title": f"Source {source_id}",
        "url": url,
        "authors": [],
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
        "domains": [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
        **extra,
    }
    p.write_text(fm.serialize(front, "Body.\n"))
    return p


def _make_wiki_source(kb_root: Path, source_id: str) -> Path:
    p = paths.wiki_dir() / "sources" / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "source",
        "source_id": source_id,
        "source_type": "web",
        "title": f"Source {source_id}",
        "ingested_at": "2026-01-01T00:00:00Z",
        "domains": [],
    }
    p.write_text(fm.serialize(front, "## Summary\n\nstub\n\n## Key claims\n\nstub\n"))
    return p


# --- check_url unit tests ---------------------------------------------------


def test_check_url_ok(kb_root: Path) -> None:
    class _FakeResp:
        status = 200
        url = "https://example.com/page"
        def __enter__(self): return self
        def __exit__(self, *a): pass

    with patch("urllib.request.urlopen", return_value=_FakeResp()):
        status, effective = check_url("https://example.com/page")
    assert status == "ok"


def test_check_url_redirect(kb_root: Path) -> None:
    import urllib.error

    class _FakeResp:
        status = 200
        url = "https://example.com/new-page"
        def __enter__(self): return self
        def __exit__(self, *a): pass

    with patch("urllib.request.urlopen", return_value=_FakeResp()):
        status, effective = check_url("https://example.com/old-page")
    assert status == "redirect"
    assert effective == "https://example.com/new-page"


def test_check_url_dead_on_404(kb_root: Path) -> None:
    import urllib.error
    with patch("urllib.request.urlopen", side_effect=urllib.error.HTTPError(
        "https://example.com", 404, "Not Found", {}, None
    )):
        status, _ = check_url("https://example.com/gone")
    assert status == "dead"


def test_check_url_dead_on_connection_error(kb_root: Path) -> None:
    with patch("urllib.request.urlopen", side_effect=OSError("connection refused")):
        status, _ = check_url("https://example.com/gone")
    assert status == "dead"


def test_check_url_dead_on_empty_url(kb_root: Path) -> None:
    status, _ = check_url("")
    assert status == "dead"


# --- LinkRotPoller tests ----------------------------------------------------


def test_poller_no_sources(kb_root: Path) -> None:
    result = LinkRotPoller().run()
    assert result.success


def test_poller_skips_no_url(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "")
    result = LinkRotPoller().run()
    assert result.fetched == 0
    assert result.skipped == 1


def test_poller_checks_url_and_writes_status(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "https://example.com/page")

    with patch("gateway.pollers.link_rot.check_url", return_value=("ok", "https://example.com/page")):
        result = LinkRotPoller().run()

    assert result.fetched == 1
    front, _ = fm.parse((paths.raw_dir() / "web" / "web-aaa.md").read_text())
    assert front["link_status"] == "ok"
    assert "last_checked_at" in front


def test_poller_updates_wiki_source_page(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "https://example.com/page")
    _make_wiki_source(kb_root, "web-aaa")

    with patch("gateway.pollers.link_rot.check_url", return_value=("dead", None)):
        LinkRotPoller().run()

    wfront, _ = fm.parse((paths.wiki_dir() / "sources" / "web-aaa.md").read_text())
    assert wfront["link_status"] == "dead"


def test_poller_skips_recently_checked(kb_root: Path) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _make_raw_web(kb_root, "web-aaa", "https://example.com/page", last_checked_at=now)

    called = []
    with patch("gateway.pollers.link_rot.check_url", side_effect=lambda u: called.append(u) or ("ok", u)):
        result = LinkRotPoller().run()

    assert called == []
    assert result.skipped == 1


def test_poller_redirect_stores_redirect_url(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "https://example.com/old")

    with patch("gateway.pollers.link_rot.check_url", return_value=("redirect", "https://example.com/new")):
        LinkRotPoller().run()

    front, _ = fm.parse((paths.raw_dir() / "web" / "web-aaa.md").read_text())
    assert front["link_status"] == "redirect"
    assert front.get("meta", {}).get("redirect_url") == "https://example.com/new"


# --- lint/link_rot tests ----------------------------------------------------


def test_lint_empty(kb_root: Path) -> None:
    assert lint_run() == []


def test_lint_dead_flagged_as_warning(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "https://dead.example.com", link_status="dead")
    findings = lint_run()
    assert len(findings) == 1
    assert findings[0].severity == "warning"
    assert "dead link" in findings[0].message
    assert findings[0].metadata["source_id"] == "web-aaa"


def test_lint_ok_not_flagged(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "https://ok.example.com", link_status="ok")
    assert lint_run() == []


def test_lint_unchecked_flagged_as_info(kb_root: Path) -> None:
    _make_raw_web(kb_root, "web-aaa", "https://example.com/unchecked")
    findings = lint_run()
    assert len(findings) == 1
    assert findings[0].severity == "info"
    assert "never checked" in findings[0].message


def test_lint_dead_with_archive_url_in_message(kb_root: Path) -> None:
    _make_raw_web(
        kb_root,
        "web-aaa",
        "https://dead.example.com",
        link_status="dead",
        meta={"archive_url": "https://web.archive.org/web/123/dead.example.com"},
    )
    findings = lint_run()
    assert "Wayback" in findings[0].message
