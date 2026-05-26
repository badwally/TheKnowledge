"""`wiki` CLI entry point.

Implemented at the current milestone: ingest, filter, filter-correct.
Other subcommands print "not yet implemented" and exit 2 until their
milestone lands. See BUILD.md.
"""

import argparse
import sys
from pathlib import Path

import argcomplete

from gateway import __version__


SUBCOMMANDS: dict[str, str] = {
    "ingest": "Ingest a single source (path or URL) into the canonical wiki",
    "batch-ingest": "Ingest a whole vault or directory; supports --legacy-import",
    "query": "Query the wiki; may invoke NotebookLM for large-corpus questions",
    "filter": "Run the semantic filter on a candidate source (read-only)",
    "filter-correct": "Override a past filter decision; pin as a corrected example",
    "backfill-examples": "Populate policy.yaml + example bank from legacy research-notebook artifacts",
    "finetune": "Inspect or distill the per-domain example bank into a tighter policy candidate",
    "nlm-add": "Add a source to a NotebookLM corpus",
    "nlm-sync": "Sync every raw source tagged with a domain into its NotebookLM corpus",
    "nlm-slides": "Generate a slide deck from a NotebookLM corpus; file as wiki artifact",
    "nlm-audio": "Generate an audio overview; file as wiki artifact",
    "nlm-briefing": "Generate a briefing doc; file as wiki artifact",
    "nlm-revise": "Revise an existing NotebookLM artifact",
    "finalize": "Finalize a draft page (re-run validator with citation rule restored)",
    "finalize-batch": "Batch-finalize stale drafts (dry-run by default; --execute to apply; --suggest enables LLM cite-suggest for Cat B)",
    "cite": "Add [[sources/<id>]] citation tokens to specific lines of a wiki page",
    "cite-add": "Add a citation by claim text (resolves to a line via escalation: exact → normalized → optional --fuzzy)",
    "edit": "Replace the body of one named section in a wiki page (constrained, validator-checked)",
    "concept-add": "Author a wiki/concepts/<slug>.md page from a markdown body",
    "lint": "Run health checks across the wiki",
    "index": "Rebuild or update the content index",
    "search": "Search wiki + raw sources",
    "status": "Show recent activity, watcher state, pending queues",
    "migrate": "Apply a schema or content migration script",
    "mcp-serve": "Start the MCP server exposing gateway operations as native tools",
    "watch": "Run the inbox watcher daemon in the foreground (used by launchd)",
    "discover-domains": "Cluster source pages into draft domain proposals (M36)",
    "promote-domain": "Bless a draft domain proposal: write policy + back-tag sources",
    "demote-domain": "Reverse a promotion: remove tags + delete auto-generated policy",
    "reject-proposal": "Delete a draft domain proposal",
    "research": "Corpus-constructive research: fan out search, filter, build a NotebookLM session, file syntheses",
    "bootstrap-domain": "Author a starter policy.yaml from a natural-language domain description",
    "serve": "Start the local web UI (FastAPI + React)",
    "poll": "Run a registered poller (e.g. apple-notes) to fetch new items into raw/",
    "schedule": "Manage cron-driven scheduled jobs (list/add/remove/enable/disable/run/dry-run)",
    "auth": "Manage bearer tokens for /api/ingest (add/list/revoke) — K3 cloud shim",
    "evaluate": "Run per-domain evaluation (M50): scores wiki content against golden Q/A pairs at .knowledge/eval/<domain>/goldens.yaml",
    "context": "Read-only fetch of a wiki page + N-hop wikilink-resolved neighbors (M51, INT-11)",
    "agent-log": "Show per-agent event counts and top payloads (AGT-14)",
    "contradiction": "List or resolve structured contradiction pages (QUAL-3)",
    "triage": "Manage the inbox-triage review queue (AGT-1)",
    "draft-close": "Run the draft-closer agent: auto-finalize easy wins, escalate hard cases (AGT-2)",
    "agents": "Run a named agent (inbox-triage | draft-closer | agent-digest) on demand or from the scheduler",
}

IMPLEMENTED: set[str] = {
    "ingest",
    "filter",
    "filter-correct",
    "backfill-examples",
    "finetune",
    "status",
    "watch",
    "nlm-add",
    "nlm-sync",
    "nlm-slides",
    "nlm-audio",
    "nlm-briefing",
    "nlm-revise",
    "finalize",
    "finalize-batch",
    "cite",
    "cite-add",
    "edit",
    "concept-add",
    "query",
    "mcp-serve",
    "batch-ingest",
    "lint",
    "discover-domains",
    "promote-domain",
    "demote-domain",
    "reject-proposal",
    "research",
    "bootstrap-domain",
    "serve",
    "poll",
    "schedule",
    "auth",
    "evaluate",
    "context",
    "agent-log",
    "contradiction",
    "triage",
    "draft-close",
    "agents",
}


def _not_yet_implemented(subcommand: str) -> int:
    print(
        f"`wiki {subcommand}` is not yet implemented at the current milestone.\n"
        f"See BUILD.md for the milestone that lands this command.",
        file=sys.stderr,
    )
    return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wiki",
        description=(
            "Gateway for the canonical knowledge base at ~/code/knowledge/. "
            "All operations on raw/ and wiki/ go through this CLI or the matching MCP tools. "
            "See WIKI.md for the contract."
        ),
    )
    parser.add_argument("--version", action="version", version=f"wiki {__version__}")

    subparsers = parser.add_subparsers(dest="subcommand", metavar="<subcommand>")

    # ingest
    p_ingest = subparsers.add_parser(
        "ingest",
        help=SUBCOMMANDS["ingest"],
        epilog=(
            "Examples:\n"
            "  wiki ingest https://arxiv.org/abs/2301.07041 --domain glp1\n"
            "  wiki ingest raw/pdf/some-paper.md --with-plan --domain glp1\n"
            "  wiki ingest https://www.youtube.com/watch?v=abc123 --draft"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_ingest.add_argument("input", help="URL or path to canonical markdown source")
    p_ingest.add_argument("--domain", default=None, help="Domain slug for filter scoring")
    p_ingest.add_argument(
        "--with-plan",
        action="store_true",
        help="Invoke the wiki authorship agent to update entity/concept/synthesis pages",
    )
    p_ingest.add_argument(
        "--draft",
        action="store_true",
        help="Allow partial citations on agent-generated pages; mark as draft",
    )
    p_ingest.add_argument(
        "--plan-timeout",
        type=float,
        default=None,
        help="Plan-client wall-clock budget in seconds (default 300; bump for "
        "large source bodies — 50KB+ PDFs often need 600+).",
    )

    # filter (read-only scoring)
    p_filter = subparsers.add_parser(
        "filter",
        help=SUBCOMMANDS["filter"],
        epilog=(
            "Examples:\n"
            "  wiki filter https://arxiv.org/abs/2301.07041 --domain glp1\n"
            "  wiki filter raw/web/some-article.md"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_filter.add_argument("input", help="URL or path to a source to score")
    p_filter.add_argument("--domain", default=None, help="Domain slug for the policy to apply")

    # filter-correct
    p_correct = subparsers.add_parser("filter-correct", help=SUBCOMMANDS["filter-correct"])
    p_correct.add_argument("source_id", help="Source id (e.g., yt-LfRiBJgD7sk)")
    decision = p_correct.add_mutually_exclusive_group(required=True)
    decision.add_argument("--include", action="store_true", help="Override decision to include")
    decision.add_argument("--exclude", action="store_true", help="Override decision to exclude")
    p_correct.add_argument("--rationale", required=True, help="Why the original decision was wrong")
    p_correct.add_argument("--domain", default=None, help="Domain slug if not in source frontmatter")

    # status (no args)
    p_status = subparsers.add_parser(
        "status",
        help=SUBCOMMANDS["status"],
        epilog=(
            "Examples:\n"
            "  wiki status\n"
            "  wiki status --cost"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_status.add_argument(
        "--cost",
        action="store_true",
        help="Include estimated USD cost in the 7-day LLM-usage block (K5)",
    )

    # watch (no args; runs foreground)
    subparsers.add_parser("watch", help=SUBCOMMANDS["watch"])

    # nlm-add: add a source (already in raw/) to a domain's NotebookLM corpus
    p_nlm_add = subparsers.add_parser("nlm-add", help=SUBCOMMANDS["nlm-add"])
    p_nlm_add.add_argument("domain", help="Domain slug")
    p_nlm_add.add_argument("source_id", help="Source id (e.g., yt-LfRiBJgD7sk)")

    # nlm-sync: bulk-add every raw source tagged with a domain into its corpus
    p_nlm_sync = subparsers.add_parser("nlm-sync", help=SUBCOMMANDS["nlm-sync"])
    p_nlm_sync.add_argument("domain", help="Domain slug")
    p_nlm_sync.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Process at most N sources (useful for smoke-testing)",
    )
    p_nlm_sync.add_argument(
        "--dry-run",
        action="store_true",
        help="List sources that would be synced; do not call NotebookLM",
    )

    # nlm-slides
    p_nlm_slides = subparsers.add_parser("nlm-slides", help=SUBCOMMANDS["nlm-slides"])
    p_nlm_slides.add_argument("domain", help="Domain slug")
    p_nlm_slides.add_argument("topic", help="Slide deck topic / focus")

    # nlm-audio
    p_nlm_audio = subparsers.add_parser("nlm-audio", help=SUBCOMMANDS["nlm-audio"])
    p_nlm_audio.add_argument("domain", help="Domain slug")
    p_nlm_audio.add_argument("topic", help="Audio overview topic / focus")

    # nlm-briefing
    p_nlm_briefing = subparsers.add_parser("nlm-briefing", help=SUBCOMMANDS["nlm-briefing"])
    p_nlm_briefing.add_argument("domain", help="Domain slug")

    # nlm-revise: revise a slide deck (multiple --slide flags allowed)
    p_nlm_revise = subparsers.add_parser("nlm-revise", help=SUBCOMMANDS["nlm-revise"])
    p_nlm_revise.add_argument("artifact_slug", help="Slug of an existing slide artifact")
    p_nlm_revise.add_argument(
        "--slide",
        action="append",
        required=True,
        dest="slides",
        help="Slide revision: '<slide-num> <instruction>' (repeatable)",
    )

    # finalize: re-validate a draft page; clear draft flag if citations resolve
    p_finalize = subparsers.add_parser("finalize", help=SUBCOMMANDS["finalize"])
    p_finalize.add_argument(
        "page_path",
        help="Path to a draft page (relative to KNOWLEDGE_ROOT or absolute)",
    )
    p_finalize.add_argument(
        "--abandon",
        action="store_true",
        help="Delete the draft page and remove its backlinks instead of finalizing",
    )

    p_finalize_batch = subparsers.add_parser(
        "finalize-batch", help=SUBCOMMANDS["finalize-batch"]
    )
    p_finalize_batch.add_argument(
        "--domain",
        default=None,
        help="Restrict to drafts whose frontmatter `domains` includes this value.",
    )
    p_finalize_batch.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Process at most this many stale drafts.",
    )
    p_finalize_batch.add_argument(
        "--execute",
        action="store_true",
        help="Actually finalize (default is dry-run; no files modified).",
    )
    p_finalize_batch.add_argument(
        "--suggest",
        action="store_true",
        help="Run LLM cite-suggest on Cat B drafts. With --execute (Aggressive mode), auto-applies unambiguous + evidence-verified suggestions and finalizes.",
    )

    # evaluate: run per-domain evaluation (M50)
    p_evaluate = subparsers.add_parser(
        "evaluate",
        help=SUBCOMMANDS["evaluate"],
        epilog=(
            "Examples:\n"
            "  wiki evaluate glp1\n"
            "  wiki evaluate glp1 --limit 50\n"
            "  wiki evaluate --scaffold glp1"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_evaluate.add_argument("domain", nargs="?", default=None,
                            help="Domain to evaluate (omit when using --scaffold).")
    p_evaluate.add_argument("--limit", type=int, default=None,
                            help="Score at most this many goldens.")
    p_evaluate.add_argument("--scaffold", default=None, metavar="DOMAIN",
                            help="Write a template goldens.yaml for the named domain.")

    # context: read-only fetch of a wiki page + N-hop wikilink-resolved neighbors (M51, INT-11)
    p_context = subparsers.add_parser(
        "context",
        help=SUBCOMMANDS["context"],
        epilog=(
            "Examples:\n"
            "  wiki context food-noise --caller my-agent\n"
            "  wiki context food-noise --depth 2 --format json --caller eval-pipeline"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_context.add_argument("query", help="Slug, path, or title substring.")
    p_context.add_argument("--depth", type=int, default=1,
                           help="How many wikilink hops to follow (default 1).")
    p_context.add_argument("--format", choices=["markdown", "json"], default="markdown",
                           help="Output format (default markdown).")
    p_context.add_argument("--caller", required=True,
                           help="Free-form caller identifier (logged to log.md).")

    # cite: add [[sources/<id>]] citation tokens to specific lines of a wiki page
    p_cite = subparsers.add_parser("cite", help=SUBCOMMANDS["cite"])
    p_cite.add_argument(
        "page_path",
        help="Path to the wiki page to cite into (relative to KNOWLEDGE_ROOT or absolute)",
    )
    p_cite.add_argument(
        "additions",
        nargs="*",
        metavar="LINE:SOURCE_ID",
        help="One or more LINE:SOURCE_ID pairs (e.g., 26:web-2026-01-01-361). LINE is 1-indexed into the on-disk file. Omit when using --suggest.",
    )
    p_cite.add_argument(
        "--suggest",
        action="store_true",
        help="Use LLM to propose cite invocations (M49); emits stdout, does not modify the page.",
    )

    # cite-add: claim-text-driven citation insertion (K1)
    p_cite_add = subparsers.add_parser("cite-add", help=SUBCOMMANDS["cite-add"])
    p_cite_add.add_argument(
        "page_path",
        help="Path to the wiki page (relative to KNOWLEDGE_ROOT or absolute)",
    )
    p_cite_add.add_argument(
        "claim_text",
        help='The claim sentence to cite (copy-paste from page; e.g., "Food noise reduction is dose-dependent.")',
    )
    p_cite_add.add_argument(
        "source_id",
        help="Source id to cite (e.g., web-2026-05-24-test, pubmed-12345678)",
    )
    p_cite_add.add_argument(
        "--fuzzy",
        action="store_true",
        help="If deterministic match misses, fall back to an LLM resolver (incurs one Sonnet/Haiku call)",
    )

    # edit: constrained section-replace (K1)
    p_edit = subparsers.add_parser("edit", help=SUBCOMMANDS["edit"])
    p_edit.add_argument(
        "page_path",
        help="Path to the wiki page (relative to KNOWLEDGE_ROOT or absolute)",
    )
    p_edit.add_argument(
        "--section",
        required=True,
        help='Section name (case-insensitive match against `## <name>` headers; e.g., "Summary")',
    )
    p_edit.add_argument(
        "--body-file",
        help="Path to a markdown file containing the replacement section body. Reads from stdin if omitted.",
    )

    # concept-add: author wiki/concepts/<slug>.md from a markdown body
    p_concept = subparsers.add_parser("concept-add", help=SUBCOMMANDS["concept-add"])
    p_concept.add_argument("slug", help="Concept slug (kebab-case)")
    p_concept.add_argument(
        "--domain",
        required=True,
        help="Domain slug this concept belongs to",
    )
    p_concept.add_argument(
        "--canonical-name",
        required=True,
        help='Human-readable name (e.g., "AI as Substrate")',
    )
    p_concept.add_argument(
        "--content-from",
        help="Path to a markdown file containing the body. Reads from stdin if omitted.",
    )
    p_concept.add_argument(
        "--draft",
        action="store_true",
        help="File with draft=true; downgrades citation grounding to warning",
    )
    p_concept.add_argument(
        "--cite-source",
        action="append",
        dest="cite_sources",
        metavar="SOURCE_ID",
        help="Source ID to add to synthesizes: list (repeatable, e.g. --cite-source web-2024-02-07-3a2)",
    )
    p_concept.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing concept page with the same slug",
    )

    # query: ask the persistent NotebookLM corpus and file a synthesis page
    p_query = subparsers.add_parser(
        "query",
        help=SUBCOMMANDS["query"],
        epilog=(
            "Examples:\n"
            '  wiki query "What mechanisms underlie GLP-1 food-noise suppression?" --domain glp1\n'
            '  wiki query "Compare semaglutide and tirzepatide efficacy" --domain glp1 --draft'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_query.add_argument("question", help="Question to ask the persistent domain corpus")
    p_query.add_argument(
        "--domain",
        required=True,
        help="Domain slug whose persistent NotebookLM corpus to query",
    )
    p_query.add_argument(
        "--draft",
        action="store_true",
        help="Allow partial citations on the synthesis; mark draft until finalized",
    )

    # research: corpus-constructive research loop
    p_research = subparsers.add_parser(
        "research",
        help=SUBCOMMANDS["research"],
        epilog=(
            "Examples:\n"
            '  wiki research "GLP-1 receptor agonists and reward blunting" --domain glp1\n'
            "  wiki research --review abc123\n"
            "  wiki research --execute abc123"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_research.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="Research prompt / question (omit when using --execute)",
    )
    p_research.add_argument(
        "--domain",
        default=None,
        help="Domain slug (omit to let the gateway infer one from the prompt)",
    )
    p_research.add_argument(
        "--include-local",
        action="append",
        default=None,
        dest="include_local",
        help="Path or glob to include via the local-files adapter (repeatable)",
    )
    p_research.add_argument(
        "--trust-local",
        action="store_true",
        help="Skip the semantic filter for local-source items",
    )
    p_research.add_argument(
        "--max-results",
        type=int,
        default=50,
        help="Max candidates each adapter is allowed to return (default 50)",
    )
    p_research.add_argument(
        "--draft",
        action=argparse.BooleanOptionalAction,
        default=True,
        help=(
            "File synthesis pages with draft=true (citation rule downgraded "
            "to warning). Default ON for `wiki research` — NotebookLM's "
            "synthesis prose routinely emits interpretive openers and "
            "mid-section aggregate claims that fail strict citation grounding. "
            "Pass --no-draft to force strict-mode validation (apply_plan "
            "rejects on uncited claims). Recommended workflow: keep the "
            "draft default, follow up with `wiki cite` and `wiki finalize` "
            "per page once the framing prose has been attributed."
        ),
    )
    p_research.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip NotebookLM creation; report a structured plan only",
    )
    p_research.add_argument(
        "--review",
        action="store_true",
        help=(
            "Generate the per-adapter query plan, persist it to "
            "nlm/query_plans/<session-id>.yaml, and stop. Edit the YAML, "
            "then resume with --execute <session-id>."
        ),
    )
    p_research.add_argument(
        "--execute",
        dest="execute_session",
        default=None,
        metavar="SESSION_ID",
        help=(
            "Resume from a persisted query plan (e.g. one written by "
            "--review). Loads the plan, marks edited:true if the YAML "
            "was touched after generation, and proceeds to fan-out."
        ),
    )
    p_research.add_argument(
        "--queries",
        dest="external_plan_path",
        default=None,
        metavar="PATH",
        help=(
            "Use a hand-authored query plan YAML at PATH instead of "
            "generating one. Mutually exclusive with --execute."
        ),
    )
    p_research.add_argument(
        "--no-plan",
        dest="no_plan",
        action="store_true",
        help=(
            "Disable the runtime per-adapter query planner; dispatch the "
            "prompt verbatim to every adapter (M37 behavior). Useful for "
            "offline runs or when no Claude CLI is available."
        ),
    )

    # mcp-serve: start the MCP server (stdio)
    subparsers.add_parser("mcp-serve", help=SUBCOMMANDS["mcp-serve"])

    # batch-ingest: vault-scoped operations (M8 supports --legacy-import)
    p_batch = subparsers.add_parser("batch-ingest", help=SUBCOMMANDS["batch-ingest"])
    p_batch.add_argument("vault", help="Path to the vault to migrate / batch-process")
    p_batch.add_argument(
        "--legacy-import",
        action="store_true",
        help="Treat <vault> as a legacy research-notebook Obsidian vault and migrate it",
    )
    p_batch.add_argument(
        "--domain",
        default=None,
        help="Canonical domain slug for the migrated content",
    )
    p_batch.add_argument(
        "--dry-run",
        action="store_true",
        help="Build the slug map and report counts; do not write canonical files",
    )

    # lint
    p_lint = subparsers.add_parser(
        "lint",
        help=SUBCOMMANDS["lint"],
        epilog=(
            "Examples:\n"
            "  wiki lint\n"
            "  wiki lint --scope orphans\n"
            "  wiki lint --scope broken-wikilinks"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_lint.add_argument(
        "--scope",
        default=None,
        help="Run a single check (e.g., orphans, schema-drift)",
    )

    # backfill-examples
    p_backfill = subparsers.add_parser(
        "backfill-examples", help=SUBCOMMANDS["backfill-examples"]
    )
    p_backfill.add_argument(
        "--domain",
        required=True,
        help="Canonical domain slug (e.g., glp1-reward-modulation)",
    )
    p_backfill.add_argument(
        "--legacy-config",
        type=Path,
        default=None,
        help="Path to a legacy `config/domains/<slug>.yaml` to convert into policy.yaml",
    )
    p_backfill.add_argument(
        "--json",
        type=Path,
        action="append",
        default=[],
        dest="json_paths",
        help="Path to a legacy staged JSON checkpoint (repeat for multiple files)",
    )
    p_backfill.add_argument(
        "--policy-version",
        default=None,
        help="Override the policy_version pinned on each example (default: <domain>-legacy-v1)",
    )

    # finetune
    p_finetune = subparsers.add_parser("finetune", help=SUBCOMMANDS["finetune"])
    p_finetune.add_argument(
        "--domain",
        default=None,
        help="Domain slug (omit with --check to inspect every domain)",
    )
    mode = p_finetune.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="Report example counts vs trigger threshold (no LLM calls)",
    )
    mode.add_argument(
        "--distill",
        action="store_true",
        help="Run a distillation call; writes a candidate policy_versions/<timestamp>.yaml",
    )
    p_finetune.add_argument(
        "--threshold",
        type=int,
        default=None,
        help="Override the trigger threshold (default: 500)",
    )
    p_finetune.add_argument(
        "--force",
        action="store_true",
        help="With --distill: skip the threshold gate (use sparingly)",
    )

    # discover-domains (M36)
    p_discover = subparsers.add_parser(
        "discover-domains", help=SUBCOMMANDS["discover-domains"]
    )
    p_discover.add_argument(
        "--scope",
        default=None,
        help="Glob (relative to repo root) restricting candidate sources, "
        "e.g. 'wiki/sources/pdf-*'",
    )
    p_discover.add_argument(
        "--since",
        default=None,
        help="ISO-8601 prefix; only sources ingested at-or-after this timestamp",
    )
    p_discover.add_argument(
        "--untagged",
        action="store_true",
        help="Only include sources with empty/missing 'domains:' frontmatter",
    )
    p_discover.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="Plan-client wall-clock budget in seconds (default 300; "
        "use 900+ for 200+ source corpora)",
    )

    # promote-domain (M36)
    p_promote = subparsers.add_parser(
        "promote-domain", help=SUBCOMMANDS["promote-domain"]
    )
    p_promote.add_argument(
        "proposal_slug",
        help="Slug of the proposal page (e.g. 'proposal-investing-letters')",
    )

    # serve (M40)
    p_serve = subparsers.add_parser("serve", help=SUBCOMMANDS["serve"])
    p_serve.add_argument(
        "--port",
        type=int,
        default=7474,
        help="Port to bind (default 7474)",
    )
    p_serve.add_argument(
        "--bind",
        default="127.0.0.1",
        help="Host to bind (default 127.0.0.1; use 0.0.0.0 for LAN access)",
    )

    # bootstrap-domain (M39)
    p_bootstrap = subparsers.add_parser(
        "bootstrap-domain", help=SUBCOMMANDS["bootstrap-domain"]
    )
    p_bootstrap.add_argument(
        "description",
        help="Natural-language description of the new domain (1-3 paragraphs)",
    )
    p_bootstrap.add_argument(
        "slug",
        help="Slug for the new domain (lowercase, hyphenated)",
    )
    p_bootstrap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing non-promoted policy at this slug",
    )

    # demote-domain (M36)
    p_demote = subparsers.add_parser(
        "demote-domain", help=SUBCOMMANDS["demote-domain"]
    )
    p_demote.add_argument(
        "domain_slug",
        help="The proposed_domain slug to reverse",
    )

    # reject-proposal (M36)
    p_reject = subparsers.add_parser(
        "reject-proposal", help=SUBCOMMANDS["reject-proposal"]
    )
    p_reject.add_argument(
        "proposal_slug",
        help="Slug of the proposal page to delete",
    )

    # poll
    p_poll = subparsers.add_parser("poll", help=SUBCOMMANDS["poll"])
    p_poll.add_argument(
        "name",
        nargs="?",
        default=None,
        help="Poller name (e.g. apple-notes); omit with --list",
    )
    p_poll.add_argument(
        "--list",
        action="store_true",
        help="List registered pollers and exit",
    )

    # schedule: cron-driven job runner (K4 / M48)
    p_schedule = subparsers.add_parser("schedule", help=SUBCOMMANDS["schedule"])
    p_sched_sub = p_schedule.add_subparsers(dest="schedule_action", required=True)

    p_sched_list = p_sched_sub.add_parser("list", help="List all scheduled jobs")  # noqa: F841

    p_sched_add = p_sched_sub.add_parser("add", help="Add or replace a scheduled job")
    p_sched_add.add_argument("name", help="Job name (used as the file_lock key)")
    p_sched_add.add_argument("cron", help='Cron expression in UTC (e.g., "30 4 * * *")')
    p_sched_add.add_argument("command", help="Shell command to execute on each tick")
    p_sched_add.add_argument(
        "--disabled",
        action="store_true",
        help="Add the job in disabled state (no auto-runs until `wiki schedule enable`)",
    )
    p_sched_add.add_argument(
        "--cooldown-seconds",
        type=int,
        default=600,
        help="Wait this many seconds after a failure before re-running (default 600)",
    )

    p_sched_rm = p_sched_sub.add_parser("remove", help="Remove a job by name")
    p_sched_rm.add_argument("name")

    p_sched_en = p_sched_sub.add_parser("enable", help="Enable a job")
    p_sched_en.add_argument("name")

    p_sched_dis = p_sched_sub.add_parser("disable", help="Disable a job")
    p_sched_dis.add_argument("name")

    p_sched_run = p_sched_sub.add_parser(
        "run", help="Tick: run every due job (launchd invokes this every 60s)"
    )

    p_sched_dry = p_sched_sub.add_parser(
        "dry-run", help="Show what `run` would execute without actually running"
    )

    # auth: bearer-token management for /api/ingest (K3 / M48)
    p_auth = subparsers.add_parser("auth", help=SUBCOMMANDS["auth"])
    p_auth_sub = p_auth.add_subparsers(dest="auth_action", required=True)

    p_auth_add = p_auth_sub.add_parser("add", help="Mint a new bearer token")
    p_auth_add.add_argument(
        "name",
        help="Human-readable token name (e.g., ios-shortcut-andrew-iphone)",
    )

    p_auth_list = p_auth_sub.add_parser(  # noqa: F841
        "list", help="List token names (does not disclose hashes or plaintext)"
    )

    p_auth_rev = p_auth_sub.add_parser("revoke", help="Revoke a token by name")
    p_auth_rev.add_argument("name")

    # agent-log (AGT-14)
    p_agent_log = subparsers.add_parser("agent-log", help=SUBCOMMANDS["agent-log"])
    p_agent_log.add_argument(
        "--since",
        default="24h",
        choices=["24h", "48h", "7d"],
        help="Time window to aggregate (default: 24h)",
    )

    # contradiction (QUAL-3)
    p_contradiction = subparsers.add_parser("contradiction", help=SUBCOMMANDS["contradiction"])
    p_contra_sub = p_contradiction.add_subparsers(dest="contradiction_action", required=True)

    p_contra_list = p_contra_sub.add_parser("list", help="List contradiction pages")
    p_contra_list.add_argument(
        "--severity",
        choices=["major", "minor", "methodological"],
        default=None,
        help="Filter by severity",
    )
    p_contra_list.add_argument(
        "--status",
        default="open",
        help="Filter by status (default: open)",
    )

    p_contra_resolve = p_contra_sub.add_parser("resolve", help="Resolve a contradiction")
    p_contra_resolve.add_argument("slug", help="Slug of the contradiction page")
    p_contra_resolve.add_argument(
        "--status",
        required=True,
        choices=["resolved", "wontfix"],
        help="New status",
    )
    p_contra_resolve.add_argument(
        "--note",
        default="",
        help="Resolution note",
    )

    # draft-close (AGT-2)
    p_draft_close = subparsers.add_parser("draft-close", help=SUBCOMMANDS["draft-close"])
    p_dc_sub = p_draft_close.add_subparsers(dest="draft_close_action", required=True)
    p_dc_sub.add_parser("run", help="Run the draft-closer agent")

    # triage (AGT-1)
    p_triage = subparsers.add_parser("triage", help=SUBCOMMANDS["triage"])
    p_triage_sub = p_triage.add_subparsers(dest="triage_action", required=True)
    p_triage_sub.add_parser("list", help="List sources in the review-band triage queue")

    # agents (A1 — unified run surface for scheduled agents)
    p_agents = subparsers.add_parser("agents", help=SUBCOMMANDS["agents"])
    p_agents_sub = p_agents.add_subparsers(dest="agents_action", required=True)
    p_agents_run = p_agents_sub.add_parser("run", help="Run a named agent")
    p_agents_run.add_argument(
        "agent_name",
        choices=["inbox-triage", "draft-closer", "agent-digest"],
        help="Agent to run",
    )

    # Stubs for everything else
    for name, help_text in SUBCOMMANDS.items():
        if name in IMPLEMENTED:
            continue
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument(
            "args",
            nargs=argparse.REMAINDER,
            help="(arguments forwarded to the subcommand; not parsed yet)",
        )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    argcomplete.autocomplete(parser)
    ns = parser.parse_args(argv)

    if ns.subcommand is None:
        parser.print_help()
        return 0

    if ns.subcommand == "ingest":
        return _run_ingest(ns)
    if ns.subcommand == "filter":
        return _run_filter(ns)
    if ns.subcommand == "filter-correct":
        return _run_filter_correct(ns)
    if ns.subcommand == "status":
        return _run_status(ns)
    if ns.subcommand == "watch":
        return _run_watch(ns)
    if ns.subcommand == "nlm-add":
        return _run_nlm_add(ns)
    if ns.subcommand == "nlm-sync":
        return _run_nlm_sync(ns)
    if ns.subcommand == "nlm-slides":
        return _run_nlm_slides(ns)
    if ns.subcommand == "nlm-audio":
        return _run_nlm_audio(ns)
    if ns.subcommand == "nlm-briefing":
        return _run_nlm_briefing(ns)
    if ns.subcommand == "nlm-revise":
        return _run_nlm_revise(ns)
    if ns.subcommand == "finalize":
        return _run_finalize(ns)
    if ns.subcommand == "finalize-batch":
        return _run_finalize_batch(ns)
    if ns.subcommand == "cite":
        return _run_cite(ns)
    if ns.subcommand == "cite-add":
        return _run_cite_add(ns)
    if ns.subcommand == "edit":
        return _run_edit(ns)
    if ns.subcommand == "concept-add":
        return _run_concept_add(ns)
    if ns.subcommand == "query":
        return _run_query(ns)
    if ns.subcommand == "mcp-serve":
        return _run_mcp_serve(ns)
    if ns.subcommand == "batch-ingest":
        return _run_batch_ingest(ns)
    if ns.subcommand == "lint":
        return _run_lint(ns)
    if ns.subcommand == "backfill-examples":
        return _run_backfill_examples(ns)
    if ns.subcommand == "finetune":
        return _run_finetune(ns)
    if ns.subcommand == "discover-domains":
        return _run_discover_domains(ns)
    if ns.subcommand == "promote-domain":
        return _run_promote_domain(ns)
    if ns.subcommand == "bootstrap-domain":
        return _run_bootstrap_domain(ns)
    if ns.subcommand == "serve":
        return _run_serve(ns)
    if ns.subcommand == "demote-domain":
        return _run_demote_domain(ns)
    if ns.subcommand == "reject-proposal":
        return _run_reject_proposal(ns)
    if ns.subcommand == "schedule":
        return _run_schedule(ns)
    if ns.subcommand == "auth":
        return _run_auth(ns)
    if ns.subcommand == "research":
        return _run_research(ns)
    if ns.subcommand == "poll":
        return _run_poll(ns)
    if ns.subcommand == "evaluate":
        return _run_evaluate(ns)
    if ns.subcommand == "context":
        return _run_context(ns)
    if ns.subcommand == "agent-log":
        return _run_agent_log(ns)
    if ns.subcommand == "contradiction":
        return _run_contradiction(ns)
    if ns.subcommand == "triage":
        return _run_triage_cmd(ns)
    if ns.subcommand == "draft-close":
        return _run_draft_close_cmd(ns)
    if ns.subcommand == "agents":
        return _run_agents_cmd(ns)

    return _not_yet_implemented(ns.subcommand)


def _run_poll(ns: argparse.Namespace) -> int:
    from gateway import pollers

    if ns.list or ns.name is None:
        names = pollers.list_pollers()
        if not names:
            print("no pollers registered")
            return 0
        print("registered pollers:")
        for n in names:
            print(f"  {n}")
        return 0 if ns.list else 2

    try:
        poller = pollers.get_poller(ns.name)
    except pollers.UnknownPollerError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    result = poller.run()
    if not result.success:
        for err in result.errors:
            print(f"error: {err}", file=sys.stderr)
        return 1

    print(result.summary or f"{ns.name}: ok")
    if result.fetched or result.skipped:
        print(f"  fetched={result.fetched} skipped={result.skipped}")
    return 0


def _run_schedule(ns: argparse.Namespace) -> int:
    from gateway import scheduler as _scheduler

    action = ns.schedule_action

    if action == "list":
        jobs = _scheduler.load_schedule()
        if not jobs:
            print("no scheduled jobs (`wiki schedule add` to register one)")
            return 0
        print(f"{len(jobs)} scheduled job(s):")
        for j in jobs:
            state = "enabled" if j.enabled else "DISABLED"
            last = j.last_run or "(never)"
            exit_str = "" if j.last_exit_code is None else f" exit={j.last_exit_code}"
            print(f"  {j.name}  [{state}]  cron={j.cron!r}  last_run={last}{exit_str}")
            print(f"    command: {j.command}")
        return 0

    if action == "add":
        try:
            job = _scheduler.add_job(
                name=ns.name,
                cron=ns.cron,
                command=ns.command,
                enabled=not ns.disabled,
                cooldown_seconds=ns.cooldown_seconds,
            )
        except Exception as e:  # noqa: BLE001 — surface croniter validation errors
            print(f"error: invalid schedule (cron parse failed?): {e}", file=sys.stderr)
            return 2
        print(f"ok: added job {job.name!r}")
        return 0

    if action == "remove":
        if _scheduler.remove_job(ns.name):
            print(f"ok: removed {ns.name!r}")
            return 0
        print(f"error: no job named {ns.name!r}", file=sys.stderr)
        return 2

    if action in ("enable", "disable"):
        if _scheduler.set_enabled(ns.name, enabled=(action == "enable")):
            print(f"ok: {action}d {ns.name!r}")
            return 0
        print(f"error: no job named {ns.name!r}", file=sys.stderr)
        return 2

    if action in ("run", "dry-run"):
        summary = _scheduler.run_all_due(dry_run=(action == "dry-run"))
        if action == "dry-run":
            print(f"dry-run: would run {summary['would_run']}, would skip {summary['skipped']}")
        else:
            print(
                f"ran={summary['ran']} failed={summary['failed']} "
                f"skipped={summary['skipped']}"
            )
        return 0 if summary.get("failed", 0) == 0 else 1

    print(f"error: unknown schedule action: {action}", file=sys.stderr)
    return 2


def _run_auth(ns: argparse.Namespace) -> int:
    from gateway.web import auth as _auth

    action = ns.auth_action

    if action == "add":
        try:
            plaintext = _auth.add_token(ns.name)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
        print(f"ok: token {ns.name!r} minted")
        print(f"  bearer token (save this — it is shown ONCE):")
        print(f"    {plaintext}")
        print()
        print("Use with:")
        print(f"  curl -H 'Authorization: Bearer {plaintext}' \\")
        print("       -H 'Content-Type: application/json' \\")
        print("       -d '{\"url\": \"https://example.com\"}' \\")
        print("       http://localhost:7474/api/ingest")
        return 0

    if action == "list":
        tokens = _auth.list_tokens()
        if not tokens:
            print("no tokens (use `wiki auth add <name>` to mint one)")
            return 0
        print(f"{len(tokens)} token(s):")
        for t in tokens:
            last = t.get("last_used_at") or "(never)"
            print(f"  {t['name']}  created={t['created_at']}  last_used={last}")
        return 0

    if action == "revoke":
        if _auth.revoke_token(ns.name):
            print(f"ok: revoked {ns.name!r}")
            return 0
        print(f"error: no token named {ns.name!r}", file=sys.stderr)
        return 2

    print(f"error: unknown auth action: {action}", file=sys.stderr)
    return 2


def _run_finetune(ns: argparse.Namespace) -> int:
    from gateway.ops.finetune import (
        DistillError,
        distill_prompt,
        trigger_state,
        trigger_states_all,
    )

    threshold = ns.threshold if ns.threshold is not None else 500

    if ns.distill:
        if not ns.domain:
            print("--distill requires --domain <slug>", file=sys.stderr)
            return 2
        try:
            result = distill_prompt(
                ns.domain,
                threshold=threshold,
                enforce_threshold=not ns.force,
            )
        except DistillError as e:
            print(f"distill failed: {e}", file=sys.stderr)
            return 1
        print(f"ok: distilled candidate for {result.domain}")
        print(f"  candidate: {result.candidate_path}")
        print(f"  examples used: {result.examples_used}")
        if result.summary:
            print(f"  summary: {result.summary[:240]}")
        return 0

    # Default and --check: report state.
    if ns.domain:
        state = trigger_state(ns.domain, threshold=threshold)
        readiness = "ready" if state.ready else "below threshold"
        print(
            f"{state.domain}: {state.count}/{state.threshold} examples — {readiness}"
        )
        return 0

    states = trigger_states_all(threshold=threshold)
    if not states:
        print("no policies registered; run `wiki backfill-examples` first")
        return 0
    for s in states:
        readiness = "ready" if s.ready else "below threshold"
        print(f"  {s.domain}: {s.count}/{s.threshold} examples — {readiness}")
    return 0


def _run_backfill_examples(ns: argparse.Namespace) -> int:
    from gateway.ops.example_bank import backfill

    if ns.legacy_config is None and not ns.json_paths:
        print(
            "backfill-examples needs at least one of --legacy-config or --json",
            file=sys.stderr,
        )
        return 2

    summary = backfill(
        domain_slug=ns.domain,
        legacy_config_path=ns.legacy_config,
        json_paths=ns.json_paths,
        policy_version=ns.policy_version,
    )

    print(f"ok: backfill {summary['domain']}")
    if "policy" in summary:
        print(f"  policy: {summary['policy']}")
    if "examples_written" in summary:
        print(f"  examples written: {summary['examples_written']}")
        print(f"  examples skipped: {summary['examples_skipped']}")
        if summary["errors"]:
            print(f"  errors: {len(summary['errors'])}")
            for e in summary["errors"][:5]:
                print(f"    - {e}", file=sys.stderr)
    return 0


def _resolve_input(raw: str) -> str | Path:
    """URL strings pass through; everything else is treated as a filesystem path."""
    if raw.startswith(("http://", "https://")):
        return raw
    return Path(raw).expanduser().resolve()


def _emit_result(result, *, no_op_label: str = "no-op", ok_label: str = "ok") -> int:
    if result.success:
        prefix = no_op_label if result.no_op else ok_label
        print(f"{prefix}: {result.summary}")
        for p in result.paths_touched:
            print(f"  touched: {p}")
        if result.authorship_report is not None:
            report = result.authorship_report
            print(f"  authorship: {report.format_summary()}")
            for line in report.format_detail():
                print(line)
        for w in result.warnings:
            print(f"warning: {w}", file=sys.stderr)
        return 0
    print("operation failed:", file=sys.stderr)
    for e in result.errors:
        print(f"  - {e}", file=sys.stderr)
    return 1


def _run_ingest(ns: argparse.Namespace) -> int:
    from gateway.ops.ingest import ingest
    from gateway.plan import ClaudeCLIPlanClient

    timeout_s = getattr(ns, "plan_timeout", None)
    plan_client = ClaudeCLIPlanClient(timeout_s=timeout_s) if timeout_s else None

    return _emit_result(
        ingest(
            _resolve_input(ns.input),
            domain=ns.domain,
            with_plan=getattr(ns, "with_plan", False),
            draft=getattr(ns, "draft", False),
            plan_client=plan_client,
        )
    )


def _run_filter(ns: argparse.Namespace) -> int:
    from gateway.ops.filter_op import filter_source

    return _emit_result(filter_source(_resolve_input(ns.input), domain=ns.domain))


def _run_filter_correct(ns: argparse.Namespace) -> int:
    from gateway.ops.filter_correct import filter_correct

    decision = "include" if ns.include else "exclude"
    return _emit_result(
        filter_correct(
            ns.source_id,
            decision=decision,
            rationale=ns.rationale,
            domain=ns.domain,
        )
    )


def _run_status(ns: argparse.Namespace) -> int:
    from gateway.ops.status import status

    result = status(with_cost=getattr(ns, "cost", False))
    print(result.summary)
    return 0 if result.success else 1


def _run_watch(ns: argparse.Namespace) -> int:
    from gateway.watcher import run_foreground

    return run_foreground()


def _run_nlm_add(ns: argparse.Namespace) -> int:
    from gateway.ops.nlm import nlm_add

    return _emit_result(nlm_add(ns.domain, ns.source_id))


def _run_nlm_sync(ns: argparse.Namespace) -> int:
    from gateway.ops.nlm import nlm_sync

    def _progress(idx: int, total: int, source_id: str, status: str, detail: str) -> None:
        marker = {"added": "+", "skipped": "·", "failed": "x"}.get(status, "?")
        # Trim long detail lines so progress stays readable.
        detail_short = (detail or "")[:80]
        print(f"  [{idx:>3}/{total}] {marker} {source_id:<28} {detail_short}", flush=True)

    result = nlm_sync(
        ns.domain,
        dry_run=ns.dry_run,
        limit=ns.limit,
        progress=None if ns.dry_run else _progress,
    )
    return _emit_result(result)


def _run_nlm_slides(ns: argparse.Namespace) -> int:
    from gateway.ops.nlm import nlm_slides

    return _emit_result(nlm_slides(ns.domain, ns.topic))


def _run_nlm_audio(ns: argparse.Namespace) -> int:
    from gateway.ops.nlm import nlm_audio

    return _emit_result(nlm_audio(ns.domain, ns.topic))


def _run_nlm_briefing(ns: argparse.Namespace) -> int:
    from gateway.ops.nlm import nlm_briefing

    return _emit_result(nlm_briefing(ns.domain))


def _run_nlm_revise(ns: argparse.Namespace) -> int:
    from gateway.ops.nlm import nlm_revise

    return _emit_result(nlm_revise(ns.artifact_slug, ns.slides))


def _run_finalize(ns: argparse.Namespace) -> int:
    from gateway.ops.finalize import finalize

    return _emit_result(finalize(ns.page_path, abandon=ns.abandon))


def _run_finalize_batch(ns: argparse.Namespace) -> int:
    from gateway.ops.finalize_batch import finalize_batch

    return _emit_result(
        finalize_batch(
            domain=ns.domain,
            limit=ns.limit,
            execute=ns.execute,
            suggest=ns.suggest,
        )
    )


def _run_evaluate(ns: argparse.Namespace) -> int:
    from gateway.ops.evaluate_op import evaluate_op

    return _emit_result(
        evaluate_op(
            domain=ns.domain,
            limit=ns.limit,
            scaffold=ns.scaffold,
        )
    )


def _run_context(ns: argparse.Namespace) -> int:
    from gateway.ops.context_op import context_op

    result = context_op(
        ns.query,
        depth=ns.depth,
        fmt=ns.format,
        caller=ns.caller,
    )
    if not result.success:
        for err in result.errors:
            print(err, file=sys.stderr)
        return 1
    # Raw stdout: result.summary is the payload (markdown or JSON), meant to be
    # piped into a sibling project's context loader or `jq`. The standard
    # `ok: ... touched: ...` envelope would corrupt machine-readable formats.
    print(result.summary)
    return 0


def _run_cite(ns: argparse.Namespace) -> int:
    if ns.suggest:
        from gateway.ops.cite_suggest import suggest_cites
        from gateway.core import OperationResult

        suggestions = suggest_cites(ns.page_path)
        lines: list[str] = []
        for s in suggestions:
            if s.auto_appliable:
                quote_preview = s.evidence_quote[:60].replace("\n", " ")
                lines.append(
                    f"wiki cite {ns.page_path} {s.line}:{s.source_id}  # quote: {quote_preview}"
                )
            else:
                lines.append(
                    f"# ESCALATED line={s.line} source={s.source_id} reason={s.skip_reason!r}"
                )
        if not lines:
            lines.append("# no suggestions emitted")
        return _emit_result(OperationResult(
            success=True,
            summary="\n".join(lines),
        ))

    if not ns.additions:
        print(
            "error: provide at least one LINE:SOURCE_ID pair, or pass --suggest",
            file=sys.stderr,
        )
        return 2

    from gateway.ops.cite import cite

    additions: list[tuple[int, str]] = []
    for token in ns.additions:
        if ":" not in token:
            print(
                f"error: invalid LINE:SOURCE_ID token (missing ':'): {token}",
                file=sys.stderr,
            )
            return 2
        line_str, _, sid = token.partition(":")
        try:
            ln = int(line_str)
        except ValueError:
            print(
                f"error: line number is not an integer: {line_str!r} (in {token})",
                file=sys.stderr,
            )
            return 2
        additions.append((ln, sid.strip()))
    return _emit_result(cite(ns.page_path, additions))


def _run_cite_add(ns: argparse.Namespace) -> int:
    from gateway.ops.cite_add import cite_add

    return _emit_result(
        cite_add(
            ns.page_path,
            claim_text=ns.claim_text,
            source_id=ns.source_id,
            fuzzy=ns.fuzzy,
        )
    )


def _run_edit(ns: argparse.Namespace) -> int:
    from gateway.ops.edit_section import edit_section

    if ns.body_file:
        try:
            new_body = open(ns.body_file, encoding="utf-8").read()
        except OSError as e:
            print(
                f"error: cannot read --body-file {ns.body_file!r}: {e}",
                file=sys.stderr,
            )
            return 2
    else:
        new_body = sys.stdin.read()
    return _emit_result(
        edit_section(ns.page_path, section=ns.section, new_body=new_body)
    )


def _run_concept_add(ns: argparse.Namespace) -> int:
    from gateway.ops.concept_add import concept_add

    if ns.content_from:
        try:
            body = open(ns.content_from, encoding="utf-8").read()
        except OSError as e:
            print(f"error: cannot read --content-from {ns.content_from!r}: {e}", file=sys.stderr)
            return 2
    else:
        body = sys.stdin.read()
    if not body.strip():
        print(
            "error: concept body is empty (read from stdin or --content-from)",
            file=sys.stderr,
        )
        return 2
    return _emit_result(
        concept_add(
            ns.slug,
            canonical_name=ns.canonical_name,
            body=body,
            domain=ns.domain,
            draft=ns.draft,
            cite_sources=ns.cite_sources,
            force=ns.force,
        )
    )


def _run_query(ns: argparse.Namespace) -> int:
    from gateway.ops.query import query

    return _emit_result(query(ns.question, domain=ns.domain, draft=ns.draft))


def _run_mcp_serve(ns: argparse.Namespace) -> int:
    from gateway.mcp_server import run

    run()
    return 0


def _run_batch_ingest(ns: argparse.Namespace) -> int:
    from gateway.ops.batch_ingest import batch_ingest

    return _emit_result(
        batch_ingest(
            ns.vault,
            legacy_import=ns.legacy_import,
            domain=ns.domain,
            dry_run=ns.dry_run,
        )
    )


def _run_lint(ns: argparse.Namespace) -> int:
    from gateway.ops.lint import lint

    return _emit_result(lint(scope=ns.scope))


def _run_discover_domains(ns: argparse.Namespace) -> int:
    from gateway.ops.discover_domains import discover_domains

    return _emit_result(
        discover_domains(
            scope=ns.scope,
            since=ns.since,
            untagged=ns.untagged,
            timeout_s=ns.timeout,
        )
    )


def _run_promote_domain(ns: argparse.Namespace) -> int:
    from gateway.ops.promote_domain import promote_domain

    return _emit_result(promote_domain(ns.proposal_slug))


def _run_bootstrap_domain(ns: argparse.Namespace) -> int:
    from gateway.ops.bootstrap_domain import bootstrap_domain

    return _emit_result(
        bootstrap_domain(
            description=ns.description,
            slug=ns.slug,
            force=ns.force,
        )
    )


def _run_serve(ns: argparse.Namespace) -> int:
    import uvicorn

    print(f"wiki serve · http://{ns.bind}:{ns.port}", flush=True)
    uvicorn.run(
        "gateway.web.app:app",
        host=ns.bind,
        port=ns.port,
        log_level="info",
    )
    return 0


def _run_demote_domain(ns: argparse.Namespace) -> int:
    from gateway.ops.demote_domain import demote_domain

    return _emit_result(demote_domain(ns.domain_slug))


def _run_reject_proposal(ns: argparse.Namespace) -> int:
    from gateway.ops.reject_proposal import reject_proposal

    return _emit_result(reject_proposal(ns.proposal_slug))


def _run_research(ns: argparse.Namespace) -> int:
    from gateway.llm import model_for
    from gateway.plan import ClaudeCLIPlanClient
    from gateway.research.orchestrator import research

    # M46-followup Fix E: research's plan_client is used for query planning
    # (and domain inference), not multi-page authorship. Bounded fan-out
    # generation — Sonnet handles it well at lower cost than Opus.
    plan_client = (
        None
        if ns.no_plan
        else ClaudeCLIPlanClient(model=model_for("plan_query_planner"))
    )

    return _emit_result(
        research(
            ns.prompt,
            domain=ns.domain,
            include_local=ns.include_local,
            trust_local=ns.trust_local,
            max_results_per_adapter=ns.max_results,
            plan_client=plan_client,
            draft=ns.draft,
            dry_run=ns.dry_run,
            review=ns.review,
            execute_session=ns.execute_session,
            external_plan_path=ns.external_plan_path,
        )
    )


def _run_agent_log(ns: argparse.Namespace) -> int:
    from gateway.ops.agent_log import aggregate

    window_map = {"24h": 24, "48h": 48, "7d": 168}
    since_hours = window_map.get(ns.since, 24)
    data = aggregate(since_hours=since_hours)

    if not data:
        print(f"No agent events in the last {ns.since}.")
        return 0

    for agent, stats in sorted(data.items()):
        print(f"{agent}: {stats['count']} event(s)")
        for payload in stats["top_payloads"]:
            if payload:
                print(f"  - {payload}")
    return 0


def _run_contradiction(ns: argparse.Namespace) -> int:
    from gateway.ops import contradiction as cont_ops

    if ns.contradiction_action == "list":
        return _emit_result(
            cont_ops.list_contradictions(
                severity=ns.severity,
                status=ns.status,
            )
        )
    if ns.contradiction_action == "resolve":
        return _emit_result(
            cont_ops.resolve_contradiction(
                ns.slug,
                status=ns.status,
                note=ns.note,
            )
        )
    return 2


def _run_draft_close_cmd(ns: argparse.Namespace) -> int:
    from gateway.agents.draft_closer import run_draft_closer

    if ns.draft_close_action == "run":
        result = run_draft_closer()
        print(
            f"draft-closer: finalized={result.pages_finalized} "
            f"escalated={result.pages_escalated} skipped={result.pages_skipped}"
        )
        if result.errors:
            for e in result.errors:
                print(f"  error: {e}", file=sys.stderr)
        return 0
    return 2


def _run_triage_cmd(ns: argparse.Namespace) -> int:
    from gateway.agents.inbox_triage import triage_list

    if ns.triage_action == "list":
        items = triage_list()
        if not items:
            print("triage queue is empty")
            return 0
        print(f"{'source_id':<36} {'domain':<20} {'score':<8} {'title'}")
        print("-" * 80)
        for item in items:
            sid = item.get("source_id", "")
            domain = item.get("domain") or ""
            score_val = item.get("filter_score")
            score_str = f"{score_val:.2f}" if score_val is not None else "—"
            title = (item.get("title") or "")[:30]
            print(f"{sid:<36} {domain:<20} {score_str:<8} {title}")
        return 0
    return 2


_AGENT_NAMES = ("inbox-triage", "draft-closer", "agent-digest")


def _run_agents_cmd(ns: argparse.Namespace) -> int:
    if ns.agents_action != "run":
        print(f"error: unknown agents action: {ns.agents_action}", file=sys.stderr)
        return 2

    name = ns.agent_name

    if name == "inbox-triage":
        from gateway.agents.inbox_triage import run_inbox_triage_batch
        result = run_inbox_triage_batch()
        print(
            f"inbox-triage: processed={result.processed} "
            f"skipped={result.skipped} failed={result.failed}"
        )
        return 0 if result.failed == 0 else 1

    if name == "draft-closer":
        from gateway.agents.draft_closer import run_draft_closer
        result = run_draft_closer()
        print(
            f"draft-closer: finalized={result.pages_finalized} "
            f"escalated={result.pages_escalated} skipped={result.pages_skipped}"
        )
        return 0

    if name == "agent-digest":
        from gateway.ops.agent_log import aggregate, build_digest_page
        from datetime import datetime, timezone
        data = aggregate(since_hours=24)
        if not data:
            print("agent-digest: no agent events in the last 24h")
            return 0
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        content = build_digest_page(date_str=date_str)
        # Write the draft digest page through the gateway apply_plan path.
        from gateway.plan import Plan, WikiUpdate
        from gateway.ops.apply_plan import apply_plan
        slug = f"agent-digest-{date_str}"
        plan = Plan(
            source_id="agent-digest",
            rationale=f"Daily agent-activity digest for {date_str} (AGT-14)",
            updates=[WikiUpdate(
                target_path=f"wiki/synthesis/{slug}.md",
                update_kind="create",
                content=content,
            )],
        )
        op_result = apply_plan(plan, draft=True)
        if op_result.success:
            print(f"agent-digest: wrote draft page wiki/synthesis/{slug}.md")
            for w in op_result.warnings or []:
                print(f"  warning: {w}")
        else:
            for err in op_result.errors or []:
                print(f"  error: {err}", file=sys.stderr)
            return 1
        return 0

    print(f"error: unknown agent name: {name!r}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
