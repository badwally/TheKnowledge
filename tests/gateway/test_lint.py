"""Tests for M9: lint orchestrator + the six cheap checks."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm
from gateway import nlm_registry, paths
from gateway.lint import (
    LintFinding,
    citation_density,
    inbox_pending,
    nlm_pending,
    orphans,
    schema_drift,
    stale_drafts,
)
from gateway.ops.lint import KNOWN_CHECKS, lint


# --- helpers ---------------------------------------------------------------


def _write_concept(slug: str, *, body: str | None = None, draft: bool = False, started_days_ago: int | None = None, domains: list[str] | None = None) -> Path:
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug.replace("-", " "),
        "domains": domains or ["d-test"],
    }
    if draft:
        front["draft"] = True
        if started_days_ago is not None:
            started = datetime.now(timezone.utc) - timedelta(days=started_days_ago)
            front["draft_started_at"] = started.strftime("%Y-%m-%dT%H:%M:%SZ")
            front["draft_unresolved_claims"] = 3

    body = body or (
        f"# {slug}\n\n"
        f"## Summary\n\nA solid claim with a citation [[sources/yt-x]].\n\n"
        f"## Key claims\n\n- another claim [[sources/yt-x]]\n\n"
        f"## Sources\n\n- [[sources/yt-x]]\n\n"
        f"## Related\n\n- [[concepts/related-thing]]\n"
    )
    target = paths.wiki_dir() / "concepts" / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, body))
    return target


def _write_source_in_raw(source_id: str, *, score: float = 0.9, domain: str = "d-test", nlm_corpus_ids: list[str] | None = None) -> Path:
    front = {
        "id": source_id,
        "type": "youtube",
        "title": f"Title {source_id}",
        "url": f"https://example.com/{source_id}",
        "ingested_at": "2026-04-28T12:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
        "domains": [domain],
        "nlm_corpus_ids": nlm_corpus_ids or [],
        "wiki_pages": [],
        "meta": {},
        "filter": {
            "score": score,
            "policy_version": f"{domain}-v1",
            "rationale": "test",
            "decided_at": "2026-04-28T12:00:00Z",
            "user_correction": None,
        },
    }
    target = paths.raw_source_path("youtube", source_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, "body"))
    return target


# --- orchestrator ---------------------------------------------------------


def test_known_checks_includes_all_documented_checks():
    expected = {
        "orphans",
        "stale-drafts",
        "stale-claims",
        "contradictions",
        "missing-pages",
        "citation-density",
        "schema-drift",
        "filter-calibration",
        "inbox-pending",
        "nlm-pending",
    }
    assert KNOWN_CHECKS == expected


def test_lint_writes_report_and_log_entry(kb_root):
    result = lint()
    assert result.success
    # A report file lives under .knowledge/lint/
    reports = list(paths.lint_dir().glob("*.md"))
    assert len(reports) == 1
    text = reports[0].read_text()
    assert "# Lint Report" in text
    assert "## Summary" in text
    # Log entry written
    log_text = paths.log_path().read_text()
    assert "lint" in log_text


def test_lint_unknown_scope_errors(kb_root):
    result = lint(scope="not-a-real-check")
    assert not result.success
    assert any("unknown lint scope" in e for e in result.errors)


def test_lint_scope_runs_only_one_check(kb_root):
    result = lint(scope="orphans")
    assert result.success
    reports = list(paths.lint_dir().glob("*-orphans.md"))
    assert reports


# --- orphans --------------------------------------------------------------


def test_orphans_flags_concept_with_no_inbound_links(kb_root):
    _write_concept("alpha")  # no other page links to it
    findings = orphans.run()
    paths_flagged = [f.path for f in findings]
    assert any("concepts/alpha" in p for p in paths_flagged)


def test_orphans_does_not_flag_linked_concept(kb_root):
    _write_concept(
        "alpha",
        body=(
            "# alpha\n\n"
            "## Summary\n\nclaim [[sources/yt-x]]\n\n"
            "## Key claims\n\n- [[sources/yt-x]]\n\n"
            "## Sources\n\n- [[sources/yt-x]]\n\n"
            "## Related\n\n- [[concepts/beta]]\n"
        ),
    )
    _write_concept(
        "beta",
        body=(
            "# beta\n\n"
            "## Summary\n\nlinks back to [[concepts/alpha]] [[sources/yt-x]]\n\n"
            "## Key claims\n\n- [[sources/yt-x]]\n\n"
            "## Sources\n\n- [[sources/yt-x]]\n\n"
            "## Related\n\n- [[concepts/alpha]]\n"
        ),
    )
    findings = orphans.run()
    flagged = [f.path for f in findings]
    # Both pages link to each other, so neither is orphan
    assert not any("concepts/alpha" in p for p in flagged)
    assert not any("concepts/beta" in p for p in flagged)


def test_orphans_exempts_mocs(kb_root):
    moc_front = {"type": "moc", "slug": "test-moc", "domain": "d-test"}
    moc_body = (
        "# Test MOC\n\n"
        "## Overview\n\nx\n\n"
        "## Key entities\n\n-\n\n"
        "## Key concepts\n\n-\n\n"
        "## Synthesis pages\n\n-\n"
    )
    target = paths.wiki_dir() / "mocs" / "test-moc.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(moc_front, moc_body))

    findings = orphans.run()
    flagged = [f.path for f in findings]
    assert not any("mocs/test-moc" in p for p in flagged)


# --- stale-drafts ---------------------------------------------------------


def test_stale_drafts_flags_old_drafts(kb_root):
    _write_concept("old-draft", draft=True, started_days_ago=30)
    findings = stale_drafts.run(threshold_days=7)
    assert len(findings) == 1
    assert findings[0].metadata["age_days"] >= 30


def test_stale_drafts_does_not_flag_fresh_drafts(kb_root):
    _write_concept("fresh-draft", draft=True, started_days_ago=2)
    findings = stale_drafts.run(threshold_days=7)
    assert findings == []


def test_stale_drafts_skips_non_drafts(kb_root):
    _write_concept("not-draft", draft=False)
    findings = stale_drafts.run(threshold_days=1)
    assert findings == []


# --- citation-density ------------------------------------------------------


def test_citation_density_flags_low_ratio(kb_root):
    body = (
        "# x\n\n"
        "## Summary\n\nThis is an uncited claim sentence with enough words to count.\n\n"
        "Another uncited claim that has plenty of words and no citation.\n\n"
        "## Key claims\n\n- uncited claim with words but no source link.\n\n"
        "## Sources\n\n- [[sources/yt-x]]\n\n"
        "## Related\n\n- [[concepts/y]]\n"
    )
    _write_concept("density-low", body=body)
    findings = citation_density.run(threshold=0.6)
    flagged = [f for f in findings if "density-low" in f.path]
    assert len(flagged) == 1
    assert flagged[0].metadata["total"] >= 2
    assert flagged[0].metadata["ratio"] < 0.6


def test_citation_density_does_not_flag_drafts(kb_root):
    body = (
        "# x\n\n"
        "## Summary\n\nThis is an uncited claim with enough words to be flagged in strict mode.\n\n"
        "## Key claims\n\n- nothing here.\n\n"
        "## Sources\n\n- [[sources/yt-x]]\n\n"
        "## Related\n\n- [[concepts/y]]\n"
    )
    _write_concept("density-draft", draft=True, started_days_ago=1, body=body)
    findings = citation_density.run(threshold=0.99)
    flagged = [f for f in findings if "density-draft" in f.path]
    assert flagged == []


# --- schema-drift ---------------------------------------------------------


def test_schema_drift_flags_missing_section(kb_root):
    front = {
        "type": "concept",
        "slug": "broken",
        "canonical_name": "Broken",
        "domains": ["d-test"],
    }
    body = "# broken\n\n## Summary\n\nshort.\n"  # missing Key claims, Sources, Related
    target = paths.wiki_dir() / "concepts" / "broken.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, body))

    findings = schema_drift.run()
    flagged = [f for f in findings if "broken" in f.path]
    assert flagged
    # Citation-grounding errors are suppressed in schema-drift
    assert not any("citation-grounding" in (f.metadata.get("rule") or "") for f in flagged)


def test_schema_drift_clean_page_no_findings(kb_root):
    _write_concept("clean")
    findings = schema_drift.run()
    flagged = [f for f in findings if "clean" in f.path]
    assert flagged == []


# --- inbox-pending --------------------------------------------------------


def test_inbox_pending_counts_md_only(kb_root):
    inbox = paths.raw_dir() / "inbox"
    (inbox / "ready.md").write_text("---\nid: x\n---\nbody")
    (inbox / "ignore.txt").write_text("not a markdown file")
    findings = inbox_pending.run()
    assert any(f.metadata.get("count") == 1 and f.metadata.get("kind") != "failed" for f in findings)


def test_inbox_pending_reports_failed_dir_separately(kb_root):
    failed = paths.raw_dir() / "inbox" / "_failed"
    failed.mkdir(parents=True, exist_ok=True)
    (failed / "20260427T030000Z-bad.md").write_text("malformed")
    findings = inbox_pending.run()
    assert any(f.metadata.get("kind") == "failed" for f in findings)


def test_inbox_pending_empty_returns_no_findings(kb_root):
    findings = inbox_pending.run()
    assert findings == []


# --- nlm-pending ----------------------------------------------------------


def _write_policy(domain: str, threshold_include: float = 0.7) -> Path:
    target_dir = paths.policies_dir() / domain
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / "policy.yaml"
    path.write_text(yaml.safe_dump({
        "domain": {"slug": domain},
        "filter": {
            "threshold_include": threshold_include,
            "threshold_review": 0.5,
        },
    }))
    return path


def test_nlm_pending_flags_eligible_unsync_source(kb_root):
    nlm_registry.register("d-test", "nb-12345")
    _write_policy("d-test", threshold_include=0.7)
    _write_source_in_raw("yt-eligible", score=0.85, domain="d-test", nlm_corpus_ids=[])

    findings = nlm_pending.run()
    flagged = [f for f in findings if "yt-eligible" in f.message]
    assert len(flagged) == 1
    assert flagged[0].metadata["domain"] == "d-test"


def test_nlm_pending_skips_already_synced(kb_root):
    nlm_registry.register("d-test", "nb-12345")
    _write_policy("d-test", threshold_include=0.7)
    _write_source_in_raw("yt-synced", score=0.9, domain="d-test", nlm_corpus_ids=["nb-12345"])

    findings = nlm_pending.run()
    assert not any("yt-synced" in f.message for f in findings)


def test_nlm_pending_skips_below_threshold(kb_root):
    nlm_registry.register("d-test", "nb-12345")
    _write_policy("d-test", threshold_include=0.8)
    _write_source_in_raw("yt-low", score=0.4, domain="d-test", nlm_corpus_ids=[])

    findings = nlm_pending.run()
    assert not any("yt-low" in f.message for f in findings)


def test_nlm_pending_no_registry_no_findings(kb_root):
    _write_source_in_raw("yt-anything", score=0.95, domain="d-test")
    assert nlm_pending.run() == []


# --- missing-pages (M15) --------------------------------------------------


from gateway.lint import missing_pages


class _StubClient:
    """Stub FilterClient that returns a canned response and records the prompt."""

    def __init__(self, response: str):
        self.response = response
        self.prompts: list[str] = []

    def call(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return self.response


def _write_moc(slug: str, *, domain: str = "d-test", body: str | None = None) -> Path:
    front = {"type": "moc", "slug": slug, "domain": domain}
    body = body or f"# {slug}\n\n## Overview\n\n"
    target = paths.wiki_dir() / "mocs" / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, body))
    return target


def test_missing_pages_empty_wiki_makes_no_call(kb_root):
    client = _StubClient(response='{"missing": []}')
    findings = missing_pages.run(client=client)
    assert findings == []
    assert client.prompts == []


def test_missing_pages_returns_findings_per_domain(kb_root):
    _write_concept("a", domains=["d-x"])
    _write_concept("b", domains=["d-x"])
    _write_moc("d-x", domain="d-x")

    client = _StubClient(
        response='{"missing": [{"name": "Acme Corp", "kind": "entity", "slug": "acme-corp", "occurrences_estimate": 5, "rationale": "appears in 5 pages"}]}'
    )
    findings = missing_pages.run(client=client)
    assert len(findings) == 1
    assert findings[0].check == "missing-pages"
    assert findings[0].metadata["domain"] == "d-x"
    assert findings[0].metadata["slug"] == "acme-corp"
    assert findings[0].metadata["kind"] == "entity"
    assert "Acme Corp" in findings[0].message
    assert "d-x" in findings[0].message
    assert len(client.prompts) == 1
    assert "Domain: d-x" in client.prompts[0]


def test_missing_pages_calls_once_per_domain(kb_root):
    _write_concept("a", domains=["d-x"])
    _write_concept("c", domains=["d-y"])
    _write_moc("d-x", domain="d-x")
    _write_moc("d-y", domain="d-y")

    client = _StubClient(response='{"missing": []}')
    missing_pages.run(client=client)
    assert len(client.prompts) == 2
    assert any("Domain: d-x" in p for p in client.prompts)
    assert any("Domain: d-y" in p for p in client.prompts)


def test_missing_pages_drops_suggestions_that_already_exist(kb_root):
    _write_concept("acme-corp", domains=["d-x"])  # already-existing slug
    _write_concept("other", domains=["d-x"])
    _write_moc("d-x", domain="d-x")

    client = _StubClient(
        response='{"missing": [{"name": "ACME Corp", "kind": "entity", "slug": "acme-corp"}, {"name": "Beta Lab", "kind": "concept", "slug": "beta-lab"}]}'
    )
    findings = missing_pages.run(client=client)
    slugs = [f.metadata["slug"] for f in findings]
    assert "acme-corp" not in slugs
    assert "beta-lab" in slugs


def test_missing_pages_dedups_within_response(kb_root):
    _write_concept("a", domains=["d-x"])
    _write_moc("d-x", domain="d-x")

    client = _StubClient(
        response='{"missing": [{"name": "Foo", "kind": "concept", "slug": "foo"}, {"name": "Foo", "kind": "concept", "slug": "foo"}]}'
    )
    findings = missing_pages.run(client=client)
    assert len(findings) == 1


def test_missing_pages_tolerates_code_fences(kb_root):
    _write_concept("a", domains=["d-x"])
    _write_moc("d-x", domain="d-x")

    fenced = '```json\n{"missing": [{"name": "Foo", "kind": "concept", "slug": "foo"}]}\n```'
    client = _StubClient(response=fenced)
    findings = missing_pages.run(client=client)
    assert len(findings) == 1


def test_missing_pages_unparseable_response_yields_no_findings(kb_root):
    _write_concept("a", domains=["d-x"])
    _write_moc("d-x", domain="d-x")

    client = _StubClient(response="I can't help with that.")
    findings = missing_pages.run(client=client)
    assert findings == []


def test_missing_pages_client_failure_emits_warning(kb_root):
    _write_concept("a", domains=["d-x"])
    _write_moc("d-x", domain="d-x")

    class _Failing:
        def call(self, _prompt: str) -> str:
            raise RuntimeError("network down")

    findings = missing_pages.run(client=_Failing())
    assert len(findings) == 1
    assert findings[0].severity == "warning"
    assert "d-x" in findings[0].message


# --- filter-calibration (M16) ---------------------------------------------


from gateway.lint import filter_calibration


class _ScoredClient:
    """Stub FilterClient returning JSON shape that filter.parse_response accepts."""

    def __init__(self, score_value: float = 0.85, rationale: str = "ok"):
        self.score_value = score_value
        self.rationale = rationale
        self.calls = 0

    def call(self, _prompt: str) -> str:
        self.calls += 1
        import json as _json
        return _json.dumps({"score": self.score_value, "rationale": self.rationale})


def test_filter_calibration_no_sources_returns_empty(kb_root):
    findings = filter_calibration.run(client=_ScoredClient())
    assert findings == []


def test_filter_calibration_skips_domain_without_policy(kb_root):
    _write_source_in_raw("yt-no-policy", score=0.8, domain="d-without")
    findings = filter_calibration.run(client=_ScoredClient())
    assert any(
        f.metadata.get("skipped") == "no_policy"
        and f.metadata.get("domain") == "d-without"
        for f in findings
    )


def test_filter_calibration_aligned_scores_no_outliers(kb_root):
    _write_policy("d-cal")
    _write_source_in_raw("yt-a", score=0.85, domain="d-cal")
    _write_source_in_raw("yt-b", score=0.82, domain="d-cal")

    client = _ScoredClient(score_value=0.85)  # within 0.20 of stored
    findings = filter_calibration.run(sample_size=10, client=client)
    summaries = [f for f in findings if f.severity == "info" and f.metadata.get("domain") == "d-cal"]
    outliers = [f for f in findings if f.severity == "warning"]
    assert len(summaries) == 1
    assert summaries[0].metadata["sample_size"] == 2
    assert outliers == []
    assert client.calls == 2


def test_filter_calibration_flags_outliers_above_threshold(kb_root):
    _write_policy("d-cal")
    _write_source_in_raw("yt-drift", score=0.20, domain="d-cal")  # stored low

    client = _ScoredClient(score_value=0.95)  # delta = +0.75 -> outlier
    findings = filter_calibration.run(sample_size=10, client=client)
    outliers = [f for f in findings if f.severity == "warning"]
    assert len(outliers) == 1
    assert outliers[0].metadata["source_id"] == "yt-drift"
    assert outliers[0].metadata["delta"] == 0.75


def test_filter_calibration_score_failure_emits_warning(kb_root):
    _write_policy("d-cal")
    _write_source_in_raw("yt-broken", score=0.5, domain="d-cal")

    class _Failing:
        def call(self, _prompt: str) -> str:
            raise RuntimeError("upstream down")

    findings = filter_calibration.run(sample_size=10, client=_Failing())
    assert any(
        f.severity == "warning" and "yt-broken" in f.message
        for f in findings
    )


def test_filter_calibration_sample_caps_at_population_size(kb_root):
    _write_policy("d-cal")
    _write_source_in_raw("yt-a", score=0.7, domain="d-cal")

    client = _ScoredClient(score_value=0.7)
    filter_calibration.run(sample_size=99, client=client)
    assert client.calls == 1


def test_filter_calibration_runs_independently_per_domain(kb_root):
    _write_policy("d-x")
    _write_source_in_raw("yt-x1", score=0.6, domain="d-x")
    # d-y has source but no policy -> skipped, doesn't poison d-x
    _write_source_in_raw("yt-y1", score=0.6, domain="d-y")

    client = _ScoredClient(score_value=0.6)
    findings = filter_calibration.run(sample_size=10, client=client)

    skipped = [f for f in findings if f.metadata.get("skipped") == "no_policy"]
    summaries = [f for f in findings if f.severity == "info" and f.metadata.get("sample_size")]
    assert len(skipped) == 1 and skipped[0].metadata["domain"] == "d-y"
    assert len(summaries) == 1 and summaries[0].metadata["domain"] == "d-x"
    assert client.calls == 1
