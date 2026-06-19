from __future__ import annotations

import pytest

from gateway import cli as cli_mod
from gateway import mcp_server, tier


def _mcp_exposed_ops() -> set[str]:
    return set(cli_mod.IMPLEMENTED) - set(mcp_server.CLI_ONLY)


def test_every_mcp_exposed_op_is_classified():
    """Totality: classify() returns read|build for every MCP-exposed op, none unclassified."""
    for op in _mcp_exposed_ops():
        assert tier.classify(op) in {"read", "build"}, op


def test_classify_rejects_non_mcp_exposed_op():
    """A CLI_ONLY op (or unknown op) is not classifiable — it has no tier."""
    with pytest.raises(KeyError):
        tier.classify("demote-domain")  # CLI_ONLY


def test_read_ops_are_subset_of_mcp_exposed():
    assert tier.READ_OPS <= _mcp_exposed_ops()


def test_read_tier_server_registers_exactly_the_read_classified_set():
    """Parity: the read-tier server's registered tools == the read-classified set."""
    server = mcp_server.build_read_tier_server()
    registered = {t.name for t in server._tool_manager.list_tools()}
    assert registered == set(tier.read_tier_tool_names())


def test_read_tier_excludes_build_tools_negative_control():
    """A read-tier mount does NOT register build tools — calling one is tool-not-found,
    not a silent no-op. Pin the highest-risk build tools explicitly."""
    server = mcp_server.build_read_tier_server()
    registered = {t.name for t in server._tool_manager.list_tools()}
    for build_tool in ("wiki_ingest", "wiki_query", "wiki_deposit", "wiki_filter", "wiki_edit"):
        assert build_tool not in registered


def test_full_server_still_registers_everything():
    """The full server (mcp_server.mcp) is unchanged — superset of the read tier."""
    full = {t.name for t in mcp_server.mcp._tool_manager.list_tools()}
    assert set(tier.read_tier_tool_names()) <= full
