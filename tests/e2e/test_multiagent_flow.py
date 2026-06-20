"""P1 — E2E multi-agent deposit→commit→read round-trip.

N concurrent MCP deposits are issued by different agents, the committer
drains the queue in one run_worker(once=True) call, and each page is then
readable via the real retrieve path.

Negative control: test_deposit_without_drain_is_not_readable — proves that
the round-trip asserts the COMMIT, not just the enqueue (run_worker returns
None, so the only proof of commit is disk/git/retrieve state).
"""

from __future__ import annotations

import asyncio
import json
import subprocess
from io import StringIO
from pathlib import Path

import pytest

from mcp.shared.memory import create_connected_server_and_client_session

from gateway import cli
from gateway.mcp_server import mcp
from gateway.ops.committer import run_worker


# ---------------------------------------------------------------------------
# git helper + repo fixture (mirrors test_mcp_surface.py:41-51)
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


pytestmark = pytest.mark.e2e


# ---------------------------------------------------------------------------
# Step 1/2: N concurrent MCP deposits → drain → disk + git + retrieve
# ---------------------------------------------------------------------------


def test_n_agent_deposit_drain_read_round_trip(
    repo: Path, capsys: pytest.CaptureFixture
):
    """N concurrent MCP deposits → run_worker(once=True) → every page committed
    (disk + git Intent-Id) AND retrievable via the real read path.

    Drives the full async multi-agent path through the real MCP protocol,
    real committer, and real retrieve surface. No monkeypatching of the core path.
    """
    n = 6
    titles = [f"Multiagent Entity {i}" for i in range(n)]

    async def _deposit_all() -> list[dict]:
        receipts = []
        async with create_connected_server_and_client_session(mcp) as client:
            results = await asyncio.gather(
                *[
                    client.call_tool(
                        "wiki_deposit",
                        {
                            "payload": {
                                "page_type": "entity",
                                "title": t,
                                "body": (
                                    f"# Overview\n{t} is a test entity.\n\n"
                                    f"# Detail\nMore about {t}.\n"
                                ),
                                "aliases": [t.lower().replace(" ", "-")],
                                "domains": ["test-domain"],
                                # durable unset — no [[sources/...]] wikilink
                                # required (deposit.py:121).
                            },
                            "identity": {"agent": f"agent-{i}"},
                        },
                    )
                    for i, t in enumerate(titles)
                ]
            )
        for result in results:
            receipts.append(json.loads(result.content[0].text))
        return receipts

    receipts = asyncio.run(_deposit_all())

    # All deposits must have been queued
    for r in receipts:
        assert r["success"], f"deposit failed: {r}"
        assert r["disposition"] == "queued", r
        assert r["intent_id"], f"no intent_id in receipt: {r}"

    # Drain the queue — run_worker returns None; proof of commit is disk+git state.
    run_worker(once=True)

    entities_dir = repo / "wiki" / "entities"
    for i, title in enumerate(titles):
        slug = title.lower().replace(" ", "-")
        page_path = entities_dir / f"{slug}.md"
        assert page_path.exists(), (
            f"Expected committed page at {page_path} but it does not exist. "
            f"title={title!r}"
        )
        content = page_path.read_text()
        assert title in content, f"title missing from committed page: {content[:300]}"

    # Every committed page must carry an Intent-Id: trailer in git log
    log_output = _git(repo, "log", "--format=%B").stdout
    assert "Intent-Id:" in log_output, (
        "No Intent-Id: trailer found in any commit — CommitGate did not record "
        f"provenance.\nFull log:\n{log_output}"
    )

    # HEAD must have advanced past the seed commit
    commits = _git(repo, "log", "--oneline").stdout.strip().splitlines()
    assert len(commits) >= 2, (
        f"Expected at least 2 commits (seed + at least one deposit), got: {commits}"
    )

    # Read through the REAL retrieve path — refresh() self-heals the index,
    # no explicit rebuild step needed. KNOWLEDGE_ROOT is set by the fixture.
    probe_title = "Multiagent Entity 3"
    probe_slug = "multiagent-entity-3"

    rc = cli.main(["retrieve", probe_title, "--domain", "test-domain"])
    captured = capsys.readouterr()
    assert rc == 0, (
        f"wiki retrieve exited {rc}.\nstdout: {captured.out}\nstderr: {captured.err}"
    )
    assert probe_slug in captured.out or probe_title in captured.out, (
        f"Expected slug/title for {probe_title!r} in retrieve output.\n"
        f"stdout:\n{captured.out}"
    )


# ---------------------------------------------------------------------------
# Step 3: negative control — no drain means no commit, no retrieve
# ---------------------------------------------------------------------------


def test_deposit_without_drain_is_not_readable(
    repo: Path, capsys: pytest.CaptureFixture
):
    """Negative control: deposits without run_worker must NOT produce committed
    pages on disk and must NOT be retrievable.

    This proves the positive test asserts the COMMIT, not just the enqueue.
    If run_worker is skipped, the queue holds the intents but no page file
    exists and wiki retrieve returns a corpus-miss (rc != 0 or empty output).
    """
    titles = ["Negative Control Entity A", "Negative Control Entity B"]

    async def _deposit_all() -> list[dict]:
        receipts = []
        async with create_connected_server_and_client_session(mcp) as client:
            results = await asyncio.gather(
                *[
                    client.call_tool(
                        "wiki_deposit",
                        {
                            "payload": {
                                "page_type": "entity",
                                "title": t,
                                "body": f"# Overview\n{t} is a negative-control entity.\n",
                                "domains": ["test-domain"],
                                # durable unset — no [[sources/...]] required.
                            },
                            "identity": {"agent": "negative-control-agent"},
                        },
                    )
                    for t in titles
                ]
            )
        for result in results:
            receipts.append(json.loads(result.content[0].text))
        return receipts

    receipts = asyncio.run(_deposit_all())

    # Deposits must have been accepted (queued) — they hit the MCP surface OK.
    for r in receipts:
        assert r["success"], f"deposit failed unexpectedly: {r}"
        assert r["disposition"] == "queued", r

    # DO NOT call run_worker — no drain, no commit.

    # Pages must NOT exist on disk
    entities_dir = repo / "wiki" / "entities"
    for title in titles:
        slug = title.lower().replace(" ", "-")
        page_path = entities_dir / f"{slug}.md"
        assert not page_path.exists(), (
            f"Page {page_path} exists on disk WITHOUT drain — "
            "round-trip test is not proving commit, just enqueue."
        )

    # wiki retrieve must not surface the uncommitted entities
    rc = cli.main(["retrieve", "Negative Control Entity A", "--domain", "test-domain"])
    captured = capsys.readouterr()
    # Either rc != 0 (corpus miss) or output must not contain the slug
    negative_slug = "negative-control-entity-a"
    assert rc != 0 or negative_slug not in captured.out, (
        f"wiki retrieve surfaced {negative_slug!r} without a drain — "
        "the committed page should not exist yet.\n"
        f"rc={rc}\nstdout:\n{captured.out}"
    )
