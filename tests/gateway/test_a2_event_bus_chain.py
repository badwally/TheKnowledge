"""A2 (M60) — event bus chain: watcher → ingest.complete event → inbox-triage subscribe.

Verifies the decoupled architecture:
- watcher emits ingest.complete after a successful ingest (not coupled directly to inbox-triage)
- events.subscribe("inbox-triage") returns the event (using the subscription YAML config)
- No direct watcher → inbox-triage coupling exists
"""

from __future__ import annotations

import json
import uuid
import yaml
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from gateway import events, frontmatter as fm, paths
from gateway.core import OperationResult
from gateway.watcher import WatcherDaemon


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _write_agent_yaml(kb_root: Path, agent: str, subscribes_to: list[str]) -> None:
    agents_dir = kb_root / ".knowledge" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "agent": agent,
        "subscribes_to": subscribes_to,
        "debounce_s": 0,
        "max_concurrent_runs": 1,
    }
    (agents_dir / f"{agent}.yaml").write_text(yaml.safe_dump(data))


def _make_inbox_file(kb_root: Path, source_id: str = "web-abc") -> Path:
    inbox = kb_root / "raw" / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    p = inbox / f"{source_id}.md"
    front = {"id": source_id, "type": "web", "title": "Test article"}
    p.write_text(fm.serialize(front, "# Test\n\nBody.\n"))
    return p


# ---------------------------------------------------------------------------
# watcher emits ingest.complete on success
# ---------------------------------------------------------------------------


def test_watcher_emits_ingest_complete_on_success(kb_root: Path) -> None:
    inbox_file = _make_inbox_file(kb_root, "web-evt-001")
    raw_target = kb_root / "raw" / "web" / "web-evt-001.md"
    raw_target.parent.mkdir(parents=True, exist_ok=True)
    raw_target.write_text(fm.serialize({"id": "web-evt-001", "type": "web"}, "body"))

    fake_result = OperationResult(
        success=True,
        summary="ingested: web-evt-001 (web)",
        paths_touched=[raw_target],
    )

    def fake_ingest(path: Path) -> OperationResult:
        return fake_result

    daemon = WatcherDaemon(inbox=kb_root / "raw" / "inbox", ingest_fn=fake_ingest, settle_seconds=0)
    daemon._process(inbox_file)

    event_files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(event_files) == 1, "Expected exactly one event file after ingest"

    data = json.loads(event_files[0].read_text())
    assert data["event_type"] == "ingest.complete"
    assert data["agent"] == "watcher"
    assert data["payload"]["source_id"] == "web-evt-001"


def test_watcher_does_not_emit_on_failure(kb_root: Path) -> None:
    inbox_file = _make_inbox_file(kb_root, "web-fail-001")

    def fake_ingest(path: Path) -> OperationResult:
        return OperationResult(success=False, errors=["bad source"])

    daemon = WatcherDaemon(inbox=kb_root / "raw" / "inbox", ingest_fn=fake_ingest, settle_seconds=0)
    daemon._process(inbox_file)

    event_files = list((kb_root / ".knowledge" / "events").rglob("*.json"))
    assert len(event_files) == 0


# ---------------------------------------------------------------------------
# events.subscribe returns ingest.complete for inbox-triage subscriber
# ---------------------------------------------------------------------------


def test_subscribe_inbox_triage_returns_ingest_complete_event(kb_root: Path) -> None:
    _write_agent_yaml(kb_root, "inbox-triage", ["ingest.complete", "poll.complete"])

    # Emit an ingest.complete event (simulating watcher)
    event_id = events.emit(
        "ingest.complete",
        payload={"source_id": "web-sub-001"},
        agent="watcher",
        correlation_id=str(uuid.uuid4()),
    )
    assert event_id  # event was written (not debounced)

    # inbox-triage subscribes — should see the event
    received = events.subscribe("inbox-triage", since_cursor=None)
    assert len(received) == 1
    assert received[0]["event_type"] == "ingest.complete"
    assert received[0]["payload"]["source_id"] == "web-sub-001"


def test_subscribe_inbox_triage_ignores_filter_scored_events(kb_root: Path) -> None:
    _write_agent_yaml(kb_root, "inbox-triage", ["ingest.complete", "poll.complete"])

    # Emit a filter.scored event — inbox-triage does NOT subscribe to this
    events.emit(
        "filter.scored",
        payload={"source_id": "web-filter-001"},
        agent="pipeline",
        correlation_id="c1",
    )

    received = events.subscribe("inbox-triage", since_cursor=None)
    assert received == []


def test_no_direct_watcher_to_triage_coupling(kb_root: Path) -> None:
    """Watcher's _process method must NOT import or call inbox_triage directly."""
    import inspect
    import gateway.watcher as watcher_mod

    source = inspect.getsource(watcher_mod.WatcherDaemon._process)
    assert "inbox_triage" not in source, (
        "Watcher._process must not call inbox_triage directly — "
        "use the event bus for decoupled subscription."
    )
