"""Search adapters for `wiki research`.

Each adapter implements the `SearchAdapter` Protocol from `base.py` and
returns a list of normalized `CandidateItem`s for a given query. New
sources slot in by adding a module here and registering it in
`enabled_adapters()`.

Adapters in v1: arxiv, youtube, web (Firecrawl), pubmed, local.
Future: substack-via-gmail, apple_notes, notion, slack.
"""

from __future__ import annotations

import sys

from gateway.research.adapters.base import CandidateItem, SearchAdapter


__all__ = ["CandidateItem", "SearchAdapter", "enabled_adapters"]


def enabled_adapters(
    *,
    include_local: list[str] | None = None,
) -> list[SearchAdapter]:
    """Return adapter instances enabled for this run.

    `include_local` is a list of paths/globs supplied via the orchestrator's
    `--include-local` flag (repeatable). When non-empty, the local-files
    adapter is enabled with those paths as its discovery roots.

    Other adapters are enabled unconditionally in v1; configuration via
    `wikiloom.toml`-style switches comes later. Each adapter is responsible
    for skipping itself gracefully when its required credentials/keys are
    missing (e.g., YouTube without `YOUTUBE_API_KEY`).

    Adapters are imported lazily and individually so the registry stays
    usable while sibling adapters (arxiv/youtube/web) are still landing
    in parallel branches. A missing module is logged to stderr and
    skipped rather than aborting the whole research run.
    """
    adapters: list[SearchAdapter] = []

    _network_specs: list[tuple[str, str, str]] = [
        ("arxiv", "gateway.research.adapters.arxiv", "ArxivAdapter"),
        ("youtube", "gateway.research.adapters.youtube", "YouTubeAdapter"),
        ("web", "gateway.research.adapters.web", "WebAdapter"),
        ("pubmed", "gateway.research.adapters.pubmed", "PubMedAdapter"),
    ]

    for name, module_path, class_name in _network_specs:
        try:
            module = __import__(module_path, fromlist=[class_name])
            adapter_cls = getattr(module, class_name)
        except ImportError as e:
            print(
                f"[research.adapters] skipping {name}: ImportError ({e})",
                file=sys.stderr,
            )
            continue
        except AttributeError as e:
            print(
                f"[research.adapters] skipping {name}: missing class "
                f"{class_name} ({e})",
                file=sys.stderr,
            )
            continue
        adapters.append(adapter_cls())

    if include_local:
        try:
            from gateway.research.adapters.local import LocalAdapter
        except ImportError as e:
            print(
                f"[research.adapters] skipping local: ImportError ({e})",
                file=sys.stderr,
            )
        else:
            adapters.append(LocalAdapter(paths=list(include_local)))

    return adapters
