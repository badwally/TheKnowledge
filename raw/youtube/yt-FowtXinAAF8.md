---
schema_version: 1
id: yt-FowtXinAAF8
type: youtube
title: 'Shapes applications and tools Part 1: Introduction to RDF data model and motivation'
url: https://www.youtube.com/watch?v=FowtXinAAF8
authors:
- Jose Emilio Labra Gayo
ingested_at: '2026-06-18T01:38:17Z'
content_hash: sha256:9e05166aabef2faf9b51fef614e544ea39226c098d6f0e8e2360da180ec5fb2a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Jose Emilio Labra Gayo
  channel_url: https://www.youtube.com/@jelabra
  duration_seconds: 2540
  caption_track: cached
  snippet_count: 401
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:17Z'
  user_correction: null
---
[7] this part of this material was already prepared for previous tutorials so i also
[13] collaborated with eric dimitris and iof capone
[19] so just a very short introduction in my case i i wrote initially a book in spanish
[26] was semantical but i also with this other guys another book
[33] called validating rdf data in 2017 and in the book is you can buy the book
[40] but the book is also available online so you have this html version that you can
[46] go to this this link there and and if you go here oops
[54] you can see the way the book and i'm going to activate this one so this
[60] is the link to the to the book to the web page of the book you can read the contents and
[67] there is also a link there to to the to the samples
[72] in the book that you can take the samples and download the book and the the samples and play with with uh sex or
[80] circle i also have this webpage in case that you are interested in more details and more publications
[87] i have in the recent years we we did several publications related with
[93] this topic about sex and soccer and that's what i'm going to do
[93] Contents
[98] to talk to today so the the contents the topics that i was planning to
[104] to to do in this session i i will start with a very short
[109] introduction to the rdf data model then some motivation about why we want
[114] to validate rdf data and my plan was to to do these two sessions about sex
[121] by example and circle by example to have an overview of saxon circle
[128] probably i will probably just keep some of the slides here i kept the slides in the
[136] in in the tutorial more as a reference but not to follow all of all the slides
[142] because otherwise the tutorial will be very uh i would have to go very fast uh with the slides so i will
[150] keep the slides here as a reference but my plan is not to vote into all the details here
[156] and also i will i have another set where i can do a short comparison
[161] between sex and circle with some examples uh probably i will my plan here is to to do if this in more
[169] detail and i also had it for this tutorial another okay so as i was saying that
[169] RDF overview
[176] i also have this about comparison between section cycle
[181] and and the most new material in this tutorial is about a topic about
[188] shapes applications and tools and some challenges and perspectives about validation and sex and circle and
[196] this topic maybe is the most interesting topic for people who are interested in
[201] research for in this semantic web conference maybe there are people who are interested in some new challenges and and all that so
[210] probably this is going to be the most interesting and my plan is to have the last hour uh the last hour of this tutorial
[218] for this topic for safe applications and tools because i think the other parts you can read the
[223] book and you can get what's all of the contents there okay so just as i said the short
[231] overview of the rdf data model i have to go to another set of
[238] slides that the the overview this is a chapter two i mean this is a very short
[244] history of rdf um probably all of you if you are in the semantic web conference do you know
[250] about this the rdf you will have triples we have subjects predicates objects and
[256] you can have different syntaxes of rdf and if you have a triple then that's a
[262] basic statement you can add other triples for example you have alice is enrolled in this course it has
[269] this name and this age and then you can add more statements
[274] and then later more statements you can have cycles here so this forms a
[280] graph and then you can have this graph in one part and then you can have another graph
[286] in another part and the the nice thing about the rdf is that as the the predicates
[294] and the subjects and objects it can be uris and uris are global you can merge
[301] very easily if you have two rdf runs you can merge those graphs so that's i think probably one of the most
[308] important properties of rdf is that it helps information integration when you have
[314] different information on different rdf data from different sources and you can
[319] easily integrate them so there as i said you have this basic rdf syntax where you have a list of
[326] triples but then you also have another syntax which is more
[331] i mean it was more designed for for people for human readers which is turtle
[338] this is more much more readable and this is the syntax that i prefer and i wanted to put this slide here in
[345] this tutorial because if you are able to read turtle syntax
[352] then you will find very easy to understand the for example the the shape expressions syntax because at
[359] the end shape expressions the syntax is inspired by tartar it's a combination between
[366] turtle sparkle and other syntaxes but but at the end it is very familiar and it is just a
[374] continuation of this syntax so you know that if you have several simplifications you can
[380] simplify different things and then you also can define data types for literals you have
[387] this also these rules to simplify for example you have if you don't put
[394] you just put a number then this is the same as uh as an interval uh also you have
[400] some predefined some built-in data types which usually come from xml schema so
[408] and this is for literals and then another topic is the blank notes you have this is the possibility to to
[415] say something about a note that you know that it is sixth but you
[422] don't know anything else so for example if you want to say that bob knows someone whose age is 23
[428] you can say bob knows this one which is a blank note so this is not a uri and this blank node
[436] has an hs of 23 so this is a way to to define this and this is usually
[441] mathematically this is an existential quantification so there is some x that
[447] says that bob knows x and x has h23 okay then the last thing that we have in
[455] rdf is language tagged strings so you can say for example that span
[462] has two labels uh one is spain in in english and the other one is
[468] espana in espanol in spanish and and you have this qualifier this tag
[474] which represents the language of this literal so this is another thing that is built in
[481] rdf and the question is is that all and the answer is yes the
[487] rdf is really very very simple and simple is better and i think that's probably one of the strengths
[493] of rdif is that this is a very simple data model which where you have
[498] the subjects in the predicate you always have uris in the subjects you can have uris
[505] or blank nodes and in the objects the values of the triples you can have either subjects blank nodes
[513] or literals and as i said this is all there is a whole ecosystem around rdf
[513] RDF ecosystem
[521] so i mean that was not all but because otherwise probably we don't have the semantic web
[527] conferences that was all because we also have a very nice query language which is sparkle we also have inference the
[534] possibility to infer new language new triples using for example rdf schema
[540] or owl or their other inference systems we also have the possibility to have
[546] shared vocabularies and if we put rdf behind
[552] with the web and we will have what we call linked data and knowledge graphs which are another
[559] variant of all these so there is a whole ecosystem around rdf but the idea is that the basis of rdf
[566] is are very simple okay
[572] so we were here in the rdf data model and just to to an overview we have a lot
[579] of good scenes in rdf so rdf is very nice as an integration language is
[585] probably the lingua franca for semantic web um probably so this is i mean semantic web is not
[590] just rdf and rdf is not only for semantic work but they are very close and very uh they are very
[597] good friends so so the rdf is important if you are in
[602] this conference and also we have rdf is very flexible you can
[609] adapt rdf to multiple environments multiple domains you can represent
[615] most of the information you can represent that using rdf in fact i i had never
[622] any problem to represent any information in rdf so it's very very easy to adapt data models to
[629] any domain and it's reusable because this open is reusable data when it is represented in
[636] rdf so it's very good for knowledge representation and we have also very good
[644] technology for example for querying rdf like sparkle or rdf data stores so those were the good parts but there
[644] Problems with RDF
[651] are other parts in rdf that i think are a little bit more difficult and i think that's the
[657] the problem that we try to solve with shape expressions or with soccer is that when people want to to
[665] to produce rdf or they want to to consume rdf so when you're trying to use rdf
[673] in practice there are there are several problems uh one of the problems is that
[680] is what i call here that we have a lot of serializations and usually developers don't know even where
[686] to start so so they don't know if they're going to use the tarte error which libraries they have to support a tartar or this was the
[694] old way uh the old school rdf was with xml but it's very difficult to to parse rdf
[702] if it is in rdf xml nowadays it is more trendy to use json ld
[707] so you have to choose between them or you have you can allow all of them you just use a rdf library that supports
[713] offloading but i mean it's a bit a bit tricky to work on that also to just put rdf
[721] inside html it's not so easy we have rdfa we have microdata
[726] so this is also a another tricky point but what's the the point that we are
[732] going to talk today in this tutorial is how to describe rdf or when you have
[738] rdf content and you wanted to describe it how which technology you have to
[743] describe this is for me one of the main important things that attracted me to to this validating
[752] problem and also if you are able to describe the data then you can check if that data is what
[759] you were describing if you say that you have data about a person and that person has a
[764] name and an average place then you should be able to do yes
[771] validate if that's the case if that's the case and that's what we call a validation
[777] okay sorry
[785] okay so why describing and validating rdf
[790] as i said here is for there are two parts of this same coin so we have
[798] if you if we have rdf imagine this is this represents uh rdf for example you
[804] can have rdf data stored and there are people who are going to produce data here so
[810] there are people who are going to add data to the rdf data store and there are people who are going to
[815] consume these data stored so there are people who are interested to know what are here in the data store
[822] the idea is that we are going to use shapes to describe here what is here what are what is what are the contents of this data store
[828] and the idea is that if we use uh shapes then developers can i mean if you
[835] want to produce that you can understand what are the contents that you are going
[840] to produce um sometimes you can't say well but i know what we i want to produce so that's not
[846] a problem but the problem is if you are working a big problem in a big domain and you are not
[853] only you a single person but maybe you are a team and if you are a team and maybe you imagine that you are the
[860] the the architect of the team and you have a
[865] set of developers and those developers they you wanted to tell those developers
[871] what is the content the structure of the content that you want to produce
[877] and for that you need a tool that allows you to describe these contents and that's one of the
[884] things that we are going to use with shapes so we want to to ensure that the developers they are producing the
[891] rdf that we were expecting to produce as something which is very interesting also you may may want to advertise you
[899] may want to say hey this is the the that's the i i am going to push this rdf data store and the contents of
[906] this rdf data store are this and i have a representation here
[912] of people and companies or whatever so you wanted to say what is the structure of the content of of this data store and
[919] for that we are going to use shapes and also there is another topic that i'm going to
[924] talk last session is about generating interfaces um so this is for producers and for
[931] consumers for consumers you just want to understand what are behind this data store for
[936] example i think now for somebody in wikidata we have wiki data
[941] this is a very big very very big data store where we put there are a lot of contents and
[948] we just want to understand what are the contents that are in wikidata we wanted to to know if we are talking about a city
[956] and we wanted to know what is the structure or what are the properties that have cities if we are talking about
[964] people the same we want to know what are the properties here so we want to verify the structure for example even before
[971] processing it and also in an automatic way for somebody you have a web service that is going to consume data for example from wikidata
[978] and you know that you are going to have a list of cities you want to know what is the structure
[984] that you expect from those cities for example maybe the cities have a property called country
[989] that refers to which country they belong to or other properties so you want to know which what is this data structure
[996] and finally if you know data structure then you can generate queries in a better way and you can even optimize how you are going to process
[1003] that data so those are the the main motivations i think for for validating and describing rdf
[1010] and i see this they are quite interesting so the in other technologies for example
[1010] RDF in other technologies
[1017] this is i mean what we were working in ship expressions and shackle
[1022] is not new if you look at what we have in other technologies and for example in relational database
[1029] you have the data definition language in xml they did a lot of
[1037] how to say a lot of recommendations a lot of proposals for for validation you have dtds
[1045] xml schema relax ng schematron so that there were several proposals in json they are also
[1052] developing json schema but for rdf there was nothing there to fill that up
[1059] you had ontologies you have rdf schema but that was not to to describe or to validate it was
[1065] more to to to have some kind of inference so and that's a different topic okay so
[1073] just to continue to understand data problem so the idea so this is just
[1080] trying to have some kind of inspiration of what if you we want to describe imagine that
[1085] you have this uh this is the some a very simple note you have this rdf note and you want to describe
[1093] this if you want to describe this you would say okay i have a node this node is
[1098] alice this is an iri and i have these two properties and and i have the value of one of the
[1105] properties is always if this is the name i could say okay the value must be a
[1112] string and i i can also say okay but the the value of nose is not a string the value of nose must
[1119] be another note okay so alice knows another node so and both could
[1124] know another node etc so so this is what you want to describe
[1130] so an abstract representation of that could be something like this so you could say okay i have a shape where i
[1136] have a node it's an iri and i have a property name which is a string
[1141] and imagine that you can say a constraint is that i will only allow one value for this
[1149] for this property so imagine that in your domain you want to say okay but people cannot
[1154] have two names so you put this constraint so you have only one name
[1159] and then the nose is the other property it should be also in this case iri but i
[1166] could allow zero one or plus because maybe bob doesn't know anyone but at least knows
[1172] both and knows carol so can't know two or three people
[1177] so these are the constraints how do you put that so this is the abstract uh
[1183] meaning of the strat save how do you put that in a shape expressions that's and this is the real so this is
[1190] the concrete concrete syntax of sex is that you have the shape of a user
[1195] should be a node which is a iri and have this property which is name
[1201] which is a string and knows another iri and this star means that
[1206] zero or one or more okay i think let's continue with with this example about this motivation
[1213] of why we want uh to to validate or how we are going to represent uh
[1221] shapes in this case it was used in shape expressions but as we would later we will show later
[1227] shuttle is very similar to this okay so another topic was trying to understand the problem
[1234] that we want that we have when we want to validate it's about the flexibility of rdf
[1240] rdf is very flexible it doesn't put constraints for example
[1245] in the values of properties for example you could have in this case is imagine you have a node
[1251] angie and the creator of this is the song angie the creator could be kiss creatures and also make the other
[1257] but imagine that you have this model where you allow either a string or a note in this case this is a blank
[1265] note that has a first name and a last name so this you could have
[1271] a combination of a simple literal so the proper this value could be a
[1277] single literal but it could also be a more complex structure and there is no problem in rdf
[1284] you could define that and the language to validate this could should allow this kind of combinations okay
[1284] Repeated properties
[1292] finally finally for this motivating part is that you also have this thing about
[1298] repeated properties sometimes you could have data models in rdf where
[1305] you have the same property for example here we have product id and product id this is the
[1312] the same property but the data model that of the nodes that you are respecting of the values
[1318] of this property could be different for example remain that you want to say okay but
[1323] i have one properties product id and has a major this is a book and has a isbn so
[1329] you have the this is a literal that has the isbn but then you have another product id a
[1336] value which must be a string in this case this is an internal code
[1342] and has this this structure so when you want to validate sometimes you you must say that you have
[1350] two properties product id with two different uh shapes
[1357] okay so that's the idea so and i put here uh some practical examples from someone for fire
[1363] you have observations and the blood pressure you have different for the same property you have different
[1369] uh observations of blood pressure another thing for me is is interesting
[1375] is that we should separate shapes from types types come from the on top what you want
[1382] and when you say that you have a note that has the type of a person
[1388] in the ontology world that's that's okay but usually you could have in your domain you could
[1395] have several nodes in your domain that has that same type for example you have
[1402] imagined that you have a in a health information system you have nodes
[1407] that are customers you have also notes that are passions etc and
[1414] all of those nodes have the same type they have the type of a person because they are all all of them are people but the
[1422] data model that they have the shape of the nodes of is different because you could have a
[1428] different shape for customers and a different shape for passions etc okay so that's the idea that uh
[1434] that's something that i think it's also important to separate the the type from the shape that
[1442] has the notes of without that okay and finally embroider this is i think this is
[1448] something that probably is not easy uh for people who
[1453] were a lot of time working with ontologies and and the semantic web conference i think they
[1460] at the beginning some people thought that why do you want a new language to validate uh if we
[1468] already have ontologies and i think that's that has um
[1474] that grief that gave some kind of tension between the semantic web traditional
[1480] community and the more recent people who really want to use rdf
[1486] for practical purposes and the idea is that for as far as i can explain this is that
[1493] ontologies for me they are at a much higher level and usually when you are thinking
[1499] and when you are defining an ontology you are thinking about your domain and you have the
[1505] and especially in the semantic web conference sorry in the semantic way you must
[1511] think in a very open way for example you can especially if you link that to
[1518] inference imagine that you want to represent a people a person you could say okay in an
[1524] ontology i can say that every person has two parents
[1532] and exactly two parents which are people and that's okay for an ontology
[1539] but imagine that you have a for example data and you want to validate data and you have alice in this case you
[1546] declare that it has two parents and both that has the in this rdf data has only declared that
[1554] has one parent which is dave if you put this ontology as a constraint
[1563] the system would complain here because bob only has a one parent
[1568] so that's that would complain but if you know about open world assumption
[1575] in in all he here all wouldn't complain what he would do
[1581] here is to say that to to infer the bob has one parent which is dave
[1588] and also has another parent which is a blank no whatever is another note that you
[1594] don't know anything about that but the system would infer that bob has two parents and one of them doesn't know
[1600] who it is okay so that's the idea of all you can infer things and that's okay i mean this
[1605] domain you can infer things that you you can infer that bob has two two parents one of them is dave the
[1612] other one you don't know anything and later if you have more information about bob maybe you you infer that there is
[1619] another parent who is 43 years old then you could infer that this note has an age of 43
[1625] so and that's very good for all so because you are talking about the domain but for shapes what we want to do is to
[1633] describe this data we want to describe this data and we want to validate if this data we want to put
[1638] to put that in a data store and for example if you try to put that in a practical way
[1644] trying to enforce that every node has two parents exactly two parents would
[1650] be impossible here because that constraint would generate an infinite value i mean you know not so well you
[1656] could have cycles but you could have every node must have a two parents and then this other node
[1664] must have another two parents and unfold and so on so so trying to um to put that as a
[1670] constraint in the data uh wouldn't work so you need to say okay but in this data i must
[1677] allow that one node has two parents another note must have one another maybe it doesn't have any
[1684] regression of parents and that's the constraints for example here in in sex you could say okay i have
[1689] the shape of a person he's an iri in this case and has parent and i can say okay but i have can have
[1695] zero one or two parts so this is the cardinality and and this is a way to put here this
[1700] constraint so for example if you have another node that that declares that it
[1706] has three parents in safe expressions or soccer which in a separate
[1711] way would complain but a circle for example if you declare that there are three parents
[1717] uh what all would do is to infer that two of those two parents of those three
[1723] parents are the same one okay you know so that's the the main thing and that's why ontologies
[1729] i mean from my point of view entries are very good to do to this to when you are talking
[1735] about the domain and you are focused on the domain while shapes are very good when you are
[1742] focusing on the graph on the rdf data so and those are things that are different um
[1749] another way to to say it is that people who work with ontologies are
[1755] could be the ontology engineers and people who work with shapes could be
[1761] data engineers so they are more people more practical in a someway okay but i know
[1766] that of course this is a very rough classification but this is a a way of thinking about this
[1774] okay so just this is a slight uh i just wanted to say
[1774] Previous validation approaches
[1782] that uh what the motivating part is that there were other previous validation
[1787] approaches but this is the part that i will probably escape just to say that uh for example i was doing before
[1795] working on shape expressions i also was proposing to use a sparkle to validate but the problem of spark is that it is
[1801] very verbose and the same i mean trying to validate something very simple
[1807] can take a lot of time for example this is a very simple way to validate you have a name which is a string
[1812] and you have maybe the gender which is female or male and this is the sparkle
[1819] query to try to validate this so this is one of the problems of a sparkle there were also another
[1825] proposal was the spin that also later evolved to the shackle and also we have a star dock
[1832] they also have the another way an oslc so those are the main approaches but there are
[1838] several approaches but later they all converge in these two main approaches which are i think section
[1838] Section 2 Introduction
[1845] second and this is the topic of this validation of this tutorial about sections again
[1853] i have to say that i think everything started almost in 2013 you know there was a
[1860] workshop about rdf validation and the conclusion of that workshop was that
[1865] there was a need of a higher level language which was more concise and that
[1871] language could work for rdf validation so that was one of the conclusions of of this and i i attended i had the
[1880] chance to attend this workshop um i met there eric
[1886] he was already proposing a language for that and i joined efforts with within uh to
[1893] say okay i will do another implementation i was learning a skull at that moment and so
[1899] so he did an implementation in javascript and i worked in another implementation of shape expressions in scala and we
[1907] did this the first proposal for that then there was the w3c datasets working group that was
[1913] chartered one of the inputs was sex but there was a
[1918] there were other people who joined and there was a bit of a disagreement between the different approaches
[1925] and the result of the data steps working group was later a shackle that was accepted as
[1931] a recommendation the people who were working on sex uh had some disagreement with some of the
[1938] proposals on circle so there was a bit of a division there uh later those two communities
[1946] separated and probably i am one of the guys who i try to to to be in
[1953] both sex and circle but most of the people are there are some people in sex and there are other people in shackle
[1960] and i think that's not good and probably in the future uh the ideas should be to to converge but
[1966] at this moment that's the reality so at this moment later uh sex in 2017
[1972] was released as a community it was not a recommendation it was a w3c
[1978] community group draft and later sex was adopted by wikidata
[1984] and was i think was a very good thing for for sex because
[1992] more people were attracted to useless sex and at this moment there are a lot of
[1998] use cases as i will try to explain later using sex and other use cases using
[2003] shackle and and that's that's the reality and i don't know what's going to happen in the future
[2008] okay so let's see you were able you were not able to do the the thing is
[2016] that i don't know you can hear me but i cannot access the chat for whatever reason ah okay so maybe we
[2023] should start something more collaborative where thank you francisco now i can hear
[2030] you much better so if you want to to do the question just yeah thank you thank you so um
[2035] in the in the this was related to the slide you were
[2041] just basically discussing uh our versus rbf and basically my
[2048] my point is that i notice a lot of people particularly people so you can see in
[2053] the community there is like still people who believe that all too should be the modeling languages for
[2058] ontologies and there are people who are discussing the idea that basically the only thing you need is rdf plus
[2065] some validation rules like the one that you are showing today in the tutorial and i was just basically wondering uh
[2074] basically what this is uh your position regarding that i mean you think that basically
[2079] these validation rules together with uh with the with rdf data is just sufficient
[2084] although i think you see there's still the utility of of using out thank you yes thank you
[2090] very much for your question i was very i was uh it was interesting because my my
[2096] position there is not to replace all and my position is
[2101] is on that i mean i think there is a field for both
[2108] so so if i go back to this slide i think they are not contradictory and you can
[2116] have both in your problem you can have people who are ontology engineers who are
[2121] focused on their domain and you can have different ontologies and you can
[2126] combine definitions from different ontologies you might need to have an ontology of people
[2133] another ontology about products of books and you just join
[2141] information from those ontologies and on the other hand you also have data below and then you can
[2147] have rules here and those constraints and rules but those rules in my opinion those
[2153] rules are for your specific domain or sorry for your specific problem so
[2158] you have for example imagine that you are working for one problem where you have books and
[2166] people and you want to represent the data model in that problem and you put those constraints in that data model
[2172] that's the representation that you obtain for example for elsevier you have one one publisher that has people
[2179] represented with some properties and books represented with other properties but you also can have an ontology which
[2186] is a more general ontology of people and imagine this is uh you have this definition of ontology of
[2193] sorry of shapes for elsevier and then you have another publisher for example springer which has
[2201] a another data model and another a different set of shapes and you could have in that
[2209] different problem you could have another set of constraints so from my point of view
[2215] ontologies can coexist with shapes ontologies should be defined
[2222] in a way that have less constraints and are much more reusable and
[2229] shapes could be i mean you could have libraries of saves and that's something that i was planning to to talk
[2236] later you could have libraries of reducable sales but usually shapes
[2241] are much more problem oriented so there are shapes and constraints they are usually
[2247] for your particular problem and when you want to validate your particular data
[2252] while ontologies are for example if you have a very good ontology of person
[2257] you could use that ontology of person and you could reduce that ontology in other different problems so
[2265] i think the three have uh i mean both ontologies uh shapes
[2273] and data can coexist and in hearing shapes you could also have some rules but
[2280] i mean probably the problem here is where you put the rules you could have the rules in the ontology or you could
[2286] have the rules and constraints or you you could have a different thing called rules where you want to inference
[2292] to infer differences that you cannot infer with with ontologies so that's my
[2297] point of view i don't know if i solved the question yes i just wanted just to basically challenge in this example you
[2297] Challenge
[2304] were showing is that basically there is the potential danger of basically ending to a situation where actually
[2310] people understand the data in a different way so basically you go back to your example basically
[2317] you will see that in the shapes you basically you are making some assumptions one is
[2322] basically that you have unique id you are using you are following the the unique
[2328] name assumption right so basically when you just say that you have uh two parents uh basically you are
[2334] assuming that all the ideas in your rdf graph is actually different so basically h id
[2340] it means basically represent a different entity when you go to wow which basically doesn't follow this rule and
[2346] this is open wall basically that implies that you may be and this is not actually wrong
[2352] basically just say that you can have only only two parents but you have two three individuals that
[2358] basically are referred to the parent or person then you basically you can just assume safely that because you don't
[2364] have full information about the world about your domain basically two of the individuals basically represent the same thing and
[2370] actually it's not wrong it's just basically your assumptions so basically you end into the danger of
[2375] basically misunderstanding of or making assumptions about the data that
[2381] perhaps are not complying with the our definitions or vice versa it's not the our
[2387] definition and not and that is actually very difficult in a in our in in in a setting like this is
[2395] the web and the internet where everything is distributed and you might have people in different organizations looking at the same data
[2401] but following different constraints so basically the implied meaning the the meaning of the data depending on
[2408] what you are following might be different in different organizations or for different people and that is actually a
[2413] bit i would say that this is uh an implicit danger of basically the coexistence yes but i mean this
[2421] that's why i say that you could have reduce a library of reusable shapes for
[2428] example if you are working in a big organization where you have a multinational organization where you
[2434] have and you want all of the different uh national uh organizations to follow the same set
[2441] of shapes you could have that library of saves i mean i know i was not saying that you are going to use your saves in your
[2448] in just your particular domain but yes i think they are complementary i mean i think uh
[2456] and probably yes shapes uh put more constraints on the things that you have in ontology
[2462] but i think that's good i mean i really think that uh that's very useful uh where in practice uh you you need i mean
[2471] otherwise you have the i mean sometimes it's very useful to
[2476] have ontologies but sometimes you want to to know to put constraints on the data that you
[2484] have in your data store okay so that's my point of view so i really think that
[2490] they i mean in practice i think this is very useful to have
[2496] the three and probably i mean yes it's possible you have you could have assumptions different assumptions uh
[2503] okay and that's i'm i mean in the last part when i was i was going to talk about how i use
[2511] saves for example for continuous integration uh i think if you have a
[2517] if you are working with continuous integration you could have shapes which are compatible with with
[2522] ontologies and in fact i use shapes to validate
[2528] ontologies also but maybe that's for a different topic so maybe i can talk it about that later
[2534] okay but i partially agree with that okay okay let's continue okay thank you for the
[2540] question okay so
