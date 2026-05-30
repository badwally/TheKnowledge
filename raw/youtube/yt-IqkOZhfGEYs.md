---
schema_version: 1
id: yt-IqkOZhfGEYs
type: youtube
title: Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs
url: https://www.youtube.com/watch?v=IqkOZhfGEYs
authors:
- MITCBMM
ingested_at: '2026-05-30T21:59:46Z'
content_hash: sha256:8d9bfda47439c12858d8036cc6212d0fa1722965244c41af9ec16cc6648cfb48
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: MITCBMM
  channel_url: https://www.youtube.com/@MITCBMM
  duration_seconds: 204
  caption_track: fetched
  snippet_count: 88
filter:
  score: 0.8
---
[0] [MUSIC PLAYING]
[4] MARTIN SCHRIMPF: Before
we started this project,
[6] research in neuroscience
was typically
[8] at an individual,
experimental level.
[11] You collected data from,
for instance, V4 or IT,
[13] and then you test one V4
model and one IT model,
[16] and those are usually separate.
[17] So what we're trying here is to
start an integrative approach
[20] that really combines
experiments at multiple levels
[22] and puts more
constraints on the models
[24] to be more and more brain like.
[26] For the first set
of benchmarks, we
[27] connected two neural benchmarks
and one behavioral benchmark.
[30] The two neural benchmarks were
high quality, UTI recordings
[34] from V4 and IT,
sort of high level
[37] areas in visual processing.
[39] And the behavioral
benchmark was from humans
[41] doing a matching sample task.
[42] The set of these benchmarks
together is what we call
[45] Brain-Score .
[46] On the model side, we also
collected daily use models
[49] in machine learning.
[50] So these were ranging
from early AlexNet
[52] all the way to the latest
and greatest ResNets
[54] or PNASnet at the time.
[56] And then we evaluate
those models
[58] on how well they could predict
the neural activity in V4
[60] and IT and on how well they
could capture human behavior
[64] on a fine grain image level.
[66] JONAS KUBILIUS: So when we
benchmarked all of these models
[68] on brain score, we
found that there
[71] is a very robust
global correlation,
[73] such that models that are
performing better on image nets
[77] are also more predictive
of brain responses.
[81] However, the state of
the art model on ImageNet
[84] is not the best model for
predicting brain responses.
[88] So it seems like, if you're
only optimizing for ImageNet
[91] that that strategy may
not be sufficient anymore
[95] to get the best
models of the brain.
[99] So when you look at the
best Brain-Score models,
[102] they are doing their job.
[104] They're predicting neural
and behavioral responses
[106] as we want it.
[107] However, they have many layers.
[111] And that is quite
at odds how we tend
[113] to think about visual
system, where there is just
[116] a handful of visual areas.
[117] The mapping becomes pretty
tricky between the models
[120] and visual system.
[122] And there is another problem.
[124] All of these models
are feet forward,
[126] while the visual system
is quite recurrent,
[129] and recurrence plays
an important role
[131] in how we recognize objects.
[134] So we decided to
develop a model that
[136] would be shallow and recurrent.
[138] And that recurrence would
be compensating for the lack
[141] of depth in the model.
[144] MARTIN SCHRIMPF: Now testing
CORnet on the ImageNet
[146] benchmark, we found that it
was actually very competitive
[148] compared to other models,
especially considering
[151] its shallowness.
[152] JONAS KUBILIUS: And we
also saw that it's actually
[154] doing really well
on Brain-Score,
[157] which was our target goal.
[159] Now, on top of that,
we thought, well,
[161] this is a recurring model.
[163] So how about we try to predict
neural responses over time?
[167] Which is not what these
feed-forward models could do.
[170] Happily enough, we found
a very good correlation
[172] between these measures.
[174] MARTIN SCHRIMPF: In
addition to that,
[175] we also tested how well
could this model transfer
[178] to another data set?
[179] And we found that it
really outperformed
[180] comparable shallow models.
[182] Now going forward,
we're trying to expand
[183] our set of integrative
benchmarks even more.
[186] So we're going to put in V1,
V2 processing, more behaviors
[190] and so forth.
[191] And our plan is to test
CORnet all of them along
[193] with the other models.
[194] In addition, we're opening
up the Brain-Score platform
[196] for new submissions.
[197] So if you think
you have the best
[198] model for image
processing in the brain,
[199] please send it our way.
[200] [MUSIC PLAYING]
