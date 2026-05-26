"""AGT-6: briefing_cron — per-domain nlm-briefing with corpus-hash skip."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult
from gateway.ops.briefing_cron import (
    _blessed_domains,
    _corpus_hash,
    _load_stored_hash,
    _store_hash,
    run_briefing_cron,
)


# --- helpers ----------------------------------------------------------------


def _make_policy(kb_root: Path, domain: str) -> None:
    p = paths.policies_dir() / domain / "policy.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"domain:\n  slug: {domain}\n")


def _make_raw_source(kb_root: Path, source_id: str, domain: str) -> None:
    p = paths.raw_dir() / "web" / f"{source_id}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "type": "web",
        "title": f"Source {source_id}",
        "url": "https://example.com",
        "authors": [],
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
        "domains": [domain],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    p.write_text(fm.serialize(front, "Body.\n"))


# --- unit tests -------------------------------------------------------------


def test_blessed_domains_empty_no_policies(kb_root: Path) -> None:
    assert _blessed_domains() == []


def test_blessed_domains_lists_policy_dirs(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_policy(kb_root, "beta")
    assert _blessed_domains() == ["alpha", "beta"]


def test_hash_roundtrip(kb_root: Path) -> None:
    _store_hash("alpha", "abc123")
    assert _load_stored_hash("alpha") == "abc123"


def test_load_stored_hash_missing(kb_root: Path) -> None:
    assert _load_stored_hash("nonexistent") is None


def test_corpus_hash_deterministic(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-aaa", "alpha")
    h1 = _corpus_hash("alpha")
    h2 = _corpus_hash("alpha")
    assert h1 == h2
    assert len(h1) == 16


def test_corpus_hash_excludes_other_domains(kb_root: Path) -> None:
    _make_raw_source(kb_root, "web-aaa", "alpha")
    _make_raw_source(kb_root, "web-bbb", "beta")
    h_alpha = _corpus_hash("alpha")
    h_beta = _corpus_hash("beta")
    assert h_alpha != h_beta


def test_run_no_domains(kb_root: Path) -> None:
    result = run_briefing_cron()
    assert result.success
    assert "no blessed domains" in result.summary


def test_run_skips_when_hash_unchanged(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_raw_source(kb_root, "web-aaa", "alpha")
    current = _corpus_hash("alpha")
    _store_hash("alpha", current)

    called = []
    with patch("gateway.ops.nlm.nlm_briefing") as mock_brief:
        mock_brief.side_effect = lambda d: called.append(d) or OperationResult(success=True)
        result = run_briefing_cron()

    assert result.success
    assert called == []
    assert "0 ran" in result.summary
    assert "1 skipped" in result.summary


def test_run_calls_briefing_when_hash_changed(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_raw_source(kb_root, "web-aaa", "alpha")

    called: list[str] = []

    def _fake_briefing(domain: str) -> OperationResult:
        called.append(domain)
        return OperationResult(success=True, summary="ok")

    with patch("gateway.ops.nlm.nlm_briefing", _fake_briefing):
        result = run_briefing_cron()

    assert result.success
    assert "alpha" in called
    assert "1 ran" in result.summary


def test_run_stores_hash_after_success(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_raw_source(kb_root, "web-aaa", "alpha")
    expected_hash = _corpus_hash("alpha")

    with patch("gateway.ops.nlm.nlm_briefing", return_value=OperationResult(success=True)):
        run_briefing_cron()

    assert _load_stored_hash("alpha") == expected_hash


def test_run_records_error_on_nlm_failure(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_raw_source(kb_root, "web-aaa", "alpha")

    with patch(
        "gateway.ops.nlm.nlm_briefing",
        return_value=OperationResult(success=False, errors=["NLM timeout"]),
    ):
        result = run_briefing_cron()

    assert not result.success
    assert any("NLM timeout" in e for e in result.errors)


def test_briefing_cron_never_calls_audio_or_slides(kb_root: Path) -> None:
    """Structural guard: briefing_cron module must not import nlm_audio or nlm_slides."""
    import inspect
    from gateway.ops import briefing_cron as mod

    src = inspect.getsource(mod)
    assert "nlm_audio" not in src, "briefing_cron must not call nlm_audio"
    assert "nlm_slides" not in src, "briefing_cron must not call nlm_slides"
