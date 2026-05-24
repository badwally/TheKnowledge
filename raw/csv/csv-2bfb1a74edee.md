---
id: csv-2bfb1a74edee
type: csv
title: 9w9g-2c83
url: ''
authors: []
ingested_at: '2026-05-10T22:48:25Z'
content_hash: sha256:6c32536919b75871aa710afd471f4f7361068786fd1922a5774d8589ad18b7ff
source_path: raw/csv/csv-2bfb1a74edee.csv
domains:
- condo-capital-infra
nlm_corpus_ids: []
wiki_pages: []
meta:
  row_count: 526
  column_count: 0
  columns: []
  delimiter: ','
  encoding: utf-8-sig
  original_filename: 9w9g-2c83.csv
  extraction_tool: csv (stdlib)
filter:
  score: 0.2
  policy_version: condo-capital-infra-v1
  rationale: Opaque CSV with no columns, no title beyond an alphanumeric ID, no URL,
    and no contextual metadata indicating relevance to reserve-study methodology,
    regulated jurisdictions, or any of the six probabilistic components. Cannot be
    verified against inclusion criteria and lacks the methodological or provenance
    signals required for the domain.
  decided_at: '2026-05-10T22:48:32Z'
  user_correction:
    decided_at: '2026-05-10T22:49:00Z'
    score: 1.0
    rationale: Raw market-sizing data for NS condominium universe (Active Condominium
      Corporations registry by county, total units). Filter is correctly cautious
      about reserve-study methodology relevance, but per Brief-0006 and ADR-0004 this
      is the load-bearing Atlantic-Canada market-frame anchor for the Halifax design-partner
      engagement (Brief-0004) and the Y1-Y2 expansion path. Raw data dumps that calibrate
      market sizing should not be evaluated under the same semantic threshold as research-content
      sources.
---
# 9w9g-2c83

CSV with **526** data rows × **0** columns.



_476 additional rows omitted from preview. Full data in sidecar._
