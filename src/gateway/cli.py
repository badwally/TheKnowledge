"""`wiki` CLI entry point.

Implemented at the current milestone: ingest, filter, filter-correct.
Other subcommands print "not yet implemented" and exit 2 until their
milestone lands. See BUILD.md.
"""

import argparse
import sys
from pathlib import Path

from gateway import __version__


SUBCOMMANDS: dict[str, str] = {
    "ingest": "Ingest a single source (path or URL) into the canonical wiki",
    "batch-ingest": "Ingest a whole vault or directory; supports --legacy-import",
    "query": "Query the wiki; may invoke NotebookLM for large-corpus questions",
    "filter": "Run the semantic filter on a candidate source (read-only)",
    "filter-correct": "Override a past filter decision; pin as a corrected example",
    "nlm-add": "Add a source to a NotebookLM corpus",
    "nlm-slides": "Generate a slide deck from a NotebookLM corpus; file as wiki artifact",
    "nlm-audio": "Generate an audio overview; file as wiki artifact",
    "nlm-briefing": "Generate a briefing doc; file as wiki artifact",
    "nlm-revise": "Revise an existing NotebookLM artifact",
    "finalize": "Finalize a draft page (re-run validator with citation rule restored)",
    "lint": "Run health checks across the wiki",
    "index": "Rebuild or update the content index",
    "search": "Search wiki + raw sources",
    "status": "Show recent activity, watcher state, pending queues",
    "migrate": "Apply a schema or content migration script",
    "mcp-serve": "Start the MCP server exposing gateway operations as native tools",
    "watch": "Run the inbox watcher daemon in the foreground (used by launchd)",
}

IMPLEMENTED: set[str] = {"ingest", "filter", "filter-correct", "status", "watch"}


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
    p_ingest = subparsers.add_parser("ingest", help=SUBCOMMANDS["ingest"])
    p_ingest.add_argument("input", help="URL or path to canonical markdown source")
    p_ingest.add_argument("--domain", default=None, help="Domain slug for filter scoring")

    # filter (read-only scoring)
    p_filter = subparsers.add_parser("filter", help=SUBCOMMANDS["filter"])
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
    subparsers.add_parser("status", help=SUBCOMMANDS["status"])

    # watch (no args; runs foreground)
    subparsers.add_parser("watch", help=SUBCOMMANDS["watch"])

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

    return _not_yet_implemented(ns.subcommand)


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
        for w in result.warnings:
            print(f"warning: {w}", file=sys.stderr)
        return 0
    print("operation failed:", file=sys.stderr)
    for e in result.errors:
        print(f"  - {e}", file=sys.stderr)
    return 1


def _run_ingest(ns: argparse.Namespace) -> int:
    from gateway.ops.ingest import ingest

    return _emit_result(ingest(_resolve_input(ns.input), domain=ns.domain))


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

    result = status()
    print(result.summary)
    return 0 if result.success else 1


def _run_watch(ns: argparse.Namespace) -> int:
    from gateway.watcher import run_foreground

    return run_foreground()


if __name__ == "__main__":
    sys.exit(main())
