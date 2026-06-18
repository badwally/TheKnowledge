---
schema_version: 1
id: yt-3g_vsBSqfhw
type: youtube
title: Road to NODES | Build Your First Knowledge Graph AI Agent with Neo4j MCP
url: https://www.youtube.com/watch?v=3g_vsBSqfhw
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:14Z'
content_hash: sha256:aedb5f7902c5a7a0927298642d51f2a786d84efcc23db07d9991bdf35047fbd9
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 7490
  caption_track: fetched
  snippet_count: 2549
filter:
  score: 0.85
---
[0] All right, good morning, good evening,
[2] good afternoon everybody and welcome to
[5] the second to last road to notes
[7] workshop today. I'm uh little sad but
[11] also a little happy that we can do this
[13] today. So today we talk about knowledge
[15] graph uh AI agents with the new MCP
[18] server. So pretty pretty cool pretty
[20] pretty hot topic. I've been at a at an I
[23] event yesterday in Hamburg in Germany
[25] where everybody was talking about AI and
[27] everything AI. So it was it was um it
[30] was quite quite interesting experience
[32] and I think we are continuing this vibe
[34] um going forward today. I'm I'm I'm
[36] super happy to to hear more about um
[39] this and especially yesterday was a bit
[41] more business focused. Today I think we
[43] go hands-on um and we dive in um with um
[47] our hands on keyboards with with Will
[49] Lion
[50] who I'm very happy to to um to have as a
[53] as a host for for this um you know event
[56] today. Uh it's always great great to
[59] have Will back. Uh he's been a regular
[61] uh at row to nodes as well as at nodes
[64] since
[66] years five six years probably since the
[69] beginning basically I think you've been
[70] there all the time um and uh it's great
[73] to to have you join again uh for for
[75] this workshop today u on the very
[78] interesting um topic on on on knowledge
[81] cross with AI agents on MTP uh server. I
[84] see people from um just reading this and
[86] because I see it's always nice to see
[88] from uh the United States, from France,
[90] uh from Canada, from uh Mexico, from the
[95] United Kingdom. Um so, you know, one
[99] more Canada. So, Uruguay, Scotland.
[101] Yeah, that's great. South Africa. Um
[104] lots of uh all the states in the United
[107] States. So, Florida, Philadelphia,
[109] Philly, um New York City. So, it's
[112] always great. India, Switzerland also.
[114] Um again is is is it's great to see this
[117] this whole graph global graph community
[120] come together and um and to talk uh with
[123] you about these interesting topics and
[125] to learn with you on in these
[127] interesting topics as well. So as I said
[129] this is the the second to last event on
[132] road to notes. There's one more um road
[134] to events happening uh which is on aura
[136] agents and that's going to be tomorrow.
[138] Um we had to move as you all probably uh
[141] remember to move this event short notice
[143] because we was a little bit under the
[144] weather last week. Um and so we do this
[146] today uh and we do another one uh road
[149] to notes one more workshop tomorrow. Um
[151] so that's um that's going to be the the
[154] upcoming um road to notes sessions and
[156] um I'll give you a little shout out or
[158] little little heads up of what's coming
[159] up towards um the future at the end of
[162] this episode. Um we will record this
[165] session. So this session is is recorded.
[167] So if you know if you have to drop out
[169] at some point or if you miss something,
[171] want to rewatch something, you know, you
[172] can always come back to it. We'll send
[174] you um the link to the video recording
[176] later this week. So you can always watch
[178] that. She will already share the slides
[179] or pin that message. So you can always
[182] look at that as well. And um yeah, if
[186] you have any questions uh use the Q&A
[188] function. So at the top of your chat,
[190] you see three messages or three buttons.
[192] You can click one says chat, which is
[194] where you are right now, which is where
[196] you are talking. So that's great. You
[197] can always put comments in. You can, you
[199] know, have, you know, feedback,
[201] whatever. Put it there. If you have a
[203] questions, use a question, use the Q&A
[205] button. With that, you you open a new
[208] chat panel and then with that, you can
[209] send a question. And that question I can
[211] see in a Q&A panel slide, which is a
[213] little bit easier for me to navigate and
[215] don't miss uh questions that come in.
[217] And at certain points, whenever Will
[219] tells me so or at definitely at the end
[221] of the session today, uh we will have a
[223] little bit of time to answer questions.
[225] So we we are we we we take some some uh
[227] some of that um out of position today
[230] and um yeah I think that's that's
[233] covered it. Uh I think from my side Will
[235] um you need to click on go on stage at
[238] the bottom right of the screen where
[241] little green button
[243] here you are. Hi Will. How is it going?
[246] >> There we go. Hey uh I was wondering uh
[249] wondering if I was on or not. Cool.
[251] Well, yeah, thanks um thanks Alex for
[254] for hosting. Thanks everyone for joining
[255] and yeah, as Alex mentioned, sorry for
[258] rescheduling. Um quite sick last week
[261] when we were supposed to do this. I
[263] don't think we could have gotten through
[264] it that day. So, thanks thanks to
[265] everyone for moving to today.
[268] >> Yeah. And and since we're recording
[270] this, I mean now now you know everybody
[272] gets it. So, I mean it doesn't help it
[273] as I say now because if somebody
[275] couldn't attend now, they wouldn't
[277] listen to it right now. Everybody who
[278] has registered for this event will get
[280] the recording. So even if people who
[282] weren't able today um to to join in,
[285] they they can watch the the recording
[287] that that we'll we'll take on. So yeah.
[291] Cool. Um yeah, I think I'll I'll hand it
[293] over to you. As I said, I'll be here um
[296] all the time. Um if you if you have
[298] questions, use the Q&A function. I will
[301] um I will jump in. Will you let me know
[302] when is a good time to read out some
[304] questions and I can always come come on
[306] screen and and read the questions. Um
[308] otherwise um uh yeah enjoy everybody
[312] have have fun and uh yeah have a good
[315] good uh road to notes today.
[319] Awesome. I'm just sharing my screen
[321] here. There we go. So I shared um a link
[325] to the slides. Alex I think pinned those
[327] in the chat. They're um on the screen
[330] here. Dub.sa shnefjcpworkshop.
[335] Um, yeah, as Alex said, like definitely
[337] want to keep this as handson as possible
[340] since we're all here um together. So,
[342] feel free to ask um any questions you
[346] have in um in the chat or as Alex said
[349] in the that QA tab, we can track the
[351] questions there if you're just want to
[354] heckle me. That's a good uh good one for
[356] the general uh chat channel. But know
[358] I'll be be monitoring that. So yeah,
[360] feel free to um to chime in there with
[362] any any questions or thoughts and
[364] definitely monitor that as we go along.
[367] So here's the the slides. Um
[371] I think there's some information in
[373] here, but a lot of what we're going to
[375] do is is going to be hands-on. So I'd
[376] say yeah, like have have the slides open
[378] in another tab that um that should be
[381] useful hopefully.
[384] Cool. So um yes, if you don't know me,
[387] my name is Will. Um, I've been a member
[390] of the the Neoraj uh community for a
[393] while. I I worked at Neoraj for a while.
[395] I was a new user for a while. Um, more
[397] recently I've been working a lot with um
[401] AI agents and um seeing how that fits
[404] into the uh evolving AI ecosystem. Um so
[408] you can find me online there. Um and
[410] again last chance to to grab the slides
[412] here.
[415] Cool. So I I think you know really like
[418] the um the focus of today's session is
[421] MCP. So using Neoraj uh and model
[425] context protocol to expose
[428] knowledge graph tools, right? So we'll
[431] talk a bit about MCP. Um let let us know
[434] in the chat. I'm curious like what folks
[436] experience with MCP is like have you
[439] have you built an MCP server? Are you
[442] have you you know used MCP clients? what
[445] MCP
[447] uh tooling are are you comfortable
[450] comfortable are are you familiar with um
[453] definitely let us know in the chat
[454] that's that's super helpful but that's
[456] really the the focus of today is um
[460] trying to understand how MCP and and
[463] NearJ fit together um and take a look at
[467] really how we can expose tools to our AI
[472] uh agents and models that allow us to
[476] interact with a knowledge graph. So
[478] that's really the um the focus of it. So
[481] I see some some folks saying uh MCP is
[484] pretty new. That's great. That that's
[486] perfect. Um you folks have used cloud
[488] code. Cool. That's great. Um
[494] people using fastmcp. Cool. That's
[496] great. Yep.
[498] Awesome. Cool. So by the you know by by
[502] the end of today um you know we should
[504] all be able to get a Neoraj MCP server
[508] up and running uh and connected to an AI
[511] app. We're going to start with cloud
[513] desktop um and we'll sort of see how we
[517] can use um some of the existing Neoraj
[520] MCP servers to do some exploratory data
[524] analysis. Um, then we're going to take a
[525] look at how we can build our own MCP
[527] server and use some of the tools in the
[530] ecosystem like the MCP inspector um to
[533] help us develop that MCP server. And
[536] while we're doing that, we're going to
[537] take a look at some uh some vibe coding,
[540] some agent coding assistance uh to help
[543] us actually use MCP to build in UFJ MCP.
[548] Sounds a little uh little fun, little
[550] recursive there. Um but then we'll also
[552] take a look at how MCP can enable I
[554] guess like uh data layers for the
[558] uh for the AI application. So we'll take
[561] a a deeper dive into uh agent memory um
[564] and see how MCP can possibly expose
[567] tools for for agent memory and and we'll
[569] take a look at a project there. So
[570] that's the that's the goal for today. We
[573] have two hours. Um, so an hour and 50
[575] minutes from now, um, we'll be done and
[577] you will know how to do all three of
[578] those things um, in the next two hours.
[582] So, like I said, we want to be as
[584] hands-on as possible. Um, we're going to
[587] use Claude Desktop. Um, so if you want
[590] to follow along and you don't have
[591] Claude downloaded and installed, um, go
[595] ahead and do that. cloud.com/d download.
[598] We're specifically going to use the
[600] cloud desktop application so that we can
[602] work with um MCP servers running uh
[606] locally on our machine. Um so if you use
[609] cloud in and the web or something like
[610] that, you'll definitely want to download
[611] cloud desktop. You don't need to have um
[614] a paid account with cloud. That's one of
[616] the reasons I I like to pick cloud
[618] desktop to play around. We can um
[619] connect to the nearfjmcp servers uh
[622] without having a paid account. should
[623] have enough credit with just the free
[625] trial for Claude there. So, we're going
[627] to use Claude. Um, you want to download
[630] and install that. And then we're also
[632] going to use uh GitHub code spaces.
[635] GitHub code spaces is like um a dev
[640] container. So, like a containerized
[641] development environment. Um, this is
[644] this is useful just because it has all
[645] of the dependencies
[647] uh installed for us in uh this repo. So
[650] this nearj MCP workshop repo um we're
[654] going to leverage this later on. Um you
[656] might want to go ahead and create the
[657] code space now. If you open this repo in
[660] GitHub, click on code and then create
[662] code space on main. That'll create this
[664] like hosted containerized development
[667] environment for you uh with all the um
[670] prerequisites sort of installed in that
[673] environment for when we're going to
[674] build our own MCP server. But first
[676] we're going to start with cloud. So go
[677] ahead and download cloud desktop.
[680] Cool. So, let me uh talk for a little
[685] bit here and then we will um get fired
[688] up with with NearJ and MTVP. The other
[691] thing I should say here is we are going
[693] to use um NearJ of course uh and so I'll
[698] be using NearJ Aura. That's probably the
[700] best um best way to just spin up a
[703] freaking NearJ instance using uh near a
[706] but we'll take a look at that in a
[708] minute. I see a question here that um I
[710] have claude code. Is that okay? Um cloud
[713] code is
[715] um
[717] we're not going to look at cloud code
[718] today. Cloud code is kind of like a CLI
[723] agentic coding agents that can use MCP.
[727] Um we're specifically going to use Cloud
[730] Desktop and and see how to connect that
[732] a little bit different than Cloud Code.
[735] Um, so if you want to follow along with
[737] exactly what we're going to do today,
[738] I'd recommend uh Cloud Desktop.
[742] Cool.
[744] So, let's talk a little bit about um
[748] what
[750] MCP is and kind of how how Neo Forj fits
[753] into the the ecosystem.
[757] So, I think a few folks said in in the
[760] chat that they were totally new to MCP.
[762] a few folks I think um had some
[765] experience building MCP servers but
[768] maybe let's talk just a few minutes at a
[770] at a high level like what is MCP why why
[773] is it interesting why is everyone sort
[776] of talking about it now um and
[779] fundamentally I I think MCP is a
[783] standardized protocol right it's model
[785] context protocol it's a protocol
[787] fundamentally for exposing tools uh to
[792] AI
[793] uh applications. And so the interesting
[795] piece here is there's this sort of like
[799] birectional data flow. And and so you
[801] might uh use MCP in a chat interface
[805] like cloud desktop um you might add an
[808] MCP server in your IDE
[812] um like in cursor or VS code
[816] something like that. uh and those MCP
[820] servers, they might expose tools
[824] uh from maybe Slack or here we have
[827] Google Maps. Um maybe you want your AI
[830] application to be able to post a message
[833] to Slack. Maybe you want um be able to
[837] access data from a database in your AI
[840] application, right? MCP is a standard
[843] protocol that enables AI applications to
[846] sort of interact with data sources and
[849] tools. Um, I think that there's a lot of
[854] uh comparisons at least initially when
[856] folks were talking about MCP to the USBC
[860] uh protocol. And so I include this one
[863] because I I think this is a good um
[866] highlevel sort of um look at what the
[869] the goals of MCP are. Right? So you're
[872] thinking um as a developer of an AI
[876] application. Uh I want to connect to
[880] um Google Drive. I want to connect to
[882] GitHub. I want to connect to Slack. Um
[886] before MCP I would need to build sort of
[888] a unique API to be able to interact with
[892] those services. With MCP now as either
[896] the AI application developer or maybe
[899] the the maintainer of those services,
[901] right? the maintainer of of GitHub or
[905] Slack can publish an MCP server that
[908] defines how tools can interact with uh
[914] with those services. So to allow the the
[917] model to interact with and understand
[919] um it environment.
[922] This is a slide from a deep learning.ai
[926] course. Um, I I included this here
[929] because I I think it does a good job of
[931] kind of encapsulating
[934] uh in one slide what MCP is all about,
[937] but also is a good shout out for this uh
[940] short course. This does a really good
[941] job not just of talking about like what
[944] MCP is, um what the different pieces
[946] are, how they fit together, but um also
[949] goes through how to create um an MCP
[953] server. So this one was in partnership
[956] with Anthropic and and Deep Learning.AI.
[958] So good good resource there.
[960] Fundamentally, what an MCP server does
[963] is expose uh exposes tools, resources,
[967] and prompt templates. Most of the time,
[970] we're going to be looking at the tools
[972] that an MCP server exposes. Um you can
[976] think of these as like functions. Um and
[978] so an MCP server um is exposing these
[982] tools. your uh AI application can then
[986] leverage those tools uh to
[990] again sort of help your AI application
[992] interact with and understand uh its
[994] environment.
[997] So that's MCP. You can think of um as
[999] MCP as
[1002] again kind of a standardized way to
[1004] expose tools to models. Um, MCP I think
[1008] is really interesting right now because
[1010] it led to this inflection point in the
[1014] AI ecosystem once folks have sort of
[1017] standardized around MCP as a way to um
[1021] enable uh agents to interact with lots
[1025] of different services and and this
[1027] really it's a huge power up for sort of
[1030] extending the capabilities of what we
[1031] could build um with these AI
[1033] applications and so because of this it's
[1035] been fun to see NearJ and the community
[1037] really invest in uh lots of different
[1041] MCP functionality for Neoraj. Um and so
[1044] if we look at this page, this is in the
[1047] uh EFJ developer guides uh MCP
[1050] integrations uh page here and this talks
[1055] about the see on the the right here.
[1058] Actually, let's just open this page up.
[1061] Do that. Yes, we can do that.
[1067] So we can see here zoom in. Yeah, we can
[1071] zoom in. Cool. So we can see here that
[1074] um there are actually a few different
[1079] MCP servers for NearJ. There's the
[1082] official MCP server uh for NearJ. This
[1085] one, this is currently um out in uh beta
[1090] release. Uh we're not going to use this
[1091] one today. Although the GB repo um that
[1096] we that we're going to look at does have
[1098] some some tooling for uh installing this
[1103] GCP server. Um this is still in
[1105] development. This is a good um
[1108] drop the link to this in the chat. Um
[1110] this GitHub repo is a good place to sort
[1113] of follow the uh the progress here. And
[1116] in change log I think there's been a few
[1119] uh beta releases here. Yeah, some pre-
[1122] releases. So, this is uh the sort of
[1126] official MCP server. Again, still in
[1128] development, but there are a number of
[1130] Nefrj Labs MCP servers. Um, and so there
[1133] are a handful here. We're only going to
[1135] work with one of these, but it's
[1136] interesting to understand um what some
[1139] of these are. So, MCP near NEFJ cipher.
[1142] This is uh an MCP server that exposes
[1146] three tools. uh one for finding the
[1149] schema of your NEFJ database uh one for
[1152] executing a read cipher statement and
[1155] one for executing a write cipher
[1157] statement. So the MCPJ cipher server
[1162] this is when you want your uh model to
[1166] generate database queries and then
[1169] execute um those database queries
[1171] against NearJ.
[1174] Um, another one is the MCP nearj memory.
[1177] Um, this one is interesting. This is
[1180] kind of a an implementation of the
[1185] uh knowledger graph memory server that's
[1188] included in the MCP reference
[1190] implementation um that uses nearj. So
[1192] this is a look at how we could use um
[1195] knowledge graph memory with our AI
[1198] agent. There's an MCP server uh for
[1201] nearj aura. So it allows us to create
[1204] instances, list our instances. Um so not
[1207] interacting with the databases
[1208] themselves but rather provisioning
[1210] instances. Um there's the
[1214] uh data model server which uh can help
[1219] us with
[1221] creating data models for Neoraj. There's
[1224] the GDS integration which allows us to
[1226] um use graph algorithms uh with Neoj
[1229] through MCP. uh and then the MCP sandbox
[1232] uh server which allows us to create
[1235] NeoFj sandbox instances. And so what's
[1237] interesting here is that you can see
[1239] some of these are are sort of meant to
[1242] be used with developer tools, right? So
[1245] we'll see this in a moment. Um where
[1247] we're going to use the ERJ cipher server
[1251] in VS Code to help us like tune some
[1254] cipher queries to help us generate some
[1255] cipher queries but also to help us
[1258] manage servers or services rather. So to
[1261] help us provision Nefj instances this
[1264] sort of thing. And then there are lots
[1266] of uh integrations with agent
[1268] frameworks, right? Because MCP is a way
[1271] to integrate uh services into a
[1275] applications. So if you're using um
[1277] Google's ADK, lang chain, lane graph,
[1280] hydantic AI and so on. Um you can see
[1283] examples of using uh MCPJ
[1288] MCP server with this. So that's kind of
[1290] an an overview of like the existing uh
[1293] NEFJ servers that are out there.
[1295] Hopefully that uh that kind of
[1298] might show a little bit about kind of
[1300] the difference of the um official NEFJ
[1303] MCP and and some of the labs MCPS that
[1306] are out there. Cool. So hopefully that
[1308] is enough of um
[1311] uh of a overview of MCP. Um, I want to
[1315] spend the rest of the time really
[1316] hands-on showing how we can use some of
[1318] these different tools together. So, I
[1320] think we'll um we'll pause there kind of
[1323] on our our rough overview of MCP. But,
[1326] if there are any questions um that folks
[1328] have that kind of didn't cover
[1331] um sort of an intro to MCP, we can
[1334] definitely make sure we um address those
[1336] now before we jump into setting up um J
[1341] Aura and Cloud Desktop. So maybe we'll
[1343] pause here for a second.
[1345] >> Yeah, there was um wasn't um too many
[1351] questions. Um I think the one the one
[1353] question um that is interesting maybe um
[1356] is from Brett who wants to know if
[1359] there's a remote hosted version
[1360] available or any plans for there to be.
[1363] I would love to see it um as tooling for
[1366] cloud hosted AI orchestration agent
[1368] workflows uh they use.
[1372] So at the moment the NEOJ one is not
[1375] available as a hosted one. You have to
[1376] deploy yourself and I don't know when or
[1381] if there will be a hosted one available.
[1383] Um so I I I
[1386] would imagine that maybe this could
[1388] happen but um at the moment it's not um
[1392] not announced.
[1395] >> Yeah. Yeah. And I think just as um as
[1397] kind of an outsider looking in, I I
[1399] think that uh as we see kind of the
[1405] MFJ Labs MCP servers, we've seen those
[1408] um that have been like community-led um
[1411] efforts out there and now we're seeing
[1413] official MCP server um that that's
[1416] getting a lot of development. I think
[1417] that might be kind of the the path to um
[1421] hosted MCP. And again, I just looking um
[1425] looking in from the outside, I I could
[1426] see that kind of being the path there.
[1428] So, I imagine this is this is something
[1430] that um that is on the radar for sure.
[1432] Yeah, good question.
[1433] >> Yep, definitely. Um the other question
[1436] is when what to use when you have and a
[1439] specific one to the workshop today um
[1440] when you have Linux uh because cloud
[1442] desktop is only available for Windows
[1444] and Mac. Anything you can suggest to
[1447] people?
[1449] >> Right. Um that is a good point. Um if so
[1456] cloud desktop does not run um on Linux
[1458] which I I didn't realize. Um apologies
[1461] for that. I would say maybe um maybe
[1465] don't try to follow along with that
[1468] section. If there's another um MCP
[1472] host application that you've used like
[1475] cursor, we're going to use VS Code um in
[1479] in a moment too. So maybe maybe try one
[1481] of those instead of cloud desktop and
[1484] and I'll I'll show how to how to do this
[1486] in VS Code as well. I like to start with
[1488] cloud desktop because it's um it's again
[1492] it's like free to get started and um in
[1495] most cases it works for a lot of folks.
[1499] Um folks are saying some success with
[1502] zed um if they're using Linux. Yeah. and
[1504] and a lot of the the concepts like we
[1506] we'll look at cloud desktop, we'll look
[1508] at VS Code, but a lot a lot of the
[1509] concepts um of you know sort of how do I
[1512] connect to how do I connect my EFJ MCP
[1515] to a um MCP host application a lot of
[1519] those are going to be the same um
[1520] similar ideas whether you're using cloud
[1522] desktop code Z any any of those sort of
[1526] agentic tools that support MCP are going
[1528] to be similar
[1530] >> yeah and then one more time what do
[1532] people need to download from from the
[1534] repo you shared you shared.
[1539] >> Yeah. Uh let's see here. So here's the
[1543] repo. I'll drop a link to this in the
[1547] chat.
[1550] And um this is going to be kind of the
[1552] the second hands-on piece, but we're
[1554] going to use this thing called uh code
[1557] spaces. Um, and so if you go to code
[1560] code spaces and then I've already
[1562] created one, but you'll have this button
[1564] to like create a code space on main.
[1565] Click that and that will open up this
[1568] sort of like hosted VS Code development
[1571] environments um, which will install some
[1575] dependencies and get us ready for the
[1578] workshop.
[1579] >> Okay, cool. Maybe you can zoom in a
[1583] little bit. um when when showing code I
[1585] think for the slides it was fine but for
[1586] the code we need I think we need a
[1588] little
[1590] little enlargement
[1592] >> cool sounds good but other than that I
[1595] don't see any other questions uh so I'll
[1597] I think we we can continue
[1600] >> cool sounds good well yeah so what I
[1604] want to do now is
[1607] uh take a look at exploratory data
[1611] analysis with with nearj JMCP. So, so
[1613] there are roughly
[1615] a a couple of different use cases that I
[1617] want to take a look at for uh using near
[1621] JMCP. Um the first is roughly in in this
[1625] area of like helping us learn new
[1628] developer tools. Um and so uh in this
[1632] case we're going to start with an empty
[1635] NearJ instance. Uh and we're going to
[1637] connect cloud desktop uh to our NearJ
[1640] instance. and then uh help us to sort of
[1644] create a graph data model to load some
[1647] load some data uh and explore our graph.
[1652] So cool. So yeah, so go to cloud.comd
[1655] download setup um cloud desktop if you
[1659] haven't done that um already. That'll be
[1662] the first step here. cloud.com
[1667] download
[1672] Mac or Windows. And again, if you're
[1673] using Linux or um or if you have another
[1678] MCP host application kind of like like
[1680] an agentic coding app like VS Code or
[1682] Cursor, something like that, feel free.
[1685] Um, we're going to use Claude
[1692] and we are also going to use
[1700] uh let's go to our
[1708] want
[1712] slash
[1714] docs.
[1715] We want the developer guides
[1722] on Genai.
[1727] This is the page I'm looking for.
[1734] And what we're going to do is get the
[1735] EFJ Cypress uh MCP server up and
[1738] running.
[1743] So, let's take a look at the
[1746] documentation. Drop a link to this in
[1753] the chat. There we go. So, this is the
[1756] uh first EFJ MCP server that we're going
[1759] to work with. This is the uh MCPRJ
[1763] cipher.
[1765] And we can see here that there are um a
[1768] couple of tools. Read cipher, write
[1770] ciphers. These are executing read or
[1771] write statements and then um get the
[1774] schema which is going to return the data
[1776] that is already loaded in uh the
[1779] database. And we can see here there are
[1781] lots of different options for um things
[1784] like how to configure the the transport
[1786] mode, where to uh how to connect this
[1790] with different
[1794] um
[1796] different MCP host applications like
[1798] cloud desktop. We're gonna use Cloud
[1800] Desktop. And so, um, I think the easiest
[1803] way to do this is probably to,
[1806] um, in the
[1809] documentation, copy this code block
[1812] here. So this is the configuration for
[1816] configuring and adding an MCP server to
[1820] cloud desktop uh which has become kind
[1822] of the standard format for how we can uh
[1826] add MCP servers to MCP host
[1830] applications. And in Claude, I'm going
[1833] to go to settings
[1841] and developer
[1845] and edit config.
[1848] And this is going to take me to
[1851] uh editing. I'll open this up. Text
[1854] edit. That's probably good enough. um
[1858] the
[1860] cloud desktop config and we can saw we
[1862] can see I already had a um configuration
[1864] in there
[1866] that's fine. So here I pasted in um the
[1870] configuration for starting the
[1874] MCP nearj cipher MCP server um and then
[1880] there's some Neoraj connection
[1882] credentials here that we'll need to fill
[1884] in in a moment. Yeah, this is the way
[1886] that we add uh MCP servers to Cloud
[1890] Desktop. So again, I went to uh settings
[1895] in Cloud Desktop developer and then um
[1899] it showed me some existing NFj servers
[1901] or some existing MCP servers. You may
[1904] just see something like this edit
[1906] config. Um, and this this just like
[1908] opens
[1910] uh Finder or whatever to open this cloud
[1913] desktop config file. And then I pasted
[1916] uh that block in from the readme.
[1920] Cool. So, let's let's take a look at
[1922] what's going on here. Um, well, this is
[1924] this is a JSON configuration. Uh, we're
[1928] telling Cloud Desktop that uh what MCP
[1933] servers we want to connect to. Here
[1936] we're naming uh the server.
[1941] Zoom in as much as we can. There. There
[1944] we go. Uh so the name is going to be
[1945] near database.
[1947] And then uh the command to run the MCP
[1952] server. We're going to run this locally.
[1956] Um so the or we call it an MCP server.
[1961] It's going to run locally on our
[1963] machine. uh and connect to a NEFJ Aura
[1968] instance. So, UVX is the command that
[1971] we're going to use to run this MCP
[1974] server. Um if you're not familiar with
[1976] UVX, UV is a package manager for uh
[1980] Python. Uh and so UVX means run this
[1984] package MCP nearj cipher. Uh and then
[1988] we're specifying um the transport. So
[1992] there are uh
[1995] several different um transport methods
[2000] available with MCP. Um standard IO, this
[2004] is a common one for
[2007] uh MCP servers that we're running
[2008] locally. Streamable HTTP um is the
[2012] common one when we're have when we're
[2014] working with uh remote MCP servers.
[2017] We'll take a look at that in a moment.
[2021] And then we're specifying uh the
[2024] environment variables to connect to our
[2026] Neoraj instance.
[2029] So that's the next piece we need to fill
[2032] in here. Uh and so I'm going to go to
[2037] Nej aura next.
[2043] Maybe
[2045] I can find my
[2048] sorry.
[2052] Uh so NEFJ Aura is where we can create
[2056] um our
[2058] free uh Nefjura instances if if we want
[2061] to follow along in the workshop with a
[2063] free instance or we can also create um
[2067] professional tier Aura instances. I have
[2069] a few running. Um this is my
[2073] or a free instance professional. Um
[2077] here that I've created one
[2079] console.nefj.io.
[2081] I'll drop a link to this in the chat is
[2083] the
[2087] URL to sign in to aura. Uh and then
[2092] we'll create an instance. Um and you can
[2094] create
[2096] uh maybe one one or two free instances.
[2099] And then um beyond that you should have
[2102] a free tier. I forget how it works. Is
[2105] is it like 14 days? Something like that.
[2107] But anyway, the the free tier which is
[2108] perpetually free. That's fine. You can
[2110] use that one. Um
[2114] should be good enough for today. Lots of
[2116] other interesting things. Um Alex
[2118] mentioned the uh Aura agents feature
[2122] which is in preview now. This is going
[2124] to be covered uh in depth I think
[2127] tomorrow in tomorrow's um road to nodes
[2130] workshop. So be sure to check that out.
[2132] We'll we'll skip over that uh
[2133] functionality for today. It should be a
[2135] good one.
[2138] Cool. So uh create an instance free
[2140] tier. Um if you want to follow along I
[2144] already have created an instance here.
[2147] um you get sort of a little popup here
[2151] with your connection credentials when
[2154] you create an Aura instance. So let's go
[2157] ahead and update our placeholders here
[2160] for the NeoRaj URI.
[2164] And so on the right here, this is what I
[2166] um
[2168] what I downloaded when I create my
[2170] NeoRaj Aura instance. Um this gets
[2172] downloaded automatically.
[2175] So, here's my
[2178] URI
[2181] password.
[2185] Um,
[2189] um, oh yeah, I think I I originally saw
[2192] that is because I was messing around
[2194] with this in claw desktop. Okay, so
[2197] we'll go ahead and do that. And then um
[2199] the next piece is I think we need to
[2202] actually restart uh Claude to pick up
[2205] those changes. So I'm going to go to
[2207] cloud desktop and just quit it. Restart
[2211] it.
[2218] Restarting cloud here.
[2226] Cool. And so now uh when I click on this
[2230] little tool indicator here,
[2234] I can see there are a few different
[2236] connections that I have like web search.
[2239] These are some of the the built-in
[2240] connections that Claude has. But I have
[2243] this new uh Nefj database uh MCP server
[2248] which I can toggle on and off. And then
[2250] these are the tools uh that have been
[2253] discovered. So there's the getj schema
[2257] uh execute a read cipher statement
[2259] execute a write cipher statement. And so
[2263] the first thing I like to do is always
[2266] test this by saying something like what
[2268] data
[2270] is in my
[2273] near instance.
[2278] And so now we're going through kind of
[2281] the
[2282] this like agentic loop with Claude,
[2284] right? And and so Claude has um a big
[2288] long system prompt that is something,
[2290] you know,
[2293] roughly something like be as helpful as
[2295] you can, use your tools to respond to um
[2300] the user's messages, this sort of thing.
[2302] And so because I'm saying what data is
[2305] in my Neoraj instance the model Claude
[2308] is deciding uh the
[2312] best way to respond to this is to call a
[2314] tool the get near schema tool uh which
[2318] is going to fetch data uh from the
[2322] database and determine what data is
[2327] loaded in there.
[2331] Cool. And I have
[2333] data in this database. Let me um let me
[2336] delete this. Actually, this was a an
[2340] empty instance. Let's go ahead and clear
[2343] this out so that we're all starting from
[2347] the same spot here.
[2353] So, that is this one. I think
[2360] let's go in here and we'll just delete
[2366] or grab our password rather so we can
[2368] delete
[2369] our nodes.
[2373] Cool. So, uh if you're not familiar too
[2375] much with NearJ, this is a query which
[2378] is like a a query workbench for NearJ.
[2381] This here's some data that I already
[2383] have loaded. We'll take a look at this
[2384] in a minute. I'm just going to
[2389] delete everything. So, match in detach,
[2391] delete.
[2393] Cool. Now, there's no data in my
[2395] database.
[2397] If I go back to Claude, let's create a
[2400] new
[2402] chat here.
[2404] We'll say what data is in my
[2408] Nej database.
[2417] And now this time when we call uh get
[2420] schema it returns an empty result.
[2424] Uh and
[2426] Claude is going to verify like hey like
[2428] let let's verify this now. Let's
[2430] actually run a
[2432] cipher statement. Uh and you can see
[2435] here it's going to run two statements.
[2437] One is just counting the number of nodes
[2440] and one is counting the number of
[2441] relationships.
[2443] >> And so if we can see what what's going
[2445] on here like what's interesting is
[2448] >> we can use a little little bit into that
[2451] uh that view. It's a bit a bit tiny.
[2453] Yeah, I think that's better. Thank you
[2455] very much.
[2456] >> Cool. Thanks.
[2458] What's what's interesting here is that
[2459] it's the it's the model that is
[2463] generating the database query, right? So
[2466] we can see here that get nearj schema uh
[2471] doesn't really seem to take any
[2473] parameters. Uh but the readj cipher tool
[2478] that does take uh parameters which is
[2482] the query that we want to execute.
[2484] Where's that query come from? It's the
[2486] claude model. So our our AI application
[2489] model that is generating that database
[2492] query that doesn't come from the MCP
[2495] server um MCP server is essentially just
[2498] like exposing this as a tool saying like
[2500] hey I can execute cipher statements
[2504] AI application like claude in this case
[2507] give me the the query to execute is how
[2511] this works.
[2514] Cool. Well, we have no data in our
[2516] database. We want to be able to um sort
[2520] of work with Neoraj through MCP a as a
[2524] developer a as an analyst. Maybe I want
[2526] to be able to um interactively develop a
[2532] a data model. And so let's um work with
[2538] Claude to help us come up with um a
[2541] graph data model for let's say a
[2544] e-commerce application. Um so we'll say
[2547] something like um help me create a
[2553] graph data model for a
[2556] uh e-commerce
[2559] application
[2561] uh knowledge graph.
[2564] Let's say create uh sample data in near
[2568] the J. So I want to build um an
[2571] e-commerce knowledge graph let's say uh
[2574] and I want to just load the data load
[2578] nej with some uh sample data uh is the
[2582] goal here. Um and so we can see here
[2586] that
[2589] claude uh is just generating uh some
[2594] cipher statements to load the data here.
[2597] First it created
[2599] uh some customers now products and so
[2602] on. Uh and it's going to go ahead and
[2605] load that data in our Aura instance for
[2609] us.
[2612] Now this is an interesting area where we
[2615] can actually work quite a bit with the
[2618] prompt here. Notice that
[2622] uh our model just
[2625] started creating data in the database,
[2628] right? We didn't have this sort of like
[2630] back and forth uh where first it maybe
[2633] gave me a diagram of the data model that
[2636] it wanted to uh to use. Maybe um specify
[2640] the features that we want to use. And so
[2643] uh this is typically where we want to
[2645] tune the uh system prompt for our agent.
[2650] In Claude, we do this by creating um
[2654] projects or uh or sub agents um where it
[2660] allows us to sort of create rules or or
[2663] sort of tune the prompt uh where we
[2665] could specify uh like user preferences
[2668] like hey don't just create data uh when
[2670] I ask you to help me create a data model
[2673] and sample data like help me uh iterate
[2675] with the user that sort of thing.
[2679] Another important thing to note here um
[2681] as we're thinking about how this works
[2683] is that the
[2686] model is not always going to generate a
[2688] perfect
[2690] uh cipher statement, right? Like um the
[2693] textto cipher uh concept, right? Where a
[2698] model is generating a cipher statement
[2700] based on um some text is pretty good,
[2704] but it's not always going to be uh going
[2707] to be perfect. And so, uh, Claude is
[2710] good about this, but something just
[2711] something to think about as we're
[2713] building a applications ourselves is
[2714] that we want to have this like
[2716] iterative, uh, environment where if we
[2719] maybe generate a database query that,
[2722] um, is not correct, our AI application
[2726] is able to to deal with that.
[2728] Cool. So, this is the uh, the data model
[2731] that
[2733] our
[2735] claude agent uh, came up with. products,
[2737] categories, customers, orders,
[2739] addresses, vendors, payment methods.
[2742] These are the nodes. Uh we have
[2746] uh wish lists,
[2748] wish list belongs to
[2751] customer, product is in a category, um
[2754] and so on. And we have some example
[2757] queries and and so on. Uh, one thing I
[2759] like about Claude is the artifact
[2762] feature where it's really good um at
[2766] creating
[2768] uh diagrams or creating like JavaScript
[2772] code and and running it. So let's say uh
[2776] create a graph
[2779] visualization
[2780] um
[2782] that shows all
[2785] customers and products ordered.
[2790] So here's where we get into sort of the
[2792] exploratory data analysis, right? So,
[2794] so, so far what we've done, um, we just
[2797] rewind a little bit here is we've
[2800] connected our Neoraj MCP server to Cloud
[2805] Desktop. Uh, and we've kind of verified
[2810] that we're able to expose the tools from
[2814] the the NEFJMCP server to Claude
[2816] Desktop. We asked Claude to help us
[2819] create a graph data model for an
[2821] e-commerce app and load that into Neo
[2824] forj and we generated some uh cipher
[2827] queries to create that uh in the
[2829] database. And now we asked for a graph
[2833] visualization showing all customers and
[2834] products. And so the the first thing
[2836] we're doing is fetching data. So here's
[2838] a generated query, customers, orders,
[2841] products, turning all that information
[2844] uh to then feed into the graph
[2846] visualization using D3 that that Cloud
[2849] is going to generate for us. Um so we'll
[2851] let that run for a minute. See what what
[2852] Cloud comes up with. Um cool. Here it
[2855] is. Don't have to don't have to wait for
[2858] that. Let's see. We can look at that.
[2860] Yeah, cool. So this is um this is an
[2863] artifact uh feature.
[2867] which
[2870] looks like we didn't cla didn't quite
[2873] vibe code correctly, but that's okay. We
[2876] can
[2878] tell that we have an error here. Um, but
[2881] essentially
[2883] the idea here is that we're generating
[2885] some code to help us visualize some some
[2888] data from the graph is essentially the
[2891] idea. So that's where the exploratory
[2893] data analysis piece comes in is that uh
[2897] we can
[2900] interact in natural language with our
[2905] uh with our agent and
[2909] MCP allows the uh agent to interact with
[2914] the database by generating database
[2916] queries. Claude also has some
[2918] functionality for generating these
[2920] artifacts to help us make sense of um of
[2922] this data. Cool. So, we'll we'll pause
[2924] there. Um really what I what I wanted to
[2928] cover in this section I think was was
[2930] really just showing how we can
[2933] uh fire up this MCP nearj cipher tool uh
[2936] and how we can connect that to cloud
[2940] desktop. Um some of the things that we
[2943] can do in cloud desktop for interacting
[2945] with Neo forj through natural language
[2948] can help us generate um data in the
[2952] database exploratory data analysis help
[2954] us sort of generate uh database queries
[2957] and work with the results. So we'll
[2959] pause there um and maybe answer any
[2963] questions that come up here.
[2970] Uh so there's one question uh from
[2973] Sanchalita
[2975] Sanchalita. Yes. How is security
[2977] implemented when claude is writing to
[2979] Aura DB?
[2983] >> Yeah, that is a great question. Um
[2987] security around MCP this is always um
[2991] always an important thing to think
[2993] about. So in this case, let's go um
[2998] let's go here to look at our tools.
[3000] There there are a few things that we can
[3003] uh look at as we think about security.
[3006] So one thing is we can uh we can sort of
[3012] control
[3013] what functionality our AI agent in the
[3017] space cla um is able to do with our
[3021] database at the tool level. So the nearj
[3025] cipher MCP server has three tools. Um
[3030] one that exposes the schema, one that
[3032] executes readonly cipher statements and
[3035] one that executes write cipher
[3037] statements. So if we for instance wanted
[3040] to just have readon access, we could
[3042] disable this tool, right? So we could
[3045] not expose this tool to our AI
[3048] application in this case cloud. and say
[3049] you can only have access to the read
[3052] tool or uh the git schema tool. Um that
[3056] that's one thing to consider is just
[3058] thinking of and and especially as you're
[3060] building your own MCP servers like what
[3062] uh tools you want to expose. The other
[3066] thing to think about is when we
[3068] connected to claude here um when we in
[3074] our cloud configuration
[3076] we specified um what what Python package
[3080] we want to run for the MCP server and we
[3083] specified the Neo forj user. So this is
[3086] our our like administrative
[3088] uh database user. we could create a
[3090] database user that has uh certain
[3092] permissions only to maybe certain data
[3094] that we want to um to access in the
[3097] graph through MCP um and be sure we're
[3100] connecting uh to NearJ through the MCP
[3102] server through that database user. So
[3104] that's another way to um to think about
[3108] security uh in different ways to make
[3110] sure you're not exposing too much uh too
[3113] much permission, too much data to your
[3116] um MCP server.
[3119] and you you you can identify what a user
[3122] sees and doesn't see uh through through
[3125] the role based access management. So you
[3127] could limit it somewhat through that.
[3132] >> Yep.
[3134] >> Uh there's another question from uh
[3136] Claraara. Claraara asks, "Are queries
[3139] kept in Neo forj when when you send
[3142] something over or is it just um sitting
[3145] there in cloud?"
[3147] >> Um so I guess yeah, it's just kind of um
[3153] queries are generated by Claude, right?
[3155] And and so let's look at one of our tool
[3159] calls here. Uh well, here let's let's
[3163] try this. Um, let's
[3166] say create a personalized
[3170] recommendation query for
[3174] Carol White. So, Carol here is one of
[3177] the users. She bought a KitchenAid mixer
[3180] and an Instant Pot. And I want to
[3182] generate um personalized recommendations
[3185] for this user, Carol. Um,
[3188] >> so it's the the AI application in this
[3192] case, right? So Claude, so that's
[3194] generating the database query and and so
[3197] Claude is going to use like the context
[3199] that it has. So it it understands the uh
[3203] the schema that the data model uh and
[3206] it's going to generate that query and
[3208] then here it's going to try
[3211] to execute this. We'll see it does get
[3214] back some uh some results. Maybe needs
[3215] to to tune that. Um but anyway but yeah
[3218] those queries like one to to clarify
[3220] those are first of all generated by the
[3224] model um so in this case like the claude
[3227] sonnet or five and then the AI
[3230] application so cloud desktop um can
[3235] execute those queries through an
[3237] invocation of in this case the read
[3239] nearj cipher tool and it passes the uh
[3243] the cipher query to run and then the
[3245] results uh you can see the the JSON
[3247] result here. This is the result that
[3249] comes back um from the database that
[3252] then lives in context um in the the like
[3256] context window of this chat that that's
[3259] managed by claude of course but like
[3261] it's um an important thing I guess
[3264] important pattern to like keep in mind
[3266] as you're as you're interacting with um
[3270] >> with agents through this sort of chat is
[3272] I I like to say I like to start off
[3274] something easy like what data is in my
[3275] nearj database and that's because
[3279] >> the model is going to start it's going
[3281] to like choose the tool it's going to u
[3285] build up in its context the result of
[3287] those of those tool calls and so um so
[3291] the results of those queries live in the
[3295] context of in this case claude um but
[3298] but anyway to answer your question no
[3299] like they're not they're not actually
[3301] stored in Neo forj like the the cipher
[3305] queries generated by the model executed
[3308] against NearJ through the tools that
[3311] we're exposing through the MCP server,
[3314] but the results of those uh tool call in
[3318] invocation. So running those cipher
[3320] statements, that data stays as context
[3323] for the model and the results um uh of
[3326] this conversation throughout my like
[3328] agentic chat uh with Claude in this case
[3331] if that makes sense.
[3333] Yeah, I I think you could pro probably
[3337] look at this if you have monitoring
[3339] tools enabled that see what users did
[3341] what queries and then probably they
[3343] would show up.
[3345] >> But that's a little bit complicated.
[3349] >> Yeah. I if you were um if you were like
[3352] managing an EFJ instance and and you
[3354] wanted to see what queries were executed
[3356] by which user, yeah, there there's like
[3359] um query logging and functionality you
[3361] can enable per user to to try to find
[3364] that. So yeah, kind of depends on on
[3365] what you're trying to accomplish there
[3367] for sure.
[3368] >> Yep. Yep. Um then there's one question
[3372] from Anand. Anand asks, how does claw
[3374] generate the cipher query? Is it purely
[3376] based on the graph schema or is there
[3377] any any other um you know tips or tricks
[3382] well not little tips or tricks but is
[3383] there any other features that it has uh
[3385] to create the the queries?
[3388] >> Yeah. So it's it's a few things right
[3391] it's one the data that the model was
[3395] trained on. Um and so these like
[3399] foundation models, they have lots of
[3402] SQL, cipher, like lots of different um
[3406] understanding of of the syntax and and
[3410] functionality of of cipher and other
[3411] database C images. So that that that's a
[3413] big piece of it. Um then the other piece
[3416] is like the context that is built up in
[3420] this chat. And so for example, that can
[3423] be the schema. So when I say what data
[3425] is in my NEFJ database, the the result
[3429] of this like the understanding of the
[3431] model um is built up in context. And so
[3434] then the AI application is able to
[3436] leverage its understanding um of the
[3440] data that that it was trained on like
[3442] the syntax of cipher essentially the
[3444] context that it has. So like the
[3447] information about the current schema,
[3450] what data is in the database um is
[3452] another piece. And then also like to
[3456] help manage that context there there are
[3458] other tools that allow you to um inject
[3462] documentation
[3464] um and
[3466] uh depending on
[3469] what AI application or or like agent
[3472] coding system you're using. There are
[3474] different ways to do that. Either um
[3476] index docs pages directly or through MCP
[3480] that sort of thing. But I think the when
[3482] you're talking about sort of cipher
[3485] generation here, those are yeah the the
[3488] two fundamental pieces are kind of the
[3491] data that it's been trained on at the
[3493] model as a whole. Um and then anything
[3496] that's been built up in the context
[3498] which can include understanding the
[3500] database schema um
[3504] database queries that have run
[3506] previously that again some sometimes
[3508] they they air out and need to
[3510] iteratively um execute those. And then
[3513] thirdly, anything we want to inject into
[3516] the context like additional
[3517] documentation
[3521] >> and there was a add-on sort of from from
[3524] Crispen in chat and Chrisen says I
[3526] thought Neoj was able to be schemaless.
[3528] Neforj is able to be schemaless, but for
[3531] for these um LLM based tools, it is
[3535] always good to give a little schema
[3536] because otherwise they bounce around a
[3539] lot and come up with all kinds of crazy
[3541] ideas of of what your schema should look
[3543] like or what your data model should look
[3544] like and this keeps them a little bit
[3546] more in in line, I would say.
[3552] Yeah. I I I think that
[3555] I think of it at least as as the data
[3558] model at least, right? Um
[3560] >> Yes. Yeah. Yeah.
[3561] >> Maybe we're not like imposing some some
[3564] strict schema, but we we certainly have
[3566] a data model that we're working with and
[3568] and we have it here, right? Like for our
[3571] um our shopping example. Um where's our
[3575] these are our recommendations for Carol
[3577] but where's our um our visualization.
[3581] So anyway yeah like like any application
[3584] has a data model for your database. You
[3587] can think of that
[3590] uh as
[3592] a schema is kind of how we refer to it
[3595] in the the terminology here in the MCP
[3598] tooling. Like like if you look at this
[3600] get nearj schema um
[3604] with let's try it now. Show me my if I
[3607] say show me my Neo forj schema. Um
[3612] really what it's doing is is inspecting
[3614] the data that's in the database. Not
[3616] necessarily that there's like a
[3621] top-down
[3622] schema that's enforced by the database,
[3624] right? Like that's what we mean when we
[3626] say nearj is schema optional is I can
[3628] sort of I can define constraints as
[3630] needed to
[3632] to define my data model. But anyway,
[3634] lots of interesting things there around
[3635] like ontologies and these sorts of
[3637] things you could
[3640] >> Yeah. Yeah.
[3645] Um cool while this loads
[3648] >> I don't know do we want maybe one more
[3650] question um in terms of compatibility
[3653] and maybe I don't know if you have any
[3654] experiences with this ling asks if
[3658] neo forj co-pilot is is that something
[3661] that could be adjust adopted similar to
[3663] what um what you just showed here with
[3665] claude
[3667] >> yeah totally and and that's actually our
[3668] our next example um we're going to take
[3671] a look at using the nearfj mcp server
[3675] with C-pilot. Um, so that this sort of
[3679] chat functionality that we have in
[3681] claude where we're just kind of like
[3683] generating queries and generating like
[3686] uh nice visualizations. Yeah, we're
[3688] going to see how we can use that as a
[3689] developer to help kind of like tune some
[3692] queries in in VS Code sort of thing.
[3696] >> So, we'll see that in a sec. That's a
[3697] great great segue for us perhaps.
[3701] >> Yeah, that's a good segue. Exactly. I I
[3702] see a couple lot of questions on on
[3704] tuning queries um you know um how to
[3707] address that and how to how to optimize
[3710] um you know query execution or query
[3713] query planning from Jerry for example
[3715] here comes I don't want claw to execute
[3718] the query immediately I want maybe
[3719] confirm before it executes is is that
[3722] something you can do um
[3725] with with the um with the MCB models we
[3728] have
[3730] >> totally yeah so like um that's going to
[3733] be something where you're going to want
[3736] to control that at the AI application
[3740] level. Um and typically that's handled
[3743] through like the system prompt for uh
[3749] for your your agent. Um in cloud this is
[3753] done at the uh project level or uh
[3758] there's another thing called a sub aent
[3759] um for cloud code but we can do this um
[3762] at the project. So the cool thing about
[3765] the project is that it allows us to um
[3768] to kind of tune the prompt a little bit.
[3771] So we can say what are we working on?
[3773] We're working on I don't know e-commerce
[3777] uh knowledge graph. We're using
[3781] uh Neo forj to help build e-commerce
[3787] knowledge graph tooling.
[3790] And so in this project
[3793] um we can uh store
[3797] instructions. Um if you use something
[3800] like cursor that this could be something
[3802] similar to like cursor rules. And so uh
[3805] we're going to say you just say
[3807] something like when given a
[3811] request to
[3814] create an application data model
[3819] um always
[3821] suggests always say make suggestions
[3827] to the user for
[3831] confirmation.
[3832] never just execute
[3837] cyer statements. Right? So we can kind
[3840] of tune that um in the instructions
[3843] uh so that now we can say like uh I want
[3847] to
[3850] create a graph
[3854] data model for new commerce app
[3860] in the sample data. So now
[3864] we should use that instruction as part
[3866] of the prompt and yeah so now we can see
[3870] here's our proposed e-commerce data
[3872] model um here's some samples like
[3876] do you want to model this or do you want
[3879] to iterate on this that sort of thing
[3882] and so the reason we reason didn't just
[3884] create uh that data in the graph when we
[3887] use basically the same user message is
[3890] because of that instruction
[3892] that we gave it in the project
[3895] which is right here. So we said
[3899] whenever we're given a request always
[3901] you know make suggestions and and have
[3904] the user give confirmation.
[3908] >> Cool.
[3909] Um yeah uh I think in the interest of
[3912] time let's let's continue. Maybe um at
[3915] some point you can show show us how this
[3917] this looks like in Neo forj. I think
[3919] there was another question from
[3920] Gabriella. Maybe maybe not for whenever
[3923] it fits so we can uh we can see uh what
[3926] what it actually did on the on the
[3928] database side.
[3930] Cool. Yeah, let's do it. We can do that
[3932] right here. So if I switch over to Aura
[3938] in the query tab.
[3941] So, I just
[3943] hit the the star here to find uh
[3948] find some nodes. Here's the um
[3953] the rough
[3956] data example that we have. So, here's
[3959] what is green. So, here's an order. Uh
[3962] this order was Oh, and let me zoom in as
[3965] much as I can here.
[3974] Sorry. There we go.
[3979] Okay. So, yes. So,
[3987] here's our user Alice. Alice has placed
[3992] um a couple of orders
[3994] like this order
[3996] uh contains Levis's.
[4000] Don't have any other uh Oh, so she
[4002] bought Alice bought Levis's and an
[4005] iPhone 15 Pro
[4009] in this order. And we have some
[4012] additional information and some
[4013] additional nodes are added like
[4014] frequently bought with. So, uh, the
[4018] Samsung Galaxy is frequently bought with
[4021] Levis's. These are in the category men's
[4024] clothing.
[4025] Um, we have a bit of like a hierarchy,
[4030] right? Men's clothing belongs to the
[4032] clothing category. So, we have some like
[4035] product category here that could be
[4037] useful for recommendation queries. Um, I
[4041] think we also had
[4045] the payment method.
[4050] So, here's another order.
[4055] Yep. Cool. So, that's that's what that
[4057] looks like in Neo forj.
[4060] Uh, and again, this is the the sample
[4061] data created by Cloud for us.
[4067] Cool. So yeah, let's uh move on to kind
[4070] of the next example that I wanted to
[4072] look at which is uh building your own
[4076] MCP server. So, so far we saw uh how you
[4080] can use the existing Neo forj uh MCP
[4085] servers that uh well specifically we saw
[4088] using the cipher uh tools to create um
[4094] to execute cipher statements um in near
[4098] using statements generated in an AI
[4100] application like cloud desktop. Um, now
[4104] we're going to look at a couple of
[4106] examples where we've created our own uh
[4110] MCP server. Uh, and to do that uh we're
[4114] going to use the um this existing GitHub
[4118] repo that
[4122] is right here in GitHub. I'm going to
[4125] drop a link to this in
[4128] chat.
[4132] And what I want to do is open this code
[4135] space environment. You you can certainly
[4137] clone this and and run it locally. Um
[4140] there's a a Python or a TypeScript
[4142] example. Um
[4145] that's probably fine. Um I don't think
[4148] if you have like a typical uh en
[4152] environment setup you should be okay
[4154] locally. I'm going to create though this
[4156] um this code space instance
[4159] which gives us this VS code like
[4162] environment um running in a
[4166] containerized development platform.
[4170] Anyone using code spaces? I'm curious
[4173] like regularly. I like to use these for
[4175] workshops, but I know some folks use
[4178] these for for regular developments as
[4180] well.
[4185] Cool. So, let's see. I don't think we
[4187] have much to say in the slides here
[4190] before we get into this, but let me just
[4192] double check. Nope. Cool.
[4202] Okay, that one over here.
[4207] Sorry, my um
[4212] screen is misbehaving.
[4227] Um, okay. So, where were we? Code space.
[4231] This guy.
[4236] Cool. So, let me just make sure
[4241] we got any questions while we're waiting
[4244] for this to set up or any questions
[4246] about the setup.
[4249] Let's see.
[4259] Cool. Well, if you have any any issues
[4262] getting code space set up, definitely
[4265] let us know in the chat.
[4275] Cool. So, um
[4279] let's go ahead and see uh
[4284] what we have here.
[4287] We'll zoom in. Let's get as much space
[4289] as we can. Okay, cool. So,
[4295] the
[4300] this looks like an older version
[4303] actually. Let me um
[4306] this looks like a somewhat older
[4307] version. Let me delete this one
[4311] and create a new code space.
[4318] And while that loads
[4321] um we'll walk through
[4324] some of the code here. So okay cool. So
[4326] we saw how to use the MCP server uh for
[4332] Neoraj where the
[4335] sort of functionality
[4338] uh to execute arbitrary cipher
[4341] statements um is is really the point of
[4345] the Nej cipher server. Uh maybe we don't
[4348] want to expose like the ability to to
[4351] run arbitrary cipher statements. Maybe
[4354] we have some uh cipher statements that
[4357] we want to expose. Maybe the like the
[4360] ability to generate personalized
[4362] recommendations
[4363] um or something like that. We want to
[4366] build an MCP server that is maybe a
[4369] little more uh custom for the data set
[4372] that we're working with uh or or
[4374] whatever it is. Um, and so what we're
[4377] going to look at here are uh kind of
[4379] some some bare bones implementations of
[4383] uh an MCP server for an e-commerce uh
[4387] store. Um both uh in Python or
[4392] TypeScript. Um and there's two tools
[4395] here. One uh to search customers. So,
[4399] search for customers um by name or
[4402] email. And then to view like their
[4406] customer purchase history, that sort of
[4408] thing. And then uh a tool to recommend
[4413] products for uh for a customer based on
[4417] co-purchase behavior.
[4420] Cool. So,
[4423] let's take a look uh at the Python
[4427] version of this. Um,
[4429] and we'll open this in
[4434] our code space. So, if I go to the
[4437] Python directory,
[4440] there should be a read me there. Cool.
[4443] And so,
[4445] there are
[4449] uh some instructions for how to get this
[4452] uh up and running.
[4456] So let's go ahead and follow those. So
[4461] we're using UV and say UV uh sync
[4471] Python.
[4475] So UV this is a package manager for
[4478] Python.
[4480] Uh, so the first thing that's going to
[4481] do is download all of the
[4487] >> Can you zoom in a little bit, Will?
[4490] >> Yes, definitely. Uh, so that's going to
[4493] download our dependencies
[4495] and then the next thing we need to do is
[4498] uh set our connection credentials for
[4502] NearJ.
[4504] Uh and so if we take a look here,
[4506] there's this uh example
[4509] env. We're going to
[4514] make a new env file
[4518] env.
[4523] Cool. And instead of
[4527] uh these credentials, we're going to
[4529] want to add in our NeoRaj aura
[4532] credentials.
[4535] Go back here
[4540] and replace the Neo Forj URI and the
[4543] password
[4545] with uh
[4548] password and connection for our Aura
[4550] instance.
[4552] And then
[4555] I'm going to just following the the
[4558] steps here. I'm going to say uv run
[4563] new forj MCP
[4566] e-commerce and that's just going to run
[4568] our
[4571] MCP server.
[4575] Cool. So you can see that's running
[4576] locally on 8000. Um, let's take a look
[4580] at code to see what this is actually
[4582] doing.
[4590] Okay. And I'll zoom in a bit. So, we're
[4595] using uh the fast MCP
[4599] package. Uh, this is I I think version
[4603] one of this became the like official
[4606] Python MCP SDK.
[4609] uh and moved to the
[4612] anthropic uh MCP repo. I saw I saw
[4615] there's a version two of fastmcp
[4619] um that someone else is maintaining.
[4621] This is not using that. This is using
[4622] the official uh fastmcp
[4626] package. Um and then we're using the
[4629] near forj
[4631] database driver.
[4635] And essentially what we're doing here is
[4636] we're loading uh our
[4640] connection credentials from environment
[4642] variables to create a nearj
[4647] uh driver instance. And then we have
[4649] kind of a helper function here to uh
[4652] just execute
[4654] cipher statement.
[4658] And then here we have a search customer
[4661] function that we've annotated with this
[4664] MCP.tool.
[4666] So
[4667] couple important things to um to
[4670] understand about the way that
[4673] MCP
[4675] um tools are exposed to models. Uh one
[4680] is that natural language is an important
[4682] piece of this. The models need to
[4684] understand as described in natural
[4687] language what the tool is doing. Uh and
[4690] so we've defined a function search
[4693] customers. Uh well it it takes a string
[4698] uh and it returns a
[4701] list of dictionary. So a list of
[4703] customer um objects here.
[4708] This piece here, this documentation
[4710] string, this is this is really important
[4712] because this is what's given to the
[4714] model so that the model can understand
[4717] like when it should call this tool. So,
[4720] uh this will search for customers by
[4722] name or email parameters um that it
[4726] needs to generate uh and what it
[4728] returns. So, all of this is passed to
[4731] the model uh so that the model can
[4733] understand okay cool I have access to
[4735] this tool. uh it's a function search
[4739] customer uh and this is what it does.
[4743] That's really important um I guess thing
[4746] to understand about how natural language
[4748] how important natural language is for
[4750] for these models. Now we we've defined
[4753] um a cipher statement here. We're just
[4755] searching for a customer and then
[4756] returning um customer information. Then
[4759] we have another uh function here
[4761] recommend product.
[4763] We have a doc string again that explains
[4766] this will recommend products uh based on
[4770] purchase behavior. Look this up by
[4772] customer ID and so on. And that's it.
[4776] Right? So two two functions essentially
[4779] we annotate those with this mcpto tool.
[4783] And what that means is we're now um
[4788] exposing these two tools recommend
[4790] product and search customer which are
[4794] essentially uh functions that we've
[4797] exposed to our AI uh application.
[4802] So you can see here that like we can use
[4805] this MCP server model is not able to
[4807] just execute arbitrary cipher
[4809] statements, right? It's only able to
[4811] search for customers and recommend
[4814] products.
[4816] Cool. So, we're running this um locally
[4820] on port 8000 which is running in
[4825] this code space. Um I'm going to open a
[4831] new terminal here
[4833] and I'm going to run npx
[4838] at model
[4841] context
[4845] protocol slashinspector.
[4848] See if I spelled that right. Um,
[4853] drop a link to this in the chat.
[4856] We're going to run this. Um,
[4862] talk about what this is in a minute. So,
[4865] cool. I type that right. So, I ran npx
[4870] at model context protocolinsspector. So,
[4873] MPX, this is um this is a command from
[4877] uh the JavaScript ecosystem that's going
[4881] to run uh this model context protocol
[4884] inspector package
[4888] and it's going to run this um
[4894] and then
[4898] open the MCP inspector. Cool. So um so
[4903] the MCP inspector this is a tool that
[4907] allows us to
[4910] uh essentially like inspect and and work
[4914] with
[4916] MCP servers as we are uh developing
[4919] them. Alex is making fun of me for not
[4922] closing my window here. Maybe we'll do
[4924] that. There we go. A little easier to
[4927] see.
[4930] Cool. Yeah. So MCP inspector is super
[4932] useful as we're building uh MCP servers.
[4938] The right we saw like how we can connect
[4943] our MCP server to to cloud and and sort
[4947] of go through that process. Um but it
[4950] would be nice if we could just see like
[4952] what are the tools, resources, etc. that
[4955] we're exposing. Um, and just like can we
[4958] like invoke those directly? Kind of like
[4960] a like a browser uh developer tool if
[4963] you're familiar with that. Uh, and so
[4968] this one is going to be uh over HTTP. So
[4974] the transport type this is this is
[4976] fairly important uh with MCP servers
[4979] where the transport type uh is standard
[4984] IO. This is going to be for like command
[4986] line um servers uh or they're going to
[4989] be streamable HTTP. Um we wrote uh ours
[4994] in using streamable HTTP with the fast
[4997] MCP or with the the TypeScript uh MCP
[5001] SDK. It's really easy to as you're
[5004] implementing these to to switch and
[5006] choose different transport
[5008] methods.
[5011] I
[5013] cannot localhost 8,000. Oh, you know
[5016] what? I think what this is I think I
[5017] think this is the challenge of running
[5020] this on
[5024] um
[5029] running this in um code space. Perhaps
[5035] we might just run this locally instead.
[5039] Okay. Yeah, let me run this locally so
[5040] we can see what um what this looks like.
[5044] The the issue that we run into here um
[5047] is with our ports and whatnot is that
[5053] MCP inspector is running in the browser
[5058] and is forwarding to like the MCP server
[5061] that we're running in this code space
[5064] and the port forwarding might not be set
[5066] up correctly. So, um, let me show you
[5068] what this looks like and then we'll move
[5070] on to, um, to another project that I
[5073] want to take a look at.
[5077] Say, Python,
[5083] see
[5086] the
[5089] [Music]
[5092] Python project
[5095] uh, which is here. And what did we call
[5097] this? We called this
[5104] forj ncp
[5106] e-commerce.
[5112] Then the other thing we want to do is um
[5116] px model
[5119] context protocol
[5122] inspector.
[5126] Yes.
[5130] Okay. So, I'm just going to run that
[5131] locally.
[5135] And there we go. Just to show how this
[5138] works. Cool. So, I connected to a
[5144] MCP server um over HTTP
[5150] 8000MCP.
[5153] And we can see here that uh I can do
[5156] things like list the resources
[5159] uh prompts. Our MCP server doesn't
[5161] expose any resources or prompts.
[5163] Resources are like the um static uh
[5168] either files or or things that we're
[5170] exposing um to the model. Prompts. These
[5174] are like predefined prompts that work
[5176] well in in the applications. Um but
[5179] again, most of the time we're interested
[5181] in tools. So I clicked on list tools and
[5184] I have two tools that um that we're
[5188] exposing here. One is search customers
[5192] and recommend products. And so search
[5195] customer takes a search term to match
[5198] against name or email
[5200] search for Bob. We can run the tool. We
[5204] get success because um tool ran and we
[5208] can see here here's the data that we get
[5210] back. So, we found we found a Bob
[5212] Johnson
[5215] mail.com
[5218] 1920.
[5220] Cool. Can we recommend a product for
[5223] this customer? So, this one says
[5227] customer
[5229] ID, which I don't know if we actually
[5232] saw that. Um, and part of the issue is
[5236] this when we get an error in the schema.
[5238] So part of the issue here is that we are
[5243] running
[5245] um
[5248] into a syntax error. And if we see like
[5252] this statement, this our first uh search
[5255] customer where we search for
[5259] Bob, if we get back some data, it's not
[5263] quite the right like format that we
[5266] want, right? like we could get we could
[5269] include some more information here maybe
[5270] about customers and that sort of thing.
[5272] But anyway, this is the
[5276] uh MCP inspector that shows us how to
[5279] invoke these tools and and kind of debug
[5282] them um in
[5286] the tool as we are building our MCP
[5289] servers can be um can be super useful.
[5292] The other thing I wanted uh wanted to
[5295] show here, let's do this in
[5299] VS code
[5302] uh is how we can update this code uh
[5308] using the Neo Forj MCP server. Um and so
[5311] so one example is like these cipher
[5314] statements that we have here. Well, this
[5316] one just returns
[5318] um a syntax error. Uh, and this one
[5322] isn't quite returning like all the
[5324] information that I'm interested in. Uh,
[5327] we have this like agent mode in in VS
[5330] Code. Now, is there a way that we could
[5332] sort of leverage NearJ MCP? So, is there
[5336] a way that we could have VS Code like
[5339] query the database maybe improve these
[5342] cipher queries? Um, I I like to think of
[5344] this as I don't know like database aware
[5347] or like schema coding, right? So, can I
[5353] can I use those tools to improve our uh
[5358] application that we're building? And so,
[5360] the first thing we're going to do there,
[5361] we should have this like agent mode chat
[5363] in in VS Code.
[5367] Uh the first thing we're going to do is
[5368] click on uh this settings icon and go to
[5375] MCP servers.
[5377] And we should see here that we have this
[5380] nearj database
[5382] server installed.
[5385] And if we click here, um let's look at
[5388] the show configuration.
[5393] Cool. And so so where did where did this
[5395] come from? Well, um if you've used uh
[5398] MCP
[5400] servers in VS Code before, and actually
[5403] let let us know in in the chat. I'm
[5405] curious like are are folks using VS Code
[5409] or cursor like what what are your
[5411] favorite um
[5414] sort of AI agent uh tooling uh these
[5417] days to use with MCP? I'm curious. Let
[5419] us know. Um but this is how we add an
[5423] MCP server in VS Code uh by populating
[5427] uh this MCP.json.
[5430] And so if you do like command shiftp
[5433] um you can do mcp add server uh list
[5437] servers that sort of thing. This one um
[5441] I just included kind of the skeleton in
[5443] the the repo. And so similarly we're
[5446] going to want to
[5449] add our Neoraj URI to our aura instance
[5454] which I have here. Again, you'll get
[5458] that uh file downloaded when you first
[5462] create your Aura instance
[5465] and the password
[5470] is here.
[5476] >> Cool. Um and so now
[5480] if we go back to
[5482] MCP servers. So in the agentic chat I
[5486] went to settings MCP servers.
[5492] MCP servers installed nearj database.
[5497] Click on the settings. And then this one
[5501] is important because
[5503] this server is using standard IO. VS
[5506] Code is is going to run the command to
[5508] start it and stop it.
[5511] And so
[5513] uh if this were like a hosted like
[5515] remote HTTP,
[5517] uh then
[5520] we wouldn't need to start it and stop
[5522] it.
[5525] Cool. Cool. So, it sounds like folks uh
[5527] let's see from the chat here, folks are
[5529] using uh VS Code, PyCharm, couple folks
[5532] using PyCharm with Copilot. Cool.
[5536] Good to hear.
[5541] Okay. So now um that MCP server is
[5547] available in our agent mode and so uh I
[5553] could now
[5556] come in and say
[5562] uh something
[5568] here. I could say something like um
[5572] use your
[5574] forj tools. Well, let's start out with
[5577] something simple. Uh and I say what data
[5580] is in my forj.
[5593] So,
[5594] there's a few things we could do here.
[5598] Um,
[5601] notice I highlighted this cipher
[5604] statement. Um, because what I really
[5606] wanted to do was
[5609] uh
[5613] what I really want to do is like work on
[5616] fixing this query. I want the model to
[5618] come up with a better query um
[5621] to generate personalized
[5623] recommendations. Um and so I'm going to
[5625] use
[5627] Claude Sonnet 45 that I typically have
[5631] better results um with that.
[5634] And we'll say
[5637] maybe without adding the context. Let's
[5640] try a new
[5643] chat here. Let's not add this context.
[5645] and we'll say um
[5650] use your near forj tools to
[5655] see what data is in my forj
[5662] really wants me to use GPT5. Okay,
[5665] that's fine.
[5672] Cool. And so what what we can do here um
[5686] looking at our environment variables.
[5688] That's really not what I want to happen.
[5692] And this is something to experiment with
[5694] a bit. Um
[5699] and we say
[5705] but we'll use cloud sonnet five and I
[5708] want to say
[5711] test this
[5713] cypher query uh and improve the
[5717] vision query.
[5722] I don't typically use um use VS Code. Uh
[5727] I I use Windsurf Cursor and so on. So I
[5731] seem a little rusty with vibe coding.
[5733] Maybe that's why. Okay. So now we got it
[5734] to uh to use its Neo forj tool and so
[5740] it's going to so it um inspected the
[5743] schema. Okay. Okay. Great. I can see uh
[5747] the schema. Now I want to run uh a
[5751] database query.
[5757] Cool. So now um
[5760] now by sort of tweaking the uh the model
[5764] that it was using we switched to cloud
[5766] 45 sonnet and by uh selecting this query
[5772] specifically that we want to change. Now
[5774] we're able to um to get the VS Code
[5777] agent to
[5779] iterate a bit on these. And we can see
[5781] here, let me just turn this to always
[5783] allow in this always allow the read
[5787] cipher. That's fine. Cool. So now uh
[5790] what we're seeing is we're
[5793] in this like
[5795] iterative uh process where our agent is
[5799] like tweaking this query and checking
[5802] the results. So we can see like here it
[5805] tried with a customer
[5810] to see
[5812] the results that we're getting and so
[5814] on. So we can we can work with uh
[5819] MCP servers
[5822] this way that in uh agentic coding
[5825] environments where they're actually able
[5827] to
[5829] inspect this the database schema
[5831] generate queries run them and here we
[5833] can see here's the diff uh that it's
[5835] suggesting VS code based on
[5840] however many iterations
[5842] 10 or so iterations that it took and
[5844] actually expect inspecting the results,
[5846] right? And and so it's like, hey, for
[5848] this customer, we got um these
[5851] recommendations
[5853] and so on.
[5855] Cool. And so, uh that allows us to
[5859] essentially use the Nej MCP to help us
[5862] tune uh anj MCP application.
[5867] Okay, cool. So, we've got like 20
[5868] minutes left. Um there's one more kind
[5871] of section I wanted to go through, but
[5874] let's um let's maybe take another pause
[5878] here and answer any uh questions that
[5880] we've missed so far.
[5882] Yeah, there is one uh from Roger
[5888] uh and uh Roger asks if you have used
[5891] any of the uh tuned text to cipher LLMs
[5895] or do you stay with the more you know
[5898] vanilla uh ones like like set here in
[5901] this case?
[5903] >> Yeah, that that's a good question. Um I
[5905] I would love for other folks in in the
[5908] audience um to kind of chime in and and
[5910] say what their experience has been like
[5912] if if folks are up for that. Um in my
[5915] experience, I have
[5918] not used the text to cipher models um
[5922] too much because I've found that I I
[5924] haven't really needed them. I found that
[5927] the
[5928] foundational models are are like pretty
[5931] good. um Claude Sonnet uh 45 is kind of
[5936] my default um model that I use for these
[5939] sort of like coding projects. I think
[5941] it's it's pretty good at trying to
[5943] figure out when to use tools like code
[5946] and database generation. Is this
[5948] something you kind of play around with?
[5950] I mean we saw earlier like
[5953] claude uh or um GBT5 like not so great
[5957] at figuring out when to invoke the tools
[5959] or maybe that's the way we've described
[5961] the tools. So, so it kind of depends. I
[5963] I think um especially when you're
[5965] looking at being able to work with
[5968] multiple MCP servers is you really want
[5971] that can a model that can understand and
[5973] work with tool calling. Um but yeah,
[5976] specifically for like database query
[5978] generation, I found that yeah, Cloud
[5980] Sonnet 45 is kind of the the default
[5981] that I use, but curious if if other
[5984] folks are using the um the text to
[5986] cipher models and and having success
[5988] with that. Perhaps it's for more complex
[5991] cases. Um that sort of thing that maybe
[5994] the the foundational models don't have
[5996] some of that understanding built in.
[6000] >> Yeah. Yeah. Could be. Um but yeah, I
[6003] think that's um that's what we have at
[6006] the moment in terms of questions.
[6009] >> Okay, cool. Well, let's um hop back to
[6013] the slides here. And there's kind of one
[6015] uh final section I want to talk through
[6018] and that's this idea of AI agent memory.
[6021] Um and then we'll take a look at how we
[6024] can uh use MCP and Neoraj to kind of
[6028] start to address this idea of um an AI
[6032] agent memory layer. So
[6035] taking a like like a step back here uh
[6039] and thinking of when we're talking about
[6042] an AI agent like what what actually are
[6044] we talking about here? Fundamentally
[6047] uh this idea of the augmented LLM,
[6049] right? Where we're adding the ability to
[6054] uh understand and and interact with the
[6058] agents environment through tool calling.
[6061] And this can be tool calling that
[6063] enables uh retrieval. So fetching
[6066] additional data that is then used in the
[6069] context of the LLM invocation or uh
[6073] memory, right? Where we're maybe
[6075] managing the context uh of our
[6078] avocation.
[6080] Um this is a like a fairly simplistic
[6082] example I think of why we need agent
[6085] memory. Um I think you know if you've
[6087] used a applications then uh you know
[6090] maybe you've you've experienced
[6092] something like this before where you
[6094] know in a session you're like hey I'm
[6096] I'm working on Python project for data
[6098] analysis I prefer pandas over numpy and
[6101] the agent um it's like okay great here's
[6104] some some python examples we're going to
[6107] use pandas but then in another session
[6110] you say okay like help me you know
[6114] generate some code and the agent says,
[6115] "Sure, happy to help." Like, "What
[6117] language are you using? Do you have
[6118] library preferences?" And like all these
[6121] uh these sort of like preferences that
[6123] I've expressed go away. That that's
[6125] really frustrating, right? But if we
[6126] have memory um where the agent can
[6130] understand, in this case, it's going to
[6131] be like user preferences that have been
[6134] um expressed that helps us have a lot
[6136] more trust uh in uh in the A
[6140] application. So some of the challenges
[6142] if we don't have agent memory uh is you
[6145] know this lost context problem right
[6147] where it seems like the agent is
[6149] forgetting like essential information
[6151] based on on things that I've told it uh
[6154] preferences that I that it should have
[6156] learned um or are you know responses
[6159] from the model are like super generic
[6161] inaccurate we've all seen like these
[6164] hallucinations
[6166] sorts of things as people are talking
[6168] about AI agent memory
[6170] Um I see people talking about like
[6173] short-term and long-term memory. Um that
[6176] is one way to to think of this
[6178] distinction where for the like shortterm
[6182] memory that is typically one session one
[6187] interaction like one chat that I'm
[6188] having uh with an AI agent and I want to
[6191] be able to look up maybe like all the
[6193] session information for that user's
[6195] interaction and inject all of that into
[6197] context because that's that's our
[6199] short-term working memory. longer term
[6201] memory. Uh that's typically going to be
[6205] well maybe I want to uh load into a
[6208] vector index like the unstructured right
[6211] like um transcript of of my discussion
[6214] with an agent and I'm going to use like
[6216] vector search to make sure that I'm
[6218] always injecting the most relevant
[6220] context like that. That's one um axis to
[6223] think about that like short-term versus
[6225] long-term memory. Um, another way to
[6227] think about that is
[6229] episodic, procedural, personal or
[6232] working memory as well. Um, where
[6234] episodic memory I'm thinking about like
[6238] uh storing experiences and events from
[6240] past interactions. Procedural where I've
[6242] learned or the model the agent has
[6244] learned to perform tasks and workflows.
[6248] Um, so lots of different types of of
[6250] memory when we're we're talking about
[6252] memory, but fundamentally,
[6254] uh, when we're thinking about memory, it
[6256] all comes down to managing the context.
[6259] Uh, there's a lot of discussion out
[6261] there about, uh, context engineering.
[6265] Um, and we can see why this is becoming
[6269] more and more important. Um, so on the
[6271] left, this is you maybe like early days
[6274] of uh of working with some of these AI
[6277] tools where the context window, it's
[6280] really just system prompt and the user
[6282] message and that's what you're you're
[6284] sending to uh to invoke to the LLM. uh
[6287] but now as as the AI ecosystem has
[6290] evolved and become a bit more complex
[6292] you know we're including documents uh
[6296] and memory in the context where uh we're
[6300] now including tool calls um and this is
[6304] really interesting because those tools
[6307] even if we're not invoking them uh
[6310] they're included in the context as like
[6313] a possible option for uh for the model
[6316] right like the model could chose could
[6318] choose to invoke those tools. We still
[6320] need to include the natural language
[6322] description of all of those tools. Um we
[6325] saw this in the the doc string and the
[6327] the Python example that we created
[6329] earlier where we need to leverage all of
[6331] those um or include all those tools in
[6333] the context if the model is going to be
[6334] able to choose to invoke them, right?
[6336] And so anyway, memory and and memory
[6340] management is a piece of this because we
[6341] we don't want to just throw every single
[6344] like bit of unstructured data that we
[6346] have into the context. We need to uh we
[6349] need to be able to make sure that we
[6351] have the
[6353] most I don't know the most uh like up
[6356] toate there's some time decay element to
[6358] this but the most relevant context uh
[6361] available um any given time.
[6364] So uh I've been doing some some research
[6366] into um into agent memory over the last
[6369] few months is a really interesting area.
[6371] Um there's a few papers especially I
[6373] think that especially in the context of
[6376] working with graphs um that I think are
[6378] really important. um MIMGPT this paper
[6381] uh I think did a good job of just kind
[6383] of
[6385] laying out this framework where the
[6388] models are responsible for uh sort of
[6392] managing
[6394] their memory similar to how uh they
[6396] would manage resources in an operating
[6399] system. Um and and so the model uh has
[6402] tools for sort of choosing what to pull
[6404] into uh into that context and and sort
[6407] of extending from that basic idea uh we
[6410] have the Zep and Mimzero papers. Um Zep
[6414] and Mimzero
[6416] uh both use Neoraj for agent memory. So
[6420] the Mimzero paper talks about um Mimzero
[6423] graph functionality with Neo forj. Zep
[6426] talks about an open-source
[6428] uh AI a uh memory framework called
[6431] graffiti. Um and based on you know some
[6435] of the ideas from these papers uh I
[6438] built a little demo project which we'll
[6440] we'll take a look at um in a minute. Um,
[6442] but this this should give you an idea
[6444] of, you know, a use case where we want
[6449] to through MCP, we'll see how MCP fits
[6452] into this in a minute, but through MCP,
[6454] we want to expose knowledge graph memory
[6457] tools to an AI agent. And there's really
[6459] like two or three pieces to this. One is
[6462] graph construction. Um, so when we're
[6466] talking about agent memory, this is
[6468] being able to uh construct a graph from
[6474] the chat uh with an agent. Um, or also
[6478] we'll see in in uh the example we're
[6481] going to look at in a minute, also take
[6482] unstructured data or JSON and sort of
[6485] build that knowledge graph as well. So
[6487] then the other piece is okay, how do I
[6489] expose graph search to my AI application
[6492] for memory retrieval and and that
[6494] context engineering piece of of how do I
[6496] make sure that I have the most relevant
[6498] uh memories and then how do I expose
[6500] these as as cool? Well, MCP is the the
[6503] answer to that. Um so let's look at this
[6505] this first piece the the graph
[6507] construction um from unstructured data.
[6510] So entity extraction is um is an
[6514] important piece of this. That's kind of
[6515] the the first step. Um, this is a prompt
[6518] that is adapted from the ZEP paper. Um,
[6522] where essentially we're taking the
[6524] message and the previous like in
[6527] messages as well, passing that to an LLM
[6530] to identify uh the entities.
[6534] So, the example we're going to show is
[6536] is um this string. So, William Lion
[6540] works for Hyperode as director of
[6541] developer experience. He's currently in
[6543] Yellowstone National Park and traveling
[6544] to Todd Springs for the DevText
[6546] conference next week where he will be
[6548] speaking about AI native app
[6549] architecture on October 1st. This one's
[6551] a little bold. I use this for an example
[6554] from a few weeks ago at Dev to Next, but
[6558] this is essentially what the
[6561] uh model comes back with like hey
[6563] there's some entities like people uh
[6566] concepts can also be entities. So AI
[6568] native app architecture that's um that
[6572] is a entity a concept then we go through
[6574] this resolution phase um I'm going to
[6577] skip over that entity resolution is is
[6579] super important there there's lots can
[6580] be said about that um but essentially
[6583] this step is about identifying the
[6586] canonical entities like are are there
[6589] duplicates um essentially and then
[6592] similar idea for the uh relationship
[6595] extraction these are like the facts Um
[6598] and again we send this to the model. So
[6601] we send the entities that we've
[6602] extracted uh and the text of the memory
[6606] um to the model. And again this is this
[6608] is the prompt adapted from the ZEP paper
[6611] uh to do that. And in the graph we can
[6614] store sort of the well I guess we have a
[6617] couple of options. One is we could we
[6619] could impose some more uh some more
[6622] structured data model on our graph where
[6625] maybe we're saying these entities are
[6628] related and we're storing as a property
[6630] on the relationship how they're
[6632] connected or we can just let the model
[6634] sort of come up with uh the relationship
[6638] types to describe how they're connected.
[6640] Kind of depends on how we want to be
[6642] able to traverse and work with the graph
[6644] there.
[6646] Cool. uh Zep places a lot of importance
[6649] on temporal relationships and and points
[6653] out that like hey your preferences are
[6654] going to be invalidated uh you're going
[6657] to have new preferences that take over.
[6660] Um, so that's an important uh feature in
[6663] Zap uh where we're adding essentially
[6666] metadata um at uh to the relationships
[6671] and uh the relationships especially of
[6674] of when like what date range or when did
[6677] this become invalid, when did it become
[6679] valid? This is um this is I think a
[6683] really key observation. This is
[6685] something that a graph can express very
[6688] very well. the temporal nature of these
[6690] relationships that are really difficult
[6693] to express uh say in like vector
[6697] database or just a bunch of unstructured
[6700] uh text be very difficult to understand
[6703] um
[6705] uh be able to express that and and
[6708] encode that um in our agent memory. We
[6712] also uh geocode the locations to get a
[6714] spatial index here. Um one thing that I
[6716] was surprised to see that models are
[6719] actually quite good at geocoding which
[6721] is taking um a description like an
[6723] address or name of a place and
[6724] converting that to a latitude and
[6726] longitude. And then the other piece um
[6729] of graph construction is to generate
[6731] embeddings. So for the like description
[6734] of these things we generate embeddings
[6736] um to help us in the search phase of
[6738] these. Then the next step is uh using
[6741] graph algorithms um in GDS. uh
[6744] specifically we're looking at uh
[6745] community detection and so let let me
[6748] skip ahead to the data model. So the
[6750] community detection uh identifies
[6753] entities that uh are frequently like
[6757] co-mentioned and across memories. Um and
[6760] that's going to help us at the retrieval
[6762] step to be sure to uh return entities
[6765] from similar names.
[6768] Um and then the graph search piece for
[6771] this well essentially we're doing a
[6773] combined vector plus graph traversal the
[6776] uh vector search that becomes the entry
[6778] point and then we traverse the graph uh
[6782] looking at um entities that are
[6784] mentioned together across memories using
[6786] community- based traversals. Right? So
[6788] leveraging the uh the data model here.
[6792] Cool. So really quick we have like five
[6794] minutes left. Let's see if we can um get
[6796] this running. Um, and I'll I'll point
[6798] you to the code for this just to kind of
[6800] show how this works. So, we said there's
[6803] two tools. There's um our save message
[6807] tool which goes through this pipeline
[6808] like extracting entities in resolution
[6812] building uh the relationships building
[6814] that in the graph and then the memory
[6815] search tool allows us to do this
[6818] combined vector plus graph retrieval uh
[6821] to load this data. So, um,
[6826] yeah, synced here.
[6828] I called this, uh, project go fetch. Um,
[6832] if you're familiar with some of like the
[6834] the rag, um, benchmarks, they have this
[6839] concept of the golden retriever, uh,
[6841] that there's like a retrieval that
[6843] retrieves the the correct document.
[6845] That's the golden retriever. So, I was
[6847] reading through this and thinking of
[6848] golden retrievers when I when I created
[6850] this project. So anyway, that's why it's
[6852] called go fetch.
[6856] Find it somewhere in the window here.
[6867] Go to the fetch. Cool. Yeah. So I'll
[6869] drop a link to this in
[6872] the chat.
[6874] Cool. So the code's here. Um you can
[6877] play around with this. Uh
[6880] this is written in um Typescript
[6885] and it's using uh the Enthropics
[6889] TypeScript SDK. Uh it works with both
[6892] NearJ or Dgraph. Um but let's go ahead
[6896] and
[6898] fire this up. So
[6902] fetch
[6908] Okay, cool. So, that started and let's
[6912] run our MCP inspector
[6915] uh which we learned is
[6918] developer tool for building
[6922] spect MCP tools
[6926] port is in use. Oh, we're running it
[6928] somewhere else. Okay, hold on.
[6932] running NCP inspector here. Let's close
[6935] that.
[6939] We'll run it over here.
[6947] Cool. So,
[6950] let's list our tools
[6952] connected to our other MCP server. Where
[6955] is this one running? This one is running
[6959] on 3003. Okay.
[6964] So, let's disconnect and we'll switch to
[6968] port 3003
[6970] slash
[6972] MCP. Okay,
[6975] tools.
[6978] Cool. So, we have save user message and
[6982] graph memory search. So, let's do uh
[6986] save user message. And
[6990] just to save time here, let's see if I
[6992] can copy that sample
[6996] that I was using before.
[7000] Uh yeah, so William Lion blah blah blah
[7003] speaking at a conference. Oh, come on.
[7007] and get the text for that.
[7012] And let's say this is the message we
[7014] want to save. And if we look here, if we
[7017] look
[7019] uh down here, we can see
[7022] here's the steps uh that we're going
[7026] through. And so
[7028] we called the LLM for entity extraction.
[7031] Uh we found five entities.
[7035] We checked the database to see if
[7037] they're existing. Uh they're not. Uh we
[7040] generated embeddings for all of those
[7042] things. Uh we found
[7046] a location for Colorado Springs,
[7049] latitude and longitude, and then we did
[7051] uh for relationships,
[7054] created those um in the graph.
[7061] And if we now search do graph memory
[7066] search
[7068] and
[7070] I don't know maybe our query is related
[7073] to
[7075] William Lion.
[7078] Now we can see we're going to we can
[7080] take a look in our output MCP server.
[7083] It's going to do a vector search for
[7087] William Lion. Yep. There we go. And then
[7089] traverse the
[7091] similar entities. Oops, clicked off
[7094] that. Here,
[7097] here we go. This guy. Cool. So, we have
[7101] kind of like a summary and then the top
[7104] matching entities. You can see William
[7106] Lion, the person matches 100% because
[7109] that is massive vector search. But that
[7111] like that's not enough. We need to
[7112] traverse the graph to find all of the
[7114] entities and memories related to William
[7116] Lion and and we can summarize them. And
[7119] then this would then be injected into
[7121] context for our uh for our AI app.
[7127] Cool. So that was um a quick look at you
[7130] know how can we use some of the the
[7132] concepts that we talked about to build
[7135] um this sort of data layer for AI
[7138] applications um
[7141] powered through uh through MCP. So we're
[7145] about out of time here. Um here are the
[7148] some of the papers that that I've been
[7150] looking at. Um
[7153] talk a bit about like how to expose
[7155] memory. I think that that's an
[7156] interesting one to think about. But
[7158] thinking about how do we bridge like the
[7163] knowledge graph we've created this like
[7165] unstructured data with our uh connect
[7168] that to our business domain. I think
[7170] that is something we're going to see in
[7171] these memory frameworks going forward.
[7174] On the right here you can see um some
[7176] examples from uh how zap and graffiti is
[7180] approaching this with uh p by defining
[7184] uh pideantic models um and so being able
[7187] to essentially have like structured
[7188] outputs in that sort of um entity
[7191] extraction phase where what you're
[7194] extracting entities are lining up with
[7196] your application data. um this site uh
[7201] this page here the developer guides this
[7203] is going to be um your next resource to
[7205] learn more about NearJ and uh NearJ MCP
[7209] and and dig in there. So definitely
[7211] encourage you to check out this site um
[7214] as well as some of the graph academy um
[7217] content on MCP um and certainly any of
[7221] the other road to node sessions and um I
[7224] should have gone through and took a look
[7225] at some of the interesting uh nodes
[7227] talks related to MCP because I know
[7229] there are several of those um but
[7232] definitely that's another good resource
[7234] to um to check out as well.
[7237] >> Cool. Thank you very much uh Will. That
[7240] was that was amazing. Uh lots of demos,
[7243] lots of hands-on. I think there's lots
[7245] of uh lots of good good content there.
[7248] I'm I'm I'm sure a couple people asked
[7249] this and I want to repeat this again.
[7251] Yes, we have recorded this session. Yes,
[7253] we will send you an email with the link
[7255] to the recording later this week. So,
[7257] you can uh jump back in um and watch
[7260] what maybe was a bit quick at times uh
[7262] if you want to re repeat what will uh
[7266] showed you today. And again, the slides.
[7268] Yeah, again in this in the in the in the
[7270] chat, thank you will. So, um yeah, I
[7273] think that's um that's uh what's uh
[7277] happening. Um I just um quickly wanted
[7280] to say that we have a road to nodes
[7284] workshop tomorrow. I think I said this
[7285] again in the beginning, but you know,
[7287] Aura agents will tease it a little bit.
[7290] So, we we do this tomorrow, same time as
[7292] this one. If you haven't registered for
[7294] it, you can check it out on the um road
[7296] to notes website.
[7298] If you are interested in more uh events
[7301] leading up towards nodes which already
[7303] is in in two weeks time we have a
[7306] speakers round table on the 28th of
[7308] October. Uh so that's also next week um
[7311] where we have a couple of speakers four
[7313] in total invited to thank you will
[7316] exactly that's the page uh for for the
[7318] road to notes workshop and then we have
[7320] this speakers round table with four
[7322] sessions uh where I have invited a
[7324] couple of um you know sort of all stars
[7329] um of the um of the roads uh sorry of
[7332] the nodes um event with Katarina Nesvit,
[7334] Christian Frank, Shupam Bakshi and Luan
[7337] Mskita.
[7338] um and they will talk about their
[7340] sessions at nodes. And then obviously
[7341] nodes is happening on the 6th of
[7343] November. So if that is um something you
[7346] haven't registered for, what are you
[7348] waiting for? Um it's now or never
[7351] really. That's what it is. So I'm um I'm
[7354] hoping to see you all in two weeks time
[7356] and notes. And um yeah uh next next
[7359] steps I think this um great what will
[7362] already showed is the um the graph
[7366] academy is a great place for you to
[7369] learn the community. If you have any
[7370] question, anything is unclear, check out
[7372] the community either on Discord or on
[7374] the forums, uh interact with our
[7376] friendly developer community there and
[7378] let us know how it goes on, how build
[7380] your own applications, build your own um
[7384] graph app with Neo forj MCP and uh and
[7387] let us know what you built and uh and
[7389] share it with the community. And yeah, I
[7391] think sorry for overrunning a little
[7392] bit, but um yeah, um thank you all for
[7395] watching. Thank you for participating
[7396] again. Will, thank you for for doing the
[7398] workshop today. And um yeah, see you
[7401] tomorrow. See you next week or at Nodes.
[7404] I'm counting on you.
[7406] >> Cool. Thanks everyone for joining.
[7408] Thanks uh thanks Alex for organizing and
[7410] hosting and yeah, this was a fun one. Um
[7413] hopefully yeah, hope hopefully uh
[7416] something some useful insights there.
[7418] Kind of a bit of a a whirlwind just kind
[7420] of look at different ways to use um MCP
[7423] with NearJ. I I think that there's a lot
[7425] of like super interesting I don't know
[7428] evolution in a lot of these like AI
[7431] application tooling right now. So it's a
[7433] super fun time to be working with uh
[7435] working with these tools for sure.
[7437] >> Yeah. And then because I just see this
[7439] in the questions um maybe will before um
[7442] we go uh away can you make sure that you
[7445] add the memory part to the deck you
[7447] we've shared in the initial um link. I
[7450] think somebody said that this is not
[7452] part of this deck isn't it? Oh, it is.
[7455] Oh, it is. Okay. Just scroll to the very
[7457] end. I see it here. It's there. So, um,
[7460] sorry, maybe you missed it. So, Abishek,
[7462] I think you posted this question.
[7463] Somebody voted for it. It's at the very
[7465] end of the deck. So, you just go all the
[7468] way to the end of it. It's there. All
[7471] right. Um, cool. With that, uh, I wish
[7474] you all a great rest of your day. Uh,
[7475] rest of the, uh, uh, yeah, evening,
[7478] afternoon, uh, whatever it is for you.
[7480] And um yeah, see you around in the next
[7484] 4J events um happening around the globe.
[7487] Until then, goodbye.
