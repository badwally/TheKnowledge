"""Phase 1 T1.2 — OperationResult async fields + _serialize extension (A5).

Commit is asynchronous, so a deposit call returns an acceptance receipt rather
than paths-touched. The receipt shape extends OperationResult with optional
intent_id / disposition / retry_after / canonical_path (default None); existing
consumers tolerate their absence because _serialize reads a fixed field set.
"""

from __future__ import annotations

from pathlib import Path

from gateway.core import OperationResult
from gateway.mcp_server import _serialize


def test_operation_result_new_fields_default_none():
    r = OperationResult(success=True)
    assert r.intent_id is None
    assert r.disposition is None
    assert r.retry_after is None
    assert r.canonical_path is None


def test_serialize_includes_legacy_keys_for_plain_result():
    r = OperationResult(success=True, summary="ok")
    out = _serialize(r)
    for key in ("success", "no_op", "summary", "paths_touched", "errors", "warnings"):
        assert key in out
    # New keys present but None for a legacy/plain result.
    assert out["intent_id"] is None
    assert out["disposition"] is None
    assert out["retry_after"] is None
    assert out["canonical_path"] is None


def test_serialize_surfaces_new_fields_when_set():
    r = OperationResult(
        success=True,
        intent_id="abc123",
        disposition="queued",
        retry_after=30,
        canonical_path=Path("wiki/sources/x.md"),
    )
    out = _serialize(r)
    assert out["intent_id"] == "abc123"
    assert out["disposition"] == "queued"
    assert out["retry_after"] == 30
    assert out["canonical_path"] == "wiki/sources/x.md"
