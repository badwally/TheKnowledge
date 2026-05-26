"""Repo-metadata poller (INT-8).

Polls ~/code/*/README.md, ~/code/*/CLAUDE.md, ~/code/*/docs/*.md and writes
each changed or new file to raw/note/ as a canonical note source.

Cursor: per-file SHA-256 content hashes stored at
  .knowledge/pollers/repo-metadata/cursor.yaml

Re-ingest only when a file's hash differs from the cursor.  Stable slug is
derived from project name + relative path + a short path hash so it never
collides across renames.
"""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm
from gateway import paths, validator
from gateway.pollers.base import Poller, PollerResult


_CODE_ROOT: Path = Path.home() / "code"

_EXCLUDED_DIRS: frozenset[str] = frozenset({
    "node_modules", ".venv", "__pycache__", ".git", "vendor", "dist", "build",
})


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _path_hash8(p: Path) -> str:
    return hashlib.sha256(str(p).encode()).hexdigest()[:8]


def _slugify(text: str) -> str:
    """Lowercase, replace non-alphanumeric runs with hyphens, strip edges."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "x"


def _make_slug(project_name: str, rel_path: Path) -> str:
    """Stable slug: note-repo-<project>-<rel_slug>-<hash8>."""
    rel_stem = rel_path.with_suffix("")  # drop .md
    rel_slug = _slugify(str(rel_stem).replace("/", "-").replace("\\", "-"))
    p_slug = _slugify(project_name)
    h8 = _path_hash8(Path(project_name) / rel_path)
    return f"note-repo-{p_slug}-{rel_slug}-{h8}"


def _collect_files(project_dir: Path) -> list[tuple[Path, Path]]:
    """Return [(abs_path, rel_path)] for target files under a project dir.

    Targets: README.md, CLAUDE.md at root; any .md under docs/.
    Skips any path component that names an excluded directory.
    """
    results: list[tuple[Path, Path]] = []

    for name in ("README.md", "CLAUDE.md"):
        candidate = project_dir / name
        if candidate.is_file():
            results.append((candidate, Path(name)))

    docs_dir = project_dir / "docs"
    if docs_dir.is_dir() and docs_dir.name not in _EXCLUDED_DIRS:
        for md_file in sorted(docs_dir.glob("*.md")):
            if md_file.is_file():
                results.append((md_file, Path("docs") / md_file.name))

    return results


def _content_hash(text: str) -> str:
    return validator.compute_content_hash(text)


class RepoMetadataPoller(Poller):
    """Poll sibling ~/code/ projects and ingest their documentation."""

    name = "repo-metadata"
    source_type = "note"

    def run(self) -> PollerResult:
        code_root = _CODE_ROOT

        if not code_root.is_dir():
            return PollerResult(success=True, fetched=0, skipped=0, summary="repo-metadata: code root absent")

        cursor = self.read_cursor()
        file_hashes: dict[str, str] = cursor.get("files", {})

        fetched = 0
        skipped = 0
        updated_hashes = dict(file_hashes)

        for project_dir in sorted(code_root.iterdir()):
            if not project_dir.is_dir():
                continue
            if project_dir.name in _EXCLUDED_DIRS:
                continue

            project_name = project_dir.name
            domain_slug = project_name
            domains: list[str] = []
            if (paths.policies_dir() / f"{domain_slug}.yaml").exists():
                domains = [domain_slug]

            for abs_path, rel_path in _collect_files(project_dir):
                body_text = abs_path.read_text(encoding="utf-8", errors="replace")
                body = body_text if body_text.endswith("\n") else body_text + "\n"
                hash_key = str(abs_path)
                new_hash = _content_hash(body)

                if file_hashes.get(hash_key) == new_hash:
                    skipped += 1
                    continue

                slug = _make_slug(project_name, rel_path)
                front: dict = {
                    "id": slug,
                    "type": "note",
                    "title": f"{project_name}/{rel_path}",
                    "url": "",
                    "authors": [],
                    "ingested_at": _now_iso(),
                    "content_hash": new_hash,
                    "domains": domains,
                    "nlm_corpus_ids": [],
                    "wiki_pages": [],
                    "meta": {
                        "source_app": "repo-metadata",
                        "project": project_name,
                        "rel_path": str(rel_path),
                        "abs_path": str(abs_path),
                    },
                }
                self.write_raw(slug, fm.serialize(front, body))
                updated_hashes[hash_key] = new_hash
                fetched += 1

        self.write_cursor({"files": updated_hashes})
        return PollerResult(
            success=True,
            fetched=fetched,
            skipped=skipped,
            summary=f"repo-metadata: fetched={fetched} skipped={skipped}",
        )
