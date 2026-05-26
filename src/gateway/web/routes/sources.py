"""TOOL-13: /api/sources — source explorer endpoint."""

from __future__ import annotations

from fastapi import APIRouter, Query

from gateway import frontmatter as fm, paths
from gateway.web.schemas import SourceRecord


router = APIRouter(prefix="/api/sources", tags=["sources"])


def _load_sources(
    q: str = "",
    domain: str | None = None,
    source_type: str | None = None,
    limit: int = 200,
) -> list[SourceRecord]:
    raw = paths.raw_dir()
    if not raw.exists():
        return []

    q_lower = q.lower() if q else ""
    results: list[SourceRecord] = []

    for type_dir in sorted(raw.iterdir()):
        if not type_dir.is_dir():
            continue
        stype = type_dir.name
        if source_type and stype != source_type:
            continue
        for md_path in sorted(type_dir.glob("*.md"), reverse=True):
            try:
                text = md_path.read_text(errors="replace")
                front, body = fm.parse(text)
            except Exception:
                continue

            domains_val = front.get("domains") or []
            if isinstance(domains_val, str):
                domains_val = [domains_val]

            if domain and domain not in domains_val:
                continue

            title = str(front.get("title", md_path.stem))
            source_id = str(front.get("id", md_path.stem))

            if q_lower and q_lower not in title.lower() and q_lower not in source_id.lower() and q_lower not in body.lower():
                continue

            filter_block = front.get("filter") or {}
            score: float | None = None
            if isinstance(filter_block, dict):
                raw_score = filter_block.get("score")
                if raw_score is not None:
                    try:
                        score = float(raw_score)
                    except (TypeError, ValueError):
                        pass

            word_count = len(body.split())

            results.append(SourceRecord(
                source_id=source_id,
                source_type=stype,
                title=title,
                domains=list(domains_val),
                ingested_at=str(front.get("ingested_at", "")),
                filter_score=score,
                link_status=front.get("link_status") or None,
                word_count=word_count,
                draft=bool(front.get("draft", False)),
            ))

            if len(results) >= limit:
                return results

    return results


@router.get("", response_model=list[SourceRecord])
def list_sources(
    q: str = Query(default="", description="Substring search over title, ID, and body"),
    domain: str | None = Query(default=None, description="Filter by domain slug"),
    type: str | None = Query(default=None, alias="type", description="Filter by source type (web, pdf, etc.)"),
    limit: int = Query(default=200, ge=1, le=1000, description="Maximum results"),
) -> list[SourceRecord]:
    """List raw sources with optional search and domain/type filters."""
    return _load_sources(q=q, domain=domain, source_type=type, limit=limit)
