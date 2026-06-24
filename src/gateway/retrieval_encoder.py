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

    def __init__(self, model_id: str, dim: int):
        self.model_id = model_id
        self.dim = dim
        self.model_version = f"mlx:{model_id}:{dim}"
        self._model = None

    def _ensure(self):
        if self._model is None:
            from mlx_embeddings import load  # local dep, installed only where the model runs
            self._model = load(self.model_id)

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        import numpy as np
        self._ensure()
        raw = self._model.encode(list(texts))           # (n, native_dim)
        arr = np.asarray(raw, dtype="float32")[:, : self.dim]   # Matryoshka truncate
        norms = np.linalg.norm(arr, axis=1, keepdims=True)
        arr = arr / np.clip(norms, 1e-12, None)
        return arr.tolist()


def retrieval_encoder():
    """Factory: env WIKI_RETRIEVAL_ENCODER selects the encoder.
    'stub' (default) | 'mlx:<model_id>:<dim>'. Mock in tests via monkeypatch."""
    spec = os.environ.get("WIKI_RETRIEVAL_ENCODER", "stub")
    if spec == "stub":
        return StubRetrievalEncoder()
    if spec.startswith("mlx:"):
        _, model_id, dim = spec.split(":", 2)
        return MlxQwen3Encoder(model_id, int(dim))
    raise ValueError(f"unknown WIKI_RETRIEVAL_ENCODER: {spec!r}")
