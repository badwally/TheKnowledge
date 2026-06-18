---
schema_version: 1
id: yt-e4D0CH8eiv0
type: youtube
title: Building knowledge graphs in the real world. Expert panel at Connected Data
  London 2018
url: https://www.youtube.com/watch?v=e4D0CH8eiv0
authors:
- Connected Data
ingested_at: '2026-06-18T01:38:16Z'
content_hash: sha256:6574fa55ceab06130211ac7d96243887e2d1b7e7f38cd49ccb4bf89be5b4be70
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Connected Data
  channel_url: https://www.youtube.com/@ConnectedData
  duration_seconds: 1973
  caption_track: cached
  snippet_count: 326
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:16Z'
  user_correction: null
---
[0] Introduction
[6] hello everybody so we just had a fantastic talk talking about one
[13] real-life knowledge graph being used in practice and so this is a this is a
[19] panel about really deploying knowledge knowledge graphs and we have some great
[24] speakers for you today I am actually not going to introduce them and the way we're gonna because you have a nice pamphlet in your thing to tell you the
[31] background of each of our speakers what I'm gonna do is ask each of you to present a little bit about your
[38] knowledge graph in practice of your company and so we'll start with okay so
[38] Presentation of Text Journal
[46] I work for text journal text journal is a provider of semantic software for the
[53] HR and equipment domain so we serve the people who and the companies that need
[59] to understand people's profiles resumes CVS and also vacancies so practically
[65] the supply and demand side of the labor market and we want to match this together so in that context the critical
[72] aspect of domain knowledge that we need is knowledge about professions and skills and qualifications and how these
[78] are related to each other so we need to know what professors are out there how
[83] they are expressed in in in text that's very important in different languages if
[90] they mean the same thing or if they are actually something different and how they're related to each other so it's a very conceptual knowledge graph and the
[98] main technology we use his property graph for representing that and the main applications of it is for semantic
[105] parsing so we perceive is a magazine we abstract entities relations and for search for expansion and semantic a
[112] matching hi I'm not a severity my work
[112] Presentation of Refinative
[119] I'm an information architect in refin ative which was previously known as
[124] financial and risk business of Thomson Reuters so we are actually a data
[130] company and we have a huge amount of data in our knowledge graph that fits
[135] actually many products many services one of these products / my D that Niall had both referred to
[144] earlier so this is a free product we also have another product which is both framework my colleagues Africa rel will
[152] talk to you about it in a while which is an enriched graphic more enriched than
[159] the perm ID which is a commercial product so we have a as I said a huge
[164] amount of context so we maintain what we call a metadata repository every
[171] publisher in our company must register their data sets in that metadata
[177] repository they should put some metadata around it so provenance who is the best
[185] contact for but also they can express the semantic meaning of their data set
[192] the different kind of distribution how are we providing them how these
[198] different syntactic formats can represent it in the semantic meaning and
[207] how so people can from this metadata registry people the consumers can
[213] actually discover the datasets and can understand how they can use them and
[218] they can even track provenance and lineage so how is it how is this data
[225] set related to other data sets as well so this metadata registry is built on
[230] AWS which uses Neptune as a triple store we support by temporality in our data we
[239] do it with named graphs we name graphs are actually used also to support
[247] versioning in our ontology and actually I want call them ontology so will call
[253] them vocabularies because they are mostly utilizing charcoal because we use these schemas to actually validate also
[262] the data as they enter our metadata registry so we have 100% data quality
[262] Presentation of Solando
[270] hi so um my name is Katerina curry and I work I'm an oncologist at solando and
[277] the knowledge graph we have at solando is also really a vocabulary for fashion to drive use cases like search
[284] understanding and to build a slightly more dynamic browsing experiences for
[289] our customers we are also using Amazon Neptune we're using named graphs
[296] actually was interesting to hear using versioning we haven't gotten into versioning yet certainly to explore that
[303] but we use named graphs to write implied triples have them in explicit form so
[310] that applications that are built on top of the knowledge graph and the ontology would serve more before mentally hello
[310] Presentation of dbpedia
[321] yeah I have so I have two stories one of the history of dbpedia and one of the the current stuff we're doing so TV PDR
[330] is actually one of the oldest knowledge graph there is so we the first version was published in two and twelve years
[336] ago and it was kind of like a knowledge graph before the word knowledge graph was even pushed by Google so the main
[343] thing we did was we extracted the knowledge from Wikipedia and hosted us as a data place and ran free publishing
[350] for everybody and this data was immensely useful I think one of the most common use cases is to enrich search for
[359] example the relation between Beyonce and Ivy Park is also in Wikipedia so it gets extracted by dbpedia so you kind of like
[366] get this for for free because you can just download it and it was so it was immensely useful and kind of like
[372] community formed around it that improved the data quality and worked on this for years and companies included this into
[380] into their their data base but so after
[385] wherever we have a fairly large community and it's very diverse like you can you mention that everybody has their
[391] own data to care about and everything and we're still two years ago we started
[397] this discussion like we're sitting kind of like all in the same boat and that we
[402] want to work with data want to build these knowledge graphs but the collaboration between different
[408] community members are really is really difficult so we changed our mission in a bit or refined it so before that it was
[415] put useful data on the web and people download it and now we have the slogan that we provide global and unified
[421] access to knowledge graphs so that in the end you can collaborate across organization borders so this
[430] collaboration comes in two flavors so one is the the data curation part so in
[435] the end the data you have somebody else has the same data and you actually want to curate it together because it's more
[440] cost efficient so that's goes for libraries and public research projects
[446] and everything and the other way of collaboration in the business side is more like the supply chain management so
[453] you want to get data from somewhere else and integrate it into your your product and this is not this is still not
[460] working so well so now we are changing from the content provision of the free data we still do this but we are
[466] building like a platform which is called the data path which which can be used to connect knowledge graphs across
[473] organizations and reuse data and provide feedback mechanisms and more reliable
[478] supply chains lots of different
[485] different perspectives interesting common set of technologies I think one
[490] of the things we wanted to do in this panel is giving you a little bit of a feel for what it takes both technically
[496] but more importantly organizationally to build these knowledge graphs so maybe I'll start with you Panos how what is
[504] like the key thing you need to do to get started with building these knowledge graphs from an organizational
[510] perspective why so define a use case
[510] Define a use case
[518] that is quite specific so you need to avoid I mean it's good for for selling
[525] into clients but you need to avoid hype things and try the things you don't want to do it just because it's trendy but
[531] but because I think the Rina mention how she got buy-in from her VP
[536] from upper management so for upper management it makes sense only if it makes money so you need to find a
[542] particular sub case that will get you a quick win and proof of concept that will
[548] show the viability and will buy you resources to continue because as I like
[556] to say knowledge graph is not one single project it's not it's first of all it's
[561] not just the artifact you build the artifact that you built all the process around it to support it to support its
[567] its lifecycle if you only build the artifact and you leave it like that it will it will die in a while because all
[574] the knowledge will be obsolete so start with why you want to build the knowledge
[579] graph be very specific and then try to find actually allies find doesn't matter
[586] so much the technology I mean it matters after how matters before after the what
[592] for me that's the great talk from you on
[598] the why in in Thomson Reuters or affinity what's the why the why for the
[611] metadata registries as I said because we needed some somewhere to register all
[616] our datasets and the consumers be able to find them but also to understand how
[623] can they use them so we had a very specific case for the ballroom where we
[629] provide the data in RDF again as I said my colleague will explain more but it's
[636] just another format that can be automatically integrated so it depends
[642] on the product fantastic so can we dive into so we've talked
[648] about a little bit about the why as the important part of why you shouldn't fill these knowledge graphs in the first place I'm just interested in what do you
[654] see as your current challenges in your your knowledge construction and maybe
[659] we'll start with you because you know we're you know you have your 20 concepts or so and you're building it out and you
[666] should in performance so what what challenge going forward mmm the challenge I mean currently we have now hundreds of
[666] Challenges going forward
[673] concepts and 20 are the ones that are driving revenue at the moment there I
[680] think there are a lot of challenges one is that actually what would be the next use case to do because there are quite a
[686] lot of use cases like I would love to read dbpedia and do the Beyonce inference from there but then how many
[693] Beyonce's do we have in our search market getting endorsement for that use case necessarily so so this kind of
[700] capabilities that we could build we do need a strong enough big enough use case you actually start investing in it and
[708] start investing like developer time to it so that's it's like really organizational business driven driven
[715] decisions when you're a company that makes money for stakeholders and so but
[724] the yeah I would say that maybe the other colleagues have more there are others as well yeah the organizational
[731] business reasoning part and Sebastian from dbpedia this point of view what's what's really challenging you as you
[731] Data challenges
[738] move to this data challenges the cost
[743] right so solando can carry the cost Thomson Reuters can carry the cost you say I would make a two year project
[749] build a knowledge graph of course the rewards are quite good but if you don't
[755] have that resources then data quality for example is really really bad it has
[762] a bad curve because it follows the law of diminishing returns so you increased you have to increase
[767] the manpower but you cannot the increase in data quality or quantity doesn't
[773] increase with the same scale right so you invest more and more resources and then you add only 5% of data quality for
[780] example so there it really makes sense to pool across across organizations
[787] right because especially in pre competitive data so for example the list
[793] of singers list of TV shows list of authors list of publications so this is
[799] all publicly available information and you should outsource the maintenance of it like work together with other people
[806] because unless you have of course if you're a very big company like Google you can do it in-house and curate it
[813] right but you need to we need to break down the cost and make this this
[818] commodity data are cheap and that's why we need something like synchronization
[823] mechanism across the organizations so are each of your knowledge graphs kind
[823] Knowledge graphs
[828] of riffing off that consuming public data you you said you want to consume public data eventually maybe in the
[834] future but it isn't in text kernel are you consuming public data sources to
[840] help out you know we do consume them but not in a live version so when every time
[840] Public data sources
[849] we want to make an enrichment we look for any type of resources that may contain the knowledge this can be the
[855] BPD it can be the Escada machine memory stock it can be other web resources but
[862] usually one problem is the heterogeneity of semantics so what we mean as a skill
[869] for example convene within in the pedia in different things so for example can
[875] be we can take the little domains that's one thing we want or the types of medical areas things like that so we
[882] need to do mappings and this doesn't make sense to be live it's it's a one-off project every time that's hard
[888] work and so far we don't have any incentive to keep live links to the
[893] other or maybe no we have only two for ESCO because ESCO is going to be used by
[899] the employment agencies of its country so there we do have incentive because we
[905] want to be interoperable with them let's
[905] Questions
[917] see I have one or two more questions I had some very interesting questions all of you use github to manage your your
[924] ontology vocabularies or or get so you use github to help manage your ontology
[932] dbpedia as well the EBP okay interesting very interesting we did
[938] that as well at Elsevier I wanted to open it up for questions so I have one
[945] more questions and if you you have questions of mine just to raise your hand and we'll we'll run around the
[950] audience to start getting some questions but before we before we get there this
[959] is technical let's talk about rules and inference so of a big an interesting
[968] thing is where do you see the role of inference are you using rules inside
[974] your knowledge graphs or is it just purely an entity kind of relation kind of style knowledge graph okay I have
[974] Role sensing
[982] been working in the industry for many years I'm not working as a researcher or
[988] in university so the open world assumption was a barrier for us so the
[996] latest years short of has come to my rescue and we're using Shaco for
[1003] describing our ontology but also we are using it as a role
[1010] sensing to create information in a controlled way so for example if I want
[1015] to discover if I want to create new information if I was using inferences it would be uncontrollable all the
[1022] information that you can get based on our actions and this is not something
[1027] that can work in the industry you want to create and be totally in control of the new information you will
[1034] have in your triple store so we actually have worked with rules but also in my
[1039] previous job in in top quadrant as a semantic Solutions Architect
[1044] we were using spin rules now we are using charcoal rules in in riffin ative
[1051] so in general we don't use inference anymore inference rules like the ones
[1051] Inference rules
[1059] that come from our the Ethne or all actually not supported by Amazon left you
[1064] which is also very interesting um maybe it's there for a reason I remember that back when it was placed
[1071] craftsmen the place cart developers weren't really into RDFS domain and range at all and also talking like not
[1080] seeing the benefits there we are also not implementing that we're not making
[1086] making use of them I was considering them in the beginning and open world assumption was really hard for my
[1092] colleagues to understand and to work with so now this like example of us
[1097] reducing latency has been a very practical set of rules that are application-specific
[1103] that we maintain and so we're not using the kind of rules language to define
[1110] those although we could but we are just using other other scripts to do it so
[1110] Open world assumption
[1123] about the open world assumption also in our case doesn't work we don't want to have this kind of inferences it's not
[1130] this kind of case with mostly like one constraints as well as with respect to
[1136] the standard inferences that although RDF gives again we don't implement it in the sense that every application has its
[1142] own peculiarities to give you an example when we make a search school when we
[1148] want to expand the search query one could say that if you are looking for a term for a concept then all these more
[1154] specific concepts should be expanded expand or all its synonyms could expand that's not always the case why because
[1161] for example some of the synonyms are just too ambiguous or two that really causes a problem instead instead of
[1167] helping us or you really don't want to when you are looking for example for
[1174] someone who knows no scikit-learn as a toolkit you don't want some it's very
[1180] specific so you don't want to generalize with someone who knows machine learning or something else like that so we any
[1186] type of inference it's incorporated into the applications million products
[1191] interesting Thanks hey and so that brings up our first question over there
[1191] Maturity of knowledge graphs
[1198] it strikes me that your knowledge graphs are relatively mature you're over the kind of the hump of critical mass
[1205] adoption if I was to put you into an organization where they had no knowledge graphs what steps would you take and
[1213] what tools would you be using with only
[1213] Use cases
[1221] what one experience of that once at solando and having learned a lot on the
[1227] way the first thing probably is to to really make it really specific of what
[1234] the company needs most in that current time just to make sure we're talking about use cases all the time and I guess
[1241] we're talking about why you start with why but really for that specific company first be very clear on the Y and then
[1250] technically whatever is needed so so sometimes property graphs might do the
[1257] trick more than RDF graph or or not even RDF but something else so so so the next
[1264] make make that choice but it really starts with the why yeah in general you
[1264] Why
[1271] should see the knowledge graph not as I mean okay there are cases where it is
[1277] but normally you can use the knowledge graph not as a replacement of your current infrastructure but as a valuable
[1283] addition so it helps to keep like the
[1288] knowledge in ontology x' and in in mappings maybe and but keep the normal
[1294] infrastructure itself you can even compile ontology stew Java for example so you have a real performance gain
[1300] there but it's good to manage this this semantic layer separately and then how
[1305] you achieve this is that you pick certain use cases which are very interesting and you build this parallel
[1311] infrastructure in a prototype and show the value and that gets kind of like the
[1317] tension so so on the end this because dbpedia was kind of like the semantic access to Wikipedia
[1322] so to submit that the cemento fication really brought benefits right and that's
[1328] also one of the reasons why Viki data's is there now because it was a good it
[1333] was 10 years long it was a good showcase and then they finally came around to make in wiki data all right so that's
[1340] making the prototype throwing the valued in parallel to the existing infrastructure is a low-cost investment
[1346] actually so the answer to the question
[1346] Ontology
[1354] is you need to be a detective you need to be investigator I mean just go around and talk to people you will realize that
[1361] many teams will be already using some type of ontology does they don't call it like that it can be a simple file with
[1369] some keywords it can be an XML that contains a relation that is not named
[1375] but it's a relation there and you've also realized that when you talk to another team they have already also
[1380] using the same know--let's but not the other teams so they use their own version so it's an investigative process
[1389] that unfortunately doesn't end you I'm still I'm two years already in the
[1394] component and I'm still good surprises about hidden knowledge about how knowledge these use different
[1399] terminology what what people used to call a synonym that is not a synonym it's a it's a hard work but you need to
[1399] Summary
[1407] do it so just summarize know your why find the showcase and be Sherlock Holmes
[1415] okay so do we have other questions from the audience if I may add yeah this question I have seen I have witnessed
[1415] Trends
[1422] trends in the different industries so I have seen oil and gas industry companies
[1429] using Semantic Web just because they want to be compliant with iso 15926 which is a very important standard in
[1436] this industry so this is where you should start if you are in that domain farm and life sciences have for a lot of
[1446] years now have fully developed ontology like sno-med or mesh so they usually
[1451] farm and life sciences companies what they do is they take these huge oncology's they slice and
[1458] dice it because it's it's hardly F and it's very easy to do it they gather in their knowledge graph their own
[1465] information around it and then they are using these parts of the ontology for
[1471] machine learning techniques so there are other industry consumer goods where they
[1478] are using the knowledge graphs because they want to capture compliance so for
[1485] example I have a product but this product is consist consists from any
[1491] materials and molecules I cannot ship it to one country because one molecule is permitted to one country
[1497] but not permitted to the other all this flexibility that RDF offers can help you
[1504] describe all these things and also in banks I have been in projects where
[1510] they're using graphs for lineage so and regulation compliance as well for
[1516] example I have a value in my report where I will trust me to four f-14 for
[1523] example in u.s. so what did his value in this report came from do I need to hire
[1529] 1,000 consultants to find out where this value came from no if I have a lineage
[1535] and RDF lineage and I know where this value was affected upstream or if I
[1541] change this value in an asset what is the effects downstream so there are some prominent use cases now
[1541] Master data management
[1549] fantastic thank you other questions I so
[1554] I'm interested in using building a knowledge graph for use case of master data management and one of the few of
[1562] the important things there is being able to keep track of data provenance meditator by temporality that kind of
[1570] thing and neither the idea of standards or already vendors out there I'm aware
[1575] of sort of handle this sort of stuff natively and I was wondering if there
[1581] are any insights into how to manage that sort of stuff so managing lineage
[1581] Managing lineage
[1588] managing so for provenance there is a very nice standard it's the probe
[1588] Managing provenance
[1594] ontology we'll use it in refin ative but I have used it in many products for
[1600] lineage and reference data you're pretty much right you need a data governance tool and actually these technologies are
[1609] very well candidate for a data management tool well you will need to have notification
[1615] every time something changes people and teams need to be notified you need to
[1620] track history so it's better to manage the reference data assets or master
[1626] entities with a nice data governance to
[1634] add to that that I wouldn't actually know because we built mainly most of the
[1639] governance tools and data studio tools ourselves but that's again like you said that our company can invest in that kind
[1647] of work we do very applied work but I think more and more we see this on the
[1652] hallway and with the sponsors of connected data as well there are more and more good tools that would make it
[1658] easier and nobody is offering protegé for you to so the way we publish so we
[1671] changed we improved a bit the way of publishing now with TPD and it's very
[1677] technical the data bus the data bus has a maven plug-in in the sense that you
[1683] can treat there is a similarity between data versioning and software versioning
[1688] yeah but they are not there are differences but there are similarities and then you need to change something
[1695] anyhow we develop the data bus maven plug-in that allows you to publish data
[1700] and the same where that maven publishes software artifacts and we also have a
[1706] triple store that collects this metadata and acts as something like the maven central where you retrieve the software
[1713] artifacts so this is software you could use for free it's it is made for
[1720] software releases so it's not maybe on a daily basis like a good model for data there are other
[1726] tools for this you can search for them quit if is one store 1 store that does it so these are track really the
[1734] individual commits while the database may be plugging more managers release
[1740] releases of the versions yeah so that's a bit of a difference because you need
[1745] to handle the volume right so cannot publish a snapshot it's each second right so that that's all fantastic so I
[1754] think we have time for one more question
[1754] Domaindriven design
[1762] sorry man so I'm familiar with a domain
[1767] driven design where developers they they have communications with domain experts
[1773] and many other people and inside the business they discover domain objects
[1779] value objects all sorts of processes within particular context and then map that all out inside of code eventually
[1785] they develop some ubiquitous language and most of this sounds very similar to
[1793] ontology and what knowledge graph are trying they're trying to accomplish nothing not instilling an autograph but
[1799] more ontology z' what happens to applications when when the like have to
[1807] or when they implement ontology z' i don't even know if this is a right
[1812] question to ask but I just yeah that doesn't make any sense at all yeah yeah
[1812] Applications
[1820] yes yeah and then like we're normally or at least why I'm used to where these
[1827] applications all these processes are encoded in acting just code instead of instead of yeah exactly yeah so maybe
[1836] we'll simplify the question with how do your applications interact with the
[1841] knowledge graph so that you provide maybe yeah let's start and go around and that'll be the last question yeah so
[1841] How do applications interact with the knowledge graph
[1849] there are many ways it can be done and it can be in a more or less disruptive way so for example what we do
[1855] external is that we just make it custom exports so we do have our centralized
[1862] knowledge graph and then per application we give exports of the knowledge in a format that they were already used in
[1869] our case it was it was XML so it can be
[1874] done in neutral you don't have to tell them now you know you're going to make Sparkle queries directly or cipher
[1880] queries or whatever that's one thing the other thing that is important for me is
[1886] that you have to convince your developers if you like or the product owners or etc in some cases to change
[1893] their algorithms in order to take advantage of what the knowledge graph can provide I mean the content for
[1900] example if you are doing entity extraction and you're not doing the Samba Gration the knowledge graph can
[1906] help you but it's not enough you need also an algorithm and this algorithms to be developed by the developers so you
[1912] may have the best knowledge graph but if your applications don't take advantage
[1918] of its power you have nothing so it's not only I'm making a fancy knowledge
[1923] graph and it's enough that's anything else to add given that we're running out
[1923] Im making a fancy knowledge graph
[1929] of time rapidly maybe just both those we are
[1929] Microservice infrastructure
[1936] doing yes and I was talking earlier about a micro service infrastructure and
[1941] also the bother talks on on having micro services on top of the graph so api's
[1948] are easy to understand it's it's not as Jason and API is using those and putting
[1956] ApS on top of your knowledge graph it makes a lot of sense and then you can work under the hood on how and how the
[1962] data is served or maybe this API is implementing an algorithm that always gets smarter with the knowledge graph
[1968] all right let's thank our panelists
[1973] I think
