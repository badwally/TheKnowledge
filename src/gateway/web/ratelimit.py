"""In-process per-token rate limiting.

Product-readiness review (260530) finding #2: with auth in place, a single
credentialed caller could still flood the mutating/expensive endpoints and
drain paid LLM/NotebookLM quota. A token bucket per identity caps the rate.

Kept deliberately small and dependency-free (no slowapi): the gateway is a
single-process service with a handful of tokens, so an in-memory dict of
buckets is sufficient and needs no eviction. The middleware consults this
only for non-GET requests, so read/polling traffic is never limited.

Default rate is `WIKI_RATE_LIMIT_PER_MIN` (60/min ≈ 1/s sustained, with a
matching burst). A value of 0 or below disables limiting.
"""

from __future__ import annotations

import os
import threading
import time

_DEFAULT_RATE_PER_MIN = 60


def default_rate_per_min() -> int:
    raw = os.environ.get("WIKI_RATE_LIMIT_PER_MIN")
    if raw is None:
        return _DEFAULT_RATE_PER_MIN
    try:
        return int(raw)
    except ValueError:
        return _DEFAULT_RATE_PER_MIN


class TokenBucketLimiter:
    """Token bucket keyed on an arbitrary identity string.

    `rate_per_min` is both the refill rate (tokens per minute) and the bucket
    capacity (burst). `clock` is injectable for deterministic tests; it
    defaults to a monotonic clock so wall-clock changes cannot grant or deny
    requests spuriously.
    """

    def __init__(self, rate_per_min: int | None = None, *, clock=time.monotonic) -> None:
        self.rate_per_min = (
            rate_per_min if rate_per_min is not None else default_rate_per_min()
        )
        self._clock = clock
        self._refill_per_sec = self.rate_per_min / 60.0
        self._capacity = float(self.rate_per_min)
        self._buckets: dict[str, tuple[float, float]] = {}  # id -> (tokens, last_ts)
        self._lock = threading.Lock()

    @property
    def enabled(self) -> bool:
        return self.rate_per_min > 0

    def allow(self, identity: str) -> bool:
        """Consume one token for `identity`. Return True if allowed, False if
        the bucket is empty (caller should respond 429)."""
        if not self.enabled:
            return True
        now = self._clock()
        with self._lock:
            tokens, last = self._buckets.get(identity, (self._capacity, now))
            # Refill for elapsed time, capped at capacity.
            tokens = min(self._capacity, tokens + (now - last) * self._refill_per_sec)
            if tokens < 1.0:
                self._buckets[identity] = (tokens, now)
                return False
            self._buckets[identity] = (tokens - 1.0, now)
            return True
