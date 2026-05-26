"""Filesystem watcher daemon.

Watches `raw/inbox/` for new markdown files and runs `wiki ingest` on each.
Atomic renames are debounced with a settle delay so partial writes are not
ingested mid-flight. Failed ingests get moved to `raw/inbox/_failed/` with a
timestamp prefix; watcher continues running.

Designed to be run as a launchd agent (`scripts/install_watcher.sh`) but
also runnable in the foreground for development/debug:

    wiki watch
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import logging
import os
import shutil
import signal
import sys
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from gateway import paths


log = logging.getLogger("gateway.watcher")

DEFAULT_SETTLE_SECONDS = 2.0
HEARTBEAT_INTERVAL_SECONDS = 30.0


def pid_file() -> Path:
    return paths.knowledge_internal() / "watcher.pid"


def heartbeat_file() -> Path:
    return paths.knowledge_internal() / "watcher.heartbeat"


def failed_dir() -> Path:
    # inbox is not a source type (it's a drop zone), so build the path directly.
    return paths.raw_dir() / "inbox" / "_failed"


# --- the daemon -------------------------------------------------------------


@dataclass
class WatcherStats:
    """In-memory counters; persisted only via log.md and heartbeat file."""

    started_at: str = ""
    events_received: int = 0
    ingested: int = 0
    failed: int = 0
    skipped_non_md: int = 0


class WatcherDaemon:
    """Coordinates watchdog events into ingest calls with a settle delay."""

    def __init__(
        self,
        *,
        inbox: Path | None = None,
        settle_seconds: float = DEFAULT_SETTLE_SECONDS,
        ingest_fn=None,
    ):
        self._inbox = inbox or (paths.raw_dir() / "inbox")
        self._settle = settle_seconds
        self._pending: dict[Path, threading.Timer] = {}
        self._pending_lock = threading.Lock()
        self._observer: Observer | None = None
        self._stop_event = threading.Event()
        self._heartbeat_thread: threading.Thread | None = None

        # ingest_fn is injectable for tests; default loads lazily so import
        # of this module doesn't pull in trafilatura / yaml unconditionally.
        self._ingest_fn = ingest_fn
        self.stats = WatcherStats()

    # --- lifecycle ---------------------------------------------------------

    def start(self) -> None:
        """Install the observer, write PID file, run until stop()."""
        self._inbox.mkdir(parents=True, exist_ok=True)
        failed_dir().mkdir(parents=True, exist_ok=True)
        paths.knowledge_internal().mkdir(parents=True, exist_ok=True)

        self.stats.started_at = _now_iso()
        pid_file().write_text(str(os.getpid()))

        handler = _InboxEventHandler(self)
        self._observer = Observer()
        self._observer.schedule(handler, str(self._inbox), recursive=False)
        self._observer.start()

        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="watcher-heartbeat"
        )
        self._heartbeat_thread.start()

        log.info("watcher started (inbox=%s, pid=%s)", self._inbox, os.getpid())

        # Process anything that landed in inbox before we started
        self._scan_existing()

        try:
            while not self._stop_event.is_set():
                self._stop_event.wait(timeout=1.0)
        finally:
            self._shutdown()

    def stop(self) -> None:
        """Signal stop and wait for shutdown."""
        self._stop_event.set()

    def _shutdown(self) -> None:
        log.info("watcher stopping")
        if self._observer is not None:
            self._observer.stop()
            self._observer.join(timeout=5)
            self._observer = None

        with self._pending_lock:
            for timer in self._pending.values():
                timer.cancel()
            self._pending.clear()

        try:
            pid_file().unlink(missing_ok=True)
            heartbeat_file().unlink(missing_ok=True)
        except OSError:
            pass

        log.info("watcher stopped (events=%d ingested=%d failed=%d)",
                 self.stats.events_received, self.stats.ingested, self.stats.failed)

    def _heartbeat_loop(self) -> None:
        while not self._stop_event.is_set():
            try:
                heartbeat_file().write_text(_now_iso())
            except OSError as e:
                log.warning("heartbeat write failed: %s", e)
            self._stop_event.wait(timeout=HEARTBEAT_INTERVAL_SECONDS)

    def _scan_existing(self) -> None:
        """Process files that were already in inbox/ when we started."""
        if not self._inbox.exists():
            return
        for path in self._inbox.iterdir():
            if path.is_file() and path.suffix == ".md":
                self.handle_event(path)

    # --- event entry points -----------------------------------------------

    def handle_event(self, path: Path) -> None:
        """Schedule processing of `path` after the settle delay.

        Re-arming on subsequent events for the same path naturally debounces
        partial writes and tools that emit multiple modify events per save.
        """
        if path.parent != self._inbox:
            return  # not our concern
        if not path.suffix == ".md":
            self.stats.skipped_non_md += 1
            log.info("skipping non-md file: %s", path.name)
            return

        self.stats.events_received += 1
        with self._pending_lock:
            existing = self._pending.pop(path, None)
            if existing is not None:
                existing.cancel()
            timer = threading.Timer(
                self._settle, self._process_after_settle, args=(path,)
            )
            timer.daemon = True
            self._pending[path] = timer
            timer.start()

    def _process_after_settle(self, path: Path) -> None:
        with self._pending_lock:
            self._pending.pop(path, None)

        if not path.exists():
            log.info("file gone before settle: %s", path)
            return

        self._process(path)

    def _process(self, path: Path) -> None:
        ingest_fn = self._ingest_fn or _default_ingest
        try:
            result = ingest_fn(path)
        except Exception as e:  # never let the watcher die on bad input
            log.error("ingest crashed on %s: %s", path, e, exc_info=True)
            self._move_to_failed(path, reason=f"crash: {e}")
            self.stats.failed += 1
            return

        if result.success:
            self.stats.ingested += 1
            log.info("ingested: %s — %s", path.name, result.summary)
            for w in result.warnings:
                log.warning("  %s", w)
            # Emit ingest.complete event so AGT-1 subscribers can pick it up.
            if result.paths_touched:
                try:
                    import uuid
                    from gateway import events as _events
                    source_id = result.paths_touched[0].stem
                    _events.emit(
                        "ingest.complete",
                        payload={"source_id": source_id},
                        agent="watcher",
                        correlation_id=str(uuid.uuid4()),
                    )
                except Exception as _e:
                    log.warning("event emission failed for %s: %s", path.name, _e)
            # Successful ingest -> file is now in raw/<type>/<id>.md;
            # the inbox copy is no longer needed.
            try:
                path.unlink()
            except OSError as e:
                log.warning("could not remove inbox file %s: %s", path, e)
        else:
            self.stats.failed += 1
            log.error("ingest failed: %s — %s", path.name, "; ".join(result.errors))
            self._move_to_failed(path, reason="; ".join(result.errors))

    def _move_to_failed(self, path: Path, *, reason: str) -> None:
        """Move a problematic file to inbox/_failed/<timestamp>-<name>."""
        target_dir = failed_dir()
        target_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        target = target_dir / f"{timestamp}-{path.name}"
        try:
            shutil.move(str(path), str(target))
        except OSError as e:
            log.error("could not move %s to %s: %s", path, target, e)
            return
        # Drop a sibling .reason.txt for forensics
        try:
            target.with_suffix(target.suffix + ".reason.txt").write_text(reason + "\n")
        except OSError:
            pass
        log.info("moved to failed: %s (%s)", target.name, reason)


# --- watchdog adapter -------------------------------------------------------


class _InboxEventHandler(FileSystemEventHandler):
    """Thin watchdog adapter that forwards relevant events to the daemon."""

    def __init__(self, daemon: WatcherDaemon):
        self._daemon = daemon

    def on_created(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self._daemon.handle_event(Path(event.src_path))

    def on_moved(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        # Atomic writes (write-tmp + rename) land here as the destination
        self._daemon.handle_event(Path(event.dest_path))


# --- helpers ---------------------------------------------------------------


def _default_ingest(path: Path):
    """Default ingest function used by the daemon when none is injected."""
    from gateway.ops.ingest import ingest

    return ingest(path)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --- foreground runner -----------------------------------------------------


def run_foreground() -> int:
    """Entry point used by `wiki watch` and the launchd plist."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )
    daemon = WatcherDaemon()

    def _on_signal(signum, _frame):
        log.info("received signal %s", signum)
        daemon.stop()

    signal.signal(signal.SIGINT, _on_signal)
    signal.signal(signal.SIGTERM, _on_signal)

    try:
        daemon.start()
        return 0
    except Exception as e:
        log.error("watcher exited with error: %s", e, exc_info=True)
        return 1


# --- inspection used by `wiki status` --------------------------------------


def watcher_state() -> dict:
    """Snapshot of watcher liveness for status reporting."""
    pid_path = pid_file()
    hb_path = heartbeat_file()
    state: dict = {
        "running": False,
        "pid": None,
        "started_at": None,
        "last_heartbeat": None,
        "inbox_pending": 0,
        "inbox_failed": 0,
    }

    if pid_path.exists():
        try:
            pid = int(pid_path.read_text().strip())
            os.kill(pid, 0)  # signal 0: liveness probe
            state["running"] = True
            state["pid"] = pid
        except (ValueError, ProcessLookupError, PermissionError, OSError):
            pass

    if hb_path.exists():
        state["last_heartbeat"] = hb_path.read_text().strip()

    inbox = paths.raw_dir() / "inbox"
    if inbox.exists():
        state["inbox_pending"] = sum(
            1 for p in inbox.iterdir() if p.is_file() and p.suffix == ".md"
        )
    failed = failed_dir()
    if failed.exists():
        state["inbox_failed"] = sum(1 for _ in failed.iterdir() if _.is_file())

    return state
