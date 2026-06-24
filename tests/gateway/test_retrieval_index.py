from pathlib import Path
import pytest
from gateway import paths, search_index, frontmatter as fm
from gateway.retrieval_index import retrieval_index, dense_section_hits


def _page(slug, body, draft=False):
    d = paths.wiki_dir() / "concepts"; d.mkdir(parents=True, exist_ok=True)
    front = {"type": "concept", "slug": slug, "title": slug, "domains": ["d"],
             "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z"}
    if draft: front["draft"] = True
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def test_retrieval_index_uses_separate_db(kb_root: Path):
    idx = retrieval_index()
    assert idx._db_path == paths.retrieval_embedding_db_path()
    assert idx._db_path != paths.embedding_db_path()    # NOT the lexical index db


def test_dense_section_hits_finds_paraphrase_match(kb_root: Path):
    _page("vagal", "## Mechanism\n\nThe drug slows stomach emptying via the vagus nerve.\n")
    _page("noise", "## Other\n\nUnrelated content about quarterly tax filing.\n")
    retrieval_index().rebuild_from_canonical()
    hits = dense_section_hits("delays gastric emptying through vagal signaling", k=5)
    assert hits, "expected dense neighbors"
    assert any(rel.endswith("vagal.md") for rel, _heading, _dist in hits)
    assert all(isinstance(d, float) for _r, _h, d in hits)


def test_hits_for_sections_populates_page_metadata(kb_root: Path):
    _page("alpha", "## Mechanism\n\nbody about alpha topic.\n")
    search_index.refresh(rebuild=True)
    rel = "wiki/concepts/alpha.md"
    hits = search_index.hits_for_sections([(rel, "Mechanism"), (rel, "Nonexistent")])
    assert (rel, "Mechanism") in hits
    h = hits[(rel, "Mechanism")]
    assert h.slug == "alpha" and h.title == "alpha" and h.page_type == "concept"
    assert (rel, "Nonexistent") not in hits          # missing section omitted
