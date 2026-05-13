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


# --- post-apply_plan promote failure does NOT abandon ----------------------


def test_promote_failure_does_not_abandon_session(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """apply_plan success + promote failure → warning, not abandon.

    Regression for the 2026-05-11 incident: one stale URL inside
    `session.promote()` raised, the orchestrator caught it as a fatal
    error, and the session was marked abandoned even though apply_plan
    had already written 7 wiki pages to disk."""
    adapter = _StubAdapter(name="web", items=[_candidate("https://x.example/")])
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)
    monkeypatch.setattr(sm, "fetch_nlm_sources", lambda nb_id: [])

    # analysis returns a minimal successful AnalysisResult.
    from gateway.research.analysis import AnalysisResult

    def _ok_analyze(notebook_id, *, domain, research_query, client, **_):
        return AnalysisResult(
            domain=domain,
            research_query=research_query,
            notebook_id=notebook_id,
            taxonomy={"field": research_query, "branches": []},
            findings={},
            synthesis={},
        )

    assert orch._analysis is not None, "analysis module must be importable"
    monkeypatch.setattr(orch._analysis, "analyze", _ok_analyze)

    # apply_plan returns success with a synthetic touched path.
    from gateway.core import OperationResult

    def _ok_apply(plan, *, draft=False, force_new_slug=False):
        return OperationResult(
            success=True,
            paths_touched=[policy_kb / "wiki" / "mocs" / "alpha.md"],
            summary=f"applied plan for {plan.source_id}",
        )

    monkeypatch.setattr(orch, "apply_plan", _ok_apply)

    # promote raises — simulates the stale-URL failure.
    def _boom_promote(*args, **kwargs):
        raise RuntimeError("Could not add url source.")

    monkeypatch.setattr(orch._session, "promote", _boom_promote)

    nlm = _MockNlm()
    result = orch.research("test prompt", domain="alpha", nlm_client=nlm)

    # The wiki was authored — overall result must be success.
    assert result.success, result.errors
    # Promote failure surfaced as a warning, not as a session abort.
    assert any(
        "Could not add url source" in w for w in result.warnings
    ), f"expected promote warning in: {result.warnings}"

    # Session must NOT be abandoned — pages are on disk.
    from gateway import nlm_registry

    sessions = nlm_registry.list_sessions("alpha")
    assert sessions, "session should have been registered"
    assert sessions[0]["status"] != "abandoned", (
        f"session was abandoned after apply_plan succeeded: {sessions[0]}"
    )


def test_promote_partial_failure_surfaces_as_warnings(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """Per-source promote failures (e.g. one stale URL in N) → warnings,
    not session abort. The session is marked promoted with the actual
    added count."""
    adapter = _StubAdapter(name="web", items=[_candidate("https://x.example/")])
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)
    monkeypatch.setattr(sm, "fetch_nlm_sources", lambda nb_id: [])

    from gateway.research.analysis import AnalysisResult

    def _ok_analyze(notebook_id, *, domain, research_query, client, **_):
        return AnalysisResult(
            domain=domain,
            research_query=research_query,
            notebook_id=notebook_id,
            taxonomy={"field": research_query, "branches": []},
            findings={},
            synthesis={},
        )

    monkeypatch.setattr(orch._analysis, "analyze", _ok_analyze)

    from gateway.core import OperationResult

    def _ok_apply(plan, *, draft=False, force_new_slug=False):
        return OperationResult(
            success=True,
            paths_touched=[policy_kb / "wiki" / "mocs" / "alpha.md"],
            summary=f"applied plan for {plan.source_id}",
        )

    monkeypatch.setattr(orch, "apply_plan", _ok_apply)

    # promote returns partial-success — 2 added, 1 stale URL failed.
    def _partial_promote(*args, **kwargs):
        return 2, [("https://stale.example/", "Could not add url source.")]

    monkeypatch.setattr(orch._session, "promote", _partial_promote)

    nlm = _MockNlm()
    result = orch.research("test prompt", domain="alpha", nlm_client=nlm)

    assert result.success, result.errors
    assert any("stale.example" in w for w in result.warnings), result.warnings


def test_analysis_log_records_actual_branch_count(
    monkeypatch: pytest.MonkeyPatch, policy_kb: Path
):
    """log.append for step=analysis records len(findings), not 0.

    Regression for the pre-2026-05-12 `branches=0` bug where the
    orchestrator looked up a non-existent `branches` attribute on
    AnalysisResult."""
    adapter = _StubAdapter(name="web", items=[_candidate("https://x.example/")])
    _patch_adapters(monkeypatch, [adapter])
    _patch_filter_score(monkeypatch, score_value=0.9)
    _patch_converter_dispatch(monkeypatch)
    monkeypatch.setattr(sm, "fetch_nlm_sources", lambda nb_id: [])

    from gateway.research.analysis import AnalysisResult

    def _ok_analyze(notebook_id, *, domain, research_query, client, **_):
        return AnalysisResult(
            domain=domain,
            research_query=research_query,
            notebook_id=notebook_id,
            taxonomy={"field": research_query, "branches": []},
            findings={"branch-a": {}, "branch-b": {}, "branch-c": {}},
            synthesis={},
        )

    monkeypatch.setattr(orch._analysis, "analyze", _ok_analyze)

    from gateway.core import OperationResult

    def _ok_apply(plan, *, draft=False, force_new_slug=False):
        return OperationResult(
            success=True,
            paths_touched=[policy_kb / "wiki" / "mocs" / "alpha.md"],
            summary="applied",
        )

    monkeypatch.setattr(orch, "apply_plan", _ok_apply)
    monkeypatch.setattr(orch._session, "promote", lambda *a, **kw: (0, []))

    captured: list[dict] = []
    real_append = orch.log.append

    def capturing_append(event_type, *, fields, summary):
        captured.append({"event": event_type, "fields": dict(fields), "summary": summary})
        return real_append(event_type, fields=fields, summary=summary)

    monkeypatch.setattr(orch.log, "append", capturing_append)

    nlm = _MockNlm()
    result = orch.research("test prompt", domain="alpha", nlm_client=nlm)
    assert result.success, result.errors

    analysis_entries = [
        c for c in captured
        if c["event"] == "research" and c["fields"].get("step") == "analysis"
    ]
    assert len(analysis_entries) == 1, captured
    assert analysis_entries[0]["fields"]["branches"] == 3, analysis_entries[0]
    assert "3 branch(es)" in analysis_entries[0]["summary"]


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


# --- M44.1: parallel filter -------------------------------------------------


def _make_candidate(idx: int) -> CandidateItem:
    return CandidateItem(
        source_type="web",
        item_id=f"c{idx}",
        url=f"https://example.com/{idx}",
        title=f"Candidate {idx}",
        description=f"body for {idx}",
        authors=[],
        publish_date="",
        source_metadata={},
    )


def test_run_filter_parallel_threshold_preserves_input_order(policy_kb, monkeypatch):
    """Accepted candidates must come back in input order regardless of scheduling."""
    from gateway.filter import policy as _policy

    candidates = [_make_candidate(i) for i in range(20)]

    # Score every other candidate above the include threshold (0.5).
    scores = [0.9 if i % 2 == 0 else 0.1 for i in range(20)]

    def _score(front, body, policy, examples=None, client=None, body_head_chars=16000):
        idx = int(front["url"].rsplit("/", 1)[-1])
        return FilterResult(
            score=scores[idx],
            rationale="stub",
            policy_version=f"{policy.domain_slug}-v1",
            decided_at="2026-05-12T00:00:00Z",
        )

    monkeypatch.setattr(orch, "filter_score", _score)
    policy = _policy.load_policy("alpha")

    accepted = orch._run_filter(
        candidates,
        domain="alpha",
        policy=policy,
        trust_local=False,
        filter_client=None,
        session_id="test-session",
        max_workers=8,
    )

    assert [int(c.url.rsplit("/", 1)[-1]) for c, _ in accepted] == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert all(s == 0.9 for _, s in accepted)


def test_run_filter_actually_runs_concurrently(policy_kb, monkeypatch):
    """8 workers must enter `filter_score` simultaneously (verified via barrier)."""
    import threading
    from gateway.filter import policy as _policy

    n = 8
    enter_barrier = threading.Barrier(n + 1, timeout=5.0)  # +1 for main thread

    def _slow_score(front, body, policy, examples=None, client=None, body_head_chars=16000):
        enter_barrier.wait()  # blocks until all n workers + main reach this point
        return FilterResult(
            score=0.9,
            rationale="stub",
            policy_version=f"{policy.domain_slug}-v1",
            decided_at="2026-05-12T00:00:00Z",
        )

    monkeypatch.setattr(orch, "filter_score", _slow_score)
    policy = _policy.load_policy("alpha")
    candidates = [_make_candidate(i) for i in range(n)]

    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        fut = pool.submit(
            orch._run_filter,
            candidates,
            domain="alpha",
            policy=policy,
            trust_local=False,
            filter_client=None,
            session_id="test-session",
            max_workers=n,
        )
        # Will deadlock (barrier timeout fires as BrokenBarrierError) if
        # _run_filter is sequential — only 1 worker enters at a time.
        enter_barrier.wait()
        accepted = fut.result(timeout=10.0)

    assert len(accepted) == n


def test_run_filter_isolates_per_item_errors(policy_kb, monkeypatch):
    """One bad candidate should not sink the batch."""
    from gateway.filter import policy as _policy
    from gateway.filter.semantic import FilterError

    candidates = [_make_candidate(i) for i in range(5)]

    def _score(front, body, policy, examples=None, client=None, body_head_chars=16000):
        idx = int(front["url"].rsplit("/", 1)[-1])
        if idx == 2:
            raise FilterError("boom")
        return FilterResult(
            score=0.9,
            rationale="ok",
            policy_version=f"{policy.domain_slug}-v1",
            decided_at="2026-05-12T00:00:00Z",
        )

    monkeypatch.setattr(orch, "filter_score", _score)
    policy = _policy.load_policy("alpha")

    accepted = orch._run_filter(
        candidates,
        domain="alpha",
        policy=policy,
        trust_local=False,
        filter_client=None,
        session_id="test-session",
        max_workers=4,
    )

    # Indexes 0, 1, 3, 4 accepted; index 2 dropped due to FilterError.
    assert [int(c.url.rsplit("/", 1)[-1]) for c, _ in accepted] == [0, 1, 3, 4]


def test_run_filter_empty_candidates_returns_empty(policy_kb):
    from gateway.filter import policy as _policy

    policy = _policy.load_policy("alpha")
    assert (
        orch._run_filter(
            [],
            domain="alpha",
            policy=policy,
            trust_local=False,
            filter_client=None,
            session_id="test-session",
        )
        == []
    )


# --- M45: synthesizes emission --------------------------------------------


def test_branch_synthesis_update_emits_synthesizes_and_included_works():
    """Per-branch synthesis page (`first-derivative`) emits `synthesizes:`
    listing the constituent sources plus a `## Included works` section."""
    from gateway import frontmatter as fm

    branch_findings = {
        "specifics": {
            "answer": "Specifics body.",
            "citations": {1: "nlm-id-1", 2: "nlm-id-2"},
            "sources_used": [],
        },
        "comparisons": {
            "answer": "Comparisons body.",
            "citations": {1: "nlm-id-3"},
            "sources_used": [],
        },
    }
    source_map = {
        "nlm-id-1": "raw/web/web-aaa",
        "nlm-id-2": "raw/web/web-bbb",
        "nlm-id-3": "raw/web/web-ccc",
    }
    update = orch._make_branch_synthesis_update(
        domain="alpha",
        session_id="sess-1",
        branch_name="Some Theme",
        branch_findings=branch_findings,
        research_query="rq",
        source_map=source_map,
    )
    front, body = fm.parse(update.content)
    assert front.get("synthesizes") == [
        "sources/web-aaa",
        "sources/web-bbb",
        "sources/web-ccc",
    ]
    assert "## Included works" in body
    for slug in ("web-aaa", "web-bbb", "web-ccc"):
        assert f"[[sources/{slug}]]" in body


def test_branch_synthesis_omits_synthesizes_when_no_citations():
    """Branch with no resolvable citations does not emit `synthesizes:`."""
    from gateway import frontmatter as fm

    update = orch._make_branch_synthesis_update(
        domain="alpha",
        session_id="sess-1",
        branch_name="Empty Branch",
        branch_findings={"specifics": {"answer": "ok", "citations": {}, "sources_used": []}},
        research_query="rq",
        source_map={},
    )
    front, body = fm.parse(update.content)
    assert "synthesizes" not in front
    assert "## Included works" not in body


def test_cross_cutting_synthesis_lists_per_branch_synthesis_slugs():
    """Cross-cutting page is second-derivative — `synthesizes:` lists
    `synthesis/<slug>` entries for each branch, never raw sources."""
    from gateway import frontmatter as fm

    update = orch._make_cross_cutting_update(
        domain="alpha",
        session_id="sess-1",
        research_query="rq",
        synthesis={"recurring_patterns": {"answer": "ok", "citations": {}, "sources_used": []}},
        source_map={},
        branch_names=["Theme One", "Theme Two", "Theme Three"],
    )
    front, body = fm.parse(update.content)
    expected = sorted({
        "synthesis/sess-1-theme-one",
        "synthesis/sess-1-theme-two",
        "synthesis/sess-1-theme-three",
    })
    assert front.get("synthesizes") == expected
    assert "## Included works" in body
    for slug in expected:
        assert f"[[{slug}]]" in body
    # One-level strict typing: no raw sources in cross-cutting synthesizes
    assert not any(s.startswith("sources/") for s in front["synthesizes"])


def test_cross_cutting_synthesis_omits_synthesizes_when_one_branch():
    """One-branch corpus doesn't aggregate — exemption requires ≥2 entries."""
    from gateway import frontmatter as fm

    update = orch._make_cross_cutting_update(
        domain="alpha",
        session_id="sess-1",
        research_query="rq",
        synthesis={},
        source_map={},
        branch_names=["Only Branch"],
    )
    front, _ = fm.parse(update.content)
    assert "synthesizes" not in front
