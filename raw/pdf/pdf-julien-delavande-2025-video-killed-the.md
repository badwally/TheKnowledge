---
id: pdf-julien-delavande-2025-video-killed-the
type: pdf
title: 'Video Killed the Energy Budget: Characterizing the Latency and Power Regimes
  of Open Text-to-Video Models'
url: ''
authors:
- Julien Delavande
- Regis Pierrard
- Sasha Luccioni
ingested_at: '2026-04-29T16:13:45Z'
content_hash: sha256:317ce6f78fc0916a7932b19809d3cb789c4b5f9fa62960db90ddca5684f864ae
source_path: raw/pdf/pdf-julien-delavande-2025-video-killed-the.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 17
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__1b710a6e.pdf
published_at: '2025'
---
Video Killed the Energy Budget:
Characterizing the Latency and Power Regimes of
Open Text-to-Video Models
JulienDelavande RegisPierrard
HuggingFace HuggingFace
ENSParis-Saclay regis.pierrard@huggingface.co
julien.delavande@ens-paris-saclay.fr
SashaLuccioni
HuggingFace
sasha.luccioni@huggingface.co
Abstract
Recentadvancesintext-to-video(T2V)generationhaveenabledthecreationof
high-fidelity,temporallycoherentclipsfromnaturallanguageprompts. Yetthese
systems come with significant computational costs, and their energy demands
remain poorly understood. In this paper, we present a systematic study of the
latencyandenergyconsumptionofstate-of-the-artopen-sourceT2Vmodels. We
first develop a compute-bound analytical model that predicts scaling laws with
respecttospatialresolution,temporallength,anddenoisingsteps. Wethenvalidate
these predictions through fine-grained experiments on WAN2.1-T2V, showing
quadraticgrowthwithspatialandtemporaldimensions,andlinearscalingwith
thenumberofdenoisingsteps. Finally,weextendouranalysistosixdiverseT2V
models,comparingtheirruntimeandenergyprofilesunderdefaultsettings. Our
resultsprovidebothabenchmarkreferenceandpracticalinsightsfordesigningand
deployingmoresustainablegenerativevideosystems.
1 Introduction
Text-to-video(T2V)generationhasrapidlybecomeoneofthemostcompellingfrontiersofgenerative
AI.ProprietarysystemssuchasOpenAI’sSora[Brooksetal.,2024]andDeepMind’sVeo[DeepMind,
2025]haveshowcasedremarkableprogressinrealismandtemporalconsistency. Atthesametime,
theopen-sourcecommunityisclosingthegap,releasingincreasinglypowerfulmodels[Guoetal.,
2024,Yangetal.,2025,HaCohenetal.,2024,Team,2024,Wanetal.,2025]thatcanbeexecutedon
commodityGPUs. Asthesesystemstransitionfromresearchprototypestoreal-worldapplications
usedincreativetoolsandproduction-gradevideosynthesisAPIs,itbecomescrucialtounderstand
notonlytheirquality,butalsotheircomputationalcostsandenvironmentalimpacts.
Generatingevenafewsecondsofcoherentvideotypicallyrequiresdozensofdenoisingsteps,high
spatialresolutions,andhundredsofframes. Thisleadstosubstantialenergyconsumptionandlong
inferencetimes. Yet,mostevaluationsofT2Vmodelsemphasizeperceptualmetricssuchassample
fidelity,FIDscores,ormotionsmoothness,whilelargelyoverlookinglatencyandenergyefficiency.
Inanerawheredemocratizationandsustainabilityarekey,theseoverlookeddimensionsdeserve
systematicstudy.
Inthispaper,wemakethefollowingcontributions:
39thConferenceonNeuralInformationProcessingSystems(NeurIPS2025)Workshop:WhatMakesaGood
Video:NextPracticesinVideoGenerationandEvaluation.
5202
peS
32
]GL.sc[
1v22291.9052:viXra

• Theoreticalanalysis. Wedevelopacompute-boundanalyticalmodeloflatencyandenergy
forWAN2.1-T2V[Wanetal.,2025],decomposingFLOPsbyoperatorandpredictingscaling
lawswithrespecttospatialresolution,temporallength,anddenoisingsteps.
• Empiricalvalidation. Weperformfine-grainedmicrobenchmarksonWAN2.1-T2Vtotest
thesepredictions,revealingquadraticscalinginspatialandtemporaldimensions,andlinear
scalinginsteps.
• Cross-model benchmarking. We extend our analysis to six open-source T2V models,
comparingtheirlatencyandenergyprofilesunderdefaultgenerationsettings.
• Implications. We discuss the consequences of these findings for efficient deployment,
sustainablemodeldesign,andfuturedirectionssuchasdiffusioncachingandquantization.
Together, thesecontributionsprovidebothamodelingframeworkandempiricalevidenceforun-
derstandingthestructuralinefficienciesofT2Vpipelines,offeringactionableinsightsforbalancing
qualityandsustainabilityingenerativevideosystems.
2 RelatedWork
Theenvironmentalcostsofmachinelearningareanewbutgrowingfieldofscholarship,starting
withthepioneeringstudyofStrubelletal.,whichwasthefirsttoquantifythecarbonfootprintof
trainingalargelanguagemodel(LLM)[2019]. Thesubsequentyearsweremarkedbymoreworkon
thecarbonfootprintofdifferenttypesofmachinelearning(ML)modelsandthefactorsthatinfluence
themPattersonetal.[2021],Luccionietal.[2022],Guptaetal.[2021],Wuetal.[2022]. Whilemuch
oftheinitialworkwasfocusedonMLmodeltraining–giventhatitpresentsalargerup-frontcostin
termsofenergyandcarbon–recentworkhasincreasinglyfocusedoninference,giventheubiquity
ofdeployingdifferentkindsofMLmodelsinpractice. Notably,Luccionietal.[2024]carriedoutthe
firstlarge-scalestudyontheenergyandcarboncostsfordifferenttasksandapproches,including
imagegeneration.
Whilethereislimitedexistingworkontheenergydemandsofvideogeneration, recentworkby
Lietal.[2024],studiedtheenergyneededtogeneratevideosbytheOpen-SoramodelZhengetal.
[2024]. Theyanalyzedtheenergyrequiredtogenerate2-secondvideosat240presolution,andfound
thatnotonlyisvideogenerationsignificantlymoreenergy-intensivethantextgeneration(which
corroboratesthefindingsofLuccionietal.[2024]),butalsothat"theprimarysourceofemissions
stemmingfromiterativediffusiondenoising". Theyalsofoundthattheenergyrequirementsofvideo
generationscalesnear-quadraticallywithvideoresolution. Thisistheonlyexistingpublishedstudy
ontheenergyrequirementsofvideo-generation,whichisnonethelesslimitedtoasinglemodeland
type of output (i.e. video length and resolution), emphasizing the importance of having a better
understandingofthisimportanttopic. Thiswasthemotivationforourownstudy,whichwedescribe
inthefollowingsection.
3 TheoreticalModelofLatencyandEnergy
Togroundouranalysis,wefocusontheWAN2.1-T2V-1.3Bmodel[Wanetal.,2025],whichservesas
ourreferencearchitecture. WAN2.1isrepresentativeofmodernlatenttext-to-videodiffusionsystems:
apretrainedtextencoderprovidesconditioning,atimestepembeddingMLPinjectsthediffusion
stepindex,alargeDiT(DiffusionTransformer)performsthebulkofspatio-temporaldenoising,and
aVAEdecodermapslatenttensorsbacktopixelspace. ThisstructureisshowninFigure1. The
sameframeworkcanbeappliedtootherrecentmodelswithminoradjustments. WAN2.1isalsothe
mostdownloadedtext-to-videomodelontheHuggingFaceHubatthetimeofwriting,motivatingits
selectionforanin-depthstudy.
Wearethenabletoderiveacompute-boundanalyticalmodelofWAN2.1inference,decomposing
FLOPsbyoperatorandpredictinglatencyandenergyasexplicitfunctionsofresolution(H,W),
numberofframesT,anddenoisingstepsS.
3.1 Computevs. Memory-BoundRegimes
OnmodernGPUssuchastheNVIDIAH100,inferencekernelscanbeeither:
2

Figure1: SimplifiedarchitectureofWAN2.1-T2V-1.3B.
• Compute-bound,whenexecutionislimitedbyarithmeticthroughput(FLOP/s).
• Memory-bound,whenlimitedbymemorybandwidth.
ProfilingshowsthatthemainoperatorsofWAN2.1inference(self-attention,cross-attention,MLPs,
VAEconvolutions)arepredominantlycompute-bound. GPUutilizationremainssaturated,andpower
traces indicate negligible CPU-induced idle time. We therefore adopt a compute-bound model,
followingtheclassicrooflineformulation[Williamsetal.,2009],wherelatencyisproportionalto
totalFLOPsdividedbysustainedthroughput. Thisapproximationisconsistentwithpriorstudiesof
large-scaletransformerworkloads[Shoeybietal.,2019,Narayananetal.,2021,Hagemannetal.,
2024,Jiangetal.,2024,Pavanietal.,2025].
3.2 NotationandConstants
WefollowtheHPCconventionwhereonemultiply-addcorrespondstotwoFLOPs. Throughout,
H W denotesthespatialresolution,T thenumberofframes,S thenumberofdenoisingsteps,N
→
thenumberofDiTlayers,dthehiddensize,f theMLPexpansionfactor,mthetextconditioning
length,gthenumberofclassifier-freeguidance(CFG)passes,andωthelatenttokenlengthseenby
theDiT.Acompletelistofsymbols,constants,andhardwareparametersisprovidedinAppendixA.
TheDiTtokenlengthωgrowswiththespatial(H,W)andtemporal(T)dimensionsofthelatentgrid:
T H W
ω= 1+ .
4 1616
! "
3.3 Operation-LevelFLOPBreakdown
ThetotalFLOPspervideogenerationcanbedecomposedintocontributionsfromthetextencoder,
timestepMLP,thediffusiontransformer(DiT),andtheVAEdecoder,seetable1. Afullderivation
oftheseFLOPformulasisprovidedinAppendixA,wherewedetaileachoperator(self-attention,
cross-attention,MLP,VAE,textencoder,timestepMLP).
3.4 TotalFLOPs
ThetotalFLOPsforgeneratingavideoofspatialsizeH W,T frames,andS stepsis:
→
F =F +F +F +Sg F +F +F +F .
total text VAE,conv VAE,mid-attn self cross mlp ω
·
Wedefineµastheratiobetweensustainedandpeakthroug#hput: $
F /D
µ= total measured.
!
peak
3

Table1: FLOPcostofWAN2.1-T2V-1.3Bcomponents. Top: oncepervideo. Bottom: perdenoising
step(tobemultipliedbygS). SymbolsaredefinedinlineinSection3,withthecompletelistdeferred
toAppendixA.
Component FLOPs Notation
Oncepervideo
Textencoder(T5) p L 8md2 +4m2d +4f md2 F
text text text text text text text
Ndec,conv ! "
VAEdecoderconvolutions 2k(j)k(j)k(j)C(j)C(j)T(j)H(j)W(j) F
t h w in out VAE,conv
j=1
%
VAEdecoder2D“middle”attention T 8C2L +4L2C F
VAE,mid-attn
→ → → → →
! "
Perdenoisingstep(multiplybygS)
DiT
Self-attention(Nlayers) N 8ωd2+4ω2d F
self
Cross-attention(Nlayers) N 4ωd2+4md2+4ωmd F
# $ cross
MLP(Nlayers) N 4fωd2 F
# $ mlp
TimestepMLP(sharedacrosslayers) 2d d + 14d2 F
#ω $ ω
Assumingcompute-boundexecutionwithempiricalefficiencyµ,andletting! denotetheGPU’s
peak
theoretical peak throughput in dense BF16, the total latency D of generating a video can be
total
approximatedas:
F
D total .
total ↑ µ!
peak
Inpractice,theH100providesadenseBF16peakof! = 989TFLOP/s(NVIDIAdatasheet),
peak
butthislevelisunattainable. Theempiricalefficiencyµthusactsasacorrectionfactor,reflecting
both hardware under-utilization (tile misalignment, kernel overheads, memory-bound ops) and
approximationsofourlatencymodel. ForWAN2.1–afterperformingtheexperimentsexplainedin
section4–weobtainµ 0.456,consistentwithsustainedFLOPutilizationof30–63%reportedfor
↑
large-scaletransformerinferenceonH100s[Hagemannetal.,2024,Jiangetal.,2024,Pavanietal.,
2025]. WecalibratedµbylinearregressionofmeasuredlatenciesagainsttheoreticalFLOPsacross
ourexperiments,whichyieldedµ=0.456withnegligibleoverheadandR2 =0.998.
Compute-boundregime. OntheH100,mainoperatorssuchasself-attentionandMLPsbecome
compute-boundabovesequencelengthsofω 295andω 590,respectively.Sinceallconfigurations
studiedhereoperateatmuchhighertokencou ↑ nts(ωistypi ↑ callyinthe104-105rangeevenformoderate
resolutionssuchas480 720andafewsecondsofvideo),theseblocksarefirmlycompute-bound.
→
Forveryshortω,theMLPdominateslatencyandenergy,butsuchregimesarefarbelowouroperating
range. Full derivation and extensions to other hardware showing the same trends are given in
AppendixB.
3.5 EnergyModel
SincesustainedGPUpowerremainsclosetoP duringinference,thetotalenergyconsumedE :
max total
E P D .
total max total
↑ ·
whereP denotestheGPU’smaximumpowerdraw(here 700W). Thus,energyandlatency
max
↓
scaleproportionally.
3.6 PredictedScalingRegimes
Fromtheseequations,wecananticipatedistinctcomputationalregimes:
4

• Quadratic scaling in spatial and temporal dimensions. Since the DiT token length ω
grows linearly with H, W, and T, the self- and cross-attention terms contribute (ω2)
O
FLOPs, leading to quadratic growth in latency and energy as resolution or frame count
increases.
• Linearscalingindenoisingsteps. EachstepappliesthesamesequenceofN transformer
layers,sotheidealcostscalesas (S).
O
• Negligiblecontributionsfromauxiliarycomponents. Thetextencoderisrunonceper
video, and the timestep MLP adds only a small overhead per step. Likewise, the VAE
decoder scales linearly with voxel count T H W and is quickly dominated by the
→ →
quadraticDiTcost.
Insummary,thetheoreticalmodelpredictsthatWAN2.1inferenceistransformer-dominatedand
compute-bound,withquadraticregimesinspatialandtemporaldimensions,lineardependenceon
denoisingsteps,andminoroverheadfromconditioningnetworks. Thesepredictionswillbevalidated
againstempiricalmeasurementsinSection5.
4 Methodology
Ourmethodologycombinestwocomplementaryperspectives. First,weperformcontrolledmicro-
benchmarksonWAN2.1-T2V-1.3B,ourreferencemodel,tovalidatethescalingregimespredicted
bythetheoreticalmodel(Section3). Second, webenchmarkadiversesetofrecentopen-source
text-to-videomodelsunderdefaultsettings,tosituateWAN2.1withinthebroaderecosystem.
4.1 HardwareandMeasurementProtocol
AllexperimentswereconductedonadedicatedNVIDIAH100SXMGPU(80GBHBM3)paired
withan8-coreAMDEPYC7R13CPU,withnoco-scheduledjobs. WemeasuredGPUandCPU
energyusingCodeCarbon[Courtyetal.,2024],whichinterfaceswithNVMLandpyRAPL,and
estimatedRAMenergyusingCodeCarbon’sdefaultheuristic1.
Toreducenoise,eachmeasurementincludedtwowarmupiterations,followedbyfiverepeatedruns.
InferenceusedtheHuggingFaceDiffuserslibraryvonPlatenetal.[2022]withdefaultgeneration
parameters. WereliedonthestandardoptimizationsprovidedbyrecentPyTorchreleases,suchas
fusedkernelsandFlashAttention[Dao,2023],whichareautomaticallyenabled.
4.2 ControlledScalingExperimentsonWAN2.1-T2V-1.3B
To validate the theoretical model, we systematically varied the three key structural parameters:
resolution,numberofframes,anddenoisingsteps. Sincethetextencoderalwayspadsortruncates
promptstoafixedlengthof512tokens,thespecificchoiceofpromptdoesnotaffectruntime. We
thereforefixedasinglepromptandappliedthesamewarmup-and-repetitionprotocolasaboveto
isolatestructuralscalinglaws.
• Spatialresolution: from256 256to3520 1980,bothdimensionsdivisibleby8(model
→ →
constraint). Framesandstepsfixed.
• Temporallength(frames): from4to100inincrementsof4(modelconstraint). Resolution
andstepsfixed.
• Denoisingsteps: from1to200. Resolutionandframesfixed.
Foreachconfigurationweloggedtotallatency(seconds)andenergyforeachhardwarecomponent
(GPU/CPU/RAM).
4.3 Cross-ModelBenchmark
Toprovideabird’s-eyeviewofenergyandlatencycostsacrosscurrentsystems,weselectedadiverse
setofmodelsspanningdifferentarchitecturesandparameterscales(Table2),focusingonthosethat
areamongthemostdownloadedandtrendingontheHuggingFaceHubatthetimeofwriting.
1https://mlco2.github.io/codecarbon/methodology.html#ram
5

Forthisbenchmark,wegenerated50differentpromptspermodel. Eachpromptwasmeasuredwith
theprotocolabove(2warmups,5runs),yieldingrobustaveragesandstandarddeviationsthatcapture
bothruntimenoiseandinputvariability.
• AnimateDiff[Guoetal.,2024](License)-lightweightmotion-layerdiffusion.
• CogVideoX-2b/5b[Yangetal.,2025](License)-cascadedbase+refinerstages.
• LTX-Video-0.9.7-dev[HaCohenetal.,2024](License)-autoregressivetemporalmodeling.
• Mochi-1-preview [Team, 2024](License) - large-scale diffusion optimized for motion
realism.
• WAN2.1-T2V(1.3Band14B)[Wanetal.,2025](License)-high-resolutionlatentdiffusion
withDiTbackbone.
Table2: Defaultgenerationsettingsforeachmodel(fromHuggingFacemodelcards).
Model Steps Resolution(HxW) Frames FPS
AnimateDiff 4 512 512 16 10
→
CogVideoX-2b 50 480 720 49 8
→
CogVideoX-5b 50 480 720 49 8
→
LTX-Video 40 512 704 121 24
→
Mochi-1-preview 64 480 848 84 30
→
WAN2.1-T2V-1.3B 50 720 1280 81 15
→
WAN2.1-T2V-14B 50 720 1280 81 15
→
Wedidnotassessperceptualqualitytoisolatecomputebehavior;instead,theseexperimentsconfront
thepredictedquadraticandlinearregimes(Section3)withactualscalinglawsandscheduler-induced
deviations.Allcode,prompts,andconfigurationsareavailableinananonymizedrepositoryatGitHub
repo,andallgeneratedvideosarereleasedontheHuggingFaceHubatHForg.
5 EmpiricalFindings
WenowcomparethetheoreticalpredictionsofSection3withempiricalmeasurements–firstby
conductingafine-grainedvalidationonWAN2.1-T2V-1.3Bandcomparingmeasuredenergyand
latencyagainsttheoreticalcurvesasresolution,temporallength,anddenoisingstepsvary. Wethen
situatetheseresultsinthebroadercontextofotheropen-sourcevideogenerationmodels.
5.1 ValidationonWAN2.1-T2V-1.3B
InthissectionwefocusexclusivelyonGPUenergyandlatency,sinceGPUaccountsfor80–90%of
thetotalconsumptionanddominatesinferencecost. Figuresshowtheoreticalpredictions(stacked
areas by operator: self-attention, cross-attention, MLP, VAE, text encoder, timestep MLP) with
empiricalmeasurementsoverlaidaspointswitherrorbars.
5.1.1 SpatialResolution
Increasingtheresolutionfrom256 256to3520 1980(frames-81andsteps-50fixed)causes
→ →
bothlatencyandenergytogrowquadratically. Theoreticalpredictions(stackedbyoperator)and
empiricalmeasurementsarecomparedinFigure2. Theagreementremainsstrongacrosstheentire
range,withmodestdeviationsathighresolutions(seeTable3). TheVAEcontributionremainsminor
comparedtotheDiTblocks.
5.1.2 TemporalLength(Frames)
Varying the number of frames from 4 to 100 (resolution - 720 1280 and steps - 50 fixed) also
→
inducesquadraticgrowthinbothlatencyandenergy,asshowninFigure3. Thisbehaviordirectly
followsfromthequadraticdependenceofattentiononthetokencountω. Themodelcloselytracks
empiricalresults,witherrorsreportedinTable3.
6

(a)GPUenergyvs. spatialresolution (b)Latencyvs. spatialresolution
Figure 2: Empirical results (points) vs. theoretical predictions (stacked areas per operator) as a
functionofresolution. Bothenergyandlatencyfollowthepredictedquadraticregime.
(a)GPUenergyvs. numberofframes (b)Latencyvs. numberofframes
Figure 3: Empirical results (points) vs. theoretical predictions (stacked areas per operator) as a
functionoftemporallength. Bothmetricsfollowthequadraticregimepredictedbythemodel.
5.1.3 DenoisingSteps
Incontrasttoresolutionandframecount(resolution-720 1280andframes-81fixed),scalingwith
→
thenumberofdenoisingstepsisperfectlylinear,exactlyaspredictedbythetheoreticalmodel. Each
additionalstepappliesthesameN transformerlayers,leadingtoacostthatgrowsproportionally
withS. Figure4showsnear-perfectalignmentbetweenpredictionsandmeasurements,witherrors
below2%(Table3).
(a)GPUenergyvs. denoisingsteps (b)Latencyvs. denoisingsteps
Figure 4: Empirical results (points) vs. theoretical predictions (stacked areas per operator) as a
functionofdenoisingsteps. BothenergyandlatencyscalelinearlywithS,innear-perfectagreement
withthecompute-boundmodel.
7

Table3: Meanpercentageerror(MPE)betweentheoreticalpredictionsandempiricalmeasurements.
Energy Latency
Resolutionscaling 11.6% 14.0%
Temporallength 6.6% 10.5%
Denoisingsteps 1.9% 1.9%
5.2 Cross-ModelComparison
Finally,wecompareaverageGPUenergyconsumption,latency,andcomponent-wiseenergyshares
acrosssevenopen-sourcetext-to-videomodelsundertheirdefaultgenerationsettings(Figure5).
(a)GPUenergypermodelforonevideo (b)Generationlatencypermodelforonevideo
(c)Energyshares(GPU/CPU/RAM)
Figure5: Cross-modelcomparisonofenergyandlatency. Top: GPUenergyandlatency(logscale,
withstd). Bottom: relativecontributionsofGPU,CPU,andRAM.
Weobserveorders-of-magnitudedisparities: AnimateDiffrequiresonly0.14Whintotal, while
WAN2.1-T2V-14Bconsumesover415Wh,afactorofnearly3000 . Latencyfollowsasimilar
→
trend,withlightweightmodelsproducingclipsinlessthanasecond,whilelarge-scalearchitectures
suchasWAN2.1-14BorMochirequireseveralminutesofinference. Thesedifferencesstemfrom:
• Modelsize: largermodels(WAN2.1-14B,Mochi)processmoreparametersperstep.
• Samplingsteps: AnimateDiffrunsin4stepsvs.60–64forothers.
• Videolength: framecountandFPSvarysignificantly.
• Architecturalcomplexity: cascadedpipelines(CogVideoX)requiremultiplestages.
Asshowninthebottompanel,GPUconsistentlydominatesenergyconsumption(>80%)acrossall
models,confirmingacompute-boundregimewithhighGPUutilization.CPUandRAMcontributions
remainsecondary,thoughslightlymorepronouncedincascadedormulti-stagepipelines.
8

Table 4: Cross-model average latency and energy consumption (default settings). All values are
reportedasmean std.
±
Model Latency(s) GPU(Wh) CPU(Wh) RAM(Wh)
WAN2.1-T2V-14B 1875 2.1 359.7 0.5 35.6 4.0 19.8 0.02
± ± ± ±
WAN2.1-T2V-1.3B 410 0.5 78.8 0.1 7.4 0.4 4.3 0.01
± ± ± ±
Mochi-1-preview 263 0.5 44.7 0.2 4.6 0.01 2.8 0.01
± ± ± ±
CogVideoX-5B 124 0.4 21.6 0.05 2.4 0.03 1.3 0.004
± ± ± ±
CogVideoX-2B 50.6 0.2 8.3 0.03 0.84 0.04 0.53 0.002
± ± ± ±
LTX-Video-0.9.7-dev 9.7 0.01 3.16 0.006 0.32 0.002 0.19 0.001
± ± ± ±
AnimateDiff 0.68 0.002 0.115 0.001 0.016 0.0001 0.008 0.00003
± ± ± ±
6 Discussion
OurresultsconfirmthatWAN2.1inferenceoperatesinacompute-boundregime,wherelatency
andenergyscalequadraticallywithspatial(H,W)andtemporal(T)dimensions,andlinearlywith
denoisingsteps(S). Theclosematchbetweentheoryandmeasurementvalidatestheanalyticalmodel
andprovidesclearguidanceforpractitioners.
Implicationsforefficiency. QuadraticscalinginH,W,andT meansthatevenmodestincreases
inresolutionorvideolengthincursteepcosts: doublinganyofthesedimensionsinisolationyields
4 morecompute,whilescalingmultipledimensionscompoundsmultiplicatively(e.g.,H andW
↓ →
doubled 16 ). Thus,outputsizecontrolisapowerfullever: reducingspatialortemporallength
↔ →
oftensavesmorethanarchitecturalchanges. Inpractice,offeringpresets(e.g.,“lowresolution,low
frames”vs.“highfidelity”)balancesuserneedswithenergycost.
Validatedlinearregimeinsteps. Incontrast,denoisingstepsscalelinearly,withmeasuredcosts
matchingtheoreticalpredictionsonceempiricalefficiencyµisapplied. ThismakesS areliableknob
forlatency–qualitytrade-offs: halvingstepsroughlyhalvesbothlatencyandenergy.
Opportunities for model-level improvements. The public Hugging Face implementation of
WAN2.1lacksinference-timeoptimizations,buttheoriginalpapersuggestseffectivetechniques:
(i)diffusioncaching,reusingredundantattention/CFGactivationsforupto1.62 savings,and(ii)
→
quantization,usingFP8/INT8mixedprecisionfor 1.27 speedupwithoutloss. Otheravenues
↓ →
includesteppruning,low-rankattention,andkernelfusiontobetterexploitGPUtensorcores.
Broaderimplications. Videodiffusionisfarmorecostlythantextorimagegeneration.Normalized
per output, Luccioni et al. [Luccioni et al., 2024] report average costs of 0.002 Wh for text
↓
classification, 0.047 Wh for text generation, and 2.9 Wh for image generation. By comparison,
generatingasingleshortvideowithWAN2.1–T2V–1.3Bconsumesnearly 90Wh.Thisplacesvideo
↓
diffusionroughly30 morecostlythanimagegeneration,2,000 thantextgeneration,and45,000
→ → →
than text classification. At scale, the quadratic growth in (H,W,T) implies rapidly increasing
hardware and environmental costs, highlighting the need for hardware-aware optimizations and
sustainablemodeldesign. TheoreticalthresholdsderivedinAppendixBsuggestthatcompute-bound
behaviorextendstoalltestedaccelerators,reinforcingthegeneralityofourscalingmodel.
7 LimitationsandConclusion
Limitations. OuranalysisprovidesadetailedcharacterizationofWAN2.1–1.3Busingtheopen-
sourceHuggingFacecodebase. Assuch,itdoesnotcapturepotentialimprovementsfrominternal
optimizationssuchasdiffusioncaching,quantization,orkernelfusion. Thetheoreticalmodelalso
assumesuniformattentioncostandignoresmemoryhierarchyeffects,whichmaycausedeviations
forsmallinputsorextremeaspectratios.
Energymeasurementswereconductedonasinglehardwareplatform(NVIDIAH100SXM).While
Appendix B shows that the compute-bound regime and associated scaling trends should extend
9

to other accelerators for realistic token lengths, this remains to be confirmed experimenta. We
deliberatelyexcludedperceptualqualityfromourscope,leavingopenthequestionofenergy–fidelity
tradeoffs. Finally,manyproductionT2Vsystems(e.g.,Veo)alsogenerateaudio,whosecontribution
toenergycostremainsunexplored.
Conclusion. Wepresentedasystematicstudyoflatencyandenergyconsumptionintext-to-video
generation. Throughfine-grainedexperimentsonWAN2.1,wevalidatedasimpleanalyticalmodel
thatpredictsquadraticscalingwithspatialandtemporaldimensions,andlinearscalingwithdenoising
steps. Cross-modelbenchmarksconfirmedthatthiscompute-boundregimeextendsbroadlyacross
recentopen-sourcesystems,withorders-of-magnitudedisparitiesincostdependingonmodelsize,
samplingstrategy,andvideolength.
These findings highlight both the structural inefficiency of current video diffusion pipelines and
theurgentneedforefficiency-orienteddesign. Promisingavenuesincludediffusioncaching,low-
precisioninference,steppruning,andimprovedattentionmechanisms. Wehopethisworkserves
asbothabenchmarkreferenceandamodelingframeworktoguidefutureresearchonsustainable
generativevideosystems.
10

References
Tim Brooks, Bill Peebles, Connor Holmes, Will DePue, Yufei Guo, Li Jing, David Schnurr,
Joe Taylor, Troy Luhman, Eric Luhman, Clarence Ng, Ricky Wang, and Aditya Ramesh.
Videogenerationmodelsasworldsimulators. 2024. URLhttps://openai.com/research/
video-generation-models-as-world-simulators.
BenoitCourty,VictorSchmidt,SashaLuccioni,Goyal-Kamal,MarionCoutarel,BorisFeld,Jérémy
Lecourt,LiamConnell,AmineSaboni,Inimaz,supatomic,MathildeLéval,LuisBlanche,Alexis
Cruveiller,ouminasara,FranklinZhao,AdityaJoshi,AlexisBogroff,HuguesdeLavoreille,Niko
Laskaris,EdoardoAbati,DouglasBlank,ZiyaoWang,ArminCatovic,MarcAlencon,Micha!
Ste˛ch!y,ChristianBauer,LucasOtávioN.deAraújo,JPW,andMinervaBooks. mlco2/codecarbon:
v2.4.1,May2024. URLhttps://doi.org/10.5281/zenodo.11171501.
Tri Dao. Flashattention-2: Faster attention with better parallelism and work partitioning. arXiv
preprintarXiv:2307.08691,2023.
DeepMind. Veo: Advanced video generation model. https://storage.googleapis.com/
deepmind-media/veo/Veo-3-Tech-Report.pdf,2025. Accessed: 2025-08-08.
YuweiGuo,CeyuanYang,AnyiRao,ZhengyangLiang,YaohuiWang,YuQiao,ManeeshAgrawala,
DahuaLin,andBoDai. Animatediff: Animateyourpersonalizedtext-to-imagediffusionmodels
withoutspecifictuning,2024. URLhttps://arxiv.org/abs/2307.04725.
Udit Gupta, Young Geun Kim, Sylvia Lee, Jordan Tse, Hsien-Hsin S Lee, Gu-Yeon Wei, David
Brooks,andCarole-JeanWu. Chasingcarbon: Theelusiveenvironmentalfootprintofcomputing.
In2021IEEEInternationalSymposiumonHigh-PerformanceComputerArchitecture(HPCA),
pages854–867.IEEE,2021.
YoavHaCohen,NisanChiprut,BennyBrazowski,DanielShalem,DuduMoshe,EitanRichardson,
EranLevin,GuyShiran,NirZabari,OriGordon,PoriyaPanet,SapirWeissbuch,VictorKulikov,
YakiBitterman,ZeevMelumian,andOfirBibi. Ltx-video: Realtimevideolatentdiffusion,2024.
URLhttps://arxiv.org/abs/2501.00103.
JohannesHagemann,SamuelWeinbach,KonstantinDobler,MaximilianSchall,andGerarddeMelo.
Efficient parallelization layouts for large-scale distributed model training, 2024. URL https:
//arxiv.org/abs/2311.05610.
ZihengJiang,HaibinLin,YinminZhong,QiHuang,YangruiChen,ZhiZhang,YanghuaPeng,Xiang
Li, CongXie, ShibiaoNong, YuluJia, SunHe, HongminChen, ZhihaoBai, QiHou, Shipeng
Yan,DingZhou,YiyaoSheng,ZhuoJiang,HaohanXu,HaoranWei,ZhangZhang,PengfeiNie,
LeqiZou,SidaZhao,LiangXiang,ZheruiLiu,ZheLi,XiaoyingJia,JianxiYe,XinJin,andXin
Liu. Megascale: Scalinglargelanguagemodeltrainingtomorethan10,000gpus,2024. URL
https://arxiv.org/abs/2402.15627.
BaolinLi,YankaiJiang,andDeveshTiwari. Carboninmotion: Characterizingopen-soraonthe
sustainabilityofgenerativeaiforvideogeneration. ACMSIGENERGYEnergyInformaticsReview,
4(5):160–165,2024.
AlexandraSashaLuccioni,SylvainViguier,andAnne-LaureLigozat. Estimatingthecarbonfootprint
of bloom, a 176b parameter language model, 2022. URL https://arxiv.org/abs/2211.
02001.
Sasha Luccioni, Yacine Jernite, and Emma Strubell. Power hungry processing: Watts driving
the cost of ai deployment? In The 2024 ACM Conference on Fairness, Accountability, and
Transparency,FAccT’24,page85–99.ACM,June2024. doi: 10.1145/3630106.3658542. URL
http://dx.doi.org/10.1145/3630106.3658542.
DeepakNarayanan,MohammadShoeybi,JaredCasper,PatrickLeGresley,MostofaPatwary,Vijay
Korthikanti, Dmitri Vainbrand, Prethvi Kashinkunti, Julie Bernauer, Bryan Catanzaro, Amar
Phanishayee,andMateiZaharia. Efficientlarge-scalelanguagemodeltrainingonGPUclusters.
CoRR,abs/2104.04473,2021. URLhttps://arxiv.org/abs/2104.04473.
11

DavidPatterson,JosephGonzalez,QuocLe,ChenLiang,Lluis-MiquelMunguia,DanielRothchild,
DavidSo,MaudTexier,andJeffDean. Carbonemissionsandlargeneuralnetworktraining,2021.
URLhttps://arxiv.org/abs/2104.10350.
Jessica Pavani, Rosangela Helena Loschi, and Fernando Andres Quintana. Modeling temporal
dependenceinasequenceofspatialrandompartitionsdrivenbyspanningtree: anapplicationto
mosquito-bornediseases,2025. URLhttps://arxiv.org/abs/2501.04601.
MohammadShoeybi,MostofaPatwary,RaulPuri,PatrickLeGresley,JaredCasper,andBryanCatan-
zaro. Megatron-lm: Trainingmulti-billionparameterlanguagemodelsusingmodelparallelism.
CoRR,abs/1909.08053,2019. URLhttp://arxiv.org/abs/1909.08053.
EmmaStrubell,AnanyaGanesh,andAndrewMcCallum. Energyandpolicyconsiderationsfordeep
learninginNLP. CoRR,abs/1906.02243,2019. URLhttp://arxiv.org/abs/1906.02243.
GenmoTeam. Mochi1. https://github.com/genmoai/models,2024.
PatrickvonPlaten,SurajPatil,AntonLozhkov,PedroCuenca,NathanLambert,KashifRasul,Mishig
Davaadorj,DhruvNair,SayakPaul,WilliamBerman,YiyiXu,StevenLiu,andThomasWolf.
Diffusers: State-of-the-artdiffusionmodels. https://github.com/huggingface/diffusers,
2022.
Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu,
HaimingZhao,JianxiaoYang,JianyuanZeng,JiayuWang,JingfengZhang,JingrenZhou,Jinkai
Wang,JixuanChen,KaiZhu,KangZhao,KeyuYan,LianghuaHuang,MengyangFeng,Ningyi
Zhang,PandengLi,PingyuWu,RuihangChu,RuiliFeng,ShiweiZhang,SiyangSun,TaoFang,
TianxingWang,TianyiGui,TingyuWeng,TongShen,WeiLin,WeiWang,WeiWang,Wenmeng
Zhou,WenteWang,WentingShen,WenyuanYu,XianzhongShi,XiaomingHuang,XinXu,Yan
Kou,YangyuLv,YifeiLi,YijingLiu,YimingWang,YingyaZhang,YitongHuang,YongLi,You
Wu,YuLiu,YulinPan,YunZheng,YuntaoHong,YupengShi,YutongFeng,ZeyinziJiang,Zhen
Han,Zhi-FanWu,andZiyuLiu. Wan: Openandadvancedlarge-scalevideogenerativemodels,
2025. URLhttps://arxiv.org/abs/2503.20314.
SamuelWilliams,AndrewWaterman,andDavidPatterson.Roofline:aninsightfulvisualperformance
modelformulticorearchitectures. Commun.ACM,52(4):65–76,April2009. ISSN0001-0782.
doi: 10.1145/1498765.1498785. URLhttps://doi.org/10.1145/1498765.1498785.
Carole-JeanWu,RamyaRaghavendra,UditGupta,BilgeAcun,NewshaArdalani,KiwanMaeng,
Gloria Chang, Fiona Aga, Jinshi Huang, Charles Bai, et al. Sustainable AI: Environmental
implications, challenges and opportunities. Proceedings of machine learning and systems, 4:
795–813,2022.
ZhuoyiYang,JiayanTeng,WendiZheng,MingDing,ShiyuHuang,JiazhengXu,YuanmingYang,
WenyiHong,XiaohanZhang,GuanyuFeng,DaYin,YuxuanZhang,WeihanWang,YeanCheng,
BinXu,XiaotaoGu,YuxiaoDong,andJieTang. Cogvideox: Text-to-videodiffusionmodelswith
anexperttransformer,2025. URLhttps://arxiv.org/abs/2408.06072.
ZangweiZheng,XiangyuPeng,TianjiYang,ChenhuiShen,ShengguiLi,HongxinLiu,YukunZhou,
Tianyi Li, and Yang You. Open-sora: Democratizing efficientvideo production for all. arXiv
preprintarXiv:2412.20404,2024.
12

A DetailedFLOPDerivationsandScalingLaws
Conventions. WefollowtheHPCconventionwhereonemultiply–addequalstwoFLOPs. Matrix
multiplicationsofshape(a b) (b c)thereforecost2abcFLOPs. Biasadditions,activations,layer
→ · →
norms,andsoftmaxarelowerorderandomittedunlessstated. Allresultsbelowapplyperforward
pass.
Table5: CompletesetofWAN2.1-T2V-1.3Bhyperparametersandconstants. Thistableprovidesthe
fullnotation,includingVAElayer-wisesymbols(instantiatedexplicitlyinAppendixA.8).
Symbol Value Meaning
Globalvideoparameters
T variable Numberofframes
H W variable Inputspatialresolution
→
S variable Numberofdenoisingsteps
g 2 CFGpassesperstep(cond+uncond)
v ,v 4,8 TemporalandspatialdownsamplingfactorsoftheVAE
t s
p ,p 2,2 SpatialpatchsizeintheDiTlatentgrid
h w
DiffusionTransformer(DiT)
N 32 NumberofDiTlayers
d 2048 Hiddensize
f 4 MLPexpansionfactor(8192=4d)
ω (1+ T)H W Tokenlengthoflatentgrid
4 1616
Textencoder(T5-XXL)
m 512 Outputtokenspervideo(conditioninglength)
p 2 Callspervideo(cond+uncond)
text
d 4096 Hiddensize
text
L 24 Encoderlayers
text
f 2.5 MLPexpansionfactor
text
Timestepembedding
d 256 HiddenwidthoftimestepMLP
ω
VAE(layer-wise;valuesinApp.A.8)
j 1,...,N LayerindexalongtheVAEdecoderpath
dec,conv
N 11 Numberof3DconvlayersintheVAEdecoder
dec,conv
k(j),k(j),k(j) – 3Dkernelsizesofdecoderlayerj
t h w
C(j),C(j) – In/outchannelsatdecoderlayerj
in out
T(j),H(j),W(j) – Outputgridsizesatdecoderlayerj
C 384 Channelwidthatmiddleattentionblock
T→,H ,W T/4 ,H/8,W/8 Gridsizesatmiddleresolution
L→ → → ↗ ↘ H W Spatialtokenlengthperframe(2Dmiddleattention)
→ → →
Hardware/efficiencyconstants
µ 0.456 Empiricalefficiency(fractionof! )
peak
! 989 1015FLOP/s PeakGPUthroughput(H100)
peak
→
P 700W SustainedGPUpower
max
D F /(µ! ) Totallatency
total total peak
A.1 LatentTokenizationandShapes
LetthevideohaveT framesandspatialsizeH W inpixels. TheVAEdownsamplestemporallyby
→
afactorv andspatiallybyv ,andtheDiToperatesonspatialpatchesofsizep p inthelatent
t s h w
→
13

grid. ThetokenlengthωseenbytheDiTis
T H W
ω = 1+ . (1)
v v p v p
t s h s w
! "
InWAN2.1weuse(v ,v ,p ,p )=(4,8,2,2),hencetheshorthandω=(1+ T)H W usedinthe
t s h w 4 1616
maintext.
A.2 Self-AttentionintheDiT
Letdbethemodelwidthandhthenumberofheads(withd =d/h). Forasequenceoflengthω:
h
Q,K,Vprojections: 3 2ωd2 = 6ωd2
→
Attentionlogits(QK
↑
): 2ω2d
Weightedsum(AV): 2ω2d
Outputprojection: 2ωd2. (2)
SummingonallN DiTlayersyields
F = N (8ωd2 + 4ω2d). (3)
self
→
(Theheadcounthcancelsout,sinceh d =d.)
h
·
A.3 Cross-Attention(Video Text)
↔
Letmbethenumberoftexttokensanddthesharedwidth. AssumingnoKVcache(K,Vrecomputed
eachdenoisingstepasitisdoneinthecurrentofficialimplementation)andonecross-attentionblock
perDiTlayer:
Queryfromvideo: 2ωd2
Keys/valuesfromtext: 4md2 (KandV)
Attentionproducts: 2ωmd + 2ωmd = 4ωmd
Outputprojection: 2ωd2. (4)
HenceovertheNlayers
F = N (4ωd2 + 4md2 + 4ωmd). (5)
cross
→
WithKVcaching,the4md2termbecomesonce-per-videowhilethe4ωmdproductsremainperstep.
Withwindowedorfactorizedattention,ωormmaybereplacedbytheeffectivewindowsize.
A.4 TransformerMLP
Withexpansionfactorf andsequencelengthω, atwo-layerMLPd fd dcostsoverallDiT
↔ ↔
layers
F = N 4fωd 2. (6)
mlp
→
A.5 StackingAcrossS Steps,andCFG
Let g denote the number of conditional forward passes (CGF) per denoising step (g = 2 under
classifier-freeguidance). Combining(3)–(6),theDiTcostis
F (T,H,W;S,N,d,f,m,g) = gS F +F +F , (7)
DiT self cross mlp
→
withωgivenby(1).
# $
A.6 TextEncoder
ForaL -layerencoder(e.g.,T5/CLIP-like)withwidthd ,expansionf ,andmtokens:
text text text
Self-attnperlayer: 8md2 +4m2d
text text
FFNperlayer: 4f md2 . (8)
text text
Forp forwardpassespervideo(e.g.,p =2forconditionalandunconditionalprompts),
text text
F = p L 8md2 +4m2d +4f md2 . (9)
text text text text text text text
Thistermisonce-per-video,independentofS.
# $
14

A.7 TimestepEmbeddingMLP
Mappingascalardiffusionsteptoad-dimvectorandinjectingitintoeachblockviaasmallMLP
withhiddenwidthd :
ω
F = gS(2d d + 14d2). (10)
ω ω
A.8 VAE:ConvolutionsandMiddleAttention
WeaccountfortheVAEcostasthesumof(i)allconvolutionallayersalongthedecoderand(ii)a2D
self-attention“middle”blockevaluatedindependentlypertimeslice.
Convolutionallayers. Fora3Dconvolutionwithkernel(k t (j),k h (j),k w (j)),channelsC i ( n j) ↔ C o (j u ) t
andoutputsizeT(j) H(j) W(j),thecostis
→ →
F(j) = 2k(j)k(j)k(j)C(j)C(j) T(j)H(j)W(j). (11)
conv3d t h w in out
SummingoverthedecoderpathgivesF = Ndec,convF(j) ,withconcreteper-layershapes
VAE,conv j=1 conv3d
providedinTable6. WAN-2.1VAEincludea2Dself-attentionmiddleblockevaluatedindependently
&
oneachtimeslice(L =H W ,channelwidthC ):
→ → → →
F = T 8C2L + 4L2C . (12)
VAE,mid-attn
→ → → → →
# $
Middleself-attention(2D,pertimeslice). LetC bethechannelwidthatthemiddleresolution,
and T ,H ,W the temporal/spatial sizes (thus L→ = H W tokens per time slice). Using the
deriva→tion→inA→ppendixA.2,themiddleattentioncos→tis → →
F = T 8C2L + 4L2C , (13)
VAE,mid-attn
→ → → → →
wherethefinal2C2L termarisesfromtheout#putprojectionandi$sincludedinthe8C2L term
above. → → → →
WAN2.1decoderinstantiation(values). InWAN2.1,theVAEdecoderstartsfromalatentgrid
(T ,H ,W )= T/4 , H/8, W/8 withz=16channels. Acausal3 3 3convolutionexpands
0 0 0
↗ ↘ → →
thisto384channels,followedbya“middle”blockconsistingoftworesidual3 3 3convolutions
# $ → →
anda2Dself-attentionlayerappliedindependentlypertimeslice. Thedecoderthenprogressively
upsamples: twotemporal+spatialupsamplings(doublingT,H,W andhalvingchannels),followed
byonepurelyspatialupsampling(doublingH,W andhalvingchannels). Residualblocks(threeper
stage)refinefeaturesateachresolution,andafinal3 3 3convolutionproducestheRGBoutputat
→ →
(T,H,W).
Table6summarizesthedominantoperatorsforFLOPaccounting. ApplyingEq.(11)acrossthese
layersyieldsF ,whileEq.(13)givesthemiddle-attentioncost.
VAE,conv
A.9 TotalFLOPsandLeading-OrderScaling
Wefinallyobtain
F (H,W,T,S) = F + F + F + F + F , (14)
total text VAE,conv VAE,mid-attn ω DiT
withcomponentsgivenby(9),(11),(13),(10),and(7). SinceωgrowslinearlywithH,W,andT
(Eq.1),theω2dandωmdtermsinF dominatefortypicalsettings(ω m),yieldingquadratic
DiT
≃
growthinH,W,andT,andlineargrowthinS.
Scopeandcaveats. (i)FlashAttentionandfusedkernelsreducememorytrafficandconstantsbut
do not change FLOP counts. (ii) KV caching changes only the cross-attention 4md2 term from
per-steptoonce-per-video. (iii)Windowedorfactorizedattentionreplacesω(orm)byaneffective
windowsize,alteringquadraticscaling. (iv)Ifactivationsornormsbecomebandwidth-bound,the
proportionalitybetweenFLOPsandlatencyweakens;ourWAN2.1measurementsonH100indicated
compute-boundbehaviorovertheoperatingpointsconsidered.
15

Table6: VAEdecoder: representativedominantoperatorsforFLOPaccounting(layerj). Itmirrors
theencoder;z=16,C =384,middleresolution( T/4 ,H/8,W/8).
→ ↗ ↘
Stagej Optype Kernel(k ,k ,k ) C(l) C(l) T(l) H(l) W(l)
t h w in ↔ out
D0 conv3d (3,3,3) z 384 T/4 H/8 W/8
↔ ↗ ↘
Middle(RBs) conv3d (3,3,3) 384 384 T/4 H/8 W/8
↔ ↗ ↘
Middle(attn2D) attn-2D – 384 384 T/4 H/8 W/8
↔ ↗ ↘
D1(RBs) conv3d (3,3,3) 384 384 T/4 H/8 W/8
↔ ↗ ↘
Up(time) conv3d(time) (3,1,1) 384 2 384 T/2 H/8 W/8
↔ → ↗ ↘
Up(space) conv2d(space) (1,3,3) 384 192 T/2 H/4 W/4
↔ ↗ ↘
D2(RBs) conv3d (3,3,3) 192 384 T/2 H/4 W/4
↔ ↗ ↘
Up(time) conv3d(time) (3,1,1) 384 2 384 T H/4 W/4
↔ →
Up(space) conv2d(space) (1,3,3) 384 192 T H/2 W/2
↔
D3(RBs) conv3d (3,3,3) 192 192 T H/2 W/2
↔
Up(space) conv2d(space) (1,3,3) 192 96 T H W
↔
Head conv3d (3,3,3) 96 3 T H W
↔
B TheoreticalCompute-BoundThresholdsforDiTBlocks
Weestimatethearithmeticintensity(FLOPperbytetransferredbetweenHBMandregisters)forthe
mainoperationsinDiT:theself-attentionblock(withFlashAttention)andtheMLP.Wethenderive
thecompute-boundthresholdωε atwhichtheoperation’sintensitymatchesthehardwarebalance
ε =! /B.
peak
Letsbethebytesizeofascalar(e.g.,s=2forBF16),andassumeafullyoptimizedimplementation
thatreadsinputsandwritesoutputsonlyoncefromHBM,soeachtensorcontributestwicetomemory
traffic(read+write).
FlashAttention(forward). WeincludeonlythematrixmultiplicationsQK ↑ andPV (notprojec-
tions). ThetotalFLOPsscaleasF =4ω2d,andtotalmemorytransferasD =2ωds(readinputs
attn attn
Q,K,V andwriteoutputofsizeωd).
F 4ω2d 2ω sε
AI (ω)= attn = = ωε =
attn D 2ωds s ⇐ attn 2
attn
MLP block (GEMM) The total FLOPs are F = fωd2, and the memory transfer is D =
mlp mlp
(fd2+ωd+fωd)s.
F fωd
AI (ω)= mlp = ωε =sε
mlp D (fd+ω(1+f))s ⇐ mlp
mlp
Ford=2048,s=2,andε =295(H100BF16),wefind:
2 295
ωε = · =295,ω ε =2 295=590,
attn 2 mlp ·
Thus,allMLParecompute-boundforω> 590,andattentionbecomescompute-boundforω> 290.
InourWAN2.1runs,ω 104,sobothblocksoperatefarinthecompute-boundregime.
≃
Caveat. Thesethresholdsassumepeaktheoreticalperformance. Inpractice,weobserveanem-
piricalefficiencyµ 0.4forcomputethroughputontheH100. Similarly, theeffectivememory
↑
throughputoftenremainswellbelowBduetoirregularaccesspatternsandlatencybottlenecks.
Otherhardware. Table7 reportsε andthe correspondingcompute-bound thresholdsforboth
attentionandMLPblocksacrossarangeofaccelerators.
16

Table7: ApproximateFLOP-to-bandwidthratios(ε =! /B)andcorrespondingcompute-bound
peak
thresholdsωεforDiTblocks(BF16).
Accelerator ! Bε ω ε /ωε
peak attn mlp
(TFLOP/s) (TB/s) (FLOP/byte)
NVIDIAH100SXM 989 3.35 295 295/590
NVIDIAA100SXM 312 2.0 156 156/312
RTX4090 330 1.0 330 330/660
NVIDIAL4 121 0.3 605 605/1210
TPUv6 918 1.6 574 574/1148
AMDM3250X 2500 6.0 417 417/834
IntelGaudi3 1678 3.7 453 453/906
AllrealisticsettingsinWAN2.1yieldω 104,evenforlow-resolutionandshort-durationinputs.
≃
Thus,bothMLPandattentionblocksoperatewellbeyondthecompute-boundthresholdonalltested
accelerators.
17
