"""Tests for fragmentation lint check — Step 9.

Adversarial with named negative controls (standing build rule):
- 3 near-duplicate concept pages (high mutual entity-namespace similarity) → flagged
- 1 distinct concept page → NOT flagged (negative control)

The fragmentation check uses EmbeddingIndex.nn("entity", ...) with mutual distance ≤ band.
We upsert pages directly into the embedding index in the fixture.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.embedding_index import EmbeddingIndex
from gateway.lint import fragmentation


def _concept(kb_root: Path, slug: str, title: str, aliases: list[str] | None = None) -> None:
    """Create a concept page and upsert its identity into the embedding index."""
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": title,
        "aliases": aliases or [],
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    body = f"# {title}\n\nConcept page body for {title}.\n"
    (d / f"{slug}.md").write_text(fm.serialize(front, body))

    # Upsert into entity namespace of the embedding index.
    idx = EmbeddingIndex()
    rel = f"wiki/concepts/{slug}.md"
    identity_text = title
    if aliases:
        identity_text = title + " " + " ".join(aliases)
    idx.upsert("entity", rel, identity_text)


def test_fragmentation_flags_near_duplicate_cluster_not_distinct(kb_root: Path) -> None:
    """3 near-duplicate concept pages form a flagged cluster; 1 distinct page is not flagged."""
    # Three near-duplicate concepts with very similar identity text (high cosine similarity).
    # The lexical encoder uses char-trigrams: nearly-identical titles → distance < 0.30.
    _concept(kb_root, "insulin-resistance-1", "Insulin resistance",
             aliases=["insulin insensitivity"])
    _concept(kb_root, "insulin-resistance-2", "Insulin resistance disorder",
             aliases=["insulin insensitivity syndrome"])
    _concept(kb_root, "insulin-resistance-3", "Insulin insensitivity",
             aliases=["insulin resistance variant"])

    # Completely distinct concept — should NOT appear in any fragmentation cluster.
    _concept(kb_root, "quantum-chromodynamics", "Quantum chromodynamics",
             aliases=["QCD", "strong nuclear force"])

    findings = fragmentation.run()

    # The cluster of 3 near-duplicate insulin-resistance pages must be flagged.
    cluster_members: set[str] = set()
    for f in findings:
        assert f.check == "fragmentation"
        for member in f.metadata.get("members", []):
            cluster_members.add(member)

    # At least one finding covering the insulin cluster
    insulin_rels = {
        "wiki/concepts/insulin-resistance-1.md",
        "wiki/concepts/insulin-resistance-2.md",
        "wiki/concepts/insulin-resistance-3.md",
    }
    # At minimum, 2 of the 3 insulin pages should appear in cluster_members
    # (exact clustering depends on threshold; they are all very close)
    overlap = insulin_rels & cluster_members
    assert len(overlap) >= 2, (
        f"expected at least 2 of the 3 near-duplicate insulin pages to be "
        f"flagged in a fragmentation cluster; got cluster_members={cluster_members}"
    )

    # The distinct page must NOT appear in any cluster.
    distinct_rels = {"wiki/concepts/quantum-chromodynamics.md"}
    assert not (distinct_rels & cluster_members), (
        f"the distinct QCD concept page must not appear in any fragmentation cluster; "
        f"cluster_members={cluster_members}"
    )


def test_fragmentation_empty_index_no_findings(kb_root: Path) -> None:
    """Negative control: no pages in the embedding index → no findings."""
    findings = fragmentation.run()
    assert findings == [], (
        f"expected no findings when embedding index is empty; got: {findings}"
    )


def test_fragmentation_single_page_no_cluster(kb_root: Path) -> None:
    """Negative control: a single page cannot form a cluster of size >= 2."""
    _concept(kb_root, "solitary-concept", "Unique topic with no near duplicates")
    findings = fragmentation.run()
    assert findings == [], (
        f"a single page cannot form a cluster; got: {findings}"
    )


def test_fragmentation_finding_has_metadata_members(kb_root: Path) -> None:
    """Each finding must carry metadata['members'] with at least 2 rel-paths."""
    _concept(kb_root, "dup-a", "Semaglutide weight loss therapy",
             aliases=["GLP-1 agonist weight loss"])
    _concept(kb_root, "dup-b", "Semaglutide obesity treatment",
             aliases=["GLP-1 receptor weight loss"])
    findings = fragmentation.run()
    for f in findings:
        members = f.metadata.get("members", [])
        assert len(members) >= 2, (
            f"every fragmentation finding must have >= 2 members; got: {members}"
        )
