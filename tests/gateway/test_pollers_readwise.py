"""Tests for the Readwise poller (INT-9).

All HTTP calls are mocked — no real Readwise API is hit.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.pollers import readwise as rw_mod
from gateway.pollers import get_poller, list_pollers
from gateway.pollers.readwise import ReadwisePoller


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _doc(
    id_: str = "doc-1",
    title: str = "My Article",
    author: str = "Jane Smith",
    category: str = "articles",
    source_url: str | None = "https://example.com/article",
    updated: str = "2026-05-01T10:00:00Z",
    highlights: list[dict] | None = None,
) -> dict:
    if highlights is None:
        highlights = [{"text": "Key insight here.", "note": None, "highlighted_at": "2026-05-01T09:00:00Z"}]
    return {
        "id": id_,
        "title": title,
        "author": author,
        "category": category,
        "source_url": source_url,
        "updated": updated,
        "highlights": highlights,
    }


def _paginated_response(*pages: list[dict]) -> list[dict]:
    """Build a sequence of API response dicts with next URLs."""
    responses = []
    for i, page_docs in enumerate(pages):
        is_last = i == len(pages) - 1
        responses.append({
            "results": page_docs,
            "next": None if is_last else f"https://readwise.io/api/v3/list/?page={i + 2}",
        })
    return responses


def _mock_get(responses: list[dict]):
    """Return a callable that replaces requests.get, cycling through responses."""
    call_count = 0

    class _MockResponse:
        def __init__(self, data):
            self._data = data
            self.status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return self._data

    def _get(url, **_kwargs):
        nonlocal call_count
        resp = responses[min(call_count, len(responses) - 1)]
        call_count += 1
        return _MockResponse(resp)

    return _get


# ---------------------------------------------------------------------------
# new document written correctly
# ---------------------------------------------------------------------------


def test_new_document_written_to_raw_note(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    doc = _doc()
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response([doc])))

    poller = ReadwisePoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 1

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-readwise-doc-1.md"))
    assert len(files) == 1
    front, body = fm.parse(files[0].read_text())

    assert front["type"] == "note"
    assert front["id"] == "note-readwise-doc-1"
    assert front["title"] == "My Article"
    assert front["authors"] == ["Jane Smith"]
    assert front["url"] == "https://example.com/article"
    assert front["meta"]["source_app"] == "readwise"
    assert front["meta"]["readwise_id"] == "doc-1"
    assert front["meta"]["readwise_category"] == "articles"
    assert front["meta"]["source_url"] == "https://example.com/article"

    assert "## Highlights" in body
    assert "Key insight here." in body


def test_source_app_is_readwise_on_every_output(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    docs = [_doc(id_="d1", title="A"), _doc(id_="d2", title="B")]
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response(docs)))

    poller = ReadwisePoller()
    poller.run()

    note_dir = paths.raw_dir_for("note")
    for f in note_dir.glob("note-readwise-*.md"):
        front, _ = fm.parse(f.read_text())
        assert front["meta"]["source_app"] == "readwise"


def test_highlight_with_note_renders_inline(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    doc = _doc(highlights=[
        {"text": "Important quote.", "note": "My annotation.", "highlighted_at": "2026-05-01T09:00:00Z"},
    ])
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response([doc])))

    poller = ReadwisePoller()
    poller.run()

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-readwise-doc-1.md"))
    _, body = fm.parse(files[0].read_text())
    assert "Important quote." in body
    assert "My annotation." in body


def test_null_source_url_becomes_empty_string(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    doc = _doc(source_url=None)
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response([doc])))

    poller = ReadwisePoller()
    poller.run()

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-readwise-doc-1.md"))
    front, _ = fm.parse(files[0].read_text())
    assert front["url"] == ""
    assert front["meta"]["source_url"] == ""


# ---------------------------------------------------------------------------
# idempotency — re-run with same document updates highlights, no duplicate
# ---------------------------------------------------------------------------


def test_rerun_same_document_updates_not_duplicates(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    doc = _doc(highlights=[{"text": "Original highlight.", "note": None, "highlighted_at": "2026-05-01T09:00:00Z"}])
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response([doc])))

    poller = ReadwisePoller()
    poller.run()

    # Second run: same doc, new highlight
    updated_doc = _doc(highlights=[
        {"text": "Original highlight.", "note": None, "highlighted_at": "2026-05-01T09:00:00Z"},
        {"text": "New highlight added.", "note": None, "highlighted_at": "2026-05-02T09:00:00Z"},
    ], updated="2026-05-02T10:00:00Z")
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response([updated_doc])))
    poller.run()

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-readwise-doc-1.md"))
    assert len(files) == 1  # not duplicated

    _, body = fm.parse(files[0].read_text())
    # Should have both highlights, not doubled
    assert body.count("Original highlight.") == 1
    assert "New highlight added." in body


# ---------------------------------------------------------------------------
# cursor advances to max(updated) after successful batch
# ---------------------------------------------------------------------------


def test_cursor_advances_to_max_updated(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    docs = [
        _doc(id_="d1", updated="2026-05-01T10:00:00Z"),
        _doc(id_="d2", updated="2026-05-03T10:00:00Z"),
        _doc(id_="d3", updated="2026-05-02T10:00:00Z"),
    ]
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response(docs)))

    poller = ReadwisePoller()
    poller.run()

    cursor = poller.read_cursor()
    assert cursor["last_updated_after"] == "2026-05-03T10:00:00Z"


def test_cursor_unchanged_on_empty_response(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    monkeypatch.setattr(rw_mod.requests, "get", _mock_get(_paginated_response([])))

    poller = ReadwisePoller()
    poller.run()

    cursor = poller.read_cursor()
    assert cursor.get("last_updated_after") == "2020-01-01T00:00:00Z"


# ---------------------------------------------------------------------------
# missing token → failure
# ---------------------------------------------------------------------------


def test_missing_token_returns_failure(kb_root, monkeypatch):
    monkeypatch.delenv("READWISE_TOKEN", raising=False)

    poller = ReadwisePoller()
    result = poller.run()

    assert result.success is False
    assert any("READWISE_TOKEN" in e for e in result.errors)


# ---------------------------------------------------------------------------
# pagination — follows next URL until null
# ---------------------------------------------------------------------------


def test_pagination_follows_next_until_null(kb_root, monkeypatch):
    monkeypatch.setenv("READWISE_TOKEN", "tok-abc")
    page1 = [_doc(id_="p1-doc1"), _doc(id_="p1-doc2")]
    page2 = [_doc(id_="p2-doc1")]
    responses = _paginated_response(page1, page2)

    call_log: list[str] = []

    class _MockResponse:
        def __init__(self, data):
            self._data = data

        def raise_for_status(self):
            pass

        def json(self):
            return self._data

    call_idx = 0

    def _get(url, **_kwargs):
        nonlocal call_idx
        call_log.append(url)
        resp = responses[min(call_idx, len(responses) - 1)]
        call_idx += 1
        return _MockResponse(resp)

    monkeypatch.setattr(rw_mod.requests, "get", _get)

    poller = ReadwisePoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 3
    assert len(call_log) == 2  # two HTTP calls


# ---------------------------------------------------------------------------
# registry
# ---------------------------------------------------------------------------


def test_registered_under_readwise():
    assert "readwise" in list_pollers()


def test_get_poller_returns_readwise_instance():
    p = get_poller("readwise")
    assert isinstance(p, ReadwisePoller)
    assert p.name == "readwise"
    assert p.source_type == "note"
