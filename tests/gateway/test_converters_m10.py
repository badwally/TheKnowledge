"""Tests for M10 converters (youtube, arxiv, pubmed, pdf) and pollers.

All network-dependent tests inject mocks via monkeypatching the small
`_fetch_*` adapters in each converter module. PDF tests use real
pdfplumber against a synthesized one-page PDF (cheap, no network).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import converters
from gateway import frontmatter as fm
from gateway import paths
from gateway.converters import arxiv as arxiv_mod
from gateway.converters import pdf as pdf_mod
from gateway.converters import pubmed as pubmed_mod
from gateway.converters import youtube as yt_mod
from gateway.converters.base import ConversionError


@pytest.fixture(autouse=True)
def _reset_registry():
    converters.reset_registry_for_tests()
    yield
    converters.reset_registry_for_tests()


# --- youtube ---------------------------------------------------------------


def test_youtube_extract_video_id_handles_common_forms():
    cases = {
        "https://www.youtube.com/watch?v=LfRiBJgD7sk": "LfRiBJgD7sk",
        "https://youtu.be/LfRiBJgD7sk": "LfRiBJgD7sk",
        "https://www.youtube.com/embed/LfRiBJgD7sk": "LfRiBJgD7sk",
        "https://youtube.com/shorts/abc123XYZ-_": "abc123XYZ-_",
        "https://www.youtube.com/watch?v=LfRiBJgD7sk&t=42": "LfRiBJgD7sk",
    }
    for url, expected in cases.items():
        assert yt_mod.extract_video_id(url) == expected, url


def test_youtube_detect_rejects_non_youtube():
    c = yt_mod.YouTubeConverter()
    assert not c.detect("https://example.com/foo")
    assert not c.detect("/local/file.mp4")


def test_youtube_convert_produces_canonical(monkeypatch):
    monkeypatch.setattr(yt_mod, "_fetch_oembed", lambda vid: {
        "title": "GLP-1 RA Mechanisms",
        "author_name": "Test Channel",
        "author_url": "https://www.youtube.com/c/TestChannel",
    })
    monkeypatch.setattr(yt_mod, "_fetch_transcript", lambda vid: [
        {"text": "Welcome to the show.", "start": 0.0, "duration": 2.5},
        {"text": "Today we discuss GLP-1.", "start": 2.5, "duration": 3.0},
    ])

    text = yt_mod.YouTubeConverter().convert("https://www.youtube.com/watch?v=abc123XYZ_-")
    front, body = fm.parse(text)
    assert front["id"] == "yt-abc123XYZ_-"
    assert front["type"] == "youtube"
    assert front["title"] == "GLP-1 RA Mechanisms"
    assert front["authors"] == ["Test Channel"]
    assert front["meta"]["snippet_count"] == 2
    assert "[0] Welcome to the show." in body
    assert "[2] Today we discuss GLP-1." in body


def test_youtube_convert_empty_transcript_raises(monkeypatch):
    monkeypatch.setattr(yt_mod, "_fetch_oembed", lambda vid: {"title": "x", "author_name": "y"})
    monkeypatch.setattr(yt_mod, "_fetch_transcript", lambda vid: [])
    with pytest.raises(ConversionError):
        yt_mod.YouTubeConverter().convert("https://www.youtube.com/watch?v=abc123XYZ_-")


# --- arxiv -----------------------------------------------------------------


def test_arxiv_extract_id_handles_url_forms():
    assert arxiv_mod.extract_arxiv_id("https://arxiv.org/abs/2403.12345") == "2403.12345"
    assert arxiv_mod.extract_arxiv_id("http://arxiv.org/abs/2403.12345v2") == "2403.12345"
    assert arxiv_mod.extract_arxiv_id("https://arxiv.org/pdf/2403.12345") == "2403.12345"
    assert arxiv_mod.extract_arxiv_id("https://example.com/foo") is None


def test_arxiv_detect():
    c = arxiv_mod.ArxivConverter()
    assert c.detect("https://arxiv.org/abs/2403.12345")
    assert not c.detect("https://arxiv.org/list/cs.LG/2024")
    assert not c.detect("/local/file.md")


def test_arxiv_convert_produces_canonical(monkeypatch):
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "GLP-1 receptor agonism in mesolimbic circuitry",
        "abstract": "We show that GLP-1 receptor agonists modulate dopamine signaling.",
        "published_at": "2024-04-02",
        "authors": ["J. Liu", "P. Rondard"],
        "categories": ["q-bio.NC"],
        "doi": "10.1234/example.2024",
    })

    text = arxiv_mod.ArxivConverter().convert("https://arxiv.org/abs/2403.12345v1")
    front, body = fm.parse(text)
    assert front["id"] == "arxiv-2403.12345"
    assert front["type"] == "arxiv"
    assert front["meta"]["arxiv_id"] == "2403.12345"
    assert front["meta"]["categories"] == ["q-bio.NC"]
    assert front["meta"]["doi"] == "10.1234/example.2024"
    assert front["published_at"] == "2024-04-02"
    assert "GLP-1 receptor agonists" in body


def test_arxiv_convert_no_abstract_raises(monkeypatch):
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "", "published_at": "", "authors": [], "categories": [], "doi": "",
    })
    with pytest.raises(ConversionError):
        arxiv_mod.ArxivConverter().convert("https://arxiv.org/abs/2403.12345")


# --- pubmed ----------------------------------------------------------------


def test_pubmed_extract_pmid():
    assert pubmed_mod.extract_pmid("https://pubmed.ncbi.nlm.nih.gov/39847203") == "39847203"
    assert pubmed_mod.extract_pmid("https://pubmed.ncbi.nlm.nih.gov/39847203/") == "39847203"
    assert pubmed_mod.extract_pmid("https://example.com/foo") is None


def test_pubmed_detect():
    c = pubmed_mod.PubMedConverter()
    assert c.detect("https://pubmed.ncbi.nlm.nih.gov/39847203/")
    assert not c.detect("https://www.nih.gov/foo")


def test_pubmed_convert_produces_canonical(monkeypatch):
    monkeypatch.setattr(pubmed_mod, "_fetch_metadata", lambda pmid: {
        "title": "Reward modulation by GLP-1RA: a review",
        "abstract": "**Background.** Some background.\n\n**Findings.** Some findings.",
        "journal": "Nature Neuroscience",
        "published_at": "2024-08-15",
        "doi": "10.1038/example.2024",
        "mesh_terms": ["Glucagon-Like Peptide 1", "Dopamine"],
        "authors": ["Jane Smith", "John Doe"],
    })
    text = pubmed_mod.PubMedConverter().convert("https://pubmed.ncbi.nlm.nih.gov/39847203/")
    front, body = fm.parse(text)
    assert front["id"] == "pubmed-39847203"
    assert front["type"] == "pubmed"
    assert front["meta"]["pmid"] == "39847203"
    assert front["meta"]["mesh_terms"] == ["Glucagon-Like Peptide 1", "Dopamine"]
    assert front["meta"]["journal"] == "Nature Neuroscience"
    assert front["published_at"] == "2024-08-15"
    assert "Some findings." in body


def test_pubmed_normalize_month():
    assert pubmed_mod._normalize_month("Jan") == "01"
    assert pubmed_mod._normalize_month("June") == "06"
    assert pubmed_mod._normalize_month("12") == "12"
    assert pubmed_mod._normalize_month("garbage") == "01"


# --- pdf -------------------------------------------------------------------


def _build_minimal_pdf(path: Path, *, text: str = "Hello PDF World", title: str = "Test PDF", author: str = "Test Author") -> Path:
    """Synthesize a one-page PDF using pdfplumber's underlying pdfminer reader.

    We bypass any heavy PDF generation library by invoking reportlab if
    present. If reportlab isn't available, fall back to a hand-rolled
    minimal PDF — pdfplumber accepts simple PDFs.
    """
    try:
        from reportlab.pdfgen import canvas  # type: ignore[import-not-found]
        from reportlab.lib.pagesizes import letter  # type: ignore[import-not-found]
        c = canvas.Canvas(str(path), pagesize=letter)
        c.setTitle(title)
        c.setAuthor(author)
        c.drawString(72, 720, text)
        c.save()
        return path
    except ImportError:
        # Hand-rolled minimal PDF (one page, single string)
        content = (
            "%PDF-1.4\n"
            "1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
            "2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
            "3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            "/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj\n"
            f"4 0 obj << /Length {12 + len(text)} >> stream\n"
            f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET\nendstream endobj\n"
            "5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n"
            f"6 0 obj << /Title ({title}) /Author ({author}) /CreationDate (D:20260101) >> endobj\n"
            "xref\n0 7\n0000000000 65535 f \n"
            "trailer << /Size 7 /Root 1 0 R /Info 6 0 R >>\nstartxref\n0\n%%EOF\n"
        )
        path.write_bytes(content.encode("latin-1"))
        return path


def test_pdf_detect():
    c = pdf_mod.PDFConverter()
    assert c.detect("/tmp/foo.pdf")
    assert c.detect("foo.PDF")
    assert not c.detect("foo.md")
    assert not c.detect("https://example.com/foo.pdf")


def test_pdf_convert_extracts_text_and_writes_sidecar(kb_root, tmp_path):
    src_pdf = tmp_path / "source.pdf"
    _build_minimal_pdf(src_pdf, text="Hello PDF Body", title="Hello", author="Test Auth")

    text = pdf_mod.PDFConverter().convert(str(src_pdf))
    front, body = fm.parse(text)

    assert front["type"] == "pdf"
    assert front["id"].startswith("pdf-")
    assert "Hello PDF Body" in body
    assert front["meta"]["extraction_tool"] == "pdfplumber"

    # Sidecar PDF preserved at raw/pdf/<id>.pdf
    sidecar = paths.raw_dir_for("pdf") / f"{front['id']}.pdf"
    assert sidecar.exists()
    assert sidecar.stat().st_size == src_pdf.stat().st_size


def test_pdf_convert_missing_file_raises(kb_root):
    with pytest.raises(ConversionError):
        pdf_mod.PDFConverter().convert("/does/not/exist.pdf")


# --- registry order -------------------------------------------------------


def test_dispatch_youtube_url_routes_to_youtube_converter():
    c = converters.dispatch("https://www.youtube.com/watch?v=abcDEF12345")
    assert isinstance(c, yt_mod.YouTubeConverter)


def test_dispatch_arxiv_url_routes_to_arxiv_converter():
    c = converters.dispatch("https://arxiv.org/abs/2403.12345")
    assert isinstance(c, arxiv_mod.ArxivConverter)


def test_dispatch_pubmed_url_routes_to_pubmed_converter():
    c = converters.dispatch("https://pubmed.ncbi.nlm.nih.gov/39847203/")
    assert isinstance(c, pubmed_mod.PubMedConverter)


def test_dispatch_generic_url_falls_back_to_web():
    from gateway.converters.web import WebConverter
    c = converters.dispatch("https://example.com/some/article")
    assert isinstance(c, WebConverter)


def test_dispatch_pdf_path_routes_to_pdf_converter():
    c = converters.dispatch("/tmp/whatever.pdf")
    assert isinstance(c, pdf_mod.PDFConverter)


# --- ingest_file end-to-end with PDF --------------------------------------


def test_ingest_file_pdf_end_to_end(kb_root, tmp_path):
    src_pdf = tmp_path / "thing.pdf"
    _build_minimal_pdf(src_pdf, text="The quick brown fox jumps over.", title="Quick Brown")

    from gateway.ops.ingest import ingest

    result = ingest(src_pdf)
    assert result.success, result.errors

    # Raw markdown + sidecar PDF live under raw/pdf/
    raw_files = list(paths.raw_dir_for("pdf").glob("pdf-*.md"))
    sidecars = list(paths.raw_dir_for("pdf").glob("pdf-*.pdf"))
    assert len(raw_files) == 1
    assert len(sidecars) == 1

    # Wiki source page exists
    raw_front, _ = fm.parse(raw_files[0].read_text())
    assert paths.wiki_source_path(raw_front["id"]).exists()


# --- pollers ---------------------------------------------------------------


def test_apple_notes_poller_default_run_is_noop(kb_root):
    from gateway.pollers.apple_notes import AppleNotesPoller

    result = AppleNotesPoller().run()
    assert result.success
    assert result.fetched == 0


def test_apple_notes_poller_writes_raw_and_advances_cursor(kb_root, monkeypatch):
    from gateway.pollers.apple_notes import AppleNotesPoller

    poller = AppleNotesPoller()
    monkeypatch.setattr(
        AppleNotesPoller,
        "fetch_notes_since",
        lambda self, cursor: [
            {
                "id": "note-1234",
                "title": "Walk thoughts",
                "body": "Reflection on the morning walk.",
                "modified_at": "2026-04-28T08:00:00Z",
                "folder": "Inbox",
            },
            {
                "id": "note-5678",
                "title": "Reading list",
                "body": "Books to read this quarter.",
                "modified_at": "2026-04-28T09:00:00Z",
                "folder": "Lists",
            },
        ],
    )

    result = poller.run()
    assert result.success
    assert result.fetched == 2

    # Files written under raw/note/
    note_files = list(paths.raw_dir_for("note").glob("*.md"))
    assert len(note_files) == 2

    # Cursor advanced
    cursor_data = poller.read_cursor()
    assert cursor_data["last_modified_iso"] == "2026-04-28T09:00:00Z"


def test_apple_notes_poller_skips_invalid_items(kb_root, monkeypatch):
    from gateway.pollers.apple_notes import AppleNotesPoller

    poller = AppleNotesPoller()
    monkeypatch.setattr(
        AppleNotesPoller,
        "fetch_notes_since",
        lambda self, cursor: [
            {"id": "", "body": "missing id"},
            {"id": "note-x", "body": ""},
            {"id": "note-y", "body": "valid", "modified_at": "2026-04-28T01:00:00Z"},
        ],
    )
    result = poller.run()
    assert result.success
    assert result.fetched == 1
    assert result.skipped == 2
