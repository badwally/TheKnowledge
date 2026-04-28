"""Named file locks under .knowledge/locks/.

Uses POSIX flock for exclusive locking. Tests can run in parallel safely
because each lock name maps to a unique file and flock is per-file.
"""

import contextlib
import fcntl
from typing import Iterator

from gateway import paths


@contextlib.contextmanager
def file_lock(name: str) -> Iterator[None]:
    """Acquire an exclusive lock identified by `name`.

    Lock files are persistent (we don't delete them) so two processes locking
    the same name see the same inode. Empty lock files are harmless.
    """
    locks = paths.locks_dir()
    locks.mkdir(parents=True, exist_ok=True)
    lock_path = locks / f"{name}.lock"

    # Open in append mode so we don't truncate; the file's content is unused.
    with open(lock_path, "a") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
