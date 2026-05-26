"""TOOL-12: daily-domain-digest — poll-triage-synthesize loop.

Finds sources ingested in the last LOOKBACK_HOURS for a domain, builds a
summary with an LLM call, and writes a draft synthesis page at
wiki/synthesis/daily-<domain>-<YYYY-MM-DD>.md.

Idempotency: if today's page already exists, returns a no-op result.
Threshold: if fewer than MIN_NEW_SOURCES new sources found, skips.

Output page is always draft: true (requires `wiki finalize` to promote).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter.semantic import ClaudeCLIFilterClient, FilterClient
from gateway.locking import file_lock


_MIN_NEW_SOURCES = 1
_LOOKBACK_HOURS = 24
_MAX_BODY_CHARS = 800
_MAX_SOURCES_IN_PROMPT = 10
_LOCK_NAME = "wiki-author"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _page_path(domain: str, date_str: str) -> Path:
    slug = f"daily-{domain}-{date_str}"
    return paths.wiki_dir() / "synthesis" / f"{slug}.md"


def _cutoff_iso(hours: int) -> str:
    dt = datetime.now(timezone.utc) - timedelta(hours=hours)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _is_after(iso_str: str, cutoff: str) -> bool:
    try:
        a = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        b = datetime.fromisoformat(cutoff.replace("Z", "+00:00"))
        return a >= b
    except Exception:
        return False


def _find_new_sources(domain: str, cutoff: str) -> list[dict[str, Any]]:
    """Return metadata dicts for sources tagged to domain ingested after cutoff."""
    raw = paths.raw_dir()
    if not raw.exists():
        return []
    results = []
    for type_dir in sorted(raw.iterdir()):
        if not type_dir.is_dir():
            continue
        for md_path in sorted(type_dir.glob("*.md")):
            try:
                front, body = fm.parse(md_path.read_text(errors="replace"))
            except Exception:
                continue
            domains_val = front.get("domains") or []
            if isinstance(domains_val, str):
                domains_val = [domains_val]
            if domain not in domains_val:
                continue
            ingested_at = str(front.get("ingested_at", ""))
            if not ingested_at or not _is_after(ingested_at, cutoff):
                continue
            results.append({
                "id": str(front.get("id", md_path.stem)),
                "title": str(front.get("title", md_path.stem)),
                "body": body[:_MAX_BODY_CHARS],
            })
    return results


def _build_prompt(domain: str, sources: list[dict[str, Any]]) -> str:
    lines = [
        f"You are synthesizing new knowledge for the '{domain}' research domain.",
        f"The following {len(sources)} source(s) were ingested in the last 24 hours.",
        "Write a concise daily digest (200–400 words) summarizing the key findings,",
        "new entities or concepts introduced, and any notable patterns across sources.",
        "Use plain prose. Be specific and reference source IDs in parentheses.",
        "",
    ]
    for src in sources[:_MAX_SOURCES_IN_PROMPT]:
        lines.append(f"=== [{src['id']}] {src['title']} ===")
        lines.append(src["body"].strip())
        lines.append("")
    return "\n".join(lines)


def _build_page(domain: str, date_str: str, source_ids: list[str], summary_text: str) -> str:
    slug = f"daily-{domain}-{date_str}"
    front: dict[str, Any] = {
        "type": "synthesis",
        "slug": slug,
        "title": f"Daily digest: {domain} ({date_str})",
        "domains": [domain],
        "draft": True,
        "created_at": _now_iso(),
        "last_updated": _now_iso(),
        "synthesizes": [f"sources/{sid}" for sid in source_ids],
    }
    included = "".join(f"- [[sources/{sid}]]\n" for sid in source_ids)
    body = f"## Summary\n\n{summary_text.strip()}\n\n## Included works\n\n{included}"
    return fm.serialize(front, body)


def run_daily_domain_digest(
    domain: str,
    *,
    client: FilterClient | None = None,
    date_str: str | None = None,
    lookback_hours: int = _LOOKBACK_HOURS,
) -> OperationResult:
    """Find new sources for domain, summarize with LLM, write draft synthesis page."""
    if client is None:
        client = ClaudeCLIFilterClient()
    if date_str is None:
        date_str = _today_str()

    out_path = _page_path(domain, date_str)
    if out_path.exists():
        return OperationResult(
            success=True,
            summary=f"daily-digest: {domain}/{date_str} already exists, skipped",
            data={"skipped": True, "reason": "already_exists"},
        )

    cutoff = _cutoff_iso(lookback_hours)
    sources = _find_new_sources(domain, cutoff)

    if len(sources) < _MIN_NEW_SOURCES:
        return OperationResult(
            success=True,
            summary=f"daily-digest: {domain}/{date_str} — {len(sources)} new sources (< {_MIN_NEW_SOURCES}), skipped",
            data={"skipped": True, "reason": "insufficient_sources", "found": len(sources)},
        )

    prompt = _build_prompt(domain, sources)
    try:
        summary_text = client.call(prompt)
    except Exception as exc:
        return OperationResult(
            success=False,
            summary=f"daily-digest: LLM call failed — {exc}",
        )

    source_ids = [s["id"] for s in sources[:_MAX_SOURCES_IN_PROMPT]]
    page_content = _build_page(domain, date_str, source_ids, summary_text)

    with file_lock(_LOCK_NAME):
        out_path.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(out_path, page_content)

    log.append(
        op="daily-digest",
        fields={"domain": domain, "date": date_str, "sources": len(sources)},
        summary=f"daily-digest: {domain}/{date_str} — {len(sources)} sources → {out_path.name}",
    )

    return OperationResult(
        success=True,
        summary=f"daily-digest: {domain}/{date_str} written ({len(sources)} sources)",
        data={"domain": domain, "date": date_str, "sources": len(sources), "slug": out_path.stem},
    )


def run_all_domains(
    *,
    client: FilterClient | None = None,
    date_str: str | None = None,
    lookback_hours: int = _LOOKBACK_HOURS,
) -> OperationResult:
    """Run daily-domain-digest for all domains with a policy.yaml."""
    pd = paths.policies_dir()
    domains = sorted(p.parent.name for p in pd.glob("*/policy.yaml")) if pd.exists() else []

    results = []
    errors: list[str] = []
    for domain in domains:
        r = run_daily_domain_digest(
            domain, client=client, date_str=date_str, lookback_hours=lookback_hours
        )
        results.append(r)
        if not r.success:
            errors.append(f"{domain}: {r.summary}")

    written = sum(1 for r in results if r.success and not r.data.get("skipped"))
    skipped = sum(1 for r in results if r.data.get("skipped"))

    return OperationResult(
        success=len(errors) == 0,
        summary=(
            f"daily-digest: {written} written, {skipped} skipped, "
            f"{len(errors)} errors across {len(domains)} domains"
        ),
        data={"domains": len(domains), "written": written, "skipped": skipped, "errors": errors},
    )
