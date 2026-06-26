"""Top-level conftest: shared fixtures for tests/ (non-gateway subtree)."""

import os
from pathlib import Path

import pytest

from gateway import paths


@pytest.fixture(autouse=True)
def _force_stub_retrieval_encoder(monkeypatch: pytest.MonkeyPatch) -> None:
    """Insulate the whole suite from the checked-in `.knowledge/retrieval.yaml`
    (4B) production default: every test runs on the deterministic CI stub encoder
    unless it explicitly overrides. The env var beats the config file in
    `_resolve_encoder_spec`, so this is a no-op for behavior today but guarantees
    no test loads the neural model (absent in CI). A test exercising the config
    loader undoes this with `monkeypatch.delenv` in its own body."""
    monkeypatch.setenv("WIKI_RETRIEVAL_ENCODER", "stub")


@pytest.fixture
def kb_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Override KNOWLEDGE_ROOT to a temp directory for the duration of the test."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    for sub in (
        "raw",
        "raw/inbox",
        "raw/inbox/_failed",
        "wiki",
        "wiki/sources",
        "nlm",
        ".knowledge",
        ".knowledge/locks",
    ):
        (tmp_path / sub).mkdir(parents=True, exist_ok=True)
    for src_type in paths.SOURCE_TYPES:
        (tmp_path / "raw" / src_type).mkdir(parents=True, exist_ok=True)
    return tmp_path
