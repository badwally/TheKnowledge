"""AGT-13: wiki skill-emit — per-domain skill auto-generation."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm, paths
from gateway.ops.skill_emit import skill_emit, _render_skill, _MAX_LINES


# --- helpers -------------------------------------------------------------------


def _write_policy(kb_root: Path, domain: str, *, inclusion: list[str] | None = None) -> Path:
    d = kb_root / ".knowledge" / "policies" / domain
    d.mkdir(parents=True, exist_ok=True)
    policy = {
        "version": "v1",
        "domain": {
            "slug": domain,
            "topic": f"Topic for {domain}",
            "description": f"Description for {domain}.",
        },
        "filter": {"threshold_include": 0.7},
        "inclusion_criteria": inclusion or [f"Discusses {domain}"],
        "exclusion_criteria": ["Off-topic content"],
    }
    p = d / "policy.yaml"
    p.write_text(yaml.safe_dump(policy, allow_unicode=True), encoding="utf-8")
    return p


def _write_moc(kb_root: Path, domain: str, *, with_links: bool = True) -> Path:
    d = kb_root / "wiki" / "mocs"
    d.mkdir(parents=True, exist_ok=True)
    front = {"type": "moc", "slug": domain, "domain": domain}
    if with_links:
        body = (
            "## Overview\n\n"
            "See [[entities/test-drug]] and [[concepts/test-mechanism]].\n"
            "Also [[entities/test-person]] and [[concepts/test-concept-2]].\n"
        )
    else:
        body = "## Overview\n\nProse only.\n"
    p = d / f"{domain}.md"
    p.write_text(fm.serialize(front, body), encoding="utf-8")
    return p


def _write_synthesis(kb_root: Path, domain: str, slug: str, title: str) -> Path:
    d = kb_root / "wiki" / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": title,
        "domains": [domain],
        "question": "Q?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 1,
        "synthesizes": ["sources/web-2026-01-01-abc"],
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "Body [[sources/web-2026-01-01-abc]].\n"))
    return p


# --- unit tests ----------------------------------------------------------------


def test_render_skill_includes_domain_name():
    content = _render_skill("test-domain", None, None)
    assert "test-domain" in content


def test_render_skill_under_max_lines():
    content = _render_skill("test-domain", None, None)
    assert len(content.splitlines()) <= _MAX_LINES


def test_render_skill_includes_inclusion_criteria():
    policy = {
        "domain": {"slug": "test", "topic": "Test"},
        "inclusion_criteria": ["Criterion A", "Criterion B"],
    }
    content = _render_skill("test", policy, None)
    assert "Criterion A" in content
    assert "Criterion B" in content


def test_render_skill_includes_entities_from_moc():
    moc_body = "Text [[entities/my-drug]] and [[entities/my-person]].\n"
    content = _render_skill("test", None, moc_body)
    assert "my-drug" in content
    assert "my-person" in content


def test_render_skill_includes_concepts_from_moc():
    moc_body = "Text [[concepts/food-noise]] and [[concepts/reward-blunting]].\n"
    content = _render_skill("test", None, moc_body)
    assert "food-noise" in content
    assert "reward-blunting" in content


# --- integration tests ---------------------------------------------------------


def test_skill_emit_creates_skill_file(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain")
    _write_moc(kb_root, "test-domain")

    result = skill_emit("test-domain")

    assert result.success
    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    assert skill_path.exists()


def test_skill_emit_content_has_frontmatter(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain")
    _write_moc(kb_root, "test-domain")
    skill_emit("test-domain")

    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    content = skill_path.read_text()
    assert content.startswith("---")
    assert "name: wiki-test-domain" in content


def test_skill_emit_includes_inclusion_criteria(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain", inclusion=["Must discuss test-topic"])
    _write_moc(kb_root, "test-domain")
    skill_emit("test-domain")

    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    content = skill_path.read_text()
    assert "Must discuss test-topic" in content


def test_skill_emit_includes_entities_and_concepts(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain")
    _write_moc(kb_root, "test-domain", with_links=True)
    skill_emit("test-domain")

    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    content = skill_path.read_text()
    assert "test-drug" in content
    assert "test-mechanism" in content


def test_skill_emit_includes_open_threads(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain")
    _write_moc(kb_root, "test-domain")
    _write_synthesis(kb_root, "test-domain", "test-synth", "My Open Thread")
    skill_emit("test-domain")

    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    content = skill_path.read_text()
    assert "My Open Thread" in content


def test_skill_emit_idempotent(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain")
    _write_moc(kb_root, "test-domain")

    r1 = skill_emit("test-domain")
    r2 = skill_emit("test-domain")

    assert r1.success and r2.success
    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    # Second call overwrites with same content — file still exists
    assert skill_path.exists()


def test_skill_emit_fails_without_policy_or_moc(kb_root: Path) -> None:
    result = skill_emit("nonexistent-domain")
    assert not result.success
    assert "nonexistent-domain" in result.errors[0]


def test_skill_emit_succeeds_with_policy_only(kb_root: Path) -> None:
    _write_policy(kb_root, "policy-only-domain")
    result = skill_emit("policy-only-domain")
    assert result.success


def test_skill_emit_output_under_max_lines(kb_root: Path) -> None:
    _write_policy(kb_root, "test-domain", inclusion=[f"Criterion {i}" for i in range(50)])
    _write_moc(kb_root, "test-domain")
    skill_emit("test-domain")

    skill_path = paths.knowledge_root() / ".claude" / "skills" / "wiki-test-domain" / "SKILL.md"
    lines = skill_path.read_text().splitlines()
    assert len(lines) <= _MAX_LINES
