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
