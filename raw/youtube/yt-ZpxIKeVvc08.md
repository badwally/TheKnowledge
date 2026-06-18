---
schema_version: 1
id: yt-ZpxIKeVvc08
type: youtube
title: 'KGC 2022: ''Yes, You Can Use Knowledge Graphs in Real Life!'' — Amazon Web
  Services & Lexis Nexis'
url: https://www.youtube.com/watch?v=ZpxIKeVvc08
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:30Z'
content_hash: sha256:8512eed1d8aee3f44e4cc69c2233f20a2e45ee58efd861a8858842f7787bdcb1
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1765
  caption_track: cached
  snippet_count: 771
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:30Z'
  user_correction: null
---
[7] and it's connecting in
[18] all right we're good to go the floor is
[21] yours aura
[24] okay
[25] great this mic works right
[29] all righty um so i'm ora and um
[32] my my co-presenter is mark from
[35] lexisnexis
[37] and um
[38] we're going to talk a little bit about
[40] uh mostly about a great uh system that
[44] mark and his colleagues have built
[47] um using uh the uh
[49] amazon neptune graph database and i'm a
[52] member of the of the of the neptune team
[56] um and basically this presentation is
[58] gonna go i'll say a few words
[60] uh kind of general things about
[63] knowledge graphs and how i see things
[65] and particularly with respect to
[66] building applications
[68] and then mark's gonna uh basically walk
[70] through the uh the the process that they
[73] had built building this application of
[75] theirs
[76] um
[77] i would say that the bars pretty high at
[79] the moment these two talks uh before us
[82] were pretty inspirational so um let's
[86] just see see how this goes but uh here's
[88] kind of like a game plan
[94] all right so let me let me let me give
[96] you a couple of sort of
[97] general observations i've been doing
[100] this for a long time
[101] um i spent a big part of my career in uh
[104] sort of research environments
[107] and uh um and lately more in
[110] in sort of a customer facing uh uh and
[113] uh customer facing role let's say
[118] and and and basically pitching this idea
[120] of of knowledge graphs so
[122] uh what we're trying to do
[124] uh and what i'm sure all of you are
[127] trying to do is to go from
[129] the separate
[131] data silos
[132] to some kind of an interconnected web of
[135] data
[137] and oftentimes
[140] i get asked about uh knowledge graphs
[142] and uh and sort of like you know um
[146] people will say that knowledge crafts
[148] are a use case for graph databases and
[150] i'd say no that's not true
[152] knowledge graphs are not a single use
[154] case
[158] deciding to build a knowledge craft
[160] system is sort of a
[163] kind of an important decision in your
[165] organization because you're now taking
[167] steps towards
[169] large-scale data integration
[172] you will have to do some cleanup
[174] of your of your organization's data
[177] but where it leads
[179] is basically what i would call
[181] democratization of data make data
[184] accessible
[185] to more people in your organization all
[188] organizations have all kinds of data
[191] but mostly it's like we heard in the
[193] previous presentation
[195] it's kind of behind gatekeepers it's in
[197] silos you can't get to it
[202] and
[203] what's really important
[205] is that to make data accessible it's not
[207] just the physical bits
[209] it's also you have to be able to give
[212] people kind of the meaning of the data
[216] uh and i think that this is
[218] something that's missing a lot and and
[222] um
[223] when i hear about things like the the
[225] modern data stack and things like this
[227] it's sort of like well yes but people
[229] have to understand what the data means
[231] what those bits mean they can't do
[233] anything with those bits if they if they
[236] if they don't understand it so
[238] so the democratization of data is really
[241] about
[242] being able to communicate the meaning of
[245] the data to people
[251] and so so having said that and then this
[254] is also something we we've now heard
[256] that uh
[257] when you're building the knowledge graph
[259] system if you will
[262] um
[263] it's not a single use case
[266] so basically the applications that
[268] follow sort of the realizations of those
[271] use cases
[272] there's something that's kind of built
[274] on top of the
[275] the knowledge craft system
[278] and
[279] saying this and having heard these talks
[281] here uh uh so far i feel like i'm just
[284] like saying trivialities but
[288] when i talk to a lot of people sort of
[290] outside this community
[292] uh it turns out they're not the trivial
[295] things and and and these are important
[297] things to communicate
[299] um
[301] and uh
[303] you know you start with a single use
[304] case but you should be prepared for
[306] other use cases
[308] uh that are coming and and and and
[311] these technologies
[314] there is sort of an element of
[315] serendipity to them you you keep
[318] building more and more
[320] applications use cases whatever you
[322] whatever you call them and you realize
[324] that hey i can you know i can start
[326] connecting these in in clever ways and i
[328] can do things that i didn't anticipate
[331] i was going to be able to do
[334] now of course now there are new
[336] technologies and new skills at in in
[339] play
[340] so people don't know what an ontology is
[342] people don't know what reasoning is
[345] you have to understand about the machine
[346] learning potentially and all kinds of
[349] things like that
[351] and so here's sort of a very very
[353] trivialized uh diagram of what most
[357] knowledge graph systems look like
[361] you basically go from okay so you have
[363] to ingest data and and so you go and you
[365] do etl from legacy sources they may be
[367] virtual graphs so you may be
[368] materializing them
[370] uh you may have external data external
[373] to your organization
[375] uh now then you store the data let's say
[378] you store it in a graph database
[380] uh you provide some kind of enrichment
[383] this happens typically via let's say
[385] some type of reasoning
[387] and and i'd like to take a sort of a
[388] very generalized view of reasoning in
[390] the sense that
[392] you know oftentimes certainly the
[393] community that i originally come from
[395] when people say reasoning they or
[397] immediately this means logic and things
[399] like that
[400] but of course also uh their statistical
[402] reasoning
[404] any which way you can kind of enrich the
[406] data
[408] that makes it ready for consumption
[411] and then uh
[412] consumption of course means
[414] uh
[415] user in interfaces and user experience
[418] and i think this is one of those things
[420] where we uh if i think about the graph
[422] community where we're really kind of
[423] lagging behind
[425] all of a sudden we have this
[427] remarkably expressive data
[430] and
[431] we don't have expressive user interfaces
[435] and then of course it also means apis
[438] and
[440] when mark explains uh their application
[442] uh you will see that apis play an
[444] important role
[448] and so finally um
[451] it's important to understand that this
[453] is really not a technological problem
[456] so the bigger problems in your
[457] organization are the people and the
[460] process uh that you're going to use to
[464] get to something that um that that we
[466] call knowledge as a product
[470] and
[471] i think this is sort of uh
[473] something where we have to kind of stop
[474] and say okay what what are we now
[476] talking about so
[479] we know quite well how to build software
[482] products
[483] from the sense that we understand the
[485] roles
[486] and the processes uh
[489] all the different things gathering
[491] requirements thinking about user
[493] experience release blah blah blah you
[495] know um
[498] we need that for for data we need that
[501] for knowledge
[502] uh and so so you know for one thing you
[505] need a product manager for your data
[508] products or your knowledge products
[511] uh
[512] and uh shameless shameless plug here uh
[514] once equator and i have uh recently
[516] written a book
[518] where we kind of talk about this stuff
[519] so um i urge you to uh to take a look at
[522] that
[525] all right and now i'm gonna hand off to
[527] uh to mark
[534] uh we can't hear you
[548] can you hear me at this point
[551] yep
[553] yeah okay
[555] all right thanks aura so i'll go through
[557] some depth into a knowledge graph system
[560] that we've developed at lexisnexis
[562] that has
[566] kind of
[567] borne some fruit in terms of
[568] democratizing data in terms of
[571] multiplying the value of our
[573] data science inferences and rolling
[576] those out across multiple
[577] end user products
[579] so
[580] lexisnexis is a legal research and
[583] publishing company and our mission is to
[586] spread the rule of law around the world
[588] by making it easier for researchers to
[590] get to the data that they need to craft
[593] better legal arguments
[595] and one of the major challenges to that
[598] is that the data that our users need
[601] legal researchers
[602] tends to be disconnected
[604] so
[605] there are documents from law firms those
[607] are legal briefs arguments
[610] documents from the courts that decide on
[611] the outcomes of those
[613] arguments
[614] and then lots and lots of documents from
[616] third party vendors which can be
[618] analysts
[619] news reports all of that
[622] so
[623] our users want to see these connected
[627] in a legal matter
[629] we will see
[631] documents in each of these categories so
[633] if i if i sue my co-presenter aura that
[636] will generate a legal matter
[638] beastling versus lesla that will
[641] produce documents in each of these
[642] categories so users want to see them
[644] together and on top of that we of course
[647] want to do interesting machine learning
[649] that makes use of the entire legal
[651] matter
[652] so at lexisnexis we wanted to connect
[655] and search our data automatically for
[657] our users and present a nice integrated
[659] experience
[660] so next slide
[662] the first product
[664] that we built is called brief analysis
[667] and the idea here is for a user who is
[670] drafting the legal argument to upload a
[673] draft of their brief to our system
[676] we will parse that for
[678] legal concepts and citations to other
[681] opinions that that draft makes
[684] and then recommend similar briefs
[686] so if you are in a trademark
[688] infringement case you may want to see
[690] other briefs that are also about
[691] trademarking arguments
[693] and get an idea of arguments you might
[695] have missed or citations to make
[698] so that recommendation engine is based
[701] on this very simple graph
[704] right so grief is connected to zero more
[706] legal concepts that we've extracted as
[709] well as zero more court opinions that it
[711] cites
[712] a similar brief
[714] is just a brief from our large corpus
[716] that shares some of the same connections
[719] so the next slide
[723] this is what the architecture looks like
[726] so um kind of thinking about
[728] auras
[730] general
[731] framework here we have ingestion which
[733] also in our case includes some machine
[735] learning transformations and extractions
[737] so we extract
[738] legal concepts and citations from
[741] our own corpus of briefs
[743] we
[744] then represent
[746] all of that knowledge in our knowledge
[748] graph so the knowledge graph really is a
[750] destination for a lot of this machine
[752] learning inference
[754] and it's a place to organize and
[756] and make that data available
[759] then
[760] that
[761] powers a
[762] front end which leads to brief analysis
[766] so that was kind of one one product
[768] uh and then kind of going to oro's point
[771] about not really knowing what all
[773] opportunities will arise from this
[775] we happen to have another
[777] product opportunity
[779] so on the next slide
[781] there is a product
[783] called context
[787] where
[788] we are
[790] extracting outcomes from judicial
[793] opinions so uh was a motion granted or
[795] denied what rates do judge different
[798] judges grant different motion types
[800] at
[801] and so this uses a different content set
[803] that uses those court documents not the
[805] law from documents
[807] but we thought it would be great to be
[809] able to connect those attorney arguments
[811] to their outcomes so we have these two
[813] different content sets
[815] generally in silos but we wanted to
[817] connect them using our knowledge graph
[819] so the next slide
[823] that turned out to be
[825] pretty straightforward so here's our our
[828] existing graph for a brief analysis
[830] all we had to do was add a few notes
[833] and slide
[836] the legal matter is really the important
[838] note here so remember that's the uh the
[841] mueslin versus
[842] lasilla or whatever it is so those
[844] documents
[845] that belong to the same legal matter
[847] that could be some number of legal
[849] briefs as well as some number of court
[851] opinions and then that court opinion is
[853] connected to a motion outcome so next
[856] slide
[858] we can now
[859] go from a law firm brief to its outcome
[863] by using this connected graph data
[866] next slide again
[870] and now we have another product uh
[872] sitting on top of this knowledge graph
[874] system so brief analysis context
[876] multiple end user products using that
[878] same um that same graph database we
[881] actually have a third product um
[883] at this point
[884] but i won't go into those details
[887] one last
[889] thing i want to raise is
[891] apis
[892] so
[893] we
[894] have been
[895] trying to
[896] raise awareness of of this offering
[899] throughout the business
[901] and
[902] the thing that really helped was to
[904] create a generic
[906] a simple api on top of our knowledge
[909] graph that
[910] any anyone in the business can hit uh
[912] it's almost more of a demo api where you
[916] uh the request is one
[920] um one entity or one document and the
[922] response is just what all is connected
[924] to this in our knowledge graph and that
[927] has really
[928] spurred interest in the graph and
[930] spurred new use cases where
[933] anyone from the business can just hit
[935] that they don't need to know any query
[937] language
[938] it's just a very simple api and that
[941] really gets people to kind of light up
[943] and realize what all we have in here
[945] um the next slide
[949] and that has led to
[951] lots of interesting new use cases that i
[953] never would have imagined
[954] i'll go through just a couple of these
[958] so interesting machine learning use
[959] cases so i mentioned that
[962] we happen to use our graph as a
[964] destination for a lot of machine
[966] learning inferences so in that sense
[968] machine learning powers the graph
[969] but
[971] we have various downstream data science
[973] teams that have kind of seen this graph
[975] and seen the opportunity there to help
[976] to see how that graph can power machine
[978] learning in turn
[980] so
[980] for example we do a lot of named entity
[983] recognition in our natural language
[985] documents
[986] so
[987] if we have
[989] various documents that we know from the
[991] graph are in the same legal matter then
[994] we can reasonably assume that those
[996] documents tend to talk about the same
[998] people
[998] and that can improve our named entity
[1001] recognition and resolution
[1004] entity deduping
[1006] so
[1007] uh kind of similar if we have various
[1010] entities in our entity authority that
[1013] we've kind of inferred by scraping
[1015] various web sources then we can start to
[1018] dedupe
[1019] [Music]
[1020] pairs of entities if they have
[1023] similar names and they appear in all the
[1025] same documents they have the same
[1026] connections in our knowledge graph so in
[1029] that sense it helps us detect too much
[1031] similarity
[1033] train and test separations so we always
[1036] want to avoid data leakage in machine
[1038] learning
[1039] and this is
[1041] there's a potential for
[1043] leakage in the sense that
[1045] different documents actually come from
[1047] the same legal matter
[1049] and
[1050] so of course they might mention the same
[1052] people
[1053] and so if we happen to draw a train
[1056] example and a test example from the same
[1059] legal matter we might actually be
[1061] testing on our training data so we don't
[1062] want to do that
[1064] so the knowledge graph helps us avoid
[1065] that
[1067] and that was kind of a clever use case
[1068] that another data science team came up
[1070] with and said hey we like your api can
[1072] we use it for this use case
[1074] uh
[1075] and then lastly the graph itself can
[1077] become a product so there's another
[1080] product here which is essentially
[1082] exposing the graph and its connections
[1084] to our users so those legal citations
[1087] are extremely important in legal
[1089] research and this almost just comes for
[1092] free once we have this graph we can
[1095] build a simple product on top of it that
[1097] doesn't even require any of the
[1099] fancier components that i talked about
[1101] in the other products
[1104] so last
[1106] slide so um i've tried to
[1110] give this kind of quick example of a
[1112] knowledge graph system that lets us
[1114] reuse and multiply the value of our data
[1116] science inferences by rolling it out to
[1118] various different products
[1121] it is easy to make additions we've we've
[1124] had
[1125] those experiences with context and with
[1127] a few other products where
[1130] the
[1132] the scheme of a knowledge graph is in
[1134] our experience has been easy to just add
[1137] new entity types and connections and
[1139] those compound in value right so the
[1142] every subsequent thing that you add is
[1144] connected to more and more things and so
[1146] there are more and more use cases
[1147] available for that
[1149] and we've really learned this lesson
[1150] about the simple apis that will attract
[1153] new customers and new use cases
[1155] that has really
[1157] accelerated the growth and awareness and
[1159] democratization of the data that we have
[1161] in our graph
[1163] so i think i'll stop there
[1165] and
[1166] so we have plenty of time for questions
[1168] and thanks to all of our colleagues
[1170] aws and licensed nexus
[1175] great thanks mark and before we take
[1178] questions i actually have one question
[1180] for you mark
[1181] can you
[1182] say anything about the current kind of
[1184] volume or scale
[1187] of the system as it stands today
[1193] sure so
[1195] uh on my first slide i had
[1197] some numbers of millions of documents
[1200] so those are all uh nodes in our graph
[1206] and we
[1207] support now
[1209] three uh three end user products as well
[1212] as those api use cases for our internal
[1215] data science teams
[1219] okay thanks
[1222] all right thank you very much uh
[1224] questions
[1234] thank you
[1236] hi um this is great thank you so much
[1238] for for walking through this use case
[1240] i'm curious if
[1242] so you just mentioned mark that all of
[1244] the the documents are are their own
[1246] nodes are they componentized in any way
[1249] has there been an effort to
[1251] like
[1252] break down the components of that um
[1254] unstructured content or is it more a
[1257] focus on keeping those together and um
[1259] getting just more like content concepts
[1262] or tags from them
[1266] yeah so we
[1268] have we have componentized them so
[1271] um there are notes for documents um as
[1273] well as kind of higher order
[1275] abstractions so
[1277] legal matter for example
[1279] is another type of node
[1282] concepts i mentioned
[1284] and
[1285] we also have connections to
[1287] entities and other taxonomies from
[1290] around the business so we really have
[1293] kind of different different layers of
[1295] nodes in there
[1299] i'm going to take a question from the
[1300] chat i can now see them here
[1303] let's see yeah
[1308] well okay they're up voting so the what
[1310] kind of system or model is being used
[1312] for extracting legal concepts
[1318] yeah so that is
[1320] that is a kind of purely uh nlp based
[1324] system um it has some
[1326] uh tf idf like elements to it so it's
[1331] an
[1332] unsupervised
[1334] system that will extract
[1336] common phrases or clusters of phrases
[1339] that
[1342] end up representing legal concepts or
[1343] even factual concepts
[1345] and that is really kind of a precursor
[1348] to loading uh to the knowledge graph so
[1350] that's
[1351] kind of one of the earlier steps there
[1356] questions here otherwise i'll go for
[1357] another one in the
[1358] chat yes
[1362] hi this question is for mark is there
[1364] appetite and i think there was a similar
[1366] question on the chat is there appetite
[1368] in the other verticals within lexisnexis
[1371] to
[1372] leverage what you're building
[1376] outside of the legal research
[1381] right yeah so
[1383] um
[1384] so um
[1386] elsevier is our
[1388] kind of sister organization in
[1389] scientific publishing
[1391] they do make extensive use of knowledge
[1392] graphs um and i think that there is
[1395] potential for uh for some overlap and
[1397] collaboration there
[1399] uh
[1400] yeah in general i am
[1402] i'm constantly fielding requests for um
[1405] how can we
[1406] how can this this or that team um make
[1408] use of this uh so
[1411] really
[1412] my next challenge is um kind of scaling
[1415] the system up
[1416] and
[1417] being able to serve
[1420] many different feature teams and
[1421] products uh so yes there is definitely
[1424] kind of appetite and continuing to grow
[1426] the knowledge graph system
[1429] all right i saw a question on the chat
[1431] here online um where is what is the role
[1433] of the data catalogs coming in with with
[1435] managing all the the well the actual
[1438] question is
[1441] where do you put the data catalog for
[1442] playing the role of conveying meaning of
[1444] the data and the process of
[1445] democratizing data
[1447] i can i can take that so um
[1450] i think that
[1452] anybody who is
[1453] building a knowledgecraft system should
[1455] really start from a data catalog
[1459] because invariably when you when you're
[1461] building this uh you know we're not
[1463] talking about two or three
[1466] separate sources what but we're talking
[1467] about large number of sources and data
[1469] catalog can really be
[1471] sort of a way for you to manage manage
[1473] the whole thing and that of course
[1475] includes all the managing all the
[1476] ontologies
[1478] and in and in and in that regard the
[1480] data catalog plays a
[1483] pivotal role in in most
[1487] knowledge graph projects so i think that
[1492] it's a little bit like
[1494] you can't build a knowledge graph
[1496] without a data catalog
[1498] but in order to have a data catalog you
[1501] also need a knowledge graph for that so
[1504] data cataloging itself is kind of like a
[1506] knowledge graph
[1508] um
[1509] and of course you know managing the
[1511] ontologies is
[1514] important particularly when you're when
[1515] the diversity in your data grows
[1518] um
[1520] to sort of get a handle on the on the on
[1522] meaning
[1524] of things
[1527] hey era mark thank you for the talk my
[1530] name is avi i work at a company called
[1531] vouch we're also building on top of
[1533] neptune in fact aura has helped us a a
[1534] little bit along the way um one of the
[1536] things that we have noticed is when
[1539] we're working with inferences having to
[1541] persist them and having to
[1543] think of what inferences that we have
[1544] made that have been materialized have
[1546] become stale now how do we how do you
[1548] deal with that at lexus right now
[1554] yeah so uh
[1558] currently the the knowledge graph is we
[1560] have a
[1561] a batch uh process that um basically
[1564] just wipes it all out and reloads it um
[1566] periodically that's
[1568] weekly or daily so we
[1571] um we don't necessarily have kind of
[1573] different time scales for the inferences
[1575] um but one
[1577] kind of related um interesting
[1579] opportunity that we're starting to run
[1580] into
[1581] is
[1582] that we have many different data science
[1585] teams around the organization they're
[1587] all making their own inferences and
[1589] sometimes we
[1591] infer more or less try to infer more or
[1593] less the same thing in different ways
[1595] and so
[1596] we are on the cusp of starting to have
[1599] some collisions in the knowledge graph
[1600] where um like a motion outcome for
[1603] example can be inferred from um one
[1605] source or another using one algorithm or
[1607] another and i think that gives us a
[1609] really interesting opportunity to do
[1611] some ensemble machine learning
[1614] at that point which has not really been
[1616] possible because that data has not
[1617] really collided before so i think that's
[1620] actually kind of at least an interesting
[1621] opportunity to make even better
[1624] inferences so that's kind of on on the
[1625] roadmap
[1635] schemas with ontologies and i'm
[1636] wondering whether you're using the
[1638] labeled property graphs and if so what's
[1639] schema language or were they using all
[1641] with rdf triple stores
[1645] so let me let me answer that first and
[1647] then i'll have mark give a specific
[1649] answer so uh in the neptune team we've
[1651] sort of
[1653] uh felt that
[1655] sometimes uh rdf uh and the sort of
[1659] that the semantic web style of
[1661] representing things
[1662] is better for people's use cases but we
[1664] don't want to limit people to that so we
[1666] also also support labeled property
[1668] graphs and uh
[1670] and um
[1672] now of course that leads to an
[1673] interesting interesting situation where
[1675] when we get a customer and the customer
[1677] goes like well which one should i use uh
[1679] and you know honestly i don't want to
[1681] answer that question you know i i
[1683] usually say you know let's talk about
[1684] that later
[1685] let's first talk about your data as a
[1687] graph without these distinctions between
[1690] uh and i'll talk more about this in my
[1692] keynote to tomorrow but uh um
[1695] what we're doing in the in the neptune
[1697] team is that we have a project called
[1698] one graph
[1701] where we're really kind of moving
[1702] towards a situation where when a
[1704] customer asks that question
[1706] uh i can say you know who cares
[1710] you can you can you can use the best
[1712] things from both
[1714] so so where we're going with this is
[1717] something like okay you have rdf
[1719] you can run gremlin over rdf
[1721] um and and and things like that
[1725] mark can you give a specific answer
[1727] about your system
[1730] yes so we are on rdf with sparkle
[1737] very straightforward
[1740] um i think with that i'm hungry
[1743] uh they were all hungry
[1744] uh thank you orr and mark for this this
[1747] was great round of applause please
[1750] [Applause]
[1753] we have uh we have an hour break for
[1755] lunch i've seen people coming in with
[1756] lunch we're back in an hour with the
[1759] talk from intuit from enterprise
[1762] knowledge and then i will be cheering
[1765] the session the panel
