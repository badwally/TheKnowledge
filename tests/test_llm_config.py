"""Tests for `gateway.llm.config` per-call-site model selection (Fix E).

The old layout had one `DEFAULT_PLAN_MODEL` shared across every plan-tier
call site (authorship, bootstrap-domain, query-planner). All three pinned
to Opus 4.7. This file pins the per-purpose split: authorship stays on
Opus (where deep multi-page planning is genuinely needed); bootstrap-domain
and query-planner drop to Sonnet (bounded structural generation, frees
Opus quota for the work that actually needs it).

Back-compat: `model_for("plan")` keeps returning the authorship model so
existing callers (and the `ClaudeCLIPlanClient` default) don't regress.
"""

from __future__ import annotations

import pytest

from gateway.llm import config as llm_config


def test_model_for_filter_returns_haiku():
    assert llm_config.model_for("filter") == "claude-haiku-4-5-20251001"


def test_model_for_vlm_returns_opus():
    assert llm_config.model_for("vlm") == "claude-opus-4-7"


def test_model_for_plan_returns_authorship_opus_back_compat():
    """`model_for('plan')` is the back-compat alias for the authorship
    purpose. Must stay on Opus 4.7 to avoid regressing existing callers
    (ClaudeCLIPlanClient defaults to this when no model is passed)."""
    assert llm_config.model_for("plan") == "claude-opus-4-7"


def test_model_for_plan_authorship_returns_opus():
    """`wiki ingest --with-plan` runs the wiki authorship agent: a
    multi-page Plan with citation discipline. Deep reasoning matters
    more than throughput here — Opus 4.7."""
    assert llm_config.model_for("plan_authorship") == "claude-opus-4-7"


def test_model_for_plan_bootstrap_domain_returns_sonnet():
    """`wiki bootstrap-domain` generates a structured policy.yaml once
    per domain. Bounded structural authoring; Sonnet 4.6 handles it
    well and at ~5x lower cost / faster turnaround than Opus."""
    assert llm_config.model_for("plan_bootstrap_domain") == "claude-sonnet-4-6"


def test_model_for_plan_query_planner_returns_sonnet():
    """`wiki research --review` expands a research prompt into per-adapter
    query plans (arxiv/youtube/web/semscholar). Breadth of fan-out
    matters more than depth of reasoning. Sonnet 4.6."""
    assert llm_config.model_for("plan_query_planner") == "claude-sonnet-4-6"


def test_model_for_cite_suggest_returns_sonnet():
    """`wiki cite --suggest` (M49 AGT-2) runs attribution matching:
    given a draft and its declared sources, identify which source
    supports each claim. Bounded reasoning task; Sonnet 4.6."""
    assert llm_config.model_for("cite_suggest") == "claude-sonnet-4-6"
    assert llm_config.DEFAULT_CITE_SUGGEST_MODEL == "claude-sonnet-4-6"


def test_model_for_evaluate_judge_returns_sonnet():
    """`wiki evaluate` runs Sonnet 4.6 as LLM-as-judge over wiki context.
    Bounded reasoning + structured-output task; Sonnet 4.6."""
    assert llm_config.model_for("evaluate_judge") == "claude-sonnet-4-6"
    assert llm_config.DEFAULT_EVALUATE_JUDGE_MODEL == "claude-sonnet-4-6"


def test_model_for_unknown_stage_raises():
    with pytest.raises(ValueError, match="unknown LLM stage"):
        llm_config.model_for("definitely-not-a-stage")  # type: ignore[arg-type]


# --- wire-up tests: callers pick the right per-purpose model --------------


class _RecordingPlanClient:
    """Stand-in that records constructor kwargs so wire-up tests can
    inspect which model the caller asked for. Implements the minimum
    PlanClient surface used by bootstrap-domain / query-planner."""

    last_init_model: str | None = None

    def __init__(self, *args, model: str | None = None, **kwargs):
        type(self).last_init_model = model

    def call(self, prompt: str) -> str:
        # Not exercised by the wire-up test; bootstrap-domain bails before
        # the LLM call because we're testing only the constructor wiring.
        return ""


def test_bootstrap_domain_default_plan_client_uses_sonnet(monkeypatch, tmp_path):
    """When the caller doesn't pass a plan_client, bootstrap_domain must
    construct one with the plan_bootstrap_domain model (Sonnet 4.6),
    not the back-compat plan default (Opus)."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    for sub in ("wiki", "wiki/proposals", ".knowledge", ".knowledge/policies"):
        (tmp_path / sub).mkdir(parents=True, exist_ok=True)

    _RecordingPlanClient.last_init_model = None
    monkeypatch.setattr(
        "gateway.plan.ClaudeCLIPlanClient", _RecordingPlanClient
    )

    from gateway.ops.bootstrap_domain import bootstrap_domain

    # Call with no plan_client → default construction path runs.
    # The op will then fail later (empty body from recorder), but the
    # constructor call we care about already happened.
    bootstrap_domain(
        "A short test description for the bootstrap domain pipeline.",
        "test-fix-e-bootstrap-slug",
    )

    assert _RecordingPlanClient.last_init_model == "claude-sonnet-4-6"
