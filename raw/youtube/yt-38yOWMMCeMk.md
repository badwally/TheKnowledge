---
id: yt-38yOWMMCeMk
type: youtube
title: 'Tech talk: A practical introduction to Bayesian hierarchical modelling'
url: https://www.youtube.com/watch?v=38yOWMMCeMk
authors:
- Faculty
ingested_at: '2026-05-20T17:02:42Z'
content_hash: sha256:30ca841300fa5b9eb64adf4c8a1717b97b7aa16cce616a18d7dd1ff273b6be28
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Faculty
  channel_url: https://www.youtube.com/@faculty_ai
  duration_seconds: 3171
  caption_track: fetched
  snippet_count: 1512
---
[8] um
[8] hi everyone thank you so much for
[10] joining me today
[12] my name is omar and today we're going to
[15] be talking about
[16] hierarchical modeling
[19] and before i get into it however let me
[22] let me just spend two minutes of
[24] introductions
[27] so i'm i'm a data scientist at faculty
[30] and in case you don't know faculty
[32] we are an artificial intelligence
[34] company our mission
[36] is to make artificial intelligence real
[40] that means that we spend a lot of time
[43] doing research
[44] working to bring artificial intelligence
[47] to your business
[48] so it can have an impact in a positive
[50] way
[52] and we believe that artificial
[54] intelligence should be
[56] trustworthy impactful and beneficial
[58] across society
[60] and those principles have shaped our
[61] work with more than 200 organizations
[64] across public across public and private
[66] sectors so if you're interested in
[68] knowing how
[69] artificial intelligence can can help you
[72] grow
[72] and accelerate your business please
[74] don't hesitate to contact us we'll be
[75] more than happy to chat with you
[78] okay so with the formalities out of the
[80] way
[81] let me give you an overview of today's
[85] talk
[86] do my best to stick to the typical
[89] dramatic arc
[90] so starting with you know hierarchical
[93] modeling is the answer but what is the
[95] question that
[96] what is the question so i'm going to
[98] spend two minutes talking about
[99] data with hierarchical structures and
[102] then
[103] because hierarchical models really shine
[105] when we are using a pageant approach
[107] i'll spend some time just reviewing the
[110] very basics of bayesian inference
[112] not to give you like a full treatment of
[114] the topic but just to help you
[116] to help us set up the notation that i'm
[117] going to be using for the rest of the
[119] talk
[120] and having done that and
[123] i'll discuss the two popular approaches
[125] that people commonly use
[126] when modeling hierarchical data and i'll
[129] put particular emphasis
[130] in their limitations then like to save
[133] the day
[134] that's when i will introduce you to
[136] hierarchical models and i'll give you
[137] the intuition for them
[139] i'll give you some examples and i'll
[141] give you the code that you will need to
[142] implement them
[144] so at the end of the talk i'll give you
[145] a recap of all the points that we have
[147] covered and also dedicate some time to
[148] answer your questions
[150] so if you have any questions please just
[153] try them
[153] under on the chat and we'll get to those
[155] at the very end
[159] and before i proceed just let me tell
[162] you that
[163] if you want to follow the slides at your
[164] own pace
[166] all of those are available in my github
[168] account
[169] and also all the code that i'm going to
[172] be using
[172] using is there available i still need to
[175] make some updates to that code
[177] so that it's readable for you but it
[179] should be ready this afternoon as well
[184] okay so what is the problem that we're
[186] trying to solve
[189] whenever we whenever we start a new
[191] project we wish that
[193] our client will give us a large data set
[196] with mostly numerical features but
[198] unfortunately more of more often than
[200] not
[201] we come to find that a the data is not a
[204] lot of data
[205] and b it is played with categorical
[208] features
[209] it's like the two nightmares of every
[211] data scientist and
[213] big part of the work we do goes into
[215] figuring out what is the correct way
[217] of dealing with all of these
[219] non-numerical information right
[221] typically the solution that we end up
[222] with involves
[224] some form of encoding like a set of
[226] rules for translating
[228] the categorical features into numbers so
[231] they can be fed into a machine learning
[233] model
[234] we then test all of our ideas and decide
[236] for one
[238] base perhaps on some form of cross
[240] validation
[241] and then when we start a new project we
[243] have to start from scratch
[245] because the method that we use last time
[247] for encoding might not be the ideal one
[249] for for this
[250] different use case so today
[253] i'm going to teach you about
[254] hierarchical models
[256] which is the correct framework for
[258] dealing with any sort of categorical
[260] features
[261] and i dare to say now that you're
[263] thinking that
[264] haracad models should be appropriate for
[266] describing only hierarchical data
[268] that is data that can stay contains
[271] nested categories like
[272] say states within a country
[276] and after all that's kind of what the
[278] name suggests
[279] and you'd be right in those cases
[281] hierarchical models are the right answer
[284] but they are also the right approach
[286] even if the categories in your data
[287] do not form a nested structure okay so
[290] if you need to account
[291] for categorical features nested or not
[294] nested
[295] hierarchical models are the right
[297] approach and that's good news
[301] now i once heard my favorite writer say
[304] that no discussion should be carried out
[306] without examples
[307] so following his advice i'll move us
[310] away from the purely abstract
[312] by considering a very popular example in
[314] the literature
[315] you will find it very easily on google
[317] if you want to
[318] and the example is commonly referred to
[321] the
[322] rathon in minnesota cases study what is
[325] it
[325] so what is it about as you might know
[329] radon is a gas which is abundant in
[331] nature
[332] it is everywhere and it's usually not a
[334] problem however
[336] high concentrations of radon can
[338] actually be detrimental to people's
[339] health
[341] and unfortunately sometimes houses are
[344] built
[345] nearby natural radon deposits which of
[347] course poses a threat for the people
[349] living there
[350] so in an attempt to identify the places
[353] at risk
[354] some staff was designated to go all
[356] around the u.s
[357] measuring the concentrations of radon
[360] and that were present in people's houses
[362] and some of these measurements were
[363] carried out in the basement some were
[365] made on the on the ground floor
[367] and the county on which the measurement
[369] was made was also recorded
[371] so what you're seeing here in the
[373] current slide are the measurements for
[375] the state of minnesota only
[377] almost a thousand measurements which is
[379] you know like it's an okay amount of
[381] data
[382] unfortunately if we highlight the data
[385] that we have for
[386] each individual county we immediately
[389] realize that in some countries we have
[391] very limited data like this one which we
[394] have only four measurements
[396] or this other one that has only two
[398] measurements not even on the same floor
[402] and yes some counties do have
[403] significant amount of data but the
[405] problem is that many do not
[407] and why is that a problem well if we
[410] wanted to prioritize
[412] like taking actions depending on which
[414] counties are more at risk
[416] we will need to provide an estimate of
[418] how much radon there is
[419] in each county right and you know you
[421] really shouldn't trust the statistics
[423] that were derived using two data points
[427] so the problem is that given the data we
[429] have
[430] how can we provide a reliable estimate
[432] of the radar levels in each county
[434] an estimate that is somehow able to
[436] combine in a statistically rigorous way
[439] the information available within a
[441] specific county
[442] but also the information available for
[444] the whole state of minnesota
[446] so that's that's what we where we are
[448] heading
[449] but before we get into the into the main
[453] part of the of the talk we need to give
[455] a quick detour into what is a new
[457] friends
[458] but using inference is a must when we
[460] are doing hierarchical models
[461] so it will be important that we are on
[463] the same page here
[466] okay so inference is all about
[470] understanding our data right here i'm
[472] using the letter y
[473] to denote my data and given the data we
[476] have
[477] the byzan approach starts by making an
[479] assumption about how
[481] how such data could have been generated
[483] we choose a
[484] family of probability distributions
[486] parameterized by
[488] by some numbers which here i've called
[490] theta
[491] and this modeling assumption is called
[494] the likelihood function
[496] the abstraction might seem unfamiliar to
[498] you but i assure you it's nothing new
[500] when when you're making the decision of
[502] using say
[504] linear regression or logistic regression
[506] if you're doing classification
[507] or a neural network the choice you're
[510] making at that stage
[512] that is the likelihood and theta would
[514] correspond to the coefficients of your
[516] linear regression
[517] or the weights of your neural network
[519] etc so in the machine learning community
[522] the likelihood is commonly called
[524] the model but i'll refrain from using
[526] that terminology here
[527] because in the bygian approach we
[529] understand that
[530] the likelihood is only a part of the
[532] problem okay
[534] so and the likelihood is such that if we
[537] have enough data
[538] it will kind of concentrate around the
[539] narrow region of parameter space
[542] like pinning down the the values of the
[544] parameters
[545] that could have generated the data we
[547] are seeing
[549] if the data that we have is is not
[553] informative enough however
[554] the likelihood will be very diffuse
[556] consistent with a wide range
[558] of parameter values
[562] okay but the likelihood is only half the
[564] story a distinguishing feature of what
[566] is an inference
[567] is that whatever prior knowledge we had
[570] about the parameters
[572] that gets encoded into a probability
[573] distribution which we call the prior
[578] and again a tight prior distribution
[581] reflects the fact that we have high
[583] confidence in our domain expertise
[585] when we can very confidently narrow down
[588] the possible
[589] the possible parameter values and
[592] conversely a diffuse prior
[594] 5 reflects that like we have very poor
[597] domain expertise
[598] so a wider range of parameter values are
[600] allowed
[603] and by using inference combines these
[605] two pieces of information
[607] so that by a base theorem we obtain what
[610] we call
[610] the posterior distribution that is what
[612] we know about the parameters
[615] given our prior knowledge and the data
[617] we had collected
[619] and you know hopefully hopefully it'll
[622] be the case
[623] that the posterior distribution has less
[626] variance
[627] than the prior distribution so this is
[629] reflecting the fact that we have learned
[631] something in the process
[632] because the uncertainty after we have
[634] seen the data is less
[636] than the uncertainty we had before the
[638] data
[639] but that doesn't always happen okay poor
[643] knowledge
[643] combined with poor data will of course
[645] lead you to pre-inferences that's just
[648] a fact of life um
[651] but let me emphasize that obtaining the
[654] mathematical expression for this
[655] posterior distribution
[657] is not the ultimate goal of inference
[659] right that is trivial
[661] that's just like multiplying two
[662] functions and everyone can do that
[664] what we really want is to use that
[666] distribution
[667] to perhaps take its average or maybe the
[670] quantiles
[671] or perhaps we want to use that
[672] distribution to make predictions about
[674] future data
[675] and all of those questions answering all
[677] of those questions
[678] requires us to compute expectation
[680] values under the posterior distribution
[682] and that's that's the really difficult
[684] part
[685] because expectation values involve
[687] taking integrals
[688] and you know integrals are very
[690] difficult
[691] in fact if you're doing any modeling
[693] work talking about
[695] there's not just one parameter but but
[697] dozens of parameters or even hundreds of
[699] them
[700] so the integrals that you will need to
[701] compute are very very high dimensional
[704] very contractible and analytically
[708] so instead of solving integrals exactly
[711] we typically fall back on the famously
[713] known fact that
[714] any expectation you want uh can be
[717] approximated
[718] by taking samples and sampling from an
[721] arbitrary distribution
[722] regardless of dimension it's to a large
[725] extent to solve problem
[727] the gold standard for doing for sampling
[730] is an algorithm called markov chain
[732] monte carlo or mcmc for short
[735] and efficient versions of mcmc are
[737] already implemented in python
[739] perhaps in a bit too many libraries the
[742] examples that i'll be showing you today
[744] and the ones that are available on my
[746] github are using numpyro
[748] but don't worry too much about the code
[750] implementation i'm sure that even if you
[752] don't know numpyro
[754] you'll be able to follow the code very
[757] easily
[758] okay so that's our speed run of pacion
[761] in france
[762] let's now step back step back in into
[766] our main topic which is how are we going
[768] to model the categorical features
[771] and i'll start by i'll start by showing
[773] you the two approaches that do not work
[776] the first one is called complete pulling
[781] in complete pulling we take an overly
[783] simplified approach
[784] which is just to ignore the categorical
[786] features just
[788] treat all groups as belonging to the
[790] same category
[791] using the same parameters for describing
[793] every single group
[795] and i know that this already sounds like
[796] a horrible idea but at least
[799] we are kind of overcoming the small data
[801] problem because everyone gets thrown in
[803] the same bucket
[804] and i'm going to show you how this
[806] approach works in practice but
[808] before i get to that please let me
[810] clarify the notation that i'm using here
[812] um i'm using y to denote my data like i
[815] said and the subscript
[817] on that y is being used here to
[819] enumerate the different observations
[821] that's like the standard thing
[823] so in my made-up diagram uh here i have
[826] observations one and 2
[827] belonging to group 1 observations 3 4
[831] and 5
[831] belonging to group 2 and etc
[836] but for this talk of today i'm really
[838] not interested
[839] in keeping track of the individual
[841] observations what i really care about
[843] are the the groups to which these
[845] observations belong
[847] so to avoid having many indices i'm
[850] going to abandon
[851] the standard notation and instead use a
[854] subscript
[855] to the note group membership so my
[858] diagram will look like this
[860] um it's not that i have less data right
[862] i'm just abbreviating
[863] and saying that y sub 1 are all
[866] observations made for group 1
[868] y sub 2 are all observations made for
[871] group 2
[872] etc
[875] okay so going back to our textbook
[877] example
[878] how would a complete pulling model look
[880] like in this case
[882] well during the modeling phase we simply
[884] forget about the fact that the data was
[886] gathered from different counties
[888] and we just see the data as belonging to
[890] minnesota
[892] as a whole and let's say that i'm going
[894] to choose to describe my data
[896] with a linear regression model and
[898] that's my likelihood
[900] it has three parameters
[903] the first parameter alpha is the
[905] intercept term
[906] it tells me what is the average level of
[908] radon on the ground floor
[911] the second parameter beta tells me what
[914] is the slope so how much the level
[916] changes
[916] when i go from the basement to the to
[918] the ground floor
[921] and finally there's this parameter sigma
[924] which measures
[925] how much noise there is in my data and
[928] since i'm putting all of the counties in
[929] the same bucket
[931] this parameter is kind of doing a lot of
[933] work right in a sense
[934] the difference from the differences from
[936] one county to the next
[938] any possible source of noise is is
[940] getting drawn into this parameter
[943] and okay so that's the likelihood but
[945] i'm doing bayesian inference remember so
[947] i'm gonna need some priors on the
[949] parameters
[950] and because i know very little about
[952] radon and i know very little
[954] about minnesota i'm just going to choose
[956] briars that are fairly wide
[958] to reflect my ignorance so i have alpha
[962] i have a prior for our that is normally
[965] distributed around zero
[966] um with five standard deviation we're on
[969] the logarithmic scale so that's really
[971] like something very very wide
[974] okay so those are my priors but the
[977] question is what is the posterior
[978] distribution right
[979] what can i say and can i say it more
[982] about my parameters
[984] given the data that i have seen so we
[987] construct a posterior distribution by
[989] by multiplying likelihood and priors
[992] and then we can use markov chain monte
[994] carlo to draw samples from that
[996] posterior distribution
[998] and we can maybe take the mean of the
[999] posterior etc
[1002] so i'll give you a very quick demo of
[1004] how that works in empire
[1006] the relevant part of your code will look
[1008] something like this
[1010] you have some import statements um to
[1013] get some helper functions from numpyro
[1015] like a sample function
[1017] uh and the densities that we are going
[1018] to use in the model
[1020] and all of our model is going to be
[1023] encoded in a function
[1024] and this function takes data as
[1026] arguments
[1028] in this case the only feature that is
[1029] going into my model
[1031] is the floor on which the measurement
[1033] was made
[1034] so basement or grantsor and the log
[1037] radon is my
[1038] target variable if you if you like
[1040] that's just the measurements
[1044] the main body of the function contains a
[1046] bunch of sample statements
[1048] and each sample statement is a
[1049] multiplicative factor in in bayes rule
[1053] some of the sample statements correspond
[1055] to the prior distribution
[1056] for my parameters and this is the sample
[1060] statement
[1061] is my likelihood function where i'm
[1063] saying that the observations
[1065] of log radon are normally distributed
[1067] around the given mean
[1068] mu with some standard deviation sigma
[1073] and i'm doing linear regression so that
[1076] mu is just given by a straight line
[1078] with intercept alpha and slow beta
[1081] but strictly speaking like mu is not a
[1083] new parameter right it's just a
[1084] deterministic
[1086] combination of parameters that i already
[1088] had alpha and beta
[1090] so this deterministic statement isn't
[1092] just making that explicit
[1095] okay so once you have your model written
[1097] in the form of function
[1099] numpyro has everything you need to run
[1101] markov chain monte carlo
[1103] you just have to create an instance of
[1105] the mcmc class
[1107] passing your model as an argument pack
[1110] your data into a dictionary
[1112] that then gets fed into into the class
[1116] you just hit run and it's really that
[1118] simple you get the samples
[1120] so now that you have those samples
[1124] you compute whatever expectation you
[1125] want but let's just plot the samples in
[1128] a histogram
[1129] so that we understand what they look
[1130] like
[1132] and you will see something like this so
[1135] our model had three parameters remember
[1137] so we have three
[1138] three marginal distributions one for
[1141] alpha one for beta and one for sigma
[1144] and just from these histograms we see
[1146] that we've learned a lot
[1147] right if you look at the alpha if you
[1150] remember my prior
[1151] alpha was a normal distribution centered
[1153] at zero
[1155] with the standard deviation equal to
[1156] five but now what i'm seeing here
[1159] is a posterior distribution centered
[1161] around
[1162] 0.7 ish and with the standard deviation
[1166] i would say around
[1167] 0.1 roughly that's like a
[1170] 50 times less uncertainty than what i
[1172] started with
[1173] and this is possible because i have so
[1176] much data for minnesota
[1177] but it doesn't really matter if i
[1179] started with a poor domain knowledge
[1182] my likelihood function is doing all the
[1183] work helping us to make good inferences
[1186] so when i combine the distributions of
[1188] my intercept and the distribution of my
[1190] slope
[1191] then i can get a distribution over the
[1194] over the line
[1195] that goes from basement to ground floor
[1197] and
[1199] it will look something like this when we
[1200] put it in the context of the data
[1202] we see that the mean radon level for
[1205] minnesota
[1205] can be estimated very precisely so just
[1208] to be clear
[1209] the line that i'm showing you now is how
[1211] well we can estimate the
[1213] the average radar level and i'm not i'm
[1216] not showing you the full posterior over
[1217] the data which would also include
[1219] the variance term sigma the the width of
[1223] the purple line here
[1225] like which is almost hard to see um is
[1228] just reflecting the fact that when it
[1229] comes to the location of the mean
[1231] we have very little uncertainty about
[1233] that
[1235] okay but having a having an accurate
[1237] estimate for the for the state
[1239] of minnesota can be very useless right
[1241] because
[1242] when we are interested in the individual
[1244] counties
[1245] describing each county with the same
[1248] statewide average
[1249] doesn't help me prioritize any specific
[1251] county the county on the top
[1253] left looks a bit weird right the two
[1256] measurements that i have
[1257] are way above average with which looks
[1260] dangerous
[1261] but my model is ignoring that so i have
[1263] a highly biased model if you like
[1267] this brings me to my next approach which
[1269] is called a
[1270] no pulling model in a no pulling
[1274] approach
[1275] what we do is favor the individual
[1277] information we have about each group
[1280] and just treat each group as independent
[1282] from each other
[1283] so we end up with a separate model for
[1285] each group literally
[1286] and it's very easy to see how we do that
[1288] in our example
[1290] instead of having a single line for the
[1291] whole stage of minnesota
[1294] i fit a separate line for the data in
[1296] each county
[1298] so you have to be very careful here
[1299] because the distinction from the
[1301] complete pulling model
[1302] and the no pulling model it's all hidden
[1305] in the indices of my parameters
[1308] but what i'm saying is that each county
[1311] will get
[1311] its own intercept term each county will
[1314] get
[1314] a different a different slope sorry a
[1317] different slope
[1318] and you can also have a different noise
[1320] term
[1321] for each county if you think that's the
[1323] right thing to do but in this case
[1325] i'm just going to assume that the amount
[1326] of noise is the same in every county
[1329] just to keep things simple
[1332] and again i need priors on my parameters
[1336] but given that i have no more
[1337] information about any specific county
[1339] those are just names to me
[1341] uh it makes sense that i use the same
[1343] prior for everyone right
[1345] um and how do i write a code for such a
[1348] model
[1350] well again the model is defined as a
[1352] python function
[1353] that takes data as arguments
[1356] the key difference is that now the
[1359] county on which the measurement was made
[1361] is part of the information that is going
[1362] to fit into my model
[1365] i'm also making use of this plate
[1367] context manager provided by numpyro
[1370] so that instead of having a man to
[1372] manually define
[1373] a different alpha for each county i just
[1376] define these parameters inside of this
[1378] context
[1379] and numpyro automatically turns this
[1382] into a vector of parameters
[1387] then when constructing the line that
[1389] passes
[1390] through the data we just have to be
[1392] careful of using
[1394] the alpha and the beta that correspond
[1397] to the count that i care about
[1401] these are like um like the indices that
[1403] i have on my likelihood
[1405] so what's gonna happen when i draw
[1407] samples from this model well
[1409] before we had just one alpha and one
[1412] beta
[1412] and the variance but now i have
[1415] 87 alphas one for each county 87 beaters
[1419] and i have also the variance term
[1421] so if i wanted to look at those those
[1422] will be like a lot of histograms to put
[1424] on one slide
[1426] and so instead i'm going to hand pick 15
[1429] counties that i want to
[1431] focus on and instead of looking at the
[1433] histograms like
[1434] face on what we are doing here is that
[1437] we are looking at the histograms from
[1438] above
[1439] so that that's two plots on that you're
[1441] seeing on the left
[1442] where for each county i am showing you
[1444] the portion of the histogram
[1446] that would correspond to like the 95
[1448] interval
[1449] and then on a slightly thicker black
[1451] line i'm showing you the 50 percent
[1454] interval
[1455] and that big white dot in the center is
[1456] just the median
[1458] so in what in what's coming i want you
[1460] to pay special attention to
[1462] this county right here which happens to
[1465] have an unusually high estimate for
[1466] alpha
[1467] but it's also very uncertain this is a
[1469] county that only had two measurements
[1472] so when i combine the samples for alphas
[1475] and the samples for betas
[1476] again we get a distribution over the
[1478] possible line that goes from basement to
[1480] ground floor
[1481] and we see something like this now
[1484] we have a different estimate line for
[1486] each county and we might be okay with
[1488] how those estimates look like for
[1490] perhaps the two bottom plots
[1492] um but look at the uncertainty that i
[1494] have on the two on the top
[1495] two plots in the top left plot in
[1498] particular my uncertainty is going from
[1501] one to four and remember that this is on
[1504] the logarithmic scale
[1505] okay so that's like three orders of
[1507] magnitude
[1508] and fine we now have bespoke inferences
[1511] for each county but
[1512] some of these inferences are useless and
[1514] because there's just too much
[1516] uncertainty to them
[1519] so isn't there a way that we can capture
[1522] uh like the information from the other
[1524] countries somehow like
[1526] share information across those groups
[1530] uh yes there is but that's what that's
[1532] what that's what this is about
[1533] that brings me to the topic of
[1535] hierarchical models
[1537] and there are many ways of thinking
[1538] about hierarchical models
[1540] but my favorite way of introducing the
[1542] topic is to first
[1544] talk about a slightly broader concept
[1547] which is called partial pulling
[1549] okay so what is partial pulling well we
[1552] have these two approaches
[1553] complete pulling where all the groups
[1556] are modeled with the same parameters
[1558] and we have the node pooling where each
[1559] group is given its own set of parameters
[1563] and these parameters are completely
[1564] independent from each other in this case
[1569] in partial pulling we understand that
[1571] these two options
[1572] are not two totally unrelated approaches
[1576] but rather we see them as the extremes
[1578] of a continuing spectrum of modelling
[1580] approaches
[1581] this continuum is obtained by
[1582] introducing some amount of correlation
[1585] between between the group level
[1586] parameters
[1590] and we can obtain some degree of
[1592] correlation by
[1593] first starting with the node pulling
[1595] model where everything is independent
[1598] and with then we introduce an extra set
[1600] of parameters like latent parameters
[1602] whose job is not to describe the data
[1604] anymore but rather to describe the
[1606] parameters themselves
[1608] and by the way the diagram that you're
[1610] seeing now on the screen
[1612] this is the reason why we call them
[1613] hierarchical models it's not because the
[1615] data is hierarchical
[1617] it could be but that's not the reason
[1619] the reason is that the parameters are
[1620] hierarchical
[1621] we have parameters for the data and then
[1624] we are going to introduce parameters
[1625] four parameters
[1627] that that's the reason for the name so
[1630] okay at this point just like we had to
[1633] make an assumption
[1634] for the likelihood function and just
[1636] like we had to make an assumption for
[1638] the prior
[1639] there's also an assumption here to be
[1640] made about
[1642] what latent model are we going to use
[1646] a popular choice which is also friendly
[1648] as a form of an introduction
[1650] is to use a gaussian model parameterized
[1653] in terms of mean and its variance
[1655] so now the group parameters the fetus um
[1658] not only they have to feed the data they
[1661] also have to feed each other
[1662] in such in such a way that they
[1664] accommodate to a normal distribution
[1668] if the variance of the latent model is
[1670] chosen to be very large
[1672] we obtain basically a flat distribution
[1674] which allows the parameters to be
[1676] wherever they want
[1680] and if we choose a small variance then
[1682] the parameters are forced to be very
[1684] close to each other
[1686] so let me show you how we how you would
[1689] write this down for
[1690] our example and but for simplicity
[1693] let's say that for now i'm just
[1695] interested in introducing
[1696] pulling for the for the intercept term
[1699] for the alphas
[1700] and i'm going to forget about the betas
[1701] for now
[1704] so like i said we go back to our no
[1707] pulling model where everything is
[1708] independent from each other
[1710] and then we replace the prior on alphas
[1713] on the alpha with a model for the alphas
[1716] and because i'm doing by using inference
[1718] that just means that i need to introduce
[1720] some priors on these new parameters that
[1722] i've introduced
[1724] so i'm gonna have a prior for the mean
[1727] um
[1728] and i don't know around which value the
[1730] parameters are going to center so
[1732] my prior for the mean is going to be
[1733] very wide
[1736] but instead of having a prior for for
[1738] the variance for the sigma alpha
[1740] i'm going to manually tell my model how
[1743] much variance i want to have
[1744] between the group parameters
[1748] again like the nonpirate code is quite
[1750] simple
[1751] it looks just like the no pulling model
[1754] except that
[1756] as an input to my model i'm going to
[1758] specify how much pulling i want to have
[1762] the intercepts of the counties are now
[1765] given a model instead of just a prior
[1768] and so new parameters come into play and
[1771] that just means
[1772] that i need to put some priors on these
[1773] new parameters
[1776] so i can specify how much pooling i want
[1778] a value i give a value for sigma alpha
[1781] and then i can get samples from this
[1782] model
[1785] and you would see something like this so
[1787] for now let's just
[1788] now focus on the on the parameter alpha
[1791] i'll forget about beta i'll forget about
[1793] al just let's look at the alphas
[1797] on the far left i have the result for
[1799] when i set the variance between the
[1800] parameters to be zero
[1802] as expected like all the groups end up
[1805] being having the same estimates
[1807] which is equivalent to a complete
[1808] pulling model right when when all para
[1811] all counties were being described by the
[1813] average minnesota
[1814] estimates on the far right
[1818] if i let sigma alpha be equal to 1 in
[1821] this context that's a very high value
[1823] and then i see that the group parameters
[1826] can be very different from each other
[1827] and in fact this is just exactly the
[1829] same result that i got
[1831] when i was doing the no pulling approach
[1833] allowing everything to be independent
[1837] and finally i have this middle ground
[1839] when i said sigma alpha to be 0.5
[1842] so the parameters are now kind of
[1844] similar to each other but only slightly
[1847] and i no longer have like a wild
[1848] estimate there which is very very high
[1851] so if you were to play this game for
[1853] many values of sigma alpha
[1855] and do these plots you would end up with
[1857] something like look like
[1858] this plot here so now i'm just showing
[1861] you the mean i've got rid of the
[1863] i could i got rid of the the confidence
[1866] interval the credible interval thing
[1867] because
[1869] you'll be too cluttered here so i'm just
[1871] showing you the mean of the alphas
[1872] as i'm as i'm changing the amount of
[1874] pulling in the model
[1877] so partial pulling allows me to learn
[1880] from the data
[1881] of the other counties and the amount of
[1883] pulling that i that i choose
[1885] tells my model how important the data
[1888] from the other counties is
[1891] and i get to say if the other counties
[1893] are super important
[1895] so i recover a complete polling or if
[1898] the other counties are like irrelevant
[1900] and i recover the no pulling approach
[1904] and just look at how my estimate for
[1907] this county gets
[1908] drastically regularized as i increase
[1910] the pull right
[1911] quickly joining the rest of the values
[1915] and a very cool feature is that the
[1918] amount of pulling
[1919] does not happen uniformly across my
[1921] parameters if you look at what's
[1922] happening here
[1924] we see that there's the estimate for
[1926] nobles
[1927] which starts to decrease immediately as
[1929] i increase the pulling
[1931] but the estimate for lake of the woods
[1934] stays kind of flat
[1935] for a while and only really starts
[1937] creasing
[1938] once the pooling has gotten strong
[1940] enough
[1942] this is happening because i had more
[1944] data for lake of the woods
[1945] than i did for novels so my model just
[1948] knows
[1950] how to take that into account and
[1953] that's great and all but i think i think
[1955] i know what you're thinking
[1956] which is how much bullying should we use
[1960] right before we have to decide between
[1961] two approaches
[1963] complete or not pulling now i have an
[1966] infinite number of options and i have to
[1968] choose one amongst them
[1971] and that brings me to hierarchical
[1974] modeling
[1975] and with everything that we've covered
[1977] so far it's going to be a very very
[1979] a very easy jump we want to use some
[1982] amount of pulling
[1983] perhaps but the correct amount of
[1985] pulling is kind of unknown to us
[1988] we don't want to pull the parameters if
[1990] they don't want to be pulled
[1992] we just want to allow for that
[1994] possibility but we don't want to be
[1996] imposing anything
[1998] so in the magician in the bayesian
[2000] viewpoint
[2002] unknown is just another word for
[2004] parameter
[2005] and if we want to estimate a parameter
[2008] all we have to do
[2009] is give a prior for it show the data
[2013] and then let the magic of markov chain
[2015] monte carlo do its work
[2016] to give us the estimate
[2020] so let's do that so i take my partial
[2022] pulling model
[2024] and where i was given a a specific value
[2028] for sigma alpha
[2029] i now just put a prior on that i have no
[2031] idea what the right amount of pulling
[2033] should be
[2034] so the prior that i have to choose is
[2035] going to be very wide in this case i'm
[2037] choosing an exponential distribution
[2039] which is covering a very wide range of
[2041] values from 0 to 1
[2043] 2 and even higher values so i'm saying
[2047] that all of those
[2048] pollings are possible i don't know which
[2049] one
[2052] in my python code now this means that i
[2055] will no longer have to specify by hand
[2058] how much pulling i want to have so
[2059] that's no longer an argument in my
[2061] function
[2062] instead i just give a prior for it and
[2065] then proceed to run
[2066] markov chain monte carlo in the usual
[2068] way what comes out
[2070] on the other side once we get the sample
[2072] it's just it's really nice
[2074] um i get an estimate for the intercept
[2077] that exhibits like a natural amount of
[2078] pulling
[2080] an amount of pulling that was not
[2081] imposed by me but it was learned from
[2083] the data
[2085] and how much pulling that's the
[2087] histogram on the right she's showing you
[2089] my posterior distribution
[2090] over sigma alpha and which is somewhere
[2094] which
[2095] has its mean around 0.35
[2099] 0.4 perhaps but i don't have to commit
[2102] to any single value of sigma
[2104] alpha right the budgeting approach is
[2106] already taking the average
[2108] of all of these possibilities so if we
[2111] go back to
[2112] to the previous plot that we had here
[2114] what we've learned
[2115] is that the right amount of pulling is
[2117] somewhere in this blue region
[2119] and by using inference automatically
[2121] takes the average of all those
[2122] possibilities
[2124] so let's finally take a look at how this
[2126] model behaves
[2127] in the context of the actual data
[2134] if you want to if you i want you to pay
[2137] special attention here
[2138] to the to the region that that i have in
[2140] the in the red circle
[2142] because that work that's where the main
[2143] action is happening
[2145] um we started with this complete pulling
[2148] model
[2149] right which turned out to be useless
[2151] because
[2152] it's kind of ignoring the fact that the
[2154] observation that i have here
[2156] is way above average okay um
[2160] so this is like a high bias model
[2164] then we moved to a no pooling approach
[2167] and
[2168] we ended up with like overfitting
[2171] basically because if we are told to fit
[2173] a line
[2174] and we are only given two data points
[2176] well what else are we gonna do
[2178] other than you know drawing a line that
[2180] passes exactly through my two points
[2183] and the fact that in the context of the
[2186] rest of the data these two points are
[2187] abnormally large
[2189] that's kind of irrelevant to me i just
[2191] feed a line that passes
[2192] through those two points and that's my
[2194] best estimate for the mean
[2195] however we do recognize that with two
[2198] points
[2198] our best estimate is not going to be a
[2201] very good estimate
[2202] so we end up with this massive massive
[2204] uncertainty
[2207] then we tried hierarchical model
[2210] and now we are not ignoring the
[2212] individual data of each county
[2214] but i am also not overfitting because i
[2216] can now share information across all
[2218] counties
[2219] and i'm also obtaining more precise
[2221] estimate for free
[2223] so let's look at it again we have
[2227] high bias we have high variance
[2231] and we get this one which is just right
[2235] and you might be wondering why the
[2236] uncertainty in the basement
[2238] is still high and that's because i'm not
[2240] doing any pooling for the parameter beta
[2243] for the slopes
[2244] so if you introduce a hierarchical model
[2246] for the slope then you will be able to
[2248] fix that uncertainty too
[2252] okay um so that's hierarchical models
[2254] let me now
[2255] talk to you about something about how
[2258] you incorporate
[2259] group level information and so what am i
[2262] talking about
[2264] if you're one of the lucky ones your
[2266] client might come to you and say
[2269] hey i actually have more data in this
[2271] other file
[2272] and then it turns out that the data
[2274] you're shown is not
[2275] of the same data but it's actually some
[2277] other file
[2278] with information about the categories
[2280] that were in this other file
[2282] and this this new data set is it's a lot
[2284] smaller of course
[2286] and for example in the in the radon in
[2289] the rather cases study
[2290] we actually know what the abundance of
[2293] uranium
[2293] is in each county so that's kind of like
[2295] an extra piece of information we might
[2297] use
[2298] so you think to yourself hey that might
[2301] be useful
[2302] so you proceed to do a merge of the
[2305] tables and then just chuck everything
[2306] into your extra boost right well
[2309] that's a mistake in this new data that
[2312] you've just been given
[2313] is not data about the radar measurements
[2316] it's data about your groups
[2318] and those two pieces of information
[2320] leaving two entirely different levels
[2323] your model should somehow take that into
[2325] account
[2327] and with hierarchical models doing that
[2330] is really super simple because what you
[2333] can do
[2334] is that you go back to the parts of your
[2336] model that was describing the intercepts
[2339] for instance
[2341] and you turn that into a regression
[2343] model itself
[2344] like a linear regression for example
[2347] where now
[2348] i'm using the uranium uranium abundance
[2350] as a predictor
[2351] that's like the u here and
[2354] this linear regression is a bit
[2356] mysterious okay it's like
[2358] it's all happening on parameter space
[2361] uh so this model does not directly talk
[2363] to the radon measurements
[2366] in some way somehow hidden from us
[2369] but it is allowing for information to be
[2371] shared across the different groups
[2374] in a way that the data that we have is
[2376] being incorporated
[2378] at the right level and i will no longer
[2381] bother you with the code that's like the
[2383] easy part
[2384] let's just let's just jump straight into
[2386] the results
[2389] here's what the results would look like
[2391] in the complete pulling model
[2392] so i'm showing you now the the radon
[2395] estimates the alpha
[2396] for all counties but now plotted against
[2400] the abundance of uranium uranium in that
[2402] county
[2403] in the complete pooling model where we
[2405] treated every county as equal
[2408] and we made no attempt to incorporate
[2410] uranium levels
[2411] the estimates would ended up look
[2413] something looking something like this
[2414] just all the same
[2418] second we have the no pulling approach
[2421] where each
[2422] county was given its own estimate right
[2424] um
[2425] we ignored the data from the other
[2426] counties we also didn't include any
[2429] information about uranium
[2430] so we ended up with something like the
[2432] plot here which has like very
[2434] uncontrolled variation from county to
[2435] county
[2437] and perhaps if you start this for long
[2438] enough maybe you will be able to
[2440] distinguish a slight correlation between
[2442] uranium and dragon
[2444] but if there's really a correlation
[2446] there our model at this
[2448] stage was not making any attempt to
[2450] capture that
[2453] then we introduce hierarchical modeling
[2455] as a way to
[2456] sharing information between groups and
[2458] also controlling our estimates
[2460] look at that reduction in variance by
[2462] the way it's like uncontrolled
[2464] controlled um but again
[2467] no information about uranium was
[2469] included at this stage right
[2471] so our model cannot really resolve any
[2473] obvious correlations
[2475] then when we include the uranium data
[2479] look at what happens
[2482] now not only am i controlling my
[2484] inferences
[2486] like not only am i sharing information
[2488] between counties
[2489] but having this deeper understanding of
[2491] the structure in the data
[2492] allows me to make very very accurate
[2495] inferences
[2496] by being very careful about my modeling
[2499] approach
[2500] i'm able to really squeeze every drop of
[2502] information out of my data
[2504] and look at the uncertainty bars in the
[2507] in the estimates
[2508] all of the counties basically have the
[2510] same uncertainty that's like very very
[2512] powerful
[2516] okay so hopefully i've convinced you
[2518] that hierarchical models are the right
[2520] approach whenever you have to deal with
[2521] categorical information
[2523] because it allows you to share
[2524] information between groups it prevents
[2527] you from overfitting
[2528] to a small data set and it seamlessly
[2530] incorporates the different data sources
[2532] to the
[2532] at the right level however
[2535] before you decide that you must
[2537] definitely want to jump on this train
[2539] i feel like i have to give you a few
[2541] words of warning
[2543] uh first of all you have to be careful
[2546] about pre-packaged software
[2548] that claims to do claim to do
[2550] hierarchical models for you
[2552] which work by simply doing maximum
[2554] likelihood estimates
[2556] maximum likelihood doesn't really work
[2558] with hierarchical models
[2560] unless you are doing some other happy
[2562] assumptions on top
[2563] and in pre-packed software those
[2565] assumptions will be
[2567] hidden from you so you won't be able to
[2569] question them
[2570] um so if you want to get it right you
[2572] will need a verizon approach and by
[2574] easier modeling is just
[2575] difficult especially in hierarchy in
[2578] hierarchical models
[2579] where the complexity can quickly get out
[2582] of control
[2583] if you think of the pulling that we were
[2584] introducing for the alphas
[2586] you can imagine that now you also
[2587] introduce pulling for the betas
[2589] maybe you allow for different variants
[2591] from county to county
[2593] you incorporate your uranium for each of
[2595] these
[2596] parameters then you can further
[2598] introduce correlations between sulfurs
[2600] and betas
[2602] it quickly gets very overwhelming even
[2604] for this very simple example
[2607] and the mathematical aspect of that is
[2609] really just half the problem
[2610] it's often the easy part because to make
[2613] markov chain monte carlo work
[2614] efficiently
[2615] so that you don't have to wait taste you
[2618] will often have to parameterize your
[2620] model in some very very specific ways
[2622] and knowing the right parameterization
[2625] unfortunately something just comes with
[2628] experience
[2630] all that being said i still recommend
[2634] you jump on the train hierarchical
[2636] models are such a powerful technique to
[2637] have in your toolkit
[2639] and once you learn them you really see
[2642] the opportunity to use them everywhere
[2644] so trust me
[2647] um okay um that's it for the for the
[2650] main part of the talk let's just now
[2652] uh spend a few minutes answering your
[2654] questions
[2655] so let me try to bring the q a here
[2660] um can you please share your github link
[2662] i guess i could have read that at the
[2664] very start of the talk
[2665] um uh we will also be sending you the
[2668] github link
[2668] um via email so you just make sure that
[2672] if you
[2672] just register for the talk i'll be
[2674] sharing you with that one with you
[2677] later but it was
[2682] um no that's the one
[2687] is there a reason you didn't standardize
[2689] the data to
[2691] having a standard normal distribution
[2694] and before the first complete pulling
[2696] model or is it just for brevity in your
[2698] presentation
[2699] um standardizing your data can
[2702] definitely um
[2704] can definitely improve the performance
[2706] of your of your model make it make your
[2708] algorithm work more efficient
[2710] but you don't always have to uh
[2711] sometimes it's a must
[2713] like if you're doing like a gaussian
[2715] process perhaps and
[2717] if you don't standardize things are
[2718] going to go very wrong
[2720] but in this simple example i didn't have
[2722] to bother with standardizing it was just
[2724] too simple
[2726] um so i have another question that says
[2730] can you tell us a little bit more about
[2732] your prior
[2733] for one over sigma being a gamma
[2735] distribution
[2736] uh right let me bring that that slide uh
[2741] here um
[2748] and this one i guess where the sigma is
[2750] given an inverse gamma distribution
[2753] so yeah the notation is a bit weird i
[2755] just mean
[2756] sigma is distributed like an inverse
[2757] gamma and the reason i do that is
[2760] because
[2761] an inverse gamma distribution doesn't
[2764] have any support at zero so i'm saying
[2766] that
[2766] i know there is some variance so the
[2768] variance in my data is not zero
[2771] but what i want to say is like i don't
[2773] know how large it can be
[2775] the inverse gamma distribution has a
[2776] really really flat
[2778] right tail which allows for very high
[2780] values if the data really wants to be
[2782] very noisy that's the reason for that
[2784] prior
[2787] and i have another question that says
[2789] out of interest
[2790] what made you choose non-pyro over stan
[2793] by mc3
[2795] and i never heard of pyro but before i
[2797] used to stand
[2798] and i'm wondering what difference are um
[2802] the reason we choose number numpyr is
[2805] now the
[2806] the default choice here at faculty we
[2808] kind of we actually had meetings and
[2810] analyze all the different libraries and
[2814] just eventually decided that numpyro
[2817] was the more suitable for the kind of
[2819] work that we want to do
[2820] vampire has nice interfaces for doing
[2824] mcmc
[2825] and also for doing variational bass
[2828] if you want to do other kinds of by
[2830] using inference
[2832] and as opposed to something like stan
[2834] for stan is very nice
[2836] but you can only do mcmc and the problem
[2838] with stand for us was that
[2840] stan relies on c plus plus so you need
[2843] to have a c plus plus compiler
[2845] and whenever you are deploying a
[2847] bayesian model it just gets very
[2849] very hard and very tricky engineering
[2852] going on
[2854] so non-pyro is just it's all based in
[2856] python
[2857] and it's very powerful so that's what we
[2860] choose it basically
[2863] um i have another question that says how
[2866] sensitive
[2867] is the amount of pulling to the prior
[2869] that you have so i'm
[2870] i'm guessing this question is like um
[2874] if i change the the prior of an
[2876] exponential one to something different
[2878] is that going to affect the the answer
[2882] the the short answer is that yes you
[2885] will
[2886] affect your answer but it's really not
[2887] that sensible you'd be surprised that
[2889] the posterior that you get after is just
[2891] just indistinguishable from
[2893] what you had before as long as you have
[2896] a
[2897] um a prior that this is not like
[2900] highly informative you know like
[2902] definitely suppressing some values
[2905] um you will you will always end up with
[2907] like distributions that look very
[2909] similar
[2911] of course this depends on the data but
[2913] most of the time that that's the case
[2917] um nice i have uh i think i'll take a
[2920] one last question which says that do you
[2924] always
[2924] need to assume that a single amount of
[2927] pulling
[2928] is the right for all groups might you
[2931] have sometimes many pulling parameters
[2933] for predefined group sets
[2936] um 1.12 groups
[2944] um i am not sure that i'm
[2948] understanding here um
[2952] so the pooling is something that happens
[2954] across groups
[2955] and i think that you are saying that
[2959] maybe you want to pull closer some
[2961] groups and
[2962] the others not pull them such as clothes
[2966] and if i'm understanding right that's
[2968] because
[2969] you maybe have some other information
[2972] about
[2973] about that distinguishes the type of
[2976] group that you have like
[2978] um like in this case a uranium or maybe
[2981] you have some other geographical
[2982] information about the places
[2984] so they can you have some extra
[2985] information and
[2987] the short answer is then no you can
[2990] definitely pull
[2991] separately the different groups that you
[2994] have
[2994] but that means that you have to build a
[2997] slightly more complex structure
[2999] but i think the framework still still
[3002] works out
[3005] um okay um
[3010] let me uh i think we have time for one
[3012] more so let me just find one
[3014] which is nice um
[3017] i have here a question that says
[3021] do you always need to use mcmc i
[3024] recently read about
[3025] variational inference and apparently
[3027] this is quicker for big data
[3029] with more simplistic calculations that
[3031] is right so
[3032] markov chain monte carlo is a is a very
[3035] popular choice because
[3038] in a sense you have some theorems that
[3040] tells you that markov chain monte carlo
[3042] if you get enough samples
[3043] it's going to converge to the right
[3044] answer
[3046] the disadvantage of markov chain monte
[3048] carlo is that it is very slow
[3051] especially in hierarchical models so
[3055] you might want to be looking for some
[3058] other alternatives that do
[3059] variational inference in a quicker way
[3062] one of those is like variational base
[3065] um which is a very popular one it's just
[3067] like kind of approximating your
[3068] distributions with
[3070] other friendlier distributions that you
[3071] can easily sample from
[3074] um i think the problem with variational
[3077] inference
[3078] is that it is not guaranteed to converge
[3080] the right answer
[3082] so sometimes if your model is well
[3084] behaved um
[3086] you can just get away with doing
[3087] variational inference which is going to
[3089] be quicker
[3090] but you have no way of knowing if you
[3093] are getting the right answer so that's
[3095] always it's always the spine of like
[3097] you have the answer but is this right
[3100] and then just to confirm that you're
[3101] right maybe what people do is like
[3103] you also run mcmc once just to um
[3107] get some peace of mind that variational
[3109] base and mcmc are giving you the same
[3110] answer
[3112] um but so yeah then you have to run mcmc
[3116] again and that kind of kind of defeats
[3117] the purpose
[3120] um but variational basis is very cool if
[3123] you manage to like
[3124] tune it well and and have a
[3127] fairly simple model then i think it's a
[3130] good way
[3131] it's a definitely a good option
[3134] um okay so there are many more questions
[3138] but i don't think we have time to go
[3139] through all of them
[3141] so what i'm going to do is just the same
[3143] as last time
[3144] where um i'm just going to keep a log of
[3146] the questions and i will
[3148] send you back a full fully detailed
[3150] answer to all of your questions via an
[3152] email
[3153] and i'll also make sure to share that
[3154] github link on the email as well
[3157] cool so thank you everyone for for
[3160] joining me
[3161] have a nice rest today
[3169] you
