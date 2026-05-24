"""Tests for eval persistence (M50 Phase D)."""

from __future__ import annotations

from pathlib import Path

from gateway.evaluate.persistence import (
    write_run,
    append_to_trend,
    read_trend,
    runs_dir_for,
    trend_path_for,
    goldens_path_for,
)
from gateway.evaluate.schema import EvalResult, EvalRunSummary


def _make_summary(domain: str = "test-domain", ts: str = "2026-05-24T22-00-00Z",
                  mean: float = 0.75) -> EvalRunSummary:
    return EvalRunSummary(
        domain=domain,
        timestamp=ts,
        n_questions=2,
        mean_score=mean,
        results=[
            EvalResult(golden_id="q01", question="Q1?", score=0.8,
                       cite_hits=["a"], cite_misses=["b"]),
            EvalResult(golden_id="q02", question="Q2?", score=0.7),
        ],
        total_input_tokens=10000,
        total_output_tokens=400,
        total_cache_read_tokens=8000,
    )


def test_write_run_creates_yaml_under_runs_dir(kb_root):
    summary = _make_summary()
    path = write_run(summary)
    assert path == runs_dir_for("test-domain") / "2026-05-24T22-00-00Z.yaml"
    assert path.exists()
    text = path.read_text()
    assert "q01" in text
    assert "mean_score: 0.75" in text


def test_append_to_trend_creates_csv_with_header_on_first_call(kb_root):
    summary = _make_summary()
    append_to_trend(summary)
    csv_path = trend_path_for("test-domain")
    assert csv_path.exists()
    lines = csv_path.read_text().strip().split("\n")
    assert lines[0].startswith("timestamp,")
    assert "2026-05-24T22-00-00Z" in lines[1]
    assert "0.75" in lines[1]


def test_append_to_trend_appends_subsequent_rows(kb_root):
    append_to_trend(_make_summary(ts="2026-05-24T22-00-00Z", mean=0.75))
    append_to_trend(_make_summary(ts="2026-05-25T22-00-00Z", mean=0.82))
    rows = read_trend("test-domain")
    assert len(rows) == 2
    assert rows[1]["timestamp"] == "2026-05-25T22-00-00Z"
    assert float(rows[1]["mean_score"]) == 0.82


def test_read_trend_returns_empty_when_file_absent(kb_root):
    rows = read_trend("never-evaluated-domain")
    assert rows == []


def test_goldens_path_for_returns_expected_location(kb_root):
    path = goldens_path_for("d1")
    assert path == kb_root / ".knowledge" / "eval" / "d1" / "goldens.yaml"
