"""NLM artifact endpoints (M43)."""

from __future__ import annotations

from fastapi import APIRouter

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.nlm import nlm_add
from gateway.web.routes.domains import _to_response
from gateway.web.schemas import (
    ArtifactSummary,
    NlmAddRequest,
    OperationResultResponse,
)


router = APIRouter(prefix="/api/nlm", tags=["nlm"])


_ARTIFACT_DIRS = ("briefing", "audio", "slides")


@router.post("/domains/{slug}/add", response_model=OperationResultResponse)
def post_nlm_add(slug: str, req: NlmAddRequest) -> OperationResultResponse:
    """Synchronous: add a single source to the domain's NotebookLM corpus."""
    result = nlm_add(slug, req.source_id)
    return _to_response(result)


@router.get("/domains/{slug}/artifacts", response_model=list[ArtifactSummary])
def list_artifacts(slug: str) -> list[ArtifactSummary]:
    """List wiki/artifacts/* pages where frontmatter domain == slug."""
    artifacts_dir = paths.wiki_dir() / "artifacts"
    if not artifacts_dir.exists():
        return []
    out: list[ArtifactSummary] = []
    for type_dir in _ARTIFACT_DIRS:
        d = artifacts_dir / type_dir
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(path.read_text())
            except (fm.FrontmatterError, OSError):
                continue
            if str(front.get("domain") or "") != slug:
                continue
            out.append(
                ArtifactSummary(
                    slug=str(front.get("slug") or path.stem),
                    type=str(front.get("artifact_type") or type_dir),
                    title=str(front.get("title") or ""),
                    domain=str(front.get("domain") or ""),
                    created_at=str(front.get("created_at") or ""),
                    nlm_artifact_url=front.get("nlm_artifact_url"),
                )
            )
    out.sort(key=lambda a: a.created_at, reverse=True)
    return out
