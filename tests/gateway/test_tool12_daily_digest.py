"""TOOL-12: wiki routine daily-domain-digest tests."""

from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import pytest

from gateway import frontmatter as fm, paths, validator
from gateway.validator import validate_synthesizes_integrity
from gateway.ops.daily_digest import (
    _build_page,
    _build_prompt,
    _find_new_sources,
    _is_after,
    _page_path,
    run_all_domains,
    run_daily_domain_digest,
)


# --- helpers ----------------------------------------------------------------


def _make_raw_source(
    kb_root: Path,
    source_id: str,
    domain: str = "test-domain",
    hours_ago: float = 1.0,
) -> Path:
    from gateway import validator as v
    ingested_at = (
        datetime.now(timezone.utc) - timedelta(hours=hours_ago)
    ).strftime("%Y-%m-%dT%H:%M:%SZ")
    body = f"Body text for {source_id}."
    p = paths.raw_source_path("web", source_id)
    p.parent.mkdir(parents=True, exist_ok=True)
    front: dict[str, Any] = {
        "id": source_id,
        "title": f"Title for {source_id}",
        "type": "web",
        "ingested_at": ingested_at,
        "content_hash": v.compute_content_hash(body),
        "domains": [domain] if domain else [],
    }
    p.write_text(fm.serialize(front, body))
    return p


def _make_policy(kb_root: Path, domain: str) -> Path:
    pd = paths.policies_dir() / domain
    pd.mkdir(parents=True, exist_ok=True)
    p = pd / "policy.yaml"
    p.write_text(f"domain: {domain}\n")
    return p


class _StubClient:
    def __init__(self, response: str = "Stub summary text."):
        self.response = response
        self.calls: list[str] = []

    def call(self, prompt: str) -> str:
        self.calls.append(prompt)
        return self.response


# --- unit tests: helpers ----------------------------------------------------


def test_is_after_true():
    recent = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert _is_after(recent, cutoff)


def test_is_after_false():
    old = (datetime.now(timezone.utc) - timedelta(hours=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert not _is_after(old, cutoff)


def test_is_after_bad_input():
    assert not _is_after("not-a-date", "2026-01-01T00:00:00Z")


def test_page_path(kb_root: Path):
    p = _page_path("glp1", "2026-05-26")
    assert p == paths.wiki_dir() / "synthesis" / "daily-glp1-2026-05-26.md"


def test_build_prompt_includes_domain_and_sources():
    sources = [{"id": "web-abc", "title": "Article A", "body": "Content A"}]
    prompt = _build_prompt("glp1", sources)
    assert "glp1" in prompt
    assert "web-abc" in prompt
    assert "Article A" in prompt


def test_build_page_has_required_sections(kb_root: Path):
    content = _build_page("glp1", "2026-05-26", ["web-abc", "web-def"], "Summary text.")
    front, body = fm.parse(content)
    assert front["type"] == "synthesis"
    assert front["draft"] is True
    assert "sources/web-abc" in front["synthesizes"]
    assert "## Summary" in body
    assert "## Included works" in body
    assert "[[sources/web-abc]]" in body


def test_build_page_synthesizes_mirrors_included_works(kb_root: Path):
    content = _build_page("glp1", "2026-05-26", ["web-abc"], "Summary.")
    front, body = fm.parse(content)
    result = validate_synthesizes_integrity(front, body)
    assert not result.errors, result.errors


# --- _find_new_sources ------------------------------------------------------


def test_find_new_sources_empty(kb_root: Path):
    sources = _find_new_sources("test-domain", "2026-01-01T00:00:00Z")
    assert sources == []


def test_find_new_sources_recent(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-abc", domain="test-domain", hours_ago=1.0)
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    sources = _find_new_sources("test-domain", cutoff)
    assert any(s["id"] == "web-2026-05-26-abc" for s in sources)


def test_find_new_sources_old_excluded(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-old", domain="test-domain", hours_ago=48.0)
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    sources = _find_new_sources("test-domain", cutoff)
    assert not any(s["id"] == "web-2026-05-26-old" for s in sources)


def test_find_new_sources_wrong_domain_excluded(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-xyz", domain="other-domain", hours_ago=1.0)
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    sources = _find_new_sources("test-domain", cutoff)
    assert not any(s["id"] == "web-2026-05-26-xyz" for s in sources)


# --- run_daily_domain_digest ------------------------------------------------


def test_run_skips_when_no_new_sources(kb_root: Path):
    client = _StubClient()
    result = run_daily_domain_digest("test-domain", client=client, date_str="2026-05-26")
    assert result.success
    assert result.data.get("skipped")
    assert result.data.get("reason") == "insufficient_sources"
    assert len(client.calls) == 0


def test_run_writes_page_with_new_source(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-r1", domain="test-domain", hours_ago=1.0)
    client = _StubClient("Stub synthesis output.")
    result = run_daily_domain_digest("test-domain", client=client, date_str="2026-05-26")
    assert result.success
    assert not result.data.get("skipped")
    page = paths.wiki_dir() / "synthesis" / "daily-test-domain-2026-05-26.md"
    assert page.exists()
    content = page.read_text()
    assert "Stub synthesis output." in content
    assert "## Included works" in content


def test_run_idempotent_already_exists(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-r2", domain="test-domain", hours_ago=1.0)
    client = _StubClient()
    run_daily_domain_digest("test-domain", client=client, date_str="2026-05-26")
    # Run again — should skip
    result2 = run_daily_domain_digest("test-domain", client=client, date_str="2026-05-26")
    assert result2.success
    assert result2.data.get("reason") == "already_exists"
    assert len(client.calls) == 1  # only called once


def test_run_llm_error_returns_failure(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-r3", domain="test-domain", hours_ago=1.0)

    class _BrokenClient:
        def call(self, prompt: str) -> str:
            raise RuntimeError("network down")

    result = run_daily_domain_digest("test-domain", client=_BrokenClient(), date_str="2026-05-26")
    assert not result.success
    assert "LLM call failed" in result.summary


def test_run_result_data_fields(kb_root: Path):
    _make_raw_source(kb_root, "web-2026-05-26-r4", domain="test-domain", hours_ago=1.0)
    client = _StubClient()
    result = run_daily_domain_digest("test-domain", client=client, date_str="2026-05-26")
    assert result.data.get("domain") == "test-domain"
    assert result.data.get("date") == "2026-05-26"
    assert result.data.get("sources") == 1


# --- run_all_domains --------------------------------------------------------


def test_run_all_no_domains(kb_root: Path):
    result = run_all_domains(client=_StubClient())
    assert result.success
    assert result.data.get("domains") == 0


def test_run_all_with_policy(kb_root: Path):
    _make_policy(kb_root, "domain-a")
    _make_raw_source(kb_root, "web-2026-05-26-a1", domain="domain-a", hours_ago=1.0)
    result = run_all_domains(client=_StubClient("All-domain output."), date_str="2026-05-26")
    assert result.success
    assert result.data.get("written", 0) >= 1


# --- MCP registration -------------------------------------------------------


def test_mcp_wiki_routine_registered():
    from gateway import mcp_server
    assert callable(getattr(mcp_server, "wiki_routine", None))
