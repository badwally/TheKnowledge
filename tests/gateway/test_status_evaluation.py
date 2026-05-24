"""Tests for M50 evaluation scores block in `wiki status`."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway.evaluate.persistence import append_to_trend
from gateway.evaluate.schema import EvalRunSummary
from gateway.ops.status import status


def _summary(domain: str, timestamp: str, mean_score: float) -> EvalRunSummary:
    return EvalRunSummary(
        domain=domain,
        timestamp=timestamp,
        n_questions=10,
        mean_score=mean_score,
        results=[],
    )


def test_status_shows_evaluation_block_per_domain_with_trend(kb_root: Path):
    # Seed two domains: alpha-d with two runs, beta-d with one run.
    append_to_trend(_summary("alpha-d", "2026-05-24T10-00-00Z", 0.6))
    append_to_trend(_summary("alpha-d", "2026-05-25T10-00-00Z", 0.7))
    append_to_trend(_summary("beta-d", "2026-05-25T10-00-00Z", 0.85))

    result = status()
    text = result.summary

    assert "alpha-d" in text
    assert "beta-d" in text

    # alpha-d: delta from 0.6 to 0.7 = +0.10
    assert "+0.10" in text

    # beta-d: only one run → initial
    assert "initial" in text


def test_status_evaluation_block_empty_when_no_domains(kb_root: Path):
    result = status()
    text = result.summary

    assert "Evaluation scores" in text
    assert "none yet" in text.lower()


def test_status_evaluation_block_shows_correct_mean_score(kb_root: Path):
    append_to_trend(_summary("glp1", "2026-05-24T10-00-00Z", 0.823))

    result = status()
    text = result.summary

    assert "glp1" in text
    assert "0.823" in text
    assert "initial" in text


def test_status_evaluation_block_negative_delta(kb_root: Path):
    append_to_trend(_summary("condo", "2026-05-24T10-00-00Z", 0.8))
    append_to_trend(_summary("condo", "2026-05-25T10-00-00Z", 0.6))

    result = status()
    text = result.summary

    assert "condo" in text
    assert "-0.20" in text


def test_status_evaluation_domains_sorted_alphabetically(kb_root: Path):
    append_to_trend(_summary("zzz-domain", "2026-05-25T10-00-00Z", 0.5))
    append_to_trend(_summary("aaa-domain", "2026-05-25T10-00-00Z", 0.9))

    result = status()
    text = result.summary

    # aaa-domain must appear before zzz-domain
    idx_aaa = text.index("aaa-domain")
    idx_zzz = text.index("zzz-domain")
    assert idx_aaa < idx_zzz


def test_status_evaluation_skips_domains_with_no_trend_rows(kb_root: Path):
    """A domain dir that exists but has no trend.csv rows should be silently skipped."""
    # Create the domain dir without a trend.csv
    from gateway.evaluate.persistence import eval_dir_for
    eval_dir_for("empty-domain").mkdir(parents=True, exist_ok=True)

    result = status()
    text = result.summary

    assert "empty-domain" not in text
    assert "none yet" in text.lower()
