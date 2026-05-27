"""TOOL-15: wiki ask-corpus — NLM corpus direct query (CLI + MCP)."""

from __future__ import annotations

import argparse
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from gateway.core import OperationResult


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _ok_result(**kwargs) -> OperationResult:
    defaults = dict(success=True, summary="Wrote draft: wiki/synthesis/test-answer.md", data={})
    defaults.update(kwargs)
    return OperationResult(**defaults)


# ---------------------------------------------------------------------------
# CLI: _run_ask_corpus_cmd
# ---------------------------------------------------------------------------


def test_ask_corpus_cli_calls_query(kb_root: Path) -> None:
    from gateway.cli import _run_ask_corpus_cmd

    ns = argparse.Namespace(subcommand="ask-corpus", domain="glp1", question="Does GLP-1 reduce craving?", no_draft=False)
    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_query:
        rc = _run_ask_corpus_cmd(ns)

    mock_query.assert_called_once_with("Does GLP-1 reduce craving?", domain="glp1", draft=True)
    assert rc == 0


def test_ask_corpus_cli_no_draft_flag(kb_root: Path) -> None:
    from gateway.cli import _run_ask_corpus_cmd

    ns = argparse.Namespace(subcommand="ask-corpus", domain="glp1", question="Question?", no_draft=True)
    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_query:
        _run_ask_corpus_cmd(ns)

    mock_query.assert_called_once_with("Question?", domain="glp1", draft=False)


def test_ask_corpus_cli_failure_returns_nonzero(kb_root: Path) -> None:
    from gateway.cli import _run_ask_corpus_cmd

    ns = argparse.Namespace(subcommand="ask-corpus", domain="glp1", question="Q?", no_draft=False)
    failed = OperationResult(success=False, summary="NLM timeout", data={})
    with patch("gateway.ops.query.query", return_value=failed):
        rc = _run_ask_corpus_cmd(ns)

    assert rc != 0


# ---------------------------------------------------------------------------
# CLI: parser wiring
# ---------------------------------------------------------------------------


def test_ask_corpus_registered_in_subcommands() -> None:
    from gateway.cli import SUBCOMMANDS, IMPLEMENTED

    assert "ask-corpus" in SUBCOMMANDS
    assert "ask-corpus" in IMPLEMENTED


def test_ask_corpus_parser_parses_domain_and_question() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["ask-corpus", "glp1", "My question here?"])
    assert ns.domain == "glp1"
    assert ns.question == "My question here?"
    assert ns.no_draft is False


def test_ask_corpus_parser_no_draft() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["ask-corpus", "edge-ai", "What limits on-device?", "--no-draft"])
    assert ns.no_draft is True


# ---------------------------------------------------------------------------
# MCP: wiki_ask_corpus tool
# ---------------------------------------------------------------------------


def test_mcp_wiki_ask_corpus_exists() -> None:
    from gateway import mcp_server

    assert hasattr(mcp_server, "wiki_ask_corpus")
    assert callable(mcp_server.wiki_ask_corpus)


def test_mcp_wiki_ask_corpus_calls_query(kb_root: Path) -> None:
    from gateway.mcp_server import wiki_ask_corpus

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_query:
        result = wiki_ask_corpus(domain="glp1", question="Test question?")

    mock_query.assert_called_once_with("Test question?", domain="glp1", draft=True)
    assert result["success"] is True


def test_mcp_wiki_ask_corpus_draft_false(kb_root: Path) -> None:
    from gateway.mcp_server import wiki_ask_corpus

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_query:
        wiki_ask_corpus(domain="glp1", question="Test?", draft=False)

    mock_query.assert_called_once_with("Test?", domain="glp1", draft=False)


def test_mcp_wiki_ask_corpus_returns_serializable_dict(kb_root: Path) -> None:
    from gateway.mcp_server import wiki_ask_corpus

    with patch("gateway.ops.query.query", return_value=_ok_result(data={"page": "wiki/synthesis/foo.md"})):
        result = wiki_ask_corpus(domain="glp1", question="Q?")

    import json
    json.dumps(result)  # must not raise
    assert isinstance(result, dict)
