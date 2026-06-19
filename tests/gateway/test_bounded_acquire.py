from __future__ import annotations

import threading
import time

import pytest

from gateway import locking


def test_bounded_acquire_times_out_when_held(tmp_path, monkeypatch):
    """A real second holder blocks; a bounded acquire raises LockTimeout, never hangs.
    No monkeypatch of fcntl — real flock on a real lock file."""
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path)
    holder_has_lock = threading.Event()
    release = threading.Event()

    def hold():
        with locking.file_lock("librarian-commit"):
            holder_has_lock.set()
            release.wait(timeout=5)

    t = threading.Thread(target=hold)
    t.start()
    assert holder_has_lock.wait(timeout=5)

    start = time.monotonic()
    with pytest.raises(locking.LockTimeout):
        with locking.file_lock("librarian-commit", timeout=0.2):
            pass
    elapsed = time.monotonic() - start
    assert elapsed < 2.0, "bounded acquire must return near its deadline, not hang"

    release.set()
    t.join(timeout=5)


def test_bounded_acquire_succeeds_when_free(tmp_path, monkeypatch):
    """Negative control: a free lock acquires immediately under a bounded timeout."""
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path)
    with locking.file_lock("librarian-commit", timeout=0.2):
        pass  # no raise


def test_no_timeout_is_back_compatible_blocking(tmp_path, monkeypatch):
    """timeout=None preserves blocking LOCK_EX: it waits, then succeeds on release."""
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path)
    release = threading.Event()
    acquired = threading.Event()

    def hold():
        with locking.file_lock("x"):
            acquired.set()
            release.wait(timeout=5)

    t = threading.Thread(target=hold)
    t.start()
    assert acquired.wait(timeout=5)

    got = threading.Event()

    def waiter():
        with locking.file_lock("x"):  # no timeout -> blocks until release
            got.set()

    w = threading.Thread(target=waiter)
    w.start()
    assert not got.wait(timeout=0.3)  # still blocked while held
    release.set()
    assert got.wait(timeout=5)  # unblocks after release
    t.join(timeout=5)
    w.join(timeout=5)


def test_commit_gate_acquires_commit_lock_bounded(monkeypatch):
    """The commit barrier passes a bounded timeout (not None) — never the no-timeout block."""
    import inspect
    from gateway import commit_gate
    src = inspect.getsource(commit_gate)
    assert 'file_lock("librarian-commit", timeout=' in src, (
        "commit barrier must use bounded acquisition (A3)"
    )
    assert commit_gate.COMMIT_LOCK_ACQUIRE_TIMEOUT > 0
