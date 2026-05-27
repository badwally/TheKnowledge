"""TOOL-16: wiki question new / list — question page management."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from gateway import paths
from gateway.core import OperationResult


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _questions_dir(kb_root: Path) -> Path:
    d = paths.knowledge_root() / "wiki" / "questions"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# question_new — unit tests
# ---------------------------------------------------------------------------


def test_question_new_creates_file(kb_root: Path) -> None:
    from gateway.ops.question import question_new

    result = question_new("test-slug", "My test question?", "glp1")

    assert result.success
    assert "wiki/questions/test-slug.md" in result.summary
    target = paths.knowledge_root() / "wiki" / "questions" / "test-slug.md"
    assert target.exists()


def test_question_new_frontmatter(kb_root: Path) -> None:
    from gateway import frontmatter as fm
    from gateway.ops.question import question_new

    question_new("my-question", "What is GLP-1?", "glp1", status="open")

    target = paths.knowledge_root() / "wiki" / "questions" / "my-question.md"
    front, body = fm.parse(target.read_text())

    assert front["type"] == "question"
    assert front["slug"] == "my-question"
    assert front["title"] == "What is GLP-1?"
    assert front["domains"] == ["glp1"]
    assert front["status"] == "open"
    assert "created_at" in front
    assert "last_updated" in front


def test_question_new_body_sections(kb_root: Path) -> None:
    from gateway import frontmatter as fm
    from gateway.ops.question import question_new

    question_new("sections-test", "Does X cause Y?", "test-domain")

    target = paths.knowledge_root() / "wiki" / "questions" / "sections-test.md"
    _, body = fm.parse(target.read_text())

    assert "## Question" in body
    assert "## Context" in body


def test_question_new_invalid_slug(kb_root: Path) -> None:
    from gateway.ops.question import question_new

    result = question_new("Invalid Slug!", "Title", "glp1")

    assert not result.success
    assert "invalid slug" in result.errors[0]


def test_question_new_invalid_status(kb_root: Path) -> None:
    from gateway.ops.question import question_new

    result = question_new("valid-slug", "Title", "glp1", status="unknown")

    assert not result.success
    assert "invalid status" in result.errors[0]


def test_question_new_duplicate_slug(kb_root: Path) -> None:
    from gateway.ops.question import question_new

    question_new("dup-slug", "First", "glp1")
    result = question_new("dup-slug", "Second", "glp1")

    assert not result.success
    assert "already exists" in result.errors[0]


def test_question_new_partial_status(kb_root: Path) -> None:
    from gateway.ops.question import question_new

    result = question_new("partial-q", "Partial question?", "glp1", status="partial")

    assert result.success


# ---------------------------------------------------------------------------
# question_list — unit tests
# ---------------------------------------------------------------------------


def _write_question(
    kb_root: Path,
    slug: str,
    domain: str = "glp1",
    status: str = "open",
    title: str = "Test?",
) -> None:
    from gateway.ops.question import question_new
    question_new(slug, title, domain, status=status)


def test_question_list_empty(kb_root: Path) -> None:
    from gateway.ops.question import question_list

    result = question_list()
    assert result == []


def test_question_list_returns_all(kb_root: Path) -> None:
    from gateway.ops.question import question_list

    _write_question(kb_root, "q-one", status="open")
    _write_question(kb_root, "q-two", status="answered")

    items = question_list()
    slugs = {i["slug"] for i in items}
    assert "q-one" in slugs
    assert "q-two" in slugs


def test_question_list_filter_domain(kb_root: Path) -> None:
    from gateway.ops.question import question_list

    _write_question(kb_root, "q-glp1", domain="glp1")
    _write_question(kb_root, "q-edge", domain="edge-ai")

    items = question_list(domain="glp1")
    assert all(i["slug"].startswith("q-glp1") or "glp1" in i["domains"] for i in items)
    assert not any(i["slug"] == "q-edge" for i in items)


def test_question_list_filter_status(kb_root: Path) -> None:
    from gateway.ops.question import question_list

    _write_question(kb_root, "q-open", status="open")
    _write_question(kb_root, "q-answered", status="answered")

    open_items = question_list(status="open")
    assert all(i["status"] == "open" for i in open_items)
    assert not any(i["slug"] == "q-answered" for i in open_items)


def test_question_list_item_shape(kb_root: Path) -> None:
    from gateway.ops.question import question_list

    _write_question(kb_root, "shape-test", domain="glp1", status="open", title="Shape test?")

    items = question_list()
    assert len(items) == 1
    item = items[0]

    assert item["slug"] == "shape-test"
    assert item["title"] == "Shape test?"
    assert item["status"] == "open"
    assert item["domains"] == ["glp1"]
    assert "last_updated" in item
    assert "path" in item


# ---------------------------------------------------------------------------
# CLI: parser + dispatch
# ---------------------------------------------------------------------------


def test_question_registered_in_subcommands() -> None:
    from gateway.cli import SUBCOMMANDS, IMPLEMENTED

    assert "question" in SUBCOMMANDS
    assert "question" in IMPLEMENTED


def test_question_new_cli_dispatch(kb_root: Path) -> None:
    from gateway.cli import build_parser, _run_question_cmd

    parser = build_parser()
    ns = parser.parse_args(["question", "new", "cli-test-q", "CLI title?", "--domain", "glp1"])
    rc = _run_question_cmd(ns)

    assert rc == 0
    target = paths.knowledge_root() / "wiki" / "questions" / "cli-test-q.md"
    assert target.exists()


def test_question_list_cli_json(kb_root: Path) -> None:
    from gateway.cli import build_parser, _run_question_cmd
    from gateway.ops.question import question_new
    import io, contextlib

    question_new("list-json-q", "List JSON?", "glp1")
    parser = build_parser()
    ns = parser.parse_args(["question", "list", "--json"])

    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        rc = _run_question_cmd(ns)

    assert rc == 0
    data = json.loads(captured.getvalue())
    assert isinstance(data, list)
    assert any(i["slug"] == "list-json-q" for i in data)


# ---------------------------------------------------------------------------
# MCP tools
# ---------------------------------------------------------------------------


def test_mcp_wiki_question_new_exists() -> None:
    from gateway import mcp_server

    assert hasattr(mcp_server, "wiki_question_new")
    assert callable(mcp_server.wiki_question_new)


def test_mcp_wiki_question_list_exists() -> None:
    from gateway import mcp_server

    assert hasattr(mcp_server, "wiki_question_list")
    assert callable(mcp_server.wiki_question_list)


def test_mcp_wiki_question_new_creates(kb_root: Path) -> None:
    from gateway.mcp_server import wiki_question_new

    result = wiki_question_new("mcp-q", "MCP question?", "glp1")

    assert result["success"] is True
    target = paths.knowledge_root() / "wiki" / "questions" / "mcp-q.md"
    assert target.exists()


def test_mcp_wiki_question_list_returns_list(kb_root: Path) -> None:
    from gateway.mcp_server import wiki_question_new, wiki_question_list

    wiki_question_new("listed-q", "Listed?", "glp1")
    items = wiki_question_list()

    assert isinstance(items, list)
    assert any(i["slug"] == "listed-q" for i in items)
