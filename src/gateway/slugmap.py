"""Legacy → canonical slug detection and ID generation per MIGRATION.md § 6.

Legacy research-notebook vaults use short slugs that map directly to source
IDs via frontmatter:

- YouTube: `<videoId>.md` with `video_id:` in frontmatter → `yt-<videoId>`
- arXiv:   `arxiv_<id>.md` with `source_type: arxiv` → `arxiv-<id>` (version stripped)
- PubMed:  `pubmed_<pmid>.md` with `source_type: pubmed` → `pubmed-<pmid>`

This module is separate from `wiki_pages.py` (which handles wiki-page slugs)
because legacy slug detection is migration-specific machinery.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import yaml

from gateway import frontmatter as fm


_ARXIV_VERSION_RE = re.compile(r"v\d+$")
_ARXIV_URL_RE = re.compile(r"arxiv\.org/abs/([^\s/?]+)")


@dataclass
class LegacySource:
    legacy_path: Path        # absolute path to the legacy file
    legacy_slug: str         # filename stem (e.g., '_5qjj2CzBSw' or 'arxiv_2404.01358')
    source_type: str         # 'youtube' | 'arxiv' | 'pubmed' | 'other'
    canonical_id: str        # 'yt-_5qjj2CzBSw' | 'arxiv-2404.01358' | 'pubmed-39847203'
    legacy_front: dict
    legacy_body: str


def detect_legacy_source(path: Path) -> LegacySource | None:
    """Parse a legacy source page and identify its canonical mapping."""
    try:
        front, body = fm.parse(path.read_text())
    except (fm.FrontmatterError, OSError):
        return None

    legacy_slug = path.stem
    source_type, canonical_id = _identify(legacy_slug, front)
    if not source_type:
        return None

    return LegacySource(
        legacy_path=path,
        legacy_slug=legacy_slug,
        source_type=source_type,
        canonical_id=canonical_id,
        legacy_front=front,
        legacy_body=body,
    )


def _identify(legacy_slug: str, front: dict) -> tuple[str, str]:
    """Return (source_type, canonical_id) for a legacy source's frontmatter."""
    # YouTube: legacy frontmatter has `video_id:` directly
    vid = front.get("video_id")
    if vid:
        return "youtube", f"yt-{vid}"

    src_type = str(front.get("source_type", "")).lower()
    url = str(front.get("url", ""))

    # arXiv
    if src_type == "arxiv" or legacy_slug.startswith("arxiv_") or "arxiv.org" in url:
        aid = front.get("arxiv_id") or _arxiv_id_from(legacy_slug, url)
        if aid:
            return "arxiv", f"arxiv-{_ARXIV_VERSION_RE.sub('', str(aid))}"

    # PubMed
    if src_type == "pubmed" or legacy_slug.startswith("pubmed_") or "pubmed" in url:
        pmid = front.get("pmid") or _pmid_from(legacy_slug, url)
        if pmid:
            return "pubmed", f"pubmed-{pmid}"

    # YouTube fallback: 11-char video-id-shaped slug + youtube URL
    if re.match(r"^[A-Za-z0-9_-]{10,15}$", legacy_slug) and "youtube" in url.lower():
        return "youtube", f"yt-{legacy_slug}"

    return "", ""


def _arxiv_id_from(legacy_slug: str, url: str) -> str | None:
    if legacy_slug.startswith("arxiv_"):
        return legacy_slug[len("arxiv_"):]
    match = _ARXIV_URL_RE.search(url)
    return match.group(1) if match else None


def _pmid_from(legacy_slug: str, url: str) -> str | None:
    if legacy_slug.startswith("pubmed_"):
        return legacy_slug[len("pubmed_"):]
    match = re.search(r"pubmed[/.]\D*(\d+)", url)
    return match.group(1) if match else None


def build_slug_map(vault_path: Path) -> dict[str, LegacySource]:
    """Walk `<vault>/sources/` and return {legacy_slug: LegacySource}."""
    sources_dir = vault_path / "sources"
    if not sources_dir.is_dir():
        return {}

    out: dict[str, LegacySource] = {}
    for path in sorted(sources_dir.glob("*.md")):
        ls = detect_legacy_source(path)
        if ls is not None:
            out[ls.legacy_slug] = ls
    return out


def citation_mapping(slug_map: dict[str, LegacySource]) -> dict[str, str]:
    """Build a {old_target: new_target} dict for `citations.rewrite_wikilinks`.

    Legacy wikilinks may be `[[<legacy_slug>]]` (bare) or `[[sources/<legacy_slug>]]`.
    Both forms map to the canonical `sources/<canonical_id>`.
    """
    mapping: dict[str, str] = {}
    for ls in slug_map.values():
        canonical = f"sources/{ls.canonical_id}"
        mapping[ls.legacy_slug] = canonical
        mapping[f"sources/{ls.legacy_slug}"] = canonical
    return mapping


def save_slug_map(domain_slug: str, slug_map: dict[str, LegacySource], target_dir: Path) -> Path:
    """Persist a slug-map audit artifact to `<target_dir>/<domain>-slug-map.yaml`."""
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{domain_slug}-slug-map.yaml"
    payload = {
        "domain": domain_slug,
        "count": len(slug_map),
        "entries": [
            {
                "legacy_slug": ls.legacy_slug,
                "legacy_path": str(ls.legacy_path),
                "source_type": ls.source_type,
                "canonical_id": ls.canonical_id,
            }
            for ls in sorted(slug_map.values(), key=lambda s: s.canonical_id)
        ],
    }
    target.write_text(yaml.safe_dump(payload, sort_keys=False, default_flow_style=False))
    return target
