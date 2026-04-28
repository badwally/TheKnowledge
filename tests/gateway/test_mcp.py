"""Tests for the M7 MCP server.

Tools delegate to the same gateway operations as the CLI; the protocol
plumbing is the SDK's responsibility. Tests focus on:

- Tool registration: every wiki_* tool is registered.
- OperationResult serialization: dicts are JSON-friendly.
- Tool dispatch: invoking a tool function reaches the underlying op.
- mcp-serve subcommand wires through to the runner (importable).
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import mcp_server
from gateway import paths
from gateway.core import OperationResult


# --- registration ---------------------------------------------------------


_EXPECTED_TOOLS = {
    "wiki_ingest",
    "wiki_filter",
    "wiki_filter_correct",
    "wiki_query",
    "wiki_finalize",
    "wiki_nlm_add",
    "wiki_nlm_slides",
    "wiki_nlm_audio",
    "wiki_nlm_briefing",
    "wiki_nlm_revise",
    "wiki_status",
}


def _list_registered_tools() -> set[str]:
    """Use FastMCP's async API to list tools."""
    tools = asyncio.run(mcp_server.mcp.list_tools())
    return {t.name for t in tools}


def test_all_expected_tools_registered():
    registered = _list_registered_tools()
    missing = _EXPECTED_TOOLS - registered
    assert not missing, f"missing MCP tools: {missing}"


def test_no_duplicate_tools():
    registered = _list_registered_tools()
    # Tools listed should be unique
    tools = asyncio.run(mcp_server.mcp.list_tools())
    names = [t.name for t in tools]
    assert len(names) == len(set(names))


def test_each_tool_has_a_description():
    tools = asyncio.run(mcp_server.mcp.list_tools())
    for tool in tools:
        if tool.name in _EXPECTED_TOOLS:
            assert tool.description, f"tool {tool.name} missing description"


# --- serializer -----------------------------------------------------------


def test_serialize_round_trips_through_json():
    result = OperationResult(
        success=True,
        no_op=False,
        summary="ingested: yt-x",
        paths_touched=[Path("/a/b/c.md"), Path("/a/b/d.md")],
        errors=[],
        warnings=["one warning"],
    )
    serialized = mcp_server._serialize(result)
    # Must be JSON-encodable
    text = json.dumps(serialized)
    parsed = json.loads(text)
    assert parsed["success"] is True
    assert parsed["summary"] == "ingested: yt-x"
    assert parsed["paths_touched"] == ["/a/b/c.md", "/a/b/d.md"]
    assert parsed["warnings"] == ["one warning"]
    assert parsed["errors"] == []


def test_serialize_failure_preserves_errors():
    result = OperationResult(
        success=False,
        summary="",
        errors=["thing broke", "another thing"],
    )
    serialized = mcp_server._serialize(result)
    assert serialized["success"] is False
    assert serialized["errors"] == ["thing broke", "another thing"]


# --- dispatch (each tool reaches the op layer) ----------------------------


def test_wiki_status_returns_a_result(kb_root):
    out = mcp_server.wiki_status()
    assert "success" in out
    assert out["success"] is True
    assert "summary" in out


def test_wiki_ingest_dispatches_to_ingest_op(kb_root, make_source, tmp_path, monkeypatch):
    """Calling the tool function should reach gateway.ops.ingest.ingest."""
    captured = {}

    def fake_ingest(source, **kwargs):
        captured["source"] = source
        captured["kwargs"] = kwargs
        return OperationResult(success=True, summary="fake")

    monkeypatch.setattr("gateway.ops.ingest.ingest", fake_ingest)
    out = mcp_server.wiki_ingest("https://example.com/x", domain="d", with_plan=True, draft=True)
    assert out["success"] is True
    assert captured["source"] == "https://example.com/x"
    assert captured["kwargs"]["domain"] == "d"
    assert captured["kwargs"]["with_plan"] is True
    assert captured["kwargs"]["draft"] is True


def test_wiki_ingest_resolves_path_inputs(kb_root, monkeypatch, tmp_path):
    captured = {}

    def fake_ingest(source, **kwargs):
        captured["source"] = source
        return OperationResult(success=True, summary="fake")

    monkeypatch.setattr("gateway.ops.ingest.ingest", fake_ingest)
    test_file = tmp_path / "x.md"
    test_file.write_text("---\nid: x\n---\nbody")
    mcp_server.wiki_ingest(str(test_file))
    assert isinstance(captured["source"], Path)
    assert captured["source"].is_absolute()


def test_wiki_filter_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake_filter(source, *, domain=None, client=None):
        captured["source"] = source
        captured["domain"] = domain
        return OperationResult(success=True, summary="score=0.5")

    monkeypatch.setattr("gateway.ops.filter_op.filter_source", fake_filter)
    out = mcp_server.wiki_filter("https://example.com/x", domain="d")
    assert out["summary"] == "score=0.5"
    assert captured["domain"] == "d"


def test_wiki_filter_correct_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake(source_id, *, decision, rationale, domain=None):
        captured.update(
            source_id=source_id, decision=decision, rationale=rationale, domain=domain
        )
        return OperationResult(success=True, summary="corrected")

    monkeypatch.setattr("gateway.ops.filter_correct.filter_correct", fake)
    out = mcp_server.wiki_filter_correct("yt-x", "include", "because")
    assert out["success"] is True
    assert captured == {"source_id": "yt-x", "decision": "include", "rationale": "because", "domain": None}


def test_wiki_query_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake_query(question, *, domain=None, client=None):
        captured.update(question=question, domain=domain)
        return OperationResult(success=True, summary="filed synthesis")

    monkeypatch.setattr("gateway.ops.query.query", fake_query)
    out = mcp_server.wiki_query("how does X work?", domain="d1")
    assert out["success"] is True
    assert captured["question"] == "how does X work?"
    assert captured["domain"] == "d1"


def test_wiki_finalize_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake_finalize(page_path, *, abandon=False):
        captured.update(page_path=page_path, abandon=abandon)
        return OperationResult(success=True, summary="finalized")

    monkeypatch.setattr("gateway.ops.finalize.finalize", fake_finalize)
    out = mcp_server.wiki_finalize("wiki/concepts/x.md", abandon=True)
    assert out["success"] is True
    assert captured == {"page_path": "wiki/concepts/x.md", "abandon": True}


def test_wiki_nlm_add_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake(domain, source_id, *, client=None):
        captured.update(domain=domain, source_id=source_id)
        return OperationResult(success=True, summary="added")

    monkeypatch.setattr("gateway.ops.nlm.nlm_add", fake)
    out = mcp_server.wiki_nlm_add("d1", "yt-x")
    assert out["success"] is True
    assert captured == {"domain": "d1", "source_id": "yt-x"}


def test_wiki_nlm_slides_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake(domain, topic, *, client=None):
        captured.update(domain=domain, topic=topic)
        return OperationResult(success=True, summary="filed slides")

    monkeypatch.setattr("gateway.ops.nlm.nlm_slides", fake)
    out = mcp_server.wiki_nlm_slides("d1", "reward dose response")
    assert out["success"] is True
    assert captured["topic"] == "reward dose response"


def test_wiki_nlm_audio_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake(domain, topic, *, client=None):
        captured.update(domain=domain, topic=topic)
        return OperationResult(success=True, summary="filed audio")

    monkeypatch.setattr("gateway.ops.nlm.nlm_audio", fake)
    out = mcp_server.wiki_nlm_audio("d1", "deep dive")
    assert out["success"] is True


def test_wiki_nlm_briefing_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake(domain, *, client=None):
        captured.update(domain=domain)
        return OperationResult(success=True, summary="filed briefing")

    monkeypatch.setattr("gateway.ops.nlm.nlm_briefing", fake)
    out = mcp_server.wiki_nlm_briefing("d1")
    assert out["success"] is True
    assert captured["domain"] == "d1"


def test_wiki_nlm_revise_dispatches(kb_root, monkeypatch):
    captured = {}

    def fake(slug, slides, *, client=None):
        captured.update(slug=slug, slides=slides)
        return OperationResult(success=True, summary="revised")

    monkeypatch.setattr("gateway.ops.nlm.nlm_revise", fake)
    out = mcp_server.wiki_nlm_revise("2026-04-28-topic-slides", ["1 make title bigger"])
    assert out["success"] is True
    assert captured["slug"] == "2026-04-28-topic-slides"
    assert captured["slides"] == ["1 make title bigger"]


# --- CLI wiring -----------------------------------------------------------


def test_mcp_serve_subcommand_in_help():
    from gateway import cli

    parser = cli.build_parser()
    # argparse stores subparser choices on the action
    sub_action = next(a for a in parser._actions if isinstance(a, type(parser._actions[-1])) and getattr(a, "choices", None))
    # Less brittle: just check the subcommand is enumerated in help
    out = parser.format_help()
    assert "mcp-serve" in out
