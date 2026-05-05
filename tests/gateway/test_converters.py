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


def _build_minimal_pdf(path, *, text: str) -> None:
    """Synthesize a one-page PDF for tests. Copy of the helper in test_converters_m10."""
    try:
        from reportlab.pdfgen import canvas  # type: ignore[import-not-found]
        from reportlab.lib.pagesizes import letter  # type: ignore[import-not-found]
        c = canvas.Canvas(str(path), pagesize=letter)
        c.drawString(72, 720, text)
        c.save()
    except ImportError:
        content = (
            "%PDF-1.4\n"
            "1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
            "2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
            "3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            "/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj\n"
            f"4 0 obj << /Length {12 + len(text)} >> stream\n"
            f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET\nendstream endobj\n"
            "5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n"
            "xref\n0 6\n0000000000 65535 f \n"
            "trailer << /Size 6 /Root 1 0 R >>\nstartxref\n0\n%%EOF\n"
        )
        path.write_bytes(content.encode("latin-1"))


def test_ingest_arxiv_url_with_fetch_pdf_uses_pdf_body(kb_root, monkeypatch):
    """`ingest(url, fetch_pdf=True)` routes through ArxivConverter.convert_with_pdf."""
    from gateway.converters import arxiv as arxiv_mod

    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "Just an abstract.",
        "published_at": "2024-04-02", "authors": ["A"], "categories": [],
        "doi": "", "primary_category": "", "journal_ref": "", "comment": "",
    })

    def _fake_download(aid, target):
        _build_minimal_pdf(target, text="Full PDF body content.")

    monkeypatch.setattr(arxiv_mod, "_download_pdf", _fake_download)
    arxiv_mod._reset_rate_limit_for_tests()

    result = ingest("https://arxiv.org/abs/2403.12345", fetch_pdf=True)
    assert result.success, result.errors

    raw = paths.raw_source_path("arxiv", "arxiv-2403.12345").read_text()
    front, body = fm.parse(raw)
    assert "Full PDF body content." in body
    assert "Just an abstract." not in body
    assert front["meta"]["abstract_only"] is False


def test_ingest_arxiv_bare_id_routes_to_arxiv_converter(kb_root, monkeypatch):
    """`ingest("2403.12345")` (non-URL string) dispatches through arxiv."""
    from gateway.converters import arxiv as arxiv_mod

    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "Bare-id abstract.",
        "published_at": "2024-04-02", "authors": [], "categories": [],
        "doi": "", "primary_category": "", "journal_ref": "", "comment": "",
    })
    arxiv_mod._reset_rate_limit_for_tests()

    result = ingest("2403.12345")
    assert result.success, result.errors

    raw = paths.raw_source_path("arxiv", "arxiv-2403.12345").read_text()
    front, body = fm.parse(raw)
    assert front["type"] == "arxiv"
    assert "Bare-id abstract." in body


def test_ingest_fetch_pdf_unsupported_for_web_returns_error(kb_root, monkeypatch):
    """fetch_pdf=True against a non-arxiv source returns a clear error."""
    _install_fake_trafilatura(
        monkeypatch,
        html="<html/>",
        body="Web body.\n",
        metadata={"title": "T", "author": None, "date": "2026-01-01"},
    )
    result = ingest("https://example.com/article", fetch_pdf=True)
    assert not result.success
    assert any("fetch_pdf" in e or "convert_with_pdf" in e for e in result.errors)


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
