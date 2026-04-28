"""Schema-drift check per WIKI § 12.2.

Walks all wiki pages and runs the validator. Reports any rule violation
*except* citation-grounding (which is reported by citation-density to avoid
double-counting).

Citation grounding is fundamentally a quality concern; schema drift is
fundamentally a structural concern. Same page can fail one without the
other, so they get separate buckets in the report.
"""

from __future__ import annotations

from pathlib import Path

from gateway import frontmatter as fm
from gateway import paths, validator, wiki_pages
from gateway.lint import LintFinding, SEVERITY_ERROR


_SUPPRESSED_RULES = {"citation-grounding"}


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return findings

    for type_name, schema in wiki_pages.PAGE_SCHEMAS.items():
        d = paths.knowledge_root() / schema.directory
        if not d.exists():
            continue
        for path in sorted(d.glob("**/*.md")):
            findings.extend(_check_one(type_name, path))
    return findings


def _check_one(type_name: str, path: Path) -> list[LintFinding]:
    rel = str(path.relative_to(paths.knowledge_root()))
    try:
        text = path.read_text()
    except OSError as e:
        return [
            LintFinding(
                check="schema-drift",
                severity=SEVERITY_ERROR,
                message=f"could not read file: {e}",
                path=rel,
            )
        ]
    try:
        front, body = fm.parse(text)
    except fm.FrontmatterError as e:
        return [
            LintFinding(
                check="schema-drift",
                severity=SEVERITY_ERROR,
                message=f"frontmatter: {e}",
                path=rel,
            )
        ]

    result = validator.validate_wiki_page(front, body, type_name)
    out: list[LintFinding] = []
    for err in result.errors:
        if err.rule in _SUPPRESSED_RULES:
            continue
        out.append(
            LintFinding(
                check="schema-drift",
                severity=SEVERITY_ERROR,
                message=str(err),
                path=rel,
                metadata={"rule": err.rule, "field": err.field_name},
            )
        )
    return out
