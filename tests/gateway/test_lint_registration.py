"""Tests for T2 Step 13: lint check registration + CLI/MCP tier placement.

Adversarial with named negative controls (standing build rule):
- fragmentation and claim-conservation registered in _CHECKS → scoped lint works
- remediate is BUILD-tier (must NOT appear in read_tier_tool_names())
- negative control: remediate absent from read tier
"""

from __future__ import annotations

import pytest


def test_fragmentation_check_registered_in_lint() -> None:
    """lint(scope='fragmentation') runs exactly the fragmentation check."""
    from gateway.ops.lint import KNOWN_CHECKS
    assert "fragmentation" in KNOWN_CHECKS, (
        "fragmentation check must be registered in ops/lint._CHECKS"
    )


def test_claim_conservation_check_registered_in_lint() -> None:
    """lint(scope='claim-conservation') runs exactly the claim-conservation check."""
    from gateway.ops.lint import KNOWN_CHECKS
    assert "claim-conservation" in KNOWN_CHECKS, (
        "claim-conservation check must be registered in ops/lint._CHECKS"
    )


def test_scoped_lint_fragmentation_runs(kb_root) -> None:
    """lint(scope='fragmentation') succeeds and returns OperationResult."""
    from gateway.ops.lint import lint
    res = lint(scope="fragmentation")
    assert res.success, f"scoped lint for fragmentation failed: {res.errors}"


def test_scoped_lint_claim_conservation_runs(kb_root) -> None:
    """lint(scope='claim-conservation') succeeds and returns OperationResult."""
    from gateway.ops.lint import lint
    res = lint(scope="claim-conservation")
    assert res.success, f"scoped lint for claim-conservation failed: {res.errors}"


def test_remediate_absent_from_read_tier() -> None:
    """Negative control: remediate is a build-tier op — must NOT be in read_tier_tool_names().

    If it appeared in the read tier, it could submit intents from a context that
    is supposed to be read-only.
    """
    from gateway import tier
    tool_names = tier.read_tier_tool_names()
    assert "wiki_remediate" not in tool_names, (
        "wiki_remediate must be a build-tier tool — not in read_tier_tool_names()"
    )


def test_wiki_remediate_registered_in_mcp_server() -> None:
    """wiki_remediate is registered as a @mcp.tool() in mcp_server.py."""
    import gateway.mcp_server as mcp_module
    assert hasattr(mcp_module, "wiki_remediate"), (
        "wiki_remediate must be registered as a @mcp.tool() in mcp_server.py"
    )


def test_remediate_cli_subcommand_implemented() -> None:
    """'remediate' subcommand is in IMPLEMENTED in cli.py."""
    from gateway.cli import IMPLEMENTED, SUBCOMMANDS
    assert "remediate" in SUBCOMMANDS, (
        "'remediate' must appear in SUBCOMMANDS dict in cli.py"
    )
    assert "remediate" in IMPLEMENTED, (
        "'remediate' must appear in IMPLEMENTED set in cli.py"
    )
