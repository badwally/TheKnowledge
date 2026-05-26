"""Poller registry. API-only sources land items in `raw/<type>/` for the
watcher / `wiki ingest` to pick up. Pollers are invoked manually
(`wiki poll <name>`) or scheduled via launchd / cron.
"""

from __future__ import annotations

from gateway.pollers.apple_notes import AppleNotesPoller
from gateway.pollers.arxiv_revisions import ArxivRevisionPoller
from gateway.pollers.base import Poller, PollerResult
from gateway.pollers.gmail_newsletters import GmailNewsletterPoller
from gateway.pollers.link_rot import LinkRotPoller
from gateway.pollers.pubmed_retractions import PubmedRetractionPoller
from gateway.pollers.readwise import ReadwisePoller
from gateway.pollers.repo_metadata import RepoMetadataPoller
from gateway.pollers.rss import RSSPoller


_REGISTRY: dict[str, type[Poller]] = {
    AppleNotesPoller.name: AppleNotesPoller,
    ArxivRevisionPoller.name: ArxivRevisionPoller,
    GmailNewsletterPoller.name: GmailNewsletterPoller,
    LinkRotPoller.name: LinkRotPoller,
    PubmedRetractionPoller.name: PubmedRetractionPoller,
    ReadwisePoller.name: ReadwisePoller,
    RepoMetadataPoller.name: RepoMetadataPoller,
    RSSPoller.name: RSSPoller,
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
