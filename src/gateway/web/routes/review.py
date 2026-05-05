"""Review console endpoints (M42)."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter

from gateway import contradictions_log
from gateway import frontmatter as fm
from gateway import paths
from gateway.filter import policy as _policy
from gateway.filter.policy import PolicyError
from gateway.web.schemas import ContradictionRecord, DraftSummary, FilterBandSource, OrphanSource


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


@router.get("/contradictions", response_model=list[ContradictionRecord])
def list_contradictions() -> list[ContradictionRecord]:
    records = contradictions_log.read_records()
    out: list[ContradictionRecord] = []
    for r in records:
        out.append(
            ContradictionRecord(
                source_id=str(r.get("source_id") or ""),
                existing_page=str(r.get("existing_page") or ""),
                existing_claim=str(r.get("existing_claim") or ""),
                new_claim=str(r.get("new_claim") or ""),
                severity=str(r.get("severity") or "moderate"),
                recorded_at=str(r.get("recorded_at") or ""),
            )
        )
    return out


@router.get("/orphans", response_model=list[OrphanSource])
def list_orphans() -> list[OrphanSource]:
    raw = paths.raw_dir()
    if not raw.exists():
        return []
    out: list[OrphanSource] = []
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            wiki_pages = front.get("wiki_pages") or []
            if isinstance(wiki_pages, list) and len(wiki_pages) > 0:
                continue
            out.append(
                OrphanSource(
                    source_id=str(front.get("id") or path.stem),
                    source_type=str(front.get("type") or source_type),
                    title=str(front.get("title") or ""),
                    ingested_at=str(front.get("ingested_at") or ""),
                    domains=list(front.get("domains") or []),
                )
            )
    # Newest first
    out.sort(key=lambda o: o.ingested_at, reverse=True)
    return out


@router.get("/filter-band", response_model=list[FilterBandSource])
def list_filter_band() -> list[FilterBandSource]:
    """Return sources with filter.score between threshold_review and threshold_include."""
    raw = paths.raw_dir()
    if not raw.exists():
        return []

    # Cache loaded policies per request
    policy_cache: dict[str, _policy.Policy | None] = {}

    def get_policy(domain: str) -> _policy.Policy | None:
        if domain not in policy_cache:
            try:
                policy_cache[domain] = _policy.load_policy(domain)
            except PolicyError:
                policy_cache[domain] = None
        return policy_cache[domain]

    out: list[FilterBandSource] = []
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            filter_block = front.get("filter") or {}
            if not isinstance(filter_block, dict):
                continue
            score = filter_block.get("score")
            if score is None:
                continue
            try:
                score_f = float(score)
            except (TypeError, ValueError):
                continue
            domains = front.get("domains") or []
            if not isinstance(domains, list):
                continue
            for domain in domains:
                policy = get_policy(str(domain))
                if policy is None:
                    continue
                if policy.threshold_review <= score_f < policy.threshold_include:
                    out.append(
                        FilterBandSource(
                            source_id=str(front.get("id") or path.stem),
                            source_type=str(front.get("type") or source_type),
                            title=str(front.get("title") or ""),
                            score=score_f,
                            threshold_review=policy.threshold_review,
                            threshold_include=policy.threshold_include,
                            domain=str(domain),
                        )
                    )
                    break  # one row per source, even if multi-domain
    out.sort(key=lambda b: b.score)  # ascending — most ambiguous first
    return out
