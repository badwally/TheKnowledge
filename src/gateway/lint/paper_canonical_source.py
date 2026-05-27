"""ONT-5: paper entities must carry a canonical_source: field.

Flags entity pages with entity_kind: paper that lack a canonical_source
pointing to an ingested raw source ID.
"""

from __future__ import annotations

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    for type_name, path, front, body in walk_wiki_pages():
        if type_name != "entity":
            continue
        if front.get("entity_kind") != "paper":
            continue
        canonical = front.get("canonical_source")
        if not canonical:
            slug = front.get("slug", path.stem)
            findings.append(
                LintFinding(
                    check="paper-canonical-source",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"paper entity '{slug}' lacks canonical_source; "
                        "add canonical_source: <source-id> pointing to raw/<type>/<id>.md"
                    ),
                    path=str(path.relative_to(paths.knowledge_root())),
                    metadata={"entity_kind": "paper", "slug": slug},
                )
            )
    return findings
