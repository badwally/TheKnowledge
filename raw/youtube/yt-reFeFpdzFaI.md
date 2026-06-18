---
schema_version: 1
id: yt-reFeFpdzFaI
type: youtube
title: Xavier Bresson - Integrating Large Language Models and Graph Neural Networks
  - LoG 2024 Keynote
url: https://www.youtube.com/watch?v=reFeFpdzFaI
authors:
- Learning on Graphs Conference
ingested_at: '2026-06-17T20:57:34Z'
content_hash: sha256:000b7bfba2737edcdead34b683d9c6504d00c31d5d9b8bddd6450551466745f8
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Learning on Graphs Conference
  channel_url: https://www.youtube.com/@learningongraphs
  duration_seconds: 3616
  caption_track: fetched
  snippet_count: 1361
filter:
  score: 0.75
---
[2] all right so I think we can start um
[6] I'll keep it very brief uh it's my
[8] pleasure to introduce zavier Bron uh
[12] zavier is associate professor at
[14] National University of Singapore and he
[18] needs no introduction he is the Pioneer
[20] of graph deep learning um he has some of
[23] the most cited Works has organized
[26] several conferences and tutorials
[28] including being a huge support of the
[31] learning on graphs conference and
[33] winning some of the biggest individual
[35] grants for This research so zav take it
[40] away all right thank you for the
[42] introduction chanana so welcome everyone
[44] and thank you for for joining so um I'm
[47] excited um to talk to you about graph
[51] neuron Network and large language model
[52] so this is a collaborative work with sha
[56] shinki Brian Hoy Thomas Lauren Yan LUN
[60] and other uh
[64] collaborators okay so uh here is the
[66] outline of the talk so I will first
[68] introduce large language models um and
[71] then I will ask the question if we still
[73] need graph neuron networks in the era of
[78] llms um I will review the advantages and
[82] limitations of large language models and
[84] graph neuron networks uh to identify uh
[88] task where this combination can be
[90] useful and in particularly I will
[93] present uh two uh works the first one
[96] will be to use uh llms for improving um
[99] GNN resoning and the second one will use
[102] GNN for LM resoning and I will
[106] conclude all right so I think we live um
[108] in a very exciting times uh with the
[110] Deep learning Revolution uh compared to
[113] when I I was doing my PhD um so um
[116] computer vision completely changed with
[118] the introduction of deep learning as you
[119] know so it was in
[121] 2012 uh with image net architecture at
[124] that time was um convolution network is
[127] still U very powerful architecture um
[130] with alexnet um eight layers 60 million
[133] parameters uh two gpus and the industry
[137] quickly understood actually that uh that
[139] was going to be very um uh very um um
[145] productive uh for uh to make money so um
[149] it works very well for uh automatic
[152] recommendation um it will work pretty
[155] well in autonomous vehicle it's coming
[157] um and of course for uh surveillance
[159] this is a very powerful tool um the the
[164] revolution for natural language
[165] processing came a bit later in 2022 so
[169] data set was uh internet basically the
[171] architecture was a
[173] Transformer um and there was much more
[176] layers like 100 layers and 17 five
[180] billion parameters compared to Alex net
[183] number of gpus was also much larger um
[187] from two to 10,000 and but um it really
[190] created a new industry that we call
[192] generative AI for everyday task for
[195] example coding text summerization
[197] content creation dialog system
[199] everything is um automatic now with this
[202] system and and actually um people gave a
[205] name to this large pre-train Network um
[208] train on massive uh data set this is
[210] called a foundation
[212] model so we have now this generative a
[214] industry booming um so for example Tech
[217] generation we have proprietry llms with
[221] GPT gimi from Google uh Cloud anthropic
[225] and Croc um um Twitter and we have also
[229] open source llms uh thanksfully you know
[232] thanks to um to meta and Yan Lun
[235] basically we we are able to uh you know
[238] manipulate uh this llm and this is
[240] fantastic for researcher like us so Lama
[243] Tre
[245] mistol gimma gima by by Google data set
[249] are quite quite huge um but something
[252] also interesting is that the
[253] architecture has not very changed from
[255] you know
[257] 2020 um so it's still a decoder there
[260] are some few few improvements but
[262] basically this is still you know a
[264] Transformer the hardware changed quite a
[266] lot so it's 20,000 um gpus uh if you
[269] want to buy it for for yourself so it
[271] would cost today like 4 billion US
[273] dollar and the next generation is going
[275] to be even larger with
[278] ,000 uh you know H1 gpus for image
[282] generation so we have also poetry models
[285] like M Jour flux stable diffusion and
[287] Deli uh we are not lucky for researcher
[290] because we don't have access to this uh
[291] open source um um you know models thata
[295] set are quite huge um and architecture
[298] also strangely is still you know
[300] Transformer with some variants but this
[302] is called a visual Transformer and we
[303] use diffusion model so this is the new
[306] uh stable way to do uh um to generate
[309] new data um yeah so um this llms they
[314] have been trained on on internet
[316] basically and we know that internet is a
[318] network right is a network connecting um
[321] web pages and each web page is basically
[323] a text document with a lot of
[325] information so um so and then if you
[329] look at for example also Wikipedia um uh
[332] so you have you're going to have links
[334] inside uh the web page um connecting to
[338] other Wikipedia Pages the same also if
[341] you take a Json file so there is a lot
[343] of Json file on internet for the
[344] structure of um uh of websites and when
[348] you open uh ajon file you will see links
[350] so there is a lot of links so basically
[353] what it means it means that llms have
[355] been trained on graph data and a lot of
[357] graph data because internet is uh not
[359] only the text but also the connections
[361] between the text so um they have learned
[365] uh you know the relationship between
[367] Text data so the the thing that they
[370] have been trained on so huge massive
[373] data sets so they are able to you know
[376] identify for example relationships
[377] between entities if you ask them and
[380] also predict non labels in a network for
[382] example of scientific articles so when
[386] llm came B basically with with a uh with
[390] Shing e and and and and my collaborators
[393] basically we asked the question do we
[395] still need GNN actually for you know
[397] reasoning over graph structure data U
[400] because llms have seen everything right
[402] so they have been trained on on on on on
[405] internet so they know graph graph data
[409] so that was I I was very worried to tell
[411] you the truth so um so in this talk I'm
[414] going to focus on text attributed graph
[417] so they are basically what we call text
[419] textual graph so each node uh is going
[422] um to be connected to other nodes for
[424] example here this is a Knowledge Graph
[426] and each node the feature will be text
[429] okay and also the The Edge information
[432] to the the the connection between two
[434] notes and the The Edge feature will also
[436] be text okay so uh it's basically um a
[441] topological graph and on the top of it
[443] you have a lot of text uh
[445] information so we will not consider
[448] non-textual graph like molecular uh
[451] graph this is not the goal of this uh of
[453] this presentation okay so first of all
[456] uh what what we did uh was okay let's
[459] look at a popular data set uh and let's
[462] try to um predict using llm so the
[465] popular data set we use was U the one
[468] from OGB um so this is ogn archive so
[472] this is um um a data set which is a
[475] network of scientific uh papers um so
[479] the number of not is 170,000 number of
[482] Ages is 1 million and here the task is
[484] basically a prediction task for the
[487] class of the paper so um we have 40
[491] classes to predict and the node feature
[493] are basically the for each node this is
[495] an article so you have the title and you
[497] have the abstract and you just want to
[499] predict you know the class so um the
[502] results are as follows uh so if you use
[505] a GNN uh train on the bag of word
[509] features uh given by OGB Library uh
[512] basically you would get 70% accuracy
[516] okay now if you look at the OGB
[518] leaderboard um the SOA paper is actually
[521] a Glam which is a combination of a
[524] language model and a graph neuron
[526] Network and uh the Precision W
[529] 76.6 uh per accuracy okay and then what
[533] we simply did is basically we took at
[535] that time it was 2022 we took at that
[537] time the best llm that was GPT 3. .5 and
[541] we asked that you know given the title
[543] the abstract and the 40 classes to
[545] predict actually the the correct classes
[548] and he was able to do
[550] 73.5% accuracy so the good news is that
[555] um it's not um better than the
[558] state-ofthe-art using GNN is still
[561] closed but uh I think this is um that
[564] was a big relief I think for for me um
[567] that we still need a GNN in the of of
[571] llms also something that was interesting
[574] is that of course probably the OGB data
[576] set um was uh was part of the training
[580] data set of uh GPT 3.5 so remember GPT
[585] 3.5 was trained on internet and probably
[588] this data set was part of the the
[590] training data so we have seen the the
[591] test set and this is what I
[593] mean okay so now let's try to see um the
[598] uh how how how can we com find um graph
[601] neural networks and large language
[602] models uh so for this we need to
[604] identify what are the um strengths and
[607] also the limitations uh of these
[609] techniques so large language models uh
[613] they are really impressive uh they are
[615] able to accurately model language
[617] distribution so predicting the next
[619] world uh given the context they do that
[622] you know it's it's very impressive um
[625] and and they have been trained actually
[627] on everything you know from human
[630] knowledge which is on internet so so the
[632] way I see it for me is like so you you
[634] you have the human knowledge which is
[636] which is here um and then you you have
[639] this llm which is some kind of AI Oracle
[642] okay so an oracle knows everything you
[644] have seen everything and then humans we
[647] we go to the Oracle and we ask we prompt
[649] the Oracle okay um give me an answer to
[653] my question so he will answer something
[655] okay so you can ask anything toac
[657] understand something but the problem
[659] with is that because you has so much
[661] knowledge you need to have a very
[663] precise you know questions to the to the
[666] Oracle authoriz it will not give you the
[668] answer that you like okay so but still
[671] you know that was that was very
[672] impressive at that time so in 2020 when
[675] GPT 3.5 um was released so very strong
[679] zero short capabilities so the scaling
[681] lows um despite some people can say
[683] today uh for training and inference have
[686] not yet saturated so bigger networks
[688] larger data set longer training time
[691] longer search inference actually still
[693] improve the result and and it's very
[695] easy to see why it's because companies
[697] they are buying more and more gpus so we
[699] know that the scanning loss is is is not
[702] dead the limitation so we know that
[705] because again we we don't know how to
[706] prompt correctly an llm they we they
[709] will make you know errors uh we call
[711] that gently hallucinations but this is
[714] basically very bad answers uh so they
[717] have logic uh they have also Limited
[719] logical reasoning so for example there
[721] is Terry Taro which is um who is like a
[724] very strong mathematician and it try you
[726] know the last version of GPT and you say
[728] basically oh um they are actually very
[730] limited uh again you need to you need to
[733] give them a lot of precise pump to make
[735] it work so they have a limited logical
[737] reasoning uh so what openi try recently
[740] to do is to improve that by learning um
[743] you know um chain of thoughts for
[746] example and also for inference to do
[748] search algorithm so it proves uh this
[750] limitation but it's still not there um
[753] they have also limited graph with
[754] inabilities even again if they have seen
[757] the test set of the graph task during
[761] training for GNN I think strength is
[764] basically to be able so if you have a
[767] graph like this and you have a question
[768] for example is the monalisa in the same
[770] city as Alice friend Bob so you have
[774] here monalisa you have the city you have
[777] Alice you have Bob so if you do multiple
[779] layers of GNN what you will do you will
[781] basically learn a multi-op path that
[784] will go through uh the solution of your
[786] task so they are very they are very you
[789] know good to do that and they are very
[792] effective for many different modalities
[795] and you know now we're talking about
[797] text but they're also very good for for
[799] example um you know physics biology
[803] combinatorial optimization and also
[805] chemistry and we know that you know
[807] chemistry that was um that was the very
[809] good year for AI so there was a Nobel
[811] price in chemistry um for Alpha fold and
[814] alal fold as you know is an N
[817] Transformer so predicting the pair wise
[819] distances between residues in amino acid
[821] sequences so this is a graph neural
[822] network basically limitations for GNN is
[825] basically they like graph Foundation
[828] model in the scale of natural engage
[830] processing and computer vision of course
[832] the community has worked um a lot on
[835] that it's very interesting to push in
[836] this direction but uh you know there is
[839] this emergent property basically means
[841] that we need to to go beyond the scale
[843] of um training data and compute to get
[847] something very powerful uh so we are not
[850] yet there the problem is basically uh
[852] you know the data set we don't have like
[854] large data set available OGB you know is
[857] still comparatively small uh compared to
[859] image net which has 150 gigabyte of
[863] images the hardware for running Spar
[865] linear algebra is not optimized it's
[867] it's much slower than uh standard dance
[870] operations um exist pre gnns because
[873] basically of that they are small you
[875] know they they are not doing you know um
[879] billions of parameters this is basically
[881] millions of parameters and I think also
[884] something which is um today which is
[887] which is a limitation is that industry
[889] has not yet found some interesting
[891] application of of GNN because industry
[893] is really driven you know the the the
[895] the AI research and AI product uh why we
[898] have GPT today it's because industry got
[900] interesting in deep learning and then uh
[902] also to to develop you know product so
[905] um so it's not yet clear you know how to
[907] make profitable uh stuff from from GNN
[910] it will come I think but it's not yet
[913] there so combining anlm and GNN
[916] basically this is it means developing um
[918] a joint U training a joint text and
[921] graph Foundation model and this is of
[923] course a very attractive idea very
[925] promising idea but today I think the the
[928] issue is that there is a very huge
[930] imbalance between the knowledge coming
[933] from from text from um from llms and and
[937] nagee coming from from GNN so of course
[940] what we would like to do is to do some
[942] this kind you know of architecture where
[944] we have the text then the text will go
[946] through an llm it will process it it
[947] will give us some vectors U the same
[950] also for graph it will go to the GNN we
[953] we process it we give us some vector and
[954] then the vectors would be um would be um
[958] um I'm sor would be uh processed
[961] together with self attention or cross
[962] attention and for example if we do text
[964] generation so the fact that you know we
[967] have a huge difference between um these
[970] two domains I think this is this is very
[972] challenging uh so what it means it means
[975] basically that we need to tailor you
[976] know the the combination of llms and and
[979] gnns to get some value of that so for
[983] example what we can do uh we can use the
[986] llm um using the the vast knowledge of
[989] llm and then try to improve the
[991] performance of small scale uh text
[995] attributed
[996] um uh graphs and we can also do the
[1000] reverse one U that you know we can use a
[1003] knowledge graph for example to
[1005] constraint the llm to give more precise
[1009] uh response okay so reducing
[1012] hallucinations this
[1014] way so this is what we will do next so
[1016] we will um we will review two um works
[1020] that that we have done and this is
[1021] really focusing on text resoning task um
[1024] so the first work will be we will use
[1026] llms to enhance GNN resoning so this is
[1029] a work basically that is taking llm um
[1032] resoning abilities to improve uh GNN
[1036] predictions um and and it's pretty
[1039] actually effective and robust um the
[1042] second paper we we will we will review
[1044] is basically a GNN will enance LM
[1046] resoning so this is a foundation work
[1048] where we try to put together all the
[1051] benefits of um llms gnns and also uh
[1057] something that we call graph rag that
[1059] that I will
[1061] explain okay so let's see the first um
[1064] the first technique here so the this the
[1068] technique is called tape so here the
[1070] idea would be to use llm knowledge to
[1074] improve um the the quality of the not
[1077] features um in the in a tag okay so if
[1081] we have better not feature then we will
[1083] be able to predict uh you know with more
[1086] accuracy with higher accuracy so the
[1088] question is how do we extract again
[1090] information from an LM um for a specific
[1094] tag uh
[1096] task so to do that we are going to um to
[1100] prompt uh the LM because um LMR again uh
[1105] accumulated so much knowledge that what
[1107] we would like to do is to prompt uh the
[1110] the prediction the LM but at the same
[1112] times we also want to understand its
[1114] reasoning okay so we will ask the so
[1118] given for example um an article um the
[1121] article would be the title The Abstract
[1124] we would ask the prom question so
[1126] basically predict the the um the class
[1130] but at the same time we will ask the llm
[1132] to give us you know uh it's reasoning so
[1135] why did you did you decide for this uh
[1137] for these predictions okay okay um so we
[1141] call also reasoning or explanation uh if
[1143] you want
[1145] okay so now that we have the um you know
[1149] the sequence of words for abstract title
[1152] explanation prediction uh this is not
[1155] something that we can directly use with
[1157] GNN so what we need to do basically is
[1159] to have uh a mapping from sequence to
[1163] Vector okay so we want to take um this
[1166] input sequence of words and then output
[1170] uh a d dimensional Vector that will
[1172] summarize this information and that will
[1175] improve basically the um the
[1178] expressivity of this node feature so
[1180] remember that in this example a node is
[1182] an article okay this is another article
[1185] and then what we want is to predict if
[1187] there is a relationship um no I'm sorry
[1191] what we want to predict is uh you know
[1193] the the
[1194] class okay so what we propose we propose
[1198] something that is going to left
[1200] both um proprietry and open source llms
[1204] so um this technique is a kind of
[1208] interpretor between a closed llm and an
[1212] open
[1213] llm okay so the Clos llm can be GPT that
[1217] can be a gmin so we know that this um um
[1222] this closed this proi tree uh llms
[1224] actually are better than the open ones
[1228] okay so we we we we can go on the
[1231] leaderboard of um of llms and you see
[1234] that always the top two are GPT and
[1238] gimini okay so the the the unfortunately
[1241] for researcher uh proprietary proi Tre
[1244] LMS they are better than the open ones
[1247] but the problem with the closed llms is
[1249] basically that they only provide
[1251] sequence of words right they don't
[1254] provide the vectors that we want to
[1256] train the GNN so in contrast if you look
[1260] at the open source llms like
[1262] Lama or gimma um basically they they're
[1267] going to provide the text but also the
[1269] vectors right so we have access to
[1271] everything inside the architecture we
[1273] have the hidden vectors the hidden
[1274] features but also the um you know the
[1278] the output everything is uh is given to
[1280] us so what we decided to do in 20122 so
[1283] at that time GPT 3.5 was the best um
[1288] closed llm so this is the one that we
[1290] used so we we have our article so this
[1295] is the n ey in the graph given the title
[1297] The Abstract with query we get the
[1299] explanation we get the prediction and
[1302] then what we do is that we are going to
[1304] convert the sequence of uh for example
[1307] of words in the prediction by using um a
[1312] a language model so like a small one
[1314] which is De Berta in this situation it
[1316] has 129 million parameters
[1319] and here let me zoom in so what we do is
[1321] basically so we have our sequence of War
[1323] token so this is basically the
[1325] explanation if you want um and here we
[1327] have you know in any um Transformer
[1330] architecture you can have a class token
[1332] basically something uh that will
[1334] summarize uh the sequence of world so we
[1337] give as an input uh this we go through L
[1340] um Transformer layers we output and then
[1343] we get um the class token after l number
[1346] of Transformer then we go through an MLP
[1349] a small MLP to fine tune on the training
[1353] set okay so the training set we know the
[1355] the correct uh class so we want
[1357] basically to fine-tune um the MLP on the
[1361] on the correct class on of the training
[1363] set so in the MLP here it's a small one
[1366] only two layers the first layer
[1367] basically would just be um some features
[1371] um and then it would go through another
[1373] layers to get the number of classes so
[1376] for example that can be 40 uh 7 it is
[1379] cor 40 if it is um OGB archive um so
[1384] this guy here uh is going to be um a
[1387] vector of uh seven uh seven other
[1389] dimensions so this is actually going to
[1392] be our U enrich feature so this feature
[1394] will represent this the input sequence
[1397] that we have here okay and this is very
[1399] tailored to the to the task that uh you
[1403] want to solve okay so this way we are
[1405] able to uh get enrich feature for the
[1408] explanation a feature for you know title
[1411] abstract and and then we can also have
[1413] prediction feature okay so what we
[1416] should do if we uh if we are in 2024
[1419] actually we should change you know the
[1420] small the Berta language model by um Now
[1425] using a large language model okay so we
[1428] why we can do that at at the university
[1431] is basically if you take for example
[1433] Lama 2 or or or or GMA uh you can fine
[1437] tune them using this very nice technique
[1439] of Laura okay so low rank um uh fine
[1443] tuning and and basically with my small
[1446] gpus actually I'm I'm able to fine tune
[1449] you know a large language model like
[1450] Lama 2 uh so this is this is very great
[1453] okay so basically what we would do we
[1455] just need to change the proi tree llm
[1457] with the best one so you take the one
[1459] that you like um and then here instead
[1462] of using uh the betta you can use lama
[1465] lama 2 for
[1467] example okay so once you have your
[1469] enriched uh not features what you're
[1472] going to do you you are going to train
[1473] your gnm okay with this new uh note
[1476] features so you can use your favorite um
[1478] uh GNN okay and then you can make uh the
[1481] prediction so we can compare the quality
[1484] of not feature now um so we are going to
[1487] see Shadow feature um language model and
[1490] large language model features okay so
[1493] the shadow features so if you if you
[1495] look at um OGB data set so they have
[1497] already uh the designed some nice and
[1501] crafted features for each data set for
[1504] example this is Skip gram for OGB
[1506] archive um and what happened is that you
[1509] get 70% um accuracy on the on the test
[1513] set in only four minutes okay so this is
[1516] very fast and I think this is a very
[1517] good um Baseline for model performance
[1521] now as I said before um the the
[1524] state-ofthe-art is Glen um and Glen was
[1527] training simultaneously a language model
[1530] okay and also a GNN and basically this
[1533] model got the best you know accuracy of
[1536] 76.5% but of course because you need to
[1538] train um you know your language model uh
[1542] this is going to take more more time so
[1543] it's going to take you know 9.2 uh hours
[1546] okay so there is here at that time
[1548] before the introduction of CH GPT that
[1551] was really a huge trade-off between you
[1553] know if you want to increase your
[1554] accuracy you need to pay the price of
[1556] you know much more computational
[1559] um you know Hardware but also uh
[1561] training
[1562] time so now this is what what what we
[1565] suggested um basically uh we use this um
[1569] llm we prompt them we translate into
[1572] vectors and then we we fine tune so uh
[1575] accuracy was um um 75 um per and only
[1581] three hours to do that so interestingly
[1584] once we we publish the paper uh so we
[1586] got at the at the top one of the leader
[1589] board and then there was other
[1591] techniques that use the same approach of
[1594] course a little better and then now the
[1597] top three even today actually I was
[1598] surprised I I look at that um recently
[1600] so even today uh the top three models
[1603] for OGB archive are basically based on
[1606] this type
[1607] technique okay so of course one uh revie
[1611] number two uh say that oh we cannot
[1614] trust your results because um OGB
[1617] archive is part of the uh llm uh
[1620] training data set so we cannot trust you
[1623] so what we did basically is that we we
[1625] produce a new um OGB archive no not OGB
[1630] archive but an archive data set we
[1632] called it tape archive 23 so it's it's
[1634] available to download he have 77 um,
[1638] papers uh same number of classes and and
[1641] basically we have the same conclusion
[1642] there is nothing that changes uh when
[1645] when when we do that and again this is
[1647] also the reason that an then an llm is
[1650] um even if if you has seen you know the
[1651] test set um is not able to reason uh
[1655] very strongly uh with graph uh structure
[1658] so so you still need the GNN to you know
[1660] to to use the topological relationship
[1664] and to to make good
[1666] prediction we did some ablation study
[1668] what we observe is that there is no
[1670] specific feature which is better than
[1671] the others it's actually the combination
[1673] which is
[1675] important uh so intermediate conclusion
[1677] for this work so basically
[1679] um we can use the LM knowledge um and
[1682] his reasoning abilities to enhance um
[1685] the not features of the tag and also the
[1688] U make it to fine tune to the to the
[1690] specific um to the specific task okay so
[1693] what we did is something like um uh was
[1697] uh is not end to endend so we don't
[1699] train everything together it's actually
[1701] we first generate good features and then
[1705] we train the GNN so this is I think a
[1707] the
[1709] the trend now of llm so basically LM is
[1712] not train end to end they are like four
[1714] steps self supervis find tuning uh
[1718] reward um reward model and uh finally um
[1722] um um a reinforcement learning okay so
[1726] so a each step is done in in um
[1729] independently because each step is very
[1730] clear to do it to train and and I think
[1733] you know it's very stable and this is
[1734] exactly the same conclusion that we have
[1736] here uh we can make it very is stable
[1739] and it's efficient everything which is
[1740] stable we have better performance
[1742] usually okay uh and also something
[1745] interesting is that we can we can
[1746] leverage both actually uh proi Tre and
[1749] open source llms so we have the we have
[1752] the best of the of the Two Worlds uh
[1754] it's also of course uh yeah so some
[1757] people will like it it's interpretable
[1759] because you can see the reasoning um you
[1761] know words of the of the
[1765] LM okay so so now let me uh
[1769] let me go to the second um the second
[1772] technique that I want to introduce this
[1773] is called G retriever um and the idea is
[1777] as I told you before is that so llm is
[1780] is very powerful it knows everything um
[1782] but the problem is going to make errors
[1784] because we we we never have a good
[1786] prompt in some sense so we need to
[1789] constrain to regularize you know the llm
[1792] response into um a much smaller space um
[1797] and and and to do that actually we are
[1799] going to use you know a tag text
[1802] attributed graph like a Knowledge Graph
[1805] and it will force the llm basically to
[1807] uh to answer related to this uh to this
[1811] tag okay so the key question is of
[1814] course how do we extract pertinent
[1816] information from you know a graph and uh
[1820] to force the llm to be more
[1822] focused okay so to do that uh we are
[1825] going to use the uh the tokens so I
[1828] think now everybody um understand that
[1831] uh so because of the Transformer
[1833] architecture what is very nice is to
[1835] work everything as an input right so the
[1837] input of your LM can be of course your
[1840] quer token but it can also be other
[1843] information like visual visual tokens
[1846] and also graph tokens so this is what
[1847] we're going to do here we are going to
[1849] use two kinds of uh tokens so the first
[1852] one would be and I I will explain that
[1854] in the in the following slides uh a
[1856] graph encod token uh which is going to
[1859] be here and then a text based token
[1861] which is going to be here okay so the
[1865] graph encoder token this is something
[1867] very natural for example if you do
[1868] molecular science uh you want to
[1871] represent your graph as one vector and
[1873] then you use this one vector to make a
[1874] prediction for the property that you
[1876] want so here we this is the same idea so
[1879] we we can select any favor GNN we apply
[1883] multiple graph learning layers to
[1885] compute a very deep node hidden feature
[1888] you compute then uh the mean uh over the
[1891] nodes and then you apply an MLP a small
[1894] MLP on that so this way you will have um
[1896] a graph enoder token that summarize your
[1900] your your topological graph and also the
[1902] feature on your graph and with one
[1905] vector okay so this is going to be this
[1906] guy of D
[1908] Dimensions uh the other thing of course
[1910] is that an llm um wants to use uh word
[1914] tokens right so um the information the
[1918] process the way it processes information
[1920] is by using word so we need to uh if you
[1923] want to have access to tap you know to
[1925] the knowledge of llms we basically need
[1928] to transform the graph and its feature
[1930] into a sequence of natural uh language
[1934] tokens this is this is important to do
[1936] that and um so for example here you have
[1938] a graph and you can represent this graph
[1942] by um some textual uh representation for
[1946] example a graph G is a set of direct
[1948] edges defined by i j where node i points
[1951] to node J so here the graph J is defined
[1954] with edges um 04 one six and so on okay
[1959] so you have a onetoone mapping between
[1962] this mathematical representation of the
[1964] graph and this um text representation of
[1967] the
[1968] graph however um there are many ways uh
[1972] to use language to represent graph um so
[1977] for for for for example example in this
[1979] paper they they they have this nice
[1981] example to show oh you have you know
[1983] many representation so the text based
[1985] representation of a graph is not unique
[1988] okay so this is this is um this can be
[1991] an issue the other one is also what what
[1993] I say is not text equivalent okay it's
[1996] not text equivalent in the sense that if
[1998] you change you know this guy by this guy
[2001] you will have probably different results
[2003] okay so we want to have some some kind
[2005] of
[2006] equivalance um for for the T
[2008] representation but we we don't have
[2010] it the other thing is a scalability
[2012] issue when you want to represent a graph
[2015] with text okay so if you take an open
[2018] source llm the the context window is
[2021] limited right so for example if if you
[2023] use the one that we use in Academia Lama
[2026] 2 so basically this is 4,000 tokens of
[2029] limitation so if your graph is small no
[2031] problem but if your graph is for example
[2034] the Wikipedia um graph then this is like
[2038] uh a huge number you know of uh of notes
[2041] and huge number of of edges so this is
[2043] not something that you can do there is a
[2045] scalability
[2046] issue of course llms um are prone to
[2050] hallucination uh so for example here we
[2053] we we have an example that you an llm
[2055] can produce uh nodes and edges that do
[2059] not exist actually in the in the
[2062] knowledge graph that we use so in if in
[2064] the in the vocabulary of the graph um
[2067] you know we we have some for example
[2069] here the one de doesn't exist um and is
[2073] able is still you know it's part of the
[2075] vocabulary so the llm can can give you
[2077] actually this uh this uh this entity
[2080] here which which doesn't
[2082] exist so the what we propose is
[2085] basically so first we're going to apply
[2088] um a graph rag that I'm going to explain
[2091] how we do that to retrieve a subgraph
[2094] from um possibly a large uh text
[2097] attribute graph which is going to be
[2099] relevant to the query of the user okay
[2104] um step two we are going to concatenate
[2107] um the user query but also the graph
[2109] encoding token and the text based graph
[2111] tokens to create the input sequence of
[2114] the llm okay then step three the LM will
[2117] give us um will generate an answer step
[2120] four we will U train everything so we
[2122] will simly train the GNN parameters and
[2125] also we fine-tune the llm parameters us
[2128] Laura and the good thing is that you see
[2130] um if you use Laura you're only using
[2133] 0.5% of seven billion parameters so it's
[2136] only 35 million and the GNN has
[2138] something like five million so it's not
[2140] that much actually to train so this is
[2141] something we can do in
[2143] Academia so the graph rag that we propos
[2146] so this is a graph retrieval augmented
[2148] generation so rag is is today very
[2151] popular uh here we want to extend to
[2153] graph the the main problem is of course
[2156] the scalability so I'm going to to tell
[2158] you how we how we solve this problem so
[2161] um yeah let me maybe go here so the
[2164] first thing is to do indexing so what we
[2165] do is that we're going to have um a text
[2168] attributed graph so we're going to take
[2171] um the node uh feature so this is the
[2174] text not feature we have also the edge
[2176] feature the same so we will apply um a
[2179] pre-train and Frozen um large language
[2182] model or or small language model so at
[2185] that time we just use a small language
[2187] model um um but but we can we can use a
[2191] larg model now so you do that and you
[2193] get some D dimensional representation of
[2196] all the nodes and of the edge okay and
[2198] you store them in um in in a database in
[2201] a graph database so so today we are
[2204] lucky there are many open um um graph
[2207] databases that that are that can be used
[2210] so for example P DGL but also Lama um
[2214] index also there is Microsoft and nebula
[2217] graph there are also some propi Tre um
[2220] graph database like Neo 4J okay so we do
[2224] that so we take this and we have Vector
[2226] presentation of the node and the edges
[2228] okay the second thing is that we are
[2229] going to do retrieval so given a query
[2232] uh from the user uh we will represent to
[2235] the query for example what is the name
[2237] of Justin bber brother so we will use
[2239] the same um you know language model to
[2243] represent the query as as we did for the
[2245] node and the edges okay and then what we
[2248] will do is basically we just do a
[2249] similarity metric evaluation so here we
[2253] just use you know cosine metric um and
[2256] we can retrieve this way the top uh key
[2259] um notes and edges from um the the graph
[2263] database okay so we would get something
[2265] like this which is a noisy I would say
[2268] subgraph and then the next step would
[2270] basically to extract um um just you know
[2275] um a smaller uh a small graph which has
[2279] the most relevant information and that's
[2281] it okay so the way we do that we're
[2283] going to solve the price collecting
[2285] Steiner tree okay so the the the price
[2289] collected Shiner tree is basically a
[2291] tree so if you start from this original
[2293] graph and then each node has a price so
[2296] the higher the price the more important
[2298] you want to be in the tree in the final
[2300] tree so you can solve um you know you
[2303] want to maximize the price but also you
[2305] don't want to take everything so you're
[2306] going to have a pin with the cost of the
[2309] solution that you want so usually this
[2311] is you you don't want to or it should be
[2313] minus I'm sorry it should be minus here
[2315] so you you don't want to take too much
[2317] notes so basically this is the number of
[2320] notes that you have here okay so when
[2322] you um when you solve this um comat
[2325] optim optimization problem which is NPR
[2327] but you can have an approximate solution
[2330] um using um semi definite programming
[2332] sdp you will get something like that
[2335] okay so this is directly tree and you
[2337] see that D Tree usually has some kind of
[2339] root node um and he flow out for example
[2343] and and of course he wants to take the
[2344] larger noes okay so this is the original
[2347] Steiner um um Steiner train we can
[2351] modify it because here there was only
[2353] the notes but of course when we do um uh
[2356] um graph learning there is also the edge
[2359] feature that we want to uh to use so we
[2362] can incorporate uh you can easily
[2363] incorporate Edge information okay so we
[2365] have a prize also for the edge so you
[2368] see this is for example an age which is
[2369] more important than this age here um and
[2372] we just you know modify a little bit um
[2375] the combinatorial optimization problem
[2377] here and and we can solve it you know
[2379] using a very fast technique so this is
[2381] very NE um the approximation is near is
[2384] the most linear time
[2386] approximation okay so if we compare the
[2389] standard rag with the graph rag so the
[2392] standard R basically you will have your
[2393] knowledge uh database um and then you
[2396] will extract
[2398] um you know the number of relevant
[2400] document that you want for the graph rag
[2403] here so we have also a graph database
[2406] and we are going to extract um a much
[2409] smaller but very relevant uh graph uh
[2412] related to the query of the user
[2415] okay so now I'm coming back to the
[2418] tokens uh of the input llm so the first
[2420] one again this is the graph and other
[2422] tokens already talk about this uh so
[2424] this is you know an MLP on the mean of
[2428] the the nod
[2430] uh the node hidden feature are the last
[2432] layer of the um of the GNN um and it's
[2437] going to be here so this is something of
[2439] course if you have learnable parameter
[2441] here everything can be uh can be changed
[2443] you know by back
[2445] propagation so for the text base
[2447] basically we would have two um sequence
[2450] of um input words so the first one is
[2452] the cray of the user which is the name
[2454] of Justin Bieber
[2456] brother and the second one would be the
[2458] textualization of the graph okay so this
[2460] is a this is something again that is
[2463] that is important for um to use the to
[2467] tap the llm um
[2470] ability okay so we do that so we have
[2472] the graph representation it would go
[2474] through the text embedder so any llm has
[2477] this first layer that is doing to do the
[2479] the word um embedding okay so here token
[2482] embedding and then um it will go to you
[2485] know the
[2486] llm so the training the training is uh
[2488] is very standard so we give this um
[2491] input tokens we have the Transformer L
[2493] Transformer layers uh and then the
[2496] system the we generate um recursively uh
[2501] the the response um because we know um
[2504] the label using a training set we can
[2507] basically fine-tune um the system to
[2509] give us uh the right answer okay so we
[2512] can uh again we are going to okay
[2515] compute the crossentropy loss uh with
[2517] with respect to the generated answer and
[2520] the the ground truth and then we are
[2522] going to do the backward pass to compute
[2524] the gradient and then update uh the
[2526] parameters of the system so for GNN but
[2528] also for the
[2530] llm okay so in in summary G retriever is
[2534] composed of four steps so we have um
[2536] graph rag uh which are this here which
[2540] is for subgraph retrieval related to the
[2543] query of the users then we have a
[2545] computation of graph tokens using GNN uh
[2549] we have also um uh yes response
[2553] Generations once we we go through uh you
[2556] know the input tokens and also the
[2558] Transformer layers uh and finally model
[2561] training okay so here we try to combine
[2564] um you know the best of all words
[2566] together and I think this is done in a
[2568] very natural way um yeah we have to uh
[2572] change the existing data set and create
[2574] a new uh Benchmark uh to evaluate at
[2578] this um you know this task so doing the
[2581] reasoning of of text attributed graphs
[2584] um yeah so so we have different things
[2587] uh explanation graphs syn graphs and uh
[2590] web
[2591] qsp so the main result are basically
[2594] that um okay here there are there are
[2596] many things but uh you should only focus
[2598] on that so if you do our technique GE
[2600] retrieval basically you will be able to
[2602] beat if you only do llm so you have your
[2605] llm your query and then you get the
[2607] answer
[2608] if you uh if you do only the GNN promp
[2610] tuning so we still do better and if you
[2613] only do the Lura fine tuning llm so we
[2616] still do better okay so this is really
[2618] trying to combine the best of this uh of
[2620] this
[2621] worlds okay so the scalability is
[2624] basically now we are able to uh for
[2626] example only use um you know Reduce by
[2629] 83% and 99% the number of um um you know
[2634] the number of tokens number of notes um
[2637] that that we use so instead of taking
[2639] you know the whole wikkipedia graph we
[2641] will only take you know a very small
[2644] graph subgraph of the Wikipedia um of
[2648] the Wikipedia
[2650] Network yeah of course the one that we
[2652] were interesting is uh does it improve
[2654] hallucination so we compare with the
[2656] Baseline which is just doing llm with
[2659] query uh and we manually so what we did
[2662] is that we um we we we asked you know
[2665] one um we we did one queries and then
[2669] responses and we look at manually uh if
[2673] uh you know there is some missing notes
[2675] or or adding uh you know wrong nodes and
[2678] the same also for the edges and and we
[2680] see that um if you use G retriever you
[2682] really reduce um the the
[2686] hallucination ablation studies so so
[2689] what we observe basically is that um and
[2691] that was very interesting is um so the
[2694] token given by the GNN and and the The
[2697] Tokens The text tokens of the graph they
[2700] actually contribute equally okay so the
[2702] information coming from the GNN and the
[2704] information coming from the text and the
[2706] llm uh of the graph is basic they are
[2709] basically both important okay so they
[2711] are complimentary they really improve
[2713] everything so I think it makes sense of
[2715] course because you have your GNN we know
[2716] that they are pretty good for extracting
[2719] graph information but also the llm has a
[2721] very strong capability uh with you know
[2724] with text uh representation so the two
[2727] are
[2728] complimentary so in conclusion um so if
[2732] we want to unlock the L capity we need
[2734] to use um you know um graph as um uh you
[2739] know represented as as token as words
[2742] but actually combining everything so the
[2744] llm the GNN and the graph rack provide
[2746] Superior performance so it's not only
[2748] the LM capability that does the work is
[2750] actually many other um so graph is
[2754] effective efficient and mitigate an
[2756] hallucinations so here are the paper the
[2758] code and I really invite you to uh read
[2762] the blog post by shaing he so she she
[2765] has done a terrific work here she's the
[2768] main um uh the main um you know um
[2772] researcher in this project and sheeded
[2775] for this actually the 2024 Google
[2777] scholarship so and I really yeah invite
[2780] you to to read a blog post if you want
[2783] to have a high level introduction of of
[2785] this so Al so um yeah so uh the the b b
[2792] geometric team you know they they
[2793] included the the griever so this is very
[2795] nice and I think also something which is
[2797] very interesting um is to look at again
[2800] we always go back to the question um can
[2803] we use GNN to improve products right and
[2805] I think here there is an opportunity so
[2807] if we look at the history of web search
[2811] engines so everything starting with you
[2813] know Google page rank U they didn't use
[2815] any text processing
[2817] then there was word Tove they use word
[2819] Tove then they use language model uh
[2823] they use also rag um and finally we have
[2826] gini okay so gmin is llm plus rag so llm
[2830] um if you don't if they don't know the
[2832] answer they will look at rag uh when
[2835] when you prompt uh gimini so the next
[2837] step hopefully would be to use um GNN
[2841] and um you know some um text attributed
[2844] graph Knowledge Graph that would uh that
[2846] would be used f for web search engine so
[2849] here what is attractive I think is that
[2851] everything is integrated and and
[2853] learnable so this is a you know deep
[2856] learning so the next step of of course
[2859] that we are working um with shaing is
[2862] basically uh okay so we have the text uh
[2865] in um the text feature we have the graph
[2867] feature so the last feature uh you want
[2870] is basically doing the image uh
[2872] introducing the image um information so
[2875] again today everything is a Transformer
[2878] so what you can do is that you can take
[2879] your image you can decompose your image
[2881] into patches and then your patch can be
[2884] represented by um you know just a vector
[2886] so this is a a visual token and then you
[2890] you go through you know uh L Transformer
[2893] layers and you back propagate also to uh
[2896] update the representation of your the
[2898] parameters of your uh of your visual
[2901] Transformer um and that's it so um thank
[2904] you so much
[2906] for um yeah for being there and I I'm
[2909] happy to take any
[2911] question thanks for the awesome talk um
[2915] so if the participants have any
[2917] questions you can type those into chat
[2919] or slack
[2921] um and yeah to perhaps get us started I
[2926] had a question
[2929] um and yeah I I I thought like how how
[2933] you propos to tokenize everything
[2935] essentially and um fine tune with Laura
[2938] these language models is is really
[2940] exciting right like it really unlocks
[2943] multimodality um you you did have a
[2946] slide about graph tokenization right and
[2949] that there's no canonical order so how
[2952] do you deal with that in this work you
[2954] know like how do you kind of decide how
[2957] the graph is tokenized in the
[2962] end are you talking about this
[2964] one yeah like where you where you sh on
[2967] um the talk like a graph slide as well
[2971] right
[2973] um um talk I'm not sure what you mention
[2977] uh right this slide right so is this how
[2979] you kind of textualized the well so
[2984] textualization where is it this one yes
[2987] yeah yeah so textualization is
[2991] arbitrary completely arbitrary so I
[2994] think um Brian perzi you know this nice
[2998] um you know paper and um this is an
[3001] issue right um so it's you want you want
[3005] basically to have as you said a
[3007] canonical representation and there is
[3009] not okay so so what is for the llm that
[3014] you have been trained you know the best
[3016] representation to extract the most
[3018] information so this is this is
[3019] impossible to to to say so um not only
[3024] you don't have a unique representation
[3025] but you still need to have like a the
[3027] representation otherwise you cannot have
[3028] access to the LM knowledge but at the
[3031] same time you you have no idea you know
[3034] if this representation is good or not so
[3036] uh this is like prompt right so there is
[3039] no yeah um no way to know the quality of
[3042] your prompt before before you try so for
[3045] example what we did um I don't know if
[3048] you noticed that but uh for example
[3052] there is a change of performance in the
[3054] prompt if you put the tit to after the
[3059] abstract so so I think all these models
[3062] they have this issue um so the way you
[3064] prompt you're going to have very
[3065] different so here there should be no
[3067] difference right if you put the title
[3068] before uh before the abstract but there
[3071] is a difference so uh you need to play
[3074] and this is you know um I was half
[3077] joking um when when I talk about these
[3080] llms that um you know so they know they
[3083] have seen everything they they are you
[3085] know they have seen all the human
[3087] knowledge um and you can ask them
[3089] anything but if you are not precise if
[3091] you don't know how to ask them the
[3092] question they will never give you a
[3093] right answer so so the only way I think
[3096] to bypass this is is um basically to get
[3100] along with the non-uniqueness of the
[3103] text representation but then to find you
[3105] so before you know Laura I was I was
[3108] quite pessimistic about this technique
[3109] and I said oh it's very hard you know to
[3112] find actually some good representation
[3114] that at the end will be some vectors and
[3115] then you need to align the vectors
[3117] together with the graph uh the graph
[3119] vectors and everything else but you will
[3121] never be able to get something good
[3122] because they have not been trained this
[3124] way but if you do this Laura um you know
[3127] fine tuning then you have a way to align
[3130] this Vector information so it's not
[3132] perfect uh so far it also doesn't make
[3135] sense if you do the um you know at the
[3139] end yeah for example yeah let's go to
[3141] the end so it doesn't make sense in some
[3143] sense in some sense you know to combine
[3145] the visual tokens the graph tokens
[3147] with uh you know the world tokens
[3149] because they are very different
[3150] modalities so what you do with the MLP
[3153] that you put here you're training to
[3155] align you know the the the the visual
[3158] space uh the graph space with the text
[3161] space and then what you do if if here
[3164] this is frozen basically you don't do
[3166] anything you hope for the best you hope
[3168] that in this space you know the
[3170] alignment is good enough to give you
[3172] good Precision so so it's never the case
[3175] I don't think so but um there are so
[3177] much parameters that eventually give you
[3180] something good but now that we can fine
[3182] tune with Laura uh then what you do is
[3185] Bally you force all these spaces to to
[3188] align and and this is why it works
[3190] better when you fine
[3193] tune yeah thanks I mean thanks for all
[3196] the details it's it's always exciting to
[3199] to discuss research this way um
[3204] so do you have time for um one more
[3207] question yeah
[3208] sure yeah so I guess like another thing
[3211] to discuss right would be so if we can
[3214] convince industry of um the potential of
[3217] these approaches and I'm certainly
[3219] excited do you think it's it's possible
[3221] in the future that um we have llms which
[3224] are let's say like more implicitly able
[3227] to handle graph structured data here we
[3230] had to fine tune with with Laura and so
[3233] forth right but do you think like
[3236] there's a possibility to have um graphs
[3239] as one of the pre-training modalities
[3242] yeah yeah this is what the community
[3244] trying to do today right so let me go to
[3246] the slide uh this is exactly what the
[3249] community is trying to do right um it's
[3252] basically can we do some graph
[3254] Foundation
[3255] model um so you would be able to
[3258] pre-train um your your graph in
[3261] different modalities and then you Rec
[3263] combine then with other modalities what
[3265] we do today is that here we are using
[3267] the llm self attention
[3269] layers right so what but what we would
[3271] like to do ultimately is to use some um
[3275] so you train very powerful Foundation
[3278] model for graph Foundation model for
[3279] vision Foundation model for text and
[3282] then you combine them using these um you
[3285] know Transformer layers for different
[3287] task that would be you know I think for
[3289] industry that would be the best way to
[3291] to go uh the problem is that today only
[3294] llms has so much
[3297] um knowledge
[3300] parameters uh you know uh so there is
[3303] very it's very imbalance there is no way
[3305] I think today that we can do a product
[3308] um we can be powerful with GNN only GNN
[3311] today is just a top cherry on the top in
[3314] some sense so in so it's not like you
[3317] know we are missing um data training
[3320] data so the web is full of uh you know
[3323] uh graph structure data is full of that
[3326] there there is no issue with that the
[3328] question is how do you make a product
[3331] that would you know uh excite uh
[3334] industry like you know meta Google and
[3338] so on uh that would tomorrow say okay
[3340] let's do like chpt but let's do this for
[3343] graph so I think you know because it's
[3345] not clear and also I have this you know
[3347] there was a redit at some point someone
[3349] was saying you know why isn't GNN in
[3352] Hyman industry so that was a very
[3354] interesting I think um uh uh you know
[3357] discussion um so the only today industry
[3361] that likees GNN is
[3364] biology right so because you cannot do
[3367] today llm for biology so uh the only one
[3371] that can make money of that is is
[3373] basically biology and and so we have the
[3376] Nobel price um so there is a huge
[3380] promise that this deep learning graph no
[3383] network and so on um can make money uh
[3386] of course it's it's a promise it's not
[3389] yet there but I think this is today
[3392] where the money is for for GNN but of
[3395] course you would like to do it also for
[3397] you know for text there is no reason we
[3398] cannot do that but as long as we don't
[3401] have like industry I mean we we need to
[3403] be um you know honest with ourselves so
[3406] industry drives uh you know the AI the
[3409] big AI um you know Improvement like like
[3412] GPT right so GPT could never be at
[3414] develop uh you know in in Academia
[3417] so of course Academia is very important
[3419] to get the ideas you know like for
[3420] example diffusion models have been
[3422] developed by a PhD student in Germany
[3424] and so on so ideas we come from Academia
[3428] but um you know scanning up and making
[3431] um a so social change would come from
[3434] industry so it's a yes it's it's part of
[3437] the pipeline if we if we are not able to
[3439] convince people to use GNN for you know
[3442] text um so either GNN is not good enough
[3447] or we are not doing a good work you know
[3448] to find the the right uh
[3451] product yeah nice yeah I think I think
[3455] this work is uh is definitely going in
[3458] that direction right um there's there's
[3462] question yeah there's a question from
[3465] the audience um so the questions as
[3467] follows for graph rag could it be
[3469] possible that retriev nodes and edges
[3471] are mutually exclusive and don't
[3474] actually form connected subgraphs
[3477] if so is there methodology to ensure
[3479] that the retri subgraph is
[3482] connected yeah so this this is a very
[3484] good question so I think this is
[3485] completely arbitrary again so um
[3487] depending on the task you you want to um
[3490] you know you want to solve so sometimes
[3492] maybe you want directed uh you know
[3495] subgraph you want
[3496] undirected uh there are many ways to
[3499] retrieve you know subgraph so uh you
[3502] know minimum spaning Tre is the simplest
[3504] one but they don't have any uh you know
[3507] um um in some sense the the size of the
[3511] the output size cannot be controlled
[3512] this is the number of nodes so here we
[3514] want something you know with less so I
[3516] would say everything is possible as long
[3518] as you know the task that you want to
[3521] optimize um so here we use this one but
[3524] again it you know that was for us that
[3527] was directed so that was for us and we
[3529] also wanted to have like a small size so
[3532] we can quickly you know do that so we we
[3534] wanted something better than the min
[3536] spanning tree so this is why we used
[3538] Steiner tree um which is standard but
[3542] again I think you can use different you
[3544] know subg graphic traction um that is
[3548] going to fit um your your objective
[3551] there there is no problem with that um
[3553] it just you know you need a process to
[3555] extract a subgraph that's very important
[3557] and this process has to be linear time
[3559] because if you if you do that on you
[3561] know on on large graph I mean at the end
[3565] again we are talking about product you
[3566] want to do it you know on the fly so you
[3569] want something very very fast that's I
[3571] think the only condition so uh of course
[3573] a linear um approximation uh a linear
[3577] time approximation is never as precise
[3580] but if you take enough you know notes
[3582] and ages it should be good enough I
[3584] think for your
[3587] application yeah that makes sense thanks
[3589] for all the detailed answers um and yeah
[3593] thanks for the wonderful talk um I think
[3596] it's it's really exciting and you know
[3598] like how all these Technologies come
[3600] together and with graph rag with graph
[3603] Vector databases I think we're we're on
[3606] the cusp of hopefully the kinds of
[3608] breakthroughs you talked about
[3611] um right thanks for the talk sure thank
[3615] you very
