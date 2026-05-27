"""Tests for the wiki evaluate gateway op (M50 Phase F + M101 --all-domains)."""

from __future__ import annotations

from pathlib import Path

import pytest
from unittest.mock import MagicMock, patch

from gateway.evaluate.persistence import domains_with_goldens, goldens_path_for
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


# ---------------------------------------------------------------------------
# M101: --all-domains and domains_with_goldens
# ---------------------------------------------------------------------------


def _fake_judge_for(score: float = 0.5):
    j = MagicMock()
    j.score.return_value = EvalResult(golden_id="q01", question="Q?", score=score)
    return j


def test_domains_with_goldens_returns_all(kb_root: Path) -> None:
    evaluate_op(scaffold="alpha")
    evaluate_op(scaffold="beta")
    domains = domains_with_goldens()
    assert "alpha" in domains
    assert "beta" in domains
    assert domains == sorted(domains)


def test_domains_with_goldens_empty_when_none(kb_root: Path) -> None:
    assert domains_with_goldens() == []


def test_evaluate_op_all_domains_runs_each(kb_root: Path) -> None:
    for slug in ("d1", "d2"):
        save_goldens(goldens_path_for(slug), [
            Golden(id="q01", question="Q?", must_cite=[], must_assert=[], must_not_assert=[]),
        ])
    with patch("gateway.evaluate.runner.Judge", side_effect=[_fake_judge_for(), _fake_judge_for(0.7)]):
        result = evaluate_op(all_domains=True)
    assert result.success
    assert "2/2 domains scored" in result.summary


def test_evaluate_op_all_domains_no_goldens_returns_error(kb_root: Path) -> None:
    result = evaluate_op(all_domains=True)
    assert not result.success
    assert "no domains" in result.errors[0].lower()


def test_evaluate_op_all_domains_partial_failure(kb_root: Path) -> None:
    for slug in ("good", "bad"):
        save_goldens(goldens_path_for(slug), [
            Golden(id="q01", question="Q?", must_cite=[], must_assert=[], must_not_assert=[]),
        ])
    from gateway.evaluate.runner import NoGoldensError

    def _run_side_effect(domain, **kwargs):
        if domain == "bad":
            raise NoGoldensError("simulated failure")
        from unittest.mock import MagicMock as MM
        s = MM()
        s.n_questions = 1
        s.mean_score = 0.5
        s.total_input_tokens = 0
        s.total_cache_read_tokens = 0
        s.timestamp = "2026-01-01T00-00-00Z"
        s.results = []
        s.domain = domain
        return s

    with patch("gateway.ops.evaluate_op.run_evaluate", side_effect=_run_side_effect):
        result = evaluate_op(all_domains=True)
    assert result.success
    assert "1/2" in result.summary
    assert len(result.errors) == 1


def test_cli_evaluate_all_domains_flag() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["evaluate", "--all-domains"])
    assert ns.all_domains is True
    assert ns.domain is None


def test_cli_evaluate_domain_and_all_domains_coexist() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["evaluate", "glp1", "--all-domains"])
    assert ns.domain == "glp1"
    assert ns.all_domains is True


def test_judge_rescues_score_from_malformed_json(kb_root: Path) -> None:
    """Score rescue path: unescaped quote in assertion text must not zero out golden."""
    from gateway.evaluate.judge import Judge
    from gateway.evaluate.schema import Golden

    golden = Golden(id="q01", question="Q?", must_cite=["src1"],
                    must_assert=["fact"], must_not_assert=[])
    # Simulate a response where an unescaped quote breaks JSON parsing
    malformed = '{"score": 0.87, "cite_hits": ["src1"], "assertion_hits": ["it said "hello" to the world"], ...}'

    fake_call = MagicMock()
    fake_call.text = malformed
    fake_call.input_tokens = 10
    fake_call.output_tokens = 5
    fake_call.cache_read_tokens = 0

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = fake_call

    judge = Judge(client=fake_client)
    result = judge.score(golden=golden, wiki_context="ctx")
    assert result.score == pytest.approx(0.87)
    assert "rescued" in result.judge_reasoning


def test_judge_returns_zero_when_no_score_in_malformed_json(kb_root: Path) -> None:
    from gateway.evaluate.judge import Judge
    from gateway.evaluate.schema import Golden

    golden = Golden(id="q01", question="Q?", must_cite=[],
                    must_assert=[], must_not_assert=[])
    fake_call = MagicMock()
    fake_call.text = "completely unparseable {{{ garbage"
    fake_call.input_tokens = 0
    fake_call.output_tokens = 0
    fake_call.cache_read_tokens = 0

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = fake_call

    judge = Judge(client=fake_client)
    result = judge.score(golden=golden, wiki_context="ctx")
    assert result.score == 0.0


def test_evaluate_op_max_chars_passed_to_run_evaluate(kb_root: Path) -> None:
    save_goldens(goldens_path_for("big-domain"), [
        Golden(id="q01", question="Q?", must_cite=[], must_assert=[], must_not_assert=[]),
    ])
    captured: dict = {}

    def _capture(domain, *, limit=None, max_chars=None, client=None):
        captured["max_chars"] = max_chars
        s = MagicMock()
        s.n_questions = 1
        s.mean_score = 0.5
        s.total_input_tokens = 0
        s.total_cache_read_tokens = 0
        s.timestamp = "2026-01-01T00-00-00Z"
        s.results = []
        s.domain = domain
        return s

    with patch("gateway.ops.evaluate_op.run_evaluate", side_effect=_capture):
        result = evaluate_op(domain="big-domain", max_chars=800_000)
    assert result.success
    assert captured["max_chars"] == 800_000


def test_cli_evaluate_max_chars_flag() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["evaluate", "big-domain", "--max-chars", "800000"])
    assert ns.max_chars == 800_000


def test_evaluate_weekly_job_registered() -> None:
    from gateway import scheduler
    jobs = {j.name: j for j in scheduler.load_schedule()}
    assert "evaluate-weekly" in jobs
    job = jobs["evaluate-weekly"]
    assert job.command == "wiki evaluate --all-domains"
    assert job.enabled is True
