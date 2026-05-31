# Mac Mini CMO Deployment Plan

**Date:** 2026-05-28
**Purpose:** Deploy a separate, isolated knowledge gateway instance on a Mac Mini for the CMO, exposed as a remote MCP server accessible from her claude.ai session.

## Context and decisions

The CMO works exclusively from claude.ai (no Claude Code CLI, no terminal). The right integration surface is the MCP server — it exposes every gateway operation and she accesses it through Settings > Integrations in claude.ai with a URL + Bearer token.

Key constraints locked before this plan:
- **Separate vault.** No shared data with `~/code/knowledge`. Her corpus starts from a defined domain export; Andrew retains sole write access to the source vault.
- **Selected domain export.** Domains to port are decided before Phase 2. `orita-cmo` is confirmed. Others TBD.
- **NotebookLM.** CMO vault uses a separate Google account to prevent NLM notebook visibility bleed.
- **Cloudflare Tunnel** (not Tailscale Funnel, not public server). Free, no port forwarding, no cert management, works behind NAT. Best operational simplicity for a single-user deployment.

---

## Architecture

```
CMO (claude.ai)
    └── MCP Settings: https://<tunnel>.cfargotunnel.com + Bearer token
            │
            ▼ HTTPS (Cloudflare Tunnel)
Mac Mini localhost:7475
    └── wiki mcp-serve --http --port 7475
            │  FastMCP streamable-http transport
            │  auth.verify_bearer() middleware
            ▼
    CMO vault at ~/code/knowledge-cmo/
            ├── raw/        ← her ingested sources
            ├── wiki/       ← her wiki pages
            └── .knowledge/ ← policies, auth.yaml, locks
```

Andrew's vault at `~/code/knowledge/` is unchanged and inaccessible from the CMO instance.

---

## Phase 1 — Gateway code changes

These changes land in the main repo and are shared infrastructure.

### P1-A: HTTP transport for `wiki mcp-serve`

**File:** `src/gateway/cli.py` — add `--http` and `--port` flags to `mcp-serve` subparser.

**File:** `src/gateway/mcp_server.py` — extend `run()` to accept a `transport` parameter. When `transport="streamable-http"`, call `mcp.run(transport="streamable-http", host="127.0.0.1", port=<port>)`. FastMCP supports this natively.

Default behavior (stdio) must remain unchanged — existing Claude Code integrations must not break.

### P1-B: Wire bearer auth to MCP HTTP transport

**File:** `src/gateway/mcp_server.py` — when running in HTTP mode, wrap the FastMCP ASGI app with middleware that calls `auth.verify_bearer()` from `src/gateway/web/auth.py` on every request. The bearer token infrastructure (sha256 hashing, `.knowledge/auth.yaml`, `wiki auth add/list/revoke`) is already built (K3/M48) — this is wiring, not new auth logic.

Return `401 Unauthorized` on missing or invalid token. Log the token name (not the plaintext) to `log.md` on each authenticated request for audit trail.

### P1-C: Vault root flag

**File:** `src/gateway/paths.py` — the gateway currently derives paths from a hardcoded `~/code/knowledge/`. Add support for `KNOWLEDGE_ROOT` environment variable as an override. This allows the Mac Mini to run the same codebase against `~/code/knowledge-cmo/` without patching.

Verify that all `paths.*` calls resolve correctly against the override before proceeding to Phase 2.

### P1-D: Test coverage

- Unit test: `wiki mcp-serve --http --port 7475` starts and responds to a bearer-authed request
- Unit test: unauthed request to HTTP MCP returns 401
- Unit test: `KNOWLEDGE_ROOT` override resolves paths correctly
- Existing MCP parity test (`tests/gateway/test_mcp_parity.py`) must still pass

---

## Phase 2 — Mac Mini setup

### P2-A: Repo clone and environment

```bash
git clone https://github.com/badwally/TheKnowledge.git ~/code/knowledge-cmo
cd ~/code/knowledge-cmo
python3.11 -m venv .venv
.venv/bin/pip install -e .
```

Configure environment (add to `~/.zshrc` or a vault-specific `.env`):
```
KNOWLEDGE_ROOT=~/code/knowledge-cmo
ANTHROPIC_API_KEY_RESEARCH=<cmo-vault-key>   # separate Anthropic API key, own budget
```

The audio transcription stack (`whisper` extra) is optional — install only if CMO will ingest audio.

Run `KNOWLEDGE_ROOT=~/code/knowledge-cmo wiki lint` and expect a clean empty-vault pass.

### P2-B: Domain export from source vault

No built-in `wiki export-domain` command exists. Manual export procedure:

1. For each domain to port (e.g. `orita-cmo`):
   - Copy `raw/` files tagged `domains: [orita-cmo]` in their frontmatter
   - Copy corresponding `wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, `wiki/synthesis/` pages
   - Copy `.knowledge/policies/orita-cmo/` (policy YAML + example bank)
   - Copy `nlm/notebooks.yaml` entry for the domain (NLM notebook IDs will be stale — see P2-C)

2. Run `wiki lint` on the CMO vault after import. Expect citation-grounding warnings for any synthesis pages whose sources were not included in the export. Fix by either exporting the missing sources or marking those pages `draft: true`.

3. Write a simple export script at `scripts/export-domain.sh` that automates step 1 for repeatability. This script lives in the source vault and is run by Andrew, not the CMO.

### P2-C: NotebookLM re-registration

The exported domains carry NLM corpus IDs from Andrew's Google account. These are invalid on the CMO vault's Google account.

After export, clear `nlm_corpus_ids` from all exported source frontmatter (or write a one-liner to do it). Run `wiki nlm-sync <domain>` on the CMO vault after configuring the CMO's Google account credentials — this re-registers sources into the CMO account's NotebookLM notebooks and stamps new corpus IDs.

### P2-D: Mint bearer token

```bash
KNOWLEDGE_ROOT=~/code/knowledge-cmo wiki auth add cmo-claudeai
```

Save the plaintext token securely (1Password or equivalent). It is printed once and never stored in plaintext. The CMO uses this token in her claude.ai MCP configuration.

---

## Phase 3 — Cloudflare Tunnel + launchd

### P3-A: Install and configure Cloudflare Tunnel

```bash
brew install cloudflare/cloudflare/cloudflared
cloudflared tunnel login          # authenticate with Cloudflare account
cloudflared tunnel create knowledge-cmo
```

Configure `~/.cloudflared/config.yml`:
```yaml
tunnel: knowledge-cmo
credentials-file: ~/.cloudflared/<tunnel-id>.json
ingress:
  - hostname: knowledge-cmo.<yourdomain>.com   # or use trycloudflare.com free subdomain
    service: http://localhost:7475
  - service: http_status:404
```

If using a custom domain, add the CNAME to DNS via Cloudflare dashboard.

### P3-B: launchd plists

Two daemons needed: the MCP server and the Cloudflare Tunnel. Both go in `~/Library/LaunchAgents/`.

**`~/Library/LaunchAgents/com.knowledge.mcp-serve.plist`:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge.mcp-serve</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/<user>/code/knowledge-cmo/.venv/bin/wiki</string>
        <string>mcp-serve</string>
        <string>--http</string>
        <string>--port</string>
        <string>7475</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>KNOWLEDGE_ROOT</key>
        <string>/Users/<user>/code/knowledge-cmo</string>
        <key>ANTHROPIC_API_KEY_RESEARCH</key>
        <string><!-- inject from keychain or secrets file --></string>
    </dict>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/knowledge-mcp.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/knowledge-mcp.err</string>
</dict>
</plist>
```

**`~/Library/LaunchAgents/com.knowledge.cloudflared.plist`:** same pattern, `cloudflared tunnel run knowledge-cmo`.

Load both: `launchctl load ~/Library/LaunchAgents/com.knowledge.*.plist`

Note: API keys in launchd plist environment are readable to the local user. If the Mac Mini is shared, use macOS Keychain + a wrapper script instead of inline plaintext.

---

## Phase 4 — claude.ai integration and validation

### P4-A: CMO configuration

In her claude.ai Settings > Integrations > Add MCP Server:
- **URL:** `https://knowledge-cmo.<yourdomain>.com/mcp` (FastMCP's default path for streamable-http transport — verify exact path from FastMCP docs)
- **Authorization:** `Bearer <token from P2-D>`

### P4-B: Smoke test sequence

From her claude.ai session, ask Claude to:
1. Call `wiki_status` — should return CMO vault stats, not Andrew's
2. Ingest a test URL: `wiki_ingest url="https://example.com" domain="orita-cmo"`
3. Run `wiki_query question="what do we know about X?"` against the CMO domain
4. Verify `wiki_lint` returns clean

Confirm at the source vault (`~/code/knowledge/`) that none of the above operations touched Andrew's corpus.

---

## Open risks

| Risk | Mitigation |
|---|---|
| FastMCP streamable-http path unknown | Test locally with curl before Mac Mini setup; check FastMCP docs/source for `/mcp` path |
| claude.ai MCP spec support (SSE vs streamable-http) | If streamable-http rejected, fall back to `transport="sse"` — FastMCP supports both |
| launchd env vars with API keys | Use macOS Keychain wrapper if Mac Mini is shared hardware |
| Domain export completeness | Run `wiki lint --scope orphans` on CMO vault post-import; fix forward |
| NLM re-registration rate limits | NotebookLM has undocumented source-add limits; stagger `wiki nlm-sync` if domain is large |

---

## Work sequence

```
P1-C (KNOWLEDGE_ROOT) → P1-A+B (HTTP transport + auth) → P1-D (tests)
  ↓
P2-A (Mac Mini env) → P2-B (domain export) → P2-C (NLM re-reg) → P2-D (token)
  ↓
P3-A (Cloudflare Tunnel) → P3-B (launchd)
  ↓
P4-A (CMO config) → P4-B (smoke test)
```

P1 is the only phase that requires commits to the main repo. P2–P4 are Mac Mini operational work.
