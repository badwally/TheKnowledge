"""Tests for `wiki discover-domains` — bottom-up cluster discovery (M36)."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.discover_domains import discover_domains


class StubPlanClient:
    def __init__(self, response: str):
        self.response = response
        self.last_prompt: str | None = None
        self.call_count = 0

    def call(self, prompt: str) -> str:
        self.last_prompt = prompt
        self.call_count += 1
        return self.response


def _seed_source_page(
    *,
    source_id: str,
    title: str,
    summary: str = "Body content for the source.",
    domains: list[str] | None = None,
    source_type: str = "pdf",
    ingested_at: str | None = None,
):
    """Write a wiki/sources/<id>.md file with the given metadata."""
    front = {
        "type": "source",
        "source_id": source_id,
        "source_type": source_type,
        "title": title,
        "ingested_at": ingested_at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    if domains is not None:
        front["domains"] = domains
    body = (
        f"# {title}\n\n"
        f"## Summary\n\n{summary}\n\n"
        f"## Key claims\n\n- Placeholder claim\n\n"
        f"## Cross-references\n\n- (none)\n"
    )
    page = paths.wiki_dir() / "sources" / f"{source_id}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(front, body))
    return page


def _proposal_content(
    *,
    slug: str,
    title: str,
    proposed_domain: str,
    member_sources: list[str],
    rationale: str = "Cluster identified from source titles and summaries.",
) -> str:
    front = {
        "type": "domain-proposal",
        "slug": slug,
        "title": title,
        "proposed_domain": proposed_domain,
        "status": "draft",
        "member_sources": member_sources,
        "rationale": rationale,
    }
    refs = "\n".join(f"- [[sources/{sid}]]: member" for sid in member_sources)
    body = (
        f"# {title}\n\n"
        f"## Rationale\n\n{rationale}\n\n"
        f"## Member sources\n\n{refs}\n"
    )
    return fm.serialize(front, body)


def _plan_response(updates: list[dict]) -> str:
    return json.dumps(
        {
            "source_id": "discover-test",
            "rationale": "stub clustering",
            "updates": updates,
        }
    )


# --- empty corpus -----------------------------------------------------------


def test_discover_domains_no_sources_returns_no_op(kb_root):
    client = StubPlanClient(response="should-not-be-called")
    result = discover_domains(client=client)
    assert result.success
    assert result.no_op
    assert client.call_count == 0


# --- happy path -------------------------------------------------------------


def test_discover_domains_files_proposals_via_plan(kb_root):
    _seed_source_page(source_id="pdf-aaa", title="GLP-1 receptor agonists in obesity")
    _seed_source_page(source_id="pdf-bbb", title="Semaglutide cardiovascular outcomes")
    _seed_source_page(source_id="pdf-ccc", title="Wyckoff Volume Spread Analysis")
    _seed_source_page(source_id="pdf-ddd", title="Tape reading patterns for day trading")

    proposal_a = _proposal_content(
        slug="proposal-glp1-metabolism",
        title="GLP-1 and metabolic medicine",
        proposed_domain="glp1-metabolism",
        member_sources=["pdf-aaa", "pdf-bbb"],
    )
    proposal_b = _proposal_content(
        slug="proposal-trading-mechanics",
        title="Trading mechanics: Wyckoff and tape reading",
        proposed_domain="trading-mechanics",
        member_sources=["pdf-ccc", "pdf-ddd"],
    )
    response = _plan_response(
        [
            {
                "target_path": "wiki/proposals/proposal-glp1-metabolism.md",
                "update_kind": "create",
                "content": proposal_a,
            },
            {
                "target_path": "wiki/proposals/proposal-trading-mechanics.md",
                "update_kind": "create",
                "content": proposal_b,
            },
        ]
    )
    client = StubPlanClient(response=response)
    result = discover_domains(client=client)

    assert result.success, result.errors
    assert client.call_count == 1
    # Prompt embeds candidate source titles
    assert "GLP-1 receptor agonists in obesity" in client.last_prompt
    assert "Wyckoff Volume Spread Analysis" in client.last_prompt
    # Proposal pages exist on disk
    assert (paths.wiki_dir() / "proposals" / "proposal-glp1-metabolism.md").exists()
    assert (paths.wiki_dir() / "proposals" / "proposal-trading-mechanics.md").exists()


# --- filters ----------------------------------------------------------------


def test_discover_domains_untagged_filter_skips_already_tagged_sources(kb_root):
    _seed_source_page(source_id="pdf-untagged", title="Untagged source", domains=[])
    _seed_source_page(
        source_id="pdf-tagged", title="Tagged source", domains=["existing-domain"]
    )

    response = _plan_response([])  # not enough candidates → no proposals
    client = StubPlanClient(response=response)
    discover_domains(untagged=True, client=client)

    assert client.last_prompt is not None
    assert "Untagged source" in client.last_prompt
    assert "Tagged source" not in client.last_prompt


def test_discover_domains_scope_glob_restricts_candidates(kb_root):
    _seed_source_page(source_id="pdf-keep", title="In-scope PDF source")
    _seed_source_page(source_id="yt-skip", title="Out-of-scope YouTube source")

    response = _plan_response([])
    client = StubPlanClient(response=response)
    discover_domains(scope="wiki/sources/pdf-*", client=client)

    assert "In-scope PDF source" in client.last_prompt
    assert "Out-of-scope YouTube source" not in client.last_prompt


# --- atomicity --------------------------------------------------------------


def test_discover_domains_atomicity_when_one_proposal_invalid(kb_root):
    _seed_source_page(source_id="pdf-aaa", title="A")
    _seed_source_page(source_id="pdf-bbb", title="B")

    valid_proposal = _proposal_content(
        slug="proposal-valid",
        title="Valid cluster",
        proposed_domain="valid-cluster",
        member_sources=["pdf-aaa"],
    )
    # Invalid: missing required field `proposed_domain` in frontmatter
    invalid_front = {
        "type": "domain-proposal",
        "slug": "proposal-broken",
        "title": "Broken cluster",
        "status": "draft",
        "member_sources": ["pdf-bbb"],
        "rationale": "broken proposal",
    }
    invalid_body = (
        "# Broken cluster\n\n## Rationale\n\nbroken\n\n## Member sources\n\n- [[sources/pdf-bbb]]\n"
    )
    invalid_proposal = fm.serialize(invalid_front, invalid_body)

    response = _plan_response(
        [
            {
                "target_path": "wiki/proposals/proposal-valid.md",
                "update_kind": "create",
                "content": valid_proposal,
            },
            {
                "target_path": "wiki/proposals/proposal-broken.md",
                "update_kind": "create",
                "content": invalid_proposal,
            },
        ]
    )
    client = StubPlanClient(response=response)
    result = discover_domains(client=client)

    assert not result.success
    assert any("proposed_domain" in e for e in result.errors)
    # Atomicity: even the valid proposal must NOT be on disk
    assert not (paths.wiki_dir() / "proposals" / "proposal-valid.md").exists()
    assert not (paths.wiki_dir() / "proposals" / "proposal-broken.md").exists()
