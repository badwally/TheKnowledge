#!/usr/bin/env bash
# Smoke-test the K3 (M48) /api/ingest endpoint with curl.
#
# Mirrors the HTTP call that the iOS Shortcut sends so you can verify
# the endpoint works end-to-end before configuring the Shortcut on
# your phone.
#
# Configurable via env vars:
#   WIKI_URL    base URL (default http://localhost:7474)
#   WIKI_TOKEN  bearer token (default reads first token from auth.yaml)
#
# Usage:
#   scripts/test-ingest-curl.sh <URL>
#   scripts/test-ingest-curl.sh https://example.com
#
# Example with explicit token:
#   WIKI_TOKEN=abc123 WIKI_URL=https://my-laptop.tailnet.ts.net \
#       scripts/test-ingest-curl.sh https://example.com

set -euo pipefail

if [[ "${1:-}" == "" || "${1:-}" == "--help" ]]; then
    echo "usage: $0 <URL>" >&2
    echo "  env: WIKI_URL (default http://localhost:7474)" >&2
    echo "  env: WIKI_TOKEN (no default; required — get from \`wiki auth list\`)" >&2
    exit 2
fi

URL="$1"
WIKI_URL="${WIKI_URL:-http://localhost:7474}"

if [[ -z "${WIKI_TOKEN:-}" ]]; then
    echo "error: WIKI_TOKEN is required" >&2
    echo "       (this script does NOT auto-read from auth.yaml because" >&2
    echo "        the file stores only hashes — the plaintext is shown" >&2
    echo "        ONCE at \`wiki auth add\` time and not retrievable later)" >&2
    echo "" >&2
    echo "  WIKI_TOKEN=<your-token> $0 $URL" >&2
    exit 2
fi

echo "POST ${WIKI_URL}/api/ingest"
echo "  body: {\"url\": \"${URL}\"}"
echo ""

response=$(curl -sS -X POST \
    -H "Authorization: Bearer ${WIKI_TOKEN}" \
    -H "Content-Type: application/json" \
    -d "{\"url\": \"${URL}\"}" \
    "${WIKI_URL}/api/ingest")

echo "response: ${response}"
task_id=$(echo "${response}" | python3 -c "import json, sys; print(json.load(sys.stdin).get('task_id', ''))")

if [[ -z "${task_id}" ]]; then
    echo ""
    echo "error: no task_id in response (auth failed? endpoint not reachable?)" >&2
    exit 1
fi

echo ""
echo "polling /api/tasks/${task_id} until done…"
for i in $(seq 1 60); do
    sleep 1
    status_resp=$(curl -sS "${WIKI_URL}/api/tasks/${task_id}")
    status=$(echo "${status_resp}" | python3 -c "import json, sys; print(json.load(sys.stdin).get('status', ''))")
    case "${status}" in
        done)
            echo "  status=done (after ${i}s)"
            echo ""
            echo "result:"
            echo "${status_resp}" | python3 -m json.tool
            exit 0
            ;;
        failed)
            echo "  status=failed (after ${i}s)" >&2
            echo "${status_resp}" | python3 -m json.tool >&2
            exit 1
            ;;
        *)
            echo "  status=${status:-?}  (poll ${i}/60)"
            ;;
    esac
done

echo "" >&2
echo "error: task did not complete within 60s" >&2
exit 1
