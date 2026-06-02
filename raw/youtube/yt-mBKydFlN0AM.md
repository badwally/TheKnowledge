---
schema_version: 1
id: yt-mBKydFlN0AM
type: youtube
title: Language models align with brain regions that represent concepts across modalities
url: https://www.youtube.com/watch?v=mBKydFlN0AM
authors:
- Conference on Language Modeling
ingested_at: '2026-06-01T23:58:37Z'
content_hash: sha256:56d816a6d01588c6710070d2005376ed99b425c1e70064cf966f3cc448764f66
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Conference on Language Modeling
  channel_url: https://www.youtube.com/@colm_conf
  duration_seconds: 662
  caption_track: fetched
  snippet_count: 292
filter:
  score: 0.7
---
[0] My name is Maria Riskina and today I'll
[2] present our work that shows that
[4] language models align with brain regions
[6] that represent concepts across
[7] modalities. Uh concepts are considered a
[10] key unit of human cognition and the
[12] question of whether language models can
[14] represent conceptual meaning has long
[16] been of interest to scientists in
[17] different fields. On the on the
[20] theoretical side, there are opinions of
[22] both ends of the spectrum with strong
[24] intuitions uh and much back and forth
[27] between them. But in terms of empirical
[29] evidence, we now know that language
[31] models can uh capture relationships
[34] between visual concepts like colors from
[36] text only. Models trained on only text
[39] or only images have been found to
[42] independently converge on similar
[43] representations to the extent that it's
[47] been posited that what these models
[49] learn is a shared statistical model of
[51] reality just in different projections.
[55] Another piece of evidence that fits into
[57] this is the growing body of work that
[59] shows similarities between
[60] representations learned by artificial
[62] neural models and representations
[64] estimated from brain activity with some
[66] work in particular showing that model
[68] representations converge not only with
[71] each other but with the brain as well.
[74] uh the work on measuring alignment
[76] between models and brains usually
[78] extracts the brain side representations
[80] from established networks of brain
[82] regions and those networks are often
[84] modality specific. So if we're looking
[86] for a representation of a text input we
[89] would use the language network. If it's
[90] images you would use the visual cortex
[93] etc. But if we wanted to extract
[95] representations of concepts that are not
[97] tied to any particular modality, there
[99] isn't a network of concept processing
[102] regions that we could use for that. How
[104] the human brain represents concepts is
[106] still an open question. Uh Francisco
[109] Pereira and colleagues had actually
[111] collected a data set that targets
[113] conceptual representations in the brain.
[115] So they started with a list of 180
[118] concept words which could be different
[120] parts of speech and for each word they
[123] created stimuli that represented those
[125] concepts in three different formats they
[127] call paradigms. The first is a sentence
[130] with the concept word. The second is a
[133] picture labeled with the concept word
[136] and the third is a word cloud in which
[138] the concept word is surrounded by other
[140] related words.
[142] And those stimuli were created for each
[145] concept in the list. They actually
[146] created several stimuli for each
[148] paradigm, but I'm only showing one
[151] example here for each. Uh, and then they
[154] were shown to participants. And
[155] participants were asked specifically to
[157] think about the meaning of the sentence
[159] or picture or wordcloud uh in the
[162] context of the highlighted concept word.
[164] And while they were doing that, their
[166] brain responses were recorded using
[168] fMRI. So the full data set contains for
[170] each participant brain activations for
[173] four to six stimuli sentences, pictures
[175] and word clouds per concept.
[178] And the way fMRI works is it records
[181] changes in blood flow across the brain
[183] at the time of viewing a stimulus. And
[186] for that the brain is discretized into a
[188] grid of small units of volume called
[190] vauels. And for each vauil we have one
[193] activation value per stimulus.
[197] Now for every vauel we can aggregate
[199] those activations within a paradigm. And
[201] here I'm starting with sentences. The
[204] goal here is to have a vector of
[205] activations with 180 elements each
[208] corresponding to one concept. Since
[211] there are multiple sentences for each
[212] concept, we average the activations over
[214] them. And then we do the same for
[217] pictures and for word clouds. And now we
[220] have a vector for each paradigm. And we
[222] can compute pair-wise correlations
[224] between them. And finally we average
[226] these correlations to obtain one final
[228] value which we call semantic
[230] consistency. It shows how consistent a
[232] voxil's response uh to concepts is
[235] across paradigms. So uh semantic
[239] consistency is high for vauels that
[241] respond strongly to the same concept
[244] regardless of which modality which
[246] paradigm it's presented in. When we look
[249] for where the vauels with statistically
[252] significant semantic consistency are, we
[255] find that they are concentrated in the
[257] left hemisphere. Uh, and when we
[259] threshold this map using an anatomical
[261] segmentation of a brain cortex, we end
[264] up with these three regions of interest
[266] or roy I'm showing them in different
[268] colors. And these are regions where
[270] these uh semantically consistent voxels
[273] are concentrated. And we think this is a
[274] good proxy for the hypothetical concept
[277] representation network. Uh generally one
[280] should be cautious with claims about
[282] what a particular brain area does. But I
[284] wanted to give a little bit of context
[286] from prior work in neuroscience here. So
[288] these red areas I'm showing are roughly
[290] where the language network is found in
[292] most people. So one of our regions
[294] overlaps with those and one is adjacent
[297] and the exhibitor temporal cortex known
[299] to be involved in visual processing
[300] overlaps with our third region. So now
[303] that we know which regions we will be
[305] looking at, we can start comparing them
[307] against language models and for that we
[309] have two method and the first one is
[312] brain encoding. Given a stimulus, we
[315] extract its representation from the
[317] language model and from the brain in the
[319] form of activations and then we fit a
[321] ridge regression model to predict brain
[324] activations from language model
[325] representations.
[327] On the language model side, we compare
[329] 15 transformer models that we chose
[332] specifically to look for correlations
[334] with known factors like scale within the
[336] same family, effect of instruction
[339] tuning or multimodality where we compare
[341] vision language models with just their
[343] base language counterparts.
[346] And for each model, we run cross
[348] validation to choose the layer and token
[349] pooling method that yields the best
[351] predictive performance.
[354] uh we start by predicting brain
[356] activations across the whole brain. So
[358] each point on this plot is a piece of
[360] the anatomical segmentation that I've
[361] shown earlier. The yaxis shows the
[364] correlation between the predicted
[366] activations and the ground truth ones.
[368] This is how we evaluate brain encoding.
[370] Uh and we report mean performance across
[372] all models because in this experiment
[374] they were actually very very similar.
[377] X-axis shows semantic consistency and
[379] you can see that predictive performance
[381] is correlated with it and that actually
[383] holds for all three of our paradigms. So
[386] brain areas with higher semantic
[387] consistency are better predicted by
[389] language models. Uh the only outlier is
[392] this cluster of areas I'm highlighting.
[394] Those are all areas of the visual
[395] cortex. So of course they're good at
[397] representing pictures but not
[399] necessarily crossmodel meaning. Then we
[402] zoom in on our three regions. And here
[404] because of the potential overlap with
[406] the language network, we want to see if
[408] this predictive performance is actually
[409] driven by semantic consistency or by how
[412] much an area responds to language. And
[414] by response to language, I mean a uh
[417] measure from prior work in neuroscience
[420] where uh you compare how strongly an
[422] area gets activated by sentences as
[424] compared to lists of madeup nonwords. So
[428] to do this in a controlled way, we split
[430] all the vauels in each of our roy into
[432] quartiles. So each vauil falls into a
[435] bin from one to four based on how high
[437] it semantic consistency is and then
[439] another bin from one to four based on
[441] how high its language response is. So
[443] vauels are now grouped by cartisian
[445] products of these two sets of quartiles
[447] and then we hold one of the variables
[449] fixed and vary the other and see how
[451] predictive performance changes across
[453] quartiles. So here each row of plots
[456] corresponds to one region and the x-axis
[458] is quartile by semantic consistency and
[461] each line corresponds to a language
[463] response quartile. So we're varying
[466] semantic consistency while holding
[468] language fixed and for all of our for
[471] all paradigms the lines go up. There is
[473] a strong correlation between
[475] productivity and consistency. But when
[477] we do the opposite, we fix consistency
[479] and we vary language response. The
[482] correlation is less conclusive,
[484] especially if you compare to what we
[486] just saw for semantic consistency. And
[489] it's especially noticeable for the third
[491] region here, which shows no correlation
[493] with language at all. You can see that
[495] all the blue lines are kind of flat. Um,
[498] and in fact, this region does not really
[501] respond to language at all. It is not a
[503] language processing region. So uh
[505] semantic consistency correlates with
[507] productivity even when it's decoupled
[509] from language.
[511] And our second method is
[512] representational similarity analysis
[514] where we take all the stimuli from all
[516] three paradigms and we average their
[518] representations separately in the model
[520] and in the brain to get a single
[522] representation per concept on either
[524] side. We can then compute how dissimilar
[527] each pair of concepts is in the model
[530] and in the brain and finally correlate
[533] those distance matrices to measure how
[535] alike the representational geometries of
[537] the two spaces are.
[539] Uh here again each row corresponds to a
[542] brain region and each pair of bars to a
[544] particular model. The gray bars show the
[546] baseline where we randomly shuffle the
[548] ordering of the concepts on the brain
[550] side. So they're not matched with the
[552] language model side. And in all three
[554] regions, the actual correlation is
[557] actually significantly greater than this
[559] randomized baseline. All the models I'm
[561] showing here are text only. So we can
[564] only use text stimuli, sentences and
[566] word clouds. But for vision language
[568] models, we look at two settings, text
[570] only for fair comparison with unimodel
[573] ones, and one where we use both text and
[576] images. And the results with both text
[578] and images here shown by the lighter bar
[580] uh tend to be higher than with text only
[583] shown by the darker bar. There are some
[585] differences between models but they're
[588] not very prominent and we didn't find
[590] that they correlate with model size or
[592] instruction tuning uh which were both uh
[595] shown in prior work to be factors that
[597] contribute to model brain alignment. uh
[600] and we also find that multimodal models
[602] in the textonly setting perform
[604] comparably to their language only
[606] counterparts.
[608] Uh so to sum up we introduced a new fMRI
[611] based measure of semantic consistency.
[613] We used it to find brain regions that
[615] represent concepts consistently across
[617] modalities. We used two methods for this
[620] analysis. Uh brain encoding which is
[623] prediction based and RSA which measures
[626] alignment of representational spaces. We
[629] find that encoding performance strongly
[631] correlates with semantic consistency
[633] even in regions with low response to
[635] language.
[636] Uh and we find significant
[638] representational similarity between
[640] models and semantically consistent brain
[642] regions which in vision language models
[644] further increases when both images and
[646] text are used. And together we think
[648] this can be viewed as evidence for the
[651] model's ability to capture crossmodel
[653] conceptual meaning.
[657] Thank you very much and I'll be happy to
[659] take any questions.
