"""ONT-8: lint check for grandfathered slugs longer than 80 chars.

New pages are hard-rejected by the validator. Pages that existed before
ONT-8 are grandfathered: this check surfaces them as SEVERITY_WARNING so
they can be resolved incrementally.
"""

from __future__ import annotations

from gateway import paths
from gateway import frontmatter as fm
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages

_MAX_SLUG_LEN = 80


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    kb_root = paths.knowledge_root()

    for _type_name, path, front, _body in walk_wiki_pages():
        slug = front.get("slug")
        if slug is None:
            continue
        if len(str(slug)) > _MAX_SLUG_LEN:
            rel = str(path.relative_to(kb_root))
            findings.append(
                LintFinding(
                    check="slug-too-long",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"slug is {len(str(slug))} chars (max {_MAX_SLUG_LEN}); "
                        "grandfathered — rename to comply with ONT-8"
                    ),
                    path=rel,
                    metadata={"slug": str(slug), "length": len(str(slug))},
                )
            )
    return findings
