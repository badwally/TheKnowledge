"""WS2: wiki retrieve composite RAG primitive tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.ops.retrieve import is_placeholder_section, retrieve, retrieve_op


def _page(slug: str, title: str, body: str, domain: str = "d", draft: bool = False) -> None:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept", "slug": slug, "title": title, "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    if draft:
        front["draft"] = True
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def test_retrieve_returns_wrapped_block(kb_root: Path):
    _page(
        "gastric", "Gastric emptying",
        "## Mechanism\n\nThe drug delays gastric emptying via vagal signaling.\n",
    )
    search_index.refresh(rebuild=True)
    block, sections = retrieve("gastric emptying vagal", domain="d")
    assert sections
    assert "<page " in block and "</page>" in block
    assert 'section="Mechanism"' in block
    assert "vagal signaling" in block


def test_retrieve_preserves_source_citations(kb_root: Path):
    _page(
        "cited", "Cited concept",
        "## Body\n\nA claim grounded in evidence [[sources/web-2026-01-01-abc]].\n",
    )
    search_index.refresh(rebuild=True)
    block, _ = retrieve("claim grounded evidence", domain="d")
    assert "[[sources/web-2026-01-01-abc]]" in block


def test_retrieve_respects_budget(kb_root: Path):
    for i in range(6):
        _page(f"p{i}", f"Page {i}", f"## S{i}\n\n" + ("token alpha " * 200) + "\n")
    search_index.refresh(rebuild=True)
    block, sections = retrieve("token alpha", domain="d", budget_chars=1500)
    assert len(block) <= 1500 + 2000  # last section may overshoot by one block
    assert len(sections) < 6


def test_retrieve_caps_section_size(kb_root: Path):
    _page("big", "Big page", "## Huge\n\n" + ("word " * 5000) + "\n")
    search_index.refresh(rebuild=True)
    _block, sections = retrieve("word", domain="d", max_section_chars=500)
    assert sections
    assert "[section truncated]" in sections[0].text
    assert len(sections[0].text) <= 600


# ---- Hole 1: draft visibility (demote-not-exclude + section content-gate) ----
# Brief: docs/260622_rag-retrieval-draft-visibility-brief.md.
# The legacy migration committed ~1,100 curated concept/entity/synthesis pages as
# draft:true. Hard-excluding drafts from `retrieve` made the curated layer invisible
# to the default agent grounding path. Fix: admit drafts into the pool (demoted by
# _DRAFT_PENALTY), gate out placeholder-stub *sections* at the section level, and
# annotate surfaced drafts so consumers know provenance is unfinalized.

# Marker family verified on disk 2026-06-23: a placeholder section's body is a lone
# markdown-italic parenthetical (`_(...)_`) and nothing else. ~1,090 occurrences span
# _(needs population from legacy import)_, _(summary not yet generated …)_,
# _(claims not yet extracted)_, _(no cross-references yet)_, _(no citations returned)_.
_PLACEHOLDER = "_(needs population from legacy import)_"


@pytest.mark.parametrize(
    "text",
    [
        "_(needs population from legacy import)_",
        "_(summary not yet generated — agent-driven authorship lands in M6)_",
        "_(claims not yet extracted)_",
        "_(no cross-references yet)_",
        "_(no citations returned)_",
        "  _(needs population from legacy import)_  \n",  # surrounding whitespace
    ],
)
def test_is_placeholder_section_true(text: str):
    assert is_placeholder_section(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "",  # empty is handled by the empty-section skip, not this predicate
        "Real prose with substance and a [[sources/web-2026-01-01-abc]] citation.",
        # A real section that merely *contains* a parenthetical note is not a stub.
        "_(legacy note)_ followed by substantive grounding content about the topic.",
        # Two parentheticals wrapping real content must not be mistaken for a stub.
        "_(a)_ real content in the middle _(b)_",
        "Body text ending in a parenthetical _(aside)_",
    ],
)
def test_is_placeholder_section_false(text: str):
    assert is_placeholder_section(text) is False


def test_retrieve_admits_substantive_draft(kb_root: Path):
    # G-POS: a draft page with real content is now reachable (was hard-excluded).
    _page("draftp", "Draft term page", "## X\n\nunique draftonly content here.\n", draft=True)
    search_index.refresh(rebuild=True)
    _block, sections = retrieve("draftonly content", domain="d")
    assert [s.slug for s in sections] == ["draftp"]


def test_retrieve_skips_placeholder_section(kb_root: Path):
    # G-NEG-1: a draft whose matched section is a placeholder stub must NOT surface,
    # and the placeholder marker must never leak into the assembled block.
    _page(
        "stub", "Stub page",
        f"## Summary\n\n{_PLACEHOLDER}\n",
        draft=True,
    )
    search_index.refresh(rebuild=True)
    # Query matches the placeholder's own tokens — the only thing that could match.
    block, sections = retrieve("needs population legacy import", domain="d")
    assert all(s.slug != "stub" for s in sections)
    assert "needs population from legacy import" not in block


def test_retrieve_keeps_substantive_section_of_hybrid_draft(kb_root: Path):
    # The dominant legacy draft is HYBRID: real lede/Methods + placeholder sections.
    # The substantive section must surface; the placeholder section must not pollute.
    _page(
        "hybrid", "Hybrid draft",
        "## Methods\n\nReal grounding content about vagal afferent signaling here.\n\n"
        f"## Summary\n\n{_PLACEHOLDER}\n",
        draft=True,
    )
    search_index.refresh(rebuild=True)
    block, sections = retrieve("vagal afferent signaling", domain="d")
    assert [s.slug for s in sections] == ["hybrid"]
    assert 'section="Methods"' in block
    assert "needs population from legacy import" not in block


def test_retrieve_demotes_draft_below_finalized(kb_root: Path):
    # G-NEG-2 / demotion: when a finalized and a draft page match equally, the
    # finalized page outranks the draft (admitted, not promoted over canonical).
    _page("final", "Final page", "## S\n\nsentinel topic alpha content.\n", draft=False)
    _page("drafty", "Drafty page", "## S\n\nsentinel topic alpha content.\n", draft=True)
    search_index.refresh(rebuild=True)
    _block, sections = retrieve("sentinel topic alpha", domain="d")
    slugs = [s.slug for s in sections]
    assert "final" in slugs and "drafty" in slugs
    assert slugs.index("final") < slugs.index("drafty"), f"finalized must outrank draft: {slugs}"


def test_retrieve_annotates_draft_pages(kb_root: Path):
    # Q2: surfaced drafts carry draft="true" so consumers (incl. wiki answer's LLM)
    # know the provenance is unfinalized; finalized pages carry no such marker.
    _page("dft", "Draft annotated", "## S\n\nannotation sentinel content draftside.\n", draft=True)
    _page("fin", "Final annotated", "## S\n\nannotation sentinel content finalside.\n", draft=False)
    search_index.refresh(rebuild=True)
    block, _ = retrieve("annotation sentinel content", domain="d")
    import re
    # The draft page's <page> tag has draft="true"; the finalized one does not.
    draft_tag = re.search(r'<page[^>]*title="Draft annotated"[^>]*>', block)
    final_tag = re.search(r'<page[^>]*title="Final annotated"[^>]*>', block)
    assert draft_tag and 'draft="true"' in draft_tag.group(0)
    assert final_tag and 'draft="true"' not in final_tag.group(0)


def test_retrieve_empty_query(kb_root: Path):
    block, sections = retrieve("", domain="d")
    assert block == "" and sections == []


def test_retrieve_op_no_results(kb_root: Path):
    _page("x", "X", "## Y\n\ncontent.\n")
    search_index.refresh(rebuild=True)
    result = retrieve_op("nonexistent quantum chromodynamics", domain="d")
    assert not result.success
    assert "no results" in result.summary


def test_retrieve_op_success_logs_and_returns_data(kb_root: Path):
    _page("topic", "Topic page", "## Detail\n\nrelevant detail about widgets.\n")
    search_index.refresh(rebuild=True)
    result = retrieve_op("relevant widgets", domain="d", caller="test")
    assert result.success
    assert result.data["section_count"] >= 1
    assert result.data["sources"][0]["path"].startswith("wiki/concepts/")
    assert paths.log_path() in result.paths_touched


def test_retrieve_op_xml_escaping(kb_root: Path):
    # Title with special chars must not break the <page> attributes.
    _page("amp", "Tax & Form <1120>", "## Filing\n\nhow to file the form.\n")
    search_index.refresh(rebuild=True)
    block, _ = retrieve("file the form", domain="d")
    assert "&amp;" in block and "&lt;1120&gt;" in block


def test_mcp_wiki_retrieve_registered():
    from gateway import mcp_server
    assert hasattr(mcp_server, "wiki_retrieve")


def test_retrieve_multi_domain_balances_quota(kb_root: Path):
    # alpha dominates lexically (5 matching pages); beta has 2.
    for i in range(5):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token alpha-{i}.\n", domain="alpha")
    for i in range(2):
        _page(f"b{i}", f"Beta {i}", f"## S\n\nshared signal token beta-{i}.\n", domain="beta")
    search_index.refresh(rebuild=True)

    # Single global call collapses toward the dominant domain...
    _block_single, single = retrieve("shared signal token", k=4)
    assert {s.domain for s in single} == {"alpha"}, "precondition: global call collapses to alpha"

    # ...multi-domain quota merge must surface BOTH named domains.
    _block, sections = retrieve("shared signal token", domains=["alpha", "beta"], k=4)
    doms = {s.domain for s in sections}
    assert "alpha" in doms and "beta" in doms, f"expected both domains, got {doms}"


def test_retrieve_multi_domain_dedups_and_survives_budget(kb_root: Path):
    # One page tagged to BOTH domains.
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    both = {
        "type": "concept", "slug": "dual", "title": "Dual tagged",
        "domains": ["alpha", "beta"],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / "dual.md").write_text(fm.serialize(both, "## S\n\nshared signal token dual.\n"))
    # Plus several large single-domain pages so the budget truncates well below
    # the merged set (8 distinct pages; a budget that admits only ~3 sections).
    for i in range(4):
        _page(f"a{i}", f"Alpha {i}", "## S\n\nshared signal token " + ("alpha " * 300), domain="alpha")
    for i in range(4):
        _page(f"b{i}", f"Beta {i}", "## S\n\nshared signal token " + ("beta " * 300), domain="beta")
    search_index.refresh(rebuild=True)

    _block, sections = retrieve(
        "shared signal token", domains=["alpha", "beta"], k=8, budget_chars=6000,
    )
    paths_seen = [s.rel_path for s in sections]
    assert len(paths_seen) == len(set(paths_seen)), "no page should appear twice"
    assert len(sections) < 8, "budget should truncate the merged set"
    assert {s.domain for s in sections} >= {"alpha", "beta"}, "balance survives truncation"


def test_retrieve_op_accepts_domains(kb_root: Path):
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token a{i}.\n", domain="alpha")
    _page("b0", "Beta 0", "## S\n\nshared signal token b0.\n", domain="beta")
    search_index.refresh(rebuild=True)
    res = retrieve_op("shared signal token", domains=["alpha", "beta"], k=4)
    assert res.success
    assert res.data["section_count"] >= 2


def test_mcp_wiki_retrieve_accepts_domains(kb_root: Path):
    from gateway.mcp_server import wiki_retrieve
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token a{i}.\n", domain="alpha")
    _page("b0", "Beta 0", "## S\n\nshared signal token b0.\n", domain="beta")
    search_index.refresh(rebuild=True)
    res = wiki_retrieve("shared signal token", domains="alpha,beta", k=4)
    assert res["success"]
    # _serialize exposes the assembled block as `summary`; both named domains
    # must appear as <page domain="..."> attributes (balanced, not collapsed).
    assert 'domain="alpha"' in res["summary"]
    assert 'domain="beta"' in res["summary"]


# ---------------------------------------------------------------------------
# RRF fusion helper
# ---------------------------------------------------------------------------
from gateway.ops.retrieve import _rrf_fuse


def test_rrf_fuse_rewards_agreement_and_merges():
    lexical = ["a", "b", "c"]
    dense   = ["b", "d", "a"]
    fused = _rrf_fuse([lexical, dense], k_rrf=60)
    assert set(fused) == {"a", "b", "c", "d"}     # union, deduped
    assert fused[0] == "b"                          # appears high in BOTH lists → top
    assert fused.index("a") < fused.index("c")      # 'a' in both beats 'c' in one


def test_rrf_fuse_single_list_preserves_order():
    assert _rrf_fuse([["x", "y", "z"]]) == ["x", "y", "z"]


# ---------------------------------------------------------------------------
# B3: hybrid BM25+dense path
# ---------------------------------------------------------------------------
from gateway.ops import retrieve as retr


def test_hybrid_surfaces_paraphrase_miss(kb_root: Path, monkeypatch):
    # 'reward-deficit' page uses jargon; query is lay. BM25 alone misses it.
    _page("rewarddef", "Reward deficit", "## Body\n\nAnhedonia: blunted reward sensitivity and lost motivation.\n")
    _page("filler", "Filler page", "## Body\n\ngastric emptying vagal tax filing widget unrelated.\n")
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    # stub encoder is paraphrase-tolerant → dense pulls rewarddef for the lay query
    block, sections = retr.retrieve("losing pleasure and drive", domain="d", hybrid=True)
    assert any(s.slug == "rewarddef" for s in sections)


def test_hybrid_preserves_hole1_placeholder_gate(kb_root: Path):
    _page("stubby", "Stubby page", "## Summary\n\n_(needs population from legacy import)_\n", draft=True)
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    block, _ = retr.retrieve("needs population legacy import", domain="d", hybrid=True)
    assert "needs population from legacy import" not in block
