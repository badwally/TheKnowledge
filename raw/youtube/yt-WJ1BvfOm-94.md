---
schema_version: 1
id: yt-WJ1BvfOm-94
type: youtube
title: Predictive Information Criteria in Hierarchical Bayesian Models for Clustered
  Data
url: https://www.youtube.com/watch?v=WJ1BvfOm-94
authors:
- Stan
ingested_at: '2026-05-20T17:36:45Z'
content_hash: sha256:5e57476b96af2a17020d1dbd025d4f9549b71267805b6fed8ed0dc4d9d61c155
domains:
- risksystems
nlm_corpus_ids:
- dee0eae4-b11f-4df2-a418-d10fffd42c7e
wiki_pages:
- wiki/concepts/predictive-information-criteria.md
- wiki/concepts/deviance-information-criterion.md
- wiki/concepts/widely-applicable-information-criterion.md
- wiki/concepts/leave-one-out-cross-validation.md
- wiki/concepts/hierarchical-bayesian-modelling.md
- wiki/concepts/multilevel-models.md
- wiki/concepts/marginal-vs-conditional-likelihood.md
- wiki/concepts/pareto-smoothed-importance-sampling.md
- wiki/concepts/item-response-theory.md
- wiki/concepts/posterior-predictive-distribution.md
- wiki/concepts/mixed-predictive-distribution.md
- wiki/entities/sophia-rabe-hesketh.md
- wiki/entities/edgar-merkle.md
meta:
  channel: Stan
  channel_url: https://www.youtube.com/@stan3394
  duration_seconds: 2688
  caption_track: fetched
  snippet_count: 949
---
[0] I've been talking introduce myself so
[4] very briefly I'm Sofia Garvin esketh and
[7] the talk is about predictive information
[9] criteria for Erica Bayesian models for
[11] custom data and this is joint work with
[14] Stanford who's going to be presenting
[16] some of this and at work oh she's not
[19] unfortunately couldn't make it and I'd
[22] like to thank the organizers for
[23] inviting us
[29] so first I'll define the predictive
[32] information criteria that is the AIC D I
[36] see leave one out I'm showing the
[38] connection to be one out cross
[39] validation then I'll say what I mean by
[42] hierarchical Bayesian models for
[44] clustered data and examples of these are
[46] mixed or multi-level models emmalin's
[49] structural equation models sense and
[52] item response Theory models or IR T's
[56] then for these models is important
[59] distinction between marginal and
[62] conditional versions of the information
[63] criteria so that I'll describe those and
[67] then Dan will illustrate the importance
[69] of making those distinctions through an
[72] example to item response theory or IOT
[75] so what is the target or what are the
[79] information criteria trying to do let me
[82] first introduce some notation the
[85] likelihood is denoted F all the
[88] responses are denoted both by all the
[92] parameters are denoted theta and the
[95] prior I will use P palaces P generally
[98] for probabilities of or densities so
[102] what we want the goal is to assess how
[104] well this model predicts future or
[109] out-of-sample data kind of validation
[111] data that we have
[112] seen yet and one but if you had this
[117] amount of sample data how would we
[119] evaluate the prediction error of our
[120] model well a very popular way of doing
[123] that is through the deviance so that's
[126] minus twice the log of the likelihood
[128] evaluated at the out-of-sample data but
[132] what do we do about theta if we want to
[134] get some prediction error measure so for
[137] the TI see what we do is we plug in the
[140] posterior mean of theta so we get the
[143] plot in deviance which is just minus
[146] twice the dog likelihood for new data
[150] but at the posterior means of parameters
[153] and for the W AIC which is something
[156] more principled as I'm just plugging in
[158] the posterior mean we integrate over the
[160] full posterior that we do compromise by
[163] having to use his point wise predict of
[165] densities here and so we take the
[169] posterior expectation of the point was
[171] predictive densities these can also be
[174] called predictive densities here but the
[179] real target of the TRC and WIC is
[181] actually the expectation of these
[184] prediction errors over the distribution
[187] of future data so for the TI see that
[193] time it looks like this we have the
[196] expectation of a future data but we
[199] can't really evaluate that expectation
[201] because we don't know the generator
[203] generating distribution of the future
[205] data we assume that they come from the
[208] same true model as the observed data but
[210] the whole point is that we don't know
[211] what that one is
[213] and we can't even evaluate this plug in
[216] deviance for one out-of-sample data set
[219] because we don't have any valid
[220] typically we just have one dataset so
[223] what we do is we instead we use the
[227] in-sample plugin deviants so we just use
[231] the data that we have to evaluate the
[233] deviance at the posterior means and of
[236] course that's being overly optimistic
[237] for the prediction error because we're
[239] using the data twice once to estimate
[241] theta and then to evaluate the fit to
[242] the data so we add something to the
[245] prediction error to make it less
[247] optimistic this is also sometimes called
[250] the optimism but in this penalty term
[252] again the PD does the effect of number
[256] of parameters and that's basically the
[259] posterior expectation of the deviance
[262] minus the deviance evaluated at the
[264] posterior expectation of the parameters
[265] and here I'm writing those expectations
[270] and in practice you would evaluate those
[272] when you're doing MCMC as just sample
[276] average of your MCMC drawers but I'm not
[279] going to write all these sums over since
[281] it was to keep the notation simple okay
[284] so for the W AIC the target is the
[289] expectation over future data of the not
[293] predictive density so this is also for
[296] Al PPD and we do this we have the same
[301] problem we don't know what the
[302] distribution of Y is for future data we
[305] don't have a new validation data so we
[307] just use the in sample version of this
[309] and then compensate by using a penalty
[313] term twice TW where PW is the effective
[317] number of parameters which is now
[318] proximate it by the person the sum of
[321] posterior variances of this law point
[325] wise predictive densities and and the
[329] variance with austere variances obtained
[332] by the sample variance of the MCM
[335] each of these about conditional
[338] densities and the stubby ase is
[342] appealing and also kind of it helps them
[345] to applicant to know that it's
[347] asymptotically equivalent to leave one
[349] out cross validation because leave one
[352] out cross validation has the same target
[353] it's also trying to expropriate minus
[356] twice the expected log what was
[359] addictive density and so the important
[365] thing here is in the target is that the
[369] data we condition on in order to learn
[371] about the parameters theta so in the
[373] posterior we condition on the data that
[376] we have but we evaluate the predictive
[378] density on different data new data so
[381] that's kind of the essential idea to
[383] sleep on out that we want to base the
[385] posterior distribution on the data
[388] except for the unit for which we want to
[390] make a prediction yes oh not since you
[393] can see that that's trying to we now
[395] don't have to penalize reusing the data
[396] twice so this Y minus I is the data
[401] except for all the units except unit I
[403] does have the training data from which
[406] we learn about theta but you can see
[408] that to implement this is
[410] computationally prohibitive because we
[413] would have to run MCMC for each of these
[416] training data sets so it's only really
[418] feasible for very tiny data sets like
[420] the famous eight schools data very good
[423] idea to run the same time so what
[428] standard practice is some PS is to be
[434] too smooth to point something and the
[436] idea of important sampling is that we
[439] can get away with doing MCMC only once
[442] so we're using the wrong posterior
[444] conditioning on all the data but then we
[446] compensate
[447] having this importance ratio here which
[449] is the posterior that we want divided by
[452] the one that we appreciate but we're
[454] using and this doing this properly out
[458] doing this sort of naive array can be
[460] very noisy so that's why this parameter
[462] smoothing is needed and I'm not going to
[464] go to details because this very nice
[465] paper you can refer to the Vitara gallon
[467] agave 2017 okay so but I'm going to
[473] apply these ideas to hierarchical
[475] Bayesian models and these are defined in
[477] stages so in this case three stages and
[479] I'm going to illustrate by using a
[481] multi-level modeling example starting at
[484] the last page so the model for the
[487] response I J for unit I entrusted
[490] cluster chasers can be custom data is a
[495] normal the models basically a normal
[498] distribution site with mean alpha plus
[500] theta J and barracks Sigma squared and
[502] the important thing here is that Zeta J
[504] has a J subscript so it is a variant for
[507] a mature or in this case we can say it's
[509] a varying intercept and this this
[513] parameter has a normal prior
[515] distribution with mean 0 variance sigh
[518] and what makes this a hierarchical
[522] Bayesian model is that the prior for
[524] this parameter Zeta depends on a
[526] parameter design which we like called a
[528] hybrid parameter and we can learn about
[531] this parameter the prior from the data
[533] so if you're not Bayesian this actually
[536] completes the model formulation and and
[542] the only thing that a non-base annoyed
[545] about non-bayesian would be worried
[547] about here is that there is a random
[549] trauma term zito J and the way they
[553] would get around it is by calling it a
[554] random variable instead and because it's
[557] not observed as and making
[559] and in many ways I think it would be
[561] useful patients would use that term
[563] because it's a special Pharma term it's
[565] a bit different than the other
[565] parameters we can learn about its
[568] distribution from the data okay so but
[572] to make this model fully basing we have
[574] to specify tyres for all the parameters
[576] including the hyper for our website and
[579] that's called the hyper prior but in
[582] this in this talk I will use some
[584] generic notation for these kinds of
[586] models so I'm just use F C for the
[590] conditional density of Y given Z done
[593] and the other parameters or the other
[595] parameters is accept website are in the
[598] vector Omega and then I use G for the
[600] privacy to give him side and then P for
[603] thee for the other clients and see that
[606] Jade could in principle be multivariate
[608] so therefore it's bold these are
[611] sometimes called direct parameters
[612] because the end of the video directly
[614] they could be daring intercepts of
[617] varying coefficients as we've seen in a
[618] multi-level model but generally they
[621] could be make there was in structural
[623] equation models or IRT and in that case
[626] it's a cluster data's it's like a
[628] different meaning so if you in an item
[631] response Theory the cluster would be a
[634] person Y is a multivariate vector for
[638] responses to different items so the
[640] units are I become the items and the
[642] person becomes the cluster and in a
[645] Bayesian setting is sort of ambiguous
[647] whether you think of Z so J as
[648] parameters like there was but I think
[650] typically you think of them as
[651] parameters okay so for this hierarchical
[657] Bayesian model there are two versions of
[659] the likelihood the conditional
[661] likelihood is conditional on the lake
[663] there was data so it's the product of
[668] trusted contributions and the cluster
[670] contributions factorize into a product
[673] of unit contributions because given the
[676] leg there was
[677] independent and this is kind of the
[680] natural definition of the likelihood in
[682] Stan or other basing software in the
[686] model block you would - I saw the a bit
[689] of the tutorial would say possum
[691] why is possum or something and that
[693] would be conditional on Zita
[698] in contrast a maximum likelihood we
[702] integrate out the CETA
[704] so its marginal over the label
[706] terrible's not matter of everything like
[708] can basically technology sometimes
[711] everything like in the deep end the base
[713] factor but here with us we still
[715] conditioned on the parameters Omega and
[717] psy but we integrate over the
[719] distribution of the latent variable so
[721] this is the prior the name variables and
[723] this is the likelihood that's used in
[725] maximum likelihood estimation of these
[727] Mobile's so if you use elmer and are
[729] that's what's being maximized and the
[732] only parameters for non-bayesian are the
[734] omega n PSI because the Zetas are maybe
[736] their wills so in a way the traditional
[740] like you were treating the Zetas as if
[742] they are parameters and then the
[743] marginal likelihood we're treating the
[744] message they are kind of missing data
[748] okay so in the example that I've looked
[753] at the kind of random intercept example
[756] the marginal distribution has a closed
[759] form
[759] it's basically for one cluster the
[762] responses that say students in school
[764] the joint probability of all these
[767] responses is not very normal with mean
[770] alpha and variance side plus T does get
[774] and with covariance of size so the
[778] correlation between any two students
[780] would be what you may know is the
[782] intraclass correlation beside pardon
[784] Esmond yeah so that's the marginal
[787] likelihood okay so since there are two
[791] versions of the likelihood and and
[795] therefore the deviance then obviously
[797] there will be two versions of the DI c1
[800] then the conditional D I see the
[803] definition we saw before we just plug in
[805] the conditional likelihood everywhere
[807] where we see a likelihood and so this is
[810] what's produced by most spacing software
[815] in the mountain of dscp we just put in
[818] the margin elected everywhere and this
[822] is this requires additional computation
[825] because the marginal likelihood is a bit
[828] more complex so it's not really
[831] available most days in software but our
[835] co-authored Merkel has implemented this
[838] in LaVon which is an hour package that
[841] exploits the our package LaVon which is
[844] for structural equation modeling to
[846] evaluate the marginal likelihood
[848] forgiven drawers of the parameters and
[853] but when the likelihood is not tractable
[856] for example when you have binary
[857] responses then you can use adaptive
[861] quadrature and we developed a man a
[863] version of that that's very efficient
[864] when we have MCMC drawers available ok
[871] and with that basically done we'll use
[873] that in the IOT example okay so for the
[877] W AIC there are two versions meritless
[879] Naraku Co Bayesian model of the
[881] predictive distribution that's so
[883] central to the welc the most obvious one
[886] is probably the posterior predictive
[888] distribution where we just take that
[891] conditional predictive distribution
[895] given zeta and integrate that over the
[898] posterior of omega and sita given Y so
[902] and we can get rid of the Sai here by
[906] integrating it out but waiting what I
[908] want to show is a blue that this
[910] posterior of Y given Zeta
[914] so you see if I give in my even after we
[920] condition on our meager side which
[922] themselves obviously we learn about
[925] these from the data
[926] even after we condition on them Zha
[929] depends directly on the responses that
[931] we have for cluster Jane yeah so that's
[937] an important thing to remember so when
[939] we used the posterior predictive
[940] distribution we're really checking how
[943] predictive our model is for new units
[945] from the existing clusters because we're
[947] learning from the existing clusters the
[950] other day that have been up for those
[951] clusters here whereas if we use the
[955] marginal posterior distribution so this
[959] thing in square brackets I so sorry if
[963] we use the marginal posterior
[964] distribution would that mean L so this
[968] is the mixed predictive distribution I'm
[969] sorry and this was introduced by Cameron
[972] magnets term in 1996 and the idea here
[975] is that we used the marginal likelihood
[977] instead of the conditional likelihood
[979] and the first if I expand out the
[981] marginal likelihood into this integral
[983] you can see that now Zita comes from the
[987] prior so we're not learning about Zita
[989] directly from there from the data we
[991] have for the cluster J so this
[995] effectively is a prediction for a new
[998] unit in a new cluster so if you were for
[1001] example a posterior predictive checking
[1004] then in the for the posterior predictive
[1008] distribution you would be using the
[1010] posterior samples of Zita
[1012] but then generate new data wine but if
[1015] he is the mixed predictive distribution
[1017] then you use posterior samples of on the
[1019] upside but he would sample mutant and
[1022] I'm given the news either you
[1024] yes sir that's the mix predictive
[1026] distribution and that's appropriate for
[1028] inference of swinging clusters because
[1030] we're not conditioning directly on the
[1033] responses we have for the cluster okay
[1038] so correspondingly then there are two
[1040] versions of the waa I see the the
[1043] conditional waa RC uses the posterior
[1046] predictive distribution so we
[1049] conditioning so we're learning directly
[1051] about ZJ from the data we have for
[1054] cluster Jane and therefore this
[1056] corresponds to leaving one unit out
[1059] cross validation so that's a low low
[1064] Hilo or something like that so this
[1069] corresponds to we're leaving out the
[1072] unit in learning about Zeta and Omega
[1074] but not the entire cluster in contrast
[1080] if we do and our claim this is this is
[1082] what you get automatically in if you
[1086] stand together with a loop package but
[1090] the marginal W AIC uses the marginal
[1095] uses the mixed predictive distribution
[1097] here so here we don't learn about zito j
[1102] directly from any data that we have for
[1104] the cluster so it's it's much closer to
[1108] leaving the entire cluster out in the in
[1111] the deep on out method and so we call
[1113] that loop only one cast around
[1115] cross-validation and this one we can
[1122] compute also using the loop package but
[1124] we have to provide the marginal
[1126] likelihoods which can be sometimes
[1129] difficult to do but it's automated and
[1131] blonde now you can ask the bomb to do it
[1133] for you so is this ever used this much
[1139] see well is actually hinted at in
[1142] several places for example in Galvin
[1145] from in Vitaly that there's a
[1147] distinction hierarchical Bayesian models
[1149] about how you define these things but it
[1153] has been used for on clustered data and
[1155] by by the appellant Miller and all that
[1159] as far as we know it hasn't really been
[1161] used for clustered data but there's
[1163] already people in the audience so maybe
[1165] you can correct me
[1166] so what somebody can correct me on that
[1168] you will see an application of this to
[1170] clustered data presented by down in a
[1173] minute but before that I want to make a
[1176] few comments about the special case of
[1178] untrusted data so just to start before
[1181] he comes it takes over for me okay so in
[1186] the untrusted case this posterior
[1189] predictive distribution really collapses
[1191] to the prior predictive distribution or
[1193] if you want to leave one out there's no
[1194] distinction between leaving a unit or a
[1196] cluster out yeah so these things kind of
[1199] so here if you look again at the
[1201] posterior predictive distribution if we
[1205] want to make predictions for new data YJ
[1207] that we can't condition on that exact
[1210] data points so this is exactly what I
[1212] wrote before except for the eyes
[1214] subsequent now we can condition on this
[1216] YJ because we don't have anyone to
[1218] predict it so so we get rid of that and
[1224] then once we done condition on YJ than
[1228] Zetas oh he also becomes independent of
[1234] independent of Omega given sign so then
[1237] we're back to the expression for the
[1239] mixed predictive distribution so really
[1244] it doesn't actually make sense to two PS
[1247] I asked to do with the conditional
[1249] likelihood at this point was made by
[1253] Milla
[1253] 2018 that's so great but that's still
[1256] impressed that we actually just
[1257] discovered information for the stroke
[1260] and they make that thing
[1262] that start that point very strongly but
[1264] this whole concept of leave one out if
[1267] you leave the unit out then you don't
[1269] have any information about Z today then
[1272] you can't really use the conditional
[1273] likelihood it has to be the marginal one
[1278] okay so just a brief example that many
[1283] of you will be familiar with is the
[1285] eight schools data which is like a
[1287] meta-analysis of each school we have one
[1289] data point YJ that represents the s an
[1292] estimate of an effect size namely how
[1294] effective some SAT preparation program
[1296] has been and then we have a Sigma J
[1299] which which is the corresponding
[1300] standard error and we use a kind of
[1302] random effects meta-analysis the true
[1306] effect sizes
[1309] Zita j to vary with variance tau squared
[1314] and we was the overall effect size
[1317] across all the eight schools so the
[1320] conditioner likeness is very obvious
[1322] it's just a normal distribution with
[1323] with means either j and very sigma j
[1327] squared and the marginal likelihood is
[1330] also has closed form here so when we
[1333] integrate over Zeta we the mean the
[1336] amount of languages the population need
[1339] across the eight schools or across the
[1341] population of schools more than a maybe
[1343] and the variance is tau squared plus
[1346] Sigma J square so in the paper by veturi
[1352] Gelman and gari they found that the the
[1355] tau squared supported by the data is
[1358] fairly small and and so that case is
[1360] difficult to see much action so they
[1363] also can affect the data that I just
[1365] multiplying by some scale factor s and
[1369] when you keep Sigma J squared that means
[1371] that the data that looks like towers
[1374] largest sort of a scenario of tau will
[1377] be larger and the price Vegeta will be
[1379] more weak
[1380] so when they use the scale factor for
[1384] they found that the difference between
[1388] the W AIC based on the conditional
[1391] likelihood
[1393] and the leaf one out is Israeli plant so
[1398] 68 verse 36 so so the WIAC becomes a
[1402] terrible approximation to leave one out
[1404] and they did leave one out exactly
[1406] because it's only eight spools so we
[1408] found the same thing but when you use
[1413] the marginal wasd which was not
[1415] considered by the tower are in 2017 they
[1418] actually have something else pretty
[1420] close to the leave one out cross
[1421] validation okay so I'm gonna hand over
[1424] to Dan now
[1448] all right so I'm going to talk over an
[1450] example of using marginal information
[1452] criteria and the context I usually work
[1454] on which is item response theory models
[1457] the example what I'm going to work with
[1460] is too late in the regression rush model
[1463] briefly it's a model for the probability
[1467] that somebody responds to a question say
[1469] on a tests correctly given some person
[1475] specific parameters and some vitamins
[1477] specific parameters so the probability
[1480] of the correct response threat response
[1482] is y equals 1 or an incorrect response y
[1486] equals 0 depends on a person specific
[1490] parameter that is theta which is the
[1492] ability for person change and an item
[1495] specific parameter that is Delta the
[1497] difficulty for item I so the probability
[1500] of a correct response is then the
[1503] difference between the two passed
[1505] through an inverse logit link function
[1509] the latent regression part of the model
[1511] comes in the prior of theta where it's
[1516] assumed to be drawn from a normal
[1517] distribution with the mean that depends
[1520] on this regression prediction so X is a
[1524] vector a person related covariance and
[1526] lambda is a vector of regression
[1529] parameters lastly we also estimate the
[1532] standard deviation for theta as in the
[1537] side we have the webpage put together
[1539] for education related examples in stem
[1542] it includes links to articles also some
[1545] case studies and tutorials we've written
[1547] as well as linking to my our package for
[1551] IRT using Stan which is called head
[1552] stand when I use adaptive quadrature to
[1558] get marginal likelihoods
[1559] it's convenient to reformulate the model
[1561] in this way though it's mathematically
[1563] equivalent to what I just showed what
[1566] I've done is replaced the in person
[1568] ability parameter by a combination of
[1572] these
[1572] things we have the latent regression
[1575] prediction again and a person specific
[1578] which residual azita J being a residual
[1582] zina J has a prior mean of zero and the
[1587] same standard deviation as before I've
[1591] also put on the slide the other priors
[1594] for the non-hierarchical priors when I
[1597] write t3 here what I mean as a student T
[1599] distribution with a shape parameter of
[1602] three I consider these to be weakly
[1605] informative priors except of course for
[1607] the regression coefficients what's
[1609] weakly informed and depends on the scale
[1611] of X so that's something we have to keep
[1613] track of so to obtain information
[1618] criteria in the setting for AIC or the
[1621] lead one out approximation what I need
[1624] is the likelihood for each observation
[1626] at each posterior draw so in the
[1631] conditional case that's given here and
[1634] that is equal to the probability I just
[1636] showed on the last slide the only
[1638] difference is by plugging in parameter
[1641] values of their posterior draws that is
[1644] this subscript indicating the posterior
[1646] drop for the marginal case there's a
[1650] change in the unit of analysis the
[1653] marginal likelihood is for clusters in
[1655] this case the cluster is a person each
[1658] person sort of owns a cluster of their
[1660] responses to the various questions so to
[1663] obtain that marginal likelihood we use
[1666] the conditional likelihood for a
[1668] person's response to a question and
[1671] multiply that over all the questions for
[1673] a given person then we integrate out the
[1677] residual from that product and over its
[1680] prior distribution and that gives us the
[1683] marginal likelihood so the marginal
[1686] likelihood protect depends on sy which
[1689] is the standard deviation of the
[1691] researcher
[1692] whereas the additional depends on xenon
[1695] Sita the residual itself of course it's
[1699] not so easy to do that because it's a
[1701] logistic model there's not an analytical
[1704] solution for that integral so instead we
[1707] use an adaptive quadrature scheme for
[1711] that we need a few things firstly we
[1714] need the posterior main in the posterior
[1716] standard deviation for each residual so
[1720] let's call those mu and V and then we
[1725] also need a set of standard Gaussian
[1727] quadrature notice these can be obtained
[1730] from several different references I use
[1733] in our package step mod to get them than
[1736] just that this is just kind of like
[1738] approximating a standard normal
[1740] distribution with a histogram so each of
[1744] that the quadrature node M has a weight
[1748] call that W and a location call that
[1751] case what I'd like to do is adapt them
[1756] to put them closer to the posterior for
[1758] zina
[1759] so to do that I update the location like
[1762] this changing the scale by multiplying
[1766] by the posterior standard deviation for
[1768] the residual and then adding the
[1770] posterior mean having changed the
[1774] location of the nodes I also have to
[1775] change the weight and I do that using
[1778] this really ugly equation here I'm not
[1781] going to try to walk through it right
[1782] now but something interesting about it
[1785] is that it depends on side the standard
[1790] deviation of the residuals so that's a
[1792] parameter in the model and it changes
[1795] from iteration to iteration so it's kind
[1797] of neat about that is that the weights
[1799] change between posterior draws for a
[1802] given cluster but the node locations are
[1804] always the same
[1805] cluster anyhow having those adapted
[1810] quadrature nodes we can approximate the
[1812] marginal likelihood like this we again
[1815] have the conditional likelihood but
[1818] instead of plugging in Zita we plug in
[1821] the note location multiply that together
[1824] for each item a person responded to and
[1826] then weighed that by the weights
[1829] associated with that node do that for
[1832] every node and add them together you
[1834] have an approximation for the marginal
[1836] likelihood so let's use that to obtain
[1840] marginal information criteria I'm going
[1843] to use this example data it's a verbal
[1846] aggression data it's based on a question
[1848] they're given to people to assess their
[1851] propensity towards a verbal aggression
[1853] it has 20 more questions on it an
[1857] example is a bus fails to stop from me I
[1859] would want to curse so each question has
[1862] this frustrating situation and then a
[1865] possible reaction to that that situation
[1868] people responded for those questions
[1871] with either yes perhaps or no and I've
[1874] coded yes and perhaps as correct it's
[1877] correct if you're verbally aggressive
[1880] and then no is coded s incorrect 316
[1886] people responded they filled out this
[1889] questionnaire and as I mentioned there
[1891] is 24 questions along with that are 2
[1895] covariance related to the people the
[1898] first one was an indicator variable for
[1900] whether or not the person is male I have
[1903] changed that to be contrast coded so it
[1905] takes a value of 0.5 and negative
[1907] five the other variable is their score
[1912] on a separate measure of what is called
[1914] trait anger and I play minesweeper go to
[1917] that it now has a mean of zero and a
[1919] standard deviation of 0.5 I did that so
[1922] that the parameters in lambda they will
[1928] be associated with variables of the
[1930] correct scale so now that prior will be
[1931] sensible what I would do is fit five
[1936] different versions of the latent
[1938] regression Rosch model the difference
[1941] between them will only be what
[1942] covariance I put in it so the first
[1945] model will have no covariance it's just
[1948] going to include the intercept in the
[1949] lady regression the second model
[1952] includes the anchor variable the third
[1954] the male variable the fourth includes
[1957] both and fifth includes both and their
[1960] interaction
[1962] I'll look pain 10,000 posterior draws
[1965] for each model and that's a huge number
[1967] it is a great deal menu than more than
[1970] is needed to get accurate and that good
[1975] understanding of the parameters however
[1978] these information criteria are highly
[1981] susceptible to Monte Carlo error and so
[1983] I'm obtaining a huge number of draws to
[1985] stabilize those estimates I'm going to
[1989] get both conditional and marginal
[1991] information criteria and for the
[1992] marginal case I'm going to use eleven
[1994] adaptive quadrature nodes lastly I'm
[1998] going to replicate all of this ten times
[2000] so we can see in an empirical sense how
[2003] much the results vary due to Monte Carlo
[2006] error and here are results I'm showing
[2011] information criteria estimates for di CW
[2014] AIC and the lead one out approximation
[2016] on the top is for the results with the
[2020] condition
[2021] versions on the bottom for the marginal
[2022] and then along the x-axis results for
[2027] the replications are clustered by model
[2030] in the marginal ABS art let's start with
[2033] the conditional in the conditional case
[2036] the information criteria estimates still
[2038] have a high degree of Monte Carlo error
[2040] even after the ten thousand posterior
[2042] draws so if you're doing this sort of
[2044] thing where you use information criteria
[2046] to pick a favorite model you're going to
[2049] have a bad day in the conditional case
[2051] you'll select a different model every
[2053] time you run the analysis it happened to
[2056] me that's how I know this is a problem
[2059] in the marginal case we have a good deal
[2062] more stability but it did require 10,000
[2065] posterior draws to get there however we
[2069] can say that consistently model 4 is
[2072] chosen as the favorite so the Marshall
[2077] case has this better property that it's
[2079] more stable but for this particular
[2082] problem of trying to choose a set of
[2084] predictors related to the person it's
[2085] also the only one that makes sense the
[2089] conditional information criteria are
[2091] making an inference about the predictive
[2093] accuracy of the model but as as though
[2095] the model is going to be fit to new data
[2097] from the same people and the same
[2100] questions what I need is the inference
[2103] that comes from the marginal case where
[2104] I'm marginalizing over the person's
[2106] distribution so I'm making an inference
[2108] about new data that might come from new
[2111] people so since I'm using a latent
[2117] regression on those covariants that's
[2119] the relevant part to look at lastly we
[2124] can look at rather than the whole of the
[2127] information criteria estimates just the
[2129] penalty parts or what you might call the
[2133] effective number
[2133] parameters so this plug is laid out in
[2136] the same way as the previous one but
[2139] I've added to it horizontal lines to
[2142] indicate the number of parameters in
[2144] focus or another way to think about that
[2147] is the maximum the penalty term we would
[2150] expect to be so for all the conditional
[2154] models the number of parameters I would
[2156] say that are in focus are 339 that is 24
[2162] parameter specific to the items and 300
[2165] paren 316 parameters specific to the
[2168] persons minus one because I can
[2170] strengthen the item difficulties oh the
[2175] results for the conditional case are
[2176] well below that and the reason for that
[2179] is that prior information reduces the
[2182] number of effective parameters and for
[2185] the person specific parameters we have
[2187] that hierarchical prior that is
[2189] informative so the number of effective
[2192] parameters is reduced and noticeable
[2193] extensive in the marginal case the
[2197] number of effective sorry the number of
[2200] parameters in focus varies from model to
[2203] model
[2203] it's the count of the item parameters
[2206] plus the latent regression parameters
[2209] plus the parameter for the standard
[2212] deviation of the residuals so that will
[2216] vary between 25 and 28 depending on the
[2220] model and for the marginal case the
[2222] actual estimates obtained are much more
[2226] similar to the number of parameters in
[2228] focus that's what I've got from my
[2232] section
[2252] okay so I guess they're just freaking
[2255] gluttonous but it's important to make an
[2258] informed decision between marginal and
[2260] conditional versions of the information
[2261] criteria but people just tend to do what
[2264] comes out of software without being
[2266] aware of the issues the marginal we
[2270] would argue that the marginal
[2271] information criteria are generally more
[2273] justified than the conditional ones one
[2277] reason is that maybe the second one is
[2279] more useful as Dan mentioned that we
[2283] want to generalize to other people in
[2285] the case of IRT especially when our
[2288] model an important aspect of the model
[2290] we might evaluate is what predictors to
[2292] use for verbal aggression then we want
[2296] to see how predictive those predictors
[2299] are for future people and not for the
[2302] other people that we have in the data so
[2304] but also and and so basically when we
[2307] want to evaluate the form of the prior
[2309] procedure which may include covariance
[2310] then then it seems like we have to use
[2313] the marginal version of the information
[2314] criterion there are also theoretical
[2319] problems with the conditional version of
[2321] the information criterion one of the
[2323] them I talked about very briefly in the
[2326] unplastered case it doesn't really make
[2328] the sense to think of it as some kind of
[2329] new one out cross validation there are
[2335] also two problems I didn't mention
[2337] before that so that were pointed out by
[2340] Millar and that is that the conditional
[2343] version of the W AIC doesn't meet the
[2347] regularity conditions that are necessary
[2349] to show that asymptotically it reaches
[2351] the right target one of the those
[2353] conditions is that the distribution of
[2356] those pieces of data has to be identical
[2358] I am Sonia
[2359] they'll have to be identically
[2361] distributed but the conditional
[2364] distribution depends on Z today so theta
[2367] J's often the means so each Tito J has
[2369] different mean and the other problem is
[2372] that the number of parameters increases
[2373] with the sample size a similar issue has
[2377] been pointed out by Plummer not been
[2379] 2008 for the DI see when you use the
[2382] conditional version but you know again
[2385] that the number of parameters increases
[2387] with a sample size and therefore the
[2388] penalty term doesn't approximate the
[2390] that optimism very well and using the
[2393] data twice so i think thats related to
[2396] the incidental parameter problem and
[2398] maximum likelihood you know in the
[2400] number of parameters increases better
[2402] sample size and then an illustrator to
[2404] show that there was there some empirical
[2406] problems with the conditional
[2408] information criteria that they they have
[2411] even large Monte Carlo errors than the
[2413] marginal ones that was even more
[2416] pronounced in the same example that we
[2419] discussed them and paper that goes along
[2420] with the stock okay I'm just gonna
[2423] really not very much know you know and
[2426] then also that WSC is a poor
[2429] approximation to the leaf one out and
[2431] that was also something could see in
[2432] Danis slides okay so here the three key
[2435] references to other people that relate
[2437] to our talk the first to talk about
[2440] marginal versions of WeSC but in the
[2444] case of my cluster Tatum and the last
[2446] one you probably all know because it's
[2448] the one that blue is based on our
[2450] package and then they'll hear the other
[2453] papers rattling much and this is the
[2456] tape that goes with the talk it's going
[2459] to be in our drive any minute just
[2462] putting some fun finishing touches on it
[2464] and much of this work is based on Dan
[2468] first dissertation and the levant
[2470] package is published or isn't press
[2474] something
[2474] etc and really this was another mention
[2478] of that website on education examples
[2480] where you can find some of the code and
[2481] I guess we'll make the code away with
[2483] the place to the talk there and so on
[2485] but I would also like to ask you if you
[2487] know if you have any case studies or if
[2490] you know of any papers that you stand in
[2492] education research we would like to link
[2494] to those things on this website so thank
[2497] you
[2498] [Applause]
[2527] so the question I had is regarding using
[2535] conditioner marginal information
[2537] criteria it seems that it depends on
[2540] whether I want to make predictions for
[2543] individuals or predictions for
[2546] individuals already have data on and
[2549] since I'm going to be using different
[2551] information criteria does that mean that
[2552] I might be using a different model for
[2556] within and out of sample prediction
[2567] okay so for out-of-sample predictions if
[2571] you leave the cluster out you
[2572] automatically have to use the marginal
[2573] version for in south of predictions you
[2576] have the choice between the marginal and
[2577] conditional versions and then I think
[2579] you would have to choose the one that's
[2580] appropriate for the influences you want
[2582] to make so if you want to generalize to
[2583] new clusters you would use the marginal
[2586] version and I would like to mention
[2588] there's a paper by by Galman on Wang
[2591] where they is a hierarchical Bayesian
[2595] model where the clusters are actually
[2597] state and income bracket combinations or
[2601] something like that and as to do with
[2602] voting predictions and then I guess he
[2606] wanted to take for these states and
[2607] these income brackets so that's an
[2610] example where you probably don't want to
[2611] use the marginal so they correctly
[2614] they're use the conditional version of
[2616] the information criterion so we're about
[2622] to add a one dimensional integrator to
[2624] stand with that let you get rid of this
[2627] approximate know you've got so you're
[2632] saying you're one dimensional a degree
[2633] does not approximate well it's a
[2636] numerical integrator but we'll get to
[2638] control the error okay so with adaptive
[2640] prototype that's also what we can do is
[2642] we can choose the number of nodes and so
[2644] we can make their a small but but we're
[2646] thrilled if stab does it that's great
[2649] yeah that got a limb very soon
[2661] but if it's success if the user can if
[2665] it's straightforward to use your
[2666] one-dimensional integrator to to
[2670] evaluate this marginal likelihood
[2671] illusions then it will be useful yes sir
[2676] we have time for one more question thank
[2682] you very much
[2683] [Applause]
