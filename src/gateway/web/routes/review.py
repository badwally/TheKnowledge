"""Review console endpoints (M42)."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter

from gateway import frontmatter as fm
from gateway import paths
from gateway.web.schemas import DraftSummary


router = APIRouter(prefix="/api/review", tags=["review"])


_DRAFT_TYPE_DIRS = ("entities", "concepts", "synthesis", "mocs")


@router.get("/drafts", response_model=list[DraftSummary])
def list_drafts() -> list[DraftSummary]:
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return []
    out: list[DraftSummary] = []
    now = datetime.now(timezone.utc)
    for type_dir in _DRAFT_TYPE_DIRS:
        d = wiki / type_dir
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            if not front.get("draft"):
                continue
            started = str(front.get("draft_started_at") or "")
            try:
                started_dt = datetime.fromisoformat(started.replace("Z", "+00:00"))
                age_days = (now - started_dt).total_seconds() / 86400
            except (ValueError, TypeError):
                age_days = 0.0
            out.append(
                DraftSummary(
                    path=str(path.relative_to(paths.knowledge_root())),
                    type=str(front.get("type") or type_dir.rstrip("s")),
                    slug=str(front.get("slug") or path.stem),
                    draft_started_at=started,
                    draft_unresolved_claims=int(front.get("draft_unresolved_claims") or 0),
                    age_days=round(age_days, 1),
                )
            )
    # Oldest first (largest age_days first)
    out.sort(key=lambda d: d.age_days, reverse=True)
    return out
