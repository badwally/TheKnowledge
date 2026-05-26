"""INT-12: publish-notion — wiki → Notion read-only mirror tests."""

from __future__ import annotations

import json
import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.publish_notion import (
    _collect_pages,
    _load_registry,
    _registry_path,
    _save_registry,
    publish_notion,
)


# --- helpers ----------------------------------------------------------------


def _make_wiki_page(
    kb_root: Path,
    page_type: str,
    slug: str,
    domain: str,
    **extra_front,
) -> Path:
    type_dir = paths.wiki_dir() / f"{page_type}s"
    type_dir.mkdir(parents=True, exist_ok=True)
    p = type_dir / f"{slug}.md"
    front = {
        "type": page_type,
        "slug": slug,
        "title": f"Title for {slug}",
        "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
        **extra_front,
    }
    p.write_text(fm.serialize(front, f"Body for {slug}.\n"))
    return p


def _stub_client(
    *,
    create_db_id: str = "db-001",
    create_page_id: str = "page-001",
    update_result: dict | None = None,
    archive_result: dict | None = None,
    create_db_raises: Exception | None = None,
    create_page_raises: Exception | None = None,
    update_raises: Exception | None = None,
    archive_raises: Exception | None = None,
):
    client = MagicMock()
    if create_db_raises:
        client.create_database.side_effect = create_db_raises
    else:
        client.create_database.return_value = {"id": create_db_id}
    if create_page_raises:
        client.create_page.side_effect = create_page_raises
    else:
        client.create_page.return_value = {"id": create_page_id}
    client.update_page.return_value = update_result or {"id": "page-xxx"}
    if archive_raises:
        client.archive_page.side_effect = archive_raises
    else:
        client.archive_page.return_value = archive_result or {"id": "page-xxx"}
    return client


# --- registry tests ---------------------------------------------------------


def test_registry_round_trip(kb_root: Path) -> None:
    _save_registry("alpha", {"__database_id__": "db-1", "concepts/foo.md": "p-1"})
    loaded = _load_registry("alpha")
    assert loaded["__database_id__"] == "db-1"
    assert loaded["concepts/foo.md"] == "p-1"


def test_load_registry_missing_returns_empty(kb_root: Path) -> None:
    assert _load_registry("nonexistent-domain") == {}


# --- _collect_pages tests ---------------------------------------------------


def test_collect_pages_finds_concept(kb_root: Path) -> None:
    _make_wiki_page(kb_root, "concept", "food-noise", "glp1")
    pages = _collect_pages("glp1")
    assert len(pages) == 1
    assert pages[0]["type"] == "concept"
    assert pages[0]["slug"] == "food-noise"
    assert pages[0]["title"] == "Title for food-noise"


def test_collect_pages_filters_by_domain(kb_root: Path) -> None:
    _make_wiki_page(kb_root, "concept", "foo", "glp1")
    _make_wiki_page(kb_root, "concept", "bar", "other-domain")
    pages = _collect_pages("glp1")
    slugs = {p["slug"] for p in pages}
    assert slugs == {"foo"}


def test_collect_pages_multi_domain_page_included(kb_root: Path) -> None:
    _make_wiki_page(kb_root, "concept", "shared", "glp1", domains=["glp1", "biohacking"])
    pages = _collect_pages("glp1")
    assert len(pages) == 1


def test_collect_pages_excludes_sources_by_default(kb_root: Path) -> None:
    _make_wiki_page(kb_root, "concept", "foo", "glp1")
    _make_wiki_page(kb_root, "source", "src-001", "glp1")
    pages = _collect_pages("glp1")
    types = {p["type"] for p in pages}
    assert "source" not in types


def test_collect_pages_includes_sources_when_flag_set(kb_root: Path) -> None:
    _make_wiki_page(kb_root, "concept", "foo", "glp1")
    _make_wiki_page(kb_root, "source", "src-001", "glp1")
    pages = _collect_pages("glp1", include_sources=True)
    types = {p["type"] for p in pages}
    assert "source" in types


def test_collect_pages_includes_body_excerpt(kb_root: Path) -> None:
    _make_wiki_page(kb_root, "concept", "foo", "glp1")
    pages = _collect_pages("glp1")
    assert "Body for foo" in pages[0]["body_excerpt"]


# --- publish_notion tests ---------------------------------------------------


def test_publish_notion_missing_parent_page_id(kb_root: Path, monkeypatch) -> None:
    monkeypatch.delenv("NOTION_PARENT_PAGE_ID", raising=False)
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    client = _stub_client()
    result = publish_notion("alpha", client=client)
    assert not result.success
    assert "NOTION_PARENT_PAGE_ID" in result.errors[0]


def test_publish_notion_no_pages_returns_success(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    client = _stub_client()
    result = publish_notion("empty-domain", client=client)
    assert result.success
    client.create_database.assert_not_called()


def test_publish_notion_creates_database_and_page(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    client = _stub_client(create_db_id="db-alpha", create_page_id="p-foo")

    result = publish_notion("alpha", client=client)

    assert result.success
    client.create_database.assert_called_once()
    client.create_page.assert_called_once()
    # Registry should now have db ID and page mapping
    reg = _load_registry("alpha")
    assert reg["__database_id__"] == "db-alpha"
    assert "concepts/foo.md" in reg
    assert reg["concepts/foo.md"] == "p-foo"


def test_publish_notion_reuses_existing_database(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    _save_registry("alpha", {"__database_id__": "db-existing"})
    client = _stub_client()

    publish_notion("alpha", client=client)

    client.create_database.assert_not_called()
    client.create_page.assert_called_once()


def test_publish_notion_updates_existing_page(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    _save_registry("alpha", {"__database_id__": "db-001", "concepts/foo.md": "p-existing"})
    client = _stub_client()

    result = publish_notion("alpha", client=client)

    assert result.success
    client.create_page.assert_not_called()
    client.update_page.assert_called_once_with(
        "p-existing",
        title="Title for foo",
        last_updated="2026-05-01T00:00:00Z",
        domains=["alpha"],
    )


def test_publish_notion_archives_removed_page(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "current", "alpha")
    # Registry has a page that no longer exists in wiki
    _save_registry("alpha", {
        "__database_id__": "db-001",
        "concepts/current.md": "p-current",
        "concepts/removed.md": "p-removed",
    })
    client = _stub_client()

    result = publish_notion("alpha", client=client)

    assert result.success
    client.archive_page.assert_called_once_with("p-removed")


def test_publish_notion_handles_create_page_error(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    _save_registry("alpha", {"__database_id__": "db-001"})
    client = _stub_client(create_page_raises=Exception("API timeout"))

    result = publish_notion("alpha", client=client)

    assert not result.success
    assert len(result.errors) == 1
    assert "API timeout" in result.errors[0]


def test_publish_notion_database_create_failure(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    client = _stub_client(create_db_raises=Exception("Notion 401 Unauthorized"))

    result = publish_notion("alpha", client=client)

    assert not result.success
    assert "create database" in result.errors[0]


def test_publish_notion_summary_includes_counts(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "foo", "alpha")
    _make_wiki_page(kb_root, "entity", "bar", "alpha")
    client = _stub_client(create_db_id="db-alpha")
    client.create_page.side_effect = [{"id": "p-1"}, {"id": "p-2"}]

    result = publish_notion("alpha", client=client)

    assert result.success
    assert "2" in result.summary  # 2 created
    assert "alpha" in result.summary


def test_publish_notion_registry_saved_on_partial_error(kb_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("NOTION_PARENT_PAGE_ID", "parent-1")
    _make_wiki_page(kb_root, "concept", "good", "alpha")
    _make_wiki_page(kb_root, "concept", "bad", "alpha")
    _save_registry("alpha", {"__database_id__": "db-001"})

    call_count = 0

    def create_side_effect(**kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 2:
            raise Exception("second page failed")
        return {"id": f"p-{call_count}"}

    client = MagicMock()
    client.create_page.side_effect = create_side_effect

    publish_notion("alpha", client=client)

    # Registry should be saved (with the successful page) despite the error
    reg = _load_registry("alpha")
    assert "__database_id__" in reg
