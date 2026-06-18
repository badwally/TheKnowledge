---
schema_version: 1
id: yt-Z6Yy1xxWQ_0
type: youtube
title: Headless BI Architecture and Trade-offs - Pavel Tiunov, Cube Dev
url: https://www.youtube.com/watch?v=Z6Yy1xxWQ_0
authors:
- Presto Foundation
ingested_at: '2026-06-18T01:38:30Z'
content_hash: sha256:10bf97b9b794eab52f5bef6e8f9ed2605cbc63376fe270e03e243d1afd1526a0
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Presto Foundation
  channel_url: https://www.youtube.com/@PrestoFoundation
  duration_seconds: 892
  caption_track: cached
  snippet_count: 299
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:30Z'
  user_correction: null
---
[0] yeah great question about like deleting
[2] the table
[3] um I'll try to address this question uh
[6] during my presentation
[8] so I'm going today to talk about
[11] headless bi and semantic layers you
[14] already heard about this today
[17] so
[18] um
[20] couple words about myself I'm co-founder
[23] and CTO at cubedev and I'm original
[27] author of a cube I'm really fortunate to
[31] be able to manage right piece of
[34] software that has so many stars as a
[37] press that has
[38] but no one knows about it
[41] does anyone know what the cube is
[45] all right
[47] just some of you but no not all of you
[50] let's fix this so
[52] um
[54] all right so let's talk about headless
[56] bi
[58] um this is a term that was going back in
[61] 2021 uh by folks called a base case so
[67] they basically noticed that in a modern
[72] data stack you have a lot of data
[74] sources on one side and a lot of data
[78] tools that consume the data on other
[80] side and more importantly you have
[84] a lot of folks like enrolls that
[87] consuming the data within organization
[90] and they they were started to think
[94] about
[95] uh what if all this stuff is connected
[98] and
[99] um basically you end up with picture as
[103] this you you end up with some
[107] really not structured piece in in
[109] between and they wondered if there
[112] should be something like as a category
[114] category in a modern beta stack that can
[117] fill this Gap so and they ended up with
[120] a headless Bay term
[122] so but not there they actually like
[126] invented the idea itself uh and um
[130] basically
[132] this is like if you start to think about
[135] like the Headless bi wear and what
[137] precedes is it's a semantic player and
[142] um if you're as old as me you've
[144] probably seen pictures like this uh
[147] and basically the truth is is actually
[153] uh semanticleer is um steel and was part
[159] of many many bi tools out there and uh
[164] um but one I guess bi2 stands out so and
[169] this is Luker
[171] so they were very successful to making
[175] semantic wear in a code and this is a
[178] low camel probably you're familiar with
[180] that and they were very commercial
[183] successful with it and
[186] was one of one of the keys in this
[189] success and
[192] the Year this headless bi article went
[196] out the Google announced that their
[199] partner with Tableau long-term
[202] competitor of lucar to provide uh looker
[206] with an API that will be able
[210] will allow like the blue users to
[212] connect it to looker and visualize data
[215] with Tableau instead of looker itself so
[219] here we'll enter the Headless bi term so
[223] keep the semantic layer caching access
[226] control and the couple visualizations
[228] and you you'll get the Headless bi IDM
[232] so and if you follow modern data stack
[235] space there were there was there was a
[239] lot of headless Bay tools popping around
[242] um in it last two years
[245] um yeah so let's talk about headless
[248] bear architecture
[250] um
[251] so we believe that there are
[254] four
[256] um
[258] uh base pieces of headless Bay
[261] architecture as data modeling Access
[264] Control caching and apis
[267] so let's go through each of those
[270] so if you think about like data modeling
[274] or semantic where there was
[277] Innovation and a last decade
[281] it's called life query and most of bi
[285] tools supported is basically uh bi tools
[289] that can
[291] generate a SQL and upload all query
[295] execution inside of data warehouse
[297] instead of downloading the data and all
[300] modern bi to suffer this approach and if
[305] you if you are familiar with a more old
[308] school approach it used to be like
[310] downloading the data and every bi tool
[313] supported downloaded downloading the
[315] data
[316] and um so and data modeling
[322] like uh in terms of how you can generate
[325] this SQL code is usually end up
[330] in a in another code and it's um usually
[333] like multi-dimensional model so it's
[337] called the very different uh it has very
[340] different names and very different tools
[342] we call it cubes and it's actually
[345] historically it's called a lab cubes or
[349] if you're familiar with the term it's
[351] called relational lab
[353] so it allows you to Define your data
[356] model in terms of Cubes measures
[358] Dimensions Etc and then this model is
[361] used to generate SQL for your data
[364] warehouse
[365] so on top of this first piece you're
[369] adding uh multi-talancing security
[372] control
[373] this will allow you to do stuff very
[377] simple stuff from
[379] role-based access security hiding
[381] columns
[383] restricting likes rows visual level
[387] access security and also
[392] doing very crazy stuff like uh measuring
[396] your API quarters for example yeah so
[399] that can be done as a as a part of
[403] Access Control
[405] then their caching goes and we think
[408] caching is very essential piece of
[411] um headless bi and every bi2 by the way
[415] has some sort of caching and there are
[418] two types of caching kits in memory
[420] caching and so-called aggregation
[422] awareness and this use Case by the way
[425] uh one of the most major use cases for
[428] of our pressed customers and Athena
[431] customers because uh
[434] as you may know like uh Presta can be
[438] not very like responsive for really big
[441] queries it will take like 10 60 seconds
[444] maybe minutes uh to process like single
[447] query but if you peregrate the data
[450] materialize and uh
[452] very efficient store
[455] in QP we build around which is called
[458] cubestore and it's capable to serve like
[461] billions of rows in a single cache table
[465] and this allows your users to access
[468] this Aggregates instead of raw data and
[472] basically optimize user experience here
[476] and last but not least it's an um
[481] basically apis so there are two types of
[484] apis in headless bi so first one is
[487] obviously SQL and this
[493] API allows you to connect all uh
[498] basically data tools because all these
[501] tools speak SQL
[503] and there are two approaches with SQL uh
[506] one is basically to provide
[509] to mimic some protocol for example Cube
[512] mimics postgres and redshift another way
[515] as DBT does you can use team plating and
[518] proxy some workload to data or houses
[521] yeah so
[523] and we see both of those used
[527] in virus tools
[531] and this again this SQL API allows you
[535] to
[537] um
[538] connect
[540] your headless bi to other bi tools for
[543] visualization and because of live query
[545] mode so you you can
[549] offload your query processing to
[551] headless bi instead of data or house but
[554] headless bi another hand uses the SQL to
[558] generate SQL for data or house and
[561] that's
[563] how this question about deletion table
[567] comes together so you can rename
[569] actually drop tables under an underlying
[573] like data sources in underlying data
[575] sources but actually for your users it
[578] will be the same table so nothing
[580] changes for users so it provides your
[583] decoupling of actual data which lies in
[586] your data source from what your users
[590] see
[591] in API in this particular learning SQL
[594] and another
[597] SQL oh sorry another API which is
[601] rest and graphql API is very handful
[605] when you're trying to build embedded
[607] analytics solution and you
[609] basically at the point where you want to
[613] build a custom
[616] build UI and have a really native
[619] experience for for your application for
[621] and for your customers
[625] all right
[626] um
[627] so
[629] let's talk about trade-offs
[632] yeah I will talk about only a
[636] um
[637] semantic layer trade of Muslim and like
[641] data modern trade-offs so once you go
[644] with this approach
[646] there are
[648] basically main General trade-off you can
[650] think of
[651] it's
[653] as its control versus flexibility
[656] and as
[658] how much you define on your semantic
[660] query in your semantic layer data
[663] modeling clear versus how much you model
[667] on your bi side of things let's consider
[670] this specific example uh for example we
[674] want to calculate daily active users to
[678] weekly active users right here and there
[681] are other ways of doing this calculation
[683] you either can model this calculation
[686] right and you enter your inside your Obi
[690] tool or any data consuming tool
[694] basically by dividing two of those
[697] measures or you can
[700] Define this
[702] at your data modeling
[706] layer and
[708] the trade-off here would be
[711] what if this
[713] metric definition would change in future
[716] right so if it changes in future
[718] everything
[719] what depends on this metric will be
[722] updated automatically and in the case
[724] you allow users to write their own uh
[728] calculations it's not however once you
[732] idle this
[736] uh like specific measures like daily
[740] active users and weekly active users uh
[743] people can do their own calculations
[745] anymore so this is trade-off
[748] around control and flexibility here
[752] uh
[754] another one example would be joins so
[758] pretty the same idea as in previous
[760] example however a more complex one in
[763] terms of what can be allowed and and
[766] what's not so let's for example think
[770] about
[772] this model like orders customers and we
[777] our people to join them in a bi tool
[780] right uh
[782] you also can use
[787] feature of cube so-called views
[791] or in Luca it's called explorers and to
[794] fix actually all the joint paths and it
[798] will be either a star schema or
[801] snowflake schema
[802] and All Join piles will be preset and
[806] users cannot change it and however
[812] in this case users can change how joins
[816] behave right so again this will will be
[819] read off about control versus
[821] flexibility and what user can query and
[824] what's not
[826] um
[827] and press the same example as a royal
[830] security so uh
[833] you can expose all the fields which can
[835] be used for
[837] basically filtering your data uh on a
[842] like cement clear site or like headless
[844] Bayside right but
[846] another hand you can
[849] delegate all the role well security to
[852] your cement clearer and in this key case
[855] so you you actually
[858] don't need to think about authentication
[861] and no sorry not authentication about
[864] authorization on API stuff and maintain
[867] it yeah you just delegated the semantic
[870] player and if it changes all all
[872] Downstream data tools can receive this
[875] update yeah another hand you remove any
[880] like flexibility to control any security
[882] features on uh inside of Downstream
[886] tools yeah so yeah thank you that's
[889] that's it from my side and I would love
[892] to take your questions if any yeah
