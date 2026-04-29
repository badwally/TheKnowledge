---
id: pdf-ali-modarressi-2025-nolima-long-context
type: pdf
title: 'NoLiMa: Long-Context Evaluation Beyond Literal Matching'
url: ''
authors:
- Ali Modarressi
- Hanieh Deilamsalehy
- Franck Dernoncourt
- Trung Bui
- Ryan Rossi
- Seunghyun Yoon
- Hinrich Schütze
ingested_at: '2026-04-29T16:13:59Z'
content_hash: sha256:01754197d9d85be7c16eb8bc60514c9bc33b0c04bee80e27ccc839f4f46d922f
source_path: raw/pdf/pdf-ali-modarressi-2025-nolima-long-context.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 15
  extraction_tool: pdfplumber
  pdf_metadata_subject: Proceedings of the International Conference on Machine Learning
    2025
  pdf_metadata_keywords: Machine Learning, ICML
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__2d1e08cb.pdf
published_at: '2025'
---
NOLIMA: Long-Context Evaluation Beyond Literal Matching
AliModarressi12* HaniehDeilamsalehy3 FranckDernoncourt3 TrungBui3 RyanRossi3 SeunghyunYoon3
HinrichSchu¨tze12
Abstract overextendeddocuments. Examplesincludelong-ormulti-
Recent large language models (LLMs) support document question answering (QA), summarization, and
longcontextsrangingfrom128Kto1Mtokens.A many-shotin-contextlearning(Leeetal.,2024;Changetal.,
popularmethodforevaluatingthesecapabilities 2024;Agarwaletal.,2024).Toevaluatethesemodels’effec-
is the needle-in-a-haystack (NIAH) test, which tivenessinhandlinglongcontexts,severalbenchmarkshave
involvesretrievinga“needle”(relevantinforma- beendeveloped. OneprominentbenchmarkisNeedle-in-a-
tion)froma“haystack”(longirrelevantcontext). Haystack(NIAH),whichtestsamodel’sabilitytosearch
Extensions of this approach include increasing forandretrieveaspecificfact(the“needle”)hiddenwithin
distractors,factchaining,andin-contextreason- irrelevantinformation(the“haystack”)(Kamradt,2023;Mo-
ing. However,inthesebenchmarks,modelscan htashami & Jaggi, 2023). While the baseline NIAH task
exploitexistingliteralmatchesbetweenthenee- assessessurface-levelretrievalcapabilities,recentadapta-
dleandhaystacktosimplifythetask. Toaddress tionshaveincreaseditscomplexity. Theseenhancementsin-
this,weintroduceNOLIMA,abenchmarkextend- cludeintroducingmultipleneedles,incorporatingadditional
ing NIAH with a carefully designed needle set, distractormaterial,andinterconnectingfactstonecessitate
wherequestionsandneedleshaveminimallexical in-contextreasoning(e.g.,fact-chaining)(Hsiehetal.,2024;
overlap,requiringmodelstoinferlatentassocia- Levyetal.,2024;Kuratovetal.,2024). Otherbenchmarks,
tionstolocatetheneedlewithinthehaystack. We suchaslong-,multi-documentQA,andlongconversation
evaluate12popularLLMsthatclaimtosupport understanding, have also been proposedto evaluate long-
contextsofatleast128Ktokens. Whiletheyper- contextcomprehensioninamoredownstreamtaskmanner
formwellinshortcontexts(<1K),performance (Liuetal.,2024;Yenetal.,2024;Zhangetal.,2024;Dong
degradessignificantlyascontextlengthincreases. etal.,2024;Wangetal.,2024;Maharanaetal.,2024).
At32K,forinstance,10modelsdropbelow50%
Arguably,thesetasksshareacommonfoundation: theabil-
oftheirstrongshort-lengthbaselines. EvenGPT-
ity to recall previously seen information (Goldman et al.,
4o,oneofthetop-performingexceptions,experi-
2024). This broader category, termed association recall
encesareductionfromanalmost-perfectbaseline
tasks, has been extensively studied in machine learning
of99.3%to69.7%. Ouranalysissuggeststhese
(Graves et al., 2014; Ba et al., 2016). A key argument is
declinesstemfromtheincreaseddifficultytheat-
thattheattentionmechanism,whichistheunderlyingfoun-
tentionmechanismfacesinlongercontextswhen
dation of many LLMs, is inherently adept at identifying
literal matches are absent, making it harder to
andrecallingassociationspresentintheinput(Olssonetal.,
retrieverelevantinformation.
2022;Aroraetal.,2024). However,thisraisesanimportant
question: Long-contextbenchmarksfeaturetaskswherethe
queriedinput(e.g.,aquestionoratask)hasliteralmatches
1.Introduction
withtheprovidedcontext. Dosuchliteralmatchesmakeit
Inrecentyears,largelanguagemodels(LLMs)havemade easierforlanguagemodelstolocaterelevantinformation
remarkableadvancementsinhandlinglong-contextinputs andoutputcorrectanswers?
(Chen et al., 2023; Xiong et al., 2024; Peng et al., 2024).
Wearguethatmanyexistinglong-contextbenchmarkseither
This capability has unlocked new possibilities in various
explicitly(e.g.,synthetictasksorNIAH-based)orimplicitly
NLPtasksthatrequireunderstandingorgeneratingcontent
(e.g.,multi-documentorlong-documentQA)containsuch
*WorkdoneduringaninternshipatAdobeResearch. 1Center literalmatches. Toaddressthis, weintroduce NOLIMA,
forInformationandLanguageProcessing,LMUMunich,Germany abenchmarkdesignedtominimizeliteraloverlapbetween
2MunichCenterforMachineLearning(MCML)3AdobeResearch. questions and their corresponding needles. In NOLIMA,
Correspondenceto:AliModarressi<amodaresi@cis.lmu.de>. questions and needles contain keywords that are related
through associative links, such as real-world knowledge
1
5202
beF
7
]LC.sc[
1v76150.2052:viXra

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
orcommonsensefacts. Byembeddingtheseneedlesina R-1 R-2 R-L
haystack, NOLIMA challenges models to leverage latent
Long-documentQA
associative reasoning capabilities rather than relying on BenchQA(Zhangetal.,2024) 0.966 0.545 0.960
→
surface-levelmatching. BenchMC(Zhangetal.,2024) 0.946 0.506 0.932
→
We evaluate NOLIMA over 12 state-of-the-art language RAG-style(Multi-doc)QA
RULERQA(Hsiehetal.,2024) 0.809 0.437 0.693
models, all claiming to support token lengths of at least
HELMET(RAG)(Yenetal.,2024) 0.689 0.304 0.555
128K,includingGPT-4o, Gemini1.5Pro, andLlama3.3
Recall-based
70B(Hurstetal.,2024;Teametal.,2024a;Meta,2024).Un-
VanillaNIAH(Kamradt,2023) 0.905 0.789 0.855
likeNIAH-basedevaluations,whichcontainliteralmatches
RULERS-NIAH(Hsiehetal.,2024) 0.571 0.461 0.500
andexhibitnear-saturatedperformance,NOLIMApresents BABILong(0K)(Kuratovetal.,2024) 0.553 0.238 0.522
amoredemandingchallengethathighlightsthelimitations
NOLIMA 0.069 0.002 0.067
ofthesemodels. Weevaluate12state-of-the-artlanguage
models, allofwhichclaimtosupporttokenlengthsofat
Table1.ROUGE precision scores between the input document
least128K,includingGPT-4o,Gemini1.5Pro,andLlama
andthequestion: higherROUGEscoresindicategreaterliteral
3.370B(Hurstetal.,2024;Teametal.,2024a;Meta,2024). matchesbetweenthequestionandtherelevantcontext.
Theirperformancedeclinesnoticeablyascontextlengthin-
creases,withconsiderabledropsevenat2K–8Ktokens. For
instance,at32Ktokens,10outof12modelsachieveonly evaluatethiscapability. Needle-in-a-Haystack(NIAH)is
halfoftheirshort-contextperformance. the most well-known and widely used benchmark (Mo-
htashami & Jaggi, 2023; Kamradt, 2023). However, due
We conduct extensive analyses using NOLIMA, yielding
to performance saturation, various extensions have been
thefollowinginsights:
proposed. Theseincludeincreasingcomplexitybyadding
moreneedles,chainingneedlestorequireinter-needlerea-
• Impact of Latent Hops and Fact Direction: We
soning(fact-chaining),orincorporatingarithmeticorcode
demonstrate how the number of associative reason-
reasoning(Kamradt,2023;Hsiehetal.,2024;Levyetal.,
ing steps (latent hops) and the ordering of elements
2024;Kuratovetal.,2024;Hengleetal.,2024;Zhangetal.,
withinafactstatementsinfluencetaskperformance.
2024). Sometasksincreasethecomplexitytosuchanex-
• Context Length vs. Needle Position: Our aligned- tentthattheybecomeoverlydifficulteveninshort-context
depth analysis shows that as latent reasoning com- scenarios. Forinstance,BABILongincludestasksthatper-
plexitygrows,performancedependsmoreoncontext formpoorly(e.g. thecountingtaskachieves28%accuracy)
lengththanneedleposition.Withoutsurface-levelcues, evenwithoutanyirrelevantbackgroundtext(0K)(Kuratov
longercontextsoverwhelmtheattentionmechanism. etal.,2024). Similarly,theAncestralTreeChallenge(ATC)
employsextensivefact-chaining,resultingintasksthatare
• AblationTests: Weconfirmthatthepresenceofliteral
overly complex even for short contexts (<1K) (Li et al.,
matchessignificantlysimplifiesthetask,enablingmod-
2024). Whilesuchtaskschallengelanguagemodelsinlong
elstoachievehighaccuracyinansweringquestions. In
contexts, they raise the question of whether the tasks are
contrast,whenliteralmatchesserveasdistractors,they
inherentlytoocomplexformodelstohandle,regardlessof
severelyimpairaccuracy.
contextlength.
• Chain-of-Thought(CoT)PromptingandReasoning-
based Models: While CoT prompting or reasoning- Literal Matchingin Long-Context Benchmarks. An-
basedmodelssuchasGPT-o1(OpenAIetal.,2024) otherfrequentpatterninmanylong-contextbenchmarksis
improveperformancebyencouragingstep-by-steprea- thepresenceofliteralmatchesbetweenthefactsrequired
soning,theyfailtofullymitigatethechallenge,partic- toansweraquestionandthequestionitself. Thisfactisnot
ularlyincontextsexceeding16Ktokens. limitedtosyntheticrecall-basedtasks(e.g.,vanillaNIAH,
RULERretrieval-basedsets)butalsoaffectsdownstream-
ThroughNOLIMA,werevealthelimitationofliteralmatch- likeQA-basedbenchmarks(Hsiehetal.,2024;Liuetal.,
inginlong-contextbenchmarksandintroduceanovelap- 2024;Zhangetal.,2024;Baietal.,2024;Yenetal.,2024),
proach for evaluating models’ latent reasoning in longer whichoftenimplicitlyincludeliteralmatchesbetweenthe
contexts. relevant document and the question. Although many of
thesestudiesintroducecomplexitybyaddingsimilardocu-
mentsasdistractors,literalmatchescanstillprovidecues.
2.RelatedWork
These cues may help models focus on potential relevant
With the increasing popularity of long-context language factsbasedonmatches,asattentionmechanismsexcelat
modeling,numerousbenchmarkshavebeenintroducedto recallingrepetitivepatterns(Olssonetal.,2022;Aroraetal.,
2

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
Question Needles KeywordTypes
WhichcharacterhasbeentoW q? D
In
e
v
f
.
. A
W
c
n
tu
i
a
s
ll
n
y
e
,
x
[
t
C
t
H
o
A
w
R
he
]
r
l
e
iv
[
e
C
s
H
n
A
ex
R
t
]
to
liv
th
e
e
s.
W n. W
W
n
q
B
C
u
o
i
u
l
n
d
t
i
r
n
i
g
es
s
,
&
cit
L
ie
a
s
n
,
d
s
m
ta
a
te
rk
s
s
Table2.AnexampletemplateoftheproposedneedlesetinNOLIMA(alltemplatesareavailableinAppendixA.)Theplaceholders
[CHAR], W q, and W n represent the randomly selected character (also the answer), the query keyword, and the needle keyword,
respectively.Def.:defaultorder.Inv.:invertedorder.
2024). Welaterdemonstratetowhatextentliteralmatches TheSemperOperaHouseislocatedinDresden. Thus,the
simplifyrecall-basedquestions(cf. 4.4.4). Toquantifythe modelshouldbeabletoidentifythelatentassociationlink
prevalence of these matches in popular benchmarks, we between W (“Dresden”) in the question and W (“Sem-
q n
compute ROUGE (R-1, R-2, and R-L) precision scores1 perOperaHouse”)intheneedle. Sincethereisnoliteral
(Lin,2004)betweentheneedle(inrecall-basedtasks),the overlapbetweenneedleandquestion,themodelmustrely
relevantdocument(inmulti-documentsetups),orthefull onthislatentassociationlinktoretrieve“Yuki”,thecorrect
document(inlong-documentQA)andthecorresponding answer. Forsomeofourneedles,theassociationinvolves
question. Thisanalysismeasuresthedegreeofliteralover- commonsensereasoninginsteadofworldknowledge. Ex-
lap between the question and the context. Based on the ample: “ThenYukimentionedthathehasbeenveganfor
scoresinTable1,NOLIMAdemonstratessignificantlyless years.” “Whichcharactercannoteatfish-basedmeals?”
→
literaloverlapcomparedtootherdatasets. Topushthelimitsofthemodel’sabilitytoidentifyhidden
associations,weincludequestionsthatrequiretwohopsto
connectW withW ,forexample:
3. NOLIMA q n
ThegoalofNOLIMAistodesignataskthatisinherently WhichcharacterhasbeentothestateofSaxony?
simpletosolvethroughassociativereasoning,butforwhich
Here,themodelshouldtapintoitsknowledgethatDresden
surface-level matching has zero utility. As a result, NO-
(and hence the Semper Opera) is located in the state of
LIMAallowsustocleanlyinvestigateassociativereasoning
Saxony. Thistwo-hopsetupfurtherincreasesthedifficulty
inlong-contextscenarioswithoutconfoundingfromsurface-
ofidentifyingthelatentassociationofW withW .
leveleffects. q n
TomakeNOLIMAaneffectivebenchmarkforevaluating
ThemainelementsofNOLIMAaresimilartovanillaNIAH.
LLMlong-contextabilities,weimposeseveralconstraints
A“needle”–asinglekeypieceofinformation–isplaced
ontheneedleset. (i)Weselectkeywordsthatensuresim-
withina“haystack”,i.e.,alongirrelevanttext(inourcase,
plicity–sothat,withoutirrelevantcontext,theassociations
snippetsfrombooks). Givenaquestion,themodelisthen
areclearandthemodelcanidentifythecorrectanswer. (ii)
testedonitsabilitytofindtheneedle.Theneedleisdesigned
We randomize the assignment of character names from a
tobeaclearlyrelevantanswertothequestion. Incontrastto
diversepooltominimizesensitivitytotokenizationprob-
existingNIAHtasks,weimposetheconditionthattheques-
lems and mitigate ethnic bias (Navigli et al., 2023; Jiang
tionhaveminimalliteralmatchwiththeneedle. Toachieve
etal.,2024). Namesalreadyoccurringinthehaystacksare
this,wedesignasetofneedlesandcorrespondingquestions,
excluded. (iii)WeensureW isuniquelyassociatedwith
collectivelyreferredtoasa“needleset.” Table2presents n
W ,avoidlanguage-basedcuesandemployprefacephrases
oneoftheconstructedneedlesettemplates(seeAppendixA q
toisolateneedlesfromprecedingcontext. SeeAppendixA
forthefulllist). Eachneedleconsistsofauniquecharacter
fordetails.
andspecificinformationaboutthem. Example:
Actually,YukilivesnexttotheSemperOperaHouse. 3.1.HaystackFilteringPipeline
Theneedlecontainsakeyword(W ,here“SemperOpera Toensurethatthehaystackdoesnotcontain: (1)Anydis-
n
House”)thatservesasthecriticallinkbetweenneedleand tracting words that have extreme literal or high semantic
question. Thequestionisdesignedtoretrievethisinforma- similaritieswiththekeypointsmentionedinthequestion(2)
tionbyaskingwhichcharacterpossessesaspecificattribute Anyinformationthatexplicitlyorinaninferrablecasebea
W ,“Dresden”intheexample: potentialfalseanswertothequestion,wedeviseafiltering
q
process.
WhichcharacterhasbeentoDresden?
1Weuseprecisionasourmetrictomeasurehowmanyofthe DistractorFiltering. Forthisstep,weuseanembedding
question’s tokens exist in the relevant context, rather than the function, Contriever(Izacardetal.,2022), tofindsimilar
reverse. words in the haystack to the keywords of the questions.
3

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
"Books ! Needle set
w/o distractors
Remove conflicting
Gather questions
information from the text
Which character has been
------------- ------------- -------------
--------------- to France? --------------- ---------------
--------------- --------------- ---------------
--------------- --------------- ---------------
--------------- --------------- ---------------
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Scan over + #Llama 3.3 70b ! ! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - . - - . - - . - - - - - - - - - - - - - - - -
--------------- chunks Manually check --------------- ---------------
--------------- flagged examples --------------- ---------------
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - T Yo a u s ' k ll P be r o g m ive p n t : a text snippet and a question afterward. You must answer the (not N/A) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
--------------- question based on the information in the text snippet. The answer should --------------- ---------------
--------------- either be based on a *direct mention* or a *strong inference*. IMPORTANT: --------------- ---------------
--------------- The response should include an explanation leading to the final answer or, if --------------- ----... -------
--------------- there is no answer, write N/A. --------------- ---------------
--------------- --------------- ---------------
--------------- + 4 Shots (2+2 N/A) Examples --------------- ---------------
--------------- --------------- ---------------
--------------- Story: {Chunk} --------------- ---------------
----------... Question:{Question} --------... ---...
Repeat until no further removal
Figure1. Haystackconflictinginformationfilteringpipeline
Firstwegatherallwordsinthehaystackandcomputetheir 4.Experiments
respectiveembedding. Thenusingdot-productsimilarity
4.1.DatasetConfiguration
wecomputetheirsimilaritytothequestionkeywords. We
manually inspect the top-20 similar words per each W q In NOLIMA, we use 5 groups of needles, each with two
andflagthosewithhighsemanticorsubstringsimilarityfor fact-order variations: default and inverted. In the default
removal.Intheremovalprocessthosesentencesthatcontain order,theanswercharacteralwaysprecedestheneedlekey-
flaggedwordsareremovedfromthehaystack. Thisinitial wordW . Intheinvertedorder,thefactisconveyedwith
n
filteringstephelpstoavoidanuncontrolledsetofsuperficial thecharacternameplacedafterW . Eachgroupincludes
n
distractorsthatcouldundesirablydisrupttheexperimental 2–6keywordsets,withsomesetscontainingmultipleW
q
results. We will discuss the impact of distractors on the itemstoproducebothone-hopandtwo-hopexamples. This
modelperformanceinouranalysis(Section4.4.4). setupresultsin58question-needlepairsintotal. Togen-
eratethehaystacks,weselect10open-licensedbooks,en-
suringeachcoversatleast50Ktokens. Usingthefiltering
mechanism described in Section 3.1, we process the text
ConflictingInformationFiltering. Inthisstep,weim-
toprepareitforhaystackconstruction. Tomitigatepoten-
plementasemi-automaticredactionprocesstodetectand
tial memorization issues—since these books are publicly
removesuchconflictinginformation. AsshowninFigure
available—weconstructhaystacksbyconcatenatingshort
1,thisprocesstakesthehaystacktext—alreadyfilteredfor
snippets. Specifically,weiterativelyandrandomlyselecta
distractors—along with questions from our needle set as
book,extractacontinuoussnippet(under250tokens),and
input. Assumingthemodelshouldinfercaseswithinshort
appendittothehaystackuntilitexceeds2Klines,resulting
contexts, we scan the input texts in smaller chunks.2 To
inhaystacksexceeding60Ktokens.Inallexperiments,each
identify potential answers within a chunk, we pair each
needleisplaced26timesatequalintervalsacrosstheevalu-
questionwiththechunkandinputthemintoaninstruction-
atedcontextlength. With5randomlygeneratedhaystacks,
tunedlanguagemodel,alongwithashortinstructionand
58 question-needle pairs, and 26 placements per context
few-shotexamples. Themodelrespondswitheither“N/A”
length, thissetupresultsin7,540testspercontextlength
(indicatingnorelevantinformationwasfound)oranexpla-
experiment.
nationidentifyingapossibleconflict. Flaggedexamplesare
manuallyreviewed3todeterminewhethertheidentifiedin-
4.2.Models
formationshouldberemoved. Ifnoconflictsarefound,the
textremainsunchanged. Thisprocessisrepeatedacrossall For the filtering process, we opted using Llama 3.3 70b
selectedhaystacksuntilnofurtherremovalsarenecessary. instructiontunedmodel(Meta,2024). Asacontroltest,for
eachquestion,weplaceitsneedlein100randomlyselected
2Withan800-characterstrideanda1000-characterchunksize
chunks to verify whether the model (1) understands the
( 250tokens).
↑ 3Allmanualreviews—inbothfilteringsteps—wereconducted filteringtaskand(2)isfamiliarwiththefactsandcapable
byoneoftheauthors. of inferring the answer. The model achieves a score of
4

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
Claimed Effective BaseScore
Models 1K 2K 4K 8K 16K 32K
Length Length ( 0.85:Thr.)
↓
GPT-4o 128K 8K 99.3(84.4) 98.1 98.0 95.7 89.2 81.6 69.7
Llama3.370B 128K 2K 97.3(82.7) 94.2 87.4 81.5 72.1 59.5 42.7
Llama3.1405B 128K 2K 94.7(80.5) 89.0 85.0 74.5 60.1 48.4 38.0
Llama3.170B 128K 2K 94.5(80.3) 91.0 81.8 71.2 62.7 51.8 43.2
Gemini1.5Pro 2M 2K 92.6(78.7) 86.4 82.7 75.4 63.9 55.5 48.2
Jamba1.5Mini 256K <1K 92.4(78.6) 76.3 74.1 70.8 62.2 52.7 43.6
CommandR+ 128K <1K 90.9(77.3) 77.0 73.5 66.3 39.5 21.3 7.4
MistralLarge2 128K 2K 87.9(74.7) 86.1 85.5 73.3 51.5 32.6 18.7
Claude3.5Sonnet 200K 4K 87.6(74.4) 85.4 84.0 77.6 61.7 45.7 29.8
Gemini1.5Flash 1M <1K 84.7(72.0) 68.6 61.6 51.0 44.4 35.5 28.6
GPT-4omini 128K <1K 84.9(72.2) 67.7 58.2 44.1 32.6 20.6 13.7
Llama3.18B 128K 1K 76.7(65.2) 65.7 54.4 44.1 31.9 22.6 14.2
Table3.NOLIMAbenchmarkresultsontheselectedmodels.FollowingHsiehetal.(2024),wereporttheeffectivelengthalongsidethe
claimedsupportedcontextlengthforeachmodel. However,wedefinetheeffectivelengthasthemaximumlengthatwhichthescore
remainsaboveathresholdsetat85%ofthemodel’sbasescore(showninparentheses).Scoresexceedingthisthresholdareunderlined.
Scoresthatarebelow50%ofthebasescoreareshadedin red.
99.8%inthistest, indicatingitsabilitytoeffectivelyflag duetoitsdifficultieswithgeneralizingoverlongcontexts.
conflictinginformationfromthehaystacks. Foreachquestion-needleexample,wecomputetheaverage
score over 5 haystacks, then take the maximum score of
For the evaluation process, we select five closed-source
thatexampleacrossthe250,500,and1Ktests. Thefinal
models: GPT-4o,GPT-4oMini(Hurstetal.,2024),Gemini
basescoreisobtainedbyaveragingthesemaximumscores
1.5Pro,Flash(Teametal.,2024a),andClaude3.5Sonnet
acrossallquestion-needleexamples. InspiredbyHsiehetal.
(Anthropic, 2024), along with seven open-weight Llama
(2024),wealsoreporttheeffectivelengthofeachmodel.
models: TheLlama3.xmodelfamily(3.18B,70B,405B,
WhiletheyusetheperformanceofLlama2modelata4K
and3.370B)(Dubeyetal.,2024;Meta,2024),MistralLarge
lengthasathreshold(85.6%), wedefinethethresholdas
(Mistral,2024),CommandR+(CohereForAI,2024),and
85%ofthebasescore. Thus,theeffectivelengthofamodel
Jamba1.5Mini(Teametal.,2024b). Allthesemodelsare
isthelargesttestedlengththatexceedsthisthreshold. Addi-
well-knownandwidelyusedinlong-contextsetups. Inour
tionally,someplotsshowthenormalizedscore,calculated
analysisonreasoning-basedpromptingandmodels,weeval-
bydividingtheaccuracyscorebythebasescore.
uateGPT-o1,GPT-o3Mini(OpenAIetal.,2024;OpenAI,
2025),andDeepSeek-R1Distill-Llama-70B(DeepSeek-AI
4.4.Results
et al., 2025). More details regarding model versions and
deploymentdetailsaredescribedinAppendixB. Table 3 presents the performance results of all NOLIMA
testsontheselectedmodels.Mostmodelsachievehighbase
4.3.EvaluationSetup&Metric scores,indicatingthatthedesignedneedlesetisrelatively
simple to answer in shorter contexts. Even models with
Duringinference,weuseatasktemplate(seeAppendixC)
basescoresexceeding90.0%exhibitasignificantlyshorter
that instructs the model to answer the question based on
effectivelengththantheirclaimedlengths,generallylimited
theprovidedtext. Sinceallquestionsseekthenameofthe
to 2K tokens, with GPT-4o being an exception. While
charactermentionedintheneedle,anyreturnedanswercon- ↑
GPT-4o demonstrates strong overall performance, it fails
tainingthecorrectnameisconsideredaccurate. Accuracy
to generalize effectively beyond 8K tokens. Out of the
isreportedastheproportionoftestswithcorrectanswers.
12models, 10exhibitperformanceat32Klengthsthatis
Modelsareevaluatedonalltasksovercontextlengthsof halforlessoftheirbasescores. Forcomparison,inother
250,500,1K,2K,4K,8K,16K,and32K.Totakeintoac- benchmarkswithsimilarsettings,suchasBABILong(QA1)
counthowmodelswouldperformonNOLIMAregardless (Kuratov et al., 2024) and RULER (Hsieh et al., 2024),
of long-context scenario, we control the difficulty of the Llama3.170Bachieveseffectivelengthsof16K4and32K,
taskbybyreportingabasescore. Evaluationsatcontext respectively. However,inNOLIMA,Llama3.170Bhasan
lengthsof250,500,and1Kareusedtocomputethebase effectivelengthofonly2Kandshowsasignificantdropin
score. These three are the shortest contexts. If a model performanceat32Klengths(42.7%vs. 94.3%basescore).
cansolvethetaskattheselengths,thenanydeteriorationof
4InBABILong,theeffectivelengthisalsobasedon85%ofthe
itsperformanceatgreaterlengthsisexpectedtobesolely
0Kbaseperformancethreshold
5

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
(a) FullSweep(One-hop) (b) FullSweep(Two-hop) (c) Last2K(One-hop) (d) Last2K(Two-hop)
Figure2.Thefullsweepplots(a&b)illustrateperformanceacrosstheentirecontextwindow.Theplotsforthelast2Ktokens(c&d)
depictperformancewhenneedleplacementsarealignedwithinthefinal2Ktokensforvariouscontextlengths.Thecolorshadingofeach
plotlinerepresentsthetestedcontextlength.Tominimizenoiseandhighlighttrendsmoreclearly,weincreasedthenumberofplacements
from26to51andappliedamovingaveragewithawindowsizeof12.
ModelssuchasClaude3.5Sonnet,Gemini1.5Flash,GPT- Each group of needles includes both a default and an in-
4omini,andLlama3.18Bmayhaveweakerbasescores, vertedtemplateandFigure3(b)showsthatinvertedexam-
but their effective lengths are calculated relative to these plesaremorechallengingtoanswer.Wearguethisdifficulty
scores. This reveals an interesting observation: a model arisesfromthemodel’scausalattentionmechanism,partic-
likeClaude3.5Sonnet,despitehavingalowerbasescore, ularlyinlongercontextswhereattentionsignalsweaken. In
mayunderperforminshortercontextsbutdemonstratebetter thedefaulttemplate,thequestionorparticularlyW ,can
q
lengthgeneralizationthanmodelswithhigherbasescores, linkdirectlytoW ,whichcouldcontaininformationabout
n
suchasLlama3.170BandLlama3.370B.Infact,Sonnet thecharacter’snamesincethenameappearsearlierinthese-
evenachieveshigherrawscoresin4K-tokenexperiments quence. Thisallowsthemodeltobacktraceeffectivelyfrom
comparedtosomehigher-base-scoremodels. W throughW tothecharacter. Intheinvertedtemplate,
q n
W maystillattendtoW ,butsincethefactisincomplete
Modelscalinggenerallyimprovesperformance,asseenin q n
(thecharacterhasn’tbeenstatedyet),themodelcannotuse
the progression from Llama 3.1 8B to 70B, Gemini 1.5
thatattentiontoresolvethequestion. Instead,itmustrely
Flash to Pro, or GPT-4o mini to GPT-4o. However, the
onweakersignalsencodedinthecharacter’snametoestab-
benefitsofscalingdiminishatlargerscales; forexample,
lish the link, which becomes harder with longer contexts
theperformancegapbetweenLlama3.170Band405Bis
duetodiminishingattentionstrength. Whilethesefindings
smaller(andsometimesworse)thanthatbetween8Band
shedlightonthechallenge,deepermechanisticanalysisis
70B. In general, “lite” models such as Gemini 1.5 Flash,
beyondthescopeofthispaperandrequiresfurtherstudy.
GPT-4o mini, and Llama 3.1 8B perform well in shorter
contexts(<1Ktokens)butfailtogeneralizeeffectivelyin
longercontexts.
4.4.1.LATENTHOPS&INVERSION
AsdiscussedinSection3,ourneedlesetalsoincludesexam-
plesrequiringtwo-hopassociativelinkingfromthequestion
keyword to the needle keyword. To evaluate the impact
onlengthgeneralization,Figure3(a)presentsthenormal-
izedperformanceoftwotop-performingmodelsonone-hop
andtwo-hoptasks. Itisevidentthat,forthesamecontext
lengths,questionsinvolvingtwo-hoplatentreasoningsteps
(a) One-hopvs.Two-hop (b) Defaultvs.Inverted
aremorechallengingthanthoserequiringone-hopreason-
ing. Notably, the performance gap between one-hop and
two-hoptaskswidenswithincreasingcontextlengths. GPT- Figure3.Impactof(a)numberofhopsand(b)inversiononnor-
4o demonstrates impressive generalization performance, malizedperformanceacrossGPT-4oandLlama3.370Bmodels.
handling both types of examples effectively even at con- Thereddottedlineindicatesthe0.85effectivethreshold.
textlengthsupto4K.
6

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
4.4.2.NEEDLEPLACEMENTDEPTHANALYSIS
A common evaluation across NIAH-based benchmarks
(Kamradt,2023)examinestheimpactofneedleplacement
within the context window. In Figure 2(a), we observe a
”lost-in-the-middle”effect(Liuetal.,2024)in32K,where
model performance dips when the needle appears in the
middleoflongercontexts.
Additionally,Figure2(b)revealsakeyphenomenon: longer
contexts in more complex (two-hop) examples dampens
theperformancedistributionoverthefullsweepdepending
ontheirlength. Invanillamulti-documentorNIAH-based
benchmarks(Kamradt,2023;Liuetal.,2024),modelsper-
formconsistentlywellwhentheneedle(orgolddocument)
appearsattheverybeginningorendofthecontextwindow,
withminimalimpactfromcontextlength. However,inNO-
LIMA,astaskcomplexityincreasesintwo-hopscenarios,
largercontextsizesshifttheentiretrendlinedownwardto-
wardzero,withperformancedecliningevenattheedgesof
thecontextwindow.
To further investigate this issue, we devise an alternative
setupthatfocusesonanalyzingthelast2Ktokensinstead
of sweeping across the full context. Therefore, we align
theplacementpositionsinthelast2Ktokensforallcontext
lengths(seeFigure4). Thismakesthatforacertaintoken
depth the only changing factor in each plotline would be
thecontextlength,whichinturnmeansthatthemodelhas
moretokensthatcanbeattendedto.
Based on the final 2K results in Figure 2(c), the one-hop
setupconfirmsourearlierobservationsfromthefull-sweep
plots. The“lost-in-the-middle”phenomenon—whereper-
formancedipstowardthecenterofthecontext—primarily
appearsinsimplertasks. Eachplotlinedropsasitmoves
towardthecenter,reflectingitsdependenceonplacement
position and the way the model encodes positional infor-
mation. In contrast, the two-hop scenario appears to be
Placement positions
2K Inactive haystack
4K
8K
Input haystack
2K
4K
8K
peewS
lluF
K2
tsaL
4K 8K 16K 32K
One-hop
-w/oCoT 90.3 84.1 73.2 56.2
-w/CoT 95.6 91.1 82.6 60.6
Increaserate 5.9% 8.3% 12.8% 7.8%
Two-hop
-w/oCoT 70.7 57.4 42.7 25.9
-w/CoT 82.4 70.1 56.7 34.3
Increaserate 16.5% 22.1% 32.7% 32.4%
Table4.ComparisonofChain-of-Thought(CoT)improvementsin
performanceforLlama3.370B,evaluatedonbothone-hopand
two-hoptests.
influenced more by attention limitations than by position
encodingalone. Figure2(d)revealsthat,ratherthandepth
exacerbatingperformancedrops,theplotlinesremainrela-
tivelystableoverthelast2Kpositions. However,context
lengthsignificantlyreducestheoverallperformancetrends
observedinthisrange. Llama3.xmodels,likemanyother
recent language models, features rotary position embed-
dings(RoPE)whichisarelativePE(Suetal.,2024). For
each token depth in Figure 2(d), as the relative distance
betweenquestionandfactremainsthesameregardlessof
contextlength,positionencodingdoesnotexplaintheper-
formance drop. Instead, the main limiting factor is the
increasedcontextlength: asthenumberoftokensgrows,
theattentionmechanismstrugglestoprocessinformation
effectively. Intheabsenceofstrongsurface-levelcues(e.g.,
literalmatches),locatingrelevantfactsbecomeschalleng-
ingforthemodel,regardlessoftheirpositionwithinlong
contexts.
4.4.3.COTPROMPTING
SinceNOLIMAexamplesrequireanassociativereasoning
betweentheneedleandquestionkeywordstoretrievethe
correctanswer,inthispartweevaluatewhenthemodelis
promptedtoreasoninaChain-of-Thought(CoT)style(Wei
etal.,2022)beforereturningafinalanswer(seeAppendix
Cformoredetails). InTable4,wepresenttheresultswhen
asked for CoT compared to asking directly for the final
answer. CoT prompting shows improvements over long-
context tests and it shows a higher rate of improvement
intwo-shot. Despitetheimprovements,thetasksseemto
remainchallenging. Forexample,two-hopexampleswith
CoTpromptingbarelyachievethescoresofone-hopexam-
pleswithoutCoTandcontinuetoperformpoorlyontexts
16Ktokensorlonger. ThechallengewithCoTprompting
isthatthequestionsinNOLIMAarestraightforward. They
Figure4.Needleplacementsinfullsweep(top)vs.last2Ktokens arementioningasingularcluetotheanswer,meaningthey
sweep (bottom): In the last 2K setup, placement positions are cannotbefurtherdecomposedintosimplersteps.Thislimits
alignedindifferentcontextlengths,unliketheproportion-based thebenefitsofCoTprompting. However,thedifficultylies
positioninginfullsweep. inreasoningthroughtheassociationbetweenthequestion
7

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
Base 8K 16K 32K
4K 8K 16K 32K
Score
Direct 98.3 98.5 98.5
Llama3.370b
One-hop 84.1 73.2 56.2
-w/oCoT 98.3 55.5 37.2 16.7 8.9
-w/LiteralMatch(MC) 98.7 97.4 93.1
-w/CoT 97.1 73.0 51.2 31.8 10.1
Two-hop 57.4 42.7 25.9
Reasoningmodels
-w/LiteralMatch(MC) 96.3 94.6 87.2
GPT-o1 99.9 92.0 78.0 60.1 31.1
GPT-o3Mini 98.8 52.8 36.9 25.5 18.9
DeepSeekR1-DL-70b 99.9 91.4 75.5 49.4 20.7 Table6.Resultsintwoliteralmatchsetups: directandmultiple
choice(MC)questions.Model:Llama3.370B
Table5.EvaluationresultsofNOLIMA-Hard:Scoresfallingbe-
low50%ofthebasescorearehighlightedin red.
scope. Thisdramaticallysimplifiesthetaskofidentifying
the correct answer, as the literal match serves as a direct
hint,reducingambiguityinthereasoningprocess.
andtheneedle, whichremainsasignificantchallengefor
themodel. DistractingLiteralMatches. Whileliteralmatchescould
serveascuesiftheyarepartoftherelevantfact,theycan
Toassesstheperformanceofreasoning-basedmodels(e.g.,
alsoactasdistractorsiftheyareirrelevanttotheanswer. In
GPT-o1)onNOLIMA,weselectedthe10mostchallenging
Section2,wenotedthatsomerelatedbenchmarksinclude
needle-questionpairsfromthe58available,basedonthe
similardocumentsinthecontextasdistractorstotestthe
resultssummarizedinTable3. Werefertothissubsetas
model’sabilitytodiscernthecorrectanswerfromirrelevant
NOLIMA-HardandpresenttheevaluationresultsinTable5.
ones. This setup creates matches between the query and
Whilereasoning-basedmodelsoutperformCoTprompting
bothrelevantandirrelevantdocumentsorfacts. Incontrast,
onLlama3.3,theystillfailtoachievefull-lengthgeneraliza-
tiononthissubset. Acrossallmodels,performancedrops
NOLIMAallowsustoexploreadifferentscenario: when
thecontextcontainsdistractingwordsoverlappingwiththe
belowthe50%markat32Kcontextlength. Notably,base
question,whiletherelevantfacthasminimaloverlapwith
scoresarenearlyperfect,demonstratingthesimplicityof
thequery. Weinsertadistractorsentenceintothehaystack
thetask—evenwithinthisdesignated“hard”subset. This
(details in Appendix D) containing W but entirely irrel-
means that even with intermediate reasoning steps, mod- q
evant to both the needle and the question’s intent. This
elsstillstruggletolinktheneedletothequestioninlong
setup poses a significant challenge, requiring the model
contextswithoutsurface-levelcues.
todisregardirrelevantliteraloverlapswhileidentifyinga
relevant fact with no meaningful overlap with the query.
4.4.4.ABLATIONSTUDY: LITERALMATCHEFFECT
AsshowninFigure5, suchdistractorshaveasubstantial
To examine the simplifying impact of literal matches on impact on degrading length generalization. GPT-4o now
results,wedefinetwonewsetsoftests: (1)Direct: ques- demonstratesaneffectivelengthofjust1K,whileLlama3.3
tionsthatexplicitlyaskaboutthefactstatedintheneedle 70Bperformsevenworse. Whileaddingdistractorsslightly
bystatingW n inthequestion,resemblingavanillaNIAH lowersbasescores(GPT-4o: 93.8, Llama3.370B:84.4),
evaluation (Kamradt, 2023). (2) Multiple Choice (MC): the normalized plots still clearly illustrate a performance
questionsthatmaintaintherequiredlatentassociativerea-
soning while incorporating literal matches. In this setup,
thequestion includesfour character namesas answerop-
tions—threefromthehaystackandonecorrectanswerfrom
theneedle.
Asexpected,Table6showsthatdirectexampleswithahigh
degreeofliteraloverlapbetweenthequestionandtheneedle
arestraightforwardforthemodeltoanswer,eveninlong
contexts,consistentwithpriorfindingsinRULER(Hsieh
etal.,2024). Additionally,literalmatchessignificantlyaid
themodelwhenthequestionsremainunchanged,andonly
themultiple-choiceformatisintroduced. Theinclusionof
literal matches in the multiple-choice setup provides sig-
nificantguidancetothemodel. Byofferingthecharacter Figure5.NormalizedperformancecomparisonacrossGPT-4oand
namesasansweroptions,includingthecorrectnamefrom Llama 3.3 70B models, with and without distractors. The red
theneedle,themodelcanfocusitssearchwithinasmaller dottedlinemarksthe0.85effectivethreshold.
8

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
dropatlongerlengths. Theseresultshighlightthechallenge WorkshoponIn-ContextLearning,2024. URLhttps:
ofresolvingqueriesincontextswhereirrelevantoverlaps //openreview.net/forum?id=goi7DFHlqS.
misleadthemodel,andtherelevantfactsharesnooverlap
Anthropic, A. Claude 3.5 sonnet model card addendum.
withthequestion.
Claude-3.5ModelCard,3,2024.
5.Conclusion Arora, S., Eyuboglu, S., Timalsina, A., Johnson, I., Poli,
M.,Zou,J.,Rudra,A.,andRe,C. Zoology: Measuring
NOLIMAprovidesachallengingbenchmarkforevaluating andimprovingrecallinefficientlanguagemodels. InThe
thereasoningcapabilitiesoflargelanguagemodelsinlong- TwelfthInternationalConferenceonLearningRepresen-
contextsettings. Byremovingliteraloverlapsbetweenques- tations, 2024. URL https://openreview.net/
tionsandrelevantinformation,thebenchmarktestsmodels’ forum?id=LY3ukUANko.
abilitytoinferandlinkinformationwithinextensiveirrel-
evantcontent. Ourfindingsshowthatevenstate-of-the-art Ba,J.,Hinton,G.E.,Mnih,V.,Leibo,J.Z.,andIonescu,C.
modelsstruggle,especiallyascontextlengthincreases,re- Usingfastweightstoattendtotherecentpast. Advances
vealingseriouslimitsintheirattentionmechanism. While inneuralinformationprocessingsystems,29,2016.
causalattentionshouldtheoreticallyaccessallpreviousto-
Bai,Y.,Lv,X.,Zhang,J.,Lyu,H.,Tang,J.,Huang,Z.,Du,
kens,modelsoftenrelyonsurface-levelcuesinlongercon-
Z.,Liu,X.,Zeng,A.,Hou,L.,Dong,Y.,Tang,J.,andLi,
texts. Thisvulnerabilitybecomesmorepronouncedwhen
J.LongBench:Abilingual,multitaskbenchmarkforlong
thecontextcontainsliteralmatchesthatfailtoconnectwith
context understanding. InKu, L.-W., Martins, A., and
thetrulyrelevantfact,causingmodelstooverlookthecor-
Srikumar,V.(eds.),Proceedingsofthe62ndAnnualMeet-
rect information and focus instead on superficial signals.
ingoftheAssociationforComputationalLinguistics(Vol-
WebelieveourfindingswithNOLIMAarelikelytoextend
ume1:LongPapers),pp.3119–3137,Bangkok,Thailand,
todownstreamapplications. Forinstance,insearchengines
August 2024. Association for Computational Linguis-
orRAGsystems,arelevantdocumentcontainingthecorrect
tics. doi: 10.18653/v1/2024.acl-long.172. URLhttps:
answer may have a lexical gap with the query. So, even
//aclanthology.org/2024.acl-long.172/.
ifsuchadocumentisretrievedalongsideothersthatlikely
havehigherlexicalsimilarity,languagemodelsmaystruggle Chang,Y.,Lo,K.,Goyal,T.,andIyyer,M. Booookscore: A
toextractthecorrectanswer,astheycanbecomedistracted systematicexplorationofbook-lengthsummarizationin
bythelexicaloverlapsinthoseotherdocuments. Thiswork theeraofLLMs.InTheTwelfthInternationalConference
highlightstheneedforbenchmarksthatgobeyondsurface- on Learning Representations, 2024. URL https://
level retrieval to assess deeper reasoning. NOLIMA sets openreview.net/forum?id=7Ttk3RzDeu.
anewstandardforevaluatinglong-contextcomprehension
Chen, S., Wong, S., Chen, L., and Tian, Y. Extending
andemphasizestheimportanceofdevelopingapproaches
contextwindowoflargelanguagemodelsviapositional
capableofhandlingcomplexreasoninginlongcontexts.
interpolation. arXivpreprintarXiv:2306.15595,2023.
ImpactStatement CohereForAI. c4ai-command-r-plus-08-2024,2024. URL
https://huggingface.co/CohereForAI/
Thispaperpresentsworkaimedatadvancingthefieldof c4ai-command-r-plus-08-2024.
long-contextlanguagemodelingbyevaluatingandanalyz-
ingthemostcommonlyusedLLMs. Therearemanypoten- DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J.,
tialsocietalconsequencesofourwork,nonewhichwefeel Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X.,
mustbespecificallyhighlightedhere. et al. Deepseek-r1: Incentivizing reasoning capabil-
ity in llms via reinforcement learning. arXiv preprint
arXiv:2501.12948,2025.
Acknowledgments
Dong, Z., Tang, T., Li, J., Zhao, W. X., and Wen, J.-R.
WethankAbdullatifKo¨ksal,LeonieWeissweiler,andAmir
BAMBOO:Acomprehensivebenchmarkforevaluating
HosseinKargaranfortheirvaluablefeedbackandsupport,
longtextmodelingcapacitiesoflargelanguagemodels.
particularlyintheearlystagesofthisproject.
InCalzolari,N.,Kan,M.-Y.,Hoste,V.,Lenci,A.,Sakti,
S., and Xue, N. (eds.), Proceedings of the 2024 Joint
References InternationalConferenceonComputationalLinguistics,
Language Resources and Evaluation (LREC-COLING
Agarwal,R.,Singh,A.,Zhang,L.M.,Bohnet,B.,Rosias,
2024),pp.2086–2099,Torino,Italia,May2024.ELRA
L., Chan, S. C., Zhang, B., Faust, A., and Larochelle,
and ICCL. URL https://aclanthology.org/
H. Many-shot in-context learning. In ICML 2024
2024.lrec-main.188/.
9

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., and Iwa-
A.,Letman,A.,Mathur,A.,Schelten,A.,Yang,A.,Fan, sawa, Y. Large language models are zero-shot reason-
A., et al. The llama 3 herd of models. arXiv preprint ers. InOh,A.H.,Agarwal,A.,Belgrave,D.,andCho,
arXiv:2407.21783,2024. K. (eds.), Advances in Neural Information Processing
Systems,2022. URLhttps://openreview.net/
Goldman, O., Jacovi, A., Slobodkin, A., Maimon, A.,
forum?id=e2TBb5y0yFf.
Dagan, I., and Tsarfaty, R. Is it really long con-
text if all you need is retrieval? towards gen- Kuratov,Y.,Bulatov,A.,Anokhin,P.,Rodkin,I.,Sorokin,
uinely difficult long context NLP. In Al-Onaizan, Y., D. I., Sorokin, A., and Burtsev, M. BABILong: Test-
Bansal, M., and Chen, Y.-N. (eds.), Proceedings of ingthelimitsofLLMswithlongcontextreasoning-in-
the 2024 Conference on Empirical Methods in Natu- a-haystack. In The Thirty-eight Conference on Neural
ral Language Processing, pp. 16576–16586, Miami, Information Processing Systems Datasets and Bench-
Florida,USA,November2024.AssociationforCompu- marks Track, 2024. URL https://openreview.
tationalLinguistics. doi: 10.18653/v1/2024.emnlp-main. net/forum?id=u7m2CG84BQ.
924. URL https://aclanthology.org/2024.
Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu,
emnlp-main.924/.
C.H.,Gonzalez,J.E.,Zhang,H.,andStoica,I. Efficient
Graves, A., Wayne, G., and Danihelka, I. Neural turing memorymanagementforlargelanguagemodelserving
machines,2014. URLhttps://arxiv.org/abs/ withpagedattention. InProceedingsoftheACMSIGOPS
1410.5401. 29thSymposiumonOperatingSystemsPrinciples,2023.
Hengle,A.,Bajpai,P.,Dan,S.,andChakraborty,T. Multi- Lee, J., Chen, A., Dai, Z., Dua, D., Sachan, D. S., Bo-
lingualneedleinahaystack: Investigatinglong-context ratko,M.,Luan,Y.,Arnold,S.M.R.,Perot,V.,Dalmia,
behaviorofmultilinguallargelanguagemodels. arXiv S., Hu, H., Lin, X., Pasupat, P., Amini, A., Cole, J.R.,
preprintarXiv:2408.10151,2024. Riedel, S., Naim, I., Chang, M.-W., and Guu, K. Can
long-contextlanguagemodelssubsumeretrieval,rag,sql,
Hsieh,C.-P.,Sun,S.,Kriman,S.,Acharya,S.,Rekesh,D., andmore?,2024. URLhttps://arxiv.org/abs/
Jia,F.,andGinsburg,B. RULER:What’stherealcontext 2406.13121.
size of your long-context language models? In First
ConferenceonLanguageModeling,2024. URLhttps: Levy,M.,Jacoby,A.,andGoldberg,Y. Sametask,more
//openreview.net/forum?id=kIoBbc76Sy. tokens:theimpactofinputlengthonthereasoningperfor-
manceoflargelanguagemodels. InKu,L.-W.,Martins,
Hurst,A.,Lerer,A.,Goucher,A.P.,Perelman,A.,Ramesh, A., and Srikumar, V. (eds.), Proceedings of the 62nd
A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A., Annual Meeting of the Association for Computational
Radford,A.,etal. Gpt-4osystemcard. arXivpreprint Linguistics(Volume1: LongPapers),pp.15339–15353,
arXiv:2410.21276,2024. Bangkok,Thailand,August2024.AssociationforCom-
putationalLinguistics. doi: 10.18653/v1/2024.acl-long.
Izacard,G.,Caron,M.,Hosseini,L.,Riedel,S.,Bojanowski,
818. URL https://aclanthology.org/2024.
P., Joulin, A., and Grave, E. Unsupervised dense in-
acl-long.818/.
formation retrieval with contrastive learning. Transac-
tionsonMachineLearningResearch,2022. ISSN2835- Li, M., Zhang, S., Liu, Y., and Chen, K. Needlebench:
8856. URLhttps://openreview.net/forum? Canllmsdoretrievalandreasoningin1millioncontext
id=jKN1pXi7b0. window?, 2024. URL https://arxiv.org/abs/
2407.11963.
Jiang,B.,Xie,Y.,Hao,Z.,Wang,X.,Mallick,T.,Su,W.J.,
Taylor,C.J.,andRoth,D. Apeekintotokenbias: Large Lin, C.-Y. ROUGE: A package for automatic evalua-
language models are not yet genuine reasoners. In Al- tion of summaries. In Text Summarization Branches
Onaizan,Y.,Bansal,M.,andChen,Y.-N.(eds.),Proceed- Out, pp. 74–81, Barcelona, Spain, July 2004. Asso-
ings of the 2024 Conference on Empirical Methods in ciation for Computational Linguistics. URL https:
Natural Language Processing, pp. 4722–4756, Miami, //aclanthology.org/W04-1013/.
Florida,USA,November2024.AssociationforCompu-
Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua,
tationalLinguistics. doi: 10.18653/v1/2024.emnlp-main.
M.,Petroni,F.,andLiang,P. Lostinthemiddle: How
272. URL https://aclanthology.org/2024.
language models use long contexts. Transactions of
emnlp-main.272/.
theAssociationforComputationalLinguistics,12:157–
Kamradt, G. Needle in a haystack-pressure testing llms. 173, 2024. doi: 10.1162/tacl a 00638. URL https:
GithubRepository,pp. 28,2023. //aclanthology.org/2024.tacl-1.9/.
10

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
Maharana,A.,Lee,D.-H.,Tulyakov,S.,Bansal,M.,Barbi- Su, J., Ahmed, M., Lu, Y., Pan, S., Bo, W., and Liu, Y.
eri,F.,andFang,Y. Evaluatingverylong-termconver- Roformer: Enhanced transformer with rotary position
sationalmemoryofLLMagents. InKu,L.-W.,Martins, embedding. Neurocomputing,568:127063,2024.
A., and Srikumar, V. (eds.), Proceedings of the 62nd
Team, G., Georgiev, P., Lei, V. I., Burnell, R., Bai, L.,
Annual Meeting of the Association for Computational
Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S.,
Linguistics(Volume1: LongPapers),pp.13851–13870,
et al. Gemini 1.5: Unlocking multimodal understand-
Bangkok,Thailand,August2024.AssociationforCom-
ingacrossmillionsoftokensofcontext. arXivpreprint
putationalLinguistics. doi: 10.18653/v1/2024.acl-long.
747. URL https://aclanthology.org/2024. arXiv:2403.05530,2024a.
acl-long.747/.
Team,J.,Lenz,B.,Arazi,A.,Bergman,A.,Manevich,A.,
Peleg,B.,Aviram,B.,Almagor,C.,Fridman,C.,Padnos,
Meta, A. Llama 3.3 model card. 2024. URL
D.,etal. Jamba-1.5: Hybridtransformer-mambamodels
https://github.com/meta-llama/
atscale. arXivpreprintarXiv:2408.12570,2024b.
llama-models/blob/main/models/llama3_
3/MODEL_CARD.md.
Wang, M., Chen, L., Cheng, F., Liao, S., Zhang, X., Wu,
B., Yu, H., Xu, N., Zhang, L., Luo, R., Li, Y., Yang,
Mistral, A. Mistral large 2. Mistral Large 2 Blog-
M., Huang, F., and Li, Y. Leave no document behind:
post, 2024. URL https://mistral.ai/news/
Benchmarkinglong-contextLLMswithextendedmulti-
mistral-large-2407/.
docQA. InAl-Onaizan,Y.,Bansal,M.,andChen,Y.-N.
(eds.), Proceedings of the 2024 Conference on Empiri-
Mohtashami, A. and Jaggi, M. Random-access infi-
calMethodsinNaturalLanguageProcessing,pp.5627–
nite context length for transformers. In Thirty-seventh
5646,Miami,Florida,USA,November2024.Association
ConferenceonNeuralInformationProcessingSystems,
forComputationalLinguistics. doi: 10.18653/v1/2024.
2023. URLhttps://openreview.net/forum?
emnlp-main.322. URL https://aclanthology.
id=7eHn64wOVy.
org/2024.emnlp-main.322/.
Navigli,R.,Conia,S.,andRoss,B.Biasesinlargelanguage Wei,J.,Wang,X.,Schuurmans,D.,Bosma,M.,ichter,b.,
models: Origins,inventory,anddiscussion. J.Dataand Xia,F.,Chi,E.,Le,Q.V.,andZhou,D. Chain-of-thought
InformationQuality,15(2),June2023. ISSN1936-1955. promptingelicitsreasoninginlargelanguagemodels. In
doi: 10.1145/3597307. URLhttps://doi.org/10. Koyejo, S., Mohamed, S., Agarwal, A., Belgrave, D.,
1145/3597307.
Cho,K.,andOh,A.(eds.),AdvancesinNeuralInforma-
tionProcessingSystems,volume35,pp.24824–24837.
Olsson,C.,Elhage,N.,Nanda,N.,Joseph,N.,DasSarma,
CurranAssociates,Inc.,2022.
N., Henighan, T., Mann, B., Askell, A., Bai, Y., Chen,
A.,Conerly,T.,Drain,D.,Ganguli,D.,Hatfield-Dodds, Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue,
Z.,Hernandez,D.,Johnston,S.,Jones,A.,Kernion,J., C., Moi, A., Cistac, P., Rault, T., Louf, R., Funtow-
Lovitt,L.,Ndousse,K.,Amodei,D.,Brown,T.,Clark, icz, M., Davison, J., Shleifer, S., von Platen, P., Ma,
J.,Kaplan,J.,McCandlish,S.,andOlah,C. In-context C., Jernite, Y., Plu, J., Xu, C., LeScao, T., Gugger, S.,
learning and induction heads, 2022. URL https:// Drame, M., Lhoest, Q., and Rush, A. Transformers:
arxiv.org/abs/2209.11895. State-of-the-artnaturallanguageprocessing. InLiu,Q.
andSchlangen,D.(eds.),Proceedingsofthe2020Confer-
OpenAI. Openai o3-mini system card. 2025. enceonEmpiricalMethodsinNaturalLanguageProcess-
URL https://openai.com/index/ ing: SystemDemonstrations,pp.38–45,Online,October
o3-mini-system-card/. 2020. Association for Computational Linguistics. doi:
10.18653/v1/2020.emnlp-demos.6. URL https://
OpenAI,:Jaech,A.,Kalai,A.,Lerer,A.,Richardson,A., aclanthology.org/2020.emnlp-demos.6/.
El-Kishky,A.,Low,A.,Helyar,A.,Madry,A.,Beutel,A.,
Carney,A.,etal. Openaio1systemcard. arXivpreprint Xiong, W., Liu, J., Molybog, I., Zhang, H., Bhargava, P.,
arXiv:2412.16720,2024. Hou, R., Martin, L., Rungta, R., Sankararaman, K. A.,
Oguz, B., Khabsa, M., Fang, H., Mehdad, Y., Narang,
Peng,B.,Quesnelle,J.,Fan,H.,andShippole,E. YaRN:Ef- S., Malik, K., Fan, A., Bhosale, S., Edunov, S., Lewis,
ficientcontextwindowextensionoflargelanguagemod- M., Wang, S., and Ma, H. Effective long-context scal-
els. InTheTwelfthInternationalConferenceonLearning ingoffoundationmodels. InDuh,K.,Gomez,H.,and
Representations,2024. URLhttps://openreview. Bethard,S.(eds.),Proceedingsofthe2024Conference
net/forum?id=wHBfxhZu1u. of the North American Chapter of the Association for
11

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
ComputationalLinguistics: HumanLanguageTechnolo-
gies (Volume 1: Long Papers), pp. 4643–4663, Mex-
ico City, Mexico, June 2024. Association for Compu-
tationalLinguistics. doi: 10.18653/v1/2024.naacl-long.
260. URL https://aclanthology.org/2024.
naacl-long.260/.
Yen,H.,Gao,T.,Hou,M.,Ding,K.,Fleischer,D.,Izsak,P.,
Wasserblat,M.,andChen,D. Helmet: Howtoevaluate
long-contextlanguagemodelseffectivelyandthoroughly.
arXivpreprintarXiv:2410.02694,2024.
Zhang,X.,Chen,Y.,Hu,S.,Xu,Z.,Chen,J.,Hao,M.K.,
Han, X., Thai, Z. L., Wang, S., Liu, Z., and Sun, M.
bench:Extendinglongcontextevaluationbeyond100k
↓
tokens, 2024. URL https://arxiv.org/abs/
2402.13718.
12

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
A.NeedleSetDesign&Considerations
InTable7,wedemonstratethefullneedlesetthatweuseinNOLIMA. Indesigningtheneedletemplates,therearemultiple
considerationsinvolved. First,alltemplatesintheneedlesetbeginwithasmallintroductoryphraseoratleastoneword
(e.g.,“Actually,”“In2013,”)todistinguishthemselvesfromtheprecedingcontext. Thisensuresthattheneedle’skeywordor
characterisnotinadvertentlylinkedtothepriorcontext. Sinceanewlineisappendedattheendofeachneedle,thisissueis
mitigatedifthekeywordorcharacterappearsattheendoftheneedle.
Question Needles KeywordTypes
Def. There was [CHAR] who was an engineer liv- W n Countries,cities,states
WhichcharacterhasbeentoW q?
Inv.
i
T
n
h
g
e
i
r
n
e
W
w
n
a
.
s an engineer living in W n, named W q Countries,cities,states
[CHAR].
WhichcharacterhasbeentoW q? D
In
e
v
f
.
. A
W
c
n
tu
i
a
s
ll
n
y
e
,
x
[
t
C
t
H
o
A
w
R
he
]
r
l
e
iv
[
e
C
s
H
n
A
ex
R
t
]
to
liv
th
e
e
s.
W n. W
W
n
q
B
C
u
o
i
u
l
n
d
t
i
r
n
i
g
es
s
,
&
cit
L
ie
a
s
n
,
d
s
m
ta
a
te
rk
s
s
Def. In2013,afterwaitinginlineforhours,[CHAR] W n Buildings&Landmarks
WhichcharacterhasbeentoW q?
Inv.
fi
In
n
2
al
0
l
1
y
3
s
,
a
t
w
he
t
o
h
r
e
ig
o
i
r
n
i
a
g
l
in
W
al
n
W
pa
n
in
p
t
a
in
in
g
t
w
in
a
g
s
u
s
p
ee
c
n
lo
u
s
p
e
c
.
lose W q Countries,cities,states
by[CHAR],finally,afterwaitinginlineforhours.
Def. A message came in from [CHAR] saying, “I’m W n Dietary restriction
WhichcharactercannotdrinkW q?
Inv.
W
A
n
m
”
e
a
s
n
s
d
ag
n
e
oth
c
i
a
n
m
g
e
m
i
o
n
re.
saying, “I’m W n,” from W q
(
D
e
r
.g
in
.,
k
l
s
ac
&
to
B
se
ev
in
er
to
ag
le
e
r
s
ant)
[CHAR].
Def. Then[CHAR]mentionedthathehasbeenW nfor W n Dietary restriction
WhichcharactercannoteatW q? years. (e.g.,vegan)
Inv. TherewasaW nguest,named[CHAR]. W q Foods
Table7.Ourproposedneedlesettemplatesin NOLIMA. Theplaceholders[CHAR],W q, andW n representtherandomlyselected
character(alsotheanswer),thequerykeyword,andtheneedlekeyword,respectively.Def.:defaultorder.Inv.:invertedorder.
Anotherconsiderationisthattheneedlekeywordshouldbeuniquelyassociatedwiththequerykeyword. Forinstance,inthe
followingsentence:
TherewasanengineerlivinginCambridge,namedYuki.
Althoughtheterm”Cambridge”iscommonlyassociatedwiththe”UnitedKingdom,”itisnotuniquelyso;itcouldalsorefer
tocitiesintheUnitedStates,Canada,orothercountries. Additionally,weaimtoavoidrelyingonlanguage-specificmarkers.
Manycitieshavedistinctiveelementsintheirnames,suchasorthographicfeatures,morphologicalstructures,orcultural
namingconventions,thathintattheirlinguisticorgeographicorigins. Byminimizingtheinfluenceofsuchmarkers,the
needledesignensuresamorerigorousevaluationofthemodel’sabilitytomakemeaningfulconnectionsbasedonlearned
knowledgeratherthansurface-levellinguisticcues. Foreachtemplate,wemanuallycurated2-6keywordpairs,resultingin
atotalof28keywordpairs. Takingintoaccounttheorderoffactstatements,thisgenerates58needle-questionpairs.
B.Models
InTable8,welistallthemodelsselectedforevaluation. ModelsthatareopenweightsweredeployedusingthevLLM
library(Kwonetal.,2023),withweightsobtainedfromHuggingFace(Wolfetal.,2020).
C.TaskPromptTemplates&InferenceSettings
InTable9,wepresentthetaskpromptsusedacrossallevaluations. Whilewedonotemploythecommonlyused”Let’s
thinkstepbystep”promptintheChain-of-Thought(CoT)setup(Kojimaetal.,2022),ourpromptencouragesthemodel
to elaborate and expand its reasoning sufficiently before producing a final answer. To manage the extensive testing
scope—7,540 tests per context length—we limit reasoning to three sentences or a maximum of 192 generated tokens.
Inthe CoTsetup, a testisconsidered successfulif thefinal answer (onthe newline) includesthecorrect answer. This
differswiththenon-CoTsetup,wheresuccessisdeterminedbasedonwhetherthecorrectanswerispresentwithinthe
13

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
Model ContextLength OpenWeights? ModelRevision
GPT-4o 128K No gpt-4o-2024-11-20
GPT-4omini 128K No gpt-4o-mini-20240718
Llama3.370B 128K Yes meta-llama/Llama-3.3-70B-Instruct
Llama3.1405B 128K Yes meta-llama/Llama-3.1-405B-Instruct
Llama3.170B 128K Yes meta-llama/Llama-3.1-70B-Instruct
Llama3.18B 128K Yes meta-llama/Llama-3.1-8B-Instruct
Gemini1.5Pro 2M No gemini-1.5-pro-002
Gemini1.5Flash 1M No gemini-1.5-flash-002
Claude3.5Sonnet 200K No anthropic.claude-3-5-sonnet-20241022-v2
Jamba1.5Mini 256K Yes ai21labs/AI21-Jamba-1.5-Mini
CommandR+ 128K Yes CohereForAI/c4ai-command-r-plus-08-2024
MistralLarge2 128K Yes mistralai/Mistral-Large-Instruct-2411
Reasoning-basedmodels
GPT-o1 128K No gpt-o1-2024-12-17
GPT-o3Mini 128K No gpt-o3-mini-2025-01-31
DeepSeekR1-DL-70b 128K Yes deepseek-ai/DeepSeek-R1-Distill-Llama-70B
Table8. Detailsoftheselectedmodelsusedforevaluation.
generatedoutput. Forallstandardinstruction-tunedmodels,weusegreedydecodingduringgeneration. Forreasoning-based
models,weutilizethedefaultsamplingdecodingmechanismforGPT-o1andGPT-o3Mini,whileR1-basedmodelsemploy
top-Psamplingwithp=0.95andatemperatureof0.6. Inaddition,wecapthemaximumnumberofgeneratedtokensin
reasoning-basedmodelsat1536tokens,includingbothreasoningandoutputtokens. Inallmodels,weapplyeachmodel’s
instruction-tunedchattemplates.
Mode PromptTemplate
Youwillansweraquestionbasedonthefollowingbooksnippet:
haystackw/needle
{ }
Usetheinformationprovidedinthebooksnippettoanswerthequestion.Your
w/oCoT answershouldbeshortandbasedoneitherexplicitlystatedfactsorstrong,
logicalinferences.
Question: question
{ }
Returnonlythefinalanswerwithnoadditionalexplanationorreasoning.
Youwillansweraquestionbasedonthefollowingbooksnippet:
haystackw/needle
{ }
Usetheinformationprovidedinthebooksnippettoanswerthequestion.
w/CoT Beawarethatsomedetailsmaynotbestateddirectly,andyoumayneed
toINFERtheanswerbasedonthegiveninformation.Beginwithabrief
explanationofyourreasoninginNOMORETHANTHREE(3)sentences.
Then,returnthefinalansweronanewline.
Question: question
{ }
Table9. Detailsofprompttemplatesutilizedinourevaluation.
D.DistractorDesign
ToconstructandintegratethedistractorsentencesmentionedinSection4.4.4,wedevisedtwotemplates,applieduniformly
acrossallneedle-questionpairs. DependingontheW ,weuseoneofthefollowingtemplates:
q
14

NOLIMA:Long-ContextEvaluationBeyondLiteralMatching
TherewasanarticleaboutW inthedailynewspaper.
q
or
TherewasaphotoofW inthedailynewspaper.
q
SomeinstancesofW maynaturallyincludeanarticle(e.g.,”a”or”an”),makingthembettersuitedforthesecondtemplate,
q
whileothersfitthefirst. Regardlessofthechoice,thetemplatesaredesignedtoremainneutralandunrelatedtotheintentof
thequestionorthefactstatedbyanyneedle.
Tominimizeinterferencewiththeneedle,werandomlyplacethedistractorsentencewhileensuringatokendistanceofat
least20%ofthecontextlength. Forexample,ina1K-tokentest,thedistractormustbeatleast200tokensawayfromthe
needle. Additionally,toavoidanyadvantagefromproximitytothebeginningorendofthecontext(whichmaygainextra
attention),werestrictplacementtobetweenthe20%and80%marksofthecontextlength. Together,thesetwoconstraints
leaveaspanof40%-60%ofthecontextlengthavailableforrandomplacementofthedistractorsentence.
15
