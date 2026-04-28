"""Orphan check: wiki pages with no inbound wikilinks from other pages.

Identity for inbound counting:
- entity:    `entities/<slug>`
- concept:   `concepts/<slug>`
- source:    `sources/<id>`
- synthesis: `synthesis/<slug>`
- moc:       `mocs/<slug>`
- artifact:  `artifacts/<type>/<slug>`

A page X is orphan iff no OTHER wiki page contains a `[[<X-identity>]]`
or `[[<X-identity>...]]` (with anchor or alias). MOC and artifact pages
are excluded from "orphan" status — they're intentional entry points.
"""

from __future__ import annotations

from pathlib import Path

from gateway import citations
from gateway import paths
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


_ORPHAN_EXEMPT_TYPES = {"moc", "artifact"}


def _identity_for(type_name: str, path: Path, front: dict) -> str | None:
    rel = path.relative_to(paths.knowledge_root())
    parts = rel.with_suffix("").parts
    # parts[0] should be "wiki"; remainder is e.g. ("entities", "semaglutide")
    if parts[0] != "wiki":
        return None
    return "/".join(parts[1:])


def run() -> list[LintFinding]:
    pages: list[tuple[str, Path, str]] = []
    inbound: dict[str, int] = {}

    # First pass: collect identities + count inbound links from every page's body.
    bodies: list[tuple[str, Path, str, str]] = []  # (type, path, identity, body)
    for type_name, path, front, body in walk_wiki_pages():
        identity = _identity_for(type_name, path, front)
        if identity is None:
            continue
        bodies.append((type_name, path, identity, body))
        pages.append((type_name, path, identity))
        inbound.setdefault(identity, 0)

    # Build inbound counts (excluding self-references).
    for type_name, path, identity, body in bodies:
        for citation in citations.find_wikilinks(body):
            target = citation.target
            if target == identity:
                continue
            if target in inbound:
                inbound[target] += 1

    findings: list[LintFinding] = []
    for type_name, path, identity in pages:
        if type_name in _ORPHAN_EXEMPT_TYPES:
            continue
        if inbound.get(identity, 0) == 0:
            findings.append(
                LintFinding(
                    check="orphans",
                    severity=SEVERITY_WARNING,
                    message=f"{type_name} '{identity}' has no inbound wikilinks",
                    path=str(path.relative_to(paths.knowledge_root())),
                    metadata={"page_type": type_name},
                )
            )
    return findings
