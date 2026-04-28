#!/usr/bin/env bash
# Install the knowledge-watcher as a launchd user agent.
#
# Generates ~/Library/LaunchAgents/com.knowledge.watcher.plist pointing at
# the wiki binary in this repo's .venv, then loads it. Re-running is safe:
# the existing agent is unloaded first.
#
# Logs go to ~/code/knowledge/.knowledge/watcher.{out,err}.log
#
# Uninstall: scripts/install_watcher.sh --uninstall

set -euo pipefail

KB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_BIN="${KB_ROOT}/.venv/bin/wiki"
PLIST_LABEL="com.knowledge.watcher"
PLIST_PATH="${HOME}/Library/LaunchAgents/${PLIST_LABEL}.plist"
LOG_DIR="${KB_ROOT}/.knowledge"

unload_if_present() {
    if launchctl list | grep -q "${PLIST_LABEL}"; then
        launchctl unload "${PLIST_PATH}" 2>/dev/null || true
    fi
}

if [[ "${1:-}" == "--uninstall" ]]; then
    unload_if_present
    if [[ -f "${PLIST_PATH}" ]]; then
        rm "${PLIST_PATH}"
        echo "removed ${PLIST_PATH}"
    fi
    echo "watcher uninstalled"
    exit 0
fi

if [[ ! -x "${WIKI_BIN}" ]]; then
    echo "error: ${WIKI_BIN} not found or not executable" >&2
    echo "run: cd ${KB_ROOT} && python3 -m venv .venv && source .venv/bin/activate && pip install -e ." >&2
    exit 1
fi

mkdir -p "${LOG_DIR}"
mkdir -p "$(dirname "${PLIST_PATH}")"

cat > "${PLIST_PATH}" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_LABEL}</string>

    <key>ProgramArguments</key>
    <array>
        <string>${WIKI_BIN}</string>
        <string>watch</string>
    </array>

    <key>WorkingDirectory</key>
    <string>${KB_ROOT}</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>KNOWLEDGE_ROOT</key>
        <string>${KB_ROOT}</string>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:${HOME}/.local/bin</string>
    </dict>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>${LOG_DIR}/watcher.out.log</string>

    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/watcher.err.log</string>
</dict>
</plist>
EOF

unload_if_present
launchctl load "${PLIST_PATH}"

echo "watcher installed: ${PLIST_PATH}"
echo "logs:"
echo "  ${LOG_DIR}/watcher.out.log"
echo "  ${LOG_DIR}/watcher.err.log"
echo ""
echo "verify with: wiki status"
echo "uninstall:   $0 --uninstall"
