"""QUAL-1: link_rot lint — report dead and unchecked web sources.

Dead sources are flagged as warnings. Sources whose `link_status` is absent
(never checked) are flagged as info. Wayback archive_url (QUAL-13) is surfaced
in the message for dead sources that have one.
"""

from __future__ import annotations

from gateway import frontmatter as fm, paths
from gateway.lint import SEVERITY_INFO, SEVERITY_WARNING, LintFinding


def run() -> list[LintFinding]:
    raw_web = paths.raw_dir() / "web"
    if not raw_web.exists():
        return []

    findings: list[LintFinding] = []
    for src in sorted(raw_web.glob("*.md")):
        try:
            front, _ = fm.parse(src.read_text())
        except Exception:
            continue

        source_id = src.stem
        link_status = front.get("link_status")
        url = str(front.get("url") or "")

        if link_status == "dead":
            archive_url = (front.get("meta") or {}).get("archive_url")
            msg = f"dead link: {url}"
            if archive_url:
                msg += f" (Wayback: {archive_url})"
            findings.append(
                LintFinding(
                    check="link-rot",
                    severity=SEVERITY_WARNING,
                    message=msg,
                    path=f"raw/web/{source_id}.md",
                    metadata={
                        "source_id": source_id,
                        "url": url,
                        "archive_url": archive_url,
                    },
                )
            )
        elif link_status is None and url:
            findings.append(
                LintFinding(
                    check="link-rot",
                    severity=SEVERITY_INFO,
                    message=f"link never checked: {url}",
                    path=f"raw/web/{source_id}.md",
                    metadata={"source_id": source_id, "url": url},
                )
            )

    return findings
