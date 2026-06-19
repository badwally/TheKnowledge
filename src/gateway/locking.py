"""Named file locks under .knowledge/locks/.

Uses POSIX flock for exclusive locking. Tests can run in parallel safely
because each lock name maps to a unique file and flock is per-file.

M47 introduces `LOCK_NAMES` — a registry of sanctioned lock-name prefixes
and exact names so the concurrency model is auditable from one place. The
registry is informational today; a future milestone may enforce it at
`file_lock(...)` call sites.
"""

import contextlib
import fcntl
import re
from typing import Iterator

from gateway import paths


# Sanctioned lock-name surface as of M47. Exact names + name prefixes.
# Listed here so the concurrency model is auditable without grepping the
# whole codebase. Enforcement is informational today (see
# `is_known_lock_name`); future milestones may turn the assertion on.
LOCK_NAMES: frozenset[str] = frozenset(
    {
        # Single-global write barriers
        "wiki-author",       # any gateway op that mutates a wiki/<type>/<slug>.md
        "nlm-registry",      # mutations to nlm/notebooks.yaml or nlm/source_maps/
        "log",               # log.md append (M47 fix for ARCH-1 racy log)
        "index",             # index.md update (M47 fix for ARCH-1 racy index)
        # Librarian Phase 1 (decision 1): the single serial commit barrier.
        # Replaces the global `wiki-author` barrier for the commit step (§4
        # migration delta); authoring runs concurrently, only commit is serial.
        "librarian-commit",
    }
)


# Sanctioned per-resource lock-name PREFIXES — `<prefix>-<id>` is allowed.
LOCK_NAME_PREFIXES: frozenset[str] = frozenset(
    {
        "ingest",            # per-source ingest: ingest-<source-id>
        "schedule",          # per-scheduled-job (K4): schedule-<job-name>
        "agent",             # per-agent concurrency (AGT-9): agent-<name>
    }
)

_PREFIX_RE = re.compile(r"^(?P<prefix>[a-z][a-z0-9]*)-[A-Za-z0-9._-]+$")


def is_known_lock_name(name: str) -> bool:
    """Return True if `name` is sanctioned per LOCK_NAMES / LOCK_NAME_PREFIXES.

    Informational helper for audits and future enforcement. ``file_lock()``
    does not call this today — adding a lock name to either set is a
    documentation update, not a behavior change.
    """
    if name in LOCK_NAMES:
        return True
    m = _PREFIX_RE.match(name)
    if m and m.group("prefix") in LOCK_NAME_PREFIXES:
        return True
    return False


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
