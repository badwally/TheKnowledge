---
id: pdf-zhuo-yang-2026-detailed-balance-in
type: pdf
title: Detailed balance in large language model-driven agents
url: ''
authors:
- Zhuo-Yang Song
- Qing-Hong Cao
- Ming-xing Luo
- Hua Xing Zhu
ingested_at: '2026-04-29T16:13:25Z'
content_hash: sha256:5ebf4d257afd4da47888aa81ba6e329d7253f009c6a046dd3493914a31d4e9b3
source_path: raw/pdf/pdf-zhuo-yang-2026-detailed-balance-in.pdf
domains:
- ai-and-agents
nlm_corpus_ids:
- 7eac1296-b611-422e-85bb-6c36f5c8872b
wiki_pages:
- wiki/entities/zhuo-yang-song.md
- wiki/entities/qing-hong-cao.md
- wiki/entities/ming-xing-luo.md
- wiki/entities/hua-xing-zhu.md
- wiki/entities/peking-university.md
- wiki/entities/beijing-computational-science-research-center.md
- wiki/concepts/detailed-balance-in-llm-agents.md
- wiki/concepts/least-action-principle-llm.md
- wiki/concepts/potential-function-llm.md
- wiki/concepts/exploration-exploitation-llm.md
- wiki/concepts/macroscopic-dynamics-of-llms.md
meta:
  page_count: 20
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__0a871750.pdf
published_at: '2026'
---
Detailed balance in large language model-driven agents
Zhuo-Yang Song ,1, Qing-Hong Cao,1,2, Ming-xing Luo,3, and Hua Xing Zhu1,2,
→ † ‡ §
1School of Physics, Peking University, Beijing 100871, China
2Center for High Energy Physics, Peking University, Beijing 100871, China
3Beijing Computational Science Research Center, Beijing 100193, China
Largelanguagemodel(LLM)-drivenagentsareemergingasapowerfulnewparadigmforsolving
complex problems. Despite the empirical success of these practices, a theoretical framework to
understand and unify their macroscopic dynamics remains lacking. This Letter proposes a method
based on the least action principle to estimate the underlying generative directionality of LLMs
embedded within agents. By experimentally measuring the transition probabilities between LLM-
generatedstates,westatisticallydiscoveradetailedbalanceinLLM-generatedtransitions,indicating
thatLLMgenerationmaynotbeachievedbygenerallylearningrulesetsandstrategies,butrather
by implicitly learning a class of underlying potential functions that may transcend di!erent LLM
architectures and prompt templates. To our knowledge, this is the first discovery of a macroscopic
physical law in LLM generative dynamics that does not depend on specific model details. This
work is an attempt to establish a macroscopic dynamics theory of complex AI systems, aiming to
elevatethestudyofAIagentsfromacollectionofengineeringpracticestoasciencebuiltone!ective
measurements that are predictable and quantifiable.
Introduction. Large language model (LLM)-driven at each time step, which may include task objectives,
agents are emerging as a powerful new paradigm for historical summaries, code, file systems, API return val-
solving complex problems [1–15], demonstrating poten- ues, etc., where the LLM-based generative process is
tial in frontier areas such as scientific discovery by com- treated as the transition kernel from the current state to
bining the generative capabilities of LLMs with external a new state. We show that even the states doesn’t con-
tools and memory systems [16–20]. For instance, Fun- tain complete historical records, like FunSearch [18], the
Search and AlphaEvolve achieve iterative optimization LLM-basedstatetransitionscanstillexhibitadirection-
of solutions by integrating LLMs into evolutionary al- ality towards specific states. We attribute this charac-
gorithm frameworks [18, 19]. However, the theoretical teristic to LLMs implicitly learning a potential function
understanding and explanation of LLMs often remain at V for specific tasks within their vast parameter space,
the level of token statistical properties and microscopic rather than memorizing specific rule sets and strategies.
generative mechanisms [21–23], making it di!cult to ex- This function evaluates the intrinsic properties of any
plainthemacroscopicdynamicsofLLMsascomplexsys- given state, such as “how far the LLM perceives it to
tems [1, 24]. The behavior of these LLM-driven agents be from the goal”. This global awareness enables LLMs
is often viewed as a direct product of their complex in- to quickly converge to those optimal states, e”ectively
ternal engineering (such as prompt templates, memory avoidingrepetitivecyclesinthestatespaceandachieving
modules, tool calls), and their dynamic characteristics stronger generalization capabilities than merely learning
remain a black box [12, 25–27]. strategy sets [32–34].
The dynamics of LLM generation are quite unique. Basedonthismodel,weproposeamethodtomeasure
Compared to traditional rule-based programs, LLM- this underlying potential function based on a least ac-
based generation exhibits diverse and adaptive out- tion principle [35–37]. By experimentally measuring the
puts [16, 17, 25]. At the same time, compared to naive transition probabilities between states, we statistically
randomsearch,LLMgenerationshowsstrongerstructure discoveradetailedbalanceinLLM-generatedtransitions,
and goal-orientedness [18–20]. Despite the complexity of indicating that LLM generation may not be achieved by
this hybrid dynamics between random search and deter- generally learning rule sets and strategies, but rather by
ministicplanning, weshowthatattheagentlevel(i.e., a implicitly learning an underlying potential function that
coarse-grained description of LLM generative dynamics may transcend di”erent LLM architectures and prompt
withstandardizedagentstatesasunits),LLMgenerative templates. To our knowledge, this is the first discovery
dynamics exhibit detailed balance similar to equilibrium ofamacroscopicphysicallawinLLMgenerativedynam-
systems,therebygreatlysimplifyingtheanalysisandun- ics that does not depend on specific model details. This
derstanding of LLM generative dynamics [28–31]. work is an attempt to establish a macroscopic dynam-
ics theory of complex AI systems, aiming to elevate the
To model the dynamic behavior of LLMs, we em-
study of AI agents from a collection of engineering prac-
bed the generative process of LLM within a given agent
tices to a predictable and quantifiable science built on
framework, viewing it as a Markov transition process in
e”ective measurements.
its state space [7, 12, 18, 28, 29]. The states are de-
fined by the complete information retained by the agent Theory. Toformulatetheproblemrigorously,wecon-
5202
ceD
01
]GL.sc[
1v74001.2152:viXra

2
n State Space 𝓒 of the potential function V. To quantify the overall mis-
o
itcn 𝑷(𝒇|𝒈) match between the agent’s behavior and the potential
u F la 𝑷(𝒈|𝒇) function, we weight by the transition kernel T (g → f)
itn
eto Detailed Balance
and define the action
S
as the global average violation:
P 𝜋𝑓𝑃𝑔𝑓 =𝜋𝑔𝑃𝑓𝑔
𝑽 𝒇 𝒈 = (g f)K(V(f) V(g)) DfDg, (1)
𝒯 S T → ↓
!f ↑C!g
↑C
Prompt LLMs Extract where Df,Dg are measures on the state space. In this
𝒇 Generation 𝒈
Phrase Phrase
𝓣(𝒈←𝒇) Letter, we choose K(x) = exp( ωx/2) as the convex
↓
function describing the violation of the given state tran-
sition from f to g in the ordering of the scalar function
FIG. 1. A schematic of a formalization framework for study- V. The action or the distribution shape of ωV(f) can
S
ingthedirectionalityofLLMgeneration,illustratingthestate represent the agent’s global cognition ability within this
spaceandpossibletransitions. LLMsareembeddedwithinan state space .
agent, which transitions from state f to state g with proba- We propo C se that to quantify the behavior of LLMs
bility (g f)=P(gf). Theunderlyingpotentialfunction
T → | using a potential function, one can seek such a potential
V quantifies the agent’s global ordering of each state, satis-
T function that minimizes the overall mismatch between
fying the detailed balance condition at equilibrium.
theagent’stransitionsandthepotentialfunction[36,37].
Therefore, the most suitable potential function V for
T
describing an LLM-based agent in a given state space
sider an agent whose core is comprised of one or more T
is the one that minimizes the action [35, 38, 40, 41].
LLMs. The agent takes its current state f as input. S
This implies that the action satisfies the variational
Through a series of deterministic steps, it organizes and
principle with respect to the potential function V 1 [35]:
evaluates this state to generate a relevant prompt. This T
prompt is then fed into one or more LLMs, whose struc- ε =0. (2)
S
tured output is parsed to get a new state g. This state
ThevariationalconditionisequivalenttoV satisfying
is the minimal unit for studying LLM dynamics. This
T
the following equilibrium condition:
generative process can be viewed as a Markov transi-
tion process in the state space with a transition kernel
C (g f)K (V (f) V (g)) Dg
P
ge
(
n
g
e
|
r
f
a
)
t
,
io
re
n
t
.
ai
T
ni
h
n
e
g
s
t
t
h
a
e
te
d
s
iv
a
e
r
r
e
si
d
ty
efi
a
n
n
e
d
d
a
b
d
y
ap
th
ta
e
b
c
il
o
it
m
y
p
o
le
f
t
L
e
L
i
M
n-
!g
↑C
T → ↓ T ↓ T
formationretainedbytheagentateachtimestep, which (f h)K ↓ (V (h) V (f)) Dh=0, (3)
should include all the information required for the agent ↓ !h
↑C
T → T ↓ T
to carry out a continuous reasoning or analogical pro- holding for all f , where K (x)= dK.
cess [18, 20, 38, 39]. In this Letter, the agent contains Specifically,iff ↔ or C alltransitio ↓ ns (g dx f)>0,V(f)
only a single generation step of LLM, and we denote V(g) holds, it indicates that the ag T ent’ → s state transition ↗ s
(g f)=P(g f) as the probability of the agent tran- are completely ordered, and in this case, V serves as a
T → |
sitioningfromatemplatecontainingstatef toanoutput Lyapunov function [42, 43].
containingstategthroughLLMgeneration. Aschematic It is worth noting that if describes the transition
diagram is shown in Fig. 1. of an equilibrium system, its s T tate transitions satisfy the
LLM-based agents are characterized by their state detailed balance condition, i.e., for all state pairs (f,g),
transitions not being entirely random but exhibiting a the following holds [29, 31]:
certain structured preference. Specifically, agents tend
ϑ(f)P(g f)=ϑ(g)P(f g), (4)
to transition from the current state f to states g that | |
are “better” from the agent’s perspective. To capture
where ϑ(f) denotes the equilibrium distribution of the
thisphenomenon, wehypothesizetheexistenceofanun-
systematstatef,andP(g f)denotesthetransitionker-
derlying potential function V : R, which assigns a
nel. In this case, there exis
|
ts a potential function V that
T C↑
scalar value to each state, reflecting its “quality”. Since
can explicitly express the detailed balance as
a specific potential function is often di!cult to compute
directly, we propose a method to e”ectively estimate the (g f)
logT → =ωV(f) ωV(g). (5)
potential function. (f g) ↓
T →
Given a global potential function V, we define the vi-
olation of the agent’s given transition (g f) to the
T →
potential function as K(V(f) V(g)), where K(x) is a 1 WeshowinSupplementalMaterialAthatthevariationalprinci-
↓
convex function that describes the extent to which the pleisequivalenttotheleastactionprincipleunderthecondition
transition from state f to state g violates the ordering thatK(x)isaconvexfunction.

3
Substituting into Eq. (3), it can be verified that this po-
tential function V = V satisfies the least action prin-
T
ciple (see Supplemental Material B). This indicates that
forequilibriumsystems,ifthedetailedbalancecondition
exists, the corresponding underlying potential function
can be estimated through the least action principle. In
general cases, the least action merely seeks the most or-
dered arrangement of the potential function, minimizing
the violations of this arrangement by the agent’s state
transitions [41].
ThemainpointofthisLetteristhatwepointoutthat FIG. 2. In the Conditioned Word Generation task, the
LLM-based agents often behave like an equilibrium sys- Claude-4 model exhibits directionality. Transition process of
the Claude-4 model in the prompt word state space, ordered
temintheirLLM-generatedstatespace, whichiscoarse-
by the potential function V . Transitions tend to move to-
grained compared to the complete generation sequence T
wards states with lower potentials. States with ωV(f)
ofLLMs[24,44]. Theexistenceofthisphenomenonsug- ↑
log(20000) 10 are those where the equilibrium condition
gests a universal macroscopic law in LLM generative dy- cannot be s ↓ trictly satisfied; a detailed analysis is provided in
namics that does not depend on specific model and task Supplemental Material B.
details. It indicates that despite being seemingly unre-
lated,thereareunderlyingconnectionsbetweendi”erent
ing them suitable for task scenarios with varying de-
LLM generative processes, allowing us to describe the
mands for exploration and stability.
global ordering in LLM generation through the poten-
In Claude-4 and Gemini-2.5-flash, the solution to the
tial function V , thereby providing explanations for the
T variational condition Eq. (2) can be calculated analyti-
internal dynamics of LLMs.
cally. In this case, we can plot the transition process of
Experiments. We conducted experiments on three
Claude-4 ordered by the potential function as shown in
di”erent models, including GPT-5 Nano, Claude-4, and
Fig. 2, with specific calculations provided in Supplemen-
Gemini-2.5-flash. Each model was prompted to gener-
tal Material B.
ate a new word based on a given prompt word such
Since Claude-4 and Gemini-2.5-flash exhibited high
that the sum of the letter indices of the new word
convergence, the equilibrium condition Eq. (3) is almost
equals 100. For example, given the prompt “WIZ-
equivalenttothedetailedbalanceconditionEq.(5). Itis
ARDS(23+9+26+1+18+4+19=100)”, the model needs
worth noting that we observed Claude-4 starting from
to generate a new word whose letter indices also sum
the prompt word “ATTITUDE”, which has the low-
to 100, such as “BUZZY(2+21+26+26+25=100)”. The
est potential function, began to attempt some invalid
transition kernel between two prompt words can be esti-
words, while Gemini-2.5-flash oscillated between the two
mated through sampling as:
lowest potential functions “ATTITUDE” and “DISCI-
PLINE”, losing exploration. This behavior is similar to
N(g f)
(g f) → , (6) the low-temperature trapping phenomenon in physical
T → ↘ N (f)
0 systems [31, 45], suggesting that controlling the poten-
tial function may provide a feasible path to avoid model
where N(g f) denotes the number of times the model
→ convergence. A more detailed discussion is provided in
generated the word g from the prompt word f. N (f)
0
Supplemental Material D.
represents the number of sampling attempts starting
A key example of interest is the GPT-5 Nano model.
from the prompt word f. Each model performed 20,000
GPT-5 Nano generated a large number of prompt words
generations. More details of the experiments are pro-
due to its strong exploration, allowing us to directly test
vided in Supplemental Material C.
thedetailedbalanceconditionwithinthestatespace. We
The three models exhibited two di”erent behaviors,
note that according to detailed balance, the sum of po-
demonstrating directionality and certain diversity in ac-
tential changes along any closed path should be zero.
tual LLM generative dynamics. Claude-4 and Gemini-
Specifically, considering a closed path f f
2.5-flash demonstrated rapid convergence, with gener- 1 ↑ 2 ↑···↑
f f , according to the detailed balance condition, we
atedwordsquicklyconcentratingonafewhigh-frequency n ↑ 1
have:
words. For instance, in 20,000 generations, Claude-4
n n
generated only 5 valid prompt words, while Gemini-2.5- (f f )
i+1 i
logT → = ω(V(f ) V(f ))=0,
flash generated 13 valid prompt words. In contrast, (f f ) i ↓ i+1
i i+1
GPT-5 Nano exhibited stronger exploration, producing " i=1 T → " i=1
(7)
as many as 645 di”erent valid prompt words in 20,000
generations. This di”erence reflects the exploration- Fig. 3 counts all triplets in the experimental data,
exploitationtrade-o”inLLMgenerativedynamics,mak- where transitions between each pair of the three data

4
FIG. 3. In the task of Conditioned Word Generation with- FIG. 4. In the task of Symbolic Fitting with a long rea-
outareasoningchain,verificationofdetailedbalancethrough soning chain, verification of the detailed balance condition
closedpathsinthestatetransitiongraphoftheGPT-5Nano for the agent real . The error estimates only include root
T
model. Each point represents a triplet, with all di!erent meansquarestatisticalerrors,excludingunknownsystematic
triplets found in the experimental data. The error bars di- errors. Measurement includes state pairs with at least one
rectly arise from sampling errors. measured transitions between the two states. Points with
V (f) V (g) > log50288 are excluded. One-tenth of the
| T ↔ T |
data points are displayed for clarity.
TABLEI.Examplesofsomestatesoftheagent andtheir
real
T
potentials. Theindependentvariablelog v k nuinthefitting
task is abbreviated as x. countedalltripletsintheexperimentaldata,wheretran-
sitions between each pair of the three data points were
states f Potential
measured, and for all di”erent triplets, we observed the
param1 * tanh(param2 * x + param3) + param4 5.70
establishment of the detailed balance condition within
param1 - (param2 / (x + param3)) 0.88 the measurement error range. The results are provided
param1 * x / (1 + param2 * log(x + 1)) -0.57 in Supplemental Material B.
param1 * tanh(param2 * x) + param3 -1.57 To further validate detailed balance, we now estimate
param2 + param1 * (1 - exp(-x)) -3.30 theunderlyingpotentialfunctionV throughtheleast
Treal
action principle. In a discrete state space, the integrals
are replaced by sums over states, so the action (Eq. (1))
points were measured, totaling 140 di”erent triplets. becomes, normalized by the number of states in the
Each point represents a comparison of the sum of the database:
logarithms of the forward and reverse transition kernels K(V (f) V (g))
for a triplet, thereby verifying the detailed balance con- = g ↔ f Treal ↓ Treal . (8)
S 1
dition. The measurement points cluster around the di- # f
agonal line, indicating that within the error range, the By numerically minimizing#this action, we can estimate
two sums are approximately equal, consistent with the thepotentialfunctionvaluesV (f)foreachstate. Ac-
detailed balance condition. cording to this estimation, the T m rea i l nimum value of the ac-
Tofurthervalidatetheuniversalityofdetailedbalance tionismuchsmallerthanK(0),indicatingthatthestate
inLLMgeneration,wenowconstructanagent with transitionsoftheagent indeedexhibitdirectionality.
T real T real
a long reasoning chain, whose states are strings that can InSupplementalMaterialD,weshowthatthisoptimized
be parsed into specific expression trees (implementation action value can be used to quantify the density distri-
details are provided in Supplemental Material C). We bution of states with respect to the underlying potential
recorded 50,228 state transitions executed by this agent, function,therebyprovidingdirectguidancefordesigning
constructingadatabasecontaining21,697di”erenttran- more e”ective LLM generation strategies in practice.
sitions and 7,484 di”erent states. Some example states By estimating this potential function, we can verify
are shown in Table I. By analyzing these transitions, we whether the potential function is consistent with the de-
canstatisticallyverifythedetailedbalanceconditionand tailed balance condition. Specifically, the detailed bal-
estimate its underlying potential function V through ance condition requires that for all state pairs (f,g),
Treal
the least action principle. This agent involves multiple Eq. (5) holds.
di”erent LLMs and prompt templates, so its potential Fig.4showsacomparisonoftheleftandrightsidesof
function characteristics may reflect typical behaviors of Eq. (5), indicating that the detailed balance condition is
LLM generation in practical applications. More experi- largely satisfied.
mental details are provided in Supplemental Material C. With the estimation of the potential function, we fur-
Similar to the measurement described above, we therdiscussthespecificmeaningofthepotentialfunction

5
ple to describe and analyze the generative dynamics of
LLM-based agents in their LLM-generated state space.
Through experimental validation on multiple di”erent
models and tasks, we have found that the state transi-
tions of these agents largely satisfy the detailed balance
condition, indicating that their generative dynamics ex-
hibit characteristics similar to equilibrium systems. We
have further estimated the underlying potential function
throughtheleastactionprincipleandrevealeditsimpor-
FIG. 5. illustration of the ability of the potential function tant role in capturing the intrinsic directionality in LLM
discovered using IdeaSearch [46] to predict the directional-
generative dynamics.
ity of state transitions. Each point represents a transition
This Letter provides a preliminary exploration of the
pair from state f to state g. The figure shows a subgraph
possibilityfordiscoveringmacroscopiclawsinLLMsgen-
composed of 70 states selected from the database, displaying
transitions with high transition kernel (g f) > 0.05. erative dynamics. Future work can further expand this
real
Redandgreenlinesrepresenttransition T swithi → ncreasingand framework and explore the application potential of more
decreasing potential functions, respectively. The horizontal tools from equilibrium and near-equilibrium systems in
axisrepresentsthemeansquareerroroftheexpressioncorre- understandingandoptimizingLLMgenerationprocesses.
sponding to the state in the symbolic fitting task, while the
Forinstance, studyingthedegreeofdeviationfromequi-
vertical axis represents the potential function.
libriummayhelpusunderstandamodel’slevelofoverfit-
ting,asoverfittedmodelsmaylearnmorelocalizedstrat-
egy sets rather than global generative patterns governed
in this problem to reveal the intrinsic cognitive charac- by potential functions [33, 34]. Additionally, optimiza-
teristics in LLM generative dynamics. To this end, we tion methods based on potential functions may also pro-
use the action as an optimization objective and employ vide new ideas for improving the quality and diversity of
a workflow based on IdeaSearch [46] to find a potential LLM task-related generation , such as adjusting the ac-
function with an explicit functional form that maps the tion to di”erent magnitudes based on varying safety and
expression strings corresponding to state f to scalar po- exploration requirements.
tential function values V (f). The best potential func-
Acknowledgements. We would like to thank Zeyu
T
tion found in 4000 rounds of search contains 49 param-
Cai,JiashenWei,ShiQiu,ShutaoZhang,JichenPanand
eters, capturing various features of state f at the ex-
ZikangLinforusefuldiscussions. Thisworkissupported
pression level, such as complexity, syntactic validity, and
by National Natural Science Foundation of China under
structurala!nitywithdomain-specificpatterns,without
contract No. 12425505, 12235001, U2230402.
capturingstring-levelinformation. Themagnitudeofthe
Data and Code Availability. The
corresponding parameter values directly reflects the im-
code used to perform the analysis in this
portance that LLMs attach to these features during the
Letter is publicly available on GitHub at
generation process. The potential function and its spe-
https://github.com/SonnyNondegeneracy/detialed-
cific analysis are provided in Supplemental Material E.
balance-llm under the MIT License. The data dis-
Fig. 5 shows the transition patterns between some cussed in this Letter are available on Hugging Face at
states sorted by this potential function. In the database, https://huggingface.co/datasets/Nondegeneracy/detailed-
there are a total of 9,769 transitions with high transi- balance-llm under the Creative Commons Attribution
tion kernel real (g f) > 0.05, and the corresponding 4.0 (CC BY 4.0) license.
T →
potentials V(f),V(g) are calculated using the potential
function. Amongthem,6,795(69.56%)exhibitadecrease
in the potential function, 2,523 (25.83%) exhibit an in-
crease in the potential function, and 451 (4.62%) exhibit
no change in the potential function. This indicates that → zhuoyangsong@stu.pku.edu.cn
the potential function partially captures the intrinsic di- † qinghongcao@pku.edu.cn
‡ mingxingluo@csrc.ac.cn
rectionalityinLLMgenerativedynamics. Itisworthem-
§ zhuhx@pku.edu.cn
phasizing that LLMs overall tend to choose states with
[1] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter,
relativelylowpotentialfunctionvaluesasthenextstate, F.Xia,E.H.Chi,Q.V.Le,andD.Zhou,inProceedings
even though they may not necessarily perform better on of the 36th International Conference on Neural Informa-
actualdata. Inthisway,thepotentialfunctioncanreveal tion Processing Systems, NIPS ’22 (Curran Associates
the di”erences between the intrinsic cognition of LLMs Inc., Red Hook, NY, USA, 2022).
[2] S.Yao,J.Zhao,D.Yu,N.Du,I.Shafran,K.Narasimhan,
and real data.
and Y. Cao, React: Synergizing reasoning and acting in
Conclusion and Outlook. In this Letter, we have language models (2023), arXiv:2210.03629 [cs.CL].
proposed a framework based on the least action princi- [3] S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Gri”ths,

6
Y. Cao, and K. Narasimhan, Tree of thoughts: Deliber- F. J. R. Ruiz, and A. M. et. al., Alphaevolve: A cod-
ate problem solving with large language models (2023), ing agent for scientific and algorithmic discovery (2025),
arXiv:2305.10601 [cs.CL]. arXiv:2506.13131 [cs.AI].
[4] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, [20] Z.-Y. Song, Z. Cai, S. Zhang, J. Wei, J. Pan, S. Qiu,
S.Narang,A.Chowdhery,andD.Zhou,Self-consistency Q.-H. Cao, T.-J. Hou, X. Liu, M. xing Luo, and
improves chain of thought reasoning in language models H.X.Zhu,Iteratedagentforsymbolicregression(2025),
(2023), arXiv:2203.11171 [cs.CL]. arXiv:2510.08317 [physics.comp-ph].
[5] L. Wang, W. Xu, Y. Lan, Z. Hu, Y. Lan, R. K.-W. Lee, [21] N.Bhattacharya,N.Thomas,R.Rao,J.Dauparas,P.K.
and E.-P. Lim, Plan-and-solve prompting: Improving Koo,D.Baker,Y.S.Song,andS.Ovchinnikov,inPacific
zero-shot chain-of-thought reasoning by large language Symposium on Biocomputing, Vol. 27 (World Scientific,
models (2023), arXiv:2305.04091 [cs.CL]. Singapore, 2022) pp. 34–45.
[6] T. Schick, J. Dwivedi-Yu, R. Dess`ı, R. Raileanu, [22] Y. Sun and B. Haghighat, Phase transitions in
M.Lomeli,L.Zettlemoyer,N.Cancedda,andT.Scialom, large language models and the o(n) model (2025),
Toolformer: Language models can teach themselves to arXiv:2501.16241 [cs.LG].
use tools (2023), arXiv:2302.04761 [cs.CL]. [23] Z.Liu,Y.Liu,J.Gore,andM.Tegmark,Neuralthermo-
[7] G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, dynamic laws for large language model training (2025),
Y. Zhu, L. Fan, and A. Anandkumar, Voyager: An arXiv:2505.10559 [cs.LG].
open-ended embodied agent with large language models [24] E. Hoel, Entropy 19 (2017).
(2023), arXiv:2305.16291 [cs.AI]. [25] J. J. Hopfield, Proceedings of the Na-
[8] W. Chen, X. Ma, X. Wang, and W. W. Cohen, Pro- tional Academy of Sciences 79, 2554 (1982),
gram of thoughts prompting: Disentangling computa- https://www.pnas.org/doi/pdf/10.1073/pnas.79.8.2554.
tionfromreasoningfornumericalreasoningtasks(2023), [26] J. Wei, Y. Tay, R. Bommasani, C. Ra!el, B. Zoph,
arXiv:2211.12588 [cs.CL]. S.Borgeaud,D.Yogatama,M.Bosma,D.Zhou,D.Met-
[9] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, zler, E. H. Chi, T. Hashimoto, O. Vinyals, P. Liang,
J.Callan,andG.Neubig,inProceedingsofthe40thInter- J.Dean,andW.Fedus,TransactionsonMachineLearn-
national Conference on Machine Learning, Proceedings ing Research (2022), survey Certification.
of Machine Learning Research, Vol. 202 (PMLR, 2023) [27] R.Schae!er,B.Miranda,andS.Koyejo,inProceedingsof
pp. 10764–10799. the37thInternationalConferenceonNeuralInformation
[10] J. Liang, W. Huang, F. Xia, P. Xu, K. Hausman, Processing Systems, NIPS ’23 (Curran Associates Inc.,
B. Ichter, P. Florence, and A. Zeng, Code as policies: Red Hook, NY, USA, 2023).
Language model programs for embodied control (2023), [28] A. A. Markov (2006) uRL https://api.
arXiv:2209.07753 [cs.RO]. semanticscholar.org/CorpusID:126339706.
[11] D. J. Mankowitz, A. Michi, A. Zhernov, M. Gelmi, [29] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth,
M. Selvi, C. Paduraru, E. Leurent, S. Iqbal, J.-B. A. H. Teller, and E. Teller, The Journal of Chemical
Lespiau, and A. e. a. Ahern, Nature 618, 257 (2023). Physics 21, 1087 (1953).
[12] J.S.Park,J.O’Brien,C.J.Cai,M.R.Morris,P.Liang, [30] M. M´ezard, G. Parisi, and M. A. Virasoro, Spin Glass
and M. S. Bernstein, in Proceedings of the 36th Annual Theory and Beyond (World Scientific, Singapore, 1987).
ACM Symposium on User Interface Software and Tech- [31] D.V.Schroeder,Anintroductiontothermalphysics (Ox-
nology,UIST’23(AssociationforComputingMachinery, ford University Press, 2020).
New York, NY, USA, 2023). [32] R.S.Sutton,A.G.Barto,etal.,ReinforcementLearning:
[13] M. Besta, N. Blach, A. Kubicek, R. Gerstenberger, An Introduction, Vol. 1 (MIT Press, Cambridge, MA,
M. Podstawski, L. Gianinazzi, J. Gajda, T. Lehmann, 1998).
H. Niewiadomski, P. Nyczyk, and T. Hoefler, Proceed- [33] N.TishbyandN.Zaslavsky,2015IEEEInformationThe-
ings of the AAAI Conference on Artificial Intelligence ory Workshop, ITW 2015 (2015).
38, 17682 (2024). [34] N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy,
[14] M. Mohammadi, Y. Li, J. Lo, and W. Yip, in Proceed- and P. T. P. Tang, ArXiv abs/1609.04836 (2016).
ingsofthe31stACMSIGKDDConferenceonKnowledge [35] J.Safko,H.Goldstein,andC.Poole,Classicalmechanics
Discovery and Data Mining V.2,KDD’25(ACM,2025) (2002).
p. 6129–6139. [36] K.Friston,NatureReviewsNeuroscience11,127(2010).
[15] R.Sapkota,K.I.Roumeliotis,andM.Karkee,Aiagents [37] A.Tschantz,M.Baltieri,A.K.Seth,andC.L.Buckley,
vs. agentic ai: A conceptual taxonomy, applications and in 2020 International Joint Conference on Neural Net-
challenges (2025), arXiv:2505.10468 [cs.AI]. works (IJCNN) (2020) pp. 1–8.
[16] D. A. Boiko, R. MacKnight, B. Kline, and G. Gomes, [38] D. B. West, Introduction to graph theory (2001).
Nature 624, 570 (2023). [39] M. Yasunaga, X. Chen, Y. Li, P. Pasupat, J. Leskovec,
[17] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, P.Liang,E.H.Chi,andD.Zhou,Largelanguagemodels
A. D. White, and P. Schwaller, Chemcrow: Augment- asanalogicalreasoners(2024),arXiv:2310.01714[cs.LG].
ing large-language models with chemistry tools (2023), [40] T.Joachims,inProceedingsoftheEighthACMSIGKDD
arXiv:2304.05376 [physics.chem-ph]. International Conference on Knowledge Discovery and
[18] B. Romera-Paredes, M. Barekatain, A. Novikov, M. Ba- Data Mining,KDD’02(AssociationforComputingMa-
log,M.P.Kumar,E.Dupont,F.J.R.Ruiz,J.S.Ellen- chinery, New York, NY, USA, 2002) p. 133–142.
berg,P.Wang,O.Fawzi,P.Kohli,andA.Fawzi,Nature [41] X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, Mathematical
625, 468 (2024). Programming 127, 203 (2011).
[19] A. Novikov, N. Vu˜, M. Eisenberger, E. Dupont, P.-S. [42] A.M.Lyapunov,Internationaljournalofcontrol55,531
Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, (1992).

7
[43] S. H. Strogatz, Nonlinear dynamics and chaos: with ap-
plicationstophysics,biology,chemistry,andengineering
(CRC press, 2015).
[44] S. Weinberg, Physica A 96, 327–340 (1979).
[45] J. C. Scho¨n, Journal of Physics A: Mathematical and
General 30, 2367 (1997).
[46] I. Collaboration, Ideasearch, https://github.com/
IdeaSearch/IdeaSearch-fit (2025).
[47] I. Collaboration, Ideasearchfitter, https://github.com/
IdeaSearch/IdeaSearch-framework (2025).
[48] R.S.Olson,W.LaCava,P.Orzechowski,R.J.Urbanow-
icz, and J. H. Moore, BioData mining 10, 36 (2017).
[49] K.Singhal,S.Azizi,T.Tu,S.S.Mahdavi,J.Wei,H.W.
Chung,N.Scales,A.Tanwani,H.Cole-Lewis,andS.e.a.
Pfohl, Nature 620, 172 (2023).
[50] N.J.Szymanski,B.Rendy,Y.Fei,R.E.Kumar,T.He,
D.Milsted,M.J.McDermott,M.Gallant,E.D.Cubuk,
A. Merchant, H. Kim, A. Jain, C. J. Bartel, K. Persson,
Y. Zeng, and G. Ceder, Nature 624, 86 (2023).
[51] Z.-Y. Song, T.-Z. Yang, Q.-H. Cao, M. xing Luo, and
H.X.Zhu,Explainableai-assistedoptimizationforfeyn-
man integral reduction (2025), arXiv:2502.09544 [hep-
ph].
[52] Q.-H. Cao, Z.-Y. Hou, Y.-Y. Li, X. Liu, Z.-Y. Song,
L.-Q. Zhang, S. Zhang, and K. Zhao, Scalable quan-
tum state preparation via large-language-model-driven
discovery (2025), arXiv:2505.06347 [quant-ph].

8
SUPPLEMENTAL MATERIAL FOR “DETAILED BALANCE IN LARGE LANGUAGE MODEL-DRIVEN
AGENTS”
A. EQUIVALENCE OF THE LEAST ACTION PRINCIPLE AND THE VARIATIONAL CONDITION
ThissupplementarymaterialprovestheequivalenceofthevariationalconditionEq.(2)andtheleastactionprinciple
when K(x) is a convex function. The proof is conducted in the discrete case.
Firstly, we prove that the variational condition is a necessary condition for the least action.
Proof 1 Assume that when the least action is satisfied, V does not satisfy the variational condition Eq. (2), then
T
there exists at least one state f such that
0
ε
S =0. (9)
εV(f ) ≃
0 $V=V
$ T
$
This implies that there must exist another potential fun$ction V
↓
defined as
T
ε
V
T
↓ (f)=V
T
(f)+ϖε f,f0εV( S
f 0 ) $V=V
, (10)
$ T
where ε is the Kronecker delta, and ϖ is a su!ciently small constan$t. Expanding the action around it yields
f,f0 $
S
ε
[V ↓ ]= [V ]+ S (V ↓ (f) V (f))+O(ϖ2)
S T S T f εV(f) $V=V T ↓ T
" $ T
ε $
= [V ]+ S $ (V ↓ (f 0 ) V (f 0 ))+O(ϖ2)
S T εV(f 0 ) $V=V T ↓ T
$ T
$ 2
= [V ]+ϖ ε S $ +O(ϖ2). (11)
S T % εV(f 0 ) $V=V &
$ T
$
By choosing a su!ciently small ϖ> 0, the first-order te$rm dominates, and due to Eq. (9), we have
2
ε
S >0, (12)
εV(f )
% 0 $V=V &
$ T
$
Thus, $
[V ]< [V ]. (13)
↓
S T S T
This contradicts the assumption that V is the least action, thus completing the proof.
T
Next, we prove that when K(x) is a convex function, the potential function V satisfying the variational condition
T
is necessarily a global minimum point of the action . This can be reduced to proving that the action is a convex
S S
functional.
Proof 2 Let V ,V be any two potential functions, and 0 ϱ 1, then
1 2
⇐ ⇐
[ϱV +(1 ϱ)V ]
1 2
S ↓
= K(ϱV (f)+(1 ϱ)V (f) ϱV (g) (1 ϱ)V (g)) (g f)
1 2 1 2
↓ ↓ ↓ ↓ T →
f,g
"
ϱK(V (f) V (g))+(1 ϱ)K(V (f) V (g)) (g f)
1 1 2 2
⇐ ↓ ↓ ↓ T →
f,g
"
=ϱ [V ]+(1 ϱ) [V ], (14)
1 2
S ↓ S
where the inequality arises from the convexity of K(x) and the positivity of (g f), thus completing the proof.
T →
In summary, when K(x) is a convex function, the variational condition Eq. (2) and the principle of least action are
equivalent.

9
From To ATT. TUR. PER. PRO. BUZ. escape
\
ATT. 0 0 66 20 0 3914
TUR. 4122 0 0 0 0 0
PER. 3879 0 0 0 0 121
PRO. 3558 0 0 0 0 442
BUZ. 3859 238 0 0 0 0
TABLEII.Transitionkernel (g f)=min(N(g f)/4000,1)fortheClaude-4model,whereATT.,TUR.,PER.,PRO.,and
T → →
BUZ. represent the states ATTITUDE, TURKEY, PERSONAL, PROBLEM, and BUZZY, respectively. Each row represents
the number of transitions starting from state f, and each column represents the number of transitions to state g. The reason
for“escape” isthat sometransitionsarerejected becausetheyarenot wordsorthesumoflettersisnot 100, orthegenerated
word is still the prompt word, especially for transitions starting from the ATTITUDE state.
B. THE LEAST ACTION PRINCIPLE FOR EXTREME AGENTS
This Supplemental Material proves that the detailed balance condition Eq. (5) is a su!cient condition for the
variationalprinciple. Itthenintroducessometechniquesforanalyticallycalculatingtheminimumvalueoftheaction,
based on which the potential function distributions of the Claude-4 are analyzed.
Detailed balance condition is a su!cient condition for the variational principle
Proof 3 Assume that the agent satisfies the detailed balance condition Eq. (5), then for any state pair (f,g), we
T
have
(f g)= (g f)e ω(V (f) V (g)). (15)
T → T → ↗ T ↗ T
Therefore, substituting this relation into the equilibrium condition Eq. (3), we obtain
1
K (V (f) V (g)) K (V (g) V (f))e ω(V (f) V (g)) (g f)=0. (16)
2 ↓ T ↓ T ↓ ↓ T ↓ T ↗ T ↗ T T →
" f,g ’ (
Substituting the derivative of K(x) into the above equation, the result is naturally satisfied.
It’s worth noting that any K(x) function satisfying
K (x) K ( x)e ωx =0, (17)
↓ ↓ ↗
↓ ↓
makes the detailed balance condition a su!cient condition for the variational principle. There are no specific require-
ments for the form of K(x) here.
Analytically calculating the minimum action value
TakingtheClaude-4modelasanexample, wedemonstratehowtoanalyticallycalculatetheminimumactionvalue
to analyze the distribution of the potential function. Since only 5 di”erent prompt words are involved, a relatively
accurate estimation method is N (f)=20000/5=4000, thus estimating the transition kernel (g f) as
0
T →
N(g f) N(g f)
(g f) → min → ,1 . (18)
T → ↘ N (f) ↘ 4000
0 ) *
where N(g f) is the number of transitions from state f to state g as shown in the table II. We excluded self-loop
→
transitions (f = g) and states that were recorded only once ( N(g f) 1). We also indicate that transitions
g→ ↓ → ⇐
startingfrom agiven statemay “escape”for more detailed discussion, i.e., (escape f)=1 (g f). Here,
# T → ↓ gT →
N(g f) represents the number of transitions from state f to state g.
→ #

10
FIG. 6. Transition process of the Gemini-2.5-flash model in the prompt word state space, sorted by the potential function
V . Transitions tend to move towards states with lower potential functions. States with ωV(f) log(20000) 10 are those
T ↑ ↓
where the equilibrium condition cannot be strictly satisfied. Thick lines represent high-frequency transitions, while thin lines
represent low-frequency transitions. Each horizontal line represents a state, arranged in order of increasing potential function.
Now, setting the zero point of the potential function as V (ATT.) = 0, for the state PERSONAL, which has
T
transitions only with the ATTITUDE state, the equilibrium condition Eq. (3) degenerates into the detailed balance
condition, yielding
(PER. ATT.) 66/4000
ωV (PER.) logT → =log 4.1. (19)
T ↘ (ATT. PER.) 3879/4000 ↘
T →
Similarly, for the state PROBLEM, we have V (PRO.) 5.2. For the state BUZZY, there are no transitions into it,
T ↘
meaning that its potential function value cannot be estimated; it can only be judged that it should be much greater
than log(20000) 10, which should be the maximum range for accurate measurement of the potential function.
⇒ ⇒
For the state TURKEY, there are two transitions: one from ATTITUDE to TURKEY and another from BUZZY
to TURKEY. Since it has been assumed that V (BUZZY) , the equilibrium condition Eq. (3) simplifies to
T ↑⇑
K (ωV (TUR.) ωV (ATT.)) (TUR.,ATT.)=K (ωV (BUZ.) ωV (TUR.)) (BUZ.,TUR.), (20)
↓ ↓
T ↓ T T T ↓ T T
thus obtaining
ωV (TUR.) . (21)
T ↑⇑
In summary, the potential function of the Claude-4 model is approximately
0, f =ATT.,
4.1, f =PER.,
ωV (f)  . (22)
T ↘ 5.2, f =PRO.,
, f =BUZ. or TUR.,
⇒⇑
This is consistent with the results in Fig. 2. It
is
worth noting that in this case, the potential function is almost
self-consistently derived directly from the results of the detailed balance condition.
Similarly, analyzing the Gemini-2.5-flash model yields the transition map shown in Fig. 6.
The potential function of Gemini-2.5-flash is approximately
0, f =ATTITUDE,
0.5, f =DISCIPLINE,
ωV
T
(f)
↘
 4
5
.
.
8
2
,
,
f
f
=
=
E
B
X
LI
C
S
E
S
L
F
L
U
E
L
N
,
T,. (23)
, f =others,
 ⇒⇑

11
TABLEIII.Databasestatisticsforthetwoagents,includingtransitionsamplingcounts,uniquestatecounts,uniquetransition
counts, and the number of states with sampling times greater than 1.
Agent Transition Samples Unique States Unique Transitions States with Samples >1
IdeaSearchFitter 50228 7484 21697 2551
Conditioned Word Generation (GPT5-Nano) 19968 645 9473 620
FIG. 7. Verification of the detailed balance condition for the Conditioned Word Generation Agent using GPT5-Nano model.
The error estimates only include root mean square statistical errors, excluding unknown systematic errors. Measurement
includesstatepairswithatleastonemeasuredtransitionsbetweenthetwostates. Theagent’sunderlyingpotentialfunctionis
consistent with the detailed balance condition, with systematic deviations from detailed balance observed at higher potential
function values. Points with V (f) V (g) >log20000 are excluded. One-fifth of the data points are displayed for clarity.
| T ↔ T |
C. IMPLEMENTATION OF AGENT
To validate the detailed balance proposed in this Letter, LLMs need to be embedded into an agent framework to
standardize their state space and state transitions. This Supplemental Material describes the implementation details
of two completely di”erent agent frameworks and supplements more experimental results, including the examination
of detailed balance through the potential function for the Constrained Word Generation Agent using GPT5-Nano
model and the direct examination of Eq. (7) in the IdeaSearchFitter Agent. For the Constrained Word Generation
AgentusingGPT5-NanomodelandtheIdeaSearchFitterAgent,whichinvolvemorestates,arelativelyappropriate
estimate is to ignore “escape” and directly take N (f) = N(g f). To achieve a more accurate evaluation, we
0 g →
filter out those states f for which N(g f) 1, as shown in Eq. (24).
g → ⇐ #
The transition sampling counts, unique state counts, unique transition counts, and the number of states with
#
samplingtimesgreaterthan1forthetwoagentsareshowninTableIII.ThecodeusedtoconstructtheAgentsbelow
can be found in the GitHub repository.
Conditioned Word Generation Agent
To examine the generative dynamics of the model, we constructed an agent based on a conditioned word
real,I
T
generation task. This agent generates a word through an LLM, requiring that the sum of the indices corresponding
to all letters in the word equals 100 (for example, ATTITUDE, EXCELLENT). The state space of this agent consists
of all words that satisfy this condition, and the large models used in state transitions are GPT5-Nano, Claude-4, and
Gemini-2.5-flash, which read the context containing prompts and given states to generate new words that meet the
condition. The specific implementation can be found in the GitHub repository.
The implementation of the Conditioned Word Generation Agent shows two di”erent behavioral patterns, with
the Claude-4 and Gemini-2.5-flash models exhibiting significant convergence, while the GPT5-Nano model demon-
strates broader exploration capabilities. Fig. 7 presents the results of verifying the detailed balance condition for the
Conditioned Word Generation Agent using the GPT5-Nano model.

12
FIG.8. Verificationofdetailedbalancethroughclosedpathsinthestatetransitiongraphofthecomplexagent . Eachpoint
real
T
represents a triplet, with a total of 620 di!erent triplets found in the experimental data, where each transition was detected
at least twice. This indicates that within the error range, the sums of the logarithms of the forward and backward transition
kernels are roughly equal, consistent with the detailed balance condition. To clearly display the figure, only 1/5 of the data
points are shown.
IdeaSearchFitter Agent
To examine the performance of LLM generative dynamics in specific tasks, we constructed an agent based on
real
T
the symbol fitting task using IdeaSearchFitter [47]. The state space of this agent consists of strings represented
as expression trees f, and state transitions are achieved by generating new expression trees through LLMs. The
agent runs in expert mode 10 times to obtain the database used in the main text; specifically, “example num” is set
to 1 to simplify the state space to numexpr strings, and “auto polish” is set to True to test with richer prompts.
“sample temperature” and “model sample temperature” are set to 1000.0 to uniformly sample the state space. Each
runsearchesthe“nikuradse 2”datasetfromPMLB[48]withoutearlystoppingconditions. Thefinaldatasetcontains
50,228 state transitions, involving 21,697 unique transitions and 7,484 unique states, of which 2,551 states were
sampled more than once. The implementation can be found in the GitHub repository.
Within this Agent, the method for estimating the transition kernel is:
N(g f)
→ , N(g f)>1 and g =f,
T (g → f)= 
0
#
,
g→↘ =f N(g ↓ → f)
#oth
g
e
→
rwise
↓
.
→ ≃ (24)

We excluded self-loop transitions (f =g) and states that were recorded only once ( N(g f) 1) to make the
g→ ↓ → ⇐
estimation of the transition kernel more accurate. Here, N(g f) represents the number of transitions from state f
→ #
to state g.
Inthemaintext,weexaminedthedetailedbalanceconditionoftheIdeaSearchFitteragentbydirectlycomparing
the di”erences in its potential function and the logarithm of the transition kernel ratios. To further validate detailed
balance, we also verified it through closed paths in its state transition graph. Specifically, we searched for all possible
triplets(f,g,h)intheexperimentaldatasuchthattransitionsexistbetweeneachpair. Foreachtriplet,wecalculated
the sums of the logarithms of the forward and backward transition kernels along the closed path, with the results
shown inFig. 8. Atotalof 620di”erent tripletswerefound inthe experimentaldata, indicatingthat withinthe error
range, the sums of the logarithms of the forward and backward transition kernels are roughly equal, consistent with
the detailed balance condition.
Next,wedemonstratethatevenwhenchangingthespecificformofK(x),aslongasitsatisfiesEq.(17),thepotential
functiondistributionconsistentwithdetailedbalancecanstillberecoveredthroughtheprincipleofleastaction. Fig.9
shows the results when using a common function form in transition dynamics, K(x)=log(1+e ωx). It can be seen
↗
that the potential function distribution is basically consistent with the results obtained using K(x) = e ωx/2 in the
↗
main text, further supporting the reasonableness of the detailed balance condition.
Finally,inordertofurthervalidatethereasonablenessofdetailedbalance,wediscusssuchpairswherethetransition
g f was not measured, while the transition f g was measured. Using the same notation conventions as in the
→ →

13
FIG.9. VerificationofthedetailedbalanceconditionforbothagentsusingK(x)=log(1+e↑ x),withallsettingsthesameas
in the main text. (a) Results for the IdeaSearchFitter agent. (b) Results for the Conditioned Word Generation Agent.
FIG.10. ForpairsintheIdeaSearchFitterandConditionedWordGenerationAgentwherethetransitionf gwasmeasured
→
but the transition g f was not, we compare the di!erences in their potential functions and the logarithm of the transition
→
kernel ratios. The figure shows points corresponding to 500 such pairs. The black dashed line represents the 90th percentile
line. It is mostly above the red dashed line representing detailed balance, indicating that the inequality Eq. (25) is basically
satisfied,withthosepointsatlarger ωV (f) ωV (g) possiblyarisingfromsystematicoverestimationofthepotentialfunction
di!erences. (a) Results for the Ide | aSeTarchF ↔ itteTr ag | ent with a total of 18,935 such pairs. (b) Results for the Conditioned
Word Generation Agent with a total of 8,805 such pairs. From this figure, it can be directly seen that most of such transition
pairs come from cases where N(f g)=1.
→
main text, we can estimate
(g f) 1/N(f)
ωV (f) ωV (g)=logT → > . (25)
T ↓ T (f g) N(f g)/N(g)
T → →
Here, N(f) represents the total number of transitions from state f. Fig. 10 shows the comparison results for these
pairs. ItcanbeseenthatthesepairsbasicallysatisfytheinequalityEq.(25),whichfurthersupportsthereasonableness
of the detailed balance condition. It is worth emphasizing that since these pairs are not fully included in the convex
optimization of the minimum action, the estimates of ωV (f) ωV (g) may sometimes be overestimated.
| T ↓ T |
D. DETAILED DISCUSSION ON THE MEANING OF ACTION
The generative dynamics of LLMs are often highly directional. In the main text, we pointed out that the strength
of this directionality can be measured by the size of the minimum action. In this Supplemental Material, we show
that the action actually provides a method for estimating how the state density in the LLM-generated state space
varies with the potential, and we use Majority Voting as an example to show that although the measurement of the
potential function must be performed through the agent, the distribution of the potential function is not sensitive to
the specific design of the agent when detailed balance is satisfied.
TakingtheIdeaSearchFitteragentandtheConditionedWordGenerationAgentconstructedwithGPT5-Nanoas
examples,wemeasuredthedistributionofpotentialfunctionsforallstatesinthedatabasethatweresampledatleast
twice,asshowninFig.11. Thedistributionsofbothagentsexhibitsignificantlocalizedstructures,indicatingthatthe

14
FIG.11. (a)DistributionofpotentialfunctionsforallstatessampledatleasttwiceintheIdeaSearchFitteragent. Itexhibits
a localized structure and can be fitted with a Gaussian distribution (µ = 0.56,ε = 4.37). (b) Distribution of potential
N ↔
functionsforallstatessampledatleasttwiceintheConditionedWordGenerationAgent. Itexhibitsalocalizedstructureand
can be fitted with a Gaussian distribution (µ= 0.93,ε =2.30).
N ↔
statedensityoftheagentsmaybelocalized; inotherwords,thelong-termbehavioroftheseagentsmaybeinsensitive
to the sampling temperature in the state space. The distribution can be fitted with a Gaussian distribution (µ,ς).
N
The relatively high standard deviation indicates that this potential function distribution is wide, within which the
agent can exhibit significant directionality.
To quantify the relationship between action and state distribution, we assume that for a typical transition g f,
→
it satisfies ωV(f) ωV(g) 1. Considering detailed balance, we can approximately write
↓ ⇓
2exp(ω(V(f) V(g))) (g f)DfDg. (26)
S↘ ↓ T →
! !f,gforV(f)<V(g)
If we only consider the scaling introduced by detailed balance, without considering the more specific structure of the
state transition kernel, we can assume that (taking ω =1 to simplify the notation):
2 V2 V2
exp (V V ) f g dV dV
S⇒ ! !Vf<Vg 2ϑς2 / f ↓ g ↓ 2ς2 ↓ 2ς2  f g
= + ≃ dV + ≃ dV 2 exp (V V ) V f 2 V g 2 . (27)
!↗≃ f !Vf g 2ϑς2 / f ↓ g ↓ 2ς2 ↓ 2ς2 
By making the variable substitutions u=V +V and v =V V , we can obtain
f g g f
↓
+ ≃ + ≃ 2 u2+v2
dv du exp v
S⇒ 2ϑς2 ↓ ↓ 4ς2
!0 !↗≃  
+ ≃ 2 v2
= dv exp v
⇔ϑς ↓ ↓ 4ς2
!0  
=2eε2
erfc(ς), (28)
whereerfcisthecomplementaryerrorfunction. Forlargeς,wecanapproximatelywrite S↘ S ε ω ⇐ = ϑ 0,indicatingthatthe
size of the action is inversely proportional to the standard deviation of the state density. Note that the normalization
should be chosen to match the measurement as =K(0). The comparison of the expected minimum action size
ε=0
S
through the potential function and the actual minimized action for the two agents is shown in Table IV.
This suggests that the size of the action estimates the characteristic energy scale in the agent’s transitions, with
smaller actions indicating that the agent’s transition dynamics are more directional, while larger actions suggest that
it is di!cult for the agent’s transitions to exhibit a clear directionality.
It is worth noting that measuring action is a more e!cient method compared to directly measuring the directional
distributionoftheentirestatespace. Inpracticalapplications,theagent’stransitionscanbesampledthroughlimited
measurements to estimate the characteristic energy scale corresponding to this generative dynamics, thereby helping

15
TABLE IV. Comparison of expected minimum action size through the potential function and actual minimized action for two
agents.
Agent ε Expected min. action Actual min. action
IdeaSearchFitter 4.38 0.129 0.150
Conditioned Word Generation(GPT5-Nano) 2.30 0.245 0.195
FIG. 12. Numerical comparison of both sides of Eq. (30). The comparison is performed for M = 10, with di!erent colors
representing di!erent values of (g f). The three subplots represent the cases of n=5,7,9, respectively.
T →
to improve the design of agent tasks more e!ciently. For example, in Fig. 5, it can be seen that when poorer fits
are sampled by IdeaSearchFitter, hyperparameters should be controlled to reduce the action and enhance the
directionality of the agent’s generation. While after reaching a better fit, the directionality of the internal generative
dynamics of the LLM no longer aligns with that required by the optimization function, and hyperparameters should
be controlled to increase the action, allowing the agent to serve as a mutation core [18, 20] to explore the state space
more e!ciently without directional constraints.
We next illustrate that when detailed balance is satisfied, the design of the agent often only changes the scale of
the potential function rather than its distribution. Therefore, the size of the action may serve as a universal metric
for agent design. First, we assume that before each agent transition, instead of directly generating and extracting a
new state, M candidate states are generated, and then the state that appears more than n>M/2 times among the
candidate states is selected as the new state (if no state meets this condition, the transition is rejected). Under this
design, assuming the original agent transition kernel is (g f), the new transition kernel can be written as
T →
M
M
(g f)= [ (g f)]k[1 (g f)]M k
↓ ↗
T → k T → ↓T →
k=n) *
"
=I (n,M n+1), (29)
(g f)
T ↔ ↓
where I (a,b) is the regularized incomplete beta function. Assuming is not very large, we have
x
T
(g f) I (n,M n+1) (g f) n
T ↓ → = T (g ↔ f) ↓ T → . (30)
(f g) I (n,M n+1) ↘ (f g)
T↓ → T (f ↔ g) ↓ )T → *
Numerical comparison is shown in Fig. 12. It can be seen that when (g f) is small, Eq. (30) basically
T →
holds. Indicating that simply multiplying V by a constant n can estimate the new potential function V nV ,
T T→ ↘ T
suggesting that the specific design of the agent has little e”ect on the distribution of the potential function. For this
issue, we also realize that K(0) 1, indicating that by increasing the selection threshold n, the action can be
S⇒ ⇐ϑε ⇒ n
e”ectively reduced, thereby enhancing the directionality of the agent’s generative dynamics, while increasing M does
notsignificantlya”ectthesizeoftheactionbutcanimprovesamplingsuccessratesbyincreasingthesamplingbudget
when the transition kernel is small.

16
Generallyspeaking,anagentperformingtaskswithinthedistribution(e.g.,infieldssuchashealthcare,experiments,
etc. [16, 49, 50]) should be designed to have a lower action, while an agent performing tasks outside the distribution
(e.g.,infieldssuchasexploringthefrontiersofmathematicsandtheoreticalphysics[18–20,51,52])shouldbedesigned
to have a higher action.
E. DISCOVERY OF POTENTIAL FUNCTION USING IDEASEARCH
In this Supplemental Material, we describe how to configure IdeaSearch and present the form and meaning of the
bestpotentialfunctiondiscovered. IdeaSearchisanautomaticprogramsearchmethodbasedonLLMs[20,46],which
can iteratively evaluate and optimize programs to solve complex problems by combining LLMs and evolutionary
algorithms. We use IdeaSearch to search for the expression form of the potential function. Specifically, we represent
the expression of the potential function as a combination of a predefined list of functions and operators, and the goal
of IdeaSearch is to find an expression that maps this list to a floating-point number to minimize the corresponding
action. IdeaSearch is configured with 16 di”erent models to search for the target potential function. After running
for 4000 rounds, the parameters in the best potential function were manually replaced and optimized using a random
descent algorithm to minimize the action. The result is shown in Code 1, and the specific configuration parameters,
evaluation, and running scripts of IdeaSearch can be found in the GitHub repository.
The best potential function assigns a potential value by tokenizing the input mathematical function string and
then evaluating its structure and complexity, normalizing the value to the range [-1, 1]. The function considers not
only the syntactic integrity of the input string but also extracts various features, including function usage, parameter
structure, and specific substructures. These features are combined to form the final expression. It is important to
emphasize that even though the structure of the potential function discovered by IdeaSearch does not capture the
non-commutativity of the potential function with respect to strings, it can still be used to estimate the directionality
of the agent’s transitions. This indicates that the directionality of agent transitions arising from LLM generation can
be observed at di”erent levels of coarse-graining, such as string level or expression level.
The following table lists the optimized parameter values obtained through random descent optimization with the
minimum action being 0.47. All values are rounded to 2 decimal places.
Parameter Value Parameter Value
empty input potential 0.85 freq var weight 1.82
paren penalty ↔1.70 freq var cap 10.04
extra char penalty 0.43 entropy bonus 0.60
extra char threshold 2.13 log v bonus 1.35
length penalty divisor 4.00 log bonus 0.60
max depth penalty 0.42 pattern affinity bonus 0.15
max depth threshold 0.33 pattern count divisor 11.67
func penalty 0.36 linear logv weight 0.29
div pow penalty 0.42 centered linear weight 0.27
abs penalty 6.50 nonlinear weight 0.81
trig penalty 0.75 exp weight 0.35
nested expr penalty 0.54 proximity cap 3.74
div zero risk penalty 0.54 proximity bonus 0.14
pow risk penalty 1.05 simple bonus 1.00
sqrt risk penalty 0.20 simple length threshold 77.42
no params penalty 1.00 simple func threshold 2.00
few params penalty 1.50 short bonus 0.50
few params threshold 2.87 short length threshold 50.72
optimal params min 3.00 max energy 4.59
optimal params max 5.53 K 1.37
optimal params bonus 0.43 pattern affinity threshold 0.29
excess params penalty 1.07 pattern affinity adjustment 0.01
excess params threshold 0.48 min potential 1.72
↔ max potential ↔0.93
nan inf default 0.00
overall factor 2.04
TABLE V: Optimized parameter values for the potential function dis-
covered using IdeaSearch.
The potential function discovered using IdeaSearch is implemented in Python as shown in Code 1.
Listing 1. Potential function discovered using IdeaSearch
import numpy as np
1
import re
2
import math
3
4

17
# Default values for parameters if not provided
5
default_params = {
6
’id_to_token’: {
7
0: ’sin’, 1: ’cos’, 2: ’tan’, 3: ’arcsin’, 4: ’arccos’, 5: ’arctan’,
8
6: ’tanh’, 7: ’log’, 8: ’log10’, 9: ’exp’, 10: ’square’, 11: ’sqrt’,
9
12: ’abs’, 13: ’*’, 14: ’**’, 15: ’/’, 16: ’+’, 17: ’-’, 18: ’1’,
10
19: ’2’, 20: ’pi’, 21: ’log_v_k_nu’, 22: ’param1’, 23: ’param2’,
11
24: ’param3’, 25: ’param4’, 26: ’param5’, 27: ’param6’, 28: ’param7’,
12
29: ’param8’, 30: ’param9’, 31: ’(’, 32: ’)’, 33: ’!’
13
}
14
}
15
16
def potential_optimized_batch(token_ids_list: list, params: dict) -> np.ndarray:
17
"""
18
!!!!Batch!version!of!potential!using!numpy!vectorization!for!speed.
19
!!!!Follows!the!exact!logic!of!potential()!but!processes!multiple!expressions!at!once.
20
21
!!!!Args:
22
!!!!!!!!token_ids_list:!A!list!of!token_id!lists,!each!representing!a!mathematical!
23
expression.
!!!!!!!!params:!A!dictionary!containing!the!parameters!for!calculating!the!potential.
24
25
!!!!Returns:
26
!!!!!!!!A!numpy!array!of!potentials!(energies)!for!all!expressions.
27
!!!!"""
28
# Use provided params, falling back to defaults
29
p = {**default_params, **params}
30
31
n = len(token_ids_list)
32
if n == 0:
33
return np.array([])
34
35
id_to_token = p[’id_to_token’]
36
37
# Pre-allocate arrays for vectorized operations
38
potentials = np.zeros(n, dtype=np.float64)
39
40
# Process each expression
41
for i, token_ids in enumerate(token_ids_list):
42
# Reconstruct expression string from tokens
43
s = "".join(id_to_token.get(t, "") for t in token_ids)
44
s = (s or "").strip()
45
s_lower = s.lower()
46
47
# 1) Input validity check
48
if not s_lower:
49
potentials[i] = p[’empty_input_potential’]
50
continue
51
52
# 2) Syntax completeness check
53
depth = 0
54
max_depth = 0
55
bad_paren = False
56
for ch in s:
57
if ch == ’(’:
58
depth += 1
59
if depth > max_depth:
60
max_depth = depth
61
elif ch == ’)’:
62
depth -= 1
63
if depth < 0:
64
bad_paren = True
65
depth = 0
66
if depth != 0:
67

18
bad_paren = True
68
69
# 3) Feature extraction
70
funcs = re.findall(r’\b(?:exp|log|ln|log10|sqrt|tanh|sin|cos|tan|abs|pow|ceil|
71
floor|log_v_k_nu)\b’, s_lower)
num_funcs = len(funcs)
72
73
num_exp = s_lower.count(’exp’)
74
num_log = s_lower.count(’log’) + s_lower.count(’ln’) + s_lower.count(’log10’)
75
num_sqrt = s_lower.count(’sqrt’)
76
num_abs = s_lower.count(’abs’)
77
num_trig = s_lower.count(’sin’) + s_lower.count(’cos’) + s_lower.count(’tan’)
78
num_div = s_lower.count(’/’)
79
num_pow = s_lower.count(’**’) + s_lower.count(’^’)
80
81
param_list = re.findall(r’\bparam\d+\b’, s_lower)
82
unique_params = sorted(set(param_list))
83
num_params = len(unique_params)
84
param_counts = [param_list.count(p_name) for p_name in unique_params]
85
total_params = sum(param_counts)
86
87
if num_params > 0:
88
mean_params = total_params / num_params
89
freq_var = sum((c - mean_params) ** 2 for c in param_counts) / num_params
90
entropy = -sum((c / total_params) * math.log((c / total_params) + 1e-12) for
91
c in param_counts) if total_params > 0 else 0.0
entropy_norm = entropy / (math.log(num_params) + 1e-12) if num_params > 1
92
else 0.0
else:
93
freq_var, entropy_norm = 0.0, 0.0
94
95
# Nikuradse-2 related structure recognition
96
has_log_v = ’log_v_k_nu’ in s_lower
97
linear_logv = bool(re.search(r’\bparam\d+\s*\*\s*log_v_k_nu\b’, s_lower))
98
centered_linear = bool(re.search(r’\bparam\d+\s*\*\s*\(\s*log_v_k_nu\s*[-]\s*
99
param\d+\s*\)’, s_lower))
logistic_present = len(re.findall(r’1\s*/\s*\(\s*1\s*\+\s*exp’, s_lower)) > 0
100
tanh_present = len(re.findall(r’\btanh\s*\(’, s_lower)) > 0
101
softplus_present = len(re.findall(r’log\s*\(\s*1\s*\+\s*exp’, s_lower)) > 0
102
103
pattern_count = int(has_log_v) + int(linear_logv) + int(centered_linear) + int(
104
logistic_present) + int(tanh_present) + int(softplus_present)
pattern_affinity = pattern_count / p[’pattern_count_divisor’]
105
106
nested_expr = bool(re.search(r’exp\s*\(’, s_lower)) or bool(re.search(r’log\s*\(’
107
, s_lower))
108
div_zero_risk = ’/’ in s_lower
109
pow_risk = num_pow > 0
110
sqrt_risk = num_sqrt > 0 and not bool(re.search(r’sqrt\s*\(\s*abs’, s_lower))
111
112
# 4) Energy calculation and mapping to [-1, 1]
113
energy = 0.0
114
115
# Syntax completeness penalty
116
if bad_paren:
117
energy += p[’paren_penalty’]
118
extra_chars = len(re.findall(r’[^0-9a-zA-Z_\+\-\*\/\^\.\(\),\s]’, s_lower))
119
energy += max(0, extra_chars - p[’extra_char_threshold’]) * p[’extra_char_penalty
120
’]
energy += math.log1p(len(s)) / p[’length_penalty_divisor’]
121
energy += max(0, max_depth - p[’max_depth_threshold’]) * p[’max_depth_penalty’]
122
123
# Basic function and operator complexity penalty
124

19
energy += num_funcs * p[’func_penalty’]
125
energy += (num_div + num_pow) * p[’div_pow_penalty’]
126
energy += num_abs * p[’abs_penalty’]
127
energy += num_trig * p[’trig_penalty’]
128
129
# Risk penalty
130
energy += p[’nested_expr_penalty’] if nested_expr else 0.0
131
energy += p[’div_zero_risk_penalty’] if div_zero_risk else 0.0
132
energy += p[’pow_risk_penalty’] if pow_risk else 0.0
133
energy += p[’sqrt_risk_penalty’] if sqrt_risk else 0.0
134
135
# Parameter diversity adjustment
136
if num_params == 0:
137
energy += p[’no_params_penalty’]
138
elif num_params < p[’few_params_threshold’]:
139
energy += p[’few_params_penalty’] * (p[’few_params_threshold’] - num_params)
140
elif p[’optimal_params_min’] <= num_params <= p[’optimal_params_max’]:
141
energy -= p[’optimal_params_bonus’]
142
else:
143
energy += (num_params - p[’excess_params_threshold’])
144
145
energy += p[’freq_var_weight’] * min(freq_var, p[’freq_var_cap’])
146
energy -= p[’entropy_bonus’] * entropy_norm
147
148
# Nikuradse-2 prior structure reward
149
if has_log_v:
150
energy -= p[’log_v_bonus’]
151
elif num_log > 0:
152
energy -= p[’log_bonus’]
153
154
# Structure matching reward
155
energy -= p[’pattern_affinity_bonus’] * pattern_affinity
156
157
# Structure similarity weighted penalty
158
proximity_score = 0.0
159
if has_log_v and num_params > 0:
160
proximity_score = (
161
p[’linear_logv_weight’] * int(linear_logv)
162
+ p[’centered_linear_weight’] * int(centered_linear)
163
+ p[’nonlinear_weight’] * (int(logistic_present) + int(tanh_present) +
164
int(softplus_present))
+ p[’exp_weight’] * num_exp
165
)
166
proximity_score = min(p[’proximity_cap’], proximity_score)
167
energy -= p[’proximity_bonus’] * proximity_score
168
169
# Simplicity preference
170
171
simple_pattern = re.compile(r’^[0-9a-zA-Z_\s\+\-\*\/\.\(\),]+$’)
truly_simple = bool(simple_pattern.match(s_lower)) and num_funcs <= p[’
172
simple_func_threshold’] and num_pow == 0
if truly_simple and len(s) < p[’simple_length_threshold’]:
173
energy -= p[’simple_bonus’]
174
elif len(s) < p[’short_length_threshold’]:
175
energy -= p[’short_bonus’]
176
177
# Avoid unstable operations
178
if ’0’ in s_lower and (’/’ in s_lower or ’**’ in s_lower):
179
energy += 0 # Final mapping
180
181
if energy < 0:
182
energy = 0.0
183
max_energy = p[’max_energy’]
184
if energy > max_energy:
185
energy = max_energy
186

20
187
K = p[’K’]
188
norm = 1 - math.exp(-energy / K)
189
val = -1 + 2 * norm
190
191
# Fine-tuning for key pattern matching
192
if pattern_affinity >= p[’pattern_affinity_threshold’] and (logistic_present or
193
tanh_present or softplus_present or has_log_v):
val -= p[’pattern_affinity_adjustment’]
194
195
if math.isnan(val) or math.isinf(val):
196
val = p[’nan_inf_default’]
197
val = max(p[’min_potential’], min(p[’max_potential’], val))
198
199
potentials[i] = float(round(val, 5))*p[’overall_factor’]
200
201
return potentials
202
