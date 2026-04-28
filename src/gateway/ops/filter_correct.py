"""`wiki filter-correct <source-id>` — override a past filter decision.

Updates the source frontmatter's `filter.user_correction` block and pins
the corrected example to the bank with `pinned_by: user-correction`. The
next filter call sees this example as a high-signal calibration input.
"""

from __future__ import annotations

from datetime import datetime, timezone

from gateway import frontmatter as fm
from gateway import log, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter import pin
from gateway.locking import file_lock


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _find_source(source_id: str):
    """Locate raw/<type>/<source_id>.md by trying every known type."""
    for source_type in paths.SOURCE_TYPES:
        candidate = paths.raw_source_path(source_type, source_id)
        if candidate.exists():
            return source_type, candidate
    return None, None


def filter_correct(
    source_id: str,
    *,
    decision: str,
    rationale: str,
    domain: str | None = None,
) -> OperationResult:
    """Apply a user correction to a source's filter decision."""
    if decision not in ("include", "exclude"):
        return OperationResult(
            success=False,
            errors=[f"decision must be 'include' or 'exclude', got {decision!r}"],
        )

    source_type, raw_path = _find_source(source_id)
    if raw_path is None:
        return OperationResult(
            success=False,
            errors=[f"no raw source found with id {source_id!r}"],
        )

    text = raw_path.read_text()
    try:
        front, body = fm.parse(text)
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    effective_domain = domain or (front.get("domains") or [None])[0]
    if not effective_domain:
        return OperationResult(
            success=False,
            errors=["source has no domains; pass --domain <slug> to specify"],
        )

    corrected_score = 1.0 if decision == "include" else 0.0
    correction_block = {
        "decided_at": _now_iso(),
        "score": corrected_score,
        "rationale": rationale,
    }

    with file_lock(f"ingest-{source_id}"):
        existing_filter = front.get("filter") if isinstance(front.get("filter"), dict) else {}
        new_filter = dict(existing_filter)
        new_filter["user_correction"] = correction_block
        front["filter"] = new_filter

        write_atomic(raw_path, fm.serialize(front, body))

        policy_version = (
            existing_filter.get("policy_version")
            or f"{effective_domain}-v1"
        )
        pin(
            source_id=source_id,
            domain=effective_domain,
            decision=decision,
            score=corrected_score,
            policy_version=str(policy_version),
            rationale=rationale,
            pinned_by="user-correction",
            frontmatter_snapshot={
                "type": front.get("type"),
                "title": front.get("title"),
                "authors": front.get("authors", []),
                "url": front.get("url"),
            },
            content_excerpt=body[:500],
        )

        log.append(
            op="filter-correction",
            fields={
                "id": source_id,
                "domain": effective_domain,
                "decision": decision,
                "original_score": existing_filter.get("score", "?"),
            },
            summary=f"rationale={rationale!r}",
        )

    return OperationResult(
        success=True,
        paths_touched=[raw_path],
        summary=f"corrected: {source_id} → {decision}",
    )
