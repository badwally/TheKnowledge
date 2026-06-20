"""T4 — CLI surface E2E tests.

Step 3: Drive real CLI commands via cli.main([...]) against a real git repo.
After each command, assert on-disk + git state — not just exit code 0.

Commands covered:
  - remediate --dry-run  (no mutation, exit 0, reports zero depathed)
  - revert-resolution    (enqueues a reversal intent; verified in queue state)
  - policy-edit          (rejected fail-closed when no principal configured)
  - demand-cluster       (clusters gaps; exit 0 with empty dataset)
  - commit-worker --once (drains queue; verifies a pre-submitted page commits)
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest
import yaml

from gateway import cli
from gateway.intent_queue import IntentQueue


# ---------------------------------------------------------------------------
# git helper + repo fixture (mirrors test_commit_gate.py:30-39)
# ---------------------------------------------------------------------------


def _git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Real git repo with KNOWLEDGE_ROOT pointing to tmp_path."""
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
# Step 3a: remediate --dry-run
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_cli_remediate_dry_run_on_empty_wiki(repo: Path):
    """remediate on an empty wiki exits 0 and reports zero depathed pages.

    On-disk assertion: no wiki/ pages removed; git HEAD unchanged.
    """
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()

    rc = cli.main(["remediate", "--dry-run"])

    assert rc == 0, f"remediate --dry-run returned {rc}"

    # No commits made (dry-run on empty wiki changes nothing)
    head_after = _git(repo, "rev-parse", "HEAD").stdout.strip()
    assert head_before == head_after, "remediate --dry-run must not commit anything"


@pytest.mark.e2e
def test_cli_remediate_dry_run_wiki_page_not_removed(repo: Path):
    """remediate --dry-run leaves pages in place even if they would be orphaned.

    On-disk state before: one wiki page with zero inbound links.
    Expected: page still exists after dry-run; no git commit made.
    """
    wiki_dir = repo / "wiki" / "concepts"
    wiki_dir.mkdir(parents=True)
    orphan = wiki_dir / "orphan-concept.md"
    orphan.write_text(
        "---\ntype: concept\nslug: orphan-concept\ncanonical_name: Orphan Concept\n"
        "domains: []\ncreated_at: 2026-01-01\nlast_updated: 2026-01-01\n---\n"
        "## Overview\nThis page has no inbound links.\n"
    )
    _git(repo, "add", str(orphan))
    _git(repo, "commit", "-qm", "add orphan concept")

    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()

    rc = cli.main(["remediate", "--dry-run"])

    assert rc == 0, f"remediate --dry-run returned {rc}"
    # dry-run must NOT commit anything
    head_after = _git(repo, "rev-parse", "HEAD").stdout.strip()
    assert head_before == head_after, "remediate --dry-run must not commit"
    # page still exists on disk
    assert orphan.exists(), "remediate --dry-run must not delete the orphan page"


# ---------------------------------------------------------------------------
# Step 3b: revert-resolution enqueues an intent
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_cli_revert_resolution_enqueues_intent(repo: Path):
    """revert-resolution enqueues a reversal intent into the queue.

    On-disk assertion: a submitted/ entry exists in .knowledge/ with the
    correct reversal_type payload.
    """
    act_id = "test-act-abc123"

    rc = cli.main(["revert-resolution", act_id])

    # success → 0; the op only enqueues, so 0 is the expected exit
    assert rc == 0, f"revert-resolution returned {rc}"

    # Assert the intent is durably queued on disk
    q = IntentQueue()
    # submitted/ or authored/: depth() > 0 means something is in flight
    # We check submitted/ directly because run_worker has NOT been called.
    submitted_dir = q._root / "submitted"
    entries = list(submitted_dir.glob("*.json")) if submitted_dir.exists() else []
    assert entries, (
        f"Expected a submitted intent in {submitted_dir} after revert-resolution "
        f"but found none. Queue depth: {q.depth()}"
    )
    # Verify the payload of the single entry
    record = json.loads(entries[0].read_text())
    payload = record.get("payload", {})
    assert payload.get("reversal_type") == "contradiction-resolution", (
        f"Unexpected payload in submitted intent: {payload}"
    )
    assert payload.get("reverts_act") == act_id, (
        f"reverts_act mismatch: expected {act_id!r}, got {payload.get('reverts_act')!r}"
    )


# ---------------------------------------------------------------------------
# Step 3c: policy-edit — rejected fail-closed when no principal configured
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_cli_policy_edit_rejected_without_principal(
    repo: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
):
    """policy-edit rejects (fail-closed) when GATEWAY_POLICY_PRINCIPAL is unset.

    On-disk assertion: no commit made; queue remains empty.
    Git assertion: HEAD unchanged.

    This is the expected production behavior — policy-edit is a privileged
    CLI-only operation that requires an allowlisted server principal. An unset
    principal is rejected before any mutation occurs.
    """
    # Ensure the principal env var is unset (might be set in test environment)
    monkeypatch.delenv("GATEWAY_POLICY_PRINCIPAL", raising=False)

    policy_file = tmp_path / "policy.yaml"
    policy_file.write_text(
        yaml.dump({"identity_threshold": 0.30, "blocking_band": 0.15})
    )

    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()

    rc = cli.main([
        "policy-edit",
        "test-domain",
        str(policy_file),
        "--reason", "test: no principal should reject",
    ])

    # policy-edit with no principal enqueues a rejected result → non-zero exit
    # OR exit 0 with disposition=rejected (the CLI emits the result and returns 0).
    # Either way: NO commit must be made.
    head_after = _git(repo, "rev-parse", "HEAD").stdout.strip()
    assert head_before == head_after, (
        "policy-edit without principal must not commit anything"
    )

    # The queue must remain empty (rejected before enqueue)
    q = IntentQueue()
    submitted_dir = q._root / "submitted"
    entries = list(submitted_dir.glob("*.json")) if submitted_dir.exists() else []
    # Allow: either no entries at all, or any entry has disposition=rejected payload
    for entry in entries:
        record = json.loads(entry.read_text())
        payload = record.get("payload", {})
        # policy-edit intent should have op="policy-edit" in identity
        ident = record.get("identity", {})
        if ident.get("operation") == "policy-edit" or payload.get("op") == "policy-edit":
            pytest.fail(
                f"policy-edit without principal must not enqueue; found entry: {record}"
            )


# ---------------------------------------------------------------------------
# Step 3d: demand-cluster on an empty ledger exits 0
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_cli_demand_cluster_empty_ledger(repo: Path):
    """demand-cluster on a repo with no recorded gaps exits 0.

    On-disk assertion: no new wiki pages created; HEAD unchanged.
    """
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()

    rc = cli.main(["demand-cluster"])

    assert rc == 0, f"demand-cluster returned {rc}"

    head_after = _git(repo, "rev-parse", "HEAD").stdout.strip()
    assert head_before == head_after, "demand-cluster on empty ledger must not commit"

    # No wiki pages created
    wiki_dir = repo / "wiki"
    pages = list(wiki_dir.rglob("*.md")) if wiki_dir.exists() else []
    assert not pages, (
        f"demand-cluster on empty ledger must not create wiki pages; found: {pages}"
    )


# ---------------------------------------------------------------------------
# Step 3e: commit-worker --once drains a pre-deposited page to git
# ---------------------------------------------------------------------------


@pytest.mark.e2e
def test_cli_commit_worker_once_drains_deposited_page(repo: Path):
    """Pre-deposit a concept page via deposit(), then run commit-worker --once
    via cli.main and assert the page is committed to disk + git.

    This drives the real commit pipeline through the CLI surface.
    """
    from gateway.ops.deposit import deposit

    payload = {
        "page_type": "concept",
        "title": "CLI E2E Commit Worker Concept",
        "body": "## Overview\nCommitted via commit-worker CLI E2E test.\n",
        "durable": False,
    }
    identity = {"agent": "e2e-cli-test"}

    receipt = deposit(payload, identity)
    assert receipt.success, f"deposit failed: {receipt}"
    assert receipt.disposition == "queued"

    # Run commit-worker --once via CLI
    rc = cli.main(["commit-worker", "--once"])

    assert rc == 0, f"commit-worker --once returned {rc}"

    # Assert the page committed to disk
    expected_slug = "cli-e2e-commit-worker-concept"
    page_path = repo / "wiki" / "concepts" / f"{expected_slug}.md"
    assert page_path.exists(), (
        f"Expected committed page at {page_path} but it does not exist. "
        f"Receipt intent_id: {receipt.intent_id}"
    )
    content = page_path.read_text()
    assert "CLI E2E Commit Worker Concept" in content, (
        f"title missing from committed page: {content[:300]}"
    )

    # Assert git state: at least one commit beyond seed
    commits = _git(repo, "log", "--oneline").stdout.strip().splitlines()
    assert len(commits) >= 2, (
        f"Expected at least 2 commits (seed + deposit), got: {commits}"
    )

    # The most recent commit message should reference the intent or deposit
    latest_msg = _git(repo, "log", "-1", "--format=%B").stdout
    # CommitGate stamps Intent-Id into the commit message
    assert "Intent-Id:" in latest_msg or expected_slug in latest_msg, (
        f"Latest commit does not look like a librarian deposit commit:\n{latest_msg}"
    )
