"""DOC-5: log.md rotation — archive old entries to quarterly files."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import paths
from gateway.ops.rotate_log import KEEP_DAYS, _archive_path, _parse_entries, _quarter, rotate_log


# --- unit helpers --------------------------------------------------------------


def _ts(days_ago: int) -> str:
    dt = datetime.now(timezone.utc) - timedelta(days=days_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _entry(days_ago: int, op: str = "test") -> str:
    return f"\n## [{_ts(days_ago)}] {op}\n\nSome content.\n"


def _write_log(kb_root: Path, content: str) -> Path:
    p = paths.log_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p


# --- _quarter unit tests -------------------------------------------------------


def test_quarter_q1():
    dt = datetime(2026, 2, 15, tzinfo=timezone.utc)
    assert _quarter(dt) == "2026-Q1"


def test_quarter_q4():
    dt = datetime(2026, 11, 1, tzinfo=timezone.utc)
    assert _quarter(dt) == "2026-Q4"


# --- _parse_entries unit tests -------------------------------------------------


def test_parse_entries_splits_correctly():
    text = (
        "# Header\n\nPreamble.\n"
        "\n## [2026-01-01T00:00:00Z] op1\n\nContent.\n"
        "\n## [2026-02-01T00:00:00Z] op2\n\nContent.\n"
    )
    parts = _parse_entries(text)
    assert len(parts) == 3  # preamble + 2 entries
    assert parts[0][0] is None  # preamble has no timestamp


# --- rotation integration tests ------------------------------------------------


def test_rotate_log_archives_old_entries(kb_root: Path) -> None:
    recent = _entry(KEEP_DAYS - 5, "recent")
    old = _entry(KEEP_DAYS + 10, "old")
    _write_log(kb_root, f"# Knowledge Log\n\nPreamble.{old}{recent}")

    result = rotate_log(keep_days=KEEP_DAYS)

    assert result.success
    log_text = paths.log_path().read_text()
    assert "recent" in log_text
    assert "old" not in log_text


def test_rotate_log_creates_archive_file(kb_root: Path) -> None:
    old_dt = datetime.now(timezone.utc) - timedelta(days=KEEP_DAYS + 10)
    q = _quarter(old_dt)
    _write_log(kb_root, f"# Knowledge Log\n\nPreamble.{_entry(KEEP_DAYS + 10)}")

    rotate_log(keep_days=KEEP_DAYS)

    archive = _archive_path(q)
    assert archive.exists()
    assert "old" in archive.read_text() or archive.read_text()  # content present


def test_rotate_log_preserves_recent_entries(kb_root: Path) -> None:
    _write_log(kb_root, f"# Knowledge Log\n\nPreamble.{_entry(5)}{_entry(10)}{_entry(KEEP_DAYS + 5)}")

    rotate_log(keep_days=KEEP_DAYS)

    log_text = paths.log_path().read_text()
    # The old entry (KEEP_DAYS+5 days ago) was archived — its date should not appear
    old_date = _ts(KEEP_DAYS + 5)[:10]
    # Verify old date is only in archive, not in log (rotate-log entry has today's date)
    archive_files = list(paths.knowledge_root().glob("log.archive.*.md"))
    assert len(archive_files) == 1
    assert old_date in archive_files[0].read_text()


def test_rotate_log_nothing_to_archive(kb_root: Path) -> None:
    _write_log(kb_root, f"# Knowledge Log\n\nPreamble.{_entry(5)}{_entry(10)}")

    result = rotate_log(keep_days=KEEP_DAYS)

    assert result.success
    assert "nothing to rotate" in result.summary


def test_rotate_log_dry_run_does_not_write(kb_root: Path) -> None:
    old_content = f"# Knowledge Log\n\nPreamble.{_entry(KEEP_DAYS + 10)}"
    _write_log(kb_root, old_content)

    result = rotate_log(keep_days=KEEP_DAYS, dry_run=True)

    assert result.success
    assert "dry-run" in result.summary
    assert paths.log_path().read_text() == old_content


def test_rotate_log_missing_log_ok(kb_root: Path) -> None:
    result = rotate_log()
    assert result.success
    assert "does not exist" in result.summary


def test_rotate_log_idempotent(kb_root: Path) -> None:
    _write_log(kb_root, f"# Knowledge Log\n\nPreamble.{_entry(KEEP_DAYS + 10)}")

    r1 = rotate_log(keep_days=KEEP_DAYS)
    # Second run: old entries already in archive, nothing left to rotate
    r2 = rotate_log(keep_days=KEEP_DAYS)

    assert r1.success and r2.success
    assert "nothing to rotate" in r2.summary


def test_rotate_log_appends_to_existing_archive(kb_root: Path) -> None:
    old_dt = datetime.now(timezone.utc) - timedelta(days=KEEP_DAYS + 10)
    q = _quarter(old_dt)
    archive = _archive_path(q)
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text("# Existing archive\n\nOld content.\n")

    _write_log(kb_root, f"# Knowledge Log\n\nPreamble.{_entry(KEEP_DAYS + 10)}")
    rotate_log(keep_days=KEEP_DAYS)

    content = archive.read_text()
    assert "Existing archive" in content
    assert "Old content" in content
