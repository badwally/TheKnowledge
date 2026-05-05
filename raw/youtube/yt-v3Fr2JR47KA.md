---
id: yt-v3Fr2JR47KA
type: youtube
title: The Future of MCP — David Soria Parra, Anthropic
url: https://www.youtube.com/watch?v=v3Fr2JR47KA
authors:
- AI Engineer
ingested_at: '2026-04-30T17:28:32Z'
content_hash: sha256:62022abd9818bcb561f265654d5d2ad13bb03f23c39465e8faff273f1874fe56
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AI Engineer
  channel_url: https://www.youtube.com/@aiDotEngineer
  duration_seconds: 1120
  caption_track: fetched
  snippet_count: 525
---
[7] [music]
[15] >> Well,
[17] welcome.
[19] Let's get started.
[21] This
[23] is an MCP application.
[26] That's an agent shipping its own
[27] interface not through like a plugin, not
[30] through an SDK,
[31] not rendered on the fly by the model on
[34] the client side, or hardcoded into the
[36] product. That is something that is
[38] served over an MCP server, and you can
[41] take the server, put it into cloud, you
[43] can put it into ChatGPT, you can put it
[45] into VS Code Cursor, and it will just
[47] work.
[50] And that
[52] I think it's kind of cool because for
[54] doing that, you need something that a
[56] lot of things that we're want in the
[58] ecosystem do not offer. You need
[60] semantics, you need to have both sides,
[62] client and the server, to understand
[65] what each side is talking, to understand
[66] how you render this, understand that
[68] there's a UI coming.
[70] And for that, you need a protocol.
[74] And the best part about this,
[76] an MCP server doesn't just ship an app,
[78] or can ship an app, it can also ship
[80] tools with it, and so you can interact
[83] with it with the application as a human,
[85] and you can have the model interact with
[87] it through tools, which is I think a
[89] very unique thing that I think we have
[91] not explored much
[93] just yet.
[95] Okay.
[96] But, let's quickly rewind a little bit
[98] from this what I think is a really cool
[100] glimpse into the future of MCP into over
[104] a year ago, 18 months, an eternity in AI
[107] life cycle, um all of this did not
[109] exist. There was just a little spec
[111] document, a few SDKs, uh mostly written
[114] by Claude, local only with little more
[118] than just tools. And in that last 18 or
[121] 12 months, you guys have been absolutely
[123] crazy building stuff, um building
[125] servers, building um an crazy ecosystem
[128] around this, and we on our side have
[130] been busy busy taking this local only
[132] thing, added remote capabilities, added
[136] centralized authorization, added new
[139] primitive like elicitation and tasks,
[141] and last but not least, added new
[143] experimental features to the protocol
[145] like the MCP applications that you've
[147] just seen.
[150] And in the meantime,
[152] we have reached, I think, a really cool
[154] milestone because again, you all of you
[156] have been absolutely crazy building,
[157] building, and building. Of course,
[159] luckily with the help of a a bunch of
[161] agents. Um
[163] we're now like at 110 million
[166] monthly downloads. And that's just, of
[167] course, not us using it in our clients
[170] and servers. That's like OpenAI's agent
[172] SDK, that's Google's ADK, that's
[174] LangChain, thousands of frameworks and
[177] tools that you might have never ever
[178] heard of it pulling it as a
[180] as a dependency, which means there's one
[182] common standard that all of us have at
[186] our disposal to speak to each other. Um
[189] just a bit for context, uh React, one of
[192] the most successful um
[194] open source projects probably of the
[196] last decades, took roughly double the
[198] amount of time to reach that download
[199] volume.
[200] And in the meantime, of course, you all
[201] have been building really, really cool
[202] servers from like little toy projects of
[205] WhatsApp servers and Blender servers, uh
[207] to building SAS integrations like
[209] Linear, Slack, and Notion that are
[210] really powering what everyone does every
[213] day when they use MCPs. But most
[215] importantly, the vast majority of MCP
[217] server most of all of us have built are
[219] behind closed doors uh connecting
[221] company systems to agents uh and AI
[224] applications.
[226] But I still think this is just the
[228] absolute beginning of where we are.
[231] Because I think 2025 was all about
[234] exploring, and 2026 is all about putting
[237] these agents into production. Because if
[240] you really think about it, in my mind,
[241] 2024, we just built a bunch of like
[244] demos and showed some cool stuff to
[245] people, and there was a little bit of a
[247] buzz there. 2025 was really all about
[250] coding agents. But coding agent, if you
[252] really think about it, are the most
[254] ideal scenario for an agent. It's local,
[257] it's verifiable, you can call a
[259] compiler, like you have a developer who
[261] can fix if it goes wrong in front
[264] of the in front of the computer, uh and
[266] you can display a UI interface, and the
[269] user's quite happy.
[271] But I think now with the capabilities of
[273] the model increasing, we're going into a
[275] new era, which I think this year will be
[278] we will see the start, where we're not
[279] just doing coding agents, we're going to
[281] have general agents that will do real
[284] knowledge worker stuff, like things a
[286] financial analysis analyst want to do,
[289] uh a marketing person want to do. And
[291] they need one thing in particular. They
[294] don't need a local agent that calls a
[296] compiler. What they need is something
[298] that could connect to like five SAS
[299] applications and a and a shared drive
[302] because the most important part for them
[304] for an agent is connectivity.
[307] And in my mind, connectivity is not one
[309] thing. If one if someone tells you
[311] there's one solution to all your
[312] connectivity problem, be it computer
[314] use, be it CLIs, be it MCP,
[316] they are probably pretty wrong because
[318] the right because the right thing, of
[320] course, is that it always means it
[322] depends, and there's a real a big
[324] connectivity stack, and there's a right
[326] tool for the right job. And in my mind,
[329] there are three major things that you
[330] want to consider building an agent in
[332] 2026. It's skills, MCP, and of course,
[335] like CLI or computer use depending on
[337] your use case. And they have three very
[340] distinct things that they can do in
[341] three different things you want to
[343] consider when you build your agent.
[347] Number one, skills, of course, is just
[349] like domain knowledge, it's just like
[350] capture-specific capabilities put into a
[353] very simple file, and it's mostly
[354] reusable. There are some minor
[356] differences between the different
[357] platform.
[359] Of course, CLIs very popular when local
[362] coding agents. It's an amazing tool to
[364] get simply started, to have something
[367] that you can pose in a bash, that you
[369] that automatically discover where the
[371] model can automatically discover what
[372] the CLI is capable of. And most
[374] importantly, if you have things that are
[376] like CLIs, like GitHub, Git, and other
[379] things that are in pre-training, CLI is
[381] an amazing solution for your
[383] connectivity part, and they're
[384] particularly good when you have a local
[386] agent where you can assume a sandbox,
[388] where you can assume a code execution
[390] environment.
[392] But if you don't have this, if you need
[393] rich semantics, when you need a UI that
[396] can display long-running tasks, when you
[398] can have when you need things like
[400] resources, when you need to build
[401] something that is full decoupled and
[404] needs platform independence, or you
[405] don't have a sandbox, when you need
[407] things like authorization, governance,
[410] policies, or short to say boring enter
[413] boring but important enterprise stuff,
[416] or if you want to have experiments like
[418] MCP applications or what comes soon,
[421] skills over MCP, then I think MCP is
[425] just like additional connective tissue
[427] that is just yet another tool in the
[429] toolbox for you to build an amazing
[431] agent.
[432] And so this is all to say that I think
[434] in 2026, we're going to start building
[436] agents that use all of it. They don't
[439] use one thing, they use all of it, and
[440] they use them quite seamlessly together.
[445] But I don't think we're quite there just
[447] yet.
[449] Because we need to build a lot of stuff
[451] partially um because
[455] our agents kind of still suck.
[457] Um and partially because I think we just
[459] haven't talked enough about like some of
[461] the techniques you can do
[462] uh to really put this connective tissue
[464] together.
[467] The number one thing that we need to go
[470] and start building is on the client
[472] side, on the on the agent harness side,
[474] on the things that powers the connective
[476] parts, that be it a cloud code, uh be it
[480] a pie, be it whatever application you're
[482] going to build.
[485] And the number one thing we're going to
[486] do there, and what we all have to do,
[487] and something I want to really get
[489] across today, is that we need to go and
[491] start building something called
[492] progressive discovery.
[494] Most people when they think about like,
[496] "Oh,
[497] I MCP," they can't think about like
[500] context load. But if you really consider
[502] what a protocol does, the protocol just
[504] puts information across the wire, but
[506] the client is responsible for dealing
[508] with that information. And what
[510] everybody so far has done because we're
[512] in this very early experimentation
[513] phase, is to simply put all the tools
[515] into the context window, and then be
[517] quite surprised that maybe the context
[519] window gets large. Um
[522] but what you can do instead, and what
[524] you should do instead, you should start
[526] using this progressive discovery
[528] pattern,
[529] which is to say, use something like tool
[532] search to defer the loading of the
[534] tools, and start loading the tools when
[538] the model needs it. And we have this in
[540] the Anthropic API, and people can use
[543] this uh on on competitors' APIs as well.
[546] But also, you can just build this in
[548] yourself where you just download the
[549] tool directly, and the moment you give
[551] the you give the model a tool loading
[553] tool, basically, and the model goes
[555] like, "Ah, maybe I need a tool now. Let
[556] me look up what tools I need." And then
[559] you load them on demand.
[562] And here in this example, what you're
[563] seeing is on the left side is uh Claude
[565] Code before we added this to Claude
[567] Code, and then after it uh
[570] to Claude Code. So you see a massive
[572] reduction
[573] in tool
[575] uh use uh tool context usage.
[579] The second part of that is is something
[581] called programmatic tool calling, or
[583] what other people usually refer to um
[585] to code mode.
[587] Um this is the idea that one thing that
[591] you really want to do is you want to
[593] compose things together. You don't want
[596] the model to go call a tool, take the
[599] result, then go and talk, call another
[601] tool,
[602] take the result, call another tool.
[604] Because what you're effectively doing is
[605] you're letting the model orchestrate
[607] things together, and in that
[608] orchestration, you're using inference,
[610] you're it's it's latency sensitive, and
[612] all of it stuff could be done way more
[614] effective if you would instead write
[619] a script.
[621] Um
[622] and in fact, that's actually what you
[623] constantly do and what you constantly
[624] see things like hard code do when it
[627] writes the bash command. But you can of
[628] course do this with everything, and you
[630] can do this with MCP, and you should do
[632] this with MCP. So, what does this mean?
[634] So, what you want instead of having one
[637] tool at another, you want to give the
[639] model a repple tool, provide like a like
[642] a execution environment, like a V8
[644] isolate or a monty or something like
[647] that, or a lua interpreter, and just
[649] have the model write the code for you,
[652] and the model just executes that code,
[654] and then composes them together. And
[657] there's a neat little feature in MCP
[659] called structured output that tells you
[661] what the return value of the output will
[664] be, and the model can use this
[666] information to to figure out type
[668] information, which then mean it can
[670] really nicely compose these things
[673] together. And in this example here,
[675] instead of doing two different calls,
[677] you do one call, and you can filter that
[680] the model will automatically
[682] remove things from a JSON and just
[684] continue.
[686] Of course, if you don't have uh
[688] structured output, you can always just
[690] ask the model to give you structured
[691] output
[693] um
[694] uh by just extracting it and saying,
[696] "Hey, call us cheap model and say, 'I
[698] want this expected type, give it back to
[700] me.'" And bam, you have a type, the
[701] model can compose things together, and I
[703] think this is something we're just not
[705] doing enough yet, and this is I think
[707] something where we can improve our agent
[708] harnesses.
[710] And then last but not least, of course,
[711] you can just compile compose these
[713] things together with executables, like
[715] with CLIs, with other components, with
[717] APIs as well.
[719] Um next, what we need to do besides the
[722] client work, which is progressive
[723] discovery and
[725] um programmatic tool calling, we need to
[728] go and start building properly for
[730] agents. And that means we all need to
[732] stop taking rest APIs and put them
[735] one-to-one
[736] into
[738] uh an MCP server. Every time I see
[740] someone building another rest to MCP
[743] server a conversion tool, I'm it's a bit
[745] cringe because I think it's just it just
[747] results in horrible things.
[748] Um and what you should do instead, you
[750] should design for an agent. Or
[751] basically, you can start designing for
[753] you as a human, how you would want to
[755] interact with this, because that's
[756] actually a very, very good start for an
[759] agent.
[760] If you want to orchestrate things
[762] together, you should reach, of course,
[764] for programmatic tool calling, and you
[766] can do this on the client side, as I
[767] said before, but you can also do this on
[769] the server side. The Cloudflare
[772] MCP server and others like that are
[774] great examples how you can have, instead
[776] of providing tools, provide an execution
[779] environment to the model and then just
[781] have them orchestrate things together,
[783] which again cuts on token usages,
[785] cuts on latency, and is way more
[787] powerful in its composition. And then
[790] last but not least, you should start and
[792] we should start as server authors to use
[794] this rich semantics that MCP offers over
[797] alternatives. This means shipping MCP
[799] applications, it means shipping
[802] skills over MCP, it means
[805] um using things like task and other
[807] aspects that the protocol offers that
[809] we're currently slightly underused, or
[811] things like elicitations.
[813] Things that only MCP can do for you.
[816] And of course,
[818] that's all the work you all need to do,
[820] and maybe some of our product people
[821] need to do, we also need to do a lot of
[823] work on MCP itself. And there's a few
[825] things down the line that we're going to
[828] go and have to go and solve.
[830] The number one thing is we need to
[831] improve the core. There's a few things
[833] that, as we have developed the protocol
[835] over the last year, that are just not in
[837] a good shape. Number one is that the
[839] current streamable HTTP is very hard to
[842] scale if you're a large hyperscaler.
[845] >> [snorts]
[845] >> And so, we have a proposal from our
[847] friends at Google,
[849] who are working on something called a
[850] stateless transport protocol, which make
[853] it significantly easier to just treat
[856] MCP servers like
[858] you know, another stateless uh rest
[860] server or something like that and we are
[862] used to know how to deploy to like cloud
[865] runs or kubernetes and so on. So, that's
[867] coming down in June and hopefully lining
[869] in the SDKs very soon.
[871] In addition, we need to improve our
[874] asynchronous task primitive, which
[876] basically is a very fancy way to say we
[879] just want to have agent-to-agent
[880] communication. We have a very
[881] experimental version of the protocol
[883] that very few clients support, so we're
[885] going to start building more clients out
[888] like that, and most importantly, we are
[889] improving some of the little semantics
[891] that we need to do. We're going to ship
[893] a TypeScript version SDK version two and
[895] Python SDK version two based on a lot of
[898] the lessons learned over the last year.
[902] There's a there's a
[904] SDK called fast MCP.
[907] Who's using fast MCP? Yeah. It's just
[909] way better than Python SDK that
[911] we're shipping, right? And that's on me
[912] because I wrote the Python SDK.
[915] Um and and so, I have a bunch of people
[917] who are way better Python developers
[918] than me help me write it better. Um the
[921] second part is we need to start
[923] integrating everywhere. We're going to
[924] ship for particularly for enterprises
[926] something called cross-app access. It's
[928] a new thing that we're working closely
[930] together with identity providers, which
[932] just allows you It's a very fancy way to
[933] say
[934] once you log in once with your local
[936] company identity provider, be it a
[938] Google, be it an Okta, you will be able
[940] to just use MCP servers without having
[941] to re-login. So, it's a bit more
[943] smoothness. Um in addition, we're going
[946] to add something called a server
[948] discovery by
[950] by specifying how you can discover
[953] servers on well-known URLs
[955] automatically. So, crawlers, browsers,
[958] um
[959] agents can just go to a website and say,
[961] "Oh, I'm instead of just parsing the
[963] website, is there also an MCP server I
[965] can use?" And we will be able to
[966] automatically discover this.
[968] This is a really cool thing that will
[969] come down also in June when we launch
[971] the next specification
[973] and will be supported there.
[975] And then last but not least, we're
[977] starting to use our extension mechanisms
[979] in in MCP, which means that some clients
[981] will support this, like for example, MCP
[983] applications will only be supported by
[986] web-based interfaces, because if you're
[988] a CLI, you just have a hard time
[990] rendering HTML, right? Um and we will do
[992] more of these extensions. One of the
[994] most exciting extensions that I think is
[996] is cool, we're just going to ship skills
[998] over MCP, because it's very obvious that
[1000] if you have a large MCP server with tons
[1002] and tons of tools, you just want to ship
[1004] the main knowledge with it and say, "Oh,
[1006] this is how you're supposed to use this.
[1008] This is how you're supposed to use
[1009] this." And it allows you as a server
[1011] author to continuously ship updated
[1013] skills without having to rely on plugin
[1015] mechanisms on registries and other
[1017] stuff.
[1018] So, that's coming down.
[1019] Um
[1020] there's a lot a lot of experimentation
[1022] from people already in that space. You
[1023] can already do some of that today if you
[1025] just give the model a load skills tool.
[1027] Like there you can you can build
[1028] primitives or versions of this today
[1030] without having to rely on the semantics,
[1032] but of course, we're going to define the
[1034] semantics.
[1035] Okay. So, that's for me a long-winded
[1038] way to think to say that I think MCP is
[1040] actually in a really good shape, and I
[1042] think in this year, we're going to push
[1045] uh
[1045] agents to full connectivity,
[1048] um MCP will continue to play a major,
[1050] major, major role. And we want, of
[1053] course, your feedback. We are very open
[1054] community. We are just have created a
[1056] foundation. We're mostly running as an
[1058] open-source community with a discord,
[1061] with issues. Um just come to us and tell
[1063] us where the are we wrong, what are
[1065] we getting right, um so that we can
[1067] improve this on a continuous basis.
[1069] So, 2026, I think is all about
[1071] connectivity, and the best agents use
[1074] every available method. Like they will
[1075] use computer use, they will use CLIs,
[1077] they will use MCPs, and they will use
[1079] will use skills.
[1081] Because they want to have a wide variety
[1083] of things they can do, and then they can
[1085] ship cool stuff like this,
[1088] um
[1088] which is
[1090] um
[1092] one of the product features we shipped
[1093] recently.
[1094] Uh under the hood, it's nothing but an
[1097] MCP application
[1099] um that renders stuff, right?
[1101] Cool.
[1104] So, we can now look at uh the model
[1106] writing graphs.
[1108] Anyway,
[1109] thank you.
[1118] >> [music]
