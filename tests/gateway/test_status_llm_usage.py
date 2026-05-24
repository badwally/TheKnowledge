"""Tests for K5 LLM usage block in `wiki status` (M47)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from gateway import log as log_mod
from gateway import paths
from gateway.llm.telemetry import CallResult
from gateway.ops.status import _aggregate_llm_usage, status


def _sample_call(**overrides) -> CallResult:
    defaults = dict(
        text="ok",
        input_tokens=100,
        output_tokens=50,
        cache_read_tokens=10,
        cache_creation_tokens=5,
        model="claude-haiku-4-5-20251001",
        stop_reason="end_turn",
        duration_ms=1000,
        total_cost_usd=0.0001,
    )
    defaults.update(overrides)
    return CallResult(**defaults)


def test_aggregate_empty_log_returns_empty():
    assert _aggregate_llm_usage("", window_days=7) == {}


def test_aggregate_one_llm_call_one_op(kb_root: Path):
    log_mod.log_llm_call("filter", _sample_call())
    log_text = paths.log_path().read_text()
    buckets = _aggregate_llm_usage(log_text, window_days=7)
    assert "filter" in buckets
    b = buckets["filter"]
    assert b.calls == 1
    assert b.input_tokens == 100
    assert b.output_tokens == 50
    assert b.cache_read_tokens == 10
    assert b.cache_creation_tokens == 5
    assert b.duration_ms == 1000


def test_aggregate_multiple_calls_same_op_sum(kb_root: Path):
    for _ in range(3):
        log_mod.log_llm_call("filter", _sample_call(input_tokens=100, output_tokens=20))
    log_text = paths.log_path().read_text()
    buckets = _aggregate_llm_usage(log_text, window_days=7)
    assert buckets["filter"].calls == 3
    assert buckets["filter"].input_tokens == 300
    assert buckets["filter"].output_tokens == 60


def test_aggregate_separates_by_op(kb_root: Path):
    log_mod.log_llm_call("filter", _sample_call())
    log_mod.log_llm_call("plan_authorship", _sample_call(input_tokens=5000))
    log_mod.log_llm_call("vlm", _sample_call())
    log_text = paths.log_path().read_text()
    buckets = _aggregate_llm_usage(log_text, window_days=7)
    assert set(buckets.keys()) == {"filter", "plan_authorship", "vlm"}
    assert buckets["plan_authorship"].input_tokens == 5000


def test_aggregate_filters_old_entries_outside_window():
    """Entries older than `window_days` get excluded."""
    # Manually craft a log with two entries: one recent, one ancient.
    ancient = (
        "## [2020-01-01T00:00:00Z] llm-call | op=filter | model=foo | "
        "in_tokens=1 | out_tokens=1 | cache_read=0 | cache_creation=0 | "
        "duration_ms=10 | cost_usd=0.0\n"
    )
    recent_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    recent = (
        f"## [{recent_ts}] llm-call | op=filter | model=foo | "
        f"in_tokens=2 | out_tokens=2 | cache_read=0 | cache_creation=0 | "
        f"duration_ms=10 | cost_usd=0.0\n"
    )
    log_text = ancient + recent
    buckets = _aggregate_llm_usage(log_text, window_days=7)
    # Only the recent one counts.
    assert buckets["filter"].calls == 1
    assert buckets["filter"].input_tokens == 2


def test_aggregate_ignores_non_llm_call_lines(kb_root: Path):
    log_mod.append("ingest", {"id": "yt-abc"}, summary="ingested")
    log_mod.log_llm_call("filter", _sample_call())
    log_mod.append("query", {"q": "test"}, summary="answered")
    log_text = paths.log_path().read_text()
    buckets = _aggregate_llm_usage(log_text, window_days=7)
    # Only the one llm-call counts; ingest/query lines ignored.
    assert sum(b.calls for b in buckets.values()) == 1


def test_status_renders_llm_block_when_entries_present(kb_root: Path):
    log_mod.log_llm_call("filter", _sample_call(input_tokens=200, output_tokens=40))
    log_mod.log_llm_call("plan_authorship", _sample_call(input_tokens=5000, output_tokens=1000))
    result = status()
    assert "LLM usage (last 7 days)" in result.summary
    assert "2 calls" in result.summary
    # tokens shown with commas
    assert "in=5,200" in result.summary
    assert "out=1,040" in result.summary
    assert "by op:" in result.summary
    assert "filter=1" in result.summary
    assert "plan_authorship=1" in result.summary


def test_status_omits_llm_block_when_no_entries(kb_root: Path):
    result = status()
    assert "LLM usage" not in result.summary


def test_status_with_cost_flag_includes_cost_line(kb_root: Path):
    log_mod.log_llm_call("filter", _sample_call(total_cost_usd=0.0003))
    log_mod.log_llm_call("filter", _sample_call(total_cost_usd=0.0007))
    result = status(with_cost=True)
    assert "reported cost" in result.summary
    # 0.0003 + 0.0007 = 0.0010 → formatted as $0.0010
    assert "0.0010" in result.summary


def test_status_without_cost_flag_omits_cost_line(kb_root: Path):
    log_mod.log_llm_call("filter", _sample_call(total_cost_usd=0.5))
    result = status(with_cost=False)
    assert "reported cost" not in result.summary
