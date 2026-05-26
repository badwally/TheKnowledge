# Contributing

## Prerequisites

- Python 3.11+
- git
- Homebrew (macOS, needed for `ffmpeg` if you use voice/audiobook conversion; Apple Silicon recommended for Whisper transcription)
- Tab completion (optional): see [docs/shell-completion.md](docs/shell-completion.md)

## Environment setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
wiki --help          # smoke test — all subcommands should be listed
```

If `wiki --help` fails, check that the venv is active and the package installed in editable mode (`pip show knowledge-gateway`).

## Running tests

```bash
pytest -x                                       # stop on first failure; expect 1179+ passing
pytest tests/gateway/test_mcp_parity.py         # K2 gate — must stay green before any merge
pytest tests/gateway/test_converters_web.py -v  # run one test file
```

If tests fail on a clean checkout, verify you are using Python 3.11+ (`python --version`) and all dev dependencies installed (`pip install -e ".[dev]"`).

## Running lint

```bash
wiki lint                          # all checks
wiki lint --scope orphans          # one check (faster)
wiki lint --scope stale-drafts
```

Expected output shape: one line per finding (`[WARNING]` or `[ERROR]`), then a summary count. Zero errors is the bar for merging. Warnings are advisory.

## Adding a source converter

Full contract is in [src/gateway/converters/README.md](src/gateway/converters/README.md). The six steps:

1. Add the type string to `SOURCE_TYPES` in `src/gateway/paths.py`.
2. Add it to `ALLOWED_SOURCE_TYPES` in `src/gateway/validator.py` and define an `ID_PATTERNS` regex.
3. Implement a `Converter` subclass in `src/gateway/converters/<type>.py` with `detect()` and `convert()`.
4. Register it in `src/gateway/converters/__init__._ensure_registered`.
5. Update `WIKI.md` § 3.1 (type enum), § 3.2 (meta block), § 6.1 (ID format).
6. Write tests at `tests/gateway/test_converters_<type>.py` mirroring an existing converter's shape.

**You're done when:**
- `pytest tests/gateway/test_converters_<type>.py` passes.
- `wiki lint` shows no new errors.
- `pytest tests/gateway/test_mcp_parity.py` stays green.
- `wiki ingest <sample-url-or-file> --domain <slug>` succeeds end-to-end.

## Adding a poller

Full contract is in [src/gateway/pollers/README.md](src/gateway/pollers/README.md). The five steps:

1. Subclass `Poller` from `src/gateway/pollers/base.py`; set the `name` class attribute.
2. Implement `run() -> PollerResult`: read cursor, fetch new items, write to `raw/<type>/`, write cursor.
3. Register in `src/gateway/pollers/__init__._REGISTRY`.
4. If event-triggered, add subscription YAML at `.knowledge/agents/<name>.yaml`.
5. Write tests at `tests/gateway/test_pollers_<name>.py`.

**You're done when:**
- `pytest tests/gateway/test_pollers_<name>.py` passes.
- `wiki poll <name>` runs without error on a clean cursor.
- Running `wiki poll <name>` a second time with no new items writes nothing and advances no cursor.

## Adding a gateway op

1. Add a function in `src/gateway/ops/<op>.py` returning `OperationResult`.
2. Add a CLI subcommand to `src/gateway/cli.py`: register in `SUBCOMMANDS`, `IMPLEMENTED`, `build_parser()`, and `main()`.
3. Add a MCP tool to `src/gateway/mcp_server.py` (or add to `CLI_ONLY` with justification).
4. Write tests at `tests/gateway/test_<op>.py`.

**You're done when:**
- `wiki <op> --help` prints usage.
- The MCP tool is registered (or `CLI_ONLY` exemption documented).
- `pytest tests/gateway/test_mcp_parity.py` stays green.

## Adding a lint check

1. Create `src/gateway/lint/<check_name>.py` with a `run()` function returning `list[LintFinding]`.
2. Register the check slug in `KNOWN_CHECKS` in `src/gateway/lint/__init__.py` and wire it into the dispatch table.
3. Write a test that creates a violating page and confirms a finding is returned.

**You're done when:**
- `wiki lint --scope <check_name>` runs and surfaces findings for a known violation.
- `wiki lint` output includes the check in its summary.

## Commit conventions

```
feat|fix|perf|docs|chore|style|refactor(<area>): <description>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Examples: `feat(ingest): add --draft flag to skip citation validation`, `fix(validator): handle missing domains field on source pages`, `docs(contributing): add gateway op recipe`.

Rules:
- No `--no-verify` (hooks run citation lint and direct-write checks).
- No amending published commits; create a new commit to fix.
- No force-pushing main.

## PR checklist

Before merging any branch:

- [ ] `pytest -x` passes.
- [ ] `wiki lint` shows no new errors.
- [ ] `pytest tests/gateway/test_mcp_parity.py` green (K2 gate).
- [ ] If milestone boundary: `docs/milestones/M<N>.md` written, `BUILD.md` § 10 row added.
- [ ] If milestone boundary: `docs/session-state.md` updated, open contracts resolved.
- [ ] WIKI.md gateway operations table updated if new ops were added.
