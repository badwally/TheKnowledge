---
schema_version: 1
id: yt-xLjufsJ8NMM
type: youtube
title: The Role of Knowledge Graphs for LLM accuracy in the Enterprise KGC 2024
url: https://www.youtube.com/watch?v=xLjufsJ8NMM
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-17T20:57:29Z'
content_hash: sha256:5ab1b3ddf535a873ab7fc8cef25006c3c4543be7085a9e511a1dd628874a1920
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 2115
  caption_track: fetched
  snippet_count: 987
filter:
  score: 0.8
---
[10] Good. All righty. Um, we got everything
[13] up. Great.
[16] Okay. Next up, uh, it's a pleasure to
[18] get to introduce a good friend Juan
[20] Cicada from Data World. Uh, and
[24] the role of knowledge graphs for LLM
[26] accuracy in the enterprise. I know one
[28] has done very much deep dive on what's
[31] the interaction between LLMs and graphs
[34] very much our theme here today. So
[36] please join me in welcoming Juan. Thank
[38] you.
[40] Hello everybody. Great to be here. Um so
[43] I'll be talking about this paper that we
[45] published uh last year with with my
[48] colleague Dean Elam. I think Dean's here
[50] and uh there's Dean and Brian Jacob.
[52] Who's uh seen this paper and actually
[54] looked it? Okay, we got a handful. Cool.
[56] Okay, so we're going to dive into this
[58] and actually got some special news later
[59] on. So uh to to conclude in case you
[62] need to leave uh in the next uh minute
[65] uh investing in knowledge graphs provide
[67] higher accuracy to LLM powered question
[70] answering systems over structured data
[72] over SQL databases. Right? So the the
[74] the takeaway here is for the research
[76] that we did that we presented here, we
[78] have evidence that we can talk about
[80] three times more accuracy than if you
[82] don't use knowledge graphs. you're
[83] running question answering directly over
[84] SQL databases. So the point is that I
[88] want everybody to take away is that you
[90] need to invest in knowledge graphs to be
[92] to be successful for your AI
[94] applications over your structured data
[96] around this. That means that you need to
[98] start treating your metadata, your
[99] semantics, your context as first class
[101] citizens. And if you don't, you are
[103] going to fail. So don't be a failure. Um
[107] and a lot of this work they presented is
[109] kind of a call out that I want to make
[110] is that we need to have more bridges
[112] between industry and academia. So I I
[114] really haveve been very fortunate. I
[116] come from these both words, both worlds.
[119] So a lot of the work that we're
[119] presenting here has been kind of thanks
[121] to a lot of people who have been
[122] collaborating around this. Um this my I
[125] I build bridges. I like to build from
[127] industry academia and also I host a
[129] podcast catalog and cocktails the honest
[131] no BS uh data podcast that Paco has been
[135] that Ben has been on. We got more folks
[137] and today we're going to do it with Aura
[139] at 5:00 in room 205. You want to see it
[141] at 5 p.m. we're going to do it live.
[144] Okay. Okay, so the research question uh
[146] what we started out so think about over
[149] a year ago right everybody's doing MLMs
[151] and and people are saying oh I can now
[152] generate SQL for this stuff right great
[154] and we start seeing all these very cute
[156] examples but what was what not
[158] understood is to what extent these large
[161] language models can accurately answer
[163] questions over enterprise SQL databases
[167] and then we're all saying in this
[168] community oh we need semantics we need
[170] knowledge graphs that's going to improve
[171] it okay to what extent does that
[173] actually improve. So we don't have these
[176] numbers. We don't understand this very
[177] well. Um so the hypothesis is that if
[181] you actually take an LLM question
[184] answering system and you give it a SQL
[186] database and if you take that questions
[189] over your LLM and you translate it to
[191] queries directly over your over your SQL
[193] database, basically text to SQL and you
[195] compare that to questions over a
[198] knowledge graph. that knowledge that
[200] knowledge graph is a is the knowledge
[201] representation of that SQL database. The
[204] accuracy is going to be higher if it's
[205] over the knowledge graph representation
[206] of your SQL database. So if I were to
[208] kind of think about what a graph would
[210] look like for accuracy, it would look
[211] like this. Questions over the knowledge
[213] are going to be higher higher accuracy.
[216] And what I would love to be able to make
[218] this claim is that by investing in
[220] knowledge graphs, we're going to have
[221] higher accuracy for these question
[222] answering systems. I want evidence to
[224] support this claim. So what happens is
[227] that benchmarks so text to SQL and and
[230] natural language I think natural
[232] accessing data natural language has been
[234] I think probably argue one of the
[236] inspirations for the field of computer
[238] science 60 70 years ago and the area of
[242] text to SQL is not new so just call out
[244] for folks they're thinking that they're
[246] doing the latest craziest stuff latest
[248] coolest things you're not people have
[249] been working on text to SQL for decades
[251] and decades and decades so please read
[255] that history. Now I would argue is that
[258] the benchmarks that DualS does text to
[261] SQL stuff of are fairly academic are
[263] disconnected from reality. So we looked
[265] at this and we said okay first of all we
[267] need to have an enterprise SQL schema
[269] and one that looks into what the real
[271] what what happens in the enterprise. So
[274] the OMG the standard organization has
[276] one about the insurance domain called
[278] the property casualty data model. It's
[279] all open. You can go just Google it OMG
[281] property casualty data model. you can
[283] get the SQL DDL that's there. Second, we
[287] want to understand the enterprise
[288] questions. So, it's not just a laundry
[291] list of questions. There has to be a
[292] reason for these existence of these
[294] questions. And we're going to go through
[294] this quadrant of questions that we have.
[297] Now, the third thing is that we want to
[299] be able to have this context, the
[301] mapping, the semantics, make this
[302] explicit as a first class citizen. That
[305] is this context was not part of existing
[308] benchmarks. So, these are the three kind
[309] of the framework that we're presenting.
[311] Note that we present this benchmark.
[312] It's there. It's public. We want people
[314] to go use it. But I also want you to
[316] take away this as a framework for you to
[318] apply this in your organization. You
[320] already have the your database schemas.
[323] We already had a couple talks about
[325] that. But I want you to start organizing
[327] the questions based on the framework
[328] going to tell you and make this context
[330] explicit too. So this is just the OMG
[335] standard schema right there. You can go
[336] find it, Google it. I'm just showing you
[338] a picture about it. Okay. So the
[340] questions think about it as this
[342] quadrant. So you have two different two
[344] two uh uh uh spectrums of complexity.
[347] One will have a spectrum of complexity
[349] of schemas basically less complex
[352] schemas less tables more complex schemas
[355] more tables. And then let's think about
[357] the complexity of the questions. Easy
[359] questions harder questions. Easy
[361] questions are give me a list of things.
[363] Harder questions, metrics, calculations,
[366] KPIs. So you put these things together,
[368] you get a this quadrant. So hey, return
[370] me all the claims we have by claim
[372] number, open date, close date. Easy
[374] question over over easy scheme. I just
[376] need one table, predict three columns.
[378] Okay, let's increase the complexity of
[380] the question, but still something I can
[381] answer in a small amount of tables. This
[383] is about getting the average time. I
[385] need to do some aggregation, do some
[386] math.
[388] Uh get me the lost payment, the loss
[390] reserve, the expense payments amount,
[391] all these things. It's a list of things
[393] and I probably have to join six, seven
[394] tables to go get that. Now comp high
[397] complex high schema complexity is oh I'm
[399] now doing KPIs talk about to total loss
[402] about loss ratio you need to be able to
[403] combine all these gigantic tables and so
[405] forth so that's the complex so if we in
[409] the benchmark so let's take an example
[411] here the benchmark has the question and
[413] the expected answer given a particular
[415] instance not the query now the reason
[418] why is and this is something I've seen
[420] in other academic work is that there's
[422] an over if you give the query there's an
[423] overemphasis I need to start generating
[425] the query I don't care if you generated
[427] a a a query that executes very quickly
[430] if it's wrong I don't care right it's
[433] wrong so I think if you start focusing
[435] on kind of engineering I'm generating
[436] the right optimized query you're pushing
[438] the focus where it shouldn't be so for
[441] example if I have this particular
[442] question and that in that particular
[444] data instance that is the answer so I'm
[448] just going to go through these are all
[449] the sample questions you can see through
[450] that falls into that complexity into
[452] that quadrant
[454] high uh average time to settle claim
[456] right got to go join all these tables do
[457] a difference between these uh uh the
[460] dates and do an average over that and
[461] that's a particular answer again here
[464] are the types of questions that we have
[465] over this
[468] low question high schema complexity
[470] here's interesting like this is typical
[473] some models and databases right this is
[475] like that claim amount table is one
[477] table has all amounts and then you have
[479] other tables which are like the type
[480] tables you have to go join them to know
[482] which type it is so you have to join all
[484] these things over and over
[487] here are the sample questions. Um, and
[490] then high question, high schema
[491] complexity. I'm joining all these
[493] particular tables together, right? And
[495] total loss, right? That's a very
[497] specific uh insurance uh uh metric which
[500] is needed to be able to calculate what
[501] your loss ratio is. Every single
[502] insurance company knows what their loss
[504] ratio is.
[506] Again, these are the types of questions.
[509] So, the context, we want to make the
[512] context explicit. And to be explicit,
[514] I'm talking about given the ontology,
[516] give me a schema, right? The the target
[517] schema, your semantic layer. I'm using
[519] all these words very interchangeably.
[521] All right? I'm not being any pedantic
[522] around this stuff, right? And the
[524] mapping, how do I com how do I what are
[526] the rules, the mappings that connect the
[528] source to the target. Uh in the
[530] benchmark that we have, which is their
[532] public, we use the open standards that
[535] we're used to, which is RDF and owl and
[537] R2RML. And as we'll talk about, other
[540] people have replicated this. I'm not
[542] saying this is only for RDF just I'm
[544] just doing something standardsbased you
[545] can do with anything else you want any
[547] proprietary tool that you want to go do
[549] this so for example what are these
[551] mappings if I say if I define the the
[554] concept of a claim I can say hey in the
[556] table claim in this case it's a onetoone
[559] mapping the table every single instance
[561] every single row in the table claim maps
[563] to the concept claim and and the company
[565] claim number column actually maps to the
[567] con the attribute called company claim
[569] claim number and so forth So these are
[571] the mappings that happen.
[574] Then here's where we start realizing
[576] that we need to understand what this
[577] stuff means. So policyh holders, how do
[580] I know what is a policy holder? Well,
[581] there's a code and it's called PH,
[583] right? I guess you can hint why the LM
[586] will not know this and that's why
[587] they're not get accurate results. You
[588] need to go invest in this stuff, right?
[591] Uh I need to know what a premium is.
[593] Well, to get the premium, you need to
[595] know that you have to join the policy
[597] amount table and the premium table
[598] together and put this all right. You
[600] just need to know that's the way how to
[602] define what a premium is. So, we're
[603] making this. Remember that the original
[605] claim is investing in semantics. I am
[607] investing in semantics here.
[612] Okay, we're talking about accuracy. What
[614] do we mean by accuracy? How are we
[615] scoring this? So, we're actually using
[617] the term accuracy from uh the spider
[620] benchmark. Spider is from from the folks
[622] at Yale, they have kind of the de facto
[625] model, right? The de facto benchmark
[627] around things. What's fascinating about
[628] that is you look at the benchmark,
[630] they're like, "Oh, 98%." I'm like,
[631] "Really?" Yeah. What's if you look at
[634] the t the tables and the and the
[635] questions they have, it's kind of
[636] disconnected from reality. I mean, if
[638] you look at those benchmark, you're
[639] saying, "Oh, this is 98%. You're saying
[641] this is a solved problem." It's
[642] obviously not a solved problem. So,
[643] there's a disconnect over there. Now,
[645] what is an execution accur accuracy
[647] metric? Is it's basically a binary
[649] decision. it's right or it's wrong. The
[652] columns the column labels are not
[654] considered and the order of the columns
[656] are not considered. So for example, if I
[659] say given this question return all the
[661] claims we have by claim number, open
[662] date and close date and this is the
[663] expected answer and I get this I get I
[667] generate a query that generates this
[669] result. The labels are different. The
[672] orders of the columns are different. The
[673] orders of the row are different. It's
[674] still a valid it's a it's still an
[676] accurate answer. However, if I get this
[679] particular answer back, I generate a
[682] query that generates this answer, the
[684] claim number, you see it's one and two,
[685] doesn't map, then the this is an
[687] inaccurate answer. Now,
[691] LLMs are undeterministic, right? So, if
[694] I ask a question once and generates a
[696] query, I could ask it again and may
[697] generate the same query, may generate a
[698] different query. So, we need to have we
[701] need to be able to go deal with this. So
[702] we have this notion of an overall
[704] execution accuracy is that we run the
[706] question over and over over again and
[707] then we just uh divide the number of
[710] execution accuracies over the total
[711] number of of of runs. So if I ran the
[714] question 10 times and 10 times generated
[715] a query that generated uh always correct
[718] it has a 100%. If generated 10 times and
[721] five times it was right it has a 50%.
[724] And then finally I can take all those
[726] overall execution accuracies and I in a
[728] bucket I'm saying hey I want to look at
[729] it for all questions or for quadrant and
[731] I can do that average and that's how I
[732] could get an average for every quadrant.
[735] Okay so now the setup
[738] um we did something very very simple on
[742] purpose because we want to understand
[744] the baseline. Second, I'll also argue
[747] that we like to overengineer things and
[750] we kind of think automatically believe
[752] that that simple thing is not going to
[753] work even though we've never tested it.
[755] So, first of all, this is the the the
[758] the two kind of comparisons that we
[760] have. We have a zeroot prompt.
[763] Literally, it's this. The following is a
[766] SQL DDL. Boom. Paste it in. Write a SQL
[771] query for the following question.
[773] That's it. The following is an owl
[775] ontology and turtle syntax. Boom. You
[777] just paste that owl turtle syntax in
[779] there. Write a sparkle query for the
[781] following question. That is it. The
[782] results I'm going to present is using
[784] that very simple zeroot prompt. So you
[787] can imagine that we can get even more
[788] sophisticated with after these results.
[791] So with that prompt what you see on the
[793] right side right there, you get that
[795] question the DDL goes into that zero
[797] shot prompt. It generates goes into GBD4
[800] which is what we tested. Generates a SQL
[801] query. execute it, get the results back.
[803] For the knowledge graph, we took the
[806] mappings and we virtualized this. So
[808] this we used data.worlds virtualization.
[810] You could have materialized this into an
[812] RDF graph and just run it. But that
[813] we're just using the tools that we have.
[815] Uh so it takes a sparkle. Note that the
[817] the SQL that comes out of the
[818] virtualization that's deterministic
[820] because that's just now part of the
[821] engine that does the sparkle to SQL
[822] using the mappings.
[824] Uh when we the results that we
[826] presented, we ran this over a couple of
[827] weeks back in September October. uh so
[830] everything has between 30 to to to 330
[832] uh uh runs. So the results
[837] this is the overall results we have. So
[838] if you take all the questions that we
[840] have so it's around 40 questions 10 in
[842] each quadrant um with that very simple
[845] prompt after investing in in the
[847] semantics investing in that mapping in
[848] the ontologies we have 54% accuracy
[851] compared to 16 that's over three times
[853] more just again with that very simple
[856] prompt no vector databases nothing just
[859] super simple on purpose again just try
[861] to get this very bare minimum but we we
[865] did the investment in the semantics
[868] now Obviously, the devil's in the
[869] details. So, let's go into this. First
[870] of all, remember that you have this
[873] overall uh execution accuracy. So, this
[876] is a kind of this is a heat map that
[877] would shows the things that were
[880] if I did a 100 runs like 100% means that
[883] every single time it ran it got it
[885] correct, right? You can start seeing
[886] kind of these differences. Why did it
[888] get it right sometimes? Why did it get
[889] wrong sometimes? Who knows? I don't know
[892] what's happening inside these mach these
[894] models, right? Nobody knows. Again, what
[897] can we interpret? There's a lot of like
[899] unknowns in here and I think that's
[900] going to be interesting to understand
[901] what's happening inside of an L1. Now,
[904] let's look at the quadrants.
[912] So, what we saw here is that this low
[915] schema to high schema complexity is five
[917] tables. And actually, this is pretty
[920] consistent with the with folks that I've
[921] been talking to at at all the big
[924] database vendors that when they're doing
[925] their their now their co-pilots, right,
[927] their text to SQL stuff, they're really
[929] constraining it to a to smaller hand of
[932] tables because the moment that you start
[933] increasing it, you're going to get all
[934] these hallucinations and all these
[936] things. Um, and these co-pilots, right,
[939] people are doing all this stuff. Look,
[941] if you are a technical user and you're
[943] writing SQL query for someone knows SQL,
[945] it's fine if it's not fully accurate
[946] because like the query itself is not
[949] accurate, but probably the content of
[951] that query I don't know 80% whatever is
[954] accurate and that is better than
[955] starting from scratch. So I mean that's
[957] the claim and we're going to actually
[958] see how much it's actually these
[959] co-pilots are actually going to improve
[960] improve productivity. But so this is the
[964] this is this is already what we're
[966] seeing kind of from the low schema
[968] complexities the low schema complexities
[970] we're getting much higher accuracy
[972] already again with that very simple
[974] prompt
[976] uh again we can go see this with this
[977] heat map approach too to go now what's
[981] interesting is science right remember
[984] science is a social process
[987] peer reviewing get people out there but
[989] also what's what is fantastic is when
[992] other people reproduce their work and
[994] valid get validate the results. So like
[997] after we published this the folks at DBT
[1000] they're not they're using semantic
[1002] layers not specifically graphs or stuff
[1003] they validated they reproduced and
[1005] validated the results and other
[1006] different semantic layer companies have
[1008] been doing the same thing. can imagine
[1010] semantic layer companies even though
[1011] they don't do that much with graphs
[1013] they're now using the word graphs a lot
[1015] right uh and also they're like finally
[1018] it's our day right we can do this right
[1019] so they're really really excited about
[1020] this I think all the semantic layer
[1022] companies that I'm aware of have
[1023] reproduced our results and I'm seeing
[1024] things saying oh 99% like great if
[1027] you're 99% you're doing something
[1029] because nothing is perfect in life so
[1033] but what's interesting is to understand
[1034] why things are wrong so let one of the
[1037] when we start manually looking at the
[1038] results and why things are wrong is
[1040] partially accurate results. I want to
[1042] talk about this is are when the results
[1044] you're like uh it's not completely
[1047] wrong. I didn't get the complete exact
[1049] expected answer but it was almost there.
[1051] So I kind of should have gotten some
[1052] partial credit which means like there
[1054] was an overlap like you gave me a subset
[1056] of the stuff or sometimes you gave me
[1058] identifiers. So for example these are
[1060] queries that got zero points basically
[1063] but they were kind of right. Right. If
[1065] you actually give in a user experience,
[1067] so you give this back to a user, you can
[1068] say, "Hey, you forgot the identifier or
[1071] something, give me the actual number and
[1072] then you can kind of reprompt it again."
[1074] So you should have gotten some some
[1076] results around that. But inaccurate
[1078] results, why were things completely
[1080] wrong
[1081] on the SQL side? It was just
[1083] hallucinating column names, right? Just
[1086] making up names that didn't exist. Uh
[1088] obviously didn't know the values, right?
[1090] You had to know that this code was PH
[1092] for the policy holder. obviously would
[1094] not didn't know that it would put use
[1096] the word policy holder and if you by
[1098] chance use that term then it could have
[1099] worked but no and then it would just
[1101] hallucinate joins it would generate a
[1103] bunch of joins that would actually work
[1105] sometimes and but didn't it would return
[1107] no results or return results but they
[1109] were wrong ones what was fascinating is
[1112] that when the sparkle queries the when
[1115] there were incorrect results it just
[1116] didn't follow the path it went from A to
[1119] C instead of saying the ontology says
[1122] you have to go from A to B and B to C or
[1125] the edges from A to B and it went from B
[1127] to A. So it kind of got the paths mixed
[1130] up. By the way, a hypothesis I have
[1133] around this is that uh the reason why it
[1137] does the the the knowledge graph or
[1139] sparkle and I haven't tested myself in
[1141] cipher but what you can what you can
[1142] tell it's looking it's also pretty well
[1143] is it's like language right English
[1147] subject verb object node edge node
[1150] subject triples. So it's kind of really
[1152] it's it's it's really very similar
[1154] there. Uh that's number one. Second is
[1156] because the relationships are first
[1158] class citizens. They're very explicit in
[1161] the graph. Well, in SQL databases,
[1164] they're implicit. They're in the
[1165] combination of these two columnies,
[1167] these two tables. Uh and third, I would
[1170] argue that for when it comes to Sparkle,
[1173] the variable names can be anything. So
[1175] you actually give it a little bit of a
[1176] liberty to be creative. So it can come
[1179] up with variable names that doesn't
[1180] matter. It can be whatever. So I think
[1182] that's where it gives a little bit of
[1183] room to to to hallucinate and but it
[1186] still works. Again I don't have uh ways
[1189] to support this but but I kind of things
[1191] that I think about. So let's look at it.
[1193] These are actually questions and the the
[1195] generated queries given given those
[1197] prompts. Return all policies and their
[1199] policy holders. Obviously that was a
[1200] hallucinated value. You can see here
[1202] that I asked for the policy number and
[1205] it returned the the IRI the identifier
[1207] for the policy. So that's why it gets it
[1209] incorrect. So, it's a partial accurate.
[1211] What is the total amount of premiums
[1213] that a policy holder has paid by policy
[1215] number? That was a um hallucinated
[1217] column. This was almost correct. Note
[1220] that I asked by policy holder. The body
[1223] of the query is correct. It actually
[1225] includes policy holder. It just didn't
[1226] project it. So, this is pretty
[1229] fascinating how it gets this. Right?
[1230] This was a simple one, right? It assumed
[1234] that the claim identifier column was the
[1236] actual the claim number, but that's not
[1237] the claim number. That's an internal
[1239] primary key.
[1240] What are all the premiums that have been
[1242] paid by policy holders? Been paid.
[1244] That's the wrong code. That's correct.
[1246] Look at this. What is the total loss of
[1248] each claim by claim? That's the
[1250] question. And I passed it the ontology
[1252] and internal syntax and it generated the
[1254] right sparkle query. This is pretty damn
[1256] cool.
[1258] Uh this is when uh it got it got the the
[1261] direction wrong, right? So we think
[1263] about policies and claims but in reality
[1265] you have a coverage and the claim is
[1267] against the coverage and the coverage
[1269] and and you and you have your policy has
[1271] a bunch of coverages. So that's that
[1272] coverage concept in the middle. So here
[1274] it went directly from the policy of the
[1275] premium.
[1277] So we started with this question to what
[1280] to what extent can the the accuracy so
[1282] we have an answer the answer well
[1287] 16% to 54% so three times more and we
[1290] get it for all these different quadrants
[1291] and I kind of if we visualize it this
[1293] way we can kind of see this extent that
[1295] I'm talking about
[1297] now
[1299] we started off with this this is what I
[1301] wanted to get to right this was a
[1302] hypothesis I'm presenting strong
[1305] evidence to support this so I feel very
[1307] comfortable from a scientific point of
[1308] view as a scientist to make this claim
[1310] now. So you can all make this claim. I
[1313] really want everybody to take away to
[1315] start investing your semantics. And for
[1317] people who are struggling to get buy in
[1319] internally to why we need to invest in
[1321] semantics, here's your evidence to go
[1323] present to your to to to your
[1324] stakeholders. Now one more thing
[1328] we are so I run I head the AI lab at
[1332] data.world world and we're very open on
[1335] the work that we're doing. We're
[1336] actually a public benefit corporation,
[1338] right? So, as a public benefit
[1340] corporation, we are our goal is to be
[1342] able to go to to share all the work that
[1344] we're doing, right? We have we have a
[1345] public benefit mission. So, not only sh
[1347] maximize shareholder value but also
[1348] support our public benefit mission. So,
[1350] that's why we're doing all this research
[1351] and we're presenting this all to the
[1352] world. And the latest research that
[1354] we've done is what we're calling on
[1357] semantic query check. So this is
[1358] literally I'm first time I'm talking
[1360] about this like I actually did the
[1362] analysis that this is stuff that Dean
[1364] was doing and I did all the finished the
[1366] analysis on my plane last night and I
[1369] don't think Dean you've actually I send
[1371] a slack I sent a slack to everybody like
[1373] 11 p.m. last night. So you have not even
[1376] so you're seeing this for the first time
[1377] this final analysis. So um so ontologies
[1381] to the rescue here it's well defined the
[1384] semantics well defined policy is sold by
[1386] an agent which in code I say there is
[1390] this property called sold by it has a
[1392] domain policy has a a range agent. So if
[1396] I ask a question return all the policy
[1398] that an agent sold and the LLM generates
[1401] a query like this
[1404] is syntactically correct query it will
[1406] run it will execute it will return zero
[1409] results but it's semantically incorrect.
[1414] Why is it incorrect?
[1419] Why is it incorrect? Yeah,
[1422] exactly. Because X is a agent which is
[1426] the domain of sold by but it should be a
[1428] policy. So this was the types of issues
[1430] that we were seeing that the LLM was
[1432] generating. So what we said is like wait
[1435] this is semantics well defined.
[1437] Basically we're just using the RDFS
[1439] inferencing rules of domain ranges of
[1441] ranges and so forth. So this was the the
[1444] insight that we had is like well we can
[1445] actually check this deterministically.
[1448] So now when when we talk about these
[1451] co-pilots which are like oh you got a
[1453] question get get a querying where the
[1454] LLM is like the center of things we're
[1456] really moving into like the agent world
[1458] right and by the way everybody's talking
[1459] about agents this is not new people the
[1461] agents also has been the thing for 40 50
[1463] years on planning so all the young folks
[1465] in the audience who are thinking about
[1466] agents the latest coolest thing please
[1467] read like your old AI textbooks because
[1470] this is not new and don't reinvent the
[1472] freaking wheel let's advance faster
[1473] anyways my my old man grumpy hat off now
[1476] okay thank you thank you okay need
[1477] needed to get up. So planning like we
[1480] could create a mach state machines that
[1482] has a plan and one of those plans is I
[1484] get I'm going to ask LLMs to go do
[1487] things. I can then check my work. I can
[1489] check my work deterministically. So what
[1491] we've done is that actually taken a a
[1494] series of all these uh inferencing rules
[1496] of the semantics of of RDFS and do a
[1499] check and we're checking the body of the
[1501] rule the body of the query to say does
[1503] the resulting query match the semantics
[1506] the intention of the ontology and if it
[1509] doesn't and we can check that
[1510] deterministically and if it doesn't we
[1513] know why
[1515] the domain is wrong it contradicts so we
[1518] can actually check it and now what's
[1520] interesting is could we actually fix it?
[1523] I know why it's wrong. I can actually
[1525] write an explanation and I got this
[1527] really amazing friend called LM GPT,
[1530] whatever you want to call it. I can tell
[1532] it and I'm like, "Hey, this query is
[1534] wrong for the following reasons. Can you
[1536] please fix it?" So, we've checked, we
[1539] have these two things. We have our
[1540] semantic query checker and we also have
[1542] our LLM repair. So, just I know a couple
[1545] minutes I'm wrapping up here. So, we've
[1547] put these stuff together and what's
[1549] interesting is that now we can have
[1550] accurate results. We can still have
[1552] inaccurate results. And the reason why
[1553] we've seen inaccurate results is because
[1555] we're checking the body of the query,
[1557] not the head of the query. So, maybe I'm
[1558] returning some stuff in the head which
[1559] is wrong. But also, I could try to
[1562] repair and not decide, hey, I've tried
[1564] so many times, I still don't know. So,
[1566] guess what? Three valued logic. Yes, no,
[1569] and I don't know. And I don't know is a
[1571] perfectly valid answer. So putting this
[1574] together, the next question that we have
[1576] is to what extent can the ontology of
[1578] the knowledge graph and the LLM itself
[1580] be used to repair the errors in the
[1583] sparkle query that that it generated
[1585] itself. So you can actually further
[1586] increase the accuracy. So with we have
[1589] like a series of five six rules from the
[1591] from the from the RDFS uh uh uh
[1594] inferencing rules.
[1596] We jump from 54% to 72 and look how
[1599] every single quadrant improved.
[1603] Now if we check the unknowns
[1606] it actually decides I don't know I could
[1608] not fix this after three times four
[1610] times I forget how many things we did
[1611] it.
[1613] So the ultimate error rate that we have
[1615] right now is around 20%. And actually
[1618] for the low questions low schema
[1619] complexity we're at an error rate of
[1621] only 10%.
[1623] By the way this is still with the
[1624] simplest prompt. No nothing freaking
[1627] sophisticated.
[1629] Now, let's go add more and make this
[1631] better and better.
[1633] So, uh, just to wrap up, this is just a
[1636] piece of the work that we've done. We've
[1638] added this inside of our new AI context
[1640] engine. Like, but I'm super excited,
[1642] fascinated. I can take all this stuff
[1643] from our lab and our research, test this
[1645] out with customers, do hackathons, and
[1647] we plugging it back into the product.
[1649] So, it's really, really cool. And the
[1650] way that we are doing this is that our
[1652] the data catalog that we talked about
[1654] before is the context of your
[1655] organization. And that's how we build
[1656] this knowledge graph. We built the
[1658] knowledge from all the context of all
[1659] the technical and your business
[1660] metadata. You have your large language
[1662] models that we're combining and together
[1665] we built a series of these agents. We
[1667] have the question answering agent that
[1669] can all this stuff. We're working on
[1670] knowledge engineering agents that can
[1672] help me create the mappings and we're
[1673] doing a series of agents around this.
[1675] And that is what this AI context engine
[1677] is we're doing. And I'm just super
[1679] thrilled, excited that we can just take
[1681] this research that we've been doing and
[1683] as actually in the opening presentation
[1685] today stand on the shoulders of giants
[1688] folks in this community have been doing
[1689] things folks who are in that wall over
[1690] here. This is all the combination of
[1693] stat statistical and symbolic AI right
[1697] so to conclude invest in knowledge
[1700] graphs you want to provide higher
[1701] accuracy for LM power question answering
[1703] systems it's three times more for our
[1706] previous result but this is increasing
[1708] and it's more
[1710] knowledge graphs are requirement for
[1712] your enterprise AI
[1714] um please treat and treat semantics
[1718] knowledge with the respect it deserves
[1719] treat as a first class citizen
[1721] And with that, thank you very much.
[1728] Yeah, I mean, I took the liberty of
[1730] going out because I have Yeah, we're up
[1732] on lunch. Let's have a couple questions
[1734] start out.
[1736] Yeah, great work. I read it back when
[1738] you published it. Happy to see presented
[1741] with so much passion. Uh
[1744] my question is you touched on this. uh
[1747] but to what extent ch when when you give
[1750] chpt an ontology it assumes that uh the
[1756] sparkle engine underneath will do
[1759] reasoning.
[1761] Oh, at this moment we're not No, no, no,
[1763] no, no. Uh, the example that I saw
[1765] playing with wiki data is okay, it knows
[1768] the semantics, I mean the basic things
[1770] about the schema, properties, classes,
[1772] whatever. And then when it generates
[1774] queries, it assumes that you uh do
[1778] transitive closure of type over subclass
[1783] and stuff like this. And and it assumes
[1786] that you have done subproperties, right?
[1790] And the query that it generates
[1792] are written as if
[1795] the reasoning works underneath. And so
[1797] in your case, did you observe anything
[1799] like that? We did not.
[1803] Well,
[1806] yeah. Yeah. So the point is that in in
[1808] this benchmark the ontology is doesn't
[1810] have the semantics are just basically
[1812] RDFS, right? So even there's not a lot
[1815] of subclassing and subpropying in this
[1817] ontology to begin with. So it's not
[1819] going to tickle that very easily. So we
[1821] probably didn't see it because
[1823] morphontology doesn't do that
[1827] actually
[1835] a quick one. So totally you know on
[1838] board and and and agree with you and I
[1840] know you're a big proponent of semantics
[1842] first world. So what you describe is a
[1844] kind of a corrective approach. I mean
[1846] someone sometime defined the notion of a
[1848] policy holder and when they implemented
[1850] as a relational database it ended up
[1852] buried in a so how I have the impression
[1855] that if instead of approaching this as a
[1857] corrective action if we build it in the
[1858] process of construction that will be a
[1861] lot more efficient what are your
[1862] thoughts on that I mean how do we build
[1863] it in into the process in the
[1865] construction so that we don't have to go
[1866] and and extract it and and rectify the
[1868] problem afterwards yeah fully agreed and
[1871] I think
[1873] my first answer is everybody should read
[1875] Dave Mcone's book on software wasteland
[1877] and the datacentric revolution, right?
[1879] And convince themselves to go do that. I
[1880] think it's more of a it's a social
[1882] cultural issue to go do that. Why why do
[1885] we do things so ugly? Because we're
[1886] incentivized was what my this is my
[1888] rant. We're incentivized to be efficient
[1889] and not resilient. You're describing a
[1891] very resilient and smart world, but
[1893] people are incentivized to be efficient
[1895] and do things very quickly and fast. So,
[1898] so fast is throwing at the wall and
[1900] see what sticks and stuck and then then
[1901] I jump out of my next job. So, got to
[1903] change those incentives. So
[1906] well and this is this is great to see
[1908] and it's already had a pretty big impact
[1910] in the uh language large language
[1912] community and the knowledge graph
[1914] community within life sciences. So kudos
[1916] to you guys. Thank you. Um my question
[1918] is you know you know the life science
[1920] domain and you know that our ontologies
[1922] are a mess. Um how how would this change
[1926] potentially if I put say NCI thesaurus
[1928] which is not that formalized but is
[1930] heavily used right in the middle of
[1931] that? What do you what do you think's
[1933] going to be the outcome there?
[1936] Uh
[1939] bashing all that fantastic work for
[1941] years and years. I'll take the blame for
[1943] that one. Actually, I'm going to throw
[1944] that to my colleague Dean in the back.
[1949] Well, first off, things like the NCI
[1951] thesaurus don't act like ontologies in
[1953] the way that things like Vibo do. You
[1955] understand what I mean by that? So, it's
[1956] kind of the wrong category. Having said
[1958] that, that's sorry rest of the room. And
[1959] we don't have much time about that, but
[1960] you know what I mean. The thesaurus, you
[1963] can call it a thesaurus. Makes a lot
[1965] more sense as if you were to treat it as
[1966] a glossery. And what Juan hasn't talked
[1968] about is how we go back to the data
[1970] catalog and say, gee, what are the uses
[1974] of compounds like glyphosate? I'm use
[1976] kebby because I know it by heart. So you
[1979] could go into there and say, well, wait
[1980] a minute. Kebby or glyphosate, that's a
[1982] that's a term. Kebie, that's a term. Now
[1985] that query becomes
[1987] glyphosate has use what and the right
[1991] answer is pesticide or actually it's
[1993] herbicide. So if you use it as data
[1996] instead of as structure Juan's talking
[1998] about structure and that's the problem
[2000] with the oboontology. Some are
[2001] structural and some are data and so the
[2003] ones that are data should really be
[2004] treated instead. And you even use the
[2006] word as a thesaurus. When you do that
[2008] there's a whole different way to talk
[2009] about it. That's not the topic of Juan's
[2011] talk, but it is the topic of our product
[2014] where we actually bring the glossery in
[2016] at in a different phase of the story
[2018] here. That's all I can say right now.
[2019] We're way out of time. To add a little
[2021] bit to this, I think for the context of
[2023] expand in things that we've actually
[2024] done now is if you search for something
[2026] like a metric, call it active users. How
[2029] many active users does a company does
[2031] does or company X have? Right? Well,
[2033] what do you define as active users?
[2035] Well, maybe you have a definition in
[2037] your glossery in your data catalog says
[2039] an active user means a user who has been
[2042] to the website two times this blah blah
[2044] blah some formula and it could be just
[2046] in English. So what happens is that when
[2048] you ask a question part of the agent
[2050] framework should say oh do I know all
[2051] these things about this? Oh this exists
[2053] in the ontology that has a mapping this
[2054] thing doesn't exist in ontology but it
[2056] exists in the glossery and it has this
[2058] definition. Maybe I can use that to
[2060] rephrase the question and let me go
[2061] rephrase it back. Hey user, I'm
[2063] rephrasing this. Does this look good? Oh
[2064] yes, try it again. Oh, now I have all
[2067] those new things that showed up in that
[2068] in the in the definition in the new
[2070] definition that I looked up from the
[2071] glossery. Those have mappings to it. I
[2073] can go execute that. So that's actually
[2075] something that we've already done. I
[2076] mean again that's out outside of the lab
[2079] too. That's already inside of our
[2080] product. And I think that is why the
[2083] catalog and just like good old good old
[2086] metadata management and glossery is
[2089] critical for these things too. And then
[2091] all of that would also be indexed and
[2092] that would go into a vector database and
[2094] go find it. And what you want from the
[2095] vector is to get back your identifiers,
[2097] your eyes and that's what you're going
[2098] to be using. So we could also talk about
[2101] semantic random walks if you want to go
[2103] off sidebar about this too. Um I think
[2106] we should probably head to lunch or at
[2108] least take questions offline. Yeah, I'm
[2109] I'm here for the rest of the day and
[2111] Dean and I are going to be around so
[2112] happy to Thank you very much. Juan. All
[2113] right.
