---
schema_version: 1
type: entity
slug: coupler-io
canonical_name: Coupler.io
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T14:04:50Z'
last_updated: '2026-05-28T14:04:50Z'
---

# Coupler.io

## Summary

Coupler.io is a no-code data-integration platform that pulls data from SaaS applications such as HubSpot into destinations including Google BigQuery, Google Sheets, and Microsoft Excel [[sources/yt-3JqJkRF0_yU]]. Its unit of work is an "importer" — a named configuration that ties one source app and one destination together with an automatic refresh schedule [[sources/yt-3JqJkRF0_yU]].

## Key facts

- Category: no-code SaaS-to-warehouse / spreadsheet ETL platform [[sources/yt-3JqJkRF0_yU]].
- Supported destinations for HubSpot data: BigQuery, Google Sheets, and Microsoft Excel [[sources/yt-3JqJkRF0_yU]].
- Importer model: name the importer, select a source app (e.g. HubSpot), connect the source account, pick a data category (e.g. Deals), then configure a destination [[sources/yt-3JqJkRF0_yU]].
- HubSpot source options: by default both basic and custom fields are imported; custom fields can be restricted by listing their HubSpot internal names (one per line); a "Start date" filter restricts records by creation date [[sources/yt-3JqJkRF0_yU]].
- BigQuery destination requires a Google Cloud service-account JSON key with `BigQuery data editor` and `BigQuery job user` roles [[sources/yt-3JqJkRF0_yU]].
- Refresh schedule supports per-weekday selection and per-hour cadence (e.g. hourly weekdays only, Saturday/Sunday excluded) plus time-zone preference [[sources/yt-3JqJkRF0_yU]].
- Marketed setup time: roughly 5 minutes for a HubSpot → BigQuery importer with no coding required [[sources/yt-3JqJkRF0_yU]].
- Coupler.io Academy is the official YouTube channel publishing setup tutorials at `youtube.com/@coupleracademy` [[sources/yt-3JqJkRF0_yU]].

## Sources

- [[sources/yt-3JqJkRF0_yU]] — Coupler.io Academy: "How to Set up HubSpot to BigQuery integration | Tutorial"

## Related

- [[entities/hubspot]]
- [[entities/bigquery]]
