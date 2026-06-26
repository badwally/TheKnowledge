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
        # Quantized builds (4B/8B *-DWQ) emit bfloat16, whose PEP-3118 buffer numpy can't read
        # directly; .tolist() materializes to Python floats first (also avoids importing mlx.core,
        # keeping the stub/fake test path CI-safe). float32 builds (0.6B-8bit) skip the round-trip.
        te = out.text_embeds
        if not isinstance(te, np.ndarray):
            te = te.tolist()
        arr = np.asarray(te, dtype=np.float32)[:, : self.dim]   # Matryoshka truncate
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


def _resolve_encoder_spec() -> str:
    """Encoder spec precedence: WIKI_RETRIEVAL_ENCODER env > the checked-in
    `.knowledge/retrieval.yaml` (`encoder:` key) > 'stub'.

    The env var wins so CI/tests (and ad-hoc overrides) force the stub; the
    config file is the durable production default, so the neural encoder
    activates without a per-shell export. Absent/unparseable config → 'stub'.
    The dense index MUST be built under the resolved spec — a dim mismatch is
    caught and degraded to lexical-only in `dense_section_hits`.
    """
    env = os.environ.get("WIKI_RETRIEVAL_ENCODER")
    if env:
        return env
    from gateway import paths
    cfg = paths.knowledge_internal() / "retrieval.yaml"
    if cfg.exists():
        try:
            import yaml
            data = yaml.safe_load(cfg.read_text()) or {}
            spec = data.get("encoder")
            if spec:
                return str(spec)
        except Exception:
            pass  # malformed config never breaks retrieval — fall through to stub
    return "stub"


def retrieval_encoder():
    """Factory: `_resolve_encoder_spec()` selects the encoder.
    'stub' | 'mlx:<model_id>:<dim>'. Memoized per spec so the neural model is
    loaded once per process, not rebuilt (and reloaded) every query."""
    spec = _resolve_encoder_spec()
    enc = _ENCODER_CACHE.get(spec)
    if enc is None:
        enc = _ENCODER_CACHE[spec] = _build_encoder(spec)
    return enc
