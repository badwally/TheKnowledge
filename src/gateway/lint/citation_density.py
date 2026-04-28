"""Citation-density check per WIKI § 5.3.

For each citation-grounded page (entity/concept/source/synthesis), reports
when the cited-claim ratio falls below threshold. Drafts are excluded —
their unresolved-claim count is reported by stale-drafts instead.
"""

from __future__ import annotations

from gateway import citations
from gateway import paths, wiki_pages
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


DEFAULT_DENSITY_THRESHOLD = 0.6


def run(*, threshold: float = DEFAULT_DENSITY_THRESHOLD) -> list[LintFinding]:
    findings: list[LintFinding] = []
    for type_name, path, front, body in walk_wiki_pages():
        if front.get("draft"):
            continue
        schema = wiki_pages.schema_for_type(type_name)
        if schema is None or not schema.citation_grounded:
            continue
        cited, total, ratio = citations.citation_density(body)
        if total == 0:
            continue
        if ratio < threshold:
            findings.append(
                LintFinding(
                    check="citation-density",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"{cited}/{total} claims cited ({ratio:.0%}); "
                        f"threshold {threshold:.0%}"
                    ),
                    path=str(path.relative_to(paths.knowledge_root())),
                    metadata={
                        "cited": cited,
                        "total": total,
                        "ratio": round(ratio, 3),
                        "threshold": threshold,
                    },
                )
            )
    return findings
