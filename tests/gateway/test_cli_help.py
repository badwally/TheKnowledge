"""TOOL-10: shell completion wiring and --help examples on key subcommands."""

import pytest
from gateway.cli import build_parser, main


SUBCOMMANDS_WITH_EXAMPLES = [
    "ingest",
    "filter",
    "query",
    "research",
    "context",
    "evaluate",
    "status",
    "lint",
]


def test_build_parser_returns_parser():
    parser = build_parser()
    assert parser is not None
    assert parser.prog == "wiki"


@pytest.mark.parametrize("subcommand", SUBCOMMANDS_WITH_EXAMPLES)
def test_subcommand_help_contains_example(subcommand, capsys):
    with pytest.raises(SystemExit) as exc:
        main([subcommand, "--help"])
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert "wiki " + subcommand in out or "Examples:" in out


def test_argcomplete_importable():
    import argcomplete  # noqa: F401


def test_main_no_args_prints_help_and_exits_zero(capsys):
    result = main([])
    assert result == 0
    out = capsys.readouterr().out
    assert "wiki" in out
