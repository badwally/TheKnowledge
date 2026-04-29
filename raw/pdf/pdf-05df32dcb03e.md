---
id: pdf-05df32dcb03e
type: pdf
title: SSRN-id1630903
url: ''
authors: []
ingested_at: '2026-04-29T16:25:28Z'
content_hash: sha256:bd7509ac0d84049c3d2a449a89ad1d33f1c1943d864eb5e114c487f7f135a5db
source_path: raw/pdf/pdf-05df32dcb03e.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 20
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/SSRN-id1630903.pdf
published_at: '2015'
---
MATHEMATICS OF OPERATIONS RESEARCH INFORMS
Vol.00,No.0,Xxxxx0000,pp.000–000 doi10.1287/xxxx.0000.0000
issn0364-765X|eissn1526-5471|00|0000|0001
(cid:13)c 0000INFORMS
Optimal Trend Following Trading Rules
Min Dai
DepartmentofMathematicsandRiskManagementInstitute, NationalUniversityofSingapore,
Singapore,matdm@nus.edu.sg
Zhou Yang
SchoolofMathematicalSciences, SouthChinaNormalUniversity,Guangzhou, China,yangzhou@scnu.edu.cn
Qing Zhang
DepartmentofMathematics,TheUniversityofGeorgia,Athens,GA30602,USA,qz@uga.edu
Qiji Jim Zhu
DepartmentofMathematics,WesternMichiganUniversity,Kalamazoo,MI49008,USA,zhu@wmich.edu
This paper is concerned with the optimality of a trend following trading rule. The underlying market is
modeled as a bull-bear switching market in which the drift of the stock price switches between two states:
theuptrend(bullmarket) and thedowntrend (bearmarket).Weconsider that case when themarket mode
isnotdirectlyobservableandmodeltheswitchingprocessasahiddenMarkovchain.Thisisacontinuation
of ourearlier studyreported inDaietal. [5]whereatrendfollowing ruleisobtained intermsofasequence
of stopping times. Nevertheless, a severe restriction imposed in [5] is that only a single share can be traded
over time. As a result, the corresponding wealth process is not self-financing. In this paper, we relax this
restriction. Our objective is to maximize the expected log-utility of the terminal wealth. We show, via a
thorough theoretical analysis, that the optimal trading strategy is trend-following. Numerical simulations
and backtesting, in support of our theoretical findings,are also reported.
Key words: Trend following trading rule, bull-bearswitching model, partial information, HJB equations
MSC2000 subject classification: 91B28, 93E11, 93E20
OR/MS subject classification: Primary: Finance; secondary: Investment
History:
1. Introduction Trading strategies can be classified into three categories: i) buy and hold;
ii) contra-trend, and iii) trend following. The buy-and-hold strategy is desirable when the average
stock return is higher than the risk-free interest rate. Recently Shiryaev et al. [16] provided a
theoretical justification of the buy and hold strategy from the angle of maximizing the expected
relative error between the stock selling price and the aforementioned maximum price. The contra-
trend strategy, on the other hand, focuses on taking advantages of mean reversion type of market
behaviors. A contra-trend trader purchases a stock when its price falls to some low level and bets
an eventual rebound. The trend following strategy tries to capture market trends. In contrast to
the contra-trend investors, a trend following believer often purchases shares when prices advance
to a certain level and closes the position at the first sign of upcoming bear market.
There is an extensive literature devoted to contra-trend strategies. For instance, Merton [14]
pioneeredthecontinuous-timeportfolioselectionwithutilitymaximization,whichwassubsequently
extended to incorporate transaction costs by Magil and Constantinidies [13] (see also Davis and
Norman [6], Shreve and Soner [17], Liu and Loeweinstein [12], Dai and Yi [4], and references
therein). Assuming that there is no leverage or short-selling, the resulting strategies turn out to
be contra-trend because the investor is risk averse and the stock market is assumed to follow a
geometric Brownian motion with constant drift and volatility. Recently Zhang and Zhang [21]
showed that the optimal trading strategy in a mean reverting market is also contra-trend. Other
1
Electronic copy available at: https://ssrn.com/abstract=1630903
Electronic copy available at: http://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
2 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
work relevant to the contra-trend strategy includes Dai et al. [2], Song et al. [18], Zervors et al.
[20], among others.
This paper is concernedwith a trend following trading rule. In practice, a trend following trader
often uses moving averages to determine the general direction of the market and generate trading
signals. Related research along the line of statistical analysis in connection with moving averages
canbefoundin,forexample,Faber[7] amongothers.Nevertheless,rigorousmathematicalanalysis
is absent. Recently, Dai et al. [5] provided a theoretical justification of the trend following strat-
egy in a bull-bear switching market and employed the conditional probability in the bull market
to generate trade signals. However, the work imposed a less realistic assumption widely used in
existing literature (e.g. [18], [20], and [21]): only one share of stock is allowed to be traded, so the
resulting wealth process is not self-financing. It is important to address how relevant the trading
rule is to practice. It is the purpose of this paper to deal with more realistic self-financing trad-
ing strategies. Here we adopt an objective function emphasizing the percentage gains. As a result
the corresponding payoff has to account for the gain/loss percentage of each trade, which is also
desirable in actualtrading. On the other hand, these more realistic considerations make the model
more technically involved than in the ‘single share’ transaction considered in Dai et al. [5].
Most existing literature in trading strategies assumes that the investor can observe full market
information (e.g. Jang et al. [8] and Dai et al. [3]). In contrast, we follow Dai et al. [5] to model
the trends in the markets using a geometric Brownian motion with regime switching and partial
information. More precisely, two regimes are considered:the uptrend (bull market) and downtrend
(bear market), and the switching process is modeled as a two-state Markov chain which is not
directly observable. We consider a finite horizon investment problem and aim to maximize the
percentage gains. We assume that the investor trades all available funds in the form of either “all-
in” (long) or “all-out” (flat). That is, when buying, one fills the position with the entire account
balance and when selling, one closes the entire position. We will show again that the optimal
trading strategy is a trend following system characterized by the conditional probability over time
and its up and down crossings of two threshold curves. These thresholds can be obtained through
solving a system of associated HJB equations. Such a trading strategy naturally generates entry
time and exit time which can be mathematically described by stopping times. We also carry out
numerical simulations and market tests to demonstrate how the method works.
This work and Dai et al. [5] were initialized by an attempt to justify the technical analysis with
moving average. A moving average trading strategy is generally in “all in - all out” form but is
difficult to justify theoretically. This motivates us to design and justify an alternative “all in -
all out” strategy that is analogous to the moving average trading strategy. This work has been
recently extended to the Merton’s portfolio optimization problem by Chen et al. [1], where the
investor may choose an optimal fraction of wealth invested in stock.
In contrast to [5], the present paper provides not only a more reasonable modeling but also a
more thorough theoretical analysis. First, we remove a technical condition imposed in [5] when
proving the verification theorem. The key step is to show that the optimal trading strategy incurs
only a finite number of trades almost surely (Lemma 2). Second,since the solution to the resulting
HJBequationisnotsmoothenoughtousetheItˆolemma,weemployanapproximationapproachto
prove the verification theorem (Theorem 4). Third, we show that for the optimal trading strategy,
the upper limit involved in defining the reward function is, in fact, a limit (Theorem 5). Hence,
the definition of the reward function makes sense in practice. Last but not least, we find that
the theoretical characterization on the optimal trading strategy obtained in [5] remains valid for
the present model (Theorem 1). We further present sufficient conditions to examine whether or
not the optimal trading boundaries are attainable (Theorem 2 and Theorem 3). In spite that
these conditions are not sharp, our result reveals that under certain scenario, the optimal trading
boundaries are always attainable for sufficiently small transaction costs.
Electronic copy available at: https://ssrn.com/abstract=1630903
Electronic copy available at: http://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 3
The rest of the paper is arranged as follows. Following the problem formulation in the next
section, Section 3 is devoted to a theoretical characterization of the optimal trading strategy in
a regime switching market. We report our simulation results and market tests in Section 4. We
conclude in Section 5. Some technical proofs are given in Appendix.
2. Problem Formulation Consider a complete probability space (Ω,F,P). Let S denote
r
the stock price at time r satisfying the equation
dS =S [µ(α )dr+σdB ], S =S, t≤r≤T <∞,
r r r r t
where α ∈{1,2} is a two-state Markov chain, µ(i) ≡ µ is the expected return rate in regime
r i
i=1,2, σ>0 is the constant volatility, B is a standard Brownian motion, and t and T are the
r
initial and terminal times, respectively. We assume that the stock does not pay any dividends. No
generality is lost because dividends, if exist, can be re-invested in the stock and, thus, reflected in
the stock price.
The process α represents the market mode at each time r: α = 1 indicates a bull market
r r
(uptrend) and α =2 a bear market (downtrend). In this paper, we make a realistic assumption
r
−λ λ
that α is not directly observable. Let Q= 1 1 , (λ >0, λ >0), denote the generator of
r λ −λ 1 2
2 2
(cid:18) (cid:19)
α . So, λ (λ ) stands for the switching intensity from bull to bear (from bear to bull). We assume
r 1 2
that {α } and {B } are independent.
r r
Due to the non-observability of α , the decisions (of buying and selling) have to base purely on
r
the stock prices. Let F =σ{S : r≤t} denote the σ-algebra generated by the stock price. Let
t r
t≤τ0≤v0≤τ0≤v0···≤τ0≤v0 ≤··· , a.s.,
1 1 2 2 n n
denote a sequence of F -stopping times. For each n, define
t
τ =min{τ0,T} and v =min{v0,T}.
n n n n
A buying decision is made at τ if τ <T and a selling decision is at v if v <T, n=1,2,.... In
n n n n
addition, we require the liquidation of all long positions (if any) at the terminal time T.
We assume that the investor is taking an “all in - all out” strategy. This means that she is
either long so that her entire wealth is invested in the stock or flat so that all of her wealth is
in a bank account that draws the riskfree interest rate. We use indicator i= 0 or 1 to signify
the initial position to be flat or long, respectively. If initially the position is long (i.e, i=1), the
correspondingsequence of stopping times is denotedby Λ =(v ,τ ,v ,τ ,...). Likewise, if initially
1 1 2 2 3
the net position is flat (i=0), then the corresponding sequence of stopping times is denoted by
Λ =(τ ,v ,τ ,v ,...).
0 1 1 2 2
Let 0<K <1 denote the percentage of slippage (or commission) per transaction with a buying
b
order and 0<K <1 that with a selling order.
s
Let ρ≥0 denote the risk-free interest rate. Given the initial time t, initial stock price S =S,
t
initial market trend α =α, and initial net position i=0,1, the reward functions of the decision
t
sequences, Λ and Λ , are the expected return rates of wealth:
0 1
J (S,α,t,Λ )
i i
∞ I {τn<T}
S 1−K
E log eρ(τ1−t) eρ(τn+1−vn) vn s , if i=0,
 t  S 1+K 
 
(
n Y =1
τn" b# )
=     E log  S v1eρ(τ2−v1)(1−K ) ∞ eρ(τn+1−vn) S vn  1−K s I {τn<T} ,
 t s
 S S 1+K 
( " #
n=2
τn" b# )
Y
    if i=1,



where I A repr   esents the indicator function of A.
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
4 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
Remark 1. Note that different from the reward functions in [5], the above reward functions
account for percentage gain/loss of each trade. Between trades, the entire balance is in a risk-free
asset drawing interests at rate ρ. We only consider the control problem in the finite time horizon
[0,T]. This is signified by involving the indicator function I in the payoff function J . The
{τn<T} i
meaningof thisindicatorfunctionis thatabuyingorderatstoppingtimeτ will beaccountedonly
n
when τ <T. If a long position remains at t=T, then it has to be sold at that time. Transactions
n
at t>T will not affect the payoff J .
i
It is clear that
J (S,α,t,Λ )
i i
∞
S 1−K
E ρ(τ −t)+ log vn +ρ(τ −v )+log s I , if i=0,
t 1 S n+1 n 1+K {τn<T}
 ( n=1 " τn (cid:18) b(cid:19) #)
 X
=    E log S v1 +log(1−K )+ρ(τ −v )
  t S s 2 1
  (" #

∞
S 1−K
+ log
vn
+ρ(τ −v )+log
s
I , if i=1,
  S n+1 n 1+K {τn<T}
    X n=2 " τn (cid:18) b(cid:19) #)

  ∞

N
where the term E ξ for random variables ξ is interpreted as limsup E ξ .
t n n N→∞ t n=1 n
n=1
Remark 2. WeXwill show in Section 3 that the optimal strategy can be givenPin terms of the
conditional probability in a bull market and two threshold levels. A buying (selling) decision is
triggeredwhen the conditionalprobability in a bull market crosses these thresholds.Moreover, the
optimal strategy involves only a finite number of trades (see Lemma 2).
It is easy to see that one should never buy a stock if the riskfree rate is greater than the log-
return rate of stock in the bull market, i.e. ρ≥µ
−σ2
, and never sell the stock if the riskfree rate
1 2
is lower than the log-return rate of stock in the bear market, i.e., ρ≤µ −
σ2
. To exclude these
2 2
trivial cases, we assume
σ2 σ2
µ − <ρ<µ − . (1)
2 2 1 2
Note that the market trend α is not directly observable. Thus, it is necessary to convert the
r
problem into one that is observable. One way to accomplish this is to use the Wonham filter [19].
Let p =P(α =1|S ) denote the conditional probability in a bull market (α =1) given the
r r r r
filtrationS =σ{S : 0≤u≤r}.Thenwecanshow(seeWonham[19])thatp satisfiesthefollowing
r u r
stochastic differential equation
(µ −µ )p (1−p )
dp =[−(λ +λ )p +λ ]dr+ 1 2 r r dB , (2)
r 1 2 r 2 σ r
where B is the innovation process (a standard Brownian motion; see e.gb., Øksendal [15]) given by
r
dlog(S )−[(µ −µ )p +µ −σ2/2]dr
b dB = r 1 2 r 2 . (3)
r
σ
It is easy to see that S canbbe written in terms of B :
r r
dS =S [(µ −µ )p +µ ]dr+S σdB . (4)
r r 1 2 r b2 r r
In view of this, the separation principle holds for the partially observed optimization problem.
b
The problem is to choose Λ to maximize the discounted return J subject to (2) and (4). We
i i
emphasize that this new problem is completely observable because p , the conditional probability
r
in a bull market, can be obtained by using the stock price up to time r.
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 5
Note that the reward function J only accounts for the percentage gain/loss. For any given τ
i n
and v , we have
n
S vn vn
log
vn
= f(p )dr+ σdB , (5)
r r
S
τn Zτn Zτn
where b
σ2
f(p )=(µ −µ )p +µ − . (6)
r 1 2 r 2 2
Note also that
vn
E σdB =0. (7)
t r
Zτn
Therefore, the reward function J is independent obf the initial stock price S. Consequently, given
i
p =p, we can rewrite the reward function as
t
J =J (p,t,Λ ).
i i i
For i=0,1, let V (p,t) denote the value function with the state p at time t. That is,
i
V (p,t)=supJ (p,t,Λ ). (8)
i i i
Λi
The following lemma gives the bounds of the value functions.
Lemma 1. Let V (p,t), i=1,2 be the value functions defined in (8). We have
i
σ2
ρ(T −t)≤V (p,t)≤ µ − (T −t)
0 1 2
(cid:18) (cid:19)
and
σ2
log(1−K )+ρ(T −t)≤V (p,t)≤log(1−K )+ µ − (T −t).
s 1 s 1 2
(cid:18) (cid:19)
Proof. It is clear that the lower boundsfor V follow fromtheir definition.It remains to estimate
i
their upper bounds. Using (5) and (7) and noticing 0≤p ≤1, we have
r
S vn
E log
vn
= E f(p )dr
t t r
S
(cid:18) τn(cid:19) (cid:20)Zτn σ2 vn (cid:21) σ2
≤ µ − dr= µ − (v −τ ).
1 2 1 2 n n
(cid:18) (cid:19)Zτn (cid:18) (cid:19)
Note that log(1−K )<0 and log(1+K )>0. It follows that
s b
∞ σ2
J (p,t,Λ ) ≤ E ρ(τ −t)+ µ − (v −τ )+ρ(τ −v )
0 0 t 1 1 2 n n n+1 n
( )
n=1(cid:20)(cid:18) (cid:19) (cid:21)
σ2X σ2
≤ max ρ,µ − (T −t)= µ − (T −t),
1 2 1 2
(cid:26) (cid:27) (cid:18) (cid:19)
where the last equality is due to (1). We then obtain the desired result. An upper bound for V
1
can be established similarly. (cid:3)
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
6 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
Next, we consider the associated Hamilton-Jacobi-Bellman equations. Using the dynamic pro-
gramming principle, one has
V (p,t)=supE {ρ(τ −t)−log(1+K )+V (p ,τ )}
0 t 1 b 1 τ1 1
τ1≥t
and
v1
V (p,t)=supE f(p )ds+log(1−K )+V (p ,v ) ,
1 t s s 0 v1 1
v1≥t (cid:26)Zt (cid:27)
where f(·) is as given in (6). Let
2
1 (µ −µ )p(1−p)
L=∂ + 1 2 ∂ +[−(λ +λ )p+λ ]∂
t 2 σ pp 1 2 2 p
(cid:18) (cid:19)
denote the generator of (t,p ). Then, the associated HJB equations are
t
min{−LV −ρ,V −V +log(1+K )}=0,
0 0 1 b (9)
min{−LV −f(p),V −V −log(1−K )}=0,
1 1 0 s
(cid:26)
with the terminal conditions
V (p,T)=0,
0 (10)
V (p,T)=log(1−K ).
1 s
(cid:26)
Using the same technique as in Dai et al. [5], we can show that Problem (9)-(10) has a unique
boundedstrongsolution(V ,V ),whereV ∈W2,1([ε,1−ε]×[0,T]),foranyε∈(0,1/2),q∈[1,+∞).
0 1 i q
It should be pointed out that the differential operator L is degenerate at p=0,1 and the solution
is only locally bounded in W2,1.
q
Remark 3. In thispaper,we restrictthestatespaceof p to(0,1)becausebothp=0 andp=1
are entranceboundaries(see Karlin and Taylor [9] and Dai et al. [5] for definition and discussions).
Now we define the buy region (BR), the sell region (SR), and the no-trading region (NT) as
follows:
BR = {(p,t)∈(0,1)×[0,T):V (p,t)−V (p,t)=log(1+K )},
1 0 b
SR = {(p,t)∈(0,1)×[0,T):V (p,t)−V (p,t)=log(1−K )},
1 0 s
NT = (0,1)×[0,T)(cid:31)(BR∪SR).
To study the optimal strategy, we only need to characterize these regions.
3. Main results In this section, we present the main theoretical results.
3.1. Characterization of the optimal trading strategy Let
ρ−µ +σ2/2 1+K
p = 2 , a=log b. (11)
0 µ −µ 1−K
1 2 s
Theorem 1. There exist two monotonically increasing boundaries p∗(t), p∗(t): [0,T)→[0,1]
s b
such that
SR = {(p,t)∈(0,1)×[0,T):p≤p∗(t)}, (12)
s
BR = {(p,t)∈(0,1)×[0,T):p≥p∗(t)}. (13)
b
Moreover,
i) p∗(t)≥p ≥p∗(t) for all t∈[0,T);
b 0 s
ii) lim p∗(t)=p ;
s 0
t→T−
a
iii) there is a δ> such that p∗(t)=1 for t∈(T −δ,T);
µ −ρ−σ2/2 b
1
iv) p∗(t), p∗(t)∈C∞ if p∗(t),p∗(t)∈(0,1).
s b s b
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 7
Figure1. Optimal buy and sell boundaries
1
0.95
0.9
0.85
0.8
0.75
0.70 0.2 0.4 0.6 0.8 1
t
p
BR
p∗b(t)
NT
p∗s(t)
SR
Parameter values: λ =0.36, λ =2.53, µ =0.18, µ =−0.77, σ=0.184, K =K =0.001, ρ=
1 2 1 2 b s
0.0679, T =1.
Proof. Denote Z(p,t)≡V (p,t)−V (p,t). Similar to Lemma 2.2 in [5], we can show that Z(p,t)
1 0
satisfies the following double obstacle problem:
min{max{−LZ−f(p)+ρ,Z−log(1+K )},Z−log(1−K )}=0, (14)
b s
in (0,1)×[0,T), with the terminal condition Z(p,T)=log(1−K ), and
s
−LV =ρ+(−LZ−f(p)+ρ)−=ρI +f(p)I ,
0 {Z<log(1+Kb)} {Z=log(1+Kb)}
(15)
(V
0
(p,T)=0,
−LV =f(p)+(−LZ−f(p)+ρ)+=f(p)I +ρI ,
1 {Z>log(1−Ks)} {Z=log(1−Ks)}
(16)
(V
1
(p,T)=log(1−K
s
).
Then we can use the same argument as in the proof of Theorem 2.5 in [5] to obtain the desired
results. (cid:3)
We call p∗(t) (p∗(t)) the optimal sell (buy) boundary. To see better how Theorem 1 works, we
s b
provide a numericalresult for illustration.In Figure 1, we plot the optimalsell and buyboundaries
againsttime,wheretheparametervaluesusedareλ =0.36, λ =2.53, µ =0.18, µ =−0.77, σ=
1 2 1 2
0.184, K =K =0.001, ρ=0.0679, and T =1. It can be seen that p∗(t) and p∗(t) are almost flat
b s s b
except when t is close to T where they sharply increase with t. Moreover, the sell boundary p∗(t)
s
approaches the theoretical value
ρ−µ +σ2/2 0.0679+0.77+0.1842/2
p = 2 = =0.9,
0 µ −µ 0.18+0.77
1 2
as t→T =1.Betweenthetwo boundariesis theNT, abovethebuyboundaryis theBR, andbelow
the sell boundary is the SR. Also, we observe that there is a δ such that p∗(t)=1 for t∈[T −δ,T],
b
which indicates that it is never optimal to buy stock when t is very close to T. Using Theorem 1,
the lower bound of δ is estimated as
a log(1.001/0.999)
= =0.021,
µ −ρ−σ2/2 0.18−0.0657−0.1842/2
1
which is consistent with the numerical result.
Thebehaviorofthethresholdsp∗(·)andp∗(·)whentapproachesT isduetoourtechnicalrequire-
s b
ment of liquidating all the positions at T. Interested in long-term investment, we will approximate
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
8 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
these thresholds, as in [5], by constants p∗= lim p∗(t) and p∗= lim p∗(t). Assuming that the
s s b b
T−t→∞ T−t→∞
initial positionis flatandtheinitial conditionalprobabilityp(0)∈(p∗,p∗),ourtradingstrategycan
s b
be described as follows: as p goes up to hit p∗, we take a long position, that is, investing all the
t b
wealth in the stock. We will close out the position only when p goes down and hits p∗. According
t s
to (2)-(3), we have
(µ −µ )p (1−p )
dp =g(p )dr+ 1 2 r r dlogS , (17)
r r σ2 r
where
(µ −µ )p (1−p )((µ −µ )p+µ −σ2/2)
g(p)=−(λ +λ )p+λ − 1 2 t t 1 2 2 .
1 2 2 σ2
Relation (17) implies that p , the conditional probability in the bull market, increases (decreases)
t
as the stock price goes up (down). Hence, our optimal trading strategy buys while the stock price
is going up and sells when the stock price declines. In other words, it is trend-following in nature.
We have seen from Proposition 1 that both the buy and sell boundaries are increasing with time
and that the buy (sell) boundary boundary is bounded from below (above) by p . Note that p=0
0
and p=1 are entrance boundaries that cannot be reached from the interior of the state space (see
Remark 2 in Dai et al. [5]). A natural question is whether or not the sell (buy) boundary can
coincide with p=0 (p=1). The following theorem provides an affirmative answer and sufficient
conditions.
Theorem 2. Let p and a be given as in (11).
0
i) If
1 λ
p <min , 2 (18)
0 3 6(λ +λ )
(cid:26) 1 2 (cid:27)
and
p p
0 ≤a≤ 0 , (19)
λ2 − λ1+λ2 9(µ1−µ2) + 2+6λ1
12(µ1−µ2)p0 2(µ1−µ2) σ2 µ1−µ2
then
1 12p
p∗(t)≡0, ∀t≤T − − 0.
s p λ
0 2
ii) If λ >λ and
1 2
1 λ −λ σ2(λ +λ ) σ2(1−p )
p ≥1−min , 1 2 , 1 2 , a≥ 0 , (20)
0 3 6(λ +λ ) 18(µ −µ )2 µ −µ
(cid:20) 1 2 1 2 (cid:21) 1 2
then
p∗(t)≡1, ∀t<T.
b
TheproofofTheorem2reliesonatechnicalpartialdifferentequationapproachandispostponed
to Appendix.
Figure 2 below illustrates situations where the parameter values do satisfy the conditions in
Theorem 2. In Figure 2(a), the sell boundary coincides with the entrance boundary p=0 before
t=0.98. Hence, one should never sell stock except when t is very close to 1. In Figure 2(b), the
buy boundary remains at the entrance boundary p=1, which means that one should never buy
any stock.
Nowwepresentasufficientconditiontoensurethatboththesellboundaryandthebuyboundary
are attainable when t is not close to the terminal time T.
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 9
Figure2. Scenarios of p∗ s(t)=0, p∗
b
(t)≡1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
−0.1
0 0.2 0.4 0.6 0.8 1
t
p
1.05
1
p∗ b(t)
0.95
0.9
p∗ s(t)
0.85
0 0.2 0.4 0.6 0.8 1
t
p
p∗ b(t)
p∗ s(t)
(a) (b)
Parameter values. Case (a): λ =0.2, λ =30, µ =0.15, µ =0.1, σ=0.2, K =K =0.0006, ρ=
1 2 1 2 b s
0.085, T =1;Case(b):λ =20, λ =1, µ =0.2, µ =0, σ=0.45, K =K =0.05, ρ=0.08, T =1.
1 2 1 2 b s
Theorem 3. Let p and a be as given in (11). If p < 1 and
0 0 3
p p
a≤min 0 , 0 , (21)
( 9(µ1−µ2) + 2+6λ1 8(µ1−µ2) + 16λ2 )
σ2 µ1−µ2 σ2 (µ1−µ2)p0
then
1
p∗(t)>0, p∗(t)<1, ∀t≤T − .
s b p
0
Again we postpone the technical proof to Appendix.
TheconditionsinTheorem3isnotsharp.However,condition(21)alwaysholdsifthetransaction
costs are sufficiently small. We also emphasize that the conditions presented in Theorem 3 are
sufficientbutnotnecessary.Infact,ournumericaltestsrevealthatforreasonableparametervalues,
the sell and buy boundaries are strictly between (0,1) when t is not close to the terminal time T.
3.2. A verification theorem We now present a verification theorem, indicating that the
solutions V and V of problem (9)-(10) are equal to the value functions and sequences of optimal
0 1
stopping times can be constructed by using (p∗,p∗).
s b
Theorem 4. (Verification Theorem) Let (w (p,t),w (p,t)) be the unique solution to problem
0 1
(9)-(10)andp∗(t)and p∗(t)betheassociated freeboundaries,wherew ∈W2,1([ε,1−ε]×[0,T]), i=
b s i q
0,1, for any ε∈(0,1/2), q∈[1,+∞). Then, w (p,t) and w (p,t) are equal to the value functions
0 1
V (p,t) and V (p,t), respectively.
0 1
Moreover, let
Λ∗=(τ∗,v∗,τ∗,v∗,···),
0 1 1 2 2
where the stopping times τ∗ =T ∧inf{r≥t: p ≥p∗(r)}, v∗ =T ∧inf{r≥τ∗ : p ≤p∗(r)}, and
1 r b n n r s
τ∗ =T ∧inf{r>v∗ : p ≥p∗(r)} for n≥1, and let
n+1 n r b
Λ∗=(v∗,τ∗,v∗,τ∗,···),
1 1 2 2 3
where the stopping times v∗=T ∧inf{r≥t: p ≤p∗(r)}, τ∗=T ∧inf{r>v∗ : p ≥p∗(r)}, and
1 r s n n−1 r b
v∗ =T ∧inf{r≥τ∗: p ≤p∗(r)} for n≥2. Then Λ∗ and Λ∗ are optimal.
n n r s 0 1
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
10 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
Note that in Theorem 4, we removed the technical condition v∗ →T used in [5]. In addition,
n
the solution to problem (9)-(10) is not smooth enough to use the Itˆo lemma. We will employ an
approximationapproachtoovercomethisdifficulty.Notethatonecannotdirectlyutilizetheresults
of Lamberton and Zervos [11] which are for a stationary problem.
BeforeprovingTheorem4,weintroducetwolemmas.Thefirstindicatesthattheoptimaltrading
strategy incurs only a finite number of trades almost surely.
Lemma 2. Let v∗,τ∗ be as given in Theorem 4. Define
n n
N =inf{n:v∗ =T or τ∗ =T} and infØ=+∞.
n n+1
Then there exists a constant C such that
E(N)≤C.
In particular, N(ω) is finite almost surely. In other words, for fixed path, v∗ =τ∗=T when n is
n n
large enough.
Proof. Recalling p∗(r)≥p ≥p∗(r), p∗, p∗∈C∞ (see Theorem 1), and
b 0 s s b
V (r,p∗(r))−V (r,p∗(r))=log(1+K )>log(1−K )=V (r,p∗(r))−V (r,p∗(r)),
1 b 0 b b s 1 s 0 s
we deduce that p∗(r)>p∗(r) and there is a δ>0 such that
b s
p∗(r)−p∗(r)>4δ.
b s
Denote
r r (µ −µ )p (1−p )
P1=p + −(λ +λ )p +λ du−p∗(r), P2= 1 2 u u dB ,
r t 1 2 u 2 s r σ u
Zt
h i
Zt
where P1 is an absolutely continuous stochastic process and P2 is a martingale. Apparbently
P1+P2=p −p∗(r). (22)
r r r s
Since stochastic process p has continuous paths, the definitions of p∗, p∗ imply that
r s b
(P1 −P1 )+(P2 −P2 )=(P1 +P2 )−(P1 +P2 )
τn∗ vn ∗
−1
τn∗ vn ∗
−1
τn∗ τn∗ vn ∗
−1
vn ∗
−1
= (p
τn ∗
−p∗
s
(τ
n
∗))−(p
vn ∗ −1
−p∗
s
(v
n
∗
−1
))
= p∗(τ∗)−p∗(τ∗)>4δ.
b n s n
Hence, we deduce
either P1 −P1 >2δ or P2 −P2 >2δ. (23)
τn∗ vn ∗
−1
τn∗ vn ∗
−1
On the other hand, P1 is clearly bounded since p , p∗(r)∈[0,1]. Owing to (22), we infer that
r s
P2 is bounded as well. Hence, we can choose a positive integer M such that
|P2|≤Mδ.
If P2 −P2 >2δ, then the continuity of P2 implies that the martingale P2 should cross upward
τn ∗ vn ∗
−1
at least one of the intervals [iδ,(i+1)δ](i=−M,−M+1,·,·,·,M −1) during [v∗ ,τ∗].
n−1 n
Hence, by virtue of (23), we deduce that
M−1
N ≤ U (P2)+U (P1), (24)
[iδ,(i+1)δ] 2δ
i=−M
X
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 11
where U (P2) denotes the number of crossing upward the interval [iδ, (i+1)δ] for P2
[iδ,(i+1)δ]
during [0,T ], and U (P1) denotes the number of crossing upward a 2δ-length interval for P1
2δ
during [0,T ]. In view of the inequality for crossing upward, we infer
1 1 C
E(U (P2))≤ E(|P2|)+|iδ| ≤ E(|P2|)+M ≤ , (25)
[iδ,(i+1)δ]
δ δ 4M
(cid:16) (cid:17)
where C is a constant large enough. Since p ∈[0,1] and p∗ is increasing, it is easy to see
r s
C
U (P1)≤ . (26)
2δ
2
The combination of (24), (25), and (26) yields the desired result. (cid:3)
Our next lemma indicates that the solution to problem (9)-(10) has the same bounds as the
value function (see Lemma 1).
Lemma 3. Let (w (p,t),w (p,t)) be the solution to problem (9)-(10). Then
0 1
σ2
ρ(T −t)≤w (p,t)≤ µ − (T −t)
0 1 2
(cid:18) (cid:19)
and
σ2
log(1−K )+ρ(T −t)≤w (p,t)≤log(1−K )+ µ − (T −t).
s 1 s 1 2
(cid:18) (cid:19)
Proof. Clearly
−L(w −ρ(T −t))=−Lw −ρ≥0,
0 0
from which we immediately infer by the maximum principle w ≥ρ(T −t). Owing to w −w −
0 1 0
log(1−K )≥0, we have w ≥log(1−K )+ρ(T −t).
s 1 s
To prove the right hand side inequalities, we utilize (15) and (16) to get
σ2
−Lw ≤ max{ρ,f(p)}≤µ − ,
0 1 2
σ2
−Lw ≤ max{ρ,f(p)}≤µ − .
1 1 2
Again by the maximum principle, the desired result follows. (cid:3)
Now we are ready to prove the verification theorem.
Proof of Theorem 4. First, we show that for any stopping times θ ≥θ ≥t,
2 1
θ2 S
E w (p ,θ )≥E f(p )dr+w (p ,θ ) =E log
θ2
+w (p ,θ ) a.s. (27)
t 1 θ1 1 t r 1 θ2 2 t S 1 θ2 2
(cid:20)Zθ1 (cid:21) (cid:20) θ1 (cid:21)
Since w is only locally bounded in W2,1((0,1)×[0,T]), we cannot directly use the Itˆo formula.
1 q
To overcome the difficulty, we introduce the following stopping times:
β =inf{r≥θ :p ∈(0,1/m)∪(1−1/m,1)}∧θ , m=1,2,···.
m 1 r 2
Note that p=0 and p=1 cannot be reached from the interior of (0,1) (see Remark 2 in [5]). We
then infer that β →θ as m→∞.
m 2
Due to w ∈W2,1([1/m,1−1/m]×[0,T]), applying the Itˆo formula to w (p ,r) in [θ ,β ] yields
1 q 1 r 1 m
(c.f. Krylov [10])
βm βm (µ −µ )p (1−p )
w (p ,θ )=w (p ,β )− Lw (p ,r)dr− ∂ w (p ,r) 1 2 r r dB a.e.
1 θ1 1 1 βm m 1 r p 1 r σ r
Zθ1 Zθ1
b
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
12 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
By the Sobolev embedding theory, ∂ w ∈C([1/m,1−1/m]×[0,T]), which implies that the last
p 1
term in the above equation is a martingale. Taking conditional expectation in the above equation,
we deduce that
βm
E w (p ,θ )=E w (p ,β )− Lw (p ,r)dr . (28)
t 1 θ1 1 t 1 βm m 1 r
(cid:20) Zθ1 (cid:21)
Since w , w ∈W2,1 , we can rewrite
0 1 q,loc
Lw = −f(p)I +L(w +log(1−K ))I
1 {w1>w0+log(1−Ks)} 0 s {w1=w0+log(1−Ks)}
= −f(p)I −ρI .
{w1>w0+log(1−Ks)} {w1=w0+log(1−Ks)}
Hence
T
E |Lw (p ,r)|dr <∞. (29)
1 r
(cid:20)Z0 (cid:21)
Sending m→∞ in (28) and using (29) and Lemma 3, we have by the dominated convergence
theorem
θ2
E w (p ,θ )=E − Lw (p ,r)dr+w (p ,θ ) a.s.
t 1 θ1 1 t 1 r 1 θ2 2
(cid:20) Zθ1 (cid:21)
Using −Lw −f(p)≥0, we then obtain (27). In a similar way we can show
1
E w (p ,θ )≥E [ρ(θ −θ )+w (p ,θ )] a.s. (30)
t 0 θ1 1 t 2 1 0 θ2 2
We next show, for any Λ and k=1,2,...,
1
S
E w (p ,v )≥E ρ(τ −v )+log
vk+1
t 0 vk k t k+1 k S
" τk+1
(31)
+w (p ,v )+(log(1−K )−log(1+K ))I .
0 vk+1 k+1 s b {τk+1<T}
#
In fact, using (27) and (30) and noticing that
w ≥w −log(1+K ) and w ≥w +log(1−K ),
0 1 b 1 0 s
we have
E w (p ,v )
t 0 vk k
≥ E [ρ(τ −v )+w (p ,τ )]
t k+1 k 0 τk+1 k+1
≥ E [ρ(τ −v )+ w (p ,τ )−log(1+K ) I ]
t k+1 k 1 τk+1 k+1 b {τk+1<T}
S
≥ E [ρ(τ −v )+(cid:0) log
vk+1
+w (p ,v )−(cid:1)log(1+K ) I ]
t k+1 k S 1 vk+1 k+1 b {τk+1<T}
(cid:18) τk+1 (cid:19)
S
≥ E [ρ(τ −v )+ log
vk+1
+w (p ,v )+log(1−K )−log(1+K ) I ]
t k+1 k S 0 vk+1 k+1 s b {τk+1<T}
(cid:18) τk+1 (cid:19)
S
= E [ρ(τ −v )+log
vk+1
+w (p ,v )+(log(1−K )−log(1+K ))I ].
t k+1 k S 0 vk+1 k+1 s b {τk+1<T}
τk+1
Note that the above inequalities also work when starting at t in lieu of v , i.e.,
1
S
w (p ,t)≥E ρ(τ −t)+log
v1
+w (p ,v )+(log(1−K )−log(1+K ))I .
0 t t 1 S 0 v1 1 s b {τ1<T}
(cid:20) τ1 (cid:21)
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 13
Use this inequality and iterate (31) with k=1,2,..., and note w ≥0 to obtain
0
w (p,t)≥V (p,t).
0 0
Similarly, we can show that
S S
w (p ,t)≥E log
v1
+w (p ,v ) ≥E log
v1
+w (p ,v )+log(1−K ) .
1 t t S 1 v1 1 t S 0 v1 1 s
(cid:20) t (cid:21) (cid:20) t (cid:21)
Use this and iterate (31) with k=1,2,... as above to obtain
w (p,t)≥V (p,t).
1 1
By Lemma 2, we immediately obtain v∗,τ∗ →T as k →∞. It can be seen that the equalities
k k
hold when τ =τ∗ and v =v∗. This completes the proof. (cid:3)
k k k k
We conclude this section by showing that for the optimal trading strategy, the limsup in the
reward functiondefinedin Section2 is, in fact,a limit. Hence,the definition of the reward function
makes sense in practice.
Theorem 5. The limit of E[Θ(m)] as m tends infinity exists, where
m
Θ(m)= log S vn∗ +ρ(τ∗ −v∗)+log 1−K s I .
S n+1 n 1+K {τn∗<T}
n=1 " τn∗ (cid:18) b(cid:19) #
X
Proof. Lemma 2 implies that for fixed path, τ =v =T for n large enough. So the sum is finite
n n
a.s., and lim Θ(m) exists a.s.
m→∞
Next, we estimate the bound of Θ(m). Similar to the proof of Lemma 1, we can obtain
σ2
Θ(m)≤ µ − (T −t).
1 2
(cid:18) (cid:19)
Using the same argument as in the proof of Lemma 1, we have
m
log
S
vn∗ +ρ(τ∗ −v∗) ≥ µ −
σ2
(T −t).
S n+1 n 2 2
n=1
" τn∗ #
(cid:18) (cid:19)
X
Moreover, it is clear that
m
1−K 1−K
s s
log I ≥log N for any m.
1+K
{τn∗<T}
1+K
n=1 (cid:18) b(cid:19) (cid:18) b(cid:19)
X
Lemma 2 implies that
σ2 1−K
E µ − (T −t)+log s N
2 2 1+K
(cid:20)(cid:18) (cid:19) (cid:18) b(cid:19) (cid:21)
exists. The convergence of E[Θ(m)] follows from the Lebesgue dominated convergence theorem.
(cid:3)
4. Simulation and market tests In this section, we carry out numerical simulations and
backtesting to examine the effectiveness of our trading strategy. To estimate p , the conditional
t
probability in a bull market, we use a discrete version of the stochastic differential equation (17),
for t=0,1,...,N with dt=1/252,
(µ −µ )p (1−p )
p =min max p +g(p )dt+ 1 2 t t log(S /S ),0 ,1 , (32)
t+1 t t σ2 t+1 t
(cid:18) (cid:18) (cid:19) (cid:19)
where the price process S is determinedby the simulated paths or the historicalmarket data. The
t
min and max are added to ensure the discrete approximation p of the conditional probability in
t
the bull market stays in the interval [0,1].
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
14 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
4.1. Simulations ForsimulationweusetheparametersgiveninTable1.Thesenumberswere
used in [5]. The time horizon is 40 years.
λ λ µ µ σ K ρ
1 2 1 2
0.36 2.53 0.18 -0.77 0.184 0.001 0.0679
Table 1. Parameter values
We solve the HJB equations and derive p∗ = 0.796 and p∗ = 0.948. We run the 5000 round
s b
simulationsfor10times.Startingwith$1,themeanofthetotal/annualizedreturnandthestandard
deviation are given in Table 2. The trend following strategy clearly outperforms the buy and hold
in terms of return. Moreover, the trend following strategy has a monthly Sharp ratio of 0.22 while
the return of the buy and hold strategy is lower than the riskfree rate ρ=0.0679.
Trend Following Buy and Hold No. of Trades
Mean 75.76(11.4%) 5.62(4.4%) 41.16
Stdev 2.48 0.39 0.29
Table 2. Statistics of ten 5000-path simulations
Comparing to the simulation results in [5] we only observe a slight improvement in terms of
the ratio of mean return of the trend following strategy to that of the buy and hold strategy.
However, the improvement is not significant enough to distinguish statistically from the results in
[5] despite theoretically the present paper is more solid than [5]. Together with sensitivity tests on
thresholds conducted in [5], this reveals that using the conditional probability in the bull market
as trade signals is rather robust against the change of thresholds. It is analogous to the scenario
when technical analysis is used: the effects of using 200-day moving average and 150-day moving
average as trade signals are likely comparable.
The above simulation results are based on the average outcomes of large numbers of simulated
paths. We now investigate the performance of our strategy with individual sample paths. Table 3
collects simulation results on 10 single paths using buy-sell thresholds p∗=0.795 and p∗ =0.948
s b
with the same data given in Table 1. We can see that the simulation is very sensitive to individual
paths. Nevertheless, on large number of trials our strategy clearly outperforms the buy and hold
strategy statistically.
Notethatthisobservationisconsistentwiththemeasurementofaneffectiveinvestmentstrategy
in marketplace. For example, O’Neil’s CANSLIM works during a period of time does not mean it
works on each stock when applied. How it works is measured based on the overall average when
applied to a group of stocks fitting the prescribed selection criteria.
Trend Following Buy and Hold No. of Trades
67.080 3.2892 36.000
24.804 2.2498 42.000
22.509 0.40591 42.000
1887.8 257.75 33.000
26.059 0.16373 48.000
60.267 1.5325 43.000
34.832 5.7747 42.000
8.6456 0.077789 46.000
128.51 30.293 37.000
224.80 29.807 40.000
Table 3. Ten single-path simulations
4.2. Market tests We now turnto the questionwhetherthetrendfollowing tradingstrategy
presented works in real markets. In view of the path sensitivity discussed in the end of the last
section we conduct our tests using a broad based stock index which reflects the aggregation of
the behaviors of a large number of stocks. While ex-post tests are employed in [5], we conduct
the ex-ante tests for the SP500 index – a broad based index that has a set of accessible historical
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 15
data reasonably long for our tests. Our goal is evaluating whether our theoretically optimal trend
following strategy provides useful guidance in real market.
The historical data for SP500 is available since 1962. We assume that any trading action will
take place at the close of the market and, therefore, will use the SP500 daily closing price for our
test. We define an up trend to be rally at least 20% and a down trend decline at least 20%. For
any giving period of the SP500 historical data, say 5 or 10 years, one can find several up and down
trends.Wecanusethestatisticsofthedurationandtotalappreciation/depreciationofthesetrends
toempiricallycalibratetheparametersµ ,λ ,i=1,2andσ.However,afterquicklyscanningseveral
i i
such periods of data we find that the empirical estimate of these parameters is quite different in
different time periods. The change of the parameters, of course, is not unanticipated. Many social,
economic and technological factors contribute to such a change and make it difficult to precisely
predict. However, these exogenous impacts on the parameters happen over time. Thus, we make
the following working assumptions: (a) the parameters gradually change over a long time horizon
(say 10 years) yet they are relatively stable in a short time horizon (say 1 year) and (b) recent
data is more relevant compared to the data in the distant past. Base on these assumptions we
determine the parameters by beginning with the statistical estimate of the 10 year data from 1962
to 1972 as follows: µ and λ are estimated as the average of annualized return and reciprocal of
1 1
the length of the up trends and µ and λ are the average of annualized return and reciprocal of
2 2
the length of the down trends. We conduct the trend following strategy using these parameters
and the corresponding thresholds in the following year and then update the parameters and the
correspondingthresholds at the beginning of a new year using the new data that become available
if a new up or down trend is completed.To reflectassumption (b),we updatetheparametersusing
the so called exponential average method in which the update of the parameters is determined by
the old parameters and new parameters with formula
update=(1−2/N)old+(2/N)new,
where we chose N = 6 based on the number of up and down trends between 1962–1972. The
exponentialaverageallowsustooverweighttherecentinformationwhileavoidingunwantedabrupt
changes due to dropping old information. Then we use the yearly updated parameters to calculate
the corresponding thresholds. Finally, we use these parameters and thresholds to test the SP500
index from 1972-2011. The equity curve of the trend following strategy is compared to the buy
and hold strategy in the same period of time in Figure 3. The upper, middle and the lower curves
represent the equity curves of the trend following strategy, the buy and hold strategy including
dividend, and the SP500 index without dividend adjustment, respectively.
As we can see, the trend following strategy not only outperforms the buy and hold strategy in
total return, but also has a smoother equity curve, which means a higher Sharpe ratio; see Table
4.
Index(time frame) TF TF Sharpe BH BH Sharpe 10 year bonds
SP500 (1972-2011) 11.03% 0.217 9.8% 0.128 6.79%
Table 4. Testing results for trend following trading strategies
The test result for SP500 here is, if not better, at least comparable to the ex-pose test in [5]
showing that trends indeed exist in the price movement of SP500. It is worthwhile pointing out
that in [5], there is a mistake that the dividends are not treated as reinvestment. As a correction,
the returns of the buy and hold strategy and the trend following strategy in [5] (Table 10) should
be respectively 54.6 and 70.9, instead of 33.5 and 64.98, for SP500 (1962-2008).
We note that although an index such as the SP500 reflects the aggregation of the behavior
of many individual stocks, trading it with the trend following strategy could still experience an
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
16 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
103
102
1975 1980 1985 1990 1995 2000 2005 2010
Figure3. Trend following trading of SP500 1972–2011 compared with buyand hold
instability as observed in the end of last section. Using the trend following strategysimultaneously
onalargenumberofstocksshouldsmoothoutthefluctuationoftheperformanceandachievebetter
stability. In spite that such tests belong to the area of developing proprietary trading strategies
and do not fall in the scope of this paper, the testing methods used here are relevant and useful.
5. Conclusion We have considereda finitehorizoninvestment problemin a bull-bear switch-
ingmarket,wherethedriftofthestockpriceswitchesbetweentwo parameterscorrespondingtoan
uptrend(bullmarket) anda downtrend(bearmarket) accordingtoan unobservableMarkovchain.
The goal is to maximize the expected log-utility of the terminal wealth. We restricted attention to
allowing flat and long positions only and used a sequence of stopping times to indicate the time
of entering and exiting long positions. We have shown that the optimal trading strategy is trend
following, characterized by the conditional probability in the uptrend crossing the buy and sell
boundaries.
Regarding futureresearch,it would be interestingto see how the approach works in models with
more than two states, e.g., (bull, bear, sideways markets). In addition, substantial empirical tests
on much broader selections of stocks will be useful to reveal when the trend following method
works and when it fails in the marketplace.
Appendix. Proofs of Theorems 2 and 3.
Proof of Theorem 2. i) First we prove
Z(p,t)≡log(1+K ), ∀p≥3p , 0≤t≤T −1/p . (33)
b 0 0
Let us construct a function:
−a[(p−2p )(T −t)−1]2+log(1+K ), 2p ≤p≤min{2p + 1 ,1};
0 b 0 0 T−t
Z =
1
(log(1+K
b
), min{2p
0
+
T
1
−t
,1}<p≤1.
We claim that Z is a subsolution of (14) in (2p ,1)×(T −1/p ,T). Indeed,
1 0 0
1 1 1
Z 2p + ,t =log(1+K ), ∂ Z 2p + ,t =0, ∀2p + ≤1.
1 0 T −t b p 1 0 T −t 0 T −t
(cid:18) (cid:19) (cid:18) (cid:19)
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 17
So, Z ∈W2,1((2p ,1)×(0,T)). Moreover, for 2p ≤p≤min{2p + 1 ,1} and T −1/p ≤t≤T,
1 q 0 0 0 T−t 0
we have
a(µ −µ )2p2(1−p)2(T −t)2
−LZ = −2a(p−2p )[(p−2p )(T −t)−1]+ 1 2
1 0 0 σ2
−2aλ p(T −t)[(p−2p )(T −t)−1]+2aλ (T −t)[(p−2p )(T −t)−1](1−p)
1 0 2 0
a(µ −µ )2[(p−2p )2+4p (p−2p )+4p2)](1−p)2(T −t)2
≤ 2a+ 1 2 0 0 0 0
σ2
+2aλ [(p−2p )+2p ](T −t)[1−(p−2p )(T −t)],
1 0 0 0
where the inequality is due to 0≤p−2p ≤1 and −1≤(p−2p )(T −t)−1≤ 1 (T −t)−1≤0.
0 0 T−t
Noticing that 0≤1−p≤1, 0≤(p−2p )(T −t)≤1,and0≤p (T −t)≤1, we then deduce
0 0
a(µ −µ )2(1+4+4)
−LZ ≤ 2a+ 1 2 +2aλ (1+2)
1 σ2 1
9(µ −µ )2
= 2+ 1 2 +6λ a
σ2 1
(cid:20) (cid:21)
≤ (µ −µ )p ,
1 2 0
where the last inequality is due to the right hand side condition in (19). It is clear that for any
min{2p + 1 ,1}≤p≤1, we have
0 T−t
−LZ =−L(log(1+K ))=0≤(µ −µ )p .
1 b 1 2 0
On the other hand, in the domain M,{(p,t)∈[2p ,1)×[T −1/p ,T]:Z(p,t)<log(1+K )}, one
0 0 b
has
−LZ≥f(p)−ρ≥f(2p )−ρ=(µ −µ )p ≥−LZ .
0 1 2 0 1
Apparently,
Z (2p ,t)=log(1−K )≤Z(2p ,t), Z (p,T)=log(1−K )≤Z(p,T).
1 0 s 0 1 s
Using the maximum principle in the domain M, we infer Z ≥Z in [2p ,1)×[T −1/p ,T ]. In
1 0 0
particular,
Z(3p ,T −1/p )≥Z (3p ,T −1/p )=log(1+K ).
0 0 1 0 0 b
It is not hard to show that Z(p,t) is decreasing with respect to t and increasing with respect to p.
We then obtain (33).
Consider another function:
a λ 1
Z=log(1−K )+ p−3p + 2 T − −t inN,
s 6p 0 2 p
0 (cid:20) (cid:18) 0 (cid:19)(cid:21)
∆
where N =(0,3p )×(T −1/p −12p /λ ,T −1/p ). We now show that Z is a subsolution of (14)
0 0 0 2 0
in N. It is easy to verify
∂ Z<0, ∂ Z>0, Z(3p ,T −1/p −12p /λ )=log(1+K ), Z<log(1+K )inN.
t p 0 0 0 2 b b
Moreover,
a λ a λ
−LZ= (λ +λ )p− 2 ≤ 3(λ +λ )p − 2 .
6p 1 2 2 6p 1 2 0 2
0 (cid:20) (cid:21) 0 (cid:20) (cid:21)
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
18 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
In the domain {(p,t)∈N :Z(p,t)<log(1+K )},
b
a λ
−LZ≥f(p)−ρ≥−(µ −µ )p ≥ 3(λ +λ )p − 2 ≥−LZ,
1 2 0 6p 1 2 0 2
0 (cid:20) (cid:21)
where the third inequality is due to (18) and the left hand side condition in (19). It is clear that
Z(p,T −1/p )≤Z(3p ,T −1/p )=log(1−K )≤Z(p,T −1/p ), ∀p∈(0,3p ],
0 0 0 s 0 0
Z(3p ,t)≤log(1+K )=Z(3p ,t), ∀t∈(T −1/p −12p /λ ,T −1/p ).
0 b 0 0 0 2 0
Again using the maximum principle, we deduce Z≤Z in the domain N. In particular,
Z(p,t) ≥ Z(p,T −1/p −12p /λ )≥Z(p,T −1/p −12p /λ )
0 0 2 0 0 2
> Z(0,T −1/p −12p /λ )>log(1−K ), ∀p>0,t≤T −1/p −12p /λ ,
0 0 2 s 0 0 2
which yields the desired result.
ii) From (20), we infer
λ +λ
p ≥2/3, (λ +λ )(3p −2)−λ ≥ 1 2;
0 1 2 0 2 2
4(µ −µ )2(1−p ) (λ +λ ) σ2(λ +λ )
1 2 0 ≤ 1 2 , 1 2 ≥(µ −µ )(1−p ).
σ2 2 18(µ −µ ) 1 2 0
1 2
Construct the following function:
log(1−K ), 0≤p<3p −2,
s 0
Z(p,t)=
(log(1−K )+
σ2[p−(3p0−2)]2
, 3p −2≤p≤1.
s 9(µ1−µ2)(1−p0) 0
It is easy to see that Z ≥log(1−K ) and Z ∈W2,1((0,1)×[0,T))∩C((0,1)×[0,T]), for any
s q
q≥1. For 0<p<3p −2, we have
0
−LZ=−L(log(1−K ))=0≥f(3p −2)−ρ≥f(p)−ρ.
s 0
For 3p −2≤p≤2p −1, we find
0 0
σ2 −(µ −µ )2p2(1−p)2
−LZ = 1 2 +2[(λ +λ )p−λ ][p−(3p −2)]
9(µ −µ )(1−p ) σ2 1 2 2 0
1 2 0 (cid:26) (cid:27)
≥ −(µ −µ )(1−p )=f(2p −1)−ρ≥f(p)−ρ.
1 2 0 0
For 2p −1≤p≤1, we have
0
σ2 (µ −µ )24(1−p )2
−LZ ≥ − 1 2 0 +(λ +λ )(1−p )
9(µ −µ )(1−p ) σ2 1 2 0
1 2 0 (cid:20) (cid:21)
σ2 (λ +λ )(1−p )
≥ 1 2 0
9(µ −µ )(1−p ) 2
1 2 0
≥ (µ −µ )(1−p )=f(1)−ρ≥f(p)−ρ.
1 2 0
Hence, Z must be a supersolution of (14). We then deduce that
σ2(1−p )
Z(p,t)≤Z(p,t)<Z(1,t)=log(1−K )+ 0 ≤log(1−K )+a=log(1+K ), ∀p<1,
s s b
µ −µ
1 2
which implies that the buy region does not exist. So, p∗(t)≡1 for all t. (cid:3)
b
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS 19
Proof of Theorem 3. Consider an auxiliary function:
2
log(1−K )+a 4p −1 , p0 ≤p≤ p0,
Z= s p0 4 2
(log(1−K ), (cid:16) (cid:17) 0≤p< p0.
s 4
Clearly Z∈W2,1((0,p /2)×(0,T))∩C([0,p /2]×[0,T]) and
q 0 0
Z≥log(1−K ). (34)
s
It is not hard to verify that for p∈(p /4,p /2), we have
0 0
a −16(µ −µ )2p2(1−p)2
−LZ = 1 2 +8(λ +λ )p(4p−p )−8λ (4p−p )
p2 σ2 1 2 0 2 0
0 (cid:20) (cid:21)
4(µ −µ )2 8λ
≥ − 1 2 + 2 a.
σ2 p
(cid:20) 0 (cid:21)
Using (21), it follows
−LZ≥−(µ −µ )p /2=f(p /2)−ρ≥f(p)−ρ (35)
1 2 0 0
for p∈(p /4,p /2). In the case p∈(0,p /4),
0 0 0
−LZ=−L(log(1−K ))=0≥f(p)−ρ. (36)
s
The combination of (34)-(36) yields
min −LZ−f(p)+ρ,Z−log(1−K ) ≥0
s
(cid:8) (cid:9)
in p∈(0,p /2), t∈[0,T). Moreover, it is clear that
0
Z(p,T)≥log(1−K )=Z(p,T), Z(p /2,t)=log(1+K )≥Z(p /2,t).
s 0 b 0
Thus Z must be a supersolution of (14) in [0,p /2]×[0,T ]. By the maximum principle, we infer
0
Z≥Z in [0,p /2]×[0,T]. Then, for p<p /4, we have
0 0
log(1−K )≤Z≤Z≡log(1−K ),
s s
which implies Z≡log(1−K ) for p<p /4. Note that we can obtain (33) in terms of p <1/3 and
s 0 0
(21). The desired result then follows. (cid:3)
Acknowledgments. Dai is supported by the Singapore MOE AcRF grant (No. R-146-000-
188/138/201-112)andNUS GlobalAsia Institute-LCFFundR-146-000-160-646.Yangis partially
supported by NNSF of China (No. 11271143, 11371155, 11326199), University Special Research
Fund for Ph.D. Program in China (No. 20124407110001). We thank seminar participants at
Carnegie Mellon University, Wayne StateUniversity, and University of Illinois at Chicago for help-
ful comments. Finally, we thank the referees and the editors for their valuable comments and
suggestions, which led to improvements of the paper.
Electronic copy available at: https://ssrn.com/abstract=1630903

Daiet al.: TrendFollowing Trading
20 MathematicsofOperationsResearch00(0),pp.000–000,(cid:13)c 0000INFORMS
References
[1] Chen, Y., M. Dai, L. Goncalves-Pinto. 2013. Portfolio selection with unobservable bull-bear regimes,
Working Paper, National University of Singapore.
[2] Dai,M.,H.Jin,Y.Zhong,X.Y.Zhou.2010.Buylowandsellhigh,Contemporary QuantitativeFinance:
Essays in Honour of Eckhard Platen, C. Chiarella and A. Novikov (Eds.), Springer, 317-334.
[3] Dai,M.,H.F.Wang,Z.Yang.2012.Leveragemanagementinabull-bearswitchingmarket,J.Economic
Dynamics Control 36 1585-1599.
[4] Dai, M., F. Yi. 2009. Finite horizontal optimal investment with transaction costs: a parabolic double
obstacle problem, J. Diff. Equ. 246 1445-1469.
[5] Dai, M., Q. Zhang, Q. Zhu. 2010. Trend following trading under a regime switching model, SIAM J.
Fin. Math. 1 780-810.
[6] Davis, M.H.A., A.R. Norman. 1990. Portfolio selection with transaction costs, Math. Oper. Res 15
676-713.
[7] Faber,M.T.2007.A quantitativeapproachto tacticalassetallocation,J. Wealth Management 9 69-79.
[8] Jang,B.G.,H.K.Koo,H.Liu,M.Loewenstein.2007.Liquiditypremiaandtransactioncosts,J.Finance
62 2329-2366.
[9] Karlin, S., H.M. Taylor. 1981. A Second Course in Stochastic Processes, Academic Press, New York.
[10] Krylov,N.V. 1980. Controlled Diffusion Processes, Springer-Verlag,New York.
[11] Lamberton, D., M. Zervos. 2013. On the optimal stopping of a one-dimensional diffusion, Electron. J.
Probab. 18 1-49.
[12] Liu, H., M. Loeweinstein. 2002. Optimal portfolio selection with transaction costs and finite horizons,
Rev. Financial Studies 15 805-835.
[13] Magill,M.J.P.,G.M.Constantinides.1976.Portfolioselectionwithtransactioncosts,J. Economic The-
ory 13 264-271.
[14] Merton, R.C. 1971.Optimal consumption and portfolio rules in a continuous time model, J. Economic
Theory 3 373-413.
[15] Øksendal, B. 2003. Stochastic Differential Equations, 6th ed. Springer-Verlag,Berlin, New York.
[16] Shiryaev, A., Z. Xu, X. Y. Zhou. 2008. Thou shalt buy and hold, Quantitative Finance 8 765-776.
[17] Shreve, S.E., H.M. Soner. 1994. Optimal investment and consumption with transaction costs, Ann.
Appl. Probab. 4 609-692.
[18] Song, Q.S., G. Yin, Q. Zhang. 2009. Stochastic optimization methods for buying-low and selling-high
strategies, Stoch. Analysis. Appl. 27 523-542.
[19] Wonham, W.M. 1965.Some applications of stochastic differential equations to optimal nonlinear filter-
ing, SIAM J. Control 2 347-369.
[20] Zervos,M.,T.C.Johnsony,F.Alazemi.2013.Buy-lowandsell-highinvestmentstrategies,Math.Finance
23 560-578.
[21] Zhang, H., Q. Zhang. 2008. Trading a mean-reverting asset: Buy low and sell high, Automatica 44
1511-1518.
Electronic copy available at: https://ssrn.com/abstract=1630903
