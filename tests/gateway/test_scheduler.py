"""K4 (M48): scheduler substrate tests."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import paths
from gateway.scheduler import (
    ScheduleJob,
    is_job_due,
    load_schedule,
    run_all_due,
    save_schedule,
)


def _utc(dt_str: str) -> datetime:
    """Parse ISO-8601 'YYYY-MM-DDTHH:MM:SSZ' into a tz-aware UTC datetime."""
    return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


# --- load/save round-trip ---------------------------------------------------


def test_load_empty_schedule_when_file_missing(kb_root: Path):
    jobs = load_schedule()
    assert jobs == []


def test_save_then_load_roundtrip(kb_root: Path):
    jobs = [
        ScheduleJob(
            name="nightly-lint",
            cron="30 4 * * *",
            command="wiki lint",
            enabled=True,
        ),
        ScheduleJob(
            name="hourly-poll",
            cron="0 * * * *",
            command="wiki poll apple-notes",
            enabled=False,
        ),
    ]
    save_schedule(jobs)
    loaded = load_schedule()
    assert len(loaded) == 2
    by_name = {j.name: j for j in loaded}
    assert by_name["nightly-lint"].cron == "30 4 * * *"
    assert by_name["nightly-lint"].enabled is True
    assert by_name["hourly-poll"].enabled is False


# --- is_job_due cron semantics ---------------------------------------------


def test_is_job_due_first_run_is_due(kb_root: Path):
    """A job that has never run before is due at any reasonable `now`."""
    job = ScheduleJob(
        name="x",
        cron="*/5 * * * *",
        command="echo hi",
        enabled=True,
        last_run=None,
    )
    now = _utc("2026-05-24T15:00:00Z")
    assert is_job_due(job, now) is True


def test_is_job_due_disabled_never_due(kb_root: Path):
    job = ScheduleJob(
        name="x",
        cron="* * * * *",
        command="echo hi",
        enabled=False,
        last_run=None,
    )
    assert is_job_due(job, _utc("2026-05-24T15:00:00Z")) is False


def test_is_job_due_recent_run_not_due(kb_root: Path):
    """A job that just ran 30s ago isn't due yet on a */5 schedule."""
    job = ScheduleJob(
        name="x",
        cron="*/5 * * * *",
        command="echo hi",
        enabled=True,
        last_run="2026-05-24T14:55:00Z",
    )
    # Next */5 boundary after 14:55 is 15:00. At 14:55:30 still not due.
    assert is_job_due(job, _utc("2026-05-24T14:55:30Z")) is False


def test_is_job_due_after_interval(kb_root: Path):
    job = ScheduleJob(
        name="x",
        cron="*/5 * * * *",
        command="echo hi",
        enabled=True,
        last_run="2026-05-24T14:55:00Z",
    )
    # 15:01 is past the 15:00 cron firing → due.
    assert is_job_due(job, _utc("2026-05-24T15:01:00Z")) is True


# --- cooldown guard --------------------------------------------------------


def test_is_job_due_respects_cooldown_after_failure(kb_root: Path):
    """A job that failed within `cooldown_seconds` should not re-run yet."""
    job = ScheduleJob(
        name="x",
        cron="* * * * *",  # every minute
        command="exit 1",
        enabled=True,
        last_run="2026-05-24T15:00:00Z",
        last_exit_code=1,
        cooldown_seconds=600,
    )
    # 5 minutes after a failure: cooldown is 10 minutes, so not due.
    assert is_job_due(job, _utc("2026-05-24T15:05:00Z")) is False


def test_is_job_due_after_cooldown_expires(kb_root: Path):
    job = ScheduleJob(
        name="x",
        cron="* * * * *",
        command="exit 1",
        enabled=True,
        last_run="2026-05-24T15:00:00Z",
        last_exit_code=1,
        cooldown_seconds=600,
    )
    # 11 minutes after failure: cooldown expired → due.
    assert is_job_due(job, _utc("2026-05-24T15:11:00Z")) is True


# --- run_all_due ----------------------------------------------------------


def test_run_all_due_executes_due_job_and_records_exit_code(kb_root: Path, tmp_path: Path):
    sentinel = tmp_path / "scheduler-test-marker.txt"
    jobs = [
        ScheduleJob(
            name="touch-sentinel",
            cron="* * * * *",
            command=f"echo touched >> {sentinel}",
            enabled=True,
            last_run=None,
        )
    ]
    save_schedule(jobs)

    summary = run_all_due()
    assert summary["ran"] == 1
    assert summary["skipped"] == 0
    assert sentinel.exists()

    # After running, last_run + last_exit_code persist
    reloaded = load_schedule()
    assert reloaded[0].last_run is not None
    assert reloaded[0].last_exit_code == 0


def test_run_all_due_skips_disabled_jobs(kb_root: Path):
    jobs = [
        ScheduleJob(
            name="off",
            cron="* * * * *",
            command="echo x",
            enabled=False,
        )
    ]
    save_schedule(jobs)
    summary = run_all_due()
    assert summary["ran"] == 0
    assert summary["skipped"] == 1


def test_run_all_due_dry_run_does_not_execute(kb_root: Path, tmp_path: Path):
    sentinel = tmp_path / "dry-run-must-not-appear.txt"
    jobs = [
        ScheduleJob(
            name="x",
            cron="* * * * *",
            command=f"echo nope >> {sentinel}",
            enabled=True,
            last_run=None,
        )
    ]
    save_schedule(jobs)
    summary = run_all_due(dry_run=True)
    assert summary["would_run"] == 1
    assert not sentinel.exists()


def test_run_all_due_logs_through_gateway(kb_root: Path, tmp_path: Path):
    """Each scheduled run appends one structured log line."""
    sentinel = tmp_path / "log-test.txt"
    jobs = [
        ScheduleJob(
            name="logged-job",
            cron="* * * * *",
            command=f"echo x >> {sentinel}",
            enabled=True,
        )
    ]
    save_schedule(jobs)
    run_all_due()

    log_text = paths.log_path().read_text() if paths.log_path().exists() else ""
    assert "schedule" in log_text
    assert "name=logged-job" in log_text or "logged-job" in log_text
