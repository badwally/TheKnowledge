"""ONT-11: synthesizes: coverage check.

Synthesis pages that lack `synthesizes:` frontmatter are missing the
Cochrane-style included-studies record that M45 established.  38/94 pages
have it; this lint pass warns on the 56 that do not, escalating the
existing validator integrity check to a corpus-wide scan.

Severity: WARNING (review prescribed "lint warning → error after backfill").
"""

from __future__ import annotations

from gateway import frontmatter as fm, paths
from gateway.lint import LintFinding, SEVERITY_WARNING


def run() -> list[LintFinding]:
    synth_dir = paths.wiki_dir() / "synthesis"
    if not synth_dir.exists():
        return []

    findings: list[LintFinding] = []
    for p in sorted(synth_dir.glob("*.md")):
        try:
            front, _ = fm.parse(p.read_text())
        except Exception:
            continue

        synthesizes = front.get("synthesizes")
        if not synthesizes:
            rel = str(p.relative_to(paths.knowledge_root()))
            findings.append(
                LintFinding(
                    check="synthesizes-coverage",
                    severity=SEVERITY_WARNING,
                    message=(
                        "synthesis page missing `synthesizes:` — add a list of "
                        "`sources/<id>` or `synthesis/<slug>` entries to record "
                        "the included studies (Cochrane-style, M45/ONT-11)"
                    ),
                    path=rel,
                    metadata={"slug": front.get("slug", p.stem)},
                )
            )

    return findings
