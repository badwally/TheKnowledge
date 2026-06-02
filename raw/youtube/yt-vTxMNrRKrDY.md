---
schema_version: 1
id: yt-vTxMNrRKrDY
type: youtube
title: A shared neural encoding model for the prediction of subject-specific fMRI
  response (MICCAI 2020)
url: https://www.youtube.com/watch?v=vTxMNrRKrDY
authors:
- Sabuncu Lab
ingested_at: '2026-06-01T23:58:56Z'
content_hash: sha256:3c5a23b9d134f08d909ddd4790e8c8485d8bd525ffa612cff6c0d8badd92bbd9
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Sabuncu Lab
  channel_url: https://www.youtube.com/@sabunculab5182
  duration_seconds: 593
  caption_track: fetched
  snippet_count: 311
filter:
  score: 0.72
---
[3] hi everyone
[4] i'm meenakshi and i'll be presenting our
[6] work on a shared neural encoding model
[8] for the prediction of subject-specific
[10] fmri response
[11] this is joint work with jia keith amy
[14] and my advisor mert up
[17] so let me start with a basic description
[19] of what encoding models are
[21] and how they can be useful in
[22] neuroscience encoding models are popular
[26] computational models in sensory
[27] neuroscience
[28] that are used to predict how neurons or
[30] populations of neurons across the brain
[32] respond to complex naturalistic stimuli
[35] these encoding studies
[37] typically use machine learning methods
[38] to predict fine-grained brain activity
[40] from stimulus features
[42] at this point it is important to ask
[44] what is the use of these encoding or
[46] predictive models in cognitive
[47] neuroimaging
[49] in the past sensory systems have been
[51] studied extensively using task-based
[53] paradigms
[54] where the brain activity is recorded
[56] upon stimulation with hand-crafted
[57] stimuli
[59] this paradigm has been very successful
[61] for example in identifying scene
[63] selective or phase selective regions in
[64] the brain
[66] while successful for testing specific
[68] hypotheses this approach is limited
[70] in the sense that no single task-based
[72] experiment can help in developing broad
[74] theories of sensory processing in the
[76] brain
[77] predictive models on the other hand are
[79] based on our sample prediction
[81] and they generalize to arbitrary new
[83] stimuli and can thus offer
[84] more holistic descriptions of sensory
[86] processing in an individual
[88] the biggest advantage is that once we
[90] have such a general model
[92] we can use it to generate normal
[93] hypotheses about information processing
[96] that can then be tested under more
[97] controlled conditions
[99] these models can also be used in other
[101] applications such as neural population
[103] control
[104] by optimally synthesizing stimuli to
[106] elicit a desired neural activation
[108] pattern
[111] as a main motivation behind our work on
[113] shared urine coding
[114] we know that building accurate subject
[116] level models of brain function
[118] often requires large amounts of data per
[120] subject for good generalization
[122] however most encoding studies are
[124] constrained by the size of their
[126] stimulus set
[127] due to the time consuming and expensive
[128] data acquisition process
[131] further subject level data especially if
[133] acquired in single childs can be very
[135] noisy
[136] there is very limited work in leveraging
[138] multi-subject data
[139] for more robust and accurate
[141] individualized neural encoding
[143] in this study we attempt to address this
[145] limitation and our main goal is to
[147] leverage group level data
[149] to improve subject-specific response
[151] prediction
[153] in in the present study we developed
[155] both visual and auditory encoding models
[158] that predict fine-grained voxel-level
[160] brain activity patterns from draw images
[162] and auditory spectrogram inputs
[164] respectively these neural encoding
[166] models comprise two components
[168] a feature extractor which pulls out the
[170] relevant features from raw images
[172] or audio waveforms as shown by the
[174] s-vector in the figure
[175] and a response model which maps these
[177] stimuli features into brain responses
[180] ideally you would expect inter-subject
[182] knowledge transfer
[183] to be successful if different subjects
[185] share similar cortical representations
[186] of naturalistic stimuli
[189] indeed recent studies have revealed that
[191] coarse screen response topographies are
[193] highly similar across subjects
[195] and naturalistic stimuli such as movies
[197] engage a large portion of the brain
[199] invoking a response that is shared
[201] across individuals
[203] in light of these observations we
[205] propose the illustrated shared encoding
[207] framework
[207] with a novel convolutional response
[209] model assuming that individual
[211] differences mostly occurred to find a
[213] scale
[213] and that there is a significant response
[215] component that is shared across
[217] individuals
[218] we propose to leverage a shared response
[220] model such that early layers of this
[221] model
[222] which capture core screen responses are
[224] common across subjects while the deeper
[227] layers which predict this fine grained
[228] responses are subject specific
[231] this is similar to a multitask learning
[233] setup where we are using a single shared
[235] architecture
[236] to predict the responses of multiple
[238] subjects the main advantages here
[240] are that we can combine data from
[242] multiple subjects into a shared model
[244] and this approach allows simultaneous
[246] optimization of encoding models across
[248] subjects
[249] further since only a handful of
[251] convolutional layers are subject
[252] specific
[253] it poses minimal memory overhead with
[255] additional subjects
[256] and can thus handle fmri data sets with
[258] a large cohort
[260] finally this approach is amenable to
[262] incremental learning
[263] with divorce reading stimuli across
[265] subjects with less constraints on data
[267] collection from single
[268] subjects
[272] in our experiments we study 70 fmri
[275] recordings from a randomly selected
[277] sample of 10 subjects from the hcp movie
[279] watching database
[281] the data set comprises four audio visual
[283] movies each nearly 15 minutes long
[286] we split the first three movies for
[287] training and validating our models
[289] and use the fourth held out movie for
[291] independent independent testing of our
[292] models
[294] we compute log mel spectrograms over
[296] every 1 second of audio waveform in the
[298] movies
[298] to obtain a 2d image like input for the
[300] audio feature extractor
[302] and extract the last stream of every
[304] second of the video
[305] to present to the visual representation
[307] network for obtaining visual features
[312] here is a short glimpse of the stimulus
[314] and response data for a single movie in
[315] the hcp dataset
[317] the left figure shows the average
[319] response across all subjects
[320] whereas the right figure shows the
[322] stimulus frames the subjects also listen
[324] to the corresponding audio
[326] while lying inside the scanner
[331] we evaluated all our models by computing
[333] the pearson's correlation coefficient
[335] between the predicted and measured
[337] response at every voxel
[339] and summarize the performance of models
[341] by computing mean correlation
[342] across all stimulus driven voxels we
[346] compared our approach
[347] against encoding models with the same
[349] architecture that are trained with
[350] single subject data
[351] as well as against individual level
[353] encoding models that employ a linear
[355] response model instead of the proposed
[357] convolutional response model
[359] the top row shows the performance of all
[361] auditory encoding models
[363] whereas the bottom row shows the
[364] performance for visual models
[366] in both cases we find that the shared
[368] encoding model
[369] consistently performs better than
[371] individual encoding models
[373] that are chained separately on single
[374] subjects in terms of both the mean
[376] correlation
[377] as well as the number of boxes that show
[379] significant correlation between the
[380] predicted and measured response values
[384] finally it is important to note that the
[386] shared model does not simply predict a
[388] mean response
[389] but indeed captures meaningful
[390] individual level idiosyncrasies pretty
[392] well
[393] this is most clearly seen by the
[395] diagonal nature of matrices on the right
[396] hand side
[397] which show that the predicted response
[399] for a subject best matches the actual
[401] response of the same subject
[405] we also visualize the correlations
[407] between the predicted and measured fmri
[409] response
[410] across the cortical surface for both the
[412] proposed models
[413] the figure here shows the average
[415] correlations across all the 10 subjects
[417] in our study
[418] for the auditory model we see
[420] significant correlations in the parable
[421] auditory cortex
[423] extending into some other language areas
[425] as well for the visual model
[427] while we see significant correlations
[428] across the entire visual cortex
[430] the performance is much better in higher
[432] order visual regions across
[434] both the dorsal and ventral visual
[435] stream
[439] next we wanted to investigate the
[441] possibility of using encoding models as
[443] neural activity synthesizers
[445] given that we have a predictive model
[447] linking stimulus and brain activity of
[449] each subject
[450] we can feed its stimuli from alternate
[452] paradigms such as task fmri
[454] here for example we used phase and scene
[457] stimuli from the hcp working memory task
[460] next we used synthesized or predicted
[462] neural activity for these stimuli
[464] to generate subject-specific contrasts
[466] and computed the dice overlap
[468] between the predicted contrast for each
[469] subject against the true contrast of
[471] every subject
[472] to produce an n cross n matrix for each
[474] contrast where n
[476] is the number of subjects the diagonal
[478] dominance in the dice matrix for both
[481] phase and scene contrast suggests that
[483] the predicted contrast for a subject
[485] are more similar to the same subject's
[487] true contrast
[489] further we didn't observe a prominent
[490] diagonal structure
[492] for individual subject models presumably
[494] because they generalize poorly to art of
[496] domain stimuli
[498] importantly the predicted contrast
[500] highlight areas previously known to be
[502] involved in the processing of faces and
[504] scenes
[505] for example the fusiform face area is
[507] consistently seen in phase contrasts
[510] whereas the para hippocampal areas are
[512] seen in the scene contrast
[514] this agreement with results known from
[515] task-based experiments
[517] suggests that these encoding models
[519] could indeed have applications in
[520] personalized brain mapping
[527] to conclude we've made a promising step
[529] towards shared neural encoding models
[532] this approach enables us to build
[534] predictive models of neural responses
[536] across different subjects in concert
[538] rather than in isolation
[539] and thereby facilitates inter-subject
[541] knowledge transform
[543] further it allows us to exploit the
[545] redundancies or shared response across
[547] subjects
[548] so that we can build much better
[549] predictive models of neural responses
[551] with limited data from individual
[553] subjects
[554] to enable end-to-end optimization of the
[556] shared model for whole brain response
[558] prediction
[559] we proposed a convolutional response
[561] model that dramatically reduces the
[563] number of free parameters
[565] in comparison to a linear response model
[567] while yielding better predictions
[569] finally we found that these models can
[572] generalize remarkably well to
[574] out-of-domain stimulus sets from
[575] alternating cognitive paradigms
[577] and thus demonstrated their application
[579] as virtual neural activity synthesizers
[581] for personalized brain mapping
[586] thank you for listening i'd be happy to
[588] take any questions during the oral or
[589] poster session
