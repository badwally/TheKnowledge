"""Tests for evaluation runner (M50 Phase E)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from gateway import frontmatter as fm
from gateway.evaluate.runner import run_evaluate, NoGoldensError
from gateway.evaluate.schema import EvalResult, Golden, save_goldens
from gateway.evaluate.persistence import goldens_path_for


def _seed_goldens(domain: str = "test-domain"):
    save_goldens(goldens_path_for(domain), [
        Golden(id="q01", question="Q1?", must_cite=["a"], must_assert=["A"], must_not_assert=[]),
        Golden(id="q02", question="Q2?", must_cite=["b"], must_assert=["B"], must_not_assert=[]),
    ])


def _seed_minimal_wiki(kb_root: Path, domain: str = "test-domain"):
    page = kb_root / "wiki" / "synthesis" / "minimal.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {"type": "synthesis", "slug": "minimal", "title": "m",
         "domains": [domain], "synthesizes": []},
        "# minimal\n\nSome content.\n",
    ))


def test_run_evaluate_dispatches_one_call_per_golden(kb_root):
    _seed_goldens()
    _seed_minimal_wiki(kb_root)

    fake_judge = MagicMock()
    fake_judge.score.side_effect = [
        EvalResult(golden_id="q01", question="Q1?", score=0.9,
                   input_tokens=1000, cache_read_tokens=500),
        EvalResult(golden_id="q02", question="Q2?", score=0.6,
                   input_tokens=1000, cache_read_tokens=500),
    ]

    with patch("gateway.evaluate.runner.Judge", return_value=fake_judge):
        summary = run_evaluate("test-domain")

    assert summary.n_questions == 2
    assert summary.mean_score == pytest.approx(0.75)
    assert fake_judge.score.call_count == 2
    assert summary.total_input_tokens == 2000
    assert summary.total_cache_read_tokens == 1000


def test_run_evaluate_writes_run_yaml_and_appends_trend(kb_root):
    _seed_goldens()
    _seed_minimal_wiki(kb_root)

    fake_judge = MagicMock()
    fake_judge.score.return_value = EvalResult(
        golden_id="q01", question="Q1?", score=0.9,
        input_tokens=100, cache_read_tokens=50,
    )
    with patch("gateway.evaluate.runner.Judge", return_value=fake_judge):
        run_evaluate("test-domain", limit=1)

    runs = list((kb_root / ".knowledge" / "eval" / "test-domain" / "runs").glob("*.yaml"))
    assert len(runs) == 1
    trend = kb_root / ".knowledge" / "eval" / "test-domain" / "trend.csv"
    assert trend.exists()


def test_run_evaluate_limit_caps_question_count(kb_root):
    _seed_goldens()
    _seed_minimal_wiki(kb_root)

    fake_judge = MagicMock()
    fake_judge.score.return_value = EvalResult(
        golden_id="q01", question="Q1?", score=0.5,
    )
    with patch("gateway.evaluate.runner.Judge", return_value=fake_judge):
        summary = run_evaluate("test-domain", limit=1)
    assert summary.n_questions == 1
    assert fake_judge.score.call_count == 1


def test_run_evaluate_missing_goldens_raises(kb_root):
    with pytest.raises(NoGoldensError):
        run_evaluate("nonexistent-domain")


def test_run_evaluate_judge_instantiated_once_per_run(kb_root):
    """One Judge instance per run so cache_control on the system prompt
    accrues benefit across all questions within the 5-min TTL."""
    _seed_goldens()
    _seed_minimal_wiki(kb_root)

    fake_judge = MagicMock()
    fake_judge.score.return_value = EvalResult(
        golden_id="q01", question="Q1?", score=0.5,
    )
    judge_class_mock = MagicMock(return_value=fake_judge)
    with patch("gateway.evaluate.runner.Judge", judge_class_mock):
        run_evaluate("test-domain")
    # Judge class was instantiated exactly once
    assert judge_class_mock.call_count == 1
