"""ONT-12: lint check for `tags:` fields that are not a list of strings.

tags: is an optional list[str] for sub-domain topic clustering. Pages that
carry tags in the wrong type (scalar string, dict, list with non-string items)
are flagged as WARNING so they can be fixed incrementally.
"""

from __future__ import annotations

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    kb_root = paths.knowledge_root()

    for _type_name, path, front, _body in walk_wiki_pages():
        tags = front.get("tags")
        if tags is None:
            continue
        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            continue
        rel = str(path.relative_to(kb_root))
        findings.append(
            LintFinding(
                check="tags-invalid-type",
                severity=SEVERITY_WARNING,
                message=(
                    f"tags must be list[str] (ONT-12); "
                    f"got {type(tags).__name__ if not isinstance(tags, list) else 'list with non-string items'}"
                ),
                path=rel,
                metadata={"tags_type": type(tags).__name__},
            )
        )
    return findings
