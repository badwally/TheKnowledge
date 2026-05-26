"""AGT-13: Per-domain skill auto-generation.

`wiki skill-emit <domain>` reads the domain's policy.yaml, MOC, and recent
log entries, then writes `.claude/skills/wiki-<domain>/SKILL.md` with:
- Domain inclusion/exclusion criteria (from policy.yaml)
- Top entities and concepts (from MOC section headers and wikilinks)
- Open threads (from recent synthesis pages' titles)

The output is deterministic: same inputs → same file. Regenerated automatically
on `bootstrap-domain`, `promote-domain`, and weekly steward runs.

File cap: <300 lines enforced at generation time.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult

_MAX_LINES = 295
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
_LOG_DOMAIN_RE = re.compile(r"domain=(\S+)")


def _load_policy(domain: str) -> dict | None:
    p = paths.knowledge_internal() / "policies" / domain / "policy.yaml"
    if not p.is_file():
        return None
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8"))
        return raw if isinstance(raw, dict) else None
    except Exception:
        return None


def _load_moc(domain: str) -> str | None:
    moc_path = paths.wiki_dir() / "mocs" / f"{domain}.md"
    if not moc_path.is_file():
        return None
    try:
        _, body = fm.parse(moc_path.read_text(encoding="utf-8"))
        return body
    except Exception:
        return moc_path.read_text(encoding="utf-8")


def _extract_top_concepts(moc_body: str, *, max_items: int = 10) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for m in _WIKILINK_RE.finditer(moc_body):
        target = m.group(1).strip()
        if target.startswith("concepts/"):
            slug = target[len("concepts/"):]
            if slug not in seen:
                seen.add(slug)
                out.append(slug)
        if len(out) >= max_items:
            break
    return out


def _extract_top_entities(moc_body: str, *, max_items: int = 8) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for m in _WIKILINK_RE.finditer(moc_body):
        target = m.group(1).strip()
        if target.startswith("entities/"):
            slug = target[len("entities/"):]
            if slug not in seen:
                seen.add(slug)
                out.append(slug)
        if len(out) >= max_items:
            break
    return out


def _extract_open_threads(domain: str, *, max_items: int = 5) -> list[str]:
    synth_dir = paths.wiki_dir() / "synthesis"
    if not synth_dir.exists():
        return []
    threads: list[str] = []
    for p in sorted(synth_dir.glob("*.md"), reverse=True):
        try:
            front, _ = fm.parse(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if domain not in (front.get("domains") or []):
            continue
        title = front.get("title") or front.get("slug") or p.stem
        threads.append(str(title))
        if len(threads) >= max_items:
            break
    return threads


def _render_skill(domain: str, policy: dict | None, moc_body: str | None) -> str:
    domain_info = (policy or {}).get("domain") or {}
    topic = domain_info.get("topic") or domain
    description = domain_info.get("description") or ""

    inclusion = (policy or {}).get("inclusion_criteria") or []
    exclusion = (policy or {}).get("exclusion_criteria") or []

    concepts = _extract_top_concepts(moc_body or "")
    entities = _extract_top_entities(moc_body or "")
    threads = _extract_open_threads(domain)

    lines: list[str] = [
        "---",
        f"name: wiki-{domain}",
        f"description: Domain assistant for {domain} — inclusion criteria, key entities/concepts, open threads",
        f"triggers: [wiki-{domain}]",
        "---",
        "",
        f"# wiki-{domain} skill",
        "",
        f"**Domain:** {domain}  ",
        f"**Topic:** {topic}",
        "",
    ]

    if description:
        lines += [description, ""]

    lines += [
        "## Inclusion criteria",
        "",
        "Sources and claims are relevant to this domain if they:",
    ]
    for criterion in inclusion:
        lines.append(f"- {criterion}")
    if not inclusion:
        lines.append("- (no criteria defined; run `wiki bootstrap-domain` to populate)")
    lines.append("")

    if exclusion:
        lines += ["## Exclusion criteria", ""]
        for criterion in exclusion:
            lines.append(f"- {criterion}")
        lines.append("")

    if entities:
        lines += ["## Key entities", ""]
        for e in entities:
            lines.append(f"- [[entities/{e}]]")
        lines.append("")

    if concepts:
        lines += ["## Key concepts", ""]
        for c in concepts:
            lines.append(f"- [[concepts/{c}]]")
        lines.append("")

    if threads:
        lines += [
            "## Open threads",
            "",
            "Recent synthesis pages (starting points for new research):",
        ]
        for t in threads:
            lines.append(f"- {t}")
        lines.append("")

    lines += [
        "## Usage",
        "",
        f"```",
        f"wiki ingest <url> --domain {domain}",
        f"wiki research \"<question>\" --domain {domain}",
        f"wiki query \"<question>\" --domain {domain}",
        f"```",
        "",
        "## Reference",
        "",
        "- WIKI.md — gateway conventions, frontmatter schema, hard rules",
        f"- `wiki/mocs/{domain}.md` — domain map of content",
        f"- `.knowledge/policies/{domain}/policy.yaml` — filter policy",
        "",
        f"*Auto-generated by `wiki skill-emit {domain}`. Regenerate after major corpus changes.*",
    ]

    # Enforce line cap
    if len(lines) > _MAX_LINES:
        lines = lines[: _MAX_LINES - 2] + ["", f"*(truncated at {_MAX_LINES} lines)*"]

    return "\n".join(lines) + "\n"


def skill_emit(domain: str) -> OperationResult:
    """Generate `.claude/skills/wiki-<domain>/SKILL.md` for `domain`."""
    policy = _load_policy(domain)
    moc_body = _load_moc(domain)

    if policy is None and moc_body is None:
        return OperationResult(
            success=False,
            errors=[
                f"domain {domain!r} has no policy.yaml and no MOC — "
                "run `wiki bootstrap-domain` or `wiki promote-domain` first"
            ],
        )

    content = _render_skill(domain, policy, moc_body)

    skills_base = paths.knowledge_root() / ".claude" / "skills"
    skill_dir = skills_base / f"wiki-{domain}"
    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_path = skill_dir / "SKILL.md"
    skill_path.write_text(content, encoding="utf-8")

    log.append(
        "skill-emit",
        fields={"domain": domain, "path": str(skill_path.relative_to(paths.knowledge_root()))},
        summary=f"emitted skill for domain {domain!r}",
    )

    line_count = len(content.splitlines())
    return OperationResult(
        success=True,
        paths_touched=[skill_path],
        summary=f"wrote {skill_path.relative_to(paths.knowledge_root())} ({line_count} lines)",
    )
