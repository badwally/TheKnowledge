"""Broken wikilink check: every [[<dir>/<slug>]] must resolve (QUAL-4).

Walks all wiki pages and checks that every wikilink target exists on disk:

- `sources/`, `entities/`, `concepts/`, `mocs/`, `synthesis/` are checked.
- `[[nlm:<uuid>]]` links are exempt — opaque corpus references intentionally
  don't map to on-disk pages.
- `[[target|alias]]` where the target does not exist is reported as a
  warning (forward-reference) rather than an error, because the alias
  signals intent to create the target later.
"""

from __future__ import annotations

import re

from gateway import citations, paths
from gateway.lint import LintFinding, SEVERITY_ERROR, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


_CHECKABLE_PREFIXES = frozenset(
    {"sources/", "entities/", "concepts/", "mocs/", "synthesis/"}
)

# Detects whether the raw [[...]] token contains a | alias.
_ALIAS_RE = re.compile(r"\[\[[^\]]+\|[^\]]+\]\]")


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    kb_root = paths.knowledge_root()
    wiki_dir = kb_root / "wiki"

    for type_name, path, front, body in walk_wiki_pages():
        rel = str(path.relative_to(kb_root))
        seen: set[str] = set()
        for citation in citations.find_wikilinks(body):
            target = citation.target
            if target.startswith("nlm:"):
                continue
            if not any(target.startswith(p) for p in _CHECKABLE_PREFIXES):
                continue
            if target in seen:
                continue
            candidate = wiki_dir / f"{target}.md"
            if candidate.is_file():
                continue
            seen.add(target)
            has_alias = "|" in citation.raw
            findings.append(
                LintFinding(
                    check="broken-wikilinks",
                    severity=SEVERITY_WARNING if has_alias else SEVERITY_ERROR,
                    message=(
                        f"forward-reference [[{target}]] target not yet created"
                        if has_alias
                        else f"broken wikilink [[{target}]] — target not found"
                    ),
                    path=rel,
                    metadata={"target": target, "source_page": rel},
                )
            )
    return findings
