---
schema_version: 1
id: yt-MXiVLwN8lho
type: youtube
title: Semantic similarity for faster Knowledge Graph delivery at scale. Vassil Momtchev
url: https://www.youtube.com/watch?v=MXiVLwN8lho
authors:
- Connected Data
ingested_at: '2026-06-18T01:38:22Z'
content_hash: sha256:0231c5b067696ae45709e2dbd6bfd756d7fe3ded34ed6978886125bfd5c35762
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Connected Data
  channel_url: https://www.youtube.com/@ConnectedData
  duration_seconds: 2317
  caption_track: cached
  snippet_count: 382
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:22Z'
  user_correction: null
---
[0] Introduction
[5] before we have the last break of the day so we have with us Vassili mom safe who
[10] is the CTO of on the text and he's going to be talking about semantic similarity
[16] well-muscled thanks for joining and floors yours Thank You Jorge it's pleasure to have
[23] you every everyone I'm the CTO phone to text basically my responsibility is to
[30] direct the general product development in the company and in the today talk
[36] which is the age struck out give you a really healthy mix of some scientific information some use cases how to create
[43] knowledge graphs and obviously some software architectures how you can really implement this but before to dig
[51] into the presentation I really want to ask a question so why we have all these people here talking about knowledge
[58] graph we have really a bunch of smart people who invested probably a good portion of their time testing some
[66] different different different scientific methods how to implement this and also we know a lot of business people who try
[73] to implement this in their organizations so this is one of the questions and I'm
[73] About the company
[80] really happy that somebody tried to quantify this because we see this in the last 15 years that across industry
[86] research show that the big organizations they show actively use only half of their structured data and if we go to
[93] the unstructured data this percentage is real even lower it goes as low as 1% we're on to Texas
[101] the company we specialize in two technologies one is the text analytics and the other is knowledge graphs and
[108] knowledge representation here today our talk are we more focused on the knowledge graphs so we're basically
[115] serving one of the most innovative organizations who are trying to develop new intelligent systems which better
[123] utilize the enterprise knowledge and by saying enterprise knowledge this is no
[128] longer focused to a single organization you know in the modern world they're evolving business models which
[135] combine data from different organizations so no longer you have to work only with your internal
[140] organization you have to mix it also with external reference data and also
[145] inside of these organizations you have obviously securities nobody has access to the full information so in this talk
[145] What is the problem
[154] I'll explain three things what is basically the problem by giving you four
[159] very concrete examples what is the solution and what is the solution in practical software terms to implement
[166] nice so I will step make a step back and talk what is actually a knowledge graph
[171] and this is our understanding about knowledge graphs the knowledge graph is something which is populated from
[177] unstructured information as I said we do a lot of text analytics which helps you from non structured data to populate a
[183] knowledge graph but on the other hand we have also to deal with the master data or this is the data which you need to do
[191] any type of a text analytics and what are really the four fundamental problem
[199] Fisher's of the knowledge graph first of all it should be graph that means that naturally it should be a native graph
[205] model which basically allows you to connect new data and extend the model
[211] and to not be fixed to any physical schema the second feature is semantics
[216] semantics is really having a schema of the information and symbolic when connects to this knowledge graph there
[222] should be a way to understand what is in sight of this graph without reading some
[228] complex manuals what is really exactly the format so it's the schema of the information should be some descriptive
[234] the smartness is something which is very often overlooked once you design a knowledge graph you want to do some
[240] smart analytics and most of my talk will be how you can implement these martinel ethics once you design a knowledge graph
[246] and last but not least the knowledge graphs are a why because they combine data from different sources so if they
[253] have they need to be up-to-date with all the changes and all the changes should
[258] be the data should be fresh in my experience I have seen different engineering teams which often
[266] over one or two of these aspects for instance if they start if the team
[271] starts focusing over on the graph and semantics typically I have seen often these projects end up in designing a
[278] very complex model and nobody is really thinking how to make to make track the provenance of the information how to
[284] constantly update it and some of these projects becomes really problematic on the other hand the experience of the
[291] data based people donate the typical database people they really are concerned mostly with the freshness of
[298] the data how to make these data sets up updatable and they focus over their wife
[303] and often these projects end up in doing yet another data warehouse where you
[308] need all the questions in the beginning you design the model for one year obviously you need you can update the
[314] schema but this is a fragile system which you cannot easily extend so in
[320] this talk and our understanding is that the true knowledge graph needs to on all these features in order to say it a
[326] knowledge graph in this conference I saw some examples like somebody saying that
[332] okay if I represent as a knowledge or the telecom information then I can count
[337] every node with how many accounts it was interacting okay but this is not really
[342] Norwich graph under each even database problem so by just using a knowledge graph database it doesn't make
[350] automatically your application a knowledge graph and for instance this is
[355] not betting because designing through knowledge graphs which have all these features if you are unworking enough
[360] that you need to face them this is a really challenging task why this is a
[360] Challenges
[368] challenging task because designer can interpret when you design a knowledge graph you have to face multiple
[374] challenges which are typical from the data management systems so first of all
[380] combining data from different sources you face the master data management problem whether this entity is exactly
[386] the same as the other entity how do you merge them which properties do you keep do you keep multiple versions of the
[392] truth or you try to make a model with a single version of the truth the other thing is the subject matter expertise
[399] you need somebody who is really savvy in these models in order to model what are the taxonomies and to know what are the
[405] business terms you want to work and typically for the different organization they have different economies data
[412] warehousing can say as I said updating the data is a challenging and keeping
[417] it's fresh it's a challenging task in itself combining it with the other
[423] capabilities it's even more difficult the metadata management like in the other examples you see there are
[430] organizations with thousands of tables which try to understand what is this data how it was represented how we
[436] should track it and govern on the digital asset management is mostly who is really responsible one owner of this
[442] data and how you update it who is the owner and obviously if you really complete all these levels at the end
[449] somebody will say ok it's very valuable resource so I want to interact via nice interface to do an enterprise search on
[456] top of this data ok so I make another step and wanted to
[456] Perspective
[463] give you the perspective what is really building on knowledge graph and in this
[468] example I took something which is public publicly available so everybody can
[474] reproduce these results and it's easy to understand I mean there is no complex subject matter expertise in order to
[480] understand these examples so everybody knows what is the Internet Movie Database there are movies inside
[486] everybody knows what is wiki data wiki data is really probably the most visible
[492] source of structured information so we imagine that you now start working a startup and your boss tells you ok
[499] please make a knowledge graph which combines data from these two particular sources because we want to do a like a
[505] better decision making what will be the next time the movie how we want to predict the future and let's take this
[513] journey in the next minutes to see whether it's a easy task so the very
[519] first thing once you get these data sources is to be challenged with the
[524] types of the data and you see that there are 4 million episodes in internet movie database and
[530] wiki data uses a very different type system what are the different movies we all
[536] know that these are all movies but you see that even on the type level there is a big discrepancy and the other the
[542] other obvious thing is that Internet Movie Database is a much bigger and it looks like some sort of a super set than
[549] a wiki data for the next experiments we are going to use only a 5,000 data set
[555] of Internet Movie Database obviously all the other items they are scalable and can work with the full 5 million movies
[562] but just for making these results reproducible we got one of the Internet
[569] Movie Database which is available in the target weather depth so I'm a practical
[575] software engineer and my first task is let's say let's move much the movie
[580] titles and see how this will work so the first thing what we can see is multiple
[587] level of inconsistencies so one of the sources talks about films and the other talks about TV movies the question is
[594] whether these are exactly the same type of informations we see a lot of
[599] inconsistent metadata and you see why you have to manage the metadata once a science fiction and the other is science
[606] sci-fi somebody needs to manually go there and unify this metadata in order
[611] to make consistency obviously we have a different theater key like military science fiction and so on and obviously
[617] the reference data under reference data we call data which is of high quantities and it's external for the source right
[624] the geographic communication we have also very obvious inconsistencies one says you say US and the other United
[631] States for computer without the background knowledge this will be like two completely different entities
[637] hopefully in the source but this is a luxury which we don't get in the enterprise system we have manually
[645] curated cross links which can be used to evaluate the matchings and everything but in typical enterprise knowledge
[652] graph you have to do this completely blindly and to get this type of and to hit these problems one by one without
[659] knowing they exist so the classical
[659] Classical approach
[664] approach which every software developer start this is probably the naive but very
[670] straightforward I'm going to use the titles and I'm going to say let me try to match the identities between these
[676] two different sources so what we can see immediately is that there is some inconsistencies like the Harry Potter
[683] there is a part two and part two written with a number okay probably this is
[689] something which we can fix with a very simple algorithm like Levenstein distance or something like this the next
[696] we see the perfume I I really hope that you have seen some of these movies because they are really perfect
[701] masterpieces like the perfume the story of murder and the other source it's really the perfume they decided to cut
[707] the other part obviously the software engineer will say okay I can match this
[712] is a perfect so I can really match this as well the last the third example
[718] however is really a nasty one the pirate Lu versus the board that rocked it's
[724] completely no correlation between two entities but for some reason wiki they
[729] decided to use the European version titles of the fumes and Internet Movie Database as the u.s. source decided to
[735] use the u.s. one so there is really no correlation within these two sources but
[741] if you check the identifiers this is one in the same movie and obviously the simple example avatar okay you just go
[748] and find that there at least for Avatar movies from the different years the
[753] natural instinct is that you are going to say okay I have to include additional metadata and let's take the last example
[759] with avatar okay so we attack X to the rule and what out of a sudden happens is
[759] Results
[766] that we was ten percent of the matches by because once again these data sources
[771] create inconsistent dates one says what was the release date in Europe the other
[776] what was in the u.s. even more disappointing we see that the movie
[782] still remains even over 250,000 movies because only in 95 there were three
[789] movies Pocahontas with the same year with the same name which are different
[794] and we see that these are different is they have different durations I don't know what was the reason but there were
[801] hundreds of such movies which are absolutely ambiguous and you cannot differentiate in any way so I really I
[810] will share something personal I really hate on presentations when somebody talks about only about challenges and
[816] how difficult is a task so the next part of the presentation I will explain some
[821] innovative ways how you can really try to address this challenge and fix this
[826] identity matching problem so have you ever heard about knowledge graphs texts
[832] and weddings do you know the term embeddings okay so this is a new scientific Trenton
[838] topic which started recent years and I think it's really very relevant for the knowledge graph because this gives
[844] really direct partners a feature which is over overworked by the different
[850] users of the knowledge graphs so what is the knowledge graph this is the idea if you have a complex topology of the graph
[850] What is Knowledge Graph
[857] how you can compare and predict similar links in the graphs or similar nodes in
[863] the graph based on their connectivity the same you can do also for the links so this can be used for link prediction
[870] one of the big benefits is that it requires no input tray nning date right
[876] most of the machine learning methods obviously this task with mapping quick data with Internet Movie Database can be
[883] easily fixed if you have a machine learning because you have the training examples you are going to get the
[888] features and this is done but in the classical scenario you don't have this and you are absolutely blind so you
[894] cannot it's really I'm really somehow surprised seeing so many people talking
[899] about how they use machine learning for mapping enterprise sources because I have never really seen a complex
[906] mappings between different sources with no identifiers of beacon of gold standards in order to train a machine
[912] learning model so the basic model is thematic how we represent the mathematic
[919] mathematically this graph nodes this is a very simple example let's imagine that
[924] we have a two-dimensional space one is really the duration of the movies and the other is the charm y and let's
[931] suppose that we we're doing a simple binary watching we have a comedy and a drama for now we
[937] ignore that there are some movies which are comedy and drama in the same way and we take two movies one is The Godfather
[944] which is really a long drama free hours movie so we're going to put this vector
[949] because it's a won't movie it's goes into the drama section so we draw this vector the other is really American Pie
[956] which is something very different a short movie a comedy so the vector will
[962] go somewhere down in the space so the idea of the knowledge graph embeddings is that you represent this graph nodes
[969] is a vector space model and by combining the difference the cosine between these
[975] vectors you can predict what is to singularity in reality this is a
[975] Movie Knowledge Graph
[982] slightly more complex and let's go to England details so let's suppose that we
[988] want to make these knowledge graph and bearings for the movies and we are going to use free features one is the actor
[993] the other is the director and the third is the country of origin you can see that some of these algorithms even the
[1000] US and the United States are not Hawaii so we are going to get even some fuzziness to be absolutely sure that we
[1007] have inconsistent metadata and it will be a tough challenge for the algorithm so for each movie we let's call this
[1015] document we are going to what every row in this table so we add for every idea a
[1022] different role and its columns these are links whether the first movie has a link
[1028] to the atom the fever or whatever is his name whether it's really directed by Luc
[1034] Besson and so on so you can imagine one huge matrix which represents all the movies
[1043] and all the terms or entities which participate this huge matrix is actually
[1048] a very sparse one because even for some
[1053] relatively small models this goes something like millions - millions and
[1058] one of the biggest challenges is that if you have so complex vectors it's a very
[1063] slow process to much them obviously you can do this but to be extremely slow tomorrow vectors of so big dimensionality in the
[1063] Random indexing algorithm
[1071] past 15 years there was a very good effort how to mathematically solve this
[1077] problem and we choose one of the algorithms there is a bunch of algorithms but we prefer to use this
[1083] random indexing algorithm Alex I promise this is the most technical so I and I
[1089] will try to explain it in simple terms so the basic principle is that you have
[1094] a huge matrix which is 250 thousand rows and one heard five million columns and
[1101] in order to make this faster you you need to see the dimensionality of this matrix and to reduce it to 250 documents
[1109] to something quite 2000 or freaking 3000 there are some scientifically proven
[1114] methods like MSA and so on which are for that format it's the composition but
[1120] they are awfully slow and they don't scale so in this scientific paper a smart guy decided let's use some random
[1128] vectors elemental vectors and you see them in the table and we choose them randomly completely randomly and for
[1136] every movie we are going to get the vectors of the element of vectors of the
[1141] terms which are there so in the first row which is the I think this is the
[1148] Avatar movie you take the free actors because they are present and you assume
[1153] their vectors you remember how you some vectors you just connect them and then you're connecting the resulting vector
[1159] and in the second movie you're going to get also the other vectors and in this
[1165] case these random vectors are slightly directed in the directions where they mostly frequently concur and they have
[1172] proven scientifically actually scientifically and experimentally that if you do this over a large scalable
[1178] collection you get something very close to the matically mathematically complex model so the time to compute this matrix
[1185] because this is a linear algebra is less than five minutes and this is a feature
[1191] which is part of the database and you need really sub-second sources later on to find the similarity between the two
[1196] for different instances okay so now let's suppose there
[1202] we did these big matrix of the movies with all the matrix and wishing the dimensionality what we what we get is
[1209] features you you can start document to document type of searches like the
[1214] document this is the movie in this particular case and we can say the only which are the similar movies and the
[1220] assumption here is that if a movie is directed by one person and it gets a
[1226] senior actors you know similar Jean similar similar duration this you much
[1231] pose to the other type of movies so this is really the type of search we are going to use in this particular example
[1238] the other features you can do with this algorithm is document to term which stays for a specific actor for a
[1246] specific movie giving what is the most specific director or the actor so you
[1251] can get all sorts of dimensions or the other is turn to turn tell me which are
[1256] the actors which are mostly similar if you populate enough data you see whether they frequently play in the same type of
[1266] movies so what are really the features of these algorithms is that this is it
[1272] has all the features of the vector space models what is really a vector space model it gives you really some partial
[1278] matching so it there is a fuzziness in this so if you say how is similar to
[1284] movies you are going to get a really a very nice score saying okay it's a kind of similar but not exactly you can do
[1291] waiting so you can give some weights better to some of the features and
[1296] obviously it's very good for ranking and last but not least it has some context
[1301] context sensitivity as context sensitivity matching which means that if
[1307] because of this vector dimensionality if actors play very often together you find
[1316] them similar even if this particular actor is not exactly there so the simple ways if we apply the same algorithm on
[1323] text because it can be applied for textual terms as well is to say okay what are really the most typical words
[1332] which are for Germany and if we index political news you will find on camera marker and so on because these
[1337] are typically words which co-exist so you can really truly find semantics in
[1343] in the Mattocks okay the worst but no please parties okay you know this guy is
[1350] telling me some fancy algorithms it gave me some challenging tasks but how this
[1357] changed my situation how I can really develop a simple system which can benefit from all these features and my
[1363] role as a CTO is to talk to senior people and also to software engineer so I have to speak the language of the two
[1370] worlds and this is what we really suggest as a reference architecture and do in most of our knowledge graph
[1377] solutions so the knowledge graph it has to do several features so the first it
[1377] Features
[1383] should have be easy to consume the data and this is one of the big challenges I think it was several times mentioned
[1389] that RDF is really difficult through many software engineers so there should
[1394] be an easy way how you solve the data but at the same time in the back end you
[1399] need some either information architects or data ninjas it depends the size of
[1405] your organization who really needs to know the bitten pieces who should really care about the metadata whether us is
[1411] the same as United States and they should be digging into the data at least this is my type of experiences that I
[1417] have seen two types of software engineers one is really obsessed on API is and the programming and they are
[1423] really obsessed with data it's very hard to find a person who is really in the both worlds and it's doing the same
[1429] thing the other thing is we in our platform there is no need for back-end
[1434] development once you configure your model you are going to get automatically a graphical endpoint which is going to
[1440] consume allows your front-end developers to consume the data also as part of our
[1447] products we give a flexible data processing tools we are going to demonstrate because you are not going to
[1453] avoid this the classic of ETL type of tasks getting a CSV file it's really
[1458] tricky you have all these knows to parse the dates to fix the numbers and so on and finally we always believe in the
[1466] open interfaces in order to have open interfaces should be able to federate your graphical and point in our systems or
[1473] even if you want you can interact on the sparkle level which is offered by a graph DP which is our database okay so
[1483] let's do the whole story is how we can map these two datasource make a
[1488] knowledge graph and offer it for a single day development this is really two tasks how we can do this knowledge
[1493] graph development so gravity being one the most popular RDF databases it has a
[1499] free version and it's it has integrated features for doing ETL basically I'm not
[1506] sure if you're familiar with the openrefine this is interface for parsing in detailing the data it's part of the
[1512] database so if you go one step back wiki data is already distributed in RDF so
[1517] you can just take the data set and worry to gravity be you don't need to do any processing all the structural semantic
[1523] and other formattings are already saved for internet movie database however the dumpster in CSV format and you need to
[1531] perform some simple sitio tags when I start any with with any CSV file I know
[1537] that they're probably their spaces which are not trimmed and these are common
[1543] tasks which the tool gives you in order to quickly fix the data you need to set okay this is a number this is the date
[1549] no to CSV sources ever use the one formatting of the dates you need really
[1554] to guess what is it in order to pass it as the date types and also the fortunately in this data set they give
[1560] us the links like Internet Movie Database we keep this only for evaluation purposes these are not index
[1566] and not unknown for the model so what you need to do is to do some reg X in
[1571] order to extract them typically this is a standard job and without doing this
[1576] thing the magic will be much more expensive so for data engineer this is a trivial job the other thing is we want
[1585] to multi CSV to are here data this getting more complex but the two gives you an easy interface once you or the
[1591] data and you parse it as a table it gives you a virtual Sparco endpoint which allows it query with sparkle so in
[1598] this case if you have parsed correctly the numbers and the dates also you are going to get the right RDF types what is a literal what
[1605] is a URI and also this gives you the sparkle gives you a way to split multivalued few fields like somebody
[1612] decided that they want to give you those arms in the single fields and they said action vertical bar 3 war and you want
[1620] basically to sparked this in order to get its different values at this stage we don't do any schema level alignment
[1627] we just get the data source the two is going to read the column names and it's going to suggest predicate for every
[1633] column the next thing is what the similarity plug-in expects and it tooks
[1633] Subject predicates
[1640] accept any type of a stripper's like call it a subject predicate an object so
[1646] if we give and this is really the way how to subset which part of the graph you want to index and to apply the
[1652] schema level alignment we see in in the bottom that in the wiki data we have a
[1657] completely different model like we have entity for the movie then we have entity for though I turn and then we have with
[1664] RDF fest labor what is the atom the name in the other database because in the other internet
[1670] movie database there are no IDs for the actors so this is a simple field and we
[1675] say this is directly connected to the ID so basically what we need to do is to
[1681] use to query sparkle queries which is going to subset the graph and it's going
[1687] to index it this two queries are very trivial to be written and this is probably one of one of the only
[1687] Query predicates
[1693] developments you have to do is basically saying how to get the movies from the wiki data and which are the features
[1700] what we want to feed these predicates p16 one is really the director the
[1705] country of origin and the director and the other data set which is actually queried over the future endpoint we say
[1712] we have director named country and for some odd reason they decided actor number one actor number two and after
[1718] number three we are just going to merge this into a single mapping table and we
[1718] Single mapping table
[1725] say okay these are all actors so we put one values and now we integrate also the schema which is quite trivial and set
[1732] the translational table the wall indexing of these millions of
[1739] entities is actually a few minutes and the next thing is what we are going to do is to say okay let's find senior RDF
[1746] resources to the pirate radio this is was really this odd movie which had a totally different totally different name
[1754] and surprisingly we can see that the pirate radio now mods the boat that rocked the world so these are two
[1762] completely independent matrix how you decide that this is one and the same movie basically on the actors the movie
[1769] and the director and since we didn't apply all the metadata field drink you see that the score is somewhere forty
[1775] six percent but still this is a much higher than all the other suggested entities so yes what is the lesson
[1784] worlds that even with a limited data set and metadata curation you can get a
[1789] quite decent suggestions which are saying okay this is one of the entities and obviously this is alternative to the
[1796] string matching and this is an alternative which uses absolutely different mathematical model it does not
[1803] it obviously has some errors because of the reduces the dimensionality but still
[1809] it's writing the programming combining two different cache functions and combine combining two different cache
[1815] functions the chance to get collisions gets really minimal so before to go to
[1815] Design considerations
[1822] the wrap up I wanted to give some important design considerations and this
[1828] is purely for the software these developers why we're doing this way why we prefer rdf over property graphs there
[1836] were a couple of these questions here I just won't don't want to get into the details but I personally believe RDF is
[1842] currently a much better alternative because it gives you a schema and having scheme of these knowledge graphs is a
[1848] critical importance I I said that schema and semantics is one of the main features of these knowledge graphs so
[1855] going with property graphs you can solve this problem but you don't get it out of the box the other thing is in RDF you
[1861] have much more data sets so weak data dbpedia massive number of data sets are
[1867] distributed in RDF and I can just take this data and do not do any conversion obviously we have
[1872] reasonings and not and last but not least this is a model which treats strings for two things so if you have
[1880] loops based on and you have white okay look besson is a very unique name but if
[1885] you have will submit one of these examples you get probably 50 different
[1890] views myths and what ultimately we want to do is to work with identifiers but not labels because they will give you
[1896] collisions the next question is about visualization versus of consolidation I know that many people talk about
[1903] visualization it's the perfect way we leave the data where is it we don't do anything but in practice from a database
[1910] Theory the visualization works only for simple hookups you cannot really do
[1915] anything quite these knowledge graph embeddings with remote data which you haven't seen so in order to really do a
[1921] heavy data integration you need to pop up the data see it at least one time index it and then will be able to
[1927] process it if you really want visualization the way we decide is is to put it push it to the graph QL level
[1934] which is really the way how to federate the data and it's really not a date integration on the database model but
[1940] it's more like merging different api's on the API level the earth decision we
[1947] make is to push the integrate to integrate the random indexing and this in the similarity pudding forced the
[1953] database many people will ask why you're done pulling these data to spark and
[1959] then pushing it back imagine that you have a wife knowledge graph in these computations needs to happen every one
[1966] minute so just putting the data and replicating to spark will take a massive
[1971] amount of time and at the end you have to implement a real database in the spark engine in order to deal with this
[1978] data updates in real time so we as developers we always push the
[1983] computation as close as possible to the database in order to avoid these overheads and why we choose graphic over
[1990] over sparkin for the end user developers okay it's a very trivial day they really don't care about the specifics what
[1997] really the information architects want they want a simple API use an area tour
[2002] your application sit with the product owner and say okay this is how I want to do wise and just want to render it okay
[2002] Questions
[2009] so thank you this is our knowledge graph production assembly wine and I will be
[2014] happy to answer any of your questions
[2021] [Applause] thank you any questions anyone okay now
[2034] it's better to get them on Mike wonderful presentation in biochemical
[2043] space or life science space we also encountered this problem of finding Simon semantic similarity between known
[2050] so we apply this to go terms and then there is a scoring function that allows you to filter down from hundreds and or
[2059] five hundreds of code terms to maybe a twenty of them which are more relevant and give meaning to your result but you
[2067] shown it that the vector representation of your entities is even more effective
[2072] so do you can you comment on if this approach is better compared to
[2079] approaches that use utilize the scoring function okay so so I'll give you some
[2085] context because I know the gene ontology I has spent a quite long time of my wife developing for pharmaceutical companies
[2091] so the gene ontology is a relatively small taxonomy okay it's not trivial but
[2098] it's a relatively small defining biological process molecule structures and so on I wouldn't say that there is a
[2106] single method which is going to solve all your problems and that's why my focus is that you need to use two
[2113] different alternative approaches like two different hash functions which doesn't conflict so one we base it on
[2120] the knowledge graph similarity and the other one based on those things in URT by the way this algorithm has also the
[2126] feature two combines them in a single model this is something I haven't covered but you can do a combination
[2131] between the string similarity and the graph topology as well so my my message will be that doing this
[2140] type of mappings is not a trivial job and typically this should be a decorative process which you say okay I
[2147] do a simple string matching if if there is a single match I'm fine then for the
[2152] next level of inconsistencies and the one tear of entities I'm going to use the vector space model combine it with
[2159] the string matching so best the best results you get if you combine multiple
[2164] Guri terms to work the same because every of these algorithms gives you a different error which you want to
[2169] eliminate
[2174] yeah really interesting talk thank you um so I have a question about the last part of it so I think it was
[2174] Question
[2181] maybe last slide the one we talked about basically and I wanted to ask this
[2189] question where you say is better you have to have all the data in one place in order to be able to do this and you
[2195] can't really kind of feather a with this technique is that because fundamentally the technique you need to
[2203] assemble that matrix of everything yes yes I'm fine basically you can quit it also virtually
[2208] but the algorithm needs to see at least one time the data so in the pure
[2214] visualization where there is a remote system you arranging or where your query processor has no clue what is the
[2220] distribution of the data what is in there what is the dynamics and I don't
[2226] say virtualization is betting actually if you can use virtualization with simple hookups it's definitely the way
[2232] to go there but it really limits you you can imagine I want to join these data source with another data source
[2238] virtually this we mean to download the two sources to join it in memory and to return the results which is already you
[2243] have consolidated and you have thrown away the results because I guess I'm coming from a position where semantic
[2252] alignment particularly in schemas you know the early knowledge graph is a really important thing to be able to do so we have to do that in the underlying
[2258] data in order to get the alignment in the schemas so a global level but we're
[2263] not really in position where we can pull the data in one place yes I can imagine
[2269] so this algorithm basically can work with any even remote data basically you can but still for
[2277] some reason in order to do this matrix of similarities you need to see the data let's imagine that you have to do this
[2283] on the fly to query to remote data sources and to say any trim is something
[2289] for this avatar even avatar the simple movie so how you're going to approach
[2294] this you get the avatar drink you send it to a source you send to the other source you get a bunch of data and you
[2300] probably miss many of the results which are the same movie but with a different title so at the end you get to this
[2307] practical problem that you're going to get incomplete results or not the same expect civet II of the quiz
[2317] okay thanks well let's let's wrap up and have a go
