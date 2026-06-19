"""Tests for preflight op (Task 4: read-tier plan/executor pre-flight).

TDD — tests written RED first (Step 9).
"""
from __future__ import annotations

import pytest


# ---------------------------------------------------------------------------
# Step 9 — preflight interface + tier classification
# ---------------------------------------------------------------------------


def test_preflight_in_read_ops():
    """'preflight' is in tier.READ_OPS."""
    from gateway import tier
    assert "preflight" in tier.READ_OPS


def test_wiki_preflight_in_read_tier_tool_names():
    """'wiki_preflight' is in read_tier_tool_names()."""
    from gateway import tier
    assert "wiki_preflight" in tier.read_tier_tool_names()


def test_preflight_returns_success(kb_root):
    """preflight returns OperationResult(success=True) with gaps/enrichment_status."""
    from gateway.ops.preflight import preflight
    result = preflight("a research plan about nutrition and metabolism")
    assert result.success is True
    assert result.data is not None
    assert "gaps" in result.data
    assert "enrichment_status" in result.data


def test_preflight_gaps_is_list(kb_root):
    """preflight data['gaps'] is a list."""
    from gateway.ops.preflight import preflight
    result = preflight("a plan about macroeconomic policy")
    assert isinstance(result.data["gaps"], list)


def test_preflight_does_not_enqueue_intent(kb_root):
    """preflight must NOT enqueue any intent — queue depth unchanged after call."""
    from gateway.ops.preflight import preflight
    from gateway.intent_queue import IntentQueue

    q = IntentQueue()
    depth_before = q.depth()
    preflight("a research plan about the federal reserve")
    depth_after = q.depth()
    assert depth_after == depth_before, (
        f"preflight enqueued {depth_after - depth_before} intent(s) — must enqueue none"
    )


def test_preflight_does_not_spend_tokens(kb_root):
    """preflight must be LLM-free — no client/model call."""
    # This is structurally enforced: preflight calls retrieve() (LLM-free) not answer().
    # We verify by calling it without an API client in scope — it must not raise.
    from gateway.ops.preflight import preflight
    # No anthropic client configured — if preflight calls an LLM it will raise/fail
    result = preflight("how does insulin resistance develop", root=kb_root)
    assert result.success is True


def test_preflight_enrichment_status_has_coverage(kb_root):
    """preflight data['enrichment_status'] contains a 'coverage' key."""
    from gateway.ops.preflight import preflight
    result = preflight("a plan about semaglutide and weight loss mechanisms")
    assert "coverage" in result.data["enrichment_status"]


def test_preflight_tier_parity_still_passes():
    """Adding preflight to READ_OPS does not break the tier parity invariants."""
    from gateway import mcp_server, tier

    # preflight must be in MCP-exposed ops (i.e., in IMPLEMENTED, not CLI_ONLY)
    mcp_exposed = set(tier._mcp_exposed_ops())
    assert "preflight" in mcp_exposed, "preflight must be in IMPLEMENTED and not CLI_ONLY"

    # The read-tier server must register wiki_preflight
    server = mcp_server.build_read_tier_server()
    registered = {t.name for t in server._tool_manager.list_tools()}
    assert "wiki_preflight" in registered


def test_preflight_read_tier_server_registers_wiki_preflight():
    """build_read_tier_server() registers wiki_preflight (not RuntimeError)."""
    from gateway import mcp_server
    server = mcp_server.build_read_tier_server()
    registered = {t.name for t in server._tool_manager.list_tools()}
    assert "wiki_preflight" in registered


def test_preflight_is_classified_read():
    """tier.classify('preflight') returns 'read'."""
    from gateway import tier
    assert tier.classify("preflight") == "read"


def test_preflight_negative_control_not_build():
    """preflight is NOT a build-tier op."""
    from gateway import tier
    assert tier.classify("preflight") != "build"
