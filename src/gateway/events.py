"""AGT-9: filesystem event bus.

Events are written to .knowledge/events/<YYYY-MM-DD>/<seq:04d>.json.
Sequence numbers are monotonic within a calendar day (UTC).

Subscriptions are read from .knowledge/agents/<name>.yaml.

Debounce: if a subscription YAML defines debounce_s > 0, a second emit
of the same event_type by the same agent within that window is suppressed
(no file written).

max_concurrent_runs: enforced via lock file at .knowledge/locks/agent-<name>.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway import paths
from gateway.locking import file_lock


def _today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _next_seq(day_dir: Path) -> int:
    """Return the next zero-based sequence integer for the given day directory."""
    existing = sorted(day_dir.glob("*.json"))
    if not existing:
        return 0
    return int(existing[-1].stem) + 1


def _load_agent_config(agent_name: str) -> dict | None:
    config_path = paths.agents_dir() / f"{agent_name}.yaml"
    if not config_path.exists():
        return None
    return yaml.safe_load(config_path.read_text()) or {}


def _find_last_emit_time(event_type: str, agent: str) -> float | None:
    """Return the Unix timestamp of the most recent event of (event_type, agent), or None."""
    ev_dir = paths.events_dir()
    if not ev_dir.exists():
        return None
    latest: float | None = None
    for json_file in ev_dir.rglob("*.json"):
        try:
            data = json.loads(json_file.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if data.get("event_type") == event_type and data.get("agent") == agent:
            emitted = data.get("emitted_at", "")
            try:
                ts = datetime.strptime(emitted, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()
                if latest is None or ts > latest:
                    latest = ts
            except ValueError:
                continue
    return latest


def emit(
    event_type: str,
    *,
    payload: dict[str, Any],
    agent: str,
    correlation_id: str,
) -> str:
    """Emit an event to the event store.

    Returns the event_id (uuid4 string). If a matching subscription config
    has debounce_s > 0 and the same (event_type, agent) was emitted within
    that window, the event is suppressed and the prior event_id is returned
    as an empty string.
    """
    # Check debounce against any subscription config for this agent
    config = _load_agent_config(agent)
    if config:
        debounce_s = int(config.get("debounce_s", 0))
        if debounce_s > 0:
            last = _find_last_emit_time(event_type, agent)
            if last is not None:
                import time as _time
                age = _time.time() - last
                if age < debounce_s:
                    return ""

    day_dir = paths.events_dir() / _today_str()
    day_dir.mkdir(parents=True, exist_ok=True)

    event_id = str(uuid.uuid4())
    seq = _next_seq(day_dir)
    event_data = {
        "event_id": event_id,
        "event_type": event_type,
        "correlation_id": correlation_id,
        "agent": agent,
        "payload": payload,
        "emitted_at": _iso_now(),
    }
    out_path = day_dir / f"{seq:04d}.json"
    out_path.write_text(json.dumps(event_data, indent=2))
    return event_id


def subscribe(
    agent_name: str,
    *,
    since_cursor: str | None,
) -> list[dict]:
    """Return events matching this agent's subscription since since_cursor.

    since_cursor is the path string of the last-seen event file; events at
    or before that path (lexicographic order) are excluded. Pass None to
    return all matching events.

    Returns [] if no subscription config exists for agent_name.
    """
    config = _load_agent_config(agent_name)
    if config is None:
        return []

    subscribed_types: list[str] = config.get("subscribes_to", [])

    ev_dir = paths.events_dir()
    if not ev_dir.exists():
        return []

    all_files = sorted(ev_dir.rglob("*.json"))
    if since_cursor is not None:
        cursor_path = Path(since_cursor)
        all_files = [f for f in all_files if f > cursor_path]

    results: list[dict] = []
    for json_file in all_files:
        try:
            data = json.loads(json_file.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if data.get("event_type") in subscribed_types:
            results.append(data)
    return results


def list_events(
    *,
    since: datetime | None = None,
    event_type: str | None = None,
    agent: str | None = None,
) -> list[dict]:
    """Return all events, optionally filtered by time window, type, or agent."""
    ev_dir = paths.events_dir()
    if not ev_dir.exists():
        return []

    results: list[dict] = []
    for json_file in sorted(ev_dir.rglob("*.json")):
        try:
            data = json.loads(json_file.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if event_type is not None and data.get("event_type") != event_type:
            continue
        if agent is not None and data.get("agent") != agent:
            continue
        if since is not None:
            emitted = data.get("emitted_at", "")
            try:
                ts = datetime.strptime(emitted, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                if ts < since:
                    continue
            except ValueError:
                continue
        results.append(data)
    return results
