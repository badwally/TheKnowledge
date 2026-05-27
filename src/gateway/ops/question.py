"""`wiki question new` + `wiki question list` — question page management (TOOL-16, M95)."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic
from gateway.lint._walk import walk_wiki_pages

__all__ = ["question_new", "question_list"]

_SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def question_new(
    slug: str,
    title: str,
    domain: str,
    status: str = "open",
) -> OperationResult:
    """Create a new question page at wiki/questions/<slug>.md."""
    if not _SLUG_RE.match(slug):
        return OperationResult(
            success=False,
            errors=[f"invalid slug {slug!r}: must be lowercase alphanumeric + hyphens"],
        )
    if status not in ("open", "partial", "answered"):
        return OperationResult(
            success=False,
            errors=[f"invalid status {status!r}: must be open, partial, or answered"],
        )

    target = paths.knowledge_root() / "wiki" / "questions" / f"{slug}.md"
    if target.exists():
        return OperationResult(
            success=False,
            errors=[f"question page already exists: wiki/questions/{slug}.md"],
        )

    now = _now_iso()
    front: dict[str, Any] = {
        "type": "question",
        "slug": slug,
        "title": title,
        "domains": [domain],
        "status": status,
        "created_at": now,
        "last_updated": now,
    }

    body = (
        f"# {title}\n"
        "\n"
        "## Question\n"
        "\n"
        "<!-- State the research question precisely. -->\n"
        "\n"
        "## Context\n"
        "\n"
        "<!-- Why this question matters; what is already known. -->\n"
    )

    target.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(target, fm.serialize(front, body))

    rel = f"wiki/questions/{slug}.md"
    log.append(
        "question-new",
        fields={"slug": slug, "domain": domain, "status": status},
        summary=f"created question page: {rel}",
    )

    return OperationResult(
        success=True,
        summary=f"Created {rel}",
        data={"path": rel, "slug": slug},
    )


def question_list(
    *,
    domain: str | None = None,
    status: str | None = None,
) -> list[dict[str, Any]]:
    """Return a list of question page metadata dicts, optionally filtered."""
    results = []
    for page_type, path, front, _body in walk_wiki_pages():
        if page_type != "question":
            continue
        if domain is not None:
            doms = front.get("domains") or []
            if domain not in doms:
                continue
        q_status = front.get("status", "open")
        if status is not None and q_status != status:
            continue
        results.append(
            {
                "slug": front.get("slug", path.stem),
                "title": front.get("title", ""),
                "status": q_status,
                "domains": front.get("domains") or [],
                "last_updated": front.get("last_updated", ""),
                "path": str(path.relative_to(paths.knowledge_root())),
            }
        )
    results.sort(key=lambda r: (r["status"], r["last_updated"]))
    return results
