---
schema_version: 1
id: yt-H4BbWdhhuEE
type: youtube
title: 'KGC 2022 Panel: ''Knowledge Graph Architecture: Where Are We and Where Are
  We Going?'''
url: https://www.youtube.com/watch?v=H4BbWdhhuEE
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:19Z'
content_hash: sha256:c6e168db58fedf5d004a21c0ead27b0f3cfff676e56305f0fbe86b07e9ab41ca
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 3582
  caption_track: cached
  snippet_count: 562
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:19Z'
  user_correction: null
---
[3] can we get the air meat here okay
[22] hello hello
[28] hello it's very interesting to see it all in one
[35] slice hello
[40] testing test do we have is gautam are you on there
[58] okay well when he joins well okay so a matter of time because we only have one hour and there's so much stuff
[64] to talk about um and i thought gautam was gonna be here in person we're gonna have this let
[70] me sit over here so first of all we've had a great session and let me introduce myself again my name is juan cicada i'm the
[77] principal scientist at data.world but i'm also moderating this because i also
[82] have our podcast cataloging cocktail which is an honest no bs non-salesy conversation about data and
[89] even though i do work for a vendor i'm not going to be talking in representation from the vendor
[95] and that's why there are no other vendors in here because we don't want to be salesy so
[101] you all very well presented the architectures today of knowledge graphs um so part of the question i want to go
[108] through is what does the knowledge graph architecture look like today and we've seen them we've seen several of them
[113] today and what i want to go through is where should we be going tomorrow
[121] what so and what you presented today what were the lessons learned
[126] like i don't think we magically got here all right on the first time so what are the things that you should
[132] go off and and tell your previous self from one two three years ago saying hell no i don't want to go do this
[140] and then there's another topic which is bob moogle started out today talking about the modern data stack and
[147] snowflake and and reverse etl and and and all these other things and
[153] none of that stuff showed up today so what's the relationship between these knowledge graph architectures and the
[159] modern data stack and uh we're i think gautam is there hey yeah hey hey
[165] everyone sorry like you know i i could join remotely right yeah okay okay
[171] so hopefully you got my interest so with that i'm just gonna
[176] you kind of saw my intro so who wants to go first was kind of guess i'm gonna start pushing and uh
[181] let's just start talking so who wants to take it off first sure so
[187] i think i guess one of the the this is answering kind of two of your questions at once um i think the future of
[194] knowledge graph architectures is that there is not a kind of single knowledge graph architecture that it's one of the
[200] kind of most kind of flexible frameworks that is very specific to different use cases i think
[206] that there are going to be knowledge graphs that are very relevant to certain applications you know like the
[212] recommender engine use case that i talked about that's something that is highly specialized and um you know
[218] requires a kind of micro architecture in the in the larger ecosystem of that
[224] organization but in gregor's presentation you talked about knowledge graphs for kind of like
[231] enterprise-wide data connectivity and sharing and so i think there's going to be
[237] more and more in all drafts that follow that format too um so i i think that there's going to be a
[244] there are i don't know they're going to be a variety of ways and scales that knowledge graphs are going to be more
[251] and more prevalent um as we go forward all right so you you you also spoke a lot about prototyping right now
[258] gautam and and gregory i mean ubs and intuit gigantic companies and you from
[263] we can tell these are things in production is the architecture that you have today
[268] is it how is that evolving for tomorrow um so first of all
[274] 100 agree with sarah what i see it's there's no one-size-fits-all
[279] and banking on one technology or one specific stack um is futile in my mind or my
[287] opinion it will evolve over time and where we
[294] where we see the future heading is embracing the diversity and basically already planning for okay we have to
[301] deal with multiple technologies we have to deal with multiple cloud vendors most likely we have to deal with multiple
[307] database technologies you name it so embracing the the diversity that's where
[312] i see or where we prepare all right so gregor saying embracing diversity gautam can you add
[320] to this on the screen and you're muted if you're talking
[327] yeah sorry i muted myself yeah i i think uh like first of all like really thanks for
[333] this uh rotation and uh i would say from the knowledge graph
[339] perspective it will take some time to take a shape
[345] to kind of a well-defined architecture or a pattern that everyone can use
[350] for for time being like you know the knowledge graph is going in a way that it's trying to solve problems from
[357] various domains right so each domain is picking their own like solution to solve for the
[364] knowledge graph architecture right and how i see that initially like the technology goes very broad like you know
[371] it diverges into multiple kind of things and then it starts converging kind of a thing so currently we are a stage where
[377] we are like divergent but after some time i mean maybe in like next five
[382] years or so we will start seeing like adoption of knowledge graph in like multiple
[388] organizations and then converging towards a common architecture that can be used by like i mean as a pattern for
[396] everyone like you know in that industry so that's how i see like you know we we would be going towards an alcohol
[403] and one thing i'll add too to answer your question about what does like the future look like my
[408] wish list would be when a company is establishing themselves maybe they're
[413] starting up or they're you know doing some very kind of strategic conversations that they have
[419] someone who is like a chief modeling officer or someone who at like the top down when making a business plan is
[427] coming up with this is the way that we want our data to be monolith modeled in a central fashion and that that would
[434] just be part of the the way that applications are evolving and continuing to be integrated
[441] because i think what is happening right now is that we have organizations that already have
[447] tons of data tons of applications they're trying to reconcile the meaning and using central models to bring those
[453] together but i think it would be interesting in the future if you start with that like model first and see if
[458] that sets like a strategic guideline for for or for you know people at all all
[463] different levels bravo so so this is super interesting and this is i i mean if you i push a lot this
[470] whole notion of we need to we live in this world of a data first world we need to go into this knowledge first world
[476] are you proposing that we should be able to we're shifting the role of a chief data officer to a chief
[481] data and knowledge officer or chief knowledge officer is this a crazy thing to think about or is it just words it doesn't matter
[488] both have a place like chief data officer more concerned about governance and
[494] um adhering to to security those kind of and explaining
[500] the data and then chief how did you call it achievement chief modeling officer but not i mean i do
[506] work in knowledge management so but i'm happy to see a chief knowledge officer just someone who who values the the
[512] importance of having a model in the first place will go a long way go to intuit do you foresee something
[520] like that in the future or is this too crazy are we smoking dope here uh
[526] like inter currently like the direction is uh we have achieved data officer of
[531] course like the chief knowledge officer like not yet given a lot of thought
[537] about it like getting to its side but who knows like things may change over the time looking at the industry trend
[542] kind of thing but it's good to be like you know closely connected with the data organization
[548] because that is where all the knowledge lies like that's how i see at the same time like the data organization has to
[554] be accessible by all the like business marketing and like you know even
[559] non-tech people so that they they can you know bring their insights within the
[565] data organization they can bring their needs that's how this whole overall knowledge graph can be built here
[571] all right so let's dig in let's get into the details here because i i we're kind of still kind of fluffy and i want to do
[576] some stuff so what are the parts of the architectures that we're not talking today that we should be that should be
[582] in the future for example um it goes mentioned but not specifically we talked about identity
[588] right we have to go reconcile identity but and all these architectures i see even in
[593] the modern data stack and and hear knowledge graphs like where does entity resolution show up i mean explicitly are
[598] we are we put in are we just assuming it happens but but so that's one thing i'm not seeing for example um
[605] inferencing is something that has we we've we've talked about it but it it doesn't see is it just also entailed
[612] that it's going to be part of these systems or is there something more explicit that's missing here as two examples just
[618] very specifically what are we not talking about today that we should be that is something that we will be talking about tomorrow
[626] who wants to go first try to take it um so when it comes to
[633] the aspects that we that we're not talking i can speak for for ourselves say one of
[638] the big headaches that we have is the representation of temporal data
[644] how how does the whole data set change and more of over time don't have a good answer for that part
[650] and um the whole topic of entitlements is a major major headache for us
[657] um how shall we permission someone to look at data
[663] is it based on the source um right now we sort of like dancing around it by
[669] saying well whatever the entitlement structure and the sources but as soon as you combine
[674] a couple of sources it becomes a hard problem so those are two areas where i think that
[680] um we as a community need to invest a little more time and effort
[686] very specifically temporal and entitlements anything to add
[691] yeah i mean to touch on the two examples that you used around like identity graphs and then um
[699] in inference i think that those will look different in terms of i think identity types of graphs or and that
[706] would support entity resolution should be hopefully in the future something that's like business strategic and um something
[714] that you know that there's there are efforts around people not to extend the chief modeling officer
[721] um like use case too much but you know you would have people who also are owning you know what is our employee 360
[727] look like what does our customer 360 look like back to the use case about where customers that you talked about in
[733] your in your um in your presentation you know where all the different places that customers are represented and so i do
[739] think that every business has probably less than 10 like key concepts that are like critical to the way their
[745] business operates and so it would be interesting in the future if you have people that are guiding the identity
[751] resolution for each of those things and using shared technology but different modeling across those
[757] i think inference is something that is more specific to use case like it
[763] will it would need to be more driven by specific business problems and specific industries at specific organizations i
[770] don't foresee there being just kind of like generalized inferencing technology i guess maybe
[776] some types of like insight engines but i think it will be hard to get real like
[781] investment and momentum of those if there's not trying to like infer what you know having those be more use case
[786] driven gautam would you add something else
[792] uh i would like to add a few points here one is that like identity resolution that is having one
[799] hot topic like you know that we are also working on and i know we solved for the identity
[805] but now the identity resolution what we have found is that like different domains
[811] they look for different algorithms for resolving the identity so it's not like you know one kind of a
[817] silver bullet through which we can solve it so in such a scenario like developing
[823] identity resolution as a capability and adding an ai aspect to it like that is
[829] that is another part like you know where we can add a confidence level and then this durable capability that can be
[835] configured like based on different use cases and domains that that can sell for
[840] like a large organization like into it right so i mean and at the same time like uh
[845] when we say identity it's not only just about our customers like in future we might need to look for it like our
[852] customers customers kind of a thing like so i mean there are like businesses where you are not limited like just to
[859] like initial set of customers because it's a network effect when we create a graph so there one has to
[866] bring the same lens and maybe some configurable service for that where you
[871] can resolve the identity of your customers customers also and that way this whole ecosystem can work and and i
[877] mean obviously you can start integrating with other organizations other graphs kind of a thing that way this whole
[883] ecosystem develops i think one other thing we didn't
[889] acknowledge too much today and probably appropriately because this is the data architecture track but is around
[895] content as like a data product too and i think in the future we're going to see
[900] more componentized content and ways that like the best practices around you know
[906] extracting meaning from content not just through like tags and concepts but having you know more
[913] more struck i guess yeah more like structure from unstructured content um as part of the
[920] knowledge graph ecosystem so we've been talking about kind of like the future but i want to go a little bit
[925] back to the past of what is your message for folks who are
[930] trying to go do the same stop don't even consider doing that right because you're going to go down a
[936] rabbit hole and we've already done that what are those things that you'll tell people don't do and things that you would encourage them to
[942] to continue um so i would say
[949] we watch sarah's um presentation was an excellent summary of what to do and what not to do
[957] so i i wish i could travel back in time like 10 years and
[962] as he changed a few things because i went down every rabbit hole and probably made all the mistakes um so it was nice
[969] can you share a couple of the the true pain points that you're like oh my you you cry thinking that you went
[975] down with that like how yeah yeah well one is is
[981] trying to solve the wrong problem and that is probably my biggest regret
[986] is running after the wrong use case um not clarifying the the problem enough
[993] it goes a long way to as you first figure out what the problem is um and it's it's a shiny technology that
[1000] you can apply but if it's a wrong problem it doesn't matter
[1006] so that's probably the i know it sounds a bit shallow but it's it's the truth like
[1013] figure out what the problem is and solve just that okay so so to build on that like how what is or what was your
[1020] realization like how did you realize that this is the wrong problem i mean did you wake up one morning talk or what
[1025] was the evolution for this um the the evolution was that budget was
[1032] drying up money money drives everything right here so if if you find the right problem and
[1038] if you solve someone's pain point in the business money will follow and
[1045] surefire sure way to realize oh you're on the wrong track is budget dries up you cannot hire you
[1052] cannot buy renew licenses so things slowly die off that's that was my
[1059] realization no one tells you up front you suck but it's it gets slowly okay that's a very
[1066] concrete lesson learned here right is follow the money if you can't get the money for this right probably not
[1071] solving the right problem i think another kind of lesson learned throughout different types of use cases
[1078] um like you mentioned you know graph technology can feel like this shiny thing that you want to like experiment
[1084] with and and try to fit everything but i think we've learned throughout different engagements that not everything has to
[1090] be modeled and stored within the graph there you know there's like certain types i was working on one project where
[1098] we um i actually mentioned it in the presentation it was pulling together data from different um like uh
[1106] what are they called scientific instruments and some of them were uh bringing in continuous data and so we
[1113] were we had information on particular um like experiments that had like you know
[1119] millions and millions of data points and it didn't make sense to spend the energy
[1124] pulling those into the graph and using those um it just you know increases the cost increases the um the
[1132] you know the physical cost but then also just the cost of doing like executing queries and so i think as part of the
[1138] design process it's important to look at everything really and critically like what involves in what is
[1144] you know beneficial to have within the graph and what can have a kind of relationship or storage outside of the
[1149] graph so i think we're going to be seeing more and more that being part of the modeling conversation and more ways to like
[1157] virtually connect with metadata about your concepts that it's not critical to
[1162] have actually stored within the graph right so this is a really important point i'm glad he brought it up because i wanted to get there and i want to get
[1168] there in a second about how to know what goes in a graph and what doesn't go into graph because i think also my experience
[1173] is like oh you think everything gets into the graph and like that's probably one of the first things you realize you don't and i want to purchase the gautam
[1179] you brought up in your presentation about all having all these different storage mechanisms a polyglot approach
[1185] um is it was this a realization you had from the beginning or were you guys going down the let's
[1192] put everything in a graph and then realize we shouldn't can you can you share with your share with us your
[1197] experience your insights on this yeah so so yeah i happy to share that yeah so what happened is that like we
[1205] started a journey like three years back and we had already the like experts and architects like you know who had deep
[1212] knowledge into this uh kind of a problem domain now
[1217] in that scenario i like you know i'm happy to share that we actually started like
[1223] from polygon strategy only like because we in the past like we have come across those pitfalls where you start from the
[1230] graph or you start from one specific like you know database storage technology so that's the reason we from
[1236] the beginning itself started on the polyglot where we said hey this is the kind of data which
[1242] goes better into like a big document store and this is a great kind of attribute
[1325] and we use whatever technology is the right fit so we use [Music]
[1330] um what i would use um elasticsearch for search um
[1336] graph store use kafka or it's not not necessarily a database
[1341] but we use kafka with k sql that makes it almost a database so we use whatever fits a bill
[1348] all right i think this is an important message too that i think a lot of people coming on board with knowledge graphs think that it's a graph database right
[1355] our knowledge graph is a graph database equivalent i think the takeaway here is it's not it's much more than that i
[1362] think the devil's in the details here so um let's talk about access
[1368] and several times we've heard about graphql we've heard about apis we have query languages uh
[1374] sparkle cipher gremlin all that stuff what are the access patterns
[1380] within your data architect your knowledge graph architecture
[1385] yeah question for me for everybody right um so we we started out with an api first
[1392] approach um then we morphed it into graphql and a similar pattern to to our
[1398] persistence storage that we say we support whatever um
[1405] whatever what's the bill same there we have some rest we have graphql
[1411] we pipe out data into into kafka it it depends really on the use case
[1417] in this case i would say the same thing it completely depends on the use case um
[1423] and that i think one of the benefits is that you can you know you can use a single knowledge graph to
[1430] serve multiple different types of access patterns and so these all get translated to
[1436] a query over the graph or or just kind of get a little bit more into the details
[1443] um so it some the most of it goes against the sparkle endpoint um but we cache
[1451] a lot of our knowledge graph because our apis get hammered
[1456] um so we have probably eighty percent of our graph is in persistent cache okay
[1463] gautam could like to add yeah yeah sure sure i would like to add like
[1468] you know as i mentioned in my presentation like three access patterns one was like using a graphql api which
[1476] is like behind a graphql graph orchestrator and that can access data from like the
[1481] document as well as from the graph database second is like the notifications any change data that
[1486] happens in our whole knowledge graph that's gets published to the like
[1492] topics and we generally go for the generic topics rather than the consumer specific topics and these generic topics
[1499] can be subscribed and consumers can read on what is happening inside the knowledge cloud and thirdly
[1505] like uh in the access pattern as i mentioned like a replay so for that what i would like to add is that a lot
[1512] of analysts and other like uh let's say data scientists they need to run queries so we've we built an offline
[1520] knowledge graph store also so that like every night this whole thing gets hydrated into an offline store which is
[1527] like where like heavy queries only for the analysis can be run whereas the live
[1532] queries which are serving our real-time production use cases they are like going through the these three access patterns
[1539] kind of thing so this is how like this whole ecosystem we have work and of course like there are more access
[1546] mechanisms like using widgets like and i mean these are the ways by which we want to
[1552] add it in future so that i mean anyone like can have access to
[1557] our graph within minutes kind of a thing rather than like you know writing their own mechanisms to get insights from us
[1564] yeah anything to add all right so i wanted to
[1569] talk about other parts of architectures is the people aspect right i think um
[1575] i'm gonna hold it on all right well let me just say let's talk about people you seem to want to go say things about people go
[1581] we talk about technology all the time i forget that or my my biggest
[1587] challenge is um finding new talent the pipeline is
[1594] it's not a like fresh talent it's not in a pipeline we heard it from the
[1599] forgot the name of your insurance startup where to find the people i'm right with
[1604] you i mostly in europe these days israel is also a hotbed
[1612] outside of those areas it's really difficult to find talent so my my biggest concern is
[1619] that the pipeline of new talent dries up i'm happy to hear that there's a
[1624] knowledge graph university great idea thank you for plucking it for myself yeah
[1629] of those happy to share any information about that but it really is um you know i think one of the reasons so
[1636] at ek i think we were like one of the largest team of ontologists and have been able to
[1642] through kind of collaborating with a lot of roles that like if people were in-house they might
[1648] be a little bit more on their own and might not be able to have that kind of collaboration and professional development so we've seen you know a lot
[1654] of best practices have come out of that and have captured that as part of the knowledge graph university but it's
[1659] something that we we see as well is that there's it's kind of like a specialized skill set um that is
[1666] is hard to find just um in the industry but what would be great to partner up with um
[1672] universities and colleges such as cornell to have something specialized and and to
[1679] create this pipeline and who are you try what are the types of of roles and what should
[1686] people know that you would like to go higher right now like literally who are you higher who do you need to
[1691] hire right now what what are the skills they need to go have coding
[1698] rdf sparkle data literacy in general like someone who knows data can can be cross-trained
[1705] relatively quick a willingness to learn that's what i'm looking i'm not i'm not even looking for
[1712] do you have sparkle rdf because it's such a small community i'm looking for someone who
[1718] um a data engineer who's quick and willing to learn and to to assess is rather
[1725] difficult um but that's that's the approach we do a lot of internal then cross training
[1732] sometimes it works sometimes it doesn't um but having this that's why most of my
[1738] teams are in in europe because this is where the universities are investing a lot and there's simply
[1744] more people who are already exposed to the technology and that makes it easier to to
[1750] hire gautam how about you how is the people aspect that into it i mean are
[1756] you how's hiring for you and are you training internally
[1762] i think hiring i would say single word like tough that is the part like it's very difficult to find the right kind of
[1770] people for this kind of a domain experience and i mean the current market situation so
[1776] that is something i would say like harry has been a like really a big challenge for us at the same time
[1784] this has given us a very big opportunity to grow like you know
[1789] uh experts within the interview right and that's the culture we have developed
[1795] like you know having a multiplier factor like if we get i mean an expert how we
[1800] can like you know have multiple experts by gaining the knowledge of that person
[1806] within that team so so that that is really a strategy that has helped us a lot so
[1811] i mean and that also promotes a culture of like where uh engineers
[1816] even though they are not hired for specific skill but they get an opportunity to grow their skill into
[1823] this kind of hot areas within the organization and that's like big motivation and like you know binding
[1829] factor and and like you know career growth factor for the people perspective
[1834] so so that way like uh i'm fortunate like you know that we have like a good
[1840] man right-minded people like who have grown as the data experts as the knowledge
[1847] graph experts within the team and that is something like you know i would like to share that yeah
[1854] so we want we want to get people questions in the audience to start thinking about them but so you wanted to follow up or
[1860] no okay well so i want to continue on this people aspect right now because one of the things that i see a lot is is
[1867] as i mentioned before we live in this data first world and everybody is just here i'm setting up my pipelines and
[1874] printing my data but i'm like what aura was saying earlier today is that we need to be able to understand what the data
[1879] means right the accessible data is the bits plus the semantics but a lot of this semantics is is us being able to be
[1886] a bridge between the consumers and trying to unders they understand what the problem is and they're able to
[1891] translate that into the data to the data folks and be those bridges right and we're talking about data product
[1896] managers um and and one of the things i struggle is that we today in the in an industry
[1902] like modeling is a lost art um i mean that's something i see i mean
[1908] you're saying i don't know in the finance world it's different differently but how do we change this culture with
[1914] people about you need to start thinking about it's not just about the data and dealing with the pipelines and the big
[1920] data and and and look at my quality but it's like no we actually have to go start talking to end users and they're
[1926] in and talking to humans is complicated right it's a cultural shift and it
[1931] it seems that it's something kind of scary and people aren't not on board yet that's something i've been seeing myself
[1938] i mean you're shaking your head here what do you i'm curious to go see are you living this this situation that
[1944] i'm sharing right now and how do we address it um i i'm not sure if i if i
[1949] live the same or have the same experience but what i see is that
[1955] if anything graphs make it actually easier to to think about data structures
[1960] and it's not so a lost art if if it's someone who does relational modeling
[1967] that might be a lost art but but if we look at folks today i mean
[1975] all the the the the data engineers developers and software engineers right they're like well no sql right
[1982] yeah here's a bunch of json i'm just data is in there right so you built everything in application but like no
[1987] there's semantics in there but you just don't where is that right and that gets lost and it's something we've gotten used to
[1994] today and i think that's kind of the source of the problem i think it's like a pendulum so it's it
[2001] the the data lakes and the lake warehouses whatever the name is that was the
[2007] on the far end of the pendulum now it swings back to the data mesh paradigm and people realizing oh we have
[2014] to think about data as a product and domain specific little modeling goes a long way so maybe we spend
[2020] some effort to to describe what we have so i see it it swings
[2026] back and and we're going or we appreciate the modeling a bit more um than we did in the last five years
[2033] you've been shaking your head or yeah well i agree agree with all this i i do think that um
[2039] one of the i think the critical role in you know creating a culture where
[2045] engineers are thinking about things in a more user-centric way is having that data
[2051] product manager you know creating a culture of you know exposing engineers
[2056] to the business value of what you're creating and um you know interactions with users i would also say you know
[2063] interactions with modeling people interactions with user experience designers have like
[2069] building out knowledge graphs i mean we talk about the different teams that we like to see when building out um
[2077] when building out knowledge graph products but i think it's really important that there there's a lot of collaboration across those and that
[2082] every everyone's kind of moving in parallel um and that comes from a data product manager i think
[2089] at intuit how are you guys seeing this like do you also how much investments you have in in the data modeling and
[2096] having data product managers and so forth
[2102] uh i mean at intuit perspective uh like
[2107] what it's like a common kind of a team nothing like you know that we differentiate
[2113] these like functions because i mean the need is like you know to wear multiple
[2118] hats and uh like that's how we try to solve for this problem rather than uh
[2124] taking it like in silos where like one person is specifically for this kind
[2129] of a problem right so that's how we tackle it and on the need basis on the
[2134] like you know project basis we form the mission teams and they're like we can put on these hats and solve for whether
[2141] it's a data modeling for like you know for data architecture all these kind of things
[2147] so another thing that we've seen kind of throughout the day is this notion about domains
[2152] how do you suggest that you you figure out what is the first domain you start with
[2158] that's an excellent question let me know if you get the answer
[2167] personally by chance looking at the use case and
[2174] hoping it's it's the right domain to be in okay just luck
[2180] a little bit a little bit of luck yeah i think it's a combination of if you look at you know wanting to provide
[2187] value to business stakeholders and sponsors looking at something where there's
[2193] honestly like where there's data and content available and um in in a format or you know aggregated in
[2201] a way that incorporating into a graph provides significant value that it doesn't
[2207] currently have but also is achievable and something that you can kind of put
[2212] together um in a quick valuable way so i think it comes a lot down to like what
[2219] the resources are and we talked about it before like where there's interest and where there's money and where you can
[2224] provide value to then grow out a more like a culture of building out knowledge
[2229] in this kind of way i i just say it's it's kind of it's kind of lame that we don't know how
[2234] to go do this and i think if we start thinking about like what you're suggesting the chief modeling officer but i'll push it to more of the chief
[2241] knowledge officer that should really be like some cross-cutting kind of uh
[2248] domain itself right that is i need somebody our team to go off and just go talk to people all across organizations
[2255] all they're doing is just interviewing people to be able to go identify what's going on i mean it's almost like this like the
[2261] scientific method is like let me go observe the real world in what scene and i'm like hey i'm seeing this i'm seeing
[2267] these words these words come up all the time they all mean different things and they're all tied to some money
[2274] something's interesting here i think and and that's a good idea like from from my
[2279] perspective it's it's probably also different for every industry like there's no
[2285] it would be easy if it would be oh just zero in on this domain and you're good
[2290] it's it's not that simple and probably for a good reason yeah and i mean as much as i think
[2296] i would like to think that the best domain to tackle first is the one that would like provide the most like value and improvement to users and internally
[2303] into customers a lot of what we're seeing too is use cases driven by risk
[2310] or privacy concerns or governance risks where um there needs to be like a
[2315] centralized modeling on pii because they don't know you know where is pii across
[2321] the organization as there are more and more privacy laws it's important to have that so i think that that's going to be
[2327] like increasingly a driving driving factor you know working worked with a
[2333] medical supplies retailer and they wanted us to start with what is the
[2338] highest like regulated content and making sure that they're that that information was modeled in a in a
[2344] centralized way that they would be able to you know mitigate any risks that would come with
[2349] the that content or data that's being regulated come to think of the um i had a little
[2355] more time to think about the question um for me one of the the litmus tests is
[2363] if the problem is hard enough then chances are i can apply a graph somehow to solve it
[2369] and then i know okay this is this is worth the time to to invest if it's simple or something that's already
[2375] covered with a simple report then probably not a good use case for a graph yeah the analogy of
[2381] the if is do you need an aspirin or a vitamin right you need to find really big pains not something that it's like
[2386] what kind of already works you can make it better gautam how about you get into it like
[2392] how do you all define or identify the dom the first domain of the mains to work on
[2398] so so i think uh there are two ways from where we start
[2404] one is like the business needs that is how we start from and the
[2410] business needs are primarily like uh based on like new kind of use cases or innovation we are trying
[2416] that is from where let's say we have credit karma and we have made them so it came up like you know new kind of a
[2423] business use cases started coming like from that perspective then the other domain is like uh
[2429] within the intuit like we have a very good thought leadership from our architects
[2435] where we look forward for taking the platform to a target state so that is like our continuous journey not being
[2442] settling with like you know one sale kind of an architecture so we keep on moving towards the target state looking
[2449] at the industry trends based on that we like you know it's kind of a confluence
[2454] of the business needs as well as like architect like direction that way we
[2460] reach to the right kind of a domains where we start focusing on and then like once we build it in a generic way it's
[2467] much easier for like picking up like a new kind of problems which are of similar nature in that domain kind of a
[2474] thing so that's like you know our key recipe for like picking the domains
[2480] so one thing we need to talk about architectures and you brought up in gregor and your talk is data mesh already right so for me one of
[2486] the interesting things about data mesh is finding this balance between centralization and decentralization and
[2492] we talk about architectures right they're usually it's like oh they're centralized or who does who manages
[2498] everything how are we seeing this knowledge graph architectures evolving in this balance
[2504] between a centralized and decentralized world so for example i mean
[2509] is everything centralized who how are you how are you managing this this and so that's a question for
[2515] everybody here we go um so the central aspect for us is the the
[2520] model so we say there is a set of of standards and rules and yes we use rdf
[2529] but it's extensible and we we allow others to contribute and this also is a constant
[2537] tug of war if if there are two teams um
[2543] serving the same domain and have different opinions about what the right model is but it's good as long as they're on the
[2549] same using the same standards it's like the free market it's like the the analogy of of the bazaar
[2555] um you set up a few ground rules and then let the
[2561] bazaar figure out how to how to deal with it so that's that's the central aspect of it
[2567] but it should be extensible and open for everyone to to contribute
[2574] you yeah i think that the the architecture i mean it depends on use
[2579] case to use case but i feel like a driving factor should be the organizational like culture and norms
[2585] that there are um where you know some organizations have strong centralized governance and
[2592] um and generally just have kind of a like a centralized like executive power
[2597] and so i think that the arc if if that works then that then the architecture can follow suit um but it could be
[2604] different where if there's if an organization has a lot of trust in different departments or application owners or
[2610] things like that then you can start with something that's a little bit more decentralized but i think in either
[2617] either scenario you know the architecture can push the organization a little bit past where it's going but
[2622] in the end in architecture and the the products that are related to it is only going to be as successful as the users
[2628] who are operating it in so i think you have to be kind of move within what the organizational culture is so great you
[2634] said something here very important which is um the model is centralized but extensible you want to set a few ground rules
[2640] let's get more specific on this what exactly is centralized with respect to the model and what are those specific
[2647] ground rules so centralized is the glossary of terms so when we talk about
[2653] the application then there's only one application when we talk about a trade
[2658] or a loan then we have a central glossary where you say this is a loan a
[2664] loan is a loan but you can have specializations of it but the the um the
[2670] super class is alone and we reserve the right to say
[2675] we define it and here's a place where you can look up what a loan is
[2681] now there are others saying you know what rdf screw you i'm not interested we say that's fine
[2686] do whatever you want but if you talk about a loan you better refer to it so use json schema or json ld to say this
[2694] data point that i have here is alone and by the way look it up there so you have the definition in one place
[2700] how big is a model that is centralized in your case we have a couple thousand classes
[2706] so you've centralized the development of a couple thousand classes and that's
[2711] what people either use that or they can extend that if they want um yes they refer to it it is like a schema.org okay
[2719] and um a thousand seems like a lot or or it's a big number is it big or is it not big i
[2725] mean compared to some of our uml models it's small
[2732] and how long in your case did it take to get to that to that thousand i'm two and a half years
[2739] damn i see people kind of oh okay interesting all right
[2745] is that good is that bad i mean i don't know but it's it's a it's a good data point right it's a bar to go set in here
[2750] right actually so to expand on that like what is what was the process in those during
[2756] those two and a half years what was the culture to get there like i
[2761] don't think everybody walked in the room and they're like yep we agree and we keep going right so yeah and we still
[2767] have a lot of discussions um and it doesn't mean that everyone follows so that's our our group weight guideline
[2774] but there are pockets kingdoms who are independent of it and that's
[2780] okay we deal with it but we
[2786] allow the application or not we encourage applications to um contribute to the firmware fabric
[2793] that's how we call it basically hook yourself into the firmware fabric share your data
[2799] as far as you're comfortable with it but share it by explaining it and use the
[2806] firmware fabric so that others or others can compare apples and apples
[2811] that's our our sales pitch it's an ongoing process i'm not sure if you ever
[2816] if we ever get to 100 probably not um but it's one way it's it's
[2821] definitely better than our current situation no and i i subscribe with this i mean i mean the world is full of chaos and we
[2828] can't expect to be able to organize this chaos so we need to enable and have some friction and at the end of the day if
[2835] people disagree well let's go figure out why they're disagreeing maybe we can come up with an agreement or not i think this is i like
[2841] to call this uh let's enable some intellectual friction uh and and at the end we may agree or we figure out
[2848] we just have to live in different kingdoms for some reason uh but so how is this an intuit like
[2855] we just heard at ubs they have a thousand concepts centralized took them two and a half years to get there
[2861] what does it look like at intuit yeah i mean i think to it like
[2868] i mean we of course like we try to centralize things uh
[2873] for one primary purpose that do not want to have clones like you know for a specific thing
[2880] uh like within the organization because that's like a big challenge like if the
[2886] communication flows are blocked and similar kind of a technology or
[2892] like thing is developed by two or multiple teams kind of a thing and then we have a
[2897] clones and a problem of like who to like you know stop and how to manage and it
[2902] involves a lot of cost also so we have a like concept of a city map kind of a thing using that
[2909] we have like a centralized kind of a city map but like it's a decentralized
[2914] implementation like i mean within that city map everyone like gets their own area domain where they can go build it
[2921] architect it kind of a thing and like you know make it like a durable capability that
[2927] can be used by like the rest of the like you know organization so that's the like
[2932] solution approach that we have taken uh for our intuition
[2938] so we got 10 minutes left are there questions people have okay okay i got so
[2945] i always like to do this the magic wand exercise right so magic wand you got the beautiful knowledge drive architecture
[2951] it's working and everybody's like knows how to go use it what are the use what are the
[2956] applications the use cases that you think like this is this is the future because it's
[2962] they're they're using the knowledge graph question for me for everybody
[2971] what is the one thing i mean i i think every organization wants
[2977] google you know every organization just wants the knowledge panel that you have in
[2982] google that you can look up any concept any question um you know i think that that's the kind
[2989] of experience that people want in every sense of their their world i mean i i
[2994] work with some clients that just said yeah you know our intranet doesn't work well enough so we just use google you
[2999] know it's public enough or you know it's large enough that a lot of our product information is just on the web um so you
[3006] know there's so many different applications that google has modeled but that's that's where i think
[3011] organizations want to be i want to be that way in my daily life you know right love it so future is every organization will have a google knowledge group panel
[3017] how how do you see it um so i have freedom for my magic wand yes magic one
[3024] um so we call it the situational awareness what i want is to know every data point
[3031] every network connection every piece of data in in the firm where is it
[3039] what does it mean who's using it who's accessing it
[3045] that is one of our goals and and what we're planning to do is to apply
[3050] some graph ml magic we don't know yet how to do this but that's our goal to have full
[3055] situational awareness what data is where when who acts as it um what does it mean and and end
[3063] all right and go to you you got a magic wand what are you gonna do with it
[3069] uh i think if we get a magic wand i would really love to get the best people in the industry and
[3076] that's how like you know grow a culture like you know through which we can like solve this problem like and
[3084] continue to like grow this at the same time like you know bring back the expertise and knowledge of those
[3091] people through these like conferences back to our technology world so that
[3096] like we don't keep it like as a hidden secret but share it like broadly with that rest of the world like that all
[3101] right so magic wanted to actually go magically get the people we need that we don't have right now all right we got a few minutes and i'm
[3107] sure questions who is all right go one one two three four let's see be quick
[3115] crisp concise yeah on the topic of graph evolution graph maintenance
[3121] um what are the key architecture principles to put in place like if i make a parallel to apis i mean
[3128] building an api is simple building an api that meets slo slas high availability
[3133] cost effectiveness in the cloud that imposes some architecture choices to do so any any thing that we
[3141] need to think about as we build the graph for evolution of the graph and maintenance i mean this morning was a
[3146] question about how do we manage materialize links that we create based
[3153] on insight or our inference
[3158] question for me the um so one thing that we apply there is what we call data observability
[3166] so we're looking at the same data over time and have basically a watchdog and it's
[3171] if a data set if there's any deviation from what's usually expected
[3177] over time at least we get an alert but it's it's
[3183] it's a hard problem and i cannot claim that we succeed but this is our idea that we we need to have tooling um
[3192] that supports us because doing this um on a on a manual basis or just just
[3198] hoping that things don't change that doesn't fly
[3204] uh quick question in the use cases that you have encountered um do you have i've
[3209] seen a need for multi-hope graph traversals beyond two hops or something like that
[3217] yes absolutely yeah and i think it depends on the you i one use case that comes to mind was a deterministic recommender
[3225] that was doing like kind of traversing relationships i think we max out at
[3230] maybe four relationships with that um to try to connect um like unstructured
[3236] content based on topics so it was traversing topics but also metadata like
[3241] user profile and like other kind of like person type information um but yes
[3246] absolutely uh yes hi everyone uh al baker i lead
[3252] the implementation team at stardog uh one big fan of your work since your original phd came out
[3257] i do wanna take one issue that data modeling is dead though in that um uh
[3266] so uh kind of the question uh for gregor and i'll kind of get there in one moment
[3273] and that is i always view it as database normalization is perhaps the most critical skill
[3279] uh and all the questions on you know how do we hire and uh
[3284] looking at that and kind of where that conversation went i suspect a lot of the challenges in recent years has been some
[3290] of the schema on read type systems and you mentioned three data lakes so i was hoping to give us some commentary on
[3296] uh some of the challenges there and if
[3302] the the modeling and kind of trending towards higher levels of normalization within the graph
[3307] is something that you see within your implementations let me just play it back to that i'm
[3313] sure i understood the question and so do you mean that the
[3319] that there's no emphasis on data modeling that uh
[3325] is there any difference from a traditional database l being elevated into the graph versus some of the new
[3331] things like data lakes where maybe the schema was not modeled the same way as it has
[3336] been in the past like you don't fire up erwin to model s3 and upgrade your like you would
[3343] oracle and stuff like that i would um i think the the
[3349] a lot of the data lake implementations missed completely data architecture to begin with
[3356] just dumping all stuff into great technology doesn't help i
[3362] compare our graph initiative more with the classical
[3367] relational modeling 20 years ago same rigor applies
[3375] we have a dedicated modeling team that we're about to dissolve
[3383] and the reason for this is not because we don't need modeling we realize that having a
[3388] dedicated team is almost like an ivory tower so we do instead we embed all those
[3395] modelers within implementation teams and that is something that works out quite well for
[3402] us but it's definitely an emphasis is on modeling for sure
[3408] related to this uh hi justin beck 0.72 um how do we get
[3414] vendors of data to actually become enablers to this like the bloombergs and
[3419] factsets and and you know duns and bradstreet you know they they give us data dictionaries and old excel sheets that
[3426] have you know textual descriptions of things but no standards often
[3432] um you know we shouldn't have to remodel what a company is or what a person is or
[3437] something that if the vendor selling that data has a clear definition how do we how do we encourage vendors to
[3444] actually provide this that the new data dictionary of the future everybody is passing semantic models instead of uh
[3451] excel sheets of you know simple glossaries
[3458] excellent question um sorry do you want it i have an opinion you want a magic wand
[3470] so there's bloomberg people here so how about we wrap up that question saying let's all talk to them right now there's
[3476] some bluebird okay
[3481] all right well it's four o'clock i want to wrap it up as as always as we do in our podcast we give our takeaways i've
[3486] been taking my notes here so embrace diversity there is no one-size-fits-all do we need a chief
[3492] modeling officer or what i would prefer a chief knowledge officer what are we not talking about today
[3497] temporal entitlements permission to access data identity resolution by domain but with shared infrastructure
[3503] different domains look at identity resolution differently let lessons learned solving the wrong problem and the money dries up so we
[3510] need to focus on that not everything needs to be in the graph from an access perspective api first graphql but
[3516] depends on the use case a lot of caching's involved people we talk a lot about people we're
[3522] finding people right now is in europe and israel you're saying but we need to go educate hire more how to identify the domains a lot of luck we'll go find the
[3529] use cases regulatory find those big pains between the centralization decentralization the models are being
[3536] centralized extensible using the same standards ubs has a thousand concepts built over two years into it has a city
[3543] map what does the future look like uh we want the google every company
[3548] should have a knowledge graph situational awareness we want to know everything who uses it what uses it and gautam would use his magic wand to go
[3555] hire the people he actually needs and embed modelers and implementation teams that's the summary of this big panel
[3562] and with that if you like what you heard i do this every week on catalog and cocktails so i'm actually going to record it live
[3568] with front swan an hour and you can listen to it every thursday so that's my my shameless plug thank you
[3574] very much the panelists thank you thank you thanks everyone thank you [Applause]
[3582] thank you very much
