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


def dense_section_hits(query: str, k: int) -> list[tuple[str, str, float]]:
    """Top-k (rel_path, heading, distance) section neighbors of `query`."""
    out: list[tuple[str, str, float]] = []
    for hit in retrieval_index().nn("section", query, k=k):
        rel, _, heading = hit.key.partition("#")
        out.append((rel, heading, hit.distance))
    return out
