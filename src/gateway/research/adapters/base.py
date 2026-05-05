"""SearchAdapter Protocol + CandidateItem dataclass.

Every adapter follows the same contract: take a query string (and
optional filter hints derived from the research prompt + domain
policy), return a list of `CandidateItem`s. Items are merged across
adapters by URL hash, then run through the semantic filter before any
NotebookLM push.

The schema mirrors `~/code/research-notebook/src/search/`'s normalized
output so ports stay close to the originals.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class CandidateItem:
    """One source candidate emitted by an adapter.

    Fields mirror the normalized item schema research-notebook's search
    adapters produce.

    - `item_id`: stable per-adapter ID (arxiv ID, youtube video ID,
      sha1(url) for web, file path hash for local). Used for dedup
      *within* an adapter's output; cross-adapter dedup keys on `url`.
    - `source_type`: one of the registered converter source-types
      (`arxiv`, `youtube`, `pubmed`, `web`, `pdf`, `docx`, `md`, ...).
      Determines which converter materializes the item into `raw/`.
    - `url`: canonical fetch URL. For local files, `file://<absolute>`.
    - `source_metadata`: arbitrary per-adapter payload (e.g., arxiv
      categories, youtube channel/duration/views). Filter and downstream
      analysis can inspect but should not require it.
    """

    item_id: str
    source_type: str
    url: str
    title: str
    authors: list[str] = field(default_factory=list)
    publish_date: str | None = None  # ISO-8601 date or None if unknown
    description: str = ""
    content_type: str = ""           # adapter-specific (e.g., "preprint", "video", "article", "pdf")
    source_metadata: dict = field(default_factory=dict)


class SearchAdapter(Protocol):
    """Protocol every adapter implements.

    Adapters MUST be safe to instantiate without their backing API
    being available; failure to authenticate / fetch should surface
    only when `search()` is called, and should raise a typed exception
    the orchestrator can downgrade to a per-adapter warning without
    aborting the whole research run.
    """

    name: str
    """Stable short name used in logs / config (e.g., 'arxiv', 'youtube')."""

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int = 50,
    ) -> list[CandidateItem]: ...


class AdapterError(RuntimeError):
    """Raised when an adapter's search call fails irrecoverably.

    Orchestrator catches per-adapter and continues the run with a logged
    warning rather than aborting (one missing API key shouldn't kill a
    whole research session).
    """
