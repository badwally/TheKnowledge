"""QUAL-9: domain_purity lint — centroid drift in blessed domains.

Reports wiki/sources pages tagged to multiple blessed domains, indicating
possible cross-domain contamination from the legacy migration.
"""

from __future__ import annotations

from gateway import frontmatter as fm, paths
from gateway.lint import SEVERITY_WARNING, LintFinding


def run() -> list[LintFinding]:
    """Find source pages tagged to multiple blessed domains (centroid drift)."""
    sources_dir = paths.wiki_dir() / "sources"
    if not sources_dir.exists():
        return []

    policies_dir = paths.policies_dir()
    if not policies_dir.exists():
        return []

    blessed_domains: set[str] = {
        p.parent.name for p in policies_dir.glob("*/policy.yaml")
    }
    if not blessed_domains:
        return []

    findings: list[LintFinding] = []
    for p in sorted(sources_dir.glob("*.md")):
        try:
            front, _ = fm.parse(p.read_text())
        except Exception:
            continue
        domains = list(front.get("domains") or [])
        shared = [d for d in domains if d in blessed_domains]
        if len(shared) > 1:
            findings.append(
                LintFinding(
                    check="domain-purity",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"source tagged to {len(shared)} blessed domains: "
                        + ", ".join(sorted(shared))
                    ),
                    path=str(p.relative_to(paths.wiki_dir())),
                    metadata={
                        "source_id": p.stem,
                        "domains": domains,
                        "shared_blessed": shared,
                    },
                )
            )
    return findings
