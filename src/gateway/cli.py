"""`wiki` CLI entry point.

`ingest` is wired to the M1 implementation. All other subcommands print
"not yet implemented" and exit 2 until their milestone lands. See BUILD.md.
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
}

IMPLEMENTED: set[str] = {"ingest"}


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

    # Real wiring for `ingest`
    p_ingest = subparsers.add_parser("ingest", help=SUBCOMMANDS["ingest"])
    p_ingest.add_argument("input", help="Path to a canonical markdown source file (M1)")

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

    return _not_yet_implemented(ns.subcommand)


def _run_ingest(ns: argparse.Namespace) -> int:
    # Local import keeps `wiki --help` cheap and avoids loading PyYAML
    # for users who only want to read help.
    from gateway.ops.ingest import ingest_canonical

    input_path = Path(ns.input).expanduser().resolve()
    result = ingest_canonical(input_path)

    if result.success:
        if result.no_op:
            print(f"no-op: {result.summary}")
        else:
            print(f"ok: {result.summary}")
            for p in result.paths_touched:
                print(f"  touched: {p}")
        for w in result.warnings:
            print(f"warning: {w}", file=sys.stderr)
        return 0

    print("ingest failed:", file=sys.stderr)
    for e in result.errors:
        print(f"  - {e}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
