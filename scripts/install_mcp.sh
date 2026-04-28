#!/usr/bin/env bash
# Install the wiki MCP server into the user's Claude Code MCP config.
#
# Adds an entry to ~/.claude/mcp_servers.json (creating the file if missing).
# After install, restart Claude Code so it picks up the new server. Tools
# appear as `wiki_*`.
#
# Uninstall:  scripts/install_mcp.sh --uninstall

set -euo pipefail

KB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_BIN="${KB_ROOT}/.venv/bin/wiki"
CONFIG_PATH="${HOME}/.claude/mcp_servers.json"

if [[ ! -x "${WIKI_BIN}" ]]; then
    echo "error: ${WIKI_BIN} not found or not executable" >&2
    echo "run: cd ${KB_ROOT} && python3 -m venv .venv && source .venv/bin/activate && pip install -e ." >&2
    exit 1
fi

mkdir -p "$(dirname "${CONFIG_PATH}")"

read_config() {
    if [[ -f "${CONFIG_PATH}" ]]; then
        cat "${CONFIG_PATH}"
    else
        echo "{}"
    fi
}

if [[ "${1:-}" == "--uninstall" ]]; then
    if [[ ! -f "${CONFIG_PATH}" ]]; then
        echo "no MCP config at ${CONFIG_PATH}; nothing to uninstall"
        exit 0
    fi
    python3 - "$CONFIG_PATH" <<'PY'
import json, pathlib, sys
path = pathlib.Path(sys.argv[1])
data = json.loads(path.read_text() or "{}")
removed = data.pop("knowledge", None) or data.pop("wiki", None)
path.write_text(json.dumps(data, indent=2) + "\n")
print("removed:", "knowledge" if removed else "(nothing under 'knowledge')")
PY
    echo "wiki MCP server uninstalled from ${CONFIG_PATH}"
    exit 0
fi

# Install / upsert
python3 - "$CONFIG_PATH" "$WIKI_BIN" "$KB_ROOT" <<'PY'
import json, pathlib, sys
config_path, wiki_bin, kb_root = sys.argv[1], sys.argv[2], sys.argv[3]
path = pathlib.Path(config_path)
data = json.loads(path.read_text() or "{}") if path.exists() else {}
data["knowledge"] = {
    "command": wiki_bin,
    "args": ["mcp-serve"],
    "env": {"KNOWLEDGE_ROOT": kb_root},
}
path.write_text(json.dumps(data, indent=2) + "\n")
print("wrote:", path)
PY

echo ""
echo "wiki MCP server installed."
echo "Tools available in Claude Code as: wiki_ingest, wiki_filter, wiki_query,"
echo "  wiki_finalize, wiki_filter_correct, wiki_status, wiki_nlm_*"
echo ""
echo "Restart Claude Code to pick up the new server."
