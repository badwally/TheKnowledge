# Backlog: H1a (Scaling Empirical Evidence) Blocked by Paywall/Rate-Limit Source Access

**Category:** Research Domain / Source Access
**Priority:** Medium
**Effort:** ~2-4 hours (source hunting + fresh session)
**Trigger to action:** Either (a) arxiv rate limits clear and retry shows >5 distinct citations, or (b) preprint/OA links are identified for the key papers listed below

---

## Problem

The convergent-ai-brain H1a sub-claim ("empirical evidence that representational
alignment scales with model competence") cannot be synthesized because the key
primary sources are inaccessible:

- **arxiv**: 429 rate-limit on all 8 arxiv queries during the session — arxiv
  IDs `2603.00793`, `2312.14285`, `2405.07987`, `2602.14486`, `2310.04645`,
  `2605.05556`, `2602.07539`, `2410.11516` all failed at convert time.
- **PNAS / biorXiv**: HTTP 403 on `pnas.org` and `biorxiv.org` fetches — the
  Yamins/DiCarlo 2014 (PNAS), Schrimpf Brain-Score 2018 (biorXiv), and 5 other
  papers returned 403.
- **Semantic Scholar**: 2 sources (`249613319`, `280693118`) returned "could not
  fetch" — likely broken IDs or rate-limited.

Only 1 of 21 materialized sources had rich extractable content: `web-2025-09-23-25b`
("A Python Toolbox for Representational Similarity Analysis", eLife open access,
~13k words). NLM's analysis cited only that source for all 4 branches, fabricating
content about ECoG studies, LLaMA scaling, and Brain-Score and attributing it to
the RSA toolbox.

## Evidence

Session `2026-05-30-what-is-the-empirical-evidence-that`, executed 2026-06-02:
- Index settled at 11 distinct sources (index_settle fix confirmed working)
- 21 materialized; but word counts: 4 × pubmed abstracts (19–199 words), most
  web sources behind paywalls
- All 5 synthesis pages: `synthesizes: [sources/web-2025-09-23-25b]`, `sources_count: 1`
- Content described GPT-Neo ECoG scaling and LLaMA reading fMRI — none of which
  is in the RSA toolbox

All 8 H1a synthesis pages abandoned (3 old + 5 from this session). Session
marked abandoned in nlm/notebooks.yaml.

## Key Sources Needed

To unblock H1a, obtain open-access versions of:

| Paper | arxiv / OA link | Why it matters |
|-------|-----------------|----------------|
| Goldstein et al. 2022 — shared computational principles | PMC:8904253 (Nature Neuroscience) | Primary ECoG + next-word prediction evidence |
| Schrimpf et al. 2021 — Brain-Score language | biorXiv:10.1101/2020.06.26.174482 | Core benchmark paper |
| Yamins & DiCarlo 2016 — ventral stream review | PNAS (paywalled) | Foundational scaling evidence |
| Huth et al. 2016 — semantic fMRI atlas | Nature (paywalled) | Key fMRI encoding model |
| TopoLM / topographic LM paper | arxiv ID TBD | Brain-alignment training objective |

## Recommended Fix

1. Wait for arxiv rate limits to clear (usually 24-48h), then retry with a new
   session targeting the arxiv IDs above directly via `--queries` with arxiv IDs.
2. For PNAS/biorXiv: prefer `https://www.biorxiv.org/content/...v2.full` URLs
   (full-text HTML, not PDF) which trafilatura can extract without 403s.
3. Run a fresh H1a session (`wiki research --review` with domain
   `convergent-ai-brain`, new date-stamped session ID).
