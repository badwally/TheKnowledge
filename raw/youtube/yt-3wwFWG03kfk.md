---
schema_version: 1
id: yt-3wwFWG03kfk
type: youtube
title: 'NODES AI 2026 - Smarter MCP Servers: Using a Graph to Solve the Context Window
  Problem'
url: https://www.youtube.com/watch?v=3wwFWG03kfk
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:18Z'
content_hash: sha256:2d1c36d2aab652bbd6f14801f589ccfedf689c17473f5d32a40685ec217435c5
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 1686
  caption_track: fetched
  snippet_count: 705
filter:
  score: 0.75
---
[9] Uh thank you for that. So, for the next
[13] 30 minutes, I'm going to talk to you
[14] about
[16] considerations for making smarter MCP
[19] servers. And in particular, we're
[21] looking at contact window problems.
[25] And
[26] you might ask yourself, well, what is
[28] that? So,
[30] this is where an AI agent's token limit
[34] is exceeded. And that can cause a number
[37] of symptoms.
[39] It's often referred to as context rot.
[44] And a contributor to this,
[47] and I'll come on to
[48] a bit more detail about context windows,
[51] is how we build MCP servers, and in
[55] particularly around tool definitions.
[60] So,
[61] this isn't something which is merely
[64] theoretical.
[66] If we look at a real-world example here,
[69] here's something which somebody posted
[71] on Reddit.
[73] And they posed this question about
[77] they'd looked at Claude code,
[79] used the doctor utility which can show
[81] you tokens consumption,
[84] and discovered they'd consumed 27,000
[87] tokens
[88] before they'd even done anything.
[92] And that all contributes towards the
[94] context window filling up.
[97] And that context window is essentially
[100] a term for describing
[103] all the things which your large language
[105] model has to deal with.
[108] And it also,
[110] if we look beyond the context window,
[113] all those tokens are burning money.
[117] And that's before
[119] you've actually done anything with your
[120] MCP server and your large language
[123] model.
[125] And if we dig a bit more into what's
[128] going on,
[130] you can look at this particular picture.
[133] And if we look at the top,
[136] we can see what's going on here
[138] when we look at the interaction between
[140] the model,
[141] the MCP client and server.
[144] And one of the first thing that happens
[148] is your MCP client will ask
[151] for the list of tools which the MCP
[154] server has available.
[156] That tool list,
[158] so the name of the tool, its definition,
[161] description,
[163] is processed by the model. And that
[165] consumes total tokens
[168] and it takes up space in your context
[170] window.
[171] And like I've just mentioned,
[174] you haven't actually done anything yet.
[176] So,
[178] when we think about context and the
[181] context window and how tokens are being
[183] used here,
[186] we need to take this into account when
[188] we think about how we're designing our
[190] MCP servers
[192] and how we structure
[194] the tools an MCP server has
[198] and how that server delivers them.
[202] We now need to take that into
[203] consideration along with everything else
[206] you do when you're building an MCP
[208] server like
[210] what communication protocol you're going
[212] to use. Are you going to use you're
[213] going to use standard IO? You're going
[215] to use HTTPT?
[217] Are you going to use off? You're going
[219] to What are you going to do about
[220] logging?
[222] Now I have to think about how can I
[224] optimize the presentation of tools to
[226] the model
[227] so I can optimize the token burn and I
[230] can optimize the context itself.
[233] And when you're thinking about this,
[235] you can roughly say
[238] for every single tool definition you
[240] have,
[241] it consumes 200 tokens.
[244] And if you were
[247] considering building an MCP server,
[249] which was going to surface
[252] a bunch of traditional REST APIs,
[255] that could be multiple endpoints you
[258] were presenting as tools. So, maybe it
[261] could be like 60 plus tools.
[263] So, if you do the math, that gives you
[265] around 12,000 tokens
[269] right at the start of the conversation
[271] between your MCP server and your model.
[277] And that And that tool count
[279] matters, right? Because we've seen it
[282] burns tokens.
[283] It
[284] impacts our context window.
[287] And when MCP servers first appeared, we
[291] all
[292] kind of ran to get on board that
[294] bandwagon.
[295] And we just jumped straight in, right?
[296] So, we simply said,
[298] "Let's give out all of our tools."
[302] Because then,
[304] the model's aware of them, right?
[306] So,
[309] by doing that in our haste, we kind of
[312] looked before we
[314] Well, we did we forgot to look before we
[316] leapt, right? So,
[318] if we take a moment and pause, and take
[320] a deep breath,
[322] and take a step back,
[324] we need to consider what tools the model
[327] needs to get a thing done.
[331] And we need to try to avoid
[333] the model drinking from a fire hose.
[337] So, we need to think about how can we
[339] give the model what it needs
[342] whilst avoiding
[344] cluttering up with stuff it doesn't
[346] need.
[348] And
[349] here's where I'm going to talk about
[351] three potential patterns you can
[353] consider when you're looking at MCP
[355] servers.
[357] And they have trade-offs, right?
[359] Nothing's for free.
[362] So, if we talk about the full list of
[364] approach, which is what I just
[366] mentioned,
[367] where we give the model
[370] everything on startup.
[373] And that's what the MCP specification
[376] says happens.
[378] So, the client says, "Give me Give me
[380] the tools." The server responds with the
[382] tool list. So, we know it'll always
[384] happen. It's a reliable way of doing
[387] this.
[388] But, it burns tokens.
[390] If we look to the far right,
[393] then we can see what you could describe
[395] as lazy loading.
[398] So, here we're giving the model the
[400] ability to discover tools.
[404] So, the idea being
[405] that it finds the tools
[408] that it needs, can ask more questions
[410] about the tool, and then runs it.
[414] And then, in the middle,
[417] we're kind of trying to strike a middle
[419] ground where
[421] we want to give
[423] the model the tools that it's most
[425] likely to need first.
[428] And then, we'll also give it the ability
[431] to find out more.
[435] And one of the things we have to bear in
[437] mind across all of these is
[440] a model
[442] doesn't always do what you expect.
[445] So, it turns out it may not always ask.
[448] So, that's one things which you need to
[450] bear in mind.
[452] So, let's jump into looking at each of
[454] these approaches in turn.
[457] Let's start with the full list.
[463] So, this is guaranteed almost by the MCP
[465] specification itself.
[468] According to specification, when an MCP
[470] client starts up, it always will ask an
[473] MCP server for the tool list.
[477] So, you know that the model will be
[480] aware of all of the tools.
[483] But,
[484] token usage, right? And the context
[486] window.
[488] If we scale this up to incorporate lots
[491] and lots of tools,
[493] then we start to run into some of those
[495] challenges.
[496] But, there are some things we can do
[499] in terms of mitigation.
[502] And one of those is
[504] to implement some kind of capability
[507] capability filtering.
[510] So, we try and change
[513] the way we look at the design of MCP
[515] server from how is the model discovering
[518] tools
[519] to how can we give the tools which are
[523] relevant.
[525] And
[527] one of the ways we can look at this is
[529] to kind of look at filtering tool sets
[532] as a product decision, not just an
[534] engineering one.
[536] So, we can look at this in terms of
[541] at what point should we give the tools
[543] out?
[544] And how
[546] do we go about doing that?
[548] So, we can look at it in terms of
[551] if I'm in
[553] a development type environment, then
[557] my MCP server could expose tools for
[559] debugging and to help me with
[561] development. But, those tools would not
[564] appear in a production environment
[566] because they're not relevant.
[568] We can also look at the role.
[571] So,
[572] the end user, if you like, who's
[574] connecting
[576] by our agent
[578] to this MCP server to get a thing done.
[580] We can look at who they are
[583] and see what they need
[585] and then give them a subset of the
[588] overall tool list.
[590] Um for example, you could look at scopes
[593] in a JWT
[595] and based on that, you could assign a
[597] bunch of tools.
[599] We could also look at the context. So,
[601] for example, we could decide that some
[604] tools you can always use
[607] but other tools are locked away behind
[609] some form of authentication.
[612] And there's a great example of this when
[614] you go look at how GitHub has done it.
[617] And they allow for selecting of groups
[620] of tools or individual one.
[623] So, in that particular example there,
[626] you can see that I'm asking for a subset
[630] of the overall list of tools which
[632] GitHub can give me.
[634] So, I'm calling out specific ones.
[636] But it also allows you to to get hold of
[639] tools based on a category as well.
[642] So, that's an example of using the full
[644] list but then filtering what tools you
[647] get.
[649] So, the approach on the right-hand side
[652] from that diagram I showed you just a
[654] few moments ago
[656] is to do what I would describe as lazy
[658] loading.
[660] So, this is where you literally have
[662] three tools.
[664] And the first tool
[665] allows the model to discover what
[668] capabilities exist.
[670] So, it's literally asking the question
[673] what can the MCP server do?
[676] And it will get
[678] a list of the tools by name and you
[680] might give each tool a brief
[681] description.
[683] The model can then go for a particular
[685] tool, ask the question, well, how does
[687] this tool work?
[689] And then based on that, it can then go
[692] ahead and execute that tool.
[695] And this, as you can see, there's only
[697] three tools. So, it dramatically reduces
[700] the context
[701] and dramatically reduces the number of
[703] tokens.
[706] But,
[707] and there's always a button, right? With
[709] lazy loading, you are heavily relying on
[713] a model
[715] to follow what you to follow this
[718] pattern of
[719] listing capabilities, choosing the right
[722] tool, and then using it.
[724] You're really at the whim of that model.
[727] And I say in those terms
[729] because models can't be compelled.
[734] So, um
[735] if you haven't come across that yet,
[738] um you will. And
[740] you need to coach and encourage.
[743] And if you've ever dealt with teenagers,
[746] it's a
[746] very similar kind of thing.
[749] Now, there are some things you can do
[750] around that in terms of you can look
[753] into uh skills,
[755] which can help describe how a tool can
[757] be used and what it can be used for.
[760] But, you're still relying on that model
[763] to take that advice.
[765] And we can see that where
[768] there are some
[770] um
[771] occasions where we've actually seen that
[773] with our MCP server, which we have for
[776] Neo4j.
[778] And that has the capability for a model
[781] to discover
[783] what graph data science tools algorithms
[786] are available for it to use.
[788] And what we've noticed is
[791] if you phrase the question
[794] very carefully,
[796] then
[797] it will go ahead and use
[800] that particular route, where it
[801] discovers the tool,
[803] and then goes ahead and calls the
[805] correct GDS algorithm.
[808] But, we've also frequently seen if you
[810] don't phrase your question in that way,
[813] then the model will take the shortest
[816] path available to it.
[818] And I apologize for that. There is no
[820] pun intended there.
[822] And it will take that path and would
[825] write cipher.
[827] And that gives you a result, but it's
[829] not necessarily the best result.
[832] It's not necessarily the best path for
[834] the model to have taken,
[836] but it will do it.
[838] And so you can see there
[840] where
[841] you phrase the question,
[843] so the model
[845] gets a clear specific task.
[850] You can see there where it will just try
[852] and do it straight away. Or it will take
[854] the easy path, or it will infer the
[856] wrong parameters to use.
[859] And one thing just to be be aware of is
[862] if you're going to go down this lazy
[863] loading approach, is it really depends
[866] on
[867] how you're structured. So if you're
[869] writing an agent
[871] working with the model,
[872] you have more control over what's going
[874] on.
[876] And that allows you to take advantage of
[879] this type of approach.
[881] But if you've got a public MCP server,
[885] then
[885] this doesn't work spectacularly well.
[889] So the middle approach, the balanced
[892] approach if you like, when we looked at
[894] that initial slide,
[896] this is where we've got a graph
[899] sitting behind our MCP server.
[903] And here what we're doing
[905] is we're using our knowledge we've
[907] encoded in our graph
[910] to help with our registry of tools.
[914] And one of the things we're we're doing
[916] is
[917] taking advantage of the fact that graphs
[920] are really good at answering questions,
[923] which a flat list cannot.
[926] So, here we can model
[929] the tools. We can model them into
[931] categories.
[933] We can record how often they're used. We
[936] can look at how well they're used, etc.
[939] So, kind of like usage data as well.
[943] And the reason this is important is it
[947] allows us to on that initial
[951] tool call, that tool list command, which
[953] the MCP client gives at startup,
[957] is we can give the model the common
[960] tools first.
[963] So, for example, we could give it eight
[965] commonly used tools, and we know they're
[968] commonly used because we've described
[970] that in the graph, which is supplying
[973] that list of tools.
[975] And then we give
[977] the discoverable
[978] tooling as well. So, we allow the model
[983] to find out more tools, and we allow it
[985] to do it by categories.
[988] So, if you've got tools which allow you
[990] to interact with a database,
[992] you've probably grouped them
[994] into things which may query your
[996] database, like read-only tooling,
[999] tooling that allows you to do imports,
[1001] tooling that allows you to do mutations,
[1003] change of data. So, you can use that
[1006] information, those categories,
[1008] to group that tooling together.
[1011] So, here
[1015] we're ensuring that the model can't miss
[1018] what tools to start with,
[1019] but also because we're baking that
[1021] discovery into that initial tool list,
[1023] the model is aware of it.
[1026] And the other thing we want to do as
[1027] part of our MCP server functionality is
[1030] every time a model uses a tool, we're
[1033] going to record that usage.
[1036] And so, that allows us to when we front
[1039] up that initial common list,
[1042] that list is built off real-world usage.
[1046] So we can ensure those commonly used
[1050] tools appear first.
[1052] And then all the other stuff, we make it
[1055] findable.
[1058] So if you look into me a bit more detail
[1060] about how this could look at the back
[1062] end,
[1063] we've got
[1065] a graph there and we've got
[1068] our gold nodes, they're categories.
[1071] So if I look at that database example I
[1073] just mentioned,
[1074] that could be queries, it could be
[1076] mutations, it could be importing.
[1078] That's a category.
[1080] And then we've associated
[1082] in lavender,
[1084] those are all the individual tools
[1085] associated with those categories. The
[1087] tool may belong to more than one
[1089] category, right?
[1090] And this allows us using Cypher to find
[1093] the common tools based on usage.
[1097] And that will be the initial list we
[1099] give out to the model and we could put a
[1102] limit on it. So we can say, "Give me the
[1104] top 10. Give me the top five." Whatever
[1106] it may be.
[1108] And then every time a tool has been
[1110] used,
[1111] we're updating the graph.
[1113] So that common tool list stays relevant.
[1116] It's based on what our model is being
[1118] used for.
[1120] So here's here's an example. Um so
[1123] if I was to create an MCP server for our
[1126] Aura API,
[1129] and I could roughly model in an MCP
[1132] server
[1134] the Aura API with 26 endpoints.
[1138] Well, 26 tools, if you like.
[1141] And if I gave that set of tools
[1144] to the model every time on startup, that
[1147] would consume approximately
[1150] just over 5,000 tokens.
[1153] But,
[1154] if I took the approach I've just been
[1156] talking about,
[1158] I can look at my usage data for the Aura
[1160] API,
[1162] and then I can use that data to say what
[1166] tools should I give initially, those
[1169] commonly used tools.
[1171] And I can see here that
[1174] top four,
[1176] based on actual usage of the Aura API,
[1178] are
[1179] getting information about an Aura
[1181] instance, creating a snapshot,
[1183] listing all my Aura instances,
[1186] and then listing information about the
[1188] the tenants, the projects which I have.
[1191] So, that top four, that's my initial
[1193] list.
[1195] And then the ones underneath it, they're
[1196] the ones which I'm going to start giving
[1198] out when the model asks for them.
[1202] And if if I take that approach, for
[1204] example, I
[1206] list out
[1208] eight commonly used tools, so I go for
[1210] those top eight, for example,
[1213] and then I give two more, one's
[1214] discovery, one is execution.
[1217] Then I'm now down to approximately 2,000
[1220] tokens at startup.
[1222] And that's roughly about 62%
[1225] saved.
[1227] Right. So, that's one
[1229] one approach that I could take here.
[1232] And the thing to be aware of is what I'm
[1235] doing is
[1237] the MCP server is storing its tools
[1241] in in my graph.
[1244] So, it doesn't have to necessarily be
[1246] a graph which I'm using with my MCP
[1248] server, it could be an entirely separate
[1250] one.
[1251] And the tool list is living in the graph
[1252] itself, and the tools are the graph.
[1255] And so, you could imagine
[1258] for things like restful environments
[1260] where you want to front those with an
[1262] MCP server,
[1264] this is a great way of doing it because
[1266] you've got or likely to have users
[1268] information about your rest endpoints.
[1271] So that can help you with that initial
[1273] set of common tools,
[1274] and then based on usage, you can adjust
[1277] as needed.
[1279] And it's entirely possible that you
[1281] could
[1282] bootstrap this if you've got your
[1285] endpoints in an open API spec, you could
[1287] bootstrap from there.
[1291] So,
[1292] there's three possible approaches here.
[1296] And it really depends on your situation.
[1300] So,
[1301] if we consider
[1303] what scenario
[1306] you're in.
[1307] So, we know from the MCP specification
[1310] itself
[1312] that it will always ask for the list of
[1314] tools. So, I know that the full tool
[1317] list approach will always work.
[1319] I've got fairly good confidence because
[1322] I'm giving out that common batch of
[1324] tools.
[1325] With the graph back to approach, that's
[1327] good as well.
[1329] Um lazy loading, like I've mentioned
[1331] before,
[1333] you're relying on the model.
[1335] If I also consider questions like
[1337] reducing my initial context,
[1339] is it deterministic? Will it work with
[1342] any type of client? So,
[1345] by that I'm talking about
[1347] am I using something like Claude Desktop
[1350] or open API ChatGPT, or am I writing my
[1354] own agent? That's what I kind of need to
[1357] consider.
[1358] And then I also want to think about can
[1361] this adapt over time and adjust to
[1363] what's actually going on
[1365] with the way my MCP service has been
[1367] used.
[1368] And then finally, will it scale?
[1370] So, those are some of the questions you
[1372] want to go ask yourself,
[1374] and then you can see how each of those
[1376] approaches
[1377] maps to those questions.
[1382] And in in many ways
[1385] the question you're kind of not really
[1387] asking is which pattern,
[1390] it's understanding the trade-offs.
[1392] That's the question you really need to
[1393] look at.
[1395] And I've put in that text there that
[1398] black box with that white text.
[1401] This is literally when I asked Claude
[1404] why it had taken a particular approach,
[1408] and I wanted to understand why it hadn't
[1411] used
[1412] some of the tools which it had available
[1414] to it in the MCP server I had.
[1417] And Claude told me that you essentially
[1419] you cannot tell me what to do.
[1423] So,
[1424] it cooperates and it does so
[1426] voluntarily.
[1428] Not because
[1430] in my tool description I'd used the word
[1432] mandatory
[1433] or I described it as you must do this.
[1437] And so that's one of things you you need
[1439] to be aware of. So, if you're writing
[1442] the agent,
[1444] so I'm writing some kind of chatbot for
[1445] example,
[1447] then I've got much more control over
[1449] what's going on. And again, if you ask
[1452] Claude about what's the hierarchy it
[1455] uses to determine what it will do,
[1458] the ultimate
[1460] determiner, if you like, right at the
[1461] top is Anthropic itself.
[1464] Then the agent, then the user.
[1467] And so that's how it decides it's going
[1470] to do a thing. Ultimate control is with
[1472] Anthropic. But if you're writing the
[1474] agent, you have a bit more control over
[1476] what's going on.
[1478] And so in that environment, you can use
[1480] lazy loading if you wish.
[1483] Right, cuz you have more control.
[1486] If you don't own the agent, and you've
[1489] got no real idea who the clients could
[1491] be, so I'm hosting a publicly available
[1494] MCP server,
[1496] um then I'm looking at
[1499] listing all the tools, like doing that
[1501] full list.
[1503] I could also
[1506] look at
[1508] the graph backed approach in all of
[1509] these cases as well, if I want to have
[1512] some kind of responsive MCP server that
[1515] almost gives the impression it's
[1517] learning over time.
[1519] The other thing you you need to bear in
[1520] mind is um go read what the MCP spec
[1523] says.
[1525] And lean into that. There's no point in
[1527] trying to fight that.
[1529] Leverage the fact that
[1531] information is always sent on startup.
[1534] Like the tools list call always happens.
[1538] And then, when you consider your MCP
[1540] server,
[1541] think about what the large language
[1544] model will see
[1546] and at what time it sees it, and can you
[1548] do some controls around that?
[1551] So, those are some things, some
[1553] patterns,
[1555] some thoughts,
[1557] things to consider when you're designing
[1559] your MCP server.
[1561] Um so,
[1564] I'd like to thank you for your your time
[1566] today. I've
[1569] um
[1569] >> I'm not quite sure how to help you with
[1571] that.
[1572] >> Uh that's uh Alexa dropping in and
[1574] prompting me.
[1575] Probably classic example of of models.
[1577] Um thanks for your time.
[1579] And I shall
[1582] uh let me see if I can cover off some of
[1584] these questions in the couple of minutes
[1585] we've got left. Um the graph of tools
[1588] manually.
[1589] Um so,
[1593] with the example I gave, I actually had
[1596] usage data coming from an API, which was
[1599] in use today.
[1600] So, I could use that to determine what
[1603] my common tools would be.
[1606] Um if you haven't got that kind of
[1608] information, then
[1610] you can take
[1612] an educated guess what those common
[1614] tools should be.
[1616] Start with those and then use the data
[1619] you're getting back from your NCP
[1621] server,
[1623] which is updating that graph, which is
[1624] recording that usage to start to um trim
[1628] and adjust that list.
[1630] Um
[1632] the order of calling tools, um
[1635] yep, that could vary and that's another
[1637] thing you could
[1639] start to bake into that graph.
[1642] And you could start recording in the
[1644] graph that models were using tool A and
[1649] then they're going to use tool B.
[1652] And that could help you categorize
[1654] tools, but then also in your tool
[1656] descriptions, you can tell the model
[1658] that
[1659] um
[1660] to
[1661] it's often the case that tool A is
[1663] is then called and then tool tool B
[1666] follows it. So, you can bake that into
[1669] the graph, you can also bake that into
[1671] the descriptions which you give out with
[1672] your tools
[1674] um to help educate your
[1676] uh model on what to do.
[1679] Um so, again, thanks for your time today
[1681] and um enjoy the rest of the event.
