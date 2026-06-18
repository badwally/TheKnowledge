---
schema_version: 1
id: yt-sBf8TJgqdwY
type: youtube
title: The Fastest Path To Building An Agent For Your Knowledge Graph Is By Using
  MCP
url: https://www.youtube.com/watch?v=sBf8TJgqdwY
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:15Z'
content_hash: sha256:4cc04a5294e2fbf4810e00ca1da4cfbebad31ebd9846ba9f2d968f1d7494aa15
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 1788
  caption_track: fetched
  snippet_count: 652
filter:
  score: 0.7
---
[9] Thank you very much. Hey everyone. Um,
[13] thanks for joining. Good to good to see
[15] everyone at nodes. Um, I think I think I
[18] have been uh a part of every node since
[21] they started. So that's super fun. Um, I
[24] dropped a link to the the slides in the
[27] chat here. Um, feel free to grab those.
[29] There's some links and um resources that
[32] you might find useful. You also scan the
[34] that QR code. Uh so my name is Will. I
[38] work on the product team at Neoraj uh
[41] with a focus on AI innovation
[44] initiatives. Um some folks might might
[47] have seen me around the NearJ community
[49] before. I I used to work on the
[51] developer relations team for a while and
[53] then uh the last two years I've been uh
[56] working in a few different AI startups
[58] and uh recently back to to NearJ on the
[61] the product team. So good to see
[64] everyone there. There's some links uh to
[65] get a hold of me too if you want to feel
[68] free to uh to reach out. Happy to chat
[70] with folks. So the the title of this
[73] when when I pitched it was the fastest
[74] path to building an agent for your
[76] knowledge graph is is by using Neo forj.
[78] That was several months ago when when I
[80] when I proposed it. I think um I think
[83] now if I would say what's the fastest
[85] path to building an agent for your
[87] knowledge graph is by actually creating
[89] an aura agent. Um I'm curious. Let me
[93] know in the the chat. I'm really curious
[95] like if anyone has tried Aura agent yet.
[98] This is um still in preview but it's
[101] available in Aura. Sign into the the
[103] Aura console and you'll see it there. Um
[106] this is a really neat way to create uh
[109] agents that have tools. So uh text to
[114] cipher tool. We can create cipher
[115] templates or just really simple
[118] similarity search uh and create a agent
[120] that can access those tools that are
[124] capable of quering your database and
[125] then uh they're exposed an API. So, uh,
[128] if I was going to build a talk, uh,
[130] today about the fastest way to build an
[132] agent for your knowledge graph, this is
[133] probably the the route I would take. So,
[136] um, definitely read the read this blog
[138] post. I think Ed had a a talk today on
[140] Ora agent. Um, I might be mistaken, but
[143] but definitely, um, check that out if
[145] you're interested in in creating agents
[147] for uh, for your knowledge graph. So
[150] really I think uh maybe a better way to
[153] to frame this talk is we're going to
[155] talk about MCP agents uh and graphs with
[158] NeoRaj.
[160] So we'll do a do a brief overview of of
[163] NeoRaj um are folks familiar with with
[166] NearJ I see um or sorry are folks
[170] familiar with with MCP is rather what I
[172] meant to say. I see a few folks in the
[174] chat say that they did the training
[176] yesterday for our agent. Cool. That's
[178] awesome. U but yeah, let us know in the
[181] chat. Uh we can kind of level set there
[183] on on MCP, but then really I want to
[186] talk about, you know, the the NearJ MCP
[188] ecosystem. Uh how we can use MCP servers
[193] that can connect to Neoraj for uh
[196] different uh different ways to use those
[198] with agents. And then we'll look at how
[200] we can build your own MCP server. Uh and
[202] then of course we'll we'll talk about
[203] some of the challenges of of working
[205] with uh MCP and and how to think about
[207] that.
[209] And you know feel free uh feel free to
[213] uh keep the session as interactive as
[214] possible. You know I can see the chat
[216] here so you know feel free to drop that
[218] in uh any questions or feedback thoughts
[221] you have. There also some some Neo forj
[223] folks uh in the chat as well.
[226] Cool. So if we take a step back um this
[231] blog post this was uh building effective
[234] agents published by Anthropic almost a
[237] year ago. post. I think this was
[238] December of of last year and I think
[241] this was a really influential blog post
[243] to
[245] kind of set different frameworks for how
[247] to think about uh building agents and um
[251] it goes deep into different patterns for
[253] sort of multi- aent uh coordination and
[256] and that sort of thing. But really I
[258] think there's this this important
[260] concept at the heart of of this idea of
[263] an agent which is the augmented LLM,
[266] right? So an LLM just has uh data
[271] knowledge that it was trained on. Of
[273] course we need to bring more recent more
[276] relevant maybe private enterprise data
[279] uh to the LLM. We also to have a true
[283] agent the LLM needs to the agent rather
[286] needs to be able to um understand and
[289] interact with its environment and it
[291] does this through the use of tools. Uh
[294] so tools you can think of this as like
[296] functionality functions that we've given
[299] uh to our agent to be able to interact
[301] with its environment.
[304] If we extend that that concept a little
[305] bit and and look at like what is a rough
[308] architecture for uh your typical agent
[310] look like it's something like this.
[312] There's there's an orchestration
[314] layer that's orchestrating like user
[317] messages uh system prompts tool calls uh
[320] with your LLM. Uh, how do we use tools?
[324] Well, well, we use it to interact with
[326] external services like maybe I'm
[328] building an agent that has access to my
[331] GitHub and is going to uh I don't know
[334] post messages in in Slack when I uh do a
[337] release or or something like that. Um,
[340] retrieval is also an important piece of
[342] this, right? how am I going to fetch
[345] relevant data based on uh the user
[348] message based on the query? Uh and that
[352] also is done through tools. Uh the
[355] ability for the agent to interact uh
[357] with its environment. And now these
[360] these tool calls so the the access to
[363] tools models choosing to uh invoke the
[368] tools that happens in the agent loop. Uh
[372] this is typically a a three-stage loop.
[374] You can think of this as the uh
[376] typically called the a react loop. So
[377] there's um reasoning
[380] action and then observation as a result
[383] uh of the action and then we go through
[385] that loop again. Have we achieved the
[387] goal? Can we um can we sort of respond
[390] to the user in the loop? Uh no, we need
[393] to maybe call another tool. Okay, we
[395] have more information and we we reason
[397] about that and and go through this loop.
[400] And so when we're thinking of like the
[402] definition or like the the heart of like
[403] what is an agent, um Simon Willis uh
[407] said, you know, an an LM agent runs
[409] tools in a loop to achieve a goal. Uh
[412] that's kind of how we think of it. And
[415] that loop is really important when we
[418] think about context. So context, this is
[422] um like additional data that's passed to
[425] the LLM when we want to uh invoke it.
[428] And if we look on the the left side of
[430] this diagram, right, without the the
[433] sort of augmented LLM, we have a system
[436] prompt and a user message. We send that
[438] to uh to the model and we get back uh
[442] some response. But now in this agent
[445] loop where we have things like tool
[447] calling, there actually might be a lot
[449] in that context, right? we have uh tool
[451] definitions. Uh maybe we have memory.
[455] Maybe we have um like files and
[458] documents that we want to to add into
[460] the context. Um all of this sort of
[462] starts to add up when we call those
[464] tools. Well, the results of those tools
[467] also go into the context and and so we
[469] need to start thinking about uh managing
[471] what's in our context. And this gave
[473] rise to the this term context
[475] engineering. Um, so regardless, I guess
[478] I'm maybe sort of on the the left end of
[480] of of this meme here, right? How do we
[483] think about agents? Well, an agent is is
[485] just an LLM uh calling tools in a loop
[489] to achieve a goal.
[492] And MCP uh is one of the ways that we
[495] can expose tools uh to our agent. So
[499] let's do a brief overview of of MCP. um
[502] MCP model context protocol is a protocol
[507] uh for exposing tools and and other
[510] things. We'll talk about the other
[511] things but think think of tools exposing
[513] tools uh to our models. So the ability
[518] to uh for the model to interact with and
[521] understand uh its environment.
[525] Early on MCP was referred to as like the
[527] USBC uh of the the agent world and I
[532] don't know that resonated I I think with
[534] some folks. It's basically like a
[536] standard interface when you're building
[538] um an AI application is maybe a way to
[540] think of it. So before MCP, we were all
[543] sort of building our own sort of unique
[546] bespoke APIs for interacting with
[548] external services. uh MCP comes along
[551] and we can just build that MCP server
[554] once and then use that as an interface
[557] to that service in all of our uh on all
[560] of our AI applications. And even better
[562] is that someone else maybe um GitHub for
[565] example can build and publish an MCP
[568] server and then we can use their
[569] official MCP server uh to interact with
[573] GitHub across all of our AI
[575] applications.
[577] So uh I copied this slide from the deep
[580] learning.ai course. Um I think this is
[584] uh this is a really good course that
[586] goes a little bit deeper on you know
[588] what MCP is, how do I how do I work with
[591] it but also how do I build MCP servers.
[593] So fundamentally um an MCP server
[596] exposes uh tools, resources and prompt
[600] templates. Mostly we're focusing on
[603] tools. tools. These are, you know,
[605] functions that the model can choose to
[608] invoke uh to either fetch data, call an
[611] API, something like that. Resources.
[613] These are uh readonly data. Uh this
[616] could be something like maybe a bunch of
[619] example uh data models or example
[623] um cipher queries that might be helpful.
[626] And then the prompt templates, these are
[628] kind of like prepackaged prompts that we
[630] know uh work well. uh with sort of the
[635] uh service that we're building the MCP
[637] server for that our a application can
[639] then uh can then use. There are also
[641] lots of other interesting uh features
[644] that are are in MCP like uh sampling
[647] which allows us to uh to sort of send a
[650] prompt back to another model. We can uh
[653] sort of evoke and ask for specific
[655] information. So definitely check out
[657] this course um if you're interested in
[659] MCP in general. What we're going to
[661] focus on today is diving into like the
[664] Neo Forj MCP ecosystem. So this landing
[668] page, this is the um MCP page in the
[671] developer guides, has information about
[674] a bunch of different MCP servers. Um and
[678] so it can be a little confusing and and
[680] maybe overwhelming like which which MCP
[682] server do I want? Um and roughly
[686] speaking here there's docs for the um
[689] official nearj supported MCP server and
[693] then we have these near labs MCP servers
[696] and this is an important distinction
[697] like near labs these are uh more
[700] experimental projects that allow us to
[704] sort of build things put them out and
[706] and validate them with the community.
[707] These are not officially supported by
[709] Neo forj. uh there there are a lot of
[714] challenges and especially around
[716] security and authorization with MCP. So
[718] if you're uh if your requirements you
[721] know need an officially supported uh and
[725] uh MCP server look for the official MCP
[728] server but then these NEFJ labs servers
[731] these projects have um
[734] maybe more experimental functionality
[736] and there are a handful of those. We'll
[738] talk about what some of those are in a
[739] minute. And then there's uh
[740] documentation on different framework
[742] integrations like the Google MCP toolbox
[745] for building MCP servers or integrating
[748] uh MCP servers into all of the different
[751] uh agent frameworks.
[754] So the official MCP server uh this is
[756] currently in uh beta. I think it's uh
[759] beta 3 now. Earlier today um John and
[762] Michael did a a talk that showed how to
[766] use the uh official MCP server. Um, so
[769] it's definitely functional. You can try
[771] it out. Uh, there's some releases in the
[774] GitHub repo there. The NJFJ cipher MCP
[777] server. Um, this is the one we're going
[779] to use today. This allows uh for
[783] exposing the schema and also uh for our
[787] model to be able to execute cipher
[790] queries.
[792] There's also the Nefrj data modeling MCP
[795] server. um Jesus and and Alex did a a
[798] talk earlier today using the data
[801] modeling uh server to build an ontology.
[804] So this is useful uh for creating data
[808] models, visualizing them. This heavily
[811] uses the resources feature. So there are
[813] lots of uh example data models for uh
[817] for different use cases. There's also
[820] the Nej knowledger graph memory server
[822] is one of the the labs MCP servers.
[825] Memory is a really interesting topic. Um
[828] we'll we'll talk a little bit about that
[829] today. Uh memory is important for for
[832] agents uh to be able to sort of hold
[835] states and and knowledge across multiple
[838] conversations or or interactions with
[839] the user. Um entities uh entity
[843] extraction and identifying facts and
[845] preferences turns out to be quite quite
[847] important. Um so this is an MCP server
[849] that you can add to say like cloud
[851] desktop for example uh which will be
[854] able to build a knowledge graph um of
[856] memories behind the scenes.
[858] Let's take a look at uh a few things
[861] like what can we do with the nearj MCP
[864] server. Uh one is exploratory data
[867] analysis. Um cloud desktop is a really
[870] good MCP host application for this. Um
[874] one because it has a really nice nice
[876] interface. Um, and also because it has a
[880] free version, uh, so we don't need to
[882] pay for a subscription to be able to
[884] test it out. This is the configuration
[887] to add the, uh, near MCP server to
[892] claude desktop. Um, basically what we're
[895] using uvx here to run this python uh,
[899] mcp near cipher package and then passing
[901] in credentials to our neoj instance as
[904] environment variables.
[906] can take a look here. Um, here I've
[909] added the Nefrj cipher MCP server to
[914] cloud desktop in the configuration and
[917] it shows up here. I I have a memory
[920] server as well that I've disabled. But
[921] here's the Nefarj database uh MCP server
[925] and you can see the there's three tools
[926] here. There's fetch the schema um
[929] execute a read cipher statement and
[931] execute a write cipher statement. I'm
[934] going to go through a a conversation
[936] that I had earlier so we can see how
[939] this works. Uh and so initially my
[942] database was empty. I said, "Hey, what's
[945] in my Neoraj database?" And we can see
[947] here that Claude chose to execute the
[951] get near schema tool uh and found that
[956] the database is empty. It confirmed that
[957] by running a cipher query to get a count
[959] of the nodes like hey there's there's
[961] nothing in there. And this is where um
[966] I think working like learning new tools,
[969] iterating on data models, the um
[972] exploratory data analysis pieces is
[975] really uh interesting and useful. So I
[977] said, "Hey, I want to design a knowledge
[979] graph uh for product catalog, customers,
[982] order information, suggest a schema." Uh
[985] and Cloud suggested a schema like nodes,
[987] relationships. Um we can iterate on
[989] this. I said, "Hey, yep, looks good."
[991] And now create some sample data. Um, and
[994] this is really neat because now uh Cloud
[996] is going to execute a bunch of write
[998] statements that just going to load some
[1000] sample data into my Neoraj Aura instance
[1007] and this is really good for like testing
[1008] and development, right? Um, and then,
[1011] you know, I can go on and say, hey, you
[1012] know, what are some uh questions that I
[1014] can answer? Generate the cipher queries,
[1016] show me the results, that that sort of
[1018] thing. uh cloud is also really good
[1020] about creating artifacts like
[1021] visualization and um and these sorts of
[1024] things. So that's one uh one use case is
[1028] you know this sort of exploratory data
[1030] analysis uh with Neoraj uh vibe coding
[1034] uh is another like really interesting
[1037] area. Um I like to think of this more as
[1039] like schema assisted um uh development.
[1043] So if we're using something like cursor,
[1046] cloud code, windsurf, um VS code in any
[1050] of these like agent uh coding agent or
[1055] uh idees, we can add the nearj MCP
[1059] server uh and then we can uh leverage
[1063] that in our coding agent. So our coding
[1064] agent has access to the schema and the
[1066] ability to to execute uh cipher queries.
[1069] We're going to take a look at this um
[1071] using uh using that in a moment for
[1074] schema assisted coding um in the context
[1078] of building our own um MCP server. So I
[1081] I did a workshop a couple weeks ago I
[1084] think on um MCP with Neo Forj. So we're
[1087] going to look at uh the example MCP
[1090] server that we built there. Uh it's on
[1092] it's on GitHub. I've got it loaded here
[1096] in cursor. Uh and you can see here that
[1098] I've added the uh nearf database MCP
[1103] server the same one that I I had in
[1104] claude. Um to do this I just you can
[1107] just click add MCP server and paste in
[1109] that that JSON snippet. And so we have
[1112] the the same three tools here. We have
[1113] access to the schema and then the
[1115] ability to execute uh read and write
[1118] cipher statements.
[1122] So um let's take a look at the code
[1124] here. there in in this repo there's a
[1125] Python version and also a TypeScript
[1127] version uh both using the uh official
[1131] anthropics um MCP SDK from the uh model
[1135] context protocol
[1138] uh or
[1140] in Python that is the fast MCP package
[1144] there's currently two versions of these
[1145] one um version one in the official sort
[1149] of Python SDK there's a a version two
[1152] which has some additional functional
[1154] that's not this is using the the
[1155] official one. Uh and so we have some you
[1159] know basic infrastructure here like hey
[1161] we need to create a driver instance.
[1163] Here's kind of a a helper function that
[1165] executes a cipher statement using uh the
[1168] neoraj driver and then we want to be
[1171] able to define tools. So when we define
[1173] tools natural language is is actually
[1176] quite important here. So we need to uh
[1180] have a natural language description of
[1183] the tool and its parameters because this
[1185] is how the model is going to choose uh
[1189] to execute this tool. How it's going to
[1191] understand what the tool uh can be used
[1194] for and uh what parameters need to be
[1197] generated.
[1199] We have uh so this is a search customer
[1202] um tool that has a pretty basic cipher
[1205] statement uh and just returns that. And
[1207] then we have another tool that we've
[1208] defined here which is recommend product.
[1211] So given a customer ID, let's have a
[1214] product recommendation query uh and
[1218] return recommended products to the user.
[1222] And that's that's pretty much it, right?
[1223] We have we have functions that have some
[1224] logic. In this case, it's going out and
[1227] um executing a database query. And we
[1230] just annotate those with the this
[1232] MCP.tool.
[1233] Let's go ahead and give this a run.
[1237] So, our MCP server is up and running uh
[1240] on port 8000. And I'm going to launch
[1242] the MCP inspector. This is a a really
[1246] useful tool for uh debugging,
[1250] testing, and development of uh MCP
[1254] servers. So, let's go ahead and connect
[1257] to our MCP server. And we can see here
[1260] that we're
[1262] uh we can list like resources, prompts
[1265] that are exposed. Our MCP server um
[1267] exposes two tools. Search customer. So
[1270] we can
[1272] search for customers. Let's run this
[1275] tool. It runs um cipher query and and
[1279] returns some results. So we found a user
[1283] um James here.
[1286] Let's check out the recommend product.
[1289] Um I happen to remember James. James'
[1292] customer ID is customer 004.
[1296] Uh let's go ahead and run this tool. Oh,
[1298] and we get an error. So we have a syntax
[1301] error in our cipher statement. So let's
[1303] jump back to the code here. Um so this
[1306] is our problematic
[1309] cipher statement. Um and so what I'm
[1311] going to do here is highlight
[1316] this. I'm going to say add to chat. So
[1317] this is going to add uh these lines into
[1320] a new uh agent mode chat in cursor. And
[1324] I'm going to say this uh cipher
[1326] statement
[1328] returns an error. Use your Neoraj tools
[1332] to uh fix the cipher statement.
[1339] So this is like a a coding agent chat.
[1342] Um I've added into the context like the
[1345] specific um problem specific area I want
[1348] to uh debug and improve. And we can see
[1351] here that cursor uh is okay. Great. I
[1355] need to fix this cipher uh query. So the
[1358] first thing I'm going to do is fetch the
[1359] schema. And then we're going to run uh
[1365] some different versions of the cipher
[1368] statement. And I'm starting to get a
[1369] diff here. Uh and so there was a syntax
[1372] error in here. Uh we're going to
[1376] update the query. Uh, and then what's
[1378] really neat is that cursor is able to
[1380] test it. So it's able to to generate the
[1382] query not just based on the schema, but
[1383] it's also able to actually test that
[1386] query um and see to make sure that it um
[1389] that it actually works.
[1392] And so there was a problem here. We had
[1394] we were doing some improper
[1397] uh aggregation uh before we were
[1400] returning.
[1404] We can see the results of all these of
[1406] all these tool calls here.
[1411] Cool. It says, "Hey, this this works
[1413] without errors." Um, great. And then
[1415] it's just kind of testing it again.
[1418] So, let's keep all of these.
[1422] Let's restart
[1427] our MCP server. We'll launch the
[1429] inspector again.
[1434] We can connect again. Tools list tools
[1438] recommend product
[1441] customer 004.
[1444] Run the tool to get recommendations. We
[1447] don't get any recommendations, but we
[1448] don't get an error. Um, and the reason
[1450] we don't get any recommendations is
[1452] because this user doesn't have any
[1453] overlapping um, products that it's
[1456] purchased. And so I could go back here
[1458] and say um I didn't get any results for
[1465] right and curs will will stick in
[1468] customer 004 for the customer ID and and
[1471] figure out oh well the reason you're not
[1473] getting any results is because you don't
[1475] have any overlapping product purchases
[1477] and it'll recommend a fallback and and
[1480] so on. So anyway, this is just an
[1481] example of how we can use the uh NearJ
[1485] MCP server
[1488] in coding agents to kind of help with uh
[1492] with schema assisted coding is is the
[1494] way I like to think of it. Uh AI agent
[1497] memory is we were talking about this
[1500] this earlier when we were looking at the
[1501] knowledge graph memory server. This is a
[1503] really interesting area. I'm going to
[1505] kind of skip through here. Um definitely
[1508] check out these slides if you're
[1510] interested in in memory. There's um an
[1512] example project that I built that uses
[1515] MCP to expose uh memory search tool and
[1519] um message saving that does in
[1520] extraction and this kind of thing. So
[1523] check that out if you're interested to
[1524] see how that works. Um instead of in the
[1526] last few minutes here, what I want to do
[1528] is talk a bit about uh some of the
[1530] challenges that come up when working
[1533] with MCP. Some of the the biggest ones
[1536] are um you know working with tool
[1538] calling models, authorization and and
[1540] then managing context. So
[1544] one observation is is that not all
[1547] models are um great at tool calling. Um
[1552] our friends at Leta recently published
[1554] this uh benchmark context bench which is
[1558] this is deeper than just tool calling.
[1561] It's sort of like uh how good are the
[1563] models at chaining together multiple
[1565] tool calls and and this sort of thing.
[1567] And we can see here that cloud sonnet 45
[1569] is is the clear winner uh here. And if
[1573] we think about like why this is well in
[1577] order to uh invoke a or request a tool
[1581] call the model needs to emit uh a
[1584] special token that indicates hey I would
[1586] like to call this tool. uh and like
[1589] these tokens they they don't exist out
[1591] out in the wild and so uh this this
[1594] doesn't happen during training. This is
[1596] like a post-training thing that we have
[1599] to do. Uh and so uh how good the models
[1603] are at tool calling depends on I think
[1608] part of it is like how much effort is
[1610] invested in this like post-training um
[1612] process. Anthropic I think has invested
[1614] quite a bit um into this area.
[1620] Um the folks at Cloudflare had had this
[1622] observation, right, that like not all
[1624] models are are so great at tool calling.
[1628] And they have an an interesting approach
[1630] that they they call code mode in in
[1632] their agent framework where the uh agent
[1636] framework actually will convert the
[1638] tools exposed through MCP to a
[1641] TypeScript API and then spin up a
[1643] sandbox and the agent will write code
[1645] that executes in that sandbox. Um they
[1648] found that this improves uh the tool
[1650] calling ability of of models.
[1652] authorization is um is really a whole
[1656] area I think that is best practices are
[1659] being identified there. There are a lot
[1660] of um horror stories uh there's a docker
[1664] blog post series that uh is horror
[1667] stories of uh of MCP. It's good good
[1670] timing around uh Halloween. Um one of
[1673] the examples is uh you know software
[1675] supply chain injection where they in um
[1679] injected some uh attack into a popular
[1683] uh package that was used as an MCP
[1685] proxy. Um so these are these are things
[1687] to think about as you're uh adopting
[1690] MCP. Uh and then managing context is
[1693] also a bit of a challenge here. We saw
[1695] this this image earlier where the tool
[1698] definition and the tool results by by
[1700] default go into the context uh which can
[1703] eat up a lot of tokens. It can also uh
[1705] make it more difficult for the model to
[1707] figure out like which uh which tools to
[1710] call. Um, and here's a a blog post from
[1714] Enthropic that came out a couple days
[1716] ago uh making this observation
[1719] uh that tool calling, direct tool
[1722] calling consumes lots of tokens and
[1726] they're looking at a similar approach to
[1728] to Cloudflare of you know agents scale
[1730] scale better if you're actually writing
[1731] code against the tools rather than using
[1734] this like JSON representation for tool
[1737] calling. Cool. So, we're about um about
[1740] out of time here. There are lots of
[1743] resources out there on using um MCP with
[1746] Neo forj. These are just some of the the
[1748] MCP talks today at nodes. I think most
[1751] of these already happened. Um look for
[1754] the recordings on the the YouTube
[1756] channel. Um, if you're interested in uh
[1758] in finding any of these uh for the
[1761] Neoraj MCP ecosystem, this page is going
[1764] to be your best bet uh in the developer
[1767] guides with uh links to resources for
[1770] all the different MCP uh NearJ MCP
[1772] servers and framework uh integrations.
[1775] Uh and then here are some of the the
[1777] tools that we mentioned uh earlier
[1780] today. And we are out of time here so we
[1783] will stop there. Thanks a lot everyone.
