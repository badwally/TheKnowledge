---
id: yt-1gUnORGKkTM
type: youtube
title: Common Mistakes People Make with Evals [Hamel Husain]
url: https://www.youtube.com/watch?v=1gUnORGKkTM
authors:
- Jason Liu
ingested_at: '2026-05-23T18:54:56Z'
content_hash: sha256:ba63e2c4465a28894ef002b0724cb3f7d2fceaa88da85369690bab2ec8530fa1
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Jason Liu
  channel_url: https://www.youtube.com/@jxnlco
  duration_seconds: 2434
  caption_track: fetched
  snippet_count: 1133
---
[0] this. So, yeah, just to set
[2] expectations, this presentation is going
[3] to be pretty light-hearted. It's meant
[5] to be fun. We're going to leave a lot of
[8] time at the end for questions, but I'm
[10] just going to give you an overview of
[12] certain things to prompt those questions
[15] in your mind. Okay, this question, so
[16] this what is this presentation about?
[18] Common mistakes people make with eval.
[20] And specifically, I want to give you a
[23] guide to wasting time, money, and
[26] resources. I learned this from Jason
[28] taught me this technique. Eval is a
[30] really large kind of subject area. It
[32] could be dry. I don't want to just talk
[35] about okay best practices of evals, how
[38] to do them, so on and so forth. Let's
[40] make it fun. And so to make it fun, we
[42] can invert. And by invert inversion, we
[45] mean, okay, like how can we do evals
[47] wrong? I think that is a lot more fun.
[49] Let's get into it. I'm Hamill. Jason
[52] already introduced me. You can find my
[54] website there. As Jason mentioned, I've
[56] written a lot about evals. And the
[58] reason I've written a lot about evals is
[60] because this is where people tend to
[64] fail the most. And it's not really about
[66] eval strictly. Eval is just the how of
[70] making AI work properly. A lot of times
[73] people when they're building AI
[75] applications, they hit a plateau because
[78] you're only doing if you're just doing
[79] vibe checks. People want to know okay
[81] like how can you go beyond vibe checks
[83] and eval is the central way for you to
[86] put some structured approaches in place
[89] that allow you to measure your
[91] application. Okay, what is the first
[93] step that you can use to really to start
[96] failing fast? And the first thing kind
[98] of mistake is focus on tools not
[102] processes. I find that 95% of the folks
[105] that I work with when we start working
[106] together they have this mindset and just
[109] like Jason I do a lot of consulting and
[111] what does that mean? Okay, rag problems
[113] instead of trying to measure retrieval
[116] metrics and things like that use a rag
[118] use a vector database. You've already
[119] been beaten with that specific advice
[122] throughout this course. So you don't
[124] need me to really elaborate on that.
[126] Need to measure progress? Use
[128] off-the-shelf eval. So a lot of people
[129] are using off-the-shelf eval. We'll get
[131] into that in a little bit, but using
[133] offtheshelf evals is the wrong choice
[136] 99.9% of the time. Fine-tuning without
[139] measuring, fine-tuning models, you don't
[142] even have to be using an open model,
[143] just like fine-tuning open AI, but
[145] without eval is a really bad idea.
[148] Similarly, if you have accuracy issues,
[150] okay, instead of trying to debug that
[153] and trying to figure out like why do you
[155] have performance or accuracy issues or
[157] the LM is not doing what you want, just
[159] trying like different models, just
[161] hopping from one model to the next, it
[163] really it just doesn't work. You're
[165] going to be spinning your wheels.
[167] Similarly, agents not working, try a new
[169] LLM framework. Okay? If agent's not
[171] working, instead of using Langraph, try
[174] Llama index. Llama index doesn't work,
[176] try something else. And then lastly,
[178] probably one of the most the things that
[180] drives me crazy is like eval are a
[182] vendor problem. A lot of people think,
[184] hey, eval what tools do I use? Should I
[187] be using Langsmith? Should I be using
[189] Brain Trust? Should I be using Arise?
[191] What should I be using? That's the first
[193] question that comes to mind. That means
[194] you're in trouble because it's not a
[196] vendor problem. It's a process that you
[199] need to go through and the vendor is not
[201] the solution. And so when you focus on
[203] tools, not processes, like what ends up
[206] happening is like you are going to be
[209] your life is going to look like this
[211] whack-a-ole game. And this is my friend
[213] Greg. And you're really not going to be
[214] making progress. You're just going to be
[216] rotating around different tools without
[219] really having a robust way to improve
[222] things. And so just to drive this home,
[224] this is a real quote from a large
[227] Fortune 500 company. And the CTO said,
[230] "In my opinion, the eval framework
[232] should be generic enough to apply it to
[235] any task. People actually believe this.
[237] And if you believe it, stop it. Get
[239] help. Get help somewhere. Get help from
[242] Jason or get help from John. Doesn't
[244] matter. Get help from somewhere." So
[246] another kind of like example is if you
[250] really want to hurt yourself in really
[252] light stick of dynamite under your ass,
[255] should throw up a dashboard that looks
[257] like this. Import your favorite LLM eval
[260] library and use off-the-shelf metrics.
[263] Calculate helpfulness score,
[264] truthfulness score, personalization,
[267] accuracy, tone. Put on a dashboard, be
[269] like, "Hey, I'm doing eval." And then
[271] you can tell all your co-workers, "Look
[273] how good we're doing." You can even
[274] track those metrics over time. But
[276] really, what are you what are you doing
[279] good at? Nobody knows. You just have
[281] numbers that don't really mean anything.
[283] Who the hell knows the the difference
[285] between 4.2 2 and
[287] 4.7. This tone, what the hell does tone
[290] mean? This is actually a real dashboard.
[292] Okay, it's not a screenshot of the
[294] dashboard. I asked Claude to recreate
[297] the dashboard slightly from a real
[300] screenshot of a client, but this is
[302] actually what I saw. And yeah, this is
[305] one way to waste incredible time and
[307] money cuz you're going to chase these
[309] metrics. They won't really mean
[310] anything. And there's a lot of eval
[312] tools will offer these. You can like
[314] import from eval import help helpfulness
[318] and you can apply that on your traces
[320] and it's honestly it's a waste of time.
[323] Do not do this. Use do error analysis
[327] and find problems that you actually have
[330] and then measure those. Don't measure
[332] this generic [ __ ] So let's go into
[334] it further just to drive home the point
[336] more. Yes. to really maximize the blast
[340] radius of that dynamite under your ass.
[342] Just let other others dictate your
[344] metrics. Use all of them blindly and
[347] trust that they align with your goals.
[349] So, okay, like these are some examples.
[350] I think this is an this on the left hand
[352] side. This is like some eval tool inside
[356] OpenAI's dashboard. Oh, sorry. And they
[359] have some metrics here like sentiment,
[361] they have factuality, whatever. This is
[364] a screenshot from another eval tool,
[366] Brain Trust. This is one from Galileo.
[369] It doesn't really matter if you really
[371] want to yourself fail as fast as
[373] possible. Just adopt all of these at the
[375] same time actually and just like import
[377] all the metrics and throw it on a
[378] dashboard because that will cause
[381] maximum confusion. Okay, so that's like
[383] the first step to failure. The second
[386] step if you really want to twist it
[388] further and really just maximize pain is
[392] like just avoid looking at data. And
[395] these are some rules of thumb, some kind
[397] of beliefs that you can adopt to really
[401] be effective at maximizing this kind of
[403] failure. So one is just believe that a
[406] tool will do it for you. Like you can
[408] just you don't need to look at data.
[410] This is the age of LLM. Why should you
[412] be doing any manual work at all
[414] whatsoever? Just use a tool. Just
[417] outsource it to the tool. It's not your
[418] problem. Okay? And then also, okay,
[421] fine. If you do need to look at data,
[423] you know what? It's not your problem.
[424] Just let an engineer do it. All this LM
[426] [ __ ] is just engineering [ __ ]
[428] anyways. Just let an engineer [ __ ]
[430] look at your data. You don't need to
[431] look at it. And then also just don't
[433] even look at data at all because
[435] honestly just trust your gut. You don't
[437] need to look at anything. Your feelings
[440] are right always right. And then
[442] ultimately just and a lot of people do
[444] this is just depend on users to tell you
[446] if it's broken. So avoid looking at
[448] data. And just to drive home the point
[450] of delegating looking at data engineers
[453] a lot of people do that when I when we
[454] say look at look at data it's the person
[457] with the domain expertise that needs to
[458] look at data and this is a critical
[460] mistake people make so there's a
[463] technique called error analysis that you
[465] may have heard about in this course or
[467] you may have seen indirectly which is
[469] it's really important for you to go
[471] through your data and look at it and
[473] annotate that data so that you can
[475] discover the failure modes you have and
[478] to actually measure things that matter
[481] and not that dashboard full of XYZ
[483] metrics. Yeah. If and we talk about it.
[486] I have a little page here. This is from
[488] a different presentation for executives.
[491] But if you want to maximize failure,
[494] don't do this. Do not look at your data.
[496] Do not label it. And a lot of people, if
[499] you really want to fail even harder,
[501] just make it have an excuse that like,
[504] hey, looking at data is hard. You need
[505] to buy specialized tools to do that.
[508] Don't use simple easy to use things. So
[511] being unsarcastic for a moment, you can
[513] you can use things like Excel to start
[516] looking at data and do this error
[518] analysis. I'm not going deep into error
[520] analysis now. We can talk about that in
[521] the Q&A. This is just more to bring up
[523] the the point of hey like error analysis
[526] 101 is basically looking at your traces
[530] and categorizing the errors that you
[532] have and writing notes about them and
[534] then doing some data analysis over those
[536] not those notes to highlight what kinds
[539] of failures you have. This is like a
[541] example just a screenshot from a some
[544] error analysis that I've done recently
[546] where okay like LM responses there's a
[550] lot of incomplete responses where the
[552] input had code in it. So that might not
[555] mean anything to you but this is an
[556] example and that drives okay what kinds
[559] of tests you writes what kinds of eval
[561] you might write so on so forth. And then
[562] finally encourage agent astronauts. So
[565] instead of actually building anything
[567] just keep drawing these diagrams and I
[570] see this all the times. Oh should we use
[573] lang graph? Should we use you know llama
[575] index is our architecture like really
[577] sweat about if your architecture is
[579] right if you're using like enough agents
[581] and what agent should go where and just
[584] get really caught up in that and forget
[587] about eval. Just start with the most
[589] complex solution. And then really last
[592] the last thing you could do is really
[593] just throw away everything that has been
[596] the wisdom of classic machine learning.
[598] So this is a diagram. You may have seen
[600] it before if you've you're familiar with
[602] machine learning. This is from a a
[604] Google paper about technical debt in
[607] machine learning systems where it's like
[608] machine learning systems are all very
[610] complicated. There's a lot of different
[611] concerns that you have feature
[613] extraction serving infrastructure
[615] process management tools machine
[617] learning code and hey we don't need any
[619] you don't really you can have the belief
[621] like hey you don't need any data
[623] literacy you don't really need any of
[625] this knowledge because LLMs are just
[627] APIs but really are is it is that really
[630] the case and if you look really closely
[633] a lot of these things are the same
[635] configuration there's elements of that
[638] with when we talk to talk about managing
[640] prompts, data collection, you have human
[642] in the loop workflows when we want to
[644] curate data sets. This course covered
[646] rags, so don't need to go into what that
[648] is, but there's a reason EVAL is at the
[650] center of this because you want to
[652] verify what's coming in and out of the
[655] LLM. And then finally, on an unsarcastic
[657] note, you you could also just ignore
[660] conventional wisdom. Hey, that manual
[662] inspection of data probably has that is
[665] very important and then eval are very
[667] important. But as you can yeah that's
[670] and yeah that's the that's the sarcastic
[673] talk. Hopefully that was lighthearted
[675] and fun. We're doing a course on evals
[678] that will take you through in a lot of
[680] detail like how to construct evals, how
[684] to deal with very complicated cases like
[686] where you may have multi-turn
[688] conversations where outputs are
[689] ambiguous, what to do if you don't have
[692] data, what to do if you don't have
[693] users, all kinds of things. We go that
[695] through that in a lot of detail. If
[697] that's interesting to you, check it out.
[699] Otherwise, we can Yeah, we can have Q&A.
[702] Awesome. Let me uh open up the slide.io
[704] And then I think there's only a couple
[706] questions there and then we probably
[707] have a conversation more about some of
[709] the things that you've seen so far in
[711] your consulting. The first question is
[713] for the retriever component. What is the
[715] suggested approach for evaluating
[717] results when you have ground truth?
[718] Right. So this would be in generation
[720] for example. Are you able to see the
[721] buildings by the way? Sorry. What was
[722] the question buildings? Are you able to
[724] see the uh questions as well? I just
[725] left a comment in the chat. Oh, I see.
[727] Let me open it. Perfect. You're still
[729] sharing your screen by the way. Let me
[730] stop. Okay. Let me open the questions.
[732] For the retriever component, what's
[734] suggest suggested approach for
[735] evaluating results when you have ground
[736] truth? So actually you should look at
[738] Jason's blog. He has a really good blog
[741] post. I think it's like levels of rag
[744] maybe. And in that, let me see if I can
[746] find it. I can take a look. So there's
[748] like level four evaluations. And that's
[751] like a nice very highle way to think
[754] about in that blog post level, it's
[756] called levels and complexity rack
[758] applications. He does like synthetically
[761] generate what the Q&A like the Q&A pairs
[764] are. The same holds true if you already
[765] have ground truth if that makes sense.
[767] And you can I think here this is also a
[769] good case of actually using something
[771] like an LLM to judge these results right
[773] because excuse me we have pretty good
[776] reasoning models now where given a
[777] certain answer if it's certain if it's
[779] slightly rephrased or anything like that
[781] do you feel like just judging the
[783] similarity of a synthetic answer or a
[785] ground truth error with the LLM output
[787] is a pretty good idea or do you feel
[789] like even then we need to start thinking
[790] about training our own LLM as a judge
[793] for just comparing string answers for
[794] example. Yeah, if you're comparing
[796] string answers, then no. But if you want
[798] some more nuance analysis, like you're
[800] saying that you want some kind of LM as
[803] a judge, that's fine. I think that in
[805] practice, you need to do an analysis
[809] that lets you trust your LM as a judge.
[812] And what that means is you need to do
[813] some human labeling that where you
[816] measure the agreement of the judge with
[818] you. Because at the end of the day, the
[820] reason why most LM judge fail is people
[822] don't trust them and they don't
[823] understand them. So that's yeah it's key
[826] that you do that and I think that kind
[828] of answers to John's question as well.
[830] Yeah. Do you think that with these new
[831] reasoning models there's more to trust
[833] or do you still generally think that the
[835] case that is it still doesn't really
[836] live up to expectations especially with
[838] the 03 like mini for example. So you do
[842] have to check it like there's no I don't
[844] care how smart it is. Even if it was you
[846] Jason manually judging everything I
[849] would still check it to trust it. And
[851] like you might check it less like the
[853] stronger the model it is you may but you
[856] still have to do that exercise of okay
[859] does it match the domain expert there's
[861] really no escaping that cuz at the end
[863] of the day you have to trust the judge.
[866] There's only one way to do that. I see
[868] this is a question that I tend to bring
[869] up as well which is what if we don't
[871] actually care about the values of these
[872] offtheshelf evals but just that as we
[875] monitor them over time we want to look
[876] at situations when they change
[878] radically. Imagine a line sort of
[881] plummets at some random day at some
[883] random time. Yeah. So what you can do is
[886] you can do statistical tests and things
[888] like that to see and you can set up
[891] monitoring on that to see okay if points
[894] are going beyond certain thresholds. So
[896] that's certainly a valid exercise.
[898] There's actually some people building
[900] tools that focus on just that aspect.
[903] It's certainly valid. I would say make
[906] sure that your evals are not too
[910] hypothetical like that you understand if
[912] what the value means to you. So it
[914] shouldn't be like going back to that
[916] dashboard where I have all these random
[918] metrics and you just want to know if one
[920] of them changes drastically. I find that
[923] if you don't understand your metric then
[925] it's just adding a lot of noise. I would
[927] just caveat don't make the exercise too
[929] academic. I guess a followup question on
[931] the off-the-shelf evals is do you not
[933] believe in any general purpose eval
[935] frameworks or is it the case that we
[937] feel like it's too early in the tax
[939] cycle and we don't really have a a a
[941] strong standard yet? So I think on
[943] balance general eval frameworks where
[946] you just point some at it and it just
[949] tells you whether what your problems are
[951] and you're doing good or bad generally
[954] don't work that well. They demo really
[957] well in like sales meetings, but they
[959] don't work. And that's because domains
[962] tend to be fairly specific and the
[965] problems they tend not to align with the
[967] problems that you should actually care
[969] about and the failures that you are
[970] actually having. They might surface some
[972] problems, but it's a slippery slope like
[975] you don't want to just rely on those and
[978] think that you've solved your EVAL
[980] problem because it tends to be fairly
[983] low signal. Now, if we start getting
[986] close to AGI, then maybe you could say
[989] like the work that I'm doing or Jason is
[992] doing to look at data and figure out
[995] like what you should be measuring and
[996] how you should do that. Okay, that can
[998] be done by an AI, but at this point it's
[1001] not at that. Maybe you could pose a
[1004] general question to an AI at some point
[1007] where it might be able to do that, but
[1008] it's hard to know that without looking
[1010] at data first and coming up with
[1012] specific metrics. And then also like you
[1015] can measure an infinite set of things.
[1017] So you can come up with an infinite set
[1019] of metrics and also there's lots of
[1022] different components in AI applications.
[1024] There's tool calls, there's rag, there's
[1026] agents, and you can measure each
[1028] component and you can ground really fast
[1031] in all of these things if you're if you
[1034] don't prioritize and have some focus.
[1037] And that's why it's really important to
[1039] do error analysis first to focus
[1042] yourself on what matters. So that's
[1045] another reason why I just don't think
[1047] general purpose eval frameworks are a
[1049] good idea. Do you have any like if the
[1052] next question is do you have any case
[1053] studies or examples where you have
[1055] divine defined some kind of very highly
[1057] specific or highly valuable set of evals
[1059] that you've implemented and worked
[1061] really well? Yeah, I have a couple of my
[1062] own, but I'd love to hear yours first.
[1064] Okay. Yeah, I'll just give you some
[1065] really dumb examples just to drive home
[1067] the fact that it doesn't have to be
[1068] rocket science. So, for example, if you
[1070] ever see if you see like UU IDs being
[1072] emitted into the user or in the AI
[1075] response when it shouldn't be cuz it's
[1077] in the system message or something.
[1079] Okay, that might happen. Or you might
[1081] have formatting issues. You might have
[1083] other dumb things that you can easily
[1085] write assertions and tests for that you
[1088] know shouldn't be happening, but you
[1090] only find that because you're looking at
[1091] your data. Another example is I'm
[1093] working with a a leasing an AI apartment
[1096] leasing assistant and its job is to one
[1100] of his jobs is to help make
[1101] appointments, but it's always getting
[1103] dates wrong. There's like some ambiguity
[1106] sometimes in the way that you might ask
[1107] for appointment about what date you're
[1109] actually talking about that a human that
[1111] you might understand but the AI is
[1114] getting wrong. So yeah, you can have
[1116] some you can test that. You can test
[1118] okay, you can have ground truth there
[1120] and you can write tests. There's and
[1122] there's some examples I've talked about
[1123] publicly. For example, like I've worked
[1126] on a lot of code things. So like a
[1128] natural language query assistant like
[1130] there's a product called honeycomb where
[1132] you can type in natural language query
[1134] and it or it generates a honeycomb
[1137] query. So in that case, yeah, I have LM
[1139] as a judge that really bakes in like a
[1143] lot of failure modes that tend to happen
[1145] that is correlated with a domain expert
[1148] and they trust it. So those are some
[1151] examples of like everything from really
[1154] stupid right assertion to like LM as a
[1156] judge. Yeah, I'll add one that I talk
[1158] about in next week's lecture just
[1160] because it's been top of mind which is
[1161] we have a I worked on a sales bot where
[1164] after the call we would basically try to
[1166] reference as many existing articles and
[1168] our marketing content to supplement the
[1170] conversation that we had. So maybe
[1172] during the phone call we talk about this
[1174] new feature. We want to make sure that
[1175] in our email we link to that feature or
[1177] link to a blog post that mentions that
[1179] feature. And when we first ran this,
[1181] what we found was sometimes it would
[1183] either make up a URL entirely or the URL
[1186] would be from our domain. So maybe it's
[1189] like json.com, but then the slug was
[1191] wrong. And our simple eval was
[1192] effectively running a regular expression
[1194] to find all the URLs verifying that all
[1196] the URLs came from our website and then
[1200] we would make a small post request to
[1201] that URL to make sure that page was not
[1203] a 404. This is a very simple. Find a
[1206] regular expression, ping every single
[1208] URL, verify that it's on our domain,
[1210] it's on a white list of domains, or it
[1212] has a 200 status. And just by doing
[1215] that, we went from a 1% to 3%
[1217] hallucination rate to basically no
[1220] errors in our URL generation. This might
[1221] feel obvious, but even deep research
[1223] right now, if you ask for tables of
[1225] URLs, sometimes will just create
[1228] example.com/ whatever. And so even deep
[1230] research right now will give you URLs
[1232] that don't point to anything. And that's
[1234] a great example. You can only become
[1236] aware of that kind of error if you
[1238] looked at your data and you've looked at
[1240] some examples. If you just threw like a
[1242] general eval framework on it, there's no
[1245] way in hell that would be like tell you
[1247] about this very specific thing. That's
[1248] why they don't work. Yeah, there's been
[1250] examples like early on in development
[1252] where someone had asked a question about
[1253] a feature and it would just pull this
[1255] feature from any arbitrary provider. We
[1257] also have this feature, but there
[1259] there's probably some probability that
[1260] it mentions the feature from a URL from
[1262] a competitor and that would be that
[1263] would look terrible. But these tests
[1264] again are very simple. Like another very
[1266] simple eval was for meeting
[1268] summarization where our eval was just
[1270] the length of the summary divided by the
[1272] length of the transcript and we knew we
[1274] wanted to be between 40 to 50%. We
[1277] didn't want it to be 10%, but we didn't
[1278] want it to be 90%. And again, you don't
[1281] really need any sophisticated tools to
[1282] build those things out. And those are
[1284] the things that really matter, right?
[1286] It's very if you use sophisticated
[1287] tools, you're going to you're going to
[1289] torpedo yourself because you're just
[1291] going to waste time. Like you're never
[1293] going to get to that answer. Exactly.
[1294] So, a ton of these simple things are um
[1296] pretty pretty straightforward. I think
[1298] the second question is is really
[1300] interesting because you've also written
[1301] extensively around this which is what is
[1303] the equivalent of a unit test, a
[1306] integration test and an endto-end test
[1307] for AI applications and how do you focus
[1309] on each one? Okay, I've written about
[1311] that so much that I don't it's yeah let
[1314] me see if I can figure out a different
[1315] way to say it is you can test an
[1317] infinite amount of things. Okay, like I
[1320] said, you can test the rag, you can test
[1322] the retrieval separately, you can test
[1324] the function calls are working, you can
[1325] test, you can do an intent, you can just
[1327] test the final output, you could do all
[1329] kinds of [ __ ] Uh, you can use LM as a
[1332] judge. What do you test? That's the
[1334] question everyone has. And the answer to
[1337] that question is doing the error
[1339] analysis, looking at your data. I would
[1341] almost say eval is not even as important
[1344] as looking at your data. And when I say
[1346] looking at your data, it's a structured
[1348] way of looking at your data. And there's
[1350] different levels or different levels of
[1353] sophistication of looking at your data.
[1355] But just to begin with, it's going
[1357] through your traces and categorizing
[1360] different errors and then doing some
[1361] data analysis on that to figure out okay
[1365] what is like the most pressing problem
[1367] that I should solve. And then also in
[1369] there you will find okay, these are some
[1372] things I should measure. You can't
[1373] measure every you shouldn't try to just
[1374] come up with try to measure everything.
[1376] Now the question of what is the
[1377] equivalent of unit integration end to
[1379] end tests I think that doesn't really
[1382] matter. I think it's apparent like you
[1383] can measure different components you can
[1385] measure the entire system as a whole
[1388] just does the output work like the is
[1391] the output given to the user the final
[1392] result is it what they're looking for
[1394] but really it should be driven by the
[1397] error analysis. Yeah, in these examples
[1399] with the meeting notes, it was very much
[1400] just a case that our customers kept
[1402] saying that feedback that the summary
[1403] was too short relative to how long our
[1406] six-hour meeting was and now we'll
[1407] define one eval to address that and then
[1410] someone else would say, you know what,
[1411] the links keep breaking. Okay, great.
[1413] Now, let's add one more eval. It's
[1414] rarely the case, at least in science, to
[1417] create these eval before we actually
[1419] build out the product. I think a lot of
[1420] computer scientists at least if you
[1421] think about what the CS homework looks
[1423] like it's very much let's enumerate all
[1425] the failure modes and then write
[1427] software that captures these failure
[1428] modes whereas I think in practice a lot
[1430] of the time you will tend to deploy
[1432] something get some testers get that
[1434] feedback and then you capture the evals
[1436] through that negative feedback. This is
[1437] also a really great question because I
[1439] also have a a pretty high conviction
[1441] answer these days which is what is the
[1443] least painful way to do human data
[1445] labeling? How do you convince
[1446] enterprises to dedicate what n
[1448] percentage of time to verify answers
[1449] especially when domain experts are
[1451] needed? So it's really important to
[1452] remove all friction from doing human
[1454] labeling. And human labeling, let's
[1456] generalize that term a little bit to
[1458] looking at data. Okay? Like so what I
[1462] mean by that is where your data lives.
[1464] If it's living in some kind of
[1466] application, whatever logging system
[1468] that you're using, you shouldn't have to
[1470] click 10 times on something to read
[1473] trace. Also a lot of domain specific
[1478] situations call for rendering the trace
[1480] in a very specific way. Let's say you
[1482] have markdown in your trace. Let's say
[1484] you have widgets that you're that you're
[1486] rendering in your chatbot whatever. A
[1489] lot of times like you need to render
[1490] that information so that you can read
[1492] it. You don't want to read a big blob of
[1495] stuff that's not human readable. Also a
[1497] lot of times like there might be
[1498] metadata that you need access to. There
[1500] might be external systems that you need
[1502] to or you need like side by side to
[1504] evaluate whether a trace is doing what
[1506] it whether this to evaluate like an
[1509] interaction being successful or not. A
[1511] lot of times so for the simple cases it
[1514] can be really effective to use Excel.
[1516] Sometimes it depends if it's really long
[1518] multi-turn conversations that don't fit
[1520] in Excel and it's janky then you can't
[1522] really use it. Sometimes you can use
[1525] these observability eval tools. They'll
[1527] have annotation cues, but it's really
[1529] important that you're able to page
[1530] through them very fast without having to
[1533] click on a bunch of stuff and a lot of
[1535] times I build my own. You can build
[1537] something in Streamlit, Graddio,
[1539] whatever. And it doesn't take that long
[1541] to build. You just have some buttons and
[1543] place to put notes, but then you can
[1545] render stuff in the way you want. You
[1547] can render the chat in the way you want.
[1548] You can render, you can put metadata on
[1550] the page. You can render markdown. You
[1552] can render widgets. whatever the hell
[1554] you can put links on there that link
[1556] like whatever you need and that's often
[1559] worth it. It takes away all the pain
[1562] from annotating and because it's the
[1564] most important activity you can engage
[1566] in with AI. It's really high return on
[1568] investment. I would say you need to
[1570] think about doing that and we're not
[1572] really talking about that much time. We
[1575] say like dedicate how you convince
[1577] enterprises dedicate percent of time.
[1579] You're not we're not you don't have to
[1580] annotate every single trace that occurs.
[1583] You can sample. There's ways to sample.
[1586] Jason may have already talked about you
[1587] can cluster your traces. You can explore
[1590] these different clusters, things like
[1592] that. And it's not about Yeah. The way
[1595] convincing enterprises is you can't skip
[1597] it. If you skip looking at data, then
[1599] you might as well just stop. It's not
[1602] going to work. Essentially, as a
[1604] consultant, there's been times when I've
[1605] just offered to give them money back,
[1606] right? Like, if you're hiring me to make
[1608] your AI better and you're not going to
[1609] label any data, then it's not going to
[1610] get any better. So, here's the money
[1612] back. Let me know if you're more serious
[1614] about doing this kind of work. I'll also
[1616] add one call out or two call outs
[1618] really. The first one is especially in
[1620] the world of having things like lovable
[1622] or bolt or sonnet and cursor building
[1625] oneoff data labeling tools has become
[1628] very straightforward especially if you
[1629] just make your backend some kind of
[1631] SQLite thing right I think some of these
[1633] new AI tools they can just connect to
[1634] superbase and now you have a backend in
[1636] the cloud. The second thing also is the
[1638] fact that there are different kinds of
[1641] tasks you can ask someone to do. If you
[1643] were to give me a task that says given
[1645] this text summarize something for me
[1647] that would take the human a lot of
[1649] effort and cognitive load and it would
[1650] be a very slow task that might take 3
[1652] minutes per label. But humans and just
[1654] like models are much better at choosing
[1657] preferences or doing binary tasks. So,
[1659] not only is it about what task do you
[1661] build, but how how can you make a task
[1663] that is should just be a pass fail,
[1666] right? If you generate me two summaries,
[1668] I it's very easy for me to tell you
[1670] which summary is the better one.
[1671] Whereas, if you give me a single
[1672] summary, now I have to think of read
[1674] this whole thing and figure out what's
[1675] going on. Same thing with reasoning
[1677] steps. It's one thing to ask a human to
[1679] reason. It's another to say given an LLM
[1681] reasoning, do you agree with it or not?
[1683] And again, it's all about making these
[1685] tasks very binary where they should just
[1687] be J to accept, K to reject, then you're
[1689] on to the next
[1690] label further and say highly bias
[1693] yourself towards binary scoring. Don't
[1696] have one to five scores because it's
[1699] very complicated to align on that and
[1701] they tend to go off the rails when
[1703] you're beginning. Just you need to
[1704] simplify and use binary kind of
[1707] judgments. Matthew, do you want to jump
[1708] on to first question? Hey. Yeah, I have
[1711] a question about how to like eval in the
[1714] context of experiments. If you're making
[1715] a change to LLM system, it seems largely
[1718] the way a lot of people do it is just
[1720] eyeballing, right? As in not really
[1722] attempting to measure statistical effect
[1724] and just seeing the number goes up. And
[1725] I was curious, I know the answer is
[1727] probably it depends right on what
[1728] ultimately you're trying to do like what
[1730] you care about like the sensitivity or
[1732] like how precise you care about your
[1734] results, but from your experience like
[1736] working with a lot of teams on this. I'm
[1738] just curious if there's any if you see
[1740] like how much of the sort of statistical
[1742] robustness do you see when writing
[1743] evals? Yeah. Interpreting the results of
[1745] evals. There isn't to be honest with you
[1747] in the wild there isn't I haven't seen
[1749] too much robustness. People trying to
[1751] add error bars on their evals and things
[1753] like that. people struggling with
[1756] creating the evals to begin with that
[1758] make sense and it's quite the journey
[1761] for people at least now especially if
[1763] you don't have like data expertise or
[1765] data science background if you have data
[1766] science background totally different
[1768] situation but that's the minority of the
[1770] situations and yeah there aren't many
[1772] people doing it yeah like it is worth
[1775] thinking about especially like if your
[1776] system is stable and you have like good
[1779] baseline from which to begin with and
[1781] you have some idea of what you're
[1782] looking for but Yeah, that's my
[1784] observation. The closest I've gotten to
[1787] doing this kind of experimentation is
[1788] just two things like either one
[1791] bootstrap sampling with replacement to
[1793] compute some kind of error bars when you
[1795] do these like bar charts or two thinking
[1797] about doing these like kind of t tests.
[1799] That said, you know, I think a lot of
[1801] companies I I join, they start with only
[1803] maybe 30 to 40 evals in which case like
[1805] nothing is really going to work. A lot
[1807] of the statistical signals is really
[1808] going to come in once you have hundreds
[1810] of evals to run against. And so the
[1812] first step unless you already have
[1813] hundreds of evals is basically just to
[1816] you know create synthetic data create
[1817] more tests sample from user production
[1819] traffic and then get to a place where we
[1821] can use something like bootstrapping or
[1822] t test to compare results. Awesome.
[1825] Thank you both John. Uh I wanted to
[1827] follow from the this conversation but
[1829] also the previous whenever you have
[1832] humans labeling stuff help me understand
[1835] a little bit more concretely where that
[1837] where does that data go like where do
[1839] you store it? How much of it goes into a
[1841] business discussion? This is what we
[1842] need to focus on versus concrete unit
[1845] test or like more formal valves. When do
[1848] you do the valves? Is it when you're
[1850] merging a branch or is it just periodic
[1852] or is is there like a time-wise pipeline
[1855] of setting up a valves for companies?
[1858] Yeah. So, okay. With the labeling, where
[1860] does it live? Could live anywhere. You
[1862] want some kind of database ideally that
[1864] you can put stuff into group them by
[1866] annotation run or something like that.
[1868] sometimes is spreadsheets. It depends. I
[1870] don't try to be too dogmatic about it
[1872] because the most important thing is
[1873] people do it and then it ends up in a it
[1876] should be used for decision- making. So
[1878] you're like where does it come up in the
[1879] business context? Okay, we are seeing
[1881] that XYZ problem is occurring a lot.
[1885] Let's go fix that. And then ABC problem
[1887] is here. We don't really know how to fix
[1889] it, but let's go ahead and at least
[1891] write an eval for that right now, you
[1893] know, to try to at least start measuring
[1894] it cuz we don't even know how to fix.
[1896] Those are the kinds of discussions that
[1897] happen. And then like when do you run so
[1899] let's say you run evals so like emails
[1902] have a cost you know there's like the
[1905] spectrum is like free to like very
[1907] expensive free is writing an assertion
[1910] that's like a string comparison
[1912] somewhere in the middle is like maybe LM
[1914] as a judge which is okay you're running
[1916] you're calling an LLM and then like on
[1918] the and then there's like whatever human
[1921] humans like labeling stuff there's not
[1923] really like a silver bullet answer but
[1926] for the free stuff you And you can think
[1929] of that as this. You can run those just
[1931] as frequently as you run your unit tests
[1933] in your code. Whatever you have in pi
[1935] test, you can put those in pi test if
[1937] you want. Doesn't matter. With the ones
[1938] that are a little bit more expensive,
[1939] you have to be a little thoughtful like
[1941] how expensive is it. And you might want
[1943] to run it a little bit more infrequently
[1946] depending on what it is. There's like
[1948] slow tests and some of these tests like
[1950] take time. They might take like several
[1952] minutes to run. And so what I have done
[1954] with my clients is like we yeah we have
[1957] different cadences for different tests
[1960] and different things that will trigger
[1961] those tests. It's not just on every
[1963] commit. It's like on some other kind of
[1966] event that will trigger those tests if
[1968] that makes sense. Yeah. You just have to
[1970] figure out the cost benefit and
[1972] slaughter it in. But there's a spectrum
[1974] that you can think about. And your
[1976] customers when they're dealing with even
[1978] the unit test, they can still be very
[1980] non-deterministic that like the unit
[1982] test in this domain is a weird beast
[1984] compared to what we've always thought of
[1986] as unit test. What do your customers how
[1989] do your customers process a unit test
[1991] that doesn't have a deterministic
[1992] failure but always this weird
[1994] stoiccastic stuff? Yeah. So that is so
[1998] in those cases like we we're logging
[2001] things. So sometime I have some
[2002] customers that like have LM invocations
[2004] in their unit test because they're so
[2005] cheap like they're like ah it's not a
[2007] big deal whatever who cares and for
[2009] those cases like those metrics are
[2010] logged to a database and then they're
[2013] just looking at really high level is the
[2015] number actually like is there a notice
[2018] not noticeable deviation and there's
[2020] some more analysis that's automatically
[2022] done. It's not just one metric. It's
[2024] okay. These are different product areas
[2026] and different scenarios and what are the
[2028] errors errors in each of those. And then
[2030] we have a side by side that shows like
[2032] the baseline versus that and we're just
[2034] looking to see okay is there a large
[2036] deviation. You could do a statistical
[2038] analysis on it. Like I said, a lot of my
[2040] clients are not there yet. They're like
[2042] just getting to that point where like
[2044] putting the plumbing in place. Ashan, do
[2046] you want to go for the last question
[2048] before we wrap up? Yeah, my question is
[2051] following up on the question of the
[2053] quick
[2054] eval summary generation that you
[2057] basically do a display and see how much
[2060] summary you captured. wanted to know if
[2064] you have any experiences on creating
[2067] evals for content generation something
[2070] like legal contract that's
[2073] uh given a prompt or given a query you
[2077] generate a contract and you want to
[2079] evaluate if you've captured all the
[2082] nuances or all the articles have been
[2086] mentioned or any similar experience want
[2089] to know what would be the approach for
[2091] that can you explain what you all the
[2093] articles are mentioned because in this
[2095] example you you could have a situation
[2097] where given some request ahead of time
[2101] what articles should have been
[2102] mentioned. If we have a golden data set
[2104] like that then you can think about
[2106] something like a precision and recall
[2108] for your citations. So given this
[2110] context and this request I know I should
[2112] have mentioned articles 4 9 and 12. Is
[2115] that at least being cited? And if it's
[2117] cited that's one level of those would be
[2119] like the binary tests right? Those are
[2120] the tests that you can run forever
[2121] afterwards. A goon. No, I was going to
[2125] for an example of article. Let's say we
[2128] are creating a contract generation and
[2132] it is in regards to a project and we
[2135] have series of older projects or data
[2139] set and then given that prompt we want
[2141] to generate that contract and then check
[2145] for example if the termination clause is
[2149] mentioned or is not. So there would be
[2151] another set of problems, right? Like we
[2152] could, for example, consider this in a
[2154] way that's much more structured. In
[2156] which case, maybe what I'm asking the
[2157] LLM to do is actually return a JSON
[2159] object first and then I'm going to
[2161] format that into a legal document. And
[2163] if we do that, then we can verify
[2165] specific attributes, whether they're
[2167] missing, how long are they. That's one
[2169] level. The second level of things that
[2171] we look at is basically building a suite
[2174] of judges where really it's just going
[2176] to be like a rubric where maybe there
[2178] are just six different checks I want to
[2181] verify. And as long as you make each one
[2182] binary and you verify whether or not
[2184] that the these binary classifications
[2186] are aligned with your own preferences,
[2188] you'll effectively get a rubric that
[2190] still is something that's very high
[2191] quality. So, one could be I want to
[2194] evaluate the structure of the output
[2196] because every contract has to have a
[2198] termination date and so this is
[2199] something I care about. Maybe I have a
[2201] rubric where there's much more
[2202] subjective things. And then lastly, just
[2205] checking whether or not the documents
[2206] that I think this answer or this
[2208] question should have cited are actually
[2210] being cited. And that could be more of
[2212] like a precision and recall. Am I
[2214] referencing articles that don't need to
[2215] be mentioned? That would be low recall.
[2217] Did I forget to mention article 17 B1?
[2220] If that's the case and I didn't have
[2221] good re recall, it's usually going to be
[2223] a suite of these things. And really, I
[2225] would go down and say, "Okay, turns out
[2226] we do have an issue with making sure
[2228] these dates are extracted correctly.
[2231] Let's build an email for that
[2232] specifically. Oh, I'm noticing articles
[2234] aren't being created. Let's go build a
[2235] single email for that." But again, it
[2238] goes backwards from the errors into what
[2240] the email should be rather than just
[2242] saying we should have a suite of emails.
[2243] I see. Do you have any other examples of
[2246] what? Yeah, that's an important thing to
[2247] repeat again. You should repeat that 10
[2249] times. Go from the errors you actually
[2252] have into the eval. Do not ever go think
[2256] about oh let's like let's think of some
[2258] evals and let's like slap it on your
[2260] data. Just don't never don't ever do
[2262] that. Yeah, makes sense. So for the
[2265] example that I'm working on now and
[2267] challenge with is generating response to
[2270] a RFP and there is generally I've aed a
[2276] system that goes and captures all the
[2278] requirement creates bunch of question
[2280] and then uses those question to
[2283] formulate the template of the response.
[2286] But sometimes there are some nuances
[2289] that is hidden between paragraphs or
[2292] something that is very vague language
[2294] that will be missed and it's a critical
[2297] thing and it is something that like only
[2300] because I have the domain expertise I
[2302] could go read and then figure it out and
[2305] I want to know what or if you had a
[2308] similar experience from a different
[2310] domain and yeah we've done this kind of
[2312] work in financial due diligence but here
[2314] what we've mostly done is make sure the
[2317] templating that we do is very static
[2319] across multiple industries. And so it's
[2321] not the case that I extract the
[2324] questions and create a template. It's
[2325] more that I already have an existing
[2326] template. And so there is always a
[2328] question of how long have the
[2329] co-founders known each other for. That's
[2331] a question that we're going to apply in
[2332] every situ single situation. And because
[2334] of that, we then can just build
[2337] something where we have the field. It's
[2339] autopop populated by an LLM. And when a
[2341] human is reviewing the template, they
[2343] can always press thumbs up or thumbs
[2344] down to figure out that this is good
[2346] quality or bad quality. And now what I
[2348] do is I just go over my template and go
[2350] what are the areas of my template that's
[2352] failing the most and what kind of
[2353] investments do I need to make that
[2355] better. And now usually it becomes a
[2357] thing where oh we are not counting the
[2360] names of the companies correctly because
[2362] in some use cases Calvin Klein for
[2364] Calvin Klein is actually different than
[2365] Calvin Klein CK. Right. Okay. Now, let's
[2368] go build out some dduplication emails to
[2371] to make sure we can solve this problem
[2373] specifically. But there the idea is we
[2374] templatize things. We add buttons to
[2377] collect feedback and then we review that
[2379] feedback to figure out what we need to
[2380] improve next. Thank you. No problem. But
[2382] also, you don't need to be is worth
[2384] mentioning. You don't need to be like
[2385] overzealous about evals. Measure things
[2388] that you want to track. A lot of times
[2390] you'll see an error if you're doing
[2391] error analysis properly, you'll see a
[2392] lot of things that you should just go
[2394] fix. Oh, this is happening. I know
[2396] exactly how to fix that. and then just
[2398] go fix it. You may not need to write an
[2400] email for it. You have to use some
[2401] judgment. Okay, should I be tracking
[2403] this or not? Yeah, the goal really is to
[2405] make a better product. The goal is not
[2406] to have some kind of comprehensive uh
[2408] suite of tests. Asha, did you have a
[2409] followup? I just saw your hand was
[2411] surprised. In which case, I think this
[2413] is a good time to stop. You have 2
[2415] minutes left. Again, HL, thank you for
[2417] this. I'm pretty excited to hear hear
[2418] the longer talk. When is your talk, by
[2420] the way? Do you know if it's on like the
[2422] Friday or the Thursday? I think it's on
[2424] Thursday. On Thursday. Cool. I'll make
[2426] sure we can make that and then yeah,
[2427] sure. I'm sure we'll see it on YouTube
[2429] and and everything else and I'll share
[2430] it with the group afterwards. Great. All
[2431] right, sounds good. Thank you so much,
[2432] H.
