# Shell completion for `wiki`

The `wiki` CLI uses [argcomplete](https://kislyuk.github.io/argcomplete/) for tab completion. Once activated, pressing Tab after a partial subcommand name or flag will expand it.

## Setup

Add one line to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
eval "$(register-python-argcomplete wiki)"
```

Then reload:

```bash
source ~/.zshrc   # or ~/.bashrc
```

## What completes

- Subcommand names (`wiki ing<TAB>` → `ingest`)
- Flag names (`wiki ingest --<TAB>` → `--domain`, `--with-plan`, `--draft`, …)

File-path and domain-slug arguments are not completed (they depend on live filesystem state and are not registered as completers).

## Troubleshooting

If completion does not activate, verify that `register-python-argcomplete` is on your PATH from the active virtualenv:

```bash
which register-python-argcomplete
```

If you manage the venv manually, activate it before sourcing the profile line, or use an absolute path:

```bash
eval "$(/Users/andrewgrant/code/knowledge/.venv/bin/register-python-argcomplete wiki)"
```
