---
schema_version: 1
id: yt-ai4YdLiCGNM
type: youtube
title: How to handle data about what does not exist
url: https://www.youtube.com/watch?v=ai4YdLiCGNM
authors:
- Barry Smith
ingested_at: '2026-06-18T01:38:15Z'
content_hash: sha256:755e9831111758fa8cb087fc66faf5c99ce64a9d2a1aa006accb48e87374c855
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Barry Smith
  channel_url: https://www.youtube.com/@BarrySmithOntology
  duration_seconds: 654
  caption_track: cached
  snippet_count: 246
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:15Z'
  user_correction: null
---
[2] this is a brief introduction to the
[4] modal relations ontology which is part
[7] of the Common Core ontologies developed
[10] by Rod nud Niki and his team in Buffalo
[13] and um I'm summarizing now ideas
[16] developed by the team for describing
[20] entities such as planned or designed
[23] entities which on a realist perspective
[27] uh don't exist you'll see that we have
[27] The Common Core Ontologies Import Structure
[30] Foo at the top and then we have a
[31] relation ontology which is imported from
[34] the very large collection of relations
[37] in the relation ontology which was
[40] created by the OBO Foundry you will also
[43] see in the top right hand corner
[45] something called the modal relation
[47] ontology which I'm uh I'm very
[49] interested in uh showing to you because
[52] I think this is also an original and
[54] unique
[55] contribution and um so the you can see
[60] how they're divided time and place
[61] attributes physical objects
[64] processes and there are um many many
[68] different users of the Common Core
[71] ontologies um had many different uses of
[73] the Common Core onology so the Cyber and
[76] sensor domains the space mission domains
[79] so you'll see that there is a a sort of
[82] tilt in the direction of what might be
[83] interesting from the point of view of
[85] the
[86] military uh but the commic cor
[88] ontologies themselves are all free and
[91] open
[92] source um what happens is that we have
[92] The Common Core Domain Ontologies
[95] domain ontologies for things like um uh
[100] military
[101] planning which are uh not not quite so
[106] freely available as the Common Core
[108] ontologies themselves at the top
[112] here um and now the way that commic cor
[115] ontologies are used is one way is by
[119] taking large databases so yesterday I
[122] talked a little bit about the the large
[124] number of government um repositories
[127] with catalogs and taxonomies attached to
[129] them so we take data of that sort and
[133] then we use the com Cor ontologies in
[135] order to tag the column headers in such
[138] data tables and this turns out to be a
[142] very efficient way of acquiring
[144] semantically enhanced data for various
[148] purposes and so it principle we can do
[148] Aligning Data with OSCAR
[150] this to create ontologies of the data
[153] that we have at very high levels using a
[157] tool called Oscar which creates on
[160] ontology chains semi-automatically from
[162] raw
[164] data and
[164] Design Challenges Encountered
[167] um now there are various problems um
[170] which arise as soon as you start using a
[174] highly General mid-level ontology in
[176] this way so attributes change over time
[179] how do you deal with things like ages
[181] people get older and so uh how do you
[185] deal with that in such a way that you
[187] you always have uh data which is up
[190] todate uh and correct and then there is
[193] a problem with keeping track of
[195] Providence how do you know where
[197] specific kinds of data come from and you
[200] also have a a big problem which is what
[202] I want to deal with in the final couple
[204] of minutes um so bfo is realist ontology
[211] as contrasted with the famous dce which
[214] everyone knows about which is a an
[216] ontology which deals also with
[219] non-existent entities such as Nica
[222] guarino's 14th
[224] daughter and bfo does not want to deal
[228] with non-existent entities because it
[229] wants to be a realist
[231] ontology but there are entities in the
[234] world which are very important to
[236] bfo which deal with non-existent
[240] entities and they are for instance plans
[243] and
[244] designs and bfo does not want to be in a
[247] position where its ontology cannot deal
[250] with plans and designs and so
[255] um we're going to see how bfo can deal
[258] with plans and Designs by looking at the
[260] modal relation
[262] ontology so um we we've talked a little
[266] bit about the problems which arise when
[269] entities are dealt with over time for
[272] instance when they age and I'm not going
[272] Constraints on Expressions of Object Phases
[275] to deal with this because it will uh it
[277] will distract us from what I really want
[277] Object Phase as Stasis
[279] to deal with but let me just mention the
[283] the idea of
[284] stasis so when Abraham Lincoln is
[288] President then he has a president
[292] role and this President role occupies a
[296] certain temporal
[298] interval and so we reify the president
[302] role in order to be able to assert that
[304] Abraham Lincoln was president at a
[307] certain time and uh this turns out to be
[310] a very uh valuable way of dealing with
[315] the problems which arise as a result of
[317] the fact that people can
[319] change and this idea of a stasis a
[322] stasis is a very boring process it's a
[326] process which does not involve any
[329] change
[331] and we other people use the word
[334] state but the word State means so many
[337] different things to different people
[339] that we we found that using an odd word
[342] stasis and defining it very carefully as
[345] a process kind of process just a flat
[348] process if you like is more
[351] useful and uh we won't talk about
[355] literals um we won't talk about the way
[359] CC deals with
[361] Providence um we won't talk about uh the
[361] Representation of Planned Events
[366] ways Providence are recorded because we
[368] want to talk about non-existent entities
[371] or rather we want to see how we can deal
[375] with what people think they are doing
[377] when they think they are talking about
[379] non-existent entities within a bfo ccoo
[383] framework and so we're going to look
[386] very quickly at designed artifacts
[388] predicted outcomes
[390] and reference of false
[392] statements and um what what we want to
[397] to do we want to uh stick with realism
[400] so we shouldn't be able to infer from
[402] anything that we say anything that is
[405] false and we don't want to be able to
[408] infer from anything that we say that
[410] some non-existing entity
[413] exists but we do want to make it
[415] possible to
[417] compare actual entities
[421] with what looked like non-existent
[423] entities and an example would be we have
[426] an airplane which was built to a certain
[430] specification and the airlane is
[432] delivered and it flies but when they fly
[436] it it it proves not quite to satisfy the
[439] specification it's heavier or slower or
[443] um there is some difference and so the
[445] airplane as specified in the
[448] requirements
[450] specification on the
[452] box is not exactly the aircraft that is
[457] actually on the field about to take
[461] off and so this distinction between the
[466] desired specifications and the actual
[468] specifications is very important in
[470] manufacturing so how do we allow
[473] comparisons between actual entities and
[476] putative non-existent entities so that
[478] that problem
[480] is solved by the modal relation
[480] Representation of Nonexistent Entities
[484] ontology and what the modal relation
[486] ontology does is the following we create
[489] a copy of all the relations in bfo and
[493] CCO but we it's a it's a different
[497] relation with a different name
[499] space and when we use relational
[504] expressions from the modal relation
[506] ontology then the ontological commitment
[509] to the existence of the reference of the
[511] corresponding statements goes
[514] away so we can make all the comparisons
[517] that we want and we we create
[521] sentences which look very much like
[523] sentences about real objects but because
[527] we're using the modal relation ontology
[529] we cannot infer that those real objects
[531] exist in the way that we can always
[534] infer that they exist when we use the
[537] plain vanilla relation ont ology of
[540] which the modal relations ontology is a
[542] copy now this is a very simple idea it
[545] allows you to understand what's going on
[547] in
[548] designs the relationship between a
[551] design and the designed
[553] object is very
[557] similar whether or not the designed
[561] object ever gets built so in other words
[563] when we're talking about the
[564] relationship between the design and the
[566] designed object in the case where a
[568] design is never ever realized which is
[570] in most cases and the way we talk about
[573] that relationship when when the designed
[576] object really does get built which is
[578] when you're really
[579] successful they are similar kinds of
[582] talk but there's a big difference we
[584] can't infer the existence of the
[586] designed object the product in the first
[588] case and we can in the second
[591] case all right and so this is how we
[593] represent plans using the modal relation
[596] ontology and you just see mro everywhere
[600] and we can talk about testing of the
[602] artifact which is the result of uh the
[605] plan even if it never even if the
[607] testing never
[608] occurs and this is the way we deal with
[608] Comparison of Actuals and Plans
[611] the difference between actual events and
[613] planned events which is also a
[615] comparison of the sort which for
[618] instance military organizations are
[619] making all the time because they want to
[622] plan in such a way that they follow the
[625] track which led to success rather than
[627] the track which led to failure
[630] these are some of the people who are
[632] either using uh common core ontologies
[635] or reviewing it for purposes of use so
[638] the industrial ontologies Foundry which
[640] I talked about they are using it in a
[641] big way and some of the
[644] other manufacturing organizations
[646] mentioned here are uh supporting the
[649] industrial ontologies Foundry and so
[651] they are using it also and with that I
[654] will stop
