---
schema_version: 1
id: yt-RZbSCbMr1es
type: youtube
title: Q²Forge Minting Competency Questions and SPARQL Queries for Question-Answering
  Over Knowledge Graphs
url: https://www.youtube.com/watch?v=RZbSCbMr1es
authors:
- Wimmics Inria
ingested_at: '2026-06-17T20:57:23Z'
content_hash: sha256:0d27797752ebf59f23ecd4188393581a916086d6632cb518d53aa411754a0038
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Wimmics Inria
  channel_url: https://www.youtube.com/@wimmicsinria3092
  duration_seconds: 1220
  caption_track: fetched
  snippet_count: 491
filter:
  score: 0.85
---
[1] Hi, I'm Frank Michelle from University
[3] Gazour CNS in France. Uh, this video is
[8] a replay of a presentation I gave in
[10] December 2025 at KCAP, the knowledge
[13] capture conference. And the title goes
[16] like this
[20] to forge mining competency questions and
[23] sparkle queries for question answering
[25] over knowledge graphs.
[27] So I'd like to start uh this
[30] presentation with a few words about what
[32] it takes to make a knowledge graph
[34] reusable. As you know there are lots of
[36] public knowledge graphs available on the
[38] web. You can get them from the linked
[40] open data cloud cloud or from from data
[43] portals and usually they come with
[46] metadatabased description uh that
[49] includes the authors, the date of
[51] publication, the title, maybe keywords
[54] uh the domains that pertain to a license
[57] and so on and so on. And usually these
[59] met data are sufficient to enable a
[62] certain degree of fairness. But when it
[65] comes to actually reuse a knowledge
[68] graph, you need more than that. And what
[70] you would typically like to get is a set
[72] of competency questions. That is natural
[75] language questions that will give you an
[77] idea of the questions that the graph can
[79] help you answer. But al that's not the
[83] only thing you would like to get uh a
[85] description of the data model. That is
[87] what are the ontologies that are being
[89] used in the graph and how they are used.
[91] And uh ideally that would come with also
[95] sparkle queries, example sparkle queries
[98] because as you know it's much easier to
[100] start from existing sparkle queries in
[102] the tapdom than crafting new ones from
[104] your from your own. Um and typically you
[108] will also need them to translate
[109] competency questions into sparkle
[111] queries and as you know this requires a
[113] double expertise. One which is about the
[116] domain of the knowledge graph itself and
[117] the second one which is about sparkle
[119] and cement web technologies in
[121] chuggable. So if you don't have all of
[124] that, you would typically start
[126] exploring the knowledge graph with uh
[129] prototypical sparkle queries to figure
[131] out what's in the data. And that will
[134] give you a fair idea of what's in the
[137] graph. And from there you will try to
[139] start figuring out some questions that
[141] experts would like to ask about this
[143] knowledge graph. And then you will need
[146] to translate those questions into
[148] sparkle. But that's quite a t time
[150] consuming task. So you would decide to
[153] train or fine-tune maybe a language
[155] model to do that for you. That is
[157] translate a natural language question
[159] into an accurate sparkle query. But to
[161] do that to train to fine-tune this model
[164] you will need more examples of query and
[168] question and query pairs. And the
[170] problem is that there are quite little
[172] such data sets of question inquiry pairs
[175] and they usually have a rather limited
[178] scope that is there often pertain either
[180] to DBP or wiki data but they are not
[183] necessarily adaptable and applicable to
[185] any kind of knowledge of knowledge
[187] graph. So to address those issues we
[191] have designed a framework that we call
[193] QForge that seeks to address several
[195] goals. The first one is to create data
[198] sets of question and query pairs that is
[202] a natural language question and
[204] equivalent sparkle query pairs that we
[206] call Q2 sets and the Q2 in Q to forge
[209] stands for question query. So you can
[211] read it as question query forge.
[214] Um QFO forge also seeks to address
[218] several use cases. The first one would
[220] be if you're a knowledge graph
[222] publisher, you could use Q to Forge to
[224] document your knowledge graph first of
[226] all with competency questions, but
[228] ideally also with sparkle queries,
[230] example sparkle queries that may or may
[232] not be the equivalent of the the
[234] competency questions that you you
[236] provide. As a knowledge graph consumer,
[239] you would typically use QFO forge to
[242] help you formulate queries and and and
[245] translate existing questions that you
[247] have into accurate sparkle queries. And
[251] if you would are developing a query
[253] answering system, you would typically
[256] use QForge to train and benchmark
[258] translation models or conversational
[260] agents and so on. And again, to do that,
[263] you would need data sets of question
[264] query pairs. Um finally QForge is a
[268] framework but it's also a pipeline and
[271] we intend to make this pipeline generic
[273] that is it would be able to be
[276] applicable to to apply to any kind of
[278] knowledge graph or any kind at least RDF
[281] knowledge graph with a sparkle endpoint
[283] but uh in any kind of domain it should
[286] be extensible that is there are some
[289] predefined steps in the pipeline of Q
[291] toge but you could add your own your own
[293] steps or also replace existing steps
[296] with Euron implementation. The pipeline
[298] is also end to end that is it goes from
[300] the creation of a competency question to
[303] the creation of an equivalent sparkle
[306] query its execution and refinement. But
[309] pipeline also intends to be flexible.
[311] That is you're not locked into a whole
[313] pipeline from which in which you need to
[316] go from the beginning to the end. You
[317] can pick up just one of the tasks in the
[320] pipeline, execute it with your input,
[322] get the output and do something else
[324] with that.
[326] And basically Q to forge implements
[329] three main tasks that are all assisted
[331] by language models. May they be large on
[334] small this or or small. This is
[335] configurable. The first one like I said
[338] will be to create competency questions.
[340] The second one will be to translate
[342] questions possibly those competency
[344] questions or some other questions that
[346] you have into counterpart sparkle
[348] queries. And the last part the last task
[351] will be to verify and refine the sparkle
[354] queries that have been generated.
[357] So now I'll present the different steps
[359] of the pipeline.
[362] So the first step will be to create a
[364] knowledge graph configuration where you
[366] will provide some minimal information
[368] about the target knowledge graph. That
[371] would be a name, description, sparkle
[373] endpoint, the name spaces and prefixes
[375] that you would like to use in the
[377] sparkled queries. Typically there are
[379] also some additional parameters that are
[382] not configurable through this interface
[384] but through the back end directly uh and
[387] these pertain typically to the language
[389] models that you would like to use in the
[392] different steps and how you assign those
[394] models to each and every step of the of
[396] the pipeline.
[398] Uh once we have this configuration we
[401] will start with doing a bit of
[402] pre-processing that we we will extract
[405] some important information from the
[407] knowledge graph and typically that will
[409] consist in extracting a test textual
[411] description of the classes and
[413] properties that are being used in the
[415] knowledge graph and we will use that
[417] later.
[419] The second step will be the first real
[422] big task that you would be interested in
[424] which is the generation of competency
[426] questions. So here we'll generate the
[428] competency questions and optionally
[430] optionally export them for use with
[432] another tool and [clears throat] here is
[435] how the interface interface looks like.
[437] So basically we will prompt a language
[440] model providing it with some information
[442] that you have already given in the
[444] knowledge graph configuration and you
[446] can edit it of of course uh that will
[449] also contain the use ontologies uh that
[452] are extracted from the knowledge graph
[454] and typically using the vid annotations
[457] and there are also an an additional free
[460] input field where you could put any kind
[463] of thing that seems relevant for the
[465] model to be able to uh generate accurate
[469] competency questions. So typically if
[471] you have published um an article that
[475] describes the knowledge graph that's
[477] typically where you would paste the
[479] abstract of uh the article so that you
[482] will guide the model through the
[485] description of the graph of the entities
[486] it contains and help it uh provide and
[489] generate more accurate competency
[492] questions. Once this is done, you will
[494] choose a model number of questions and
[496] run and submit the the whole prompt to
[499] the language model. And if everything
[502] goes well, it will reply reply with a
[505] JSON formatted uh answer like this one.
[508] Each question comes with a complexity
[511] level which could be basic, intermediate
[513] or advanced and a certain and and a few
[516] tags that qualify the the domain of the
[519] question.
[520] Um once you've that you can either
[523] export the set of questions for use in
[526] another application or save them locally
[528] in your browser typically in a cookie.
[531] And when you do that you can then move
[533] on to the next step which will be the
[535] actual generation of the sparkle query
[538] not only generation but also the
[540] execution and the interpretation of the
[543] sparkle query results. So here Q2 forge
[547] relies on various scenarios that are
[549] provided by the back end and here I need
[551] to get into a bit more details. So here
[555] is one of the scenarios that we use. Uh
[558] here typically the user would fill in a
[561] question that can be one of the
[562] competency questions that that has been
[564] generated in the previous step or
[566] another question. So there is a first
[568] step which is a basic validation where
[570] we just ask a model to make sure that
[572] the qu the question that is being asked
[575] is relevant with respect to the graph.
[577] That's that's a very basic step and if
[579] if that's the case then we will go on
[581] with the pre-processing of the question.
[583] So here there are quite a few things
[586] that happen. In the preprocessing we we
[588] will first extract named entities from
[590] the question and from there we will try
[594] to extract the related classes that is
[597] the classes the ontology classes that
[600] are similar to the named entities in the
[603] text embedding space and this is why in
[605] the prep-processing step I mentioned
[607] that we need to do this prep-processing
[609] of computing the text embeddings of of
[611] the classes so using this similarity
[615] measure we will select the classes that
[617] that seem to be the most relevant to
[619] answer the question and then we will try
[622] to figure out how to represent the
[624] classes that is not only just take the
[627] ontology definition of class but how
[630] they are actually used in the knowledge
[633] graph which might be very different from
[635] the actual definition of the ontology
[637] itself. So here we have different
[640] options uh that can be serialized in
[643] natural language as tpples in a turtle
[646] like syntax. So we can experiment with
[648] these these different syntaxes. And the
[650] last step the last thing that we will do
[652] in this step is to select possibly
[655] existing example sparkle queries. So I
[659] didn't mention it but with the knowledge
[661] graph configuration you can also provide
[663] a few example sparkle queries and that's
[665] generally very effective to guide the
[668] model through the generation of an
[671] accurate sparkle query. Once we have
[674] retrieved all of that, the classes and
[676] the possible example sparkle queries, we
[679] will now create a prompt that will
[681] instruct the model to generate an
[684] equivalent sparkle query and we'll
[686] submit this this prompt. So here there
[690] are few few possibilities. So first we
[693] will verify that the answer contains an
[695] actual queries that is just at least
[698] syntactically correct sparkle query and
[701] if not we have a retry mechanism. If
[703] there is a a query we will try to run it
[706] that is submit the query to the sparkle
[709] endpoint get the result and ask a model
[712] again to interpret the results.
[715] So here is how the user interface looks
[718] like. So here you can see the different
[720] steps of the diagram I just showed that
[723] are streamed back to the user interface.
[726] And if everything goes fine, you will in
[729] the end get a sparkle query like this
[731] one. And if it gets even more fine, you
[734] will get an answer to the sparkle query
[737] and the model will interpret the answer
[739] and provide you with a natural language
[741] answer. [snorts] Okay, so that's all
[744] fine, but to be honest, quite often this
[747] is not the way it works because either
[749] the query is not right or not good
[751] enough. Maybe it lacks a few triples or
[754] maybe it it adds triples that shouldn't
[756] be there. Whatever. There are plenty of
[759] reasons for which it it might not work
[761] and it might result return zero result
[764] typically. So to to go ahead with that
[767] you have here another button refine and
[771] this refine button takes you to the last
[774] step of the pipeline which is about
[776] refining the sparkle query. So here we
[778] will refine and judge the query. I will
[781] I will explain this. So here is the
[783] interface. The first part of the
[785] interface is basically a sparkle query
[787] editor. here this is this is yes if you
[789] know it when you where you could just uh
[792] edit whatever you like in the query and
[794] submit it to the endpoint and check the
[796] results and and do it again and so on.
[798] Okay. [snorts] Now the problem is that
[800] quite often ontologies contain terms may
[804] they be classes or properties that are
[807] very opaque. Typically if you use obo
[810] you have these obo iO000000115
[815] and so on. you don't know what that
[817] means and that's the case with plenty of
[819] oboontologies. So here we have another
[822] part of the query of of the interface
[824] that will retrieve those desript textual
[828] descriptions of the classes and the
[829] properties to help you make sense of the
[832] query that has been generated and make
[834] sure whether it's good or understand if
[837] something has not been used in the right
[838] way. And lastly we have a judge step. So
[842] here you will typically use uh language
[846] model again you select language model
[848] here of your choice and you will use it
[851] to judge the relevance of the query
[853] that's been generated with respect to
[855] the question. So we will prompt the
[858] language model and ask it to be critical
[861] about the query its relevance to the
[864] question and provide some hints for
[866] improvements.
[868] So this is the end of the main steps of
[870] the pipeline and um so far we have run
[874] two preliminary experimentations which
[877] with two quite different knowledge
[879] graphs. The first one with genomics uh
[882] has 27 million triples. The second one
[885] is about metabolomics and it has 36
[887] billion triples. So it's much bigger.
[890] And here the the table below gives you a
[892] few figures about the number of classes
[894] in each of the graphs. The number of
[896] properties, time it takes to compute the
[900] text embeddings of the classes in the
[902] preprocessing step. The time it takes to
[905] generate some competency questions to
[907] translate competency question into a
[909] sparkle query and so on. So those
[911] figures are of course only for
[914] information purpose because they largely
[916] depend on the hardware that you're using
[919] but not only that also of on the
[921] language models that you have chosen for
[923] each of the different steps. So starting
[927] from the empirical experimentations we
[930] have already considered the next steps
[933] that we want to go through and those
[935] next steps will take place in the
[937] context of the metabolomic AI project.
[940] uh whose goal is to analyze and
[942] interpret metabolomics data by combining
[945] knowledge graphs with AI and machine
[947] learning techniques. And among those
[950] next steps, what we want to do, of
[952] course, is to run a much larger scale
[954] experimentation to assess different
[956] things. First, the relevance and the
[959] accuracy of the questions, the
[961] competency questions that are generated
[963] and the sparkle query counterparts of
[965] the questions and the relevance of the
[967] pairs. Also we want to be able to assess
[970] the effectiveness of the different
[973] approaches the rag approaches that we
[975] are using. So like I said we provide uh
[978] the model with a set of relevant classes
[980] how to select those classes. We provide
[982] it with a a serialization of the classes
[984] to describe them and give the model an
[987] idea of how they are used in the graph.
[989] So how to serialize those. So all of
[992] these there are multiple options each
[993] time and we need to have a much more uh
[998] exhaustive experimentation to assess all
[1001] of these different techniques and which
[1002] one works best in which situation and so
[1004] on. U we also want to investigate the uh
[1010] follow-up interactions that is for now
[1012] we have we we create a set of questions
[1015] and from one question we create a query
[1017] and we execute it and we refine it. So
[1019] we would like to have something which is
[1021] much more a follow-up dialogical
[1023] interaction between the user and the
[1024] interface. Uh we also intend to explore
[1028] what it takes to vis to uh present
[1032] appropriate visualization of the sparkle
[1034] results. Like I said for now we just
[1036] provide a textual interpretation of the
[1038] results. But sometimes text is not the
[1041] most relevant. Maybe sometimes you need
[1043] a graphics of some time. You need a map
[1045] or any kind any other kind of uh
[1047] visualization. So there are lots of
[1049] things here to do to automatically
[1051] select the most appropriate
[1052] visualization technique.
[1055] We also want to explore what it takes to
[1058] generate not only sparkle queries but
[1060] federated sparkle queries that is
[1062] sparkle queries that will be able to
[1063] span multiple knowledge graphs at the
[1065] same time. Um and finally we intend to
[1069] experiment with agentic interactions
[1071] with knowledge graphs. So here I will
[1074] just give you a hint of what that means
[1076] for now. This is how it works. So you
[1078] have a user agent that connects to the
[1081] web interface and the web interface uses
[1083] an API to invoke the different services
[1086] that are provided by a back end and
[1088] those services are the creation and
[1091] activation of a configuration the
[1093] generation it can ask [clears throat]
[1094] for the generation of competency
[1096] questions or the translation of a
[1097] question to sparkle judge question and
[1099] so on and so on. Um what we want to do
[1102] is uh to
[1104] make this available not only to a human
[1106] user but also to an AI agent by means of
[1109] an MCP server that publishes the
[1112] services of the API and as a matter of
[1115] fact we have a very early stage proof of
[1118] concept um to evaluate this. So we have
[1121] published those API services as an MCP
[1124] server and now we are using this drive
[1127] AI use uh tool. So to ask a few
[1130] questions. So here uh imagine we are in
[1133] the place of an AI agent and we we ask
[1136] what are the available knowledge graph
[1137] configurations and uh the the agent
[1140] selects automatically the right tool to
[1142] get the list of the configuration and
[1144] then we ask to generate four competency
[1146] questions on one of the knowledge graphs
[1148] that has been configured. And here the
[1150] the after a first failure will first try
[1153] to generate the questions but it doesn't
[1155] work until a knowledge graph
[1157] configuration has been activated. So it
[1159] figures this out the second time and the
[1161] second time it does an activate config
[1163] and it asks to generate uh the number of
[1166] the four competency questions that we
[1169] have asked. So again [snorts] this is
[1171] very early proof of concept but still it
[1174] seems to be promising and this is the
[1176] kind of thing we will to explore in this
[1178] in the context of this metabolomic
[1180] project.
[1182] So as a conclusion here is uh the link
[1185] to our GitHub repository where you can
[1188] find uh the code everything is open
[1191] source and uh just to remind the main
[1194] goals of cutoforge it is to generate
[1197] test and refine data sets of natural
[1200] language question and equivalent sparkle
[1202] queries. um it is rag based, it is
[1205] domain agnostic and knowledge graph
[1207] agnostic that is you should be able to
[1208] use it with almost any kind of knowledge
[1211] graph in any kind of domain. It's
[1213] modular and extensible and um thank you
[1217] for your attention.
