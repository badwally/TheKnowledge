"""Tests for wiki list-domains and wiki list-concepts (discoverability commands)."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm
from gateway.ops.list_domains import list_domains
from gateway.ops.list_concepts import list_concepts


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_policy(kb_root: Path, slug: str, topic: str = "") -> None:
    pol_dir = kb_root / ".knowledge" / "policies" / slug
    pol_dir.mkdir(parents=True, exist_ok=True)
    data = {"domain": {"slug": slug, "topic": topic or f"{slug} domain."}}
    (pol_dir / "policy.yaml").write_text(yaml.dump(data))


def _write_concept(kb_root: Path, slug: str, domains: list[str],
                   canonical_name: str = "") -> Path:
    p = kb_root / "wiki" / "concepts" / f"{slug}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm.serialize(
        {"type": "concept", "slug": slug,
         "canonical_name": canonical_name or slug,
         "domains": domains},
        f"# {slug}\n\nBody.\n",
    ))
    return p


def _write_synthesis(kb_root: Path, slug: str, domains: list[str]) -> Path:
    p = kb_root / "wiki" / "synthesis" / f"{slug}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm.serialize(
        {"type": "synthesis", "slug": slug,
         "title": f"Synthesis: {slug}",
         "domains": domains,
         "question": "What?",
         "synthesizes": [],
         "sources_count": 0},
        f"# {slug}\n\nBody.\n",
    ))
    return p


# ---------------------------------------------------------------------------
# list_domains
# ---------------------------------------------------------------------------

def test_list_domains_returns_blessed_domains(kb_root):
    _write_policy(kb_root, "glp1", "GLP-1 receptor agonists and metabolic health.")
    _write_policy(kb_root, "orita-cmo", "Strategic knowledge base for the CMO of Orita.")
    result = list_domains()
    assert result.success
    assert "glp1" in result.summary
    assert "orita-cmo" in result.summary


def test_list_domains_shows_page_count(kb_root):
    _write_policy(kb_root, "glp1", "GLP-1.")
    _write_concept(kb_root, "food-noise", ["glp1"])
    _write_concept(kb_root, "reward-blunting", ["glp1"])
    result = list_domains()
    assert result.success
    # 2 pages tagged to glp1 should appear in the count column
    assert "2" in result.summary


def test_list_domains_empty_when_no_policies(kb_root):
    result = list_domains()
    assert result.success
    assert "no blessed domains" in result.summary


def test_list_domains_json(kb_root):
    import json
    _write_policy(kb_root, "glp1", "GLP-1.")
    result = list_domains(fmt="json")
    assert result.success
    rows = json.loads(result.summary)
    assert isinstance(rows, list)
    assert rows[0]["slug"] == "glp1"
    assert "wiki_pages" in rows[0]


def test_list_domains_ignores_dirs_without_policy_yaml(kb_root):
    # A directory without policy.yaml (e.g. a draft/proposal dir) should be skipped.
    orphan = kb_root / ".knowledge" / "policies" / "draft-domain"
    orphan.mkdir(parents=True, exist_ok=True)
    result = list_domains()
    assert result.success
    assert "draft-domain" not in result.summary


# ---------------------------------------------------------------------------
# list_concepts
# ---------------------------------------------------------------------------

def test_list_concepts_returns_all_concepts(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    _write_concept(kb_root, "reward-blunting", ["glp1"], "Reward Blunting")
    result = list_concepts()
    assert result.success
    assert "food-noise" in result.summary
    assert "reward-blunting" in result.summary


def test_list_concepts_filters_by_domain(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    _write_concept(kb_root, "agency-gtm", ["orita-cmo"], "Agency GTM")
    result = list_concepts(domain="glp1")
    assert result.success
    assert "food-noise" in result.summary
    assert "agency-gtm" not in result.summary


def test_list_concepts_canonical_name_in_output(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    result = list_concepts(domain="glp1")
    assert "Food Noise" in result.summary


def test_list_concepts_tab_separated(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    result = list_concepts(domain="glp1")
    assert "\t" in result.summary
    slug, name = result.summary.strip().split("\t")
    assert slug == "food-noise"
    assert name == "Food Noise"


def test_list_concepts_kind_synthesis(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    _write_synthesis(kb_root, "2026-01-01-glp1-summary", ["glp1"])
    result = list_concepts(domain="glp1", kind="synthesis")
    assert result.success
    assert "2026-01-01-glp1-summary" in result.summary
    assert "food-noise" not in result.summary


def test_list_concepts_kind_all(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    _write_synthesis(kb_root, "2026-01-01-glp1-summary", ["glp1"])
    result = list_concepts(domain="glp1", kind="all")
    assert result.success
    assert "food-noise" in result.summary
    assert "2026-01-01-glp1-summary" in result.summary


def test_list_concepts_empty_domain(kb_root):
    _write_concept(kb_root, "food-noise", ["glp1"])
    result = list_concepts(domain="nonexistent-domain")
    assert result.success
    assert "no concepts pages found" in result.summary or "no concept" in result.summary


def test_list_concepts_json(kb_root):
    import json
    _write_concept(kb_root, "food-noise", ["glp1"], "Food Noise")
    result = list_concepts(domain="glp1", fmt="json")
    assert result.success
    rows = json.loads(result.summary)
    assert rows[0]["slug"] == "food-noise"
    assert rows[0]["name"] == "Food Noise"
