"""AGT-4: contradiction sweeper — weekly per-domain LLM contradiction scan.

Runs the same LLM-based contradiction detection as lint/contradictions but
on a schedule, writing results as draft synthesis pages for review.

Output: wiki/synthesis/contradictions-<domain>-<week>.md (draft: true)
Idempotency: page already exists for this domain+week → skip.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter.semantic import ClaudeCLIFilterClient, FilterClient
from gateway.lint.contradictions import (
    LintFinding,
    _Claim,  # noqa: PLC2701 — shared implementation detail with lint/contradictions
    _MAX_CLAIMS_PER_CALL,
    _MIN_CLAIMS_PER_DOMAIN,
    _build_prompt,
    _chunked,
    _findings_for_pairs,
    _gather_claims_by_domain,
    _parse_response,
)
from gateway.locking import file_lock


_LOCK_NAME = "wiki-author"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _week_str() -> str:
    now = datetime.now(timezone.utc)
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


def _page_path(domain: str, week: str) -> Path:
    slug = f"contradictions-{domain}-{week}"
    return paths.wiki_dir() / "synthesis" / f"{slug}.md"


def _blessed_domains() -> list[str]:
    pd = paths.policies_dir()
    if not pd.exists():
        return []
    return sorted(p.parent.name for p in pd.glob("*/policy.yaml"))


def _build_page(domain: str, week: str, findings: list[LintFinding]) -> str:
    slug = f"contradictions-{domain}-{week}"
    now = _now_iso()

    referenced_pages: set[str] = set()
    for f in findings:
        for key in ("a_page", "b_page"):
            p = f.metadata.get(key, "")
            if p:
                referenced_pages.add(p)

    front = {
        "type": "synthesis",
        "slug": slug,
        "title": f"Contradictions in {domain} — {week}",
        "domains": [domain],
        "question": f"What are the contradictory claims in the {domain} domain for {week}?",
        "created_at": now,
        "last_updated": now,
        "sources_count": len(referenced_pages),
        "synthesizes": [],
        "draft": True,
        "generated_by": "contradiction-sweeper",
    }

    pair_lines: list[str] = []
    for f in findings:
        a_page = f.metadata.get("a_page", "")
        b_page = f.metadata.get("b_page", "")
        a_text = f.metadata.get("a_text", "")
        b_text = f.metadata.get("b_text", "")
        rationale = f.metadata.get("rationale", "")
        pair_lines += [
            f"- **[[{a_page}]]**: {a_text}",
            f"  vs **[[{b_page}]]**: {b_text}",
        ]
        if rationale:
            pair_lines.append(f"  _{rationale}_")
        pair_lines.append("")

    source_links = [f"- [[{p}]]" for p in sorted(referenced_pages)]

    body = "\n".join([
        "## Synthesis",
        "",
        f"Auto-generated contradiction scan for `{domain}`, week {week}.",
        f"{len(findings)} potential contradiction pair(s). Review and resolve via `wiki contradiction`.",
        "",
        *pair_lines,
        "## Sources cited",
        "",
        *source_links,
        "",
    ])
    return fm.serialize(front, body)


def sweep_domain(
    domain: str,
    *,
    client: FilterClient | None = None,
    week: str | None = None,
) -> OperationResult:
    """Sweep one domain for contradictions and write a draft synthesis page."""
    if client is None:
        client = ClaudeCLIFilterClient()
    if week is None:
        week = _week_str()

    out_path = _page_path(domain, week)
    if out_path.exists():
        return OperationResult(
            success=True,
            summary=f"contradiction-sweeper: {domain}/{week} already exists, skipped",
        )

    by_domain = _gather_claims_by_domain()
    claims = by_domain.get(domain, [])
    if len(claims) < _MIN_CLAIMS_PER_DOMAIN:
        return OperationResult(
            success=True,
            summary=f"contradiction-sweeper: {domain} has fewer than {_MIN_CLAIMS_PER_DOMAIN} claims, skipped",
        )

    all_findings: list[LintFinding] = []
    for chunk in _chunked(claims, _MAX_CLAIMS_PER_CALL):
        prompt = _build_prompt(domain, chunk)
        try:
            response = client.call(prompt)
        except Exception as e:
            return OperationResult(
                success=False,
                errors=[f"LLM call failed for {domain}: {e!r}"],
                summary=f"contradiction-sweeper: {domain} — LLM error",
            )
        pairs = _parse_response(response)
        all_findings.extend(_findings_for_pairs(domain, chunk, pairs))

    if not all_findings:
        return OperationResult(
            success=True,
            summary=f"contradiction-sweeper: {domain}/{week} — no contradictions found",
        )

    page = _build_page(domain, week, all_findings)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with file_lock(_LOCK_NAME):
        write_atomic(out_path, page)
        log.append(
            op="contradiction-sweeper",
            fields={"domain": domain, "week": week, "pairs": len(all_findings)},
            summary=f"wrote {out_path.name}",
        )

    return OperationResult(
        success=True,
        paths_touched=[out_path, paths.log_path()],
        summary=(
            f"contradiction-sweeper: {domain}/{week} — "
            f"{len(all_findings)} pair(s) → {out_path.name}"
        ),
    )


def run_contradiction_sweep(
    domain: str | None = None,
    *,
    client: FilterClient | None = None,
    week: str | None = None,
) -> OperationResult:
    """Sweep all blessed domains (or one specific domain) for contradictions."""
    if domain is not None:
        return sweep_domain(domain, client=client, week=week)

    domains = _blessed_domains()
    if not domains:
        return OperationResult(success=True, summary="contradiction-sweeper: no blessed domains")

    ran: list[str] = []
    skipped: list[str] = []
    errors: list[str] = []

    for d in domains:
        result = sweep_domain(d, client=client, week=week)
        if not result.success:
            errors.extend(result.errors or [f"{d}: sweep failed"])
        elif any(
            word in result.summary
            for word in ("already exists", "no contradictions", "fewer than")
        ):
            skipped.append(d)
        else:
            ran.append(d)

    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"contradiction-sweeper: {len(ran)} swept, "
            f"{len(skipped)} skipped, {len(errors)} errors"
        ),
    )
