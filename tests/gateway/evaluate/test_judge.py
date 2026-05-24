"""Tests for the eval Judge (M50 Phase C).

Mocks AnthropicAPIClient. Real-network verification in the M50 hand-test.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from gateway.evaluate.schema import Golden, EvalResult
from gateway.evaluate.judge import Judge
from gateway.llm.telemetry import CallResult


def test_judge_parses_structured_output():
    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"score": 0.85, '
            '"cite_hits": ["pubmed-12345"], '
            '"cite_misses": ["pubmed-67890"], '
            '"assertion_hits": ["GLP-1 reduces food-cue reactivity"], '
            '"assertion_misses": [], '
            '"anti_assertion_violations": [], '
            '"reasoning": "Cites one of two required sources; covers the main assertion."}'
        ),
        input_tokens=4000, output_tokens=150, cache_read_tokens=3000,
        model="claude-sonnet-4-6",
    )

    judge = Judge(client=fake_client)
    golden = Golden(
        id="q01",
        question="Does GLP-1 reduce food-cue reactivity?",
        must_cite=["pubmed-12345", "pubmed-67890"],
        must_assert=["GLP-1 reduces food-cue reactivity"],
        must_not_assert=[],
    )

    result = judge.score(golden=golden, wiki_context="<wiki context>")

    assert isinstance(result, EvalResult)
    assert result.score == 0.85
    assert result.cite_hits == ["pubmed-12345"]
    assert result.cite_misses == ["pubmed-67890"]
    assert result.assertion_hits[0].startswith("GLP-1")
    assert result.input_tokens == 4000
    assert result.cache_read_tokens == 3000
    assert result.golden_id == "q01"


def test_judge_handles_malformed_json():
    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text="not json", input_tokens=10, output_tokens=2,
        model="claude-sonnet-4-6",
    )

    judge = Judge(client=fake_client)
    golden = Golden(id="q01", question="Q?", must_cite=[],
                    must_assert=[], must_not_assert=[])

    result = judge.score(golden=golden, wiki_context="ctx")
    assert result.score == 0.0
    assert "json" in result.judge_reasoning.lower() or "parse" in result.judge_reasoning.lower()


def test_judge_anti_assertion_violation_populates_field():
    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"score": 0.3, "cite_hits": [], "cite_misses": [], '
            '"assertion_hits": [], "assertion_misses": [], '
            '"anti_assertion_violations": ["The wiki says X causes Y, which is wrong."], '
            '"reasoning": "Wiki asserts a forbidden claim."}'
        ),
        input_tokens=100, output_tokens=20, model="claude-sonnet-4-6",
    )

    judge = Judge(client=fake_client)
    golden = Golden(
        id="q01", question="Q?",
        must_cite=[], must_assert=[],
        must_not_assert=["The wiki says X causes Y"],
    )

    result = judge.score(golden=golden, wiki_context="ctx")
    assert len(result.anti_assertion_violations) == 1
    assert result.score == 0.3


def test_judge_tolerates_code_fence_wrapping():
    """LLM may emit JSON wrapped in ```json ... ``` despite the prompt
    saying not to. The parser must strip the fences."""
    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '```json\n'
            '{"score": 0.6, "cite_hits": [], "cite_misses": [], '
            '"assertion_hits": [], "assertion_misses": [], '
            '"anti_assertion_violations": [], "reasoning": "ok"}\n'
            '```'
        ),
        input_tokens=50, output_tokens=20, model="claude-sonnet-4-6",
    )

    judge = Judge(client=fake_client)
    golden = Golden(id="q01", question="Q?",
                    must_cite=[], must_assert=[], must_not_assert=[])

    result = judge.score(golden=golden, wiki_context="ctx")
    assert result.score == 0.6
