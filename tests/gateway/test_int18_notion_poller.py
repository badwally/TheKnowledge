"""INT-18: Notion source poller tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from gateway import frontmatter as fm, paths, validator
from gateway.notion_client import NotionClient
from gateway.pollers.notion import (
    NotionSourcePoller,
    _build_note_id,
    _extract_title,
    _is_newer,
    _page_id_clean,
    _render_raw,
)


# --- NotionClient static helpers --------------------------------------------


class TestNotionClientBlocksToMarkdown:
    def test_paragraph(self):
        blocks = [{"type": "paragraph", "paragraph": {"rich_text": [{"plain_text": "Hello world", "annotations": {}}]}}]
        assert "Hello world" in NotionClient.blocks_to_markdown(blocks)

    def test_heading_levels(self):
        for level in (1, 2, 3):
            blocks = [{"type": f"heading_{level}", f"heading_{level}": {"rich_text": [{"plain_text": "Title", "annotations": {}}]}}]
            md = NotionClient.blocks_to_markdown(blocks)
            assert md.startswith("#" * level + " Title")

    def test_bulleted_list(self):
        blocks = [{"type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"plain_text": "item", "annotations": {}}]}}]
        assert "- item" in NotionClient.blocks_to_markdown(blocks)

    def test_numbered_list(self):
        blocks = [{"type": "numbered_list_item", "numbered_list_item": {"rich_text": [{"plain_text": "item", "annotations": {}}]}}]
        assert "1. item" in NotionClient.blocks_to_markdown(blocks)

    def test_to_do_unchecked(self):
        blocks = [{"type": "to_do", "to_do": {"rich_text": [{"plain_text": "task", "annotations": {}}], "checked": False}}]
        assert "- [ ] task" in NotionClient.blocks_to_markdown(blocks)

    def test_to_do_checked(self):
        blocks = [{"type": "to_do", "to_do": {"rich_text": [{"plain_text": "done", "annotations": {}}], "checked": True}}]
        assert "- [x] done" in NotionClient.blocks_to_markdown(blocks)

    def test_code_block(self):
        blocks = [{"type": "code", "code": {"rich_text": [{"plain_text": "x = 1", "annotations": {}}], "language": "python"}}]
        md = NotionClient.blocks_to_markdown(blocks)
        assert "```python" in md
        assert "x = 1" in md

    def test_quote(self):
        blocks = [{"type": "quote", "quote": {"rich_text": [{"plain_text": "wisdom", "annotations": {}}]}}]
        assert "> wisdom" in NotionClient.blocks_to_markdown(blocks)

    def test_divider(self):
        blocks = [{"type": "divider", "divider": {}}]
        assert "---" in NotionClient.blocks_to_markdown(blocks)

    def test_image_external(self):
        blocks = [{"type": "image", "image": {"external": {"url": "https://example.com/img.png"}, "caption": []}}]
        md = NotionClient.blocks_to_markdown(blocks)
        assert "https://example.com/img.png" in md

    def test_bookmark(self):
        blocks = [{"type": "bookmark", "bookmark": {"url": "https://example.com", "caption": []}}]
        md = NotionClient.blocks_to_markdown(blocks)
        assert "https://example.com" in md

    def test_unknown_block_skipped(self):
        blocks = [{"type": "unsupported_type", "unsupported_type": {}}]
        assert NotionClient.blocks_to_markdown(blocks) == ""

    def test_empty_blocks(self):
        assert NotionClient.blocks_to_markdown([]) == ""


class TestRichTextToMarkdown:
    def test_bold(self):
        rt = [{"plain_text": "bold", "annotations": {"bold": True}, "href": None}]
        assert "**bold**" in NotionClient._rich_text_to_md(rt)

    def test_italic(self):
        rt = [{"plain_text": "em", "annotations": {"italic": True}, "href": None}]
        assert "*em*" in NotionClient._rich_text_to_md(rt)

    def test_strikethrough(self):
        rt = [{"plain_text": "del", "annotations": {"strikethrough": True}, "href": None}]
        assert "~~del~~" in NotionClient._rich_text_to_md(rt)

    def test_code_inline(self):
        rt = [{"plain_text": "var", "annotations": {"code": True}, "href": None}]
        assert "`var`" in NotionClient._rich_text_to_md(rt)

    def test_link(self):
        rt = [{"plain_text": "click", "annotations": {}, "href": "https://example.com"}]
        md = NotionClient._rich_text_to_md(rt)
        assert "[click](https://example.com)" in md

    def test_plain_text(self):
        rt = [{"plain_text": "hello", "annotations": {}, "href": None}]
        assert NotionClient._rich_text_to_md(rt) == "hello"

    def test_empty(self):
        assert NotionClient._rich_text_to_md([]) == ""


# --- poller helpers ---------------------------------------------------------


def test_page_id_clean():
    assert _page_id_clean("abc-123-def") == "abc123def"
    assert _page_id_clean("abc123") == "abc123"


def test_build_note_id():
    nid = _build_note_id("abc123def456")
    assert nid.startswith("note-notion-")
    assert len(nid) == len("note-notion-") + 12


def test_build_note_id_stable():
    assert _build_note_id("abc123") == _build_note_id("abc123")


def test_build_note_id_different():
    assert _build_note_id("page_a") != _build_note_id("page_b")


def test_extract_title():
    page = {
        "properties": {
            "Name": {
                "type": "title",
                "title": [{"plain_text": "My Page"}],
            }
        }
    }
    assert _extract_title(page) == "My Page"


def test_extract_title_untitled():
    assert _extract_title({"properties": {}}) == "Untitled"


def test_is_newer():
    assert _is_newer("2026-05-02T00:00:00Z", "2026-05-01T00:00:00Z")
    assert not _is_newer("2026-05-01T00:00:00Z", "2026-05-01T00:00:00Z")
    assert _is_newer("anything", "")  # empty cursor → always newer


# --- _render_raw ------------------------------------------------------------


def test_render_raw_valid_frontmatter(kb_root: Path):
    raw = _render_raw(
        note_id="note-notion-abc123def456",
        title="Test Page",
        url="https://notion.so/abc",
        source_app="notion",
        domain="research",
        edited_at="2026-05-26T10:00:00Z",
        body_md="Some content.",
    )
    front, body = fm.parse(raw)
    result = validator.validate_source_frontmatter(front)
    assert not result.errors, result.errors
    assert front["type"] == "note"
    assert front["source_app"] == "notion"
    assert front["domains"] == ["research"]
    assert "Some content." in body


def test_render_raw_no_domain(kb_root: Path):
    raw = _render_raw(
        note_id="note-notion-abc123def456",
        title="No Domain",
        url="",
        source_app="notion",
        domain="",
        edited_at="2026-05-26T10:00:00Z",
        body_md="",
    )
    front, _ = fm.parse(raw)
    assert "domains" not in front


# --- poller run() -----------------------------------------------------------


def _make_stub_client(
    *,
    pages: dict[str, tuple[dict, list]] | None = None,
    db_pages: dict[str, list[dict]] | None = None,
    db_page_blocks: dict[str, list] | None = None,
    get_page_raises: Exception | None = None,
    get_blocks_raises: Exception | None = None,
    query_db_raises: Exception | None = None,
) -> "StubNotionClient":
    return StubNotionClient(
        pages=pages or {},
        db_pages=db_pages or {},
        db_page_blocks=db_page_blocks or {},
        get_page_raises=get_page_raises,
        get_blocks_raises=get_blocks_raises,
        query_db_raises=query_db_raises,
    )


class StubNotionClient:
    def __init__(
        self,
        pages: dict,
        db_pages: dict,
        db_page_blocks: dict,
        get_page_raises=None,
        get_blocks_raises=None,
        query_db_raises=None,
    ):
        self._pages = pages
        self._db_pages = db_pages
        self._db_page_blocks = db_page_blocks
        self._get_page_raises = get_page_raises
        self._get_blocks_raises = get_blocks_raises
        self._query_db_raises = query_db_raises

    def get_page(self, page_id: str) -> dict:
        if self._get_page_raises:
            raise self._get_page_raises
        meta, _ = self._pages.get(page_id, ({}, []))
        return meta

    def get_page_blocks(self, page_id: str) -> list:
        if self._get_blocks_raises:
            raise self._get_blocks_raises
        if page_id in self._pages:
            _, blocks = self._pages[page_id]
            return blocks
        return self._db_page_blocks.get(page_id, [])

    def query_database(self, db_id: str, filter_body=None) -> list:
        if self._query_db_raises:
            raise self._query_db_raises
        return self._db_pages.get(db_id, [])


def _make_notion_page(page_id: str, title: str, edited: str = "2026-05-26T10:00:00Z") -> dict:
    return {
        "id": page_id,
        "last_edited_time": edited,
        "url": f"https://notion.so/{page_id}",
        "properties": {
            "Name": {"type": "title", "title": [{"plain_text": title}]}
        },
    }


def _make_text_block(text: str) -> dict:
    return {
        "type": "paragraph",
        "paragraph": {"rich_text": [{"plain_text": text, "annotations": {}}]},
    }


def test_run_no_token(kb_root: Path):
    poller = NotionSourcePoller()
    import os
    env_backup = os.environ.pop("NOTION_TOKEN", None)
    try:
        result = poller.run()
        assert not result.success
        assert "NOTION_TOKEN" in result.errors[0]
    finally:
        if env_backup is not None:
            os.environ["NOTION_TOKEN"] = env_backup


def test_run_empty_config(kb_root: Path):
    poller = NotionSourcePoller()
    client = _make_stub_client()
    result = poller.run(client=client)
    assert result.success
    assert result.fetched == 0


def test_run_single_page(kb_root: Path):
    page_id = "abc123def456"
    config = {"pages": [{"page_id": page_id, "domain": "research"}], "databases": []}
    poller = NotionSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(
        __import__("yaml").safe_dump(config)
    )
    page_meta = _make_notion_page(page_id, "My Research Note")
    blocks = [_make_text_block("Key finding here.")]
    client = _make_stub_client(pages={page_id: (page_meta, blocks)})
    result = poller.run(client=client)
    assert result.success
    assert result.fetched == 1
    note_id = _build_note_id(page_id)
    raw_path = paths.raw_source_path("note", note_id)
    assert raw_path.exists()
    front, body = fm.parse(raw_path.read_text())
    assert front["type"] == "note"
    assert front["source_app"] == "notion"
    assert "Key finding here." in body


def test_run_cursor_skips_unchanged(kb_root: Path):
    page_id = "page001"
    edited = "2026-05-26T10:00:00Z"
    config = {"pages": [{"page_id": page_id, "domain": ""}], "databases": []}
    poller = NotionSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(__import__("yaml").safe_dump(config))
    poller.write_cursor({"pages": {page_id: edited}, "databases": {}})
    page_meta = _make_notion_page(page_id, "Old Note", edited=edited)
    client = _make_stub_client(pages={page_id: (page_meta, [])})
    result = poller.run(client=client)
    assert result.fetched == 0
    assert result.skipped == 1


def test_run_cursor_written(kb_root: Path):
    page_id = "page002"
    config = {"pages": [{"page_id": page_id, "domain": ""}], "databases": []}
    poller = NotionSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(__import__("yaml").safe_dump(config))
    page_meta = _make_notion_page(page_id, "New Note", edited="2026-05-26T11:00:00Z")
    client = _make_stub_client(pages={page_id: (page_meta, [_make_text_block("content")])})
    poller.run(client=client)
    cursor = poller.read_cursor()
    assert cursor["pages"][page_id] == "2026-05-26T11:00:00Z"


def test_run_database_pages(kb_root: Path):
    db_id = "dbXYZ"
    page_id = "p001"
    config = {"pages": [], "databases": [{"database_id": db_id, "domain": "tech"}]}
    poller = NotionSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(__import__("yaml").safe_dump(config))
    db_page_meta = _make_notion_page(page_id, "DB Page")
    client = _make_stub_client(
        db_pages={db_id: [db_page_meta]},
        db_page_blocks={page_id: [_make_text_block("DB content")]},
    )
    result = poller.run(client=client)
    assert result.fetched == 1
    note_id = _build_note_id(page_id)
    assert paths.raw_source_path("note", note_id).exists()


def test_run_get_page_error(kb_root: Path):
    page_id = "bad_page"
    config = {"pages": [{"page_id": page_id, "domain": ""}], "databases": []}
    poller = NotionSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(__import__("yaml").safe_dump(config))
    from gateway.notion_client import NotionError
    client = _make_stub_client(get_page_raises=NotionError("403 Forbidden"))
    result = poller.run(client=client)
    assert len(result.errors) > 0
    assert result.fetched == 0


def test_run_max_pages_limit(kb_root: Path):
    pages = {f"page{i:03d}": (_make_notion_page(f"page{i:03d}", f"Page {i}"), [_make_text_block("x")]) for i in range(5)}
    config = {
        "pages": [{"page_id": pid, "domain": ""} for pid in pages],
        "databases": [],
        "max_pages": 3,
    }
    poller = NotionSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(__import__("yaml").safe_dump(config))
    client = _make_stub_client(pages=pages)
    result = poller.run(client=client)
    assert result.fetched == 3


def test_poller_registered():
    from gateway.pollers import _REGISTRY
    assert "notion" in _REGISTRY
