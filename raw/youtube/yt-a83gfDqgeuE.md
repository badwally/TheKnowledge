---
schema_version: 1
id: yt-a83gfDqgeuE
type: youtube
title: Whence Whyis? Creating Knowledge Graphs from Documents — Jamie McCusker | KGC
url: https://www.youtube.com/watch?v=a83gfDqgeuE
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:14Z'
content_hash: sha256:6a1220e6c191e3e1f42a8e4a429ee89c87d800c1213b4074c24f9f22505ef4f7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1921
  caption_track: cached
  snippet_count: 287
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:14Z'
  user_correction: null
---
[10] That's one.
[33] So hi, I'm Jamie McCusker. I'm going to be talking about my knowledge graph framework why is today and specifically
[40] how I've been uh using it to uh create knowledge graphs both from documents and
[46] from data. Uh but just as a programming note um
[54] I realize that so much of uh so many of you probably have never actually seen why is or what the point of it is even
[61] especially with there are a lot of uh commercial knowledge graph frameworks out there. Um so I decided to kind of
[68] refocus the talk on the basics of kind of why is how it's put together the motivations behind it and uh why I think
[75] it's uh special and interesting to work with.
[82] So uh first off we'll start with WZ. So what
[87] where did this where did YZ come from? Hence Wentz. Uh so I actually started
[93] Yaz um not with the name of YZ but it started with a question of what would a
[99] what does what does it mean to have a nanocale knowledge graph and so first I
[105] wait nanocale uh because actually at the time I was working with nanom materials uh and uh but I realized that also so
[114] there's a thing called a nano publication which is essentially it's three named graphs there's is an
[121] assertion which is the one we normally think about. It is a very uh simple
[126] named graph in a knowledge graph uh where you would put the knowledge as you normally think of. But how do we know
[133] that this is true? Well, we want to be able to provide provenence about those things. Uh that's the provenence graph.
[140] That's graph number two. Number three is the the uh artifact as a whole, the nano publication itself. How do we talk about
[146] the provenence of the nano publication? Who published it? when was it published and and kind of you know that sort of
[153] stuff. Um and that's the that's the third uh graph. So it's basically uh you
[160] know three named graphs very simple uh that people sometimes think of nanopublications as always being very
[166] small in terms of number of triples. You can have a billion triples in your uh nanopublication assertion. It doesn't
[173] matter uh as long as they all have the same providence.
[179] From there, um, I started, uh, you know, I started
[185] thinking a lot about the, uh, kind of the underlying, uh, promise of the
[190] semantic web, especially the semantic web, uh, layer cake as it, uh, exists today and has existed in the past. And
[198] the thing is is that um there was a promise there that there's all of these cool things we can do with semantic web
[206] and a lot of them have been realized in kind of special use cases here and
[211] there. There are things around provenence and trust and things around reasoning and things around um being
[217] able to do uh data integration across large number of data sources and even
[222] large data sources. a lot of things around um triplication as it used to be
[228] called or what I call knowledge curation um and really uh you know there are all
[234] of these I call them bluffs okay so I said well let's call all the bluffs at once what
[241] happens if we put together something that can realize what everyone's been
[246] trying to do individually into an integrated platform and the last piece is that We uh I was
[254] involved with PRAV back in the day. Um and uh so kind of between
[259] nanopublications as a function of or structure for kind of capturing graph
[266] provenence and prov itself as a way of describing that provenence. We actually
[272] have a lot of really interesting opportunities for knowledge graph management. The last piece is of course
[279] linked open data which of course is uh you know there are a lot of linked open
[284] data platforms out there um but they are basically publishing containers right
[291] they don't necessarily uh do a lot with these other things and so and the last
[297] of course is domain ontologies uh this one is my favorite scio uh semantic
[303] science integrated ontology um but the thing is when we pull all this stuff together. These are Legos that are
[309] supposed to click together. And so let's click them together and see what we can do.
[316] Um so the other piece of course is that uh when uh when you use Y is uh
[324] everything is standardsbased. We are working with RDF front to back there. There is no relational database in it.
[331] Um everything is tracked through uh the use of bravo and nanop publications for
[338] uh revisioning uh truth maintenance as possible using the providence that we
[344] provide through provo because we can say that one nanop publications derived from another um and we of course it's a link
[352] data native that was u like a afternoon project to implement a link data server
[357] on top of you know a triple store Um and uh we can actually perform entity
[364] resolution using kind of like all the as I call it labelish properties that are out there which there's a there's a
[369] number um we can publish data sets using decat we can uh and we can create views
[376] based on the ontologies that we load into the knowledge graph. So when we say hey this is a uh you know this is a
[384] decat data set let's make a view for data sets and have that be a render a
[391] way to render the view for it.
[396] I'm not pushing the button hard enough. Uh so but what is why is so as I said it's
[402] a nanocale uh knowledge graph publishing management analysis framework. So the idea was
[410] originally that this is a um this is basically a workbench for performing
[416] knowledge graph research and then immediately turning around and operationalizing
[422] the out the outputs of that research into a production ready knowledge graph
[429] framework. So someone can come along and create a new a new entity resolver. They
[435] can evaluate it against largecale knowledge graphs uh test it and then publish a plug-in for it that can then
[443] be integrated into production wise uh knowledge graphs immediately. Same thing
[450] with any uh knowledge extraction approaches, any uh knowledge creation approaches, any new visualizations that
[457] might be available. The idea is that it's all pluggable. It's all something that doesn't have to languish as a
[464] research project on an uh an underused GitHub repo for five years before
[470] someone notices it and tries to incorporate it into uh into their framework. When you actually use this,
[477] it's already there. It's ready to go. And essentially the idea is that we are
[484] building knowledge graphs using the best of breed capabilities from both the
[491] commercial space and the research space to be able to say hey this is these
[496] capabilities can be put together without having to worry about any underlying framework issues or compatibilities.
[506] So how do we do this? Well, we start by um we start with a a software stack of
[513] course because everyone everyone loves their ca everyone loves their uh their architecture diagrams. Uh so kind of
[522] from bottom up we use uh we use uh Gina Fuzaki. Now that is obviously uh you
[530] know it's open source it's available for use to everyone. Um, it has some query
[536] uh uh complexity issues and uh it eats disk like a pig, but it's open source
[543] and everyone can grab it. It's also standards compliant enough where it is a
[549] reference implementation that can be plugged that someone else can take a commercial database plug it in without
[556] really any trouble. Uh we also use um so one of the interesting things about Y is
[562] is that it uh natively supports uh databased artifacts and resources in the
[569] graph. You can upload files, you can upload a lot of files into Yas and have them be stored in a uh in a uh file
[578] repository. Each file that you upload gets its own URI and then you can
[583] publish metadata about those files in place in the graph and be able to do
[589] things like transform it into RDF if you like. You can serve it up, you can do whatever you need to do with it. Um, and
[595] so we we publish images, we publish data, we publish documents, it all can go into YAS or not because it's just a
[602] URI and so you can just reference it out on the web instead if that's helpful. And then finally we use celery as the
[608] basis for a distributed inference agent system uh that I will talk about in a
[613] minute. Um but on top of uh on top of all that we have essentially a user
[619] interface uh system and a uh knowledge inference system. Uh we can then provide
[627] custom views, custom uh basically we can do on demand loading of linked data uh
[634] using uh importers. Um and on top of that are basically a bunch of uh uh a
[642] bunch of uh user interfaces based on uh things like uh Vega Light, Sight
[648] Escape.js, Vue.js, use material design. We're trying to kind of keep it nice and cool and sexy.
[654] But the the thing is that all this stuff up here is all replaceable. You can customize everything front to back on
[661] the user interface. On the knowledge curation side, you can replace the database. It's all pluggable.
[670] Uh this is kind of the ecosystem that uh why enables. you have the ability to uh
[676] essentially build out a set of knowledge curation capabilities uh both in uh kind
[682] of so uh essentially uh knowledge extraction uh you know if you like uh if
[689] you like mrebel you can write a um an agent for that if you have a prompt based uh knowledge extraction tool that
[696] you like you can write one for that um and uh you can couple that with uh semantic ETL approaches both standard
[703] ones like uh RML, but also uh uh kind of more domain specific ones like semantic
[710] data dictionaries and my favorite uh semantic ETL to tools settler. Um that
[717] along with the ability to uh map in link data on demand uh that all gets fed into ontologies. But the thing is is that the
[724] interaction with users also produces knowledge. And so all of this of course is the basis for uh you know everything
[732] kind of comes in as its own nanopublication. And then uh it the
[738] knowledge inference system also keys off of that. It says hey here's a new chunk of knowledge. Let's use what we see here
[746] and you know is am I as an agent interested in this? that am I interested
[752] in this? It's just a sparkle query that gets run over this chunk of knowledge that we've basically uh atomized at the
[760] nano scale and uh we then have you can uh the other side of an uh agent is a
[767] python function that you can then produce some new RDF and that gets added to the graph gets added back to the
[774] cycle. Inference agents, as I said, are this is really I mean, so uh you fill in the
[781] this blank here and this blank here, but this is an in this is all there is to an
[786] inference agent. It's really that simple. You uh you get some RDF lib
[791] resource objects for uh kind of an uh the resource in question. You get some
[797] input input information in one graph, you write output information to another graph, and you send it on its way. And
[803] that's all there is. And then uh what happens is that the
[810] life cycle of these nanopublications basically it means that you know you have these you have transactions
[818] essentially coming in from many different places. uh they all get pushed to uh to the Sparkle endpoint and then
[825] there's uh kind of as that's being managed that gets uh run against every
[831] registered agent that's in the system and they can do all sorts of stuff uh
[836] including things that we haven't imagined yet because it's very open-ended and you can you know as you
[842] write your new knowledge graph you can add those agents as you like ways of testing them but once it's in once it's
[848] actually registered in this it kind of works in this process you run that thing that creates a new nanop publication for
[855] every time that you have every time that function runs um and that adds new nanopublications to the graph and starts
[863] the process over. And so for those of you who are familiar with reasoners, this starts looking like a forward chaining reasoner. And that's because it
[869] is except that your um you know your head is a uh is a fi a python function
[878] that produces uh arbitrary RDF. Your body is a um is a sparkle query that can
[887] match against arbitrary RDF which makes it a ve very powerful and very easy to
[892] make very complex uh basically inference steps within your knowledge graph. You
[898] know you can tie in obviously large language models. You can tie in and can
[904] we can and do tie in you know whole whole scale knowledge curation and
[909] pretty much everything else. Now on to the user interface. So as I
[915] mentioned we have a type based user interface. Um we have the ability to take um basically this is a matrix of
[924] the oh sorry just uh hopefully that wasn't a spoiler. Uh so
[932] basically for every type that you have that you're interested in um there are
[937] actually a number of different views. So view is that standard thing. You just go to a web page and you see it, right?
[942] That's kind of normal a normal way of looking at things. But there's also other things you might want to do with
[948] the uh with entities in the graph, you know, including editing them, creating new ones, uh finding things that are
[955] related, um edit again. I don't know why. Anyway, uh looking for instances of
[962] for instance class. And so you'll see that between the view itself and the
[968] type there it basically creates a matrix of um templates that get rendered. These
[974] are all Ginger templates people who know how to write uh who know how to code web applications that'll look very normal
[981] and uh and uh kind of run-of-the-mill for them. Uh and but one of the cool
[987] things about it is that there are data views and there are web views and the
[992] data views will drive um user interfaces and so you can actually customize what
[999] you see in a user interface based on these data views without having to change the interface itself. Conversely,
[1005] you can consume uh you can consu so for instance with related you can actually
[1011] consume that against a number of different things. So if you're looking for things that are similar to it, that's interesting to a web page, but
[1017] that's also interesting to a uh a a you know a network explorer. And so every
[1023] time so we basically treat these as crossf functional contracts and I'll show you a better example of that in a
[1030] second. Uh we also have uh kind of leveraged the fact that we can you know
[1036] basically store sparkle queries as entities unto themselves and pairing them with a tool called Vegaite which is
[1043] a way of writing uh very simple uh schemas for uh for visualizations and
[1050] you're actually able to get very uh build out either very simple or very complex uh data visualizations.
[1057] Uh and actually on one of our projects we had a material scientist, not a computer scientist, not a programmer,
[1063] but a material scientist create he got very enthusiastic about it and create over a hundred different visualizations
[1070] for the materials mind knowledge graph including some fun ones like a happy new
[1076] year. Um, the other thing we do is that there's this ability to because again we're
[1083] talking about kind of cross-linking uh views with um with user interfaces,
[1090] we can define some of these fairly closely and be able to say hey this is how you if you're looking at like you
[1096] know links out from an entity we can basically say hey this is how you do it.
[1101] This is the structure that we want but we don't have to stick with simple uh
[1106] subject predicate object. So obviously so I know a lot of you don't like reification but I always think of
[1112] reification uh some what one person's reification is another person's object
[1117] that everyone else likes to ignore. And so I I uh I like using reifications
[1125] because it realizes things that you probably didn't think were actually important.
[1131] And so here we basically let you uh kind of build out a uh kind of these
[1137] interactions which can be again complex or simple depending on the graph.
[1143] Um oh did I did I skip over? Yeah I did. Okay. Um the other thing is that because
[1150] we have this view here, you know, essentially this gets composed, these get these templates get filled by
[1156] sparkle queries. And so we can do some really interesting stuff with this
[1161] including uh you know you can have multiple uh sparkle multiple uh matches
[1167] to a given link in there. And so what we can do is we can actually combine them
[1173] in this case with uh Stoofer Z method because uh in some some of our knowledge
[1178] graphs we actually have probabilities attached through the nano publication to
[1184] the assertions that are in the graph and so we can roll those up into a uh into a
[1190] cumulative um probability for multiple assertions for it. So if you have a a
[1197] classifier that has a certain level of confidence, you can pair that you can uh join that into a ensemble of classifiers
[1205] and basically provide uh consensus predictions on your uh on your actual uh
[1212] whatever it is you're saying. And this is actually uh this is a
[1217] network explorer. This looks really complicated, right? So this is actually one of the values of uh using that sort
[1223] of rollup. This is every interaction uh that Jean Beljan Yeah. every person that
[1231] Jean Beljan uh interacts with in in lay miz. Uh it's a lot of people uh but the
[1237] thing is that sometime some people are fleeting and they come and go and that's fine. And in this network graph you get
[1243] one link for every character interaction. Um if you roll it up to kind of the
[1249] people he interacts with the most you can actually see a narrative structure in here. you can see who he interacts
[1256] with the most and who they interact with most. Uh and essentially we do that simply by filtering on that uh on the um
[1265] struct on the uh uh meta analysis that we performed.
[1272] Uh we're also able to customize those views. So um here we you know here we
[1278] actually have like a uh you know this is a reified uh participant that actually
[1284] does uh you know basically we have b two interaction two people interacting here
[1290] here it's just a simple subject predicate object and so depending on the query you use the the uh the the that
[1298] lets you kind of roll that up and so it's like it's almost a way of projecting uh a RDF graph in
[1305] customizable ways into a linked property graph except that you don't have to worry about those pesky flat properties
[1312] that you get in LPGs. Similarly, uh if you have classes of
[1318] things, sorry, you have classes of things. Is this for
[1325] me or is this some my um
[1332] Yeah, I wasn't going to do drink first. Um this is these are classes, right? So
[1337] classes work differently from instances, but we're still using the same views.
[1344] uh and uh what what I do is that essentially
[1349] I have the ability to roll up these views and say hey this is how we
[1355] might want to look at how these uh how these things interact with each other
[1361] so sorry um going back to charts this is kind of
[1367] showing narrative flow of thank you of the graph um
[1374] Oh my god. Thank you. Lifesaver.
[1381] Oops. Uh we're
[1388] also able to use uh so uh the Vega team also has this tool called uh um uh why
[1397] do I I don't remember the name of it. I did, didn't I?
[1402] Did I? Oh, yeah. So, okay. So, you're able to view so you're able to edit these things, but then you can also um
[1409] you know, so that this the this is a more complex vega visualization from the
[1415] Y-axis is number of interactions or the number of appearances of a character.
[1423] Oh man. Um the colors are individual characters.
[1432] So you can see so this bit here this is actually Jean Beljon. You can see that in this book he
[1439] just disappears. This might be the one where he talks about the French uh he does like a lot of weird
[1447] digressions and and yeah that that's that's probably one
[1453] of those. Uh we also have the abil you know obviously you want to publish it so you
[1459] have the ability to to kind of create the visualization as a resource in and of itself
[1465] which means that you can add metadata itself and it becomes a a member of the graph same as everything else. Uh uh
[1472] data voyager is the name of the of a tool that they have that actually lets you um kind of build these sorts of
[1480] visualizations uh use kind of drag and drop and uh we've integrated that as well. Um this
[1487] is an example of a nanop publication. This one's very simple but it describes
[1492] the uh the data that we loaded uh to actually produce the limiz graph. it it
[1499] comes from there's actually a uh they're available on GitHub and then what we do and so this guy Mad Studio New actually
[1508] provides it he did some kind of clean up and curation to finish out uh Donald N's work um but basically we have the
[1515] ability to say that hey yeah I uh Jamie made this uh a while back now and uh you
[1523] know we can also say that you know this uh the the JS that you know the file
[1528] conforms to a particular data dictionary and so then we can actually process it and you know actually run it through. So
[1535] when we load this file in we actually just get this RDF it records this but
[1541] then the semantic data dictionary agent looks at this and says hey there's a std in here let's make uh a template for
[1549] processing it and then that hands it off to the semantic ETL agent which actually processes it.
[1556] Uh and finally, what you came here for is real work with like knowledge extraction. Um this is uh kind of hot
[1565] and not quite off the presses. Uh basically, uh we have the ability to uh
[1573] so this is a uh kind of there's a dialogue agent here that I'm actually
[1578] talking with. And don't worry about the the null values here. That's actually that's those are actually tool calls.
[1585] those are responses where where you uh don't have necessarily any output but it's actually producing triples that are
[1592] pulling it in pulling in. So uh what it's done is I in another conversation I I told it about myself. So it actually
[1599] went and looked in the graph and said Jamie McCuster is an ontologist because that's all they had. Um and so I said
[1604] that she went uh I went to RPI and advised Deborah McKinnus. So basically went through this thing and kind of
[1610] describe myself and if you actually go into the graph for me and look look me up uh it's actually pulled that out and
[1616] it actually does that in a fairly consistent way. Um and next steps are to
[1622] using context learning to be able to customize how this create uh is created and so we can actually build uh graphs
[1628] in the style that you need rather than the style that uh people have been training uh knowledge extractors for the
[1635] past 10 years which is basically wiki data which is great but not all graphs are wiki data. Behind the scenes, we're
[1642] also uh this is kind of where it came out of. Uh behind the scenes, basically uh we have this idea of kind of pulling
[1650] in uh you know uses schema.org. Actually, it doesn't show what I thought it would show, but this is actually from
[1655] another project where we were doing uh scene graph extraction uh through dialogue. And so we were actually so we
[1663] use um the activity stream uh framework to actually uh represent uh dialogue in
[1671] the knowledge graph. So again the dialogue itself is part of the graph. It's part of the provenence that comes
[1677] along with it and each comment you make is a nanopublication that gets added.
[1682] Um so anyway yeah so uh to actually get yas it's a python package you can use
[1690] pip pip install y um there's a docker image uh documentation on read the docs
[1698] uh we have a github and uh it's really kind of boringly standard for for these
[1704] sorts of uh open source packages which is a good thing because you don't have to uh you only have to bother me when
[1710] you start getting stuck or you just want to talk to me cuz I'm fun to talk to. Uh
[1716] and then last bit is the credits. Uh this this is not just me. I mean I did
[1722] do a lot of it but uh at RPI uh this is you know kind of a long this has been a
[1728] long-term project. Sam Stoofer, Gordon Miner, Sabir Rashiden, Mik Santos uh are
[1734] staff and faculty or no staff staff and uh students. Uh so uh Sabi was was a
[1742] student uh Sam Gordon and Enrique were uh fellow staff members. Uh we all
[1747] worked on this together uh to uh to uh to kind of build this out. We also have
[1753] some collaborators from other uh institutions specifically uh from Duke,
[1759] Tulumo, Fate and Ana Wallace helped me a lot a ton with the user interface especially around uh data sets and data
[1766] visualization. Uh, and Mike Degan is the guy who made those hundreds of
[1772] visualizations for us. And that is the last slide.
[1786] Um, do we have a microphone?
[1791] Oh my god. I'm sorry. I'll just ask. I just want to have you
[1804] uh have you shown what you've done with especially with the considering the
[1810] lesser the character uh to the language department set RPI.
[1817] No, because it's not uh I haven't done the interesting part yet, which is to have it to have a a knowledge extractor
[1824] read lay for me. That's going to be I am curious because I think this will
[1831] go very well if you uh include the text encoding initiative TI
[1839] in your work. Talk to anybody in the English department or any of that. I think this
[1845] is amazing. Thank you. All right. Thank you. Oh, sorry. No, go
[1851] ahead. No, no. It's okay. So, this great work. My question is going back to your first
[1858] slide, nano publication, can you say in the extraction?
[1863] Which part is assertion? Which part is provenence? And which part is public? Yeah. I I just want to relay this to the
[1871] example you're doing. Okay. So when you um the assertion is
[1877] the fact that Jean Beljan talked to Cozette in chapter 3 paragraph 2.
[1884] Those are the facts. The providence is that it was stored in uh Donald N's
[1892] uh lay miz uh character thing.
[1897] The publication info is the fact that Oh, I just broke the remote. Sorry. I'll
[1902] fix that one before we finish. Uh is the fact that um I Jamie McCusker uploaded
[1908] the data set into Y as on the such and so a date. So basically the events that how you
[1915] have that data or you make that data available as a publication. Exactly. Very very well. Thank you. I just want
[1921] to link to your first slide. Yeah. Yeah.
