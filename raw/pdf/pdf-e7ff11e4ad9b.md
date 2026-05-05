---
id: pdf-e7ff11e4ad9b
type: pdf
title: Leopold-Aschenbrenner_Existential-risk-and-growth_
url: ''
authors: []
ingested_at: '2026-04-29T16:23:44Z'
content_hash: sha256:9d7bb87643bbc1432e7097acd1c33f89590d972635a248ca33ba80ea911bebfc
source_path: raw/pdf/pdf-e7ff11e4ad9b.pdf
domains:
- ai-and-agents
nlm_corpus_ids:
- 7eac1296-b611-422e-85bb-6c36f5c8872b
wiki_pages:
- wiki/entities/leopold-aschenbrenner.md
- wiki/entities/global-priorities-institute.md
- wiki/entities/philip-trammell.md
- wiki/concepts/existential-risk.md
- wiki/concepts/time-of-perils.md
- wiki/concepts/environmental-kuznets-curve.md
- wiki/concepts/directed-technical-change.md
- wiki/concepts/scale-effect-existential-risk.md
- wiki/concepts/differential-technological-development.md
- wiki/concepts/value-of-life-economics.md
- wiki/concepts/endogenous-growth-model.md
- wiki/concepts/ai-existential-risk.md
meta:
  page_count: 99
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/Leopold-Aschenbrenner_Existential-risk-and-growth_.pdf
published_at: '2020'
---
Existential risk and
growth
Leopold Aschenbrenner
Global Priorities Institute | September 2020
GPI Working Paper No. 6-2020

Existential Risk and Growth
Leopold Aschenbrenner∗
Columbia University and Global Priorities Institute, University of Oxford
September 30, 2020 – Version 0.6
Preliminary
Abstract
Humanactivitycancreateormitigaterisksofcatastrophes,suchas
nuclear war, climate change, pandemics, or artificial intelligence run
amok. These could even imperil the survival of human civilization.
What is the relationship between economic growth and such existen-
tial risks? In a model of directed technical change, with moderate
parameters, existential risk follows a Kuznets-style inverted U-shape.
This suggests we could be living in a unique “time of perils,” having
developed technologies advanced enough to threaten our permanent
destruction, butnothaving grown wealthy enough yet to bewilling to
spend sufficiently on safety. Accelerating growth during this “time of
perils” initially increases risk, but improves the chances of humanity’s
survivalin thelong run. Conversely, even short-term stagnation could
substantially curtail the future of humanity.
∗
Contact: leopold.aschenbrenner@columbia.edu. IamverygratefultoPhilipTrammell
forhisgenerousmentorshipandhelpwiththisproject. IamalsogratefultotheCentrefor
EffectiveAltruism,theUniversityofOxford’sFutureofHumanityInstitute,andColumbia
ISERP for their support.

EXISTENTIAL RISK AND GROWTH 1
1 Introduction
The last two centuries of economic progress have brought enormous prosper-
ity. Yetthiseconomicprogresshasalsocreatedthepossibilityofcatastrophes
such as nuclear war, extreme climate change, or bioengineered pandemics. In
the next century, powerful artificial intelligence (AI) might engender amaz-
ing advances, but some worry that it could run amok. Increasing attention
is being paid to these so-called “existential” risks that could imperil human
civilization. In particular, existential risks are those that threaten human
extinction or could otherwise irreversibly curtail the potential of humankind
(suchasawarthatpermanentlysendsusbacktotheStoneAge); seeBostrom
(2002), Posner (2004), and Farquhar et al. (2017). Some philosophers argue
that because of the potential “astronomical” value associated with the long-
run future of humanity, mitigating existential risk that could curtail this
future should be of paramount concern; see Bostrom (2003).
However, most people generally have a positive rate of pure time prefer-
ence; they do not care much about the long-run future of humanity. What
happens to existential risk when resources are allocated impatiently? In par-
ticular, whatistheinteractionbetween economicgrowthandexistential risk?
Does faster economic growth accelerate the development of dangerous new
technologies, thereby increasing theprobability ofanexistential catastrophe?
I develop a model of endogenous and directed technical change, involving
a tradeoff between consumption and safety. Consumption and the associated
technologies carry some risk of disaster, which can be mitigated by spend-
ing on safety and developing safety technology. The outcome turns out to
critically depend on the scale effect of existential risk—that is, how pro-
portionally growing both consumption and safety affects existential risk. If
existential risk decreases with scale, no special concern for safety is required
for risk to fall to zero exponentially and for risk to decrease with growth. If
existential risk increases with scale moderately, the level of existential risk
may follow an inverted U-shape. This grounds the intuition of some promi-
nent thinkers, like Sagan (1994) and Parfit (2011), that human civilization
could be passing through a unique “time of perils.” We may have advanced
enough to create technologies that threaten our permanent destruction, but
not yet grown wealthy enough to be willing to spend much on safety. During
this “timeof perils,” accelerating growth initially increases risk, but (perhaps
counterintuitively) improves the chances of humanity’s survival in the long
run. Conversely, even short-term stagnation substantially hurts the chances

EXISTENTIAL RISK AND GROWTH 2
ofhumanity’s survival inthe longrun. Finally, if thescale effect of existential
riskistoolargeandthereturnsto research diminishtoorapidly, itisimpossi-
ble to avert an eventual existential catastrophe. Though the social the social
planner may choose the “end of growth”—stagnation in consumption—if the
marginal utility of consumption diminishes rapidly, humanity is doomed to
soon destruction regardless.
This paper relates to the literature on the relationship between economic
growth and environmental degradation (see Brock and Taylor (2005) for an
overview). MostrelevantisStokey(1998), demonstratingthatifthemarginal
utility of consumption diminishes rapidly, there is an inverted U-shape re-
lationship between economic development and pollution; this relationship is
often called the “environmental Kuznets curve.” I find that the level of ex-
istential risk may follow a similar inverted U-shape. However, Stokey (1998)
looks at environmental degradation that additively reduces utility; existen-
tial risk that imperils the survival of human civilization is a quite different
concern.
To model people’s concern about risks of existential catastrophes, I build
on previous work on the value of life. Hall and Jones (2007) show that
for a large class of conventional preferences, as consumption grows and the
marginal utility of consumption declines, it becomes relatively more valuable
to purchase additional days of life rather than increasing consumption on
any given day of life. Jones (2016) shows how this can lead society to value
safety over consumption growth, resulting in optimal consumption growth
lower than what is feasible. In his richer endogenous growth model, lifesav-
ing goods can be purchased to increase people’s lifespan. I build on this
model to look at existential risk. Unlike the mortality in Jones’s model, hu-
man activity can increase risk, and I model risk as depending on aggregate
not per-capita variables.
Critically, modeling existential risk as depending on total instead of per-
capita variables allows for a scale effect. Previous work has not allowed
for such a scale effect. In particular, Martin and Pindyck (2015, 2019) and
Aurland-Bredesen (2019) posit a fixed set of possible catastrophes, which
would each require a constant permanent tax on consumption to avert. Yet
thisisaknife-edgeassumption: holdingsafetyspendingconstantasafraction
of output only holds risk constant when the scale effect is exactly zero or
when population doesn’t grow. This paper generalizes from this knife-edge
assumption, illustrating the divergent dynamics of the cases when existential
risk decreases, increases, or increases very rapidly with scale.

EXISTENTIAL RISK AND GROWTH 3
The rest of this paper is organized as follows. Section 2 presents the
economic environment of the model and a benchmark “rule of thumb alloca-
tion.” Section 3 presents the asymptotic (impatient) optimal growth path,
highlighting how the scale effect of existential risk matters for the long run.
Section 4 discusses empirical evidence on the model parameters. Section
5 illustrates the transition path of the case with a moderate scale effect,
yielding the inverted U-shape path of existential risk. Section 6 analyzes
what happens to existential risk when growth accelerates. Section 7 presents
conclusions.
2 The Economic Environment
I look at an endogenous idea-based growth model based on the Jones (1995)
version of the Romer (1990) model. Similar to Jones (2016), this model
features a consumption and a safety sector with directed technical change
(see also Acemoglu (2002) and Acemoglu et al. (2012)).
2.1 Setup
The economy features a consumption sector, producing consumption output
C , and a safety sector, producing safety output H . A different set of tech-
t t
nology is used for each sector: A represents consumption technologies, while
t
B represents safety technologies.
t
Each person is either a worker or a scientist, and in turn workers and
scientists can work in either the consumption or safety sector. Workers are
denoted by L and use the available technology to produce output; scientists
are denoted by S and do R&D to increase the stock of technology. Total
production in each sector is then given by:1
C = AαL and H = BαL , (1)
t t ct t t ht
with α > 0.
The production functions for our two sets of technologies are given by:
A˙ = SλAφ and B˙ = SλBφ, (2)
t at t t bt t
1
Typically,thisismicrofoundedwithacontinuumofintermediategoodsineachsector.
I omit that here for concision. In addition, following the lead of the standard endogenous
growth models, labor is the only factor of production for simplicity.

EXISTENTIAL RISK AND GROWTH 4
where as in Jones (1995), I assume φ < 1 and 0 < λ ≤ 1.
LetN bethetotalpopulation; wethenhavethefollowingstraightforward
t
resource constraints:
L +L = L and S +S = S and L +S = N . (3)
ct ht t ct ht t t t t
Next, consider existential risk. Jones (2016) considers individual-level
mortality that can be reduced with lifesaving goods. I instead wish to con-
sider risks that threaten the survival of humanity as a whole.
These risks differ from Jones’s individual-level mortality in two critical
ways. First, these risks are man-made; humans have created the risk of
catastrophic climate change, dangerous AI running amok, or nuclear war.
Risk increases with more consumption: higher consumption may mean more
carbon emissions, more air travel that facilitates the spread of infectious
disease, more bioengineering that could result in an extremely lethal bio-
engineered pandemic, and more artificial intelligence technology that could
go awry. At the same time, the risk of an existential catastrophe may be
mitigated by investing in safety: we can abate pollution, engineer more re-
liable nuclear weapon locks (“permissive action links”) to reduce the risk of
accidental nuclear war, or invest in pandemic preparedness. Thus, unlike in
Jones (2016), where mortality is only a function of spending in the lifesaving
sector, existential risk in this model is a function of both consumption and
safety spending. Growth in consumption is thus not purely positive, but
creates risks. This model is inspired by the idea of “differential technological
development,” as articulated by Bostrom (2002): existential risk depends on
the relative rate of development of potentially dangerous technologies versus
technologies that ameliorate these hazards.
The second crucial difference to Jones (2016) is that existential risks de-
pend on total consumption and total safety spending—not on per-capita
consumption and per-capita safety spending. The risk of catastrophic cli-
mate change depends on total emissions, not per-capita emissions; the risk
of a pandemic depends on the total amount of opportunities for a deadly
(potentially bioengineered) pathogen to jump to a human (zoonosis) and
then spread from there, not per-capita opportunities for zoonosis; the risk
of a nuclear winter depends on the total number of nuclear weapons, not
per-capita nuclear weapons; the risk from a terrorist with WMDs depends
on what the craziest person is willing and able to do, not on the average
person. Similarly, existential risk mitigation depends on total spending on

EXISTENTIAL RISK AND GROWTH 5
carbon emissions abatement, biosecurity, AI safety, etc. This introduces a
scale effect: risk depends on the total size of the economy, similar to how
technological development depends onscaleinendogenous idea-basedgrowth
models.
I will assume that an existential catastrophe results in permanent zero
utility thereafter. This assumption should be exactly valid in the case of hu-
man extinction. It should also be a valid approximation for most existential
catastrophes that, while not quite killing everybody, irreversibly curtail the
potential of humankind (such as a war that permanently sends us back to
the Stone Age).2
Mathematically, human civilization face a time-varying hazard rate δ .
t
This represents a stochastic probability of an existential catastrophe. The
probability that human civilization survives to date t (starting from date 0)
is given by
M t = e−R 0 tδsds, (4)
corresponding to the laws of motion
M˙ = −δ M , M = 1. (5)
t t t 0
The hazard rate is endogenous, and as explained above increases with
total consumption and decreases with total safety spending:
δ = δCǫH−β. (6)
t t t
For those concerned about the long-run future of humanity, the key vari-
∞
able is M
∞
= lim
t→∞
M
t
= e−R
0
δsds. This represents the probability that
human civilization does not succumb to an existential catastrophe and en-
joys a long future with astronomical value.3 Critically, note that M is only
∞
∞
greater than zero iff δ ds is bounded.
0 s
2Some have considereRd other risks, such as a creeping, irreversible spread of global
authoritarianism; see Caplan (2008). Such a risk would not be covered by this model. I
wishto focus oncatastrophesthatwouldkillmostofthe people aliveatthe time or make
people’s lives so miserable so as to reduce their utility to roughly zero.
3Note that surviving to time “infinity” in this model does not literally mean human
civilization survives forever. Instead, it means human civilization does not destroy it-
self; there are other natural/physical limits to the survival of human civilization that are
not considered here. In particular, there might be natural sources of extinction risk, but
Snyder-Beattie et al. (2019) find that these are negligible compared to potential anthro-
pogenic extinction risks. Thus, I focus on anthropogenic existential risk in this paper.

EXISTENTIAL RISK AND GROWTH 6
Given c ≡ C /N and h ≡ H /N , expected lifetime utility for a repre-
t t t t t t
sentative agent is
∞
U = e−ρtu(c )M dt, (7)
t t
Z0
with standard flow utility:
c1−γ
u(c ) = u+ t . (8)
t 1−γ
Theparameteruisaconstant thatspecifies theupper boundoftheutility
ofliferelativetodeath(withtheutilityofdeathimplicitlynormalizedto0)in
the case where γ > 1 and thus c1−γ/(1−γ) is negative. See Hall and Jones
(2007) for a discussion of this constant. In particular, we will generally
assume that there is a level of consumption below which utility is negative,
i.e. life is not worth living. For γ > 1, this means u¯ is positive; for γ < 1,
this means u¯ is negative.
Finally, I assume an exogenous positive rate of population growth:4
N˙ = nN . (9)
t t
There are then three allocative decisions that need to be made:
1. The fraction of total scientists working on consumption: s ≡ Sat.
t St
2. The fraction of total workers working on consumption: ℓ ≡ Lct.
t Lt
3. The fraction of the population that is a scientist: σ ≡ St.
t Nt
2.2 Rule of Thumb Allocation
As a benchmark, it will be helpful to consider a simple “rule of thumb”
allocation, as in Jones (2016). This rule of thumb allocation is analogous
to Solow’s (1956) assumption of a fixed saving rate in his version of the
neoclassical growth model. In particular, I will consider a rule of thumb
allocation where the fraction of scientists and labor working on safety is
fixed. Later, I will consider the optimal allocation, in which the fraction of
resources dedicated to safety can evolve.
4ThisisrequiredforsustainedexponentialgrowthintheJones(1995)flavorofendoge-
nous growth models; the growing scale drives the long-run growth rate.

EXISTENTIAL RISK AND GROWTH 7
Proposition 1. Balanced growth under rule of thumb allocation
Consider a rule of thumb allocation where s = s, ℓ = ℓ, and σ = σ, all
t t t
strictly between zero and one. There exists a balanced growth path such that
λn
g∗ = g∗ = , (10)
A B 1−φ
αλn
g∗ = g∗ = g ≡ , (11)
c h 1−φ
g∗ = (ǫ−β)(g +n), (12)
δ
with
δ → 0 if ǫ < β, δ → δ∗ > 0 if ǫ = β, δ → ∞ if ǫ > β. (13)
t t t
Proof. See Appendix A.1.
Given our symmetric production functions and fixed allocation of labor
and scientists to safety and consumption, the long-run growth of bothsectors
looks like growth in the standard Jones (1995) version of the Romer (1990)
model. In particular, given the diminishing returns to research and the non-
rivalry of ideas, the long-rungrowth of both consumption and safety depends
on population growth. Moreover, given that a fixed fraction of workers and
scientists is allocated to the safety sector, both safety and consumption per
capita grow at the same rate.
What is important to note about this rule of thumb allocation is what
happens to existential risk. In the case that ǫ < β, i.e. safety is more potent
in reducing risk than consumption is in increasing it, the hazard rate δ falls
∞
to zero at an exponential rate. Therefore, δ ds is bounded, which implies
0 s
that the long-run probability of human civilization’s survival, M , is strictly
∞
R
greater than zero. In the knife-edge case of ǫ = β, the hazard rate converges
to a constant, implying M = 0. In the case that ǫ > β, i.e. consumption is
∞
more potent in increasing risk than safety is in decreasing it, the hazard rate
increases exponentially. This causes not only M = 0, but in fact δ → ∞,
∞
so the instantaneous probability of an existential catastrophe approaches 1.
Here, we begin to see the central role of ǫ−β. Recall that δ = δCǫH−β.
t t t
Thus, ǫ − β represents the scale effect of existential risk. If ǫ < β, risk
decreases with scale. Then, the future of humanity is bright: even if the
allocation of resources to safety stays fixed, existential risk decreases expo-
nentially. However, if ǫ > β, existential risk increases with scale. Then, more

EXISTENTIAL RISK AND GROWTH 8
scaledoesn’t leadtomorenonrivalideasandthereby moreoutput—asitdoes
in the classic Romer/Jones endogenous idea-based growth model—but more
scale also increases risk. In the rule of thumb allocation, the fixed allocation
of resources to safety leads the hazard rate to explode when ǫ > β. In a
sense, ǫ−β characterizes the fragility of the world.
3 The (Impatient) Optimal Allocation
I now turn to the optimal allocation. I consider a representative agent that
maximizes its utility. The representative agent discounts future utility with
positive rate ρ: the agent is impatient. Moreover, this representative agent
is selfish, i.e. it does not consider the growing population. (However, since
our population is growing at a constant rate, taking into account the growing
population is equivalent to lowering ρ.)
The optimal allocation of resources is a time path for c , h , s , ℓ , σ , A ,
t t t t t t
B , M , δ that maximizes the utility of the representative agent, solving the
t t t
following problem:
∞
max U = M u(c )e−ρtdt, (14)
t t
{st,ℓt,σt} Z0
subject to
c = Aαℓ (1−σ ), (15)
t t t t
h = Bα(1−ℓ )(1−σ ), (16)
t t t t
A˙ = sλσλNλAφ, (17)
t t t t t
B˙ = (1−s )λσλNλBφ, (18)
t t t t t
M˙ = −δ M , δ = δNǫ−βcǫh−β. (19)
t t t t t t t
Tosolvefortheoptimalallocation, IdefinethecurrentvalueHamiltonian:
H = M u(c )+p sλσλNλAφ +p (1−s )λσλNλBφ −v δ M , (20)
t t at t t t t bt t t t t t t t
where s , ℓ and σ are our control variables and M , A , and B our state
t t t t t t
variables. The costate variables p , p , and v capture the shadow values
at bt t
of an extra consumption idea, an extra safety idea, and an extra lifetime
respectively.

EXISTENTIAL RISK AND GROWTH 9
Based on the maximum principle and the arguments of Romer (1986),
the first-order conditions characterize a solution.
It will be useful to define
v
v˜ ≡ t . (21)
t u′(c )c
t t
This is the shadow value of life, converted to consumption units by u′(c ), as
t
a ratio to the level of consumption.
After some manipulation (see Appendix A.2) the first order conditions
yield:
1−ℓ βδ v˜
t t t
= , (22)
ℓ 1−ǫδ v˜
t t t
1−s βδ v˜ ρ−g −φg g
t = t t · pat At · Bt , (23)
s 1−ǫδ v˜ ρ−g −φg g
t t t pbt Bt At
σ λ(p A˙ +p B˙)
t at bt
= , (24)
1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t
v˙ 1
ρ = t + [u(c )−v δ ], (25)
t t t
v v
t t
p˙ 1 c A˙ δ
ρ = at + [M u′(c )α t +p φ t −αǫv M t ], (26)
t t at t t
p p A A A
at at t t t
p˙ 1 B˙ δ
bt t t
ρ = + [p φ +αβv M ]. (27)
bt t t
p p B B
bt bt t t
The term v˜—and in particular the product δ v˜—thus determines the allo-
t t t
cation of workers and scientists to consumption vs. safety. In Appendix A.2,
I show that v can also be represented as
t
u(c )
t
v = , (28)
t ρ−δ +g
t vt
and thus
u˜ u(c )
t t
v˜ = , u˜ = . (29)
t ρ−δ +g t u′(c )c
t vt t t
u˜ istheopportunitycost ofdeathu(c ), converted into consumption units by
t t
u′(c ), divided by the level of consumption c . u˜ thus represents the relative
t t
valueof life. The denominator ofv˜ essentially converts this into a discounted
t

EXISTENTIAL RISK AND GROWTH 10
present value. Therefore, v˜ represents the discounted relative value of life
t
and determines the demand for safety.
Note that the allocation of labor and scientists to safety is proportional
to βδtv˜t . The numerator represents the marginal value of safety: the re-
1−ǫδtv˜t
duction in the hazard rate. The denominator represents the marginal value
of consumption: the utility benefits of consumption (normalized to 1) minus
the increase in the hazard rate. Note that δ v˜ can’t rise forever as in (as in
t t
Jones, 2016); if ǫδ v˜ > 1, the marginal value of consumption is negative.
t t
3.1 The Optimal Allocation with ǫ ≤ β
First,considerthecaseinwhichsafetygoodsareatleastaspotentinreducing
existential risk as consumption goodsin increasing existential risk, i.e. ǫ ≤ β.
Then, existential risk weakly decreases with scale. The asymptotic growth
path depends on the curvature of our preferences. The propositions here
echo the results in Jones (2016).
Proposition 2. Optimal growth with ǫ ≤ β and γ > 1+(β−ǫ) 1−φ +1
αλ
Assume that ǫ ≤ β and that the marginal utility of consumption falls rapidly,
(cid:0) (cid:1)
in the sense that γ > 1 + (β − ǫ) 1−φ +1 . Then the optimal allocation
αλ
features an asymptotic constant growth path such that as t → ∞, the fraction
(cid:0) (cid:1)
of labor working in the consumption sector ℓ and the fraction of scientists
t
working on consumption technologys both fall to zero at constant exponential
t

EXISTENTIAL RISK AND GROWTH 11
rates, while σ → σ∗, and asymptotic growth is given by:5
t
λ(g +n)
g∗ = s > 0, (30)
A 1−φ
λn
g∗ = > g∗, (31)
B 1−φ A
αλn
g∗ = g, g ≡ , (32)
h 1−φ
β +(β −ǫ)1−φ
g = g · αλ < g, g∗ > 0, (33)
c γ +ǫ−1 c
" #
g∗ = −(γ −1)g∗ < 0, (34)
δ c
γ −1−β +ǫ ǫ−β
g∗ = g∗ = −g · −n· < 0, (35)
s ℓ (1+ αλ )(γ +ǫ−1) (1+ αλ )(γ +ǫ−1)
1−φ 1−φ
λαg
σ∗ = B . (36)
ρ+(γ −1)g +(1−φ+λα)g
c B
Note that δ → 0 exponentially, implying M > 0. Finally, note that this
t ∞
solution is valid for all ρ > 0.
Proof. See Appendix A.3.
Unlike intheruleofthumb allocation, theallocationofresources to safety
can adjust. In particular,
u(c ) 1
u˜ = t = ucγ−1 + . (37)
t u′(c )c t 1−γ
t t
Thus, given γ > 1, the relative value of life u˜ increases as consumption
t
grows. As people grow wealthier, the marginal utility of consumption de-
clines, and it becomes relatively more valuable to purchase more life and
spend on avoiding death. Note that this happens regardless of discount rate
ρ: no particular concern for the future is necessary for this dynamic. The
rising value of life means that resources are shifted towards the safety sector.
As such, consumption growth is substantially less than what is feasible and
substantially less than safety growth.
5 These results have the following form: limt→∞gct =g c ∗, and so on.

EXISTENTIAL RISK AND GROWTH 12
Proposition 3. Optimal growth with ǫ < β and γ < 1+(β−ǫ) 1−φ +1
αλ
Assume that ǫ < β and that the marginal utility of consumption falls, but not
(cid:0) (cid:1)
too rapidly, in the sense that γ < 1 + (β − ǫ) 1−φ +1 . Then the optimal
αλ
allocation features an asymptotic constant growth path such that as t → ∞,
(cid:0) (cid:1)
the fraction of labor working in the safety sector ℓ ˜ ≡ 1−ℓ and the fraction of
t t
scientists making safety ideas s˜ ≡ 1−s both fall to 0 at constant exponential
t t
rates, while σ → σ∗, and asymptotic growth is given by:
t
λn
g∗ = , (38)
A 1−φ
λ(n+g )
g∗ = s˜ < g∗,g∗ > 0, (39)
B 1−φ A B
g∗ = g (40)
c
g∗ = −βg∗ +ǫg∗ −(β −ǫ)n < 0, (41)
δ h c
with the exact values for g∗ and g∗ depending on γ. If 1 < γ < 1 + (β −
s˜ h
ǫ) 1−φ +1 :
αλ
(cid:0) (cid:1)
−n αλ (1+β −ǫ−γ)+(β −ǫ)
1−φ
g∗ = g∗ = < 0, (42)
s˜ ℓ˜ h 1+β(1+ αλ ) i
1−φ
(1+ αλ )(1−γ +β −ǫ)+(1+ 1−φ)(β −ǫ)
g = g · 1− 1−φ αλ < g∗. (43)
h " 1+β(1+ αλ ) # c
1−φ
If γ ≤ 1:
−n (1+ αλ )(β −ǫ)
1−φ
g∗ = g∗ = < 0, (44)
s˜ ℓ˜ h1+β(1+ αλ ) i
1−φ
(2+ αλ + 1−φ)(β −ǫ)
g = g · 1− 1−φ αλ < g∗. (45)
h " 1+β(1+ αλ ) # c
1−φ
Note that δ → 0 exponentially, implying M > 0.
t ∞
Proof. See Appendix A.4.
When γ is smaller, the value of life does not grow faster than the hazard
rate δ declines. Thus, the critical product δ v˜ declines, and resources are
t t t

EXISTENTIAL RISK AND GROWTH 13
shifted to consumption. As such, consumption growth remains as fast as is
feasible.
I wish not to emphasize the difference between the allocation for larger
or smaller γ, however. Instead, notice that regardless of the value of γ, the
hazard rate falls exponentially to zero, and thus M > 0. At the same time,
∞
consumption continues to grow exponentially and c → ∞. In that sense, the
t
outcomeoftheoptimal allocationintermsof thelong-runfutureofhumanity
is broadly similar to the rule of thumb allocation when ǫ < β.
To see why this is the case, note that when ǫ−β, existential risk decreases
with scale. Thus, growth naturally decreases risk.
Depending on the exact preferences, it may be possible to improve upon
the rule of thumb allocation by shifting more resources to safety or to con-
sumption over time, but the broad trajectory of the future of humanity looks
bright in any case.
Finally, note that there exists a knife-edge case, which I consider for
completeness.
Proposition 4. “Interior” growth with ǫ < β and γ = 1 + (β −
ǫ) 1−φ +1 , or with ǫ = β and γ ≤ 1
αλ
Assume either that ǫ < β and the knife-edge condition that γ = 1 + (β −
(cid:0) (cid:1)
ǫ) 1−φ +1 , or the knife-edge condition that ǫ = β and γ ≤ 1. Then the
αλ
optimal allocation features an asymptotic balanced growth path such that as
(cid:0) (cid:1)
t → ∞, s and ℓ approach constants strictly between zero and one, and the
t t
optimal allocation features the same balanced growth path as under the rule
of thumb allocation.
Proof. See Appendix A.5.
3.2 The Optimal Allocation with ǫ > β
Now, consider the case where consumption goods are more potent in in-
creasing existential risk than safety goods in reducing existential risk, i.e.
ǫ > β, but this difference is not too large, i.e. ǫ 6≫ β. Again, the asymptotic
growth path will depend on the curvature of our preferences. Here, we see a
divergence from Jones (2016).
Proposition 5. Optimal growth with ǫ > β and γ > 1
Assume that ǫ > β. Assume that ǫ 6≫ β in the sense that ǫ−β < αλ . Finally,
β 1−φ
assume that the marginal utility of consumption falls rapidly, in the sense that

EXISTENTIAL RISK AND GROWTH 14
γ > 1. Then the optimal allocation features an asymptotic constant growth
path such that as t → ∞, the fraction of labor working in the consumption
sector ℓ and the fraction of scientists working on consumption technology s
t t
both fall to zero at constant exponential rates, while σ → σ∗, and asymptotic
t
growth is given by:
λ(g +n)
g∗ = s > 0, (46)
A 1−φ
λn
g∗ = > g∗, (47)
B 1−φ A
g∗ = g, (48)
h
β +(β −ǫ)1−φ
g = g · αλ < g, g∗ > 0, (49)
c γ +ǫ−1 c
" #
g∗ = −(γ −1)g∗ < 0, (50)
δ c
γ −1−β +ǫ ǫ−β
g∗ = g∗ = −g · −n· < 0, (51)
s ℓ (1+ αλ )(γ +ǫ−1) (1+ αλ )(γ +ǫ−1)
1−φ 1−φ
λαg
σ∗ = B . (52)
ρ+(γ −1)g +(1−φ+λα)g
c B
Note that δ → 0 exponentially, implying M > 0. Finally, note that this
t ∞
solution is valid for all ρ > 0.
Proof. See Appendix A.6.
Given γ > 1, the relative value of life u˜ rises as consumption grows,
t
as before. Unlike before, however, we now have ǫ − β > 0: existential risk
grows with scale. Despite this scale effect, workers and scientists are shifted
to the safety sector quickly enough that δ still declines exponentially on the
t
asymptotic growth path. In turn, M > 0. Unlike in the rule of thumb
∞
allocation, there is a nonzero probability that humanity does not succumb
to an existential catastrophe.
Proposition 6. Optimal growth with ǫ > β and 1−ǫ < γ ≤ 1
Assume that ǫ > β. Assume that ǫ 6≫ β in the sense that ǫ−β < αλ . Assume
β 1−φ
that the marginal utility of consumption falls, but not as rapidly, in the sense
that γ ≤ 1. Finally, assume that the elasticity of the hazard rate is larger
than the elasticity of utility with respect to consumption, i.e. ǫ > 1−γ. Then
the optimal allocation features an asymptotic constant growth path such that

EXISTENTIAL RISK AND GROWTH 15
as t → ∞, the fraction of labor working in the consumption sector ℓ and the
t
fraction of scientists working on consumption technology s both fall to zero
t
at constant exponential rates, while σ → σ∗, and asymptotic growth is given
t
by:
λ(g +n)
g∗ = s > 0, (53)
A 1−φ
λn
g∗ = > g∗, (54)
B 1−φ A
g∗ = g (55)
h
ǫ−β
g∗ = g −(n+g) < g∗, g∗ > 0, (56)
c ǫ h c
g∗ = 0, (57)
δ
(1−γ)ρ+(1−γ)2g
δ → c , (58)
t
ǫ−1+γ
ǫ−β
g∗ = g∗ = − n < 0. (59)
s ℓ ǫ
Note that in this case M = 0. Also, ρ > (1−γ)g is required for our integral
∞ c
to stay bounded.
Proof. See Appendix A.7.
Unlike when ǫ < β, workers and scientists are shifted to safety even when
γ ≤ 1, not just the narrower class of preferences with γ significantly greater
than one as in Jones (2016). This is because even though the relative value
of life u˜ is bounded when γ ≤ 1, δ continues increasing because of the scale
t t
effect. When ǫ > 1−γ, δ v˜ would get too large without shifting resources, so
t t
labor and scientists are shifted to safety in the optimal allocation. Neverthe-
less, despite resources being shifted to safety, they are not shifted to safety
∞
quickly enough to bound δ ds, so the long-run probability of humanity’s
0 s
survival is M = 0 when γ ≤ 1.
∞
R
However, there is also another case when ǫ < 1−γ. Here, the elasticity
of the hazard rate is smaller than the elasticity of utility with respect to
consumption, so resources need not be all shifted to safety to bound δ v˜ ,
t t
and so the optimal allocation features balanced growth as in the rule of
thumb allocation and δ → ∞.
t

EXISTENTIAL RISK AND GROWTH 16
Proposition 7. Optimal growth with ǫ > β and γ < 1−ǫ
Assume that ǫ > β. Assume that the marginal utility of consumption falls
less rapidly, in the sense that γ < 1 − ǫ. (Note that we do NOT need to
assume that ǫ 6≫ β.) Then the optimal allocation features an asymptotic
constant growth path such that as t → ∞, δ → ∞, and the fraction of labor
t
working in the consumption sector ℓ and the fraction of scientists making
t
consumption ideas s both converge to constants strictly between 0 and 1. The
t
optimal allocation then features a balanced growth path as under the rule of
thumb allocation:
1−γ −ǫ
ℓ∗ = (60)
1−γ −ǫ+β
λn
g∗ = g∗ = , (61)
A B 1−φ
αλn
g∗ = g∗ = g ≡ , (62)
c h 1−φ
g∗ = (ǫ−β)(g +n) > 0, (63)
δ
δ → ∞. (64)
Proof. See Appendix A.8.
Critically, consider thecomparison ofthese optimal allocationsto therule
of thumb allocation. In the rule of thumb allocation when ǫ > β, δ → ∞
t
and M = 0 because of the scale effect of existential risk. By contrast, when
∞
γ > 1 − ǫ, resources are shifted to the safety sector in optimal allocation,
counteracting the scale effect. Thus, δ converges to a small constant or even
t
zero. Given γ > 1, the optimal allocation even features δ falling to zero
t
exponentially, and thus M > 0; however, if γ ≤ 1, M = 0. Nonetheless,
∞ ∞
if the marginal utility of consumption falls sufficiently slowly, i.e. γ < 1 −
ǫ, not all resources are shifted to the safety sector asymptotically and the
optimal allocation looks like the rule of thumb allocation, with the hazard
rate exploding.
The case of ǫ > β is thus a world in which existential risk is an enormous
challenge, but can still be overcome. With a static concern for safety, as in
the rule of thumb allocation, the scale effect portends disaster. By shifting
resources to safety, as in the optimal allocation for sufficiently curved pref-
erences, this scale effect can be contained; in fact, when γ > 1, even the
impatient optimal allocation features a nonzero probability of humanity’s
survival in the long run.

EXISTENTIAL RISK AND GROWTH 17
Finally, we take care of theknife edge scenario of γ = 1−ǫ, which involves
two subcases.
Proposition 8. Optimal growth with ǫ > β, γ = 1 − ǫ, and αλ <
1−φ
(ǫ−β)(1+ǫ)
βǫ
Assume that ǫ > β. Assume that the marginal utility of consumption falls,
but not as rapidly, in the sense that γ ≤ 1. Assume that the elasticity of the
hazard rate equals than the elasticity of utility with respect to consumption,
i.e. ǫ = 1 − γ. Finally, assume that αλ < (ǫ−β)(1+ǫ). Then the optimal
1−φ βǫ
allocation features an asymptotic constant growth path such that as t → ∞,
δ → ∞, while the fraction of labor working in the consumption sector ℓ and
t t
the fraction of scientists making consumption ideas s fall to zero exponen-
t
tially. σ → σ∗, and asymptotic growth is given by:
t
λ(g +n)
g∗ = s > 0, (65)
A 1−φ
λn
g∗ = > g∗, (66)
B 1−φ A
αλn
g∗ = g, g ≡ , (67)
h 1−φ
1
g∗ = g < g, g∗ > 0, (68)
c c
1+ǫ 1+ αλ
1−φ
g∗ = (ǫ−β(cid:16))n¯ +ǫg (cid:17)−βg > 0,δ → ∞ (69)
δ c h
g∗ = g∗ = −ǫg < 0. (70)
s ℓ c
Proof. See Appendix A.9.
Proposition 9. Optimal growth with ǫ > β, γ = 1 − ǫ, and αλ ≥
1−φ
(ǫ−β)(1+ǫ)
βǫ
Assume that ǫ > β. Assume that the marginal utility of consumption falls,
but not as rapidly, in the sense that γ ≤ 1. Assume that the elasticity of the
hazard rate equals than the elasticity of utility with respect to consumption,
i.e. ǫ = 1 − γ. Finally, assume that αλ ≥ (ǫ−β)(1+ǫ). Then the optimal
1−φ βǫ
allocation features an asymptotic constant growth path such that as t → ∞,
the fraction of labor working in the consumption sector ℓ and the fraction of
t
scientists working on consumption technology s both fall to zero at constant
t

EXISTENTIAL RISK AND GROWTH 18
exponential rates, while σ → σ∗, and asymptotic growth is given by:
t
λ(g +n)
g∗ = s > 0, (71)
A 1−φ
λn
g∗ = > g∗, (72)
B 1−φ A
g∗ = g, (73)
h
ǫ−β
g∗ = g −(n+g) < g∗, g∗ > 0, (74)
c ǫ h c
g∗ = 0, but δ → ∞ subexponentially, (75)
δ
ǫ−β
g∗ = g∗ = − n < 0. (76)
s ℓ ǫ
Proof. See Appendix A.10.
3.3 Certain Existential Catastrophe with ǫ ≫ β
Now, consider the case in which ǫ ≫ β, i.e. consumption goods are signif-
icantly more potent in increasing existential risk than safety goods are in
reducing it.
Now, there is no way to stop δ → ∞. To understand why this is the case,
t
note that in the Jones (1995) version of the Romer (1990) model, growth in
the long run is αλ n: the diminishing returns to R&D combined with the
1−φ
nonrivalry of ideas means that in the long run, the growth rate depends
on the growth rate of population. In our model, even if all workers and
scientists are shifted to working on safety asymptotically, the contribution of
safety growth to the growth rate of δ would be −β αλ n.
1−φ
At the same time, when ǫ > β in our model, existential risk increases
with scale: population growth increases scale and thus contributes (ǫ−β)n
to the growth rate of δ. The problem arises when (ǫ−β)n > β αλ n: then,
1−φ
even if everyone were to work on safety asymptotically and even if per capita
consumption were to stay constant, that cannot stop the hazard rate δ from
t
growing.
When ǫ−β > αλ , the scale effect of existential risk is larger than the
β 1−φ
scale effect of ideas. Thus, given exogenous population growth, there is no
way to stop δ → ∞ and M = 0. Even halting population growth and
t ∞
stagnating would only provide temporary relief: without population growth,
there is no growth in safety technology. δ would remain at a constant high
t

EXISTENTIAL RISK AND GROWTH 19
level, existential catastrophe follows eventually, and M = 0. Letting c
∞ t
fall exponentially could temporarily reduce existential risk, but eventually
life would be so miserable that extinction would be preferable to continued
existence. Inshort, whenǫ ≫ β,eventual existential catastropheisinevitable
regardless of what society does.
This case stands in stark contrast to the previous case when ǫ > β.
When the scale effect of existential risk is not too large, c → ∞ and, given
t
sufficiently curved preferences, M > 0. Even with a scale effect, existential
∞
risk could be overcome. When ǫ ≫ β, the scale effect of existential risk is
larger than the scale effects of ideas. A key factor here is αλ . If the returns
1−φ
tomoreresearch(φ)andmorepeopleworking onresearch (λ)donotdecrease
as rapidly, αλ is higher, and so a larger scale effect of existential risk can be
1−φ
dealt with.
In some sense, the world of ǫ ≫ β is the economist’s version of the Fermi
Paradox or the Doomsday Argument: the world is simply too fragile and
R&D too hard for existential risk to be overcome.
Now we come to the optimal allocations. Note that we already dealt with
thecase where γ ≤ 1−ǫ in theprevious section. In particular, when γ < 1−ǫ
(proposition 7), the asymptotic growth path features positive consumption
growth while s and ℓ converge to constants (while δ → ∞ with positive
t t t
g , as is unavoidable). Thus, when the diminishing returns to consumption
δ
fall sufficiently slowly, the relative concern for life is small enough that de-
spite ǫ ≫ β, the optimal allocation still doesn’t shift all resources to safety
asymptotically and consumption grows exponentially without bound.
In fact, this is the only ǫ ≫ β case where consumptions grows exponen-
tiallywithout bound. When γ > 1−ǫ, we have what we might call an“end of
growth” scenario (see the proposition below). Risk grows so rapidly with the
scale effect andthediminishing returns toconsumption arelargeenough that
the social planner chooses to eventually have consumption stagnate rather
than add even more risk. Note, however, that even stagnation cannot stop
δ → ∞ in the presence of population growth, so M = 0 (and as explained
t ∞
earlier, even stopping population growth would result in M = 0).
∞
In the below, I will call c∗ the level of consumption that c converges to
t
and stagnates at, and I will call c the level of consumption at which utility
0
is 0. c is an immiseration level of consumption; anything below that and
0
life is not worth living.
Proposition 10. Optimal growth with ǫ ≫ β and γ > 1−ǫ

EXISTENTIAL RISK AND GROWTH 20
Assume that ǫ ≫ β in the sense that ǫ−β > αλ . Assume that the marginal
β 1−φ
utility of consumption falls at least moderately rapidly, in the sense that γ >
1−ǫ. Then the optimal allocation features a constant asymptotic growth path
such that as t → ∞, consumption stagnates with g = 0 and c → c∗, δ → ∞,
c t
while the fraction of labor and scientists working in the consumption sector
ℓ and s fall to zero exponentially and σ → σ∗. Asymptotic growth is given
t t t
by:
λ(g +n)
g∗ = s > 0, (77)
A 1−φ
λn
g∗ = > g∗, (78)
B 1−φ A
g∗ = g, (79)
h
g = 0, c → c∗, (80)
c t
g = (ǫ−β)n−βg∗ > 0, δ → ∞, (81)
δ h
1
g∗ = g∗ = − g < 0, (82)
s ℓ (1+ αλ )
1−φ
with the value of c∗ depending on γ. If γ = 1, i.e. utility is logarithmic in
consumption,
1
c∗ = exp −u¯ , (83)
ǫ
(cid:18) (cid:19)
c∗ 1
= exp , (84)
c ǫ
0 (cid:18) (cid:19)
while if γ > 1 or 1 > γ > 1−ǫ:
1
1 + 1 γ−1
c∗ = ǫ γ−1 , (85)
u
" #
1
c∗ γ −1 γ−1
= +1 (86)
c ǫ
0 (cid:20) (cid:21)
Proof. See Appendix A.11.
We can then lookat the ratio of c∗ relative to c , i.e. how much higher the
0
level of consumption society stagnates at is than the immiseration level of

EXISTENTIAL RISK AND GROWTH 21
consumption. For example, if we think an immiseration level of consumption
corresponds to $300/year, and
c∗
= 10, then c∗ corresponds to consumption
c0
of $3000/year.
For example, for ǫ = 1/2 and γ = 2,
c∗
= 3, i.e. consumption converges
c0
to a level that is just three times higher than the immiseration level. For
the same ǫ but γ = 1,
c∗
≈ 7.4, i.e. consumption converges to a level that
c0
is about 7.4 times higher than the immiseration level. And for the same ǫ
but γ = 3/4,
c∗
= 16, i.e. consumption converges to a level that is 16 times
c0
higher than the immiseration level.
We see that
c∗
decreases with γ. Similarly,
c∗
decreases with ǫ. To
illustrate this, we
c
c
0
an look at a contour plot of
c∗
fo
c
r
0
different levels of γ and
c0
ǫ. (For technical reasons, the plot only shows parameter combinations that
result in
c∗
≤ 100.)
c0
Figure 1: The ratio of the “end of growth” level of consumption, c∗, relative
to the immiseration level of consumption, c , for different values of γ and ǫ
0
This“endofgrowth“scenariomightaccordwithsomecommonintuitions.

EXISTENTIAL RISK AND GROWTH 22
Perhaps economic growth and the technological innovations that come with
it are just too dangerous. Instead of continuing to grow indefinitely, it might
be optimal—even for an impatient society!—to halt consumption growth.
(Indeed, from per-capita perspective, it could even be optimal to halt—or
even reverse—population growth aswell, but populationgrowth isexogenous
in our model.)
It is worth keeping in mind, though, that the world in which the “end of
growth“ is optimal is also the world in which an existential catastrophe is
inevitable. The “end of growth” may slow the rise of risk, but an existential
catastrophe will destroy civilization soon anyway. From a “longtermist” per-
spective, i.e. fromtheperspective oftotal, non-discounted utilitarianwelfare,
is ultimately not much value in this world, since there is no chance of hu-
manity surviving—there is no potential for “astronomical value.” Even some
totalitarian state that forced population to fall exponentially and had c fall
t
to just above the immiseration level in the name of risk reduction would fail
to enable humanity’s survival: the last person alive couldn’t do enough R&D
to have δ (continue) to fall exponentially, so M = 0.
t ∞
Finally, we consider the knife-edge case for completeness.
Proposition 11. Optimal growth with ǫ−β = αλ and γ > 1−ǫ
β 1−φ
Assume that ǫ−β = αλ . Assume that γ > 1−ǫ. Then, the optimal allocation
β 1−φ
features an asymptotic growth path such that g = 0, g = 0, while the fraction
c δ
of labor and scientists working in the consumption sector ℓ and s fall to
t t
zero exponentially. In particular, note that in the case that γ ≤ 1, c can
t
still increase (subexponentially) without bound while δ → δ∗ < 1. In the case
t
that γ ≥ 1, c must still be bounded.
t
Proof. See Appendix A.12.
3.4 Summary
To provide an overview of the various optimal allocations, I have compiled
an overview of the asymptotic growth paths under different parameter values
below. For the sake of clarity, I have omitted the knife-edge cases.

EXISTENTIAL RISK AND GROWTH 23
Table 1: Overview of Optimal Allocations
ǫ<β ǫ>β ǫ≫β
gc =gh =g gc =gh =g
Rule of thumb
δt →0 δt →∞
allocation
M∞ >0 M∞ =0
st,ℓt →s∗,ℓ∗
Optimal
gc =gh =g¯>0
allocation with st, ℓt →1
δt →∞
smallest γ gc =g, gh <gc
M∞ =0
δt →0
M∞ >0 st, ℓt →0
Optimal
gc <gh, gh =g
allo
s
c
m
a
a
ti
l
o
le
n
r
w
γ
ith δt →δ∗ >0
g
st
c
,
=
ℓt
0
→
, ct
0
→c∗
M∞ =0
gh =g
st, ℓt →0 st, ℓt →0 δt →∞
Optimal
gc <gh, gh =g gc <gh, gh =g M∞ =0
allocation with
δt →0 δt →0
large γ
M∞ >0 M∞ >0
δ explodes under rule Doomed to existential
Existential risk δ exponentially decays
of thumb. Optimal catastrophe whatever
in rule of thumb under rule of thumb.
allocation can contain society does. Social
vs. optimal Optimal allocation
growth in δ and planner may choose
allocation changes pace of decay.
achieves positive M∞. “end of growth.”
4 Evidence on Parameters
To understand our results, we have to know what realistic parameter values
are and thus which world we live in. In particular, it would be very helpful
to know whether ǫ > β.
Evidence from broad trends in growth and existential risk
Over the past century, world economic output has grown manyfold. Tech-
nological risk to human civilization has arguably grown manyfold as well.
Nuclear winter, catastrophic climate change, and genetically-engineered pan-
demics are all risks that have emerged in the past century. The Bulletin of
Atomic Scientists, who publishes the “Doomsday Clock” assessing the likeli-
hood of existential catastrophe, puts it as follows:

EXISTENTIAL RISK AND GROWTH 24
Our species has never before in its 200,000-year history been so
close to a disaster as we are this century. Its unsettling enough
that the Doomsday Clock has been set to an ominous 3 minutes
to midnight (or doom) since 2015 [Note: 2 minutes to midnight
since 2018]. But the real gravity of our situation only comes into
focus once one realizes that before 1945, there was no need for
the Doomsday Clock in the first place, given the low probability
of doom. (Torres, 2016)
The key question then is what has happened to the fraction of safety
spending as fraction of total output. If safety spending has not decreased
as a fraction of total output, the functional form δ = δCǫHβ immediately
t t t
implies ǫ > β.
Regrettably, I have not been able to find good data on safety spending
as it is defined in this model. However, it seems like the effort spent on
mitigating existential risk was approximately none a century or two ago. For
example, nuclear disarmament and security, climate change abatement, and
research on AI safety are all efforts that began only in the past century, and
these efforts appear to be intensifying in the past decades. In that sense, it
appears that the fraction of output spent on safety has increased.
It would clearly be desirable to collect better data on both the level of
existential risk and the fraction of output spent on safety. Nevertheless, the
general trend appears to imply ǫ > β.
Evidence on αλ
1−φ
Jones and Romer (2010) give a broad and plausible range of αλ ∈ [1/2,2].
1−φ
Note that this figure is for the economy as a whole. The R&D production
function for the safety sector may be different, although we have no reason
to believe it is, and so our base case should be that the nature of R&D is
similar in both sectors. As such, I have imposed the same parameters on
both the consumption and safety ideas production function in this paper.
Moreover, recent research by Bloom et al. (2017) demonstrates relatively
sharply diminishing returns to research across a wide range of sectors using
micro-evidence, indicating a low αλ .
1−φ

EXISTENTIAL RISK AND GROWTH 25
Evidence on γ
Mostofthelargeempiricalliteratureonthecoefficientofrelativeriskaversion
suggests γ > 1 is the relevant case. See e.g. Lucas (1994) on asset pricing
and Chetty (2006) on labor supply. γ also traditionally equals the inverse
of intertemporal substitution. The traditional evidence here suggests values
well below one, implying γ well above 1; see Hall (2009) for a survey.
Evidence on ρ
Financial data reflecting consumer behavior tends to find pure time prefer-
ences in the range of 2%–5% (Pindyck, 2013). Weitzman (2007) finds data
roughly consistent with a ρ of 2%. Nordhaus uses a rate of pure time prefer-
enceof1.5%inhisseminalDICEclimatechangemodel(Nordhaus and Sztorc,
2013).
Implications
Our sparse evidence on the parameter values indicates that ǫ < β is unlikely,
and the ǫ > β world may well the one we live in. At the same time, the
ǫ ≫ β case appears surprisingly possible. If we take the high-end estimate
of αλ = 2, then an ǫ of 3/2 and a β of 1/2 would mean that ǫ ≫ β. If we
1−φ
look at the lower-end estimate of αλ = 1/2, which may be the more realistic
1−φ
number given recent evidence on the sharply diminishing returns to research,
even e.g. ǫ = 3/4 and β < 1/2, or ǫ = 1/2 and β < 1/3, would suffice for
ǫ ≫ β. Perhaps our efforts at mitigating existential risk do not matter much
after all—not because existential risk isn’t a problem, but because existential
catastrophe is inevitable whatever we do.
It would clearly be beneficial to get better empirical evidence on these
parameters. However, from now on, I will focus on the ǫ > β and ǫ 6≫ β
case. This appears to be the empirically likely case.
Perhaps more importantly though, this is the case in which the effect of
growth on risk is in doubt and this effect matters.
If ǫ < β, (faster) growth straightforwardly reduces risk.
If ǫ ≫ β, growth does increase risk, but in some sense it doesn’t matter
much: anexistential catastrophewill wipe out humanity soonanyway. Inthe
faceof parameter uncertainty, thevast majority ofthe valueof thefuture will
be in cases where ǫ 6≫ β, i.e. in cases where M > 0 and thus “astronomical
∞
value” is possible.

EXISTENTIAL RISK AND GROWTH 26
If ǫ > β (but ǫ 6≫ β), growth does not straightforwardly reduce risk—
without reallocation from consumption to safety, proportional growth in fact
increases risk. At the same time, it is possible for M > 0 and thus to attain
∞
“astronomical value.”
In addition, I will focus on the case where γ > 1. This appears to be the
empirically relevant case. Moreover, when ǫ > β and γ ≤ 1, we again get
M = 0 regardless of any intervention.
∞
5 Transition Dynamics
Theanalysissofarhasshedlightonthelong-runbehaviorofgrowthandrisk.
However, we live in a world far away from this asymptotic result. To under-
stand the relationship between growth and risk as it might apply to today, I
consider the transition dynamics of the (impatient) optimal allocation.
In particular, I analyze the case where γ > 1 and ǫ > β.
5.1 Laws of Motion in the Optimal Allocation
The transition dynamics of the optimal allocation can be studied as a system
of six differential equations in six “state-like” variables: s , ℓ , σ δ , y ≡ g ,
t t t t t At
and z ≡ g . With the addition of N , these variables then characterize
t Bt t
all other variables. They each converge to constant values: s∗ = 0, ℓ∗ = 0,
σ∗ = λαgB , δ∗ = 0, y∗ = g , and z∗ = g .
ρ+(γ−1)gc+(1−φ+λα)gB A B
ˆ
Let sˆ denote the growth rate of s, ℓ denote the growth rate of ℓ, and so
on.
Proposition 12. Laws of Motion in the Optimal Allocation
In the optimal allocation, our “state-like” variables s , ℓ , σ δ , y , and z
t t t t t t

EXISTENTIAL RISK AND GROWTH 27
grow according to following laws of motion:
λ 1−σ λ 1−s 1−σ
sˆ= αz (1−ℓ) −αy ℓ , (87)
1−λ σ 1−λ s σ
θ ((cid:13)A +ω θ (cid:13)B)
ˆ ℓ ℓ σ
ℓ = , (88)
1−ω ω θ
ℓ σ σ
σˆ = θ ((cid:13)B +ω ℓ ˆ ), (89)
σ σ
σ ℓ
δ ˆ = (ǫ−β) n−σˆ +α(ǫy −βz)+ℓ ˆ ǫ+β , (90)
1−σ 1−ℓ
(cid:18) (cid:19) (cid:18) (cid:19)
yˆ= λ(n+sˆ+σˆ)−(1−φ)y, (91)
s
zˆ= λ n−sˆ +σˆ −(1−φ)z, (92)
1−s
(cid:18) (cid:19)
where the following definitions have been used:
σ
ω = (γ −1+ǫ−β) , (93)
ℓ
1−σ
ℓ
ω = − (1+β)+ǫ , (94)
σ 1−ℓ
(cid:18) (cid:19)
(1−ℓ) 1+ 1−ℓ ǫ
ℓ β
θ = , (95)
ℓ (cid:16) (cid:17)
1+ γ −1+ǫ+β ℓ (1−ℓ) 1+ 1−ℓ ǫ
1−ℓ ℓ β
1−σ (cid:16) (cid:17)
(cid:0) (cid:1)
θ = , (96)
σ 1+(β −ǫ)σ −λ(1−σ)
u(c )
(cid:13)A = (β −ǫ)n+(1−γ −ǫ)αy +αβz −ρ−δ + t , (97)
v
t
s u(c ) 1−ℓ 1−σ
(cid:13)B = (1−λ) sˆ+(λ+β −ǫ)n+αβz −αǫy + t −αλz t ,
1−s v 1−s σ
t t t
(98)
and
u(c ) ℓ 1
t = βδu˜+ǫδu˜, u˜ = ucγ−1 + , (99)
v 1−ℓ t 1−γ
t
1
1 α −β ǫ−β
δ ℓ z 1−φ s 1− λ φ
δ 1−ℓ y 1−s
!
(cid:18) (cid:18) (cid:19) (cid:19)
c = (cid:16) (cid:17) . (100)
t (cid:0) (cid:1)
N
t
Proof. See Appendix A.13.

EXISTENTIAL RISK AND GROWTH 28
5.2 Numerical Simulation
Simulating this system of equations yields a candidate transition path for
each set of parameters. These candidate transition paths feature two broad
dynamics that emerge for different combinations of parameter values. The
first dynamic features growth rates of A and B (and thus c and h) that
start very high (with c very close to 0) and then fall to the steady state.
The second dynamic features growth rates of A and B (and thus c and h)
that start small and then rise over time to the steady state. In trying to
understand the long-term dynamics of our civilization, the latter appears
to be the relevant case. Over the period of recorded history, consumption
was initially broadly flat (but nonzero). Then, growth sped up. Thus, I
will focus on the second case. Although the exact dynamics depend on the
specific parameter values of course, the example below illustrates the central
qualitative features of this case.
I set γ = 1.5, ǫ = 0.4, β = 0.3, ρ = 0.02, and n = 1%. These are
meant to be reasonable values for illustration; other values produce similar
results. I choose the other parameter values, including φ, λ, δ, and u, to
target several stylized facts about the world. In particular, I seek to find
a year t with a value of life-year as a ratio to per capita consumption (u˜)
0
of 4 (corresponding e.g. to per capita consumption of $20,000 and a value
of a life-year of $80,000), in which consumption per capita grows at around
1 percent per year, around 95% of workers are in the consumption sector,
and the hazard rate is approximately 0.1%. This 0.1% rate of existential
catastrophe has become a relatively widely used benchmark; see Stern (2006)
and M´ejean et al. (2017, 2019).
This is not meant to be a formal calibration in any sense: we do not have
good information about many of the parameters. This exercise is merely
meant to illustrate the qualitative dynamics; the calibration helps us use a
reasonable set of parameters. Critically, note that the qualitative dynamics
of these results are similar for other parameter choices, such as different γ,
different ǫ and β, and different ρ. I explain the details of the simulation in
Appendix B.1.
Figure2showsthekeyallocationofworkersandscientists toconsumption
along the transition path. Figure 3 shows the growth rates of consumption
and safety along the transition path. Figure 4 shows the hazard rate δ along
the transition path.

EXISTENTIAL RISK AND GROWTH 29
Percent
100
90
80
70
60
50
40
30
20
10
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 2: The allocation along the transition path. Time 600 corresponds
to today and the values at this date are highlighted in the graph. A period
represents a year.
Consider first the allocation variables displayed in Figure 2. At the time
representing today, nearly all scientists and workers are in the consumption
sector. Asconsumptiongrowsandthustherelativevalueoflifeu˜grows, both
sandℓdeclineasresourcesareshiftedtothesafetysector. Notethatinitially,
safety is increased by shifting workers towards the safety sector; only later
are scientists shifted towards the safety sector. Both s and ℓ eventually settle
in to their asymptotic, exponential decline to zero. The share of scientists in
the population σ rises steadily to its steady-state value.

EXISTENTIAL RISK AND GROWTH 30
Growth rate
2%
1%
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 3: The growth rates along the transition path. Time 600 corresponds
to today and the values at this date are highlighted in the graph. A period
represents a year.
Next, consider the growth rates along the transition path in Figure 3.
The growth rates of consumption technology A and thereby consumption per
capita c rise steadily, accelerating from a low initial level to higher consump-
tion growth at the time representing today. We saw that as consumption
grows and the value of life rises, workers and scientists are shifted to the
safety sector. This causes the growth rate of A to level off and consumption
growth to slow, while the growth of safety per capita haccelerates. Note that
the additional safety growth is driven by shifting workers to the safety sector
at first; only after a while does the growth of safety technology B begin to
accelerate. All growth rates eventually converge to their constant asymptotic
values, with consumption growing significantly slower than safety. However,
consumption does continue growing at a constant exponential rate.

EXISTENTIAL RISK AND GROWTH 31
Percent
0.2
0.15
0.1
0.05
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 4: The hazard rate along the transition path. Time 600 corresponds
to today and the value at this date is highlighted in the graph. A period
represents a year.
Finally, consider perhaps the most interesting dynamic: the hazard rate
alongthetransitionpathinFigure4. Thekey qualitative dynamicisthatthe
hazard rate curve has an inverted U-shape. The hazard rate starts at a rela-
tively low level. Yet since ǫ > β, existential risk grows with scale, so δ grows.
This means that at the time representing today, the risk of an existential
catastrophe is much higher than it was hundreds of years ago. As consump-
tion grows, the value of life rises and so resources are shifted to safety. This
slows the growth rate of δ, yet existential risk keeps rising—the scale ef-
fect still dominates for a while. Eventually, the growth in safety relative to
consumption outpaces the scale effect, so the δ-curve bends: existential risk
starts to fall. The hazard rate δ ultimately decays exponentially.
Recall that what matters in determining the long-term probability of
∞
humanity’s survival is the area under the hazard rate, since M
∞
= e−R
0
δsds.
Theexponential decayofthehazardrateontheasymptoticpathensures that
∞
δ ds is finite, and so M > 0. Extrapolating from the simulation, the
0 s ∞
long-run probability of human civilization’s survival conditional on surviving
R

EXISTENTIAL RISK AND GROWTH 32
to the time that represents today is approximately 19.3%. However, note
that I calibrated the above simulation to have a δ of approximately 0.1%
today; a different calibration would rescale this curve and thus change the
magnitude of the survival probability.
5.3 Discussion: The Existential Risk Kuznets Curve
This inverted U-shape of the hazard rate curve is related to the literature on
the “environmental Kuznets curve,” which posits an inverted U-shape rela-
tionship between economic development and pollution(see Brock and Taylor
(2005) for an overview). The mechanism at work in this model is similar
to the classic Stokey (1998) paper on the theory behind the environmental
Kuznets curve: if γ > 1, richer societies care less about increasing consump-
tion and more about other things, such as the environment, or, in this case,
life. Initially, pollution rises with scale, but eventually declines as the rela-
tive value of environmental protection increases, producing a hump-shaped
pollution curve. While the matter at hand is very different—environmental
degradation that additively reduces utility versus existential catastrophes
that imperil human civilization—the analogy supports the soundness of the
result.
There are two important things to keep in mind, however, about what we
might call the “existential risk Kuznets curve.” First, the timescales involved
here appear to be very long, involving hundreds or even thousands of years
of economic development. Zooming in even a few hundred years around the
present in the graph above, we would likely only increasing risk, much as
some argue we have seen in the past century. On the one hand, this shows
the value of economic theory: it allows us to gain a long-run perspective on
potential societal dynamics. On the other hand, this means we cannot easily
test this model prediction empirically, giving us reason for caution.
Secondly, note that this existential risk Kuznets curve appears in the
transition dynamics of the optimal allocation. Considering that existential
risk mitigation is a global public good, it is unlikely resources are allocated
to safety optimally in the real world. As such, this should not be taken to be
a prediction of what a particular country with a particular set of institutions
will do with regard to existential risk.
Nevertheless, there are a number of reasons why we might still be inter-
ested in the transition dynamics under the (impatient) optimal allocation.
For one, since there are very long timescales involved here, it is very hard to

EXISTENTIAL RISK AND GROWTH 33
know (and thus model) what government and societal institutions will evolve
to deal with existential risk. However, the ideal these institutions will likely
aim at is the optimal allocation. The optimal allocation might thus be a
rough proxy for the real-world allocation.
Moreover, the (impatient) optimal allocationrepresents what I would call
the “democratic possibilities frontier” or the “impatient public possibilities
frontier.” Those who are principally concerned about the long-run future
of humanity and advocate for a zero rate of pure time preference might
want us to spend as much as possible on safety in order to avoid existential
catastrophe and enable human flourishing millions of years into the future.
Indeed, even in the Hamiltonian of the optimal allocation, the relative value
of life v˜ is a discounted term; the lower your discount rate ρ, the more
t
you would want to spend on safety. However, the broader public is not so
patient. As the empirical evidence cited earlier shows, people tend to have a
(relativelylarge)positiverateofpuretimepreference; thepublicisimpatient.
Even perfectly designed institutions that take into account existential risk
externalities will ultimately be constrained by the degree to which society
actually cares about the future—they will be constrained by an impatient
public. The existential risk Kuznets curve illustrates the implications of
this impatience. On the one hand, this impatience results in a period of
initially rising levels of risk. For example, this might mean that the arguably
rising level of existential risk of the past century is not necessarily a market
failure, but may well be part of the optimal path given positive pure time
preference. On the other hand, rising standards of living lead even the most
impatient public to start caring more aboutsafety andaverting an existential
catastrophe. This leads workers and scientists to be shifted to the safety
sector, eventually causing the hazard rate δ to exponentially decline. Even if
people are impatient, if you make them well off enough, they will start caring
about existential risk.
Seeing the arguably rising levels of existential risk in the past century,
some might call for an end to economic growth. Yet this existential risk
Kuznets curve indicates that stopping economic growthwould be deleterious:
it would simply freeze the hazard rate at a high level, leading to a fatal
catastrophe sooner or later. Economic growth enables even an impatient
public with a high rate of pure time preference to start caring about life,
thus ultimately reducing risk and even leading to positive M .
∞
Some prominent thinkers have previously posited that humanity is pass-
ing through a unique period with an elevated risk of technological catastro-

EXISTENTIAL RISK AND GROWTH 34
phe. Sagan (1994) calls this the “time of perils.” Parfit (2011, p. 616),
concurs:
We live during the hinge of history. Given the scientific and
technological discoveries of the last two centuries, the world has
never changed as fast. We shall soon have even greater powers to
transform, not only our surroundings, but ourselves and our suc-
cessors. If we act wisely in the next few centuries, humanity will
survive its most dangerous and decisive period. Our descendants
could, if necessary, go elsewhere, spreading through this galaxy.
This existential risk Kuznets curve provides theoretical evidence that
grounds the intuition that we are living in a “time of perils.” We may
be economically advanced enough to have created the means for our perma-
nent destruction, but not economically advanced enough to care enough about
decreasing this existential risk.
This “time of perils” has profound implications. For instance, those alive
today who care about preserving the long-term future of humanity may have
extraordinary altruistic leverage. By working to reduce existential risk now
(increasing the resources dedicated to safety), they canreduce the area under
the “hump” of the hazard rate δ. This in turn increases M , unlocking
∞
tremendous value. Moreover, since so few resources arededicated to safety at
the moment, there are likely very high marginal value opportunities available
to work on safety. This is a unique situation. Suppose existential risk did
not decline to zero exponentially: then M = 0 regardless—the existential
∞
risk curve would never bend—so reducing risk now would not change the
probability of a long and flourishing future of humanity. And if existential
risk did not initially increase, it would never be such a substantial challenge
and there wouldn’t be such high marginal value opportunities to work on
reducing it.
6 Does Faster Growth Increase the Probabil-
ity of Existential Catastrophe?
Faster economic growth is conventionally seen as a great boon for humanity.
Yet when considering existential risk, this picture becomes more muddled.

EXISTENTIAL RISK AND GROWTH 35
Faster economic growth might speed up the development of potentially dan-
gerous technology, such as powerful AI, or accelerate the pace of climate
change. What if faster economic growth—in a world that does not (yet)
value life highly—also accelerates the growth in risk? Could the side effect of
mundane efforts to e.g. make trade more efficient or increase labor force par-
ticipation be increasing the probability of an existential catastrophe? While
the existential risk Kuznets curve explicated in the last section suggests we
shouldatleast wantsomeeconomicgrowthevenfromtheperspectiveofmax-
imizing M , this does not tell us anything about how the pace of economic
∞
growth affects the probability of an existential catastrophe.
First, consider a generic, uniform shock—e.g. more people working—on
the balanced growth path of the rule of thumb allocation. Since the fraction
of workers and scientists working in the safety sector is fixed, this increases
the number of scientists and workers in the safety sector and consumption
sector by the same proportion. If ǫ < β, this shock therefore decreases the
hazard rate δ. If ǫ = β, there is no effect on δ. But if ǫ > β, the shock
increases the hazard rate δ because of the scale effect.
When ǫ < β, faster growth reduces existential risk even in the rule of
thumb allocation. Yet when ǫ > β, accelerating growth also accelerates the
growth in risk if the allocation of resources to safety does not adjust.
I will look at what happens when we accelerate growth in the (impatient)
optimal allocation. In particular, I will look at the ǫ > β case, since in the
ǫ < β case, faster growth reduces risk even when the allocation of resources
to safety does not adjust. As explained earlier, although the real-world allo-
cation may be imperfect, the optimal allocation might be a rough proxy for
how societies will decide to allocate resources to safety inthe long run. More-
over, theoptimal allocationrepresents the“democraticpossibilities frontier”:
the (high) positive rate of pure time preference the public appears to have
dictates the degree to which societies can trade off consumption for safety. I
also focus on the γ > 1 case as in the previous section.6
6.1 Simulating an Acceleration of Growth
First, consider what happens when growth is faster for a given time period,
resulting in permanently higher economic output (i.e. this results in a per-
6 Note that if γ ≤ 1, accelerating growth would not matter for the chances of human
civilization’s survival in the long run: M∞ = 0 anyway, regardless of whether growth is
faster or slower.

EXISTENTIAL RISK AND GROWTH 36
manent level effect).
In this model, population growth is the driving force behind economic
growth. More population means more nonrival ideas which means more
output. Moreover, it easy to manipulate population growth in our model by
manipulating n. Thus, I consider the effect of accelerated populationgrowth.
In particular, I simulate 2% (instead of 1%) population growth for 30 years
around the time representing today. We can take this to literally represent
theeffectofsomepro-natalistpolicy. However, thebasicdynamics illustrated
below should apply to a broad class of generic accelerations in growth, e.g.
increasing labor force participation, increasing human capital, increasing the
number of “effective” people by making global exchange easier, or increasing
research effort.
See Appendix B.2 for details of how I simulate the acceleration in growth.
The following figures compare the transitionpathwith steady growthand
the transition path with a period of accelerated growth. The transition path
with steady growth is depicted with the solid colors; the transition path with
a period of accelerated growth is depicted with the lighter colors. Figure 5
shows the growth rates of consumption and safety along the transition path.
Figure6showsthefractionofworkersandscientistsallocatedtoconsumption
along the transition path. Figure 7 shows the relative value of life u˜ along
the transition path. Figure 8 shows the hazard rate δ along the transition
path.

EXISTENTIAL RISK AND GROWTH 37
Growth rate
2%
1%
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 5: The growth rates along the transition path, comparing steady
growth (solid colors) and a period of accelerated growth (lighter colors). A
period represents a year.
Consider first the growth rates depicted in Figure 5. At around time 600,
population growth accelerates for 30 years. This accelerates the growth rates
of consumption technology A and safety technology B on the transition path
with the accelerated growth. Both growth rates remain higher for a while,
untiltheyeventuallyconvergetothesamesteadystateasalongthetransition
path with steady growth. The higher growth rates of A and B increase the
growth rates of c and h. g and g are thus higher on the transition path
c h
with a period of accelerated growth, until these too converge to the same
steady state as along the transition path with steady growth. Note that
consumption growth actually initially decelerates a bit during the period of
accelerated population growth to compensate for the scale effect of faster
population growth.

EXISTENTIAL RISK AND GROWTH 38
Percent
100
90
80
70
60
50
40
30
20
10
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 6: The allocation along the transition path, comparing steady growth
(solid colors) and a period of accelerated growth (lighter colors). A period
represents a year.
Next, consider thekey allocationvariablesshown inFigure6. Thegrowth
of the share of researchers in the population slightly increases during the
period of accelerated growth. More importantly, along the transition path
with the period of accelerated growth, workers and scientists are shifted to
to safety earlier than along the transition path with steady growth.

EXISTENTIAL RISK AND GROWTH 39
Relative value of life
100
90
80
70
60
50
40
30
20
10
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 7: The relative value of life u˜ along the transition path, comparing
steady growth (solid green) and a period of accelerated growth (light green).
A period represents a year.
To understand the dynamics at play, consider Figure 7, which compares
the relative value of life u˜ along the transition path with accelerated and
steady growth. At approximately time 600, when there is a period of faster
population growth, u˜ begins to diverge along the two transition paths. After
time 600, u˜ is higher along the transition path with accelerated growth com-
pared to along the transition path with steady growth. Recall the growth
rates illustrated in Figure 5: the acceleration of growth meant faster con-
sumption growth. Faster consumption growth in turn means that along the
transition path with accelerated growth, people are richer, earlier, than they
would have been with steady growth. Since u˜ = u(c) = ucγ−1 + 1 and
u′(c)c t 1−γ
γ > 1, these richer people then value life more highly; they are more con-
cerned for safety, earlier. Thus, resources are shifted to safety earlier, as we
saw in the allocation dynamics.

EXISTENTIAL RISK AND GROWTH 40
Percent
0.2
0.15
0.1
0.05
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 8: The hazard rate along the transition path, comparing steady
growth (black) and a period of accelerated growth (gray). A period rep-
resents a year.
Consider the hazard rate δ depicted in Figure 8. After the period of
accelerated growth around time 600, it initially seems as if all of the wor-
ries about faster economic growth have been confirmed: the acceleration in
growth also accelerates the growth in the hazard rate. This is all an observer
at the time—or even hundreds of years later—would be able to observe.
Armed with empirical data, this observer would conclude that faster growth
increased existential risk.
Yet zooming out, this is not so. The acceleration of growth also acceler-
ates the rise of the relative value of life u˜. As such, v˜ is higher: people start
t
caring more about safety earlier in the world with a period of accelerated
growth compared to the world with steady growth. Resources are shifted to
safety sooner, and thus the hazard rate curve bends earlier. In a sense, the
period of faster growth accelerates the movement along the existential risk
Kuznets curve. As a result, the overall area under the hazard rate curve is
lower—and recall that this is all that matters for the long-run probability of
civilization’s survival.

EXISTENTIAL RISK AND GROWTH 41
As before, on the steady growth transition path, M conditional on sur-
∞
viving to the time that represents today is approximately 19.3%. However,
on the transition path with a period of accelerated growth, M conditional
∞
onsurviving tothetimethat represents todayisapproximately 20.8%. Thus,
we see how the period of accelerated growth, despite increasing risk initially,
improves the changes of humanity’s survival in the long run! This effect is
not trivial: faster growth for a relatively short period of time now appears
to result in increasing the long-run probability of human survival by 1.5 per-
centage points. Instead of faster economic growth being a problem in the
context of existential risk, this suggests that faster economic growth could
actually contribute to the challenge of mitigating existential risk—even when
people are impatient.
When previously discussing the existential risk Kuznets curve, I men-
tioned that we may well be living through a “time of perils.” This analysis
suggests that one way to increase the probability of humanity’s survival is
to simply try to get through the “time of perils” as quickly as possible.
This may counterintuitively mean accelerating the increase in existential risk
initially (if we are currently on the upward-sloping part of the hazard rate
curve). However, this accelerationist strategy would ultimately decrease the
area under the hazard rate curve and increase the probability of a long,
flourishing future.
Thereverse oftheabovehappenswhengrowthdecelerates: themovement
along the existential risk Kuznets curve decelerates, and society is stuck with
higher levels of existential risk for longer, in turn dramatically decreasing the
long-run probability of humanity’s survival. Slower growth—even just for
a while—doesn’t just mean lower living standards, but potentially a much
higher chance of an existential catastrophe and a much lower chance of a long
futureof humanity. This should strike fear of even short-term stagnationinto
the hearts of all those who care about the long-term future.
The key condition here is that ǫ 6≫ β. The acceleration of growth initially
increases risk due to the scale effect—but since the scale effect of ideas is
larger than the scale effect of existential risk, it was still possible to mitigate
risk eventually once u˜ got high enough and people started caring. Yet if
ǫ ≫ β, the higher u˜ does not matter: even if society wanted to mitigate the
additional risk later on, it would be impossible.

EXISTENTIAL RISK AND GROWTH 42
6.2 Simulating a Transitory Boom
So far, we have been looking at an acceleration in growth that results in a
permanent level effect. What happens when we have a transitory economic
boom, i.e. a time of faster growth that doesn’t change the long-run level
of output? For the reasons stated before, we again manipulate population
growth, letting it be 2% for 40 years and then 0% for the 40 years after that
(instead of a steady 1%). Thus, the long-run population is unaffected; there
is simply a temporary upward blip. We may interpret this literally as the
effect of a transitory baby boom. However, the basic dynamics illustrated
below should apply to a broader class of transitory booms, e.g. an economic
boom as part of the business cycle in which the economy is operating over
capacity.
See Appendix B.2 for details of how I am simulating the acceleration in
growth.
The following figures compare the transitionpathwith steady growthand
the transition path with a transitory boom. The transition path with steady
growth is depicted with the solid colors; the transition path with a transitory
boom is depicted with the lighter colors. Figure 9 shows the growth rates
of consumption and safety along the transition path. Figure 10 shows the
key allocation of workers and scientists to consumption along the transition
path. Figure 11 shows the hazard rate δ along the transition path.

EXISTENTIAL RISK AND GROWTH 43
Growth rate
2%
1%
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 9: The growth rates along the transition path, comparing steady
growth (solid colors) and a transitory boom (lighter colors). A period repre-
sents a year.
Consider first the growth rates shown in figure 9. The faster population
growth initially accelerates the growth rates of both consumption technology
A and safety technology B. Growth in both of these then slows down when
population growth is slower during the time of slower population growth.
The upward blip in the growth rates of A and B in turn lead to an upward
blip in the growth rates of c and h. Nevertheless, after the temporary boom,
all growth rates are the same, as had the boom not happened.

EXISTENTIAL RISK AND GROWTH 44
Percent
100
90
80
70
60
50
40
30
20
10
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure10: Theallocationalongthetransitionpath,comparingsteadygrowth
(solid colors) and a transitory boom (lighter colors). A period represents a
year.
Next, consider the key allocation variables depicted in figure 10. There is
atemporaryupward blip inthefractionof populationworking asresearchers.
There is also a temporary downward blip in the fraction of workers and
researchers working in the consumption sector. Yet unlike when growth was
accelerated resulting in a permanent level effect, this temporary economic
boom does not change the long-term trajectory of the relative value of life;
thus, the long-term trajectory of the allocation variables is unchanged.

EXISTENTIAL RISK AND GROWTH 45
Percent
0.2
0.15
0.1
0.05
0
0 200 400 600 800 1000 1200 1400 1600
Time
Figure 11: The hazard rate along the transition path, comparing steady
growth (solid black) and a temporary boom (gray). A period represents a
year.
Consider the hazard rate illustrated in figure 11. The long-run trajectory
of the hazard rate is the same.
Nevertheless, this doesn’t mean that temporary boomhas no effect: there
isanupward blip inthehazardrateduring theboom. Recall againthatwhat
matters in determining the long-term probability of humanity’s survival is
the area under the hazard rate curve. This upward blip in the hazard curve
increases the area under the hazard curve, which reduces humanity’s long-
term survival probability. Extrapolating from the simulation, conditional
on surviving until the time representing today, the difference in long-term
survival probabilities is approximately 0.17 percentage points. Considering
this may just be the effect of e.g. the business cycle, and the outcome at
stake is whether humanity goes extinct or not, this is again a surprisingly
large effect.
The opposite occurs when we simulate a temporary bust, i.e. a slow-
down in (population) growth followed by an increase in growth such that
the long-term trend remains the same. Then, the hazard rate curve exhibits

EXISTENTIAL RISK AND GROWTH 46
a downward blip, which increases the long-term probability of humanity’s
survival.
We previously saw that a period of accelerating growth can increase the
long-term probability of humanity’s survival. Here, we thus add important
nuance: the additional growth has to result in a permanent level effect. Sim-
ply “juicing” growthfor a while may actually backfire, reducing the probabil-
ity of humanity’s survival. Nevertheless, the intuition we developed remains
the same: we want to get through the “time of perils” as quickly as possible.
Stagnation—in this case the “cooling off” after a transitory boom—during
the “time of perils” is deleterious.
6.3 Patience vs. Growth
The key mechanism at work in this paper is that growing consumption grows
people’s relative value of life u˜ (when γ > 1). The period of accelerated
growth improves the chances of civilization’s survival in the long run because
it accelerates the rise in the relative value of life u˜. As people grow richer,
theycaremoreaboutpreventing anexistential catastropheanddemandmore
safety.
By contrast, philosophers who are concerned about the long-term future
often appeal to ethical arguments for a zero rate of pure time preference.
They care about existential risk mitigation not because of a high u˜, but
because of low or no utility discounting.
How do the these two mechanisms—increasing consumption vs. reducing
the rate of pure time preference ρ—compare in terms of increasing concern
for safety?
Recall that in the optimal allocation,
1−ℓ βδ v˜
t t t
= ,
ℓ 1−ǫδ v˜
t t t
1−s βδ v˜ ρ−g −φg g
t = t t · pat At · Bt .
s 1−ǫδ v˜ ρ−g −φg g
t t t pbt Bt At
Both the allocation of workers to safety and the allocation of scientists to
safety are proportional to v˜. v˜ represents people’s demand for safety. Recall
t t
that
u˜ u(c )
t t
v˜ = , u˜ = .
t ρ−δ +g t u′(c )c
t vt t t

EXISTENTIAL RISK AND GROWTH 47
We see that people’s concern for life depends on both u˜, which in turn de-
pends on consumption, and ρ.
Thus, we can compare how lowering ρ—making people more patient—
and increasing c —making people better off and thus increasing u˜—compare
t
in terms of increasing v˜, people’s concern for life. Although this concern for
life does not necessarily translate directly to the allocation of resources to
safety in the real world as it does in the optimal allocation, we would hope
that the real-world allocation responds to the people’s demand for safety in
the long run.7
Proposition 13. Elasticities of Concern for Life
Suppose the marginal utility of consumption falls rapidly, such that γ > 1.
Let Ev˜ be the elasticity of v˜ with respect to ρ. Let Ev˜ be the elasticity of v˜
ρ c
with respect to c . As u˜ → ∞ and δ → 0,
t
Ev˜ → −1, (101)
ρ
Ev˜ → (γ −1). (102)
c
In particular, when u˜ is large and δ is sufficiently smaller than ρ, Ev˜ ≈ −1
ρ
and Ev˜ ≈ (γ −1).
c
Proof. See Appendix A.14.
For large enough u˜ (i.e. people are already decently well off and care
about life somewhat), the elasticity of v˜ with respect to ρ is approximately
−1. Halving ρ roughly doubles the concern for life v˜. Moreover, the elasticity
ofv˜withrespecttocisapproximately(γ−1). Forexample, ifγ = 2,doubling
croughlydoublestheconcernforlifev˜. Thelargerγ, thelargerthiselasticity,
since a larger γ means the marginal utility of consumption decreases more
rapidly and so the relative value of life u˜ increases more rapidly.
I have computed the approximate elasticities for different values of γ
below. To help clarify the comparison, in the third column, I note what ρ
would have to be reduced to, from a base of ρ = 2%, to match the increase
in the concern for life v˜ from a doubling of consumption.
t
7Note that when I am referring to ρ, this ρ is the rate of pure time preference without
regard for increasing population. In a total utilitarian setting, the rate of pure time
preference is ρ+n. Thus, the elasticities with regard to the rate of pure time preference
in a total utilitarian setting would be lower if n>0.

EXISTENTIAL RISK AND GROWTH 48
Table 2: Patience vs. Growth: Comparison of Effect on Concern for Safety
γ Ev˜ ρ equivalent to doubling consumption
c
1.1 0.1 1.87%
1.5 0.5 1.41%
2 1 1%
4 3 0.25%
For γ close to 1, even doubling consumption is equivalent only to a small
change in pure time preference in terms of regard for safety. Increasing
consumption is relatively ineffective in increasing people’s concern for safety.
Yet for larger γ, increasing consumption has very large effect on the concern
for safety—equivalent to very large reductions in pure time preference.
Note that I have been using an approximation for the elasticities that
is valid for sufficiently large u˜. For lower u˜, g is higher, so Ev˜ is lower.
vt ρ
At the same time, for lower u˜, Ev˜, is higher—in fact, Ev˜ → ∞ as u˜ → 0.
c c
This indicates that the above numbers are a lower bound for the relative
effectiveness of growing c versus lowering ρ. If people are poorer and u˜ is
lower, increasingcismuchmoreeffective relativetodecreasing ρinincreasing
the concern for safety than the numbers above imply.
Nevertheless, the general takeaway is clear. Making people better off
could increase concern for safety and thus demand for existential risk miti-
gation in a way that would be equivalent to significant changes in people’s
attitude toward the future.
7 Conclusion
Human activity can create or mitigate existential risks. Analyzing this in
a model of endogenous growth, when the scale effect of existential risk is
moderate and the marginal utility of consumption declines quickly enough,
this paper grounds the intuition of some prominent thinkers that humanity
may be in a critical “time of perils.” We may be economically advanced
enoughtobeabletodestroyourselves, butnoteconomicallyadvancedenough
that we care about this existential risk and spend on safety. This “time of
perils” implies that working on reducing existential risk now could be very
impactful from an altruistic perspective.

EXISTENTIAL RISK AND GROWTH 49
Faster economic growth appears to generally improve the odds of human-
ity’s survival. When the world is not very fragile, growth straightforwardly
reduces risk. When the world is extremely fragile, growth increases risk, but
humanity is doomed to destruction anyway—the odds of humanity’s survival
arezeroanyway. Inthemoderatefragilitycase, fastereconomicgrowth, while
initially increasing risk, can help us get through this “time of perils” more
quickly andthus increases the long-runprobability of humanity’s survival. In
particular, note that this effect doesn’t require a permanently higher growth
rate; the improvement in humanity’s odds of survival are potentially sub-
stantial even for a temporary period of faster growth. Conversely, even a
temporary period of slow economic growth—as we have arguably been expe-
riencing in the developed economies in recent decades—could substantially
curtail the future of human civilization.
This model suggests even if you care only about the very long-termfuture
of humanity, the pace of economic growth in the short run could be key to
whether we make it there.
This paper suggests many future research directions. It would clearly
be desirable to get better empirical data on the scale effect of existential
risk. More broadly, a better understanding of how exactly existential risk is
created and mitigated—and therefore modeled—would be helpful. It would
also be interesting to look at the implications of a decentralized allocation, as
well as possible mechanisms to efficiently provide for the global public good
of existential risk mitigation. Finally, from the perspective of maximizing
altruistic impact, it would be valuable to compare the impact on the long-
run probability of humanity’s survival from working on policies that might
accelerate the rate of growth to direct work on reducing existential risk by
funding the safety sector.

EXISTENTIAL RISK AND GROWTH 50
Appendices
A Proofs and Derivations
A.1 Proof of Proposition 1
Note that
A˙ Sλ
g = t = at (103)
At A A1−φ
t t
Given that S is a fixed fraction of the total population, the numerator
at
grows at rate λn. The denominator grows at (1 − φ)g . Given that on a
At
balanced growth path, g must be constant, the numerator and denominator
A
must grow at the same rate, yielding
λn
g = (104)
A
1−φ
The same reasoning applies to g , giving us
B
λn
g = (105)
B
1−φ
Now, note that C = AαL . Given that L is a fixed fraction of the total
t t ct ct
population, C grows at rate αg + n. Given c = C /N , c grows at rate
t At t t t t
αg . Thus, on the balanced growth path,
At
αλn
g = αg = (106)
c A 1−φ
The same reasoning applies to g , so
h
αλn
g = αg = (107)
h B 1−φ
Finally, consider what happens to δ = δNǫ−βcǫh−β. It follows directly
t t t t
that g = (ǫ−β)n+ǫg −βg . Thus, on the balanced growth path
δt ct ht
αλn αλn αλn
g = (ǫ−β)n+ǫ −β =⇒ g = (ǫ−β) +n (108)
δ 1−φ 1−φ δ 1−φ
(cid:18) (cid:19)

EXISTENTIAL RISK AND GROWTH 51
A.2 First Order Conditions of the Hamiltonian
FOC: s
t
∂H
0 =
∂s
t
=⇒ 0 = λsλ−1p σλNλAφ −λ(1−s )λ−1p σλNλBφ
t at t t t t bt t t t
=⇒ λp A˙ s−1 = λp B˙ (1−s )−1
at t t bt t t
1−s p B˙
=⇒ t = bt t (109)
s p A˙
t at t
FOC: ℓ
t
∂H
0 =
∂ℓ
t
∂
=⇒ 0 = (M u(c )−v δ M )
t t t t t
∂ℓ
t
∂ (Aαℓ (1−σ ))1−γ ∂
=⇒ M (u+ t t t ) = M v δNǫ−β ([Aαℓ (1−σ )]ǫ[Bα(1−ℓ )(1−σ )]−β)
t ∂ℓ 1−γ t t t ∂ℓ t t t t t t
t t
(1−γ)(Aαℓ (1−σ ))−γAα(1−σ )
=⇒ t t t t t = v δNǫ−βǫ[Aαℓ (1−σ )]ǫ−1Aα(1−σ )
1−γ t t t t t t t
[Bα(1−ℓ )(1−σ )]−β
t t t
+v δNǫ−β(−β)[Bα(1−ℓ )(1−σ )]−β−1
t t t t t
Bα(1−σ )(−1)[Aαℓ (1−σ )]ǫ
t t t t t
=⇒ u′(c )c ℓ−1 = v δNǫ−βǫℓ−1cǫh−β +v δNǫ−ββ(1−ℓ )−1h−βcǫ
t t t t t t t t t t t t t
=⇒ u′(c )c ℓ−1 = v δ (ǫℓ−1 +β(1−ℓ )−1)
t t t t t t t
(1−ℓ ) v (1−ℓ )
=⇒ t = t δ (ǫ t +β)
t
ℓ u′(c )c ℓ
t t t t
v (1−ℓ ) v
=⇒ (1−ǫδ t ) t = βδ t
t u′(c )c ℓ t u′(c )c
t t t t t
(1−ℓ ) v v
=⇒ t = βδ t (1−ǫδ t )−1
t t
ℓ u′(c )c u′(c )c
t t t t t
(110)

EXISTENTIAL RISK AND GROWTH 52
Consider the term vt : it is shadow value of life divided by the value
u′(ct)ct
of consumption in util terms. It thus represents the relative value of life, and
it is convenient to define this explicitly:
v
v˜ ≡ t (111)
t
u′(c )c
t t
giving us:
1−ℓ βδ v˜
t t t
= (112)
ℓ 1−ǫδ v˜
t t t
Note that this is a very logical condition: the ratio of workers is propor-
tional to what these workers can produce. In the numerator is the hazard
rate times the relative value of life times β (the effectiveness of safety goods
in reducing existential risk)—this is what can be gained by making a safety
good. In the denominator is 1 (which is value of consumption relative to v˜)
t
minus the existential risk increasing effects of consumption.
FOC: σ
t
∂H
0 =
∂σ
t
∂ (Aαℓ (1−σ ))1−γ
=⇒ 0 = M (u+ t t t )+λσλ−1p sλNλAφ
t ∂σ 1−γ t at t t
t
∂
+λσλ−1p (1−s )λNλBφ −M v δNǫ−β ([Aαℓ (1−σ )]ǫ[Bα(1−ℓ )(1−σ )]−β)
t at t t t t t ∂σ t t t t t t
t
1−γ λp A˙ +λp B˙
=⇒ 0 = M (Aαℓ (1−σ ))−γAαℓ (−1)+ at bt
t 1−γ t t t t t σ
−M v δNǫ−βǫ[Aαℓ (1−σ )]ǫ−1(−1)Aαℓ [Bα(1−ℓ )(1−σ )]−β
t t t t t t t t t t t
−M v δNǫ−β(−β)[Bα(1−ℓ )(1−σ )]−β−1(−1)Bα(1−ℓ )[Aαℓ (1−σ )]ǫ
t t t t t t t t t t t
M u′(c )c +v M βδ −v M ǫδ λ(p A˙ +p B˙)
=⇒ t t t t t t t t t = at bt
1−σ σ
t t
˙ ˙
σ λ(p A+p B)
=⇒ t = at bt (113)
1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t

EXISTENTIAL RISK AND GROWTH 53
FOC: M
t
∂H/∂M +v˙
t t
ρ =
v
t
v˙ 1
=⇒ ρ = t + [u(c )−v δ ] (114)
t t t
v v
t t
FOC: A
t
∂H/∂A +p˙
t at
ρ =
p
at
p˙ 1 1−γ
=⇒ ρ = at + [M (Aαℓ (1−σ ))−γαAα−1ℓ (1−σ )+φAφ−1p sλσλNλ
p p t 1−γ t t t t t at t t t
at at
−M v δNǫ−β(Bα(1−ℓ )(1−σ ))−βǫ(Aαℓ (1−σ ))ǫ−1αAα−1ℓ (1−σ )]
t t t t t t t t t t t
p˙ 1 c A˙ δ
=⇒ ρ = at + [M u′(c )α t +p φ t −αǫv M t ] (115)
t t at t t
p p A A A
at at t t t
FOC: B
t
∂H/∂B +p˙
t bt
ρ =
p
bt
p˙ 1
=⇒ ρ = bt + [φBφ−1p (1−s )λσλNλ
p p bt t t t
bt bt
−M v δNǫ−β(Aαℓ (1−σ ))ǫ(Bα(1−ℓ )(1−σ ))−β−1(−β)αBα−1(1−ℓ )(1−σ )]
t t t t t t t t t t t
p˙ 1 B˙ δ
=⇒ ρ = bt + [p φ t +αβv M t ] (116)
bt t t
p p B B
bt bt t t
Transversality Conditions
Note that the three standard transversality conditions apply:
lim[e−ρt ·v M ] = 0 (117)
t t
t→∞
lim[e−ρt ·p A ] = 0 (118)
at t
t→∞
lim[e−ρt ·p B ] = 0 (119)
bt t
t→∞

EXISTENTIAL RISK AND GROWTH 54
The Price of Ideas
To solve for the allocation of scientists (see FOC: s ), I need to solve for the
t
relative price of ideas p /p . To do this, I manipulate FOC B :
bt at t
p˙ 1 B˙ δ
bt t t
ρ = + [p φ +αβv M ]
bt t t
p p B B
bt bt t t
p˙ B˙ 1 δ
=⇒ ρ− bt −φ t = [αβv M t ]
t t
p B p B
bt t bt t
αβv M δ /B
=⇒ p = t t t t (120)
bt
ρ−g −φg
pbt Bt
Similarly, I manipulate FOC A :
t
p˙ 1 c A˙ δ
ρ = at + [M u′(c )α t +p φ t −αǫv M t ]
t t at t t
p p A A A
at at t t t
p˙ A˙ 1 c δ
=⇒ ρ− at −φ t = [M u′(c )α t −αǫv M t ]
t t t t
p A p A A
at t at t t
αM (u′(c )c −ǫδ v )/A
=⇒ p = t t t t t t (121)
at
ρ−g −φg
pat At
Combining the two, the relative price must satisfy:
p B βδ v ρ−g −φg
bt t = t t · pat At (122)
p A u′(c )c −ǫδ v ρ−g −φg
at t t t t t pbt Bt
Putting this in terms of the previously defined relative value of life v˜ I
t
get:
p B βδ v˜ ρ−g −φg
bt t = t t · pat At (123)
p A 1−ǫδ v˜ ρ−g −φg
at t t t pbt Bt
There needs to be a condition on ρ to keep the denominators positive.

EXISTENTIAL RISK AND GROWTH 55
Allocation of Scientists
Recall from FOC: s that:
t
1−s p B˙
t bt
=
s p A˙
t at
I can now substitute in the relative price of ideas:
1−s βδ v˜ ρ−g −φg g
t = t t · pat At · Bt (124)
s 1−ǫδ v˜ ρ−g −φg g
t t t pbt Bt At
Recall from FOC: ℓ that (1 − ℓ )/ℓ = (βδ v˜)/(1 − ǫδ v˜), so both of
t t t t t t t
these key allocation variables depend on δ v˜, that is, on the race between
t t
the decline in the hazard rate and the possible rise in the value of life relative
to consumption.
Note that in Jones (2016), (1 − ℓ )/ℓ and (1 − s )/s are instead pro-
t t t t
portional simply to βδ v˜. Incorporating the existential risk effects of higher
t t
consumption, there is a (much) higher allocation of labor and of scientists
to safety, in particular in the case that the value of life rises faster than the
hazard rate falls, i.e. δ v˜ rises.
t t
Moreover, our model introduces an additional constraint. Since ℓ is the
t
fraction of labor allocated to consumption, it must be that 0 < ℓ ≤ 1 (where
t
the strict inequality comes from the fact that at least some labor must be
allocatedtoconsumption alongthebalancedgrowthpath). Thus, (1−ℓt) must
ℓt
be finite, i.e. the denominator cannot be 0. Given that ǫ, β, δ , and v˜ are
t t
guaranteed to be positive, along the optimal path:
1
δ v˜ < (125)
t t
ǫ
Thisforeshadowswhatwillhappenalongthebalancedgrowthpath: given
the parameters of our preferences, either δ falls to 0 more quickly than v˜
t t
grows, in which case δ v˜ falls to 0, or δ v˜ asymptotically approaches 1/ǫ.
t t t t
Characterizing v˜
t
Using FOC: M , I obtain
t

EXISTENTIAL RISK AND GROWTH 56
v˙ 1
ρ = t + [u(c )−v δ ]
t t t
v v
t t
v˙ u(c )
=⇒ ρ− t +δ = t
t
v v
t t
u(c )
=⇒ v = t (126)
t
ρ+δ −g
t vt
u(c )/u′(c )c
=⇒ v˜ = t t t (127)
t
ρ+δ −g
t vt
Thus, therelative valueoflifedepends ontheextra utility apersonenjoys
versus increasing consumption on the current margin—this is why the degree
of diminishing returns, γ, in our utility function plays such a key role.
Given our isoelastic CRRA utility,
c1−γ
u(c ) u+ t
t 1−γ
=
u′(c )c c−γc
t t t t
u(c ) c1−γ
=⇒ t = (u+ t )(c −(1−γ) )
u′(c )c 1−γ t
t t
u(c ) 1
=⇒ t = ucγ−1 + (128)
u′(c )c t 1−γ
t t

EXISTENTIAL RISK AND GROWTH 57
A.3 Proof of Proposition 2
First, given equations (128) and (127) and γ > 1, along a balanced growth
path in which c → ∞:
t
g = g −g
v˜
u′
u
(
(
c
c
t
t
)
)
ct
ρ+δt−gvt
g v˜ = g ucγ−1+ 1
t 1−γ
g = (γ −1)g (129)
v˜ c
as long as δ converges to some constant.
t
I shall now conjecture that the solution for the balanced growth path
takes the following form: s and ℓ fall toward zero at a constant exponential
t t
rate, while σ → σ∗. The key condition for this result will be γ > 1+(β −
t
ǫ) 1−φ +1 .
αλ
Given c = Aαℓ (1 − σ ), taking logs and derivatives, in our proposed
(cid:0) (cid:1) t t t t
solution consumption growth is given by:
g = αg +g (130)
c A ℓ
Now, observe in (124) that s is inversely proportional to βδtv˜t , and that
t 1−ǫδtv˜t
the remaining terms in (124) will be constant along a balanced growth path.
Observe in (FOC: ℓ ) that ℓ is also inversely proportional to βδtv˜t . Thus,
t t 1−ǫδtv˜t
along the balanced growth path, g = g and I get:
ℓ s
g = αg +g (131)
c A s
The growth rates of A and B follow straightforwardly from their produc-
tion functions. Given A˙ = sλσλNλAφ, g = A˙ t = sλ t σ t λN t λ , which becomes
t t t t t At At A1−φ
t
constant along a balanced growth path, so the numerator and denominator
must grow at the same rate:
lim ln ˙ (sλσλNλ) = lim ln ˙ (A1−φ)
t t t t
t→∞ t→∞
=⇒ λ(g +n) = (1−φ)g
s A
λ(g +n)
=⇒ g = s (132)
A 1−φ
Given B˙ = (1 − s )λσλNλBφ, g = Bt = (1−st)λσ t λN t λ , which becomes
t t t t t Bt B˙ t B t 1−φ
constant a balanced growth path, so the numerator and denominator must

EXISTENTIAL RISK AND GROWTH 58
grow at the same rate. The key difference to A here is that s falling to 0
t
at a constant exponential rate means that 1 −s will converge to 1 and be
t
asymptotically constant, i.e. lim g = 0.
t→∞ 1−st
lim ln ˙ ((1−s )λσλNλ) = lim ln ˙ (B1−φ)
t t t t
t→∞ t→∞
=⇒ λn = (1−φ)g
B
λn
=⇒ g = (133)
B 1−φ
Plugging (132) into (131) I thus get:
λ(g +n)
s
g = α +g (134)
c 1−φ s
Plugging this into (129):
αλ(g +n)
g = (γ −1)[ s +g ] (135)
v˜ 1−φ s
Now make a key observation. Recall from FOC: ℓ that (1 − ℓ )/ℓ =
t t t
(βδ v˜)/(1−ǫδ v˜) (and the allocation of scientists is proportional to this as
t t t t
well). Given a constant, positive ǫ and β, the only way for ℓ (and s ) to
t t
fall to 0 is for δ v˜ to grow. However, remember (125): δ v˜ < 1/ǫ. Thus, as
t t t t
t → ∞, δ v˜ → 1/ǫ, i.e. δ v˜ is asymptotically constant. However, this inturn
t t t t
means that ǫδ v˜ converges to 1 asymptotically, meaning that 1 −ǫδ v˜ will
t t t t
fall to 0 exponentially. This then delivers the desired exponential increase in
(1−ℓ )/ℓ and the exponential fall to 0 of ℓ (and s ).
t t t t
This convergence of δ v˜ → 1/ǫ is unique to this model. In Jones (2016),
t t
given sufficient curvature of preferences, δ v˜ goes to infinity. However, this
t t
convergence is very logical: in the denominator of our condition for (1 −
ℓ )/ℓ is the marginal product of consumption labor, 1 − ǫδ v˜. 1 is the
t t t t
normalized value of consumption, whereas −ǫδ v˜ is the relative impact of
t t
consumption onlife. Wereδ v˜ to keep rising above1/ǫ, themarginalproduct
t t
of consumption labor would be negative: consumption labor would destroy
life more than it increases utility.
Thus, I know that:

EXISTENTIAL RISK AND GROWTH 59
˙
lim ln(δ v˜) = 0
t t
t→∞
=⇒ g = −g (136)
δ v˜
Plugging in (135):
αλ(g +n)
g = −(γ −1)[ s +g ] (137)
δ 1−φ s
I thus need an expression for g . Given δ = δNǫ−β[Aαℓ (1−σ )]ǫ[Bα(1−
δ t t t t t t
ℓ )(1−σ )]−β:
t t
g = lim l ˙ n(Nǫ−β[Aαℓ (1−σ )]ǫ[Bα(1−ℓ )(1−σ )]−β)
δ t t t t t t t
t→∞
=⇒ g = lim (ǫ−β)l ˙ n(N )+ǫln ˙ ([Aαℓ (1−σ )])−βln ˙ ([Bα(1−ℓ )(1−σ )])
δ t t t t t t t
t→∞
=⇒ g = (ǫ−h β)n+ǫ(αg +g )−βαg i
δ A ℓ B
=⇒ g = α(ǫg −βg )+ǫg +(ǫ−β)n
δ A B ℓ
=⇒ g = α(ǫg −βg )+ǫg +(ǫ−β)n (138)
δ A B s
where I substitute in g = g as explained earlier.
s ℓ
I plug this in and solve:
λ(g +n) λn αλ(g +n)
α(ǫ s −β )+ǫg +(ǫ−β)n = −(γ −1)[ s +g ]
s s
1−φ 1−φ 1−φ
αǫλ+αλ(γ −1) −αλǫn+αβλn−(γ −1)αλn−(1−φ)(ǫ−β)n
=⇒ g (ǫ+γ −1+ ) =
s
1−φ 1−φ
−αλǫn+αβλn−(γ −1)αλn−(1−φ)(ǫ−β)n
=⇒ g =
s
(1−φ)(ǫ+γ −1)+αǫλ+αλ(γ −1)
αλn(−ǫ+β −γ +1)+(1−φ)(ǫ−β)n
=⇒ g =
s (1−φ)(ǫ+γ −1)+αλ(ǫ+γ −1)
n[αλ(1+β −ǫ−γ)+(1−φ)(β −ǫ)]
=⇒ g = (139)
s (γ +ǫ−1)(αλ−φ+1)

EXISTENTIAL RISK AND GROWTH 60
g is negative
s
⇐⇒ αλ(1+β −ǫ−γ)+(1−φ)(β −ǫ) < 0
⇐⇒ αλ(γ −1−β +ǫ) > (1−φ)(β −ǫ)
αλ
⇐⇒ ((γ −1)−(β −ǫ)) > β −ǫ
1−φ
αλ αλ
⇐⇒ (γ −1) > (β −ǫ) 1+
1−φ 1−φ
(cid:18) (cid:19)
1−φ
⇐⇒ γ > 1+(β −ǫ) +1
αλ
(cid:18) (cid:19)
(140)
Thus, γ > 1+(β −ǫ) 1−φ +1 is the key condition delivering this bal-
αλ
anced growth path.
(cid:0) (cid:1)
I can now calculate the other asymptotic growth rates as well. It will be
helpful to define:
αλn
g ≡ (141)
1−φ
The asymptotic convergence of 1−ℓ directly implies:
t
αλn
g = αg = = g (142)
h B 1−φ
I can put g in terms of g:
s
αλn(1+β −ǫ−γ)+n(1−φ)(β −ǫ)
g =
s (γ +ǫ−1)(1−φ)+(γ +ǫ−1)(αλ)
γ −1−β +ǫ ǫ−β
=⇒ g = −g · −n· (143)
s (1+ αλ )(γ +ǫ−1) (1+ αλ )(γ +ǫ−1)
1−φ 1−φ

EXISTENTIAL RISK AND GROWTH 61
I can now calculate g from (134):
c
λ(g +n)
s
g = α +g
c 1−φ s
αλn αλ
=⇒ g = +(1+ )·g
c s
1−φ 1−φ
(γ −(1+β −ǫ))+ 1−φ(ǫ−β)+ αλ (γ −(1+β −ǫ))+(ǫ−β)
=⇒ g = g · 1− αλ 1−φ
c " (1+ αλ )(γ +ǫ−1) #
1−φ
(1+ αλ )(γ −(1+β −ǫ))+(1+ 1−φ)(ǫ−β)
=⇒ g = g · 1− 1−φ αλ
c " (1+ αλ )(γ +ǫ−1) #
1−φ
1+1−φ
(γ −(1+β −ǫ))+(ǫ−β) αλ
1+ αλ
=⇒ g = g · 1− 1−φ
c  γ −1+ǫ 
 
 (γ −(1+β −ǫ))+(ǫ−β)1−φ 
=⇒ g = g · 1− αλ
c
γ −1+ǫ
" #
β +(β −ǫ)1−φ
=⇒ g = g · αλ (144)
c γ +ǫ−1
" #
Since g < 0, g < g. g > 0 follows directly when β ≥ ǫ, as in this case.
s c c
How Low Can ρ Go?
What values of ρ are permissible for our asymptotic growth path to be valid?
In particular, the denominators of our shadow prices must be positive
and the optimal allocations must satisfy the transversality conditions.
First, consider p . Recall that
bt
αβv M δ /B
t t t t
p =
bt ρ−g −φg
pbt Bt
The denominator has to be positive along the balanced growth path and
g → g . Then, if the denominator is positive and thus asymptotically
pbt pb
constant along the balanced growth path:
g = lim ln ˙ (M )+ln ˙ (v δ )−g
pb
t→∞
t t t B

EXISTENTIAL RISK AND GROWTH 62
Since δ converges to 0, g = 0. Moreover, recall that δ v = δ v˜u′(c )c ,
t M t t t t t t
so g δv = g δv˜ +g u′(c)c = g u′(c)c = (1−γ)g c since δ t v˜ t is asymptotically constant,
so
g = (1−γ)g −g (145)
pb c B
The condition that the denominator of g is positive and asymptotically
pb
constant along the balanced growth path now becomes:
ρ > g +φg = (1−γ)g +(φ−1)g (146)
pb B c B
Given γ > 1 and φ < 1 the right hand side is negative, meaning any ρ ≥ 0
is valid.
Recall the transversality condition for B :
t
lim[e−ρt ·p ·B ] = 0
bt t
t→∞
Note that since γ > 1, −g > g , so the transversality condition is
pb B
satisfied even for ρ = 0
Now, consider p . Recall that
at
αM (u′(c )c −ǫδ v )/A
t t t t t t
p =
at ρ−g −φg
pat At
The denominator has to be positive along the balanced growth path and
g → g . Then, if the denominator is positive and thus asymptotically
pat pa
constant along the balanced growth path:
g = lim ln ˙ (u′(c )c −ǫδ v )−g
pa t t t t A
t→∞
given g = 0. Again, δ v = δ v˜u′(c )c , so
M t t t t t t
g = lim l ˙ n(1−ǫδ v˜)+l ˙ n(u′(c )c )−g
pa t t t t A
t→∞
=⇒ g = lim l ˙ n(1−ǫδ v˜)+(1−γ)g −g
pa t t c A
t→∞

EXISTENTIAL RISK AND GROWTH 63
As ǫδ v˜ converges to 1/ǫ along the balanced growth path, (1 − ǫδ v˜)
t t t t
falls exponentially to zero. Indeed, note that since 1 − s and βδ v˜ are
t t t
asymptotically constant, g = −g = g , so
s βδv˜/(1−ǫδv˜) 1−ǫδv˜
g = g +(1−γ)g −g (147)
pa s c A
The condition that the denominator of g be positive and asymptotically
pa
constant now becomes
ρ > g +φg = g +(1−γ)g +(φ−1)g (148)
pa A s c A
Again, since g < 0, γ > 1, φ < 1, g > 0, and g > 0, the right hand
s c A
side is negative and any ρ ≥ 0 is valid.
Recall the transversality condition for A :
t
lim[e−ρt ·p ·A ] = 0
at t
t→∞
Since g < 0 and γ > 1, I get −g > g , satisfying the transversality
s pa A
condition for A even for ρ = 0.
Next, recall the final transversality condition
lim[e−ρt ·v ·M ] = 0
t t
t→∞
Since g = 0, M → M∗ > 0. Thus, either g falls exponentially to zero
M t t v
or ρ > 0 for the transversality condition to hold.
Recall (126):
u(c )
t
v =
t ρ+δ −g
t vt
u(c ) → u and g → g along a balanced growth path. Thus, given a
t vt v
positive denominator, the denominator is asymptotically constant as δ → 0,
t
implying
g = 0 (149)
v
Since δ falls exponentially to zero andg = 0, the denominator is positive
t v
if and only if ρ > 0. ρ > 0 then also ensures the transversality condition
holds.
Thus, our balanced growth path is a valid solution for any ρ > 0.

EXISTENTIAL RISK AND GROWTH 64
Note that this ρ is still not considering population growth, i.e. considers
a somewhat selfish agent.
Finally, I have to find σ∗. Substituting the prices of ideas into (FOC: σ )
t
I get:
σ λ(p A˙ +p B˙)
t at bt
=
1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t
λ(αMt(u′(ct)ct−ǫδtvt)/AtA˙ + αβvtMtδt/BtB˙)
σ
=⇒ t = ρ−gpat−φgAt ρ−gpbt−φgBt
1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t
u′(ct)ct−ǫδtvt βvtδt
σ
=⇒ t = λα(g ρ−gpat−φgAt +g ρ−gpbt−φgBt )
1−σ At u′(c )c +(β −ǫ)δ v Bt u′(c )c +(β −ǫ)δ v
t t t t t t t t t
Now, recall that δ v˜ → 1/ǫ, so δ v = δ v˜ ·u′(c )c → 1/ǫ·u′(c )c .
t t t t t t t t t t
σ∗
u′(ct)ct−u′(ct)ct (β/ǫ)u′(ct)ct
=⇒ = lim λα(g
ρ−gpat−φgAt
+g
ρ−gpbt−φgBt
)
1−σ∗ t→∞ At (β/ǫ)u′(c t )c t Bt (β/ǫ)u′(c t )c t
σ∗ λαg
=⇒ = lim Bt (150)
1−σ∗ t→∞ ρ−g pbt −φg Bt
I can now substitute in g along our balanced growth path.
pb
σ∗ λαg
B
= (151)
1−σ∗ ρ+(γ −1)g +(1−φ)g
c B
Therefore,
λαg λαg
σ∗ 1+ B = B
ρ+(γ −1)g +(1−φ)g ρ+(γ −1)g +(1−φ)g
(cid:20) c B(cid:21) c B
λαgB
=⇒ σ∗ = ρ+(γ−1)gc+(1−φ)gB
1+ λαgB
ρ+(γ−1)gc+(1−φ)gB
λαg
=⇒ σ∗ = B
ρ+(γ −1)g +(1−φ)g +λαg
c B B
λαg
=⇒ σ∗ = B
ρ+(γ −1)g +(1−φ+λα)g
c B

EXISTENTIAL RISK AND GROWTH 65
A.4 Proof of Proposition 3
I conjecture that s˜ ≡ 1−s and ℓ ˜ ≡ 1−ℓ fall exponentially to zero on the
t t t t
asymptotic growth path, while σ → σ∗. Then, it follows directly that
t
g = αg +g (152)
h B ℓ˜
Moreover, since (1 − ℓ )/ℓ = ℓ ˜ /(1 − ℓ ˜ ) and (1 − s )/s = s˜/(1 − s˜) are
t t t t t t t t
both proportional to (βδ v˜)/(1 − ǫδ v˜ ) along an asymptotic growth path,
t t t t
implying g = g along the asymptotic growth path (analogous to g = g
s˜ ℓ˜ s ℓ
along the asymptotic growth path in the proof of proposition 2). Thus,
g = αg +g (153)
h B s˜
Moreover, an asymptotically constant g requires
B
λ(n+g )
s˜
g = (154)
B
1−φ
thus implying
λ(n+g )
s˜
g = α +g (155)
h s˜
1−φ
Since ℓ ˜ → 0, ℓ is asymptotically constant,
t t
g = αg (156)
c A
Similarly, s is asymptotically constant, so an asymptotically constant g
t A
then directly requires that
λn
g = (157)
A
1−φ
thus implying
λn
g = α (158)
c 1−φ
Now, noticethatfors˜ tofalltozeroexponentially, (1−s )/s = s˜/(1−s˜)
t t t t t
hasto fallexponentially to zero. Onthe asymptotic growthpaths˜/(1−s˜) is
t t

EXISTENTIAL RISK AND GROWTH 66
proportional to (βδ v˜)/(1−ǫδ v˜), so for s˜ to fall to zero exponentially, δ v˜
t t t t t t t
has to fall to zero exponentially, meaning 1−ǫδ v˜ is asymptotically constant.
t t
Thus, g = g = g . Thus,
(βδtv˜t)/(1−ǫδtv˜t) δtv˜t s˜
g = g +g (159)
s˜ δ v˜
It follows that
g = ǫg −βg +(ǫ−β)n
δ c h
λn λ(n+g )
=⇒ g = ǫα −βα s˜ −βg +(ǫ−β)n (160)
δ 1−φ 1−φ s˜
To get an expression for g , I must differentiate between the cases in
v˜
which γ ≤ 1 and γ > 1. Note that
g = g −g
v˜
u′
u
(
(
c
c
t
t
)
)
ct
ρ+δt−gvt
g v˜ = g ucγ−1+ 1
t 1−γ
as long as δ converges to a constant
t
Thus, when γ > 1, g = (γ −1)g , while when γ ≤ 1, v˜ is asymptotically
v˜ c
constant so g = 0. I will consider the γ > 1 case first. Then,
v˜
g = g +g
s˜ δ v˜
λn λ(n+g ) λn
=⇒ g = ǫα −βα s˜ −βg +(ǫ−β)n+(γ −1)α
s˜ 1−φ 1−φ s˜ 1−φ
αλn αλ
=⇒ g = (ǫ−β +γ −1)−βg (1+ )+(ǫ−β)n
s˜ s˜
1−φ 1−φ
αλ αλn
=⇒ g (1+β +β ) = (ǫ−β +γ −1)+(ǫ−β)n
s˜ 1−φ 1−φ
n[αλ(ǫ−β +γ −1)+(1−φ)(ǫ−β)]
=⇒ g =
s˜ (1+β)(1−φ)+βαλ
−n αλ (1−ǫ+β −γ)+(β −ǫ)
1−φ
=⇒ g = (161)
s˜ h 1+β(1+ αλ ) i
1−φ

EXISTENTIAL RISK AND GROWTH 67
Then, the condition for g to be negative is
s˜
αλ(ǫ−β +γ −1)+(1−φ)(ǫ−β) < 0
αλ
⇐⇒ ((γ −1)−(β −ǫ)) < (β −ǫ)
1−φ
αλ αλ
⇐⇒ (γ −1) < (β −ǫ) 1+
1−φ 1−φ
(cid:18) (cid:19)
1−φ
⇐⇒ γ < 1+(β −ǫ) +1 (162)
αλ
(cid:18) (cid:19)
which is the key condition delivering our result.
Let g ≡ αλn. I can now calculate g :
1−φ h
αλn αλ
g = + 1+ g
h s˜
1−φ 1−φ
(cid:18) (cid:19)
n αλ (ǫ−β +γ −1)+(ǫ−β)
αλn αλ 1−φ
=⇒ g = + 1+
h 1−φ 1−φ h 1+β(1+ αλ ) i
(cid:18) (cid:19) 1−φ
αλ (ǫ−β +γ −1)+(ǫ−β)+(ǫ−β +γ −1)+ 1−φ(ǫ−β)
=⇒ g = g 1+ 1−φ αλ
h 1+β(1+ αλ ) !
1−φ
(1+ αλ )(1−γ +β −ǫ)+(1+ 1−φ)(β −ǫ)
=⇒ g = g · 1− 1−φ αλ (163)
h " 1+β(1+ αλ ) #
1−φ
In the case that γ ≤ 1, I get
g = g +g
s˜ δ v˜
λn λ(n+g )
=⇒ g = ǫα −βα s˜ −βg +(ǫ−β)n
s˜ s˜
1−φ 1−φ
αλn αλ
=⇒ g = (ǫ−β)−βg (1+ )+(ǫ−β)n
s˜ 1−φ s˜ 1−φ
αλ αλn
=⇒ g (1+β +β ) = (ǫ−β)+(ǫ−β)n
s˜
1−φ 1−φ
n[αλ(ǫ−β)+(1−φ)(ǫ−β)]
=⇒ g =
s˜ (1+β)(1−φ)+βαλ
−n (1+ αλ )(β −ǫ)
1−φ
=⇒ g = (164)
s˜ h1+β(1+ αλ ) i
1−φ

EXISTENTIAL RISK AND GROWTH 68
which given β > ǫ is negative as conjectured.
I can then calculate g :
h
αλn αλ
g = + 1+ g
h 1−φ 1−φ s˜
(cid:18) (cid:19)
n (1+ αλ )(ǫ−β)
αλn αλ 1−φ
=⇒ g = + 1+
h 1−φ 1−φ h1+β(1+ αλ ) i
(cid:18) (cid:19) 1−φ
(2+ αλ + 1−φ)(β −ǫ)
=⇒ g = g · 1− 1−φ αλ
h " 1+β(1+ αλ ) #
1−φ
Finally, notethatgiven g ≥ 0andg < 0inbothcases, since g +g = g ,
v˜ s˜ v˜ δ s˜
I know g is negative, and thus I know that δ falls exponentially to zero.
δ t

EXISTENTIAL RISK AND GROWTH 69
A.5 Proof of Proposition 4
In the case that ǫ < β, the proof is straightforward. In particular, in the
previous two proofs for the cases that γ > 1, when I plug in γ = 1 + (β −
ǫ) 1−φ +1 it immediately follows that g = 0.
αλ s
In the case that ǫ = β and γ ≤ 1, the proof is straightforward as well. In
(cid:0) (cid:1)
particular, consider the γ ≤ 1 case in the previous proof; plugging in ǫ = β
immediately yields g = 0.
s
Once g = 0, the proof proceeds as in the rule of thumb allocation.
s

EXISTENTIAL RISK AND GROWTH 70
A.6 Proof of Proposition 5
This proof is essentially the same as for proposition 2, including the section
on the minimum valid value of ρ, with slight modifications.
First, g < 0 follows directly from γ > 1 and ǫ > β, so no additional
s
condition is necessary.
Second, I need to ensure that g > 0, which is necessary since I am as-
c
suming c → ∞ such that g → 0. If ǫ ≫ β, this is not the case. Specifically,
t v˜
β +(β −ǫ)1−φ
g = g · αλ > 0
c γ +ǫ−1
" #
1−φ
⇐⇒ β +(β −ǫ) > 0
αλ
αλ
⇐⇒ β > ǫ−β
1−φ
ǫ−β αλ
⇐⇒ < (165)
β 1−φ

EXISTENTIAL RISK AND GROWTH 71
A.7 Proof of Proposition 6
I conjecture that s (and ℓ ) fall exponentially to 0, while consumption grows
t t
at a positive rate.
Given γ ≤ 1, u(ct) is asymptotically constant , so
u′(ct)ct
g = g −g
v˜
u′
u
(
(
c
c
t
t
)
)
ct
ρ+δt−gvt
=⇒ g = 0 (166)
v˜
as long as δ converges to a constant.
t
For s (and ℓ ) to fall exponentially to 0, δ v˜ must rise and eventually
t t t t
converges asymptotically to 1/ǫ. Therefore, on the balanced growth path,
g = −g . Thus, 0 = −g .
v˜ δ δ
The growth rates g = α(ǫg −βg )+ǫg +(ǫ−β)n, g = λ(gs+n), and
δ A B s A 1−φ
g = λn follow just as in the proof of proposition 2.
B 1−φ
Thus,
0 = g = α(ǫg −βg )+ǫg +(ǫ−β)n
δ A B s
λ(g +n) αλn
=⇒ 0 = α(ǫ s −β )+ǫg +(ǫ−β)n
s
1−φ 1−φ
αλ αλ
=⇒ g ·(−ǫ)(1+ ) = (ǫ−β)(1+ )n
s 1−φ 1−φ
ǫ−β
=⇒ g = − n (167)
s
ǫ
which is negative, as conjectured.
Just like in the proof of proposition 2, g = αg = αλn ≡ g follows.
h B 1−φ
I can then calculate g :
c
g = αg +g
c A s
λ(g +n)
=⇒ g = α s +g
c 1−φ s
αλ αλ ǫ−β
=⇒ g = n· −(1+ )
c
1−φ 1−φ ǫ
(cid:20) (cid:21)
ǫ−β
=⇒ g = g −(n+g) (168)
c
ǫ
Given ǫ > β, it follows that g < g.
c

EXISTENTIAL RISK AND GROWTH 72
I have to check that g > 0 (since g = 0 requires c → ∞).
c v˜ t
ǫ−β
g = g −(n+g) > 0
c
ǫ
αλ αλ
⇐⇒ ǫ > (1+ )(ǫ−β)
1−φ 1−φ
αλ
⇐⇒ 0 > (ǫ−β)−β
1−φ
ǫ−β αλ
⇐⇒ < (169)
β 1−φ
which is the same condition that ǫ 6≫ β from before.
Finally, I determine δ → δ∗. In the case that γ < 1:
t
1
δ∗ = lim 1/v˜
t
ǫ t→∞
1 ρ+δ −g
=⇒ δ∗ = lim t vt
ǫ t→∞ ucγ−1 + 1
t 1−γ
(ρ+δ∗ −g )(1−γ)
=⇒ δ∗ = v
ǫ
Note that v = u(ct) , so given a positive and thus asymptotically con-
t ρ+δt−gvt
stantdenominator, g = lim u′(ct)c˙t = lim u′(ct)c·g = lim 1/(ucγ−1+
v t→∞ u(ct) t→∞ u(ct) c t→∞ t
1 )·g = (1−γ)g .
1−γ c c
(ρ+δ∗ −(1−γ)g )(1−γ)
=⇒ δ∗ = c
ǫ
1−γ (1−γ)ρ−(1−γ)2g
=⇒ δ∗(1− ) = c
ǫ ǫ
(1−γ)ρ−(1−γ)2g
=⇒ δ∗ = c
ǫ(1− 1−γ)
ǫ
(1−γ)ρ−(1−γ)2g
=⇒ δ∗ = c (170)
ǫ+γ −1
Since ǫ > 1−γ, the denominator is positive.
For the numerator to be positive, it must be the case that (1−γ)ρ−(1−
γ)2g > 0 ⇐⇒ ρ > (1−γ)g . This ensures that our integral over utility is
c c

EXISTENTIAL RISK AND GROWTH 73
bounded: u(c ) grows at rate (1 −γ)g asymptotically, so if ρ were smaller
t c
than that, the integral could be unbounded. (And we can’t solve cases with
potential unbounded utility with our mathematical methods.)
Thus, δ does indeed converge to a constant as conjectured.
When γ = 1, u(ct) = u + ln(c ), so δ → 0. However, δ does not fall
u′(ct)ct t t t
fast enough (not exponentially, g = 0)—in particular, δ → 0 proportional
δ t
to 1/v˜ proportional to 1/ln(c )—so M → 0 even when γ = 1.
t t t

EXISTENTIAL RISK AND GROWTH 74
A.8 Proof of Proposition 7
I conjecture that the asymptotic growth path features positive consumption
growth and δ → ∞ with constant asymptotic g > 0, with σ → σ∗. Given
t δ t
γ ≤ 1, u(ct) → 1 asymptotically.
u′(ct)ct 1−γ
Recall that
u(c )/(u′(c )c )
t t t
δ v˜ = δ .
t t t ρ+δ −g
vt
On an asymptotic growth path, g = g . Thus, as δ gets large and
vt v t
u(ct) → 1 on the asymptotic growth path,
u′(ct)ct 1−γ
1
δ v˜ → . (171)
t t 1−γ
Thus, δ v˜ is asymptotically constant. Note that δ v˜ < 1/ǫ must still be
t t t t
satisfied, but since ǫ < 1−γ, 1/ǫ > 1/(1−γ), so this holds.
In turn, δ v˜ being asymptotically constant means s and ℓ converge to
t t t t
constants s∗ and ℓ∗. The rest follows as in the rule of thumb allocation;
in particular, we get positive asymptotic consumption growth and positive
growth of δ (since ǫ > β), as conjectured.
t
We can determine ℓ∗. Recall that
1−ℓ βδ v˜
t t t
=
ℓ 1−ǫδ v˜
t t t
1−ℓ∗ β 1
=⇒ = 1−γ
ℓ∗ 1−ǫ 1
1−γ
1
=⇒ ℓ∗ =
β 1
1+ 1−γ
1−ǫ 1
1−γ
1−ǫ 1
=⇒ ℓ∗ = 1−γ
1−ǫ 1 +β 1
1−γ 1−γ
1−γ −ǫ
=⇒ ℓ∗ = (172)
1−γ −ǫ+β
Given ǫ < 1−γ, ℓ∗ is clearly positive and less than one.

EXISTENTIAL RISK AND GROWTH 75
A.9 Proof of Proposition 8
I again conjecture that the asymptotic growth path features positive con-
sumption growth g and δ → ∞ with positive g . As in the previous proof,
c t δ
we get δ v˜ → 1 . However, since now 1 = 1, βδtv˜t → ∞ asymptotically.
t t 1−γ 1−γ ǫ 1−ǫδtv˜t
Thus, since (1−ℓ )/ℓ and (1−s )/s are both proportional to βδtv˜t on an
t t t t 1−ǫδtv˜t
asymptotic growth path, ℓ and s go to 0. I conjecture that ℓ and s fall to
t t t t
zero at constant exponential rates, while σ → σ∗.
t
We can plug in the given ǫ = 1−γ:
ucγ−1 + 1
1−ǫδ v˜ = 1−(1−γ)δ t 1−γ
t t t ρ+δ −g
t vt
ucγ−1 δ
=⇒ 1−ǫδ v˜ = 1− (1−γ)δ t + t
t t t ρ+δ −g ρ+δ −g
(cid:18) t vt t vt(cid:19)
Thus, asymptotically, as δ → ∞ and g = g ,
t vt v
=⇒ 1−ǫδ v˜ → 1− (1−γ)ucγ−1 +1
t t t
=⇒ 1−ǫδ v˜ → −(1−γ)ucγ−1. (173)
t t (cid:0) t (cid:1)
(Note that the RHS is still positive, as we are assuming u¯ negative when
γ < 1.)
In particular, note that βδv˜ is constant asymptotically, as is (1−s ) and
t t
(1−ℓ ). Thus, from the FOCs we get that g = g = g .
t s ℓ 1−ǫδtv˜t
g = g = g = −(1−γ)g (174)
s ℓ 1−ǫv˜t c
=⇒ g = g = −ǫg .
s ℓ c
g and g are indeed negative as conjectured.
s ℓ
As in proposition 2, we have
g = αg +g (175)
c A s
λ(g +n¯)
s
g = (176)
A
1−φ
g = αg (177)
h B
λn¯
g = (178)
B 1−φ
g = (ǫ−β)n¯ +ǫg −βg (179)
δ c h

EXISTENTIAL RISK AND GROWTH 76
(Verifying σ → σ∗ proceeds similarly as in that proposition as well.)
t
We can use this to solve for an explicit expression for g
c
λ(−ǫg +n¯)
g = α c −ǫg
c 1−φ c
αλ αλ
1+ǫ 1+ g = n¯
1−φ c 1−φ
(cid:18) (cid:19)
αλ
1
1−φ
g = n¯ = g < g, (180)
c
1+ǫ 1+ αλ 1+ǫ 1+ αλ
1−φ 1−φ
(cid:16) (cid:17) (cid:16) (cid:17)
which is indeed positive, as conjectured.
From this we get an explicit expression for g as well:
s
αλ
g = g = −ǫ 1−φ n¯.
s ℓ
1+ǫ 1+ αλ
1−φ
(cid:16) (cid:17)
We finally must verify that g > 0 as conjectured.
δ
g = (ǫ−β)n¯ +ǫg −βg
δ c h
ǫ
=⇒ g = (ǫ−β)n¯ + −β g¯
δ 1+ǫ 1+ g¯
!
n¯
(cid:0) (cid:1)
From this, we get that g > 0 iff
δ
αλ (ǫ−β)(1+ǫ)
< .
1−φ βǫ

EXISTENTIAL RISK AND GROWTH 77
A.10 Proof of Proposition 9
First, note that that the asymptotic growth path must feature g > 0.
c
To see this, note first that g < 0 is not permissible, since then consump-
c
tion would eventually fall below the zero utility level. If g = 0 were the
c
case, that would require g = g < 0. But g = 0 would also mean g < 0.
s ℓ c δ
This is because given our condition that αλ ≥ (ǫ−β)(1+ǫ), it must also be
1−φ βǫ
true that αλ > (ǫ−β), so βg¯ > (ǫ−β)n¯. Thus, g = (ǫ−β)n¯ −βg +ǫg =
1−φ β δ h c
(ǫ − β)n¯ − βg¯ < 0. But that would mean δ → 0, so δ v˜ → 0 (since u˜ is
t t t
bounded), and thus s and ℓ would go to 1, contradicting g = g < 0.
t t s ℓ
Moreover, I claim that it must be the case that g = 0.
δ
If g > 0, we get the result as in the proof of proposition 8, where g > 0
δ c
only if αλ < (ǫ−β)(1+ǫ), which is not met here.
1−φ βǫ
If g < 0, δ v˜ → 0, so s and ℓ to 1. But then consumption grows at
δ t t t t
least as fast as safety, and so given ǫ > β, g > 0.
δ
Thus, it must be the case that g = 0. However, it also can’t be the case
δ
that δ is bounded. If that were to case, δ v˜ would be bounded by something
t t
strictly less than 1/ǫ. In turn, s and ℓ could not sustain constant negative
t t
exponential growth rates. But then we would get balanced growth, with
g > 0 since ǫ > β, which is a contradiction.
δ
Thus, it must be the case that δ → ∞ subexponentially. Now, since δ
t
still goes to ∞, δ v˜ → u˜ = 1 = 1, so s and ℓ go to zero.
t t 1−γ ǫ t t
In particular, if g = g were equal to zero, we would get balanced growth
s ℓ
with g > 0 (given ǫ > β). Thus, it must be the case that g = g < 0. (They
δ s ℓ
can’t be > 0, since s and ℓ are going to zero.
t t
As in the proof for proposition 6, for g = 0 to be the case when s and
δ t
ℓ fall exponentially to 0, it must be the case that
t
ǫ−β
g = g = − n¯, (181)
ℓ s
ǫ
and the other growth rates follow as in that proof, in particular g = g¯ −
c
(n¯ + g¯)ǫ−β. g > 0 holds when αλ > (ǫ−β) as shown in that proof. As we
ǫ c 1−φ β
show earlier in this proof, this condition hold in this case.
Note that now δ v˜’s approach to 1/ǫ is driven not by the growth in c
t t t
but rather by the subexponential growth in δ and thus the approach of
t
δt to 1. Recall that δ v˜ → δt u˜ . c grows much quicker than δ
ρ+δt−gv t t ρ+δt−gv t t t
(exponential vs. subexponential), so u˜ is asymptotically 1 quicker than
1−γ

EXISTENTIAL RISK AND GROWTH 78
δt is asymptotically 1. (Thus, the relationship g = −ǫg derived in the
ρ+δt−gv s c
proof of proposition 8 does not apply here.)

EXISTENTIAL RISK AND GROWTH 79
A.11 Proof of Proposition 10
First, note that the optimal allocation cannot feature an asymptotic growth
path with g < 0. This would mean c → 0, but eventually c would fall
c t t
below the zero utility level, i.e. dying would be preferred to living.
We also cannot have g > 0 on an asymptotic growth path.
c
Toseethis, notethatδ → ∞nomatterwhat. Moreover, thatδ cangrow
t t
at most exponentially on an asymptotic path because n¯ grows exponentially
and c can grow at most exponentially. Thus, g = g , from which follows
t vt v
u˜
δ v˜ = δ → u˜
t t t ρ+δ −g
t vt
as δ → ∞.
t
Now, we consider three different cases of γ separately. If γ > 1, u¯ =
ucγ−1+ 1 → ∞ as c → ∞ as we saw previously. But then δ v˜ goes above
t 1−γ t t t
the bound of 1/ǫ we get from our FOCs. Thus, c can’t grow indefinitely and
t
must be bounded above.
If 1 − ǫ < γ < 1, we have u˜ = ucγ−1 + 1 → 1 . But 1 > 1, so
t 1−γ 1−γ 1−γ ǫ
again we would have δ v˜ go above the bound of 1/ǫ. Again, c can’t grow
t t t
indefinitely and must be bounded above.
Finally, consider γ = 1, i.e. log utility. Then, u˜ = u(ct) = u¯+log(ct) =
u′(ct)ct 1/ct·ct
u¯ + log(c ) = u(c ). Thus, as c → ∞, u¯ grows without bound, and δ v˜
t t t t t
goes above the bound of 1/ǫ. Again, c can’t grow indefinitely and must be
t
bounded above.
Thus, we must have g = 0. For this to be the case on an asymptotic
c
growth path (with σ → σ∗), we must have
t
λ(g +n)
s
0 = g = α +g
c 1−φ s
αλ αλ
=⇒ (1+ )g = − n
s
1−φ 1−φ
1
=⇒ g = − g, (182)
s (1+ αλ )
1−φ
so s must fall to zero at a constant exponential rate. Note that on an
t
asymptotic growth path g = g by our FOCs, so ℓ falls to 0 as well. The
ℓ s t
other growth rates then follow as usual.

EXISTENTIAL RISK AND GROWTH 80
Since s andℓ fallto zero, δ v˜ must converge to1/ǫ. But δ v˜ → u˜. Thus,
t t t t t t
c must increase and converge to a level c∗ such that u˜ → 1/ǫ. In particular,
t
this means that c∗ is given as follows:
u(c∗) 1
u˜ = = . (183)
u′(c∗)c∗ ǫ
We now differentiate based on γ. If γ = 1, this means
1
u¯+log(c∗) =
ǫ
1
⇐⇒ c∗ = exp −u¯ . (184)
ǫ
(cid:18) (cid:19)
The zero utility level c is the level of consumption at which log(c ) =
0 0
−u¯ ⇐⇒ c = exp(−u¯), so
0
c∗ 1
= exp . (185)
c ǫ
0 (cid:18) (cid:19)
If γ > 1 or 1 > γ > 1−ǫ,
1 1
uc∗γ−1 + =
1−γ ǫ
1
1 + 1 γ−1
⇐⇒ c∗ = ǫ γ−1 (186)
u
" #
(Note that if γ > 1, we are assuming u¯ > 0, so this is positive; if γ < 1,
we are assuming u¯ < 0, so this is positive then too.)
We determine c :
0
c1−γ
u = − 0
1−γ
1
1 γ−1
=⇒ c = (187)
0 (γ −1)u
(cid:20) (cid:21)
Then,
1
c∗ (1 + 1 )(γ −1)u γ−1
ǫ γ−1
=
c u
0 " #
1
c∗ γ −1 γ−1
=⇒ = +1 . (188)
c ǫ
0 (cid:20) (cid:21)

EXISTENTIAL RISK AND GROWTH 81
When γ > 1, this is clearly positive; when 1 > γ > 1−ǫ, 1−γ < ǫ, so
γ−1 < 1, so this is positive as well.
ǫ

EXISTENTIAL RISK AND GROWTH 82
A.12 Proof of Proposition 11
Note that with this knife-edge condition, if g = 0 and g is at “full speed”,
c h
i.e. g = g¯, we have g = 0. If g > 0, g > 0.
h δ c δ
Again, we can’t have g < 0 on the asymptotic path in the optimal
c
allocation, because consumption would fall below the zero utility level.
Similarly, we can’t have g > 0, since then g > 0, so δ → ∞, δ v˜ → u˜,
c δ t t t
and u˜ becomes bigger than 1/ǫ eventually (in all cases, whether γ > 1, γ = 1,
or 1 > γ > 1−ǫ).
Thus, the asymptotic growth path must feature g = 0. In turn, this
c
means g = 0.
δ
g = 0, requires, as in proposition 10, that
c
1
g = g = − g. (189)
ℓ s (1+ αλ )
1−φ
The other growth rates follow as usual.
In the case that γ ≥ 1, c must be bounded. To see this, note that if
t
c increases (subexponentially) without bound, u˜ → ∞, so we would need
t
δ → 0 to keep δ v˜ < 1/ǫ. But this impossible, since we can at most keep
t t t
the growth in δ due to the scale effect in check, not decrease δ to zero.
t t
In the case that γ < 1, c can increase without bound, since u˜ is still
t
bounded. δ must then converge to a level δ∗ such that δ∗ 1 = 1, i.e.
t 1−γ ǫ
δ∗ = 1−γ < 1.
ǫ

EXISTENTIAL RISK AND GROWTH 83
A.13 Proof of Proposition 12
Note that for any variable a, ( \ 1−a) = 1−˙a = −a˙ a = −aˆ a .
1−a a1−a 1−a
Law of Motion: y
Recall that y ≡ g =
(stσtNt)λ
. Taking logs and derivatives:
At A1−φ
t
yˆ= λ(n+σˆ +sˆ)−(1−φ)y (190)
Law of Motion: z
Similarly, I consider zˆ. Recall that z ≡ g =
((1−st)σtNt)λ
. Taking logs and
Bt B1−φ
t
derivatives:
s
zˆ= λ n+σˆ −sˆ −(1−φ)z (191)
1−s
(cid:18) (cid:19)
Law of Motion: δ
Recallthatδ = δNǫ−βcǫh−β, withc = Aαℓ (1−σ )andBα(1−ℓ )(1−σ ).
t t t t t t t t t t t
Again, taking logs and derivatives:
δ ˆ = (ǫ−β)n+ǫg −βg
ct ht
σ ℓ σ
=⇒ δ ˆ = (ǫ−β)n+ǫ αy +ℓ ˆ−σˆ −β αz −ℓ ˆ −σˆ
1−σ 1−ℓ 1−σ
(cid:18) (cid:19) (cid:18) (cid:19)
σ ℓ
=⇒ δ ˆ = (ǫ−β) n−σˆ +α(ǫy −βz)+ℓ ˆ ǫ+β (192)
1−σ 1−ℓ
(cid:18) (cid:19) (cid:18) (cid:19)
Law of Motion: s
Next, I consider sˆ. Recall the FOC for s : 1−st = pbtB˙ t = pbt((1−st)σtNt)λB t φ .
t st patA˙
t
pat(stσtNt)λAφ
t
Taking logs and derivatives of both sides:
s s
−sˆ −sˆ= g +λ −sˆ +σˆ +n +φz −g −λ(sˆ+σˆ +n)−φy
1−s pbt 1−s pat
(cid:18) (cid:19)
s s
=⇒ sˆ 1+ = g −g +φy −φz +λsˆ 1+
1−s pat pbt 1−s
(cid:18) (cid:19) (cid:18) (cid:19)
1−λ
=⇒ sˆ = g −g +φy −φz (193)
1−s
pat pbt

EXISTENTIAL RISK AND GROWTH 84
RecallFOCsforA andB : pa˙t = ρ− 1 [M u′(c )αct +p φA˙ t−αǫv M δt ]
t t pat pat t t At at At t tAt
and p˙bt = ρ− 1 [p φB˙ t +αβv M δt ] respectively. Substituting, I get
pbt pbt bt Bt t tBt
1−λ 1 c A˙ δ
sˆ = ρ− [M u′(c )α t +p φ t −αǫv M t ]
t t at t t
1−s p A A A
at t t t
1 B˙ δ
−ρ+ [p φ t +αβv M t ]+φy −φz
bt t t
p B B
bt t t
1−s αM βδ v αM (u′(c )c −ǫδ v )
=⇒ sˆ= t t t − t t t t t (194)
1−λ p B p A
(cid:20) bt t at t (cid:21)
Recall the FOC for σ : 1−σt =
Mt[u′(ct)ct+(β−ǫ)δtvt].
From the FOC for s ,
t σt λ(patA˙+pbtB˙) t
I know p B ˙ = 1−stp B ˙ ; substituting this yields:
bt t st at t
1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t
λ =
σ t p A˙ 1+ 1−st
at st
y 1−σ M [u′(c )c(cid:16)+(β −ǫ(cid:17))δ v ]
=⇒ λ t = t t t t t (195)
s σ p A
t t at t
Similarly, I get:
z 1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t
λ = (196)
1−s σ p B
t t bt t
Now, recall the FOC for ℓ : 1−ℓt = βδtv˜t . I manipulate this:
t ℓt 1−ǫδtv˜t
1−ℓ −ǫδ v˜ +ℓ ǫδ v˜ = ℓ βδ v˜
t t t t t t t t t
=⇒ ℓ (β −ǫ)δ v = (1−ℓ )u′(c )c −ǫδ v (197)
t t t t t t t t
=⇒ (1−ℓ )u′(c )c = ǫδ v +ℓ (β −ǫ)δ v (198)
t t t t t t t t
Combining (195) and (197) gives us
y 1−σ M [u′(c )c −ǫδ v ]
t t t t t t
λ ℓ = (199)
s σ p A
t t at t
Similarly, combining (196) and (198) gives us
z 1−σ M βδ v
λ (1−ℓ) t = t t t (200)
1−s σ p B
t t bt t

EXISTENTIAL RISK AND GROWTH 85
Substituting (199) and (200) into (194) yields:
1−s z 1−σ y 1−σ
sˆ= αλ (1−ℓ) t −α ℓ t
1−λ 1−s σ s σ
(cid:20) t t t t (cid:21)
λ 1−σ λ 1−s 1−σ
=⇒ sˆ= αz (1−ℓ) −αy ℓ (201)
1−λ σ 1−λ s σ
Law of Motion: σ
I can use the FOC for σ , (198), (196) and rearrange:
t
1−σ M [u′(c )c +(β −ǫ)δ v ]
t t t t t t
=
σ λ(p A ˙ +p B ˙ )
t at bt
1−σ 1−ℓM [u′(c )c +(β −ǫ)δ v ]
=⇒ t = t t t t t
σ t 1−ℓ λ 1+ st (p B˙)
1−st bt
1−σ 1−s M(cid:16)[βδ v ] (cid:17)
=⇒ t = t t t t (202)
σ 1−ℓ λ(p g B )
t bt Bt t
Taking logs and derivatives yields:
σ s ℓ
−σˆ −σˆ = −sˆ +ℓ ˆ −δ +δ ˆ +g −g −zˆ−z (203)
1−σ 1−s 1−ℓ
vt pbt
From the FOC for M , I get g = v˙t = ρ− u(ct) +δ . From the FOC for
t vt vt vt t
B I get g = p˙bt = ρ − 1 [p φB˙ t + αβv M δt ]. I can substitute in these
t pbt pbt pbt bt Bt t tBt
ˆ
expressions and the expressions I previously found for δ and zˆ. This yields:
σ s ℓ u(c ) αM βδ v
−σˆ −σˆ = −sˆ +ℓ ˆ −δ +δ ˆ +ρ− t +δ −ρ+φz + t t t −zˆ−z
1−σ 1−s 1−ℓ v t p B
t bt t
1 s ℓ σ ℓ
=⇒ −σˆ = −sˆ +ℓ ˆ +(ǫ−β) n−σˆ +α(ǫy −βz)+ℓ ˆ ǫ+β
1−σ 1−s 1−ℓ 1−σ 1−ℓ
(cid:18) (cid:19) (cid:18) (cid:19)
u(c ) s αM βδ v
− t +(φ−1)z −λ n+σˆ −sˆ +(1−φ)z + t t t
v 1−s p B
t (cid:18) (cid:19) bt t
1 σ s ℓ ℓ
=⇒ −σˆ +(β −ǫ) −λ = −sˆ (1−λ)+ℓ ˆ +ǫ+β
1−σ 1−σ 1−s 1−ℓ 1−ℓ
(cid:18) (cid:19) (cid:18) (cid:19)
u(c ) αM βδ v
+n(ǫ−β −λ)+αǫy −αβz − t + t t t
v p B
t bt t
(204)

EXISTENTIAL RISK AND GROWTH 86
We can plug in (200) and rearrange:
1+(β −ǫ)σ −λ(1−σ) s u(c )
=⇒ σˆ = (1−λ) sˆ+(λ+β −ǫ)n+αβz −αǫy + t
1−σ 1−s v
t
ℓ 1−ℓ 1−σ
+(− (1+β)+ǫ )ℓ ˆ−αλz t
1−ℓ 1−s σ
(cid:18) (cid:19) t t
I set the following definitions:
1−σ
θ = (205)
σ
1+(β −ǫ)σ −λ(1−σ)
ℓ
ω = − (1+β)+ǫ (206)
σ
1−ℓ
(cid:18) (cid:19)
s u(c ) 1−ℓ 1−σ
(cid:13)B = (1−λ) sˆ+(λ+β −ǫ)n+αβz −αǫy + t −αλz t
1−s v 1−s σ
t t t
(207)
Then:
σˆ = θ ((cid:13)B +ω ℓ ˆ ) (208)
σ σ
Law of Motion: ℓ
Recall the FOC for ℓ : 1−ℓt =
βδtu′
(
v
c
t
t)ct . Since u′(c )c = c1−γ, taking logs
t ℓt 1−ǫδtu′
(
v
c
t
t)ct
t t
and derivatives, this yields:
−ℓ ˆ 1 = δ ˆ +g −(1−γ)g + ǫδ tu′( v c t t)ct δ ˆ +g −(1−γ)g
1−ℓ vt ct 1−ǫδ vt vt ct
tu′(ct)ct
(cid:16) (cid:17)
Substituting 1−ℓt ǫ =
ǫδtu′
(
v
c
t
t)ct I get:
ℓt β 1−ǫδtu′
(
v
c
t
t)ct
1 1−ℓ ǫ
ℓ ˆ = − 1+ (δ ˆ +g +(γ −1)g ) (209)
vt ct
1−ℓ ℓ β
(cid:18) (cid:19)
From the FOC for M , I get g = v˙t = ρ− u(ct) +δ . It follows directly
t vt vt vt t

EXISTENTIAL RISK AND GROWTH 87
that g = αy +ℓ ˆ−σˆ σ . I can substitute in these two expressions and δ ˆ :
ct 1−σ
1−ℓ ǫ
ℓ ˆ = −(1−ℓ) 1+ ·
ℓ β
(cid:18) (cid:19)
σ
[(ǫ−β) n−σˆ +α(ǫy −βz)
1−σ
(cid:18) (cid:19)
ℓ u(c ) σ
+ℓ ˆ ǫ+β +ρ− t +δ +(γ −1) αy +ℓ ˆ−σˆ ]
1−ℓ v t 1−σ
(cid:18) (cid:19) t (cid:18) (cid:19)
ℓ 1−ℓ ǫ
=⇒ ℓ ˆ 1+(γ −1+ǫ+β )(1−ℓ) 1+
1−ℓ ℓ β
(cid:20) (cid:18) (cid:19)(cid:21)
1−ℓ ǫ σ
= (1−ℓ) 1+ ·[(γ −1+ǫ−β) σˆ +(β −ǫ)n
ℓ β 1−σ
(cid:18) (cid:19)
u(c )
+(1−γ −ǫ)αy +αβz −ρ−δ + t ] (210)
v
t
I set the following definitions:
(1−ℓ) 1+ 1−ℓ ǫ
ℓ β
θ = (211)
ℓ (cid:16) (cid:17)
1+ γ −1+ǫ+β ℓ (1−ℓ) 1+ 1−ℓ ǫ
1−ℓ ℓ β
σ (cid:16) (cid:17)
ω = (γ −(cid:0)1+ǫ−β) (cid:1) (212)
ℓ 1−σ
u(c )
(cid:13)A = (β −ǫ)n+(1−γ −ǫ)αy +αβz −ρ−δ + t (213)
v
t
Then:
ℓ ˆ = θ ((cid:13)A +ω σˆ) (214)
ℓ ℓ
I substitute in (208):
ℓ ˆ = θ ((cid:13)A +ω θ ((cid:13)B +ω ℓ ˆ ))
ℓ ℓ σ σ
=⇒ ℓ ˆ [1−ω ω θ ] = θ ((cid:13)A +ω θ (cid:13)B)
ℓ σ σ ℓ ℓ σ
θ ((cid:13)A +ω θ (cid:13)B)
=⇒ ℓ ˆ = ℓ ℓ σ (215)
1−ω ω θ
ℓ σ σ

EXISTENTIAL RISK AND GROWTH 88
Addendum: u(ct)
vt
To determine both (cid:13)A and (cid:13)B, I need an expression for u(ct). First, recall the
vt
FOC for ℓ : 1−ℓt =
βδtu′
(
v
c
t
t)ct . Thus,
t ℓt 1−ǫδtu′
(
v
c
t
t)ct
ℓ u(c ) u(c ) v
βδ t = t (1−ǫδ t )
1−ℓ u′(c )c v u′(c )c
t t t t t
ℓ u(c ) u(c ) u(c )
=⇒ βδ t = t −ǫδ t
1−ℓ u′(c )c v u′(c )c
t t t t t
ℓ u(c ) u(c ) u(c )
=⇒ βδ t +ǫδ t = t (216)
1−ℓ u′(c )c u′(c )c v
t t t t t
Let u˜ = u(c) . Then,
u′(c)c
u(c ) 1
u˜ = t = ucγ−1 + (217)
u′(c )c t 1−γ
t t
Thus, I need an expression for c . Look at δ:
t
δ = δNǫ−βcǫh−β
t t t t
δ c −β c−β
=⇒ t t = Nǫ−βcǫh−β t
δ h t t t h−β
(cid:18) t(cid:19) t
1
δ c
−β ǫ−β
=⇒ t t = N c
t t
δ (cid:18) h t(cid:19) !
1
−β ǫ−β
δt ct
δ ht
=⇒ (cid:18) (cid:19) = c (218)
(cid:16) (cid:17) t
N
t
Next, note that
c Aαℓ (1−σ )
t t t
=
h Bα(1−ℓ )(1−σ )
t t t
α
c ℓ A
=⇒ t = t
h 1−ℓ B
t t (cid:18) (cid:19)

EXISTENTIAL RISK AND GROWTH 89
Finally, note that
z B˙ A A (1−s )λσλNλBφ
= t t = t t t t t
y B A˙ B sλσλNλAφ
t t t t t t t
z A1−φ 1−s λ
=⇒ = t t
y B t 1−φ (cid:18) s t (cid:19)
1 λ
z 1−φ A 1−s 1−φ
=⇒ = t t
y B s
(cid:18) (cid:19) t (cid:18) t (cid:19)
1 λ
z 1−φ A 1−s 1−φ
=⇒ = t t
y B s
(cid:18) (cid:19) t (cid:18) t (cid:19)
1 λ
z 1−φ s 1−φ A
=⇒ t = t (219)
y 1−s B
(cid:18) (cid:19) (cid:18) t(cid:19) t
Thus:
1
1 λ α −β ǫ−β
δt ℓt z 1−φ st 1−φ
δ 1−ℓt y 1−st
!
(cid:18) (cid:18) (cid:19) (cid:19)
c = (cid:16) (cid:17) (cid:16) (cid:17) (220)
t
N
t

EXISTENTIAL RISK AND GROWTH 90
A.14 Proof of Proposition 13
We know from the FOCs of the Hamiltonian that:
u˜ u(c )
t t
v˜ = , u˜ = (221)
t t
ρ+δ −g u′(c )c
t vt t t
First, consider thedenominator ofv˜: ρ+δ −g . Asδ → 0, ρ+δ −g →
t t vt t t vt
ρ+g .
vt
Next, consider g . We know from our FOCs that
vt
u(c )
t
v =
t ρ+δ −g
t vt
If the denominator converges to a constant as δ → 0 and u˜ → ∞, we get
t
u˙(c ) u′(c )c˙ u′(c )cg
g → t = t = t ct (222)
vt
u(c ) u(c ) u(c )
t t t
1
=⇒ g → g (223)
vt ct
u˜
t
Thismeansg → 0asu˜ → ∞,soindeedmeansthedenominatorv converges
vt t
to a constant.
This implies that as δ → 0 and u˜ → ∞:
t
u˜ u˜
v˜ = t → t (224)
t
ρ−δ +g ρ
t vt
This immediately implies
Ev˜ → −1 (225)
ρ
and
Ev˜ → Eu˜ (226)
c c
We now turn to Eu˜. We know
c
1
u˜(c ) = ucγ−1 +
t t 1−γ
=⇒ u˜′(c ) = (γ −1)ucγ−2 (227)
t

EXISTENTIAL RISK AND GROWTH 91
Thus,
u˜′(c )c (γ −1)ucγ−1
Eu˜ = t t = t (228)
c u˜(c ) ucγ−1 + 1
t t 1−γ
(γ −1) u˜ + 1
t γ−1
=⇒ Eu˜ = (229)
c (cid:16)u˜ (cid:17)
=⇒ Eu˜ → (γ −1) (230)
c
=⇒ Ev˜ → (γ −1) (231)
c
as u˜ → ∞.
t
Finally, to calculate the ρ′ that increases v˜ equivalent to a doubling of
t
consumption (starting from ρ∗%) for the table in the main text, I find the ρ′
that satisfies:
ρ′ E c v˜
2E c v˜ = (232)
ρ∗
(cid:18) (cid:19)
ρ′ −1
=⇒ 2(γ−1) = (233)
ρ∗
(cid:18) (cid:19)
=⇒ ρ′ = 2(1−γ)ρ∗ (234)

EXISTENTIAL RISK AND GROWTH 92
B Numerical Simulation
B.1 Simulating the Transition Dynamics
I solve the system of differential equations characterizing the optimal alloca-
tion numerically using “reverse shooting” (like Jones (2016)). I start from
the steady state, consider a small deviation, and then run time backwards.
In the notation that follows, I start from time T and run time backwards to
time 0.
Given values for the parameters γ, ǫ, β, ρ, λ, φ, α, n, u, and δ, as well as
a specified N and a small δ > 0 (small deviation from the steady state), I
T T
need to find values of s and ℓ . To do this, I use the function ‘fminsearch’
T T
in Matlab to find values of s and ℓ that minimize the distance between sˆ ,
T T T
ˆ
ℓ and σˆ and their steady state values. I then run time backwards, giving
T T
us a candidate path.
To determine the values for the other parameters, I first pick ǫ, β, and γ.
I also set φ Then, I use the function ‘patternsearch’ in Matlab to find values
for λ, δ, u, N and δ which minimize the weighted sum of the deviations
T T
from a selection of moments of the candidate path and a set of preferred
values. These moments are given below.
1. Given a candidate path, I first find the year t in which u˜, the value
0
of a year of life as a ratio to consumption, is closest to 4. The first moment
is u˜ compared to 4.
t0
2. The second moment is the growth rate of consumption at t compared
0
to 1 percent.
3. The third moment is ℓ , the fraction of workers in the consumption
t0
sector, compared to 95%.
4. The fourth moment is the growth rate of proportion of the population
working as scientists at time t , g , compared to 2%.
0 σt0
5. The fifth moment is hazard rate δ at time t , compared to 0.1%.
0
6. The sixth moment is the growth rate of δ at time T compared to g ,
δ
to ensure the the simulation is close to steady state at time T.
I pick γ = 1.5, ǫ = 0.4, and β = 0.3 as reasonable parameters. In
addition, I set ρ = 0.02, α = 1, and n = 1%. Note that these choices don’t
seem to matter for the qualitative results (as long as ǫ > β and γ > 1).
The process described above can find different local minima depending on
the initial guess as well the value of φ supplied, so I hunt for the best overall
fit. I end up using φ = 5/6 and λ = 0.3, δ = 3.8965 × 10−5, u = 0.0098,

EXISTENTIAL RISK AND GROWTH 93
N = 9.2955×1014,and δ = 5×10−4.
T T
To extrapolate M , I have to calculate the area under the hazard rate
∞
∞
curve, i.e. δ ds. Note that:
t0 s
R ∞ T ∞
δ ds = δ ds+ δ ds
s s s
Zt0 Zt0 ZT
∞ T ∞
=⇒ δ ds ≈ δ ds+ δ ·e−sgδds
s s T
Zt0 Zt0 Z0
∞ T δ
=⇒ δ ds ≈ δ ds+ T (235)
s s
g
Zt0 Zt0 δ
since at time T, we are approximately at the steady state, where δ declines
exponentially.
Thus, I sum the area under our simulated δ from the time representing
T
today to the end of the simulation, which gives us δ ds. Verifying that
t0 s
indeed δ ˆ ≈ g , I can then calculate δT. Summing these two terms gives
T δ gδ R
∞
us the desired δ ds, and then the probability of humanity surviving to
t0 s
∞
infinity conditio R nal on surviving until t 0 is then e
−R
t0
δsds
.
B.2 Simulating the Acceleration in Growth
The natural way to simulate the acceleration of growth (in this case, faster
population growth) would be to solve the differential equations characteriz-
ing the optimal allocation using “forward shooting”. However, due to the
instability of the system of differential equations, this yields unreliable re-
sults. Thus, I again proceed by solving the system of differential equations
using “reverse shooting” as when we simulated the transition dynamics.
First, the transition path without the acceleration in growth is given by
the path as found in Appendix B.1. I will refer to this as the unperturbed
path.
Next, we would like to simulate the transition path with accelerated
growth. I use the same parameters as in Appendix B.1 except for a time-
varying rate of n, set as discussed in the main text. This gives me a can-
didate path with accelerated growth. I would like to find a transition path
with acceleration that matches the unperturbed path up until the moment
of acceleration. Thus, using the function ‘fminsearch’ in Matlab, I find δ
T
and N that yield a candidate path with accelerated growth that minimizes
T

EXISTENTIAL RISK AND GROWTH 94
the weighted sum of the deviations from a selection of moments and a set of
preferred values.
In particular, I pick some year t prior to the year in which growth ac-
0
celerates; this will be the reference year on the unperturbed path. Given a
candidate path, I find a year t∗ in which δ t∗ of our candidate path is closest
to δ
t0
on the unperturbed path. Then, my moments are s t∗, ℓ t∗, σ t∗, δ t∗, y t∗,
z t∗, and N t∗, compared to their respective values at t
0
on the unperturbed
transition path. Since s, ℓ, σ, δ, y, z, and N uniquely characterize all the
variables of our economy onthe optimal allocationand boththe unperturbed
and the accelerated path evolve according to the same system of differential
equations prior to the acceleration, this ensures that both the unperturbed
and accelerated transition path represent the same economy up until the
moment where growth is accelerated.
I experiment with the weights and the reference year to hunt for the best
overall fit. I end up picking δ = 5.0326×10−4 and N = 9.3991×1014 for
T T
the accelerated transition path that results in a permanent level effect, and
δ = 5.0001×10−4 and N = 9.2948×1014 for the transition path with the
T T
temporary boom.
This method appears to work well (i.e. matches the unperturbed path
very well) for an acceleration in growth that is not too large, although it is
still imperfect. However, it enables us to sidestep the difficulty of “forward
shooting”andcompare thetransitionpathswith andwithout anacceleration
in growth using “reverse shooting”.
I extrapolate the long-term survival probability M as before.

EXISTENTIAL RISK AND GROWTH 95
References
Acemoglu, Daron, “Directed Technical Change,” Review of Economic Studies,
2002, 69 (4), 781–809.
, Philippe Aghion, Leonardo Bursztyn, and David Hemous, “TheEnvi-
ronment and Directed Technical Change,” American Economic Review, Febru-
ary 2012, 102 (1), 131–166.
Aurland-Bredesen, Kine Josefine, “The Optimal Economic Management of
Catastrophic Risk.” PhD dissertation, Norwegian University of Life Sciences
School of Economics and Business 2019.
Bloom, Nicholas, Charles Jones, John Van Reenen, and Michael Webb,
“Are Ideas Getting Harder to Find?,” Technical Report w23782, National Bu-
reau of Economic Research, Cambridge, MA September 2017.
Bostrom, Nick, “Existential Risks: Analyzing Human Extinction Scenarios,”
Journal of Evolution and Technology, Vol. 9, No. 1 (2002), March 2002, 9,
1–35.
, “Astronomical Waste: The Opportunity Cost of Delayed Technological Devel-
opment,” Utilitas, November 2003, 15 (3), 308–314.
Brock, William and M. Scott Taylor, “Economic Growth and the Environ-
ment: A Review of Theory and Empirics,” Handbook of Economic Growth,
Elsevier 2005.
Caplan, Bryan,“TheTotalitarian Threat,”in“GlobalCatastrophicRisks”2008,
p. 498.
Chetty, Raj,“ANewMethodofEstimatingRiskAversion,” American Economic
Review, December 2006, 96 (5), 1821–1834.
Farquhar, Sebastian, John Halstead, Owen Cotton-Barratt, Stefan
Schubert, Hadyn Belfield, and Andrew Snyder-Beattie, “Existential
Risk: Diplomacy andGovernance,” Technical Report,Global Priorities Project,
Oxford University 2017.
Hall, Robert E., “Reconciling Cyclical Movements in the Marginal Value of
Time and the Marginal Product of Labor,” Journal of Political Economy, April
2009, 117 (2), 281–323.

EXISTENTIAL RISK AND GROWTH 96
and Charles I. Jones, “The Value of Life and the Rise in Health Spending,”
The Quarterly Journal of Economics, February 2007, 122 (1), 39–72.
Jones, Charles I., “R & D-Based Models of Economic Growth,” Journal of
Political Economy, 1995, 103 (4), 759–784.
, “Life and Growth,” Journal of Political Economy, March 2016, 124 (2), 539–
578.
and Paul M. Romer, “The New Kaldor Facts: Ideas, Institutions, Popu-
lation, and Human Capital,” American Economic Journal: Macroeconomics,
January 2010, 2 (1), 224–245.
Lucas, Deborah J., “Asset Pricing with Undiversifiable Income Risk and Short
Sales Constraints: Deepening the Equity Premium Puzzle,” Journal of Mone-
tary Economics, December 1994, 34 (3), 325–341.
Martin, Ian W. R. and Robert S. Pindyck, “Averting Catastrophes: The
Strange Economics of Scylla and Charybdis,” American Economic Review, Oc-
tober 2015, 105 (10), 2947–2985.
and Robert S Pindyck, “Welfare Costs of Catastrophes: Lost Consumption
and Lost Lives,” Working Paper 26068, National Bureau of Economic Research
July 2019.
M´ejean, Aur´elie, Antonin Pottier, St´ephane Zuber, and Marc Fluer-
baey, “Intergenerational Equity under Catastrophic Climate Change,” Techni-
calReport2017.25,FAERE-FrenchAssociationofEnvironmentalandResource
Economists November 2017.
, , , and , “When Opposites Attract: Averting a Climate Catastrophe
despite Differing Ethical Views,” Technical Report 2019.
Nordhaus, William and Paul Sztorc, “DICE 2013R: Introduction and User’s
Manual,” October 2013.
Parfit, Derek, On What Matters: Volume Two, Oxford University Press, May
2011.
Pindyck, Robert S., “Climate Change Policy: What Do the Models Tell Us?,”
Journal of Economic Literature, September 2013, 51 (3), 860–872.
Posner, Richard A., Catastrophe: Risk and Response, Oxford, New York: Ox-
ford University Press, 2004.

EXISTENTIAL RISK AND GROWTH 97
Romer, Paul, “Cake Eating, Chattering, and Jumps: Existence Results for Vari-
ational Problems,” Econometrica, 1986, 54 (4), 897–908.
, “Endogenous Technological Change,” Journal of Political Economy, 1990, 98
(5), S71–102.
Sagan, Carl, Pale Blue Dot: A Vision of the Human Future in Space, Random
House Publishing Group, 1994.
Snyder-Beattie, Andrew E., Toby Ord, and Michael B. Bonsall, “An Up-
per Bound for the Background Rate of Human Extinction,” Scientific Reports,
December 2019, 9 (1), 11054.
Solow, Robert M., “A Contribution to the Theory of Economic Growth,” The
Quarterly Journal of Economics, 1956, 70 (1), 65–94.
Stern, Nicholas, “The Stern Review on the Economic Effects of Climate
Change,” Population and Development Review, 2006, 32 (4), 793–798.
Stokey, Nancy,“AreThereLimitstoGrowth?,”International Economic Review,
1998, 39 (1), 1–31.
Torres, Phil, “How Likely Is an Existential Catastrophe?,” September 2016.
Weitzman, Martin L., “Subjective Expectations and Asset-Return Puzzles,”
American Economic Review, September 2007, 97 (4), 1102–1130.
