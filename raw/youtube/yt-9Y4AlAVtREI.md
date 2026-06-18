---
schema_version: 1
id: yt-9Y4AlAVtREI
type: youtube
title: 'Neo4j Cypher: Getting started! | Neo4j Tutorial'
url: https://www.youtube.com/watch?v=9Y4AlAVtREI
authors:
- AmpCode
ingested_at: '2026-06-18T01:38:13Z'
content_hash: sha256:f2df3a7f0b3312bfaf6870cfd2cee92de790d5947e23bf0067d2afe39b18c2f6
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AmpCode
  channel_url: https://www.youtube.com/@ampcode
  duration_seconds: 756
  caption_track: cached
  snippet_count: 303
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:13Z'
  user_correction: null
---
[0] hello and welcome back to the channel I
[1] hope you have set up your new 4G on your
[4] Windows PC so that we have seen in the
[6] previous lecture so this lecture is all
[8] about Cipher fundamental and how we can
[10] write a query to fetch the data from the
[13] neo4j database so without further Ado
[16] let's get into it okay so before jumping
[16] Getting Started with Cypher
[19] on to writing queries we need to First
[21] understand what exactly is Cypher and
[24] why we are using Cipher query language
[26] instead of any other programming
[27] language like SQL so let's discuss that
[30] now we already know that a property
[32] graph model which is leveraged by neo4j
[35] database is comprised of different kinds
[38] of nodes and relationship and we will be
[40] also having some properties so we can
[42] relate it to as a key value pairs of
[45] data in our nodes or it can also be
[48] present in the relationship to add more
[50] context into your graph so this may
[53] sound simple so the simple combination
[55] of nodes and relationship really makes
[58] the powerful property graph model and if
[61] you talk about the patterns patterns are
[63] nothing but the combination of these
[65] nodes and relationship which can
[67] represent simple as well as the complex
[69] graph traversals or the parts that we
[72] are going to see in the next lecture so
[75] pattern recognition is like the
[76] fundamental of how our brain works our
[79] brain likes the visual data it's like
[82] for example visual diagrams or any
[84] memory matching game so Cipher is also
[86] based on these patterns and finding the
[89] simple or complex patterns inside your
[91] data so this will make Cipher a very
[94] simple and logical language to learn for
[96] every developer so if we talk about the
[99] cipher syntax as you can see here Cipher
[102] is like designed to be very human
[104] readable so its construct is like based
[108] on English Pros as well as the
[110] iconography so we can easily convert any
[113] data any nodes and relationships into
[116] the cipher query because its syntax will
[119] be similar to how we see that in our
[121] actual graph and it makes the syntax
[124] vary visually and easily understandable
[127] so let's talk about it with some simple
[129] example
[130] so as you can see here we got a very
[130] Cypher Syntax
[133] simple graph in which we have the person
[135] node company and the technology node and
[137] we also have different properties which
[139] is name in the person node as well as in
[142] company as well as in the technology we
[144] have the property as a type and we have
[147] the relationships between all these
[149] nodes
[149] so as you can see we can easily convert
[152] this graph into like a readable English
[155] phrases so as you can see we can say it
[158] as these Jennifer person likes graph so
[163] graph is nothing but a technology and we
[166] have the likes relationship between
[167] these two nodes as well as we can say it
[169] as Jennifer is friends with this person
[172] which is another person which is Michael
[174] and also Jennifer works for neo4j so we
[178] have converted this graph into the
[180] English phrases so the next step would
[182] be we want to convert it into the cipher
[184] and we are going to see it in the
[187] further lectures where we will see what
[190] is like a cipher keywords and how we can
[193] convert this graph into a cipher query
[195] language to fetch different patterns
[198] using your data so as we already know
[198] Representing Nodes in Cypher
[201] that the nodes and relationships are the
[203] fundamental components of every property
[206] graph model so as you can see here how
[209] we can represent nodes in the cipher so
[212] it is very simple if we talk about the
[214] previous examples only we had like the
[216] four nodes as well as relationships
[218] present so as you can see we got the
[220] four nodes here so nodes are nothing but
[223] which represents the data entity in your
[226] graph and you can identify the nodes in
[228] your graph using the nouns or objects so
[231] as you can see we got the two person
[233] which are named Michael as well as
[236] Jennifer respectively and we also have
[238] like the company and Technology entities
[240] which represents the neo4j node as well
[243] as the graph node which is the type of
[245] technology so this is how you can
[247] represent nodes using the cipher query
[250] language so to sum it up in our graph
[253] Michael neo4j Jennifer as well as the
[256] graph are nothing but the nodes in our
[259] knowledge graph so as you can see for
[262] representing this nodes in use in the
[264] cipher query we have to surround the
[267] node using the parenthesis so as you can
[269] see in the round brackets we will
[271] represent our nodes so now let's talk
[273] about the variables and the node labels
[275] so if you want to later refer our node
[279] in the cipher query we can give it a
[281] variable which is like a similar to
[283] other programming language like Python
[285] and you can represent the variable
[287] inside the parenthesis itself so for
[290] person you can mention like P or t for
[293] think but this could be readable in the
[296] real world because if your queries are a
[299] bit complex and you have like a bigger
[301] queries then putting a readable name
[304] like for person you can directly call
[307] your variable like a person so that will
[309] be more readable than just providing P
[312] so this is like a simple tip to write
[315] Cipher queries so you can refer that
[317] node in the subsequent commands in your
[319] Cipher queries that is very simple and
[322] if we talk about the node labels so if
[325] you remember from the property graph
[327] model we can also group our nodes in the
[330] labels so let's say an example of like a
[334] movie graph so in the movie data set we
[336] will be having different kinds of notes
[338] so some nodes will have like an
[340] information about the movies so we can
[342] provide a movie label and group all
[345] those nodes together similarly we can
[347] have like the nodes which represent
[350] different properties belongs to some
[352] actor so if the Keanu reuse is like a
[356] node in our graph that belongs to the
[359] actor label and similar goes to the
[361] director as well as the person who watch
[364] the movies as well as the ratings and so
[366] on this could be anything so if you want
[369] like you can have like different labels
[372] in your graph so those could make sense
[374] as well so in the movie recommendation
[377] system having all these nodes would
[379] really make sense and you can group that
[381] together so a person could be like an
[384] actor or a director so you can apply
[386] multiple labels to that node and group
[389] them together
[389] so if we compare it to the relational
[392] databases node labels are just like the
[395] table names so if you have in the movie
[398] data set in rdbms you will be having
[400] like a movie table then you will be
[402] having the actor table so to group all
[405] those relevant records together similar
[407] concept applies to the neo4j also in
[411] which we will be having different kinds
[413] of labels so that to group your relevant
[416] data together okay so now we will talk
[416] Representing Relationships in Cypher
[419] about the relationships in Cipher and
[422] how we can represent it in a cyber query
[424] so to add more connection and richness
[427] to our graph we will introduce
[429] relationships in our graph so earlier we
[432] only had the notes in our graph but
[434] those are not related to each other so
[436] in this case we have brought the
[438] different relationships and it has a
[441] certain direction in our graph so as you
[444] can see we got the likes is friends with
[447] and the works for relationships so so
[450] these are like the different
[451] relationship types in our graph so this
[455] also should be readable because at the
[458] end of the day our graph should relate
[461] to the English phrases because it is
[464] represented as a simple English language
[466] so as you can see here everyone should
[469] be able to read that graph because we
[471] have brought like the person label so we
[474] already know that this particular person
[476] for example Jennifer Phil likes some
[479] neo4j technology so that there is a
[483] relationship going from the person to
[485] the technology so as you can see we can
[487] relate our relationships and this makes
[490] our graph more connected and also it
[492] increases the performance while
[494] traversing through the complex patterns
[497] in our data and similar to the nodes as
[499] well we can have like different
[501] variables for our relationships so we
[504] can assign like L variable to the likes
[506] relationship then if variable to the
[509] east friends relationship and W variable
[512] for the works for relationship it
[514] totally depends on you and you can refer
[516] them in our subsequent steps in your
[519] Cipher query so this is very helpful and
[522] it is like similar to the other
[524] programming language so once we jumped
[526] in to writing our first Cipher queries
[529] then you will understand how we can
[531] utilize these variables so so far we
[531] Node or Relationship Properties
[534] have talked about the most fundamental
[536] components of our property Knowledge
[538] Graph which is a nodes and relationship
[540] but the last piece of this is the
[544] relationship or a nodes properties that
[547] we are going to see now so as you can
[549] see these properties are nothing but a
[552] key value pairs which will provide more
[554] details and the additional data in our
[557] nodes as well as the relationships so as
[560] I already told you that properties could
[561] be also in the nodes as well as in the
[564] relationship so as you can see to
[567] represent this in the cipher we are are
[570] using the curly braces in our notes or
[573] the relationships so you already know
[575] that the node is represented between the
[578] parenthesis and I forgot to told you
[580] that the relationship is represented in
[583] the square brackets so you have to
[585] remember that that is like a
[586] fundamentals of Cipher so as you can see
[589] to represent any property which is in
[593] the node we can directly give it in the
[596] parenthesis of nodes so as you can see
[598] we got the person node here in the
[601] parenthesis and we have the curly
[603] brackets in which we have the key value
[606] pair so the key will be like the name
[608] for person and like the property value
[612] which is like a Jennifer so it
[614] representing a person who has the
[617] property name as Jennifer but we also
[620] given a variable to our node which is p
[623] so to refer this person in the
[626] subsequent steps of your Cipher query
[628] you can directly give it as P so
[631] assigning variable is very important to
[634] use that node in the further steps like
[637] the wear condition to filter out your
[638] nodes that is very important
[640] and similarly to represent the property
[644] in your relationship as a relationship
[646] property so if you have like is friends
[649] with and in this relationship we have
[652] like a different property so since 2018
[655] so which means that some person is
[658] friends with since 2018 to another
[661] person that is very simple English
[664] language and everyone can like read that
[667] using this so as you can see we got the
[670] relationship is friends with in the
[672] square brackets and we have the
[674] directions as well so we can represent
[676] this using the arrows so as you can see
[679] we got the sense key and the 2018 value
[683] in the curly braces and we have the Rel
[686] Rel which represent this relationship
[689] and Rel is a assigned variable for our
[692] relationship so this is how you can
[695] represent relationship or the node
[697] properties in your Cipher query so so
[700] far we have learned what is node what
[703] are like relationships and how we can
[705] represent them in the cipher query as
[708] well as we have seen like how we can
[710] represent different nodes and
[712] relationship properties in your Cipher
[714] so the next lecture will be we need to
[717] discuss the cipher keywords which are
[720] like very important like the select
[722] Clause where Clause there are different
[724] Cipher keywords present in neo4j so to
[728] learn that you need to First understand
[730] the basic fundamentals of the cipher so
[733] in the next lecture we will talk about
[735] and jump on to writing the cipher
[737] queries from the beginner level to the
[739] advanced level and we will see all the
[742] syntax and like the different keywords
[744] as well as like the complex stuff like
[746] Loops as well as sub queries and all
[749] that stuff in the sub segment lecture so
[751] stay tuned And subscribe to the channel
[753] and if you have any difficulties you can
[756] let me know in the comments and we can
