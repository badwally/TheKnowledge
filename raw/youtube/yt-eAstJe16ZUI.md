---
schema_version: 1
id: yt-eAstJe16ZUI
type: youtube
title: ANNs as Models of Language Processing in the Brain (Greta Tuckute)
url: https://www.youtube.com/watch?v=eAstJe16ZUI
authors:
- OnNeuro
ingested_at: '2026-06-02T00:37:05Z'
content_hash: sha256:d2a354a232a2299fa999b11251c749fa3df8bd88c072c6b27bbe13925fababeb
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: OnNeuro
  channel_url: https://www.youtube.com/@onneuro2132
  duration_seconds: 4043
  caption_track: fetched
  snippet_count: 1826
filter:
  score: 0.8
---
[0] um so joining us today i am i'm stoked
[3] we have greta takuta
[5] so greta is a phd candidate at mit and
[8] she's working with dr ev federenko who
[10] we just had the pleasure of
[11] hearing from last week um before mit
[14] though greta received her bachelor's and
[16] master's degrees
[17] in molecular biomedicine which is cool
[19] from the university of copenhagen in
[21] denmark
[22] and we were just talking about earlier
[23] about how all of her a lot of her
[25] publications have
[26] handsome co-authors which made me smile
[28] um her research combines neuroscience
[30] artificial intelligence and cognitive
[32] science to study semantic processing
[34] and temporal dynamics in the brain but
[37] when she's not busy sciencing and being
[39] cool on all those domains
[40] she's also an award-winning photographer
[43] and an avid reader of magic realism
[45] books i i looked at your
[46] your reading list i noticed your recent
[48] one was i have no mouth and i must
[50] scream which sounds both terrifying and
[52] intriguing
[54] yeah please this is great please welcome
[56] me are joining me in welcoming greta
[58] takuta
[61] thank you so much for the nice
[62] introduction and thanks so much for the
[65] opportunity
[65] to speak today i'm really excited and
[68] nice to virtually
[70] meet everyone so yeah today
[73] i will be speaking about artificial
[76] neural networks
[77] as models of language processing in the
[80] human brain
[81] and this is a result of a collaboration
[85] with martin shrimp another grad student
[87] at brain and cognitive sciences at mit
[90] um edan blanc who is now faculty at ucla
[93] and then two other grad students also in
[95] brainerd and cognitive sciences at mit
[97] karina kampf
[98] and ekbar hussaini and then it's
[100] supervised by dr nancy kenwicher
[102] dr josh tenenbaum and dr f federenko
[106] and yeah everything that i'm presenting
[107] is obviously a product
[109] thereof
[112] um so i think for for everyone who has
[115] not
[115] lived under a rock in the last couple of
[118] years
[119] you've probably seen uh titles like this
[123] uh basically all these papers trying to
[126] merge
[126] uh artificial intelligence neural
[128] networks deep learning
[130] with neuroscience cognitive science and
[133] psychology
[134] and obviously the idea that neural
[137] networks can
[138] serve as theories of neural computation
[141] it's not new uh in the 80s doing the
[144] apparel distributed processing movement
[147] with these connectionist networks um
[151] these networks were already being
[153] proposed to be like solutions
[155] to problems in perception memory and
[157] language
[158] um but it didn't move much further at
[160] that point
[161] um so now there's like a huge like surge
[164] in this like interest
[164] of using these like neural networks um
[167] as models of like perception and
[170] cognition so this
[174] a lot of these papers mention notions
[177] such as
[178] we are interested in comparing the
[179] representations between neural networks
[182] and the brain and that sounds great
[184] that's exciting
[185] but to me that also sounds kind of vague
[188] so this brings me to the outline of this
[190] talk and i would really like to
[194] first give an introduction to using
[196] artificial neural networks
[198] a n as models of perception and
[200] cognition
[202] then i would like to present some
[203] preliminary results
[205] in the domain of language and
[208] also how can we exploit these networks
[211] and can they actually teach us something
[212] about
[213] language and cognition and lastly i
[216] would like to take this vague notion of
[217] comparing representations from neural
[219] networks
[220] uh to the brain and try to like
[223] make it more um make it more evident
[227] what is actually going on when you
[229] compare these representations
[230] um to talk some more like methodology
[233] and
[234] feel free to just like unmute and
[236] interrupt if you have any like
[237] clarification questions um i try to like
[241] in the
[242] uh final part of my talk to like uh
[245] recapitulate some like discussion points
[247] i hope we can leave like further
[248] discussion for the end but definitely
[249] just unmute and ask if you have any
[251] any questions
[257] all right so the idea of using neural
[260] networks uh to model perception
[262] um started especially in the visual
[265] domain
[266] so this is a paper by yemen sadal from
[269] 2014
[271] where they state that they can use these
[273] hierarchical models
[275] as we now know as convolutional neural
[277] networks to model responses
[279] in the private visual ventral stream
[283] and in this experiment they used
[286] responses from macaque monkeys from the
[291] i.t from the inferior temporal cortex
[295] and they showed different images uh from
[297] various
[298] uh categories and then what we see in
[300] the bottom part
[301] here is uh in black the actual neural
[304] responses from the macaque brain
[307] and in red we see model predictions from
[309] these convolutional networks
[311] and i think it's important to highlight
[313] here that
[314] these red traces are not just like a
[316] fitted model but it's actually like a
[318] held out um prediction uh on like an
[322] unseen test set so we see these models
[324] actually
[324] do pretty well what they also found
[327] which is
[328] is pretty interesting is that there is a
[330] connection
[331] between task performance and as we're
[334] like in the visual domain then
[336] here task performance was image
[338] categorization performance so how well
[340] some of these neural networks could
[342] categorize images
[344] and then on the y-axis we have like the
[347] um
[348] the explained variants in the i-t cortex
[350] so the neural explained variants
[352] and what they found was that there was a
[354] relation between these two
[356] meaning that models that perform better
[359] in this like image categorization task
[361] also map better onto the brain and
[363] basically they
[364] so this suggests that using performance
[368] optimization
[369] um can also be used to build these like
[372] quantitative predictive models of neural
[374] processing
[377] and then i had a slide where i wanted to
[380] talk about
[381] why is this a good idea but after some
[383] time i changed it to uh
[386] is this a good idea and
[389] now i actually decided that we're gonna
[390] leave this for the end so i'm not even
[392] gonna talk about that now
[395] so the scope of this talk is that we
[397] have seen that these
[399] artificial neural networks have worked
[401] well in modeling the
[402] sensory cortex for instance visual and
[404] auditory processing
[406] and now we basically wanted to ask can
[409] we exploit these
[411] networks to inform us about high-level
[413] language processing
[414] in the human brain and here by language
[418] processing i
[419] refer to the extraction of meaning from
[422] spoken or written phrases sentences
[425] stories
[426] so this uniquely human ability is kind
[429] of an interesting domain because
[431] it's it bridges perception and high
[434] level reasoning
[435] so this is what i'll focus on in this
[437] talk
[440] and to investigate whether you can map
[441] these neural networks with the brain we
[443] use an approach called
[445] benchmarking so in the top part of my
[447] slide
[448] you can see different stimuli in this
[451] case because we are talking about
[452] language these are sentences
[455] and the basic idea is that we want to
[457] present these sentences
[459] to models and to humans so these are our
[462] experimental subjects
[464] so we basically want to present
[466] identical stimuli to the models and to
[468] humans
[469] and then see how do the internal
[471] representations compare
[474] so in the lower part of the slide here
[476] you can see that we have
[478] we present some sentences we extract
[480] model activations and then we want to
[482] compare
[483] it to the neural recordings from the
[484] human brain and i'll go more into depth
[486] of that
[488] so to start out i'm just gonna talk a
[490] little bit about
[492] the human system of interest in this
[494] particular case
[496] and here we're interested in the core
[498] language network
[500] and uh yeah i heard that dr fedorenko
[502] gave a talk last week
[503] so to the ones who are there you
[505] probably already know a lot about
[507] it but just a quick recap um
[510] the core language network is a set of
[514] left lateralized regions um mainly like
[517] frontal
[518] and the frontal and temporal part of the
[520] brain that support
[521] high level language processing and this
[524] is beyond like the low level auditory
[526] and visual perceptual stage
[530] and the way we define this network is by
[533] using a contrast
[534] for instance an fmri it can also be
[537] applicable to other modalities
[539] so a contrast between sentences
[543] and uh non-words so by doing this we
[546] want to define like i put
[547] like these participant specific
[549] functional regions
[551] as the core language network because um
[554] as dr feliwinko has shown previously
[557] there are like a lot of intrasubject
[560] anatomical variability
[562] especially when defining these regions
[563] so it's probably sub-optimal to just
[566] like
[566] define them in like a anatomical
[569] stereotactic space so these are
[570] functionally defined
[573] so in our particular work we used
[577] a data set this is our main data set
[579] which was an fmri data set
[581] from a paper pereira at all from 2018
[586] and in this paper subjects were exposed
[589] to visually presented sentences
[592] so in particular 627 sentences
[596] and we had 10 unique subjects
[599] corresponding
[600] to approximately 13 000 voxels in each
[602] subject
[604] and by having this data set we can
[607] construct
[608] a stimulus response matrix here they
[611] stimulate our sentences
[613] and the response are the voxel responses
[615] from the human brain
[617] so in this case we would have these like
[619] 627 sentences
[621] as the rows in the matrix and then
[623] columns we have the voxels across the
[625] participants
[628] and this is like a small example of some
[630] of the sentences
[632] beekeeping encourages the conservation
[634] of local habitats
[636] these sentences were all like
[638] naturalistic sentences they were kind of
[640] like
[640] wikipedia style they were spanning like
[643] a broad range of topics
[645] and were presented in like small
[646] passages of like three or four
[648] sentences within like the same topic
[654] so now we talked about the human data
[656] set
[657] so i'm just gonna briefly talk about the
[659] models that we were interested
[661] in and in our approach
[665] we actually investigated 43
[669] diverse state-of-the-art artificial
[671] neural network
[672] models for language i'm not going to go
[675] into like a lot of depth and like
[676] describing these models
[678] we can talk about it later if somebody's
[680] interested but
[681] briefly we had three categories
[684] of models uh one is the embedding type
[688] of models
[689] um i guess some of you are probably
[690] familiar with like glove and word to
[692] back
[693] um and the next uh category
[696] was these like more recurrent networks
[699] like lstms
[700] and then by far the large the largest uh
[703] group of models
[704] was these uh transformer architectures i
[706] think we have
[707] 38 transformer architectures um so these
[711] span
[711] both like the bird family xlm t5 albert
[714] gpt
[716] and these names just refer to different
[717] like sub-category families of
[719] transformer models
[721] and these um transformer models
[724] are these like architectures that have
[726] really like revolutionized like language
[728] modeling within the last couple of years
[730] and they transform one sequence into
[732] another with the help of like two parts
[734] so there's an
[735] encoder and a decoder part um but
[738] it's really efficient because it has
[741] like attentional mechanisms
[742] so it performs really well on like
[744] language modeling tasks
[746] um just kind of a
[750] question from the chat um
[753] um what is the reading level of the
[756] stimulus sentences
[759] so um the sentences were presented one
[762] sentence at a time
[764] if that's the question um
[767] i think maybe you like that or the how
[771] correct me if i'm wrong in what you're
[773] asking james
[778] um if it's the reading level
[780] corresponding to like how difficult the
[782] sentences are
[783] um i actually don't know exactly which
[786] like metric i would
[788] like classify that as um sorry but
[791] it was like very like naturalistic type
[793] like similar to what you would find like
[795] in a
[796] simple like wikipedia article so it
[798] wasn't like super simple sentences but
[800] it wasn't obviously like
[801] really like syntactically or
[802] semantically challenging
[807] awesome i i actually also had a question
[809] about these
[810] um language models um so
[813] forgive me because uh i am
[817] you know kind of new to um a ns
[820] in general um so i'm wondering like
[823] what this like potential attentional
[826] like component
[827] is that you were talking about and like
[829] i i think um last year we did
[832] i had we had some exposure to like the
[834] word to vec like models but
[836] like where like where is the attention
[838] coming in
[840] um in this all right
[843] um that's a good question um so in these
[846] like transform models you have like
[847] these like two structures like the
[849] encoder and the decoder
[851] and the attentional mechanism comes into
[853] play that
[854] the model kind of like says like skims
[857] through like a sentence find out what
[859] are like the important things to focus
[860] on
[861] and then kind of like passes that
[862] through the network so you always like
[864] know
[865] oh now this particular part of the
[867] sentence of interest
[869] and then continuously like updates it's
[871] like
[872] embedding to like optimize the
[874] performance
[876] this was like a very short explanation
[879] because these networks are
[881] wildly complex um
[884] but actually yeah but yeah this slide
[887] was on like the objective function
[888] on all these like language models which
[891] is yeah what is language modeling
[893] and i just like illustrating that here
[895] uh which is
[896] um basically a task of predicting the
[899] next word
[899] or character in a document so what all
[902] these like language models uh
[904] try to do is to maximize the probability
[907] of seeing the next word
[909] or minimize perplexity and perplexity
[911] here is like you know kind of like a
[912] value of like surprisal
[914] so you want to be like as little
[917] surprised as you know possible um
[921] when you like model these things
[924] um and just like another short comment
[927] if anybody's interested in either
[929] reading or working with these like
[931] transformer models
[932] um then this library called hugging
[934] phase transformers
[936] is incredible in terms of implementation
[938] and they also have some really good like
[939] guides as to like
[941] what do they do how can you extract a
[943] perplexity metric
[944] how can you tokenize it's like they have
[947] really really good resources for that so
[949] i can definitely recommend so
[950] a huge shout out to these um this
[953] library
[953] because some of these models as you can
[955] probably imagine are
[957] both like wildly complex and really hard
[959] to implement so they really made this
[961] task much easier
[964] and last comment about the models is
[967] that
[967] um we kind of like had two goals in mind
[970] by choosing these models
[972] the first one was you know can these
[974] models even like predict neural
[976] responses
[977] and the second one was do they predict
[980] differently
[980] can we distinguish them like is there
[982] any difference between them
[986] cool so now we have an idea of like the
[988] models and the human recordings
[990] so now an important point is well how do
[993] we want to compare these things
[997] and to do this we want like a proxy for
[1000] like a similarity score
[1002] and on the left hand side we see again
[1005] sentences
[1006] as rows and model activations as columns
[1009] the model activations depend on
[1010] exactly which model you have and then we
[1013] have the brain
[1014] recordings in red here and what we chose
[1017] to do
[1018] uh i would love to discuss this like
[1020] further um
[1021] in the end of the talk because there are
[1023] many ways of doing this
[1024] but the way that we did it was to fit a
[1027] linear regression so just like a simple
[1029] linear regression
[1031] from the model activations to the brain
[1033] recordings
[1036] and then what we do um we take we fit
[1040] this model on sorry on 80
[1042] of the data so it's basically like a
[1044] k-fold cross-validation like a five-fold
[1047] um and then we have like a held out
[1051] twenty percent
[1052] uh model activations and based on this
[1055] we try to predict
[1056] the brain responses so this refers to
[1059] like an encoding approach
[1061] where you know you if you think about it
[1063] you are kind of like trying to ask you
[1065] know
[1065] how much neurally relevant information
[1068] is
[1069] present in these like distributed model
[1072] activation representations
[1075] and then when you have a predicted
[1078] brain response you can basically just
[1080] measure the pearson correlation
[1082] like an r value between the predicted
[1085] and then the actual brain response
[1087] and that is what we denote as our like
[1089] similarity score
[1092] and then a thing you're like well which
[1095] granularity does this happen on like
[1097] what do you fit it on
[1098] and um yeah sorry so of course
[1102] uh the last slide um
[1105] so i wonder the because there are
[1108] different models uh so
[1110] i wonder the their
[1113] this model must have different like
[1116] number of
[1116] units because you calculate the weight
[1119] of
[1120] this unit so i just wonder if
[1124] if they are have different number of
[1125] units or they have
[1127] actually approximately similar uh like
[1130] layer or units that's my first question
[1133] and also another question is do you mean
[1137] the cross validation do you held out the
[1140] subject or skill
[1144] right those are two great questions
[1147] um to answer your first question
[1151] in terms of how big are these like model
[1153] activation units whether they're
[1155] approximately similar in size
[1157] it's a really good consideration and
[1159] questions because they're not they're
[1161] not identical
[1162] for instance some of the embedding
[1163] models they would have like dimension
[1165] 300 and some of the like larger
[1167] transformer models have dimension
[1169] like uh one of them has like 700
[1172] something then
[1173] i think the largest embedding size we
[1175] have is 1600 which is the gpt2 excel
[1179] model
[1180] so they do vary and this is a really i
[1183] think uh
[1184] interesting thing to discuss like how
[1186] does like the model size
[1187] actually matter for like downstream like
[1189] interpretation of your results
[1191] yeah good question and your second
[1194] question in terms of what we are fitting
[1196] it on maybe my next slide will answer to
[1199] some of that let me know if it doesn't
[1201] um so here we work with like
[1204] fmri data so i know this plot is on the
[1208] surface but we work with like volumetric
[1211] uh etheremida so voxels and we basically
[1214] uh we're fitting um
[1218] one model per voxel so we would get one
[1221] score
[1221] one correlation value for every single
[1224] voxel
[1225] for every single participant and i think
[1227] maybe what you were asking
[1228] will also was kind of this slide
[1231] possibly
[1232] which is then all right we have like
[1234] these like correlation scores
[1236] across uh subjects so let's say in this
[1239] example we have
[1241] three subjects that perform the
[1242] experiment so we get
[1245] a correlation score for each single
[1247] voxel
[1248] for each single participant across all
[1250] these like three subjects
[1253] then what what do we do with that um
[1256] so what we chose to do was um let's say
[1259] like the first
[1260] x number of correlation values here
[1263] corresponded to the ones from subject
[1265] one
[1266] and the next one is from subject to and
[1268] from structure three
[1269] then we take the median within a subject
[1272] so you would get
[1274] one's productivity score here for
[1276] subject one
[1278] the next one for subject two and then a
[1280] third one for subject three
[1282] and then the last step to get like an
[1284] aggregated value
[1286] is then to take the median of those
[1288] subject-wise values so we end up with
[1290] you know
[1291] one predictivity metric
[1295] so now we're sure all right that's got a
[1298] clarification question uh so
[1299] you're doing the model activations
[1303] you're talking specifically about like
[1304] the output nodes or
[1306] relating uh like sub layers as well
[1310] right this is also a great question
[1312] because
[1313] as you mentioned some of these models
[1315] some of the models only have one layer
[1318] some of the models have 12 layers some
[1319] of the models have like 30-something
[1321] layers
[1323] so we actually treated every single
[1327] layer
[1328] as a model so meaning that if you have
[1332] layer
[1332] number 10 in a certain uh big model
[1336] then we would use that particular layer
[1338] to actually extract activations from
[1340] that
[1340] layer that being like the hidden states
[1343] of that layer
[1344] exactly so for the larger models say we
[1347] have like
[1348] um one of the gpt models that has 12
[1350] layers you're actually like kind of
[1352] investigating
[1353] 12 different models
[1356] okay thanks cool thank you
[1361] yeah so now we have this like aggregated
[1362] productivity metric so
[1364] now we're almost ready to see like how
[1366] well do these
[1368] models then fit but because obviously as
[1371] we all know neural recordings
[1373] are inherently noisy
[1376] they have different like signal to noise
[1378] ratios
[1379] uh we wanted to kind of like normalize
[1381] this score
[1382] so that we kind of like divided by like
[1386] the upper bound
[1387] of how noisy the data set it like how
[1389] well can we
[1390] expect to even predict um
[1394] so to do that we have like a normalized
[1397] predictivity metric which is that
[1399] aggregated productivity i just mentioned
[1402] divided by an estimated ceiling and the
[1405] estimated ceiling
[1407] is like an extrapolated reliability of
[1410] that particular data set
[1411] which kind of like places an upper bound
[1413] of like how well
[1415] given the noise in the data set can we
[1417] expect to predict the data
[1419] so for this particular data set we found
[1421] there is an asymptotic relationship
[1423] around seven subjects and
[1427] then we divide all our we normalize
[1430] all our productivity values by this
[1432] value of like 0.3
[1436] um so here is i guess
[1440] a result or a
[1443] part of the results which is on the
[1446] x-axis we have the different models that
[1448] i explained
[1449] uh before and on the y-axis we have this
[1452] predictivity metric
[1453] and as we see the models are able to
[1456] predict the neural data
[1458] to varying degrees uh what is
[1461] interesting to see
[1462] is that here on the right hand side the
[1464] blue bars
[1465] this is the gpt2 family
[1469] i don't know if somebody has been on
[1471] like reddit or twitter or something
[1472] you've probably seen the hype about
[1473] first gpt2 and then there was this site
[1476] called talk to transformer and now
[1477] there's cpt3
[1479] um so yeah it has received kind of a lot
[1481] of attention but what we find
[1483] is actually that gpt also maps pretty
[1486] well
[1486] onto the brain um
[1490] so now we saw that but um
[1494] i think an interesting point to talk
[1496] about is like
[1497] all right we see that we have these
[1499] models that can somewhat reliably
[1501] predict the newer recordings
[1502] then like can that teach us anything is
[1504] that even interesting like
[1506] what can we do with that um
[1509] and in order to answer that question
[1511] i'll quickly want to like take a step
[1513] back
[1513] and think about the question that we
[1516] initially wanted to ask
[1517] which was like what are the mechanisms
[1520] that are underlying
[1521] human language comprehension and this is
[1525] an example of like a core goal in
[1527] neuroscience
[1528] where you know you have like some
[1530] stimuli some input
[1532] to the human brain and then you go to
[1534] like extract some kind of meaning from
[1535] it
[1536] so can we actually use these like neural
[1538] networks to help us like
[1540] answer that question
[1543] um and i'm gonna go over
[1546] four three different uh points and the
[1550] first one will be
[1551] do these models like even generalize can
[1553] you like
[1555] take another data set and have the same
[1558] uh predictivity um are they reliable
[1561] like or are they just like
[1562] is it just like lucky that they fit our
[1564] data set
[1565] another point is that do they map onto
[1568] some like task performance as we saw in
[1570] vision
[1571] and the third point is that can we use
[1573] these models to teach us something about
[1575] different brain regions
[1577] and the last part is can we dissect
[1580] these models
[1580] and like mechanistically start asking
[1582] like what makes these models like fit
[1584] well to the brain
[1587] so first tapping into the first question
[1590] um so i was explaining we have this like
[1593] benchmarking approach
[1594] and in order to like figure out whether
[1596] this actually generalizes
[1597] we would want to have many neural data
[1601] sets
[1602] and we refer to this approach as like
[1605] integrative benchmarking
[1606] so we're trying to find some things like
[1609] a model that can explain
[1610] several data sets and not just a single
[1612] one
[1614] and in the optimal scenario we would
[1617] not only have neural measurements but we
[1619] would also have
[1621] different types of neural measurements
[1622] behavioral measurements
[1624] so we could imagine having both like
[1626] fmri data sets
[1628] intracranial recordings eg meg
[1631] uh behavioral say like reading times who
[1634] would have like
[1634] an integration of different metrics that
[1637] we could then call like a brain or human
[1639] score
[1641] so in this particular work
[1644] we had two additional data sets that i
[1647] will briefly talk about now
[1650] so in addition to the pereira data set
[1652] which was this
[1653] fmri data set we had a data set with
[1657] intracranial recordings so in this case
[1660] we had
[1661] five subjects who read pretty simple
[1665] sentences eight word long sentences
[1668] presented one word at a time given like
[1670] the increased
[1672] temporal resolution of the e-cock
[1675] responses
[1677] and then next we had another fmri
[1680] dataset
[1681] which was different from our first fmri
[1684] data set
[1686] in the sense that here subjects were
[1689] reading
[1689] stories so it was not like fixed
[1692] sentences
[1692] it was literally just like a story and
[1695] it was also presented auditorily as
[1698] opposed to
[1699] visually in the prayer paper um so this
[1702] data set which is from blank it all
[1704] uh 2014 here we also had five subjects
[1708] and then they were divided into like
[1709] different story fragments
[1711] that we were then trying to predict
[1717] and as i mentioned an interesting thing
[1719] to look into is like how well do these
[1721] like
[1722] productivity scores then correlate
[1724] across data sets
[1726] and the first plot i'm showing here
[1729] is kind of an easy like slightly easier
[1732] more simple comparison
[1734] because uh in the pereira data set that
[1736] i've been talking about the last
[1738] 15 minutes um we there were like two
[1742] sub experiments so there was one
[1745] experiment which was
[1746] um say like 250 sentences then there was
[1750] another one
[1751] that was like 350 and a different set of
[1755] subjects performed these experiments but
[1757] the materials were somewhat similar they
[1759] were not identical they were like new
[1760] topics new sentences
[1762] uh but first we checked whether like
[1764] these two scores correlate well
[1767] and fortunately we found that great they
[1770] actually correlate really really well
[1772] so what about the harder comparison
[1774] which is for instance generalizing from
[1777] the
[1777] fmri the pereira scores to the federance
[1781] data set which was the e-cog data set
[1783] and we also still do see that there is a
[1786] correlation
[1788] not as strong and lastly generalizing
[1792] between the
[1793] two fmri datasets we also see that
[1796] there's a correlation
[1798] in the like predicted values
[1802] yet uh it's interesting to see that in
[1805] this
[1805] other fmri data set that would that
[1808] consisted of these like naturalistic
[1810] stories
[1811] um it was generally predicted lower than
[1814] our other other data set um which could
[1817] be due to several reasons
[1819] um because maybe some of these models
[1821] like lack this like long
[1823] range uh context or other reasons that
[1826] we could
[1826] discuss too um
[1830] so all right there's some
[1831] generalizability obviously
[1833] in the optimal scenario we would have
[1835] many more data sets
[1837] um and they provide different you know
[1839] strengths to like validating this
[1841] approach
[1842] so next um question about
[1844] generalizability
[1846] yes does this and maybe there's like
[1849] something here that
[1850] um like maybe there would be identical
[1852] but
[1853] um if you train it the opposite way like
[1856] say you train it just
[1858] using the blank data set um
[1861] is the is the relationship the same or
[1865] is it
[1865] is it stronger perhaps so
[1868] say you would train these models just on
[1870] one data set and then you would try to
[1872] generalize to other data sets
[1875] yeah that sounds really really
[1878] hard i wish that was possible
[1882] no i think i think what you're pointing
[1884] out now is like an ultimate goal
[1886] for sure that you would predict on
[1888] something and then you take
[1890] another data sets like that's completely
[1891] independent and then you would basically
[1893] use that as like the held out thing
[1896] that is would be incredible
[1899] um but from i think what we have seen
[1902] is that it is actually still a
[1905] quite challenging task so
[1909] we are cross-validating across sentences
[1911] but if you start cross-validating across
[1913] like larger chunks of data
[1915] so you say you pick out like eight
[1917] sentences or like a full topic
[1919] and then you want to generalize that
[1921] within the same data set
[1923] it's definitely harder than just
[1924] sentences so
[1927] ultimate goal yes i guess maybe a
[1930] follow-up to this
[1933] um kind of pushing
[1935] pushing the limits here potentially but
[1938] like
[1938] so you have like you know these like
[1940] cross domains like visually presented
[1942] then auditorily presented
[1943] but have you considered using like
[1947] i don't know say like a movie data set
[1949] where like there is auditorily
[1951] presented word stimuli um but there's
[1954] also these like rich visual components
[1956] that are happening that are also kind of
[1957] creating
[1958] meaning for the subject um and then
[1960] feeding just the text
[1962] to the model right
[1966] um no i think this is a really
[1968] interesting point and i'm actually very
[1970] very interested in this like multimodal
[1972] perceptual integration
[1975] yeah i would love to do that so we
[1978] haven't looked at it at all
[1979] um i've i've been thinking a little bit
[1982] about like
[1983] how one could do it you know there are
[1985] like certain models
[1986] language models that are trained on
[1987] visual input um
[1990] i think i've mainly looked at like image
[1992] type of networks so they learn to like
[1994] look at an image
[1995] extract like a visual embedding and then
[1997] you go from a visual embedding to like a
[1999] textual embedding and then to predict
[2000] text
[2001] and yeah i've been like pretty curious
[2004] as to you know can you
[2005] use that embedding to then predict the
[2007] language responses
[2008] because we always like most often
[2011] um encounter language in context with
[2013] other modalities right so there should
[2015] be
[2016] some really interesting link there yeah
[2018] this is something i'm very interested in
[2019] pursuing further for sure
[2022] thanks cool thank you
[2025] um so yeah now i'm just gonna briefly
[2028] talk about
[2029] uh task performance and just to remind
[2031] us um
[2033] in the visual domain we saw this like
[2034] pretty interesting link
[2036] between like um image categorization
[2039] and neural productivity and now we can
[2043] ask is there like
[2044] a similar link in language
[2047] and as i briefly explained earlier
[2050] in language modeling we use perplexity
[2053] as like a metric so the lower complexity
[2056] you have the better your model is
[2057] performing on this
[2058] next word prediction task which is the
[2060] goal of language modeling
[2063] um so we looked at here on the x-axis we
[2066] have this like perplexity metric
[2069] uh called like a next word prediction
[2071] benchmark uh which is on a
[2073] data cell data set called wikitex2 which
[2076] is like wikipedia articles
[2077] so basically asking how well can these
[2080] models like predict the upcoming word in
[2082] this like data set
[2083] um and here notice the axis is flipped
[2086] so lower is better and is on this end
[2090] and on the y-axis we have these like
[2093] three
[2093] neural data set aggregate datasets
[2095] aggregated
[2097] and what we find is that there's
[2099] actually a relationship between
[2100] the performance of these language models
[2103] and then
[2104] the neural productivity um
[2107] so one might think all right that's cool
[2109] but maybe
[2110] you know these it would take any metric
[2113] maybe and maybe it would just correlate
[2115] like
[2115] maybe this is just like a lucky
[2117] coincidence right um
[2120] so what we did was that there is a like
[2123] a
[2123] suite of like language evaluation tools
[2126] called
[2126] glue which stands for general language
[2129] understanding
[2130] evaluation and this like they have like
[2133] different benchmarks for testing
[2135] um different sentence understanding
[2137] tasks
[2138] an example could be like negation like
[2141] lexical
[2142] entailment analyzing like the sentiment
[2145] of the sentence
[2147] so then we tested whether our neural
[2150] predictivity was like correlated with
[2152] any of these tasks
[2153] and we actually found that it was
[2155] non-significant
[2157] so therefore we see that there is like
[2158] as uh selectively
[2161] uh like the neural response selectively
[2163] correlates
[2165] with this like performance on the next
[2167] word prediction task
[2169] so this might suggest that optimizing
[2172] for these predictive representations
[2175] could be like a critical shared
[2177] objective goal
[2179] of both biological brains the human
[2181] brain
[2182] and then also artificial neural networks
[2184] for language
[2189] next i would like to pinpoint um
[2194] whether we could possibly use this model
[2196] to teach us anything about
[2198] brain regions because in vision you know
[2200] there's like somewhat like a coarse
[2203] mapping of like the different processing
[2205] you go from v1 to v2
[2207] and so on and there's even like
[2209] anatomical um
[2211] data on that so there's like somewhat a
[2213] mapping between
[2214] function and anatomy this in more like
[2217] high-level language processing is still
[2219] pretty unclear and debated you know how
[2221] exactly these like regions interact with
[2223] each other
[2225] um so basically like can we
[2228] can these like models like guide us
[2230] towards maybe understanding what
[2232] different regions of like the language
[2234] network are doing
[2237] and um what we see here is across
[2241] just like five different subjects uh we
[2244] see their
[2245] surface uh projected language regions
[2248] uh the top uh two rows here
[2251] uh is the model uh predictions
[2254] from glove this like embedding type of
[2256] model and the
[2258] color scheme here uh corresponds to how
[2262] how well the productivity is so we see
[2265] that in general as you also saw on the
[2266] bar plot that glove predicts
[2268] the regions pretty poorly uh somewhere
[2271] maybe on like some temporal regions it's
[2274] predicting better maybe we can maybe it
[2278] suggests
[2278] that oh like this optimization goal for
[2281] glove which is co-occurrence
[2283] is possibly represented in certain areas
[2288] and similarly this is like the
[2289] productivity map for
[2291] gpt 2xl which was our top performing
[2294] model in fmri
[2295] and we do see that overall it performs
[2298] pretty well but there are still
[2300] some regions that are maybe predicted
[2302] better than others
[2304] um that being said it seems to be
[2308] that there's a lot of like variability
[2309] among subjects so it's pretty
[2311] challenging to draw like
[2313] any like clear conclusion from this but
[2315] this is just to illustrate that
[2317] you know possibly you could use this
[2319] tool to look at oh if you predict
[2321] uh region a of the brain pretty well
[2323] with this model and this model was
[2325] optimized for task b then possibly
[2328] um you could start extracting more like
[2331] mechanistic links in that way
[2335] um so in your last
[2338] slide because we know the language is
[2341] left letterized
[2342] so is it like natural to
[2345] expect maybe you have better
[2348] productivity
[2349] in the left hemisphere or it's
[2353] it's not an assumption
[2358] i think this is a it's a good question i
[2360] think it's
[2361] it's definitely a reasonable assumption
[2364] uh
[2364] for sure that you would predict better
[2366] in like the left
[2368] letter left in the left regions
[2373] i can't remember whether we looked into
[2376] comparing left versus right
[2379] um i mean you can of course like eyeball
[2382] and be
[2382] like oh maybe like left is predicted
[2385] better than right but i actually cannot
[2387] recall whether we looked into it
[2388] consistently but i think it's like a
[2390] super reasonable assumption and yeah you
[2391] would
[2392] predict that yeah thanks
[2395] yeah of course um and as
[2399] um was already asked earlier in the talk
[2401] uh regarding like
[2402] what do we do with different layers of
[2404] the models um
[2407] we you know extract all layers from
[2409] particular model so let's say
[2412] we would end up within 725 models
[2416] across all layers then can we look into
[2420] how do these layers fit onto the brain
[2422] is there
[2423] any systematicity there and this is like
[2425] a pretty challenging
[2426] question so this is also like super
[2428] preliminary results
[2429] um the left hand plot here shows
[2433] the relative layer position on the
[2436] x-axis
[2437] so one here will correspond to like the
[2440] deepest layer meaning the output layer
[2442] while
[2443] zero here is like the input layer so
[2446] just the embedding for instance
[2448] um and we see a trend here that it seems
[2451] that like the late intermediate layers
[2455] um converge towards
[2458] optimal brain responses and there was
[2460] another recent paper
[2462] um i get to practice my french now maybe
[2467] also from this year uh that were also
[2469] looking into different types of
[2471] transformer networks
[2472] and they also found that there's
[2475] something about these like late
[2476] intermediate layers
[2477] that really explain the brain response
[2479] as well
[2483] and then another question this gets even
[2485] more
[2486] preliminary and vague then you can start
[2488] saying oh well if the
[2490] layers map differently onto the brain
[2492] can we then plot
[2493] that and this is like an example of
[2496] uh here the colors again correspond to
[2499] relative
[2500] layer position so one is like the
[2502] deepest layer
[2503] so for this particular subject uh this
[2506] is plotting gpt to excel we can see oh
[2509] there are some regions here that are
[2510] purely predicted
[2512] by the last layer while somewhere it's
[2515] like some of the earlier layers
[2516] um i don't have any like unified
[2519] conclusion
[2520] to draw from this but i think it's like
[2523] something that would be really
[2524] interesting to look into in more like a
[2526] systematic way at some point
[2530] um and last uh point which i hope will
[2533] be pretty brief is then can we like
[2535] dissect
[2536] these models to figure out like what
[2537] makes them like predict the brain pretty
[2540] well
[2541] um and this is a quite challenging
[2544] question to ask especially when you use
[2547] a lot of these like language models
[2549] because they're as we call them off the
[2552] shelf
[2552] so they're like pre-trained uh from
[2555] someone else and then they'll just like
[2556] package so we use them we haven't
[2558] trained them from scratch ourselves
[2559] which is like
[2560] wildly computationally expensive um so
[2564] they differ in the way they were trained
[2565] in the way they were tokenized how much
[2567] they were trained on
[2569] so it's pretty hard to make a direct
[2570] comparison but we have like an
[2572] exploratory analyses
[2575] uh which is like tapping into the effect
[2578] of
[2578] model architecture and training
[2582] so here we just tested how different
[2584] like architectural
[2585] properties and training properties in
[2587] addition to that
[2588] next word prediction task would
[2591] correlate with brain responses and just
[2595] uh briefly it seems that the larger
[2598] the model is the more hidden layers the
[2601] more features it has
[2603] the better it also predicts uh brain
[2605] responses
[2606] and maybe it there's a lot of confounds
[2609] here obviously because
[2610] as i mentioned they were trained very
[2612] differently but also that the larger
[2614] models are the more recent ones that
[2616] were trained on like
[2617] even better gpus even better hardware so
[2620] this is also somewhat like a hard
[2623] comparison to make
[2625] but i would like to point out that um
[2629] if we want to tap into this question uh
[2631] some people have started looking into
[2634] how you can you know make more like
[2636] systematic comparisons
[2638] where you for instance only compare the
[2641] training you only compare
[2643] one perturbation in terms of the
[2644] architecture
[2646] and another grad student in dr
[2648] federenko's lab ekbar husseini
[2650] is uh presenting a poster on this in
[2653] at society uh the snl conference which
[2656] is in two weeks
[2658] um and there's been some work on this
[2661] like last year the year before
[2664] trying to look at different like
[2666] architectural features such as like
[2668] context length and how that plays a role
[2670] in brain representations
[2672] and then there are also some work for
[2674] more like computer sciencey
[2676] uh domain uh that look into like what do
[2679] these potential mechanism do because
[2680] it's really complex
[2682] so this is where you know neuroscience
[2684] kind of have to work synergistically
[2686] with computer science um
[2690] so this almost brings me to
[2694] the end um i would like to go through
[2697] just a few points about this like
[2700] mapping methodology and some of the
[2702] decisions that are being made
[2703] just to like kind of like recapitulate
[2705] um and then use that as
[2707] as like a basis for uh discussion
[2710] um so yeah basically as i mentioned you
[2713] know either you have to read the method
[2715] section of these papers
[2716] really closely to kind of get which
[2718] decisions have been made
[2720] or you have like play around with it
[2721] yourself um so here i hope i can give
[2724] like somewhat of an idea of which
[2725] choices we actually do make
[2728] um so one thing that i mentioned we're
[2731] just going to start out by the
[2733] neural measurements it's like what do we
[2735] want to fit the model to
[2737] do you want to fit it to voxels do you
[2740] want to fit it to like a functional
[2742] region of interest
[2743] do you want to fit it to an anatomical
[2746] region of interest
[2748] there are many choices to be made here
[2750] and many assumptions do you want to
[2751] aggregate over regions or not
[2755] another thing is
[2758] what are the selection criteria of the
[2760] neural data that you include
[2763] there are some papers that have criteria
[2766] of if you include certain voxels then we
[2769] want them to be
[2770] very stable over representations or
[2774] that you already like pre-select maybe
[2777] like voxels or like new
[2778] or neural data that already is just
[2782] you would already expect it to do well
[2784] given some circumstances so
[2786] um i think that's an interesting thing
[2788] to keep an eye out for
[2791] um then there's c normalization that i
[2793] mentioned earlier
[2794] like we have noise and all neural data
[2797] we have to figure out what to do about
[2798] it
[2799] in cognitive neuroscience there seems to
[2800] be no
[2803] unified or like accepted way of doing
[2805] this so
[2806] you know we just estimated like a signal
[2809] to noise ceiling and divided everything
[2810] by that
[2811] you could do this in many different ways
[2816] and next in terms of the similarity
[2818] score
[2819] as i explained we used our like a
[2822] regression fitting
[2824] model where we have like an encoding
[2826] model where we try to predict
[2829] the brain recordings and rooted
[2832] in this like encoding approach is you
[2835] know
[2836] the view that the brain is like
[2838] processing information and we want to
[2839] encode and like decode information from
[2841] it
[2842] so one could also go the other way we
[2844] could do decoding as well
[2848] and another metric which is also
[2851] sometimes being used
[2852] is a representational similarity
[2854] analysis
[2855] rsa so here instead of fitting
[2858] regressions
[2859] you basically create like these um
[2863] similarity uh matrices uh there's like a
[2867] symmetric matrix a semester
[2868] sorry symmetric matrix where instead of
[2871] looking at actual brain responses you're
[2873] looking at
[2873] similarities of responses
[2876] um and the reason why some people really
[2880] like to use these
[2881] is that intuitively if you assume that
[2884] you have a computationally accurate
[2886] model of the brain
[2888] then you would also assume that the
[2890] patterns of similarity between the brain
[2892] activations and
[2893] the model activations would be similar
[2894] so that's like the underlying assumption
[2896] here
[2898] and we actually uh looked into how
[2901] our data generalizes to this
[2905] representational similarity approach
[2907] so on the x-axis we just have our normal
[2910] encoding approach
[2911] and on the y-axis we have using these
[2914] like dissimilarity matrices
[2916] and we do see that there is a
[2917] correlation so that's
[2919] fortunate
[2922] and next if you choose to use this like
[2925] encoding or decoding approach then
[2928] obviously you are fitting some kind of
[2930] regression
[2931] we just chose a simple linear regression
[2934] but
[2935] this no one says it has to be a linear
[2937] regression
[2938] it could easily be like some simple
[2941] non-linear model
[2944] it seems that this like linear readout
[2946] assumption
[2947] is widely accepted in like cognitive
[2949] neuroscience but
[2951] often neural computations are non-linear
[2955] maybe there's non-linearity when you
[2957] record like the fmri bold response
[2960] maybe there's non-linearity in the fact
[2962] that you
[2963] um aggregate over brain regions or you
[2966] have like successive neural computations
[2968] so that's another assumption that you
[2970] have to be have to be aware of
[2973] um another thing which was also a great
[2975] question that was being posed earlier
[2976] is about you know these models have
[2979] different number of like
[2980] activations right they have different
[2982] number of units so you could maybe just
[2984] expect are
[2985] the larger the model is the better it
[2987] would just fit any data
[2990] so i think it's interesting to look into
[2993] dimensionality reductions you say all
[2995] right
[2995] let's reduce all model activations to a
[2999] set size
[3000] um or fit a model that penalizes so like
[3003] regular like regularizes
[3005] like as a rich regression for instance
[3007] where you would like regularize
[3009] the weights and yeah this also brings me
[3013] to like the third point here which is
[3015] if you start choosing like a risk
[3017] regression or some non-linear model
[3020] then you have to tune some parameters um
[3023] some
[3023] papers in this field use rich regression
[3026] and sometimes they like
[3028] tune there's one hyperparameter and a
[3030] rich regression the lambda value
[3032] and then you can like cross validate and
[3034] find like an optimal value
[3035] is that fair um if you cross validate
[3039] enough maybe you can fit anything
[3040] should you just set a value should you
[3043] yeah what what assumption which
[3045] assumptions are being made here
[3047] um next um which
[3051] alison also taps into the question you
[3053] asked like
[3054] what do we want to predict in like the
[3056] optimal world we would want to predict
[3059] from one data set to a completely
[3060] different data set right
[3062] um and we would
[3065] want to do more than just predicting
[3067] between words we want to do more than
[3069] just predicting amongst sentences
[3072] um and more than just passages right
[3074] like we would want to like generalize as
[3076] much as we can
[3077] but that does still seem to be a
[3079] challenge and a lot of papers doing this
[3081] still only like cross-validate and
[3083] generalize over like
[3084] relatively easy or like easier
[3088] tasks but um i agree this is like a
[3090] really really
[3091] important goal
[3094] um and next uh you gotta you have to
[3097] like
[3097] figure out like what is what do you
[3100] compare it to what's the baseline
[3102] like what's like any baseline
[3104] performance of this
[3105] um so i think that we tried doing was to
[3109] just take
[3109] a random vector so say you have a model
[3113] with size 700 then you just take a
[3116] random vector
[3117] of size 700 and then you see how well
[3119] can that predict
[3121] the brain responses
[3125] and here what we see in the dark green
[3127] bar
[3128] is the performance of gpt 2 xl our top
[3130] performing model
[3132] which was close to the ceiling value and
[3134] then the light green bar is the random
[3136] embedding
[3137] so we do see that the performance
[3140] decreases
[3141] so it means that not any feature space
[3145] works
[3149] and lastly how do you want to evaluate
[3152] accuracy uh we just reported
[3156] um these like r values um some papers
[3160] uh actually uh make this into like a
[3163] binary task
[3165] um there's the one of the original
[3167] papers
[3168] by tom mitchell and all in science in
[3170] 2008 that were predicting
[3173] meanings of nouns and they did like a
[3176] pairwise comparison so if
[3178] your sentence is predicted better better
[3181] than like a random sentence then you get
[3183] a one
[3183] otherwise you get a zero so it's like
[3185] kind of like a binary accuracy task
[3188] and some papers still do this um in the
[3190] field
[3191] and it's definitely um an approach
[3194] that one can one can use but there's
[3196] like some strong assumptions about
[3198] how accurate you want your model to be
[3203] um yeah so this is like all the
[3206] different
[3207] some of the different points you can
[3209] think about and
[3210] just a quick summary slide about what
[3214] we hopefully learned is that some of
[3217] these
[3217] a n models seem to predict human neural
[3221] responses to linguistic input with
[3223] decently high accuracy and next we see
[3226] that this like neural productivity
[3228] correlates across data sets spanning
[3231] different
[3232] recording modalities fmri and e-cog in
[3234] this case
[3235] and across diverse materials that were
[3238] presented both
[3238] visually and auditorily and next
[3242] it seems that a drive for this like
[3244] online prediction
[3246] uh may be like a mechanism that shapes
[3249] language processing in the human brain
[3255] so by that we can discuss whether this
[3257] is a good idea
[3259] or not and all the assumptions that are
[3260] being made
[3263] and what time is it thanks so much greta
[3267] thank you it's two
[3271] yeah so um i know we're heading up at
[3273] time so if you need to leave
[3275] feel free but um greta if you have time
[3277] maybe we can have a little bit of
[3279] discussion here
[3280] if you're free definitely open it up to
[3284] any questions or discussion
[3287] that would be great i have a question um
[3292] and i guess it kind of touches on the
[3294] is it a good idea kind of idea
[3297] um so a lot of these models
[3300] are like evaluated by or based on the
[3303] idea of like
[3304] next word prediction or like next phrase
[3306] prediction
[3307] um i guess what is what is like your
[3310] take on like
[3311] how that is as an evaluation metric
[3313] since like
[3314] we like how well does a human like
[3317] predict the next word in a sentence or
[3318] something like that and i guess
[3320] continuing from that
[3322] um what do you see as like being the
[3325] next
[3325] step forward for abstraction away from
[3328] something like
[3329] next word prediction like do you think
[3331] it's something more like
[3332] multimodal like allison was i'm touching
[3335] on
[3336] is it like prediction across languages
[3339] um what do you see as the next step
[3341] forward for abstraction
[3344] right these are very interesting
[3347] questions
[3347] um yeah as you mentioned a lot of these
[3352] models are trained for next word
[3353] prediction which seems to work pretty
[3355] well
[3356] but what we have also seen in like all
[3359] the like computer science natural
[3360] language processing community is that
[3363] even some of these models like the gpt
[3365] models that do really well on predicting
[3367] the next word within a sentence and
[3369] maybe within sentence two and three
[3371] they start really falling into some like
[3374] traps in terms of like
[3376] context and semantics so it seems that
[3380] you know this abstraction level to a
[3382] certain degree is still lacking
[3384] um so one thing is that synergistically
[3388] with like computer science
[3389] we need to develop models that
[3392] generalize
[3393] better are more robust and can perform
[3396] better abstractions
[3398] i'm currently taking a class actually
[3400] with dr jacob andreas
[3403] about neurosymbolic approaches to do
[3404] that so instead of having these like
[3406] distributed units you would try to embed
[3408] some symbolic structures
[3410] i think that's a really interesting
[3411] approach and i'd be curious how these
[3413] like
[3413] more symbolic structures compare to the
[3416] brain
[3417] um in terms of what you mentioned
[3420] um in terms of generalizing to different
[3424] languages
[3425] we actually had a model that was like a
[3427] multilingual model so that seems to
[3429] work decently well otherwise there's the
[3433] multimodal approach because you know in
[3435] some ways it seems
[3439] ridiculous that humans you know take in
[3441] like input from all modalities at all
[3443] times we have
[3443] so much information and when we do these
[3446] comparisons we are only tapping
[3448] into like a model that was trained on
[3450] text and just text co-occurrence
[3452] basically
[3453] and then we're trying to use that as
[3456] like a mechanistic hypothesis of the
[3458] brain
[3459] so in some ways it seems really coarse
[3462] but
[3462] it's it's a beginning so yeah the
[3464] multimodal approach is
[3467] is something that i think is really
[3473] exciting
[3475] i can also mention another thing that
[3477] i'm really excited about in terms of
[3479] like extract
[3480] abstraction um which would be
[3485] that say you have a model that predicts
[3487] the neural response pretty well
[3490] could you then say all right i know this
[3492] model predicts this region pretty well
[3495] can i then go the other way and say all
[3498] right
[3499] i have this brain region what would be
[3501] the optimal like
[3502] stimuli to drive that region um there's
[3505] a science paper from bashivan at all
[3507] 2019
[3508] um who do some that do something similar
[3510] in uh the visual domain with like
[3513] uh neural sites as well so that is fun
[3524] uh thank you for the very interesting
[3527] uh talk i have maybe a naive question
[3531] but let's say that
[3535] maybe in a dozen years or something we
[3538] had some sort of model that perfectly
[3542] predicted the neural responses to
[3545] language
[3546] or had perfect generalizability
[3551] to what degree could we then look at
[3553] that model
[3555] as an explanation for how the brain
[3559] mechanisms are working
[3561] so like does the architecture of that
[3563] perfect model
[3565] how how do we bridge that gap
[3568] um to explain the neural mechanisms
[3573] right thank you it's definitely not a
[3575] naive question
[3577] i didn't talk a lot about
[3578] interpretability actually
[3582] and this is something that is for some
[3583] people really crucial and some people
[3586] really don't care it seems that there's
[3588] like two alleys right
[3589] one alley is like all right we just need
[3591] to maximize productivity it doesn't
[3593] matter how the mod
[3594] looks like let's just like engineering
[3596] wise maximize productivity
[3598] and then i said the other ally who are
[3600] like oh but we wanted to you know
[3603] we want if we wanted to serve as like a
[3606] mechanistic
[3607] hypothesis of the brain then we need to
[3610] have like
[3611] a somewhat biologically plausible
[3613] implementation
[3615] and right now we are not doing anything
[3618] that has
[3618] to do with biological plausibility um
[3622] these architectures that predict well
[3625] it's so unclear how they even map
[3629] onto different brain regions different
[3630] processing stages it's
[3633] really really challenging um so as you
[3636] say if we at some point have a model
[3638] that has
[3639] great abstraction it's like robust
[3641] predicts like the brain pretty well
[3644] then a next step would be to say all
[3646] right
[3647] i know that in this part of the brain we
[3649] have x number of connections or
[3652] the connections go this and this far can
[3655] we then try to take
[3656] these um like restrictions these like
[3661] uh this knowledge and then put that into
[3663] the model and then
[3664] build a more like plausible uh model
[3667] that would be really really interesting
[3669] and something that's now being done in
[3671] envision now
[3672] i think there's like an europe's paper
[3674] this year
[3675] on if you exploit
[3679] some of the information from the brain
[3682] on like uh detection of the visual
[3685] features you can improve the models so
[3686] it kind of seems
[3687] then it's like a synergistically loop of
[3689] like integrating biological knowledge
[3691] in these like computer science models
[3694] which where
[3695] both parts actually seem to benefit uh
[3697] but in language
[3699] sadly we are not there or unfortunately
[3701] because means that there's a lot to do
[3703] so it depends on how you see it yeah
[3706] thanks for the great question
[3707] yeah i don't know what people think
[3709] about interpretability whether it's
[3710] important or not
[3712] i may be also uncertain as to what i
[3714] think myself
[3716] so
[3722] right now if a model like the gpt2
[3726] is doing the best at predicting are
[3728] researchers
[3731] right now able to suggest that there's
[3735] similar mechanisms going on like how how
[3737] valid do you think
[3739] it is to be making those kinds of
[3741] conclusions like
[3743] what you were saying about um the brains
[3746] implementing this optimal prediction
[3749] thing maybe similarly
[3750] right yeah that's that's a good question
[3753] um
[3754] i think we can start extrapolating on a
[3757] very high level
[3759] we can't extrapolate on like the low
[3760] level mechanisms of the model
[3762] but what is interesting is that these
[3764] transformer models that perform really
[3765] well
[3767] what is like new about this transformer
[3769] approach is that they have these
[3770] attentional mechanisms
[3772] and if you think about it like in the
[3774] human brain you know what
[3775] we do all the time and what makes a
[3778] large part of what makes humans
[3779] intelligent is that your com
[3781] always constantly able to figure out
[3784] what do i want to focus my attention on
[3787] that's what
[3788] makes me like not think about what's
[3790] going on like outside my window or
[3791] whatever right
[3792] so in that sense like you can start
[3794] creating these links on like a very
[3797] high level which is interesting to start
[3799] thinking about like oh attention matters
[3801] like
[3802] uh online prediction for the next
[3804] meaning to occurs
[3805] is important and yeah no i think you can
[3809] extrapolate some interesting concepts
[3811] but on the lower level
[3812] it's still really challenging
[3818] i have a question i don't know if
[3822] you know about if anyone use
[3825] like uh use this
[3828] artificial neural network and combine
[3831] with
[3832] developmental studies like
[3835] maybe we can use some simple network of
[3838] the
[3838] models and then gradually increase the
[3843] complex complexity and sophisticated
[3846] uh units into and then can predict the
[3849] dynamic changes of the brain
[3852] is that possible or do you know anyone
[3854] is doing that
[3856] um that would be incredible and i don't
[3859] know anyone who's doing it so if anybody
[3861] is working with
[3862] language development as an email me
[3865] no um i actually don't know about anyone
[3868] doing that but
[3869] it just seems like such a
[3873] cleaner pro or like somewhat clean
[3874] approach besides the fact that i heard
[3876] it's really challenging to record neural
[3878] data from
[3878] infants but if we look away from that
[3881] fact
[3882] it seems like obvious and oh could we
[3884] fit yes simpler models without different
[3886] mechanism to like earlier
[3888] uh developmental stages and then later
[3890] on move on to complex stages and what
[3892] actually changes that would be
[3896] a really ins like interesting research
[3898] program that i think
[3900] one could work on for like the next like
[3902] 50 years probably
[3904] um another thing in that alley in terms
[3906] of development which i think is
[3907] interesting is
[3908] uh these like language models are just
[3910] like trained on like massive like
[3912] corpora of text
[3914] um but i think the field of like
[3917] curriculum learning as it's called is
[3918] pretty interesting so you would like
[3920] first
[3920] feed say like x number of like the most
[3924] frequent words to the model then repeat
[3926] them a lot of times
[3928] then you like build onto like a next
[3930] stage and kind of like trying to mimic
[3932] how like humans do learn language uh to
[3935] make these models
[3936] more robust there's some work on that
[3939] i'm not like a
[3941] know that much about the field but i
[3942] think that's an interesting
[3944] approach too yeah development is cool
[3949] thanks thank you
[3960] any other questions for greta
[3968] no you guys had some really really great
[3970] uh questions both like throughout the
[3972] talk and after
[3973] so um i think these are some of the like
[3975] large
[3976] uh issues we have to consider um and
[3979] hopefully like this entire like
[3981] framework
[3982] can you know be like a a basis of of
[3985] that
[3987] i feel like this is really cool and i
[3989] feel like you have like a lot of work
[3991] cut out for you
[3992] like it like this seems so generative
[3994] like there's so many
[3995] options to go here you have like your
[3998] whole career like
[3999] filled automatically
[4002] there's so many things to do like yeah
[4004] so many things to do for everyone yeah
[4006] it's
[4006] it's an interesting time for sure i feel
[4009] very grateful
[4011] i think i'm gonna stop sharing here but
[4013] yeah definitely feel free to like reach
[4014] out or
[4015] yeah if you're interested
[4019] well speaking of gratitude i just want
[4021] to say thank you again this was an
[4022] amazing
[4023] um talk and yeah very interesting
[4026] um just join me in thanking greta
[4030] thank you so much this was really fun i
[4032] appreciate it
[4033] and have an incredible weekend thanks
[4037] you too bye everyone thank you
