"""WS6: wiki answer — local grounded synthesis (stubbed LLM)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.ops.answer import answer, answer_op


@dataclass
class _StubResult:
    text: str
    output_tokens: int = 42
    input_tokens: int = 100
    cache_read_tokens: int = 0


class _StubClient:
    """Records the prompt it was given and returns a canned answer."""

    def __init__(self, reply: str):
        self.reply = reply
        self.calls: list[dict] = []

    def call_with_usage(self, **kwargs):
        self.calls.append(kwargs)
        return _StubResult(text=self.reply)


def _page(slug: str, title: str, body: str, domain: str = "d") -> None:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept", "slug": slug, "title": title, "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def _seed(kb_root: Path) -> None:
    _page(
        "widget", "Widget protocol",
        "## Spec\n\nThe widget protocol uses a 3-way handshake "
        "[[sources/web-2026-01-01-abc]].\n",
    )
    search_index.refresh(rebuild=True)


def test_answer_grounds_on_retrieved_context(kb_root: Path):
    _seed(kb_root)
    client = _StubClient("The widget uses a 3-way handshake [[sources/web-2026-01-01-abc]].")
    res = answer("how does the widget protocol work", domain="d", client=client)
    assert res.answer
    assert "web-2026-01-01-abc" in res.source_ids
    # The context block was sent as the cached prefix.
    assert "WIKI CONTEXT" in client.calls[0]["user_prompt_prefix"]
    assert "widget protocol" in client.calls[0]["user_prompt_prefix"]


def test_answer_strips_confabulated_citations(kb_root: Path):
    _seed(kb_root)
    # Model invents a citation not present in the retrieved context.
    client = _StubClient(
        "Handshake detail [[sources/web-2026-01-01-abc]]. "
        "Invented fact [[sources/fake-99999]]."
    )
    res = answer("widget protocol", domain="d", client=client)
    assert "fake-99999" not in res.answer
    assert "fake-99999" in res.stripped
    assert "web-2026-01-01-abc" in res.answer


def test_answer_no_context_returns_empty(kb_root: Path):
    search_index.refresh(rebuild=True)
    client = _StubClient("should not be called")
    res = answer("nothing matches this query xyzzy", domain="d", client=client)
    assert res.answer == ""
    assert res.sections == []
    assert client.calls == []  # no LLM call when nothing retrieved


def test_answer_op_success(kb_root: Path):
    _seed(kb_root)
    client = _StubClient("Answer [[sources/web-2026-01-01-abc]].")
    result = answer_op("widget protocol", domain="d", client=client, caller="test")
    assert result.success
    assert result.data["source_ids"] == ["web-2026-01-01-abc"]
    assert paths.log_path() in result.paths_touched


def test_answer_op_no_context_fails(kb_root: Path):
    search_index.refresh(rebuild=True)
    client = _StubClient("x")
    result = answer_op("xyzzy nothing", domain="d", client=client)
    assert not result.success
    assert "no wiki context" in result.summary


def test_answer_op_files_draft(kb_root: Path):
    _seed(kb_root)
    client = _StubClient("Grounded answer [[sources/web-2026-01-01-abc]].")
    result = answer_op("widget protocol", domain="d", client=client, file_draft=True)
    assert result.success
    filed = result.data.get("filed_path")
    assert filed and filed.startswith("wiki/synthesis/")
    page = (paths.knowledge_root() / filed)
    assert page.exists()
    front, body = fm.parse(page.read_text())
    assert front["draft"] is True
    assert front["provenance"] == "wiki-answer"
    assert "[[sources/web-2026-01-01-abc]]" in body


def test_mcp_wiki_answer_registered():
    from gateway import mcp_server
    assert hasattr(mcp_server, "wiki_answer")
