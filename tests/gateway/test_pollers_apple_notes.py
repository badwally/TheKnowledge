"""Tests for the Apple Notes poller (M34).

osascript / JXA is mocked throughout — these tests do not invoke the real
Notes app. Hand-test on a real Notes account is a separate manual step.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.pollers import apple_notes as ap_mod
from gateway.pollers import get_poller, list_pollers, UnknownPollerError


# --- HTML stripper ---------------------------------------------------------


def test_html_strip_preserves_paragraph_breaks():
    html = "<p>First paragraph.</p><p>Second paragraph.</p>"
    assert ap_mod._strip_html(html) == "First paragraph.\nSecond paragraph."


def test_html_strip_collapses_whitespace_within_paragraphs():
    html = "<p>Hello   <span>world</span>   today</p>"
    assert ap_mod._strip_html(html) == "Hello   world   today"


def test_html_strip_handles_lists_and_breaks():
    html = "<ul><li>One</li><li>Two</li><li>Three</li></ul>"
    assert ap_mod._strip_html(html) == "One\nTwo\nThree"


def test_html_strip_drops_empty_lines():
    html = "<p>Line one.</p><p></p><p>Line two.</p>"
    assert ap_mod._strip_html(html) == "Line one.\nLine two."


def test_html_strip_handles_headings():
    html = "<h1>Title</h1><p>Body text.</p>"
    assert ap_mod._strip_html(html) == "Title\nBody text."


# --- fetch_notes_since (osascript mocked) ----------------------------------


def _mock_jxa_payload(notes: list[dict]) -> str:
    """Return a JSON string the way osascript would output it."""
    return json.dumps(notes)


def test_fetch_notes_since_returns_all_when_cursor_none(monkeypatch):
    payload = _mock_jxa_payload([
        {
            "id": "x-coredata://Notes/1",
            "title": "First note",
            "folder": "Notes",
            "modified": "2026-04-29T01:00:00Z",
            "body": "<p>Hello world</p>",
        },
        {
            "id": "x-coredata://Notes/2",
            "title": "Second note",
            "folder": "Notes",
            "modified": "2026-04-29T02:00:00Z",
            "body": "<p>Another</p>",
        },
    ])
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: payload)

    poller = ap_mod.AppleNotesPoller()
    notes = poller.fetch_notes_since(cursor=None)

    assert len(notes) == 2
    assert notes[0]["body"] == "Hello world"
    assert notes[1]["body"] == "Another"
    assert notes[0]["modified_at"] == "2026-04-29T01:00:00Z"


def test_fetch_notes_since_filters_by_cursor(monkeypatch):
    payload = _mock_jxa_payload([
        {"id": "1", "title": "Old", "folder": "", "modified": "2026-04-28T00:00:00Z", "body": "<p>x</p>"},
        {"id": "2", "title": "New", "folder": "", "modified": "2026-04-29T05:00:00Z", "body": "<p>y</p>"},
    ])
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: payload)

    poller = ap_mod.AppleNotesPoller()
    notes = poller.fetch_notes_since(cursor="2026-04-28T12:00:00Z")

    assert len(notes) == 1
    assert notes[0]["title"] == "New"


def test_fetch_notes_since_handles_empty_payload(monkeypatch):
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: "")
    poller = ap_mod.AppleNotesPoller()
    assert poller.fetch_notes_since(cursor=None) == []


def test_fetch_notes_since_raises_on_invalid_json(monkeypatch):
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: "not json at all")
    poller = ap_mod.AppleNotesPoller()
    with pytest.raises(RuntimeError):
        poller.fetch_notes_since(cursor=None)


# --- run() integration -----------------------------------------------------


def test_run_writes_canonical_markdown_and_advances_cursor(kb_root, monkeypatch):
    payload = _mock_jxa_payload([
        {
            "id": "x-coredata://Notes/abc",
            "title": "Test note one",
            "folder": "Inbox",
            "modified": "2026-04-29T03:00:00Z",
            "body": "<h1>Topic</h1><p>Some body content here.</p>",
        },
    ])
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: payload)

    poller = ap_mod.AppleNotesPoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 1
    assert result.skipped == 0

    # Find the file written under raw/note/
    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-apple-*.md"))
    assert len(files) == 1
    text = files[0].read_text()
    front, body = fm.parse(text)

    assert front["type"] == "note"
    assert front["title"] == "Test note one"
    assert front["meta"]["source_app"] == "apple-notes"
    assert front["meta"]["source_id"] == "x-coredata://Notes/abc"
    assert front["meta"]["folder"] == "Inbox"
    assert front["meta"]["modified_at"] == "2026-04-29T03:00:00Z"
    assert "Topic" in body
    assert "Some body content here." in body

    cursor = poller.read_cursor()
    assert cursor.get("last_modified_iso") == "2026-04-29T03:00:00Z"


def test_run_idempotent_when_no_new_notes_after_cursor(kb_root, monkeypatch):
    """A second run with a cursor at-or-after the latest note returns 0 fetched."""
    payload = _mock_jxa_payload([
        {
            "id": "x-coredata://Notes/abc",
            "title": "Note",
            "folder": "",
            "modified": "2026-04-29T03:00:00Z",
            "body": "<p>Body</p>",
        },
    ])
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: payload)

    poller = ap_mod.AppleNotesPoller()
    poller.run()
    second = poller.run()

    assert second.success is True
    assert second.fetched == 0


def test_run_skips_notes_with_empty_body(kb_root, monkeypatch):
    payload = _mock_jxa_payload([
        {"id": "1", "title": "Has body", "folder": "", "modified": "2026-04-29T01:00:00Z", "body": "<p>x</p>"},
        {"id": "2", "title": "Empty", "folder": "", "modified": "2026-04-29T02:00:00Z", "body": ""},
        {"id": "3", "title": "Whitespace only", "folder": "", "modified": "2026-04-29T03:00:00Z", "body": "<p>   </p>"},
    ])
    monkeypatch.setattr(ap_mod, "_run_osascript", lambda script, **_kw: payload)

    poller = ap_mod.AppleNotesPoller()
    result = poller.run()

    assert result.fetched == 1
    assert result.skipped == 2


def test_run_returns_error_on_osascript_failure(kb_root, monkeypatch):
    def boom(script, **_kw):
        raise RuntimeError("osascript not available; this poller requires macOS")
    monkeypatch.setattr(ap_mod, "_run_osascript", boom)

    poller = ap_mod.AppleNotesPoller()
    result = poller.run()

    assert result.success is False
    assert any("osascript" in e for e in result.errors)


# --- registry --------------------------------------------------------------


def test_list_pollers_includes_apple_notes():
    assert "apple-notes" in list_pollers()


def test_get_poller_returns_apple_notes_instance():
    p = get_poller("apple-notes")
    assert isinstance(p, ap_mod.AppleNotesPoller)
    assert p.name == "apple-notes"
    assert p.source_type == "note"


def test_get_poller_unknown_name_raises():
    with pytest.raises(UnknownPollerError):
        get_poller("does-not-exist")
