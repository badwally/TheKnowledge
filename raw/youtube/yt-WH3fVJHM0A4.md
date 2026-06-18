---
schema_version: 1
id: yt-WH3fVJHM0A4
type: youtube
title: 'The Year of the Graph: Evaluating graph databases. Panel discussion at Connected
  Data London'
url: https://www.youtube.com/watch?v=WH3fVJHM0A4
authors:
- Connected Data
ingested_at: '2026-06-18T01:38:29Z'
content_hash: sha256:80a71955c2b234aea9d57496c8d092387746ffb4fdf098f35fd72496af1c3f51
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Connected Data
  channel_url: https://www.youtube.com/@ConnectedData
  duration_seconds: 2147
  caption_track: cached
  snippet_count: 306
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:29Z'
  user_correction: null
---
[3] so while they're taking the seats just a quick kind of survey so how many of you
[10] are familiar with graph databases okay
[15] the majority that's good then how many of you are actually using them in projects okay but about the same people
[22] okay so yeah that was actually the first the trigger on how to start the
[28] discussion because I figured the case some people are going to be fairly familiar with the topic and some others well it's it's it's only they're only
[36] getting started so the first question the first topic we're going to address is actually how does one define a graph
[43] database because there's quite a few definitions flying around and as I recently went under undertook the
[52] research research report that I started
[58] writing actually that was the first thing I had to deal with like okay how do i define a graph database so
[64] basically what does the line stand so in my view as I was going through that in
[71] order to view database system as a graph database it has to be well it has to go
[77] all the way so to put it so there has to be an API that covers the entire it
[82] cover cell and if anything you can do with a graph so both transactional and analytical operations otherwise it's I
[90] don't know it can be a system that you use for analytics or it can be something that's half graph but not entirely so
[97] your what what you're taking that how
[104] from perspective of RDF graph I would
[110] say it depends the gray graph database
[116] is our graph system graph system is
[121] system which describes the data which
[131] means it's quite flexible and it
[137] depends on the user but but it's also
[158] flexible what people means by operations let's let's imagine there's a basic
[164] crude system could operations saving update delete and restore the data and
[174] from perspective of RDF it's quite widely used the the model some
[180] operations are not active I mean mmm there is some data databases system
[189] there is no delete data you can say you can link the data not active or you can
[197] describe versioning data versioning and you can say that from some version the
[203] data disappeared but still exist in the system you can define it and the some
[213] RDF graphs are only growing and at the F
[223] it's quite flat flexible the you can you can you can cut the data into different
[231] sub graphs some nodes networks and it's
[239] quite easy to to merge them together do requests across them it's quite quite
[245] quite flexible but the basic concept is simple you just have to you just have
[251] three URL URL like not notice we just
[260] have subject particular objects something has a property and value of this property and from RDF perspective
[268] does enough you have to beat beak
[274] you know concepts big philosophies just quite quite simple and from bet based on
[281] the simple system you can build up and as a previous previous lecture was quite
[288] nice because you could you could find you can describe some simple model and
[294] then merge them together quite easily because of this free information subject
[301] critical object you can merge them together and build up build up that build up and receive final okay so the
[320] definition of a graph database I'll try to keep it simple it has a concept of
[327] nodes and connections or edges and those are both first-class data objects and it
[334] supports crud operations create read update delete and then you know whether
[341] you have a specialty database or not it's still a graph database there's there's room in the market I'll make
[347] this one quick observation and then hand it on someone asked me the other day or
[353] they said I'm using Stanford's snap why should I use taiga graph and snap
[359] Stanford network analysis project or it basically started out as algorithms and
[367] set data sets that they would share publicly because they're a research organization they now have a system
[376] where for loading the data so here's a system where you can run their algorithms to try them but it supports
[382] no Enterprise operations there's there's no idea of backup there's there's no
[388] idea of security it's just like when I did my PhD dissertation I had to create
[394] a graph storage structure I barely I would not call that database I just
[401] needed something to demonstrate my algorithm and there a lot of those around actually
[407] a few they cry we looked at all kinds of things I mean I think the question is wrong right - who cares right if you
[413] call it graph database or not what's your use case what you trying to do you know if you want to store your RDF in a
[418] big data warehouse which we do it with innit if then we store it and we add extra things on top of the RDF we run a
[424] bunch of other operations but then when we want to push that out to customers who do want the kind of database that
[431] the features described doesn't matter that you might use neo they might use Tiger they might use something else and
[436] then when we talk about people doing machine learning and graph analytics then if you're using spark if using
[443] kragle if you're using another framework for processing that's fine too I think the difference is really it's the way
[449] that you think about the data it's about adding the semantics and the meaning in that data and trying to preserve that
[456] through the process and throw and use it actually use it for something sensible
[461] because you can have a graph databases and do a whole bunch of very you know relational type things in it right you
[466] don't need to or you can try and do things that are better suited for a document database you know so if I'm
[472] trying to build a search engine I'm probably gonna need you know elastic search there's elastic give me just enough you know graph query capabilities
[479] in what it has to allow me to do what I need to do maybe that's the right solution for you so I think we get a
[484] little bit cut up on this RDF or this or that it really depends on the use case of what you need to do you know if you
[491] turn the do something really really fast then you know you got Tiger off you got the guy from man graph your nickel in
[496] into memory it's a huge variety it's really exciting time to be in the industry because of the variety that's
[502] that's on offer but I think if you you get really hung up on the different features of the different systems unless
[507] you have a clear idea of what it is you're actually trying to to deliver which is that which is the most important thing yeah I completely agree
[517] with it's it's it's kind of your mindset but what do you think about what what is
[522] the graph so I know from industry projects that have large at the price grass and they don't use graph
[532] technology for most of their that their daily work so forth look at the swing of nature SCI graph
[539] they use elastic search for storing the graph and so they kind of materialize
[545] what once step hops in into the their jason documents and then store it in in
[552] elastic search and the same is for for for the death bought knowledge graph they they they they crawl data from the
[558] web tube and they claim to have the the largest web knowledge graph in the world they use they also use elastic search so
[567] it's it does not offer add anything typically the graph database office you
[572] so when you would like to do two traversals you not you cannot use a last
[578] elastic search anymore but i think they have a graph in a my understanding they
[583] deal with graphs so that's that's one
[591] very pragmatic way of looking at this but for example if you if you have a
[596] graph and you're using something like elastic it means that as you pointed out well there's only so far this can take
[602] you if you want to do traversals if you want to do graph queries then you have to you basically i outgrown it so one
[610] very fundamental let's say divide in the in the graph database world is you know this rdf versus property model and
[618] there's certain things that distinguish these two and there's certain use cases that people tend to use each of these
[626] models for so let's let's start with with victor of this time who's obviously
[632] in the in the property graph world since Tigra graph is a property graph and well
[638] what do you think well do you think that there's such a big divide among these two and what do you see people using
[645] mostly property graphs for i don't think
[650] there's a big divide i think there are people who have a way I see it is
[658] property graphs are general-purpose RDF is specialized and if you are already
[665] using RDF and taking advantage of certain features it has
[671] you would have to you know spend a little time to rethink well how would I accomplish the same thing with a more
[678] general purpose tool where I would it's not out-of-the-box there yet but I have
[684] to set up my data model and my operations to perform what I was doing before
[689] and then you have to ask well why would I make that shift you know yeah again as
[694] as Jeff was saying you have to look at your application what are the demands is there a product out there that can
[700] satisfy those demands so you know Tiger graph is we have yes speed on analytics
[708] on scalable systems so we appeal to people who either have large amounts of
[715] data now or foresee having large amounts of data I want to want to be able to grow and are trying to do analytics
[724] which nests not may not be highly semantic where we you know we deal with
[730] you know you can think of more concrete types of objects we're not dealing with
[736] you know concepts and and trying to you know do logical reasoning on those concepts we could there's you can do
[744] that but it's I guess the one thing I'll say that I found that's when I've tried
[750] to think how would I take an RDF application and move it to property graph one thing is RDF I think has the
[759] idea of inheritance you can have like a class or a type and then a subtype and
[765] and that's not something that's inherently in Tiger graph mate it's not inherently in property graphs in general
[772] you could build it in in your application
[781] so do we have an we have an RDF graph and I guess why do we have that I guess
[787] we're a Content publisher so we want to have a level of standardization that we publish out to multiple consumers so we
[794] can all agree what there's those definitions of those meanings of those concepts are and I say that's really important have a common vocabulary and
[801] so because we're a publisher we could publish in RDF and it could be consumed by any RDF graph or a property graph
[808] whereas if we built it in a very custom way within a particular property graph that wouldn't be a I've been as calm in
[815] a way to to kind of construct it and share it so I guess that that shareability and that open
[821] interoperability was the kind of reason we went down the RDF route I guess you
[826] know we love it and we hate it at the same time it does what it needs to do
[832] there's a great community around it is there are some great tools around it I think you know speed and performance is
[838] always a concern for us that's improving with different technologies like Neptune's come out now
[844] and that's really exciting right so that that's really made some may be easier
[849] for us then put our knowledge graph the RDF graph into something that we can then get a level of performance that's
[855] this required I think we're you know what what are the benefits of that yeah
[861] things like having things like shackle for example which we really like is a standard we can do you know rules we can
[867] do you know Natacha cool things you can do with it and so we like that right and we can say
[873] as a publisher yeah we're using some open standards right and here it is so that that's it that's a benefit for us
[880] things like provenance as well all right we like I think on the property graph side when we see customers when the when
[886] they're using that why do they choose that I think they choose it because they're of the particular operations you
[891] can perform on the traversals so you know if you're using cipher using gremlin using the graph Cree language in
[899] thyra graph they're very very powerful and you can do do things more easily than you can do with something like
[905] sparkle the downside the ways you're creating a custom property model and I
[911] think what we've seen a number of customers the take that anything else graphically
[916] exciting but then they're having to take on a whole bunch of extra modeling work we should maybe we hadn't anticipated
[922] and so I think that can be that could be an interesting car for you'll think I'm just gonna take my deal and load it in
[928] so I guess with the RT of publishing it with the ontology and everything it gives you that out of the box yeah I
[936] agree with Victor that that the liability property growth model is is more than the general model everything
[943] that looks like a graph can be converted into a label property graph so if you use refn and most notably the web
[952] ontology language that imposes some constraints on your data which are not
[957] there in the in the label property graph world and and and it has the good thing
[963] about the the web ontology language in RF is they sustain that so it's much
[969] more easier to to exchange data with RDF then exchange data from one graph
[976] database to another graph graph database
[984] in semantic integration we currently work on our dear quite intense because
[992] it's a really powerful tool and quite flexible there are some ADF features you
[1001] can we exploit quite strong for example
[1007] when we describe properties we can we can say that properties has inheritance
[1017] so we can we can say that for example yeah power power of expression is my
[1024] strong for example we can say that someone likes some some one other person and we can express that the person is
[1033] lost or other other other able and it's quite quite easy to say that and
[1040] yeah it's quite quite powerful and there are machines which are called reasoner's
[1048] and they can quite go to the data quite
[1056] deep and and Express or export from RDF
[1063] graph the stuff which which are not directly set as and yeah it's quite
[1072] powerful really and there are some some
[1080] features which we miss and of course in graph property graph stuff and and
[1090] tricks and tips are all so welcome and way of expression data and describing
[1097] metadata match with the data and yeah
[1102] different many many environment many people work
[1107] with with RDF and especially academic work world is quite strong supporters to
[1117] large projects frameworks really at the foj and a party generous and yes in the
[1129] java bald skull about the JVM world is quite quite powerful okay so yeah you
[1139] you've already touched upon some of the key differences so RDF on the one hand
[1144] offers interoperability and also the ability to have richer and more
[1149] expressive semantic models on the other hand property graphs typically tend to
[1155] offer faster traversal times and more hence more more scalability for for bigger scale and but actually one very
[1163] important aspect was well the use case so these characteristics tend to drive you know the adoption patterns they say
[1171] so depending on what you want to do you have to understand what's more important for you and then choose appropriately
[1177] basically so let's switch to two use cases and Jeff you mentioned earlier
[1182] that in Thomson Reuters you're using you're doing a number of things with with graphs so you can set some light on
[1188] these cases so so one use case we have
[1198] is trying to deliver improved search experience so in that case we are we're
[1205] building our base level graph of organizations of supply chain competitors peer so the kind of
[1212] ecosystem around a particular company and that's all in our RDF graph store
[1218] because that's the kind of content that we're continuously publishing and pushing into our graph store and then we
[1224] have another process where we're taking all of our inbound news or documents and then we're doing we're adding metadata
[1231] and marking up all those documents with topics concepts entities and so on so
[1236] then we're kind of building this kind of super set off you know things are moving and changing a lot and then the kind of
[1242] base level graph then what we need to deliver for the individual user is you know right now right this minute which
[1249] news story should I look at based on all the information that's just been just
[1254] hit the graph yeah so for that I need to kind of pull out little sub graphs around the entity around the topic and
[1262] run a whole range of kind of shortest paths traversals so in that case we're using you know document store for the
[1269] documents then we're tagging those documents or pushing that I see rdf into
[1275] the overall graph we're pulling the sub graph that connects that up into a property graph and then we're running
[1281] all those traversals you know huge hundreds of thousands of traversals actually fishing the number of users
[1287] based on number events to then deliver that kind of instant insight yeah and so
[1294] we're kind of using a combination of different things together in that in that architecture as new technologies
[1302] come along maybe we could do all of that in one place maybe I don't know I'm sure
[1308] would think but at sunrise we've kind of got the slow slightly slower moving kind
[1314] of stuff in our kind of RDF warehouse and then when we're running those traversals we're pulling it into a property graph but we're not persisting
[1321] and storing that entire data set in in a property graph trees don't because you don't need to we just need to run that
[1326] calculation in that particular runtime
[1334] in our projects we use RDF systems because we need the explicity of our
[1341] land and our AF so you know and all of our projects we do have ontology axioms
[1348] or swirl rules so we we need systems that are able to to execute this this
[1356] rules so we use systems like like Aria box for instance or a gross scale which
[1363] is one of our own systems that that the best RDF reasoning on top of a graph
[1370] database actually so so for storing in the data on disk we use neo4j could be any other graph
[1377] database but it typically we use in the neo4j because it has a free communication Edition but on top of that
[1385] we have our and RDF reasoning and RDF
[1392] data modeling and you know I mean that's what our project demands for and and
[1399] therefore we use it so as I said we have
[1409] a few projects exploiting quite some
[1415] reasoning and RDF systems however either said there was also missing features we
[1423] which we need for our projects for our clients and for that we use on top of
[1431] RDF another layer for property graphs so
[1438] we can we can build at the same time property graph I mean Grameen based
[1443] queries yeah and but in our for example
[1451] we have quite huge project with some company in financial markets and they're
[1462] interested on finding staff which are doesn't exist in the data directly so we
[1468] use quests on different reasoner's and our ontology is is it's prepared or
[1478] describes that describe the model and plus big advantage of reasoner stuff so
[1487] reasoner's can consume the the ontology so it's it's describes the debate the
[1494] basic data which are quite simple and basic you can you can you can find them
[1501] in I don't know 5 of 6 files comma delimited files but then we
[1508] exploit the date using the reasoner's and if we miss some features we can add
[1515] this property graph queries yeah me me
[1520] mix approach yeah mix approach so I was really
[1527] fascinated that that to my colleagues mentioned that their their projects or
[1534] or enterprises see you need and actually are maybe now using both RDF and
[1541] property graphs that I guess in your case you said the the store up knowledge is RDF and when you're publishing your
[1549] you're publishing RDF but there needs
[1554] sometimes when you need to do some some analytics you import it into property graph in that that fits some of the
[1563] general use cases we see people may already have their data sitting in some
[1569] data lake or some other relational database but that they have some
[1576] analytical need that they're not able to achieve yet it's it's graph oriented and so they're looking for a
[1582] high-performance property graph well they don't really care they're they're
[1587] looking for a graph and they'd have a certain performance requirement they have and if whoever they can whoever can
[1594] do it is fine with them some of the
[1600] interesting use cases we've seen so in general I think recommend personalized
[1609] recommendation is is good for graphs that's you know maybe not really highly
[1617] semantic but still requires graph you know customer 360 gathering all the data
[1623] related to an individual and trying to get a very holistic that's where the 360
[1629] 360 degree view so you have a better understanding of that entity whether
[1635] that's a person or some other organization and they're you know doing whether it's
[1641] recommendation or on the flipside security criminal investigation but one
[1650] other you know this is sort of a rare application but I think it's neat we have an electric utility that is
[1656] modeling their electric distribution network and that industry also needs to
[1662] do analytics on their distribution network and so they do the analytics in
[1667] graph ok so it turns out that it's yeah
[1674] there's no silver bullet let's say it's not like one single system that at least
[1680] today that can deliver and everything that a customer may may need so the
[1685] mixed approach seems to be prevalent I
[1693] mean the other one of the reasons we have the separate warehouse is that we can it can scale horizontally right so
[1699] we can we just think I'll see em well it's based on Cassandra and elastic and things and something but it's it's
[1706] something that is it scales very wet nicely right and it's very cost effective most of property graph systems
[1713] until now are scale up right so we have very large graphing we've course he's just several versions and iterations of
[1719] that that are being being you know running you know live all the time and some of the graph systems that the pure
[1726] graph database is right there we found the terms of performance whether at slow times or read times or
[1732] just in terms of just the actual scale is just holding that that data set there
[1738] really struggle with that and so that's one reason that we've we've kept those two those two later separate right so I
[1743] think the scalability is really important and even though it was something like Neptune for example it's still you know a scale up right so we
[1751] have to go to the largest instance to load our data and we let me bring it time to do to do other work I think you
[1757] know is that is our data particularly large data set I don't I don't think that it is obviously if you have a
[1762] smaller data set I can fit into that in you know another system that's fine but
[1767] I think as graske in a larger and larger that issue of kind of run my centrality analytics Karamat reversals
[1774] and cannot run across you know multiple parallel machines that's a real missing you know area right today and in for a
[1781] lot of the graph systems are in place and that's a better it's been for the next question we should play what the strengths and weaknesses but that to us
[1788] that's a weakness and that's why we we went with the approach weird Tiger rap
[1793] scales out actually we actually I think
[1799] we've already sort of painted the picture of you know strengths and weaknesses of its approach so and also
[1805] because we kind of run over time I'm going to turn to the audience now and
[1810] let let them know if they have any questions for you well I'll try to make
[1827] it a general purpose answer of okay what what do you need to address you know so
[1834] you have nodes and edges and at the simplest idea you need to partition the
[1840] graph you need to put some of the nodes and edges on on this machine some on that one and and and so on and people
[1847] who come from academic perspective or often thinking of the challenge of doing
[1852] a min cut of how do you find the cut line that cuts across the fewest edges
[1859] and and that's you know certain analytical challenge and it's doable if
[1864] you have a static data set but if you have a dynamically changing data set the
[1871] answer you have today is not valid tomorrow so the approach that Tiger
[1876] graph takes is we don't bother trying to find the min cut we actually our default
[1883] partitioning scheme is to do a random hashing of the vertex IDs
[1889] you know when every time a new node is created we look at the ID and and we
[1895] randomly select a node where it will be stored and it's all hash table lookup so
[1902] it's very fast so it's still very fast lookup yes there's communication from one
[1908] machine to another but we we minimize the amount of communication and I was
[1913] discussing in length with somebody earlier today why in two use cases there's really no penalty for that
[1922] uniform distribution and but I'll let other people give their answers of I
[1928] guess that question was for me but if anybody else if anybody else has anything to say about you know graph
[1934] partitioning
[1974] well it's I'm not that's probably shortest path might be a problematic case so the two cases where
[1983] I was laying out where there's there's not really significant penalty one case
[1988] maybe no penalty if you're doing a full graph analysis like PageRank PageRank
[1996] has to traverse every single edge in the graph multiple times so it doesn't
[2002] matter where you but you have to put the cut somewhere right so it's gonna do the
[2007] same amount of work pretty much no matter how you slice the pie the other
[2014] may be on the other end of the spectrum is what we call internally a small point
[2020] query where you're starting from one vertex and going of one or two hops and
[2026] so you're not going to do very much traversal yes you might in in the worst case have to bounce back and forth with
[2033] with each hop but the advantage of doing the uniform distribution is that when
[2039] you're doing that type of workload like small transactions you're usually trying to do lots of those and then you're
[2046] actually increasing your concurrency because this one machine is busy but all
[2051] the others are free and you know by doing it randomly the probability that the another one is free is actually
[2058] higher
[2063] other questions
[2074] well it works in the sense that you know we have systems in production and that
[2080] our customers are happy I'm not making any claims that it is you
[2085] know comparing how we didn't compare it to a min cut we just said we can this is
[2091] a high performance it's an easy solution to implement and it and it works how it
[2098] works I have before page rank I we do
[2109] have a published benchmark where we took yeah you know if you go to our website I
[2118] don't want to spend my time on I don't want to take up other people's time you can go to our website and and look for
[2124] our benchmark report and we did a distributed database comparing single machine to multiple machines on page
[2130] rank and you can download all the code if you want to verify it yourself
[2147] well thanks thanks everyone and thank you for uh 10
