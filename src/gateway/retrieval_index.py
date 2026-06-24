"""Dense neural section retriever for the RETRIEVE path (Hole 2).

A second EmbeddingIndex instance bound to the neural encoder and a SEPARATE db
(retrieval_embedding_db_path). The existing lexical EmbeddingIndex — and the
entity/question/section namespaces it serves for dedup/demand/lint — is untouched.
"""
from __future__ import annotations

from gateway import paths
from gateway.embedding_index import EmbeddingIndex
from gateway.retrieval_encoder import retrieval_encoder


def retrieval_index() -> EmbeddingIndex:
    return EmbeddingIndex(encoder=retrieval_encoder(),
                          db_path=paths.retrieval_embedding_db_path())


_VEC_CACHE: dict = {}  # db_path -> (mtime, keys, matrix)


def _cached_section_vectors(idx):
    """Load the section-namespace vectors ONCE per (db, mtime) — brute-force NN
    must not re-read all vectors from sqlite per query (that was the ~590ms cost)."""
    import sqlite3
    import numpy as np
    p = idx._db_path
    if not p.exists():
        return [], None
    mt = p.stat().st_mtime
    cached = _VEC_CACHE.get(p)
    if cached and cached[0] == mt:
        return cached[1], cached[2]
    conn = sqlite3.connect(p)
    try:
        rows = conn.execute(
            "SELECT key, vec FROM vectors WHERE namespace='section'"
        ).fetchall()
    finally:
        conn.close()
    keys = [r[0] for r in rows]
    mat = (np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
           if rows else None)
    _VEC_CACHE[p] = (mt, keys, mat)
    return keys, mat


def dense_section_hits(query: str, k: int) -> list[tuple[str, str, float]]:
    """Top-k (rel_path, heading, distance) section neighbors of `query`.

    Uses the encoder's `embed_query` (instruction-prefixed) when available so the
    query is asymmetric to the raw stored documents, and an in-memory vector cache
    so NN is a single matmul, not a per-query sqlite scan.
    """
    import numpy as np
    idx = retrieval_index()
    keys, mat = _cached_section_vectors(idx)
    if mat is None:
        return []
    enc = idx._encoder
    embed_q = getattr(enc, "embed_query", enc.embed)   # stub has no embed_query
    qv = np.asarray(embed_q([query])[0], dtype=np.float32)
    dists = 1.0 - (mat @ qv)
    order = np.argsort(dists)[:k]
    out: list[tuple[str, str, float]] = []
    for i in order:
        rel, _, heading = keys[i].partition("#")
        out.append((rel, heading, float(dists[i])))
    return out
