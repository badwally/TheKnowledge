"""Tests for the converter framework and the M2 web converter."""

from __future__ import annotations

import pytest

from gateway import converters, frontmatter as fm
from gateway import paths
from gateway.converters import web as web_mod
from gateway.converters.base import ConversionError, Converter
from gateway.converters.web import WebConverter
from gateway.ops.ingest import ingest, ingest_url


# --- registry / dispatch ----------------------------------------------------


class _StubConverter(Converter):
    type_name = "other"

    def detect(self, source: str) -> bool:
        return source.startswith("stub://")

    def convert(self, source: str) -> str:
        raise NotImplementedError


@pytest.fixture(autouse=True)
def _reset_registry():
    """Each test starts with a clean registry."""
    converters.reset_registry_for_tests()
    yield
    converters.reset_registry_for_tests()


def test_dispatch_routes_url_to_web():
    c = converters.dispatch("https://example.com/article")
    assert isinstance(c, WebConverter)


def test_dispatch_unknown_raises():
    with pytest.raises(converters.NoConverterError):
        converters.dispatch("ftp://example.com/file")


def test_register_then_dispatch_uses_first_match():
    converters.register(_StubConverter())
    assert isinstance(converters.dispatch("stub://thing"), _StubConverter)
    # Built-in WebConverter is added by _ensure_registered on first dispatch
    assert isinstance(converters.dispatch("https://example.com"), WebConverter)


def test_register_idempotent():
    converters.register(_StubConverter())
    converters.register(_StubConverter())
    matches = [c for c in [converters.dispatch("stub://x")]]
    assert len(matches) == 1


# --- web converter detection -----------------------------------------------


def test_web_detect_accepts_http_and_https():
    c = WebConverter()
    assert c.detect("http://example.com")
    assert c.detect("https://example.com/path")


def test_web_detect_rejects_local_paths():
    c = WebConverter()
    assert not c.detect("/tmp/file.md")
    assert not c.detect("file.md")
    assert not c.detect("ftp://example.com")


# --- web converter convert (mocked trafilatura) ----------------------------


def _install_fake_trafilatura(monkeypatch, *, html, body, metadata: dict):
    monkeypatch.setattr(web_mod, "_fetch", lambda url: html)
    monkeypatch.setattr(web_mod, "_extract_markdown", lambda h: body)

    class _MetaProxy:
        def __init__(self, d):
            self._d = d

        def as_dict(self):
            return self._d

    monkeypatch.setattr(web_mod, "_extract_metadata", lambda h: _MetaProxy(metadata))


def test_web_convert_produces_canonical_text(monkeypatch):
    _install_fake_trafilatura(
        monkeypatch,
        html="<html>...</html>",
        body="# Article\n\nFirst paragraph.\n\nSecond paragraph.",
        metadata={
            "title": "Sample Article",
            "author": "Jane Doe",
            "date": "2026-04-25",
            "description": "A short description.",
        },
    )

    text = WebConverter().convert("https://example.com/p/sample")
    front, body = fm.parse(text)

    assert front["type"] == "web"
    assert front["title"] == "Sample Article"
    assert front["url"] == "https://example.com/p/sample"
    assert front["authors"] == ["Jane Doe"]
    assert front["published_at"] == "2026-04-25"
    assert front["id"].startswith("web-2026-04-25-")
    assert front["meta"]["site"] == "example.com"
    assert "First paragraph" in body
    # content_hash should match the body
    from gateway.validator import compute_content_hash
    assert front["content_hash"] == compute_content_hash(body)


def test_web_convert_falls_back_when_no_published_date(monkeypatch):
    _install_fake_trafilatura(
        monkeypatch,
        html="<html>...</html>",
        body="Body without a date.\n",
        metadata={"title": "Untitled", "author": None, "date": None},
    )

    text = WebConverter().convert("https://example.com/no-date")
    front, _ = fm.parse(text)
    assert "published_at" not in front
    assert front["id"].startswith("web-")
    assert front["authors"] == []


def test_web_convert_fetch_failure_raises(monkeypatch):
    monkeypatch.setattr(web_mod, "_fetch", lambda url: None)
    with pytest.raises(ConversionError):
        WebConverter().convert("https://example.com/dead")


def test_web_convert_empty_extract_raises(monkeypatch):
    monkeypatch.setattr(web_mod, "_fetch", lambda url: "<html></html>")
    monkeypatch.setattr(web_mod, "_extract_markdown", lambda h: "   ")
    with pytest.raises(ConversionError):
        WebConverter().convert("https://example.com/empty")


# --- ingest end-to-end via converter ---------------------------------------


def test_ingest_url_end_to_end(kb_root, monkeypatch):
    _install_fake_trafilatura(
        monkeypatch,
        html="<html>x</html>",
        body="Body content for the URL ingest test.\n",
        metadata={
            "title": "URL Ingest Test",
            "author": "Test Author",
            "date": "2026-04-27",
        },
    )

    result = ingest_url("https://example.com/articles/url-ingest")
    assert result.success, result.errors
    assert not result.no_op

    # Some web file was written under raw/web/
    web_dir = paths.raw_dir_for("web")
    written = list(web_dir.glob("web-2026-04-27-*.md"))
    assert len(written) == 1, f"expected one raw/web/ file, got {written}"

    raw_text = written[0].read_text()
    front, body = fm.parse(raw_text)
    assert front["url"] == "https://example.com/articles/url-ingest"
    assert "Body content" in body

    # And a wiki source page exists for the same id
    wiki_path = paths.wiki_source_path(front["id"])
    assert wiki_path.exists()


def test_ingest_top_level_dispatcher_url(kb_root, monkeypatch):
    _install_fake_trafilatura(
        monkeypatch,
        html="<html/>",
        body="Dispatcher test body.\n",
        metadata={"title": "T", "author": None, "date": "2026-01-01"},
    )
    result = ingest("https://example.com/x")
    assert result.success, result.errors


def test_ingest_top_level_dispatcher_path(kb_root, make_source, tmp_path):
    src_text = make_source()
    p = tmp_path / "src.md"
    p.write_text(src_text)
    result = ingest(p)
    assert result.success, result.errors
    assert paths.raw_source_path("youtube", "yt-testABC_123").exists()


def test_ingest_url_idempotent(kb_root, monkeypatch):
    _install_fake_trafilatura(
        monkeypatch,
        html="<html/>",
        body="Idempotent body.\n",
        metadata={"title": "I", "author": None, "date": "2026-04-27"},
    )
    first = ingest_url("https://example.com/idempotent")
    assert first.success and not first.no_op

    second = ingest_url("https://example.com/idempotent")
    assert second.success
    # Same content_hash means M1's idempotency short-circuit fires.
    assert second.no_op


def test_ingest_url_page_changed_immutability(kb_root, monkeypatch):
    _install_fake_trafilatura(
        monkeypatch,
        html="<html/>",
        body="Original body.\n",
        metadata={"title": "C", "author": None, "date": "2026-04-27"},
    )
    first = ingest_url("https://example.com/changing")
    assert first.success

    # Page content changes (same URL, same date, so same id)
    _install_fake_trafilatura(
        monkeypatch,
        html="<html/>",
        body="Modified body.\n",
        metadata={"title": "C", "author": None, "date": "2026-04-27"},
    )
    second = ingest_url("https://example.com/changing")
    assert not second.success
    assert any("source-immutability" in e for e in second.errors)
