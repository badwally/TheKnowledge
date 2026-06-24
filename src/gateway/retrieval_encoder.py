"""Encoders for the dense RETRIEVE path (Hole 2). Separate from the lexical
EmbeddingIndex encoder so dedup/demand/merge-map gates stay on lexical-fallback-v1.

CI uses StubRetrievalEncoder (deterministic, no model download). Production uses a
local neural encoder (MLX/GGUF) selected by WIKI_RETRIEVAL_ENCODER.
"""
from __future__ import annotations

import os
from typing import Sequence

from gateway.embedding_index import LexicalFallbackEncoder


class StubRetrievalEncoder(LexicalFallbackEncoder):
    """Deterministic stand-in for the neural encoder in tests. Reuses the lexical
    hashing (paraphrase-tolerant, L2-normalized) at a configurable dim."""

    def __init__(self, dim: int = 256, model_version: str = "stub-retrieval-v1"):
        self.dim = dim
        self.model_version = model_version


class MlxQwen3Encoder:
    """Local MLX Qwen3-Embedding encoder. Lazy-loads weights on first embed().
    Never instantiated in CI (no model download)."""

    def __init__(self, model_id: str, dim: int, max_length: int = 1024):
        self.model_id = model_id
        self.dim = dim
        self.max_length = max_length
        self.model_version = f"mlx:{model_id}:{dim}"
        self._model = None
        self._tok = None

    def _ensure(self):
        if self._model is None:
            from mlx_embeddings import load  # local dep, installed only where the model runs
            self._model, self._tok = load(self.model_id)

    # Qwen3-Embedding retrieval expects an instruction-prefixed QUERY and a raw
    # DOCUMENT (asymmetric). Documents go through embed(); queries through
    # embed_query() so the index stores raw passages and only the query carries
    # the instruction.
    QUERY_INSTRUCTION = (
        "Instruct: Given a search query, retrieve relevant wiki passages that "
        "answer it\nQuery: "
    )

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        import numpy as np
        from mlx_embeddings import generate
        self._ensure()
        out = generate(self._model, self._tok, list(texts), max_length=self.max_length)
        # mlx-embeddings returns a BaseModelOutput; .text_embeds is the pooled (n, native_dim) matrix.
        arr = np.array(out.text_embeds, dtype=np.float32)[:, : self.dim]   # Matryoshka truncate
        norms = np.linalg.norm(arr, axis=1, keepdims=True)
        arr = arr / np.clip(norms, 1e-12, None)
        return arr.tolist()

    def embed_query(self, texts: Sequence[str]) -> list[list[float]]:
        return self.embed([f"{self.QUERY_INSTRUCTION}{t}" for t in texts])


_ENCODER_CACHE: dict = {}  # spec -> Encoder (memoized so the neural model loads ONCE)


def _build_encoder(spec: str):
    if spec == "stub":
        return StubRetrievalEncoder()
    if spec.startswith("mlx:"):
        _, model_id, dim = spec.split(":", 2)
        return MlxQwen3Encoder(model_id, int(dim))
    raise ValueError(f"unknown WIKI_RETRIEVAL_ENCODER: {spec!r}")


def retrieval_encoder():
    """Factory: env WIKI_RETRIEVAL_ENCODER selects the encoder.
    'stub' (default) | 'mlx:<model_id>:<dim>'. Memoized per spec so the neural
    model is loaded once per process, not rebuilt (and reloaded) every query."""
    spec = os.environ.get("WIKI_RETRIEVAL_ENCODER", "stub")
    enc = _ENCODER_CACHE.get(spec)
    if enc is None:
        enc = _ENCODER_CACHE[spec] = _build_encoder(spec)
    return enc
