---
schema_version: 1
id: yt-6PF25foNpf8
type: youtube
title: Subramoney (event-based architectures) - Schrimpf (brain-score)
url: https://www.youtube.com/watch?v=6PF25foNpf8
authors:
- Neural Reckoning
ingested_at: '2026-06-01T19:55:46Z'
content_hash: sha256:5401431f16903520a5c878ca4de441c8de54691b2092973f3def7bb82145d8ef
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neural Reckoning
  channel_url: https://www.youtube.com/@neuralreckoning
  duration_seconds: 4145
  caption_track: fetched
  snippet_count: 1858
filter:
  score: 0.7
---
[0] welcome everyone back to the Smitha
[2] seminars
[3] um today we're going to hear two talks
[5] um one from Anand and one from Martin uh
[8] both talks will be about 20 minutes long
[10] and then there'll be time for questions
[11] and discussion afterwards
[14] um just the usual Zoom things so please
[17] keep yourself muted during the talks but
[19] feel free to post questions in the chat
[21] and uh yeah we're recording the session
[23] and it will be available to view on
[25] YouTube afterwards
[27] uh yeah so with that I'd like to
[30] introduce Anand uh announce did a
[32] masters in computer science and then did
[34] some work in Industry before doing his
[37] PhD on biologically plausible learning
[39] rules and meta learning in spiking
[41] neural networks with Wolfgang Mars
[44] and then for the last few years he's
[46] been working as a postdoc in Germany and
[49] yeah I'll leave him to tell you about
[51] his work today
[53] thanks Marcus
[55] yeah hi everyone uh like Marcus I'm a
[59] post talk at lower University bookmark
[61] in Germany I'm part of this institute
[63] called Institute for neural computation
[65] uh the group of Lawrence wiscott and
[69] today I'm going to be talking about a
[71] general purpose event-based
[72] architectures for deep learning
[76] so
[77] so uh my kind of proposition here is
[81] that uh we need to look Beyond biology
[83] based models for deep learning
[85] especially on neuromorphic Hardware
[87] uh so spiking neural networks uh that we
[90] all know and love were developed as
[92] models of biological neurons but uh I
[95] mean they have become the canonical
[96] model for neuromorphic computing
[98] especially for doing deep learning
[100] applications uh and the focus of
[103] neuromorphic devices is Shifting further
[105] towards deep learning uh because of
[107] their Energy Efficiency advantages and
[109] with deep learning you have higher
[111] expectations of task performance
[114] so I think we need to ask ourselves are
[116] these biologically inspired spiking net
[118] neural networks really optimal for deep
[120] learning with metamorphic devices
[123] and what I propose is that we need to
[127] design deep learning architectures up
[128] initial for deep learning on
[130] neuromorphic devices because
[133] we can distill the essential advantages
[135] properties of these biological models
[138] and we can really customize
[139] architectures for specific deep learning
[142] specific neuromorphic Hardware we can
[145] design these architectures to achieve
[148] exactly what we need in terms of longer
[150] memory or better stability properties
[153] gradient properties and so on and we
[156] don't really need to be beholden to
[158] biological models if you are just
[161] focusing on the Deep learning part right
[164] so then the obvious question that arises
[167] is what are the key properties of
[169] spiking neural networks uh and what is
[172] the decided data for neuromorphic
[174] architecture so why are spiking neural
[176] networks so popular for the atmosphere
[178] Hardware
[179] um so I mean so as we all know
[182] neuromorphic Hardware is focused on
[185] Energy Efficiency and there are some
[187] properties from biological neural neural
[190] networks and from spiking neural
[192] networks that actually lead to this
[193] Energy Efficiency so one of them is
[195] sparsity uh both in time and in space uh
[200] so the sparsity in time is activity
[201] sparsity where activity of the units are
[204] transmitted only when needed so
[206] inspecting neural networks these are the
[207] binary spikes that are sent to other
[209] units and then there is parameter
[211] sparsity where you just have fewer
[213] connections uh each unit is only
[216] connected to a few other units in the
[218] network and not all the other units so
[220] uh activity is really only transmitted
[222] to units that need them
[224] so the second main property that has
[227] been used a lot in neuromorphic Hardware
[229] is even based communication
[231] right and this is communication that
[233] happens only through discrete events
[235] sending messages between units so you're
[237] not sending uh you're not communicating
[240] all the time like you do with a
[241] traditional Network
[242] uh but uh you're only sending like
[245] discrete events and uh so when you
[248] combine this with activities parsitting
[249] units only need to update their state on
[252] an incoming event uh and in between
[254] depending upon the Dynamics that you
[256] choose uh we don't really need to do
[258] anything at all
[260] so there are other properties uh such as
[262] asynchrony where you don't really have a
[264] shared clock signal across the units
[267] and maybe a few others that have not
[269] thought of uh that uh spiking neural
[273] networks have so uh so I should say that
[275] event-based communication also
[276] implicitly implies Computing with time
[279] so you should uh so that is already a
[282] property that's included over here
[285] okay so what can we do so now that we
[288] know uh or at least we think you know
[290] what the uh property of spiking uh
[293] neural networks are important uh we can
[296] think about uh designing general purpose
[298] event-based models and uh this is a
[302] principle very very straightforward all
[303] you have to do is add an event
[304] generating mechanism to each unit and
[306] whatever model you have and the unit
[309] Dynamics can be arbitrary
[311] right so you could take something that
[313] looks like this uh so for a live leaky
[316] integrate and fire neuron or something
[319] with an Adaptive threshold or with
[321] exponential integrated file uh so all of
[324] these standard spiking neural network
[326] models uh you have an internal State uh
[328] which is the membrane potential I mean
[330] here I'm calling it C for reasons that
[332] you will see
[334] soon and so the idea is that you have
[337] some Dynamics you have some internal
[339] State and then you have this event
[340] generating mechanism uh based on a
[343] threshold and then whenever the event is
[346] sent the state is reset
[348] and there is a recurrence in this within
[351] this unit so that you can really use
[355] information over time
[358] so this is kind of like the general
[359] principle so you could quite just as
[363] easily use a lstm or a GRE unit over
[365] here instead of leaky David and fire
[367] Dynamics because you could just add a
[369] threshold on the uh cell state of the
[373] gru or lstm right and over there the
[377] internal state is just the entire state
[378] of Dynamics you could also use any other
[382] dynamics that you wanted to so uh so
[386] what I do now is take this General
[387] principle and apply it to one particular
[390] example a gated recurrent unit and as I
[393] go along I'll tell you why uh which
[395] shows they get a recurrent unit because
[396] it has some very very interesting
[398] properties otherwise as well
[400] but the first thing to do is uh to kind
[403] of look at the Dynamics of the Gated
[404] recurrent unit uh this is what it looks
[407] like it has an update gate uh which is a
[409] gate that's a function of the external
[411] input X and the recurrent State Y and
[414] then you have a reset gate which is also
[417] another gate that's with different
[419] parameters that's a function of X and Y
[422] that you have a proposed update set
[424] and the output of this gated recurrent
[427] unit is some combination of this
[429] proposed update said and the previous
[433] time step State y right uh so you both U
[438] and R are values between 0 and 1 and the
[440] function as Gates as they do when
[443] you know lstm as well uh so because the
[446] sigmoid you always have values between 0
[448] and 1.
[449] okay so what we want to do now is to use
[452] this principle that I described before
[454] and just add an event generating
[456] mechanism to the gru
[458] so uh I write the cell State now as this
[463] combination of the proposed update and
[465] the cell State and add a reset to the
[468] cell State and introduce a heavy side
[471] step function with the threshold so the
[473] idea is that whenever the cell State
[475] reaches the value of the threshold it
[477] sends the value of the cell state to all
[479] the other units so that is the output of
[481] the event based Gru or egru as we call
[485] it
[486] and the cell state is exactly the same
[488] as uh what we had before over here but
[492] with the addition of a reset mechanism
[493] so every time an event is sent the cell
[496] state is reset and then it starts
[497] integrating input again
[500] so this is kind of what our uh egru
[504] looks like
[505] um and it's really as simple as that
[508] right so now each unit is only sending
[510] uh discrete messages whenever the cell
[513] State crosses the threshold
[515] and when the cell state is below this
[518] threshold then the output of the unit is
[521] zero so there's nothing being said at
[523] all
[524] and so this very obviously uh leads to
[526] activities sparsity of the network
[530] so how do we do learning so now that we
[532] introduced uh heavy side step function
[535] which is not differentiable it looks
[537] like you continue to back propagation
[538] Through Time
[540] but uh we do know a lot of tricks uh
[542] about how to handle this from the
[545] spiking neural network literature and
[547] what we can do is introduce a pseudo
[550] derivative or a surrogate gradient for
[552] this thresholding function uh so I mean
[556] I show like the particular function that
[558] we use but so what is really cool about
[561] this model is that uh and this is also
[564] true for spiking neural networks uh
[566] which is that if there is activity
[567] sparsity in the forward pass so if only
[570] these white units are activated as you
[572] go forward in time
[574] uh in the backward pass you get sparsity
[577] as well
[578] because you only need to propagate the
[580] gradients through the units that are
[581] active uh of course I mean when you use
[583] a pseudo derivative uh with
[586] um some support that looks like this you
[589] would have to propagate gradients
[590] through all the units that had a cell
[592] State between plus or minus Epsilon of
[595] the threshold
[596] uh but you don't really need to
[599] propagate the gradients through the rest
[600] of the errors right so you can choose
[603] and appropriate pseudo derivative and
[604] make the backward pass pass as well
[606] and uh beyond the support of the pseudo
[608] derivative all the gradients are zero so
[610] they're not packed up again
[612] so
[613] um so which means that uh the activity
[616] sparsity the forward pass
[618] can translate into efficient backward
[621] pass training as well in this model
[622] which is a really cool property
[625] that we can use
[629] um
[629] so so this is like the basic model and
[633] we tried this on a bunch of uh tasks uh
[636] so deep learning benchmarks uh
[638] benchmarks that come from spiking neural
[640] network literature as well the first one
[642] we did was uh this DBS 128 GSA
[645] recognition so DBS so this this is like
[648] data that's based on uh hand gestures
[650] collected by this Dynamic Mission sensor
[652] camera in terms of events
[655] so so each sample is a stream of events
[658] a stream of offer on events uh spread
[661] out over time and this describes the
[664] moment of M right so this is work done
[666] by one of my colleagues
[667] and uh so here's like a table of results
[671] and so the first thing to look at is uh
[674] so the standard lstm based models uh so
[678] without a convolutional layer in front
[680] achieve about 86 percent accuracy and
[683] with a convolutional layer in front with
[685] the LX net achieve about
[687] 97.7 or so percent accuracy
[691] and uh so our model can actually quite
[694] easily compete with that so we have a
[696] version so da over here stands for data
[700] augmentation so it's trained with
[702] additional data augmentation as well so
[704] both the state of the art model as well
[706] as some of ours and so our model can
[709] easily kind of beat that and get 97.8
[711] percent accuracy uh with the CNN and
[715] data augmentation and without it gets
[717] about this it beats this and gets about
[720] 90 percent
[721] but now what is important is to look at
[723] the uh not just the number of parameters
[726] but because we are talking about
[727] activity sparsity we want to really have
[730] an estimate of how much computation that
[732] we how much computation we perform at
[734] the forward bus right so over here
[736] there's this entire column of activities
[737] per City and you see that most of the
[740] egru models achieve about 80 percent
[742] activities parsitting and we want a good
[745] estimate of how this translates into the
[747] amount of computation that's performed
[749] uh so what we can do is we can calculate
[752] the effective multiply accumulate
[753] operations that are done in the forward
[755] pass and this takes into account the
[757] activities positive because whenever a
[760] unit is zero you just don't do enough
[762] you don't you don't have to do any
[763] operation for that unit when you
[764] propagate uh to the next time step
[768] uh so
[769] with the egru model you can really see
[772] that we can get very very efficient
[775] models so uh for the case without the
[778] CNN and augmentation we basically are
[782] about half the state of the art in terms
[785] of computation but getting comparable
[787] accuracy and for the case with the
[790] convolutional neural network and this is
[792] kind of interesting because uh
[793] convolutional neural networks are quite
[795] computationally expensive so this model
[797] for example has like 600 million
[799] effective Mac operations for the forward
[802] bus and we are able to solve the same
[805] task with a much smaller convolutional
[808] layer and a recurrent egru with
[812] activities Varsity of 80 percent
[814] and achieve the same amount of
[816] performance right so this is almost an
[817] order of magnitude uh reduction in the
[820] amount of Mac operations over here
[823] so
[824] um if you and and so there is also
[826] backward sparsity that is quite
[827] significant so the training is also
[829] efficient
[830] um and if you look at the activity of
[832] the network it's very reminiscent of
[834] what you see with Spike in data networks
[835] which is uh that most of the units are
[838] not active most of the time
[840] uh and as you go uh from layer to layer
[843] the activity increases but uh you just
[845] have like overall a lot of Spar sitting
[848] okay so the uh second task that we tried
[851] on was the sequential feminist image
[854] classification task so this is one of
[856] the tasks where you take an MS digit and
[858] give input pixel by pixel uh scanning
[861] from left to right and top to down in
[863] the image
[864] and over here uh well I mean we don't we
[867] don't achieve we don't beat the state of
[869] the art yet uh but uh we do get really
[871] really efficient models that have
[873] comparable performance so uh in just
[876] sequential amnest uh we have a model
[877] that gets uh 98.3 percent but with about
[882] like uh slightly fewer parameters in the
[885] state of the art uh permuted sequence
[887] laminates which is a much harder problem
[889] uh again we get like fewer uh operations
[893] uh and somewhat close to the state of
[896] the art performance right so it
[897] basically works well
[900] um but so what we did with this uh
[903] sequential mnist was also look at how
[905] the model scales uh in terms of the size
[908] of the uh Network so in terms of the
[911] number of units in the network
[913] and uh so here is a plot uh which which
[917] shows uh what happens when you do this
[919] on the left side uh y-axis the orange
[922] curve is the number of operations
[925] uh on the right side is the number of
[927] epochs that it took to converge uh to
[930] some value of accuracy and the x-axis is
[933] the size of the network
[934] so what is interesting is uh you see
[937] that as you increase the size of the
[939] network for the same task the network
[941] converges faster so this is not quite
[943] unexpected right this is actually what
[946] you would expect to see and as you
[947] increase maybe uh uh it stops converging
[951] but we just run it up to 2000 units
[955] but uh the number of operations uh
[958] calculated in terms of these Mac
[960] operations stays almost the same uh even
[963] as you increase the size of the network
[966] more than 20 times right so we've got
[969] close to 20 times
[971] um so this is quite interesting because
[972] uh you can actually over parameterize
[975] models
[976] and get like better training properties
[979] uh without doing significantly more
[982] computation
[986] so uh and then uh the other like really
[990] uh interesting uh application that we
[993] tried this on was language modeling and
[995] uh so this is uh one of these uh tasks I
[999] mean language modeling is where uh
[1002] models really seem to benefit from
[1004] having really large sizes as we see a
[1006] lot of deep learning today so we wanted
[1008] to see how our model performs in
[1010] comparison uh but mostly compared with a
[1013] set of the art recurrent models so we
[1016] we're still not required models are
[1018] still not like close to Transformers but
[1021] it does get really really close to the
[1024] uh performance of lstm based
[1027] state-of-the-art models so these are
[1029] like essentially on the so I mean the
[1031] measure of performance over here is
[1032] perplexity so Rover is better so
[1035] inventory bank which is a relatively
[1036] small data set we are basically able to
[1039] get a perplexity that's close to the
[1042] state-of-the-art models uh but with a
[1045] fraction of the parameter a fraction of
[1047] the computation required right and
[1049] similarly for Wiki text 2 which is an
[1051] even larger data set again with about
[1053] half the amount of computation required
[1055] we are able to get quite close to uh
[1058] the
[1059] performance and I should I should say
[1061] here that a lot of the bottleneck of
[1063] getting good performance as it is often
[1066] the case in deep learning is uh just the
[1068] amount of time spent and optimizing the
[1071] hyper parameters
[1073] and so this was a case where we did
[1076] some hyper parameter tuning based on the
[1078] computational resources we had and we're
[1080] still able to get quite close to STM
[1082] based architectures so the second caveat
[1084] over here is uh Gru models by themselves
[1087] are not they have a bit of a slight
[1089] disadvantage compared to lstm models so
[1093] just like the base and GRE model does
[1095] worse than the lstm based models uh but
[1098] uh we are working on having an
[1101] event-based version of the lstms value
[1102] currently
[1104] so um so the other interesting property
[1106] that we can see from these language
[1108] modeling experiments is that you can
[1109] actually trade off the backwards
[1111] sparsity with the performance that it
[1113] requires so you can use this surrogate
[1116] gradient into parameter Epsilon so this
[1118] is essentially the support of the
[1120] surrogate gradient and uh so the wider
[1123] you make it the lower the backwards Part
[1124] City uh and then but but there is kind
[1128] of like a bit of a trade-off so as you
[1130] can see with some level of backwards
[1132] sparsity nodes and 20 you get like the
[1135] best uh what looks like the best
[1137] performance over here on average at
[1140] least and you can kind of make the
[1142] circle gradient narrower and narrower
[1144] and still have
[1145] uh uh fairly decent performance right
[1150] so depending upon the resources that you
[1151] have for training you can really trade
[1153] this off
[1154] okay
[1155] so uh so the other uh so the reason that
[1158] we chose the gru for the first
[1160] um kind of model event-based model was
[1163] that they have a very interesting
[1165] property which is that the GRE model
[1167] itself can be written as continuous time
[1170] uh equations quite elegantly so the GRE
[1173] equations are just I mean if you just
[1175] quintet them a bit you'll see that they
[1177] are essentially forward either equations
[1179] of some continuous time model and you
[1182] can just write it as a continuous time
[1183] model directly without
[1186] uh much uh difficulty right and uh so so
[1192] you basically uh did this uh to analyze
[1195] uh what our event-based model could do
[1198] uh and for this uh you essentially take
[1201] the uh Gru continuous time model and
[1205] make it even based in the same way so uh
[1208] except that now we can really
[1210] mathematically uh Define things more
[1212] formally and analyze uh exactly what
[1216] sort of properties this model has so
[1219] um so we essentially defined all the
[1222] gates just like in the discrete time GRE
[1224] model we added an activation Dynamics
[1228] which is essentially a variable that
[1229] integrates the inputs coming into each
[1232] unit
[1233] uh and uh this is the continuous time
[1236] dynamics of the cell State uh and this
[1238] essentially looks very similar to the
[1239] discrete term equations that we're
[1240] looking at before
[1242] and you can also mathematically uh more
[1245] rigorously Define uh the concept of uh
[1248] emitting an event
[1250] um so whenever the cell state of the
[1253] unit emitting the event reaches a
[1256] threshold then the unit cell state is
[1259] reset to zero uh and uh the other units
[1263] don't really change their cell state but
[1266] uh all the other units receive an input
[1268] to their activations uh based on the
[1271] cell state of the unit sending the spike
[1274] right so this is kind of I mean I don't
[1276] want to kind of go too much into detail
[1278] here but uh you essentially end up with
[1280] like very very simple equations that
[1282] describe what emitting the unit means
[1285] and you can handle the input in the same
[1287] way
[1288] so
[1289] uh what is now interesting about
[1291] defining the model in this way is that
[1294] you can also do a backward pass in
[1297] Cutters time based on the adjoint method
[1300] so you write the laws using some adjoint
[1302] variables and the Dynamics of this
[1304] continuous time model and you end up
[1306] getting joint Dynamics which is
[1308] essentially like the equivalent of the
[1309] backward pass for the discrete time
[1311] model that also look fairly simple so I
[1315] mean maybe the
[1317] derivative of the F with respect to C
[1320] looks like it's going to be a whole
[1321] Matrix but it's actually just it's just
[1323] ends up being a vector so the center uh
[1326] Matrix transpose multiplied by the
[1328] adjoint variable ends up being just a
[1330] vector so all of these Dynamics are on a
[1333] per unit basis you don't really have to
[1335] consider interactions between units and
[1338] you can calculate the gradient updates
[1341] for the parameters of the network based
[1345] only on quantities uh at the time of the
[1348] events
[1349] right and this is a very very cool and
[1351] interesting property uh so in spiking
[1354] neural networks this was kind of uh
[1357] called event prop uh which is published
[1359] some time ago and the same property
[1362] holds for these kind of General models
[1364] as well because as you see the Dynamics
[1366] of the model is defined quite generally
[1369] as if
[1370] um and so what this means is that uh you
[1374] only really need to back propagate uh
[1377] the cross-unit back propagation
[1378] communication is also even based so you
[1381] only need to do that at the times of the
[1383] events and only within the unit you need
[1385] to do some sort of uh backward pass uh
[1388] in between the events right uh so which
[1391] is which can really make trading super
[1393] efficient
[1395] okay so
[1397] um that's uh so you can actually uh look
[1399] at our uh archive paper that I linked to
[1402] before but I'll link again uh for more
[1404] details about this uh but uh this kind
[1408] of uh model uh essentially uh I mean to
[1411] summarize summarize this uh talk
[1415] um biologically possible spiking around
[1417] Dynamics they are sub-optimal for deep
[1419] learning on neuromorphic Hardware
[1421] uh so you can modify the unit Dynamics
[1423] to make it spiking by adding an event
[1426] generating thresholding function
[1429] so and we Define this based on gated
[1432] recurrent unit or Gru and so what is
[1435] interesting is that uh it exhibits High
[1438] activities sparsity in the forward pass
[1440] but it also exhibits uh sparsity in the
[1443] backward bus so in learning right so
[1445] this is true for both the discrete time
[1446] model where disparity is not exactly the
[1450] same as the forward sparsity because of
[1451] the surrogate gradient that we Define uh
[1455] but uh for the continuous time model
[1457] this sparsity in the backward pass is
[1459] exactly the same as the forward pass and
[1461] uh it which has the potential to be
[1463] super efficient
[1465] so uh because we do get the event-based
[1468] gradient descent updates and uh we can
[1470] analyze it mathematically so for example
[1472] you could really Define the Dynamics of
[1474] the units based on stability conditions
[1477] based on avoiding uh Vanishing gradient
[1480] or exploiting gradient problems you
[1482] could Define it based on modeling long
[1484] term dependencies and then still get
[1486] this kind of event based updates
[1489] for such a network
[1491] and so you could really have very very
[1493] powerful uh architectures that come out
[1496] of this
[1497] and so
[1500] well I mean I would uh argue that um
[1503] this kind of more general purpose models
[1506] can potentially replace spiking neural
[1508] networks for challenging and complex
[1509] tasks such as language modeling but
[1511] basically like almost a lot of other
[1514] deep learning applications
[1516] all right so uh in terms of Outlook
[1519] um
[1519] I mean what uh me and my group are
[1523] planning to do are explore like other
[1526] unit Dynamics for different use cases
[1530] uh but also really look at uh which sort
[1534] of Dynamics are good for specific
[1535] neuromorphic devices so there are
[1537] metamorphic devices which support
[1539] non-binary packets for communication uh
[1542] we're working on more efficient software
[1543] implementations of these models and we
[1545] are actually working quite closely with
[1547] uh Tu Dresden in Germany uh who
[1550] developed the Spinnaker 2 Hardware uh to
[1553] have an implementation of one of these
[1555] models there and hopefully scale it up
[1556] to way more parameters anyways
[1558] so I should say this was a joint so the
[1561] egru was trying to work with a bunch of
[1563] people so Khalil Mark and Christian from
[1566] utreston and David from University boom
[1570] and I've linked my our uh Archive
[1574] preprint of this GRE based event-based
[1577] models uh over here so thank you very
[1580] much I'll take questions
[1584] thanks so much that was a really clear
[1587] talk and super interesting
[1590] um so yeah I just had one quick question
[1591] I guess and then anyone else can ask
[1593] away
[1595] um so I was wondering and have you so
[1596] you showed good performance on lots of
[1599] different types of tasks but do you
[1601] think there's a sort of class of tasks
[1602] or particular types of tasks that this
[1605] architecture would really excel at
[1607] compared to other types of tasks
[1612] so we have mostly focused on like
[1614] recurrent architectures but as far as we
[1617] have seen uh anything that uh lstm or a
[1621] GRU can do our architecture works well
[1623] for that as well
[1625] uh so it's I mean and in principle you
[1628] could do the same thing for feed forward
[1629] networks as well right I mean the
[1630] benefits are not as great for a feed
[1632] forward Network
[1634] um but uh yeah I mean I don't really see
[1636] a limitation in terms of the type of
[1638] tasks
[1640] okay cool well yeah with that happy if
[1644] anyone else to ask questions man
[1648] yes hey can you hear me yeah I can leave
[1652] hey sorry I had a just a little
[1654] confusion maybe technical bit when you
[1657] talked about the the amount of sparsity
[1659] in the back prop phase compared to that
[1662] excellent parameter and I think I didn't
[1665] really understand how this relation
[1667] worked because in my head it would have
[1668] been the other way the more the narrower
[1671] function you would have used uh the more
[1674] sparse you would get as a return right I
[1677] don't really understand how this
[1679] relation is the other way or maybe it's
[1681] just confusion on my side uh no it is
[1684] actually uh what you said so over here
[1686] you can kind of see that so not over the
[1688] circuit function the higher the
[1690] backwards possible
[1692] you mean the less event you get that you
[1695] need to appropriate through right
[1697] exactly okay okay yeah my bad yeah okay
[1700] cool
[1714] I guess the other quick question I had
[1716] was you showed at some point I figured
[1718] with the oh sorry there's a question in
[1720] the chat as well
[1721] um let me just ask this quickly and you
[1724] try to figure at some point with uh the
[1726] spiking in a few layers could you just
[1728] show that again quickly oh yeah
[1731] so is it the
[1734] so is the top layer is the top uh
[1737] subplot here is that the first layer in
[1739] the network or is that the is that the
[1741] input layer is that the yeah that's the
[1743] input here exactly okay oh so then then
[1746] it is like so then it is actually a bit
[1748] different to spiky neural networks right
[1749] because spiking neural networks we tend
[1752] to see more sparsity as we go through
[1754] the layers you tend to get more sparse
[1756] activity deeper layers
[1758] um this is kind of the opposite right
[1759] you get more activity and deeper layers
[1761] I mean we kind of well uh what we found
[1764] was that this is like really task
[1765] dependent okay so it depends on like how
[1768] the input is encoded so there were cases
[1770] where uh if you use like a different
[1772] input encoding then you don't really get
[1773] much sparsity in the initial layers but
[1776] then you get more the final layers so
[1778] this kind of varies a lot there's at
[1780] least like as far as I know there was no
[1781] hard and fast rule that we noticed
[1785] yeah I mean with Biology or anything
[1788] else I guess I wouldn't want to say a
[1790] fast rule I think usually becomes faster
[1793] and deeper layers in spiking networks
[1796] um but maybe that's not true yeah that's
[1798] a very interesting point I guess uh I
[1800] mean so in some sense like these models
[1802] are uh really like
[1804] um kind of equivalent to complex neuron
[1806] models right so uh it would be quite
[1808] interesting to study this emergence of
[1810] sparsity and how it correlates with
[1812] Biology
[1813] yeah I guess I said maybe Martin later
[1816] can talk well maybe not but maybe he can
[1819] talk about how activity changes as deep
[1822] layers in the visual processing
[1824] anyway so there's some questions which I
[1827] can read out uh so Laura fandel asked um
[1830] hi thanks for the great talk would egru
[1833] be applicable to time series problems
[1835] like detecting movements with EMG or EEG
[1838] like signals
[1840] but yeah absolutely so
[1842] um I mean anything you can use a
[1844] recurrent Network for you can use the
[1845] hru but with the sparsity benefits
[1848] uh so you don't necessarily need to
[1850] encode your input in terms of events so
[1853] if you do then you would get like an
[1854] additional Advantage but you could just
[1856] like for a language modeling for example
[1858] we just use a very fairly standard
[1860] encoding just like you would do for
[1862] lstms and then uh since we don't we're
[1865] not forced to work with binary
[1867] communication like with spiking networks
[1870] uh we can just like pass in a vector of
[1873] like any real value of numbers right
[1877] cool and uh Colin will ask um if the
[1881] Paradigm in neuromorphic engineering
[1883] moves towards the event-based
[1885] architectures you described and away
[1887] from spiking neural networks would that
[1889] represent a shift away from or towards
[1891] neural networks that mimic
[1894] um directly the animal brain
[1896] yeah that's a very interesting question
[1898] so actually first of all a lot of the
[1901] existing neuromorphic architectures
[1902] already support more general purpose
[1904] models so the intelohy or already
[1908] supports what they call graded spikes
[1910] which is you know just sending like
[1912] non-binary values across uh Spinnaker
[1915] architectures support like arbitrary
[1916] Dynamics it's just that people have been
[1918] using uh spiking neural network Dynamics
[1921] uh all this time because that's what
[1923] they were focusing on
[1925] um so uh but there are of course like
[1928] analog Geographic Hardware which have
[1930] like built-in uh leaky integrated file
[1933] Dynamics or some other specific Dynamics
[1935] and this is not something that can be
[1936] easily changed so I guess it's already a
[1938] mix of things
[1940] um so the question about whether uh it
[1942] gets closer or a way further away from
[1945] animal brain I think that's a very
[1946] interesting question because uh like I
[1949] said you could really do do very similar
[1952] thing for more complex neuron models so
[1954] you could really try to model biology by
[1956] you know writing a multi-compartment
[1959] model with like much more complex
[1961] Dynamics within this framework and try
[1963] to train them uh instead of using like
[1965] Point neuron models
[1967] and then in that sense it would actually
[1970] become closer to animal brain Dynamics
[1973] with all the complexity right I mean of
[1974] course it's a separate question whether
[1975] adding this complexity helps or hinders
[1978] understanding biology
[1980] uh but uh you could you could easily do
[1982] that so this is these are I think like
[1984] two orthogonal things uh it's not really
[1986] going away from uh biology necessarily
[1992] well thanks for answering those
[1994] questions and I think uh as Martin
[1996] commented in the chat but kind of takes
[1998] us quite nicely into Martin's talk
[2000] um yeah on whether or not different uh
[2003] modeling choices take us closer to uh
[2006] neural activity so yeah thanks Alan and
[2009] uh yeah it's your head you could uh yeah
[2012] yeah you could share your screen Maybe
[2017] uh cool and with that I'll introduce our
[2019] second speaker Martin
[2022] um so like Anand Martin studied computer
[2025] science and then did some work in
[2027] industry
[2028] um after that he did a PhD at MIT with
[2031] Jim to Carlo and really excitingly he's
[2035] recently been appointed as a professor
[2036] at epfl
[2038] yeah we're really excited to have Martin
[2040] here today
[2042] um because of his work on brand school
[2043] which I hope he'll talk about and yeah
[2047] that's something which has come up in a
[2048] lot of these seminars and yeah it came
[2051] up just now so yeah Martin thanks
[2056] cool thank you very much for having me
[2058] uh this is exciting um I I will try to I
[2062] think mostly talk about brain score I'll
[2064] also try to talk a bit about the
[2065] rationale behind some of the choices we
[2067] made uh and I hope there's especially
[2069] with the spiking Community I hope
[2071] there's going to be some question about
[2072] what level level abstraction we might
[2075] want to focus on
[2076] uh as a spoiler I'll try to put forth a
[2079] view of uh Spike rates but hopefully we
[2081] can have a discussion and maybe I can
[2083] convince me always
[2085] okay uh so I wanna
[2087] preemptively so much has said this uh I
[2090] am incoming faculty pfl so if anything
[2093] that I'm going to talk about sounds
[2094] exciting to you and you're maybe looking
[2095] for a position uh then please get in
[2098] touch and let's talk
[2099] uh also maybe I can entice you with some
[2102] pretty pictures the campus is right by
[2103] the lake it's a really beautiful area
[2107] um okay the other thing I wanted to say
[2108] up front is that everything I'm gonna
[2110] mention here is not just Maverick it's
[2111] really the product of uh some fantastic
[2114] collaborations uh of the people are
[2116] shown here and I've been very fortunate
[2118] to always have fantastic and smart
[2120] people to work with
[2122] all right so upfront I just want to
[2124] declare that the goal broadly of uh
[2127] Maverick and uh because the others that
[2129] I just showed is to model primary visual
[2131] intelligence
[2132] and uh the plan is for me to first walk
[2135] a little bit through what parameters
[2136] intelligence means and then uh I'll get
[2139] towards some modeling efforts and the
[2141] fifth time at the end where we can talk
[2142] about some more recent models that we
[2144] originally built
[2145] so uh as a human uh if you see an image
[2149] like this one you don't take it all at
[2151] once rather you fix it on different
[2153] areas of the image so for instance you
[2154] might first look at the stroller
[2156] um you might then also look at the bike
[2158] and you might notice the dog uh sitting
[2160] on the beach here
[2161] what's really fascinating about humans
[2163] is that you can detect these these
[2166] objects in favor parts of the image in a
[2170] very brief amount of time so I'm gonna I
[2173] hope this works so soon but I'm gonna
[2174] flash these images improve succession
[2175] and I bet you will still be able to
[2177] recognize all of the objects uh pretty
[2179] seamlessly
[2181] so these are around 100 milliseconds or
[2183] so uh and probably you have no trouble
[2185] recognizing what the objects are even if
[2187] they're blurry uh and if they're really
[2189] fast
[2191] so this is a paradigm that we call Core
[2193] object recognition so it's the image of
[2195] the center of phobia usually presented
[2196] very briefly
[2197] and like I said humans are really good
[2200] at this so we can easily recognize this
[2202] image as a dog
[2203] we can even do this when there are
[2204] changes in size color distortions
[2206] occlusion or motion blur uh it's still
[2209] going to be really easy for you to
[2210] recognize the dog in all of these images
[2213] and while we know what the area where
[2216] what one areas that enables this this
[2219] Behavior Uh this area is called the
[2221] ventral visual stream I'll talk a little
[2222] bit about the later
[2223] uh we don't know how exactly this works
[2225] so we know where it roughly happens that
[2227] that we were it was a good object
[2229] connection but we don't really know why
[2231] uh so the one big question in the field
[2233] of neuros ancestors always been how
[2234] exactly does this work
[2238] and turns out if you look at this a bit
[2240] more closely so on the right here is a
[2242] diagram of all the visual areas that are
[2244] thought to be involved in Vision this is
[2246] a classic work from federal Anderson
[2248] and the point I really just want to make
[2250] with the status that brim thrusting is
[2252] highly complex so it has just been very
[2254] difficult for our field to make sense of
[2257] what exactly is going on
[2259] and so quite necessarily if we have to
[2262] start with what I'm going to call
[2263] piecewise efforts so for instance if
[2265] interested in Vision you might take some
[2267] electrodes in a primate brain maybe the
[2269] only parts of the brain you might
[2270] collect some data uh maybe even build a
[2272] model that expends that data and then
[2274] there's another group that also collects
[2276] some data and maybe they also build a
[2277] model but eventually what our fields and
[2280] recently was left with was this
[2281] collection of isolated data and isolated
[2283] models so
[2284] we added off the the pieces but nobody
[2286] really talked to each other at the
[2288] moment this is somewhat anecdotal to uh
[2291] to the story of different men feeling an
[2293] elephant and nobody quite getting the
[2295] the full picture
[2298] yeah
[2301] so I don't want to diminish any of this
[2303] work it's totally necessary
[2305] but I think everyone would agree that if
[2307] we're after a unified model then these
[2309] steps alone are insufficient
[2312] so what I'm gonna try to advocate for is
[2314] that our field builds want to kind of
[2316] call system models
[2317] and the idea to get there uh I think
[2320] it's not a clever idea it's just a
[2322] necessity is integrative benchmarking
[2325] that's what it just means let's take all
[2326] the data together and use them
[2328] collectively to guard and constrain the
[2330] models
[2331] and that is exactly what brain school is
[2333] trying to enable
[2338] excuse me
[2340] so come back to the anecdotes uh our
[2342] hope is that this will let us see the
[2344] the full picture not just as little
[2345] parts of the elephant but the full
[2347] elephant of pyramid vision
[2350] and so assuming back into how exactly
[2352] the ventric virtual stream process
[2354] objects so when you're uh when light
[2356] hits the retina so an image is processed
[2359] by brain it sends it through lgm to V1
[2362] which is the first cortical area in the
[2364] primary brain to process images it then
[2365] goes through a hierarchical stages that
[2367] we call b2e4.t and that t is thought to
[2370] hold the representations out of which
[2372] you can linearly decode things like
[2374] object identity uh maybe also size or
[2377] rotation or different things like that
[2379] so when we now want to compare models to
[2382] these mechanisms in the brain then
[2384] there's really two major sets of data
[2386] that we've been working with one is the
[2387] behavioral data so the outputs of the
[2389] system and second is the neural data so
[2391] how does the system internally represent
[2394] uh these incoming images
[2396] and so these together make up the
[2398] benchmarks that we now have in brain
[2399] secure and I'm going to work a little
[2401] bit through what exactly those are like
[2404] so I'm going to show you one behavioral
[2405] Benchmark and you can play subject for a
[2408] little bit uh to see what what the data
[2410] collection is like
[2411] so imagine uh you're being paid for this
[2414] so you have to fix it on the white dot
[2416] and I'm gonna I'm gonna flash an image
[2418] and then there's gonna be two choices so
[2420] in person I would ask you to raise your
[2421] hand but maybe you can raise it and zoom
[2424] even if the camera's off okay maybe you
[2425] can just think uh which Which choice you
[2427] would make okay ready
[2430] uh so you probably have chosen the dog
[2432] in which case uh as a subject you would
[2435] be getting paid and this was a pretty
[2437] easy crowd but you can probably imagine
[2438] if these images are rotated in some ways
[2441] and we introduce changes in Viewpoint
[2443] parameters at some point this gets
[2445] pretty tricky so for instance here you
[2447] might not have been sure if this was
[2448] really a bear or maybe it was a rhino or
[2449] something else
[2451] that's what we can do with these trials
[2453] is we can build a confusion Matrix that
[2455] tells us for every image and all
[2458] possible distractors how easy is it to
[2460] recognize the correct object in the
[2461] image so for instance recognizing dog
[2463] versus Fork is pretty simple so it's
[2466] indicated in green and blue colors here
[2468] whereas maybe distinguishing the bear
[2470] from the Rhino might be more difficult
[2471] which is still indicated in red
[2474] so when you then build a benchmark this
[2476] is the behavioral data that we work with
[2477] from the humans and the experimental
[2480] Paradigm to show the models is to just
[2482] use the same images
[2484] uh we use a unified API to work with all
[2487] the models I'm not going to go into
[2488] digital on that but I heard it's just a
[2490] way to treat all models as the same
[2492] thing so here we have the models perform
[2494] a task of object categorization and have
[2496] them look at the stimuli that developers
[2499] are shown to the humans
[2501] the stand allows us to get the better
[2504] predictions of the model so these are
[2505] just the choices that the models make on
[2508] these images whether they get confused
[2510] in certain ways so we've got the same
[2511] kind of confusion Matrix and then we use
[2514] a similar similarity metric that here is
[2516] simply a correlation to compute a score
[2518] of how aligned the models and humans are
[2521] with respect to this particular task
[2524] I want to point out that this is not
[2526] just accuracy but rather it's really the
[2527] Image level alignment so if humans get
[2530] certain images wrong then the model is
[2533] actually being punished if it gets it
[2534] right so the model has to make the same
[2535] mistakes as humans and has to get the
[2537] same things right it's really alignment
[2539] not just ground with accuracy
[2543] okay so the nice thing about this
[2546] task setup is that we can also run it on
[2548] monkeys here you can see a macaque
[2551] monkey at some cage doing the same kind
[2553] of task so at the bottom here you see a
[2554] screen should ring a Bells the same kind
[2557] of task that you just did and it gets a
[2560] reward and a green screen if it gets
[2561] right and a black screen and timeout
[2563] where it usually wants to keep going if
[2564] it gets it wrong
[2565] and my card monkeys are extremely good
[2567] at this and I should say that it's been
[2569] found in the past that their virtual
[2571] system is extremely similar to that of
[2572] humans
[2574] but uh in the case of monkeys we can use
[2577] more invasive tools so we can show
[2578] images and record from their brain
[2583] activity at the same time so here we
[2584] record the the spike rates
[2587] and essentially you can think of that as
[2588] one vector across neurons per image so
[2591] at the end of the day we're left with
[2593] the Matrix of images times neurons we're
[2595] essentially one element tells us how
[2598] active a particular neuron is for a
[2599] particular image
[2601] and I want to take a brief moment to
[2604] give some rationale for why we're
[2606] choosing Spike rates here so this is
[2608] worked by uh Tong in 2015 and the these
[2613] plots here are different sites uh from
[2615] the recordings that I just showed you
[2616] the x-axis is time so zero is stimulus
[2619] onset the stimulus is on for 100
[2620] milliseconds and then for many sites you
[2623] get the typical Spike responses
[2626] now we usually choose to use the spike
[2629] rates between 70 and 170 milliseconds
[2632] that's where the neuron is most active
[2633] we don't use
[2635] the spikes but rather
[2637] how many spikes were within the time
[2640] period
[2641] and that gives us pretty much the Matrix
[2643] that we are the richest saw
[2645] and the reason we do that is because it
[2647] was found that when you fit a linear
[2649] decoder on these bike rates to predict
[2652] obviously classes in the image then uh
[2656] you can
[2658] actually predict human behavior
[2659] extremely accurately so the plot on the
[2662] right to explain a bit more on the
[2663] x-axis's performance so this is just
[2665] ground truth accuracy and the y-axis is
[2668] consistency with human behavior so again
[2670] how similar are the choices of it to
[2672] humans it's a similar metric to what I
[2673] showed you before so do you make the
[2675] same mistakes to get the same things
[2676] right
[2677] in for instance uh in before we don't
[2680] get this alignment even though we get we
[2682] extrapolated we get really good
[2683] performance but in it from I.T Spike
[2686] rates we get high performance and are
[2689] soft in the human zone so we are
[2691] consistent with human behavior
[2693] I even make the same mistakes and we get
[2694] the same things right
[2696] and because we found that Spike rates
[2698] are
[2700] the thing that actually predicts human
[2701] behavior at least in this task pretty
[2703] much perfectly we so far didn't see a
[2705] reason to go down to spikes uh there's a
[2708] thing for the discussion where we can
[2709] talk more I'd love to hear other
[2711] viewpoints on this
[2712] okay but really this is to say uh we're
[2715] using Spike rates and uh all the rest of
[2718] the benchmarks are going to be on spec
[2719] grids typically in this 70 to 170
[2721] millisecond window
[2724] so again when we build a benchmark now
[2726] to test the models we show the same
[2728] images to the model uh we're gonna have
[2731] to look at the images uh I should say
[2733] since there's many layers in the model
[2735] we typically pre-declare some of the
[2737] layers to be different areas in the
[2739] ventral Stream So maybe this layer
[2740] should be one this one is V2 before an
[2742] OT
[2743] yeah we usually do this on hell.data uh
[2746] but I'm yeah I'm going to leave it there
[2748] so we record from the corresponding area
[2750] which has been created pre-committed to
[2752] a certain layer in the neural network
[2754] and then we get the activity sorry the
[2756] activations in the
[2760] uh of that layer in response to the same
[2762] images that the monkey version and then
[2764] we use a similar metric that's called
[2766] neural productivity to obtain a
[2767] similarity score and again this assesses
[2770] the internal alignment of model and
[2771] parameter representations
[2772] if
[2774] there are questions I can talk a little
[2775] bit about what the new productivity
[2776] measure is but in in a nutshell it's
[2778] really uh we fit a linear regression
[2780] from a subset of the model predictions
[2782] to the data so we cross validate over
[2784] images and then on held out images we
[2786] apply that regression so the regression
[2788] weights and try to predict the data and
[2790] then we compute a correlation to this
[2793] tenfold and overall get an overall
[2797] similarity score now there's different
[2798] ways of doing this there's ways to
[2799] compute the similarity score without
[2801] regression for instance RDM is for those
[2803] of you if you might have heard of that
[2806] um but yeah so the different options we
[2808] typically use what we call Android
[2809] productivity or this this regression
[2811] measure
[2813] right so putting it all together now uh
[2815] we have the brain we get measures from
[2818] the brain in the bush of interesting
[2820] mirrors ranging from B1 through it as
[2823] well as the bureau outputs
[2824] these then make up the benchmarks that
[2827] we test models on in brain score and
[2830] for modern candidates we pre-commit
[2832] certain layers or single layers to the
[2835] regions in the promoters team
[2839] so when we're actually run models I'm
[2841] going to show scores on the different
[2843] sub regions on the left
[2846] we can test for instance hmax which is a
[2848] more classic Neuroscience model
[2850] this is from I think the 1999 or so it
[2854] performs okay but maybe that's a lot to
[2857] to wish for so when we now tested the
[2860] latest at the time at least latest uh
[2863] deep learning models
[2865] including like resnets densnets
[2866] mobilnets and whatnot we find that one
[2870] they're a lot better than what we had in
[2872] neurosense before so certain of these
[2874] these networks at the time of the state
[2876] of the art models of neural and
[2877] behavioral element with respect to
[2879] Primary Vision
[2880] but also that they're uh that they have
[2882] some ways to go
[2883] I want to point out that all of these
[2886] scores are always shown uh in an
[2888] up-to-date Fashion on the brainscoder
[2890] website so I encourage you to to check
[2892] that out
[2893] and again here the the models are all
[2894] compared in a unified Manner and not
[2896] just on one Benchmark so come back to
[2898] what is at the beginning we don't want
[2900] to just see a part of the elephant but
[2901] rather we just models on all the
[2902] available Branch works so really like
[2904] the most attempt to predict all past
[2907] present and future data that we have
[2908] available
[2910] and then our community is adding more
[2912] and more of these benchmarks so I really
[2914] really think this is a way to guard
[2916] against the wolf fitting because models
[2918] have to predict data that maybe doesn't
[2919] even exist yet but that someone is going
[2921] to connect in the future
[2923] and it's a much stronger test of
[2925] generalization at the moment I'm going
[2926] to show you what this looks like right
[2927] now so uh at this point in time we have
[2930] 51 different neural and behavioral
[2932] benchmarks so these range from
[2934] distributional measures like uh
[2936] centers around modulation and V1 up to
[2939] behavioral generalization uh for for
[2942] Behavior as well as everything in
[2945] between
[2946] I really think this is quite an
[2947] extensive set now uh and at least a
[2949] manual is the biggest set of primate
[2951] Vision benchmarks that are publicly
[2953] available
[2956] now we can also do some science with
[2959] this so on the waxes I'm going to plot
[2961] average brain score so this is going to
[2963] be the average over V1 V2 V for it neuro
[2966] as well as the behavior measures that we
[2968] have
[2969] and so one dot is going to be one model
[2972] across all the models we found at least
[2974] in 2018 that
[2976] models from the densnet and resonant
[2978] families were the most brain like you
[2980] might notice that these happen to be
[2981] models that have skipped connections so
[2983] there might be some architecture inside
[2984] there as well
[2987] but what we can also do with this now is
[2989] we can ask is there some kind of
[2990] normative variable that explains why
[2993] some models are better than others so
[2995] can we find
[2996] something that predicts the the brain
[2998] scuffle model
[3000] and there are two goals for this one is
[3003] it might hint that how the brain
[3005] optimizes so it might tell us why some
[3007] models are better than others and the
[3008] second goal is just an engineering goal
[3010] which is that if the x-axis is easier to
[3013] optimize than the y-axis then that's a
[3015] way to more efficiently improve the
[3016] models
[3019] and so what we found is that plotting
[3021] image Network one performance versus
[3022] brain score actually gives us a pretty
[3024] strong correlation so the better models
[3027] are demonstrated the more brain like
[3029] they are number centers would say uh
[3030] probably everyone knows this but it's
[3031] it's a big computer vision
[3033] classification data set so over a
[3035] million images and the task for models
[3038] is to classify the objects in the image
[3042] and so at the time we thought oh great
[3043] uh maybe we can just wait for for image
[3046] not to or for computer vision to solve
[3048] the brain for us if this correlation
[3049] holds then maybe we can just
[3052] sort of sit back and eventually computer
[3054] vision will have a perfect image of the
[3056] model that maybe does a really good
[3057] model of the brain but you might notice
[3059] that even for these models there's still
[3060] a long way to go
[3062] uh so we're far from done and maybe to
[3064] to form the enthusiasm around this a
[3066] little bit we found
[3068] this year then that if you look at the
[3070] latest models
[3071] there's actually no more correlation
[3073] maybe even an anti-correlation so models
[3075] that are better dimensionate now
[3087] Okay so
[3089] I want to spend
[3091] maybe yeah the last couple of minutes to
[3094] talk about some models that we've built
[3096] I'm gonna go over this pretty briefly
[3098] if there are particular questions on one
[3101] specific model then let's just talk
[3102] about them in discussion
[3104] so like I said the models are far from
[3106] perfect and I think some people will
[3109] take this to me now maybe deep learning
[3111] isn't hardly flawed for me this just
[3112] means uh there's room for improvement so
[3115] I I think the dogma of new networks is
[3117] consistent with the Neuroscience Dogma
[3119] so I think staying within that that
[3121] framework makes sense to me uh but
[3123] clearly there's work to be done and we
[3124] we need to make the models better
[3125] because so far they're uh poor in many
[3128] ways
[3129] uh one way in which we've made models
[3132] better is a model that we call a cornet
[3134] so
[3135] typically these deeper networks have
[3137] hundreds of layers uh which is a bit
[3140] difficult to align with neural Anatomy
[3141] so what we aim for in cornet was to
[3143] build a much more compact model that
[3146] only has about a dozen layers and then
[3148] in order to retain performance we
[3150] introduced recurrence so this is one
[3152] block of cornet it has four blocks that
[3155] correspond to V1 V2 for an ID
[3158] and you notice that the block has this
[3160] recurrent Motif so input is process but
[3162] that is processed again with the same
[3164] weights so it's a simple form of
[3165] recurrence that is not stateful in this
[3168] case where only has a very simple state
[3171] uh but it actually gets us pretty far
[3173] um so uh I don't have this product here
[3175] but with respect to other models
[3178] coordinates is much much more shallow so
[3181] many fewer layers uh but retains image
[3183] to Performance as well as principle
[3185] performance and maybe even generalize
[3186] this a bit better
[3187] one other point that we were really
[3189] excited about with this model is that it
[3190] allows us to test if we can predict
[3192] temporal Dynamics so the spike rates of
[3195] uh it over time and turns out that it
[3200] can so the devices here is how long it
[3202] takes the ID representation to solve an
[3205] object meaning that if you add different
[3207] points in time if you try to use the
[3209] sticker approach that I showed you
[3210] before and you try to decode the object
[3212] at what time does it actually recognize
[3215] the object so some some objects or some
[3217] images are recognized earlier some are
[3220] decoded later and turns out that Cordon
[3222] can to a first extent at least predict
[3224] when exactly that is going to happen in
[3227] the it population
[3228] this is one measure of temporary
[3230] Dynamics in it
[3232] another model that recently build is
[3234] called v1let so here we found that if we
[3237] plot the
[3239] brain score V1 alignment of models
[3241] versus the robustness to whitebox and
[3243] result attacks then models that are more
[3247] like V1 are actually more robust so for
[3249] instance the records here are Motors
[3251] that are address really trained to be
[3253] robust to Corruptions in the image
[3256] and so uh
[3258] my colleagues uh Joe Lopez to the model
[3261] that uses a B1 front end that is not
[3265] trained it's it's really a classic V1
[3267] model from neurosense in a sense and
[3269] that is put in the front of a network
[3270] and then the rest of the network is
[3272] trained and Trend or mentioned that as
[3273] usual and that network is almost by
[3277] Design better at V1 but also happens to
[3280] be much more robust to the to the set of
[3281] sort of attacks as well as much
[3282] Corruptions and without animator sort of
[3284] trading so this is just standard
[3285] training so for some time this was uh
[3287] things did if they are done on
[3288] robustness and it's probably been
[3290] preceded but it's really a maybe a sign
[3292] of Neuroscience giving some insight into
[3294] machine learning again
[3297] into the the final thread I want to
[3299] mention you is that there's usually a
[3301] lot of controversy around the the
[3303] training of these models so usually
[3305] they're yeah they're trained for
[3307] millions of images and for many epochs
[3310] so in this work we showed that you can
[3311] actually get away with much fewer
[3313] updates uh
[3315] meaning that on the x-axis here is the
[3318] number of epochs times the number of
[3320] images and also including the weights
[3321] and we showed that actually without any
[3324] training you can already do decently
[3326] well on on brain score so as at least
[3329] with respect to some standard model and
[3331] then with two orders uh
[3333] magnitude figure updates you can already
[3336] retain around 80 of the score so far
[3338] from perfect but I I think a pretty
[3342] decent first approach that that shows
[3344] that maybe you don't need all that
[3345] training uh there's a paper came out
[3348] today from like bonusini and efferences
[3350] group that showed similar results for
[3352] language so this might be somewhat
[3353] consistent that maybe
[3355] we don't need all the training to be
[3356] brain aligned uh perhaps at least for
[3358] for the rural areas for Behavior maybe
[3360] we need other Downstream training uh but
[3363] it seems like at least from an alignment
[3364] we yeah we don't need as many supervised
[3367] updates
[3368] infected Vision uh
[3370] found that you can use unsupervised
[3374] methods and without any training or
[3376] without any label images at all you can
[3378] already do decently well at least on
[3380] smaller architectures this is yet to be
[3382] generalized to larger models but I think
[3384] this this gives some hope that you can
[3386] relax supervised training to to a good
[3389] extent
[3391] yeah I'm Gonna Leave the models there uh
[3393] let's talk more about it in the
[3394] discussion if we have time and wrap up
[3396] so the most of what I talked about was
[3399] this platform brain score which is a set
[3402] of Integrative benchmarks that allow us
[3403] to identify the current most brain like
[3405] models and vision and also discover the
[3407] key relationships between row function
[3409] and computation I'll show you one
[3410] example of that where we show that
[3412] image.net is a strong predictor of brain
[3414] score at least up to a certain level
[3416] and then second I told you that the
[3418] models still have many flaws but I think
[3421] that also yeah gives us a reason to
[3424] improve them and uh just build better
[3426] models and I showed some examples where
[3429] we proved the neuromy and they're
[3431] Trading
[3432] uh so with that again please reach out
[3434] if you're interested in these questions
[3435] and uh yeah let's talk about the
[3437] questions there thank you
[3440] cool thanks so much for that talk it was
[3442] so interesting to hear
[3444] um so yeah I'll start by reading a
[3446] question from the chat and then I'll
[3447] open up the floor so uh Mark Schoen
[3451] asked um thanks for the interesting talk
[3452] Martin how do you measure Spike rate for
[3455] feed forward value Networks
[3458] and then he has another question but
[3459] I'll ask them thanks for passing I can
[3461] never keep track of the question so
[3463] that's the first question so the the
[3466] spike rate is really just the
[3469] um the activations of a particular layer
[3471] so let's say you have a 10 layer Network
[3473] then maybe you declare layer five to be
[3476] the one that best corresponds to V2 or
[3478] so then when you show images you just
[3480] keep track of the activations so these
[3482] are continuous networks so there's some
[3484] real valued number there and we can
[3486] treat that as a spike rate
[3489] um yeah like I said there's there's 10
[3490] ways to compare them uh
[3492] we typically use this linear regression
[3494] which uh then it allows for like a
[3497] linear rotation and rescaling uh but
[3499] that
[3500] then aligns it maybe more strongly to
[3503] the actual spray grids from from the uh
[3505] print recordings but I really adjust the
[3506] activations in the models
[3509] I think yeah thanks and then Mark also
[3513] asked um recently Transformers have
[3515] moved up the ranks on imagenet
[3517] um is the recent Trend in correlation
[3519] observed due to the trade-off between
[3521] convolutional neural networks and
[3523] Transformers and do you find
[3526] Transformers to be less brain line yeah
[3528] that's a really interesting question um
[3530] I I don't think I have a definite answer
[3531] so uh I have maybe some pieces of an
[3534] answer so some of the recent trend is
[3536] indeed because Transformers are better
[3539] at image net but uh a lot of the
[3541] Transformers we tried
[3542] really sort of went down the hill on
[3544] brain score uh so initially we thought
[3546] oh maybe Transformers are just the wrong
[3547] architecture but then earlier this year
[3550] we had uh our inaugural brain skill
[3552] competition so people were submitting
[3554] models and tried to
[3555] predict a lot of these benchmarks and
[3559] the I think second best model in that
[3561] competition was actually based on a
[3562] Transformer that's now like I think
[3564] around top three on the leaderboard so I
[3566] think it's at least to me it's not clear
[3569] if there's really a trade-off with the
[3571] architecture and if maybe Transformers
[3573] are less pretty like architecture or
[3575] maybe architecture doesn't matter at all
[3577] like I guess that's some of the
[3579] intuition in Machining right now that at
[3580] least if if you're using a reasonable
[3583] space of architectures then as long as
[3585] you scale it up big enough maybe it's
[3587] just not as important
[3588] um I'm not entirely sure from the brain
[3591] side it it seems like some transform
[3593] architectures are not great at least
[3595] with respect to certain kinds of
[3597] training but uh then there also seem to
[3599] be ways to remedy that and actually make
[3601] it pretty well aligned on these
[3602] benchmarks
[3611] uh yep thanks and then uh yeah we have a
[3614] question from uh Rory
[3616] um Rory says what do you think about
[3618] interpreting activations as voltages
[3620] instead of firing rates
[3623] um like C elegans neurons is it
[3625] presumptuous to assume spiking
[3628] yeah uh there's probably a deeper
[3631] discussion here maybe I'll
[3633] so I I come more from an engineering
[3635] background uh it's my maybe my some
[3638] Progressive answer is uh it seems to
[3639] work so I'm so far okay with it uh I
[3642] think we as a sort of as Neuroscience
[3644] Community we have work to do to make it
[3647] more aligned that's what these models
[3649] are trying to do in some ways we haven't
[3651] really worked on models that really
[3653] output activations that could actually
[3656] be voltages I think there are other
[3657] groups that have done some of this where
[3659] you also respect the uh the balance of
[3662] for instance excitatory and inhibitory
[3664] neurons in the brain uh the models I've
[3666] shown you so far do not do that they
[3668] might stumble upon inhibition by
[3670] accident but we certainly haven't
[3672] enforced it and probably if you
[3674] without the regression if you just view
[3676] these activations they
[3678] I would guess to where yeah I know they
[3681] don't immediately look like Spike grids
[3682] so they're like in a linear Subspace
[3684] they're aligned um but maybe not per se
[3687] and I should say that the reason for
[3688] this linear alignment is really that if
[3690] you compare it to two brains for
[3692] instance to monkey brains uh you also
[3694] just can't find like one neuron here
[3696] that corresponds to the other one there
[3697] really you always have to allow for some
[3698] linear rotation and these higher level
[3700] areas
[3702] so um I think the linear regression is
[3704] is a fair thing to do or maybe it's
[3706] maybe there's ways to make it more
[3708] restrictive
[3709] but yeah I think that's basically on the
[3712] models on that front yes
[3717] um yeah I I also just wanted to add so I
[3720] I really loved the approach I remember
[3721] when the first Pages came out and I
[3724] think there's loads we can learn from it
[3726] but I guess just there's a bit of it's
[3728] like a devil's advocate question
[3730] um what do you think we could learn from
[3733] a model which had a higher brain score
[3735] so it I think it's one of the top brain
[3737] score we could get up to so like what
[3739] would a model with the bread score of
[3741] one tell us yeah yeah so yeah one is
[3744] indeed at the top well like we we
[3745] normalize all the scores by an estimated
[3747] ceiling so how consistent and reliable
[3749] is the data
[3750] um so you don't have to break data that
[3752] the data itself can predict that's one
[3754] version of the ceiling yes what would it
[3756] mean to have a perfect one um so I
[3759] personally am most excited by sort of
[3761] the engineering aspects of it or the
[3764] application aspect so we uh the the
[3766] Color Lab presented some papers where
[3768] you can use these models now to for
[3770] instance control the neural activity so
[3772] uh let's say you have a good model of it
[3774] that can predict it firing rates from
[3777] images and I can sort of flip the whole
[3779] thing around you can ask what you have
[3780] to do in order to drive some of the
[3782] neurons really high and maybe keep
[3783] everything else really low so let's say
[3785] I want some one hot encoding in the in
[3786] the neural space and I want to really
[3789] drive one iTune run up then what are the
[3791] images that I have to show for this and
[3792] you can uh there's different links for
[3794] this but you can one of them is you can
[3796] back propagate through the entire
[3797] network onto the pixels so you can
[3799] change the pixels in a way to maximally
[3801] at least predicted by the model
[3803] maximally Drive the 181 and that
[3805] actually works so you can actually use
[3806] the models to control node activity in
[3808] that way sort of not invasively from
[3810] stimuli alone and so this was uh by
[3813] Busch running car in science 2019 and
[3816] one thing that's somewhere in the
[3817] appendix that maybe we should talk about
[3819] more is that
[3820] we looked a little bit at the alignment
[3823] on brain scale measures versus how well
[3824] the models can control neurotactivity
[3826] and turns out there's a there's a pretty
[3828] strong correlation so the the more
[3829] aligned models are at
[3832] some of these measures on brain score
[3833] the better they're able to control their
[3835] activity I think that's remember that's
[3837] a general Trend like I think if you can
[3839] predict something there is a lot of hope
[3841] to be able to control it and maybe to do
[3844] other cool things with it so I think the
[3846] if we have better and better models then
[3848] in moment there's a lot of hope to maybe
[3850] even want to go towards School
[3851] applications there's actually one key
[3853] thing I want to focus on in uh in the
[3855] lab I'm going to set up to try and see
[3858] if how far we can go with these models
[3860] but what can we really do with models
[3862] that are pretty predictive and I mean
[3863] what are the the key shortcomings that
[3866] we need to focus on because like I said
[3867] there's there's a ton of ways in which
[3868] they're wrong and I'd love to get a
[3870] better handle on what exactly would be
[3872] the most impactful to fix
[3875] that was a great answer so just yeah so
[3878] I guess just to follow up on the last
[3879] bit of it so you would imagine that if
[3881] you had recordings from like a disease
[3884] model
[3886] um and then you could build
[3888] um
[3888] yeah models which had a high brain score
[3890] on those disease model data then what
[3893] you'd compare is you compare the models
[3895] yeah the models between the standard
[3896] data and the disease model based on our
[3898] school it's different and maybe that
[3899] gives you some Intuition or hypothesis
[3902] to test on what's going wrong in the
[3903] disease model yeah exactly so what one
[3906] concrete
[3907] um project that we're directly in the
[3909] space that I've been working on is uh
[3910] sort of towards visual Prosthetics so
[3913] let's say if you have a model that can
[3915] predict what the behavioral effects are
[3917] of micro stimulation applied in I.T then
[3921] you might be able to use the model to
[3923] infer the right stimulation patterns to
[3924] elicit particular little persons and
[3928] yes like this is unpublished but there's
[3930] it looks like there's some hope that
[3931] this works at least quantitatively the
[3933] model predicts this pretty well actually
[3935] so for instance You can predict uh that
[3937] depending on which sites you stimulate
[3939] uh you're going to get more of a face
[3940] response or less of a face response from
[3942] Monkey so I think like long term if we
[3944] then improve on this access then uh we
[3946] might be able to get models that one day
[3948] can help people that are blind uh and
[3950] maybe can actually have a visual
[3951] prostituted prosthesis that stimulates
[3953] and recreates some of the biomimetic
[3955] vision and I think that we need the
[3957] models in here because we we don't know
[3959] how to stimulate right in it the models
[3962] might be able to tell us what exactly to
[3963] do
[3965] oh that sounds really cool
[3967] and yeah I mean I guess sort of
[3969] following up a bit on my question about
[3971] getting to the brain score of one
[3973] um again I'm not sure I believe it but I
[3975] think I just have to say it as the
[3977] snooper host
[3978] um do we think that using networks with
[3980] leaky integrate and fire neurons is
[3983] that's the missing 0.6 brain school is
[3986] that all we need to do to get the main
[3989] score up to one uh I don't know I would
[3991] love if someone tried it uh I think like
[3993] so far we we don't have a single model
[3995] submission that is a spiking your
[3997] network and I would love if we just had
[3999] some of those models up there uh I don't
[4001] know maybe an amount of a few models
[4003] applicable I would have someone could
[4005] submit it
[4007] yeah I was actually thinking of exactly
[4008] the same thing but uh yeah that's
[4010] awesome yeah that's quite normal
[4012] it'll be quite interesting to see how
[4014] well it does with the brain score
[4016] yeah that'd be awesome we have a bunch
[4018] of tutorials to to help with this
[4019] Mission and uh yeah we can always get in
[4021] touch and happy to help more yeah
[4026] yeah I mean I guess it doesn't even have
[4028] to be spiking we can see oh yeah
[4030] following up the question earlier we can
[4032] compare the egru network to the spiking
[4036] Network for example
[4037] yeah anything that can make no
[4039] predictions uh like so far on the level
[4041] of Spike rates uh yeah it's very good
[4049] cool
[4050] um I have so many questions but I feel
[4052] like I could just keep asking all day so
[4054] I think I'll I'll leave it well maybe
[4056] it's just one last one so I I remember
[4058] when the first paper came out the idea
[4060] was to have
[4061] um maybe a wrong but wasn't the idea to
[4063] have like data from other model animals
[4066] as well
[4069] yeah are there benchmarks or other
[4071] animals yet or not really uh so far no
[4074] uh we've been talking to the Ellen
[4077] Institute a little bit um I think there
[4078] are some like the different threads in
[4081] the mouse community that may be
[4082] interested in this uh I think so far
[4084] it's unclear to me if we have found
[4086] someone who really wants to spearhead
[4087] this like I I don't know anything about
[4089] mice so someone else I think would have
[4091] to delete this we're also working on
[4093] making the whole platform or the whole
[4095] code Library more modular so for
[4097] instance come people working on a brain
[4098] score for the human language system
[4101] um and I think yeah from there it should
[4103] be easy to adapt it so like all of this
[4104] is open source we have support
[4107] um so we definitely want to grow this in
[4109] some ways I think it's just really up to
[4110] the the sub communities to figure out if
[4112] they want to do this if the time is
[4113] right for them
[4114] um for for brains conversion I really
[4116] hope we can get some more human neural
[4118] data on there as well like right now we
[4120] have a lot of human behavior data but uh
[4122] like no after my recordings from humans
[4123] for instance
[4125] so definitely depends to expand uh
[4127] beyond what you have right now
[4129] that sounds great
[4132] um yeah well unless anyone else has any
[4134] more questions
[4135] um I think that oh yeah so thanks so
[4138] much to both of our speakers for the
[4139] time and yeah thanks to everyone for all
[4142] the questions and interesting discussion
