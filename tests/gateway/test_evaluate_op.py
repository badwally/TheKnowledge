"""Tests for the wiki evaluate gateway op (M50 Phase F)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from gateway.evaluate.persistence import goldens_path_for
from gateway.evaluate.schema import Golden, EvalResult, save_goldens
from gateway.ops.evaluate_op import evaluate_op


def test_evaluate_op_scaffold_creates_template(kb_root):
    result = evaluate_op(scaffold="new-domain")
    assert result.success
    assert goldens_path_for("new-domain").exists()


def test_evaluate_op_scaffold_refuses_overwrite(kb_root):
    evaluate_op(scaffold="d1")
    result = evaluate_op(scaffold="d1")
    assert not result.success
    assert "already exists" in (result.errors[0] or "").lower()


def test_evaluate_op_requires_domain_when_no_scaffold(kb_root):
    result = evaluate_op()
    assert not result.success
    assert "domain" in (result.errors[0]).lower()


def test_evaluate_op_runs_and_returns_mean_score(kb_root):
    save_goldens(goldens_path_for("test-domain"), [
        Golden(id="q01", question="Q?", must_cite=[], must_assert=[], must_not_assert=[]),
    ])
    fake_judge = MagicMock()
    fake_judge.score.return_value = EvalResult(
        golden_id="q01", question="Q?", score=0.5,
    )
    with patch("gateway.evaluate.runner.Judge", return_value=fake_judge):
        result = evaluate_op(domain="test-domain")
    assert result.success
    assert "0.500" in result.summary


def test_evaluate_op_missing_goldens_returns_error(kb_root):
    result = evaluate_op(domain="never-seeded")
    assert not result.success
    assert "no goldens" in (result.errors[0]).lower() or "scaffold" in (result.errors[0]).lower()
