"""K4 (M48): scheduler substrate for cron-triggered gateway jobs.

A small launchd-driven loop that ticks every 60s and runs any due
entries from `.knowledge/schedule.yaml`. Same shape as the watcher:
launchd manages the daemon (KeepAlive=true, StartInterval=60), this
module owns the per-tick logic.

Per the K4 plan:
- Cron parsing via the lightweight `croniter` dep
- Subprocess shell-out for job execution (any command, not just `wiki *`)
- Per-job `file_lock("schedule-<name>")` so overlapping ticks can't
  double-execute a single job
- Cooldown guard (default 10 min): a job that failed isn't retried
  until `cooldown_seconds` have elapsed, preventing launchd-restart
  thrashing on persistently-broken commands
- UTC-only in v1; users wanting local-time scheduling write a shell
  wrapper that converts

Storage shape (`.knowledge/schedule.yaml`):

    jobs:
      - name: nightly-lint
        cron: "30 4 * * *"
        command: "wiki lint"
        enabled: true
        cooldown_seconds: 600
        last_run: "2026-05-24T04:30:00Z"
        last_exit_code: 0
        last_duration_seconds: 12
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
import subprocess
import time
from typing import Any

import yaml
from croniter import croniter

from gateway import log as log_mod
from gateway import paths
from gateway.locking import file_lock


_DEFAULT_COOLDOWN_SECONDS = 600  # 10 minutes after a failed run


@dataclass
class ScheduleJob:
    """One entry in `.knowledge/schedule.yaml`."""

    name: str
    cron: str
    command: str
    enabled: bool = True
    cooldown_seconds: int = _DEFAULT_COOLDOWN_SECONDS
    last_run: str | None = None              # ISO-8601 UTC
    last_exit_code: int | None = None
    last_duration_seconds: float | None = None


def _schedule_path():
    return paths.knowledge_internal() / "schedule.yaml"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


# --- load / save ----------------------------------------------------------


def load_schedule() -> list[ScheduleJob]:
    """Read `.knowledge/schedule.yaml`. Returns empty list if absent."""
    path = _schedule_path()
    if not path.exists():
        return []
    raw = yaml.safe_load(path.read_text()) or {}
    entries = raw.get("jobs") or []
    out: list[ScheduleJob] = []
    for e in entries:
        # Filter to only known fields; unknown keys are silently dropped to
        # preserve forward compat if the YAML grows.
        kwargs = {
            k: v for k, v in e.items()
            if k in ScheduleJob.__dataclass_fields__
        }
        out.append(ScheduleJob(**kwargs))
    return out


def save_schedule(jobs: list[ScheduleJob]) -> None:
    """Write `.knowledge/schedule.yaml`. Creates the parent directory."""
    path = _schedule_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"jobs": [asdict(j) for j in jobs]}
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))


# --- cron evaluation ------------------------------------------------------


def is_job_due(job: ScheduleJob, now: datetime) -> bool:
    """Return True if `job` should run at `now`.

    Logic:
    - Disabled jobs are never due.
    - Cooldown: if last_exit_code != 0 and last_run was within
      cooldown_seconds, skip.
    - If never run: due at any time the cron expression is satisfied
      from epoch (effectively always-due for sane expressions).
    - Otherwise: compute next-fire time after last_run; due iff
      next-fire <= now.
    """
    if not job.enabled:
        return False

    last_run = _parse_iso(job.last_run)
    if (
        last_run is not None
        and job.last_exit_code is not None
        and job.last_exit_code != 0
    ):
        if now - last_run < timedelta(seconds=job.cooldown_seconds):
            return False

    # Use last_run as the anchor; if missing, treat the job as never-run
    # and due on the first matching cron tick at-or-before `now`.
    if last_run is None:
        # Walk backward from now and check that we're at-or-after the
        # previous cron fire. If the cron has ever fired in history, the
        # job is due.
        prev = croniter(job.cron, now).get_prev(datetime)
        return prev <= now

    next_fire = croniter(job.cron, last_run).get_next(datetime)
    return next_fire <= now


# --- execution ------------------------------------------------------------


@dataclass
class _RunResult:
    exit_code: int
    duration_seconds: float
    stderr_tail: str


def _run_command(command: str) -> _RunResult:
    """Execute `command` via shell. Captures stderr tail for diagnostics."""
    start = time.monotonic()
    try:
        proc = subprocess.run(
            command,
            shell=True,
            cwd=str(paths.knowledge_root()),
            capture_output=True,
            text=True,
            timeout=3600,  # 1h hard ceiling per job
            check=False,
        )
        return _RunResult(
            exit_code=proc.returncode,
            duration_seconds=time.monotonic() - start,
            stderr_tail=(proc.stderr or "").strip()[-300:],
        )
    except subprocess.TimeoutExpired:
        return _RunResult(
            exit_code=124,  # convention for timeout
            duration_seconds=time.monotonic() - start,
            stderr_tail="timed out after 3600s",
        )


def run_all_due(*, dry_run: bool = False) -> dict[str, Any]:
    """Single tick: run every due job. Idempotent under concurrent ticks
    via per-job `file_lock`.

    Returns a summary dict with counts (ran / skipped / would_run /
    failed). Suitable for printing from the CLI dispatcher.
    """
    jobs = load_schedule()
    now = datetime.now(timezone.utc)

    ran = 0
    failed = 0
    skipped = 0
    would_run = 0

    new_jobs: list[ScheduleJob] = []
    for job in jobs:
        if not is_job_due(job, now):
            skipped += 1
            new_jobs.append(job)
            continue

        if dry_run:
            would_run += 1
            new_jobs.append(job)
            continue

        # Per-job lock prevents two scheduler instances from double-executing
        # the same job in the same tick (and a fast-running scheduler from
        # racing against a slow-running prior tick of the same job).
        with file_lock(f"schedule-{job.name}"):
            result = _run_command(job.command)

        ran += 1
        if result.exit_code != 0:
            failed += 1

        # Update the job's bookkeeping fields.
        job.last_run = _now_iso()
        job.last_exit_code = result.exit_code
        job.last_duration_seconds = round(result.duration_seconds, 3)
        new_jobs.append(job)

        log_mod.append(
            op="schedule",
            fields={
                "name": job.name,
                "exit_code": result.exit_code,
                "duration_s": round(result.duration_seconds, 2),
            },
            summary=(
                f"scheduled job {job.name!r} → exit={result.exit_code} "
                f"({result.duration_seconds:.1f}s)"
                + (f"\nstderr tail: {result.stderr_tail}" if result.stderr_tail else "")
            ),
        )

    # Only persist if we actually ran something or are not in dry_run mode.
    if not dry_run and ran > 0:
        save_schedule(new_jobs)

    return {
        "ran": ran,
        "skipped": skipped,
        "failed": failed,
        "would_run": would_run,
    }


# --- helpers exposed for CLI / future MCP wrapper -------------------------


def add_job(
    *,
    name: str,
    cron: str,
    command: str,
    enabled: bool = True,
    cooldown_seconds: int = _DEFAULT_COOLDOWN_SECONDS,
) -> ScheduleJob:
    """Add (or replace by name) a job in the schedule. Returns the new job."""
    # Cron validation: croniter raises on bad expressions.
    croniter(cron, datetime.now(timezone.utc))
    jobs = load_schedule()
    jobs = [j for j in jobs if j.name != name]
    new = ScheduleJob(
        name=name,
        cron=cron,
        command=command,
        enabled=enabled,
        cooldown_seconds=cooldown_seconds,
    )
    jobs.append(new)
    save_schedule(jobs)
    return new


def remove_job(name: str) -> bool:
    """Remove a job by name. Returns True if it existed."""
    jobs = load_schedule()
    new = [j for j in jobs if j.name != name]
    if len(new) == len(jobs):
        return False
    save_schedule(new)
    return True


def set_enabled(name: str, enabled: bool) -> bool:
    """Toggle enabled flag. Returns True if the job existed."""
    jobs = load_schedule()
    found = False
    for j in jobs:
        if j.name == name:
            j.enabled = enabled
            found = True
    if found:
        save_schedule(jobs)
    return found
