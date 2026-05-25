"""ONT-3: lint check for structured contradiction pages.

Walks wiki/contradictions/*.md and surfaces open+major contradictions
as SEVERITY_WARNING so they appear in every lint run.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_WARNING


def run() -> list[LintFinding]:
    contradictions_dir = paths.wiki_dir() / "contradictions"
    if not contradictions_dir.exists():
        return []

    findings: list[LintFinding] = []
    for md_file in sorted(contradictions_dir.glob("*.md")):
        text = md_file.read_text()
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            front = yaml.safe_load(text[3:end]) or {}
        except yaml.YAMLError:
            continue

        status = str(front.get("status", ""))
        severity = str(front.get("severity", ""))
        if status == "open" and severity == "major":
            slug = str(front.get("slug", md_file.stem))
            findings.append(
                LintFinding(
                    check="contradiction-pages",
                    severity=SEVERITY_WARNING,
                    message=f"open major contradiction: {slug}",
                    path=str(md_file.relative_to(paths.knowledge_root())),
                    metadata={"slug": slug, "severity": severity, "status": status},
                )
            )
    return findings
