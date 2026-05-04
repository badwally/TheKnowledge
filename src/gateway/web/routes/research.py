"""Research orchestration endpoints (M41)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import yaml
from fastapi import APIRouter

from gateway import nlm_registry, paths
from gateway.web.schemas import ResearchSessionSummary


router = APIRouter(prefix="/api/research", tags=["research"])


_SLACK_SECONDS = 2.0


@router.get("/sessions", response_model=list[ResearchSessionSummary])
def list_sessions() -> list[ResearchSessionSummary]:
    plans_dir = paths.knowledge_root() / "nlm" / "query_plans"
    if not plans_dir.is_dir():
        return []

    out: list[ResearchSessionSummary] = []
    for path in plans_dir.glob("*.yaml"):
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict):
            continue
        session_id = str(data.get("session_id") or path.stem)
        domain = str(data.get("domain") or "")
        prompt = str(data.get("prompt") or "")
        generated_at = str(data.get("generated_at") or "")

        queries = data.get("queries") or {}
        if isinstance(queries, dict):
            query_count = sum(len(v or []) for v in queries.values() if isinstance(v, list))
        else:
            query_count = 0

        edited = _is_edited(path, generated_at)
        state = _derive_state(domain, session_id, edited)

        out.append(
            ResearchSessionSummary(
                session_id=session_id,
                prompt=prompt,
                domain=domain,
                state=state,
                generated_at=generated_at,
                edited=edited,
                query_count=query_count,
                sources_count=_sources_count(domain, session_id),
            )
        )

    out.sort(key=lambda s: s.generated_at, reverse=True)
    return out


def _is_edited(path: Path, generated_at: str) -> bool:
    """YAML mtime > generated_at + 2s slack."""
    if not generated_at:
        return False
    try:
        gen_dt = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    try:
        mtime_ts = path.stat().st_mtime
    except OSError:
        return False
    return mtime_ts > gen_dt.timestamp() + _SLACK_SECONDS


def _derive_state(domain: str, session_id: str, edited: bool) -> str:
    """Compute lifecycle state from registry + edit flag.

    Returns one of: plan_only | edited | done | abandoned.
    'running' detection is left to the frontend (via task_id polling on
    create/execute responses) — this helper does not look into TaskStore.
    """
    if not domain or not session_id:
        return "edited" if edited else "plan_only"
    sess = nlm_registry.get_session(domain, session_id)
    if sess is None:
        return "edited" if edited else "plan_only"
    status = sess.get("status") if isinstance(sess, dict) else None
    if status == nlm_registry.PROMOTED:
        return "done"
    if status == nlm_registry.ABANDONED:
        return "abandoned"
    return "edited" if edited else "plan_only"


def _sources_count(domain: str, session_id: str) -> int | None:
    if not domain or not session_id:
        return None
    sess = nlm_registry.get_session(domain, session_id)
    if not isinstance(sess, dict):
        return None
    val = sess.get("sources_count")
    if val is None:
        return None
    try:
        return int(val)
    except (TypeError, ValueError):
        return None
