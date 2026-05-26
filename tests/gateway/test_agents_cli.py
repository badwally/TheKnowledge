"""Tests for wiki agents CLI + run_inbox_triage_batch (A1 — M60)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.agents.inbox_triage import run_inbox_triage_batch, BatchTriageResult


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _make_raw_source(
    kb_root: Path,
    source_id: str,
    *,
    source_type: str = "web",
    domains: list[str] | None = None,
    with_filter: bool = False,
) -> Path:
    p = kb_root / "raw" / source_type / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front: dict = {"id": source_id, "type": source_type, "title": f"Title {source_id}"}
    if domains:
        front["domains"] = domains
    if with_filter:
        front["filter"] = {"score": 0.9, "decision": "include"}
    p.write_text(fm.serialize(front, f"# {source_id}\n\nBody.\n"))
    return p


# ---------------------------------------------------------------------------
# run_inbox_triage_batch
# ---------------------------------------------------------------------------


def test_batch_skips_already_filtered_sources(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-001", with_filter=True)
    _make_raw_source(kb_root, "web-002", with_filter=True)

    with patch("gateway.agents.inbox_triage.run_triage") as mock_triage:
        result = run_inbox_triage_batch()

    mock_triage.assert_not_called()
    assert result.skipped == 2
    assert result.processed == 0
    assert result.failed == 0


def test_batch_processes_unfiltered_sources(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-100")
    _make_raw_source(kb_root, "web-101")

    from gateway.agents.inbox_triage import TriageResult
    fake_result = TriageResult(source_id="web-100")

    with patch("gateway.agents.inbox_triage.run_triage", return_value=fake_result) as mock_triage:
        result = run_inbox_triage_batch()

    assert mock_triage.call_count == 2
    assert result.processed == 2
    assert result.skipped == 0
    assert result.failed == 0


def test_batch_mixed_sources(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-200", with_filter=True)   # skipped
    _make_raw_source(kb_root, "web-201", with_filter=False)  # processed

    from gateway.agents.inbox_triage import TriageResult
    fake = TriageResult(source_id="web-201")

    with patch("gateway.agents.inbox_triage.run_triage", return_value=fake):
        result = run_inbox_triage_batch()

    assert result.processed == 1
    assert result.skipped == 1


def test_batch_handles_empty_raw_dir(kb_root: Path) -> None:
    result = run_inbox_triage_batch()
    assert result.processed == 0
    assert result.skipped == 0
    assert result.failed == 0


def test_batch_failure_counted_not_raised(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-300")

    with patch("gateway.agents.inbox_triage.run_triage", side_effect=RuntimeError("boom")):
        result = run_inbox_triage_batch()

    assert result.failed == 1
    assert result.processed == 0


# ---------------------------------------------------------------------------
# wiki agents CLI — run inbox-triage
# ---------------------------------------------------------------------------


def test_cli_agents_run_inbox_triage(kb_root: Path) -> None:
    from gateway.cli import main
    import sys

    with patch("gateway.agents.inbox_triage.run_inbox_triage_batch",
               return_value=BatchTriageResult(processed=2, skipped=5)):
        sys.argv = ["wiki", "agents", "run", "inbox-triage"]
        rc = main()

    assert rc == 0


def test_cli_agents_run_draft_closer(kb_root: Path) -> None:
    from gateway.cli import main
    from gateway.agents.draft_closer import DraftCloserResult
    import sys

    fake = DraftCloserResult(pages_finalized=1, pages_escalated=0, pages_skipped=3)
    with patch("gateway.agents.draft_closer.run_draft_closer", return_value=fake):
        sys.argv = ["wiki", "agents", "run", "draft-closer"]
        rc = main()

    assert rc == 0


def test_cli_agents_run_unknown_name_fails(kb_root: Path) -> None:
    from gateway.cli import main
    import sys

    sys.argv = ["wiki", "agents", "run", "nope"]
    # argparse will error before our handler — just ensure it exits non-zero
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code != 0
