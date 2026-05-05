"""Poller registry. API-only sources land items in `raw/<type>/` for the
watcher / `wiki ingest` to pick up. Pollers are invoked manually
(`wiki poll <name>`) or scheduled via launchd / cron.
"""

from __future__ import annotations

from gateway.pollers.apple_notes import AppleNotesPoller
from gateway.pollers.base import Poller, PollerResult


_REGISTRY: dict[str, type[Poller]] = {
    AppleNotesPoller.name: AppleNotesPoller,
}


class UnknownPollerError(LookupError):
    """Raised when no poller is registered under the requested name."""


def get_poller(name: str) -> Poller:
    """Instantiate the poller registered under `name`. Raises if unknown."""
    cls = _REGISTRY.get(name)
    if cls is None:
        raise UnknownPollerError(
            f"no poller named {name!r}; registered: {sorted(_REGISTRY)}"
        )
    return cls()


def list_pollers() -> list[str]:
    """Return registered poller names, sorted."""
    return sorted(_REGISTRY)


__all__ = [
    "Poller",
    "PollerResult",
    "UnknownPollerError",
    "get_poller",
    "list_pollers",
]
