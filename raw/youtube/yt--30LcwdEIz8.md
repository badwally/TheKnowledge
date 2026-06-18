---
schema_version: 1
id: yt--30LcwdEIz8
type: youtube
title: Semantic Layers w/ Artyom Keydunov & Pavel Tiunov (Cube.dev)
url: https://www.youtube.com/watch?v=-30LcwdEIz8
authors:
- Joe Reis
ingested_at: '2026-06-18T01:38:10Z'
content_hash: sha256:d1b31739d28a0c986de3061d77c22d65df5f3573bfa9952f57ce63a0e4f776ca
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Joe Reis
  channel_url: https://www.youtube.com/@JoeReisData
  duration_seconds: 3351
  caption_track: cached
  snippet_count: 553
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:10Z'
  user_correction: null
---
[0] Intro
[1] happy Monday how's it going everybody [Music]
[8] yeah it's pretty cool so yeah you're in Salt Lake again surprisingly enough uh icon among other things yeah yeah how
[15] was pycon yeah yeah
[21] yeah I think I went and got my badge and then I just had a lot of other things going on so it happened it's almost
[27] worse it's in your home City because you're not awake yeah yeah exactly so cool uh yeah enough
[34] about us uh so we got uh the co-founders of uh Cube on the show um uh Pavel and artem so for people who
[42] don't know who you already want to give a quick intro uh yeah yeah sure
[47] um thank you for having me today my name is artem I am one of the co-founder and authors of uh Cube uh with Paulo we
[56] started keeping 2019 is an open source project and uh building building it and
[62] that so super excited to be on the show today I'm co-founder Institute Cube and
[69] basically yeah I was building that from scratch a lot and that's how we landed
[75] this Cube and basically uh I I built the
[81] vast majority of a cube in the early days and still building it right now
[86] yeah that's cool we talk about a bit I'm very curious like as a just a um a
[91] founding CTO especially like how you balance uh uh you know maintaining the project while trying to focus on the um
[97] you know the productized version of that I suppose yeah but but yeah I mean so you know we're here to talk about semantic layers it's it's a it's
[104] becoming a popular term uh I think it's also a term that I sense is
[109] is maybe consolidating but I feel like there's still maybe different definitions of what a semantic layer is
[115] do you guys want to uh throw your hat in the ring and uh give us your take and what a semantic layer is
[115] What is a Semantic Layer
[122] what automatic layer is and is not I think is a maybe a good way of framing the question so yeah go for it
[129] yeah I think you're right it's the consolidating maybe like a two three
[134] years ago we we saw some explosion of like last wave last generation of
[140] companies trying you know like to build some multiplayer um and we saw a lot of terms like
[146] metrics layer metric store Atlas bi and semanticleer 2. so and it's been I don't
[153] know like maybe four or five companies that like uh raised to see drought at serious a and Cube was one of them that
[160] tried it you know like to go after that sort of problem again it's not like that
[166] is a first wave right we have companies like at scale and then if we look uh even uh at older generation business
[173] objects in to some extent we can consider in order to base multiplayer as well but NLS sort of a generation last
[180] wave has been a few companies like a gen Cube super gray and transform data and few more and yeah funny enough like
[187] pretty much every company used a different term um I think just because
[193] it's still people try to understand how the semantic layer should look like you know like what features it should have
[199] and where it should you know like provide more value less value where it has more features for example some
[206] people would called it metric store uh you know coming out of companies like
[211] Airbnb where they have successfully implemented you know like the metrics repositories and they uh maybe over
[219] indexed a little on like matrix definition you know like like a V key for metrics all of this so that's you
[225] know like was one of the versions of semantic later where like more Focus was put onto the technology the metrics how
[230] you define them how data consumers can search for them all of that um other companies you know like uh Cube
[238] use determine headless bi because we came from the uh like more like embedded
[244] analytics side of the business and we thought Lincoln bi is commonly used for embedded analytics right and then you
[250] have headless Bia because we don't give a charts essentially right you're like given API for you to build in better
[256] analytics that's why we prefer the term headless bi um but then again now it's all like
[262] consolidating into semanticleer I think which is good for like industry because you know like it's easier for for uh
[269] practitioners to sort of navigate navigate the space less terms just more consistency
[277] yeah yeah because I always get confused I don't really get as confused but I know
[283] back when everyone's talking about metrics semantics uh Lord knows what else like I was just like I I'm clear on
[289] like which one is which um you know as you point out Airbnb had its article that you know they they
[295] built a metric store many many moons ago and it was amazing and I'm like that's cool um what's the difference between a
[295] Metric vs Semantic
[301] metric and a semantic um it's like a right I don't know it's I'm glad that at least
[307] um so hopefully consolidating on terms but uh yeah I don't know what were your thoughts on any of this yeah yeah kind
[313] of the same thing I think we're starting for a long time this was just kind of a
[319] it was sort of a buzzword for a while and I think now it's turning into a real clear thing about what this exactly is
[324] in fact do you want to take a stab at just like defining it for the audience here like just a very concise definition
[330] of what a semantics layer is uh yeah
[336] I think and I feel like every person who's building you know
[343] semantically right now will still give a different answer so we're still going through the sort of consultation you
[349] know like kind of standardization here but I think it's an interface to data
[355] and it's uh it's a data modeling uh piece of uh of bi so
[363] um when I when I look at the you know like what's happened in Chris bi is you
[369] commonly have a data modeling coupled with with bi right and then you need to
[375] repeat that data modeling again in every bi and uh the problems semantic layer is
[381] solving is that they're just trying to apply dry to that it's like do not repeat yourself at every API just
[387] extract that data modeling and make it you know like sort of unified for every bi so and then
[393] make it an interface to your data right so every day I would go to the data model and kind of use it as an interface
[399] so and in short it's in interface and a problem with solving gives you it solves
[405] the repetition through the do a repeat yourself principle right yeah I think the first time I
[410] encountered this was um it's seen it in uh business objects a bit and then with a look ml as I think
[417] the first time that I saw it like really explicitly done in a code first way yeah um and so that was it was pretty well no
[424] actually the first time I saw this was in uh an orms actually way back in the day with uh yeah with a with like Ruby
[430] on Rails right uh just uh they're uh was an active record or something where yeah
[436] because because then you started because then I looked at uh look and I was like this seems suspiciously like what rails
[442] was doing and Django was doing uh with both templating languages and uh disability to find something once and
[448] reuse yeah that was pretty interesting so uh well I will tell you one term that
[453] we've been using uh when we started cube is what we called it the orm for data or
[459] data RM I don't remember oh yeah yeah yeah yeah not to add more inconsistency
[465] you know like to different terms but that's one we used back then so uh yeah I we saw a lot of similarities my
[471] background is I've been quoting a little bit in this rook and rail so when we started to cube I was thinking a lot is
[477] like is it like is it like European rails but data specifically active record part of the part of the Ruby
[483] interesting okay yeah that's it's pretty funny actually so I'm not completely crazy
[488] it's funny too because you can kind of come at this problem from two different points so there's the orm point of view
[494] software development let's take those principles and apply them to analytics yeah and then there's the problem that
[500] any analyst has had when they don't have a metrics layer or semantics layer and that is every analyst is defining their
[506] own reports and they're trying to Define standardized company metrics like profit or how many customers we have and the
[512] reports are all inconsistent because it's all embedded in individual SQL queries and no one can quite get it
[517] exactly the same but that's what dimensional modeling was supposed to solve for right it was was having a consistent you know store of your facts
[525] and and uh dimensions and and whatnot but um and like your take on that too
[530] like do you feel like that the um I hate to call it the old school way but I call it the traditional way of data modeling
[536] for analytics do you feel like that still has a place or do you feel like that's being somewhat supplanted by uh
[536] Dimensional Modeling
[542] semantic layers or are they are they compatible with each other that's another question uh yeah I think they're more compatible
[550] it's like a dimensional model Indica Stills I think it's still relevant and you know
[556] like I see a lot of people doing it there's maybe you know like it still could be a question is like do we still
[562] need to do you know the classic you know the gimbal style dimensional modeling just because our technology kind of
[568] changed a lot and you know like in the last what 20 25 years you know like when you know like ETA came initially and I
[576] think it's it's true technology changed a lot and now we can just in many cases do one big table right so I think you
[582] know like semantically I should be more of a tool giving you either to inquinoleic if you don't want to do dimensional modeling you can still do
[588] that or you want to do like more like OBT you can still do that as well
[593] yeah yeah it's interesting because and then we had who is it Larry Burns in the show a couple weeks ago and we're
[598] talking about data modeling and he was really a fan of even approaching it from the um you know the conceptual and logical layer first and then the
[605] physical implementations of whether you choose Kimball or one big table or sort of a secondary uh issue according to him
[610] and he's I mean he's been writing about data modeling since like the early 2000s so I think he's had a lot of time to
[617] think about it like almost at least 20 years or probably more of it when you publish it but what I find interesting
[622] in that is it feels like the the conceptual and logical modeling has definitely gone I would argue somewhat
[628] by the wayside um and people really focus on sort of the um have implemented and see a data warehouse or a cloud data
[636] platform I guess as they're now called uh modern data stack or whatever but that's
[641] um at least it's an observation I've had I'm not sure if you're seeing something different but it seems like again like the conceptual logical which is more
[648] kind of the higher level modeling is maybe being somewhat ignored and you know we just make a bunch of metrics and
[654] uh and just throw them into reports I don't know if you're seeing the same thing or again if I'm just like crazy
[659] and stuff so yeah yeah I think it's
[665] it feels it is definitely more diverse and you know later people don't try to be you know kind of put into some
[671] boundaries it's like you do you know like that and follow the book specifically right in your data modeling
[676] so you can you follow your you know like your entity structure your your business
[681] model you know like and again yes you can you can you know like I think all
[687] those techniques they like secondary really so you know like and if you feel that what I see just like people you
[694] know like people feel they just working and doing the job they apply on it right so same with skill right when I think
[701] about the data mod Lincoln Cube it just it's not built for one specific technique right so again it could
[706] support if you wanted to data dimensional modeling you can do that if you want to do one big table you can do
[711] that I think overall look you know uh Cube approaches closer probably to
[719] like one big table really but you know like it's still still easier to do like
[724] uh dimensional if needed you mentioned looking out so you know I think it's Cube has just two two entities as well
[732] as like look look ml has views and explorers we call them cubes and Views it's a little bit different names but
[739] they like serve the same purpose so you build your data graph where you define all the joints everything and then you
[744] just build we call it fuse just like one big table so you you explore them in you
[751] know like you build them to expose into different bis and then bis can read them as one big tables if needed if you still
[757] prefer two-dimensional modeling so you can you can rebuild it as you know like it's more dimensional modeling and then
[764] the eyes will look at it and the star scheme of snowflake schema but default ways just to do one Peak
[770] uh one big table got it that's pretty cool she had a couple questions already uh it's gonna be a good show if you're
[776] getting questions this early uh Jeffrey Jacobs ass on LinkedIn uh why aren't views useful more for semantic layers
[776] Views
[786] uh yeah and it's confused small like uh
[791] more like uh database use yeah yeah because we did mention local ml views which aren't exactly the same thing so
[798] yeah yeah I think I think I'm gonna assuming it's a database view yeah yeah for sure and I I can I can jump on it
[805] Paul Wallington feel free to feel free to chime in because uh we talk a lot about it why you know like why we is it
[812] really what are you building because it's it's is it adding value you can just run you know like uh everything
[818] inside your like warehouse and build a bunch of views I I think to answer that question I need to look
[824] at the you know like when we look at the semantic layer I think usually about two things one is how do you define semantic
[830] layer and then how do you query semantic layer the first thing is defining semantic layer I believe the ddl is not
[838] just the best way to define semantic layer just you know like for managing your data definitions and metrics so you
[844] need some sort of you know like a declaration language uh which you can put under the Version Control and then
[850] you know like you can collaborate that so you you know like you can make safely changes you can make your PRS you can
[856] read that so you knowledge is applying everything you know like in in the definitions off of use it could be not
[863] uh you still need some framework even if it compiles down to the Views uh
[869] eventually still need some sort of you know like a good framework to to manage and scale the definitions of the data
[874] and then on the second side uh the how you query that the problem is that the
[880] databases they don't have a notion of the measure right now and the concept of a measure at all so you still will do
[886] all the aggregations on on a querying site right so uh while it could be fine
[892] for like a very simple aggregations it's easily get you know like uh nested it's easily could get more advanced and
[898] tricky and this way you're starting doing this aggregation during the query time and uh that's actually the part of
[905] the metric definition that's a part of the your data definition and it started to happen on the bi side so that's probably
[913] why knowledge it's not possible to do um and I also joins I think once you learn
[921] the joint program like with use uh you you have actually two options so either
[928] you would expose like joint dimension in a view and basically do the joins inside
[933] your SQL where you query and then you need to basically solve the cosmen
[939] threat problem which is by itself like uh very very hard problem to solve
[947] like inside and SQL and manage or you can incorporate your joints and Views but you end up with a combinatorial
[953] expulsion it's very very easy to get like basically uh 120 tables out of five
[961] you need to join like under the hood so and that's that's
[966] uh something that becomes very unmanageable pretty quickly
[972] yeah that's that's kind of how I think of this problem having worked with look ml for example somewhat in the past
[978] um the this approach like the kind of look and now semantic layer approach is more flexible in terms of mixing and
[983] matching metrics whereas otherwise you get this massive combinatorial problem defining a thousand different views or
[988] something across data yeah absolutely I'm actually saying Rivera has a question here and he's actually got a
[988] Why not DDL
[994] couple questions I'll start with the uh latest one here and it goes back to when you comment on a detail there are them
[999] um yes why hasn't ddl adopted semantic layer functions or is or yes am I going off the rails no pun intended for Ruby
[1006] on real estate I'm guessing but um yeah uh
[1011] uh yeah I think you know like if I if I
[1017] take a step back why data warehouses since I'm not building too anticulators right probably it would be question and
[1023] then you know the gdl could be a tool for them to build that uh I think you know like data warehouse vendors they
[1030] are looking into building so multiplayer so Google bought looker specifically for that right we we all know that looking
[1036] model is a semantic layer for bigquery and like lookamal is going to exist only to sell more bigquery
[1043] um so um why it's not why they bought blue occur and not doing this through some
[1049] sort of you know like dtl I just think you know my take is that detail is not the best tool for the job for defining
[1056] the metrics maybe there is some way you know like extending it but it may look
[1062] you know like if you extend it to in much you know like it's going to look like a local mile so why not just like
[1068] have some sort of like a look ml instead uh or any other you know like a semantic layer framework to Define metrics again
[1074] I just don't think it's it's DDO is the best way of doing this but it may be
[1080] done technically so in all it can we'll see yeah but before it's done it should be like extended SQL itself should be
[1086] extended because it's enough enough from SQL perspective for sure here's another question I have
[1086] Does Semantic Layers play a role
[1092] like in the cloud era maybe even before with Hadoop Plus data warehouses we saw this kind of proliferation of analytic
[1098] systems in other words a company instead of having one main analytic system might have two or three so say they have data
[1104] bricks and bigquery data bricks and stuff like um does do semantic layers play a role
[1109] there in combining data from different systems
[1116] we we got a little question a lot um I think that comes to the you know
[1121] like are we we're still talking about definition of semanticleer right like when we started it's like we try to
[1127] understand what it should done versus what it shouldn't that's one I'm Still Still you know like wrapping my head
[1134] around uh there is a category of software like pra trino Presta right so
[1141] you know like it's like a query Federation that you know like you would expect to do that I don't think
[1146] and you know like dream io2 so do we um should that be a part of you know
[1152] like semantic layer or not should they build their own semantic layer so I think we have some crossovers that uh we
[1158] still try to understand my take is that for example Cube shouldn't do that while
[1163] we have a cross data source you know like joins and cross data source just querying
[1170] overall I think it's just intended to bring more like semantic layer they can work on top of multiple data sources
[1177] rather than trying in order to really do like a complicated figuration so uh and
[1183] when it you know like someone from a community is asking me can I use Google Federation I would say like technically
[1189] you can try to use it to that extent but you probably need to look at Trina you know that's going to be probably the
[1194] better fit for your use case and then you can run a tube on top of Trina so uh Power you may have a different take on
[1202] this now that that that's it I guess uh like from like beta modeling perspective once
[1209] you land in a complex core refrigeration uh problem you should you should use uh
[1215] like great query Federation engine because under the hood and Cube we don't build for fully flooded query engine we
[1222] have a cache which can be suited to fulfill the gap between you have like uh
[1228] data in one place you you can like regulate that and the date in another
[1234] place and just join two relapse together but not beyond that just when you have a
[1240] sense of very specific query that can be served from like two data sources but not on data modeling or ad hoc wearing
[1248] anything like that interesting I see Sonny has a follow-up
[1248] Application Data Modeling
[1253] question here uh he says when we say data modeling do we model for analytics versus Warehouse or application data
[1260] modeling I think that's a good question so
[1268] I felt I've been answering all the questions
[1273] I guess a uh a semantic layout for application data modeling I feel like this is an area where um
[1281] you know it's something I've been writing a lot about the uh
[1286] I would say there's kind of paralleling what's happening in analytics where maybe we need to kind of
[1286] Semantic Layers OTP
[1292] rethink how we're um defining our metrics right I mean the same thing is happening over in
[1298] um applications as well right so I mean you've all worked with orms I'm sure you you know the the joys and the absolute
[1305] uh horror show of a mess you can create with your data using an orm and so you
[1311] have any thoughts on application um data modeling um with semantic layers
[1317] and by application you mostly mean OTP stuff right yeah exactly yeah yeah go ahead yeah I think I think
[1326] right now uh uh with this whole concept there is also a concept like of ntg layer and there is a whole question
[1333] about like should this like semantic wear thing grow into like OTP stuff I
[1340] would say it's it's an open court question and uh there are uh let's like
[1346] very nice idea and but there are like too too many like technical hurdles
[1352] right now to overcome because in a sense like from technological perspective you
[1357] need completely different set of Technologies to sort the web traffic versus OTP traffic uh it means while you
[1366] can model all the stuff pretty the same way but from uh like uh from serving
[1373] perspective it should be different and a lot of stuff which is happening like on modeling clear like for example for cube
[1380] uh it boils down to like tweaking the performance stuff and at that point uh
[1387] you would need to have like two branches like OTP on the lab but I think like uh
[1394] at the end of the day there are ways to do it but there are like really big
[1399] technical challenges to overcome like um for example eventual consistency what
[1404] if you're using data or house but you you want to write back based on the data
[1410] from data warehouse like snowflake tries to solve it right like providing code TPM transactions stuff like that but
[1416] still like a very uh long way to go um yeah I can see that so
[1422] well I mean I should point out you know just even um collecting all the analytical data sources together and trying to come up with a consistent way
[1429] of doing it there is I can imagine that's challenging so I'm trying to escape the one uh semantic
[1435] layer to rule them all would be uh and I guess in another level too does it I mean there's certain nuances where maybe
[1440] it makes sense maybe it doesn't so an application if you define certain things a certain way like uh
[1445] things related to a customer maybe analytical questions are you know they're usually different and same with machine learning so
[1445] Data Contracts
[1452] um but I think something like that will probably happen at some point it seems to be the inevitability but maybe not
[1458] well especially for real-time data that's where we've talked about it a lot where it's exactly it might have a separate you know facts Dimensions model
[1465] for your data warehouse but there are certain real-time analytics where you need to Define that schema in in the
[1470] application like you cannot post-process it fast enough basically that's what I think data contracts are trying to attempt right but it's you know what are
[1476] your thoughts on data contract I mean what is the data contract uh kind of intersect with a semantic layer and then where are the uh completely different
[1485] uh I think this multiplayer should should have some way to work with the
[1491] data contracts I know I just uh I try to understand there's a data
[1497] contract should be a feature of some you know like of some software some tool we have you know like maybe like a cdpu you
[1504] know like a collection overall or you know they can somehow to be integrated this magic layer or it should be some
[1510] sort of you know like a separate Tool uh that sits you know like and work across
[1516] multiple you know again it works with semantic layers ETL and you know like CDP and just kind of you know like
[1522] ensures some sort of you know it defines an insurance contracts or you just move
[1528] the you know like the process again and you know like and then the part of this process should be implemented across
[1534] multiple tools so I think it's a little it's a little unclear so I haven't seen a lot of you know like practical implementation of this I mean like every
[1541] company has some sort of you know like a documentation rules and you know like guidelines you know like around around
[1547] that area but it's not like some you know like standardization or like some resistance of the phenolic
[1553] kind of approach that I have been seeing you know like consistent across multiple orgs of implementing this uh and I
[1561] haven't seen a specific vendor that you know like dedicated to doing this you
[1566] know they can kind of pushing for some specific philosophy here so yeah I mean what is what is your take I I
[1575] I think a data contract is very much a defense mechanism it's not an offense mechanism right so
[1580] you basically like trying to ensure that whatever contract you have without stream producers is what you expect as a
[1587] consumer and that catches a violation you know before it makes its way to production right so it's it's
[1593] a check and a balance what's the things I've been thinking about right now is sort of what's the intersection of like
[1598] stuff like data catalogs semantic layers contracts
[1603] um so I feel like these roles similar ish in their own ways but they're different enough where maybe they are
[1609] Standalone I uh um would love your take on sort of the uh you know where does the semantic
[1614] layer fit in with the data catalog for example yeah that's an open-ended question I would love your opinion on yeah that one is that one's a little bit
[1622] more tangible than you know like crosses and uh yeah data contracts at this point because we got a lot of leaky data
[1628] catalogs vendors out there right um yeah
[1634] I think some people expect to have some sort of you know like a data catalog features around semantic layers that's
[1640] what I'm you know like see you know like by talking to people especially you know like if we talk about the idea of the
[1646] metrics store or metrics repository right like that people would go in to see all your metrics you know like to
[1652] see how to query those metrics uh so that really feels a little like a data catalog already
[1659] um what we do at Cube and you know we'll
[1665] see whether it's the right approach or not we'll try to not build it at all almost at all we're building some
[1671] internal tools just to help semantic later Engineers to work with uh with the
[1677] data model you know like to understand lineage graph all of that but the these
[1683] tools they're not intended to be exposed to the end data consumers so instead we wanted to integrate with uh tools on the
[1691] market like Elation right or something like that just to give you know like data consumers and you know like all the
[1698] business units a way to look at this sort of phenolic and metrics and catalogs through the their existing data
[1703] catalog solution so I again I feel like semantic letters just should integrate with existing tools but yeah
[1710] it may be a different approach yeah interesting she got a question here from
[1710] Decoupling Semantic Layers
[1715] Jonathan Neo what's up Jonathan it's uh it's not Australia right now I have no idea to do what time it is um but yeah
[1721] do you think that we'll have the same decoupling and semantic layer and the visualization layer like we've seen in front end uh back-end Frameworks like
[1728] node.js and uh front-end Frameworks like react uh uh yeah I think the short answer is
[1735] yes um you think that whole Ada you know like
[1740] uh other all the semantic player is to decouple the function of bi right as a
[1746] dimension in the beginning because like we have a data modeling and then we have a visualization in API like a local ML and
[1754] look here in the rest of the looker with charts and all of that and then ideas just like let's decouple that again for
[1760] the purpose of you know like make it dry and you know like just make it maintain it uh separately it what happened with a
[1768] you know like a application developer is a really good you know like a example
[1773] back then in Reuben rails days right we were writing called Big you know like a full stack applications with all the
[1779] logic you know like having in one modeling application now we sort of decoupled it and it's it's only benefits
[1786] right we can we can maintain it and we can scale it so yeah the same the same
[1791] idea here and I believe it could happen I think the the biggest issue the
[1797] biggest challenge is how to make sure that the bi experience is still Native even if a data model is decoupled
[1803] because many bis their UI and their interfaces and the user experience has
[1809] been really driven by data model it's like looker and you define and explore
[1814] and then you have this explore in a list of explorers right so now you're decoupling data model how you make sure
[1821] that the UI of the bis is still you know like working well and it's still user friendly and it's easier for you know
[1827] like a non-technical data consumers to consume data through some bi while data
[1833] model is decoupled so that's that's the biggest challenge yeah it's actually really interesting it
[1839] brings up a point that um like I always kind of joke with Matt and
[1845] with the audience that data feels like it's about 10 to 15 years behind software I mean I don't think it's even really a joke it's not a I mean it's a
[1851] reality but we have to joke because it's kind of depressing yeah um but the uh but the notion of like MVC which you
[1858] know rails I think adopted back in the day you know tightly viewed I mean it's interesting though because you don't I I
[1864] haven't personally seen like the same sorts of paradigms being discussed in the data world where NBC sort of old hat
[1870] and software development but it did represent when it was you know popular back in the 2000s like a way of
[1876] abstracting out your model your viewing your controller um and each of these had separation of concerns obviously there's there's new
[1882] paradigms now and so forth but um yeah I mean it's it's kind of interesting that because it sort of
[1889] represents a similar-ish type of conversation about how do we start decoupling out the view layer from the
[1894] the model layer and and so forth and it's I don't know if you you guys have had nerdy discussions like Matt and I
[1899] have had on this topic but uh you seem like you guys have fun chats like that so yeah yeah I think we even
[1909] we obviously been talking about MVC too I think we remembered even facade patterns it's one of the you know like
[1915] this like a canonical patterns in the book right so the like facade pattern I think reminds you know like the data
[1922] model a little as well where you know like you're really building facade of your data right it's multi-clare and
[1928] then you exposing it as an interface to the um to the like all the bi tools but yeah
[1934] I I see a lot of similarities here uh you know like with oil Ram mentioned and
[1940] you know like MVC concept so and uh it's it's funny also you know like maybe to
[1947] follow up one of the questions that previously been asked about application data modeling it will be interesting to
[1954] see how at some point you know like and I believe it will you know like all those ideas installed will start to
[1960] converge you know like and we'll have application development and data development you know like kind of you
[1965] know let's turn into kind of you know like uh coming together uh especially you know
[1972] like if we're houses will provide some sort of uh transactional support eventually for us right uh so that would
[1980] be and so-called hdap architecture so that would be that would be interesting to see what is what is your take on that
[1986] by the way how do you how do you see if that is coming we've heard about this in the last chapter of our book fundamentals of data engineering and it
[1992] was so we kind of speculated on the future of data engineering and I think what we one of the conclusions we had
[1998] was there's just going to be I think a fusion of uh software engineering data engineering and ml engineering like
[2004] because data really in the past data existed in sort of a one-way life cycle right where you know it kind of starts
[2011] it's created then it goes somewhere else and it becomes a report and then who knows what happens to it maybe decisions made but that it's a
[2018] very fuzzy feedback cycle in that respect but but now you know with the rise of you know data powered
[2023] applications you know whether that's you know analytical data or whether that's machine learning this goes right back
[2029] into the application and so I feel like software engineers and data engineers and ml engineers at some point are going
[2035] to become basically the similar type of person perhaps the same person maybe there's a full stack data developer now
[2041] or something I don't know but it's but I feel like there's a very interesting artificial divide between
[2046] um maybe it's not artificial maybe it's necessary in some cases but I think we overstate like the importance of like oh well analytics is over here and this is
[2053] analytics and software's over here as a software and machine learning is over here like I was just actually finishing
[2058] the slides of my talk I'm giving uh in Munich later this week about the um you know the intersection of data
[2064] engineering and ml engineering and how it you know that could make a very strong argument they're very similar and
[2069] a very strong argument they're not and so um you can hold two opposing ideas in your head at the same time time but uh
[2075] but with software it's it's fascinating because you're exactly right it feels like the world is converging right hdap
[2081] and so forth um right the data engineers and data people are starting to talk about software practices uh and I'm glad this
[2088] is happening so it but the the I think the Crux of it's really going to be software Engineers understanding data
[2094] which I think has been the harder part um because software Engineers typically depending where you work obviously if
[2100] you work at a big company right where there's data power you know you're kind of data Centric and data powered applications like that's just part part
[2106] of your job your title might not be data engineer but you're working on some of the biggest Data Systems in the world so
[2111] I don't know what do you think about oh yeah yeah I mean I tend to agree I think there is this very much the traditional
[2117] separation between the data generators basically the people who consume on the analytics side and that's caused a lot
[2122] of headaches right like no amount of Downstream data modeling can fix data problems that you create in your
[2129] application I mean you can kind of clean things up but there are certain things you're not going to be able to restore or there's just a lot of pain around the
[2135] amount of time that you DL takes for example you know data pipelines to get things in order and I think I mean the
[2142] the data mesh concept is very controversial but the part about it that I really like is the fact that you're
[2147] integrating the data creators with the people who are responsible for analytics right and so whatever the Ultimate Team
[2154] structure is I hope we can kind of get rid of that artificial divide especially in big Enterprises but it exists in
[2160] startups too yeah it exists and so I mean yeah so it's part of that the notion of the new book I'm working on is
[2165] just sort of the end and you know thinking about data modeling from end to end in the data life cycle
[2171] um and end to end also means like um beginning to beginning
[2177] so this is this is sort of the uh the the the the thought process I don't know
[2182] I'm very fascinated to see where this this goes over the next few years I think like the semantic layer is definitely a giant first um step towards
[2189] that sort of decoupling that will actually make this make sense because right now because everything is monolithically tied to each other it's
[2196] it's impossible to get these separations by definition and so that I think it's a huge hurdle to making this happen so I
[2203] don't know it's interesting I got a couple questions here um these are all good questions actually
[2203] Semantic Layers for NonTechnical Users
[2209] uh Sunny asks do you think um yeah kind of going back to what we're
[2214] talking about maybe a few minutes ago but do you think that semantic layers and models will be focused on non-technical users for self-service
[2220] analytics and more traditional data teams of analytics engineers
[2228] um I think some anti-claration models should definitely be focused on
[2235] non-technical users helping them to navigate you know like the data model and hopefully not make
[2241] mistakes when they know like self-serving uh but also they could be
[2246] helpful for the data analysts who are building uh you
[2251] know charts and dashboards to provide to the non-technical user so maybe you know like building uh embedded analytics
[2258] application and then data apps just because uh you know they would be able to query the
[2264] same metrics you know they cannot repeat themselves when the data modeling so there is like a huge benefits here
[2271] um I think it's sort of a semantic layer should still give away your knowledge to sometimes
[2278] maybe queries raw data and then merge it with model data especially you know like formal like and data teams and analytics
[2285] Engineers who need more power so it's it's sort of it's sort of a facade and a protection right and then it's at some
[2291] point we we need to understand when you know like when some people and
[2296] some teams should be able to bypass that protection so that's that's something that's been on top of our mind as well
[2302] is like how that should be designed uh and you know like based on different consumption scenarios but uh I think you
[2309] know like definitely to support dashboarding can you know like a slight exploration that use cases can
[2316] definitely be supported from a semantic player if you're talking about molecule detailed uh you know like data
[2321] investigation I would say almost I I think you know like here we're all
[2327] talking about yes some data can come from a semantic layer but then still going to be a lot of you know like a
[2332] query raw data for you know like we're like we're talking about really data professional and they usually know you
[2338] know like what they did and you know like we're talking about the you know like a different error pronus
[2345] right rather than you know business users and non-technical users
[2345] Decoupling the Semantic Layers
[2352] and then um I'm gonna be going on a roundabout way of the questions uh but uh Jonathan
[2357] also asks uh kind of follow-up question to his question about decoupling the symmetic layer and the visualization layer um it says if that's the way
[2365] forward uh why haven't we have a better abstraction for the visualization layer that feels closer to how bi tools exist
[2371] he said so far the visualization Frameworks that exists like D3 plotly leaflet chart require a front-end
[2377] developer to implement
[2383] foreign probably want to announce for that like
[2389] yeah I I think yeah I can take this one uh so I think what's happening right now
[2395] so we are um I would say at the at the beginning of a market annealing that
[2402] basically should happen if like semanticular is a thing so the
[2409] uh why we don't see this too yet is just a question I I guess it's just a matter
[2415] of time because there was no like semanticleer which is like uh
[2421] self-sustained and there are not not a lot of those yet so I guess uh once
[2428] semantic wear exists like as a technical implementation right so there should be
[2434] more and more tools that connect to those semantic players and we will see more and more like thin tools that
[2442] either have like really integrated like uh
[2447] semanticular uh on their side either don't have it and just use like existing
[2452] ones uh like we can see one two like which is called light Dash which is like
[2458] heavily built on top of gbto right but they built mostly on top of like DBT
[2464] models uh uh however I think this will continue
[2470] to evolve once we see more and more like semanticore implementations which work
[2478] yeah I think it's what we've seen too especially when you get into embedded analytics it's still not perfect right you can definitely take the route we see
[2484] this a lot where software Engineers will you know take one of the um you know Frameworks that Jonathan posted there
[2489] and um you know take a stab at it the issue is that software Engineers typically aren't trained in the art of building
[2496] visualizations [Music] yeah weird process
[2502] what you also need like design ux UI all these pieces yeah yeah they look like
[2507] to be frank yeah it's pretty bad um some of them some of them are good I've worked some some like fantastic
[2514] um yeah I remember one time I had to build a uh I started a job and in two weeks I had to get out an entirely new
[2520] uh analytical framework for the company um that was a nice crash course and
[2526] light us up but the designer I worked with fantastic we luckily got it out in that time frame but that was pretty
[2531] bananas especially like uh cool get started cool I'll I'll do that
[2537] um so it can be done but it does take somebody I think has a good eye-end design and hopefully this becomes a lot
[2542] more um available I know that you know it'll be interesting to see what the intersection is of the uh open source
[2547] Frameworks and also the bi vendors and kind of uh because I think a lot of bi tools tend to be very kind of top heavy
[2553] I would say um and right they know they solve certain types of questions but if they come up with a very lightweight
[2558] view of how they do stuff too that would be pretty sick so yeah
[2558] QA Time
[2564] um gosh lots of fun questions here Davis Vance uh we're actually doing a uh an
[2570] AMA with him later today for his book club yeah yeah and
[2578] yeah that's right Dave it's really cool dude um but uh he has two non-technical do non-technical users want to be more
[2585] involved or do we hire analytics professionals to do that work for them he says I think adding more data
[2590] distracts business users from the work of thinking about customers and Building Solutions for them uh same dichotomy so
[2596] I don't know if you have thoughts on this
[2602] David's stuff
[2614] um and I think it's not really connected to semanticular a little bit more like a workflow question right yeah uh more of
[2622] a macro question yeah I think uh data teams should definitely
[2627] be embedded into the business you know like and I feel like maybe in our organization scales we should have
[2635] multiple you know like uh data professionals being embedded into multiple verticals of the business and
[2641] just kind of building this understanding of that and then bringing that understanding back to you know like that
[2646] the data modeling shouldn't data modeling be centralized or not uh I think it would probably if we'll have a
[2654] centralized platform of framework that helps to scale into different departments and segments that would be
[2660] ATO and then we'll be able to have data professionals who embedded into specific
[2666] departments to own some part of that uh centralized but specialized spine
[2672] declares like a data model that would that would be great but uh yeah that's just my quick take on that question
[2681] and you take Pavel yeah I I think like uh
[2688] uh I guess right now like
[2694] I want to touch more on like the semantic weather thing here it's actually a maybe a like uh semantic
[2702] player stuff should help uh more this with this uh like I would say hiring
[2709] question so uh I think that that's that's the demand we see like from our
[2716] like early adopters of like cement Square thing that's actually uh they want trying to solve this all the data
[2723] mess and uh basically save time for like doing actual job with data rather than
[2729] fulfilling like questions from their business stuff like that yeah
[2734] that's interesting I don't know what do you think about it does more what's more data uh help or hurt so don't know it
[2741] depends I mean I actually I have some thoughts that are trickling down through this whole discussion today which is we
[2746] almost need to focus maybe someone is already writing on this off to look around but we almost need need to think more about data ux we need to think
[2753] about this in terms of a user experience because I think technical people tend to think just in terms of okay what's my
[2758] data model and it tends to be a physical data model kind of like you were saying Joe right like they're very focused on the nuts and bolts and data and then on
[2765] the opposite end of the spectrum you have people who maybe just care about pretty visualizations and you really need to care about that whole experience
[2772] end to end so the data is successful as possible so more I would say basically more data can be a problem going back
[2780] earlier to an earlier part of the discussion you have your highly technical like exploratory analysts who dig into the raw data and look for new
[2787] insights but often business users just get confused by too much data too early I think this is changing though to us my
[2793] podcast I was doing on uh my other podcast uh the Joe Reese show but we're stuck with Ryan Dolly about this a
[2799] couple weeks ago and I think he actually had a very good point where he's he's had a series of Articles where he's written that I think the whole
[2805] the whole way we've been doing bi needs to be rethought um I would say you know and I do agree
[2811] it's we're stuck in this dashboard mode a way of thinking and it's somewhat Antiquated I mean you know tell me that
[2818] and here's why a lot of the same questions and the same issues that we've been running into for decades we still have them and at some point you need to
[2825] maybe look in the mirror and ask okay is it maybe is it the way we've been doing things that needs to be called into question as data people and I would say
[2832] yeah there are we should rethink this maybe people you know need to consume data in different ways it's a different
[2837] experience and the other thing obviously that you know the big elephant in the room are large language models and how that's going to impact uh bi I think
[2844] that that needs to be thought about and and um well people are doing it and thinking about it later but um you know
[2850] it's uh the nature of it but that's that's going to change a lot of the interface I would say um I know you know companies like
[2856] hotspot already integrating and you know their own GPT type of uh interfaces and
[2861] I expect stuff like that's going to be table Stakes uh pretty soon how you train it on your own data and get it um
[2867] to produce correct answers as an entirely different question um that'll let people smarter than me
[2872] figure out but uh I I think that's going to be the table Stakes interface something like that so yeah but you're
[2879] what you're alluding to here I think is it's really exciting but there's the solution hallucination problem or it
[2884] might just make things up instead of the correct answer well we saw it the other day yeah yeah we asked chat gbt uh What
[2890] uh you know who wrote our book and it came back with uh what was it I'm a senior data engineer at Google and you
[2897] you're a senior data scientist at the Airbnb or something yeah so
[2903] which were not I don't know nothing I checked so uh yeah it's it's interesting but um yeah I mean kind of kind of you
[2903] Wrap Up
[2909] know wrapping it up like what do you what do y'all think is next like you're if you're the kind of uh put on your uh Nostradamus hat and you know and predict
[2916] five years from now where semantic layers are gonna be what what do you think it's going to be at
[2922] uh I think it's converging of you know like software engineering and data
[2928] engineering canola and basically old TP and Olaf I think that's uh this one big
[2934] big area where you know hopefully we'll see innovation in the next five years you know they can really you know like
[2940] this two type of the workloads and you know like two type of the applications kind of being converged together and you
[2947] know like see multiplayers hopefully will be able to facilitate that um the other thing is as you just
[2953] mentioned large models right and just like all the AI uh The Innovation that we see happening right now uh how that
[2961] going to impact the data and you know like it's it's hard to predict at this point you know if there are some
[2967] practical applications as you mentioned like thought spot and we I know there are some other companies that build in
[2972] control of cube as well you know like to provide the natural language interface because now this AI system that actually
[2978] can ask follow-up questions I think that was a missing Pace bags and you know like when thoughtspot and some other
[2984] companies try to build a they're like natural language interfaces the data it was like pretty emotional like one one
[2991] shot you kind of try to ask a question and it yeah the system tries to guess and gives you an answer and now this
[2996] actually the system can start asking the follow-up questions like what do you mean by active users and what do you mean by the quarter right like and all
[3003] of this so you know again it can create this understanding and then queries multiplayer and then you know it
[3009] hopefully gives you the correct answer so I think you know like it's going to be a lot of interesting interesting you
[3016] know like ways to interface and you know work with data like AI driven ways to explore and work
[3023] with data so that's something you know like I'm really looking forward in the next five years too yeah that's cool what do you think Paulo
[3031] yeah I think I think like from semanticular perspective uh I think SQL
[3036] should be extended uh like yeah in five upcoming years and it and it will
[3042] actually blur the lines uh of like semantic words data or houses bi tools
[3050] and basically we'll create a lot more ways of for indoor connection
[3055] basically uh uh like bi tools uh I think
[3060] uh will will probably uh gain some data from like based on a SQL from other like
[3067] semantic workers either like build like uh like as a standalone semantic players
[3073] like Cube or like semantic words inside of data workhouses there there will be a
[3078] standard like more like standardized way to fetch this data and create this data
[3084] using SQL so it will create a lot of more opportunities to like interconnect
[3089] tools yeah uh but at the end of the day I believe uh more like this in like
[3096] software engineering practices win and uh like semantic Words which code base
[3102] will like become more like a standard error
[3107] that's interesting that's an interesting perspective yeah and I
[3112] my personal pick is I think they're here to stay I don't think they're going anywhere I don't think we're going to go back to the world just like a kind of
[3119] scatter shot SQL queries and um you know promiscuous definitions just floating around uh in the air I don't
[3125] know what do you think uh probably here to stay just going to evolve rapidly yeah I love this discussion or to him about the interactivity of of uh these
[3133] large language models and it's starting with chat GPT right and if you think about it if you think about using uh
[3139] like Siri right that interaction is very stilted it's very phone tree like it's
[3145] like push one push two whatever whereas this like open-ended using a tool to explore your data and then if we can
[3150] combine that with semantic layer that seems like a very powerful approach yeah because I mean the thing that the llms
[3157] get wrong is that well they get a lot of things wrong um I mean because they're they're basically is their token prediction engines they oh they're
[3163] supposed to provide the most convincing answer that you know based on the probability of um you know what what
[3168] tokens are associated with what word bath you're on um and that's it it's not I mean and and
[3174] so like with gbd4 they were you know through the human interaction the reinforcement cycle there it gets more accurate but that's
[3181] um not what it's trained to do from a deep learning perspective right as far as I can tell identity keep it number four like very
[3187] quiet um but having a semantic layer would be cool because then at least you provide I'm assuming it can be trained correctly
[3193] on it the definitional Integrity of like what does a metric mean right so that's right that's sort of the missing piece so right because right now it's like I
[3200] don't know customer could be a horse or a uh or a car when you basically it doesn't make any
[3206] sense right yeah to actually validate that it's going to be correct information semantically it sounds like
[3211] a very important tool for that yeah certainly cool awesome uh cool
[3217] um for people who want to learn more about what you guys are up to at Cube how can they do that
[3222] um the give is open source so and you know that's probably GitHub repository is the best place to land on queers you
[3229] know like if we have a website so too so you know like there's two areas and we have a slight community so to ask
[3234] questions so this tree place is probably the best you know like when you know like
[3239] I also welcome everyone you know like who wants to learn more just ping me on LinkedIn you know like
[3245] I would would love to chat cool yeah and uh it'll throw it out to Jonathan Neo if he's looking for another open source
[3251] project to uh contribute to maybe a shout out to the guys at Cube so it's it's cool what you're working on I I'm
[3257] uh I'm excited for the the future so thanks for being on the show thank you thank you for having us yeah anytime uh
[3264] upcoming stuff for us Matt what are you uh up to this week um I'm trying to make it to the location
[3269] easy to happy hour in Manhattan tomorrow so if I make my flight gets there in time I should it's okay
[3277] 2023 in Flight sir yeah yeah Lord knows what the hell happens with that yeah that sounds fun
[3284] um yeah I'll be in uh Munich um later this week we'll be keynoting at the applied AI conference in Munich uh
[3291] some Emma lops thing that's on what is it Friday so if you're in the area come say hi then I'll be in Berlin
[3297] uh next week um just hanging out I think I'm doing a bunch of podcasts there so
[3303] should be fun um yeah Renner one of the guys here Sebastian actually at pycon we're at a
[3309] AWS event recognize him as a funny mustache so we're gonna go to a podcast
[3315] yeah it is I can't grow one um look absolutely ridiculous so um oh and by
[3320] the way so Matt and I were um starting to uh do data engineering workshops as well so if you want uh if your company
[3327] wants to um you know internet data team want to learn data engineering uh hit us
[3332] up you know how to get a hold of us and so that'd be a lot of fun to work with a lot of the companies out there so yeah we'll have some information available
[3338] for us yeah yes yeah sounds fun all right cool well
[3345] we'll see you all next Monday uh so we'll talk then all right see ya awesome thank you thank you
[3351] bye
