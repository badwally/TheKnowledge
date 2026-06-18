---
schema_version: 1
id: yt-fYoW8TxUAco
type: youtube
title: Brain-Score Benchmarking - CCN 2024
url: https://www.youtube.com/watch?v=fYoW8TxUAco
authors:
- Cognitive Computational Neuroscience
ingested_at: '2026-05-30T20:40:41Z'
content_hash: sha256:02aab4e2dc2af89eacfdc85a5e0a04a4391479625e55b4e9ab2eb655f961a36f
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: Cognitive Computational Neuroscience
  channel_url: https://www.youtube.com/@cogcompneuro
  duration_seconds: 6866
  caption_track: fetched
  snippet_count: 2882
filter:
  score: 0.7
---
[0] e
[44] today
[63] [Music]
[89] I e
[129] want
[152] [Music]
[170] we'll get started in 1 minute
[188] d
[224] good great hey everyone welcome back
[227] from lunch my name is Greta and I'm
[229] excited to introduce the brain score
[232] benchmarking
[233] competition brain score is a platform to
[236] test on how how well computational
[238] models perform on both Behavior and also
[241] neural uh data neural recordings um also
[244] called benchmarks so this competition is
[246] about neural benchmarks the data that
[249] the models are usually tested on uh so
[251] brain score the first code for brain
[253] score is written in
[255] 2017 and a lot has happened since then
[258] including a competition uh designed to
[261] find better models in uh
[263] 2022 and now things have been switched
[266] around a bit and this competition has
[267] been about finding uh benchmark that can
[271] help test uh these models as to how how
[274] good they actually are of um neural and
[276] behavioral responses um so I'll
[279] introduce Martin shrimp and Co car who
[281] are the main organizers of this workshop
[283] and uh please go ahead and start your
[290] introduction thank you Greta uh thank
[293] you also to F and Talia and the whole
[296] CCN committee this is great this really
[298] feels like a home conference for
[301] and yeah I'll have more thanks later but
[303] uh I I thought we would start by just
[305] declaring that our goal is to build a
[308] model of the system basically how is it
[311] that the human brain gives rise to
[313] intelligent behavior and personally I
[316] think there is sort of three main
[317] underlying reasons for that one is that
[319] is the basic science reason we want to
[321] have a mechanistic understanding a
[322] computational understanding of how
[324] intelligence actually comes about how it
[326] works it might lead to Next Generation
[329] Ai and and finally it might also lead to
[331] Future applications that maybe can
[333] actually help people at some point so if
[335] we now think about how to build such a
[337] model then how do we build a model of a
[339] complex system well I think there's one
[341] field that's pretty close to ours which
[343] is AI and usually there's sort of yeah
[346] at least two maybe three things that
[348] come to mind in the a I would say one of
[350] course is compute which I'm not going to
[351] go into into detail here but the other
[353] one is data probably everyone knows imet
[356] at some point once we had a million
[358] images to actually train models on and
[360] maybe importantly then also another
[363] couple 10K to actually test them on we
[365] were able to make a lot of progress and
[368] uh this maybe one version of what
[370] progress looks like so on the x-axis you
[372] see the different years and on the y
[374] axis is basically how the model accuracy
[376] over the years just became better and
[377] better and better uh Bic starting pre
[381] pre- deep net area into Alex net into
[383] ret and so forth and one thing I want to
[384] highlight here is that these models
[387] built a lot on each other basically
[389] machine was really good at sharing
[391] things and reusing things and
[392] recombining things so once alexnet came
[395] out people used those components and
[398] improved them and share them again and
[399] then the community saw which of those
[401] components actually work out and which
[402] ones don't and then you take the stuff
[404] that works out combin it with maybe new
[405] ideas and that's how you can keep
[407] building more and more of these things
[409] and that I would say in Neuroscience
[412] we've started to build and test models
[414] as well but I would say we haven't
[416] really been as good at sharing and maybe
[418] recombining things and that's one thing
[419] that that brain is trying to to push for
[422] with a lot of open source and also open
[424] evaluations so that you can really
[425] directly see which of the models and
[427] which of the model components improve on
[429] things and which ones may be done so you
[430] can see positive gradient towards
[432] ideally a complete model of of the brain
[435] at some point and so in in a lot of ways
[438] we are in a really good time because we
[440] have a lot of data so this plot is about
[442] neural data but there's also a lot of
[443] behavi data this is from the Stevenson
[445] lab on the x-axis again are years and on
[448] the y axis on a log scale now are how
[450] many neurons you can simultaneously
[451] record each dot is just one experiment
[453] so this goes up exponentially maybe it's
[455] even growing a lot faster now but
[457] clearly we have access to unprecedented
[460] amounts of data that we have never had
[462] before and still I would say it's been
[464] really difficult to make sense of all of
[466] this data we don't really have ways to
[468] process all of this if we just go to the
[471] basement and think really hard I would
[473] say rather there is a need for models
[475] here we have to digest all of this
[477] especially if you then consider maybe
[478] not just one experiment but actually all
[479] of them together then really I think
[482] there just not uh not a way around
[485] models so maybe connecting to what Greta
[487] said in the beginning about uh where the
[489] all came from sort of the the earliest
[492] days were pre I think pre- benchmarks in
[495] a sense and maybe as a as a quick shout
[497] out to my adviser Jim who's sitting in
[499] the front I think when I started in the
[501] lab one of the first questions I asked
[502] him was I want to build some cool models
[505] how do I actually test them how do I how
[506] do I what are the standard benchmarks
[508] that I can test them on and at the time
[510] the answer was oh we don't really have
[512] any of that we we have maybe data but
[514] you can't really compare things and
[516] especially if you want to compare with
[518] maybe models that are tested on other
[519] data then really all hell breaks loose
[521] so the the first yeah initially it was
[523] really just code for uh a single project
[527] and then eventually people found it
[528] useful so at some point we start
[530] branching out from really these small
[532] scale data to eventually put things
[534] together because otherwise you run into
[536] this case where we have what we call P
[538] efforts so you might have one lab that
[540] collects data from let's say V1 in the
[542] brain and maybe they even build a model
[544] and then that is published and usually
[546] discarded and then there's another lab
[547] that collects data from somewhere else
[549] again data is collected model is built
[551] publish and and discard and then you're
[553] left with this sort of Sue of data and
[555] Sue of models that just don't really
[556] talk to one another and I think in this
[559] case it just seems like the the sum of
[560] all these parts is much less than it
[562] could be so you might know this in in
[564] proverb where uh different people feel
[566] parts of an elephant nobody can really
[568] get the full picture that's what what we
[570] thought we were starting from this is
[572] all of course necessary you need this
[574] exploration in science as well where you
[575] maybe don't yet put things together but
[578] the the view of brain SC platform is
[580] really that it is the right time to
[581] actually scale things up and start
[583] integrating so the the hope is that we
[584] can build the system models that then
[587] are tested on not just one data set but
[589] ially all the data and ideal also an
[592] easy way so that we can really see the
[594] the full
[595] picture and so when we first started
[598] this I tried to to look at the first
[600] slide I ever presented this uh this is
[601] from 2018 uh I had built a very pretty
[605] logo which nobody liked so then we we
[607] had some revamping of that but uh at the
[610] time yeah we we just started from some
[611] data that we had lying around you can
[612] see we didn't even have V1 or V2 uh so
[615] this was already a first need for
[616] integration because then 20 Mo options
[618] lab came in gave us that data and now
[620] there's of course a lot more efforts
[621] like algonaut now last year powered by
[623] the large scale data set NSD there was
[627] before all of this check Al new
[628] prodiction challenge uh the neur Nance
[630] benchmarks Andor and I'm sure there's
[632] many others that I'm not putting here so
[634] I think this really starting to happen
[635] in our field which I find very
[638] exciting and we yeah we recently tried
[641] to then phrase this together like why
[643] why do we actually find this exciting
[645] for me it's mostly that I hope that
[648] these really good models at the end of
[650] the day will enable new technologies new
[652] applications and also I think across
[654] different model Trends we will gain some
[657] intuitive understanding maybe not that
[658] the classic level of circuits but but
[660] more on a level that's a bit more
[662] abstract like architecture and
[663] optimization and the belief for how to
[666] get there is maybe simple as in this
[668] plot where on the x-axis uh it's
[670] plotting the number of benchmarks on a
[672] log scale and the idea is that if you
[674] use more and more benchmarks to choose
[675] the best model then the performance of
[677] that model on yet another hell out
[679] Benchmark will just be better and better
[681] because you you have more and more
[683] statistical power and more more
[684] benchmarks to really choose which model
[686] is best at the end of the day you can
[688] phrase this another way which is
[689] basically as you add more benchmarks you
[690] reduce variance in what the model score
[693] really is like with respect to all data
[695] that you could possibly collect So
[696] eventually if you have let's say a
[697] thousand benchmarks you would hope that
[699] the best model identified by those
[701] benchmarks will also perform really well
[703] on another Hout Benchmark that the model
[705] has never seen
[708] before and yeah so from those hble
[710] Beginnings you you might if you have
[712] seen the website you might have seen
[713] that we tried to improve things quite a
[714] lot uh so new logo maybe a bit better
[717] than the one that I had and new leader
[719] board I think it's a lot more accessible
[722] where I know there are still many things
[723] that need to be worked on but uh this
[726] just to say that we are aware of many of
[728] them I know many of your logging issues
[730] we're we're trying to to improve things
[733] and yeah now there's also vision and
[734] language uh one thing I just want to say
[738] is with this competition I think we
[739] basically doubled the number of
[740] benchmarks really for the models in the
[743] room you have a lot more access to a lot
[744] of data now that as as I'll show in a
[747] second really hurts current models
[750] there's lot of models I think there's a
[751] lot of community maybe one issue that we
[753] have right now is that our community is
[755] a bit M skewed if we have ideas for how
[757] to to make that better then let's talk
[759] about it and yeah at the time I think
[762] before before this year we had a really
[765] good sort of upward trend of more and
[767] more models being submitted there was a
[768] peak that you can see in 2022 in the
[770] modeling competition but modelers are I
[774] think very much bought into this game
[775] access to data sure like it's an easy
[777] sell what I think is maybe has not
[779] worked as well as Buy in from
[780] experimentalists which is what prompted
[782] this this whole competition and uh yeah
[785] I mean I'm not going to read all of
[786] these but a lot of push back I think
[788] came from the best models maybe not
[790] actually being the best models because
[791] they're not being tested on what someone
[793] really cares about personally or that
[796] the metrics that are being used are are
[797] not perfect and so this the idea really
[800] for this competition was okay if you
[803] think things are broken which probably
[805] all agree on then here's we're going to
[807] give you money if you improve things uh
[809] so whole compilation pool and then what
[811] I think enabled it was we had a lot of
[813] models available uh the the platform is
[815] available and a lot of data that is just
[817] untapped with people that actually know
[819] how to work it and you you hear from a
[821] lot of the people that were able to tap
[822] into this data in a
[824] second and so then forther competition
[826] this year we focused on the visual
[827] vental Stream So the the eras that yeah
[830] mat mentioned earlier uh that underly
[832] our ability to do object recognition and
[835] we tested basically the models from the
[837] 2022 competition that were uh doing well
[841] we tested the the best 10 models as of
[843] uh a few months ago and we just tested a
[845] bunch of reference models that we
[846] thought everyone was interested in we
[848] are in the process of running all the
[850] other now one and a half thousand models
[851] as well so that you can see the trends
[853] but as you can imagine that takes some
[855] time so it's yeah just not ready for the
[857] competition uh before getting into the
[859] the results I want to first thank Co for
[862] co-organizing all of this with me uh I
[864] want to thank the MIT quests the
[866] engineering team and uh Eric and Jim
[869] also for sponsoring the price money so
[871] the the winers in particular should be
[873] thankful and also the broad Community
[875] for yeah I think enabling all of this in
[877] the first place it's now the the people
[880] that have won the competition I'm not
[882] going to say much I'll just quickly
[884] mention them so that you see who they
[886] are uh we have two winners for each
[890] track so for the behavior track the
[892] winner is Nick Baker followed by
[895] marinovich sorry for mispronouncing and
[897] for the N track winner is David kogan
[900] followed by Andrea costantino um the the
[902] stimul are some samples of what they had
[904] submitted uh you will hear from them if
[906] the stimula are the the key idea or or
[909] what else but I also want to mention
[911] some honorable submissions that I think
[913] are worth looking into so one is by Ben
[916] lanquist who I think has a really cool
[918] Benchmark where basically every model
[920] scores zero uh but unfortunately he's
[922] not eligible for Price money because
[924] he's in my group sorry Ben then uh
[927] there's Mike Ferguson who of the
[929] submitters should know because he has
[931] been tremendously helpful I think in
[932] just getting everyone's uh things
[935] submitted and then I also want to point
[936] out L Summer from Martin he's group he I
[939] think it's the only undergrad that
[940] submitted but he actually got things
[942] done really quickly and uh I think has a
[944] really nice Benchmark that is worth
[946] looking into as well okay uh some quick
[949] stats on what what happened so or maybe
[952] sort of three messages one is let's as a
[956] community maybe stop using Alex net I
[957] think we have many better models by now
[959] uh for instance if we just look at the
[961] competition benchmarks so the the
[962] different uh columns here are basically
[964] all the benchmarks that people have
[965] submitted and then these are the scores
[967] of Alex net which are pretty red so you
[970] might conclude okay so models just don't
[972] do this well right now well if you look
[974] at a model that is a lot better like
[976] resex with massively unlabeled data
[979] pre-training then that does a lot better
[982] uh so a lot more green still far from
[984] perfect like green here just means that
[985] it's a lot better but still uh not doing
[987] everything perfectly it's just just
[989] means that out of out of all these
[991] benchmark scores this model tends to do
[992] a lot better than alexnet and I think
[994] there's many other models so alexnet
[996] itself in 20124 I think just doesn't cut
[998] it anymore on a lot of these benchmarks
[1000] we have better
[1002] ones the second message that I came out
[1005] I think is pretty interesting is that if
[1007] you look at model scale so how many
[1009] parameters in the model and how much
[1011] data is a trained on so on the left is
[1012] parameter count on on a lock scale with
[1015] the average score on the benchmarks on
[1017] the Y scale then models that are really
[1020] small just don't seem to do as well
[1022] compared to models that are quite a bit
[1023] bigger this doesn't mean that scal is
[1025] the only answer I don't think that's
[1026] true but I think this also says that
[1029] keeping it super small with current
[1030] approaches doesn't seem to be
[1033] sufficient and the first thing that I
[1035] think for the in the interest of them
[1036] I'm not going to go into much detail but
[1038] uh across the benchmark scores you do
[1040] see that there's quite some interesting
[1041] correlations so some behavioral
[1043] benchmarks that are similar but then
[1045] yeah for instance here but then also
[1046] some differences where it's it's not
[1049] clear why models are performing really
[1052] well on one Benchmark but don't the
[1053] other uh you can also connect all of
[1055] this to previous benchmarks I'm going to
[1057] skip that in the rest of time uh I want
[1059] to thank Ben here because he made all of
[1061] these stats and all the statistics he's
[1063] also on the jop market for a post if
[1066] you're interested in a really cool
[1068] student in in the ctive competation
[1070] Neuroscience space I think Ben is a tery
[1072] person to talk to and so maybe finally
[1076] the most important message is that with
[1078] this compe
[1079] there's a lot of new benchmarks now that
[1082] models just fail on pretty horribly so
[1086] even the best models that we have are
[1088] just not able to predict this data which
[1090] I think for the modeling people in the
[1091] in the room this is a potential Gold
[1094] Mine where you can really show some some
[1096] improvements over what is otherwise the
[1098] state-ofthe-art and there's just a lot
[1100] of Delta that you can you can capitalize
[1102] on so let's put better models from that
[1104] and let's hear from the competition
[1106] winners on what exactly makes the models
[1108] fail so badly on these benchmarks
[1117] thanks
[1121] first hi everyone so we'll start with
[1123] the winners of the behavioral benchmarks
[1125] so our first speaker will be Nick Baker
[1129] [Applause]
[1156] me see if this works
[1172] yeah maybe if I just
[1175] try great there we go hi everyone well
[1179] it's great to be here with you and
[1180] thanks so much to the brain score team
[1183] for organizing this cool event uh so The
[1187] Benchmark I worked on for CCN this year
[1190] is all about how humans and nural
[1193] networks perceive the shape of objects
[1196] right and use that for object
[1198] recognition uh so a little bit of
[1199] History all of you probably know already
[1201] you know traditional feed forward
[1203] networks are not so good at recognizing
[1206] objects by their shape so you go from
[1209] you know maybe 90 plus% accuracy to in
[1213] the low 40s when you show a silhouette
[1216] versus a
[1217] photograph um but this story has gotten
[1220] better recently uh with more modern
[1223] networks whether that's because of
[1225] bigger training data or new
[1227] architectures I'm not sure why uh but
[1230] these modern Transformer neural networks
[1233] can recognize photographs at like 90
[1236] plus% accuracy and Silhouettes at 80
[1238] plus% accuracy so clearly networks can
[1242] recognize objects by their shape right
[1246] uh the question we were interested in uh
[1249] was what kind of shape information these
[1252] networks use right uh so one possibility
[1256] is that they really care about local
[1258] shape sh this would be stuff like fur or
[1261] feathers or we could think of them as
[1263] texture like properties of the object
[1266] shape uh the other possibility is they
[1269] might care about what I'll call
[1271] configural shape this would be like how
[1274] parts are arranged with respect to each
[1277] other and the third possibility is you
[1279] know like humans they care about both
[1282] local and Global shape or configural
[1285] shape uh so here's how we tested that we
[1288] created the new kinds of Silhouettes
[1291] called
[1292] Frankenstein um and all a Frankenstein
[1294] is is you take the top half of an object
[1297] you flip it around and you put it on the
[1299] bottom half of the object so this is
[1302] kind of nice because it preserves the
[1304] local shape information almost totally
[1307] in the image but it disrupts the the
[1310] configural shape information so to the
[1313] extent a recognition system cares about
[1316] configural shape they should be worse at
[1319] recognizing Frankenstein than uh intact
[1323] Silhouettes uh so we tested that on both
[1326] humans and neural networks I'll skip
[1327] through the details but they essentially
[1329] had to do a nine alternative Force
[1331] Choice task with
[1333] animals and here's what we find for
[1335] humans uh so uh maybe unsurprisingly
[1339] humans were better at recognizing intact
[1343] Silhouettes than Frankenstein
[1345] Silhouettes right humans care about
[1348] configural shape
[1349] we have Decades of perceptual research
[1352] that shows that not too
[1354] surprising here's where things get more
[1356] interesting we tested on a variety of
[1360] artificial networks and I understand the
[1362] brain scor team tested on several more
[1365] uh across the board we found you know
[1369] basically no difference in how networks
[1373] recognize intact whole Silhouettes
[1376] compared to Frankenstein silhouettes
[1379] right so
[1381] networks don't appear to care about the
[1384] configural properties of an as of an
[1387] object shape uh and now maybe the
[1390] million dollar question is why don't
[1392] they care about this right um and I'll
[1396] suggest two possibilities for now I'm
[1398] sure there are others uh the first is me
[1401] that maybe they just you know don't need
[1403] to care about configural shape they're
[1406] getting you know 98%
[1409] accuracy or something already you know
[1412] why learn something new and complicated
[1414] when you're already you know getting
[1415] close to
[1416] 100% if that's true what we really need
[1419] to do is create training curricula that
[1423] require the apprehension of configural
[1425] shape right where local Contour texture
[1429] or even texture information are not
[1432] going to cut it to accurately classify
[1435] images um and if networks then succeed
[1438] with this new training program you know
[1440] problem
[1441] solved the other possibility and this is
[1444] maybe a little more speculative is that
[1447] configural shape requires um what I'm
[1450] going to call abstract visual relations
[1453] um and artificial neuron networks at
[1455] least the ones we currently have may be
[1458] unable to apprehend these abstract
[1461] visual relations so if we think of this
[1463] kind of symbolically as having relations
[1466] like above you know which can take
[1469] arbitrary inputs or twice the length of
[1471] the principal axis which can take
[1473] arbitrary inputs uh artificial neural
[1476] networks may not be set up to learn
[1479] these kinds of abstract relations um and
[1482] we may need new more symbolic kinds of
[1484] network architectures um to start to
[1487] build capacities to recognize objects by
[1490] their Global shape I wish I had more
[1492] time to elaborate on that I've cited a
[1494] few papers here that talk about this
[1496] more um but why don't I end here today
[1499] by thanking James Elder my collaborator
[1502] on this work and the Brain score team
[1504] for having
[1506] [Applause]
[1511] me we have time for a couple of minutes
[1513] for questions so if anyone has a
[1515] question please go ahead
[1533] so uh configuration also matters for
[1536] internal features uh in particular for
[1540] face recognition um and have you thought
[1544] about that and and that tends to happen
[1548] most when you're an expert at some
[1551] category so dog show judges on dogs
[1555] birders on birds Etc
[1559] yeah that's a great question so I have
[1561] thought about that a little bit so yeah
[1564] faces I think are a great example of
[1567] this kind of abstract process that I
[1569] think needs to happen you know I think
[1571] especially of like when you see a face
[1573] from like a pair of screws and a line or
[1577] something like that where you know the
[1579] inputs you know the pair of screws don't
[1581] look like eyes the line doesn't look
[1583] like a mouth but when they're configured
[1585] the right way they look like a face to
[1588] us um so a neural network you know we
[1591] haven't tested this but I wouldn't
[1593] imagine would ever call that a face um
[1597] but it looks like a face to us and I
[1599] think that is because we're really
[1601] sensitive to these configural aspects
[1604] and like you said you know we're so kind
[1607] of used to and recognizing faces is so
[1610] important to us uh we really are good at
[1613] picking out these abstract properties of
[1616] the face
[1633] those are really interesting results so
[1635] thank you for um sharing them one
[1638] question I have is you know you had a
[1640] slide showing the performance of various
[1642] Networks On The Benchmark yeah that one
[1644] the one we just this one yeah so what do
[1646] you make of the fact that the vit was
[1648] you know already doing this task at
[1651] higher than a um human level is that to
[1654] say theories about what you need in the
[1658] model to achieve good performance are
[1660] like unnecessary at this point because
[1662] the red is doing really well or like if
[1666] you think that the the gap between red
[1669] and blue is what's important then like
[1672] obviously you know why would you need to
[1674] have a gap right that's not like a thing
[1676] you would think would things would be
[1677] selected on right you think we selected
[1679] on doing well right so if we're already
[1681] doing as well as the uh Human by some of
[1685] the models you know what else do we need
[1688] that's a great question so I I think you
[1691] could argue what doing well really means
[1694] here like for this elephant I guess you
[1698] can't yeah you can't see my mouse is
[1700] calling that an
[1702] elephant or is being confident that's an
[1704] elephant doing well well in some sense
[1707] it is right because there 's you know
[1709] local features that are in common with
[1711] an elephant it's more like an elephant
[1713] than whatever else is in the database so
[1716] um the fact that a network can do well
[1718] you know do we really want to call that
[1719] a failure I would say it's just a
[1722] difference between humans and networks
[1724] not necessarily a failure of neural
[1726] networks but a difference between what
[1729] humans do and what networks do because
[1732] humans look at this elephant on the
[1734] right and you know at least some of the
[1736] time more often than the elephant on the
[1738] left say
[1739] you know what the heck is that um
[1740] networks look at it and they say okay
[1743] you know that's a great elephant um so
[1746] uh I would say you know if you want to
[1748] build a network that is going to you
[1751] know have really high classification
[1753] accuracy I think we're on the right
[1755] track if you want to build one that is
[1757] like humans uh maybe there's still some
[1760] work to
[1762] do to go but thank you sure thanks
[1771] I was just remind I was just reminded to
[1773] mention that the winning award was 3,000
[1775] USD so congrats Nick again and
[1780] uh now I'm going to call up um Marine D
[1785] Movic um oh Jeff are you gonna okay oh
[1788] so uh Jeff Bowers is going to give the
[1790] talk for her and this is the runners of
[1793] price for the behavioral Benchmark award
[1795] uh competition is also 2,000 USD
[1800] [Applause]
[1825] great yeah I'd like to thank the
[1826] organizers as well it's it's a really I
[1828] think a great initiative here uh yeah so
[1833] uh talk about some data based on some
[1836] dotted line drawings and textured
[1838] Silhouettes so starting
[1840] off very much l like the last talk a
[1843] critical feature of human vision is it
[1845] relies on largely shape so in a classic
[1848] early study in Psychology by IR Beerman
[1851] showed that people could identify
[1852] colored photographs and line drawings at
[1855] essentially the same speed same accuracy
[1857] there was no benefit so all the texture
[1859] all the color was irrelevant to
[1861] classifying isolated objects uh so
[1864] that's a critical feature of human
[1866] Vision another you know classic finding
[1869] you know well known from psychology for
[1870] 100 years or more is that when when we
[1872] see scenes we organize elements of those
[1875] scenes uh by various perceptual
[1877] organizational principles sometimes
[1879] called gastal principles and so we
[1881] organize these things in ways and those
[1884] organizations are critical there's a
[1886] stepping stone towards recognizing
[1888] objects object we organize elements into
[1890] scenes into surfaces into object parts
[1894] and those are the representations that
[1895] are used in turn to classify objects so
[1900] uh you know it's again so so these are
[1903] we we care about shape and and we
[1905] compose shape often using these various
[1908] basic stult principles so that's human
[1910] Vision whereas we know uh that most Uh
[1914] current models that do well on brain
[1916] score for instance for one thing don't
[1918] care that much about shape and at least
[1920] that was uh true of some of the early
[1923] models the classic paper by Robert Goos
[1925] and colleagues uh where they super
[1928] you've all seen this before no doubt you
[1930] put the texture of a of an elephant on
[1932] the shape of a cat and the model
[1934] confidently claims that's an elephant
[1936] they care more about texture than shape
[1938] whereas humans would not would would
[1940] would confidently identify that Blended
[1942] object as a as a cat not a not
[1944] a not an elephant and uh and Chris the
[1948] paper of ours uh by by G of moto where
[1952] we kind of uh show even when we train a
[1954] model to have a shape bias on one set of
[1956] stimuli when train a new set of stimuli
[1959] it would go ahead and care more about
[1961] texture so there's a very strong
[1962] inductive bias of these models to care
[1965] about non-shape features when learning
[1967] new to categorize new items
[1971] so uh and also so so humans care about
[1974] shape models don't care so much about uh
[1976] shape often and furthermore
[1979] um humans you know are very sensitive to
[1981] perceptual organizational principles and
[1982] we've shown some of our own studies that
[1984] these models don't uh reliably and uh
[1988] you know capture most gastal
[1990] organizational principles so the logic
[1994] of our study was well let's make images
[1996] that are defined by shape that are in in
[1999] turn the product of gestal principles so
[2001] that presumably would cause these models
[2004] a great deal of grief and so that's what
[2007] we did and we used so we have we've been
[2009] Genera we've built our kind of a
[2011] something call we call a mindset Vision
[2013] toolbox we have this data set that's now
[2016] available that you can download uh where
[2018] we've you know collected about stimuli
[2020] from about 30 classic psychology
[2022] experiments or they're not all classic
[2023] psychology experiments but most of them
[2025] are classic psychology experiments
[2026] others are relevant visual stimuli to
[2028] test hypothesis about human vision and
[2031] they goes from high level Vision to
[2033] lowlevel vision and in between uh and
[2035] you know it was designed uh to make it
[2037] easy for uh people to to to test their
[2040] experiments on on on psychological
[2042] experiments and we just grabbed two of
[2045] our two of these stimuli sets amongst
[2048] the 30 are the ones we uh we use to
[2051] generate stimuli that had these
[2052] properties so we have uh and and we
[2055] wanted to generate things I mean again
[2057] we care about shape we care about gal
[2058] principles so it should be trivial and
[2060] so we picked images that we thought PE
[2063] humans would find trivial so we have for
[2065] instance uh a dotted set of outlines of
[2069] objects so you know you have to kind of
[2070] good continuation is the classic castol
[2072] principle so you can perceive that as a
[2074] line and you can see that as a bicycle
[2076] easily enough or we have texture uh
[2078] where we kind of compose more like a
[2080] silhouette but but not a constant
[2081] silhouette just a textured set of of of
[2084] characters again uh organizing based on
[2088] kind of principal similarity defining a
[2090] shape and humans can identify these
[2092] things quite so these are all TR to
[2093] identify these are birds uh the
[2096] difference between the left and the
[2097] right and so of these two was simply the
[2099] spacing between the dots and here we had
[2102] just different textured elements so we
[2103] had four data sets that we composed in
[2106] this way
[2109] elephants simple experiment four groups
[2112] of participants
[2115] saw uh 10 from 10 object categories 10
[2118] members per category so 100 images uh
[2121] per bench mark and 50 participants and
[2123] we flash these images oh I didn't even
[2126] say but oh oh yeah so I did so fixation
[2128] flashing for 200
[2130] milliseconds uh and then you respond one
[2133] of five
[2134] categories and not surprisingly humans
[2137] find this trivial so uh you know people
[2140] were about 95% in identifying these
[2142] objects when they're flashed if I
[2144] understood I think we the the one came
[2147] second place was based on this dotted
[2149] outline in this double space condition
[2151] which humans found slightly harder uh
[2153] but still getting about 95% 94% or
[2156] something like that whereas if you look
[2159] at the the performance across all the
[2161] models my understanding is the average
[2163] performance was a scaled score of 16%
[2167] I'm not quite sure what that is in raw
[2168] numbers but anyways models uh did very
[2171] poorly on these
[2172] stimuli
[2174] um so and more General point I want to
[2177] make is that we
[2178] know good behavioral and brain
[2181] predictions can be mediated by Visual
[2184] confounds and stimuli we know for
[2186] instance you know from you know object
[2188] you know from studies that there are
[2190] shortcuts and when you kind of identify
[2191] an image and classify it it can be
[2194] carried out by shortcuts for instance
[2196] the G study showed that there was a
[2197] shortcut there was texture that was
[2199] driving object recognition but those
[2201] same kinds of shortcuts or confounds and
[2203] principle can be used to classify and
[2206] and and and make predictions both
[2208] through RSA or linear regression methods
[2210] and so we have two of our papers here
[2212] one of them G of mocha on Thursdays got
[2214] a a poster where we kind of show
[2218] confound in brain score uh that in fact
[2221] it's it's the background not the target
[2223] object object that's driving most of
[2224] brain productivity in it so there's lots
[2228] of uh confounds and stimuli and
[2233] uh lots of stimuli that are predictive
[2235] object category a lot of stim features
[2237] that could be used to predict brain
[2239] score and so there as a consequence good
[2242] predictions don't inform you what the
[2244] similarity the metric you are they
[2246] actually similar underlying
[2247] representation or not well you don't
[2249] know because they're confound and you
[2252] haven't if you use a naturalistic data
[2253] set in which you haven't controlled or
[2255] manipulated independent variables you
[2257] don't know what features are driving the
[2259] good predictions and so the the this is
[2261] a figure from our BBS paper where we
[2263] just you know highlight this point that
[2264] you know the higher the prediction
[2266] doesn't necessarily mean any better
[2267] correspondence to the human brain and
[2269] what you need to do what you know in
[2271] most areas of science what they do is
[2274] run experiments where you manipulate
[2276] independent variables designed to test
[2278] specific hypothesis and to rule out
[2280] confounds finding out what are the
[2282] features that are driving good
[2283] predictions once you know what the
[2285] features are then you can say are those
[2287] the same features that drive human
[2289] performance on a task so that's you know
[2291] the standard methods of science you run
[2293] experiments where you manipulate
[2294] independent variables but my critique of
[2297] brain score is that's not what's been
[2298] doing so far I think this exercise is
[2300] great because that's what people you
[2301] know people are Chris Baker and us our
[2304] stimuli we manipula they're artificial
[2306] in some ways but they're specific Al
[2308] manipulate to test a particular
[2309] hypothesis is it configural processing
[2311] or not is it gal principles or not when
[2314] you when you manipulate images you test
[2316] specific hypotheses and you can and and
[2318] you can make some kind of informed
[2320] decision about whether these models are
[2321] working like humans uh and I think the
[2323] answer is that so far they're not uh
[2326] because and um so that's that that's the
[2329] message I would like to say about the
[2331] brain I guess well in the panel
[2332] discussion we'll have some conversations
[2334] about this but I think there's been a
[2335] mistake in the field of using these
[2337] observation
[2338] data sets of naturalistic stimuli not
[2341] running experiments to test hypotheses
[2344] about what is driving the predictions so
[2346] that's the uh that's the
[2355] conclusion maybe we can take one
[2357] question
[2362] Audi thanks
[2372] great talk um I want to take your
[2374] suggestion of uh avoiding confounds one
[2377] step further with your own stimuli um it
[2379] has been shown also that these uh uh
[2381] networks often look more at the higher
[2384] spatial frequencies so if your images
[2386] would be uh low pass filtered I think
[2390] you wouldn't even need Cal principles to
[2394] uh solve them so could it all due be due
[2396] to the fact that the networks here at
[2398] least for those stimul that you've used
[2399] here in benchmarks are looking for the
[2401] highest special frequencies so it's a
[2403] different confound maybe than the one
[2405] that you think your so are you
[2407] suggesting that if if I I did filter the
[2410] images that the performance of the model
[2412] would be better I mean if if that's no
[2415] no you that wouldn't do it either okay
[2416] no no I don't think you would you would
[2418] need to test it with images where the
[2420] the special frequency spectrum doesn't
[2422] matter for for finding the solution I
[2425] think yeah yeah I I I think that's right
[2427] and and uh yeah and that and that's a
[2429] you know that's a concrete hypothesis
[2430] yeah yeah it's a hypothesis yeah yeah I
[2432] totally agree with you yeah
[2437] [Applause]
[2445] yeah can ask get
[2450] sorry oh okay um so yeah uh I was
[2453] surprised that the uh accuracy for the
[2455] models that you've tested are so low I
[2456] was wondering if uh it's because there's
[2458] lack uh of instruction in terms of what
[2461] the model should be looking at cuz like
[2462] I just uploaded one of your images to
[2464] chat gbt and and say describe this image
[2467] in one word right it'll tell me it's
[2468] dots but I have to ask what object does
[2471] it represent in one word and it'll tell
[2473] me it's a plane right so do you think
[2476] it's uh the low accuracy of I think it's
[2477] only like 0.16 is like because there's a
[2480] lack of instruction in terms of what the
[2482] model should be looking
[2483] at um well in this case these models
[2486] have only one task is to classify so
[2488] it's not really I mean if if there was a
[2491] if there were multiple things these
[2492] models were capable of doing you need
[2495] some instruction but I guess my I guess
[2497] my first gut reaction is that there is
[2499] only one thing to do but uh but yeah did
[2503] did I didn't hear did did chat GPT
[2505] actually or did GPT 4 whatever succeed
[2508] or not succeed when you did it so we
[2510] found it failed on our stimula when we
[2512] did it but yeah so like uh basically
[2515] there when you ask a person okay what
[2517] this image actually represent right and
[2519] then they could have the they tend to uh
[2521] recognize it as an object whereas when
[2524] model process the visual stimuli they
[2526] could just say oh I recognize a lot of
[2527] dots so I'll tell you it's a dot it
[2529] doesn't really say oh it's shaped in an
[2530] object in the form of a plane so I think
[2534] the model the accuracy could be low
[2535] because there's lack of instructions
[2537] into
[2543] that cool thanks uh so before going to
[2546] the nor renders I want to make two quick
[2548] points one is Jim just reminded me that
[2550] I completely forgot one tiny detail
[2551] which is how we actually chose the
[2553] winners uh so basically the the
[2555] Criterion was if the average score of
[2558] all models on your benchmark is the
[2560] lowest then you win uh so the more you
[2562] disrupt the model performance is the
[2563] better uh and so now we'll hear from
[2566] David kogan on how we can disrupt the N
[2569] benchmarks I also want to point out real
[2570] quick at the end of this we have two
[2572] boxes with t-shirts uh we we got some
[2574] swag so if you want to get some some
[2576] cool new merch also stickers please grab
[2578] those yeah
[2588] it cool thank you uh so before I get
[2591] started I'd just like to acknowledge the
[2593] brain score team not just for the
[2594] awesome platform you guys have built but
[2596] um also for your endless patience with
[2598] me during the submission process so
[2601] thanks um our neural Benchmark utilized
[2604] an fmri data set from a study of
[2606] occluded object perception in humans so
[2609] specifically we were investigating
[2611] amodal completion which is where despite
[2614] of partial or fragmented view of an
[2616] object on your retina uh we often still
[2618] perceive or understand that the object
[2620] is a complete hole and in this
[2623] experiment we characterized the neural
[2625] representation of occluded objects
[2627] across both early and high level visual
[2629] cortex and we tried to understand to
[2631] what extent the neural representation is
[2633] completed um in the different visual
[2635] regions
[2638] um so to do this we presented these
[2640] eight object images without occlusion
[2643] and then with these two sets of
[2644] occluders which are complimentary in the
[2647] sense that they obscure entirely
[2649] non-overlapping halves of the image U
[2652] and the rationale for this is that it
[2654] creates two different views of an object
[2656] which complete to the same object but at
[2658] the pixel level they are entirely um
[2662] uncorrelated well technically they're
[2663] anti-correlated um but there's no shared
[2665] information there and so so therefore
[2668] the extent to which you see similar
[2669] patterns of response say in a region of
[2671] the brain or a layer of a a computer
[2673] vision model is going to give you an
[2675] indication as to how robust the model is
[2677] to occlusion how much completion might
[2679] be happening in the
[2681] representation so we presented these
[2683] images to nine subjects while we
[2685] recorded fmri at 70 they instructed to
[2688] fixate at the center of the image and
[2691] perform a basic 2 AFC discrimination
[2693] task animate inanimate uh and then we've
[2695] just performed a basic uh represent
[2697] presentational similarity analysis
[2699] within each region of visual cortex so
[2701] we just correlate the patterns of
[2703] response to the different images to
[2704] generate these representational
[2707] similarity
[2711] matrices so the primary measure in this
[2714] experiment was uh this sort of
[2715] completion idea so it's indicated by
[2718] invariance of the response to the
[2719] position of the occluders so on that
[2722] plot that's basically the height of the
[2723] green bar and what we anticipated going
[2726] into this or or hypo iiz was that we
[2728] would see um High sensitivity to ACC
[2730] cluder position in early visual cortex
[2732] and then get this like lovely emergence
[2734] of the completed representation As you
[2736] move through um but as you can see
[2739] that's kind of not what happened we
[2740] actually got some some pretty strong uh
[2742] index of of completion very early on
[2745] from the earliest cortical regions and
[2747] this surprised us somewhat uh because it
[2749] seems to be that it's it's no less
[2751] strong in V1 as it is all the way in in
[2753] high level visual cortex uh in it uh and
[2757] so so after we saw this I was like hm
[2758] maybe this will do well on the the brain
[2760] score Benchmark that's coming up because
[2762] um this suggests that V1 is is storing a
[2765] fairly completed representation and
[2767] usually there's a lot there's a lot of
[2768] models on there there's sort of they're
[2770] either feed forward or they lack the
[2772] kind of recurrent processing which we
[2774] believe explains a lot of this effect
[2779] here just as an aside we also see a
[2782] similar uh sort of uniformity across
[2784] visual regions if we were going to
[2785] compare uh un included and uded objects
[2788] so the difference between the dark blue
[2790] and the light blue bars is basically the
[2792] impact on the representation that you
[2793] have when you add an excluder to a
[2795] previously uncluded image uh and again
[2798] this effect is a Little Bit Stronger but
[2800] it seems to be just as strong in V1 as
[2801] it is in
[2804] it okay so to convert that data set to a
[2807] benchmark we had to overcome this issue
[2810] with uh the lack of measurement noise so
[2812] what happens if you put the 24 images
[2813] into a model say this is cornet and then
[2816] you get the representation out and do
[2817] the same RSM you get this really strong
[2820] diagonal you get this it's it's perfect
[2822] correlation there and this presents an
[2824] issue for our analyses because uh the
[2826] way they worked is you you're kind of
[2827] comparing on versus off diagonal things
[2829] and it sets a really really high bar for
[2832] the model and it seemed a little bit
[2833] unfair so uh with very little time to go
[2836] before the deadline we reverted to um a
[2839] more basic uh representational geometry
[2842] comparison between the models and the
[2843] humans so that's just a fancy way of
[2845] saying we took the model RSN we removed
[2848] the on diagonal values and then we
[2850] correlated it with each of our nine
[2852] subjects so here are the individual rsms
[2854] for
[2856] V4 and uh the ceiling that we calculate
[2859] here is uh it's the lower bound of uh
[2863] standard noise ceiling analysis in uh
[2865] RSA so what we do is we take each
[2867] individual's RSM we correlate it with
[2870] the mean of the remaining group um and
[2872] then we do that nine times across our
[2874] subjects and so the ceiling here is 335
[2876] that's how well the humans predicted
[2878] each other and uh I'm told that the 19
[2881] tested models scored an average of uh
[2883] 066 on this so much worse than the
[2886] humans predicted each other and uh if I
[2890] could speculate on why that is uh I
[2892] think it's probably a little bit to do
[2894] with like the visual diet because you
[2896] see sort of uh this selective uh image
[2901] uploading to the internet this
[2902] photographer bias that you see in image
[2904] net and so uh they're not really as
[2905] experienced with the collusion as we are
[2906] but probably it's it's more to do with
[2909] um especially since it was one of the
[2910] earlier visual regions that The
[2912] Benchmark performed um so well at was uh
[2915] is the fact that there there's isn't
[2917] really built in the the capacity for
[2919] recurrence to sort of fill in an object
[2921] representation over recurrent
[2924] Cycles um okay so with that uh I would
[2927] like to mention that we've made both the
[2929] stimuli and the rsms publicly available
[2931] for this Benchmark so you can take a
[2932] look them look at them yourselves and if
[2934] you'd like to come chat with me please
[2935] come find me uh if you can't find me
[2937] I've got a post a session on Thursday
[2939] afternoon and with that I'd like to
[2941] thank everyone at the tong lab awesome
[2942] place to work and the funding bodies
[2944] that support my research and you guys
[2946] for listening
[2952] cheers time for one question I
[2958] think hey David um great talk and very
[2961] cool data set um I was surprised though
[2964] by the amount of variability across
[2966] subjects did were you and do you have
[2968] any thoughts it seems like in particular
[2970] half showed a lot of that blocky
[2973] structure that you would expect but the
[2976] others did
[2977] not yeah that's a great point I think uh
[2979] if I was going to run this again I would
[2981] definitely get more data per subject uh
[2984] and yeah some of them are showing a much
[2987] better or or clearer uh clustering uh
[2991] yeah I think it is just there is just a
[2993] lot of individual level subject noise uh
[2996] that was quite common so ultimately a
[2997] lot of the analysis we do had to be at
[2999] kind of the group level for the for the
[3001] the true shape of the data to come
[3005] out um thanks for the nice talk um how
[3009] do you distinguish filling in of the
[3012] image from having a receptive field
[3015] that's just larger than one
[3018] pixel sure uh yeah so we've actually
[3021] done some experimentation on this uh so
[3024] we attempted to see to what extent of
[3027] basic receptive field properties could
[3029] get you sort of above zero similarity
[3031] across those two corresponding views and
[3033] it turns out you can get some uh but it
[3036] doesn't really get you anywhere near the
[3038] kinds of uh like completion levels that
[3040] we're seeing in V1 so if you look at
[3042] these um circles on the left these are
[3044] estimated prf size averages in V1 in a
[3047] human subject sample uh we then created
[3049] a uh well we parameterized the
[3052] pre-existing V1 net model um to have a
[3054] receptive field size on average the size
[3056] of that Sur Circle but the the kernel
[3058] size is much bigger so it can integrate
[3060] information more and the performance is
[3062] on the right so the completion is still
[3064] way lower than we've estimated in like
[3066] V1 across multiple experiments um and
[3069] it's mostly sort of driven by that
[3070] negative correlation which we use to to
[3072] seal uh to to Baseline uh this estimate
[3075] as well so yeah it gives you a little
[3077] bit but it doesn't give you anything
[3078] like what we're actually seeing in human
[3080] visual
[3081] cortex thanks thank you
[3090] okay next up is Andrea costantino who
[3092] won the second prize in the no track uh
[3095] same price money as in the B one so this
[3097] is 2K to you please enjoy
[3102] [Applause]
[3113] thanks one sec yeah I don't see m
[3121] Mouse
[3122] second
[3135] yeah are you a big Power
[3137] person yeah settings
[3148] okay probably try I'll try to connect
[3149] again then because probably we need to
[3152] do it on the other
[3161] screen all
[3165] right all
[3170] right
[3172] okay all right um so first of all I
[3175] would like to thank the I would like to
[3177] thank uh Martin and the Brain score team
[3181] for organizing the event the competition
[3183] and giving me the opportunity to be here
[3185] and talk about our submission and then I
[3187] would like to uh stress that this is a
[3189] shared submission and so I would also
[3191] like to thank my um collaborators hanso
[3194] debe and Stefan
[3197] BR okay so I want to I want to start
[3199] this talk with a brief behavoral
[3201] experiment so I will show you three
[3202] images so the the image of an object the
[3205] image of a of an animal and a third
[3208] stimulus and I'm going to ask you if
[3210] this is more similar to the to to an
[3213] object or an
[3214] animal okay most of the people here
[3216] would say that this third stimulus is
[3218] more similar to an object as you would
[3220] have guess because it is an object and
[3223] um we can plot this kind of um simil
[3226] this kind of Behavioral responses we can
[3228] plot it on a two dimensional um
[3230] representational space and we can do it
[3232] for another triplet and another triplet
[3234] and so on and eventually what we are
[3236] going to see see is a clustering like
[3238] this one where um let's say lookalikes
[3241] are more similar to objects than to
[3244] animals this is what we call an object
[3246] bias so this is a tendency to judge
[3248] lookalikes as more similar to object
[3250] than animals and this is what is at the
[3252] core of our submission um so this is a
[3255] data set that was developed by Stefania
[3258] brat in
[3259] 2019 so here you can see uh basically
[3262] three different uh category of stimuli
[3265] where we you have animal objects and
[3266] lookalikes and um basically in in this
[3270] study the the subject were presented
[3273] with this uh with this data set while
[3275] they were lying in a scanner and they
[3276] were asked to do a a similarity judgment
[3280] task okay so in term of results as we
[3283] mentioned before results from the study
[3284] essentially show a weak object bias at
[3286] the behavioral level where lookalikes
[3288] tend to be judged as more similar to
[3291] objects than
[3293] animals at the uh in term of DNN
[3296] activations we also see a strong object
[3298] bias where lookalikes are basically
[3300] mixed with with objects but they are
[3303] still very distinct from from animals
[3306] okay but the most important thing here
[3307] for the competition is actually the um
[3310] the brain activations which show an
[3312] animal bias that is very different from
[3314] what DNN and and humans
[3316] do okay so in this case basically the
[3318] the lookalikes are more similar to to
[3320] animals than two
[3322] objects I would like to highlight that
[3324] these results are not spous results in
[3326] the sense that they were replicated
[3328] internally across to different tasks
[3330] they were replicated with a EG
[3332] experiment and they were replicated um
[3335] with a computational experiment where we
[3337] tested several very specific hypothesis
[3340] about the let's say the basis of this
[3343] animal
[3345] bias okay so overall these results tell
[3347] us that so first of all they show us a
[3349] human brain failure in object
[3351] representation where the brain is
[3352] actually wrong in some sense or at least
[3355] the the areas that we that we EXP Lord
[3357] is they are wrong in some sense right
[3358] because they categorize uh look alike as
[3361] as more similar to animals than than
[3363] objects but most importantly for for the
[3365] brain score competition we also see a a
[3368] strong discrepancy between brain and DNN
[3370] that was um confirmed by our by our
[3373] computational uh experiments but it was
[3375] also corroborated now by the brain score
[3380] results okay I would like to end this
[3382] this talk by briefly touching on a on a
[3384] few points that I think are important
[3386] lesson that we learn from these results
[3388] so first of all they a well controlled
[3390] data set um so first of all these
[3392] results along with the achievement on
[3394] the brain score competition demonstrate
[3395] how a carefully controlled data set and
[3398] design can provide informative insights
[3400] about um about what is behind the
[3403] failure of the models even within more
[3405] predictive rather than purely
[3407] explanatory modeling Frameworks okay so
[3410] this has been touched already in in
[3411] previous in previous talk so in natural
[3413] images we have a lot of features and
[3415] these features tend to vary and
[3417] correlate with each other so they carry
[3419] a lot of confound so so big data sets
[3422] like imet and so on uh they carry a lot
[3424] of compounds that we can actually
[3425] control with these smaller data sets
[3428] also these results they show uh how DNN
[3430] can be a powerful and versatile tool so
[3433] basically a computational language to
[3435] test very specific hypothesis um about
[3438] psychological
[3439] phenomena so overall this achievement
[3441] illustrates the relevance of the
[3443] experimental approach on one hand
[3445] combined with the strengths of the
[3446] offered by uh dnns uh as image
[3449] computable models with Rich and high
[3451] dimensional representations that we
[3453] think uh are needed to understand
[3455] representational complexity observed in
[3458] the brain okay so the predictive power
[3460] of these representations along with the
[3462] explanatory power of controlled
[3463] experiments can move forward our
[3465] understanding of of biological and
[3467] artificial Vision
[3469] systems however these results also
[3471] suggest that maximizing alignment with
[3473] the human brain may be uh not what we
[3476] want may be not sufficient to build
[3478] better model of Visions it can even
[3479] result in conflicting demands right so
[3481] for example here if we want to optimize
[3484] to let's say predict the activations in
[3487] it we can have models that actually
[3488] underperform models that actually they
[3491] are wrong
[3494] behaviorally and that's
[3503] it hi thank you um so my question is how
[3508] much do you think the instructions that
[3510] are being given to the participant and
[3512] to the DNN is affecting the alignment
[3514] scores um to Echo a previous question if
[3518] you added something like a text encoder
[3520] to go along with the visual encoder do
[3522] you think that that way it would then
[3524] have you would fix this alignment
[3526] problem so this is a very good question
[3528] we um so we got these kind of questions
[3531] from reviewers in in the computational
[3534] in the computational paper specifically
[3535] and and you can see
[3537] we also use clip for example that is a
[3539] language in form model and we saw the
[3541] same exact results so basically the DNN
[3544] have an object bias rather than an
[3546] animal bias um so I mean these are all
[3549] hypotheses that can be tested uh we
[3551] tested one of them but and with clip
[3554] what is the text input that you're
[3555] putting in say again with clip are you
[3558] just using the visual encoder or you
[3560] using any of the text encoder as well uh
[3562] we are using the division
[3572] right okay no more questions then uh
[3575] let's thank Andrea
[3583] again and so now we'll have Co giving I
[3587] think a high level overview of what
[3588] maybe doesn't work well yet also has a
[3590] way to set up the panel which then Jim
[3593] will moderate and yeah please go
[3603] how everyone thanks for coming and
[3605] attending this session so I just want to
[3607] say that like it's very nice that many
[3610] of you had thanked me as a part of the
[3611] brain score team I'm like a distant
[3613] cousin of the brain score team so I'm
[3615] not like literally part of the brain
[3616] score team I have been kind of like a
[3618] you know appreciator of brain score but
[3620] a reluctant contributor to brain score
[3622] for a while but I think I'm you know
[3624] changing my views so I I'll set up some
[3627] some thoughts and this is going to be
[3628] more like of like a broader overview of
[3631] like how I think about it and how I've
[3632] been influenced to think about it so
[3634] it's about the brain score you know
[3635] benchmarking competition and I was
[3637] trying to come up with a title that
[3639] could fit my talk but I think this is
[3640] the closest I could come like nuances in
[3642] building benchmarks but you know it
[3644] might not be the talk might not be fully
[3646] aligned with this title so let's start
[3648] so I like to think in metaphors and you
[3650] I'm going to use a metaphor so this is
[3652] me and I'm trying to uh touch the bottom
[3655] surface of the Moon or some part of the
[3656] moon and I I think this is how I also
[3658] think about like making progress in
[3659] Neuroscience right and I'll say visual
[3661] Neuroscience so the I think the one of
[3664] the thing is that I can I can raise my
[3665] hand and I'm not touching the Moon that
[3666] much I can say so or I can measure the
[3669] distance from the Moon and I have a
[3671] ladder to sort of like go to the moon so
[3673] if I if I if I measure the distance and
[3675] I say okay the top of the ladder is like
[3676] some distance away from the Moon if this
[3679] distance is very small then I can kind
[3681] of my strategy is to add more rungs to
[3683] the ladder right I'm not going to do
[3684] something drastically different I'm
[3685] almost there so I'm going to go and and
[3688] and then I'm going to reach the moon
[3689] right so for the for the rest of the
[3692] talk I like to think of the Moon as some
[3693] sort of like idea of data in
[3695] Neuroscience like what we mean by the
[3696] brain and like how can we probe the
[3698] brain these ladders are the models and
[3702] uh the model improvements are these
[3703] rungs or however which way we going to
[3705] change the ladder or whatever but the
[3708] there's also an interesting thing about
[3709] like how do I actually measure the
[3711] distance so there could be many ways of
[3712] measuring distance so I'm not going to
[3714] talk about that there's also actually
[3715] another uh event called the battle of
[3717] the metrics that you might be interested
[3719] that might actually more explicitly talk
[3721] about the the the thing so that's one
[3723] situation but imagine I'm in a situation
[3725] like that where I'm there and the moon's
[3727] over there and I can still measure the
[3729] distance I'm not probably going to you
[3731] know you know bu uh build a ladder to
[3734] get to the moon in this case so so my
[3737] model improvements actually depend on
[3739] like where I am with respect to the Moon
[3741] right so I think we should appreciate
[3742] the fact that if we have the data and we
[3745] have the model we at least know how far
[3747] we have to travel and that's all about
[3749] benchmarking and this is actually the
[3751] most important thing I feel like bench
[3752] score is contributing to the field
[3754] Beyond some other OB obviously important
[3756] things as well okay so this is the
[3758] current uh brain score platform that
[3760] Martin showed uh I'm going to start
[3762] showing a few things that you know uh
[3765] provokes me to to think about it in some
[3767] way so I would say that okay sorry uh
[3770] one point I wanted to make is that if
[3771] you take the best model years like 0 53
[3774] you know almost halfway there for for
[3776] overall brain score and maybe like the
[3778] best scores are 6 so you can think of
[3780] this situation like this okay this is
[3782] like know somewhat influenced by what
[3784] data was available what he could put in
[3786] so the ladder is almost halfway there or
[3788] not halfway there but or a little bit
[3790] higher than halfway right okay so um one
[3794] group of us who who has access to the
[3796] ladders like we can play with models we
[3799] have we can collect data or we do talk
[3801] to you know experimentalists we can
[3803] measure ourselves and we can say okay
[3805] you know here is here is my situation
[3807] that I'm halfway away from from the moon
[3810] for for core object recognition right so
[3813] I got to improve this a little bit so it
[3816] if you if you think of the problem like
[3817] this it feels like we got a big enough
[3818] ladder all we need to do is you know get
[3820] some data add these like bits and pieces
[3823] and we'll we'll get there okay so that's
[3825] that's the obvious strategy if you think
[3827] of the problem like this but that could
[3829] be another way of thinking about this
[3831] that we have a ladder but we are looking
[3833] at the moon through a telescope and we
[3834] are saying that hey the ladder has
[3836] reached the moon but we are completely
[3838] you know doing this in denial of like
[3840] where the moon actually is and how
[3841] faulty our measurements are or how
[3843] faulty our metrics are or our you know
[3845] models are so I think a lot of people
[3847] would look at you know the current
[3850] scores and be like you know what I don't
[3852] think this is the right demonstration
[3854] like this is the right demonstration of
[3856] the the world the right demonstration is
[3857] like that but and and I don't I don't
[3859] know personally I actually don't
[3860] subscribe to the top view but I'll tell
[3862] you a few reasons why that kind of
[3864] things might come up why that kind of
[3866] feelings might come up so the first one
[3868] okay and what that literally means is
[3870] that whoever is claiming that is
[3872] claiming that the Moon is not there the
[3873] moon's actually over there so if the
[3875] moon is over there we have a big
[3876] distance to cover okay so if you look at
[3879] a Ben you know platform like this and if
[3881] you look at the neural data so there's
[3882] like some Choice has been made right V1
[3884] V2 V4 it why not you know some other
[3887] area why not the dorsal stream there
[3889] enough papers to say the dorsal areas
[3891] are also relevant to object recognition
[3894] so some people might be offended like
[3895] why is my favorite area not here so I
[3897] don't care about this rankings anymore
[3899] there's behavioral stuff which is like
[3902] you know why is my behavior not here and
[3904] and I actually totally agree that this
[3905] is actually a justifiable you know
[3908] frustration because like but but what I
[3910] would also like to channel is that this
[3912] whole process of benchmarking is as as
[3915] much a social process than it's a
[3917] objective scientific process so I think
[3919] these kind of events we need to come
[3920] together I I'll try to motivate a little
[3922] bit later so who chose these you know
[3926] and why those like why V1 V2 V4 it so
[3929] there are reasons for these you know
[3931] these choices initially so can we agree
[3933] on shared goals driving these Benchmark
[3935] choices like do we have shared goals in
[3937] the fields that can actually drive those
[3939] choices and I think my answer is like
[3941] they're probably isn't there should be
[3943] but there isn't and do we need to agree
[3945] like some people might say oh why should
[3946] we agree and you know Zoom uh zoom into
[3949] a local minimum maybe we don't need to
[3951] agree
[3953] um so that's one side of the problem the
[3956] real problem or or like to me what feels
[3958] a little bit more real is that if I look
[3960] at brain score I look at the Top Model
[3962] if I look at V1 V2 V4 it they're all
[3965] part of the same layer of the model
[3966] right so automatically I get a feeling
[3968] like that's something like wrong like I
[3971] don't know what it is but something
[3972] wrong then you go to the second model
[3975] sorry the first model the first three
[3977] are the same the second one is uh the
[3979] the it is different the second model all
[3981] are the same blocks they're all the same
[3983] blocks V1 V2 V4 it is the same part of
[3985] the model
[3986] the third one V1 is actually later than
[3991] V2 and V4 okay so so as a
[3995] physiologist I'm sort of frustrated I'm
[3997] offended I don't know what it is but um
[3999] what it really means is that I value
[4001] certain
[4003] benchmarks more than some others like I
[4005] think this idea of like the
[4007] physiological latency of the responses
[4009] that sets up this hierarchy I value
[4011] those benchmarks more so there is that
[4013] but who am I like who decides this how
[4015] do we decide it right so I think there
[4017] should be some considerations of like
[4018] how do we go about answering these
[4020] questions and to me this does not throw
[4022] brain score out of this you know
[4024] scenario this is the same thing I had uh
[4027] I was thinking when when um Jeff
[4029] mentioned this uh thing about like this
[4031] specific hypothesis testable ideas and I
[4033] think this these I these sort of like
[4036] way of testing model is exactly what we
[4038] should be doing and we should be doing
[4040] within a parameter like this where it
[4042] enables you to test those models like
[4044] when imag net came up
[4046] adversarial you know uh images were not
[4048] known at the point maybe maybe known to
[4050] somebody but it came up later we didn't
[4052] say imag net wasn't useful we still have
[4054] benchmarking competition so I think
[4056] those two are separate problems in my
[4057] head but I think these kind of events
[4059] actually allow us to talk to each other
[4062] and figure out like how do we combine
[4063] these frustrations and do something more
[4065] productive so the suggestion I have is
[4067] that initially we just had that one
[4070] Arrow from maybe one lab or two lab now
[4072] we need to engage and diversify these
[4075] from these four who are actually you
[4077] know talking to the thinking about the
[4079] same problems in their in their Labs so
[4081] we should engage and diversify this you
[4083] know the benchmarks and how we think
[4085] about this the the other question
[4089] is can the new data tell us how to
[4092] improve like we get some new data we get
[4093] this like we have this competition we
[4095] have this new benchmarks what did we
[4097] learn about the strategies to make
[4099] better models and can we improve in the
[4101] same way is that just more data or what
[4103] what are the strategies of course we
[4104] heard some strategies today
[4106] from folks who I would claim as they
[4109] belong in this this part where they're
[4110] actually like dealing with all these
[4112] components there's also another set of
[4115] people who I think arguably for me has
[4118] been most influential in this whole game
[4121] is those people who have a different
[4123] Moon these are folks from AI who have
[4125] nothing to do with the brain but they're
[4127] just generating models to reach their
[4128] own Moon and I think we need to pull
[4131] those models into this benchmarking
[4133] system so as I'm saying this and I was
[4135] actually making the the slides I
[4137] realized what PhD student is going to
[4139] take up this project who's going to fund
[4141] this project it means talking to like
[4143] cognitive neuroscientist system
[4145] neuroscientist AI specialist youit have
[4147] software Engineers managing that
[4149] platform this is not an easy thing to do
[4151] like you can tell whatever you want try
[4153] and Implement one of this you'll realize
[4155] where we are and why we had to start
[4157] with some of these specific you know
[4158] benchmarks right and on top of that
[4161] another interesting thing is that there
[4163] are other folks who just like to look at
[4165] the Moon in different ways you know so
[4167] these folks are experimental people who
[4168] don't necessarily you know engage with
[4171] image computable models or any model
[4174] sometimes but honestly when I look at
[4176] their papers I think they're collecting
[4177] the most interest interesting kinds of
[4179] data so there has to be also a
[4181] requirement to somehow interface with
[4183] them and get their data into the
[4185] platform as benchmarks right so again so
[4187] these are the complexities that that are
[4189] really at at play here at display here
[4192] and I think these kind of discussions
[4194] that we'll probably follow are are the
[4196] right sort of moves to go forward sort
[4198] of you know harmoniously together so
[4201] that was my talk uh I quickly wanted to
[4203] thank Jim and the team for actually
[4205] developing brain score and and having
[4207] all these stimulating con conversations
[4209] in the lab and you know for Martin for
[4212] tagging me along and uh you know for
[4213] your great friendship uh throughout this
[4216] time so and yeah I have my new labs and
[4218] I also try to you know discuss this
[4221] stuff with with my folks in the lab and
[4223] and thanks to the funding agencies for
[4224] letting me come here and play for the
[4226] flight thank
[4227] [Applause]
[4230] [Music]
[4232] [Applause]
[4235] you so next up is I think we should have
[4238] the panel
[4240] members come up uh and bring their own B
[4244] yo C
[4285] coming
[4292] okay hi everyone um my name is Jim Dar
[4296] Carlo I run a lab here at MIT um and uh
[4300] I've been a big supporter of this effort
[4301] that Martin's LED in brain score um I
[4303] want to start by thanking Martin and the
[4305] team for organizing this Martin and Co I
[4307] guess so thank you round of applause for
[4308] you
[4313] guys so I I I played hardly any role in
[4316] this competition other than to cheerlead
[4318] but now I was asked to just moderate
[4319] this panel discussion so I I I I gave
[4322] these guys all a bit of questions ahead
[4323] of time but I'm first going to ask them
[4325] to just give their 10 second
[4328] introduction to who they are and any
[4329] relationship at all to brain score so
[4331] let's just go around and why don't we
[4332] start there go ahead
[4334] Dan uh yes I'm Dan yans and I'm uh in
[4339] Psychology and computer science at
[4341] Stanford um I was here in Jim's group
[4345] prior to the launch of brain score so
[4348] you know I've been seeing it for many
[4350] years I Al should say I'm the board I'm
[4351] on the board of the brain score advisor
[4354] Advisory Board um
[4359] okay I I'm um federenko and I have a
[4362] language lab here at MIT and I guess um
[4365] a version of language brain score um is
[4369] the plane we were building as Martin and
[4373] Greta and others were writing the first
[4375] paper relating a whole bunch of models
[4377] to a bench a few benchmarks we had in
[4379] the lab um so that's been my involvement
[4384] guess hi uh I'm Janelle feather I'm
[4387] currently a uh postto at flat iron
[4390] Institute um in New York City uh and but
[4393] I will be starting as an assistant
[4395] professor at K melon next year in 2025
[4399] um and so uh my relationship to brain
[4402] score is that um I did my PhD at MIT
[4404] sort of while brain brain score was very
[4406] actively being developed um I was
[4408] thinking a little bit more about
[4409] benchmarking things on the auditory side
[4411] which I think would be really fun to
[4412] expand brain score at some point into um
[4415] but yeah I'm excited to be
[4418] here yeah I just gave a talk U I'm goar
[4422] I was a postdoc with Jim and now I'm an
[4424] assistant professor at yor University
[4427] and and I'm also in the brain score
[4428] advisory team but uh yeah I saw brain
[4431] score develop from scratch by Martin and
[4433] Jim and others effort so uh I'm hoping
[4436] to contribute more to brain score I
[4438] contributed a little bit here and there
[4439] on the benchmarking side
[4441] so yeah and I'm a Jeff Bowers a
[4444] professor at the University of Bristol
[4445] in the UK so I'm not linked to brain
[4448] score I guess I'm a Critic of brain scor
[4449] so that's maybe my role here okay good
[4453] we'll we'll try to tap that Jeff so let
[4455] me just try with the first question real
[4456] quick I want one quick answer from each
[4458] of you does the field actually need
[4460] platforms like brain score you can say
[4462] yes no or maybe and then we'll expand
[4465] Okay so go ahead Dan oh yeah definitely
[4467] because without it you'll never know
[4468] that's more than one word yes no yes
[4471] okay yes right I didn't hear from E yes
[4476] yes Jeff I'll say no okay good so that
[4480] so there's four yeses and we could maybe
[4481] have them elaborate but maybe we could
[4483] start with Jeff so the field does not
[4484] need a platform like brain Square could
[4486] you tell the audience more of why you
[4489] think
[4490] not um well I I guess it's just the
[4494] approach that I think think so far I
[4496] mean I think this this what we're doing
[4498] right now is great which is maybe
[4501] transforming what I've seen was brain
[4502] score but I you know again like I
[4504] briefly said before I see brain score as
[4507] a an approach of science where you're
[4510] using big observational studies without
[4513] manipulating images testing
[4515] hypotheses focusing on the basis of the
[4518] predictions just looking for higher
[4519] scores which I think makes a lot of
[4522] sense in an engineering context but in a
[4523] scientific context I think it's uh
[4527] leading to blind alleys where you kind
[4528] of working harder and harder to get a
[4530] high score and
[4533] often just you know but in the wrong
[4536] space altogether okay so to Jeff's
[4539] worried a bit about just chasing the
[4540] benchmarks without gaining intuition of
[4542] the models along the way just Channel
[4544] some of what you're saying yeah and and
[4546] with a particular focus on I mean the
[4548] people you're you know people are
[4549] manipulating models but they're not
[4551] manipulating images just focus on
[4554] naturalistic image data
[4555] I think is leading to mistakes okay so
[4559] good does anybody of the yers want to
[4561] comment on that or disagree or agree in
[4563] any way anybody want to chime in yeah
[4565] I'm happy to disagree because if you
[4568] think you have an idea or hypothesis you
[4570] can encode that as a
[4573] metric and like you can choose whatever
[4576] stimuli you want whether it's natural
[4577] stimuli or non-natural stimuli once
[4579] you've done that you to judge
[4582] correctness you have a notion in your
[4583] mind of what correctness means and has
[4585] to be able to be Quantified or else you
[4587] can't say it's science so if you've got
[4589] a definition of what's correct and you
[4591] can control the stimuli then don't you
[4594] want people to quote Chase The Benchmark
[4596] of satisfying a model that will do on
[4599] the stimuli that you think are important
[4601] the being good at the metric that you
[4603] think success is yeah of well I'm I'm
[4606] saying to this session where people are
[4610] running experiments so you know they
[4612] testing hypothesis is a good approach
[4614] that's but that's I mean the word
[4616] Benchmark is being transformed into an
[4619] experiment and if you run an experiment
[4621] where you manipulate with the particular
[4623] hypothesis in mind of course I'm a
[4625] psychologist I run experiments but my my
[4628] objection has been for a while now
[4630] there's been this pursuit of predicting
[4633] and making strong conclusions about the
[4636] similarities based on working with
[4639] naturalistic images and not knowing what
[4641] the basis of the predictions are so in
[4645] that but yes if if the if if people
[4649] change their approach to do experiments
[4652] then I'm totally on board and that's
[4653] what we've been doing and that's what I
[4655] think everybody should be doing so it's
[4657] not it's not against it's not against
[4659] experiments it's observational data sets
[4662] without controlling the materials and
[4663] testing hypothesis let's let somebody
[4665] else weigh in in the middle there any of
[4667] you three
[4668] want sure yeah I'm actually really
[4671] sympathetic to the um over Obsession in
[4674] the field currently with naturalism I
[4676] think that has taken back a lot of
[4679] progress that has been made in thinking
[4681] about a lot of problems and people kind
[4683] of think it will just once we know how
[4685] to predict brain responses to some
[4687] naturalistic stimulus will understand
[4688] everything and it's just not going to
[4690] happen I mean I work in the domain of
[4691] language and just too many things are
[4693] confounded and most linguistically
[4695] interesting things just don't happen in
[4696] naturalistic word because it's all like
[4698] high frequency words and easy
[4700] constructions for language we started
[4702] with data we just had available because
[4704] there is Alo host of complexities in
[4706] collecting High Fidelity item specific
[4709] responses to language because unlike
[4711] Vision you can't just present the same
[4712] image a 100 times and get a really
[4714] reliable response it's really annoying
[4716] in that way but um so we just had some
[4718] stimuli that we had collected data on
[4720] for whatever reason we started with
[4721] those and so that was the initial thing
[4723] but since then um Gruta and abbal
[4726] husseini a lot of others have been
[4728] collecting data on exactly the kinds of
[4730] things that um you were pointing out
[4732] Jeff like including controlling for
[4734] particular things or even selecting sets
[4737] of stimuli that specifically are
[4738] designed to discriminate best among some
[4740] class of models or you know to then get
[4742] insights into why and so on um but I do
[4745] hear you on naturalism I think the field
[4747] has gone way way to the dark side with
[4751] that Janelle yeah yeah I mean I mean to
[4754] chim in I I also just agree about um
[4757] thinking about
[4758] more targeted um maybe synthetic uh
[4763] experimental stimuli um and I mean this
[4765] debate has has went on since sort of
[4767] whenever people first started collecting
[4769] very naturalistic data sets right like I
[4771] know that Nicole rest and Tony M had
[4773] this like really nice article in Praise
[4774] of artifice in like the early 2000s
[4778] right um and so this like even predates
[4780] sort of this idea of benchmarking it's
[4782] just like whenever you're designing an
[4783] experiment what types of stimuli should
[4785] you actually be using um and so I kind
[4788] of think about I I'm like really happy
[4790] now that like some of these what some
[4792] people would call like out of
[4793] distribution or like very targeted types
[4796] of stimuli are being added to to the
[4798] brain score platform because I think
[4799] that that is where it needs to go but I
[4801] guess I want to Pivot a little bit to
[4802] just say that like I think that that is
[4804] like kind of a separate issue than like
[4806] having some sort of publicly available
[4807] benchmarking system and I think that
[4809] brain score in a way like it it really
[4813] is a it really does a lot for the
[4815] community in terms of reproducibility
[4817] because actually running somebody else's
[4820] uh data set and metrics um in exactly
[4823] the same way on your own system can
[4825] oftentimes be very very very hard um and
[4828] the actual platform that has been built
[4830] where you can submit a model and get it
[4832] scored on various data sets means that I
[4835] think that like if we if we put a little
[4837] bit of trust in the BL brain score
[4839] developers which I I hope that we do
[4842] that means that we can sort of trust the
[4843] results in terms of Which models are
[4845] actually doing better on the various
[4847] benchmarks which I think is a really
[4848] good thing for the community to
[4850] have um I want to add one more point I
[4853] think I partially agree and and there's
[4855] some points of disagreement so the um
[4859] there are there is an example in the
[4861] exist so there I think there's a debate
[4862] about brain score as it exists today and
[4865] how we Vision it for tomorrow
[4867] so in the brain score that exists today
[4869] there has been a couple of occasion
[4870] where there has been targeted
[4872] experiments so for example we did a
[4874] study together where we um had models
[4877] compared to humans and image by image
[4880] and we decided like which are these
[4881] images that are different between humans
[4883] and models and then we had developed
[4885] like a whole bunch of record networks
[4886] based on it that solve that problem so
[4889] that is not U um like maybe those are
[4892] not the exact same experiments that
[4893] others were doing but this was also sort
[4895] of like a little bit of a hypothesis
[4897] testing with the existing set of model
[4899] so some attemps like that has been done
[4901] not at the level that it should be done
[4903] so that part I agree but some something
[4905] that I want to point out is that
[4907] sometimes like when we have a very
[4908] specific hypothesis then it ends up
[4911] being like it could be that we will
[4914] overfit on solution a little bit towards
[4916] that and I think brain score kind of
[4918] like you know is sort of guard rails
[4920] against that by then testing the models
[4922] across all other possible benchmarks and
[4924] to show that you know you improved on
[4926] that particular thing but then you
[4927] didn't really like improve on the others
[4929] so that's also some an advantage that I
[4932] find that even the current brain score
[4933] sort of has as it exists today so yeah
[4936] those would be my two
[4938] things I would just like to comment one
[4940] more time on this there's my
[4942] understanding having been close to and
[4944] then a little bit further further from
[4945] brain score is that there's no bias
[4947] towards natural stimulating natural
[4949] stimuli in our in the people in Who
[4951] Running brain score's mind right like
[4954] just to put it in in like in context I
[4956] think there's a mantra that a correct
[4958] model should work on all stimuli whether
[4960] or not they're natural or created by you
[4963] in some way and that's very deeply held
[4964] belief within this in the brain score
[4967] context so to the extent that there's a
[4969] bias in using natural stimuli rather
[4971] than like stimuli design to test a
[4973] certain hypothesis I think it's just
[4976] those are the things that got
[4977] contributed effectively so to put that a
[4979] little more context right now the
[4981] metrics for you know there's metrics for
[4982] different neural alignment on different
[4984] brain areas and for V1 and for for V4
[4988] and it they tend to be more natural
[4989] stimulus biased but for we V1 and V2
[4992] almost all of them are tested on the you
[4995] know standard hyp hypothesis testing you
[4998] know artificial so-called stimuli and
[5001] that's because the people who did the
[5002] neural collection on those areas those
[5004] are the stimuli that they cared about
[5007] and so the models to be good have to do
[5009] well got to do well on V4 and it and V1
[5012] and V2 and so you know um I think it's
[5015] just the people in the field have
[5017] different hypotheses and the different
[5018] things that they're testing and
[5020] sometimes the hypotheses are better
[5022] tested by natural stimula and sometimes
[5023] they're better tested by artificial
[5025] stimula and so I would suspect at this
[5027] point that the majority some decent
[5030] fraction of the actual metrics currently
[5032] on brain score do contain artificial
[5034] stimuli
[5035] so I just I think it's like maybe
[5037] there's like a um sort of a stereotype
[5041] of what's on brain on brain score but I
[5043] think that stereotype is not true well
[5047] um the critical point isn't whether it's
[5049] natural or not the critical question is
[5052] whether the stimuli are manipulated in
[5054] ways to test a particular hypothesis and
[5057] focusing on the data from it and and and
[5061] was it V V4 those stimuli are not
[5064] designed to test what is so we have this
[5068] poster coming on Thursday where we kind
[5070] of we take the a data set from brain
[5072] score where we have you know these the
[5074] it or before where we have an object uh
[5077] in in a you know in a random pose on a
[5080] random background and we ask the
[5082] hypothesis well what is it is it the
[5084] object or is it the background that's
[5086] driving the prediction so that's a
[5088] hypothesis and you you and you you have
[5090] to manipulate the images to answer that
[5093] question and so for you know for I won't
[5096] speak to the V1 data so much but the
[5098] point is this people aren't asking the
[5101] question what are the features that are
[5103] driving good predictions in these models
[5106] in brain score because you wouldn't know
[5109] until until we ran this study you didn't
[5112] this is a model of it's supposed to be a
[5114] model of core object recognition and you
[5117] don't know whether it's the background
[5119] or the object that's driving predictions
[5122] and so I can tell you on Thursday which
[5124] it is but you you wouldn't know unless
[5127] and you could run you could run brain
[5129] score you could run more and more images
[5130] you could do it over and over again you
[5132] would never know the answer to that
[5134] question unless you you manipulated the
[5137] images in such a way that you dissociate
[5140] the object from the background and when
[5142] you do that and that's like what Robert
[5143] garos did he says you could run Bing
[5145] score all you want if you ask the
[5147] question is it the texture or the shape
[5149] that matters more it doesn't matter what
[5151] brain score you get you can get 100%
[5153] brain score you would not know unless
[5156] what you did was what Robert garos did
[5157] which he says I'm going to manipulate
[5159] the image and put the texture of the
[5161] elephant on the shape of the cat that's
[5163] an experiment to test a particular
[5165] hypothesis and there is no way to get
[5167] around that unless you manipulate the
[5169] images to test a particular hypothesis
[5172] and that's what brain score does not do
[5174] can I um can I try to summarize a
[5175] discussion because I think there's
[5177] actually a bunch of agreement and maybe
[5179] Jeff will push back on this but I think
[5181] there is agreement maybe even among Jeff
[5183] that the field needs plat forms were
[5185] reproducible tests of things geros and
[5188] others every paper that's been done
[5190] ideally somebody submits a model as
[5192] Janelle said and you can get reliable
[5194] scores back and that's as Co pointed out
[5196] as talk hard work for teams of Engineers
[5198] just to stand that up and keep it going
[5200] I see you're noding Jeff soer in that
[5202] sense of a benchmarking open platform
[5205] you might agree that that's a necessary
[5207] component that was always the reason for
[5210] brain score there's a secondary
[5212] inference which some of you are making
[5214] and Jeff's making strongly that the
[5215] purpose of brain score is to in some
[5217] sense substitute for the hypothesis for
[5219] being the scientist in hypothesis
[5220] testing that is not the reason for brain
[5222] score was never intended to be and so
[5225] you could use brain score to then follow
[5227] up with various things and So Co was
[5229] making this point brain score is
[5230] essentially that Delta measuring device
[5232] but it rolls into the fact that
[5234] sometimes people take the chosen
[5236] benchmarks as traditionally how we as
[5239] scientists has engaged in hypothesis
[5241] testing especially Vision scientists I
[5244] would turn the crank one knob so just
[5245] seeing that we may have agreement on all
[5247] of that but I'll just turn the crank one
[5249] knob to say you could always imagine no
[5251] matter what the hypothesis is what is
[5253] the next move on the model build and I
[5255] think we could have a discussion about
[5257] how we as do we think that maybe this is
[5260] my next question for the panel as we as
[5263] you look at a set of benchmarks and
[5265] deviations we saw today a few benchmarks
[5267] that models failed poorly on and maybe
[5270] as Jeff said oh we had intuition let's
[5271] design those and we'll show they form
[5273] pale we'll show it's because not doing X
[5275] Y or Z in in his version of of the
[5277] telling but we could do that with any of
[5279] the benchmarks or even any of the images
[5281] within the benchmarks how do we as a
[5283] field react to those Deltas to co Delta
[5286] to the
[5287] Moon I would I would posit there's a
[5290] large Divergence of opinions there and I
[5291] like to hear from this panel is like as
[5293] brain Square as a public measurement
[5295] tool not a here's telling you exactly
[5298] how to build the best model tool which
[5299] is a difference to be clear how does
[5301] this group think about who should be
[5303] responsible for building the best models
[5305] and how does a brain score contribute or
[5307] maybe not contribute to that goal which
[5309] is sort of what I hear Jeff saying like
[5311] how does it drive the field forward to
[5313] the next models of the system that we
[5316] all care about and are trying to model
[5317] so that's my next question in a
[5318] long-winded way do folks have comments
[5320] on
[5325] that maybe no one
[5327] cares I have another question if that's
[5329] not exciting maybe I said it too how do
[5331] we how do we react to benchmarks as a
[5333] community to build next models should
[5334] that go as a social
[5337] process well I do have a comment on it
[5340] but I feel bad that I've been talking so
[5341] much okay so sorry I feel like I've been
[5343] talking too much go for it Dan well okay
[5346] I think one part of it is that better
[5349] understanding of what the things on
[5350] there are so you said there's no hypo
[5353] replying to something else which I think
[5354] is a really critical part of this well
[5356] there's two things one of them is you
[5358] said that there was not a hypothesis
[5359] being tested by benchmarks like um you
[5362] know neural predictivity on the hung it
[5367] particular data set um and um you know
[5372] uh only having natural stimuli in it but
[5375] that's not true there was a hypothesis
[5377] on the in the minds of the creators it
[5380] just wasn't the hypothesis that you
[5382] would test what was our hypothesis it's
[5385] we wanted to see how well models
[5387] optimized for something like
[5388] categorization goal on the things that
[5391] you the the um like uh the the supposed
[5395] animals the the simulated animal the
[5397] model would see in the world how well
[5400] does that you know drive it predictivity
[5404] on other data sets basically and that
[5407] that configuration was our hypothesis
[5410] that models optimized for things in the
[5412] real world like mostly stimuli as you
[5414] draw them from the from the distribution
[5416] of natural images would drive a lot of
[5419] responses whether we the data the the
[5421] test data set was confounded as a
[5423] different story but the um that confound
[5427] is only a confound if you have a certain
[5428] hypothesis in mind okay but um it's all
[5432] a certain you know certain idea the
[5434] confound you mentioned actually isn't a
[5436] confound for us because we we're talking
[5438] about neural responses to things you
[5439] might see in the world now um that
[5442] doesn't necessarily mean you the neuros
[5444] responses are true for all you know all
[5447] stimuli and maybe if you put certain
[5449] stimuli in that you think are going to
[5451] distinguish between models that we
[5454] should do that but the hypothesis we
[5456] were testing at the time was different
[5457] than that but it was a hypothesis okay
[5460] so I think like not picking stereotyped
[5463] broad
[5465] objections and like being well that that
[5467] system only never would imagine they
[5469] were not interested in hypothesis
[5471] testing I think a better go rout is to
[5474] ask what hypothesis were you testing as
[5476] if somehow we were different than
[5478] scientists in some uh uh un like sort of
[5482] engineering e way as opposed to actually
[5483] trying to test something about the world
[5486] but the other thing I think was when I
[5487] saw that you were going to be here and
[5489] that you had like one of the winning um
[5491] metrics I thought oh wow this is great
[5494] so because it's like if you if folks who
[5497] traditionally haven't thought that
[5498] what's been doing in brain score is
[5499] actually science can participate in a
[5501] way that they think is important and the
[5504] rest of us will benefit from because you
[5506] know now we can test on your benchmark
[5508] right then that would be a really good
[5511] outcome right like I actually didn't
[5513] submit any metrics any any metrics to
[5515] The Benchmark because I was like it's
[5517] not important if I do right if like I
[5520] want people who have an certain
[5521] experimental hypothesis and have not
[5523] been engaged to to submit Benchmark you
[5524] know subm make submissions right I
[5526] hopefully I'll will submit things later
[5528] next time next time please please do
[5530] yeah yeah well I I just felt that like
[5532] it what we really wanted to test was
[5534] that we could see that if people think
[5536] okay brain score is stereotypically this
[5538] or that can see that independently of
[5541] whether they believe this
[5541] stereotypically they can participate and
[5543] they can change people's view of what
[5545] metrics they people should testing for
[5547] example if we've gone too far and using
[5549] natural stimuli then if they can submit
[5552] something that would be really uh
[5553] effective at model Separation by virtue
[5555] of using certain hypothesis testing
[5557] based stimuli that's the thing we really
[5560] want Janelle looks like you want to say
[5562] something I wanted to go back to your
[5563] original I wanted to go back to the
[5565] question but I yeah I agree with what
[5568] Dan was saying as well which um I so
[5572] which which I think your question was
[5574] was basically how do we take brain score
[5576] and use it to develop new models and I
[5578] think that the currently for me the most
[5581] interesting part of brain score and the
[5583] metrics of model comparison that we are
[5585] making right now is actually the
[5586] behavior and not the neural data um and
[5589] so I really liked the behavioral track
[5591] here because I think that the behavior
[5592] is really telling us ways that our
[5594] models are failing that are potentially
[5596] more interpretable than some of the
[5598] other measures that we have right now
[5601] where we can say okay well I mean
[5603] everyone uses sort of the texture shape
[5605] bias as one example right and so it's
[5607] like okay well this texture shape bias
[5608] is in a model so now we have an idea
[5610] that this is in there and so let's come
[5612] up with some way to fix it but once we
[5614] come up with that way to fix it I think
[5616] that we have to go back and still test
[5618] that model on for instance natural
[5619] images and it's really good to actually
[5622] test it on those neural predictions
[5624] because if we see that we fix the model
[5625] on this one specific type of data but
[5628] now it's failing suddenly on everything
[5630] else then then that that seems like we
[5633] we still need to make some improvement
[5635] we've like fixed something over here but
[5636] have really broken a lot of stuff on the
[5638] other side I actually want to quickly
[5641] follow up on Janelle so I think Janel
[5643] made this point which I was this has
[5645] caused me a lot of depression uh
[5647] thinking about science so I think Janel
[5649] made this point that like the behavioral
[5650] benchmarks were the most like intuitive
[5653] ones for experimenters to like act on
[5655] probably and I think this is the part
[5657] that really depresses me because I think
[5659] there's this notion that there's an
[5660] experimentor Who develops some
[5662] intuitions or insights and then is part
[5664] of this Loop that changes the whole like
[5667] you know contributes to the next move
[5669] and I think this is the same need that
[5671] drives you know interpretability for
[5673] models and all all that stuff so I to
[5675] while I totally agree that behavioral
[5678] ones are the ones behavoral benchmarks
[5680] might be the ones where we have a clear
[5682] idea what to do next because we had
[5684] access to behavior our own behavior
[5686] while designing those choices it might
[5689] turn out that not too far from now there
[5691] will be using a platform like brain
[5693] score there will be model suggesting you
[5696] know changes to to themselves and like I
[5698] feel like we can literally write down
[5700] all the moves that we can make in the
[5702] modeling you know parameters right now
[5705] with the existing knowledge about what
[5707] we what we know about the brain like
[5708] what are the comp other components in
[5710] different ways that we can combine and
[5712] some people might call that architecture
[5713] search or XYZ so as we get better at
[5716] that the game might just be you know
[5718] step out and just let this system you
[5720] know figure itself out and and I don't
[5722] know what will happen to my job or what
[5724] to the field at that point but I think
[5727] that's not too far
[5728] away okay um Jeff something quick you
[5731] want to say or I'm going to switch
[5732] topics uh well in terms of what I mean
[5736] the thing about doing hypothesis testing
[5740] uh in a directed way is it it does help
[5744] you know what ways in particular you
[5746] need to fix your model so when garos did
[5749] his study it was clear that we need to
[5753] build a shapee by it if you did if you
[5755] if you used if you if if you didn't have
[5757] his data set and you're working with the
[5759] brain score data set higher and higher
[5761] numbers you wouldn't know that there was
[5763] this problem with not perceiving shape
[5766] and emphasizing texture or you know you
[5769] wouldn't know that your model isn't
[5771] implementing uh gal principles well
[5773] enough so once you the good thing about
[5776] running experiments testing particular
[5778] hypothesis is it does give you a
[5782] direction about how to improve models
[5785] and and you know and just very briefly
[5787] to push back a little bit on Dan's point
[5790] I mean
[5792] it's the hypothesis isn't just that you
[5794] can predict the hypothesis I think that
[5797] people the CLA the conclusions people
[5799] are drawing is that these models are the
[5802] better the prediction the better the
[5804] model is in core object recognition and
[5807] so it's not just prediction it's a
[5809] particular type of prediction it's a
[5811] prediction that's giving insights into
[5814] object recognition so what you need to
[5815] do is do hypothesis testing on things
[5819] like well if this is a model of core
[5822] human object recognition does it care
[5824] about shape does it care about gastal
[5827] principles not it's not enough to say I
[5829] was just looking for better predictions
[5832] because the better predictions might be
[5834] the background it might be based on the
[5835] texture so you you need not you know you
[5838] the conclusions once draw you need to
[5840] have the corresponding hypotheses
[5843] assessed and I think people are making
[5845] strong conclusions about core object
[5847] recognition having not test the
[5849] hypothesis that it's the object not the
[5851] background that's driving prediction or
[5853] is okay so let's um setting a lot
[5857] there's a lot to comment on there but I
[5858] think in the interest of time let's move
[5860] to a more simplified form of this
[5862] constructive version of if you were each
[5864] to improve one thing on brain score what
[5867] what would you like just one thing and
[5870] these are concrete questions for some of
[5871] the engineers that are in the room what
[5873] what would it be
[5875] do we have to do it in one word well no
[5877] one thing not one word but one word
[5879] would be great if you could pull that
[5880] off um I would remove I would disband
[5882] the um like um composite like overall
[5888] score okay because I think that for
[5890] instance there were the model that was
[5892] shown as being number one at least in
[5894] the thing that was shown there is a
[5896] model out of my group but actually we
[5897] just my my student one he who I think is
[5900] here downloaded a model off the web a
[5902] particular architecture model and then
[5904] it it comes up as being the best model
[5906] but actually I don't really I don't
[5907] think any of us really buy that because
[5909] the way it comes up being the best model
[5911] is because it has a very high score on
[5912] some behavioral consistency and like not
[5915] quite such good scores on neurometrics
[5917] but somehow the aggregation process puts
[5920] that together so actually this is
[5921] related to to CO's showing at the end
[5924] which is who judges which model which
[5926] metric matters most and I don't think we
[5928] should be doing that all we should be
[5930] not aggregating or at least not
[5932] aggregating if the metrics have you know
[5934] pairwise um consistency that is not very
[5937] good maybe we you could look at the the
[5939] the consisten the the correlation to of
[5942] the metrics to get clusters or something
[5944] in a natural way okay that's separate
[5946] question but the aggregation I always
[5948] find that information if when personally
[5950] what I use brain score is I put one
[5952] metric lowlevel metric on one axis and
[5955] one on the other and that and that
[5957] correlation is really more interesting
[5959] to me than the score because and I
[5961] always find that the more disaggregated
[5963] the I put on the on the axis the more uh
[5966] interesting results I see so I would
[5969] remove this idea that there's a
[5970] competition to win the overall thing I
[5974] mean eventually when all the metrics are
[5975] correlated with for a set of models
[5978] those should be the best ones but um
[5981] right now since that's not the case I
[5983] think we are if we're trying to quote
[5985] beat The Benchmark I don't think we're
[5986] likely to get good insights and Rel
[5989] related question is basically um you
[5992] know uh
[5994] when when somebody is concerned about
[5995] say for example the one that co co
[5997] brought up is the hierarch the hierarch
[5999] you know the hierarchical
[6001] neuroanatomical consistency is wrong for
[6004] many models and I find that a really
[6005] important model metric and it was
[6007] actually one of the things that was like
[6009] good about some of the early models they
[6012] had that property um and I always look
[6014] at that metric myself if comput it
[6016] myself and if that's wrong I'm very
[6019] skeptical of a model so okay maybe I
[6021] other people don't care about that I
[6023] I've been trying tock Lobby for a metric
[6024] like that or for a while and we haven't
[6026] seen that I don't know why but hopefully
[6027] it's just a lot of work to put the
[6028] metrics together is basically a problem
[6030] but like we should not be aggregating or
[6034] maybe if we are aggregating right now it
[6036] should be in a much more smart way right
[6038] Dan says don't Aggregate and uh he
[6040] proposed some other metrics that you
[6041] guys should submit and also not make the
[6043] dumb aggregations the focus of the thing
[6045] so so that basically you end up not
[6048] getting Insight okay uh EV this is
[6051] inspired by a discussion with Greta T um
[6055] uh we think that having more flexibility
[6059] in how ceilings are computed or more
[6061] care in general about that es especially
[6064] given the differences between domains
[6066] for how that may work would be really
[6068] helpful but just to add to that also I
[6070] think um it would be helpful to try to
[6073] incentivize uh data submission in some
[6077] way because as of right now like the
[6079] most valuable things I mean models are
[6082] cheapish
[6084] all depends but data are really
[6085] expensive like data is what takes you
[6087] know painstaking you know many hours all
[6089] of you who collect data know this for
[6091] both animals and humans and then like
[6094] once we collect a data set my first
[6096] priority is to protect the interests of
[6097] the junior scientists who collected
[6099] those data and that may slow down this
[6102] communal process of trying to aggregate
[6104] this all in one place and I don't know
[6106] quite how to think about that yet or
[6108] just comment out what a better way than
[6110] to incentivize submission of data than
[6112] to have a benchmark competition with
[6114] prize money that's that's a cool idea
[6116] right so here we are um but there's
[6119] another point you mentioned about
[6120] incentives that if we have time i' like
[6121] to maybe return to but Janelle your what
[6123] would be the your one thing what would
[6125] you
[6126] improve yeah I think that um maybe
[6129] thinking a little bit about how brain
[6130] score could separate out the data sets
[6132] from the actual metrics that they're
[6133] being evaluated on and what I mean by
[6135] this is that we have various data sets
[6137] like you know the hbm the the V4 and it
[6139] data sets but you can evaluate those
[6141] using many different measures you could
[6142] evaluate them using regression you could
[6144] evaluate them using RSA and then even
[6146] within regression you can choose what
[6147] type of regression you're using um you
[6149] could be doing something which actually
[6150] would encourage some sparsity of
[6153] sampling from the various units of the
[6155] networks which maybe actually might be
[6156] more fair than something like a PLS
[6159] regression that is that is typically
[6160] used and so each of these methods are
[6162] going to have their own biases and it
[6165] would be very good to know whether
[6168] things are improving because we're
[6169] improving them only on one of these
[6171] metrics versus models are actually
[6174] improving because they're doing better
[6175] on all of these metrics for a particular
[6177] data
[6178] set okay
[6180] co uh for for me it will be usability
[6183] like user interface I think we should
[6186] like log the software engineers in a
[6188] room and not let them see the light of
[6189] the day whereas someone else who
[6191] actually like will be using it like as
[6194] another like researcher in this field
[6196] might be able to like communicate what
[6198] they're doing through the brain score
[6200] website to the community because I think
[6201] at the end if nobody uses it and and if
[6203] it it's the same five people who uses it
[6205] and we know who they are it's not really
[6207] like you know revolutionary for the
[6209] field so I think usability and user
[6211] interfaces for me the Top Choice yeah I
[6215] I think I agree with everything that's
[6216] been said here I guess the other obvious
[6219] one is just
[6220] including more benchmarks that are just
[6223] experiments that you know of the sort
[6225] that have been described here adding
[6227] more of those uh and not aggregating
[6229] over them but just studying them
[6230] individually that would be a real that
[6232] would be great
[6234] okay in that spirit and towards EV
[6235] comment too it's like more benchmarks
[6237] and as Dan pointed out and you many of
[6238] you point out the fuel of brain scores
[6240] the data and the benchmarks which is to
[6242] remind you is data seen through a metric
[6244] is what's referred to as a benchmark and
[6247] as Janelle or someone point out models
[6248] are are easier to come by and that um
[6251] but how to incentivize folks to submit
[6254] this is one venue to do that there's a
[6257] longer Range View that many of us hold
[6258] that like in it it should be rewarding
[6260] for scientists experimentalists to do
[6263] experiment whether it's hypothesis
[6265] driven or not that disrupts the models
[6267] and that was the spirit of this
[6269] competition and they should that should
[6270] be more important than writing a paper
[6272] about their data in a way is the field
[6274] that we many of us could imagine in the
[6276] future and so I'm looking I see ev
[6278] nodding like how do we do you believe in
[6280] that dream and how do we get to switch
[6282] from an incentive model which is tell a
[6284] story about your own data set you're a
[6286] grad student you got to you know push
[6288] the monkey around for two years and then
[6289] get some data and then tell a tell a
[6291] cute story that was hypothesis driven or
[6294] you submit your data set and disrupt all
[6296] the models that they all suddenly fall
[6298] to the floor on predicting something
[6299] that you collected whether it's
[6300] Behavioral or neural as a wow I'm now
[6303] that's an important result I've
[6305] disrupted the standard model of physics
[6307] kind of result right I've disrupted the
[6308] standard model of vision is sort of the
[6310] dream there or of language can we get
[6312] there and what do we need to do to make
[6315] that to make that incentive so that
[6316] people keep doing experiments for
[6318] exactly these reasons otherwise there
[6319] will be no fuel right any any thoughts
[6321] on that how to incen better this is an
[6324] attempt even this meeting I have no
[6326] answers it's a very hard uh question but
[6328] I just remember when I was um a graduate
[6330] student I think in my first or second
[6332] year Steve padosi who is now a faculty
[6334] at Berkeley said you know we should just
[6336] stop writing papers we should just put
[6338] up like the graphs like here's our
[6340] result and just let the field interpret
[6342] and I was like no no no no we should not
[6344] do this science is all about
[6346] storytelling and there have been many
[6347] cases where similar some day they have
[6349] been lying around and not until somebody
[6351] comes in with a particular lens thinking
[6353] about things in a particular way that
[6355] these data become important for in the
[6358] way that they have become important
[6360] later and I I don't know how like maybe
[6362] because I work on language but even
[6364] though you know we've shown that
[6365] language is separate from thought but
[6367] somehow it seems that putting a
[6369] scientific narrative into a set of
[6371] clearly articulated arguments I don't
[6373] see how numbers would ever replace this
[6375] but maybe I'm just very shortsighted
[6380] individual I I I agree I I guess I I
[6383] don't see why uh you couldn't disrupt
[6386] all of these benchmarks but then but
[6388] then also have you know your your paper
[6391] in whatever form it is which explains
[6394] what you did in order to do that what
[6396] the experiments were what the what the
[6398] story is like that seems incredibly
[6401] important because the code on brain
[6402] score it's we don't know if we're going
[6405] to be able to run it in 15 years um and
[6407] so at least having a you know having at
[6410] least a PDF which like generally
[6412] explains maybe not a PDF I don't know
[6415] however you want to store your files but
[6417] something just put the put the graphs
[6419] into GPT 4 yeah no I agree with you yeah
[6423] but just something you know so that we
[6425] can actually as a field look back on it
[6427] and say okay this is this is generally
[6429] what what was going
[6432] on u i I think that we should increase
[6436] the price money from 3,000 to like
[6439] 30,000 maybe like it's it's I think I I
[6442] actually honestly first of all I think
[6444] there's already a lot of problems to
[6445] solve this is like trying to tell
[6447] everybody else how to do things which is
[6449] nobody's going to like that so the way
[6450] to win them over is by increasing the
[6452] price money and I think then slowly
[6454] because then slowly the publication
[6456] strategies might be like I'll publish
[6458] one less paper this year but maybe
[6460] contribute to brain
[6461] score okay good I like your bluntness Co
[6467] yeah Jeff any thoughts on incentives or
[6471] you yeah ex retrospective that sounds
[6473] like a good plan uh no but but the the
[6476] general thing is I yeah I don't think
[6477] papers should go away so uh you know
[6480] it's great to have uh a score and brain
[6483] score and but have a paper associated
[6486] with each Benchmark and uh okay did
[6490] there's a little bit of time if we if if
[6491] anybody in the audience wants to direct
[6493] the the discussion anyway please step to
[6495] the mic and I'll call on you otherwise I
[6496] can I can keep asking questions that
[6498] these guys have been queued up for so
[6500] I'm just opening that invitation
[6502] actually it's 3:45 we have 5 minutes
[6503] left is that right Martin five minutes
[6506] or so at most if any has a question step
[6508] step up but it sounds to me that even
[6511] even Jeff I might say has started to at
[6513] least say there should be allowable to
[6515] have brain score as an available
[6517] platform maybe ideally fueled by
[6520] hypothesis driven experiments that then
[6522] get incentivized to be posted where
[6524] papers are also published alongside
[6525] those things if I could try to channel
[6528] your view in a constructive way given
[6531] the brain score Community does that is
[6532] that a fair
[6533] Fair summary or if I misspoke yeah I
[6535] mean it just doesn't feel to me that
[6538] yeah that feels doesn't feel like what I
[6540] imagine brain score was but yeah if if
[6542] what brain score became was a public
[6545] platform for making it easy to test
[6548] models against on key experiments uh
[6552] then that's and and then you don't and
[6553] you don't kind of compete to get an
[6555] overall score but you it's an
[6557] opportunity to make it easy to assess
[6559] your model on a critical experiment if
[6561] that's what brain score becomes I'm all
[6562] for it yeah okay great does anybody and
[6566] again we could going to end in a few
[6567] minutes here does anybody have any
[6569] parting thoughts of things in this
[6570] discussion that's prompted for them or
[6573] oh there is someone there okay go ahead
[6575] ask uh thanks for the great discussion
[6577] um I think it's very interesting that to
[6579] that we kind of like landed on this oh
[6581] multiple scores or multiple aggregate
[6584] scores not good because isn't that kind
[6587] of like you know ml scores or like even
[6589] you know original brain scores is one
[6592] score right right so I mean I'm not 100%
[6596] sure if this is what would Jeff would be
[6598] pushing
[6600] but isn't that against the idea of
[6603] having a the V Benchmark or a
[6605] competition at all if we're trying to
[6606] say oh what's the what's a good model
[6608] for V1 or it I mean there should be in
[6611] there are independent um experiments if
[6613] you like um and an AG score might not
[6617] even make sense anymore is
[6620] that kind of interesting point to to
[6624] discuss yeah to try to Channel that I
[6626] guess the question is yeah where do you
[6628] guys come down on the aggregate scores I
[6630] heard Dan say disand the leaderboard in
[6632] the aggregate score but I also know that
[6635] part of I hear people saying we should
[6636] check that everything worked on all the
[6637] old benchmarks so there's a question of
[6640] how we do the aggregation in different
[6642] ways but the the spirit of the platform
[6644] is to let's say unit test on everything
[6647] in the past and give scores on
[6649] everything to push towards models that
[6650] can explain across domains rather rather
[6653] than targeted for single domains so to
[6655] speak but that that may that does sound
[6658] like an aggregation once you sort of and
[6660] you need to summarize that so how do we
[6662] balance out the displaying all the
[6664] scores versus then you know combining
[6666] them to to give an answer of the best
[6668] integrative model so to speak what is a
[6670] strategy on I think that when the scores
[6672] are not highly correlated you shouldn't
[6674] be aggregating that way because it tends
[6676] to destroy information okay so if you
[6678] look at the correlation Matrix score
[6680] versus score you know across the model
[6683] and you see oh there's some blocks in
[6684] the diagonal you know block diagonals in
[6687] that Matrix those can be used
[6689] essentially to form clusters that you
[6690] might want to aggregate but since
[6692] actually it's the case that we still
[6694] don't know what those clusters are I
[6696] think I would not disband actually the
[6699] leader but I would just deemphasize make
[6702] you know for example in in computer
[6704] vision they actually don't aggregate
[6705] that way what they do is they have
[6708] several key things where they think
[6709] these are the things we need to get
[6711] better at and they they have little
[6713] subtracts of the competition like you
[6715] know Coco for instance has like
[6717] detection and localization this and that
[6719] okay um we should do
[6722] that okay any other quick thoughts and
[6725] we maybe could take one more quick
[6727] question from the audience I see and
[6728] then we're going to have to wrap up here
[6730] unless Janelle are you burning to say
[6732] something or no oh I was going to say
[6733] what Dan just said okay all right second
[6736] that okay go ahead please uh thanks for
[6738] the cool platform I think one of the
[6739] most understated benefits of this is
[6741] having a single API to access a bunch of
[6743] data sets so it's very difficult to like
[6745] go to indiv individual papers look at
[6747] how each person like um has their own
[6748] induc syncratic way of packaging their
[6750] data so just having access to the data
[6752] sets in the same format is already a
[6754] very very useful tool even if you don't
[6756] include the benchmarking at all and I
[6758] think improving the usability of the
[6759] platform and like encouraging people to
[6761] publish their data sets in the brain
[6762] score format would be a very strong step
[6765] I mean there are already a bunch of
[6766] existing data sets that just require
[6768] packaging it' be nice to incentivize
[6770] that as well okay I'm going to I'm going
[6772] to end on that positive note about data
[6774] sets and as you know there are more
[6775] mandates from the federal government to
[6777] post data sets there are more platforms
[6779] for data sets things like Dandy and
[6780] others and I know the brain score team
[6782] is working on porting those things so
[6784] that things flow naturally into
[6785] platforms like brain score in this
[6788] Spirit of open science and access so
[6790] thank you for highlighting that point
[6791] and I want to close today by first
[6794] thanking the panel so let's give a round
[6796] of applause to all these
[6801] guys and again I want to say the only
[6804] reason this platform really exists is
[6805] partly because Martin started it so I
[6807] don't know thank you to Martin
[6811] and and and the the rest of us are just
[6814] trying to help keep it going and I'm
[6815] glad to see the community growing and it
[6817] requires constant Community tending and
[6819] support and in all kinds of ways so
[6822] those of you are interested in
[6822] contributing to community please come up
[6824] to any of us afterwards and there's
[6826] always some ways to help you got big
[6828] Deep Pockets that'd be great we'll pay
[6830] for engineers but otherwise contributing
[6832] all kinds of other things on the code
[6833] base is exactly what what how makes this
[6836] thing work so please come up to
[6837] especially to Martin and the team here
[6839] to talk about those things I want to
[6840] thank everybody for attending this event
[6842] Martin did you have anything else you
[6843] want to say at the end or am I the end
[6845] here oh shirts yeah we got swag up here
[6847] so thank you guys all for coming and
[6849] we'll hang around thanks okay
[6854] bye thank thank you
[6864] looking for
