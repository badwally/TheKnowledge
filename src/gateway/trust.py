"""Server-derived trust tier (design §6, G5). Source-type default + filter score.
Agent self-report is NEVER an input — closes the buggy-agent-inflates-trust vector."""

from __future__ import annotations

_SOURCE_TYPE_DEFAULT = {
    "pubmed": 1.0, "arxiv": 0.9, "docx": 0.7, "pdf": 0.7, "web": 0.5,
    "youtube": 0.4, "note": 0.4, "voice": 0.4,
}

# Neutral trust — contributes nothing to the authority key (centered at 0.5).
NEUTRAL_TRUST = 0.5


def server_trust_tier(source_type: str, filter_score: float | None = None) -> float:
    base = _SOURCE_TYPE_DEFAULT.get(source_type, 0.5)
    if filter_score is None:
        return base
    return round(0.5 * base + 0.5 * max(0.0, min(1.0, filter_score)), 4)
