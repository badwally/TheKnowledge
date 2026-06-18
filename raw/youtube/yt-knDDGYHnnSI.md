---
schema_version: 1
id: yt-knDDGYHnnSI
type: youtube
title: 'GraphRAG: The Marriage of Knowledge Graphs and RAG: Emil Eifrem'
url: https://www.youtube.com/watch?v=knDDGYHnnSI
authors:
- AI Engineer
ingested_at: '2026-06-17T20:57:05Z'
content_hash: sha256:f624998b57317354a7ba905651b565bea239d584d499a1919b7f05dd08d59ae6
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AI Engineer
  channel_url: https://www.youtube.com/@aiDotEngineer
  duration_seconds: 1156
  caption_track: fetched
  snippet_count: 456
filter:
  score: 0.85
---
[0] [Music]
[14] I basically dedicated my professional
[16] life towards getting developers to be
[19] able to build better applications and
[22] build applications better by leveraging
[25] not just individual data points kind of
[27] retrieved at once like one at a time or
[31] summed up or grouped calculated averages
[34] but individual data points connected by
[36] relationships right and today I'm going
[38] to talk about that applied in the world
[41] of llms and
[43] gen so before I do that though I'm going
[45] to take a little bit of a detour I'm
[47] going to talk about search the evolution
[49] of search everyone here in this room
[50] knows that the vast majority of web
[52] searches today are handled with Google
[54] but some of you know that it didn't
[56] start that way it started this way who
[58] here recognizes this web page right yeah
[61] who here recognizes alav Vista as a name
[63] like a a few people right um back in the
[67] mid90s there was dozens of web search
[69] company dozens plural like 30 40 50 web
[72] search companies and they all used
[73] basically the same technology they lo
[76] used keyword-based text search inverted
[79] index type search bm25 like for those of
[81] you who know what that means and it
[83] worked really really well until it
[86] didn't and the Ala Vista effect kicked
[89] in which was the not that you search for
[91] something you got a thousand or
[93] thousands of hits back and you had to
[96] look through Page after page until you
[98] found the result that was relevant to
[100] you the alav Vista effect you got too
[102] much back from the internet that wasn't
[104] a problem in the beginning because most
[106] of the things you searched for when I
[108] went on onto the internet in the
[109] beginning got zero results back because
[111] there was no content about that on the
[113] internet
[114] right but the Ala fist effect too many
[117] search results was solved by Google this
[120] is Google's press release mid you know
[123] mid 2000 they talk about a billion URLs
[126] they've indexed right but they also talk
[128] about the the technology that they use
[129] behind the scenes the technology called
[131] page rank that delivers the most
[134] important search results really early on
[137] in fact the first the top 10 Blue Links
[139] on that first page right that technology
[143] page rank is actually a graph algorithm
[146] which is actually it's called igen
[148] vector centrality and the innovation
[150] that Google did was applying that to the
[153] scale of the internet and the scale of
[155] the web right page rank that ushered in
[159] and created honestly the most valuable
[161] company on the planet for quite quite
[163] some while the page rank era right that
[167] lasted for about a decade about a dozen
[169] years until in 2012 Google wrote this
[173] blog post which is an amazing blog post
[175] introducing the knowledge graph things
[178] not strings where this they said you
[180] know what guys we've done an upgrade on
[183] the back end of our search technology
[185] the biggest one since we invented page
[187] rank where we're move moving away from
[190] not just storing the text and the links
[192] between the documents but also the
[195] concepts embedded in those documents
[197] things not just strings and we all know
[201] what the knowledge graft looks like
[202] visually when you search for something
[204] on on on Google today Moscone Center
[207] just around the the corner from here
[209] you're going to get this little panel
[211] right on the right hand side if you look
[213] at that panel it has a combination of
[216] unstructured text in this case from
[218] Wikipedia with structure text it has the
[221] address the owner of the mcone building
[224] you know that kind of stuff this thing
[227] is backed on the back end by the data
[229] structure looking like this right it has
[232] these concept the rings that we call
[234] nodes that are connected to other nodes
[237] through relationships and the both the
[239] nodes and the Rel relationships have key
[241] value properties you can attach two
[243] three a th000 10,000 on both the nodes
[246] and very importantly also on the
[248] relationships this is a Knowledge Graph
[251] and that was the next decade or so 12
[254] years of Google's dominance until a few
[258] months ago a few months ago at Google IO
[262] they took the next step ushered in by
[265] the AI Engineers conference a year ago
[268] well not quite but of course the entire
[270] C around gen and this is one of the
[272] example that they did the classic travel
[274] itinerary they helped me plan out this
[276] this travel everyone here is in this
[278] room knows that this is backed by an llm
[281] and it is backed by an llm in
[283] combination with this knowledge graph
[285] data structure graph rag this is usering
[290] in the next era of web search the graph
[293] rag era what I'm going to talk to you
[296] about today is how can you use well
[298] first of all should you and if so how
[301] can you use graph rag for your own rag
[303] based
[305] applications so what is graph rag right
[308] it is very very simple graph rag is rag
[312] where on the retrieval path you use a
[315] Knowledge Graph very very simple it
[318] doesn't say you only use a Knowledge
[320] Graph but you use a Knowledge Graph
[322] maybe in combination with other
[323] Technologies like vector search so let's
[326] take the classic example of a customer
[328] service bot right and let's say that you
[331] are working at a company that is
[334] building Wi-Fi routers for example right
[337] and you have a bunch of support articles
[339] right and they've been stored in text
[341] files right and then you are tasked with
[345] building a bot that either is gives
[347] direct end users access to it or your
[349] own customer service agent employees
[351] like access to this information and you
[354] know how to do this because you live in
[356] the llm world and the Gen world so
[357] you're going to use rag for this right
[360] and so you have that data it's text
[362] documents you've added that text onto
[365] the properties of particular nodes right
[368] so have a node per article but then
[370] you've also said that you know what this
[372] article is about this particular Wi-Fi
[375] product right you have a relationship to
[376] that Wi-Fi product and that Wi-Fi
[379] product sits in a hierarchy of other
[381] Wi-Fi products and it's written by this
[383] particular customer service engineer you
[385] know that kind of stuff and then the end
[387] user has a question hey my wife Wii
[390] lights are flashing yellow and my
[392] connection drops like what should I do
[394] something like that I think we all know
[396] how we do this we vectorize the search
[399] right we get a some kind of vector
[401] embedding back we use Vector search to
[403] get the core documents but here's where
[405] the graph rag part kicks in you get
[407] those core articles back which are
[409] linked to the noes actually the text is
[411] on the nodes but then you use the graph
[414] to Traverse from there and retrieve more
[416] context around it maybe it's not just
[419] that particular article for that
[421] particular Wi-Fi but something else in
[423] that family maybe you use the fact that
[426] this particular engineer has very highly
[429] ranked content and then you rank that
[431] higher right you retrieve more context
[433] than what you get out of the a&n based
[435] search from your from your vector store
[439] and you pass that on to the llm along
[441] with the question you get an answer back
[443] and you hand it to the
[445] user so the core pattern is actually
[448] really really simple but really really
[450] powerful right you start with doing a
[453] vector search I think of this almost as
[455] a primary key it's of course not a
[457] primary but almost like a primary key
[459] lookup into the graph you use that
[461] Vector search you get a an initial set
[463] of nodes then you walk the graph and you
[467] expand that and find relevant content
[470] based on the structure of the graph then
[472] you take that and you return it to the
[473] LM or optionally maybe that gives you a
[477] th000 or 10,000 nodes back and then you
[479] do what Google did you rank that you get
[482] the top K based on the structure of the
[484] graph maybe you even use page rank right
[487] you get that you pass it on to the llm
[489] really really simple but really really
[492] powerful and then there's a number more
[494] advanced patterns but that's kind of the
[496] next the next talk I'll do in a year the
[499] like more sophisticated graph retrieval
[501] patterns right but the core one very
[503] very
[505] simple okay so if that's what graph rag
[509] is what are the benefits of graph rag
[511] when should you use it when should you
[512] not use it the first and most Stark
[516] benefit is accuracy it's directly
[519] correlated to the quality of the answer
[521] there's been a ton of research articles
[524] about this in the last six months or
[526] something like that I believe the first
[528] one was this one by data. world I just
[530] picked out three out at random here that
[532] I that I that I like this is the first
[535] one that I know of by dataworld which is
[537] a data cataloging company based on a
[539] knowledge Gra graph and they proved out
[541] across I think 43 different questions
[544] that on average the response quality the
[547] accuracy was three times higher if they
[550] use a knowledge graph in combination
[552] with with Vector
[554] search I love this paper by LinkedIn uh
[557] it's a shows a very similar type I think
[560] it's like 75% or 77% increase in in
[564] accuracy um but it also has a great
[566] architecture view so you can take a the
[569] QR code right there look at that paper
[571] which combines various components and
[573] also the flow through that that I
[575] thought was just really pedagogical um
[578] but by and large it's showing the same
[580] thing a little bit of different numbers
[582] but significantly higher accuracy when
[584] it used graph in combination with Vector
[587] search and then Microsoft had a
[589] fantastic blog post and subsequently I
[592] think two academic papers the blog post
[594] was in February of this year where they
[596] also talk about the increased quality of
[599] respon bonds but also beyond that hey
[602] you know what graph rag enables us to
[604] answer another important class of of
[607] questions that we couldn't even do with
[610] Vector search alone or Baseline Vector
[612] search that's what they or Baseline rag
[614] alone so first benefit higher quality
[617] response
[618] back the second one is easier
[622] development and this one is a little bit
[624] interesting because there's an asterisk
[625] in there because what we hear very
[627] clearly from our user is that it's
[629] easier to build rag applications with
[632] graph rag compared to Baseline rag but
[634] we also hear it's like it's actually
[637] hard and what's the Nuance there well
[639] the Nuance is if you already have a
[641] Knowledge Graph up and running so
[642] there's a learning curve where people
[644] need to learn how do I create the
[646] knowledge graph in the first place once
[648] you have that it's a lot easier but how
[650] do you create that Knowledge Graph right
[653] so let's put a little pin in that if I
[655] rush through the next few slides quickly
[657] enough I'm going to show you hopefully a
[659] demo on on on on that but let's put a
[661] little pin in that so this is an example
[663] this is from a um a very high growth
[667] stage fintech company that is very
[670] Cutting Edge in Ai and they started
[673] playing around with graph rag a few
[675] about six months ago and they took an
[677] existing application and they said you
[679] know what we're going to Port this from
[681] a vector database to Neo and most of the
[685] operations yield a better result they
[686] can calculate the embeddings on a
[688] database level getting related actions
[691] is as simple as following the
[692] relationships between nodes and this one
[695] I love the cache and the cach here is
[697] their application they call it the Cache
[699] can be visualized this is an extremely
[702] valuable debugging tool and in the
[704] parenthesis I actually already fixed a
[706] couple of bugs just thanks to this right
[710] amazing like once you've been able to
[712] create that graph it's a lot easier to
[714] build your rag
[716] application and why is that right right
[720] so let's talk a little bit about
[721] representation let's say we have the
[724] phrase in there apples and oranges are
[725] both fruit and we want to represent that
[728] in Vector space and in graph space in
[731] graph space we already talked about this
[733] apple is a fruit orange is a fruit
[736] pretty easy that's the representation in
[739] graph space in Vector space it looks
[742] like this maybe or maybe this is
[745] something else like we actually don't
[747] know two different ways of representing
[749] that phrase and then we can run
[751] similarity calculations in different
[754] ways using these both both
[756] representations that I'm not going to go
[757] through right now we can search in
[759] different ways these are not competing
[763] ways of doing it they're complimentary
[765] ways of doing it right one is not better
[767] than the other except I will make one
[769] statement which
[771] is when you sit down and you write your
[774] application when you build your
[775] application I'm actually going to make
[777] the statement that one of them is
[778] superior this Vector space
[781] representation is completely opaque to a
[782] human
[783] being but the graph representation is
[787] very very clear it is explicit it's
[790] deterministic it's visual you can see it
[793] you can touch it as you build our
[795] applications this is the I already fixed
[798] a couple of bugs thanks to this just by
[800] porting it from a vector only store to
[803] graph rag they were able to see and work
[804] with the data and that is really
[807] freaking powerful that shows up in
[810] development time as you're building your
[812] applications it's also showing up for
[815] our friends in it who worry about things
[818] maybe that is not directly related to
[820] building the application which is
[823] explainability which is auditability
[826] which is
[827] governance That explicit data structure
[831] has knock on effects over there that are
[833] really really powerful once you're up
[835] and running in production and You' to be
[837] able to explain why something happen
[841] happened so higher accuracy better
[845] answers easier to build once you're
[847] through the hump of creating the
[848] knowledge graph and then increased
[850] explainability and governance for it and
[853] the business right those are the three
[856] things so how do you get started with
[859] with graph raging well I've talked a lot
[861] about this already like how do you
[862] create the knowledge graph in the first
[864] place so a little bit of nuance here so
[867] basically there are three types of data
[869] out in the world that I care about when
[871] I think about knowledge graph creation
[873] the first one is structure data so this
[875] is your data in your snowflake or
[877] something like that or postgress right
[880] the other one is unstructured data PDF
[882] files raw text from a web page and the
[885] other one the third one is mixed people
[888] tend to call this semi-structured but
[889] it's not hit me up afterwards and I'll
[891] tell you why it's not but basically what
[892] this one is is structure data where some
[895] of the fields are long form text right B
[899] basically we're great in the first
[901] bucket in the graph world it's very easy
[904] to go from Snowflake or postgress or
[906] MySQL or Oracle into a property graph
[910] model the unstructured one is really
[913] freaking hard right it's hard to do in
[916] theory it's also had immature tooling
[918] for a long run the middle one is
[922] actually where the majority of at least
[924] Enterprise production use cases are in
[926] the real world
[930] so man two and a half minutes this is
[932] rough um there are two types of graphs
[935] and I'm not going to talk about them I
[936] want to talk about them lexical graphs
[938] and domain graphs is actually really
[939] relevant but I really want to get to
[941] this demo so I've talked about creating
[945] graphs with unstructured information so
[947] we just built this new tool that we
[949] launched just a few weeks ago called the
[951] knowledge graph Builder and you see it
[953] here I can can you see the screen okay
[957] so basically here you can drag and drop
[959] your PDF files you can put in YouTube
[962] links Wikipedia links you can point it
[964] to your kind of cloud service bucket
[966] right and it's can extract the data from
[968] there and create the graph so here I
[970] added a few things I added um a PDF of
[975] Andrew ning's newsletter the batch I
[977] added the Wikipedia page for open Ai and
[980] I added the YouTube from swix and alesio
[983] you know the four Wars lat and space
[985] podcast so I added all that and I
[988] uploaded it into this knowledge graph
[991] Builder and when I do that it creates if
[996] let's see here I knew the ethernet
[999] connection was going to do it it
[1001] automatically created a little Knowledge
[1005] Graph if it
[1007] renders wait for it it says one minute
[1011] here so it better render pretty soon all
[1013] right let me do this again please work
[1020] oh
[1023] no yeah oh my my why isn't oh oh crap oh
[1031] no and it's ticking down all
[1034] right wait for it wait for it all
[1039] right you can do
[1041] it can do
[1044] it and I was like trying to keep it
[1046] alive in the in the thing too all right
[1050] okay let's see I think we are here and
[1054] then it says show me a graph and it's
[1057] not going to show me the graph oh yeah
[1059] it will come on you can do it all right
[1065] yes so what we have here check this
[1069] out I would love to sit here and just
[1070] drink in your applause but we need to
[1072] look at this data so check this out this
[1075] is the document the four Wars document
[1077] here are the various chunks and then you
[1079] can take a chunk and you can expand that
[1082] this I put in the the the embedding and
[1085] you can I'll zoom out here and you can
[1088] see that it takes the The Logical
[1091] concept elements out of that chunk like
[1094] machine learning they talk about
[1096] something that is developed in a similar
[1098] fashion I don't even know there's some
[1100] company there right and you get that
[1102] entire graph of all this information on
[1107] top of that I really don't have time to
[1108] show it but there's also I really don't
[1111] have time to show it there's a chat but
[1113] in here that you can use and you can
[1115] introspect the result that gets back
[1117] I'll one more second take up your phones
[1121] if you think this looks cool take a
[1123] photo of this QR code and you're going
[1126] to have an amazing landing page where
[1128] you have access to all of this
[1129] information you can get up and running
[1131] yourself thank you for the additional
[1132] minute thank you thanks everyone for
[1134] paying attention
[1139] [Music]
