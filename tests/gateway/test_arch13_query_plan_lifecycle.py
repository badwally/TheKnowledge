"""ARCH-13: Query plan lifecycle — status field, stamp_executed, stamp_abandoned, archive."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway.research.query_plan_store import (
    ARCHIVE_AFTER_DAYS,
    STATUS_ABANDONED,
    STATUS_EXECUTED,
    STATUS_PLANNED,
    QueryPlan,
    QueryPlanError,
    archive_dir,
    archive_old_plans,
    load,
    path_for,
    query_plans_dir,
    save,
    stamp_abandoned,
    stamp_executed,
)


# --- helpers -------------------------------------------------------------------


def _make_plan(session_id: str, *, status: str = STATUS_PLANNED) -> QueryPlan:
    return QueryPlan(
        session_id=session_id,
        domain="test-domain",
        prompt="test prompt",
        generated_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        queries={"arxiv": ["test query"]},
        status=status,
    )


# --- status field round-trip ---------------------------------------------------


def test_new_plan_has_planned_status(kb_root: Path) -> None:
    plan = _make_plan("test-plan-001")
    assert plan.status == STATUS_PLANNED


def test_save_load_preserves_status_planned(kb_root: Path) -> None:
    plan = _make_plan("test-plan-002", status=STATUS_PLANNED)
    save(plan)
    loaded = load("test-plan-002")
    assert loaded.status == STATUS_PLANNED


def test_save_load_preserves_status_executed(kb_root: Path) -> None:
    plan = _make_plan("test-plan-003", status=STATUS_EXECUTED)
    plan.executed_at = datetime(2026, 5, 1, tzinfo=timezone.utc)
    save(plan)
    loaded = load("test-plan-003")
    assert loaded.status == STATUS_EXECUTED
    assert loaded.executed_at is not None
    assert loaded.executed_at.year == 2026


def test_save_load_preserves_status_abandoned(kb_root: Path) -> None:
    plan = _make_plan("test-plan-004", status=STATUS_ABANDONED)
    save(plan)
    loaded = load("test-plan-004")
    assert loaded.status == STATUS_ABANDONED


def test_legacy_plans_default_to_planned(kb_root: Path) -> None:
    """Plans without status field (pre-ARCH-13) load as planned."""
    plan = _make_plan("legacy-plan")
    save(plan)
    # Manually strip status from the file
    p = path_for("legacy-plan")
    content = p.read_text()
    lines = [l for l in content.splitlines() if not l.startswith("status:")]
    p.write_text("\n".join(lines) + "\n")
    loaded = load("legacy-plan")
    assert loaded.status == STATUS_PLANNED


# --- stamp_executed ------------------------------------------------------------


def test_stamp_executed_sets_status_and_timestamp(kb_root: Path) -> None:
    plan = _make_plan("exec-plan")
    save(plan)
    stamp_executed("exec-plan")
    loaded = load("exec-plan")
    assert loaded.status == STATUS_EXECUTED
    assert loaded.executed_at is not None


def test_stamp_executed_on_missing_plan_raises(kb_root: Path) -> None:
    with pytest.raises(QueryPlanError):
        stamp_executed("nonexistent-plan")


# --- stamp_abandoned -----------------------------------------------------------


def test_stamp_abandoned_sets_status(kb_root: Path) -> None:
    plan = _make_plan("abandon-plan")
    save(plan)
    stamp_abandoned("abandon-plan")
    loaded = load("abandon-plan")
    assert loaded.status == STATUS_ABANDONED


def test_stamp_abandoned_on_missing_plan_raises(kb_root: Path) -> None:
    with pytest.raises(QueryPlanError):
        stamp_abandoned("nonexistent-plan")


# --- archive_old_plans ---------------------------------------------------------


def test_archive_moves_old_executed_plans(kb_root: Path) -> None:
    plan = _make_plan("old-exec", status=STATUS_EXECUTED)
    plan.executed_at = datetime.now(timezone.utc) - timedelta(days=ARCHIVE_AFTER_DAYS + 5)
    p = save(plan)
    # Age the file's mtime
    old_mtime = (datetime.now(timezone.utc) - timedelta(days=ARCHIVE_AFTER_DAYS + 5)).timestamp()
    os.utime(p, (old_mtime, old_mtime))

    archived = archive_old_plans()
    assert archived == 1
    assert not p.exists()
    assert (archive_dir() / p.name).exists()


def test_archive_skips_planned_plans(kb_root: Path) -> None:
    plan = _make_plan("still-planned")
    p = save(plan)
    old_mtime = (datetime.now(timezone.utc) - timedelta(days=ARCHIVE_AFTER_DAYS + 5)).timestamp()
    os.utime(p, (old_mtime, old_mtime))

    archived = archive_old_plans()
    assert archived == 0
    assert p.exists()


def test_archive_skips_recent_executed_plans(kb_root: Path) -> None:
    plan = _make_plan("recent-exec", status=STATUS_EXECUTED)
    save(plan)  # mtime is now — under the cutoff

    archived = archive_old_plans()
    assert archived == 0


def test_archive_empty_dir_returns_zero(kb_root: Path) -> None:
    assert archive_old_plans() == 0
