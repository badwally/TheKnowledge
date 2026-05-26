"""Persistent storage for per-session query plans.

A `QueryPlan` is the per-adapter query list generated for one
`wiki research` invocation. Plans are written to
`nlm/query_plans/<session-id>.yaml` so the user can:

- review what queries were dispatched after a run (post-hoc audit);
- edit the YAML before resuming with `--execute <session-id>` (pre-flight
  curation);
- accumulate a corpus of curated plans that future plan-client calls
  can consume as few-shot good-example seeds.

The "edited" signal is filesystem-level: if a YAML's mtime is later
than its `generated_at` timestamp, the user has touched it. The
orchestrator stamps `edited: true` on resume so future scans
(`recent_edited`) can find it without re-comparing mtimes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml

from gateway import paths


__all__ = [
    "QueryPlan",
    "QueryPlanError",
    "query_plans_dir",
    "archive_dir",
    "path_for",
    "save",
    "load",
    "exists",
    "is_edited",
    "recent_edited",
    "stamp_executed",
    "stamp_abandoned",
    "archive_old_plans",
]


SCHEMA_VERSION: int = 1

STATUS_PLANNED = "planned"
STATUS_EXECUTED = "executed"
STATUS_ABANDONED = "abandoned"

ARCHIVE_AFTER_DAYS: int = 90


class QueryPlanError(RuntimeError):
    """Raised on missing or malformed query plan files."""


@dataclass
class QueryPlan:
    session_id: str
    domain: str
    prompt: str
    generated_at: datetime
    queries: dict[str, list[str]]
    target_counts: dict[str, int] = field(default_factory=dict)
    plan_client_model: str | None = None
    edited: bool = False
    status: str = STATUS_PLANNED
    executed_at: datetime | None = None
    version: int = SCHEMA_VERSION


def query_plans_dir() -> Path:
    return paths.nlm_dir() / "query_plans"


def archive_dir() -> Path:
    return query_plans_dir() / "archive"


def path_for(session_id: str) -> Path:
    return query_plans_dir() / f"{session_id}.yaml"


def exists(session_id: str) -> bool:
    return path_for(session_id).is_file()


def save(plan: QueryPlan) -> Path:
    """Serialize `plan` to disk; return the file path.

    Creates the parent directory on first write. Overwrites silently —
    the caller is expected to manage session-id uniqueness.
    """
    target = path_for(plan.session_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload: dict = {
        "version": plan.version,
        "session_id": plan.session_id,
        "domain": plan.domain,
        "prompt": plan.prompt,
        "generated_at": plan.generated_at.astimezone(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "plan_client_model": plan.plan_client_model,
        "target_counts": dict(plan.target_counts),
        "queries": {k: list(v) for k, v in plan.queries.items()},
        "edited": plan.edited,
        "status": plan.status,
    }
    if plan.executed_at is not None:
        payload["executed_at"] = plan.executed_at.astimezone(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
    target.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return target


def stamp_executed(session_id: str) -> None:
    """Mark a plan as executed, recording the current time."""
    plan = load(session_id)
    plan.status = STATUS_EXECUTED
    plan.executed_at = datetime.now(timezone.utc)
    save(plan)


def stamp_abandoned(session_id: str) -> None:
    """Mark a plan as abandoned."""
    plan = load(session_id)
    plan.status = STATUS_ABANDONED
    save(plan)


def archive_old_plans(*, older_than_days: int = ARCHIVE_AFTER_DAYS) -> int:
    """Move executed plans older than `older_than_days` to the archive dir.

    Returns the number of plans archived.
    """
    base = query_plans_dir()
    if not base.is_dir():
        return 0
    dest = archive_dir()
    dest.mkdir(parents=True, exist_ok=True)
    cutoff = datetime.now(timezone.utc).timestamp() - older_than_days * 86400
    archived = 0
    for entry in sorted(base.iterdir()):
        if not entry.is_file() or entry.suffix != ".yaml":
            continue
        try:
            plan = load(entry.stem)
        except QueryPlanError:
            continue
        if plan.status != STATUS_EXECUTED:
            continue
        if entry.stat().st_mtime > cutoff:
            continue
        target = dest / entry.name
        entry.rename(target)
        archived += 1
    return archived


def load(session_id: str) -> QueryPlan:
    """Read the plan for `session_id`. Raises if missing or malformed."""
    target = path_for(session_id)
    if not target.is_file():
        raise QueryPlanError(f"no query plan at {target}")
    try:
        raw = yaml.safe_load(target.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        raise QueryPlanError(f"malformed query plan {target}: {e}") from e
    if not isinstance(raw, dict):
        raise QueryPlanError(f"query plan {target} is not a mapping")
    return _parse(raw, source=target)


def is_edited(session_id: str) -> bool:
    """True if the YAML mtime is later than its `generated_at` timestamp.

    Returns False if the plan is missing or unreadable; callers that
    care about that distinction should call `exists` first.
    """
    target = path_for(session_id)
    if not target.is_file():
        return False
    try:
        plan = load(session_id)
    except QueryPlanError:
        return False
    if plan.edited:
        return True
    mtime = datetime.fromtimestamp(target.stat().st_mtime, tz=timezone.utc)
    # Allow 2s slack — write-then-stat can produce mtime slightly after
    # generated_at on slow filesystems even without a user edit.
    return (mtime - plan.generated_at).total_seconds() > 2.0


def recent_edited(domain: str, *, n: int = 5) -> list[QueryPlan]:
    """Return the most recent *edited* plans for `domain`, newest first.

    Used to seed the plan-client with few-shot good examples on
    subsequent runs in the same domain. "Edited" here means the plan's
    `edited: true` flag is set — typically stamped on `--execute` when
    the YAML mtime exceeded `generated_at`.
    """
    base = query_plans_dir()
    if not base.is_dir():
        return []
    plans: list[QueryPlan] = []
    for entry in base.iterdir():
        if not entry.is_file() or entry.suffix != ".yaml":
            continue
        try:
            plan = load(entry.stem)
        except QueryPlanError:
            continue
        if plan.domain != domain or not plan.edited:
            continue
        plans.append(plan)
    plans.sort(key=lambda p: p.generated_at, reverse=True)
    return plans[:n]


# --- internals -------------------------------------------------------------


def _parse(raw: dict, *, source: Path) -> QueryPlan:
    try:
        generated_at_str = raw["generated_at"]
        generated_at = _parse_iso_z(generated_at_str)
    except KeyError as e:
        raise QueryPlanError(f"{source} missing required field: {e}") from e
    except ValueError as e:
        raise QueryPlanError(
            f"{source} has malformed generated_at: {e}"
        ) from e

    queries = raw.get("queries") or {}
    if not isinstance(queries, dict):
        raise QueryPlanError(f"{source}: queries must be a mapping")
    normalized: dict[str, list[str]] = {}
    for adapter, qs in queries.items():
        if not isinstance(qs, list):
            raise QueryPlanError(
                f"{source}: queries.{adapter} must be a list"
            )
        normalized[str(adapter)] = [str(q) for q in qs]

    executed_at_str = raw.get("executed_at")
    executed_at: datetime | None = None
    if executed_at_str:
        try:
            executed_at = _parse_iso_z(str(executed_at_str))
        except ValueError:
            pass

    return QueryPlan(
        session_id=str(raw.get("session_id") or source.stem),
        domain=str(raw["domain"]),
        prompt=str(raw.get("prompt") or ""),
        generated_at=generated_at,
        queries=normalized,
        target_counts={
            str(k): int(v)
            for k, v in (raw.get("target_counts") or {}).items()
        },
        plan_client_model=(
            None
            if raw.get("plan_client_model") is None
            else str(raw["plan_client_model"])
        ),
        edited=bool(raw.get("edited", False)),
        status=str(raw.get("status", STATUS_PLANNED)),
        executed_at=executed_at,
        version=int(raw.get("version", SCHEMA_VERSION)),
    )


def _parse_iso_z(s: str) -> datetime:
    """Parse an ISO-8601 string ending in 'Z' as a tz-aware UTC datetime."""
    if not isinstance(s, str):
        raise ValueError(f"expected string, got {type(s).__name__}")
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt
