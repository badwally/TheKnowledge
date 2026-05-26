"""M0 smoke tests: confirm package imports, CLI runs, version is reported."""

import subprocess
import sys

import gateway
from gateway import cli


def test_package_imports():
    assert gateway.__version__ == "0.1.0"


def test_cli_help_lists_subcommands(capsys):
    parser = cli.build_parser()
    parser.print_help()
    out = capsys.readouterr().out
    # Spot-check that the major subcommands are listed
    for name in ("ingest", "query", "filter", "nlm-slides", "lint", "migrate"):
        assert name in out, f"subcommand `{name}` missing from --help output"


def test_cli_version_via_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "gateway.cli", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "0.1.0" in result.stdout


def test_cli_unimplemented_returns_nonzero():
    # `index` is still a stub; should exit 2 with not-yet-implemented.
    # Update this test when `index` is wired up (currently search is implemented).
    rc = cli.main(["index"])
    assert rc == 2
