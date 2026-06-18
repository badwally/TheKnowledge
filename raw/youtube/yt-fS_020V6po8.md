---
schema_version: 1
id: yt-fS_020V6po8
type: youtube
title: 'Lecture 07: Uplift - Mapping Relational Databases to RDF'
url: https://www.youtube.com/watch?v=fS_020V6po8
authors:
- Christophe Debruyne
ingested_at: '2026-06-18T01:38:18Z'
content_hash: sha256:ee4c7fdd9478cf886018383ec8e5a318bcb69e490ca47be8328484f5a85a4a7b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Christophe Debruyne
  channel_url: https://www.youtube.com/@chrdebru
  duration_seconds: 2870
  caption_track: cached
  snippet_count: 457
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:18Z'
  user_correction: null
---
[0] hello my name is christopher dubane and in this lecture we will cover how we can transform data contained in relational
[5] databases into rdf
[11] what we aim to do in this lecture is transform the data containing container relational databases into rdf
[17] in this example we have two relational tables person and city and we assume that people are
[24] related to their city via city id which is a foreign key pointing towards
[31] records in the table city what we want to achieve is the following we want to state that
[38] these two records represent people and they are identified in some way
[44] shape or form and those people have first names last names
[50] they're both of the type fourth person and hopefully you recall that folf is a vocabulary to describe people and
[57] both of them are based near a particular city one being dublin and one being ghent
[66] the relational database to rdf movement or rdb to rdf for short all started with tim berners-lee proposing a direct
[72] mapping language to transform relational databases to rdf this sparked a discussion and over the
[78] years two w3c recommendations were published that specified how one can map
[84] relational data to rdf the first one was a direct mapping of relational data to rdf
[90] and the second one r2rml is a highly customizable mapping language that allows us to
[96] prescribe how data contained in relational databases needs to be transformed into rdf
[104] rdb to rdf started with a blog post written by tim berners-lee where he
[109] discussed a set of mappings that can be generated automatically between relational databases and rdf
[114] and you can find the post over here in that post he has written the
[120] following the semantic web data model is very directly connected with the model of relational databases
[126] a relational database consists of tables which consists of rows or records and each record consists of a
[132] set of fields the record is nothing but the content of its fields just as an rdf node is
[137] nothing but the connections the property values and then he proceeded to state the mapping is very direct
[146] a record is an rdf node the field column name is an rdf property type and
[154] the record field table cell is a value now indeed it is not always that simple
[161] can you provide examples well it could be for instance that in a relational database
[169] you might have due to normalization and reference tables being removed you might have
[176] a subset of your relational data relational table schema
[182] actually representing a complex type and not merely a value of a record field
[189] we will see a couple of such examples in this lecture
[195] both w3c recommendations were published on the same date back in 2012
[200] we will first cover the direct mappings now it started with tim berners-lee's
[206] blog post where he proposed a direct mapping that immediately reflects the structure of
[211] the database his proposal was refined into a recommendation now in both instances
[219] the target rdf vocabulary directly reflects the names of the database schema elements and neither structure
[225] nor target vocabulary can be changed so it's not customizable
[230] he then declared the process existing table and column names are encoded into your eyes
[236] reflecting classes and properties then the data is extracted transformed
[242] into rdf and loaded into a triple triple store which basically boils down to an etl process
[248] extraction transformation and load this proposal as i said over time was
[254] refined into a wtc recommendation published in 2012 which you can find here
[254] Direct Mappings
[262] now in direct mappings the database both schema and data primary keys and foreign keys are given
[268] to a direct mapping engine to produce an rdf graph fields are mapped to literals primary
[275] keys are used to construct uris for the resources and foreign keys are used to construct properties and relate
[281] resources for example in this example i will transform this
[287] very simple relational database into rdf you can see that i have two
[292] tables people and addresses both have a very simple primary key called id
[299] and there's a foreign key relating the table people to the table addresses via the column
[305] addr in people to the column id in addresses
[312] before we can start the transformation process the algorithm as prescribed by the w3c
[318] recommendation needs a base uri in our example the base uri will be http
[325] colon slash foo dot example slash db slash
[334] the rdf that will be generated will look as follows
[340] we will have our base declaration and we will have a couple of namespace
[346] prefixes that will be useful for our example such as xsd for the data
[351] types rdf for rdf type and so forth and so forth
[356] let's start by transforming the contents of the table people
[362] what you can see here is that the name of the column was used to create a uri to represent
[369] the type so this type has the uri http colon
[374] slash foo dot example slash db people you can
[380] furthermore see that each column name was used to create
[386] a property the uri of the uris of these properties look as
[392] follows they have they their uri contains the name of the
[399] table hash the name of the column name and then the values are
[404] assigned to each instance we also know that the column adr
[413] is a has a foreign key to the table addresses
[419] for foreign keys the properties that correspond with those
[424] get a uri that looks as follows there's the name of the table
[432] hash ref for reference and then the list of column names that constitute
[438] that foreign key it will also point for each instance
[443] to the corresponding rdf resource now
[450] how do instances get their uris well for each record a
[456] resource is created and the uri looks as follows it is the name of the table slash and
[463] then for each column in the primary key it will contain the name of the column the equal sign
[471] the value of that column and if there is more than one column in the primary key they are separated by a ampersand
[482] you can see that null values do not result in rdf statements
[489] the second table is a lot more simple because it doesn't contain many columns and it does not contain any
[496] foreign keys but you can see that this one corresponds with this one
[501] and that's how we generate our rdf graph now the w3c recommendation direct
[508] mapping recommendation does prescribe how you need to deal with data types
[514] for instance we know that the these columns
[521] id addresses or addr and id here they're very likely
[528] of the data type integer the direct mapping w3c recommendation
[535] provides a mapping of sql data types to xsd data types so in this exam in this example which i
[542] have simplified for this lecture you would see that this one would be date typed
[548] as follows xsd integer
[548] Are Direct Mappings Meaningful
[558] at this point i usually start a small discussion with my students i ask them the question are direct
[565] mappings meaningful and can you identify potential problems
[570] direct mappings are meaningful to those who know the database
[575] in my example i know because i own or develop the database that addr
[582] stand stands for the address but that was still pretty
[589] straightforward however the foreign key did not state what the relationship was between
[596] people and addresses was it the address of residency was it the address of birth
[602] what not we do not know other problems that we could identify
[608] include the groupings it is very well possible
[614] that in our database we have a column that is
[620] reduced to a value that should be represented as a
[626] complex thing something that is a resource with their own uris and whatnot
[634] think of gender or maybe even the city in a address table cities are complex
[640] things that can have metadata as well assigned via rdf statements
[647] to address these issues another proposal was developed and published as a w3c
[653] recommendation over time and that is the r2rml mapping language
[653] R2RML
[659] r2rml which stands for rdb to rdf mapping language is also a wtc recommendation since fall
[667] 2012 have been published at the same time and they allow us to create an artworml file
[673] that annotates a relational database with existing vocabularies and or ontologies and they can be
[680] formalized using rdfs all and so forth the r2rml file containing those mappings
[687] goes to an r2rml mapping engine to produce the rdf
[693] the r2rmlw3c recommendation does not only specify an ontology to specify those mappings
[701] but also a algorithm that prescribes how those mappings should be interpreted to produce rdf
[709] and this is pretty neat because the ontology provided by r2rml
[716] is a semantic web ontology it is represented in rdf it's stored in an rdf
[722] and the r2 rml files are themselves stored as rdf and this allows us to treat them as rdf
[729] as well which means we can add statements with other vocabularies such as provo for provenance information
[737] metadata who created the mapping where the dm mapping come from and so
[742] forth and so forth which could uh render the whole process
[748] a little bit more transparent and reproducible but that's not the topic of this course we will now be covering
[755] the mapping language itself
[755] Table Addresses
[761] let's start by creating a an rml mapping for our simple example
[767] we will now start with the table addresses because it's a little bit more simple
[773] on the right hand side you can see that i have created an instance of a triples map
[779] the dribbles map will contain all the directives to transform the information in a result
[785] set into rdf a triple map consists of three things first
[793] we have the logical table which can either be a
[798] table name and the table name can contain names of tables or views or an sql query
[804] we will see an example later on that is mandatory other than otherwise the triples map does not know
[811] what to transform a tropics map must contain a subject map
[817] the subject map prescribes or tells the r2rml engine how to generate and state something about the subjects of those
[824] trebles in this example we will generate for each row in the table addresses
[830] a resource with the following uri http column foo dot example slash addresses
[837] slash and then we use values from the columns in the result set
[843] we also know that each insta each record corresponds with a place we
[849] avail of the dbp deontology to state that each subject generated as such
[855] is of the class dbp year place resulting in a triple resource with that uri
[863] rdf type dbp data place you can have more you can have zero or more class
[868] statements now finally a triples map can contain
[875] zero or more predicate object maps predicate object maps as the name implies will generate for each row
[884] predicate and object combinations we will see what will happen if we
[890] provide more predicate and predicate map directives and object and object mapped directives in a
[896] project predicate object map in this particular example we will generate rdf statements
[902] using the predicate fourth name that will be related to each subject and
[908] its values will be taken from the columns and in this particular case we will take
[914] the values for the object from the column city and we will treat them as strings
[920] in this case it is implied
[926] as i said the logical table of a trebles map can contain either a table name or an
[931] sql query here you can see an example that is equivalent where i used a query
[938] to retrieve all values of id and city from the table addresses
[945] now on to the next example in the next example we will create a
[951] triple map for people but we've seen that there's a foreign key so we can relate
[956] people to addresses which we'll cover here again pretty straightforward we have a
[961] new dribbles map and make sure that you provided a different name a different name node
[967] in the rml file it has a logical table people has a different subject map now i
[975] am creating instances of person and i want to them to be disjoint from addresses so i have to
[980] make sure that their uris are different they're of the class fourth person
[986] and i create a predicate object map much like in the previous example for fourth name but here i retrieve
[992] values from the column fname here now how do i relate to
[999] well i will create a special predicate object map in this predicate object map i use the
[1005] predicate fov based near and for the objects i will inform the
[1011] art or ml engine that he has to retrieve the values from another triple map
[1016] so the parent triple map is the addresses triple map that we created in the previous slide
[1022] now the engine is smart enough to do a natural join if no joint condition is provided
[1030] but in this case a natural join wouldn't work so we provide joint conditions and we tell the r2 rml
[1036] engine you have to combine the two logical tables as follows you have to match the ids
[1045] sorry the addr field from our triple map with the id field of the parent triple
[1051] map and he will then generate a join and sql
[1056] join in order to create rdf statements for this particular predicate object map
[1065] now in this very simple example we haven't covered what would happen if some values are
[1071] null if values are null and used in the mapping then it will not
[1076] generate any statement we also didn't cover how to deal with
[1081] rdf graphs yet but given these two triple
[1086] triples maps the values given these two triples maps
[1086] R2RML Engine
[1094] um which are stored in one file we now need to avail off an
[1101] r2rml processor and an engine you can find in other videos that i
[1107] avail of one that i've developed you basically provide all the things
[1113] that are necessary a connection url username password and so forth and so forth the two triples maps are stored in
[1121] a mapping file and we tell the engine that it needs to generate turtle
[1126] and the output file is called as follows you can find the video on my channel
[1134] the result is as follows you can see that i have two instances of people person one and
[1141] person two and the first person is related with an address
[1147] via the predicate vote based near and it's as simple as that
[1147] R2RML Concepts
[1155] if you were to consult the r2rml w3c recommendation you will see that the key concepts of
[1163] r2rml are related as follows we have covered most of them we know that a triple map must contain a
[1170] logical table it must contain a subject map and it must contain
[1175] zero or more predicate object maps and each object map has a predicate map and an object map to
[1182] help generate the rdf statements there's a very special
[1188] object map that is the reference object maps that requires joint conditions
[1194] r2rml provides also a way to organize your rdf statements into
[1201] named graphs so a subject map and a predicate object map all can have zero or more graph map
[1209] statements we will see later on what will happen if we use those
[1209] Term Maps
[1217] here's another diagram from the w3c recommendation relating
[1222] various concepts of the r2rml mapping language there's this notion of a term map which
[1228] is the let's say superclass of the various maps
[1234] the various term maps that we've already encountered we have encountered subject map object map predicate map we have not yet
[1241] encountered graph maps in an example but we will see one later on now term maps
[1248] can have uh can generate values based on either a constant a column or a
[1254] template and i'm i'm not entirely happy with how it is represented because
[1261] the constant value if it's used in a subject map graph map or predicate map
[1266] then it must be an iri it must be a resource but if it's used in a object map then
[1274] its value must be either a literal or an iri and this gives the impression that it has to be an iri
[1279] so the the the representation is a bit unfortunate in the w3c recommendation
[1288] now not understanding what you use you can also assign term types to a term map and you
[1296] can state that it generates resources named resources with rri
[1301] or you can state that it generates blank nodes with our blank node and you can say that it generates
[1306] literals with rr literal and you can furthermore provide language
[1312] tags and data types if you're generating literals
[1318] finally there is rr inverse expression they are useful only when accessing relational databases as virtual graphs
[1326] they provide some sort of optimization hint and i will provide an example of that later on
[1333] now are our class statements in subject maps we've seen in the example that a subject
[1340] map can have zero or more rr class statements whenever the
[1346] result set contains no null values for anything used in either the template
[1351] column name and so forth to generate the identifier either the uri or the internal
[1358] identifier for a blank node whenever that's possible it will generate rdf type statements
[1364] for each class appearing in the subject map so for address one for instance i would
[1369] then have http colon foo dot example slash addresses slash 1
[1375] rdf type dbpedia place while there are nuances when combined
[1383] with graph maps this is this can be considered syntactic sugar
[1388] for the following so the subject map generates for each subject a triple with rdf
[1394] type as a predicate and db pedia plays as an object so in other words in this particular
[1401] case rdf type and dbpedia please are constants so can we generate or can we create a
[1408] predicate object map with two constants and the answer is yes we just create a predicate object map
[1414] where we assign the constant value rdf type to predicate and we assign the constant value dbp a
[1421] place to object so you can consider this to be
[1430] syntactic sugar but as i said once named graphs come into play
[1438] it's a little bit more nuanced
[1443] here we have another example of synthetic sugar whenever you use constants you can
[1452] ditch the predicate map and object map properties so in this example you see
[1459] that we related rdf type to our predicate and dbpedia place to our object
[1466] and this is basically equivalent with rr predicate
[1474] map with a value rr constant
[1483] rdf type
[1488] and for the object pretty similarly we would have an our object map
[1496] that has the rr constant
[1502] dbpedia sorry db d
[1509] pedia place
[1515] this needs to be connected um so these two are equivalent
[1515] Predicate Object Maps
[1524] now what happens in practice something that i have encountered in project r that other people have done
[1532] to optimize the process now the algorithm as prescribed by the
[1538] r2rml recommendation states that for each triples map it will generate a query for the logical
[1546] table and will be applied to all the graph maps subject maps and predicate object maps that do not refer to another
[1553] table so the result set of this query will then be used to generate rdf for
[1562] this subject map and this predicate object map for the predicate object map maps that
[1569] refer to a parent triples map a new query will be generated based on the join of the two logical
[1576] tables so in order to generate rdf for this predicate object map it will take
[1583] this table name and the table name of addresses and do a join based on these join conditions whenever
[1590] you have very large databases this could slow down the process
[1597] however if you know what you're doing and all the information to generate
[1604] these links is contained in your child triples map
[1610] then you can between quotes bypass this process by creating a
[1616] regular regular predicate object map as follows
[1624] you copy paste the template or that column value or the
[1631] template whatever of the subject map of your parent triples map and you place it in the object map
[1637] as follows and you obviously need to use the column names from your child triples map
[1646] now this will work only when you have
[1653] a correspondence for example if you were to have a value in the people's
[1661] table that does not appear in addresses well then you will generate a resource
[1668] but there will be no information provided to that resource via the addresses triples map
[1676] that is obviously not going to happen if you have a foreign key but if you have databases where you
[1681] don't have foreign keys but some things can be joined however there are missing values well you might end up with an rdf graph
[1687] that is not equivalent to the graph that is generated when
[1693] if you would have used the param triples map
[1693] Graph Maps
[1699] now graph maps graph maps may seem a bit daunting but they're
[1706] pretty simple once exemplified so graph maps can be assigned to subject
[1714] maps and predicate object maps and they both can have one or more graph maps
[1720] they are specified in two ways either by assigning a constant with the property r
[1725] graph or by providing a graph map and that returns
[1730] rise so name resources there is a if you do that then you have
[1738] to use the r graph map property rather than our graph similar to the example we've seen before for our
[1745] predicate and our predicate map and our object and our object map there's a special named
[1752] resource called our default graph for the default nameless graph now if a subject map has no graph maps
[1760] then the set of graph maps is our default graph if both the subject map and predicate
[1767] object map have no graph maps then the set of graph maps is our default graph
[1773] otherwise it is for each predicate object map the union of both graph sets
[1780] sounds complicated but it's not let's explore exemplify
[1780] Union
[1785] in this example we see a subject map a practical object map and a predicate
[1791] object map that uses a parent triples map it's the example from the previous slide and i
[1797] have divided them into three now what happens if i execute this
[1804] mapping well all generated by the subject map will
[1810] be entered into the default graph and the same for the first predicate object map and
[1816] the second object map predicate object map
[1821] now what would happen if i assigned a rr graph statement to the subject map
[1828] and it refers to the r default graph well that doesn't change anything triples generated by the
[1834] subject map will will be stored into the default graph the triples generated by the predicate
[1841] object map the first one will be stored in the default graph and that of the second predicate object
[1846] map as well now what will happen if i assign a uri
[1854] to the rr graph statement of the subject map and in this case i give it the our uri
[1862] fragment one so for simplicity this is the first name graph well obviously we will have a named
[1869] graph of that uri and all the rdf statements generated by
[1875] the subject map will be stored in that named graph finally however
[1883] the triples generated by the predicate object maps will also be stored
[1888] in that named graph why well if no graph statements were provided
[1894] for the subject map and the predicate object map the default graph is the default the default graph is a default graph
[1902] that's funny that it rhymes however the w3c recommendation states
[1909] if either has a value provided then it's the union
[1914] so the subject map has an rr graph statement therefore it is not the union of our
[1921] graph number of the the first name graph and the default graph
[1926] there's only one so all the triples generated by the predicate object maps that have
[1932] no rr graph statements will be generated into the rr graph statements of the
[1938] subject map let's make it a little bit more
[1944] challenging and assign the subject map and the predicate object maps each different graphs and hopefully that
[1950] will make the rule a little bit more clear so in the subject map we still have our
[1958] one named graph so the triples generated by that subject map will be stored in
[1964] that named graph the first predicate object map has an rr
[1969] graph statement pointing to a another named graph number two so there will be a second
[1976] named graph and the triples generated by the predicate object map will not only be
[1982] stored in number 2 but also a number 1. remember the rule states
[1987] the union of the graphs of the subject map and that of the predicate object map
[1996] the same holds for the second named a second predicate object map
[2001] where triples will be stored not only in the third name graph but also in the
[2007] one provided by the subject map
[2013] in the final example i want to exemplify two things first a predicate object map or a
[2019] subject map can have zero or more rr graph statements and here you can see
[2025] two secondly i wanted to demonstrate what would happen if you assign another or the default
[2032] graph to either the subject map or the predicate object map well in this particular case for the
[2039] subject map nothing changes all the triples generated by the subject map still go to the first name graph
[2046] for the first predicate object map nothing changes either the triples will be stored in the second
[2052] name graph and the first name graph the second predicate object map
[2058] refers to both the both the name graph number three and the default graph so they will be
[2063] stored in two different graphs and they will also be stored in the
[2069] named graph referenced by the subject map
[2069] Quirks
[2075] now we will cover some quirks is not the right word but um
[2082] special things about the r2rml language that people might struggle with but they're all
[2088] described in very much detail in the w3c recommendation there's a couple of implied rules
[2095] so we know that r2rml supports mapping values with constants column values or column
[2101] values applied to a template now if an object map does not refer to a column
[2107] or has no language tag or has no data type tag then the values default to named nodes
[2114] unless you explicitly specify it to be a literal so in this particular example
[2122] had we not provided this directive the r2rml engine assumes
[2129] that for this particular predicate map using the predicate fourth name you will
[2136] generate a named resource using the combination of these two column values and we know
[2142] that this is not a valid uri so it will break this will provide an error but if you use a template directive
[2150] for an object map and you want to use a template directive to generate literals
[2155] then you have to tell the engine that you have to state i am generating things of the term type
[2161] literal now when you
[2161] Language Tags
[2168] create term maps with the term type literal and that can only be the case in the
[2174] object map you can assign them a language tag
[2180] so in this particular example we state that this predicate map generates rdf statements using the
[2186] predicate label rdfs label the values will be fetched from the column title
[2192] and they will receive the language tag en so this will generate triples with the
[2199] following object title so let's assume the title
[2206] is full and it will then generate a language tag en now
[2214] asking the question why is the above term type implied to be a literal well it is implied to be a literal
[2220] because we avail of the rr column directive if we use column the art or ml
[2228] engine will assume that we're fetching values
[2233] it uses a column it is not uncommon to find in relational databases
[2233] Multiple Languages
[2240] tables containing values with its translations so you might have a particular id a language
[2248] for instance dutch and you would have brussel and then you would have another record for the same thing sorry
[2255] and you would find that the translation in french would be put cell and so forth and so forth unfortunately
[2261] r2rml has in my opinion poor support to
[2266] basically state well use this as language that attack for that in a dynamic manner what can
[2273] you do well if you have a table of multiple languages and you have some sort of discriminator
[2279] as you can see here then you can create a logical table
[2286] for each of uh the languages that you have so you would then state okay select all
[2292] the values for which i the language corresponds with nl and then
[2298] another one another triples map for the french values and so forth and so forth
[2304] another approach would have been to create one logical table and use the language column to create a single
[2309] mapping for all languages however that is not part of the recommendation
[2315] and support for it depends on the implementation so there is a extension um if i'm not
[2321] mistaken proposed by and her phd student that
[2329] created an extension that allows for that so you can state the language column is provided here now unless you use one
[2337] of these extensions you cannot avail of set functionality but another problem with an extension is
[2344] that you then create mappings that are beyond the standard scope so they become
[2349] less interoperable now for data types data types can only
[2349] Data Types
[2356] be declared for term maps that are of the type or are literal and are without a
[2361] language tag so you either use a language tag or a data type but you cannot use both obviously those term maps are
[2369] only object maps so in this particular example we have an object map that
[2374] refers to the column amp no employee number and we assign it to b
[2380] of the data type x is the positive integer you are not only limited to
[2386] data types of the xsd namespace you can reveal of other uris for instance
[2395] uh from geosparkle geo wkt literal that's one example that uh on
[2402] top of my head that i'm aware of now again to reiterate why is r2rml
[2410] so powerful and flexible well it allows you to avail off projections and selections
[2418] in your queries to generate rdf what do i mean by that well
[2424] let's assume you have a table and you have multiple columns you have
[2431] multiple rows and it can be that you have a
[2436] couple of columns inside your table that represent a concept i will use a
[2443] different color so that grouping may represent
[2449] an instance of a class that is related to the instance of another class
[2456] captured by the rest of the records in that table a good example would be a city a city is
[2463] often a column in a table addresses yet cities are instances on their own so you can create a triple
[2470] map for what we call a projection or table similarly you can map selections if you
[2477] need to create a a separate triples map for cats in your pet table you can do so
[2484] and then you only select a couple of or a subset of the records and then you can create a triples map
[2491] for fish if they have different properties to cats and so
[2496] forth and so forth at the beginning i stated that i was
[2502] going to say something about rr inverse expression our inverse expression was used for
[2509] uh when one is dealing with virtual graphs in other words you're retrieving rdf by
[2515] translating the sparkle queries into sql queries via mediator so the rml mapping is used
[2523] to generate sql queries on the fly now r2rml transforms database terms into
[2530] rdf terms the inverse expression helps one to transform rdf terms back into database
[2536] terms which may increase performance i personally i am not aware
[2541] of any implementation that supports or implements this as it is not necessary for our rml views
[2548] to be generated and work is a optimization technique so let's
[2548] Inverse Expression Example
[2555] exemplify the use of rr inverse expression first i assume i have a database and a
[2561] table where all surnames are stored in capital letters for this example to work
[2567] now obviously uh well not obviously in my example i want to generate uris
[2574] for people but i'm not going to use the capital letters so i have a triples map
[2579] where i create rdf statements about things based on the
[2586] following sql query i avail the email address and i transform the values of surname into
[2594] lower caps and i assign it to the variable elser now the subjects have the following
[2602] uri structure http examples of slash persons flash and then the lower cap
[2607] value of their surname and i assign their email addresses via the both and
[2613] box predicate now what will happen if i fire the following query and i ask
[2620] give me the email address of that particular person well the sql
[2625] query for retrieving the value of an email address should correspond with select email from employee where
[2634] the lower cap representation of the surname equals the briana and this may be very slow now
[2642] that isn't the case when we use this mapping to access the
[2649] uh the database as a virtual graph so on the fly
[2656] this sparkle query is transformed into that sql query this particular one can
[2662] be very slow so how can we optimize that well with the rr inverse directive we
[2669] can state that the surname needs to equal this following transformation
[2675] function so whenever we fire this query this will generate the following query
[2682] select sql query pardon me select email from employee where
[2687] surname equals upper dubrada and if surname were to be indexed this
[2694] query would be much much faster so that is the use of our inverse
[2700] expression it optimizes it potentially optimizes the retrieval of information when accessing
[2709] the contents of a relational database as a virtual rdf graph
[2709] Use Cases
[2714] so how can you use these rml mapping files well you can use them to translate the
[2719] data into rdf which are then subsequently stored into triple stores for
[2725] consumption the downside side of that is that it will be harder to maintain
[2731] updates so if your data base evolves over time you have to make sure that those changes
[2738] are propagated to your triple store triple stores there are many you can fail off jenna tdb
[2744] for two ozil blaze graph and what not as we've seen with the inverse
[2752] expression you can also use those mappings to access the rdf sorry the database as a
[2760] virtual rdf graph and whenever you formulate sparkle queries over the rdf
[2766] well they're changed into intermediate sql queries so the advantage is that you have
[2774] at any time the most up-to-date data but the execution of the queries might take
[2780] a little bit longer if you were to follow the course on open information systems
[2786] at the very investigated vessel then the teaching assistant will demonstrate how you can use on top to mediate between ontologies and
[2795] the database via those rml mappings
[2795] Conclusion
[2800] so this brings us to the end of the lecture to conclude we've covered the two w3c recommendations for
[2808] transforming relational databases into rdf one being the direct mapping that reflects the
[2814] structure of the database and the other more flexible and extensible approach
[2819] being the rml mapping language what we haven't covered in or what i
[2825] haven't covered in this video lecture are some of the more recent initiatives proposing extensions to the mapping
[2831] languages in order for instance in to cope with functions
[2836] and other types of data but you can find those in the pdf version of the slide deck
[2844] i welcome you or i encourage you to consult my youtube channel where you can find a video of an r2rml
[2851] tutorial step by step rtml or r2rml tutorial with sample data so that you can get
[2858] better grasp on the material that we've covered today here are a couple of references that
[2865] i've used to write this video uh video lecture and i
[2870] wish you the best of luck in creating rdf from databases
