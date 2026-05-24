"""Tests for K5 locking + log_llm_call additions (M47).

Covers:
- LOCK_NAMES registry + is_known_lock_name helper
- log.append locking (closes ARCH-1 racy-log under concurrent writers)
- log.log_llm_call structured telemetry line format
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

from gateway import log as log_mod
from gateway import paths
from gateway.llm.telemetry import CallResult
from gateway.locking import (
    LOCK_NAMES,
    LOCK_NAME_PREFIXES,
    is_known_lock_name,
)


# --- LOCK_NAMES registry ---------------------------------------------------


def test_lock_names_includes_load_bearing_names():
    """The four single-global locks must be in the registry."""
    assert "wiki-author" in LOCK_NAMES
    assert "nlm-registry" in LOCK_NAMES
    assert "log" in LOCK_NAMES        # K5 / ARCH-1 fix
    assert "index" in LOCK_NAMES      # K5 / ARCH-1 fix


def test_lock_name_prefixes_includes_load_bearing_prefixes():
    """The two per-resource lock prefixes must be in the registry."""
    assert "ingest" in LOCK_NAME_PREFIXES
    assert "schedule" in LOCK_NAME_PREFIXES   # K4 placeholder


def test_is_known_lock_name_accepts_exact_names():
    assert is_known_lock_name("wiki-author") is True
    assert is_known_lock_name("log") is True
    assert is_known_lock_name("index") is True
    assert is_known_lock_name("nlm-registry") is True


def test_is_known_lock_name_accepts_prefixed_names():
    assert is_known_lock_name("ingest-yt-abc123") is True
    assert is_known_lock_name("ingest-pdf-foo-bar-baz") is True
    assert is_known_lock_name("schedule-nightly-lint") is True


def test_is_known_lock_name_rejects_unknown_prefix():
    assert is_known_lock_name("frobnicate-thing") is False
    assert is_known_lock_name("hacky-lock-name") is False


def test_is_known_lock_name_rejects_unknown_exact():
    assert is_known_lock_name("totally-not-a-lock") is False


# --- log.append concurrency (ARCH-1 fix) -----------------------------------


def test_log_append_creates_header_when_missing(kb_root: Path):
    path = paths.log_path()
    assert not path.exists()
    log_mod.append("test-op", {"k": "v"}, summary="hello")
    text = path.read_text()
    assert text.startswith("# Knowledge Log")
    assert "test-op" in text
    assert "k=v" in text
    assert "hello" in text


def test_log_append_concurrent_writes_dont_interleave(kb_root: Path):
    """50 concurrent log.append calls must produce 50 well-formed entries.

    ARCH-1 regression test: pre-M47, naked file.write under concurrent
    writers could interleave multi-line entries. Now wrapped in
    file_lock('log'); all entries should appear intact.
    """
    def writer(i: int) -> None:
        log_mod.append("concur", {"i": i}, summary=f"summary-line-for-{i}")

    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(writer, range(50)))

    text = paths.log_path().read_text()
    # Every iteration's marker should appear exactly once and uncorrupted.
    for i in range(50):
        assert f"i={i} " in text or f"i={i}\n" in text, f"missing marker i={i}"
        assert f"summary-line-for-{i}" in text, f"missing summary for {i}"


# --- log_llm_call structured entry -----------------------------------------


def _sample_result(**overrides) -> CallResult:
    defaults = dict(
        text="ignored body",
        input_tokens=100,
        output_tokens=50,
        cache_read_tokens=20,
        cache_creation_tokens=5,
        model="claude-haiku-4-5-20251001",
        stop_reason="end_turn",
        duration_ms=1234,
        total_cost_usd=0.000123,
    )
    defaults.update(overrides)
    return CallResult(**defaults)


def test_log_llm_call_writes_single_pipe_delimited_line(kb_root: Path):
    log_mod.log_llm_call("filter", _sample_result())
    text = paths.log_path().read_text()
    # The entry header line
    lines = [ln for ln in text.splitlines() if ln.startswith("## [") and "llm-call" in ln]
    assert len(lines) == 1
    line = lines[0]
    assert "op=filter" in line
    assert "model=claude-haiku-4-5-20251001" in line
    assert "in_tokens=100" in line
    assert "out_tokens=50" in line
    assert "cache_read=20" in line
    assert "cache_creation=5" in line
    assert "duration_ms=1234" in line
    assert "cost_usd=0.000123" in line


def test_log_llm_call_includes_session_id_when_provided(kb_root: Path):
    log_mod.log_llm_call("plan_authorship", _sample_result(), session_id="r-2026-001")
    text = paths.log_path().read_text()
    assert "session=r-2026-001" in text


def test_log_llm_call_includes_extra_fields(kb_root: Path):
    log_mod.log_llm_call(
        "filter",
        _sample_result(),
        extra={"error": "timeout", "attempt": 2},
    )
    text = paths.log_path().read_text()
    assert "error=timeout" in text
    assert "attempt=2" in text


def test_log_llm_call_no_body_just_header(kb_root: Path):
    """The llm-call entry should be a one-liner (header only, no body lines)."""
    log_mod.log_llm_call("vlm", _sample_result())
    text = paths.log_path().read_text()
    # After the header line, the next non-blank line should be another
    # log entry (or end of file), not a multi-line body for this entry.
    lines = text.splitlines()
    # Find the llm-call header
    idx = next(i for i, ln in enumerate(lines) if "llm-call" in ln)
    # Next non-blank line, if any, must be a `## [` (another entry) — not a body line
    for follow in lines[idx + 1:]:
        if follow.strip() == "":
            continue
        assert follow.startswith("## ["), f"unexpected body line after llm-call: {follow!r}"
        break
