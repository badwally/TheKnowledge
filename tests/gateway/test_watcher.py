"""Tests for the M4 filesystem watcher daemon.

Most tests exercise WatcherDaemon directly without spinning up watchdog,
since the watchdog Observer→handler→queue chain is just a thin adapter.
One end-to-end test runs a real Observer in a thread to confirm the
adapter actually fires.
"""

from __future__ import annotations

import threading
import time
from pathlib import Path

import pytest

from gateway import paths
from gateway.core import OperationResult
from gateway.watcher import WatcherDaemon, run_foreground, watcher_state


# --- helpers ----------------------------------------------------------------


def _record(results, status="ok", **kwargs):
    """Build a fake ingest function that records the path it was called with."""

    def _fake_ingest(path):
        results.append(path)
        if status == "ok":
            return OperationResult(success=True, summary=f"ingested {path.name}", **kwargs)
        if status == "fail":
            return OperationResult(success=False, errors=["fake failure"])
        if status == "crash":
            raise RuntimeError("boom")
        raise ValueError(status)

    return _fake_ingest


# --- handle_event / settle / process ---------------------------------------


def test_handle_event_ignores_non_md(kb_root):
    daemon = WatcherDaemon(settle_seconds=0.05, ingest_fn=lambda p: OperationResult(success=True))
    daemon.handle_event(kb_root / "raw" / "inbox" / "ignore.txt")
    assert daemon.stats.skipped_non_md == 1
    assert daemon.stats.events_received == 0


def test_handle_event_ignores_files_outside_inbox(kb_root):
    daemon = WatcherDaemon(settle_seconds=0.05, ingest_fn=lambda p: OperationResult(success=True))
    elsewhere = kb_root / "raw" / "youtube" / "x.md"
    elsewhere.write_text("---\nid: x\n---\nbody\n")
    daemon.handle_event(elsewhere)
    assert daemon.stats.events_received == 0


def test_settle_processes_after_delay(kb_root):
    inbox = kb_root / "raw" / "inbox"
    target = inbox / "x.md"
    target.write_text("hello")

    seen: list[Path] = []
    daemon = WatcherDaemon(settle_seconds=0.05, ingest_fn=_record(seen))
    daemon.handle_event(target)

    # Wait beyond the settle delay
    time.sleep(0.2)
    assert seen == [target]
    assert daemon.stats.ingested == 1
    # successful ingest removes the inbox file
    assert not target.exists()


def test_settle_debounces_multiple_events(kb_root):
    inbox = kb_root / "raw" / "inbox"
    target = inbox / "y.md"
    target.write_text("hello")

    seen: list[Path] = []
    daemon = WatcherDaemon(settle_seconds=0.1, ingest_fn=_record(seen))

    # Three rapid events should result in a single ingest
    daemon.handle_event(target)
    time.sleep(0.02)
    daemon.handle_event(target)
    time.sleep(0.02)
    daemon.handle_event(target)

    time.sleep(0.3)
    assert seen == [target]
    assert daemon.stats.events_received == 3
    assert daemon.stats.ingested == 1


def test_failed_ingest_moves_to_failed(kb_root):
    inbox = kb_root / "raw" / "inbox"
    target = inbox / "bad.md"
    target.write_text("malformed")

    daemon = WatcherDaemon(settle_seconds=0.05, ingest_fn=_record([], status="fail"))
    daemon.handle_event(target)
    time.sleep(0.2)

    failed = list((inbox / "_failed").iterdir())
    moved = [p for p in failed if p.name.endswith("-bad.md")]
    assert len(moved) == 1
    reasons = [p for p in failed if p.name.endswith(".reason.txt")]
    assert len(reasons) == 1
    assert "fake failure" in reasons[0].read_text()
    assert daemon.stats.failed == 1


def test_crashing_ingest_moves_to_failed_and_keeps_running(kb_root):
    inbox = kb_root / "raw" / "inbox"
    target = inbox / "crash.md"
    target.write_text("triggers crash")

    daemon = WatcherDaemon(settle_seconds=0.05, ingest_fn=_record([], status="crash"))
    daemon.handle_event(target)
    time.sleep(0.2)

    failed = [p for p in (inbox / "_failed").iterdir() if p.name.endswith("-crash.md")]
    assert len(failed) == 1
    assert daemon.stats.failed == 1


def test_file_disappears_before_settle(kb_root):
    inbox = kb_root / "raw" / "inbox"
    target = inbox / "ephemeral.md"
    target.write_text("about to vanish")

    seen: list[Path] = []
    daemon = WatcherDaemon(settle_seconds=0.1, ingest_fn=_record(seen))
    daemon.handle_event(target)
    target.unlink()  # remove before settle expires

    time.sleep(0.25)
    # Nothing was processed because the file vanished
    assert seen == []
    assert daemon.stats.ingested == 0
    assert daemon.stats.failed == 0


# --- watcher_state inspection ----------------------------------------------


def test_watcher_state_not_running(kb_root):
    state = watcher_state()
    assert state["running"] is False
    assert state["pid"] is None
    assert state["inbox_pending"] == 0


def test_watcher_state_counts_inbox(kb_root):
    inbox = kb_root / "raw" / "inbox"
    (inbox / "a.md").write_text("a")
    (inbox / "b.md").write_text("b")
    (inbox / "skip.txt").write_text("ignored by watcher anyway")
    state = watcher_state()
    assert state["inbox_pending"] == 2  # only .md files counted


def test_watcher_state_detects_running_pid(kb_root, monkeypatch):
    pid_path = kb_root / ".knowledge" / "watcher.pid"
    pid_path.parent.mkdir(parents=True, exist_ok=True)
    pid_path.write_text(str(threading.get_ident() and 99999))  # placeholder

    # Ensure os.kill says "alive" by patching it
    import gateway.watcher as watcher_mod

    monkeypatch.setattr(watcher_mod.os, "kill", lambda pid, sig: None)
    state = watcher_state()
    assert state["running"] is True


# --- end-to-end with real watchdog Observer (slow but real) ----------------


def test_observer_wires_through_to_ingest(kb_root):
    """A real watchdog Observer should pick up a new file and feed the daemon."""
    inbox = kb_root / "raw" / "inbox"

    seen: list[Path] = []
    daemon = WatcherDaemon(settle_seconds=0.1, ingest_fn=_record(seen))

    # Run start() in a background thread
    t = threading.Thread(target=daemon.start, daemon=True)
    t.start()

    # Give the observer a moment to install
    time.sleep(0.2)

    # Drop a file
    new = inbox / "dropped.md"
    new.write_text("dropped by test")

    # Wait for settle + processing
    deadline = time.time() + 3.0
    while time.time() < deadline and not seen:
        time.sleep(0.05)

    daemon.stop()
    t.join(timeout=3.0)

    assert seen, "observer did not deliver the new file to the daemon"
    assert seen[0].name == "dropped.md"
