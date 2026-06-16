"""Tests for gateway.secrets_env — the background-agent secret loader.

launchd agents (watcher, scheduler) do not inherit the interactive shell
environment. `load_secrets_env` bridges that gap by reading a gitignored
`.knowledge/secrets.env` at process start and populating `os.environ` with
`setdefault` semantics (a real env var always wins).
"""

from gateway import secrets_env


def test_main_loads_secrets_env_before_dispatch(tmp_path, monkeypatch):
    """cli.main applies .knowledge/secrets.env so background daemons (which
    reach the converters only through main) see FIRECRAWL_API_KEY."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)
    internal = tmp_path / ".knowledge"
    internal.mkdir()
    (internal / "secrets.env").write_text("FIRECRAWL_API_KEY=fc-via-main\n")

    from gateway import cli

    rc = cli.main([])  # no subcommand: prints help, returns 0 — loader still runs

    assert rc == 0
    assert secrets_env.os.environ["FIRECRAWL_API_KEY"] == "fc-via-main"


def test_loads_key_from_file(tmp_path, monkeypatch):
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)
    env_file = tmp_path / "secrets.env"
    env_file.write_text("FIRECRAWL_API_KEY=fc-abc123\n")

    loaded = secrets_env.load_secrets_env(env_file)

    assert loaded == {"FIRECRAWL_API_KEY": "fc-abc123"}
    assert secrets_env.os.environ["FIRECRAWL_API_KEY"] == "fc-abc123"


def test_does_not_clobber_existing_env(tmp_path, monkeypatch):
    monkeypatch.setenv("FIRECRAWL_API_KEY", "fc-from-shell")
    env_file = tmp_path / "secrets.env"
    env_file.write_text("FIRECRAWL_API_KEY=fc-from-file\n")

    loaded = secrets_env.load_secrets_env(env_file)

    # A real shell env var wins; the file value is not applied.
    assert "FIRECRAWL_API_KEY" not in loaded
    assert secrets_env.os.environ["FIRECRAWL_API_KEY"] == "fc-from-shell"


def test_missing_file_is_noop(tmp_path):
    loaded = secrets_env.load_secrets_env(tmp_path / "nope.env")
    assert loaded == {}


def test_skips_comments_and_blank_lines(tmp_path, monkeypatch):
    monkeypatch.delenv("WIKI_WEB_SCRAPER", raising=False)
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)
    env_file = tmp_path / "secrets.env"
    env_file.write_text(
        "# a comment\n"
        "\n"
        "   \n"
        "WIKI_WEB_SCRAPER=fallback\n"
        "no_equals_sign_here\n"
        "FIRECRAWL_API_KEY=fc-xyz\n"
    )

    loaded = secrets_env.load_secrets_env(env_file)

    assert loaded == {"WIKI_WEB_SCRAPER": "fallback", "FIRECRAWL_API_KEY": "fc-xyz"}


def test_strips_export_prefix_and_quotes(tmp_path, monkeypatch):
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)
    monkeypatch.delenv("WIKI_WEB_SCRAPER", raising=False)
    env_file = tmp_path / "secrets.env"
    env_file.write_text(
        'export FIRECRAWL_API_KEY="fc-quoted"\n'
        "export WIKI_WEB_SCRAPER='fallback'\n"
    )

    loaded = secrets_env.load_secrets_env(env_file)

    assert loaded == {"FIRECRAWL_API_KEY": "fc-quoted", "WIKI_WEB_SCRAPER": "fallback"}


def test_default_path_uses_knowledge_internal(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)
    internal = tmp_path / ".knowledge"
    internal.mkdir()
    (internal / "secrets.env").write_text("FIRECRAWL_API_KEY=fc-default-path\n")

    loaded = secrets_env.load_secrets_env()

    assert loaded == {"FIRECRAWL_API_KEY": "fc-default-path"}
    assert secrets_env.os.environ["FIRECRAWL_API_KEY"] == "fc-default-path"
