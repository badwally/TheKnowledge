---
id: pdf-895bb1ddd34b
type: pdf
title: FallbackPDF__895bb1dd
url: ''
authors:
- Grant
- Andrew
ingested_at: '2026-04-29T16:16:28Z'
content_hash: sha256:8e8c0cfb85633ef7d70c04152c5cd1f1b8c7321bf08a38a5b17b1b4714399a70
source_path: raw/pdf/pdf-895bb1ddd34b.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 2
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__895bb1dd.pdf
published_at: '2025'
---
ViacomCBS Dolby Media Cloud Test Proposal
October 28, 2020
Viacom Test Proposal – DRAFT
We propose a lightweight test implementation of Dolby Media Cloud (DMC) designed to assess
the role of our XCD component in improving Quality of Experience for a limited set of internal
Viacom end-users and to present the depth and quality of test data synthesized by DMC.
Proposal
ViacomCBS test assets will be processed into the multi-source, multi-path XCD format according
to the ViacomCBS Adaptive Bit Rate ladder using Dolby processing technologies. Using a
combination DMC’s XCD component services and DMC’s Broker component services for
decisioning, the system will decide on the appropriate asset selection and delivery path for a
given session. Assets will be delivered via ViacomCBS’ current CDN vendors. Applications
integrated with Dolby’s Media Cloud SDK will support content playback via an internal Viacom
audience. Playback will initiated by the user and then automated according to scripts integrated
into the Test Application.
The player data will be captured and stored in the Dolby Media Cloud for processing.
Playback will be triggered according to scripts integrated into the Test Application.
Term
We expect the test to run for a period agreed upon with ViacomCBS, sufficient to develop a
statistically meaningful dataset.
Data Collection
Network QoS and playback QoE data will be collected for comparison to ViacomCBS historical
data for similar assets.
Test Audience
The test audience will include ViacomCBS employees with access to supported Android mobile
and television devices. As noted below, we are open to providing test devices.
Test Hypotheses
At the conclusion of the test, we will evaluate associated data to determine:

(1) That our multi-source, multi-path approach realizes a measurable improvement across
agreed upon network QoS and playback QoE metrics following delivery decisions instructed via
the Dolby Broker (XCD on/off) relative to the single-path control;
(2) That our system is able to maintain an immersive audio experience as network conditions
fluctuate based on the combination of pre-virtualization and decisioning via the Dolby Broker
for otherwise “challenging” content played back on Android devices;
(3) That the data collected via the DMC system will compare favorably to other reasonably
similar first- or third- party ViacomCBS data sources.
Dolby Commitment
To support the test within ViacomCBS’ test infrastructure, Dolby will provide:
(1) appropriate content processing using Dolby’s Hybrik content processing system;
(2) a fully-integrated test application (for internal audience) for use on Android test devices;
(3) requisite engineering support for setup and test execution, including CDN configuration;
(4) if necessary, the Android test devices for deployment to the limited ViacomCBS test
audience.
Viacom Commitment
ViacomCBS will provide:
(1) test assets that can be distributed to Android devices “in the clear”, without content
encryption;
(2) asset processing parameters for use via Hybrik on AWS EC2/S3 instances in the same region
as ViacomCBS infrastructure;
(3) CDN configuration across the range of CDNs used by Viacom today for multi-CDN delivery
testing;
Test Synthesis
At the conclusion of the test period, we will meet together to review the synthesized data and
execute proper comparison to determine the performance of the system against the agreed
upon criteria (e.g. the items noted above). During the synthesis, we will assess further
deployment of Dolby Media Cloud for testing within an in-market consumer audience.
