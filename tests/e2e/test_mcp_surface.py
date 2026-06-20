"""T4 — MCP surface E2E tests.

Step 1: exact-set tool assertion for the read-tier server vs. the build server.
  - Read-tier server exposes EXACTLY read_tier_tool_names() — no more, no less.
  - Negative control: build server has the build-only tools (deposit, remediate, …)
    that are absent on the read server — proving the read server FILTERS rather
    than the tools simply not existing.

Step 2: MCP deposit round-trip via the build server.
  - call_tool("wiki_deposit", {...}) → disposition="queued"
  - run_worker(once=True) → page committed to disk + git.
"""

from __future__ import annotations

import asyncio
import json
import subprocess
from pathlib import Path

import pytest

from mcp.shared.memory import create_connected_server_and_client_session

from gateway import mcp_server
from gateway.mcp_server import build_read_tier_server
from gateway.tier import read_tier_tool_names


# ---------------------------------------------------------------------------
# Shared git-repo fixture (mirrors test_commit_gate.py:30-39)
# ---------------------------------------------------------------------------


def _git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / ".gitignore").write_text(".knowledge/\n.index/\n")
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    return tmp_path


# ---------------------------------------------------------------------------
# Step 1a: read-tier server exposes EXACTLY the read allowlist
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_read_tier_server_exact_tool_set():
    """The read-tier server exposes exactly read_tier_tool_names() — exact equality,
    not subset. A superset would mean a build tool leaked onto the read mount."""

    async def _run() -> tuple[frozenset[str], frozenset[str]]:
        srv = build_read_tier_server()
        async with create_connected_server_and_client_session(srv) as client:
            result = await client.list_tools()
            actual = frozenset(t.name for t in result.tools)
        expected = read_tier_tool_names()
        return actual, expected

    actual, expected = asyncio.run(_run())

    assert actual == expected, (
        f"read-tier tool set mismatch.\n"
        f"  extra (leaked build tools): {sorted(actual - expected)}\n"
        f"  missing: {sorted(expected - actual)}"
    )


# ---------------------------------------------------------------------------
# Step 1b: negative control — build server HAS the build-only tools
# (proves the read server FILTERS them rather than the tools not existing)
# ---------------------------------------------------------------------------

_BUILD_ONLY_TOOLS = frozenset(
    {"wiki_deposit", "wiki_remediate"}
)
"""Subset of tools that must be present on the BUILD server and absent on READ.

These are the MCP-exposed build-tier tools. commit-worker and policy-edit are
CLI_ONLY (not registered on ANY MCP server), so they cannot appear in list_tools.
The negative-control purpose is satisfied by asserting that the tools that DO
exist on the build server (deposit, remediate) are absent on the read server.
"""


@pytest.mark.e2e
def test_build_server_has_build_only_tools_negative_control():
    """Negative control: the BUILD server registers the build-only MCP tools.

    This proves the read-tier filter is doing real work — the tools exist on the
    build mount, so their absence on the read mount is not an artifact of them
    simply never being registered anywhere.
    """

    async def _run() -> frozenset[str]:
        async with create_connected_server_and_client_session(mcp_server.mcp) as client:
            result = await client.list_tools()
            return frozenset(t.name for t in result.tools)

    build_tools = asyncio.run(_run())

    for name in _BUILD_ONLY_TOOLS:
        assert name in build_tools, (
            f"Expected build tool {name!r} to be registered on the build server "
            f"(proving the read server filters it rather than it not existing). "
            f"Build tools present: {sorted(build_tools)}"
        )

    # Confirm same tools absent from read server — closes the proof
    read_tools = read_tier_tool_names()
    for name in _BUILD_ONLY_TOOLS:
        assert name not in read_tools, (
            f"Build tool {name!r} found in read allowlist — read server not filtering"
        )


# ---------------------------------------------------------------------------
# Step 2: MCP deposit round-trip — call_tool → run_worker → committed on disk
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_mcp_deposit_round_trip_commits_page(repo: Path, monkeypatch: pytest.MonkeyPatch):
    """Deposit a concept page via the build MCP server, then drain the queue with
    run_worker(once=True) and assert the page is committed to disk and git.

    This drives the real MCP protocol path, not the Python deposit() fn directly.
    """
    from gateway.intent_queue import IntentQueue
    from gateway.ops.committer import run_worker

    payload = {
        "page_type": "concept",
        "title": "Test Concept MCP E2E",
        "body": "## Overview\nA concept page written via the MCP surface.\n",
        # No domains — avoids quarantine (no policy.yaml required).
        # durable=False — no [[sources/...]] wikilink required.
        "durable": False,
    }
    identity = {"agent": "e2e-test"}

    async def _deposit() -> dict:
        async with create_connected_server_and_client_session(mcp_server.mcp) as client:
            result = await client.call_tool(
                "wiki_deposit",
                {"payload": payload, "identity": identity},
            )
            # result.content is a list of TextContent; parse the first item
            text = result.content[0].text
            return json.loads(text)

    receipt = asyncio.run(_deposit())

    assert receipt["success"], f"deposit failed: {receipt}"
    assert receipt["disposition"] == "queued", receipt
    intent_id = receipt["intent_id"]
    assert intent_id, "no intent_id in receipt"

    # Drain the queue — run_worker(once=True) claims → authors → commits
    q = IntentQueue()
    run_worker(once=True, queue=q)

    # Assert the page is committed to disk
    expected_slug = "test-concept-mcp-e2e"
    page_path = repo / "wiki" / "concepts" / f"{expected_slug}.md"
    assert page_path.exists(), (
        f"Expected committed page at {page_path} but it does not exist. "
        f"Intent id was {intent_id}. Queue depth: {q.depth()}"
    )
    content = page_path.read_text()
    assert "Test Concept MCP E2E" in content, f"title missing from committed page: {content[:300]}"

    # Assert the commit carries the provenance trailer stamped by CommitGate
    latest_msg = _git(repo, "log", "-1", "--format=%B").stdout
    assert "Intent-Id:" in latest_msg, (
        f"Latest commit does not carry an Intent-Id: trailer — "
        f"CommitGate did not record provenance.\nCommit message:\n{latest_msg}"
    )
    # Also verify HEAD advanced past seed
    commits = _git(repo, "log", "--oneline").stdout.strip().splitlines()
    assert len(commits) >= 2, f"Expected at least 2 commits (seed + deposit), got: {commits}"


# ---------------------------------------------------------------------------
# #3 — read-tier carry-forward: an agent reads its OWN just-committed write
# THROUGH the real read-tier MCP mount (not the CLI/op path).
# ---------------------------------------------------------------------------
# This is the loop the deterministic harness substitutes for: deposit (build
# tier call_tool) → commit (run_worker) → read-your-writes via the read-tier
# server call_tool. Existing e2e reads via cli.main(["retrieve", ...]); none
# drives a READ op through build_read_tier_server().


@pytest.mark.e2e
def test_read_tier_carry_forward_reads_own_committed_write(
    repo: Path, monkeypatch: pytest.MonkeyPatch
):
    """deposit (build mount) → drain → retrieve THROUGH the read-tier mount.

    Negative control: before the drain, the read-tier retrieve must NOT surface
    the page — proving the assertion tests the COMMIT, not the enqueue.
    """
    from gateway.intent_queue import IntentQueue
    from gateway.ops.committer import run_worker

    title = "Carryforward Probe Entity"
    slug = "carryforward-probe-entity"
    payload = {
        "page_type": "concept",
        "title": title,
        "body": "## Overview\nA page deposited via the build mount for carry-forward.\n",
        "durable": False,
    }
    identity = {"agent": "e2e-carryforward"}

    async def _retrieve_via_read_tier(query: str) -> str:
        async with create_connected_server_and_client_session(
            build_read_tier_server()
        ) as client:
            result = await client.call_tool("wiki_retrieve", {"query": query})
            return result.content[0].text

    # --- Negative control: nothing committed yet → read-tier must not surface it.
    # Assert on the SLUG, not the title: wiki_retrieve echoes the query string in
    # its summary, so the title would match even with zero results; the slug only
    # appears when the page itself is retrieved.
    before = asyncio.run(_retrieve_via_read_tier(title))
    assert slug not in before, (
        f"read-tier surfaced the page before it was committed; output={before[:300]}"
    )

    # --- Deposit through the BUILD mount (the privileged write surface).
    async def _deposit() -> dict:
        async with create_connected_server_and_client_session(mcp_server.mcp) as client:
            result = await client.call_tool(
                "wiki_deposit", {"payload": payload, "identity": identity}
            )
            return json.loads(result.content[0].text)

    receipt = asyncio.run(_deposit())
    assert receipt["success"] and receipt["disposition"] == "queued", receipt

    # --- Commit it.
    run_worker(once=True, queue=IntentQueue())
    assert (repo / "wiki" / "concepts" / f"{slug}.md").exists(), "page not committed"

    # --- Carry-forward: the SAME agent reads its own write THROUGH the read mount.
    # The slug appears only if the page itself is in the retrieved block (the
    # echoed query carries the title, never the hyphenated slug).
    after = asyncio.run(_retrieve_via_read_tier(title))
    assert slug in after, (
        f"read-tier mount did not surface the just-committed page (read-your-writes "
        f"failed across the tier boundary); output={after[:500]}"
    )


@pytest.mark.e2e
def test_read_tier_mount_cannot_deposit(repo: Path):
    """The read-tier mount must not expose a write path: calling wiki_deposit on
    it is rejected (isError) and enqueues nothing — the boundary holds at call
    time, not merely in the advertised tool set."""
    from gateway.intent_queue import IntentQueue

    async def _attempt_write():
        async with create_connected_server_and_client_session(
            build_read_tier_server()
        ) as client:
            return await client.call_tool(
                "wiki_deposit",
                {"payload": {"page_type": "concept", "title": "X"}, "identity": {}},
            )

    result = asyncio.run(_attempt_write())
    assert getattr(result, "isError", False) is True, (
        "read-tier mount did not reject wiki_deposit as an error result"
    )
    assert IntentQueue().depth() == 0, (
        "read-tier wiki_deposit ENQUEUED an intent — write boundary breached"
    )
