---
id: pdf-ned-augenblick-2025-overinference-from-weak
type: pdf
title: Overinference from Weak Signals and Underinference from Strong Signals
url: ''
authors:
- Ned Augenblick
- Eben Lazarus
- Michael Thaler
ingested_at: '2026-04-29T16:19:44Z'
content_hash: sha256:69c218591a0e8317960e9872ae38552de20302c125a615cfde41f940e0ee776b
source_path: raw/pdf/pdf-ned-augenblick-2025-overinference-from-weak.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 106
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__efc403c5.pdf
published_at: '2025'
---
Overinference from Weak Signals and
∗
Underinference from Strong Signals
Ned Augenblick†
Eben Lazarus‡
Michael Thaler§
September 2024
Abstract
When people receive new information, sometimes they revise their beliefs too
much, and sometimes too little. In this paper, we show that a key driver of whether
people overinfer or underinfer is the strength of the information. Based on a model
in which people know which direction to update in, but not exactly how much to
update, we hypothesize that people will overinfer from weak signals and underinfer
from strong signals. We then test this hypothesis across four di!erent environments:
abstract experiments, a naturalistic experiment, sports betting markets, and financial
markets. In each environment, our consistent and robust finding is overinference from
weak signals and underinference from strong signals. Our framework and findings can
help harmonize apparently contradictory results from the experimental and empirical
literatures. JEL codes: C91, D83, D91, G14, G41.
∗An early version of this paper was circulated as Thaler (2021). We would especially like to thank Matthew Rabin for
his advice throughout this project. We are grateful to the editor, Andrei Shleifer, and four anonymous referees for very
helpfulfeedback,aswellasNickBarberis,FrancescaBastianello,RolandBénabou,PolCampos-Mercade,StefanoDellaVigna,
Ben Enke, Christine Exley, Xavier Gabaix, Nicola Gennaioli, Thomas Graeber, Benjamin Hébert, Spencer Kwon, Martin
Lettau, Alessandro Lizzeri, Peter Maxted, Terrance Odean, Pietro Ortoleva, Cameron Peng, Josh Schwartzstein, David
Sraer, David Thesmar, Mike Woodford, Leeat Yariv, and seminar participants at BEAM, NBER Behavioral Finance, HBS,
Lund, Princeton, Stockholm University, UBC, UC Berkeley, and UC Santa Barbara. The experiments were approved by
IRBs at Princeton University (13114-03), UCL (SHSEco-2223-003-1), and UC Berkeley (2023-07-16581). The pre-analysis
plans are available at https://aspredicted.org/ax4wg.pdf (Study 1a), https://aspredicted.org/8Q4_6Y9 (Study 1b), and
https://aspredicted.org/SYW_QWF(Study2).
†HaasSchoolofBusiness,UniversityofCalifornia,Berkeley. Email: ned@haas.berkeley.edu.
‡HaasSchoolofBusiness,UniversityofCalifornia,Berkeley. Email: lazarus@berkeley.edu.
Correspondence: 545StudentServices#1900,Berkeley,CA,94720.
§DepartmentofEconomics,UniversityCollegeLondon. Email: michael.thaler@ucl.ac.uk.

I. Introduction
How do people update their beliefs given new information? This important question has
spawned a vast experimental and empirical literature, with seemingly contradictory results. A
common finding in the experimental literature is that people often underreact to information
in standard updating tasks. But this is seemingly at odds with observational evidence
from real-world settings, such as excess volatility in asset prices, which often appears more
consistent with overreaction. Updating behavior is clearly context-dependent, but what
specific mediating factors help explain how people will respond to a given piece of information?
This paper hypothesizes that people commonly overinfer from weak information and
underinfer from strong information. We start with a theoretical framework in which we
formalize these concepts and provide simple but general conditions under which the e!ect will
arise. We then use a classic experimental paradigm to show that while people do underinfer
when provided with strong signals (as commonly studied in the lab), they overinfer from
su"ciently weak signals (which have been previously understudied). After replicating and
extending this result in a follow-up study, we then demonstrate that this e!ect is not an
artifact of the abstract environment by showing the same results in a novel experiment with
more naturalistic information. Finally, we use two empirical settings to show that betting
markets and asset prices exhibit excess volatility when information is weak, but this e!ect
reverses with su"ciently strong information.
Tounderstandtheintuitionforourhypothesis, considertheconstantstreamofinformation
faced by people every day. People might read a new poll about an election, have a conversation
with their boss at work, or see news about daily stock-market movements. In many cases,
people understand the directional impact this news should have on their beliefs, but are less
certain about the strength of the information. That is, they know that better polling raises a
candidate’s election chances, managerial praise raises promotion chances, and positive stock
returns raise early retirement chances, but they don’t know exactly how much their beliefs
should move. How will a person update in this situation? Consider the extreme case in which
the person knows that a signal is positive but is completely unsure about the signal’s strength.
The person only knows that beliefs should rise, and therefore updates as if the news has
“intermediate” strength. But if a person is always updating an intermediate amount, then
they will be overreacting to weak news and underreacting to strong news.1 In other words,
1Welargelyusetheterms“overinfer”and“overreact”interchangeably. However,weseeasubtledi!erence:
aperson“overinfers”iftheyperceiveasignalasmoreinformativethanaBayesianwould, while“overreaction”
is the resultant behavior of reacting too strongly. We will generally use “overinfer” when we are clearly
discussing overestimating signal strength (such as in our theory), while we will generally use “overreact” when
discussing observable behavior. We will only highlight the di!erence when there is a contaminating force
(such as base-rate neglect) that might cause beliefs to react too strongly for a reason other than overinference.
1

when people know the signal’s direction, insensitivity to objective signal strength leads to a
pattern of over- and underreaction relative to a full Bayesian.
In more realistic scenarios, people will have a rough guess of the strength of signals they
receive. This estimate might be based on a simplified model, unconscious approximation, or
constrained information processing given attention to certain aspects of a signal. Given that
the estimate is imperfect, the person should still shrink their estimate toward an intermediate
strength. While di!erent people can have di!erent estimates given the same information, the
shrinkage will on average lead to overreaction to weak signals and underreaction to strong
signals. In Section II, we model this intuition formally, and show that it holds across a general
set of information structures, estimation strategies, and possibly non-Bayesian updating rules.
We then use distributional assumptions to obtain a set of simple, parametric updating rules
that can be taken to the data.
Our theory relies throughout on the four high-level assumptions that people (1) pay
attention to a given piece of information; (2) can easily determine its directional meaning;
(3) form reasonable estimates of its strength; and (4) are at least partially aware that this
estimate is imperfect. We think these assumptions hold in many important settings, including
the ones we consider in our empirical analysis. There are, however, important cases in which
each may be violated, such as when people (1) simply ignore very weak information; (2) are
unsure of a signal’s directional meaning; (3) form systematically biased strength estimates;
or (4) fail to account for estimation noise. These potential violations underscore that our
theory is not intended to provide a universal explanation for all under- and overreaction.
Rather, our goal is to identify a single important mediating factor that helps explain behavior
parsimoniously across a range of common situations.
To test our theoretical predictions, we study how people’s reaction to new information
varies when signals are weak versus strong. To do so, we create three controlled lab experi-
ments (with preregistered hypotheses) and study two empirical environments in which signal
strengths vary systematically and updating behavior can be measured consistently. While
the environments and methods di!er, we find consistent results across each of the settings.
The first two experiments (Studies 1a and 1b) employ the classic “bookbag-and-poker-
chips” paradigm (Green, Halbert, and Robinson 1965). This is the most commonly used
experimental setup to study belief updating; for example, Benjamin’s (2019) survey of the
literature includes 500 experimental treatment blocks across 21 papers that study inference
from symmetric binary signals about a binary state, which is our main focus. Belief updating
in these settings often features underreaction relative to Bayes’ rule, with Benjamin’s “Stylized
Fact 1” stating that “Underinference is by far the dominant direction of bias.” The vast
majority of this evidence, though, is on strong signals: in all of these papers where people
2

receive one symmetric binary signal, its diagnosticity — the likelihood of seeing a “high”
signal conditional on the “high” state — is never lower than 3/5. Our hypothesis is that
people will overinfer given lower signal strengths. There is a hint of the importance of signal
strength for underreaction in these studies: Benjamin notes that “Underinference...is more
severe the larger is the diagnosticity,” suggesting that the pattern may flip. We hypothesize
that this is indeed the case.
To test our hypothesis, in Study 1a we run this standard experiment with 500 participants
using our much wider range of signal strengths. In the main treatment, participants are
presented with two decks of cards: a green deck containing more spades than diamonds, and a
purple deck with more diamonds than spades. Participants see a single card drawn from one
of the two decks, and they must then estimate probabilities for which deck was chosen based
on the suit of the drawn card. We vary signal strength by changing the number of spades and
diamonds in each deck. This design broadly aligns with our theoretical setup: the direction to
update is fairly clear (e.g., a spade is evidence for the green deck), but the correct magnitude
is less obvious (requiring clear understanding of the data-generating process, correct use of
Bayes’ rule, and exact calculation of the proportion of suits in each deck).
We find that almost all participants update their beliefs in the right direction, but there is
substantial heterogeneity in how much they revise their beliefs. We interpret this as showing
that participants know to update in a particular direction, but di!er in how they perceive the
strength of the signal. Notably, participants’ answers are not random: the average perceived
signal strength rises monotonically with the true strength. Our main result, however, is that
this relationship is muted, leading to overreaction to weak signals and underreaction to strong
signals in a manner consistent with our theory. Reassuringly, our estimates of the magnitudes
of underinference for the high-strength signals are in line with the previous literature. It is
only in the previously understudied low-strength signals, with diagnosticity below 3/5, that
we find overinference: for very weak signals, participants act as if signals are twice as strong
as they truly are.
Study 1a focuses on the case in which both decks are equally likely to be drawn ex ante,
so we conduct a follow-up in Study 1b in which we systematically vary the prior (considering
values of 1/4, 1/3, and 1/2) in addition to the signal strength. All of our main findings
continue to hold. Participants again overreact to weak signals and underreact to strong
signals. While we estimate that people exhibit modest base-rate neglect, our core findings
about inference are not substantially a!ected. In other words, although people’s biases in
using base rates can impact how they react to new information, disentangling these biases
from our e!ects does not impact our conclusion that people overinfer from weak signals and
underinfer from strong signals.
3

Exploring heterogeneity in updating, both experiments provide further evidence in line
with the theoretical framework. Intuitively, the theory suggests that our e!ect will be stronger
for people with less precise estimates of the signal strength. Consistent with this prediction,
we find that our e!ect is stronger for people who exhibit more variance in their level of under-
and overinference in 1a and 1b, have less task experience in 1a and 1b, have lower scores on
a cognitive reflection test (adapted from Frederick 2005) in 1a, and state that they are more
uncertain about their answers in 1b (adapted from Enke and Graeber 2023).
Studies 1a and 1b provide clean evidence for our e!ect, as the bookbags-and-poker-chips
setting allows us to manipulate the DGP and compare people’s behavior to an objective
benchmark. But this control comes with some costs: the setting is quite abstract, and signals
are di"cult to understand largely as a result of numerical and calculation-related complexity.
As with many experiments, one may be concerned that people treat this math-exam-like
situation in a di!erent way than in real-life scenarios.
Given this concern, our Study 2 analyzes belief updating in a more naturalistic setting,
where participants are not provided with precise numbers representing likelihoods or signal
strengths. Since naturalistic DGPs are often highly complicated, it is challenging to find
an appropriate environment. Such an environment must (1) be reasonably understood by
participants, (2) allow for clean variation in signal strength, and (3) allow some way to
estimate the correct answer in order to calculate under- and overreaction. To address these
challenges, we design a new experiment in which we ask basketball fans to predict the outcome
of an NBA basketball game given sequences of game scenarios. For example, we elicit the
probability that a team wins when they are ahead by 1 point with 2 minutes left in the game,
and then we elicit it again given a scenario in which they have just made a shot to go ahead
by 3 points a few seconds later. Although the DGP itself is complex, (1) the scenario is simple
enough for basketball fans to immediately understand it, (2) the strength of the same news
(like a scored basket) changes over the course of the game, and (3) we can use a data-driven,
third-party benchmark estimate of signal strength. Note again that as in our theory, the
direction of the news is clear (a made shot increases the probability of winning), but the
exact change in probability in di!erent scenarios is less clear (requiring some estimation
process given personal experience and understanding of basketball games). While there are
costs in moving away from a fully controlled DGP, this environment provides a much more
naturalistic source of uncertainty about signal strengths.
To implement Study 2, we recruited 500 basketball fans, providing them with sequences
of events over the course of four quarters of a hypothetical NBA game. Here, the variation in
information strength is largely driven by timing: making a basket to take a lead in the fourth
quarter is a much stronger signal than making a basket in the first quarter. As in the abstract
4

experiments, we find that the vast majority of participants update in the right direction, but
there is dispersion in the perceived strength of each signal. Crucially, people again are not
answering randomly: on average, a basket is seen as a stronger signal in the fourth quarter
than in the first. But just as before, the relationship is muted, such that people on average
overreact to weak signals (in the first quarter) and underreact to strong signals (in the fourth
quarter), switching from over- to underreaction on average in the third quarter. Overall,
these findings replicate the core findings from Studies 1a and 1b in a more realistic setting.
While Study 2 is more naturalistic than Studies 1a and 1b, it still places participants in
a new experimental paradigm with fictional scenarios and relatively low stakes. In light of
these concerns, we turn to evidence from more realistic high-stakes settings by studying the
movement of market-implied probability distributions in both (1) sports betting markets
and (2) financial markets. For (1), we use over 5 million transactions from a large sports
prediction market for five major sports, corresponding to about 260,000 sporting events.
The market-implied beliefs for these sporting events — particularly the subsample of NBA
games — provide an empirical analogue to our Study 2. For (2), we study S&P 500 index
option markets, using option-implied beliefs regarding the future value of the S&P from daily
option prices observed over a roughly 20-year span.
These settings allow us to examine external validity but come with their own challenges.
Perhaps the most important one is that we can no longer create credible estimates of
the Bayesian probability for a given situation, as we see neither the full information set
of participants nor the structure of the DGP.2 To overcome this challenge, we develop a
new empirical method based on theoretical results from Augenblick and Rabin (2021) and
Augenblick and Lazarus (2023). The core intuition of these papers is that, when a Bayesian is
changing their beliefs over time about some event, they must be learning something and thus
on average must reduce their uncertainty correspondingly. This intuition can be formalized
by defining movement as the sum of the squared deviations of changes in beliefs over time,
and uncertainty reduction as the drop in perceived variance in the outcome. While movement
and uncertainty reduction may di!er for a given signal realization, they must be equal
in expectation across signal realizations, regardless of the DGP. This insight allows for a
DGP-agnostic test of Bayesian updating in observational data. And crucially, these statistics
are intuitively and theoretically related to over- and underinference: overinference will lead to
2In our finance data, it is clear that creating a “correct” forecast of the distribution of future outcomes is
infeasible. In the sports data, one could create a reasonable forecast given observables (like score and game
time), but this would not reflect the observer’s full information set (injury or foul issues, game importance,
whether Drake is courtside, etc.), and therefore stating that the observer’s beliefs are wrong is dubious. This
is not an issue in the experiment because participants’ information sets are limited and controlled by the
experimenter. We also face challenges related to the use of prices (which reflect the marginal trader’s beliefs
and risk preferences) instead of individual beliefs. We discuss how we deal with these in Section IV.
5

positive excess movement relative to uncertainty reduction on average, while underinference
will lead to too little movement relative to the reduction in uncertainty.
While this allows for an intuitive test of over- vs. underinference with an unknown DGP, to
test our theory, we also need to distinguish situations in which signals are weak versus strong.
Given that the signal strength is also unobservable, we turn to the same separating variable
from Study 2: time to resolution. As in the experiment, our insight is that when a person
is predicting the value of the S&P 500 in three months, information today should generally
not lead to much belief movement; meanwhile, information today is highly informative for
the value of the S&P tomorrow, and we should accordingly observe more movement of
short-horizon beliefs in response to information.3 Our theory then intuitively suggests that
there should be too much movement (evidence for overinference and overreaction) at long
forecast horizons, and too little movement (vice versa) at short horizons.
Turning to the data, we find strong and consistent evidence for the hypothesized e!ect
in both sports betting and financial markets. Both uncertainty reduction and movement
increaseovertimeasresolutionapproaches, butmovementisgenerallyhigherthanuncertainty
reduction early on (i.e., far from resolution), and lower toward the end of the event. For
example, in the options data, there is very little daily uncertainty reduction until a few weeks
before the contract expires, but beliefs consistently move back and forth, generating excess
movement. In other words, news today appears to hold relatively little information about
the value of the S&P in multiple months, but the market acts as if it has more diagnosticity.
However, within two weeks of a contract’s resolution, the relationship reverses: movement is
either less than or equal to uncertainty reduction. That is, as signals become stronger, the
market begins to underreact. On net, total movement averaged over an entire option contract
is too high, matching the finding of excess movement in Augenblick and Lazarus (2023). But
this overall average masks meaningful heterogeneity as one varies the signal strength, in the
manner predicted by our theory. The same broad pattern holds in the sports-betting data we
consider. In both cases, the results are clear both visually and in formal statistical tests on
movement and uncertainty reduction.
Given that we cannot observe true signal strength, we must rely on our indirect measure
(time to resolution)to test the relationship between signal strength and over- vs. underreaction
in our two real-world high-stakes settings. The strength of our experimental settings, mean-
while, is that these variables are observable or plausibly constructable, but the experiments
are lower-stakes and less realistic. The multiple settings thus provide complementary evidence
3The relationship between the time horizon and signal strength of course depends on the exact DGP.
We show that the predicted relationship holds strongly in simulations of game-like DGPs; it also holds in
standard option-pricing models. More importantly, it clearly holds in our empirical settings.
6

for our theory, whose predictions align well with both sets of data.
Our experimental results relate to a large literature on updating, including many papers
documenting other forms of over- and underinference; we provide a brief and incomplete
review here. Classically, our paper is most closely related to Phillips and Edwards (1966) and
Gri"n and Tversky (1992). Phillips and Edwards are the first we know of to consider the
e!ect of signal strength on inference, in an unincentivized task with many sequences of signals.
Gri"n and Tversky’s inference experiments focus on sample-proportion and sample-size
e!ects in updating from multiple signals, but they also show evidence for insensitivity to the
discriminability of a given signal, which corresponds to our definition of signal strength.
More recently, Gonçalves, Libgober, and Willis (2024) find underreaction to strong signals
butevenfurtherunderreactiontotheretractionofthosesignals, whileKieren, Müller-Dethard,
and Weber (2024) find overreaction to disconfirming signals. Bordalo et al. (2023) also find
evidence for insensitivity to signal strength, along with a range of other results (including
multimodalityandinstabilityinupdating)acrosstasks; wediscusshowourmodelingapproach
complements and contrasts with theirs at the end of Section II. Other recent papers (Bordalo
et al. 2020, Afrouzi et al. 2023, Fan, Liang, and Peng 2024) consider forecasting rather than
inference behavior; we discuss our framework’s applicability and connections to this literature
in our conclusion. Ba, Bohren, and Imas (2024) run an experiment confirming many of the
patterns that we originally documented in our Study 1a, and argue with additional studies
that the patterns they observe are consistent with a two-stage model of channeled attention,
followed by cognitively imprecise updating. We see these results as complementary.
Two particularly important recent influences on our paper are Khaw, Li, and Woodford
(2021) and Enke and Graeber (2023). Khaw, Li, and Woodford (2021) present a model of
cognitive noise that connects mental errors in perceiving and encoding information with
insensitivity to information in choice tasks. We build o! the structure of this model to study
updating, under the premise that people form imperfect estimates of a signal’s strength
using multiple possible processes (such as making simplifying assumptions about the DGP,
attending to certain information, and imperfectly processing that information). Enke and
Graeber (2023) present a related model of cognitive uncertainty in which people’s perception
of new information is noisy. This leads people to be insensitive to new information overall
and shade their posterior toward their prior, such that they underinfer on average. Our
argument follows similar logic with one important distinction: we focus on environments in
which people have no issue determining the direction of the signal, but perceive the strength
of the signal imperfectly. Consequently, people do not shade toward their prior belief, but
rather shade toward the belief given a signal with an “average” strength. In our setting, the
relative perception of signal strength determines whether people underinfer or overinfer, and
7

we predict overinference when signals are weak.4
Our results are further related to a large literature using asset prices for evidence on beliefs,
as surveyed in Barberis (2018).5 For the overall market, a long literature (building from Shiller
1981, with more recent work including Barberis et al. 2015 and Giglio and Kelly 2018) argues
for a link between apparent excess volatility and overreaction. For individual firms, earnings
news seems to provide strong information about near-term firm fundamentals (Kormendi
and Lipe 1987, Bouchaud et al. 2019), and multiple papers (e.g., Bernard and Thomas 1989,
DellaVigna and Pollet 2009) provide evidence that post-earnings announcement drift arises
from the market underreacting to such news. A host of other factors, including uninformative
news content (Tetlock 2014) and a string of good fundamental news (Bordalo et al. 2024), are
predictive of apparent overreaction and return reversals.6 Kwon and Tang (2024) reconcile
some of these findings by considering the distribution of past outcomes for the given category
of news; they argue that categories with more extreme outliers tend to generate greater
overreaction. Our focus on the informativeness of a given signal is conceptually somewhat
di!erent.7 While signal strength is clearly not the only relevant factor for belief behavior,
we contribute by isolating it as a simple, powerful determinant in a range of settings, with
complementary evidence from both a new set of experiments and market-price data.
We proceed as follows. Section II provides our theoretical framework; Section III presents
the three experiments; Section IV analyzes the sports betting and finance data; and Section V
discusses and concludes. The Online Appendix contains model proofs, additional empirical
details and results, and screenshots of the pages in the experiments.
II. Theory
Overview. We consider a setting in which people can easily understand the direction they
should update their beliefs after seeing a signal, but where it may be challenging to understand
4Enke and Graeber run a variety of experiments, including one mirroring our abstract experiment. As in
their paper, we also find that cognitive uncertainty correlates with insensitivity to signal strength, but this
now leads to greater overinference from weak signals (which they did not include in their experiment).
5A smaller, growing literature uses sports-betting data to similar ends. As a relevant recent example,
Moskowitz (2021) shows that betting returns from the open of betting to the start of a game predict reversals
from there until the end of the game. We focus instead on variation within a game.
6While we do not provide direct evidence, our theory suggests an interpretation that earnings surprises
are strong news about short-term fundamentals (generating underreaction), while even a string of news gives
fairly weak information about the long-run or aggregate regime (leading to overreaction), loosely in the spirit
of Barberis et al. (1998). Separately, Giglio and Shue (2014) document underreaction to the passage of time.
We view this as underattentiveness to certain relevant aspects of information, as modeled in Section II.D.
7That said, we provide only a high-level theory of what default “intermediate” signal strength people
shrink toward. The results of Kwon and Tang (2024) suggest that salience of outliers in past data may be
important for determining this default strength for a given type of signal.
8

the strength of the signal, even if the signal is perfectly observed. There are a variety of
reasons why a person may find it di"cult to fully comprehend the signal strength. In contexts
where the signal strength and correct posterior can in theory be calculated directly (e.g., in
controlled experiments), the person could have issues undertaking a set of potentially complex
mental calculations, but may nonetheless have the ability to generate a rough estimate. In
real-world settings, the person may not fully understand the exact data-generating process,
but may nonetheless have a simplified model of the process. Similarly, the person may only
be able to appreciate parts of a complicated signal and thus generate an incomplete estimate
of its strength. In each case, the person is using a cognitive process — whether conscious and
deliberative or unconscious and automatic — to form an estimate of the signal strength. Our
goal is to provide a framework that is broad enough to capture these di!erent situations.
After setting up the model in II.A, we show how overinference from weak signals and
underinference from strong signals arises from a set of simple and intuitive (potentially
non-Bayesian) updating rules. In II.B, we study a parameterized model to derive a more
concrete relationship between strength and reaction, which we then use in our experimental
analysis. In II.C, we consider how incorrect priors, base-rate neglect, or uncertainty about
direction may a!ect the analysis. In II.D, we broaden the analysis to consider multiple people
with possibly correlated estimates, providing a specific example arising from limited attention.
II.A. Setup and Main Results
Setup. We considerapersonwhoreceives anarbitrarysignal s aboutabinarystate ω 0,1 ,
→{ }
with s generated according to the likelihood function p(s ω). As a benchmark for
→S |
comparison, we denote the correct prior that ω = 1 by ε and the Bayesian posterior given s
0
as ε (s), or ε .
1 1
To formalize the idea that some aspects of a signal are easier to understand than others,
we break the signal into two components, s = (s ,s ). The first component, s , determines
d m d
the direction of updating and accordingly can only take two values, “positive” or “negative.”
Given a positive (negative) directional signal, the Bayesian posterior is always above (below)
the prior.8 Given the direction, the second component s m R determines the magnitude or
→
strength of the signal. We define signal strength S formally as
p(s ω = 1)
(1) S(s) log | ,
↑ ! "p(s ω = 0)#!
! | !
! !
! !
! !
which is the magnitude of the log odds ratio of the signal. Defining logit(x) log x , a
↑ 1 x
→
$ %
8Formally, s is such that ω (s =positive,s ) ω ω (s =negative,s ) for any s and s . Note
d 1 d m
↓
0
↓
1 d →m m →m
also that all p() can be understood either as mass functions or densities, while P() refers to a probability.
· ·
9

Bayesian updates such that
(2) logit(ε (s)) = logit(ε ) S(s) .
1 0
±
Logitof Logitof Signal Signal
Posterior Prior Direction Strength
& ’( ) & ’( ) (fr&o’m()sd) (from&’s( m )
|
sd)
Consequently, fixing ε , a signal s with a greater signal strength S(s) will lead to a larger
0
absolute change in beliefs ε (s) ε .
1 0
| ↔ |
Estimates of Signal Strength. Our main behavioral assumption is that a person fully under-
stands the direction of the signal, but does not fully understand the magnitude. Instead,
we assume that people use some internal process to form a guess about S, which we call
an estimate e R. While the Bayesian uses the information in the signal s = (s
d
,s
m
), the
→
person we consider uses the information in sˆ (s ,e).
d
↑
We consider the behavior of the person’s perceived signal strength given S, as the perceived
signal strength determines the person’s inference from the signal. In Section II.B below, we
take the traditional approach of assuming that the person is a constrained Bayesian: they only
receive a noisy estimate of the strength, and they update correctly given the joint distribution
of signal strengths and estimates. From these assumptions, we derive the parameterized
relationship between signal strength and reaction. Our initial goal in this section, however,
is to demonstrate the generality of our main e!ect given very minimal assumptions on
the distribution of e and assuming intuitive (and potentially non-Bayesian) updating rules.
That is, rather than deriving updating rules under specific (and likely unrealistic) Bayesian
assumptions, we show how our e!ect occurs under a broad class of updating rules.
Reasonable Estimates and Updating Rules. We start with a minimal set of restrictions on the
distribution of estimates given a signal strength, requiring that the estimate be a well-ordered
approximation of the true strength:
Assumption 1. For each direction s ,9 estimates are formed such that:
d
(a) e is unbiased: E[e S] = S.
|
(b) e is well-ordered: p p ( ( e e | | S S = = S S 2 1 ) ) strictly increases in e for all S 2 > S 1 .
(c) e is imperfect: there is no pair (e,S) such that P(S e) = 1.
|
Part (a) is e!ectively a normalization such that the estimate is centered around the correct
signal strength. Part (b) assumes the strict monotone likelihood ratio property (MLRP) on
9We allow all statements to potentially condition on s , but we leave this conditioning implicit to ease
d
notation for the distribution of e. That is, p(eS) is shorthand for p(es
d
,S), and so on for related expressions.
| |
10

estimates. This commonly used property implies that higher estimates are associated with
higher levels of S; under Bayesian updating, this implies that posteriors for S are monotonic
in e (Milgrom 1981). In our case, we impose MLRP to ensure that the distribution of
estimates is well-behaved enough to be able to make general statements even in cases of
non-Bayesian updating. Part (c) rules out trivial cases in which e fully reveals the signal
strength S. This implies that the set of feasible signal strengths is non-degenerate.
Next, we consider the person’s prior perceptions of signal strength. Before observing
ˆ
any information, the person has some subjective expectation S of signal strength S. After
0
observing if s is positive or negative (but before incorporating the estimate e), the person
d
updates this expectation to S ˆ (s d ). We do not require these expectations to be correct, but we
do require the minimal assumption that they be within the feasible set of signal strengths:
Assumption 2. S ˆ (s d ) is strictly between min sm S(s d ,s m ) and max sm S(s d ,s m ).
Given the above expectation S ˆ (s d ) of S, the person then generates an estimate e following
Assumption 1. How will the person update given their prior expectation and this new
signal? Instead of requiring Bayesian updating, we assume only that the person’s posterior
expectation of signal strength S ˆ (sˆ) = E ˆ [S s d ,e] will move from S ˆ (s d ) toward e:
|
Assumption 3. For all sˆ, the posterior S ˆ (sˆ) is strictly between the prior S ˆ (s d ) and estimate e.
Crucially, given that the estimate is noisy, we assume that the person will not update all
the way to e. This intuitive property is referred to as “updating toward the signal” (UTS)
by Chambers and Healy (2012), who show that it is satisfied in many commonly studied
updating environments.10 We are, in e!ect, assuming implicitly that the person is aware that
their internal estimate is noisy and therefore shades their signal-strength belief toward their
prior. Note that we place no further restriction on how much the person updates from a
given e: for all sˆ, there exists some ϑ (0,1) such that S ˆ (sˆ) = ϑe+(1 ϑ)S ˆ (s d ), but the
→ ↔
signal weight ϑ need not be constant and may vary with e (and with s ).
d
To summarize, the person observes a signal s = (s ,s ) containing both directional and
d m
magnitude information. A Bayesian would correctly interpret this signal as having strength
S(s). In contrast, the person in our model understands s
d
but doesn’t fully understand s
m
and therefore cannot fully resolve S(s). Instead, she forms a reasonable, well-ordered, but
noisy estimate e of S(s). She then uses a very general and intuitive updating rule using
sˆ= (s d ,e) to form her expectation of signal strength S ˆ (sˆ).
10As Chambers and Healy note, some papers assume UTS directly (e.g., Shapiro 1986; Moore and Healy
2008), as we do. Note that we assume strict UTS, rather than a weaker version in which S ˆ(s d ) S ˆ(sˆ) e.
↗ ↗
11

Overinference and Underinference. Our primary objective is to study whether a person is
over- or underinferring relative to the full (signal-understanding) Bayesian benchmark. While
the Bayesian’s view of the signal strength is fixed at S(s) given a signal s, a person’s perceived
S ˆ (sˆ) depends on their estimate e, which is stochastic. Consequently, we focus on the expected
perception E[S ˆ (sˆ) s], and we define over- and underinference in the following natural way.11
|
Definition. The person overinfers from s if E[S ˆ (sˆ) s] > S(s) and underinfers from s if
|
E[S ˆ (sˆ) s] < S(s).
|
Our main result is that this person is biased in their perception of signal strength:
Proposition 1 (Over- and Underinference). Thepersonoverinfersfromweaksignals
and underinfers from strong signals: there exists a unique switching point S↑ such that they
overinfer from s if S(s) < S↑ and underinfer if S(s) > S↑ .
The proof, provided in Online Appendix A.1, involves expressing E[S ˆ (sˆ) s] S(s) as an
| ↔
expectation of a single-crossing function g(e) with respect to the conditional distribution
p(e S(s)). Then, using a well-known result (formalized by Karlin 1968, among others)
|
referred to as the variation diminishing property, the fact that p(e S(s)) satisfies the MLRP
|
(by Assumption 1) implies that E[S ˆ (sˆ) s] S(s) is single-crossing as well: in particular,
| ↔
E[S ˆ (sˆ) s] S(s) > 0 for small S(s) and E[S ˆ (sˆ) s] S(s) < 0 for large S(s), with a unique
| ↔ | ↔
interior switching point S↑ .
Although this proof is slightly involved, the results are intuitive. First, consider the
extreme case in which the person places no weight on their strength estimate e (because, for
example, the estimate is extremely noisy). The person will e!ectively be fully insensitive to
signal strength, such that they expect the same intermediate strength (S ˆ (s
d
)) regardless of
actual strength S. This leads to overinference when S is low and underinference when S is
high. As the weight on e rises, the person will still shrink toward an intermediate strength as
compared to a full Bayesian. The resulting partial insensitivity to signal strength leads to
overinference from weak signals and underinference from strong signals on average.
Note that under our general assumptions, it is not necessarily the case that a person’s
expected signal strength S ˆ (sˆ) is monotonic in e or that the amount of over- or underinference
11Givenourfocusoninferencefromsignalsofvaryingstrengths,wedirectlydefineover-andunderinference
in terms of mean perceived signal strength. Fixing ω , this intuitively corresponds to over- and underreaction
0
in beliefs, as belief changes logit(ωˆ 1 (s)) logit(ω 0 ) are generally monotonic in perceived strength S ˆ(sˆ). This
| ↔ |
connection can fail given the non-linear mapping from signal strength to beliefs, but it will hold to first order
(e.g., in a small-noise limit, as in Khaw, Li, and Woodford 2021, Appendix G). We can also simply modify
Assumptions 1–3 to focus on beliefs (so e is an estimate of the correct ω ), in which case our results will hold
1
for beliefs. Unless stated otherwise, we assume throughout that belief changes are monotonic in S ˆ(sˆ) with the
correct direction.
12

E[S ˆ (sˆ) s] S(s) is monotonic in S(s).12 Online Appendix A.1 provides conditions under which
| ↔
these additional monotonicity results will hold: as long as the weight placed on the estimate
does not fall dramatically given small increases in e S ˆ (s d ) , then S ˆ (sˆ) will be monotonic
| ↔ |
in e; and as long as the weight does not increase strongly in e, then E[S ˆ (sˆ) s] S(s) will be
| ↔
monotonic in S(s).
II.B. Parametric Example: Updating with Log-Normal Estimates
In the previous subsection, we showed how a person following a set of intuitive (but potentially
non-Bayesian) updating assumptions will overinfer from weak signals and underinfer from
strong signals. We now specialize the model to show that a quasi-Bayesian facing log-normal
distributions will also update following the predictions in Proposition 1, with the updating
rule taking a particularly simple form that will then guide our experimental analysis.13
First, we assume that signal strength is log-normally distributed with logS (µ ,ϖ2),
↘N S S
regardless of direction. A Bayesian’s expectation of signal strength after seeing either direction
is thus S ˆ (s d ) ↑ E[S | s d ] = exp(µ S +ϖ S 2/2). Next, givenaspecific strength S, we assume thatthe
person’s estimate e is log-normally distributed, loge (logS ϖ2/2,ϖ2). The correction
↘N ↔ e e
ϖ2/2 ensures that the estimate is centered around the true signal strength: E[e S] = S.
↔ e |
How will a Bayesian then react to e? Using standard results given a log-normal likelihood
and conjugate prior, the updating rule for expected signal strength is
ϖ2 ϖ2
(3) S ˆ (sˆ) = exp *" 1 ↔ ϖ2 + S ϖ2 # · logS ˆ (s d ) + "ϖ2 + S ϖ2 # · loge+ϖ e 2/2 + .
e S e S $ %
Posterior (LogAdjusted) (LogAdjusted)
Exp & e ’ c ( ta ) tion We P ig r h io t r on Prio & rEx ’ p ( ecta ) tion W E e st ig im ht at o e n & Est ’ im ( ate )
& ’( ) & ’( )
Intuitively, the Bayesian will take a weighted average of the adjusted prior and estimate
in log space, and then exponentiate to form their posterior expectation of strength. The
weight on the imperfect strength estimate depends on the relative precision of the estimate
versus the prior: as the precision of the estimate rises, the weight on the estimate rises; as
the precision of the prior rises, the weight on the estimate falls.
Given this updating rule, people will overinfer from weak signals and underinfer from
strong signals on average, with a simple and estimable functional form for the e!ect. In
12For example, if a person updates from their prior S ˆ(s d ) strongly toward the estimate e 1 but very weakly
toward the estimate e 2 =e 1 +ε, the person can have a large drop in S ˆ(sˆ) from a small increase in e.
13Theupdatingruleissimilartooneobtainedfromdi!erentfoundations(basedonKhaw,Li,andWoodford
2021 and Woodford 2020) in a previous version of this paper (Augenblick, Lazarus, and Thaler 2023).
13

Figure I. Theoretical Predictions of Over- and Underinference by Signal Strength
3
1
.3
.1
.03
htgnertS
deviecreP
2.5
2
1.5
1
.5
.03 .1 .3 1 3
True Signal Strength
langiS
no
thgieW
Our Model (Parametric)
Constant Overinference
Constant Underinference
Bayesian
.5 .6 .7 .8 .9 1
Signal Precision
Notes: Thesefiguresprovidetworepresentationsofthecoredeviationinourmodel. SolidlinescorrespondtoBayesian
updating(correctperceptionofsignalstrengthS),dotteddashedlinestounderinference(withperceivedsignalstrength
0.8 S), short dashed lines to overinference (perceived signal strength 1.2 S), and darker dashed lines to the over- and
und · erinferencebehaviorintheparametricversionofourmodel(perceivedsig · nalstrengthk Sω withk=0.88andω=0.76,
·
asestimatedfromStudy1a). Theleftpanelplotssignalstrengthperceptionasafunctionofsignalstrengthonalog-log
scale. Therightpanelplotstheweightputonsignalsasafunctionofthetrueprecision. Bothfiguresshowthatourmodel
predictsoverweightingofweaksignalsandunderweightingofstrongsignals.
particular, the expectation of S ˆ (sˆ) = S ˆ (s d ,e) over the distribution of estimates is
(4) E[S ˆ (sˆ) s] = kS ω,
|
where ϱ ↑ ϖ S 2/(ϖ S 2 +ϖ e 2) → (0,1) and k ↑ exp(ϱ2ϖ e 2/2)S ˆ (s d )1 → ω. Note that E[S ˆ (sˆ) | s] ↓ S if
1
and only if S
↗
S↑
↑
k1
→
ω. That is, as in Proposition 1, people overinfer from signal strengths
below S↑ and underinfer above S↑ .
The relationship between reaction and signal strength given this setup can be represented
and visualized in a number of ways. Taking logs of (4) yields
(5) log(E[S ˆ (sˆ) s]) = log(k)+ϱlog(S),
|
such that there is a log-linear relationship between the expected and true signal strength,
with a positive intercept and a muted slope between 0 and 1. The left panel of Figure I
plots this relationship given the parameters k and ϱ we estimate from our first experiment
(discussed further in Section III). For comparison, we also plot the relationship for a Bayesian
(for which they are equal), a person who exhibits constant underinference, and a person who
exhibits constant overinference.
This relationship can also be represented in terms of the e!ective weight a person places on
a signal with strength S. While a Bayesian observing the full signal will update following (2)
14

using S, a person in our model updates as if the signal strength is, on average, wˆ(S)S for
some weight function wˆ(S). The full Bayesian e!ectively uses w(S) = 1, while for our model,
(6) wˆ(S) = kS→ (1
→
ω).
This weight is greater than 1 for weak signals and less than 1 for strong signals. Note that
wˆ(S) approaches 1 as ϱ 1, so the degree of over- and underinference shrinks as the person’s
≃
estimation process becomes more precise.
Rather than using the relationship in (6) directly, we often follow past literature (Benjamin
2019) and focus on the relationship between the inference weight and signal diagnosticity or
precision ς(s). For a symmetric signal (where p(s ω = 1) = 1 p(s ω = 0)), signal precision
| ↔ |
is ς(s) max p(s ω = 1),p(s ω = 0) = logit
→
1(S(s)), which is a monotonically increasing
↑ { | | }
transformation of strength S(s).14 The qualitative relationship between weight and precision
matches the relationship between weight and strength. In particular, the weight wˆ(s) is
above 1 for low precisions and below 1 for high precisions:
(7) wˆ(s) = (logit(ς )) (1 ω) logit(ς(s)) (1 ω),
↑ → → → →
| |
1 1
where ς ↑ ↑ 1+exp( ↔ k →1 → ω) → is the switching point. The right panel of Figure I plots
this relations$hip, again using p%arameters k and ϱ estimated from the experiment and again
as compared to Bayesian updating, underinference, and overinference. We return to these
graphs in Section III.
II.C. Relaxing Assumptions
Prior Belief Distortions. We have assumed to this point that the person starts with a correct
prior, εˆ = ε . If the person has an incorrect prior that is observable (and otherwise updates
0 0
according to the assumptions in II.A), it is straightforward to correct for the distortion
induced by εˆ = ε in our empirical analysis. Rather than estimating perceived signal
0 0
⇐
strength using logit(εˆ (s)) logit(ε ) from (2), the incorrect prior can be controlled for by
1 0
| ↔ |
using logit(εˆ (s)) logit(εˆ ) . The person uses their perceived signal strength to update
1 0
| ↔ |
from their prior to their posterior, so perceived strength can be backed out from the posterior
and prior, and Proposition 1 continues to provide testable predictions. Note that this is true
even if the person’s prior εˆ arose after updating from an estimate of the previous-period
0
signal. In this case, even though the person used a noisy estimate and was insensitive to the
past signal strength, εˆ incorporates this uncertainty. See Online Appendix A.3 for details.
0
14Signal precision is by definition between 1/2 and 1. When ω =1/2 (as in our first experimental study),
0
the Bayesian posterior after a positive signal is equal to the signal precision, ω (s)=ϑ(s).
1
15

This analysis becomes more complicated if the person’s prior is not observed, or if the
person uses their prior in a non-standard way (e.g., with base-rate neglect). For example,
suppose that an experiment provides a person with both an endowed prior ε and a signal s
0
simultaneously, and asks for a single updated posterior. If people are unsure how to use both
the prior and the signal, or use a distorted version of the prior due to base-rate neglect, their
single answer will reflect both their prior distortion and our e!ect. Online Appendix A.3
discusses in more detail how these prior distortions contaminate people’s reactions and when
they potentially overwhelm our e!ect. We use two approaches in our experiments to control
for this issue. In Study 1a, we focus on uninformative priors ε = 0.5, where biases like
0
base-rate neglect have no impact. In Studies 1b and 2, we vary the prior and then control for
potential base-rate neglect using a regression approach following Grether (1980).
Uncertainty About the Direction. Our theory is geared to situations in which people know
the correct direction to update, but are unclear about the strength. In this case, imperfect
estimates lead to insensitivity to strength, which leads to our main e!ect. We can extend the
model to situations in which the person is unsure about both the direction and strength of the
signal(suchthatthepersonformsanestimateeofsigned signalstrengthSsigned
↑
log p
p
(
(
s
s
| ε
ε
=
=
1
0
)
)
|
and does not observe the direction directly). This version of the model is closely r$elated t%o
that of Enke and Graeber (2023) (except that we work in signal-strength space instead of
probability space), and we also predict that insensitivity without directional information
generally leads to underinference.15 Intuitively, if people do not know the directional meaning
of a signal, they shade toward a reaction of zero. See Online Appendix A.3 for details.
II.D. Multiple People, Limited Attention, and Correlated Estimates
The analysis thus far has focused on the expected reaction of a single person. In this section,
we instead consider the average response across di!erent people i = 1,...,N (where N should
be thought of as large). A natural preliminary way to extend our analysis to this case is to
assume that each person understands the direction s and generates a mutually independent
d
strength estimate e . That is, people see the same signal and agree on its direction, but there
i
is diversity in people’s estimated signal strengths due to di!erent interpretations, models, or
perceptions of the problem. Under this assumption, our results (immediately) continue to
hold across people. Specifically, define the expectation over people given s as Ei [ s] and the
·|
person-specificstrengthperceptionasS ˆ
i
(sˆ
i
). Then, ratherthanfocusingonexpectedperceived
15That said, our definition of underinference becomes strained in this context, so we are reluctant to make
strong statements. For example, suppose the correct signed signal strength is 2, but a person perceives it to
be -1. Is this an under- or overinference? In our main model, this issue does not arise because we assume
that the correct updating direction is known, which we believe is typically the case in our empirical settings.
16

strength of an individual across potential estimates E[S ˆ (sˆ) s] as in Proposition 1, the same
|
results hold taking the expectation across people Ei [S ˆ i (sˆ i ) s] (see Online Appendix A.4 for a
|
more formal discussion). Intuitively, under the assumption that estimates are independent
across people, there is no formal distinction between taking the expectation with respect to
the distribution of estimates and taking a cross-sectional expectation across people.
The assumption of independent estimates is appropriate for some situations. For example,
in Study 2, we ask people to update their subjective probability of a team winning a basketball
game after observing a made or missed basket in simple situations. We find that people’s
perceptions of the strength of a given signal tend to be diverse and smooth, presumably
because people have di!erent ways of using their knowledge and experiences to estimate its
e!ect. Similarly, in Studies 1a and 1b, signals are presented in a computationally challenging
form (e.g., a signal with conditional likelihood 202/337). We again find similar diversity
and smoothness in responses, likely because people have di!erent estimates of the precise
value of this number and how to use it to form a posterior. However, there are also natural
situations in which people might form correlated estimates of a given signal’s strength. For
example, people may have similar simplified models of a given DGP or similar strategies for
combining available information to determine a signal’s meaning. Similarly, some dimensions
of a piece of information may be more salient than others, such that people incorporate
similar dimensions in forming their estimate of signal strength. These cases will lead to
correlated estimates across people and potentially non-smooth multimodal posterior belief
distributions, as in Bordalo et al. (2023).
Example: Limited Attention. To study correlated estimates more formally, we consider a
case in which the signal’s strength component (the second entry in s = (s ,s )) has multiple
d m
dimensions: s = (s ,...,s ). While a Bayesian uses all components to determine
m m,1 m,n
signal strength, people in our model have limited attention, limited processing ability, or
attend specifically to certain features of the signal, such that they only appreciate a subset of
components. Correlation in estimates will occur if people focus on the same components.
Specifically, we assume that regardless of direction, the components s are independently
m,j
and identically distributed (µ ,ϖ2 ), and the true log signal strength is the average of these
N S m
components:
1 n
logS = s
m,j
.
n
j=1
,
Consequently, signal strength is log-normally distributed, logS (µ ,ϖ2), with ϖ2 = ϖ2 /n.
↘N S S S m
While a Bayesian uses all n components and can determine S, person i only attends to n
i
n
↗
of the components, captured in a fixed person-specific vector a 0,1 n, where a = 1 if
i i,j
→{ }
17

the person attends to component j. Given this setup, person i’s best (log) estimate of S is
1 n ϖ2
loge = 1(a = 1) s e,i,
i i,j m,j
n · ↔ 2
i j=1
,
whereϖ
e
2
,i
= n
n → · n
n
i
iϖ
m
2 = n
→ ni
niϖ
S
2 (withtheterm
↔
ϖ
e
2
,i
/2againincludedsothatE[e
i |
S] = S). The
estimate e
i
is log-normally distributed conditional on S, loge
i ↘N
(logS
↔
ϖ
e
2
,i
/2,ϖ
e
2
,i
). This
settingthusmapstotheoneinSectionII.B,withϖ2 = ϖ2 /nandϖ2 = ϖ2 = (n n )ϖ2 /(n n ).
S m e e,i ↔ i m · i
That is, that model can be microfounded with people who only consider a subset of the
full signal.16 Crucially, however, this multi-component model produces correlated updating
behavior across people, governed by the overlap in a across i.
i
This correlation can create a specific type of violation of Proposition 1. That result says
that all signals s of a given strength S(s) will lead to over- or underinference in the same
way on average. But in this setting, the same is not necessarily true. To take an extreme
example, if everyone focuses on the same components, then they will have the same estimate
e i for a given signal s. While this estimate is random conditional on S (it is drawn from a
distribution with mean S), it is not random conditional on the full signal s (since s contains
the entries that will be used to determine loge ). This suggests a simple adjustment under
i
which our results do apply: when over- and underinference are defined conditional on S rather
than s, then a version of the proposition holds (see Online Appendix A.4). That is, our
results hold when averaging over signals of the same strength.
Finally, as we discuss in Online Appendix A.4, it is possible to obtain more precise
predictions about the correlation in updating behavior under di!erent sets of assumptions
about the signal components or attention vectors. If there are few components or all people
are drawn to a small set of salient components, people’s estimates will be correlated, and
we may see multimodality in responses.17 If people must estimate a probability given a
complex DGP and a rich signal, or if the main salient part of a signal is the direction s (as
d
may sometimes apply in time-series settings), we might expect more independent strength
estimates and smoother distributions of resulting strength perceptions.
To summarize, we model an updating environment in which a person knows the directional
meaning of signals, but only forms a rough estimate of the exact strength. As this estimate is
16The strength sensitivity parameter ϖ in (4) becomes ϖ =n /n. So fixing n, an increase in n (e.g., due
i i i
to greater sophistication) should lead to less-noisy estimates and less insensitivity to true strength for person
i. An increase in n (e.g., from a more complicated signal) should generate the opposite behavior for all i.
17For example, if an abstract problem only includes a few numbers representing the “prior” and a “signal,”
we might see some people focusing on the prior, some on the signal, and some on both. Bordalo et al. (2023)
provide a richer foundation and set of predictions for this form of behavior arising from bottom-up attention
to salient features, which further speaks to instability across problems with the same correct answer.
18

imperfect, the person shades their perceived strength toward some intermediate value, which
leads to overinference from weak signals and underinference from strong signals on average.
In the following sections, we test this core prediction for updating in a range of environments.
We also predict that the e!ect will be dampened as a person’s estimate becomes more precise.
Estimation precision will increase with more thought or sophistication, more experience, or
attending to more components in a multi-dimensional problem. While estimation precision is
not directly observable, we test this relationship using a variety of proxies in our experiments.
III. Experimental Evidence
To test our core prediction that people overinfer from weak signals and underinfer from
strong signals, we design and conduct three experiments. Each experiment studies the causal
e!ect of varying signal strengths on participants’ updating behavior and, by implication,
the level of over- and underinference. The first experiment (“Study 1a”) adapts a classic
belief-updating design from Green, Halbert, and Robinson (1965). The next experiment
(“Study 1b”) replicates the first experiment and expands the analysis by varying the prior
and eliciting a more direct proxy for precision in signal strength estimates. The final study
(“Study 2”) uses a novel naturalistic design in which participants predict the win probability
of basketball games. Each study was preregistered,18 and we largely follow the preregistration
plans, although some of the estimated results from the first study are placed in Online
Appendix B to conserve space. We note these cases in the main text.
III.A. Study 1a: Abstract Updating Experiment
Design. The design of the first experiment follows the broad “bookbag-and-poker-chips” (or
“balls-and-urns”) paradigm, which is a benchmark design for measuring underinference and
overinference in past literature (Benjamin 2019). Participants are told that there are two
card decks, each with N cards. One deck is labeled as Green, and the other is labeled as
Purple. Each deck is composed of Diamond and Spade cards, with the Green deck having D
1
Diamonds and N D Spades and the Purple deck having D Diamonds and N D Spades.
1 2 2
↔ ↔
In the main treatment, the computer chooses either the Green or Purple deck with equal
probability. Participants do not observe the color. Instead, participants are shown the suit
of a single card drawn from the chosen deck. Given this signal, participants are asked to
provide a percent chance that the chosen deck is Purple or Green. These probabilities are
restricted to be between 0 and 100 percent and must sum to 100. In addition to the main
18Study 1a: https://aspredicted.org/ax4wg.pdf; Study 1b: https://aspredicted.org/8Q4_6Y9;
Study 2: https://aspredicted.org/SYW_QWF.
19

treatment, there are treatments with multiple draws of cards, elicitation of willingness-to-pay
for drawing cards, and where the signal precision is unknown. The timing of the treatments
and more details are described in Online Appendix B.1. Screenshots of the experimental
interface are contained in Online Appendix C.
The relative proportion of suits in each deck determines the signal strength of observing
a card. For example, if the Purple deck contains a large proportion ς = D /N of Diamonds,
1 1
while the Green deck contains a very small portion ς of Diamonds, a Diamond card is
2
a strong signal that the chosen deck is Purple. Given our core prediction, we vary these
proportions to vary signal strength. Following the literature, we largely focus on symmetric
signal structures, in which ς ς = 1 ς . We choose 32 possible values of ς within the
1 2
↑ ↔
range [0.047, 0.495] or [0.505, 0.953]. These values correspond to 16 possible signal strengths
(S = logit ς ) in the range S [0.02,3.00].19 On each question, we randomized whether
| | →
the Green deck or Purple deck had more Diamonds or Spades, which suit was chosen, and
whether the number of cards in a deck N was 1665 or 337.20
We use monetary incentives to elicit participants’ beliefs, as incentives have been shown to
improve decision-making in these settings (e.g., Grether 1992). We implement a version of the
binarized scoring rule (Hossain and Okui 2013) that is easier for participants to comprehend:
paired-uniform scoring (Vespa and Wilson 2017).21 Participants’ answers determine the
probability that they win a high bonus as opposed to a low bonus.
Implementation. Study 1a was conducted in March 2021. Participants were recruited from
the online platform Prolific (prolific.co). Prolific was designed by social scientists in order
to attain more representative samples online; it has been shown to perform well relative
to other participant pools (Rigotti, Wilson, and Gupta 2023). 500 participants completed
the experiment and passed the attention check, of whom five were randomly chosen to win
bonuses (either a high bonus of $100, or a low bonus of $10). All participants received a $3
show-up fee, and the average bonus earnings for the selected participants was $82.
Participants play 12 rounds in the main part of the study, in each of which they observe
one draw of a card. We elicit 6,000 predictions in this part: 4,036 from one symmetric signal,
and 1,964 from one asymmetric signal. To test that participants have a basic understanding
of the setting, we randomly make 72 signals fully uninformative.22 The rest of the study
19More specifically, we choose whole numbers of cards such that signal strengths would be closest to the
following values: 0.02,0.05,0.10,0.15,0.20,0.30,0.40,0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.50,3.00 .
{ }
20The deck sizes are intentionally large and irregular to (1) allow for a wide range of signal strengths,
(2) remove clear anchor points for people’s answers, and (3) induce some uncertainty in mental calculations.
21In general, binarized scoring rules have been argued to better account for risk aversion and hedging than
other incentive rules (Azrieli, Chambers, and Healy 2018).
22That is, both decks have exactly the same composition, so the correct update is to stay at 50 percent.
Reassuringly, 96 percent of participants answer exactly 50 percent.
20

Figure II. Study 1a: Over- and Underinference by Signal Strength
3
1
.3
.1
.03
htgnertS
deviecreP
2.5
2
1.5
1
.5
.03 .1 .3 1 3
True Signal Strength
langiS
no
thgieW
Data
Parametric
Bayesian
.5 .6 .7 .8 .9
Signal Precision
Notes: Theleftpanelplotstheperceivedsignalstrength(thelogitbeliefchange)asafunctionoftruesignalstrengthona
log-log scale. The right panel plots the average weight participants put on signals relative to a Bayesian for whom the
weightis1. Inbothpanels,blackmarkersplotthedata(with95%confidenceintervals). Observationsarewinsorizedfor
eachsignalstrengthcategoryatthe5%and95%level. Dashedlinesfitthedatausingthepowerweightingfunctionfrom
equation(6),estimatingparametersusingnonlinearleastsquares. ThickersolidlinesindicateBayesianbehavior. Both
panelsshowthatparticipantsoverweightweaksignalsandunderweightstrongsignals.
includes an attention check, multiple draws of cards, demand for information, and signals with
ambiguous strength. Given space constraints and to emphasize our core results, we largely
focus on the main treatment, where people see one symmetric signal and signal strength does
not depend on the signal realization. Details for the additional treatments are in Online
Appendix B and a previous working-paper version of this paper (Augenblick, Lazarus, and
Thaler 2023, or ALT 2023).
Main Results. In the main condition where signals are symmetric, the signal precision from
learning the suit of one drawn card is ς = ς = ς . Given that the prior is 1/2 (both decks
1 2
are equally likely to be chosen), a Bayesian will place probability ς that the card was drawn
from the deck that contains more of that card’s suit.
We used Figure I in the theoretical section to visually represent our core predictions under
the log-normal parameterization of our model. Figure II presents the same graphs with the
addition of the actual data from the experiment, where we back out participants’ perception
of signal strength from their posterior (given a fixed prior of 1/2). We compare our estimates
for each condition (black circles) and the fitted predictions of the parameterized model
(dashed lines, described below) with Bayesian updating (solid lines). The left panel shows
that participants’ behavior is not purely random: they qualitatively understand that stronger
signals are in fact stronger, as average perceived signal strength rises monotonically with
true strength. But this relationship is quantitatively muted, so participants systematically
overinfer from weak signals and underinfer from strong signals. As in the parameterized
model, this relationship between true and perceived signal strength is close to linear in logs.
21

The right panel presents the same information in a di!erent way, showing that people
are e!ectively overweighting weak signals and underweighting strong signals, with a shape
that again largely hews to the predictions of the parameterized model. For very weak signals,
participants are acting as if signals are more than twice as strong as they truly are; for very
strong signals, they are acting as if signals are roughly 2/3 as strong as they truly are.
The parametric curves in Figure II are obtained by estimating the model parameters k and
ϱ from equation (6), wˆ(S) = k S→ (1 → ω), using nonlinear least squares. The estimated value
·
for k is 0.88 (s.e. 0.02) and for ϱ is 0.76 (s.e. 0.03). The value of ϱ is statistically significantly
less than one (p < 0.001), as predicted. These values correspond to an estimate for the
switching point ς of 0.64 (s.e. 0.01).23 All standard errors are clustered by participant.
↑
Experiments using this paradigm have been run many times in the past, largely focusing
on higher signal strengths. In Online Appendix Figure A1, we compare our estimates to the
manystudiesdiscussedinBenjamin(2019). Ourresultslineupwithpaststudies’estimatesfor
these higher signal strengths. In particular, we match the literature in finding underinference
for signals with precision at or above 2/3. It is only for signals with precision below 0.6 that
we see overinference, and this is a range that the previous literature had not explored.
To explore our main results more formally in a consistent way across studies, Table I
presents the results of regressions for the weight on the signal, wˆ(S), on a constant and the
true signal strength S. Bayes’ rule would predict a constant of 1 and slope of 0 on S in
such a regression, while our theory predicts a constant above 1 (indicating overinference for
very weak signals) and a slope below 0 (indicating that people are partially insensitive to
signal strength, and switch to underinference for strong signals).24 Column (1) confirms the
relationship suggested by Figure II for Study 1a: the constant is above 1, the slope is below 0,
and both e!ects are precisely estimated and strongly significant.
Heterogeneity. The theory assumes that people use a randomly drawn estimate of signal
strength to form their beliefs. Consequently, it predicts our main e!ect occurs on average,
but also that there will be heterogeneity: some people will overreact and some will underreact
to any given signal. Online Appendix Figure A2 plots the raw cumulative distribution and
probability density functions at the individual level for strong and weak signals. Nearly
everyone updates in the right direction, and the distributions are centered in accordance
with our main e!ect. But given the non-trivial spread in the distributions, there is clear
heterogeneity in perceived signal strength and associated updating behavior.
23Equivalently, people are updating as if the distribution of strengths is such that S↑ =logit(0.64)=0.58.
24Both our model and Figure II suggest a nonlinear relationship between weight and strength. We thus see
thelinearspecificationinTableIasprovidingacleanhypothesistestofthekeye!ectpredictedbyourtheory,
rather than identifying model parameters directly (which we do separately via nonlinear least squares).
22

Table I. The E!ects of Signal Strength on Over- and Underinference
Bayes Theory Study 1a Study 1b Study 2
Dep. Var.: Weight on Signal (1) (2) (3) (4) (5)
Constant 1 > 1 1.420 2.180 2.182 1.706 1.700
(0.030) (0.049) (0.048) (0.024) (0.025)
Signal Strength 0 < 0 -0.308 -0.957 -0.958 -2.078 -2.060
(0.031) (0.065) (0.065) (0.111) (0.112)
Weight on Prior 1 0.980 0.976
(0.013) (0.009)
Participant FE Yes Yes Yes Yes Yes
Round FE Yes Yes Yes Yes Yes
Observations 3964 7500 7500 8000 8000
R2 0.23 0.16 0.17 0.24 0.24
p-val.: Const. = 1 <0.001 <0.001 <0.001 <0.001 <0.001
p-val.: Slope = 0 <0.001 <0.001 <0.001 <0.001 <0.001
Notes: Columns(1)–(5)showOLSestimateswithstandarderrorsinparenthesesclusteredbyparticipant. Thedependent
variableistheweightputonthesignalcomparedtoaBayesian,definedfollowingSectionIIaswˆ(S)=S ˆ/S,wheretheperceived
strengthS ˆisestimatedforagivenobservationfromthelogitchangeinbeliefs. Weightsgreaterthan1correspondtooverinference;
weightslessthan1correspondtounderinference. Ourtheorypredictsaconstantof>1(indicatingoverinferenceassignalsbe-
comeveryweak)andacoe!cientonsignalstrengthof<0(indicatingrelativelymoreunderinferenceassignalsbecomestronger).
Columns(3)and(5)controlforweightonpriorfollowingequation(8),andacoe!cientbelow1indicatesbase-rateneglect.
The model also makes the prediction that the core e!ect will be larger as a person’s
estimate of signal strength becomes less precise. Naturally, we cannot observe the precision
of a person’s internal estimates of strength, and therefore must rely on a set of proxies. To
estimate heterogeneity in treatment e!ects, we then interact these proxies with the signal
strength in regressions for the weight placed on the signal, with results presented in Table II.
Our first proxy for (im)precision uses the standard deviation in a person’s implied signal
weights across the experiment. Intuitively, a person whose estimates have very high precision
will have low variance in these weights, since most weights will be around 1; meanwhile, a
person whose estimates have low precision will have high variance in weights.25 As shown in
column (1) of Table II, our e!ect is stronger (i.e., the interaction term is negative) for people
who have higher standard deviation of their weights on other questions.
Our second proxy for estimation precision is task experience: if people become better
at understanding and estimating signal strength as they get more practice, then they will
be less precise earlier in the experiment (and our core e!ect will be stronger). As shown
25There is a small endogeneity issue in using the same observation to measure a person’s reaction and
also to calculate a person’s weight variance across choices. As a result, we relate a person’s reaction in one
decision to the standard deviation in their weights for all other decisions on similar problems.
23

Table II. Heterogeneity in Treatment E!ects
Study 1a Study 1b
Dep. Var.: Weight on Signal (1) (2) (3) (4) (5) (6)
Constant 1.395 1.416 1.421 2.147 2.183 2.181
(0.021) (0.030) (0.030) (0.037) (0.048) (0.048)
Strength 0.118 -0.072 -0.175 -0.002 -0.698 -0.756
(0.036) (0.009) (0.028) (0.070) (0.089) (0.120)
Strength Noise -0.383 -0.433
⇒
(0.036) (0.046)
Strength Inexperience -0.042 -0.037
⇒
(0.009) (0.012)
Strength CRT Incorrect -0.102
⇒
(0.028)
Strength Uncertainty -0.542
⇒
(0.288)
Base-Rate Neglect 0.980 0.980 0.980
(0.013) (0.013) (0.013)
Participant FE Yes Yes Yes Yes Yes Yes
Round FE Yes Yes Yes Yes Yes Yes
Observations 3964 3964 3964 7500 7500 7500
R2 0.28 0.24 0.23 0.20 0.17 0.17
Notes: OLS,withstandarderrorsinparenthesesclusteredattheparticipantlevel. Thedependentvariableisthe
weightputonthesignalcomparedtoaBayesian,asinTableI.Weightsgreaterthan1correspondtooverinference;
weights less than 1 correspond to underinference. Study 1b controls for weight on prior, whereϑ< 1 indicates
base-rate neglect. Noise is defined as the SD of weights on other questions. CRT incorrect ranges from 0 to 3.
Inexperienceequalsthenumberofroundsremaininginthemainexperiment. Uncertaintyrangesfrom0to1andis
describedinSectionIII.B.Wedonotincludetheestimationprecisionproxiesasseparateregressors,astheyare
absorbedbyeithertheparticipantorroundfixede"ectsincludedinallregressions.
in column (2) of Table II, consistent with this idea, people overweight weak signals and
underweight strong signals by more in earlier rounds of the experiment.
In addition to these two proxies, we also preregistered correlating our e!ects with per-
formance on a three-item cognitive reflection test (CRT; Frederick 2005). In column (3)
of Table II, we find that people with lower CRT scores show the core e!ect significantly
more. We also preregistered looking at an additional heterogeneity by self-reported news
consumption, and indeed find that less experience with news consumption is correlated with
our core e!ect (see ALT 2023).
Extensions: Asymmetric, Multiple, and Ambiguous Signals, and Other Concerns. The main
treatment of the experiment focuses on how people respond to one symmetric signal with a
24

deterministic signal strength. The experiment included additional treatments in which we
relax each of these features. We report some key takeaways here.
First, we consider asymmetric signals such that one deck has a similar share of Spades
and Diamonds, but the other deck does not. We find that our main results continue to hold
for these asymmetric signals, and as suggested by our theory, the more complicated problem
leads to a stronger e!ect. Using the same nonlinear least squares estimation as above, we
estimate a value for k of 0.84 (s.e. 0.03) and for ϱ of 0.56 (s.e. 0.04), with a similar estimated
switching point ς of 0.66 (s.e. 0.01).
↑
Second, in Online Appendix Figure A3, we replicate the finding in Gri"n and Tversky
(1992) that people react less to multiple signals than a single signal with the same overall
strength; in Gri"n and Tversky’s language, participants are underattentive to the weight of
evidence. The reduction in reaction to multiple signals is essentially constant for all strengths,
so this e!ect is orthogonal to our main e!ect. Third, we consider ambiguous signals by telling
participants that the share of suits in each deck is equal to one of two possible values (high or
low). Our main e!ect continues to hold, and results suggest that people first estimate each
possible signal strength, and then average these estimates, to form their overall expected
strength (see ALT 2023 for further details).
Finally, we consider a set of alternative hypotheses for our results that are unrelated
to over- or underinference. Our results are not explained by participants being averse to
not updating when signals are not informative; they also cannot be explained by reactions
to particular components of the experiment, for example being influenced by the relative
salience of the first deck or the second deck (or the Green and Purple color), positive or
negative signal, the suit of the signal, or the particular deck size.26
III.B. Study 1b: Follow-Up Experiment
Design. To probe the robustness of the results from Study 1a, we run a follow-up in Study 1b
using the same general design, but now considering asymmetric prior beliefs. Given our
focus on the robustness of the main results, Study 1b drops the additional treatments in the
original study and focuses on the reaction to a single symmetric signal.
To allow for asymmetric prior beliefs, we vary the probability that the first (Green) deck
is chosen. In the original study, the chosen deck is picked randomly from 2 decks, such that
the likelihood of picking the Green deck is 1/2. In order to vary this prior likelihood in a
2696% of participants who see a completely uninformative signal say exactly 50 percent. We also see below
that results are very similar when the prior is equal to 33.3%, suggesting that results are not driven by a
preference for stating the closest round number above/below the prior given a weak signal. We find a tightly
estimated null e!ect of color and suit asymmetry, and only modest di!erences when the deck size varies
between 1,665 and 337. Again see ALT (2023) for further details and discussion.
25

salient way, Study 1b includes treatments in which there are 2, 3, or 4 decks, and each deck
is chosen with equal probability (1/2, 1/3, or 1/4, respectively). As in the original study, the
first deck is Green and has D Diamonds and N D Spades. The other decks are di!erent
1 1
↔
shades of Blue and have identical compositions of N D Diamonds and D Spades. Given
1 1
↔
this setup, the signal strength matches that of the original study, but the person’s prior that
the Green deck is chosen is either 1/2, 1/3, or 1/4.27 After the suit of the drawn card is
shown to the participant, we elicit the probability that each deck was chosen. Our analysis
considers the stated probability for the Green deck as the belief outcome of interest.
Implementation. Study 1b was conducted in March 2024. Participants were again recruited
on Prolific. As preregistered, 500 participants completed the experiment and passed an
attention check. Ten participants were randomly chosen to win bonuses. If they won the
high bonus, they received $50; if not, they received no bonus. All participants received a
$3.60 show-up fee, and the average bonus earnings for the selected participants was $35.
Participants played 15 rounds in the study, in each of which they received one draw of a card.
The experiment involved three blocks of five rounds. Each block gave participants a di!erent
prior, in which the Green deck, as above, had either a 1/2, 1/3, or 1/4 probability of being
chosen.
Results. We first visually present the main results in Figure III, which replicates Figure II
using the new data from Study 1b. We find that the broad patterns in the logit belief changes
(in the left panel) and resulting implied signal weights are very similar to those from Study 1a,
even when allowing for asymmetric priors.
Next, we replicate the regression from Study 1a for the implied weight on the signal, with
results shown in column (2) of Table I. Since wˆ(S) is measured from the logit belief change,
this analysis implicitly assumes that people correctly incorporate the prior probability. But
as discussed in Section II.C, these results may be contaminated if people do not appreciate
or misweight the prior (as is true with base-rate neglect). As such, column (3) estimates and
controls for the e!ect of misweighted priors. In particular, it includes the additional regressor
logitϖ0 in the regression, which (omitting the error term and fixed e!ects) is now
logitϖ1→ logitϖ0
logitε
(8) wˆ(S(s)) = φ +φ S(s)+(ϑ 1) 0 ,
0 1
· ↔ · logitε logitε
1 0
↔
PreviousTerms Base-RateNeglectTerm
& ’( ) & ’( )
27Another way to vary the prior would have been to continue to use two decks, but tell participants that
the Green deck would be chosen with some specific probability. We instead chose the multi-deck design as it
makes the change in the prior more clear and, from our perspective, easier to understand.
26

Figure III. Study 1b: Over- and Underinference by Signal Strength
1.6
.8
.4
.2
.1
.05
noitcaeR
tigoL
)htgnertS
deviecreP(
3
2.5
2
1.5
1
.5
.05 .1 .2 .4 .8 1.6
True Signal Strength
langiS
no
thgieW
Data
Parametric
Bayesian
.5 .6 .7 .8 .9
Signal Precision
Notes: Theleftpanelplotsthelogitbeliefchange(equaltoperceivedstrengthinourtheory)asafunctionoftruesignal
strengthonalog-logscale. TherightpanelplotstheaverageimpliedweightparticipantsputonsignalsrelativetoaBayesian
forwhomtheweightis1. Inbothpanels,blackmarkersplotthedata(with95%confidenceintervals). Observationsare
winsorizedforeachcategoryofsignalstrengthandprioratthe5%and95%level. Dashedlinesfitthedatausingthepower
weighting function from equation (6), estimating parameters using nonlinear least squares. Thicker solid lines indicate
Bayesianbehavior. Bothpanelsshowthatparticipantsoverweightweaksignalsandunderweightstrongsignals.
and an estimated ϑ< 1 represents base-rate neglect.28 Controlling for misweighted priors
does not a!ect our main results: the estimated constant and slope on strength in columns (2)
and (3) are close to identical, and we continue to strongly reject the Bayesian null in the
manner predicted by our theory. If anything, comparing the columns for this study with
column (1) for Study 1a, asymmetric priors seem to strengthen our e!ects, potentially because
signal-strength estimation is more challenging when there are more decks. That said, the
estimates across the two studies may not be directly comparable, as Study 1b uses a more
limited set of signal strengths.
We also analyze the e!ects of asymmetric priors in a specification that follows the Grether
(1980) regression approach more directly:
(9) logitεˆ (s) = ϑ logitε φ S(s).
1 0
· ± ·
To allow for di!erences in inference in response to signals of di!erent strengths, we estimate (9)
separately for each signal strength S(s). The results are presented in Online Appendix Ta-
ble A1, and they align with those in Table I, albeit with di!erent interpretation for the
strength coe"cient φ. We find that participants significantly overweight weak signals (φˆ> 1)
28Theregressor’sdenominatorlogitω logitω isincludedtomakeϱ herematchitstypicalinterpretation
1 0
↔
in a Grether (1980) regression. The typical Grether regression is logitωˆ =ϱlogitω +ς(logitω logitω ),
1 0 1 0
↔
or logitωˆ
1
logitω
0
= (ϱ 1)logitω
0
+ς(logitω
1
logitω
0
). Our regression sets ς = ς
0
+ς 1S(s) and
u lo s g e i s tω wˆ(s) l = ↔ ogit l l o o ω g g i i t t , ω ω ˆ1 1 w ↓ ↓ e l l o o g g o i i t t b ω ω t 0 0 ai ↔ n as e t q h u e at o i u on tco ( m 8) e , w va i r t i h ab ϱ le ↔ . ha S v o ing div th id e in s g am b e ot i h nt s e i r d p e r s et o a f ti t o h n e a G s re in the G r re e t q h u e a r t ’ i s on ca b se y .
1 0
↔
Intuitively, base-rate neglect matters more for the estimated weight the greater the distance of ω from 0.5
0
(the regressor’s numerator) relative to the signed signal strength (its denominator).
27

and underweight strong signals (φˆ< 1). We find that there is significant base-rate neglect
for strong signals but none for weak signals, indicating that the modest estimates for overall
base-rate neglect may partly reflect the inclusion of the weak-signal treatments.29
In the rightmost columns of Table II, we examine heterogeneity in our main treatment
e!ect by interacting signal strength with proxies for estimation precision (or imprecision),
controlling for base-rate neglect as in equation (8). Column (4) considers the same noise
proxy from Study 1a, finding again that people who have higher variance in weights exhibit
stronger e!ects. Column (5) considers how our e!ect correlates with task experience, again
finding that people exhibit a stronger e!ect earlier in the experiment.
We also elicit one additional measure to proxy for participants’ estimation precision,
based on the elicitation procedure used by Enke and Graeber (2023). In particular, we ask
people to answer “How certain are you that the optimal guess is somewhere between x 1%
↔
and x+1%?” on a scale from 0 to 100. We ask people this question three separate times
during the experiment, and average their answers to get an additional measure of a person’s
estimation precision: intuitively, a person with low precision will report higher subjective
uncertainty than a person with high precision (as shown by Enke and Graeber 2023, and
Enke, Graeber, and Oprea 2024). Column (6) suggests that this new proxy of cognitive
uncertainty is also associated with our e!ect in the direction predicted by the theory: people
with more stated uncertainty about their answer seem to exhibit our core e!ect more strongly.
Finally, we again estimate k and ϱ from equation (6). The estimated value for k is 0.89
(s.e. 0.02) and for ϱ is 0.61 (s.e. 0.02). The value of ϱ is statistically significantly less than one
(p-value < 0.001). These values correspond to an estimate for ς of 0.68 (s.e. 0.01). Allowing
↑
for base-rate neglect in the model gives an estimate of 0.94 for the weight on prior, and leads
to little change in the other estimates (k = 0.87 and ϱ = 0.69).
III.C. Study 2: Naturalistic Experiment
Overview. Thebenefitoftheabstractdata-generatingprocessinStudies1aand1bisthatitis
cleanly and fully defined. This constrained structure allows for straightforward manipulation
of signal strength and calculation of a precise Bayesian benchmark, which is a key reason
this paradigm is so widely used. But one possible concern is that this abstract, numerically
oriented environment is unnatural for most people, more closely mirroring a math exam than
a real-life updating situation. If people solve abstract inference problems di!erently than
29The table also presents a set of additional analyses. Column (1) considers only the ω =0.5 treatment,
0
finding our usual results. Column (2) replicates the analysis for all priors, imposing ϱ=1, and finds slightly
stronger results. Column (3) allows for separate ς across strengths but sets ϱ to be constant, with similar
resultsandmildbase-rateneglect. Column(4)presentsthefullsetofϱandς estimatesdescribedinthetext.
28

more naturalistic problems, our results might not generalize to real-life behavior.
Given this concern, our next experiment attempts to study updating behavior in a more
naturalistic environment. In particular, we analyze how NBA basketball fans update their
beliefs that a team wins a game given information that they make or miss a shot in di!erent
situations. This environment provides an experimental parallel to one of the observational-
data settings considered in Section IV. We choose to focus on it here because while the DGP
is naturalistic and complex, fans intuitively understand this process well and can easily make
reasonable predictions. A made basket is almost always a positive signal, and a missed basket
is a negative signal, but the exact strength of this signal is unclear.
This last feature also represents the main challenge in analyzing a naturalistic setting:
not having exact knowledge of the signal strength would seem to make it di"cult to test for
over- and underreaction. Crucially, however, this environment is one where we can obtain
credible estimates of the correct probabilities in di!erent situations using historical game data.
We do so using an online win-probability calculator from Inpredictable, a sports analytics
site that provides estimates for di!erent game situations.30 To provide participants signals
with varying strength, we vary the game situation. As detailed below, the key source of
signal-strength variation across scenarios is similar to the one we later use in our analysis
of sports betting data: the timing of the event. NBA basketball games have four quarters,
and a basket made in the fourth quarter is a stronger signal of the game’s winner than a
basket made in the first quarter. Our core prediction, therefore, is that people will overreact
to made or missed shots in early quarters (when signals are weaker), and underreact to made
or missed shots in late quarters (when signals are stronger).
Design. Participants are told that they will see a variety of simple scenarios in an NBA
game (which include the score di!erential, time remaining, and which team has possession)
between two unnamed teams (e.g., Team A and Team B), and that their goal is to estimate
the probability that each team wins the basketball game in that scenario. Participants are
sequentially given four sets of scenarios, with each scenario set starting with 2:40 left in one
of the four quarters and the time decreasing by 10-15 seconds after each event. The order of
the sets is random.
Within each scenario set, the person is first given a base scenario. They are then told the
actual calculated probability of the base scenario, such that all participants have the same
prior. To provide variation in priors within a quarter, we randomize whether the lead in the
30Our estimates are taken from https://stats.inpredictable.com/nba/wpCalc.php. This calculator
takes as input the current score di!erential, time remaining, and which team has possession, and outputs a
win probability based on historical data. To check whether this calculator gives reasonable estimates, we also
created our own simple calculator based on more, or fewer, years of data; the estimates from our versions of
thecalculatorandtheonlinecalculatorareextremelysimilar. Wetieourhandsbyusingthisthird-partytool.
29

Figure IV. Study 2: Example of an Information Page Participants See
base scenario is 1 or 5. Then, the participants are told the outcome of the next possession.
This signal is equally likely to be good news for the team on o!ense (a made 2-point basket)
or good news for the team on defense (a missed basket that leads to the defensive team
getting possession). They are then asked for the probability that a given team will win after
observing this event. We again elicit beliefs using the paired-uniform scoring version of the
binarized scoring rule (Vespa and Wilson 2017; Hossain and Okui 2013), with participants’
answers determining the probability that they win a high bonus rather than a low bonus.31
After the person enters their answers, they go through this process for 3 more consecutive
possessions in the same quarter. For each subsequent possession within this scenario set, they
see the sequence of previous events within the quarter, as well as the answers they entered.
After completing a scenario set, they move on to the next scenario set in a di!erent quarter,
where they are again told a base scenario and shown a series of signals. Figure IV shows
a screenshot with an example of the page participants see after the base scenario and one
event, and a full set of screenshots of the study pages are again in Online Appendix C.
We identify our core e!ect by exploiting variation in signal strength across these scenarios.
Interestingly, the empirical variation in signal strength in these scenarios is driven almost
31Our study instructions include the following: “We have used a model based on a database of regular-
season NBA games with several years of play-by-play data to estimate the likelihoods of each team winning
in these scenarios. The closer your answer is to the likelihood, the more likely you are to win the $50 bonus.”
30

entirely from variation in the amount of time left rather than the event or score di!erential.32
This motivates us to group our estimates by quarter when visually presenting our results
below, to see whether we indeed observe overreaction on average in response to the weak
signals in early quarters, and underreaction given the strong signals in late quarters.
Implementation. Study 3 was conducted in April 2024. Participants were recruited from
Prolific from a sample of Americans who reported that they were basketball fans. As
preregistered, 500 participants completed the experiment, passed an attention check, and
stated that they followed the NBA. Ten participants were randomly chosen to win bonuses.
If they won the high bonus, they received $50; if not, they received no bonus. All participants
received a $2.50 show-up fee and the average bonus earnings for the selected participants was
$25. Participants played 16 rounds in the study (4 possessions in a given quarter’s scenario
set, and 4 quarters).
Results. To study the relationship between participant’s perceived signal strength and the
true signal strength, we first back out a participant’s perceived signal strength from their
beliefs before and after an event as follows:
(10) logit(εˆ t+1 (s t+1 )) = logit(εˆ t ) S ˆ (s t+1 ) .
±
Logitof Logitof Signal Perceived
Guess Prior Direction SignalStrength
& ’( ) & ’( ) &’() & ’( )
For the base scenario (t = 0) in a given set, we set the prior εˆ to the calculator-estimated ε ,
0 0
as we give this win probability to the participant at the beginning of a set. We then provide
signals (events) s t+1 and elicit εˆ t+1 (s t+1 ) for each t = 0,1,2,3, backing out S ˆ (s t+1 ) from
εˆ (s )andtheirpreviousεˆ (whichtheystillseeonscreen); onebenefitofgivingasequence
t+1 t+1 t
of signals is our ability to observe the previous εˆ t in backing out S ˆ (s t+1 ). We back out true
signal strength S(s
t+1
) in a similar manner, but using the calculator’s estimated ε
t+1
(s
t+1
)
after each signal. Following the previous studies, we then compare S ˆ (s t+1 ) to S(s t+1 ).
We visually present our main results in Figure V, averaging perceived and true signal
strength across all events in each quarter. The left panel shows that as in the previous studies,
the relationship between perceived and true signal strength is approximately linear in logs,
with a positive intercept and a muted slope. The dots are ordered by quarter from left to
right: the first quarter has the lowest true signal strength, the fourth quarter has the highest,
32Fixingtimeandinitialscoredi!erence,ourevents(madeandmissed2-pointshots)havesimilarstrengths,
as NBA teams average close to 1 point per possession. Similarly, fixing time, baskets have surprisingly similar
strengths given di!erent initial score di!erences. Intuitively, while a basket shifts probability when tied more
than when up by 10 (say 50% to 60% vs. 90% to 93%), these have virtually the same signal strength S given
the di!erent base probabilities. Quantitatively, using past game data and regressing estimated strength on
time remaining yields an R2 of about 55%, and adding the score margin only improves this to 57%.
31

Figure V. Study 2: Over- and Underinference by Quarter
.6
Q4
.3
Q3
Q2
Q1
.15
.075
noitcaeR
tigoL
)htgnertS
deviecreP(
2
1.5
1
.5
.075 .15 .3 .6
True Signal Strength
langiS
no
thgieW
Data
Parametric
Bayesian
.1 .2 .3 .4 .5
True Signal Strength
Notes: Theleftpanelplotsthelogitbeliefchange(ourmeasureofperceivedstrength,asin(10))asafunctionoftruesignal
strengthonalog-logscale,wheretruesignalstrengthisbasedontheinpredictable.comwin-probabilitycalculator. The
rightpanelplotstheaverageweightparticipantsputonsignalsrelativetoaBayesianforwhomtheweightis1,alsoagainst
true signal strength (rather than precision, since signals are not necessarily symmetric). In both panels, black markers
plotthedata(with95%confidenceintervals),averagedbyquarter;signalstrengthsincreaseineachquarter. Observations
arewinsorizedforeachcategoryofquarterandscoredi"erentialatthe5%and95%level. Dashedlinesfitthedatausing
thepowerweightingfunctionfromequation(6),estimatingparametersusingnonlinearleastsquares. Thickersolidlines
indicateBayesianbehaviorbasedonthecalculator’saveragechange. Bothpanelsshowthatparticipantsoverweightweak
signals(inearlierquartersofthegame)andunderweightstrongsignals(inthefourthquarterofthegame).
and participants understand this ordering. But while average perceived signal strength does
rise over quarters, participants are insensitive to how much true signal strength is increasing,
such that they overreact early and underreact late (switching around the third quarter). This
can also be seen in the right panel, which plots the implied weights placed on events by
quarter. People weight first-quarter events by about 1.6 times as much as the win-probability
estimates suggest, and weight fourth-quarter events by less than 2/3 as much.
We then conduct regressions for the estimated signal weights as in the previous studies,
with results shown in the last two columns of Table I. As usual, we estimate these regressions
at the individual observation level, and thus do not group by quarter for this analysis. In
column (4), we regress wˆ(S) only on a constant and S, implicitly assuming that people
correctly incorporate their prior beliefs. We find the same qualitative patterns as in the
abstract experiments. Quantitatively, we see greater insensitivity to signal strength than in
the abstract studies, possibly because this is a more complex environment. In column (5), we
allow for misweighting prior beliefs, with estimation proceeding from equation (8). We find
modest base-rate neglect, but minimal change in our main coe"cients of interest.
We also run a Grether-style regression in Online Appendix Table A2, again following
equation (9) and now estimated separately for each quarter. We again find that participants
overinfer from events in the first half, underinfer from events in the second half, and exhibit
modest base-rate neglect overall. This modest base-rate neglect may be because the sequential
setting makes the prior belief more salient than in some other contexts, leading participants
32

to internalize their prior. But mimicking the results in Study 1b, the last column of that
table shows that priors are appropriately weighted for weak signals (in early quarters), but
that there is statistically significant base-rate neglect for stronger signals (in later quarters).
Finally, we estimate k and ϱ from equation (6), again using nonlinear least squares.
The estimated value for k is 0.40 (s.e. 0.02) and for ϱ is 0.41 (s.e. 0.02). The value of ϱ is
statistically significantly less than one (p-value < 0.001). Allowing for base-rate neglect in
the model gives an estimate of 0.976 (s.e. 0.06) for the weight on prior, and leads to little
change in the other estimates (k = 0.42 and ϱ = 0.44).
III.D. Discussion
Across our three experiments, we find robust evidence that people overinfer from weak signals
and underinfer from strong signals. Our findings hold in both abstract decision problems
(Studies 1a and 1b) and naturalistic ones (Study 2), as well as with fixed symmetric priors
(Study 1a), exogenously varied asymmetric priors (Study 1b), and endogenous priors based
on previous belief-updating questions (Study 2). While prior-weighting biases like base-rate
neglect can theoretically contaminate our predictions of overreaction and underreaction, in
our data they have little impact on our main estimated e!ect.
We find that these observed patterns of over- and underinference are consistent with people
understanding the direction they should update their beliefs, but only imperfectly estimating
the strength of the signals they receive. Our heterogeneity analyses provide suggestive
evidence of this as well: greater answer precision, subjective confidence, task experience,
and cognitive reflection are all correlated with greater sensitivity to signal strength and
belief-updating patterns that are closer to Bayes’ rule.
IV. Evidence from Finance and Sports Betting
Tobuildonourexperimentalevidenceandtestourtheoryinrelevantobservationalsettings,we
now consider evidence from a set of sports betting markets and financial markets. Departing
from the lab setting comes with multiple costs: (1) it is generally infeasible for us to estimate
the true conditional probability of an outcome or true signal informativeness, as we no longer
have knowledge of the true DGP (as we did in Studies 1a and 1b) nor the full information set
available to participants over time (as we did in Study 2); and (2) measuring subjective beliefs
and perceived signal informativeness is also less straightforward. To overcome these issues, we
apply new theoretical tools that allow us to proxy for signal informativeness and test updating
behavior, given a set of beliefs data. We then choose a set of markets from which to measure
price-implied beliefs: we consider the prices of di!erent bets (with payouts of either $0 or $1)
33

with known terminal dates. By considering price movements across informativeness regimes,
we test whether the patterns of over- and underinference documented in the experiments
apply in these real-world settings. We first describe our theoretical approach in more detail,
before turning to our empirical data and results.
IV.A. Conceptual Framework and Approach
Our conceptual framework for testing the behavior of beliefs builds closely on Augenblick and
Rabin (2021) (AR 2021) and Augenblick and Lazarus (2023) (AL 2023). Whereas Section II
provided a model of over- and underinference from signals, our goal here is di!erent: rather
than a full alternative model of inference, we aim to characterize the Bayesian null in a way
that allows for empirically implementable hypothesis tests. But while our starting point is
someone who updates according to Bayes’ rule, our tests are designed such that rejections are
consistent with over- or underinference and therefore speak to the patterns predicted from
Section II. We also build on that section’s notation where appropriate, generalizing it to a
dynamic setting with arbitrary signal structures.
Timeisdiscrete, t = 0,1,2,...,T, andthereisagainabinarystateω 0,1 . Eachperiod,
→{ }
a person observes a signal s from arbitrary distribution p(s ω,H ), where H s t
t t | t → 1 t ↑{ ϱ }ϱ=1
is the history of signal realizations. The person’s prior belief in state 1 is denoted by ε , and
0
their belief at time t given the DGP (i.e., their prior and p( )) and history H is ε (H ), or ε
t t t t
·
for short. The belief stream ω refers to the collection of the person’s beliefs over time.
While we cannot directly test for overinference vs. underinference without knowledge of
the DGP, keeping track of the following two objects will allow for well-motivated indirect
tests. First, define the movement of a belief stream from period t to t > t as the sum of
1 2 1
squared changes of beliefs over these periods:
m (ω) t2→ 1 (ε ε )2.
t1,t2
↑ ϱ=t1
ϱ+1
↔
ϱ
,
Then, defining the uncertainty of belief at period t as u (ω) (1 ε )ε , we define uncertainty
t t t
↑ ↔
reduction from period t to period t > t as:
1 2 1
r (ω)
t2→ 1
(u (ω) u (ω)) = u (ω) u (ω).
t1,t2
↑ ϱ=t1
ϱ
↔
ϱ+1 t1
↔
t2
,
For each variable, we define the concomitant random variable in capital letters (e.g., M ).
t1,t2
Our null model will be that the person fully understands the meaning of all signals and
updates according to Bayes’ rule. Under this null, beliefs satisfy ε t (H t ) = Et [ω] E[ω H t ]
↑ |
for all H t , where E is the expectation under the true (physical) measure.
34

The Equality of Movement and Uncertainty Reduction. As in AR (2021), the martingale
property of beliefs under the null implies that, regardless of the DGP, expected Bayesian
belief movement from any period t to period t must equal expected uncertainty reduction:
1 2
Proposition 2 (Movement and Uncertainty Reduction). Assume ε t (H t ) = Et [ω].
For any DGP and for any periods t 1 and t 2 , Et1 [M t1,t2 ] = Et1 [R t1,t2 ].
This result formalizes the “correct” amount of belief volatility (or movement) under rationality,
without the need to know the true unobservable DGP. (We provide a review of the proof in
Online Appendix A.5.) One can then follow AR (2021) to use this as the basis for a statistical
test for Bayesian updating: given a set of belief streams, one can calculate the di!erence
between movement and uncertainty reduction (which they call “excess movement”) and then
apply a means test to see if the average di!erence is statistically di!erent from zero. If so, one
can reject — with a certain confidence level — that the beliefs arose from Bayesian updating.
The result thus provides a testable link between belief movement, uncertainty reduction,
and signal strength: when we observe a Bayesian person’s beliefs moving, this must (on
average) mean that she is receiving informative signals and reducing her uncertainty accord-
ingly.33 Crucially, this test (1) is valid regardless of the DGP, and (2) can be applied to
arbitrary belief substreams (from period t to t ), as Proposition 2 applies ex ante in all
1 2
cases. Thus, given some ex ante known and observable sorting variable related to signal
strength, we can test whether excess movement is related to signal strength. We will use
time to resolution (T t) as our separating variable, and we discuss its relation to signal
↔
strength — and the relation of excess movement to over- and underinference — below.
Excess Movement and Over- and Underinference. We now consider what kinds of non-
Bayesian behavior generate di!erent violations of the equality in Proposition 2. Most
importantly for us, there is a natural positive connection between excess movement and
overinference: people who overinfer are intuitively changing their beliefs “too much” relative
to the informativeness of signals on average, generating Et1 [M t1,t2
↔
R t1,t2 ] > 0. The opposite
is true in the case of underinference.
AR (2021) formalize this connection. First, in a two-period environment, a person with a
correct prior who overinfers from signals will exhibit a positive excess movement statistic,
while a person who underinfers will exhibit a negative statistic. Second, they show that the
same relationship holds over many periods in a symmetric binary-signal environment, despite
33Formally, note from (2) that for any ω
t
, belief movement (ω
t+1
(S(s
t+1
)) ω
t
)2 is increasing in signal
↔
strength S(s t+1 ). So if we are in a regime with high signal strength ex ante, Et [M t,t+1 ] will be high, and by
Proposition 2, so will Et [R t,t+1 ]. We will verify that both of these increase with our informativeness proxy.
35

the complication that the person’s prior may not be correct in later periods.34 We suspect
that the same relationship between inference and excess movement applies quite generally,
but it is di"cult to characterize other DGPs analytically. We therefore turn to simulations to
verify that the same intuitive relationships hold under our updating model in environments
that more closely map to our empirical setting. We also use our simulations for further
verification that our time-based measure of signal strength is a good proxy in this setting.
As a caveat, we note that while overinference (underinference) generates positive (negative)
excess movement both analytically and in simulations, there could be other drivers of excess
movement that we cannot rule out in observational beliefs data: we only observe overall
reactions.35 But given that the patterns we observe in the data end up aligning closely with
the predictions of our model, we view the data as providing supporting evidence alongside
our experimental results (in which we can isolate inference behavior more directly).
Simulated Belief Streams. We now consider patterns in movement and uncertainty reduction
for a person who updates according to our model in Section II — as well as a person who
exhibits constant over- or underinference — when forming beliefs about the outcome of a
sporting event or the future level of the stock market in simulated data. Empirically, these
settings feature similar random-walk-like DGPs with signals (points scored, daily returns)
received in each period, with the aggregate of that information determining the final state.
To transparently model such situations in our simulated economy, we consider a simple
random-walk-like DGP in which there are two “teams” representing the two states, exactly
one team scores in each of T periods, each team has equal probability of scoring in each
period, and the final state is which team has the highest score after the final period. For
example, if a team is leading by one score with two periods left, they have a 75% chance of
being the final winner because they win if they score in one of the final two periods.
We conduct one million simulations of this DGP, and we present average results by
time period in Figure VI. The top-left panel shows the expected movement and uncertainty
reduction statistics over time for a Bayesian. First, following Proposition 2, the statistics
must be equal at each period. Next, note that both statistics are rising as the resolution of
34Specifically, the paper considers a specification of over- or underinference equivalent to eq. (9), in which
logit(ωˆ
t+1
)=logit(ωˆ
t
) ςS(s
t+1
). Their Proposition 6 states that a person with ωˆ
t
=ω
t
and ς> 1 will have
±
E[M
t,t+1
]>E[R
t,t+1
] (and the opposite if ς< 1). Proposition 7 states that, given a DGP with a constant
signal strength and ω
0
= 1/2, a person with ωˆ
0
= 1/2 and ς> 1 will have E[M
t1,t2
] > E[R
t1,t2
] given any
history H (and the opposite if ς< 1). One quarter of a basketball game very roughly approximates such a
t0
binary symmetric environment, to take an example (see footnote 32).
35Base-rate neglect, for example, tends to generate positive excess movement (AR 2021). Another bias,
probability weighting, e!ectively matches the results from constant underinference. In fact, given a prior of
50%, the classic symmetric functional form for probability weighting from Gonzalez and Wu (1999) is exactly
equivalent to a person who constantly underinfers from all signals.
36

Figure VI. Simulated Movement and Uncertainty Reduction Over Time: Di!erent Models
.025
.02
.015
.01
.005
doireP
ni
egarevA
Bayesian
.025
Belief Movement
Uncertainty Reduction
.02
.015
.01
.005
0 4 8 12 16 20 24
Time Period
doireP
ni
egarevA
Constant Overinference
0 4 8 12 16 20 24
Time Period
.025
.02
.015
.01
.005
doireP
ni
egarevA
Constant Underinference
.025
.02
.015
.01
.005
0 4 8 12 16 20 24
Time Period
doireP
ni
egarevA
Our Model
0 4 8 12 16 20 24
Time Period
Notes: Thisfigureshowstheaveragebeliefmovement(thickerblackline)anduncertaintyreduction(thinnerlightline)
statisticsovertimeforfourdi"erentmodels,averagedover1millionsimulationsofthegame-likeDGPdiscussedinthe
textwithT =27. Wedropthefirstandlastperiod,astheyalwayshavezeroexcessmovementgiventhisDGP,andplot
theremaining24periods. Theupdatingmodelsare(1)Bayesianupdating(correctperceptionofsignalstrengthS),(2)
underinference(withperceivedsignalstrength0.8 S),(3)overinference(withperceivedsignalstrength1.2 S),and(4)our
model(perceivedsignalstrengthk Sω withk= · 0.88andω=0.76). ForBayesianupdating,thesestatis · ticsarealways
·
equal. Forunderinference,movementisalwayslessthanuncertaintyreduction,andtheoppositeistrueforoverinference.
Forourmodel,movementisgreaterthanuncertaintyreductioninearlytimeperiods(whensignalsaregenerallyweak)and
lowerinlatertimeperiodsclosetoresolution(whensignalsaregenerallystrong).
the game approaches. Initial periods always contain very little information, while the later
periods sometimes convey no information (because one team has an insurmountable lead)
and sometimes convey strong information (because the scores are close). Overall, though,
signal strength rises over time, and average movement and uncertainty reduction increase
accordingly. This is intuitive theoretically.36 And as we show shortly, it also applies in all of
our empirical settings; importantly, we consider settings where all uncertainty will be resolved
36Forexample, foroptionprices, theBlack–Scholesmodelpredictsthatthesensitivityofanoptionpriceto
the same change in the underlying price (i.e., option delta) decreases exponentiallywith time tomaturity, and
the same applies (in fact more strongly) for the option spreads used to construct option-implied beliefs. That
is, the same underlying price change rationally generates a bigger change in beliefs about the option payo!
closer to maturity. Our simulated random walk is in fact a discrete-time approximation of a Black-Scholes
economy, but the same logic will hold in practically any option-pricing model beyond this one.
37

by some fixed end period, and as a result strength increases closer to that expiration.
What do the statistics look like for people who over- or underinfer from signals? Following
intuitionandthetheoreticalresultsfromsimplerDGPs,overinference(top-rightpanel)leadsto
positiveexcessmovementineveryperiod,whiletheoppositeistrueforunderinference(bottom-
left panel). The bottom-right panel displays the results for our model, with parameters
estimated from our Study 1a. In the early periods, average signal strength is low, leading
to overinference, which in turn generates excess movement. In later periods, the amount of
information revealed is higher, leading to underinference. Belief movement increases, but
not in line with the increase in uncertainty reduction. There is therefore a switching period
at which average movement crosses below uncertainty reduction. This switching is in e!ect
the signature pattern for our model, as it does not occur under Bayesian updating or when
there is universal overinference or underinference. We now proceed to test whether the same
patterns hold empirically.
IV.B. Sports Betting Data
Data Description. We start with data on sports betting. Our data comes from Betfair, which
operates a large prediction market in which individuals are matched on an exchange to make
opposing financial bets about the outcome of a sporting event. We observe time-stamped
transaction prices for a contract in which one party pays another party a set amount given
a particular realized outcome of the game (e.g., Team A beats Team B). Prices are quoted
as fractional odds; for example, a transaction for the Team A contract might occur at 3/1
odds, meaning the person buying one unit of it will receive $4 if Team A wins and lose $1
if Team A loses. These odds can then be normalized to obtain an implied probability (in
this case, 1/4). As in a standard centralized exchange, contract prices (and implied beliefs)
change with supply and demand.
These are the same data as used in AR (2021), and we use the same 2006–2014 sample
and similar data filters as in that paper. In particular, we focus on markets for five major
sports — soccer, basketball, baseball, ice hockey, and American football — and we consider
only contracts over the final winner of the game. We thus omit more exotic contracts, such as
which team will be winning at the midpoint or number of goals scored. There are generally
two contracts per game (e.g., one paying o! if Team A wins, another if Team B wins); we use
the contract for which the starting beliefs are closest to 0.5. We use observations only when
the game is being played. To remove high-frequency noise, we follow AR (2021) and keep
only the first transaction in a given minute increment. We also drop trades with less than
1% of the overall average transacted amount. Finally, we attempt to have similar timing in
events by dropping less-common events in a category for which the timing of the game is
38

di!erent (such as WNBA games, which are shorter than NBA games). We are left with over
5 million transaction prices from about 260,000 sporting events over the sample.
Given our focus in this section on equilibrium bet-price data, we follow the literature
that interprets these prices as “market beliefs.”37 A test based on Proposition 2 can thus be
viewed as a test of the joint null that market prices may be interpreted as beliefs and that
these beliefs are Bayesian. But while this might a!ect the interpretation of full-sample excess
movement tests, it poses less of a problem for our purposes. We are fixing the environment
(i.e., the particular betting market in question) and comparing excess movement as one varies
the signal strength (proxied by time to maturity) within this environment. If we assume that
the mapping from individual to market beliefs does not change systematically within a stream
as one moves closer to maturity, our findings are at minimum directionally informative about
both individual and market-level reactions to information across signal-strength regimes.
Graphs of Movement and Uncertainty Reduction. Figure VII shows average movement and
uncertainty reduction (as well as confidence intervals) across time for each sport. Observations
occur in continuous time and therefore must be aggregated in some way. Our data contain
observations in clock time (“1:31pm”) rather than game time (“4:50 through the third
quarter”); we therefore consider average movement and uncertainty reduction for observations
within 24 time windows, each of which corresponds to 1/24 the length of an average game.38
As in the simulations, average movement and uncertainty reduction are generally increasing
over time (with the exception of mid-period breaks). As discussed in Section III.C, signals in
basketball games increase in strength strongly over time; the increase in both movement and
uncertainty reduction over time shows that the same pattern applies for all sports.39
The relative patterns of the two series, though, follow the predictions of our model of over-
and underinference. Early in games for each sport, movement is greater than uncertainty
reduction, and for each sport there is a time at which movement drops below uncertainty
reduction. For four of the five sports, movement then continues to be lower than uncertainty
reduction after this time (for hockey, movement stays lower than uncertainty until the final
period). The market accordingly appears to overreact to the less-informative signals at the
37The interpretation of market prices as averages of individual beliefs has been studied in a range of work.
In standard Bayesian settings with complete markets, this interpretation is straightforward (see AL 2023).
With heterogeneity, Gjerstad (2005) and Wolfers and Zitzewitz (2006) show the interpretation is valid when
traders have log utility and trade statically (cf. Manski 2006). But with speculative trading, prices often
react more to new information than individual beliefs (Martin and Papadimitriou 2022).
38For example, as the average basketball game lasts around 132 minutes, basketball games are broken
into 24 chunks of 5.5 minutes. The final chunk then includes all observations that occur after 132 minutes.
Results are similar if we use di!erent numbers of chunks. Separately, in constructing confidence intervals for
this figure (but not for the regressions), we assume observations are uncorrelated across contracts.
39This follows unless markets completely misunderstand directional changes in signal strength (thinking
stronger signals are weaker), seemingly counter to all available evidence (e.g., Croxson and Reade 2013).
39

Figure VII. Movement and Uncertainty Reduction Over Time for Sports Betting Data
.02
.015
.01
.005
0
wodniW
ni
egarevA
Soccer
.03
Belief Movement
Uncertainty Reduction
.02
.01
0
0 8 16 24 32 40 48 56 64 72 80 88 96
Game Minute
wodniW
ni
egarevA
Basketball
0 10 20 30 40 50 60 70 80 90 100 110 120
Game Minute
.06
.04
.02
0
wodniW
ni
egarevA
Baseball
.08
.06
.04
.02
0
0 16 32 48 64 80 96 112 128 144 160 176 192
Game Minute
wodniW
ni
egarevA
Ice Hockey
0 12 24 36 48 60 72 84 96 108 120 132 144
Game Minute
.04
.03
.02
.01
0
wodniW
ni
egarevA
American Football
0 16 32 48 64 80 96 112 128 144 160 176 192
Game Minute
Notes: This figure shows average belief movement (thicker black line) and uncertainty reduction (thinner light line)
statisticsovertimeforthebeliefsimpliedbybettingpricesforfivedi"erentsports(with95%confidenceintervals). Minute0
isthebeginningofthegame,andthelastminuteistheendofthegame. Eachestimatedpointisthesummedmovementor
uncertaintyreductionwithinoneof24equal-lengthtimewindows,averagedoverallthegamesinthesample. Ineachcase,
movementisgreaterthanuncertaintyreductioninearlytimeperiods(whensignalsaregenerallyweak),anditislower
thanuncertaintyreductionclosetotheendofthegame(whensignalsaregenerallystrong),aspredictedbythemodel.
beginning of a game, and underreact to the more-informative signals at the end of a game.
Interestingly, for basketball (in the top-right panel), excess movement switches from positive
to negative around the end of the third quarter, precisely mirroring the switch from over- to
underinference observed in our experimental basketball setting in Study 2 (see Figure V).
40

Statistical Tests. Are the patterns in the figures statistically meaningful? To answer this
question, we require a test to determine if there is overreaction (captured by expected
movement being greater than uncertainty reduction) when signals are weak (captured by low
uncertainty reduction), and underreaction when signals are strong. But we cannot simply
sort observations by realized uncertainty reduction (or some ex post proxy for signal strength)
and then test how excess movement changes across this sort. Instead, Proposition 2 tells
us that we must test whether expected movement Et [M t,t+1 ] equals expected uncertainty
reduction Et [M t,t+1 ] ex ante. We must therefore consider an ex ante sort variable, and analyze
the relationship between average movement and uncertainty reduction across settings with
di!erent strength.
As we have seen, time to resolution is a strong such ex ante variable separating low
(early) from high (late) signal-strength periods. We therefore, for each sport, regress average
movement in each time window on average uncertainty reduction in the same time window.
Under the null of Bayesian updating, the constant will be equal to 0 and the slope coe"cient
equal to 1, as average movement should be equal to average uncertainty reduction in every
period. However, for a person who updates according to our model, average movement
will be higher than average uncertainty reduction when reduction is low, but lower than
uncertainty reduction when reduction is high, such that the constant will be positive and the
slope coe"cient will be less than one.
The results for these regressions are shown in the first five columns of Table III. Each
regression is run on 24 collapsed observations, where each observation contains the average
movement and uncertainty reduction in a given time window. The use of these calculated
averages introduces a generated-regressor issue for inference, so we bootstrap standard errors
by resampling events (games) with replacement and recalculating averages and regression
coe"cients10,000times.40 Foreachsportinthefirstfivecolumnsinthetable,theconstantand
slope coe"cients are highly statistically significantly di!erent from the Bayesian benchmark
in the direction predicted by the theory: in all cases, the positive constant and slope below
one are consistent with overinference from weak signals (when average uncertainty reduction
is low) and underinference from strong signals (when uncertainty reduction is high).
To understand the magnitude of the estimates, note that beliefs moving 3 percentage
points up and then 3 points down would produce movement of 0.0018 (close to the average
constant coe"cient) and no uncertainty reduction. Given this average constant, the average
slope coe"cient then implies that movement will cross uncertainty reduction when both are
around 0.014, which occurs before the end of the game for all the sports in Figure VII.
A potential concern when testing for a one-to-one slope is measurement error in the
40OLS standard errors are very similar.
41

Table III. Regressions of Average Movement on Average Uncertainty Reduction
Sports Finance
Dep. Var.:
Movement Soccer Basketball Baseball Hockey Football Raw Risk-Adj.
Constant 0.0009 0.0018 0.0026 0.0018 0.0015 0.0065 0.0060
(0.0001) (0.0001) (0.0002) (0.0002) (0.0002) (0.0003) (0.0003)
Uncert. Red. 0.918 0.806 0.889 0.945 0.912 0.680 0.733
(0.005) (0.008) (0.013) (0.013) (0.027) (0.040) (0.041)
R2 0.977 0.985 0.995 0.976 0.995 0.944 0.941
Time Chunks 24 24 24 24 24 24 24
Events 175,026 48,430 16,536 19,445 3,212 955 955
Belief Obs. 4,589,289 867,567 166,346 109,751 86,193 58,864 58,864
p-val: Const = 0 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001
p-val: Slope = 1 <0.001 <0.001 <0.001 <0.001 0.007 <0.001 <0.001
Notes: ThistablepresentstheresultsfromOLSregressionsofaveragemovementineachofthe24timeperiodsonaverage
uncertaintyreductioninthattimeperiod,forfivesportsandtheoptionsdata(bothrawandrisk-adjusted,asdescribedinthe
text). Bootstrappedstandarderrors,inparentheses,arecalculatedbyresamplingeventswithreplacementandrecalculating
averagesandregressions10,000times. Bayesianupdatingpredictsconstant=0andslope=1,whileourtheorypredictsconstant
>0(correspondingtooverinferenceforveryweaksignals)andslope<1(relativelymoreunderinferenceforstrongersignals).
regressor and resulting attenuation bias. This would be a meaningful concern if, instead of
following Proposition 2, we regressed period-by-period realized m on r .41 But because
t,t+1 t,t+1
we take averages over thousands of belief changes at a given time horizon, we are able to
estimate expected uncertainty reduction at that time plus a tiny error term. In our case,
the estimated variance of the error term at each period is more than 100,000 times smaller
than the estimated variance of the regressor, so any resulting attenuation bias is negligible.42
Note that the R2 values in all cases are very close to 1: average movement and uncertainty
reduction move very closely together, but with a muted slope.
IV.C. Index Options Data
Data Description. The sports betting data provide a useful lab for studying beliefs in an
incentivized setting similar to the one in Study 1b of our experiment. We now consider
whether similar patterns apply to a large-scale financial market, where beliefs are expressed
over outcomes of first-order macro importance. In particular, we consider options on the S&P
41For a Bayesian, Et [M t,t+1 ]=Et [R t,t+1 ], but r t,t+1 is equal to that expectation plus a mean-zero error.
42By averaging the movement and uncertainty reduction statistics over time chunks, we do face the subjec-
tive question of how many chunks to use. We show in Online Appendix Tables A3–A4 (with accompanying
figures) that estimated slopes change slightly (di!erently across sports) when using 12 or 36 chunks, but
p-values remain highly significant in all cases aside from hockey with 12 chunks and football with 36.
42

500 index, which are e!ectively bets on the value of the market index as of a fixed future
expiration date.43 We use the OptionMetrics database to obtain option price quotes for S&P
index options traded on the Chicago Board Options Exchange (CBOE), which is the largest
U.S. exchange. We observe the best posted bid and ask quotes at the end of every day for
each strike price and expiration date, and we take the average of these two and use this as
our end-of-day price.
These are the same data as used in AL (2023), and we use the same sample (1996–2018)
and similar filters as in that paper. As our list of filters is somewhat long, we relegate
details to Online Appendix B.2. After filters, we are left with over 4 million option prices
corresponding to about 955 option expiration dates (the analogue of a single event in the
betting data) and 5,500 trading dates. To ensure that prices are liquid, AL (2023) consider
options expiring at most one year away from the trading date. For our purposes, we cut o!
the analysis at 100 trading days from expiration (in calendar time, roughly 4.5 months). This
somewhat arbitrary choice is largely so that our movement and uncertainty reduction figures
are easily readable, and our results continue to hold when using longer-horizon options.
Converting Option Prices to Market-Implied Beliefs. On any given trading date t, there
are prices for a range of S&P options with the same expiration date T. They di!er only in
their strike prices K (for a call option, the minimum S&P index value at which the option
will obtain a positive payo! at expiration). Using minimal assumptions (following Breeden
and Litzenberger 1978), the set of option prices for such a (t,T) pair can be translated
into a market-implied (or risk-neutral) probability distribution over the future S&P price
on the option expiration date. Intuitively, by buying a set of options, one can construct
a strategy that pays o! $1 if, say, the S&P is between 5,500 and 6,000 on September 30,
and $0 otherwise. The market price of constructing such a binary bet can be read as an
option-implied probability that the S&P will indeed be in this range.
Unlike in the case of sports betting data, index options have payo!s that are tied (by
construction) to the value of aggregate wealth. Option prices therefore reflect risk aversion
in addition to subjective probability assessments about the future index value. This is the
main complication in using option-implied probability distributions: they do not, in general,
correspond to any notion of aggregate subjective beliefs. (They are equivalent to subjective
beliefs only in the case of risk neutrality over the index value, which motivates referring
to them as risk-neutral beliefs.) For example, suppose that there are two possible date-T
43An option contract specifies an expiration date T and strike price K, which together with the realized
value of the S&P (V ) determine the payo! to the buyer of the contract. If V >K, then the holder of a
T T
call option receives $V K; otherwise they receive $0. They pay c for the option upfront, and the seller
T t
↔
receives the negative of the buyer’s payo!. (For a put option, the holder instead receives max(K V ,0).)
T
↔
43

macroeconomic states that are perceived by investors as equally likely. If investors value a
marginal dollar in the “bad” state (when the market is low) more than in the “good” state
(when the market is high), they will be willing to pay more for the option that pays o! in
that state. If these risk preferences are not taken into account, one will (falsely) conclude
that investors believe that the bad state is more likely.
Addressing this issue is the main theoretical task taken up in AL (2023). That paper shows
that under certain assumptions, one can place a bound on excess movement in risk-neutral
(RN) beliefs under the null that underlying subjective beliefs are rational. The bound is
tight in the space of possible DGPs — that is, one can construct a DGP under which it
holds exactly — but it is not necessarily tight under the true real-world DGP.44 We therefore
provide two sets of results in the current analysis, (1) using the raw (unadjusted) RN beliefs,
and alternatively (2) translating these beliefs to a set of physical (subjective, risk-adjusted)
beliefs under an assumption on risk aversion. For (2), we consider many possible assumptions
in translating from risk-neutral to physical beliefs, detailed in Online Appendix B.2. While the
dozens of possible assumptions and parameterizations a!ect the physical belief estimated for a
given risk-neutral belief, it turns out their e!ect on our movement and uncertainty-reduction
statistics is so small as to be nearly indetectable.45 We thus report results here under our
main translation, which assumes a representative investor with power utility over the terminal
index value. We present estimates under a wide range of alternative parameterizations in
Online Appendix Figure A9, which shows that these choices have little e!ect on our results.
To implement our measurement of RN beliefs empirically, we need a set of discrete possible
outcomes as of date T. In particular, we must partition the set of possible date-T index
values into discrete ranges (in the example above, the single range considered was from
5,500 to 6,000). To maintain the same set of possible outcomes across di!erent expiration
dates, we set these states to correspond to ranges for the log excess return on the S&P 500
from the first observable option trading date to the expiration date. In particular, we define
10 potential return outcomes ω , each of which (aside from the two tails) corresponds to a
j
five-percentage-point range for the S&P’s log return in excess of the risk-free rate: state ω
1
is realized if the S&P’s log excess return is below -0.2 (i.e., roughly -20%) from date 0 to
date T; state ω is realized if the log excess return is in the range ( 0.2, 0.15] (between
2
↔ ↔
-20% and -15%); ω if ( 0.15, 0.10]; and so on, up to ω = (0.15,0.2] and ω above 0.2.
3 9 10
↔ ↔
We then use options to measure RN beliefs ε for each state j over trading days
t↑,j
44While the bound is su"cient for the full-stream tests considered in that paper, it might not be here: we
wish to understand how “true” excess movement evolves with signal informativeness within a stream.
45The brief intuition is that risk aversion is unlikely to be changing meaningfully from day to day. But the
main point of interest for this analysis is that the basic patterns found in the experimental data and in the
sports betting data are also observed in the finance data, regardless of the RN beliefs correction used.
44

t = 0,1,...,99.46 For example, ε is the option-implied belief, as of t, that the S&P’s excess
t↑,3
return from 0 to T will end up being between -15% and -10%. At T = 100, we assign
probability 1 to the actual realized return state. Note that unlike for the sports betting
data, we no longer have only two possible states. Instead, we are using the full histogram of
beliefs over 10 possible return outcomes. This departs from AL (2023), where the histogram
is converted into a set of binarized conditional beliefs. We keep the full histogram here in
order to minimize the potential e!ects of noisy prices, which AL (2023) show can induce
meaningful measurement error in the binarized statistics.47
So for each trading day and expiration date, we calculate the belief movement and
uncertainty reduction statistics for each state’s risk-neutral belief (m and r ),
t,t+1,j,T t,t+1,j,T
and we then average the resulting statistics across all 10 states (m = 1 10 m ,
t,t+1,T 10 j=1 t,t+1,T
and similarly for r
t,t+1,T
). Given that each belief has an interpretation as a-binary belief
over whether the given state will be realized or not, Proposition 2 still applies to these
aggregated statistics (see AR 2021, Proposition 3). Finally, as before, after calculating these
values, we then break the data into 24 equal-length time windows sorted by trading days to
expiration. Within each such chunk (for trading days t through t ), we calculate average
1 2
overall movement and uncertainty reduction over all events T (e.g., 1 955 m ) as our
955 T=1 t1,t2,T
empirical measures of E[M t1,t2 ] and E[R t1,t2 ]. -
Graphs of Movement and Uncertainty Reduction. Figure VIII shows average movement and
uncertainty reduction over time in the options data, analogous to Figure VII. Date 0 is again
100 trading days from expiration, while date 100 is expiration. The left panel shows the
average movement and uncertainty reduction statistics for the raw risk-neutral beliefs, and the
right panel shows the statistics for physical beliefs obtained under the main risk adjustment
procedure. In both cases, movement is consistently above uncertainty reduction relatively far
from expiration, when signals are only very weakly informative and uncertainty reduction
is statistically indistinguishable from zero. Uncertainty reduction increases dramatically
closer to expiration (when market movements are more informative regarding the true index
value at the expiration date). And while option-implied belief movement increases alongside
uncertainty reduction, it appears to do so less than one for one, with uncertainty reduction
46Full details on how we construct the risk-neutral belief distribution are again provided in Online
Appendix B.2. Given ω , we then also calculate the corresponding risk-adjusted physical belief ω using
t↑,j t,j
the power-utility risk adjustment described above, and all the calculations for movement and uncertainty
reduction are then duplicated for these adjusted beliefs.
47They also provide and estimate a correction for this error on the binarized statistics (which are used in
thatpapergiventheirtheoreticalsetting). WeshowinOnlineAppendixFigureA10thattheirnoise-corrected,
binarized RN beliefs exhibit very similar patterns in movement and uncertainty reduction as in our histogram
data. The Online Appendix also includes figures and tables showing that results are unchanged with di!erent
numbers of time windows, as well as in subsamples of the option data (post-2000 and post-2010).
45

Figure VIII. Movement and Uncertainty Reduction Over Time for Finance Data
.04
.03
.02
.01
0
wodniW
ni
egarevA
S&P Options: Unadjusted
Belief Movement .04
Uncertainty Reduction
.03
.02
.01
0
0 10 20 30 40 50 60 70 80 90 100
Trading Day
wodniW
ni
egarevA
S&P Options: Risk-Adjusted
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: Thisfigureshowstheaveragebeliefmovement(thickerblackline)anduncertaintyreduction(thinnerlightline)
statisticsovertimeforthebeliefsimpliedbyoptiondata(with95%confidenceintervals). Tradingday0correspondsto100
daysfromexpiration,andthelasttradingdayistheexpirationdate. Eachestimatedpointisthesummedmovementor
uncertaintyreductionwithina4-trading-daywindow,averagedoveralloption-expirationdatesinthesample(1996–2018).
Theleftpanelusestheunadjusted(risk-neutral)beliefsimpliedbyoptions. Therightpanelusesariskadjustmentdescribed
inthetext. Movementisgreaterthanuncertaintyreductionfarfromexpiration(whensignalsaregenerallyweak),anditis
lowerthanuncertaintyreductionclosetoexpiration(whensignalsaregenerallystrong),aspredictedbythemodel.
crossing above movement roughly 10 days from expiration.
The patterns observed in this high-stakes financial market are similar to those in the sports
betting data for many sports plotted in Figure VII. They are also similar to the simulated
results from our theoretical framework plotted in the bottom-right panel of Figure VI. Recall
that these simulations are parameterized using the estimates from our experimental data, so
the theory accordingly helps unify the evidence obtained in both the lab and real-world data.
Statistical Tests. We conclude this analysis by conducting the same formal tests as in the
previous case, regressing average movement on average uncertainty reduction in each time
window. The results are shown in the final two columns of Table III. For both the raw and
risk-adjusted data, the estimated slope and constant are again highly statistically significantly
di!erent from the Bayesian benchmark in the direction predicted by our theory. The positive
constant again indicates overreaction when signal informativeness (uncertainty reduction)
is low, as movement is significantly positive in these cases; meanwhile, the slope being less
than one (and numerically nearly identical to the estimated slope in the sports betting data)
indicates underreaction for high enough levels of signal informativeness. The market therefore
appears to over- and underreact in the way predicted for individuals modeled in Section II.
More broadly, the consistent results from the lab and from observational data indicate a key
determinant for this updating behavior that applies across settings.
46

V. Discussion and Conclusion
We provide evidence that people overinfer from weak signals and underinfer from strong
signals. We demonstrate this phenomenon using three tightly controlled experiments and
using a new empirical method applied to betting and financial markets. In each setting,
beliefs appear to move in the correct direction and shift more when signals are stronger. But
perceptions of signal strengths appear consistently anchored toward some intermediate level;
in other words, people act as if they are partially insensitive to the objective signal strength,
leading on average to overinference from weak signals, underinference from strong signals,
and corresponding over- and underreaction in beliefs. This partial insensitivity to signal
strength is well captured by a model in which a person understands the directional meaning
of a signal but is less certain about the strength of the information. These findings help unify
seemingly contradictory results in past literature and data on inference behavior.
Naturally,weviewthisasoneofmanypossiblereasonswhypeoplemayreacttoinformation
in a non-Bayesian manner. Our theory directly applies when a person pays attention to a
discrete signal, easily determines its directional meaning, has a reasonable but imperfect
estimate of its strength, and partially corrects for this imperfection. We take these conditions
as given, but it would be fruitful to unpack them, and to study when they do or do not
hold. For instance, if attention is endogenous to signal strength in certain situations, people
may not attend to (and therefore underinfer from) some weak signals. Similarly, people
may estimate strength in a systematically biased way, such that they overinfer from some
strong signals. The limited-attention version of our model in Section II.D — in which people
focus on a subset of entries in the signal-strength vector — provides one possible framework
for exploring these issues. Finally, for some predictions, people may be naive about the
imperfection in their estimate. Consequently, we see modeling the di!erent stages of the
estimation process — including how people form simple models of situations, attend to and
process information through these models, and correct for estimation errors — in more detail,
and understanding how these change across decision environments, as important next steps.
We see several additional paths for potential future research. First, although we find
similar main results in our abstract experiments and our more naturalistic experiment,
it is worth understanding better whether participants facing math-test-like experimental
environmentsusedi!erentdecision-makingprocessesandheuristicsthantheydoinnaturalistic
environments. Using abstract environments has huge benefits — better control and mapping
to abstract models — but may come at the cost of only observing a very particular class of
behaviors. For example, our theory and results suggest that estimates of base-rate neglect
might depend on whether the experiment uses abstract “endowed” priors versus a naturalistic
47

“internalized” prior; telling people that their prior should be 80% may generate di!erent
findings than a person genuinely believing 80% from previous experience and updating.
Relatedly, our work suggests that some standard results (like underinference, in our case) may
be limited to classic parameters (like strong signals) used in past experiments, an insight also
observed recently in work by Blavatskyy, Panchenko, and Ortmann (2023) and McGranaghan
et al. (2024). While there are benefits in using experimental designs and parameter values
known to “work,” these choices may again limit external validity.
Second, our results suggest future directions to study the demand for news in the real
world. There has been a shift in news provision and consumption away from traditional
news outlets and toward other platforms (Liedke and Gottfried 2022), despite concerns about
platforms’ low-quality news and misinformation (Allcott and Gentzkow 2017). One potential
explanation is that people respond to news in general, but are insu"ciently sensitive to the
quality of the information source. In our abstract environment in Study 1a, we in fact find
some suggestive evidence for this: we ask people to decide how many signals to purchase
(related to Ambuehl and Li 2018), and find that people purchase too many weak signals and
too few strong signals relative to the instrumental value of the information (Online Appendix
Figure A4). It would be valuable to empirically understand whether these e!ects generalize
outside the lab in a way that might help explain the prevalence of lower-quality news sources.
Finally, while our results speak most directly to inference behavior, we see natural
connections to the behavior of forecasts — stated expectations, rather than beliefs — at
di!erent horizons. Afrouzi et al. (2023) and Fan, Liang, and Peng (2024) find evidence
for overreaction to news in a set of experimental forecasting tasks, as well as a selection
of survey data. But there is consistent evidence in recent work that such overreaction
decreases strongly with the persistence of the given series in a range of settings, in many
cases switching to underreaction as a series approaches unit-root persistence.48 A model in
which the conditional mean (rather than ε ) is the object of interest may help speak to these
t
patterns: if forecasters understand a shock’s directional impact on the future conditional
mean but do not perfectly understand how much it should change, then stronger signals
will take the form of more-persistent shocks, potentially generating the observed patterns
of over- and underreaction.49 Given the importance of forecast behavior for macroeconomic
48Among others, Reimers and Harvey (2011) and Afrouzi et al. (2023) provide evidence in the lab, and
Bordalo et al. (2020) provide evidence in survey data. Using both options and stock-return surveys, Gandhi,
Gormsen, and Lazarus (2023) show evidence for overreaction in forecasts of the future equity premium,
which is a moderately persistent series. For the Treasury yield curve, Wang (2021) and Farmer, Nakamura,
and Steinsson (2024) show evidence for e!ective underreaction (e.g., positive coe"cients in regressions of
survey-basedforecasterrorsonforecastrevisions)fortheshort-horizoninterestrate,whichisaverypersistent
serieswithanannualizedautocorrelationofabove0.9. Gabaix(2019)providesareviewandfurtherdiscussion.
49In a simple setting with two possible values for the conditional mean at a given future date, our results
48

and financial-market contexts outside of the ones we consider here, it would be useful to
explore this connection both theoretically and empirically. We leave these, and other potential
applications of our findings, for future work.
University of California, Berkeley, United States
University of California, Berkeley, United States
University College London, United Kingdom
References
Afrouzi, Hassan, Spencer Y. Kwon, Augustin Landier, Yueran Ma, and David Thesmar (2023),
“Overreaction in Expectations: Evidence and Theory,” Quarterly Journal of Economics 138,
1713–1764.
Allcott, Hunt and Matthew Gentzkow (2017), “Social Media and Fake News in the 2016 Election,”
Journal of Economic Perspectives 31, 211–236.
Ambuehl, Sandro and Shengwu Li (2018), “Belief updating and the demand for information,” Games
and Economic Behavior 109, 21–39.
Athey, Susan (2002), “Monotone Comparative Statics under Uncertainty,” Quarterly Journal of
Economics 117, 187–223.
Augenblick, Ned and Eben Lazarus (2023), “A New Test of Excess Movement in Asset Prices,”
Working Paper.
Augenblick, Ned, Eben Lazarus, and Michael Thaler (2023), “Overinference from Weak Signals and
Underinference from Strong Signals,” arXiv Working Paper 2109.09871v4, https://arxiv.org/
pdf/2109.09871v4.
Augenblick,NedandMatthewRabin(2021),“BeliefMovement,UncertaintyReduction,andRational
Updating,” Quarterly Journal of Economics 136, 933–985.
Azrieli, Yaron, Christopher P. Chambers, and Paul J. Healy (2018), “Incentives in Experiments: A
Theoretical Analysis,” Journal of Political Economy 126, 1472–1503.
Ba, Cuimin, J. Aislinn Bohren, and Alex Imas (2024), “Over- and Underreaction to Information,”
Working Paper.
Barberis, Nicholas (2018), “Psychology-Based Models of Asset Prices and Trading Volume,” in
Handbook of Behavioral Economics: Applications and Foundations, ed. by B. Douglas Bernheim,
Stefano DellaVigna, and David Laibson, vol. 1, Amsterdam: Elsevier, 79–175.
Barberis, Nicholas, Robin Greenwood, Lawrence Jin, and Andrei Shleifer (2015), “X-CAPM: An
extrapolative capital asset pricing model,” Journal of Financial Economics 115, 1–24.
Barberis, Nicholas, Andrei Shleifer, and Robert Vishny (1998), “A model of investor sentiment,”
Journal of Financial Economics 49, 307–343.
Benjamin, Daniel J. (2019), “Errors in Probabilistic Reasoning and Judgment Biases,” in Handbook
of Behavioral Economics: Applications and Foundations, ed. by B. Douglas Bernheim, Stefano
DellaVigna, and David Laibson, vol. 2, Amsterdam: Elsevier, 69–186.
can be applied immediately. But it would be useful to explore richer generalizations of our framework in
dynamic forecasting settings. We think these settings are particularly well suited for further applications
of our general framework, as they often feature news that is clearly “good” or “bad” relative to a previous
expectation, but with some uncertainty as to its precise meaning.
49

Bernard, Victor L. and Jacob K. Thomas (1989), “Post-Earnings-Announcement Drift: Delayed
Price Response or Risk Premium?” Journal of Accounting Research 27, 1–36.
van Binsbergen, Jules H., William F. Diamond, and Marco Grotteria (2022), “Risk-free interest
rates,” Journal of Financial Economics 143, 1–29.
Blavatskyy, Pavlo, Valentyn Panchenko, and Andreas Ortmann (2023), “How common is the
common-ratio e!ect?” Experimental Economics 26, 253–272.
Bliss, Robert R. and Nikolaus Panigirtzoglou (2004), “Option-Implied Risk Aversion Estimates,”
Journal of Finance 59, 407–446.
Bordalo, Pedro, John J. Conlon, Nicola Gennaioli, Spencer Y. Kwon, and Andrei Shleifer (2023),
“How People Use Statistics,” NBER Working Paper no. 31631.
Bordalo, Pedro, Nicola Gennaioli, Rafael La Porta, and Andrei Shleifer (2024), “Belief Overreaction
and Stock Market Puzzles,” Journal of Political Economy 132, 1450–1484.
Bordalo, Pedro, Nicola Gennaioli, Yueran Ma, and Andrei Shleifer (2020), “Overreaction in Macroe-
conomic Expectations,” American Economic Review 110, 2748–2782.
Bouchaud, Jean-Philippe, Philipp Krüger, Augustin Landier, and David Thesmar (2019), “Sticky
Expectations and the Profitability Anomaly,” Journal of Finance 74, 639–674.
Breeden, Douglas T. and Robert H. Litzenberger (1978), “Prices of State-Contingent Claims Implicit
in Option Prices,” Journal of Business 51, 621–651.
Chambers, Christopher P. and Paul J. Healy (2012), “Updating toward the signal,” Economic
Theory 50, 765–786.
Croxson, Karen and J. James Reade (2013), “Information and E"ciency: Goal Arrival in Soccer
Betting,” The Economic Journal 123, 1697–1724.
DellaVigna, Stefano and Joshua M. Pollet (2009), “Investor Inattention and Friday Earnings
Announcements,” Journal of Finance 64, 709–749.
Enke, Benjamin and Thomas Graeber (2023), “Cognitive Uncertainty,” Quarterly Journal of
Economics 138, 2021–2067.
Enke, Benjamin, Thomas Graeber, and Ryan Oprea (2024), “Complexity and Hyperbolic Discount-
ing,” NBER Working Paper no. 31047.
Fan, Tony Q., Yucheng Liang, and Cameron Peng (2024), “The Inference-Forecast Gap in Belief
Updating,” Working Paper.
Farmer, Leland E., Emi Nakamura, and Jón Steinsson (2024), “Learning About the Long Run,”
Forthcoming, Journal of Political Economy.
Frederick, Shane (2005), “Cognitive Reflection and Decision Making,” Journal of Economic Per-
spectives 19, 25–42.
Gabaix, Xaiver (2019), “Behavioral Inattention,” in Handbook of Behavioral Economics: Applications
and Foundations, ed. by B. Douglas Bernheim, Stefano DellaVigna, and David Laibson, vol. 2,
Amsterdam: Elsevier, 261–343.
Gandhi, Mihir, Niels Joachim Gormsen, and Eben Lazarus (2023), “Forward Return Expectations,”
NBER Working Paper no. 31687.
Giglio, Stefano and Bryan Kelly (2018), “Excess Volatility: Beyond Discount Rates,” Quarterly
Journal of Economics 133, 71–127.
Giglio, Stefano and Kelly Shue (2014), “No News Is News: Do Markets Underreact to Nothing?”
Review of Financial Studies 27, 3389–3440.
Gjerstad, Steven (2005), “Risk Aversion, Beliefs, and Prediction Market Equilibrium,” Working
Paper.
Gollier, Christian (2001), The Economics of Risk and Time, Cambridge, MA: MIT Press.
50

Gonçalves,Duarte,JonathanLibgober,andJackWillis(2024),“Retractions:UpdatingfromComplex
Information,” Working Paper.
Gonzalez, Richard and George Wu (1999), “On the Shape of the Probability Weighting Function,”
Cognitive Psychology 38, 129–166.
Green, Paul E., Michael H. Halbert, and Patrick J. Robinson (1965), “An Experiment in Probability
Estimation,” Journal of Marketing Research 2, 266–273.
Grether, David M. (1980), “Bayes Rule as a Descriptive Model: The Representativeness Heuristic,”
Quarterly Journal of Economics 95, 537–557.
Grether, David M. (1992), “Testing Bayes rule and the representativeness heuristic: Some experi-
mental evidence,” Journal of Economic Behavior and Organization 17, 31–57.
Gri"n, Dale and Amos Tversky (1992), “The Weighing of Evidence and the Determinants of
Confidence,” Cognitive Psychology 24, 411–435.
Hossain, Tanjim and Ryo Okui (2013), “The Binarized Scoring Rule,” Review of Economic Studies
80, 984–1001.
Karlin, Samuel (1968), Total Positivity, vol. 1, Stanford, CA: Stanford University Press.
Khaw, Mel Win, Ziang Li, and Michael Woodford (2021), “Cognitive Imprecision and Small-Stakes
Risk Aversion,” Review of Economic Studies 88, 1979–2013.
Kieren, Pascal, Jan Müller-Dethard, and Martin Weber (2024), “Disconfirming Information and
Overreaction in Expectations,” Working Paper.
Kormendi, Roger and Robert Lipe (1987), “Earnings Innovations, Earnings Persistence, and Stock
Returns,” Journal of Business 60, 323–345.
Kwon, Spencer Y. and Johnny Tang (2024), “Extreme Categories and Overreaction to News,”
Working Paper.
Lazarus, Eben (2022), “Horizon-Dependent Risk Pricing: Evidence from Short-Dated Options,”
Working Paper.
Liedke, Jacob and Je!rey Gottfried (2022), “U.S. adults under 30 now trust information from
social media almost as much as from national news outlets,” Pew Research Center, https:
//pewrsr.ch/3DF4dn1.
Malz, Allan M. (2014), “A Simple and Reliable Way to Compute Option-Based Risk-Neutral
Distributions,” Federal Reserve Bank of New York Sta! Report no. 677.
Manski, Charles F. (2006), “Interpreting the predictions of prediction markets,” Economics Letters.
Martin, Ian W. R. and Dimitris Papadimitriou (2022), “Sentiment and Speculation in a Market
with Heterogeneous Beliefs,” American Economic Review 112, 2465–2517.
McGranaghan,Christina,KirbyNielsen,TedO’Donoghue,JasonSomerville,andCharlesD.Sprenger
(2024), “Distinguishing Common Ratio Preferences from Common Ratio E!ects Using Paired
Valuation Tasks,” American Economic Review 114, 307–347.
Milgrom, Paul R. (1981), “Good News and Bad News: Representation Theorems and Applications,”
Bell Journal of Economics 12, 380–391.
Moore, Don A. and Paul J. Healy (2008), “The Trouble With Overconfidence,” Psychological Review
115, 502–517.
Moskowitz, Tobias J. (2021), “Asset Pricing and Sports Betting,” Journal of Finance 76, 3153–3209.
Phillips, Lawrence D. and Ward Edwards (1966), “Conservatism in a simple probability inference
task,” Journal of Experimental Psychology 72, 346–354.
Reimers, Stian and Nigel Harvey (2011), “Sensitivity to autocorrelation in judgmental time series
forecasting,” International Journal of Forecasting 27, 1196–1214.
Rigotti, Luca, Alistair Wilson, and Neeraja Gupta (2023), “The Experimenters’ Dilemma: Inferential
Preferences over Populations,” Working Paper.
51

Shapiro, Carl (1986), “Exchange of Cost Information in Oligopoly,” Review of Economic Studies 53,
433–446.
Shiller, Robert J. (1981), “Do Stock Prices Move Too Much to be Justified by Subsequent Changes
in Dividends?” American Economic Review 71, 421–436.
Tetlock, Paul C. (2014), “Information Transmission in Finance,” Annual Review of Financial
Economics 6, 365–384.
Thaler, Michael (2021), “Overinference from Weak Signals, Underinference from Strong Signals,
and the Psychophysics of Interpreting Information,” arXiv Working Paper 2109.09871v1, https:
//arxiv.org/pdf/2109.09871v1.
Vespa, Emanuel and Alistair Wilson (2017), “Paired-Uniform Scoring: Implementing a Binarized
Scoring Rule with Non-Mathematical Language,” Working Paper.
Wang, Chen (2021), “Under- and Overreaction in Yield Curve Expectations,” Working Paper.
Wolfers, Justin and Eric Zitzewitz (2006), “Interpreting Prediction Market Prices as Probabilities,”
NBER Working Paper no. 12200.
Woodford, Michael (2020), “Modeling Imprecision in Perception, Valuation, and Choice,” Annual
Review of Economics 12, 579–601.
52

Online Appendix
Overinference from Weak Signals and
Underinference from Strong Signals
Ned Augenblick, Eben Lazarus, and Michael Thaler
Contents
A Proofs and Additional Theoretical Discussion . . . . . . . . . . . . . . 2
A.1 Proofs for Section II.A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
A.2 Additional Discussion for Section II.B . . . . . . . . . . . . . . . . . . . . . . 4
A.3 Proofs and Additional Discussion for Section II.C . . . . . . . . . . . . . . . 5
A.4 Proofs and Additional Discussion for Section II.D . . . . . . . . . . . . . . . 8
A.5 Proofs for Section IV.A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
B Additional Data Details and Estimation Results . . . . . . . . . . . . . 10
B.1 Experimental Studies: Details and Robustness Checks . . . . . . . . . . . . . 10
B.2 Empirical Analysis: Details and Robustness Checks . . . . . . . . . . . . . . 17
C Experiment Study Materials . . . . . . . . . . . . . . . . . . . . . . . . . . 30
C.1 Study 1a . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
C.2 Study 1b . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
C.3 Study 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
1

A. Proofs and Additional Theoretical Discussion
A.1. Proofs for Section II.A
Proof of Proposition 1. Fix an arbitrary direction s . Given Assumption 3, we can write
d
S ˆ (sˆ) = ϑ(e)e+(1 ϑ(e))S ˆ (s d ) for some ϑ(e) (0,1), where ϑ( ) may depend on s d . We
↔ → ·
want to characterize
(A-1) E[S ˆ (sˆ) s] S(s) = E (1 ϑ(e))S ˆ (s d )+ϑ(e)e s S(s).
| ↔ ↔ ↔
. ! /
!
!
For notational convenience, assume a continuous space of estimates e (in which p(e s) is a
|
probability density function with support E R).1 From Assumption 1, E[e s] = S(s), so
⇑ |
S(s) = ep(e s)de, with p(e s) non-degenerate. Using this in (A-1),
| |
E
E[S ˆ (sˆ) s] S(s) = (1 ϑ(e))S ˆ (s
d
)+ϑ(e)e p(e s)de S(s)
| ↔ ↔ | ↔
E $ % 
(A-2) = (1 ϑ(e))(S ˆ (s
d
) e)p(e s)de.
↔ ↔ |
E
Denote g(e) (1 ϑ(e))(S ˆ (s
d
) e). For the first term in g(e), Assumption 3 gives that
↑ ↔ ↔
1 ϑ(e) > 0. For the second term, S ˆ (s d ) e crosses 0 exactly once for e R: it is positive
↔ ↔ →
for e < S ˆ (s d ), and negative for e > S ˆ (s d ). We thus have that
(A-3) E[S ˆ (sˆ) s] S(s) = g(e)p(e s)de = E[g(e) s] = E[g(e) s
d
,S],
| ↔ | | |

where g(e) is strictly single-crossing from above and where p(e s) = p(e s
d
,S) has the strict
| |
MLRP in S, from Assumption 1(b). By the variation diminishing property of Karlin (1968),2
the expectation of a strictly single-crossing function with respect to an MLRP distribution is
also strictly single-crossing, with the same arrangement of signs as the function (here, positive
and then negative). That is, if E[S ˆ (sˆ) s] S(s) = 0 at S(s) = S↑ , then there is overreaction
| ↔
(E[S ˆ (sˆ) s] S(s) > 0) for S(s) < S↑ and underreaction (E[S ˆ (sˆ) s] S(s) < 0) for S(s) > S↑ .
| ↔ | ↔
Further, this switching point S↑ must exist and lie within the range of feasible values
1The steps in the proof carry through for discrete e when replacing integrals with sums and adjusting
straightforwardly (though tediously) for discontinuities.
2See Karlin’s Theorem 3.1 of Chapter 5, or Gollier (2001, Proposition 16) for a textbook reference
based on the generalization of Athey (2002, Theorem 2). These results are typically stated for a function
that is single-crossing from below (SCB); in our case, one can define the SCB function g˜(e) g(e) and
then take S(s) E[S ˆ(sˆ)s] = g˜(e)p(es)de, and all the statements carry through with si ↑ gn ↔ s changed
↔ | |
appropriately. Note also that (A-3) can be restated, suppressing dependence on the arbitrary and fixed s , as
d
E[S ˆ(sˆ)S] S=E[g(e)S], and it  is this expression to which we apply Karlin’s result. (Note that all references
| ↔ |
in this Online Appendix are listed in the reference list in the main text.)
2

S(s)
→
[min
sm
S(s
d
,s
m
),max
sm
S(s
d
,s
m
)]. To see this, consider the case S(s) = min
sm
S(s
d
,s
m
).
By Assumption 2, S ˆ (s d ) > S(s) in this case, while E[e S] = S(s) by Assumption 1. Thus
|
E[S ˆ (sˆ) s] = E[ϑ(e)e+(1 ϑ(e))S ˆ (s d ) s]mustsatisfyS(s) < E[S ˆ (sˆ) s] < S ˆ (s d )byAssumption3,
| ↔ | |
where the lower bound obtains from ϑ(e) 1 and E[e S] = S(s) (and the upper bound
≃ |
obtains from ϑ(e) 0). Thus E[S ˆ (sˆ) s] S(s) > 0 at this minimal S(s). The same argument
≃ | ↔
gives that E[S ˆ (sˆ) s] S(s) < 0 at the maximal S(s). The intermediate value theorem then
| ↔
gives that there is such a switching point S↑
→
(min sm S(s d ,s m ),max sm S(s d ,s m )) at which
E[S ˆ (sˆ) s] S(s) = E[S ˆ (sˆ) s] S↑ = 0, and the single-crossing result above guarantees its
| ↔ | ↔
uniqueness, completing the proof. ↭
Derivation of Monotonicity Results. As at the end of Section II.A, under Assumptions 1–3,
it is not necessarily the case that a person’s expected signal strength S ˆ (sˆ) is monotonic in
e or that the amount of over- or underreaction E[S ˆ (sˆ) s] S(s) is monotonic in S(s). For
| ↔
conditions under which these additional monotonicity results hold, we again use Assumption 3
to write S ˆ (sˆ) = ϑ(e)e+(1 ϑ(e))S ˆ (s d ) for some ϑ(e) (0,1), and for simplicity assume that
↔ →
ϑ(e) is continuously di!erentiable (as are other relevant functions of e or S considered below).
Using this representation, a necessary and su"cient condition for S ˆ (sˆ) to be (strictly)
monotonically increasing in e is that
(A-4) ϑ ↓ (e) e S ˆ (s d ) +ϑ(e) > 0.
↔
$ %
For e > S ˆ (s d ), this requires that the weight on the estimate, ϑ(e), not fall dramatically given
small increases in e. For e < S ˆ (s d ), the weight on the estimate must not fall dramatically
given small decreases in e. Taken together, S ˆ (sˆ) will be monotonic in e as long as the weight
on the estimate does not fall dramatically given small increases in e S ˆ (s d ) (i.e., as e moves
| ↔ |
further from the default S ˆ (s d )), as stated in the text. Note that one simple su"cient condition
for (A-4) is the constant-weighting case (ϑ(e) = ϑ), since in this case ϑ(e) = 0 and the
↓
condition reduces to ϑ(e) > 0, which is guaranteed by Assumption 3.
Meanwhile, for E[S ˆ (sˆ) s] S(s) to be (strictly) monotonically decreasing in S(s), we must
| ↔
have that
d E S ˆ (sˆ) s
1 < 0.
$ .dS !
!
/% ↔
!
Fix a direction s
d
, so that conditioning on s is equivalent to conditioning on S. Since
3

E[S ˆ (sˆ) s] = (1 ϑ(e))S ˆ (s
d
)+ϑ(e)e p(e s)de, the above condition requires
| ↔ |
 $ %
↼p(e s)
(1 ϑ(e))S ˆ (s
d
)+ϑ(e)e | de < 1
↔ ↼S
 $ %
ςp(es)
(1 ϑ(e))S ˆ (s
d
)+ϑ(e)e ςS | p(e s)de < 1
⇓⇔ ↔ p(e s) |
 $ % |
ςp(es)
⇓⇔ E  (1 ↔ ϑ(e))S ˆ (s d )+ϑ(e)e p( ς e S | s) ! s  < 1,
!
$ % | !
 ! 
!
or equivalently that !
ςp(es) ςp(es)
(A-5) Cov s  ϑ(e)(e ↔ S ˆ (s d )), p( ς e S | s) < 1 ↔ E[S ˆ (sˆ) | s]E p( ς e S | s) ! s  ,
!
| | !
   ! 
!
where Cov ( , ) is the covariance conditional on s. Note further that !
s
· ·
ςp(e
|
s) ςp(e
|
s)
↼p(e s)
E ςS s = ςS p(e s)de = | de = 0,
p(e s) !  p(e s) | ↼S
| ! !  | 
 ! 
!
since the density must integ!rate to 1 for all S. The monotonicity condition in (A-5) can
therefore be simplified to
ςp(es)
(A-6) Cov s ϑ(e)(e S ˆ (s d )), ςS | < 1.
 ↔ p(e s)
|
 
εp(es)
By Assumption 1(b), εS | increases in e. Monotonicity in the degree of over-/underreaction
p(es)
|
in S therefore requires that ϑ(e) not increase dramatically with e, as stated in the text, so
that the covariance on the left side of (A-5) is less than 1. One can verify that this condition
is again immediately satisfied in the constant-weighting case.
A.2. Additional Discussion for Section II.B
This appendix briefly discusses the mapping between the general environment in Section II.A
and the log-normal environment in II.B. First, it is straightforward to verify that Assump-
tions 1 and 2 are satisfied in the log-normal environment. Assumption 3 is slightly more com-
plex. This assumption requires that S ˆ (s d ) < S ˆ (sˆ) < e when e > S ˆ (s d ), and S ˆ (s d ) > S ˆ (sˆ) > e
when e < S ˆ (s d ). Given the updating rule in (3), this requires exp(ϖ S 2/2) < S ˆ( e sd) when
4

e > S ˆ (s d ), and exp(ϖ e 2/2) < S ˆ( e sd) when e < S ˆ (s d ).3 In this case, the posterior is strictly
between the prior and estimate. Alternatively, to guarantee that Assumption 3 holds for all
e, one could drop the unbiasedness requirement of Assumption 1(a) (i.e., E[e S] = S, which is
|
an unimportant normalization) and assume loge (logS,ϖ2), in which case Assumption 3
↘N e
will always hold.
However, even if Assumption 3 is not guaranteed to hold in this log-normal setting, this
is unimportant for our main results on over- and underreaction. This is demonstrated in
equation (4), which shows that the conclusions in Proposition 1 apply regardless, and the
person accordingly overreacts to weak signals and underreacts to strong signals (with resulting
switching point S↑ discussed in the text) in this log-normal environment. We accordingly do
not focus on the conditions under which the primitive assumptions hold; what is important
is that the main results continue to hold in this setting.
A.3. Proofs and Additional Discussion for Section II.C
Prior Distortions: Incorrect Priors, Uncertain Priors, and Base-Rate Neglect. In the case
of an incorrect prior belief εˆ discussed at the beginning of Section II.C, we can calculate
0
the belief change logit(εˆ (s)) logit(εˆ ) when εˆ is observed. Perceived signal strength
1 0 0
| ↔ |
still follows the predictions in Proposition 1. Under the maintained assumption that belief
changes are monotonic in perceived signal strength (see footnote 11 in the main text), the
overreaction to weak signals and underreaction to strong signals in Proposition 1 will thus
continue to be reflected in the belief change logit(εˆ (s)) logit(εˆ ) .
1 0
| ↔ |
We now consider the case in which the correct prior is uncertain. We can model this by
adding a pre-period t = 1, and we assume that the person entered this previous period with
↔
a prior εˆ known with certainty, then observed a signal s (with known direction s ) and
→
1 0 d0
used a strength estimate e to form S ˆ (sˆ ) and εˆ (sˆ ) following Bayes’ rule given distributions
0 0 0 0 0
p(S
0
|
s
d0
) and p(e
0
|
s
d0
,S
0
).4 This post-estimation prior is then the center of a non-degenerate
distribution for the correct prior ε (s ), representing a situation with uncertainty over this
0 0
correct prior. The person then observes s and updates to εˆ (sˆ ) as before (again following
1 1 1
Bayes’ rule), with s independent of s conditional on ω, and with e and e depending only
1 0 0 1
3These conditions will hold for most draws of e given reasonably small variances. More formally, these
conditionsaresatisfiedalmostsurelyinasmall-noiselimitinwhichφ2/φ2 isfixedwhileφ2,φ2 0. Asimilar
e S e S ≃
limit is considered, for example, in Khaw, Li, and Woodford (2021, Section 4 and Appendix G).
4As in Section II.B, we continue to assume quasi-Bayesian updating. This allows us to formalize the
statement in the text that ωˆ incorporates all uncertainty about past signals. In the more general case
0
consideredinSectionII.A,thestatementthatthepersonoverreactstoweaksignalsandunderreactstostrong
signals in period 1 is almost tautological: as long as the belief change continues to be monotonic in perceived
signal strength, and perceived signal strength in period 1 is formed following Assumptions 1–3, then the
results hold immediately.
5

on s and s , respectively.5
0 1
With this setup, applying Bayes’ rule twice, the posterior given sˆ and sˆ is
0 1
p(sˆ ω = 1) p(sˆ sˆ ,ω = 1)
logit(εˆ ) = logit(εˆ )+log 0 | +log 1 | 0
1 1
→ "p(sˆ 0 ω = 0)# "p(sˆ 1 sˆ 0 ,ω = 0)#
| |
p(sˆ sˆ ,ω = 1)
= logit(εˆ (sˆ ))+log 1 | 0 .
0 0
"p(sˆ
1
sˆ
0
,ω = 0)#
|
Note that p(sˆ sˆ ,ω) = p(sˆ ω), since s and s are independent conditional on ω, and e and
1 0 1 0 1 0
| |
e depend only on s and s , respectively. Therefore,
1 0 1
p(sˆ ω = 1)
logit(εˆ ) = logit(εˆ (sˆ ))+log 1 | .
1 0 0
"p(sˆ
1
ω = 0)#
|
The belief update in period 1, logit(εˆ ) logit(εˆ (sˆ )) , accordingly depends on perceived
1 0 0
| ↔ |
signal strength log p(sˆ1| ε=1) exactly as was the case before, with the previous period’s
p(sˆ1| ε=0)
estimate (or mul!tipl$e previou%s! periods’ estimates) a!ecting only εˆ . Under the assumption
! ! 0
! !
that log p p ( ( s s ˆ ˆ 1 1 | | ε ε = = 1 0 ) ) is monotonic in S ˆ 1 (sˆ 1 ) = E ˆ [S 1 | s d1 ,e 1 ] (again as in main text footnote 11),
all ou!r re$sults the%r!efore carry through to this case.
! !
! !
In the case that the previously formed prior is unobserved, though, we cannot calculate
logit(εˆ ) logit(εˆ (sˆ )) directly. Instead, we again use logit(εˆ ) logit(ε ) as our proxy for
1 0 0 1 0
| ↔ | | ↔ |
reaction. This measure now includes both perceived signal strength and the prior distortion:
p(sˆ ω = 1)
(A-7) logit(εˆ ) logit(ε ) = logit(εˆ (sˆ )) logit(ε ) log 1 | .
1 0 0 0 0
| ↔ | | ↔ |±! "p(sˆ
1
ω = 0)#!
! | !
! !
! !
There are thus two cases to consider. (1) If the expected prior d!istortion in the fir!st term has
the same sign as the signal direction, then logit(εˆ ) logit(ε ) will overstate the degree of
1 0
| ↔ |
overreaction in the perceived signal strength S ˆ (sˆ), and there may appear to be overreaction
even to strong signals. This will apply, for example, if the correct prior is much lower than
0.5, but people do not use this correct prior and instead shade toward a default uninformative
prior of 0.5. This will push up the apparent reaction to a positive signal. (2) If the expected
prior distortion has the opposite sign as the signal direction, then logit(εˆ ) logit(ε ) will
1 0
| ↔ |
understate the degree of overreaction in the perceived signal strength S ˆ (sˆ), and there may
appear to be underreaction (or incorrectly signed reactions) even to weak signals. Intuitively,
the prior distortion o!sets the signal reaction in this case. We should expect these issues to
5Note that this setup does not depend on the specific timing of periods 0 and 1; this notation simply
formalizes the idea that the correct prior is formed from some signal (like information provided in an
experiment) separate from the additional piece of information in signal s .
1
6

matter less when the prior estimation is more precise than the signal strength estimation, or
when the default prior (often 0.5) is close to the correct prior.
The same analysis applies to the case with base-rate neglect, which will simply move
the e!ective prior εˆ in (A-7) toward the person’s default prior (which, in this binary-state
0
setting, is again often modeled as the uninformative prior of 0.5). Cases in which the correct
prior is equal to or close to 0.5 will therefore have little to no role for such base-rate neglect.
More generally, we expect our results to hold within a range of priors around ε = 0.5. (Based
0
on our experimental results, this range appears reasonably wide.) For correct priors close
to 0 or 1, meanwhile, given strong enough base-rate neglect, this can o!set our main e!ect
according to situations (1) and (2) as described in the preceding paragraph.
We discuss and control for the e!ects of base-rate neglect in additional detail in Sec-
tion III.B, which presents the results of an experiment with priors di!erent from 0.5. In
particular, as shown in eq. (8) and discussed in footnote 28 of the main text, the measured
signalweightwˆ(s)(whichweestimateas logitϖˆ1→ logitϖ0)willbedistortedbybase-rateneglectto
logitϖ1→ logitϖ0
the extent that logitε (the distance of the prior from 0.5) is high relative to logitε logitε
0 1 0
↔
(the true signed signal strength), though of course this only matters to the degree that the
person engages in strong base-rate neglect.
Uncertainty About the Direction. Following the discussion in the text, we now assume that the
person forms an estimate e of Ssigned , with that estimate satisfying Assumption 1 with respect
to Ssigned . In place of Assumption 2, we assume that the default value (the person’s subjective
prior) is S ˆ 0,signed = 0. This e!ectively assumes a symmetric signal strength distribution
where E[Ssigned ] = 0.6 Similar to Assumption 3, we assume that the posterior S ˆ signed (sˆ) is
strictly between 0 and the estimate e. Given this, it is immediate that on average, there is
underreaction in perceived signed strength: E[ S ˆ signed s] = a(s) Ssigned < Ssigned , where
| | | | | | |
a(s) (0,1). Note that this definition of underreaction is in terms of the absolute perceived
→
signed strength relative to the absolute true signed strength. The interpretation of this result
ˆ
as “underreaction” becomes more strained when the signs of Ssigned and Ssigned are di!erent,
as discussed in the main text.
6We note that the prediction of underreaction does not necessarily apply in asymmetric cases, which can
lead to strange situations. While the expected change in beliefs is always equal to 0 (at least for a Bayesian),
due to the non-linear transformation from signal strength to belief changes, it is not necessarily the case that
the signal strength has a mean of zero. If one removes the assumption of symmetry, we can say only that
there is underreaction for su"ciently extreme signed strengths, but we cannot necessarily make statements
acrossallsignalstrengths. Thisanalysisis,however,notthemainfocusgiventhesettingsweseektodescribe.
7

A.4. Proofs and Additional Discussion for Section II.D
Independent Estimates. We formally define the cross-sectional expectation as Ei [X i s] =
|
lim 1 N X for any measurable X (whose distributionimplicitly depends on s). Under
N N i=1 i i
↔↗
the assump-tions that the estimates e
i
are independent across people, there is no formal
distinction between taking the expectation with respect to the distribution of estimates
(as we did previously) and taking the cross-sectional expectation across people. Therefore,
Proposition 1 continues to apply, in the sense that there exists a unique switching point S↑
such that there is overreaction on average (Ei [S ˆ i (sˆ i ) s] > S(s)) if S(s) < S↑ , and there is
|
underreaction on average (Ei [S ˆ i (sˆ i ) s] < S(s)) if S(s) > S↑ .
|
Correlated Estimates and Over-/Underreaction Conditional on S. We consider the case with
multi-dimensional signals and perfect correlation in estimates given identical attention vectors
a for all i. In this case, as stated in the text, Proposition 1 holds under the following new
i
definition: there is overreaction if E[S ˆ
i
(sˆ
i
) S] > S, and underreaction if E[S ˆ
i
(sˆ
i
) S] < S.
| |
Since s
m,j
are i.i.d. over components j and exchangeable, E[s
m,j
S] = logS. (By compari-
|
son, conditional on s, s m,j is known, so a given person’s S ˆ (s) in that case could potentially
di!er across s for the same S, invalidating our results. This motivates our conditioning on S
here.) Similarly, e
i
is log-normally distributed conditional on S, loge
i ↘N
(logS
↔
ϖ
e
2
,i
/2,ϖ
e
2
,i
),
where this (and the expression for ϖ2 provided in the text) follow from standard characteriza-
e,i
tions of a multivariate normal distribution along with some algebra. Therefore, conditioning
on S, E[S ˆ
i
(sˆ
i
) S] = kS ω, where k and ϱ are as given in the text. This is exactly as in (4), and
|
we conclude that Proposition 1 applies using the above definition of over- and underreaction.
Further, since we have assumed the extreme case of perfectly correlated estimates, this will
also apply when considering the expected cross-sectional expectation E[Ei [S ˆ
i
(sˆ
i
) s] S] given
| |
that S ˆ i (sˆ i ) is identical across i for a given s.
Predictions on Correlation Behavior. As stated in the text, one can make further statements
about the correlation in updating behavior across people under additional assumptions about
the signal components and person-specific vectors a . For example, if the components are
i
ordered by salience, then it is natural to assume that a is such that a = 1 for j n and
i i,j i
↗
a = 0 for n < j n (i.e., person i pays attention to the first n components, and the only
i,j i i
↗
di!erence across people is in how large n is). In this case, the following expression holds
i
for the ex ante correlation between estimates for any two people i and i, ordered such that
↓
0 < n n :
i i
↗ ↑
n
i
Corr(e ,e ) = (0,1].
i i
↑  n i →
↑
8

This expression follows from the fact that Cov(e ,e ) = Var(s )/max(n ,n ), while
i i m,j i i
↑ ↑
Var(e ) = Var(s )/n and Var(e ) = Var(s )/n .
i m,j i i m,j i
↑ ↑
The above expression can be generalized to cases where the components are not salience-
ordered. In these cases, the correlation will simply scale down as one decreases the overlap in
the entries of a and a that are equal to 1. For example, if there are two components and
i i
↑
two types of people, with type 1 attentive only to component 1 and type 2 attentive only to
component 2, then there will be multimodal estimates, with perfect correlation across people
within type and none across types. With high-dimensional vectors in which the components
are not ordered according to salience (i.e., cases where people’s attention vectors are varied),
estimates will be closer to the independent case, and we will see smoother distributions of
resulting strength perceptions.
A.5. Proofs for Section IV.A
Proof of Proposition 2. Here, we provide a brief restatement of the proof of Proposition 1 of
AR (2021) for completeness. Since ε t = ε t (H t ) = Et [ω], by the law of iterated expectations
(LIE), beliefs are a martingale: ε t = Et [ε t+1 ]. Therefore, for arbitrary t 1 ,
Et1 [M t1,t1+1
↔
R t1,t1+1 ] = Et1 [(ε t1+1
↔
ε t1 )2
↔
(ε t1 (1
↔
ε t1 )
↔
ε t1+1 (1
↔
ε t1+1 ))]
= Et1 [(2ε t1
↔
1)(ε t1
↔
ε t1+1 )]
= (2ε
t1
↔
1)(Et1 [ε
t1
↔
ε
t1+1
]) = 0,
where the first line uses the definition of movement and uncertainty reduction, the second
line simplifies, and the last line rearranges and uses the martingale property of beliefs.
Similarly, Et1+ϱ [M t1+ϱ,t1+ϱ+1
↔
R t1+ϱ,t1+ϱ+1 ] = 0 for any ↽
↓
0, and therefore by the LIE,
Et1 [M t1+ϱ,t1+ϱ+1
↔
R t1+ϱ,t1+ϱ+1 ] = 0. So summing all these terms from t 1 to arbitrary t 2 > t 1 ,
t2→ t1→ 1
Et1 [M t1,t2
↔
R t1,t2 ] = Et1 [M t1+ϱ,t1+ϱ+1
↔
R t1+ϱ,t1+ϱ+1 ] = 0,
ϱ=0
,
as stated. ↭
9

B. Additional Data Details and Estimation Results
B.1. Experimental Studies: Details and Robustness Checks
Study 1a
Timing Details. Participants saw the following five treatment blocks: (1) one symmetric
signal, (2) one asymmetric signal, (3) three symmetric signals, (4) demand for information,
(5) uncertain signals. Details of each are in the subsequent subsections. The ordering of when
they saw each treatment block was as follows:
Rounds Treatment Block Frequency Observations
1–12 One symmetric signal 67 percent 4,036
1–12 One asymmetric signal 33 percent 1,964
13 Attention check 100 percent 500
14–18 Three symmetric signals 100 percent 2,500
19–23 Demand for information 100 percent 2,500
24–25 One uncertain signal 100 percent 1,000
Questions within each treatment block were randomized for each participant. The ordering
of treatment blocks (besides “one symmetric” and “one asymmetric”) were fixed for ease of
participant comprehension. For instance, participants do not see the “demand for information”
treatment until they have played rounds in which they inferred from one signal and from
multiple signals. The uncertain-signals treatment comes after the demand-for-information
treatment because they do not reflect the signals that participants would purchase.
10

Additional Results Discussed in the Text. Figures A1–A3 provide additional results discussed
in the text.
Figure A1. Comparison to Literature
2.5
2
1.5
1
.5
0
)1
=
seyaB(
langiS
no
thgieW
.5 .6 .7 .8 .9 1
Signal Precision
Our Data (Study 1a) Benjamin (2019)
Notes: Thisfigureshowstheweightputonsignalsofdi"erentprecisions,whereweightisdefinedrelativetoaBayesian
(whoseweightof1isintheblueline)asinthemaintext. BlackcirclescorrespondtodatafromourStudy1awith95%
confidenceintervals(asplottedinFigureII).LighttranslucentcirclescorrespondtodatafromBenjamin(2019). Weuse
thedatafromhissupplementaryfiles,restrictingtothe70studiesinwhichparticipantsupdatefromonebinarysignal
whentheprioris0.5andsignalprecisionissymmetric. Notethatmostpapersincludemultiplestudies.
11

Figure A2. Heterogeneity in Inference at the Individual Level
1
.8
.6
.4
.2
0
sesnopseR
fo
erahS
0 .5 1 1.5 2 2.5
Weight on Signals
Strong Signals Weak Signals
.5
.4
.3
.2
.1
0
sesnopseR
fo
erahS
Weight<0 Weight=0 -2 -1 0 1 2 3
Log(Weight on Signals)
Weak Signals Strong Signals
Notes: This figure shows how much weight is put on weak and strong signals at the individual level, where weight is
definedrelativetoaBayesianasinthemaintext. ThetoppanelshowstheCDFofindividuals’weightsonstrongandweak
signals. Theverticallineat1representsBayesianupdating. ThebottompanelshowsthePDFofthelogofindividuals’
weightsonstrongandweaksignals. Theverticallineat0representsBayesianupdating. Participantswithnonpositive
weightareseparatedout. Weaksignalshaveprecisionp<0.6andstrongsignalshaveprecisionp>0.7. Observationsare
winsorized,foreachsignalstrength,atthe5%level.
12

Figure A3. Over- and Underinference by Number and Strength of Signals
2.5
2
1.5
1
.5
0
)1
=
seyaB(
langiS
no
thgieW
.5 .6 .7 .8 .9 1
Signal Precision
One positive, zero negative Two positive, one negative Three positive, zero negative
Notes: ThisfigureplotstheaverageweightparticipantsputonsignalsrelativetoaBayesian(indicatedbythedashedline),
splitbysignaldistribution. Blackcirclescorrespondtoonesignalofprecisionφ(asinFigureII);lightsquarescorrespond
totwosignalsofprecisionφinonedirectionandonesignalofprecisionφintheopposingdirection;andhollowdiamonds
correspondtothreesignalsofstrengthS/3,whereS=logitφforprecisionφ,inthesamethedirection. Thisfigureshows
thatparticipantsputlessweightonthreesignalsascomparedtotheweighttheyputononesignalbutthatweightdeclines
insignalprecisioninallcases. Errorbarsindicate95%confidenceintervals.
13

Further Results: Demand for Information. Patterns of overinference and underinference can
also lead to demand for information that is too high or too low relative to the optimum.
Figure A4 plots the average number of signals purchased as a function of each signal strength,
comparing participant behavior to the optimal choice if participants were Bayesian and only
valued signals for their instrumental value.
Figure A4. Number of Signals Purchased
3
2.5
2
1.5
1
.5
0
desahcruP
slangiS
.5 .55 .6 .65 .7 .75
Signal Precision
Notes: Thisfigureplotsthenumberofsignalspurchasedasafunctionofsignalprecision. Thehorizontallinescorrespond
tothepayo"-maximizingnumberofsignalsthatwouldbepurchased. Thisfigureshowsthatparticipantsover-purchase
weaksignalsandunder-purchasestrongsignalsrelativetoapayo"maximizer. Errorbarsindicate95%confidenceintervals.
As can be seen in the figure, participants systematically over-purchase weak signals and
under-purchase strong signals. The cost of a signal that leads a Bayesian to form a posterior
of less than 0.57 outweighs its benefit; however, the majority of participants purchase at least
one signal when p = 0.55 and p = 0.525. Additionally, 81 percent of participants purchase
fewer than the optimal level of three signals when p = 0.73. Over- and underinference patterns
therefore matter not just for stated beliefs; they also lead people to overvalue low-quality
information and undervalue high-quality information, as reflected in their purchase decisions.
14

Study 1b
Grether Regression Approach
Table A1. E!ect of Logit Prior and Signal Strength on Logit Posterior
(1) (2) (3) (4)
50% Prior All Priors All Priors All Priors
Signal Strength: 0.05 2.371 2.844 2.800 2.795
(0.224) (0.286) (0.179) (0.178)
Signal Strength: 0.20 1.359 1.554 1.504 1.500
(0.072) (0.083) (0.059) (0.059)
Signal Strength: 0.50 1.176 1.208 1.190 1.191
(0.054) (0.041) (0.035) (0.035)
Signal Strength: 1.25 0.840 0.852 0.857 0.857
(0.028) (0.021) (0.020) (0.020)
Signal Strength: 1.75 0.824 0.768 0.762 0.762
(0.021) (0.017) (0.015) (0.015)
Logit Prior 1 0.984
(.) (0.016)
Logit Prior: Signal=0.05 1.028
(0.017)
Logit Prior: Signal=0.20 1.036
(0.021)
Logit Prior: Signal=0.50 0.996
(0.023)
Logit Prior: Signal=1.25 0.944
(0.029)
Logit Prior: Signal=1.75 0.915
(0.029)
Participant FE Yes Yes Yes Yes
Round FE Yes Yes Yes Yes
Observations 2500 7500 7500 7500
R2 0.80 0.60 0.76 0.76
Notes: OLS,withstandarderrorsinparenthesesclusteredatparticipantlevel. Weregresslogit
posterioroneachsignalstrengthseparately. Column(1)restrictstoobservationswheretheprioris
symmetric(asinStudy1a);othercolumnsusethefulldataset. Column(2)assumesthatpeopleput
weight1ontheirprior. Column(3)allowsformisweightingpriorsoverall. Column(4)allowsfor
weightsonpriorstovaryforeachsignalstrength. Seemaintextfordiscussion.
15

Study 2
Grether Regression Approach
Table A2. Weight on Signal and Prior by Quarter of Basketball Game
(1) (2) (3)
All Quarters All Quarters All Quarters
Quarter 1 x Signal Strength 1.344 1.405 1.406
(0.108) (0.066) (0.066)
Quarter 2 x Signal Strength 1.398 1.360 1.359
(0.110) (0.059) (0.059)
Quarter 3 x Signal Strength 0.968 0.929 0.928
(0.070) (0.041) (0.040)
Quarter 4 x Signal Strength 0.735 0.585 0.587
(0.037) (0.020) (0.020)
Logit Prior 1 0.906
(.) (0.013)
Quarter 1 x Logit Prior 1.001
(0.051)
Quarter 2 x Logit Prior 0.948
(0.031)
Quarter 3 x Logit Prior 0.917
(0.025)
Quarter 4 x Logit Prior 0.889
(0.014)
Participant FE Yes Yes Yes
Round FE Yes Yes Yes
Quarter FE Yes Yes Yes
Observations 8000 8000 8000
R2 0.48 0.86 0.86
Notes: OLS,withstandarderrorsinparenthesesclusteredatparticipantlevel. Weregresslogit
posterioronsignalsineachquarterseparately. Column(1)assumesthatpeopleputweight1on
theirprior. Column(2)allowsformisweightingpriorsoverall. Column(3)allowsforweightson
priorstovaryforeachquarter. Seemaintextfordiscussion.
16

B.2. Empirical Analysis: Details and Robustness Checks
Measurement Details for Risk-Neutral Beliefs
This subsection describes our use of option-price data, as introduced in Section IV.C, in
greater detail. (Much of this detail is directly from AL 2023.) First, we describe how we
clean the option data and then translate the option prices to risk-neutral beliefs. We then
detail how we translate from risk-neutral to physical beliefs under di!erent parameterizations
for risk aversion.
Option Data Cleaning and the Risk-Neutral Distribution. We start from the OptionMetrics
data described in the text, obtaining the end-of-day bid and ask prices for all European call
and put options on the S&P 500 index, for all available strike prices and option expiration
dates for trading dates from January 1996 through December 2018. We then average the bid
and ask price to obtain the mid price. We also, as in AL (2023), obtain S&P 500 index prices
to use when determining the realized index-return state. We first get end-of-day index prices
(which we take as well from OptionMetrics, and then augment these with hand-collected
settlement values for any options whose settlement value depends on the opening (rather
than closing) index price, from the CBOE website.7
To measure the risk-free rate
Rf
in order to define our excess return space, we follow
t,T
van Binsbergen, Diamond, and Grotteria (2022) and estimate the risk-free rate from the
cross-section of option prices by applying put-call parity. We use their “Estimator 2,” which
estimates
Rf
from Theil–Sen (robust median) estimation of the put-call parity relationship.
t,T
This provides a risk-free rate consistent with observed option prices.
For the OptionMetrics data, we then use the same steps as described in Online Ap-
pendix C.5 of AL (2023) to clean the data and convert to a risk-neutral distribution. For
cleaning, we drop any options with bid or ask price of zero (or less than zero), with uncom-
putable Black–Scholes implied volatility or with implied volatility of greater than 100 percent,
with more than one year to maturity, or (for call options) with mid prices greater than the
price of the underlying; we drop any option cross-section (i.e., the full set of prices for the pair
(t,T)) with no trading volume on date t, with fewer than three listed prices across di!erent
strikes, or for which there are fewer than three strikes for which both call and put prices are
available (as is necessary to calculate the forward price and risk-free rate).
We then measure the risk-neutral distribution following Malz (2014), again as described
7The results for the binarized noise-corrected data in Figure A10 below also use separate data directly
from AL (2023), so we refer to that paper — in particular, Section 6 and Online Appendix C.5–C.6 — for
details on the data and methodology used for the noise estimation (which use intraday option data obtained
directly from the CBOE), as well as the conversion of the histogram of risk-neutral beliefs to binarized beliefs.
17

in Online Appendix C.5 of AL (2023):
1. We translate the option mid prices into equivalent Black–Scholes implied volatilities.
2. We discard the resulting observations for in-the-money calls and puts, so that the
remaining steps use data from only out-of-the-money put and call prices. To determine
the at-the-money point, we use the strike K at which call and put prices are equal (or
closest to each other).
3. For each trading date–expiration date pair, we fit a clamped cubic spline to the resulting
implied volatility curve (i.e., the curve of implied volatility vs. strike price).
4. Evaluate this spline at 1,901 strike prices, for S&P index values ranging from 200 to
4,000 (so that the evaluation strike prices are K = 200,202,...,4000), to obtain a set
of fitted implied-volatility values across this fine grid of possible strike prices for each
(t,T) pair.
5. Invert the resulting smoothed implied volatility schedule back into call prices qˆ .
t,T,K
6. Using a discrete-state version of the classic Breeden and Litzenberger (1978) formula,
calculate the risk-neutral CDF for the date-T index value at strike price K as follows:
P↑t (V T < K) = 1+R t f ,T (qˆ t,T,K ↔ qˆ t,T,K → 2 )/2.
7. Defining V and V to be the date-T index values corresponding to the upper
T,j,max T,j,min
and lower bounds, respectively, of the bin defining return state ω (i.e., the upper
j
and lower end of the five-percentage-point excess-return range defining a given return
outcome), calculate the risk-neutral belief that state ω will be realized at date T as
j
ε t↑,j = P↑t (V T < V T,j,max )
↔
P↑t (V T < V T,j,min ). (The beliefs for states ω 1 and ω 10 then
collect the tail probabilities for below -20% and above 20% returns, respectively.)
We do this for states ω ,...,ω , where the return states are as defined and described in
1 10
the text — i.e., 5-log-point ranges of log excess returns from the first observable option
trading date (within a year of expiration) to the expiration date — for all trading dates under
consideration. We then use the resulting histogram of risk-neutral beliefs for our tests.
We note that unlike AL (2023), we include beliefs over the tail return states ω and ω ,
1 10
whereas AL discard them before calculating binarized beliefs ε /(ε +ε ). AL discard
t↑,j t↑,j t↑,j+1
them due to concerns over complications from potential changes in risk aversion over tail
outcomes; given the binarization, small changes in risk aversion would have large e!ects on
the measured binarized RN beliefs. But this is not the case for our analysis: since we just
use the (non-binarized) histogram of beliefs, the tail states have very low probabilities and
thus do not meaningfully a!ect the results. (Results are very similar when only including
movement and uncertainty reduction for states 2 through 9.) This is another way in which
18

just using the RN histogram, rather than continuing from above and calculating the binarized
beliefs, helps minimize the potential e!ect of noise on our results.
Translating from Risk-Neutral to Physical Beliefs. Given the RN beliefs as measured from
above, we now describe the translation from RN to physical beliefs in greater detail. Assume
there exists a representative investor (“the market”) with time-separable utility over the
market index value.8 Assume, as above, that the state space (the set of possible terminal
index values V ) is discrete, with states indexed by j (V = ω for j = 1,2,...,J), and denote
T T j
terminal utility by U(V ). The physical belief regarding the likelihood of state j is ε , and
T t,j
the risk-neutral belief is ε . The two are related as follows:
t↑,j
U (ω )ε
↓ j t,j
(A-8) ε = .
t↑,j
U (ω )ε
k ↓ k t,k
-
(This is a multi-state generalization of equation (5) of AL 2023, or see equation (7) of Bliss
and Panigirtzoglou 2004.) Our main translation assumes that U ↓ (V T ) = V T→ ↼, corresponding
to the assumption of power utility over the terminal index return, with constant relative risk
aversion coe"cient of φ. We then follow Bliss and Panigirtzoglou (2004) in estimating φ as
the value under which the physical beliefs over the S&P 500 value at the one-month horizon
are well calibrated (i.e., unbiased); see Bliss and Panigirtzoglou (2004) for details on the
maximum likelihood estimation procedure.9
We then consider dozens of generalizations of this basic framework. First, we reparameter-
ize (A-8) in terms of the ratio of marginal utilities (or SDF realizations) across adjacent index
states ⇀ , by substituting U (ω ) = ⇀ U (ω ). We then make a range of assumptions on the
j ↓ j j ↓ j 1
→
function ⇀ . We assume that ⇀ varies by state j, either linearly or quadratically in V , and
j j T
we estimate ⇀ by maximum likelihood for each state; we assume that ⇀ varies over time
j j
(either linearly or quadratically) or by horizon to expiration (as in Lazarus 2022); and then we
consider interactions in which ⇀ varies both by bin j and over time. In all cases (as can be
j
seen in Figure A9, the right panel of which contains one line for each parameterization), the
movement and uncertainty reduction statistics are close to unchanged. (This is in contrast
to the physical probabilities, which do change depending on the parameterization; it is their
evolution over time that is unchanged.)
8These illustrative assumptions aid in the interpretation of our risk-aversion assumptions, but they are
stronger than needed in general; see AL (2023) for a discussion.
9Like Bliss and Panigirtzoglou (2004), we obtain reasonable estimates of risk aversion of (with estimated
ςˆ< 10) given this calibration procedure.
19

Additional Empirical Results
We now provide a set of robustness results (Figures A5–A12 and Tables A3–A4) for the
betting and finance data. As described in the text, we present figures and regression tables
for when the data is split into either 12 or 36 time chunks. For the options data, we also show
results of di!erent risk adjustments, use of binarized noise-corrected data, and in subsamples.
Di!erent Time Windows
Figure A5. Movement and Uncertainty Reduction for Sports Betting: 12 Time Chunks
.025
.02
.015
.01
.005
0
wodniW
ni
egarevA
Soccer
.03
Belief Movement
Uncertainty Reduction
.02
.01
0
0 18 36 54 72 90 108
Game Minute
wodniW
ni
egarevA
Basketball
0 22 44 66 88 110 132
Game Minute
.06
.04
.02
0
wodniW
ni
egarevA
Baseball
.08
.06
.04
.02
0
0 34 68 102 136 170 204
Game Minute
wodniW
ni
egarevA
Ice Hockey
0 24 48 72 96 120 144
Game Minute
.04
.03
.02
.01
0
wodniW
ni
egarevA
American Football
0 32 64 96 128 160 192
Game Minute
Notes: ThisfigurereplicatesFigureVII,butwith12equal-lengthtimewindows,ratherthan24. Seethatfigure’snotesfor
detailsonconstruction.
20

Figure A6. Movement and Uncertainty Reduction for Finance Data: 12 Time Chunks
.025
.02
.015
.01
.005
0
wodniW
ni
egarevA
S&P Options: Unadjusted
.025
Belief Movement
Uncertainty Reduction
.02
.015
.01
.005
0
0 10 20 30 40 50 60 70 80 90 100
Trading Day
wodniW
ni
egarevA
S&P Options: Risk-Adjusted
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: ThisfigurereplicatesFigureVIII,butwith12equal-lengthtimewindows,ratherthan24. Seethatfigure’snotes
fordetailsonconstruction.
21

Table A3. Regressions of Movement on Uncertainty Reduction: 12 Time Chunks
Sports Finance
Dep. Var.:
Movement Soccer Basketball Baseball Hockey Football Raw Risk-Adj.
Constant 0.0014 0.0018 0.0024 0.0013 0.0015 0.0060 0.0054
(0.0003) (0.0003) (0.0004) (0.0009) (0.0002) (0.0005) (0.0005)
Uncert. Red. 0.839 0.797 0.903 0.987 0.912 0.796 0.861
(0.006) (0.007) (0.012) (0.012) (0.027) (0.054) (0.063)
R2 0.984 0.991 0.996 0.990 0.997 0.945 0.941
Time Chunks 12 12 12 12 12 12 12
Events 175,026 48,430 16,536 19,445 3,212 955 955
Belief Obs. 4,589,289 867,567 166,346 109,751 86,193 58,864 58,864
p-val: Const = 0 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001
p-val: Slope = 1 <0.001 <0.001 <0.001 0.274 0.002 0.004 0.025
Notes: ThistablereplicatesTableIII,butwith12equal-lengthtimewindows,ratherthan24. Seethattable’snotesfordetails
onestimationandinterpretation.
22

Figure A7. Movement and Uncertainty Reduction for Sports Betting: 36 Time Chunks
.03
.02
.01
0
wodniW
ni
egarevA
Soccer
.03
Belief Movement
Uncertainty Reduction
.02
.01
0
0 12 24 36 48 60 72 84 96 108
Game Minute
wodniW
ni
egarevA
Basketball
0 12 24 36 48 60 72 84 96 108
Game Minute
.06
.04
.02
0
wodniW
ni
egarevA
Baseball
.1
.08
.06
.04
.02
0
0 20 40 60 80 100 120 140 160 180
Game Minute
wodniW
ni
egarevA
Ice Hockey
0 16 32 48 64 80 96 112 128 144
Game Minute
.04
.03
.02
.01
0
wodniW
ni
egarevA
American Football
0 20 40 60 80 100 120 140 160 180
Game Minute
Notes: ThisfigurereplicatesFigureVII,butwith36equal-lengthtimewindows,ratherthan24. Seethatfigure’snotesfor
detailsonconstruction.
23

Figure A8. Movement and Uncertainty Reduction for Finance Data: 36 Time Chunks
.05
.04
.03
.02
.01
0
wodniW
ni
egarevA
S&P Options: Unadjusted
.05
Belief Movement
Uncertainty Reduction
.04
.03
.02
.01
0
0 10 20 30 40 50 60 70 80 90 100
Trading Day
wodniW
ni
egarevA
S&P Options: Risk-Adjusted
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: ThisfigurereplicatesFigureVIII,butwith36equal-lengthtimewindows,ratherthan24. Seethatfigure’snotes
fordetailsonconstruction.
24

Table A4. Regressions of Movement on Uncertainty Reduction: 36 Time Chunks
Sports Finance
Dep. Var.:
Movement Soccer Basketball Baseball Hockey Football Raw Risk-Adj.
Constant 0.0014 0.0016 0.0027 0.0020 0.0015 0.0063 0.0058
(0.0001) (0.0001) (0.0002) (0.0002) (0.0001) (0.0003) (0.0003)
Uncert. Red. 0.847 0.849 0.883 0.925 0.920 0.705 0.751
(0.003) (0.008) (0.015) (0.013) (0.026) (0.035) (0.040)
R2 0.955 0.974 0.993 0.975 0.982 0.932 0.928
Time Chunks 36 36 36 36 36 36 36
Events 175,026 48,430 16,536 19,445 3,212 955 955
Belief Obs. 4,589,289 867,567 166,346 109,751 86,193 58,864 58,864
p-val: Const = 0 <0.001 <0.001 <0.001 <0.001 0.051 <0.001 <0.001
p-val: Slope = 1 <0.001 <0.001 <0.001 <0.001 0.054 <0.001 <0.001
Notes: ThistablereplicatesTableIII,butwith36equal-lengthtimewindows,ratherthan24. Seethattable’snotesfordetails
onestimationandinterpretation.
25

Further Robustness Results for Options Data
Figure A9. Movement and Uncertainty Reduction for Options: Alternative Adjustments
.1
.08
.06
.04
.02
0
wodniW
ni
egarevA
S&P Options: Risk-Adjusted
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: ThisfigurereplicatestherightpanelofFigureVIIItoshowthesmoothedaveragemovement(blacklines)and
uncertaintyreduction(lighterredlines)statisticsovertimeforthebeliefsimpliedbyoptiondata,butwithalternativerisk
adjustments. Eachlinerepresentsadi"erentmethodtocalculaterisk-adjustedbeliefsfromtheraw,unadjustedrisk-neutral
beliefs,asdescribedinAppendixB.2. Someaspectsofthefigure(includingconfidenceintervals)areomittedtoenablea
clearviewoftherangeofplottedlinesacrossriskadjustments. Whilethedi"erentrisk-adjustmentmethodsdoleadto
di"erentinferredbeliefs,thebroadpatternofmovementanduncertaintycurvesisverysimilaracrossthemethods,asthe
curvesareclosetooverlappinginmostcases.
26

Figure A10. Movement and Uncert. Red. for Finance: Binarized, Noise-Corrected Beliefs
.015
.01
.005
0
-.005
wodniW
ni
egarevA
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: ThisfigurereplicatestheleftpanelofFigureVIII,butusingthebinarizedandnoise-correctedrisk-neutralbeliefs
datafromAugenblickandLazarus(2023). Beliefmovementisplottedinblack,anduncertaintyreductioninlighterred.
Dataarenotadjustedforriskaversion. SeeFigureVIIIfordetailsontheplot,andseeSection6andOnlineAppendixC.6
ofAL(2023)fordetailsonthenoisecorrectionandbinarization.
27

Figure A11. Movement and Uncertainty Reduction for Finance Data: Post-2000
.04
.03
.02
.01
0
wodniW
ni
egarevA
S&P Options: Unadjusted
Belief Movement .04
Uncertainty Reduction
.03
.02
.01
0
0 10 20 30 40 50 60 70 80 90 100
Trading Day
wodniW
ni
egarevA
S&P Options: Risk-Adjusted
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: This figure replicates Figure VIII, using only data after the year 2000. See that figure’s notes for details on
construction. The figure demonstrates that our option results are robust to not including the early part of the sample,
whichcontainssomewhatnoisieroptiondata(seeAL2023).
28

Figure A12. Movement and Uncertainty Reduction for Finance Data: Post-2010
.04
.03
.02
.01
0
wodniW
ni
egarevA
S&P Options: Unadjusted
Belief Movement .04
Uncertainty Reduction
.03
.02
.01
0
0 10 20 30 40 50 60 70 80 90 100
Trading Day
wodniW
ni
egarevA
S&P Options: Risk-Adjusted
0 10 20 30 40 50 60 70 80 90 100
Trading Day
Notes: ThisfigurereplicatesFigureVIII,usingonlydataafter2010. Seethatfigure’snotesfordetailsonconstruction.
AlongwithFigureA11,thisfiguredemonstratesthatouroptionresultsarerobustacrosssubsamples.
29

C. Experiment Study Materials
C.1. Study 1a
Overview and Instructions
30

31

32

Main Decision Screen
33

Attention Check
34

Unknown Signal Strength
35

Demand for Information
36

37

Demographics
38

39

Cognitive Reflection Test
40

41

C.2. Study 1b
Overview and Instructions
42

43

44

45

Main Decision Screen
46

Attention Check
47

Confidence Elicitation
48

C.3. Study 2
Overview and Instructions
49

50

51

Main Decision Screen
52

Attention Check
53
