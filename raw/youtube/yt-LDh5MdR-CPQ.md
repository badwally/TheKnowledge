---
schema_version: 1
id: yt-LDh5MdR-CPQ
type: youtube
title: 'LlamaIndex Webinar: Advanced RAG with Knowledge Graphs (with Tomaz from Neo4j)'
url: https://www.youtube.com/watch?v=LDh5MdR-CPQ
authors:
- LlamaIndex
ingested_at: '2026-06-17T20:57:26Z'
content_hash: sha256:4ce4cf4a6c06862c679d084dcd5007d9d3cf87a03be751daa929a43bbc95da21
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: LlamaIndex
  channel_url: https://www.youtube.com/@LlamaIndex
  duration_seconds: 3206
  caption_track: fetched
  snippet_count: 1050
filter:
  score: 0.8
---
[0] hey everyone uh welcome back to another
[2] episode of The Llama index webinar
[4] series uh today is straping up to be one
[7] of our most popular webinars workshops
[9] ever uh with uh property graph indexes
[12] in llama index in partnership with neo4j
[16] um and so this is going to be a special
[18] workshop on teaching you how to build
[20] Advanced Knowledge Graph Rag and you'll
[21] be able to learn how to use our brand
[23] new property graph abstractions both uh
[25] to construct an existing graph as well
[27] as a queria graph um and so we're
[29] excited to host toas from neo4j as well
[32] as Logan from our side and without
[34] further Ado um feel fre to kick it
[36] off okay so uh like I said yeah I'm
[40] happy to be here and talk about
[42] graphs so as mentioned today we're going
[45] to talk about the new property graph
[47] index integration in Lama
[50] index and if you might be wondering
[53] property graph what actually is that
[57] right because most of the time
[61] I don't know if I can remove this so
[64] most of the time um when dealing with GS
[68] especially in the rec like Frameworks
[71] what we see is usually triplers just
[74] like subject uh relationship type and
[78] then uh object and the other way around
[83] but actually property graphs have now
[87] got uh an actual um
[91] standard and there's the new gql
[94] standard which is uh part of the iso
[99] committee um and uh that's very exciting
[103] uh but basically property graph as you
[106] might metion means that nodes have
[110] properties and relationships have
[112] properties as well so for example U here
[117] we have one node and it has property is
[120] name Amy PS date of birth employee ID
[124] right but it also has
[127] this one special property that we call
[132] label uh in property graph uh models and
[135] as you can see for example the green uh
[138] node has an
[140] employee uh node label right and node
[143] labels are used
[145] to put notes into sets sets of
[148] categories so for example in this
[150] example we have three node labels so we
[154] have employee company and
[157] City and as mentioned before uh
[160] relationships can also have properties
[163] right so it's a
[165] slightly different um data
[169] representation that what you might be
[171] used
[172] to like from the previous let's say
[176] implementation in Lama index the
[178] knowledge implementation where we only
[181] only dealt with
[184] triers so that's about property graphs
[188] and now let's talk a little bit about
[191] property graph index
[193] integration so the
[196] flow that uh most of the time you will
[200] follow when you're using property graph
[202] index
[203] integration uh you start with a bunch of
[206] documents and Lama index has great
[208] support for various types of documents
[211] uh so I will not go into that but
[214] basically documents you can think of
[216] them as just wrappers around
[219] text and so basically we take a bunch of
[223] documents and we pass the text from
[225] those documents to graph
[229] Constructors so in the integration that
[232] Logan did you can use one or multiple uh
[237] graph
[239] Constructors uh to create a Knowledge
[241] Graph and we'll talk a little bit more
[244] about them later I'll show you what
[247] which sh available out of the
[250] box and so uh the property the graph
[255] Constructors extract like structured
[258] information from uh documents and store
[261] them um as a graph in the knowledge
[264] graph so there are a couple of
[267] Integrations uh that Lama index already
[269] has
[271] uh as I'm from newj will focus on the
[273] newj integration but there are others as
[276] well and probably more coming
[280] up so once you've built your knowledge
[284] graph on the other side we have the
[286] so-called graphet
[288] rers so the graph ret rers their job is
[294] to uh basically based on the user
[298] question they have some sort of logic
[302] they can use to retrieve data from the
[305] knowledge gra right uh and again there
[308] are a couple of out of the box that you
[312] can use and we'll also show how easy is
[316] to
[318] um uh Define a custom uh graph in the
[323] workshop lated so that's basically the
[327] kind of the flow that you
[330] can think of and what llama index does
[333] is it provides graph Constructors and
[335] graph retrievers I mean obviously also
[338] the other parts just that the graph
[340] Constructors and graph retrievers are
[343] part of the new property graph index
[346] integration and the idea is that they
[349] are very modular and
[351] customizable so that if you're beginner
[354] you can just use something out of the
[356] box but if you like Advanced user and
[358] you need something custom
[361] it's very easy to customize uh the
[364] pipeline for your
[366] needs so let's uh like uh like on at
[371] high level property graph construction
[374] as I said we take a bunch of documents
[376] and we can select a Knowledge
[378] Graph so here I have an example uh uh
[383] documents where like former open AI uh
[388] employees founded new companies right so
[391] for example here you you would have four
[394] different um documents me read some
[399] information right but the nice thing
[402] about knowledge graphs is that you kind
[406] of condense that
[410] information and unify it right so
[414] that
[417] basically the information that was
[419] previous spread across multiple uh
[422] documents is now easily accessible uh
[426] and uh nicely represented in a Knowledge
[432] Graph okay and then I prepared uh couple
[437] of slides what is available out of the
[441] box in Lama index so out of the box we
[445] have
[447] three uh graph Constructors
[451] the first one is the so-called implicit
[454] pad
[455] extractor and what it does it it just um
[460] uh we have a new word for it it's called
[462] lexical graph but what it actually does
[465] you just take the green note is the
[468] original
[470] document and what it does it just
[472] chunks uh the documents so the what's
[476] this like uh Gray is
[482] nodes are text chunks right and text
[485] chunks are connected to the source
[487] document and then also we have uh an
[491] ordered list of text chunks so that we
[493] know uh how do they follow each other so
[497] this is the implicit P extractor um
[501] graph Constructor and it doesn't require
[503] an LM because it's just uh basically
[507] chunking up and then creating
[510] a linked list of text
[512] chunks so and then the next one is the
[517] simple llm P selector and as the name
[520] would suggest you need an llm for
[524] that and uh from what I've been digging
[528] around in the in in the um
[533] implementation how the simple llm ptic
[536] sctor works is basically through prompt
[539] engineering
[542] uh so you in the prompt you define
[547] um what uh like how the output should
[551] look like and then you provide
[554] U uh a paring function that uh extracts
[559] that uh output from an LM and creates a
[563] Knowledge Graph so it's I would call it
[566] like a plump based uh solution uh and uh
[573] by default all nodes have the same label
[577] like the default implementation all no
[580] have the same label and again the purple
[584] one is the text Chunk so we always store
[587] the reference text in the graph as well
[592] and then the no the the entities that
[595] were mentioned in the text Chunk we have
[598] the mentioned relationships
[600] to those uh
[603] entities and then obviously entities can
[607] have relationships between each other
[609] right so for example
[611] Amilia uh aard was American Aviation
[616] pioner right and this is kind of the
[620] simpler uh version of graph extraction
[623] now obviously you can customize it and
[627] make it more uh
[631] Advanced but by default um all nodes
[635] have the same label
[638] U
[639] yeah and then uh the more
[643] advanced is the schema llm P
[647] extractor so here you have the ability
[650] to Define which nodes and uh node labels
[654] and relationship types you can extract
[656] um this one will also show use in the
[659] work shop so you'll get to see uh
[663] in practice how that how do we Define
[666] the
[667] schema but basically as you can see by U
[672] by different colors of noes means that
[676] they have different uh no labels and
[680] again the purple ones are the text
[684] chunks the defin text chunks and then
[686] the text
[688] chunks mention the entities that
[692] appeared in those text chunks and then
[694] obviously we have a bunch of U
[698] relationships between uh those uh
[703] entities as well and this one uh works
[707] best with llms that provide function
[710] calling like native function calling
[713] like the
[714] commercial LS like open
[717] Gemini misal
[720] uh probably some others Gro is a nice
[723] one as well Gro is actually a really
[726] nice one because uh it uh it's really
[731] fast and that's really nice for the
[732] knowledge
[735] construction uh but yeah uh so it works
[740] best with u l with Native function
[743] calling but Logan told me that it will
[745] also work with
[748] u models that don't provide native
[751] function calling just not as well or
[754] maybe the schema uh should be simpl in
[758] those using those LS but U as I said I
[762] haven't tested that out but uh maybe you
[766] can test it out and let me know or let
[768] us know how it
[770] works so this is basically
[774] the uh out of the box graph Constructors
[777] that you can use
[780] uh and then uh what's not in
[787] the uh uh llama index yet but since
[792] llama index provides a low level
[795] connections to graph stor near for this
[798] example if we can also come up with
[801] custom entity dis disfiguration which we
[803] will do in this Workshop as well and
[807] entity dis immigation just means
[811] that if you have multiple nodes in the
[814] knowledge
[816] graph excuse me that reference the same
[820] real word entity you kind of want to
[823] merge them together into a single noes
[826] so that you have a better structural
[828] Integrity right so for here in this
[832] example this note ends with a limited
[835] this one has abbreviation limited and
[837] this one doesn't have limited right but
[840] it all references the same
[842] note so that mean that's why we want to
[846] merge it into a single note so that we
[850] have better seal integrity and in the
[852] workshop we'll use a combination of text
[854] embeddings and uh word distance heris
[857] stics to find potential candidates and
[861] then merge them uh together here is
[865] basically if you're uh anxious you can
[869] follow this link and this is basically
[871] the notebook that we'll be using
[874] today okay and then on the other side we
[877] have property graph
[879] retrievers so as you see I just took the
[883] previous image and just slice it up
[886] because here we have the remaining of
[887] the arrow but the graph retriever as I
[890] said uh based on the user input they
[894] have some logic how to uh retrieve uh
[898] information from the knowled
[900] graph and then pass that information to
[903] an llm so that the llm can generate the
[906] final l so basically a typical like
[913] Pipeline and we have I think
[917] four uh out of the box retrievers that
[920] you can use so here I didn't have time
[922] to draw nice diagrams so I just uh sum
[927] summarize them
[930] quickly so the first one is the llm
[933] synonym retriever it takes the user
[936] query generates synonyms using an
[941] llm and then it finds relevant notes
[944] using exact keyword match so that's
[946] really
[948] important because llm is not aware of
[952] any values in the database when it's
[955] generating the
[957] synonyms so it's not
[959] not uh are given that the llm will know
[965] which like how to construct the keywords
[968] so that they will match any notes in the
[971] graph so because it uses at least the
[974] new forj um integration uses exact
[977] keyword match it's the least reliable
[981] right because it needs exact keyword
[982] match we
[986] could we could basically optimize this
[989] uh to allow some misspelling or stuff
[992] like that but at the moment it's using
[995] exact keyword match and then once it
[998] finds a relevant
[1000] notes it returns basically the direct
[1004] neighborhood or basically you have an
[1006] option to
[1008] decide uh how many like what's the
[1012] distance what's the neighborhood size of
[1014] the nose that you want to return so by
[1017] default we return just Direct neighbors
[1020] of that
[1022] node and then the second one is the
[1025] vector
[1028] context so um in the previous one we
[1031] used exact keyword search to find
[1033] relevant notes but here in this example
[1036] we using Vector search so that means
[1039] it's more robust and less reliable on
[1044] exact keyword match that because with
[1047] keyword with Factor search
[1050] you will always get some results from
[1052] the database because you take top
[1055] n uh and then uh hopefully some relevant
[1059] notes are
[1060] identified using Vector search and then
[1064] uh we just do the same thing as we did
[1066] in the previous one we just return the
[1069] direct neighborhood uh of relevant nodes
[1072] that were found using the vector
[1077] search and then another one uh is the
[1082] textto cipher
[1084] so as the name
[1086] implies we the take the text and use an
[1091] llm to generate Cypher statement so this
[1093] is kind of very
[1097] um flexible approach right because the
[1101] line can construct any sour of uh Cipher
[1105] statements so for example um with oops
[1110] how do I go back with Vector context
[1112] right when you're just finding for uh
[1116] searching for Relevant notes using
[1119] Vector search and then returning direct
[1121] neighborhoods it's very hard to answer
[1124] questions like how many nodes are in the
[1127] graph because it's like an aggregation
[1133] query and Vector Contex is not suitable
[1137] for aggregation queries
[1140] uh at least not like on the global scale
[1144] um but like for example with texer you
[1147] could ask it questions like how many
[1149] nodes are in the graph or like how many
[1151] P are in the graph and the lln will
[1154] generate a
[1157] appropriate U Cipher statements and
[1161] return that information for you that so
[1164] text CER is much more flexible than the
[1167] previous TOS but but the on there's
[1172] obviously always a tradeoff that is less
[1174] reliable because we're using Ln to
[1176] generate saer statements and
[1179] that's at the moment how is it it's
[1182] mostly
[1183] correct uh but that just but not like
[1187] always so you kind of U trading
[1192] of flexibility for a bit of accuracy um
[1196] but then on the other side what you have
[1199] is also
[1201] uh some different uh like Tex CER allows
[1205] you to also do aggregations and stuff
[1208] like that which the
[1210] previous uh uh R didn't allow
[1214] you and then the last one is the
[1217] so-called Cipher template
[1220] R and here instead of generating Cipher
[1225] statements with an llm you basically
[1228] Define the CER statements you want to be
[1231] executed and you just
[1233] um parameterize or like provide like a
[1237] parameterized cipher template so
[1241] basically you have uh a cipher statement
[1245] with like one or more um uh parameters
[1251] and then at credit time basically the
[1254] llm you provide uh instruction to to an
[1258] llm how to populate those uh
[1261] parameters and then at query time uh llm
[1266] extracts relevant parameters it needs to
[1269] use with the cipher
[1271] template uh populates the template and
[1274] then executes the predefined cipher
[1277] template so that's where the template
[1280] comes from because it's uh
[1285] predefined and then uh here I have
[1288] questions but let do a
[1291] demo to I'm just going to read through
[1294] some questions in the chat so far just
[1296] to make sure we cover some of them um
[1298] before uh before the workshop um the
[1300] first is um I think one question is
[1302] actually about using llms and um if you
[1306] have a set of recommended LMS that you
[1308] think are better for say like Knowledge
[1310] Graph construction um as well as the
[1312] cost of running llms across a large
[1314] Corpus of documents to construct an
[1316] allograph I'm curious to get your
[1318] initial there um as well as like
[1320] recommendations for some of these users
[1322] some of them are thinking about using
[1323] like rock for
[1325] instance yeah so what you will see is
[1327] that graph constru like
[1330] LMS and graph construction it's very
[1333] model dependent so different models will
[1337] uh generate different graph graphs and
[1342] it's very like given different versions
[1344] of GPT 4 will behave
[1347] differently so so I did some testing
[1351] like I'm not like an expert in all of
[1353] the LNS but for example what I will tell
[1355] you when you're using like a predefined
[1358] schema uh like the GPT 3.5 will try to
[1362] fit all that information into the schema
[1366] so that uh it kind of over fits
[1370] information into the schema where
[1373] uh uh uh it's not really where it
[1378] wouldn't really fit in reality but then
[1380] GPT for Turbo and the for are much
[1385] better at like ignoring the information
[1389] that is not part of the
[1391] schema uh for example if you want to use
[1395] I would really recommend using LMS that
[1398] are fast so for example gp4 just throw
[1401] it out of the window because it takes
[1403] forever and it's costly right so in that
[1406] like grock is really ni nice CU it's
[1409] really fast but then the problem with
[1412] Gro is they don't don't want to take our
[1414] money just yet so hopefully when they
[1417] will be taking out credit cards that's
[1422] something I would definitely uh look
[1425] into but like in general it's like the
[1430] better the model the better will be the
[1432] results no more it will follow um The
[1435] Prompt instructions right so uh great
[1439] and just following up with with just one
[1441] more quick question is um uh you know
[1444] this might not actually quite exist in
[1446] in some of our obstructions right now
[1447] but um one of the questions around like
[1450] dealing with missing information from
[1451] the graph which sort of implies this
[1453] like maybe you do some LM construction
[1455] pass it's not completely exactly where
[1458] you want it to be and so you do some
[1460] human um in the loop PA to try to like
[1462] modify and shape the graph uh to you
[1465] know better reflect what you want out of
[1467] that data um have you seen that like
[1469] kind of human in the loop approach
[1471] towards like graph
[1473] construction so it's not really human in
[1475] the loop it's more like they have some
[1477] characteristics because I didn't really
[1479] mention but it
[1482] the if you want to take a look U the
[1486] grass rack by Microsoft paper is really
[1489] nice and it deals with some of this uh
[1493] questions so the first one is also like
[1496] what types of what what's the size of
[1499] text chunks you should use right and the
[1501] thing is the it's kind of funny like the
[1506] number of notes and relationships is
[1509] kind of irrelevant to the chunk
[1512] sizes so that just means if you're using
[1515] smaller text chunks more information
[1518] will be selected and if you're using
[1520] bigger text chunks like this the overall
[1524] number of extractions will be the um
[1527] extracted information will be the the
[1528] same but since you're using larger text
[1531] chunks right on the like in summary less
[1536] information will be extracted from
[1539] larger text CHS so that's one one one
[1542] thing they mention in the paper and then
[1544] the second thing they mentioned they
[1546] have some sort of
[1548] characteristics where they can decide
[1550] okay not enough information was
[1552] extracted from the text and then they do
[1555] a second R so basically instead of
[1557] having a human in the it's kind of
[1559] automated and saying okay you didn't do
[1562] a good enough job now let's do a second
[1565] pass on the
[1568] graphic oh okay yeah super
[1572] interesting any other questions
[1575] so should be feel free to carry on
[1577] there's a ton of questions but I think
[1579] we'll
[1582] mean because the extraction part will
[1585] take a couple of minutes and we can uh
[1589] answer questions um so here I I Define
[1595] My Graph St
[1597] so okay just second okay that's
[1603] fine and uh one thing I also noticed is
[1607] that people are sometimes confused by
[1609] documents uh because like all Lama
[1614] index um mostly deals with the document
[1617] right but document is just a dier around
[1619] the text so it's very easy to go from
[1622] text to document we just instantiate a
[1626] document with the text property and
[1628] that's about it right so so here in this
[1631] example we're going to create a bunch of
[1635] documents based on the news so we have a
[1638] bunch of news um and we're going to use
[1642] GPT Pho and for example one thing that's
[1645] also interesting there's like a lot of
[1648] things
[1650] uh that comes popping up and uh one
[1652] thing I noticed today was today or
[1656] yesterday somebody did some benchmarks
[1658] and they said basically that if you're
[1661] using slightly higher temperature than
[1663] zero even for the the terministic tasks
[1667] you get better the results and that's
[1670] like and it was specifically for
[1673] photo right so again that's kind of very
[1677] interesting and we we all learning uh as
[1680] we go along
[1682] right but as as as mentioned we're going
[1685] to use the schema llm pet instructor in
[1689] this
[1691] Workshop so with schema llm pet
[1694] instructor you have to Define the types
[1697] of notes do you want to selct so here I
[1699] went for person location organization
[1703] product and event so it's mostly a very
[1707] um typical
[1709] uh
[1710] extraction and then there's the event
[1713] which is kind of more ambiguous and in
[1717] allows the llm to extract any type like
[1720] a lot of information right because event
[1723] can be anything
[1726] basically and then I also we also have
[1730] to Define the types of relationships we
[1732] want to exct so here I focused more on
[1736] the like organization business part
[1739] where we have suppliers competitors
[1742] Acquisitions subsidiaries CEOs stuff
[1745] like that so we're going to hopefully
[1748] extract some
[1750] business relevant SL financial
[1754] information hopefully from
[1757] the knowled gra and then uh so this is
[1763] the first part of the when we are
[1765] defining the scheme and then the second
[1767] part is we also have to
[1770] Define uh which information which
[1774] relationships is assigned to each person
[1777] right because not all relationships can
[1781] be part of all node labels right so we
[1784] have to Define uh so for example a
[1788] product only has provides uh
[1790] relationship and then provides is only
[1793] on the organization so then I um iide
[1798] the would generate only provides
[1801] relationships between organizations and
[1803] produ
[1805] because it's it doesn't really make
[1807] sense to have uh provides relationship
[1810] from location to let's say a product so
[1813] this is a a little bit more granular
[1816] um schema definition uh that we need to
[1822] provide and then we just uh let's go
[1827] with 100 uh and then we just pass the
[1830] possible entities relationship
[1832] validation schema to the llm and here
[1836] you have the strict mode so strict mode
[1840] like even if you
[1843] provide instructions to the llm which
[1847] types of noes and relationships it
[1850] should use it doesn't really mean that
[1852] it will follow them oops bad idea 100%
[1856] correct right because l just LMS they do
[1859] what they
[1862] want and then Logan uh implemented a
[1866] strict mode so it means that but since
[1870] we know the types of relationships and
[1872] noes we expect we can filter them out if
[1877] we want to uh in the code right or we
[1881] can leave any other nodes in the
[1884] relationship that
[1885] identified so in this case let's just I
[1890] love any information uh
[1894] the llm decides additionally to extract
[1898] now gp4 is quite good at
[1901] following um the provided schema but
[1905] other models and this is also because as
[1908] I said gbt for is an native function
[1911] calling model so when you're using
[1914] functions or tools to extract
[1917] information s information
[1919] it will have much better accuracy
[1922] whereas like llama 3 which is not Gro so
[1926] Lama 3 via orama right doesn't have
[1929] function calling it's still a really
[1931] good
[1932] model but it might not follow the uh
[1937] schema always right so that's why you
[1940] have the option to filter it in
[1944] postprocessing if you want to or not and
[1947] here we'll go for
[1949] not and we're going to exct information
[1953] from 100
[1954] articles and it's going to take like two
[1958] three minutes I think so we have time
[1961] for a couple of
[1965] questions um yeah for sure I'm trying
[1969] I'm trying to figure out what questions
[1970] asked um maybe maybe one thing is um uh
[1974] actually going back to the retrieval
[1976] side so you know there is Vector search
[1979] with the vector context Retriever and
[1981] then there's also Tex de Cipher um you
[1983] mentioned some limitations of uh Texas
[1986] Cipher like in your mind like what are
[1988] some of the maybe like tips and tricks
[1990] you see in getting Texas Cipher working
[1992] a little bit better for users um in
[1995] terms of making it making sure it
[1996] generates more reliable Cipher queries
[1998] how to make sure it actually retrieves
[2000] Val in
[2003] context
[2005] so but I mean this is kind of hard
[2009] question
[2010] so text Cipher works good for like the
[2016] when the user knows what's in the
[2019] database right and knows how to ask the
[2023] questions that fits the
[2025] schema right so that's one thing and
[2029] then how do you achieve that so what you
[2032] could do is you could have some qu re
[2034] writing steps that take the user input
[2038] and rewrites it into more of
[2042] a a question that fits the graph schema
[2046] and it's a little bit more verbos or
[2049] implicit on how it wants the information
[2052] to be
[2054] retrieved so that's one thing uh
[2057] obviously providing it with few short
[2059] examples is very
[2062] helpful because by default it uses zero
[2065] short um generation right which we just
[2068] give it the graph
[2070] schema and then hope for the best but
[2073] what you can also do is you can uh also
[2077] provideed few short examples and then uh
[2080] hope that it follows those examples and
[2083] obviously the thing is like with more
[2086] complex graph
[2089] schemas uh there's like a the just how
[2094] to describe those schemas takes a lot of
[2096] tokens so when
[2098] like and then maybe not linearly but the
[2102] bigger the size of the schema the less
[2105] it will I mean yeah the V the accuracy
[2109] will be so what you can also do is then
[2112] um just provide parts of the schema so
[2116] instead of having one text to Cipher
[2118] that deals with the whole graph schema
[2121] what you can do is you can
[2123] have like an
[2126] agent with like several tools and then
[2129] each of those tools uh focus on
[2132] different parts of the schema right uh
[2134] so you kind
[2136] of lower the complexity of the
[2140] task
[2142] yeah yeah that makes a lot of sense um I
[2145] know it's about to finish up um but that
[2149] maybe just another question and and we
[2151] can also carry this over after things
[2153] are done but is ne4 designed to uh work
[2157] with like uh like technical document use
[2159] cases like patents and scientific papers
[2163] um like will help in identifying and
[2165] building relationships between you know
[2167] science technical Concepts uh that's one
[2169] of the questions from the
[2171] audience yeah so um yeah how you say Neo
[2176] is domain agnostic so you can store any
[2178] information you want in it that being
[2182] said it's quite quite funny that you
[2184] mentioned patents and uh
[2188] technical document documentation because
[2190] that's really relevant or at least what
[2194] we see a lot of pharmaceutical or
[2197] biomedical companies right this is such
[2201] there's a lot of money in patents and
[2205] for me it was also
[2207] interesting for example biomedical
[2209] companies when they have this great idea
[2211] what we should do or what we should
[2213] research you know what they first do
[2215] they check if there's already a patent
[2218] right and then if it's already a patent
[2220] they don't research it because it won't
[2222] make money you can't patent it so and
[2227] I've seen uh basically like big
[2229] pharmaceutical
[2230] companies they all have their patent
[2233] graph they all like uh scrape like PM
[2238] you don't actually have to scrape it
[2239] because it has apis right but it's like
[2244] you can think of it like biomedical
[2245] technical documentation like with all
[2247] the latest research and they generate
[2250] knowledge graphs uh from those and then
[2254] use it to inform or recommend so one
[2258] thing that they do is basically they
[2261] generate graph from all the latest
[2263] research then they use
[2266] recommendations uh to to recommend to
[2269] doctors based on their specialization
[2272] which articles they should read right so
[2276] yes definitely NE can be used for um
[2280] patents and is actually used by existing
[2283] customers for patents and Technical
[2292] documentation okay yeah so now that
[2294] we've uh imported the graph we can also
[2298] take a look at
[2303] it not right graph is visualizations are
[2308] quite
[2309] nice so let's see we
[2316] have okay so we can see that
[2320] uh uh for
[2324] example let's see why why we have an
[2327] award we have two awards no LEL so
[2330] that's kind of funny but it wasn't in
[2334] our
[2336] uh description right so even GPT 40 can
[2340] decide oh a about really nice of the FA
[2344] Cup and the English legal title so let's
[2348] see basic probably will be who won so it
[2352] was gold
[2354] McQueen what the cup so probably there
[2358] should be a football team in there but
[2361] it's interesting you can see that even
[2363] uh and we have a disease as well one
[2367] this so even GPT
[2369] photo can
[2371] decide uh to add some information uh
[2376] that wasn't in the uh schema so that's
[2379] why we have the
[2381] um the strict mode
[2384] right if we use strict mode through we
[2388] wouldn't see those these uh nodes in the
[2391] graph because
[2394] um obviously we would filter them out PR
[2397] automatically right and then let's try
[2404] to see if we
[2406] have I'm trying to find if there's
[2409] anything more connected but basically
[2415] unfortunately okay
[2418] cool and let's
[2422] uh so we have for example United he
[2425] group is a note and now we can see a
[2429] bunch of competitors
[2431] right and we can also see probably it's
[2435] not doing so well because it had a stock
[2438] sell off and stock prise decline right
[2441] and this is as I mentioned event is kind
[2443] of ambiguous and it can be a lot of
[2445] things so in this case it was stock has
[2450] stock
[2451] price declined and JN X works at United
[2454] H group that so like all over all uh the
[2460] GPT for all uh followed
[2465] uh the uh uh schema right quite nicely
[2470] and we can see like a nice graph uh over
[2473] here and let's
[2476] go forward and then as I mentioned
[2481] before entity duplication is kind
[2484] of a must I think it's
[2488] often Overlook but you kind of want to
[2491] uh find uh
[2493] entities like notes in the graph that
[2496] reference the same uh real world entity
[2499] and merge them and here we have a kind
[2502] of involved Cipher query which took like
[2505] eight hours to come off
[2507] it by multiple people but in the end uh
[2512] we found like a nice way of using um
[2515] text and beding so here we have the code
[2517] and similarity threshold and then weary
[2520] distance so how many characters can you
[2523] change in
[2525] uh in the string to have it the same and
[2528] you can see it works quite well like so
[2531] for example Bank of America and Bank of
[2533] America
[2534] Corporation music music
[2537] group like new newcast United coinbase
[2541] so overall it works really nicely to
[2545] find uh
[2548] uh like this duplicates but obviously
[2551] it's not perfect because nothing in life
[2553] is perfect so for example this one is
[2558] kind of I mean it's the same it's still
[2562] Jeff vual space suit that but one is
[2566] fire side chat which is what yeah maybe
[2570] not really but fine and for example
[2574] Baltimore this one also right okay I can
[2578] understand that these two should be
[2579] merged but maybe this is a city and
[2582] shouldn't be merged together
[2585] that so as always uh you have the option
[2591] uh to uh tweak these two parameters and
[2596] you also have the option to uh then do
[2598] some manually like human in theop here
[2601] human in the loop is kind of important
[2604] to know what entities are you emerging
[2608] in uh but I think like just having like
[2612] some sort of Baseline to start with uh
[2614] is really nice and I think this Cipher
[2617] credit not really nice because you can
[2619] see a lot of um entities that should be
[2623] merged together that and let's just
[2626] merge them
[2628] together and then for the last part as
[2631] we
[2632] said we're going to implement a custom
[2636] the
[2637] and we have the four uh existing ones um
[2642] but here we're going to implement um a
[2645] ret that first
[2647] identifies
[2649] um all the relevant entities in the text
[2653] because for example the vector
[2656] context just takes the whole
[2659] string uh embeds it and then finds
[2662] relevant not that but what if multiple
[2665] entities are mentioned in the text
[2669] then like vector index might not be the
[2673] greatest because if
[2676] you if uh it will embed the both
[2682] entities into a single uh embedding and
[2685] then who I don't really know who really
[2687] knows what happens with those numbers
[2689] there's a bunch of zeros and ones and
[2692] what do they actually represent who
[2694] knows so what we'll do really quick
[2698] before the retrieval piece um actually
[2700] quick question on the entity uh disin
[2703] viation um that Cipher query I mean
[2706] given how involved it is but given the
[2709] fact that I imagine like a lot of people
[2711] probably need to do some sort of DD is
[2713] this like a template that's just like
[2715] shared publicly because it seems like it
[2716] would be generally useful for a lot of
[2718] people yeah yeah this is uh part of the
[2722] blog is this is all available
[2725] uh over
[2729] I mean we can add a link in the webinar
[2733] if you know how to but it's this one so
[2739] if
[2741] I I know how to do
[2745] chat let me spam it a little bit
[2748] uhhuh to everyone yeah no problem I
[2750] think we shared the notebook yeah we
[2752] Shar the notebook in the chat but
[2753] basically like that basically your the
[2755] to the audience it's like if you want
[2757] just a nice Cipher query to do n d dup
[2760] obviously there's some limitations you
[2762] probably need to tweak the the word
[2764] similarity and those types of things a
[2765] little bit but like if you want an
[2768] existing template to go off of you can
[2770] just like copy and paste from this
[2771] notebook right because it's a pretty
[2772] long Cipher string so I would imagine a
[2774] lot of people are gonna be able to write
[2776] this it's also I I would I would make it
[2780] a model in llama index it's just that
[2783] then it's like read NE forj specific and
[2786] then like it's it doesn't fit the best
[2789] into llama index like because you guys
[2791] want to have things that are I say
[2794] integration agnostic so uh but maybe we
[2797] can figure out that in the coming months
[2801] how to add that because it would be nice
[2803] to have those out of the box right uh
[2806] you just
[2807] expose these two parameters and uh let
[2812] it do the magic right but maybe this is
[2816] something yeah is I think even the raw
[2818] Cipher is useful for for the audience um
[2820] and then I just doing a quick check on
[2822] time I know we have you know technically
[2824] 5 to 10 minutes left um but you know I I
[2826] know the last section is just like the
[2828] custom retrieval section but maybe we
[2830] can can just like walk through the high
[2832] level Concepts maybe just like go
[2834] through the overall class and then and
[2836] then that should be a good conclusion to
[2837] to this Workshop yeah we can do this
[2840] actually quite fast so as I said we
[2843] extract entities uh from um the user
[2846] input and we use a
[2849] identic uh open identic Pro program so
[2853] basically
[2855] again I would imagine we we kind of use
[2858] function calling behind the scenes right
[2860] we
[2861] say this is your input parameter and
[2864] it's a list of named entities in the
[2866] text and we we ask GPT for o to um
[2872] select it uh so basically so then okay
[2877] I'm rambling a bit but uh so how do you
[2880] define your custom retri uh so your
[2883] custom retri just needs two methods or
[2886] actually just one but the in it is also
[2890] quite nice if you want to uh instantiate
[2894] for example some other functions or
[2897] classes and in in in the in it here we
[2901] uh instantiate entity extraction which
[2903] is the open identic program right the
[2908] to Define to extract relevant entities
[2910] from
[2911] text and then we also extract Define or
[2916] instantiate um existing Vector Contex
[2920] retriever uh we can use
[2923] it and then u in the custom retriever
[2927] it's actually the code is very simple
[2929] right we just uh exct or
[2933] find detect it maybe the best word uh if
[2938] there are entities in the text so if
[2940] there are entities in the text we just
[2943] uh run a vector retriever for every
[2946] entity in the text and if the llm
[2950] doesn't find any uh specific entities we
[2954] just use the vector to div on the whole
[2957] text sline and that's basically it and
[2961] then you you have a couple of
[2964] options how you do you um on the
[2969] structure or format of the results that
[2972] you can pass back to dat L and here in
[2975] this example we just pass back the text
[2979] we can remove this because we don't need
[2981] to change anything uh yeah
[2987] and then we just basically instantiate
[2990] the whole thing and let's see what
[2994] happens so if you ask what do you know
[2996] about Mal or
[2998] data basically the Ln detects two
[3001] entities right and then for each of the
[3005] those two entities it R Vector retriever
[3009] separately so that it kind of ensures
[3013] that we will get both information for
[3016] both for both entities right because if
[3019] you just
[3020] use Vector on the hor string or text
[3024] anding of the on the hor string you
[3027] might just get it for one entity but not
[3030] the other right because if you use topk
[3032] for maybe one is more significant uh in
[3037] the text and bearings but with this
[3039] approach we make sure to cover all the
[3042] entities so we get a nice answers for
[3046] both
[3048] entities so yeah
[3050] that's like a high level overview of the
[3053] D and now we
[3055] can uh answer a couple of questions
[3060] again yeah and and maybe just to kind of
[3062] like say a few words to um to help wrap
[3066] this up I think you know what Tomas
[3067] really showed you was an end to-end
[3069] process of both like constructing a
[3071] Knowledge Graph um and then also
[3073] retrieving from it and not just that
[3076] like showing both the high level API as
[3078] well as the lower level API so whether
[3080] you're a beginner user for nfts and llms
[3082] and L index and neo4j you know you can
[3084] basically get do all this stuff in about
[3086] like five lines of code or if you really
[3088] want to go in you're an advanced user
[3090] you're pretty familiar with M crafts we
[3092] offer a lot of opportunities for you to
[3093] Define your own custom extractors right
[3096] uh with our core abstractions um like a
[3098] robust like property graph store like
[3100] the underlying lowlevel like storage
[3102] system to
[3120] um I think a lot of people are
[3121] interested in knowledge crafts we
[3123] basically see it as like a superet a
[3125] potential superet of existing rag
[3128] Solutions especially if you're able to
[3129] leverage these like properties and
[3131] relations to help augment your retriable
[3134] um and there's a lot of very
[3141] interesting like an Enterprise developer
[3143] You're Building all crafts within uh the
[3145] company um feel free to you know reach
[3147] out to one of us for any sort of like
[3149] blog posts case study we're always happy
[3151] to feature like really interesting use
[3153] cases of like knowledge graphs llms like
[3156] w index and and neo4j right um and so
[3159] always happy to Showcase like very
[3161] interesting applications um but
[3163] hopefully this Workshop was was useful
[3165] um to all of you today uh and you know
[3167] we'll have this on our YouTube um
[3169] Channel and then basically hopefully
[3171] we'll do you know maybe even like a
[3173] series covering like other types of
[3174] topics um as we go forth but we're
[3177] definitely looking forward to to new
[3178] types of applications um built with like
[3181] knowledge crafts kgs and and L so I
[3184] think I think with that said it's
[3186] probably a good time to generally wrap
[3188] up and really sorry I think a lot of you
[3189] had a lot of questions in the in the
[3191] chat um we uh weren't able to get
[3194] through all them but we'll have this
[3195] YouTube uh video out and basically feel
[3198] free to comment there as well so thank
[3200] you everyone thank you to and thanks
[3202] Logan for for hopping in
