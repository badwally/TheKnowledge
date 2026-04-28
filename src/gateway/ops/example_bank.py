"""Example-bank + policy backfill from research-notebook legacy artifacts.

Two operations, exposed both directly and via `wiki backfill-examples`:

1. **backfill_policy(legacy_config_path, domain_slug)** — convert a legacy
   `config/domains/<slug>.yaml` into the canonical policy schema at
   `.knowledge/policies/<slug>/policy.yaml`. The canonical schema (WIKI § 10.1)
   adds `domain.slug`, a `filter:` block with sane thresholds, and flattens
   `inclusion_criteria.required` and `exclusion_criteria.hard_exclude` into
   plain lists.

2. **backfill_examples(json_paths, domain_slug)** — read research-notebook
   staged JSON checkpoints (`glp1_scored.json`, `ai_temporal_video_*.json`,
   etc.) and write canonical example bank YAMLs at
   `.knowledge/policies/<slug>/examples/<canonical_id>.yaml`. Each entry is
   pinned with `pinned_by: "legacy-backfill"`.

Three legacy item-id shapes are recognized:
- `pmid:<digits>`        -> `pubmed-<digits>`
- `arxiv:<id>`           -> `arxiv-<id>` (any trailing version stripped)
- YouTube video records  -> `yt-<video_id>` (from the `video_id` field)
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from gateway import paths
from gateway.filter import examples as example_bank


_ARXIV_VERSION_RE = re.compile(r"v\d+$")


@dataclass(frozen=True)
class BackfillReport:
    written: int = 0
    skipped: int = 0
    errors: list[str] = None  # type: ignore[assignment]

    def __post_init__(self):
        # Avoid mutable default in @dataclass(frozen=True).
        if self.errors is None:
            object.__setattr__(self, "errors", [])


# --- policy backfill -------------------------------------------------------


_DEFAULT_FILTER = {
    "threshold_include": 0.70,
    "threshold_review": 0.50,
    "example_count_in_prompt": 12,
    "example_strategy": "balanced",
}


def backfill_policy(legacy_config_path: Path, domain_slug: str) -> Path:
    """Read a legacy `config/domains/<slug>.yaml` and write the canonical
    policy.yaml. Returns the canonical path."""
    legacy_config_path = Path(legacy_config_path).expanduser().resolve()
    if not legacy_config_path.is_file():
        raise FileNotFoundError(f"legacy config not found: {legacy_config_path}")

    legacy = yaml.safe_load(legacy_config_path.read_text()) or {}
    if not isinstance(legacy, dict):
        raise ValueError(f"legacy config must be a YAML mapping, got {type(legacy).__name__}")

    legacy_domain = legacy.get("domain", {}) or {}
    canonical: dict[str, Any] = {
        "version": str(legacy.get("version", "v1")),
        "domain": {
            "slug": domain_slug,
            "topic": str(legacy_domain.get("topic", "")),
            "field": str(legacy_domain.get("field", "")),
            "description": str(legacy_domain.get("description", "")).strip(),
        },
        "filter": dict(_DEFAULT_FILTER),
        "inclusion_criteria": _flatten_criteria(legacy.get("inclusion_criteria")),
        "exclusion_criteria": _flatten_criteria(legacy.get("exclusion_criteria")),
        "quality_signals": dict(legacy.get("quality_signals", {}) or {}),
    }

    target = paths.policies_dir() / domain_slug / "policy.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(yaml.safe_dump(canonical, sort_keys=False, allow_unicode=True))
    return target


def _flatten_criteria(value: Any) -> list[str]:
    """Legacy uses `inclusion_criteria.required` / `exclusion_criteria.hard_exclude`
    nested keys; canonical uses a flat list. Tolerate either shape."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(s) for s in value if isinstance(s, str)]
    if isinstance(value, dict):
        out: list[str] = []
        for v in value.values():
            if isinstance(v, list):
                out.extend(str(s) for s in v if isinstance(s, str))
        return out
    return []


# --- example-bank backfill -------------------------------------------------


def backfill_examples(
    json_paths: Iterable[Path],
    domain_slug: str,
    *,
    policy_version: str | None = None,
) -> BackfillReport:
    """Convert one or more legacy staged JSON checkpoints into canonical
    example bank YAMLs under `.knowledge/policies/<domain>/examples/`."""
    policy_version = policy_version or f"{domain_slug}-legacy-v1"

    written = 0
    skipped = 0
    errors: list[str] = []

    for path in json_paths:
        path = Path(path).expanduser().resolve()
        if not path.is_file():
            errors.append(f"not found: {path}")
            continue

        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON ({e})")
            continue

        for record in _iter_records(data):
            try:
                w, s = _backfill_one_record(
                    record, domain_slug=domain_slug, policy_version=policy_version
                )
                written += w
                skipped += s
            except Exception as e:
                errors.append(f"{path.name} item: {e!r}")

    return BackfillReport(written=written, skipped=skipped, errors=errors)


def _iter_records(data: Any) -> Iterable[dict]:
    """Legacy JSONs are either a list of records or a dict with `videos` /
    `items` / `entries` containing the list."""
    if isinstance(data, list):
        for r in data:
            if isinstance(r, dict):
                yield r
        return
    if isinstance(data, dict):
        for key in ("videos", "items", "entries", "results"):
            v = data.get(key)
            if isinstance(v, list):
                for r in v:
                    if isinstance(r, dict):
                        yield r
                return


def _backfill_one_record(
    record: dict, *, domain_slug: str, policy_version: str
) -> tuple[int, int]:
    """Returns (written, skipped) — both 0 or 1."""
    canonical_id = _canonical_id(record)
    if not canonical_id:
        return 0, 1

    relevance = record.get("relevance_score")
    if relevance is None:
        return 0, 1
    try:
        score = float(relevance) / 5.0
    except (TypeError, ValueError):
        return 0, 1

    included = record.get("included")
    if included is None:
        # Pre-decision records (raw search results) — skip.
        return 0, 1
    decision = "include" if included else "exclude"

    rationale = (record.get("inclusion_rationale") or "(no rationale)").strip()
    snapshot = _frontmatter_snapshot(record)
    excerpt = _content_excerpt(record)

    example_bank.pin(
        source_id=canonical_id,
        domain=domain_slug,
        decision=decision,
        score=round(score, 3),
        policy_version=policy_version,
        rationale=rationale,
        pinned_by="legacy-backfill",
        frontmatter_snapshot=snapshot,
        content_excerpt=excerpt,
    )
    return 1, 0


def _canonical_id(record: dict) -> str | None:
    """Map a legacy record to a canonical source ID."""
    item_id = record.get("item_id")
    if isinstance(item_id, str) and ":" in item_id:
        prefix, _, raw = item_id.partition(":")
        prefix = prefix.lower()
        raw = raw.strip()
        if not raw:
            return None
        if prefix in ("pmid", "pubmed"):
            return f"pubmed-{raw}"
        if prefix == "arxiv":
            return f"arxiv-{_ARXIV_VERSION_RE.sub('', raw)}"
        return None

    vid = record.get("video_id")
    if isinstance(vid, str) and vid:
        return f"yt-{vid}"

    # YouTube records sometimes store the id only in the URL.
    url = str(record.get("url") or "")
    m = re.search(r"v=([A-Za-z0-9_-]{6,15})", url)
    if m:
        return f"yt-{m.group(1)}"

    return None


def _frontmatter_snapshot(record: dict) -> dict[str, Any]:
    snap: dict[str, Any] = {
        "title": str(record.get("title", "")),
    }
    if record.get("source_type"):
        snap["source_type"] = record["source_type"]
    if record.get("authors"):
        snap["authors"] = record["authors"]
    if record.get("publish_date") or record.get("published_at"):
        snap["published_at"] = str(record.get("publish_date") or record.get("published_at"))
    if record.get("channel_name"):
        snap["channel"] = record["channel_name"]
    if record.get("source_metadata"):
        snap["source_metadata"] = record["source_metadata"]
    return snap


def _content_excerpt(record: dict) -> str:
    text = record.get("description") or ""
    return str(text)[:500]


# --- convenience driver ----------------------------------------------------


def backfill(
    *,
    domain_slug: str,
    legacy_config_path: Path | None = None,
    json_paths: Iterable[Path] | None = None,
    policy_version: str | None = None,
) -> dict[str, Any]:
    """Run policy + examples backfill in one shot. Returns a structured
    summary suitable for CLI display."""
    summary: dict[str, Any] = {"domain": domain_slug}

    if legacy_config_path is not None:
        policy_path = backfill_policy(legacy_config_path, domain_slug)
        summary["policy"] = str(policy_path)

    if json_paths:
        report = backfill_examples(
            json_paths, domain_slug, policy_version=policy_version
        )
        summary["examples_written"] = report.written
        summary["examples_skipped"] = report.skipped
        summary["errors"] = list(report.errors)

    return summary
