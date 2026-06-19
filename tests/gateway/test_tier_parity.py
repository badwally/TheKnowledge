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


def test_policy_edit_is_not_an_mcp_tool_anywhere():
    """SEC-Critical: policy-edit is HUMAN-CLI-ONLY. wiki_policy_edit must be
    absent from BOTH the read-tier server and the full (build-tier) server, and
    must not exist as a module-level wiki_* tool. There is no use case for an
    agent to autonomously rewrite corpus-wide policy."""
    read_server = mcp_server.build_read_tier_server()
    read_tools = {t.name for t in read_server._tool_manager.list_tools()}
    full_tools = {t.name for t in mcp_server.mcp._tool_manager.list_tools()}

    assert "wiki_policy_edit" not in read_tools, (
        "policy-edit must not be on the read-tier surface"
    )
    assert "wiki_policy_edit" not in full_tools, (
        "policy-edit must not be on the build-tier MCP surface (human-CLI-only)"
    )
    assert not hasattr(mcp_server, "wiki_policy_edit"), (
        "wiki_policy_edit must not be defined as an MCP tool"
    )


def test_policy_edit_is_cli_only():
    """policy-edit is in CLI_ONLY (no MCP surface), mirroring demote-domain."""
    assert "policy-edit" in mcp_server.CLI_ONLY
