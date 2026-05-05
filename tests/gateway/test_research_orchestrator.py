"""Tests for `gateway.research.orchestrator`.

End-to-end happy-path with `dry_run=True`, plus error-isolation and
domain-resolution checks. NotebookLM, adapters, filter, and converters
are all mocked at their interface boundaries.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest
import yaml

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.filter.semantic import FilterResult
from gateway.research import orchestrator as orch
from gateway.research import source_map as sm
from gateway.research.adapters import CandidateItem
from gateway.research.adapters.base import AdapterError


# --- fixtures --------------------------------------------------------------


def _write_policy(kb_root: Path, slug: str, threshold: float = 0.5) -> None:
    pol_dir = kb_root / ".knowledge" / "policies" / slug
    pol_dir.mkdir(parents=True, exist_ok=True)
    (pol_dir / "policy.yaml").write_text(
        yaml.safe_dump(
            {
                "version": "v1",
                "domain": {"slug": slug, "topic": slug, "field": "test"},
                "filter": {
                    "threshold_include": threshold,
                    "threshold_review": threshold - 0.2,
                    "example_count_in_prompt": 0,
                    "example_strategy": "balanced",
                },
                "inclusion_criteria": ["always"],
                "exclusion_criteria": [],
                "quality_signals": {},
            }
        )
    )


@pytest.fixture
def policy_kb(kb_root: Path) -> Path:
    """`kb_root` plus a registered domain `alpha`."""
    _write_policy(kb_root, "alpha", threshold=0.5)
    return kb_root


# --- mock adapters ---------------------------------------------------------


@dataclass
class _StubAdapter:
    name: str
    items: list[CandidateItem] = field(default_factory=list)
    raise_error: Exception | None = None

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int = 50,
    ) -> list[CandidateItem]:
        if self.raise_error is not None:
            raise self.raise_error
        return list(self.items)


def _patch_adapters(
    monkeypatch: pytest.MonkeyPatch, adapters: list[_StubAdapter]
) -> None:
    monkeypatch.setattr(
        orch, "enabled_adapters", lambda *, include_local=None: list(adapters)
    )


# --- mock filter ----------------------------------------------------------


def _patch_filter_score(
    monkeypatch: pytest.MonkeyPatch, *, score_value: float
) -> None:
    """Replace `filter_score` inside the orchestrator with a constant scorer."""

    def _score(front, body, policy, examples=None, client=None, body_head_chars=16000):
        return FilterResult(
            score=score_value,
            rationale="stub",
            policy_version=f"{policy.domain_slug}-v1",
            decided_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )

    monkeypatch.setattr(orch, "filter_score", _score)
    monkeypatch.setattr(orch, "_load_examples", lambda domain: [])
    monkeypatch.setattr(orch, "_select_examples", lambda examples, policy: [])


# --- mock converter --------------------------------------------------------


@dataclass
class _StubConverter:
    type_name: str = "web"

    def detect(self, source: str) -> bool:
        return True

    def convert(self, source: str) -> str:
        # Build a valid canonical source page.
        body = f"Body for {source}.\n"
        slug_id = "web-2026-04-29-" + (
            "".join(ch for ch in source.lower() if ch.isalnum())[-12:]
            or "abcdef123456"
        )
        front = {
            "id": slug_id,
            "type": "web",
            "title": f"Title for {source}",
            "url": source,
            "authors": ["Test"],
            "published_at": "2026-04-29",
            "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "content_hash": validator.compute_content_hash(body),
            "domains": ["alpha"],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {},
        }
        return fm.serialize(front, body)


def _patch_converter_dispatch(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(orch.converters, "dispatch", lambda url: _StubConverter())


# --- candidate factory -----------------------------------------------------


def _candidate(url: str, *, title: str = "Some article") -> CandidateItem:
    return CandidateItem(
        item_id=url.rsplit("/", 1)[-1] or "x",
        source_type="web",
        url=url,
        title=title,
        description="(short description)",
    )


# --- happy-path dry-run ----------------------------------------------------


def test_dry_run_happy_path(monkeypatch: pytest.MonkeyPatch, policy_kb: Path):
    adapter = _StubAdapter(
        name="web",
        items=[
            _candidate("https://example.com/a", title="A"),
            _candidate("https://example.com/b", title="B"),
        ],
    )
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)

    result = orch.research(
        "test prompt about widgets",
        domain="alpha",
        dry_run=True,
    )
    assert result.success, result.errors
    assert "[dry-run]" in result.summary
    assert "wiki/mocs/alpha.md" in result.summary
    assert "cross-cutting" in result.summary

    # Materialization wrote raw files in dry-run too (cheap, idempotent).
    raw_dir = policy_kb / "raw" / "web"
    assert any(p.suffix == ".md" for p in raw_dir.iterdir())


# --- adapter errors are isolated -------------------------------------------


def test_adapter_error_does_not_abort(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    good = _StubAdapter(
        name="web", items=[_candidate("https://kept.example/")]
    )
    bad = _StubAdapter(name="boom", raise_error=AdapterError("nope"))
    _patch_adapters(monkeypatch, [good, bad])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)

    result = orch.research(
        "anything",
        domain="alpha",
        dry_run=True,
    )
    assert result.success, result.errors
    # The good adapter's candidate made it all the way through.
    assert "materialized sources: 1" in result.summary


# --- strict filter drops everything ----------------------------------------


def test_strict_filter_returns_no_op(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    # Threshold is 0.5 from the policy; score 0.1 < threshold.
    adapter = _StubAdapter(
        name="web", items=[_candidate("https://x.example/")]
    )
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.1)
    _patch_converter_dispatch(monkeypatch)

    result = orch.research(
        "ignored prompt",
        domain="alpha",
        dry_run=True,
    )
    assert result.success
    assert result.no_op
    assert "no candidates met threshold" in result.summary


# --- unknown domain --------------------------------------------------------


def test_unknown_domain_errors(monkeypatch: pytest.MonkeyPatch, policy_kb: Path):
    result = orch.research(
        "anything",
        domain="not-registered",
        dry_run=True,
    )
    assert not result.success
    joined = " ".join(result.errors)
    assert "no policy" in joined
    assert "discover-domains" in joined


def test_no_domain_no_inference_errors(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    # No --domain and no plan_client → infer returns None → error.
    _patch_adapters(monkeypatch, [])
    result = orch.research("anything", domain=None, dry_run=True)
    assert not result.success
    joined = " ".join(result.errors)
    assert "infer" in joined or "discover-domains" in joined


# --- analysis failure triggers abandon -------------------------------------


@dataclass
class _MockNlm:
    """Minimal NlmClient covering everything the orchestrator touches."""

    next_persistent: str = "nb-persistent"
    next_session: str = "nb-session"
    creates: list[str] = field(default_factory=list)
    sources_added: list[tuple[str, str]] = field(default_factory=list)
    text_added: list[tuple[str, str, str | None]] = field(default_factory=list)

    def notebook_create(self, title: str) -> str:
        self.creates.append(title)
        # Persistent first call, session second
        if "session" in title:
            return self.next_session
        return self.next_persistent

    def source_add_url(self, notebook_id: str, url: str) -> None:
        self.sources_added.append((notebook_id, url))

    def source_add_text(self, notebook_id, content, *, title=None):
        self.text_added.append((notebook_id, content, title))

    def notebook_query(self, notebook_id, question):
        return {"answer": "", "citations": {}, "sources_used": []}


def test_analysis_failure_marks_session_abandoned(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    adapter = _StubAdapter(name="web", items=[_candidate("https://x.example/")])
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)

    # Patch source_map.fetch to avoid any subprocess calls.
    monkeypatch.setattr(
        sm, "fetch_nlm_sources", lambda nb_id: []
    )

    # Force the analyze() call to blow up.
    def _boom(*args, **kwargs):
        raise RuntimeError("simulated analysis failure")

    if orch._analysis is not None:
        monkeypatch.setattr(orch._analysis, "analyze", _boom)
    else:
        # If the parallel agent hasn't shipped analysis, the orchestrator
        # itself raises in step 12 — same observable behavior.
        pass

    nlm = _MockNlm()
    result = orch.research(
        "test prompt",
        domain="alpha",
        nlm_client=nlm,
    )
    assert not result.success
    joined = " ".join(result.errors)
    assert "alpha" in joined or "session" in joined or "research session" in joined

    # The session must be in `abandoned` state in the registry.
    from gateway import nlm_registry

    sessions = nlm_registry.list_sessions("alpha")
    assert sessions, "session should have been registered before abandon"
    assert sessions[0]["status"] == "abandoned"


# --- empty prompt ----------------------------------------------------------


def test_empty_prompt_errors(policy_kb: Path):
    result = orch.research("   ", domain="alpha", dry_run=True)
    assert not result.success


# --- adapter list empty (no candidates) ------------------------------------


def test_no_adapters_no_op(monkeypatch: pytest.MonkeyPatch, policy_kb: Path):
    _patch_adapters(monkeypatch, [])
    result = orch.research("anything", domain="alpha", dry_run=True)
    assert result.success
    assert result.no_op
    assert "no candidates" in result.summary


# --- M37.1 query plan integration ------------------------------------------


class _StubPlanClient:
    """PlanClient stub that returns a canned per-adapter JSON response."""

    def __init__(self, response: str):
        self.response = response
        self.last_prompt: str | None = None

    def call(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response


def test_planner_generates_and_persists_plan(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """When a plan_client is configured, queries are generated, persisted,
    and the per-adapter list is what gets fanned out."""
    captured_queries: list[str] = []

    @dataclass
    class _Recording:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            captured_queries.append(query)
            return [_candidate(f"https://example.com/{query[:5]}")]

    adapter = _Recording()
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)

    plan_client = _StubPlanClient(
        '{"web": ["query alpha", "query beta"]}'
    )

    result = orch.research(
        "test prompt",
        domain="alpha",
        plan_client=plan_client,
        dry_run=True,
    )
    assert result.success, result.errors

    # Plan persisted
    qpdir = policy_kb / "nlm" / "query_plans"
    persisted = list(qpdir.glob("*.yaml"))
    assert len(persisted) == 1
    parsed = yaml.safe_load(persisted[0].read_text())
    assert parsed["queries"]["web"] == ["query alpha", "query beta"]
    assert parsed["edited"] is False
    assert parsed["domain"] == "alpha"

    # Both queries reached the adapter
    assert "query alpha" in captured_queries
    assert "query beta" in captured_queries


def test_review_gate_stops_before_fan_out(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    captured_queries: list[str] = []

    @dataclass
    class _Recording:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            captured_queries.append(query)
            return []

    _patch_adapters(monkeypatch, [_Recording()])
    plan_client = _StubPlanClient('{"web": ["q1", "q2"]}')

    result = orch.research(
        "test prompt",
        domain="alpha",
        plan_client=plan_client,
        review=True,
    )
    assert result.success
    assert "review-gate" in result.summary
    assert "--execute" in result.summary

    # Plan persisted, but no adapter call
    qpdir = policy_kb / "nlm" / "query_plans"
    assert len(list(qpdir.glob("*.yaml"))) == 1
    assert captured_queries == []


def test_execute_resumes_from_persisted_plan(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """`--execute <session-id>` loads the YAML and uses its queries."""
    from gateway.research import query_plan_store as qps

    persisted = qps.QueryPlan(
        session_id="2026-04-30-prior-run",
        domain="alpha",
        prompt="prior prompt",
        generated_at=datetime(2026, 4, 30, 10, 0, 0, tzinfo=timezone.utc),
        queries={"web": ["resumed query"]},
    )
    qps.save(persisted)

    captured: list[str] = []

    @dataclass
    class _Recording:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            captured.append(query)
            return [_candidate(f"https://r/{query[:8]}")]

    _patch_adapters(monkeypatch, [_Recording()])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)

    result = orch.research(
        prompt=None,
        execute_session="2026-04-30-prior-run",
        dry_run=True,
    )
    assert result.success, result.errors
    assert captured == ["resumed query"]
    # session_id reused — no new plan file
    qpdir = policy_kb / "nlm" / "query_plans"
    assert {p.stem for p in qpdir.glob("*.yaml")} == {"2026-04-30-prior-run"}


def test_execute_stamps_edited_when_mtime_advances(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    import os
    import time
    from gateway.research import query_plan_store as qps

    past = datetime(2026, 1, 1, tzinfo=timezone.utc)
    persisted = qps.QueryPlan(
        session_id="touched-session",
        domain="alpha",
        prompt="p",
        generated_at=past,
        queries={"web": ["q"]},
    )
    qps.save(persisted)
    target = qps.path_for("touched-session")
    now_ts = time.time()
    os.utime(target, (now_ts, now_ts))

    @dataclass
    class _Stub:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            return []

    _patch_adapters(monkeypatch, [_Stub()])
    orch.research(
        prompt=None,
        execute_session="touched-session",
        dry_run=True,
    )
    reloaded = qps.load("touched-session")
    assert reloaded.edited is True


def test_queries_path_loads_external_yaml(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path, tmp_path: Path
):
    """`--queries <path>` adopts the external plan; new session is created."""
    external = tmp_path / "curated.yaml"
    external.write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "session_id": "irrelevant",
                "domain": "irrelevant",
                "prompt": "irrelevant",
                "generated_at": "2026-01-01T00:00:00Z",
                "queries": {"web": ["external q"]},
                "edited": True,
            }
        )
    )

    captured: list[str] = []

    @dataclass
    class _Recording:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            captured.append(query)
            return []

    _patch_adapters(monkeypatch, [_Recording()])

    result = orch.research(
        "fresh prompt",
        domain="alpha",
        external_plan_path=str(external),
        review=True,
    )
    assert result.success
    # New plan persisted under fresh session id (not "irrelevant")
    qpdir = policy_kb / "nlm" / "query_plans"
    persisted = list(qpdir.glob("*.yaml"))
    assert len(persisted) == 1
    assert persisted[0].stem != "irrelevant"
    parsed = yaml.safe_load(persisted[0].read_text())
    assert parsed["queries"]["web"] == ["external q"]
    assert parsed["domain"] == "alpha"
    assert parsed["prompt"] == "fresh prompt"


def test_execute_and_queries_are_mutually_exclusive(policy_kb: Path):
    result = orch.research(
        prompt=None,
        execute_session="x",
        external_plan_path="y",
    )
    assert not result.success
    assert any("mutually exclusive" in e for e in result.errors)


def test_execute_with_missing_plan_errors(policy_kb: Path):
    result = orch.research(
        prompt=None,
        execute_session="does-not-exist",
    )
    assert not result.success
    assert any("query plan" in e for e in result.errors)


def test_no_plan_client_falls_back_to_verbatim(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """M37 backwards-compat: without a plan_client, prompt is dispatched
    verbatim and no plan is persisted."""
    captured: list[str] = []

    @dataclass
    class _Recording:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            captured.append(query)
            return []

    _patch_adapters(monkeypatch, [_Recording()])
    orch.research(
        "verbatim prompt",
        domain="alpha",
        plan_client=None,
        dry_run=True,
    )
    assert captured == ["verbatim prompt"]
    # No plan persisted on the offline path
    qpdir = policy_kb / "nlm" / "query_plans"
    assert not qpdir.exists() or not list(qpdir.glob("*.yaml"))


def test_planner_failure_falls_back_to_verbatim(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """If the plan_client returns garbage, the run continues using the
    prompt verbatim — slop-but-running beats hard-fail."""
    captured: list[str] = []

    @dataclass
    class _Recording:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            captured.append(query)
            return []

    _patch_adapters(monkeypatch, [_Recording()])
    plan_client = _StubPlanClient("totally not JSON")

    orch.research(
        "fallback test",
        domain="alpha",
        plan_client=plan_client,
        dry_run=True,
    )
    assert captured == ["fallback test"]


def test_history_examples_seeded_into_planner_prompt(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """`recent_edited` results are passed into the planner so future runs
    learn from past curation."""
    from gateway.research import query_plan_store as qps

    history = qps.QueryPlan(
        session_id="curated",
        domain="alpha",
        prompt="curated prior prompt",
        generated_at=datetime(2026, 4, 1, tzinfo=timezone.utc),
        queries={"web": ["pinned good query"]},
        edited=True,
    )
    qps.save(history)

    @dataclass
    class _Stub:
        name: str = "web"

        def search(self, query, *, max_results=50, **kwargs):
            return []

    _patch_adapters(monkeypatch, [_Stub()])
    plan_client = _StubPlanClient('{"web": ["new q"]}')
    orch.research(
        "follow-up",
        domain="alpha",
        plan_client=plan_client,
        dry_run=True,
    )
    assert plan_client.last_prompt is not None
    assert "pinned good query" in plan_client.last_prompt
