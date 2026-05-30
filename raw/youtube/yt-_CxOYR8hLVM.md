---
schema_version: 1
id: yt-_CxOYR8hLVM
type: youtube
title: 'NeuroHackademy 2021: Self-supervised approaches for neural decoding and alignment'
url: https://www.youtube.com/watch?v=_CxOYR8hLVM
authors:
- UW eScience Institute
ingested_at: '2026-05-30T20:02:03Z'
content_hash: sha256:65e130f1019ac74cd3d2a82c30b017519994ff3c2e843c9024a5b3330403eaa9
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: UW eScience Institute
  channel_url: https://www.youtube.com/@UWeScienceInstitute
  duration_seconds: 3417
  caption_track: fetched
  snippet_count: 1560
filter:
  score: 0.7
---
[0] so i will i'll start by introducing uh
[3] our next speaker
[4] eva dyer is in a
[7] neuroscientist and a data scientist at
[10] uh
[10] georgia tech memory university and i
[13] think
[14] something that i find really interesting
[16] and special about eva's work is that
[18] when you think about data science you
[19] think of that as being maybe in the
[21] intersection between
[23] fields maybe here in this case machine
[25] learning and neuroscience
[27] and it's often very hard to do cutting
[29] edge work that's both cutting
[31] you know at the cutting edge of machine
[32] learning and at the cutting edge of
[34] neuroscience and i think
[35] uh it was quite unique in the fact that
[38] whenever i hear her talk i see that it's
[41] really
[42] kind of pushing the boundaries on both
[43] of them at the same time
[45] um and so today she'll talk about
[48] self-supervised learning and take it
[51] away
[52] cool thanks so much for the invitation
[54] and
[55] um you know i've attended the neuro
[58] academy in the past when it's in person
[61] so
[62] it's a shame that we don't all get to
[64] you know join together
[66] um in person but um excited to you know
[70] still share this time with you all
[72] so what i'll talk about today
[76] is some recent work that we've been
[78] doing um
[79] as arya was saying you know we work at
[81] the interface of machine learning data
[84] science and neuroscience
[86] and in general we're interested in
[90] ways in which we can take information
[93] from the brain whether it be from
[94] individual neurons or
[96] maybe even through fmri or other signals
[99] you know measuring
[100] you know information and signals within
[102] the brain
[104] and be able to take those and boil them
[106] down into some sort of
[108] simplified or potentially interpretable
[111] representation of what's going on within
[113] the brain and
[114] if we can do a good job of forming those
[116] representations
[118] um in a way that's stable and sort of
[121] reliable
[122] then we can also potentially be able to
[124] decode information for the brain which
[126] can help in
[127] you know brain machine interfaces
[129] prosthetics and also
[130] um have a lens into how the brain is
[134] changing over the course of disease or
[136] aging or
[137] neurodegeneration which is an
[139] application that we're particularly
[141] interested in so
[142] um so what i'll talk about today
[145] hopefully
[145] okay let's see okay is um
[149] is ways in which we are trying to
[154] um you know think about new frameworks
[158] for forming these representations in an
[160] unsupervised way so meaning
[162] where we don't necessarily have labels
[164] that are driving our underlying um
[167] uh picture of what the activity looks
[171] like right
[172] so um before i jump into the actual
[176] project
[176] and the work that that i'll discuss
[178] today in self-supervised representation
[180] learning which i'll go into the details
[182] of
[184] uh i'll just quickly talk about the team
[188] that made all this happen
[189] and and introduce the folks both from
[191] our labs so over here
[193] on the left um the two projects i'll
[195] talk about today were mainly driven by
[197] midi and also ron
[199] in my lab and this is a an ongoing
[201] collaboration with folks at um washu and
[204] st
[204] louis keith hangen and his team
[208] and then also researchers at deepmind
[210] including mohamed azar and michelle
[212] valko
[214] and kind of bringing all of these you
[216] know with these very large
[218] projects we need a lot of a lot of
[220] different minds and a lot of different
[222] um expertise and insights to really
[224] bring these large projects together
[226] so these are these are the folks that
[229] have made this work possible
[231] so as i sort of alluded to at the
[234] beginning
[235] um when looking at pictures
[238] of what the brain is doing oftentimes we
[241] can
[242] you know we have access to labels or
[244] information about behavior that we might
[246] want to relate to the brain so
[248] traditional approaches for supervised
[250] decoding have often
[252] you know take those behavioral labels
[254] and try to find a mapping between brain
[255] activity
[256] and you know the outputs of the brain so
[258] if we're talking about movement
[260] you know predicting a reach or where in
[263] space we intend to make a movement
[265] towards
[266] or if it's in visual representations you
[269] know what are we actually looking at
[270] right like what are the
[272] what are the inputs coming in so um if
[274] we have
[275] a label to associate with data
[278] and we can form a supervised mapping
[281] between the two
[282] that gives us a way of reading out
[284] information but obviously we know that
[285] there's probably a lot of other stuff
[287] that's really going on
[288] under the hood right and so being able
[290] to
[291] form a representation of activity
[294] without having specific labels to guide
[296] us could be
[297] a very powerful way of getting a lens
[299] into what's really going on in the brain
[301] so that sort of
[302] motivates this idea of unsupervised
[305] learning as a way forward in
[307] understanding what populations of
[310] neurons
[310] are doing potentially and sorry
[313] i should have had a few more intro
[315] slides here i'm realizing
[317] um but so in unsupervised learning often
[319] what we try to do is we try to take
[321] collections of data and essentially
[325] form some sort of generative model
[328] or a way of reconstructing or
[331] recapitulating images or samples that
[335] we've sort of
[336] we've learned from through whatever
[338] machine learning architecture
[340] system that we apply um
[343] and uh you know on one hand this is a
[346] good
[347] strategy because it gives us if we kind
[349] of constrain
[351] the dimensionality of our representation
[353] through this reconstruction process
[356] it can give us a way of finding the kind
[358] of core and essential features but
[360] in the end we're actually asking our
[362] system to still be able to reconstruct
[365] the full data right and so in some ways
[369] um because this isn't necessarily lossy
[373] we require to hold on to a lot of
[377] information that might not actually be
[379] relevant for
[380] a downstream inference or decoding task
[383] right through this sort of
[384] reconstruction
[386] framework or or thought process if you
[389] will or perspective
[390] so um in the machine
[394] learning community the emergence of
[397] these tools
[398] um in what's called self-supervised
[401] learning which is a form of unsupervised
[403] you know label-free learning have really
[406] started to take um
[408] or gain a lot of momentum in the field
[411] and
[412] these these methods are now starting to
[415] actually approach the performance of
[417] supervised
[418] methods in terms of their ability to
[420] solve complex
[422] um downstream tasks like image
[424] recognition on you know really large
[426] data sets like imagenet
[428] so uh the sort of origin of this project
[432] was just thinking about okay
[434] we know that these self-supervised
[436] methods are now
[437] providing really exciting new ways of
[440] getting a lens into
[442] data in machine learning and might we be
[445] able to leverage or sort of harness
[447] the tools in our ability
[450] to understand what the brain is doing as
[452] i motivated right forming these
[454] representations of neural activity but
[457] using these
[458] these new tools that move away from just
[460] this reconstruction based perspective
[463] okay so with that very long-winded intro
[468] now i'll go to this slide which is uh
[471] you know kind of digging into the
[472] principles underlying self-supervised
[475] learning
[476] and um you know this is a talk i'm i'm
[479] gonna talk about our work in this space
[481] but also this is meant to be a tutorial
[485] and so i know that there's a lot of
[487] different concepts that i'm kind of
[489] going through right now and feel free to
[491] stop me and ask questions to clarify
[495] things at any point
[496] just um you know because i hope that
[499] um you all will be able to take away
[501] some
[503] some new insights into this rather than
[505] it just being you know
[507] a huge brain dump okay so
[510] uh so what is self-supervised learning
[512] um there's a lot of different
[514] ways in which it's done but what i'll
[516] talk about today is a kind of subset of
[518] them that really rely
[520] on this idea of information maximization
[524] and this principle that essentially if i
[527] have a data point
[528] and i can create a transform it in some
[531] way to create a new view
[533] or a new
[536] visualization of it if you will um
[539] and and let's just say i can create
[541] these augmentations of the data
[543] such that the underlying semantics is
[546] preserved
[547] but maybe the pixels and like the you
[549] know the explicit
[551] encoding of that information could be
[553] very different across these different
[555] views so
[556] as i'm showing here you know i have a
[558] picture of a dog
[559] in my data set and um the idea would be
[563] to apply
[563] different transformations to that image
[566] that will still
[567] you know create another image of a dog
[570] but you know it's been zoomed it's been
[573] scaled
[574] um you know it's been rotated in this
[577] case you know you might
[578] imagine applying some cutout or masking
[581] of certain parts of the image
[584] um or even additive noise and
[587] essentially in all of these cases
[588] through all these augmentations we still
[591] have
[592] essentially captured the essence of dog
[594] right and so now what we're going to do
[596] is we're going to feed in
[597] all of these different augmentations of
[601] a sample
[601] into our network or into this you know
[605] deep learning architecture um that's
[607] essentially
[608] trying to maximize the similarity
[612] between
[612] all of these different transform views
[615] in the latent
[616] space of this architecture so
[618] essentially
[619] we'll create the approach you know at a
[621] high level is creating
[622] augmentation so these different views of
[625] a data point
[626] and then trying to learn a
[627] representation that's going to
[630] put these different augmentations in a
[631] similar part of the latent space
[633] or essentially maximize the similarity
[635] between them
[636] and the principles underlying this are
[639] related to
[642] as i said before kind of information
[643] maximization or
[645] finding some way where the mutual
[648] information
[649] between all these augmentations is sort
[651] of is maximized
[652] under this projection and so you can
[654] imagine that
[656] if i you know do a lot of really crazy
[659] things to this picture of a dog
[662] but build a representation that makes
[664] all of these very unique pictures of a
[666] dog
[667] essentially the same in the
[669] representation space
[671] then i will have built a very rich
[673] feature space that allows me to
[675] solve these sorts of image recognition
[678] problems in a really robust manner
[680] right and so really the principles here
[683] are
[684] using augmentations and this infomax
[687] sort of
[688] loss as a way of building it in
[691] variances
[692] into your into your network okay
[696] so um there are sort of two
[700] main classes or i guess the the first
[704] sort of instantiation of this idea of
[707] information maximization
[708] in this kind of instance specific manner
[712] um what is sort of you know
[715] broadly cast through through this net of
[718] what are called contrastive learning
[721] algorithms and essentially what they're
[723] doing
[724] is you take you know your sample you can
[726] take these different views of it so here
[728] we're taking the cat
[729] and kind of zooming in and cropping some
[731] new region in space
[733] and as i said before our goal is to
[735] basically pull
[737] these different you know images of a cat
[739] together they're the same example
[741] and so we know their label right we
[743] don't know that it's a cat but we know
[745] all these views are the same
[747] example right and then at the same time
[750] the loss function will have another sort
[753] of
[753] contrastive part to it that's going to
[756] also try to push apart
[759] other views of other examples that are
[762] generated from different samples in your
[764] data set right
[765] so in this case you know i have a cat
[769] and i have another picture of a dog but
[771] you could imagine having other pictures
[773] of cats
[774] that are going to serve as what are
[776] called negative examples and are going
[778] to be pushed apart
[779] under this loss function right all you
[782] know
[782] are the things that are from the same
[784] example and everything else is kind of
[786] considered
[787] a different instance or a different
[789] class in some sense
[792] so um so methods like simclear
[796] are an example of this contrastive
[799] learning framework
[800] and um and you know the
[804] these methods as i said before i've been
[806] kind of you know very
[807] quickly closing the gap on supervised um
[811] architectures that are trained
[812] end-to-end right where whereas in this
[815] case
[816] we train the network with this
[817] unsupervised loss without labels
[820] we freeze the network and then we just
[822] read out through a linear decoder
[825] information about the different classes
[826] so essentially you can you can
[829] use the network in a fully unsupervised
[831] way and then read out its
[832] representations to understand whether or
[834] not it's learned important aspects
[837] of the data that are indicative of this
[839] you know downstream
[841] in this case image recognition um and so
[846] as i said before there's this
[847] contrastive learning mechanism where you
[849] pull these together and you push these
[850] apart and then more recently there have
[852] been a number of methods
[854] introduced that essentially get rid of
[856] this
[857] explicit contrastive mechanism and
[860] really
[861] aim to just establish this sort of
[864] affinity
[865] or pulling of things together and then
[868] you can
[869] use different mechanisms to essentially
[871] ensure that
[872] um not everything gets pushed together
[874] within the latent space
[876] and so um so this method that
[879] sort of gets away or gets rid of these
[882] negative examples um that was
[885] you know recently introduced is called
[887] bile or bootstrap your own latent
[890] and um i i'm showing this picture here
[893] just to kind of
[894] show where we're at in terms of you know
[896] these complex
[897] image recognition task and how bile and
[900] now supervised methods are essentially
[903] at similar levels of performance okay
[907] and i'll just kind of go into the
[910] details of this
[912] i've already set it at a high level but
[914] just to kind of
[916] um give a little more of a
[920] detailed picture into what this um
[924] bootstrap your own layton algorithm is
[925] doing so as i described we have
[928] um some sample from our data set
[932] we have some class of augmentations that
[935] will apply to it that are stochastically
[937] sampled so we have different you know
[938] transformations that we can apply
[941] those will produce two different views
[944] of the same sample
[945] and essentially within these frameworks
[948] you you
[949] pass each of the views through
[952] a mirrored it's
[955] kind of complicated and we can i don't i
[958] don't want to go
[958] too much into all of the stuff under the
[961] hood but essentially
[963] you're you have these two networks they
[966] are
[967] almost they're exactly the same
[970] architecture and they're almost the same
[972] weights
[973] but they're um one of the one of the
[976] networks is like a slower
[979] version of the weights that are being
[981] updated in
[982] in the online network so essentially
[986] instead of back propagating all of your
[989] gradients through both of these networks
[991] you're only going to update
[992] one of the networks and then you're
[994] going to use those weights to then
[997] um produce like a momentum average
[1000] version of the previous weights of the
[1002] target and with
[1004] with a new update sorry that was a
[1006] little bit long-winded
[1007] um but needless to say it's sort of
[1010] drawn here so we have this online
[1012] network we have a target network
[1014] i'm d uh i'm denoting the encoder with
[1019] f theta here and as i said this isn't
[1021] exactly the same network
[1023] but it's going to be a kind of slowed
[1025] down version of this top one
[1027] we're going to pass this view through to
[1029] generate a representation
[1031] y below through this other view we'll
[1034] get some representation of the other
[1036] view called y
[1037] prime and then what we're going to do is
[1040] pass this through a very simple
[1041] predictor
[1042] that essentially is going to try to map
[1045] these different augmentations y and y
[1047] prime into a similar part of the latent
[1049] space and that's given by this loss
[1051] function here
[1052] which is just minimizing in this case
[1054] just an l2
[1056] distance or euclidean distance between
[1059] the prediction of y
[1060] and y prime so basically these two dual
[1063] networks are sort of
[1064] working together to give these different
[1067] augmentations or different views of a
[1069] sample
[1070] and then the predictor is trying to
[1072] solve this task
[1073] of bringing them together within the
[1075] latent space
[1077] and this sg is just denoting a stop
[1080] gradient so as i was saying we're
[1081] we're going to only um update the
[1084] weights in this network and then we're
[1086] going to stop the gradient from actually
[1088] going back into the second network and
[1090] and updating it okay so this is
[1093] we're sort of building on these dual
[1096] deep networks
[1097] and and this sort of approach for
[1099] information maximization and as i said
[1101] biol is trying to essentially find this
[1104] a minimization
[1106] of these different views in the latent
[1107] space using
[1109] a mechanism that looks like this or a
[1111] loss that looks like this
[1113] okay so with all of that sort of
[1117] background
[1118] on you know what is self-supervised
[1120] learning and what are these
[1122] what is the what are the principles
[1123] behind the these um
[1125] approaches um we can now dig into
[1129] how we went about applying this idea
[1132] now to neural activity or neural data
[1135] sets
[1135] which are you know the same ideas might
[1139] be applied to other types of neural data
[1140] but in this case
[1142] we were interested in in applying it to
[1146] spike sorted data where we have many
[1148] neurons
[1149] measured in in cortical or hippocampal
[1153] areas in this case
[1154] um but we have a population of neurons
[1156] that we're recording from over time
[1158] and we've bend and sorted and then
[1161] measured the firing rates from all of
[1163] those
[1164] all of those neurons within the recorded
[1166] population
[1167] okay so we have this data
[1171] we have many neurons that are firing
[1174] over time and we want to understand what
[1175] they're doing
[1176] right and so going back to our original
[1178] motivation of finding this
[1180] representation
[1181] and so the first question that we have
[1184] when
[1184] trying to use these self-supervised
[1187] learning techniques
[1188] is what kind of augmentation should we
[1190] use
[1191] um right because we saw as in um as an
[1194] image case in computer vision we have
[1197] very
[1198] strong domain expertise that can guide
[1202] us
[1203] into building transformations like
[1205] zooming and rescaling and
[1207] and cropping that will still guarantee
[1210] or
[1210] will still preserve the semantic content
[1213] with high probability
[1216] while still providing some you know
[1219] diversity in in what the actual
[1221] instantiation
[1223] of the sample is and so
[1226] um we first sort of started with this
[1230] idea
[1231] of um using nearby points in time
[1236] as a as a starting point for building
[1239] an augmentation for neural data and this
[1242] makes sense because you know
[1243] we can assume some sort of temporal
[1246] consistency in the world and in our
[1248] representations and so
[1250] if we were to look at you know a given
[1253] brain
[1253] state or firing rate pattern at some
[1256] point
[1257] in time given here by x so it's a vector
[1260] of firing rates over over d neurons
[1264] um then then one way to define an
[1266] augmentation would be to look at a
[1268] nearby point in time
[1270] and ask whether or not we can you know
[1272] you
[1273] essentially form a representation that
[1276] will
[1276] uh converge to some sort of temporally
[1279] consistent
[1281] inf uh representation right because if
[1284] we can put
[1285] nearby points in time into similar parts
[1287] of the latent space then this
[1289] should induce some sort of smoothness in
[1291] our representation
[1293] um and so yeah so our initial solution
[1298] was to essentially um use nearby time
[1301] points
[1302] as a as an augmentation to sort of seed
[1305] the learning and and and this operation
[1308] for
[1308] for our self-supervised loss function
[1312] um and it makes sense there's been a lot
[1313] of work in
[1315] predictive coding within neuroscience as
[1318] well showing that you know
[1319] the brain wants to build representations
[1322] where it can predict
[1324] new things that will happen right given
[1326] previous observations
[1328] um and so
[1331] you know on one hand this is a
[1334] reasonable solution but
[1336] on the other hand it it doesn't is it is
[1339] um
[1340] insufficient to actually build in
[1342] richness
[1343] into into the data sets that we've
[1346] tested thus far
[1347] and so what we found is taking it a step
[1350] further is actually introducing not only
[1353] not only this
[1354] jitter or sort of looking at nearby
[1357] points in time
[1358] but also removing or masking
[1361] certain neurons from the brain states
[1364] over which we want to predict
[1366] so this is kind of similar to that cut
[1368] out or masking example that we showed
[1370] before in images essentially what we'll
[1373] do
[1373] is we're going to you know take a brain
[1376] state
[1377] mass some set of neurons and then create
[1380] another augmentation of a nearby brain
[1383] state with using
[1384] some different subset of neurons so now
[1387] essentially the network is being asked
[1389] to figure out some way
[1391] of finding the things that are sort of
[1393] consistent across
[1394] different subsets of neurons within our
[1396] population
[1397] that essentially will you know build
[1400] some representation where these things
[1402] are nearby in the latent space so it
[1404] might feel
[1406] a little bizarre to start and i think
[1410] um in some sense there are a lot of
[1413] interesting questions that we can start
[1415] to ask
[1417] using these frameworks about like
[1420] if a type of augmentation works what
[1424] does it actually tell us about how the
[1426] information is being represented within
[1428] that population of neurons right
[1430] so if we have a distributed code
[1434] then it makes sense that if we drop out
[1436] subsets of neurons we could
[1437] we should still be able to um decode
[1440] similar pieces of
[1442] information even from a subset of that
[1443] population and we know that
[1445] when we go into the brain and we record
[1447] a different subset of neurons each time
[1450] um we can still decode these this
[1453] information
[1454] often and so it makes sense that having
[1456] some amount of
[1458] permutation invariants that might be
[1461] induced through this dropout operation
[1464] could actually be an important type of
[1467] implicit bias or regularization that
[1470] could be just useful for
[1472] neural networks applied to to neural
[1474] data in general
[1476] um there were a few
[1480] questions in slack i wonder oh yeah yeah
[1482] please while you're talking or do you
[1484] prefer we
[1485] yeah go ahead that would be great uh so
[1487] i think uh priya i had a few questions
[1489] come up for you you can um mute yourself
[1492] and ask
[1493] yeah hi thanks um this is really
[1495] interesting i'm really excited
[1497] but yeah i think i'm i'm kind of
[1499] circling around this issue of
[1501] how do you know that the augmentations
[1503] are i would put some quotes
[1505] realistic you know um
[1509] like thinking about the example of a dog
[1511] okay your
[1512] visual perceptor or your you know vision
[1515] machine whatever you could see a dog
[1517] from the left or from the right or
[1518] upside down
[1519] um but you could also see a dog you know
[1522] at an unusual angle or
[1524] head-on instead of um just kind of flat
[1527] like that
[1528] and kind of related it's like okay
[1531] so you're doing the augmentations by
[1533] dropping out neurons but
[1534] how many or which neurons can you drop
[1537] out and
[1537] how do you know that it's still actually
[1539] just a perturbation
[1541] or yeah an augmentation of this quote
[1543] same
[1544] state and that you you're not like
[1546] training on a different state now
[1549] yeah those are those are great oh was
[1551] that it sorry
[1552] yeah yeah okay um
[1556] those are great questions and it's
[1559] actually hard to like fit all of this
[1561] into the motivation right because it's
[1563] like there's so many things
[1565] to really unpack here um
[1568] so to answer your second question about
[1572] how do we know that we haven't you know
[1574] broken the semantics or
[1575] remove this information um
[1579] we we don't we don't fully know
[1584] but we can read out
[1587] information that has to do with the
[1589] behavior that we know is linked to these
[1591] neural recordings and ask whether or not
[1592] we can still decode these pieces of
[1594] information
[1595] right so i'll get into some examples um
[1598] two in particular one where we're
[1600] looking at um
[1602] macaques or non-human primates that are
[1604] carrying out a reaching task where we
[1606] know the underlying behavior
[1608] that neurons in the motor cortex are
[1610] representing right and so
[1613] if we can form a representation and then
[1615] from that
[1616] read out these different pieces of
[1618] information about the target location
[1620] and and decoding of of different reaches
[1623] then at least we know that we have a
[1627] representation that has some
[1630] meeting meaningful link to the behavior
[1632] that we know is related
[1634] but we don't yeah we don't necessarily
[1636] know that we haven't lost
[1637] other pieces of information that these
[1639] circuits might care about
[1641] with that being said you know when we
[1643] compare this to other unsupervised
[1645] representation learning systems like
[1647] they also suffer from similar issues
[1650] of losing information but they do it
[1653] through just like minimizing an l2 loss
[1655] and so you're not sure what you're
[1657] losing there either but it's
[1658] usually linked more to things that have
[1661] high variance right
[1663] and so in some ways we we could
[1666] we're using augmentations as a way of
[1669] like building in these invariances
[1672] to to get a picture into what the brain
[1674] is doing but yes there's not necessary
[1676] you know where
[1677] we can use this as a lens into into that
[1680] and then use
[1681] these different behavioral readouts as a
[1683] way to kind of see what we've
[1685] preserved and what we might have broken
[1689] in the data i guess if you will um so
[1692] hopefully that kind of gives you
[1693] um some answers to your question and
[1696] i'll get further in
[1697] and then the other thing that you asked
[1699] was how do you know if it's realistic
[1703] and so one thing that i'll say here is
[1706] that
[1707] while it's true that yeah there's all
[1710] these different ways that you could
[1711] imagine seeing a dog and many of them
[1713] you're never going to create
[1715] just through a transformation of that
[1717] dog right
[1718] but then there's also a lot of things
[1720] that people do in these cases to like
[1723] build in other invariances that actually
[1726] are generating things that you would
[1728] never expect to actually
[1730] see in nature so like a picture of a cut
[1732] out dog
[1734] is not really from the actual
[1736] distribution of the data
[1737] but but because it still has the dog in
[1740] it
[1741] and it's telling the network now to look
[1742] over like to build a representation that
[1745] doesn't take in the whole image but also
[1747] has to build
[1748] its inference from smaller parts
[1752] of the image right um in that sense
[1755] it's it's not realistic but it's still
[1758] helpful and i think maybe for similar
[1760] reasons
[1761] we find that dropping out of neurons
[1764] through this kind of
[1765] local property of coding if you will
[1768] could also be a reason why we get some
[1770] some nice properties from
[1772] from our system or from our um
[1776] from what we're doing here and
[1780] and i i see another i see another hand
[1784] up as well yeah yes
[1787] hi this is uh really interesting and
[1789] exciting
[1790] and and i probably come from uh quite of
[1793] uh
[1793] up opposite of a country perspective
[1797] as seeing this type of controlling
[1800] neurons
[1801] can can leading to a highly complex
[1803] state of modeling
[1805] so there are a lot of modeling and a
[1807] treating
[1808] the same set of data set so so what's
[1811] your thoughts on
[1813] now we fix the model and then fit as
[1816] many data as possible and this can can
[1819] can be a lot of
[1820] docs from lots of perspectives
[1823] as many as possible and see how that
[1826] fixed the model behave
[1827] towards that big data set so this might
[1830] be very different from
[1832] the modeling you are implementing now
[1834] but what's your thoughts about
[1836] that kind of uh perspective so i think
[1839] that i understand your question
[1842] and i i think actually what we
[1846] end up doing next is maybe
[1849] kind of moving in the direction that
[1851] you're talking about but i might need to
[1852] clarify your question
[1854] um so
[1858] or maybe okay so here i'll tell you what
[1860] we do next and then maybe you can tell
[1862] me if that answers to some extent some
[1864] of the questions that you had right
[1866] um so one of the things right is like
[1870] okay so i have this picture and if i
[1872] know good augmentations then i can
[1874] basically you know figure out how to
[1876] transform them all but i think what
[1878] you're saying
[1878] is i actually have a lot of images of
[1880] dogs
[1882] right i don't just have this image of a
[1885] dog
[1886] and so if there would be some way of
[1888] actually knowing
[1889] where the other dogs were i don't know
[1891] if this was your question but this is
[1893] where i was getting to
[1894] um yes yes actually
[1898] this is kind of mimic the the six
[1901] pictures that you have that the data are
[1905] not perfect right
[1906] there are incomplete space there so
[1909] i i mean imagine like data are so dirty
[1912] so
[1913] they are labeled oh i see i see yeah
[1915] yeah that's a different point but
[1917] um it's interesting because you can
[1919] imagine building an invariance
[1921] through these systems because you have a
[1924] lot of varied perspectives that you want
[1926] to be able to capture at test time right
[1929] which would be helpful here but then at
[1931] the same time you can also imagine
[1933] this self-supervised learning or
[1935] augmentation also being helpful for
[1939] avoiding nuisance variables or other
[1942] noise in your data that you don't want
[1944] to recapitulate
[1945] in your representation and so i think
[1947] what you're saying
[1948] is you could have noisy data and because
[1951] the noise isn't the same across all the
[1953] different
[1954] views or augmentations you could
[1957] you could also use this as a way of
[1959] helping with with that as well i think
[1961] and and see that particular model how
[1963] that behave
[1964] towards that kind of noise sense but i
[1967] think this is
[1967] very interesting we should explore both
[1970] from a modeling perspective and from
[1971] data perspective
[1973] yeah no it's uh there it's still kind of
[1976] unclear exactly where
[1979] all of because as i was saying there are
[1982] some cases where really
[1983] harsh and non-domain realistic
[1987] augmentations are best and other cases
[1990] where
[1990] you know having realistic generation of
[1994] of perspectives is is helpful um
[1997] so yeah likely those really
[2001] bizarre augmentations are probably
[2003] helpful in breaking noise and other
[2005] and other corruption in the data more so
[2008] than the
[2009] kind of generative modeling perspective
[2012] um but that sort of gets us to the
[2015] motivation
[2016] for um this new representation learning
[2020] approach
[2021] that we developed which is
[2025] which is kind of related to both of the
[2028] questions that we just discussed
[2029] which is that you know when i have
[2033] a large data set that is actually quite
[2037] rich and diverse why not try to find
[2040] other examples in my data set that i can
[2044] use as an
[2045] augmentation right and so
[2048] this idea that i talked about before
[2049] it's like okay i have a picture of a dog
[2051] and if i know how to
[2052] make another picture of a you know the
[2054] same dog still look different then i can
[2057] use this approach
[2058] but what if i could just find other
[2059] pictures of dogs and then try to build
[2061] a model that could learn to you know
[2064] predict across
[2065] all these different instantiation of
[2067] different dogs
[2068] and so we developed this idea
[2072] which we call mind your own view or meow
[2075] which essentially tries to
[2078] find augmentations that are just
[2081] different samples within the same data
[2083] set
[2083] and so essentially finding these links
[2086] across um different examples
[2089] as a way of forming these predictive
[2091] relationships
[2093] and so if we think about this in the
[2095] context of brain activity
[2097] if we were looking very locally before
[2100] over these you know nearby points in
[2102] time to form our augmentations
[2104] uh we're now asking
[2107] whether or not it's possible to go
[2109] outside of that you know kind of local
[2111] point or
[2113] view and um you know find
[2116] other brain states that might be similar
[2119] to what we're experiencing but not
[2120] might not be close to us in time and
[2124] some ideas of you know or motivations
[2127] behind this is like you know
[2128] we can imagine what a similar looking
[2131] dog would look like right or we can have
[2133] memories of what um this same dog
[2138] or maybe a dog from our childhood that
[2140] might have had the same color fur or
[2141] something right
[2142] so the brain is able to generate
[2147] um or make links between different
[2151] points in time that have similar
[2153] kind of representations of the state um
[2156] and then
[2156] and by forming those kind of you know
[2159] more long-range predictions we might be
[2161] able to have
[2162] a more rich representation space that
[2164] isn't so myopic
[2165] or sort of local right so that was the
[2168] sort of
[2168] um idea behind this approach for ssl
[2173] is to mine from within the data set to
[2175] find augmentations
[2177] and then use those as a way to enhance
[2180] um
[2180] self-supervised learning and so this is
[2183] the sort of
[2185] picture of um of this approach which we
[2188] call
[2188] mine your own view which builds on bile
[2192] the
[2192] the previous algorithm that i sort of
[2195] showed
[2195] and so it does it by um you know
[2198] essentially as i showed before we have
[2200] these two different dual networks
[2202] oh someone's crying or with joy then
[2205] maybe they liked meow
[2206] as a as an acronym um and there's
[2210] cats here so
[2214] um right so as we saw before we have
[2216] these dual networks we would normally
[2219] you know take an image produce these two
[2221] different views of it
[2223] pass it through the online and the
[2224] target network and then before we were
[2227] trying to just build this predictive
[2229] relationship between representations of
[2231] augmentations
[2232] and what we do now is go a step further
[2234] through this sort of secondary
[2236] and it's almost like a hierarchical
[2240] cascaded architecture right where you
[2242] have these more local things that you're
[2245] trying to predict
[2246] in the first stage and then you try to
[2248] use that representation and and go
[2250] across these more non-local or distant
[2253] parts within the representation space
[2256] and forming predictions across different
[2258] samples in this case
[2260] and so we um i have the loss function
[2262] here it's just combining this sort of
[2264] bio loss on augmentations plus this
[2267] other mining term
[2268] um and then this is just showing this
[2270] example of
[2272] basically to find those candidates or
[2275] sorry to find the the examples that will
[2278] link through this mining procedure
[2280] um in the end what we do is we basically
[2283] put candidate views or samples
[2285] through the um through the second
[2288] encoder
[2289] and then we select them using nearest
[2291] neighbors or something that
[2293] finds k nearest neighbors and then picks
[2295] one of them stochastically
[2297] so essentially what you're doing is you
[2300] are
[2301] forming these representations through
[2303] these dropped out and nearby points and
[2305] times that gives you like this good
[2307] local representation of the environment
[2309] and the world
[2310] and then from that you can start linking
[2312] these non-local points that are close to
[2314] you in the representation space
[2316] using something like nearest neighbors
[2318] and feeding that
[2319] into the system and so just showing here
[2322] this idea of like oh now i have all
[2324] these different candidates and i would
[2325] choose another
[2326] one that's sort of close to my picture
[2329] of a cat but it's not the same one
[2331] okay so now um oh wow
[2335] this i've already spent quite a quite a
[2337] while
[2338] so um and we're we're done at 4 30.
[2342] oh no we started a little late so
[2349] um okay so now this um we can get into
[2353] the results
[2355] uh using meow and these other
[2358] self-supervised learning approaches that
[2359] i discussed before
[2361] on on two different main examples the
[2364] first one being this movement decoding
[2366] example
[2367] from non-human primate and here we're
[2370] recording from primary motor cortex so
[2373] m1
[2374] what i'm showing here are the results
[2376] now for four different
[2377] data sets so what we do is we um
[2381] basically you know you have to figure
[2383] out oh how am i going i think another
[2385] question earlier was oh how do you
[2386] actually augment the data right
[2388] or sorry how do you figure out which
[2390] neurons to drop out
[2392] um so in this case we have sort of tuned
[2396] the the hyper parameters so the
[2398] architecture
[2400] and and the the drop out probabilities
[2404] and augmentations on one data set
[2406] and hold all of that fixed and and
[2409] and then use that same sort of
[2411] architecture and everything for these
[2413] other three data sets so in this case
[2415] you know we can actually generalize now
[2418] with retraining those architectures on
[2420] different individuals without having to
[2423] re-optimize the the augmentations and
[2425] drop out and
[2427] and and so on and so forth so we're just
[2429] showing um
[2430] the ability to form these
[2432] representations across these different
[2434] data sets
[2435] then we freeze the network and then
[2437] we're going to just train a linear
[2438] classifier
[2440] to be able to decode one of eight
[2442] different reach directions that the
[2443] animal is making a reach towards
[2446] um and and then from that we're
[2449] reporting the accuracy of that eight
[2452] choice
[2453] decoding um or sorry eight choice target
[2458] um output
[2462] sorry so um what i'm showing here are
[2465] the results with
[2466] an auto encoder that has this same sort
[2470] of
[2470] you know decoder um decoding task
[2473] applied to its representation space um
[2476] as well as sim clear the contrastive
[2478] learning method bio biomeow
[2481] and in all these cases we're comparing
[2484] with a supervised decoder that's trained
[2486] end-to-end on the same task so
[2490] one thing that's really interesting and
[2492] a cool takeaway from this
[2494] is that in many of the data sets that we
[2496] tested we can actually
[2497] outperform a supervised decoder
[2501] on held out test data
[2504] um in terms of this neural decoding test
[2506] so what that means is that you know you
[2508] if you want to train um a deep learning
[2512] architecture on a neural decoding task
[2515] right and you want to train it
[2516] end-to-end you might have some
[2518] overfitting
[2519] or some loss in terms of your
[2521] generalization when you try to test it
[2524] on some new data set that you haven't
[2525] trained on right and what we're showing
[2527] here is that through
[2529] this drop out
[2532] and you know and like so what i'm what
[2534] i'm showing here is even for bile
[2536] which doesn't use this additional sort
[2538] of long-range
[2541] um prediction as as a way of
[2544] infusing you know information into the
[2547] representations
[2548] in both bile and meow we're actually
[2551] outperforming a supervised decoder
[2552] so what we're showing is that dropout is
[2555] inducing some really nice
[2557] implicit biases into these neural
[2559] networks that allow us to generalize
[2561] better on downstream decoding tasks than
[2564] just
[2564] training the neural network alone so
[2566] that's a really cool result
[2568] i think in itself um and then moreover
[2570] we're showing you know
[2571] in some cases really large improvements
[2574] over
[2575] um you know things like auto encoders or
[2578] bio or some of these other
[2579] representation learning systems
[2581] um and we have um added to these results
[2585] now with even
[2586] fancier auto encoders um and so
[2591] this shows us that both the temporal
[2593] shift and dropout augmentation provide
[2595] this diversity and preservation of past
[2597] semantics in this case
[2599] um we can go further and kind of dig
[2601] into how different
[2603] classes of augmentations you know impact
[2606] the final decoding performance and
[2608] really dissect this
[2609] carefully um and what i'm showing here
[2612] are just
[2613] visualizations of the of the latent
[2615] space
[2616] um from some of these different methods
[2619] both for
[2620] two different individuals and what we
[2621] find in general is if we look at the
[2623] global
[2624] and local structure that we get with
[2626] meow we can kind of preserve the tasks
[2629] semantics and geometry more effectively
[2632] which
[2633] in this case is center outreaching so
[2634] we're actually preserving the
[2636] ordering of the targets and the circular
[2640] structure
[2641] this is now looking um just in 3d
[2644] at visualizations of um of these
[2647] embeddings
[2648] um the points are you know being colored
[2650] by the target direction so we can see
[2652] this really nice kind of
[2654] um global geometric structure
[2658] and pulling all these different classes
[2659] out and then also preserving the sort of
[2662] velocity distribution
[2664] um of the task as well okay
[2667] i spent a very long time um kind of
[2671] going
[2671] to all the you know nitty gritty here
[2674] hopefully you learned um
[2677] some new things about representation
[2679] learning i know we're running out of
[2681] time so i'm going to try to just kind of
[2683] quickly go through this um the second
[2686] example
[2688] is now applying the same
[2691] tools but to um to
[2694] rodent and in this case i'll dig
[2697] further into the mouse ca1 so
[2700] hippocampus results but
[2702] um these results are just showing that
[2704] you know with the same
[2705] classes of augmentations we can actually
[2708] still
[2709] do very good at decoding of of different
[2712] behavioral variables from the
[2713] representations learned with this
[2715] but now in this case we have really
[2717] coarse behavioral labels so
[2719] you know before we had this really
[2721] constrained task where the behavior was
[2723] really embedded
[2724] um within those labels but now we just
[2727] have labels about whether or not the
[2728] animal was awake
[2730] or whether or not they were in rem or
[2732] non-rem sleep
[2733] and these are now recordings over 12
[2736] hour long stretches
[2738] in free behaving conditions where the
[2740] animal is just sort of moving around the
[2741] cage and doing what they will
[2743] right and so the labels that we're
[2746] giving
[2746] to kind of optimize at least the
[2748] augmentations in this case are really
[2750] far from what the full richness of the
[2753] data is
[2754] and what we find is that when we
[2756] actually visualize the representations
[2758] learned
[2759] and now we're color coding them by the
[2761] different labels of ram non-rem and wake
[2764] um even just with the the the
[2767] behavioral readouts that we have which
[2769] we have very good decoding accuracy on
[2771] um we're finding that there's a lot of
[2773] really interesting
[2775] clustered and other structures that are
[2778] present within these representations
[2780] found by meow
[2781] that we can't get with just analyzing
[2784] the firing rates alone using different
[2786] dimensionality reduction techniques
[2788] so there's something that's really
[2790] coming out of these methods that we
[2792] can't get with a reconstruction
[2794] type approach but we're digging further
[2796] into this to really
[2798] um do this test this out rigorously but
[2801] i'll quickly show you in the last time
[2803] remaining
[2803] some new tools that we have developed
[2805] which i'm really excited about
[2807] which allow us to in tensorboard
[2811] which maybe you're kind of playing
[2813] around with a little bit
[2814] over in in the course um so tensorboard
[2818] you know gives us a way of basically
[2819] taking a neural network and then looking
[2821] at the latent space or the
[2823] representations
[2824] um within the network kind of in an easy
[2826] way and we basically
[2828] built an uh tensorboard extension that
[2830] allows us to kind of click on points in
[2832] the latent space
[2833] so shown here and then um zoom in to
[2836] all of these nearest neighbors in the
[2839] representation space and
[2840] and look at the video and behavioral
[2843] readouts
[2843] of what was actually going on within the
[2845] cage over those points and times that
[2848] the network is saying were
[2850] sort of close in terms of their
[2851] representation and so
[2853] this stuff is um hot off the press like
[2856] we just finished this
[2857] last week so we're starting to just now
[2859] really
[2860] dissect all of this but what i'm showing
[2862] here is a cluster that's been pulled out
[2866] that seems to correspond very heavily to
[2868] water bottle drinking so here i'm just
[2870] showing a positional
[2871] heat map over all of the nearest
[2874] neighbors
[2875] and where the animal was we can see like
[2877] a tracing of the cage
[2879] it's ball and it's um water bottle spout
[2882] and and in many of these cases i don't
[2884] know if we can
[2885] see if you can sort of see in the video
[2888] in most of these cases um we're finding
[2891] that the animal indeed is drinking from
[2893] the water bottle which is really cool
[2894] because this is kind of a rare event
[2897] that we were trying to pull out through
[2898] like behavioral decoding before
[2902] and so it was really exciting to see
[2904] that the neural data revealed to us this
[2906] unique
[2907] aspect of the behavior we can go further
[2910] into other clusters
[2912] this one we call getting comfy but
[2915] basically they have a nest at the center
[2917] and in all of these frames it's sort of
[2919] moving its bedding material
[2921] and we see again that you know in the
[2923] positional heat map we have a pretty
[2925] high
[2925] correspondence um this is cool because
[2929] they have two um they have like a box
[2932] and a ball down here in the right corner
[2934] and so this is a cluster of behavior
[2937] that has to do with this sort of
[2939] um play dynamic
[2943] um and we can kind of as i said these
[2946] are still really new but we're starting
[2948] to
[2949] consistently find that meow is kind of
[2952] zooming in on these behaviorally
[2954] relevant
[2956] aspects of the data and we have a way of
[2960] of pulling out video and kind of going
[2963] between the two in this easy way
[2965] by the way if anyone wants um to use
[2968] this tool
[2969] where we're happy to share just i mean
[2972] you know
[2972] if you have video and you have latent
[2974] spaces and you want to find
[2975] a way to visualize them please feel free
[2978] to reach out
[2979] um this was nest building so this is
[2981] kind of cool because
[2982] it actually involves like a lot of
[2984] different places in space but they're
[2987] all kind of related to
[2989] pulling in the nest material and so on
[2991] and so forth and we're starting to also
[2993] look into some of the sleep
[2995] transitions or sleep clusters as well
[2998] where we don't have behavioral readouts
[3000] um currently but um we can see whether
[3004] or not the animal is transitioning
[3005] between different sleep stages okay
[3007] great so i know that we're basically at
[3011] time and i want to give
[3014] time for more questions so i'll just
[3016] summarize
[3017] i talked about and introduced a new
[3020] approach for self-supervised learning
[3022] that allows us to
[3024] mine our data sets to find augmentations
[3027] that we can use
[3028] for prediction we
[3032] talked about the application of it to
[3034] neural population activity and
[3036] representation learning
[3038] and showing you know we can beat these
[3040] supervised decoders in some cases
[3043] um and then finally i'll just say that
[3047] we have
[3047] new work coming out i have a link at the
[3050] bottom
[3051] that sort of combines these
[3052] self-supervised learning
[3054] techniques with generative models which
[3056] i was dissing on at the beginning but
[3058] like
[3059] we wanted to have the best of both right
[3061] um
[3062] and what we're trying to do there is to
[3064] be able to use these ideas
[3065] to disentangle neural representations
[3069] and
[3069] and find ways to figure out
[3073] the how and the what in in movement so
[3076] um both figuring out where you want to
[3079] go and also how you get there through
[3081] the residual
[3082] components that you can get through the
[3083] generative model so kind of
[3085] having um having this ability to form
[3087] good representations and still generate
[3089] neural activity through combining um
[3093] and don't have time to go into that but
[3096] we have
[3096] stuff up on the website now if you're
[3098] interested
[3099] um in this other tool called swap vae
[3103] which
[3104] takes this idea further for um
[3107] even more interpretable representations
[3110] okay
[3110] and i'll end there thank you so much for
[3113] your attention and
[3114] i have yeah happy to take more questions
[3120] thank you yeah we can have a few more
[3122] minutes for questions from folks
[3131] uh yeah feel free
[3134] so just to be clear in the mouse video
[3138] the position in the cage was just for
[3141] the
[3142] viewing convenience and the model was
[3144] trained
[3145] just on the neural data right right
[3147] right yeah so this was just a way for us
[3150] to kind of
[3151] zoom in to the neural representations
[3155] and
[3156] see if they're correlated with behavior
[3159] we don't use that when training the
[3161] model but
[3163] we're really excited to see if we can
[3166] link it back to those cor
[3167] those finer scale behaviors in the
[3169] future okay and what's the
[3171] area that's being recorded from so this
[3174] is all in hippocampus
[3177] okay wow
[3180] wow yeah so there's a lot of cool stuff
[3183] happening there in
[3184] the campus thank you
[3187] yeah this was also this is like just
[3189] showing a zoomed out view
[3191] um of it after pca as well
[3194] so here we can see um more of the
[3197] clustering kind of without
[3200] more of this fractionated representation
[3202] that we're showing in this case
[3204] where it's like even more clustery
[3210] i guess a question that arises from that
[3212] and i'm sort of paraphrasing here
[3213] questions that are rising in slack is we
[3215] know there's there's some position
[3217] coding
[3218] in hippocampus right um
[3222] so in a sense it's not surprising that
[3225] um
[3227] this is surprising right where it's not
[3230] positionally
[3231] focused but we're it's picking up where
[3234] it's learning
[3235] how like positionally focused patterns
[3237] that's something you might expect just
[3239] from position
[3240] coding so wonder how you how you think
[3243] about that
[3244] yeah so this is like where the cool
[3246] science
[3247] is now right in terms of understanding
[3250] this
[3250] and um
[3254] so as i understand it a lot of times in
[3257] these more
[3258] free behavior conditions and i would
[3260] love to talk to
[3261] folks here if or if you have insights
[3264] into this
[3265] um in these free behavior conditions
[3268] often like place
[3270] cells aren't very like the the cells
[3272] aren't very strongly encoding of
[3275] places they are in more kind of
[3277] controlled
[3278] you know mazes and and tasks where the
[3281] animal is kind of put into
[3283] a more challenging environment that that
[3286] isn't necessarily reflective of its
[3288] natural behavior
[3290] um and so as i understand it in many
[3293] cases you don't see a strong of a place
[3295] in coding
[3296] effect within these natural behavior
[3298] conditions so that's one thing
[3301] and on the other hand it's like okay
[3303] well when when we are
[3305] dealing with naturalistic behavior it
[3307] makes sense that there could be a more
[3309] complex encoding that
[3311] goes beyond just you know encoding of
[3313] place and is
[3314] actually kind of more behaviorally
[3316] relevant or
[3317] it's sort of relevant to the motivation
[3320] or intention
[3321] or you know engagement of the animal
[3324] when it's in that place which is i guess
[3328] what we would potentially
[3330] think about when looking at the yeah the
[3332] results
[3333] say here right um
[3336] and then at the same at the same time
[3338] there's a lot of
[3340] behavioral clusters that are basically
[3343] in the same place but are different
[3346] behaviors
[3347] and those are also being kind of encoded
[3349] in different parts of the representation
[3351] space but that's
[3352] less clear to me you know right now
[3356] we'd have to dissect that a little bit
[3358] further to
[3359] see if that's a interesting
[3364] i think maybe a different way to to sort
[3366] of look at it is to say
[3368] sure in in the history of this this
[3370] field when people have recorded in
[3372] hippocampus
[3373] they've been able to extract this
[3375] position coding because that's so
[3377] explicit
[3377] but it's entirely possible that
[3379] hippocampus is also coding for much more
[3380] abstract
[3382] properties of behavior much more
[3383] complicated properties of behavior
[3385] that could only be pulled out in this
[3387] way
[3388] from naturalistic behavior also so
[3392] yeah that's i mean that's the exciting
[3394] promise
[3395] here right is kind of through combining
[3397] these advanced
[3399] analytical tools with kind of unique
[3402] measurement technologies or um
[3405] yeah recording tools we're seeing
[3408] something
[3409] you know new and it's exciting right
[3412] data science
