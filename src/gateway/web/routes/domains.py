"""Domain endpoints: list domains, list proposals, promote/demote/reject."""

from __future__ import annotations

import yaml
from fastapi import APIRouter, HTTPException

from gateway import frontmatter as fm
from gateway import nlm_registry, paths
from gateway.ops.demote_domain import demote_domain
from gateway.ops.promote_domain import promote_domain
from gateway.ops.reject_proposal import reject_proposal
from gateway.web.schemas import (
    DomainSummary,
    OperationResultResponse,
    ProposalSummary,
)


router = APIRouter(prefix="/api", tags=["domains"])


@router.get("/domains", response_model=list[DomainSummary])
def list_domains() -> list[DomainSummary]:
    out: list[DomainSummary] = []
    policies_dir = paths.policies_dir()
    if not policies_dir.exists():
        return out
    for d in sorted(policies_dir.iterdir()):
        if not d.is_dir():
            continue
        policy_yaml = d / "policy.yaml"
        if not policy_yaml.exists():
            continue
        try:
            data = yaml.safe_load(policy_yaml.read_text()) or {}
        except yaml.YAMLError:
            continue
        slug = (data.get("domain") or {}).get("slug", d.name)
        topic = (data.get("domain") or {}).get("topic", "")
        out.append(
            DomainSummary(
                slug=slug,
                topic=topic,
                sources_count=_count_domain_sources(slug),
                has_notebook=nlm_registry.get_persistent(slug) is not None,
            )
        )
    return out


@router.get("/proposals", response_model=list[ProposalSummary])
def list_proposals() -> list[ProposalSummary]:
    out: list[ProposalSummary] = []
    prop_dir = paths.wiki_dir() / "proposals"
    if not prop_dir.exists():
        return out
    for path in sorted(prop_dir.glob("*.md")):
        try:
            front, _ = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        out.append(
            ProposalSummary(
                slug=str(front.get("slug") or path.stem),
                title=str(front.get("title") or ""),
                proposed_domain=str(front.get("proposed_domain") or ""),
                status=str(front.get("status") or ""),
                member_sources_count=len(front.get("member_sources") or []),
            )
        )
    return out


@router.post("/domains/{slug}/promote", response_model=OperationResultResponse)
def post_promote(slug: str) -> OperationResultResponse:
    result = promote_domain(slug)
    return _to_response(result)


@router.post("/domains/{slug}/demote", response_model=OperationResultResponse)
def post_demote(slug: str) -> OperationResultResponse:
    result = demote_domain(slug)
    return _to_response(result)


@router.post("/domains/{slug}/reject", response_model=OperationResultResponse)
def post_reject(slug: str) -> OperationResultResponse:
    result = reject_proposal(slug)
    return _to_response(result)


def _to_response(result) -> OperationResultResponse:
    if not result.success:
        raise HTTPException(
            status_code=400,
            detail={
                "summary": result.summary,
                "errors": result.errors,
                "warnings": result.warnings,
            },
        )
    return OperationResultResponse(
        success=result.success,
        summary=result.summary,
        paths_touched=[str(p) for p in result.paths_touched],
        warnings=result.warnings,
        errors=result.errors,
        no_op=result.no_op,
        authorship_report=_serialize_authorship_report(
            getattr(result, "authorship_report", None)
        ),
    )


def _serialize_authorship_report(report) -> dict | None:
    if report is None:
        return None
    return {
        "pages_created": list(report.pages_created),
        "pages_updated": list(report.pages_updated),
        "contradictions": [
            {
                "existing_page": c.existing_page,
                "existing_claim": c.existing_claim,
                "new_claim": c.new_claim,
                "source_id": c.source_id,
                "severity": c.severity,
            }
            for c in report.contradictions
        ],
    }


def _count_domain_sources(slug: str) -> int:
    raw = paths.raw_dir()
    if not raw.exists():
        return 0
    count = 0
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            try:
                front, _ = fm.parse(path.read_text())
                if slug in (front.get("domains") or []):
                    count += 1
            except (fm.FrontmatterError, OSError):
                continue
    return count
