"""QUAL-14: superseded-citations lint — wiki pages citing superseded sources.

Reports wiki pages that contain [[sources/<id>]] citations where the source
has been superseded by a newer version (`superseded_by:` set in raw frontmatter).
These pages should be reviewed and updated to cite the new version.
"""

from __future__ import annotations

from gateway import frontmatter as fm, paths
from gateway.lint import SEVERITY_WARNING, LintFinding


def run() -> list[LintFinding]:
    """Find wiki pages that cite superseded sources."""
    # Collect superseded source IDs
    superseded: dict[str, str] = {}  # old_id → new_id
    for type_dir in sorted(paths.raw_dir().iterdir()):
        if not type_dir.is_dir():
            continue
        for p in sorted(type_dir.glob("*.md")):
            try:
                front, _ = fm.parse(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            successor = front.get("superseded_by")
            if successor:
                source_id = front.get("id") or p.stem
                superseded[source_id] = str(successor)

    if not superseded:
        return []

    # Walk wiki pages and report any that cite superseded sources
    findings: list[LintFinding] = []
    wiki = paths.wiki_dir()
    for page in sorted(wiki.rglob("*.md")):
        try:
            content = page.read_text(encoding="utf-8")
        except OSError:
            continue
        for old_id, new_id in superseded.items():
            if f"[[sources/{old_id}]]" in content:
                findings.append(
                    LintFinding(
                        check="superseded-citations",
                        severity=SEVERITY_WARNING,
                        message=(
                            f"cites superseded source {old_id!r} "
                            f"(successor: {new_id!r}); review and update"
                        ),
                        path=str(page.relative_to(wiki)),
                        metadata={
                            "superseded_id": old_id,
                            "successor_id": new_id,
                        },
                    )
                )
    return findings
