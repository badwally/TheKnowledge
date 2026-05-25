"""Tests for AGT-9: filesystem event bus."""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from gateway import events, paths


# ── helpers ──────────────────────────────────────────────────────────────────

def _agent_yaml(root: Path, agent_name: str, subscribes_to: list[str], debounce_s: int = 0, max_concurrent: int = 1) -> None:
    agents_dir = root / ".knowledge" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "agent": agent_name,
        "subscribes_to": subscribes_to,
        "debounce_s": debounce_s,
        "max_concurrent_runs": max_concurrent,
    }
    (agents_dir / f"{agent_name}.yaml").write_text(yaml.safe_dump(data))


# ── emit ─────────────────────────────────────────────────────────────────────

def test_emit_writes_json_file(kb_root: Path) -> None:
    event_id = events.emit("ingest.complete", payload={"source": "s1"}, agent="triage", correlation_id="log-123")
    assert event_id is not None
    # Find the written file
    event_files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(event_files) == 1
    data = json.loads(event_files[0].read_text())
    assert data["event_id"] == event_id
    assert data["event_type"] == "ingest.complete"
    assert data["agent"] == "triage"
    assert data["correlation_id"] == "log-123"
    assert data["payload"] == {"source": "s1"}
    assert "emitted_at" in data


def test_emit_sequence_zero_padded(kb_root: Path) -> None:
    events.emit("ingest.complete", payload={}, agent="a", correlation_id="c1")
    events.emit("filter.scored", payload={}, agent="a", correlation_id="c2")
    events.emit("poll.complete", payload={}, agent="a", correlation_id="c3")
    files = sorted((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(files) == 3
    stems = [f.stem for f in files]
    assert stems[0] == "0000"
    assert stems[1] == "0001"
    assert stems[2] == "0002"


def test_emit_sequence_monotonic_per_day(kb_root: Path) -> None:
    for _ in range(5):
        events.emit("agent.run", payload={}, agent="x", correlation_id="c")
    files = sorted((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(files) == 5
    stems = [int(f.stem) for f in files]
    assert stems == list(range(5))


def test_emit_stores_correlation_id_verbatim(kb_root: Path) -> None:
    corr = "log-entry-ABCDEF-2026-05-25"
    events.emit("ingest.complete", payload={}, agent="ag", correlation_id=corr)
    files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    data = json.loads(files[0].read_text())
    assert data["correlation_id"] == corr


def test_emit_event_id_is_uuid4_like(kb_root: Path) -> None:
    event_id = events.emit("ingest.complete", payload={}, agent="a", correlation_id="x")
    # uuid4 format: 8-4-4-4-12 hex digits
    import re
    assert re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", event_id)


# ── debounce ─────────────────────────────────────────────────────────────────

def test_debounce_suppresses_duplicate_within_window(kb_root: Path) -> None:
    _agent_yaml(kb_root, "triage", ["ingest.complete"], debounce_s=60)
    events.emit("ingest.complete", payload={"n": 1}, agent="triage", correlation_id="c1")
    events.emit("ingest.complete", payload={"n": 2}, agent="triage", correlation_id="c2")
    files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(files) == 1


def test_debounce_allows_different_event_type(kb_root: Path) -> None:
    _agent_yaml(kb_root, "triage", ["ingest.complete", "filter.scored"], debounce_s=60)
    events.emit("ingest.complete", payload={}, agent="triage", correlation_id="c1")
    events.emit("filter.scored", payload={}, agent="triage", correlation_id="c2")
    files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(files) == 2


def test_debounce_zero_never_suppresses(kb_root: Path) -> None:
    _agent_yaml(kb_root, "triage", ["ingest.complete"], debounce_s=0)
    events.emit("ingest.complete", payload={}, agent="triage", correlation_id="c1")
    events.emit("ingest.complete", payload={}, agent="triage", correlation_id="c2")
    files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(files) == 2


# ── subscribe ─────────────────────────────────────────────────────────────────

def test_subscribe_returns_matching_events(kb_root: Path) -> None:
    _agent_yaml(kb_root, "inbox", ["ingest.complete", "poll.complete"])
    e1 = events.emit("ingest.complete", payload={"s": "a"}, agent="pipeline", correlation_id="c1")
    events.emit("filter.scored", payload={}, agent="pipeline", correlation_id="c2")
    e3 = events.emit("poll.complete", payload={}, agent="pipeline", correlation_id="c3")
    found = events.subscribe("inbox", since_cursor=None)
    ids = {e["event_id"] for e in found}
    assert e1 in ids
    assert e3 in ids
    # filter.scored not in subscription
    assert all(e["event_type"] in ("ingest.complete", "poll.complete") for e in found)


def test_subscribe_since_cursor_excludes_older(kb_root: Path) -> None:
    _agent_yaml(kb_root, "inbox", ["ingest.complete"])
    e1 = events.emit("ingest.complete", payload={}, agent="p", correlation_id="c1")
    e2 = events.emit("ingest.complete", payload={}, agent="p", correlation_id="c2")
    # cursor = e1 path means only events after it
    files = sorted((kb_root / ".knowledge" / "events").rglob("*.json"))
    cursor = str(files[0])
    found = events.subscribe("inbox", since_cursor=cursor)
    ids = {e["event_id"] for e in found}
    assert e1 not in ids
    assert e2 in ids


def test_subscribe_missing_agent_returns_empty(kb_root: Path) -> None:
    events.emit("ingest.complete", payload={}, agent="p", correlation_id="c")
    found = events.subscribe("nonexistent-agent", since_cursor=None)
    assert found == []


# ── lock name registry ────────────────────────────────────────────────────────

def test_agent_lock_prefix_registered() -> None:
    from gateway.locking import LOCK_NAME_PREFIXES, is_known_lock_name
    assert "agent" in LOCK_NAME_PREFIXES or is_known_lock_name("agent-triage")


# ── paths ─────────────────────────────────────────────────────────────────────

def test_events_dir_under_knowledge_internal(kb_root: Path) -> None:
    assert paths.events_dir() == kb_root / ".knowledge" / "events"


def test_agents_dir_under_knowledge_internal(kb_root: Path) -> None:
    assert paths.agents_dir() == kb_root / ".knowledge" / "agents"
