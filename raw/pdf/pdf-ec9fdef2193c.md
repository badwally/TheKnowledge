---
id: pdf-ec9fdef2193c
type: pdf
title: SSRN-id2585056
url: ''
authors: []
ingested_at: '2026-04-29T16:25:48Z'
content_hash: sha256:f0dc4ccca7593c04e4fa301db4232e5278ec6f806dc8dac6f20d3208b5d55d8c
source_path: raw/pdf/pdf-ec9fdef2193c.pdf
domains:
- trading-and-markets
nlm_corpus_ids:
- ccbda94f-7251-42bb-864f-0e1c9850f7ad
wiki_pages:
- wiki/entities/valeriy-zakamulin.md
- wiki/entities/university-of-agder.md
- wiki/concepts/anatomy-of-moving-average-rules.md
- wiki/concepts/weighted-moving-average-of-price-changes.md
- wiki/concepts/moving-average-types.md
- wiki/concepts/momentum-rule.md
- wiki/concepts/price-minus-moving-average-rule.md
- wiki/concepts/moving-average-change-of-direction-rule.md
- wiki/concepts/double-crossover-method.md
- wiki/concepts/weighting-function-shape-determines-performance.md
meta:
  page_count: 33
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/SSRN-id2585056.pdf
published_at: '2016'
---
Market Timing with Moving Averages: Anatomy
(cid:3)
and Performance of Trading Rules
Valeriy Zakamuliny
First draft: June 2014. This revision: May 29, 2016
Abstract
The underlying concept behind the technical trading indicators based on moving aver-
ages of prices has remained unaltered for more than half of a century. The development
in this (cid:12)eld has consisted in proposing new ad-hoc rules and using more elaborate types of
moving averages in the existing rules, without any deeper analysis of commonalities and
differences between miscellaneous choices for trading rules and moving averages. The (cid:12)rst
contribution of this paper is to uncover the anatomy of market timing rules with moving
averages. Our analysis offers a new and very insightful reinterpretation of the existing
rules and demonstrates that the computation of every trading indicator can equivalently
be interpreted as the computation of a weighted moving average of price changes. There-
fore the performance of any moving average trading rule depends exclusively on the shape
of the weighting function for price changes. The second contribution of this paper is a
straightforward application of the useful knowledge revealed by our analysis. Speci(cid:12)cally,
we evaluate the out-of-sample performance of 300 various shapes of the weighting function
for price changes using historical data on four (cid:12)nancial market indices. The goal of this
exercise is to suggest answers to long-standing questions about optimal types of moving
averages and whether the best performing trading rule can beat the passive counterpart in
out-of-sample tests.
Key words: technical analysis, trading rules, market timing, moving averages, out-of-
sample testing
JEL classi(cid:12)cation: G11, G17.
(cid:3)The author is grateful to Steen Koekebakker, Pete Nikolai, and the participants of the 3rd Economics &
FinanceConference(April2015,Rome,Italy)fortheirinsightfulcommentsonearlierdraftsofthispaper. The
usual disclaimer applies.
ya.k.a. Valeri Zakamouline, School of Business and Law, University of Agder, Service Box 422, 4604 Kris-
tiansand, Norway, Tel.: (+47) 38 14 10 39, E-mail: Valeri.Zakamouline@uia.no
1
Electronic copy available at: https://ssrn.com/abstract=2585056

1 Introduction
Technicalanalysisrepresentsamethodologyofforecastingthefuturepricemovementsthrough
the study of past price data and uncovering some recurrent regularities, or patterns, in price
dynamics. One of the fundamental principles of technical analysis is that prices move in
trends. Analysts (cid:12)rmly believe that these trends can be identi(cid:12)ed in a timely manner and
used to generate pro(cid:12)ts and limit losses. Market timing is an active trading strategy that
implements this idea in practice. Speci(cid:12)cally, this strategy is based on switching between the
market and cash depending on whether the prices trend upward or downward. A moving
average of prices is one of the oldest and most popular tools used in technical analysis for
detecting a trend. Over the past two decades, market timing with moving averages has been
the subject of substantial interest on the part of academics1 and investors alike.
However,despiteaseriesofpublicationsinacademicjournals,themarkettimingrulesbased
on moving averages have remained virtually unaltered for more than half of a century. Modern
technical analysis still remains art rather than science. The situation with market timing is as
follows. There have been proposed many technical trading rules based on moving averages of
prices calculated on a (cid:12)xed size data window. The main examples are: the momentum rule,
the price-minus-moving-average rule, the change-of-direction rule, and the double-crossover
method. In addition, there are several popular types of moving averages: simple (or equally-
weighted) moving average, linearly-weighted moving average, exponentially-weighed moving
average, etc. As a result, there exists a large number of potential combinations of trading rules
with moving average weighting schemes. One of the controversies about market timing is over
which trading rule in combination with which moving average weighting scheme produces the
best performance. The situation is further complicated because in order to compute a moving
average one must de(cid:12)ne the size of the averaging window. Again, there is a big controversy
over the optimal size of this window. The development in this (cid:12)eld has consisted in proposing
new ad-hoc rules and using more elaborate types of moving averages (for example, moving
averagesofmovingaverages)intheexistingruleswithoutanydeeperanalysisofcommonalities
1See, among others, Brock, Lakonishok, and LeBaron (1992), Neely, Weller, and Dittmar (1997), Brown,
Goetzmann, and Kumar (1998), Sullivan, Timmermann, and White (1999), Lo, Mamaysky, and Wang (2000),
Ready(2002),OkunevandWhite(2003),EllisandParbery(2005),Faber(2007),Marshall,Cahan,andCahan
(2008), Fi(cid:12)eld, Power, and Knipe (2008), Zhu and Zhou (2009), Gwilym, Clare, Seaton, and Thomas (2010),
NeuhierlandSchlusche(2011),Moskowitz,Ooi,andPedersen(2012),Metghalchi,Marcucci,andChang(2012),
Kilgallen (2012), Clare, Seaton, Smith, and Thomas (2013), P(cid:127)ata(cid:127)ri and Vilska (2014), and Zakamulin (2014).
2
Electronic copy available at: https://ssrn.com/abstract=2585056

and differences between miscellaneous choices for trading rules and moving average weighting
schemes.
In this paper, we contribute to the literature in two important ways. The (cid:12)rst contribution
of this paper is to uncover the anatomy of market timing rules with moving averages of prices.
Speci(cid:12)cally, we present a methodology for examining how the value of a trading indicator is
computed. Then using this methodology we study the computation of trading indicators in
manymarkettimingrulesandanalyzethecommonalitiesanddifferencesbetweentherules. We
reveal that despite being computed seemingly different at the (cid:12)rst sight, all technical trading
indicators considered in this paper are computed in the same general manner. In particular,
the computation of every technical trading indicator can equivalently be interpreted as the
computation of a weighted moving average of price changes. Consequently, the only real
difference, between diverse market timing rules coupled with various types of moving averages,
lies in the shape of weighting function used to compute the moving average of price changes.
Our methodology of analyzing the computation of trading indicators for the timing rules
based on moving averages offers a broad and clear perspective on the relationship between
different rules. We show, for example, that every trading rule can also be presented as a
weighted average of the momentum rules computed using different averaging periods. Thus,
the momentum rule might be considered as an elementary trading rule on the basis of which
one can construct more elaborate rules. In addition, we establish a one-to-one equivalence
between a price-minus-moving-average rule and a corresponding moving-average-change-of-
direction rule. Overall, our analysis offers a new and very insightful re-interpretation of the
existing market timing rules.
The second contribution of this paper is a straightforward application of the useful knowl-
edge revealed by our analysis of anatomy of timing rules and is motivated as follows. In all
previous academic studies on the pro(cid:12)tability of market timing rules (see the references in
footnote 1 above), the researchers usually selected an arbitrary and limited set of so-called
\most popular combinations" of trading rules with moving average weighting schemes. There-
fore the conclusions on the pro(cid:12)tability of market timing rules reached in previous studies are
exclusively related to the chosen set of combinations. Put differently, these conclusions cannot
be generalized to the entire universe of all potential combinations of trading rules with moving
average weighting schemes.
3
Electronic copy available at: https://ssrn.com/abstract=2585056

Earlier, in order to select the best combination of a trading rule with a moving average
weighting scheme, using relevant historical data a researcher had to perform the tests of all
possible combinations in order to (cid:12)nd the one with the best performance. This is a daunting
and next to impossible task. Our analysis allows a researcher to simplify dramatically this
procedure because the performance of any moving average trading rule depends exclusively on
the shape of the weighting function for price changes. Therefore, to (cid:12)nd the best trading rule
one needs only to test various shapes of the weighting function. In this paper we, for the (cid:12)rst
time, evaluate the out-of-sample2 performance of 300 various shapes of the weighting function
for price changes using historical data on four (cid:12)nancial market indices. These shapes are
chosen to represent different variations of a few most typical shapes of the weighting functions
used in market timing with moving averages. Our (cid:12)ndings suggest answers to long-standing
questions about optimal types of moving averages and whether the best performing trading
rule can beat the passive counterpart in out-of-sample tests.
The rest of the paper is organized as follows. In the subsequent Section 2 we present the
moving averages and trading rules considered in the paper. Then in Section 3 we demonstrate
the anatomy of trading rules with different moving averages and brie(cid:13)y review an alternative
approach to the construction of trading indicators based on moving averages. Section 4 de-
scribes our empirical data, the set of weighting functions, the methodology for out-of-sample
testing, and the results of the tests. Finally, Section 5 concludes the paper.
2 Moving Averages and Technical Trading Rules
2.1 Moving Averages
Amovingaverageofpricesiscalculatedusinga(cid:12)xedsizedata\window"thatisrolledthrough
time. Thelengthofthiswindowofdata, alsocalledthelookbackperiodoraveragingperiod, is
the time interval over which the moving average is computed. We follow the standard practice
and use prices, not adjusted for dividends, in the computation of moving averages and all
technical trading indicators. More formally, let (P ;P ;:::;P ) be the observations of the
1 2 T
2Itisworthmentioningthat,tothebestknowledgeoftheauthor,thereareonlytwopaperstodate,Sullivan
etal.(1999)andZakamulin(2014),wheretheresearchersimplementout-of-sampletestsofpro(cid:12)tabilityofsome
trading rules in the stock market.
4
Electronic copy available at: https://ssrn.com/abstract=2585056

monthly3 closing prices of a stock price index. A moving average at time t is computed using
the last closing price P t and k lagged prices P t(cid:0)j , j 2 [1;k]. It is worth noting that the time
interval over which the moving average is computed amounts to k months and includes k+1
monthly observations. Generally, each price observation in the rolling window of data has
its own weight in the computation of a moving average. More formally, a weighted Moving
Average at month-end t with k lagged prices (denoted by MA (k)) is computed as
t
∑
MA (k) = w t P t +w t(cid:0)1 P t(cid:0)1 +w t(cid:0)2 P t(cid:0)2 +:::+w t(cid:0)k P t(cid:0)k = ∑ k j=0 w t(cid:0)j P t(cid:0)j ; (1)
t w t +w t(cid:0)1 +w t(cid:0)2 +:::+w t(cid:0)k k
j=0
w t(cid:0)j
where w t(cid:0)j is the weight of price P t(cid:0)j in the computation of the weighted moving average.
It is worth observing that in order to compute a moving average one has to use at least one
lagged price, this means that one should have k (cid:21) 1. Note that when the number of lagged
prices is zero, a moving average becomes the last closing price, that is, MA (0) = P .
t t
Themostcommonlyusedtypesofmovingaveragesare: theSimpleMovingAverage(SMA),
theLinear(orlinearlyweighted)MovingAverage(LMA),andtheExponentialMovingAverage
(EMA). A less commonly used type of moving average is the Reverse Exponential Moving
Average (REMA). These moving averages at month-end t are computed as
∑
SMA t (k) = k+
1
1
∑k
P t(cid:0)j ; LMA t (k) = ∑
k
j=0 k
(k
(
(cid:0)
k(cid:0)
j +
j +
1)P
1)
t(cid:0)j
;
j=0 j=0
∑ ∑ (2)
EMA (k) = ∑
k
j=0
(cid:21)jP
t(cid:0)j
; REMA (k) = ∑
k
j=0
(cid:21)k(cid:0)jP
t(cid:0)j
;
t k (cid:21)j t k (cid:21)k(cid:0)j
j=0 j=0
where 0 < (cid:21) (cid:20) 1 is a decay factor.
As compared with the simple moving average, either the linearly weighted moving average
or the exponentially weighted moving average puts more weight on the more recent price ob-
servations. Theusualjusti(cid:12)cationfortheuseofthesetypesofmovingaveragesisawidespread
belief that the most recent stock prices contain more relevant information on the future direc-
tion of the stock price than earlier stock prices. In the linearly weighted moving average the
weights decrease in arithmetic progression. In particular, in LMA(k) the latest observation
hasweightk+1, thesecondlatestk, etc. downtoone. Adisadvantageofthelinearlyweighted
3Throughout the paper, we assume that the price data comes at the monthly frequency. Yet the results
presented in the (cid:12)rst part of the paper are valid for any data frequency.
5
Electronic copy available at: https://ssrn.com/abstract=2585056

moving average is that the weighting scheme is too rigid. In contrast, by varying the value of
(cid:21) in the exponentially weighted moving average, one is able to adjust the weighting to give
greater or lesser weight to the most recent price. The properties of the exponential moving
average:
lim EMA (k) = SMA (k); lim EMA (k) = P : (3)
t t t t
(cid:21)!1 (cid:21)!0
Contrary to the normal exponential moving average that gives greater weights to the most
recentprices,thereverseexponentialmovingaverageassignsgreaterweightstothemostoldest
prices and decreases the importance of the most recent prices. The properties of the reverse
exponential moving average:
lim REMA t (k) = SMA t (k); lim REMA t (k) = P t(cid:0)k : (4)
(cid:21)!1 (cid:21)!0
Instead of the regular moving averages of prices considered above, traders sometimes use
more elaborate moving averages that can be considered as \moving averages of moving aver-
ages". Speci(cid:12)cally, instead of using a regular moving average to smooth the price series, some
traders perform either double- or triple-smoothing of the price series. The main examples
of this type of moving averages are: Triangular Moving Average, Double Exponential Moving
Average, andTripleExponentialMovingAverage(see, forexample, KirkpatrickandDahlquist
(2010)). To shorten and streamline the presentation, we will not consider these moving aver-
agesinourpaper. Yetourmethodologycanbeappliedtotheanalysisofthetradingindicators
based on this type of moving averages in a straightforward manner.
2.2 Technical Trading Rules
Every market timing rule prescribes investing in the stocks (that is, the market) when a Buy
signal is generated and moving to cash or shorting the market when a Sell signal is generated.
In the absence of transaction costs, the time t return to a market timing strategy is given by
( )
r = (cid:14) r + 1(cid:0)(cid:14) r ; (5)
t tjt(cid:0)1 Mt tjt(cid:0)1 ft
where r and r are the month t returns on the stock market (including dividends) and the
Mt ft
risk-free asset respectively, and (cid:14) 2 f0;1g is a trading signal for month t (0 means Sell and
tjt(cid:0)1
6
Electronic copy available at: https://ssrn.com/abstract=2585056

1 means Buy) generated at the end of month t(cid:0)1.
In each market timing rule the generation of a trading signal is a two-step process. At the
(cid:12)rst step, one computes the value of a technical trading indicator using the last closing price
and k lagged prices
TR(k)
Indicator t = Eq(P t ;P t(cid:0)1 ;:::;P t(cid:0)k ); (6)
where TR denotes the timing rule and Eq((cid:1)) is the equation that speci(cid:12)es how the technical
trading indicator is computed. At the second step, using a speci(cid:12)c function one translates the
value of the technical indicator into the trading signal. In all market timing rules considered
in this paper, the Buy signal is generated when the value of a technical trading indicator is
positive. Otherwise, the Sell signal is generated. Thus, the generation of a trading signal can
beinterpretedasanapplicationofthefollowing(mathematical)indicator function tothevalue
of the technical indicator
( )
TR(k)
(cid:14) = 1 Indicator ; (7)
t+1jt + t
where the indicator function 1 ((cid:1)) is de(cid:12)ned by
+
8
>
>
<
1 (or Buy signal) if x > 0;
1 (x) = (8)
+ >
>
: 0 (or Sell signal) if x (cid:20) 0:
Westartthe presentationoftrading rulesconsideredinthe paper withtheMomentumrule
(MOM) which is the simplest and most basic market timing rule. In the Momentum rule one
compares the last closing price, P t , with the closing price k months ago, P t(cid:0)k . In this rule a
Buy signal is generated when the last closing price is greater than the closing price k months
ago. Formally, the technical trading indicator for the Momentum rule is computed as
Indicator M t OM(k) = MOM t (k) = P t (cid:0)P t(cid:0)k : (9)
Then the trading signal is generated by
MOM(k)
(cid:14) = 1 (MOM (k)): (10)
t+1jt + t
Most often, in order to generate a trading signal, a trader compares the last closing price
7
Electronic copy available at: https://ssrn.com/abstract=2585056

with the value of a k-month moving average. In this case a Buy signal is generated when the
last closing price is above a k-month moving average. Otherwise, if the last closing price is
below a k-month moving average, a Sell signal is generated. Formally, the technical trading
indicator for the Price-Minus-Moving-Average rule (P-MA) is computed as
Indicator P-MA(k) = P (cid:0)MA (k): (11)
t t t
Some traders argue that the price is noisy and the Price-Minus-Moving-Average rule pro-
duces many false signals (whipsaws). They suggest to address this problem by employing two
moving averages in the generation of a trading signal: one shorter average with averaging pe-
riod s and one longer average with averaging period k > s. This technique is called the Double
Crossover Method4 (DCM). In this case the technical trading indicator is computed as
Indicator DCM(s;k) = MA (s)(cid:0)MA (k): (12)
t t t
It is worth noting the obvious relationship
DCM(0;k) P-MA(k)
Indicator = Indicator : (13)
t t
Less often, in order to generate a trading signal, the traders compare the most recent value
of a k-month moving average with the value of a k-month moving average in the preceding
month. Intuitively, whenthestockpricesaretrendingupward(downward)themovingaverage
isincreasing(decreasing). Consequently,inthiscaseaBuysignalisgeneratedwhenthevalueof
a k-month moving average has increased over a month. Otherwise, a Sell signal is generated.
Formally, the technical trading indicator for the Moving-Average-Change-of-Direction rule
(∆MA) is computed as
Indicator ∆ t MA(k) = MA t (k)(cid:0)MA t(cid:0)1 (k): (14)
4Also known as the Moving Average Crossover (MAC).
8
Electronic copy available at: https://ssrn.com/abstract=2585056

3 Anatomy of Trading Rules
3.1 Preliminaries
It has been known for years that there is a relationship between the Momentum rule and the
Simple-Moving-Average-Change-of-Direction rule.5 In particular, note that
SMA t (k(cid:0)1)(cid:0)SMA t(cid:0)1 (k(cid:0)1) = P t (cid:0)P t(cid:0)k = MOM t (k) : (15)
k k
Therefore
Indicator ∆SMA(k(cid:0)1) (cid:17) Indicator MOM(k) ; (16)
t t
where the symbol \(cid:17)" means equivalence. The equivalence of two technical indicators stems
fromthefollowingproperty: themultiplicationofatechnicalindicatorbyanypositiverealnum-
ber produces an equivalent technical indicator. This is because the trading signal is generated
depending on the sign of the technical indicator. The formal presentation of this property:
1 (a(cid:2)Indicator (k)) = 1 (Indicator (k)); (17)
+ t + t
where a is any positive real number. Using relation (16) as an illustrating example, observe
that if SMA t (k(cid:0)1)(cid:0)SMA t(cid:0)1 (k(cid:0)1) > 0 then MOM t (k) > 0 and vice versa. In other words,
the Simple-Moving-Average-Change-of-Direction rule, ∆SMA(k(cid:0)1), generates the Buy (Sell)
trading signal when the Momentum rule, MOM (k), generates the Buy (Sell) trading signal.
t
What else can we say about the relationship between different market timing rules? The
ultimate goal of this section is to answer this question and demonstrate that all market timing
rules considered in this paper are closely interconnected. In particular, we are going to show
that the computation of a technical trading indicator for every market timing rule can be
interpreted as the computation of the weighted moving average of monthly price changes over
the averaging period. We will do it sequentially for each trading rule.
5See, for example, http://en.wikipedia.org/wiki/Momentum (technical analysis).
9
Electronic copy available at: https://ssrn.com/abstract=2585056

3.2 Momentum Rule
The computation of the technical trading indicator for the Momentum rule can equivalently
be represented by
Indicator M t OM(k) = MOM t (k) = P t (cid:0)P t(cid:0)k
∑k (18)
= (P t (cid:0)P t(cid:0)1 )+(P t(cid:0)1 (cid:0)P t(cid:0)2 )+:::+(P t(cid:0)k+1 (cid:0)P t(cid:0)k ) = ∆P t(cid:0)i ;
i=1
where ∆P t(cid:0)i = P t(cid:0)i+1 (cid:0)P t(cid:0)i denotes the monthly price change. Consequently, using property
(17), the computation of the technical indicator for the Momentum rule is equivalent to the
computation of the equally weighted moving average of the monthly price changes:
∑k
1
Indicator M t OM(k) (cid:17) k ∆P t(cid:0)i : (19)
i=1
3.3 Price-Minus-Moving-Average Rule
First, we derive the relationship between the Price-Minus-Moving-Average rule and the Mo-
mentum rule:
∑ ∑ ∑
Indicator P-MA(k) = P (cid:0)MA (k) = P (cid:0) ∑ k j=0 w t(cid:0)j P t(cid:0)j = k j=0 w t(cid:0)j ∑ P t (cid:0) k j=0 w t(cid:0)j P t(cid:0)j
t t t t k
j=0
w t(cid:0)j k
j=0
w t(cid:0)j
∑ ∑
=
k j=1∑ w t(cid:0)j (P t (cid:0)P t(cid:0)j )
=
k j=1∑ w t(cid:0)j MOM t (j)
:
k
j=0
w t(cid:0)j k
j=0
w t(cid:0)j
(20)
Using property (17), the relation above can be conveniently re-written as
∑
Indicator P-MA(k) (cid:17) k j=1∑ w t(cid:0)j MOM t (j) : (21)
t k
j=1
w t(cid:0)j
Consequently, the computation of the technical indicator for the Price-Minus-Moving-Average
rule,P (cid:0)MA (k),isequivalenttothecomputationoftheweightedmovingaverageoftechnical
t t
indicators for the Momentum rules, MOM (j), for j 2 [1;k]. It is worth noting that the
t
weighting scheme for computing the moving average of the momentum technical indicators,
MOM (j), is the same as the weighting scheme for computing the weighted moving average
t
10
Electronic copy available at: https://ssrn.com/abstract=2585056

MA (k).
t
Second, we use identity (18) and rewrite the numerator in (21) as
∑k ∑k ∑j
w t(cid:0)j MOM t (j) = w t(cid:0)j ∆P t(cid:0)i = w t(cid:0)1 ∆P t(cid:0)1 +w t(cid:0)2 (∆P t(cid:0)1 +∆P t(cid:0)2 )+:::
j=1 j=1 i=1
+w t(cid:0)k (∆P t(cid:0)1 +∆P t(cid:0)2 +:::+∆P t(cid:0)k ) = (w t(cid:0)1 +:::+w t(cid:0)k )∆P t(cid:0)1 (22)
0 1
∑k ∑k
@ A
+(w t(cid:0)2 +:::+w t(cid:0)k )∆P t(cid:0)2 +:::+w t(cid:0)k ∆P t(cid:0)k = w t(cid:0)j ∆P t(cid:0)i :
i=1 j=i
The last expression tells us that the numerator in (21) is a weighted sum of the monthly
∑
price changes over the averaging window, where the weight of ∆P t(cid:0)i equals k
j=i
w t(cid:0)i . Thus,
another alternative expression for the computation of the technical indicator for the Price-
Minus-Moving-Average rule is given by
( )
∑ ∑
∑
Indicator P-MA(k) (cid:17) k i= ∑ 1 ( k j= ∑ i w t(cid:0)j ∆ ) P t(cid:0)i = k i=∑1 x t(cid:0)i ∆P t(cid:0)i : (23)
t k i=1 k j=i w t(cid:0)j k i=1 x t(cid:0)i
where
∑k
x t(cid:0)i = w t(cid:0)j (24)
j=i
is the weight of the price change ∆P t(cid:0)i . In words, the computation of the technical indicator
for the Price-Minus-Moving-Average rule is equivalent to the computation of the weighted
moving average of the monthly price changes in the averaging window.
It is important to note from equation (24) that the application of the Price-Minus-Moving-
Average rule usually leads to overweighting the most recent price changes as compared to the
original weighting scheme used to compute the moving average of prices. If the weighting
scheme in a trading rule is already designed to overweight the most recent prices, then as a
rule the trading signal is computed with a much stronger overweighting the most recent price
changes. This will be demonstrated below.
Let us now, on the basis of (23), present the alternative expressions for the computation
of Price-Minus-Moving-Average technical indicators that use the speci(cid:12)c weighting schemes
described in the preceding section. We start with the Simple Moving Average which uses the
11
Electronic copy available at: https://ssrn.com/abstract=2585056

equally weighted moving average of prices. In this case the weight of ∆P t(cid:0)i is given by
∑k ∑k
x t(cid:0)i = w t(cid:0)j = 1 = k(cid:0)i+1: (25)
j=i j=i
Consequently, the equivalent representation for the computation of the technical indicator for
the Price-Minus-Simple-Moving-Average rule:
∑
Indicator P-SMA(k) (cid:17) k i=∑1 (k(cid:0)i+1)∆P t(cid:0)i = k∆P t(cid:0)1 +(k(cid:0)1)∆P t(cid:0)2 +:::+∆P t(cid:0)k : (26)
t k (k(cid:0)i+1) k+(k(cid:0)1)+:::+1
i=1
This suggests that alternatively we can interpret the computation of the technical indicator
for the Price-Minus-Simple-Moving-Average rule as the computation of the linearly weighted
moving average of monthly price changes.
We next consider the Linear Moving Average which uses the linearly weighted moving
average or prices. In this case the weight of ∆P t(cid:0)i is given by
∑k ∑k (k(cid:0)i+1)(k(cid:0)i+2)
x t(cid:0)i = w t(cid:0)j = (k(cid:0)j +1) = ; (27)
2
j=i j=i
which is the sum of the terms of arithmetic sequence from 1 to k (cid:0)i+1 with the common
differenceof1. Astheresult,theequivalentrepresentationforthecomputationofthetechnical
indicator for the Price-Minus-Linear-Moving-Average rule
∑
Indicator P-LMA(k) (cid:17) k i=∑1 (k(cid:0)i+1) 2 (k(cid:0)i+2) ∆P t(cid:0)i : (28)
t k (k(cid:0)i+1)(k(cid:0)i+2)
i=1 2
Then we consider the Exponential Moving Average which uses the exponentially weighted
moving average or prices. In this case the weight of ∆P t(cid:0)i is given by
∑k ∑k ( )
(cid:21)
x t(cid:0)i = w t(cid:0)j = (cid:21)j = 1(cid:0)(cid:21) (cid:21)i(cid:0)1(cid:0)(cid:21)k ; (29)
j=i j=i
whichisthesumofthetermsofgeometricsequencefrom(cid:21)i to(cid:21)k. Consequently,theequivalent
presentation for the computation of the technical indicator for the Price-Minus-Exponential-
12
Electronic copy available at: https://ssrn.com/abstract=2585056

Moving-Average rule
∑ ( )
Indicator P-EMA(k) (cid:17) k i=∑1 (cid:21)i(cid:0)1(cid:0)(cid:21)k ∆P t(cid:0)i : (30)
t k ((cid:21)i(cid:0)1(cid:0)(cid:21)k)
i=1
Ifk isrelativelylargesuchthat(cid:21)k (cid:25) 0,thentheexpressionforthecomputationofthetechnical
indicator for the Price-Minus-Exponential-Moving-Average rule becomes
∑
Indicator P-EMA(k) (cid:17) k i=∑1 (cid:21)i(cid:0)1∆P t(cid:0)i = ∆P t(cid:0)1 +(cid:21)∆P t(cid:0)2 +:::+(cid:21)k(cid:0)1∆P t(cid:0)k ; when (cid:21)k (cid:25) 0:
t k (cid:21)i(cid:0)1 1+(cid:21)+:::+(cid:21)k(cid:0)1
i=1
(31)
In words, the computation of the trading signal for the Price-Minus-Exponential-Moving-
Average rule, when k is rather large, is equivalent to the computation of the exponential
moving average of monthly price changes. It is worth noting that this is probably the only
trading rule where the weighting scheme for the computation of moving average of prices is
identical to the weighting scheme for the computation of moving average of price changes.
The weight of ∆P t(cid:0)i for the Reverse Exponential Moving Average is given by
∑k ∑k 1(cid:0)(cid:21)k(cid:0)i+1
x t(cid:0)i = w t(cid:0)j =
(cid:21)k(cid:0)j
= 1(cid:0)(cid:21) ; (32)
j=i j=i
which is the sum of the terms of geometric sequence from 1 to
(cid:21)k(cid:0)i.
Consequently, the
equivalent representation for the computation of the technical indicator for the Price-Minus-
Reverse-Exponential-Moving-Average rule
∑ ( )
Indicator P-REMA(k) (cid:17) k i=∑1 1(cid:0)(cid:21)k(cid:0)i+1 ∆P t(cid:0)i : (33)
t k (1(cid:0)(cid:21)k(cid:0)i+1)
i=1
3.4 Moving-Average-Change-of-Direction Rule
The value of this technical trading indicator is based on the difference of two weighted moving
averages computed at times t and t(cid:0)1 respectively. We assume that the size of the averaging
window is k (cid:0) 1 months, the reason for this assumption will become clear very soon. The
13
Electronic copy available at: https://ssrn.com/abstract=2585056

straightforward computation yields
∑ ∑
Indicator ∆ t MA(k(cid:0)1) = M ∑ A t (k(cid:0)1)(cid:0)MA t(cid:0)1 (k(cid:0)1) = ∑ ∑ k i= (cid:0) 0 k i 1 = (cid:0) w 0 1 t w (cid:0)i t P (cid:0)i t(cid:0)i (cid:0) k i=∑ (cid:0) 0 1 k i w = (cid:0) 0 t 1 (cid:0) w i P t(cid:0) t(cid:0) i i(cid:0)1
= k i= (cid:0) 0 1w t∑ (cid:0)i (P t(cid:0)i (cid:0)P t(cid:0)i(cid:0)1 ) = k i=∑1 w t(cid:0)i+1 ∆P t(cid:0)i :
k
i=
(cid:0)
0
1w t(cid:0)i k
i=1
w t(cid:0)i+1
(34)
Consequently, the computation of the technical indicator for the Moving-Average-Change-of-
Direction rule can be directly interpreted as the computation of the weighted moving average
of monthly price changes:
∑
Indicator
∆MA(k(cid:0)1)
=
k
i=∑1
w t(cid:0)i+1 ∆P t(cid:0)i
: (35)
t k
i=1
w t(cid:0)i+1
Note that the weighting scheme for the computation of the moving average of monthly price
changes is the same as for the computation of moving average of prices. From (35) we easily
recover the relationship for the case of the Simple Moving Average where w t(cid:0)i+1 = 1 for all i
∑
Indicator ∆SMA(k(cid:0)1) (cid:17) k i=1 ∆P t(cid:0)i (cid:17) Indicator MOM(k) ; (36)
t k t
where the last equivalence follows from (19).
In the case of the Linear Moving Average, where w t(cid:0)i+1 = k (cid:0) i + 1, we derive a new
relationship:
∑
Indicator ∆LMA(k(cid:0)1) (cid:17)
k
i=∑1
(k(cid:0)i+1)∆P
t(cid:0)i (cid:17) IndicatorP-SMA(k); (37)
t k (k(cid:0)i+1) t
i=1
where the last equivalence follows from (26). Putting it into words, the Price-Minus-Simple-
Moving-Average rule, P (cid:0)SMA (k), prescribes investing in the stocks (moving to cash) when
t t
the Linear Moving Average of prices over the averaging window of k (cid:0) 1 months increases
(decreases).
In the case of the Exponential Moving Average and Reverse Exponential Moving Average,
14
Electronic copy available at: https://ssrn.com/abstract=2585056

the resulting expressions for the Change-of-Direction rules can be written as
∑
Indicator
∆EMA(k(cid:0)1)
=
k
i=∑1
(cid:21)i(cid:0)1∆P
t(cid:0)i
; (38)
t k (cid:21)i(cid:0)1
i=1
∑
Indicator
∆REMA(k(cid:0)1)
=
k
i=∑1
(cid:21)k(cid:0)i∆P
t(cid:0)i
: (39)
t k (cid:21)k(cid:0)i
i=1
Observe in particular that if k is rather large, then, using result (31), we obtain yet another
new relationship:
Indicator P-EMA(k) (cid:17) Indicator ∆EMA(k(cid:0)1) ; when (cid:21)k (cid:25) 0: (40)
t t
In words, when k is rather large, the Price-Minus-Exponential-Moving-Average rule is equiv-
alent to the Exponential-Moving-Average-Change-of-Direction rule. As it might be observed,
forthemajorityofweightingschemesconsideredinthepaper, thereisaone-to-oneequivalence
between a Price-Minus-Moving-Average rule and a corresponding Moving-Average-Change-of-
Direction rule. Therefore, the majority of the moving-average-change-of-direction rules (and
may be all of them) can also be expressed as the moving average of Momentum rules.
Finally it is worth commenting that the traders had long ago taken notice of the fact that,
forexample,veryoftenaBuysignalisgenerated(cid:12)rstbythePrice-Minus-Moving-Averagerule,
then with some delay a Buy signal is generated by the Moving-Average-Change-of-Direction
rule. Therefore the traders sometimes use the trading signal of the Moving-Average-Change-
of-Direction rule to \con(cid:12)rm" the signal of the Price-Minus-Moving-Average rule (see Murphy
(1999), Chapter 9). Our analysis provides a simple explanation for the existence of a delay
between the signals generated by these two rules. Speci(cid:12)cally, the delay naturally occurs be-
cause the Price-Minus-Moving-Average rule overweights more heavily the most recent price
changes than the Moving-Average-Change-of-Direction rule computed using the same weight-
ing scheme. Therefore the Price-Minus-Moving-Average rule reacts more quickly to the recent
trend changes than the Moving-Average-Change-of-Direction rule.6
6Assume,forexample,thatthetraderusesthesimplemovingaverageweightingschemeinboththerules. In
this case our result says that the Price-Minus-Simple-Moving-Average rule is equivalent to the Linear-Moving-
Average-Change-of-Direction rule. As a consequence, it is naturally to expect that the Price-Minus-Simple-
Moving-AveragerulereactsmorequicklytotherecenttrendchangesthantheSimple-Moving-Average-Change-
of-Direction rule.
15
Electronic copy available at: https://ssrn.com/abstract=2585056

3.5 Double Crossover Method
The relationship between the Double Crossover Method and the Momentum rule is as follows
(here we use result (20))
Indicator DCM(s;k) = MA (s)(cid:0)MA (k) = (P (cid:0)MA (k))(cid:0)(P (cid:0)MA (s))
t t t t t t t
∑ ∑
k wk MOM (j) s ws MOM (j) (41)
= j=1∑t(cid:0)j t (cid:0) j=1∑t(cid:0)j t :
k j=0 w t k (cid:0)j s j=0 w t s (cid:0)j
Differentsuperscriptsintheweightsmeanthatforthesamesubscripttheweightsaregenerally
not equal. For example, in case of either linearly weighted moving averages or reverse expo-
nential moving averages wk ̸= ws , yet for the other weighting schemes considered in this
t(cid:0)j t(cid:0)j
paper wk = ws . In order to get a closer insight into the anatomy of the Double Crossover
t(cid:0)j t(cid:0)j
Method, we assume that one uses the exponential weighting scheme in the computation of
moving averages (as it most often happens in practice). In this case the expression for the
value of the technical indicator in terms of monthly price changes is given by (here we use
results (22) and (29))
( )
∑ ∑ ∑ ∑ ∑ ∑
Indicator DCM(s;k) = k j=1 (cid:21) ∑ j j i=1 ∆P t(cid:0)i (cid:0) s j=1 (cid:21) ∑ j j i=1 ∆P t(cid:0)i = k i=1 ∑ k j=i (cid:21)j ∆P t(cid:0)i
t k (cid:21)j s (cid:21)j k (cid:21)j
( j=0 ) j=0 j=1
∑ ∑ ∑ ( ) ∑ ( )
(cid:0) s i=1 ∑ s j=i (cid:21)j ∆P t(cid:0)i = k i=1 (cid:21)i(cid:0)(cid:21)k+1 ∆P t(cid:0)i (cid:0) s i=1 (cid:21)i(cid:0)(cid:21)s+1 ∆P t(cid:0)i :
s (cid:21)j 1(cid:0)(cid:21)k+1 1(cid:0)(cid:21)s+1
j=1
(42)
If we assume in addition that both s and k are relatively large such that (cid:21)s (cid:25) 0 and (cid:21)k (cid:25) 0,
then we obtain
∑k ∑s ∑k
Indicator D t CM(s;k) (cid:25) (cid:21)i∆P t(cid:0)i (cid:0) (cid:21)i∆P t(cid:0)i = (cid:21)i∆P t(cid:0)i : (43)
i=1 i=1 i=s+1
The expression above can be conveniently re-written as
∑
Indicator DCM(s;k) (cid:17)
k
i∑=s+1
(cid:21)i(cid:0)s(cid:0)1∆P
t(cid:0)i when k > s;(cid:21)s (cid:25) 0;(cid:21)k (cid:25) 0: (44)
t k (cid:21)i(cid:0)s(cid:0)1
j=s+1
16
Electronic copy available at: https://ssrn.com/abstract=2585056

In words, the computation of the trading signal for the Double Crossover Method based on
the exponentially weighted moving averages of lengths s and k > s, when both s and k are
rather large, is equivalent to the computation of the exponentially weighted moving average
of monthly price changes, ∆P t(cid:0)i , for i 2 [s+1;k]. Note that the most recent s monthly price
changes completely disappear in the computation of the technical trading indicator. In other
words, in the computation of the trading indicator one disregards, or skips, the most recent
s monthly price changes. When the values of s and k are not rather large, the most recent
s monthly price changes do not disappear in the computation of the technical indicator, yet
the weights of these price changes are reduced as compared to the weight of the subsequent
(s+1)-th price change.
3.6 Discussion
Summing up the results presented above, all technical trading indicators considered in this
paper are computed in the same general manner. We (cid:12)nd, for instance, that the computation
ofeverytechnicaltradingindicatorcanbeinterpretedasthecomputationofaweightedaverage
of the momentum rules computed using different averaging periods. Thus, the momentum rule
might be considered as an elementary trading rule on the basis of which one can construct
more elaborate rules. The most insightful conclusion emerging from our analysis is that the
computation of every technical trading indicator, based on moving averages of prices, can also
be interpreted as the computation of the weighted moving average of price changes. More
formally, our analysis shows that the value of every trading indicator can alternatively be
computed using the following general formula
∑
Indicator TR(k) (cid:17) k i=∑1 x t(cid:0)i ∆P t(cid:0)i ; (45)
t k
i=1
x t(cid:0)i
where x t(cid:0)i is the weight of the price change ∆P t(cid:0)i .
Our main conclusion is that, despite being computed seemingly different at the (cid:12)rst sight,
the only real difference between miscellaneous rules lies in the weighting scheme used to com-
pute the moving average of price changes. Figure 1 illustrates a few distinctive weighting
schemes for the computation of technical trading indicators based on moving averages. In par-
ticular, this (cid:12)gure illustrates the weighting schemes for the Momentum rule, the Price-Minus-
17
Electronic copy available at: https://ssrn.com/abstract=2585056

Reverse-Exponential-Moving-Average rule (with (cid:21) = 0:8), the Price-Minus-Simple-Moving-
Average rule, the Price-Minus-Linear-Moving-Average rule, and the Double Crossover Method
(based on using two exponential moving averages with (cid:21) = 0:8). For all technical indicators
we use k = 10 which means that to compute the value of a technical indicator we use the most
recent price change, ∆P t(cid:0)1 , denoted as Lag0, and 9 preceding lagged price changes up to lag
∆P t(cid:0)10 , denoted as Lag9. In addition, in the computation of the technical indicator for the
Double Crossover Method we use s = 3.
Lag0
Lag1
Lag2
Lag3
Lag4
Lag5
Lag6
Lag7
Lag8
Lag9
MOM P−REMA P−SMA P−LMA DCM
52.0
02.0
51.0
01.0
50.0
00.0
Figure 1: Weights of monthly price changes used for the computations of the technical trading in-
dicators with k = 10. MOM denotes the Momentum rule. P-REMA denotes the Price-Minus-
Reverse-Exponential-Moving-Average rule (with (cid:21) = 0:8). P-SMA denotes the Price-Minus-Simple-
Moving-Average rule. P-LMA denotes the Price-Minus-Linear-Moving-Average rule. DCM denotes
the Double Crossover Method (based on using two exponential moving averages with (cid:21) = 0:8 and
s = 3). Lag(i(cid:0)1) denotes the weight of the lag ∆P t(cid:0)i , where Lag0 denotes the most recent price
change ∆P t(cid:0)1 and Lag9 denotes the most oldest price change ∆P t(cid:0)10 .
Apparently, the Momentum rule assigns equal weights to all monthly price changes in the
averaging window. The next three rules overweight the most recent price changes. They are
arranged according to increasing degree of overweighting. Whereas the Price-Minus-Simple-
Moving-Average rule employs the linear weighting scheme, the degree of overweighting in the
Price-Minus-Reverse-Exponential-Moving-Average rule can be gradually varied from the equal
18
Electronic copy available at: https://ssrn.com/abstract=2585056

weighting scheme (when (cid:21) = 0) to the linear weighting scheme (when (cid:21) = 1), see property (4).
Formally this can be expressed by
P-REMA(k) MOM(k) P-REMA(k) P-SMA(k)
lim Indicator = Indicator ; lim Indicator = Indicator :
(cid:21)!0 t t (cid:21)!1 t t
(46)
Comparing to the Price-Minus-Simple-Moving-Average rule, a higher degree of overweight-
ing can be attained by using the Exponential-Moving-Average-Change-of-Direction rule. The
degree of overweighting in this rule can be gradually varied from the linear weighting scheme
(when (cid:21) = 1) to the very extreme overweighting where only the most recent price change has
a non-zero weight (when (cid:21) = 0), see property (3). Formally this can be expressed by
∆EMA(k) MOM(k) ∆EMA(k)
(cid:21) li ! m 1 Indicator t = Indicator t ; (cid:21) li ! m 0 Indicator t = ∆P t(cid:0)1 : (47)
When (cid:21) (cid:25) 0:82, the degree of overweighting the most recent price changes in the Exponential-
Moving-Average-Change-of-Direction rule is virtually the same as in the Price-Minus-Linear-
Moving-Average rule. Therefore, we demonstrate only the weighting scheme in the Price-
Minus-Linear-Moving-Average rule.
In contrast to the previous rules, the weighting scheme in the Double Crossover Method
underweights both the most recent and the most old price changes. In this weighting scheme
the price change ∆P t(cid:0)s(cid:0)1 = ∆P t(cid:0)4 has the largest weight in the computation of moving
average.
Our alternative representation of the computation of technical trading indicators by means
of the moving average of price changes, together with the graphical visualization of the weight-
ing schemes for different rules presented in Figure 1, reveals a couple of paradoxes. The (cid:12)rst
paradoxconsistsinthefollowing. Manytradersarguethatthemostrecentstockpricescontain
more relevant information on the future direction of the stock price than earlier stock prices.
Therefore, one should better use the LMA(k) instead of the SMA(k) in the computation of
trading signals. Yet in terms of the monthly price changes the application of the Price-Minus-
Simple-Moving-Averagerulealreadyleadstooverweightingthemostrecentpricechanges. Ifit
is the most recent stock price changes (but not prices) that contain more relevant information
on the future direction of the stock price, then the use of the Price-Minus-Linear-Moving-
19
Electronic copy available at: https://ssrn.com/abstract=2585056

Average rule leads to a severe overweighting the most recent price changes, which might be
suboptimal.
The other paradox is related to the effect produced by the use of a shorter moving average
in the computation of a trading signal for the Double Crossover Method. Speci(cid:12)cally, our al-
ternative representation of the computation of technical trading indicators reveals an apparent
con(cid:13)ict of goals that some traders want to pursue. In particular, on the one hand, one wants
to put more weight on the most recent prices that are supposed to be more relevant. On the
other hand, one wants to smooth the noise by using a shorter moving average instead of the
last closing price (as in the Price-Minus-Moving-Average rule). It turns out that these two
goals cannot be attained simultaneously because the noise smoothing results in a substantial
reduction of weights assigned to the most recent price changes (and, therefore, most recent
prices). Figure 1 clearly demonstrates that the weighting scheme for the Double Crossover
Method has a hump-shaped form such that the largest weight is given to the monthly price
change at lag s. Then, as the lag number decreases to 0 or increases to k (cid:0)1, the weight of
the lag decreases. Consequently, the use of the Double Crossover Method can be justi(cid:12)ed only
when the price change at lag s contains the most relevant information on the future direction
of the stock price.
3.7 Alternative Construction of Trading Indicators
Let fp g be the series of observations of the log-prices of a stock index. That is, p = log(P )
t t t
where P is the month t closing price. The trading indicators based on moving averages can,
t
in principle, be constructed alternatively using the log-prices
TR(k)
Indicator t = Eq(p t ;p t(cid:0)1 ;:::;p t(cid:0)k ): (48)
In this case the straightforward application of our methodology (for examining how the value
of a trading indicator is computed) leads to the following general formula for the computation
of the value of trading indicator
∑
Indicator TR(k) (cid:17) ∑ k i=1 x t(cid:0)i q t(cid:0)i ; (49)
t k
i=1
x t(cid:0)i
20
Electronic copy available at: https://ssrn.com/abstract=2585056

where q t(cid:0)i = p t(cid:0)i+1 (cid:0) p t(cid:0)i is the log-return on the index over (t (cid:0) i;t (cid:0) i + 1) and x t(cid:0)i is
the weight of the log-return q t(cid:0)i in the computation of moving average. In words, in this case
the value of any trading indicator based on moving averages of log-prices can alternatively be
computed using a weighting moving average of log-returns.
Infact,HongandSatchell(2015)presentedalreadyin2013theresultthatcanbeconsidered
as a particular case of equation (49) when the trading rule is DCM(s;k) where in both shorter
and longer windows one uses the SMA weighting scheme. Later on Beekhuizen and Hallerbach
(2015) considered other types of trading rules and derived7 several particular cases of general
equation (49).
4 Best Performing Weighting Schemes in Out-of-Sample Tests
4.1 Data
The data for our empirical study in this section are similar to the data used in the study by
Zakamulin (2014). Speci(cid:12)cally, we use data on two stock market indices, two bond market
indices, and the risk-free rate of return. The two stock market indices are the Standard and
Poor’s Composite stock price index and the Dow Jones Industrial Average index. The two
bond market indices are the Long-Term and Intermediate-Term US Government Bond indices.
Our sample period begins in January 1926 and ends in December 2012 (87 full years), giving
a total of 1044 monthly observations.
We use the monthly Standard and Poor’s Composite stock price index data and corre-
sponding dividend data provided by Amit Goyal.8 From 1926 to 1956, the index data come
from various reports of the Standard and Poor’s. From 1957 this index is identical to the
Standard and Poor’s 500 index. For more details about the construction of the index and its
dividendseriesseeWelchandGoyal(2008). TheDJIAindexvaluesforthetotalsampleperiod
and dividends for the period 1988 to 2012 are provided by S&P Dow Jones Indices LLC, a
subsidiary of the McGraw-Hill Companies.9 The dividends for the period 1926 to 1987 are
obtained from Barron’s.10
7Their paper appeared several months after our paper was made available on the Internet.
8See http://www.hec.unil.ch/agoyal/.
9See http://www.djaverages.com.
10See http://online.barrons.com.
21
Electronic copy available at: https://ssrn.com/abstract=2585056

ThebonddataarefromtheIbbotsonSBBI2013ClassicYearbook. Weuseboththecapital
appreciation returns and total returns on the Long-Term and Intermediate-Term Government
Bonds. The risk-free rate of return is also provided by Amit Goyal. In particular, the risk-free
rate of return for our sample period is the Treasury bill rate.
4.2 Empirical Research Design
4.2.1 The Set of Weighting Schemes
The generation of different shapes of the moving average weighting function is based on the
following idea. Even though there are various combinations of trading rules based on moving
averages of prices coupled with various types of moving averages, all these combinations result
in basically only three types of the shape of the weighting function: equal weighting of price
changes (as in the MOM rule), underweighting the most old price changes (as in the P-MA
rule or in the most ∆MA rules), and underweighting both the most recent and the most old
price changes (as in the DCM). In order to generate these shapes, we employ three types of
weighting schemes based on exponential moving averages: (1) convex EMA weighting scheme
(CV-EMA) produced by ∆EMA(k) trading rule, (2) concave EMA weighting scheme (CC-
EMA) produced by P-REMA(k) trading rule, and (3) hump-shaped EMA weighting scheme
(HS-EMA) produced by DCM(s;k) trading rule where in both short and long windows we use
concave EMA weighting schemes. There is an uncertainly about the proper choice of the size
of the shorter window s in the DCM rule. Since the most popular combination in practice is
to use a 200-day long window and a 50-day short window, we set s = 1k for all values of k.
4
For some (cid:12)xed number of price change lags k, the shape of each type of a moving average
weighting function depends on the value of the decay factor (cid:21). In order to generate many
different shapes of the weighting function, in each trading rule we vary the value of (cid:21) 2
f0:00;1:00g with a step of ∆(cid:21) = 0:01. As a result, for each type of the EMA we get 100
differentshapes. SincewehavethreedifferenttypesoftheEMA,thetotalnumberofgenerated
shapes amounts to 300. As a result, we obtain 300 different trading strategies; each strategy is
speci(cid:12)ed by a particular shape of the moving average weighting function. Figure 2 illustrates
the shapes of each type of weighting functions for two arbitrary values of (cid:21). Both CV-EMA
and CC-EMA weighting schemes underweight the most old price changes. Yet, whereas in
22
Electronic copy available at: https://ssrn.com/abstract=2585056

0.20
0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Lag
thgieW
0.08
Decay, l
0.8
0.9
0.06
0.04
0.02
0.00
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Lag
thgieW
Decay, l
0.6
0.9
Panel A: Convex EMA (CV-EMA) weighting scheme Panel B: Concave EMA (CC-EMA) weighting scheme
0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Lag
thgieW
Decay, l
0.7
0.9
Panel C: Hump-shaped EMA (HS-EMA) weighting scheme
Figure 2: The types of the moving average weighting schemes used in our empirical study. Panel A
illustrates the convex exponential moving average weighting scheme produced by ∆EMA(k) trading
rule. Panel B illustrates the concave exponential moving average weighting scheme produced by P-
REMA(k) trading rule. Panel C illustrates the hump-shaped exponential moving average weighting
scheme produced by DCM(s;k) trading rule. (cid:21) denotes the decay factor. In all illustrations the
number of price changes k = 18. Lag denotes the weight of the lag ∆P t(cid:0)i , where Lag0 denotes the
most recent price change ∆P t(cid:0)1 and Lag17 denotes the most oldest price change ∆P t(cid:0)18 .
the CV-EMA the weight of the price lag i is a convex exponential function with respect to
i (see equation (38)), in the CC-EMA the weight of the price lag i is a concave exponential
function with respect to i (see equation (33)). It is worth repeating (recall the discussion in
Section 3.6) that by varying the value of (cid:21) from 0 to 1, the weighting scheme of the CC-EMA
varies from the equal weighting scheme (when (cid:21) = 0) to the linear weighting scheme (when
(cid:21) = 1); the weighting scheme of the CV-EMA varies from the very extreme overweighting
(when (cid:21) = 0, only the most recent price change has a non-zero weight) to the linear weighting
scheme (when (cid:21) = 1). Last but not least, the HS-EMA with (cid:21) = 1 is equivalent to using
the linear weighting schemes in both the shorter and longer windows (in this case the trading
signal can be generated by SMA(s)-SMA(k)).
23
Electronic copy available at: https://ssrn.com/abstract=2585056

4.2.2 Performance Measurement in Out-of-Sample Tests
We closely follow the methodology used in the study by Zakamulin (2014). Each shape of the
weighting function in our study is associated with a trading rule denoted by TR(k). Since our
goal is to estimate the real-life performance of trading rules, we need also to account for the
fact that the rebalancing an active portfolio incurs transaction costs. We suppose that buying
and selling stocks and bonds is costly, whereas buying and selling Treasury bills is costless.
Denoting by (cid:23) the one-way transaction costs, the return to the trading rule over month t is
given by 8
>
>
>
> > > r Pt if ((cid:14) t = Buy) and ((cid:14) t(cid:0)1 = Buy);
>
>
>
>
< r Pt (cid:0)(cid:23) if ((cid:14) t = Buy) and ((cid:14) t(cid:0)1 = Sell);
r =
t >
>
>
> > > r ft if ((cid:14) t = Sell) and ((cid:14) t(cid:0)1 = Sell);
>
>
>
>
: r ft (cid:0)(cid:23) if ((cid:14) t = Sell) and ((cid:14) t(cid:0)1 = Buy);
wherer denotesthedividend-adjustedreturntothepassivecounterpartoftheactivetrading
Pt
rule(eitherstockorbondindexreturnovermontht). Weassumethattheone-waytransaction
costs in the stock market amount to 0.25% ((cid:23) = 0:0025), whereas in the bond market the one-
way transaction costs amount to 0.10% ((cid:23) = 0:001).
The performance is measured by means of the Sharpe ratio. Speci(cid:12)cally, the Sharpe ratio
of a trading rule with excess returns re = r (cid:0)r is computed as (according to Sharpe (1994))
t t ft
(cid:22)(re)
SR(re) = t ;
t (cid:27)(re)
t
where (cid:22)(re) and (cid:27)(re) denote the mean and standard deviation of re respectively.
t t t
Itiscrucialtoobservethatinordertocomputethevalueofthetechnicalindicatorweneed
to specify the size of the averaging window k. The out-of-sample performance measurement
methodisbasedonsimulatingthereal-lifetradingwhereatraderhastomakeachoiceofwhat
sizeoftheaveragingwindowk tousegiventheinformationaboutthepastperformancesofthe
trading rule for different values of k. Speci(cid:12)cally, the out-of-sample testing procedure begins
with splitting the full historical data sample [1;T] into the initial in-sample subset [1;(cid:28)] and
out-of-sample subset [(cid:28)+1;T], where T is the last observation in the full sample and (cid:28) denotes
the splitting point. The initial in-sample period of [1;(cid:28)] is used to complete the procedure
24
Electronic copy available at: https://ssrn.com/abstract=2585056

of selecting the value of k which produces the best performance. That is, the choice of the
(cid:3)
optimal k is given by
(cid:28)
k (cid:3) = arg max SR(re;re;:::;re);
(cid:28) 1 2 (cid:28)
k2[kmin;kmax]
where kmin and kmax are the minimum and maximum values for k, and SR(re;re;:::;re)
1 2 (cid:28)
denotes the trading rule’s Sharpe ratio computed using the excess returns from month 1 to
(cid:3)
month (cid:28). Subsequently, the trading signal for month (cid:28) +1 is determined using the TR(k )
(cid:28)
rule. We then expand the in-sample period by one month, perform the selection of the value
of k which produces the best performance once again using the new in-sample period of [1;(cid:28)+
(cid:3)
1], and determines the trading signal for month (cid:28) +2 using the TR(k ) rule. We repeat
(cid:28)+1
this procedure, pushing the endpoint of the in-sample period ahead by one month with each
iteration of this process, until the trading signal for the last month T is determined.
The out-of-sample performance of a trading strategy is measured by computing trading
rule’s Sharpe ratio using the excess returns over the out-of-sample period, (re ;re ;:::;re).
(cid:28)+1 (cid:28)+2 T
To facilitate the performance comparison, we compute the Sharpe ratio of the passive coun-
terpart of the active trading rule using the excess returns over the same out-of-sample period
(re ;re ;:::;re ) and report the difference between the Sharpe ratio of the trading rule
P;(cid:28)+1 P;(cid:28)+2 P;T
and the Sharpe ratio of the passive strategy
∆SR = SR (cid:0)SR ;
TR P
where SR and SR denote the Sharpe ratios of the trading rule and its passive benchmark
TR P
respectively. Because the estimate for a Sharpe ratio is subject to estimation errors, we have
scienti(cid:12)c evidence that a trading rule outperforms its passive counterpart only when we can
reject the following null hypothesis
H : ∆SR (cid:20) 0:
0
This hypothesis is tested using Jobson and Korkie (1981) test with the Memmel (2003) cor-
rection. Speci(cid:12)cally, given SR , SR , and (cid:26) as two estimated Sharpe ratios and correlation
TR P
coefficient between the excess returns of the active and passive strategies over a sample of size
25
Electronic copy available at: https://ssrn.com/abstract=2585056

T, the test of the null hypothesis is obtained via the test statistic
SR (cid:0)SR
z = √ [ TR P ];
1 2(1(cid:0)(cid:26)2)+ 1(SR2 +SR2 (cid:0)2(cid:26)2SR SR )
T 2 TR P TR P
which is asymptotically distributed as a standard normal.
4.3 Empirical Results
For each stock and bond market index, we perform out-of-sample simulation of the returns to
300 different trading rules (where each one is associated with a speci(cid:12)c shape of the weighting
function) over the period January 1930 to December 2012. Since the most typical recommen-
dation for the size of the averaging window varies from 10 to 12 months, to be on the safe side
we set kmin = 4 and kmax = 18. For each index, Table 1 reports the top 10 best performing
weighting schemes together with their decay factors and the mean sizes of the averaging win-
dow11 k+1, the difference between the Sharpe ratio of the trading rule and the Sharpe ratio
of its passive counterpart ∆SR, and the p-value of testing the null hypothesis H : ∆SR (cid:20) 0.
0
For the Standard and Poor’s Composite index, 7 out of 10 best performing weighting
schemes belong to the HS-EMA type where the decay factor varies in the range from 0.95
to 1.00. It is worth noting that in the best performing weighting scheme the decay factor
equals to 1.00 which means that the best performing trading rule can be implemented as the
difference between SMA(s) and SMA(k). Interestingly, since the mean value of k +1 equals
to 9 and, therefore, the mean value of s+1 equals to 3, the best performing weighting scheme
closely corresponds to the very popular among practitioners DCM rule where one uses 50-day
and 200-day simple moving averages. The CC-EMA weighting scheme with (cid:21) = 0:82 and the
CV-EMA weighting scheme with (cid:21) 2 f0:94;0:95g are also among the top 10 best performing
weighting schemes. The major types among the top 10 best performing weighting schemes for
the Standard and Poor’s Composite index are illustrated in Figure 3, Panel A. Whereas the
Sharpe ratio of the passive strategy amounts to 0.38, the Sharpe ratio of a weighting scheme,
that belongs to the top 10 best ones, exceeds the Sharpe ratio of the passive strategy by 0.12-
0.15. For 9 out of 10 best performing weighting schemes we can reject the null hypothesis at
11Note that in our exposition the value of k denotes the number of the lagged price changes. Therefore the
value of k+1 equals the number of prices used to compute the value of the trading indicator.
26
Electronic copy available at: https://ssrn.com/abstract=2585056

the 10% level in favor of the alternative hypothesis that the Sharpe ratio of the trading rule is
greater than the Sharpe ratio of the passive strategy.
For the Dow Jones Industrial Average index, among the top 10 best performing schemes 3
belong to the HS-EMA type, 4 to the CC-EMA type, and 3 to the CV-EMA type. As for the
Standard and Poor’s Composite index, the best performing weighting scheme also belongs to
the HS-EMA type. In contrast to the parameters of the best performing HS-EMA scheme for
theStandardandPoor’sCompositeindex,inthiscasetheHS-EMAschemeusesasubstantially
longer length of the averaging window (15 versus 9) and a notable lower decay factor (0.82
versus 1.00). The major types among the top 10 best performing weighting schemes for the
Dow Jones Industrial Average index are illustrated in Figure 3, Panel B. Interestingly, 3 out
of 4 CC-EMA weighting schemes (that are among the top 10 best ones) have a decay factor in
the range 0.21-0.23. As a result, the weighting in these schemes is close to the equal weighting
of price changes as in the MOM rule. The Sharpe ratio of the passive strategy also amounts
to 0.38, while the Sharpe ratio of a weighting scheme, that belongs to the top 10 best ones,
exceeds the Sharpe ratio of the passive strategy by 0.05-0.06. However, none of the top 10
bestperformingweightingschemesproducestheperformancewhichisstatisticallysigni(cid:12)cantly
better than that of the passive strategy (at conventional statistical levels).
For the bond market indices, the best performing weighting schemes belong almost exclu-
sively to the CV-EMA type. Notably, the best performing weighting scheme for timing the
Long-Term Government Bond index has a decay factor of 1.00 which means that the best
performing trading rule in out-of-sample tests can be implemented as P-SMA(k) rule. An-
other observation that is worth mentioning is that market timing does not work at all on
the Long-Term Government Bond index. Even the best performing rule in this case has the
same Sharpe ratio as that of the passive strategy (which amounts to 0.29). In contrast, for the
Intermediate-TermGovernmentBondindextheSharperatiosofthebestperformingweighting
schemes exceed the Sharpe ratio of the passive strategy (that is equal to 0.43) by 0.07-0.09.
Yet,noneoftheweightingschemesproducestheperformancewhichisstatisticallysigni(cid:12)cantly
better than that of the passive strategy. Interestingly, for this bond index the mean size of
the averaging window is much smaller than that for any other index in our empirical study.
Another interesting observation is that the 5th best performing weighting scheme is of the
HS-EMA type with a decay factor of 1.00. The major types among the top 10 best perform-
27
Electronic copy available at: https://ssrn.com/abstract=2585056

Weighting Average size Decay Difference
Rank P-value
Scheme k+1 (cid:21) ∆SR
Panel A: Standard and Poor’s Composite
1 HS-EMA 9.07 1.00 0.15 0.06
2 HS-EMA 8.88 0.99 0.15 0.07
3 HS-EMA 9.37 0.95 0.14 0.07
4 HS-EMA 9.26 0.96 0.14 0.08
5 CC-EMA 9.86 0.82 0.13 0.08
6 HS-EMA 8.42 0.97 0.13 0.09
7 CV-EMA 9.89 0.95 0.13 0.09
8 HS-EMA 8.31 0.94 0.13 0.10
9 CV-EMA 9.38 0.94 0.12 0.10
10 HS-EMA 8.50 0.98 0.12 0.11
Panel B: Dow Jones Industrial Average
1 HS-EMA 15.05 0.82 0.06 0.27
2 CV-EMA 10.00 0.76 0.06 0.27
3 CV-EMA 10.41 0.89 0.06 0.25
4 HS-EMA 13.90 0.87 0.06 0.27
5 CC-EMA 11.85 0.23 0.06 0.28
6 CC-EMA 11.85 0.22 0.06 0.28
7 CC-EMA 11.85 0.21 0.06 0.28
8 CV-EMA 10.00 0.77 0.06 0.28
9 CC-EMA 12.15 0.98 0.05 0.28
10 HS-EMA 14.18 0.85 0.05 0.28
Panel C: Long-Term Government Bonds
1 CV-EMA 11.86 1.00 0.00 0.50
2 CV-EMA 10.06 0.68 -0.00 0.52
3 CV-EMA 9.86 0.63 -0.01 0.54
4 CC-EMA 10.81 0.32 -0.01 0.54
5 CC-EMA 10.81 0.31 -0.01 0.54
6 CV-EMA 8.84 0.62 -0.01 0.55
7 CV-EMA 8.59 0.71 -0.01 0.56
8 CV-EMA 8.55 0.65 -0.01 0.57
9 CC-EMA 9.00 0.96 -0.02 0.58
10 CV-EMA 9.27 0.69 -0.02 0.59
Panel D: Intermediate-Term Government Bonds
1 CV-EMA 4.38 0.68 0.09 0.14
2 CV-EMA 4.27 0.71 0.09 0.16
3 CV-EMA 4.49 0.73 0.09 0.16
4 CV-EMA 4.71 0.72 0.09 0.16
5 HS-EMA 5.31 1.00 0.08 0.17
6 CV-EMA 5.09 0.84 0.08 0.19
7 CV-EMA 4.00 0.54 0.07 0.21
8 CV-EMA 5.87 0.83 0.07 0.20
9 CV-EMA 5.01 0.66 0.07 0.21
10 CV-EMA 8.59 0.62 0.07 0.21
Table 1: For each index, this table reports the top 10 best performing weighting schemes (out of
total 300 tested) in our out-of-sample tests. Rank denotes the rank of a weighting scheme; the best
performingschemeisassignedthe1strank. Averagesizek+1denotesthemeanvalueofk+1overthe
out-of-sampleperiod. Weighting schemedenotesthetypeoftheweightingscheme. Decay (cid:21)reports
thevalueofthedecayfactorintheweightingscheme. Difference ∆SRdenotesthedifferencebetween
the Sharpe ratio of the trading rule (associated with the weighting scheme) and the Sharpe ratio of its
passive counterpart. P-value denotes the p-value of testing the null hypothesis H :∆SR(cid:20)0.
0
ing weighting schemes for the Long-Term Government Bond index and the Intermediate-Term
Government Bond index are illustrated in Figure 3, Panels C and D respectively.
28
Electronic copy available at: https://ssrn.com/abstract=2585056

0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 9
Lag
thgieW
Method
HS−EMA, Decay=1.0
CC−EMA, Decay=0.82
CV−EMA, Decay=0.95 0.2
0.1
0.0
0 1 2 3 4 5 6 7 8 9
Lag
thgieW
Method
HS−EMA, Decay=0.82
CV−EMA, Decay=0.76
CC−EMA, Decay=0.23
Panel A: Standard and Poor’s Composite Panel B: Dow Jones Industrial Average
0.3
0.2
0.1
0.0
0 1 2 3 4 5 6 7 8 9
Lag
thgieW
0.5
Method
CV−EMA, Decay=1.00
CV−EMA, Decay=0.68 0.4
CC−EMA, Decay=0.32
0.3
0.2
0.1
0.0
0 1 2 3 4
Lag
thgieW
Method
CV−EMA, Decay=0.68
HS−EMA, Decay=1.00
CV−EMA, Decay=0.54
Panel C: Long-Term Government Bonds Panel D: Intermediate-Term Government Bonds
Figure 3: For each index, this (cid:12)gure provides illustrations of 3 major types of weighting schemes that
belong to the top 10 best performing schemes in out-of-sample tests. Lag denotes the weight of the lag
∆P t(cid:0)i , where Lag0 denotes the most recent price change.
4.4 Discussion
Because of the marginal differences in the performances of the top 10 best weighting schemes
in out-of-sample tests, and because of the fact that virtually for every (cid:12)nancial index in our
studyeachmajortypeoftheweightingschemehappenstobeamongthetop10, itisextremely
difficulttodrawgeneralconclusionsaboutwhattypeoftheweightingschemeproducesthebest
performance. Forpractitioners,itiscomfortingtoknowthatthepopularDCMrule,whereone
uses 50-day and 200-day simple moving averages, is very close to the best performing rule for
timing the Standard and Poor’s 500 index. Zakamulin (2015) entertains a method of (cid:12)nding
the most robust moving average weighting scheme, where \robustness" of a weighting scheme
is de(cid:12)ned as its ability to generate sustainable performance under all possible market scenarios
regardless of the size of the averaging window. He (cid:12)nds that the CV-EMA weighting scheme
with a decay factor of 0.85-0.90 produces the most robust performance. The same type of the
weighting scheme with decay factors that are close to the range of 0.85-0.90 can also be found
29
Electronic copy available at: https://ssrn.com/abstract=2585056

among the top 10 best for all (cid:12)nancial indices in our study except the Long-Term Government
Bond index.
Excluding the Intermediate-Term Government Bond index, the mean size of the averaging
window, k+1, is close to the most often used size of 10 months (200 days). Practitioners also
(cid:12)nd this information comforting to know. Yet, practitioners should be aware of the fact that
there is no single size of the averaging window that works best for any (cid:12)nancial index at any
given time. We have evidence that the optimal size of the averaging window is time-varying.
Last but not least, the results of our empirical study agree with the conclusions reached in
thestudybyZakamulin(2014). Speci(cid:12)cally,onlyfortheStandardandPoor’sCompositeindex
we (cid:12)nd weak evidence12 that the best performing weighting schemes are able to outperform
the passive strategy. Additionally, for 2 out of 4 (cid:12)nancial indices the top 10 best weighting
schemes outperform the passive benchmark in terms of the value of their Sharpe ratio. Yet,
thereisnostatisticalevidenceofoutperformance. FortheLong-TermGovernmentBondindex
we(cid:12)ndthatthebestperformingweightingschemesarenotabletobeatthepassivebenchmark
even in terms of the value of the Sharpe ratio.
5 Conclusions
In this paper we present the methodology to study the computation of trading indicators in
many market timing rules based on moving averages of prices and analyze the commonalities
anddifferencesbetweentherules. Ouranalysisrevealsthatthecomputationofeverytechnical
trading indicator considered in this paper can equivalently be interpreted as the computation
of the weighted average of price changes over the averaging window. Despite a great variety of
trading indicators that are computed seemingly differently at the (cid:12)rst sight, we (cid:12)nd that the
only real difference between the diverse trading indicators lies in the shape of the weighting
function used to compute the moving average of price changes. The most popular trading
indicators employ either equal-weighting of price changes, overweighting the most recent price
changes, or a hump-shaped weighting function with underweighting both the most recent and
most distant price changes. The trading indicators basically vary only by the degree of over-
and under-weighting the most recent price changes.
12The evidence is \weak" because we can reject the null hypothesis only at the 10% level. Note also that we
perform a one-tailed test which produces lower p-values as compared to a two-tailed test.
30
Electronic copy available at: https://ssrn.com/abstract=2585056

As a straightforward practical application of our analysis, in this paper we perform a
comprehensive out-of-sample test of 300 different shapes of the moving average weighting
function using historical data on four (cid:12)nancial market indices. These 300 shapes are chosen to
represent different variations of a few most typical shapes of the weighting functions used in
market timing with moving averages. The results of our tests suggest answers to long-standing
questions about optimal types of moving averages and whether the best performing weighting
scheme can beat the passive counterpart in out-of-sample tests.
Unfortunately, we (cid:12)nd no clear-cut answer to the (cid:12)rst question. Yet, practitioners (cid:12)nd it
comfortingtoknowthatthepopulardouble-crossovermethod, whereoneuses50-dayand200-
day simple moving averages, is very close to the best performing rule for timing the Standard
and Poor’s 500 index. Another well performing weighting scheme in out-of-sample tests is
the convex exponential moving average of price changes with a decay factor that lies in the
range 0.85-0.95 (for monthly data). Practitioners also (cid:12)nd it comforting to know that for the
majority of indices in our study the mean size of the averaging window is close to the most
often used size of 10 months (200 days).
Regardingtheanswertothesecondquestion, onlyforoneindexwe(cid:12)ndweakevidencethat
the best performing weighting schemes outperform the passive strategy in out-of-sample tests.
Forallother(cid:12)nancialindicesinourstudythereisnostatisticallysigni(cid:12)cantevidenceofmarket
timingoutperformanceevenforthebestperformingweightingschemes. Thereforetheresultsof
ourempiricalstudyareinsharpcontrastwiththe(cid:12)ndingsreportedinthemajorityofprevious
studies where the authors document that \market timing works". Our (cid:12)ndings reaffirm the
following conclusion reached in the two previous studies where the researchers implement out-
of-sample tests of pro(cid:12)tability of some trading rules in the stock market (Sullivan et al. (1999)
andZakamulin(2014)): thepro(cid:12)tabilityofmarkettimingishighlyoverstated, tosaytheleast.
31
Electronic copy available at: https://ssrn.com/abstract=2585056

References
Beekhuizen,P.andHallerbach,W.G.(2015). \UncoveringTrendRules", Whitepaper,Robeco
Asset Management.
Brock, W., Lakonishok, J., and LeBaron, B. (1992). \Simple Technical Trading Rules and the
Stochastic Properties of Stock Returns", Journal of Finance, 47(5), 1731{1764.
Brown, S. J., Goetzmann, W. N., and Kumar, A. (1998). \The Dow Theory: William Peter
Hamilton’s Track Record Reconsidered", Journal of Finance, 53(4), 1311{1333.
Clare, A., Seaton, J., Smith, P. N., and Thomas, S. (2013). \Breaking Into the Blackbox:
Trend Following, Stop losses and the Frequency of Trading - The Case of the S&P500",
Journal of Asset Management, 14(3), 182{194.
Ellis, C. A. and Parbery, S. A. (2005). \Is Smarter Better? A Comparison Of Adaptive, And
Simple Moving Average Trading Strategies", Research in International Business and
Finance, 19(3), 399 { 411.
Faber, M. T. (2007). \A Quantitative Approach to Tactical Asset Allocation", Journal of
Wealth Management, 9(4), 69{79.
Fi(cid:12)eld, S. G. M., Power, D. M., and Knipe, D. G. S. (2008). \The Performance Of Moving
AverageRulesInEmergingStockMarkets", Applied Financial Economics,18(19),1515{
1532.
Gwilym, O., Clare, A., Seaton, J., and Thomas, S. (2010). \Price and Momentum as Robust
Tactical Approaches to Global Equity Investing", Journal of Investing, 19(3), 80{91.
Hong, K. J. and Satchell, S. (2015). \Time Series Momentum Trading Strategy and Autocor-
relation Ampli(cid:12)cation", Quantitative Finance, 15(9), 1471{1487.
Jobson, J. D. and Korkie, B. M. (1981). \Performance Hypothesis Testing with the Sharpe
and Treynor Measures", Journal of Finance, 36(4), 889{908.
Kilgallen, T. (2012). \Testing the Simple Moving Average across Commodities, Global Stock
Indices, and Currencies", Journal of Wealth Management, 15(1), 82{100.
Kirkpatrick, C. D. and Dahlquist, J. (2010). Technical Analysis: The Complete Resource for
Financial Market Technicians. FT Press; 2nd edition.
Lo, A. W., Mamaysky, H., and Wang, J. (2000). \Foundations of Technical Analysis: Compu-
tational Algorithms, Statistical Inference, and Empirical Implementation", The Journal
of Finance, 55(4), 1705{1770.
Marshall, B. R., Cahan, R. H., and Cahan, J. M. (2008). \Can Commodity Futures Be
Pro(cid:12)tably Traded With Quantitative Market Timing Strategies?", Journal of Banking
and Finance, 32(9), 1810 { 1819.
32
Electronic copy available at: https://ssrn.com/abstract=2585056

Memmel, C. (2003). \Performance Hypothesis Testing with the Sharpe Ratio", Finance
Letters, 1, 21{23.
Metghalchi, M., Marcucci, J., and Chang, Y.-H. (2012). \Are Moving Average Trading Rules
Pro(cid:12)table? Evidence From The European Stock Markets", Applied Economics, 44(12),
1539{1559.
Moskowitz, T. J., Ooi, Y. H., and Pedersen, L. H. (2012). \Time Series Momentum", Journal
of Financial Economics, 104(2), 228{250.
Murphy, J. J. (1999). Technical Analysis of the Financial Markets: A Comprehensive Guide
to Trading Methods and Applications. New York Institute of Finance.
Neely, C., Weller, P., and Dittmar, R. (1997). \Is Technical Analysis in the Foreign Ex-
change Market Pro(cid:12)table? A Genetic Programming Approach", Journal of Financial
and Quantitative Analysis, 32, 405{426.
Neuhierl,A.andSchlusche,B.(2011). \DataSnoopingandMarket-TimingRulePerformance",
Journal of Financial Econometrics, 9(3), 550{587.
Okunev, J. and White, D. (2003). \Do Momentum-Based Strategies Still Work in Foreign
Currency Markets?", Journal of Financial and Quantitative Analysis, 38(2), 425{447.
P(cid:127)at(cid:127)ari, E. and Vilska, M. (2014). \Performance of Moving Average Trading Strategies over
Varying Stock Market Conditions: the Finnish Evidence", Applied Economics, 46(24),
2851{2872.
Ready, M. J. (2002). \Pro(cid:12)ts from Technical Trading Rules", Financial Management, 31(3),
43{61.
Sharpe, W. F. (1994). \The Sharpe Ratio", Journal of Portfolio Management, 21(1), 49{58.
Sullivan, R., Timmermann, A., and White, H. (1999). \Data-Snooping, Technical Trading
Rule Performance, and the Bootstrap", Journal of Finance, 54(5), 1647{1691.
Welch, I. and Goyal, A. (2008). \A Comprehensive Look at the Empirical Performance of
Equity Premium Prediction", Review of Financial Studies, 21(4), 1455{1508.
Zakamulin, V. (2014). \The Real-Life Performance of Market Timing with Moving Average
and Time-Series Momentum Rules", Journal of Asset Management, 15(4), 261{278.
Zakamulin, V. (2015). \Market Timing With a Robust Moving Average", Working paper,
University of Agder.
Zhu, Y. and Zhou, G. (2009). \Technical Analysis: An Asset Allocation Perspective On The
Use Of Moving Averages", Journal of Financial Economics, 92(3), 519 { 544.
33
Electronic copy available at: https://ssrn.com/abstract=2585056
