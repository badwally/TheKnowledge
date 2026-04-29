"""Untagged-sources lint check (M36).

Counts wiki/sources/<id>.md pages whose `domains:` frontmatter is empty
or missing. These sources are inert from the citation-graph perspective:
they have no domain policy, won't surface in `lint --scope missing-pages`,
and won't be selected by domain-scoped queries.

The remediation is `wiki discover-domains --untagged` followed by
`wiki promote-domain <slug>` for any cluster that maps cleanly to a
domain you want to author against.
"""

from __future__ import annotations

from gateway import frontmatter as fm
from gateway import paths
from gateway.lint import LintFinding, SEVERITY_INFO


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    sources_dir = paths.wiki_dir() / "sources"
    if not sources_dir.exists():
        return findings

    untagged_ids: list[str] = []
    for path in sorted(sources_dir.glob("*.md")):
        try:
            front, _ = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        domains = front.get("domains") or []
        if not domains:
            sid = str(front.get("source_id") or path.stem)
            untagged_ids.append(sid)

    if not untagged_ids:
        return findings

    findings.append(
        LintFinding(
            check="untagged-sources",
            severity=SEVERITY_INFO,
            message=(
                f"{len(untagged_ids)} source page(s) have no domains: tag — "
                "run `wiki discover-domains --untagged` to surface candidate clusters"
            ),
            metadata={
                "count": len(untagged_ids),
                "examples": untagged_ids[:10],
            },
        )
    )
    return findings
