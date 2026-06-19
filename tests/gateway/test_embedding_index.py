"""Librarian Phase 2 (T1/T2) — embedding index: store, pluggable encoder,
lexical fallback, three namespaces, per-namespace thresholds.

The embedding index adds ALONGSIDE the FTS index (`search_index.py`) with the
same derived / gitignored / rebuildable discipline. The active encoder is the
I2 lexical fallback (`lexical-fallback-v1`) — pure numpy, no heavy ML deps.
"""

from __future__ import annotations

import math

import pytest

from gateway import paths


@pytest.fixture
def root(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    (tmp_path / "wiki").mkdir()
    return tmp_path


# --- Task 1: paths -------------------------------------------------------


def test_paths_embedding_db_path(root):
    p = paths.embedding_db_path()
    assert p == paths.index_dir() / "embeddings.db"
    # Lives under the gitignored .index/ tree (derived state).
    assert ".index" in p.parts


def test_paths_embedding_shadow_db_path(root):
    p = paths.embedding_shadow_db_path()
    assert p == paths.index_dir() / "embeddings.shadow.db"
    assert p != paths.embedding_db_path()


# --- Task 1: lexical fallback encoder ------------------------------------


def _dist(a, b):
    # cosine distance for unit vectors
    return 1.0 - sum(x * y for x, y in zip(a, b))


def test_lexical_encoder_deterministic(root):
    from gateway.embedding_index import LexicalFallbackEncoder

    enc = LexicalFallbackEncoder()
    assert enc.model_version == "lexical-fallback-v1"
    assert enc.dim == 256

    v1 = enc.embed(["GLP-1 receptor agonist"])[0]
    v2 = enc.embed(["GLP-1 receptor agonist"])[0]
    assert v1 == v2  # deterministic, byte-stable

    # unit norm
    assert math.isclose(math.sqrt(sum(x * x for x in v1)), 1.0, abs_tol=1e-6)
    assert len(v1) == 256

    # paraphrase closer than an unrelated string (negative control)
    para = enc.embed(["GLP-1 receptor agonists"])[0]
    unrel = enc.embed(["federal reserve monetary policy"])[0]
    assert _dist(v1, para) < _dist(v1, unrel)


def test_lexical_encoder_distinct_texts_differ(root):
    from gateway.embedding_index import LexicalFallbackEncoder

    enc = LexicalFallbackEncoder()
    a, b = enc.embed(["order block price action", "anhedonia reward deficit"])
    assert a != b
    assert _dist(a, b) > 0.0


# --- Task 1: store upsert + nn per namespace -----------------------------


def test_upsert_and_nn_per_namespace(root):
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    for ns in ("entity", "section", "question"):
        idx.upsert(ns, f"{ns}-a", "GLP-1 receptor agonist semaglutide")
        idx.upsert(ns, f"{ns}-b", "federal reserve interest rate policy")
        idx.upsert(ns, f"{ns}-c", "order block institutional price action")

        hits = idx.nn(ns, "GLP-1 receptor agonists", k=3)
        assert hits, ns
        assert hits[0].key == f"{ns}-a", (ns, [(h.key, h.distance) for h in hits])
        # ascending distance
        dists = [h.distance for h in hits]
        assert dists == sorted(dists)
        # negative control: the unrelated key is not rank 0
        assert hits[0].key != f"{ns}-b"


def test_nn_empty_namespace_returns_empty(root):
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    idx.upsert("entity", "e1", "something")
    assert idx.nn("question", "anything", k=5) == []


def test_upsert_is_idempotent_overwrite(root):
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    idx.upsert("entity", "e1", "first text")
    idx.upsert("entity", "e1", "second different text")
    # one row, latest text
    hits = idx.nn("entity", "second different text", k=5)
    assert len([h for h in hits if h.key == "e1"]) == 1
    assert hits[0].key == "e1"


def test_model_version_recorded(root):
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    idx.upsert("entity", "e1", "x")
    assert idx.model_version() == "lexical-fallback-v1"


def test_self_heal_after_store_deleted(root):
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    idx.upsert("entity", "e1", "GLP-1 semaglutide")
    paths.embedding_db_path().unlink()  # nuke the derived store

    # A fresh index re-creates the store on first write; reading before write
    # returns empty (derived, never canonical).
    idx2 = EmbeddingIndex()
    assert idx2.nn("entity", "GLP-1", k=5) == []
    idx2.upsert("entity", "e1", "GLP-1 semaglutide")
    assert idx2.nn("entity", "GLP-1 semaglutide", k=5)[0].key == "e1"


# --- Task 2: namespace routing + per-namespace thresholds ----------------


def test_upsert_page_routes_entity_and_section(root):
    from gateway import frontmatter as fm
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    page = (
        "---\n"
        "type: entity\n"
        "title: Semaglutide\n"
        "aliases: [Ozempic, Wegovy]\n"
        "---\n"
        "# Overview\n"
        "A GLP-1 receptor agonist.\n\n"
        "# Dosing\n"
        "Titration schedule.\n"
    )
    front, _ = fm.parse(page)
    idx.upsert_page("wiki/entities/semaglutide.md", page, front)

    # entity row keyed by rel_path
    ent = idx.nn("entity", "Semaglutide Ozempic", k=5)
    assert any(h.key == "wiki/entities/semaglutide.md" for h in ent)

    # section rows keyed by rel_path#heading
    sec = idx.nn("section", "titration dosing schedule", k=5)
    assert any(h.key.startswith("wiki/entities/semaglutide.md#") for h in sec)

    # no question row created from a page
    assert idx.nn("question", "anything at all", k=5) == []


def test_upsert_page_source_type_has_no_entity_row(root):
    from gateway import frontmatter as fm
    from gateway.embedding_index import EmbeddingIndex

    idx = EmbeddingIndex()
    page = (
        "---\n"
        "type: source\n"
        "title: Some Paper\n"
        "---\n"
        "# Summary\n"
        "Findings about GLP-1.\n"
    )
    front, _ = fm.parse(page)
    idx.upsert_page("wiki/sources/paper.md", page, front)

    # section rows present, no entity row (negative control)
    assert idx.nn("section", "findings GLP-1", k=5)
    assert idx.nn("entity", "Some Paper", k=5) == []


def test_thresholds_per_namespace_distinct(root):
    from gateway.embedding_index import thresholds

    t = thresholds()
    assert set(t) == {"section", "entity", "question"}
    # entity (co-reference identity) is the strictest operating point
    assert t["entity"] < t["section"] < t["question"]
    # negative control: they are not all equal (three operating points, not one)
    assert len(set(t.values())) == 3
