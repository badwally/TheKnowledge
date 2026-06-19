"""Op->tier classification — Librarian Phase 4 (A2, decision 7).

The MCP surface splits into a runtime READ tier (LLM-free, bounded, idempotent,
side-effect-free) and a BUILD tier (everything that writes or spends model
tokens). The split is DEFAULT-DENY: an op is read-tier only if it is provably
side-effect-free AND token-free; every other MCP-exposed op is build. Over-
including a side-effecting op on the read mount is a security hole, so the read
set is an explicit allowlist, not a derived complement.
"""

from __future__ import annotations

from gateway import cli as _cli
from gateway import mcp_server as _mcp


# Provably side-effect-free AND token-free ops (hyphenated CLI form). Each was
# verified to perform no corpus/derived write and make no Claude/judge/NLM call.
READ_OPS: frozenset[str] = frozenset(
    {
        "retrieve",      # FTS/BM25 retrieval ladder — LLM-free
        "search",        # FTS5/BM25 ranked search
        "context",       # page + ranked neighbors
        "related",       # co-citation neighbors
        "status",        # watcher heartbeat / pending queue
        "intent-status", # intent_id -> disposition (A1 read-tier status op)
        "lint",          # read-only health check (reports, does not fix)
        "list-concepts",
        "list-domains",
        "agent-log",     # reads operational-provenance log
        "agents",        # lists agent registry
    }
)

# Auxiliary wiki_* tools with no CLI op (see mcp_server parity test) that are
# read-tier. wiki_poll_list / wiki_question_list are read-only enumerations.
READ_AUX_TOOLS: frozenset[str] = frozenset({"wiki_poll_list", "wiki_question_list"})


def _mcp_exposed_ops() -> frozenset[str]:
    return frozenset(_cli.IMPLEMENTED) - _mcp.CLI_ONLY


def classify(op: str) -> str:
    """Return 'read' or 'build' for an MCP-exposed op. KeyError if not exposed."""
    if op not in _mcp_exposed_ops():
        raise KeyError(f"{op!r} is not an MCP-exposed op (CLI_ONLY or unknown)")
    return "read" if op in READ_OPS else "build"


def read_tier_tool_names() -> frozenset[str]:
    """wiki_* tool names the read-tier server must register."""
    return frozenset(f"wiki_{op.replace('-', '_')}" for op in READ_OPS) | READ_AUX_TOOLS
