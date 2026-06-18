---
schema_version: 1
id: yt-jDxUcHR9zR0
type: youtube
title: NODES 2024 - Multi-Agent Query Generation w/ LLMs on Complex Knowledge Graphs
url: https://www.youtube.com/watch?v=jDxUcHR9zR0
authors:
- Neo4j
ingested_at: '2026-06-17T18:15:01Z'
content_hash: sha256:f987843f6a15a50c0cfef417be579153838d25819b624c4ee6dc57d4cbc204ee
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 1883
  caption_track: fetched
  snippet_count: 694
filter:
  score: 0.7
---
[9] thank you Isa hello everyone thank you
[12] for joining today we will uh explore how
[15] we can leverage large language models to
[18] ask question to a Knowledge Graph using
[20] just Nal
[22] language the goal is to let to uh the
[25] main experts to be able to tap into the
[27] power of connected data even if they
[30] don't have the technical skills that are
[32] required to write sep queries for
[34] example and we want to leverage large
[37] language models because they are showing
[39] this ability to do language
[42] understanding do some sort of reasoning
[45] and they are able to generate context uh
[48] that's useful for our task and they are
[50] getting better and better over time so
[53] before diving in how we believe is the
[55] best way to tackle the problem let's see
[58] how this question answering systems are
[61] built today so the most widespread
[64] approach these days is rag retrieval
[67] augmented
[68] generation uh the idea behind rag is
[71] that not every question can be answered
[73] by llms alone if I ask who call in my
[77] company to get a new printer for example
[79] the llm cannot give me an answer because
[81] they don't know about my company in in
[84] other words the data that is required to
[87] answer my question was not in their
[89] train
[91] set what we can do what I could do is to
[94] give for example along with my question
[96] I can give information like my or charts
[100] or the list of responsibilities in my
[102] company in this case that's another
[104] story because the llm are very good on
[107] identify the piece of information needed
[110] to answer my question if I provide this
[113] type of contextual information so the
[116] idea behind rag is that there is the
[119] extra component is called the retriever
[121] here and it can be implemented in many
[124] different way but what it does uh in a
[126] act shell is to perform some sort of
[128] semantic search considering your query
[131] uh your question against all the docents
[134] that you have all your knowledge base
[136] and the retriever is able then to
[138] identify the semantically most relevant
[141] documents and you then can use those
[143] documents as a context along with the
[147] question to be sent to the llm and the
[148] llm can use this information to ground
[152] uh the answer
[154] on okay this system works but it has
[158] some uh limitation first of all rag rely
[162] evly on the retrieval if the retri
[165] retrieval pH fail to extract the
[169] relevant documents it will give in
[171] complete information the llm cannot help
[174] with the answer imagine that you have a
[176] challenging question uh user can start
[179] asking this type of questions and this
[181] type of question usually require many
[185] different pieces of um critical
[188] informations and those pieces may be
[190] spread among multiple documents maybe
[193] even not related uh these documents
[196] between each other so since retriever
[198] can grab so much content there is some
[201] chance that some of this piece of
[204] critical information will be
[205] missing so when you provide an
[208] incomplete uh um you know contextual
[211] information to the llm bad thing happens
[214] because the llm will try anyway to give
[216] you an answer they will try is best even
[219] if you have to make up uh content so you
[222] can give a wrong answer because you
[224] provide incomplete uh context and it is
[227] difficult to talk this problem is
[229] difficult to tle because you know the
[231] llm try to give you a confident answer
[233] even if they are missing some critical
[236] information we call this
[238] hallucination and uh is not the only
[240] problem I I think it's this the rag
[243] approach is definitely not something an
[246] expert would do so what will an expert
[250] do then imagine that you have to answer
[253] a question and you have a knowledge
[255] graft for doing that what you will do
[257] the first thing you will do is to go to
[259] the schema to try to make sense of this
[261] knowledge graph and if if the question
[263] is about uh people the answer has to has
[267] some reference to to that person node
[271] that you have found into the schema now
[274] imagine that we are in a law enforcement
[276] setting and someone ask you to get the
[278] list of all the red Camaros that were
[281] spotting in a certain area in a certain
[283] point in time what you will do well the
[286] first thing you will do is to go to the
[288] scheme and try to find no like car or
[291] vehicle and when you get that you will
[294] try to find the schema anything that can
[296] actually spot a vle and you may find an
[298] NPR camera for example for those camera
[301] that can read your PL number uh in that
[304] case you know that you are almost there
[307] uh so you need something that connect
[308] these two idea these two concepts and
[311] then you may find in the schema a
[312] relationship or you may find a camera
[315] event in that case you get it right
[317] because you have camera NPR camera
[320] generating a camera event the camera
[322] event is capturing a vehicle vle maybe
[325] is owned by someone a person you got it
[328] you have a traversal once you have your
[330] traval what you will do is to start
[332] applying constraints you're not
[334] interesting on every single camera in
[336] the world but you want to just know the
[338] ones that lay into the area of Interest
[342] same thing for the events you just want
[344] to know what happens in that time frame
[347] another constraint the car has to be red
[350] the model has to be come out where youve
[352] got it you have constrained traversals
[355] and you can use these constraint
[357] traversals as a building block to write
[360] uh query using uh a formal language like
[363] cyppher and you can execute this query
[366] formally against your knowledge graph
[368] and what you get from there is actually
[371] exactly the information to result you
[374] after and there is zero chance to
[376] hallucinate in this stage okay so then
[379] when you got your results your notes and
[381] relationship you decide how to present
[384] them you can present it like a graph or
[387] a chart or using a map a table whatever
[389] you say FS depending the question that
[391] they give you so that's what an expert
[394] will do roughly so let's see this um
[397] approach on an llm perspective let's try
[399] to see if we can automate those process
[402] this process so what we really need is
[406] first of all we need the ability to
[408] reason because we have to translate a
[410] question into some sort of
[412] plan then we need the ability to do some
[416] perform some sort of semantic search as
[418] rag does but not on the wall data but
[421] just on our metadata on our schema uh we
[425] can see this problem from another angle
[427] imagine that this this could be
[429] described as a translation Pro problem
[431] to words a foreign language in this case
[435] um uh Cipher will give you the grar but
[438] the schema is going to give you the
[439] vocabulary the terms that you will need
[441] to tell your foreign language and then
[443] it's a matter of translating using
[447] alens we also think that this kind of an
[449] X expert based approach is also implying
[452] some sort of paradigm shift because we
[455] are moving away from from the concept of
[458] how to generate the answer which is what
[460] drug does toward something like more how
[463] to ask the question properly and we
[466] think this does a lot of the
[469] difference now before moving on and show
[472] you a demonstration how we Implement
[474] those ideas uh let me stress a bit this
[477] um expert approach concept uh basically
[481] uh I'm going to show you the
[482] demonstration using graph of y which is
[484] our Y which is our graph analytic
[487] platform and we build this platform this
[489] software for analysts so for people that
[493] has to uh you know answer critical
[496] questions using Knowledge Graph every
[498] single day we have buil feature for them
[501] as you can imagine we buil the ability
[503] to for them to describe a conceptual
[505] schema on top of the schema less and for
[508] J we are the ability to uh annotate with
[511] free text basically anything uh classes
[516] property anything so they don't have to
[518] rely just on the name of a of a
[520] relationship for example to know what
[522] this relationship is doing in general we
[526] build feature for them and what you will
[528] see is that we leverage all those
[530] features in our solution because the llm
[533] is trying to mimic their behavior so the
[535] LM is going to face the same type of
[538] problem for which we already have propos
[540] some solution to our user and if you
[543] think about that this is kind of true in
[546] general because if you already have a
[548] product and you want to transition
[551] towards a jni solution if your solution
[555] is mimic what the the behavior of a user
[559] you won't end up with a backlog filled
[561] by feature that compete between you know
[564] features that improve uh the user
[567] experience or feature that improve the
[570] llm answer or the quality of the answer
[572] for example and we believe that this
[574] something uh important from a product
[577] perspective especi especially if you are
[579] on a transition
[581] stage okay so now let me uh show you um
[586] live demonstration so this is yum this
[589] is basically the
[590] visualization uh tool of yum that the
[593] analysts use to navigate the graph and
[597] uh what we have added is this um
[600] um user interface so we can use to
[603] interact with our system so this is um a
[607] laow enforcement Knowledge Graph you see
[609] this schema here and I will pretend
[611] today to be an investigator and I want
[614] to start my investigation so I can ask
[616] question here I will start to something
[618] very basic I'm asking to have a crime
[621] node so I can start my investigation you
[623] see what happens is that when I hit the
[626] button uh my question is sent to the
[629] system a along with the the schema
[631] description and uh we can use this um
[635] the system we use this information to
[637] implement on a multi-agent approach what
[640] I have described so far and the result
[642] you get are basically what you see here
[644] we have a note and we have a couple of
[647] textual results we have the reasoning
[650] and a summary so the reasoning is useful
[652] for two purposes first of all it will
[655] give you um it will give your user an
[657] understanding of what's Happening under
[658] the hood so
[660] basically the the idea is that um we
[664] don't show just notes and relationship
[665] on the compass uh but we give also you
[668] know an explanation or a plan of what's
[670] Happening uh this is useful if you have
[673] a complex schema for example then you
[676] may Travers the same thing with
[678] different relationship in a slightly
[681] different way and since we are using you
[683] know natural language there can be some
[685] ambiguity so knowing the plan it will
[688] help your user to fix any misunder
[690] understanding down here typing a few
[693] words and clarify what has to be
[695] clarified it's also useful for um the
[698] machine because the model is forced to
[701] generate all these token that you see
[703] here before generating the answer this
[706] gives the model so call uh time to think
[709] so the model won't rush into some
[712] obvious but perhaps wrong answer
[715] straight away so again this is something
[717] that it's useful for both the the
[720] machine and the people and we have the
[723] summary here so we can have a look what
[725] is this CRI so we can see here is a
[728] criminal trespass uh we know the date
[732] it's under investigation and uh we see
[734] from the report that there is a vehicle
[737] black vehicle involved with a partial
[740] plate now so what I can do is to select
[743] my crime and ask this question down here
[747] like I'm searching if there are an any
[751] NPR camera uh within uh nearby okay you
[755] see the system give me the results and
[758] they also switch into a map view because
[760] is it's SM enough to understand that
[762] it's the best way to present this
[763] specific type of information and that's
[766] true not only because you see that the
[768] NPR camera Z here is pretty close to the
[771] crime uh node but they also position it
[774] in a in a strategic position so we can
[777] get some interesting um get some
[780] interesting leads for for our
[781] investigation so let me select the
[783] camera this time and I will ask um if
[787] there were some vagle uh there were spot
[790] in the DAT of the incidents that are
[792] compatible with the description
[795] okay uh so let me okay so what we got
[799] here is
[801] Ana a graph expansion of all the no that
[804] matched my my question all the vehicles
[807] that you see here are potential
[809] candidate is for f
[811] investigation uh and if I look on the on
[813] the summary there is not much of extra
[816] information here we got basically what
[818] you see to the compass so let me try to
[821] do something different let me select
[824] just the
[826] uh the crime and the camera I I want to
[830] try to ask the same question but in a
[832] different way here I'm not saying just
[835] give me notes all right I'm saying look
[838] I'm an investigator and I'm working on
[841] the selected crime and uh where I am
[844] here we go and I need this type of
[847] answer so I'm not saying what I want I'm
[849] just referring to what I have selected
[851] okay but most
[853] importantly um and seeing here like um
[858] I'm basically asking for insight I'm
[860] asking uh if among this result there is
[862] something that is more likely to be
[864] involved compared to others so as you
[867] can see from the result there is not
[869] much of um of difference right we have
[873] basically the same results but so this
[876] means that this type of changing the
[878] question doesn't affect the text to
[880] Cipher agent for example but probably it
[883] will have done something on the summary
[886] step let's
[887] see yes we have here the same uh summary
[891] but we have an extra step here and if
[894] you read through it says that the vable
[897] ab1 I think this one
[901] was deducted twice within a short time
[903] frame that's
[905] true and uh which my indicated an high
[909] likehood for involvement of incidence
[911] compared to other people so we're
[912] basically saying let me select back we
[914] basically say that this veal is actually
[917] uh more uh interesting from from
[921] investigation perspective so let me try
[923] just one last
[926] thing here so I'm not touching anything
[929] I'm basically asking the same question
[932] but I just Notch a bit the system say
[934] look sometimes those Bagel are owned by
[937] uh previous
[938] offendor so let's see how the system
[941] answer to this question here we go so
[945] you see now that uh it expand further
[948] and you found that amongst all this
[950] vehicle just one is owned by this guy
[954] and if we look at the summary he said
[956] that the black chevrol every compatible
[958] plate was detective okay and its owner
[962] is Sean on whatever and we say that he
[966] has okay that's an important part who
[968] has an history of previous offenses
[970] specifically has committed crimes
[973] including battery and Criminal Trespass
[976] and this is important because Criminal
[978] Trespass is exactly what we are
[980] investigating so with a few question you
[983] see that we have now a vehicle that is
[986] strongly tied to the location the owner
[989] of of the vehicle which has a criminal
[992] history that is compatible so we can we
[994] definitely have uh you know enough
[996] information to to say that this uh this
[1000] person here can be actually um a good
[1003] candidate for the suspect is it's
[1007] potentially a suspect and we can start
[1009] the investigation we can further
[1011] investiga on on this
[1013] person okay so this is example we are
[1016] basically showing that how we can use
[1018] this system in a sort of realistic
[1021] setting and also how we can push a bit
[1025] the um the the summarization steps and
[1030] how we can leverage this step to
[1032] actually give us more um Insight
[1036] considering the data and this is
[1037] important especially if you have many
[1039] data on your
[1040] campus okay
[1043] so uh I think that I can uh spend the
[1047] rest of the time to show you how we
[1049] implement this
[1051] exactly so let me switch to Orchestra so
[1055] this is Orchestra this is our
[1057] orchestrator to is basically a low code
[1061] uh tool that we use to basically dry
[1064] draw any type of workflow and this is a
[1067] the war workflow that we use to
[1069] implement everything you see so so far
[1072] anything you saw so far so it can be it
[1074] can seem complicated but it is not
[1076] actually so uh up here we we have um um
[1080] an initialization step we basically
[1082] write down all the prompts the template
[1084] for the prompts and uh I will I will
[1088] show you those
[1091] briefly and uh down here we have the um
[1096] error and Ling stage so basically since
[1099] we have you know statistically uh
[1102] statistical systems that can do can
[1104] provide any type of uh response we have
[1107] to deal with errors this is something
[1109] that will happen Okay so what happens is
[1111] that we uh capture the the error when
[1115] they happen and uh we we do some
[1118] postprocessing from the error for the
[1120] error and we also give them another try
[1123] if it is the case so we can fix it
[1125] something and rerun and give it another
[1127] another
[1129] shot okay so uh this is the main flaw so
[1134] from here we start so um in Orchestra
[1136] all the components that you see here
[1138] basically take one message in which you
[1141] can see like a sort of a Json object and
[1144] then they do some processing and give
[1146] you a Json out another message so it's
[1148] basically a stream of messages and uh
[1152] and you can see the flow here so the
[1154] first thing that happens is that when I
[1156] hit my button I basically call this
[1158] webook and so the flow uh starts so the
[1161] first thing that we do let me zoom in a
[1163] bit the first thing thing that we do is
[1167] to uh to do the intent that section so
[1170] what we are trying to do here is to uh
[1173] okay this is the let me go here on
[1177] the okay so this is the uh the output of
[1180] the previous stage so we will see the
[1182] results in here so basically um what we
[1188] do here is to try to understand the type
[1190] of output that the user expects
[1192] considering the question like in example
[1195] we want to be a map when it's the case a
[1198] chart graph in depending of the type of
[1202] question okay so we implement this stage
[1204] this agent basically through um a sort
[1207] of a classification uh uh task so we
[1211] support graph table chart and maps in
[1214] our view so we say that he can choose
[1217] between those we explain a little bit
[1219] better what they
[1221] are we give some examples down here and
[1224] then we ask the
[1226] question and this is the type of results
[1228] that we have so we are interesting on
[1230] this string basically and then we have a
[1233] reason uh output so the reason is not
[1236] something that we to actually
[1239] surface but it's still something useful
[1241] because you can use the uh this reason
[1245] field in case of
[1247] misclassification so if for some reason
[1249] the system is wrong it won't give you
[1251] just graph but we tell you why I think
[1253] that is C okay so you can use this type
[1256] of information basically um to write
[1259] write down an extra examples here for
[1261] example and this can be used to classify
[1264] specify better the boundary for example
[1268] okay this is sort of a a basic or a
[1270] standard way to to deal with the with
[1273] the classification problem so I will
[1274] move on quickly so the next thing that
[1277] we do is to convert the schema that I
[1280] showed you at the beginning to something
[1282] that the llm can
[1284] handle uh let me show you this schem to
[1287] okay this is the way that we can Define
[1289] schem
[1290] manum uh you see we have classes with
[1294] property relation same thing if I go
[1296] here on a vehicle uh you see we have a
[1299] description uh to the attribute color
[1303] and it is like um specification that the
[1306] color code has to be this one like if we
[1308] say black we actually mean Blk and
[1311] that's important for the constraint part
[1314] okay so what we have to do what we do in
[1316] that step is to take all these
[1318] representation
[1319] programmatically I convert it into um a
[1322] format that the llm can handle and I
[1325] think I can show you here
[1328] yes for example for the relationship we
[1330] use this type of format you see we have
[1333] the source class the end class the
[1335] relationship and also property with the
[1337] type if there are so we have a list uh
[1341] of rep of text representation of the of
[1344] the relationship uh same thing for notes
[1347] we use this format here in which you
[1349] have a class uh and the relation sorry a
[1353] class the properties with their uh with
[1355] their um
[1356] type okay so uh what we do next is to
[1360] fetch The annotation that I showed you
[1362] earlier and every single annotation that
[1364] can be put already into the graph and
[1367] into the into the schema as as a
[1370] description and then we collect all this
[1372] information to build a prompt and I can
[1374] show you the prompt I will show you the
[1376] template because I think it's easier to
[1378] follow uh here we
[1381] go so this is the template this is a
[1384] ginger to template uh okay we have a mro
[1387] at the beginning this deal with the
[1389] example so if you provide an example it
[1391] will use yours otherwise you will use
[1393] some default example so the prompt
[1396] basically Starts Here we say that is a
[1398] text to Cipher uh task basically we show
[1403] uh the user question we expand it with
[1405] the actual question then we show the
[1407] schema and use the format that I just
[1410] show you right so we have the nodes here
[1413] the relationship here
[1415] expanded then if the output format we
[1418] identify the preview step is graph or
[1421] map we uh give some requirements how we
[1424] want this graph to be to be extracted if
[1428] it is a um um a table we do basically
[1432] the same
[1433] thing uh then we show the
[1436] examples then we show The annotation and
[1438] every single annotation we have as I
[1440] showed you earlier and then we show
[1442] again the question uh we repeat the
[1444] question down here because um this
[1448] section here can be pretty large
[1450] depending how large and how many
[1452] property your scheme has this can be
[1454] pretty large so we don't want the
[1456] question to be too far away from the
[1459] from the response you know two tokens
[1461] away from the response to improve the
[1463] quality uh yes basically from the same
[1466] reason we repeat the requirement if it
[1469] is the case and then we uh specify the
[1473] type of response that we have so we
[1476] basically expecting a Json response the
[1480] first and the Order of these properties
[1482] is important so the uh the first thing
[1485] that we that we ask is the relationships
[1487] or at least any relationship they think
[1489] may be useful to TS then we have the
[1492] reasoning and the reasoning is what res
[1494] surface is what you saw basically in the
[1498] um in the visualization and then we have
[1501] the query so the order is important
[1503] because the query has to be um
[1507] consistent with the reasoning that you
[1509] already the model has already generated
[1512] right so basically this reasoning is the
[1514] so called time think that I mentioned
[1517] earlier all right I think I can show you
[1521] also an example of how it is
[1524] expanded so if we go here this is how we
[1527] expand the
[1529] uh the request for the last question we
[1531] asked uh we have the prompt here you see
[1535] we have the question expanded we have
[1537] the schema with the format that I showed
[1539] you and so on and so forth then we have
[1541] uh the requirements the
[1544] examples the the description that is
[1547] important including you know the color
[1550] uh format and uh and yes and then we
[1554] have the output
[1556] format this will basically produce this
[1559] type of response it is still adjacent
[1561] with the relationship those are the
[1563] relationship you want to Traverse the
[1565] reasoning that is one what's what we
[1567] have said and finally the query the
[1570] cipher query okay so the cipher query
[1573] get extracted then we have a component
[1576] that basically fits if there are minor
[1579] problems with the syntax we fix it them
[1582] here and then we execute the query so
[1584] this component can be used either in
[1586] read write mode or in read only mode so
[1588] don't have to be you know to uh to check
[1593] if there is some right and if you don't
[1594] want to WR for example so that's pretty
[1597] important so what we do uh depending of
[1599] the type of the output we basically
[1601] convert the output to the format that
[1604] the human canas understand we store uh
[1608] the response and then um yes we notify
[1613] the the applic the the plugin that I
[1615] show you the blue one that basically the
[1617] response is ready so can patch the
[1620] response and specifically if we have a
[1622] graph uh result which you see the graph
[1625] or map uh what we do as an extra step is
[1628] to compute the summary and then again we
[1631] notify the view and say okay there is a
[1633] summary already I think we have some
[1635] minutes I can show you also the summary
[1637] down here it's very simple actually um
[1641] template for the summarization is like
[1643] that so say okay the user ask this
[1646] question we decide to use query to
[1649] answer and those are the results that we
[1652] got please summarize it that's it
[1655] basically uh what we do as an extra step
[1658] is to say does this you know the the the
[1662] request contains all also some kind of
[1666] postprocessing if if it's true uh then
[1669] please do it then we repeat the question
[1672] again because you may fetch a lot of
[1675] records and this section could be pretty
[1677] long so we repeat the question question
[1679] and then again we do the same type of
[1681] response so the first thing is results
[1684] analysis true false that's used for
[1686] basically for us to understand if uh
[1688] this section has triggered or not then
[1691] the usual reasoning and then will not
[1693] Sur face and then the
[1696] summary
[1699] okay so I think that's it uh the key
[1703] point I want to recall is that you know
[1705] we basically show that sometime rug is
[1707] not enough
[1709] and using this expert approach has some
[1711] benefits um even if we are still in a
[1714] sort of uh research stage we already uh
[1718] understood that mimic the expert
[1720] behavior is important because it's easy
[1722] to maintain and to extend if you have an
[1725] issue or if you want to implement
[1727] something new you have just ask yourself
[1730] what would an expert do and then try to
[1733] add yet another agent that is fine tuned
[1736] to fix that specific problem as we saw
[1739] before again it makes to reuse existing
[1742] features because they are going to f
[1744] basically the same problems and this
[1746] easy for uh the the transition towards
[1750] when you doing some gen transition I
[1753] think that's it I don't know if there's
[1755] some time for for question I will take
[1762] them okay it says fix the cipher okay
[1766] fix the cipher is basically a component
[1768] that do that basically analyze the CER
[1772] query using a DSL and a library and
[1776] basically if there is some issues like
[1779] the name of the property is written
[1781] within a space for example or the um
[1784] relationships are generated on the
[1787] opposite side this this happened because
[1790] this language model doesn't care that
[1792] much on the relationship direction for
[1795] this small issues we can basically uh uh
[1798] solve them straight away with this
[1801] micros
[1802] service
[1805] okay
[1810] uh okay yum is our is our main tool is
[1814] the is the graph analytic tool that we
[1816] have built our graph it's used basically
[1820] by law enforcement agency or um or
[1825] governmental U institution this kind of
[1828] thing so we have the we have this type
[1830] of client this is the tool that we have
[1832] built for
[1834] them and I don't know if there are any
[1836] question because this a product so you
[1838] have probably to speak with uh and and
[1844] see like if it is possible to find out
[1847] like this is a tool that we uh that we
[1849] install on from on our
[1853] client Okay then if there are no more
[1856] question
[1859] I think there
[1866] isn't all right if there are more no
[1868] more question I will thank you all for
[1871] attention and uh I appreciate the time
[1874] you take it uh with me today and uh
[1877] enjoy the rest of the conference bye
