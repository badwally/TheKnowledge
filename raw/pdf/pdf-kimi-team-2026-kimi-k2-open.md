---
id: pdf-kimi-team-2026-kimi-k2-open
type: pdf
title: 'Kimi K2: Open Agentic Intelligence'
url: ''
authors:
- Kimi Team
- Yifan Bai
- Yiping Bao
- Guanduo Chen
- Jiahao Chen
- Ningxin Chen
- Ruijue Chen
- Yanru Chen
- Yuankun Chen
- Yutian Chen
- Zhuofu Chen
- Jialei Cui
- Hao Ding
- Mengnan Dong
- Angang Du
- Chenzhuang Du
- Dikang Du
- Yulun Du
- Yu Fan
- Yichen Feng
- Kelin Fu
- Bofei Gao
- Hongcheng Gao
- Peizhong Gao
- Tong Gao
- Xinran Gu
- Longyu Guan
- Haiqing Guo
- Jianhang Guo
- Hao Hu
- Xiaoru Hao
- Tianhong He
- Weiran He
- Wenyang He
- Chao Hong
- Yangyang Hu
- Zhenxing Hu
- Weixiao Huang
- Zhiqi Huang
- Zihao Huang
- Tao Jiang
- Zhejun Jiang
- Xinyi Jin
- Yongsheng Kang
- Guokun Lai
- Cheng Li
- Fang Li
- Haoyang Li
- Ming Li
- Wentao Li
- Yanhao Li
- Yiwei Li
- Zhaowei Li
- Zheming Li
- Hongzhan Lin
- Xiaohan Lin
- Zongyu Lin
- Chengyin Liu
- Chenyu Liu
- Hongzhang Liu
- Jingyuan Liu
- Junqi Liu
- Liang Liu
- Shaowei Liu
- T. Y. Liu
- Tianwei Liu
- Weizhou Liu
- Yangyang Liu
- Yibo Liu
- Yiping Liu
- Yue Liu
- Zhengying Liu
- Enzhe Lu
- Lijun Lu
- Shengling Ma
- Xinyu Ma
- Yingwei Ma
- Shaoguang Mao
- Jie Mei
- Xin Men
- Yibo Miao
- Siyuan Pan
- Yebo Peng
- Ruoyu Qin
- Bowen Qu
- Zeyu Shang
- Lidong Shi
- Shengyuan Shi
- Feifan Song
- Jianlin Su
- Zhengyuan Su
- Xinjie Sun
- Flood Sung
- Heyi Tang
- Jiawen Tao
- Qifeng Teng
- Chensi Wang
- Dinglu Wang
- Feng Wang
- Haiming Wang
- Jianzhou Wang
- Jiaxing Wang
- Jinhong Wang
- Shengjie Wang
- Shuyi Wang
- Yao Wang
- Yejie Wang
- Yiqin Wang
- Yuxin Wang
- Yuzhi Wang
- Zhaoji Wang
- Zhengtao Wang
- Zhexu Wang
- Chu Wei
- Qianqian Wei
- Wenhao Wu
- Xingzhe Wu
- Yuxin Wu
- Chenjun Xiao
- Xiaotong Xie
- Weimin Xiong
- Boyu Xu
- Jing Xu
- Jinjing Xu
- L. H. Xu
- Lin Xu
- Suting Xu
- Weixin Xu
- Xinran Xu
- Yangchuan Xu
- Ziyao Xu
- Junjie Yan
- Yuzi Yan
- Xiaofei Yang
- Ying Yang
- Zhen Yang
- Zhilin Yang
- Zonghan Yang
- Haotian Yao
- Xingcheng Yao
- Wenjie Ye
- Zhuorui Ye
- Bohong Yin
- Longhui Yu
- Enming Yuan
- Hongbang Yuan
- Mengjie Yuan
- Haobing Zhan
- Dehao Zhang
- Hao Zhang
- Wanlu Zhang
- Xiaobin Zhang
- Yangkun Zhang
- Yizhi Zhang
- Yongting Zhang
- Yu Zhang
- Yutao Zhang
- Yutong Zhang
- Zheng Zhang
- Haotian Zhao
- Yikai Zhao
- Huabin Zheng
- Shaojie Zheng
- Jianren Zhou
- Xinyu Zhou
- Zaida Zhou
- Zhen Zhu
- Weiyu Zhuang
- Xinxing Zu
ingested_at: '2026-04-29T16:17:14Z'
content_hash: sha256:66c0e532f13bd96ea2b68d07ab701d2bd52e5cdd35fd3a5fd5eaa3e81cfa09d0
source_path: raw/pdf/pdf-kimi-team-2026-kimi-k2-open.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 32
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__947f6c4c.pdf
published_at: '2026'
---
KIMI K2: OPEN AGENTIC INTELLIGENCE
TECHNICALREPORTOFKIMIK2
KimiTeam
ABSTRACT
WeintroduceKimiK2,aMixture-of-Experts(MoE)largelanguagemodelwith32billionactivated
parametersand1trilliontotalparameters. WeproposetheMuonClipoptimizer,whichimprovesupon
MuonwithanovelQK-cliptechniquetoaddresstraininginstabilitywhileenjoyingtheadvanced
tokenefficiencyofMuon. BasedonMuonClip,K2waspre-trainedon15.5trilliontokenswithzero
lossspike. Duringpost-training,K2undergoesamulti-stagepost-trainingprocess,highlightedbya
large-scaleagenticdatasynthesispipelineandajointreinforcementlearning(RL)stage,wherethe
modelimprovesitscapabilitiesthroughinteractionswithrealandsyntheticenvironments.
Kimi K2 achieves state-of-the-art performance among open-source non-thinking models, with
strengths in agentic capabilities. Notably, K2 obtains 66.1 on Tau2-Bench, 76.5 on ACEBench
(En),65.8onSWE-BenchVerified,and47.3onSWE-BenchMultilingual—surpassingmostopen
andclosed-sourcedbaselinesinnon-thinkingsettings. Italsoexhibitsstrongcapabilitiesincoding,
mathematics,andreasoningtasks,withascoreof53.7onLiveCodeBenchv6,49.5onAIME2025,
75.1onGPQA-Diamond,and27.1onOJBench,allwithoutextendedthinking. Theseresultsposition
Kimi K2 as one of the most capable open-source large language models to date, particularly in
softwareengineeringandagentictasks. Wereleaseourbaseandpost-trainedmodelcheckpoints1to
facilitatefutureresearchandapplicationsofagenticintelligence.
SWE-bench Verified SWE-bench Multilingual LiveCodeBench v6 OJBench
80 80 80 80
72.5
65.8
60 54.6 60 47.3 51.0 60 53.7 46.9 44.7 47.4 44.7 60
2 4 0 0 38.8 34.4 2 4 0 0 25.8 20.9 31.5 2 4 0 0 37.0 2 4 0 0 27.1 24.0 19.5 19.6 19.5
11.3
0 0 0 0
Ki A mi g -K D e 2 e - e n In p t s S t i e r c u e Q c k a t - w V n e 3 n - d 0 3 3 -2 C 2 3 4 5 o B O m - p A e 2 p n 2 A e B I t G it C P i T l v a -4 u e . d 1 e C 4 o O d pu i s ng Kimi-K D 2 e - e In p s S t e ru e Q c k t - w V e 3 n -0 3 3 -2 2 3 4 5B O - p A e 2 n 2 A B I C G l P a T u - d 4 e .1 4 Sonnet Kimi D -K e 2 e - p In S s e t Q e ru k w c -V e t n 3 3 -0 -2 3 3 2 O 5 4 G B p e - e A m n 2 A i 2 n I B i G C 2. P l 5 a T u - F 4 d la . e 1 s 4 h O no p n u - s thinking Kimi D -K e 2 e - p In S s e t Q e ru k w c -V e t n 3 3 -0 -2 3 3 2 O 5 4 G B p e - e A m n 2 A i 2 n I B i G C 2. P l 5 a T u - F 4 d la . e 1 s 4 h O no p n u - s thinking
Tau2-bench micro-average AceBench (en) AIME 2025 GPQA-Diamond
100 100 100 100
75 66.1 67.6 75 76.5 72.7 70.5 80.1 75.6 74.5 75 75 75.1 68.4 62.9 66.3 74.9 68.2
50 48.8 54.4 50 50 49.5 46.7 46.6 50
37.3 41.0 37.0 33.9
25 25 25 24.7 25
0 0 0 0
Kimi D -K e 2 e - p In S s e t Q e ru k w c -V e t n 3 3 -0 -2 3 3 2 O 5 4 G B p e - e A m n 2 A i 2 n I B i G C 2. P l 5 a T u - F 4 d la . e 1 s 4 h O no p n u - s thinking Kimi D -K e 2 e - p In S s e t Q e ru k w c -V e t n 3 3 -0 -2 3 3 2 O 5 4 G B p e - e A m n 2 A i 2 n I B i G C 2. P l 5 a T u - F 4 d la . e 1 s 4 h O no p n u - s thinking Kimi D -K e 2 e - p In S s e t Q e ru k w c -V e t n 3 3 -0 -2 3 3 2 O 5 4 G B p e - e A m n 2 A i 2 n I B i G C 2. P l 5 a T u - F 4 d la . e 1 s 4 h O no p n u - s thinking Kimi D -K e 2 e - p In S s e t Q e ru k w c -V e t n 3 3 -0 -2 3 3 2 O 5 4 G B p e - e A m n 2 A i 2 n I B i G C 2. P l 5 a T u - F 4 d la . e 1 s 4 h O no p n u - s thinking
Tool Use Math & STEM
Figure1: KimiK2mainresults.2
1https://huggingface.co/moonshotai/Kimi-K2-Instruct
2Allmodelsevaluatedabovearenon-thinkingmodels.ForSWE-benchMultilingual,weevaluatedonlyClaude4Sonnetbecause
thecostofClaude4Opuswasprohibitive.
5202
luJ
82
]GL.sc[
1v43502.7052:viXra

KimiK2 TECHNICALREPORT
1 Introduction
The development of Large Language Models (LLMs) is undergoing a profound paradigm shift towards Agentic
Intelligence–thecapabilitiesformodelstoautonomouslyperceive,plan,reason,andactwithincomplexanddynamic
environments. This transition marks a departure from static imitation learning towards models that actively learn
throughinteractions,acquirenewskillsbeyondtheirtrainingdistribution,andadaptbehaviorthroughexperiences[63].
ItisbelievedthatthisapproachallowsanAIagenttogobeyondthelimitationofstatichuman-generateddata,and
acquiresuperhumancapabilitiesthroughitsownexplorationandexploitation. Agenticintelligenceisthusrapidly
emergingasadefiningcapabilityforthenextgenerationoffoundationmodels,withwide-rangingimplicationsacross
tooluse,softwaredevelopment,andreal-worldautonomy.
Achieving agentic intelligence introduces challenges in both pre-training and post-training. Pre-training must en-
dow models with broad general-purpose priors under constraints of limited high-quality data, elevating token effi-
ciency—learningsignalpertoken—asacriticalscalingcoefficient. Post-trainingmusttransformthosepriorsinto
actionablebehaviors,yetagenticcapabilitiessuchasmulti-stepreasoning,long-termplanning,andtoolusearerare
innaturaldataandcostlytoscale. Scalablesynthesisofstructured,high-qualityagentictrajectories,combinedwith
generalreinforcementlearning(RL)techniquesthatincorporatepreferencesandself-critique,areessentialtobridge
thisgap.
Inthiswork,weintroduceKimiK2,a1.04trillion-parameterMixture-of-Experts(MoE)LLMwith32billionactivated
parameters,purposefullydesignedtoaddressthecorechallengesandpushtheboundariesofagenticcapability. Our
contributionsspanboththepre-trainingandpost-trainingfrontiers:
• We present MuonClip, a novel optimizer that integrates the token-efficient Muon algorithm with a stability-
enhancingmechanismcalledQK-Clip. UsingMuonClip,wesuccessfullypre-trainedKimiK2on15.5trillion
tokenswithoutasinglelossspike.
• Weintroducealarge-scaleagenticdatasynthesispipelinethatsystematicallygeneratestool-usedemonstrations
viasimulatedandreal-worldenvironments. Thissystemconstructsdiversetools,agents,tasks,andtrajectoriesto
createhigh-fidelity,verifiablycorrectagenticinteractionsatscale.
• Wedesignageneralreinforcementlearningframeworkthatcombinesverifiablerewards(RLVR)withaself-
critiquerubricrewardmechanism. Themodellearnsnotonlyfromexternallydefinedtasksbutalsofromevaluating
itsownoutputs,extendingalignmentfromstaticintoopen-endeddomains.
KimiK2demonstratesstrongperformanceacrossabroadspectrumofagenticandfrontierbenchmarks. Itachieves
scores of 66.1 on Tau2-bench, 76.5 on ACEBench (en), 65.8 on SWE-bench Verified, and 47.3 on SWE-bench
Multilingual,outperformingmostopen-andclosed-weightbaselinesundernon-thinkingevaluationsettings,closingthe
gapwithClaude4OpusandSonnet. Incoding,mathematics,andbroaderSTEMdomains,KimiK2achieves53.7
onLiveCodeBenchv6,27.1onOJBench,49.5onAIME2025,and75.1onGPQA-Diamond,furtherhighlighting
its capabilities in general tasks. On the LMSYS Arena leaderboard (July 17, 2025)3, Kimi K2 ranks as the top 1
open-sourcemodeland5thoverallbasedonover3,000uservotes.
TospurfurtherprogressinAgenticIntelligence,weareopen-sourcingourbaseandpost-trainedcheckpoints,enabling
thecommunitytoexplore,refine,anddeployagenticintelligenceatscale.
2 Pre-training
The base model of Kimi K2 is a trillion-parameter mixture-of-experts (MoE) transformer [72] model, pre-trained
on15.5trillionhigh-qualitytokens. Giventheincreasinglylimitedavailabilityofhigh-qualityhumandata,weposit
that token efficiency is emerging as a critical coefficient in the scaling of large language models. To address this,
weintroduceasuiteofpre-trainingtechniquesexplicitlydesignedformaximizingtokenefficiency. Specifically,we
employthetoken-efficientMuonoptimizer[33,46]andmitigateitstraininginstabilitiesthroughtheintroductionof
QK-Clip. Additionally,weincorporatesyntheticdatagenerationtofurthersqueezetheintelligenceoutofavailable
high-qualitytokens. Themodelarchitecturefollowsanultra-sparseMoEwithmulti-headlatentattention(MLA)similar
toDeepSeek-V3[10],derivedfromempiricalscalinglawanalysis. Theunderlyinginfrastructureisbuilttooptimize
bothtrainingefficiencyandresearchefficiency.
3https://lmarena.ai/leaderboard/text
2

KimiK2 TECHNICALREPORT
2.1 MuonClip: StableTrainingwithWeightClipping
WetrainKimiK2usingthetoken-efficientMuonoptimizer[33],incorporatingweightdecayandconsistentupdate
RMSscaling[46]. ExperimentsinourpreviousworkMoonlight[46]showthat,underthesamecomputebudgetand
modelsize—andthereforethesameamountoftrainingdata—MuonsubstantiallyoutperformsAdamW[36,48],
makingitaneffectivechoiceforimprovingtokenefficiencyinlargelanguagemodeltraining.
TraininginstabilitywhenscalingMuon Despiteitsefficiency,scalingupMuontrainingrevealsachallenge:training
instabilityduetoexplodingattentionlogits,anissuethatoccursmorefrequentlywithMuonbutlesswithAdamW
inourexperiments. Existingmitigationstrategiesareinsufficient. Forinstance,logitsoft-cap[69]directlyclipsthe
attentionlogits,butthedotproductsbetweenqueriesandkeyscanstillgrowexcessivelybeforecappingisapplied. On
theotherhand,Query-KeyNormalization(QK-Norm)[11,81]isnotapplicabletomulti-headlatentattention(MLA),
becauseitsKeymatricesarenotfullymaterializedduringinference.
TamingMuonwithQK-Clip Toaddressthisissue,weproposeanovelweight-clippingmechanismQK-Clipto
explicitlyconstrainattentionlogits. QK-Clipworksbyrescalingthequeryandkeyprojectionweightspost-updateto
boundthegrowthofattentionlogits.
LettheinputrepresentationofatransformerlayerbeX. Foreachattentionheadh,itsquery,key,andvalueprojections
arecomputedas
Qh =XWh, Kh =XWh, Vh =XWh.
q k v
whereW ,W ,W aremodelparameters. Theattentionoutputis:
q k v
1
Oh =softmax QhKh Vh.
→
→d
! "
Wedefinethemaxlogit,aper-headscalar,asthemaximuminputtosoftmaxinthisbatchB:
1
Sh = maxmaxQhKh
max →dX B i,j i j→
↑
wherei,j areindicesofdifferenttokensinatrainingsampleX.
ThecoreideaofQK-ClipistorescaleW ,W wheneverSh exceedsatargetthresholdω.Importantly,thisoperation
k q max
doesnotaltertheforward/backwardcomputationinthecurrentstep—wemerelyusethemaxlogitasaguidingsignal
todeterminethestrengthtocontroltheweightgrowth.
Anaïveimplementationclipsallheadsatthesametime:
Wh εωWh Wh ε1 ωWh
q ↑ q k ↑ ↓ k
whereε = min(1,ω/S )withS = max Sh ,andϑisabalancingparametertypicallysetto0.5,applying
max max h max
equalscalingtoqueriesandkeys.
However,weobservethatinpractice,onlyasmallsubsetofheadsexhibitexplodinglogits. Inordertominimizeour
interventiononmodeltraining,wedetermineaper-headscalingfactorε =min(1,ω/Sh ),andopttoapplyper-head
h max
QK-Clip. Suchclippingisstraightforwardforregularmulti-headattention(MHA).ForMLA,weapplyclippingonly
onunsharedattentionheadcomponents:
• qC andk C (head-specificcomponents): eachscaledby→ε
h
• qR (head-specificrotary): scaledbyε
h
,
• k R (sharedrotary): leftuntouchedtoavoideffectacrossheads.
MuonClip: TheNewOptimizer WeintegrateMuonwithweightdecay,consistentRMSmatching,andQK-Clip
intoasingleoptimizer,whichwerefertoasMuonClip(seeAlgorithm1).
WedemonstratetheeffectivenessofMuonClipfromseveralscalingexperiments.First,wetrainamid-scale9Bactivated
and53BtotalparametersMixture-of-Experts(MoE)modelusingthevanillaMuon. AsshowninFigure2(Left),we
observethatthemaximumattentionlogitsquicklyexceedamagnitudeof1000,showingthatattentionlogitsexplosion
isalreadyevidentinMuontrainingtothisscale. Maxlogitsatthislevelusuallyresultininstabilityduringtraining,
includingsignificantlossspikesandoccasionaldivergence.
3

KimiK2 TECHNICALREPORT
Algorithm1MuonClipOptimizer
1: foreachtrainingsteptdo
2: //1. Muonoptimizerstep
3: foreachweightW R n ↔ mdo
↓
4: M t =µM t 1 +G t ϖM 0 =0,G t isthegradofW t ,µismomentum
↓
5: O t =Newton-Schulz(M t ) max(n,m) 0.2 ϖMatchAdamRMS
· ·
6: W t =W t
↓
1
↔
ϱ O t +ςW t#↓ 1 ϖlearningrateϱ,weightdecayς
7: endfor
$ %
8: //2. QK-Clip
9: foreachattentionheadhineveryattentionlayerofthemodeldo
10: ObtainSh alreadycomputedduringforward
max
11: ifSh >ω then
max
12: ε ω/Sh
↑ max
13: Wh Wh →ε
qc ↑ qc·
14: Wh Wh →ε
kc ↑ kc·
15: Wh Wh ε
qr ↑ qr·
16: endif
17: endfor
18: endfor
Figure2: Left: Duringamid-scaletrainingrun,attentionlogitsrapidlyexceed1000,whichcouldleadtopotential
numericalinstabilitiesandeventrainingdivergence. Right: MaximumlogitsforKimiK2withMuonClipandω =100
overtheentiretrainingrun. Themaxlogitsrapidlyincreasetothecappedvalueof100,andonlydecaytoastablerange
afterapproximately30%ofthetrainingsteps,demonstratingtheeffectiveregulationeffectofQK-Clip.
Next,wedemonstratethatQK-ClipdoesnotdegrademodelperformanceandconfirmthattheMuonClipoptimizer
preservestheoptimizationcharacteristicsofMuonwithoutadverselyaffectingthelosstrajectory. Adetaileddiscussion
oftheexperimentdesignsandfindingsisprovidedintheAppendixD.
Finally,wetrainKimiK2,alarge-scaleMoEmodel,usingMuonClipwithω =100andmonitorthemaximumattention
logitsthroughoutthetrainingrun(Figure2(Right)). Initially,thelogitsarecappedat100duetoQK-Clip. Overthe
courseoftraining,themaximumlogitsgraduallydecaytoatypicaloperatingrangewithoutrequiringanyadjustmentto
ω. Importantly,thetraininglossremainssmoothandstable,withnoobservablespikes,asshowninFigure3,validating
thatMuonClipprovidesrobustandscalablecontroloverattentiondynamicsinlarge-scalelanguagemodeltraining.
2.2 Pre-trainingData: ImprovingTokenUtilitywithRephrasing
Tokenefficiencyinpre-trainingreferstohowmuchperformanceimprovementisachievedforeachtokenconsumed
duringtraining. Increasingtokenutility—theeffectivelearningsignaleachtokencontributes—enhancestheper-token
impactonmodelupdates,therebydirectlyimprovingtokenefficiency. Thisisparticularlyimportantwhenthesupplyof
high-qualitytokensislimitedandmustbemaximallyleveraged. Anaiveapproachtoincreasingtokenutilityisthrough
repeatedexposuretothesametokens,whichcanleadtooverfittingandreducedgeneralization.
4

KimiK2 TECHNICALREPORT
2.0
1.9
1.8
1.7
1.6
1.5
1.4
1.3
0 2 4 6 8 10 12 14 16
Tokens (Trillion)
ssoL
Figure3: Per-steptraininglosscurveofKimiK2,withoutsmoothingorsub-sampling. Itshowsnospikesthroughout
theentiretrainingprocess. Notethatweomittheverybeginningoftrainingforclarity.
Akeyadvancementinthepre-trainingdataofKimiK2overKimiK1.5istheintroductionofasyntheticdatageneration
strategytoincreasetokenutility.Specifically,acarefullydesignedrephrasingpipelineisemployedtoamplifythevolume
ofhigh-qualitytokenswithoutinducingsignificantoverfitting. Inthisreport, wedescribetwodomain-specialized
rephrasingtechniques—targetedrespectivelyattheKnowledgeandMathematicsdomains—thatenablethiscontrolled
dataaugmentation.
KnowledgeDataRephrasing Pre-trainingonnatural,knowledge-intensivetextpresentsatrade-off: asingleepoch
isinsufficientforcomprehensiveknowledgeabsorption,whilemulti-epochrepetitionyieldsdiminishingreturnsand
increasestheriskofoverfitting. Toimprovethetokenutilityofhigh-qualityknowledgetokens,weproposeasynthetic
rephrasingframeworkcomposedofthefollowingkeycomponents:
• Style-andperspective-diverseprompting: Toenhancelinguisticdiversitywhilemaintainingfactualintegrity,we
applyarangeofcarefullyengineeredprompts. Thesepromptsguidealargelanguagemodeltogeneratefaithful
rephrasingsoftheoriginaltextsinvariedstylesandfromdifferentperspectives.
• Chunk-wise autoregressive generation: To preserve global coherence and avoid information loss in long
documents,weadoptachunk-basedautoregressiverewritingstrategy. Textsaredividedintosegments,rephrased
individually,andthenstitchedbacktogethertoformcompletepassages. Thismethodmitigatesimplicitoutput
lengthlimitationsthattypicallyexistwithLLMs. AnoverviewofthispipelineispresentedinFigure4.
• Fidelityverification: Toensureconsistencybetweenoriginalandrewrittencontent,weperformfidelitychecks
thatcomparethesemanticalignmentofeachrephrasedpassagewithitssource. Thisservesasaninitialquality
controlsteppriortotraining.
Wecomparedatarephrasingwithmulti-epochrepetitionbytestingtheircorrespondingaccuracyonSimpleQA.We
experimentwithanearlycheckpointofK2andevaluatethreetrainingstrategies: (1)repeatingtheoriginaldatasetfor
10epochs,(2)rephrasingthedataonceandrepeatingitfor10epochs,and(3)rephrasingthedata10timeswitha
singletrainingpass. AsshowninTable1,theaccuracyconsistentlyimprovesacrossthesestrategies,demonstratingthe
efficacyofourrephrasing-basedaugmentation. Weextendedthismethodtootherlarge-scaleknowledgecorporaand
observedsimilarlyencouragingresults,andeachcorporaisrephrasedatmosttwice.
Table1: SimpleQAAccuracyunderthreerephrasing-epochconfigurations
#Rephrasings #Epochs SimpleQAAccuracy
0(rawwiki-text) 10 23.76
1 10 27.39
10 1 28.94
5

KimiK2 TECHNICALREPORT
4096 tokens
split full input excerpt together as context full output excerpt concat
256 tokens
partial input excerpt 1 rewrite model partial output excerpt 1
auto-regressive
partial input excerpt 2 rewrite model partial output excerpt 2
auto-regressive
... ... ...
Figure4: Auto-regressivechunk-wiserephrasingpipelineforlonginputexcerpts. Theinputis
splitintosmallerchunkswithpreservedcontext,rewrittensequentially,andthenconcatenated
intoafullrewrittenpassage.
MathematicsDataRephrasing Toenhancemathematicalreasoningcapabilities,werewritehigh-qualitymathemati-
caldocumentsintoa“learning-note”style,followingthemethodologyintroducedinSwallowMath[15]. Inaddition,
weincreaseddatadiversitybytranslatinghigh-qualitymathematicalmaterialsfromotherlanguagesintoEnglish.
Althoughinitialexperimentswithrephrasedsubsetsofourdatasetsshowpromisingresults,theuseofsyntheticdata
asastrategyforcontinuedscalingremainsanactiveareaofinvestigation. Keychallengesincludegeneralizingthe
approachtodiversesourcedomainswithoutcompromisingfactualaccuracy,minimizinghallucinationsandunintended
toxicity,andensuringscalabilitytolarge-scaledatasets.
Pre-trainingDataOverall TheKimiK2pre-trainingcorpuscomprises15.5trilliontokensofcurated,high-quality
dataspanningfourprimarydomains: WebText,Code,Mathematics,andKnowledge. Mostdataprocessingpipelines
follow the methodologies outlined in Kimi K1.5 [35]. For each domain, we performed rigorous correctness and
qualityvalidationanddesignedtargeteddataexperimentstoensurethecurateddatasetachievedbothhighdiversityand
effectiveness.
2.3 ModelArchitecture
KimiK2isa1.04trillion-parameterMixture-of-Experts(MoE)transformermodelwith32billionactivatedparameters.
ThearchitecturefollowsasimilardesigntoDeepSeek-V3[10],employingMulti-headLatentAttention(MLA)[44]as
theattentionmechanism,withamodelhiddendimensionof7168andanMoEexperthiddendimensionof2048. Our
scalinglawanalysisrevealsthatcontinuedincreasesinsparsityyieldsubstantialperformanceimprovements,which
motivatedustoincreasethenumberofexpertsto384,comparedto256inDeepSeek-V3. Toreducecomputational
overheadduringinference,wecutthenumberofattentionheadsto64,asopposedto128inDeepSeek-V3. Table2
presentsadetailedcomparisonofarchitecturalparametersbetweenKimiK2andDeepSeek-V3.
Table2: ArchitecturalcomparisonbetweenKimiK2andDeepSeek-V3
DeepSeek-V3 KimiK2 !
#Layers 61 61 =
TotalParameters 671B 1.04T 54%
↗
ActivatedParameters 37B 32.6B 13%
↘
Experts(total) 256 384 50%
↗
ExpertsActiveperToken 8 8 =
SharedExperts 1 1 =
AttentionHeads 128 64 50%
↘
NumberofDenseLayers 3 1 67%
↘
ExpertGrouping Yes No -
6

KimiK2 TECHNICALREPORT
SparsityScalingLaw WedevelopasparsityscalinglawtailoredfortheMixture-of-Experts(MoE)modelfamily
usingMuon. Sparsityisdefinedastheratioofthetotalnumberofexpertstothenumberofactivatedexperts. Through
carefullycontrolledsmall-scaleexperiments,weobservethat—underafixednumberofactivatedparameters(i.e.,
constantFLOPs)—increasingthetotalnumberofexperts(i.e.,increasingsparsity)consistentlylowersboththetraining
andvalidationloss,therebyenhancingoverallmodelperformance(Figure5). Concretely,underthecompute-optimal
sparsityscalinglaw,achievingthesamevalidationlossof1.5,sparsity48reducesFLOPsby1.69!,1.39!,and1.15!
comparedtosparsitylevels8,16,and32,respectively. Thoughincreasingsparsityleadstobetterperformance,this
gaincomeswithincreasedinfrastructurecomplexity. Tobalancemodelperformancewithcost,weadoptasparsityof
48forKimiK2,activating8outof384expertsperforwardpass.
Figure5: SparsityScalingLaw. Increasingsparsityleads Figure6:Scalingcurvesformodelswithnumberofatten-
toimprovedmodelperformance. Wefixedthenumberof tionheadsequalstonumberoflayersandtheircounter-
activatedexpertsto8andthenumberofsharedexperts partswithdoubledattentionheads. Doublingthenumber
to1,andvariedthetotalnumberofexperts,resultingin ofattentionheadsleadstoareductioninvalidationloss
modelswithdifferentsparsitylevels. ofapproximately0.5%to1.2%.
NumberofAttentionHeads DeepSeek-V3[10]setsthenumberofattentionheadstoroughlytwicethenumberof
modellayerstobetterutilizememorybandwidthandenhancecomputationalefficiency. However,asthecontextlength
increases,doublingthenumberofattentionheadsleadstosignificantinferenceoverhead,reducingefficiencyatlonger
sequencelengths. Thisbecomesamajorlimitationinagenticapplications,whereefficientlongcontextprocessingis
essential. Forexample,withasequencelengthof128k,increasingthenumberofattentionheadsfrom64to128,while
keepingthetotalexpertcountfixedat384,leadstoan83%increaseininferenceFLOPs. Toevaluatetheimpactof
thisdesign,weconductcontrolledexperimentscomparingconfigurationswherethenumberofattentionheadsequals
the number of layers against those with double number of heads, under varying training FLOPs. Under iso-token
trainingconditions,weobservethatdoublingtheattentionheadsyieldsonlymodestimprovementsinvalidationloss
(rangingfrom0.5%to1.2%)acrossdifferentcomputebudgets(Figure6). Giventhatsparsity48alreadyoffersstrong
performance,themarginalgainsfromdoublingattentionheadsdonotjustifytheinferencecost. Thereforewechoose
to64attentionheads.
2.4 TrainingInfrastructure
2.4.1 ComputeCluster
KimiK2wastrainedonaclusterequippedwithNVIDIAH800GPUs. EachnodeintheH800clustercontains2TB
RAMand8GPUsconnectedbyNVLinkandNVSwitchwithinnodes. Acrossdifferentnodes,8 400GbpsRoCE
≃
interconnectsareutilizedtofacilitatecommunications.
2.4.2 ParallelismforModelScaling
Trainingoflargelanguagemodelsoftenprogressesunderdynamicresourceavailability. Insteadofoptimizingone
parallelismstrategythat’sonlyapplicableunderspecificamountofresources,wepursueaflexiblestrategythatallows
KimiK2tobetrainedonanynumberofnodesthatisamultipleof32. Ourstrategyleveragesacombinationof16-way
7

KimiK2 TECHNICALREPORT
Computation Attn MLP Attn MLP MLP Attn WGrad MLP Attn WGrad
Communication EP-D EP-C EP-C EP-D EP-D EP-C PP EP-C EP-D PP
Offload Offload Offload Onload Load
1 2 3 4 1 2 3 4 5 6 7 2 1 3 2 4 3 5 4 6 1 2 3 4 5 6 7 8 5 6 7 8
1 2 3 4 1 2 3 4 5 2 1 3 2 4 3 5 4 6 1 7 2 8 3 4 5 6 7 8 5 6 7 8
VPP + 1 warmup
1 2 3 4 1 2 3 2 1 3 2 4 3 5 4 6 1 7 2 8 3 5 4 6 5 6 7 8 5 6 7 8
1 2 3 4 1 2 1 3 2 4 3 5 4 6 1 7 2 8 3 5 4 6 5 7 6 8 7 8 5 6 7 8
Forward pass Backward pass PP communication EP-D EP-C EP-D EP-C EP dispatch and combine
Figure7: Computation,communicationandoffloadingoverlappedindifferentPPphases.
PipelineParallelism(PP)withvirtualstages[28,53,38,57,47,21],16-wayExpertParallelism(EP)[39],andZeRO-1
DataParallelism[60].
Under this setting, storing the model parameters in BF16 and their gradient accumulation buffer in FP32 requires
approximately6TBofGPUmemory,distributedoveramodel-parallelgroupof256GPUs. Placementofoptimizer
statesdependsonthetrainingconfigurations. Whenthetotalnumberoftrainingnodesislarge,theoptimizerstatesare
distributed,reducingitsper-devicememoryfootprinttoanegligiblelevel. Whenthetotalnumberoftrainingnodesis
small(e.g.,32),wecanoffloadsomeoptimizerstatestoCPU.
Thisapproachallowsustoreuseanidenticalparallelismconfigurationforbothsmall-andlarge-scaleexperiments,
whilelettingeachGPUholdapproximately30GBofGPUmemoryforallstates. TherestoftheGPUmemoryareused
foractivations,asdescribedinSec.2.4.3. Suchaconsistentdesignisimportantforresearchefficiency,asitsimplifies
thesystemandsubstantiallyacceleratesexperimentaliteration.
EPcommunicationoverlapwithinterleaved1F1B Byincreasingthenumberofwarm-upmicro-batches,wecan
overlap EP all-to-all communication with computation under the standard interleaved 1F1B schedule [21, 53]. In
comparison,DualPipe[10]doublesthememoryrequiredforparametersandgradients,necessitatinganincreasein
parallelismtocompensate. IncreasingPPintroducesmorebubbles,whileincreasingEP,asdiscussedbelow,incurs
higheroverhead. Theadditionalcostsareprohibitivelyhighfortrainingalargemodelwithover1trillionparameters
andthusweoptednottouseDualPipe.
However,interleaved1F1Bsplitsthemodelintomorestages,introducingnon-trivialPPcommunicationoverhead. To
mitigatethiscost,wedecoupletheweight-gradientcomputationfromeachmicro-batch’sbackwardpassandexecute
it in parallel with the corresponding PP communication. Consequently, all PP communications can be effectively
overlappedexceptforthewarm-upphase.
SmallerEPsize Toensurefullcomputation-communicationoverlapduringthe1F1Bstage,thereducedattention
computationtimeinK2(whichhas64attentionheadscomparedto128headsinDeepSeek-V3)necessitatesminimizing
thetimeofEPoperations. ThisisachievedbyadoptingthesmallestfeasibleEPparallelizationstrategy,specifically
EP=16. UtilizingasmallerEPgroupalsorelaxesexpert-balanceconstraints,allowingfornear-optimalspeedtobe
achievedwithoutfurthertuning.
2.4.3 ActivationReduction
Afterreservingspaceforparameters,gradientbuffers,andoptimizerstates,theremainingGPUmemoryoneachdevice
isinsufficienttoholdthefullMoEactivations. Toensuretheactivationmemoryfitswithintheconstraints,especially
fortheinitialpipelinestagesthataccumulatethelargestactivationsduringthe1F1Bwarm-upphase,thefollowing
techniquesareemployed.
Selective recomputation Recomputation is applied to inexpensive, high-footprint stages, including LayerNorm,
SwiGLU,andMLAup-projections[10]. Additionally,MoEdown-projectionsarerecomputedduringtrainingtofurther
reduceactivationmemory. Whileoptional,thisrecomputationmaintainsadequateGPUmemory,preventingcrashes
causedbyexpertimbalanceinearlytrainingstages.
FP8storageforinsensitiveactivations InputsofMoEup-projectionsandSwiGLUarecompressedtoFP8-E4M3in
1 128tileswithFP32scales. Small-scaleexperimentsshownomeasurablelossincrease. Duetopotentialrisksof
≃
performancedegradationthatweobservedduringpreliminarystudy,wedonotapplyFP8incomputation.
8

KimiK2 TECHNICALREPORT
ActivationCPUoffload AllremainingactivationsareoffloadedtoCPURAM.Acopyengineisresponsiblefor
streamingtheoffloadandonload,overlappingwithbothcomputationandcommunicationkernels. Duringthe1F1B
phase,weoffloadtheforwardactivationsofthepreviousmicro-batchwhileprefetchingthebackwardactivationsofthe
next. Thewarm-upandcool-downphasesarehandledsimilarlyandtheoverallpatternisshowninFigure7. Although
offloadingmayslightlyaffectEPtrafficduetoPCIetrafficcongestion,ourtestsshowthatEPcommunicationremains
fullyoverlapped.
2.5 Trainingrecipe
Wepre-trainedthemodelwitha4,096-tokencontextwindowusingtheMuonClipoptimizer(Algorithm1)andthe
WSDlearningrateschedule[25],processingatotalof15.5Ttokens. Thefirst10Ttokensweretrainedwithaconstant
learningrateof2e-4aftera500-stepwarm-up,followedby5.5Ttokenswithacosinedecayfrom2e-4to2e-5. Weight
decaywassetto0.1throughout,andtheglobalbatchsizewasheldat67Mtokens. Theoveralltrainingcurveisshown
inFigure3.
Towardstheendofpre-training,weconductedanannealingphasefollowedbyalong-contextactivationstage. The
batchsizewaskeptconstantat67Mtokens,whilethelearningratewasdecayedfrom2e-5to7e-6. Inthisphase,the
modelwastrainedon400billiontokenswitha4ksequencelength,followedbyanadditional60billiontokenswitha
32ksequencelength. Toextendthecontextwindowto128k,weemployedtheYaRNmethod[55].
3 Post-Training
3.1 SupervisedFine-Tuning
WeemploytheMuonoptimizer[33]inourpost-trainingandrecommenditsuseforfine-tuningwithK2. Thisfollows
fromtheconclusionofourpreviouswork[46]thataMuon-pre-trainedcheckpointproducesthebestperformancewith
Muonfine-tuning.
Weconstructalarge-scaleinstruction-tuningdatasetspanningdiversedomains,guidedbytwocoreprinciples: max-
imizing prompt diversity and ensuring high response quality. To this end, we develop a suite of data generation
pipelinestailoredtodifferenttaskdomains,eachutilizingacombinationofhumanannotation,promptengineering,and
verificationprocesses. WeadoptK1.5[35]andotherin-housedomain-specializedexpertmodelstogeneratecandidate
responsesforvarioustasks,followedbyLLMsorhuman-basedjudgestoperformautomatedqualityevaluationand
filtering. Foragenticdata,wecreateadatasynthesispipelinetoteachmodelstool-usecapabilitiesthroughmulti-step,
interactivereasoning.
3.1.1 Large-ScaleAgenticDataSynthesisforToolUseLearning
AcriticalcapabilityofmodernLLMagentsistheirabilitytoautonomouslyuseunfamiliartools,interactwithexternal
environments,anditerativelyrefinetheiractionsthroughreasoning,execution,anderrorcorrection. Agentictooluse
capabilityisessentialforsolvingcomplex,multi-steptasksthatrequiredynamicinteractionwithreal-worldsystems.
RecentbenchmarkssuchasACEBench[6]andω-bench[85]havehighlightedtheimportanceofcomprehensivetool-use
evaluation, while frameworks like ToolLLM [58] and ACEBench [6] have demonstrated the potential of teaching
modelstousethousandsoftoolseffectively.
However,trainingsuchcapabilitiesatscalepresentsasignificantchallenge: whilereal-worldenvironmentsprovide
rich and authentic interaction signals, they are often difficult to construct at scale due to cost, complexity, privacy
and accessibility constraints. Recent work on synthetic data generation (AgentInstruct [51]; Self-Instruct [75];
StableToolBench[20];ZeroSearch[66])hasshownpromisingresultsincreatinglarge-scaledatawithoutrelyingon
real-worldinteractions. BuildingontheseadvancesandinspiredbyACEBench[6]’scomprehensivedatasynthesis
framework,wedevelopedapipelinethatsimulatesreal-worldtool-usescenariosatscale,enablingthegenerationof
tensofthousandsofdiverseandhigh-qualitytrainingexamples.
Therearethreestagesinourdatasynthesispipeline,depictedinFig.8.
• Tool spec generation: we first construct a large repository of tool specs from both real-world tools and LLM-
synthetictools;
• Agentandtaskgeneration: foreachtool-setsampledfromthetoolrepository,wegenerateanagenttousethe
toolsetandsomecorrespondingtasks;
• Trajectory generation: for each agent and task, we generate trajectories where the agent finishes the task by
invokingtools.
9

KimiK2 TECHNICALREPORT
Domains User Task
Agent
interaction
MCP tools Applications
Tasks Agent Rubrics
with rubrics
observation call
real-world synthesized
tool specs tool specs Tool Judge Filtered
Simulator trajectories Agent Data
Tool Repository Agents
(a)Synthesizingtoolspecs,agentsandtasks (b)Generatingagenttrajectories
Figure8: Datasynthesispipelinefortooluse. (a)Toolspecsarefrombothreal-worldtoolsandLLMs;agentsandtasks
arethegeneratedfromthetoolrepo. (b)Multi-agentpipelinetogenerateandfiltertrajectorieswithtoolcalling.
(a) t-SNE visualization of real MCP tools, colored by their (b)t-SNEvisualizationofsynthetictools,coloredbypre-defined
originalsourcecategories domaincategories
Figure9: t-SNEvisualizationsoftoolembeddings. (a)Real-worldMCPtoolsexhibitnaturalclusteringbasedontheir
originalsourcecategories. (b)Synthetictoolsareorganizedintopre-defineddomaincategories,providingsystematic
coverageofthetoolspace. Together,theyensurecomprehensiverepresentationacrossdifferenttoolfunctionalities.
DomainEvolutionandToolGeneration. Weconstructacomprehensivetoolrepositorythroughtwocomplementary
approaches. First, we directly fetch 3000+ real MCP (Model Context Protocol) tools from GitHub repositories,
leveragingexistinghigh-qualitytoolspecs. Second,wesystematicallyevolve[82]synthetictoolsthroughahierarchical
domaingenerationprocess: webeginwithkeycategories(e.g.,financialtrading,softwareapplications,robotcontrol),
thenevolvemultiplespecificapplicationdomainswithineachcategory. Specializedtoolsarethensynthesizedforeach
domain,withclearinterfaces,descriptions,andoperationalsemantics. Thisevolutionprocessproducesover20,000
synthetictools. Figure9visualizesthediversityofourtoolcollectionthrought-SNEembeddings,demonstratingthat
bothMCPandsynthetictoolscovercomplementaryregionsofthetoolspace.
Agent Diversification. We generate thousands of distinct agents by synthesizing various system prompts and
equippingthemwithdifferentcombinationsoftoolsfromourrepository. Thiscreatesadiversepopulationofagents
withvariedcapabilities,areasofexpertise,andbehavioralpatterns,ensuringabroadcoverageofpotentialusecases.
Rubric-BasedTaskGeneration. Foreachagentconfiguration,wegeneratetasksthatrangefromsimpletocomplex
operations. Eachtaskispairedwithanexplicitrubricthatspecifiessuccesscriteria,expectedtool-usepatterns,and
evaluationcheckpoints. Thisrubric-basedapproachensuresaconsistentandobjectiveevaluationofagentperformance.
Multi-turnTrajectoryGeneration. Wesimulaterealistictool-usescenariosthroughseveralcomponents:
• UserSimulation: LLM-generateduserpersonaswithdistinctcommunicationstylesandpreferencesengagein
multi-turndialogueswithagents,creatingnaturalisticinteractionpatterns.
10

KimiK2 TECHNICALREPORT
• ToolExecutionEnvironment: Asophisticatedtoolsimulator(functionallyequivalenttoaworldmodel)executes
toolcallsandprovidesrealisticfeedback. Thesimulatormaintainsandupdatesstateaftereachtoolexecution,
enablingcomplexmulti-stepinteractionswithpersistenteffects. Itintroducescontrolledstochasticitytoproduce
variedoutcomesincludingsuccesses,partialfailures,andedgecases.
QualityEvaluationandFiltering. AnLLM-basedjudgeevaluateseachtrajectoryagainstthetaskrubrics. Only
trajectoriesthatmeetthesuccesscriteriaareretainedfortraining,ensuringhigh-qualitydatawhileallowingnatural
variationintask-completionstrategies.
HybridApproachwithRealExecutionEnvironments. Whilesimulationprovidesscalability,weacknowledge
theinherentlimitationofsimulationfidelity. Toaddressthis,wecomplementoursimulatedenvironmentswithreal
executionsandboxesforscenarioswhereauthenticityiscrucial,particularlyincodingandsoftwareengineeringtasks.
Theserealsandboxesexecuteactualcode,interactwithgenuinedevelopmentenvironments,andprovideground-truth
feedbackthroughobjectivemetricssuchastestsuitepassrates. Thiscombinationensuresthatourmodelslearnfrom
boththediversityofsimulatedscenariosandtheauthenticityofrealexecutions,significantlystrengtheningpractical
agentcapabilities.
Byleveragingthishybridpipelinethatcombinesscalablesimulationwithtargetedreal-worldexecution,wegenerate
diverse,high-qualitytool-usedemonstrationsthatbalancecoverageandauthenticity. Thescaleandautomationofour
syntheticdatageneration,coupledwiththegroundingprovidedbyrealexecutionenvironments,effectivelyimplements
large-scalerejectionsampling[26,87]throughourqualityfilteringprocess. Thishigh-qualitysyntheticdata,when
usedforsupervisedfine-tuning,hasdemonstratedsignificantimprovementsinthemodel’stool-usecapabilitiesacrossa
widerangeofreal-worldapplications.
3.2 ReinforcementLearning
Reinforcementlearning(RL)isbelievedtohavebettertokenefficiencyandgeneralizationthanSFT.Basedonthework
ofK1.5[35],wecontinuetoscaleRLinbothtaskdiversityandtrainingFLOPsinK2. Tosupportthis,wedevelopa
Gym-likeextensibleframeworkthatfacilitatesRLacrossawiderangeofscenarios. Weextendtheframeworkwitha
largenumberoftaskswithverifiablerewards. Fortasksthatrelyonsubjectivepreferences,suchascreativewritingand
open-endedquestionanswering,weintroduceaself-criticrewardinwhichthemodelperformspairwisecomparisonsto
judgeitsownoutputs. ThisapproachallowstasksfromvariousdomainstoallbenefitfromtheRLparadigm.
3.2.1 VerifiableRewardsGym
Math,STEMandLogicalTasks Formath,stemandlogicalreasoningdomains,ourRLdatapreparationfollows
twokeyprinciples,diversecoverageandmoderatedifficulty.
DiverseCoverage. Formathandstemtasks,wecollecthigh-qualityQApairsusingacombinationofexpertannotations,
internalQAextractionpipelines, andopendatasets[41, 52]. Duringthecollectionprocess, weleverageatagging
systemtodeliberatelyincreasecoverageofunder-covereddomains. Forlogicaltasks,ourdatasetcomprisesavarietyof
formats,includingstructureddatatasks(e.g.,multi-hoptabularreasoning,cross-tableaggregation)andlogicpuzzles
(e.g.,the24-game,Sudoku,riddles,cryptarithms,andMorse-codedecoding).
ModerateDifficulty. TheRLprompt-setshouldbeneithertooeasynortoohard,bothofwhichmayproducelittlesignal
andreducelearningefficiency. WeassessthedifficultyofeachproblemusingtheSFTmodel’spass@kaccuracyand
selectonlyproblemswithmoderatedifficulty.
ComplexInstructionFollowing Effectiveinstructionfollowingrequiresnotonlyunderstandingexplicitconstraints
butalsonavigatingimplicitrequirements,handlingedgecases,andmaintainingconsistencyoverextendeddialogues.
We address these challenges through a hybrid verification framework that combines automated verification with
adversarialdetection,coupledwithascalablecurriculumgenerationpipeline. Ourapproachemploysadual-pathsystem
toensurebothprecisionandrobustness:
HybridRuleVerification. Weimplementtwoverificationmechanisms: (1)deterministicevaluationviacodeinterpreters
forinstructionswithverifiableoutputs(e.g.,length,styleconstraints),and(2)LLM-as-judgeevaluationforinstructions
requiringnuancedunderstandingofconstraints. Toaddresspotentialadversarialbehaviorswheremodelsmightclaim
instructionfulfillmentwithoutactualcompliance,weincorporateanadditionalhack-checklayerthatspecificallydetects
suchdeceptiveclaims.
Multi-SourceInstructionGeneration. Toconstructourtrainingdata,weemploythreedistinctgenerationstrategiesto
ensurecomprehensivecoverage: (1)expert-craftedcomplexconditionalpromptsandrubricsdevelopedbyourdata
11

KimiK2 TECHNICALREPORT
team(2)agenticinstructionaugmentationinspiredbyAutoIF[12],and(3)afine-tunedmodelspecializedforgenerating
additionalinstructionsthatprobespecificfailuremodesoredgecases. Thismultiprongedapproachensuresbothbreadth
anddepthininstructioncoverage.
Faithfulness Faithfulnessisessentialforanagenticmodeloperatinginscenariossuchasmulti-turntooluse,self-
generatedreasoningchains,andopen-environmentinteractions. InspiredbytheevaluationframeworkfromFACTS
Grounding[30],wetrainasentence-levelfaithfulnessjudgemodeltoperformautomatedverification. Thejudgeis
effectiveindetectingsentencesthatmakeafactualclaimwithoutsupportingevidenceincontext. Itservesasareward
modeltoenhanceoverallfaithfulnessperformance.
Coding&SoftwareEngineering Toenhanceourcapabilityintacklingcompetition-levelprogrammingproblems,
wegatherproblemsandtheirjudgesfrombothopen-sourcedatasets[27,83]andsyntheticsources. Toensurethe
diversityofthesyntheticdataandthecorrectnessofrewardsignals,weincorporatehigh-qualityhuman-writtenunit
testsretrievedfrompre-trainingdata.
Forsoftwareengineeringtasks,wecollectavastamountofpullrequestsandissuesfromGitHubtobuildsoftware
developmentenvironmentthatconsistsofuserprompts/issuesandexecutableunittests. Thisenvironmentwasbuilton
arobustsandboxinfrastructure,poweredbyKubernetesforscalabilityandsecurity. Itsupportsover10,000concurrent
sandboxinstanceswithstableperformance,makingitidealforbothcompetitivecodingandsoftwareengineeringtasks.
Safety Our work to enhance the safety begins with a human-curated set of seed prompts, manually crafted to
encompassprevalentriskcategoriessuchasviolence,fraud,anddiscrimination.
Tosimulatesophisticatedjailbreakattempts(e.g.,role-playing,literarynarratives,andacademicdiscourse),weemploy
anautomatedpromptevolutionpipelinewiththreekeycomponents:
• AttackModel: IterativelygeneratesadversarialpromptsdesignedtoelicitunsaferesponsesfromthetargetLLM.
• TargetModel: Producesresponsestotheseprompts,simulatingpotentialvulnerabilities.
• Judge Model: Evaluates the interaction to determine if the adversarial prompt successfully bypasses safety
mechanisms.
Eachinteractionisassessedusingatask-specificrubric,enablingthejudgemodeltoprovideabinarysuccess/failure
label.
3.2.2 BeyondVerification: Self-CritiqueRubricReward
Toextendmodelalignmentbeyondtaskswithverifiablereward,weintroduceaframeworkforgeneralreinforcement
learning from self-critic feedbacks. This approach is designed to align LLMs with nuanced human preferences,
includinghelpfulness,creativity,depthofreasoning,factuality,andsafety,byextendingthecapabilitieslearnedfrom
verifiablescenariostoabroaderrangeofsubjectivetasks. TheframeworkoperatesusingaSelf-CritiqueRubricReward
mechanism,wherethemodelevaluatesitsownoutputstogeneratepreferencesignals. TobootstrapK2asacompetent
judge,wecuratedamixtureofopen-sourceandin-housepreferencedatasetsandinitializeitscriticcapabilityinthe
SFTstage.
Self-CritiquedPolicyOptimization Inthefirstcoreprocessofthelearningloop,theK2actorgeneratesresponses
forgeneralpromptsthatcoverawiderangeofusecases. TheK2criticthenranksallresultsbyperformingpairwise
evaluationsagainstacombinationofrubrics,whichincorporatesbothcorerubrics(Appendix.F.1),whichrepresentthe
fundamentalvaluesofourAIassistantthatKimicherish,prescriptiverubrics(Appendix.F.2)thataimtoeliminate
rewardhacking,andhuman-annotatedrubricscraftedbyourdatateamforspecificinstructionalcontexts. Although
certainrubricscanbedesignatedasmandatory,K2retainstheflexibilitytoweighthemagainstitsinternalpriors. This
capacityenablesadynamicandcontinuousalignmentwithitsevolvingon-policybehavior,ensuringthatthemodel’s
responsesremaincoherentwithitscoreidentitywhileadaptingtospecificinstructions.
Closed-LoopCriticRefinementandAlignment DuringRLtraining,thecriticmodelisrefinedusingverifiable
signals.On-policyrolloutsgeneratedfromverifiable-rewardpromptsareusedtocontinuouslyupdatethecritic,acrucial
stepthatdistillsobjectiveperformancesignalsfromRLVRdirectlyintoitsevaluationmodel. Thistransferlearning
process grounds its more subjective judgments in verifiable data, allowing the performance gains from verifiable
taskstoenhancethecritic’sjudgmentoncomplextasksthatlackexplicitrewardsignals. Thisclosed-loopprocess
ensuresthatthecriticcontinuouslyrecalibratesitsevaluationstandardsinlockstepwiththepolicy’sevolution. By
12

KimiK2 TECHNICALREPORT
groundingsubjectiveevaluationinverifiabledata,theframeworkenablesrobustandscalablealignmentwithcomplex,
non-verifiablehumanobjectives.
Consequently,thisholisticalignmentyieldscomprehensiveperformanceimprovementsacrossawidespectrumofdo-
mains,includinguserintentunderstanding,creativewriting,complexreasoning,andnuancedlanguagecomprehension.
3.2.3 RLAlgorithm
WeadoptthepolicyoptimizationalgorithmintroducedinK1.5[35]asthefoundationforK2. Foreachproblemx,
wesampleK responses y ,...,y fromthepreviouspolicyφ ,andoptimizethemodelφ withrespecttothe
1 k old ε
{ }
followingobjective:
K 2
1 φ (y x)
ε i
L
RL
(↼)=Ex r(x,y
i
) r¯(x) ωlog | ,
↗D& K i=1 &! ↔ ↔ φ old (y i | x) " ((
’
wherer¯(x)= 1 k r(x,y )isthemeanrewardsofthesampledresponses,ω> 0isaregularizationparameterthat
k i=1 i
promotesstablelearning. AsinSFT,weemploytheMuonoptimizer[33]tominimizethisobjective. Aswescale
RLtrainingtoen)compassabroaderrangeoftasksinK2,aprimarychallengeisachievingconsistentperformance
improvementsacrossalldomains. Toaddressthis,weintroduceseveraladditionstotheRLalgorithm.
BudgetControl IthasbeenwidelyobservedthatRLoftenresultsinasubstantialincreaseinthelengthofmodel-
generatedresponses[35,19]. Whilelongerresponsescanenablethemodeltoutilizeadditionaltest-timecomputefor
improvedperformanceoncomplexreasoningtasks,thebenefitsoftendonotjustifyitsinferencecostinnon-reasoning
domains. Toencouragethemodeltoproperlydistributeinferencebudget,weenforceaper-samplemaximumtoken
budget throughout RL training, where the budget is determined based on the type of task. Responses that exceed
thistokenbudgetaretruncatedandassignedapenalty,whichincentivizesthemodeltogeneratesolutionswithinthe
specifiedlimit. Empirically,thisapproachsignificantlyenhancesthemodel’stokenefficiency,encouragingconciseyet
effectivesolutionsacrossalldomains.
PTXLoss Topreventthepotentialforgettingofvaluable,high-qualitydataduringjointRLtraining,wecuratea
datasetcomprisinghand-selected,high-qualitysamplesandintegrateitintotheRLobjectivethroughanauxiliaryPTX
loss[54]. Thisstrategynotonlyleveragestheadvantagesofhigh-qualitydata,butalsomitigatestheriskofoverfitting
tothelimitedsetoftasksexplicitlypresentinthetrainingregime. Thisaugmentationsubstantiallyimprovesthemodel’s
generalizationacrossabroaderrangeofdomains.
TemperatureDecay Fortaskssuchascreativewritingandcomplexreasoning,wefindthatpromotingexploration
viaahighsamplingtemperatureduringtheinitialstagesoftrainingiscrucial. Ahightemperatureallowthemodelto
generatediverseandinnovativeresponses,therebyfacilitatingthediscoveryofeffectivestrategiesandreducingtherisk
ofprematureconvergencetosuboptimalsolutions. However,retainingahightemperatureinthelaterstagesoftraining
orduringevaluationcanbedetrimental,asitintroducesexcessiverandomnessandcompromisesthereliabilityand
consistencyofthemodel’soutputs. Toaddressthis,weemployatemperaturedecayschedule,toshiftfromexploration
toexploitationthroughoutthetraining. Thisstrategyensuresthatthemodelleveragesexplorationwhenitismost
beneficial,whileultimatelyconvergeonstableandhigh-qualityoutputs.
3.3 RLInfrastructure
3.3.1 ColocatedArchitecture
SimilartoK1.5[35],weadoptahybridcolocatedarchitectureforoursynchronizedRLtraining,wherethetrainingand
inferenceenginesliveonthesameworkers. Whenoneengineisactivelyworking,theotherenginereleasesoroffloads
itsGPUresourcestoaccommodate. IneachiterationofRLtraining,acentralizedcontrollerfirstcallstheinference
enginetogeneratenewdatafortraining. Itthennotifiesthetrainingenginetotrainonthenewdata,andsendupdated
parameterstotheinferenceengineforthenextiteration.
Eachengineisheavilyoptimizedforthroughput. Inaddition,asthemodelscalestothesizeofK2,thelatencyofengine
switchingandfailurerecoverybecomessignificant. Wepresentoursystemdesignconsiderationsintheseaspects.
13

KimiK2 TECHNICALREPORT
pod
train engine checkpoint engine inference engine
train ckpt inference
train ckpt inference
broadcast
Figure10: Parameterupdateutilizingacheckpointengine
3.3.2 EfficientEngineSwitching
During rollout, the parameters of the training engine are offloaded to DRAM. Bringing up the training engine is
thereforeasimplestepofH2Dtransmission. However,bringinguptheinferenceengineisabiggerchallenge,asit
mustobtainupdatedparametersfromthetrainingenginewithadifferentshardingparadigm.
Given the scale of K2 and the vast number of devices involved, using a network file system for resharding and
broadcasting parameters is impractical. The aggregate bandwidth required to keep overhead low reaches several
petabytespersecond. Toaddressthischallenge,wedevelopedadistributedcheckpointengineco-locatedontraining
nodestomanageparameterstates. Toperformaparameterupdate,eachcheckpointengineworkerobtainsalocalcopy
ofparametersfromthetrainingengine,thenbroadcaststhefullparametersetacrossallcheckpointengineworkers.
Subsequently,theinferenceengineretrievesonlytheparametersharditrequiresfromthecheckpointengine. This
processisillustratedinFigure10. Toenablethisfora1Tmodel,updatesareperformedparameter-by-parameterina
pipelinedmanner,minimizingmemoryfootprint(seeAppendixG).
Weopttobroadcastthefullparametersetacrosstheentirecluster,regardlessofthespecificshardingschemesoneach
inferenceworker. Whilethistransfersseveraltimesmoredatathanatheoreticallyoptimalapproach,itoffersasimpler
systemdesignthatislessintrusivetothetrainingandinferenceengines. Wechosetotradeoffthisminoroverheadto
fullydecouplethetrainingengineandtheinferenceengine,significantlysimplifyingmaintenanceandtesting.
Notably,thisapproachoutperformsthetransfer-what-you-needmethodduetoreducedsynchronizationoverheadand
highernetworkbandwidthutilization. OursystemcancompleteafullparameterupdateforKimiK2withlessthan30
seconds,anegligibledurationforatypicalRLtrainingiteration.
3.3.3 EfficientSystemStartup
Aslarge-scaletrainingispronetosystemfailure,optimizingthestartuptimeiscrucialformodelsaslargeasKimiK2.
Tostartthetrainingengine,weleteachtrainingworkerselectivelyreadpartornoneoftheparametersfromdisk,and
broadcastnecessaryparameterstoitspeers. Thedesigngoalistoensureallworkerscollectivelyreadthecheckpoint
onlyonce,minimizingexpensivediskIO.
Astheinferenceenginesareindependentreplicas,wewouldliketoavoidintroducingextrasynchronizationbarriers
betweenthem. Therefore,weopttoreusecheckpointengineforstartup: weletcheckpointenginecollectivelyreadthe
checkpointfromdisk,similartohowthetrainingenginestarts. Thenitupdatesthestateoftheuninitializedinference
engine,usingtheapproachintroducedintheprevioussection. Byleveragingthededicatedcheckpointengine,the
systemalsobecomesrobusttosingle-pointfailures,becauseaninferencereplicacanrestartwithoutcommunicating
withotherreplicas.
3.3.4 AgenticRollout
OurRLinfrastructuresupportsthetrainingoflong-horizon,multi-turnagentictasks. Duringrollout,thesetaskspresent
distinctchallenges,suchascomplexenvironmentalinteractionsandprolongedrolloutdurations. Hereweintroducea
fewoptimizationstoalleviatetheseissues.
Duetothediversityofenvironments,certaininteractionsmaybeblockedonwaitingforenvironmentfeedback(e.g.,a
virtualmachineoracodeinterpreter),leavingtheGPUsidle. WeemploytwostrategiestomaximizeGPUutilization:
14

KimiK2 TECHNICALREPORT
(i)wedeployheavyenvironmentsasdedicatedservicesthatcanscaleupmoreeasily;(ii)weemployalargenumberof
concurrentrolloutstoamortizethelatencyinducedbycertainexpensiveinteractions.
Anotherchallengeinagenticrolloutisthatindividualrollouttrajectoriescanbeextremelylong. Topreventlong-tail
trajectoriesfromblockingtheentirerolloutprocess,weemploythepartialrollout[35]technique. Thisstrategyallows
long-tailunfinishedtaskstobepaused,andresumedinthenextRLiteration.
Toimproveresearchefficiency,wealsodesignaunifiedinterfaceinspiredbytheOpenAIGymframework[49]to
streamlinetheintegrationofnewenvironments. WehopetoscaleourRLinfrastructuretomorediverseinteractive
environmentsinthefuture.
4 Evaluations
Thissectionbeginswiththepost-trainingevaluationofKimi-K2-Instruct,followedbyabriefoverviewofthecapabilities
ofKimi-K2-Base. Weconcludewithacomprehensivesafetyevaluation.
4.1 Post-trainingEvaluations
4.1.1 EvaluationSettings
Benchmarks WeassessKimi-K2-Instructacrossdifferentareas. Forcoding,weadoptLiveCodeBenchv6[31](ques-
tionsfromAugust2024toMay2025),OJBench[77],MultiPL-E[5],SWE-benchVerified[32,84],TerminalBench[71],
Multi-SWE-bench[86],SWE-Lancer[50],PaperBench[65],andAider-Polyglot[16]. Fortoolusetasks,weevaluate
performanceonω2-Bench[3]andAceBench[6],whichemphasizemulti-turntool-callingcapabilities. Inreasoning,
weincludeawiderangeofmathematical,scienceandlogicaltasks: AIME2024/2025,MATH-500,HMMT2025,
CNMO2024,PolyMath-en,ZebraLogic[43],AutoLogi[91],GPQA-Diamond[61],SuperGPQA[13],andHumanity’s
LastExam(Text-Only)[56]. Webenchmarkthelong-contextcapabilitieson: MRCR4forlong-contextretrieval,and
DROP[14],FRAMES[37]andLongBenchv2[2]forlong-contextreasoning. Forfactuality, weevaluateFACTS
Grounding[30],theVectaraHallucinationLeaderboard[73],andFaithJudge[68]. Finally,generalcapabilitiesare
assessedusingMMLU[23],MMLU-Redux[17],MMLU-Pro[76],IFEval[90],Multi-Challenge[64],SimpleQA[78],
andLiveBench[80](asof2024-11-25).
Baselines We benchmark against both open-source and proprietary frontier models, ensuring every candidate is
evaluatedunderitsnon-thinkingconfigurationtoeliminateadditionalgainsfromtest-timecompute. Open-source
baselines: DeepSeek-V3-0324andQwen3-235B-A22B,withthelatterruninthevendor-recommendedno-thinking
regime. Proprietarybaselines: ClaudeSonnet4,ClaudeOpus4,GPT-4.1,andGemini2.5FlashPreview(2025-05-20).
Eachinvokedinitsrespectivenon-thinkingmodeviaofficialAPIsunderunifiedtemperatureandtop-psettings.
Evaluation Configurations All runs query models in their non-thinking mode. Output token length is capped at
8192tokenseverywhereexceptSWE-benchVerified(Agentless),whichisraisedto16384. Forbenchmarkswithhigh
per-questionvariance,weadoptrepeatedsamplingktimesandaveragetheresultstoobtainstablescores,denotedas
Avg@k. Forlong-contexttasks,wesetthecontextwindowsizeto128Ktokensduringevaluation,truncatinganyinput
thatexceedsthislimittofitwithinthewindow. SWE-benchVerifiedisevaluatedintwomodes: AgentlessCoding
viaSinglePatchwithoutTest(Acc)andAgenticCodingviabash/editortoolsunderbothSingleAttempt(Acc)and
MultipleAttempts(Acc)usingbest-of-Nselectionwithaninternalverifier;SWE-benchMultilingualistestedonlyin
thesingle-attemptagenticsetting. Somedatapointshavebeenomittedduetoprohibitivelyexpensiveevaluationcosts.
4.1.2 EvaluationResults
AcomprehensiveevaluationresultsofKimi-K2-InstructisshowninTable3,withdetailedexplanationprovidedinthe
AppendixC.Below,wehighlightkeyresultsacrossfourcoredomains:
Agentic and Competitive Coding Kimi-K2-Instruct demonstrates state-of-the-art open-source performance on
real-worldSWEtasks. ItoutperformsmostbaselinesonSWE-benchVerified(65.8%,71.6%withmultipleattemps),
SWE-benchMultilingual(47.3%),andSWE-lancer(39.1%),significantlyclosingthegapwithClaude4Opusand
Sonnet. Oncompetitivecodingbenchmarks(e.g.,LiveCodeBenchv653.7%,OJBench27.1%),italsoleadsamongall
models,highlightingitspracticalcodingproficiencyacrossdifficultylevels.
4https://huggingface.co/datasets/openai/mrcr
15

KimiK2 TECHNICALREPORT
Table3: PerformancecomparisonofKimi-K2-Instructagainstleadingopen-sourceandproprietarymodelsacross
diverse tasks. Bold denotes the global SOTA; underlinedbold indicates the best open-source result. Data points
markedwith*aretakendirectlyfromthemodel’stechnicalreportorblog.
OpenSource Proprietary
Benchmark Kimi-K2- DeepSeek- Qwen3- Claude Claude GPT-4.1 Gemini
Instruct V3-0324 235B- Sonnet4 Opus4 2.5Flash
A22B
CodingTasks
LiveCodeBenchv6(Pass@1) 53.7 46.9 37.0 48.5 47.4 44.7 44.7
OJBench(Pass@1) 27.1 24.0 11.3 15.3 19.6 19.5 19.5
MultiPL-E(Pass@1) 85.7 83.1 78.2 88.6 89.6 86.7 85.6
SWE-benchVerified
51.8 36.6 39.4 50.2 53.0 40.8 32.6
Agentless-Single-Patch(Pass@1)
SWE-benchVerified
65.8 38.8 34.4 72.7* 72.5* 54.6 —
Agentic-Single-Attempt(Pass@1)
SWE-benchVerified
71.6 — — 80.2* 79.4* — —
Agentic-Multi-Attempt(Pass@1)
SWE-benchMultilingual(Pass@1) 47.3 25.8 20.9 51.0 — 31.5 —
Multi-SWE-bench(Pass@1) 18.3 8.0 9.0 29.2 — 11.7 14.0
SWE-Lancer(Pass@1) 39.1 30.5 24.1 40.8 — 23.0 38.5
PaperBenchCode-Dev(Acc.) 27.8 12.2 13.2 43.3 — 29.9 5.7
TerminalBenchIn-House(Acc.) 30.0 — — 35.5 43.2 8.3 —
TerminalBenchTerminus(Acc.) 25.0 16.3 6.6 — — 30.3 16.8
Aider-Polyglot(Acc.) 60.0 55.1 61.8 56.4 70.7 52.4 44.0
ToolUseTasks
Tau2retail(Avg@4) 70.6 69.1 57.0 75.0 81.8 74.8 64.3
Tau2airline(Avg@4) 56.5 39.0 26.5 55.5 60.0 54.5 42.5
Tau2telecom(Avg@4) 65.8 32.5 22.1 45.2 57.0 38.6 16.9
AceBench(Acc.) 76.5 72.7 70.5 76.2 75.6 80.1 74.5
Math&STEMTasks
AIME2024(Avg@64) 69.6 59.4* 40.1* 43.4 48.2 46.5 61.3
AIME2025(Avg@64) 49.5 46.7 24.7* 33.1* 33.9* 37.0 46.6
MATH-500(Acc.) 97.4 94.0* 91.2* 94.0 94.4 92.4 95.4
HMMT2025(Avg@32) 38.8 27.5 11.9 15.9 15.9 19.4 34.7
CNMO2024(Avg@16) 74.3 74.7 48.6 60.4 57.6 56.6 75.0
PolyMath-en(Avg@4) 65.1 59.5 51.9 52.8 49.8 54.0 49.9
ZebraLogic(Acc.) 89.0 84.0 37.7* 79.7 59.3 58.5 57.9
AutoLogi(Acc.) 89.5 88.9 83.3* 89.8 86.1 88.2 84.1
GPQA-Diamond(Avg@8) 75.1 68.4* 62.9* 70.0* 74.9* 66.3 68.2
SuperGPQA(Acc.) 57.2 53.7 50.2 55.7 56.5 50.8 49.6
Humanity’sLastExam(Acc.) 4.7 5.2 5.7 5.8 7.1 3.7 5.6
GeneralTasks
MMLU(EM) 89.5 89.4 87.0 91.5 92.9 90.4 90.1
MMLU-Redux(EM) 92.7 90.5 89.2* 93.6 94.2 92.4 90.6
MMLU-Pro(EM) 81.1 81.2* 77.3 83.7 86.6 81.8 79.4
IFEval(PromptStrict) 89.8 81.1 83.2* 87.6 87.4 88.0 84.3
Multi-Challenge(Acc.) 54.1 31.4 34.0 46.8 49.0 36.4 39.5
SimpleQA(Correct) 31.0 27.7 13.2 15.9 22.8 42.3 23.3
Livebench(Pass@1) 76.4 72.4 67.6 74.8 74.6 69.8 67.8
ArenaHardv2.0
54.5 39.9 39.9 51.6 59.7 51.7 48.7
HardPrompt(Winrate)
ArenaHardv2.0
85.0 59.3 59.8 54.6 68.5 61.5 72.8
CreativeWriting(Winrate)
FACTSGrounding(Adjusted) 88.5 68.3 68.5 83.6 — 79.2 86.6
HHEMv2.1(1-Hallu.) 98.9 88.9 94.5 94.5 — 96.7 97.8
FaithJudge(1-Hallu.) 92.6 83.4 75.7 83.0 — 91.0 93.2
LongBenchv2(Acc.) 49.1 51.1 — 52.5 — 54.3 55.5
FRAMES(Acc.) 77.1 79.2 — 76.3 — 87.4 72.9
MRCR(Acc.) 55.0 50.8 — 74.4 — 66.9 81.7
DROP(Acc.) 93.5 91.2 84.3 92.0 — 79.1 81.7
16

KimiK2 TECHNICALREPORT
AgenticToolUse Onmulti-turntool-usebenchmarks,Kimi-K2-Instructsetsanewstandard. Itachieves66.1Pass@1
onω2-Benchand76.5onACEBench,substantiallyoutperformingallbaselines. Theseresultsaffirmitsstrengthin
grounded,controlled,andagent-driventoolorchestrationacrossdomains.
General Capabilities Kimi-K2-Instruct exhibits strong, balanced performance across general knowledge, math,
instructionfollowing,andlong-contexttasks. Itsurpassesopen-sourcepeersonSimpleQA(31.0%),MMLU(89.5%)
andMMLU-Redux(92.7%),andleadsallmodelsoninstructionbenchmarks(IFEval: 89.8%,Multi-Challenge: 54.1%).
InmathandSTEM,itachievestop-tierscores(AIME2024: 69.6%,GPQA-Diamond: 75.1%),andremainscompetitive
onlong-contextfactualityandretrieval(DROP:93.5%,MRCR:55.0%). TheseresultspositionKimi-K2-Instructasa
well-roundedandcapablegeneralistacrossbothshort-andlong-contextsettings.
Open-EndedEvaluation OntheLMSYSArenaleaderboard(July17,2025),Kimi-K2-Instructranksasthetop-1
open-sourcemodeland5thoverallbasedonover3,000uservotes. Thisreal-worldpreferencesignal—acrossdiverse,
blindprompts—underscoresKimi-K2’sstrengthsingeneratinghigh-qualityresponsesonopen-endedtasks.
4.2 Pre-trainingEvaluations
4.2.1 EvaluationSettings
Benchmarks We evaluate Kimi-K2-Base across diverse capability areas. For general capabilities, we assess on
MMLU[23],MMLU-Pro[76],MMLU-Redux[17],BBH[67],TriviaQA[34],SuperGPQA[13],SimpleQA[78],Hel-
laSwag[88],AGIEval[89],GPQA-Diamond[61],ARC-Challenge[8],andWinoGrande[62]. Forcodingcapabilities,
weemployEvalPlus[45](averagingHumanEval[7],MBPP[1],HumanEval+,andMBPP+),LiveCodeBenchv6[31],
andCRUXEval[18]. Formathematicalreasoning,weutilizeGSM8K[9],GSM8K-Platinum[74],MATH[24],and
CMATH[79]. ForChineselanguagecapabilities,weevaluateonC-Eval[29],CMMLU[40],andCSimpleQA[22].
Baselines Webenchmarkagainstleadingopen-sourcefoundationmodels: DeepSeek-V3-Base[10],Qwen2.5-72B-
Base[59](NotethatQwen3-235B-A22B-Baseisnotopen-sourced,andthelargestopen-sourcedbasemodelinthe
QwenseriesisQwen2.5-72B-Base),andLlama4-Maverick[70](Llama4-Behemothisalsonotopen-sourced). All
modelsareevaluatedunderidenticalconfigurationstoensurefaircomparison.
EvaluationConfigurations Weemployperplexity-basedevaluationforMMLU,MMLU-Redux,GPQA-Diamond,
HellaSwag,ARC-Challenge,C-Eval,andCMMLU.Generation-basedevaluationisusedforMMLU-Pro,SuperGPQA,
TriviaQA, BBH, CSimpleQA, MATH, CMATH, GSM8K, GSM8K-Platinum, CRUXEval, LiveCodeBench, and
EvalPlus. TomitigatethehighvarianceinherenttoGPQA-Diamond,wereportthemeanscoreacrosseightindependent
runs. AllevaluationsareconductedusingourinternalframeworkderivedfromLM-Harness-Evaluation[4],ensuring
consistentsettingsacrossallmodels.
4.2.2 EvaluationResults
Table4presentsacomprehensivecomparisonofKimi-K2-Baseagainstleadingopen-sourcefoundationmodelsacross
diverse evaluation benchmarks. The results demonstrate that Kimi-K2-Base achieves state-of-the-art performance
acrossthemajorityofevaluatedtasks,establishingitasaleadingfoundationmodelintheopen-sourcelandscape.
GeneralLanguageUnderstanding Kimi-K2-Baseachievesstate-of-the-artperformanceon10outof12English
languagebenchmarks. NotableresultsincludeMMLU(87.79%),MMLU-Pro(69.17%),MMLU-Redux(90.17%),
SuperGPQA(44.67%),andSimpleQA(35.25%),significantlyoutperformingallbaselines.
CodingCapabilities Oncodingbenchmarks,Kimi-K2-Basesetsnewstandardswithleadingperformanceacrossall
metrics. Itachieves74.00%onCRUXEval-I-cot,83.50%onCRUXEval-O-cot,26.29%onLiveCodeBenchv6,and
80.33%onEvalPlus,demonstratingsuperiorcodegenerationandcomprehensionabilities,particularlyinscenarios
requiringstep-by-stepreasoning.
MathematicalReasoning Kimi-K2-Baseexhibitsexceptionalmathematicalcapabilities,leadingonthreeoutof
fourbenchmarks: MATH(70.22%),GSM8K(92.12%),andGSM8K-Platinum(94.21%). Itmaintainscompetitive
performanceonCMATH(90.26%),narrowlybehindDeepSeek-V3-Base(90.53%). Theseresultshighlightthemodel’s
robustmathematicalproblem-solvingabilitiesacrossvaryingdifficultylevels.
17

KimiK2 TECHNICALREPORT
ChineseLanguageUnderstanding Themodeldemonstratessuperiormultilingualcapabilities,achievingstate-of-the-
artresultsacrossallChineselanguagebenchmarks: C-Eval(92.50%),CMMLU(90.90%),andCSimpleQA(77.57%).
TheseresultsestablishKimi-K2-BaseasaleadingmodelforChineselanguageunderstandingwhilemaintainingstrong
performanceacrossotherlanguages.
Table4: PerformancecomparisonofKimi-K2-Baseagainstleadingopen-sourcemodelsacrossdiversetasks.
Benchmark(Metric) #Shots Kimi-K2-Base DeepSeek-V3-Base Llama4-Maverick-Base Qwen2.5-72B-Base
Architecture - MoE MoE MoE Dense
#ActivatedParams - 32B 37B 17B 72B
#TotalParams - 1043B 671B 400B 72B
MMLU 5-shots 87.79 87.10 84.87 86.08
MMLU-pro 5-shots 69.17 60.59 63.47 62.80
MMLU-redux 5-shots 90.17 89.53 88.18 87.77
SuperGPQA 5-shots 44.67 39.20 38.84 34.23
GPQA-Diamond(avg@8) 5-shots 48.11 50.51 49.43 40.78
SimpleQA 5-shots 35.25 26.49 23.74 10.31
English TriviaQA 5-shots 85.09 84.11 79.25 76.03
BBH 3-shots 88.71 88.37 87.10 84.09
HellaSwag 5-shots 94.60 89.44 86.02 95.27
AGIEval - 84.23 81.57 67.55 76.87
ARC-Challenge 0-shot 95.73 93.77 94.03 95.56
WinoGrande 5-shots 85.32 84.21 77.58 84.14
CRUXEval-I-cot 0-shots 74.00 62.75 67.13 61.12
CRUXEval-O-cot 0-shots 83.50 75.25 75.88 66.13
Code
LiveCodeBench(v6) 1-shots 26.29 24.57 25.14 22.29
EvalPlus - 80.33 65.61 65.48 66.04
MATH 4-shots 70.22 61.70 63.02 62.68
GSM8k 8-shots 92.12 91.66 86.35 90.37
Math
GSM8k-platinum 8-shots 94.21 93.38 88.83 92.47
CMATH 6-shots 90.26 90.53 88.07 86.98
C-Eval 5-shots 92.50 90.04 80.91 90.86
Chinese CMMLU 5-shots 90.90 88.84 81.24 90.55
CSimpleQA 5-shots 77.57 72.13 53.47 50.53
4.3 SafetyEvaluation
4.3.1 ExperimentSettings
Weconductedred-teamingevaluationsonKimiK2comparewithotheropen-sourceLLMs. Theevaluationcovereda
rangeofattackscenarios—includingharmfulcontent,privacycontent,andsecuritycontent,aswellasdifferentattack
strategiessuchaspromptinjectionanditerativejailbreak.
WechoosePromptfoo5togenerateadversarialpromptsandanalyzetheresponses. Bythisway,wecanevaluatemodel
inascalableways.
ModelSelectionWecompareKimiK2withthreeotheropen-sourceLLMs: DeepSeek-V3,DeepSeek-R1,andQwen3.
PromptfooSettingsTable5listspluginsandstrategiesevaluated,witheachpluginpairedwithallstrategiestoassess
theirperformance.
TestCaseCountGiventheinherentnon-determinismoflargelanguagemodelinference,single-passoutputsmay
exhibitvariability. Toaccountforthis,wegenerated3attackpromptsperpluginforeachstrategy.
PromptLanguageSettingsWepre-testedthelanguagecompatibilityforeachplugin-strategycombination. Some
pluginssupportbothEnglishandChinese,whileothersonlysupportEnglish. Forcombinationsthatsupportboth,we
generated3promptsineachlanguage,resultingin6promptspercombination.
5https://github.com/promptfoo/promptfoo
18

KimiK2 TECHNICALREPORT
Table5: EnabledPluginsandStrategies
Harmful GraphicContent,HarassmentandBullying,HateSpeech,Insults,Profanity,Radicalization,Self
Harm,SexualContent,ToxicChat
Plugin Criminal Chemical&BiologicalWeapons,ChildExploitation,CopyrightViolations,Cybercrime,Illegal
Activities,IllegalDrugs,IndiscriminateWeapons,IntellectualPropertyViolation,Non-Violent
Crime,ViolentCrime,SexCrimes
Misinformation CompetitorEndorsement,UnsupervisedContracts,ExcessiveAgency,Hallucination,Misin-
formationandDisinformation,SpecializedAdvice,UnsafePractices,Imitation,Overreliance,
PoliticalOpinions,ReligiousSensitivity
Privacy PrivacyViolation,PIIinAPI/Database,DirectPIIExposure,PIIinSessionData,PIIviaSocial
Engineering
Security ASCIISmuggling,CyberSecEval,Harmbench,DebugAccess,DivergentRepetition,DoNotAn-
swer,MaliciousCode,Pliny,PromptExtraction,ReasoningDoS,ToolDiscovery
Strategy Basic,PromptInjection,IterativeJailbreak,Crescendo
ManualReviewWeincorporatedhumanreviewintotheevaluationprocess. Tominimizesubjectivityproblem,we
conductedmultipleroundsofreviewandassignedthesamereviewertoevaluateallcaseswithinagiventestsetto
ensureconsistencyandreducevariabilityinjudgment.
4.3.2 SafetyEvaluationResults
Table6presentsthepassingratesofdifferentmodelsundervariousplugin–strategycombinations.
Table6: SafetyEvaluationResults
Plugin Strategy Kimi-K2-Instruct DeepSeek-V3-0324 DeepSeek-R1 Qwen3-235B-A22B
Basic 98.04 90.45 99.02 98.53
Base64 100 90.20 100 100
Harmful
PromptInjection 93.14 100 95.10 99.02
IterativeJailbreak 92.16 66.67 72.55 74.51
Crescendo 64.71 64.71 80.39 86.27
Basic 100 99.62 95.45 99.24
Base64 96.97 89.39 84.85 98.48
Criminal
PromptInjection 75.76 91.67 69.70 98.47
IterativeJailbreak 57.57 21.21 25.76 53.03
Crescendo 56.06 31.81 42.42 59.09
Basic 97.28 92.57 92.46 94.84
Base64 98.48 90.48 96.83 93.65
Misinformation
PromptInjection 98.39 86.51 93.65 93.65
IterativeJailbreak 63.97 53.97 84.13 69.84
Crescendo 85.71 55.56 88.89 84.13
Basic 100 100 100 100
Base64 100 100 100 100
Privacy
PromptInjection 88.33 98.33 100 91.67
IterativeJailbreak 76.67 100 93.33 96.67
Crescendo 96.67 100 96.67 100
Basic 77.84 75.57 70.46 90.09
Base64 82.93 82.93 63.41 95.12
Security
PromptInjection 87.80 97.56 65.85 84.13
IterativeJailbreak 43.90 60.97 43.90 78.04
Crescendo 68.29 87.80 68.29 87.80
Withouttargetedoptimizationforspecificevaluationscenarios,thepassingrateofsomecomplexcases(e.g.,Harm-
ful–IterativeJailbreak)wasrelativelyhighercomparedtoothermodels.
Across different attack strategies, the models exhibited varying trends. Under the Base64 strategy, passing rates
generallyapproachedorreached100%,suggestingthatencodingtransformationshadminimalimpactonthemodels’
19

KimiK2 TECHNICALREPORT
basicrobustness.Incontrast,theCrescendostrategyledtoageneraldropinpassingrates,indicatingstrongeradversarial
effectiveness.
Inaddition,complexattackstrategiesdonotalwaysoutperformbasicprompts. Someoriginallyadversarialprompts
maylosetheirintendedmeaningaftermultipleroundsoftransformation,renderingtheresultingmodeloutputsless
meaningful.
Automated Red-teaming Limitations Due to the involvement of human review, the evaluation results inevitably
containadegreeofsubjectivity. Additionally,certainplugintypesinvolveAPImisuseorexternaltoolinvocation,which
aremoresuitableforevaluatingagentmodelswithtool-callingcapabilities. InthecontextofbaseLLMs,suchtests
mayhavelimitedrelevance.
5 Limitations
Inourinternaltests,wehaveidentifiedsomelimitationsincurrentKimiK2models. Whendealingwithhardreasoning
tasksoruncleartooldefinition,themodelmaygenerateexcessivetokens,sometimesleadingtotruncatedoutputsor
incompletetoolcalls. Additionally,performancemaydeclineoncertaintasksiftooluseisunnecessarilyenabled. When
buildingcompletesoftwareprojects,thesuccessrateofone-shotpromptingisnotasgoodasusingK2underanagentic
codingframework. Weareworkingtoaddresstheseissuesinfuturereleasesandlookingforwardtomorefeedbacks.
6 Conclusions
WeintroducedKimiK2,a1T-parameteropen-weightMoEmodelbuiltforagenticintelligence. Leveragingthetoken-
efficientMuonClipoptimizeranda15.5T-tokenhigh-qualitydataset,KimiK2achievesstable,scalablepre-training.
Post-trainingcombineslarge-scalesynthetictool-usedatawithaunifiedRLframeworkusingbothverifiablerewards
andself-criticfeedbacks. KimiK2setsnewstate-of-the-artonagenticandreasoningbenchmarks,establishingitselfas
themostcapableopen-weightLLMtodate.
7 Acknowledgments
We would like to acknowledge the valuable support provided by the OpenHands and Multi-SWE-bench teams in
evaluatingtheSWE-benchVerifiedandMulti-SWE-benchexperimentalresults.
20

KimiK2 TECHNICALREPORT
References
[1] JacobAustinetal.ProgramSynthesiswithLargeLanguageModels.2021.arXiv:2108.07732[cs.PL].URL:
https://arxiv.org/abs/2108.07732.
[2] Yushi Bai et al. LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context
Multitasks.2025.arXiv:2412.15204[cs.CL].URL:https://arxiv.org/abs/2412.15204.
[3] VictorBarresetal.ω2-Bench:EvaluatingConversationalAgentsinaDual-ControlEnvironment.2025.arXiv:
2506.07982[cs.AI].URL:https://arxiv.org/abs/2506.07982.
[4] StellaBidermanetal.“Lessonsfromthetrenchesonreproducibleevaluationoflanguagemodels”.In:arXiv
preprintarXiv:2405.14782(2024).
[5] FedericoCassanoetal.“MultiPL-E:AScalableandPolyglotApproachtoBenchmarkingNeuralCodeGenera-
tion”.In:IEEETransactionsonSoftwareEngineering49.7(2023),pp.3675–3691.DOI:10.1109/TSE.2023.
3267446.
[6] ChenChenetal.“ACEBench:WhoWinstheMatchPointinToolLearning?”In:arXive-prints(2025),arXiv–
2501.
[7] Mark Chen et al. “Evaluating Large Language Models Trained on Code”. In: (2021). arXiv: 2107.03374
[cs.LG].
[8] PeterClarketal.“Thinkyouhavesolvedquestionanswering?tryarc,theai2reasoningchallenge”.In:arXiv
preprintarXiv:1803.05457(2018).
[9] KarlCobbeetal.TrainingVerifierstoSolveMathWordProblems.2021.arXiv:2110.14168[cs.LG].URL:
https://arxiv.org/abs/2110.14168.
[10] DeepSeek-AI.DeepSeek-V3TechnicalReport.2024.arXiv:2412.19437[cs.CL]. URL:https://arxiv.
org/abs/2412.19437.
[11] MostafaDehghanietal.“Scalingvisiontransformersto22billionparameters”.In:Internationalconferenceon
machinelearning.PMLR.2023,pp.7480–7512.
[12] GuantingDongetal.Self-playwithExecutionFeedback:ImprovingInstruction-followingCapabilitiesofLarge
LanguageModels.2024.arXiv:2406.13542[cs.CL].URL:https://arxiv.org/abs/2406.13542.
[13] Xinrun Du et al. “Supergpqa: Scaling llm evaluation across 285 graduate disciplines”. In: arXiv preprint
arXiv:2502.14739(2025).
[14] DheeruDuaetal.“DROP:AReadingComprehensionBenchmarkRequiringDiscreteReasoningOverPara-
graphs”.In:CoRRabs/1903.00161(2019).arXiv:1903.00161.URL:http://arxiv.org/abs/1903.00161.
[15] Kazuki Fujii et al. Rewriting Pre-Training Data Boosts LLM Performance in Math and Code. 2025. arXiv:
2505.02881[cs.LG].URL:https://arxiv.org/abs/2505.02881.
[16] PaulGauthier.AiderLLMLeaderboards.https://aider.chat/docs/leaderboards/.2025.
[17] AryoPradiptaGemaetal.“Arewedonewithmmlu?”In:arXivpreprintarXiv:2406.04127(2024).
[18] AlexGuetal.“Cruxeval:Abenchmarkforcodereasoning,understandingandexecution”.In:arXivpreprint
arXiv:2401.03065(2024).
[19] DayaGuoetal.“Deepseek-r1:Incentivizingreasoningcapabilityinllmsviareinforcementlearning”.In:arXiv
preprintarXiv:2501.12948(2025).
[20] ZhichengGuoetal.“StableToolBench:TowardsStableLarge-ScaleBenchmarkingonToolLearningofLarge
LanguageModels”.In:arXivpreprintarXiv:2403.07714(2025).
[21] Aaron Harlap et al. “Pipedream: Fast and efficient pipeline parallel dnn training”. In: arXiv preprint
arXiv:1806.03377(2018).
[22] YHeetal.“Chinesesimpleqa:Achinesefactualityevaluationforlargelanguagemodels,2024a”.In:URL
https://arxiv.org/abs/2411.07140().
[23] Dan Hendrycks et al. “Measuring massive multitask language understanding”. In: arXiv preprint
arXiv:2009.03300(2020).
[24] DanHendrycksetal.MeasuringMathematicalProblemSolvingWiththeMATHDataset.2021.arXiv:2103.
03874[cs.LG].URL:https://arxiv.org/abs/2103.03874.
[25] ShengdingHuetal.“Minicpm:Unveilingthepotentialofsmalllanguagemodelswithscalabletrainingstrategies”.
In:arXivpreprintarXiv:2404.06395(2024).
[26] JiaxinHuangetal.“Largelanguagemodelscanself-improve”.In:arXivpreprintarXiv:2210.11610(2022).
[27] SimingHuangetal.OpenCoder:TheOpenCookbookforTop-TierCodeLargeLanguageModels.2025.arXiv:
2411.04905[cs.CL].URL:https://arxiv.org/abs/2411.04905.
21

KimiK2 TECHNICALREPORT
[28] YanpingHuangetal.“Gpipe:Efficienttrainingofgiantneuralnetworksusingpipelineparallelism”.In:Advances
inneuralinformationprocessingsystems32(2019).
[29] YuzhenHuangetal.C-Eval:AMulti-LevelMulti-DisciplineChineseEvaluationSuiteforFoundationModels.
2023.arXiv:2305.08322[cs.CL].URL:https://arxiv.org/abs/2305.08322.
[30] AlonJacovietal.TheFACTSGroundingLeaderboard:BenchmarkingLLMs’AbilitytoGroundResponsesto
Long-FormInput.2025.arXiv:2501.03200[cs.CL].URL:https://arxiv.org/abs/2501.03200.
[31] NamanJainetal.“Livecodebench:Holisticandcontaminationfreeevaluationoflargelanguagemodelsfor
code”.In:arXivpreprintarXiv:2403.07974(2024).
[32] CarlosEJimenezetal.“SWE-bench:CanLanguageModelsResolveReal-worldGithubIssues?”In:TheTwelfth
InternationalConferenceonLearningRepresentations.2024.URL:https://openreview.net/forum?id=
VTF8yNQM66.
[33] Keller Jordan et al. Muon: An optimizer for hidden layers in neural networks. 2024. URL: https://
kellerjordan.github.io/posts/muon/.
[34] MandarJoshietal.TriviaQA:ALargeScaleDistantlySupervisedChallengeDatasetforReadingComprehension.
2017.arXiv:1705.03551[cs.CL].URL:https://arxiv.org/abs/1705.03551.
[35] KimiTeam.“Kimik1.5:Scalingreinforcementlearningwithllms”.In:arXivpreprintarXiv:2501.12599(2025).
[36] Diederik P. Kingma and Jimmy Ba. “Adam: A Method for Stochastic Optimization”. In: 3rd International
ConferenceonLearningRepresentations,ICLR2015,SanDiego,CA,USA,May7-9,2015,ConferenceTrack
Proceedings.Ed.byYoshuaBengioandYannLeCun.2015.URL:http://arxiv.org/abs/1412.6980.
[37] SatyapriyaKrishnaetal.Fact,Fetch,andReason:AUnifiedEvaluationofRetrieval-AugmentedGeneration.
2025.arXiv:2409.12941[cs.CL].URL:https://arxiv.org/abs/2409.12941.
[38] JoelLamy-Poirier.“Breadth-firstpipelineparallelism”.In:ProceedingsofMachineLearningandSystems5
(2023),pp.48–67.
[39] DmitryLepikhinetal.“Gshard:Scalinggiantmodelswithconditionalcomputationandautomaticsharding”.In:
arXivpreprintarXiv:2006.16668(2020).
[40] Haonan Li et al. CMMLU: Measuring massive multitask language understanding in Chinese. 2024. arXiv:
2306.09212[cs.CL].URL:https://arxiv.org/abs/2306.09212.
[41] JiaLietal.“Numinamath:Thelargestpublicdatasetinai4mathswith860kpairsofcompetitionmathproblems
andsolutions”.In:HuggingFacerepository13.9(2024),p.9.
[42] TianleLietal.“FromCrowdsourcedDatatoHigh-QualityBenchmarks:Arena-HardandBenchBuilderPipeline”.
In:arXivpreprintarXiv:2406.11939(2024).
[43] BillYuchenLinetal.ZebraLogic:OntheScalingLimitsofLLMsforLogicalReasoning.2025.arXiv:2502.
01100[cs.AI].URL:https://arxiv.org/abs/2502.01100.
[44] Aixin Liu et al. “Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model”. In:
arXivpreprintarXiv:2405.04434(2024).
[45] JiaweiLiuetal.“Isyourcodegeneratedbychatgptreallycorrect?rigorousevaluationoflargelanguagemodels
forcodegeneration”.In:AdvancesinNeuralInformationProcessingSystems36(2023),pp.21558–21572.
[46] JingyuanLiuetal.“MuonisscalableforLLMtraining”.In:arXivpreprintarXiv:2502.16982(2025).
[47] ZimingLiuetal.“Hanayo:HarnessingWave-likePipelineParallelismforEnhancedLargeModelTraining
Efficiency”.In:ProceedingsoftheInternationalConferenceforHighPerformanceComputing,Networking,
StorageandAnalysis.SC’23.ACM,Nov.2023,pp.1–13. DOI:10.1145/3581784.3607073. URL:http:
//dx.doi.org/10.1145/3581784.3607073.
[48] IlyaLoshchilovandFrankHutter.“DecoupledWeightDecayRegularization”.In:InternationalConferenceon
LearningRepresentations.2019.URL:https://openreview.net/forum?id=Bkg6RiCqY7.
[49] JanLudziejewskietal.OpenAIGym.2025.arXiv:2502.05172[cs.LG].URL:https://arxiv.org/abs/
2502.05172.
[50] Samuel Miserendino et al. “SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance
SoftwareEngineering?”In:arXivpreprintarXiv:2502.12115(2025).
[51] Arindam Mitra et al. “Agentinstruct: Toward generative teaching with agentic flows”. In: arXiv preprint
arXiv:2407.03502(2024).
[52] IvanMoshkovetal.“Aimo-2winningsolution:Buildingstate-of-the-artmathematicalreasoningmodelswith
openmathreasoningdataset”.In:arXivpreprintarXiv:2504.16891(2025).
[53] DeepakNarayananetal.“Efficientlarge-scalelanguagemodeltrainingongpuclustersusingmegatron-lm”.In:
Proceedingsoftheinternationalconferenceforhighperformancecomputing,networking,storageandanalysis.
2021,pp.1–15.
22

KimiK2 TECHNICALREPORT
[54] LongOuyangetal.“Traininglanguagemodelstofollowinstructionswithhumanfeedback”.In:Advancesin
neuralinformationprocessingsystems35(2022),pp.27730–27744.
[55] BowenPengetal.“Yarn:Efficientcontextwindowextensionoflargelanguagemodels”.In:arXivpreprint
arXiv:2309.00071(2023).
[56] LongPhanetal.Humanity’sLastExam.2025.arXiv:2501.14249[cs.LG]. URL:https://arxiv.org/
abs/2501.14249.
[57] PenghuiQietal.“Zerobubblepipelineparallelism”.In:arXivpreprintarXiv:2401.10241(2023).
[58] Yujia Qin et al. “Toolllm: Facilitating large language models to master 16000+ real-world apis”. In: arXiv
preprintarXiv:2307.16789(2023).
[59] Qwenetal.Qwen2.5TechnicalReport.2025.arXiv:2412.15115[cs.CL].URL:https://arxiv.org/abs/
2412.15115.
[60] SamyamRajbhandarietal.“Zero:Memoryoptimizationstowardtrainingtrillionparametermodels”.In:SC20:
InternationalConferenceforHighPerformanceComputing,Networking,StorageandAnalysis.IEEE.2020,
pp.1–16.
[61] DavidReinetal.“Gpqa:Agraduate-levelgoogle-proofq&abenchmark”.In:FirstConferenceonLanguage
Modeling.2024.
[62] KeisukeSakaguchietal.“Winogrande:Anadversarialwinogradschemachallengeatscale”.In:Communications
oftheACM64.9(2021),pp.99–106.
[63] DavidSilverandRichardSSutton.“Welcometotheeraofexperience”.In:GoogleAI1(2025).
[64] VedSirdeshmukhetal.MultiChallenge:ARealisticMulti-TurnConversationEvaluationBenchmarkChallenging
toFrontierLLMs.2025.arXiv:2501.17399[cs.CL].URL:https://arxiv.org/abs/2501.17399.
[65] Giulio Starace et al. “PaperBench: Evaluating AI’s Ability to Replicate AI Research”. In: arXiv preprint
arXiv:2504.01848(2025).
[66] HaoSunetal.ZeroSearch:IncentivizetheSearchCapabilityofLLMswithoutSearching.2025.arXiv:2505.
04588[cs.CL].URL:https://arxiv.org/abs/2505.04588.
[67] MiracSuzgunetal.ChallengingBIG-BenchTasksandWhetherChain-of-ThoughtCanSolveThem.2022.arXiv:
2210.09261[cs.CL].URL:https://arxiv.org/abs/2210.09261.
[68] ManveerSinghTamberetal.“BenchmarkingLLMFaithfulnessinRAGwithEvolvingLeaderboards”.In:arXiv
preprintarXiv:2505.04847(2025).
[69] Gemma Team et al. “Gemma 2: Improving open language models at a practical size”. In: arXiv preprint
arXiv:2408.00118(2024).
[70] LlaMATeam.TheLlama4herd:ThebeginningofaneweraofnativelymultimodalAIinnovation—ai.meta.com.
https://ai.meta.com/blog/llama-4-multimodal-intelligence/.[Accessed15-07-2025].
[71] TheTerminal-BenchTeam.Terminal-Bench:ABenchmarkforAIAgentsinTerminalEnvironments.Apr.2025.
URL:https://github.com/laude-institute/terminal-bench.
[72] AshishVaswanietal.“AttentionisAllyouNeed”.In:AdvancesinNeuralInformationProcessingSystems.
Ed.byI.Guyonetal.Vol.30.CurranAssociates,Inc.,2017. URL:https://proceedings.neurips.cc/
paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.
[73] Vectara. Hallucination Evaluation Model (Revision 7437011). 2024. URL: https://huggingface.co/
vectara/hallucination_evaluation_model.
[74] Joshua Vendrow et al. “Do large language model benchmarks test reliability?” In: arXiv preprint
arXiv:2502.03461(2025).
[75] Yizhong Wang et al. “Self-instruct: Aligning language models with self-generated instructions”. In: arXiv
preprintarXiv:2212.10560(2022).
[76] YuboWangetal.MMLU-Pro:AMoreRobustandChallengingMulti-TaskLanguageUnderstandingBenchmark.
2024.arXiv:2406.01574[cs.CL].URL:https://arxiv.org/abs/2406.01574.
[77] ZhexuWangetal.OJBench:ACompetitionLevelCodeBenchmarkForLargeLanguageModels.2025.arXiv:
2506.16395[cs.CL].URL:https://arxiv.org/abs/2506.16395.
[78] JasonWeietal.“Measuringshort-formfactualityinlargelanguagemodels”.In:arXivpreprintarXiv:2411.04368
(2024).
[79] TianwenWeietal.CMATH:CanYourLanguageModelPassChineseElementarySchoolMathTest?2023.
arXiv:2306.16636[cs.CL].URL:https://arxiv.org/abs/2306.16636.
[80] Colin White et al. “LiveBench: A Challenging, Contamination-Free LLM Benchmark”. In: The Thirteenth
InternationalConferenceonLearningRepresentations.2025.
23

KimiK2 TECHNICALREPORT
[81] MitchellWortsmanetal.“Small-scaleproxiesforlarge-scaletransformertraininginstabilities,2023”.In:URL
https://arxiv.org/abs/2309.14322().
[82] CanXuetal.WizardLM:Empoweringlargepre-trainedlanguagemodelstofollowcomplexinstructions.2025.
arXiv:2304.12244[cs.CL].URL:https://arxiv.org/abs/2304.12244.
[83] ZhangchenXuetal.KodCode:ADiverse,Challenging,andVerifiableSyntheticDatasetforCoding.2025.arXiv:
2503.02951[cs.LG].URL:https://arxiv.org/abs/2503.02951.
[84] JohnYangetal.SWE-smith:ScalingDataforSoftwareEngineeringAgents.2025.arXiv:2504.21798[cs.SE].
URL:https://arxiv.org/abs/2504.21798.
[85] ShunyuYaoetal.“tau-bench:ABenchmarkforTool-Agent-UserInteractioninReal-WorldDomains”.In:arXiv
preprintarXiv:2406.12045(2024).
[86] Daoguang Zan et al. “Multi-swe-bench: A multilingual benchmark for issue resolving”. In: arXiv preprint
arXiv:2504.02605(2025).
[87] Eric Zelikman et al. “Star: Bootstrapping reasoning with reasoning”. In: Advances in Neural Information
ProcessingSystems35(2022),pp.15476–15488.
[88] RowanZellersetal.“Hellaswag:Canamachinereallyfinishyoursentence?”In:arXivpreprintarXiv:1905.07830
(2019).
[89] WanjunZhongetal.“Agieval:Ahuman-centricbenchmarkforevaluatingfoundationmodels”.In:arXivpreprint
arXiv:2304.06364(2023).
[90] JeffreyZhouetal.“Instruction-FollowingEvaluationforLargeLanguageModels”.In:ArXivabs/2311.07911
(2023).URL:https://arxiv.org/abs/2311.07911.
[91] QinZhuetal.AutoLogi:AutomatedGenerationofLogicPuzzlesforEvaluatingReasoningAbilitiesofLarge
LanguageModels.2025.arXiv:2502.16906[cs.CL].URL:https://arxiv.org/abs/2502.16906.
24

KimiK2 TECHNICALREPORT
Appendix
A Contributions
Thelistingofauthorsisinalphabeticalorderbasedontheirlastnames. Namesmarkedwithanasterisk(*)indicate
peoplewhoarenolongerpartofourteam.
YifanBai GuokunLai ShengyuanShi ZiyaoXu
YipingBao ChengLi FeifanSong JunjieYan
GuanduoChen FangLi JianlinSu YuziYan
JiahaoChen HaoyangLi ZhengyuanSu XiaofeiYang
NingxinChen MingLi XinjieSun* YingYang
RuijueChen WentaoLi FloodSung ZhenYang
YanruChen YanhaoLi HeyiTang ZhilinYang
YuankunChen YiweiLi JiawenTao ZonghanYang
YutianChen ZhaoweiLi QifengTeng HaotianYao
ZhuofuChen* ZhemingLi ChensiWang XingchengYao
JialeiCui HongzhanLin* DingluWang WenjieYe
HaoDing XiaohanLin FengWang ZhuoruiYe
MengnanDong ZongyuLin HaimingWang BohongYin
Ang’angDu ChengyinLiu JianzhouWang* LonghuiYu
ChenzhuangDu ChenyuLiu JiaxingWang EnmingYuan
DikangDu HongzhangLiu JinhongWang HongbangYuan*
YulunDu JingyuanLiu* ShengjieWang MengjieYuan
YuFan JunqiLiu ShuyiWang HaobingZhan
YichenFeng LiangLiu YaoWang DehaoZhang
KelinFu ShaoweiLiu YejieWang HaoZhang
BofeiGao T.Y.Liu YiqinWang WanluZhang
HongchengGao TianweiLiu YuxinWang XiaobinZhang
PeizhongGao WeizhouLiu YuzhiWang YangkunZhang
TongGao YangyangLiu ZhaojiWang YizhiZhang
XinranGu YiboLiu ZhengtaoWang YongtingZhang
LongyuGuan YipingLiu ZhexuWang YuZhang
HaiqingGuo* YueLiu ChuWei YutaoZhang
JianhangGuo ZhengyingLiu QianqianWei YutongZhang
HaoHu EnzheLu WenhaoWu ZhengZhang
XiaoruHao LijunLu XingzheWu HaotianZhao
TianhongHe ShenglingMa YuxinWu YikaiZhao
WeiranHe XinyuMa ChenjunXiao HuabinZheng
WenyangHe YingweiMa XiaotongXie ShaojieZheng
ChaoHong ShaoguangMao WeiminXiong* JianrenZhou
YangyangHu JieMei BoyuXu XinyuZhou
ZhenxingHu XinMen JingXu* ZaidaZhou
WeixiaoHuang YiboMiao JinjingXu ZhenZhu
ZhiqiHuang SiyuanPan L.H.Xu WeiyuZhuang
ZihaoHuang YeboPeng LinXu XinxingZu
TaoJiang RuoyuQin SutingXu KimiK2
ZhejunJiang BowenQu WeixinXu
XinyiJin ZeyuShang XinranXu
YongshengKang* LidongShi YangchuanXu
25

KimiK2 TECHNICALREPORT
B TokenTemplateofToolCalling
Therearethreecomponentsinthetokenstructurefortool-calling:
• Tooldeclarationmessage: definesthelistofavailabletoolsandtheschemaofthearguments;
• Toolinvokingsectioninassistantmessage: encodesthemodel’srequesttoinvoketools;
• Toolresultmessage: encapsulatestheinvokedtool’sexecutionresult.
Therawtokensofthetooldeclarationmessageareformattedasfollows:
<|im_begin|>
tool_declare
<|im_middle|>
# Tools
{{ tool declaration content }}
<|im_end|>
Thebluehighlightedmarksrepresentspecialtokens,andthegreenpart,quotedbybrackets,isthetooldeclaration
content. We use TypeScript to express the tool declaration content, since TypeScript is a concise language with a
comprehensivetypesystem,abletoexpressthetypesandconstraintsoftoolparameterswithbrieftext. Thecode1
showsanexamplefortwosimpletoolsinJSONformatcompatiblewithOpenAI’schatcompletionAPI,asacomparison,
thesametoolsdefinedinTypeScript(listedinCode2)ismuchshorter. Toimprovecompatibility,partofourtraining
dataalsousesJSONasthetooldeclarationlanguage,sothat3rd-partyframeworksneednotadditionaldevelopmentto
supportourtoolcallingscheme.
Listing1: TooldefinitionwithJSONinOpenAIcompatibleAPI
[{
"type": "function",
"function": {
"name": "get_weather",
"description": "Get weather for a location and date",
"parameters": {
"type": "object",
"properties": {
"location": {
"type": "string",
"description": "City and country e.g. Beijing, China"
},
"date": {
"type": "string",
"description": "Date to query, format in ‘%Y-%m-%d’"
}
},
"required": [
"location"
]
}
}
},
{
"type": "function",
"function": {
"name": "Calculator",
"description": "Simple calculator",
"parameters": {
"properties": {
"expr": {
"type": "string",
"description": "Arithmetic expression in javascript"
}
},
26

KimiK2 TECHNICALREPORT
"type": "object"
}
}
}]
Listing2: TooldefinitioninTypeScript
namespace functions {
// Get weather for a location and date
type get_weather = (_: {
// City and country e.g. Beijing, China
location: string,
// Date to query, format in ‘%Y-%m-%d’
date?: string
}) => any;
// Simple calculator
type Calculator = (_: {
// Arithmetic expression in javascript
expr?: string
}) => any;
}
Thetokentemplateofthetoolinvokingsectioninthemodel’sresponsemessagesislistedasfollows:
<tool_call_section_begin|>
<|tool_call_begin|>
// call_id part
functions.{{tool name}}:{{counter}}
<|tool_arguments_begin|>
{{ json serialized call arguments }}
<|tool_call_end|>
<|tool_call_begin|>
// more tool calls
<|tool_call_end|>
<|tool_call_section_end|>
Asshowninthetemplate,wesupportparalleltoolcallingbyplacingmultipletoolcallsinasingleresponseturn. Each
toolcallhasauniquecallid,formattedasfunctions.{tool-name}:{counter},wheretool-nameisthenameof
thetool,andcounterisanauto-increasingcounterofalltoolcallsstartingfrom0inthedialog.
Duringinference,themodelmayoccasionallygenerateunexpectedtokens,leadingtoformaterrorswhenparsingatool
call. Tosolvethisissue,wedevelopedaconstraineddecodingmodulenamedenforcer,inspiredbylm-format-enforcer6.
Whena<tool_call_section_begin|>tokenisgenerated,itensuresthattheupcomingtool-relatedtokensfollow
thepredefinedtemplate,andtheJSONargumentstringfollowsthedeclaredschema.
Thetoolresultmessageissimplyatextmessageencodedwiththetool’scallidandthecorrespondingresults.
<|im_begin|>
tool
<|im_middle|>
## Results of {{call_id}}
{{ execution result content }}
<|im_end|>
C EvaluationDetails
CodingTasks. WeevaluateKimi-K2-Instruct’scapabilitiesoncompetitivecodingbenchmarks,LiveCodeBenchand
OJBench,whereKimi-K2-Instructattainssuperiorperformancewithscoresof53.7%and27.1%,respectively. This
excellencespansbothmedium-levelcodingchallenges,suchasLeetCodeandAtCoder,andhard-levelcontestslikeNOI
andICPC,outperformingleadingopen-sourceandproprietarymodels. Formultilingualprogrammingproficiency,we
employMultiPL-E,coveringlanguagesincludingC++,C#,Java,JavaScript,PHP,Go,Kimi-K2-Instructsurpassestop
6https://github.com/noamgat/lm-format-enforcer
27

KimiK2 TECHNICALREPORT
open-sourcemodelswithanaccuracyof85.7%,comparedwith83.1%forDeepSeek-V3-0324and78.2%forQwen3-
235B-A22B.Insoftwareengineeringtasks,Kimi-K2-InstructdemonstratesrobustperformanceonSWE-benchVerified
(Python),SWE-lancer(Python),SWE-benchMultilingual,andMulti-SWE-benchdatasets. Itsignificantlyoutperforms
open-sourcecounterpartsinresolvingreal-worldcoderepositoryissuesandnotablynarrowstheperformancegapwith
proprietarymodels. Forexample:
• SWE-benchVerified(multipleattempts): 71.6%(Kimi-K2-Instruct)vs. 80.2%(Claude4Sonnet)
• SWE-benchMultilingual: 47.3%(Kimi-K2-Instruct)vs. 51.0%(Claude4Sonnet)
• SWE-lancer: 39.1%(Kimi-K2-Instruct)vs. 40.8%(Claude4Sonnet)
On PaperBench, Kimi-K2-Instruct achieves an accuracy of 27.8%, closely matching GPT-4.1 and outperforming
DeepSeek-V3-0324(12.2%)andQwen3-235B-A22B(8.2%)byasubstantialmargin. Interminalinteractiontasks
measured by TerminalBench, Kimi-K2-Instruct attains 25.0% using the default Terminus framework and rises to
30%withinMoonshot’sin-houseagenticframework,underscoringitscapabilitiesinreal-worldagenticprogramming
scenarios. Moreover,ontheAider-Polyglotbenchmark,Kimi-K2-Instructattainsa60.0%accuracywhileemploying
rigorousdecontaminationprocedures,furtherillustratingitsstrengthandreliabilityacrossdiversecodingenvironments.
ToolUseTasks. Weevaluatemulti-turntoolusewithtwocomplementarysuites:ω2-BenchandACEBench.ω2-Bench
extendstheoriginalω-benchsingle-controlsetuptoadual-controlenvironmentinwhichboththeagentandanLLM-
simulateduserhaveconstrainedtoolaffordancesoverasharedstate,addingarealisticTelecomtroubleshootingdomain
alongsidethepriorAirline/RetailTAUtasksandenablinganalysisofcoordinationvs. purereasoning. ACEBenchisa
largebilingual(En/Zh)API-groundedbenchmark(4.5KAPIsacross8domains;2Kannotatedevalitems)partitioned
intoNORMAL(basic/personalized/atomic),SPECIAL(imperfectorout-of-scopeinputs),andAGENT(scenario-driven
multi-turn,multi-stepsandbox)trackswithautomatedgradingofcallsandoutcomes. Allmodelsruninnon-thinking
mode;wesetthetemperatureto0.0,usedeterministictooladapters,scoreω2Airline/Retail/TelecomunderAvg@4
seedswithPass@1/4,andreportoverallonACEBenchEnglish. Kimi-K2-Instructaverages66.1microPass@1across
ω2vsDeepSeek-V3-032448.8/Qwen3-235B-A22B37.3. OnACEBenchOverallKimi-K2-Instructscores76.5vs
DeepSeek72.7/Qwen70.5andremainscompetitivewithGPT-4.1(80.1).
Math & STEM & Logical Tasks. For Math tasks, Kimi-K2-Instruct achieves consistently strong performance,
averagingoverGeimini-2.5-Flashby5.3percentagepoints,overDeepSeek-V3-0324by5.5pointsandoverGPT4.1by
15.8points. Forexample,onAIME2024,Kimi-K2-Instructscores69.6%,outperforminganothertwotopopen-source
models by a large margin, DeepSeek-V3-0324 by 10.2 points and Qwen3-235B-A22B by 29.5 points. In STEM
evaluations,Kimi-K2-Instructachieves75.1%onGPQA-Diamond,outperformingDeepSeek-V3-0324(68.4%)andall
non-thinkingbaselinesbyatleast5percentagepoints. OnSuperGPQA,italsoexceedsthepreviousbestopen-source
model,DeepSeek-V3-0324,by3.5points. Kimi-K2-Instructalsosurpassestheothertwoleadingmodelsinlogical
reasoning. Itachieves89.0%onZebraLogicand89.5%onAutoLogi,exceedingDeepSeek-V3-0324(84.0%,88.9%)
andsubstantiallyoutperformingQwen3-235B-A22B(37.7%,83.3%).
GeneralTasks. Kimi-K2-InstructtiesDeepSeek-V3-0324onMMLUandMMLU-Pro,andtakestheleadonMMLU-
Reduxwitha92.7EMscore—slightlyaheadofGPT-4.1(92.4)andjust1.5pointsbehindClaude-Opus-4. Beyond
multiple-choicetasks,themodelachieves31.0%accuracyontheshort-answerSimpleQA—3.3pointsaboveDeepSeek-
V3-0324andmorethantwicethatofQwen3-235B-A22B—thoughstillbelowGPT-4.1(42.3%). Ontheadversarial
free-responseLiveBench(2024-11-25snapshot),itreaches76.4%,surpassingClaude-Sonnet4(74.8%)andleading
Gemini2.5FlashPreviewby8.6points.Acrossthischallengingtriadmeasuringbreadth,depth,androbustnessofworld
knowledge,Kimi-K2-Instructsecuresatop-tierpositionamongopen-sourcemodels. Weevaluateinstruction-following
withIFEvalandMulti-Challenge. OnIFEval,Kimi-K2-Instructscores89.8%,higherthanDeepSeek-V3-0324(81.1%)
andGPT-4.1(88.0%).OnMulti-Challenge,whichinvolvesmulti-turndialogueswithconflictinginstructions,itachieves
54.1%, outperformingDeepSeek-V3-0324(31.4%), GPT-4.1(36.4%), andClaude-Opus-4(49.0%). Theseresults
demonstratethatKimi-K2-Instructintegratesstrongfactualknowledgewithconsistentinstructionadherenceacross
bothsingle-andmulti-turnsettings,supportingrobustandreliablereal-worlddeployment.
LongContextandFactualityTasks. ToevaluatethefactualityofKimi-K2-Instruct,weemploythreebenchmarks:
FACTSGrounding,whichmeasuresadherencetoprovideddocumentsusingtheproprietarymodelsGPT-4o,Gemini
1.5ProandClaude3.5Sonnet;HHEM,whichassessessummarizationqualityviatheopen-sourceHHEM-2.1-Open
judge;andFaithJudge,whichanalyzesfaithfulnessinRAGtaskswitho3-miniasthejudge. Kimi-K2-Instructscores
88.5onFACTSGrounding,substantiallyoutperformingallopen-sourcerivalsandevensurpassingtheclosed-source
Gemini2.5Flash. WithHHEM-2.1-Openitachievesahallucinationrateof1.1%,reportedinthetablesas1minusthe
28

KimiK2 TECHNICALREPORT
Figure11: Chinesein-housebenchmarkevaluation.
rate,i.e. 98.9. OnFaithJudge’sRAGtasksthehallucinationrateis7.4%,likewisepresentas92.6fortableconsistency.
Forlong-contextcapabilities,Kimi-K2-InstructoutperformsallopensourceandproprietarymodelsonDROP(93.5%),
andexceedsDeepSeek-V3-0324onretrievaltaskMRCR(55.0%vs50.8%). Forlong-contextreasoningtasksFRAMES
andLongBenchv2,Kimi-K2-Instruct(77.1%,49.1%)lagsslightlybehindDeepSeek-V3-0324byaround2%.
Open-EndedEvaluation Beyondstatic,closed-endedbenchmarks,weevaluatethemodel’sperformanceonopen-
ended,nuancedtasksthatmorecloselyresemblereal-worldusage.
ForEnglishscenarios,weleveragetheArena-Hard-Autov2.0benchmark,whichuseLLM-as-a-judgeprotocolsto
assess generation quality across diverse, open-ended prompts [42]. These evaluations cover a wide range of high-
difficultypromptsandarewidelyrecognizedintheresearchcommunity. OnArena-Hard-Autov2.0,Kimi-K2-Instruct
achievesstate-of-the-artwin-rateonbothhardprompts(54.5%)andcreativewritingtasks(85.0%),outperformingall
open-sourcemodelsandrivalingtopproprietarysystemssuchasGPT-4.1andClaudeSonnet. Theseresultsunderscore
themodel’sstrengthinhandlingcomplexreasoningandnuancedgenerationunderdiverse,unconstrainedsettings.
However,Arena-Hard-AutoprovideslimitedcoverageofChinese-specifictasks. Toaddressthisgap,wedeveloped
anin-househeld-outbenchmarkgroundedinauthenticuserqueries. Tosafeguardtheintegrityoftheevaluation,the
benchmarkdataisaccess-restricted,therebyeliminatingtheriskofoverfitting.
As shown in Figure 11, Kimi-K2-Instruct shows strong performance across all comparisons on Chinese in-house
benchmarks. ItoutperformsChatGPT-4o-latestwitha65.4%winrate,ClaudeSonnet4with64.6%,andDeepSeek-V3-
0324with59.6%. Inallcases,thelossratestayslow(around17%),indicatingthatKimi-K2-Instructrarelyfallsbehind.
Thehighwinratesandconsistentmarginsdemonstrateitsstrongabilityonopen-endedChinesetasks.
Inadditiontocontrolledevaluations,wealsoconsiderreal-worlduserpreferencethroughpublichumanassessments.
AsofJuly17,2025,Kimi-K2-Instructrankedasthetopopen-sourcemodelandfifthoverallontheLMSYSArena
leaderboard7,basedonover3,000blindvotesfromrealusers. UnlikeLLM-as-a-judgeprotocols,thisleaderboard
reflectsdirecthumanpreferenceondiverse,user-submittedprompts,providingacomplementaryperspectiveonpractical
modelperformance.
TheresultsonArena-Hard-Auto,ourin-housebenchmarkandvotesfromLMSYSArenacollectivelyofferacompre-
hensiveviewofKimi-K2-Instruct’sopen-endedcapabilities,showingthatitisahighlypreferredmodelinreal-world
userexperienceacrossEnglishandChinese.
D QK-ClipDoesNotImpairModelQuality
TheQK-Clipdesignfollowsaminimalinterventionprinciple: itactivatesonlywhennecessary,anddeactivatesafter
trainingstabilizes. Empiricalevidenceandanalysisconvergeonitsnegligibleimpactonmodelquality.
7https://lmarena.ai/leaderboard/text
29

KimiK2 TECHNICALREPORT
Figure12: ApplyingQK-CliptoMuoninasmall-scale
settingwithanaggresivethreshold(ω =30)hasnegligible
impactonloss, indicatingthatitisasafeandeffective
methodforconstrainingattentionlogits.
Small-ScaleAblations Wetraintwosmall-scale0.5Bactivatedand3BtotalparametersMoEmodels,onewithvanilla
MuonandtheotherwithMuonClipusingalowclippingthreshold(ω =30).AsshowninFigure12,applyingMuonClip
hasnegligibleeffectsonthelosscurve,indicatingthatevenaggressiveclippingdoesnotimpairconvergenceortraining
dynamicswithMuonClip. ThisdemonstratesthatMuonClipisasafeandeffectivemethodforboundingattentionlogits
withoutdegradingmodelperformance. Furthermore,evaluationondownstreamtasksrevealsnostatisticallysignificant
degradationinperformance. TheseresultscollectivelydemonstratethatMuonClipisasafeandeffectivemethodfor
boundingattentionlogitswithoutcompromisingmodelquality.
Self-deactivation InKimiK2,QK-Clipwasonlytransientlyactive:
• Initial70000steps: 12.7%ofattentionheadstriggeredQK-Clipforatleastonce,clampingS max to100.
• Post-70000steps: AllheadsatsomepointreducedtheirS max below100,renderingQK-Clipinactive.
WhenQK-Clipisactive,itisappliedper-head(ratherthanper-layer)tominimizepotentialover-regularizationonother
heads. Aftertrainingstabilizes,QK-clipisdeactivatedandhasnoeffectatall.
E WhyMuonisMorePronetoLogitExplosion
Logitexplosionoccurswhenthelargestpre-softmaxattentionscore
S =max q k (1)
max
i,j
i· j
$ %
growsunboundedlyduringtraining. Since
q k q k x x W W , (2)
i j i j i j q k
| · |⇐⇒ ⇒⇒ ⇒⇐⇒ ⇒⇒ ⇒⇒ ⇒⇒ ⇒
andRMS-Normkeeps x x bounded,thephenomenonisprimarilydrivenbythegrowingspectral-normofW or
i j q
⇒ ⇒⇒ ⇒
W . Empirically,wefoundthatMuonismoresusceptibletologitexplosion. Wegiveourhypothesisbelow.
k
Structuraldifferenceinupdates Muonproducesaweightupdatecomingfromthemsignoperation;asaresult,all
singularvaluesoftheupdatematrixareequal—itseffectiverankisfull. Incontrast,atypicalupdatematrixproduced
byAdamexhibitsaskewedspectrum: afewlargesingularvaluesdominate,andtheeffectiverankislow. Thislow-rank
assumptionforAdamisnotnew;higher-ordermuPmakesthesameassumption.
Suchphenomenonisverifiedonthe16BMoonlightmodel,whichshowsweightstrainedwithMuonexhibithigher
singular-valueentropy(i.e.highereffectiverank)thanthosetrainedwithAdam,corroboratingthetheoreticalintuition.
SVDformulation Lettheparametermatrixatstept 1havethesingularvaluedecomposition
↔
W t 1 = ↽ i u i v i→ (3)
↓
i
’
30

KimiK2 TECHNICALREPORT
Wewritetheupdatematricesas
!W t = ↽¯u¯ j v¯ j→ (4)
j
’
Thenextparameterupdateistherefore
W t
↑
↽ i u i v i→ + ↽¯u¯ j v¯ j→ (5)
i j
’ ’
InMuon,asboththeweightsandtheupdateshaveahighereffectiverankthanAdam,wehypothesizethereisahigher
probabilityforsingular-vectorpairu v toalignwithu¯ v¯ . ThiscouldcausethecorrespondingsingularvalueofW
i i→ j j→ t
toincreaseadditively.
Attention-specificamplification Attentionlogitsarecomputedviathebilinearform
q k =(x W ) (x W ). (6)
i j i q j k
· ·
TheproductW W squaresthespectralnorm,soanysingular-valueincreaseineithermatrixiscompounded. Muon’s
q k→
tendencytoenlargesingularvaluesthereforetranslatesintoahigherriskoflogitexplosion.
F K2CriticRubricsforGeneralRL
F.1 CoreRubrics
• ClarityandRelevance: Assessestheextenttowhichtheresponseissuccinctwhilefullyaddressingtheuser’s
intent. Thefocusisoneliminatingunnecessarydetail,stayingalignedwiththecentralquery,andusingefficient
formatssuchasbriefparagraphsorcompactlists. Unlessspecificallyrequired,longitemizationsshouldbeavoided.
Whenachoiceisexpected,theresponseshouldclearlyofferasingle,well-definedanswer.
• ConversationalFluencyandEngagement:Evaluatestheresponse’scontributiontoanatural,flowingdialoguethat
extendsbeyondsimplequestion-answering. Thisincludesmaintainingcoherence,showingappropriateengagement
withthetopic,offeringrelevantobservationsorinsights,potentiallyguidingtheconversationconstructivelywhen
appropriate,usingfollow-upquestionsjudiciously,handlinghypotheticalorpersonal-analogyqueriesgracefully,
andadaptingtoneeffectivelytosuittheconversationalcontext(e.g.,empathetic,formal,casual).
• ObjectiveandGroundedInteraction: Assessestheresponse’sabilitytomaintainanobjectiveandgrounded
tone,focusingsquarelyonthesubstanceoftheuser’srequest. Itevaluatestheavoidanceofbothmetacommentary
(analyzingthequery’sstructure,topiccombination,perceivedoddity,orthenatureoftheinteractionitself)and
unwarrantedflatteryorexcessivepraisedirectedattheuserortheirinput. Excellentresponsesinteractrespectfully
but neutrally, prioritizing direct, task-focused assistance over commentary on the conversational dynamics or
attemptstocurryfavorthroughcompliments.
F.2 PrescriptiveRubrics
• InitialPraise: Responsesmustnotbeginwithcomplimentsdirectedattheuserorthequestion(e.g.,“That’sa
beautifulquestion”,“Goodquestion!”).
• Explicit Justification: Any sentence or clause that explains why the response is good or how it successfully
fulfilledtheuser’srequest. Thisisdifferentfromsimplydescribingthecontent.
F.3 Limitations
Onepotentialsideeffectofthisevaluationframeworkisthatitmayfavorresponsesthatappearconfidentandassertive,
evenincontextsinvolvingambiguityorsubjectivity. Thisstemsfromtwokeyconstraintsinthecurrentrubric:
• AvoidanceofSelf-Qualification: Theprescriptiverulesprohibitself-assessments,explicitdisclaimers,orhedging
language(e.g.,“thismaynotbeaccurate”,“Imightbewrong”). Whilethesephrasescanreflectepistemichumility,
theyareoftenpenalizedasnon-informativeorperformative.
• Preference for Clarity and Singularity: The rubric reward direct, decisive answers when users ask for a
recommendation or explanation. In complex or open-ended scenarios, this may disincentivize appropriately
cautiousormulti-perspectiveresponses.
31

KimiK2 TECHNICALREPORT
Asaresult,themodelmayoccasionallyoverstatecertaintyinareaswhereambiguity,nuance,orepistemicmodesty
wouldbemoreappropriate.Futureiterationsoftheframeworkmayincorporatemorefine-grainedhandlingofcalibrated
uncertainty.
G EngineSwitchingPipelineforRLTraining
H2D Buffer H2D Broadcast (src)
IPC Buffer Reload weights Broadcast (dst)
Device 0
Device 1
Device 2
Device 3
(a)Theoreticalperfectthree-stagepipelineweightupdate
(b)APCIEboundedthree-stagepipeline (c)Fixedtwo-stagepipeline
Figure13: pipelineforRLweightupdate
Thecheckpointenginemanagesthreeequal-sizedevicebuffersoneachGPU:anH2Dbufferforloadingtheoffloaded
modelparameters,andtwoIPCbuffersforGPU-to-GPUbroadcast. TheIPCbuffersaresharedtoinferenceengines,
allowingittodirectlyaccessthesamephysicalmemory. Thesethreebuffersallowustoarrangethethreestepsina
pipeline.
Theoreticalthree-stagepipeline. AsillustratedinFigure13a,athree-stagepipelineisintroduced. (1)H2D:ashard
ofthelatestweightsiscopiedintotheH2Dbufferasynchronously. (2)Broadcast: Oncethecopycompletes,theshard
willbecopiedtooneIPCbuffersandbroadcasttoalldevices. (3)Reload: Inferenceenginessimultaneouslyload
parametersfromtheotherIPCbuffer.
Two-stagepipelineduetoPCIesaturation. OnNVIDIAH800clusters,concurrentH2Dandbroadcastsaturatethe
sharedPCIefabric,collapsingthethreestagesintoasequentialprocedure(Figure13b). Wethereforeadoptasimpler,
two-stagescheme(Figure13c): (1)Alldevicesperformasingle,synchronousH2Dtransfer. (2)Thebroadcastand
reloadproceedinparallel.
Thetwo-stagepipelinewillbeboundbymultiplesynchronousH2Dcopyoperations. Butinlargescaledevices,model
will be split into small shards, the entire parameter set fits into the H2D buffer in one transfer, the overhead will
disappear.
ByoverlappingH2D,Broadcast,andReloadweights,wecanobtainahighbandwidthtoreshardtheweightsfromtrain
enginestoallinferenceengines.
32
