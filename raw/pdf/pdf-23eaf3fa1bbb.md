---
id: pdf-23eaf3fa1bbb
type: pdf
title: white_paper
url: ''
authors: []
ingested_at: '2026-04-29T16:27:27Z'
content_hash: sha256:85c8b4dd0e4d9c80255e79b81ea6b2ba78e450a0d9ef7a5a0b6e0a10ee723d60
source_path: raw/pdf/pdf-23eaf3fa1bbb.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 8
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/white_paper.pdf
published_at: '2020'
---
Gamma Exposure
Disclaimer
The information contained in these documents is con5dential, privileged and only for the
information of the intended recipient and may not be used, published, or redistributed
without the prior written consent of Prior Analytics LLC. The opinions expressed are in good
faith and while every care has been taken in preparing these documents, Prior Analytics LLC
makes no representations and gives no warranties of whatever nature in respect of these
documents, including but not limited to the accuracy or completeness of any information,
facts and/or opinions contained therein. Prior Analytics LLC, its subsidiaries, the directors,
employees and agents cannot be held liable for the use of and reliance of the opinions,
estimates, forecasts and 5ndings in these documents.
http://sqzme.co December 2017 1
sales@sqzme.co

Gamma Exposure
Gamma Exposure ( )™
GEX
Quantifying hedge rebalancing in SPX options
SqueezeMetrics
Research March 2016
Revised December 2017
A survey of academic literature and the methods of market practitioners
suggests that the relationship between the equity option market and its
underlying stocks is still very poorly understood.
Historically, the published research on the eQect of equity options on
underlying prices has been limited to theorizing about the eQects of option
introduction and expiration. Meanwhile, practitioners refer almost
exclusively to the volatility and variance 5gures implied by the quotes of only
a small strip of strike prices, interpolated across two near-term contracts.
Since few have even acknowledged the pervasive impact of existing options
on their underlying stocks, none have put forward a pragmatic model for
predicting the day-to-day impact of those options. Gamma Exposure (GEX)™
is the 5rst attempt at such a model.
An Illustration
The S&P 500 Index (SPX) has a large and deeply liquid market for cash-settled
options. The commonly cited CBOE Volatility Index (VIX) is derived from
these options. As a calculation of 30-day option-implied variance, VIX uses a
selection of quoted prices to derive what can be considered, put simply, an
estimate of how much the S&P 500 will move in the future.
As you might expect, VIX is eQective at predicting 30-day future realized
volatility―the CBOE places the correlation at 0.75. But the VIX is more
* CBOE
strongly correlated (0.85) to the realized volatility of the previous month.*
(see References)
This calls into question whether VIX can be used to forecast SPX variance.
In that vein, the VIX clearly fails to generate suitably distinguishable future
stock return distributions at its lower readings. The 1-day standard deviation
of SPX returns following the lowest quartile of spot VIX closes (0.51%) is not
a great deal diQerent from that of the second-lowest quartile (0.66%). A VIX
of 12 means about the same as 15 when it comes to predicting variance.
When instead we compare the highest and second-highest** quartiles of GEX
** Like low VIX,
to subsequent SPX variance, the 1-day standard deviations are 0.55% and
high GEX predicts
0.85%, respectively. On an index trading at 2000, the diQerence between
low volatility.
0.66% and 0.85% is a 4-point diQerence in range every day.
http://sqzme.co December 2017 2
sales@sqzme.co

Gamma Exposure
http://sqzme.co December 2017 3
sales@sqzme.co

Gamma Exposure
We believe that the greater granularity of the GEX distributions suggests
that there is some element of market volatility that is simply not able to be
captured by the VIX model, or indeed any other variance metric based on
quoted option prices. Rather than prices, GEX concerns itself with the
quantity and characteristics of all existing option contracts at all strikes, and
at all expirations―and the market participants who trade them.
Dynamic Hedging
The predictive power of GEX is essentially driven by the necessity of option
dealers' (market makers') re-hedging activities. In order to limit risk and
realize pro5t, an option market-maker must limit his exposure to deltas.
* It is easier to
If, e.g., a market-maker sells a single, 20-delta put contract to an investor, he
speak of dynamic
must then short-sell approximately 20 shares of the underlying stock* in
hedging in terms of
order to (temporarily) neutralize the convexity eQect of the option's gains
shares, but SPX
and losses. Since the convexity itself cannot be hedged away, the market-
options have no
maker must commit to re-hedging the option to its new delta whenever the
underlying shares,
and can be hedged underlying price changes enough to justify action.
with futures.
If in one case the price of the underlying falls and the put delta rises from 20
to 50, the market-maker will be compelled to short-sell an additional 30
shares of the underlying to stay delta-neutral. If instead the underlying rises
and the put delta falls to 0, the market-maker would buy back the previously
shorted shares. Thus, a market-maker is essentially committed to a
predictable and quanti5able regimen of buying and selling stock.
Four Assumptions
The size and liquidity of the equity option market is what makes it possible
to glean predictive information from the impact of hedging activity, but it
also introduces some challenges. With a few assumptions, we attempt to
overcome those challenges:
1. All traded options are facilitated by delta-hedgers. This is to say that every
option contract is either bought by, or sold by, a market participant whose
business is to pro5tably manage a book of options.
2. Call options are sold by investors; bought by market-makers. It is dihcult to
determine the “direction” of a trade in an ultra-liquid market, as in the case
of SPX options. A vast majority will trade at the midpoint of the bid and ask.
It is apparent from an analysis of skew, open interest at strike, and
(circularly) the eQects of GEX, however, that the practice of call overwriting
(and stock collaring) drives the market for calls.
3. Put options are bought by investors; sold by market-makers. As with calls,
puts are primarily used by investors who are already exposed to the
underlying market, and who are looking to modify the return pro5le of their
portfolio by using options. The “protective put” commands a premium for
http://sqzme.co December 2017 4
sales@sqzme.co

Gamma Exposure
this reason, thus inkuencing the apparent vertical skew of index options.
4. Market-makers hedge precisely to the option delta. If market-makers hedged
their deltas every time an option's delta changed, they would be trading
incessantly. In reality, market-makers utilize “hedging bands” to balance the
twin challenges of hedging costs and delta risk. Since it is not feasible to
gauge the breadth of every market-maker's hedging band, we simply use the
delta of the option.
With these assumptions we can compute GEX.
Computation
The gamma of an option is the 5rst derivative of its delta, expressed as the
rate of change of delta per 1-point move in the underlying. To calculate the
GEX of an option, we need to determine the share impact of that potential
change in delta on a market-maker's book.
Thus, if the gamma of a single 50-delta call option is 10, we can assume that
a market-maker will re-hedge that option to either 40 or 60 delta in the
event of any ±1 point move in the underlying. In either case, the market-
maker will need to trade 10 shares. E.g., if the underlying moves up 1 point
and the new delta is 60, the market-maker will short-sell 10 shares. If the
underlying moves down 1 point and the new delta is 40, the market-maker
will buy back 10 shares.
In the case of a put option (assumed to be held short by a market-maker), the
mechanism is the same, whereby re-hedging involves selling shares as delta
rises and buying as delta falls.
To calculate the GEX (in shares*) of all call options at a particular strike price
in a contract:
* When computing
for SPX, we GEX = Г · OI · 100
denominate GEX in
dollars. Where Г is the option's gamma, OI is the open interest in the particular
option strike, and 100 is the adjustment from option contracts to shares of
the underlying.
In the case of put options:
GEX = Г · OI · (-100)
The share adjustment is negative here because for market-makers, where
calls represent long gamma, puts represent short gamma.
The GEX of a stock (or index) is the summation of GEX at every strike price in
every available contract.
http://sqzme.co December 2017 5
sales@sqzme.co

Gamma Exposure
Market Impact
Using the above computations, a GEX 5gure that is positive implies that
option market-makers will hedge their positions in a fashion that stikes
volatility (buying into lows, selling into highs). A GEX 5gure that is negative
implies the opposite (selling into lows, buying into highs), thus magnifying
market volatility.
A corollary is that a GEX 5gure approaching zero will allow the market to
move naturally and without any particular interference from market-makers'
re-hedging activities.
The 5gure below, plotting SPX returns against SPX options' prior day Gamma
Exposure, bears this out.
Note the exponential increase in volatility as GEX trends below zero, and the
gradual tightening of the distribution as GEX rises.
It would be dihcult to come up with an alternate explanation for this
behavior.
http://sqzme.co December 2017 6
sales@sqzme.co

Gamma Exposure
Beyond SPX
As implied by its computation, GEX can be used to forecast return
distributions in any optionable equity with enough open interest to
inkuence prices. Aggregating GEX data across a basket of stocks or sectors in
order to gauge potential risk or return potential is another plausible use-
case.
An investment process that selected potential investments from the
components of the S&P 500 by screening for a GEX near zero yielded excess
returns.
All of the above are subjects for further investigation.
Conclusion
If investors continue to look toward the option market for alpha signals and
risk assessments, they would do well to consider Gamma Exposure as a
smarter alternative to price-derived volatility and variance estimates.
The key de5ciency in using option prices to gauge future volatility is that no
two market-makers' books are the same, and a tight spread from any one
market-maker completely obscures the risk appetite of every other. This
problem is readily ameliorated by computing the GEX of options known to
be in circulation and deriving projected return distributions from the
historical market impact of those contracts.
And so, when―in light of the evidence―investors eventually acknowledge
that the option market does have a truly pervasive, day-to-day impact on the
paths and volatilities of stock prices, we think that it is a natural next step to
consider GEX an essential addition to the equity investment process.
http://sqzme.co December 2017 7
sales@sqzme.co

Gamma Exposure
References
Avellaneda, Marco and Michael D. Lipkin, 2003, A market-induced mechanism for stock pinning.
Quantitative Finance 3, 417–425.
Chicago Board Options Exchange, 1976, Analysis of volume and price patterns in stocks underlying
CBOE options from December 30, 1974 to April 30, 1975, Chicago Board Options Exchange.
CBOE, https://cfe.cboe.com/cfe-education/cboe-volatility-index-vx-futures/vix-primer/historical-
performan ce
CBOE, https://www.cboe.com/micro/vix/vixwhite.pdf
Frey, R. and A. Stremme, 1997, Market volatility and feedback eQects from dynamic hedging,
Mathematical Finance 7, No. 4, 351–374.
Pearson, Neil D. and Poteshman, Allen M. and White, Joshua S., Does Option Trading Have a Pervasive
Impact on Underlying Stock Prices? (February 23, 2007). AFA 2008 New Orleans Meetings Paper.
Available at SSRN: https://ssrn.com/abstract=970592 or http://dx.doi.org/10.2139/ssrn.970592
Sorescu, S. M., 2000, The eQect of options on stock prices: 1973 to 1995, Journal of Finance 55, 487–
514.
http://sqzme.co December 2017 8
sales@sqzme.co
