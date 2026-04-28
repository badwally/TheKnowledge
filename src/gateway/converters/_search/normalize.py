"""Shared normalization utilities for source adapters."""

_SOURCE_PREFIXES = {
    "youtube": "yt",
    "arxiv": "arxiv",
    "pubmed": "pmid",
    "semantic_scholar": "s2",
}


def make_item_id(source_type: str, raw_id: str) -> str:
    if source_type not in _SOURCE_PREFIXES:
        raise ValueError(f"Unknown source type: {source_type!r}")
    return f"{_SOURCE_PREFIXES[source_type]}:{raw_id}"


def truncate_description(text: str, max_length: int = 500) -> str:
    if text is None:
        return ""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def deduplicate_items(items: list[dict]) -> list[dict]:
    seen = set()
    result = []
    for item in items:
        item_id = item.get("item_id")
        if item_id is None:
            result.append(item)
        elif item_id not in seen:
            seen.add(item_id)
            result.append(item)
    return result


def empty_scores() -> dict:
    return {"relevance_score": 0, "inclusion_rationale": "", "included": False}
