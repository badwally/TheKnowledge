---
schema_version: 1
id: yt-0W-cRw-EBAc
type: youtube
title: CSAIL Forum, Philip Isola, "The Platonic Representation Hypothesis"
url: https://www.youtube.com/watch?v=0W-cRw-EBAc
authors:
- Symposia at CSAIL
ingested_at: '2026-06-01T19:24:32Z'
content_hash: sha256:e136410535548620eee5729528f32efb6bec2c7ee736a29458665a1ca7466f1a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Symposia at CSAIL
  channel_url: https://www.youtube.com/@symposiaCSAIL
  duration_seconds: 3195
  caption_track: fetched
  snippet_count: 1439
filter:
  score: 0.8
---
[1] Hello everyone. Welcome to those of you
[4] who are in person with us today. Welcome
[6] also to everyone who is joining us
[9] online. My name is Daniela Arus. I'm the
[12] director of the computer science and
[14] artificial intelligence laboratory at
[16] MIT and I would like to welcome you to
[19] the inaugural SEAL forum. Uh today we
[22] launch a new platform for rigorous and
[26] visionary intellectual exchanges at the
[30] frontiers of computer science and
[31] artificial
[33] intelligence. And our inaugural speaker
[36] is professor Philip Isola whose
[38] groundbreaking work uh is at the
[41] intersection of computer science,
[43] computer vision, machine learning and
[46] cognitive science. And um this work has
[50] consistently challenged conventional
[53] thinking and so I am delighted to pass
[57] the microphone uh to Phillip in just a
[60] second. Okay. Yeah. Thank you for the
[62] introduction. Um and happy to talk about
[67] uh this work that we've done in my group
[69] recently that we call the platonic
[71] representation hypothesis.
[73] And this is work with uh Minyong Hut,
[76] Brian Chung, and Tong Jay Wong. They
[78] were the initial authors that we on the
[80] paper we put out last summer. And then
[82] Yulan and Ivy Jiao who are new students
[84] in my my group have been following up
[85] and doing more work on this. So um I've
[88] given this talk a few times um but
[90] there'll be some new stuff uh in it as
[92] well. I'm going to update it with the
[93] last six months of progress as well.
[95] Okay.
[99] So showing the intro animation that um I
[103] forgot to press play on that. Okay.
[105] Different ways of looking at the world.
[107] Okay. So I'll start with this story
[108] which
[109] is one of the papers I really like from
[112] the last decade. Um this is work from uh
[115] Antonioa and Odoliva uh and uh and
[118] others. And what they found is that
[121] object detectors emerge in deep scene uh
[124] convolutional neural networks. So uh in
[127] this paper from 2015 they took a neural
[129] network and they tried to probe what
[131] internally is it representing about the
[133] world. So they trained the network to
[136] predict the scene label like this is a
[137] dining room. And if you then go into the
[140] network and you probe the neurons you
[142] stick like electrodes virtual electrodes
[143] in there and you measure what those
[145] neurons respond to. They found that
[147] there were neurons that would be
[149] activated selectively for certain object
[151] categories. So there was a neuron that
[154] acted like a dog face detector and
[156] there's another neuron that acts like a
[158] um robin head detector. That's neuron B
[161] here. So this is really cool because it
[164] kind of showed that these systems are
[165] not just uninterpretable black boxes
[167] that you can actually dig into them and
[169] they have internal structure that kind
[170] of make sense. In order to understand
[172] what is going on in an image in a scene,
[174] you should first detect the objects and
[176] then you'll know that it might be like a
[177] park scene outdoors. Okay. So uh we did
[181] this study a few years ago uh where we
[184] tried to train a network to colorize
[186] photos just predict the colors in a
[187] black and white image and we ran the
[190] same uh experiment as they did in the
[192] previous work where we looked internally
[193] and asked what are the units what are
[195] the neurons uh selective to and the
[198] really interesting thing is that we find
[201] a similar pattern. So, you might think
[203] that a network trained to just colorize
[206] photos, like predict the colors in a
[207] black and white image, would have a very
[209] different internal representation than a
[211] network that's trained to classify is it
[213] a kitchen or is it a bathroom or is it a
[215] living room? But it turns out no,
[217] they're actually quite similar. So,
[218] there is a neuron inside a colorization
[220] network that detects if there's a dog in
[223] the image and there's another neuron
[224] that detects if there's a flower in the
[226] image. In order to solve the problem of
[228] just predicting missing colors, you get
[229] these kind of semantic units. And this
[231] is a story you might have heard before.
[233] Uh it's it's appeared all over the
[235] place. Uh for very um diverse kinds of
[238] ways of training your neural networks,
[240] you end up with internal structures that
[242] uh always kind of look somewhat similar.
[244] They they have base detectors. They have
[246] edge detectors on the early layers. They
[248] have gores and then they go up and they
[249] create more complicated structures. Um
[251] so there seems to be some kind of
[253] similarity in the internal
[254] representations in computer vision
[256] systems across many different models and
[258] ways of training them.
[260] Okay, so that's led us uh to this point
[262] where we really wanted to uh put a
[265] hypothesis around that idea and
[267] investigate to what degree is it um
[270] going to be true. So the hypothesis
[273] we'll investigate in this talk is uh the
[276] hypothesis that different neural
[277] networks trained on different data with
[279] different architectures, different
[280] optimization somehow converge to similar
[283] or maybe even the same way of
[284] representing the world. To what degree
[286] is that true?
[289] Okay, so there's a lot of reasons why
[293] that might be happening and you might
[294] already have some ideas in your mind
[296] like okay well of course these things
[298] learn similar structures because they're
[299] all trained on the same data sets right
[302] we have these standard data sets imageet
[304] and and so forth and now we train all
[305] our big models on the internet so maybe
[308] it's just the data it's all about the
[309] data convergence is driven by training
[312] on similar data sets okay also we all
[315] use the same architecture right we're
[316] all using transformers now could be the
[319] architecture. Maybe it's the
[320] optimization. We're all using Atom and
[323] SGD. U maybe it's about us like I'm
[325] talking to you. I'm telling you how I
[326] did it. Maybe it's just so technical
[328] like we all converge because we're going
[330] to the same conferences. We want to
[332] follow the same trends. So I think these
[334] are all part of it, but I want to argue
[335] that it's something a bit deeper. Uh
[337] that actually when we train our models
[339] on different data sets systematically,
[341] they also look like they have an uh
[343] similar internal structure. uh when we
[345] change the architecture if we don't use
[346] a transformer it also ends up converging
[349] to something kind of similar. So I want
[351] to argue that uh it's all about the
[352] world. We're modeling the world and the
[354] world is ultimately the thing that
[355] unifies all of these
[357] representations. Okay. So I'll go into a
[359] lot more detail about exactly what I
[361] mean. I'll talk about these five things.
[363] So first evidence of convergence. Uh
[366] second some ideas for what is driving
[368] convergence. Uh then a uh a thought on
[372] what we might be converging to. what is
[374] this ultimate representation that we
[375] might end up with in theory? I'll talk
[377] about some counterarguments and then
[379] some implications and applications of
[381] these
[382] ideas. So let's start with evidence of
[386] convergence. Okay. And at the end I'll
[388] uh try to leave time for uh questions so
[390] we can have some discussion at the end.
[393] Okay. So I'm going to analyze
[396] representations in neural nets uh using
[398] kernels. So what I mean by that is we
[400] will restrict our attention to
[402] representations that are vector
[404] embeddings. So neural nets that map from
[406] data to vector in Rn. Okay, this isn't
[410] everything, but this is a very broad
[411] class of
[413] systems. And we're going to characterize
[415] a representation by how it measures
[417] distance. Okay, so we do that in terms
[419] of this function we call the kernel.
[421] It's a standard object in machine
[422] learning. uh it's the inner product
[425] between the embedding for data point I
[428] and data point
[429] J. Okay, so this kernel is like the
[433] similarity matrix in the feature space
[435] of a neural
[437] network. Okay, so here's what the kernel
[440] might look like for a computer vision
[442] neural network that takes images and
[443] outputs embeddings. And what this kernel
[446] is saying is it's saying how similar is
[448] my neural network's representation of
[451] apple to orange and that will be this
[452] cell here and it will say that's quite
[454] similar uh because maybe this network
[456] has been trained to understand fruits
[458] and it knows that those are similar
[460] objects. Uh and orange and elephant will
[463] be considered dissimilar. So this matrix
[465] is telling me how does the neural
[466] network measure distance and it's one of
[468] the kind of fundamental structures that
[470] people use to understand internal
[471] representations in neural networks as
[473] well as other areas of machine learning.
[475] If we can un if we know the kernel then
[477] we know a lot about the um about the
[479] representation and what it can do.
[483] Okay. So what we're going to be looking
[485] at is the similarity between the kernels
[488] uh given by two different models. So
[490] here's one example of two different
[492] vision models. One is called clip,
[493] another's called dyno. These are
[495] standard current computer vision models.
[497] And we're going to ask to what degree
[499] are their kernels the way they measure
[500] distance uh similar to each other. So
[502] it's a similarity measure between
[504] similarity structures inside the neural
[506] network. Uh so in this case Dino and
[508] clip have some minor differences in this
[510] cartoon but they're roughly similar
[512] kernels. They both think apples and
[514] oranges are quite
[516] alike.
[517] Okay. So this is the main metric that
[520] we'll be using to analyze uh to what
[522] degree are different networks finding
[524] similar representations. And the first
[526] experiment I want to run is looking at
[528] different vision systems and asking as
[531] vision systems get better and better at
[533] the task of vision, do they end up
[535] representing the world in similar or
[537] different ways? So hypothesis one will
[540] be uh no no there's many different
[542] equally good ways of representing the
[544] visual world and there's no reason why
[546] you know current state-of-the-art
[548] systems will all choose the same one.
[550] There could be equally valid uh and
[552] diverse approaches. And hypothesis too
[554] is um actually no it turns out that all
[557] strong vision representations are
[559] somehow alike. They all measure distance
[560] in similar ways. Uh and this this has
[563] been described as kind of an anaria
[565] anaina scenario uh by bansel at all um
[568] in the past. So all strong
[570] representations are
[572] alike. Okay. So we ran this experiment.
[575] We downloaded 78 different vision
[577] models. Uh these are contrastive models.
[580] They're recurrent models. They're
[581] resonant models. They're convolutional
[583] models. They're a bunch of different
[584] models and they have different
[586] architectures, objectives, and they're
[588] trained on different types of data. And
[591] we grouped them by their performance on
[594] this VTAB benchmark, which is meant to
[596] be kind of an assessment of how good is
[597] your visual representation. You assess
[599] how good is your representation in these
[601] models by doing transfer learning onto a
[603] suite of downstream
[605] tasks. Okay, so here here's the uh
[608] result that we found. So on the y-axis
[612] is how similar are the representations
[614] to each other within a bucket of
[616] performance and the buckets of
[617] performance are on the x- axis. So what
[620] you can see is that models that perform
[623] very well. So they solve between
[626] um they solve many different vtab tasks
[629] uh they have very similar
[631] representations. So all models that
[633] solve uh these tasks well have similar
[635] representations. models that don't solve
[637] very many of the tasks uh are much more
[639] diverse and there's many ways you can be
[640] wrong but only one way you can be right
[642] in in this particular measure of
[643] performance called VAB.
[646] uh we can look at that in a slightly
[648] different way by just uh making this
[650] kind of dimensionality reduction this um
[652] visualization of here are all our
[654] different models that we tested and you
[655] can see they have different symbols for
[657] different types of architecture and
[658] objective and the color indicates their
[661] performance on the VAB transfer learning
[663] task and blue means high performance and
[665] you can see that uh the main uh feature
[668] that uh organizes uh how these models
[672] group together uh which models are cons
[674] are alike in their representations is
[676] their performance. It's not the
[677] architecture, it's not the objective, uh
[680] it's the performance. So the
[681] wellperforming models all have similar
[682] internal representations. Okay. So the
[685] the the conclusion of this experiment is
[687] that the anacrrenina situation is
[689] seeming to hold here. Uh strong models
[692] are alike, weak models are weak in their
[693] own
[695] way.
[697] Okay. So I think that that was that's an
[700] interesting result. Uh but maybe not too
[704] surprising. You know, as we get better
[707] and better vision systems, they're going
[709] to perform well at the same task. So to
[710] perform well at the same task, of
[712] course, they've got to somehow, you
[714] know, find similar features and have
[715] similar representations. Uh we're going
[717] to now ask something that's a little bit
[720] less clear, which is do you also get
[723] similarity between different modalities?
[725] So representations of language, are they
[728] becoming more similar or less similar to
[729] representations of vision?
[732] Okay, again we'll have a few hypotheses.
[733] So hypothesis one is that no, I mean as
[736] you get a better and better language
[737] model, it becomes a language expert. It
[739] just gets really good at syntax and
[740] grammar, but why would it get better at
[742] recognizing cats and dogs? That doesn't
[744] make any sense. Okay, they might even
[746] get worse because they're getting
[747] specialized specialized to to language.
[750] Okay, hypothesis two is well somehow
[752] language and vision share common
[754] properties and so actually better
[755] language models are better vision
[757] models. And there might be in like a
[759] really strong hypothesis like the very
[761] best language model is actually the same
[762] as the very best vision model. There's
[764] some like actual unification um at the
[767] end. Okay. So we're going to run um the
[771] same experiment but now we're going to
[772] look at crossmodal similarity. So we're
[774] going to take the kernel for a vision
[776] system and compare it to the kernel for
[778] a language system. But now we're cross
[780] modality. So, in order to ask if the
[782] language system is representing Apple
[784] and Orange in the same way as the vision
[786] system is, we're going to run the
[788] language system on the captions uh that
[790] correspond to the uh images that we ran
[792] the vision system on. So, we're asking
[794] is the word apple similar to the word
[797] orange in the same way as the image
[798] apple is similar to the the image
[800] orange.
[803] Okay, just to uh draw that one more
[805] time. What we're asking is if they're
[807] structured like this, does the vision
[809] model embed apple and orange near each
[812] other and far from elephant uh in the
[815] same way as the language model embeds
[818] the word apple and the word orange near
[819] each other and far from elephant. So,
[820] we're looking if the distance structure
[822] is the same between these two
[823] modalities. There could be a rotation or
[825] scale transformation. So, we're using a
[827] metric that's invariant to those types
[829] of changes. We're just looking at if it
[830] if these two representations measure
[832] distance in the same
[833] way. Similarity of embedding of apple uh
[837] and orange is roughly the same as
[839] similarity of em of embedding image of
[841] apple and image of of
[844] orange.
[845] Okay. So we measured this uh not over
[848] emojis uh we actually downloaded real
[850] photos and so we used the Wikipedia
[852] image text data set. So we have a lot of
[854] photos along with their caption and
[856] we're evaluating uh do does the vision
[859] system represent these photos of eused
[861] uh according to the same distance
[863] function as the language model
[864] represents these captions that describe
[866] those photos of
[869] Euseite. Okay, so here is the the main
[873] result. The main result is that we're
[876] going to
[877] plot alignment to vision. We're we're be
[880] measuring the alignment between
[882] different language models and a computer
[884] vision model. Here we're picking one
[885] computer vision model which is the
[886] Dinov2 model. And we're going to uh
[889] measure the alignment to the Dino V2
[890] model as a function of the language
[892] models performance at next word
[895] prediction. So as language models get
[897] better and better along the x-axis at
[900] predicting next word and sentences at
[902] their basic task, do they end up
[904] becoming more and more alike in their
[906] kernels to vision models? Okay. And so
[909] here's the result. So yes, the answer is
[912] uh uh in within this regime they do. Uh
[915] so this is a small uh vision model and
[919] as you look at different language models
[920] ranging from 1 billion parameter
[922] language models to 65 billion parameter
[924] language models, the bigger more
[926] performant language models end up having
[928] higher kernel alignment with the vision
[930] models. So better language models
[932] represent the world in ways that are
[933] more
[934] visual. And the trend goes in the other
[936] way too. So better vision models also
[940] become more aligned to language models.
[943] So Dino Giant, it's a really big
[945] computer vision model that's very good
[946] at computer vision tasks, is more
[948] similar in how it represents the world
[950] to llama, a language model, than Dino
[953] small is. So it goes both ways. Big
[957] vision models represent the world in a
[958] similar way as language models do. And
[960] big language models represent the world
[962] in a similar way as vision models do. It
[964] looks like there really is some
[965] convergence going on.
[969] Okay. So, is it going to continue? Uh,
[971] maybe. I'll I'll note that the metric
[974] that we're using, I'm not actually
[975] giving you all the details on that, but
[976] we're not at saturation. We're at a
[978] point about.16 on a metric that goes
[981] from 0 to one. Uh, so you could get
[984] better. Uh, maybe it's going to saturate
[986] or maybe this trend will fall off. It's
[987] just like a spurious correlation and it
[989] won't it won't uh hold for next year.
[991] And the last time I gave this talk, I I
[993] I would stop at that point and say
[995] speculation where this will go next. But
[997] fortunately, just two weeks ago, you
[999] know, some people ran these same
[1000] experiments, but they went up to 7
[1003] billion uh scale vision model. So we we
[1006] went up to 1 billion scale vision model
[1008] Dino V2 and we had a alignment of.16 and
[1012] people at meta went up to 7 billion a
[1015] few weeks ago and measured alignment as
[1017] a function of size of vision model and
[1019] the trend actually
[1021] continues. So they they had some
[1024] interesting nuances in this paper. So
[1025] I'll encourage you to look into it if
[1027] you're interested. Uh basically they
[1029] found that the trend continues as you
[1030] add more data but not necessarily more
[1032] model scale. But big picture uh this
[1036] this trend is continuing. It might be
[1038] kind of flattening out a little bit. So
[1040] who knows if it will go to uh go to one
[1042] and be perfectly unified. But uh we are
[1044] still seeing more alignment increasing
[1046] between vision and language models up to
[1048] the year 2025. Philip, do you understand
[1050] why from 1B to um 5B seems to be flat?
[1056] Yeah. Um so I need to look into the
[1058] details. The question is do I understand
[1060] why this part is flat here? uh 1B to 5B.
[1063] Uh I think the point that they're making
[1065] is that just increasing model scale
[1067] without commensurately increasing data
[1069] doesn't seem to have an effect on it on
[1071] its own. Uh but if you also then
[1073] increase data then you see the effect.
[1075] Um so yeah just adding more parameters
[1077] alone doesn't doesn't have the effect.
[1079] Uh but again this is not my work so I'll
[1082] need to look into those
[1083] details. Okay.
[1086] Um, so going back to our work, uh, we
[1088] didn't just run this on dyno, we ran it
[1090] on a bunch of different vision models
[1092] and the trends are the are roughly the
[1093] same. So masked autoenccoders and
[1097] imageet classifiers also as you make
[1099] better language models, they correlate
[1101] more with um, vision model performance
[1104] and vice
[1106] versa.
[1108] Okay. Uh so if
[1111] uh I'm going to now move into some
[1113] explanations for why I think this might
[1115] be happening. Uh but if you're
[1116] interested in more evidence and more
[1118] measures of convergence and debates
[1119] about exactly how to measure
[1121] convergence, uh this is a huge field. It
[1123] generally goes under the name
[1124] representational alignment. Uh there's a
[1126] huge community in neuroscience that
[1127] looks at representational alignment
[1128] between the brain and neural nets. We're
[1131] looking at just representational
[1132] alignment between neural nets and other
[1133] neural nets. Uh and here are two uh
[1136] workshops that one of them is happening
[1138] in a few weeks. this realign workshop
[1140] and another one happens yearly at
[1141] Nurups. So if you're interested, there's
[1142] a lot more material to to get into in
[1144] this community. Uh but maybe suffice it
[1147] to say uh there is a large community
[1150] that has found that models are becoming
[1152] more and more alike in their kernel
[1153] structure and other types of internal
[1157] organization. Okay. So now I want to
[1159] talk about some ideas that we have for
[1160] why this is happening. And I'm going to
[1162] first talk about some kind of machine
[1163] learning 101 ideas and then I'll I'll
[1165] talk about uh kind of a toy model of
[1168] what we might be converging to. Okay.
[1172] So, so one idea what is driving this
[1174] convergence is what we call the
[1176] multitask scaling hypothesis. And this
[1179] is saying that if I'm searching for
[1181] functions that fit my data or fit my set
[1182] of tasks, well, if I have one task that
[1185] I train the model to perform well on or
[1187] one data set I train it to perform well
[1189] on, then this is the subspace um a of
[1192] hypothesis space, the subspace of the
[1194] set of all possible functions I could
[1196] learn that actually solve the task. And
[1199] so gradient descent will find a solution
[1201] within that space. But if I have two
[1203] tasks now, I have more constraints and I
[1206] have a strictly smaller subspace of
[1208] models that can fit two tasks. And as I
[1211] add more constraints, more data, more
[1212] tasks, then I get strictly smaller um
[1215] subspaces of hypothesis space that can
[1217] actually fit the data and solve all of
[1219] those tasks. Okay, so we're training
[1221] models on more and more data on more and
[1223] more tasks. And you should expect that
[1224] that will cause some
[1226] convergence. Uh this is related to two
[1229] other ideas that are out there. One one
[1230] version of this is called the
[1231] contravariance principle in neuroscience
[1233] and then again it's an anacurreninet
[1235] principle like all happy representations
[1238] uh have to solve all the constraints and
[1240] if you violate if you you know if you're
[1242] wrong in one way you'll fail on one of
[1244] the tasks uh so if you have a lot of
[1246] pressure to be uh correct in all ways
[1248] then it kind of causes
[1250] convergence okay
[1254] um but I think that's not all there is
[1255] to it I think another condition that's
[1257] important is that you have enough
[1258] capacity
[1259] that there is a chance that two models
[1261] can actually find the same solution. So
[1264] we call this a capacity hypothesis. It's
[1266] that bigger models are more likely to
[1268] converge to a shared representation than
[1270] small models. And the basic idea is
[1272] quite simple. It's that if I have two
[1273] small models, I go back 10 years in
[1275] time. Then the two small models like one
[1277] is a linear model, one is a quadratic
[1279] model, one is like a SVM, one is a
[1281] random forest. These things aren't
[1283] universal. They they they can only fit
[1286] certain types of functions. And the
[1288] solution found by one of the models uh
[1291] cannot be the same as the solution found
[1293] by the other model because the
[1295] hypothesis space spaces just don't
[1297] overlap. Um so let's say in the ambient
[1301] space of all possible functions the best
[1303] loss is achieved at this point in the
[1305] middle here. But if I'm only searching
[1307] over small model hypothesis space then
[1309] the best I can do in this model is here
[1311] that model there. If I make the models
[1313] bigger they're closer to being
[1314] universal. there's a a chance that
[1316] they'll actually overlap and that
[1318] they'll overlap on the um the lowest
[1321] loss solution in the ambient space. So
[1323] as models get bigger um they overlap
[1326] more in the set of functions they can
[1328] represent and that gives them the chance
[1330] of actual convergence. Okay, you have to
[1332] have enough capacity for
[1335] convergence. Um okay and then uh the
[1338] last of these kind of ML 101 type
[1340] explanations is the simplicity bias. So
[1342] here we have the set of functions that
[1344] actually fits the data and solves all
[1346] the task. That was that kind of
[1348] convergent subspace of the hypothesis
[1349] space that I mentioned before. But it
[1351] still might be big. This thing is is
[1353] technically called the version space.
[1354] And the version space can be a very big
[1356] object. There can be many different um
[1359] networks with different parameters that
[1360] equally well explain and fit the data.
[1362] But within that in that space of
[1364] solutions that fit the data and solve
[1366] the tasks, which one do you find? And
[1369] here comes the idea of regularization or
[1371] what I'm calling simplicity bias that
[1373] deep nets are biased to find simple fits
[1376] to the data. There's a lot of
[1377] interesting papers on this. Um so I
[1379] don't have time to talk about all the
[1380] details. But we think that simplicity
[1383] bias and implicit regularization can
[1385] also be helping to explain convergence
[1387] that you don't only try to find a
[1389] function that fits all the data and data
[1391] scales and that becomes a smaller space
[1392] but you also have this pressure towards
[1394] simple fits and so that constrains you
[1396] to an even smaller space. And one of the
[1398] interesting results that we and some
[1399] others have is that uh actually bigger
[1401] networks have stronger simplicity bias.
[1403] And so you might actually expect that as
[1404] models get bigger uh this this
[1407] simplicity um pressure will get even
[1409] stronger.
[1412] Okay.
[1414] Okay. So as we train bigger models with
[1417] stronger and better regularizers,
[1419] they're going to maybe converge to a
[1421] smaller um subspace of solutions.
[1426] Uh but what is what's this all going to
[1428] converge to? If could we really we
[1430] really get this down to just like a
[1432] single solution like a single
[1434] representation that all networks
[1435] converge to and what might that look
[1436] like? So I don't know. I think that's a
[1438] long way off. Uh but I'm going to
[1441] mention one kind of toy mathematical
[1443] model in which we can actually show
[1444] exactly what that would be. Um and this
[1448] is where we really get to this platonic
[1451] idea in the title. So uh the the basic
[1454] idea for what I think that we might be
[1456] converging to is something like Plato
[1458] imagined with his allegory of the cave.
[1460] So he said that uh you know this is this
[1462] is a story that comes up in machine
[1463] learning vision all the time. Um but
[1465] what Plato said is uh imagine that you
[1468] know we have prisoners in a cave and
[1470] their only experience of the outside
[1471] world is the shadows on the cave wall.
[1473] And it's an allegory because that's how
[1475] we behave right. Our only experience of
[1477] the the world around me is the photons
[1479] bouncing off the shadows like just the
[1481] projections of the world onto my retina.
[1483] I don't have access to the real world in
[1485] any kind of direct physical sense. I
[1488] have to infer that there's a world out
[1490] there. Okay. So we're imagining the same
[1492] situation. There is we think some you
[1494] know world out there Z. Uh and it gets
[1497] projected by different observation
[1498] functions. X is going to be a camera and
[1502] Y will be a caption that describes the
[1504] image. And uh you could also have a
[1507] mapping to the text space via not that
[1509] camera but via um somebody just having
[1511] direct experience and talking about it.
[1514] Um and then if I unimotally train
[1516] representations on either images or on
[1518] text, well because there's a common
[1520] cause, there's a common world out there,
[1521] the latent variable Z, uh they should
[1523] somehow arrive at both being ultimately
[1526] representations of Z. That's the common
[1528] cause. Okay. So how might that happen
[1532] mathematically in one concrete scenario?
[1533] I think this is just one toy model but
[1536] um it's a starting point for getting
[1537] kind theoretical traction on this thing.
[1539] Um so we'll imagine that the world
[1541] consists of a sequence of discrete
[1542] events Z and that these events are
[1545] sampled from uh some probability
[1547] distribution over events Z. And just
[1550] like if we want to get a little
[1552] philosophical this is what I personally
[1554] think of as like the platonic ideal
[1556] these ideal forms is it's just
[1557] statistics. It's just a distribution
[1559] over events that index into
[1560] observations. It's not necessarily
[1562] actual physics like physics is just um
[1566] something we infer. We don't have direct
[1567] access over it. Okay. But anyway, all
[1570] all the data is mediated by observation
[1572] functions like cameras and people
[1574] describing the scene. Uh and observation
[1577] functions are mappings from events to um
[1579] data X and Y. And in this world, we're
[1583] going to model model co-occurrences.
[1585] We'll consider that this is a time
[1586] series over Z. And we'll model
[1588] co-occurring observations. So at two
[1591] different adjacent points in time uh
[1593] what was my observation x at time one
[1596] and time two and we'll try to model that
[1598] distribution of co-occurring
[1600] observations. And this is uh roughly how
[1603] modern contrastive learning systems work
[1605] in computer vision. They try to model
[1607] the co-occurrence distribution over
[1610] visual uh observations like like two
[1612] co-occurring patches in an image or two
[1614] co-occurring frames in a video. It's
[1616] also something people do in language uh
[1619] where they try to learn embeddings that
[1621] will uh model the co-occurrence of two
[1623] words in the same sentence. So going
[1625] back to models like word tobec for
[1627] example. Okay. So if you do this uh and
[1632] you do contrastive learning with a noise
[1634] contrastive estimation objective then
[1636] what you can show and what people have
[1638] shown is that this uh the solution to
[1640] this objective the minimizer of that
[1642] objective is the uh co-occurrence
[1644] function. It's a pointwise mutual
[1646] information function. So it's how often
[1648] do the two observations co-occur divided
[1650] by the probability that they would
[1652] co-occur if they were independently
[1654] sampled. Okay. So what this math is
[1657] saying is that uh we're going to learn a
[1659] representation f that maps data into
[1661] vectors. We're going to measure the uh
[1663] similarity between two representations.
[1665] So this is the inner product that gives
[1666] me my kernel and the kernel converges to
[1669] embeddings in which similarity in which
[1671] the kernel structure is equal to the uh
[1674] normalized co-currence rate. So in
[1676] particular the pointwise mutual
[1678] information
[1679] function. Okay, so that's that's the
[1681] platonic kernel according to this math.
[1684] Uh it says that apple and orange will
[1685] embed near each other because they
[1687] co-occur a lot together in nature in
[1689] kitchens and elephants don't co-occur as
[1691] often with apples and
[1693] oranges and okay now here comes the big
[1695] assumption of the model because I've
[1697] said that this is what uh your kernel
[1699] over images looks like but what about
[1701] your kernel over text so if we assume
[1704] that the observation is a bjective
[1706] function of the underlying event so we
[1709] don't lose any any information which is
[1711] a huge assumption and not true in
[1712] reality um and we have discrete random
[1715] variables then all the probabilities
[1717] kind of carry through the observation
[1718] function and the PMI over the
[1722] observation observations is equal to the
[1724] PMI over the underlying events and
[1727] therefore
[1728] the PMI over images that's learned by
[1732] the model is equal to the PMI over words
[1735] that's learned by the model because both
[1737] of those are equal to the PMI over
[1739] events and so it implies that the
[1742] language model and the vision model
[1743] trained with a NCE contrastive objective
[1746] will converge to identical kernels.
[1748] Okay, so it's a toy model in which that
[1750] will occur. So it just says that the
[1751] word apple and the word orange will
[1752] embed near each other uh because those
[1755] words co- occur in descriptions of
[1757] kitchens in the same way as those images
[1759] co-occur in images of kitchens.
[1762] Okay, so I think this model deviates
[1765] from reality in some interesting ways
[1766] like we don't have discrete random
[1767] variables, we don't have bjective
[1769] functions, but it's a starting point uh
[1771] for understanding what that platonic
[1773] kernel that ultimate representation
[1775] might look
[1777] like. Okay, so I now want to um go into
[1782] the last sections of the talk where I'll
[1784] mention some counterarguments because
[1786] you're probably thinking this sounds
[1787] like a little too too far-fetched. like
[1789] maybe there's some convergence, but like
[1790] come on, it's not going to get to some
[1791] platonic kernel. So, let's see some
[1795] counterarguments. Okay, so the I think
[1797] the most important counterargument um
[1799] and so we talked about this in the
[1800] original paper, but there's also been
[1801] some follow-ups that go into it in more
[1803] detail. Uh I think it's an important
[1806] point is that um hold on, there's got to
[1809] be unique information in text that's not
[1812] captured in images and vice versa. So
[1814] different modalities, how could they
[1816] learn the same representation of the
[1818] world if they fundamentally measure
[1820] independent sources of
[1822] information? Okay, so in
[1824] vision, you can go and see a solar
[1827] eclipse and I think that's just an
[1829] ineffable experience. I don't know how
[1831] to put that in writing and convey to
[1833] somebody that that actual experience.
[1835] You have to see it for
[1837] yourself. Or in language, there's
[1839] abstract concepts
[1840] like freedom of speech. How can you have
[1843] a visual experience which captures the
[1845] same meaning as that abstraction freedom
[1847] of
[1849] speech? Okay, so these are cases of uh
[1852] where you don't have a bjection between
[1854] the underlying events the underlying
[1856] platonic world and the observations in
[1858] vision or language. So language being
[1860] abstracted that means you lose
[1861] information or uh you could have a
[1863] partial observation like an image
[1864] doesn't actually capture the same
[1866] information. Okay, so these are places
[1868] where the mathematical model um falls
[1870] apart and so I think this is a real
[1872] limitation to the
[1873] analysis. Yet at the same time, some of
[1876] our best computer vision systems are
[1879] trained to reduce the world to language.
[1882] So clip is a state-of-the-art computer
[1884] vision system that just tries to
[1888] explicitly align images with sentences.
[1890] So it's trying to remove all information
[1892] about the world other than that which is
[1893] contained in sentences. And so somehow
[1896] our standard engineering practice in
[1897] computer vision is to remove unique
[1900] information about vision. Uh maybe
[1902] that's a a bad
[1904] idea. Uh I'll I'll point out this
[1906] interesting follow-up that uh Paul Yong
[1908] and others did over at MIT um here uh
[1912] which goes into this in more detail. So
[1915] uh they're showing that um basically the
[1918] platonic hypothesis will hold if you um
[1922] have shared information between two
[1924] modalities and everything is you know
[1926] mathematically bjective in the way that
[1927] I was describing but in reality that
[1929] might not be the case and you could get
[1931] other trends where as you get more
[1932] alignment between modalities you might
[1934] get worse performance uh of the models
[1936] or as performance gets better you might
[1937] get less alignment. So that there'll be
[1939] an anti-correlation between alignment
[1941] and performance on um on certain tasks.
[1944] And they say that this is going to
[1946] happen when a task requires the unique
[1949] signal in a modality that's not shared
[1950] with the other modality. And they even
[1952] show empirically that on some data sets
[1954] you do see that that um as models get
[1957] more and more aligned they actually get
[1958] worse in
[1961] performance. Okay.
[1963] Uh but but I do think we there's another
[1967] um you know saving grace to this which
[1970] is yeah language might not have the same
[1973] information as in a photo but maybe a a
[1977] paragraph or a book could have the same
[1978] information as in a photo. You know an
[1979] image is worth a thousand words. And so
[1981] we actually ran this this little
[1982] experiment where we said let's look at
[1984] the alignment between visual embeddings
[1986] and language embeddings but now we're
[1988] going to increase the length of the text
[1990] that we're going to embed. So we're
[1991] going to take captions which are very
[1993] long 30word captions and as you increase
[1995] the number of words in your captions
[1997] your embeddings of those captions become
[1999] more and more aligned with your
[2000] embeddings of the the images those
[2002] captions describe. So yeah I think maybe
[2004] in theory if we have really really
[2007] descriptive text then it might actually
[2009] capture the same information as in a
[2011] visual experience but if we have short
[2013] text then that's not going to happen and
[2015] there'll be a cap to the alignment that
[2016] you can
[2018] achieve. Okay. Uh the other big
[2021] objection uh which I think is important
[2022] is that a lot of this convergence might
[2025] not be platonic in some ideal sense. It
[2027] might be we're converging yes but not
[2029] not to reality. We're converging to uh
[2031] biases and we're converging to the
[2033] internet's view of reality which is not
[2035] actual reality and we're converging in
[2037] bad ways. And this could be due to bias
[2039] in the data. It could be due to
[2040] fundamental limitations in the
[2042] transformers and the models that we use
[2043] today. And it could be sociotechnical
[2045] that we all kind of compete on the same
[2047] benchmarks and that causes us to
[2048] converge but not for a good
[2051] reason. Okay. So uh in the last uh few
[2056] minutes I'm going to talk about um some
[2058] implications and applications. Okay. So
[2060] this was all a bit philosophical but
[2062] what can we actually do? Can we make
[2063] better systems now out of
[2065] this? Okay. So I think one important
[2068] implication is that you can share data
[2070] between modalities. So if the
[2072] representation if all roads lead to Rome
[2074] right if all different ways of modeling
[2076] the world uh lead to the same um you
[2079] know ultimate representation then we
[2081] should be able to get there through all
[2083] these paths and uh share information
[2085] between the different paths. So it
[2087] should be the the case that we can train
[2089] our vision models on language data and
[2091] make them do better. We can train our
[2092] language models on vision data. We're
[2094] going to look at two experiments here.
[2095] One is can we train better image
[2097] generative models, diffusion models by
[2099] aligning them to visual encoders. Uh and
[2102] two, can we train better language models
[2104] by aligning them to to vision models. So
[2106] now we're running kind of more causal
[2108] experiments. We're not just trying to
[2109] look at trends, but we're going to try
[2111] to actually optimize our models to be
[2112] aligned and see what
[2114] happens. Okay, so the first one um can
[2117] we train diffusion models by aligning
[2119] them to vision models? Uh this is not my
[2121] own work. This is uh work from signing
[2123] uh she and others at NYU and what they
[2126] found is that if you do this kernel
[2129] alignment so you take a diffusion model
[2130] that generates images from noise and you
[2134] take a pre-trained uh visual encoder uh
[2137] of the kind that I was like clip or dyno
[2140] uh and you simply uh have a additional
[2144] loss that says I want my kernel uh
[2147] structure to be the same between the two
[2148] models. So I want to uh have my
[2150] diffusion model uh use the kernel
[2153] structure inside my pre-trained vision
[2155] model. You'll get a much faster learning
[2158] of your image generation. So image
[2161] encoding and image decoding image
[2163] generation uh
[2165] can benefit each other via this uh
[2168] kernel structure. They both have similar
[2169] internal
[2172] representations. Um okay, here's one
[2174] that we did. This is uh Yulu and and Ivy
[2177] um have been doing this recently. Uh
[2178] it'll be at this realign workshop this
[2180] uh in a week or two at iClar. Uh where
[2184] they train a language model to be
[2186] aligned with the kernel structure of a
[2188] vision model. And the question is do you
[2190] get a better language model better at
[2192] modeling you know predicting the next
[2193] word doing language reasoning tasks. And
[2196] so it's roughly the same idea as on the
[2198] previous slide. Uh the visual is a
[2201] little different, but we take our
[2202] language model, we train it to predict
[2203] the next word, but we also extract its
[2206] kernel on some layer and align that
[2209] kernel with the kernel of a pre-trained
[2210] vision model like Dino. And we say, does
[2213] that actually make your language model
[2214] get better when you force it to
[2215] represent the world more
[2217] visually? And the answer is yes, it
[2219] actually works. So uh here's your
[2221] baseline language model. And if you try
[2225] to align it its internal structure, the
[2227] kernel to dino small, you even get a
[2230] tiny boost on this like pretty bad
[2232] vision model. This is like a llama like
[2235] a big language model. So it's not uh
[2237] trivial to get a boost. And you can get
[2240] bigger boost when you align your
[2241] language model to uh bigger dynino
[2243] models, giant dynino model better. And
[2246] then interestingly, there's some other
[2247] models that do do the best on this task.
[2251] Okay, so kernel alignment is not just a
[2254] spurious correlation. Actually,
[2256] optimizing for it can improve
[2258] performance of language
[2260] modeling. Um, another implication is
[2262] that cross modal learning between at
[2264] least language and vision should be uh
[2267] relatively easy because you can use the
[2268] kernel as a bridge. So let's say I have
[2270] my uh embedding trained on images to map
[2274] to an image embedding my my model
[2276] trained on text to map uh from uh like a
[2279] noise vector to output text. Well then
[2282] to learn translation I should just have
[2283] to somehow align these representations.
[2286] And if the representations measure
[2287] distance in the same way then they're
[2289] related by an
[2290] isymmetry they're related by a
[2292] transformation that preserves distances
[2295] and that's a very simple kind of
[2296] transformation.
[2297] Um so recently this has been an old kind
[2301] of goal of can you do unpaired
[2303] translation between images and text uh
[2306] and the kind of platonic idea suggests
[2309] that it should be relatively easy
[2310] because the kernel can be a bridge
[2312] between these two domains and recently
[2313] these uh there's an interesting paper
[2315] that actually tried this and they found
[2318] that okay so if I have a vision model
[2320] that has measured distance the same way
[2322] as a language model so the triangle like
[2323] the uh these distances are all the same
[2326] then it's just a rotation to align them.
[2328] It's just an isometric transformation to
[2330] align them and they can optimize to find
[2332] this like rotation or it can also have
[2334] translation. It can have a few things.
[2336] Uh they can optimize to find that
[2338] transformation that will align the two
[2339] modalities without paired data at all.
[2342] And it's it works at a non-trivial
[2344] level. It doesn't nail the problem but
[2346] they show
[2353] non-trivial level with no paired
[2355] examples. You just you go to Mars, you
[2357] listen to the Martian speak, you look at
[2359] the rocks on Mars. No Martian ever
[2360] points out that this is the word for
[2361] rock. And yet you can infer that what
[2363] the word for rock is just based on these
[2366] um the statistics of the word usage and
[2368] the uh visual observations. That's
[2370] that's roughly what they're claiming
[2373] here. Okay. Um there's some interesting
[2376] theory work that Lorenzo uh Rossako and
[2380] um and his colleagues have been doing uh
[2382] additionally on this idea of you know
[2384] under what theoretical conditions can
[2386] you actually learn uh to bridge between
[2388] modalities uh given that the kernels are
[2390] aligned. So you can actually bound the
[2393] um ability to stitch between two
[2395] different modalities by the kernel
[2396] alignment measures that that I've talked
[2398] about in this in this talk. Um, so I'm
[2400] not going to have time to go into this
[2401] one, but just another pointer if you're
[2402] interested in a theoretical lens on
[2405] this. Um, okay, one last one is I really
[2409] love this old problem called the Molyneu
[2411] problem. This, uh, philosopher Molyneu
[2413] wrote a letter to John Lock and he said,
[2415] uh, assume a blind man can tell the
[2417] difference between a cube and a sphere
[2418] by the way, uh, they feel when he
[2421] touches them. If the man were to be
[2423] given sight, could he immediately tell
[2426] uh which is the sphere and which is the
[2427] cube simply by looking at them? So, it's
[2429] this scenario. We're doing not touch and
[2431] vision, but we're doing vision and
[2433] language. If I have a language model
[2435] that knows how to understand this text,
[2438] and I then give my system a camera, can
[2443] I immediately learn to map from the
[2444] camera to the um the representation, the
[2447] meaning of the text?
[2449] And well if the uh representational
[2454] structure of the world uh you know is uh
[2456] if if if language modeling finds the
[2459] same representation as visual modeling
[2461] then this should this learning problem
[2463] should be relatively easy and if I
[2465] already have that representation I
[2466] already have that target that the thing
[2468] would have converged to it should be I
[2469] can learn it quite quickly. Um and but
[2473] Voninha and others in BCS have shown
[2475] that uh in fact if you do give children
[2478] uh sight who have cataracts and are born
[2480] uh blind but you give them sight at a
[2481] certain age uh they can't understand the
[2484] visual world immediately but they can
[2486] relatively quickly. It's not like they
[2487] have to redevelop uh along the same time
[2490] scale as um an infant would under uh uh
[2494] from birth. So new modalities can be
[2496] efficiently scaffolded onto existing
[2497] knowledge because they share similar
[2499] representational
[2501] structure. Okay. So final implication is
[2504] just if there really is some truth to
[2506] this platonic idea and there is some
[2508] representation that can be characterized
[2509] and can unify modalities. It seems like
[2511] an important thing we should seek it
[2512] out. We should better characterize it uh
[2514] and see how far that goes. So I'll end
[2516] there and thanks to the co-authors and
[2518] all of you.
[2524] Thank you so much Phillips. So let me
[2526] kick off the Q&A with a couple of
[2528] questions. Um I wonder if you can
[2531] elaborate a bit on the metrics you have
[2534] used to decide the alignment and
[2539] um so uh so in particular did you try a
[2543] lot of metrics or How how do you know
[2546] that you got the right? Yeah.
[2550] Um yeah, that's a great question. So, we
[2553] did try a lot of metrics. So, I I uh
[2556] essentially the metrics are uh different
[2560] ways of measuring how similar this
[2562] kernel is to that kernel. And I could
[2564] just look at like uklidian distance or
[2565] something simple. Um the one that we
[2568] ended up using for most of our
[2570] experiments is based on uh nearest
[2572] neighbors. So, it's asking are the
[2576] nearest neighbors in embedding space to
[2579] an uh are my nearest neighbors of this
[2582] image embedded by a vision model
[2585] um the same as my nearest neighbors of
[2588] the caption of that image embedded by a
[2590] language model. Uh so if I embed a photo
[2594] of euseity are the image nearest
[2595] neighbors euseity in the same way as the
[2598] text nearest neighbors or captions about
[2600] eused so that's the particular metric we
[2602] used and why did we use that one well we
[2604] tried a bunch and this one worked the
[2605] best so the way I would phrase it is
[2607] that we see convergence of the kernel
[2610] structure in terms of the local
[2611] neighborhoods the local neighborhoods
[2612] are converging maybe the global layout
[2614] like there could be scaling global
[2616] scales that actually are not being um
[2618] converged but doesn't this just capture
[2620] co occurrence
[2622] Yes, I think it I think that's kind of
[2624] that's kind of the um the theoretical
[2626] model we get to is that uh yeah um this
[2631] if two things co-occur the same way in
[2633] two different modalities then these
[2634] models will you know that will surface
[2636] in both of these models.
[2639] Okay. So I have two quick follow-ups and
[2641] then I will open uh for uh questions. We
[2645] have live a live audience so we'll take
[2648] some questions from the live audience.
[2649] Also, if you would like to ask a
[2651] question uh on Zoom, please put your um
[2654] question your hand up. Um so, my my
[2657] question is about what do we understand
[2660] from aligning uh language with vision?
[2665] So, um when you in fact this was um in
[2668] one of your um most uh your your latest
[2671] uh charts. So, if you can put that back
[2673] up um this is uh Yeah, that next one.
[2677] Next one. Next one. Yeah. So, um doesn't
[2680] that mean that by connecting language to
[2685] uh uh to vision uh you are finding some
[2689] aspects of the physical world that
[2691] you're bringing into statistical system
[2693] that otherwise does not have a uh
[2697] predefined understanding of the physical
[2700] uh world. Isn't this what we're getting
[2702] from um from this kind of experiment?
[2706] Yeah, exactly.
[2708] So, um, language models, I think one of
[2710] the critiques right now is that maybe
[2712] they don't have a lot of, you know,
[2713] embodied experience. They don't they're
[2715] not grounded. Um, and to some extent
[2719] they can learn this from massive data
[2721] online that talks about visual
[2723] experiences, physical experiences, but
[2725] maybe it's not perfect. And I think that
[2727] might be part of the idea here that
[2729] you're injecting knowledge from another
[2730] modality uh that uh is a more sample
[2734] efficient way of collecting that kind of
[2736] data. But have you tried um to do this
[2739] alignment with fantastical images that
[2742] do not obey the laws of uh oh yeah of uh
[2745] physics? Um I mean if you do it with
[2748] imageet of course those are all images
[2750] taken from the physical world it could
[2753] be interesting to create a data set of
[2755] fantastical images to see what happens.
[2758] I really like that idea. We have some
[2759] other work on like uh these fantastical
[2762] random noise images. Uh this is a
[2764] collaboration with Antonio Talba and
[2766] others and um you can train vision
[2768] models on those and they learn good
[2770] visual features. They're like random
[2773] fractals and blobby images. We haven't
[2775] tried aligning language models to that
[2777] kind of data. That would be really
[2778] interesting. Well, let's work on that. I
[2780] also have one more quick question. So
[2783] the fact that uh we see alignment uh
[2786] between language models and vision
[2788] models is very interesting to me. that
[2790] almost suggests that there is a ceiling
[2792] to what we can do with these models. U
[2794] your comments please. Yeah. Is there
[2797] just to suggest there's a ceiling? I I
[2799] think this yeah there's one perspective
[2801] is
[2804] um that maybe this is a bit diminishing
[2807] to computer vision like oh if vision
[2809] models converge to the same thing as
[2810] language models then it turns out that
[2812] there's these models are not actually
[2814] capturing all those like physical
[2816] details we thought that they're just
[2818] capturing semantics in the end. Um, and
[2822] in some sense that might indicate that
[2824] yeah, our approaches right now do have a
[2826] ceiling. Like the ceiling is the types
[2828] of semantics that language is good at
[2829] conveying. And um, you could read this
[2832] as evidence for that, I would say. Very
[2835] interesting. Um, all right. Any
[2837] questions from uh, the live audience?
[2839] Yes, in the back.
[2845] Far. So, if we draw a trend line, how
[2847] far are we from 1.0? So I'm these plots
[2851] were um some of them are on log scale.
[2855] So it's a little bit hard
[2856] to hard to extrapolate uh linearly. Um
[2861] but additionally I think that even on a
[2863] log scale they're trailing off. So you
[2866] can see over here it starts it looks
[2867] like it's starting to trail off. And
[2868] then if I show you the the recent thing
[2870] from the the paper that came out just a
[2873] few weeks ago here again you see the
[2875] scale is going to 18 and we're going you
[2878] know 10 times bigger model to do that
[2880] and like 10 times more data
[2882] approximately. So this is all like power
[2884] law scaling and um I don't think we'll
[2887] get to one according to under these
[2890] current trends one will take like the
[2891] lifetime of the universe but maybe
[2893] there's a way to you know change the
[2894] slope of the scaling law. Uh let's take
[2898] a question uh from the online audience.
[2900] Danny,
[2902] hi Phillip. Uh can you hear me? Okay.
[2905] Yeah. Excellent. Um thanks for this
[2907] talk. Um I wanted to just present a
[2911] slightly alternative philosophical view
[2914] and ask if it changes what you think the
[2917] implications of your findings are. Um so
[2920] u the kind of Vickensteinian view of
[2923] language as you probably know is you
[2926] know it it sort of says um uh meaning
[2932] uh there is no platonic meaning in some
[2934] sense we're all in the cave uh but we
[2938] have learned to function together in the
[2940] cave because of the way we use language
[2943] together and that me meaning arises
[2945] through use and I think I think as I
[2948] hear your findings, they're equally
[2951] consistent, maybe even more consistent
[2953] with that view that what you're showing,
[2956] I think, is that these models are
[2961] learning about what we as human beings
[2964] mean with with uh language and images.
[2968] Um, and I'm just curious whether that
[2971] changes anything if you kind of give up
[2973] on the Platonic representation and just
[2975] say we're we're kind of in the messy
[2977] soup of human language and there's
[2980] nothing really below that to find.
[2984] Yeah. Yeah. I think that's that's um I I
[2988] completely agree. Uh we were playing
[2991] with calling it like the Vickenstein
[2992] Plato hypothesis, but felt like that was
[2994] a little too too pretentious. Um Right.
[2997] So I yeah I think
[2999] that yeah I don't know enough of the
[3001] philosophy here to know really what
[3003] those two meant. Um but to me this this
[3008] um you know underlying reality that
[3011] generates things it actually is just a
[3014] co-occurrence. It's just a statistical
[3016] distribution over events and that can
[3018] come in through observation of the
[3020] statistics of the of the word usage or
[3023] the observations of um reality through a
[3026] camera. Uh and so that might be more
[3029] consistent with Vickenstein. Uh but I I
[3032] think that that's the same as an ideal
[3034] form in Plato's language. He just
[3035] thought of he just phrased it
[3037] differently. So there's some
[3038] philosophical debate to be had there.
[3040] But um yeah, these are all just
[3041] metaphors to try to get us at kind of um
[3045] the problem. It may have something to do
[3046] with
[3047] these point. We have time for one more
[3050] quick question uh from the live
[3052] audience. Go ahead.
[3067] Uh yeah, that I I think can this um tell
[3070] us anything about adversarial attacks?
[3072] Does this mean models are robust? Are
[3074] they vulnerable? I think that one is
[3077] like a um a pessimistic take would be
[3081] well all these models are vulnerable to
[3083] the same attack. So there's a danger
[3085] like it's like we have a homogeneous
[3087] population and a virus can come in and
[3089] take over and and so if these things are
[3091] converging then they might all have the
[3093] same vulnerability or maybe the same
[3095] bias and this can be dangerous. And a
[3097] positive take might be uh would these
[3100] all get better at actually modeling So
[3102] if language models get better at
[3104] modeling the world in a way that is
[3105] aligned with vision models and we think
[3107] that vision models are more grounded and
[3108] actually are are robust in a way that
[3111] language might not be then it's kind of
[3113] a positive that if I just train on more
[3115] language data it'll eventually become
[3117] actually grounded in reality. Uh so I
[3120] think you can see it in both ways. One
[3122] more quick question from online. Uh your
[3125] improvement in accuracy is 4%. How are
[3128] we going to get a lot of improvement?
[3131] Oh yeah, that's a great question. And I
[3134] think you might even be um are you is
[3137] the question referring to if the
[3138] question is referring to this plot, I'll
[3139] say it's actually less than 4%. It's
[3141] 1.5%. Uh there might be other plots
[3143] where we show a bigger improvement. Um
[3146] but yeah, I I think
[3149] that at a certain scale the models have
[3153] unimodally become quite powerful and
[3156] already quite quite aligned and there
[3157] might not be that much more juice to get
[3159] by explicitly training them to be
[3161] aligned or explicitly sharing data
[3162] between the two domains. So how are we
[3165] going to get you know a massive
[3166] improvement by multimodal machine
[3169] learning? uh it might be in the regime
[3171] of enough unimodal data you just can't
[3173] because you already have saturated uh
[3176] but I would also say the jury's out and
[3178] maybe people will be clever and come up
[3180] with you know better techniques.
[3182] Let's thank Philillip once more and
[3185] thank you all for joining us. Uh see you
[3188] next week uh at the CEL forum with you
[3191] and Kim. Thank you.
