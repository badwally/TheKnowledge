---
id: pdf-danny-hernandez-2025-measuring-the-algorithmic
type: pdf
title: Measuring the Algorithmic Efficiency of Neural Networks
url: ''
authors:
- Danny Hernandez
- Tom Brown
ingested_at: '2026-04-29T16:16:37Z'
content_hash: sha256:05892934c137d50ad0759d725c1e32c78a9cb298aac8e3cc8ab0d2d0fb80caf9
source_path: raw/pdf/pdf-danny-hernandez-2025-measuring-the-algorithmic.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 20
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__8c18ea1c.pdf
published_at: '2025'
---
Measuring the Algorithmic Efficiency of Neural Networks
DannyHernandez⇤ TomB.Brown
OpenAI OpenAI
danny@openai.com tom@openai.com
Abstract
Three factors drive the advance of AI: algorithmic innovation, data, and the amount of
computeavailablefortraining. Algorithmicprogresshastraditionallybeenmoredifficult
to quantify than compute and data. In this work, we argue that algorithmic progress has
an aspect that is both straightforward to measure and interesting: reductions over time
in the compute needed to reach past capabilities. We show that the number of floating-
point operations required to train a classifier to AlexNet-level performance on ImageNet
hasdecreasedbyafactorof44xbetween2012and2019. Thiscorrespondstoalgorithmic
efficiency doubling every 16 months over a period of 7 years. Notably, this outpaces the
original Moore’s law rate of improvement in hardware efficiency (11x over this period).
Weobservethathardwareandalgorithmicefficiencygainsmultiplyandcanbeonasimilar
scale over meaningful horizons, which suggests that a good model of AI progress should
integratemeasuresfromboth.
⇤DannyHernandezledtheresearch.TomBrownpairedoninitialexperiments,scoping,anddebugging.

Contents
1 Introduction 3
1.1 MeasuringalgorithmicprogressinAIiscriticaltothefield,policymakers,andindustryleaders 3
1.2 Efficiencyistheprimarywaywemeasurealgorithmicprogressonclassiccomputerscience
problems. Wecanapplythesamelenstomachinelearningbyholdingperformanceconstant 3
2 RelatedWork 4
2.1 AlgorithmicprogresshadsimilarratetoMoore’sLawinsomedomainsoverdecades . . . . 4
2.2 Linearprogramminggainswerewell-defined,steady,andfasterthanMoore’sLawfor21years 4
2.3 184xreductionintrainingcost(indollars)togettoResNet-50performancesince2017 . . . 5
2.4 Wecanestimatecostly-to-observealgorithmicefficiencyimprovementsthroughscalinglaws 5
2.5 Total investment in AI through private startups, public offerings, and mergers/acquisitions
wentup5xbetween2012and2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3 Methods 6
3.1 Mainresultprimarilybasedonexistingopensourcere-implementationsofpopularmodels . 6
3.2 Wemadefewhyperparameteradjustmentsbetweenarchitecturesanddidminimaltuning . . 6
4 Results 7
4.1 KeyResult: 44xlesscomputeneededtogettoAlexNet-levelperformance . . . . . . . . . . 7
4.2 FLOPsbasedlearningcurvescanhelpclarifycomparisonsbetweenmodels . . . . . . . . . 9
4.3 We observed a similar rate of progress for ResNet-50 level classification performance and
fasterratesofefficiencyimprovementinGo,Dota,andMachineTranslation . . . . . . . . . 9
5 Discussion 10
5.1 We attribute the 44x efficiency gains to sparsity, batch normalization, residual connections,
architecturesearch,andappropriatescaling . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.2 It’sunclearthedegreetowhichtheobservedefficiencytrendsgeneralizetootherAItasks . 11
5.3 Whynewcapabilitiesareprobablyalargerportionofprogressthanobservedefficiencygains 12
5.4 We estimate a 7.5 million times increase in the effective training compute available to the
largestAIexperimentsbetween2012and2018 . . . . . . . . . . . . . . . . . . . . . . . . 12
5.5 It’spossiblethere’sanalgorithmicMoore’sLawforoptimizationproblemsofinterest . . . . 14
5.6 ResearchprovidesleadingindicatorsofthefutureeconomicimpactofAI . . . . . . . . . . 15
5.7 Majorlimitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 Conclusion 15
7 Acknowledgements 16
A CalculationsforefficiencyimprovementsinGo,Dota,andMachineTranslation 18
B Calculationsforefficiencyimprovementsinimageclassification 19
C Accuracyachievedinrelevantmodels 20
2

1 Introduction
1.1 MeasuringalgorithmicprogressinAIiscriticaltothefield,policymakers,andindustryleaders
There’swidespreadagreementthere’sbeenimpressiveprogressinAI/MLinthedomainsofvision, natural
language,andgameplayinginthelastdecade [Krizhevskyetal.,2012,Xieetal.,2016,Silveretal.,2018].
However,there’smassivedisagreementastohowmuchprogressincapabilitiesweshouldexpectinthenear
and long term [Grace et al., 2017]. For this reason, we believe measuring overall progress in AI/ML is a
crucialquestion,becauseitcangroundthediscussioninevidence. MeasuringAIprogressiscriticaltopoli-
cymakers,economists,industryleaders,potentialresearchers,andotherstryingtonavigatethisdisagreement
anddecidehowmuchmoneyandattentiontoinvestinAI.
Forexample,thecomputeusedbythelargestAItrainingrunsperyeargrewat300,000xbetween2012and
2018 [Amodei & Hernandez, 2018]. Given the divergence from the past trend of approximately Moore’s
Law level growth for such training runs, [Sastry et al., 2019] suggests policymakers increase funding for
computeresourcesforacademia,sotheycancontinuetodothetypesofAIresearchthatarebecomingmore
expensive. MeasurementsofAIprogressinformpolicymakersthataremakingsuchdecisions.
Hardwaretrendsarerelativelyquantifiable. Moore’sLawexplainsmuchoftheadvancefrommainframes,to
personalcomputers,toomnipresentsmartphones[Moore,1965]. Bettermeasurementofscientificprogress
hasthepotentialforalotofimpactonavarietyoffronts. Giventheexistingunderstandingofkeyhardware
trends,wewereprimarilyinterestedinmeasuresthatrepresentedexclusivelyalgorithmicimprovementthat
couldhelppaintapictureoftheoverallprogressofthefield.
Wepresentmeasurementsofalgorithmicefficiencystateoftheartsovertimethat:
1. Areinformativetoawideaudienceofdecisionmakers
2. Helpmeasurenovelcontributionsproducedwithsmalleramountsofcompute
1.2 Efficiencyistheprimarywaywemeasurealgorithmicprogressonclassiccomputerscience
problems. Wecanapplythesamelenstomachinelearningbyholdingperformanceconstant
Inaclassiccomputerscienceproblemlikesorting,algorithmicqualityisprimarilymeasuredintermsofhow
cost asymptotically increases with problem difficulty, generally denoted in Big O Notation. For example,
quicksort[Hoare,1962]hasO(nlogn)averagecostintermsofoperationstofindaperfectsolutionwhereas
manysortingalgorithmsareO(n2)(wherenisthelengthofthelisttobesorted). It’simpracticaltoperform
similaranalysisfordeeplearning,becausewe’relookingforapproximatesolutionsanddon’thaveascleara
measureofproblemdifficulty.Forthesereasons,inmachinelearning,algorithmicprogressisoftenpresented
intermsofnewstatesoftheart, likea1%absoluteincreaseintop-5accuracyonImageNet, ignoringcost.
It’sdifficulttoreasonaboutoverallprogressintermsofalargecollectionofsuchmeasures,because:
1. Performanceisoftenmeasuredindifferentunits(accuracy,BLEU,points,ELO,cross-entropyloss,
etc)andgainsonmanyofthemetricsarehardtointerpret.Forinstancegoingfrom94.99%accuracy
to99.99%accuracyismuchmoreimpressivethangoingfrom89%to94%.
2. Theproblemsareuniqueandtheirdifficultiesaren’tcomparablequantitively,soassessmentrequires
gaininganintuitionforeachproblem.
3. Most research focuses on reporting overall performance improvements rather than efficiency im-
provements, so additional work is required to disentangle the gains due to algorithmic efficiency
fromthegainsduetoadditionalcomputation.
4. Thebenchmarksofinterestarebeingsolvedmorerapidly,whichexacerbates1)and2).Forinstance
it took 15 years to get to human-level performance on MNIST [LeCun et al., 1998], 7 years on
ImageNet[Dengetal.,2009,Russakovskyetal.,2015],andGLUE[Wangetal.,2018]onlylasted
9months[Devlinetal.,2018,Liuetal.,2019].
We show that we can gain clear insights into efficiency trends by analyzing training costs while holding
performanceconstant.Wefocusedontrainingefficiencyratherthaninferenceefficiency,becausewe’remore
interestedinwhatsystemsarepossibletoproducethanhowmuchitcoststorunthosesystems. Thoughwe
noteincreasedinferenceefficiencycanhaveimportanteconomicimplications[vandenOordetal.,2017]. In
the research setting, we’ve typically found ourselves FLOPS bound rather than memory or communication
3

bound. So we measured total floating-point operations used in training rather than parameters or another
measureofefficiency.
We focused on AlexNet-level performance, which we measured as 79.1% top-5 accuracy on ImageNet.
AlexNet kicked off the wave of interest in neural networks and ImageNet is still a benchmark of wide in-
terest,sothismeasureprovidedalongrunningtrendtoanalyze.
2 RelatedWork
2.1 AlgorithmicprogresshadsimilarratetoMoore’sLawinsomedomainsoverdecades
Gracecomparedalgorithmicprogresstohardwareprogresslookedatoverseveraldecadesinthedomainsof
chess,go,physicssimulations,mixedintegerprogramming,andSATsolvers[Grace,2013]. Grace’soverall
conclusionwas
Many of these areas appear to experience fast improvement, though the data are often
noisy. Fortasksintheseareas,gainsfromalgorithmicprogresshavebeenroughlyfiftyto
one hundred percent as large as those from hardware progress. Improvements tend to be
incremental,formingarelativelysmoothcurveonthescaleofyears
For the most part, these estimates and their interpretation require substantial amounts of judgment. For
instance,withchessandGotheapproachwastousetheavailableliteraturetoestimatewhatkindsofreturns
came from a hardware doubling and then attribute all ELO improvement not explained by Moore’s law to
software. Additionally, Grace suggests we treat these estimates as "optimistic" rather than representative,
becauseofincreasedsaliencyofproblemsthataremakingfastprogress,problemswithgoodmeasuresbeing
likely to progress faster, and the potential motivations of authors. Regardless, we think this related work
shows that hardware and algorithmic progress can be on a similar scale, and that even a relatively simple
modelofprogressshouldconsiderintegratingmeasuresfrombothdomains.
Progressonmixedintegerprogrammingwasparticularlystraightforwardtomeasure,sowe’veextendedthe
originalanalysisofthatdomainbelow[Bixby,2012].
2.2 Linearprogramminggainswerewell-defined,steady,andfasterthanMoore’sLawfor21years
Unlike some other optimization domains Grace looked at, linear programming was of commercial interest
foralongperiod. Progressiseasytotrackinthisdomainoverthis21yearperiodbecausethereweredistinct
releasesofcommercialsoftware(CPLEXandGurobi)thatcanbecomparedwithhardwareheldfixed.
Thetrendofa2xspeedupevery13monthsobservedinFigure1issurprisinglyconsistentoveralongtime
horizon. Thesmoothprogressispartiallyexplainedbythemeasurebeinganaggregationofmanyproblems
ofvaryingdifficulty. OverthistimeMoore’sLawyieldedanefficiencygainofapproximately1500x.
Caveats
1. It’snotablethatthebenchmarkwasdesignedandtheanalysiswasperformedbytheCEOofGurobi
(acommercialMIPSsolver)andthathehadanincentivetodemonstratelargeamountsofprogress.
2. It’s worth pointing out the implications of the maximum search time of 30,000s for the optimal
solution. When it took longer than 30,000s for the solver to find the optimal solution, 30,000s
iswhatwouldberecorded. It’sexpectedthatthemaximumsearchtimewouldhavebeeninvoked
moreforearlier,weakersolvers.Thus,themaximumsearchtimemadeearliersolverslookrelatively
stronger,makingtheoverallestimateconservativeforthisbenchmark. Wethinkusingamaximum
search time is reasonable, but we expect the overall speedup is sensitive to it. In this sense, these
measurementsarealittledifferentthantheAlexNetaccuracymeasurements, wherewewaitedfor
thecapabilitytobedemonstratedbeforemeasuringprogress.
3. Thisistherelateddomainwith highestamountofmeasuredalgorithmicefficiencyprogresswe’re
awareofforthisperiodoftime.
4

pudeeps
evitalumuC
500,000x Speedup in Mixed Integer Programming over 20 Years
1000000
100000
10000
1000
100
10
1
1995 2000 2005 2010
Figure1 A2xspeedupevery13monthswasobservedonabenchmarkof1,892mixed-integerproblems
(MIPs), a subset of linear programming. This benchmark was created by Bixby, he describes it as a set of
"real-worldproblemsthathadbeencollectedfromacademicandindustrysourcesover21years."Progressis
basedonthetotaltimespentsearchingfortheoptimalsolutionforallproblemsinthebenchmark. Progress
is easy to track in this domain over this 21 year period because there were distinct releases of commercial
software(CPLEXandGurobi)thatcanbecomparedwithhardwareheldfixed. Amaximumsearchtimeof
30,000 seconds (approximately 8 hours) per problem was used, so that’s what was recorded for instances
wheretheoptimumwasn’tfound. Weclarifiedthetrendbygraphingthetrendbyreleasedateratherthanby
versionnumber [Bixby,2012].
2.3 184xreductionintrainingcost(indollars)togettoResNet-50performancesince2017
The eventual unit institutions generally care about for training cost is dollars. Earlier we observed a 10x
efficiency improvement in terms of training FLOPs required to get ResNet-50 level accuracy (92.9% top-5
accuracy target on ImageNet). On the same target, DawnBench submissions have surpassed the contest’s
originalbenchmarkcost,$2323,byafactorof184x[Colemanetal.,2017]. Thisbroughtthecostofsucha
trainingdownto$12.60inSeptember2017,lessthanayearafterthecompetitionwasannounced. Training
costindollarsisausefuloverallmeasure,thataggregates:
1. Theefficiencygainsfromalgorithmicprogresswearemostinterestedinwithinthispaper.
2. Moore’sLaw’seffectonGPUs,TPUs,etc.
3. Reducedcloudcomputingcostsdrivenbymodernizationandincreasedcompetition.
4. Hardwareutilization. It’snottrivialtoefficientlyusetheFLOPScapacityofGPUs,TPUs,etc.
TheDawnBenchresultsmakeitclearthat3. and4. canalsobenotablecontributionstotrainingefficiency
that are worth measuring. More targeted measurements, like training efficiency in terms of FLOPs, help
clarifythetakeawayfrommeasureslikeDawnBenchthataggregatemultipleeffects.
2.4 Wecanestimatecostly-to-observealgorithmicefficiencyimprovementsthroughscalinglaws
We’vefocusedonalgorithmicefficiencyimprovementsthatareobservableempirically. [KaplanMcCandlish
2020]showedthatlanguagemodelperformanceoncross-entropyhadpower-lawscalingwiththeamountof
computeoverseveralordersofmagnitude. Empiricalscalinglawscanbeextrapolatedtoprovideanestimate
ofhowmuchwewouldhaveneededtoscaleupoldermodelstoreachcurrentlevelsofperformance.Through
5

this mechanism scaling laws provide insight on efficiency gains that may require prohibitively expensive
amountsofcomputetoobservedirectly.
2.5 TotalinvestmentinAIthroughprivatestartups,publicofferings,andmergers/acquisitionswent
up5xbetween2012and2018
We’ve primarily considered algorithmic, hardware, and data as the inputs in progress in machine learning.
Money spent would be another reasonable lens since that’s the lever available to decision-makers at the
highestlevel.[Bloometal.,2017]looksintotherelationshipbetweenscientificprogressandspending:
In many models, economic growth arises from people creating ideas, and the long-run
growthrateistheproductoftwoterms: theeffectivenumberofresearchersandtheirre-
searchproductivity... AgoodexampleisMoore’sLaw. Thenumberofresearchersrequired
today to achieve the famous doubling every two years of the density of computer chips is
more than 18 times larger than the number required in the early 1970s. Across a broad
range of case studies at various levels of (dis)aggregation, we find that ideas – and the
exponentialgrowththeyimply–aregettinghardertofind.Exponentialgrowthresultsfrom
largeincreasesinresearcheffortthatoffsetitsdecliningproductivity.
AI investment is also up substantially since 2012, and it seems likely this was important to maintaining
algorithmicprogressattheobservedlevel.[RaymondPerrault&Niebles,2019]notesthat:
1. PrivateinvestmentinAIstartupsrosefrom$7Bin2012to$40Bin2018.
2. Investment through public offerings and mergers/acquisitions grew from $5B in 2012 to $23B in
2018.
3. TheDODisprojectedtoinvest$4.0BonAIR&Dinfiscalyear2020.
4. ContractspendingonAIbytheUSgovernmenthasgrownfromabout$150Mto$728Mbetween
2012and2018.
3 Methods
3.1 Mainresultprimarilybasedonexistingopensourcere-implementationsofpopularmodels
For the majority of the architectures shown in Figure 3 [Szegedy et al., 2014,Simonyan & Zisserman,
2014,He et al., 2015,Xie et al., 2016,Huang et al., 2016,Iandola et al., 2016,Zagoruyko & Komodakis,
2016,Zhangetal.,2017,Howardetal.,2017,Sandleretal.,2018,Maetal.,2018,Tan&Le,2019]weused
PyTorch’s example models [Paszke et al., 2017] with Pytorch’s suggested hyperparameters. We mark our
deviationfromtheirhyperparametersinthenextsection. WesupplementedPyTorch’sexamplemodelswith
existingimplementationsofMobileNet,ShuffleNet [Xiao,2017,Huang,2017].
Computeusedisbasedontheproductofthefollowing:
1. FLOPs per training image, which was counted by a PyTorch library [Zhu, 2019] that we checked
againstothermethodsforseveralmodels
2. Thenumberofimagesperepoch
3. ThenumberofepochsittookanarchitecturetoperformbetterthanorequaltotheAlexNetmodel
wetrained
3.2 Wemadefewhyperparameteradjustmentsbetweenarchitecturesanddidminimaltuning
WelargelyfollowedthesuggestedhyperparametersfromthePyTorchexamplemodels. Forallpointsshown
infigure3wetrainedusingSGDwithabatchsizeof256,momentumof0.9,andweightdecayof1e-4,for
90epochs. Forpre-batchnormarchitectures,webeganwiththesuggestedlearningrateof0.01(GoogleNet
andVGG),forallotherarchitectureswebeganwiththesuggestedlearningrateof0.1.
For AlexNet we followed the original paper’s learning rate schedule of decaying by a factor of 10 every
30 epochs. For all other models, we followed the suggested 1000x total learning rate reduction. To sanity
check that these were reasonable hyperparameters, we performed a scan on ResNet18 where we set the
6

initial learning rate to 0.0316, 0.1, and 0.316 and total decay to 250x, 1000x, and 2500x. The suggested
hyperparameters performed the best. For all models other than AlexNet we smoothed out the learning rate
schedule,whichwasimportantforearlylearningasshowninFigure2.
Epoch
ycaruccA
5poT
Smooth schedule improved early learning
100 Smooth
Piece-wise
75
50
25
0
0 20 40 60 80
Epoch
etaR
gninraeL
Smooth learning rate schedule
0.1 Smooth
Piece-wise
0.01
0.001
0 20 40 60 80
Figure2 Smoothingoutthelearningrateimprovedearlylearning,whichistheregimewewereinterested
in. ResNet-50learningcurvespictured.
A natural concern would be that new models aren’t optimized well for compute in reaching AlexNet-level
performance. Beforesmoothingthelearningrateschedule,manymodelshitAlexNetperformanceatexactly
31 epochs, when the learning rate was reduced by a factor of 10x. This adjustment often increased our
measured efficiency by 2-4x, but we didn’t observe meaningful differences in final performance from the
changeinlearningrateschedule.Soeventhoughthechangetothelearningrateschedulecouldbeconsidered
minimal, it has a large effect on our measurements. The more simple shape of the updated learning curve,
suggeststhatoptimizingforconvergencemightberelativelycompatiblewithoptimizingforlowerlevelsof
performance,likeAlexNet-levelaccuracy.
As context for the quality of these re-implementations we provide tables in Appendix C that compare the
finalaccuracywereachedtotheoriginalpaperresults.
4 Results
4.1 KeyResult: 44xlesscomputeneededtogettoAlexNet-levelperformance
Infigure3weshowthatbetween2012and2019theamountofcomputethatneuralnetarchitecturesrequire
tobetrainedfromscratchtoAlexNetlevelperformancehasgonedownbyafactorof44x(16-monthdoubling
time)
Most researchers found the algorithmic efficiency gains to surprisingly high and regular. The progress is
fasterthantheoriginalMoore’sLawrate(11x)overthisperiod,wherebothtrendsmadetrainingmodelsof
AlexNet-levelperformancecheaper. Moore’sLawisobviouslyamoregeneraltrendthanwhatweobserve
inFigure3. Webelieveit’squiteinterestingtoseewhatwecansayaboutalgorithmicefficiencyprogressin
generalgiventhesetypesofmeasurement,andweexplorethisquestioninsections4.2and5.4.
7

Figure3 Lowestcomputepointsatanygiventimeshowninblue,allpointsmeasuredshowningray. We
observedanefficiencydoublingtimeof16months.
We can split the progress in training efficiency into data efficiency (needing fewer epochs) and reductions
in the number of FLOPs required per epoch. Table 1 below shows this split for the models that were the
efficiencystateoftheartforatime.
We can see that both reductions in training epochs and FLOPs per training image play an important and
varyingfactorintheoverallalgorithmicefficiencygains. Thistypeofanalysisissomewhatsensitivetohow
fartheoriginalworkpushedtowardsconvergence.2 Otherlimitationsarediscussedinsections5.4and5.7.
Calculationsforthefigure3areprovidedinAppendixB.RelevantinformationforEfficientNettrainingcost
wasprovidedthroughcorrespondencewithauthors.
2Itonlytook62ofthe90epochsforAlexNettotrainto78.8%top5accuracyonImageNet(99.6%ofthe79.1%
finalaccuracy). SoiftheoriginalAlexNethadonlybeentrainedfor62epochs, wewouldhavecalculatedtheoverall
algorithmicefficiencygainas30xratherthan44x.Wedon’tthinkit’stractabletomitigatethisconfounderwithoutadding
alotofcomplexitytoexplainingthemeasurement,butitseemedimportanttoflagasalimitationofourapproach.
8

Table1 BreakdownoftotaltrainingefficiencygainsinreachingAlexNet-levelaccuracyintoreductionof
trainingepochsandflopsperepoch
Experiment Trainingepochsfactor FLOPsperepochfactor Trainingefficiencyfactor
AlexNet 1.0 1.0 1.0
GoogleNet 11 0.38 4.3
MobileNet_v1 8.2 1.35 11
ShuffleNet_v1_1x 3.8 5.5 21
ShuffleNet_v2_1x 4.5 5.5 25
EfficientNet-b0 22 2.0 44
4.2 FLOPsbasedlearningcurvescanhelpclarifycomparisonsbetweenmodels
We find it noteworthy that in when we plot FLOPs based learning curves in figure 4 some architectures
dominateothers.
Teraflops/s-days
ycaruccA
FLOPs used to train vs top5 accuracy on ImageNet
100 AlexNet
GoogleNet
75
MobileNet_v2
Resnet-50 50
ShuffleNet_v2_1x
25
Vgg-11
0
0.01 0.1 1 10
Figure4 Somemodelsreachalllevelsofofaccuracyusinglesscomputethanothermodels
FLOPsbasedlearningcurvescanhelpclarifywhattypeofadvancesanewarchitectureconsistsof. ResNet-
50dominatesVGG-11andGoogLeNetdominatesAlexNetonthisplot. Thatisforallamountsoftraining
compute they get better accuracy. VGG-11 reached higher final accuracy than AlexNet, but it took more
computetogettoalllevelsofperformancethanAlexNet.
4.3 WeobservedasimilarrateofprogressforResNet-50levelclassificationperformanceandfaster
ratesofefficiencyimprovementinGo,Dota,andMachineTranslation
We’re also interested in measuring progress on frontier AI capabilities, the capabilities that are currently
attracting the most attention and investment. It seems to us as if language modeling [Devlin et al., 2018,
Radford et al., ,Raffel et al., 2019] and playing games [Silver et al., 2016,Silver et al., 2017,Silver et al.,
2018,OpenAIetal.,2019]arethedomainsofinterestgivenourcriteria.
Withinthosedomains,ourdesideratawere:
1. taskofsufficientdifficultytodemonstratethatimprovementsworkatscale[Sutton,2019]
9

2. benchmark of high interest over long horizon in which there’s general agreement we’ve observed
largeprogressincapabilities.
3. sufficientlygoodpubliclyavailableinformation/re-implementationstoeasilymakeanestimate
It’shardtogetallthesedesiderata,butTable2belowsummarizesallthedatawehaveobserved.
Table2 Increasedefficiency(intermsofFLOPs)inreachingthesameperformanceonselecttasks.
Original Improved Task EfficiencyFactor Period DoublingTime
AlexNet EfficientNet ImageNet 44x 6years 16months
ResNet EfficientNet ImageNet 10x 4years 17months
Seq2Seq Transformer WMT-14 61x 3years 6months
GNMT Transformer WMT-14 9x 1year 4months
AlphaGoZero AlphaZero GO 8x* 1year* 4months*
OpenAIFive OpenAIRerun Dota 5x* 2months* 25days*
*The work on Go and Dota are over shorter time scales and more the result of one research group rather
thanalargescientificcommunity,sothoseratesofimprovementshouldbeconsideredtoapplytoadifferent
regimethantheratesinimagerecognitionandtranslation.
Whenweapplythislenstotranslation[Sutskeveretal.,2014,Vaswanietal.,2017]itshowsmoreprogress
thanvisionoverashortertimehorizon. ThoughweonlyhaveshorthorizonprogressforGoandDota,we’d
onlyneedtoseeamodest3xand5xefficiencygainover5yearsfortheirratestosurpasstherateofprogress
onthevisiontask. TheunderlyingcalculationsareprovidedinappendixA.
Onemightworrythattherateofprogressinimagerecognitionisverysensitivetoperformancelevelchosen,
so we also did a shallow investigation of efficiency gains at ResNet-50 level of performance. The relevant
information, that EfficientNet-b0 took 4 epochs to get to AlexNet level accuracy, and EfficientNet-b1 [Tan
&Le,2019]took71epochstogettoResNet-50levelaccuracywasprovidedthroughcorrespondencewith
authors(whereeachwastrainedwith1epochofwarmupratherthan5).
We observed a similar rate of progress for efficiency gains in inference on ImageNet. We also did a
shallowinvestigationintohowtherateofprogressoninferenceefficiencyhascomparedtotrainingefficiency.
Weobservedthat:
1. Shufflenet[Zhangetal.,2017]achievedAlexNet-levelperformancewithan18xinferenceefficiency
increasein5years(15-monthdoublingtime).
2. EfficientNet-b0[Tan&Le,2019]achievedResNet-50-levelperformancewitha10xinferenceeffi-
ciencyincreasein3andahalfyears(13-monthdoublingtime).
These results suggest that training efficiency and inference efficiency might improve at somewhat similar
rates. Thoughit’simportanttonotewehavemanyfewerpointsacrosstimeanddomainsforinference.
5 Discussion
5.1 Weattributethe44xefficiencygainstosparsity,batchnormalization,residualconnections,
architecturesearch,andappropriatescaling
Amorethoroughstudywouldhavecarefullyablatedallthefeaturesofinterestfromsuccessfulmodelswhile
controllingformodelsizetobeabletoattributetheefficiencygainstospecificimprovementsinaquantitative
manner[Lipton&Steinhardt,2018].Weperformedsomeablations,butprimarilyrelyonlessdirectevidence
when forming opinions about which improvements we suspect were most important to the 44x increase in
efficiency.Forinstancewediscusswhattheoriginalauthorscredit,thoughit’simportanttorecognizeauthors
areincentivizedtoemphasizenovelty. Wethinkit’simportanttonotethatefficiencygainsmaycomposeina
hardtopredict,non-linearmanner.
10

BatchNormalization: Batchnormalizationenableda14xreductioninthenumberoffloating-pointoper-
ationsneededtotraintoInceptionlevelaccuracy[Ioffe&Szegedy,2015]. It’sunclearhowsuchalgorithmic
efficiency gains like batch normalization compose, but it seems reasonable to attribute some meaningful
portion of the gains to normalization. We made a few attempts to try and train a ShuffleNet without batch
normalization, but we were unable to get a model to learn. We suspect we would have needed to carefully
initializethenetworktodoso [Zhangetal.,2019].
ResidualConnections: ShuffleNetunits,thebuildingblocksofShuffleNet,areresidualblocks. Efficient-
Netalsohasresidualconnections.
Sparsity: GoogLeNetwasexplicitindescribingsparsityastheprimaryinspirationforitsarchitecture,and
GoogLeNetalonewasa4.3xefficiencyimprovementoverAlexNet. [Szegedyetal.,2014].
This raises the question of whether there is any hope for a next, intermediate step: an
architecture that makes use of the extra sparsity, even at filter level, as suggested by the
theory,butexploitsourcurrenthardwarebyutilizingcomputationsondensematrices.
ShuffleNetlargelycreditsreplacingdense1x1convolutionswithasparserstructure. Ifweassumeallthe
ShuffleNetgainscamefromsparsity, batchnormalization, andresidualconnections, itseemsreasonableto
credit sparsity with being able to produce at least the 4.3x that came with GoogLeNet (leaving 5.8x of the
25xgainshowninTable1fortheothertwoconceptualimprovements).
AppropriateScaling: Givenit’sarchitectureAlexNetwasoptimallysizedforAlexNet-levelperformance.
Given our tests of scaled up and scaled down models ShuffleNet_v2_1x, and EfficientNet-b0 seem to be
closetoappropriatelysizedforAlexNet-levelperformance. Wetestedtheeffectofscalingbyscalingdown
a ResNet-50 by EfficientNet’s compound scaling factor twice (1.4x less depth, 1.2 less width, 1.3 lower
resolution)[Tan&Le,2019]. ScalingtheResNetarchitecturetoamoreappropriatesizeforAlexNet-level
performanceyieldeda2.1ximprovementinalgorithmicefficiencyforAlexNet-levelperformance. Figure8
intheEfficientNetpapershowsthattheircompoundscalingtechniques(systematicallyscalingwidth,depth,
andresolution)canresultin5xormoregainsinalgorithmicefficiencyovermorenaivescalingapproaches.
ArchitectureSearch: EfficientNetseemstoattributemuchofitsimprovedperformancetoleveragingar-
chitecture search rather than iterating on hand designed architectures. EfficientNet was a 1.8x increase in
algorithmicefficiencyoverShuffleNetatAlexNet-levelperformance.
5.2 It’sunclearthedegreetowhichtheobservedefficiencytrendsgeneralizetootherAItasks
We’re most interested in what our small number of data points suggest about algorithmic progress overall
duringthisperiod. Werecognizeit’sdifficulttogofromoneormorespecificmeasurestostatinganything
about overall progress. In this section we share our current impressions and suggest measures that could
clarifythedegreetowhichthetrendswe’veobservedgeneralize.
Allourmeasureswerefortasksthathave:
1. receivedlargeamountsofinvestment(researchefrtimeand/orcompute)
2. inwhichthere’sgeneralagreementwe’veobservedlargeprogressincapabilities.
We suspect that this style of measurement on tasks that meet these criteria is likely to show similar rates
of improvement in algorithmic efficiency as we’ve observed here. One concern we had, was that the rates
of improvement would be very dependent on the level of performance. That may still be the case, but we
weresurprisedhowclosetheefficiencydoublingtimewasforAlexNet-levelperformance(16months)and
ResNet50-level performance (17 months). We also suspect, but are less confident, that such measurements
wouldshouldsimilarprogressinthesedomains(imagerecognition,naturallanguageprocessing,andgames).
We’dbeveryinterestedinsuchmeasurements.
However, we’re also interested in progress in high potential tasks that don’t fit these criteria, like certain
reasoningtasks. Intheprevioussection,weattributedtheefficiencygainsoverAlexNetprimarilytosparsity,
residual connections, normalization, principled scaling, and architecture search all of which are relatively
task-agnostic. But,it’spossiblethatwe’dobserveonlysmallefficiencygainsfromthesetechniquesonsuch
tasks. WeconsiderthedegreetowhichtheobservedefficiencytrendsgeneralizetootherAItasksahighly
interestingopenquestion.
11

5.3 Whynewcapabilitiesareprobablyalargerportionofprogressthanobservedefficiencygains
AlexNetachievedperformancethatnosystemhadpreviouslyachieved.Wecantrytoreasonabouthowmuch
compute would have been required in scaling up previous systems to match AlexNet’s performance. From
thispointofview,webelieveAlexNetrepresentedsignificantprogressinhowmuchcomputewasrequired
to achieve AlexNet-level performance. This analysis doesn’t attempt to quantify that progress because it’s
less tractable. More generally, the first time a capability is created, algorithmic breakthroughs may have
been leveraged to dramatically reduce the resources that would have otherwise been needed. For instance,
if we imagine simply scaling up a DQN [Mnih et al., 2013] model to play Go it could easily have needed
1000x or more times as much compute to reach AlphaGo level. Such efficiency gains are not generally
observed empirically, though they can be calculated with asymptotic analysis in some cases and estimated
withempiricalscalinglawsinothers [McCandlishetal.,2018].
More formally, if we go far enough back in time, algorithmic progress takes us from brute force search to
lowercomplexityclasses,whichiswhatenablescapabilitiesofinteresttobebuiltatall. Withinthiszoomed-
out view, the progress that went into making a capability possible at all, in total, yields an astronomically
larger algorithmic efficiency improvement factor than directly observed efficiency improvements for capa-
bilities that have recently been observed for the first time. This limit analysis lends some support to the
claimthattherateofgaininalgorithmicefficiencyonacapabilityofinterestmightoftenbefasterbeforea
capabilityisobserved.
IntheDQNandbruteforceexamplesdescribedabove,wefinditmosthelpfultostartbythinkingofascaling
law,aplotofperformancevstrainingcomputeused.Ouralgorithmicefficiencydataresultsarepointswefind
meaningfulfromthosegraphs,butsometimessimilarcomparisonswouldjustyieldanastronomicalnumber
that might not have much meaning. In such cases, we’d recommend analyzing a graph of the scaling law,
sinceitcontainstheentirepicture.
Whilemostresearcherswe’vediscussedtheresultwithfoundthe44xnumbersurprisinglyhigh,becauseof
this effect 44x may strongly underestimate algorithmic progress on image classification during this period.
When this analysis is discussed in the context of the relative importance of advancements in hardware and
softwareinAIprogress,wethinkit’scriticaltorememberthislimitation[Sutton,2019].
5.4 Weestimatea7.5milliontimesincreaseintheeffectivetrainingcomputeavailabletothelargest
AIexperimentsbetween2012and2018
Thissectionexplainswhyweestimatetherewasa7.5milliontimesincreaseintheeffectivetrainingcompute
(inFLOPs)availabletothelargestAIexperimentsduringthisperiod. Thereasoningbehindourestimateis
that’s what we get when we take the product of the AI and Compute trend [Amodei & Hernandez, 2018]
(300,000x) and AlexNet efficiency trend found in this work (25x over this period3), and carefully consider
whatthisproductmeans. Whenweconsiderthatwehavemorecomputeandthateachunitofcomputecan
domore,itbecomesclearthatthesetwotrendsaresomehowmultiplicative.
Thissectionismorespeculativethantherestofthepaper,butwethinkit’simportanttoexplorethepotential
implicationsofourefficiencymeasurements. Webelievea7.5milliontimesestimateissomewhatdefensible
whenwe:
1. Narrowlydefinecapabilitiesofinterestsothat300,000xcanbeappliedbydefinition.
2. Definewhatwemeanbyeffectivecompute.
3. Discussmajorconsiderationsforwhy25xcouldbeanunderestimate/overestimateforalgorithmic
progressoncapabilitiesofinterest.
Capabilitiesofinterest: Wedefinecapabilitiesofinterestasthetrainingrunsatclosetothepeakofsize
that was observed in 2018. Therefore it’s appropriate to apply the 300,000x from AI and Compute trend
by definition. By 2020 such systems include AlphaZero, OpenAI Five, and NLP systems. This definition
helps us avoid having to reason about what our measurements imply for distant domains. We have some
measurementsofprogressformanyofthecapabilitiesofinterestbytheabovedefinition.Thoughit’spossible
thereareunpublishedresultsthatfitthecapabilityofinterestdefinitioninrelativelydistantdomains.
3Through 2018 we use the 25x efficiency gains ShuffleNet represented rather than the 44x gains that EfficientNet
representedin2019
12

Effectivecompute: Theconceptionwefindmostusefulisifweimaginehowmuchmoreefficientitisto
train models of interest in 2018 in terms of floating-point operations than it would have been to "scale up"
trainingof2012modelsuntiltheygottocurrentcapabilitylevels.By"scaleup,"wemeanmorecompute,the
additionalparametersthatcomewiththatincreasedcompute,theadditionaldatarequiredtoavoidoverfitting,
and some tuning, but nothing more clever than that. We considered many other conceptions we found less
helpful4.
Whyouroveralltakeisthat25xislikelyanunderestimateforalgorithmicprogressoncapabilitiesof
interest Ouroveralltakereliesheavilyonourobservationsinthedomainofinterest. Wesawlargeroverall
progress in NLP and faster rates of short horizon progress for Go and Dota. In NLP we observed a 60x
efficiencyfactor over3years formachinetranslation. Thoughwe onlyhaveshort-horizon progressforGo
andDota,we’donlyneedtoseeamodest3xand5xefficiencygainsrespectivelyover5yearsfortheirrates
tosurpasstherateofprogressonthevisiontask.
Ontheotherhand,algorithmicprogresshasadomainspecificcomponent,andit’sunclearhowrepresentative
the 25x is of the average efficiency progress in the broader domain of AI during this period. However, we
believe this effect is smaller than the effect in the opposite direction of not measuring the contribution of
newcapabilitieslikeAlexNet, Seq2Seq, ororiginalAlphaGosystemsduringthisperiod. Insection5.3we
providedargumentsforwhynewcapabilitiesmightrepresent100xormorealgorithmicefficiencyprogress.
Tofurtherclarifywhatdrovechangesineffectivecomputeoverthisperiod,wesplittheAIandComputetrend
into Moore’s Law and increased spending/parallelization5. We graph an estimate for the effective compute
trendsintermsofthesetwocomponentsaswellasprogressinalgorithmicefficiencyinfigure5below.
We’reuncertainwhetherhardwareoralgorithmicprogressactuallyhadabiggerimpactoneffective
compute availableto largeexperiments over thisperiod, becauseof theways we’ve discussedin which
the algorithmic estimate is conservative. Most researchers found the algorithmic efficiency progress to be
surprisingly fast. So, regardless of one’s interpretation of what the AI and Compute trend implies about
futureAIprogress,webelieveouralgorithmicefficiencyestimatessuggests:
1. amodestupdatetowardsexpectingfasterprogressalongtheedgeofwhat’spossibleforAItodoin
theshortterm.
2. potentiallylargeupdateonlongtermexpectationsaboutAIifthealgorithmicefficiencyoncapabil-
itiesofinterestcontinuestoimproveatasimilarrate.
Directlycommentingonthelikelihoodofanyofthe3macrotrendsinfigure5continuinginthefuture
isoutofscopeforthiswork.Makingcredibleforecastsonsuchtopicsisasubstantialenterprise,we’drather
avoid here than give insufficient treatment. Rather we present the evidence we see as relevant for a reader
who’dliketoformtheirownexpectationsaboutextrapolatingtrendsinalgorithmicefficiency.
Additional reasons why 44x over 7 years could be an underestimate for progress on AlexNet-level
algorithmicefficiency:
1. OnlyAlexNetwasheavilyoptimizedforAlexNetlevelperformance.Modelsaregenerallytunedfor
performanceatconvergence,notearlylearning.Ourresultswereproducedwithminimumtuningfor
earlylearningandAlexNet-levelperformance,andtuningthemcouldonlyincreasetheirefficiency
gains.
2. It’s our understanding that the re-implementation of AlexNet we used had a better initialization
schemethantheoriginalwork. Thiseffectaddsanotherfactorofconservativenesstoouranalysis.
We expect future analysis to also be limited by this effect. This concern could be mitigated by
researcherspublishingtheirlearningcurvesinadditiontotrainingcomputeusedtotrain.
3. Wedon’taccountforgainsfrombeingabletouselowerprecisioncomputation[Guptaetal.,2015].
4. Wedon’taccountforgainsfromincreasedGPUutilizationorimprovedGPUkernels.
4Our initial thinking was in terms of what an elite team in 2012 could have done if given a large amount com-
pute, but this was unobservable. We could make something similar observable by having a group of smart physi-
cists/mathematiciansthatwereunfamiliarwithmodernMLmethodsworkonproblemswithoutaccesstomodernresults,
butthatwouldbeveryexpensivetoobserve.
5Increasedspendingandparallelizationarecoupledinthatgivenfixedtimearesearcherislimitedbyboth(i)how
many concurrent GPU’s are available to them which is primarily a financial question, and (ii) how many GPU’s can
productivelybeappliedtotheproblem,whichisascientificquestion [McCandlishetal.,2018,Jiaetal.,2018]
13

Figure5 ThenotionofeffectivecomputeallowsustocombineAIandComputetrendandthisresultina
singlegraph. Thesetrendsmultiplyasinadditiontobeingabletodomorewithafixedamountofcompute
now,researchershavemoreofit. TheAIandComputetrendisdecomposedintoahardwareefficiencygain
estimate(originalMoore’sLaw)andmoney/parallelization[Moore,1965,Amodei&Hernandez,2018].This
estimate,asdiscussedinthebodyofthissection,ismorespeculativethantherestofthepaper,butwethink
it’simportanttoexplorethepotentialimplicationsofourefficiencymeasurements.
5.5 It’spossiblethere’sanalgorithmicMoore’sLawforoptimizationproblemsofinterest
ThisworksuggeststhatinhighinvestmentareasofAIalgorithmicefficiencyimprovementiscurrentlyhav-
ing a similar-sized effect as Moore’s Law has had on hardware efficiency in the past. Others have noticed
comparable algorithmic progress over decades in related domains like Chess, Go, SAT solving, and opera-
tions research. In light of that past analysis, it’s less surprising that we’ve observed algorithmic efficiency
gains this large on training to an AlexNet level of performance. The common thread here seems to be that
thesealongwithAIsystemsarealloptimizationproblemsofinterest.
SystematicmeasurementcouldmakeitclearwhetheranalgorithmicequivalenttoMoore’sLawinthedomain
of AI exists, and if it exists, clarify its nature. We consider this a highly interesting open question. We
suspect we’re more likely to observe similar rates of efficiency progress on similar tasks. By similar tasks
we mean within these sub-domains of AI, wide agreement of substantial progress, and comparable levels
of investment (compute and/or researcher time). It’s also unclear the degree to which general vs domain
specificgainswouldbethedriversofsuchprogress,andhowgainscompoundoverlongperiodsasthefield
progressesthroughseveralbenchmarks. Problemsofhighinvestmentmightbebequitebiasedtowardsones
we’remakingprogressonrather,whereanidealmeasuremightfocusonthequestionsthatareseenasmost
important.
An AI equivalent to Moore’s Law would be harder to measure, because it’s not about progress on a single
problem, it’s about progress on the frontier of optimization problems. Through that lens, it seems more
plausiblewe’llseelongtermexponentialprogressonalgorithmicefficiencyforAIcapabilitiesofinterestif
ourprimaryfindingisanextensionofanexisting,long-runningtrendinprogressonoptimizationproblems
ofinterest.
14

5.6 ResearchprovidesleadingindicatorsofthefutureeconomicimpactofAI
The eventual overall measure of AI research’s impact on the world will likely be economic. However, it
took past general-purpose technologies like electrification and information technology a surprisingly long
time to become widespread. From the start of information technolology era it was about 30 years before
personalcomputerswereinmorethanhalfofUShomes[Jovanovic&Rousseau,2005](similartimelinefor
personalcomputers). Analysisofpastinvestmentsinbasicresearchalong20-30yeartimescalesindomains
like computers indicates that there’s at least some tractability in foreseeing long term downstream impacts
oftechnologylikemachinelearning. EconomictrendsofAIareveryinformative,butmeasuresofresearch
progressareofparticularinteresttousasleadingindicatorsoftheeventualdownstreameconomicandsocietal
impact.
5.7 Majorlimitations
Thelimitationsofthisworkarediscussedthroughout,butthemajoronesarereiteratedhere:
1. We only have a small number of algorithmic efficiency data points on a few tasks (Section 4).
It’s unclear the degree to which we’d expect the rates of progress we’ve observed to generalize to
algorithmicefficiencyprogressonotherAItaskanddomains. Weconsiderthisahighlyinteresting
openquestionthatwediscussinSection5.2.
2. We believe our approach underestimates algorithmic progress, primarily because new capabilities
arelikelyalargerportionofalgorithmicprogressthanobservedefficiencygains(Section5.3). This
weaknesscouldbeaddressedbyfittingscalinglawstoestimatethecostofprohibitivelyexpensive
trainingruns(Section2.4).
3. Thisanalysisfocusesonthefinaltrainingruncostforanoptimizedmodelratherthantotaldevel-
opmentcosts. Somealgorithmicimprovementsmakeiteasiertotrainamodelbymakingthespace
ofhyper-parametersthatwilltrainstablyandgetgoodfinalperformancemuchlarger. Ontheother
hand, architecture searches increase the gap between the final training run cost and total training
costs. Webelieveaquantitativeanalysisoftheseeffectswouldbeveryinformative,butit’sbeyond
thescopeofthispaper.
4. Wedon’tcommentonthedegreetowhichwebelieveefficiencytrendswillextrapolate,wemerely
present our results (Section 4) and the related work (Section 2) we think is relevant for someone
attempting to make such a prediction. Though we do comment on the implications if the trends
persist.
6 Conclusion
Weobservethathardwareandalgorithmicefficiencygainsmultiplyandthatneitherfactorisnegligibleover
meaningfulhorizons,whichsuggeststhatagoodmodelofAIprogressshouldintegratemeasuresfromboth.
Wehopethisworkishelpfultothosetryingtounderstand,measure,andforecastAIprogressinavarietyof
settings. We’veobservedthatAImodelsforhighinteresttasksaregettingcheapertotrainatanexponential
rate faster than Moore’s Law. Even though we’re early on in applying this trend to AI, we were surprised
and inspired to learn that the original Moore’s Law was coined when integrated circuits had a mere 64
transistors (6 doublings) [Moore, 1965] and naively extrapolating it out predicted personal computers and
smartphones(aniPhone11has8.5billiontransistors). Ifweobservedecadesofexponentialimprovementin
thealgorithmicefficiencyofAI,whatmightitleadto? We’renotsure. Thattheseresultsmakeusaskthis
questionisamodestupdateforustowardsafuturewithpowerfulAIservicesandtechnology. Conversely,if
weweretostartonlyobservingincrementalgains(say2ximprovementsevery5years),wethinkthat’dbea
meaningfulandwidelyunderstandableindicatorthatalgorithmicprogresshadsloweddown.
More ambitiously, we hope that reporting on algorithmic efficiency improvements will become a strong
and useful norm in the AI community. Improved performance is what AI algorithms are ultimately judged
by. Algorithmically efficient models on benchmarks of interest are promising candidates for scaling up
and potentially achieving overall top performance. Efficiency is straightforward to measure, as it’s just a
meaningful slice of the learning curves that all experiments generate. Given these considerations and the
primacyofefficiencyinmeasuringprogressincomputerscience,webelievethere’sastrongcaseforreporting
onandtrackingtrainingefficiencystatesoftheartovertime.
15

7 Acknowledgements
We’dliketothankthefollowingpeoplehelpfulconversationsand/orfeedbackonthispaper: DarioAmodei,
JackClark,AlecRadford,PaulChristiano,SamMcCandlish,IlyaSutskever,JacobSteinhardt,JaredKaplan,
AmandaAskell,JohnSchulman,RyanLowe,TomHenighan,JacobHilton,AsyaBergal,KatjaGrace,Ryan
Carey,NicholasJoseph,andGeoffreyIrving.
ThankstoNikiParmarforprovidingtherelevantpointsfromthetransformerlearningcurves[Vaswanietal.,
2017].
AlsothankstoMingxingTanforprovidingtherelevantpointsfromEfficientNetlearningcurvesandrunning
anexperimentwithreducedwarmup[Tan&Le,2019].
References
[Amodei&Hernandez,2018] Amodei, D. & Hernandez, D. (2018). AI and Compute. https://openai.com/
blog/ai-and-compute/. 3,12,14
[Bixby,2012] Bixby, R.E.(2012). Abriefhistoryoflinearandmixed-integerprogrammingcomputation.
DocumentaMathematica,ExtraVolumeISMP,107–121. 4,5
[Bloometal.,2017] Bloom,N.,Jones,C.I.,VanReenen,J.,&Webb,M.(2017). AreIdeasGettingHarder
toFind? WorkingPaper23782,NationalBureauofEconomicResearch. 6
[Colemanetal.,2017] Coleman, C., Narayanan, D., Kang, D., Zhao, T., Zhang, J., Nardi, L., Bailis, P.,
Olukotun, K., Ré, C., & Zaharia, M. (2017). Dawnbench: An end-to-end deep learning benchmark and
competition. 5
[Dengetal.,2009] Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009). ImageNet: A
Large-ScaleHierarchicalImageDatabase. InCVPR09. 3
[Devlinetal.,2018] Devlin, J., Chang, M., Lee, K., & Toutanova, K. (2018). BERT: pre-training of deep
bidirectionaltransformersforlanguageunderstanding. CoRR,abs/1810.04805. 3,9
[Grace,2013] Grace,K.(2013). Algorithmicprogressinsixdomains. arxiv. 4
[Graceetal.,2017] Grace,K.,Salvatier,J.,Dafoe,A.,Zhang,B.,&Evans,O.(2017). Whenwillaiexceed
humanperformance? evidencefromaiexperts. 3
[Guptaetal.,2015] Gupta, S., Agrawal, A., Gopalakrishnan, K., & Narayanan, P. (2015). Deep learning
withlimitednumericalprecision. InInternationalConferenceonMachineLearning(pp.1737–1746). 13
[Heetal.,2015] He,K.,Zhang,X.,Ren,S.,&Sun,J.(2015). Deepresiduallearningforimagerecognition.
6
[Hoare,1962] Hoare,C.A.(1962). Quicksort. TheComputerJournal,5(1),10–16. 3
[Howardetal.,2017] Howard, A. G., Zhu, M., Chen, B., Kalenichenko, D., Wang, W., Weyand, T., An-
dreetto, M., &Adam, H.(2017). Mobilenets: Efficientconvolutionalneuralnetworksformobilevision
applications. 6
[Huangetal.,2016] Huang,G.,Liu,Z.,vanderMaaten,L.,&Weinberger,K.Q.(2016).Denselyconnected
convolutionalnetworks. 6
[Huang,2017] Huang,J.(2017). Shufflenetinpytorch.https://github.com/jaxony/shufflenet. 6
[Iandolaetal.,2016] Iandola, F. N., Han, S., Moskewicz, M. W., Ashraf, K., Dally, W. J., & Keutzer, K.
(2016). Squeezenet: Alexnet-levelaccuracywith50xfewerparametersand<0.5mbmodelsize. 6
[Ioffe&Szegedy,2015] Ioffe, S. & Szegedy, C. (2015). Batch normalization: Accelerating deep network
trainingbyreducinginternalcovariateshift. 11
[Jiaetal.,2018] Jia,X.,Song,S.,He,W.,Wang,Y.,Rong,H.,Zhou,F.,Xie,L.,Guo,Z.,Yang,Y.,Yu,L.,
etal.(2018). Highlyscalabledeeplearningtrainingsystemwithmixed-precision: Trainingimagenetin
fourminutes. arXivpreprintarXiv:1807.11205. 13
[Jovanovic&Rousseau,2005] Jovanovic, B. & Rousseau, P. L. (2005). General purpose technologies. In
Handbookofeconomicgrowth,volume1(pp.1181–1224).Elsevier. 15
[Krizhevskyetal.,2012] Krizhevsky,A.,Sutskever,I.,&Hinton,G.E.(2012). Imagenetclassificationwith
deepconvolutionalneuralnetworks. InF.Pereira,C.J.C.Burges,L.Bottou,&K.Q.Weinberger(Eds.),
AdvancesinNeuralInformationProcessingSystems25(pp.1097–1105).CurranAssociates,Inc. 3
16

[LeCunetal.,1998] LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning ap-
pliedtodocumentrecognition. ProceedingsoftheIEEE,86(11),2278–2324. 3
[Lipton&Steinhardt,2018] Lipton, Z. C. & Steinhardt, J. (2018). Troubling trends in machine learning
scholarship. 10
[Liuetal.,2019] Liu, X., He, P., Chen, W., &Gao, J.(2019). Multi-taskdeepneuralnetworksfornatural
languageunderstanding. 3
[Maetal.,2018] Ma,N.,Zhang,X.,Zheng,H.-T.,&Sun,J.(2018). Shufflenetv2: Practicalguidelinesfor
efficientcnnarchitecturedesign. 6
[McCandlishetal.,2018] McCandlish, S., Kaplan, J., Amodei, D., & Team, O. D. (2018). An empirical
modeloflarge-batchtraining. 12,13
[Mnihetal.,2013] Mnih,V.,Kavukcuoglu,K.,Silver,D.,Graves,A.,Antonoglou,I.,Wierstra,D.,&Ried-
miller,M.(2013). Playingatariwithdeepreinforcementlearning. arXivpreprintarXiv:1312.5602. 12
[Moore,1965] Moore, G. E. (1965). Cramming more components onto integrated circuits. Electronics,
38(8). 3,14,15
[OpenAIetal.,2019] OpenAI,:,Berner,C.,Brockman,G.,Chan,B.,Cheung,V.,De˛biak,P.,Dennison,C.,
Farhi, D., Fischer, Q., Hashme, S., Hesse, C., Józefowicz, R., Gray, S., Olsson, C., Pachocki, J., Petrov,
M.,deOliveiraPinto,H.P.,Raiman,J.,Salimans,T.,Schlatter,J.,Schneider,J.,Sidor,S.,Sutskever,I.,
Tang,J.,Wolski,F.,&Zhang,S.(2019). Dota2withlargescaledeepreinforcementlearning. 9,19
[Paszkeetal.,2017] Paszke,A.,Gross,S.,Chintala,S.,Chanan,G.,Yang,E.,DeVito,Z.,Lin,Z.,Desmai-
son,A.,Antiga,L.,&Lerer,A.(2017). AutomaticdifferentiationinPyTorch. InNIPSAutodiffWorkshop.
6
[Radfordetal.,] Radford,A.,Wu,J.,Child,R.,Luan,D.,Amodei,D.,&Sutskever,I. Languagemodelsare
unsupervisedmultitasklearners. 9
[Raffeletal.,2019] Raffel,C.,Shazeer,N.,Roberts,A.,Lee,K.,Narang,S.,Matena,M.,Zhou,Y.,Li,W.,
&Liu,P.J.(2019). Exploringthelimitsoftransferlearningwithaunifiedtext-to-texttransformer. 9
[RaymondPerrault&Niebles,2019] Raymond Perrault, Yoav Shoham, E. B. J. C. J. E. B. G. T. L. J. M.
S.M.&Niebles,J.C.(2019). “TheAIIndex2019AnnualReport”. Technicalreport,AIIndexSteering
Committee,Human-CenteredAIInstitute,StanfordUniversity,Stanford,CA. 6
[Russakovskyetal.,2015] Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z.,
Karpathy,A.,Khosla,A.,Bernstein,M.,etal.(2015). Imagenetlargescalevisualrecognitionchallenge.
Internationaljournalofcomputervision,115(3),211–252. 3
[Sandleretal.,2018] Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., & Chen, L.-C. (2018). Mo-
bilenetv2: Invertedresidualsandlinearbottlenecks. 6
[Sastryetal.,2019] Sastry,G.,Clark,J.,Brockman,G.,&Sutskever,I.(2019). AddendumtoAIandCom-
pute: Computeusedinolderheadlineresults. 3
[Silveretal.,2016] Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., van den Driessche, G.,
Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J.,
Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T., & Hassabis, D.
(2016). Masteringthegameofgowithdeepneuralnetworksandtreesearch. Nature,529,484–503. 9,18
[Silveretal.,2018] Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot,
M., Sifre, L., Kumaran, D., Graepel, T., Lillicrap, T., Simonyan, K., & Hassabis, D. (2018). A general
reinforcementlearningalgorithmthatmasterschess,shogi,andgothroughself-play. Science,362(6419),
1140–1144. 3,9,18
[Silveretal.,2017] Silver,D.,Schrittwieser,J.,Simonyan,K.,Antonoglou,I.,Huang,A.,Guez,A.,Hubert,
T.,Baker,L.,Lai,M.,Bolton,A.,Chen,Y.,Lillicrap,T.,Hui,F.,Sifre,L.,vandenDriessche,G.,Graepel,
T.,&Hassabis,D.(2017). Masteringthegameofgowithouthumanknowledge. Nature,550,354–. 9,18
[Simonyan&Zisserman,2014] Simonyan, K. & Zisserman, A. (2014). Very deep convolutional networks
forlarge-scaleimagerecognition. 6
[Sutskeveretal.,2014] Sutskever,I.,Vinyals,O.,&Le,Q.V.(2014). Sequencetosequencelearningwith
neuralnetworks. CoRR,abs/1409.3215. 10,18
[Sutton,2019] Sutton,R.(2019). Thebitterlesson. IncompleteIdeas(blog),March,13. 12
17

[Szegedyetal.,2014] Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D., Van-
houcke,V.,&Rabinovich,A.(2014). Goingdeeperwithconvolutions. 6,11
[Tan&Le,2019] Tan, M. & Le, Q. V. (2019). Efficientnet: Rethinking model scaling for convolutional
neuralnetworks. 6,10,11,16
[vandenOordetal.,2017] van den Oord, A., Li, Y., Babuschkin, I., Simonyan, K., Vinyals, O.,
Kavukcuoglu,K.,vandenDriessche,G.,Lockhart,E.,Cobo,L.C.,Stimberg,F.,Casagrande,N.,Grewe,
D.,Noury,S.,Dieleman,S.,Elsen,E.,Kalchbrenner,N.,Zen,H.,Graves,A.,King,H.,Walters,T.,Belov,
D.,&Hassabis,D.(2017). Parallelwavenet: Fasthigh-fidelityspeechsynthesis. 3
[Vaswanietal.,2017] Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,Kaiser,
L.,&Polosukhin,I.(2017). Attentionisallyouneed. CoRR,abs/1706.03762. 10,16,18
[Wangetal.,2018] Wang,A.,Singh,A.,Michael,J.,Hill,F.,Levy,O.,&Bowman,S.R.(2018). GLUE:A
multi-taskbenchmarkandanalysisplatformfornaturallanguageunderstanding. CoRR,abs/1804.07461.
3
[Xiao,2017] Xiao, H. (2017). Pytorch mobilenet implementation of "mobilenets: Efficient convolutional
neuralnetworksformobilevisionapplications".https://github.com/marvis/pytorch-mobilenet. 6
[Xieetal.,2016] Xie,S.,Girshick,R.,Dollár,P.,Tu,Z.,&He,K.(2016). Aggregatedresidualtransforma-
tionsfordeepneuralnetworks. 3,6
[Zagoruyko&Komodakis,2016] Zagoruyko,S.&Komodakis,N.(2016). Wideresidualnetworks. 6
[Zhangetal.,2019] Zhang, H., Dauphin, Y. N., & Ma, T. (2019). Fixup initialization: Residual learning
withoutnormalization. 11
[Zhangetal.,2017] Zhang, X., Zhou, X., Lin, M., & Sun, J. (2017). Shufflenet: An extremely efficient
convolutionalneuralnetworkformobiledevices. 6,10
[Zhu,2019] Zhu,L.(2019). 6
A CalculationsforefficiencyimprovementsinGo,Dota,andMachineTranslation
MachineTranslation: WeestimatethattheTransformer[Vaswanietal.,2017]required61xlesscompute
togettoSeq2Seq-levelofperformance[Sutskeveretal.,2014]onEnglishtoFrenchtranslationonWMT’14
3yearslater. Thisestimateisbasedon:
1. totaltrainingcomputeusedbythetransformerbasemodelinoriginalpaper(3.3e18FLOPs)
2. computeestimateforSeq2SeqinAIandCompute(4.0e19FLOPs)
3. the base transformer got to Seq2Seq level around 20% of the way through it’s run. (provided by
authorsoftransformerpaper).
4.0e19/(0.20 3.3e18)=61
⇤
We estimate the the Transformer [Vaswani et al., 2017] required 9x less compute to get to GMNT-level of
performanceonEnglishtoFrenchtranslationonWMT-141yearlater. Thisestimateisbasedon:
1. totaltrainingcomputeusedbythetransformerbigmodelinoriginalpaper(2.3e19FLOPs)
2. computeestimateforGMNTtransformerpaper(1.4e20FLOPs)
3. the base transformer got to Seq2Seq level around 68% of the way through it’s run. (provided by
authorsoftransformerpaper).
1.4e20/(0.68 2.3e19)=9
⇤
AlphaGoZerotoAlphaZero: WeestimatethatAlphaZero[Silveretal.,2018]required8xlesscompute
to get to AlphaGo Zero [Silver et al., 2017] level approximately one year later. We don’t currently have
enoughinformationtocomparetoAlphaGoLee[Silveretal.,2016].Thisisbasedon:
1. anestimated4.4xdecreaseintotalFLOPsusedtotrainAlphaZeroinAIandCompute
2. it took AlphaZero 390,000 of the 700,000 steps it was trained for to match AlphaGo Zero perfor-
mance.
4.4 (700,000/390,000)=8
⇤
18

OpenAIFiveRerun: OpenAIFive"Rerun"gottothesameskilllevelfromscratchonthefinalenvironment
withoutsurgeryusing5xlesscompute2monthsaftertheOGmatch[OpenAIetal.,2019]. However,some
hardtopinportionoftheadditionalcostcamefromachangingenvironment,astherewerebalancechange
patchesapproximatelyevery2weeksduringtheoriginal10monthtrainingperiod.
B Calculationsforefficiencyimprovementsinimageclassification
Table3 FLOPsrequiredtoreachsameAlexNetlevelaccuracy
teraflop/s-days Experiment Epochs gigaflops/img gigaflops/img gigaflops/img
(used) (THOP) (paper)
367.7 Vgg-11 12 7.98 7.98 -
308.0 Wide_ResNet_50 7 11.46 11.46 -
266.1 AlexNet 90 0.77 0.77 -
118.6 Resnet-50 8 3.86 3.86 -
118.5 Resnet-34 9 3.43 3.43 -
115.3 ResNext_50 7 4.29 4.29 -
97.9 Resnet-18 15 1.70 1.70 -
82.9 DenseNet121 8 2.70 2.70 -
73.1 Squeezenet_v1_1 53 0.36 0.36 -
61.4 GoogLeNet 8 2.00 2.00 -
24.0 MobileNet_v1 11 0.57 0.58 0.57
20.2 MobileNet_v2 16 0.33 0.33 -
15.4 ShuffleNet_v2_1_5x 13 0.31 0.31 -
12.9 ShuffleNet_v1_1x 24 0.14 0.15 0.14
10.8 ShuffleNet_v2_1x 20 0.14 0.15 0.14
6.0 EfficientNet-b0 4 0.39 - 0.39
Wheretraining_flops=epochs flops_per_image images_per_epoch
Withimages_per_epoch=1.28 ⇤ 106andateraflop/ ⇤ s day =1e12 (24 60 60s/day)
⇤   ⇤ ⇤ ⇤
19

C Accuracyachievedinrelevantmodels
Table4 Top-5finaltrainingaccuracycomparisonsforrelevantmodels
Experiment MyTop-5 Pytorch/ExamplesTop-5 PaperTop-5 SingleCropValidation*
AlexNet 79.0% 79.1% 83.0% ?
Vgg-11 86.8% 88.6% 93.0% no
GoogLeNet 88.0% 89.5% 89.9% yes
Resnet-50 92.8% 92.9% 93.3% yes
Squeezenet_v1_1 80.6% 80.6% 80.3% ?
Table5 Top-1finaltrainingaccuracycomparisonsforrelevantmodels
Experiment MyTop-1 Pytorch/ExamplesTop-1 PaperTop-1 SingleCropValidation*
MobileNet_v1 71.0% - 70.6% yes
MobileNet_v2 68.5% 71.9% 72.0% yes
ShuffleNet_v1_1x 64.6% - 67.6% yes
ShuffleNet_v2_1_5x 69.3% 69.4% 71.6% yes
*Weuseasinglecenter224x224cropforevaluatingperformanceonthevalidationdatapointsforallofour
models,butnotalloforiginalpapersevaluateperformanceinthismanner.
20
