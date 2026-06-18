---
schema_version: 1
id: yt-jn5j0vlqmlk
type: youtube
title: KGC 2023 Talk — The EU Knowledge Graph by Dennis Diefenbach, The QA Company
url: https://www.youtube.com/watch?v=jn5j0vlqmlk
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:21Z'
content_hash: sha256:302b186fea24685c05fe9d745858d1e3f7f66a2fbee94bbe3360056009163afb
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1462
  caption_track: cached
  snippet_count: 581
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:21Z'
  user_correction: null
---
[0] hello I'm Dennis dieffenbach I'm from
[3] the QA company I'm very happy to present
[5] this talk about the EU Knowledge Graph
[8] and let's start
[10] so the outline of the talk is the
[12] following I'm first going to describe
[15] the infrastructure of the EU Knowledge
[17] Graph which is wikibase and spend some
[19] few words about wikibase then I'm going
[22] to describe the EU Knowledge Graph so I
[24] think it's a good chance to look really
[26] into a Knowledge Graph generally it's
[28] not so easy to do that
[31] uh in part three I'm going to describe
[33] cohesia which is a concrete use case
[35] that is building on top of the EU
[37] Knowledge Graph and some conclusion
[41] so what is the key base
[45] the Wikimedia Foundation hosts a lot of
[47] wikis the most known is Wikipedia But
[51] there is Vicky Voyage Wikimedia comments
[53] for images Wiki's pieces and the one
[56] that we are interested in is of course
[58] Wiki data because it's a knowledge graph
[62] and this is the entry of the European
[65] Union it's a q five eight
[70] uh in Wiki data and when people look at
[75] Wiki data they generally think about the
[76] data itself or Wiki data school there is
[79] a lot of data but you generally do not
[81] think about the software that runs
[82] behind and that basically allows to
[84] construct this knowledge graph
[86] and this software is wikibase it's open
[90] source software as all softwares of the
[92] media foundation and it is especially
[96] developed by a chapter of the Wikimedia
[99] Foundation which is Wikimedia
[100] Deutschland
[102] so
[104] um the idea is the following Wiki data
[107] is a great Knowledge Graph it has
[109] thousands of edits every day it has a
[111] lot of users it is really a Knowledge
[113] Graph structure that apparently works
[115] because we constructed Wiki data with it
[117] so why not to reuse the same Knowledge
[120] Graph infrastructure to construct
[122] another Knowledge Graph
[125] and this is what we did with the EU
[126] Knowledge Graph the EU Knowledge Graph
[128] is basically a Knowledge Graph
[130] constructed to collect information about
[133] the European Union and we host it for
[135] the European Commission
[137] in a few sentence uh the Euro Knowledge
[141] Graph is a data repository to store
[143] structured data about the European Union
[145] and imagine the European Union is a
[148] really big institution there are
[150] millions of citizens living in this
[152] region and if you think what you need to
[154] model about it there are many many
[157] things there are countries regions
[159] people projects beneficiaries and all of
[163] this we basically would like to
[165] potentially model into a knowledge graph
[170] this is how the knowledge graph look
[171] like it's available under
[173] knowledgecraft.eu and it looks like a
[175] typical media Wiki installation just
[177] that there is this wikibase extension
[180] which is the same software that runs
[182] behind wikidata
[186] so
[188] um we I already said that Wiki data is a
[191] very powerful Knowledge Graph and so
[194] this could be a good reason to use
[195] basically wikibase as an infrastructure
[198] but there are a couple of other
[199] arguments that I would like to bring
[202] so first of all uh wikibase is user
[206] friendly this is now the entity q1 in
[211] the EU Knowledge Graph it's the European
[212] Union I mean it's a graph about the
[215] European Union so q1 should be the
[216] European Union
[218] and if you think of it if you think
[221] about wikidata wikidata is edited by
[224] tens of thousands of users and they are
[227] not expert users they do not know
[229] anything about rdf they do not know
[230] anything about Sparkle but still they
[233] are able to construct together a huge
[235] graph and this is thanks to the fact
[238] that also the software is basically a
[241] very easy interface where people can
[243] understand the data and edit the data
[246] another argument which is very important
[249] for this conference is that it has a
[251] graph structure
[253] so this here is the European Union in
[255] the EU Knowledge Graph and for example
[258] we have this Edge that the public
[260] holiday is the Europe day not sure if
[262] you knew we could go to this graph to
[265] this Edge explore it more
[267] uh it commemorates the Schumann
[269] declaration we have information about
[271] the Schumann declaration so it has a
[273] typical graph structure foreign
[276] [Applause]
[279] service in fact is a very essential part
[283] of the wikibase ecosystem so if you
[285] install wikibase you do not get only
[287] this interface to basically edit the
[290] data to visualize the data but you get
[292] also this query interface out of the box
[294] which is used by it's crazy they are
[297] against this endpoint every day there
[299] are thousands of ten thousands of
[301] queries that are run again the official
[303] wikidata Sparkle endpoint and you get
[306] basically one for your organization
[309] so here for example we are acquiring all
[311] countries in the European Union with
[313] their population sorted by population
[315] there are also these nice charts that
[318] are coming out of the box which allow
[321] you basically to render the information
[325] another argument is that this graph is
[327] edited both by humans and by bots so
[330] basically uh either you go directly to
[333] the page you basically edit the entity
[335] or you write a bot that is running over
[338] a large part of the data and it is
[340] carrying out specific tasks and in Wiki
[344] data there are thousands of bots running
[345] over the whole data and also in the EU
[348] Knowledge Graph we have a couple of bots
[350] that are making very specific actions on
[353] top of the data
[355] it scales well uh wikibase hosts Wiki
[358] data Wiki data contains 17 billion
[360] triples if you would like to reach the
[363] scale into an organization it's not
[366] something that is so trivial and also
[368] the United graph is meanwhile a pretty
[370] large graph it contains nearly 1 billion
[372] triple so it's not something small
[377] it is multilingual that's in this
[380] context particularly important because
[382] we have 27 member states we have 24
[385] official languages potentially there are
[388] people from different languages
[389] collaborating on the same knowledge in
[391] different languages and this is what a
[393] Knowledge Graph technology allows and
[395] also the key data allows for example
[397] here we see how the European Union is
[400] contained in many different languages
[405] something that is rather rare for a
[407] Knowledge Graph infrastructure is that
[409] you have full track of changes
[411] so this year is now a particular entry
[414] in the EU Knowledge Graph and if you go
[416] to the history you see how it evolved
[418] over time
[420] so on the 11th January 2020 DG Regio
[424] created this item and then you have
[426] different users that edit it and that
[429] added different information and you see
[431] really so this this data is not static
[433] over time we add metadata we added we we
[437] edit information there bots that added
[439] parts of the information so it's really
[441] something dynamic
[444] okay so I showed you uh why we use
[450] wikibase and now let me give you uh some
[453] impression of the content of the EU
[455] Knowledge Graph
[458] um so basically we have information
[459] about European institutions this here is
[463] q171 eurostat we have quite a bit of
[467] information about uh eurostat some of
[470] them are coming also from from Wiki data
[474] we have information about European
[477] countries I mean how to describe the
[479] European Union without European
[480] countries
[481] we have information about Capital Cities
[484] about head of dates like for example
[487] here in Emanuel macron
[489] and we have also information about the
[492] Ministries that are in the inform in the
[494] European commission so DG this isn't an
[497] article about the directoral general for
[499] regional and urban policy DG region
[501] which is part of this project uh yeah
[505] and there are information about it
[508] we have information about buildings this
[510] is a canteen in Berlin I'm not sure if
[514] you look the news sometimes it is
[516] located in the Berlin building and the
[518] Berlin building is basically
[520] uh this thing that you might have seen
[523] sometimes in the news so we describe
[525] basically a particular canteen in this
[527] uh in this building
[531] it contains 1.8 million projects which
[534] are co-founded by the European Union
[536] around Europe
[538] I'm going to describe this a bit more in
[540] detail afterwards when we go to the use
[542] case it contains 640 000 beneficiaries
[546] of uh basically institution or private
[550] person that received funds by the
[552] European Union
[554] it contains nuts so we describe all
[557] statistical or geographical regions in
[560] Europe
[561] uh this is important because it's a it's
[563] a very important knowledge asset for the
[566] European Union in in the graph and in
[570] this case it's an article about the
[572] province of Asti which is a particular
[574] region in in Italy in the pyramid area
[580] it is also used for other use cases so
[583] here it is a catalog of linked Data
[586] Solutions so at some point someone
[588] wanted to put up a catalog of what a
[591] link data solution data exist also to
[593] make aware of linked data solution
[596] inside the commission and so if you have
[598] a link data solution and you would like
[600] to increase its awareness inside the
[602] European commission you can basically
[604] add your link data solution to this
[606] graph and be part of the catalog
[610] and something that was recent is there
[613] is a catalog of Sparkle endpoint so
[615] there was the wish to basically have
[617] what are all Sparkle endpoints that are
[619] there in the LOD cloud and so there is a
[622] big catalog with more than 200 Sparkle
[624] endpoints with their address and the
[627] number of triples and some metadata if
[629] available
[630] and of course there is more so you
[632] really see it's a knowledge graph which
[634] is describing a large number of
[636] heterogeneous entities and they are
[639] organized together in a graph smoothly
[641] like it would have it in the key data
[646] okay so I would like to spend a few
[649] words about how we import data into this
[652] graph
[655] we start with any piece of structured
[659] data in this case it's a it's a piece of
[661] adjacent object and it's describing a
[664] building an office a w25 croissant it
[667] was the article that we were seeing
[668] before the occupant is a climber we
[672] don't know exactly what clima is
[674] there is some address and some more
[677] information
[679] so basically what we do is that first we
[682] want to establish a data model for it so
[685] we need entities in this case like
[687] building offices we need properties like
[690] address opening hours occupant and what
[693] we do is that we do not reinvent all
[695] these Concepts from scratch but whenever
[698] they exist we take them from Wiki data
[700] and we import them locally into the
[702] graph
[703] so for example this concept of office
[708] q244596 is not something that we created
[711] but we cloned it on wikidata locally and
[714] what we get is how office is called in
[716] many languages that it is a subclass of
[719] room of workplace or facility
[722] we get how it is pronounced we get an
[724] image for it so it is really cool
[727] because basically our local Knowledge
[729] Graph is reusing public knowledge and we
[732] do not have to reinvent uh Concepts
[735] the same we do for properties in this
[738] case we reuse the property occupant in
[741] this case it's p64 for one in Wiki data
[744] it's p466 and we get for example
[747] property constraint what what should be
[749] the domain of this property what should
[751] be the range of this property and again
[753] we didn't model this data we got it for
[755] free the community is providing it for
[757] us
[760] so what we always do is that we keep
[762] identifiers between the original data
[764] source and the data source and the
[766] knowledge graph so that there is a
[768] connection and so that if the data
[769] changes over time we can basically keep
[772] track of it
[774] and at the end the the import itself is
[777] done either via client libraries there
[780] are client libraries for every
[781] programming language we use a lot python
[783] we also use open refine and there are
[786] different alternatives to communities
[788] very big and they thought about many
[790] different types of many different ways
[793] of ingesting entities
[795] foreign
[795] we have this we instead of this Json
[798] object we have this entity with the
[800] clear identifier where people can go
[803] explore it understand this data it's an
[805] instance of building of office here we
[807] reuse this Wiki data entities it's owned
[810] by the European commission there is an
[812] image it has some opening days and the
[815] occupant is not this climber which
[817] didn't mean anything but it's a
[819] directoral general for climate action
[821] which is one of the duties that we had
[823] already in the graph so everything is
[825] integrated and well aligned
[829] okay so I showed you the knowledge graph
[833] I showed you the infrastructure what
[835] more or less it contains but I mean we
[837] want a Knowledge Graph to do something
[839] with it and I'm going to present one of
[843] the main use cases which is cohesion
[846] and for that we need to do some European
[849] politics
[851] so the European Union is spending a lot
[854] of money to basically
[857] uh increase the growth in underdeveloped
[861] areas of the European Union the European
[864] Union is is Big there are areas which
[867] are more
[868] advanced economically and some less
[871] and basically 30 of the budget of the
[875] European Union which in the programming
[877] period
[878] 2014-2020 was 350 billion euros is spent
[882] basically to increase growth and under
[885] represented or underdeveloped areas of
[887] the EU
[889] and it works more or less like this so
[892] there are people sitting together in
[894] Brussels and say we would like to
[896] increase uh climate change we would like
[899] to do something about climate change we
[901] would like to push for Innovation and we
[904] would like to uh uh combat unemployment
[908] then saying for this area we allocate
[911] this part of budget for this part area
[913] another part of the budget then they are
[915] going to the member states and they are
[917] saying you have to implement projects in
[919] this specific area with this budget the
[922] countries are then implementing projects
[924] locally and are basically making calls
[927] and people can apply and say I will make
[930] a great project for climate I will make
[932] a great project where I create
[933] unemployment and then there is a
[936] selection process this projects are
[937] carried out and then at the end member
[940] states have basically to report we did
[942] all this project in this area with
[944] dispatched
[945] Etc
[946] and the goal of cohesia is basically to
[948] aggregate all this information across
[950] across the 27 member states and to
[953] basically make this data uniform
[956] accessible accessible to Citizens but
[958] also accessible to policy makers
[961] so at the end the data that uh that we
[965] need for making all of this is all the
[967] data that is published by the different
[969] member states in fact it is published by
[972] different territories in the different
[973] member states then we need a lot of
[976] files that describe this cohesion policy
[979] what is a category of intervention what
[981] is the Thematic objective what is the
[982] policy objective how these vocabularies
[985] are related to each other
[988] we need data about geographical entities
[990] because we want to describe basically
[993] where these projects take place and we
[995] also integrate data about Wiki data to
[997] say oh this is a beneficiary this
[999] beneficiary exists in Wiki data and we
[1001] can basically extract
[1003] metadata about it to enrich our graph
[1008] this is a typical project it's a project
[1011] in France we have its name in the 24
[1015] official languages it is contained in a
[1018] specific region it's an instance of a
[1020] cohesion project financed by the EU in
[1023] France for half a million euro the total
[1025] budget was 1.3 million euros it started
[1028] it ended at a certain time there is an
[1030] intervention field a programmer fund and
[1032] some other metadata about it foreign
[1036] we do not only import this data but we
[1039] also enrich it we translate everything
[1042] we compute jio coordinates if only the
[1044] addresses are given or only the postal
[1047] code are given we deduce the region in
[1049] which this project is and we link all of
[1051] this in Wiki data to enrich our
[1053] knowledge
[1054] and for example in this case originally
[1058] in the data we had justice as a
[1061] information about the beneficiary but we
[1064] linked it and now we we know that this
[1067] beneficiary is located in this street it
[1069] has this number of employee it was
[1072] created at a certain date and time and
[1075] and more
[1078] on top of this there is a there is a
[1081] website constructed which is called
[1083] cohesion it's available under cohesion
[1085] europa.u
[1087] and it looks like this
[1090] um basically this is meant as a tool for
[1093] European citizens to discover how the
[1096] money is spent the money of the European
[1098] Union is spent in Europe we can go for
[1101] example to Poland to a certain
[1103] sub-region we have where this P where
[1106] this project are carried out when we
[1109] click on on a project we see the project
[1112] itself all this metadata and this is
[1115] connected with uh with the graph so this
[1118] is the original entity in the graph
[1122] [Music]
[1122] um
[1125] and uh this year is the corresponding
[1127] visualization that we put on top and in
[1130] fact every interaction that you make on
[1133] this website is a sparkle query so this
[1136] is a geosparkle query
[1138] this is a geo Sparkle query this is a
[1141] geospark aquarium this is a select query
[1143] that is running over the graph in this
[1145] case we do not have a translation
[1146] available
[1147] and also you can search over the project
[1151] by country by region by all the
[1153] different facets and you have also
[1156] beneficiaries aggregated over all the 24
[1160] member states so now we know that the
[1162] top beneficiary in the European Union is
[1165] the general directorate for national
[1167] roads and highways which is some
[1169] institution in Poland and which received
[1172] uh 8 billion euros from E from the EU
[1177] that was spent across 71 projects
[1180] also maybe here just to make clear this
[1183] linked of Wiki data so before in the
[1186] original data we just knew that the
[1187] beneficiary is this but in fact the
[1189] description is coming from Wikipedia the
[1191] images coming from Wiki data so
[1194] basically by enriching the data the
[1196] private data that we have with public
[1198] data we can create a better service and
[1201] understand better the data
[1204] uh this is the Tweet about the lounge of
[1206] cohesion it was launched uh more or less
[1209] one year ago uh we were all sitting in
[1212] the berlemont building there was the
[1214] ministry for DG region that was
[1216] presenting it and we were hoping that
[1218] the website would not collapse and since
[1221] then we are in production and uh it's a
[1224] pretty successful project inside of the
[1226] commission
[1228] to conclude uh I have shown you how
[1232] wikibase is used as an underlying
[1234] infrastructure for the EU Knowledge
[1235] Graph and why it is a good
[1237] infrastructure in general for knowledge
[1240] graphs I've shown the content of the you
[1242] Knowledge Graph how we ingest the data
[1245] how we maintain it fresh which are the
[1247] services that are offered around and I
[1249] have shown a concrete use case that we
[1251] have basically constructed on top of the
[1253] knowledge graph and which is in
[1254] production today
[1257] I would like to thank the Doris team at
[1260] Digi connect Knowledge Management team
[1261] at DG Regio and Wikimedia Deutschland
[1264] people from all of this institution
[1267] helped to make this project successful
[1269] and working
[1271] and that's it thank you very much for
[1274] your attention and I'm happy to answer
[1275] questions
[1277] foreign
[1279] [Applause]
[1282] [Music]
[1285] you gave an example of the term office
[1287] which comes from wikidata um I'm just
[1290] curious why you chose to copy that into
[1292] your graph instead of you know linking
[1294] to Wiki data
[1296] in fact there are two scenarios which
[1300] are possible uh yeah of copying and
[1302] linking we do not do linking because
[1303] it's more difficult from more from a
[1305] software point of view so copying is
[1307] easier but in fact there are both
[1309] scenarios are realistic for example for
[1311] beneficiaries we really want to copy the
[1314] data because we want to say that this
[1316] thing is a beneficiary and this is not
[1319] the thing that we want to put in Wiki
[1321] data because in Wiki data would people
[1323] would think why is this a beneficiary
[1324] what does it mean so basically in some
[1327] situation you would like to couple
[1329] external knowledge with internal
[1331] knowledge and then you really need to
[1332] make a copy and in semantic web we do
[1334] something very similar so either we
[1336] import a vocabulary or we say we extend
[1339] it by using rdf sub property or off and
[1342] then we basically add additional data
[1348] hi I my question is when you are doing
[1352] data ingestion uh where do you check for
[1355] or where to verify the data or check for
[1358] consistency is it a pre-injection
[1361] process or post ingestion process in
[1364] terms of the knowledge graph and then my
[1366] second question is that when you are
[1367] doing all that ingestion I don't know if
[1370] it is free or Pro but when there is a
[1373] user who is doing the dynamic change at
[1376] that time how do we verify and make the
[1378] check that the data is consistent
[1380] okay
[1381] so uh maybe for the first question
[1386] um so generally we try to make the data
[1390] consistent at the beginning so for
[1392] example when we import beneficiaries we
[1394] try to link it to existing beneficiaries
[1396] but we have but it might not always work
[1399] so we have also post processes that
[1402] basically take all the beneficiaries
[1403] that we already have in the graph try to
[1405] find similarities and these entities are
[1407] done then merged afterwards so both
[1410] thing happen just because you never can
[1413] do it perfect if you have a lot of data
[1416] uh the second one is uh in fact the
[1420] people that are touching the certain
[1422] part of the graph generally know what
[1424] they are doing so we do not get many
[1426] problems about data consistency and uh
[1429] you saw that we constructed this website
[1431] on top in fact the application layer
[1434] generally tells us if there is something
[1437] wrong because if you see something wrong
[1439] in the application you know that there
[1440] is something wrong in in the data so in
[1443] this case the application is a very good
[1445] test if you model the data correctly but
[1448] in general yeah we do not have such big
[1450] problems about data quality in this
[1452] direction
[1459] okay then thank you very much enjoy the
[1462] conference and see you around
