---
id: yt-vx6ATEoEuUE
type: youtube
title: Stochastic Model for Estimating Network-Scale Deterioration and Effect of Interventions
  on Bridges
url: https://www.youtube.com/watch?v=vx6ATEoEuUE
authors:
- BayesWorks
ingested_at: '2026-05-20T18:37:45Z'
content_hash: sha256:9a6295ba53dee22cd566b7a6a8b1cfffe3453f6d28e8e114e12dda595ef63dd2
domains: []
nlm_corpus_ids: []
wiki_pages:
- wiki/entities/bayesworks.md
- wiki/entities/quebec-bridge-network.md
- wiki/concepts/network-scale-deterioration-analysis.md
- wiki/concepts/state-space-deterioration-model.md
- wiki/concepts/ssm-kernel-regression.md
- wiki/concepts/kinematic-deterioration-model.md
- wiki/concepts/visual-inspection-monitoring.md
- wiki/concepts/bounded-unbounded-inspection-transformation.md
- wiki/concepts/inspector-uncertainty.md
- wiki/concepts/kalman-filtering-deterioration.md
- wiki/concepts/missing-intervention-handling.md
- wiki/concepts/deterioration-state-aggregation.md
- wiki/concepts/intervention-effect-modeling.md
meta:
  channel: BayesWorks
  channel_url: https://www.youtube.com/@BayesWorks
  duration_seconds: 1970
  caption_track: fetched
  snippet_count: 844
---
[1] so in previous talks i've talked about
[2] modeling the deterioration behavior of
[4] structural elements
[7] based on visual inspection data
[10] in this room we're going to see how we
[11] can extend
[12] this application to go beyond structural
[14] elements such as we can get the
[17] deterioration estimate for an entire
[19] bridge
[20] so the overall deterioration state and
[23] also the overall deterioration state for
[25] our entire network of bridges
[27] so my name is zachary and this research
[31] project has been published recently
[33] under the same title of this
[35] presentation
[37] so
[38] the
[39] breakdown for this presentation is going
[41] to be as follows first we're going to
[43] have a look at the context and
[44] objectives and by context we mean some
[47] of the characteristics of visual
[48] inspections and our objective in working
[51] with visual inspection data
[53] after that we're going to have a quick
[55] recap for the element level
[57] deterioration analysis
[60] so what are the basis of the method and
[62] how it's done
[64] and then in the following section we're
[66] going to have a look at the network
[67] scale analysis so how we can extend
[71] the analysis from an element level
[74] toward like a bridge level or even a
[76] network level which we're going to see
[78] in details
[79] and finally we're going to see a
[81] demonstration which is done on a real
[83] database
[85] from the network
[87] bridges and the province of quebec
[91] so visual inspections is a monitoring
[94] technique that's
[96] utilized on a large scale to monitor the
[99] deterioration state
[101] or the health state of infrastructures
[104] over time
[105] and when we are seeing a network we mean
[108] a number of bridges so in our case we
[111] have around 10 000 bridges located in
[114] the province of quebec
[116] some of these bridges are similar to
[118] each other in terms of material or
[120] traffic load while others are completely
[123] different
[124] now in order to have some intuition
[126] about like how visual inspections are
[129] performed we need to know like what's
[131] within each bridge
[133] so for each bridge we have two
[136] the two main groups of elements so we
[139] have elements that are directly
[141] associated with the structural safety of
[144] the bridge such as the beams and like uh
[147] other the slabs
[149] and we also
[152] we have elements that are
[154] associated directly with the
[155] serviceability of the bridge such as the
[159] safety barriers or the pavements element
[163] so each one of these
[165] category of
[166] structural elements
[168] is composed of a number of elements so
[171] we have
[172] like we could have two slabs in a bridge
[175] or like uh and so on like or 20 beams
[179] and so on for each one of these
[180] categories
[182] now the inspections are performed at the
[184] element level so an inspector would go
[187] and visit a bridge at a given year so
[189] for this example we have a year 2008
[192] inspector would go and perform a visual
[194] inspection
[195] on the element
[197] or like in general it goes like for all
[199] the elements
[201] and this
[202] these inspections are reported for each
[204] year so the inspections could happen
[207] like
[210] every two years or every three years
[212] depending on the frequency or the
[214] importance of the bridge so in this case
[216] we have every three years
[217] and like it carries on now for some
[220] structural elements we have also the
[224] like an intervention would happen so we
[226] have this information we know what kind
[229] of intervention that took place and we
[231] know when it took place
[233] so we have these
[235] and things carry on so in previous
[238] presentations
[239] we've talked about all these details how
[242] we can model the effect of interventions
[245] and how we also can model the
[247] deterioration behavior so we have an
[250] estimate for the deterioration states at
[253] the element level
[255] now our objective in this study is
[258] really simple we want to extend these
[260] deterioration state estimates
[263] beyond structural elements to get the
[265] deterioration states for the
[268] structured category as we saw earlier
[270] for example for the beams or the snaps
[273] and so on and we also even want to
[276] extend it further to get the the overall
[278] deterioration state for a bridge
[280] and even for a network of bridges so
[283] this is the main objective of this uh
[286] research work now in order to tackle
[289] this objective we have to take a step
[291] back and have a look at how we are doing
[294] the deterioration analysis at the
[296] element level
[299] so
[300] what we've done in the previous research
[302] work that has been already published is
[304] that we've described the deterioration
[306] behavior using a kinematic model this
[308] kinematic model is described by the
[311] kinematic equations for the condition
[314] the speed and the acceleration
[317] now if you want to write down these
[319] equations in a different way in matrix
[321] form makes it easier to look at we see
[324] xt which is the
[326] deterioration state at time t a is the
[329] transition matrix and xt minus one which
[332] is the deterioration state at the
[334] previous time step plus wt which is the
[337] processor
[339] now
[340] in order to be able to
[342] describe or not use this kinematic model
[345] we rely on the
[347] state space models now state space
[349] models it's composed of two models the
[352] first model is the transition model
[354] which is described in similar equation
[357] as we see
[358] above or the same equation which is the
[361] kinematic model equation as we see here
[364] and the process error in this case is
[367] described by a zero mean and covariance
[370] matrix qt
[372] now
[372] the way this goes is that we have
[376] a prior estimate for the condition at
[378] time t 0
[380] and we are using the this transition
[383] model to get the estimate at time t 1
[387] now
[388] in
[389] this is so far we haven't used the
[391] observation so if we have an observation
[394] at time t one
[396] we use the observation model which is
[398] described by y t equals to c the
[401] observation matrix multiplied by x t the
[404] deterioration state of time t plus v t
[407] which is the observation error
[408] and in this work we describe the
[411] observation error
[412] by a zero mean and the variance
[414] associated with each in individual
[417] inspector so
[419] the observation is dependent on the
[421] inspector that performed the inspection
[424] so using this observation model
[426] we can update our estimate for the
[430] condition and we can get the posterior
[434] for the estimate for the condition of
[436] destruction element and we carry on the
[438] same way so we have we use the
[441] transition model to get the next
[442] estimate and then there's an observation
[445] we use the observation model to update
[448] the model estimate with this observation
[451] and this is done through mainly through
[454] the kalman filtering approach however
[456] there are other characteristics
[458] uh other modifications that relate to
[461] this so in
[464] so in order to have
[466] or have an overview of these
[468] modifications again we have the
[470] inspection data
[472] for an element e we have the inspection
[474] data presented by whitetail
[477] and vital here represent the
[480] bounded uh
[482] conditions so like
[483] in general visual inspections are
[486] uh evaluate the structural element given
[489] like a
[490] certain bounds so it says that 25 is a
[494] poor condition and 100 is a perfect
[496] condition so these are what we call
[498] bounded
[500] visual instructions now in order to
[502] apply our framework what we've done is
[504] that we've used a transformation
[507] function
[508] call it a transformation function o
[510] which is like kind of a step function
[513] that would allow us to
[516] to transform our bounded observations
[520] into an unbounded space so we get like
[523] the observations y
[525] or the inspections y
[527] and after that we will be able to pass
[530] our observations into the deterioration
[533] model which is like
[535] we call it ssm or even like ss mkr
[540] these uh studies have been again already
[543] published
[544] and
[546] the ssm car refers to using kernel
[549] regression alongside the
[551] ssm model that i've described earlier
[554] so using this deterioration model we get
[557] the
[558] deterioration state estimate at time t
[561] for that particular structural element
[564] and then
[565] what we do is that in order for to be
[568] able to interpret the results
[570] we
[572] pass we back transform this
[574] deterioration state estimate into the
[576] bounded space
[578] so we
[579] back transform it using the same step
[581] function into the bounded space we have
[583] our deterioration estimate between the
[587] bounds that are well known for the
[589] inspectors so the as i mentioned earlier
[592] that the inspections in reality are
[594] bounded to refer to
[596] what is a poor condition and what is a
[599] perfect condition
[601] so these are in general
[603] again
[604] these are things that have been
[606] described in details in previous work
[609] now to look at an examples for element
[611] level analysis let's see the inspection
[614] data here so on the x-axis we have the
[617] timeline on the yearly scale on the
[619] y-axis we have the condition the
[621] condition starts from 25 for poor
[624] condition up to 100 for perfect
[626] condition
[627] however here for visual purposes the
[630] axis started at 40.
[632] the inspection data are reported by the
[634] blue points as we see here and each
[637] point is associated with an instructor
[640] so the inspector i
[641] [Music]
[642] each inspector have a unique id in this
[645] case so
[647] the uncertainty associated with each
[650] inspector
[651] has been estimated using the framework
[654] i've described earlier
[658] using a procedure within that framework
[660] so these are the estimates that are
[662] obtained for the uncertainty of each
[664] instructor
[665] and the
[666] deterioration
[668] condition estimate for
[670] this structure element is represented by
[672] the red line and the confidence interval
[675] around it described by the red area
[679] for one standard deviation and two
[681] standard deviation
[683] so this is like in general how things
[686] look like at structural element level
[688] now again as we mentioned that we also
[691] have on the structural element level
[693] some of the elements have underwent and
[694] interventions
[696] so if we look at this case so this is
[698] for a case for a beam that underwent
[701] reparation
[702] and this is again from a real case so we
[705] know that the intervention took place at
[707] the year 2011
[710] and we have again the inspection data
[713] reported by the blue point this is for
[715] the condition and the x-axis is the
[719] timeline on the yearly scale and the
[720] y-axis is the condition and we also as
[723] we described earlier that we are using a
[726] kinematic model so we actually also
[728] characterize the deterioration speed
[730] so the figure on the right represent the
[733] deterioration
[734] speed which we have again on the x-axis
[737] the timeline and the y-axis is the
[740] deterioration speed and again the
[742] intervention is at year 2011 and in this
[747] example i'm going to show that we are
[749] actually able to
[751] quantify and model the effect of
[754] intervention on structural element level
[756] as we see for the red dash line for the
[761] condition estimate for the
[763] uh this suction element and even for the
[766] effect on the deterioration speed
[769] as we see it on this side so again all
[772] of this have been done earlier
[775] but
[775] again the application was limited to an
[779] element level application
[782] so
[783] here right now what we're going to see
[784] is that how we can take this to a
[787] network scale
[788] application or network scale analysis in
[791] order to do so what we need to do is
[794] first when we are talking about a
[795] network scale we are dealing with large
[798] amount of data so millions or like
[802] hundreds of thousands of structural
[803] elements and millions of inspections
[806] so some of these inspections might be
[808] missing some we might have some
[810] inspections that are erratic
[813] and even we might have some missing
[816] interventions reports so like we have
[819] interventions that are unreported so how
[822] we need an approach to deal with that
[824] and the other thing we need an approach
[827] or an aggregation method that would
[829] allow us to aggregate the deterioration
[831] of states estimates at the element level
[834] to take it to a category level and then
[836] like even to take it to a bridge level
[839] and even
[841] finally to a network level
[843] so these are the two prerequisites so
[845] first we're going to look at how we can
[847] handle missing data and the most
[850] important part in here so again
[853] missing data the most important part is
[857] the missing interventions so
[860] we're going to talk about that so
[862] missing interventions could be
[865] the prior knowledge about the effect of
[867] an intervention is not available so as
[869] we saw the jump in the condition
[873] we have
[874] created a model that was able to
[877] estimate
[878] the jump associated with each type of
[881] intervention so we can quantify
[884] what's the
[885] what's this jump
[887] that
[888] we can but however in some cases we
[891] might not have enough data to quantify
[894] this prior knowledge so this prior
[896] knowledge could be missing so we need to
[899] kind of
[900] handle
[901] this and the way we handle it is that
[904] we say
[904] for a given type of intervention
[907] on a
[908] given category of structural elements if
[911] we don't have
[913] the
[914] effect of this type of intervention on
[916] that structure category we look to the
[918] closest thing
[920] and the closest thing is the
[921] expectations could be the expectations
[925] of the effect
[927] of interventions of that type of
[929] intervention on a similar on uh on
[934] other categories that belong to the same
[937] group of category of structural elements
[939] so
[940] further explanation can be done but
[944] the point here is that dealing with this
[946] issue is
[947] not that complicated we can
[950] replace the unknown prior knowledge with
[952] the expectation
[954] of
[955] other
[957] of the
[958] the same type of interventions on other
[960] social elements so that's possible
[963] the other point is that
[965] or the other missing intervention
[967] information could be is the type of
[970] intervention is not reported
[972] so this we can deal with it with the
[975] look likelihood now i'm gonna
[978] explain about this later on
[982] but getting to the third point about
[985] missing interventions
[987] the intervention date and the type are
[990] not reported so here we have inspection
[992] data the inspection data shows a jump
[995] but there is no mention of any
[998] intervention so we don't know
[1001] we know when the jump happened but we
[1003] don't know when the intervention
[1004] actually happened
[1006] and we don't know what kind of
[1008] intervention that happened so in order
[1010] to
[1012] uh
[1013] talk about so we're gonna explore this
[1016] third point uh
[1018] under the un unreported interventions so
[1022] this is an example for
[1024] data visual inspection data
[1027] that has again
[1029] the x-axis is the timeline and the
[1031] y-axis is the condition
[1034] and we have the inspections reported by
[1036] the blue points
[1037] and for this case we have no mention of
[1041] an intervention
[1042] in the interventions database so
[1045] there is no information at all about the
[1048] interventions however from visually we
[1050] can see that
[1051] an intervention could have happened at
[1054] 2012 2013
[1056] or even 2014
[1058] but we don't know when it actually
[1060] happened
[1061] so one way to handle this is
[1065] just run the model and perform the
[1067] prediction as is
[1069] but the issue is that we get
[1072] a kind of a biased estimate for the
[1075] condition because the condition we try
[1077] to
[1078] kind of fit the data based on the
[1080] uncertainty and so on so it would try to
[1083] pass in between the inspections
[1086] but again
[1087] and even if we look at this case the
[1090] inspector at 2011 is the same inspector
[1094] at 2017.
[1096] so
[1097] the potential that an intervention
[1099] happen is really high so how we handle
[1102] this
[1103] the way to handle this first is to
[1106] determine that there is a trend and
[1110] upward trend so again like visually we
[1113] can see that
[1114] uh the element was uh at a certain
[1117] condition and then the
[1119] condition has improved and continue in
[1122] the same improvement rate so this is not
[1125] this the potential of this jump being
[1128] noise
[1129] is really low
[1131] but
[1132] we need to kind of have a criteria to
[1135] tell us that yes there is an upward
[1138] trend based on the inspection data that
[1141] we see here so this criteria is defined
[1144] in these equations so
[1147] the criteria basically is
[1149] delta and delta is
[1152] represents basically the ratio between
[1155] the
[1156] positive the sum of the positive
[1158] improvements
[1160] over
[1161] the sum of all changes so
[1166] the sum of positive changes again over
[1169] the sum of all changes
[1172] in the absolute value so the sum uh so
[1175] the changes are described as the
[1177] difference between two consecutive
[1179] observations and delta t here represents
[1182] to because observations not necessarily
[1184] happen every year they could happen
[1186] every two years so that's why delta t is
[1188] here
[1189] so we look at the changes between two
[1191] consecutive observations
[1193] and in the case for the positive changes
[1196] we consider
[1197] any change any change that is positive
[1200] we report it
[1202] otherwise it's zero
[1204] so this is basically the criteria that
[1207] would tell us that yes there is a
[1209] positive trend in the inspection data
[1213] and
[1214] so we've determined okay we've
[1216] determined that there is
[1218] an actual up
[1221] positive frame
[1223] so now
[1224] and we determine that there is an
[1225] intervention at a given year how do we
[1228] determine the type of intervention we
[1230] determine it using the log likelihood
[1233] estimate so
[1235] because we have a limited number of
[1238] interventions that could take place on a
[1242] given structural category of elements
[1244] we can try to
[1247] plug in the effect of each type of
[1250] intervention and estimate the log
[1253] likelihood this is uh
[1256] there are further details and further
[1258] characteristics that
[1261] are detailed in the paper but however
[1263] this is the main intuition is that we
[1266] plug in the effect
[1268] and we try we estimate the log
[1270] likelihood
[1272] and at the end we chose the intervention
[1275] that has
[1277] that has the effect that maximizes the
[1281] log likelihood
[1282] on a one structure element so based on
[1285] these criterias
[1287] what we get for again the same
[1289] inspection or the same case what you get
[1291] is that there is an intervention 2012
[1295] and that effective
[1296] the effect of intervention is modeled as
[1299] follows
[1300] so this is for
[1302] the missing interventions
[1305] are reported at all there are further
[1307] details that uh
[1309] characterize like how we deal with the
[1312] other issues but like these are the kind
[1314] of
[1315] highlight of
[1317] the
[1319] that part now
[1321] we talked about missing data now we want
[1323] to talk about handling outlayers because
[1326] again
[1327] we have a very large data set
[1330] and
[1331] a lot of data could be uh some of the
[1334] data could be erratic information or it
[1336] could be like
[1339] human error so
[1341] whenever we see an outlier
[1343] and
[1344] just to reiterate
[1347] so
[1348] for an outlier to be classified as an
[1350] outlier is that whenever the model there
[1352] is a numerical instability in the model
[1355] so it like basically the model can't
[1357] perform the prediction because of the
[1360] presence of such an observation
[1362] so that's why we've defined and that
[1365] could happen whenever we have a large
[1367] jump in the
[1369] in the observations
[1371] so this large jump could be due two
[1374] possibilities one of these possibilities
[1376] is
[1377] that this large jump is a missing
[1379] intervention
[1381] so we need to do the processes
[1384] associated with
[1385] missing intervention but however if we
[1388] couldn't find any clue that this outlier
[1391] is actually a missing intervention then
[1394] we need to remove
[1396] the outlier data
[1398] so that we can actually perform the
[1401] prediction and the forecast in the
[1403] framework
[1405] so
[1406] and the removal of the outlier is
[1408] basically based on
[1411] a weighted average so
[1415] the equation or the criterion that we've
[1418] defined is that
[1419] to identify at which time the outlier
[1421] happened is the arc max over t
[1424] and t again is the x axis
[1426] and it's the difference between
[1429] each of the observations minus the
[1432] weighted average y hat
[1435] and this weighted average is weighted
[1438] based on the uncertainty of each
[1440] inspection so basically
[1443] the
[1443] for an observation to be an outlier it
[1447] has to have uh
[1449] this has to have it has to be really far
[1453] away from all other uh observations
[1456] and the inspector that performed it has
[1458] to have a large uncertainty so this is
[1460] the main criteria or the best criteria
[1463] that we can derive
[1465] uh based on the available data in a
[1468] given element
[1470] so that's for
[1472] uh handling outliers and handling
[1474] missing data
[1476] now again there are further details and
[1478] further conditions about like what
[1481] determines an outlier what determines
[1483] the missing intervention and how we
[1485] handle both
[1487] each described and further details in
[1489] the paper
[1490] now in the
[1491] following subsection we're going to talk
[1493] about how we can aggregate the
[1495] deterioration state estimates
[1498] so
[1498] as i've showed earlier for each element
[1501] i have my bounded inspections by uh
[1504] defined by whitehead so in this example
[1507] i'm gonna see
[1509] like
[1510] i'm gonna process three elements at the
[1512] same time these three elements belong to
[1514] the same category so for example this
[1516] could be the category of
[1518] slabs so i have
[1520] three uh
[1521] three slab elements each of them has
[1524] their own inspections over time bound
[1527] and inspections and they are all within
[1528] the same bridge
[1530] so i do the same steps
[1532] i pass each one of them into the
[1534] transformation function the step
[1536] function i've talked about
[1538] and that would give me the unbounded
[1541] observations for each one of these
[1543] elements
[1544] and then i plug these observations into
[1547] my deterioration model and i get the
[1550] deterioration state estimate for each
[1552] one of these elements again nothing so
[1554] far is different now the part that we
[1558] can aggregate these estimates is
[1561] about to start so here we have
[1564] so these estimates for each one of these
[1566] elements we can aggregate them based on
[1569] a weighted sum of the gaussian densities
[1572] so these each one of these deterioration
[1575] estimates is gaussian
[1578] so we can have weighted sum of these
[1581] gaussian densities based on weights
[1583] lambdas
[1585] as we see here we can have weighted sum
[1587] that would define the and the lambdas
[1590] would define the contribution of each of
[1592] these deterioration
[1595] state estimates to the overall
[1597] deterioration state estimate so we
[1600] obtain the
[1601] uh
[1603] the merge for all the deterioration
[1605] state estimates and this is again a
[1607] gaussian and what we do finally is that
[1610] we pass this into reback transform it
[1612] using the step function
[1614] into the uh
[1616] the original space or the space where
[1619] again the inspectors know how to
[1620] interpret so
[1622] that's from 25 to 100 in this example so
[1625] that's how we merge
[1628] the uh like uh
[1631] we merge three elements and it could be
[1633] extended to an n element
[1636] but this uh just an
[1638] example for demonstration purposes now
[1641] the
[1642] gaussian mixture reduction approach
[1644] that's utilized the equations for this
[1646] approach are described in this in the
[1648] paper but the concept is really a
[1650] weighted sum of gaussian densities to
[1652] obtain a single gaussian density and
[1655] then we back transform into the original
[1657] space and we get the uh
[1659] so
[1661] this is really the principle of the
[1662] method now if we go
[1664] if we go and see a real case study again
[1668] we've talked about the
[1670] the breakdown for like what's within a
[1673] bridge
[1674] and the elements and the visual
[1676] inspections and we've talked about that
[1678] we use this visual inspections to get
[1680] the deterioration estimate for each
[1682] element now we can we what we want to do
[1685] is to extend this deterioration state
[1687] estimate to get the deterioration state
[1690] estimate for each category so for the
[1692] beams and so on and even further for the
[1696] group of uh
[1698] of categories such as the group of
[1701] elements that are responsible for the
[1703] structure safety of the bridge or
[1704] serviceability of the bridge so let's
[1706] look at an example for each we have the
[1709] first example
[1710] uh
[1711] the concrete slab category
[1713] in uh in this particular bridge so on
[1716] the left graph is the condition the
[1719] right and the speed on both
[1722] graphs we have
[1723] the timeline is
[1725] on the x-axis on the early scale and the
[1728] y-axis
[1729] on the graph on the left represent the
[1731] condition on the right to represent the
[1733] speed the inspection data here
[1736] are reported by the blue triangle with
[1738] the uncertainty so
[1740] this is really an aggregation for all
[1743] the observations performed on the
[1745] elements within this category so that's
[1748] why it's represented by a triangle
[1751] measure and as you see for this category
[1754] example we have actually an intervention
[1756] so that intervention took place in 2015
[1759] and if you want to see the deterioration
[1761] model estimate is represented by the red
[1763] dash line and the confidence interval as
[1766] we see here for both the
[1769] and the condition and the speed
[1772] so that's for one category if you want
[1774] to go further and go for all the primary
[1777] elements or all the elements that are
[1779] responsible for the safety of the bridge
[1782] we have the
[1784] observations represented by the blue
[1786] diamonds as we see here and the
[1787] uncertainty so these are the aggregated
[1789] observations for all the elements within
[1793] the bridge and these elements are again
[1796] responsible for the structure of safety
[1798] such as like
[1799] an aggregation of all the beams and
[1801] slams and so on so these are all the
[1803] observations the
[1805] intervention have happened in year 2015
[1809] and again the differential model
[1811] estimate is represented by the red dash
[1813] line and the confidence interval for
[1816] each the condition and the speed in this
[1818] case
[1820] now if you want to extend this even
[1822] further we can actually estimate the
[1824] deterioration state for a network of
[1826] bridges and this case study we've done
[1829] for seven thousand uh bridges
[1832] so again the way to look at it is that
[1834] each bridge has
[1837] elements that are responsible for
[1838] structural safety and has elements that
[1840] are responsible for the serviceability
[1842] so the way we looked at it is that even
[1844] for a network we're gonna do it the same
[1846] way so we're gonna aggregate
[1848] the deterioration state estimates
[1850] for all the br the bridges and and
[1854] within the same uh kind of type elements
[1857] so
[1858] all the structural safety for all the
[1860] bridges and all the service abilities of
[1863] elements for all the bridges
[1865] so to see an example how it looks like
[1868] so here we have a graph again a figure
[1871] with the left figure as the condition
[1873] the right trigger is the speed
[1876] and the timeline is uh on a yearly scale
[1879] on the x-axis and the condition on the
[1882] y-axis from 25 to 100 and here we
[1885] represented the observations by a
[1889] magenta diamond and this like again to
[1891] represent the aggregation of all the
[1894] elements within the primary elements uh
[1897] for all the bridges
[1900] uh are at this uh kind of condition
[1903] so as we see here this is like the
[1906] overall for the network now if you want
[1908] to see
[1909] the deterioration condition estimate we
[1913] see it in the red dash line and the
[1914] confidence interval
[1917] around this estimate each for the
[1919] condition and the speed as well
[1922] now further interpretation of these
[1924] results and further analysis can be
[1927] shown in the
[1929] paper but for this this is like really
[1931] to highlight one type of possible
[1934] analysis that we can do
[1935] now finally in conclusion the key
[1938] contributions of this work is that we've
[1940] designed a network network scale
[1943] deterioration model that would allow us
[1945] to estimate the overall deterioration
[1947] condition and speed at a bridge level or
[1950] even at a network scale
[1953] and we've also designed a model or a
[1956] method or an approach to
[1958] handle the missing data and outliers
[1961] so all of this would enable the
[1963] potential for performing network scale
[1966] planning based on visual inspections
