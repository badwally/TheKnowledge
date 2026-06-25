"""Top-level conftest: shared fixtures for tests/ (non-gateway subtree)."""

import os
from pathlib import Path

import pytest

from gateway import paths


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
