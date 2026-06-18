---
schema_version: 1
id: yt-rzD5i-6eUO0
type: youtube
title: Knowledge Graph and AgenticRAG with Llamaindex
url: https://www.youtube.com/watch?v=rzD5i-6eUO0
authors:
- AnirbanK Data Science Blog
ingested_at: '2026-06-17T20:57:27Z'
content_hash: sha256:4e36b17453d80f3f2ccff68cab8ad99c9d2fee76d14f1709f95a60ee0e87084e
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AnirbanK Data Science Blog
  channel_url: https://www.youtube.com/@anirbankdatascienceblog3552
  duration_seconds: 2404
  caption_track: fetched
  snippet_count: 838
filter:
  score: 0.7
---
[0] hello all this is anirban good evening
[3] today I'm trying to share my
[6] recent learning and experience with the
[9] neo4j graph
[11] database and I was quite fascinated with
[14] the results I got with a low code or no
[17] code approach using the Llama index
[20] library and uh I thought of sharing this
[24] I follow it up with a uh router query
[27] engine where I use multi mulle different
[31] rag pipelines and allow the llm to
[33] choose the best approach and finally I
[36] use a agentic rag which has uh Knowledge
[40] Graph as one of the
[43] components and it chooses the best
[45] approach to query a document start start
[48] with i I'm starting with the knowledge
[51] graph that I created from this book this
[54] is a very excellent book
[58] on on
[62] solar system exploration and India's
[65] contribution a beginner's guide by Dr TI
[68] praim Das from ISRO director of Space
[71] Science at ISRO which he shared ebook
[73] some time back and I was reading this so
[76] just thought of creating a knowledge
[77] graph with this and uh what I was quite
[82] amazed at is the power of llama index to
[84] create a knowledge graph with a few
[87] commands and quite accurate I found it
[91] so to start with basically I I import
[95] the libraries necessary libraries a
[97] Knowledge Graph index the neo4j graph
[99] store from llama index core and Lama
[102] index graph stores right and I load the
[105] documents using a simple directory
[108] reader that's one of the fastest way to
[110] load a PDF document in Lama index one
[113] liner it loads a document as a set
[116] of documents or nodes with metadata
[119] right and once I do that basically I
[122] clean up any any uh graph that is
[125] already there I create a graph stored
[127] connection and uh all I do is knowledge
[130] graph index. from documents and give
[132] this nodes which I extracted from the
[135] PDF file as a input and some
[139] basic
[142] uh uh some basic parameters like the
[145] storage context which gives the path to
[147] the ne forj graph store with with a
[149] username and password this is the a NE
[151] forg instance which I have a free
[152] instance which can be obtained by
[154] anybody using a Gmail ID so I'm giving
[157] the path to that and a basic setting
[160] like Max triplets per chunk equal to two
[164] so once I do that
[166] graph that I have pretty amazing and I
[169] will go to that
[171] now so what I do is uh I go to console.
[174] neo4j doio and using the free instance
[178] that I've created once one creates a
[181] free instance it will be running and it
[183] will give a connection URI like this
[185] which is what I'll be giving in my
[187] connection URI property it will also
[189] give a password which we'll have to
[192] specify there and connect to this so
[194] once we connect to this it comes up like
[197] this we have the explore interface the
[198] query interface and the import interface
[201] so since I have created the graph
[203] database with the contents of this PDF
[206] which I was showing which shows India's
[209] contribution in the exploration of the
[211] solar system what are the
[214] Expeditions India has made like Chandra
[216] Yan 1 2 and three the Mars orbit Mission
[220] whatever you all the details including
[223] the and terminologies of the space
[225] science is explained very nicely over
[227] here by B and so we can see here the the
[232] table of contents so when we go to the
[235] knowledge graph one of the first things
[237] we can do is even without knowing any
[239] weight to query the knowledge graph we
[241] can explore the knowledge graph and we
[243] can say Okay I want to see how this
[246] knowledge graph looks
[249] so once I go here I can select all the
[253] entities and all the relationships and I
[256] can say go so what it does is it shows
[260] me that it has this knowled GRA with 268
[262] nodes which is Created from the PDF
[265] document and if we close in so for
[268] example
[270] we can see here the
[273] mom m actually here is Mars orbit
[277] Mission that's abbreviation so it says
[280] that you know it it's create nicely the
[284] M Knowledge Graph with with the m and we
[288] can see the relations going out from it
[290] right uh
[293] so very nice looks very nice
[297] right so for example what is derive
[308] the so it says it reached Mass
[314] orbit all that so we can we can see the
[317] graph in detail by zooming into the
[319] portions of the
[322] graph we can see the terminology
[324] explained in this graph for
[326] example the planetary body
[344] so let's
[346] see what are the things see in this
[348] graph there are many nodes created so
[350] I'm trying to search for the space
[353] exploration using the recent mongal
[358] Jan and
[364] now we can see here Mars orbital Mission
[368] reported about bright hazes achieve
[371] notable
[372] feat carried
[380] Mars
[382] exospheric neutral composition analyzer
[385] that's an experiment launched in
[387] November 2013 captured IM Imes images
[391] are Capt captured by a Mars color camera
[394] reveal details capture detailed
[397] images so I
[399] was the role of India in all these
[402] things in solar
[404] exploration India made
[406] contributions India is
[409] up has witnessed remarkable strides in
[412] the Solar exploration but I'm still not
[415] getting the required inform about the
[420] about the Chandra Yan so here it goes
[421] Chandra Yan so if we see here how it has
[425] created the Chandra Yan Knowledge Graph
[427] node chra Yan 3 launched in 2023 stand
[431] estment successfully landed landed near
[436] Yona South Pole Landing site
[439] named station ship shaki compris three
[443] components deployed robotic Rover quite
[446] quite a nice Knowledge Graph and I was
[450] was quite fascinated how it's possible
[451] to create this knowledge graph without
[453] any cues uh to the to the library as
[457] such I'm using the automatic finder of
[460] entities right here and um
[465] to we can we can use this is the explore
[468] interface we can also use Cipher queries
[470] so this is a query interface so if I go
[473] here and uh I can create a cipher
[476] query so if I create a query so the
[480] basic query trans is match in entity
[482] return in limit 25 so it is giving me
[485] that 25 entities uh and I can see the
[489] first 25 entities that has got from that
[491] set of uh whatever 268 notes it has got
[496] so now I click on it I can see the
[499] Chandra Jan one what are the things you
[501] know related to Chandra Jan one and all
[503] that I can also give a cipher query so
[507] with a W
[508] Clause Cipher query
[511] where where so it it basically prompts
[515] me with what I need to give where N is a
[519] note n. ID I can give the starts with so
[523] when I when I say SDA it give prompts
[525] withth starts with and let's say I want
[528] to know about um about the Chandra so I
[532] can say
[534] Chandra so I want to know all the notes
[537] related to Chandra Yan so let's see and
[540] we can see it has given me all the notes
[542] related to Chandra Yan and I can I can
[544] click this Chandra Yan one I can see
[547] India lach chandran one I can click this
[550] I can see all the relationships for this
[554] node gilded scientific insights chandran
[561] one measured intensity of energy
[565] particles all these things evidence of
[567] young volcanic activity challenged
[570] existing models is a lunar
[572] exploration fantastic graph
[574] visualization I like this really in the
[577] Neo
[578] 4J I can say starts with Mars let's say
[582] let's see what comes up and I can see
[585] Mars color camera Mars orbit Mission
[589] Mars orbit so if I click any one of
[591] these I can
[593] see the relations so Marsh Oram Mission
[597] so what are all the things related to
[599] Mar or Mission a pretty good
[602] visualization let's see some more
[604] example let's
[615] say when I say Ad it's case sensitive
[618] that I can see that adel1 this is
[621] India's solar exploration
[624] space uh launch uh where the
[630] the space vehicle is is stationed at L1
[634] lagran point and it sees it gives all
[638] these things six to
[640] unreel mechanisms responsible for
[643] intense seat suits of seven
[645] sophisticated instruments
[648] Adan reached desire orbit India has sent
[651] Adan Adan Mission India's space based
[657] Observatory and it orbits the Sun so all
[659] this information I can easily get by
[663] query right now this is a pretty good
[667] example and uh of how to create this
[669] knowledge graph very quickly and uh once
[673] I do that I can now use this knowledge
[676] graph in my rag pipeline by creating a
[678] query engine from this uh Knowledge
[681] Graph so once I created the knowledge
[683] graph I can create a query engine and
[686] for example query engine index do as
[689] query engine and I use the response mode
[692] like this and I give a query let's say
[695] what is India's achievement in the
[696] latest space mission give details of the
[699] project uh in a few paragraphs so that's
[702] one of the queries I'm using just to
[704] test
[705] it takes a little bit of time uh to
[709] Traverse the knowledge graph and come
[710] back with the with the answer so there
[713] is some scope of uh improvement over
[716] here how to how to reduce the
[722] response time uh till the time it comes
[725] back I would like to also say that the
[728] various ways of creating the knowledge
[730] graph which uh which is
[734] gear for
[747] example this excellent
[752] tutorial on the property graph which is
[755] the latest Knowledge Graph
[758] from from Lama index the property of
[761] index and one can experiment with
[770] that property government so we can see
[772] this is from May 29 2024 so property
[775] graph basically uh is an improvement
[778] over the knowledge so the knowledge
[780] graph have certain limitations that's
[782] what Lama index is selling and they have
[783] come up with a improved uh Knowledge
[787] Graph called the property graph and in
[788] this property graph we can even specify
[791] our our knowledge graph entities and the
[795] relationships and based on a predefined
[798] schema we can extract the knowledge
[800] graph from the document that we have so
[802] using the schema llm path extractor you
[804] can also use implicit extraction which
[806] is what I was doing so all these
[808] facilities are available
[810] even I I remember reading an article
[812] excellent
[813] blog where it is shown how to D
[816] duplicate the duplicate entities created
[819] and these are some of the things we see
[821] in real life customizing this maybe this
[824] one yes this is the one so here we see
[827] how we can use the property graph index
[829] it is published very recently as recent
[831] as June 24 by two experts uh who are
[835] from llama index and neop so we can see
[838] how they're creat the graph using the
[840] latest you know llama
[845] index why is this coming
[853] up using the latest uh llama index um
[857] facility called property graph index and
[860] how they're creating the graph using
[863] entities and relationships predefined uh
[867] so they're using the schema llm paath
[869] extractor and how the graph is been
[870] created and this is very important
[873] entity D duplication so they've given
[875] the code how to D duplicate the entities
[878] using Vector similarity and all that
[881] it's quite a complex code and then how
[884] to create a custom Retriever with uh
[887] with llm various types of retrievers are
[889] available like llm synonym retriever
[891] Vector context retriever text to CER
[894] retri very good um question answering
[897] flow so I'll give this link
[900] in my blog so these are various ways it
[903] can be
[904] created coming back to my this thing it
[907] says that uh service unavailable so
[911] sometimes it gives this error I'm not
[913] particularly sure why it gives this
[916] error uh let me see if the connection
[919] should be I don't know there is a
[922] relation with this connection here
[925] and should not be the case because I am
[928] connecting here
[933] to the graph
[935] database that's fine uh but this should
[938] not be related to that let me try it one
[943] again based on the knowledge we created
[945] I'm just yes now it has worked it says
[949] India's achievement in the latest space
[951] mission is a successful launch and
[952] operation of the Mars Orbiter Mission
[954] also known as the mongan launched in
[956] November 2013 this Mission significant
[959] mil for India's space efforts of Mars
[962] Oram Mission aimed to study the Martian
[964] atmosphere and all that quite a good
[969] U quite a good response but I'm not sure
[973] sure why it is picking up the Mars
[975] Orbiter Mission as the latest Mission
[978] though the latest is the Chandra Yan 3
[979] in 2023 right so anyway so let us see
[983] what this answer is and we can also see
[987] from where this answer is coming by
[989] printing the noes from The response.
[992] Source notes here I'm asking another
[995] query which is basically what is India's
[998] achievement in chandran 3 as compared to
[1001] the previous Moon missions compared in
[1003] detail with observations so it says
[1006] India's achievement with chandran 3 in
[1009] comparison to previous Moon missions
[1010] involves significant advances in lunar
[1013] exp and it showcases leading force in
[1017] space exploration Etc
[1024] so good but I can say that this can
[1028] still be improved right uh so there are
[1031] various ways of quing this using there
[1034] is something called the neo4j query tool
[1036] spe we can try that as well and we can
[1039] create agent out of it and then we can
[1045] say using Neo Forge quiry to spake we
[1048] can and using the llm as open AI why the
[1052] llm is needed is creating the cipher
[1054] query and we can see that uh this has
[1058] the answer that Chandra Jan 2 is the
[1060] latest space mission which is still not
[1062] quite very good so
[1065] still ways to improve this
[1070] right so this is this is a duplication
[1074] of the same thing Knowledge Graph index
[1076] okay now we can also use a embedding
[1079] mode equal to hybrid in this case I was
[1081] not using any any embedding embedding of
[1084] the vector embedding is not used here so
[1086] when I create the knowledge graph index
[1088] I can even give a embedding mode and
[1090] specify it hybrid and create the
[1092] knowledge graph which I'm not doing now
[1094] it will take time I'll share this
[1096] notebook and we can again query in the
[1098] same way so the these are the various
[1100] ways we can use neo4j the knowledge
[1103] graph index the most recent property
[1105] graph index and customizing the schemas
[1108] using the customized schema extractor
[1112] using llms or allowing the implicit
[1114] schema extractor which is what I was
[1116] showing works pretty good I was quite
[1119] quite amazed at the basically at the at
[1123] the knowledge of that we have uh
[1126] obtained by just a few lines of code uh
[1129] from this uh Chandra Yan 3 with all its
[1133] relationships Chandra 2 ad and
[1136] everything all the all the essential
[1138] components of kind kind of come out of
[1140] course it can be improved now so that is
[1143] what I was trying to
[1144] show and uh if one is uh also trying
[1150] to creating a Knowledge Graph to start
[1153] with and on in his local machine without
[1156] having access to a cloud-based uh neo4j
[1159] which is what I'm using one can either
[1162] install the neo4j locally which is what
[1164] we did in one project we had a
[1165] requirement that we can't go to the
[1167] cloud so we can install NE for Lo or we
[1170] can use a simple graph store which is
[1172] also coming from uh from llama index so
[1176] we can use a same document and create a
[1179] simple graph using the same way so we
[1182] give the documents which we get from the
[1184] simple directory editor and create a
[1186] graph store and we say index equal to
[1188] Knowledge Graph index from documents and
[1191] we documents and the storage context
[1192] here point to the simple graph store
[1194] which is in a local mode it can be
[1196] backed up as a Json file so right now
[1198] it's creating that graph store and it
[1200] can be visualized as well in in in the
[1203] notebook using the visualization
[1204] libraries
[1206] available so I'm trying to create this
[1210] this uh within 30 minutes limit which is
[1212] what I have for my free screen capture
[1215] tool we can see here screen castify
[1218] right so as as it goes on now to extend
[1224] this concept now what are some of the
[1226] advantages of this what I can see is uh
[1230] the advantages is the knowledge graph is
[1232] a very powerful construct to represent
[1235] domain knowledge we use this in multiple
[1237] projects so one of the projects we are
[1238] trying to get the requirements in the
[1240] form of knowledge graphs there we use
[1242] something called an NLP Library fa to
[1245] extract entities and relationships and
[1247] insert it into the ne 4G database that's
[1250] also possible but we never use Lama
[1252] index which is which is a beautiful tool
[1255] which which creates this knowledge graph
[1257] within within minutes
[1260] right so that is what the beauty of this
[1263] uh llama index it creates a without any
[1265] code at all any code to specify the
[1268] entities and the relationships it just
[1271] creates this and we can see the
[1274] beautiful knowledge graphs it's and you
[1277] know I liked it so much I thought of
[1278] sharing it it's not about some technical
[1281] knowledge here it's not about something
[1283] technical it's about the share beauty of
[1285] it and what we have seen is knowledge
[1288] graphs can be a tremendous Aid in in
[1291] many cases for example
[1292] creating the user stories from domain
[1295] knowledge the domain knowledge can be
[1297] represented as knowledge graphs and we
[1300] can use we can take the help of llms
[1302] itself to create this knowledge graphs
[1304] so this knowledge graph is created by
[1306] Lama index with the help of open AI if I
[1309] take out the open a API key this
[1312] knowledge graph will not be create it it
[1313] will creep because it's a implicit
[1315] extractor which is using openi on this
[1317] PDF to create the knowledge
[1320] so all that is just combined in a few
[1323] lines of code and the low code approach
[1325] which is what I like good visualization
[1328] the many ways to create the graph there
[1330] is a small launa I found that this
[1332] knowledge graph response time is a
[1334] little high and once I store the
[1337] knowledge graph in Neo 4G I'm not sure
[1339] how to connect to that Knowledge Graph a
[1340] pre-built Knowledge Graph I was
[1342] searching in the stack Overflow I
[1344] couldn't get it if anybody can get they
[1346] can just comment in my video so here we
[1348] see we create the knowledge graph index
[1350] from documents so every time it's going
[1352] to create the knowledge on the Fly which
[1354] cannot be the case in a in a realtime
[1356] system right on a web interface people
[1358] will be waiting for
[1360] that so we can of course Knowledge Graph
[1362] in Neo 4G and do Cipher quiring on that
[1364] you create Cipher queries and use the
[1366] agentic uh way of uh connecting to the
[1369] knowledge graph which is what I showed
[1371] here uh in the last part uh that is of
[1376] course possible but the knowledge graph
[1378] index so here here I'm using the agentic
[1380] way of uh connecting to the knowledge
[1382] graph using neo4j query tool spec so
[1385] that is possible and we can get answer
[1388] but the knowledge graph index uh is uh
[1392] always I'm seeing that it's from
[1393] documents there is nothing called
[1394] Knowledge Graph index from graph store
[1398] uh lot of I I saw some people have asked
[1401] this question on the stack Overflow but
[1403] maybe it's there I'm not very sure of it
[1405] so coming back to this now
[1409] yeah so it has gone through so now we
[1411] can visual simple Knowledge Graph
[1413] property graph on the jupyter notebook
[1415] this is also pretty good uh I find right
[1418] it shows that
[1419] comets very very nice visualization
[1422] within the Jupiter notebook itself
[1423] comets comets uh you know they are the
[1426] Rel related entities Etc
[1429] the I don't know what is this solar
[1432] system okay we we see all the all the
[1435] planetary body the definitions which are
[1438] given in this book are also coming up we
[1442] can see sun and some entities we can see
[1444] Chandra Yan one we can see definitely
[1447] Chandra Jan 1 2 and three will be there
[1449] in
[1450] this so this is also pretty good Mars
[1452] Orit Mission so India conducted the
[1455] smart s Mission captured images launched
[1458] in November 2013 Etc what all the things
[1461] it it observe bright
[1463] hazes what are the scientific
[1466] instruments it had pretty good
[1469] I I like this so this is a this is a
[1471] good example of simple Knowledge Graph
[1474] though I think the knowledge graph in
[1476] neo4j is richer that's the thing I saw
[1480] and we can same way we can ask the same
[1483] question and to this knowledge graph by
[1486] creating a query engine out of this
[1488] knowledge graph and asking the question
[1490] so we can see that and we can see the
[1492] source nodes from adding it so again
[1495] it's saying the similar answer Mars
[1497] orbit Mission uh and that's the and if
[1500] you see what's India's achievement in
[1504] chandran 3 as compared to the previous
[1507] moon mission it says very clearly that
[1510] uh chra are expected to provide Mission
[1513] inent so it gives a pretty good
[1517] answer but now we'll see that how we can
[1521] create uh this kind of flow with a with
[1525] a query in with a query tools and theout
[1528] router the query engine router which
[1531] allows to pick between multiple
[1536] uh so multiple uh modes of quering this
[1541] PDF so I can create a vector index I can
[1545] index so again the same thing document
[1546] simple directory reader I load the nodes
[1549] in this document and now I split using a
[1553] splitter create the chunks right uh
[1556] chunk size of whatever chunk overlap
[1558] right and a summary index out of it this
[1561] is a very powerful construct very
[1563] powerful way of storing the documents
[1565] which llama index provides I'm not sure
[1567] if it's there in langen I'm more of a
[1569] langen person but now I'm seeing the
[1572] capabilities of llama index so summary
[1574] index is a beautiful tool and Vector
[1576] index Vector database so we can create
[1579] this with a one line struct from this
[1580] nodes a summary index and a vector index
[1583] we create the query engines based on
[1584] this index the tools the query engine
[1587] tools from these engines right so we see
[1591] that uh now the important thing is now
[1595] we use a query engine router qu engine
[1598] which which basically can route the
[1600] question to either of these tools
[1602] depending on the question which is what
[1604] I find it very fascinating concept so I
[1606] have a summary tool I have a vector tool
[1608] now I can route it to either of these
[1611] using the llm single selector depending
[1613] on my query it will either go to the
[1615] summary index or to the vector index so
[1617] here is an example and I will run
[1625] this so when I run this basically it's
[1629] loading the PDF into
[1632] a set of nodes chunk creating a vector
[1635] Index right now it's downloading the
[1637] embedding model and then it's
[1642] basically uh I have two questions here
[1646] one is uh what is the India achievement
[1649] in the latest space mission etc etc and
[1651] another is what is the unique
[1652] achievement andan 3 so let's see how
[1655] these two questions are answered by this
[1658] router query
[1677] engine so creating the indexes
[1689] and takes a minute or
[1693] so so it says selecting query engine
[1695] zero useful for summarizing questions
[1698] summarization questions related to the
[1699] document for this first question it is
[1701] using the query engine Z which is a
[1703] summary tool and it's giving me an
[1707] answer India's recent space mission now
[1710] this is a correct answer if you see
[1712] compared to the others the latest space
[1714] mission when I say it is the Chandra Yan
[1716] 3 and it gives very nicely the answer
[1719] achieved a significant milestone for
[1721] India space exploration ERS by
[1723] successfully landing near the lunar
[1725] South Pole right it demonstrated India's
[1727] capability for soft Landing
[1730] operations additionally Orit Mission it
[1732] says also is a significant achievement
[1735] for the second question when I say what
[1737] is the unique achievement of Chandra 3
[1739] it says it is using the query engine one
[1742] which is the vector
[1743] index which is useful for retrieving
[1746] specific approaching recording okay
[1750] okay so which is
[1753] fine I'll probably join two videos
[1756] together I have few minutes
[1761] more how do I do
[1767] that e
[1801] so starting from our left off so
[1804] basically when I'm using a router query
[1806] engine we can see on the question it is
[1808] routing to the appropriate tool so for
[1810] the first question it routed to the
[1812] query engine zero and it gave me this
[1816] answer detailed answer in few
[1818] paragraphs which is what is India's
[1820] achievement in the latest space mission
[1822] give details of the most recent project
[1824] and related projects give me a lot of
[1826] information including Chandra Yan three
[1829] the Mars orbit the ad L1
[1832] Etc and the second question
[1835] was was so what is the unique
[1837] achievement of Chandra Jan 3 it went to
[1838] the query the query tool one query
[1842] engine one which is the vector tool
[1844] Vector index and it says that the unique
[1847] achievement it gives an oneliner answer
[1849] what is the unique achievement of
[1850] Chandra Jan 3 it is the successful
[1853] demonstration of critical Technologies
[1854] for soft landing and R operations in the
[1856] pretty pretty concise and pretty correct
[1860] of course so we can try various
[1863] variations of these questions and see
[1865] how the answers are coming but this is
[1867] to explore the capability of a query
[1869] engine using a summary index and a
[1870] vector index at the same time on the
[1872] same document and this can be
[1876] extended with a multi-d do agent so the
[1878] multidock agent what it does it picks up
[1881] the documents from one folder there can
[1885] be multiple documents like this there
[1886] can be multiple PDF files files within
[1888] the data folder and picks up these
[1891] documents traverses this file path and
[1894] for each of these documents it creates
[1895] this Vector query tool and summary query
[1897] tool and basically it uses the agentic
[1901] workflow which is basically uh it uses
[1904] the function calling agent worker from
[1906] the tools and again it uses the llm
[1909] where I'm here I'm using the
[1911] Mr so we need the mystal API key it's a
[1914] free key one can obtain from the mystal
[1916] API site and and uh we can get the
[1920] answer of the same question so we can
[1922] just run this uh python multi do agent
[1935] dopy so it's a pretty pretty much the
[1938] same as Square engine router but then
[1940] work on multiple documents as well so
[1943] that's the difference here and it is
[1945] using the function calling agent where
[1947] it's possible to send to the tools to
[1952] the document it's possible to send the
[1955] the metadata also so here for example we
[1957] can see in the vector to Vector tool we
[1960] can send the function that's why it's
[1962] called a function calling Vector query
[1964] is a function which is being sent to the
[1965] tool and the metadata dict is being
[1969] obtained at run time by the llm which
[1972] page has a proper information it's
[1975] inferring that and sending that page
[1976] number to the metadata filter so these
[1979] are all various facilities metadata
[1981] filters reranking this can all be used
[1984] with a one line of configuration and we
[1986] can see the answer it comes out pretty
[1988] good I think this is by far the best so
[1990] it says that
[1993] um it says India's latest space space
[1997] mission achievement is printing it twice
[1998] because I've given varos equal to True
[2000] over here so that's why while doing this
[2003] it's printing when I'm printing the
[2005] response it's printing again so India's
[2007] l
[2009] India let's see from where it's
[2012] starting uh India's latest space mission
[2015] achievement is a successful launch of
[2017] chandan 3 in 23 this mission is a
[2019] followup of chandrian 2
[2021] Etc includes a Lander Ander which will
[2024] conduct experiments to study the lunar
[2026] surface and subsurface Etc in addition
[2029] to three indiia uh has made significant
[2032] contributions to other space mission for
[2034] example Indian Mars Orit Mission also
[2037] known as mongal
[2039] Etc it has also various other things it
[2042] has reported over here joint Mission
[2044] with the n NASA and is a pretty good
[2048] concise
[2049] answer this one so this is getting over
[2053] using a multi-agent multi-document agent
[2057] and uh basically finally I use this same
[2061] concept but now I use the agent with a
[2064] with a Knowledge Graph this agent was
[2066] using this multi-document was was using
[2069] the sumary index tool and the vector
[2070] index tool but now now I extend this so
[2073] I I use the simple graph tool which I
[2075] showed in the notebook just now I create
[2078] a query engine tool from the graph
[2081] store and that's my graph query tool and
[2085] when I call this function I get the
[2088] three tools the vector query tool the
[2089] summary query tool and query tool right
[2092] and
[2094] uh so on once I do the in same way I
[2097] work on the documents found in this
[2100] folder and I this three tools and I pass
[2103] this three tools and at runtime it
[2106] basically inerts which is the best tool
[2108] and uses the tool so this is the object
[2110] and index from objects which which gets
[2113] the array of tools from all the
[2115] documents present in this folder it can
[2116] be multiple documents as well right now
[2118] I have one PDF so using one PDF there
[2120] could be multiple documents and using
[2122] the function agent function calling
[2124] agent worker it and we have to it gets
[2128] erble tools so we have to give a system
[2130] prompt so let's run this agent with
[2134] Knowledge
[2153] Graph so it's creating rules from the
[2155] files right now there's one PDF file it
[2157] created multiple tools and it will use
[2161] the llm to pick up the best tool for the
[2163] situation and give the answer the system
[2165] prompt has been given you are a space
[2167] scientist designed to answer queries
[2168] over a space exploration document please
[2171] always use the tools provided to answer
[2173] the question do not rely on prior
[2175] knowledge
[2176] right so let's see is the answer we get
[2179] on the same question from this tool
[2190] so I
[2192] would say whoever is seeing this I think
[2196] they will get interested in using Lama
[2198] index and the knowledge graph and this
[2200] function agents uh function calling
[2203] agent workers the query engine router
[2206] these are some of the I think the new
[2208] developments uh which are coming up
[2210] where we are not restricted to one rag
[2213] pipeline using a vector index or a
[2215] vector database but multiple such things
[2218] and at the same time and then selecting
[2221] the best not based on our experience but
[2225] using the llm
[2226] to judge which is the answer and give us
[2230] that answer obviously in a real life
[2232] scenario there will be many validations
[2233] there will be many such processes so now
[2235] it has created the tools and now it's
[2238] going to answer uh based on
[2241] that uh the
[2249] so it's a there object here there's a
[2252] tool object here there's a tool object
[2253] here so
[2255] India missions through missions like the
[2258] Chandra Jan series of Luna Mission
[2260] giving a more generic answer these
[2264] missions it also talking about the adiel
[2267] one which is the sun Observatory so it's
[2270] is talking about the Mars Chandra Yan
[2271] series of missions the Luna Mission Mars
[2273] Orit missions Etc the adita mission and
[2277] so
[2278] system the mission on studying the sun
[2283] it talks about that and it gives so we
[2286] can we can uh see what kind of responses
[2289] we are getting using these multiple
[2291] different approaches and pick up the
[2292] best approach that's the point I will
[2294] say this is still I would say the
[2296] corporates are still not using such a
[2298] elaborate scheme of using multiple
[2300] different rag pipelines and picking up
[2302] the best there can be many many
[2305] enhancements to this for example
[2307] creating data filters creating reranking
[2310] all this can be just given as
[2312] configuration in the Lama index the
[2314] reranking tool one simple configuration
[2316] right and it can be used with a low code
[2319] or no code approach so that is what I
[2321] liked about it I hope the viewers will
[2323] use this things uh and I would also see
[2326] if there can be suggestions how can be
[2329] made in more efficient the response
[2331] times or how to connect a Knowledge
[2333] Graph index to a pre-existing uh Neo
[2336] forg store rather than saying Knowledge
[2337] Graph index from documents every time we
[2340] can't uh you know Traverse to documents
[2342] and create the knowledge graph index
[2344] every time right we have we'll have a
[2345] store which will be stored maybe in a
[2347] batch program and then we'll just query
[2349] this of course there is something called
[2351] a Neo 4G query tool but using the
[2353] knowledge graph index is it possible to
[2355] con store and do this so all these
[2358] things we can explore and create a
[2361] agentic rag workflow so this agentic rag
[2364] workflow there is a course in deep
[2365] learning. where I've taken the inputs
[2367] from but added the knowledge graph
[2369] aspect to it also and created a agentic
[2372] workflow with with knowledge graphs so
[2375] that's what I was exploring and I found
[2378] it pretty good we have used it in some
[2380] projects and knowledge graphs but it's
[2381] not very extensively used also sometimes
[2384] it's difficult to find the relation
[2385] between the entities very effectively
[2387] there are false positive entities and
[2389] all that so the D duplication approach
[2391] which I saw there in the blog post which
[2393] I'll share the link is also a very good
[2395] uh suggestion and a very good solution
[2398] to such problems with that thank you so
[2400] much I hope you like it
