---
schema_version: 1
id: yt-9_vHZoQPHcc
type: youtube
title: Implementing Knowledge Graph Quality Assessment | Panos Alexopoulos | Connected
  Data London 2025
url: https://www.youtube.com/watch?v=9_vHZoQPHcc
authors:
- Connected Data
ingested_at: '2026-06-17T20:57:25Z'
content_hash: sha256:6fb0462d2a5e30521aa3d117350d11c0a3492671b2201bdfaca0547e43616bb7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Connected Data
  channel_url: https://www.youtube.com/@ConnectedData
  duration_seconds: 161
  caption_track: fetched
  snippet_count: 63
filter:
  score: 0.7
---
[6] So
[9] managing and controlling the quality of
[11] a knowledge graph is not something that
[13] you do
[16] in one step. Right? When you build and
[19] you maintain knowledge graph, it's
[20] something that you need to do it in a
[22] life cycle form consistently. You start
[25] with selecting the quality dimensions.
[27] What do I care to measure? Do I care
[29] about accuracy? Do I care about
[31] completeness? Do I care about
[33] consistency?
[34] What is the relative importance? For
[37] instance, there is a standard tradeoff
[39] between accuracy and completeness. In
[41] the same way that in machine learning,
[42] you have the trade-off between precision
[44] and recall, right? If I want higher
[48] completeness, I can just loosen the
[50] controls of my h of my extraction
[55] methods. Add things in there. There will
[58] be wrong things but there will be also
[59] correct things. So completeness is
[62] magically improved.
[65] The second step is to define metrics
[66] quality metrics. How do I measure
[68] accuracy? How do I measure consistency?
[72] And most importantly how do I interpret
[74] the results right? I think as in many
[77] things telling me that you have a
[79] knowledge graph that is 80% accurate
[81] doesn't tell me a thing. I need to
[83] understand if this 20% is important for
[85] my business or not. right or for the
[88] applications that it uses it. It might
[90] be that in some aspects it is highly
[93] accurate in some other subdomains or
[95] some other particular relation is very
[97] bad which means that it's it's not so so
[100] usable there. A third step is to define
[103] and implement quality signals.
[105] Signals are
[108] very often confused for um for metrics
[112] but it's not really the same. So signals
[115] are um things that when you see they
[119] grow the suspicion that something is
[120] wrong
[123] but they don't necessarily um reflect
[126] the the quality. A fourth step is to
[130] define diagnostic and fixing actions.
[132] Okay, we see that something is wrong.
[136] Why is it wrong? We've seen that we have
[139] for example a lot of bad synonyms. What
[141] is the problem? Is the problem the data
[143] source that we used? Is the problem the
[146] methods that we used? Right? So, so to
[148] go back and do root root anal root root
[150] cause analysis stuff. And finally, we
[153] need to operationalize that determine
[155] who and when is going to be monitoring
[156] the quality and how should they should
[158] they act.
