"""K2 (M47): MCP-CLI parity test.

Every CLI op in ``cli.IMPLEMENTED`` must have a matching ``wiki_*`` MCP
tool, except those listed in ``mcp_server.CLI_ONLY``. This is the forcing
function: any future op that lands in the CLI but forgets MCP exposure
will fail this test in CI, preventing the surface drift documented in
the K1–K5 review (`ARCH-7`, `AGT-11`, `TOOL-1`).

The CLI_ONLY allowlist covers ops that intentionally have no MCP shape:
- daemons (`watch`)
- the MCP server itself (`mcp-serve`)
- the web server (`serve`)
- destructive cross-state actions per C4 (`demote-domain`)
"""

from __future__ import annotations

import pytest

from gateway import cli as cli_mod
from gateway import mcp_server


def test_cli_only_allowlist_is_documented():
    """The mcp_server module must declare CLI_ONLY explicitly."""
    assert hasattr(mcp_server, "CLI_ONLY"), (
        "mcp_server.CLI_ONLY must enumerate CLI ops intentionally without MCP wrappers"
    )
    assert isinstance(mcp_server.CLI_ONLY, frozenset)


def test_every_implemented_cli_op_has_mcp_tool_or_is_cli_only():
    """Parity assertion: IMPLEMENTED - CLI_ONLY ⊆ MCP tools."""
    expected_tools = {
        f"wiki_{op.replace('-', '_')}"
        for op in cli_mod.IMPLEMENTED
        if op not in mcp_server.CLI_ONLY
    }
    actual_tools = {
        name
        for name in dir(mcp_server)
        if name.startswith("wiki_") and callable(getattr(mcp_server, name))
    }
    missing = expected_tools - actual_tools
    assert not missing, (
        f"CLI ops without MCP tool: {sorted(missing)} "
        f"(add to mcp_server.py or mark CLI_ONLY)"
    )


def test_no_orphan_mcp_tools_without_cli_op():
    """Every wiki_* MCP tool should map back to either a CLI op or an explicit
    CLI_ONLY-exempt extension (currently none)."""
    cli_ops_as_mcp = {
        f"wiki_{op.replace('-', '_')}" for op in cli_mod.IMPLEMENTED
    }
    actual_tools = {
        name
        for name in dir(mcp_server)
        if name.startswith("wiki_") and callable(getattr(mcp_server, name))
    }
    orphans = actual_tools - cli_ops_as_mcp
    # Allow auxiliary tools that don't have a CLI counterpart by listing them
    # in a small expected set. wiki_poll_list is the only such today.
    expected_auxiliary = {"wiki_poll_list"}
    unexpected_orphans = orphans - expected_auxiliary
    assert not unexpected_orphans, (
        f"MCP tools without a CLI op or auxiliary entry: {sorted(unexpected_orphans)}"
    )


def test_demote_domain_is_explicitly_cli_only_per_c4():
    """Per plan C4: wiki_demote_domain is omitted from MCP (destructive cross-state).
    This pins the decision in the test so it can't drift accidentally.
    """
    assert "demote-domain" in mcp_server.CLI_ONLY
    assert not hasattr(mcp_server, "wiki_demote_domain")
