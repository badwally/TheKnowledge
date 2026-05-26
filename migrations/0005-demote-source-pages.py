"""ONT-10: demote source pages to manifest-only.

Strips stub body sections (## Summary, ## Key claims, ## Cross-references)
from all wiki/sources/*.md pages, leaving only the frontmatter header block
(title line + Source: backlink). The three sections were always placeholders;
their content was never generated. Source pages are citation targets, not
content-bearing pages — the information lives in raw/ and synthesis pages.

Run once:
    python migrations/0005-demote-source-pages.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Run from project root
ROOT = Path(__file__).parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"

# Match any ## heading and everything after it until the next ## or EOF.
_SECTION_RE = re.compile(r"\n## .+?(?=\n## |\Z)", re.DOTALL)

# The stub body always ends after the "Cross-references" section.
# Strip everything from the first ## heading onward (keeps title + Source: line).
_BODY_SECTIONS_RE = re.compile(r"\n## .+", re.DOTALL)


def _strip_stubs(body: str) -> str:
    """Remove all ## sections from the source page body."""
    return _BODY_SECTIONS_RE.sub("", body).rstrip() + "\n"


def main() -> None:
    pages = sorted(SOURCES_DIR.glob("*.md"))
    if not pages:
        print("No source pages found — nothing to do.")
        return

    modified = 0
    skipped = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")

        # Split on the YAML frontmatter fence
        parts = text.split("---", 2)
        if len(parts) < 3:
            skipped += 1
            continue

        front_raw = parts[1]
        body = parts[2]

        if "## " not in body:
            skipped += 1
            continue

        new_body = _strip_stubs(body)
        new_text = f"---{front_raw}---{new_body}"

        if new_text != text:
            page.write_text(new_text, encoding="utf-8")
            modified += 1

    print(f"Modified: {modified}  Skipped (already clean): {skipped}")


if __name__ == "__main__":
    main()
