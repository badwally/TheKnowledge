"""ONT-14: lint checks for question pages.

- open-questions: INFO finding listing open/partial questions (visibility)
- answered-no-synthesis: WARNING for answered questions without a synthesis link
"""

from __future__ import annotations

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_INFO, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


def _question_pages() -> list[tuple]:
    """Return (path, front) for all question-type wiki pages."""
    pages = []
    for _type_name, path, front, _body in walk_wiki_pages():
        if front.get("type") == "question":
            pages.append((path, front))
    return pages


def run_open_questions() -> list[LintFinding]:
    """INFO finding for each open or partial question (visibility)."""
    findings: list[LintFinding] = []
    kb_root = paths.knowledge_root()
    for path, front in _question_pages():
        status = str(front.get("status", "open"))
        if status not in ("open", "partial"):
            continue
        rel = str(path.relative_to(kb_root))
        slug = str(front.get("slug", path.stem))
        title = str(front.get("title", slug))
        findings.append(
            LintFinding(
                check="open-questions",
                severity=SEVERITY_INFO,
                message=f"[{status}] {title}",
                path=rel,
                metadata={"status": status, "slug": slug},
            )
        )
    return findings


def run_answered_no_synthesis() -> list[LintFinding]:
    """WARNING for answered questions missing a synthesis: link."""
    findings: list[LintFinding] = []
    kb_root = paths.knowledge_root()
    for path, front in _question_pages():
        status = str(front.get("status", "open"))
        if status != "answered":
            continue
        if front.get("synthesis"):
            continue
        rel = str(path.relative_to(kb_root))
        slug = str(front.get("slug", path.stem))
        findings.append(
            LintFinding(
                check="answered-no-synthesis",
                severity=SEVERITY_WARNING,
                message=f"answered question '{slug}' has no synthesis: link",
                path=rel,
                metadata={"slug": slug},
            )
        )
    return findings
