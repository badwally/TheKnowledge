"""Tests for AGT-14: wiki agent-log + daily digest."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import events, paths
from gateway.ops import agent_log


# ── helpers ───────────────────────────────────────────────────────────────────

def _emit_n(kb_root: Path, n: int, *, event_type: str = "ingest.complete", agent: str = "pipeline") -> list[str]:
    ids = []
    for i in range(n):
        eid = events.emit(event_type, payload={"i": i}, agent=agent, correlation_id=f"c{i}")
        ids.append(eid)
    return ids


# ── agent_log.aggregate ───────────────────────────────────────────────────────

def test_aggregate_counts_per_agent(kb_root: Path) -> None:
    _emit_n(kb_root, 3, agent="pipeline")
    _emit_n(kb_root, 2, agent="poller")
    result = agent_log.aggregate(since_hours=24)
    assert result["pipeline"]["count"] == 3
    assert result["poller"]["count"] == 2


def test_aggregate_empty_window_returns_empty(kb_root: Path) -> None:
    _emit_n(kb_root, 2, agent="pipeline")
    result = agent_log.aggregate(since_hours=0)
    assert result == {}


def test_aggregate_top_payloads_capped_at_5(kb_root: Path) -> None:
    _emit_n(kb_root, 8, agent="pipeline")
    result = agent_log.aggregate(since_hours=24)
    assert len(result["pipeline"]["top_payloads"]) <= 5


def test_aggregate_since_hours_48(kb_root: Path) -> None:
    _emit_n(kb_root, 3, agent="pipeline")
    result = agent_log.aggregate(since_hours=48)
    assert result["pipeline"]["count"] == 3


def test_aggregate_groups_by_agent(kb_root: Path) -> None:
    for et in ("ingest.complete", "filter.scored", "ingest.complete"):
        events.emit(et, payload={}, agent="multi", correlation_id="c")
    result = agent_log.aggregate(since_hours=24)
    assert result["multi"]["count"] == 3


# ── CLI: wiki agent-log ───────────────────────────────────────────────────────

def test_cli_agent_log_subcommand_exists(kb_root: Path) -> None:
    from gateway.cli import build_parser
    parser = build_parser()
    ns = parser.parse_args(["agent-log", "--since", "24h"])
    assert ns.subcommand == "agent-log"
    assert ns.since == "24h"


def test_cli_agent_log_since_options(kb_root: Path) -> None:
    from gateway.cli import build_parser
    for window in ("24h", "48h", "7d"):
        ns = build_parser().parse_args(["agent-log", "--since", window])
        assert ns.since == window


def test_cli_agent_log_default_since_is_24h(kb_root: Path) -> None:
    from gateway.cli import build_parser
    ns = build_parser().parse_args(["agent-log"])
    assert ns.since == "24h"


# ── daily digest scheduler entry ─────────────────────────────────────────────

def test_digest_scheduler_entry_exists() -> None:
    from gateway.scheduler import load_schedule
    import os
    import yaml
    sched_path = paths.knowledge_internal() / "schedule.yaml"
    # Check the constant/default schedule config includes agent-digest
    # The AGT-14 spec writes a constant entry — check the registered entry in scheduler module
    from gateway.ops import agent_log as al
    assert hasattr(al, "DIGEST_SCHEDULE_ENTRY")
    entry = al.DIGEST_SCHEDULE_ENTRY
    assert entry["name"] == "agent-digest"
    assert "7" in entry["cron"] or "0 7" in entry["cron"]


# ── build_digest_page ─────────────────────────────────────────────────────────

def test_build_digest_page_returns_draft_markdown(kb_root: Path) -> None:
    _emit_n(kb_root, 2, agent="pipeline")
    page = agent_log.build_digest_page(date_str="2026-05-25")
    assert "draft: true" in page
    assert "agent-digest" in page
    assert "pipeline" in page


def test_build_digest_page_no_events_still_valid(kb_root: Path) -> None:
    page = agent_log.build_digest_page(date_str="2026-05-25")
    assert "draft: true" in page
