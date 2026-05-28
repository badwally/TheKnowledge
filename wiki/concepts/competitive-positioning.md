---
schema_version: 1
type: concept
slug: competitive-positioning
canonical_name: Competitive Positioning Intelligence
domains:
- orita-cmo
created_at: '2026-05-28T01:45:53Z'
last_updated: '2026-05-28T02:00:05Z'
---

# Competitive Positioning Intelligence

## Summary

Competitive positioning intelligence at Orita is a planned Claude Code agent that synthesizes competitor activity — web/product changes, hearsay from sales calls, ecosystem and partner signals — into an analytical product rather than a news feed [[sources/pdf-4931157e130a]] [[sources/docx-7ed3b7965067]]. The agent replaces ad-hoc manual monitoring with a scheduled cron-driven function that scans defined sources, extracts and classifies signals, scores them against weighted criteria, assembles a cadenced digest, and recommends actions — including an explicit DO_NOTHING — with auditable reasoning the CMO can override [[sources/docx-7ed3b7965067]].

## Key claims

- The agent's output is an analytical product: signals are filtered, deduplicated, weighted, and presented with context and recommended responses, not surfaced as raw news [[sources/docx-7ed3b7965067]].
- The weighting framework is explicitly the core intellectual property of the spec; calibration requires CMO collaboration on historical examples [[sources/docx-7ed3b7965067]].
- Source provenance is organized into seven MECE categories: S1 Competitor Direct Channels, S2 Platform/Marketplace Signals, S3 Industry/Market Sources, S4 Community/Social Signals, S5 Financial/Organizational Signals, S6 Technical/Open Source Signals, and S7 Ecosystem/Partner Signals [[sources/docx-7ed3b7965067]].
- Access patterns include RSS/Atom feeds, periodic web scrape with diff, API polling, search queries, MCP connectors (Crossbeam, PartnerStack), and manual ingest via Slack or email forward [[sources/docx-7ed3b7965067]].
- Default source reliability scores anchor the trust model: press release/changelog 0.95, earnings call 0.90, job posting 0.85, analyst report 0.80, G2/Capterra review 0.75, LinkedIn exec post 0.70, Reddit/community 0.50, X/Twitter 0.40, speculative inference 0.30 [[sources/docx-7ed3b7965067]].
- Signals are classified along four independent facets with controlled vocabularies (no free text): Signal Category (PRODUCT, PRICING, GTM, TALENT, FINANCE, ECOSYSTEM, CONTENT, MARKET), Strategic Relevance (DIRECT, ADJACENT, ECOSYSTEM, MARKET), Impact Domain (FEATURE_PARITY, MARKET_SHARE, PRICING_PRESSURE, CHANNEL_THREAT, POSITIONING, EXPANSION), and Temporal Horizon (IMMEDIATE, NEAR_TERM, STRATEGIC, TREND) [[sources/docx-7ed3b7965067]].
- Composite signal score = confidence × 0.3 + impact × 0.5 + urgency × 0.2; impact is weighted highest because the CMO's scarce resource is attention [[sources/docx-7ed3b7965067]].
- Confidence = (source_reliability × 0.6) + (corroboration_score × 0.4), where corroboration ranges from 0.3 (single source, no corroboration) to 1.0 (first-party + third-party confirm) [[sources/docx-7ed3b7965067]].
- Impact = severity_base × relevance_multiplier; severity ranges 0.2 (minor) to 1.0 (existential threat/major opportunity); relevance multiplier is 1.0 for HIGH-priority competitors, 0.7 MEDIUM, 0.4 LOW, 0.5 for MARKET-level signals with no specific competitor [[sources/docx-7ed3b7965067]].
- Urgency maps directly from temporal horizon: IMMEDIATE 1.0, NEAR_TERM 0.7, STRATEGIC 0.4, TREND 0.2 [[sources/docx-7ed3b7965067]].
- Temporal decay follows decayed_score = composite_score × 0.5^(days_since_detection / half_life), with half-lives of 14/45/120/365 days for IMMEDIATE/NEAR_TERM/STRATEGIC/TREND; signals below 0.15 after decay are archived [[sources/docx-7ed3b7965067]].
- Action taxonomy is a controlled vocabulary of eight options: MONITOR, BRIEF_TEAM, ADJUST_MESSAGING, ACCELERATE_ROADMAP, EVALUATE_RESPONSE, ENGAGE_PARTNERS, CONTENT_RESPONSE, DO_NOTHING — with DO_NOTHING treated as a first-class explicitly-reasoned outcome rather than a non-event [[sources/docx-7ed3b7965067]].
- Recommendation logic maps composite score thresholds to actions: <0.25 → DO_NOTHING; <0.40 → MONITOR; <0.60 → BRIEF_TEAM / CONTENT_RESPONSE depending on impact domain; <0.80 → ACCELERATE_ROADMAP / ADJUST_MESSAGING / ENGAGE_PARTNERS; ≥0.80 → EVALUATE_RESPONSE (high-impact signals always escalate to human judgment) [[sources/docx-7ed3b7965067]].
- Digest cadence has three tiers: daily scan (24h new signals), weekly intelligence brief (top signals by composite score plus carry-forward items), and monthly strategic review (30-day positioning changes and emerging trends) [[sources/docx-7ed3b7965067]].
- Calibration protocol: collect 10–15 historical competitive events the CMO remembers, have CMO rank them by attention deserved, score using the framework, adjust weights until framework ranking matches CMO ranking — produces calibrated weights plus few-shot examples for the analysis prompt in 1–2 hours [[sources/docx-7ed3b7965067]].
- Override feedback loop is open for design (Slack reactions, structured reply, or weekly batch review); after 50+ overrides the calibration exercise is re-run [[sources/docx-7ed3b7965067]].
- Suggested starting competitor set (pending CMO confirmation): Okara (DIRECT, HIGH), Klaviyo native AI features (ECOSYSTEM, HIGH), Marketeam (ADJACENT, MEDIUM), Sendlane (DIRECT, MEDIUM), Postscript (ADJACENT, MEDIUM), Jasper (ADJACENT, LOW), Blaze (ADJACENT, LOW) [[sources/docx-7ed3b7965067]].
- The agent is classified Level 0 (cron + structured prompts) in the Agent Escalation Levels framework, graduating to Level 1 if a RAG corpus over accumulated intelligence justifies persistent shared state [[sources/docx-7ed3b7965067]].
- Related workflows: 0.1 (Competitive landscape monitoring), 9.5 (Competitive positioning refresh), A.11 (Competitor AEO tracking) [[sources/docx-7ed3b7965067]].

## Sources

- [[sources/pdf-4931157e130a]]
- [[sources/docx-7ed3b7965067]]

## Related

- [[concepts/agent-escalation-levels]]
- [[concepts/workflow-resource-agent-architecture]]
- [[concepts/retrieval-augmented-generation]]
- [[concepts/aeo-geo]]
- [[entities/orita]]
- [[entities/claude-code]]
- [[entities/crossbeam]]
- [[entities/partnerstack]]
- [[entities/klaviyo]]
