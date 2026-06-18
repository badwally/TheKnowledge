---
schema_version: 1
id: yt-cNui87jWYRU
type: youtube
title: Knowledge Graphs in RAG | KGC 2024
url: https://www.youtube.com/watch?v=cNui87jWYRU
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-17T20:57:31Z'
content_hash: sha256:1bcd317d1fd830f8a89f4a83a47de7b9c10dedb4d1b3ac7a5bf12fd898ea27b6
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 5791
  caption_track: fetched
  snippet_count: 2548
filter:
  score: 0.85
---
[200] discussion. There's a lot of people who
[202] are in
[206] specific
[259] testing.
[263] Yes. Computer. Yeah, I'm muted myself.
[351] Are
[611] little technical issues and we cannot
[614] hear and also we're not sharing the
[617] presentation.
[653] testing.
[655] Okay. Yes, we have audio now. Can you
[658] share your desktop the slides, please?
[660] Thank you.
[664] Not quite sure what's happening. Uh,
[671] all right.
[673] How's that?
[676] Great. Okay, let's get back to it. So,
[678] I'm making schema controlled automated
[680] knowledge graphs. This is what a schema
[682] looks like in our instance. I know the
[684] word schema is difficult. I know it's
[685] used for a lot of things, but this is
[686] broadly what it looks like. Now the
[688] point of this is so people who are
[691] non-technical or interact in natural
[693] language in this case English can
[696] constrain what's made. So you define
[701] characters or the entities you define
[704] the relations and then finally you
[706] specifically talk about the patterns. So
[709] the patterns being the triples and being
[711] the constraint. All of this is to say,
[713] you might have seen LLM make knowledge
[716] graphs before, and LLMs are fantastic in
[719] terms of they're generative and
[720] creative, and what they produce is
[722] entirely often new and different, and
[724] then potentially hallucinatory and
[725] wrong, right? So, there's some great
[727] benefits to that. There's also some
[729] problems. So, what we want to do
[732] is make sure we add some documents. So
[735] this is a case of just adding the
[737] Seinfeld schema up and then we run
[740] create graph
[743] and then we also have a query graph but
[746] you can see that this is our SDK. So in
[750] as few lines of code as possible we
[754] wanted to set the documents, set the
[757] name space, bring in the schema I showed
[760] you here which you can edit and just
[762] change and redo. uh and now you can
[764] create a graph from that schema and
[766] again we have create graph from
[767] questions we have create graph from view
[769] I'm happy to talk about them another
[770] time but right now we I'm trying to run
[772] the create graph from schema and then if
[775] I get out of this
[778] I'm using nearj aura for this example uh
[780] or I'm using nearj more broadly um can
[784] use any graph provider I really like
[785] using uh I like their uh auras very easy
[788] for people to use and now what I want to
[794] is let me run it and make sure it's
[796] running.
[797] I'm going to create a graph, right? And
[799] so this, by the way, this is a
[800] completely free Aura instance.
[803] Um I just have it running here to show
[806] that we're making it. So now I can keep
[808] kind of iteratively creating the graph.
[811] So I'm just running a create statement
[813] as I go uh sorry, a match statement as I
[817] kind of iteratively build out the
[818] triples and the patterns. And what
[819] you'll notice on the right is that the
[822] nodes and the relationships are limited
[824] uh to the ones that were in the schema.
[827] So part of the problem when you create
[829] graphs, at least what we found, maybe
[830] someone else in this room solved it.
[832] Part of the problem is that you um if
[836] you let an LLM make you a graph, it will
[839] make all sorts of things. But if I look
[841] at this graph specifically,
[844] you can see that it's extracted things
[845] like Jerry and George. And I
[848] intentionally threw this in uppercase,
[850] lowerase because of Parker's great talk
[851] yesterday around entity resolution. And
[853] I think that's important, but if I
[854] wanted to just lowerase this document, I
[855] could. But it's the the idea is that you
[858] very quickly made this graph, but all of
[860] the edges and all of the nodes are
[862] timed.
[865] So now when you want to query it, you
[866] can specifically get back the query you
[868] want. Further to this, I'm going to
[870] remove this contains
[872] limiter. I know this is a small screen.
[874] Sorry for those. I'll try and zoom in.
[875] I'm going to remove the contains
[876] limiter.
[880] And now we actually have
[883] significantly more relations because
[886] let's just take this chunk for example.
[890] We've actually through the rag process
[891] chunked every document. So our process
[895] is chunk or split a document and then do
[899] some level of extraction on that
[901] document. I know this this is a very
[902] connected gra this is part of my point
[904] about why graphs right because it's
[905] difficult to fully but in terms of a
[908] demonstration I can subgraph it and
[909] limit it but these chunks or these nodes
[912] this is the information this is the text
[914] that we've then extracted from got these
[916] entities what that means is that when
[919] you query there's massive benefit to
[922] querying a knowledge graph in the rag
[924] process but you get back the context
[926] that made it
[929] this is all to say that we've built
[930] something and that it works. We can run
[932] it, we can delete it, and we can go
[933] through that process. I just wanted to
[934] show you that we are building this stuff
[935] and we are working with it. This is the
[937] type of stuff we do. But now jump back
[939] in to what I was talking about,
[943] which is again why you should listen to
[945] me. Um, I've built a lot of graphs in a
[949] lot of different uh technologies. My
[952] masters and PhD was largely in protege
[954] in RDF and I'm sure a lot of people in
[956] this room have spent a lot of time in
[957] that. Um, but we're working in rag and
[959] rag specifically and how we can improve
[961] the rag process. And so those graphs
[964] that we build is like how quickly can we
[966] get someone to seeing what a graph is.
[969] Don't know if people in this room have
[970] had this problem, but it's like part of
[971] the difficulty is people like graphs
[973] look good, I can't necessarily use them.
[976] So this is why I like using graphs. who
[980] may agree or disagree but the relations
[982] are the valuable part right and I can
[984] see it so there's very few databases
[986] where you can see your schema and you
[988] can you know uh control what's happen
[991] again with the schema example I can just
[993] write something different if I want
[994] different characters if I want to say
[997] sandwiches it will find the sandwiches
[998] in there I can control the
[1000] representation I can visibly look and
[1002] see what happened and this is especially
[1004] important when it comes to rack or more
[1007] broadly LLMs because I don't necessarily
[1009] know what LLM are doing. I know they're
[1010] doing something and that's often very
[1012] intelligent, but what is happening I
[1014] would like to see. This is why I like
[1016] graphs.
[1018] This is what's easy about graphs. I'm
[1020] not sure if you guys would agree, but if
[1022] you make a graph for someone, they very
[1024] quickly look at it and can say, "Oh, I
[1026] get it, but why is it this way?" And so
[1028] then you create this broad discussion as
[1030] to what was made and exactly why am I
[1032] doing this if it's something that you
[1033] can see.
[1036] problem with graphs is that once
[1038] everyone can access that right everyone
[1041] can look at what it is that you've
[1042] created everyone can have an opinion of
[1044] what you've created so part of the
[1047] difficulty when we make graphs for rag
[1050] is that it's there to answer a specific
[1052] question but I was through my PhD at a
[1055] conference in Oslo at DNVGL which was
[1058] amazing but I I saw a 4-day conversation
[1061] about terminology like what is a process
[1063] what is a system well these are very
[1065] necessary conversations. Uh the
[1068] difficulty is how many different people
[1069] can contribute to this. If you are
[1072] making a graph like a snowman, that is
[1075] exactly what it should be. It should be
[1076] agreed upon definition. It should be
[1078] broadly applicable and it should be a
[1080] consistency of of medical knowledge in
[1082] this example, right? But for rag when
[1084] you look at knowledge graphs for rag
[1086] it's like well the paradigm is a little
[1087] bit different because rag in this
[1090] instance at the current iteration of rag
[1092] is just answering a point question in
[1094] time and it's really just rag is what's
[1097] the gap between what does the LLM know
[1099] what does the LLM think it knows what do
[1101] I want it to say specifically right so
[1105] graphs have become this very accessible
[1108] thing to augment rack because everyone
[1110] can see them and be like this is what
[1113] the LLM should do. However, that's not
[1116] necessarily the case when you go through
[1118] the RAG process.
[1121] LLM's happened in RAG. Uh I'm not sure
[1126] about all of you in the room, but at
[1127] least for me, that was a significant
[1129] moment. And I'm referring specifically
[1131] to GPT2. I guess would have been the
[1134] first one where we had an academic
[1135] license when that was released. GBT2 was
[1137] a fascinating moment in time where
[1138] people like all of a sudden we can't
[1140] release this model and its weights
[1142] because they're going to make news
[1144] articles and that's a problem and that
[1147] has now been blown past completely. Now
[1149] you can argue that the majority of news
[1150] articles are using this generative stuff
[1153] but LLM significantly changed it for me
[1155] for the main reason that was in GPT2 now
[1158] I can do extraction
[1160] and you're probably similar in that with
[1162] GPT2 now GBT3 GBT4 any sort of LLM you
[1166] want to use
[1168] the extraction process of unstructured
[1171] text into structured graph that I can
[1174] ask questions of with the ontology or
[1176] with the alignment that I what is now
[1179] able to be done end to end because of
[1182] LLM at least in our case. I'm not sure
[1184] if people in the room have a similar
[1186] situation but LLM's kind of quite
[1188] significantly changed it.
[1192] I was pretty impressed when I first used
[1194] GPT3 to make a full AL file. I didn't
[1198] necessarily expect that would be able to
[1200] be able to do it so effectively, so
[1202] efficiently. It was really close. Um but
[1205] it was never perfectly usable. I think
[1207] was the problem.
[1209] But when I worked in graphs for a long
[1211] time, part of the difficulty was getting
[1213] started. And I do think that LLMs made
[1216] it very easy to get started. What they
[1218] did also do is brought many more people
[1220] to the graph community because all of a
[1223] sudden this esoteric language that you
[1225] previously couldn't touch now you can
[1227] create, right? And we have the developer
[1230] of founder of shackle here at this
[1232] conference and and it's a phenomenal
[1234] language but the phenomenal constraint
[1236] but the now you can people can just
[1239] write a medium post about hey I made a
[1242] graph and it's in cipher and I like I
[1244] made I made the whole thing I've never
[1245] done graphs I just asked an LLM to make
[1247] a graph and now I made a graph right and
[1250] they're like this is really cool it's
[1251] almost there it's just missing this one
[1252] piece and I think people think with LLMs
[1255] that it's there's a linearity to improve
[1258] but really when it comes to rag and it
[1259] comes to LLMs, you're at the end really
[1262] and there isn't necessarily improvement.
[1264] There's actually a risk of going
[1265] backwards which I think people don't
[1266] necessarily appreciate. So LLM did is
[1268] bring everyone into making graphs
[1271] because everyone can look at a graph and
[1274] be like that's easier to understand than
[1275] my relational database. So now I know
[1278] what my data is doing. Why isn't it
[1280] working? Is a question that we get a
[1282] lot. Uh so we didn't have to do
[1285] extraction anymore, right? And so I went
[1287] from being like now I have to tell
[1288] Spacey exactly what to extract
[1292] uh and instead I can just prompt an LLM.
[1296] I can write in English, hey there are
[1299] people in this bit of text, get the
[1301] people out and give them a tag person
[1303] and now I have a a graph, right?
[1307] But this isn't really the case. I don't
[1309] know if people have done this. When I
[1310] first tried to do this, I was like
[1312] fantastic. This is going to work really
[1314] well. I can just ask it and it's going
[1316] to make me a graph. And that's not
[1318] necessarily the case when it comes to
[1320] this level of extraction.
[1323] Um,
[1325] have people tried this? I'm sure people
[1327] in this room have done this, right? Like
[1328] as soon as GPT Chad GPT came out, it's
[1330] like make me a graph and then you had a
[1332] cipher statement and then you pasted it
[1334] and it didn't quite work. Okay, I'll try
[1335] and change it a little bit. And then
[1337] you're like, well, it's a property
[1338] graph, so it's maybe it's name instead
[1339] of text. then you have to change this
[1340] around and all of a sudden you realize
[1342] that while it's getting really close,
[1344] not necessarily making you the graph
[1346] that you want.
[1349] So LLMs can do extraction,
[1352] but can they do extraction to the point
[1355] of some of the graphs I've already seen
[1356] presented today? No. They can bring many
[1359] more people into the idea that I can
[1361] extract structured representation from
[1363] my text. They can't necessarily make
[1366] perfect structured consistently
[1368] opinionated reliable extraction from my
[1374] rag. I've talked about it a lot, but
[1377] this is the stuff that we work on a lot.
[1379] And rag is broadly
[1381] just there's an LLM. It's trained on a
[1384] bunch of stuff. I'm sure everyone knows
[1385] this, but just in case for people
[1387] listening, rag as we see it. And we as a
[1390] company work with people doing rag all
[1391] the time and we have entirely inbound
[1393] from people whose rag doesn't work. So
[1394] we get to see a lot of these reasons.
[1396] But rag is uh the LLM that I'm using
[1401] doesn't know what I want it to.
[1404] So I'm going to give it the extra
[1407] information. Uh and this is where the
[1410] concept of fshoting comes up. I mean
[1411] fshoting has been around for ages in
[1413] terms of giving examples to a model. But
[1415] you can think about prompting as a
[1417] natural language way a few shot if you
[1418] want. And so separate or chunk my
[1421] documents into sections, right? So
[1423] whatever document you have, separate it,
[1425] right? And the separation is largely
[1427] because I have to embed them, right? And
[1429] embedding models
[1432] are a really
[1434] important and I think broadly
[1436] underexplored, undertalked about area of
[1438] where rag is, right? And so you can just
[1441] open AAI provides embedding models.
[1442] There's plenty of brilliant places that
[1444] provide embedding models, but the reason
[1445] you chunk it is that if you want to
[1447] embed or you know model your data, it
[1450] just has to be a bit smaller because
[1452] you're limited by the provider. But so
[1453] really you want to split it up. You want
[1455] to set all of your documents into
[1457] basically paragraphs and you want to put
[1459] those paragraphs somewhere, but you want
[1461] them to be embedded through a model,
[1463] right? So when I get the information
[1466] back, it's the most similar to my
[1468] question. So when I say query the vector
[1471] store right that's because I'm sure you
[1473] all know and so you you know embed it
[1475] turn into numbers put it somewhere and
[1477] then the metadata is the raw text that
[1479] you have and then you bring that back
[1480] you you query the vector store by just
[1483] writing a question and then seeing how
[1485] similar that is to one of the chunks or
[1487] many of the chunks then you get those
[1489] back and then you basically just give
[1490] those chunks to an LLM in some way. Then
[1493] LLMs are really, you say, really good at
[1496] two things being translation and
[1498] summary. It's not necessarily language
[1500] translation. It can also be code
[1501] translation, but any sort of translating
[1504] concepts and summary. So if you give an
[1506] LLM a bunch of text, it will summarize
[1509] it really well and it can summarize in
[1511] the context of this. So what you do is
[1513] write a prompt and say, "Here's my
[1514] question. Here's all the context related
[1516] to that question. Answer my question."
[1518] And that's an LLM doing summary. And
[1519] that's great. So this is basic rag. Now,
[1522] these terms are emergent. So, I'm sure
[1524] in a couple years basic rag's going to
[1525] not even be a thing or rag might not
[1527] even be a thing. You can argue that
[1528] information retrieval was already around
[1529] and people have co-opted this as a term.
[1531] But this is what people are talking
[1533] about when they say rag. And rags become
[1535] really popular, I believe, because of
[1537] its accessibility because everyone's
[1540] like chat GBT is great, but it can't
[1542] answer the question that I want. It can
[1543] tell me how to bake a cake or I can plan
[1545] a holiday with it. But if I have a
[1547] question about what I'm working on, I
[1549] need to give it something. Then
[1551] obviously chat GBT's interface allows
[1552] you to update documents. They have a rag
[1554] process in the background. But broadly
[1556] this is it right
[1559] here is where we see it failing most
[1560] often. And I'll go through these in a
[1564] bit of detail.
[1566] So
[1568] the size of the chunk and where you
[1569] split can determine how good the tree
[1571] looks. So how you chunk is really
[1575] important because then that determines
[1578] what is embedded, right? So where you
[1583] split your document, for example, if you
[1585] have like a breaking page or like if you
[1587] just split by 512 characters, which is a
[1589] really common way to split, right? You
[1591] just loop through and split your
[1592] document in pieces, you could go across
[1596] a chapter. You could go from the
[1598] conclusion to the appendence. Like you
[1600] could be bringing in information that's
[1602] not relevant. You could go through
[1603] definitions that don't matter. You could
[1605] split at the wrong point. So making sure
[1608] you have an intelligent level of
[1609] splitting. And then the size of the
[1612] chunks need to be big enough to maintain
[1613] your context but small enough to also be
[1617] giving the specific context is a really
[1620] difficult problem. And this isn't like a
[1622] solved problem by any means. There are
[1624] plenty of methods to do this but this
[1625] becomes a level of granularity which is
[1628] like what is my document? what are the
[1630] documents that I have? Can I
[1631] automatically just rip through these and
[1633] build it? How can I make sure that when
[1636] I chunk it's the right chunk that I want
[1638] to bring in? And the answer is you
[1639] can't. And the benefit of LLM is you can
[1642] test, but this is an an enormous
[1643] problem. People don't necessarily go
[1645] there. I mean data in data out is a way
[1646] to look at this, right? So if you have
[1650] this is not to mention, I'm just talking
[1651] about raw text. If you have anything
[1653] multimodal, if you're trying to get into
[1654] a table, if you're trying to get into
[1655] like a spreadsheet, where you chunk is
[1658] if you just, you know, remove the
[1660] structure now, you don't have any text
[1661] anymore.
[1662] So, what you give to the LLM is really
[1665] important, right? And this is just a
[1667] case of if I want to ask a question like
[1670] who are Jerry's friends, right, in that
[1672] Seinfeld example, and I've chunked
[1676] this script, like how does it answer
[1679] that, right? the LLM might know already.
[1682] So, you can kind of get away with it.
[1684] And a lot of rag systems, like we've
[1685] worked with some legal clients who have
[1687] built this like rag system that like we
[1690] have 400,000 legal documents and chat,
[1694] you know, GPT4 is amazing at solving 85%
[1697] of these cases. We just have a few edge
[1698] cases.
[1700] And it's like, you don't have edge
[1701] cases. GPT4 is just really good at
[1704] answering questions around this specific
[1705] legal term, right? You're actually
[1707] giving it the wrong chunks. It's just
[1709] you're getting away with it because this
[1710] is quite an intelligent lol. So you
[1712] haven't actually improved it. You've
[1714] just, you know, you basically just asked
[1716] GBT4 a question. It's ignored the chunks
[1718] you've given and then it's answered,
[1720] right? So you don't have any way to
[1722] linearly improve. If anything, you're
[1724] going backwards. And so then how well
[1726] does the embedding model align and how
[1728] easy is it to get the right chunk is
[1729] again like I'm saying massively
[1730] underexplored. I I did my PhD in graph
[1733] embeddings and the embedding a graph is
[1736] is a really interesting way. When we
[1737] look at embeddings now, it's really um I
[1741] mean it started with no deve word devec
[1743] stuff and and and that's a lot of what
[1745] I'll look at. But the embedding models
[1747] are publicly accessible. I think
[1748] companies like Voyage are doing amazing
[1750] work when it comes to domain specific
[1752] embeddings. But
[1755] if you if you can split if you can split
[1758] accurately right your document and then
[1761] you can pass it through an embedding
[1762] model then that's going to determine how
[1765] good your retrieval is because it's just
[1766] mapping embedding models to embedding
[1768] right and so to give an example about a
[1771] problem that we currently have at our
[1772] company we have an enormous legal
[1774] document and they have a definition
[1776] called vehicular capacity right and so
[1778] vehicular capacity is assumed by the
[1780] model and assumed by us to be how many
[1782] people can fit in car, right? Vehicular
[1784] capacity is defined in the document as
[1786] how many cars fit on the road, which is
[1788] like quite confusing when it comes to
[1790] this process, but you don't necessarily
[1791] have a way. So, if the embedding model,
[1794] you know, had a bunch of examples about
[1796] vehicles in cars, sorry, so vehicles in
[1799] roads, now you have a level of tweaking,
[1802] right? So, you can see how you can
[1803] improve it. You can also see how if
[1805] you're trying to solve a specific
[1806] problem for your company in your domain
[1809] that a generalized embedding model
[1811] doesn't necessarily do it. And a
[1812] generalized embedding model again show
[1814] you how to bake a cake can get you
[1816] pretty close. But the embedding model
[1818] and how you split is largely going to
[1819] determine what it is you get back.
[1823] Further to this,
[1825] we worked with a travel client and this
[1827] was they had custom travel itiner.
[1832] So we we had a custom embedding model.
[1834] We we we chunked it properly by because
[1837] it was YAML. So it was structured. Even
[1839] then we would get questions like and so
[1842] this was it was it was custom wellness
[1844] travel and so people could just type in
[1845] what they vaguely would like to do. So
[1848] the the question was like people would
[1850] be like I want to go to a European
[1851] beach, right? So that is a short kind of
[1854] curt statement matching that to a chunk
[1857] and these chunks could have a lot of
[1858] context. It's close enough. It's it's
[1860] point but it's not keyword matching.
[1862] It's matching on embeddings. It's
[1863] matching on semantic similarities. So
[1865] European beach is good but there's very
[1866] little information. And then the other
[1868] end of the spectrum would be people
[1869] saying work's been really tough lately.
[1871] Uh like I'm thinking of getting away.
[1872] I'm not exactly sure where to go. So how
[1874] do you take those two separate you know
[1876] ends of the spectrum and that that's
[1878] assuming people ask the right thing and
[1880] they don't type the wrong thing in. So
[1882] how do you take those varied questions
[1885] embed them with a model that handles all
[1886] of them and then retrieve the right size
[1888] of you can see how this tears and there
[1891] are different ways to point improve it
[1894] and then this gets to context poisoning
[1895] which I think is particularly relevant
[1897] for knowledge graphs and rag and it's
[1898] it's relatively new as a term and I
[1900] haven't seen it talked about a whole lot
[1902] but if I have a top k of 10 uh so uh
[1907] what will happen is when you retrieve
[1908] from a vector store you can set how many
[1911] chunks you want back, right? And that
[1913] can that's a variable that you can pass
[1914] through and and it matters. But let's
[1916] say I have a large legal document. I use
[1919] legal documents a lot, but I think it's
[1920] particularly pervasive in this, but
[1921] maybe anything regulatory, right? I have
[1923] a large regulatory document. There is a
[1925] lot of boiler plate in this document,
[1927] right? We have a 100 documents. A lot of
[1929] the words are just repeating. I don't
[1931] necessarily want to chunk everything,
[1932] but if I set a top K of 10 and I correct
[1936] if I can correctly match my query and
[1939] then I can correctly embed and I've
[1940] correctly chunk based on semantic
[1943] similarity at a high level. If I ask a
[1945] question like you know of the LPS in
[1948] this fund uh who has the best fees,
[1950] right?
[1953] How it can get back three of the chunks
[1956] that have the information, right? like
[1958] it can it can often LLM can often get
[1960] back the right information. But if I set
[1962] a top 10, I just got back seven chunks
[1965] that now are not relevant. So I've
[1967] gotten back seven bits of information
[1969] versus three. Significantly more of the
[1971] information I returned is is incorrect
[1974] and potentially confounding in a really
[1976] important way because LLMs are not
[1979] apologetic or they're not uh
[1982] contemplative. They are necessarily
[1985] confident.
[1986] So if I context poison that is me
[1989] fshotting my model wrong. So when it
[1993] comes to rag I think people are like
[1994] cool I've got a baseline LLM and I'm
[1997] just going to add to it and it's going
[1998] to be better. It's like you're actually
[1999] at risk of making your LLM significantly
[2002] worse. Like in the legal example I
[2003] talked about before with the the you
[2005] know plenty of law law codes and GBT4
[2007] could answer the question. If it can't
[2010] answer the question it's going to use
[2011] the context it's given. And if you give
[2013] it the wrong context, which you abs if
[2014] you look at the someone's asking a vague
[2017] question that you have to embed using a
[2018] model you don't necessarily understand
[2020] or control and then you've just broadly
[2021] split your document up into sections.
[2023] It's like you can absolutely get back
[2024] the wrong getting back the right
[2026] information is not even guaranteed. I
[2028] think a lot of people get away with it.
[2031] And then finally, the model and the LLM
[2032] don't know what you mean, right? So to
[2035] use that travel example before um that
[2038] was a chat conversation where people
[2039] could say I want to go to European beach
[2041] and then people would say things like ah
[2043] I want to go somewhere warmer right as a
[2045] as an interactive process. So does
[2047] warmer mean
[2049] a warmer country like Thailand or does
[2051] warmer mean like if you say I want to go
[2053] to a beach in August does warmer mean
[2055] Europe? Does warmer mean Indonesia? Does
[2057] what does warmer mean in this context?
[2058] Right? And that depends on the embedding
[2060] model and what you've embedded. But does
[2062] it even know what you're asking for? If
[2063] I ask for vehicular capacity, what is
[2065] the vehicular capacity of this? Is it
[2067] going to say two because that's how many
[2070] cars can fit on this road? And am I
[2072] going to interpret that as only two
[2073] people can fit in these cars? So the
[2077] basic rag can fail in a lot of different
[2079] ways.
[2080] This is a quote from um Andre Kapathy
[2083] who's phenomenal in the space.
[2085] Everyone's probably uh come across him,
[2087] but this is part of a much larger tweet
[2088] which I'd recommend from December 2023.
[2090] But to to broadly summarize, he says
[2094] LLM's like LLM's only hallucinate,
[2097] right? So an LLM is a generative model
[2100] trying to make things up, right? And
[2103] we're happy with the hallucination until
[2105] we're not, I think, is a good point.
[2107] When we first started this business, we
[2108] heard a lot of people talking about edge
[2109] cases in rag. And an edge case implies
[2112] that this thing is deterministic and it
[2114] just fails at a particular area. But no,
[2116] it's all of these LLMs are generative.
[2118] That is something to to celebrate. But I
[2121] I think the important thing here is the
[2122] LLM assistant has a hallucination
[2124] problem. Because once you try and use
[2126] this generative model to solve your
[2128] problem,
[2130] now you're getting to the point where
[2132] it's like, well, there's a difference
[2133] here. This generative model that only
[2135] hallucinates. And maybe we're not as
[2138] smart as we think we are, but those
[2139] hallucinations seem to get really close
[2140] to what we do. But there comes a point
[2145] where you can't stop all of the
[2147] different hallucinations. And so if you
[2149] want to talk about edge cases
[2152] difficult
[2155] so this is how to improve rag that we
[2157] work on right and there are so many
[2160] different ways because rag as we like to
[2162] think about is a process. the system,
[2166] right? This is a a modular process of
[2169] retrieval potentially passed through
[2170] many agents, potentially conditional.
[2173] So, there are so many ways to do
[2177] rag, right? And there's so many ways to
[2180] improve it. Um, llama index has really
[2183] great series on advance, right? Now,
[2184] every almost everyone who writes a
[2186] medium post has written how to improve
[2187] rag at some point who's worked in the
[2188] space, right? So I I' I'd hesitate to
[2190] look at all of those over and over and
[2192] over and over again. But I I do think
[2193] Llam index and particularly Lauradlar
[2195] index has some really good stuff around
[2196] advanced rag. They have infographics you
[2198] can easily share. They have points of
[2199] improvement. The important thing to
[2201] notice about that is that so many of
[2203] them are not how do you improve rag.
[2204] It's like step one. It's like no there's
[2206] this enormous kind of spiderweb of
[2209] different processes depending on your
[2210] problem because again this is
[2212] information retrieval and it's broadly
[2213] applicable to everyone. Everyone's
[2214] trying to solve different problems with
[2215] the same technology. So if if you if you
[2217] do want to know and you're more
[2218] interested, there's that. But one of one
[2220] of the ways is graphs. The way that we
[2223] broadly solve it is graphs. And so I'll
[2225] speak about graphs
[2227] specifically. Um
[2231] also advanced drag and basic grab is
[2233] kind of like shallow learning and deep
[2234] learning, right? There isn't necessarily
[2235] a distinction between these things. And
[2237] I think that the process is evolving. So
[2239] I hesitate to say advanced and basic and
[2242] again because the lines blur and it's
[2244] never really sure. But I I think these
[2245] are the terms that are broadly used
[2247] online. So if you are at this point
[2250] where you're like I I would like to know
[2251] about how my rag works. I'm interested
[2253] in graphs and others. There's prompt
[2255] improvement and there's reanking and
[2257] there's just this phenomenal stretch but
[2259] I would look at but I'll specifically
[2260] talk about graphs. This is broadly our
[2264] point, right? And and I think if we're
[2266] looking at within the context of there
[2268] are some companies here who have
[2269] phenomenal like really capable, really
[2271] intelligent, really well-reasoned,
[2273] really wellrescribed knowledge graphs,
[2275] that is not necessarily what people in
[2277] rag right now do. Again, if you read all
[2278] the Medium posts, someone just kind of
[2280] like tossed a document in and made a
[2282] vague graph and they're like, "Look at
[2283] this picture. That's crazy." Because
[2284] everyone can see graphs, right? And one
[2287] of the people we work with, a friend of
[2288] mine from my research group was like,
[2290] "The problem with knowledge graphs in
[2293] Rag is that everyone can look at a graph
[2297] and see it and be like, wrong, you're
[2299] trying to describe a representation of
[2301] language that you're telling an
[2302] artificial intelligent agent what to do,
[2304] right? So you're really being like, how
[2306] do we build the brain of this thing?"
[2308] And that is a very difficult question to
[2310] answer, but it's very simple to
[2312] critique.
[2313] So
[2315] this is broadly the question and and I
[2317] think this at a high level this is a
[2319] good answer
[2321] because
[2323] uh when we look at the issues that we
[2324] had with rag before
[2327] there's a there's a paper that came out
[2328] recently I can't remember the exact
[2329] research group I'd recommend reading it
[2331] which is around structured grounding and
[2333] so structured grounding is um
[2337] to give an example of a client we work
[2339] with it's a veterary radiology group and
[2342] They very interesting things around
[2345] veterary radiology in that uh animals
[2347] don't sit still. So you can't build a
[2349] good test set for vision. So there's
[2351] just like this very broad you know
[2353] pictures. So then radiologists get these
[2354] pictures of an animal and they're like
[2356] this is a 5-year-old Labrador. It's got
[2358] an abdomen problem. I'm going to type in
[2361] these things to chat GBT and get it back
[2363] and it hallucinates like you wouldn't
[2364] believe
[2366] because
[2369] because it's searching semantic
[2371] similarity the latent space is unbounded
[2374] uh and the best hallucination I've se
[2379] hallucination I've seen is that uh there
[2381] was a developer working in TensorFlow
[2384] building machine learning systems and
[2386] there is an optimizer within TensorFlow
[2388] probably called Adam but ADAM stands for
[2390] something and then the the co-pilot
[2393] GPT4. So a very capable model
[2396] hallucinated Adam as John.
[2399] So it got an error that said John is not
[2401] part of the Tensflow package. It's not
[2402] an optimizer in this phrase. But I think
[2405] that's funny on the surface and
[2406] terrifying in reality because it's like
[2407] well now the space of what you're
[2409] searching is entirely unbounded. Right?
[2412] I think an un an undertalked about or or
[2415] less talked about method of
[2416] hallucination is mean reversion in that
[2419] we work with a codegen client working in
[2422] solidity being the language that's in
[2424] Ethereum and that's what Ethereum writes
[2426] their contracts with this language
[2427] called solidity it's based on JavaScript
[2430] right heavily based on JavaScript and
[2432] there are significantly more JavaScript
[2433] examples online than there are Solidity
[2436] and so a lot of the hallucinations are
[2438] actually going back to JavaScript so
[2440] it's not making something up randomly
[2441] it's reverting back to the mean which is
[2442] this context and so again if you had a
[2445] developer a solidity developer they know
[2447] that they're only working within
[2448] solidity right so when it comes to the
[2450] veterary radiology example uh it
[2452] hallucinates conditions for these
[2454] animals if you gave it to uh an intern
[2457] or a research assistant they would know
[2460] that the disease that it's associated
[2462] with a Labrador only applies to bulldogs
[2466] right but you can't necessarily limit
[2467] that when it comes to LLMs or rank again
[2470] you just gave it text You gave it an
[2472] embedding model. You asked it a question
[2474] and if it can't answer, it tries to
[2475] figure it out and it doesn't figure it
[2476] out in the right direction necessarily.
[2478] It can figure it out in any direction
[2480] entirely unbounded latency. So, and I'll
[2482] tell you that the accuracy of this level
[2484] of granularity of veterary radiology
[2486] using GPT4 is about 20%. And this is not
[2488] to say GPT4 is not a good model. It is.
[2490] It's fantastic and I use it every day.
[2492] But when it comes to some levels of
[2493] granularity, it doesn't necessarily
[2495] answer the way you want. The structured
[2496] grounding is a really important part of
[2499] knowledge graphs in graph because now we
[2501] can represent this is a dog, it's a
[2505] large dog, it's a Labrador and it has
[2507] these diseases.
[2509] So you've bounded the search space and
[2512] that structured grounding is really
[2513] important. If you have an existing
[2514] knowledge graph or you're willing to put
[2516] in the effort to build one or you can
[2518] use some of the technologies to build a
[2520] fewer, however you want to do it,
[2521] structured grounding of your answer is
[2523] really important and really useful when
[2525] it comes to rag because you are trying
[2527] to answer a specific question over and
[2530] over and over again. You're not trying
[2531] to answer all of your questions almost
[2533] and I think that's a difficulty when it
[2534] comes to this process. Completeness of
[2536] answer is really relevant. Again, if I
[2539] have the Seinfeld and I say, "Who are
[2541] Jerry's friends?" Um, in the process I
[2544] described before, this is counting,
[2546] right? And so, if you want to do
[2547] counting, you shouldn't really use
[2548] vector databases. They're very aware of
[2550] this. If you want to count like in in
[2551] the travel example, how many of the
[2553] tours are in Mexico is not necessarily a
[2555] good question for for rack, right?
[2557] Because I've chunked up the tours, so
[2558] maybe they're in like three or four
[2559] parts. And so, and let's say there's
[2562] 100, I've got 400 chunks of like it's
[2564] not going to count them necessarily. So
[2565] that's a that's where relational
[2567] databases are useful or graph databases
[2569] are useful. But if you want to do
[2571] qualitative counting if that if there's
[2574] such a thing exists how how many who are
[2577] Jerry's friends, right?
[2580] The rag process doesn't necessarily give
[2582] you back like you'd have to get back
[2584] every chunk that mentioned friend with
[2587] different people and the LLM would have
[2589] to take all that information and
[2590] condense it. And I think an LLM with
[2592] that instruction with a question simple
[2594] enough as who are Jerry's friends can
[2595] probably do it assuming you get back the
[2597] right chunks and you don't confound it
[2598] and you don't mention someone else in a
[2600] graph like I had before.
[2604] Let me jump back to it.
[2608] If I go to Jerry
[2610] like and again because I've got the
[2612] chunks here I'm just going to remove
[2614] these chunks so we can see it a little
[2615] better. Again the chunks are really
[2617] important. Um, but this is a case of I I
[2619] spoke to someone once who was like
[2621] graphs should never have more than 10
[2622] nodes because I can't see them. And I
[2625] think there's some validity to that sort
[2627] of statement.
[2629] Um, if we go in and say Jerry
[2633] and so we have friends with, right? So I
[2635] can just go
[2638] uh I guess we have accounts
[2641] um wrap
[2647] I'm have to wrap this string. Actually,
[2649] I probably shouldn't mess around with
[2650] this too much.
[2652] This is going to break. So, stringify,
[2658] right? So, now this is the type of
[2660] that's a pretty simple query, right? And
[2662] there are problems with query generation
[2663] for natural language. I'm sure you've
[2665] bumped into. But now I have a complete
[2667] answer. This is an awful network and you
[2670] can see there's some uppercase and lower
[2671] case. Whatever. We fix that by just dot
[2673] lowercasing all the text we have. on the
[2674] point. The point is that this is a
[2678] complete answer now in a way that will
[2680] be difficult to recreate with rack. So
[2685] relatively simple query you get it back
[2687] as a table if you want. And the benefit
[2689] of what we've done here with the schemas
[2691] is like we pass those schemas into I
[2694] generally try to use LLM only if I have
[2697] to. I think LLMs are a fantastic very
[2699] interesting prototypical tool. our back
[2701] end basically doesn't use them um
[2703] because it uses them for some level of
[2705] querying I think generation code but you
[2707] can see that if I ask this question to a
[2710] vector system and maybe people have
[2712] different opinions but this is something
[2713] that we've seen a lot which is like
[2715] completeness of answer
[2718] multihop retrieval is harder but anyone
[2721] who works in graphs would know that
[2722] multihop retrieval is really relevant
[2724] right which is like if this happens and
[2726] this happens then get this back or like
[2728] I think the canonical example that we
[2730] had in literature was like, "Where does
[2732] Barack Obama's wife live?" And it's
[2733] like, "Well, I don't necessarily have
[2735] that fact. I have an open world
[2736] assumption though, so I don't
[2737] necessarily know." So, it's like, "I'm
[2739] going to retrieve that information."
[2741] When it comes to rag, multihop retrieval
[2744] is really useful because LLMs should be
[2749] doing translation summary right now. Um,
[2751] you can prototype and test and explore
[2753] with them doing reasoning if you would
[2756] like to or planning, right? But really,
[2758] if you want to get a level of
[2760] reliability, you can't. If you want to
[2762] put a product out there that people can
[2763] see, you cannot rely on an LLM. You're
[2766] more than welcome to, but again, you'll
[2767] get an edge case, and then that edge
[2769] case you can't fix, and then all of a
[2770] sudden there's no reliability in your
[2772] product. I built a large rag system,
[2774] didn't have a graph in it for a uh oil,
[2777] large oil and gas company as a
[2778] contractor, and it was a just a leave
[2781] policy,
[2782] right? So, you could be like, well, how
[2784] many weeks do I get for paternity leave?
[2786] and it hallucinated a little bit and
[2789] then everyone in the company was like a
[2790] this sucks and they never used it.
[2792] Right? So like when it comes to that
[2794] level of reliability, multihot retrieval
[2796] is important. Most questions that are
[2799] useful aren't who are Jerry's friends?
[2802] It's of Jerry's friends who are balding,
[2807] how many of them have a job right now?
[2809] Like that is the type of structured
[2811] question that you want to use, right?
[2812] that has some temporal process
[2814] potentially spatial temporal but it has
[2816] a level of conditional hop and I don't
[2818] want to get an LLM to do that but if my
[2821] graph has that information in it my
[2823] graph is specific the relations are
[2825] there there's a level of path that I can
[2827] follow if I give the LLM that it can
[2830] answer my question right so multihop
[2833] retrieval is really really useful part
[2835] of the difficulties people in this room
[2836] may have seen is that getting that
[2838] multihop retrieval from natural language
[2840] is really difficult because the the
[2842] queries that you want to create if you
[2843] want to generate a query it's difficult.
[2845] Yes. So questions
[2851] right and that's what you're talking
[2853] about. But my question is right we can
[2856] use because we extracted we can use to
[2859] answer the question or we can use a
[2862] chunk and then ask
[2864] question or we do both. Yeah.
[2869] Because you know I did both I never did
[2872] together. So multi is right strategy
[2875] because you I'm ontology right so if I
[2878] have a question I don't have it in blood
[2880] right so then my only option will be a
[2882] chunk
[2884] or ask because I extracted I have
[2890] yeah if you are bound to a consistent
[2892] uppertology I think that's really good
[2893] right especially if you've done the work
[2896] to build that graph out consistently and
[2898] that's a difficult amount of work but
[2899] once done it's useful so I think your
[2901] point is like how do I use the
[2903] information if I ask it a question. Is
[2904] that right? So you can return back the
[2906] triples which is a complete answer. Um,
[2910] but that's like I had an example where I
[2914] worked with the first book of Harry
[2915] Potter and I'm not sure how familiar
[2916] everyone is, but it's like you can ask a
[2919] if if you ask a question in the rag
[2921] process that I described before. Um, who
[2924] sacrificed themselves for Harry, right?
[2926] So, if you chunk it, you have to hope
[2928] that that's like a you need to get
[2930] completeness of answers. So, it's like I
[2931] got to get back everything that refers
[2932] to sacrifice. There's a bunch of
[2933] references to sacrifice, but didn't
[2935] necessarily get back that answer. So the
[2936] answers are broadly uh so then if I ask
[2939] a graph and I have this aligned to
[2940] operontology which is person and
[2942] condition and however it was you would
[2944] get back the answers Ron Weasley and
[2946] Lily Potter. So his friend and his mom,
[2949] right? You just get those answers back
[2950] as a triple, right? That that's the the
[2953] triple that you get back. That's not
[2955] particularly useful to an LLM. In some
[2957] cases, it is, but the difficulty there
[2959] is I've given it accurate and complete
[2961] highlevel context. And accurate and
[2964] complete highle context doesn't
[2966] necessarily let it make the decision. So
[2968] you're between two things, right? So
[2970] part of the reason why I showed the
[2971] chunk linking before is that what we we
[2973] have as a product is like, well, also
[2975] give it back. So if you return Lily
[2978] right and Ron also return back the
[2982] chunks that that information was
[2984] extracted from. So then you get an
[2986] answer like Ron Weasley sacrificed
[2988] himself in the chess battle and then
[2990] many years prior Lily Potter sacrificed
[2993] herself for her son in that process. So
[2995] I think you're right if if you're you're
[2997] aligned you kind of want to have it um
[3000] if you just give it that simple context
[3001] is not enough. If you just give it the
[3003] chunk it can be too much. I think the
[3005] answer and what we're working on is to
[3007] get an LLM generated summary. So every
[3009] graph basically has a property that
[3010] property is a description or summary and
[3012] that summary is LLM generated. But if
[3013] you generate that through a rag process
[3015] then now you have each node with a
[3017] particular level of description kind of
[3018] fits in the middle. Uh so that that I
[3020] think is probably the best. So you can
[3021] be aligned to operontology
[3024] uh and you can get back the right
[3025] answers. That's really just a matter of
[3026] scoping in and making sure when you do
[3028] multihop retrieval you follow the right
[3030] process. Right? my experience with
[3031] alignment to operanttology and a lot of
[3033] that for context is I did a lot of work
[3035] in ISO standards in resources and that
[3037] was a specific way to follow like you
[3039] know failure codes and maintenance and
[3041] so that it wasn't necessarily the terms
[3043] it was really what the terms related to
[3045] that that was really important with the
[3046] graph so I think if you have enough
[3050] and you want to ask questions of it and
[3052] you have a structured query language
[3053] that you can do so I think getting back
[3055] the chunks is better than um not getting
[3059] back the chunks when it comes to high
[3061] level description but it does depend I
[3063] mean this is why rag is difficult
[3064] because also that's in combination with
[3066] a prompt you can write your own prompt
[3069] right and then it's also in combination
[3070] with maybe some other schema that you
[3072] add in and then that could be one system
[3074] in part of a multi- aent system but it's
[3076] difficult to answer but I will say that
[3078] if you get back the node and just the
[3081] chunks associated with that node so the
[3082] process is node then chunk I think you
[3085] have a really good chance at the answer
[3086] but I I use the word chance very
[3088] specifically there because if you have
[3091] an uppertology, you can
[3092] deterministically get back an answer.
[3094] I'm just not sure how useful that answer
[3095] would be.
[3097] And then finally, inferred answers. I
[3099] think there's a really big value for
[3100] graphs. I see people coming to graphs
[3103] now and they can see them, so they
[3105] really like them. And then they can be
[3106] like, oh, I heard graphs do inferences.
[3108] I heard that graphs can do consistency
[3109] checking. I heard there's anomaly
[3110] detection. I heard there's all these
[3111] valuable things around knowledge graphs
[3113] and what they are. And it's like, yeah,
[3115] that's a perfectly aimatically described
[3116] onlogically aligned graph that you've
[3118] built, right? that is not I made a
[3120] network X diagram and now this thing
[3122] looks cool. So inferred answers are a
[3124] really useful potentially again because
[3126] multihop retrieval and inferred answers
[3128] or or like inferred multihop retrieval
[3130] with something like near's optional
[3132] clause, right? This is a way to do
[3136] planning or to do reasoning with an LLM
[3139] without having to let the LLM do it. So
[3142] this is a really key part of I think the
[3145] future of graph rag if you want to say
[3147] graph rag. I'm still not fully on that
[3149] term, but that I think this is the key
[3152] part. If you have an existing ontology,
[3154] this can work really well.
[3156] This is broadly the benefit of of
[3158] augmenting. I have to rush through a
[3160] bit. Uh this is protege. If someone
[3162] hasn't used protege, it's awful and it's
[3164] fantastic at the same time. I had to
[3166] spend a lot of time with this. I tried
[3167] to find the wine ontology, the pizza
[3168] ontology. But broadly, if you have this,
[3171] right, which is again, it looks simple.
[3174] It's a it's a lofty goal I think to
[3176] create a graph like that if if you if
[3179] you have structured grounding you have
[3181] multihop retrieval you can infer an
[3184] answer again if it's protege it's
[3187] constrained you have different processes
[3189] to make sure that the answers right
[3190] everything in there is consistent now
[3193] you've given the LLM exactly what it
[3194] needs right if I go back to my point
[3197] here
[3199] it was somewhere here I said just like
[3202] LLMs can do What
[3206] this right this point what if we put our
[3209] data in a graph and the LM asked the
[3210] things that we asked the LM right that
[3212] would be great if that graph was really
[3213] good and this is a really I think good
[3216] goal to aim at and a difficult thing to
[3218] achieve it's better than just basic rag
[3221] but this is kind of process that we're
[3225] looking at if we look at graph rag right
[3227] and it doesn't apply to everything yeah
[3228] please question um I noticed using the
[3231] protege example when you're referring
[3233] referring to the benefit of graphs with
[3235] LLMs. Are you using ontology and graph
[3238] interchangeably? Sure, that's a good
[3239] question. Um, I'm using protege here as
[3242] an example and people may disagree, but
[3244] as like I guess the canonical knowledge
[3245] graph of like this is the most the best
[3247] the most complete, the most well
[3249] structured, the most aligned that you
[3251] can create uh as an example, right? But
[3254] when I talk about knowledge graph and I
[3255] think this is a really good point, I'm
[3256] not trying to define knowledge graph
[3258] because I don't have a definition and I
[3259] don't you may have a personal
[3261] definition. I think nej's definition I
[3262] think onto tech definition is actually
[3264] probably one of the best but the what is
[3266] a knowledge graph and what am I talking
[3268] about is a really good question and I
[3270] think the answer is because knowledge
[3272] graph is out in the wild and because
[3273] it's a really accessible concept and
[3275] everyone can see it and contribute I
[3276] think it's difficult to standardize that
[3278] definition I'm talking about here the
[3280] perfect would be something like this the
[3283] gaps here are how do I write a sparkle
[3287] query from a natural language if I want
[3290] to go to a European beach to get back
[3292] this perfect description and secondly
[3293] how do I build this graph in the first
[3295] place and how much work is that what if
[3296] my data changes and what if the rag
[3297] process doesn't work it's an emerging
[3299] process so it's a good question I use
[3301] this more as a demonstr demonstrative
[3303] example I would say most people aren't
[3305] using verte um I would say most people
[3308] are actually using uh database like nefj
[3312] or or kuzu in terms of how quickly it is
[3313] to get started because I think the
[3315] barrier to entry to something like this
[3316] is is huge
[3318] but this is this would be Good.
[3325] There's some downsides. So,
[3329] if you don't have a graph, Larry Voss
[3331] says this really well from LREX and he's
[3332] the dev advocate from LREex and he's
[3334] great. If you don't have a graph um and
[3338] you see people using them, well, I think
[3341] there is an idea that we should have
[3342] one, right? But making a graph is a
[3347] large undertaking.
[3349] drag isn't necessarily like revenue
[3351] generating. So the ROI of making this
[3356] right is hard to justify in a lot of
[3359] ways right in a business context. So I
[3362] think making a graph if you don't have
[3363] one is a pain. Um especially if you're
[3365] unfamiliar with the technology,
[3366] especially if you don't know how to
[3367] debug it. Any sort of like you could say
[3369] that like when LLM started doing because
[3370] the rag is probably the second most used
[3373] example of LLMs right now with the first
[3374] being code generation and I use code
[3376] generation a lot but if you look at how
[3379] much good software has been created
[3380] versus how much software has been
[3381] created, it's like there's there's way
[3383] more issues. There's a lot more
[3384] problems. So so making a graph from LLM
[3387] isn't necessarily easier. More people
[3389] can do it, but that doesn't necessarily
[3390] mean it's better.
[3392] Another question that you probably have
[3394] that I have as well is like LLM's pretty
[3395] good already and should get better is I
[3397] think an interesting point right but
[3399] let's say LLM's get more domain specific
[3401] or you use a domain specific LLM or use
[3403] some sort of fine tuned or transfer
[3404] learned LLM it's like what if it doesn't
[3408] do what I say what if the domain is
[3410] vehicular capacity and that's how many
[3411] people are in a vehicle and what if I
[3413] then have to like the benefit of the
[3414] high level ones that we have at the
[3416] moment is you can kind of quite easily
[3417] trick them so LLMs are pretty good
[3419] already and should get better is fine Um
[3421] I think it's really important to when
[3422] you think about graphs not see them as
[3424] replacing see them as augmenting and I
[3426] think that needs to be described in such
[3429] a way and represented in such a way that
[3430] LLMs every new release like GBT 5 is
[3433] always rumored to be coming out right
[3435] GBT 4.x X becomes five at some point
[3437] when there's a competitive advantage I
[3438] guess but as that is released will this
[3441] make graphs obsolete my answer is no but
[3444] will this make how we make graphs
[3445] obsolete and will this make us question
[3447] what does it mean what what does
[3449] semantics mean what is representation
[3451] yes so what is semantics is a really
[3454] interesting question because you know
[3455] aimatically if you're building in
[3457] protege
[3459] things like a concept net like an is or
[3461] a hazard become really important or a
[3463] child parent relationship become really
[3465] important Right. But if an LLM has most
[3468] of that context already and it's getting
[3469] more of it, then how important is the
[3471] semantics at that level? How important
[3473] is high level instruction? How important
[3474] is up fories? I think they're really
[3476] important, but I do think there's a
[3477] question that arises in terms of what
[3479] does it mean to use them. So
[3482] there turning natural language into a
[3484] query language I won't spend much time
[3485] on, but that's just a really difficult
[3486] problem. Um I think people expect it to
[3488] be solved immediately. It's difficult.
[3490] Uh Thomas Branick from nearj has a great
[3492] project which is like a community level
[3494] of like everyone please use examples and
[3496] build them and tag them and then we can
[3497] build up around text to cipher and I I'm
[3500] under the impression nearj building a
[3502] co-pilot around text to cipher and I
[3503] think that's all really useful and I use
[3504] a lot of cipher however this will always
[3506] be a problem right text to SQL isn't
[3508] solved there are more SQL examples
[3510] online than anyone's ever seen so if
[3512] that's not solved yet with the current
[3513] space it may be solved soon but that's a
[3515] limiter
[3516] consistent representation over domains
[3518] we have a motivating question that I
[3520] think about a lot which is like rice to
[3523] a farmer is different to rice to a chef
[3525] but the node rice is the same. So how do
[3528] you communicate that and how do those
[3530] people communicate and and what is the
[3532] what are two different modalities or two
[3533] different worldviews and how do people
[3534] come to conclusion?
[3536] So consistent representation over
[3538] domains is interesting especially as
[3539] domains update change and this field's
[3540] emerging
[3542] and then specificity of representation
[3544] I'll just go back to the veterary
[3545] radiology example. um if you're not at a
[3548] level of granularity that can answer the
[3550] question, the LLM is going to make it
[3551] up. And that's where hallucinations come
[3552] from because you basically guided into a
[3554] dark room and told it to figure its way
[3556] out. And it's like the getting to the
[3558] level of granularity or representation
[3560] is really important. This is why again
[3562] the questions around operontologies are
[3563] difficult because if you start out of
[3565] concept, you get all the way down to
[3566] veterary radiology, how many steps are
[3568] in the way and how long does that take
[3569] to build?
[3571] So these are some of the downsides. Now
[3572] I mean again I use them and I think
[3573] they're useful. Yes. The third point I
[3576] just want to make sure you're not saying
[3577] that the only way to do graph rack is to
[3580] be able to convert to query language. If
[3582] you are doing that then that's a hard
[3584] problem to solve. Yes. So I I'll talk
[3586] through this a little more. Yeah. So
[3588] there's there's multiple ways and
[3589] Andreas from NEFJ recently gave a talk
[3590] and he's fantastic. If you get a chance
[3592] to see him speak I highly recommend it.
[3593] But there's broadly three ways, right?
[3595] One is um someone like a NEFJ or anyone
[3598] you can vectorize a graph, right? So
[3600] then I can actually do the vector search
[3601] that I described before. There's the the
[3603] end case which is type in please query
[3606] my graph about people and systems and
[3607] then get me back like a multi-step
[3610] inferred yielded cipher query. That was
[3612] the end state, right? There's a middle
[3614] state which is what we do at Yhow a lot.
[3616] And basically this is I think a really
[3617] common system is vector it so I can then
[3620] kind of land on a node and then run a
[3622] preset cyber query that I pass variables
[3623] into. So that's like the main way that
[3625] people are going to do this stuff,
[3626] right? And so if you have an
[3627] understanding, I think the answer is
[3628] structured query language. Many
[3630] different structured query languages and
[3631] just know which one you run.
[3636] So I don't have to talk about what we're
[3637] doing. Um
[3642] yeah. Okay. So this is just I want to
[3644] talk about graphs specifically what the
[3645] features are that work for us. Again
[3647] they in this room we have a lot of
[3649] different graphs, a lot of different
[3650] people, people have been working on this
[3651] for a long time, a lot of different
[3652] domains. So I don't want to prescribe
[3654] graphs exactly as you said before.
[3655] graphs are different but how we use them
[3657] for rag with clients this is this is
[3658] what I want to go through
[3660] so and this is the point in its current
[3662] state the point of rag is to run
[3663] specific answers from vague questions I
[3665] think that's useful right the structure
[3666] grounding kind of closes that gap I
[3667] think you have to be this has to be
[3668] really important reliability is a buzz
[3671] word right now but reliability has been
[3672] a thing in grass for ages in terms of
[3674] determinism but
[3677] this is our man again it's going to work
[3679] for us not going to work for necessarily
[3681] everyone but you have to represent the
[3683] full scope of the question nothing
[3685] further or confounding per question,
[3688] right? Because if you have a question,
[3692] uh if if you're asking a rag system a
[3694] question, right, and I have I built a
[3696] graph really just kind of just build a
[3697] graph. It's a high level of granularity,
[3699] whatever. I'm letting the LLM make the
[3700] decision. You kind of you've structured
[3702] a little bit, but it's like you kind of
[3703] want to start bottom up because the
[3706] value of the system if you can answer
[3708] all of your questions almost, that isn't
[3710] useful. So you kind of have to start by
[3712] answering at least some of your
[3713] questions definitely and then expanding
[3715] from there. So in the veterary radiology
[3717] example, this is a veterary radiologist
[3719] who writes reports. They make money per
[3722] report. 40% of their reports are about
[3724] abdomen. So it's like I don't need to go
[3726] through the process of representing
[3728] specific brain injuries if I don't want
[3729] to. Like at the moment what I really
[3731] need is like this kind of like power law
[3733] representation of what I have. But you
[3735] need to be able to answer at least one
[3736] question then expand out from there. So
[3739] granularity is covered. scope of the
[3740] questions covered and then the
[3742] representation is aligned to how the
[3743] domain experts interact with the domain.
[3744] I showed you that schema before. Um
[3746] again you can fot it wrong if you want
[3748] to if it represents your domain. I think
[3749] the interesting thing at the moment is
[3751] personalization of workflows
[3754] which is what is vehicular capacity
[3757] right what does it mean to me to
[3759] vehicular capacity because that's really
[3761] important to my system. If it doesn't
[3762] know, then it's not going to know,
[3763] right? For the travel example,
[3766] wellness travel has different peak
[3768] months to travel. So, if I say what are
[3771] the peak months to GPT4, it's not
[3773] necessarily going to get that answer,
[3775] right? And that's that's not to say if
[3776] you have specific business processes
[3778] that are different and at a competitive
[3779] advantage, that's the same level. You
[3780] need to align it to what you want.
[3784] So, this is like a broad point which
[3787] right now I hope this changes, but this
[3789] is what we think about the moment,
[3790] right? Don't let the LLM think at all.
[3794] Um, give it a task and give it
[3796] everything it needs to solve that task.
[3798] Right? I I I like the saying that LLM
[3800] are not very intelligent. They're a
[3801] 5-year-old with a thousand years to
[3803] solve the problem, right? Or like models
[3806] generally. So, give give it and they're
[3808] getting smarter and smarter and smarter,
[3809] right? But like again, you a newborn
[3811] baby will cry if it doesn't see its
[3813] mother, right? So, it's like we have
[3814] these processes really quickly. So you
[3817] want to make sure that you give it all
[3820] the data, right? But if you give it too
[3822] much data, now it's thinking again.
[3823] You're like, well, that's not great,
[3824] right? If you don't give it specific
[3826] enough data, it's thinking again. I say,
[3827] don't do that. Give it the specific data
[3829] just that it wants and no more. And so
[3831] the difficult part of this is how do you
[3832] do it really broadly? And so this goes
[3835] back to my point of like why a graph's
[3836] so big when you make it. And this is for
[3839] red, right? Snowed needs to be as big as
[3840] it is. And that's exactly as it should
[3842] be. And that's perfect, right? The
[3843] graphs I worked at in large resource
[3845] companies need to be as big as they are
[3846] because they represent so much. And
[3847] Microsoft's graph rag, I think, shows
[3849] communities really well and it aligns
[3850] all of your data. And
[3853] this is part of the problem, right? And
[3855] this is rag specific.
[3859] I think people in the room may agree or
[3861] disagree with this, but in my
[3862] experience, um, there is a large upfront
[3865] cost to making a really big map. Uh, and
[3867] the ROI is uncertain.
[3870] Um the RMI may be defined in some places
[3872] but I've been part of many projects
[3874] which spend a lot of time
[3875] multi-disiplinary someone's on leave so
[3877] we can't quite get them in but once we
[3878] get them in that's okay and then we can
[3880] bring them in and someone disagrees in
[3881] the system in terms of that's changes
[3882] and now SAP is in German and we can't so
[3884] that you got to build this large system
[3886] out right but the ROI for quering a
[3888] graph in rag is unclear because rag
[3890] itself to be honest at the moment
[3891] doesn't necessarily have commercial
[3892] viability there are very few systems in
[3894] rag that are actually in practice right
[3896] some people are testing chatbots but
[3897] they're not necessarily making money
[3898] from
[3900] And then if you do have a graph then
[3902] it's like well the previous checklist
[3905] being like this
[3907] I think and I've built a lot of large
[3910] scale graphs that are in production at
[3911] some level specifically around
[3913] maintenance for meas and stuff
[3916] and
[3918] to represent the full scope of the
[3920] question is difficult when it comes to
[3924] kind of building these large like is the
[3927] graph that you have that you spent time
[3928] on it is useful for what it is. Is it
[3931] the right graph for rag? I think is a
[3932] really interesting question. I don't
[3934] think it's a onetoone swap. I don't
[3935] think you can just move your existing
[3937] graph that you've spent time
[3938] representing into rag necessarily and
[3941] make it work for those points that I
[3942] said.
[3944] So our solution or at least the way that
[3946] we're working, at least the way that we
[3947] dog food and we build for clients and
[3948] again we have tooling but we build these
[3950] systems for people
[3953] is make a small one like make Labrador
[3956] abdomen, right? solve the problem with
[3957] that and then make it as quickly as you
[3960] can like you saw before right I just
[3961] made a graph about as quickly as I did
[3962] and it's probably wrong right if you're
[3964] a Seinfeld expert you look at it you're
[3965] like that's wrong it's like cool change
[3966] the schema build it again right and then
[3968] it's in a name space right so if you
[3969] want to do the next sign episode build
[3971] another one or put them in the same name
[3972] space or build this graph and then talk
[3973] to so you need to do it again until you
[3976] solve your problem and you're going to
[3977] have many problems when it comes to rag
[3979] but this is why and again I know that
[3981] large graphs have value and I know that
[3982] we've spent time but I wanted to be
[3983] evocative to the point of like if it's
[3986] represent Right? And LLMs now know a lot
[3989] of stuff.
[3991] Then why do we need to give graphs
[3993] everything if LLM know? You're really
[3996] just trying to give it where the LLM
[3997] isn't there yet, right? Again, you don't
[3998] want to let the LLM think, but it does
[4000] know stuff. It can you can just
[4001] consistently give you back answers about
[4003] things. So when it starts to kind of
[4005] again lead it into a dark room and let
[4007] it get itself out is like a really bad
[4008] way to to do this process.
[4013] So this is just answering the same one
[4015] before which is questions and then
[4016] answers and then I I just kind of want
[4019] to say that this is how we solved it for
[4020] ourselves. We started to build this
[4021] example and then we realized that rag
[4023] clients are like well the clients we're
[4024] working with it was legal and and travel
[4026] and financial and regulatory and they
[4028] don't actually want a large graph to
[4030] solve their rag problem. They want their
[4032] question answered and they don't really
[4033] care what it's in at all. Right? So
[4037] again this is all in the scope of rag. I
[4038] know this is a conference and I'm
[4040] looking forward to going some of the
[4041] talks around large graphs and how they
[4042] work and they're particularly interested
[4043] in the ESG talk but I think that the how
[4047] to make it work for a rag query is it
[4049] needs to be really granular really
[4051] specific not confounding completely
[4053] represent the scope and no more and our
[4055] way to do that which is a little bit of
[4056] a copout is just make it a lot smaller
[4058] and don't represent the whole domain or
[4059] just scope it in to the point that you
[4061] answered that question
[4064] so I'm just going to go through some
[4065] problems and some like broadly where we
[4067] arrive
[4068] at this piece, right? So, this is
[4072] vaguely right. At a high level, if the
[4075] LLM made something up, give it
[4077] information so it makes less stuff up.
[4080] I poison the context because I gave it
[4081] too much. So, cool. Now, do a knowledge
[4083] graph. So, this is where knowledge
[4084] graphs start to come in, which is like
[4086] structured grounding, right?
[4091] My domain isn't fully represented. It's
[4093] like, cool, build a knowledge graph of
[4095] the domain. Right? So now I made a graph
[4097] but my domain isn't represented. It's
[4098] like cool add all the stuff in that
[4100] right but then you start to get to
[4101] knowledge graph specific problems which
[4104] is my graph isn't representative of how
[4105] we work and it's like okay um what we
[4108] want to do is that like when I think
[4110] about resources we have people in
[4112] procurement we have people in supply
[4113] chain we have people in operations and
[4115] then we have specific geologists and
[4116] chemists and we have a bunch of
[4117] different people who contribute to this
[4119] problem. I do not want to give I I
[4121] shouldn't have control of the schema for
[4123] a chemist but as a data scientist I
[4125] sometimes have to. If you give a natural
[4127] language schema as a JSON document then
[4129] the chemist can control what the chemist
[4130] needs to control and they can look at
[4131] what they need to control and they can
[4132] consistently represent how the domain is
[4134] represented the granularity and the
[4135] specificity and the opinion of the
[4137] domain expert who worked on that.
[4142] This is the conclusion we broadly came
[4144] to which is like I can't represent
[4146] everything in veterary radiology but it
[4148] turns out I don't have to because the
[4150] question isn't how do I answer every
[4152] single question in veterary radiology
[4153] completely the question is how do I
[4155] solve these reports that I need
[4157] so reduce the scope is broadly what we
[4159] looked at and I know that contradicts a
[4161] lot of stuff around completely represent
[4162] the domain right but I'm not looking to
[4164] completely represent a domain I'm
[4165] looking to solve a rank question at
[4167] least that's what I'm paid to do
[4171] so this is the process that I develop uh
[4174] in people in this room may be similar.
[4176] It does require if you're perfectly
[4178] aligned to operontology or if you're in
[4179] an ISO standard, it's less applicable.
[4181] But this is how I build graphs with
[4182] LLMs, which is I build it, I look at it,
[4184] I go that sucks and then I look back and
[4186] I change it and I build it and I go that
[4187] sucks too. Turns out I wrote the schema
[4189] wrong so I'm going to change it and then
[4190] I'm going to update and look and update
[4191] and look. But if you can build a graph
[4193] like I showed you in like a minute, then
[4195] you can get in like you know 30
[4197] iterations in an hour and all of a
[4198] sudden you're like well now this is
[4199] pretty good or I can ping the right
[4200] person on Slack because it turns out me
[4202] saying Jerry friends with like friends
[4204] with isn't specific enough or if I'm in
[4206] procurement and I'm not really sure what
[4208] this word means. You ping the right
[4209] people or give it to them but that
[4212] making it representative I think is
[4213] really important when it comes to the
[4214] rag process.
[4216] Um this is a question we get a lot. My
[4218] answer of do you have any evaluations is
[4221] no.
[4222] um and I don't want to talk about them
[4224] anymore, but I keep getting asked about
[4225] it. So, what I will say is that
[4227] benchmarking this stuff is I think a
[4230] waste of most people's time. You can
[4232] benchmark it for your specific use case
[4234] if you have specific people using your
[4236] specific stuff, right? But if I was to
[4238] benchmark a graph rag solution, how is
[4240] that indicative of your domain and your
[4242] granularity and your specificity and the
[4244] way that you query and the way that you
[4245] work? Right? So, how do I evaluate this
[4247] stuff? It's like well I have a question
[4248] answer set by the people who know what
[4250] means you know what it means and then
[4252] I'm just gonna it's a we're not
[4254] affiliated but it's a mild plug I guess
[4255] is that like if you use something like
[4258] Langmith uh from Lang chain in the LLM
[4260] it's like well then you track every
[4261] question and answer and then you can
[4262] look at it and say that's wrong and then
[4263] you can look at the evaluations you can
[4264] look at what the LLM generated
[4266] tracking what you did builds you this QA
[4269] set really quickly so like one of the
[4271] best ways to evaluate this stuff is have
[4272] a have a question answer set and one of
[4274] the best ways to build a question answer
[4275] is use the system a lot if you're
[4277] anything like me using the system a lot
[4278] already. So it's like store them and
[4280] store them in a structure way and test
[4282] them. But I I think evaluation is a
[4284] really good question. How do you
[4285] evaluate this? And the unfortunate
[4286] answer is a domain expert needs to look
[4288] at the questions and answers and see if
[4289] they're right. If there's a better way,
[4291] I I I'd love to know about it, but I see
[4293] a lot of people writing blog posts and
[4295] stuff around evaluation and I just look
[4296] at it's like this just seems different
[4297] or it doesn't solve my problem or I
[4298] don't know what to do with this. So it's
[4300] like a QA sets really how to do it.
[4303] So what if the graph's too small? I
[4305] think is interesting, right? Because
[4307] I've just suggested the idea is like
[4308] scope in the domain. It's like why
[4312] did I just build a graph to solve one
[4314] question that I don't actually have a
[4315] lot? There's power law arguments, but I
[4317] said before 40% like 60% of the rest of
[4319] that is done, right? So, do I have to
[4320] tear down asmtoically to find what I can
[4322] find?
[4325] Uh this is an interesting question that
[4327] I want to talk about. Now, I'm not sure
[4329] how many ontologists are in the room,
[4330] but who's familiar with the open world
[4332] assumption, closed world assumption?
[4334] Awesome. This is exactly the room I want
[4335] to be in. Right? So, LLMs and knowledge
[4338] graphs have an open world assumption,
[4340] right? I don't know that all these facts
[4342] are here, so I'm going to make stuff up.
[4344] But I told you making stuff up is not
[4345] really what we want to talk, right? So,
[4348] I I don't really want to make things up,
[4349] right? I don't want to let the LLM make
[4351] things up. I would actually really like
[4352] it if I close the world for the
[4354] assumptions that it was making, right?
[4355] And then that's limiting in a
[4357] frustrating way. Another insight is that
[4360] most workflows are decomposed into
[4362] tasks, right?
[4364] So, um, we think about travel agency a
[4368] lot. And by the way, if anyone's looking
[4369] for an LLM graph rag product, um, I'm
[4372] still I I think it will be a travel
[4374] agent because I think that's the easiest
[4376] to extract and the most aligned to our
[4377] operontology really quickly, which is
[4379] just like locations and prices and
[4380] people. It's like it's the the least
[4382] likely to hallucinate and extract. So,
[4384] if anyone wants to like build a cool I
[4386] don't have time, but it's if if travel
[4387] agency would be great, but it's really
[4388] like I' I haven't booked a flight with
[4390] an MLM yet, right? Because I'm not
[4392] really trusting. I'm not really ready to
[4393] I don't think it's reliable. Like if
[4394] each of these are agents, right?
[4398] Then if this is 95% accurate, right? If
[4402] there's five agents and they're 95%
[4404] accurate each. And by the way, 95%
[4405] accurate in a rag system is a high bar,
[4407] right? But if I have five agents
[4408] together chained, 95% gets out to 77%.
[4412] Right? So 70% of the time I book my
[4414] flight and it doesn't work is not
[4416] acceptable.
[4419] So
[4421] agents
[4424] can do tasks, right? And so our broad
[4427] point is that give an LLM the least
[4431] responsibility possible and then have a
[4433] lot of them. And each LLM can be
[4435] assigned to an agent and each agent can
[4437] be assigned to a task and each task can
[4439] be assigned to a domain and each domain
[4440] can be assigned to a graph and each
[4441] graph can be assigned to a schema. So
[4443] when I talk about small graphs, the
[4446] point is make one schema per graph, have
[4448] one to many documents per graph. Have
[4450] one task per agent, have one graph per
[4452] agent. It's like, well, now the point of
[4455] what I talked about, which is I get
[4456] really granular in what you built. When
[4460] I talk about what's rice to a chef,
[4461] what's rice to a farmer, if I have a
[4463] rice, if I have a farmer agent, I have a
[4465] chef agent, well, now I have two
[4467] different domains. And then I can be
[4468] specific in the schema about what is
[4469] rice to each one. And they can
[4470] communicate just through prompting. I
[4472] can IOT test the whole thing and now I
[4474] can incrementally improve the schema to
[4476] get each one from 95 to 100. So now I
[4479] have full control with specific like the
[4481] one of the best examples I can think no
[4482] one's going to we're a long way away
[4484] from someone doing their full supply
[4485] chain with this. But if I think of like
[4487] a global supply chain and I think of how
[4489] many different tasks there are and I
[4491] think that I can split them down into
[4492] agents and I can incrementally give each
[4494] individual the schema and the documents
[4496] that are required and then I have a
[4497] process to update that schema and update
[4499] their documents relatively easily. Then
[4501] I see not one big graph managing a
[4503] global supply chain process because that
[4504] seems unwieldy and if someone's built
[4506] them that's fantastic but I see many
[4508] many different agents each with their
[4509] own domain interacting with a supply
[4512] chain like that.
[4515] So this is why we like small grass just
[4517] easier to make right. So whichever way
[4520] you want to define schema ontology
[4521] hierarchy taxonomies like the people
[4523] talk about all different ones but you
[4526] can define the scope of the agent right.
[4528] So if I go back to the open world
[4529] assumption, right, open world assumption
[4531] is necessary for what we currently have.
[4533] If I close the world, I have a closed
[4535] world assumption and I have everything
[4537] agentic, right? Then what I have done is
[4540] been like, well, now the the agent isn't
[4543] making things up. So I close the world
[4545] and that's limiting, but it's okay
[4546] because the agent only has one task to
[4548] do and I actually only want it to do one
[4550] thing over and over again. So why we
[4552] like small graphs is we're solving
[4554] workflow problems and we like using
[4555] graphs to do structure grounding. But if
[4557] you break those workflow problems down
[4559] into their components with the
[4561] individuals that matter, then we can
[4564] build this faster
[4568] l and knowledge graphs use an open world
[4570] assumption. Right?
[4573] If you have many agents, you can use a
[4574] closed world assumption. And I'm very
[4575] happy to discuss this. I know it's a
[4577] broad philosophical topic and I'm very
[4579] interested in it. But I I'm making some
[4581] taking some liberties here. But I think
[4582] broadly it's like LLMs need an open
[4584] world. Knowledge graphs need an open
[4585] world. No knowledge graph is complete
[4586] but you can work on knowledge graph
[4587] completeness but if you have an agent
[4590] you close the world I think that you can
[4592] make it consistent and then you can
[4593] improve it iteratively and you can get
[4594] to the point where it's like now how am
[4596] I evaluating this it's like well it's
[4597] just the domain just the schema it's
[4599] just the process yeah is the assumption
[4602] here that most of the queries are
[4603] localized to a given domain because if
[4606] you had queries that by definition
[4608] traverse multiple domains agents then
[4610] you're back to the same problems. Yeah.
[4612] So I I guess that the idea is like I I
[4614] think that rag which is like a natural
[4616] language query and then a response right
[4618] and maybe a multi- aent response isn't
[4620] really how the future of work's going to
[4621] be right I actually don't really want to
[4623] trust that so I think that how you
[4624] orchestrate a multi- aent system is
[4626] really important right but I think your
[4628] question is like which agent does it
[4629] apply to and my answer is like if you
[4631] know the workflow that should never be
[4632] the question that you ask right and I
[4634] think it's a very good question to be
[4635] but it's like if we think about travel
[4637] agency it's like I would like to do my
[4639] flight here right I've worked on this
[4640] before it's like take that natural
[4642] language query extract the relevant
[4643] information which can be done with
[4644] space. it can be done almost
[4645] deterministically then just pass those
[4647] off into what are effectively SOPs or
[4649] decision trees of like an agent flow
[4651] right and then I actually don't have to
[4652] worry about natural language to cipher
[4653] because I can just write pre-built
[4654] cipher groups right and then IO for
[4656] agents is now like well everything's
[4657] JSON or everything's paidantic or I can
[4659] pass the whole thing back and forth and
[4661] so I really just kick off the process
[4663] like we described before if someone asks
[4664] a graph query and you vectorized your
[4666] graph I can just map it to the right
[4667] node or nodes and that's actually what
[4669] we do and then I run preset queries so
[4671] this is just doing that but over and
[4672] over and over again and so so what I do
[4674] is just each agent or each task or each
[4676] conditional description in the in in the
[4678] tree in the flow is is in that process.
[4683] Doesn't assume that there's one entry
[4685] point to your workflow. Not necessarily.
[4688] So at the moment, yes, but like if you
[4690] look at rag, there's one entry point as
[4691] well. But I think that uh the way that
[4693] we've done it is like well let's say you
[4695] have different personas in like a
[4696] marketing situation, right? And it's
[4698] like well you can just multiclass
[4699] classify and then just kick that process
[4701] off. I'm not going to say this is a
[4702] deterministic process. Um but yeah
[4704] absolutely but how you then classify I
[4706] think the important thing here is that a
[4708] lot of these are software engineering
[4709] problems or machine learning problems
[4710] that have been solved in the past and so
[4712] a lot of the issue is like how do I
[4713] reduce the stockicity of the LLM and so
[4715] when it comes to like if I just ask a
[4717] single question can I just route it to
[4719] where I want to go and I think that's
[4720] largely a solve problem the difficulty
[4722] is describing the processes I'm not
[4724] saying it's easy I'm just saying that
[4725] this is a way to reliably multi- aent
[4727] solve a workflow
[4729] you mentioned previously aligning with
[4731] an operative on topology
[4733] Isn't that supposed to harmonize between
[4735] the different domains different? Yeah.
[4738] So my push and again I I spent a lot of
[4740] time with uppertologies. I think they
[4742] definitely have their place but like if
[4743] you've closed the world and the agents
[4745] there then what do you need an
[4745] operontology for in that agent right?
[4748] And so the approntology is necessary but
[4750] you could also argue that like a concept
[4752] net is probably in the LLM already. So
[4755] it's like what am I really aligning to?
[4757] And it's like well I'm actually aligned
[4758] to the LLM now. So it's like if I can
[4760] put a level of trust in like does now
[4762] that I understand a parent child
[4763] relationship. It's like I don't think it
[4764] messes that up very often. It messes up
[4766] a granularity. So then that's part of
[4769] the process. So you can add up
[4770] ontologies you can you know create the
[4772] schemas as much as you want but that's
[4774] at least something that we've noticed
[4776] and we're working more and more on it.
[4777] But I think the key thing here is like
[4779] we're not representing a domain we're
[4780] solving a rag problem and so we just
[4782] reduce the domain so we don't have as
[4784] many problems.
[4786] Um yes this is what we do. Again I've
[4788] talked about I don't want to plug too
[4790] much and I do want to be clear that like
[4791] this is intentionally provocative. I
[4792] know that like there are large graphs,
[4794] there are small graphs. People don't
[4795] necessarily want to make a small graph.
[4796] It doesn't have value. But I wanted to
[4798] give an example of like why that's the
[4800] case.
[4802] Um this is an example again of the graph
[4804] that we had. I want to go back to it.
[4806] You could argue this is small, this is
[4807] big. It really depends on what you're
[4808] looking at. But this is an entire domain
[4810] from a script, right? This has the
[4813] chunks, this has the context, this has
[4814] everything you need in it. So in theory,
[4816] you could have an agent whose job is to
[4818] like you have one agent whose job is to
[4821] make Seinfeld scripts, right? Or make a
[4823] new Seinfeld script, right? And this is
[4825] the graph that it refers to, but that's
[4827] not necessarily good enough. So then you
[4828] have an agent that's job is to interpret
[4830] this big salad graph, right? And then
[4834] that's agent's job is just to look at
[4836] this. And so I can have another agent
[4837] which is another script, right? There's
[4839] no reason why I can't have those.
[4840] They're two different schemas. So a
[4842] really motivating example for this
[4844] business was very early on it was a
[4846] random medium post by a guy didn't talk
[4848] a whole lot but uh he he was got early
[4851] access to GPT3 as an API and so was
[4853] building these these systems right as as
[4855] APIs and he wrote this thing called
[4856] writing GPT so a super well-known blog
[4859] post but it's one of the most motivating
[4860] I've seen which is like and this is a
[4862] more common workflow now but he said
[4864] okay I'm not a writer I don't write
[4866] blogs necessarily but I know vaguely how
[4868] to I'm going to build a writing agent
[4871] Right? And then in theory, you just type
[4873] what you want and it gives you back an
[4874] answer. Right? It builds you content.
[4876] They said, "But that's not really good
[4877] enough. So, what I'm going to do is I'm
[4878] going to build an SEO agent and I'm
[4880] going build a uh I'm going to build an
[4882] SEO agent. I'm going to build an editor,
[4883] like an editing agent. I'm going to
[4885] build a colloquialism agent to make it
[4888] more accessible. And then I'm going to
[4889] build an agent that's job is to tell me
[4891] where to put photos." He was a
[4894] photographer, right? This guy was like,
[4896] "Then if I have this process, not no
[4898] human in the loop, just agent
[4899] workflows." What it did is he was just
[4902] like, you know, you can make money by
[4903] just like saying, "What are the 10 best
[4905] washing machines of 2024, right? Just
[4906] put that blog post up." So he's just
[4908] like just typed it into the prompt,
[4909] right? And so when we talk about that
[4910] prompt and we talk about um routing to
[4912] different workflows. It's like he just
[4913] typed in write me a thing about the best
[4915] thing, right? So it wrote it and it was
[4916] bad. So the editor said and then it fed
[4918] back, right? And you do have to have
[4920] some level of utility, function, or
[4921] condition on that. But it's it's simple
[4923] enough. You can just say run it twice
[4924] and it gets pretty good. And then it
[4925] runs twice with the editor, runs twice
[4927] with the SEO, makes a clo, shows him
[4928] where to put the photos. Then he went
[4929] and took the photos that it describes.
[4931] Now he has original content and then was
[4932] able to get to the top of SEO rankings
[4934] pretty quick, right? This was at GPT3
[4937] level, right? That's an agentic
[4938] workflow. It is relatively simple. It
[4940] has consistency. Again, he had a low
[4942] bark. It's a blog post. It doesn't have
[4943] to be super reliable, but I think the
[4945] next steps are that motivating process,
[4947] which is what he described was how to
[4948] write a blog, right? Which almost any of
[4950] us can do, right? and I can't
[4952] necessarily edit and I don't know much
[4954] about SEO, but I can tell an LLM, make
[4957] this SEO compliant. I'm going to put it
[4958] on Google. I live in, you know, the
[4959] Western world, right? Like you you can
[4961] instruct pretty easily when it comes to
[4962] this stuff. And then, especially if
[4964] you're in a business that has domain
[4965] experts, they can instruct even better
[4966] and they can write even better schemas
[4967] and they can have even better graphs.
[4968] But if you think about those agents,
[4970] it's like what does the uh what does the
[4974] SEO agent refer to? In this example,
[4976] what I'm suggesting is it refers to
[4978] maybe someone's written a document.
[4979] Maybe someone's written this, you know,
[4980] particular um SOP of how to do SEO.
[4984] Maybe there's some reference document.
[4985] Maybe there's a Wikipedia article. Well,
[4987] there's in a graph and then it refers to
[4988] that, right? So when it answers its
[4990] question, it pulls in the structure
[4991] grounding of the context. And so that's
[4993] why we use small graphs to solve
[4995] workflow problems is because instead of
[4997] having one graph that is very broadly
[4999] applicable and I have to refer to I can
[5001] have that and you can see at that point
[5003] it doesn't necessarily need uppertology
[5004] alignment, right? There are examples
[5006] where you would like when I think about
[5007] what are the really high value reliable
[5010] questions I I think and again I was
[5011] exposed to plant control and suspensions
[5013] and failures in large operating
[5015] machinery and so those are more
[5017] difficult to trust but again if I have
[5018] an ISO standard right I can just use
[5020] that ISO standard and now it's following
[5022] that specific process
[5025] that's the end I think I've done pretty
[5026] well on time so this is a running a
[5028] closed beta at the moment um but uh yeah
[5030] please check us out uh this is this is
[5032] the type of work we're doing um we do a
[5034] bunch of other stuff around rag as well.
[5035] But I just wanted to put this here
[5036] because I think it's a good group of
[5037] people around. I can talk
[5038] philosophically around what does it mean
[5040] to be a big graph and what does it mean
[5041] to need an uppertology and what does it
[5042] mean to be semantic? Uh which I think is
[5044] interesting. But um please check this
[5046] out. Thank you very much. I'll stick
[5048] around for some questions.
[5057] Please do.
[5062] Right. So there isn't any like publicly
[5064] available graph embedding right now. Um
[5066] there are some levels of graph
[5068] embeddings. The Snap group out of
[5069] Stanford probably does the best and I
[5071] also saw there's a YC startup that's
[5073] trying to do some some graph embeddings.
[5074] But I'd say we have our own because none
[5076] exist and they're not particularly good.
[5078] But the thing that we can get away with
[5080] as well with a smaller graph is like
[5081] like when it comes to like things like
[5082] entity resolution, it's like if you have
[5084] a smaller graph, it's actually a lot
[5085] easier because then you can resolve rice
[5086] and what it is. Like in the example I
[5088] showed like how many jerries are there
[5089] in the world? A lot. How many jerries
[5091] are that in that script? One. So like
[5092] any of those is just going to be a line
[5094] but when so we use embeddings for that
[5096] process but I don't know of any that are
[5098] publicly available uh yet I know of
[5101] research projects that that I can refer
[5102] to. Yeah. If you already had a big graph
[5106] then is the suggestion here that you
[5108] should think about creating these if I
[5110] call it microraphs for a domain. So I
[5113] think that's a decision and it depends
[5114] on the the if you have if you've already
[5117] represented your domain. My question to
[5119] you is is it granular enough? And I
[5122] think when it comes to rag, the answer
[5123] is probably not everywhere you need it.
[5126] So then the question becomes, how do I
[5127] make it more granular? And there's two
[5129] broad answers. One is make a more
[5131] granular specific graph that only
[5132] answers that question. And the other is
[5134] make your existing graph more granular.
[5135] And that's going to depend on what's
[5137] your conditions, what's your alignment,
[5138] how do you do that process. I think that
[5140] is the problem in that the the large
[5142] graphs I've used are like again they um
[5145] when it comes to rag and really specific
[5147] questions and again this is just rag
[5148] there's there's other use cases but when
[5150] it comes to really specific questions in
[5151] rag um graphs that I have almost solve
[5155] all of my problems and never solve the
[5158] one that I want at that point in time.
[5160] So getting it more granular is like
[5162] that's a decision that you have to make.
[5163] I think that's a design choice. I think
[5164] if you're starting from scratch, I think
[5166] this process makes a lot more sense. If
[5167] you have an existing graph, then it's
[5168] how do you get granularity and that's a
[5170] decision. Yeah. How do you like define
[5173] granularity in the context of the
[5175] schema? Like more specific words, more
[5177] general categories, like how do those
[5179] tie together? Yeah. So, this again comes
[5180] down to evaluation. It's really
[5181] difficult to be like what is
[5182] granularity, right? What is deep
[5184] learning? Where do we get to? And it's
[5185] like, well, you just have the question
[5186] answer set and that's kind of it. But
[5187] the schemas that I showed are very
[5188] general, right? Character of it's like
[5190] if I wanted to do comedian, I could,
[5193] right? Right. And this is an instructive
[5194] process that that extracts. So it's a
[5196] really good question and it's difficult
[5198] to define granularity but as long as
[5199] you're starting with a question answer
[5201] set it's like did it answer my question
[5202] and if not make it more granular which
[5204] which is like an iterative process right
[5206] I wish I had a better solution no
[5211] pattern uh example that you showed at
[5213] the beginning and say full what would
[5216] you say is the sweet spot of
[5218] expressivity through oh that's a great
[5219] question. Yeah I really like that. Um,
[5222] so I've done a lot of work in L and
[5225] anything like URI really specifically
[5227] align and we look at schema.org a lot in
[5229] terms of alignment. The sweet spot I
[5232] think is so and again the example I
[5235] showed is like a very simple example
[5236] right so there's somewhere in the middle
[5238] um I think the sweet spot is what we're
[5241] building at the moment which is like um
[5243] I have a one tier like just parent child
[5246] relations in a schema and I have
[5248] cardality on each relation right and
[5250] then I can I can build properties out if
[5252] I want to but um I don't necessarily
[5254] need to align to like a schema or in a
[5257] lot of cases um but I think the sweet
[5260] spot is
[5263] to be honest the sweet spot would be al
[5264] if uh I had a code gen that could
[5267] automatically I think people just want
[5269] to type words I don't think they want to
[5270] necessarily type the rest of it so I
[5271] think filled it in that would be really
[5273] useful right now I think the sweet spot
[5274] is parent child taxonomy and then
[5277] cardality
[5287] I notice
[5289] board you've
[5290] It's repeated.
[5294] Yeah. Yeah. So, this is an example like
[5295] the schema is like super basic. So, it's
[5297] like we we completely pass all of the
[5298] text for this example and it's like
[5300] because the schema is
[5305] um
[5308] object clothing food character like
[5310] sometimes it's going to mess that up. I
[5311] mean the benefit of graphs is that it's
[5313] all fully crud. So, it's like just
[5314] delete it. Um, but the that's something
[5316] I really like about the representation,
[5317] but it's like it was from a previous
[5319] thing. But yeah, it's just that it's
[5320] automatically finding it. There's some
[5322] level of generation. You just kind of
[5324] change it.
[5331] Proprietary embedding algorithm. But
[5333] then uh when the query gives you like a
[5338] subset of your vectors, uh how uh in
[5341] what format do you decode them to the?
[5344] Oh, cool. Yeah. So, we don't necessarily
[5345] use proprietary. I just say that like
[5347] again we work with clients. I experiment
[5349] a lot with local and open source models
[5351] and I think they're fantastic. They're
[5352] difficult to build into a product right
[5353] now. So, you're going to get to host
[5354] your own stuff. It's difficult. I think
[5356] a lot of people are comfortable,
[5357] especially with Azure OpenAI. People are
[5359] comfortable bringing that sort of stuff.
[5360] Um, we store the vectors, right? Then
[5363] the simplest way to retrieve that. We I
[5365] have an open source package out
[5366] somewhere which is around rulebased
[5367] retrieval. Doesn't use graphs. It's just
[5369] using rules. And it's like you really
[5371] just like every vector you can just like
[5372] add metadata to. And that metadata is
[5375] really limited by character length and
[5376] that's a lot of what determines like how
[5377] big your chunks are. So you just store a
[5379] vector and then you have a bunch of
[5380] metadata in it. One of those metadata is
[5382] the text. So when I retrieve a vector as
[5384] an object, I just refer to the specific
[5387] key in that object. Where does the text
[5389] come from?
[5391] Uh oh. No. So this is building a gra. Do
[5394] you mean if you if I'm using a graph to
[5398] the Yeah.
[5401] Right. Okay. So then this would be a
[5402] process of like I I have like high level
[5405] concepts and I want to give more
[5406] information like as text description
[5407] because what I was describing is like
[5409] graph generation. If you have an
[5410] existing graph I think it goes back to
[5412] what I was talking about before which is
[5413] like attaching a description or a
[5414] summary because like you can't like pull
[5416] the works out of thin air. I think you
[5418] use graph querying to be like I'm going
[5420] to add if you use a property graph I'm
[5422] gonna add a property like summary and
[5424] I'm going to attach that summary and
[5425] that summary is going to be what's added
[5427] in as context or description. If you
[5429] have a knowledge graph, you can have
[5430] another node that has the description if
[5432] you want. But it's a case of adding free
[5434] text as some either like an extra node
[5436] or extra relation or a property on what
[5438] you're doing. But that is a case of
[5439] post-processing
[5441] like as in like if you have a graph
[5443] that's like high level and just
[5444] description really useful for
[5446] instruction.
[5453] to answer questions.
[5456] Yeah, you're giving the LLM some
[5460] additional information from the graph.
[5462] Yeah, for that first.
[5467] Oh, are you saying how do I give the LLM
[5469] the text from the graph? Oh, sorry. Uh,
[5471] yes. So query get back the triples.
[5476] Those triples are then passed in as like
[5478] a variable and they can be passed in.
[5480] The simplest way would be write a
[5481] prompt. That prompt is a string. That
[5483] prompt accepts variables. And there's
[5485] many different ways. Lang chain is a
[5486] great way to start and try out uh and
[5488] and we use lang chain a lot. We really
[5490] like lang chain is to pass in a like the
[5493] triples that you get in the prompt. So
[5495] the llm you basically give it an
[5497] instruction that says hey here's my
[5499] question lank. Um here is the context to
[5502] answer that question blank and those are
[5504] variables and so at runtime you query
[5507] pass that in then the LLM does it for
[5509] right so triple so you get triples back
[5511] yeah and you convert that into three
[5513] words
[5517] uh oh so as in like they have to be text
[5520] well do they have to be text
[5523] well not necessarily I'd say what we
[5525] literally do at the moment is it's a
[5527] pyantic model so I guess it's an object
[5529] so they don't necessarily have to be The
[5531] LLM expects some level of text
[5534] understand how triples become text right
[5538] I can tell you how we do it which is
[5540] just loop take every triple and because
[5543] sometimes triples can be too big for the
[5544] context uh we just string match it uh
[5547] and so we just say like if Jerry knows
[5550] George Jerry knows Kramer that would be
[5551] an example of a triple right that's
[5553] currently stored as a we have a list of
[5556] tupils those tupless have three
[5557] variables each of those variables are a
[5558] string and so Then we can just pass
[5560] those and say Jerry knows George,
[5562] Kramer, Elaine. And then we pass that as
[5565] text into the LM. So essentially triples
[5568] become three word sentences and those
[5570] three word sentences
[5572] somehow. Yes. Uh I I think it's Yeah,
[5576] it's a good point. I think that the
[5578] state-of-the-art is not yet at the point
[5580] where it can handle like a custom object
[5582] like we work with pandas a lot. How do I
[5584] give it a pandas daytime object? I
[5586] can't. I have to give it a string that
[5588] is date. So yeah, it is very text based.
[5590] I think there's some really interesting
[5591] stuff around multimodal, but for now
[5592] when it comes to embedding models and
[5593] this stuff, it's all text based. Yeah,
[5595] but you have a lot of control over where
[5597] that text is input with prompts. So So
[5600] how big of an input does let's call that
[5602] like the prompt generation where you're
[5604] taking the graph and converting it to
[5606] natural language like have does it make
[5608] a big difference if you do like two hops
[5609] or like dual hops and then include
[5611] properties also? Good point. So what we
[5614] spoke about before is like uh I have
[5615] preset queries, right? The easiest
[5617] preset query is like just land on the
[5619] node that best matches and then just run
[5620] a neighborhood query, right? And just a
[5622] one or if you do two hop, you can if you
[5623] want to. It depends and I think this is
[5625] useful as like this graph, right? And it
[5627] also depends on your LLM model and the
[5628] size of the context. But the goal here
[5630] is not to have like like if if bigger
[5632] context windows come out that doesn't
[5634] really change my problem. My problem is
[5635] reduction and trying to give really
[5636] specific context only. So it does depend
[5639] on what's the type of query you want to
[5641] write. For us, that's a one hot
[5643] neighborhood uh with all properties.
[5646] So for the properties that won't fit
[5648] into the sentence I guess, right? So you
[5650] have to say like like uh Jerry knows
[5653] somebody and then you say Jerry is a
[5654] person and his birthday is this. Yeah.
[5657] So you we just have like specific string
[5658] formatting. So specifically what we
[5660] return as objects is a triple with the
[5664] chunk and the chunk context. Oh the
[5666] chunk. Yep. So we can give the chunk
[5667] context back. But it's like we have a
[5669] conditional objects that's returned
[5670] based on any sort of flags you want to
[5671] pass in. And that flags is like do you
[5673] want metadata or not? So we just call it
[5675] metadata. So the easiest way to do this
[5676] because metadata is used in vector
[5678] databases a lot is just like the
[5680] properties are really just like a
[5682] dictionary you can loop through and so
[5683] you just make a metadata dictionary and
[5685] then you just customize it based on
[5686] that. Okay. And so you you talked about
[5689] tuning like chunk size. Y um what about
[5693] I feel like you could also really tune
[5695] you know what metadata you return and
[5697] does that does that make much of a
[5698] difference in your experience?
[5699] Absolutely. Yeah. Now I think you bring
[5701] up a good point which is like property
[5703] graphs are great right but if I do a
[5706] natural language to cipher or GQL I
[5708] should say um the generation like I
[5712] it'll break if I said if it saidex
[5714] instead of name right which is about as
[5715] simple as you can get when it comes to
[5716] properties. So
[5719] the metadata that you return in the same
[5722] way that the rag you return because I
[5723] think that was just a kind of a
[5724] motivating example of why rag context
[5725] poison. Yes, the metadata is really
[5727] important. We just return all of it. The
[5729] metadata that you input is really
[5731] important. And so with our schemas it's
[5732] like you can add some level of metadata
[5734] and find that as well. But yes the the
[5738] easiest way to change your model is to
[5740] few shot it with examples. Not one or
[5743] zero. It's toshot it with examples. Um,
[5746] and so you are playing with fire in the
[5748] best way you can make something amazing
[5749] or something terrible with that fuseing.
[5752] And so the most control you have over
[5754] the response to your LLM is how you fuse
[5756] shot. And so if each example has really
[5759] specific properties that you've defined
[5760] in your schema, then now you've shot it
[5762] the best or the worst as you want. So
[5764] yes, I would say the biggest control you
[5766] have, the biggest control is the
[5767] relations by far. That's an emerging
[5769] property out of LM and that may change
[5770] with GBD5, but I doubt it. The biggest
[5772] is like what is related to what. But
[5774] then the second would be what is the
[5776] metadata associated with each of what is
[5778] related to what and that is the
[5779] properties and so the properties are
[5780] really important
[5784] goodness
[5788] and that's a time Yeah.
