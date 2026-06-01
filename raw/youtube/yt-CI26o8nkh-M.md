---
schema_version: 1
id: yt-CI26o8nkh-M
type: youtube
title: Prof Dev Talk 2024 - Dr. Gemma Roig - On aligning machine and visual cortex
  representations
url: https://www.youtube.com/watch?v=CI26o8nkh-M
authors:
- Neuromatch
ingested_at: '2026-06-01T19:24:36Z'
content_hash: sha256:338fe6ffe8b86b24d7ebae5a5eb13d217691ae810591c9ba31304894210db6ff
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neuromatch
  channel_url: https://www.youtube.com/@neuromatchacademy
  duration_seconds: 3579
  caption_track: fetched
  snippet_count: 1270
filter:
  score: 0.75
---
[6] I I see that SS are joining so maybe a
[8] little bit we can wait sure
[41] okay let's get it started hello everyone
[45] um I am yal M and I will be moderating
[49] this um
[50] session um our um guest today is Dr jar
[55] Roy um from who is a full Professor uh
[59] in the department of Compu science at uh
[62] goate University Frankfurt um Jemma um
[66] before that was a an assistant professor
[69] in um um in the Singapore University of
[73] Technology and design and prior to that
[76] she was a postar flow at um the center
[80] for uh brains minds and machines at MIT
[85] um and uh she received her degree uh
[88] from eth um Z in uh computer vision um
[92] her research is
[94] interdisciplinary um and uh it um um
[99] tries to understand um the underlying
[102] computational principles of visual uh
[104] intelligence in humans and AI systems uh
[108] with the goal of um developing General
[111] AI um U Frameworks um so we are very
[115] excited to have you here Gemma um thank
[118] you for joining us and
[120] um we look forward to hear your talk
[124] yeah thanks yala it's a pleasure and
[126] honor being here and being able to talk
[129] about some of my work uh with you all um
[134] so I'm not sure if I'll be able to track
[136] the questions along the presentation but
[139] please feel free to ask along the way
[141] and I'll see if I can I can answer so
[145] like we can like I I ask the audience to
[147] put their questions in the Q&A and then
[150] after your talk we can uh go over them
[153] and discuss them but um uh I ask
[156] attendance please feel free to write up
[158] your questions as we go through the talk
[160] so you don't forget perfect excellent
[164] so um yes as uh y said I am Jemma and
[169] today I'm going to talk about on
[171] aligning machine and visual cortex
[176] representations and okay this is the
[178] last slide
[181] very
[183] good so I'd like to to start my talk uh
[187] by introducing object classification
[191] task uh which is the question of uh
[195] answering like what is in this image
[196] Which object is present in this image
[198] and here you see just like a a sample of
[201] a data set that's called imag net by now
[203] probably all of most of you will are
[206] familiar or will be familiar at some
[208] point um
[210] because it's a it's a very important
[212] data set that kind of also spark these
[215] new advances in Ai and also in
[217] computational
[220] Neuroscience so for for um tackling this
[224] task um there has been like a great
[227] advance in 2012 which the introduction
[230] of this um alexnet network based on
[233] deeper um deep
[235] learning and then over the years there
[237] have been also more uh advancements in
[241] these directions making the uh neural
[244] networks either deeper wider and
[248] changing some facts of the architectures
[250] that you see in the last one the visual
[253] image Transformers which are not a
[256] convolutional neural networks anymore
[257] but based on um self attention
[262] layers and here what you see is really
[264] the Striking result that the Deep
[267] learning approaches obtain with this uh
[269] imag data set that I introduced you at
[272] the beginning so before using deep
[275] learning networks mostly uh
[278] convolutional neural networks at the
[280] beginning so the the error rates were
[283] quite moderate uh but then with the in
[287] 2012 with this Alex net the error rate
[290] was dramatically reduced and then after
[293] that the researchers in the field
[296] started just to use uh more and more
[300] this technique to have better image
[303] classification
[306] results and of course um we know that
[310] specifically convolutional neural
[312] networks were inspired by how the visual
[316] cortech processes images specifically
[319] like the localization of the the
[322] processes starting with filters for
[323] instance and then uh building up
[325] representations through a hierarchy so
[328] they took the opportunity see also that
[331] even though these models were developed
[333] independently from how the brain works
[336] to bring them back and see how those
[339] could be used to really understand the
[341] brain uh and what are the processes that
[344] um are being done while um um observers
[349] for instance uh see some images and here
[352] you see one of the earlier works that
[354] showed that taking a model like alexnet
[358] which again was developed Ved
[360] independently from understanding the
[362] brain could actually explain a lot of
[364] the brain data variance much more than
[366] handcrafted models to targeting this
[370] scientific
[372] question so along these lines
[376] um and pushing more the boundaries of
[379] this project so there have been some
[381] efforts in which uh also emulating these
[384] challenges
[386] of um predicting or solving a task with
[390] a then giving a particular score and and
[393] so on so there there have been some
[396] efforts in putting up challenges also in
[398] computational neuro uh neuroscience and
[400] not only for instance computer vision
[402] like the imag net Challenge and one of
[405] them is this algon outs project and
[407] challenge which uh I've been
[410] co-organizing since 2019 with several
[413] other people and we um envisioned this
[418] as a project in which we could um build
[421] a platform for explaining the H human
[424] brain with algorithms in which
[426] participants would submit their models
[429] and their algorithms to explain
[431] particular brain data that we would
[433] create and that we would also design
[435] some score so for instance in 2019 we
[438] had the visual brain so it was mainly
[440] for object
[442] categorization and we had fmri and M
[445] data with a small reduced image set and
[450] then we used RS RSA that I hope you are
[453] familiar with uh as a as a metric for
[456] aligning brain and and and model
[460] representations as Benchmark and then we
[462] moved on in 2021 to include motion so we
[467] um recorded uh fmri data in this humans
[471] putting humans in the scanner for a
[473] large video set so more than 1,000
[475] videos um and then this time we used um
[478] as a benchmark to setting up who was the
[481] winner of the challenge uh with encoding
[484] models using the the percentage of
[486] variant
[487] explained and just recently uh last year
[491] in 2023 we had another one which is the
[494] we use nsds the natural
[496] SC data set um and this time it's like
[501] even larger data set with very high
[504] quality and also used encoding models so
[507] we had the typical setup of the
[509] challenge
[510] like with winners and a workshop
[512] inviting people to present their methods
[514] and then we could discuss uh how to move
[517] forward so just to give you a little bit
[520] of a teaser so there will be another one
[522] in
[523] 2025 probably it will be released in
[525] October this um October
[528] November and it will be also videos but
[532] using TV series so we envision that
[535] probably the models um can be even more
[538] interesting Beyond just
[540] images and short events and it will be
[543] fmri and also uh with encoding models so
[547] just keep
[549] tune so along these lines also going
[553] Beyond objects so what we wanted to ask
[556] so object recognition we wanted to to
[559] explore ourself in our own
[561] research let me see if I can get rid of
[564] that
[568] uh here just one
[572] second
[577] um I can just move it okay no I cannot
[580] move it so what we wanted to do is uh to
[584] explore uh different Vision task
[587] representations in the brain using also
[589] model representation so mainly our
[592] question that we pose is can we assess
[594] function of brain areas by Computing
[596] these correlates of the responses of the
[599] models uh of the of the brains to a
[601] large set of diverse models trained on
[603] different computer vision tasks so going
[605] Beyond only object categorization but
[608] also including other visual task which
[610] could be for instance um related to 3D
[614] information so how far an object is or
[616] if there is an occlusion or how objects
[619] are group and so
[623] on so how how we approach uh this so we
[629] uh had an stimulus hat that was used
[632] both for recording uh the FM responses
[635] of subjects of humans and also get
[639] representations of T specific DNN
[641] activation of train T specific DNN so
[645] what do I mean by by task specific so we
[647] had a set of dnns each of them train on
[651] different task and here you can see
[652] examples so for instance the first one
[654] that you see is the texture edges like
[657] detecting texture edges or Surface
[660] normal or S classification also of
[662] course object classification room layout
[664] and so on so one model per task and then
[668] what we wanted to find is how the
[670] representations of each of these model
[671] relates to representations of the brain
[673] in particular areas or in a search um
[677] light analysis fashion then get a
[679] ranking of it and find okay the the the
[683] representations of the models that can
[685] predict or that correlate better with
[688] the brain representations will be the
[689] one that are more related so we can uh
[692] link particular brain regions to the
[695] function that the model has been trained
[699] on um so for for the evaluation uh the
[703] of the DNN fmri comparison the
[706] representation level we used um what is
[709] called weighted RSA so mainly what you
[711] do is given some input here is X so it's
[714] an image you pass it through the model
[717] on one side or you show it to the
[719] participant in the the scanner on the
[720] other side and then you get
[721] representations either from the model or
[724] and the the subject and then you find
[726] the representation using RSA so you
[729] compute the rdms for the representation
[731] of the model the rdms for the
[733] representation of the
[735] fmri um responses and then in this case
[738] we use a regression because um we use
[741] two kind of representations of the model
[743] which is um the last layer and the
[746] previous one which is the most has
[748] related but this is just detail and then
[750] we can obtain a ranking and compare
[753] different models on how they can predict
[755] or um explain the variance of the fmri
[761] data um so for this uh what um we need
[765] of course is a set of models that have
[768] been trained with the same data set that
[771] have the same architecture and the only
[774] variable that changes is actually the
[776] task they have been trained on because
[778] then we can just
[781] um take into account this variable and
[784] validate that the function is actually
[786] the factor that really leads better
[789] explanation of the brain data so for
[792] this uh task there is this data set
[794] which is great which is the tonomy data
[796] set that also provides task models so it
[799] contains also more than million uh
[801] images that are an notated in different
[804] tasks so you can predict the output from
[809] one image um that relates to
[813] colorization the noising key Point um
[817] detection R shading object
[819] classification and so on so you can have
[822] one model as a as a proxy of one of
[825] these functions and then get the
[827] representation level that will relate to
[828] this
[829] function and this is on the model side
[832] and then on the fmri data site um we
[835] have our we had our data from a
[838] collaborator
[839] M boner bner and Einstein uh data that
[844] they use these indenes that are disjoin
[847] from the tonomy data set but still from
[849] the same data distrib distribution
[851] because both are indoor scenes that they
[855] use for studying navigational affordance
[857] in in an fmri study uh so they had
[860] individuated also some particular um Roi
[864] so they had localized them the ABC is
[866] the early visual cortex op paa PPA and
[868] RSC
[870] um scene areas so scene related areas in
[875] the
[876] brain and what what we wanted to do
[880] first is to see like which kind of
[884] functional map of the whole brain we got
[886] when we do a search like analysis with
[889] this T specific dnms with that with the
[892] weighted RSA to see first of all if the
[895] pattern is consistent and it's not
[898] random also if if the task is relevant
[900] so for instance we also took as a
[902] baseline a random DNN which is just like
[905] taking the architecture without any
[907] training and what we see is that the
[910] random DNN doesn't show anywhere so the
[913] second observation that we have is that
[916] the represent the models um that are
[920] related to to the task like for
[924] instance detecting to the edges key
[926] points and so on um mainly correlate the
[930] most in the early visual cortex which is
[932] also something that is well known in the
[935] literature and we also have the the DNN
[940] representation related to the 3D task
[942] like for instance surface normals or how
[945] far is an object from the camera and so
[946] on so forth in the dorsal
[949] regions which one could Loosely say okay
[953] this is like the wear uh pathway in a
[956] way uh and then the semantic DNN so
[959] where the semantic information is so
[961] what kind of object or what kind of
[964] scene it is it's more in the ventral
[966] regions and some of the
[968] oral so here I have to say that this was
[971] just selecting like the the model that
[974] give the highest correlation like there
[976] is no statistical analysis because we
[979] hacked 20 models that's a lot uh so what
[984] uh we did also separately is uh check
[987] the the nature and the predictive power
[989] of of this functional map by getting um
[993] different brain regions with an atlas
[996] and then predicting by subject and what
[999] we could see is that the variant explain
[1002] in nine of these rois is above 60% of
[1005] the lower noise ceiling which is
[1007] actually uh highly predictive as
[1011] well so what we can see with uh this
[1016] method is that different regions in in
[1018] the brain explained by these DNN
[1020] performing different task can unveil
[1023] functions of brain regions by comparing
[1025] with these multiple task specific models
[1028] and then consistently with the
[1030] literature so early regions better
[1032] explained by the 2D models so models
[1035] that predict to Def functions like Edge
[1037] detections there's dorsal regions by the
[1040] 3D models and the vental regions by the
[1043] semantic DNN and then this method also
[1046] has like a high explainable variance at
[1049] at Le in nine of the rois that we
[1052] analyze so it has a quantitative power
[1055] uh that it's it's quite um
[1060] remarkable okay and by the way we have
[1063] the code and the data so if you would
[1065] like to use part of it or um revalidate
[1070] our results so it's all
[1073] there so um another thing that we also
[1076] tackled is that so I showed you that
[1078] this approach
[1080] um um can do like a search light or a
[1084] particular ROI analysis with these
[1086] models uh and this is to localize so
[1090] where in the brain particular functions
[1092] are being
[1094] processed but this could also be applied
[1098] in the Dynamics so in bailing the how
[1101] the functionality changes over uh time
[1104] so what we did is um to find a
[1107] functional mapping in time with EEG so
[1109] we took the same stimulus set that we
[1111] had used with the fmri from our
[1114] collaborator and we recorded um um the
[1118] brain activations with EEG so here are
[1122] just some of the details that we use so
[1124] we had 16 subjects 75 repetitions for
[1127] each gatch with 15 runs um and and then
[1132] we had the task of asking the the
[1136] subjects if the arrow was pointing to
[1139] the same direction as the navigational
[1141] path in the previous image
[1146] okay so how did we do that so
[1150] actually the same exact methodology can
[1152] be used but instead of taking the
[1155] location in the brain to compute
[1158] particular rdms one can take the
[1161] location in time so compute the
[1163] representation the similarity Matrix for
[1166] each time window that we want to analyze
[1168] and then do the the same process again
[1173] okay um so we get the the model
[1176] representation the similarity Matrix in
[1179] the same manner as we got before but
[1181] here uh what we did that we also did in
[1184] the previous study but I don't have time
[1186] to show
[1187] you is uh to merge all the the models
[1192] that were representative of the 2D
[1194] functions with some technique that we
[1196] use to validate that this is the case
[1199] the ones with the 3D functions and the
[1201] one with semantics so we can distinguish
[1204] when to the information is process when
[1207] 3D information is processed and when the
[1209] semantic information is processed in the
[1213] Dynamics um and then we also use a
[1216] behavioral model that is the
[1217] navigational affordance model that was
[1220] actually proposed by by the original
[1222] paper that use this uh the original fmri
[1226] data because that's they were interested
[1228] in
[1230] um navigational affordance um and in
[1234] this case we also use it for for as a
[1238] comparison so that's the the metric that
[1242] we use for the alignment here so as I
[1244] said we compute the
[1247] RDM for each time point in the EG signal
[1250] so Windows of 10
[1252] milliseconds so we have one RDM per 10
[1256] milliseconds then we have the rdms
[1259] for the DNN
[1261] models that we combine we have the 2D
[1263] the 3D the semantic functions and then
[1266] also the navigational affordance
[1269] model and with this what we do is we com
[1272] we compute the unique variance so the I
[1276] didn't explain it here but the unique
[1278] variance mainly is um very similar to
[1281] the RSA but instead of just taking an
[1284] absolute value of how well one
[1287] particular model can
[1290] um correlates um with this uh the RDM of
[1295] a particular model correlates with the
[1297] RDM of the of the brain data so in this
[1300] um um metric in the unique variance what
[1303] you do is you regress out the
[1305] contributions of the other models that
[1307] you are comparing to so you can obtain
[1309] the unique variance okay so how uniquely
[1314] you can
[1314] explain factoring out the other um the
[1319] the other models what they bring the
[1321] other models so here what we see is um
[1326] um in blue the these unique variants
[1329] with the 2D uh
[1331] dnns in some green the 3D and then the
[1335] semantic and the navigational affordance
[1338] so if we analyze the paks and here you
[1340] can see it in the right hand side of the
[1344] plot okay so the 2D DNN shows the
[1348] earliest speak which is kind of expected
[1351] also it's reported previously in the
[1353] literature followed by the 3D and the
[1356] semantic DNN very closely even though
[1358] there is a bit of statistical
[1360] significance in when it
[1363] picks and finally the navigational
[1365] affordance model which is the latest so
[1367] with this what we suggest is that the
[1369] visual features are processed before the
[1371] navigational affordances in the human
[1373] brain at least in our setup and actually
[1376] this has been a disc going on in the
[1380] literature if it happens simultaneously
[1382] on one thing after the other so in our
[1386] experiments what we see is that the
[1389] representations of extracting 2D 3D and
[1391] semantic features are potentially used
[1394] for
[1397] Behavior so what we see is that the
[1400] correlation between the DNS with a brain
[1402] area and this is with fmri and the time
[1406] response that we got with the EG depends
[1408] on the task that the DNN was trained on
[1411] so the DNN models can be a potential
[1414] alternative to gain insights for
[1416] assessing a brain areas function or when
[1420] something is processed in the brain and
[1423] then what uh we are doing of course is
[1425] considering fmri data set with uh that
[1428] that have greater coverage and this
[1430] links to the algonot project as you can
[1434] imagine uh and also consider more
[1436] complex tasks than single static images
[1439] and now we are also using videos that
[1441] can maybe potentially give more
[1444] richness um to how we can do the
[1448] analysis so also to um Bridge um the AI
[1453] modeling and the
[1456] computational cognitive computational
[1458] Neuroscience we are developing this
[1461] toolbox that we call Net to brain which
[1464] is a toolbox to compare artifis models
[1467] it's not only Vision anymore we have
[1468] also llms and multimodal models with
[1471] human brain responses so it's for
[1473] facilitating this intersection of the
[1475] cognitive neuroscience and a research as
[1477] I said it provides functionality for
[1480] comparing representations of the neural
[1482] networks and brain activities and we
[1485] have RSA encoding models uh the unique
[1489] variant so all these functions that I
[1491] talked about already embedded there that
[1493] can be used it is python based and open
[1496] source and we are constant including
[1499] more data sets and DNN so some of the
[1501] data sets that I talk about are already
[1504] accessible from the toolbox but it's
[1506] also very easy to uh merge your own data
[1509] set and your own
[1511] model um yeah and it's already available
[1515] so I I'll just quickly go through one
[1517] example of the functionalities of this
[1520] net to Brand so we have implemented a
[1523] model taxonomy because one of the
[1525] challenges that we might face is like so
[1527] which models do I use for a particular
[1530] question and with a model taxonomy one
[1533] can say okay so I want models that have
[1535] the same architecture with this
[1537] particular architecture or a particular
[1539] task or a particular data set and then
[1541] you get all the models that are already
[1544] embedded there um in a table saying okay
[1547] so if you want this particular
[1549] architecture and this particular task
[1550] these are the available models that we
[1552] have
[1553] here uh and for the particular example
[1556] so what um we assess here is the
[1559] predictive capabilities of different um
[1562] language models so not large because
[1565] it's not like gbt but well we have gpt2
[1570] not that
[1571] large um then we can have like the
[1575] Second Step which is the data selection
[1577] in this particular example we use the
[1579] NSD uh the natural s data set uh the
[1583] step of the feature extraction so once
[1585] we have selected the models we can get
[1587] the model representations
[1589] um to to compute the
[1591] alignment uh on all the models that we
[1593] have
[1594] selected and then we can um find this uh
[1598] prediction in this case with linear
[1600] encoding but as I said one could also
[1602] use RSA or other functions to compute
[1606] this alignment and finally of course we
[1609] get some plotting to be able to
[1610] interpret our
[1612] results so here what you see is some of
[1615] the results that that we got with uh
[1618] this let's say almost a demo so we used
[1622] um
[1623] some um different models so we use B
[1627] which is an llm or an
[1630] LM um using the captions from the NSD
[1634] data set because it's based on on a data
[1636] set that contains captions and we have
[1639] functions for U passing this in N to
[1642] brain bir with word means that we only
[1645] take the the word of the class this is a
[1648] card or whatever object and then we also
[1652] use multimodel models based on clip
[1655] either the text part or the vision part
[1658] and then the G
[1660] gpt2 also for comparison as a as a
[1663] language model so what we see here is
[1666] that the the with the correlation
[1668] analysis uh with encoding model so how
[1671] it predicts the brain data so for V1
[1675] which is the top left so the vision
[1678] model is the one that predicts the best
[1680] and with earlier layers and then when we
[1684] while while we go through the plots so
[1686] from left to right and bottom to town
[1688] what we see is the progression of the
[1690] layers so what you see for each model is
[1693] all the layers um so early layers to the
[1696] left and later layers to the right so if
[1699] we see the vision models we see the
[1701] progression of the layers on how they
[1702] can predict the different brain areas
[1705] and also how the the language models are
[1708] increasingly predicting with higher with
[1711] higher predictivity the the brain
[1714] responses along the hierarchy of the of
[1716] the brain
[1718] regions
[1720] okay so one of the things that is also
[1722] intriguing is like okay we have a some
[1725] intuition of how these models work and
[1727] we might understand why this is the case
[1730] uh that there is this progression in
[1732] productivity but we might not know
[1734] anything because or everything because
[1736] these models are also a bit of black
[1739] boxes so another kind of efforts that we
[1741] are doing in the lab is trying to go
[1743] inside the models in particular here we
[1746] focus on Vision Transformers to try to
[1748] understand what are they really
[1750] Computing and what are the
[1753] representations uh representing in a way
[1757] um so I just uh want to mention that
[1761] here there is this work by Marina that
[1763] she is analyzing with uh visual
[1765] Transformers and how they build up
[1767] information along the
[1769] thearchy of the model to come up with a
[1772] decision and then she can also analyze
[1775] what is the role of context what is the
[1777] role of the of the actual object for
[1780] building this final decision and and
[1784] also like the different components of
[1785] like the the tension layers of or the M
[1789] MLP layers and so
[1792] on and this method also allows to go
[1796] back to the input image and then okay so
[1799] this model made this decision and it
[1801] focus on this particular areas in the
[1804] image for instance and this potentially
[1807] can also help understand like if there
[1809] is a particular alignment so how it
[1813] really like the attention that it puts
[1815] here it might be related to what is
[1817] being processed also in the
[1821] brain um but of course like doing such
[1825] interpretability is something that is
[1828] being done in cognitive Neuroscience
[1831] since many years so that there are a lot
[1833] of um uh challenges that have been
[1837] already addressed or discussed in in the
[1840] cognitive Neuroscience community that
[1842] should uh or that we can bring back to
[1846] how we can interpret AI models because
[1848] it's also kind of like very similar
[1850] blackbox thing uh with very different
[1853] implementation approaches of course so
[1856] we have also position paper on what what
[1859] do we need to do or what are the
[1860] challenges and implications of decisions
[1862] for interpreting the models and how we
[1864] can use these
[1866] interpretations so I just want to
[1868] conclude by saying that um so there are
[1872] a lot of efforts bringing AI to uh
[1875] cognitive Neuroscience uh to unveil
[1878] functionalities of the brain or or
[1880] different mechanisms on how the brain
[1883] processes information but that we can
[1885] also take insights from uh um
[1889] Neuroscience or cognitive Neuroscience
[1891] back to AI both either for building
[1893] better models or also as methods to try
[1896] to understand better the models that we
[1898] already
[1900] have and with this I'll conclude my
[1904] talk thank you very much Emma for very
[1907] um insightful talk uh and I see already
[1912] lots of questions and
[1914] Q&A um so we can go through them thank
[1917] you very much
[1920] okay um the first question is um about
[1924] the algonaut projects and they ask how
[1928] exactly is it checked that the models
[1930] are similar to how the brain works uh
[1934] are the Dynamics of the models somehow
[1936] compareed to dynamics of the brain
[1938] basically they need more information
[1940] about how this uh alignment test is
[1943] bench yeah yeah of course that's that's
[1945] a great question and of course this um
[1948] since it's a challenge we we had to make
[1950] some decisions because we wanted to have
[1953] one score that could determine a winner
[1956] um because we have a leaderboard of
[1959] first uh position second position and so
[1961] on so forth so in the first edition of
[1965] the challenge that we had both fmri and
[1967] Ms what we did is how the model
[1970] representation it's it's not really the
[1972] Dynamics of the of the model because the
[1974] the model usually is a static so the
[1976] only thing that you can do is either you
[1978] use several models or you or the you I
[1981] mean the participants or different
[1983] layers for different brain regions of
[1985] this they can do it's up to them um but
[1989] what we really do is like once they have
[1993] the the representations that they want
[1995] to compare to the brain then we either
[1999] use RSA with the rdms of model and brain
[2002] data or the encoding model in the later
[2005] editions we have been using encoding
[2007] models for that because we have like
[2009] much larger data sets
[2013] um yeah the next question is also
[2015] related to that asking uh why you
[2018] decided to change from RSA to percent
[2020] variance explained in the next round yes
[2024] sure
[2025] so I mean this is a big
[2028] debate of which metric is better and I
[2031] mean we know that different metrics can
[2033] give us different Insight like for
[2035] instance in the RSA we can have more
[2038] more information about the the geometry
[2041] of the representations and in a way it's
[2043] a bit more crude um and with the
[2046] encoding methods you have more like the
[2049] prediction the actual prediction and and
[2051] you have there a bit more flexibility of
[2054] combining representation so you you
[2056] assume in both cases that you have two
[2058] different subspaces and somehow you need
[2060] to um um align them and and these are
[2065] just two different things so when we
[2068] move to larger data set so using an RSA
[2072] has some
[2073] limitations um that you cannot really
[2076] use the whole set for instance and also
[2078] the way the data has been recorded we
[2082] also seen that it has a huge impact so
[2084] for instance the amount of repetitions
[2086] amount of subjects and so on so you have
[2089] different constraints on how you want to
[2093] get like a high predictivity using one
[2095] or the other um so since lately we have
[2098] been using much larger data sets um and
[2104] yeah so we've we've uh used in coding
[2108] models thank you and the next question
[2111] is more fundamental about like what does
[2113] representation in the brain and model
[2116] mean is it simply some pattern of
[2118] activations at a single point in time
[2121] yeah that's that's a great uh question
[2124] so in the model domain this is quite
[2128] straightforward because once you have
[2132] some stimulus you pass it through the
[2134] model and a stimulus can be a video or
[2137] it can be an image or it can even be
[2139] some part of the text and so on and then
[2142] you get activations along the layers of
[2145] the model so that's a representation in
[2147] the model so it's the activations that
[2149] you get when you process the input
[2152] information in the brain what we have is
[2156] really the neuronal patterns that we we
[2158] get either from the fmri so okay not
[2160] directly the neuron the neuronal
[2162] patterns if it's
[2164] fmri um in particular locations of the
[2168] brain
[2169] um which in fmri is integrated some in
[2173] some interval of time of course but it's
[2176] again um um so the representation is the
[2181] activation that you get as as a readout
[2183] let's say when when the subject is
[2185] looking at the stimuli and if you have
[2188] like the time domain then you have the
[2190] representation that is dynamically
[2192] changing also over time and since you
[2194] have more time resolution then that's
[2196] what you care about it's not more about
[2198] the particular location in the in the
[2201] brain but where it
[2204] happens thank you um the next one is um
[2209] can you give an example of what was
[2211] explained by these models and what do
[2213] you mean
[2215] explain yeah that's a great question
[2218] so I mean there are several aspects of
[2221] that so for instance in the first work
[2223] that I presented that we were using
[2226] different DNN stain on different
[2229] functions on different visual task so
[2232] what we use is really the DNN as proxies
[2235] of functions so the
[2239] this explain is like um is the function
[2244] specific that or or selectivity in this
[2248] case of which particular brain region or
[2251] where in time this function is being
[2254] processed or there is a process that um
[2258] happens leading to the output of of this
[2261] particular function so for instance we
[2263] um are edges being extracted or more
[2266] related to Tod um information or is like
[2270] the 3D information that is being process
[2272] and so on so forth so this is one one
[2275] aspect of it another angle um which is
[2280] also related to what um a lot of people
[2283] are doing and what I showed in the nin
[2286] example is um another thing that could
[2289] be is it more low-level information in
[2293] the sense of uh more grounded to Vision
[2296] or can semantics because its
[2298] representation extracted from language
[2301] models uh be more informative for
[2304] instance and how this changes along the
[2307] key of the brain so it depends also on
[2309] the variables that you change in the
[2311] model because at the end of the day the
[2313] models are your hypothesis and you need
[2315] also your n hypothesis uh to be able to
[2319] to do this
[2321] comparison thank you um what happens if
[2326] you have Foundation model which is
[2328] trained on multiple tasks would that
[2331] increase or decrease the um variance
[2336] explained so yeah that's also a very
[2339] good question so I think it depends on a
[2341] lot of factors so first of all it
[2343] depends on which data we are talking
[2345] about so which kind of stimuli we are
[2347] talking about which uh brain areas we
[2351] are um analyzing or doing the alignment
[2356] on um so it might be that in certain
[2361] aspects probably it will increase so we
[2364] have seen also that um
[2368] maybe clip can be considered a
[2370] foundation model in a in in a sense
[2373] because it's been train with a lot of
[2374] data and also on selflearning so we have
[2377] seen consistently that these kind of
[2380] foundational models that are multimodal
[2382] align better or can uh predict better
[2385] the the brain responses so in general
[2389] yes but the important scientific
[2391] question is why so we need like some
[2394] basic comparison of um why is this the
[2398] case or is it because I also have text
[2401] and then the semantics are embedded
[2403] through the the visual representations
[2405] as well so we can do some comparisons
[2407] with that with having like a similar
[2409] architecture with only Visual and then
[2411] compare this to the visual stream of the
[2413] multimodel for instance or is this
[2416] because of the data so ideally we could
[2418] have like another model trained with a
[2420] different kind of data and then uh
[2422] compare this because also consistently
[2424] people have reported that the data this
[2427] distribution that has been used during
[2429] training of the models has a huge impact
[2432] on the alignment more than the
[2434] architecture for
[2436] instance thank you um the next question
[2441] is I'm just wondering is there any
[2444] computational difference between DNN and
[2447] the human brain in processing the image
[2450] statistics of an effective scene and its
[2452] classification in terms of villance and
[2454] AR Rosal
[2458] um inbalance
[2460] and okay so of course I mean there are
[2465] probably a lot of different uh
[2468] differences in computation so um if the
[2472] results are not like
[2475] 100% um so they the the model
[2478] representations cannot really predict
[2480] 100% of the variance of the data so
[2482] there are a lot of differences still
[2485] that we need to fill the Gap and even if
[2487] it's 100
[2489] per at the representation level might be
[2492] the same but we can never be sure that
[2495] how it got there the the the mechanistic
[2498] uh or the algorithm that that compute
[2501] the representation is it's actually the
[2503] same so that the actual computations is
[2505] the same unless we have like a very fine
[2507] grain analysis of of the
[2510] processes
[2513] um and of course um the model a choice
[2517] limits you on what kind of computations
[2519] you are assessing so if a one chooses to
[2523] use only like a image recognition model
[2526] then that's the only thing that you are
[2528] assessing and you are not uh taking into
[2530] account other aspects
[2533] um like valence and arousal I think that
[2536] was the the
[2539] example okay thank you um in is net to
[2544] brain compatible with intracranial um
[2547] EEG or single neuron
[2550] data uh yes it
[2553] is um as long as you can treat it
[2558] as I have this data and I can get this
[2560] representation so we commonly worked
[2564] with fmri EEG and M but it is completely
[2569] transferable and it can be adapted
[2572] adapted let's say and if somebody has
[2575] troubles uh we we are happy to help
[2578] thank
[2579] you um the next question is a good
[2581] question are the alignment results
[2583] statistically robust across the andn
[2586] training runs uh it um examples
[2589] different seeds or different data sets
[2592] for the same vision task uh IM for
[2595] example image classification with uh
[2597] image net or cifr 10 yeah so that's a
[2601] great question
[2603] because the the data set that one uses
[2607] for training the networks is actually a
[2610] variable so it's not robust to that and
[2612] it's really dependent on which data set
[2614] you use for training the networks on how
[2617] much the alignment will be meaningful
[2620] and will be um uh will will have like
[2625] more a predictivity or will explain more
[2628] of the variance and this is something
[2630] that we have uh tested so for instance
[2633] just to give like a very good example if
[2635] one is interested in identifying for
[2639] instance objects and then uses a objects
[2644] outdoors and then uses only SC data sets
[2647] that contain no objects that were shown
[2650] uh or similar objects that were shown
[2652] and and it it's all indoors so the data
[2655] distribution is very different and
[2656] actually the models have only picked
[2659] patterns during training related to the
[2661] training set so this can really bias the
[2664] results one of the things that one I
[2667] think need to be consider and be very
[2669] careful about is like which kind of
[2671] models and which kind of data one uses
[2674] and this is something that one can also
[2676] test with this hypothesis testing so you
[2678] can have like the same data sorry the
[2681] same set of models but only changing the
[2684] kind of data that you have and then you
[2686] can see the
[2688] differences um this is one thing and
[2690] also the task also influences a lot of
[2693] course and and we leverage this fact in
[2696] our studies right so this is one of the
[2698] the things that that we that we used for
[2702] for the disentanglement of of the
[2704] different functions in different brain
[2707] areas did you test any like how the
[2710] representation alignment would change
[2712] for various um like for different
[2714] initialization of the model like as they
[2717] as like different
[2719] seats yeah across different runs yeah
[2722] yeah so this is desired but it is very
[2726] computational
[2728] expensive so we didn't do that actually
[2731] so we what we did is compareed to the
[2734] random uh to the random initialized
[2738] model and then
[2740] on for instance on another another
[2743] project that I didn't present what we
[2745] did is to test for different kinds of
[2747] architectures so what I mean is that the
[2751] comparison is always within the same
[2753] architecture but then you can do
[2755] multiple multiple comparison to see how
[2757] robust is this two architecture and then
[2760] in this case you can use also smaller
[2764] architectures an easier to train uh to
[2767] be able to tackle the computational
[2769] cost okay thank you um what other
[2774] network models other than DNN Could Be
[2777] Imagined to describe biologically
[2780] plausible brain
[2781] architecture um maybe also next to
[2785] visual processing
[2789] um yeah that's that's a that's a great
[2793] question so actually the there are there
[2796] is now a lot of work that is mainly uh
[2799] using DNN uh because uh you can get
[2803] these very powerful representations that
[2805] both achieve very high accuracy in
[2807] Behavior which is also quite important
[2811] uh for getting good alignment as we have
[2814] seen and has been reported also by other
[2820] um so what I think people are more
[2824] exploring is like how can we really
[2826] change the
[2827] architectures such that they are more
[2830] biologically plausible because in a way
[2833] it seems that the the AI field is
[2836] converging to less biologically
[2838] plausible like think about Transformers
[2840] or at least at the conceptual level
[2842] right even though the alignment is
[2844] greater and this is also like a puzzle
[2846] that we have
[2848] um but there are also some trends that
[2850] say let's try to constrain and make them
[2853] more biologically plausible like for
[2855] instance uh with having some constraints
[2857] on on the topography or having some
[2859] constraints on on how it process
[2862] information over time um and so on and
[2866] there are also efforts that are um
[2870] Divergent from the uh deep learning um
[2875] comparison let's say but then they
[2877] usually tackle like specific cognitive
[2880] task and how these are being processed
[2883] in the
[2885] brain okay thank
[2887] you um how would the analysis pipeline
[2891] change if you were to use sound or
[2894] speech instead of videos or like added
[2896] sound to the videos yeah
[2900] so we have done that actually in the
[2904] example that I uh that I showed in the
[2906] net to brain so we use language for
[2910] instance uh as one way of
[2912] comparison uh so from The Human Side
[2916] there is no change right because you can
[2918] get also FMI responses mg responses just
[2922] the the nature of the stimulite changes
[2924] right so instead of having images or
[2926] videos so you have sound or you have
[2929] text this is on one side and on the
[2932] other side what you need to change of
[2934] course is the kind of models that you
[2935] use so you cannot use a or
[2938] you have to adapt a vision model I
[2940] wouldn't say you cannot use it um if you
[2944] if your input uh stimulus is audio for
[2948] instance right so the set of models that
[2950] you have to use are just targeted or
[2953] that can ingest the input stimulant and
[2956] in net to brain we have also Audio
[2959] models and video models with the
[2962] multimodality input and the language
[2964] model so the pipeline like the concept
[2967] that the concept of the pipeline doesn't
[2969] change the details that are
[2973] important
[2975] thanks uh one ask how to approach you
[2978] for further
[2980] questions oh just send me an
[2983] email okay thank
[2986] you
[2989] um do you have comments on the notion of
[2992] privileged um representation
[2995] representation access in the brain and
[2997] how that would impact the field in terms
[3000] of
[3001] literature uh measuring alignment um via
[3006] correlation of activations as suddenly
[3009] the correlation isn't a straightforward
[3011] metric the order of the access matters a
[3014] lot and they provided a p paper link so
[3018] I'm I'm I don't know like if you have
[3020] you seen that I haven't so I need to
[3022] check
[3023] that yeah I don't see the the link but
[3026] but yeah I mean of course one one
[3030] question is like we we have
[3032] representations and we are Computing
[3034] correlations um or even with encoding
[3037] models is like these
[3038] predictions and of course these metrics
[3042] are not perfect and each of them have
[3045] their own advantages and their own
[3047] limitations so there is also like a
[3050] stand of resarch said like how we can
[3052] get better Matrix so what so on one hand
[3056] I think we've been
[3058] advancing quite a lot using these
[3060] techniques but even though they have
[3061] these
[3062] limitations uh and one of these could be
[3065] could be that right like one could get
[3066] like a very high correlation and and it
[3069] might be just like cofounders and not
[3071] the actual features that that drive the
[3075] correlation and it could also be biased
[3077] by data set and so on but then on the
[3079] other hand we've also been able to
[3081] understand quite a lot so I don't think
[3083] that we need to stop this but rather put
[3086] more efforts in enhancing the methods
[3089] and and and being able to answer more
[3092] scientific questions in a more
[3093] meaningful
[3095] way thank you um do you think that these
[3099] representation of models would change in
[3103] case if person um were moving if I'm not
[3106] wrong movement includes some awareness
[3109] of a space around you I think they are
[3111] referring to your um scena study and
[3114] that they are looking at like
[3116] affordances and the scene and how it can
[3118] probably process like basically if you
[3121] put people in the scene rather than like
[3124] just perceiving the same yeah yeah so I
[3127] think
[3129] that the task that and behavior that the
[3132] person is
[3134] performing will affect the
[3136] representations probably and this is
[3138] like an interesting question that one
[3139] could ask and actually we've been
[3141] thinking about it so you can even in in
[3145] the static experiment you can ask uh um
[3148] participants to perform different tasks
[3150] like to either identify objects or to
[3154] try to imagine them themselves
[3156] navigating or do different things right
[3159] so I do think that that there is an
[3161] impact here right um to to what degree I
[3166] I'm not sure I guess this is something
[3168] we can hypothesize and then uh see if it
[3172] holds with
[3174] experiments thank you um
[3177] what types of encoding models have you
[3180] used and which ones were most
[3183] successful so I mean in what we usually
[3187] do is just pure linear encoding so what
[3190] it means is that you have particular
[3193] model representation so you have a
[3194] particular architecture that you can get
[3196] the activations and then just do linear
[3199] encoding and this is kind of like the
[3202] crudest way of and the simpler way of
[3205] getting the the encoding model because
[3208] it's just like the the linear
[3210] transformation from one space to another
[3213] so for instance I can say that there are
[3216] others including participants in Alon
[3218] outs that what they did is use the DNN
[3221] as the encoder model itself so really to
[3225] predict the brain data okay so there are
[3228] different things you can learn with this
[3230] approach which I think are also great
[3233] like for instance one Beyond predicting
[3236] of course because one can predict just
[3238] for predict like getting better
[3241] predictivity score but also for instance
[3244] we had a participant uh that could trace
[3249] back so was predicting different
[3250] activations of different brain areas and
[3253] then could trace back like okay for this
[3255] particular brain region this input this
[3258] part of the image was was driving this
[3260] prediction and then things like FFA um
[3265] was getting information from faces and
[3267] so on so forth so this is something that
[3270] that he could uh unveil from his
[3275] method okay thank you um the next
[3279] attende asked very cool work I'm not the
[3283] most familiar with visual processing but
[3286] I would imagine the salience of the
[3288] simile might influence which brain
[3290] regions are recruited I'm curious if
[3292] your team is looking into this Maybe by
[3295] scoring the salian of the saliency of
[3298] the image but I imagine this would vary
[3301] greatly from Human to human
[3303] too yeah so at the moment the seleny per
[3306] se we are not assessing so one thing
[3309] that we are linking to the
[3311] interpretability of the model so the
[3313] model can also pick up certain regions
[3317] of the image for the processing towards
[3319] the final decision and this one could be
[3321] kind of like the the selency of the
[3323] model in a way which emerges from the
[3326] model itself self and this is what we
[3328] are trying to look into but uh yeah so
[3332] one uh one could think about of a more
[3334] complex model to try to incorporate all
[3337] these all these parameters I think that
[3339] would be really
[3341] cool thank you um I think um this we at
[3348] most can take one or two more questions
[3350] um are all internal um representations
[3354] of different kinds of models llms Vision
[3357] uh converion to a common space uh for
[3360] example a representation of an apple in
[3363] vision and llms uh would be similar or
[3366] very different basically from different
[3368] modalities I think you're
[3371] asking um so I okay so I think that um
[3377] there are different um aspects in this
[3380] question so one thing is if you
[3383] have
[3385] um a multimodal model um it depends on
[3389] how it integrates the information so if
[3391] it integrates from the very early visual
[3394] then you have this convergence since the
[3396] very beginning at the
[3398] model um level and then what one could
[3402] say is like if I have models that
[3404] integrate information at different
[3406] levels as different hypothesis how this
[3408] correlates with uh or how this aligns
[3410] with the different brain
[3412] regions uh what are the differences and
[3414] then you can see okay so this is really
[3417] like having like more semantics in this
[3419] brain region um and it's here it's
[3422] really converging like what is um more
[3425] the understanding of of the scene than
[3428] the lowlevel features for instance and
[3430] so on so forth um so at the model level
[3433] if you have so it really depends on on
[3435] how the the model is is learned because
[3437] if you have like different modalities
[3439] and they are all different streams and
[3441] only the alignment is done at the at the
[3444] last layer so you will have like very
[3446] align representations in a common space
[3448] at the last layer but at the very
[3450] beginning you will have like very domain
[3452] spec so very modality specific
[3455] representations let's say and then one
[3457] can can use this knowledge to to do the
[3459] alignment with the brain and see how how
[3462] it's uh in the brain in comparison to
[3464] the
[3466] model okay thank you and this will be
[3468] the last question that we can take when
[3470] the time um which DNN models can better
[3473] explain or model the dorsal pathway in
[3476] visual cortex can you name some of them
[3479] based on your
[3481] experience well I
[3483] mean what what I have seen in in the
[3487] results that I showed you is that models
[3490] that are more related
[3492] to um Global structure 3D representation
[3497] so really um a little bit also on the
[3501] semantics but even abstracting from the
[3503] SE from the semantics and having like a
[3506] more
[3507] uh understanding of uh the the position
[3510] of the object so really preserving
[3512] structure and so on this is what we have
[3514] observe that are more predictive uh in
[3517] in the
[3518] dorsal uh stream and then from there one
[3521] could really try to to craft it a little
[3525] bit more on specific functions that one
[3528] one can
[3529] hypothesize um but yeah I would say like
[3532] more more 3D and and maybe a bit of
[3537] motion as well okay okay thank you very
[3540] much Jemma for your time today like um
[3544] it was amazing the talk and also the
[3546] discussion we got many questions and we
[3549] almost went through half of it and there
[3552] are still more questions but
[3553] unfortunately we cannot take all of them
[3556] um anyway thank you very much uh for
[3559] your time and uh insightful talk uh I'm
[3563] sure everyone um enjoyed uh both the
[3568] talk and also the discussion that we had
[3569] afterwards um yeah everyone Thanks for
[3574] attending was a pleasure thanks for your
[3576] questions
