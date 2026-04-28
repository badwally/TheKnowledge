"""`wiki` CLI entry point.

M0 stub: every subcommand prints "not yet implemented" and exits non-zero.
Subcommands are wired to real implementations in subsequent milestones (M1+).
"""

import argparse
import sys

from gateway import __version__


SUBCOMMANDS = {
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
}


def _not_yet_implemented(subcommand: str) -> int:
    """Stub handler used by every subcommand at M0."""
    print(
        f"`wiki {subcommand}` is not yet implemented at M0 (repo bootstrap).\n"
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
    parser.add_argument(
        "--version", action="version", version=f"wiki {__version__}"
    )

    subparsers = parser.add_subparsers(dest="subcommand", metavar="<subcommand>")

    for name, help_text in SUBCOMMANDS.items():
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument(
            "args",
            nargs=argparse.REMAINDER,
            help="(arguments forwarded to the subcommand; not parsed at M0)",
        )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    ns = parser.parse_args(argv)

    if ns.subcommand is None:
        parser.print_help()
        return 0

    return _not_yet_implemented(ns.subcommand)


if __name__ == "__main__":
    sys.exit(main())
