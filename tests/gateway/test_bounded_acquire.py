from __future__ import annotations

import subprocess
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


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


def test_commit_gate_lock_timeout_returns_bounded_result(tmp_path, monkeypatch):
    """When the commit barrier is held, commit() returns retry-later rather than raising.

    Uses real fcntl — only paths.locks_dir is redirected to tmp_path so the
    test's holder thread and the gate compete on the same real lock file.
    COMMIT_LOCK_ACQUIRE_TIMEOUT is monkeypatched low (0.2 s) to keep the test fast.
    """
    from gateway import commit_gate
    from gateway.commit_gate import AuthoredIntent, CommitGate
    from gateway.core import OperationResult
    from gateway.intent_queue import Intent, IntentQueue, compute_intent_id

    # Redirect lock files to tmp_path (real flock, tmp inode).
    monkeypatch.setattr(locking.paths, "locks_dir", lambda: tmp_path / "locks")
    monkeypatch.setattr(commit_gate, "COMMIT_LOCK_ACQUIRE_TIMEOUT", 0.2)

    # Set up a minimal git repo so CommitGate can be constructed.
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md")
    _git(tmp_path, "commit", "-qm", "seed")

    # Build a minimal AuthoredIntent + fencing token via the queue.
    q = IntentQueue()
    payload = {"kind": "source", "target": "wiki/sources/test.md"}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid="HEAD")
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(
        intent=intent,
        writes={"wiki/sources/test.md": "# Test\nbody\n"},
        base_oid="HEAD",
    )
    fencing_token = claim.fencing_token

    # Hold the commit barrier in a background thread with an unbounded lock.
    holder_has_lock = threading.Event()
    release = threading.Event()

    def hold():
        with locking.file_lock("librarian-commit"):  # no timeout — blocks until release
            holder_has_lock.set()
            release.wait(timeout=10)

    t = threading.Thread(target=hold, daemon=True)
    t.start()
    assert holder_has_lock.wait(timeout=5), "holder thread did not acquire lock"

    gate = CommitGate(queue=q)
    result = gate.commit(authored, fencing_token)

    release.set()
    t.join(timeout=5)

    assert isinstance(result, OperationResult)
    assert result.success is False
    assert result.disposition == "retry-later"
    assert result.retry_after == commit_gate.COMMIT_LOCK_RETRY_AFTER
    assert result.intent_id == iid
    assert any("retry" in e or "busy" in e for e in result.errors)
