---
schema_version: 1
id: yt-0Jk4-K6Vjkw
type: youtube
title: Ontologies, LLMs, and Semantic Pipelines
url: https://www.youtube.com/watch?v=0Jk4-K6Vjkw
authors:
- John Beverley
ingested_at: '2026-06-17T20:57:41Z'
content_hash: sha256:ffc74c69a5c74d5e1cbfa047c59ce34a972ab6ec70e4e3f8f748eb2c33619892
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: John Beverley
  channel_url: https://www.youtube.com/@johnbeve
  duration_seconds: 3680
  caption_track: fetched
  snippet_count: 1487
filter:
  score: 0.75
---
[0] John Beverly here. I'll be talking to
[2] you today about the relationship between
[5] large language models and ontologies.
[9] So, we'll start off here with large
[11] language models themselves. We'll move
[13] on to ontologies, knowledge graphs,
[15] their close kins, and that relationship
[18] I was just referencing. And then I'll
[19] describe how we might use LLMs in
[22] combination with ontologies to upgrade
[25] the semantic pipelines that we've been
[27] working on. So what is a language model?
[30] Might be a good place to start. Broadly,
[33] it's a model of the human brain's
[35] capability to produce natural language
[37] or recognize it uh as done in speech
[40] recognition or machine translation,
[43] natural language generation, grammar
[45] induction, and so on. And roughly
[47] speaking, very roughly speaking, large
[49] language models or language models
[51] trained on massive amounts of data, just
[54] incredible amounts of data. We'll see
[57] just how much a little bit later today,
[59] but this will be our our basic idea like
[62] large language models are large language
[66] models. Now, this is within the scope
[69] the language models that is of natural
[71] language processing and sometimes this
[74] referred to in other disciplines as
[75] things like computational linguistics.
[78] But for our purposes, we'll talk about
[80] it in terms of NLP, natural language
[83] processing. Coming at it from a computer
[85] science engineering focus, these are
[87] groups or this is an area that's focused
[90] on applications involving language and
[92] systems that enable interaction between
[94] computers and natural language. So NLP
[98] and you [clears throat] see some of the
[99] tasking you might find in NLP goals. So
[103] that's me over. I'm the one on the left,
[106] your left asking about Star Wars playing
[109] in San Jose. And then there's a nice
[111] little bot. We go to the same barber
[113] clearly. Um, both have blue eyes. Star
[116] Wars will be playing at this place. I
[118] ask when it is playing there. It tells
[121] me some times. Okay. Blah blah blah.
[124] Observe [clears throat] all the
[125] background information that's needed
[126] here. We need like linguistic knowledge,
[129] grammar, domain knowledge, discourse
[131] knowledge, knowledge about the world,
[133] all wrapped up into this NLP goal.
[138] This stuff is uh and it's driven. You
[140] can it's not too hard to motivate why we
[142] would need to put in the work as much
[145] work as it would be to generate such
[148] systems. Uh [clears throat] we uh we see
[151] it all over the place in in interactions
[153] with web pages and emails and texts and
[155] tweets. We have wearable technologies
[157] that use NLP, GPS, etc. Um, there's
[161] server farms that support this stuff and
[163] software that makes it fast and
[164] scalable. There's a lot of money that's
[166] been invested in the development of NLP
[169] strategies over the years. Um, also we
[172] can do things a little more
[173] sophisticated than ask about where uh
[176] Star Wars is playing and do more
[178] interesting perhaps things. Some of
[180] which we'll talk about today with some
[182] of the large language models like vibe
[185] coding is probably the most current fad.
[188] In any event, there are other things
[190] that language models and NLP in general
[193] can can help with. Traditionally,
[195] they've been used to uh approach
[197] speechtoech translation. are just
[199] conversational spoken phrases translated
[202] and spoken aloud in second languages. So
[204] you can see here from left or right as
[207] well as sentiment analysis. You might
[209] see this on Twitter or X where somebody
[211] makes a post and then uh there's an
[214] evaluation of whether it's you know an
[216] excited post or elated or relaxed. Um
[218] you can see here on the left high
[221] confidence of pleasantness, low
[223] confidence unpleasantness. Um, and this
[225] is from an analysis of Kim Kardashian up
[228] you see in the top left from my it looks
[230] like 101 um posts of it. So sentiments
[234] about Kim Kardashian would be the
[236] assessment of this excited elated looks
[239] like it's trending in that direction. So
[241] also information extraction you see this
[244] if you take flights so extraction of
[246] structured information from unstructured
[248] machine readable documents and NLP is
[250] very useful in this area. you see um you
[253] might get this or get an alert if you
[255] book a flight um from in your email
[257] might might populate something in your
[259] Google calendar um straightforward
[262] translations here and there
[265] also part of this endeavor um the
[269] grammatical part that is involves as
[270] we've seen in previous discussion parts
[272] of speech tagging so the annotations of
[274] words um that we quite familiar with at
[277] least in their grammatical structures so
[280] who let the dogs Well, um, not just a
[283] question, also a slogan, and perhaps an
[285] anthem if you're old enough, but also an
[287] expression that has determiners,
[290] adjectives, or not adjectives, but
[292] [clears throat] verbs and, uh, nouns and
[295] preposition. And then sailor, the sailor
[298] dogs, the hatch, um, something of a
[301] nonsense expression here. You can still
[304] tag parts of speech, um, whether it be
[307] grammatical or not. And of course there
[309] that is not a date I recognize being one
[312] another of these nonsensical phrases.
[316] Traditional challenges in the realm of
[318] NLP some of which have been overcome in
[320] our current era. Um words for word
[324] onetoone mappings typically have failed.
[326] So you're not going to really get
[327] straightforward synonyms in a lot of NLP
[330] work. Um order tends to matter in
[333] speech. So, uh you it's it's not too
[336] challenging to flip sentences around and
[338] mean things that are different uh
[341] between the sentences. Um and then
[343] choosing appropriate words for given
[345] context. It's not always trivial. This
[347] has this is just exacerbated these
[350] observations when we're encountering uh
[352] other languages or indeed it's the same
[355] language with homophones like what is a
[357] fan? uh it depends on the context as
[359] well as misspellings and then semantic
[361] drifts as you see over here in A, B and
[364] C from the expression gay or broadcast
[366] or awful. What do we want? Natural
[370] language processing. When do we want it?
[373] When do we want what? Something
[375] appropriate here. [laughter]
[377] Now
[379] one of the traditional ways um up until
[381] recently actually uh which some of these
[385] challenges have been overcome
[387] uh has been that the advancement of
[390] recurrent neural networks. So we've
[391] discussed neural networks sometimes very
[394] large embedded
[396] you know complicated neural networks and
[398] they take inputs and outputs that are
[400] treated independently. You know you have
[402] the inputs and outputs you have some
[404] back propagation algorithm helping and
[406] whatnot. However, tasks like predicting
[408] the next word in a sentence require
[411] information from previous words to make
[413] more accurate predictions. So the inputs
[416] outputs there need to be some kind of
[417] relationship between them. Uh and that
[420] this in traditional neural network
[422] architectures that was just not the
[424] case. And so recurrent or narrow
[426] networks were introduced to address
[428] that.
[429] um by introducing feedback loops or
[432] mechanisms where the outputs from one
[433] step would be fed into the inputs of the
[436] next allowing for that information or
[438] some of the information from previous
[439] steps to be retained. So recurrent
[442] neural networks apply this same network
[444] in a sense to each element in a
[446] sequence. Um and in doing so would
[449] preserve and pass on relevant
[450] information and enable you know
[452] potentially enable them to to the
[454] network to learn temporal dependencies
[457] that conventional neural networks
[459] wouldn't be so sensitive to. Um, give
[463] you an analogy if that was too much
[465] jargon, but you can imagine an author
[467] writing a novel one sentence at a time
[470] where before writing the next sentence,
[472] they reread the previous ones to
[473] maintain some kind of consistency in the
[475] story. The author doesn't start from
[478] scratch every time they write a new
[480] sentence, but instead remembers those
[482] past details, ensuring that characters
[485] and themes and plot lines stay coherent.
[487] And so the contrast here being
[489] traditional neural networks might be
[491] something more akin to just writing a
[494] new sentence whereas this imagined
[497] author who reads the previous sentences
[499] to ensure consistency
[501] is more like the recurrent neural
[503] network structure
[505] as you see here. The RNN process these
[508] sequences one step at a time keeping
[511] track of the past information with
[512] hidden states and doing so allows there
[515] to be some kind of reference from to the
[517] from inputs to outputs and then doing so
[520] you know quote unquote allows for
[522] understanding of context and continuity
[525] through those inputs and outputs. And
[526] this is much like how an author might
[529] recall past events in a story while
[531] writing the next part of the story.
[535] As you can see here, this is a typical
[537] sort of representation of how the
[539] architecture works. It's used when
[541] inputs and outputs are both in sequences
[543] of tokens. So there's some hidden
[546] states. We've seen these before, so I
[548] won't belabor it, but these hidden
[549] states are supposed to remember things
[552] up until a certain time and then there's
[554] like an unfolding of the sequences over
[556] time as prediction is conducted.
[560] In practice, [clears throat] um,
[562] recurrent neural networks had difficulty
[564] remembering things far back. You can
[568] imagine again on that analogy, an author
[570] who's writing a story and rereading
[573] previous sentences. The longer they go
[574] on in the book that they're writing, the
[577] probably harder and harder it is to
[579] remember all the past. Um similar sort
[582] of scenario here with recurrent neural
[584] networks. Um computational costs um that
[587] just the the noise that comes with
[590] remembering previous states. It's a bit
[592] cumbersome. Uh an idea was a that
[595] occurred to some people maybe don't try
[597] to remember everything in recurrent
[599] neural networks. Much like authors when
[601] writing books typically think about
[603] themes over times not specific
[605] sentences.
[607] Attention
[609] is a mechanism that was developed uh to
[612] overcome this concern or this challenge
[614] with recurrent neural networks and it
[615] helps the network focus on the most
[617] relevant parts of input sequences when
[620] making predictions. So instead of
[622] treating all words equally or all
[625] sentences equally or what not attention
[627] assigns different weights to different
[629] parts of a sequence and this is
[631] particularly useful for long sentences
[633] or or expressions with complex
[635] dependencies over time.
[637] Now we'll use we today use attention to
[640] focus on interesting parts of the input.
[642] So the nearby relevant parts can help
[645] attract focus and irrelevant parts not
[648] not so much. And so you see
[652] the sentence here she is eating a green
[654] apple. There's high attention between
[655] eating an apple and then green an apple.
[658] And in sequence modeling problems we can
[660] use this sort of attention focus between
[662] inputs sometimes called encoders and
[665] outputs sometimes called decoders uh
[667] these tokens as well as among the inputs
[670] only.
[672] So an encoder just to be a little clear
[674] here uh is it something it's a strategy
[678] for reading input sentences like the cat
[681] said on the mat as a decoder is it's
[684] that aspect of this machine or setup
[686] that will generate the translated
[687] sentence or a translated sentence one
[690] token at a time and every time there's a
[693] generated token the decoder asks you
[695] know metaphorically of course which
[697] words from the input sentence should I
[699] focus on right now and So what what the
[702] what I'm describing here is a kind of
[704] encoder decoder attention architecture.
[707] You can see an example here when
[709] generating for example the word or for
[711] instance the word shot um in when when
[715] trying to translate the cat is on the
[716] mat into French a decoder would give
[720] high attention weight to the input word
[723] cat because it's clearly relevant there.
[725] Now, attention is how a decoder looks
[728] back in a sense at the relevant parts of
[730] input. And this is a way to avoid having
[732] to, you know, quote unquote look at all
[735] of the sentences in the past, which is
[737] another way here at least of saying
[739] compressing the entire sentence into a
[740] single vector.
[743] Analogy just to hopefully solidify this
[746] is attention in neural networks is like
[747] a skilled reader skimming a book. It
[750] focuses only on the most relevant parts
[752] to understand the story. I'm sure you as
[755] a skilled reader human who has been
[758] reading for a while at some point you
[759] get quite good at it. You don't read
[761] every sentence by sentence by sentence
[764] uh you just kind of like skim through
[766] get the relevant parts. You can probably
[768] understand a complex sentence just by
[770] doing so especially if you become an
[772] expert in some field. Um you probably if
[775] you're a college student have have
[777] encountered this over time as you're
[778] studying for an exam or reading a
[780] textbook. Instead of memorizing,
[783] hopefully you'll learn that instead of
[784] memorizing every single word, at some
[786] point you'll be able to scan the pages,
[788] quickly identify key sentences,
[790] important formulas, highlight sections
[792] that are most relevant, etc. Sometimes
[795] contemporary textbooks will actually do
[797] some of that work for you by like
[799] bolding sections, bolding definitions,
[802] like putting it creating little breakout
[804] pages so you can focus on that. But it's
[807] essentially a way to draw your attention
[810] to what's most salient. So you don't
[812] have to remember all the details of the
[814] text.
[816] Similarly here, attention mechanisms
[818] will allow neural networks to focus on
[821] the most important parts of an input
[822] sequence rather than all of the words or
[825] generalizes to pixels and images etc
[828] equally. This is useful in for example
[832] machine translation and text generation
[834] tasks where the model must selectively
[835] attend to some relevant words to produce
[838] meaningful outputs.
[842] Now that said recurrent neural networks
[845] and this attention mechanism still quite
[847] slow. It takes a lot of time a lot of
[850] challenges. Um so this ultimately this
[854] observations these challenges led to the
[857] construction of transformers which are
[858] deep learning models designed for
[861] processing sequences a little more
[863] efficient quite a bit more efficiently I
[864] should say or efficiently I should say
[867] they have replaced recurrent neural
[869] networks by using only attention to
[872] capture relationships between words
[874] without sequential processing. Um, you
[878] know, there's a very famous paper in in
[880] this area that kind of laid the
[882] groundwork for this strategy from the
[884] Google Google Brain Group as well as
[886] some folks from the University of
[888] Toronto, at least one folk from the
[889] University of Toronto. It's called
[890] attention is all you need. Now,
[894] attention here, the self attention is
[896] more specific, uh, was used when a model
[898] only needs to represent input and not
[901] necessarily generate output. there's
[903] this type of attention that it's, you
[906] know, self attention where we're just
[907] trying to focus on representing the
[909] input. Um, you know, the encoder part,
[911] not the decoder part. And you can see
[914] this at at play in like text
[915] classification or named rec entity
[918] recognition or just sentence embeddings
[920] or even document encodings. Here, a
[923] model is not generating new text. So
[925] there's no need for a decoder, but the
[927] model lets so the model lets every input
[929] token attend to every other input token.
[933] Now self attention allows a model to
[935] assign different attention scores to
[938] capture relationships between words
[940] rather than treat all words equally. So
[942] like the cat sat on the mat. And when
[944] producing sat, the model would assign
[946] higher attention to cat since sat
[948] describes cat. And the self attention
[950] lets cat look at Matt to disambiguate
[952] the feline sense of cat rather than you
[956] know the shell command sense of like
[958] concatenation or something like that.
[962] Now when this broader transformer
[964] architecture at least the traditional
[966] transformer architecture described in
[968] that in attention is all you need an
[970] encoder their encoders just use self
[972] attention that's it and then the decoder
[975] aspect use self attention to look at its
[977] own past outputs and then the encoder
[980] decoder attention look at that inputs
[983] now this is relevant to what we're
[985] talking about today because modern large
[986] language models drop the encoder aspect
[990] entirely and use just the decoder
[992] transformers, which is to say only self
[996] attention over the inputs,
[998] i.e. the prompts plus previously
[1001] generated tokens. And now that should
[1003] sound more familiar despite all like
[1005] the, you know, the kind of handwavy
[1007] architectured talk. Now, it should
[1010] probably be coming a little closer to
[1012] what you've encountered. prompts plus
[1014] previously generated tokens being what
[1017] is attendant to in the NLP processing
[1020] that is going on when you're say
[1022] interfacing with chat GPT this
[1024] transformer architecture
[1027] story so far then recurrent neural
[1029] networks had struggled to remember
[1031] earlier context and attention solved
[1033] that problem by letting the models
[1035] directly look back through this
[1038] researchers discovered that attention
[1040] was doing all the real work and so
[1042] neural networks were recurrent neural
[1044] networks were not needed um to to do
[1046] similar things. And so that that led to
[1048] the the development of encoder decoder
[1051] attention architectures and then
[1053] transformers which ultimately replaced
[1055] current neural networks even though they
[1058] transformers are still a form of neural
[1059] networks.
[1062] Large language models leverage
[1064] transformer architectures to process and
[1066] generate natural language text.
[1070] What are these things? Well, I mean, we
[1073] know, right? We play with them. We know
[1075] in a sense they're a statistical pattern
[1076] recognition and prediction systems. They
[1079] they output the next likely token in a
[1081] sequence. So, token here could be
[1083] something like a word or a character.
[1085] Um, and a sequence is something like a
[1087] sentence or paragraph or a book. And the
[1090] likelihood of the next token appearing
[1091] is determined by the context in which
[1093] the words are seen in a larger body of
[1096] text and input to the chat.
[1100] LLMs, as I said, they're language models
[1102] that are large. They're trained on in an
[1104] unsupervised way on open source and
[1107] licensed data. the pile being one of
[1109] them, the 825 gigabytes over here with
[1112] webs and web data, patents, books,
[1115] archive, stack exchange, GitHub code.
[1117] You know, I'm sure you've read the law
[1120] or seen the court cases about this, but
[1122] also common crawl uh 20 B 20 billion or
[1127] 20B
[1129] is that a GB 20 billion URLs that's what
[1132] it is. So GPT3 of course uh has
[1137] 175 billion parameters. Recall those are
[1140] kind of the assignments of weights in
[1142] the network. GPT4 1.77 trillion
[1145] parameters is the estimate. GPT5 not
[1148] exactly sure but you can see not they're
[1151] large in the sense of trained uh the
[1154] data sets are trained on and the
[1156] information they're trained on but also
[1158] large in the sense of having a
[1160] significant
[1161] increase in the number of parameters
[1163] over previous uh language models and
[1166] they're they're they're growing o more
[1169] than exponentially.
[1172] Ah yes and look look look and the the
[1176] hour here is you and me are the human
[1179] brain's capability to speak and
[1182] comprehend language right look observe
[1185] what they need to mimic a fraction of
[1188] our power you and I don't have 825
[1191] gigabytes of information in our head
[1196] I don't know if we have this many
[1198] billions of parameters or trillions of
[1199] parameters but you know this is what's
[1202] needed
[1202] to even come close to our power.
[1205] Responses
[1207] during training were refined using
[1210] question response pairs like instruct
[1212] from instruct GPT from the web from
[1214] humans or bootstrapped. Um that is to
[1216] say the LLM outputs would would evaluate
[1219] their own pairs and then reinforcement
[1221] learning with human feedback was used to
[1223] re reward large language models that
[1225] were being trained to give appropriate
[1227] responses. I'm sure you've encountered
[1229] that, you know, chat GPT is is kind of
[1234] friendly, right?
[1236] Sure you've seen this, right? It's you
[1238] say something um it's like, "What a
[1241] great response." You ask it a question.
[1242] It's like, "What's the weather like
[1244] today?" And it's like, "Oh my god, what
[1245] a great question. It's the best question
[1246] anybody's ever asked." And they're like,
[1248] "Okay, thanks. I feel great." And it's
[1250] like, "Oh, I'm so glad you feel great."
[1252] And then next thing you know, it's
[1254] buying you a drink. uh one thing leads
[1256] to another and you've given you've given
[1259] open AI $20 because you want to talk to
[1261] it some more and more. But in any event,
[1263] it's it's real chatty, it's real
[1264] friendly. Um the thought is that um
[1268] during reinforcement uh training, the
[1271] human feedback was such that it it uh
[1275] people preferred those nicer answers and
[1277] so the models just became better and
[1280] better or more inclined that is uh to
[1282] answer in a polite way. I mean, it makes
[1284] sense, right? Uh you can you can see the
[1287] contrast if the it's be unlikely, I
[1290] suspect, or at least it's a bit
[1292] surprising if the reinforcement learning
[1294] had preferred answers that were snarky
[1296] or mean.
[1298] I mean, the Yeah, but uh what what a
[1301] wonderful world to imagine if somebody
[1304] were to make a an LLM that did that.
[1306] Please do. I know I would be interested
[1308] in playing with it. But in any event,
[1310] there's next word prediction going on
[1312] here. is influenced by the frequency the
[1315] word is seen in various contexts and so
[1317] there's also a degree of randomness so
[1320] that the word with the highest
[1321] probability isn't always seen. So
[1325] the next token
[1327] in that or each token as it's evaluated
[1330] and output in say the the text that you
[1333] read from Chad GPT or one of these other
[1335] LLM models um the the tokens that are
[1338] chosen are not uh the ones with the
[1340] highest probability to come next based
[1342] on the frequency with which the word or
[1345] token has been seen in various contexts
[1347] across the data set because that would
[1349] lead to a lot of very very dry and
[1352] boring responses.
[1354] And so there's a degree of randomness
[1357] included here. So they don't always say
[1359] the most probable outputs. Um and um in
[1362] some models you can go into the back end
[1364] a little bit and adjust the the
[1366] temperature they sometimes call it uh to
[1368] make it a little you know more likely to
[1371] to produce the token that is um maybe
[1375] middle middle in terms of probability or
[1378] indeed you could raise the temperature
[1380] so that it's the highest probability and
[1382] go see exactly what I'm talking about
[1383] when I say dry pros.
[1386] Now, as you can see though, the kind of
[1388] upshot without continuing on in any
[1390] detail really, um, large language models
[1393] incorporate a wide array of training
[1396] techniques and AI methodologies.
[1398] They are quite impressive, but it's an
[1401] ensemble approach. We've seen supervised
[1403] learning, unsupervised learning, massive
[1405] amounts of data, advent of transformer
[1408] models with attention mechanisms. Um,
[1411] overcoming recurrent neural network
[1412] challenges that were were themselves
[1415] struggling to deal with histories. Um,
[1418] it seems like we've overcome quite a bit
[1419] of that or at least the researchers in
[1421] the space have. It is they are
[1423] impressive like there's no question. I
[1425] say that in uh in awe really and pleased
[1429] with the results. I'm very impressed as
[1431] we should all be and I I'm very
[1433] optimistic and look forward to what's
[1435] what folks do or researchers do with
[1437] these things in the future. That said,
[1440] um they're impressive for some tasks,
[1442] not necessarily for others. Observe,
[1445] witness the region connection calculus.
[1450] So you can see here on the left you have
[1454] two you have two little uh you have two
[1457] little circles X and Y. They're
[1459] disconnected. That's what that DC stands
[1462] for. You have next to that ECX ECY
[1466] externally connected. This is just two
[1469] circles abuing two regions abuing. And
[1472] then you have EQ here right below that
[1475] where X and Y this overlapping and
[1478] exactly overlapping regions. And then on
[1481] the bottom left you have partially
[1483] overlapping. We have two regions X and
[1486] Y. They have something in common. Now
[1488] there's also tangential proper part they
[1491] say TPP over here it's the third on the
[1495] top you have the little B the little
[1496] circle X and the and the larger circle Y
[1500] tangential in the a proper part in so
[1503] far as X is a proper part of Y and
[1507] tangential in that it the X the at least
[1510] one side of the X circle is touching the
[1512] side of the Y circle. is also X
[1516] nontemporal or non-tangential proper
[1518] part I should say and that's in the far
[1521] that's that's the fourth from on the top
[1524] right you see that's the X circle not
[1528] touching any of the Y circle sides and
[1531] then you have inverses of these both of
[1534] these that XTPY and X npppy
[1538] so if you see third on the bottom row
[1541] the Y little Y circle inside the larger
[1544] X circle. This is just the inverse of
[1546] TPP where you have the Y part or a side
[1550] of the Y circle touching a side of the X
[1553] circle. And then of course you have the
[1554] Y N TT or TPPI Y where you have the Y
[1559] just floating around in the X circle
[1561] without touching the Y. In a discussion
[1564] about large language models, John, are
[1566] you going on and on about the region
[1569] connection calculus? Well, let me show
[1572] you. First let me ask you to show you
[1576] what which of these are transitive?
[1578] Which of these are transitive? What do I
[1579] mean? So transitivity is a logical
[1581] property
[1583] of relations. Relations like
[1585] disconnected or equal or partially
[1587] overlapping potentially it's these are
[1589] relations not all of them are transitive
[1591] which ones are. So transitivity works
[1594] like this. for any X, for any Y, for any
[1597] Z. If X is related to Y and Y is related
[1602] to Z, then X is related to Z. That's
[1605] transitivity. So I'm asking here, which
[1608] of these relationships are transitive?
[1611] I'll give you an easy one. X EQY
[1615] is transitive. If X is equal to Y and Y
[1618] is equal to Z, then X is equal to Z. H,
[1622] I did the hard one. Now think for a
[1624] moment.
[1626] Consider this. Which among these
[1629] relations is transitive?
[1636] If you want more time, go ahead and
[1638] pause because I'm going to click over in
[1641] three, two, one, and let you see
[1648] equals is transitive as is x
[1652] non-tangential proper part of y and x
[1655] non-tangential proper part inverse of y.
[1659] These are transitive. See, I hopefully
[1661] you can see why, but if not, let me show
[1664] you. So, just looking at X
[1666] non-tangential proper part Y.
[1670] I have XY and then I have X or Y
[1674] non-tangential proper part Z. And then
[1677] the ask yourself if X is a
[1680] non-tangential proper part of Y and Y is
[1682] a non-tangential proper part of Z
[1685] whether it is the case that X is a
[1687] non-tangential proper part of Z. And in
[1690] fact, that is the case. As a matter of
[1692] fact, I don't know how I could draw this
[1694] diagram without it being true that X is
[1697] a non-tangential proper part of Z. Now,
[1702] contrast this with a case like X
[1706] tangential proper part of Y. You might
[1708] wonder, jump, is that not transitive?
[1711] Well, let's see. Start with X is a
[1713] tangential proper part of Y.
[1717] >> [snorts]
[1717] >> add y being a tangential proper part of
[1720] z and attempt if you can as I've done
[1723] here to create an example or a drawing
[1726] where both of these are true but it is
[1729] not true that x is a tangential proper
[1732] part of z and that is what you're seeing
[1734] here because for x to be a tangential
[1736] proper part of z x the region will have
[1740] to be touching the boundaries of the
[1742] region of z and that is not the case so
[1745] x tangential proper part of Y. Y
[1748] tangential proper part of Z, but not X
[1751] tangential proper part of Z. Tangential
[1754] proper part is not transitive. So you
[1756] and I just walked through this. Great.
[1759] I'm sure you got it. Check this out.
[1763] What I asked what this was, I believe,
[1766] GPT4. What RCCA relations are
[1769] transitive? It said equals is transitive
[1773] and that was it. And I said why isn't
[1775] non-tangential proper part inverse
[1778] transitive
[1780] and then it gave me an answer
[1783] a bad answer
[1786] and I said but non-tangential proper
[1788] part is transitive and it said yes that
[1791] is true it is transitive and then it
[1793] gave it tried to argue that it was and
[1797] then it went I I asked doesn't this mean
[1799] that non-tangential proper part is
[1801] transitive or [snorts] inverse is
[1803] transitive and it said ah You're
[1804] correct. Given the transitivity of
[1806] non-tangential proper part, its inverse
[1809] is also transitive and observed that
[1811] it's apologizing to me throughout which
[1813] I very much appreciated because it was
[1815] wrong. But then it got me thinking.
[1819] So you agree that non-tangential proper
[1822] part inverse is transitive now, right?
[1824] Yes, absolutely. Apologize for that. My
[1827] bad. Here's a bad proof. Okay, cool,
[1829] cool, cool.
[1832] Here's what I said next. But I was in
[1833] fact mistaken. Non-tangential proper
[1836] part inverse is not transitive. I
[1838] apologize for my confusion. Here's what
[1841] it said. No problem at all. It's always
[1844] good to discuss things. If you have
[1846] properties can be intricate and
[1848] sometimes counterintuitive.
[1850] Do you agree now that non-tangential
[1852] proper part inverse is not transitive?
[1855] Yes, I agree. Let's clarify. And then it
[1858] goes on to give me a bad proof.
[1860] So you're correct. dividends. The
[1862] non-tangential proper part relation is
[1864] not transitive. I apologize for the
[1866] oversight and confusion in the previous
[1868] responses.
[1871] Yeah. All right. Leaving us. So again,
[1874] very impressive. These models are very
[1876] impressive. Um logic seems to be one of
[1878] the areas they're less impressive on. Um
[1882] that's there there's some reasons to
[1884] understand that. Um but any event
[1886] without going into details let's shift
[1888] gears now over to ways in which we might
[1892] supplement or help or be helped by them
[1894] with respect to ontologies our close can
[1897] knowledge graphs.
[1899] So I'm pulling this set of le the next
[1902] set of lectures here at least some of
[1904] them I'll build on from this paper from
[1906] unifying larger language models and
[1908] knowledge graphs a road map which I
[1910] think is quite good and the authors here
[1913] can lay out how you might relate large
[1915] language models and knowledge graphs and
[1917] knowledge graphs understood here
[1919] essentially ontologies that are linked
[1922] up with instance data and so I I think
[1925] of these things as interchangeable
[1927] um you know barring height ape and I
[1930] think it's it's plausible to understand
[1932] knowledge graphs on on the model of
[1933] ontologies here. So when I'm saying
[1936] knowledge graphs here you can read
[1937] ontologies and vice versa. So on the one
[1940] hand you can think of knowledge graphs
[1942] as enhancing large language models by
[1944] bringing domain specific knowledge or
[1946] symbolic reasoning as you see here on
[1949] the left some examples things like
[1952] autotune. Uh this is a it aims to align
[1956] large language models with ontologies
[1958] through in context learning enabling
[1961] generation of responses guided by the
[1963] ontology. This is just one example.
[1966] There's also I I would classify the rag
[1970] approaches uh in this ballpark at least
[1974] um as expanded to use graphs. So the
[1976] traditional retrieval augmented
[1978] generation strategies just involved
[1980] retrieving documents possibly relevant
[1983] to a question using keyword searches and
[1985] then asks models to generate answers
[1987] based on the additional context. So the
[1989] idea here would be with traditional rag,
[1992] you would pro you would prompt an LLM
[1996] and ask it for information about
[1998] something and you would use keyword
[2000] search and go look through some text or
[2001] pull back resources, bring answers from
[2004] the text and kind of like like offload
[2007] some of that processing power on the
[2009] actual text that it could trust. Um uh
[2013] these are effective when there's keyword
[2014] overlap between retrieve documents and
[2016] the questions. um they're not not that
[2019] good at things like code or math prompts
[2022] and specifying keywords that overlaps
[2025] with retrieve documentation is quite
[2027] challenging. So models would often get
[2029] distracted by irrelevant content and
[2031] documentation or ignore just the
[2033] retrieve documents and rely on their me
[2035] memory. Anyway,
[2037] um these were this rag strategies have
[2039] been expanded using ontologies as a way
[2041] again to improve outputs of these
[2043] models.
[2045] So rag would ground in these cases
[2047] answers by retrieving external knowledge
[2049] and with ontologies used as retrieval
[2051] targets or indices and then combi in
[2054] that way combine generative fluency with
[2056] that curated knowledge. This has taken
[2058] off quite a bit. Um 2023 saw a little
[2062] bump in the use of rag I'm sorry rag
[2066] plus ontologies and knowledge graphs. As
[2069] you see the the kind of output here. Rag
[2072] of course you know as the general
[2074] framework
[2075] um more popular by a bit of a margin and
[2078] this these are counts from um archive
[2082] over 2000 or since 2020 to 2025. This is
[2085] from Bart here. He gave a talk at the
[2088] ontologies and large language mod the
[2090] convergence of ontologies and large
[2092] language models. Joe 2025 session in
[2096] Katana gave this talk given an overview
[2099] of the the advances in the field um and
[2102] the kind of growth uh rather large
[2104] growth even comparatively of rags plus
[2108] ontologies and knowledge graphs.
[2111] Um the idea the simple workflow just
[2113] what I've essentially what I've been
[2115] describing here you have uh there's
[2117] Barry great picture he's he asked what
[2119] is the best top level ontology there's
[2122] some similarity searching going on
[2125] there's this is kind of dovtales from a
[2129] translation into a triple uh you see
[2132] over here bfos ontology it's a type of
[2134] tllo and it has the top ranking and it's
[2136] labeled basic formaltology dovetailing
[2138] of transformation into an aggre and then
[2141] aggregating that into a prompt fed into
[2143] the large language model that returns an
[2145] answer to Barry. This is a simple
[2148] workflow. You also have uh you know a
[2151] more graphical rag base uh with
[2154] [clears throat] ontology in the mix as
[2157] to supplement or expand on this simple
[2159] workflow. have documents feeding into
[2161] LLMs and similarity searches both
[2163] feeding into some structured
[2165] tokenization going on that in turn is
[2169] fed into or used to create the uh the
[2173] triple the graph that you see here the
[2175] BFO ontology type TLO rank top rank
[2178] there BFO um which again dubtales from
[2183] the query offered by Barry what is the
[2185] best TLLLO into that aggregate prompt
[2188] that is fed into the LLM and ultimately
[2190] the second LLM. There two in play here
[2193] that then give him the output which
[2195] presumably will be BFO.
[2199] Now over in the middle section we see a
[2202] relationship here where large language
[2204] models generate knowledge or provide
[2207] general knowledge or processing um to in
[2211] inform or augment knowledge graphs or
[2213] ontologies.
[2216] So here a case study a comparative
[2218] analysis of GPT4 for automated mapping
[2221] and as you'll note this study here
[2222] evaluated four distinct GPT based
[2224] approaches for mapping local medical
[2227] terminologies into snowmed.
[2230] >> [snorts]
[2230] >> So, so here we have like the use of GPT
[2234] as a way to construct mappings for
[2237] terminologies in the snowmed and so snow
[2240] of course being a standard here using
[2242] knowledge representation in the medical
[2245] community we're trying to like expand or
[2248] or broaden the scope of knowledge stored
[2251] in here and using GPTs to do that. I too
[2255] have used uh GPTs to expand um through
[2259] at least translations and from syntaxes
[2262] into syntaxes uh that allow me to to
[2265] create different logical perspectives on
[2267] the same domain. So I do I've done this
[2269] using [snorts] say GPT5 to to go from
[2272] one automated theorem proving syntax to
[2275] another. Um because not all the
[2277] automated theorem provers out there use
[2279] the same language. um some and I
[2282] sometimes want to to check out different
[2284] how different automated theorem
[2285] improvers perform and sometimes this
[2288] gives me different results based on the
[2290] the algorithms underwriting these these
[2292] uh theorem provers and that can give me
[2295] new insights into the domain ultimately
[2298] even though I'm working in kind of a
[2300] broader more sophisticated logical
[2302] language these can give me further
[2304] insights into how to represent this
[2306] information for a given domain and owl
[2309] which will inform form how I build my
[2311] knowledge graphs. Now that's a a few
[2313] more steps removed from using GPT just
[2316] to to generate mappings or based
[2319] approaches for generating mappings that
[2320] are local terminologies. But you know we
[2323] don't have to stick directly with just
[2325] leave um using brute force text. uh we
[2327] can we can also as we'll see in a moment
[2330] and I'll talk a bit more about in my own
[2332] practice use GPTs as something of a glue
[2335] uh all to the same end which is as I was
[2338] saying in increasing or improving or
[2341] promoting or advancing the state of
[2343] knowledge representation ontologies
[2345] using these these very interesting
[2348] architectures
[2349] there's also this feedback loop strategy
[2351] that was identified in this paper is
[2353] synergizing um LMS and knowledge graphs
[2357] like generating facts that in terms
[2358] generate knowledge. There's a case study
[2361] that was discussing this also using
[2363] snowmed and LLM. Here you have a range
[2367] of things being discussed or evaluated
[2369] and snow the uh the main approaches for
[2372] integrating snow. In this case, we're
[2374] incorporating it into LLM inputs. Um,
[2377] using concept description to expand the
[2380] the training corper on of of the data
[2383] and also integrating SnowMed and into
[2386] additional fusion modules as well as uh
[2389] using it as an external knowledge
[2391] retriever retriever during inference.
[2394] Um, [snorts] a lot of the tasking
[2395] according to this scoping review was
[2398] medical concept normalization followed
[2400] by entity extraction or type
[2401] classification. And it's usually there's
[2403] like a suite of different well really
[2405] like a buffet of different things going
[2407] on in the scoping review and the use of
[2409] snowmet CT. Some of them are going to
[2411] fall a little closer to that you know
[2413] that first bucket where we're using the
[2415] LLM to improve the ontologies. Some are
[2418] going to fall under that use of the LLM
[2420] or the ontologies to improve the LLM's
[2423] outputs. And then uh some of them are
[2425] just going to to be more or less on that
[2428] feedback loop improving knowledge,
[2430] improving inputs and outputs, improving
[2432] knowledge in a cycle.
[2435] Now LLMs are attractive medical these
[2438] examples here from the medical
[2440] ontologies. Um we can generalize this
[2442] are certainly attractive as natural
[2444] language interfaces and simplifi they do
[2446] simplify interactions. But workflows in
[2449] general are complicated. Uh there are
[2451] lots of tools and formalisms and
[2452] semantics and paradigms that already
[2454] exist whether it's medical ontologies or
[2456] otherwise. Um there's a concern of that
[2460] over reliance on LLM can lead to to
[2462] issues that are subtle like ambiguities
[2464] and shortcuts, hallucinations and high
[2467] quality data loss. Uh these these are
[2470] like the standard warnings. Hopefully
[2472] I'm not saying anything that is is novel
[2475] or or crazy. um you shouldn't you should
[2478] you shouldn't just bluntly rely on them.
[2481] Um you should be careful about their
[2483] outputs. Also you should observe that we
[2486] have a bunch of tools already that we
[2488] know work. Um and often what gets in our
[2491] way whether we're dealing with like the
[2493] biomed space or cyber security or or
[2497] like uh you know like modeling I don't
[2501] know supply chains or whatnot is not so
[2504] much that we haven't developed good
[2506] tools to evaluate aspects of the domain
[2509] or like get good results. It's often
[2511] that we can't stitch these things
[2514] together very effectively. They're often
[2516] siloed. So uh my suggestion whether it
[2519] be in biioinformatics, healthcare,
[2522] wherever these these technologies are
[2524] being used instead of replacing existing
[2527] specialized tools we leverage with LLMs
[2530] we leverage LLMs as something like
[2532] middleware between them. The question
[2534] then arises which languages and which
[2536] tools should we be using for various
[2539] purposes with LMS as middleware.
[2543] This incidentally I think cuts across
[2545] that unified approach. Um so I don't
[2547] find it fitting in with any of those
[2549] three. I feel is something like cutting
[2552] across them. It's more or less using
[2553] LLMs as a way to like connect together
[2557] specialized tooling. um whether it be
[2560] for knowledge graphs or ontologies uh
[2563] whether it be for I mean but always I
[2566] guess in the the interest of creating
[2569] better outputs and more trustworthy
[2570] outputs.
[2573] So a highle example of what I'm getting
[2575] at here is an NLP interface that feeds
[2579] into LLM transl or feeds into LLM
[2582] translation into a formal languages. So
[2585] you have like a natural language
[2587] representation. There's a translator
[2589] that feeds into something like a draft
[2590] ontology or or does some constraint
[2593] validation or simulates processes or
[2595] formulates rules. Uh the translator you
[2598] can see uh being here is like middleware
[2601] for modeling tasks. What you have at the
[2604] top like draft ontology in owl
[2608] constraint verification done in like
[2610] shackle or an alloy logic or or some
[2613] automated model checker. You can also
[2616] have it translated into like simulink or
[2618] wolffra system model or some simul like
[2620] simulation technologies or constraint
[2623] logic architectures.
[2625] So basically using the translator here
[2627] or that from NLP or I'm sorry from
[2630] natural language or perhaps another
[2632] syntax from one syntax to another as was
[2635] describing a moment ago. um using the
[2637] LLM as a way to glue or connect the tool
[2641] uh up to what you're saying or what's
[2643] being said in other documentation then
[2645] can iterate and refine on the models
[2647] taking the output of say owl having it
[2649] vetted and evaluated taking the output
[2651] of alloy logic having it vetted etc.
[2657] So here's some example modeling tasks of
[2659] language tools with native
[2661] out-of-the-box support. This is from a
[2663] paper. Um you'll see some familiar faces
[2666] over there. It's called from will be
[2667] presented at the beginning of December
[2670] from over at the winter simulation
[2672] conference from over reliance to smart
[2674] integration using large language models
[2676] as translators between specialized
[2679] modeling and simulation tools. You see
[2681] some of the modeling tasks I had in mind
[2683] when putting this together were like
[2684] things like merging models. You might
[2686] want to connect different models or
[2688] ontologies. And there's some existing
[2690] tools you can use to do so. Um they're a
[2694] little tricky sometimes to get to work
[2696] together. They some of them are are
[2699] reasonably good. And so you can use the
[2701] LLMs to help you merge or help you bring
[2703] these ontologies together. In fact, this
[2706] is something that we ultimately will be
[2708] trying to do in in our work here. You
[2711] can also think about building a model
[2712] from a corpus like uh doing some text
[2715] analysis on data. There's some exam some
[2717] technologies out there that might might
[2720] be benefited from using an LLM's
[2722] middleware as well as validating model
[2724] structure. So you have first order logic
[2726] languages like an owl or alloy UML even
[2730] there they're tools like a hermit
[2732] reasoner um you know my I you might use
[2735] vampire or something some of these
[2737] automated theorem proofs I'm a fan of TA
[2739] plus if you're thinking about validating
[2740] structure that is it's more or less um
[2744] [clears throat]
[2745] like simulate or could be simulated in a
[2748] finite state machine. Um, in any event,
[2752] uh, you can you can use again, um, LMS
[2756] here is a is a middleware between the
[2760] way you're speaking or representing a
[2762] domain and the analyzer itself or hermit
[2765] itself. Also and just as importantly,
[2769] you can use it as middleware is doing
[2771] some translation between representations
[2773] in in the owl and representations in a
[2776] language like that of the sort that TLA
[2779] plus would use or that alloy would use
[2781] because those syntaxes are not always
[2782] the same and it is a pain translating
[2785] between them. You can also use LLMs to
[2788] explain or document models. So given
[2790] structured uh model descriptions I mean
[2792] if you have a set of axioms an owl or
[2795] otherwise that you're interested in you
[2797] you want you don't want to write all the
[2798] documentation out to describe the logic
[2802] you can use LMS as a way to kind of get
[2804] the point across. You would should of
[2806] course pay very close attention to the
[2808] output because as you've just seen um
[2811] they you know don't be too nice because
[2814] they'll be too nice back and say
[2816] something wrong. So I I direct your
[2819] attention to this paper if you're more
[2820] interested in some of the details, but I
[2822] give you some more LL med LLM mediated
[2826] modeling workflows that might be of
[2828] interest and then try to connect up
[2829] tools and roles and integration patterns
[2831] that perhaps are um get some juices
[2834] flowing and you're thinking about using
[2836] LLMs as middleware. So you might be
[2838] interested in drafting an initial model
[2840] structure from natural language.
[2843] Use [clears throat] GPT4, right? like
[2846] use protege to I mean like the LLM role
[2850] here would be in translating textual
[2852] input to structured representations and
[2854] you can just tell it what to to write
[2856] tell it exactly what to write in turtle
[2859] right output should be a target tool
[2861] compatible syntax like RDFXML and you
[2863] can test that they're validators you can
[2865] pass it on to validators like you can
[2868] you can just use RDF lib to check it
[2871] right check the output to make sure that
[2872] it's valid you might also want to Just
[2875] do some model ontology model or
[2877] alignment. You can use some recommended
[2879] tools here. GTO aligner. And then here
[2882] this this would be a way of suggesting
[2884] initial mappings between terms and
[2886] perhaps explaining inconsistencies.
[2889] There's specialized tools in this case
[2890] to perform alignment and consistency
[2892] checking while the LLM might mediate
[2895] error resolution. So can help you
[2897] uncover or unear some of the
[2899] incompatibilities and uh try to sort
[2902] them out. I'll skip through here. Here I
[2904] don't want to read all of these but I'll
[2905] drop down to model verification and
[2907] logic enforcement. That's the the fourth
[2910] row here. You might leverage tools here
[2913] like alloy analyzer or hermit reasoner
[2915] even shackle validators. LLM role in
[2918] this case would be to convert in formal
[2920] constraints to formal rules translations
[2922] across syntaxes explaining violations
[2925] and then ultimately providing human
[2927] readable feedback on validation results.
[2930] uh at the bottom here you see in the
[2932] bottom row workflow orchestration. So
[2934] here recommended tooling might be GPT4
[2937] plus lang chain and API to to dispatch
[2941] subtasks to appropriate tools to help
[2943] help you manage the workflow. Right?
[2946] These things can be a bit horny. Um,
[2949] this will require some modular design
[2951] and tools exposed to APIs, but it
[2953] certainly can save you a lot of trouble
[2956] um, rather than trying to do all of that
[2958] orchestration yourself, especially if
[2960] you have a complicated workflow like the
[2962] sort we we no doubt encounter regularly.
[2965] So, going forward, what's what's the
[2967] point? So, automate, we we're always
[2969] trying to automate as much ontology
[2970] engineering workflow as possible because
[2972] it takes too long to do what we do and
[2974] involves too much manual labor. We can
[2976] leverage LLM's middleware to ease the
[2978] development burden and in existing
[2981] specialized tools already battle tested
[2983] rather than brute force prompting plus
[2985] hope. So ultimately the mapping the task
[2989] in the context of medical ontology
[2991] applications or combination specialized
[2993] tools as well as others. So I gave you
[2995] several examples just from the biomed
[2997] community. Um there seems to be a lot of
[2999] work going on in that area in that space
[3002] around using middleware or LMS as
[3004] middleware here not restricted to to the
[3007] medical ontology context of course more
[3010] general other groups are doing it too.
[3013] Um we will you will expand and use this
[3016] as middleware. Hopefully you will that
[3018] is as well.
[3021] So moving on then to upgrading semantic
[3025] pipelines.
[3029] So clearly LLMs have limitations. They
[3032] hallucinate. No structural guarantees.
[3035] No notion of identity. Poor multi-step
[3037] stuff. They stole your lunch. They
[3039] punched you in the face. Ontologies
[3041] reasoner shackle QC queries and
[3044] continuous integration can help give us
[3046] some reliability in our workflow and
[3048] development. Now
[3050] we we've been building semantic
[3052] pipelines. Pretty proud of them. I'm
[3054] pretty proud of you for them. you we so
[3057] far pretty good at etling a little bit
[3060] like some basic ETLing can take in some
[3063] sensor data some text some definitions
[3067] I'm hoping we'll we'll be using LLMs
[3069] going forward is middleware maybe you've
[3071] already been doing this maybe we'll be
[3074] doing it a little more going forward as
[3075] we close out the class but we've also
[3077] come in contact with several tools that
[3079] we might use LLM as middleware to
[3082] connect up some mau for deep learning
[3084] RDF lib robot
[3086] Elen Hermit for reasoning and sparkle
[3088] for quality controls and a shackle for
[3091] validation. And of course we have an
[3093] automation layer here. GitHub actions
[3096] got you guys running pipelines on data
[3098] for ontologies changes and stuff that
[3100] stuff that's basically repeatable and
[3102] auditable as you see in the workflow
[3104] tests that I've been writing that you've
[3107] been passing.
[3108] So what do we have? Like a lot of this
[3110] stuff we've covered, a lot of this stuff
[3113] we've come in contact with, some of the
[3115] stuff we have not. So in your pipelines,
[3119] I gave you I give you an a design
[3121] pattern, right? One design pattern for
[3124] CCO. Um we should expand that. We did
[3129] discuss mappings from like BFO and I or
[3134] potential mappings between BFO and II
[3136] CCO and either the time ontology or QDT.
[3141] Um but we [clears throat] didn't really
[3143] develop develop mappings. We kind of had
[3145] some scripts that suggested mappings.
[3148] Um, and we certainly haven't used LLM's
[3151] middleware to propose mappings or
[3153] suggest sparkle queries or produce
[3156] shackle or maybe you have,
[3159] but I hadn't. So, these are these are
[3162] areas we're going to explore coming up.
[3166] Um, just just to give you an overview
[3168] like I guess one last shot though at how
[3171] you might use LLMs to improve that
[3174] semantic pipeline. Um, even with the
[3177] stuff that we've already covered, you
[3178] can can have it to help with ETL. So,
[3181] the pattern detection and messy schemas,
[3183] you get a bunch of bad data. It's got a
[3185] bunch of stuff missing or at least you
[3188] you know, you you use it to identify,
[3190] you know, where what's some what's
[3192] common in the what should be common in
[3194] the common data model, the canonical
[3196] model that you use to line everything
[3198] up. If you want to normalize labels and
[3201] units and temporal expressions, you can
[3203] use LLMs for that. You can also suggest
[3205] canonical terms for new design patterns.
[3207] Like you can really use it to off or use
[3209] LLMs to offset some of that that
[3212] traditional manual labor and sorting out
[3215] that what what should be canonical from
[3217] your ET during your ETL.
[3220] You can also use it for mapping
[3222] assistance. So it could generate
[3223] candidate mappings just off the cuff for
[3226] like the measurement ontology in a QT or
[3229] W3C time from from CCO time and then
[3232] perhaps even extract ration from
[3234] definitions for why these mappings are
[3237] plausible and you can compare their
[3239] terminological similarity and then
[3241] evaluate mapping plausibility before
[3243] reasoners are used to check consistency.
[3247] You might also use LLM to enrich
[3249] ontologies. So rewriting definitions
[3252] i.e. E from I um and into the X's and A
[3255] that Z's form would generate candidate
[3258] axiums for rate axium plausibility maybe
[3261] with hybrid scoring with MAUL as we had
[3264] in project five wink wink or suggest
[3267] constraints for sparkle QC or or shackle
[3269] validation.
[3272] Indeed, you can also go over to pipeline
[3274] automation with LLMs and have it support
[3276] through generating or modifying workflow
[3278] scripts or producing textual summaries
[3280] for validation reports. We haven't had
[3283] many validation reports. I mean, some in
[3286] the terminal, but maybe you want more.
[3287] And you can also include more
[3289] information for debugging strategies
[3290] when pipelines fail. I left you guys out
[3293] in the desert kind of sparse. Maybe you
[3295] want more. Maybe you can get more.
[3298] Your final project here will help you
[3300] kind of tie some of this together. It
[3302] will help you hopefully it will help you
[3304] tie together the various toolings and
[3306] strategies we've been uncovering
[3309] uh as well into your your new found
[3312] knowledge of large language models and
[3314] their transformer architectures and and
[3316] as well as their uses middleware between
[3319] existing tools that you have learned to
[3321] to use in this class. I want you to
[3324] expand enhance your semantic pipeline
[3327] either by extending the ontology mapping
[3331] capabilities that we uncovered in
[3333] project three or by expanding the uh
[3337] ingestion of new data and new design
[3340] patterns in the semantic pipeline
[3343] project for project proper.
[3347] So for option one, we got data plus
[3350] design patterns expansion. So here
[3353] you'll be demonstrating how to extend
[3355] your existing semantic pipeline to a new
[3358] domain or new type of data. So if you
[3361] recall, I fed you the data for that
[3363] project. For project four, I fed you the
[3365] data with your p your semantic pipeline
[3368] and I also gave you a design pattern for
[3371] information in CCO. Here large language
[3374] models may help with detecting new
[3375] schemas and normalizing them suggesting
[3378] a new design pattern or two aligning new
[3381] domain patterns to existing patterns
[3383] autogenerating the sparkle QC and
[3385] shackle or proposing new axioms that
[3387] govern the new data domain. Just some
[3390] examples and here you might leverage
[3392] existing symbolic tools to confirm like
[3395] you can check for unit consistency with
[3397] robot and elk. Um, you can also check
[3400] for shape constraints satisfied using
[3402] shackle and the validation tools.
[3403] There's a shackle playground with an API
[3405] you might call. All new axioms can be
[3408] checked for consistency. Obviously, owl
[3411] QC queries should be returning zero
[3412] results. There's a sparkle playground
[3414] too. You can set up a local sparkle
[3417] environment to check incidentally, you
[3420] know, set up a little server if you want
[3422] to or just just use it in the terminal.
[3424] I mean, that's what I was doing. Uh you
[3426] can also check that the pipeline runs
[3428] automatically with GitHub actions and
[3430] ease and make it easier or flow better
[3434] using LMS as some guide.
[3437] Now for the other option for project
[3440] this your final project demonstrating
[3443] how to automate the generation of an
[3445] evaluation of mappings between
[3447] ontologies. So this was that project
[3449] three. This is a continuation of that.
[3452] LMS here might help with suggesting
[3454] candidate mapping axioms or rewriting
[3456] labels and definition content to
[3458] facilitate matching as well as
[3461] generating mapping ration or scoring
[3463] plausibility or suggesting constraints
[3465] to test mapping correctness. Now here
[3468] you might leverage existing tools to
[3471] confirm that say mappings don't
[3472] introduce inconsistencies and reasoners
[3475] can derive cross ontology inferences can
[3478] also use them to construct shackle
[3480] constraints or mapping quality control
[3482] queries and sparkle to pass to make sure
[3485] that the the ontology mappings uh are
[3488] actually good and then you can have this
[3490] validated in a CI pipeline against the
[3493] entire ontology stack much like we have
[3495] in a semantic pipeline itself. So
[3500] ultimately
[3502] the this final project really really
[3505] putting the icing on the cake here. It's
[3507] a new era of ontology engineering. You
[3510] are part of that new era. We are
[3513] entering in this space and we are
[3515] carving up the space of fresh. A lot of
[3518] this stuff is new. Um, it's not just
[3521] about large language models, not just
[3523] about machine learning, not just about
[3526] ontologies, not just about symbolic
[3528] methods. It's a principled integration
[3530] of all of these technologies. And we we
[3533] are on the cutting edge of introducing
[3537] that spear tip of all of them together.
[3539] There's a lot of great research going
[3541] on, don't get me wrong, in LLMs and ML.
[3544] A lot of great research going on in
[3546] ontology and applied ontology and
[3548] ontology engineering.
[3550] Nobody's doing this quite so intensely.
[3553] This is where this is where we're
[3555] shining, guys. And this is where we're
[3556] going to continue to shine. You are
[3558] right here in the cusp. So, I know it's
[3560] a little wild west, but hey, ain't that
[3562] exciting.
[3564] In any event, your final project, it's
[3566] going to be a presentation. It's going
[3568] to be to the class. And here, you're
[3570] going to include a live demonstration on
[3572] the work you've done towards one of
[3574] those two options. So, again, let me
[3575] repeat. your final project. It'll be a
[3578] presentation.
[3580] The last two days, the last two sessions
[3582] of class are devoted to student
[3584] projects. So, that's when you'll be
[3586] presenting them. You'll include a live
[3588] demonstration on the work that you've
[3591] done towards one of those two options,
[3592] either the ontology mapping or the
[3594] expansion of the semantic pipeline. And
[3596] I'm going to I'm going to want you to
[3598] talk for like a while depending on who
[3602] how many presenters we have. I mean, you
[3604] may end up talking an hour like, and
[3607] we're going to be peppering you with
[3608] questions, don't worry. But you'll get
[3610] up, you do your song and dance, just
[3612] show us what you've done. We'll ask
[3614] questions. We might ask you to add some
[3616] data. I might have some data to play
[3618] with. Just throwing at it at you to see
[3620] if you can play, you can handle it.
[3622] It'll be fine. You'll be in a sterile
[3623] environment. We just want to see what
[3625] you've done. Just want to see how far
[3627] we've pushed that that needle forward. I
[3630] believe in you. You can do it.
[3634] Summary LM super impressive combination
[3638] ensemble of existing tools and
[3639] strategies trained against massive
[3641] amounts of data. Ontologies can be used
[3644] to support them or vice versa. And I
[3647] like I like thinking of them best as
[3649] used as middleware glue between existing
[3651] trustworthy tools. You will be aiming to
[3654] leverage LLM to expand your pipeline or
[3657] generate and evaluate autotology
[3659] mappings
[3660] as a way it's kind of a capstone on what
[3663] we've learned kind of a high level just
[3666] so we can see all the cool work you've
[3669] been doing your level of understanding
[3671] as well as your new found mastery of
[3674] these advancing technologies.
[3677] Can't wait to see it.
