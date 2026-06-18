---
schema_version: 1
id: yt-IWIiR6mjrXY
type: youtube
title: Aligning representations in brains and machines. Elizabeth Dupre.
url: https://www.youtube.com/watch?v=IWIiR6mjrXY
authors:
- MAIN Conference
ingested_at: '2026-06-01T19:55:49Z'
content_hash: sha256:bd0c0e654d9daed46db8e20fea68e4f5f88f09420a548fd2975ce8af5fbffe4f
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: MAIN Conference
  channel_url: https://www.youtube.com/@MAINConference
  duration_seconds: 2433
  caption_track: fetched
  snippet_count: 1013
filter:
  score: 0.7
---
[0] they'll be able to relate them. So,
[2] please don't hesitate to reach out.
[5] So, I'm really so happy to be here today
[7] to talk to you uh about a topic that's
[9] near and dear to my heart, which is
[11] aligning representations in brains and
[13] machines. And to kind of step back, uh I
[16] wanted to motivate a little bit why, you
[18] know, I care a lot about this topic, but
[20] why I think you might be interested in
[22] it as well. So let's say that you're um
[26] a neuroscientist and you're working uh
[29] with human data and maybe you've thought
[32] a little bit already about the problem
[34] of comparing across individuals and the
[37] idea so far is that okay yes if I want
[41] to move beyond case studies I need to
[43] have some way to map between neural
[45] activity patterns in participant one and
[48] participant two. Um but the way that we
[51] commonly do that as a field in
[53] neuroscience is to align to some known
[55] anatomical template. Um the problem is
[58] that we've known uh basically as long as
[61] the field of cognitive neuroscience has
[63] existed that this doesn't totally solve
[65] our problem for us right in terms of
[67] making a mapping. So, for example, this
[70] is um a really nice illustration of one
[72] particular brain region, though there
[74] are many others we could call out um
[76] known as Hesshel's gyrus. And within
[78] Hessel's gyrus, you see that depending
[81] on the particular individual you're
[82] looking at, this can present as a single
[85] gyrus, hence the name, or it can
[87] actually present as a completely
[88] duplicated gyrus. And it's not clear how
[91] to establish a mapping between these two
[93] different kinds of anatomy, right?
[95] There's no consensus. you wouldn't
[96] necessarily say, "Okay, everyone gets a
[98] half gyrus, right?" Um, so how could we
[101] make comparisons here? And maybe you
[104] say, "Okay, that sounds like it's a
[105] problem for humans because we're looking
[107] at these really high level spatial
[109] scales, but if we go to a really fine
[111] spatial scale or maybe if we move to a
[113] different model system with a different
[115] kind of anatomy, maybe that problem goes
[116] away." Unfortunately,
[119] um, systems neuroscience, uh,
[121] neuroscience more broadly has really
[122] seen that moving to higher spatial
[124] resolutions, even single neuron
[126] resolutions or to animal models, does
[128] not resolve these challenges of how to
[130] make inferences across individuals. And
[133] even actually they've exacerbated um the
[135] problem because now when we have access
[137] to this really high resolution data
[139] within individuals we see that um you
[142] know if you're doing invasive recordings
[144] with implant degradation or even in
[146] non-invasive recordings changes in
[148] neuronal plasticity and representational
[150] drift can yield substantial within
[152] individual changes and make it really
[154] complicated to compare the same
[156] individual's recordings over time.
[159] So here's an example just to kind of
[161] illustrate what I mean. Um so this is
[164] from Laura Driscoll and colleagues but
[166] summarized in this really nice opinion
[167] piece by uh rule and colleagues. And
[170] basically what they're showing is this
[171] is calcium imaging data from the
[173] posterior parietal cortex of a mouse
[174] while he navigates a T- maze. Um and so
[178] what you can see is that here are the uh
[181] calcium imaging signals from these a
[184] variety of posterior parietal cortex
[186] neurons. And if you look at Q offset um
[190] and you sort by day one's activity, you
[193] see that the mean activity in day one
[195] displays this really typical syosoidal
[197] pattern that we expect. Um but then if
[199] you keep the cell sorting from day one
[201] and look at day 10 or day 20, it seems
[204] as though the effect has gone away,
[205] right? It seems as though the neurons
[207] are no longer representing the same
[209] pattern. But in fact what we see is that
[210] if we resort by day 10 um and day 20
[215] that the pattern is persisting over time
[218] the population activity is still
[220] encoding for the same concept in this
[222] team. It's just that the specific
[224] neurons that are being recruited have
[226] changed. And so if we create a decoder
[228] for example that relies on these exact
[231] neurons it's going to start failing over
[233] time even though the population activity
[236] is persistent. Right? And so this makes
[239] it really complicated to do things like
[241] create brain machine interfaces. [sighs]
[244] Um and so maybe you say, "All right, I
[246] believe you now. I could see that this
[248] would be a problem in humans. I could
[250] buy that this would be a problem um you
[252] know in neuroscience quite broadly, but
[253] this seems like it's all a biology
[255] issue. If I'm in silic
[261] um in fact it does uh persist even in
[264] silicone. So if we're looking at
[265] artificial neural network instances, we
[267] see that convolutional and recurrent
[269] networks both show individual
[271] differences in learned representations.
[273] And importantly, this is independent of
[275] the classification accuracy that they're
[277] able to achieve. So even for um you know
[281] near identical identical classification
[283] accuracies, you can see these individual
[285] differences and these differences are
[287] persistent. So they're occurring even
[289] with the exact same architecture and
[290] with the same training set of data. um
[293] this is say uh only the initialization
[296] differing. So this is a really nice
[298] figure from mirror colleagues kind of
[300] demonstrating the problem. Here we have
[303] a convolutional neural network and we've
[304] taken multi-dimensional scaling just the
[306] first two dimensions. And if we look at
[309] multiple instantiations of the same
[311] architecture of this CNN on the same
[314] training data and we look over time
[316] across the layers what we see is that in
[319] the initial layers the representations
[322] are relatively conserved across the
[324] different instances across the different
[326] uh individual networks. But as we move
[329] through the layers, we see more and more
[331] individual differences um in terms of
[333] how
[335] uh each layer uh has representations
[338] that are are being orchestrated by the
[339] hidden units. So it does seem as though
[342] these individual differences are
[343] persistent really at any kind of neural
[346] system we're looking at, biological or
[348] artificial. Um and as you can imagine
[352] perhaps what this is setting up is that
[354] if we have these differences in uh
[357] comparing within biological systems and
[360] we similarly expect these differences in
[362] comparing within artificial systems then
[365] if we want to start um comparing across
[368] biological and artificial networks as
[370] this really lovely figure by Dan Yemens
[372] and colleagues suggests um we're just
[374] going to compound our problems. It's
[375] going to be really quite difficult to
[378] find a key way
[380] in which we can systematically compare
[383] between two systems that are themselves
[385] uh very diverse.
[387] And so the question I'm sort of posing
[391] uh in this talk is within a single data
[394] modality. So saying for the moment that
[396] we just want to cut down the noise and
[398] just look within uh biological systems
[402] or just look within artificial systems,
[404] how can we actually go about comparing
[406] learned representations across
[408] individuals and across experimental
[410] conditions? And what I've hoped uh I've
[413] kind of motivated a little bit um is
[415] that this is not a trivial problem. This
[418] I think is really a core challenge for
[420] the fields of neuroscience and AI
[422] separately and especially for us at this
[424] intersection of neuroi.
[427] So in my talk today I'm going to talk
[429] about a few different strategies that
[431] are currently in place and I'm going to
[433] in particular argue for alignment um as
[436] a really exciting strategy that uh I
[439] think you'll hear a lot more about at
[440] the in the main talk as well main talks
[444] um as well. Um, and I'm going to lay out
[447] some considerations that you might want
[448] to have when you're working with
[450] alignment and also provide some
[451] resources and recommendations for
[452] getting started with your own data, no
[454] matter what kind of data you're working
[456] with.
[458] So, first I want to lay out um this idea
[461] of measuring dissimilarity with metrics.
[464] So, this is perhaps the most common idea
[466] that you've likely already seen within
[468] the field. Um, and the the problem that
[472] we're trying to solve is basically this.
[474] we acknowledge that there are
[475] differences between individuals or
[477] across experimental conditions and uh we
[480] want to effectively measure that
[482] dissimilarity right so we want a way to
[485] say okay this is how dissimilar we think
[487] these really are
[489] this is an example um that I've lifted
[492] uh from a talk by Alex Williams um from
[494] his paper uh in Nurups last year and
[498] basically what this is showing is if we
[500] have these two toy data sets X and Y if
[503] we have some metric. In this case, it's
[506] orthogonal processes distance. It's
[508] going to provide us with a number. It's
[510] going to provide us with a
[511] quantification of how different these
[514] two particular toy data sets are um for
[518] this given metric. Right? And this can
[519] be really useful in a wide variety of
[521] circumstances. If you have two things
[524] that can't be compared for some reason,
[525] um you can only look at second level
[527] metrics. Maybe we want to just know
[530] these numbers. So this is really nice
[533] and useful. The problem of course is
[537] which metric to use, right? Um so the
[540] metric that you're going to use is in
[542] many cases constrained by the data that
[544] you have available and quite often by
[546] your field specific norms. So what do
[549] people expect you to report for this
[551] kind of data? Um unfortunately however
[554] each metric uh is only going to provide
[557] one kind of insight into the underlying
[559] structure of learned representation. So
[561] there's no single metric that is best um
[564] or is going to provide the most complete
[566] full insight into these data sets. Each
[569] one is going to provide a slightly
[570] different sense of the underlying
[572] structure and the differences between
[574] them. So for example, if we revisit
[576] these toy x and y data sets we saw with
[578] orthogonal progresses um which was uh
[581] going to just rotate x and y to look
[584] more similar that we get n one number.
[586] But if we look instead at a canonical
[588] correlation analysis based distance
[590] which is now uh invariant to any linear
[593] transformation we're going to see that
[595] we get a very different number right and
[597] it's going to say these are much more
[599] similar. And so it's not obvious uh
[602] perhaps which of these is right in any
[605] sense. Um but if we look at the field,
[609] what we see is that all of these
[611] measures and more are in really wide
[613] use. Um and so this is from a really
[616] lovely paper uh by Simon Cornblit and
[618] colleagues at ICML uh a couple of years
[621] ago. And what they're doing here uh is
[623] they're kind of sanity checking a number
[626] of metrics. So what we see is this is um
[630] uh on the x and y axis it's two
[632] different instances trained of a single
[634] convolutional neural network and they're
[636] calculating the layerwise similarity
[639] using all of these different metrics. So
[641] a CCA based meth uh metric again and
[644] then some variance this singular vector
[646] CCA a linear regression and then the
[648] metric they're proposing centered kernel
[650] alignment. Um and what they argue is
[652] that uh for these two instances of the
[656] same network, so same architecture, same
[658] training data, different
[659] initializations, we expect that uh
[662] across these metrics, the diagonal would
[664] be bright. You expect layers to always
[666] look most like themselves across uh
[668] initializations and the rest should be
[670] quite dark. But what we see is that for
[673] the given metrics, that's uh not
[675] necessarily the case. It very much
[676] depends on the particular metric of
[678] interest and on the given layers. And
[680] CKA perhaps performs best in this
[683] particular context, but by no means um
[686] is it perfect, right? It's not only
[688] showing a bright diagonal and dark
[690] everywhere else. So it's capturing one
[693] aspect of the similarity here.
[697] Um and perhaps you say okay that seems
[701] really interesting but the the metrics
[703] that I'm familiar with um have mostly
[705] come from the field and perhaps the most
[707] common metric in the field I would say
[709] right now across neuroi is
[711] representational similarity analysis um
[713] which has really been a workhorse for so
[715] much really exciting work that's
[717] happened um across all all of neuroi.
[721] So for those who aren't familiar with
[723] representational similarity analysis,
[724] it's another metric. Um, and the idea is
[728] that we're going to uh compare observed
[730] representational geometries. So
[733] basically what that realistically means
[735] is if we look at these two um activation
[739] spaces in this schematic, what we're
[741] going to do is we're going to say for
[743] each of these four different stimuli,
[745] we're going to uh plot their relative
[748] activation across the observed voxils in
[751] this new activation space. And then
[754] rather than trying to make direct
[755] comparisons voxil to voxil, we're going
[758] to compare the distances between the
[762] different stimuli within these two uh
[765] activational spaces. So the distances um
[768] are calculated within each activational
[771] space and then the difference is
[772] compared across and that allows us to
[774] derive a number which we use to um
[777] express the similarity. Right? So in
[779] spirit it's actually quite similar to
[781] all of the metrics I showed you
[783] previously, the CCA based ones, the
[786] centered kernel alignment one from
[787] Cornblath and colleagues. Um and
[789] mathematically they're actually very
[790] closely related as well. What's
[793] important though is that all of these
[794] measures uh so CCA, CKA, RSA are not
[799] true metrics in a mathematical sense,
[801] right? Um and this means that they don't
[804] satisfy a couple of important properties
[806] that we expect from metrics. Um, one of
[808] which Alex Williams and car colleagues
[810] pointed out just last year is the
[812] triangle inequality. Um, so they don't
[814] meet kind of the Pythagoras uh,
[816] intuition of how points um, on a
[819] triangle should be laid out if you have
[822] three points. And the problem with this
[824] um, is that okay, it doesn't need a
[826] mathematical definition, but in practice
[829] it can significantly complicate
[831] downstream analyses. So if you're just
[833] deriving the numbers to have the
[835] numbers, totally fine. But if you want
[838] to use the numbers to do something else,
[840] if you want to use the CKA value to do a
[842] clustering for example or a statistical
[844] analysis, it can be really quite
[846] difficult to do that in a systematic
[848] way.
[850] So
[852] all right we have differences um between
[856] systems biological and artificial and we
[858] have ways to quantify it um with metrics
[862] and I don't want to understate the role
[866] that metrics have played in neuroi they
[867] have provided hugely important insights
[869] into how systems are organized um and
[872] there's a lot of really active
[874] compelling work ongoing to define more
[877] rigorous metrics uh that meet
[879] mathematical definitions and still work
[881] well with neuroscience and artificial
[883] network data. Um, but at the end of the
[885] day, each metric is still only going to
[887] provide one perspective on the
[889] underlying representations that are
[891] learned in each of these systems, right?
[894] And so if we want to have um not just
[897] metrics but more than metrics, we're
[900] going to need uh to think about how we
[902] can actually compare across the systems
[904] themselves rather than only at these
[907] second level kind of uh extracted
[909] information. And to do that, I'm going
[912] to argue that we can uh think about
[914] alignment as a means to uncover richer,
[917] more dimensional um multi-dimensional
[920] information
[921] directly uh from the neural systems
[923] themselves.
[927] Okay. So, yes, I see Pierre in the chat
[930] um encouraging questions. Please don't
[933] hesitate to ask any questions. Um this
[935] is obviously a good point, but I'm very
[937] happy uh to be interrupted at any point.
[942] All right. So
[945] let's talk about alignment. Um so the
[949] basic premise of alignment is that
[951] whereas with metrics effectively what
[953] we're doing is we're operating in the
[956] different spaces um from different
[958] individuals or different experimental
[959] conditions. With alignment what we're
[961] trying to do is directly bring that uh
[964] disjoint data into the same space so we
[967] can make comparisons across them. So we
[969] can uh think about model fusion. There's
[971] all kinds of really exciting things that
[973] become possible when your data is
[975] actually comparable.
[978] So alignment uh is a pretty broad term.
[982] Um and there are lots and lots of
[984] methods that fall under this umbrella.
[987] So alignment can be done in a variety of
[989] ways. It can be done in high or
[991] lowdimensional space. So you can work
[993] directly in the space of the data that
[996] you have uh in voxal space in sensor
[999] space in uh the full hidden units of
[1002] your layer space or you can learn latent
[1004] factors a lower dimensional manifold and
[1007] work on aligning that instead. Um you
[1010] can also do alignment using labeled or
[1013] unlabeled experimental data. So you can
[1016] do it knowing correspondence between
[1018] your time points and leveraging that to
[1020] help drive your alignment or you can do
[1022] it without knowing correspondence
[1023] between your time point where you're
[1024] really just looking for these really
[1026] rough curistic um comparisons across uh
[1030] disjoint distributions and importantly
[1033] depending which we'll talk about in a
[1035] little bit. Um but in many cases these
[1037] alignments can then be reused in new
[1039] data uh which opens up some really
[1041] exciting possibilities
[1044] when that's available.
[1046] So this figure from Gupal and colleagues
[1049] might look quite similar to the figure I
[1051] showed you earlier for RSA and it's uh
[1054] indeed uh very much the same in spirit.
[1057] So here rather than those fourleeled
[1060] stimuli we have three different labeled
[1062] movie frames. we still have our three
[1065] voxels and we're looking at the relative
[1067] activation of each voxil for the three
[1069] movie frames. Um but importantly unlike
[1072] an RSA where what we'd be doing is
[1074] calculating or most of the metrics I
[1076] discussed excuse me where what we doing
[1078] is calculating the um distance between
[1080] these different stimuli what we're going
[1082] to do now is actually derive these uh
[1086] transformations and then uh use those
[1089] transformations to move our data into
[1092] some new common representational space
[1094] or common activation space. So this
[1097] particular um method that was proposed
[1099] by gapuli gaupali excuse me and
[1102] colleagues is known as hyper alignment
[1104] and is based on procrusties which is
[1106] that same method that I alluded to
[1108] earlier. Um but there are many many uh
[1111] methods that work exactly like this in a
[1113] highdimensional full voxal full sensor
[1117] space to bring everything into alignment
[1119] into one dimension where they can be
[1121] directly compared. [snorts] Of course,
[1124] as I mentioned, it doesn't uh
[1126] necessarily have to be done in high
[1128] dimensional space. So, this is another
[1129] method um a schematic of another method
[1132] that was originally proposed by Chen and
[1135] colleagues and is really nicely
[1136] summarized here uh by Cohen and
[1138] colleagues. So, this is called the
[1140] shared response model. And what's
[1142] happening here is just as before, you
[1145] have some shared stimulus in this case.
[1147] So, this is labeled data where you know
[1149] that everyone was watching the same
[1151] movie. for example, let's say if you're
[1153] working with human data. Um, and now
[1156] what you're going to do is rather than
[1157] just looking directly at the voxels,
[1159] you're going to find some joint
[1161] lowdimensional factorization where you
[1164] have uh shared time components across
[1168] individuals and then every um individual
[1172] gets a spatial uh component as well. So
[1176] you have this lowdimensional K which is
[1179] uh less than the overall um uh
[1183] dimensionality of your data and you're
[1186] going to be able to have the spatial
[1187] component for individuals and the time
[1189] component shared. So you're learning
[1191] some importantly what's really happening
[1193] is you're learning some lowdimensional
[1195] factorization of your data that's stable
[1197] and shared across individuals. Right? So
[1199] you don't just have to think about it in
[1201] the highdimensional space if you want to
[1203] look for latent factors.
[1206] So, okay, this was two slides and I
[1209] threw uh multiple alignment methods at
[1211] you. So, as you can imagine, there are
[1213] lots and lots of alignment methods that
[1215] are out there that fit in these broad
[1217] categories of high and low dimensional
[1219] labeled and unlabeled data. And whoa,
[1223] got clicked on that. Um,
[1226] for an alignment method, it's not
[1230] necessarily clear which method should be
[1232] chosen right away, right? So much as for
[1235] metrics, which alignment method to
[1237] choose is data dependent and in fact at
[1239] this point it does remain largely guided
[1241] by field norms. So um to systematically
[1246] explore the impact of alignment methods
[1248] is something that is still really
[1250] important within neuroi I think. And um
[1253] as part of this, Tom Baz and myself um
[1256] with our collaborators went and tried to
[1260] do a systematic benchmark of alignment
[1262] methods in fMRI data. And just to
[1265] provide a sense of how you can evaluate
[1269] fMRI methods, I wanted to highlight just
[1271] a few key results from this. Um and in
[1274] particular I wanted to highlight this
[1275] framework we used where we evaluated the
[1278] success of alignment using inter subject
[1280] decoding accuracy on unrelated
[1282] downstream tasks. Right? So what we did
[1285] here was we looked um across the field
[1289] in uh with functional neuro imaging and
[1292] we found data sets that had a lot of
[1294] data for each participant that and some
[1298] of that we could use for alignment and
[1300] some of that we could use for a separate
[1302] unrelated decoding task. So we had a
[1304] range of different kinds of alignment
[1306] data covering movie watching, audio
[1308] movie listening, task contrast maps,
[1310] visual images and a range of decoding
[1313] categories. Right? So visual working
[1315] memory, music, images, sounds, language.
[1318] This is really a broad span of what we'd
[1320] usually look at in cognitive
[1321] neuroscience.
[1323] Um and so when we used alignment on
[1326] these data,
[1327] we actually found that um we could
[1331] recover a significant amount. So first
[1334] let me just explain this figure to you
[1335] and then I will uh walk you through what
[1338] I mean by a significant amount. So here
[1341] what we're seeing is this is the inter
[1343] subject
[1345] decoding accuracy and because uh well my
[1348] pointer is the same color as a dot so
[1350] I'll move that away. Because we did
[1352] inter subject decoding each dot is a
[1354] different cross validation fold. So this
[1355] is a different subject um and the
[1358] subjects are colored according to the
[1360] particular data set that they come from.
[1362] And what we're comparing against this 0%
[1364] line is if we didn't do any kind of
[1366] functional alignment. If we just
[1368] compared using anatomical alignment,
[1370] assuming that if we moved everyone to
[1372] the same geo uh uh anatomical space
[1375] based on their uh brain uh landmarks
[1379] that we would be working in the same
[1381] functional space. So we can see that
[1383] these two methods, one of which I just
[1385] showed you a minute ago, the shared
[1387] response model, this lowdimensional
[1390] labeled data and peacewise optimal
[1392] transport, which is a highdimensional
[1395] labeled data method. Um so we see that
[1398] these are on average across participants
[1401] uh about 5% improvement over anatomical
[1404] alignment. Um and if we look if we just
[1408] did uh a within subject decoding minus
[1412] inter subject decoding so trying to see
[1414] how much we lose when we move from the
[1416] individual to the group we'd see that we
[1419] lose uh about 8% 8.5%
[1422] um of decoding accuracy. So this gain of
[1426] these uh proformia methods is a little
[1428] over half of what we normally lose to
[1430] group variability. So this is pretty
[1432] impressive in terms of gains. Um and
[1435] also importantly what we see if we look
[1439] at the uh signal itself is that we see
[1442] that we are not wildly distorting the
[1444] signal. We're not losing signal. Um
[1447] we're actually able to preserve the
[1449] signal in a really structured way. So
[1451] for example, if you look at peacewise
[1452] optimal transport compared to the target
[1456] individual we're aligning to the group
[1460] aligned using peacewise optimal
[1461] transport is still picking up the peaks
[1463] of the target individual's contrast. So
[1465] we're really preserving signal
[1467] specificity when we do this alignment.
[1470] So that was one example of aligning in
[1474] um out of sample. So we derived our
[1476] alignments on the movie. We applied them
[1478] and held out decoding data depending on
[1481] the particular kind of data you work
[1483] with that may not always be possible. So
[1487] for example a really big application of
[1490] alignment actually is brain computer
[1492] interfaces. And here it you need to find
[1495] a way to on sample or in sample align um
[1498] because you don't necessarily have
[1500] offline data that you can work with. So
[1503] in this case what we're trying to do is
[1506] we're trying to calculate our alignment
[1507] online and assess the performance as we
[1509] go via decoder accuracy of participant
[1512] movement or you know handwriting or
[1515] whatever else our uh brain computer
[1517] interfaces is helping our participant to
[1519] do. So as really nicely illustrated in
[1523] this figured by Dagia and colleagues
[1526] what we're trying to do is to estimate a
[1528] lowdimensional manifold. So again this
[1530] uh latent factor alignment
[1532] we're going to uh align it and then
[1536] we're going to take those
[1537] transformations and apply it back out to
[1539] our highdimensional s uh sensor or
[1542] implant data.
[1544] And what's really cool about this is
[1547] that um you know talking to people who
[1549] do a lot of BCI work here at Stanford,
[1552] they'll talk about how every session
[1553] where they have a participant, they have
[1555] to have a recalibration session at the
[1558] start. Um and this is really costly.
[1560] This takes a lot of time. this, you
[1562] know, hampers participant engagement
[1564] with the brain computer interface. So,
[1566] alignment provides a really nice way to
[1569] avoid constant decoder retraining for
[1572] each experimental session because
[1573] otherwise, as I alluded to in the
[1575] beginning, you can just see that you're
[1577] losing accuracy over time.
[1581] All right. Um, perfect. Okay. So, just
[1585] looking at the chat, the slide deck will
[1588] be shared. Yes, absolutely. That's a
[1590] great question. Um so I will make sure
[1592] that gets to you
[1595] and if there are any other questions
[1596] please don't hesitate to add them.
[1600] Okay so stepping back we've talked about
[1604] um metrics as one means to look at
[1606] dissimilarity. We've talked about
[1608] alignment as a means to actually move
[1611] data into the same space and in
[1612] particular kind of the uh framework for
[1615] alignment where you have high and low
[1616] dimensional data, labeled and unlabeled
[1619] data
[1620] um and how that can be used in a variety
[1622] of settings both uh training and then
[1625] applying on unrelated data and in the
[1628] case of um some settings where it's
[1630] required actually working online
[1632] alignments within uh the same data.
[1636] So, this seems really promising. It
[1638] seems like a really broad direction. Um,
[1641] but there are some, I think, uh, major
[1644] stumbling blocks that hit a lot of folks
[1645] when they're considering working with
[1646] alignment that I wanted to point out,
[1649] um, before we think about how we could
[1651] actually get started with it in our own
[1652] work. So, when you're thinking about
[1656] working with alignment, there are a few
[1658] um, highlevel concerns I think that
[1661] arise. Um, and I'd, you know, I could
[1664] think we could frame these as decision
[1666] points really. The first is choosing the
[1668] right feature space in which to do the
[1670] alignment. So, it's all well and good to
[1672] say that we'll align some data, but you
[1674] know, what does that data look like? If
[1676] we can choose going in what kind of data
[1679] to collect, how do we choose what kind
[1681] of data to collect? The next is handling
[1683] unbalanced alignments. So most of the
[1686] methods I've discussed so far really
[1689] assume that there's a onetoone
[1691] correspondence that you're going to be
[1693] able to find in your alignment. And
[1695] that's often not the case. We don't
[1697] always expect information to be
[1699] perfectly preserved between different
[1700] brains or between different um neural
[1703] network instances. For example, if the
[1705] layers are different sizes.
[1707] And then finally um we may need to think
[1710] about uh considering template based
[1713] alignments. So rather than aligning to
[1716] uh data that we have that we know exists
[1719] um if we have many many sessions many
[1721] many instances or participants we may
[1724] need to think about how can we align not
[1727] onetoone but um to some shared or common
[1730] uh template.
[1732] So, first choosing the right feature
[1734] space. Um, and I think this uh, you
[1738] know, may not be as obvious when you
[1740] first start, but I think it it's really
[1742] quite critical is that when applying
[1744] lowdimensional alignments, the selected
[1747] features subspace will significantly
[1749] impact the results. So, this is a
[1751] supplemental figure from that um, study
[1753] I just showed you where we used
[1756] peacewise SRM and optimal transport uh,
[1758] uh, to look at interubject decoding
[1760] accuracy. But really what I want to
[1763] hammer home here is this is a grid
[1765] search for the hyperparameters for
[1767] peacewise SRM. So you can see K which is
[1770] the hyperparameter for the
[1771] dimensionality. You can see this other
[1773] parameter where we look at the number of
[1775] parcels and you can see that the range
[1777] of values is really quite wide. Right?
[1780] So what we're seeing is that the
[1782] specific hyperparameters that we're
[1784] using to select our feature subspace are
[1786] going to significantly impact our
[1788] results. And it is something that really
[1790] needs to be carefully considered
[1792] particularly um in this case for
[1794] subspaces when you're working with
[1795] lowdimensional alignments. So for um
[1798] example if you're thinking in a BCI
[1800] application what are you going to use to
[1802] learn your mammoth fold? What particular
[1804] algorithm are are you going to use
[1806] there? Um that can have a really high
[1808] impact uh downstream.
[1811] [sighs and gasps] Another point is that
[1814] um you know if you're going about and
[1815] you're collecting data so if you're
[1817] designing a training set or you're
[1818] designing a stimulus set for
[1820] participants um if you're trying to do
[1823] an outof sample alignment in particular
[1826] uh you know it may not be obvious how
[1828] best to match the characteristics of
[1831] your uh training data where you learn
[1834] the alignment with where you're going to
[1835] apply it. And this is uh really complex.
[1838] I would say this is something we're
[1840] still trying to understand, but we do
[1843] have some broad rules of thumb. So, for
[1845] example, if you're going to
[1848] apply to something that's a language
[1850] task, what you learn your alignment in
[1852] should probably include language in some
[1855] form, right? It shouldn't be visual only
[1857] clips. Um, so if you can carry
[1859] information over, it will make the um
[1863] the distribution alignment a bit easier
[1866] later so long as you're covering uh
[1868] similar kinds of information both where
[1870] you're learning and where you're
[1871] applying your alignment.
[1875] Another important point um is unbalanced
[1878] alignments. So this is a really nice
[1881] figure from TW and colleagues from uh
[1883] this year at Nurups. So in some cases,
[1887] in fact, in many cases, depending on
[1888] your particular data modality and
[1890] question, um your source and target data
[1893] may not have a onetoone matching. So in
[1896] this case, for example, we have two
[1897] participants. We're looking at uh a
[1900] contrast map for the same contrast, like
[1902] an auditory language contrast. Um, and
[1904] what you can see is that for each
[1906] participant, uh, it's generally within
[1909] the same set of brain regions, but we
[1912] don't see that it covers, uh, the same
[1914] spatial extent, right? And so if we were
[1917] to enforce that all information from
[1920] subject seven moves to subject 9, um, we
[1923] might or vice versa, we might see some
[1927] kind of odd or undesirable effects. And
[1929] instead what we can do is actually allow
[1933] for um an unbalanced alignment. Allow
[1936] for not all of our information to be
[1938] matched. Um and this is really useful
[1941] quite broadly in this example for
[1943] example where different individuals have
[1945] differently sized functional areas in
[1947] artificial neural networks where you
[1948] have layers which um maybe you have the
[1950] same number of layers but within a layer
[1952] two instances two architectures have
[1954] very different numbers of hidden units.
[1956] Um allowing things to decay when you uh
[1961] move them during the alignment can
[1964] really help to make sure that
[1965] information is actually preserved. Um,
[1968] and this means that unmatched
[1971] information is going to be discarded
[1973] rather than complicating your alignment
[1975] and making it harder to understand
[1977] what's happened after the fact. So, this
[1980] is a really nice example from Sing and
[1982] Joggy at Anurup's paper a couple years
[1984] ago. What they have here is they have a
[1986] specialist network. Um, so this
[1989] specialist network had access to a
[1992] different data class than the generalist
[1993] network. And they see that if they uh
[1998] initialize them differently um much as
[2001] we've seen generally uh where you have
[2004] different initializations
[2006] um if they just average them they see
[2009] that with vanilla averaging this blue
[2011] line they see that the performance
[2014] really falls off. So this is just
[2016] averaging all of the u model weights
[2019] between the two different models.
[2021] Whereas if they use this kind of
[2023] alignment, this optimal transport uh
[2025] averaging that they argue for, they see
[2027] that they can really conserve
[2030] um the performance. And when they
[2034] initialize them the same way, they see
[2035] the effect isn't as dramatic, but it's
[2037] still present. So this optimal transport
[2040] averaging rather than just kind of a
[2042] naive averaging, performing some kind of
[2044] alignment first and then averaging um
[2047] allows you to really recover performance
[2050] between models um that otherwise because
[2053] you know of individual differences would
[2056] uh be very difficult to compare
[2058] directly.
[2062] Finally, the last kind of consideration
[2065] that I wanted to make here um is about
[2067] functional templates for alignment. So,
[2069] in all of the cases that we've
[2071] considered thus far, we assume that
[2073] we're uh performing alignment to a real
[2075] known target. So, this would be for
[2077] example a previous experimental session
[2080] or an existing uh model or um
[2084] participant. But in many cases, it would
[2086] be preferable to align to a functional
[2088] template. Um, so for those of us in
[2090] neuroscience, this might be analogous to
[2092] the idea of anatomical templates um,
[2095] such as those provided uh, in Montreal
[2097] at the M&I.
[2100] Now this is really appealing um, and
[2103] really quite difficult. So calculating
[2106] such a template is an active research
[2107] area um, and initial methods have come
[2111] out proposing various solutions. So for
[2113] example, Axi and colleagues have
[2116] proposed developing templates using
[2117] generalized procies. Um again
[2120] referencing that procrees meth method I
[2122] mentioned earlier to an inferred average
[2125] or um more recently that uh uh figure
[2128] from TW and colleagues is from a paper
[2130] where they also talk about using
[2131] Werstein berry centers um to develop an
[2134] average. There's no good answer there.
[2138] Excuse me. there's no good answer there
[2141] as to what the correct uh template would
[2144] be or should be. Um so for now I would
[2146] say this is definitely something that
[2148] folks are working on and and I'm sure um
[2151] more help would certainly be useful. Um
[2154] but this is uh a very active area.
[2158] [sighs and gasps]
[2159] Okay, perfect.
[2162] So looking at the time, let's say that
[2166] you would like to get started with
[2168] alignment. How could you go about
[2169] getting started? Um, first, a lot of
[2173] people have very kindly shared code for
[2176] different ways to do this using
[2177] different kinds of data types, right?
[2179] So, um, several of these are designed
[2182] primarily for fMRI data, in particular,
[2185] brainiaak, e furalign, uh, and pyva.
[2190] But neuroline here from Evadier and
[2193] colleagues um is actually designed for
[2196] uh data from systems neuroscience. So
[2198] like calcium imaging data, spike sort of
[2200] data. Um OT fusion from singing
[2204] colleagues is designed uh for model
[2207] fusion with neural networks.
[2209] Um and this allows you to again align uh
[2213] multiple models and then perform uh an
[2216] average of the parameters that conserves
[2218] information rather than discarding um or
[2221] losing information between the
[2223] individual differences of the different
[2224] models.
[2227] So code is great um but it's also useful
[2231] to have a general framework in mind for
[2233] how to get started. So if we have these
[2236] resources, if we have the data, and
[2237] we're, you know, convinced that
[2239] alignment is something we should be
[2240] thinking about across all of these
[2242] different systems, how can we go about
[2244] getting started? Um, I would just
[2246] provide some really general
[2248] recommendations. One of which I think is
[2250] critical, which is consider how you will
[2252] evaluate the success of alignment on
[2254] your data. So for example in the paper I
[2257] talked about from um uh Tom Baz and
[2261] myself and colleagues what we found was
[2264] that um it's nonobvious in many cases
[2268] how to actually evaluate alignment
[2270] success there. We used intercept
[2272] decoding. Um there are a variety of
[2274] metrics that you could use to evaluate
[2277] success. But I think in many cases
[2279] people will assume that okay if I
[2281] calculate and then apply an alignment
[2283] then I've improved similarity and I can
[2285] now perform whatever analysis I want.
[2288] And it's really hard to know if that's
[2290] true right I think we're still in very
[2292] early days of learning what kinds of
[2294] alignment are best uh for particular
[2297] data types and for particular questions.
[2300] So for now I would really encourage you
[2302] to consider evaluating the framework by
[2304] which you will evaluate the success of
[2306] alignment before you start um applying
[2310] it to your data.
[2312] I would also say just look at the
[2313] literature in your field. So alignment
[2316] is definitely gaining steam right now. I
[2319] feel like I'm seeing more and more all
[2320] the time um different uh groups and
[2323] papers that are using different kinds of
[2325] alignment methods in their own data. And
[2328] so I would say take a look in your field
[2330] and see what alignment methods have
[2332] already been applied. So if you're
[2333] working in brain computer interfaces,
[2335] there are some emerging best practices
[2337] there. If you're working in fMRI, if
[2339] you're working in calcium imaging, um
[2341] all of this can really help you to get a
[2343] sense of what alignment methods are
[2345] going to be useful for your data type.
[2347] Um but of course you'll still need to
[2349] evaluate was the application successful
[2352] for your particular question.
[2355] And then finally, um I think this is
[2357] something that's emerged more recently
[2359] and is incredibly important um is
[2362] evaluating if your application is likely
[2363] to have unbalanced information between
[2365] source and target data sets. So, if
[2368] you're working um with information where
[2372] you do think that you're not going to
[2374] have a one-toone correspondence or if
[2376] you think there's even a chance that you
[2377] might not have a one-toone
[2378] correspondence, choosing alignment
[2380] methods that can handle this kind of
[2382] unbalancing
[2383] um is really important and that's
[2385] something you can test in your data. You
[2387] can say, you know, once you have this
[2389] framework by which you're going to
[2390] evaluate success, you can say, okay, if
[2392] I allow for unbalancing versus not, how
[2395] does that change the success of my
[2397] alignment? What do I differentially
[2399] learn?
[2402] All right. So with that I want to thank
[2405] um my supervisors Russ Puldrich and
[2407] Scott Linderman the Wooai Neuro in
[2410] neuroscience institute um the labs and
[2413] uh obviously Unique and Miguel who've
[2416] been so instrumental in all of this work
[2418] um that I presented here and I want to
[2421] leave you with a few take-home ideas
[2424] about um alignment for our field in
[2426] neuroai and some exciting I think future
[2429] directions. So thank you
