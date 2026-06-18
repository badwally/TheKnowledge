---
schema_version: 1
id: yt-oGQZt1zR1d4
type: youtube
title: 'Making Your Knowledge Graph LLM-Ready: Quality Assessment and Design Strategies
  for GraphRAG'
url: https://www.youtube.com/watch?v=oGQZt1zR1d4
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:40Z'
content_hash: sha256:82a22d33f8f6d66b08aa60222614347dfd27f0b7c9bd36885dc19ace516f2ed5
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 1783
  caption_track: fetched
  snippet_count: 699
filter:
  score: 0.7
---
[3] [music]
[8] Hello everyone. Welcome to making your
[10] knowledge graph LLM [clears throat]
[12] ready quality assessments and design
[15] strategies for graph rag. The session
[19] will be presented by panos Alexa. So
[23] over to you panos.
[25] >> Thank you Daniel. So hello to everyone.
[29] Uh good morning from the Netherlands and
[32] I guess you're all around the world. So
[37] let's uh start. Let me share my screen.
[44] Okay. So
[47] uh in today's talk uh I'm going to to
[51] focus on uh the role of knowledge graph
[54] quality when it comes to using it in
[56] conjunction with with large language
[58] model and particularly uh when using it
[61] in the context of of graph rag. Um
[66] a bit of um a bit of clarification. Um
[70] the initial description of the talk was
[72] meant for a two-hour workshop. So it's a
[74] bit more ambitious uh but ultimately
[76] because of of time limitations and
[79] resource limitations it's going to be
[81] more of a high level talk. So what we're
[84] going to talk today about is um three
[88] things. So we're going to see a very
[90] brief overview of how of what graph rack
[92] is, what it entails and how it works.
[95] Then we're going to see um to talk about
[99] how can we assess graph quality, what
[102] metrics can we use, what these metrics
[104] can tell us, and how from these metrics
[107] we can uh determine or at least suspect
[111] whether uh our knowledge graph needs to
[113] be improved or not. And finally, we're
[115] going to see what are some typical uh
[118] quality issues that uh might happen in
[122] knowledge graphs and how this may affect
[124] the overall quality of a graph rag
[126] application and uh some high level
[130] methods on how to to detect those.
[133] Uh before that, let me introduce a bit
[136] more myself. So, I've been a DNA
[139] practitioner, author, educator for
[141] around uh for the last 20 years. I
[144] started working with ontology and
[145] knowledge graph back in 2004 far before
[148] the the era of m let's say the rebirth
[151] of machine learning big data now of
[153] course LLMs at the moment I'm working as
[156] a lead semantic data and AI solutions uh
[158] at tripleB a small consulting company in
[163] in the Netherlands
[165] um where we do where we work with
[168] clients big organizations to
[171] help them with implementing
[174] knowledge graphs and data integration
[175] solutions. Um I in 2020 I wrote a book
[180] with oral on semic data modeling uh
[183] covering best practices and you know how
[186] to avoid pitfalls and how to address
[188] things uh where you when we build
[192] knowledge graphs ontology and generally
[193] semantic uh data models and currently
[196] I'm writing a new book on evaluating AI
[198] systems.
[200] So let's start.
[203] when we interact with an LLM uh for
[206] question answering and generally the the
[209] typical uh way we interact is that we
[211] give it a question the LLM takes it and
[214] gives us an answer that's that's the
[216] simple thing and actually that's the
[217] most let's say appealing thing when it
[218] comes to to an LLM however uh it has
[222] been found through experience that uh
[225] this simple approach suffers from
[228] several drawbacks one being the famous
[231] hallucinations of course of LM the fact
[233] that they cannot always be trusted for
[237] telling you something that is correct.
[240] Um the second thing is uh the problem of
[243] knowledge cutoff. The fact that uh we
[245] cannot always expect that a large
[247] language model will know
[250] uh [groaning]
[251] will will have information about uh our
[254] particular domain or about our
[256] particular knowledge and and documents
[257] that perhaps are not accessible. Uh and
[261] a third limitation is the lack of
[263] explanability. The fact that we can get
[265] an answer maybe even with with an
[267] explanation about this answer but this
[269] explanation might not be
[272] as trustworthy as we would like.
[275] For that purpose um the the communities
[280] and the industry has come up with an
[282] approach called retrieval of meta
[283] generation.
[285] The basic idea behind this approach is
[287] as follows. We want we still want to use
[290] the DLM but we we want to give it
[294] concrete additional knowledge external
[297] knowledge that might not be in its uh in
[300] its training data already.
[303] So um in the typical rag uh in a typical
[307] rag pipeline this this external
[308] knowledge is in the form of documents.
[311] So the way uh a rag architecture works
[313] is as follows. We have a question and we
[317] feed this question before we feed it to
[319] the LLM we give it to a retriever. The
[322] retriever it's actually information
[323] retrieval system a search engine if you
[325] like which from the documents that are
[327] in our external knowledge base will uh
[329] retrieve the top k usually similar
[331] documents similar to the question these
[334] documents these top K similar documents
[337] will form the context of of our question
[339] and along with the question will be fed
[340] to the LLM. So uh and based and then the
[344] LM will use this context to reason and
[347] answer the the question. The idea what
[349] we expect from this is that because we
[352] give it particular context to the LLM
[355] that we will reduce as much as possible
[358] the probability of hallucination and
[361] that will increase the the chance that
[363] we'll get a meaningful answer.
[367] Now,
[369] graph is a variation of this main uh of
[373] this of this architecture of this
[374] pattern where the main difference is
[377] that instead of using uh documents as
[379] our external knowledge, we use a
[381] knowledge graph. Right? I'm not going to
[383] go I'm not going to define again a
[385] knowledge graph. I I I assume that
[388] attending this conference you have
[389] already some knowledge of what a
[391] knowledge graph is. But again the the
[393] idea is that rag with a knowledge graph
[396] h uses um has the same interaction
[399] paradigm more or less and uses a
[401] knowledge graph as a as an external
[403] knowledge uh knowledge source.
[406] Now there are several uh variations of
[411] of graph rack but the main the two main
[414] let's say the two basic patterns that uh
[416] we have seen being used are the as
[419] follows. The first button is called text
[421] to query. Here what we have is that we
[423] have a user posing a question. Um and
[427] what the system does is that it
[429] considers it retrieves from our
[431] knowledge graph its schema. So only it
[433] schema not its data which means that uh
[435] the type of nodes the labels the
[437] properties and the relations and uses
[440] the schema to transform the question
[442] into a structured query. If we use
[444] neoforj that query would be cipher. If
[447] our knowledge graph for example is in in
[448] RDF and semantic web languages that uh
[452] that query would be a sparkle query. If
[456] we our um knowledge graph for some
[458] reason is implemented in s in in a
[460] relational database in SQL then the
[463] question would become an SQL query.
[467] The second pattern um is
[472] uh more let's say similar to the
[475] traditional rack. This is when we
[477] consider uh facts and assessions from
[480] the knowledge graph either from the
[482] whole knowledge graph or a subset of it.
[484] Um this we create vector embeddings for
[488] for these facts and assertions. We store
[490] them in a vector uh database and then um
[495] given a question we perform a retrieval
[498] of of the most relevant facts based on
[500] embedded based similarity. Right? So uh
[504] this is a different pattern than than
[506] the previous one. It has its pros and
[508] cons with respect to the previous one.
[510] Now
[512] graph quality
[515] how do we know how can we assess whether
[517] uh a graph rack system works well for
[519] us. So there are three quality factors
[523] that we need to consider right. Um if we
[526] if I go back we'll see that uh well we
[529] have a rack system we can view it as end
[531] to end so question and answer but it
[533] also has three important components. It
[536] has a retriever it has a generator and
[538] it has an external knowledge. The
[540] quality of each of these components will
[543] inevitably affect the overall quality of
[545] the system.
[549] So when we assess a graph system sorry
[553] the quality of a graph system we need to
[555] consider the quality of the retrieval
[556] that is asking the question whether the
[558] retriever retrieves useful and relevant
[561] context for the user input for the user
[563] question. The second thing is the
[565] quality of the generation that is
[567] whether the LLM understands and uses uh
[570] this context properly and finally the
[572] quality of the knowledge graph itself.
[574] So whether the structure and content of
[575] the knowledge graph actually helps the
[577] the retrieval and the generation steps
[579] or hinders them.
[583] So how do we know what works well and
[586] what not? Right? How can we um assess
[591] um if the overall system works well or
[593] not and which of these components might
[596] not be working so well.
[599] For that we have uh metrics uh in in
[604] rack systems. There are several metrics
[606] that have uh been uh proposed by the
[609] community and are available in several
[611] toolkits. Um I will talk here about six
[615] of these. First metric is called answer
[618] correctness. This is an end to- end
[619] metric that practically measures whether
[621] the generated response to the question
[624] is factually accurate and complete with
[627] respect to a ground trth uh answer. So
[631] in order to calculate this metric we
[633] need to have uh for for a given question
[636] its ideal ground truth answer and then
[639] what we do is that we take uh the actual
[642] answer that the that the system gives us
[644] and compare it to the ground truth
[646] answer. Right? So this is an end to end
[647] metric.
[649] Um this is a useful metric to evaluate
[652] whether our system works well or not.
[654] But it doesn't it's not really useful
[656] for debugging purposes. Which means that
[658] uh if for for some reason we get a low
[660] answer correctness. We cannot know just
[663] from this metric whether the problem is
[664] in the retrieval, whether the problem is
[666] in the generation or whether the problem
[668] is in the in our knowledge graph.
[672] A second metric that is of quite helpful
[674] is also relevance. This one measures how
[676] well the generated response addresses
[678] the user query and aligns with its
[679] intent. This is similar to the
[681] correctness, but the main difference is
[682] that we don't have a ground truth
[684] answer. So the only thing that this
[685] tells us is whether the answer that we
[688] get answers the question, but not
[691] whether it's actually correct, right? Or
[693] whether it's it's the exact uh is is
[695] actually the answer that we are looking
[697] for. A third metric is faithfulness.
[700] Faithfulness measures the extent to
[702] which the generated answer is factually
[704] consistent not with the question but
[706] with the retrieve context. Right? Erh
[712] because it can be that the the answer
[714] that we get is contradictory to the
[715] context that we got or it's neutral or
[717] that it is entailed.
[720] A fourth metric is contextual relevance.
[722] This one this one measures how relevant
[725] the retrieve context is to the input uh
[728] question.
[730] Similar to cod codexual relevance we
[732] have codexual precision and codexual
[734] recall. Cortexual precision measures the
[736] extent to which the retrieve context is
[738] relevant to the expected output. So also
[741] for this metric we need a ground truth.
[742] We need to know for uh for a given
[745] question what um is the expected uh
[750] output and similar for conduction recall
[752] measure. we measure the extent to which
[754] the retrieve context includes all the
[756] information needed in order to produce
[757] the expected uh output. Now the power of
[762] this matrix is actually the usefulness
[764] is when we actually combine them. So
[767] let's see some some basic scenarios.
[770] Let's say that we measure this metric
[772] and we found and we find that we have a
[774] high answer relevancy and low
[776] faithfulness.
[778] This means that the generated answer is
[780] well aligned with the user's question.
[781] So it it does answer the question but it
[784] is not actually supported by the
[785] retrieve context. So the retrieve
[786] context says something different than
[788] what the answer tells us. [snorts] This
[791] indicate hallucination in the generation
[793] step. Right? Uh it's not that the
[796] retrieve context is relevant. So it's
[798] not it's not a retrieval problem. But
[800] the fact that the the answer is not
[805] faithful to the context indicates that
[808] DLM has really has actually let's say
[811] practically ignored the context and has
[814] decided to to give us its own answer.
[819] A second scenario is when we have low
[820] answer relevancy and high contextual
[823] call. that means that the context is
[825] relevant. H but the generated answer
[828] fails to address the user's query. So
[831] it's an answer to some to another
[832] question practically. Again here the
[835] problem likely lies in the generation
[836] steps. It's not it's not a retrieval.
[838] It's not a knowledge graph.
[840] A third case is when we find low
[843] contextual precision and no contextual
[844] recall. In that case then it means that
[847] the context is wrong and the and most
[850] likely insufficient. Here the likely
[852] cause is a retrieval failure or a wrong
[856] or incomplete knowledge graph. Uh which
[860] means that we need to further
[862] investigate it.
[864] Now [snorts]
[866] the question I get many times from
[868] people who built rag system and graph
[870] rack system is what can be wrong with my
[872] knowledge graph right because there is
[874] this from at least from how say from um
[879] the articles that I read online and uh
[882] you know the the proponents of graph
[884] rack they say that with an knowledge
[886] graph is good is perfect and works very
[888] well with with the ll the thing is that
[892] from in practice this and from my
[894] experience and I guess many of other
[896] people's experiences there can be many
[898] things potentially wrong with a
[899] knowledge graph that we need to be very
[901] careful of
[903] and I would summarize here I would say
[906] there are six main uh categories of
[908] problems in a knowledge graph the first
[911] potential issue is having a knowledge
[913] graph that contains assertions facts
[916] that are plainly false or if not plainly
[919] false highly subjective and debatable
[921] Right.
[923] So having for example let's say that we
[926] have a geographical knowledge graph that
[929] links uh countries to cities for example
[932] right and saying for example that the
[935] capital of of Greece is New York right
[938] that would be obviously wrong. So if we
[940] have a knowledge graph with wrong facts
[943] with wrong assertions this will will
[945] provide wrong context to the LLM and to
[948] the rack system and therefore the h
[951] accur the correctness of the
[954] uh of the answers will be
[958] will be compromised. Right? It can also
[961] be however that the uh assertions are
[965] not technically wrong but they can be
[967] highly vague and uh debatable. What does
[970] that mean? Let's say that we have a
[972] knowledge graph about uh professions and
[975] skills and uh
[978] um we want to use this graph in order to
[980] provide career advice. So we have
[982] [snorts] a question saying okay can you
[984] tell me what skills do I need in order
[986] to work as a data scientist or as a
[988] knowledge graph engineer [snorts]
[991] or what what skills I must have
[995] and assume that the knowledge graph
[996] contains
[998] uh this relation relation between
[1000] professions and skills. Now there is not
[1004] a universal truth about the relation
[1006] between a profession and a skill. This
[1008] can be highly
[1010] subjective in the sense that it can be
[1012] depend on context, can be depend on
[1013] industry, it can be depend on country.
[1015] Right? So it might be that the knowledge
[1019] graph seems to contain relevant
[1022] knowledge but uh if the the the
[1025] agreement as for the correctness of this
[1027] assertion is uh not high high enough
[1031] then again the the correctness and
[1034] acceptability of the overall system may
[1036] uh be compromised.
[1038] A second issue when it comes to uh
[1041] knowledge graphs can be knowledge that
[1043] is inconsistent. That is having in the
[1045] same knowledge graph assertions that
[1047] semantically contradict one another.
[1049] Right? For example,
[1052] going back to the example with uh
[1054] geography. Imagine having
[1057] a um
[1059] an assertion that a country has three
[1061] [snorts] different capitals for example.
[1063] Right? The problem with this sematic
[1065] contradiction is that they can confuse
[1069] uh the LM as well. Right? So imagine
[1071] that you retrieve a context that
[1073] contains three contradictory facts,
[1076] right? The LLM will not have a way to uh
[1080] to distinguish between the three. So
[1082] there's a high likelihood that we give
[1084] it that will give also a wrong answer.
[1088] A third um a third topic a third a third
[1092] problem is missing knowledge right um
[1096] the knowledge graph is there's a high
[1099] likelihood that is not fully complete
[1101] that doesn't contain the assessor that
[1103] actually should should be there right
[1105] and when that happens uh there are two
[1109] situ there are two potential h outcomes
[1112] either the retrieve context will not be
[1114] there so there's nothing there's no
[1116] context to be retrieved or the retrieved
[1118] context will be most likely irrelevant
[1121] to to the question because the actual
[1123] relevant context is not is not in the
[1125] knowledge graph. Right? Which means that
[1129] the the contextual recall and
[1131] potentially the contextual precision
[1132] will uh will be low.
[1135] A fourth problem is when we have
[1137] knowledge that is irrelevant and
[1139] redundant. Right? So in many cases a
[1142] knowledge graph can contain uh knowledge
[1145] about multiple domains about multiple
[1147] scenarios about multiple types of
[1149] questions.
[1151] When we feed the whole knowledge graph
[1153] to our application then um we
[1157] practically stress we we we we say we
[1160] assign high responsibility to the
[1162] retriever to find the real uh the really
[1168] um relevant
[1170] context the real relevant knowledge for
[1172] the question at hand.
[1175] So in that sense it might be better if
[1178] we are able to um if we know that our we
[1181] work on a subdomain of what the
[1183] knowledge graph contains and only pick
[1185] the know that knowledge instead of
[1187] feeding it to the complete uh knowledge
[1189] of the knowledge graph.
[1192] And the the same argument applies for
[1193] when we have in concise knowledge. In
[1195] concise knowledge is when we have when
[1197] the knowledge graph contains duplicate
[1199] or near duplicate redundant elements
[1201] especially when it comes to to entities.
[1203] This is a typical problem. Imagine
[1205] having built a knowledge graph about um
[1207] organizations and about people and
[1209] having uh for example two different
[1212] nodes or three different nodes uh cons
[1215] representing the same company or the
[1217] same the same person right this kind of
[1220] redundancy uh can pose a problem to do
[1223] to our graph application because um the
[1228] knowledge about a particular entity will
[1230] be um uh will be uh split split around
[1235] and can be difficult for the retriever
[1236] to pick it uh to pick it all up. Finally
[1241] um
[1242] uh sixth problem is when we have
[1244] knowledge that I call
[1245] incomprehensible.comprehensible
[1248] means that the knowledge graph contains
[1250] uh elements and assertions whose meaning
[1251] cannot be eased by humans. And by
[1253] elements I mean relation names the way
[1256] we the names of our labels the names of
[1259] the properties which can be ambiguous
[1261] highly vague highly uh obscure as to how
[1265] they mean and if we think an LLM as
[1268] being let's say I I don't I [snorts]
[1271] don't like to anthropomorphize things
[1272] but the idea is that the LLMs are able
[1274] to
[1277] work by natural language if the
[1280] descriptions and the names in our
[1282] knowledge graph of of our elements of
[1284] our nodes, edges and um and and
[1288] attributes cannot be easily understood
[1290] by humans because they can be too
[1291] ambiguous or too too vague. We cannot
[1293] expect the LLM to be better than this.
[1295] So there's a high chance that if that's
[1297] the case that that the LM will also fail
[1300] properly understanding what the
[1302] knowledge graph is about and therefore
[1304] not uh and bring
[1307] wrong results.
[1310] Now all these issues, all these types of
[1313] issues uh in a typical knowledge graph
[1315] management life cycle right need to be
[1318] tackled need to be uh detected as
[1321] potential problems um quantified in some
[1324] extent and then of course mitigated and
[1327] treated. When it comes to knowledge
[1329] graph detection problems there are three
[1331] uh let's say categories of of
[1333] approaches.
[1335] One first approach is to try to apply to
[1338] to define and and apply logical
[1340] constraints and actions. So for example,
[1343] we can def let's say we have a non graph
[1345] of events and each event has a start
[1347] date and end date. We can and we should
[1350] actually have a rule saying that or a
[1352] constraint saying that you know what an
[1354] event's end date cannot precede its
[1356] start date. Actually this is something
[1357] that happened to to a real use case that
[1360] I worked on a couple of months ago,
[1363] right? or having another rule like a
[1365] person cannot also be an organization
[1366] and things like that. Now these logical
[1368] cost and aums can really be be useful
[1372] but usually they are not enough. They're
[1374] not enough because not all types of of
[1377] issues can be logically expressed and
[1380] prevented.
[1382] For that we want we need to move to
[1385] things like uh huristics and soft rules.
[1388] Huristics soft rules are rules which are
[1390] not which if they let's say if they are
[1393] violated h they don't necessarily they
[1397] don't always mean that there is a
[1398] problem but there's that there is a high
[1400] chance that there is a problem for
[1402] example let's say that we have two nodes
[1404] two entities in our knowledge graph
[1406] whose names have a very high semantic
[1408] similarity more than let's say 0 9 or
[1411] 095 then there's a high likelihood that
[1414] that uh these terms are probably refer
[1416] to the same entity
[1418] Not necessarily, right? Not always, but
[1421] there is a high chance which means that
[1422] we can use this as an as an alert to
[1427] uh for further uh inspection and and uh
[1430] and checking or another example would be
[1434] to have a movie knowledge graph where
[1435] each movie has let's say less than three
[1437] actors in average. That's that's
[1442] probably a problem because we know right
[1445] it's common knowledge that um in the
[1448] majority of the cases uh a movie has
[1451] more than three actors. Of course there
[1452] are movies with one or two actors but
[1454] it's not the majority of that right.
[1458] So a heristic like that could indicate
[1460] completest problems for example.
[1463] And of course we can move even we can be
[1466] even more sophisticated and uh try to um
[1470] and go on and build more like a machine
[1473] learning based error detection
[1474] techniques including for example asking
[1476] an LLM or building our own error
[1478] detectors and classifiers right um like
[1482] for example we want to tackle ambiguity
[1484] we can ask an LLM to flank ambiguous
[1486] relations my recommendation my
[1488] experience shows that you can we can
[1490] already do a lot of things with the
[1492] first two categories, right? Logical
[1494] causes and actions and then some basic
[1496] huristics and soft tools. And for more
[1498] advanced cases, we can uh and we should
[1501] go for u building more sophisticated AI
[1505] NML error detection systems.
[1509] So let's wrap up. I think the takeaways
[1512] from this uh what I would like you to
[1515] keep from this talk is that graph rag is
[1517] indeed a worthwhile approach to
[1518] grounding glass language models with
[1520] fual domain knowledge. There's no doubt
[1522] about that at least in my in my
[1524] experience. Uh but graph rack quality
[1527] can severely be diminished if the
[1528] quality of the underlying knowledge
[1529] graph is low. And we saw at least six
[1532] problems, six ways that the quality of
[1535] the learning knowledge graph can be uh
[1537] compromised. Therefore uh it's
[1540] imperative to assess
[1544] both when we build the knowledge graph
[1546] and also as we maintain so continuously
[1548] to assess and improve the quality of of
[1550] the knowledge graph when using it as a
[1551] part of of of a rag application right
[1554] especially if we have uh built a
[1558] knowledge graph completely automatically
[1560] you know if we have generated from from
[1561] text or or other resources.
[1565] Okay, so that concludes my my talk. Uh
[1568] before going to questions, I'd like I
[1571] would just like to let you know that if
[1572] you are further interested in the
[1575] interplay between knowledge graph and
[1576] laz models, so more about graph rack,
[1579] but also on how can we use LLMs in order
[1581] to build this graph, there's a live
[1583] online course that uh I will be giving
[1586] uh next month at the Riley learning
[1588] platform. It's a it's a total six-hour
[1591] course where we where we're going to
[1593] visit the whole life cycle of knowledge
[1595] graph development and how can we build
[1598] evaluate and uh debug uh graph
[1602] applications. So thank you very much for
[1607] listening to me. If you want to contact
[1608] me, you can contact me through email,
[1610] LinkedIn, and also if you're interested,
[1612] I encourage you to join my Substack
[1615] newsletter where I give more information
[1618] and content about these aspects. So,
[1620] thank you very much. Please let me know
[1623] if you have any questions.
[1632] Okay. So, uh I see a question. Can you
[1634] give an example of an knowledge graph
[1635] for medicalical reasoning to detect
[1637] errors in the relationship? Can you use
[1638] an LLM as a judge?
[1641] Um
[1642] yeah, so indeed we can have a knowledge
[1644] graph for medicalical reasoning that
[1646] could for example uh relate um symptoms
[1650] with potential diagnosis with um other
[1653] kinds of patient information etc. and to
[1656] detect the synony graph of course yes we
[1658] can use an LLM as a judge right but I
[1661] would say that as always when it comes
[1663] to using LLM as a judge we need to judge
[1665] the judge as well right so um it's not
[1669] enough to say to give for example let's
[1671] say that
[1673] you say to the LLM okay can you tell me
[1675] if this relation is correct we need to
[1676] give it proper context also there right
[1679] and um additional
[1684] um you know guidelines on how to
[1687] properly judge it.
[1689] Okay, another question. Assuming that
[1691] the graph system is able to extract
[1692] knowledge through ETL processes and
[1694] distill data to the knowledge graph,
[1695] does it mean that manually pruning the
[1696] graph would be a smaller workload for
[1698] people and can the results of pruning be
[1700] serve as a mass template condition map
[1702] for graph knowledge extraction to
[1704] increase its focus on most relevant
[1705] data? [snorts] Yeah, actually pruning
[1709] guided pruning could be could be really
[1711] useful. Yeah. uh to if you if you think
[1714] that if you don't need all the knowledge
[1716] for that and actually um as let's say as
[1720] a more advanced graph rack pattern could
[1722] be that uh this pruning to happen um
[1727] based on the types of questions you
[1728] expect to receive right
[1732] um another question when the domain and
[1734] therefore schema is not fixed it is hard
[1736] to define logical restriction I guess in
[1738] these cases we're restricted to
[1739] heristics and as a judge yes If you if
[1742] you operate in a very open domain indeed
[1745] indeed uh it can be hard to a priori
[1749] define this
[1752] this um what you call them sorry yeah
[1756] these logical restrictions on the other
[1758] hand what I would suggest it could be
[1761] that you know as you do error detection
[1763] as you do sorry error analysis you might
[1765] see some basic patterns of of errors
[1768] that could be prevented by uh enforcing
[1772] a schema later on, right? Or at least a
[1775] a part of the schema, not not
[1777] necessarily the complete one. Okay, I
[1779] think we are done. Thank you very much.
