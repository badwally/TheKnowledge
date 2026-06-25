import os
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from gateway import paths, search_index, frontmatter as fm
from gateway import retrieval_index as ri
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


def test_dense_hits_use_embed_query_when_encoder_is_asymmetric(kb_root: Path, monkeypatch):
    """The query must go through embed_query (instruction-prefixed), never the raw
    document embed(), when the encoder exposes the asymmetric seam (Qwen3)."""
    _page("vagal", "## Mechanism\n\nThe drug slows gastric emptying via the vagus nerve.\n")
    ri._VEC_CACHE.clear()
    real = retrieval_index()
    real.rebuild_from_canonical()                    # populate the db with the stub at its dim
    dim = real._encoder.dim
    calls = {"embed": 0, "embed_query": 0}

    class _Asymmetric:
        def embed(self, texts):                       # the document path
            calls["embed"] += 1
            raise AssertionError("query must use embed_query, not embed")

        def embed_query(self, texts):                 # the query path
            calls["embed_query"] += 1
            v = np.ones(dim, dtype=np.float32)
            v /= np.linalg.norm(v)
            return [v.tolist() for _ in texts]

    fake_idx = SimpleNamespace(_db_path=real._db_path, _encoder=_Asymmetric())
    monkeypatch.setattr(ri, "retrieval_index", lambda: fake_idx)
    hits = dense_section_hits("delays gastric emptying", k=3)
    assert calls["embed_query"] == 1 and calls["embed"] == 0
    assert hits                                       # still returns neighbors


def test_section_vector_cache_keyed_on_db_mtime(kb_root: Path):
    """The in-memory vector cache (the 590ms latency fix) returns the SAME matrix
    object on an unchanged db, and re-reads only when the db mtime advances."""
    _page("vagal", "## Mechanism\n\ngastric emptying via the vagus nerve.\n")
    ri._VEC_CACHE.clear()
    idx = retrieval_index()
    idx.rebuild_from_canonical()
    idx2 = retrieval_index()
    _k1, m1 = ri._cached_section_vectors(idx2)
    _k2, m2 = ri._cached_section_vectors(idx2)
    assert m2 is m1                                   # cache hit: no per-query sqlite re-read
    future = time.time() + 10
    os.utime(idx2._db_path, (future, future))         # advance mtime
    _k3, m3 = ri._cached_section_vectors(idx2)
    assert m3 is not m1                               # mtime change invalidates -> re-read
