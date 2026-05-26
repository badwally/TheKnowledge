"""Tests for AGT-1 — inbox-triage agent.

Acceptance criteria:
- Event triggers run_triage (subscribe → matching event → run_triage called)
- Domain-present path: filter score written to source frontmatter
- Domain-absent, confident inference: domain tag applied + filter score written
- Domain-absent, ambiguous: "needs-domain" tag applied, no filter call
- Review-band source: written to .knowledge/triage/<id>.yaml
- No autonomous filter-correct call
- wiki triage list shows review-band sources
- wiki status shows triage depth
- NEVER filters when domain is "needs-domain"
"""

from __future__ import annotations

import yaml
from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.agents.inbox_triage import (
    run_triage,
    TriageResult,
    triage_list,
    triage_depth,
)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _make_raw_source(
    kb_root: Path,
    source_id: str,
    source_type: str = "web",
    domains: list[str] | None = None,
    title: str = "A test article",
    tags: list[str] | None = None,
) -> Path:
    p = kb_root / "raw" / source_type / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "type": source_type,
        "title": title,
        "url": f"https://example.com/{source_id}",
    }
    if domains:
        front["domains"] = domains
    if tags:
        front["tags"] = tags
    p.write_text(fm.serialize(front, f"# {title}\n\nBody text.\n"))
    return p


def _make_policy(kb_root: Path, domain_slug: str, description: str) -> None:
    policy_dir = kb_root / ".knowledge" / "policies" / domain_slug
    policy_dir.mkdir(parents=True, exist_ok=True)
    (policy_dir / "policy.yaml").write_text(
        yaml.dump({
            "domain_slug": domain_slug,
            "version": "v1",
            "domain_topic": description,
            "domain_description": description,
            "filter": {
                "threshold_include": 0.70,
                "threshold_review": 0.50,
            },
            "inclusion_criteria": [],
            "exclusion_criteria": [],
        })
    )


class _StubFilterClient:
    """Minimal FilterClient stub — only exposes call(), so score() uses the else branch."""

    def __init__(self, score_val: float) -> None:
        self._score_val = score_val
        self.call_count = 0

    def call(self, prompt: str) -> str:
        import json as _json
        self.call_count += 1
        return _json.dumps({"score": self._score_val, "rationale": "test rationale"})


def _mock_filter_client(score: float) -> _StubFilterClient:
    return _StubFilterClient(score)


# ---------------------------------------------------------------------------
# domain-present path
# ---------------------------------------------------------------------------


def test_domain_present_filter_score_written_to_source_frontmatter(kb_root):
    _make_raw_source(kb_root, "web-2026-01-01-aaa", domains=["glp1"], title="GLP1 research")
    _make_policy(kb_root, "glp1", "glucagon-like peptide obesity weight loss")

    client = _mock_filter_client(0.80)
    result = run_triage("web-2026-01-01-aaa", filter_client=client)

    assert result.source_id == "web-2026-01-01-aaa"
    assert result.filter_score is not None
    # Score written to source frontmatter
    source_path = kb_root / "raw" / "web" / "web-2026-01-01-aaa.md"
    front, _ = fm.parse(source_path.read_text())
    assert front.get("filter") is not None
    assert front["filter"]["score"] is not None


def test_domain_present_no_policy_skips_filter(kb_root):
    _make_raw_source(kb_root, "web-2026-01-01-bbb", domains=["unknown-domain"])

    client = _mock_filter_client(0.80)
    result = run_triage("web-2026-01-01-bbb", filter_client=client)

    # No policy → filter skipped gracefully, no crash
    assert result.source_id == "web-2026-01-01-bbb"
    assert result.filter_score is None


# ---------------------------------------------------------------------------
# domain-absent paths
# ---------------------------------------------------------------------------


def test_domain_absent_confident_inference_tags_domain(kb_root):
    """Single policy matches title ≥ 0.6 confidence → domain tagged + filter run."""
    _make_raw_source(
        kb_root,
        "web-2026-01-01-ccc",
        domains=[],
        title="glucagon peptide weight loss obesity study",
    )
    _make_policy(kb_root, "glp1", "glucagon-like peptide obesity weight loss")

    client = _mock_filter_client(0.80)
    result = run_triage("web-2026-01-01-ccc", filter_client=client)

    assert result.domain == "glp1"
    source_path = kb_root / "raw" / "web" / "web-2026-01-01-ccc.md"
    front, _ = fm.parse(source_path.read_text())
    assert "glp1" in (front.get("domains") or [])
    assert front.get("filter") is not None


def test_domain_absent_ambiguous_tags_needs_domain(kb_root):
    """Two policies both above 0.4 → needs-domain, no filter call."""
    _make_raw_source(
        kb_root,
        "web-2026-01-01-ddd",
        domains=[],
        title="glucagon peptide weight loss cancer treatment",
    )
    _make_policy(kb_root, "glp1", "glucagon peptide weight loss obesity")
    _make_policy(kb_root, "oncology", "cancer treatment peptide therapy weight")

    client = _mock_filter_client(0.80)
    result = run_triage("web-2026-01-01-ddd", filter_client=client)

    assert result.domain == "needs-domain"
    assert result.filter_score is None
    source_path = kb_root / "raw" / "web" / "web-2026-01-01-ddd.md"
    front, _ = fm.parse(source_path.read_text())
    assert "needs-domain" in (front.get("domains") or [])
    # filter_client not called
    assert client.call_count == 0


def test_domain_absent_no_match_tags_needs_domain(kb_root):
    """No policy matches above threshold → needs-domain, no filter."""
    _make_raw_source(
        kb_root,
        "web-2026-01-01-eee",
        domains=[],
        title="unrelated quantum computing topic",
    )
    _make_policy(kb_root, "glp1", "glucagon peptide weight loss obesity")

    client = _mock_filter_client(0.80)
    result = run_triage("web-2026-01-01-eee", filter_client=client)

    assert result.domain == "needs-domain"
    assert result.filter_score is None


def test_needs_domain_tag_never_triggers_filter(kb_root):
    """Source already tagged needs-domain → filter not called."""
    _make_raw_source(
        kb_root,
        "web-2026-01-01-fff",
        domains=["needs-domain"],
    )
    _make_policy(kb_root, "glp1", "glucagon peptide obesity")

    client = _mock_filter_client(0.80)
    run_triage("web-2026-01-01-fff", filter_client=client)

    assert client.call_count == 0


# ---------------------------------------------------------------------------
# review band → triage file written
# ---------------------------------------------------------------------------


def test_review_band_source_writes_triage_yaml(kb_root):
    _make_raw_source(kb_root, "web-2026-01-01-ggg", domains=["glp1"], title="Marginal GLP1 piece")
    _make_policy(kb_root, "glp1", "glucagon peptide weight loss obesity")

    # Score in review band: threshold_review=0.50 <= score < threshold_include=0.70
    client = _mock_filter_client(0.60)
    result = run_triage("web-2026-01-01-ggg", filter_client=client)

    assert result.in_review_band is True
    triage_file = kb_root / ".knowledge" / "triage" / "web-2026-01-01-ggg.yaml"
    assert triage_file.exists()
    data = yaml.safe_load(triage_file.read_text())
    assert data["source_id"] == "web-2026-01-01-ggg"
    assert data["filter_score"] == pytest.approx(0.60, abs=0.05)


def test_non_review_band_no_triage_file(kb_root):
    _make_raw_source(kb_root, "web-2026-01-01-hhh", domains=["glp1"], title="Great GLP1 piece")
    _make_policy(kb_root, "glp1", "glucagon peptide weight loss obesity")

    client = _mock_filter_client(0.90)
    result = run_triage("web-2026-01-01-hhh", filter_client=client)

    assert result.in_review_band is False
    triage_file = kb_root / ".knowledge" / "triage" / "web-2026-01-01-hhh.yaml"
    assert not triage_file.exists()


# ---------------------------------------------------------------------------
# triage list + status depth
# ---------------------------------------------------------------------------


def test_triage_list_shows_review_band_sources(kb_root):
    _make_raw_source(kb_root, "web-2026-01-01-iii", domains=["glp1"], title="Review piece")
    _make_policy(kb_root, "glp1", "glucagon peptide weight loss obesity")

    client = _mock_filter_client(0.60)
    run_triage("web-2026-01-01-iii", filter_client=client)

    items = triage_list()
    source_ids = [item["source_id"] for item in items]
    assert "web-2026-01-01-iii" in source_ids


def test_triage_depth_reflects_triage_files(kb_root):
    triage_dir = kb_root / ".knowledge" / "triage"
    triage_dir.mkdir(parents=True, exist_ok=True)
    (triage_dir / "web-2026-01-01-jjj.yaml").write_text(
        yaml.dump({"source_id": "web-2026-01-01-jjj", "filter_score": 0.55})
    )
    (triage_dir / "web-2026-01-01-kkk.yaml").write_text(
        yaml.dump({"source_id": "web-2026-01-01-kkk", "filter_score": 0.60})
    )

    assert triage_depth() == 2


def test_triage_depth_zero_when_no_files(kb_root):
    assert triage_depth() == 0
