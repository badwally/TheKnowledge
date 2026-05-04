---
id: pdf-lasse-pedersen-2011-title-how-to
type: pdf
title: 'Title: “How to Manage Managed Futures” or “The Way of the Futures”'
url: ''
authors:
- Lasse Pedersen
ingested_at: '2026-04-29T16:25:30Z'
content_hash: sha256:2da8cf4e018a914e2ddb2d086129ada5c6c384c6395b458cc2a8611c463810c0
source_path: raw/pdf/pdf-lasse-pedersen-2011-title-how-to.pdf
domains:
- trading-and-markets
nlm_corpus_ids:
- ccbda94f-7251-42bb-864f-0e1c9850f7ad
wiki_pages:
- wiki/entities/tobias-moskowitz.md
- wiki/entities/yao-hua-ooi.md
- wiki/entities/lasse-h-pedersen.md
- wiki/concepts/time-series-momentum.md
- wiki/concepts/speculator-hedger-momentum-transfer.md
- wiki/entities/university-of-chicago-booth.md
meta:
  page_count: 62
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/SSRN-id2089463.pdf
published_at: '2011'
---
Working Paper No. 79
Chicago Booth Paper No. 12-21
Time Series Momentum
Tobias Moskowitz
Booth School of Business, University of Chicago and NBER
Yao Hua Ooi
AQR Capital Management
Lasse H. Pedersen
New York University, Copenhagen Business School, NBER,
CEPR, and AQR Capital Management
Initiative on Global Markets
The University of Chicago, Booth School of Business
“Providing thought leadership on international business, financial markets and public policy”
This paper also can be downloaded without charge from the
Social Science Research Network Electronic Paper Collection:
http://ssrn.com/abstract=2089463
EEElleeleccctttrrrooonnniiccic cccooopppyyy aaavvvaaaiilliaalabbblleele aaattt::: hhhttttttpppss::://////ssssssrrrnnn...cccooommm///aaabbbssstttrrraaacccttt===222000888999444666333

Time Series Momentum
Tobias Moskowitz
Yao Hua Ooi
Lasse H. Pedersen1
This version: September, 2011
Abstract
We document significant “time series momentum” in equity index, currency, commodity,
and bond futures for each of the 58 liquid instruments we consider. We find persistence
in returns for 1 to 12 months that partially reverses over longer horizons, consistent with
sentiment theories of initial under-reaction and delayed over-reaction. A diversified
portfolio of time series momentum strategies across all asset classes delivers substantial
abnormal returns with little exposure to standard asset pricing factors and performs best
during extreme markets. Examining the trading activities of speculators and hedgers, we
find that speculators profit from time series momentum at the expense of hedgers.
1 Moskowitz is at the University of Chicago Booth School of Business and NBER, Ooi is at AQR Capital
Management, and Pedersen is at New York University, Copenhagen Business School, NBER, CEPR, and
AQR Capital Management. We thank Cliff Asness, Nick Barberis, Gene Fama, John Heaton, Ludger
Hentschel, Brian Hurst, Andrew Karolyi, John Liew, Matt Richardson, Richard Thaler, Robert Vishny,
Robert Whitelaw, and Jeff Wurgler for useful suggestions and discussions, and Ari Levine and Haibo Lu
for excellent research assistance. Moskowitz thanks the Initiative on Global Markets at the University of
Chicago Booth School of Business and CRSP for financial support.
EEElleeleccctttrrrooonnniiccic cccooopppyyy aaavvvaaaiilliaalabbblleele aaattt::: hhhttttttpppss::://////ssssssrrrnnn...cccooommm///aaabbbssstttrrraaacccttt===222000888999444666333

1. Introduction: a trending walk down Wall Street
We document an asset pricing anomaly we term “time series momentum,” which
is remarkably consistent across very different asset classes and markets. Specifically, we
find strong positive predictability from a security’s own past returns for a large set
(almost five dozen) of diverse futures and forward contracts that include country equity
indices, currencies, commodities, and sovereign bonds over more than 25 years of data.
We find that the past 12 month excess return of each instrument is a positive predictor of
its future return. This time series momentum or “trend” effect persists for about a year
and then partially reverses over longer horizons. These findings are robust across a
number of sub-samples, look-back periods, and holding periods. We find that 12-month
time series momentum profits are positive not just on average across these assets, but for
every asset contract we examine (58 in total).
Time series momentum is related to, but different from, the phenomenon known
as “momentum” in the finance literature, which is primarily cross-sectional in nature.
The momentum literature focuses on the relative performance of securities in the cross-
section, finding that securities that recently outperformed their peers over the past 3 to 12
months continue to outperform their peers on average over the next month.2 Rather than
2 Cross-sectional momentum has been documented in U.S. equities (Jegadeesh and Titman, 1993; Asness,
1994), other equity markets (Rouwenhorst, 1998), industries (Moskowitz and Grinblatt, 1999), equity
indices (Asness, Liew, and Stevens, 1997; Bhojraj and Swaminathan, 2006), currencies (Shleifer and
Summers, 1990), commodities (Erb and Harvey, 2006; Gorton, Hayashi, and Rouwenhorst, 2008), and
global bond futures (Asness, Moskowitz, and Pedersen, 2010). Garleanu and Pedersen (2009) show how to
trade optimally on momentum and reversal in light of transaction costs, and DeMiguel, Nogales, and Uppal
(2010) show how to construct an optimal portfolio based on stocks’ serial dependence and find
outperformance out-of-sample. Our study is related to but different from Asness, Moskowitz, and Pedersen
(2010) who study cross-sectional momentum and value strategies across several asset classes including
individual stocks. We complement their study by examining time series momentum and its relation to
cross-sectional momentum and hedging pressure in some of the same asset classes.
1
EEElleeleccctttrrrooonnniiccic cccooopppyyy aaavvvaaaiilliaalabbblleele aaattt::: hhhttttttpppss::://////ssssssrrrnnn...cccooommm///aaabbbssstttrrraaacccttt===222000888999444666333

focus on the relative returns of securities in the cross-section, time series momentum
focuses purely on a security’s own past return.
We argue that time series momentum directly matches the predictions of many
prominent behavioral and rational asset pricing theories. Barberis, Shleifer, and Vishny
(1998), Daniel, Hirshleifer, and Subrahmanyam (1998), and Hong and Stein (1999) all
focus on a single risky asset, therefore having direct implications for time series, rather
than cross-sectional, predictability. Likewise, rational theories of momentum (Berk,
Green, and Naik, 1999; Johnson, 2002; Ahn, Conrad, and Dittmar, 2003; Liu and Zhang,
2008; and Sagi and Seasholes, 2007) also pertain to a single risky asset.
Our finding of positive trends that partially reverse over the long-term may be
consistent with initial under-reaction and delayed over-reaction, which theories of
sentiment suggest can produce these return patterns.3 However, our results also pose
several challenges to these theories. First, we find that the correlations of time series
momentum strategies across asset classes are larger than the correlations of the asset
classes themselves. This suggests a stronger common component to time series
momentum across different assets than is present among the assets themselves. Such a
correlation structure is not addressed by existing behavioral models. Second, very
different types of investors in different asset markets are producing the same patterns at
the same time. Third, we fail to find a link between time series momentum and measures
3 Underreaction can result from the slow diffusion of news (Hong and Stein, 1999), conservativeness and
anchoring biases (Barberis, Shleifer, and Vishny, 1998; Edwards, 1968), or the disposition effect to sell
winners too early and ride losers too long (Shefrin and Statman, 1985; Frazzini, 2006). Over-reaction can
be caused by positive feedback trading (De Long, Shleifer, Summers, and Waldmann, 1990; Hong and
Stein, 1999), over-confidence and self-attribution confirmation biases (Daniel, Hirshleifer, and
Subrahmanyam, 1998), the representativeness heuristic (Barberis, Shleifer, and Vishny, 1998; Tversky and
Kahneman, 1974), herding (Bikhchandani, Hirshleifer, and Welch, 1992), or general sentiment (Baker and
Wurgler, 2006, 2007).
2
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

of investor sentiment used in the literature (Baker and Wurgler, 2006; Qiu and Welch,
2006).
To understand the relationship between time series and cross-sectional
momentum, their underlying drivers, and relation to theory, we decompose the returns to
a time series and cross-sectional momentum strategy following the framework of Lo and
MacKinlay (1990) and Lewellen (2002). This decomposition allows us to identify the
properties of returns that contribute to these patterns, and what features are common and
unique to the two strategies. We find that positive auto-covariance in futures contracts'
returns drives most of the time series and cross-sectional momentum effects we find in
the data. The contribution of the other two return components—serial cross-correlations
and variation in mean returns—is small. Negative serial cross-correlations (i.e., lead-lag
effects across securities), which affect cross-sectional momentum but not time series
momentum, are negligible and of the “wrong” sign among our instruments. The
contribution from mean returns of the assets is also small. Our finding that time series
and cross-sectional momentum profits arise due to auto-covariances is consistent with the
theories mentioned above.4 In addition, we find that time series momentum captures the
returns associated with individual stock (cross-sectional) momentum, most notably Fama
and French's UMD factor, despite time series momentum being constructed from a
completely different set of securities. This finding indicates strong correlation structure
between time series momentum and cross-sectional momentum even when applied to
4 However, this result differs from Lewellen’s (2002) finding for equity portfolio returns that temporal
lead-lag effects, rather than auto-covariances, appear to be the most significant contributor to cross-
sectional momentum. Chen and Hong (2002) provide a different interpretation and decomposition of the
Lewellen (2002) portfolios that is consistent with auto-covariance being the primary driver of stock
momentum.
3
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

different assets and suggests that our time series momentum portfolio captures individual
stock momentum.
To better understand what might be driving time series momentum, we examine
the trading activity of speculators and hedgers around these return patterns using weekly
position data from the Commodity Futures Trading Commission (CFTC). We find that
speculators trade with time series momentum, being positioned on average to take
advantage of the positive trend in returns for the first 12 months and reducing their
positions at the time when the trend begins to reverse. Consequently, speculators appear
to be profiting from time series momentum, and its eventual reversal, at the expense of
hedgers. Using a vector auto-regression (VAR), we confirm that speculators trade in the
same direction as a return shock and reduce their positions as the shock dissipates,
whereas hedgers take the opposite side of these trades.
Finally, we decompose time series momentum into the component coming from
spot price predictability versus the “roll yield” stemming from the shape of the futures
curve. While spot price changes are mostly driven by information shocks, the roll yield
can be driven by liquidity and price pressure effects in futures markets that affect the
return to holding futures without necessarily changing the spot price. Hence, this
decomposition may be a way to distinguish the effects of information dissemination from
hedging pressure. We find that both of these effects contribute to time series momentum,
but only spot price changes are associated with long-term reversals, consistent with the
idea that investors may be overreacting to information in the spot market but that hedging
pressure is more long-lived and not affected by over-reaction.
4
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Our finding of time series momentum in virtually every instrument we examine
seems to challenge the “random walk” hypothesis, which in its most basic form implies
that knowing whether a price went up or down in the past should not be informative
about whether it will go up or down in the future. While rejection of the random walk
hypothesis does not necessarily imply a rejection of a more sophisticated notion of
market efficiency with time-varying risk premia, we further show that a diversified
portfolio of time series momentum across all assets is remarkably stable and robust,
yielding a Sharpe ratio greater than one on an annual basis, or roughly 2.5 times the
market Sharpe ratio, with little correlation to passive benchmarks in each asset class or a
host of standard asset pricing factors. The abnormal returns to time series momentum
also do not appear to be compensation for crash risk or tail events. Rather, their returns
are largest when the stock market's returns are most extreme—performing best when the
market experiences large up and down moves. Hence, time series momentum may be a
hedge for extreme events, making its large return premium even more puzzling from a
risk-based perspective. The robustness of time series momentum for very different asset
classes and markets suggest that our results are likely not spurious, and the relatively
short duration of the predictability (less than a year) and the magnitude of the return
premium associated with time series momentum present significant challenges to the
random walk hypothesis and perhaps also to the efficient market hypothesis, though we
cannot rule out the existence of a rational theory that can explain these findings.
Our study relates to the literature on return autocorrelation and variance ratios that
also finds deviations from the random walk hypothesis (Fama and French, 1988; Lo and
MacKinlay, 1988; Poterba and Summers, 1988). While this literature is largely focused
5
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

on U.S. and global equities, Cutler, Poterba and Summers (1991) study a variety of assets
including housing and collectibles. The literature finds positive return autocorrelations at
daily, weekly, and monthly horizons and negative autocorrelations at annual and multi-
year frequencies. We complement this literature in several ways. The studies of
autocorrelation examine, by definition, return predictability where the length of the
“look-back period” is the same as the “holding period” over which returns are predicted.
This restriction masks significant predictability that is uncovered once look-back periods
are allowed to differ from predicted or holding periods. In particular, our result that the
past 12 months of returns strongly predicts returns over the next 1 month is missed by
looking at one year autocorrelations. While return continuation can also be detected
implicitly from variance ratios, we complement the literature by explicitly documenting
the extent of return continuation and by constructing a time series momentum factor that
can help explain existing asset pricing phenomena, such as cross-sectional momentum
premia and hedge fund macro and managed futures returns. Also, a significant
component of the higher frequency findings in equities are contaminated by market
micro-structure effects such as stale prices (Richardson, 1993; Ahn, Boudoukh,
Richardson, and Whitelaw, 2002). Focusing on liquid futures instead of individual stocks
and looking at lower frequency data (one year) mitigates many of these issues. Finally,
unique to this literature, we link time series predictability to the dynamics of hedger and
speculator positions and decompose returns into price changes and roll yields.
Our paper is also related to the literature on hedging pressure in commodity
futures (Keynes, 1923; Fama and French, 1987; Bessembinder, 1992; and de Roon,
Nijman, and Veld, 2000). We complement this literature by showing how hedger and
6
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

speculator positions relate to past futures returns, finding that speculators’ positions load
positively on time series momentum, while hedger positions load negatively on it. Also,
we consider the relative return predictability of positions, past price changes, and past roll
yields. Gorton, Hayashi, and Rouwenhorst (2008) also link commodity momentum and
speculator positions to the commodities’ inventories.
The rest of the paper is organized as follows. Section 2 describes our data on
futures returns and the positioning of hedgers and speculators. Section 3 documents time
series momentum at the one year horizon and reversals beyond one year. We also
examine the correlation of time series momentum strategies within and across asset
classes, their relation to other known return factors, and their performance during extreme
markets, relating our findings to rational risk-based and behavioral asset pricing models.
Section 4 examines the relation between time series and cross-sectional momentum.
Section 5 studies the evolution of time series momentum and its relation to investor
speculative and hedging positions. Section 6 concludes.
2. Data and preliminaries
We describe briefly the various data sources we use in our analysis.
2.1. Futures returns
Our data consists of futures prices for the 24 commodity futures in the S&P GSCI
(GSCI) index, 12 cross-currency pairs (from 9 underlying currencies), 9 developed equity
indices, and 13 developed government bond futures, from January 1965 through
December 2009. These instruments are among the most liquid futures contracts in the
7
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

world.5 We focus on the most liquid instruments to avoid returns being contaminated by
illiquidity or stale price issues and to match more closely an implementable strategy at a
significant trade size. Appendix A provides details on each instrument and their data
sources, which are mainly Datastream, Bloomberg, and various exchanges.
We construct a return series for each instrument as follows. Each day, we
compute the daily excess return of the most liquid futures contract (typically the nearest
or next nearest to delivery contract), and then compound the daily returns to a cumulative
return index from which we can compute returns at any horizon. For the equity indices,
our return series are almost perfectly correlated with the corresponding returns of the
underlying cash indices in excess of the Treasury bill rate.6
As a robustness test, we also do our analysis using the “far” futures contract (the
next maturity after the most liquid one). For the commodity futures, time series
momentum profits are in fact slightly stronger for the far contract, and, for the financial
futures, time series momentum returns hardly change if we use far futures.
Table 1 presents summary statistics of the excess returns on our futures contracts.
The first column shows when the time series of returns for each asset starts, and the next
two columns report the time series mean (arithmetic) and standard deviation (annualized)
of each contract by asset class: commodities, equity indices, bonds, and currencies. As
Table 1 highlights, there is significant variation in sample mean returns across the
different contracts. Equity index, bonds, and currencies yield predominantly positive
5 We also confirm the time series momentum returns are robust among more illiquid instruments such as
illiquid commodities (feeder cattle, Kansas wheat, lumber, orange juice, rubber, tin), emerging market
currencies and equities, and more illiquid fixed income futures (not reported).
6 Bessembinder (1992) and de Roon, Nijman, and Veld (2000) compute returns on futures contracts
similarly and also find that futures returns are highly correlated with spot returns on the same underlying
asset.
8
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

excess returns, while various commodity contracts yield positive, zero, and even negative
excess average returns over the sample period. Only the equity and bond futures exhibit
statistically significant and consistent positive excess average returns.
More striking are the differences in volatilities across the contracts. Not
surprisingly, commodities and equities have much larger volatilities than bond futures or
currency forward contracts. But, even among commodities, there is substantial cross-
sectional variation in volatilities. Making comparisons across instruments with vastly
different volatilities or combining various instruments into a diversified portfolio when
they have wide-ranging volatilities is challenging. For example, the volatility of natural
gas futures is about 50 times larger than that of 2-year US bond futures. We discuss
below how we deal with this issue in our analysis.
2.2. Positions of traders
We also use data on the positions of speculators and hedgers from the Commodity
Futures Trading Commission (CFTC) as detailed in Appendix A. The CFTC requires all
large traders to identify themselves as commercial or non-commercial which we, and the
previous literature (e.g., Bessembinder, 1992; de Roon, Nijman, and Veld, 2000), refer to
as hedgers and speculators, respectively. For each futures contract, the long and short
open interest held by these traders on Tuesday are reported on a weekly basis.7
Using the positions of speculators and hedgers as defined by the CFTC, we define
the Net Speculator Position for each asset as follows:
Speculator Long Positions - Speculator Short Positions
Net Speculator Position =
Open Interest
7 While commercial traders likely predominantly include hedgers, some may also be speculating, which
introduces some noise into the analysis in terms of our classification of speculative and hedging trades.
However, the potential attenuation bias associated with such misclassification may only weaken our results.
9
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

This signed measure shows whether speculators are net long or short in aggregate, and
scales their net position by the open interest or total number of contracts outstanding in
that futures market. Since speculators and hedgers approximately add up to zero (except
for a small difference denoted “non-reported” due to measurement issues of very small
traders), we focus our attention on speculators. Of course, this means that net hedger
positions constitute the opposite side (i.e., the negative of Net Speculator Position).
The CFTC positions data does not cover all of the futures contracts we have
returns for and consider in our analysis. Most commodity and foreign exchange contracts
are covered, but only the U.S. instruments among the stock and bond futures contracts are
covered. The third and fourth columns of Table 1 report summary statistics on the
sample of futures contracts with net speculator positions in each contract over time.
Speculators are net long on average, and hence hedgers are net short, for most of the
contracts, a result consistent with Bessembinder (1992) and de Roon, Nijman, and Veld
(2000) for a smaller set of contracts over a shorter time period. All but one of the
commodities (natural gas) have net long speculator positions over the sample period, with
silver exhibiting the largest average net long speculator position. This is consistent with
Keynes’ (1923) conjecture that producers of commodities are the primary hedgers in
markets and are on the short side of these contracts as a result. For the other asset
classes, other than the S&P 500, the 30-year U.S. Treasury bond and the $US/Japanese
and $US/Swiss exchange rates, speculators exhibit net long positions on average. Table
1 also highlights that there is substantial variation over time in net speculator positions
per contract and across contracts. Not surprisingly, the standard deviation of net
speculator positions is positively related to the volatility of the futures contract itself.
10
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

2.3. Asset pricing benchmarks
We evaluate the returns of our strategies relative to standard asset pricing
benchmarks, namely the MSCI World equity index, Barclay’s Aggregate Bond Index,
S&P GSCI Index (GSCI), all of which we obtain from Datastream, the long-short factors
SMB, HML, and UMD from Ken French’s website, and the long-short value and cross-
sectional momentum factors across asset classes from Asness, Moskowitz, and Pedersen
(2010).
2.4. Ex-ante volatility estimate
Since volatility varies dramatically across our assets (illustrated in Table 1), we
scale the returns by their volatilities in order to make meaningful comparisons across
assets. We estimate each instrument’s ex-ante volatility σ at each point in time using an
t
extremely simple model: the exponentially-weighted lagged squared daily returns (i.e.,
similar to a simple univariate GARCH model). Specifically, the ex ante annualized
variance σ2 for each instrument is calculated as follows:
t
∞
σ2 =261⋅∑(1−δ)δi( r −r )2 (1)
t t−1−i t
i=0
where the scalar 261 scales the variance to be annual, the weights (1−δ)δi add up to 1,
and r is the exponentially weighted average return computed similarly. The parameter δ
t
is chosen so that the center of mass of the weights is ∞ δ days. The
∑ (1−δ)δii = = 60
1−δ
i=0
volatility model is the same for all assets at all times. While all of the results in the paper
are robust to more sophisticated volatility models, we chose this model due to its
simplicity and lack of look-ahead bias in the volatility estimate. To ensure no look-ahead
11
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

bias contaminates our results, we use the volatility estimates at time t-1 applied to time t
returns throughout the analysis.
3. Time Series Momentum: Regression analysis and trading strategies
We start by examining the time series predictability of futures returns across
different time horizons.
3.1. Regression analysis: Predicting price continuation and reversal
We regress the excess return rs for instrument s in month t on its return lagged h
t
months, where both returns are scaled by their ex ante volatilities σs (defined above in
t−1
Section 2.D.):
rs /σs =α++βrs /σs εs (2)
t t−1 h t−h t−h−1 t
Given the vast differences in volatilities (as shown in Table 1), we divide all returns by
their volatility to put them on the same scale. This is similar to using Generalized Least
Squares instead of Ordinary Least Squares.8 Stacking all futures contracts and dates, we
run a pooled panel regression and compute t-statistics that account for group-wise
clustering by time (at the monthly level). The regressions are run using lags of h = 1, 2, ...
60 months.
Panel A of Figure 1 plots the t-statistics from the pooled regressions by month lag
h. The positive t-statistics for the first 12 months indicate significant return continuation
or trends. The negative signs for the longer horizons indicate reversals, the most
significant of which occur in the year immediately following the positive trend.
8 The regression results are qualitatively similar if we run OLS without adjusting for each security’s
volatility. This also produces statistically significant time series momentum at horizons less than a year and
reversal at longer horizons.
12
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Another way to look at time series predictability is to simply focus only on the
sign of the past excess return. This even simpler way of looking at time series momentum
underlies the trading strategies we consider in the next section. In a regression setting,
this strategy can be captured using the following specification:
rs /σs =α++βsign ( rs ) εs (3)
t t−1− h t h t
We again make the left-hand side of the regression independent of volatility (the right-
hand side is too since sign is either +1 or -1), so that the parameter estimates are
comparable across instruments. We report the t-statistics from a pooled regression with
standard errors clustered by time (i.e., month) in Panel B of Figure 1.
The results are similar across the two regression specifications: strong return
continuation for the first year and weaker reversals for the next four years. In both cases,
the data exhibit a clear pattern, with all of the most recent 12-month lag returns positive
(and nine statistically significant) and the majority of the remaining lags negative.
Repeating the panel regressions for each asset class separately, we obtain the same
patterns: one to 12-month positive trends followed by smaller reversals over the next
four years as seen in Panel C of Figure 1.
3.2. Time Series Momentum trading strategies
We next investigate the profitability of a number of trading strategies based on
time series momentum. We vary both the number of months we lag returns to define the
signal used to form the portfolio (the “look-back period”) and the number of months we
hold each portfolio after it has been formed (the “holding period”).
For each instrument s and month t, we consider whether the excess return over the
past k months is positive or negative and go long the contract if positive and short if
13
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

negative, holding the position for h months. We set the position size to be inversely
proportional to the instrument’s ex-ante volatility, 1/σs , each month. Sizing each
t−1
position in each strategy to have constant ex ante volatility is helpful for two reasons.
First, it makes it easier to aggregate strategies across instruments with very different
volatility levels. Second, it is helpful econometrically to have a time series with relatively
stable volatility so that the strategy is not dominated by a few volatile periods.
For each trading strategy (k,h) we derive a single time series of monthly returns
even if the holding period h is more than one month. This is helpful when evaluating the
strategy’s performance because it means that we need not worry about overlapping
observations. We derive this single time series of returns following the methodology used
by Jegadeesh and Titman (1993): The return at time t represents the average return across
all portfolios at that time, namely the return on the portfolio that was constructed last
month, the month before that (and still held if the holding period h is greater than two),
and so on for all currently “active” portfolios.
Specifically, for each instrument, we compute the time t return based on the sign
of the past return from time t-k-1 to t-1. We then compute the time t return based on the
sign of the past return from t-k-2 to t-2, and so on until we compute the time t return
based on the final past return that is still being used from t-k-h to t-h. For each (k,h) we
get a single time series of monthly returns by computing the average return of all of these
h currently “active” portfolios (i.e., the portfolio that was just bought and those that were
bought in the past and are still held). We average the returns across all instruments (or all
instruments within an asset class), to obtain our time series momentum strategy returns,
rTS−MOM(k,h).
t
14
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

To evaluate the abnormal performance of these strategies, we compute their
alphas from the following regression:
rTS−MOM(k,h) =α+βMKT +βBOND +βGSCI +sSMB +hHML +mUMD +ε (4)
t 1 t 2 t 3 t t t t t
where we control for passive exposures to the three major asset classes—the stock market
MKT, proxied by the excess return on the MSCI World Index, the bond market BOND,
proxied by the Barclays Aggregate Bond Index, the commodity market GSCI, proxied by
the S&P GSCI Index—as well as the standard Fama-French stock market factors SMB,
HML, and UMD for the size, value, and (cross-sectional) momentum premia. For the
evaluation of time series momentum strategies, we rely on the sample starting in 1985 to
ensure that a comprehensive set of instruments have data (see Table 1) and that the
markets had significant liquidity. We obtain similar (and generally more significant)
results if older data is included going back to 1965, but given the more limited breadth
and liquidity of the instruments during this time, we report results post-1985.
Table 2 shows the t-statistic of the estimated alphas for each asset class and across
all assets. The existence and significance of time series momentum is robust across
horizons and asset classes, particularly when the look-back and holding periods are 12
months or less. In addition, we confirm that the time series momentum results are almost
identical if we use the cash indices for the stock index futures. The other asset classes do
not have cash indices.
4. Time Series Momentum factor
For a more in-depth analysis of time series momentum, we focus our attention on
a single time series momentum strategy. Following the convention used in the cross-
15
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

sectional momentum literature (and based on the results from Figure 1 and Table 2), we
focus on the properties of the 12-month time series momentum strategy with a 1-month
holding period (e.g., k = 12 and h = 1), which we refer to simply as TSMOM.
4.1. TSMOM by security and the diversified TSMOM factor
We start by looking at each instrument and asset separately and then pool all the
assets together in a diversified TSMOM portfolio. We size each position (long or short)
so that it has an ex ante annualized volatility of 40%. That is, the position size is chosen
to be 40% / σ , where σ is the estimate of the ex ante volatility of the contract as
t-1 t-1
described above. The choice of 40% is inconsequential, but it makes it easier to
intuitively compare our portfolios to others in the literature. The 40% annual volatility is
chosen because it is similar to the risk of an average individual stock, and when we
average the return across all securities (equal-weighted) to form the portfolio of securities
which represent our TSMOM factor, it has an annualized volatility of 12% per year over
the sample period 1985 to 2009, which is roughly the level of volatility exhibited by other
factors such as those of Fama and French (1993) and Asness, Moskowitz, and Pedersen
(2010).9 The TSMOM return for any instrument s at time t is therefore:
40%
rTSMOM, s = sign(rs ) rs (5)
t,t+1 t−12,t σs t,t+1
t
We compute this return for each instrument and each available month from January 1985
to December 2009. Panel A of Figure 2 plots the annualized Sharpe ratios of these
strategies for each futures contract. As the figure shows, every single futures contract
exhibits positive predictability from past one year returns. All 58 futures contracts exhibit
9 Also, this portfolio construction implies a use of margin capital of about 5-20%, which is well within
what is feasible to implement in a real-world portfolio.
16
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

positive time series momentum returns and 52 are statistically different from zero at the
5% significance level.
If we regress the TSMOM strategy for each security on the strategy of always
being long (i.e., replacing “sign” with a 1 in equation (5)), then we get a positive alpha in
90% of the cases (of which 26% are statistically significant; none of the few negative
ones are significant, not reported). Thus, a time series momentum strategy provides
additional returns over and above a passive long position in each instrument.
The overall return of the strategy that diversifies across all the S securities that
t
are available at time t is:
(cid:3020)(cid:3295)
1 40%
(cid:1870)TSMOM (cid:3404) (cid:3533)sign(cid:4666)(cid:1870)(cid:3046) (cid:4667) (cid:1870)(cid:3046)
(cid:3047),(cid:3047)(cid:2878)(cid:2869) (cid:1845) (cid:3047)(cid:2879)(cid:2869)(cid:2870),(cid:3047) (cid:2026)(cid:3046) (cid:3047),(cid:3047)(cid:2878)(cid:2869)
(cid:3047) (cid:3047)
(cid:3046)(cid:2880)(cid:2869)
We analyze the risk and return of this factor in detail next. We also consider TSMOM
strategies by asset class constructed analogously.
4.2. Alpha and loadings on risk factors
Table 3 examines the risk-adjusted performance of a diversified TSMOM strategy
and its factor exposures. Panel A of Table 3 regresses the excess return of the TSMOM
strategy on the returns of the MSCI World stock market index and the standard Fama-
French factors SMB, HML, and UMD, representing the size, value, and cross-sectional
momentum premium among individual stocks. The first row reports monthly time series
regression results and the second row uses quarterly non-overlapping returns (to account
for any non-synchronous trading effects across markets). In both cases, TSMOM
delivers a large and significant alpha or intercept with respect to these factors of about
1.58% per month or 4.75% per quarter. The TSMOM strategy does not exhibit significant
17
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

betas on the market, SMB, or HML but loads significantly positively on UMD, the cross-
sectional momentum factor. We explore the connection between cross-sectional and time
series momentum more fully in the next section, but given the large and significant alpha,
it appears that time series momentum is not fully explained by cross-sectional momentum
in individual stocks.
Panel B of Table 3 repeats the regressions using the Asness, Moskowitz, and
Pedersen (2010) value and momentum “everywhere” factors (i.e., factors diversified
across asset classes) in place of the Fama and French factors. Asness, Moskowitz, and
Pedersen (2010) form long-short portfolios of value and momentum across individual
equities from four international markets, stock index futures, bond futures, currencies,
and commodities. Similar to the Fama and French factors, these are cross-sectional
factors. Once again, we find no significant loading on the market index or the global
value factor, but significant loading on the cross-sectional momentum everywhere factor.
However, the returns to TSMOM are not fully captured by the cross-sectional
everywhere factor—the alpha is still an impressive 1.09% per month with a t-stat of 5.40
or 2.93% per quarter with a t-stat of 4.12.
4.3. Performance over time and in extreme markets
Figure 3 plots the cumulative excess return to the diversified time series
momentum strategy over time (on a log scale). For comparison, we also plot the
cumulative excess returns of a diversified passive long position in all instruments, with an
equal amount of risk in each instrument. (Since each instrument is scaled by the same
constant volatility, both portfolios have the same ex ante volatility except for differences
in correlations among time series momentum strategies and passive long strategies.) As
18
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Figure 3 shows, the performance over time of the diversified time series momentum
strategy provides a relatively steady stream of positive returns that outperforms a
diversified portfolio of passive long positions in all futures contracts (at the same ex ante
volatility).
We can also compute the return of the time series momentum factor from 1966 to
1985, despite the limited number of instruments with available data. Over this earlier
sample, time series momentum has a statistically significant return and an annualized
Sharpe ratio of 1.1, providing strong out-of-sample evidence of time series momentum.10
Figure 3 highlights that time series momentum profits are large in October,
November, and December of 2008, which was at the height of the Global Financial Crisis
when commodity and equity prices dropped sharply, bonds prices rose, and currency
rates moved dramatically. Leading into this period, time series momentum suffers losses
in the third quarter of 2008, where the associated price moves caused the TSMOM
strategy to be short in many contracts, setting up large profits that were earned in the
fourth quarter of 2008 as markets in all these asset classes fell further. Figure 3 also
shows that TSMOM suffers sharp losses when the crisis ends in March, April, and May
of 2009, where the ending of a crisis constitutes a sharp trend reversal that TSMOM is on
the opposite side of.
More generally, Figure 4 plots the TSMOM returns against the S&P 500 returns.
The returns to TS-MOM are largest during the biggest up and down market movements.
To test the statistical significance of this finding, the first row of Panel C of Table 3
reports coefficients from a regression of TSMOM returns on the market index and
squared market index. While the beta on the market itself is insignificant, the coefficient
10 We thank the referee for asking for this out-of-sample study of old data.
19
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

on the market return squared is significantly positive, indicating that TSMOM delivers its
highest profits during the most extreme market episodes. TSMOM, therefore, has payoffs
similar to an option straddle on the market. Fung and Hsieh (2001) discuss why trend
following has straddle-like payoffs and apply this insight to describe the performance of
hedge funds. Our TSMOM strategy generates this payoff structure because it tends to go
long when the market has a major upswing and short when the market crashes.
These results suggest that the positive average TSMOM returns are not likely to be
compensation for crash risk. Historically, TSMOM does well during “crashes” because
crises often happen when the economy goes from normal to bad (making TSMOM go
short), and then from bad to worse (leading to TSMOM profits), with the recent financial
crisis of 2008 being a prime example.
4.4. Liquidity and sentiment
We test whether TSMOM returns might be driven or exaggerated by illiquidity.
We first test whether TSMOM performs better for more illiquid assets in the cross
section, and we then test whether the performance of the diversified TSMOM factor
depends on liquidity indicators in the time series. For the former, we measure the
illiquidity of each futures contract using the daily dollar trading volume obtained from
Reuters and broker feeds. We do not have historical time-series of daily volume on these
contracts, but use a snapshot of their daily volume in June 2010 to examine cross-
sectional differences in liquidity across the assets. Since assets are vastly different across
many dimensions, we first rank each contract within an asset class by their daily trading
volume (from highest to lowest) and compute the standard normalized rank of each
contract by demeaning each rank and dividing by its standard deviation i.e., (rank -
20
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

mean(rank))/std(rank). Positive (negative) values imply a contract is more (less) illiquid
than the median contract for that asset class. We find little relation between the
magnitude of the Sharpe ratio of TSMOM for a contract and its illiquidity, as proxied by
daily dollar trading volume. The correlation between illiquidity and Sharpe ratio of a time
series momentum strategy by contract is -0.16 averaged across all contracts, suggesting
that, if anything, more liquid contracts exhibit greater time series momentum profits.
We next consider how TSMOM returns covary in aggregate with the time series
of liquidity. The second row of Panel C of Table 3 reports results using the TED spread, a
proxy for funding liquidity as suggested by Brunnermeier and Pedersen (2009), Asness,
Moskowitz, and Pedersen (2010), and Garleanu and Pedersen (2011), and the top 20%
most extreme realizations of the TED spread to capture the most illiquid funding
environments. As the table shows, there is no significant relation between the TED
spread and TSMOM returns, suggesting little relationship with funding liquidity. The
third row of Panel C of Table 3 repeats the analysis using the VIX index to capture the
level of market volatility and the most extreme market volatility environments, which
also seem to correspond with illiquid episodes. There is no significant relationship
between TSMOM profitability and market volatility either.
At the bottom of Panel C of Table 3, we also examine the relationship between
TSMOM returns and the sentiment index measures used by Baker and Wurgler (2006,
2007). We examine both the level of sentiment and its monthly changes (first differences)
and examine the top and bottom extremes (20%) of these variables. As the regressions
indicate, we find no significant relationship between TSMOM profitability and sentiment
measures, even at the extremes.
21
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

4.5. Correlation structure
Table 4 examines the correlation structure of the time series momentum strategies
and compares them to the correlation structure of passive long positions in the contracts.
The first row of Panel A of Table 4 reports the average pair-wise correlation of times-
series momentum returns among contracts within the same asset class. The correlations
are positive within each asset class, ranging from 0.37 to 0.38 for equities and fixed
income futures to 0.10 and 0.07 for commodities and currencies. Part of this comovement
structure reflects the comovement of the returns to simply being passive long (or short)
each instrument at the same time. The second row of Panel A of Table 4 reports the
average pair-wise correlation of passive long positions within each asset class and, except
for currencies, passive long strategies exhibit higher correlations than time series
momentum strategies within an asset class.
Panel B of Table 4 shows the average correlation of time series momentum
strategies across asset classes. Here, we first compute the return of a diversified portfolio
of time series momentum strategies within each asset class and then estimate the
correlation of returns for TSMOM portfolios across asset classes. All of the correlations
are positive, ranging from 0.05 to 0.21. For comparison, the table also shows the
correlations across asset classes of diversified passive long positions. For every asset
class comparison, the correlation of times-series momentum strategies across asset
classes is larger than the corresponding correlation of passive long strategies, many of
which are negative.
Summing up the results from both panels, time series momentum strategies are
positively correlated within an asset class, but less so than passive long strategies.
22
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

However, across asset classes, time series momentum strategies exhibit positive
correlation with each other, while passive long strategies exhibit zero or negative
correlation across asset classes. This last result suggests that there is a common
component affecting times-series momentum strategies across asset classes
simultaneously that is not present in the underlying assets themselves, similar to the
findings of Asness, Moskowitz, and Pedersen (2010) who find common structure among
cross-sectional momentum strategies across different asset classes.
5. Time Series vs. Cross-Sectional Momentum
Our previous results show a significant relationship between time series
momentum and cross-sectional momentum. In this section we explore that relationship
further and determine how much overlap and difference exist between our time series
momentum strategies and the cross-sectional momentum strategies commonly used in the
literature.
5.1. Time Series Momentum regressed on Cross-Sectional Momentum
Panel A of Table 5 provides further evidence on the relationship between time
series momentum (TSMOM) and cross-sectional momentum (XS-MOM) by regressing
the returns to our time series momentum strategies—diversified across all instruments
and within each asset class—on the returns of cross-sectional momentum strategies
applied to the same assets. Specifically, following Asness, Moskowitz, and Pedersen
(2010), we apply a cross-sectional momentum strategy based on the relative ranking of
23
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

each asset's past 12-month returns and form portfolios that go long or short the assets in
proportion to their ranks relative to the median rank.11
The first row of Panel A of Table 5 reports results from the TSMOM strategy
diversified across all assets regressed on the XS-MOM strategy that is diversified across
those same assets. As before, time series momentum and cross-sectional momentum are
significantly related, with the beta of TSMOM on XS-MOM equal to 0.66 with a t-
statistic of 15.17 and R-square of 44%. However, as the intercept indicates, TSMOM is
not fully captured by XS-MOM, exhibiting a positive and significant alpha of 76 basis
points per month with a t-statistic of 5.90. So, TSMOM and XS-MOM are related, but
are not the same.
The second row of Panel A of Table 5 repeats the regression using XS-MOM
strategies for each asset class, including individual stocks. TSMOM is related to XS-
MOM across all of the different asset classes, including individual equity momentum,
which is not even included in the TSMOM strategy, and this is after controlling for
exposure to XS-MOM from the other four asset classes. TSMOM still exhibits a
significant alpha, however, and is therefore not fully captured by cross-sectional
momentum strategies in these asset classes.
Repeating these regressions using the TSMOM returns for each asset class
separately, we find a consistent pattern. TSMOM is related to XS-MOM within each
asset class, with R-squares are ranging from 60% in FX to 12% in fixed income, but
TSMOM is not captured by XS-MOM. The alphas of TSMOM remain significantly
positive for every asset class. We also see some interesting cross-asset relationships
11 Asness, Moskowitz, and Pedersen (2010) exclude the most recent month when computing 12-month
cross-sectional momentum. For consistency, we follow that convention here, but our results do not depend
on whether the most recent month is excluded or not.
24
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

among TS- and XS-MOM. For instance, not only is TSMOM for commodities correlated
with XS-MOM for commodities, but also with XS-MOM for currencies. Likewise,
TSMOM among equity index futures is correlated with XS-MOM among those equity
indexes but also with XS-MOM among individual stocks. And, TSMOM for fixed
income is correlated with XS-MOM for fixed income and XS-MOM for equity indexes.
These results indicate significant correlation structure in time series and cross-sectional
momentum across different asset classes, consistent with our earlier results and those of
Asness, Moskowitz, and Pedersen (2010).
5.2. A simple, formal decomposition
We can more formally write down the relationship between times-series
(TSMOM) and cross-sectional (XS-MOM) momentum. Following Lo and MacKinlay
(1990) and Lewellen (2002), we can describe a simple cross-sectional and time series
momentum strategy on the same assets as follows. For cross-sectional momentum, we let
1
the portfolio weight of instrument i be wXS,i = (ri −rEW ), that is, the past 12-month
t N t−12,t t−12,t
1 N
excess return over the equal-weighted average return, rEW = ∑ri . The return to
t−12,t N t−12,t
i=1
the portfolio is therefore
N
rXS =∑wXS,iri
t,t+1 t t,t+1
i=1
25
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Next, assuming that the monthly expected return is12 μi = E(ri ) = E(ri )/12 and
t,t+1 t−12,t
letting μ = [μ1,...,μN]′, R =[r1 ,...,rN]′, and Ω = E[(R −12μ)(R −μ)′], the
t,s t,s t,s t−12,t t,t+1
expected return to cross-sectional momentum (XS-MOM) can be decomposed as
tr(Ω) 1′Ω1
E[rXS ]= − + 12σ2
t,t+1 N N2 μ
(6)
N −1 1
= tr(Ω) − [1′Ω1−tr(Ω)] +12 σ2
N2 N2 μ
where tr is the trace of a matrix, 1 is an (N × 1) vector of ones, and σ2 is the cross-
μ
sectional variance of the mean monthly returns μi.
Equation (6) shows that cross-sectional momentum profits can be decomposed
into an auto-covariance component between lagged 1-year returns and future 1-month
returns (the diagonal elements of Ω captured by the first term), a cross-covariance
component capturing the temporal leads and lags across stocks (the off-diagonal elements
of Ω captured by the second term), and the cross-sectional variation in unconditional
mean returns (the third term). As emphasized by Lewellen (2002), cross-sectional
momentum profits need not be generated by positive autocorrelation in returns (i.e., time
series predictability). If cross-serial covariances across stocks are negative, implying that
high past returns of an asset predict lower future returns of other assets, this, too, can lead
to momentum profits. Likewise, large cross-sectional variation in mean returns can also
lead to momentum profits since on average assets with the highest mean returns will have
the highest realized returns.
12 This relation between mean returns is exact if annual returns are computed by summing over monthly
returns. If returns are compounded, this relation is approximate, but an exact relation is straightforward to
derive, e.g. using the separate means of monthly and annual returns.
26
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

The returns to time series momentum can be decomposed similarly if we let the
1
portfolio weights be wTS,i = ri . Then the expected return is:
t N t−12,t
⎛ N ⎞
E ( rTS ) = E ∑wTS,iri
⎜ ⎟
t,t+1 t t,t+1
⎝⎠
i=1 (7)
tr(Ω) μ′μ
= +12
N N
As these equations highlight, time series momentum profits are primarily driven by time
series predictability (i.e., positive auto-covariance in returns) if the average squared mean
returns of the assets is small. Comparing equations (6) and (7), we see that time series
momentum profits can be decomposed into the auto-covariance term that also underlies
cross-sectional momentum (plus the average squared mean excess return). The equations
thus provide a link between time series and cross-sectional momentum profitability,
which we can measure in the data to determine how related these two phenomena are.
Panel B of Table 5 computes each of the components of the diversified 12-month
cross-sectional and time series momentum strategies across all assets and within each
asset class according to the equations above. We report the three components of the
cross-sectional momentum strategy: “Auto” refers to the autocovariance or time series
momentum component, “Cross” refers to the cross-serial covariance or lead-lag
component, and “Mean” refers to the contribution from unconditional mean returns, as
well as their sum (“Total”). We also report the two components to TSMOM: the Auto
and mean squared return components, as well as their sum.
As Panel B of Table 5 shows, time series and cross-sectional momentum are
related but different. The auto-covariance component contributes just about all of the
cross-sectional momentum strategy profits across all assets. The cross-serial or lead-lag
27
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

component contributes negatively to XS-MOM and the cross-sectional variation in means
has a small positive contribution to cross-sectional momentum profits. The contribution
of these components to cross-sectional momentum strategies is also fairly stable across
asset classes, with the dominant component consistently being the auto-covariance or
time series piece.
The decomposition of time series momentum shows that the main component is
the auto-covariance of returns. Squared mean excess returns are a much smaller
component of TSMOM profits, except for fixed income. Since the cross-sectional
correlation of lead-lag effects among assets contributed negatively to XS-MOM, it is not
surprising that TSMOM, which does not depend on the cross-serial correlations across
assets, produces higher profits than XS-MOM.
We also regress the returns of time series momentum as defined in equation (7)
(which is linear as opposed to using the sign of the past return as before) on the returns to
cross-sectional momentum as defined in equation (6). We find that time series
momentum has a significant alpha to cross-sectional momentum, consistent with our
earlier results in Panel A of Table 5 that use a slightly different specification. We
investigate next whether the reverse is true. Does TSMOM explain XS-MOM?
5.3. Does TSMOM explain Cross-Sectional Momentum and other factors?
Panel C of Table 5 uses TSMOM as a right-hand-side variable, testing its ability
to explain other factors. We first examine XS-MOM to see if TSMOM can capture the
returns to cross-sectional momentum across all asset classes as well as within each asset
class. As the first five rows of Panel C of Table 5 show, TSMOM is able to fully explain
cross-sectional momentum across all assets as well as within each asset class for
28
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

commodities, equity indices, bonds, and currencies. The intercepts or alphas of XS-MOM
are statistically no different from zero, suggesting TSMOM captures the return premia of
XS-MOM in these markets. The only positive alpha is for XS-MOM in equity indices,
which has a marginal 1.86 t-statistic. We also regress the Fama-French cross-sectional
momentum factor for individual U.S. equities, UMD, on our TSMOM portfolio. The
UMD factor is created from individual U.S. equities and hence has no overlap with any
of the assets used to comprise our TSMOM factor. Nevertheless, TSMOM is able to
capture the return premium on UMD, which has a positive 0.49 loading on TSMOM and
an insignificant -0.28 alpha (t-stat = -0.93). We also examine the other Fama-French
factors HML, the value factor, and SMB, the size factor. HML loads negatively on
TSMOM so TSMOM naturally cannot explain the value effect, and SMB has a loading
close to zero. Finally, we also examine the returns to two popular hedge fund indices that
trade globally across many assets: the “Managed Futures” hedge fund index and “Global
Macro” hedge fund index obtained from Dow Jones/Credit Suisse from 1990 to 2009. As
the last two rows of Panel C of Table 5 shows, both hedge fund indices load significantly
on our TSMOM factor and in the case of the Managed Futures index, the TSMOM factor
captures its average return entirely. Hence, TSMOM is a simple implementable factor
that captures the performance metric of Fung and Hsieh (2001), which they show
explains hedge fund returns as well.13
The strong performance of TSMOM and its ability to explain some of the
prominent factors in asset pricing, namely cross sectional momentum as well as some
hedge fund strategy returns, suggests that TSMOM is a significant feature of asset price
13 Lequeux and Acar (1998) also document that a simple timing trade tracks the performance of currency
hedge funds.
29
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

behavior. Future research may well consider what other asset pricing phenomena might
be related to time series momentum.
6. Who trades on trends: Speculators or hedgers?
To consider who trades on trends, Figure 5 shows the Net Speculator Position
broken down by the sign of the past 12-month return for each instrument with available
CFTC data. Specifically, for each futures contract, Figure 5 plots the average Net
Speculator Position in, respectively, the sub-sample where the past 12 month return on
the contract is positive (“Positive TSMOM” ) and negative (“Negative TSMOM” ) de-
meaned using the average Net Speculator Position for each instrument. The figure
illustrates that speculators are on average positioned to benefit from trends, whereas
hedgers, by definition, have the opposite positions. Speculators have longer-than-average
positions following positive past 12-month returns, and smaller-than-average positions
following negative returns, on average. Said differently, speculators have larger positions
in an instrument following positive returns than following negative returns. This trend-
following pattern of speculative positions is found for every contract except the S&P 500
futures, where Net Speculator Positions have opposite signs, though are close to zero.
Since we also know that trend following is associated with positive abnormal returns,
these results indicate that speculators profit on average from these position changes at the
expense of hedgers.
6.1. The evolution of a trend
We next consider the dynamics of these trading positions over time. Our previous
results suggest that trends or time series momentum lasts about a year and then starts to
30
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

reverse. We investigate these return patterns in more depth and attempt to link them to
the evolution of trading positions.
Examining the evolution of trends and trading patterns may help distinguish
theories for momentum. For example, if initial under-reaction to news is the cause of
trends, then this part of the trend should not reverse, whereas the part of a trend that is
driven by over-reaction should reverse as prices eventually gravitate back toward
fundamentals.
To consider the evolution of a trend, we perform an event study of our time series
momentum strategy as follows. For each month and instrument, we first identify whether
the previous 12 months excess returns are positive or negative. For all the time-
instrument pairs with positive 12-month past returns, we compute the average return from
12 months prior to the “event date” (portfolio formation date) to 36 months after. We do
the same for the time-instrument pairs with negative past 12-month returns. We then
standardize the returns to have a zero mean across time and across the two groups (for
ease of comparison), and compute the cumulative returns of the subsequent months
following positive past year returns (“Positive TSMOM” ) and negative past year returns
(“Negative TSMOM” ), respectively, where we normalize the cumulative returns to be 1
at the event date.
Panel A of Figure 6 shows the cumulative returns conditional on positive and
negative time series momentum. The returns to the left of the event date are, of course,
positive and negative by construction. To the right of the event date, we see that the
positive pre-formation returns continue upward after the portfolio formation for about a
year, consistent with a time series momentum effect, and then partially reverse thereafter.
31
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

This is consistent with both initial under-reaction and delayed over-reaction as predicted
by sentiment theories such as Daniel, Hirshleifer, and Subrahmanyam (1998) and
Barberis, Shleifer, and Vishny (1998). While the reversal after a year suggests over-
reaction, the fact that only part of the post-formation upward trend is reversed suggests
that under-reaction appears to be part of the story. Similarly, the negative pre-formation
trend is continued for a year until it partially reverses as well.
Panel B of Figure 6 shows the evolution of Net Speculator Positions that coincide
with the positive and negative times-series momentum returns. Specifically, for each
instrument and month, we compute the average Net Speculator Position for each month
from 12 months prior to the event (portfolio formation date) to 36 months after portfolio
formation for both positive and negative trends. We see that for positive TSMOM,
speculators increase their positions steadily from months -12 to 0, building up to the
formation date. Likewise, speculators decrease their positions steadily from the negative
TSMOM event date. These patterns are not by construction since we split the sample
based on returns and not based on Net Speculator Positions. After the event, speculators’
positions begin to mean-revert towards their (positive) average levels, and plateau at
about a year (and maybe slightly longer for negative TSMOM), which is when the trend
in returns starts to reverse.
The patterns in Figure 6 indicate that while speculator positions are consistent
with trading on trends, they do not appear to keep piling into the trade with a lag. In fact,
speculators appear to reduce their trend chasing up to the point where positive returns
from following trends disappear. Conversely, hedgers, who are on the other side of these
trades, appear to be increasing their positions steadily in the direction of the trend. This
32
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

suggests that if overreaction is caused by such trading, it would have to come from
hedgers, not speculators. While the direction of causality between returns and trading
positions is indeterminate, these results also suggest that trading positions of speculators
and hedgers are closely linked to the profitability of time series momentum, where
speculators appear to be profiting from trends and reversals at the expense of hedgers.
6.2. Joint dynamics of returns and trading positions
For a more formal analysis of trading patterns and returns, we study the joint
dynamics of time series momentum returns and the change in Net Speculator Positions
using a vector autoregressive (VAR) model. We estimate a monthly bivariate VAR with
24 months of lags of returns and changes in Net Speculator Positions and plot the impulse
response of returns and Net Speculator Positions from a return shock. We need to include
more than 12 months of lags to capture delayed reversal, but our results are robust to
choosing other lag lengths between 12 and 24.
We perform a Cholesky decomposition of the variance-covariance matrix of
residuals with the return first, and consider a one standard deviation shock to the returns
of the contract. (The return response to an initial return shock is qualitatively the same
regardless of the ordering of the Cholesky decomposition because of a limited feedback
with positions.) The response to this impulse is plotted in Figure 7, both in terms of the
effect on the cumulative return to the contract and the cumulative changes in Net
Speculator Positions. As the figure shows, returns continue to rise for about a year and
then partially reverse thereafter following the return shock. Net Speculator Positions
increase contemporaneously with the return shock and then mean-revert to zero at about a
year. These results are consistent with our previous findings and confirm that speculative
33
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

positions match the return patterns of time series momentum. Speculators seem to profit
from trends for about a year and then revert to their average positions at the same time
the TSMOM effect ends; all at the expense of hedgers.
The patterns indicate that speculators profit from time series momentum, while
hedgers pay for it. One explanation might be that speculators earn a premium through
time series momentum by providing liquidity to hedgers. We explore this possibility
further by examining the predictability of returns using trading positions as well as
different components of futures returns. Specifically, we investigate whether changes in
the underlying spot price or the shape of the futures curve (e.g, “roll yield”) are driving
the time series predictability and how each of these lines up with trading positions.
6.3. Predictability of positions, price changes, and roll yield
We decompose the past return of each futures contract into the change in the price
of the underlying spot asset and the return that is related to the shape of the futures curve,
called the “roll return” or “roll yield.”
First, we define the underlying spot price changes in excess of the risk-free rate
as:
price −price
price change = t t−12 −rf
t−12,t price t−12,t
t−12
where prices are measured as the nearest-to-expiration futures price and rf is the risk-
t−12,t
free interest-rate over the 12-month period. We then define the roll return by the
following decomposition:
futures return =price change + roll return
t−12,t t−12,t t−12,t
34
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

In financial futures with little storage costs or convenience yield, the roll return is close to
zero, but, in commodity markets, the roll return can be substantial. The futures return is
calculated from the nearest-to-expiration or next-to-nearest expiration contract, whose
maturity date may not be in the same month as the spot return calculation, which is based
only on the nearest-to-expiration contract.
Our conjecture is that hedgers’ price pressure affects mostly the roll returns,
whereas information diffusion affects mostly price changes. To see why, recall first
Keynes’ basic idea that hedging pressure must affect required returns to give speculators
an incentive to provide liquidity by taking the other side of the trade. Since hedging takes
place in futures markets, hedging pressure would affect futures prices and thus lead to a
roll yield as each futures contract expires at the spot price. When hedgers, such as
commodity producers, are shorting the futures, this leads to positive roll return and what
Keynes called “normal backwardation.” On the other hand, information diffusion (which
is the driver of several of the behavioral theories), would simply affect price changes.
Panel B of Figure 7 plots the impulse response of spot price changes and Net
Speculator Positions by repeating the VAR we ran above, replacing the total futures
returns with the spot price changes only. The impulse response of spot returns and Net
Speculator Positions matches those for total returns: trends exist for about a year and
then reverse and net speculative positions mirror that pattern. This is consistent with
initial under-reaction and delayed over-reaction being due to information diffusion rather
than hedging pressure.
Panel C of Figure 7 plots the impulse response from replacing total returns with
the roll return in the VAR. Here, the picture looks quite different. A shock to roll returns
35
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

is associated with a continued upward trend to roll returns and a small effect on Net
Speculator Positions. This is consistent with hedgers having stable positions in the same
direction for extended periods of time and being willing to give up roll returns to enjoy
hedging benefits. Speculators who take the other side, profit from momentum as a
premium for providing liquidity to hedgers.
Finally, Table 6 revisits the return predictability regressions we started with,
focusing on 12-month return predictability, but examines the predictive power of the spot
versus roll return, as well as their interaction with speculative trading positions. We
regress the return of each futures contract on the past 12 month return of each contract,
the spot price change of each contract, the roll return of each contract, and the change in
Net Speculator Position. The first four rows of Table 6 report the univariate regression
results for each of these variables. The total return, spot price return, roll return, and
change in net speculator positions are all significant positive univariate predictors of
futures returns.
In multivariate regressions, however, the change in net speculator positions drops
slightly and becomes insignificant, indicating that controlling for past returns reduces
some of the predictive power of speculative positions. This is consistent with the idea
that roll return and speculator positions both capture hedging pressure, though measured
differently and neither being a perfect measure for hedging pressure. Spot price changes
and roll returns have almost the same predictive regression coefficient in the multivariate
regression, hence their joint predictive power (as measured by the R-square) is the same
as the univariate predictability of their sum, which is the total futures return. Finally, the
last row of Table 6 includes interaction terms between the spot and roll returns and net
36
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

speculative positions. While all the coefficients are positive, indicating that when changes
in net speculative positions move in the same direction as returns there is stronger
positive predictability of future returns, the results are not statistically significant.
The results in Table 6 indicate that time series momentum is not purely driven by
one component of futures returns. Both the spot return change and roll yield provide
predictive power for futures returns. In addition, as the VAR results show, there is an
interesting dynamic between time series momentum and net speculative and hedging
positions. Speculators seem to ride the trend for about a year, eventually reducing their
positions and taking the opposite side before the trend reverses. In the process, they earn
positive excess returns at the expense of hedgers, who may be willing to compensate
speculators for liquidity provision in order to maintain their hedge.
7. Conclusion
We document a significant time series momentum effect that is remarkably
consistent across the nearly five dozen futures contracts and several major asset classes
we study over the last thirty years. The time series momentum effect is distinct from
cross-sectional momentum, though the two are related. Decomposing both time series
and cross-sectional momentum profits, we find that the dominant force to both strategies
is significant positive auto-covariance between a security’s excess return next month and
its lagged 1-year return. This evidence is consistent with initial under-reaction stories, but
may also be consistent with delayed overreaction theories of sentiment as the time series
momentum effect partially reverses after one year.
37
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Time series momentum exhibits strong and consistent performance across many
diverse asset classes, has small loadings on standard risk factors, and performs well in
extreme periods, all of which present a challenge to the random walk hypothesis and to
standard rational pricing models. The evidence also presents a challenge to current
behavioral theories since the markets we study vary widely in terms of the type of
investors, yet the pattern of returns remains remarkably consistent across these markets
and is highly correlated across very different asset classes. Indeed correlation among time
series momentum returns is stronger than the correlation of passive long positions across
the same asset classes, implying the existence of a common component to time series
momentum that is not present in the underlying assets themselves.
Finally, the link between time series momentum returns and the positions of
speculators and hedgers indicates that speculators profit from time series momentum at
the expense of hedgers. This evidence is consistent with speculators earning a premium
via time series momentum for providing liquidity to hedgers. Decomposing futures
returns into the effect of price changes, which captures information diffusion, and the roll
return, which captures how hedging pressure affects the shape of the futures curve, we
find that shocks to both price changes and roll returns are associated with time series
momentum profits. However, only shocks to price changes partially reverse, consistent
with behavioral theories of delayed over-reaction applying to information dissemination,
and not hedging pressure.
Time series momentum represents one of the most direct tests of the random walk
hypothesis and a number of prominent behavioral and rational asset pricing theories. Our
findings present new evidence and challenges for those theories and for future research.
38
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

References
Ahn, D.H., J. Boudoukh, M. Richardson and R.F. Whitelaw (2002), “Partial Adjustment
or Stale Prices? Implications from Stock Index and Futures Return Autocorrelations,”
The Review of Financial Studies, vol. 15, no. 2, 655-689.
Ahn, D.H., J. Conrad, and R.F. Dittmar (2003), “Risk Adjustment and Trading
Strategies,” The Review of Financial Studies, vol. 16, no. 2, 459-485.
Asness, C. (1994), “Variables that Explain Stock Returns.“Ph.D. Dissertation, University
of Chicago.
Asness, C., J. M. Liew, and R. L. Stevens (1997), “Parallels Between the Cross-Sectional
Predictability of Stock and Country Returns,” The Journal of Portfolio Management, vol.
23, 79-87.
Asness, C., T.J. Moskowitz, and L.H. Pedersen, (2010) “Value and Momentum
Everywhere,” National Bureau of Economic Research.
Baker, M. and J. Wurgler (2006), “Investor Sentiment and the Cross-section of Stock
Returns,” Journal of Finance, vol. 61, 11645-1680.
Baker, M. and J. Wurgler (2007), “Investor Sentiment in the Stock Market,” Journal of
Economic Perspectives, vol. 21, 129-157.
Barberis, N., A. Shleifer and R. Vishny (1998), “A Model of Investor Sentiment,”
Journal of Financial Economics 49, 307-343.
Berk, J., R.C. Green and V. Naik (1999), “Optimal Investment, Growth Options and
Security Returns,” Journal of Finance 54, 1153-1608
Bessembinder, H. (1992), “Systematic Risk, Hedging Pressure, and Risk Premiums in
Futures Markets,” The Review of Financial Studies, vol. 5, no. 4, 637-667.
Bhojraj, S. and B.Swaminathan (2006), “Macromomentum: Returns Predictability in
International Equity Indices,” The Journal of Business, vol. 79, no. 1, pp. 429–451.
Bikhchandani, S.,D. Hirshleifer, and I. Welch (1992), “A Theory of Fads, Fashion,
Custom, and Cultural Change as Informational Cascades,” Journal of Political Economy,
100, 5, 992-1026.
Brunnermeier, M. and L. H. Pedersen (2009), “Market Liquidity and Funding Liquidity,”
The Review of Financial Studies, 22, 2201-2238.
Chen, J. and H. Hong (2002), “Discussion of ‘Momentum and Autocorrelation in Stock
Returns’,” The Review of Financial Studies, 15, 565-573.
39
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Cutler, D.M., J.M. Poterba, L.H. Summers (1991), “Speculative Dynamics,” Review of
Economic Studies, 58, 529-546.
Daniel, K., D. Hirshleifer, A. Subrahmanyam (1998), “A Theory of Overconfidence,
Self-attribution, and Security Market Under- and Over-reactions,” Journal of Finance 53,
1839-1885.
De Long, J.B., A. Shleifer, L. H. Summers, and Waldmann, R.J. (1990), “Positive
Feedback Investment Strategies and Destabilizing Rational Speculation,” The Journal of
Finance, 45, 2, 379-395.
DeMiguel, V., F.J. Nogales, and R. Uppal (2010), “Stock Return Serial Dependence and
Out-of-Sample Portfolio Performance,” working paper, London Business School
de Roon, F., T. E. Nijman, and C. Veld (2000), “Hedging Pressure Effects in Futures
Markets,” Journal of Finance 55, 1437–56.
Edwards, W.,(1968), “Conservatism in Human Information Processing,” In: Kleinmutz,
B. (Ed.), Formal Representation of Human Judgment. John Wiley and Sons, New York,
pp. 17-52.
Erb, C. and Harvey, C. (2006), “The Tactical and Strategic Value of Commodity
Futures,“ Financial Analysts Journal, vol. 62, no. 2, 69-97.
Fama, E., and K. French, 1987, “Commodity Futures Prices: Some Evidence on Forecast
Power, Premiums, and the Theory of Storage,” Journal of Business, 60, 55-73.
Fama, E. and K. French (1988), “Permanent and Temporary Components of Stock
Prices,” Journal of Political Economy, 96, 246-273.
Fama, E. and K. French (1993), “Common Risk Factors in the Returns of Stocks and
Bonds,” Journal of Financial Economic 33, Issue 1, 3-56.
Frazzini, A. (2006), “The Disposition Effect and Underreaction to News.” Journal of
Finance, 61.
Fung, W. and D. Hsieh (2001), “The Risk in Hedge Fund Strategies: Theory and
Evidence from Trend Followers”," Review of Financial Studies, 14, 313-341.
Garleanu, N. and L.H. Pedersen (2009), “Dynamic Trading with Predictable Returns and
Transaction Costs,” Berkeley and NYU.
Garleanu, N. and L.H. Pedersen (2011), “Margin-Based Asset Pricing and Deviations
from the Law of One Price,” The Review of Financial Studies, forthcoming.
40
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Gorton, G.B., F. Hayashi, and K. G. Rouwenhorst (2008), “The Fundamentals of
Commodity Futures Returns,” Yale ICF, working paper.
Hong, H. and J. Stein (1999), “A Unified Theory of Underreaction, Momentum Trading
and Overreaction in Asset Markets,” Journal of Finance, LIV, no. 6.
Jegadeesh, N. and S. Titman (1993), “Returns to Buying Winners and Selling Losers:
Implications for Stock Market Efficiency,” Journal of Finance 48, 65–91.
Johnson, T.C. (2002), “Rational Momentum Effects,” Journal of Finance 57, 585-608.
Keynes, J.M. (1923), “Some Aspects of Commodity Markets,” Manchester Guardian
Commercial, European Reconstruction Series Section 13:784–86.
Lequeux, P. and E. Acar (1998). “A Dynamic Index for Managed Currencies Funds
Using CME Currency Contracts,” European Journal of Finance, vol. 4(4), 311-330.
Lewellen, J. (2002), “Momentum and Autocorrelation in Stock Returns,” The Review of
Financial Studies, 15(2), 533-564.
Liu, L. and L. Zhang (2008), “Momentum Profits, Factor Pricing, and Macroeconomic
Risk,” Review of Financial Studies, 21 (6), 2417-2448.
Lo, A., and C. Mackinlay (1988), “Stock Prices Do Not Follow Random Walks:
Evidence From a Simple Specification Test,” Review of Financial Studies, 1, 41-66.
Moskowitz, T.J., and M. Grinblatt (1999), “Do Industries Explain Momentum?,” The
Journal of Finance 54, 1249-1290.
Poterba, J. M. and L.H. Summers (1988), “Mean Reversion in Stock Prices: Evidence
and Implications,” Journal of Financial Economics 22, Issue 1, 27-59.
Richardson, M., (1993), “Temporary Components of Stock Prices: A Skeptic’s View,”
Journal of Business & Economic Statistics, April 1993, Vol. 11, No. 2.
Rouwenhorst, K. G. (1998), “International Momentum Strategies,” The Journal of
Finance, vol. 53, no. 1, pp. 267-284.
Sagi, J.S., and M.S. Seasholes (2007), “Firm-specific Attributes and the Cross-section of
Momentum,” Journal of Financial Economics, vol. 84(2), 389-434.
Shefrin, H., and M. Statman (1985), “The Disposition to Sell Winners Too Early and
Ride Losers Too Long: Theory and Evidence,” Journal of Finance 40, 777–791.
Shleifer, A., and L. H. Summers (1990), “The Noise Trader Approach to Finance,”
Journal of Economic Perspectives, Volume 4, Number 2, 19-33.
41
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Tversky, A. and D. Kahneman (1974), “Judgment Under Uncertainty: Heuristics and
Biases,” Science 185, 1124-1131.
Qiu, L.X. and I. Welch (2006), “Investor Sentiment Measures,” Working Paper.
42
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Appendix A: Data sources
Equity Indices. The universe of equity index futures consists of the following 9
developed equity markets: SPI 200 (Australia), CAC 40 (France), DAX (Germany),
FTSE/MIB (Italy), TOPIX (Japan), AEX (Netherlands), IBEX 35 (Spain), FTSE 100
(U.K.), and S&P 500 (U.S). Futures returns are obtained from Datastream. We use MSCI
country level index returns prior to the availability of futures returns.
Bond Indices. The universe of bond index futures consists of the following 13 developed
bond markets: Australia 3-year Bond, Australia 10-year Bond, Euro Schatz, Euro Bobl,
Euro Bund, Euro Buxl, Canada 10-year Bond, Japan 10 year Bond (TSE), Long Gilt, US
2-year Note, US 5-year Note, US 10-year Note and US Long Bond. Futures returns are
obtained from Datastream. We use JP Morgan country level bond index returns prior to
the availability of futures returns. We scale daily returns to a constant duration of 2 years
for 2 and 3-year bond futures, 4 years for 5-year bond futures, 7 years for 10-year bond
futures and 20 years for 30-year bond futures.
Currencies. The universe of currency forwards covers the following 10 exchange rates:,
Australia, Canada, Germany spliced with the Euro, Japan, New Zealand, Norway,
Sweden, Switzerland, U.K., and U.S. We use spot and forward interest rates from
Citigroup to calculate currency returns going back to 1989 for all the currencies except
for CAD and NZD, which go back to 1992 and 1996. Prior to that, we use spot exchange
rates from Datastream and IBOR short rates from Bloomberg to calculate returns.
Commodities. We cover 24 different commodity futures. Our data on Aluminum,
Copper, Nickel, Zinc is from London Metal Exchange (LME), Brent Crude, Gas Oil,
Cotton, Coffee, Cocoa, Sugar is from Intercontinental Exchange (ICE), Live Cattle, Lean
Hogs is from Chicago Mercantile Exchange (CME), Corn, Soybeans, Soy Meal, Soy Oil,
Wheat is from Chicago Board of Trade (CBOT), WTI Crude, RBOB Gasoline spliced
with Unleaded Gasoline, Heating Oil, Natural Gas is from New York Mercantile
Exchange (NYMEX), Gold, Silver is from New York Commodities Exchange
(COMEX), and Platinum from Tokyo Commodity Exchange (TOCOM).
Position of Traders Data. We obtain speculator net length and open interest data from
the CFTC Commitments of Traders Report website for the following futures: Corn,
Soybeans, Soy Meal, Soy Oil, Wheat traded on Chicago Board of Trade (CBOT), Live
Cattle, Lean Hogs, Feeder Cattle, Australian Dollar, Canadian Dollar, Swiss Franc,
British Pound, Japanese Yen, Euro FX, New Zealand Dollar, S&P 500 traded on Chicago
Mercantile Exchange (CME), Cotton, Coffee, Cocoa, Sugar traded on Intercontinental
Exchange (ICE), WTI Crude, RBOB Gasoline spliced with Unleaded Gasoline, Heating
Oil, Natural Gas traded on New York Mercantile Exchange (NYMEX) and Gold, Silver
traded on New York Commodities Exchange (COMEX). The data cover the period
January, 1986 to December, 2009.
43
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Fig. 1. Time Series Predictability Across All Asset Classes
We regress the monthly excess return of each contract on its own lagged excess return over various
horizons. Panel A uses the size of the lagged excess return as a predictor, where returns are scaled by their
ex ante volatility to make them comparable across assets, Panel B uses the sign of the lagged excess return
as a predictor, where the dependent variable is scaled by its ex ante volatility to make the regression
coefficients comparable across different assets, and Panel C reports the results of the sign regression by
asset class. Reported are the pooled regression estimates across all instruments with t-statistics computed
using standard errors that are clustered by time (month).
Panel A:
Panel B:
7
6
5
4
3
2
1
0
-1
-2
-3
citsitatS-T
1 4 7 01 31 61 91 22 52 82 13 43 73 04 34 64 94 25 55 85
6
5
4
3
2
1
0
-1
-2
-3
-4
-5
T-Statistic by Month, All Asset Classes
Month Lag
citsitatS-T
1 4 7 01 31 61 91 22 52 82 13 43 73 04 34 64 94 25 55 85
rs /σs =α+βrs /σs +εs
t t−1 h t−h t−h−1 t
T-Statistic by Month, All Asset Classes
Month Lag
rs /σs =α+βsign(rs )+εs
t t−1 h t−h t
44
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Panel C: Results by asset class.
5
4
3
2
1
0
-1
-2
-3
citsitatS-T
Commodity Futures
3
2
1
0
-1
-2
-3
-4
Month Lag
citsitatS-T
Equity Index Futures
Month Lag
4
3
2
1
0
-1
-2
-3
citsitatS-T
Government Bond Futures
5
4
3
2
1
0
-1
-2
-3
-4
Month Lag
citsitatS-T
Currencies
Month Lag
45
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Fig. 2. Sharpe Ratio of 12-Month Time Series Momentum by Instrument
Reported are the annualized gross Sharpe ratio of the 12-month time series momentum or trend strategy for
each futures contract/instrument. For each instrument in every month the trend strategy goes long (short)
the contract if the excess return over the past 12 months of being long the instrument is positive (negative),
and scales the size of the bet to be inversely proportional to the ex ante volatility of the instrument to
maintain constant volatility over the entire sample period from January 1985 to December 2009. The
second figure plots a normalized value of the illiquidity of each futures contract measured by ranking
contracts within each asset class by their daily trading volume (from highest to lowest) and reporting the
standard normalized rank for each contract within each asset class. Positive (negative) values imply the
contract is more (less) illiquid than the median contract for that asset class.
1.2
1.0
0.8
0.6
0.4
0.2
0.0
oitaR
eprahS
ssorG
Aluminum Brent
Oil
Cattle Cocoa Coffee Copper Corn Cotton Crude
Oil
Gas
Oil
Gold Heating
Oil
Hogs Natural
Gas
Nickel Platinum Silver Soybeans Soy
Meal
Soy
Oil
Sugar Gasoline Wheat Zinc AUD-NZD AUD-USD EUR-JPY EUR-NOK EUR-SEK EUR-CHF EUR-GBP AUD-JPY GBP-USD EUR-USD USD-CAD USD-JPY ASX
SPI 200
DAX IBEX
35
CAC
40
FTSE/MIB TOPIX AEX FTSE
100
S&P
500
3
Yr
Australian
Bond
10
Yr
Australian
Bond
2
Yr
Euro -Schatz
5
Yr
Euro -Bobl
10
Yr
Euro -Bund
30
Yr
Euro -Buxl
10
Yr
CGB
10
Yr
JGB
10
Yr
Long Gilt
2
Yr
US Treasury
Note
5
Yr
US Treasury
Note
10
Yr
US Treasury
Note
30
Yr
US Treasury
Bond
Sharpe Ratio of 12 Month Trend Strategy
Commodities Currencies Equities Fixed Income
2.0
1.5
1.0
0.5
0.0
-0.5
-1.0
-1.5
-2.0
)emuloV
gnidarT
yliaD
no
desaB
knaR
dezilamroN(
ytidiuqillI Aluminum Brent
Oil
Cattle Cocoa Coffee Copper Corn Cotton Crude
Oil
Gas
Oil
Gold Heating
Oil
Hogs Natural
Gas
Nickel Platinum Silver Soybeans Soy
Meal
Soy
Oil
Sugar Gasoline Wheat Zinc AUD-NZD AUD-USD EUR-JPY EUR-NOK EUR-SEK EUR-CHF EUR-GBP AUD-JPY GBP-USD EUR-USD USD-CAD USD-JPY ASX
SPI
200
DAX IBEX
35
CAC
40
FTSE/MIB TOPIX AEX FTSE
100
S&P
500
3
Yr Australian
Bond
10
Yr Australian
Bond
2
Yr Euro
-Schatz
5
Yr Euro
-Bobl
10
Yr Euro
-Bund
30
Yr Euro
-Buxl
10
Yr CGB
10
Yr JGB
10
Yr Long
Gilt
2
Yr US
Treasury
Note
5
Yr US
Treasury
Note
10
Yr US
Treasury
Note
30
Yr US
Treasury
Bond
Illiquidity of Futures Contracts
Correlation(Sharpe ratio, Illiquidity) = ‐0.16
Commodities Currencies Equities Fixed Income
46
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Fig. 3. Cumulative Excess Return of Time Series Momentum and Diversified
Passive Long Strategy, January 1985 to December 2009.
$100
Fig. 4. The Trend Smile
The non-overlapping quarterly returns on the diversified (equally weighted across all contracts) 12-month
time series momentum or trend strategy are plotted against the contemporaneous returns on the S&P 500.
47
58 78 98 19 39 59 79 99 10
$100,000
$10,000
$1,000
)elacS
goL(
001$
fo
htworG
91 91 91 91 91 91 91 91 02
3002 5002 7002 9002
Date
Time Series Momentum Passive Long
30%
25%
20%
15%
10%
5%
0%
-5%
-10%
-15%
-25% -15% -5% 5% 15% 25%
.
snruteR
mutnemoM
seireS-emiT
S&P 500 Returns
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Fig. 5. Net Speculator Positions
For each futures contract, the figure plots the average de-meaned Net Speculator Position in, respectively, the sub-sample where the past 12 month returns on the
contract are positive (“Positive TSMOM” ) and negative (“Negative TSMOM” ). The figure illustrates that speculators are on average positioned to benefit from
trends, whereas hedgers, by definition, have the opposite positions.
20%
15%
10%
5%
0%
-5%
-10%
-15%
-20%
-25%
C attle C o c o C a off e e C or C n ott o n Cr u de G o H l d e at oil H o g N s at ga s Sil S v y e b r e a S n o s y m e a S l o y oil S u U g n a l r e
Y
a d
r
e U W d S
Y
h T e
r
S a r U & t e S a
Y
P s 5 u T
r
0 r U r y e 0
Y
S a N s
r
T u o U r r t y e e S a N s T u o r r e t y A e a N u s u s o r t t r y e a B li a o n n d d C o a ll n a a r d E i
N
a u n e r o w d o Z ll e a a r l a Y n d e S n D w o is ll s a F r r a n P c o u n d
2 5 1 0 3 0
noitisoP
rotalucepS
teN
denaeM-eD
Positive TS-MOM Negative TS-MOM
48
EElleeccttrroonniicc
ccooppyy
aavvaaiillaabbllee
aatt::
hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Fig. 6. Event Study of Time Series Momentum
For each month and instrument, we identify whether the previous 12 months returns are positive or
negative and compute the average return from 12 months prior to the “event date” (portfolio formation
date) to 36 months after following positive past year returns (“Positive TSMOM” ) and negative past year
returns (“Negative TSMOM” ). We standardize the returns to have a zero mean across time and across the
two groups (for ease of comparison), and compute the cumulative returns of the subsequent months, where
we normalize the cumulative returns to be 1 at the event date. Panel B plots the Net Speculator Position as
defined by the CFTC conditional on positive and negative past returns.
Panel A: Cumulative Returns in Event Time
1
1
0
0
Panel B: Net Speculator Positions in Event Time
Run research.papers.mf.event_study
snruteR
evitalumuC
.15
1.1
.05
1
.95
0.9
.85
-12 -6 0 6 12 18 24 30 36
Event Time (Months)
Positive TS MOM Negative TS MOM
0.12
0.1
0.08
0.06
0.04
0.02
0
-0.02
-0.04
.
noitisoP
rotalucepS
teN
-12 -6 0 6 12 18 24 30 36
Event Time (Months)
Positive TS MOM Negative TS MOM
49
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Fig. 7. Impulse Response from a Shock to Returns
Plotted are the cumulative returns and speculators’ net positions in response to a one standard deviation
shock to total returns on the futures contract (Panel A), returns on the spot asset (Panel B) and returns to
rolling the contract (Panel C). The impulse response is based on an estimated vector autoregressive model
using monthly returns with 24 lags of returns and net speculator positions that assumes coefficients are the
same across all contracts, with a Cholesky decomposition of the shock.
Panel A: Futures Returns
4.0% 30.0%
3.3% 25.0%
2.7% 20.0%
2.0% 15.0%
1.3% 10.0%
0.7% 5.0%
0.0% 0.0%
-0.7% -5.0%
0 3 6 9 12 15 18 21 24 27 30 33 36
nruteR
evitalumuC
noitisoP
rotalucepS
teN
Time Relative to Shock (Months)
Cumulative Return (left axis) Net Speculator Position (right axis)
50
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Panel B: Spot Returns
4.0% 30.0%
3.3% 25.0%
20.0%
2.0% 15.0%
1.3% 10.0%
0.7% 5.0%
0.0% 0.0%
-0.7% -5.0%
0 3 6 9 12 15 18 21 24 27 30 33 36
Panel C: Roll returns
nruteR
evitalumuC
noitisoP
rotalucepS
teN
2.7%
Time Relative to Shock (Months)
Cumulative Return (left axis) Net Speculator Position (right axis)
4.0% 30.0%
3.3% 25.0%
2.6% 20.0%
2.0% 15.0%
1.3% 10.0%
0.7% 5.0%
0.0% 0.0%
-0.7% -5.0%
0 3 6 9 12 15 18 21 24 27 30 33 36
nruteR
evitalumuC
noitisoP
rotalucepS
teN
Time Relative to Shock (Months)
Cumulative Return (left axis) Net Speculator Position (right axis)
51
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Table 1. Summary Statistics on Futures Contracts
Reported are the annualized mean return and volatility (standard deviation) of the futures contracts in our
sample from January 1965 to December 2009 as well as the mean and standard deviation of the net
speculator long positions in each contract as a percentage of open interest, covered and defined by the
CFTC data, which is available over the period January 1986 to December 2009. For the contracts with
CFTC positions data, the table also reports the coefficient and t-statistic from a regression of the monthly
returns on the futures contract on the previous month's net long speculator positions.
Average
Stdev. Net
Net
Data Start Annualized Annualized Speculator
Speculator
Date Mean Volatility Long
Long
Positions
Positions
Commodity Futures
ALUMINUM Jan-79 0.97% 23.50%
BRENTOIL Apr-89 13.87% 32.51%
CATTLE Jan-65 4.52% 17.14% 8.1% 9.6%
COCOA Jan-65 5.61% 32.38% 4.9% 14.0%
COFFEE Mar-74 5.72% 38.62% 7.5% 13.6%
COPPER Jan-77 8.90% 27.39%
CORN Jan-65 -3.19% 24.37% 7.1% 11.0%
COTTON Aug-67 1.41% 24.35% -0.1% 19.4%
CRUDE Mar-83 11.61% 34.72% 1.0% 5.9%
GASOIL Oct-84 11.95% 33.18%
GOLD Dec-69 5.36% 21.37% 6.7% 23.0%
HEATOIL Dec-78 9.79% 33.78% 2.4% 6.4%
HOGS Feb-66 3.39% 26.01% 5.1% 14.5%
NATGAS Apr-90 -9.74% 53.30% -1.6% 8.9%
NICKEL Jan-93 12.69% 35.76%
PLATINUM Jan-92 13.15% 20.95%
SILVER Jan-65 3.17% 31.11% 20.6% 14.3%
SOYBEANS Jan-65 5.57% 27.26% 8.2% 12.8%
SOYMEAL Sep-83 6.14% 24.59% 6.7% 11.2%
SOYOIL Oct-90 1.07% 25.39% 5.7% 12.8%
SUGAR Jan-65 4.44% 42.87% 10.0% 14.2%
UNLEADED Dec-84 15.92% 37.36% 7.8% 9.6%
WHEAT Jan-65 -1.84% 25.11% 4.3% 12.1%
ZINC Jan-91 1.98% 24.76%
52
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

53
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Average
Stdev. Net
Net
Data Start Annualized Annualized Speculator
Speculator
Date Mean Volatility Long
Long
Positions
Positions
Equity Index Futures
ASX SPI 200 (AUS) Jan-77 7.25% 18.33%
DAX (GER) Jan-75 6.33% 20.41%
IBEX 35 (ESP) Jan-80 9.37% 21.84%
CAC 40 10 (FR) Jan-75 6.73% 20.87%
FTSE/MIB (IT) Jun-78 6.13% 24.59%
TOPIX (JP) Jul-76 2.29% 18.66%
AEX (NL) Jan-75 7.72% 19.18%
FTSE 100 (UK) Jan-75 6.97% 17.77%
S&P 500 (US) Jan-65 3.47% 15.45% -4.6% 5.4%
Bond Futures
3-year AUS Jan-92 1.34% 2.57%
10-year AUS Dec-85 3.83% 8.53%
2-year EURO Mar-97 1.02% 1.53%
5-year EURO Jan-93 2.56% 3.22%
10-year EURO Dec-79 2.40% 5.74%
30-year EURO Dec-98 4.71% 11.70%
10-year CAN Dec-84 4.04% 7.36%
10-year JP Dec-81 3.66% 5.40%
10-year UK Dec-79 3.00% 9.12%
2-year US Apr-96 1.65% 1.86% 1.9% 11.3%
5-year US Jan-90 3.17% 4.25% 3.0% 9.2%
10-year US Dec-79 3.80% 9.30% 0.4% 8.0%
30-year US Jan-90 9.50% 18.56% -1.4% 6.2%
Currency Forwards
AUD/USD Mar-72 1.85% 10.86% 12.4% 28.8%
EUR/USD Sep-71 1.57% 11.21% 12.1% 18.7%
CAD/USD Mar-72 0.60% 6.29% 4.7% 24.1%
JPY/USD Sep-71 1.35% 11.66% -6.0% 23.8%
NOK/USD Feb-78 1.37% 10.56%
NZD/USD Feb-78 2.31% 12.01% 38.8% 33.8%
SEK/USD Feb-78 -0.05% 11.06%
CHF/USD Sep-71 1.34% 12.33% -5.2% 26.8%
GBP/USD Sep-71 1.39% 10.32% 2.7% 25.4%
54
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Table 2. T-statistics of the Alphas of Time Series Momentum Trend Strategies with
Different Look-Back and Holding Periods
Reported are the t-statistics of the alphas (intercepts) from time series regressions of the returns of time
series momentum or trend strategies over various look-back and holding periods on the following factor
portfolios: MSCI World equity market index, Lehman Brothers bond market index, S&P GSCI Index, and
HML, SMB, and UMD Fama and French factors from Ken French's website. Panel A reports results for all
asset classes, Panel B for commodity futures, Panel C for equity index futures, Panel D for bond futures,
and Panel E for currency forwards.
1 3 6 9 12 24 36 48
1 4.34 4.68 3.83 4.29 5.12 3.02 2.74 1.90
3 5.35 4.42 3.54 4.73 4.50 2.60 1.97 1.52
6 5.03 4.54 4.93 5.32 4.43 2.79 1.89 1.42
9 6.06 6.13 5.78 5.07 4.10 2.57 1.45 1.19
12 6.61 5.60 4.44 3.69 2.85 1.68 0.66 0.46
24 3.95 3.19 2.44 1.95 1.50 0.20 -0.09 -0.33
36 2.70 2.20 1.44 0.96 0.62 0.28 0.07 0.20
48 1.84 1.55 1.16 1.00 0.86 0.38 0.46 0.74
1 2.44 2.89 2.81 2.16 3.26 1.81 1.56 1.94
3 4.54 3.79 3.20 3.12 3.29 1.51 1.28 1.62
6 3.86 3.53 3.34 3.43 2.74 1.59 1.25 1.48
9 3.77 4.05 3.89 3.06 2.31 1.27 0.71 1.04
12 4.66 4.08 2.64 1.85 1.46 0.58 0.14 0.57
24 2.83 2.15 1.24 0.58 0.18 -0.60 -0.33 -0.14
36 1.28 0.74 0.07 -0.25 -0.34 -0.03 0.34 0.65
48 1.19 1.17 1.04 1.01 0.92 0.75 1.16 1.29
1 1.05 2.36 2.89 3.08 3.24 2.28 1.93 1.28
3 1.48 2.23 2.21 2.81 2.78 2.00 1.57 1.14
6 3.50 3.18 3.49 3.52 3.03 2.08 1.36 0.88
9 4.21 3.94 3.79 3.30 2.64 1.96 1.21 0.75
12 3.77 3.55 3.03 2.58 2.02 1.57 0.78 0.33
24 2.04 2.22 1.96 1.70 1.49 0.87 0.43 0.13
36 1.86 1.66 1.26 0.90 0.66 0.34 0.02 0.08
48 0.81 0.84 0.58 0.44 0.36 0.12 0.01 0.23
1 3.31 2.66 1.84 2.65 2.88 1.76 1.60 1.40
3 2.45 1.52 1.10 1.99 1.80 1.27 1.05 1.00
6 2.16 2.04 2.18 2.53 2.24 1.71 1.36 1.37
9 2.93 2.61 2.68 2.55 2.43 1.83 1.17 1.40
12 3.53 2.82 2.57 2.42 2.18 1.47 1.12 0.96
24 1.87 1.55 1.62 1.66 1.58 1.01 0.90 0.64
36 1.97 1.83 1.70 1.62 1.73 1.13 0.75 0.91
48 2.21 1.80 1.53 1.43 1.26 0.72 0.73 1.22
Panel E: Currency Forwards
1 3.16 3.20 1.46 2.43 2.77 1.22 0.83 -0.42
3 3.90 2.75 1.54 3.05 2.55 1.02 0.10 -0.84
6 2.59 1.86 2.32 2.82 2.08 0.62 -0.16 -1.14
9 3.40 3.16 2.65 2.35 1.72 0.20 -0.38 -1.17
12 3.41 2.40 1.65 1.25 0.71 -0.29 -1.01 -1.67
24 1.78 0.99 0.53 0.27 -0.05 -1.15 -1.88 -2.27
36 0.73 0.42 -0.04 -0.42 -0.96 -1.67 -2.04 -2.42
48 -0.55 -1.05 -1.41 -1.62 -1.79 -2.02 -2.34 -2.32
)shtnoM(
doireP
kcabkooL
Panel A: All Assets
)shtnoM(
doireP
kcabkooL
Panel B: Commodity Futures
)shtnoM(
doireP
kcabkooL
)shtnoM(
doireP
kcabkooL
)shtnoM(
doireP
kcabkooL
Holding Period (Months)
Panel C: Equity Index Futures
Panel D: Bond Futures
55
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Table 3. Performance of the Diversified Time Series Momentum Strategy
Panel A reports results from time series regressions of monthly and non-overlapping quarterly returns on
the diversified time series momentum strategy, that takes an equal weighted average of the time series
momentum strategies across all futures contracts in all asset classes, on the returns of the MSCI World
stock market index and the Fama and French factors SMB, HML, and UMD, representing the size, value,
and cross-sectional momentum premia in U.S. stocks. Panel B reports results using the Asness,
Moskowitz, and Pedersen (2010) Value and Momentum Everywhere factors instead of the Fama and
French factors, which capture the premia to value and momentum globally across asset classes. Panel C
reports results from regressions of the time series momentum returns on the market, volatility, funding
liquidity, and sentiment indicators and their extremes.
Panel A: Fama and French Factors
MSCI
SMB HML UMD Intercept R2
World
Coefficient 0.09 -0.05 -0.01 0.28 1.58% 14%
Monthly
(t-stat) (1.89) (-0.84) (-0.21) (6.78) (7.99)
Coefficient 0.07 -0.18 0.01 0.32 4.75% 23%
Quarterly
(t-stat) (1.00) (-1.44) (0.11) (4.44) (7.73)
Panel B: Asness, Moskowitz, and Pedersen (2010) Factors
MSCI VAL MOM
Intercept R2
World Everywhere Everywhere
Coefficient 0.11 0.14 0.66 1.09% 30%
Monthly
(t-stat) (2.67) (2.02) (9.74) (5.40)
Coefficient 0.12 0.26 0.71 2.93% 34%
Quarterly
(t-stat) (1.81) (2.45) (6.47) (4.12)
Panel C: Market, Volatility, Liquidity, and Sentiment Extremes
MSCI
MSCI TED Spread VIX Top
World TED Spread VIX
World Top 20% 20%
Squared
Coefficient -0.01 1.99
Quarterly
(t-stat) (-0.17) (3.88)
Coefficient -0.001 -0.008
Quarterly
(t-stat) (-0.06) (-0.29)
Coefficient 0.001 -0.003
Quarterly
(t-stat) (0.92) (-0.10)
Change in
Sentiment Change in
Sentiment Change in Sentiment
Sentiment Bottom Sentiment
Top 20% Sentiment Bottom
20% Top 20%
20%
Coefficient 0.03 -0.01 -0.01
Quarterly
(t-stat) (0.73) (-0.27) (-0.12)
Coefficient -0.01 0.02 0.01
Quarterly
(t-stat) (-1.08) (1.25) (0.66)
56
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Table 4. Correlations of Time Series Momentum Strategy Returns Within and
Across Asset Classes
Panel A reports for each asset class the average pair-wise correlation of each instruments’ 12-month time
series momentum strategy returns, as well as a passive long position in each instrument, within the asset
class. Panel B reports the correlation of time series momentum strategies (below the diagonal) and passive
long positions (above the diagonal) across asset classes, where an equal weighted average of the
instruments within each asset class is first formed and then the correlations between the equal weighted
portfolios across asset classes are calculated. Correlations are calculated from monthly returns over the
period January 1985 to December 2009.
Panel A: Average Pair-Wise Correlation Within Asset Class
Commodities Equities Fixed Income Currencies
TS-MOM strategies 0.07 0.37 0.38 0.10
Passive long positions 0.19 0.60 0.63 -0.04
Panel B: Average Correlation Across Asset Classes
Correlations of TS-MOM strategies
Commodities 1
Equities 0.20 1
Fixed Income 0.07 0.21 1
Currencies 0.13 0.20 0.05 1
Correlations of passive long positions
Commodities 1
Equities 0.17 1
Fixed Income -0.12 -0.03 1
Currencies -0.12 -0.20 0.02 1
57
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Table 5. Time series Momentum vs. Cross-Sectional Momentum
Panel A reports results from regressions of the 12-month time series momentum strategies by asset class
(TSMOM) on 12-month cross-sectional momentum strategies (XS-MOM) of Asness, Moskowitz, and
Pedersen (2010). Panel B reports results from the decomposition of cross-sectional momentum and time
series momentum strategies according to Section 4.B., where Auto is the component of profits coming from
the auto-covariance of returns, Cross is the component coming from cross-serial correlations or lead-lag
effects across the asset returns, Mean is the component coming from cross-sectional variation in
unconditional mean returns, and Mean squared is the component coming from squared mean returns. Panel
C reports results from regressions of several XS-MOM strategies in different asset classes, the Fama-
French momentum, value, and size factors, and two hedge fund indices obtained from Dow Jones/Credit
Suisse on the TSMOM factor.
Panel A: Regression of TS-MOM on XS-MOM
Independent Variables
XS-
XS- XS- XS- XS-
XS- MOM
MOM MOM MOM MOM Intercept R2
MOM FI US
ALL COM EQ FX
Stocks
0.66 0.76% 44%
TS-MOM ALL
(15.17) (5.90)
0.31 0.20 0.17 0.37 0.12 0.73% 46%
TS-MOM ALL
(7.09) (4.25) (3.84) (8.11) (2.66) (5.74)
0.65 0.57% 42%
TS-MOM COM
(14.61) (4.43)
0.62 0.05 0.02 0.14 0.05 0.51% 45%
TS-MOM COM
(13.84) (1.01) (0.50) (3.08) (1.06) (3.96)
0.39 0.47% 15%
TS-MOM EQ
(7.32) (3.00)
0.07 0.28 0.04 0.06 0.24 0.43% 22%
TS-MOM EQ
(1.29) (5.07) (0.67) (1.11) (4.26) (2.79)
0.37 0.59% 14%
TS-MOM FI
(6.83) (3.77)
-0.03 0.18 0.34 0.01 0.03 0.50% 17%
TS-MOM FI
(-0.62) (3.05) (6.19) (0.20) (0.48) (3.15)
0.75 0.42% 56%
TS-MOM FX
(19.52) (3.75)
0.04 0.00 -0.01 0.75 -0.01 0.40% 56%
(1.07) (0.04) (-0.17) (18.89) (-0.24) (3.49)
elbairaV
tnednepeD
TS-MOM FX
58
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Panel B: Decomposition of TS-MOM and XS-MOM
XS-MOM Decomposition TS-MOM Decomposition
Mean
Auto Cross Mean Total Auto Total
Squared
0.53% -0.03% 0.12% 0.61% 0.54% 0.29% 0.83%
ALL
0.41% -0.13% 0.11% 0.39% 0.43% 0.17% 0.59%
COM
0.74% -0.62% 0.02% 0.14% 0.83% 0.17% 1.00%
EQ
0.32% -0.10% 0.05% 0.27% 0.35% 0.70% 1.05%
FI
0.71% -0.55% 0.02% 0.18% 0.80% 0.17% 0.96%
FX
Panel C: What Factors Does TSMOM Explain?
Independent Variable
TSMOM
Intercept R 2
ALL
0.66 -0.16% 44%
XS-MOM ALL
(15.17) (-1.17)
0.65 -0.09% 42%
XS-MOM COM
(14.61) (-0.66)
0.39 0.29% 15%
XS-MOM EQ
(7.32) (1.86)
0.37 -0.14% 14%
XS-MOM FI
(6.83) (-0.87)
0.75 -0.19% 56%
XS-MOM FX
(19.52) (-1.71)
0.49 -0.28% 13%
UMD
(6.56) (-0.93)
-0.07 0.43% 1%
HML
(-1.46) (2.08)
-0.01 0.10% 0%
SMB
(-0.26) (0.49)
0.55 -0.30% 33%
DJCS MF
(9.60) (-1.37)
0.32 0.52% 14%
DJCS MACRO
(5.64) (2.38)
elbairaV
tnednepeD
59
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633

Table 6. Time Series Predictors of Returns: Spot Prices, Roll Returns, and Positions
Reported are results from regressions of the monthly futures return on the previous 12 months futures
return (“Full TS Mom” ), previous 12 months change in spot price (“Spot Price Mom” ), past 12-month roll
return (“Roll Mom” ), and the 12-month change and average level in speculators’ aggregate net (i.e., long
minus short) positions as a percent of open interest (“Net Speculator Position”). Also reported are
interactions between the change in net speculator positions and the spot and roll returns over the previous
12 months.
Chg Net Net Spot MOM Roll MOM
Full TS- Spot Price Roll
Speculator Speculator x Chg Net x Chg Net Intercept R2
Mom MOM MOM
Position Position Spec Pos Spec Pos
Coefficient 0.019 0.09% 0.6%
T-stat (3.57) (1.31)
Coefficient 0.014 0.12% 0.3%
T-stat (2.29) (1.71)
Coefficient 0.024 0.08% 0.3%
T-stat (3.22) (1.08)
Coefficient 0.007 0.12% 0.2%
T-stat (2.67) (1.63)
Coefficient 0.007 0.08% 0.2%
T-stat (2.33) (1.12)
Coefficient 0.017 0.004 0.09% 0.7%
T-stat (3.13) (1.65) (1.33)
Coefficient 0.018 0.002 0.08% 0.6%
T-stat (3.31) (0.76) (1.14)
Coefficient 0.017 0.030 0.08% 0.6%
T-stat (2.74) (3.90) (1.03)
Coefficient 0.014 0.030 0.005 0.07% 0.8%
T-stat (2.12) (3.94) (1.89) (0.99)
Coefficient 0.014 0.030 0.005 0.023 0.015 0.06% 0.8%
T-stat (2.17) (3.94) (1.78) (1.38) (0.49) (0.77)
60
EElleeccttrroonniicc ccooppyy aavvaaiillaabbllee aatt:: hhttttppss::////ssssrrnn..ccoomm//aabbssttrraacctt==22008899446633
