---
schema_version: 1
id: yt-r7Qbb1yuLkE
type: youtube
title: Wikidata Knowledge Graph to Enable Equitable and Validated Ge... - Jonathan
  Fraine & Lydia Pintscher
url: https://www.youtube.com/watch?v=r7Qbb1yuLkE
authors:
- The Linux Foundation
ingested_at: '2026-06-18T01:38:28Z'
content_hash: sha256:8f34e1ee5293f9d8cc7507920ed72094c35be29eee1e13ca00280679c582a884
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: The Linux Foundation
  channel_url: https://www.youtube.com/@LinuxfoundationOrg
  duration_seconds: 1858
  caption_track: cached
  snippet_count: 289
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:28Z'
  user_correction: null
---
[0] hello everyone uh very exciting to have so many of you here to talk about Wiki
[6] data and how it can help enable more Equitable and validated generative AI
[12] I'm ludia I'm the portfolio lead for Wiki data and I'm here with I'm Jonathan the CTO wikip
[19] media and uh I will start with some what is wik data even um so you have an intro
[26] and then Jonathan will show you cool stuff
[32] so first of all um for those of you who don't know wik data yet uh it's uh one
[37] of uh the Wikipedia projects it's a sister project of Wikipedia uh that is
[42] all about data and the data from Wiki data is used in a lot of technology that
[48] you are using every day without maybe even realizing that it's coming from Wiki data like your digital personal
[55] assistant on your phone um the data in Wiki data is available under cc0 so anyone can do
[62] with it whatever they want um and it's created by a community um with the help
[69] of machines and also for human and machines wik data is highly multilingual
[76] um so it's one of the values of Wikipedia that we U provide the
[81] knowledge that we have to as many people as possible in the language they you
[88] speak um it's a very collaborative project so anyone can uh come and edit
[94] Wiki data and last but not least it's a free and open Knowledge Graph
[100] um now not all of you might be familiar with the concept of a Knowledge Graph so
[106] I will give you a short example um wik dat for example has a has an entry for
[112] Maya Angelo um and we know a bunch of stuff about her um by connecting her to
[121] other things so for example uh we know that her place of birth was uh St Louis
[127] um that she's a human um and that she received some award which again are
[134] things in the graph um that are connected to other things then so for example St Louis would be connected to
[141] other things like um what uh who's the mayor of St Louis how many inhabitants
[148] uh does St Louis have and stuff like that that builds up a huge really huge
[154] graph with general knowledge about the world that is useful um like you find it
[161] in Wikipedia today already so now what makes wik data a bit
[168] of a special knowledge graph um if you already know knowledge graphs uh wik
[173] data is a bit different um first of all
[178] anyone can contribute including you you can go and addit Wiki data today um and
[184] contribute additional knowledge to it additional data to it wik data is also trying to model the
[192] world in a bit more nuanced way than um you're usually used to um and it's built
[198] around the concept of verifiability so for example if there are um legitimate different points of
[206] view about let's say some political territory what it belongs to and so on
[211] we try to um collect all of that all of those views and put them in context with
[217] uh references to sources that claim that to uh reliable sources that claim
[224] that um as I was already saying earlier Wiki data is very multilingual so all
[230] the data we have you can get it uh access to it in um a few hundred
[235] languages which uh we find very valuable and last but not least it is highly
[242] interconnected so it is highly connected internally within the graph but it's
[248] also uh very connected to the other Wikipedia projects and specifically Wikipedia so if you want to understand
[255] how the different Wikipedia articles for example relate to each other wik is a super helpful um source of information
[262] for that and not only that it's also connected to a ton of resources on the
[268] internet um like uh MDB the French national
[274] library um unesco's uh world heritage database Reddit you name it we probably
[281] have a connection to it so if you're for example looking for the IMDb entry for a
[286] famous actor you can find it connected to their social media account to their
[291] Facebook page whatever we probably have it and wik data is a is a great Hub to get to all those places on the web
[301] and uh which makes Wikipedia a bit uh special at the heart of all of this are
[307] people right who contribute every day to making this knowledge graph and
[313] everything around it available to you lovely
[319] people so now I was already hinting earlier there are a lot of um there's a
[327] lot of Technology out there using Wiki data's data or already that you might know or not know about um here just some
[334] examples um some lesser known ones uh the open art browser for example is a
[340] beautiful tool that lets you explore um visual art a course
[346] time um in different museums and so on um and right next to it uh is an is a
[354] mobile phone app that was developed for one of the elections in Germany um 2 years ago
[360] which is about you walking around in a city finding an election campaign poster
[366] you scan it and it will show you um how that person uh voted in the past and
[372] other information about them for example so there are a lot of different ways how
[377] you can uh use that data um now not all the data you might
[386] have um is maybe suitable to be on wi data itself or maybe you want to have
[393] your own Knowledge Graph because you want to model data in your particular way um we also released the software
[401] that is underlying Wiki data called Wiki base as free software um it's open
[406] source anyone can run their own version of wi data so to say either on their own
[413] Hardware or use the software as a service we provide called wik based cloud
[419] and um then do all the things Jonathan will talk about either with wik data
[426] itself or with their own knowledge Jonathan good so
[433] um wik day has been around for a couple of about now 12 years and um it Powers a
[440] lot of really great web apps and U mobile apps and other database interfaces but it wasn't quite being
[446] tapped into by the machine Learning Community especially open source machine learning community and with the large
[453] language models being released for public consumption we realized that we had a wealth of information which we
[459] could get out to the people to use to improve the quality of the information ecosystem and so we wanted to do this in
[467] fact we started um really diving into this project at the San Jose A.D
[473] conference was really great just let you know how the collaborations worked out well um but we want people to be able to
[479] freely access the wiki data's data but in a vectorized formatting with an embedding we want
[486] to uh integrate that embedding into our own search apis and then we want mostly for the in
[493] uh information to improve the quality of of information out there particularly
[499] focusing this at this point on large language models so of course we large language models have two major issues
[506] with them the the the data sets are outdated about the the point with which the model is released it's it's a static
[514] uh interest and then the limited context so you can only get a couple thousand say 8,000 or 16,000 I know there's some
[520] with a million but the predominant Case Case sets is a couple thousand and so we
[526] decided we could uh we already had a method for getting our information out to uh people
[533] to use and access and compile but we wanted to make it more accessible in in the right format that people who build
[539] large models people who build applications on top of them I'm sure you've heard of retrieval augmented
[544] Generation Um to to be able to use our data within them uh in particular we
[549] built a um as a prototype a graph Rag and this is on this is not released yet
[555] uh but basically with the wiki data you would use the vector embeddings uh to
[561] then scan through the plethora of it's about 20 billion types of statements or in different chunk settings a couple
[567] hundred million um paragraphs and so um you go through there and you find it and then from there once you get
[574] the information close to what you want to look for you can then uh probe the graph itself and create out of that uh
[581] more contextual information that is targeted towards your anwers so when you're doing such a Q&A you want to make
[586] sure that um when you we looked up the uh capital of France and just to see if
[593] if the if the code was working and it said London which was apparently true for a year but um the point is that the
[599] graph allows you to have more expansive and depth information um but it also has information in context so it's been
[605] validated by being linked being connected to other systems so it's not just returning what the string in the
[611] database gives you but also the graph links and other nodes being connected to it um just in case if you were um this
[619] is a diagram of a rag system uh particularly we are working with uh
[624] gina. who is a Berlin based open they provide a lot of Open Source person open models on on both hugging face and their
[631] own Services um they also provide a couple million tokens for experimentation on their website uh and
[638] they are an embedding company they've been at this for about four years they work in multilingual operations uh and um they're very
[646] helpful and collaborative so they helped us build uh what we're using their existing embeddings and then we're going
[651] to be working with each other over the next year to build specifically a multilingual embedding for Wiki data because the wiki data's um text isn't a
[658] isn't a a format which makes sense to a graph but not always to a person we're also collaborating with uh data Stacks
[665] who's providing us with an experimental uh Astra DB for the vector database itself that's up here on the left and
[673] this has been a very benefit that the two collaborations has been incredibly helpful where we now have a better grasp
[679] of what we can do what we need to do and how to make it the most effective so I just wanted to say thank you for their
[684] collaborations in fact I we met data Stacks at the last uh Linux gen comment uh um the ai.
[692] workshop um and so the I see here on the left hand side the the vector database which is where all the embedding comes
[698] from and that's that's the if you've heard of vector uh stores before that's where it is and as um Lydia was
[704] mentioning this we're working on right now is getting our tens of billions of
[709] of statements Edge Edge node Edge uh sorry node Edge node um triples into the
[715] vector database but if you have um the pipeline's all open source and freely
[721] available all the code is is um accessible on our GitHub uses a Docker so you don't have to configure system
[727] that much and so you can then take this and use your own Wiki base uh um if you
[732] install it yourself or you can use your own uh we we can provide you with a with a knowledge graph on our wik base cloud
[738] service and you just have to change the link for which what's your your um API
[743] endpoint from the wiki data to your individual Wiki base and pretty much everything else should work as as
[750] expected as retrieval algorithms go uh the user inputs a query upper left it
[755] then gets embedded and that embedding gets embedded query gets compared to the vector database which outputs you'll see
[763] here will output the text that's stored in the vector database but it also outputs the IDS and that's where our
[770] existing um just example graph rag algorithm then goes and uses our our pretty new rest API grabs all grabs the
[778] information the rest API and uses that instead uh to compile the um actual
[785] question and answer system so it takes the maybe a few thousand statements off of the Json and turns them into a
[792] different locally stored Vector database just a couple thousand and then that's
[797] where it gets the final answers from so it has a multi-step process where it it looks through the entirety of Wiki data
[803] vectorized and then it uh takes the IDS which are the most similar and grabs the
[809] the the link information from that the actual context and really deep um
[815] complete sets of information about the those particular IDs like the person's name or the location or the country or
[823] whatever it is you're looking for and if you're familiar with the rag system next you plug in that information as added
[830] updated context into the large language models and it outputs a result so we are
[836] not quite really focusing on the rag part we're FOC we're we're providing it but really our efforts go into embedding
[844] the actual data itself what we care about is that you have access to Wiki data data because we believe that Wiki
[850] data data and have shown in other experiments um is able to improve the
[855] quality of not just large language models but pretty much understanding of people on the internet so here's kind of
[861] what the data would look like on the upper left you just have the metadata you don't actually have to really think
[866] about that too much but one of the options is that we have on the right hand side ways to control for how deep
[873] do you want to go how much quality do you want the information to have if it's fresh or if it's highly cited um uh
[880] number of descriptions also equals number of languages so how universally or globally um represented is it and
[888] then so and then otherwise you would get back a stack of data like this which is very similar to what a wiki.org website
[895] looks like I kept all the Blue Links in there to show you that not only with any one of our chunks do you get a bunch of
[901] strings and text you also get the links to all the data it comes with so you can find the citation find the reference
[909] understand the background context of what is this doing what does it mean so in addition to the information you were
[915] looking for you can also have your pipeline pull back and access all kinds of other information surrounding it and
[922] that's where the linking of the in the linked open data comes from um one thing that we thought was
[928] pretty cool is that Wiki data you can there's already existing algorithms one of which we know about is called
[934] reasonator um where you can take a stack of Wiki data text and turn it into a
[940] useful paragraph and so what we came up with recently was that um you can use
[946] Wiki data byes without a large language model to answer questions you don't need the large language model itself of
[952] course it may phrase it better may have more context larger larger output but um
[958] but if we know that humans and AI Partnerships can improve their works it
[963] did I did find a research paper that said but not performance just you know ability to make decisions we feel that
[969] having humans with obviously we care about Wiki data but knowledge graphs in the AI have a very good way of
[977] understanding context and depth and scope um as well as speed and processing
[982] and ability to integrate um and so far as my philosophy goes it's only uh
[987] humans who can take that that information and deduce from it but we now have a fun live demo let's
[995] see if it works but um so yeah the effect is like I said we're working with these companies so I'm going to show you
[1001] this is on my laptop with the docker deployed it's on a CPU so it's a little bit slow but um but effectively speaking
[1008] um this is my favorite query and I know it works so that's why I'd use it
[1014] um so if we asking you know a knowledge graph and a large language model which
[1019] can't in My Philosophy cannot reason what is the meaning of life and our real
[1025] direction again is to get the information to the world it's not to answer the questions but this does do
[1030] that both and so right now it's it's already um searched the vector database
[1035] that was pretty fast then it goes and grabs all of the Json off of the rest API and says like you know and then
[1043] searches through all of them I hopefully it's cooking my CPUs so it's actually doing multiprocessing correctly but I
[1049] didn't check today and then eventually it will output a there you go a list of
[1054] um links to uh other to where you can get more information so this is where you can pull in all the other
[1060] information we talked about before each of these links if I'm lucky will work and so here's what Wiki data Works
[1067] looks like and so it says you ask what's the meaning of life it says the meaning of life is a spiritual question concerning the and philosophical the
[1073] significance of living existence in general and so for us it's about the smart search it's about the Vector
[1079] search embedding with uh combining with our elastic search and in this case also working with our rest API in the
[1085] background but you can then of course take that and create an actual uh solution itself and then if just you
[1092] know each one of these just for user interface can provide with you a short description of what that link means so
[1097] you can go back and check it out for yourself but for us again that this is just a kind of a toy to show you what
[1103] you can do on your own what we care about is that you have the information out there
[1110] so where are we at um back in December 23 when we we first created this this uh
[1117] concept and presentation for we said we our presentation was we need help and uh people came and said sure I'll let's
[1124] work on this um particularly against the data Stacks which led us to Gina we also had some other meetings with people that
[1129] didn't continue but we still appreciate their time and so it's pretty interesting now that roughly 6 months
[1135] later the English version cuz I'm American there for I know how to work it out but um is pretty well prototyped I
[1142] will say if you want we still need help with other languages Wiki data represents close to 300 languages and
[1149] how to take Knowledge Graph and turn it into string is not easy in all the Lang
[1154] in any language but the ones I can only do the like we have to have our community out there working on us with us to help us do that to make to make
[1163] tupal and turn them into Strings so that the vectorization process is effective um um we're again working with
[1170] gina. in Berlin very very helpful collaborators to build a Wiki data embedding um that will probably start
[1178] actual computation uh sometime later this summer um the fine-tuning of the
[1183] open source large language mods which again was a proposal we we we put forth uh would not be happening yet very soon
[1189] but with everything that we've done I wanted to say thank you to the Linux Foundation we joined the official
[1195] collaboration for the Gen comments which gave us wonderful access to people who really care who really want to
[1201] contribute really want to give back um and so um through them we've met several
[1206] other people to collaborate with and um just they did they didn't agree for me to list their name so I'm not but I just
[1211] want to say thank you it's really great to work with everybody here what do we offer we actually have um um a lot of
[1219] the wiki data internal knowledge of course we try to put everything on the internet we're very focused on fully
[1224] open everything open documentation open source open we will be putting open models which try we'll be working under
[1230] the model openness framework from the Linux Foundation but personal contact
[1235] always helps a little bit so we're happy to meet with people talk about people and help you through your we have Community managers and partner uh
[1243] partnership managers who will go out there and talk to individual organizations or people or groups um who
[1248] can then help understand like what is your use case um and then yep that's all
[1254] thank you very much so again Jonathan Wikipedia deand lud also we read thank
[1260] you very
[1266] much thank you so much everyone um we have about um 10 minutes for questions
[1272] right on target right on target so let's start here or do we have another
[1279] mic thank you very much uh my name is Constantine I'm with Jin tonic AI we're
[1285] doing web 3 for AI development so rag is a very practical concept but it's
[1292] selective and it's not perfect compared to knowledge graphs is there a way for
[1299] llm to Traverse the knowledge graph directly without doing extracts from the
[1306] logic graph and then followup question is that do you plan on building your own
[1312] llm so that we can use as developers super agents that would direct like in a
[1318] mixture of agent model mixture of experts model direct certain queries directly to you for fact
[1327] base [Music] um I would say yes it would be amazing
[1333] if LMS could directly um access an autograph and there are efforts to try
[1340] to figure out how to do this I'm don't know any that actually already Works do
[1345] you none that are released no but people we're in contact with who are trying this out it's actually use the the text
[1351] to Sparkle basically right or we call it Sparkle query generator but it's not our work um as far as yeah so the
[1358] fine-tuning part up here the purple one that was something along the lines of having an agent that can surf the
[1365] knowledge graph itself um and it would at some point have the exact
[1370] organizational structure of the knowledge graph built into the training data set as well that way if you're
[1376] looking for something it can pull it out and knows knows how Wiki data works but I'm not sure how that would translate to other knowledge graphs so was I'm not
[1382] sure what it would be a fully operating system but we love if you use our
[1390] data oh we need you on the mic for the camera um I I was wondering do you are
[1397] you exploring the the the use of chatbots to collect
[1403] contributions like uh for example LinkedIn is basically uh asking
[1409] anyone with some kind of knowledge to contribute so they can build their own database of
[1415] knowledge and the way that uh using chatbot to to contribute and to answer
[1422] specific questions um might be a way to collect easy in a easier way uh more
[1430] data coming from actual humans L all right um um so far no
[1440] um among other reasons because I don't think we can quite get to the um level
[1449] of accuracy that uh our community wants but it's something worth exploring at some point I would
[1454] say I would add that we don't just have the text itself we would have references and links to other text and how that
[1461] organizes and there is a way to use large language models to generate knowledge graphs but it's doesn't give
[1467] everything that Wiki data would want we have other qualifiers that add quality yeah did you get the mic
[1473] somebody else so next up here but yeah good yeah thank you so much for the uh the great uh presentation today um I
[1480] have a question about the uh the embeddings model that you are you guys are using you understand that Gina has a 1 million token uh kind of free
[1487] cheer does not I was I was saying they're they're 81 92 yeah yeah for
[1493] context you mean right right but but the the the question I had was did you
[1498] consider using any um up Source embeddings model that anyone can run
[1505] locally and then send to uh to your API the it is running locally it's on
[1510] hugging face the version V2 is that what you mean the Gina Gina provides their model open source um and the it's built
[1517] off of like the hugging face um large language models as well is that your question oh essentially so you don't
[1524] have to use the the gene IPI to to compute the EMB yes okay but what kind of framework can you do you use to uh to
[1531] actually run it locally um the hugging face sentence Transformers is what I have right now
[1537] but I also have Ama installed just in case for the large language models so yeah the the embedding is through the
[1543] hugging face sentence Transformers and then the the llm which KV the paragraph at the bottom uh that was from um uh
[1551] that that was locally as well through AMA yeah AMA doesn't okay I haven't seen that actually supported the g b
[1558] no no not AMA with Gina AMA with another um another multilingual model called
[1563] stable lm2
[1570] yeah hi um thanks for the presentation first uh I've used and contributed a bit
[1575] also to Viki data uh I have a question um about uh the onology behind Wiki data
[1584] and whether you're planning to use llms to improve it or act on it um and I
[1591] think also in graph rack sometimes the llm builds automatically higher level or
[1598] aggregated um understandings of the graph itself and uh I guess in wi data
[1604] you already have that part because it's Concepts which have already been added so I'm curious to learn how you uh how
[1611] you look at these things let me start with some tiny um Lydia has spent 12 years building Wiki data to what it is
[1617] today I came in the last 2 years and said hey I know how to do AI stuff so that's that's the separation here
[1623] Lydia's like she's the wiki data good um so um ontologies so that's one
[1632] of the things we are quite focused on improving um together with the community
[1637] and one of the things that um is happening now is that also people from
[1643] the community are building experiments um to work with large bage mod s on
[1649] improving the quality of v data itself so one uh Community member for example worked on uh using a large language
[1657] model to detect vandalism so he would uh send the change that someone did to a
[1664] large language model and uh I said like should this be reverted or should this be kept basically um and that actually
[1673] like it's it's getting somewhere um and then and another step to looking at
[1679] ontologies for example I would say why not yeah and I
[1684] mean behind wi data today about 12,000 people right and we have uh over 110
[1692] million entities that we're describing so it's a huge amount of work um and
[1698] support for this people this contributors is one of the big things uh
[1704] that we're doing and and trying to improve all right you want another
[1713] question um thank you for the presentation I think you have a very nice is um interesting problem with the
[1719] languages you are doing so many languages so how are they endel maybe first in the graph is it the same note
[1726] translated what about the llm what would you really build the the wall embeddings for all the language or you do for one
[1733] language which is maybe the more uh you know the more complete and then when you ask you translate and then in and out
[1741] maybe to avoid embedding a lot of things for
[1746] nothing maybe I can start with the first part and then Jonathan can answer the second one so um every entity in Wiki
[1754] data um has language independent data and then uh we have what we call labels
[1761] so you can view it in your language so everyone is working on the same data regardless of which language they speak
[1767] in in the graph so indeed yes so the embedding is basically only as good as the model it's
[1774] built on using to train it and so um if you've got the 100 languages was is that
[1781] the common crawl data set with 101 languages I think sorry um and so those
[1786] are the 100 languages that you can use for the embedding and even those are not great in all of the languages and so I I
[1792] mentioned things like is it Okay in Arabic but but how about Farsi or pashu and the qu they the answer is actually
[1799] mostly good with just Western Latin characters and the rest they can do the best they can I will say you know
[1806] arabic's not that bad but it does it's definitely better in European character sets um and so n so in one of the in
[1814] order to truly expand to all 300 languages we would have to take a a our own model and train it on all 300
[1821] languages and we don't ourselves have enough data for that per language there is a qualification for using
[1826] translations and that's some of our community already does this as well to get like understanding of how things are
[1832] to connected to each other but it's not in our plan right now to understand which direction to take right now we're
[1838] trying to get off the ground what we can do and then basically around next year um because this is the prototypes coming
[1844] together well enough it's um uh coming together and then reaching out to the community for help especially with those other
[1851] languages all right we are at the end of our time thank you so much everyone if you would like to discuss more with us
[1858] we will be outside and happy to chat more coffee time
