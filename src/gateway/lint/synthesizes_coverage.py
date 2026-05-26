"""ONT-11: synthesizes: coverage check.

Synthesis pages that lack `synthesizes:` frontmatter are missing the
Cochrane-style included-studies record that M45 established.

Severity: ERROR (escalated from WARNING in M71 once backfill-synthesizes
shipped). Run `wiki backfill-synthesizes` to auto-populate from body
wikilinks, then fix remaining pages manually.
"""

from __future__ import annotations

from gateway import frontmatter as fm, paths
from gateway.lint import LintFinding, SEVERITY_ERROR


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
                    severity=SEVERITY_ERROR,
                    message=(
                        "synthesis page missing `synthesizes:` — run "
                        "`wiki backfill-synthesizes` to auto-populate from body "
                        "wikilinks, then add remaining entries manually "
                        "(Cochrane-style included-studies, M45/ONT-11)"
                    ),
                    path=rel,
                    metadata={"slug": front.get("slug", p.stem)},
                )
            )

    return findings
