"""Server-derived trust tiering (Phase-3 Task 6, G5). EVAL-GATED.

Trust is a server-derived down-weight on _authority_key, never a gate. Self-report
is NEVER an input (G5). A low-trust page that matches the query stays retrievable
(eligibility floor) — trust only reorders.
"""

from __future__ import annotations

import inspect

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.trust import server_trust_tier
from gateway.search_index import IndexHit, _authority_key


@pytest.fixture
def trust_corpus(kb_root):
    """A small corpus with one low-trust source page that matches the query.

    The page is a `web` source with a low filter_score (server-derived low trust)
    but body text that matches — it must still surface (eligibility floor)."""
    src = paths.wiki_dir() / "sources"
    src.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "source", "slug": "low-trust-but-relevant",
        "title": "Low trust but relevant", "domains": ["med"],
        "source_type": "web", "filter_score": 0.05,
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    (src / "low-trust-but-relevant.md").write_text(
        fm.serialize(front, "## Body\n\nfood noise reward blunting discussion.\n")
    )
    concepts = paths.wiki_dir() / "concepts"
    concepts.mkdir(parents=True, exist_ok=True)
    cfront = {
        "type": "concept", "slug": "food-noise", "title": "Food noise",
        "domains": ["med"], "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
    }
    (concepts / "food-noise.md").write_text(
        fm.serialize(cfront, "## Def\n\nfood noise is intrusive food thoughts; reward.\n")
    )
    search_index.refresh(rebuild=True)
    return kb_root


def test_server_trust_is_source_derived_not_self_reported():
    high = server_trust_tier("pubmed", filter_score=0.9)
    low = server_trust_tier("web", filter_score=0.1)
    assert high > low


def test_self_reported_trust_is_ignored_by_server_tier():
    # The function takes NO self-report argument — a buggy agent cannot inflate it (G5).
    assert "self_report" not in inspect.signature(server_trust_tier).parameters
    assert "self_reported_trust" not in inspect.signature(server_trust_tier).parameters


def test_trust_neutral_at_half_is_authority_neutral():
    # A page at trust 0.5 contributes nothing to the authority key (centered).
    base = IndexHit(rel_path="a.md", slug="a", title="A", page_type="concept",
                    domain="med", heading="", snippet="", score=0, rank=1.0,
                    inbound_count=0, draft=False)
    neutral = IndexHit(rel_path="a.md", slug="a", title="A", page_type="concept",
                       domain="med", heading="", snippet="", score=0, rank=1.0,
                       inbound_count=0, draft=False, trust=0.5)
    assert _authority_key(base) == _authority_key(neutral)


def test_higher_trust_lifts_authority_key():
    lo = IndexHit(rel_path="a.md", slug="a", title="A", page_type="concept",
                  domain="med", heading="", snippet="", score=0, rank=1.0,
                  inbound_count=0, draft=False, trust=0.2)
    hi = IndexHit(rel_path="b.md", slug="b", title="B", page_type="concept",
                  domain="med", heading="", snippet="", score=0, rank=1.0,
                  inbound_count=0, draft=False, trust=0.9)
    assert _authority_key(hi) > _authority_key(lo)


def test_low_trust_page_stays_in_candidate_set(trust_corpus):
    # A low-trust page that matches the query must still be retrievable — trust is
    # a tiebreaker, never a gate (eligibility floor).
    hits = search_index.search_fts("food noise reward", order="authority", limit=20)
    slugs = {h.slug for h in hits}
    assert "low-trust-but-relevant" in slugs, slugs
