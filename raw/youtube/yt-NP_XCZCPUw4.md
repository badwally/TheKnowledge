---
schema_version: 1
id: yt-NP_XCZCPUw4
type: youtube
title: Masterclass Shapes Constraint Language KGC 2023
url: https://www.youtube.com/watch?v=NP_XCZCPUw4
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:23Z'
content_hash: sha256:2d29bf76d65a69d5d534fc9ba3e54f9a0f8d72429366dbc7aea0d42193e9030d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 5396
  caption_track: cached
  snippet_count: 695
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:23Z'
  user_correction: null
---
[0] Woo! We're live. Okay,
[5] welcome everyone to this master class workshop kind of thing in the shapes
[11] constraint language. Anyone of you tried shackle before?
[18] A couple. Nice. So, this is a quite introductionary master class. I'm going
[24] to go through the core concepts of Shackle. I'm also going to compare it
[30] with the more well-known owl, the web ontology language. And at
[36] the end, I'm going to give you some uh tastes of shackle use cases from real
[44] life projects that I've been on at least. And after that, we have some hands-on ex
[51] exercises. So, I'm going to just distribute this now
[57] for those of you who are in the room. So, she just could uh send it, pass it
[62] on. Uh, and for those of you online, you will find the link when we get to
[71] the exercises. And I'm going to send around a box of
[78] colors also. So, pick a couple of ones.
[87] Okay. Let's begin.
[96] I'm Veronica Hsburg from the cold
[102] country of Norway. Actually traveling from minus degrees and snow to New York
[107] and 30° C. So that was quite a weather shock for me. Uh but that was awesome.
[115] So I work at Capgeemini and as of yesterday I got the new role in
[122] Capgeemini. So now I'm obviously knowledge graph lead in IND Nordics. So
[128] quite happy with that. Um my Shackle experience stretches from
[137] 2016 and up until now. So I started working with chuckle when it was a
[144] working draft still and quite different vocabulary than the vocabulary that got
[151] standardized in 2017. Developed a couple of shackle engines for clients with working with shackle as
[158] a validation language as a modeling language and acceptance testing.
[165] Yes. But let's begin. Oh, and a tiny disclaimer for those of
[172] you in the room. I have a hearing disability. So, if you have any questions, please note them down. We can
[178] take them at the end or in the lunch break room afterwards. Thank you.
[185] Okay. So, as probably many of you know, the
[193] reason why we're here happened here back in the late 80s, early 90s with the
[200] creation of the worldwide web and Tim Bernestly vision for the worldwide web
[206] that we it was going to be a linked web o open information. We all know that how
[214] that went not exactly as expected but out of that came a lot of nice
[221] standards. So we had HTTP and the worldwide web consortium got established
[227] standardizing stuff for the web including the stack that I am very fond of which are the semantic web stack and
[236] the latest addition to the semantic web stack is the shackle language the shapes
[243] constraint language where we can validate RDF data.
[250] But before we go over to shackle, I want to establish some terminology that I'm
[255] going to use in this master class. Starting with domain and range, the good
[261] old ones. Domain and range are properties from the
[267] RDFS, RDF schema vocabulary. And the domain for a property tells us
[274] something about what to expect in the subject position of a triple. So in this
[280] example we have author as a property with a domain book. That means for every single
[290] triple where author is the predicate the the relationship the subject position
[296] shall be an instance of the class book.
[302] On the other hand, we have range.
[308] So if I want to add range for author, that could for example be person. And
[314] range is telling us something about the object position of a triple. So where
[321] author is the predicate, the object position shall be an instance of person.
[329] So that's domain and range and you will see that in the exercises afterwards.
[337] And then also something I find important is a world assumption especially when we're
[344] talking about shackle shapes and how they can be connected with our
[350] ontologies. So
[355] many of you probably know this before but repetition is always good. So the
[361] open world assumption admits incomplete knowledge and ontologies with the web
[369] ontology language has such a world assumption. So the formal definition is that the
[377] assumption that the truth value of a statement may be true irrespective of whether or not it is known to be true.
[385] So let's take an example for my toy box. So if everything I know in the entire
[393] world is the statement in a hole in the ground lived a hobbit
[399] and somebody asks me do Gandalf live in a hole in the ground.
[405] In an open world assumption, the answer would be I don't know because I do not
[412] know if Gandalf is a hobbit or if he lives in a hole in the ground based on
[418] the information I know about the world.
[425] And between the open world assumption and the closed world assumption, we have at least 10 other world assumptions, but
[432] I'm not going to cover them here. So the closed world assumption
[438] says that any statement that is known to be true uh is known to be true. That is true is
[446] known to be true. Sorry. And what is not currently known to be true is false. So
[451] it's either yes or no, not unknown. As for the open world assumption and
[458] shackle operates under a closed world assumption. So
[464] take the same example. In a hole in the ground there live the hobbit. That's everything we know in the
[470] entire world. And somebody asks if Gandalf live in a hole in the ground.
[476] The answer is no. Okay,
[482] everybody with me? Careful nods. Perfect. Then we can talk
[487] about the shapes constraint language. So the shape constraint language is a
[494] language for describing and validating RDF graphs.
[501] Some brief history of RDF validation. Some of you been playing around with
[508] spin or shapes expressions one. Okay.
[515] Because prior to shackle we didn't have any standardized method for validating
[520] RDF graphs but we did have a couple of tools or notations for doing so. Spin is
[527] one of them. Shape expression is another one and shackle became a recommendation
[535] by the W3C in July of 2017.
[543] maybe not so interesting for you then if uh there weren't many spin or shapes
[549] expression practitioners in the audience but I can mention that shackle differs a
[556] bit from spin and shape expressions is probably closer to shape expressions
[562] than spin but anyhow it differs and for spin
[567] spin is a sparkle notation for validating RDF and all shackle
[572] constraints are backed by sparkle queries. So it has their own sparkle definitions as well. So that's a common
[580] thing. Um with shackle we could uh add as many
[587] constraints as we want for one particular resource in a graph. In spin
[593] you have to create a new template for every single uh constraint. So shackle
[599] is a bit more compact and flexible than spin. Shape expressions
[606] um shape expressions tends to be or tries to be a grammar or schema for RDF
[612] while shackle is a language for RDF. So
[618] it's turtle triples or triples in any syntax that you can add onto your graph.
[626] But shapes expressions are a completely different grammar.
[631] Okay.
[637] So in my prior versions of this slides, I had this long list of different
[643] things, but I killed my darlings and ended up with these two. So the
[650] difference between uh any of you been working for some years with web ontology
[656] language couple. So both Shackle and the web ontology
[663] language are just RDF and URI and they
[668] both rely some sort on RDF schema and the main difference is the purpose
[677] of the languages. Naturally, owl is designed for inference,
[684] building restrictions, describing logic with description logic on your
[690] data, discovering logical contradictions in your information.
[697] So a reasoner or a inference engine will add information to your graph in order
[706] to fulfill the restrictions you have set for the information. While Shackle doesn't add anything to
[712] your graph and doesn't really care about the semantics of the graph either and we'll see an example of that.
[722] You can't discover negation with al but you can't can discover negation with
[728] shackle and that's because of the world assumption. So al assume that there
[733] might be some knowledge out there in the world to fulfill any statement but for
[738] shackle it's either yes or no. So shackle is a validation language and owl
[744] is an inference language.
[749] Okay. So, when to use shackle? Well, as
[757] everything, it depends and it depends on the use case.
[763] When I hear clients talking about certifications,
[769] regulations, policies, schemas, I immediately think
[775] of Shackle because there is something to be validated here and there is a closed
[780] world of information especially for regulations and we're going to see an
[785] example of machine readable regulations at the end.
[791] automation might be something for for chackle acceptance testing ontologies
[800] before it's getting pushed to any database and actually also information
[806] modeling not only for validation but we'll get back to this at the end with
[812] some real life use cases. So let's get started with the core
[819] concepts of shackle. So the shapes constraint language are built up by
[825] shapes and we have two kinds of shapes in shackle. We have node shapes where we
[831] constrain and describe focus nodes, usually the subjects of a triple. And we
[837] have property shapes describing the relationships, predicates, and the object values of a triple.
[849] And the hairy definition of a node shape is that it is a shape that is not the
[857] subject of a triple where path is the predicate.
[864] That's it. Um and here we have a node shape. We see
[872] that book shape is typed as node shape and it targets the class book. So you
[879] see that every single time I use the prefix sh that's something from the
[886] shackle vocabulary. [Music] So this means that every single
[891] constraint to follow in this shape has to do with instances of the class book
[900] and property shapes. The definition of a property shape is that it is the subject
[907] of a triple that has path as its predicate. And because that is the definition of a
[914] property shape, I don't need to type by property shapes as long as it has this
[920] predicate connected to it. But best practice is to always type your
[927] stuff. But with that said, I will do like this
[934] compromised or collapsed kind of compact. That was the
[940] word I was looking for. compact um notation in my examples in this
[945] presentation. Anyhow, we have a author shape that is typed as a property shape.
[951] It doesn't have to be, but I like to type things typed as a property shape and it has a path pointing to author and
[961] author is a RDF property or a owl property of some sort. A
[968] property And we can combine node shapes and
[975] property shapes using the resource property. So here I say that for every instance of
[982] book there might be some relationship author
[988] with some constraints. I haven't really put in any actual constraints yet, but
[993] this is the structure of how we can build constraints for subjects,
[998] predicates and objects. Okay, so let's go through the shackle
[1007] core constraint components. So I chose to divide them into the
[1012] different categories as there are described in the standard documentation.
[1022] Okay, value types. We have constraints for classes, data
[1030] types and node kinds kinds of nodes. Kinds of nodes can be Iris, blank nodes,
[1037] literals, stuff like that. But for class and data type, let's see
[1043] what we have. So I have the book shape again that targets the class book meaning we have
[1051] constraints regarding instances of the class book and I put a couple of
[1056] property shapes on them. And this notation with the blank nodes without
[1061] typing the blank node is typical in examples of shackle. But I do not
[1067] recommend writing like this in a real life project. In a project, I would
[1075] always always always name my property shapes and type them
[1082] because then I can reuse them for other node shapes and it's also easier to read
[1088] for other developers or the client themselves. But for the sake of example,
[1096] uh I use this compact notation. Okay.
[1101] Yes. Let's get back to it. So book book shape have a property shape
[1107] on author constraining that every single object
[1113] value where author is the predicate shall be an instance of the class
[1118] person. And for data type
[1125] I have a property shape on the property published. So every single object value where
[1133] published is the predicate shall be of type xsd date.
[1146] We have cardality and value ranges also.
[1151] And for cardality, it's a very much used
[1158] constraint combination of having min and max count set to one. That means that
[1163] this particular resource for example a property is
[1168] unique and mandatory. So that's a usual combination. And min
[1174] and max count are always set in integers. and value ranges ranges from min and max
[1182] inclusive exclusive. So in this example I have the book shape
[1187] again with a property shape constraining the relationship pages
[1195] to be min inclusive 10 and max exclusive 5,000. So I'm kind of strict here. So I
[1201] don't allow for any books to be more than five 5,000 pages.
[1210] Okay. And this is my favorite perhaps um string based constraint components.
[1218] So we have the min and max length of strings also as integers. We have
[1223] regular expressions. We have language in which is a list taking constraint. So you give it a list
[1232] of language tags. So you could say that for main title of a book I only accept
[1239] English and Norwegian. So then I gave it a list with English and Norwegian. So if
[1246] you encounter a book with a main title in German, you will get a violation.
[1254] And unique language is a boolean value stating that every single
[1261] string with language tag should only appear with one language tag for each language.
[1268] So only one in English, one in the region and so on. And this example illustrate the usage of
[1275] pattern. So we have note shape on books again property ISBN and then a hairy
[1284] pattern that accepts both ISBN 10 and 13. Um I have to come over to you.
[1295] So okay so you can see okay sorry about that. So I just wanted
[1300] to ask because we need to we have a eightdigit number. Um but that can start with zero. So it's
[1307] not an integer but it's like a string which should only have the um eight
[1313] digits. Yeah. Yeah. So I would probably do that shape constraint by saying giving the pattern
[1320] that it's just the numeric values and min and max length. Yeah,
[1325] I would combine minimum length, max length and pattern. Um but in pattern
[1330] you can also say the length. I can say length. Yes. Okay. Yes. If you do the reg x way.
[1336] Yes. Of finding lengths. Yes.
[1347] Okay. And then we have property pair constraints. Um a little disclaimer here. It's not
[1355] every single shackle engine available that does
[1360] support these constraint types yet. Just so you know.
[1365] Um, but what property pair constraints does, it's comparing the object value
[1371] behind two different predicates. So we could say that the object values of two
[1380] relationships or properties or predicates are the same or they are disjoint. They are less than the other
[1387] or less than or equals. And in this case I go for a person shape
[1396] with a property shape um the relationship birth with a less than or
[1401] equals to death. meaning that no person can die before they are born. So it compares the object
[1410] value of birth with the object value of death. And this um
[1417] uh you can at a project I did back in 2017 at the Oslo Public Library.
[1426] We were converting the library collections metadata from the old mark
[1434] uh things to to RDF. And a lot of the metadata was typed in
[1442] manually by librarians from these old cataloging cards. And these cataloging
[1448] cards had a lot of abbreviations that only librarians understood. They were
[1453] handwritten. So it wasn't always so easy to interpret by a human typing this from
[1460] card to computer. So after created creating shackle shapes
[1466] for the collections for books and publications, we actually discovered a couple of or more than a couple of
[1473] authors that did die before they were born.
[1482] And then we have the logical constraint components. I'm going to show you a example of usage for these when we get
[1489] to the use case section. And all of these are list taking
[1495] constraints and we have not and or and X1. X1 is basically the same as X or.
[1505] So here for person person shape again we have a node shape targeting the class person and we put a or constraint on the
[1513] node shape not on a property shape but on the node shape and this or
[1520] constraint is a list taking constraint takes in two elements. So it takes in
[1525] two property shapes. Okay. And the first one is a property shape on first name
[1532] with a min count of one. And the second element in the list is a note no a
[1539] property shape on last name with a min count of one. That means that for every
[1545] single person we expect them to have at least one first name or at least one
[1550] last name. Both is fine. With an or constraint, you can have both valid for
[1557] the whole expression to be valid. Um, but it must have at least one of these fulfilled for the whole expression to be
[1564] valid. If we have put and instead, we would
[1570] have expected both first name and last name to be valid or to be there for the
[1576] expression to be valid. And for exor it would have been either
[1582] first name or last name not both.
[1588] Okay. And then we come to something you can do
[1593] in shackle that you can't do in owl and that is
[1599] setting the object value of a triple to be
[1605] either a class object property
[1610] or a string data type property. data type properties and object type properties are disjoint sets in but
[1620] doesn't care about that. So you could support both
[1625] object values for a property
[1631] and you can also type resources to be both a shape and a class
[1638] to confuse you even more. But it's all triples, right? It doesn't matter. What
[1645] matter is what purpose you're using it for and what perspective you have on the
[1650] data. Okay, last category of stuff. Uh,
[1659] look at the time. Woo, we have a lot of time to draw stuff. Awesome. Okay, we
[1664] have the shape based constraints. We have already seen the property, right? Linking node shapes and property shapes
[1671] together. But we also have something called node which is inheritance of
[1677] shapes. So a node shape can inherit constraints from another node shape
[1683] using the node relationship.
[1688] And some other things we can close a shape. And when we close a shape, we
[1695] expect that every single property that comes in with the data is
[1702] constrained. So if the shackle engine see a property that is not constrained,
[1708] you will get a validation result produced. So an error.
[1714] And when you close a shape, they also expect you to create a
[1722] property shape for RDF type. There is no need for constraining RDF
[1729] type usually. So you can put it as a list element to ignored properties. So
[1736] the ignored properties constraint takes in a list of elements of properties to
[1743] ignore. Has value points to a default value of any kind. in is a list of values of any
[1751] kind.
[1763] RDF type is ignored in a closed shape a book. Yes. And does it mean that it it doesn't
[1769] care about its shape? That's the one I think I get that you don't have to set
[1774] the shape that it needs to check that it's a class, etc. But does it also say that if RDF type is missing for book or
[1780] if RDF type exists for book, it doesn't complain. It doesn't care about RDF type at all. Yeah.
[1785] Whether or not it's there or not. Exactly. So the ignoring is not only ignoring it in terms of shape, but also
[1791] ignoring terms of closed. Yes. Yes. Yeah.
[1804] Okay. That's it for the core constraint components. Any questions before we go
[1810] on to the validation result vocabulary?
[1817] Okay, I'll move on then. So what do we
[1822] do with all these constraints? So usually we use it for validation, right?
[1830] So all these constraints that we create for data is usually stored in its own
[1836] file or graph. We call it the shape graph. And all the instance data or
[1844] ontologies for that matter, but all the data you want to validate comes in as a
[1850] data graph and you pass those two files into a shackle engine and you get the
[1856] validation report in return. And that differs from implementation to
[1864] implementation for shackle engines whether or not you get a result when
[1869] um it confirms true. You should get the triple confirms true. But not every
[1875] implementation actually does that. And if it confirms false,
[1882] yeah, that's the result. If everything is fine, confirms true.
[1889] But if it confirms false, you will get a graph in return stating exactly what
[1896] went wrong according to the shapes that you created for your data.
[1903] So the validation result vocabulary consists of information about focus node, result path, and value. So that's
[1911] the triple that caused uh the valid uh violation.
[1918] You have the source shape. So what shape is the constraint that was broken found?
[1925] You have source constraint component detail. So you can inherit from other
[1931] results as well. Annotation property with some details and severity level.
[1938] Per default. Every single shape has severity level violation which is the
[1944] strictest. But you also can have information or warning directly from the
[1949] shackle vocabulary or you can write your own.
[1954] That's the nice thing about RDF, isn't it?
[1959] Okay. So let us do an example. So this is my data. I have a book, The Hobbit, which is a
[1968] book. It has the title The Hobbit or There I'm back again in English.
[1974] The author is Tolkien which is a author that is a subclass of person and Tolken
[1980] is born in 1892
[1987] and these are my shapes. So I have the book shape.
[1994] I get so confused with so many screens but yeah this is the book shape
[2000] that targets the class book. Meaning I constrain instances of the class book.
[2008] I have two property shapes, title shape and author shape. Untitled the shape is
[2015] about title data type string. Author shape path author
[2023] expects authors to be object value for
[2028] the property author. And I also have some stuff for persons
[2034] name shape on the relationship name data type
[2039] string should have at least one and also book should have at least one author
[2045] connected to them. Okay. So given this data
[2053] and these rules
[2058] I will get a validation result in return stating confirms false.
[2066] And why is that?
[2072] Why doesn't title pass through? Anyone see that?
[2090] So we have the title shape over here on the path title. So that's fine. The
[2095] naming was the same. So it was the same idea. But the data type is string. And
[2100] what data type do I actually pass in my data graph?
[2106] lang. Yeah, I pass a lang string, right? So that will fail because I pass a lang
[2113] string to something that expects a string and that's not the same.
[2119] So the data type should be RDF lang string in this case
[2124] and then poor toolken produces a validation result also.
[2134] And why is that? So we have the author shape
[2141] to author min count of one. Let's see.
[2147] Author mean count of one. That's fine.
[2153] And author is some kind of person. So let's see. We have a name shape min
[2159] count of one
[2164] and toolken only have the born relationship. Born is
[2170] not constrained but that's completely fine as long as you don't close the
[2176] shapes. This property will pass true but
[2182] it's not checked since we haven't constrained it. So it could be anything.
[2187] But a probability we did constrain was name
[2193] with a min count of one. So we should have one relationship name here pointing
[2198] to some string. So that's why and the validation result
[2206] will look like this for those two graphs. If I pass those two into a shackle engine, in this case the RDF for
[2213] J shackle engine, I will get this as a result.
[2219] So I get a blank node which is a validation report that confirms false
[2227] and when it confirms false I will get one or more results connected to the
[2232] validation report. So I have two results here because I have two errors and the
[2238] first result is another blank node but they are named in RDF forj's shackle
[2244] engine at least and the RDF forj shackle engine is also the same as onto text DB
[2250] uses the graph DB and it's developed by a Norwegian some
[2257] shameless uh promotion of Norwegians there. Anyhow, the first node is the
[2263] validation result and the focus node is the hobbit. Source constraint component
[2269] is the data type constraint component because we passed on a lang string but
[2274] the shape was expecting a string. Source shape is title shape path is
[2280] title and value we get the value from the data graph.
[2286] Um second result is a result focus node on toolken min count constraint
[2293] component since we didn't have m count of one for name we had zero names
[2302] sort shape name result path name and there is no value to be displayed for name.
[2308] Okay. Yes.
[2314] Other nice things to know about shackle that I don't cover too much in this mask
[2319] class is that you can deactivate shapes. So if you reuse shapes from
[2327] other places for example the commission has published a lot of shapes for different things. So if you reuse some
[2334] of those you can deactivate those you don't need. Uh we have a lot of annotation properties in shackle also
[2342] name and description label and comment. You can order and group stuff. And we
[2350] have default values also. And we can do syntax checking. And most
[2358] shackle engines actually do this syntax checking of of graphs.
[2366] Okay. I'll just walk past that one since it's outdated.
[2375] Okay. Any questions before we move on to the shackle stories?
[2382] Nope. So, as I mentioned, I've been on a few
[2391] shackle cases out of out at clients.
[2396] Since I'm a consultant, I get to work with different kinds of clients in different kinds of industries and
[2403] domains. Um so I get a lot of insight
[2408] and experience from different stuff and different use cases and different
[2415] personalities or what to call it. Okay. So the the
[2420] case that I've been at the longest is probably the Norwegian Maritime
[2425] Authority that I've spoken about prior at this conference too. Um,
[2433] and at the Norwegian Maritime Authority, we were creating machine readable regulations.
[2439] And the regulation isn't supposed to admit incomplete
[2444] knowledge. What's then the point of a legislation or a regulation?
[2452] So we chose to model the data in shackle for for the maritime authority and we
[2460] quickly discovered that the relationship between node shape and property shape
[2465] actually fitted the use case of regulations quite well because a regulation is built up by requirements
[2472] and requirements has one or more scopes. At least for the maritime authority
[2479] regulations they did have that but I think it's quite usual in other uh
[2484] regulations too. So what we did we created a pipeline that uh consisted of
[2493] a NLP module reading the regulations producing or finding context and
[2502] concepts passed them on to some RDF transformation that generated chuckle
[2507] shapes. So here we have
[2512] the identific ID for a regulatory requirement. It's
[2519] typed as a requirement and a node shape. We have some metadata connected to it.
[2525] Some very fine title and theme and label. The label was the same as the
[2531] title of the paragraph because every single paragraph is a requirement and
[2536] every single part of a paragraph is a requirement and then we can add the different scopes
[2543] that are described in the requirements as property shapes.
[2550] So this have the property or the scope of build date after 1998
[2558] 0102. So the build date thing is a scope and
[2564] it's a property shape. It's on the path built date and it's min
[2570] inclusive that particular date.
[2576] So that's a characteristic connected to a vessel that is described in this requirement.
[2582] So on the end user side, we can ask
[2587] questions as I have a fishing vessel that's one scope that is 8 m long and
[2596] it's built on 3rd of January 1998. what requirements
[2602] applies to me in order to operate in Norwegian waters. So then we can quite easily
[2610] pass those scopes in a parameterized sparkle query running on all regulations
[2620] maintained by the extracting exactly the requirements that fit those
[2626] characteristics. ignoring all that is irrelevant. So that
[2631] might be five requirements from regulation A, 10 requirements from regulation C, none from regulation E,
[2639] and one from regulation Z. So you don't have to read regulation up
[2646] and down in order to find what is applicable for you. If you're interested in uh hearing more
[2654] about this project, I gave a talk about it at Lutico last year. So you can find
[2660] that uh I will push the slides to git afterwards also and all the links are
[2665] clickable. But if you go to ludico.com uh it's in the index list at the front
[2672] page also. Okay.
[2677] And another case at the Norwegian Maritime Authority still that hadn't and
[2684] that is not the insight portal as we saw on the previous slide where you ask for
[2690] information here we automate issuing of personal certificates.
[2698] So if a sea person wants to be a master mariner, you have to have some merits, a
[2706] CV that lets you get that certificate and that is some has much to do with
[2713] what certificates you have from before or what kind of seagoing service you
[2718] have. Um seagoing service of this duration on this kind of vessel. That's
[2724] a lot of different characteristics that is relevant here. So
[2731] all these uh requirements for getting a
[2736] certificate is described in one regulation and that regulation
[2744] did not look like this because this is quite a easy representation of
[2750] regulatory requirements. But we had to model the requirements in
[2756] great great detail because we're going to automate issuing of personal
[2761] certificates. So what we did when a person wanted to apply for a new
[2766] certificate luckily in Norway everything is available through APIs. So we can
[2773] extract information of that person from APIs from the Norwegian welfare system, previous
[2780] employers, educational institutions and so on. So we created this 360 profile
[2788] for that person and then we compared his
[2793] merits with the requirements for the achieving the certificate.
[2800] And if everything passed, thumbs up. Go ahead, get the certificate. If not, you
[2807] get a detailed graph in return stating exactly what the person is missing in
[2813] order to get the certificate. So that's a quite valuable response for the one
[2818] applying for the certificate. And since the requirements for
[2825] certificates are full of equally valid
[2830] alternatives. Pretty much the whole file looks like a
[2835] combination of logical core constraint components. And these
[2841] are their own shapes with detailed descriptions of seagoing service
[2848] requirements like duration, gross tonach of a vessel, trade areas and so on.
[2859] Acceptance testing is another one. And that is a case I'm working on right now
[2866] for a client in the automotive industry.
[2871] So my client, they have a lot of different RDF projects running in
[2878] parallel. There's a lot of different stakeholders. There's a lot of different developers and architects that are going
[2885] to produce RDF files. So we have written some standard
[2890] guidelines for how to work with RDF for that organization.
[2895] For example, that every single class shall have a label. Every single class or property shall have a comment. Those
[2903] kinds of things. They're quite easy, but we need them written down. So we ensure that everyone actually follows it and
[2911] that every resource in the whole graph has that label that we need. So we were
[2918] consistent and we use whatever tool we like as a
[2926] developer or architect and then we produce RDF files. But before we can
[2932] commit them to the git repository or push them to the database, we need to
[2937] pass a shackle ac acceptance test. And that test describe
[2945] that every single class should have a label for example. So we don't check the actual content of the graph but we check
[2951] the structure of the graph. So a simplified example of that
[2960] we have a RDF RDFS class shape targeting the class RDFS class. So everything that
[2966] is typed as RDFS class should have a
[2971] label at least that is unique and mandatory
[2978] and string. So that's quite strict also. So we only allow one label for a class.
[2986] In the project I'm on, we don't allow just one label. We allow several more, but for the sake of example.
[2996] Okay. And the last one, I had real fun trying to find that project again
[3003] because this was the first shackle project I ever did. It was for the Norwegian digitalization agency. Um, we
[3011] were going to create um, I have no idea what it is in English, but in Norwegian
[3018] it's uh, oftent electronis posternal. It's a very very public sector kind of
[3024] thing, but basically it's an inside portal. It's a database of all documents
[3029] produced by public agencies in Norway because every public agency have to
[3035] deliver data to the national archives and this is the inside portal for that.
[3044] And in Norway we have this weird archive format called Norwegian archive format
[3049] or archive standard. Um it has come in many different versions. So in this case
[3057] we had to support new work 4 which was described in DTDs
[3064] and work five described in XML XSDs
[3070] and we created a script
[3075] parsing XSD into shapo. So we ended up with this
[3082] the schema for Norwegian archive standard into
[3088] uh the XSD schema into the shackle schema instead.
[3094] So when new data were coming in, we could validate if they were following
[3101] the structure of NUR, the Norwegian archive standard.
[3111] And this uh in this project we had to implement our own shuttle engine. And
[3119] that was then following the working draft vocabulary of Shuckle which was
[3124] completely different from the one that was standardized. So whatever happened to that shackle engine? I don't know.
[3133] I hope it's uh replaced with something more sound. Okay, let's get to work. So everybody
[3141] has a paper sheet. Somebody missing a paper
[3158] paper. Okay. Awesome. And for those of you
[3165] online,
[3175] uh yes, this URL, uh just give me a
[3180] second and I'll share it with those of you that are online.
[3196] Can I just paste things in the chat? Right. Organizer man,
[3203] I can paste things in the chat, right? That that uh goes to all attendees.
[3210] Uh I can paste things in the chat that goes to everyone. Yeah.
[3217] Okay. like that. So online we have this mural and here in
[3226] um New York we have paper and pencils.
[3232] Uh I tend to do this exercise when I uh throw my
[3242] semantic knowledge graph introductions. I usually use pen and paper. Uh I have
[3249] no idea how it will work out in a narrow master class as this only for a shackle,
[3255] but we'll give it a go. Okay. So,
[3261] um I'm trying to describe a very simplified
[3267] ontology for publications and books. So,
[3276] Work is like the main class of all stuff in this world. Books, movies, operas,
[3284] albums, whatnot. They are works and books
[3290] come in different kinds of publications. So we have several Norwegian publications for The Hobbit. We have
[3299] uh ah there. So these are all publications of the
[3305] same work. So we have the German, English, Norwegian, Finnish and Swedish
[3311] and new region versions of The Hobbit
[3321] and both publications and work have different kinds of characteristics
[3328] connected to them. So what I want you to do now is to pick one or two concepts
[3335] meaning these blobs and one or two properties connected to
[3343] them and try to describe them with the shekele core constraint vocabulary
[3353] and while you do that I will go to sleep. Oh, I will check the questions in
[3360] the chat on the left.
[3369] Sorry, I I have a really bad hearing, so I need to come come close.
[3374] So, we just create any shape. It's not like just try to write any shape.
[3379] Any shape for some of the concepts in the drawing. Okay.
[3390] question. How can a binding be a subclass of both
[3398] the hard cover and right here? Oh, the arrows probably go the wrong
[3404] direction. Should it be this should be a value, not a subclass? Yes,
[3411] because those should be mutually exclusive. Oh yeah. Yeah.
[3418] Yeah. Probably. And also the publication shouldn't be an
[3426] instance of book. It should be a subset book.
[3432] But it's not that important how the the publication ontology looks like. Just
[3437] get you thinking about creating shapes for some of the concepts that are visualized here.
[3488] [Music]
[3546] It has some colors.
[3567] That's not
[3602] Yeah.
[3627] My question was there's already lots of we all this
[3634] there is a lot of like thousands of all thousands of violations. Yeah.
[3639] What what how how I'm able to have an overview about
[3646] all these thousands of things. Okay. Yeah. Yeah.
[3654] Depends on the implementation also but you can do validation transactional. So you don't need to like validate the
[3661] whole database to begin with but you can do it bit by bit. Um and also it's typical that you
[3671] implement some kind of methodology for catching the the salt props. If you
[3679] expect that there will be thousands of of breaches,
[3684] if you can uh perhaps put all the validation results into its own data set
[3690] and do sparkle analysis on the the results.
[3696] So you can filter out parts of the the result before you do anything with the
[3702] data. All right. So that means we are going for the external cause for that.
[3708] We're going to the going to the external. So we can't do that with the exchange. We can't do that.
[3715] Can we do that? For the the can get can generate a summary a summary
[3722] of uh oh it's summary. Yeah. summary of this kind of thousands
[3729] of uh violations, right? Yeah, I would imagine doing that with
[3736] sparkle validation at some point. So that's better.
[3742] Okay, I see. I see. Yeah, that's making
[3777] This is just Facebook.
[3784] [Music]
[3789] explain. So now you kind of need to do the thing without
[3831] Okay. So, now I'm going to give you a couple of plot twists. Um how many of you have selected
[3840] um publication or book? Couple of ones. Okay.
[3847] Um for those of you who have selected publication or or book, I want you to
[3853] cooperate the inheritance from
[3859] um from work to publication. So make use
[3864] of the node constraint when describing publications, books at work.
[3874] Okay. Yeah. Awesome. And who of you have selected
[3881] publication with published property?
[3888] Yeah. I want you to support both dates and year
[3894] as a object value for the published relationship.
[3903] And who has selected?
[3910] Let me see. Author person, translator person. Yes,
[3920] there I want you to add a layer between
[3927] this and person like add a new class translator that is a subclass of person
[3934] and a new class author that is a subclass of author and try to incorporate the node constraint there
[3941] also with inherited. So what characteristics
[3946] is applicable for only translator but it's not as generic as for persons.
[3953] So is there something unique for translators? Are there something unique for authors?
[3963] So publication is supposed to be a subclass of book here.
[3969] So this is a subclass. Yes, it's supposed to be a subclass. There's a typo. Yes. Thank you.
[4183] Okay, let me do a final spy around and then uh
[4189] we can start addressing some of the plot twists that
[4196] I gave you. So, um three to four more minutes
[4323] Okay, great work everyone. Now I won't be
[4329] jumping around. I will sit here for a while and go through some of the plot
[4335] twists that I gave you. And I see that I have some minutes left actually. So, we
[4341] might be able to go through quite a few. Uh after that, I have a couple of
[4348] announcements that I'm looking forward to giving you. Um that is Shackle related of course.
[4356] Okay. So um I could start by showing you
[4365] I've created a git repository for the master class
[4372] which you can find on my GitHub account
[4377] named after a cheesy book. Um yeah and under
[4385] there on my account you can see at the top there you have the shackle
[4390] masterass. So there you can find the slides and
[4397] data from all my shackle master classes from the first one at knowledge
[4402] connections in 2020 and knowledge graph conference 2122 and this year if you
[4410] want to see more examples from previous years also you can also find a demo. Any
[4417] of you read Java here? Ah few. Okay. Um I have a demo you can
[4426] spin up in in Java using the RDF for J shackle engine uh which has a main file
[4432] input data input shapes and then gives you the validation result in return.
[4441] Uh yes, but I'm going to head into the data folder
[4447] and in the data folder I will choose the one for 2023
[4455] you can see the exercises here and I've also created some um
[4464] instance data Huh?
[4473] What was your the URL?
[4479] Yeah, so some instance data from the books
[4486] that was on my picture. So, I have The Hobbit
[4492] as a work with the title and author and published
[4497] and stuff like that. And I also have all the different publications
[4503] of The Hobbit that I found in my bookshelf.
[4514] And for publications I have title, publisher, translator,
[4520] publication of and published.
[4525] And then I have some data connected to
[4531] the persons relevant for for this instance data and companies.
[4541] In addition to this abox data, I have created a
[4546] very very very simple RDFS file describing the different properties
[4553] and classes found in the abox data.
[4560] And what I just did was navigate to shackle.org or which is a JavaScript
[4568] powered playground for Shackle to experience firsthand.
[4575] So here I just copy pasted in the instances from the instant instances
[4582] file and I put the RDFS stuff at the
[4587] end. So if some of you want to follow along,
[4594] I'll give you a minute to copy paste the information. Uh when you start shackle
[4601] playground for the first time or visit the page for the first time, you can see
[4607] the data graph is in JSON LD. But if you click on the drop-own menu, you could
[4612] choose to turtle instead.
[4622] V there. Thank you.
[4647] And if you're copy pasting both files into the playground, please remove the
[4654] prefixes from one of the files because you don't need to repeat them twice.
[4685] Okay.
[4691] So this is my view at the moment. I have prefixed RDF shackle owl XSD
[4701] and my empty prefix. I don't actually need every single one of those I see now
[4708] because I don't use owl and I don't use shackle for the data graph, but I need
[4714] shackle over here in the the shapes graph.
[4720] And I'm just going to use my my own name space datacapgemini.combooks
[4728] for both data and shapes. It might be more clever to distinguish
[4736] those namespaces, but I'll go for one name space for the
[4744] sake of example.
[4750] Okay. So, I'll start off with the publication shape
[4757] which is a node shape and be careful with tabbing in in the
[4764] playground because you will just move to the next item on the web page. So, use
[4769] space for indents. So node shape
[4775] target class publication
[4783] and I want to constrain some of these
[4788] properties. So I'll just choose a couple of ones.
[4795] And remember if you don't constrain a property the shackle engine won't care
[4801] about that particular property. So it will just run through the engine and nothing happens.
[4809] So I can start with publish then
[4819] no because published is a part of both work and publication. So I will start
[4825] with publication of
[4833] publication of shape which is shape property.
[4845] So my initial note shape is a publication shape that targets the class
[4850] publication. Meaning we are constraining everything
[4856] regarding instances of a publication.
[4862] And the first property shape I'm going to create for a publication is publication of
[4871] which is a property shape and we remember the definition of a
[4878] property shape. It have has to have a predicated path pointing to something and in this case the path is publication
[4887] of and
[4893] I think that any publication or the publication of
[4900] says something about what work it is connected to and no publication
[4906] is like standalone. It's always to connect uh connected to some kind of work.
[4914] So I will put in a min count of one.
[4922] And can it be connected to more than one work? Well, I don't actually know. So in
[4928] this case, I would have to ask a domain expert, which would have been my my
[4933] client. uh but for time being I'll set it only with min count one and not any
[4939] max count but at the object position of
[4946] publication of the expected instance of work.
[4953] So I will then put in work as class.
[4965] So then we have a node shape for publications and we have one property shape for the
[4971] path publication of
[4976] and every single publication must have at least one publication of relationship
[4983] pointing to some instance of the class work. So let's run that and see.
[4991] So then I hit update for data and update for shapes graph.
[4998] And I have an error somewhere in my data.
[5018] Okay. Never mind. I'll just strip it a bit.
[5025] So try to use only the instance data then.
[5035] Okay, I got some error here. say I have a validation report
[5043] on publications of and it's regarding book number three. So let's have a look
[5051] at that instance. So you can see that this publication
[5058] which is the Finnish version of The Hobbit doesn't have a relationship
[5065] publication of and we set a constraint to be publication of for a mean count of
[5072] one. Meaning that we expect at least one publication O for
[5078] every instance of publication. I don't get the error. H I don't get the error.
[5092] You copy pasted the data from uh GitHub. Then have you pushed update for both
[5101] Windows?
[5125] But nothing happened.
[5135] Count one. Yeah, it shouldn't be. It should be right. Yeah, that's weird. We can have a look at it
[5140] after afterwards.
[5149] So in order to fix that, I of course need to add a publication of for this
[5157] instance of publication. Publication of and it's a publication of
[5164] The Hobbit. And I see that time flies.
[5169] Unfortunately, I was hoping to do even more live examples.
[5178] Um, but yeah, I I can quickly show how you
[5185] would solve one of the plot twists like expecting both
[5192] date and year for published. So that
[5198] will be like a published shape a property shape
[5205] on the path published published. Yes.
[5213] And then we would have put in a or shape which is list taking and we would have
[5220] given it data type XSD
[5225] gear or data type
[5231] XSD date as blank notes.
[5244] So that would be the solution for that and published shape would have been a part of work
[5252] a work shape
[5263] with a that targets the class work and have a property to tablet shape.
[5270] And then publication shape would have had a sh node to work shape. So it
[5278] inherit every single constraint for work into publication as well.
[5285] And with that I have to jump over to the presentation again.
[5291] Only two minutes left. So a couple of announcements then. Um, me and Evil
[5300] have created a shackle wiki
[5305] on log meaning that the wiki itself is a
[5310] graph. You can traverse it as a graph because all the contents are tagged and
[5315] every single paragraph is a node in itself. So
[5321] please roast this if you like. You find all the information on core constraint
[5327] components, validation report, even the sparkle based constraints and rules in
[5333] shackle. And
[5338] if you want to hear more from IU, he has a talk on Thursday at 10 about personal
[5346] knowledge graph and how to con construct your personal knowledge into a knowledge
[5352] graph. And then second announcement, I'm writing a book on checker
[5361] with a working title checker for the practitioner. So if you're interested in following
[5368] that work or if you're interested in contributing with content on real life shackle cases, I would be more than
[5375] happy to hear from you. I'll push the slides to the GitHub
[5381] repository. All the links in the slides are clickable in the PDF.
[5387] And with that, I'll say thank you for attending.
[5396] How do you say thank you in Norwegian?
