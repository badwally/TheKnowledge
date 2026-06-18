---
schema_version: 1
id: yt-ebxxK3QWVz8
type: youtube
title: 'NODES 2024 - Graph-Driven Knowledge Retrieval: Neo4j for Healthcare Building
  Codes'
url: https://www.youtube.com/watch?v=ebxxK3QWVz8
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:13Z'
content_hash: sha256:a54b3be4568df058aa64aae4b524c083c346b30e0a51e02b22bd5d3436615829
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 875
  caption_track: fetched
  snippet_count: 339
filter:
  score: 0.8
---
[9] thanks sir hey everybody how's it going
[11] uh thank you so much for being here uh
[13] today I want to talk about my research
[16] on how knowledge crafts and lsmith
[18] evaluators can help improve the
[20] efficiency of a rack system so imagine
[24] you're building a rack system for
[25] healthcare building codes and the model
[27] can confidently returns an answer about
[29] the number of consultation rooms
[31] required but how do you know if it's
[33] actually correct and the reason I bring
[35] this up is because fgi guidelines is is
[39] something that we designers use to
[40] design a hospital building and so the
[44] data in this book is so nuanced that
[46] every time the designer builds the
[49] building designs the building we have to
[51] go to each of these sections and it's
[53] nuanced in a way that sometimes the
[55] sections asks you to go look at other
[58] sections and and so some of the typical
[60] queries of what designers would use his
[63] book as for example the consultation
[65] rooms the answer is 13 but it is a math
[68] question and so you want the llm or the
[71] Iraq system to combine the two answers
[74] and so so the current rack systems today
[77] are pretty good in retrieving relevant
[79] context right uh they're good in
[82] generating fluent responses with with
[84] the help of llms but how do we actually
[87] verify its accuracy and it's critical
[90] especially in healthcare building codes
[92] because sometimes these errors can cost
[94] millions of dollars in construction cost
[98] and so in this presentation we'll look
[100] at different indexing strategies of Lang
[103] Smith's role in testing the evaluation
[106] workflow uh types of evaluation data uh
[110] types of evaluators and some practical
[112] experiments and
[113] results so for indexing strategies I use
[117] three different types of strategies the
[118] first one is the most basic one that you
[120] all know about uh which is the text
[122] splitter so basically uh basically
[125] dividing the document into chunks with
[128] th000 characters and a split of 200
[132] overlap and saving that in the ne 4J
[135] Vector database the second strategy that
[138] I use is a raptor uh Raptor technique
[141] wherein the documents are divided into
[144] chunks which is saved in the database
[146] but the chunks are grouped into clusters
[148] and summaries and each of these
[150] summaries are then saved in the database
[153] but the summaries are then grouped and
[155] further summarized as the main summary
[158] and you know put that in the same
[160] database so it's like three layers of
[162] data that's added as
[164] nodes in the vector database and lastly
[168] the llm based gra graph Transformer
[170] indexing wherein you take the document
[173] you divide it into chunks and these
[175] chunks are saved as nodes which are then
[178] connected with the similarity
[179] relationship
[181] and that is just one layer but there's
[183] another layer where the chunks are then
[185] sent through the graph Transformer with
[187] the help of llms to create entities and
[189] relationships which are then connected
[191] to the nodes from the first level and
[195] this kind of again creates it makes it
[197] more multi directional and the reason
[200] this is good because like I showed
[203] before in the code book the data is not
[207] linear you know it's multi-directional
[209] you would have to go and check in
[210] different sections and so I feel like
[212] this was another good indexing strategy
[216] and so now we come down to lsmith so
[218] what is lsmith so lsmith is an online
[221] platform that helps with debugging
[223] collaborating testing and monitoring L
[226] applications and what is that what does
[228] that actually mean right and before we
[230] go to that I want to talk about three
[232] terminologies that is used in lsmith a
[235] lot and that's run trace and a project
[238] so as you can see the run the bottommost
[241] is a single unit of work so every time
[243] for example in an app a question is
[246] asked and the question is then uh you
[249] know taken to the question is then used
[251] to retrieve data from the retriever so
[253] that is one run and then and so and and
[256] so on and so forth and a collection of
[258] these runs becomes a trace and a
[261] collection of Trace becomes a project
[263] but what is this all mean let me show
[265] you an example so this is a dashboard on
[268] lsmith as you can see this is a project
[271] called Hospital code and each of these
[273] rows are traces and the traces have runs
[277] within them lsmith is good because now
[280] you can check if if the run if the trace
[284] has thrown an arrow as you can tell in
[286] the first four rows there has been some
[287] kind of an error or you can also verify
[290] if whether the data that was retrieved
[293] from the retrievers was accurate so this
[296] is like the basic um dashboard on lsmith
[299] and so if you were to click on one of
[301] those rows you can see one of those
[303] traces which is a row you can see all
[306] the runs that has been done on the back
[308] end once the question was asked so in
[311] this case on the right you can see the
[313] question was are handrails required in
[315] hospital coros and so every once you ask
[319] the question and every step the app
[321] takes to get to the answer can be
[323] checked on the back end to see if it was
[325] done right so this was the question uh
[328] we can then look at what the
[331] prom template is for the llm and in this
[333] case I use open AI we can look at also
[336] the vector uh the data from the vector
[339] stores that have been acquired uh this
[342] is also based on how many uh how many
[345] sets of data that you want and you can
[347] control that I think in this case I've
[349] said five and you can also go through
[351] that uh and finally you can look at how
[354] the data along with the question was
[357] sent in was put into the prompt temp
[360] template and then sent into open AI for
[363] further answering of the question and
[365] then you see the final answer so this is
[367] what Lang does so every time you ask a
[370] question it goes through multiple
[371] different runs and that becomes a trace
[374] and the trace becomes the actual project
[376] so basically it's giving you more
[379] granular uh approach to how you can
[381] control what the output is and that's
[384] what lsmith and lsmith does and helps
[386] quite a
[387] bit uh so let's talk about some of the
[391] evaluation workflows that exist but the
[394] one that I'm using is is the one that is
[397] inbuilt with
[398] lsmith and it's something like this so
[401] you have a data set and when I mean data
[403] set you have a list of questions and
[405] answers and that is the ground truth and
[408] so every time uh to to test the
[410] authenticity of the rag app you send the
[413] same question from the data set to the
[416] rag app and you get an answer as you can
[418] see on the right side but the the
[421] workflow also takes in the answer from
[424] the ground truth and then sends it to
[427] the llm as a judge so this I'm sure
[430] there are multiple different ways to
[431] evaluate the authenticity and verify the
[434] answers so in this case this is known as
[436] llm as a judge and using ground tooth or
[440] data sets as the way to verify the
[445] authenticity of the answers and so there
[447] are different types of data sets that
[449] langsi allows you to put in one of them
[452] is the developer created questions
[454] wherein it's it's a key value pair there
[456] are custom questions and answers related
[458] to the data in the vector store they're
[460] highly curated they're also manually
[462] curate uh created for example as you can
[465] see the question of how many
[467] consultation rooms and that is the right
[469] answer so if you're testing the rag app
[472] with this data set it should be 13
[474] anything beyond that you know is wrong
[477] so this are Developer clear questions
[479] you also have user questions for example
[481] you may have a rag app that is being
[483] that is used in production right now and
[486] when the users ask for questions and
[488] answers you can save as you can as you
[491] can see on the bottom left you can save
[493] the question and the chat history as a
[496] means of ground truth which can then be
[499] which the rag app can later be evaluated
[502] against and the last one is the
[504] synthetic data which is llm created data
[507] sets so three types of data sets and and
[510] so going back to what the workflow looks
[512] like so you have three different types
[513] of data sets you can choose to put any
[515] one of them or you can have all three
[518] and that acts as the ground truth when
[520] you're sending it into the llm as which
[523] acts as a judge and the final output as
[525] you can see on the right side you get
[527] the key you get two two um metrics one
[531] is the score and one is the key which is
[533] the type of evaluators so this is like
[537] the basic workflow that lsmith kind of
[539] look at and so what are the there are
[543] four different kinds of evaluators and
[545] in this case there's document relevance
[548] answer faithfulness answer helpfulness
[550] and answer correctness so all of these
[553] are used with llm as a judge and these
[557] and you provide the prompt to the llm to
[560] you know perform these evaluations and
[563] what are those proms you ask I'll tell
[565] you so document relevance and this is
[568] the prom that you get so all of these
[570] are available on the on the thing called
[573] Hub within L chain uh as you can see on
[576] the bottom of the screen that is the
[579] code to pull in the prom directly into
[582] your eval uh code and so this is the
[586] document relevance wherein it checks for
[588] the facts that are related to the
[590] question so it checks for all of the
[592] data that's been retrieved from the
[593] vector St in relation to the question
[596] faithfulness looks at hallucination and
[598] see if the facts are grounded again in
[601] comparison to the question answer data
[604] set that's that it's comparing against
[606] answer helpfulness looks at how concise
[610] is the answer because sometimes you ask
[612] for a lot of different a lot of context
[615] coming in and so you would want the llm
[617] to give the right amount of data and so
[619] this checks for that and the last one is
[622] correctness in terms of how factually
[625] accurate it is or how close is it to the
[628] key value pairs in in the data sets that
[630] we have so four different types of
[632] evaluators and so the evaluation
[635] workflow essentially looks like this so
[637] you have different types of data sets
[639] and you have different types of indexing
[641] strategies in the bottom obviously I'm
[643] doing this because I want to try and see
[645] which works the best and then you have
[647] four different evaluators for the llm as
[651] a judge so this would be what the
[654] workflow would look like when using L
[656] chain as an
[657] evaluator so I want to sh some of the
[660] outputs based off of the uh experiments
[663] that I did and so for the first one I
[666] want to talk about text spitter using
[668] text splitter as a vector database and
[671] oh no I'm using Neo 4G as Vector
[673] database but using text splitter as
[675] indexing strategy and so once you do
[678] once you do all those runs you get this
[681] dashboard wherein you can get all of the
[684] graphs so there are four different
[685] graphs based on what we spoke about four
[688] different evaluators the document
[690] relevance answer
[692] hallucination answer helpfulness score
[695] and answer reference so each dot on the
[698] graph is the run that that that has
[700] happened so I've done two runs for each
[703] of these and as you can tell the score
[705] is pretty bad and I'll tell you
[707] why so to the original question of how
[710] many consultation rooms were required
[712] for Behavioral and mental health
[713] facility with 152 beds as per that
[717] section it does not actually verify that
[719] it's 13 it just says it you need 12 beds
[723] uh per room right and so it's B it's
[726] basically a math question for the llm to
[728] figure out which that's why I feel like
[730] it kind of failed and so on the right
[733] side you can see the reference input and
[735] the output and that is obtained from the
[737] data set the key value pass and the
[740] output is what the rag app or the rag
[742] system is providing in terms of an
[744] answer and so obviously it does not
[748] match with the output right and so at
[750] the bottom of the screen you can look at
[752] what the document relevance with zero uh
[755] the scale is 0 to one again was 0.0 to
[759] 1.0 and it also shows how many tokens
[761] was used and if it was a success well
[764] it's a success that it went through with
[766] the answer but it was zero and it kind
[769] of failed because it didn't give the
[770] right answer and so we have answer
[774] faithfulness uh which again which was
[777] which shows one in this but it it's not
[780] close to what we want it just is the
[782] right section that it found answer
[785] helpfulness uh does not give the right
[787] answer and answer correctness also does
[789] not give a right answer so that was text
[792] litter in terms of raptor as a indexing
[795] strategy again the same kind of
[797] dashboard with the four different graphs
[799] uh this kind of failed too for the most
[802] part uh answer faithfulness answer
[806] helpfulness it kind of gives answers
[809] related to the section but not the
[812] actual answer that you want uh answer
[815] correctness also so all of these are
[817] zeros uh and the last one is the llm
[821] graph Transformer which I think worked
[823] the best so in terms of document
[825] relevance it was a zero but when it in
[829] terms of answer helpfulness was a zero
[832] as well but in this in terms of answer
[835] correctness it came close it got the
[838] number 10 which I think is wrong because
[841] it should be 12 but it did the math and
[843] was close to giving the answer so you
[846] know it was close but not exactly
[849] accurate but the whole point of these
[852] evaluators was is to try and analyze and
[855] see what systems uh what indexing
[858] systems work well what kind of chunking
[860] works well and so I think in my case
[864] they all fail I definitely have to go
[866] back and find a better way to index the
[869] ENT
[871] book thank you
