import sys
import types

import numpy as np
import pytest
from gateway.embedding_index import Encoder
from gateway import retrieval_encoder as re
from gateway.retrieval_encoder import (
    MlxQwen3Encoder,
    StubRetrievalEncoder,
    _build_encoder,
    retrieval_encoder,
)


def _install_fake_mlx(monkeypatch, recorder, native_dim=8):
    """Install a fake `mlx_embeddings` so MlxQwen3Encoder exercises its real
    logic (truncate/normalize/instruction/lazy-load) without downloading weights.
    Records `load` calls and the texts handed to `generate` so the query
    instruction and document-asymmetry can be asserted."""
    mod = types.ModuleType("mlx_embeddings")

    def load(model_id):
        recorder["loads"] = recorder.get("loads", 0) + 1
        recorder["model_id"] = model_id
        return ("FAKE_MODEL", "FAKE_TOK")

    def generate(model, tok, texts, max_length=1024):
        recorder.setdefault("texts", []).extend(texts)
        recorder["max_length"] = max_length
        rows = [[float(len(t) % 7 + 1) + i for i in range(native_dim)] for t in texts]
        return types.SimpleNamespace(text_embeds=np.asarray(rows, dtype=np.float32))

    mod.load = load
    mod.generate = generate
    monkeypatch.setitem(sys.modules, "mlx_embeddings", mod)
    return recorder


def test_stub_encoder_satisfies_protocol_and_is_deterministic():
    enc = StubRetrievalEncoder(dim=256)
    assert isinstance(enc, Encoder)            # runtime_checkable Protocol
    assert enc.dim == 256 and enc.model_version
    v1 = enc.embed(["hello world"])[0]
    v2 = enc.embed(["hello world"])[0]
    assert v1 == v2                            # deterministic
    assert len(v1) == 256
    assert abs(float(np.linalg.norm(v1)) - 1.0) < 1e-5   # L2-normalized


def test_stub_encoder_paraphrase_closer_than_unrelated():
    enc = StubRetrievalEncoder(dim=256)
    import numpy as np
    a, b, c = (np.asarray(enc.embed([t])[0]) for t in
               ["central bank selling bonds", "central bank sells bonds", "banana bread recipe"])
    assert float(a @ b) > float(a @ c)         # paraphrase nearer than unrelated


# --- WIP encoder productionization: spec parse / asymmetry / cache / memo ---

def test_build_encoder_parses_mlx_spec():
    enc = _build_encoder("mlx:mlx-community/Qwen3-Embedding-4B-4bit-DWQ:2560")
    assert isinstance(enc, MlxQwen3Encoder)
    assert enc.model_id == "mlx-community/Qwen3-Embedding-4B-4bit-DWQ"   # model id keeps its slash
    assert enc.dim == 2560                                              # native 4B dim, no truncation
    assert enc.model_version == "mlx:mlx-community/Qwen3-Embedding-4B-4bit-DWQ:2560"


def test_build_encoder_stub_and_rejects_unknown():
    assert isinstance(_build_encoder("stub"), StubRetrievalEncoder)
    with pytest.raises(ValueError):
        _build_encoder("voyage:hosted-model")


def test_mlx_embed_truncates_to_dim_and_l2_normalizes(monkeypatch):
    _install_fake_mlx(monkeypatch, {}, native_dim=8)
    enc = MlxQwen3Encoder("fake/model", dim=4)
    v = enc.embed(["hello"])[0]
    assert len(v) == 4                                       # Matryoshka truncate 8 -> 4
    assert abs(float(np.linalg.norm(v)) - 1.0) < 1e-6        # L2-normalized after truncation


def test_embed_query_applies_instruction_prefix(monkeypatch):
    rec = _install_fake_mlx(monkeypatch, {}, native_dim=8)
    enc = MlxQwen3Encoder("fake/model", dim=4)
    enc.embed_query(["what is active vs passive QT"])
    assert rec["texts"] == [MlxQwen3Encoder.QUERY_INSTRUCTION + "what is active vs passive QT"]
    assert MlxQwen3Encoder.QUERY_INSTRUCTION.startswith("Instruct:")   # Qwen3 asymmetric format
    assert "\nQuery: " in MlxQwen3Encoder.QUERY_INSTRUCTION


def test_embed_leaves_documents_raw(monkeypatch):
    rec = _install_fake_mlx(monkeypatch, {}, native_dim=8)
    enc = MlxQwen3Encoder("fake/model", dim=4)
    enc.embed(["raw passage"])
    assert rec["texts"] == ["raw passage"]                   # documents carry no instruction


def test_embed_handles_non_ndarray_mlx_output(monkeypatch):
    """Quantized 4B/8B builds emit a bfloat16 mlx array whose buffer numpy can't
    read directly; embed() must route any non-ndarray output through .tolist()."""
    class _MlxArray:                      # duck-typed mlx array: NOT an np.ndarray
        def __init__(self, rows):
            self._rows = rows
        def tolist(self):
            return self._rows

    mod = types.ModuleType("mlx_embeddings")
    mod.load = lambda model_id: ("M", "T")
    mod.generate = lambda m, t, texts, max_length=1024: types.SimpleNamespace(
        text_embeds=_MlxArray([[1.0, 2.0, 3.0, 4.0] for _ in texts]))
    monkeypatch.setitem(sys.modules, "mlx_embeddings", mod)
    enc = MlxQwen3Encoder("fake/model", dim=2)
    v = enc.embed(["x"])[0]
    assert len(v) == 2                                       # truncated from 4 -> 2
    assert abs(float(np.linalg.norm(v)) - 1.0) < 1e-6        # normalized despite non-ndarray input


def test_embed_passes_max_length(monkeypatch):
    rec = _install_fake_mlx(monkeypatch, {})
    enc = MlxQwen3Encoder("fake/model", dim=4, max_length=512)
    enc.embed(["x"])
    assert rec["max_length"] == 512


def test_model_loads_lazily_and_exactly_once(monkeypatch):
    rec = _install_fake_mlx(monkeypatch, {})
    enc = MlxQwen3Encoder("fake/model", dim=4)
    assert rec.get("loads", 0) == 0          # lazy: construction does not load weights
    enc.embed(["a"])
    enc.embed(["b"])
    enc.embed_query(["c"])
    assert rec["loads"] == 1                  # loaded once, reused across calls


def test_retrieval_encoder_memoized_per_spec(monkeypatch):
    monkeypatch.setattr(re, "_ENCODER_CACHE", {})
    monkeypatch.setenv("WIKI_RETRIEVAL_ENCODER", "stub")
    assert retrieval_encoder() is retrieval_encoder()         # same instance: model loads once


def test_stub_has_no_embed_query_so_dense_path_falls_back():
    # dense_section_hits selects getattr(enc, "embed_query", enc.embed); the stub
    # must NOT expose embed_query so the lexical stub stays symmetric.
    assert not hasattr(StubRetrievalEncoder(), "embed_query")
