"""Tests for `gateway.research.query_planner`."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from gateway.filter.policy import Policy
from gateway.research import query_planner as qp
from gateway.research.query_plan_store import QueryPlan


def _policy() -> Policy:
    return Policy(
        domain_slug="edge-ai-agentic",
        domain_topic="Edge inference for agentic AI workflows",
        domain_field="Edge AI, distributed systems, and AI infrastructure",
        inclusion_criteria=[
            "Discusses AI inference at the edge",
            "Covers MCP, A2A, or other agent protocols",
            "RAG over proprietary first-party data on edge",
        ],
    )


class _MockClient:
    """Minimal PlanClient stub that returns a canned response."""

    def __init__(self, response: str):
        self.response = response
        self.last_prompt: str | None = None

    def call(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response


def test_happy_path_parses_response_to_per_adapter_lists() -> None:
    client = _MockClient(
        '{"youtube": ["edge AI inference", "MCP servers"], '
        '"arxiv": ["on-device LLM quantization"], '
        '"web": [], "pubmed": []}'
    )
    result = qp.plan_per_adapter_queries(
        "RAG over proprietary edge data",
        domain="edge-ai-agentic",
        policy=_policy(),
        adapter_names=["youtube", "arxiv", "web", "pubmed"],
        plan_client=client,
    )
    assert result.queries["youtube"] == ["edge AI inference", "MCP servers"]
    assert result.queries["arxiv"] == ["on-device LLM quantization"]
    assert result.queries["web"] == []
    assert result.queries["pubmed"] == []
    assert result.target_counts["youtube"] == qp.DEFAULT_TARGET_COUNTS["youtube"]


def test_empty_prompt_rejected() -> None:
    with pytest.raises(qp.PlannerError, match="non-empty"):
        qp.plan_per_adapter_queries(
            "",
            domain="d",
            policy=_policy(),
            adapter_names=["youtube"],
            plan_client=_MockClient("{}"),
        )


def test_empty_adapter_list_rejected() -> None:
    with pytest.raises(qp.PlannerError, match="adapter"):
        qp.plan_per_adapter_queries(
            "p",
            domain="d",
            policy=_policy(),
            adapter_names=[],
            plan_client=_MockClient("{}"),
        )


def test_response_with_markdown_fences_is_tolerated() -> None:
    client = _MockClient('```json\n{"youtube": ["q"]}\n```')
    result = qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
    )
    assert result.queries["youtube"] == ["q"]


def test_response_with_leading_prose_is_extracted() -> None:
    client = _MockClient(
        'Here are the queries:\n{"youtube": ["q"]}\nLet me know.'
    )
    result = qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
    )
    assert result.queries["youtube"] == ["q"]


def test_missing_adapter_in_response_yields_empty_list() -> None:
    client = _MockClient('{"youtube": ["q"]}')
    result = qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube", "arxiv", "web"],
        plan_client=client,
    )
    assert result.queries == {"youtube": ["q"], "arxiv": [], "web": []}


def test_non_string_query_items_get_coerced_or_dropped() -> None:
    client = _MockClient('{"youtube": ["good", "", "  ", 42]}')
    result = qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
    )
    # blank strings dropped; non-strings stringified
    assert result.queries["youtube"] == ["good", "42"]


def test_non_list_adapter_value_raises() -> None:
    client = _MockClient('{"youtube": "not a list"}')
    with pytest.raises(qp.PlannerError, match="must be a list"):
        qp.plan_per_adapter_queries(
            "p",
            domain="d",
            policy=_policy(),
            adapter_names=["youtube"],
            plan_client=client,
        )


def test_empty_response_raises() -> None:
    with pytest.raises(qp.PlannerError, match="empty"):
        qp.plan_per_adapter_queries(
            "p",
            domain="d",
            policy=_policy(),
            adapter_names=["youtube"],
            plan_client=_MockClient("   "),
        )


def test_unparseable_response_raises() -> None:
    with pytest.raises(qp.PlannerError):
        qp.plan_per_adapter_queries(
            "p",
            domain="d",
            policy=_policy(),
            adapter_names=["youtube"],
            plan_client=_MockClient("just prose, no JSON here"),
        )


def test_target_counts_overridable() -> None:
    client = _MockClient('{"youtube": []}')
    result = qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
        target_counts={"youtube": 50},
    )
    assert result.target_counts["youtube"] == 50
    assert "(~50" in (client.last_prompt or "")


def test_few_shot_examples_appear_in_prompt() -> None:
    examples = [
        QueryPlan(
            session_id="s-old",
            domain="edge-ai-agentic",
            prompt="prior research about MCP enterprise",
            generated_at=datetime(2026, 4, 1, tzinfo=timezone.utc),
            queries={"youtube": ["MCP enterprise deployment"]},
            edited=True,
        ),
    ]
    client = _MockClient('{"youtube": ["new"]}')
    qp.plan_per_adapter_queries(
        "follow-up research",
        domain="edge-ai-agentic",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
        history_examples=examples,
    )
    assert client.last_prompt is not None
    assert "Past curated examples" in client.last_prompt
    assert "MCP enterprise deployment" in client.last_prompt


def test_no_history_renders_placeholder() -> None:
    client = _MockClient('{"youtube": []}')
    qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
    )
    assert "no curated examples yet" in (client.last_prompt or "")


def test_inclusion_criteria_excerpt_in_prompt() -> None:
    client = _MockClient('{"youtube": []}')
    qp.plan_per_adapter_queries(
        "p",
        domain="edge-ai-agentic",
        policy=_policy(),
        adapter_names=["youtube"],
        plan_client=client,
    )
    assert client.last_prompt is not None
    assert "Discusses AI inference at the edge" in client.last_prompt
    assert "RAG over proprietary first-party data" in client.last_prompt


def test_adapter_idiom_guidance_present_in_prompt() -> None:
    client = _MockClient('{"youtube": [], "arxiv": []}')
    qp.plan_per_adapter_queries(
        "p",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube", "arxiv"],
        plan_client=client,
    )
    assert client.last_prompt is not None
    # The per-adapter guidance hints are surfaced so the planner
    # produces idiomatic queries (short keywords for youtube,
    # paper-language for arxiv).
    assert "short keyword" in client.last_prompt
    assert "paper-language" in client.last_prompt


def test_youtube_adapter_guidance_targets_lecture_register() -> None:
    g = qp._ADAPTER_GUIDANCE["youtube"].lower()
    assert "lecture" in g
    assert "keynote" in g or "seminar" in g
    # the old vendor/tutorial bias should be gone
    assert "tutorial" not in g or "avoid" in g


def test_rendered_plan_prompt_carries_youtube_lecture_register() -> None:
    client = _MockClient('{"youtube": [], "arxiv": [], "web": [], "pubmed": []}')
    qp.plan_per_adapter_queries(
        "agents that query semantic data",
        domain="d",
        policy=_policy(),
        adapter_names=["youtube", "arxiv", "web", "pubmed"],
        plan_client=client,
    )
    assert client.last_prompt is not None
    assert "lecture" in client.last_prompt.lower()
