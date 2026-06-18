---
schema_version: 1
id: yt-qmfjbrlW2Yc
type: youtube
title: NODES 2024 - Enhancing RAG with Multi-Agent Integration
url: https://www.youtube.com/watch?v=qmfjbrlW2Yc
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:08Z'
content_hash: sha256:0b90a9e0ce19fcbe14ef3d25052b63a3c9270f4873b99d8070a062c35237cd8a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 1223
  caption_track: fetched
  snippet_count: 410
filter:
  score: 0.8
---
[2] Hey, hi everyone. My name is Satage. Um
[5] I work in the role of a principal data
[6] engineer. Uh today we'll be talking
[9] about uh this very unique concept about
[13] you know how about enhancing retrieval
[16] augmented generation uh with multiple
[19] agent integration.
[22] Uh so these are some of the content
[24] elements which we'll be talking about
[26] today.
[27] Starting with the general concept of
[30] retrieval augment generation.
[33] If you all can see her and I think most
[36] of you have an idea about the very
[39] general concept of retrieval augmented
[41] generation but uh in a sense it contains
[46] two particular elements that is your
[49] organizational data which is present in
[52] an embedded database or a token based
[55] system where uh all of your organization
[59] important data related to documents
[62] process processes, business etc. stored
[65] in a document based or embedded database
[69] and which can be first layer where you
[72] are quering for and once you have this
[75] information this particular knowledge
[78] which you're feeding to a large language
[80] model to give you more kind of a natural
[84] language response back to your user. So
[87] that's what a very general retrieval
[90] augmented generation looks like and the
[93] principal advantage of it is that um it
[98] doesn't you know remove hallucination
[100] but it reduces hallucination a kind of
[103] mitigates it by limiting
[106] uh the response by giving a very
[108] customized prompt uh engineering method
[113] along with the contextual data. So it
[115] limits the response to the contextual
[117] data of your organization to sign.
[122] Now rag uh can be applied uh across many
[126] use cases. Some of the general uh are
[130] like some addition conversational AI
[134] question answering and all of this are
[136] very specific. If you're looking for a
[139] generalized model to answer questions
[141] specific to your business model or your
[144] organization.
[148] Now when it comes to large language
[151] models and data quering uh and in
[156] general about
[158] you know generative AI uh the challenges
[162] remain still focused around the concept
[165] of hallucination
[167] where how do we trust the data uh about
[171] the data consistency
[173] and the timeliness of the data whether
[176] the data which we have received is
[178] complete because whenever you're
[181] fetching
[182] data from a particular context in the
[184] rag model uh in the rag framework
[190] your data could be spread across
[192] different components right different
[194] contextual areas it could be around
[196] different documents. So the challenges
[199] lie across different uh you know
[202] horizontal areas where not only you have
[205] to focus upon the particular document
[207] where your data is focused upon but
[210] collect them and also verify
[214] how much uh if you're not missing any
[216] data and it it also depends on your
[219] accuracy of your data because all of
[222] these four elements are key to answer a
[226] particular
[227] question or to get into a solution mode
[232] to help your customers.
[236] And this is where I think uh the
[241] four uh concepts um
[246] come together to solve this particular
[249] challenge. is you have one is the large
[253] language model which gives you the
[254] natural language response. The second is
[257] you have the embedded uh tokens or the
[262] values which store organizational data.
[266] The third is
[268] how does the document relate to your
[272] metadata around your processes your
[275] business. That is what graph databases
[279] bring. The third dimension to this whole
[283] S scenario along with the fourth is how
[286] do you bring algorithmic performance
[290] to search the very contextual data which
[294] is performant which is contextual which
[296] is also relevant to the query. So these
[300] four expects bring the fourdimensional
[304] expect to this search based contextual
[307] searching which helps you answer the
[310] customer queries.
[312] Now now in general this is what the rag
[318] uh architecture looks with the graph
[321] concept right now. Now if you see this
[324] picture here the user questions uh and
[327] we are now searching. Previously the
[330] search was limited to the embedded data
[333] where you know it was tokenized but now
[336] if you see there are two layers to
[338] searching it. The very first is we have
[341] another large language model which takes
[343] the question converts it to a graph
[346] query and we are searching it across a
[349] knowledge graph and this knowledge graph
[352] gives you back you know some more
[354] contextual data. This contextual data
[358] along with the U query is now used to
[360] search for the embedded or the vector
[362] data which gives you more information.
[366] Now this combined information is fetched
[369] and passed to the last language model in
[372] the last section which is then
[377] fed with a prompt uh message to give the
[381] user a answer back.
[384] Now one of the challenges remain is
[387] here too we have you can think about two
[391] large language models like two areas of
[393] failure where eventually large language
[398] models being probabilistic
[400] you eventually have to try it out in
[403] terms to see whether you're getting the
[405] right areas. So the key question around
[408] is how do we test this? How do we enable
[411] you know this retry model?
[414] This is where multi- aent frameworks or
[418] multi- aents come into expect.
[422] uh some of the examples of multi- aent
[424] frameworks in the area C AI, autogen and
[428] there are others also but these have
[430] been a bit uh I could say popular in
[432] terms of how companies and organizations
[435] and uh also around the open-source
[438] frameworking environment
[441] in general talking about a multi- aent
[444] framework it consists of you can think
[446] about two particular area where uh now
[451] If we think about a rag model or a a
[455] very general rag architecture, we can
[458] think about that that as a single agent
[460] like helping a particular query or a
[463] contextual problem.
[466] Now
[467] how about having the same problem but
[471] dividing that problem into all the
[473] challenge into various other aspects
[476] like subdividing it into other very
[480] smaller tasks. So that now
[484] instead of a single agent we have
[486] multiple agents which are now working on
[491] these tasks because they're simpler.
[493] They're more focused around a single
[495] responsibility principle. If you can
[497] take think about from a software
[499] development environment.
[501] Now these agents now focus upon these
[504] particular single tasks which are more
[506] refined which are more contextual. They
[508] can work on this. They are very
[511] independent. They're enabled. They work
[512] in their separate environments and they
[515] can come back with those solutions where
[518] another very centralized kind of a
[521] driver language model takes these
[523] responses and collects all the data and
[526] gives the response back. So that is
[529] where the multi- aent framework
[533] you know architecture lies in.
[539] Just to give you a very brief idea about
[541] how cle AI in general works. So if you
[544] think about there are many AI agents
[546] like large language models and each of
[549] them is working kind of has access to
[553] tools. Tools can be like you have access
[556] to Python interface or the web search,
[558] Google search
[560] where you can make API you know requests
[563] or do further tasks on it and each AI
[567] agent works through a process layer to
[570] en enable or handle a particular task
[573] and gives an outcome back.
[577] Uh here is an example if you can see
[579] let's say and it's a very sample example
[582] which you can find in GitHub crew AI uh
[585] where uh it's kind of a resume finding
[590] application
[592] and if you can think about resume
[594] writing it it contains variety of skills
[597] right the very first is you have to
[598] write through uh your skill sets second
[602] you have to know what are the market
[603] demands uh the third is you have to also
[606] see what are the job skills which are
[608] listed in a particular job description.
[611] So if you think about uh as a human
[613] being we are learning multiple roles in
[617] order to particularly answer or solve
[621] this particular challenge of you know
[623] creating our own resumes. So now if you
[626] see the different agents here and there
[628] have been rules, goals and you know kind
[631] of a backstory for them so that they
[633] have a contextual area around what they
[635] are able to work around. So you can see
[637] there's a research agent, writer agent
[639] and a review agent. So these help you
[642] know kind of the output from one agent
[645] go back to another agent and in the
[649] sequence help you know formalize and
[652] enrich the data so that not only now you
[655] have your organizational data but you
[658] know uh if you have different aspects of
[660] your data which data is relevant compare
[663] it
[664] and and you know further enrich it.
[669] Now this is where we come to the very
[672] final layer when we talk about
[675] integrating graph with the multi- aent
[679] framework. Now if you see here the only
[682] key component now which is introduced
[685] here is the multi- aent framework at the
[689] center which takes control about you
[692] know searching in the graph getting the
[695] data back and then doing the vector
[698] search but this is not limited to the
[701] single process but eventually it also
[704] fetches data from different because now
[707] not only can you do a single graph query
[709] but you can do multiple multiple graph
[711] queries and you have multiple contexts
[713] of data from graph where now this data
[717] can be further filtered uh enriched
[721] and it can be given more context through
[724] prompt engineering because now you have
[726] a particular idea let's say it's a
[728] customer uh success chat which we are
[731] dealing with and we know based on the
[734] customer if they have u let's say it's
[739] more around the payment payment uh
[742] context. So we have the payment logs
[744] maybe the orders which we can fetch data
[747] around from graph uh database for
[750] example neoj and we fetch that data and
[754] now with this data we have more context
[756] around it. So a particular model or you
[759] know an agent uh does the job of you
[762] know searching that graph query getting
[764] the data and then further enriching it
[768] and these models can be very important
[771] because uh now if you think about
[775] in a multi- aent structure you not only
[779] have text data but you could also have
[782] visual data uh like someone getting some
[785] image from a particular data store which
[787] could be independent of your current
[789] framework. So that multistructure
[793] including audio, visual plus texture is
[796] what gives
[798] the graph layer plus the
[802] searching layer from the multi- aenting
[805] framework a very multistructured data
[808] enriching process which gives you the
[811] confidence to retry it. And also the
[815] other key layer which is present here is
[818] to have a human in the loop to improve
[821] the process around you know how can we
[823] improve it because it's two important
[826] layers is the prompt engineering the
[828] retry mechanism with the parallelization
[831] with multi- aent framework and the third
[835] key aspect which enriches is the
[838] knowledge graph network because graph
[840] network helps you to correlate the
[843] networks and gives you some very you
[845] know defined data in which you can
[849] correlate from you know multiple
[852] touch points just
[861] so
[864] that is a very key element which um I
[867] wanted to bring into this discussion
[868] here now the key expect when you try
[873] this is how do we compare it? Now there
[876] have been a variety of evaluation
[878] frameworks where you can delve this but
[881] given my personal experience of the
[883] open-source frameworks and the you know
[885] some of the challenges which I've been
[888] driving uh in my opensource work
[892] the principal element which drives more
[895] performance and efficiency is the graph
[898] network given its validation and the
[901] second expect is the multi- aent
[904] framework.
[905] One of the key question which happens is
[907] where do you have where do you stop you
[910] know because as an agent framework it
[913] can retry
[915] you know as many times. So even if we
[918] have a limitless uh cloud architecture,
[922] we have to be cognizant about you know
[924] the cost aspect of it. That is where
[929] we need to have a human in the loop uh
[932] feedback mechanism where we take
[935] feedback from the you know user in terms
[937] of whether the uh response was helpful
[941] and further fine-tune because I think
[944] fine-tuning also lays a very important
[946] expecttor to gather further structure
[949] into a fine-tune small language models
[954] and the expect here is Even if we
[957] started as an industry towards talking
[959] about LLM that starts with large
[961] language models, we're more focused
[963] right now towards small language models
[967] SLMs which build the overall
[970] architecture for your system which
[973] delivers towards kind of a more
[977] structured, streamlined and more data
[980] efficient systems.
[983] So I think uh this is the key idea and
[986] you know the architectural proposition
[988] which I wanted to bring through this
[990] session. So given we have still uh kind
[993] of four minutes u I would like to you
[997] know thank you all for joining this
[999] session and if there are any questions I
[1001] am ready to answer them.
[1026] Uh so I can take a few questions. Uh and
[1029] the first one I can think about is
[1030] Angelo based on your experience what has
[1033] been the most important early
[1034] consideration a team should focus on
[1036] when architecting such solutions. Uh I I
[1039] think the most important is I think
[1041] think about your data. I think the right
[1043] quality data is very important. The
[1046] second is I think one of the key
[1048] important areas which I focused upon is
[1050] even if your data is present how
[1052] contextual is the data because the same
[1055] query can have some contextuality in
[1057] terms of probabilities in different
[1059] documents. So how do you map the data
[1062] because some sometimes when you you know
[1064] divide your data or you you know
[1068] truncate your data into different small
[1070] documents you leave some of the context.
[1072] So it's very important to overlap some
[1074] data. There are different algorithms you
[1076] know as to how do you correlate in terms
[1079] of vector data. So I think that is a
[1081] very key aspect as to fine-tune your
[1083] prompt uh get your data you know and see
[1088] what are the algorithms you're using in
[1090] particular to fetch those. Yeah.
[1102] So coming to K's question uh how is the
[1105] rag model different from many existing
[1107] tools like Zapio? Uh
[1111] so I think uh even I think Zapio I think
[1115] they also using some variation of these
[1118] models and it all depends upon your
[1120] data. uh one of the key aspects is how
[1123] secure you want your data to be with
[1125] your organization because eventually you
[1127] have to see how Zapio is handling the
[1129] data. So it's very important how do you
[1132] deal with it. uh and
[1136] even though it's rule based for Zapio it
[1138] could be a you know sequence model but
[1141] life language models are more kind of
[1143] driven through you know contextual value
[1146] and not only is it only probabilistic
[1148] but you can bring your own different uh
[1151] I think the the only limit is your
[1153] creativity because with all the tools
[1156] available with all the different areas
[1158] available you can still you know bring
[1160] all these plug-in this architecture all
[1162] together and you know experiment with it
[1165] based on your whole your own contextual
[1168] uh independency in your projects
[1174] uh with relation to orders and or
[1176] langraph which one should be good to go
[1179] even though both work I think you have
[1181] to experiment with it some of these are
[1184] you know I've seen they have a bit of
[1185] challenge in terms of your learning but
[1188] you know try them whichever examples
[1190] which have the best tools available
[1192] because you have to again see how
[1194] independent is it to customize it if you
[1197] don't have a particular you know
[1199] integration towards it so that you can
[1202] it's all about you know bringing
[1203] different tools together so if the
[1205] framework allows you to do that along
[1208] with different examples documentation I
[1210] think that should be a good way to go
[1212] about it uh I'm sorry I may not be able
[1216] to answer all the question but feel free
[1218] to approach me you know later we can
[1221] connect.
