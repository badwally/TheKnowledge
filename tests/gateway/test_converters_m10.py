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


def test_arxiv_extract_id_handles_bare_and_shorthand_forms():
    # bare new-style IDs
    assert arxiv_mod.extract_arxiv_id("2403.12345") == "2403.12345"
    assert arxiv_mod.extract_arxiv_id("2403.12345v2") == "2403.12345"
    # arxiv: shorthand
    assert arxiv_mod.extract_arxiv_id("arxiv:2403.12345") == "2403.12345"
    assert arxiv_mod.extract_arxiv_id("arxiv:2403.12345v2") == "2403.12345"
    # old-style IDs (pre-2007)
    assert arxiv_mod.extract_arxiv_id("cond-mat/0207270") == "cond-mat/0207270"
    assert arxiv_mod.extract_arxiv_id("cond-mat/0207270v1") == "cond-mat/0207270"
    assert arxiv_mod.extract_arxiv_id("https://arxiv.org/abs/cond-mat/0207270") == "cond-mat/0207270"
    # negatives
    assert arxiv_mod.extract_arxiv_id("not an id") is None
    assert arxiv_mod.extract_arxiv_id("12345") is None
    assert arxiv_mod.extract_arxiv_id("") is None


def test_arxiv_detect():
    c = arxiv_mod.ArxivConverter()
    assert c.detect("https://arxiv.org/abs/2403.12345")
    assert not c.detect("https://arxiv.org/list/cs.LG/2024")
    assert not c.detect("/local/file.md")


def test_arxiv_detect_accepts_bare_and_shorthand_forms():
    c = arxiv_mod.ArxivConverter()
    assert c.detect("2403.12345")
    assert c.detect("2403.12345v2")
    assert c.detect("arxiv:2403.12345")
    assert c.detect("cond-mat/0207270")
    assert c.detect("https://arxiv.org/abs/cond-mat/0207270")
    # negatives — must not swallow non-arxiv strings
    assert not c.detect("not an id")
    assert not c.detect("https://example.com/foo")
    assert not c.detect("/some/local/file.txt")
    assert not c.detect("12345")


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


def test_arxiv_convert_captures_extension_metadata(monkeypatch):
    """primary_category, journal_ref, comment from the Atom arxiv: namespace
    are written to front[meta]."""
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T",
        "abstract": "Abstract body.",
        "published_at": "2024-04-02",
        "authors": ["J. Liu"],
        "categories": ["q-bio.NC", "q-bio.QM"],
        "doi": "10.1234/x",
        "primary_category": "q-bio.NC",
        "journal_ref": "Nature Neuroscience 2024",
        "comment": "10 pages, 4 figures",
    })

    text = arxiv_mod.ArxivConverter().convert("2403.12345")
    front, _ = fm.parse(text)
    assert front["meta"]["primary_category"] == "q-bio.NC"
    assert front["meta"]["journal_ref"] == "Nature Neuroscience 2024"
    assert front["meta"]["comment"] == "10 pages, 4 figures"


def test_arxiv_fetch_metadata_parses_extension_elements(monkeypatch):
    """The real _fetch_metadata extracts arxiv: namespace fields from the Atom feed."""
    sample_atom = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2403.12345v1</id>
    <title>Sample title</title>
    <summary>Sample abstract.</summary>
    <published>2024-04-02T00:00:00Z</published>
    <author><name>J. Liu</name></author>
    <category term="q-bio.NC"/>
    <arxiv:primary_category term="q-bio.NC"/>
    <arxiv:doi>10.1234/x</arxiv:doi>
    <arxiv:journal_ref>Nature Neuroscience 2024</arxiv:journal_ref>
    <arxiv:comment>10 pages, 4 figures</arxiv:comment>
  </entry>
</feed>
"""

    class _FakeResponse:
        status_code = 200
        text = sample_atom

    monkeypatch.setattr(arxiv_mod.requests, "get", lambda *a, **kw: _FakeResponse())
    arxiv_mod._reset_rate_limit_for_tests()

    meta = arxiv_mod._fetch_metadata("2403.12345")
    assert meta["primary_category"] == "q-bio.NC"
    assert meta["journal_ref"] == "Nature Neuroscience 2024"
    assert meta["comment"] == "10 pages, 4 figures"
    assert meta["doi"] == "10.1234/x"


def test_arxiv_rate_limit_sleeps_between_calls(monkeypatch):
    """Two _fetch_metadata calls within the rate window force a sleep on the second.

    Mocks time.monotonic so the test is deterministic and instant.
    """
    sleeps: list[float] = []
    times: list[float] = [100.0]
    monkeypatch.setattr(arxiv_mod.time, "sleep", lambda s: sleeps.append(s))
    monkeypatch.setattr(arxiv_mod.time, "monotonic", lambda: times[0])

    class _FakeResponse:
        status_code = 200
        text = (
            '<?xml version="1.0"?>'
            '<feed xmlns="http://www.w3.org/2005/Atom">'
            '<entry><id>http://arxiv.org/abs/x</id><title>t</title>'
            '<summary>s</summary></entry></feed>'
        )

    monkeypatch.setattr(arxiv_mod.requests, "get", lambda *a, **kw: _FakeResponse())
    arxiv_mod._reset_rate_limit_for_tests()

    arxiv_mod._fetch_metadata("2403.12345")
    times[0] = 100.5  # only 0.5s has elapsed
    arxiv_mod._fetch_metadata("2404.99999")

    # First call: no prior request, no sleep. Second call: must sleep ~2.5s.
    assert sleeps, "expected at least one sleep on the second call"
    assert sleeps[-1] >= 2.4, f"expected ~2.5s sleep, got {sleeps[-1]}"


def test_arxiv_rate_limit_no_sleep_when_window_elapsed(monkeypatch):
    """If 3+ seconds have elapsed since last call, no sleep is needed."""
    sleeps: list[float] = []
    times: list[float] = [100.0]
    monkeypatch.setattr(arxiv_mod.time, "sleep", lambda s: sleeps.append(s))
    monkeypatch.setattr(arxiv_mod.time, "monotonic", lambda: times[0])

    class _FakeResponse:
        status_code = 200
        text = (
            '<?xml version="1.0"?>'
            '<feed xmlns="http://www.w3.org/2005/Atom">'
            '<entry><id>http://arxiv.org/abs/x</id><title>t</title>'
            '<summary>s</summary></entry></feed>'
        )

    monkeypatch.setattr(arxiv_mod.requests, "get", lambda *a, **kw: _FakeResponse())
    arxiv_mod._reset_rate_limit_for_tests()

    arxiv_mod._fetch_metadata("2403.12345")
    times[0] = 105.0  # 5s elapsed — well past the 3s window
    arxiv_mod._fetch_metadata("2404.99999")

    assert sleeps == [], f"expected no sleeps, got {sleeps}"


def test_arxiv_convert_no_abstract_raises(monkeypatch):
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "", "published_at": "", "authors": [], "categories": [], "doi": "",
    })
    with pytest.raises(ConversionError):
        arxiv_mod.ArxivConverter().convert("https://arxiv.org/abs/2403.12345")


def test_arxiv_convert_with_pdf_extracts_full_text(kb_root, monkeypatch):
    """convert_with_pdf downloads the PDF, extracts full text, saves sidecar.

    Mocks _download_pdf to drop a synthesized one-page PDF at the target path,
    so pdfplumber gets real bytes to extract.
    """
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "Quantum Foo",
        "abstract": "This is the abstract.",
        "published_at": "2024-04-02",
        "authors": ["J. Liu"],
        "categories": ["q-bio.NC"],
        "doi": "10.1234/x",
        "primary_category": "q-bio.NC",
        "journal_ref": "",
        "comment": "",
    })

    def _fake_download(arxiv_id, target):
        _build_minimal_pdf(target, text="Full paper body text here.")

    monkeypatch.setattr(arxiv_mod, "_download_pdf", _fake_download)
    arxiv_mod._reset_rate_limit_for_tests()

    text = arxiv_mod.ArxivConverter().convert_with_pdf("2403.12345")
    front, body = fm.parse(text)

    assert front["id"] == "arxiv-2403.12345"
    assert front["type"] == "arxiv"
    assert front["meta"]["arxiv_id"] == "2403.12345"
    assert front["meta"]["abstract_only"] is False
    assert front["meta"]["primary_category"] == "q-bio.NC"
    assert "Full paper body text here." in body
    # abstract should NOT be the body when in PDF mode
    assert "This is the abstract." not in body

    # Sidecar PDF lives at raw/arxiv/<id>.pdf
    sidecar = paths.raw_dir_for("arxiv") / "arxiv-2403.12345.pdf"
    assert sidecar.exists()
    assert front["source_path"] == "raw/arxiv/arxiv-2403.12345.pdf"


def test_arxiv_convert_with_pdf_download_http_failure_raises(kb_root, monkeypatch):
    """A non-200 from arxiv.org/pdf surfaces as ConversionError."""
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "A.", "published_at": "",
        "authors": [], "categories": [], "doi": "",
        "primary_category": "", "journal_ref": "", "comment": "",
    })

    class _NotFound:
        status_code = 404
        content = b""

    # Patch the lower-level requests.get inside _download_pdf
    monkeypatch.setattr(arxiv_mod.requests, "get", lambda *a, **kw: _NotFound())
    arxiv_mod._reset_rate_limit_for_tests()

    with pytest.raises(ConversionError, match="404"):
        arxiv_mod.ArxivConverter().convert_with_pdf("2403.12345")


def test_arxiv_convert_with_pdf_empty_extraction_raises(kb_root, monkeypatch, tmp_path):
    """If the downloaded PDF yields no extractable text, raise ConversionError."""
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "A.", "published_at": "",
        "authors": [], "categories": [], "doi": "",
        "primary_category": "", "journal_ref": "", "comment": "",
    })

    def _fake_download(arxiv_id, target):
        # Write a minimal but text-empty "PDF" — pdfplumber will return empty body
        target.write_bytes(b"%PDF-1.4\n%%EOF\n")

    monkeypatch.setattr(arxiv_mod, "_download_pdf", _fake_download)
    # Stub _extract_pdf to deterministically return empty body
    from gateway.converters import pdf as pdf_mod
    monkeypatch.setattr(pdf_mod, "_extract_pdf", lambda p: ("", {}))
    arxiv_mod._reset_rate_limit_for_tests()

    with pytest.raises(ConversionError, match="no extractable text"):
        arxiv_mod.ArxivConverter().convert_with_pdf("2403.12345")


def test_arxiv_convert_with_pdf_old_style_id_sanitizes_slashes(kb_root, monkeypatch):
    """Old-style ids like cond-mat/0207270 must produce a slash-free filename."""
    monkeypatch.setattr(arxiv_mod, "_fetch_metadata", lambda aid: {
        "title": "T", "abstract": "A.", "published_at": "",
        "authors": [], "categories": [], "doi": "",
        "primary_category": "", "journal_ref": "", "comment": "",
    })

    def _fake_download(arxiv_id, target):
        _build_minimal_pdf(target, text="Old-style PDF body.")

    monkeypatch.setattr(arxiv_mod, "_download_pdf", _fake_download)
    arxiv_mod._reset_rate_limit_for_tests()

    text = arxiv_mod.ArxivConverter().convert_with_pdf("cond-mat/0207270")
    front, _ = fm.parse(text)

    assert front["id"] == "arxiv-cond-mat-0207270"
    assert front["meta"]["arxiv_id"] == "cond-mat/0207270"  # original preserved
    sidecar = paths.raw_dir_for("arxiv") / "arxiv-cond-mat-0207270.pdf"
    assert sidecar.exists()


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


def test_apple_notes_poller_run_is_noop_when_osascript_returns_empty(kb_root, monkeypatch):
    """With no notes from Notes.app, run() succeeds with 0 fetched.

    M34 wired a real JXA adapter behind `_run_osascript`. We mock it here
    so the test doesn't invoke the real Notes app or require Automation
    permission.
    """
    from gateway.pollers import apple_notes as ap_mod

    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: "[]")

    result = ap_mod.AppleNotesPoller().run()
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
