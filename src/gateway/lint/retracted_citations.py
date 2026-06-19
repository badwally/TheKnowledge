"""QUAL-7: retracted-citations lint check.

Any wiki page that cites a source marked `retracted: true` in its raw
frontmatter must be reviewed and updated. Retracted sources may contain
invalidated claims; citing them propagates the error.

Severity: ERROR — a retracted source citation is a factual integrity risk.

Scope: all wiki pages (synthesis, sources, concepts, entities, mocs,
       artifacts, proposals).
"""

from __future__ import annotations

from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.citations import find_wikilinks
from gateway.lint import LintFinding, SEVERITY_ERROR, SEVERITY_WARNING


def _collect_retracted_ids() -> frozenset[str]:
    """Walk raw/ directories and collect source IDs with retracted: true."""
    retracted: set[str] = set()
    raw = paths.raw_dir()
    for source_type in ("pubmed", "arxiv"):
        d = raw / source_type
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            if front.get("retracted"):
                sid = front.get("id", p.stem)
                retracted.add(sid)
    return frozenset(retracted)


def run() -> list[LintFinding]:
    retracted_ids = _collect_retracted_ids()
    if not retracted_ids:
        return []

    wiki = paths.wiki_dir()
    if not wiki.exists():
        return []

    findings: list[LintFinding] = []
    # Track which pages were already flagged as direct-cite (depth=1) to avoid
    # emitting a duplicate cascade finding for the same page.
    direct_flagged: set[str] = set()

    for p in sorted(wiki.rglob("*.md")):
        try:
            _, body = fm.parse(p.read_text())
        except Exception:
            continue

        cited_retracted = [
            link.target
            for link in find_wikilinks(body)
            if link.target.startswith("sources/")
            and link.target[len("sources/"):] in retracted_ids
        ]
        if not cited_retracted:
            continue

        rel = str(p.relative_to(paths.knowledge_root()))
        direct_flagged.add(rel)
        for target in sorted(set(cited_retracted)):
            source_id = target[len("sources/"):]
            findings.append(
                LintFinding(
                    check="retracted-citations",
                    severity=SEVERITY_ERROR,
                    message=(
                        f"page cites retracted source `{source_id}` — "
                        "review the claim(s) this source supports and remove "
                        "or replace the citation (QUAL-7)"
                    ),
                    path=rel,
                    metadata={"retracted_source": source_id, "depth": 1},
                )
            )

    # Cascade: surface transitive synthesizes: dependents (G4, Phase 5 T1).
    # Import here to avoid circular imports at module load time.
    from gateway.retraction import cascade_detail
    details = cascade_detail(set(retracted_ids))
    for detail in details:
        # Skip pages already flagged as direct cites (depth=1) — they already
        # carry a more specific SEVERITY_ERROR finding above.
        if detail.rel in direct_flagged:
            continue
        findings.append(
            LintFinding(
                check="retracted-citations",
                severity=SEVERITY_WARNING,
                message=(
                    f"page is a transitive dependent of retracted source "
                    f"`{detail.retracted_source}` via synthesizes: graph "
                    f"(depth={detail.depth}) — review for downstream impact (QUAL-7)"
                ),
                path=detail.rel,
                metadata={
                    "retracted_source": detail.retracted_source,
                    "depth": detail.depth,
                },
            )
        )

    return findings
