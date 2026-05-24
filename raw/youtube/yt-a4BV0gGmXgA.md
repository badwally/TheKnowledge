---
id: yt-a4BV0gGmXgA
type: youtube
title: Five hard earned lessons about Evals — Ankur Goyal, Braintrust
url: https://www.youtube.com/watch?v=a4BV0gGmXgA
authors:
- AI Engineer
ingested_at: '2026-05-23T18:32:40Z'
content_hash: sha256:7aa1bc7cce5591dc60ab2b85db8ff56ef06a626baccc7100b50fbe82742955d4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AI Engineer
  channel_url: https://www.youtube.com/@aiDotEngineer
  duration_seconds: 1186
  caption_track: fetched
  snippet_count: 499
---
[2] [Music]
[14] Uh let's talk about some of the
[16] interesting things we've learned uh over
[18] time.
[19] Um so the first thing is I think it's
[21] super important for you to uh understand
[24] and define um whether evals are actually
[27] providing value uh for your organization
[29] or not. Um and I tried to come up with
[32] three signs that you should look for um
[34] that that are good. Uh so the first is
[38] um if a new model comes out uh you
[40] should be prepared um uh via your evals
[44] to be able to launch an update to your
[46] product within 24 hours that
[48] incorporates the new model. Uh Sarah
[50] from Notion um she talked yesterday she
[52] talked about this um specifically but um
[55] for the past several model releases
[57] every time something comes out Notion's
[59] able to incorporate um the new model
[62] within 24 hours. And I think that's a
[63] really good sign of success. If you
[65] can't do that, um, then it means that,
[67] uh, you have some work to do on your
[68] emails.
[71] Um, another sign of success is if a user
[74] complains about something, do you have a
[76] very clear and straightforward path to
[78] take their complaint and add it into
[80] your evals? Um, if you do, then you have
[82] a shot at actually um, incorporating
[85] user feedback, pulling it into your
[87] emails, and ultimately doing it better.
[89] If you don't, then you're going to lose
[90] a lot of valuable information into the
[92] ether. Uh so again I think this is a
[94] really important kind of threshold or
[96] milestone to hit.
[98] Um and the last one which I'm actually
[100] going to talk about a little bit more
[102] throughout the presentation is um you
[104] should really start using evals to play
[106] offense and understand which use cases
[109] you can solve um and how well you can
[111] solve them before you actually ship
[113] things not like unit tests which allow
[115] you to just test for regressions. Um,
[117] and so if you if you really adopt EVELs,
[119] then I think uh before you launch a new
[122] product, you have a really good idea of
[124] how well the product might work given
[126] what your EVLs say.
[130] Um, the second lesson is that great eval
[134] uh they have to be engineered. They
[136] don't just come for free with uh
[138] synthetic data sets and random LLM as a
[141] judge scores that you read about online.
[144] Um, and I think there's maybe two ways
[147] of thinking about this. Um, there's no
[149] data set that is perfectly aligned with
[151] reality. I think in the cases that there
[153] are, there's like basically nothing to
[155] do and the use cases already work, which
[158] there are a few that that are kind of
[159] like that, like solving competition math
[162] problems for example. But for most real
[164] world use cases, any data set that you
[166] can come up with ahead of time is not
[168] going to represent what users are
[169] actually experiencing. And I think um
[172] the best data sets are those that you
[174] can continuously reconcile um as you
[176] actually experience what happens in
[178] reality. And doing that well requires
[180] quite a bit of engineering. Um of course
[182] brain trust can help you with that. But
[184] I think the the point is you have to
[186] think about uh a data set as an
[188] engineering problem not just something
[189] that's given to you.
[191] And the same is true with scorers. I
[193] think um a lot of people we talk to ask
[196] hey what scorers does brain trust come
[198] with and and how can we use those uh so
[200] that we don't need to think about
[201] scoring and we actually have a really uh
[204] powerful um open source library called
[206] auto evals but it's very open- source
[208] and uh uh flexible for a reason which is
[211] that um every company that we work with
[213] that's sufficiently advanced is writing
[215] their own scoring functions um and
[217] modifying them uh constantly and I think
[220] uh one way to think about scores is
[222] they're like a spec or like a PRD for
[225] your AI application. And if you think
[226] about them that way, um, one, it it
[228] actually justifies making an investment
[230] in scoring beyond just using something
[232] off the shelf. And two, hopefully it's
[234] fairly obvious that if you just use, you
[236] know, an open- source or generic scorer,
[239] that's a spec for someone else's
[240] project, not yours.
[245] Um, there's been a real shift towards
[248] context in prompts that's not just the
[250] system prompt that you write. And I
[252] actually think that um just traditional
[254] prompt engineering pe people say this in
[256] different ways, but I think traditional
[258] prompt engineering is evolving quite a
[260] bit and it's very important to think
[261] about context, not just a prompt. Um so
[265] this um is an example of what kind of a
[267] modern prompt looks like for an agent.
[269] Usually you have a system prompt and
[271] then a for loop which you know uh runs
[274] LLM calls uh issues tool calls,
[277] incorporates the tool calls into the
[279] prompt and then iterates and iterates.
[281] Um, and I I actually took a few uh um uh
[285] uh trajectories from agents that that we
[287] see in the wild and summarized these
[289] numbers. And as you can see, a vast
[291] majority of the tokens in the average
[294] prompt um are not from the system
[296] prompt. And so, yes, it's very important
[298] to write a good system prompt and
[300] continue to improve it. But if you're
[301] not very precise about uh how you define
[305] tools and how you define their outputs,
[307] uh then you're leaving a lot on the
[308] table. And I think one of the most
[310] important things we've learned uh
[312] together with some customers is that um
[316] you can't just take tools as a
[318] reflection of your APIs or your product
[321] as it exists today. You have to think
[323] about tools in terms of what the LLM
[325] wants to see um and how you can use you
[329] know exactly what you uh present to the
[331] LLM to make it work really well. And I
[333] think that in most projects um it's
[336] actually very disruptive when you write
[338] good tools. Um it's not something that's
[340] just like an API layer on top of the
[343] stuff that you already have. And the
[344] same is true with their outputs. Um
[346] there's one example that we uh worked on
[348] recently for an internal project where
[352] um shifting the output of a tool from
[354] JSON to YAML actually made a significant
[357] difference. And I know that's a little
[358] bit of a meme in the AI universe, but
[361] it's just so much more token efficient
[363] and easy for an LLM to look at um a YAML
[367] shaped data while doing analysis than
[370] extremely verbose JSON. Um now, if
[372] you're writing code and you're plugging
[374] something into, you know, a charting
[376] library, it makes no difference because
[378] to JavaScript, YAML and JSON are both
[381] structured data. Um but to an LLM,
[383] they're very different. And so I think
[384] you have to be very very thoughtful
[386] about um you know how you actually
[388] construct the definition of a tool and
[390] how you construct its output for the LLM
[392] to maximally benefit from it.
[398] So I think one of the most important
[400] things we've learned um and actually I I
[403] would credit some of the folks at Replet
[405] uh for really uh pioneering this
[407] pattern. Um but you know every time a
[409] new model comes out uh everything might
[412] change. Um and I think you need to
[414] engineer your product, engineer your
[416] team, um engineer your you know mindset
[419] so that when a new model comes out if it
[422] changes everything for you, you can jump
[424] on that opportunity and and ship
[426] something that maybe wasn't possible
[427] before. Um and I'm going to show you
[429] some numbers uh for a product uh feature
[432] that we're actually launching and I'm
[434] going to show you a little bit of it
[435] today. Um, but uh we we've had an eval
[439] for a while that tells us how well this
[441] feature might work and we run it every
[443] few months and you can see you know it
[445] wasn't uh that long ago that GPT40
[449] was the best model out there. Um but but
[452] things have changed uh and you know
[454] progressively uh GPT41 did a little bit
[457] better. Uh 37 sonnet is much better and
[460] and for sonnet is actually even more
[462] remarkably better. Um and uh what what
[465] that's meant for us is that this feature
[467] that um you know at 10% would would
[470] really not be viable for our users to
[472] use suddenly becomes viable. Um and so
[476] you know Cloud 4 sonnet actually came
[477] out two weeks ago. Um and we're shipping
[480] the first version of this feature today
[481] which is just two weeks later. But we
[483] were able to jump on that opportunity
[485] because we ran this eval. Um we were
[488] ready to do it and we we saw that okay
[490] great we've actually finally crossed uh
[492] this threshold. Um so everyone that I
[495] personally work with or talk to I
[497] encourage to create evals that are very
[500] very ambitious and um likely not uh uh
[504] viable with today's models and construct
[506] them in a way that when a new model
[508] comes out you can just plug the new
[510] model in and try it. Um, in Brain Trust,
[513] we have this tool called the Brain Trust
[515] proxy. Um, there's a lot of of similar
[517] tools. You could use ours or you could
[519] use something else. Uh, but really the
[521] point is that you don't need to change
[522] any code to work across model providers.
[525] And so, um, you know, Google just
[527] launched the newest version of of uh,
[529] Gemini. Um, actually Gemini 2.5 Pro0520
[534] scores 1% on this benchmark. Uh, so we
[537] didn't even put it on here. Um, but
[539] maybe the thing they launched today
[540] actually uh does a lot better. We can
[542] find out, you know, with with just a few
[544] keystrokes maybe right after this talk.
[549] Um, and the last thing is it's super
[552] important if you uh think about um
[555] optimizing your prompts to optimize the
[558] entire system. Um so that means uh
[560] thinking holistically about your um AI
[564] system as the data that you use for your
[567] evals, the task which is you know the
[570] prompt, the agentic system, tools etc
[572] and the scoring functions and and every
[575] time you think about making um you know
[577] your your app better you need to think
[580] about improving this overall system. Um
[583] we actually ran a benchmark uh which is
[585] uh the same benchmark that I showed
[587] previously. um it autooptimizes prompts
[591] uh using um an LLM and uh we ran it once
[597] by just giving it the prompt and saying
[598] like hey please optimize the prompt and
[600] a second time giving it the prompt the
[602] data set and the scores and said please
[604] optimize this whole system. Um and you
[606] can see there's a very dramatic
[607] difference. So again um something goes
[610] from unviable to viable. Um, but it's
[614] just super important to optimize the
[616] entire system, not not just the prompt.
[621] And actually, uh, this is, uh, a new
[624] product feature that we are starting to
[626] launch today. Um, if you're a Brain
[627] Trust user, uh, you can go to the
[630] feature flag section of Brain and turn
[632] on a new feature flag called loop. Um
[635] and uh the loop is this amazing cool new
[638] feature that actually autooptimizes
[641] uh your eval um directly within brain
[644] trust. Uh so uh you can work in our
[647] playground and um give it you know a
[650] prompt uh a data set um and some scores
[653] and it can actually create prompts, data
[655] sets and scores too um and just you know
[658] work with it. Uh the kinds of things
[659] that we've seen work really well are
[662] optimize this prompt or uh what am I
[665] missing from this data set that would be
[667] really good to test for this use case?
[669] Um why is my score so low? Um or why is
[673] my score so high? Can you please help me
[675] write a score that is uh you know
[678] harsher than the one that I have right
[679] now? Um you can also try it out with
[681] different models. So, uh, as you could
[684] see from this, uh, we've definitely seen
[686] the best performance with Cloud 4 Sonnet
[689] and Cloud 4 Opus performs a couple of
[691] percentage points better. Um, but we
[693] encourage you to try it out with
[695] different models. You can use 03, you
[697] can use 04 mini, you can use Gemini,
[699] maybe you're building your own uh, LLM
[702] or fine-tune model. You can try that as
[703] well. Um, and yeah, we're very excited
[706] uh, for this. I think uh, I'm going to
[708] talk about this a little bit later. Um,
[710] and I'm happy to do it with some Q&A as
[712] well, but um, I actually I really think
[715] that the workflow around evals is going
[717] to dramatically change now that LLMs are
[720] capable of looking at prompts and
[723] looking at data and actually making um,
[726] you know, constructive improvements
[728] automatically. A lot of the manual labor
[730] that went into iterating with EVELs um,
[733] doesn't need to be there anymore. So,
[734] it's it's really exciting. Uh, we're
[736] excited uh, to ship this and and to
[738] start to get some feedback.
[742] Uh so just to recap um five lessons that
[744] I think are really important. Um
[746] effective eval speak for themselves.
[748] It's it's important to understand
[750] whether you've kind of reached a point
[752] of eval competence in your organization
[754] or not. It's okay if you haven't. Um
[756] it's not easy, but it's important to be
[758] honest about that and work towards it.
[761] Um when you're working on evals, it's
[764] very important to engineer the entire
[765] system. So don't just think about the
[767] prompt. Don't just think about improving
[769] the prompt. Please don't just use
[771] synthetic data or hugging face data
[774] sets. I know they're awesome, but please
[775] use more than just that. Please don't
[778] use off-the-shelf scores only. Write
[780] your own. Think very deliberately about
[783] um how you can craft the spec of what
[785] you're working on into your scoring
[787] functions.
[789] Um think very carefully about context.
[791] And I think in particular um what helps
[793] me personally is to think about writing
[796] tools uh like I would think about
[797] writing a prompt. It's my opportunity to
[800] communicate with an LLM and set it up
[802] for success. And how I define the API
[805] interface of the tool and I define its
[807] output has a very dramatic impact on
[809] that.
[811] Make sure that you're ready for new
[813] models to come out and to just change
[815] everything. Um, so if a if a new model
[818] comes out, you want to be prepared to
[820] know that immediately, ideally the day
[822] that it comes out. Um, and also be
[825] prepared to like rip out everything and
[827] replace it with a fundamentally new
[829] architecture that takes advantage of
[831] that new model. And I think part of that
[833] is obviously having the right eval. Part
[835] of it is engineering your product in a
[838] way that actually allows you to do that.
[840] And then finally when you think about
[842] optimizing or improving uh your eval
[845] performance um you have to think about
[847] optimizing the whole system the data and
[849] how you get that data the task itself um
[853] which you know the prompt tools etc and
[856] the scoring functions
[860] and with that uh we have some time for
[862] Q&A.
[863] >> Yeah there's uh two microphones up here
[866] one on the left side one on the right
[867] side. uh feel free to stand up and ask
[870] your questions.
[877] >> Hi, this is Joti. Um, one of your slides
[880] said take feedback and turn it into an
[882] eval.
[884] Are you concerned about overfitting
[886] evals at that point where every feedback
[888] then turns into an eval?
[890] >> Oh, that's a great question. Um, also
[893] nice to see you. Um so uh the question
[896] was um one of the slides was about
[898] taking feedback uh from you know real
[901] data and adding it to a data set and
[903] incorporating it in an email. Are you
[905] worried about overfitting? Um and I
[907] think the answer is I'm actually way
[909] more worried about overfitting to the
[911] data set without the user's feedback
[913] than I am to um adjusting the fit to
[916] incorporate the user's feedback. Like
[918] the most important thing about a data
[920] set is not the state of the data set at
[923] any point in time. It is how well you
[926] are equipped to reconcile the data set
[928] with the reality that you want. Um and I
[930] actually think one of the things that we
[932] discourage uh in the product and some
[934] people complain to us about this. I get
[936] it uh if you're one of those people. Um
[938] but we don't automatically take user
[940] feedback and add it to data sets right
[942] now. We actually want a human who has
[945] some taste and maybe uh can build some
[948] intuition about the problem to find the
[951] uh data points from users that are
[953] interesting and add them to the data
[954] set. And I think that is your
[956] opportunity as a user to apply some
[958] judgment about like oh okay this user is
[960] trying to do something that should
[961] obviously work. It's really sad that it
[964] doesn't work in my product. Let me add
[965] it to the data set so I can make sure it
[967] does. Excuse me.
[970] You had a slide I think in the tool
[972] descriptions about like with some
[974] percentages on it. Yeah, this one.
[976] >> What what is that?
[978] >> Yeah. So, um we took a few agents um
[982] like we you know have a lot of traces uh
[984] and we analyzed the relative um number
[988] of tokens for different message types.
[990] So the system prompt is one message
[992] type. Tool definitions um are you know
[995] the spec of what uh tools the model can
[998] call. user and assistant um uh are um
[1002] tokens from user and assistant just text
[1005] interactions and then tool responses are
[1008] um tokens from the that you know that
[1011] the tool generates itself.
[1013] >> Oh this is the percentage of tokens
[1015] >> correct and this is the relative
[1016] percentage of those tokens. Yeah. Yeah.
[1019] Yeah. Yeah. So the the the the point
[1021] that we're trying to make here is that
[1023] um I think in modern agentic systems uh
[1027] tools actually like very very
[1029] significantly dominate the token budget
[1032] of the LLM. And I think that it's very
[1035] important to um think about how you
[1037] define the definition of tools and how
[1039] you define their outputs so that you u
[1042] you know engineer the LLM for success.
[1044] uh not just sort of take you know your
[1047] GraphQL API and give it as a bunch of uh
[1049] you know uh tool calls to to the LLM.
[1054] >> Um first off that point about the thumbs
[1057] down is such a good point. I'm working
[1060] with the government and people don't
[1062] like the answer they got for example
[1064] about taxes and they give it a thumbs
[1066] down.
[1066] >> Yeah.
[1067] >> Right. So like adding that human aspect
[1070] is a really good idea. We actually even
[1072] added a little thing that said the
[1074] answer is right, but I just don't like
[1075] it.
[1076] >> That's awesome.
[1077] >> Um, but my question is about your point
[1080] that the new model changes everything.
[1083] We've updated our models several times
[1086] and and use code and open AAI and we
[1089] haven't found huge differences other
[1092] than recently someone really cheap
[1095] wanted to use 4.1 mini and like it
[1098] seemed to ignore every it. I swear it
[1102] ignored the system prop completely.
[1103] >> Yeah.
[1104] >> But what kind of things when you say it
[1106] changes everything, can you tell me a
[1107] little more about what kind of changes
[1109] you're seeing?
[1110] >> For sure. I think um the use case that
[1112] we just shipped with loop is a really
[1114] good example of that. So this is a very
[1116] ambitious uh agent. It's looking at
[1118] prompts and uh data sets and scores and
[1122] automatically optimizing the prompts
[1124] based on the data sets and scores. And
[1127] this is something that um you know we
[1129] wrote a benchmark for a while ago and we
[1132] ran with every consecutive model launch
[1135] and the numbers looked more like what
[1137] you see for GPT40 for a very long time.
[1140] This isn't true for every benchmark. So
[1142] um as part of this exercise we actually
[1144] have a bunch of uh evals that loop
[1147] optimizes. That's our eval set. And
[1150] there's some evals like uh classifying
[1153] taking movie quotes and figuring out
[1155] what movie they're coming from that have
[1156] worked really well since GPT 3.5. Um and
[1160] so there are certain use cases where it
[1161] just doesn't matter. There are other use
[1163] cases where um they're so ambitious that
[1166] they just don't work today. And I think
[1168] you want to create evals uh so that if
[1170] there's something ambitious that you
[1172] want to do in the future, you are very
[1174] well prepared when a new model comes out
[1176] to just push a button and find that out.
[1178] >> Okay. Thank you.
[1184] [Music]
