---
schema_version: 1
id: yt-tyYIuvbV2po
type: youtube
title: A New Framework for Modeling Brain Information Processing - Nikolaus Kriegeskorte
url: https://www.youtube.com/watch?v=tyYIuvbV2po
authors:
- Stanford
ingested_at: '2026-05-30T20:02:05Z'
content_hash: sha256:5b7a68706a4d3f817abc4363c9fe1e9d65c46e09a5527ebaba3ac4af7051ec1a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Stanford
  channel_url: https://www.youtube.com/@stanford
  duration_seconds: 2991
  caption_track: fetched
  snippet_count: 1165
filter:
  score: 0.7
---
[1] [Music]
[5] Stanford University.
[8] Good afternoon everybody. I'm Brian
[10] Wendell from the psychology department
[12] and uh I'm also involved in electrical
[14] engineering and uh of opthalmology and
[18] radiology. Uh I'm I'm the third of
[21] Bill's uh deputies. Uh you're only going
[24] to get to see three of us today. uh
[27] Melanka who we never know where he's
[30] Malanka somewhere. The one thing you can
[32] depend on with Malanka is he's rooting
[34] for the New England Patriots wherever he
[36] is. That's a that's a that's a constant
[38] for him. And uh some of you may wonder
[41] what these deputies actually do. We all
[43] meet. It's very pleasant group. We all
[45] uh meet Miriam uh sometimes Rob often
[49] Scott. uh once a week on Monday
[52] afternoons from 3:00 to 5:00, we eat
[54] some peanuts and uh we help Bill figure
[58] out uh what he needs to do next. And
[60] Bill does uh the overwhelming amount of
[63] work uh with help from Tanya and so
[65] forth. And the rest of us cheer him on
[67] and uh give him occasionally okay
[69] advice. Um but I'm not here to talk
[72] about Bill. Uh I'm here to talk about
[75] Nico. Nik Nicholas Crius Cord is here.
[79] It's my pleasure to introduce him for
[80] this afternoon's talk and he joins us
[82] from Cambridge, England where he is a
[85] program leader in uh the memory of of
[89] the memory perception group at the
[91] medical research council uh and he works
[94] in cognition and brain sciences uh unit
[97] there. Uh Nico has actually worked with
[100] a large number of people who are really
[102] kind of friends of Stanford and I see
[104] Nico is coming from this wonderful
[106] tradition. He originally got his uh
[109] degree in psychology and computer
[111] science which is a great uh interaction
[113] something that we here in psychology are
[115] always very positive about. I see Jay
[117] Mlen there and he's really leading an
[119] effort on that. uh Nico then took his
[121] degree with Reiner Google who's here all
[124] the time uh and a great friend of the
[126] and the university and that was during
[128] the early days of the development of
[131] functional magnetic resonance imaging
[133] and so Riner got you pushed off in the
[135] direction of confronting brain data and
[137] and actual human measurements at that
[140] Mox plunk there. He then went on to uh
[143] work as a post-doal fellow with Camille
[146] Ugerbell and who's been longtime friends
[148] of ours here and with I see Gary over
[150] there and we see Camille all the time
[152] and then he went and took another
[154] posttock with Peter Banditini and Leslie
[156] Underlighter uh at the NIMH before going
[159] on to um to to Cambridge. Uh, Nico is
[163] one of an exciting group of young
[166] investigators who are using
[167] computational methods to investigate how
[170] information is represented and processed
[174] in the primate brain. And there will be
[177] a fair amount of uh young people talking
[179] this afternoon. I'll I'll remind you
[181] about this later. and his lab's focus is
[183] on the neural mechanisms of visual
[185] object perception and both health and
[189] disease and how these mechanisms vary
[191] between individuals. So looking at one
[193] person at a time and understanding
[195] individual differences and Nico, thank
[197] you for coming out and making this trip.
[199] We look forward to your presentation.
[201] [Applause]
[207] Thanks Brian. Wow, what an honor to
[209] speak here. Um, let me see if this
[213] works. That's
[215] great. So, I've uh adjusted my my title
[219] a little bit um to make it even more
[222] provocative than it was before to make
[224] it outrageous enough to I hope provoke
[228] you to uh ask me some difficult
[230] questions at the end. I love the fact
[232] that there's enough time here for
[234] actually having uh some interaction at
[236] the end. And I I hope that's going to
[238] work out and you're going to challenge
[240] me on some of the things that I'm going
[241] to say. Um, so my title is deep neural
[245] networks, a new framework for
[246] understanding how the brain
[250] works. What does it mean to understand
[253] how the brain works? I think this is a a
[255] question that um has been of great
[258] interest to me over the years and it's
[260] only in the last couple of years that
[262] I've kind of come to an answer for
[264] myself. I don't think there's one
[266] correct answer to this, but I'll give
[268] you my answer and maybe maybe you have
[271] your own. Um, so to me it means to
[274] explain neuronal activity
[276] patterns to explain behavioral data
[279] ideally in humans because ultimately
[282] that's what motivates me. I want to
[284] understand the the human brain
[287] ultimately using fully explicit
[289] computational models. So models that are
[292] implemented in computers and that
[294] actually perform the task the cognitive
[296] task in
[297] question. Ideally these models should be
[300] neurobiologically plausible and they
[302] should perform real world complex
[305] cognitive tasks. So not toy versions of
[309] tasks but they should be able to
[310] interact with the real world. So they
[312] should be um artificial intelligence
[315] systems at the same time. So
[317] historically different um disciplines
[320] have tackled some of these uh criteria
[322] for success in in my mind um but we
[326] haven't really been able to to combine
[329] all of them at the same time. So for
[331] example, behaviorism um was concerned
[334] just with behavioral data and um that
[337] was a major limitation. Cognitive
[339] psychology stretched in the direction of
[342] information processing models of what's
[344] going on inside the brain. But it its
[348] verbal cognitive theories fell short of
[350] being fully explicit. Uh and that's
[353] probably the reason why it was
[355] superseded by cognitive science um which
[359] was at this cognitive level but more
[361] rigorous about the modeling. it had
[363] fully explicit computational
[366] models and I think that's why cognitive
[368] science in my mind is still a relevant
[371] discipline and the cognitive science
[373] society conference that initially got me
[376] excited about uh brain and cognitive
[380] sciences uh is is a good conference to
[383] this
[384] day. However, cognitive science doesn't
[388] really engage brain activity. So when
[391] for me it came time to choose a PhD
[393] project, I felt like uh AI and and and
[397] cognitive science are not enough. I I
[399] want to study brain activity as well. Um
[403] so we had cognitive neuroscience at the
[405] at the time. So cognitive neuroscience
[408] uh with the the advent of brain imaging,
[411] non-invasive functional magnetic
[413] resonance imaging in humans that was a a
[416] revolution and it was very important.
[418] However, as we tackled these complex
[422] brain activity data sets, we temporarily
[424] lost theoretical sophistication and um
[427] we didn't really test uh explicit
[430] computational models anymore for about a
[433] decade because we had our hands full
[436] just dealing with the with these tens of
[438] thousands of channels. I think it was a
[440] natural progression.
[442] So perhaps a discipline that's done best
[445] in terms of explaining neuronal activity
[448] um patterns with fully explicit
[450] computational models is computational
[452] neuroscience. And this is u an an
[455] exciting field um that I'm always uh uh
[459] fascinated by and um trying to to to
[462] follow as best I can. computational
[465] neuroscience has been very successful at
[467] predicting sensory responses of neurons
[470] to arbitrary novel images that these
[472] models have not been trained with. Um so
[475] that's a major achievement I think and
[478] also in higher level regions there are
[479] sort of models uh of evidence
[481] accumulation and decision making that
[484] sort of close the loop all the way um to
[487] behavior from um perception to behavior.
[490] However, what's not completely been
[493] successful is uh doing this for really
[497] complex cognitive tasks. So when we look
[500] at uh this area here, so real real world
[503] tasks like object recognition that just
[506] inherently require a lot of knowledge
[508] about the world and I think most of what
[511] the brain does requires massive world
[514] knowledge. AI had to learn that the hard
[516] way. AI started out with uh ideas about
[520] very general uh algorithms for
[522] intelligence and then learned that uh
[525] that that doesn't work. They all have
[527] exponential time complexity. So what you
[530] need is massive amounts of knowledge. Uh
[532] initially that was handcoded but then it
[536] it led to the rise of machine learning.
[538] machine learning is as important as it
[540] is because to make intelligence work we
[543] need to learn massive knowledge about
[545] the the world and I think in
[548] computational neuroscience also um we
[550] have to learn that we need these really
[552] uh complex models that don't have a very
[555] simple description possibly. So um a
[560] third highly relevant discipline here is
[562] artificial intelligence which has been
[564] the um discipline that has classically
[568] developed these computational models
[569] that actually perform feats of
[572] intelligence and artificial intelligence
[575] is making great strides at the moment.
[577] And there is a single um modeling
[579] technique that really falls at the the
[581] intersection of all of these and um I
[585] think therefore is uh poised to provide
[588] major progress for uh brain science as
[592] well. And this technique is uh neural
[594] networks. Neural networks are artificial
[597] models um inspired by the brain but
[600] highly abstracted that can learn massive
[603] amounts of world knowledge to uh solve
[605] artificial intelligence tasks. Neural
[608] networks have a long history in each of
[610] these three fields. They're very very
[612] old idea actually and they have a long
[615] history in each of these fields.
[616] However, they have they are only
[618] beginning to be used to meet these these
[621] two goals to explain neuronal activity
[623] patterns and to explain behavioral data.
[626] I think um Stanford is probably one of
[628] the best places in the world to pursue
[631] this uh framework which is just emerging
[634] and uh you've just made a really great
[637] decision in hiring Dan Yammens who's one
[639] of the major proponents of this
[641] approach. So my job is going to be to
[644] try to convince you um that you should
[646] be uh collaborating with Dan uh in in
[649] this direction. So this is sort of the
[652] the big um story. I would like at the
[655] end of my talk um for you to to uh maybe
[659] get some of the excite share some of my
[661] excitement about this direction that's
[663] currently uh emerging. So um in order to
[667] illustrate that I'm going to tell you a
[669] much smaller story about how in my lab
[672] we've come around to this this approach
[674] and sort of have some initial results in
[677] this
[680] direction. So in my lab we study a
[683] particular problem which is visual
[685] object recognition and that involves
[688] recognizing all the objects in real
[690] world images like this one um where we
[693] do this very effortlessly. we might
[695] uh recognize some of the the people in
[698] these images. We immediately draw a host
[701] of semantic inferences
[704] automatically and we'd like to
[706] understand this this problem. So for
[708] visual object recognition research um
[711] the goal could be um stated like this.
[713] We want to build a biologically
[715] plausible network model that can
[718] recognize novel object images that the
[720] model has not been trained with.
[722] importantly of course otherwise it's
[725] useless and predict their neuronal
[727] representations as well as human
[730] behavioral
[733] responses. So one really key
[736] methodological uh challenge in this
[739] context is how to compare
[742] representations in computational models
[744] to brain representations. This is really
[747] uh not an easy task because we think of
[750] the representations as inherently
[752] multivaried. We think of them as
[753] population codes. So they live in this
[756] very highdimensional space in both the
[758] brain and in the model. And we don't
[760] know the correspondency mapping between
[763] um the units of our model and the
[765] neurons in the brain that we've measured
[767] or the the voxil or the response
[769] channels that we've measured. And
[771] because of the commonics, this is
[773] actually not uh an easy problem to
[777] estimate this correspondency or often
[779] it's estimated as a linear mapping, but
[781] there are lots of parameters to estimate
[784] and you need a lot of additional data
[786] just to solve this kind of practical
[788] problem. We we've developed a particular
[791] approach to this that um I call
[793] representational similarity analysis
[796] where for each particular uh stimulus we
[798] measure response pattern in a region of
[801] interest. So you could think of this as
[803] um a little ROI and fMRI and these would
[806] be the voxels and then for another
[809] particular image we have um another
[812] pattern of activity here. So this is the
[814] same little region, the same response
[816] channels measured twice, but the
[818] activity pattern is different as you see
[820] from the the colors. And then um we
[823] compute the dissimilarity between these
[826] uh activity patterns which you could
[829] also think of as a distance in the
[831] representational space in which these
[834] patterns are points that correspond to
[836] the stimuli. We enter that dissimilarity
[839] into a matrix. So here in this matrix
[842] you can look up for each pair of stimuli
[844] how dissimilar the two stimuli are in
[846] the representation. We inter interpret
[849] these patterns as representations. So we
[852] interpret these dissimilarities as
[854] representational
[855] dissimilarities and um this matrix is
[858] symmetric about a diagonal of zeros and
[860] it gives us uh a characterization of the
[863] nature of the representation in this
[865] brain region. And then we can look at
[867] how this um representational uh space
[871] changes across uh uh different areas of
[874] the brain stages of computation. So here
[877] the the color now encodes the
[880] dissimilarity. Importantly this makes it
[883] straightforward to compare a brain
[886] representation to a representation in a
[888] computational model where we can take
[890] exactly the same approach. Take the
[892] pattern across all the units for each of
[894] the stimuli. um compare these patterns
[896] by some similarity measure or distance.
[900] It could be one minus the correlation.
[902] It could be the uklidian distance or the
[904] Mahalanobus
[907] distance. And then it's possible to
[909] directly compare these what we call
[912] representational geometries by
[914] correlating these uh matrices. And this
[917] circumvents this correspondency problem
[919] that we have at the level of the the
[921] units.
[925] So these matrices are called RDMs or
[928] representational dissimilarity matrices.
[930] So here in 2008 we took this approach to
[933] compare representations between human
[935] inferior temporal cortex and monkey
[938] inferior temporal cortex. It cortex is
[941] the part of the brain where highle
[943] visual semantic uh representations are
[946] thought to reside. And you see that um
[949] here I've I've colorcoded the
[951] representational distances from with
[953] these cold colors corresponding to small
[956] distances, these warm colors
[958] corresponding to large distances. You
[960] see immediately that there is a strong
[962] categorical uh structure um where all
[966] the human faces here you see our image
[968] set of 92 isolated object images. When
[971] when we compare in this representation a
[974] human face to another human face,
[975] they're always very similar. So you get
[977] this tight cluster here. When you
[979] compare an animal face to another animal
[982] face, they're also very similar. The
[984] animal faces actually are all different
[985] species, different colors. They look in
[988] different directions. Um so this is uh
[992] sort of intuitively not obviously
[994] related to visual uh similarity. And
[997] then there's this this off diagonal
[999] square here which is also blue which
[1001] corresponds to all the comparisons
[1003] between a human face and an animal face.
[1005] So this shows that there's sort of a
[1007] single face cluster and all of this is
[1009] within a larger animal cluster and then
[1012] there's also a cluster of inanimates
[1015] within which the natural and artificial
[1017] objects are not really clustering
[1020] further and the largest dissimilarities
[1023] obtained for when you compare an animate
[1025] to an inanimate object.
[1028] So all of these qualitative features of
[1030] this matrix very simple uh very similar
[1033] in the monkey it matrix and actually
[1035] also the within category
[1037] representational geometry was very very
[1039] similar in the monkey. So we analyzed
[1041] this quantitatively in this paper but
[1043] this is not what I'm going to talk about
[1045] today. Um so after this paper this paper
[1049] kind of posed the computational um
[1051] challenge to us. Importantly I I should
[1054] have said this human IT matrix was
[1056] estimated from fri voxil with um 2 mm
[1059] isotropic resolution and the monkey IT
[1062] matrix was estimated from cell
[1065] recordings. Um so despite these uh
[1068] really fundamentally different ways of
[1071] uh measuring these
[1073] representations um taking samples of the
[1076] dimensions of these representational uh
[1079] spaces we get uh in this case a rather
[1082] similar result and that was very
[1084] encouraging to us but it's also
[1086] problematic and we shouldn't uh in
[1089] general count on that. That's an
[1090] interesting topic for discussion and a
[1092] methodological challenge here. these
[1094] were very very similar. So um this
[1098] finding um posed the challenge to us can
[1101] we explain this representation with a
[1103] computational model. So we want a model
[1106] that um we train in some way and we can
[1110] use knowledge about the world. We can
[1112] use brain data but we can't use these
[1114] particular images and we can't use these
[1116] brain data. And then we want to predict
[1119] the this representational
[1121] uh uh space uh with a computational
[1125] model and that would be a candidate for
[1127] the computational mechanism leading up
[1129] to this representation in the brain.
[1133] So when we started this um this was the
[1136] PhD project of my great graduate student
[1140] Seyad Khalik Rasavi who's now at
[1143] MIT and this was in 2010. In 2010
[1148] inferior temporal cortex was a
[1150] computational mystery. So no one had a a
[1153] computational model that could really
[1155] predict either single cell responses to
[1157] arbitrary images or representational
[1160] geometries.
[1162] And at the time, computer vision was
[1164] most successful when using handgineered
[1167] visual features as inputs to shallow uh
[1171] machine learning classifiers. So neural
[1174] networks had been around for a long
[1176] time, but they didn't really work very
[1178] well for for computer vision. So we just
[1181] um you know were aware had been aware of
[1183] this this problem that we don't have any
[1186] um compelling computational model for it
[1188] for a long time. So we just wanted
[1190] something that could do the job and we
[1192] weren't picky about biological
[1195] plausibility because we thought let's f
[1197] let's have something let's see if we can
[1199] predict these representations at all and
[1201] then in a second step we can worry about
[1204] how that might be implemented with
[1206] biological neurons. So, we assembled
[1209] these 27 computational vision models
[1212] that spanned the gamut from models
[1214] motivated by brain theory to computer
[1217] vision
[1218] models. And I'm not going to um read
[1221] them all for you. Um some of you may
[1223] recognize a few of these names. So, they
[1226] included simple image representations.
[1228] Um your favorite handgineered computer
[1231] vision features like sift and fog and
[1234] gist. Most of them were untrained.
[1237] um some of them were trained in an
[1239] unsupervised uh framework. So they uh so
[1242] natural images had been used to uh
[1245] construct these features but no category
[1248] labels and two of them also were trained
[1250] in a supervised framework to some
[1254] extent. So how
[1257] similar are the model representations to
[1260] it? So what I'm going to plot here on
[1263] the vertical is the RDM correlation with
[1265] human IT. So that's the representational
[1268] dissimilarity matrix correlation of each
[1271] of the models with humanity. So it's a
[1273] measure of how similar these
[1275] representational spaces are. Um here the
[1278] gray bar is the noise ceiling. So that's
[1281] an estimate of the um range within which
[1284] we expect the true model to fall given
[1288] the noise in the data and the
[1289] variability across subjects.
[1292] So when we look at the result, we see
[1294] that um almost all of the models explain
[1298] significant variance in these
[1300] representational distance matrices. Um
[1304] however, they're all very far from this
[1306] noise ceiling. Um so they don't really
[1309] fully explain the structure in our data
[1311] at all. So our conclusion from this was
[1314] that all 27 models fail to explain it.
[1318] and we were getting ready for uh writing
[1321] this up as a somewhat depressing uh
[1323] paper but you know what can you
[1328] do? So the models um failed however each
[1332] model explained um significant variance
[1335] in the representation. So a question
[1338] that uh we wanted to address was can
[1341] weighted combinations of these features
[1343] explain the it representation because
[1346] when you uh distort when you
[1349] scale the axes of the representation or
[1352] linearly remix the features of course
[1354] you change the representational distance
[1357] matrices a lot. So it could be that we
[1360] have all the right nonlinearities
[1361] present in the set. However, we have to
[1365] uh do this sort of trivial linear
[1367] transform on top of it in order to
[1369] explain it. So what we did was we um
[1373] fitted these features to it um using
[1377] remixing and reweing. Remixing involved
[1380] fitting three support vector machine
[1382] discriminants for the major categorical
[1384] divisions that are prominent in it. So
[1386] those are animate inanimate face
[1388] non-face and body non-body to accentuate
[1392] these. And then uh we used non- negative
[1395] least squares to to fit one weight for
[1398] each of the models and one weight for
[1400] each of these SVM discriminants to
[1402] estimate a mixture that would best
[1404] explain uh the it representational
[1407] geometry and this was cross validated
[1409] across images so that we wouldn't
[1411] overfit to to our image set. So when we
[1414] did this, this is the matrix that we
[1416] obtained. You see that it gets this
[1418] little blue square right here. This is
[1420] the tight cluster of human faces which
[1423] are all frontal images and visually very
[1425] similar. But it doesn't really get any
[1427] of the other structure. It doesn't get
[1429] the the animal face cluster because the
[1431] the presumably because the the animal
[1434] faces are all different species and
[1436] different views and angles and colors.
[1439] it doesn't get the um animate cluster or
[1442] the inanimate cluster and here for
[1444] comparison you have the human IT and the
[1446] monkey it matrix again so this um
[1449] approach really didn't work even with uh
[1451] linear remixing and reweing of the
[1454] features so then something very um
[1457] significant happened in 2012 in computer
[1461] vision a deep neural network trained by
[1463] back propagation uh improved the
[1466] state-of-the-art and machine visual
[1467] object recognition by a large margin. It
[1470] won the imageet competition where
[1472] computer vision scientists submit their
[1475] algorithms and then their algorithms are
[1478] tested on image sets that uh they didn't
[1481] have access to before. So there's no way
[1483] of cheating. So this is a very good way
[1485] of really establishing um how how well
[1488] different computer vision systems do at
[1491] object recognition. So this was sort of
[1493] a sudden win and uh convinced many in
[1496] the computer vision uh community that
[1499] neural networks were the way to go. And
[1502] since 2012, this competition, as far as
[1504] I know, has never been won by uh any
[1507] system that wasn't uh a deep neural
[1510] network. So for us, of course, this was
[1513] uh super exciting. for one thing, just
[1515] because of the the computational advance
[1518] of being able to do vision uh much
[1521] better suddenly. And the the other
[1523] reason, of course, was these are the
[1525] kinds of models that are inspired by
[1528] brain science. They're much more uh
[1530] biologically plausible than the the
[1532] models that we had been testing before
[1534] as a kind of computational compromise.
[1539] So I just want to give you a little bit
[1541] um more context on artificial neural
[1543] networks. Um you might be wondering uh
[1546] this term has been around so long.
[1548] What's what's new now about this? Right?
[1550] In the 80s we were excited about this
[1552] and then somehow we forgot about them
[1554] again. Um
[1556] so what what is the uh history of neural
[1560] networks? They have a long history um
[1563] roughly co-extensive with the history of
[1566] modern computing I would say. Um in the
[1569] 40s we had mccull and pitz binary
[1571] threshold units in the 60s Rosenblat
[1574] Minsky and papers perceptron research.
[1577] Um in the 80s they uh caused a big
[1581] paradigm shift in cognitive science led
[1583] by Jay Mlelen who's in the the audience
[1586] uh over there um and really transformed
[1590] cognitive science in this this
[1593] period. However, in the
[1596] '9s people lost faith with neural
[1599] networks a little bit. So in computer
[1601] science uh people lost faith uh for two
[1604] reasons. The first was that they didn't
[1608] really
[1609] perform very well on real world problems
[1612] including object recognition. Other
[1614] methods these handgineered features beat
[1617] them and they were very hard to
[1619] theoretically analyze. So people also
[1621] felt that it's it's sort of uh
[1623] impossible to get uh rigorous
[1626] theoretical results. So that made them
[1628] less attractive.
[1632] However, more recently, there have been
[1634] breakthroughs with deep learning brought
[1636] about by a smaller community of
[1639] researchers who who kept at it in the
[1641] meantime. Um, the three most famous are
[1644] probably Jeff Hinton, uh, Joshua Benjio
[1647] and Yan Lun who developed pre-training
[1649] and regularization techniques that
[1651] enabled efficient learning of deep
[1653] networks in the early 2000s. And in the
[1657] last five years with growing computing
[1659] power and large labeled data sets via
[1662] the web available um these networks have
[1665] really uh come into their own because
[1668] now we have the the amounts of world
[1670] knowledge that they need to to soak up
[1672] in order to to really work.
[1678] So just in a nutshell, a unit in a
[1680] network of this type computes a linear
[1682] combination of its input and sends it
[1686] through a static nonlinearity which can
[1689] uh take a number of different forms. It
[1691] can be a sigmoid. It can be simply a
[1695] threshold or a very uh popular model is
[1698] the rectified uh linear nonlinearity
[1701] where um the pre-activation is just
[1704] passed through if it's positive and
[1706] otherwise the unit outputs are
[1709] zero. These simple units are then linked
[1713] up in different configurations. Here you
[1715] have a shallow feed forward network with
[1717] a single hidden layer. Here's a deep
[1719] feed forward network um with two hidden
[1721] layers in this case. More loosely deep
[1724] means that the network has lots of
[1726] hidden layers. So it has lots of uh
[1729] stages of
[1731] nonlinear transformation which allow it
[1734] to uh learn more abstract
[1737] representations of the input and this
[1739] seems to be a key feature of these
[1740] networks that allow them to perform well
[1743] and generalize well.
[1746] They can also be linked up recurrently.
[1749] So when the connections form cycles, um,
[1752] these networks produce dynamics
[1755] naturally and lend themselves to
[1757] modeling sequences such as speech sound,
[1760] convert speech sound to text, uh,
[1763] translate texts and convert text to to
[1767] speech as well.
[1773] So in computer vision the kinds of
[1776] networks that are dominant at the moment
[1779] are deep convolutional feed forward
[1781] networks. So these have a couple of
[1783] additional features that I just want to
[1785] briefly introduce you to. So they take
[1788] an input image and then uh in the first
[1791] layer
[1793] uh compute a convolution of the input
[1796] image with a little weight template. So
[1800] um there's two decisions there that um
[1803] are inspired by the visual hierarchy.
[1805] The first is that not all the possible
[1808] projections to this one unit in the
[1810] first layer here are present but there's
[1813] this local receptive field. So lots of
[1815] units are just by definition zero and
[1817] that this greatly reduces the number of
[1819] weights that have have to be learned. So
[1822] this makes it easier to train these
[1823] models. And the other um decision is to
[1828] say that um in a given map you in the
[1832] first layer you have a retinotopic map.
[1835] So this is inspired by the visual system
[1838] where the same feature is detected all
[1841] over the the image and this is
[1843] equivalent to computing a convolution of
[1846] this little weight template um with the
[1849] image and that would give you this uh
[1852] pre-activation for the the first layer
[1854] for a single feature. You see that this
[1857] feature looks like a gabbor. It's
[1858] actually not a gabbor. Um it's similar
[1861] to Gabbor, but it's um a weight template
[1864] that's been learned by this network uh
[1867] during its training to categorize
[1870] objects. So this was a deep network. It
[1872] was trained just to categorize objects,
[1874] but in the first layer, it ends up
[1876] learning these gabbor like features very
[1879] much consistent with what we see in
[1881] biological um vision. So it kind of
[1884] rediscovers this.
[1887] So for a number of it learns a number of
[1889] different features here just three shown
[1892] but it it could be uh perhaps a hundred
[1894] of these or or more that it learns just
[1897] in the first layer. This convolution is
[1899] followed by a nonlinearity. Um typically
[1903] there's a stage of pooling local
[1905] pooling. Um for example taking the local
[1908] max or the local average and then
[1911] there's usually uh local normalization
[1914] and all of this together is called a
[1916] single layer and then this process is
[1918] repeated with the parameters changing
[1921] and the receptive uh fields becoming uh
[1924] larger and larger with respect to the
[1926] original image space. So um networks
[1930] typically will have five to 20 layers.
[1932] Now there are many that have more than
[1934] 20 layers
[1936] actually. So here's the architecture in
[1939] crees at all's network which uh
[1941] convinced so many people in computer
[1943] vision that this was the way to go for
[1945] computer vision. This network was
[1948] supervised with 1.2 million category
[1950] labeled images, 1,000 categories.
[1954] This set included lots of dogs. Uh I
[1957] think 120 dog species. Uh I know about
[1961] two of them I think. Um and this if if
[1964] you see uh these these deep dream images
[1967] from Google, people are playing around
[1969] with this a lot and it's very very
[1970] inspiring. You often see dogs and um you
[1973] know this is the reason for it.
[1977] The network has been trained with
[1979] stochastic gradient descent back
[1982] propagation. It uses dropout
[1984] regularization in the final fully
[1986] connected uh
[1988] layers and it's got 60 million
[1991] parameters and 650,000 neurons in total.
[1995] So a lot of parameters despite these
[1997] ways of regularizing it having these um
[2000] local receptive fields and the weight
[2002] sharing um in the convolutional
[2008] layers. So how does how do the layers of
[2011] this network do at explaining the
[2014] representational geometry in
[2018] it? So here as before I'm going to um
[2020] plot the accuracy of the human IT
[2022] dissimilarity matrix prediction. So this
[2025] is the the same as before. I should have
[2026] labeled this axis the same way. So this
[2029] is the RDM correlation averaged across
[2032] our
[2033] subjects. Um so in layer one we get a
[2036] very small correlation with the human IT
[2039] matrix. However, it is a significant
[2041] correlation. So there's some variance
[2044] explained there which really just means
[2046] that this representation and human IT
[2048] both contain visual information. It
[2050] really doesn't tell you much more than
[2052] this to get a significant result
[2056] here. So here's the noise ceiling. So we
[2059] also see that the the performance of
[2060] this model is really far from the noise
[2062] ceiling. So this is not a good model for
[2066] it. As we go up the layers, this
[2070] correlation rises further and further.
[2072] And at layer
[2075] 7, which is the penultimate layer of
[2078] this network, we're really close to the
[2079] noise ceiling. So, we were um really
[2081] excited to to see that we can get this
[2084] close to it. So, the deep net almost
[2087] reached the noise
[2088] ceiling, but not quite. So, again, we
[2092] asked um can weighted combinations of
[2094] its units fully explain the IT
[2096] representation. So we just played the
[2098] exactly the same game that we played
[2100] with the
[2102] um computer vision models that we tested
[2105] earlier. Um we remixed the features
[2108] using the same three SVM discriminants
[2110] and we reweed the the
[2113] representations and the SVM discriminant
[2115] outputs using non-gative least squares
[2119] and this is the matrix that we got. So
[2122] this is the first time that we saw
[2124] actually sort of an a model that can
[2126] explain this uh uh structure that we'
[2129] struggled with for a number of years. So
[2132] here again for comparison is the human
[2134] IT and the monkey IT matrix and we see
[2136] that qualitatively um these are very
[2139] similar. Now they um have all the same
[2141] categorical divisions and also within
[2144] categories a very similar um
[2146] dissimilarity structure. So when we
[2149] looked at this this model, we really
[2150] reached into the the noise ceiling. Um,
[2153] and I was very excited about the fact
[2156] that I can now um get rid of this old
[2159] data set that I've been uh analyzing for
[2161] so many years because we're at the point
[2164] now where um we have a model that
[2166] explains this data set. So in order to
[2169] highlight the remaining shortcomings of
[2171] which uh I think there are many of this
[2173] model um we need better data. We need
[2176] more data.
[2180] So this model performed significantly
[2182] better than than all of the other
[2184] models. So we can now capture the
[2187] computations of the vententral stream to
[2190] some extent at least of vision at a
[2192] glance. The feed forward component of uh
[2195] the vententral stream. So that's very
[2197] exciting I think. However, we're
[2201] capturing these computations in a very
[2203] big net. there are so many parameters uh
[2206] we don't really know how this network uh
[2209] achieves this right so we still need to
[2211] find the computations in the map in the
[2214] net but we're in a much better position
[2216] now of course because this network is
[2218] totally transparent to us it's sort of
[2220] like the dream situation for a
[2222] neurohysiologist where you can show as
[2224] many stimuli as you want and you have
[2227] full data about everything uh in the
[2230] network all the responses right so this
[2232] is really I think a very healthy
[2234] challenge for analysis because we always
[2237] feel we're limited by our crappy data.
[2240] Right now, here's when you're not
[2243] limited by your crappy data. It's still
[2246] not easy. You still have to think really
[2248] hard. What are you going to do when you
[2250] have the full information? And I think
[2252] the the very exciting uh circuit level
[2254] developments that that we're seeing um
[2257] actually make this a reality in terms of
[2258] measuring uh uh real brains. And there
[2261] we face a similar challenge. Uh now we
[2264] have all this information but how do we
[2266] make sense of it? How do we use it to to
[2268] test computational
[2271] theories? So I just want to show you
[2274] some other people's work um in the
[2277] direction of understanding better how
[2278] what these representations are in these
[2280] models. Um so one approach is to
[2283] visualize the internal features. So
[2286] here's an approach from Zyla and Fergus
[2289] called deconvolutional
[2291] networks and um in the first layer we
[2294] see these gabbor like features. So I'm
[2296] going to show you four selected units
[2300] and I'm going to show you a
[2301] visualization as a template as an image
[2304] template of what this unit does. And I,
[2309] you know, maybe you're already thinking
[2311] why that might be problematic, but um
[2314] hold your horses for a moment. Um so in
[2318] layer two, we see these slightly more
[2320] complicated features of like curved
[2322] segments and more complicated patterns.
[2325] In layer three, we start seeing parts of
[2327] objects emerging. In layer four, we see
[2330] uh detectors for full objects. And in
[2334] layer five uh similarly it it looks as
[2337] though there might be detectors there
[2338] for full full
[2341] objects. Now a problem with this is that
[2344] fundamentally um the reason why these
[2348] networks can do vision is because they
[2350] don't do template matching in the image.
[2353] Template matching is fundamentally a
[2355] shallow computational uh process. It's
[2359] everyone's favorite way to uh imagine
[2363] vision and computer vision has shown
[2366] over and over again that it doesn't work
[2367] at
[2370] all. Uh so the way that this works is
[2373] for a given unit you look for an image
[2376] that drives this unit strongly and then
[2379] you look for the direction in image
[2381] space along which the unit's response
[2384] rises most steeply. So this is sort of a
[2386] different im. So there's a an image that
[2388] drove this unit strongly and uh this is
[2392] the changes to the pixels that you would
[2394] have to make to drive that unit even
[2396] more strongly. So this is a particular
[2397] dog but the same unit might respond to
[2400] many other dogs. Usually the same
[2402] category interestingly but it could also
[2404] from this you can't see it also responds
[2406] to totally different categories. So take
[2408] this with a grain of salt, but it gives
[2410] us perhaps an idea of the the complexity
[2413] of these um uh
[2417] representations. Here's another exciting
[2419] piece of work from Matias Bka's lab
[2422] using a network from Andrew Zeissman's
[2424] lab. Um they
[2426] uh designed a network that separates
[2429] content and style in images. So this is
[2433] available on archive. It's not published
[2435] yet actually.
[2436] And by separating out these two
[2439] elements, they can synthesize images
[2442] which they optimize to match these
[2445] internal representations of the content
[2447] and the style to create these uh new
[2451] composite images that combine the
[2453] content of one image with the style of
[2455] another image. And they did this for
[2456] using photographs for the content and
[2459] then uh paintings for the style. And you
[2461] get these very beautiful uh renderings
[2464] as paintings of these photographs and
[2466] some of them are re really striking and
[2469] uh you know I find this extremely uh
[2472] inspiring and it it really gives us an
[2475] idea of uh the complexity of these
[2477] models. Again the interpretation is not
[2480] straightforward. So this is sort of just
[2482] uh something we're struggling with at
[2484] the moment.
[2486] In the last two minutes, I want to tell
[2488] you quickly about um predicting
[2490] categorization reaction time for
[2492] particular objects. I've told you in the
[2494] beginning we need to also predict
[2496] behavioral measures. Um so one approach
[2499] to this is to think of categorization.
[2503] Um, when you're getting ready for a
[2504] categorization task like animate
[2506] inanimate, you're setting up this
[2508] internal readout filter from this rich
[2511] object representation in inferior
[2514] temporal cortex that gives you the the
[2516] optimal evidence for uh the object being
[2520] an animate object. And we modeled this
[2523] using the representational uh space in
[2526] the panel ultimate layer of this this
[2528] deep neural network from caches by
[2530] fitting a support vector machine
[2532] discriminant. So we get a decision
[2534] boundary in this deep nets uh
[2537] representational space and we get a
[2539] decision value for each particular image
[2542] and then some images are going to be
[2544] further away from the decision boundary
[2546] than other images and uh we predict that
[2550] for these images the the evidence toward
[2553] this being inanimate will accumulate
[2556] more rapidly and the reaction time will
[2558] be uh smaller. So here I'm plotting the
[2562] uh deep net's decision
[2565] value versus the human reaction time and
[2568] the decision boundary is here. So when
[2571] we look at the images, we see that those
[2573] images that are further away from the
[2576] decision boundary are actually
[2577] associated with smaller reaction times
[2580] in humans. So yeah, I've just colorcoded
[2582] this and this is um highly significant.
[2585] So we're looking at this um
[2587] systematically now for different readout
[2589] models and different categorical
[2591] divisions and we are interested in in
[2593] using this framework to to have some
[2596] model of the the behavioral readout as
[2599] well. So where are we now with this deep
[2602] neural network framework? Well, there's
[2604] an emerging body of work using deep nets
[2607] to explain biological vision. In 2014,
[2611] um the first three papers um came out
[2614] that attempted this.
[2617] Uh as I've said before, Dan Yammens is
[2620] an important proponent of this approach.
[2622] Um also Jim D. Kalo's uh lab uh Charles
[2627] Kadur has contributed to this. This year
[2630] another paper from Marcel Fungavan's lab
[2633] came out showing that mid-level vision
[2635] is well explained by these networks as
[2637] well. And there's a number of uh
[2639] preprints in circulation on new
[2642] developments including the work from
[2644] Matias Bedka's lab that I've shown
[2646] you. So are these deep neural nets like
[2651] brains? Well, yes they are. They're
[2653] directly inspired by brains. All
[2655] operations are biologically plausible.
[2658] um they have written topic maps of
[2660] features of increasing complexity
[2662] stage-wise uh transformations and they
[2665] explain representational spaces as I've
[2667] shown you but of course at the same time
[2669] also no there they have no recurrent
[2671] signal flow they uh uh have no spiking
[2675] they have no biologically justified
[2677] neuron types all this biological detail
[2680] is missing and the list list is
[2682] indefinite of course right so is a model
[2684] wrong for abstracting from a certain
[2686] feature of neurobiology ology I would
[2688] say only if the feature is needed to
[2691] explain brain
[2692] computations and so I think that's an
[2694] empirical question exactly which details
[2698] we need I think it's desirable to make
[2700] bold abstractions from biological
[2703] reality in this this undertaking so
[2706] what's missing at the moment one key
[2708] thing that's missing is recurrent
[2709] dynamics spatiotemporal prediction
[2711] attention probabilistic representation
[2714] another is learning and development
[2717] other visual ual functions beyond mere
[2719] category level recognition and exploring
[2722] predicting a richer array of behavioral
[2725] measures, categorization errors,
[2726] estimation errors, sensory motor
[2729] dynamics. But the point for me is that
[2732] the recent advances provide us with the
[2734] technological basis for taking the the
[2737] rich set of ideas that's in the
[2739] literature and making functioning fully
[2742] explicit models that actually perform
[2745] feats of intelligence. So in conclusion,
[2748] deep neural nets are biologically
[2750] plausible artificial systems that can
[2753] perform vision and other feats of
[2754] intelligence under real world
[2756] conditions.
[2758] They explain low to high level visual
[2761] representations of arbitrary natural
[2763] images and also predict categorization
[2765] reaction times for particular individual
[2769] images. So overall deep neural nets I
[2772] hope I've convinced you are biologically
[2775] plausible models that can perform these
[2777] real world fields of intelligence and I
[2779] think they're poised to explain the
[2781] brain computations that underly
[2783] perception, cognition and action. Thank
[2785] you very much.
[2791] Did you feel the pressure when I stood
[2792] up there? We We have time for just one
[2795] question and um we'll take Daniel
[2798] Fisher. Okay. I have very loud. I have
[2800] to wait for the microphone. The
[2802] microphone's right behind you. Okay.
[2805] Okay. So I I guess I had a um a worry
[2808] about the sort of metric that you're
[2810] using for how well you're doing
[2812] explaining the okay the data in at it
[2814] and then you sort of use that and then
[2816] start looking at your the data coming
[2818] from these deep uh deep networks and it
[2821] I worry that that's rather similar to if
[2823] one looked at playing chess where at low
[2825] levels what you look at first on a board
[2827] and what a computer looks at first on
[2829] the board are pretty similar and does
[2831] extremely well the computer at
[2832] predicting what move a person will do
[2835] But it does plays chess completely
[2837] differently by the time you get to
[2838] higher levels. And so I would sort of
[2840] worry whether that in some sense is
[2841] going on here as well. The the low
[2843] levels it is similar but the the level
[2845] the similarity in levels above that is
[2848] not exactly superficial but is is is
[2850] somewhat misleading. I wonder what you
[2852] mean by low level. Do you mean the
[2854] categorical distinctions versus within
[2856] categories? No. threaten the topic and
[2857] looking at the features that come in the
[2859] lower levels um uh of those which you
[2862] know clearly look by look biological but
[2864] at the higher levels we don't know what
[2865] the biological features look like right
[2867] we don't know um except make perhaps on
[2869] these very coarse fMRI scale um uh
[2872] images so it looks from the evidence so
[2875] far that these networks explain
[2877] representational geometries across
[2879] layers also in it right but you feel
[2882] that because of the way that we compare
[2884] the representational geometries It's a
[2886] question what you mean by explaining
[2887] them. You choose a particular metric and
[2889] particular metrics and say one explains
[2891] that and it's it's not it's not clear
[2893] how connected that metric is to what the
[2896] actual comparison of how they're how
[2897] they're doing things. And I was saying
[2899] that maybe analogous to saying okay you
[2901] can predict the next move someone is
[2902] going to do on a chessboard.
[2905] Yeah. So I mean it's it's really
[2906] interesting to think about how to
[2908] compare representational geometries.
[2910] Another approach that's widespread and
[2912] that I like very much as well is to fit
[2915] linear models to predict the response of
[2918] each response channel um to each of the
[2921] images. That's an alternative um method
[2924] and it's also a very good method. It
[2926] requires this additional very big data
[2928] set for just fitting this linear uh
[2931] mapping and then a separate validation
[2933] data set for evaluating the responses.
[2936] um what you're throwing away by looking
[2939] at the distance matrices is the uh
[2942] rotation of this uh arrangement in the
[2945] highdimensional space um and and any
[2948] shifts, right? And so the in intuition
[2951] behind this approach is that these are
[2954] just linear transformations that are
[2956] computationally trivial and that we want
[2958] to abstract from these in order to see
[2961] the the forest uh instead of the trees.
[2965] Um but you know I'd love to discuss this
[2968] with you in more detail to understand
[2970] more what your and let me follow that
[2973] thought up. We we are lucky you will be
[2974] here tomorrow. I will be and uh for
[2977] example you could join us for lunch and
[2980] you can all join us for lunch. Bill it's
[2982] on Bill. Thank you very much.
[2986] For more please visit us at
[2988] stanford.edu.
