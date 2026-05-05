"""Tests for `gateway.research.session`.

Covers session-id derivation, dedup-by-URL promotion, and abandon. The
NotebookLM CLI is mocked at the same layer `source_map` mocks it
(`subprocess.run` inside `gateway.research.source_map`).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

import pytest

from gateway.research import session as _session
from gateway.research import source_map as sm


# --- mock NlmClient --------------------------------------------------------


@dataclass
class _RecordingClient:
    """Records source_add_* calls; nothing else implemented."""

    add_url_calls: list[tuple[str, str]] = field(default_factory=list)
    add_text_calls: list[tuple[str, str, str | None]] = field(default_factory=list)

    def source_add_url(self, notebook_id: str, url: str) -> None:
        self.add_url_calls.append((notebook_id, url))

    def source_add_text(
        self, notebook_id: str, content: str, *, title: str | None = None
    ) -> None:
        self.add_text_calls.append((notebook_id, content, title))


# --- registry stub ---------------------------------------------------------


@dataclass
class _RegistryStub:
    promoted: list[tuple[str, str, int]] = field(default_factory=list)
    abandoned: list[tuple[str, str]] = field(default_factory=list)

    def mark_promoted(
        self, domain: str, session_id: str, *, sources_added: int
    ) -> None:
        self.promoted.append((domain, session_id, sources_added))

    def mark_abandoned(self, domain: str, session_id: str) -> None:
        self.abandoned.append((domain, session_id))


# --- subprocess stub for source_map.fetch_nlm_sources -----------------------


class _FakeCompleted:
    def __init__(self, *, stdout: str = "", stderr: str = "", returncode: int = 0):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


def _patch_fetch(
    monkeypatch: pytest.MonkeyPatch,
    *,
    by_notebook: dict[str, list[dict]],
) -> None:
    """Patch `subprocess.run` in source_map to dispatch by notebook id."""

    def fake_run(args, **kwargs):
        # args = ["nlm", "source", "list", <id>, "--json"]
        nb_id = args[3]
        sources = by_notebook.get(nb_id, [])
        return _FakeCompleted(stdout=json.dumps(sources))

    monkeypatch.setattr(sm.subprocess, "run", fake_run)


# --- make_session_id -------------------------------------------------------


def test_make_session_id_basic():
    sid = _session.make_session_id("GLP-1 cardiovascular outcomes", today="2026-04-29")
    assert sid == "2026-04-29-glp-1-cardiovascular-outcomes"


def test_make_session_id_caps_six_words():
    sid = _session.make_session_id(
        "one two three four five six seven eight", today="2026-01-01"
    )
    assert sid == "2026-01-01-one-two-three-four-five-six"


def test_make_session_id_strips_punctuation():
    sid = _session.make_session_id("foo!!! BAR??? baz...", today="2026-04-29")
    assert sid == "2026-04-29-foo-bar-baz"


def test_make_session_id_empty_prompt_falls_back():
    sid = _session.make_session_id("???", today="2026-04-29")
    assert sid == "2026-04-29-query"


def test_make_session_id_uses_today_when_unspecified(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(_session, "_DEFAULT_DATE_FN", lambda: "2030-12-31")
    sid = _session.make_session_id("hello world")
    assert sid.startswith("2030-12-31-")


# --- promote ---------------------------------------------------------------


def test_promote_dedups_by_url(monkeypatch: pytest.MonkeyPatch):
    # Persistent already has one URL; session has it plus one new one.
    _patch_fetch(
        monkeypatch,
        by_notebook={
            "nb-session": [
                {"id": "s1", "url": "https://a.example/", "title": "A"},
                {"id": "s2", "url": "https://b.example/", "title": "B"},
            ],
            "nb-persistent": [
                {"id": "p1", "url": "https://a.example/", "title": "A"},
            ],
        },
    )

    client = _RecordingClient()
    registry = _RegistryStub()

    added = _session.promote(
        "alpha",
        "2026-04-29-x",
        persistent_notebook_id="nb-persistent",
        session_notebook_id="nb-session",
        client=client,
        nlm_registry=registry,
    )

    assert added == 1
    # Only the new URL was added.
    assert client.add_url_calls == [("nb-persistent", "https://b.example/")]
    assert registry.promoted == [("alpha", "2026-04-29-x", 1)]


def test_promote_falls_back_to_text_when_no_url(monkeypatch: pytest.MonkeyPatch):
    _patch_fetch(
        monkeypatch,
        by_notebook={
            "nb-session": [
                # No URL — should route to source_add_text by title.
                {"id": "s1", "title": "Note one"},
                {"id": "s2", "title": "Note two"},
            ],
            "nb-persistent": [
                {"id": "p1", "title": "Note one"},  # already there
            ],
        },
    )

    client = _RecordingClient()
    registry = _RegistryStub()

    added = _session.promote(
        "alpha",
        "sess-1",
        persistent_notebook_id="nb-persistent",
        session_notebook_id="nb-session",
        client=client,
        nlm_registry=registry,
    )

    assert added == 1
    # Note two routed via text; Note one was deduped.
    assert client.add_url_calls == []
    assert client.add_text_calls == [("nb-persistent", "", "Note two")]


def test_promote_records_correct_sources_added_count(
    monkeypatch: pytest.MonkeyPatch,
):
    _patch_fetch(
        monkeypatch,
        by_notebook={
            "nb-session": [
                {"id": "s1", "url": "https://x.example/"},
                {"id": "s2", "url": "https://y.example/"},
                {"id": "s3", "url": "https://z.example/"},
            ],
            "nb-persistent": [],
        },
    )
    client = _RecordingClient()
    registry = _RegistryStub()

    added = _session.promote(
        "d1",
        "sess-2",
        persistent_notebook_id="nb-persistent",
        session_notebook_id="nb-session",
        client=client,
        nlm_registry=registry,
    )

    assert added == 3
    assert registry.promoted == [("d1", "sess-2", 3)]


def test_promote_empty_session_does_nothing(monkeypatch: pytest.MonkeyPatch):
    _patch_fetch(
        monkeypatch,
        by_notebook={
            "nb-session": [],
            "nb-persistent": [{"id": "p1", "url": "https://kept/"}],
        },
    )
    client = _RecordingClient()
    registry = _RegistryStub()

    added = _session.promote(
        "d1",
        "sess-3",
        persistent_notebook_id="nb-persistent",
        session_notebook_id="nb-session",
        client=client,
        nlm_registry=registry,
    )
    assert added == 0
    assert client.add_url_calls == []
    assert registry.promoted == [("d1", "sess-3", 0)]


# --- abandon ---------------------------------------------------------------


def test_abandon_marks_registry():
    registry = _RegistryStub()
    _session.abandon("alpha", "sess-x", nlm_registry=registry)
    assert registry.abandoned == [("alpha", "sess-x")]
