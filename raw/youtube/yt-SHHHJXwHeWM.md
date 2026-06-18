---
schema_version: 1
id: yt-SHHHJXwHeWM
type: youtube
title: Keynote 3 - Using Knowledge Graph data in Large Language Models
url: https://www.youtube.com/watch?v=SHHHJXwHeWM
authors:
- Swiss Text
ingested_at: '2026-06-17T20:57:21Z'
content_hash: sha256:3f7c5fe584bbe30c593187d409f5c288cdf64e61e868196cc833b2a24f838d94
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Swiss Text
  channel_url: https://www.youtube.com/@swisstext9397
  duration_seconds: 3915
  caption_track: fetched
  snippet_count: 1804
filter:
  score: 0.8
---
[11] thank you very much
[13] so
[15] thank you for the invitation i'm very
[17] happy to be here with with all of you
[20] um
[22] i'm going to talk to you
[24] about some of the work that we have been
[27] doing
[28] in the team and where i am this is young
[30] work with jedong a fedor was an intern
[33] from epfl
[35] jan moda and juan chen and he met all of
[38] them from google and martin martin jaggi
[41] who
[42] was in google before but since several
[44] years ago that he's in epfl um
[48] and i'm going to be talking in general
[50] about large language models and
[53] and some experiments that we have been
[54] doing to understand how
[57] these models which are purely statistic
[60] can benefit from structured knowledge
[63] graph like information
[66] i guess many of you know about large
[69] language models today but i'll give a
[71] quick introduction uh for for the ones
[74] we don't know
[75] language models are based on a few very
[78] simple principles one is transfer
[80] learning and one of these ideas is maybe
[82] we can do a supervised pre-training
[85] with very very cheap ways of collecting
[87] training data
[89] then the hope is that this will inject
[91] some knowledge into the language models
[93] that will be helpful for downstream
[95] tasks
[96] and the second idea is multitask
[98] training train a model to solve multiple
[101] tasks simultaneously
[103] and then uh the hope is that there will
[105] be knowledge transfer across all of them
[107] like summing for some information
[109] encoded into the model to sort some
[110] tasks will be useful
[112] to perform better on the other task and
[114] finally scale
[116] have bigger models and bigger amounts of
[118] data to train them
[122] regarding a super supervised free
[125] training
[126] this is something that started becoming
[128] popular a few years ago
[130] and this is a typical way in which this
[132] is done today so you have a text
[135] and this is taken from wikipedia a
[137] wikipedia document
[139] and you just remove from the text some
[142] words or some word spans
[144] and replace them with placeholders
[147] and you ask the model to reproduce what
[149] was missing in that text
[152] this is
[154] very
[154] this is a very easy way to have to be
[159] able to produce a lot of training data
[161] very easily because you just need text
[163] that's all and text you have it
[164] available it's in the web
[166] it's in libraries in book collections
[169] as
[170] is very
[172] very low bar of entry access here to to
[175] produce a large collection of text and
[178] once you have this
[180] you can scale to trillions to uh to
[182] trillions of words two quadrillions of
[184] training examples using this procedure
[186] so it's virtually unlimited the amount
[188] of the training data you have
[190] and this is in contrast to supervised
[192] fine tuning to source supervised
[194] training which is what was more popular
[197] before where you have
[200] an end task that you want to solve it
[201] can be anything from identifying
[203] entities in text identity findings for
[205] these entities identifying properties
[207] like dates or locations
[210] and in order to do this typically
[213] the procedure is to take
[215] some texts and have it annotated by
[217] humans produce human labels if there are
[220] semi-automatic ways of producing these
[222] labels then maybe you can produce silver
[224] data that is not completely accurate but
[227] it can be helpful
[229] but typically you need also some human
[231] curated data and the
[234] in in this case
[236] obviously the size of the training data
[239] will be limited by your budget you will
[241] have a certain budget to
[243] to hire people to write these
[245] annotations and that will limit how much
[247] data you can have
[250] this is a very
[252] very simplified
[253] chronology of how these models evolved
[256] over time like
[257] all we could say
[260] actual applications
[262] product product quality applications of
[265] neural networks in nlp started around
[267] 2014 with world embeddings word to back
[270] and globe were some of the earliest
[272] examples
[274] where
[275] they were also trying to supervise so
[277] these word embeddings were trained
[279] to represent the words based on the
[281] context in which they appear
[284] and typically they were used as features
[286] for cross-attention models for other
[288] different kinds of models that didn't
[290] have to be neural models but could be
[291] neural models
[293] and then
[294] also during this years 2014 1516
[298] people started use recurrent neural
[301] networks
[302] initially rns and lstms and so sequence
[305] learnings
[306] learning became the state of the art at
[308] the
[309] time and
[311] there is this example semi-supervised
[313] sequence learning which is one of the
[314] first examples where they
[316] they propose to do this and supervise
[319] pre-training they produce good results
[322] but the idea didn't really caught on yet
[324] it needed one and a half more years
[326] until the
[327] unsupervised sentiment neuro neuron
[329] paper came out where they also were
[331] doing
[332] unsupervised pre-training and showing
[334] that it provided it led to good results
[336] and sentiment analysis
[339] and
[340] and then the big and the
[343] the field was grounded in 2018 with
[346] mothers like ulm feed elmo gpt-1 on
[349] birth and also during this year the
[352] community transitioned from using
[353] recurrent neural networks like the first
[355] couple of examples to using transformer
[357] based models self-attention
[360] and then after that there's been a
[363] accelerated progress
[365] are you saying and i want to highlight
[367] t5 here
[368] because it's a mod along with the
[370] experiments i will be talking later
[372] are based on
[375] and
[376] to for this unsupervised free training
[378] i was mentioning you need a lot of date
[380] a lot of text and text is easy to
[382] produce
[384] but you still need some infrastructure
[387] and some time to collect the text and to
[389] clean it and and for that for the
[390] development of t5 the t5 team at google
[393] they also published this data set the
[395] common crawl web extracted text also
[397] known as c4
[399] and it is a
[401] resource that many people are using to
[403] train this kind of models
[405] it's a very simple idea just take a web
[407] crawl the first version of c4 was in
[410] english
[411] and a few heuristics to clean the data
[414] set for example removing lines that were
[416] not ending in punctuation removing
[418] anything that looks like javascript
[421] removing any complete page if it
[424] contains placeholder text or if it looks
[426] like programming code or if it contains
[429] any kind of bad words or bad content
[432] and
[433] deduped the data to make sure because
[436] there are many copies of web pages in
[438] the web everywhere so some did you pin
[440] there to make sure the content is uh
[444] it has enough variation and and there
[446] are no sentences that are overly
[448] represented there
[449] and this results is about 750 gigabytes
[452] of cleanish text that that is available
[455] for download here
[457] so once
[458] once we have this data
[460] one more example of how this works let's
[462] suppose that in our corpus we have a
[464] sentence like this tweet swiss text is
[466] an annual conference that brings
[468] together text analytic experts from
[470] industry and academia
[472] so the first
[474] the first thing to do is take the
[476] sentence and randomly select
[479] one or several spans that you're going
[481] to mask out
[483] like for example could be annual
[484] conference and industry in this case
[487] these
[488] spans are replaced with placeholders
[492] and then you train the model to tell you
[495] for each of these placeholders what is
[497] the text that was originally
[501] it's a very simple idea
[503] but in order to learn to reproduce this
[506] so on the one hand as i was saying it's
[508] trivial to produce trillions of words of
[510] examples of this data
[513] on the second hand
[514] for a model to be able to reconstruct
[516] the original text
[518] the model needs to be able to understand
[520] how language works to understand what is
[522] a properly grammatical sentence and to
[524] understand what makes sense semantically
[527] and that's why pre-training on so much
[529] data results in a very very powerful
[532] model that
[533] we will see later some examples out
[535] there and even emerging properties that
[537] are surprising
[541] okay now
[543] how about
[544] supervised training how how is
[546] supervised training done in when
[548] training these large language models
[552] these models
[556] we we are going to stay close to how
[558] pre-training was done and if you look at
[560] pre-training this is a generative model
[563] the input is text the output is text
[566] once you have it training later there is
[568] no limitation in the sense that it's an
[571] encoder encoder model takes the input
[573] and calls it
[574] and then the decoder generates the
[578] the missing content for these
[579] placeholders
[581] once you have it training is flexible
[583] you can
[584] take the encoder and you can plug in for
[587] example a classification head or a
[589] regression head in the output and then
[591] you can use this model
[593] for document classification in
[594] multi-class classification for
[597] for any kind of numeric prediction so
[600] in that sense it's not there are no
[602] limitations but for
[604] fine tuning for pre-training and
[606] typically
[608] we stay close to this text to text mode
[611] treating it as a generative model
[614] and same as pre-training isn't in this
[616] way finding the content of the
[618] placeholders
[620] the supervised multitask training is
[622] typically defined
[624] by telling the model with what to do
[626] with the prompt telling the model what
[628] is that as a team needs to solve by
[630] providing a prompt with instructions
[632] what to do like in this case if you want
[634] to train it for
[636] machine translation you could provide a
[638] problem like this translate from english
[640] to german
[641] and the source sentence and then you
[643] train the model to produce a target
[644] sentence
[646] but there can be many different tasks
[648] that you can
[649] train simultaneously with this multitask
[651] training so you could as a model to
[653] distinguish which sentences are
[654] grammatical from which centers are not
[656] grammatical
[657] or you could train the model
[659] to tell you a number representing the
[662] sentence similarity between two
[663] sentences and you can look here that
[666] you can do this as a text generating
[669] model asking the model to produce as
[671] plain text text ascii
[674] a numeric number representing the
[676] similarity
[678] and this is how
[680] these models are
[682] are pre-trained as i was saying
[686] then
[687] later if if you're applying this to
[689] another different task in production
[691] settings you you can do actual
[693] classification here i'm predicting the
[695] number more
[697] with
[698] as a real number but
[701] this keeps all the tasks with the same
[703] format the same input is text output is
[706] text and that simplifies the
[707] architecture
[708] and this is another example you can
[710] assist model to summarize to summarize a
[713] text and produce a summary
[715] and internally
[718] they all these things are based on
[720] transformers transformers were initially
[723] presented a few years ago with this
[725] attention is all you need paper
[727] the
[728] advantage
[730] with respect to recurrent neural network
[732] is that recurrent neural networks
[733] consume the input sequentially
[736] but here
[738] these layers they can attain over the
[740] whole input simultaneously
[743] and
[743] [Music]
[748] empirically it makes them much more
[749] powerful than rnas
[753] so
[755] so this is how
[757] the initial t5 model was produced there
[761] is a supervised pre-training which is a
[763] transformer model of the same size as as
[766] vert in the first experiment
[769] and we take this c4 data set and from
[771] this this c4 dataset we produce the
[773] training examples for
[775] a mass language model
[778] once we have this pre-trained on the
[781] mass language model
[783] we already have a network that is
[785] initialized with some weights that is a
[787] very powerful language model that it has
[789] in so much data that it understands very
[792] well what kind of content fits in every
[795] context
[797] and then you can take this and you can
[799] do multi-task training
[802] fine-tuning this model using this
[804] prompting
[805] on all these different tasks
[807] simultaneously
[809] and
[810] as it is being fine-tuned
[813] every time a checkpoint is produced the
[815] checkpoint is evaluated and a validation
[817] test set and the checkpoint with the
[820] first resource on the validation test
[821] set is chosen as a base one and that one
[824] can then later be applied to the unseen
[826] test set and to see how well this
[828] performs
[831] these are just some numbers about
[833] different model variants that were tried
[835] in the original d5 paper the small base
[837] large xl and xxl
[840] with
[841] increasing the number of layers
[843] increasing the number of the dimensions
[845] of the internal state so the number of
[847] parameters ranges between 16 million for
[849] the small one to 11 billion parameters
[852] for the largest one
[855] and these are these are results on
[859] using
[861] all these different sizes a small base
[863] large xlxl
[865] on
[866] all the tasks on which this was
[868] benchmarked
[870] and you can see that for most of the
[873] benchmarks when this was published it
[875] produces state-of-the-art results for
[878] glue
[879] cnn daily mail summarization data set
[882] squad super low these are all benchmarks
[884] some of these contains many different
[886] tasks
[887] could range from
[888] sentence similarity to to semanti to
[892] to sentiment analysis
[894] or question answering so
[897] for the first four data sets
[900] the largest size of the t5 model
[902] produces state-of-the-art results on all
[904] of these benchmarks it didn't produce a
[906] state of real result of machine
[908] translation
[910] but it got very very close to
[912] to the state of real results which were
[915] traditional machine translation systems
[917] that had been trained on high quality
[919] parallel corpora
[921] and had been
[923] and were models that had been
[925] specifically designed for machine
[926] translation
[927] so overall this look very very promising
[932] and i want to show you some examples
[934] these examples i
[935] i got them last week
[937] taking one of these t5 models that we
[940] have trained internally on
[941] on our own data sets
[944] and testing them and see what happens
[946] and i was saying that there are these
[948] emerging properties of this model from
[950] having seen so much data
[952] the first example i just take one of
[954] these fable from east of the shepherd
[956] boy and the wolf i think it will be
[958] familiar to many of you this shepherd
[960] who
[961] says the wolf is coming come to help and
[964] all the villagers come and help and he
[966] laughs at them it was a joke several
[968] times finally when the wolf comes
[971] no one goes to hell because everyone
[972] assumes he's a joke again
[974] and i tell i asked the model the moral
[977] of story is and i put a placeholder and
[979] i as a language model to feel what was
[980] missing there and the language model
[983] writes do not play tricks and those who
[985] help you in a time of need
[987] which is a really great model for this
[989] story and it's not in the input it's
[992] it's figured out that that fits in that
[994] context
[996] another example is the summarization
[998] example i i searched in google news i
[1000] took a news document if
[1004] one more of these studies that
[1006] says that coffee helps you live longer
[1009] that's good news so i asked in the end
[1011] what's the summary for this story
[1014] and the model produced coffee
[1015] consumption is associated with reduced
[1017] risk of death which is a pretty good
[1020] summary
[1021] it follows closely the second sentence
[1024] of the article
[1026] but
[1026] still it
[1028] it's good that the model decided to
[1030] focus on that sentence which is the most
[1032] important one
[1033] and and it's a little bit paraphrase to
[1036] make it more standalone
[1040] this is also another example where i fed
[1043] the model this is made up story john
[1046] found three strawberries he baked one
[1048] two g two jang one two peter jane gave
[1051] her strawberry to peter at the end john
[1053] has x
[1054] jane has y and peter has sit
[1057] and the model outputs x is one
[1059] strawberry y is known and c should be
[1062] two strawberries
[1064] and this is actually a correct
[1067] correct output for the input i provided
[1072] these models are hand selected okay so i
[1075] i played a little bit with the system i
[1076] chose the models for the model did right
[1078] these models are not trained to do
[1080] arithmetic so same as this example
[1081] worked
[1083] i tried a few other examples that didn't
[1085] work
[1086] but still the fact that sometimes it
[1088] gets it right i find it pretty amazing
[1090] that just based on
[1092] this fill in the blank objective free
[1094] training sometimes it may sometimes it
[1097] learns to do some arithmetic or at least
[1099] it learns that one strawberry
[1100] probabilistically is the most likely
[1102] filler for x given the previous context
[1108] um it's also possible to use these
[1110] models in what is called fuse fusion
[1113] learning in future learning you provide
[1115] a few examples of the tasks you want
[1117] them to solve
[1118] and then you provide the real inputs
[1120] that you need the classification for
[1122] like in this example
[1124] i tried to write i really enjoyed this
[1126] movie it's a positive review i walked
[1128] out of the cinema it's a negative review
[1130] and then i asked the mother how about
[1132] the next two
[1133] the plot keeps you on your toes
[1135] throughout the movie what is it and it
[1137] should get the prize for the most funny
[1138] movie what should it and again it makes
[1141] it right it decides
[1143] the third one is positive and the fourth
[1144] one is negative
[1146] in this case
[1148] in this case this is the first example i
[1150] tried for something like this i didn't
[1152] really
[1153] engineer it
[1155] and
[1156] i tried to use metaphors things that
[1158] were not obvious like walked out of the
[1160] cinema or keeps you on your toes or
[1163] the last one mention a price the price
[1166] tends to be positive and in this case
[1167] for worrying
[1169] so it
[1170] it does it right
[1174] now
[1175] the last two examples i want to motivate
[1178] the next section of the talk
[1180] these models can also memorize facts
[1184] and
[1185] if i take this t5 model and i asked it
[1190] the movies just was directed by x in y
[1194] it filled in the existing spielberg and
[1196] why is 1975 which is correct
[1199] so it means
[1200] it's learned that fact from the
[1202] pre-training data is pre-trained on the
[1204] web the web contains for example the
[1206] wikipedia article for jaws or the imdb
[1208] article for the imdb page for just this
[1212] information is encoded there so from the
[1214] pre-training data most likely
[1216] the model has already seen maybe several
[1218] times this fact has memorized it and if
[1221] if i ask the model to fill in these
[1223] blanks it can give you the right facts
[1225] which which is great
[1227] but then i tried another example
[1229] citilize was directed by x and y
[1232] and then in this case it output wrong
[1233] data so the director was charlie chaplin
[1236] and he said it was john ford the year
[1238] was 31 it's a 32 it was close but not
[1241] not quite right
[1244] and
[1245] one of the problems of these models is
[1247] that they are trained
[1250] to with this language model objective
[1252] that are so powerful
[1254] that they produce very plausible feelers
[1258] if
[1260] it's an older movie okay john ford
[1261] directed all the
[1263] movies around maybe in the 40s
[1265] 40s 50s
[1267] the year is closed so they produce an
[1269] output
[1270] but it's not so easy to know when
[1273] it knows the fact versus it's
[1274] hallucinating something plausible it's
[1276] very different very difficult to to
[1279] distinguish this and if you want to
[1280] apply this model say for
[1282] for a search assistant or for a
[1285] conversational interface
[1288] they tend to be to give you
[1291] sometimes correct answers but sometimes
[1294] they give you the wrong answers but they
[1295] stated with so much confidence and state
[1297] is so grammatically correct
[1300] that they're actually very misleading
[1301] when they're wrong
[1305] and then another example is that these
[1309] what we call multi-hop reasoning if you
[1311] ask something like other movies directed
[1313] by the director of schindler's list are
[1315] these and this
[1316] this is not a direct fact with a subject
[1318] predicate object you need to do several
[1321] several hops in the knowledge craft you
[1323] need to know even this movie this is the
[1324] director given the director he directed
[1327] these other movies
[1329] this kind of mass language model
[1330] objective does not train the model to do
[1332] this kind of chain reasoning and it
[1334] tends to
[1335] fail always with this kind this kind of
[1338] context
[1340] so we are going to
[1342] i'm going to talk a little bit
[1344] about some studies that we did on
[1347] memorization
[1352] for and we're going to be focusing on
[1354] question answering question answering we
[1357] can
[1358] handle it academically we can
[1361] we can formulate it in three different
[1363] ways
[1364] the first way would be reading
[1365] comprehension and this task is defined
[1368] you have a question
[1369] you provide some context
[1371] the task of the model is to understand
[1374] this context and provide a survey on
[1376] that that is
[1377] supported by that context
[1380] like in this example what color is a
[1382] lemon the context is telling you that
[1384] the lemon is a yellow
[1386] so this answer can be extracted from the
[1388] context
[1390] a slightly more different problem is
[1392] when you don't provide a context the
[1394] user does not provide the context the
[1396] user just provide the question
[1398] but you train the model to do some kind
[1400] of retrieval augmentation the model
[1402] receives a question and they it can
[1405] encode the question
[1406] it can use
[1408] some procedure to do retrieval from a
[1411] database the database can contain facts
[1414] or passages or embedding vectors from
[1417] encoded passages for example
[1420] and then based on the retrieved passages
[1422] and and the question the model needs to
[1425] extract the answer
[1426] so there is one one more step here
[1430] that
[1431] that the model needs to learn which is
[1432] given the question or the encoding of
[1434] the question how how to retrieve
[1436] relevant passages
[1439] and
[1440] the
[1441] the third one is close book question
[1444] answering when you just provide the
[1445] question there is no retrieval
[1447] augmentation
[1449] and the model needs to
[1451] produce the answer and this can only
[1454] happen properly if the model has
[1455] memorized the answer during pre-training
[1460] in
[1461] in the t5 paper actually they also
[1464] explored this
[1466] a little bit
[1467] and they
[1469] these are some examples in the training
[1472] data you have
[1473] different sentences
[1475] and some of them may contain a certain
[1478] fact like may contain that a given
[1480] person was born on a given date and then
[1483] if you ask t5
[1485] in the close book question answering
[1486] setup you ask a question you expect the
[1489] model to produce the answer
[1491] they tested this out on several open
[1494] domain uh
[1496] on several data sets natural questions
[1498] web questions and trivial qa
[1501] and they found
[1503] that
[1504] it doesn't perform too badly but it
[1507] doesn't get close to the open domain
[1509] state of the art it's significantly
[1511] underperforming even the larger t5
[1514] models
[1516] so
[1518] one thing that they tried as an
[1519] improvement is what is called salient
[1521] spam masking
[1523] in the example i
[1524] presented at the beginning of the talk i
[1526] said
[1527] that the the spans that are removed to
[1530] with this unsupervised free training
[1532] objective they were random but they
[1535] don't have to be
[1536] you you could use for example in insane
[1539] span masking you want the model to
[1541] memorize a fact so then you go and you
[1543] mask out exactly what you want the model
[1545] to memorize in this example this is the
[1548] the first sentence of the wikipedia page
[1551] how the movie vertigo
[1553] if we want the model to memorize the
[1555] release year and the director
[1558] we can go straight and mask specifically
[1561] those two spans and as a model to
[1563] produce during pre-training to produce
[1566] them
[1567] and this can be done on a large corpus
[1569] same as before
[1571] and
[1572] if if you compare
[1575] t5
[1577] if you take a t5 checkpoint and you add
[1581] either
[1582] continue pre-training on the c4 data set
[1585] with
[1586] random masking
[1588] or you continue pre-training on
[1591] on the c4 data set but using silence but
[1593] masking for the relationships that you
[1596] care about
[1597] you can see that the random masking
[1600] has reached a plateau additional
[1602] training does not improve the exact
[1604] match
[1605] score on on the predicted answers
[1608] but using saline masking it keeps going
[1611] up it keeps improving the model is
[1613] learning the facts that will allow it to
[1616] produce the right answer to the
[1618] questions in in these data sets
[1621] and now if you expand xxl with salient
[1624] span masking
[1626] and you evaluate on these datas as you
[1628] see there is a big improvement on all
[1630] three of them
[1632] and in web questions in particular it
[1634] because it became the state of the art
[1636] t5 with with this masking approach
[1642] so
[1645] wrapping up a little bit
[1648] there are two
[1650] ways in which we can leverage a
[1652] structured knowledge graph data for
[1654] question answering
[1656] the explicit approach would be
[1658] for example this retrieval augmentation
[1660] you
[1661] train the model to query
[1664] your knowledge graph
[1665] and this query can happen in different
[1667] ways
[1668] i've seen
[1670] papers where people train the language
[1672] model to produce a structure query for a
[1675] knowledge graph it could be a spark ql
[1677] or something like that to actually
[1678] produce a query that then is executed
[1680] over the database for
[1681] retrieve the answers
[1683] and then extend the input with the test
[1685] representation of these answers
[1688] and then the model do a second pass over
[1690] that and produces the answer and a
[1692] different approach is more embedding
[1693] based you encode the query
[1695] you encode the potential answers and you
[1698] look for closeness in the embedding
[1700] space and then you retrieve the
[1702] potential answers that are
[1704] the closest to the encoding of the
[1706] question so there are many different
[1707] ways
[1708] but all of them have in common that
[1710] they're explicitly querying a knowledge
[1712] graph
[1714] and the advantage this has is that you
[1716] can access the whole knowledge of the kg
[1719] the other approach which is
[1721] memorizing facts inside your model
[1725] it has a disadvantage that is not
[1727] guaranteed to remember the whole kg you
[1729] can use
[1730] sailing spam masking you can provide all
[1733] the all the facts in your knowledge
[1734] graph but this is a black box you don't
[1737] know how much is remembering from it how
[1739] much is memorizing
[1742] so the explicit retrieval from the kg is
[1745] interpretable but the implicit one is a
[1747] black box i was saying is not
[1749] interpretable
[1751] the explicit retrieval
[1753] requires but on the other hand the
[1755] explicit retrieval requires different
[1758] architectures and is harder to
[1759] productionize requires to store the
[1761] knowledge for inference
[1763] and requires to have different neural
[1765] architectures that allow the model for
[1767] example to do two passes to to do first
[1769] retrieval stage and then do a second
[1772] stage so it's typically different
[1774] architectures
[1776] sometimes you need to combine
[1777] an embedding tower with a cross
[1779] attention model to produce the answer so
[1781] it's more complicated setups
[1783] in the case of memorization you just
[1785] have your model your transformer model
[1787] that is your language model
[1788] and it will learn inside the same model
[1791] in the way it will codify
[1793] the facts that you wanted to memorize to
[1795] remember
[1799] and
[1800] the explicit approach
[1802] is something built at hog for this
[1805] question answering setup or setups what
[1807] you need more grounding the implicit
[1809] approach as we saw t5 is very generic it
[1812] can be applied to many different tasks
[1814] some of them may require knowledge some
[1816] of them may not require explicit
[1818] knowledge you just have one model that
[1820] can solve all of them because it was
[1822] trained for multitask setup
[1825] and
[1826] basic and and as i was saying you just
[1828] have one t5 model 25 model that
[1831] additionally has memorized additional
[1832] facts in the implicit approach
[1835] so you can easily replace one model with
[1837] another model without without additional
[1839] complications in production
[1842] so we're going to look at these two in
[1844] the top but we're going to start looking
[1846] at at the implicit memorization and i
[1848] will talk about some experiments that we
[1850] did
[1851] they are not close to having production
[1853] applications but we wanted to understand
[1855] better how things how how this works
[1857] internally and if we can draw some
[1860] conclusions about it and best ways to
[1862] train these models we call it knowledge
[1865] infusion this memorization
[1868] and the idea is you we have a
[1870] knowledge triple and the triple three
[1872] always have a subject a predicate and an
[1874] object
[1876] and we can do two things to feed it into
[1880] the large language model
[1882] one way is
[1884] the obvious thing is to dump the triple
[1886] as a string
[1888] if we have a human readable name for the
[1890] predicate we can just give the name of
[1892] the subject entity the predicate name
[1894] and the object name this is easy to
[1896] obtain but this one question we had is
[1898] this is not natural language
[1901] and we had seen there are papers like
[1904] there are papers like elmo ernie and
[1908] kelm that tried already to provide
[1911] structural information to the language
[1913] models and typically what they do
[1915] because these llamas are always
[1917] traditionally trained on natural
[1919] language models what these papers try to
[1922] do is to align structural triples with
[1924] natural language sentences
[1927] but this requires additional machinery
[1928] you need to be able to either generate
[1931] sentences based on the triples or align
[1933] the triples to sentences in some way you
[1935] need this triple to text mapping
[1938] in order to
[1940] in order to
[1943] put your knowledge graph in a format
[1945] that can be consumed
[1947] by natural language
[1948] large language models
[1951] so
[1952] we had this question what what happens
[1954] if we try just passing the structure the
[1957] structure knowledge just dumped as a
[1959] string much more easily
[1961] and the task is the following
[1964] we wanted to memorize for example the
[1966] objects or the subjects or the predicate
[1968] names so in this example we mask out the
[1971] object
[1973] in the first example directly from the
[1976] triple in the second in the case of
[1978] natural language from inside of the
[1979] sentence and the target is the same in
[1982] both cases the name of the object
[1986] i we
[1988] used as a starting point some previous
[1990] work which is the kelm data set what the
[1993] kelm authors did was to take wikipedia
[1995] and wiki data
[1997] and align the wiki data triples to
[1999] wikipedia sentences for the wiki for the
[2002] wiki
[2003] find a sentence in wikipedia that
[2005] mentions explicitly the subject and the
[2007] object
[2008] and some additional cleaning of the
[2011] dataset to remove to remove the false
[2014] matches
[2018] and then they train it if i mod then but
[2021] the the problem with with this alignment
[2023] is that it will not have full coverage
[2025] you will not have sentences on wikipedia
[2027] for every single wiki data triple
[2030] so in order to have full coverage on
[2031] your knowledge graph they train a
[2033] generative d5 model
[2035] to consume a triple and generate a
[2036] sentence using this alignment as
[2038] training data
[2040] and once they had this model
[2042] they
[2044] ran this model over the whole of
[2045] wikidata and for each triple generated a
[2047] sentence and now you have a natural
[2049] language sentence that represents each
[2051] of the wikidata triples
[2055] so
[2058] so in that way we use a cam data set to
[2061] have this
[2062] alignment between structural triples and
[2064] natural language sentences but we also
[2066] used
[2068] we also use the
[2069] directly
[2070] damping the triples subject comma
[2072] predicate comma object without natural
[2074] language sentences
[2076] and we validated this on close book
[2078] question answering tasks you have a
[2081] question like for example which cities
[2083] capital of germany
[2084] and this requires external knowledge for
[2086] answers so the data said we tried
[2088] previous qa we give hope trivia qa
[2090] natural questions
[2092] then we data has 35 million troopers so
[2095] you get an idea of the scale
[2097] and kelm has 15
[2100] million sentences so they don't actually
[2102] have sentences for every single wikidata
[2104] triple but they have okay coverage
[2107] acceptable coverage
[2110] and this is important while training we
[2112] mix we did a mixture with the c4 corpus
[2114] with c4 corpus with random
[2117] random
[2119] masking
[2121] because
[2123] if if we
[2124] take
[2125] t5 and we just fine tune on this weak
[2128] data data set
[2130] we observe that the model for guides the
[2133] previous pre-training and
[2135] replaces previous knowledge with just
[2137] this structural information we're
[2138] providing now
[2140] but by mixing this structure knowledge
[2142] with the original pre-training we ensure
[2145] that it keeps remembering what it has
[2147] been pre-trained for to begin with
[2151] so we do number of training steps
[2154] between hundred thousand to five hundred
[2156] thousand
[2157] and these are some
[2158] results
[2161] on these two datasets previous qa and
[2163] wikihop
[2165] and
[2166] what we were happy to learn here first
[2168] of all there is some improvement
[2171] versus the vanilla t5 models
[2174] the second line is a vanilla t5 model
[2177] with additional pre-training using the
[2180] c4 corpus and the reason we did that is
[2182] that
[2183] we want to make sure that the
[2184] improvements are due to the structural
[2186] data they are not used simply because
[2188] these models will have been trained for
[2190] a bigger number of steps so by doing
[2192] additional pre-training with the
[2193] original c for corpus we make sure
[2196] that in number of steps is comparable
[2198] and we have one one few variables to
[2200] consider here
[2202] and
[2203] you can see that on these two datasets
[2206] knowledge injection provides better
[2209] results than using original d5
[2211] on on all the metrics and something that
[2214] we were happy to see is that
[2217] numbers are pretty comparable between
[2219] using the
[2221] damp triples versus using the natural
[2224] language came in sentences
[2228] and what this is telling us is that we
[2230] don't need all this additional machinery
[2232] of aligning troopers to sentences
[2233] training the generative model and
[2235] producing the sentences for the triples
[2237] we just condemn them very easily
[2240] and this is a much more scalable way of
[2243] having a
[2244] a large language map a large knowledge
[2248] graph and dumping it in in a way that
[2250] the language model can benefit from
[2253] so this was the first
[2256] the first conclusion here
[2258] if you look at the other two data sets
[2260] trivia qa and natural questions
[2263] what we saw here is that the
[2265] improvements are much more modest
[2269] compared to the vanilla t5 models
[2273] and looking more into these data sets we
[2275] found that actually they contain a lot
[2277] of questions where the answer is not
[2279] expected to be in wikidata some of them
[2282] are for example which person
[2285] said this quote wiki data doesn't
[2287] contain quotes many questions refer to
[2290] facts that are not even modeled by the
[2292] wikidata schema or even if they are
[2295] modeled the fact does not exist on wiki
[2297] data
[2299] and
[2300] and therefore simply because the
[2303] fine-tuning data and
[2305] and the test set are not really aligned
[2306] so we didn't see big improvements so
[2309] what we did also as a proof of concept
[2312] is to say what happened if we take these
[2314] two data sets
[2316] and we restrict we we filter
[2318] the test examples with a very simple
[2321] criteria
[2323] we keep only the questions
[2325] that mention
[2326] [Music]
[2328] that mention an entity that is either
[2331] subject or object of some triple on wiki
[2333] data
[2334] and in that case we know that the
[2336] question is talking about something that
[2338] wiki data knows something about it it's
[2341] still not guaranteed that wikidata will
[2342] have the answer to that question
[2345] but we at least we get rid of a lot of
[2348] questions that we know for sure wiki
[2350] data will
[2352] will not have the answer for that
[2353] because if they only mention entities
[2355] that wiki data has no fact for them
[2358] then
[2359] we know for sure the answer is not in
[2360] wikidata and if we look at this
[2363] subset of these two data sets now we see
[2366] that the improvement is
[2368] is there and is statistically
[2369] significant on
[2371] on all these cases and for all the sizes
[2374] of t5
[2375] now we can measure some improvement
[2378] which
[2379] is good news because it means the model
[2381] is memorizing the information that we
[2382] want
[2384] and finally also as a proof of concept
[2387] we verify that in a data set that
[2389] doesn't require this memorization like
[2391] the super low benchmarks
[2393] there is no degradation we also want the
[2396] model to
[2397] to be as generic as general purpose as
[2399] the vanilla t5 and we verify this and
[2402] and this was not hap this would not
[2404] happen if we only fine tune on the
[2407] structure knowledge but because we have
[2409] this mixture with fc4 corpus while fine
[2412] tuning
[2413] that's what guaranteed that is not
[2415] forgetting the previous pre-training and
[2417] we have no degradation on these tasks
[2422] you can also see that the improvement
[2424] over the vanilla t5 model is
[2426] increasing actually
[2428] already
[2430] with the size of the model
[2434] okay so i'm going to
[2436] move on to the second part of the dock
[2439] which is the
[2441] the explicit more explicit retrieval and
[2444] as i said before this can be done in
[2446] many different ways but we we look here
[2449] at one very concrete one
[2453] and we look at dual encoders dual
[2455] encoders have been used for many
[2457] different tasks the idea is that you
[2460] want to align to corpora you want to
[2461] align two sets of items for example you
[2463] may want to align images with captions
[2466] or you may want to align documents with
[2468] queries for which the document is
[2469] relevant
[2471] and there are
[2474] different ways of training the dual
[2475] encoders but we are going to looking
[2478] concretely here
[2481] two specific architectures one is use a
[2483] symmetric dual encoder and the other
[2484] side a mutual encoder
[2487] in the asymmetric dual encoder
[2489] we have
[2492] we have two encoding towers
[2495] and
[2496] in the specific case of question
[2497] answering we use one to encode the
[2500] question and the other one to encode the
[2501] answer and this is an example we have a
[2504] qa data set the close book qa data set
[2508] unless opposed this is a
[2510] a an item in this test set just barack
[2513] obama is the question and michelle obama
[2515] is the expected answer
[2517] the question would be passed over the
[2519] question embedding tower
[2521] and this tower outputs an embedding
[2523] vector and the answer is
[2526] is fed into the answer embedding tower
[2529] which also outputs an embedding vector
[2531] and for training the loss we use is is
[2534] that is the distance between these two
[2536] vectors because we want
[2538] the question and the and its answer to
[2542] be positive examples to be mapped close
[2544] in the embedding space
[2546] and we also use negative examples taking
[2549] the question and wrong answers that are
[2551] sampled from from the same batch from
[2553] other examples in the same batch and we
[2555] train we train these two towers to make
[2557] sure the negative examples are pushed
[2560] away from each other in the embedding
[2561] space
[2564] the second
[2566] the second alternative we could use as a
[2568] missile encoder this is not always
[2570] possible
[2571] because sometimes
[2573] you have um two different corpora in the
[2576] two towers let's suppose you're aligning
[2578] images with captions
[2580] for the images you will need an image
[2582] and go there like a visual transformer
[2584] for example where for captions that
[2586] stacks as input you will need a text
[2588] encoder
[2590] if you need different architectures for
[2591] the two towers they cannot share the
[2592] parameters
[2594] but in this case in particular the
[2595] question and the answer they are both
[2597] short strings plain text
[2600] so potentially we could
[2602] use exactly the same parameters for the
[2605] two towers and that is what is called as
[2606] a missile encoder
[2609] and then we try this on on several
[2612] question answering data sets
[2615] and
[2616] we observe
[2617] and for here we use t5 also so the two
[2620] the two encoding towers are initialized
[2622] are initialized as t5 and then they're
[2625] fine tuned on these positive and
[2627] negative examples for the dual encoder
[2629] and as you can see here we got
[2632] significantly better results on
[2635] on using the visual encoder using the
[2637] same encoder for both of them
[2640] so we wanted to understand why and what
[2642] is happening here
[2644] and we tried three hybrid approaches
[2646] between the siamese and the asymmetric
[2648] encoders in the first one
[2651] we
[2652] pro
[2652] we
[2653] we force them to be asymmetric but we
[2656] share token embeddings so they have
[2658] something in common
[2660] in the second one we froze token
[2662] embeddings
[2663] to the t5 ones and in the third one we
[2667] went to the other side of the tower and
[2669] we forced them to share the parameters
[2671] for the projection layer the layer at
[2673] the very top
[2674] and we compared these three these three
[2676] hybrid alternatives
[2678] and what we saw is that
[2681] sharing embeddings doesn't really help
[2684] the performance is very very similar to
[2686] asymmetric dual encoder but sharing the
[2688] projection layer makes the asymmetric
[2691] dual encoder perform as well as some as
[2694] a symmetric dual encoder they're pretty
[2696] much a distinguishable
[2698] so let's see
[2700] and this is the
[2702] the
[2704] the sciam usual encoder improvement over
[2706] the asymmetric dual encoder on mean
[2709] reciprocal rank
[2711] and you can see for that for the
[2712] different datasets there's a mutual
[2714] encoder
[2715] the increase in performance versus the
[2717] asymmetrical encoder is very similar to
[2719] the asymmetric dual encoder with the
[2721] share projection layer
[2723] so they're basically performing the same
[2728] and and the improvement
[2730] becomes bigger the larger the model is
[2733] this is this is also something
[2735] interesting to see
[2736] with t5 large it's much bigger
[2738] improvement by being symmetric
[2740] so then we tried
[2742] plotting the embeddings for both
[2745] questions and answers on the
[2747] two-dimensional space
[2749] and
[2750] this image makes it pretty obvious what
[2752] is happening here in the asymmetric dual
[2755] encoder when you have two separate
[2757] towers with with different parameters
[2760] each of the two towers is projecting the
[2762] input to different regions in the space
[2766] and yes it's trained to force the
[2768] question and the answer are as close as
[2770] possible but because they don't share
[2772] any parameters
[2773] the each tower just choosing one region
[2776] in the space
[2777] and plus the things in into there and
[2779] all the questions come in this place all
[2781] the answers come in this place
[2783] there's a mutual encoder
[2785] is basically projecting everything in in
[2786] the same region in the same space
[2789] and there is much more flexible to
[2791] ensure that the question and an answer
[2793] are very close together
[2796] now if you look what happened with the
[2797] hybrid models sharing the projection
[2800] layer has exactly the same
[2802] effect that that we had with the same is
[2804] well encoded everything is projected
[2806] into the same space because the layer is
[2808] the one at the top the one producing the
[2810] final embeddings and has that ability
[2813] sharing the embeddings is not really
[2815] helping because they're at the beginning
[2817] and then the rest of the towers are
[2818] completely completely separate and one
[2822] advantage here is that
[2825] sometimes
[2826] you cannot use a missile encoder as i
[2828] was saying at the beginning if you're
[2830] talking for are very different types of
[2832] data like images and text or video and
[2834] text
[2835] then you cannot use siamese all encoders
[2837] there are different architectures
[2839] but you can have two asymmetric
[2842] embedding towers
[2843] as long as you share the projection
[2845] layer on top you can force the two
[2848] towers to have this effect to be
[2850] projecting things into the same space
[2854] so
[2855] just to conclude
[2856] i gave an introduction to large language
[2858] models and
[2860] they represent current state-of-the-art
[2862] for close book question answering
[2865] and
[2866] we did some explanations that try to
[2868] shed some light on limitation of
[2869] possibilities and current approaches
[2872] specifically looking into memorization
[2874] of knowledge and looking into more
[2876] embedding-based retrieval models for for
[2878] solving these tasks
[2881] and some of the conclusions
[2883] i just
[2885] wrapping up is
[2887] we saw that for
[2889] infusing data into the know into the
[2891] into the network
[2893] we don't really need to go through
[2895] natural language we can just
[2898] dump the triples as they are and it
[2901] works pretty well the larger models
[2903] benefit more from knowledge in fusion
[2906] uh
[2907] i skipped very quickly through it but we
[2909] also did experiments with smaller
[2910] knowledge graphs
[2912] as
[2913] all of this is very intuitive but it's
[2915] good to to test it empirically the
[2917] smaller the knowledge graph the better
[2919] the memorization and the better the
[2921] improvement like we tried with a movie
[2923] specific knowledge rap with a hundred
[2924] thousand facts
[2926] and the movie qa data set
[2929] and there the accuracy went from like 20
[2932] to 75 percent the accuracy of the
[2935] answers so basically it's memorizing a
[2937] lot of the knowledge graph and it's
[2939] actually being able to apply it
[2941] in the case of wikidata much bigger
[2943] knowledge graph you need much bigger
[2945] networks to memorize it and and even
[2948] even the large t5 models are struggling
[2951] to
[2952] to
[2954] to to memorize a knowledge as large as
[2957] wiki data
[2959] and looking into the retrieval models
[2961] one one of the conclusions we got is
[2963] that sharing projection layers
[2966] enables asymmetrical encoders to perform
[2969] competitively with the siamese ones and
[2972] we recommend to use this share
[2973] projection layer in this kind of setup
[2977] thank you everyone
[2980] [Applause]
[2988] thank you thank you enrique for the
[2990] brilliant presentation and
[2993] bringing to us this bleeding edge of
[2996] research at google so
[2999] i'm sure there will be a lot of
[3000] questions now from the public
[3003] yes
[3013] hi thanks for the great talk very
[3015] interesting i have two questions
[3018] but before i go there i have to draw a
[3020] big picture because i'm questioning a
[3022] bit of status quo where will it go in
[3024] the future
[3025] because now we are in a connection this
[3027] world we just increase ever the data
[3030] size and the model size which you just
[3031] mentioned what you show them is the
[3032] coming role c4
[3034] it's having some knowledge but it's
[3036] missing the knowledge so it's great what
[3037] you're doing that you're adding the
[3038] knowledge graph knowledge let's say to
[3040] get more efficient but it's still not
[3042] there where we should go
[3044] and now currently has some you know it's
[3046] in a bit in the space where the current
[3048] ai research is in general
[3050] that um
[3052] with ever increasing
[3053] have increasing models big companies
[3055] like google or all the other big
[3056] companies can do state-of-the-art
[3058] research but here small startups and
[3060] small companies are a bit left out of
[3063] you know current research so it's
[3064] actually killing some some innovation
[3066] and not to mention the costs in general
[3069] computational costs but also the carbon
[3070] footprint which is also actually a
[3072] bigger bigger problem
[3074] so
[3075] now in this connectionist world we have
[3077] the sequence to sequence models and
[3079] transformers with the attention base
[3082] gray q value position encoding mass
[3085] language modeling next sentence whatever
[3087] prediction it's doing this
[3089] sequence to sequence mapping perfectly
[3092] but it's still a bit blind let's say
[3094] because it's somewhat missing that uh
[3097] let's say not a symbolic ai knowledge
[3099] that is semantic knowledge of it because
[3101] when i look at it how
[3103] because it's trained on the unstructured
[3104] text
[3106] and so this is actually a bit redundant
[3107] in my sense why not actually removing
[3110] stub and fill words or doing some named
[3112] android recognition and
[3113] part of speech tagging so you're
[3115] reducing actually the amount of
[3116] computational power you need to to model
[3119] all that and it actually annoys what
[3120] you're doing with the knowledge crafts
[3122] that you're actually
[3123] having a bit more condensed knowledge
[3126] letting the language model learn all
[3128] those facts
[3129] and so i thought can you do
[3132] a new transformer based attention model
[3135] which is then getting more into
[3136] efficiency
[3138] to avoid the bigger carbon footprints
[3141] and then also with the knowledge class
[3142] what are you showing at the moment you
[3144] do explicit or implicit fusion into the
[3146] language model can't you do a new
[3148] generation of language models which is
[3150] just based on the knowledge graph
[3151] because there you have the symbolic
[3153] knowledge and then you can actually
[3154] scale up over the whole knowledge of the
[3156] whole world
[3157] so you're way more efficient and also
[3160] then maybe such models can be used at a
[3162] small
[3163] startup a research university and so i
[3166] hope the answer is somewhat yes that
[3168] google is going to
[3169] another symbolic ai and getting more
[3171] efficient maybe we should let the
[3172] speaker yeah
[3173] i'm soon finished
[3175] um so i hope the answer is yes because
[3177] the the the ending that joke with maybe
[3180] i hope not that larry and and sergey
[3183] invented the company google
[3185] referring to the number go goal which is
[3187] a very big number so it actually to
[3189] store the whole knowledge of the whole
[3190] world and language model i hope not we
[3192] are ending up with a global number of
[3194] parameters
[3196] yes you bring up very interesting topics
[3198] here
[3199] and i'll another question i'll cover two
[3201] or three of them
[3203] one
[3203] i i have a much more optimistic view
[3206] about
[3208] big companies and smaller companies now
[3209] because if you look at it
[3212] anyone can take
[3214] today a t5 checkpoint
[3216] and run it
[3217] or find unit and
[3220] the file one of the advantages of these
[3222] models is that they have been
[3223] pre-trained on so much amount of data
[3225] they have so much knowledge encoded
[3227] inside of this checkpoint
[3229] that
[3230] for tesla before you needed a lot of
[3232] training examples to fine-tune now you
[3235] can annotate with humans a much more
[3237] smaller data set a thousand examples
[3239] sometimes not even that sometimes you
[3241] can use few shot
[3242] and just show to the model two or three
[3244] examples
[3246] and then the model is able to do a
[3247] relatively good job out of that and
[3251] in this way i feel that large language
[3253] models are becoming a commodity you
[3256] don't have to be
[3258] to have a phd on the topic to be able to
[3261] use a large language model anyone can go
[3263] into github can download the t5
[3265] checkpoint
[3267] and come
[3268] and can start playing with it and come
[3271] build
[3272] product applications out of this that a
[3274] few years ago were science fiction
[3276] so i i i feel that the entryway is
[3279] actually going down
[3281] i think we should give the opportunities
[3282] water to ask questions if you want you
[3284] can ask the question later
[3286] okay yeah it would be somewhat related
[3288] to my current sorry it would be
[3290] somewhere related
[3291] because then data centric ai now we had
[3294] the modeling
[3295] can you construct
[3298] a knowledge graph based on my current
[3300] data but then the knowledge graph is
[3301] growing on my data and then you realize
[3303] that say sentence similarity oh actually
[3305] twenty thirty percent of my data is
[3307] absolutely because i already learned
[3308] this and so the knowledge graph is
[3310] showing
[3311] me the ways to perfectly construct a
[3313] balanced data set and use you reject
[3315] thirty percent and then you know
[3317] extrapolation i need to add some other
[3319] parts to to have a perfect data set
[3322] yeah there are many many research
[3324] directions actually related to the
[3325] topics you have mentioned like for
[3327] example you mentioned carbon carbon
[3328] footprint as well and consumption and
[3331] indeed
[3332] i'm not so familiar with side of the
[3334] work but between dedicated hardware for
[3336] example is is one line of work that
[3339] tries to re to reduce the energy
[3340] consumption for training these models
[3342] other lines of work are more sparse
[3345] networks that the transformer not all
[3348] layers are fully connected by looking
[3350] into ways to make the much more
[3351] responsive using the parameters and then
[3354] speeding up training data all of these
[3355] are active lines of research how to make
[3357] all of this more efficient and less
[3359] energy energy greedy
[3361] and another interesting topic that you
[3364] raise is this
[3365] memorization versus relying on knowledge
[3368] graph
[3369] and indeed i think that
[3371] relying on explicit knowledge graph has
[3373] many advantages versus memorization and
[3375] and
[3376] the model has to do a very very
[3378] different task when it's doing retrieval
[3380] versus when it's memorizing when it's
[3381] memorizing you're expecting to have a
[3383] huge network that has enough capacity
[3385] that encode everything inside in the
[3387] ways but when you're doing retrieval
[3389] is a completely different task to
[3391] perform a much smaller models can do
[3393] better there because a task is given
[3395] this input how to produce a query or an
[3398] encoding to retrieve the right answers
[3400] and then the answers will contain the
[3401] content i need to reason over these
[3403] answers to pro to produce the output and
[3406] you need much smaller capacity for that
[3408] a smaller network so it it changes the
[3411] paradigm a lot
[3413] i think there was another question yes
[3415] uh thanks also from my side for the nice
[3417] talk my question was concerning these
[3419] examples where the model was giving
[3421] confident but wrong answers are there
[3424] any attempts
[3425] using these knowledge graph techniques
[3427] to
[3428] incorporate uncertainty to maybe i don't
[3430] know say i don't know but my best guess
[3433] is john ford
[3435] there
[3436] there are different approaches for that
[3439] but
[3439] um
[3442] i think it's a very active research area
[3445] so it is not at all sort of problem
[3447] one way to improve no to improve
[3449] grounding is precisely through to use
[3451] retrieval augmentation
[3453] so you you could have the language model
[3455] actually issuing a search to a search
[3458] engine or is you a request to a
[3460] knowledge graph and then retrieving the
[3462] answers
[3463] and that is proven to to increase the
[3466] the accuracy of the answers a lot so
[3469] mo i think most of the research most of
[3471] the research work i've seen about it has
[3473] been about
[3474] increasing the accuracy increa by
[3477] grounding into some
[3479] some trustable data set
[3482] not so much about producing a confidence
[3484] because i i think
[3486] that's not so well understood how to get
[3489] these mothers to produce a
[3491] confidence because
[3493] the answer might not be very confident
[3495] because of language modeling problems
[3497] with the answer or because of factual
[3499] factuality of the answer and it's
[3501] difficult to distinguish
[3502] these cases
[3505] thanks
[3517] hi thank you for the nice talk i have
[3519] two questions one like little bit
[3522] specific and one general
[3524] so the
[3525] specific question would be how these
[3527] models can handle like uh negations or
[3530] balance shiftings
[3532] uh in general like for example for
[3534] sentiment analysis
[3536] um
[3537] you are doing some research in that area
[3539] and the general question would be how
[3541] would we construct like a knowledge
[3544] graph
[3545] in an unsupervised
[3547] approach like uh from the text
[3549] specifically
[3550] how the
[3551] edges can be labeled in a generalizable
[3554] way or to generate the triplets from
[3556] sentence the reverse process
[3559] thank you so
[3561] the pre-training is already
[3564] capturing
[3565] metaphors and negations and and many
[3568] many other linguistic phenomena
[3571] uh
[3572] simply based on on the size of the model
[3574] and the size of the corporate has seen
[3577] if you have a specific application you
[3579] want to apply this model to say for
[3582] example review sentiment analysis
[3585] typically what you will do is to first
[3588] take a vanilla
[3589] a large language model and and run it as
[3592] zero shot or few shots and see how well
[3594] it does
[3595] and you may be surprised and it already
[3597] performs well enough to meet your
[3600] quality bar that you were expecting and
[3602] if that happens is great
[3603] if that doesn't happen and there is a
[3605] specific
[3607] specific pattern of inputs that the
[3609] model is not performing well on
[3612] typically people do active learning at
[3614] that point
[3615] so the human
[3617] collection of human annotated data
[3620] that that the model is making mistakes
[3622] or is close to the decision boundary and
[3624] their her positives her narratives and
[3626] then fine-tune the model on this so
[3630] like standard machine learning
[3632] approaches applied to llm are applicable
[3635] to llms as well
[3638] about
[3639] inferring the kg from the llm i
[3643] sounds like a very exciting task but i
[3644] personally not worked i have not worked
[3647] in in
[3648] on that in google
[3650] and but it sounds like some very
[3652] exciting tasks to
[3654] to formulate us as a text to test
[3656] problem and and and try to see how well
[3659] it does yes
[3661] thank you
[3664] so
[3665] yeah
[3666] thank you very much for your talk so i
[3668] have to admit i'm one of those people
[3669] who treats these models more like a
[3671] commodity so i have a question a bit
[3673] about the training procedure
[3675] so i remember a couple of years ago when
[3678] you had like these
[3679] massively multitask models like they
[3681] would all kind of suffer from this
[3683] catastrophic forgetting problem
[3685] and
[3686] here it seems like it's basically a
[3687] solved problem now so can you maybe give
[3690] us
[3690] an intuition like how you deal with that
[3693] during if it's the training procedure if
[3695] it's just the size of the model like
[3697] what happened
[3698] forgetting that's happened we've seen it
[3700] happen in these large language models
[3703] and
[3703] and it's very typical you get the t5
[3706] checkpoint
[3707] and the pre the vanilla checkpoint may
[3709] be applied to a certain task and it does
[3711] very well and then you find unit on your
[3714] fine-tuning data
[3716] and it
[3717] and it overfits your find unique data
[3719] basically and it forgets a lot of things
[3721] that it has learned during pre-training
[3723] and then you see when when when applying
[3725] to unseen data
[3727] sometimes the vanilla model does better
[3729] than the fine-tuned model if if this has
[3731] happened so it's something that we see
[3732] in practice
[3734] the typical approach there is to be very
[3736] careful about the mixing proportions
[3738] when you're fine-tuning
[3740] if you see some kind of forgetting
[3742] happening
[3743] you include you include a mixture with
[3745] the data that you see the model for
[3747] getting and there is a little bit of
[3750] of cooking also
[3751] to
[3753] to trial and error to decide what is the
[3755] right mixture proportions here
[3758] okay thank you very much sure hi um
[3763] another question um
[3764] you mentioned that these models can be
[3766] considered as commodities and
[3768] they are lower in the entry bar and
[3770] everything but then it has been shown
[3772] that this model uh models can have a lot
[3775] of bias and there are there is a lot of
[3777] underrepresented uh population
[3780] communities and also underrepresent an
[3784] underrepresented way of uh
[3786] conceptualizing the things so
[3789] we are
[3790] we need to kind of believe that
[3792] these big companies are
[3794] doing their proper work to to handle
[3796] this and on how
[3798] are you tackling this kind of problem
[3801] yeah so we
[3803] when whenever we take these language
[3805] models and we want to apply to
[3807] production
[3809] google has by now some pretty big themes
[3812] about fairness in artificial
[3814] intelligence and inclusion and
[3817] and typically
[3819] these are experts on these things and
[3821] then they have specific data sets and
[3824] and they have expertise with with atom
[3827] and typically when when you want to
[3829] bring something like this into
[3830] production is
[3832] you you have to schedule office hours
[3834] with these teams you have to explain how
[3837] you how you have training how you have
[3839] to apply them and
[3841] often they ask you to
[3843] to run it in some of their data sets or
[3846] or
[3847] even to construct a new data set
[3849] specific for your task
[3851] having this in mind so indeed it's a
[3853] very important topic
[3855] and within the company we have processes
[3857] in place to
[3859] to catch as many as possible of these
[3862] potential biases
[3865] before a model like this is actually
[3867] integrated in a real application
[3876] all right so thanks if there are no auto
[3878] pressing questions we finish here we
[3880] conclude with a little present from the
[3882] organizer for our speaker
[3886] so enrique thank you very much for being
[3888] with us today
[3891] google
[3894] now
[3896] a bit of information we have the coffee
[3898] break outside and after the coffee break
[3901] in 25 minutes we'll start again here
[3904] with the business application
[3906] session and upstairs with the junior
[3908] truck session one
[3912] enjoy the coffee break
