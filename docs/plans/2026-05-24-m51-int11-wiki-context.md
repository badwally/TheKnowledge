# M51 — INT-11 `wiki context` read-side op Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a read-only outbound API for sibling projects (chief-of-staff, ai-tutor, newbiz) to pull wiki context programmatically. `wiki context <slug-or-query> [--depth N] [--format json|markdown] --caller "<id>"` resolves to a wiki page, walks `[[sources/X]]` and `[[entities/X]]` / `[[concepts/X]]` / `[[mocs/X]]` / `[[synthesis/X]]` wikilinks to depth N, and returns the assembled context block. Slug-or-query falls back to title-substring matching when the slug doesn't resolve directly. Caller arg is required for observability — every call lands in `log.md`.

**Architecture:** Single new op module `gateway.ops.context_op` containing three focused helpers — `_resolve_target` (slug → path with title-fuzzy fallback), `_walk_neighbors` (BFS over wikilinks to depth N, with cycle avoidance), `_render` (markdown or JSON envelope) — plus the public `context_op` orchestrator returning `OperationResult`. CLI + MCP surface in the usual K2 parity pattern.

**Tech Stack:** Python 3.12, existing `gateway.frontmatter` / `gateway.paths` / `gateway.log` / `gateway.core.OperationResult`, `pytest`. No new dependencies.

---

## Background

**Why purely additive.** This is a read-only outbound op. No mutation to wiki/ or raw/. The hard rule about gateway-mediated writes doesn't apply — we're handing OUT data, not writing it in.

**Why caller is required.** The review (§ INT-11 acceptance) calls it out: every context fetch logs `caller=<...>` so the operator can see which sibling project is pulling what, how often, at what depth. Observability beats freedom-of-anonymous-access for a substrate this young.

**Why title-fuzzy fallback (option B).** Pure slug-only (option A) forces every consumer to know exact slugs. Pure semantic search (option C) requires a search index the project doesn't have yet. Title-substring is the cheap middle ground: ~30 lines, no infrastructure, gracefully falls through to "no match" or "ambiguous — try one of these candidates".

**Why markdown default.** The dominant consumer is LLM context-loading. Markdown concatenation is what an LLM wants. JSON is the structured option for non-LLM callers (analysis scripts, dashboards).

---

## File Structure

**Create:**
- `src/gateway/ops/context_op.py` — single-file op (resolver + walker + renderer + `context_op` orchestrator)
- `tests/gateway/test_context_op.py` — ~12 tests

**Modify:**
- `src/gateway/cli.py` — add `context` subcommand
- `src/gateway/mcp_server.py` — add `wiki_context` MCP tool (K2 parity)
- `WIKI.md` — Gateway Operations table row
- `BUILD.md` — append M51 row to § 10
- `docs/milestones/M51.md` — milestone delivery doc

**Test count target:** 965 → ≥ 977 (≈ 12 new tests).

---

## Open Decisions (resolved before plan write)

1. **Slug-or-query strategy** — B (slug + title-substring fallback). Multi-match returns an actionable error listing the top 5 candidates.
2. **Default format** — markdown. `--format json` opts into structured envelope.
3. **Default depth** — 1. The page + its directly-cited neighbors.
4. **Wikilink types followed** — `sources`, `entities`, `concepts`, `mocs`, `synthesis`. NotebookLM corpus refs (`[[nlm:<uuid>]]`) are NOT followed (they're opaque NLM-internal refs, no on-disk target).
5. **Anchor handling** — strip `#anchor` from wikilink targets before resolving (e.g. `[[sources/X#para3]]` resolves to `wiki/sources/X.md`).
6. **Wikilink display-text handling** — extract the target before `|` (e.g. `[[mocs/agentic|Agentic Protocols]]` → `mocs/agentic`).
7. **Missing wikilink targets** — skip silently. A broken wikilink doesn't fail the whole call.
8. **Cycle avoidance** — BFS with a `visited: set[Path]` so cycles between pages don't infinite-loop.
9. **`caller` arg** — REQUIRED. Empty string or missing → error. Logged verbatim.
10. **Logging** — every call appends to `log.md` with `op=context, caller=<...>, target=..., depth=N, format=..., pages_returned=N`. Counts as a "touched" path in OperationResult.paths_touched.

---

# Phase A — Resolver + Walker

### Task A1: Failing tests for `_resolve_target`

Create `tests/gateway/test_context_op.py` with the test scaffolding + first set of resolver tests:

```python
"""Tests for the wiki context op (M51 INT-11)."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway.ops.context_op import (
    _resolve_target,
    _walk_neighbors,
    _render_markdown,
    _render_json,
    context_op,
    AmbiguousQueryError,
    NoMatchError,
)


def _write_page(kb_root: Path, kind: str, slug: str, title: str = "",
                body: str = "") -> Path:
    page = kb_root / "wiki" / kind / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {"type": kind.rstrip("s") or kind, "slug": slug,
         "title": title or slug, "domains": ["test-domain"]},
        body or f"# {slug}\n\nBody for {slug}.\n",
    ))
    return page


def test_resolve_target_by_slug_prefixed(kb_root):
    _write_page(kb_root, "entities", "alpha-co")
    p = _resolve_target("entities/alpha-co")
    assert p == kb_root / "wiki" / "entities" / "alpha-co.md"


def test_resolve_target_by_full_path(kb_root):
    _write_page(kb_root, "entities", "alpha-co")
    p = _resolve_target("wiki/entities/alpha-co.md")
    assert p == kb_root / "wiki" / "entities" / "alpha-co.md"


def test_resolve_target_by_title_substring_fallback(kb_root):
    _write_page(kb_root, "entities", "alpha-co", title="Alpha Corporation Inc")
    p = _resolve_target("Alpha Corporation")
    assert p == kb_root / "wiki" / "entities" / "alpha-co.md"


def test_resolve_target_ambiguous_title_raises(kb_root):
    _write_page(kb_root, "entities", "alpha-1", title="Alpha")
    _write_page(kb_root, "entities", "alpha-2", title="Alpha (other)")
    with pytest.raises(AmbiguousQueryError) as excinfo:
        _resolve_target("Alpha")
    assert "alpha-1" in str(excinfo.value)
    assert "alpha-2" in str(excinfo.value)


def test_resolve_target_no_match_raises(kb_root):
    with pytest.raises(NoMatchError):
        _resolve_target("definitely-does-not-exist")
```

Run: `.venv/bin/pytest tests/gateway/test_context_op.py -v` — expect ImportError.

### Task A2: Implement the resolver

Create `src/gateway/ops/context_op.py` with at minimum:

```python
"""`wiki context` — read-side outbound op (M51 INT-11).

Resolves a slug-or-query to a wiki page, walks wikilinks to depth N,
returns the assembled context. Read-only — no wiki/ or raw/ mutation.
"""

from __future__ import annotations

from pathlib import Path
import json
import re

from gateway import frontmatter as fm
from gateway import log, paths
from gateway.core import OperationResult


class NoMatchError(LookupError):
    """The slug-or-query didn't resolve to any wiki page."""


class AmbiguousQueryError(LookupError):
    """Title-substring matched >1 page; query needs to be more specific."""


_PAGE_KINDS = ("entities", "concepts", "mocs", "synthesis", "sources")
# Wikilinks followed during expansion. nlm:<uuid> excluded (opaque corpus refs).
_FOLLOWABLE_PREFIXES = ("sources/", "entities/", "concepts/", "mocs/", "synthesis/")
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def _resolve_target(query: str) -> Path:
    """Resolve `query` to a wiki page path.

    Tries, in order:
    1. As a literal path (with or without `wiki/` prefix and `.md` suffix).
    2. As a `<kind>/<slug>` reference (e.g. "entities/alpha-co").
    3. Title-substring fallback: case-insensitive match against frontmatter
       `title:` across `_PAGE_KINDS`. Multi-match → AmbiguousQueryError
       (listing up to 5 candidates). Zero match → NoMatchError.
    """
    kb_root = paths.knowledge_root()
    q = query.strip()

    # 1. literal path
    for candidate in (
        kb_root / q,
        kb_root / (q + ".md"),
        kb_root / "wiki" / q,
        kb_root / "wiki" / (q + ".md"),
    ):
        if candidate.is_file() and candidate.suffix == ".md":
            return candidate

    # 2. <kind>/<slug>
    if "/" in q and not q.startswith("wiki/"):
        candidate = kb_root / "wiki" / (q + ".md" if not q.endswith(".md") else q)
        if candidate.is_file():
            return candidate

    # 3. title-substring fallback
    needle = q.lower()
    matches: list[Path] = []
    for kind in _PAGE_KINDS:
        d = kb_root / "wiki" / kind
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                front, _ = fm.parse(p.read_text())
            except fm.FrontmatterError:
                continue
            title = str(front.get("title") or "").lower()
            if needle in title:
                matches.append(p)
    if len(matches) == 0:
        raise NoMatchError(
            f"no wiki page matched {query!r} (tried path lookup + title-substring)"
        )
    if len(matches) > 1:
        preview = "\n".join(
            f"  - {p.relative_to(kb_root)}"
            for p in matches[:5]
        )
        raise AmbiguousQueryError(
            f"query {query!r} matched {len(matches)} pages; be more specific. "
            f"top candidates:\n{preview}"
        )
    return matches[0]
```

Re-run A1 tests — expect 5 PASS.

### Task A3: Failing tests for `_walk_neighbors`

Add to the same test file:

```python
def test_walk_depth_zero_returns_root_only(kb_root):
    root = _write_page(kb_root, "entities", "root-page")
    visited = _walk_neighbors(root, depth=0)
    assert visited == [root]


def test_walk_depth_one_follows_wikilinks(kb_root):
    src = _write_page(kb_root, "sources", "web-2026-01-01-aaa", title="Src",
                      body="# Src\n\nBody.\n")
    other = _write_page(kb_root, "entities", "other-entity", title="Other",
                        body="# Other\n\nBody.\n")
    root = _write_page(
        kb_root, "concepts", "rooty",
        body="# rooty\n\nMentions [[sources/web-2026-01-01-aaa]] and [[entities/other-entity]].\n",
    )

    visited = _walk_neighbors(root, depth=1)
    assert root in visited
    assert src in visited
    assert other in visited


def test_walk_skips_missing_targets(kb_root):
    root = _write_page(
        kb_root, "concepts", "rooty",
        body="# rooty\n\nMentions [[sources/does-not-exist]].\n",
    )
    visited = _walk_neighbors(root, depth=1)
    # Only the root; missing target silently skipped
    assert visited == [root]


def test_walk_avoids_cycles(kb_root):
    a = _write_page(kb_root, "concepts", "a-loop",
                    body="# a\n\n[[concepts/b-loop]]\n")
    b = _write_page(kb_root, "concepts", "b-loop",
                    body="# b\n\n[[concepts/a-loop]]\n")
    visited = _walk_neighbors(a, depth=5)
    # Both visited exactly once
    assert visited.count(a) == 1
    assert visited.count(b) == 1


def test_walk_strips_anchor_and_display_text(kb_root):
    target = _write_page(kb_root, "sources", "web-foo", title="Foo source")
    root = _write_page(
        kb_root, "concepts", "rooty",
        body="# rooty\n\n[[sources/web-foo#para3]] and [[sources/web-foo|Foo Display]].\n",
    )
    visited = _walk_neighbors(root, depth=1)
    assert target in visited
    # Visited once despite two references
    assert visited.count(target) == 1


def test_walk_does_not_follow_nlm_corpus_refs(kb_root):
    root = _write_page(
        kb_root, "synthesis", "rooty",
        body="# rooty\n\n[[nlm:a17f0b4f-ba96-46b0-b4e1-6be759219e89]]\n",
    )
    visited = _walk_neighbors(root, depth=1)
    # Only the root; nlm refs not followed
    assert visited == [root]
```

### Task A4: Implement `_walk_neighbors`

```python
def _walk_neighbors(start: Path, depth: int) -> list[Path]:
    """BFS over wikilinks starting at `start`, up to `depth` hops.

    Returns a deduplicated list of pages in visit order (root first).
    Missing wikilink targets are silently skipped. Cycles are avoided
    via a visited set.
    """
    kb_root = paths.knowledge_root()
    visited: list[Path] = []
    seen: set[Path] = set()
    frontier: list[tuple[Path, int]] = [(start, 0)]

    while frontier:
        page, d = frontier.pop(0)
        if page in seen:
            continue
        seen.add(page)
        visited.append(page)

        if d >= depth:
            continue
        try:
            _, body = fm.parse(page.read_text())
        except fm.FrontmatterError:
            continue
        for target in _extract_wikilink_targets(body):
            resolved = _resolve_wikilink(kb_root, target)
            if resolved is not None and resolved not in seen:
                frontier.append((resolved, d + 1))
    return visited


def _extract_wikilink_targets(body: str) -> list[str]:
    """Find `[[<target>]]` patterns and return the bare target (no anchor,
    no display text) for those starting with a followable prefix."""
    out: list[str] = []
    for m in _WIKILINK_RE.finditer(body):
        target = m.group(1).strip()
        if any(target.startswith(p) for p in _FOLLOWABLE_PREFIXES):
            out.append(target)
    return out


def _resolve_wikilink(kb_root: Path, target: str) -> Path | None:
    """`<kind>/<slug>` → `wiki/<kind>/<slug>.md` if it exists, else None."""
    if not any(target.startswith(p) for p in _FOLLOWABLE_PREFIXES):
        return None
    candidate = kb_root / "wiki" / f"{target}.md"
    return candidate if candidate.is_file() else None
```

Run all resolver + walker tests — expect 11 PASS.

### Task A5: Commit Phase A

```bash
.venv/bin/pytest tests/ -q --tb=no | tail -3
git add src/gateway/ops/context_op.py tests/gateway/test_context_op.py
git commit -m "feat(m51): wiki context resolver + walker (read-side INT-11 phase A)"
```

---

# Phase B — Renderer + main op

### Task B1: Failing tests for renderers

```python
def test_render_markdown_emits_one_section_per_page(kb_root):
    a = _write_page(kb_root, "entities", "a-ent", body="# A\n\nBody A.\n")
    b = _write_page(kb_root, "sources", "src-x", body="# X\n\nBody X.\n")
    text = _render_markdown([a, b])
    assert "wiki/entities/a-ent.md" in text
    assert "wiki/sources/src-x.md" in text
    assert "Body A" in text
    assert "Body X" in text


def test_render_json_returns_structured_envelope(kb_root):
    a = _write_page(kb_root, "entities", "a-ent", title="Alpha", body="# A\n\nBody A.\n")
    b = _write_page(kb_root, "sources", "src-x", title="Src X", body="# X\n\nBody X.\n")
    blob = _render_json([a, b])
    data = json.loads(blob)
    assert data["root"]["path"].endswith("entities/a-ent.md")
    assert data["root"]["slug"] == "a-ent"
    assert len(data["neighbors"]) == 1
    assert data["neighbors"][0]["slug"] == "src-x"
```

### Task B2: Implement renderers

```python
def _render_markdown(pages: list[Path]) -> str:
    parts = []
    kb_root = paths.knowledge_root()
    for p in pages:
        rel = p.relative_to(kb_root)
        try:
            front, body = fm.parse(p.read_text())
        except fm.FrontmatterError:
            front, body = {}, p.read_text()
        title = front.get("title") or front.get("slug") or p.stem
        parts.append(f"## {rel} — {title}\n\n{body.rstrip()}")
    return "\n\n---\n\n".join(parts)


def _render_json(pages: list[Path]) -> str:
    kb_root = paths.knowledge_root()

    def _page_obj(p: Path) -> dict:
        try:
            front, body = fm.parse(p.read_text())
        except fm.FrontmatterError:
            front, body = {}, p.read_text()
        return {
            "path": str(p.relative_to(kb_root)),
            "slug": str(front.get("slug") or p.stem),
            "title": str(front.get("title") or ""),
            "kind": str(front.get("type") or p.parent.name.rstrip("s")),
            "body": body,
        }

    if not pages:
        return json.dumps({"root": None, "neighbors": []})
    return json.dumps({
        "root": _page_obj(pages[0]),
        "neighbors": [_page_obj(p) for p in pages[1:]],
    }, indent=2)
```

### Task B3: `context_op` orchestrator + tests

```python
def context_op(query: str, *,
               depth: int = 1,
               fmt: str = "markdown",
               caller: str | None = None) -> OperationResult:
    if not caller:
        return OperationResult(
            success=False,
            errors=["--caller is required (free-form identifier; logged to log.md)"],
        )
    if fmt not in ("markdown", "json"):
        return OperationResult(
            success=False,
            errors=[f"--format must be 'markdown' or 'json', got {fmt!r}"],
        )
    if depth < 0:
        return OperationResult(
            success=False,
            errors=[f"--depth must be >= 0, got {depth}"],
        )

    try:
        root = _resolve_target(query)
    except (NoMatchError, AmbiguousQueryError) as e:
        return OperationResult(success=False, errors=[str(e)])

    pages = _walk_neighbors(root, depth=depth)
    rendered = _render_markdown(pages) if fmt == "markdown" else _render_json(pages)

    log.append(
        op="context",
        fields={
            "caller": caller,
            "target": str(root.relative_to(paths.knowledge_root())),
            "depth": depth,
            "format": fmt,
            "pages_returned": len(pages),
        },
        summary=(
            f"context: caller={caller!r} target={root.relative_to(paths.knowledge_root())} "
            f"depth={depth} pages={len(pages)}"
        ),
    )
    return OperationResult(
        success=True,
        paths_touched=[paths.log_path()],
        summary=rendered,
    )
```

Tests:

```python
def test_context_op_requires_caller(kb_root):
    result = context_op("anything")
    assert not result.success
    assert "caller" in (result.errors[0]).lower()


def test_context_op_rejects_invalid_format(kb_root):
    _write_page(kb_root, "entities", "e1")
    result = context_op("entities/e1", caller="test", fmt="yaml")
    assert not result.success
    assert "format" in (result.errors[0]).lower()


def test_context_op_returns_markdown_summary_for_a_page(kb_root):
    _write_page(kb_root, "entities", "alpha-co", title="Alpha", body="# Alpha\n\nDetails.\n")
    result = context_op("entities/alpha-co", caller="test-caller")
    assert result.success
    assert "Alpha" in result.summary
    assert "Details" in result.summary


def test_context_op_logs_caller(kb_root):
    _write_page(kb_root, "entities", "alpha-co")
    context_op("entities/alpha-co", caller="chief-of-staff")
    log_text = (kb_root / "log.md").read_text()
    assert "caller='chief-of-staff'" in log_text or 'caller="chief-of-staff"' in log_text
```

### Task B4: Commit Phase B

```bash
.venv/bin/pytest tests/gateway/test_context_op.py -v
.venv/bin/pytest tests/ -q --tb=no | tail -3
git add src/gateway/ops/context_op.py tests/gateway/test_context_op.py
git commit -m "feat(m51): wiki context — renderers + orchestrator (read-side phase B)"
```

---

# Phase C — CLI + MCP + commit

### Task C1: Wire `wiki context` into the CLI

In `src/gateway/cli.py`:

1. Add to `SUBCOMMANDS`:
   ```python
   "context": "Read-only fetch of a wiki page + N-hop wikilink-resolved neighbors (M51, INT-11)",
   ```
2. Add `"context"` to `IMPLEMENTED`.
3. Argparse:
   ```python
   p_context = subparsers.add_parser("context", help=SUBCOMMANDS["context"])
   p_context.add_argument("query", help="Slug, path, or title substring.")
   p_context.add_argument("--depth", type=int, default=1)
   p_context.add_argument("--format", choices=["markdown", "json"], default="markdown")
   p_context.add_argument("--caller", required=True,
                          help="Free-form caller identifier (logged to log.md).")
   ```
4. Dispatch helper `_run_context(ns)` calling `gateway.ops.context_op.context_op(...)`.

Sanity check: `wiki context --help`. Then a real call: `wiki context entities/<some-slug> --caller smoke-test --depth 0`.

### Task C2: MCP parity tool

In `src/gateway/mcp_server.py` add `wiki_context(query, depth=1, format="markdown", caller=None)` mirroring the CLI. Wire to `context_op`. Run `pytest tests/gateway/test_mcp_parity.py`.

### Task C3: Commit Phase C

```bash
.venv/bin/pytest tests/ -q --tb=no | tail -3
git add src/gateway/cli.py src/gateway/mcp_server.py
git commit -m "feat(m51): wire wiki context CLI + MCP parity"
```

---

# Phase D — Hand-test + docs + tag

### Task D1: Hand-test

Pick a real wiki page (e.g. `wiki/synthesis/2026-05-09-how-do-the-major-u-s.md`) and run:

```
.venv/bin/wiki context "synthesis/2026-05-09-how-do-the-major-u-s" --caller m51-handtest --depth 1 --format json | head -50
.venv/bin/wiki context "synthesis/2026-05-09-how-do-the-major-u-s" --caller m51-handtest --depth 2 | wc -c
```

Confirm:
1. Depth-1 returns the page + its directly-cited neighbors.
2. Depth-2 is larger than depth-1.
3. Log entries appear in `log.md` with `caller='m51-handtest'`.
4. JSON envelope parses cleanly: `wiki context ... --format json | jq .`.

### Task D2: WIKI.md + BUILD.md + M51.md

Same pattern as M49/M50. Append a row to WIKI.md ops table, add M51 row to BUILD.md § 10, create `docs/milestones/M51.md` mirroring M50.md's shape (goal, components, modules, test delta, acceptance, hand-test results, follow-ups).

### Task D3: Tag + push

```
.venv/bin/pytest tests/ -q --tb=no | tail -3
git tag m51-int11-wiki-context
git push origin main
git push origin m51-int11-wiki-context
```

---

## Self-Review

1. **Spec coverage:** resolver ✓ (A1-A2), walker ✓ (A3-A4), Phase A commit ✓ (A5), renderers + orchestrator + tests ✓ (B1-B3), Phase B commit ✓ (B4), CLI ✓ (C1), MCP ✓ (C2), hand-test ✓ (D1), docs ✓ (D2-D3).
2. **Placeholder scan:** none.
3. **Type consistency:** `Path` everywhere for filesystem refs; `str` for queries / formats / captions. `OperationResult` shape preserved.
4. **Known unknowns:**
   - Wikilink regex may not handle all edge cases (e.g. wikilinks inside code fences, escape sequences). Punt — fix-on-demand.
   - Title-substring is case-insensitive but otherwise dumb. A user typing "alpha" matching both "Alpha Corp" and "alphabet" would be ambiguous. Acceptable for v1.
   - Depth=2+ may pull a lot of content for dense synthesis pages. v1 has no max_chars guard (unlike M50 wiki_context). Add if a hand-test surfaces a content-budget concern.

---

## Execution Handoff

Plan saved. Two options:
1. **Subagent-driven (recommended)** — same protocol as M49/M50.
2. **Inline** — execute in this session.

Which?
