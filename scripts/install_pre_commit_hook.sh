#!/usr/bin/env bash
# Install a pre-commit hook in this repo that:
#   1. Runs `wiki lint --scope schema-drift` to catch malformed wiki/raw files
#   2. Greps committed wiki/ content for raw `nlm ` invocations (Discipline
#      Gate: agents must go through `wiki nlm-*`, not `nlm` directly)
#
# Uninstall: scripts/install_pre_commit_hook.sh --uninstall

set -euo pipefail

KB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_PATH="${KB_ROOT}/.git/hooks/pre-commit"

if [[ "${1:-}" == "--uninstall" ]]; then
    if [[ -f "${HOOK_PATH}" ]] && grep -q "managed by install_pre_commit_hook.sh" "${HOOK_PATH}"; then
        rm "${HOOK_PATH}"
        echo "removed ${HOOK_PATH}"
    else
        echo "no hook installed by this script at ${HOOK_PATH}"
    fi
    exit 0
fi

mkdir -p "$(dirname "${HOOK_PATH}")"

cat > "${HOOK_PATH}" <<'HOOK'
#!/usr/bin/env bash
# managed by install_pre_commit_hook.sh
set -euo pipefail

KB_ROOT="$(git rev-parse --show-toplevel)"
WIKI_BIN="${KB_ROOT}/.venv/bin/wiki"

# 1) Discipline Gate: no raw `nlm ` calls inside committed wiki/ markdown
violations="$(git diff --cached --name-only | grep -E '^wiki/.*\.md$' || true)"
if [[ -n "${violations}" ]]; then
    bad="$(echo "${violations}" | xargs grep -l -E '^[^#`]*\bnlm\s+[a-z]' 2>/dev/null || true)"
    if [[ -n "${bad}" ]]; then
        echo "pre-commit: raw \`nlm\` invocation found in committed wiki content:" >&2
        echo "${bad}" >&2
        echo "Use \`wiki nlm-*\` operations through the gateway instead." >&2
        exit 1
    fi
fi

# 2) Schema-drift lint over current state of the repo
if [[ -x "${WIKI_BIN}" ]]; then
    if ! "${WIKI_BIN}" lint --scope schema-drift >/dev/null; then
        echo "pre-commit: \`wiki lint --scope schema-drift\` failed" >&2
        echo "Run \`wiki lint\` for the full report." >&2
        exit 1
    fi
fi
HOOK

chmod +x "${HOOK_PATH}"
echo "pre-commit hook installed at ${HOOK_PATH}"
echo ""
echo "Hook runs on every \`git commit\`:"
echo "  - rejects commits that contain raw \`nlm \` calls in wiki/*.md"
echo "  - rejects commits that fail \`wiki lint --scope schema-drift\`"
echo ""
echo "Uninstall: $0 --uninstall"
