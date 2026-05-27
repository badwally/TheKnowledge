"""TOOL-8: /today daily triage endpoint."""

from __future__ import annotations

from fastapi import APIRouter, Query

from gateway.ops.daily_review import run_daily_review
from gateway.web.schemas import (
    DailyReviewResponse,
    DraftItemResponse,
    IngestedSourceResponse,
    OrphanSourceResponse,
)


router = APIRouter(tags=["daily"])


@router.get("/today", response_model=DailyReviewResponse)
def get_today(
    lookback_hours: float = Query(24.0, ge=1, le=168),
    stale_days: int = Query(7, ge=1, le=90),
    orphan_limit: int = Query(30, ge=1, le=200),
) -> DailyReviewResponse:
    result = run_daily_review(
        lookback_hours=lookback_hours,
        stale_days=stale_days,
        orphan_limit=orphan_limit,
    )
    return DailyReviewResponse(
        as_of=result.as_of,
        inbox_count=result.inbox_count,
        inbox_failed=result.inbox_failed,
        triage_queue_depth=result.triage_queue_depth,
        recently_ingested=[
            IngestedSourceResponse(
                source_id=i.source_id,
                title=i.title,
                source_type=i.source_type,
                domains=i.domains,
                ingested_at=i.ingested_at,
            )
            for i in result.recently_ingested
        ],
        stale_drafts=[
            DraftItemResponse(
                slug=d.slug,
                title=d.title,
                age_days=d.age_days,
                wiki_path=d.wiki_path,
            )
            for d in result.stale_drafts
        ],
        orphan_sources=[
            OrphanSourceResponse(
                source_id=o.source_id,
                title=o.title,
                source_type=o.source_type,
                ingested_at=o.ingested_at,
            )
            for o in result.orphan_sources
        ],
    )
