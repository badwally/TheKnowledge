---
id: pdf-b8cec9d1ec0c
type: pdf
title: w28967
url: ''
authors: []
ingested_at: '2026-04-29T16:27:19Z'
content_hash: sha256:adc69b89dee01f8035192f263c16215432a435d9648bbd793c66e93a860d2e70
source_path: raw/pdf/pdf-b8cec9d1ec0c.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 54
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/w28967.pdf
published_at: '2021'
---
NBER WORKING PAPER SERIES
IN SEARCH OF THE ORIGINS OF FINANCIAL FLUCTUATIONS:
THE INELASTIC MARKETS HYPOTHESIS
Xavier Gabaix
Ralph S. J. Koijen
Working Paper 28967
http://www.nber.org/papers/w28967
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
June 2021
We thank Ehsan Azarmsa, Aditya Chaudhry, Antonio Coppola, Zhiyu Fu, Dong Ryeol Lee, Hae-
Kang Lee, Simon Oh, and Lingxuan Wu for excellent research assistance. We thank Francesca
Bastianello, Jean-Philippe Bouchaud, Michael Brandt, John Campbell, Francesco Franzoni,
Robin Greenwood, Valentin Haddad, Lars Hansen, Sam Hanson, John Heaton, Tim Johnson,
Arvind Krishnamurthy, Spencer Kwon, John Leahy, Hanno Lustig, Alan Moreira, Knut Mork,
Toby Moskowitz, Stefan Nagel, Jonathan Parker, Lasse Pedersen, Joel Peress, Jean-Charles
Rochet, Ivan Shaliastovich, Andrei Shleifer, Jeremy Stein, Johannes Stroebel, Larry Summers,
Adi Sunderam, Jean Tirole, Harald Uhlig, Dimitri Vayanos, Motohiro Yogo, and participants at
various seminars for comments. Gabaix thanks the Sloan Foundation for financial support. Koijen
acknowledges financial support from the Center for Research in Security Prices at the University
of Chicago Booth School of Business. The views expressed herein are those of the authors and do
not necessarily reflect the views of the National Bureau of Economic Research.
NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.
© 2021 by Xavier Gabaix and Ralph S. J. Koijen. All rights reserved. Short sections of text, not
to exceed two paragraphs, may be quoted without explicit permission provided that full credit,
including © notice, is given to the source.

In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis
Xavier Gabaix and Ralph S. J. Koijen
NBER Working Paper No. 28967
June 2021
JEL No. E7,G1,G32,G4
ABSTRACT
We develop a framework to theoretically and empirically analyze the fluctuations of the
aggregate stock market. Households allocate capital to institutions, which are fairly constrained,
for example operating with a mandate to maintain a fixed equity share or with moderate scope for
variation in response to changing market conditions. As a result, the price elasticity of demand of
the aggregate stock market is small, and flows in and out of the stock market have large impacts
on prices.
Using the recent method of granular instrumental variables, we find that investing $1 in the stock
market increases the market's aggregate value by about $5. We also develop a new measure of
capital flows into the market, consistent with our theory. We relate it to prices, macroeconomic
variables, and survey expectations of returns.
We analyze how key parts of macro-finance change if markets are inelastic. We show how
general equilibrium models and pricing kernels can be generalized to incorporate flows, which
makes them amenable to use in more realistic macroeconomic models and to policy analysis.
Our framework allows us to give a dynamic economic structure to old and recent datasets
comprising holdings and flows in various segments of the market. The mystery of apparently
random movements of the stock market, hard to link to fundamentals, is replaced by the more
manageable problem of understanding the determinants of flows in inelastic markets. We
delineate a research agenda that can explore a number of questions raised by this analysis, and
might lead to a more concrete understanding of the origins of financial fluctuations across
markets.
Xavier Gabaix
Department of Economics
Harvard University
Littauer Center
1805 Cambridge St.
Cambridge, MA 02138
and NBER
xgabaix@fas.harvard.edu
Ralph S. J. Koijen
University of Chicago
Booth School of Business
5807 S Woodlawn Ave
Chicago, IL 60637
and NBER
Ralph.koijen@chicagobooth.edu
An online appendix is available at http://www.nber.org/data-appendix/w28967

1 Introduction
One key open question is why the stock market exhibits so much volatility. This paper provides
a new model and new evidence suggesting that this is because of flows and demand shocks in
surprisingly inelasticmarkets. Wemake thecasefor thistheoretically andempirically, and delineate
some of the numerous implications of that perspective.
We start by asking a simple question: when an investor sells $1 worth of bonds and buys $1
worth of stocks, what happens to the valuation of the aggregate stock market? In the simplest
“efficient markets” model, the price is the present value of future dividends, so the valuation of the
aggregate market should not change. However, we find both theoretically and empirically, using
an instrumental variables strategy, that the market’s aggregate value goes up by about $5 (our
estimates are between $3 and $8, and we will use $5 for simplicity in the theory and discussion).1
Hence, the stock market in this simple model is a very reactive economic machine, which turns an
additional $1 of investment into an increase of $5 in aggregate market valuations.
Put another way, if investors create a flow of 1% as a fraction of the value of equities, the model
implies that the value of the equity market goes up by 5%. This is the mirror image of the low
aggregate price-elasticity of demand for stocks: if the price of the equity market portfolio goes up
by 5%, demand falls by only 1%, so that the price elasticity is 0.2. In contrast, most rational or
behavioral models would predict a very small impact, about 100 times smaller, and a price elasticity
about 100 times larger. This high sensitivity of prices to flows has large consequences: flows in the
market and demand shocks affect prices and expected returns in a quantitatively important way.
We refer to this notion as the “inelastic markets hypothesis.”
We lay out a simple model explaining market inelasticity. In its most basic version, a represen-
tative consumer can invest in two funds: a pure bond fund, and a mixed fund that invests in stocks
and bonds according to a given mandate — for instance, that 80% of the fund’s assets should be
invested in equities. Then, we trace out what happens if the consumer sells $1 of the pure bond
fund and invests this $1 in the mixed fund. The mixed fund must invest this inflow into stocks and
bonds: but that pushes up the prices of stocks, which again makes the mixed fund want to invest
more in stocks, which pushes prices up, and so on. In equilibrium, we find that the total value of
the equity market increases by $5.
Then, the paper explores inelasticity in richer setups and finds that the ramifications of this
simple model are robust. For instance, the core economics survives, suitably modified, if the fund
is more actively contrarian, so that its policy is to buy more equities when the expected excess
return on equities is high. Moreover, the model aggregates well. If different investors have different
elasticities, the total market elasticity is the size-weighted elasticity of market participants. Impor-
tantly, the correct measure of size is the share of equity they hold. The model also clarifies how to
measure net flows into the aggregate stock market (even though for every buyer there is a seller),
which guides the empirical analysis. Moreover, it extends readily to an infinite horizon: in that
case, the price today is influenced by the cumulative inflows to date and the present value of future
expected flows — divided again by the market elasticity.
Theempiricalcoreofthispaperistoprovideaquantificationofthemarket’saggregateelasticity.
To do that, we use a new instrumental variables approach, which was conceived for this paper and
workedoutinastand-alonepaper(GabaixandKoijen(2020)), the“granularinstrumentalvariables”
1The price impact is linear and symmetric: selling $2 worth of equities (buying $2 worth of bonds) decreases the
valuation of aggregate equities by $10.
2

(GIV) approach. The key idea is that we use the idiosyncratic demand shocks of large institutions
or sectors as a source of exogenous variation. We extract these idiosyncratic shocks from factor
models estimated on the changes in holdings of various institutions and sectors. We then take the
size-weighted sum of these idiosyncratic shocks (the GIV), and use it as a primitive instrument
to see how these demand shocks affect aggregate prices and the demand of other investors. This
way, we can estimate both the aggregate sensitivity of equity prices to demand shocks (which is the
multiplier around 5 we mentioned above) and the demand elasticity of various institutions (around
0.2).
Importantly, the data are consistent with a quite long-lasting price impact of flows. Indeed, in
the simplest version of the model, the price impact is perfectly long-lasting. This is not necessarily
because flows release information, but instead simply because the permanent shift in the demand
for stocks must create a permanent shift in their equilibrium price. We perform a large number of
robustness checks, for example using different data sets (the Flow of Funds as well as 13F filings).
Thefindingsareconsistentacrossspecifications,inthesensethatthepriceimpactmultiplierremains
around 5. We also construct a measure of capital flows into the market. We find that this measure
is strongly correlated with realized returns and survey expectations of returns, but it is only weakly
correlated with macroeconomic growth.
Here are three a priori reasons to entertain that markets would be inelastic First of
all, if one wants to buy $1 worth of equities, many funds actually cannot supply that: for instance, a
fund that invests entirely in equities cannot exchange them for bonds. Many institutions have tight
mandates, something that we confirm empirically. Relatedly, it is hard to find investors who could
act as macro arbitrageurs. For instance, hedge funds are relatively small (they hold less than 5% of
the equity market), and they tend to reduce their equity allocations in bad times (due to outflows
and binding risk constraints; see Ben-David et al. (2012)). Second, the transfer of equity risk across
investor sectors is small (about 0.6% of the aggregate value of the equity market per quarter for
the average pair of investor sectors). This implies that the demand elasticity of most investors is
quite small or that investors experience nearly identical demand shocks (as if they were to disagree,
we would see large flows in elastic markets), something which may be implausible. Third, a large
literature estimates demand elasticities for individual stocks using a variety of methodologies, where
the latest estimates of this “micro” demand elasticity are approximately 1 (we provide complete
references below). As the macro elasticity should arguably be lower than the micro elasticity
(considering that, for example, Ford and General Motors are closer substitutes than the stock
market index and a bond), this suggests a low macro elasticity, perhaps less than 1. Consistent
with this reasoning, a new literature explores elasticities for “factors” in the US, such as size and
value, and finds elasticities of around 0.2. Hence, in light of this existing evidence, our low macro
elasticity may be less surprising.
Suppose that the “inelastic markets hypothesis” is true; why do we care? First, investor-
specificflowsanddemandshocksarequantitativelyimpactful. Asaresult, onecanreplacethe“dark
matter” of asset pricing (whereby price movements are explained by hard-to-measure latent forces)
with tangible flows and the demand shocks of different investors. This suggests a research program
in which determinants of asset prices can be traced back to measurable demand shocks and flows
of concrete investors. By studying the actions of these investors, we can infer their demand curves,
and theorize about their determinants.
3

If equity markets are indeed inelastic, several questions that are irrelevant or uninteresting in
traditional models become interesting. For instance, if the government buys stocks, stock prices go
up — again by this factor of 5. This may be useful as a policy tool — a “quantitative easing” policy
for stocks rather than long-term bonds. It may also be used to analyze previous policy experiments,
in Hong Kong, Japan, and China, and give a quantitative framework to complement the previous
qualitative discussions of policy proposals of this kind (Tobin (1998); Farmer (2010); Brunnermeier
et al. (2020)).
Also, firms as financiers materially impact the market in our calibration. Prior research showed
that firms react to price signals, such as in their decisions to issue dividends or raise funds in stocks
versus bonds (Baker and Wurgler (2004); Ma (2019)): now we can quantify how firms’ actions
impact the market. For instance, stock buybacks can have a large aggregate effect. Suppose that
the corporate sector buys back $1 worth of equities rather than paying $1 worth of dividends. In the
traditional Modigliani-Miller world, the market value of equities does not change at all. In contrast,
in an inelastic world, the value of equities goes up, by a tentative estimate of around $2.2 As a
naive non-economist might think, “if firms buy shares, that drives up the price of shares.” A rational
financial economist might say that this is illiterate. But the naive thinking is actually qualitatively
correct in inelastic markets. Hence, potentially, as share buybacks account for a large portion of
flows (they have been about as large as dividend payments in the recent decade), corporate actions
account for a sizable share of equity purchases, and therefore of the volatility and increase in the
value of the stock market. This “corporate finance of inelastic markets” is an interesting avenue of
research.
If markets are inelastic, then macro-finance should reflect that. Accordingly, we construct a
general equilibrium model in the spirit of Lucas (1978) where there is a central role for flows and
inelasticity. It clarifies the role of demand shocks and flows, the determination of the interest rate,
and shows how to augment traditional general equilibrium models with flows in inelastic markets.
That makes those models more realistic, and better suited for policy. This model may serve as a
prototypeformodelsenrichedbyinelasticity. Indeed, itcalibrateswell, andreplicatesquantitatively
the salient features of the stock market, such as the volatility and size of the equity premium, the
slow mean-reversion of the price-dividend ratio, and the ability to predict stock return with the
price-dividend ratio at different horizons. We also show how the model can be used to match the
strong correlation between prices and subjective beliefs about long-term growth (Bordalo et al.
(2020)), even if fluctuations in beliefs have only a modest impact on actions (Giglio et al. (2021a)),
as the resulting flows are amplified in inelastic markets. We conclude that our general equilibrium
model with “inelastic markets” is competitive with other widely-used general equilibrium models
thatmatchequitymarketmoments, beitviahabitformation(CampbellandCochrane(1999)), long
run risks (Bansal and Yaron (2004)), or variable rare disasters (Gabaix (2012), Wachter (2013)).
In addition to proposing a new amplification mechanism, its main advantage, as we see it, is that
is relies on an observable force, flows in and out of equities.
We also show how to connect flows to the “stochastic discount factor” (SDF) approach: the flows
are primitive, and the SDF is a book-keeping device to record their influence on prices. This model
could be helpful to get correct risk prices in macroeconomic models, including their variation due
to flows.
One limitation of our study is that we postpone to future research the detailed investigation
of what determines flows in the first place: instead, we provide descriptive statistics showing they
2The estimate is tentative, in part as it relies on estimates of the rationality of the consumer after the buybacks.
4

correlate sensibly with other variables, such as prices and measured beliefs. The reason is chiefly
that this would be a stand-alone paper. But we think it is quite doable, and indeed we are working
on this. Rather than studying “shocks to noise traders” abstractly, we replace them with investor-
level flows and demand shocks that may be easier to understand. Indeed, episode by episode, one
can ask questions such as “why did firms lower their buybacks?” (answer: because they had lower
earnings), “why did pension funds buy?” (answer: because their mandate forces them to buy stocks
after stocks fall), or “why did hedge funds sell?” (answer: their investors sold, given their low past
returns).
Literature review Our paper is about the macro elasticity, in contrast to the micro elasticity
estimated in the literature, including Shleifer (1986), Harris and Gurel (1986a), Wurgler and Zhu-
ravskaya (2002), and Duffie (2010).3 We summarize the evidence on existing elasticity estimates in
more detail in Section 2.4.
We build on the insights of De Long et al. (1990), who write an equilibrium model in which
noisy beliefs create demand shocks that move the market and the equity premium. They discuss a
rich set of qualitative ideas, some of which we can formally analyze and quantify, such as the failure
of the Modigliani-Miller theorem and the notion that if most market participants passively hold
the market portfolio, prices react sharply to flows. De Long et al. (1990) dealt with these issues
qualitatively, but, influenced by it, a literature has studied the impact of mutual fund flows in the
market, for example Warther (1995).4 In addition, an active literature studies the impact of mutual
fund and ETF flows on the cross-section of equity prices, for instance Frazzini and Lamont (2008),
Lou (2012), Ben-David et al. (2018), Dou et al. (2020), and Dong et al. (2021). One innovation
of our paper is to provide a systematic quantitative framework to think about this, to include all
sectors (not just mutual funds), and to think about causal inference at the level of the aggregate
stockmarketviaGIV.DeuskarandJohnson(2011a)usehigh-frequencyorderflowdataforS&P500
futures to show that about half of the price variation can be attributed to flows shocks. Moreover,
they find these shocks to be permanent over the horizons that they consider.5
A few papers have modeled how flows might be important, examining general flows in currencies
(Gabaix and Maggiori (2015), Greenwood et al. (2019), Gourinchas et al. (2020)), slow rebalancing
mechanisms in currencies (Bacchetta and Van Wincoop (2010)) and equities (Chien et al. (2012),
who emphasize flows coming from the supply of shares by firms), or switching between types of
stocks (Barberis and Shleifer (2003), Vayanos and Woolley (2013b)). However, we believe we are
thefirsttoconceptuallyandquantitativelyexploretheelasticityoftheaggregatestockmarketusing
a simple economic model to link data on total holdings and flows to fluctuations in the aggregate
stock market. We also provide the first instrumental variables estimate of the elasticity of the US
equity market. Camanho et al. (2019) provide a partial-equilibrium model of exchange rates with
flows, quantified with the GIV methodology developed for the present paper and spelled out in
3A growing literature studies elasticities in global financial markets, see for instance Dierker et al. (2016) and
Charoenwong et al. (2020).
4See also Edelen and Warner (2001), Goetzmann and Massa (2003), and Ben-Rephael et al. (2012).
5Deuskar and Johnson (2011a) study a system of equations in which flows may impact returns and returns may
impact flows. To identify price impact, they rely on identification via heteroskedasticity as in Rigobon (2003). As
onlythedemandshockinfuturesmarketsisused,andnotincashmarkets,wecannotdirectlytranslatetheestimates
intomultipliers. However,undertheassumptionthatflowsincashmarketsarehighlycorrelatedwithflowsinfutures
markets, their results do show that flows explain a large fraction of market fluctuations, which is consistent with the
inelastic markets hypothesis.
5

Gabaix and Koijen (2020).
A related literature finds convincing evidence that supply and demand changes do affect prices
and premia in partially segmented markets, for bonds (for example as in Greenwood and Vayanos
(2014), Greenwood and Hanson (2013), and Vayanos and Vila (2020)), mortgage-backed securities
(Gabaix et al. (2007)), or options (Garleanu et al. (2009)), with models which typically feature
CARA investors and partial equilibrium. Here our focus is on stocks, while our model is quite
different from the models in that literature (in particular, it avoids CARA restrictions on investor
preferences) and is also developed in general equilibrium.
Our work also relates back to the work on flows and asset demand systems by Brainard and
Tobin (1968) and Friedman (1977), among others. This literature faced two important challenges
that we address; first, data on asset holdings were not as readily available as they are now and,
second, there were no obvious methods to identify the slopes of asset demand curves. We share
with Koijen and Yogo (2019) and Koijen et al. (2019) our reliance on holdings data by institutions,
and the desire to estimate a demand function. We are mostly interested in the equilibrium in the
aggregate stock market, as opposed to the cross-sectional focus of Koijen and Yogo (2019), and
we emphasize the role of flows, and the dynamics of prices and capital flows over time. Using a
similar modeling strategy as in Koijen and Yogo (2019), Koijen and Yogo (2020) estimate a global
demand system across global equity and bond markets to understand exchange rates, bond prices,
and equity prices across countries. We also relate to the literature on slow-moving capital (Mitchell
et al. (2007); Duffie (2010); Duffie and Strulovici (2012); Moreira (2019); Li (2018)), providing a
new model for price impact with long-lasting effects, and an identified estimation. Finally, part of
our contribution is a new model of intermediaries (He and Krishnamurthy (2013)), with a central
role for flows, trading mandates, and inelasticity.
Muchmoredistanttoourpaperisthetheoreticalmicrostructureliterature(Kyle(1985)). There,
inflowscausepricechanges, butcruciallythoseinflowsdonotchangetheequitypremiumonaverage
(as the mechanism is rational Bayesian updating, rather than limited risk-bearing capacity, unlike
Kondor and Vayanos (2019)), and hence do not create excess volatility. In contrast, in our paper,
inflows do change the equity premium, creating excessively volatile prices.
Outline Section 2 gives some simple suggestive facts on equity shares and potential macro ar-
bitrageurs such as broker dealers and hedge funds. It also summarizes the existing literature on
elasticity estimates. Section 3 develops our basic model of the stock market: it lays out the basic
notions, and defines clearly elasticity and its link with price impact. It also gives the theoretical
framework that we take to the data. Section 4 contains the empirical analysis, including with an
instrumental variable estimation of the aggregate market elasticity. Section 5 provides a general
equilibrium model that helps to think about how everything fits together: it specializes the ba-
sic model of Section 3 as it endogenizes the interest rate and links cash flows to production and
consumption. Section 6 discusses how the effectiveness of government policy and corporate finance
change with inelastic markets. Section 7 provides a conclusion and thoughts about the research
directions suggested by the present approach. The appendix contains the basic proofs, and details.
The online appendix contains a number of robustness checks and extensions.
Notations We use for equities, E for expectations, and E for equal-weighted averages. We
call δ the average diviEdend-price ratio of the equity market. We generally use lowercase notations
for deviations from a baseline. For a vector X = (X ) and a series of relative shares S with
i i=1...N i
6

N S = 1, we let X := 1 N X , X := N S X , X := X X so that X is the
equ i= a 1 l-w i eighted average E of the N vect i o = r 1 ’s e i leme S nts, X i= i 1 s th i e i size- Γ weighte S d−aver E age, and X E is their
S Γ
d (cid:80) ifference. We define the mean o (cid:80) f X (with i = 1. (cid:80) ..N) with weights ω as: E [X ] := (cid:80) i ωiXi.
i i ω i (cid:80)
i
ωi
2 Data and Suggestive Facts on Equity Shares and Flows
In this section we document several stylized facts and discuss how they are related to our model and
to traditional, elastic asset pricing models. These facts are meant to be no more than suggestive:
the core empirical results are in Section 4, in which we try to carefully quantify the key parameters
of our model.
After discussing the data construction in Section 2.1, we document that institutions often have
quite stable equity shares in Section 2.2, and relatedly we seek to identify investors with elastic
demand for the aggregate stock market in Section 2.3. That is, we ask: who are the deep-pocketed
arbitrageurs that could make the aggregate stock market elastic? This question relates to the work
by Brunnermeier and Nagel (2004), who show that hedge funds did not provide elasticity to the
market during the technology bubble in the late nineties.
2.1 Data sources and construction
We summarize the data sources that we use and define some of the key variables. We leave a
detailed description for Appendix C.
We use sector-level data from the Flow of Funds (FoF) on holdings of equities and bonds as well
as flows into both asset classes. Flows are differences in levels adjusted for mechanical valuation
effects. We compute total bond holdings as the sum of Treasury and corporate bond holdings, and
analogously for flows. As the FoF reports combined values of holdings and flows of foreign and US
assets (except for Treasuries), we adjust these series (Appendix C.1.3). We assume that the flows
transact at end-of-period prices. The sample is quarterly from 1993 to 2018 and we use the June
2019 vintage of the FoF data.6
We use monthly disaggregated data on assets under management, the share invested in US
equities, and flows from Morningstar for mutual funds and ETFs that are domiciled in the US and
that have the US dollar as the base currency. We select the funds in Morningstar’s US category
groups “US Equity,” “Sector Equity,” “Allocation,” and “International Equity.”7 We use the sample
from 1993 to 2019 for mutual funds and from 2002 to 2019 for ETFs.8
For state and local pension funds, we use data from the Center for Retirement Research at
Boston College. The sample is from 2002 to 2019. We use data on the share invested in equities
and fixed income as well as target holdings in equities and fixed income (including cash). State and
local pension funds report once a year (although in different quarters). We use a fund’s actual and
target allocation to equity and fixed income and scale it so that the sum of the shares equals 100%
for each fund.
We use disaggregated data on equity holdings by institutional investors via form 13F filings. We
source the 13F filings from FactSet and the construction is as in Koijen et al. (2019). The sample
6Data of different vintages can be downloaded from this website.
7We remove fund of funds in our analysis to avoid double counting.
8We omit a small number of fund-quarters in which the US equity share exceeds 300% or is lower than -300%, as
these may be data errors.
7

Figure 1: Equity shares. The left panel of the figure plots the equity share in 1993 (orange bars)
and in 2018 (green bars) by institutional sector using Flow of Funds data. The right panel displays
the value-weighted average equity share of mutual funds, ETFs, and state and local pension plans.
The equity share of the different institutions are averaged using the relative equity size of each
investor. The construction of the data is discussed in Appendix C.
5.
4.
3.
2.
1.
0
2018 1993
Househ M ol u d t s ual F fu o n re d S i s g ta n t e s e & c l t o o c r al p E P e T r n i F v s a s i L o t i e n fe p f u i e n n P n s d s u r s o i r o a p n n e c r fu t e y n c & d o s F c m e a p d s a u g n a o i l e t v y s t i r n e s ti u r S e re m ta rs e te n t a f n u d n d lo s cal B g r o o v k t e s r dealer C s los B e a d n − k e s nd funds
erahs
ytiuqE
1
8.
6.
4.
2.
0 1993q1 1997q3 2002q1 2006q3 2011q1 2015q3 2020q1 Date Mutual funds ETFs Pension funds (actual) Pension funds (target)
is from 1999 to 2019.
We use quarterly data on real GDP growth from the St. Louis Federal Reserve Bank FRED
database, series GDPC1. Data on returns with and without dividends are from the Center for
Research in Security Prices. We use the monthly, value-weighted return with and without dividends
to compute the monthly dividend payment.
Lastly, we use survey expectations of returns from Gallup, as also used by Greenwood and
Shleifer (2014), who use the fraction of investors who are bullish (optimistic or very optimistic)
minus the fraction of investors who are bearish. We update their data, which starts in 1996.Q4, to
2018.Q4, and the resulting series has some gaps.
2.2 Institutions often have a quite stable equity share
As a point of reference, we summarize in Figure 1 the evolution of ownership of the US equity
market from 1993 (orange bars) to 2018 (green bars) based on FoF data. During the last 25 years,
equity ownership moved from households’ direct holdings to institutions. The figure understates
this trend as the “household sector” in the FoF includes various institutional investors such as hedge
funds and non-profits (e.g., endowments). Broker dealers, who received much attention in the recent
asset pricing literature, hold only a small fraction of the US equity market. This limits their ability
to provide elasticity to the market.
For some of these sectors, such as mutual funds, exchange-traded funds, and pension funds, we
have investor-level data on equities and fixed income holdings. In the right panel of Figure 1, we
plot the equity share. We aggregate different investors in a given sector using the relative sizes of
their equity portfolios as opposed to assets under management, consistently with our theory (see
the discussion around 15). To appreciate the importance of this difference, consider an economy
with only pure equity and pure bond funds that have the same amount of assets under management.
The equity-weighted equity share equals 100% while the asset-weighted equity share equals only
8

50%. As the relative size of equity and bond assets move, so will the asset-weighted equity share.
Yet, the equity-weighted share will be a constant 100%. It is the equity-weighted equity share that
is relevant per our theory.
The plot shows that equity shares are quite stable over time for broad classes of investors. This
is consistent with many institutions having a rather rigid mandate to maintain a stable equity
share. In the model that we introduce in Section 3, this mandate rigidity will be captured by a low
elasticity (κ) of funds’ asset location to the expected return on equities. In recent work, Cole et
al. (2021) show that a large fraction of households9 also have a high average equity share at 79.2%
with little variation over time (the equity-weighted equity share only drops to 76.4% at the end of
2008). This stability is in part explained by the introduction of target date funds.
2.3 In search of macro arbitrageurs
Figure 1 shows that the equity shares of large groups of investors, such as mutual funds, ETFs, and
pension funds, are stable over time. As the foreign sector consists of similar institutions, this fact
naturally raises the question of who carries out arbitrage across asset classes or, equivalently, which
group of investors aggressively times the market. In the survey that we discuss in the introduction,
two investor sectors are frequently mentioned: hedge funds and broker dealers.10
As Figure 1 shows, broker dealers are very small and hold less than 0.5% of the equity market
directly. So while perhaps important for the micro elasticity, broker dealers are not well-positioned
to absorb large equity flows over longer periods of time. The hedge fund sector is also quite small,
with holdings below 4% of the equity market in long positions going into the financial crisis. Ben-
David et al. (2012) document two important facts. First, hedge funds sold a large fraction of their
equity holdings during the financial crisis, averaging to 3.06% per quarter from 2007.Q3 to 2009.Q1.
Given their small size, this corresponds to selling on average 0.1% of the market each quarter (or
0.7% in total). Redemptions and leverage constraints explain about 80% of this decline in equity
holdings. Second, flows across sectors are small. Ben-David et al. (2012) decompose the market
into hedge funds, mutual funds, short sellers, other institutional investors (e.g., pension funds and
insurance companies), and non-institutional investors (e.g., households). Measured as a fraction of
the market, these investor sectors sell or buy on average just 0.25% of the market per quarter. We
extend these calculations using data from the FoF for the technology crash in 2000-2002 and the
2008 global financial crisis in Appendix D.3. As a fraction of the market, flows between groups
average to at most 0.5% of the market.
In summary, many funds appear to have fairly tight mandates, hedge funds do not appear to
arbitrage the aggregate stock market and amplify demand shocks during severe downturns, and
flows between sectors are small.
The small flows across sectors has implications for the properties of demand shocks, which
are shocks to investors’ beliefs or risk appetite, given the elasticity of demand. The signature of
elastic demand is that disagreement among investors is associated with large flows and quantity
movements. As flows are small, theories featuring elastic demand imply that investors should agree
almostperfectlyintheirbeliefsaboutexpectedgrowthratesandtheirriskiness,andalsohavesimilar
risk aversion. In inelastic markets, in contrast, there can still be large common shocks to beliefs, for
9Their sample appears to be representative of the middle 80% of the retirement wealth distribution of retirement
investors between age 25 and 65.
10While a large literature explores the micro elasticity of hedge funds, we are interested in their market elasticity.
In the FoF, hedge funds are part of the household sector and we cannot study them separately using these data.
9

instance as during the 2008 financial crisis, but there is much more scope for disagreement.11 This
second interpretation of financial markets may be more consistent with the data on beliefs, which
points to significant fluctuations in disagreement over time (Giglio et al. (2021a)).
2.4 The micro and macro elasticity of markets: Summary of existing
evidence
This paper is about the macro-elasticity of the market (that is, how the aggregate stock market’s
valuation increases if one buys $1 worth of stock by selling $1 worth of bonds). This is in contrast
with the very large literature that studies the micro-elasticity of the market (which describes how
much the relative price of two stocks changes if one buys $1 of one, and sells $1 of the other).
In Panel A of Table 1, we provide a summary of recent estimates of the micro multiplier, which is
the percent change in prices when an investors purchases a certain fraction of the shares outstanding
in a particular company, while controlling for movements in the aggregate market.12 While there is
a range of estimates, the order of magnitude of the multiplier is around 1. That is, buying 1% of
the shares outstanding of a given stock results makes its price increase by around 1%.
In addition, several recent studies have looked at the “factor-level” multiplier, which is the price
impact if an investor buys a fraction of the shares outstanding of a cross-sectional factor such as size
or value. We report those estimates in Panel B. The studies report a multiplier that is substantially
above 1 and closer to 5. In Panel C, we report recent estimates of the “macro multiplier,” the
parameter of interest in this paper, for the Chilean and Chinese stock markets. Once again, the
multiplier estimates are well above 1. Equivalently, the macro elasticity, which is the inverse of the
multiplier, is well below 1.
Taken together, the existing evidence in the literature suggests a micro multiplier around 1 (so,
a micro elasticity around 1), and a factor or macro multiplier that is well above 1 (so, a macro
elasticity below 1).
11Tomakethismoreconcrete,usingthenotationofthenextsection,considerthesimpledecompositionofdemand
∆q = ζ∆p +fν. If markets are as elastic as in standard models, say ζ = 10, then fν = ∆q +10∆p . As the
it − t it it it t
volatility of ∆q is modest, demand shocks are largely dominated by the second term, 10∆p , and almost perfectly
it t
correlated. This leaves little room for disagreement among investors, even though this is widely document in beliefs
data, as the signature prediction of a model with elastic markets and belief disagreement is the presence of large
flows coupled with small price changes. When markets are inelastic, say ζ =0.2, then fν =∆q +0.2∆p . Demand
it it t
shocks still contain a large common component, but the correlation between demand shocks is much lower and there
is more scope for disagreement.
12Also, the empirical market microstructure estimates of price impact are larger than what we find: the price
impactthatthemicrostructureliteraturefindsisafactorofabout15(Bouchaudetal.(2018);Frazzinietal.(2018)),
which may make our estimate of 5 seem moderate. Microstructure results are typically couched in a form such as
“buying 2.5% of the daily volume of a stock creates a permanent price increase of 0.15%”. At first glance, values in
this range might appear to imply a small price impact. However, they work out to a large price impact multiplier of
M =15: with250daysoftradinginayear,anda100%peryearturnover, thetradeinourexamplewouldrepresent
apurchaseof 2.5% =0.01%ofthemarketcapitalizationofastock,sothattheimpactof0.15%onthepriceresultsin
250
amultiplierof15. Theinterpretationofthiskindofmicrostructureestimatesrequiressomecaution,aswediscussin
Section G.5. To sum up, a microstructure estimate of 15 may have the following interpretation: in inelastic markets
with a micro elasticity equal to 1, a large market-wide desired trade (“metaorder”) is on average split into 15 smaller
trades executed over time, by one or several institutions collectively (for example, by three funds pursuing a similar
strategy, each splitting their desired position change into five smaller trades). These microstructure estimates are
also themselves to be taken with caution, since identification tends to be difficult as trades are not exogenous to
prices. Using high frequency data with a GIV-based identification may be a promising way to enrich identification
procedures in microstructure.
10

Table 1: Multiplier estimates in the existing literature. The table reports multiplier estimates in
the existing literature for individual stocks (Panel A), factors such as size and value (Panel B), and
the aggregate stock market (Panel C). The multiplier is defined as the percent change in prices per
percent change in shares outstanding purchased or sold by an investor. We discuss footnote 12 and
Appendix G.5 how to interpret the trade-level estimates of Frazzini et al. (2018) and Bouchaud et
al. (2018); here, we simply report the “prima facie” estimates.
Panel A: Micro multiplier
Methodology Multiplier
Chang, Hong and Liskovich (2014) Index inclusion 0.7 to 2.5
Pavlova and Sikorskaya (2020) Index inclusion 1.5
Schmickler (2020) Dividend payouts 0.8
Frazzini et al. (2018), Bouchaud et al. (2018) Trade-level permanent price impact 15
Panel B: Factor-level multiplier
Ben-David, Li, Rossi and Song (2020a) Morningstar ratings change 5.3
Peng and Wang (2021) Fund flows 4.8
Li (2021) Fund flows+SVAR 5.7
Panel C: Macro multiplier
Da, Larrain, Sialm and Tessada (2018) Pension fund rebalancing Chile 2.2
Li, Pearson and Zhang (2020b) IPO restrictions in China 2.6-6.5
How do these estimates compare to the elasticities implied by standard asset pricing models? It
is well known (e.g. Petajisto (2009)) that the micro elasticity in standard models is very large, of the
order of 1000 or above. This implies that the micro multiplier (the inverse of the micro elasticity)
is essentially zero and “demand curves are virtually flat.” Based on the estimates reported in Table
1, the models are several orders of magnitudes off in terms of the micro elasticity.
Our focus is on the macro elasticity and we compute it for various asset pricing models in Section
F.4.13 The summary is that in traditional, elastic asset pricing models the macro elasticity is around
10 to 20, leading to a multiplier around 0.1 to 0.05. As any two stocks are closer substitutes than
stocks and bonds, the micro multiplier is much lower than the macro multiplier in standard asset
pricing models. However, the micro multiplier as estimated in the literature (see Panel A) is already
an order of magnitude larger than the macro multiplier implied by standard asset pricing models.
The macro multiplier estimates are even larger, which deepens the disconnect between existing
estimates and asset pricing models. A multiplier of 0.05 implies that if a sovereign wealth fund, for
instance, were to buy 10% of the US aggregate stock market, prices would rise by just 50bp.
The profession’s view on the macro elasticity and the underlying mechanism While
the disconnect between the empirical estimates and asset pricing models follows from the existing
literature, these facts have typically not been targeted in macro-finance asset pricing models. In
fact, as we will discuss now, this evidence does not appear to be widely known or accepted in the
profession.
13We discuss the elasticity in the models of Lucas (1978), Bansal and Yaron (2004), Barro (2006), Gabaix (2012),
and the link between our findings and Johnson (2006).
11

We quantify this via two surveys. We provide a detailed discussion in Section E and summarize
the main insights here. We conducted a first survey by putting out a request via Twitter (using
the #econtwitter tag) to complete an online survey. In addition, we asked participants of an
online seminar at VirtualFinance.org to complete the same survey – this latter audience being
naturally more representative of the population of academic researchers in finance. Both surveys
were conducted before the paper was available online and before the seminar was conducted. We
received 192 responses for the Twitter survey and 102 responses for the survey connected to the
finance seminar.
The survey question was the following: “If a fund buys $1 billion worth of US equities (perma-
nently; it sells bonds to finance that position), slowly over a quarter, how much does the aggregate
market value of equities change?” The answer given in this paper is M times a billion, where M is
the macro multiplier, which we estimate to be around M = 5. In both surveys, the median answer
was M = 0: surveyed economists, logically enough, rely on the traditional asset pricing model in
which prices are unperturbed by flows. The median positive answer was M = 0.01.14 Hence, sur-
veyed economists’ views are in line with the traditional model, but far from the estimates reported
in the empirical literature, and the new estimates we provide.
We also asked about the sector supposedly providing elasticity to the market to be able to
explore the mechanism. The two most common responses were hedge funds and broker dealers.
As discussed before, those sectors are unlikely to provide elasticity to the aggregate market, in
particular during times of stress.
3 The Inelastic Markets Hypothesis: Theory
We now provide a model that we think is more realistic to think concretely about the determinants
of stock demand, and about how flows impact prices. It is highly stylized, but will be useful to
think about the determinants of elasticity (both conceptually and in terms of calibration) and to
guide empirical work. We start with a two-period version, and then proceed to an infinite-horizon
variant.
3.1 Two-period model
There is a representative stock in fixed supply of Q shares, with an endogenous price P. The
economy lasts for two periods t = 0,1. The dividend D is paid at time 1. We call π = De 1 r
the equity premium (with De := E[D] the expected dividend at time 0 and r the risk-fr P ee−rate−), π¯ f
f
the average equity premium, and πˆ := π π¯ the deviation of the equity premium from its average.
There is also a riskless bond with time-0 p−rice equal to 1 (we endogenize the risk-free rate in Section
5).15
A representative consumer invests into stocks and bonds via I institutions or funds.16 We call
W fund i’s wealth (or equivalently assets under management) and Q the number of stock market
i i
14The answer M 1 was given by only 2.5% of respondents in the Twitter survey and by 4% of respondents in
≥
the VirtualFinance.org survey. Section E provides further details.
15Here, flowsmoveequitypricesbutnotbondprices. InthegeneralequilibriumversionofSection5, thishappens
because the consumer’s demand is infinitely elastic with respect to bond prices. We sketch the case where both
equity and bond demands are inelastic in Section G.1: the economics is similar, replacing the elasticity by a matrix
of own- and cross-elasticities.
16Those funds act competitively, i.e. are price takers.
12

shares it holds. Therefore the fraction of fund i’s wealth invested in equities is PQi . We assume that
fund i’s demand for stocks is given by a mandate, saying that it should have a W firaction invested in
equities equal to:17
PQ
i = θ eκiπˆ, (1)
i
W
i
while the rest is in the riskless bond. In the simplest case, κ = 0, fund i has a fixed mandate to
i
invest a fraction θ 0 of its wealth in equities. When κ > 0 the fund allocates more in equities
i i
when they have high≥er expected excess returns (hence, κ indexes how contrarian or forward-looking
i
the fund is). This demand function appears sensible, and could be micro-founded along many lines
– but to go straight to the effects we are interested in, we take it as an exogenous mandate.18(cid:48)19(cid:48)20
We use the index i = 0 for a special fund, a “pure bond fund” that only holds bonds (so, its θ and
i
κ are 0).
i
If consumers were fully rational, the mandate would not matter: consumers would undo all
mechanical impacts of the mandate. But consumers will not be fully rational, so mandates will
have an impact.
The elasticity of demand for stocks of a fund We use bars to denote values at time t = 0−,
before any shocks. At that time 0−, fund i has wealth W ¯ , and holds Q ¯ shares. We assume that
i i
before the shocks, equities have an equity premium π¯, so that the dividend-price ratio is at its
corresponding value, δ = D¯e, where P ¯, D ¯e are the baseline values for the stock’s price and the
P¯
expected dividend.
At time 0, the representative household invests ∆F extra dollars in each fund i (taking those
i
dollars from the pure bond fund), which represents a fractional inflow f = ∆Fi . An outflow
corresponds to ∆F < 0. We study the impact of this on the aggregate ma i rket, W i ¯ nidependently of
i
the reasons for the flows, which may be rational or behavioral. We also assume that there may be a
change d in the value of expected fundamentals. We call q and d the fractional deviations of equity
i
demand and of the expected dividend from their baseline values:
Q De
q = i 1, d = 1. (2)
i
Q
¯
− D
¯e
−
i
The next proposition gives the change in demand by fund i. Its proof is in Appendix A. We
perform the analysis for small disturbances f ,d, and hence small p,q , here and throughout the
i i
paper.21
17We write the mandate in “number of shares,” but it is equivalent to a “fraction of assets invested in equity”
formulation.
18This fund’s mandate can be viewed as a stand-in for other frictions such as inertia or a rule of thumb that a
behavioral household might follow for its stock allocation. As a result, the institutionalization of the market does
not necessarily result in more inelasticity as it depends on how households manage their own portfolios. Parker et
al. (2020) argue that the growth of target date funds made the market more elastic. In the our notation, target date
funds have κ =0.
i
19Buffa et al. (2019) explore the implications of tracking error constraints on asset prices.
20Themandatedoesnotfeaturevolatility,asvolatilityisnotcrucialheretoobtaindemandcurves(thoughvolatility
is crucial for that in the traditional model). One could easily write extensions where the allocation decreases in
volatility. In the dynamic model, we add a demand shock that can include volatility terms.
21Following common practice in macro-finance, we do Taylor expansions of the leading terms, omitting the formal
mentions of O() terms.
·
13

Proposition 1. (Demand for aggregate equities in the two-period model) Fund i’s demand change
(compared to the baseline) is, linearizing:
q = ζ p+κ δd+f , (3)
i i i i
−
where δ is the baseline dividend-price ratio, and ζ is the elasticity of equity demand by fund i,
i
ζ = 1 θ +κ δ. (4)
i i i
−
The aggregate elasticity of demand for stocks, and the “representative mixed fund” We
now move from fund-level demand to the aggregate demand for stocks, which is Q = Q ¯ (1+q ).
i i i
We call WE the equity holdings (in dollars) of fund i, and S its share of total equity holdings:
i i
(cid:80)
W ¯ E Q ¯
WE = Q P = θ W , S = i = i . (5)
i i i i i W ¯ E Q ¯
j j j j
Finally, for a given variable x (with i = 1...I), we d(cid:80)efine x to(cid:80)be its equity-holdings weighted
i S
mean:
x := S x . (6)
S i i
i
(cid:88)
So, the aggregate demand change is:
¯
∆Q Q q
q = = i i i = S q = q .
i i S
Q Q
(cid:80) i
(cid:88)
To derive an expression for it, we take the individual demand curves (3), and consider their equity-
holdings weighted average, which gives the (linearized) aggregate demand curve for equities:
q = ζ p+κ δd+f .
S S S S
−
Proposition 2 sums this up.
Proposition 2. (Aggregate demand for aggregate equities in the two-period model) The aggregate
demand for equities is
q = ζp+κδd+f, (7)
−
where ζ = ζ = S ζ is the equity-holdings weighted demand elasticity of all funds i, and likewise
S i i i
for the other quantities:
(cid:80)
θ = θ , κ = κ , ζ = ζ , f = f . (8)
S S S S
In particular, ζ is the macro elasticity of demand:
ζ = 1 θ+κδ. (9)
−
Hence, the universe of equity-holding funds in the model aggregates (up to second order terms in f
i
and d) to a “representative mixed fund” with wealth W = I W , and whose mandate is to hold
i=1 i
an equity share PQ = θeκπˆ.
W (cid:80)
14

The “aggregate flow into equities” is non-zero even though “for every buyer there is a
seller” The equity-share weighted flow f = S f in (8) can also be expressed as22
S i i i
(cid:80) θ ∆F
f = i i i , (10)
S W ¯ E
(cid:80)
i.e. as the sum of the dollar inflows ∆F into each fund i, times the marginal propensity of fund i
i
to invest in equities, θ , as a fraction of the the baseline value of aggregate equities WE = QP ¯.23
i
At the same time the net total flow is 0, ∆F = 0, as one bond removed from one fund goes to
i i
another fund, and the net amount of equities purchased is 0, ∆Q = 0, as the net amount of
shares is constant:24 (cid:80) i i
∆F = 0, ∆Q = 0 (cid:80) . (11)
i i
i i
(cid:88) (cid:88)
Hence, there is a well-defined notion of “the aggregate flow into equities,” f (equation (10)) which
S
is generically non-zero, even though “for every buyer there is a seller” (equation (11)).
The impact of flows on the aggregate price Wenowanalyzewhathappensaftertheaggregate
inflow f in equities. We assume from now on that ζ > 0. As the supply of shares does not change,
S
we must have q = 0 in the equilibrium after the flow shock. Given (7), we have 0 = q = ζp+f,
and the price change must be p = f. Proposition 3 summarizes this.25 −
ζ
Proposition 3. Suppose that the representative consumer invests ∆F in each fund i, so that the
i
total inflow in equities is a fraction f = f = S ∆Fi of the value of equities. Then, the stock
S i i W¯
i
price changes by a fraction p := P−P¯ equal to:
P¯ (cid:80)
f
p = , (12)
ζ
where ζ is the macro elasticity of demand defined in (9).
This illustrates that flows can have large price impacts if the price elasticity of demand ζ is
sufficiently low, and shows the key role of this price elasticity, which is the center of this paper.26
An undergraduate example To think through the economics of Proposition 3, we found the
following simple, undergraduate-level example useful. Suppose that there are just two funds: the
pure bond fund and the representative mixed fund, which always holds 80% in equities (the mag-
nitude suggested by Figure 1). Then, θ = 0.8, κ = 0, so that ζ = 1 θ = 0.2 and 1 = 5. Then an
− ζ
extra 1% inflow into the stock market increases the total market valuation by 5%.
It is instructive to think through the logic of this example. Suppose that the representative
mixed fund starts with $80 in stocks (of which there are 80 shares, worth $1 each) and $20 in
22Indeed, as θ = W¯ i E ,we have f = S f = W¯ i E ∆Fi = 1 θ ∆FE.
i W¯
i
S i i i i WE W¯
i
WE i i i
23This is analogous to the marginal propensity to take risk in Kekre and Lenel (2020).
(cid:80) (cid:80) (cid:80)
24For instance, if there are just the pure bond fund and a mixed fund, then the bond flow into the mixed fund
∆F is compensated by a flow out of the pure bond fund, so ∆F = ∆F .
1 0 1
−
25It is exact when all κ =0 and it uses a first-order Taylor expansion for small flows f when κ =0.
i i
(cid:54)
26If d = 0, there is an extra effect, and p = f + κδd, with κδ < 1. This implies that unaided by flows, prices
(cid:54) ζ ζ ζ
under-react to fundamentals in inelastic markets.
15

bonds. There are also $B worth of bonds outstanding. Suppose now that an outside investor sells
$1 of bonds from the pure bond fund (he had $B $20 in the pure bond fund, and now he has
$B $21), and invests this $1 into the mixed fund. I−n terms of “direct impact”, there is a $0.8 extra
dem−and for the stock (equal to 1% of the stock market valuation), and $0.2 for the bonds. But that
is before market equilibrium forces kick in.
What is the final outcome? In equilibrium, the pure bond fund still holds $B $21 worth of
bonds. The balanced fund’s holdings are $21 in bonds (indeed, it holds the remainin−g $21 of bonds)
and 4 $21 = $84 in stocks (as the balanced fund keeps a 4:1 ratio of stocks to bonds, the value
of the×stocks it holds must be $84). As the balanced fund holds all 80 shares, the stock price is
P = $84 = $1.05, whereas it started at P = $1: stock prices have increased by 5%. The fund’s
80
value also has increased by 5%, to $105.
We see that the increase in stock prices is indeed by a factor 1 = 1 = 5. Only $0.8 was
ζ 1−θ
invested in equities, yet the value of the equity market increased by $4, again a five-fold multiplier.
We conclude with a few remarks.
Share repurchases and issuances are just a type of flow Suppose that corporations buy
back shares, meaning that they buy:
Net repurchases (in value) Net issuances (in value)
f = = . (13)
C Total equity value Total equity value
−
Then, the basic net demand for shares is as above, using the total flow:
f := f +f , (14)
S C
which is equal to the size-weighted total flow in the funds, f , plus share repurchases (as a fraction
S
of the market value of equities). In short, on top of the traditional flows of investors into equities,
we want to add share repurchases by corporations. In addition, if firms have a supply elasticity ζ ,
C
then the basic equilibrium is: f ζp = f +ζ p. That is, a change in demand f ζp equals a
S C C S
change in supply f +ζ p. The−refore p − = fS+fC , so that the effective market elastic−ity is ζ +ζ .
In much of the pa−per C , we C assume that the sup ζ+ p ζ lCy of shares is inelastic, ζ = 0, which will prove t C o
C
be a good approximation.
The representative mixed fund’s equity share vs. the market-wide equity share There
are two notions of equity share. The traditional one is the wealth-weighted equity share:
WE Total value of Equities
θ = = , (15)
W WE +WB Total value of Equities+Bonds
which can also be expressed as θ = (cid:80) i Wiθi. The other one is the equity-holdings weighted equity
W (cid:80)
i
Wi
share defined earlier, θ = (cid:80) i W i Eθi, where WE was the equity holding of fund i. The former
S (cid:80) WE i
share (θ ) is directly availableiiniaggregated data, while the latter (θ ) is what matters for the
W S
macro elasticity. They are different, and indeed θ > θ .27 This makes the disaggregation issues
S W
potentially non-trivial, and will require some care in the empirical part.
27Indeed, using W
i
E = θ
i
W
i
, θ
S
= E
S
[θ
i
] =
i
S
i
θ
i
= (cid:80) (cid:80)i
i
W
W
i E
i E
θi = (cid:80) (cid:80)i
i
W
W
i
i
θ
θ
i 2
i
= E
E
W
W
[
[
θ
θ
i 2
i]
]
≥
E
W
[θ
i
] = θ
W
. As long as
there is a pure bond fund, the θ are not identical, and the inequality is strict. Formally, we assume that all funds
i (cid:80)
have weakly positive total wealth.
16

Take the undergraduate example with just two funds, the mixed fund and the pure bond fund,
and κ = 0. Then, whatever the flows, θ = θ is always constant, pinned by the mandate θ of that
S
mixed fund. However, θ varies over time, as flows in and out of equities change the market value
W
of equities, P.
3.2 Infinite horizon model
We extend the static model to a dynamic one. The forces will generalize in an empirically imple-
mentable way. There is again a constant risk-free rate r , taken here to be exogenous. Section 5
f
endogenizes it in general equilibrium, but here we concentrate on the core economics of inelasticity.
The representative stock gives a dividend D .
t
We consider the case where there is a pure bond fund and “representative mixed fund” trading
stocks and bonds. This allows us to zoom in on the core economics: an economy with several
funds can be represented via a single mixed fund to the leading order, as in Proposition 2.28 The
representative mixed fund has a mandate: the fraction invested in equities, PtQt, should be
Wt
P Q
t t = θeκπˆt+νt, (16)
W
t
where as before πˆ := π π¯ is the deviation of the equity premium from its average, and we allow
t t
for additional demand sh−ocks, ν . These can be thought of as shocks to tastes or perceptions of risk.
t
We assume that dividends and interest rates on bonds are passed to consumers: hence, reinvesting
dividends counts as an inflow.
To analyze this economy, it is useful to linearize it. This needs to be done around a simpler,
“baseline” economy, which is on a balanced growth path with a constant equity premium π¯. We call
P ¯, D ¯ , W ¯ , and Q ¯ the baseline price, dividend, wealth, and quantity of shares held by the mixed
t t t
fund. We assume that P ¯ ,D ¯ ,W ¯ = P ¯ ,D ¯ ,W ¯ : they grow with a common cumulative growth
t t t 0 0 0 t
G
factor , such that Gt+1 follows an i.i.d. growth process with mean g. As the equity premium is
G t G(cid:0)t (cid:1) (cid:0) (cid:1)
always π¯ in the baseline economy, r +π¯ g = (1+g)δ, with P¯ tQ¯ = θ and D¯ t = δ.29 At the same
time, the bond holdings of the mix
f
ed fun − d are B ¯ + F ¯, where
W¯
F ¯t is the cum
P¯
t ulative dollar inflow
0 t t
since time 0 (so F ¯ = 0): the only “new” bonds that the representative mixed fund has must come
0
from inflows, like in the undergraduate model above. They should also represent a fraction 1 θ of
the wealth of the fund, so that we have: B ¯ +F ¯ = 1−θP ¯ Q. This means that F ¯ = 1−θ P ¯ P −¯ Q ¯.
This is the flow consistent with a balanced 0 grow t th p θ ath t in the rational econom t y. θ t − 0
(cid:0) (cid:1)
Wecallp , w , d , q thedeviationsfromthebaseline, sothatd = Dt 1, p = Pt 1, w = Wt 1,
t t t t t D¯
t−
t P¯
t−
t W¯
t−
and q = Qt 1. We define the flow f as the scaled cumulative inflow in excess of the baseline:30
t Q¯
−
t
¯
F F
f = t − t . (17)
t ¯
W
t
Wecalltheexpecteddividenddeviationde = E d . Theexpectedexcessreturnisπ = E t[∆Pt+1+Dt+1]
r , and we use the following Taylor expa t nsion t (s t e + e 1 Section F for a derivation): t Pt −
f
πˆ = δ(de p )+E [∆p ]. (18)
t t − t t t+1
28This is detailed in Appendix G.7.
29Indeed, 1+r +π¯ =E P¯ t+1+D¯ t+1 =E P¯ t+1(1+δ) =(1+g)(1+δ).
f t P¯
t
t P¯
t
30This is extremely close t(cid:104)o another d(cid:105)efinitio(cid:104)n, f = (cid:105)t ∆Fs−∆F¯ s, but the above definition is the one warranted
t s=0 Ws−1
by the theory.
(cid:80)
17

The aggregate demand for stocks is as follows, generalizing (7).
Proposition 4. (Demand for aggregate equities in the infinite-horizon model) The demand change
for equities (compared to the baseline) is
q = ζp +f +ν +κδde +κE [∆p ], (19)
t − t t t t t t+1
where ζ = 1 θ+κδ is the aggregate elasticity of the demand for stocks, as in (9).
−
As the total number of shares is constant, the equilibrium condition is given by q = 0. This
t
yields the stock price as follows (the proof is in Appendix A).
Proposition 5. (Equilibrium price in the infinite-horizon model) The equilibrium price of aggregate
equities is (expressed as a deviation from the baseline):
∞
1 f +ν
p = E ρ τ τ +δde , (20)
t t (1+ρ)τ−t+1 ζ τ
τ=t (cid:18) (cid:19)
(cid:88)
where ρ = ζ is the “macro market effective discount rate”,
κ
ζ 1 θ
ρ = = δ + − . (21)
κ κ
The deviation of the equity premium from its average is:
(1 θ)p (f +ν )
πˆ = − t − t t . (22)
t
κ
We next analyze the economics of Proposition 5. The classical (or undergraduate) “efficient
markets” benchmark, where the risk premium is kept constant by very strong arbitrage forces,
corresponds to κ = , so that ζ = and ρ = δ.31
In (20), the pric∞e discounts futu∞re dividends at a rate ρ δ given in (21). So, the market is
≥
more myopic (higher ρ) when it is less sensitive to the equity premium (lower κ) and when the mixed
fund has a lower equity share (lower θ).32 It makes good sense that a lower sensitivity to the equity
premium makes the market less reactive to the future, hence more myopic.33,34 In the rest of this
section, we set ν = 0; the general case simply comes from replacing f by f +ν .
t t t t
31Strictlyspeaking,thisisonlytruewithrisk-neutralarbitrageurs,sothattheriskpremiumis0. Thegeneralcase
is in Section F.4 where the elasticity is still very high.
32The formula extends to changes in the interest rate, as in r = r¯ +rˆ . As (18) becomes πˆ = E ∆p +
ft f ft t t t+1
δ(de p ) rˆ , all expressions are the same, replacing de by de 1rˆ , including in (20). We assume here that the
t − t − ft t t − δ ft
bond is very short term, with zero duration. If the bond has non-zero duration, there is another term corresponding
to the capital gains on bonds.
33The intuition for the sign of the impact of θ on ρ is as follows: the extra term 1−θ in ρ = δ+ 1−θ is the ratio
κ κ
of the “present looking” (myopic) demand elasticity 1 θ to the “forward looking” elasticity κ. Hence a higher θ
−
leads to a less myopic demand. This myopia in (20) generates momentum: because the market is myopic (by (20)),
dividend news are only slowly incorporated into the price.
34Here the demand (19) depends on the equity premium as κπˆ = κE ∆p +κδ(de p ). A variant would be
t t t+1 t − t
that investors “see” the price-dividend ratio as differently predictive from the expected price movement, so that in
their demand we equalize κπˆ with κE ∆p +κDδ(de p ) where potentially κD =κ (e.g., if “tangible” predictors
t t t+1 t − t (cid:54)
are deemed more reliable, κ < κD). Then the demand elasticity is ζ = 1 θ+κDδ, the effective discount factor is
−
ρ = ζ, and (20) still holds, after multiplying δde by κD. This highlights that κD increases the market elasticity ζ,
κ τ κ
while κ increases market “forward-lookingness” 1.
ρ
18

A permanent inflow has a permanent effect on the price and future expected returns
of equities Suppose that at time 0 there is an inflow f that does not mean-revert. Then, the
0
impact on the price at time t 0 is (via (20), with E [f ] = f ):
0 τ 0
≥
1
E [p ] = f . (23)
0 t ζ 0
So, the “price impact” is permanent. As a result, the equity premium is permanently lower, E [πˆ ] =
0 t
δf0 (see (18)) This is simply because, if the equity demand has permanently increased, equity
− ζ
prices should be permanently higher.35
Quantitatively, ifpricesincreaseby10%duetouninformedflows, theperannumexpectedexcess
returnfallsbyamere0.3%(indeed,assumingadividendyieldof3%,πˆ = δp = 3% 0.1 = 0.3%).
This is a vivid reminder that the absence of detectable market timing str−ategies−tells×us little about
market efficiency (Shiller (1984)). Similarly, Black (1986) famously argued that the aggregate stock
market can be mispriced by as much as a factor of two; in our model, if this is due to a permanent
inflow, that would lead to a 2% change in the expected excess return,36 which is less than a single
standard error deviation of the expected excess return estimate if one were to use 30 years of data.
The impact of a mean-reverting flow Suppose now that at time 0 there is an inflow f that
0
mean-reverts at a rate φ [0,1], so that the cumulative flow is E [f ] = (1 φ )τ f . Then, if
f 0 τ f 0
there are no further disturb∈ances, the impact on the time-t price is p = ft (−see (20)), implying
t ζ+κφ
f
(1 φ )t
E [p ] = − f f , (24)
0 t ζ +κφ 0
f
and the change in the equity premium is E [πˆ ] = δ+φ f (1 φ )tf (see (22)). Hence, an inflow
0 t −ζ+κφ f − f 0
that has faster mean reversion leads to a smaller change in the price of equities (compared to
a permanent inflow), but a larger change in their equity premium on impact (indeed, δ+φ f is
ζ+κφ
f
increasing in φ ). Those effects dissipate as the inflow mean-reverts, at a rate φ .
f f
Predictable future inflows or changes in fundamentals create predictable price drifts
Suppose that it is announced at time 0 that a permanent inflow f will happen at time T > 0. The
T
price impact for t [0,T] is p = 1 fT (see (20), using f = 1 f ), so that after the initial
∈ t (1+ρ)T−t ζ τ τ≥T T
jump, the price gradually drifts upward (assuming for concreteness that the inflow is positive).
Hence, the risk premium is elevated by πˆ = 1−θp (for t [0,T), see (22)), and more elevated as
one nears the inflow. After the inflow, th t ough, κ we t are bac∈k to the case of a permanently elevated
price and permanently lower equity premium (p = fT and πˆ = δfT for t T). The same price
drift before the shock happens for a predictable t incre ζ ase in fu t ture−fun ζ dament≥als such as dividends.
A simple benchmark To think about the stochastic steady state, it is useful to consider f as
t
an autoregressive process with speed of mean-reversion φ :
f
f = (1 φ )f +εf, (25)
t f t−1 t
−
35In a Kyle (1985) model, flows change prices, like in our model; but they do not on change the equity premium
(on average), which is a crucial difference with our model. Section G.5 details the link with the Kyle model.
36Indeed, with p=ln2, πˆ = δp= (3%) 0.7 2%.
− − × (cid:39)−
19

withE εf = 0. Then,ahighinflowincreasesequitypricesandhencelowerstheequitypremium,
t−1 t
in the follo
(cid:104)
wi
(cid:105)
ng precise manner:37
1
p = bpf , πˆ = bπf , bp = , bπ = (δ +φ )bp. (26)
t f t t f t f ζ +κφ f − f f
f
Calibration We want to understand how a macro price impact of M 5 might arise, and for
this we calibrate the model. When flows are mean-reverting with speed(cid:39) φ , the price impact is
f
M = 1 , with ζM = ζ + κφ = 1 θ + κ(δ +φ ) (see (9), (24), and (26)). Some parameters
ζM f − f
are easy to estimate. We take a dividend-price ratio δ = D = 3.7%/year (we use annualized units
P
throughout).38 We calibrate φ = 4%/year to match the speed of mean-reversion of the dividend-
f
price ratio.39 Given the results in Figure 1, we take an equity share θ = 87.5% (equity-holdings
weighted as in θ ).
S
Calibrating κ is most challenging. We perform a few thought experiments to see what we
might expect κ to be. The simplest rational model of portfolio choice where θ = πt gives
it γiσ2
κ = dlnθit = 1 = 22, using an annual equity premium of 4.4%.40 But, we rarely observe such large
swings dπ itn inv π¯ estors’ portfolios: the frictionless rational model predicts agents that are much too
reactive, like in much of this paper, and in much of economics (Gabaix (2019)). To get a further
feel for κ, suppose the equity premium increases from π = 5% to π = 10%, which is a shift
t t
equal to about one to two standard deviations of its unconditional time-series variation (Cochrane
(2011); Martin (2017)). A very flexible fund with an average equity share of 50% might change
its equity allocation from 50% to 75%. This flexible fund would have κ = dlnθi = ln0.75−ln.5 8.
However, these are large swings in a fund’s strategic asset allocation that i are n d o π t typical 0 ly .05 obse(cid:39)rved
empirically, so that they are at most valid only for very flexible investors. As many balanced funds
haveafixed-sharemandateandκ = 0,wehypothesizeaκ foratypicalfundwithequityshareof50%
i
equal to about 4. Moreover, a 100% equity funds needs to have κ = 0; more generally, the rigidity
i
mechanicallyshouldincreasewiththeequityshareθ . So, wemighttentativelyparametrizeatypical
i
value of κ as κ = K(1 θ ), with K 8. So, we obtain κ = κ = K(1 θ ) 8 (1 0.88) 1.
i i S S
This gives a simple micr−oeconomic int(cid:39)erpretation for the value κ = 1. Tog−ether(cid:39), thi×s yiel−ds ζ = 0 (cid:39) .16,
and ζM = 0.2, so that the price impact is indeed M = 1 = 5. If the flows are extremely persistent,
ζM
the subtle difference between ζ and ζM vanishes (κφ ,which is 0.04 in the calibration, goes to 0).
f
4 Estimating the Aggregate Market Elasticity
The previous sections illustrate the importance of estimating the elasticity of the aggregate stock
market. Estimating this parameter is a challenge, as is the case for most elasticities in macroeco-
37This can be derived by plugging in those values in (19) with q =0 in equilibrium, or via (20).
38Section H.1 details how to go from continuous to discrete time.
39We compute the dividend yield by summing dividends during the last 12 months relative to the current level
of the CRSP value-weighted return index from January 1947 to December 2018. The annual autocorrelation of the
log dividend yield during this sample is equal to ρOLS = 0.91 with OLS standard errors equal to 0.048. We then
remove the Kendall (1954) bias 1+3ρ over our sample of T = 72 years, which is around 4 . Thus we calibrate
T 72
φ =1 ρOLS 4 4%.
f − − 72 (cid:39)
40ThisisforafundmaximizingrationallyaCRRAfunctionoffinancialwealth. InSectionF.4weconsideramore
sophisticated thought experiment, with a consumer maximizing lifetime utility out of labor income in additional to
financial wealth. Then, the value of ζ is even higher.
20

nomics. In the context of asset pricing, large literatures try to estimate the coefficient of relative
risk aversion, the elasticity of inter-temporal substitution, and the micro-elasticity of demand, but
not the macro elasticity.41
The key difficulty is that prices and flows are in part driven by other variables, such as macroeco-
nomic news, so that naively regressing prices on flows or flows on prices would not yield a consistent
estimate of the elasticities. Hence, we need an instrument. In this section, we provide first estimates
of the macro elasticity of the US stock market using the method called Granular Instrumental Vari-
ables (GIV), which we conceived for the present paper, and lay out in Gabaix and Koijen (2020).
Given the relevance of this parameter, we believe it would be valuable for future empirical asset
pricing research to explore different estimation and identification strategies in estimating its value.
In Section 4.1, we provide the basic intuition behind the GIV estimator. We report the estimates
in Section 4.2 using sector-level data from the Flow of Funds and in Section 4.3 using investor-level
data by combining 13F filings and mutual fund flows. We also connect capital flows to macroeco-
nomic variables and measures of beliefs to provide an initial analysis of the potential determinants
of flows into the equity market.
4.1 Intuition behind the GIV estimator
We first provide a brief summary of the GIV method – the appendix and Gabaix and Koijen (2020)
provide many more details, such as a justification of consistency and extensions. Recall that we use
the following notations, with the shares S adding up to 1:
j
N N
1
X := X , X := S X , X := X X . (27)
E N i S i i Γ S − E
i=1 i=1
(cid:88) (cid:88)
Suppose that we have a time series of changes in investors’ equity holdings, ∆q = Qit−Qi,t−1,
it Qi,t−1
where i indexes investors as before. The estimation procedure does not require data on flows across
asset classes: equity holdings suffice, which is empirically relevant as investor-level data on flows
are available only for a subset of investors.42 To fix ideas, we model ∆q as (omitting constants):43
it
∆q = ζ∆p +fν, (28)
it − t it
where ∆p is the aggregate stock return, and ζ is the demand elasticity of interest — we take it
t
as constant across sectors in this introduction, but will relax this in Section 4.3. We consider the
following model for fν:
it
fν = λ(cid:48)η +u , (29)
it i t it
41See Table 1 for a summary of estimates in the literature.
42If we were tohave high-quality dataon capital flows, f , then we could construct anothergranular instrumental
it
variable using capital flows by extracting idiosyncratic shocks to f . However, our theory implies that we need
it
accurate data on equity and bond holdings to measure capital flows correctly, which are unavailable in the US.
Fortunately,however,wecanimplementtheGIVprocedureusing∆q ,whichdoesnotrequireknowledgeofholdings
it
in other assets than equities. Also, in Section 4.3 we show how to use data on a subset of investors, in our case
mutual funds, to obtain another estimate.
43To lighten things up, we simplify a bit the notations. Compared to (19), we use the notation fν for ∆fν :=
it it
∆f +∆ν +κ ∆E [δde+∆p ]. Later, we absorb the change-in-expectation terms κ ∆E [δde+∆p ] into the
it it i t t t+1 i t t t+1
“demand shifter” ∆ν .
it
21

where η is a vector of common shocks (which can include observable factors, such as GDP growth,
t
or latent factors), λ is a vector of factor loadings, and u is an idiosyncratic shock. We make
i it
throughout the key identification assumption that
E[u η ] = 0. (30)
it t
The GIV method identifies ζ using variation that comes from the idiosyncratic shocks, u .
it
Using market clearing, we have ∆q = 0, that is
St
∆p = M (λ(cid:48) η +u ),
t S t St
for the multiplier
1
M = .
ζ
The goal is to estimate M, which identifies the demand elasticity, ζ.
The basic idea of the GIV is the following. We use idiosyncratic shocks to demand, u , as
it
primitive disturbances to the system, and we see how they affect prices and quantities. The GIV is
the size-weighted sum of those idiosyncratic shocks. Indeed, if we had access to u , we could just
St
estimate M by OLS, regressing ∆p = Mu +ε . We next detail how to measure those idiosyncratic
t St t
shocks empirically, or at least good proxies for them that make the above reasoning valid.
Simple example with uniform loadings We start with the case where there is a single factor,
η , and λ = 1, so that all loadings on the common shock are uniform. Then, the GIV is constructed
t i
from data as follows:
Z := ∆q = ∆q ∆q .
t Γt St Et
−
As ∆q = ζ∆p +η +u and ∆q = ζ∆p +η +u , we have:
St t t St Et t t Et
− −
Z = u u = u . (31)
t St Et Γt
−
As u is a combination of idiosyncratic shocks only, it is uncorrelated with η , see (30). This
Γt t
orthogonality condition makes Z = u a valid instrument: it is our GIV. Furthermore, if u
t Γt it
is homoskedastic, then u is uncorrelated with u .44This implies that ∆p = Mu + e , where
Γt Et t Γt t
e = M (η +u ) is uncorrelated with Z . Hence, if we estimate the OLS regression
t t Et t
∆p = MZ +e , (32)
t t t
then this identifies the true multiplier M. Alternatively, we can estimate ζ directly using Z as an
t
instrumental variable for ∆p in the regression
t
∆q = ζ∆p +(cid:15) , (33)
Et t t
−
with ∆p instrumented by Z .
t t
Intuitively, we use the sector-specific, or idiosyncratic, demand shocks of one sector as a source
of exogenous price variation to estimate the demand elasticity of another sector. Viewed this
way, the GIV estimator generalizes the idea behind the index inclusion literature to estimate the
44The same condition holds in the more general case of uncorrelated heteroskedastic u , with the inverse variance
it
weights E˜, so Z :=∆q ∆q (see Gabaix and Koijen (2020)).
t St
−
E˜t
22

micro elasticity. In the index inclusion literature, a demand shock to the group of index investors
(assuming the inclusion of a stock into the index is random) can be used to estimate the slope of
the demand curve of the non-index investors.
We reiterate that the methodology works even if we do not have data on flows f – it is enough
it
to have data on changes in equity holdings ∆q . This implies that we identify idiosyncratic shocks
it
to fν = f +ν , where f are capital flows and ν are demand shocks.
it it it it it
General case with non-uniform loadings In the general case with non-uniform loadings and
an r-dimensional vector of common latent shocks η , we define aˇ := a a , that is, the cross-
t it it Et
sectionally demeaned value of a vector a . We run a principal component−analysis (PCA) via the
t
model
∆qˇ = λ ˇ(cid:48)η +uˇ . (34)
it i t it
In this way, we extract r principal components, η . Then, we run the following OLS regression,
t
using the extracted factors η as controls:
t
∆p = MZ +β(cid:48)η +e , (35)
t t t t
and estimate the multiplier M as the coefficient on the GIV Z . The rest of Gabaix and Koijen
t
(2020) discusses numerous extensions of this basic structure and show its optimality by various
metrics (e.g. it is GMM optimal). As before, we can estimate ζ directly using Z as an instrumental
t
variable for ∆p in the regression
t
∆q = ζ∆p +β(cid:48)η +(cid:15) .
Et t t t
−
We leave the technical details of the specific algorithms that we use to Appendix B.1. We demon-
strate the performance of the GIV estimator in our specific setting in Appendix D.1 using simula-
tions.
GIV: Requirements and threats to identification FortheGIVtobeconsistent, weneed(30)
to hold: the idea is that there are random “bets” or “shocks” to various fund managers, institutions
and sectors, that are orthogonal to all reasonable common macro factors such as GDP, TFP, and so
forth. For the GIV to be a powerful instrument, we need large idiosyncratic shocks, and a few large
institutions, so that the market is “granular” in the sense that the idiosyncratic trading shocks of a
few large players meaningfully affect the aggregate.45 Fortunately, this is verified in our setting, as
it is in related settings in macro (Gabaix (2011), Carvalho and Grassi (2019)), trade (Di Giovanni
and Levchenko (2012)) or finance (Amiti and Weinstein (2018), Herskovic et al. (forthcoming),
Galaasen et al. (2020)). Ben-David et al. (forthcoming) and Ghysels et al. (2021) study the impact
of investor granularity on the cross-section of US stock returns.
The main threats to identification with GIV are that we do not properly control for common
factors, or that the loadings on the omitted factor are correlated with size, such that λ λ = 0.
S E
To mitigate the risk of omitted factors, we extract additional factors and explore the st−abilit(cid:54)y of
the estimates as we add extra factors.
45Indeed, when flow shocks have volatility σ , var(u ) = Hσ2, with H = S2. This “Herfindahl” H of the
u S u j j
holdings shares must be high: so we need a few large entities, such as funds or sectors.
(cid:80)
23

When firms are elastic and flows mean-revert When firms have a supply elasticity ζ , the
C
total elasticity is ζ + ζ , as we saw in Section 3.1. When flows mean-revert with speed φ , the
C f
measured elasticity is ζ + κφ , as we saw in (24) and (26). Combining those two extensions, the
f
measured price impact is
1
M = , ζM := ζ +κφ +ζ . (36)
ζM f C
As κφ and ζ appear to be small, the difference between ζ, ζ+κφ and ζM is rather minor, and is
f C f
best ignored in the first pass. Still, to be completely explicit, when we empirically measure “ζ”, we
actually measure a quantity that is ζ +κφ +ζ if flows mean-revert at speed φ and firms have a
f C f
supply elasticity ζ , and is strictly speaking ζ only when flows do not mean-revert and ζ = 0.46
C C
4.2 Elasticity estimates using sector-level data
Benchmark estimates We first report the GIV estimates of the macro elasticity using data from
1993.Q1 to 2018.Q4 using the Flow of Funds (FoF). Throughout this section, we model investors’
demand as
∆q = α ζ∆p +λ(cid:48)η +u , (37)
it i − t i t it
where we assume that the demand elasticity is the same across sectors. We relax this assumption
below using 13F data. We consider the same model for the corporate sector, but allow for a different
demand elasticity, ζ . The vector η includes GDP growth, a time trend,47 and one or more latent
C t
factors, ηPC.
t
The results are presented in Table 2. The first column reports the estimates where we use a
single principal component to isolate the idiosyncratic shocks to various sectors, in addition to a
common factor on which all sectors load equally.
We estimate a multiplier of M = 7.1, implying that purchasing 1% of the market results in a
7.1% change in prices. The corresponding standard error is 1.9.48 In the second column, we add a
second principal component. This lowers the multiplier estimate to M = 5.3. That is, purchasing
1% of the market results in a 5.3% change in prices. Both estimates imply that the aggregate stock
market is quite macro inelastic.
In the next two columns, we estimate the elasticities, ζ, by regressing demand changes on
instrumented changes in prices, as in (33). With one principal component, we estimate an elasticity
of ζ = 0.13 and with two principal components, we estimate ζ = 0.17. In the next two columns, we
estimate the supply elasticity ζ of the corporate sector. The short-run elasticity is low at ζ = 0.01
C C
for both one and two principal components.49 This implies that the combined elasticity is 0.14 (with
46Another enrichment would be to make capital flows sensitive to contemporaneous returns, say with a semi-
elasticity ζf, as in ∆f = ζf∆p +∆f˜. If ζq = 1 θ+κδ is the elasticity of the fund’s holdings given flows, the
t t t
− −
total elasticity of the funds’ holdings is ζ = ζq +ζf. If we have only holdings data (but not flows data), we can
measure ζq+ζf. If we have flows data, we can also measure ζf using the GIV.
47We include a time trend as some sectors grew faster in the nineties, for instance, than in the later period. We
show the robustness of our results to not including the time trend.
48We report Newey-West standard errors using the bandwidth selection as in Newey and West (1994).
49This small contemporaneous elasticity of the supply of shares by the corporate sector, estimated here causally
by IV, is consistent with the OLS findings of Ma (2019). She finds (Table VII) that Grossequityissuance =0.01πˆ (plus
Assets
other terms) at the quarterly frequency. Using that equity is about two thirds of assets, this leads, at the annual
frequency, to ∆q = 3 4 0.01πˆ =0.06πˆ, so that (by (18)) ζ =δ 0.06=0.0024. However, these estimates do not
C 2· · C ×
rule out the possibility that the medium- or long-run elasticities are higher and that firms play an important role in
stabilizing asset prices.
24

Table 2: Estimates of the macro elasticity. The first two columns report estimates of M with
one and two principal components, η , respectively. The next two columns report the elasticity
t
estimates, ζ, regressing the equal-weighted change in equity holdings ∆q on the price change ∆p
E
instrumented by the GIV Z. The next two columns report the elasticity of the corporate sector,
ζ . The final column reports the estimates of the same specification as the first column, but we
C
omit Z , where Z = S ∆qˇ and ∆qˇ defined in (63), to estimate the impact of sector-specific
t t i i,t−1 it it
shocks on prices. In constructing ∆qˇ , all estimates control for quarterly GDP growth. We report
it
the standard errors,(cid:80)which are corrected for autocorrelation, in parentheses. The sample is from
1993.Q1 to 2018.Q4.
∆p ∆p ∆q ∆q ∆q ∆q ∆p
E E C C
Z 7.08 5.28
(1.86) (1.10)
∆p -0.13 -0.17 -0.01 -0.01
(0.04) (0.05) (0.01) (0.02)
GDP growth 5.99 5.97 0.56 0.85 0.22 0.23 5.93
(0.69) (0.67) (0.27) (0.33) (0.13) (0.16) (0.91)
η 21.06 23.72 3.98 5.49 -0.72 -0.64 31.50
1
(13.58) (12.79) (2.08) (2.07) (0.69) (0.81) (15.57)
η 29.95 5.62 0.29
2
(6.54) (2.15) (0.67)
Constant -0.01 -0.01 0.00 0.00 -0.00 -0.00 -0.01
(0.01) (0.01) (0.00) (0.00) (0.00) (0.00) (0.01)
Observations 104 104 104 104 104 104 104
R2 0.436 0.515 0.279
25

Figure 2: Estimates of the aggregate multiplier M = 1 by horizon. The figure plots the multi-
ζ
period impact of demand shocks: a demand shock of f at date t increases the (log) price of equities
t
from t 1 to t + h by Mf . We use the GIV for instrumentation, see (38). The horizontal axis
t
indicate−s the horizon in quarters, from zero (that is, the current) to four quarters. Standard errors
are adjusted for autocorrelation. The sample is from 1993.Q1 to 2018.Q4.
reilpitluM
02
51
01
5
0
5−
−1 0 1 2 3 4
Horizon (quarters)
Multiplier 95%−confidence interval
one principal component) or 0.18 (with two principal components). The corresponding multipliers,
M = 1 , are M = 7.1 and M = 5.9, respectively.
In
ζ+
th
ζCe
final column, we report the same regression as in the first column but without the
instrument Z . By comparing the R-squared values, we obtain an estimate of the importance of
t
sector-specific shocks on prices. We find that the difference in R-squared values is 16%, which
highlights the importance of sector-specific shocks on prices.
The impact of flows at longer horizons In Figure 2, we explore how demand and flow shocks
propagate across time. To this end, we extend the earlier analysis by estimating
p p = a +M Z +c ηPC,e +d ∆y +(cid:15) , (38)
t+h t−1 h h t h t h t t+h
−
for h = 0,1,...,4 quarters, where p p is the (h + 1) quarter (geometric) return on the
t+h t−1
aggregate stock market. Recall that ηPC−,e is the principal com−ponent, extracted in the third step
t
of the GIV procedure as outlined in Section B.1. The figure reports M at a certain horizon. We
h
also consider a regression where we replace the left-hand side by p p , which we refer to as
t−1 t−2
h = 1. To construct the confidence intervals, we account for the aut−ocorrelation in the residuals
due t−o overlapping data.
We find that the cumulative impact is fairly stable over time. This is intuitive as sharp reversals
would imply a strong negative autocorrelation in returns, which is not something that we observe
for the aggregate stock market at a quarterly frequency. As such, and consistent with the theory,
persistent flow shocks lead to persistent deviations in prices. Size-weighted sector-specific demand
shocks are also not correlated with returns at t 1 (that is, h = 1). Unfortunately, however, the
− −
26

confidence interval widens quite rapidly with the horizon, which limits what we can say about the
long-run multiplier.
Robustness We explore the robustness of our estimates along various dimensions. In the interest
of space, we report and discuss the tables in Appendix D.4. In Tables D.8–D.10, we consider a
variety of robustness checks related to the sample period, data construction, and implementation
choices of the GIV estimator. We conclude that our results are robust to these changes in the
empirical strategy with multiplier estimates ranging from 3.5 to 8.
4.3 Elasticity estimates using investor-level data
We provide an alternative estimate of the same elasticity, but now using more disaggregated,
investor-level 13F and mutual fund data.50 We use 13F data from FactSet that cover the period
from 2000.Q1 to 2019.Q4 and we follow the data construction as in Koijen et al. (2019). Monthly
mutual fund flows come from Morningstar from January 1993 to December 2019. We provide details
in termsof the data constructionin Appendix C.2. An advantage ofthesedisaggregated datais that
we can allow for heterogeneous demand elasticities across investors. To provide another estimate of
the multiplier, we proceed in three steps.
First, we estimate innovations in fund flows for mutual funds. Let ∆f be the fractional inflow
t
into equity markets from mutual funds.51 We estimate
k
∆f = a + a ∆f +ct+(cid:15)f , (39)
t 0 l t−l mt
l=1
(cid:88)
at a monthly frequency (see Table D.12 in Online Appendix D.6). We also define K = 1 ,
1−(cid:80)k
l=1
a
l
which is the cumulative flow due to shocks (cid:15)f : as per Proposition 5, what matters is the cumulative
mt
future inflow, which is K(cid:15)f .52
mt
It is well known that the innovations, (cid:15)f , are correlated with contemporaneous realized returns
mt
(Warther (1995); Edelen and Warner (2001); Goetzmann and Massa (2003)). We extend this
literature by removing aggregate demand factors and isolating the idiosyncratic demand shocks
of mutual fund investors. In addition, we show how to translate the persistence in flows to a theory-
based estimate of the multiplier via K. We aggregate the monthly innovations, (cid:15)f , for k = 3 in
mt
each quarter and refer to these innovations as (cid:15)f. We model
t
(cid:15)f = β(cid:48)η +β(cid:48)C +uf,
t 0 t 1 t t
50In the US, all institutional investment managers managing over $100 million or more in “13F securities” (which
include stocks) must report their holdings on Form 13F every quarter.
51To compute the relevant measure of flows, we start from the share invested in US equities by fund i, θ , assets
it
undermanagement,W ,andtheflow∆F asdefinedbyMorningstar. Whenequitysharesaremissingatamonthly
it it
frequency, we fill in the equity shares using the most recent value for a given fund. We first compute ∆f = ∆Fit
it Wi,t−1
and winsorize it at 1% and 99% in each period. We then compute ∆f
t
= (cid:80) (cid:80)i θ
i
i,
θ
t−
i,t
1
−
W
1
i
W
,t−
i,t
1
−
∆
1
fit, which uses equity-
weighting, as warranted by the theory, see (10). We include “US equity,” “sector equity,” “international equity,” and
“allocation” funds in the analysis. Appendix C.2 provides additional details.
52In principle, it should be discounted at a rate ρ, but this is immaterial at the horizon of a few months that we
use. See Section G.5 for details.
27

where η are common unobserved factors, C are common observed factors, and uf are the unique
t t t
shocks to fund flows.53
Second, we wish to estimate those common factors, η , to isolate the shocks that are unique to
t
mutual fund investors. To do so, we use the 13F filings of investors outside of the mutual fund
industry (e.g., pension funds, insurance companies, and so forth).54 We consider an extension of
the model in (37), where we allow for heterogeneity in demand elasticities, ζ :
i,t−1
∆q = α ζ ∆p +λ(cid:48) η +β(cid:48)C +u .
it i − i,t−1 t i,t−1 t i t it
We assume a parametric specification for elasticities and a semi-parametric specification for factor
loadings:
ζ = ζ
˙(cid:48)x
, λ = λ
˙(cid:48)x
+λ
¨
,
i,t−1 i,t−1 i,t−1 i,t−1 i
where x is a vector of investor characteristics of which the first element is equal to 1, and ζ ˙,
i,t−1
λ ˙, and λ ¨ are to be estimated. As investor characteristics, we use active share and log AUM. In
i
addition, we allow for non-parametric factors via λ ¨ , as before. We also control for GDP growth and
i
allow investors to have heterogeneous exposures to macroeconomic conditions via β(cid:48)C . We discuss
i t
in Section B.1 how we estimate the common factors, η , and we refer to the estimates as ηe.
t t
Third, we regress returns on fund flow innovations, while controlling for common factors,
∆p = a+MZ +λ(cid:48)ηe +m(cid:48)C +e ,
t t t t t
where Z = KSMF(cid:15)f, with SMF the share of aggregate equities held by the mutual fund sector:
t t−1 t t−1
after controls, this is the surprise inflow unique to mutual funds. As a common observed factor, C ,
t
we use GDP growth. We also explore robustness to controlling for changes in volatility in C .
t
The results are summarized in Table 3. The first column presents the results with only Z
t
and GDP growth, something we show for illustration but do not recommend using. The next four
columns add the factors extracted from the 13F data, ηe, as recommended by the GIV. In the
t
final column, we also control for the quarterly (percentage) change in volatility. Without controls
other than GDP in Column 1, the multiplier estimate equals M = 10.9. By adding additional
controls, the R-squared value increases significantly and the multiplier estimate lowers, as we would
expect since demand shocks and prices are positively correlated. With four additional factors, the
R-squared value equals approximately 60% and the multiplier drops to M = 7.7 with a standard
error of 2.3. In the final column, we add changes in volatility. While these do not correlate strongly
with fund flow innovations, they do correlate with returns. This suggests that other investors are
negatively sensitive to volatility and this also captures a source of demand shocks. The multiplier
lowers further to 7.6 and the R-squared is now 70%.55 In Figure D.8, we also repeat the long-horizon
analysis as in Figure 2. As before the impact of flow shocks on prices is persistent although the
confidence interval is wide at longer horizons of one year.
In summary, we find that the multiplier estimates are quite consistent with the estimates we
found using the FoF data. These estimates well above 1 are consistent with the estimates for other
53Flows themselves may be sensitive to prices, so that (cid:15)f = ζf∆p +β(cid:48)η +β(cid:48)C +uf. In this case, if ζf is
t − t 0 t 1 t t
negative, as is the case when mutual fund investors engage in positive feedback trading, then our estimates provide
a lower bound.
54Specifically, we omit investors outside of the mutual fund industry using the same assignment of investor types
as in Koijen et al. (2019). This removes, for instance, investment advisors and mutual funds as classified by FactSet.
55As volatility is endogenous, it can be included only with interpretative circumspection. We include it here for
descriptive purposes.
28

Table 3: Estimates of the macro elasticity using mutual fund and 13F data. The first five columns
provide estimates of the multiplier M, which is the coefficient on Z = KSMF(cid:15)f, the innovation in
t t−1 t
the cumulated inflow into mutual funds after controls. We regress returns on unexpected flows, (cid:15)f,
t
times the share of aggregate equities held by the mutual fund sector, SMF, and adjusting for the fact
t−1
that inflows are autocorrelated (see (39) and the surrounding definition of K). In the first column
we only control for GDP growth and in the next four columns we add one to four common factors
to isolate the idiosyncratic component in mutual fund flows. The common factors are extracted
from 13F filings of institutions outside of the mutual fund industry. In the final column, we add
the change in quarterly volatility as an additional control. We report the standard errors, which
are corrected for autocorrelation, in parentheses. The sample is from 2000.Q1 to 2019.Q4.
∆p ∆p ∆p ∆p ∆p ∆p
Z 10.93 10.85 8.54 7.69 7.69 7.62
(2.64) (2.78) (2.18) (2.32) (2.34) (1.92)
GDP growth 4.19 4.21 4.94 4.99 5.00 3.43
(1.23) (1.25) (0.96) (1.17) (1.17) (1.17)
PC1 -0.91 -0.94 -0.95 -0.95 0.06
(0.74) (0.60) (0.63) (0.63) (0.61)
PC2 -2.98 -3.07 -3.07 -0.82
(0.66) (0.48) (0.48) (0.37)
PC3 -0.87 -0.87 -1.25
(0.56) (0.56) (0.41)
PC4 0.11 -0.21
(0.33) (0.38)
∆σ -0.10
(0.01)
Constant 0.00 0.00 -0.00 -0.00 -0.00 0.00
(0.00) (0.00) (0.01) (0.00) (0.00) (0.00)
Observations 80 80 80 80 80 80
R2 0.426 0.438 0.556 0.565 0.566 0.699
29

countries and for style factors, see Table 1. Future research can explore other strategies to control
for common demand factors to sharpen the identification.
4.4 A new measure of capital flows into the stock market
In this final section, we construct a new measure of capital flows into the stock market consistent
with the theory in Section 3. While our theory provides conceptual clarity in terms of how to
measure flows into the market, and to get around the problem that “for every buyer there is a
seller,” the data required are unfortunately not available for all investors.
In Section 4.4, we propose a way to construct an empirical counterpart to the measure based
on the available data. As this measure is new to the literature, we show its connection to prices,
macroeconomic variables, and beliefs. The results in this section provide an initial analysis of the
potential determinants of flows into the aggregate stock market. These results are intentionally
descriptive in nature and understanding the primitive drivers of these flows is an important task
for future research.
Measuring flows into the stock market We rely on the FoF data for these calculations and
we refer to Appendix C for details on the data construction of the fixed income positions and flows.
As (10) shows, the flow into the aggregate stock market can be measured by first computing the
flow for each investor, ∆f = ∆Fit , and then computing the equity weighted average, ∆f =
it Wi,t−1 St
θi,t−1Wi,t−1 ∆f . Unfortunately, the FoF aggregates data across many institutions and the
rep i o (cid:80) rtie θi d ,t− fl 1 o W w i,t s −1 can i b t e mismeasured by this definition. To see this, consider the case in which some
(cid:80)
households only invest in bonds and other households only invest in equities. If we view this as a
combined household, a 1% combined inflow into financial markets does not necessarily lead to a 1%
increase in equity holdings as the flow may be a flow to bond funds only. With disaggregated data,
such problems can be solved, but such data are unfortunately unavailable.
We propose a simple diagnostic to assess whether flows are measured accurately. In particular,
in our model, the elasticity of demand to flows equals one, see (7). We therefore estimate
∆q = α+β f +γ ∆p +δ ∆y +(cid:15) . (40)
it i it i t i t it
We report the estimates of β in Table D.13 in Appendix D. When we cannot reject H : β = 1
j 0 i
at the 5% significance level, we use the total flow. If this null hypothesis is rejected, we use the
equity flow instead. We refer to these “screened flows” as f∗. The aggregate flow is then given by
it
f∗ = S f∗ +f , where f corresponds to net repurchases of equities by firms.
St i i,t−1 it Ct Ct
(cid:80)
The correlation between capital flows and equity returns We relate our measure of capital
flows into the stock market to returns. In the left panel of Figure 3, we show that our measure
of flows is strongly correlated with returns using a binned scatter plot in the left panel. We again
find that the slope is high, but we emphasize that, because of endogeneity, the slope is not a good
measure of the impact of flows of the price. This is why earlier we developed an IV strategy to
measure that impact.56
56Ifonehasdataoncapitalflowsforasubstantialnumberofsectors, thenitwouldbepossibletoconstructaGIV
estimate based on capital flows alone. This would make it possible to estimate the causal impact of prices on capital
flows and of capital flows on prices.
30

Figure 3: Capital flows into the stock market and price changes. We plot the aggregate flow
into the stock market, using the screened flows, f∗, f∗ = N S f∗, versus the return on the
jt St j=0 j jt
aggregate stock market in the left panel used a binned scatter plot. In the right panel, we construct
a cumulative (log) return index and compute cumulative flow(cid:80)s. We extract the cyclical component
using the methodology developed in Hamilton (2018). We standardize both measures over the full
sample to be able to plot them in the same figure. The sample for both figures is from 1993.Q1 to
2018.Q4.
nruteR
2.
1.
0
1.−
2.−
−.005 0 .005 .01
Flow
4
2
0
2−
4−
1995q1 2000q1 2005q1 2010q1 2015q1 2020q1
Date
Cycle flows Cycle prices
We can also illustrate the strong co-movement between flows and prices at lower frequencies.
In particular, we construct a cumulative (log) return index and compute cumulative flows. We
then extract the cyclical component using the methodology developed in Hamilton (2018). We
standardize both measures, by removing the time-series mean and dividing them by their standard
deviations, over the full sample to be able to plot them in the same figure. These are shown in
the right panel of Figure 3. Consistent with the high-frequency co-movement that we uncover in
the left panel of Figure 3, we find that prices and flows co-move at a business cycle frequency. We
re-emphasize once again that these are merely correlations and it may be the case, for example,
that they reflect positive feedback trading by investors (Cutler et al. (1990), Shleifer (2000)).
Relating flows to shocks to GDP and to return expectations To conclude this initial
exploration of capital flows into equity markets, we relate flows to shocks to economic activity and
survey expectations of returns. We use GDP growth as our measure of economic activity, as before.
For return expectations, we use the survey from Gallup. The data are described in more detail
in Appendix C. Gallup has several missing observations and only starts in 1996.Q4. We only use
data for all series when they are non-missing, which gives us 79 quarterly observations. To obtain
innovations, we estimate an AR(1) model for each of the series (except returns). We standardize
each of the innovation series, by removing the time-series mean and dividing them by their standard
deviations, to simplify the interpretations of the regressions.
The results are presented in Table 4. In the first three columns, we relate capital flows to
survey expectations and economic growth. We find that flows and survey expectations are strongly
correlated,confirmingGreenwoodandShleifer(2014)usingamorecomprehensivemeasureofcapital
flows. A one standard deviation increase in survey expectations of future returns is associated with
a 0.48 standard deviation increase in capital flows.
This finding may point to a resolution of a recent challenge posed to the beliefs literature by
31

Table 4: Descriptive statistics on capital flows, survey expectations of beliefs, economic activity,
and stock returns. The table reports the time-series regressions of innovations to flows in the first
threecolumnsoninnovationstosurveyexpectationsofreturns(column1), GDPgrowthinnovations
(column 2), and both variables combined (column 3). We estimate the innovations in all cases by
estimating an AR(1) model, and normalize them to have unit standard deviation. Then we regress
returns on flow innovations (column 4), innovations to survey expectations of returns (column 5),
GDP growth innovations (column 6), and all three variables combined (column 7). The sample is
from 1997.Q1 to 2018.Q4, with some gaps, due to missing data for the Gallup survey.
Flow Flow Flow Return Return Return Return
Gallup 0.48 0.46 0.61 0.33
(0.10) (0.11) (0.09) (0.09)
GDP growth 0.21 0.06 0.41 0.21
(0.11) (0.11) (0.10) (0.08)
Flow 0.65 0.45
(0.09) (0.09)
Constant 0.00 0.00 0.00 0.00 0.00 0.00 0.00
(0.10) (0.11) (0.10) (0.09) (0.09) (0.10) (0.07)
Observations 79 79 79 79 79 79 79
R2 0.233 0.046 0.237 0.426 0.376 0.171 0.582
Giglio et al. (2021a). In particular, they find that although survey expectations of returns are
volatile, the pass-through to actions (that is, portfolio rebalancing) is low. One possibility is that
the strong correlation between innovations to beliefs and prices (which equals 61% in our sample)
arises even though the pass-through is low, but small flows into inelastic markets lead to large price
effects.
Flows and economic activity, as analyzed in the second column, are also positively correlated,
but the relation is substantially weaker. In the third column, we combine survey expectations and
economic activity, and find that the latter is insignificant. In the remaining columns, we study the
association between returns and flows, beliefs, and economic activity. A one standard deviation
increase in capital flows is associated with a 0.65 standard deviation increase in returns, which
is similar to a 0.61 standard increase in case of survey expectations. The link to GDP growth is
significant, but weaker with a slope coefficient of 0.41. In the final column, we combine all flows,
beliefs, and GDP growth and find that even in this multiple regression, all variables are significant.
The R-squared of this final regression is high and amounts to R2 = 58%.
Obviously, this analysis is just an initial exploration into the determinants of flows, and more
disaggregated data may be used to explore the determinants of capital flows for various institutions
and across households. If the inelastic markets hypothesis holds, this is an important area for future
research.
32

5 General Equilibrium with Inelastic Markets
So far, we took both the risk-free rate r and the average equity premium π¯ as exogenous. We now
f
endogenize them. For instance, we shall see how flows from bonds to stocks, which alter the price
of stocks, can at the same time keep the risk-free rate constant (in our model, this is because the
optimizing household also trades off saving in bonds versus consumption, and this way ensures that
the consumption-based Euler equation for bonds holds). We view this as a prototype for how to
build general equilibrium models with inelastic markets, merging behavioral disturbances, the flows
they create, their impact on prices, and potentially their impact on production.
5.1 Setup
For simplicity, we discuss in detail an endowment economy. It will be easy to then generalize the
model to a production economy. This general equilibrium model is a specialization of our infinite-
horizon model of Section 3.2 – it specifies things left general in that model, such as the origin of
the interest rate.
The endowment Y follows a proportional growth process, with an i.i.d. lognormal growth rate
t
G Be t : cau Y Y ts− t e1em = p G iri t ca = lly e d g+ iv εy t id − e 2 1 n σ d y 2, g w ro i w th th εy t a + n 1 d∼GDNP g 0 r , o σ w y 2 th . a U re ti n li o t t y v i e s ry c t o β rr t e u la ( t C e t d ) , w w i e th mo u d ( e C l ) th = at G C 1 1 − D − γ γ P .
Y is divided as Y = +Ω into an aggregate (cid:0) divid (cid:1) end and a(cid:80)residual Ω , where the dividend
t t t t t t
stream has i.i.d. lognDormal growth, D D t− t 1 = GD t = eg+εD t D −1 2 σ D 2 , so that the balanced growth path
specified in Section 3.2 has a cumulative growth factor = GD...GD. The “residual” Ω can be
thought of as a combination of wages, entrepreneurial iGn t come, t and so 1 forth (and indeed t it is the
vast majority of GDP).57 The representative firm raises capital entirely through equity, and passes
the endowment stream as a per-share dividend D = Dt , where Q is the number of shares of equities
t Q
supplied by the corporate sector, which is an unimportant constant in this baseline model without
share buybacks and issuances. Bonds are in zero net supply.58 We write the price of equities as
P = Dtept , where δ is the average dividend-price ratio and p is the deviation of the price from the
t δ t
baseline p = 0. Those quantities are all endogenous.
t
There are two funds: a pure bond fund, which just holds bonds, and the representative mixed
fund, which holds bonds and equities. The mixed fund has a mandate, to hold a fraction in equities
equal to:
θ = θexp κDp +κE [∆p ] , (41)
t t t t+1
−
which is the same as before in (1), to the leading order (in terms of deviations from the steady
(cid:0) (cid:1)
state), with κD = κδ. The formulation here is slightly more general.59
Consumption and investment by households We describe the behavior of the representative
household. SectionG.8providesmoreformalismandfurtherdetails. Thedynamicbudgetconstraint
57Formally, it could become negative, as in Campbell and Cochrane (1999), though this is a very low probability
event in our calibration. Then, the interpretation is that of a residual liability. In addition, it would be easy to keep
/Y stationary, at the cost of having it as one more state variable, reverting to its mean.
t t
D
58We can easily have the government issue bonds, backed by taxation, see Section G.8.1.
59But here we allow the mandate to potentially differentiate between “return predictability coming from the price-
dividend ratio” (captured by κDp ) and “return predictability because the price is predictable”. In a number of
t
−
settings the first one (the “carry”) is stronger than the last one (Koijen et al. (2018)), so having two κ’s is sensible.
33

of household h entails:60
QB,h
QB,h +Dh +Ωh = Ch +∆Fh + t+1. (42)
t t t t t R
f,t
Indeed, the left-hand side is the bond asset position of the household at the beginning of period t:
QB,h gives the bond holdings at the beginning of period t, while Dh and Ωh are the dividend and
t t t
residual income received by the household in its pure bond fund (which includes the “dividends”
paid by the mixed fund). This bond position is spent on consumption Ch, flows ∆Fh into the mixed
t t
fund, and investment in bonds, with a face value QB,h.
t+1
We need a behavioral element, otherwise the investor would fully undo the funds’ mandate. We
choose to decompose the household as a rational consumer, who only decides on consumption (so
dissaving from the pure bond fund), and a behavioral investor, who trades between the pure bond
fund and the mixed fund.
The rational consumer part of the household chooses consumption (but not equity shares) to
maximize lifetime utility, subject to the dynamic budget constraint for bonds (42). She takes the
actions of the investor as given.61 As she is rational, she satisfies the Euler equation for bonds:
C −γ
E β t+1 R = 1, (43)
t ft
C
(cid:34) t (cid:35)
(cid:18) (cid:19)
with C = Y in equilibrium. This pins down the interest rate R , which is constant in our i.i.d.
t t ft
growth economy.
The behavioral investor part of the household is influenced by b , a behavioral disturbance. It
t
is a simple stand-in for noise in institutions, beliefs, tastes, fears, and so on. We assume that the
investor trades (between stocks and bonds) with a form of “narrow framing” objective function (as
in Barberis et al. (2006)). He seeks to maximize E [Vp(W )] with Vp(W) = W1−γ−1 a proxy
t t+1 1−γ
value function. Specifically, when b = 0, he chooses his allocation θ ¯M in the mixed fund as:
t
θ ¯M = argmaxE Vp 1 θM R +θMR b = 0 , (44)
ft M,t+1 t
− |
θM
(cid:2) (cid:0)(cid:0) (cid:1) (cid:1) (cid:3)
where R is the stochastic rate of return of the mixed fund. This choice of a “narrow framing”
M,t+1
benchmark is opposed to the fully rational value function, which would have all the Merton-style
hedgingdemandterms,andwouldleadtotheconsumptionCAPMholdingonaverage: inparticular,
the equity premium would be too small, as in the equity premium puzzle (at π¯ = γcov εD,εy ).
t t
Instead, the above formulation with narrow framing will lead to a high equity premium π¯ = γσ2,
(cid:0) (cid:1)r
where the σ2 is the volatility of the stock market, which is affected by flow shocks.62
r
If there are no behavioral disturbances, an investor wishing to maintain a constant allocation θ ¯M
in the mixed fund should invest via F ¯ = 1−θ P ¯ P ¯ Q ¯, as in Section 3.2, that is, ∆F ¯ = 1−θ∆ .
We assume that his policy, however, i t s affe θ cted t b−y th 0 e behavioral disturbance b , so tha t t the θδ actDua t l
t
(cid:0) (cid:1)
flow is
1 θ 1
∆F = − ∆ + ∆(b ), (45)
t t t t
θδ D δ D
60There is also the usual transversality condition, lim βt Ch −γ QB,h =0.
t→∞ t t
61One could imagine a variant, where the consumer manipulates the investor’s actions. This would lead her to
(cid:0) (cid:1)
distort her Euler equation for consumption.
62This choice of “narrow framing” leads to a high equity premium. It could be replaced by another device such as
disasters. We choose here narrow framing as this behavioral ingredient is well in the behavioral spirit of this section.
34

which is higher than the baseline amount ∆F ¯ by a fraction ∆b of the “fundamental value” Dt of
t t δ
the equity market. Here we will specify that b is an AR(1).
t
In Appendix G.9, we provide a formal microfoundation of flows via beliefs: the financier part of
the household believes that the deviation of the equity premium from trend is πˆH. Under simple
t
conditions, this leads to a flow
f = κHπˆH, (46)
t t
with κH the sensitivity to the risk premium, and to a behavioral deviation b = ft. Using the
t θ
empirical findings of Giglio et al. (2021a), we estimate that κH 2, a value that we rationalize by
calibrating it in terms of other behavioral parameters. This esti(cid:39)mate is in contrast with a rational
model, which would imply κH = 1 22, a very large pass-through from beliefs to portfolio shares.
A low value of κH means that peo π¯ pl(cid:39)e have “bold forecasts” (excess variations in the perceived equity
premium) but make “timid choices” (small flows), very much as in Kahneman and Lovallo (1993).63
This type of model can be also made to match the perspective in Bordalo et al. (2020), in which
all variation in prices, flows, and the perceived risk premium πˆH comes from changes in the long-
t
term growth forecast g (all in deviations from a trend), in a way still governed by (46): Section G.9
t
provides details and a calibration. One could image a richer model for the perceived risk premium
πˆH, e.g. with extrapolative beliefs based on realized returns or growth rates. One could then work
t
out the implications for flows (via (46)) and prices (via Proposition (5)).
We conclude that linking flows to beliefs is a promising and manageable line of research, and
the analytics that we provide in this section and in Appendix G.9 help thinking about this. At the
same time, there may be other determinants of flows, for instance binding risk constraints, changes
in regulation or policy, and reaction to fairly irrelevant news, which is why we find it useful to
separate the impact of the behavioral deviation b from its determinants.
t
We finally formally define the equilibrium.
Definition 1. The state vector is Z = (Y , , ,b ). An equilibrium comprises the following
t t t t−1 t
functions: the stock price P (Z), the interest rDateD R (Z), and the consumption and asset allocation
f
C(Z), B(Z), such that the mixed fund’s allocation θ(P,Z) follows its mandate, and: (i) the
consumer follows the consumption policy C(Z), which maximizes utility subject to the above
constraints; (ii) the investor follows the behavioral policy (45), where the average allocation in the
mixed fund is given by (44), so that it is quasi-rational with narrow framing on average, but with
disturbance b ; (iii) the mixed fund’s demand for stocks Q(Z) follows its mandate (41); (iv) the
t
consumption market clears, C(Z) = Y (Z); and (v) the equity market clears, Q(Z) = Q.
5.2 Model solution
Proposition 6 describes the solution of this economy. In particular, it shows that the link between
the disturbance b and the cumulative flow f is as follows. Starting from an equilibrium situation,
t t
where b = 0, the cumulative “excess” flow is equal to:
0
f = θb . (47)
t t
This holds for any process b . Now, we specialize to the case where b follows an AR(1) with speed of
t t
mean-reversionφ . Then, sodoesf , sothatweareinthe“simplebenchmark” caseof (25)-(26), and
f t
63Quantitatively, to match the calibrated volatility of flows of σ = 2.8% (as in Table 6) we need a moderate
f
variation of beliefs σ =1.4%.
πH
35

now with an endogenous interest rate and unconditional equity premium. This AR(1) assumption is
just a placeholder for richer behavioral assumptions, for example driven by time-varying beliefs (as
in Caballero and Simsek (2019), Bordalo et al. (2020)), positive or negative feedback trading rules,
and so on. We defer to future research for richer, empirically-grounded models of the “behavioral
deviation” b , and hence of the flows. The limited goal of this framework is to have a simple model
t
of the impact of the flows in general equilibrium, which can be fully solved and which lends itself
to a number of variants. Importantly, it relies on observable flows.
Proposition 6. The solution of the economy obtains in closed form as follows, taking the limit of
small time intervals and only the first order terms in f . The market elasticity ζ and the “macro
t
market effective discount rate” ρ (see Proposition 5) are:
ζ
ζ = 1 θ+κD, ρ = . (48)
− κ
The price of equities is:
D
P = t ept, (49)
t
δ
where D is the dividend, δ = r +π¯ g is the average dividend-price ratio, and p is the deviation
t f t
−
of the price from its rational average, which increases with flows:
1
p = bpf , bp = . (50)
t f t f ζ +κφ
f
Hence the variance of stock market returns is
σ2 = var εD +bpεf , (51)
r t f t
(cid:16) (cid:17)
and depends on both fundamental risk (εD) and flow risk (εf). Both contribute to the average equity
t t
premium, which is:
π¯ = γσ2. (52)
r
The equity premium at time t is lower than its average when flows have been high, as:
π = π¯ +bπf , bπ = (δ +φ )bp. (53)
t f t f − f f
Finally, the interest rate is constant, and given by the consumption Euler equation (43):
σ2
r = lnβ +γg γ(γ +1) y . (54)
f
− − 2
Hence, we have a fairly traditional economy, except that, crucially, prices and risk premia are
now driven by flows and flow risk, in addition to fundamentals, and that markets are inelastic.
Hence, the equity premium is time-varying (because of flows), and on average higher than in the
consumption CAPM (because it reacts to flow risk, not just fundamental risk, and because the nar-
row framing makes the investor react to the variance of equity returns, rather than their covariance
with consumption), as given in (52).
36

5.3 Pricing kernel consistent with flow-based pricing
We show how to express the economics of flows in inelastic markets in the language of pricing
kernels or stochastic discount factors (SDFs). To do so, we use a simple general method to complete
a “default” pricing kernel so that it reflects the impact of flows on asset prices. The idea is simply
that there is a fringe of infinitesimal traders that can absorb any infinitesimal amount of new
assets. That gives rise to a “flow-based” pricing kernel (see Section G.10 for details). In our general
equilibrium model, this SDF is:
εD
= exp( r π t+1 +ξ ), π = π¯ +bπf , (55)
M t+1 − f − t σ2 t t f t
D
where σ2 = var εD and ξ is a deterministic term ensuring that E [ ]er f = 1, so that
D t+1 t t M t+1
ξ = π t 2 if εD is Gaussian.
t T − hi 2 s σ D 2 “flow- t b + a 1 s (cid:0) ed” p (cid:1) ricing kernel is an alternative to the consumption-based kernel of Lucas
(1978). The core economics is in how flows affect prices, and the pricing kernel (55) just reflects
that. The flow f modifies the price P according to Proposition 6 and also the pricing kernel ,
t t t+1
in such a way that P = E [ (D +P )] holds. The pricing kernel is in a sense a symMptom
t t t+1 t+1 t+1
rather than a cause in that Mmarket.
To sum up, the flow-based SDF (55) reacts to flows, and prices equities and bonds:
E [ R ] = 1, E [ R ] = 1.
t t+1 M,t+1 t t+1 ft
M M
However, in this model, consumption does not directly price equities, though it does price bonds:
C −γ C −γ
E [β t+1 R ] = 1, E [β t+1 R ] = 1.
t
C
M,t+1
(cid:54)
t
C
ft
t t
(cid:18) (cid:19) (cid:18) (cid:19)
5.4 Calibration of the general equilibrium model
We now calibrate the general equilibrium model. This extends the calibration of Section 3.2, which
is natural as the general equilibrium model is an extension of the basic infinite horizon model. We
use the parameter values given in Table 5, which are all presented in annualized terms for clarity.
We provide a summary discussion of our parameter choices here, leaving some details to Section H.
Risk aversion is moderate, at γ = 2. The macroeconomic parameter values are standard, except for
the pure rate of time preference.64 We set a speed of mean reversion of the behavioral disturbance
of φ = 4%/year, which induces the same speed of mean reversion for flows f and for the P/D
b t
ratio. Likewise, we choose its standard deviation to generate the requisite volatility of flows. For
parsimony, we assume zero correlation between flow shocks and dividend shocks.
Table 6 shows the resulting moments implied by the model. It verifies that we match all the
“classic” moments, for instance the risk-free rate, the average equity premium, and the volatility of
64To get a small risk-free rate of 1% (and only for this reason), we need to make the agents very patient, so that
β > 1. Indeed, this comes from the Ramsey equation (54), which is r lnβ +γg (neglecting precautionary
f
(cid:39) −
effects, which are very small in our calibration) with γg =4%. We share this issue with the overwhelming majority
ofthemacroeconomicsliterature: ifwenormalizedtheaveragegrowthratetozero, likemostofthemacroeconomics
literature,wewouldnothavethisdifficulty. Itwouldbeeasytoamendthat,forexamplebyaddingasmallprobability
of a disaster risk or by using Epstein-Zin preferences. We do not do that, because we do not wish to complicate the
model.
37

Table 5: Parameter values used in the calibration
Variable Value
Growth rate of endowment and dividend g = 2%
Std. dev. of endowment growth σ = 0.8%
y
Std. dev. of dividend growth σ = 5%
D
Mixed fund’s equity share θ = 87.5%
Mixed fund’s sensitivity to risk premium κ = 1
Speed of mean-reversion rate of behavioral disturbance φ = 4%
b
Std. dev. of innovations to behavioral disturbance σ = 3.3%
b
Time preference β = 1.03
Risk aversion γ = 2
Notes. Values are annualized.
Table 6: Moments generated by the calibration
Variable Value
Macro elasticity ζ = 0.16
Macro elasticity with mean-reverting flow ζM = ζ +κφ = 0.2
f
Macro market effective discount factor, ρ = ζ/κ ρ = 16%
Risk free rate r = 1%
f
Average equity premium π¯ = 4.4%
Average dividend-price ratio δ = 3.4%
Std. dev. of stock returns σ = 15%
r
Share of variance of stock returns due to flows 89%
Share of variance of stock returns due to fundamentals 11%
Mean reversion rate of cumulative flow and logD/P φ = 4%
f
Std. dev. of innovation to cumulative flow σ = 2.8%
f
Slope of log price deviation to flow bp = 5
f
Slope of equity premium to flow bπ = 0.37
f −
Notes. Values are annualized.
38

Table 7: Some stock market moments and predictive regressions
(a) Stock market moments
Data Model
Std. dev. of excess stock returns 0.17 0.15
Mean P/D 37 33
Std. dev. of logP/D 0.42 0.5
(b) Predictive regressions
Data Model
Horizon Slope S.E. R2 Mean of slope 95% CI of slope S.E. R2
1 yr 0.11 (0.034) 0.07 0.14 [0.04,0.32] (0.048) 0.09
4 yr 0.36 (0.14) 0.18 0.61 [0.18,1.19] (0.17) 0.28
8 yr 1.00 (0.34) 0.40 1.34 [0.39,2.50] (0.31) 0.43
Notes. The data are for the United States for 1947-2018, and are calculated based on the CRSP
value-weighted index. The predictive regressions for the expected stock return in panel (b) are
R = α +β ln Dt, at horizon T (annual frequency). S.E. denotes the Newey-West standard errors
t→t+T T T Pt
with 8 lags. 95% CI denotes the 95% confidence interval of the estimated coefficients on the simulated
data. Each run in the simulation uses 72 years.
stock returns. We see that the model features a large “excess volatility”: the flow shocks (with their
2.8% annual standard deviation) account for almost 90% of the variance of stock returns. It may
be surprising that we can match the equity premium without any of the “modern” asset pricing
ingredients, such as a very high risk aversion or disaster risk. The reason is that the preferences of
our behavioral investors feature “narrow framing”, which leads to an average risk premium given by
π¯ = γσ2.
r
Table 7 shows more moments specific to the stock market. We broadly match the volatility of
the log P/D ratio, its speed of mean reversion, and the predictive power of forecasting regressions
with that P/D ratio.
We conclude that our general equilibrium model featuring inelastic markets is competitive with
other widely-used general equilibrium models that match equity market moments. Its main advan-
tages, as we see it, are that it relies on an observable force, flows in and out of equities and that it
matches our evidence on the macro elasticity of the market. Also, it retains the CRRA structure, so
it is easier to mesh with the basic macro models. Hence, it might be a useful prototype highlighting
how to think about inelastic market in general equilibrium.
6 Government Policy and Corporate Finance in Inelastic Mar-
kets
We now examine how a number of issues in finance change when markets are inelastic: government
and corporate policies. Many readers may wish to skip to the conclusion, but in our experience a
39

good fraction of readers will be interested in these topics.
6.1 Governments might stabilize the stock market via quantitative easing
in equities
In inelastic markets, the government might prop up asset values, perhaps in times of crisis, or to
help firms invest by raising equity at a high price. Indeed, suppose that the government buys fG
percent of the market, and keeps it forever. Then, the market’s valuation increases by p = fG.65 So,
ζ
if the government buys 1% of the market (which may represent roughly 1% of GDP), the market
goes up by 5%.66
This is what a number of central banks have done. In August 1998, the Hong Kong government,
whenitwasunderaspeculativeattack, bought6%oftheHongKongstockmarket: thisresultedina
24%abnormalreturn,whichwasnotreversedinthefollowingeightweeks(BhanotandKadapakkam
(2006)). This effect is not entirely well-identified, but is consistent with a large price impact
multiplier 1, around 4. Likewise, the Bank of Japan owned 5% of the Japanese stock market in
ζ
March 2018 (Charoenwong et al. (2020)) and the Chinese “national team” (a government outfit)
owned a similar 5% of Chinese stocks in early 2020.67 In inelastic markets, this may have a large
price impact.68 Those government purchases of equities offer a potentially attractive government
policy, as they increase market values and lower the cost of capital for firms, and relax credit
constraints. So, they might increase hiring and real investments by firms, and GDP. We think this
is an interesting direction for future research.69
6.2 Corporate finance in inelastic markets
Imagine that firms (the aggregate corporate sector) buy back shares in one period, reducing divi-
dends and hence keeping total payouts constant. What happens?
In a frictionless model, this does not affect the firms’ values, as per Modigliani-Miller. In an
inelastic model, it should now be clear that buybacks can increase the aggregate value of equities.
How much depends on the rationality of households, as we now detail. For clarity and brevity,
we focus on the two-period model (the same economics holds with an infinite horizon, but the
expressions are more complicated; see Section G.11). At time 0, we imagine the representative firm
buys back a fraction b of the equity shares, where b is small (so that the new number of shares is
Q(cid:48) = (1 b)Q ). The buyback is financed by a fall in the time-0 dividend, so the total dividend
pa 0 yout fa−lls fro 0 m to (cid:48) = P Q b, where P is the ex-dividend price, and P Q b is used to
finance the share bDu 0 ybacDk 0 . D 0 − 0 0 0 0 0
65Note that we assume that investors do not change their holdings to counteract the government’s holdings,
meaning that Ricardian equivalence does not hold, perhaps because of a form of inattention to the government’s
actions (Gabaix (2020)).
66If the government buys it for just T periods, the impact is p = 1 1 fG . Set f = fG1 in (20).
− (1+ρ)T ζ t 0≤t<T
With the above calibration, this can be a moderate dampening if T is(cid:16)large enoug(cid:17)h.
67Lockett, Hudson. “How the invisible hand of the state works in Chinese stocks.” Financial Times, 2/4/2020.
68We are not aware of a quantification of the macro elasticity for Japan. Barbon and Gianinazzi (2019) and
Charoenwong et al. (2020) quantity a micro elasticity – the differential impact on individual stocks that are owned
versus not owned by the government.
69Brunnermeier et al. (2020) caution about potentially adverse effect if the government’s purchases might become
too central.
40

We need to take a stance on the households’ reaction to those buybacks. Call µD (respectively
µG) the fraction of the change in dividends (respectively, of the change in capital gain) that is
“absorbed” by the households – that is, consumed or reinvested in the pure bond fund. If the extra
dividend (respectively extra capital gain) is X dollars, consumers will “remove from the mixed fund”
µDX (respectivelyµGX)dollars. Ashouseholds’marginalpropensitytoconsumeishigheraftera$1
dividendratherthana$1capitalgain(Bakeretal.(2007)), itislikelythat0 < µG < µD < 1. Wedo
not seek here to endogenize µD and µG, which would be a good application of limited attention. We
simply trace their implications for the price impact of share buybacks in the following proposition
(which is proved in Section F).
Proposition 7. (Impact of share buybacks in a two-period model) Suppose that, at time 0, corpo-
rations buy back a fraction b of shares, lowering their dividend payments by the corresponding dollar
amount, hence keeping total payout constant at time 0. Then, the aggregate value of equities moves
by a fraction
µD µG θ
v = − b, (56)
ζ +µGθ
(cid:0) (cid:1)
where µD (respectively µG) is the fraction of the change in dividends (respectively change in capital
gains) “absorbed” by households, i.e. removed from the mixed fund. If µD > µG (so that the marginal
propensity to consume out of dividends is higher than that out of capital gains), then share buybacks
increase the aggregate market value: v > 0.
A provisional calibration Using the estimates of Di Maggio et al. (2020b), we set µD
0.5 and µG 0.03. Then, (56) says that a buyback of 1% of the market increases the marke(cid:39)t
capitalization(cid:39)by 2.2%. The above papers (Baker et al. (2007); Di Maggio et al. (2020b)) do not
exactly measure µD and µG: they measure the impact on consumption, not on consumption plus
reallocation to pure bond funds. It is conceivable that some of the capital gains or dividends are
reinvested in bonds, even if they’re not consumed. So, µD (respectively µG) is likely to be higher
than the marginal propensity to consume out of dividends (respectively capital gains). In addition,
what matters is the “long run” propensity, which is hard to measure, and one may conjecture that
the long-run consumption adjustment to a lasting policy change will have µD µG closer to 0.
One upshot is that it would be interesting for the empirical literature to estimate−the long-run µD
and µG, as it is important to understand the impact of firms’ actions such as buybacks in inelastic
markets.
7 Conclusion
This paper finds, both theoretically and empirically, that the aggregate stock market is surprisingly
price-inelastic, so that flows in and out of the market have a significant impact on prices and risk
premia. We refer to this as the inelastic markets hypothesis. We provide tools to analyze inelastic
markets, with a simple model featuring key elasticities and an identification strategy using the
recently developed method of granular instrumental variables, conceived for this project and laid
out in detail in Gabaix and Koijen (2020).
We emphasize though that the “inelastic market hypothesis” remains just that: a hypothesis.
Our empirical analysis relies on a new empirical methodology and on fairly unexplored data in this
41

context. An important takeaway from this paper is that the demand elasticity of the aggregate
stock market is a key parameter of interest in asset pricing and macro-finance, just like investors’
risk aversion, their elasticity of inter-temporal substitution, and the micro elasticity of demand. We
provide a first estimate, and we hope that future research will explore other identification strategies
to improve and sharpen this estimate.
If the inelastic markets hypothesis is correct, it invalidates or qualifies a number of common
views in finance and it provides new directions to answer longstanding questions in finance. We
outline and then discuss those tenets.
How tenets of finance change if the inelastic markets hypothesis is correct
“Permanent price impact must reflect information.” In Proposition 5, a one-time, non mean-
reverting inflow permanently changes prices (as in p = f), even if it contains no information
ζ
whatsoever. This is because a permanent change in the demand for equities must permanently
change their equilibrium prices – and this effect is quantitatively important in inelastic markets.
Thetypicalempiricalstrategytolookforreversalsassignsofflows(ratherthaninformation)moving
prices does not work in this case. By the same logic, we can see large changes in prices but small
changes in long-horizon expected returns.
“Fast and smart investors (perhaps hedge funds) will provide enough elasticity to the market.”
This is not true: in part because hedge funds are small (they own less than 5% of the market,
see Section 2), they cannot provide much elasticity for the market as a whole (so ζ remains low),
even though they might ensure short term news are incorporated quickly (so that κ is quite high).
In addition, those smart-money investors often face risk constraints and outflows that limit their
ability to aggressively step in during aggregate downturns.
“Trading volume is very high, so the equity market must be very elastic.” Trading volume in the
equity market is high (about 100% of the value of the market each year), but most of it exchanges
one share for another share (perhaps via a round-trip through cash). These trades within the
universe of equities do no count toward the aggregate flow f, which is a (signed) flow from bonds
to equities.
“For every buyer there is a seller; so, saying ‘there was an increase in the demand for equities’
is meaningless.” Economists often appeal to the truism that “for every buyer there is a seller” to
disregard the notion that a measurable increase in the willingness of the average trader to buy
more of the market will push prices up (“buying pressure”). Our model clarifies that this reasoning
is incorrect. In Proposition 2, f is the pressure to buy stocks (if it is positive), and the demand
q = ζp + f has a component ζp expressing that “sellers” appetite to sell shares to “buyers”
repre−sented by f. So there are bo−th buyers and sellers (or really, a force making the representative
fund buy, and a force making it sell), but at the same time, buying pressure f does move the price
by p = f. Moreover, it is directly measurable via the change in asset holdings (bonds in the case of
ζ
the undergraduate example of Section 3.1), as in (10).
“The market often looks impressively efficient in the short run, so it must be quite macro-
efficient.” The contrast between the market’s “short run efficiency” and “macro-efficiency” is sharp
in equation (20): future events are discounted at a rate ρ = ζ = δ + 1−θ, so that a highly far-
κ κ
sighted market has a lower value of ρ. So, the market can be very forward-looking (low ρ), even if
it is very macro-inelastic (low ζ), provided that “far-sightedness” κ is relatively high compared to
ζ (for example, because there are a few powerfully forward-looking arbitrageurs). As an example,
consider the announcement of an event that will take effect in a week, such as a permanent increase
42

in dividends or inflows. In our calibration, the market’s current reaction to the announcement is a
fraction 99.8% of the eventual present value of the future dividends or inflows.70 In that sense, the
market looks impressively efficient. But again, it is “short-term predictability efficient” (it smooths
announcements) and “micro efficient” (it processes well the relative valuations of stocks), but it is
not “macro efficient” (as Samuelson (1998) put it) or “long-term predictability efficient” – it does
not absorb well very persistent shocks. Furthermore, even though prices respond promptly around
major events, it is generally hard to assess whether the market moved by just the right amount,
or instead under- or over-reacted. In addition to a large literature demonstrating drifts in prices
before and after macro events (such as Federal Open Market Committee meetings), our model
implies that persistent flows around such events can lead to persistent deviations in prices, and
typical event study graphs that do not display much of a drift in prices following the event would
be uninformative about macro efficiency.
“Share buybacks do not affect equity returns, as proved by the Modigliani-Miller theorem.” In
the traditional frictionless model, the return impact of a share buyback should be zero. However,
in our model, if firms in the aggregate buy back $1 worth of equity, that can increase aggregate
valuations (Section 6.2 detailed this). Hence, share buybacks are potentially a source of fluctuations
in the market. In our model, a combination of fund mandates and consumers’ bounded rationality
leads to a violation of the Modigliani-Miller neutrality. More broadly, corporate actions such as
share issuances, transactions by insiders, et cetera, may have a large impact on prices beyond any
informational channel. Most extant empirical evidence focuses on announcements at the firm level,
while we emphasize their impact at the aggregate level. By focusing on well-identified firm-level
responses, one identifies the micro-elasticity, not the macro elasticity ζ. It will be interesting to
explore in detail how important corporate decisions are for fluctuations in the aggregate stock
market.
“Markets must be macro elastic as otherwise small flows would imply large price changes and
market timing strategies would be too profitable.” The Sharpe ratios of market timing strategies
depend on the properties of flows, see (23) and (24). If flows are highly persistent, prices may move
a lot, but the per-period expected excess returns do not change much. Indeed, in the model in
Section 5, the persistence of the dividend yield matches its empirical counterpart and using it for
market-timing purposes does not work well out of sample.
We next discuss a few questions that seem important for future research.
Why is the aggregate demand for equities so inelastic? The core of the inelastic markets
hypothesis is that the macro demand elasticity ζ is low. Why is it so low? We highlighted two
reasons, namely fixed-share mandates (so that ζ > 0, κ = 0), such as those of many funds that
are 100% in equities and hence have zero elasticity, and inertia (i.e., some funds or people are just
buy-and-hold, creating ζ = κ = 0). This may be due to a taste for simplicity, or to agency frictions:
as the household is not sure about the quality of the manager, a simple scheme like a constant share
in equities may be sensible – otherwise the manager may take foolish risks.
There are other possibilities. If some funds have a Value-at-Risk constraint, and volatility
goes up a lot in bad times, they need to sell when the markets fall, so that their ζ and κ are
negative. A different possibility is that when prices move, people’s subjective perception of the
equity premium does not move much. One reason might be that investors think the rest of the
market is well-informed. Also, going from market prices to the equity premium is a statistically
70Indeed, (1+ρ) −T =99.8%, taking the ρ calibrated in Section 3.2 and T =1/52 years.
43

error-prone procedure, so that market participants may shrink towards no reaction to this (Black
(1986), Summers (1986)). Alternatively, many investors may not place much weight on the price-
earnings ratio as a reliable forecasting tool, perhaps because they want parsimonious models and
price-dividend ratios are not that useful as short-run forecasters, or because many investors just
do not wish to bother paying attention to them (Gabaix (2014), Chinco and Fos (2019)). The
pass-through between subjective beliefs and actions might be low, as it is for retail investors (Giglio
et al. (2021a)). Finally, demand may respond little to prices because demand shocks are highly
persistent.71 In the end, while identifying the exact reasons for low market elasticity is interesting,
thisquestionhasalargenumberofplausibleanswers. Fortunately,itispossibletowriteaframework
in a way that is relatively independent to the exact source of low elasticity, and this is the path we
chose.
What are the determinants of flows? It is clear that it would be desirable to know more
about the determinants of flows at a high frequency. We provided a minimalist model with a
“behavioral disturbance” (which was enough to study its general equilibrium impact), and some
simple correlations in Section 4.4, but this is clearly a first pass. Establishing the various channels
of flows could be a whole line of enquiry, perhaps with micro data such as those used by Calvet et
al. (2009) or Giglio et al. (2021a).
Toappreciatetherichnessofthosedeterminants, letusobservethatflowshockscouldcomefrom
various sources, such as: (i) changes in beliefs about future flows or fundamentals, as these both
affect expected returns, per Proposition 5; (ii) “liquidity needs”, for instance insurance companies
selling stocks after a hurricane; (iii) more generally, heterogeneous income or wealth shocks to
different groups (including foreign versus domestic investors) changing the effective propensity to
invest in stocks by the average investor; (iv) corporate actions by firms such as decisions to buy
back or issue shares; (v) shocks to substitute assets, which might for example prompt investors to
rebalance towards stocks when bond yields go down; (vi) changes in the advertising or advice by
institutional advisers, as explored in Ben-David et al. (2020b); (vii) “road shows” in which firms
or governments try to convince potential investors to buy into a prospective equity offering or
privatization; (viii) mechanical forced trading via “delta hedging,” whereby traders who have sold
put options and continuously hedge them need to sell stocks when stock prices fall.
Some further outstanding questions In addition to the two questions we just discussed, our
framework makes a number of further issues interesting and researchable. For example, how much
can and should governments intervene in equity markets? Do share buybacks account for a large
share of market fluctuations? How forward-looking are the policies of funds (κ)? Generalizing,
what are the cross-market elasticities, meaning the forces that create “contagion” across market?
These same effects will also generalize to other markets (such as the markets for corporate bonds
71Forinstance,imagineaverysimplemodelf = F I t τ0,τ1 ,whereF isconstant, τ0,τ1 theperiodof
t k k ∈ k k k k k
timethataflowsstaysinthemarket,andτ1 τ0 exp(λ).Fromaninstitutionalperspective,onecanalsoimagine
k− k ∼(cid:80) (cid:0) (cid:2) (cid:3)(cid:1) (cid:2) (cid:3)
that a large asset manager launches a fund that attracts capital, and that this capital is sticky, but the period for
which it stays is unclear. If λ is low, then prices will respond sharply to the flow, even though the expected return
does not move much. Uncertainty about the persistence of the demand shock introduces uncertainty about how
the price change maps to expected returns, leading to a muted response and a low ζ. This model is in quite sharp
contrast with the traditional view in which flows have a temporary price impact (for instance Coval and Stafford
(2007)).
44

and currencies): if so, how and what are the policy implications? This is a rich number of questions
that hopefully economists will be able to answer in the coming years.
A Appendix: Main proofs
Proof of Proposition 2 At time 0−, before the inflow shocks, fund i’s wealth is W ¯ = P ¯ Q ¯ +B ¯,
i i
where P ¯ Q ¯ and B ¯ are respectively the fund’s holdings of equities and bonds:
i i
¯ ¯ ¯ ¯ ¯
PQ = θ W , B = (1 θ )W .
i i i i i i
−
At time 0, after the inflow shock, and the change in the equilibrium price to P, the fund’s wealth
is W = PQ ¯ + B ¯ + ∆F , so that ∆W = (∆P)Q ¯ + ∆F . So, the value of the assets in the fund
i i i i i i i
changes by a fraction:
¯ ¯ ¯
∆W Q ∆P ∆F PQ ∆P
w := i = i + i = i +f = θ p+f ,
i ¯ ¯ ¯ ¯ ¯ i i i
W W W W × P ×
i i i i
that is:
w = θ p+f . (57)
i i i
This means that the value of the fund increases via the inflow of f , and via the appreciation of the
i
stock p, to which the fund has an exposure θ .
i
Let us first take the case κ = 0. The demand (1) is:
i
¯
θ W θ W (1+w ) 1+w
i i i i i ¯ i
Q = = = Q ,
i P P ¯ (1+p) i 1+p
so that the fractional change in the fund’s demand for shares is:
Q w p θ p+f p f ζ p
i i i i i i
q = 1 = − = − = − ,
i Q ¯ − 1+p 1+p 1+p
i
with ζ = 1 θ . We see how ζ is the (signed) demand elasticity, which includes crucial income
i i i
effects.72 Fo−r small price chan−ges, this gives q f ζp . We also see that, when κ = 0 for all
i i i i
funds, the equilibrium condition qD = 0 leads to(cid:39) p = − fS exactly.
Next, consider the case with a
S
general κ . Taking
ζSlogs
and then deviations from the baseline
i
D/P ratio gives:
De
∆ln = ∆lnDe ∆lnP = d p.
P − −
On the other hand, as δ = De = 1+r +π, we have ∆ln De = ∆π = δπˆ (with πˆ = ∆π), so that:
P f P 1+r f+π
πˆ = δ(d p). (58)
−
72This is the compensated or Hicksian elasticity of demand: indeed, after the price change, the fund can purchase
itsoldholdings(whichisthefoundationoftheHicksiandemand),simplybecauseitalreadyownsthem). Controlling
forfundwealth,thedemandelasticityis 1. Butgivenfundwealthhasanelasticityθ totheprice,thetotaldemand
−
elasticity ( ζ) is 1+θ.
− −
45

We take logs in (1), so that lnQ = lnW + lnθ lnP + κ πˆ. Given that initially lnQ ¯ =
i i i i i i
lnW ¯ +lnθ lnP ¯, taking differences we have ∆lnQ = − ∆lnW ∆lnP +κ πˆ. Finally, we use the
i i i i i
Taylor expan−sion ∆lnW w and ∆lnP p to yield: −
i i
(cid:39) (cid:39)
q = w p+κ πˆ. (59)
i i i
−
Using (57), we obtain (7):
q = (1 θ )p+f +κ δ(d p) = (1 θ +κ δ)p+f +κ δd.
i i i i i i i i
− − − − −
Proof of Proposition 4 We call F the cumulative inflow into the mixed fund, normalizing F to
t 0
be the mixed fund’s initial endowment of bonds. Then, as all dividend and bond coupon are given
to the consumer, W = P Q+F , and in the baseline economy W ¯ = P ¯ Q+F ¯. We call F ˜ := F F ¯
t t t t t t t t t
thedeviationofthedollarflowsfromthebaseline. Subtracting, wehaveW W ¯ = P P ¯ Q+ − F ˜,
t t t t t
− −
i.e. W ¯ w = P ¯ Qp +F ˜, so with f = F˜ t ,
t t t t t t W¯
t
(cid:0) (cid:1)
w = θp +f . (60)
t t t
Now, from the demand for stocks, we have Q P = W θeκπˆt+νt , while in the baseline economy
t t t
Q ¯ P ¯ = W ¯ θ. Dividing through, we get: QtPt = Wteκπˆt+νt , so that (1+q )(1+p ) = (1+w )eκπˆt+νt.
t t t Q¯ tP¯
t
W¯
t
t t t
Linearizing, q +p = w +κπˆ +ν . Hence, by (60),
t t t t t
q = (1 θ)p +κπˆ +f +ν . (61)
t t t t t
− −
Finally, using πˆ = δ(de p ) + E [∆p ] (see (18)), we obtain q = (1 θ+κδ)p + κδde +
κE [∆p ]+f t +ν . t − t t t+1 t − − t t
t t+1 t t
Proof of Proposition 5 Equation (19) can be rewritten as q = κ(E ∆p ρp +δde)+f +ν .
As q = 0, this is also: t t t+1 − t t t t
t
f +ν
E ∆p ρp +δde + t t = 0. (62)
t t+1 − t t κ
Defining z := δde + ft+νt, this gives p = E tpt+1+zt, so that p = E ∞ zτ . The equity
t t κ t 1+ρ t t τ≥t (1+ρ)τ−t+1
premium comes from (61) with q = 0.
t (cid:80)
B Appendix: Identification methodology
We summarize the algorithms that we use to estimate the multipliers and elasticities in Section
4.2 and the multipliers in Section 4.3. The algorithms are the same, with some minor adjustments
given the unique features of either the FoF data or 13F data.
B.1 Algorithm used for sector-level data
We summarize the algorithm that we use for the Flow of Funds (FoF) data in Section 4.2.
46

1. We construct pseudo-equal value weights E ˜ , where we start from E ˜σ = σ i −2 , where
i,t−1 i (cid:80)N σ−2
k=1 k
σ = σ(∆q ), and define E ˜ = min ξE ˜σ, 1.5 , where ξ 1 is tuned so that E ˜ = 1. We
i it i i N ≥ i i
exclude the corporate sector in constructing the instrument. This winsorizes the quasi-equal
(cid:110) (cid:111)
(cid:80)
weights to be at most 50% higher than strict equal weights. This adjustment ensures that the
equal weights are not too concentrated for sectors with very stable ∆q .73 This is relevant
it
when the number of sectors is small, as is the case for the FoF.
2. We run the panel regression
∆q = α +β +γ ∆y +δ t+∆qˇ , (63)
it i t i t i it
using E ˜ as regression weights, and construct the ∆qˇ as the residuals. Here ∆y is quarterly
it t
real GDP growth and we allow for a time trend as some sectors grew substantially faster in,
for instance, the nineties than in the subsequent period.
3. We extract the principal components of E ˜ 2 1 ∆qˇ and denote the estimated vector of principal
i it
components by ηPC,e.
t
4. We construct the GIV instrument:74
N
Z = S ∆qˇ . (64)
t i,t−1 it
i=1
(cid:88)
5. We estimate the multiplier, M, using the time-series regression
∆p = α+MZ +λ(cid:48) ηe +e , (65)
t t P t t
where ηe = ∆y ,ηPC,e . This regression is also the first stage to estimate the elasticities.
t t t
Instrumentin (cid:16) g ∆p t by Z(cid:17)t in both cases, we estimate the demand elasticity via
∆q = α ζ∆p +λ(cid:48) ηe +e , (66)
Et E − t E t t
and the supply elasticity via
∆q = α ζ ∆p +λ(cid:48) ηe +e . (67)
Ct C − C t C t t
73Quasi-equal weights E˜ are preferable to equal weights E = 1 as they add precision — in the same way in
j j N
which to estimate a mean, weighing by inverse variance is better than equal weighing (Gabaix and Koijen (2020)).
The primary objective of inverse variance weighing is to downplay the importance of very volatile sectors that may
distort the estimation of the common factors. If the inverse variance weights get too concentrated as some sectors
are very stable, the same concern applies, and we therefore winsorize the weights at 1.5. While 50% is somewhat
N
arbitrary, it is a significant departure from equal weights. We also explore the sensitivity of our results to this cutoff
in Section D.4, and find them to be robust.
74An equivalent way to proceed is to use z = N S uˇ , where uˇ is the measure of idiosyncratic shock
t i=1 i,t−1 it it
commonfromstep4. Thisway,z ismadeofidiosyncraticshocks. AswecontrolforηPC,e below,thetwoprocedures
t (cid:80) t
are similar.
47

B.2 Algorithm used for investor-level data
We summarize the algorithm that we use to extract factors, η , in Section 4.3.
t
1. We run the panel regression
∆q = a +b ∆y +c +η x +η x +∆qˇ ,
it i i t t 1t 1i,t−1 2t 2i,t−1 it
where ∆y is GDP growth, a is an investor fixed effect, c is a time fixed effect, x is
t i t 1i,t−1
lagged size, and x lagged active share. We collect the residuals, ∆qˇ .
2i,t−1 it
2. We compute the time-series standard deviation of ∆qˇ by investor. In each quarter, we sort
it
investors into 20 groups based on this standard deviation. Intuitively, funds with different
volatilities of ∆qˇ are likely to have different exposures to the factors. By group and quarter,
it
we average ∆qˇ , ∆qˇE, where g indexes the groups.
it gt
3. We extract principal components based on the panel of 20 groups of ∆qˇE.
gt
References
Amiti, Mary and David E Weinstein, “How much do idiosyncratic bank shocks affect investment? Evidence
from matched bank-firm loan data,” Journal of Political Economy, 2018, 126 (2), 525–587.
Bacchetta, Philippe and Eric Van Wincoop,“Infrequentportfoliodecisions: Asolutiontotheforwarddiscount
puzzle,” American Economic Review, 2010, 100 (3), 870–904.
Baker, Malcolm and Jeffrey Wurgler, “A catering theory of dividends,” The Journal of Finance, 2004, 59 (3),
1125–1165.
Baker, Malcolm, Stefan Nagel, and Jeffrey Wurgler, “The Effect of Dividends on Consumption,” Brookings
Papers on Economic Activity, 2007, 38 (1), 231–292.
Bansal, Ravi and Amir Yaron, “Risks for the Long Run: A Potential Resolution of Asset Pricing Puzzles,”
Journal of Finance, 2004, 59 (4), 1481–1509.
Barberis, NicholasandAndreiShleifer,“Styleinvesting,” JournaloffinancialEconomics,2003,68(2),161–199.
Barberis, Nicholas, Ming Huang, and Richard H Thaler, “Individual preferences, monetary gambles, and
stock market participation: A case for narrow framing,” American economic review, 2006, 96 (4), 1069–1090.
Barbon, Andrea and Virginia Gianinazzi, “Quantitative Easing and Equity Prices: Evidence from the ETF
Program of the Bank of Japan,” The Review of Asset Pricing Studies, 2019, 9 (2), 210–255.
Barro, Robert J,“Raredisastersandassetmarketsinthetwentiethcentury,” TheQuarterlyJournalofEconomics,
2006, 121 (3), 823–866.
Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, “Hedge fund stock trading in the financial
crisis of 2007–2009,” The Review of Financial Studies, 2012, 25 (1), 1–54.
Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, “Do ETFs Increase Volatility?,” The Journal
of Finance, 2018, 73 (6), 2471–2535.
Ben-David, Itzhak, Francesco Franzoni, Rabih Moussawi, and John Sedunov, “The granular nature of
large institutional investors,” Management Science, forthcoming.
48

Ben-David, Itzhak, JiacuiLi, AndreaRossi, andYangSong,“Non-FundamentalDemandandStyleReturns,”
2020. Working Paper.
Ben-David, Itzhak, Jiacui Li, Andrea Rossi, and Yang Song, “Style Investing, Positive Feedback Loops, and
Asset Pricing Factors,” Working Paper, 2020.
Ben-Rephael, Azi, Shmuel Kandel, and Avi Wohl, “Measuring investor sentiment with mutual fund flows,”
Journal of Financial Economics, 2012, 104 (2), 363–382. Special Issue on Investor Sentiment.
Bhanot, Karan and Palani-Rajan Kadapakkam,“Anatomyofagovernmentinterventioninindexstocks: Price
pressure or information effects?,” The Journal of Business, 2006, 79 (2), 963–986.
Black, Fischer, “Noise,” The Journal of Finance, 1986, 41 (3), 528–543.
Bordalo, Pedro, Nicola Gennaioli, Rafael La Porta, and Andrei Shleifer, “Expectations of Fundamentals
and Stock Market Puzzles,” Technical Report, National Bureau of Economic Research 2020.
Bouchaud, Jean-Philippe, Julius Bonart, Jonathan Donier, and Martin Gould,Trades, quotes and prices:
financial markets under the microscope, Cambridge University Press, 2018.
Brainard, William C. and James Tobin, “Pitfalls in Financial Model Building,” American Economic Review:
Papers and Proceedings, 1968, 58 (2), 99–122.
Brunnermeier, Markus K. and Stefan Nagel, “Hedge Funds and the Technology Bubble,” The Journal of
Finance, 2004, 59, 2013–2040.
Brunnermeier,MarkusK,MichaelSockin,andWeiXiong,“China’smodelofmanagingthefinancialsystem,”
Technical Report, National Bureau of Economic Research 2020.
Buffa, Andrea M, Dimitri Vayanos, and Paul Woolley,“Assetmanagementcontractsandequilibriumprices,”
Technical Report, National Bureau of Economic Research 2019.
Caballero, Ricardo J and Alp Simsek, “A risk-centric model of demand recessions and speculation,” The Quar-
terly Journal of Economics, 2019.
Calvet, Laurent E., John Y. Campbell, and Paolo Sodini, “Fight Or Flight? Portfolio Rebalancing by
Individual Investors,” Quarterly Journal of Economics, 2009, 124 (1), 301–348.
Camanho, Nelson, Harald Hau, and Hélène Rey, “Global portfolio rebalancing and exchange rates,” Working
Paper, 2019.
Campbell, John Y. and John H. Cochrane, “By Force of Habit: A Consumption-Based Explanation of Aggre-
gate Stock Market Behavior,” Journal of Political Economy, 1999, 107 (2), 205–251.
Carvalho, Vasco M and Basile Grassi, “Large firm dynamics and the business cycle,” American Economic
Review, 2019, 109 (4), 1375–1425.
Chang, Yen-Cheng, Harrison Hong, and Inessa Liskovich, “RegressionDiscontinuityandthePriceEffectsof
Stock Market Indexing,” Review of Financial Studies, 2014, 28 (1), 212–246.
Charoenwong, Ben, Randall Morck, and Yupana Wiwattanakantang, “Bank of Japan Equity Purchases:
The Final Frontier in Extreme Quantitative Easing,” April 2020. NBER Working Paper 25525.
Chien, YiLi, Harold Cole, and Hanno Lustig, “Is the volatility of the market price of risk due to intermittent
portfolio rebalancing?,” American Economic Review, 2012, 102 (6), 2859–96.
Chinco, Alexander and Vyacheslav Fos, “The sound of many funds rebalancing,” 2019.
Cochrane, John H., “Presidential Address: Discount Rates,” The Journal of Finance, 2011, 66 (4), 1047–1108.
49

Cole, Allison, Jonathan Parker, and Antoinette Schoar, “Household Portfolios and Retirement Saving Over
the Life Cycle,” 2021. Working Paper, MIT Sloan.
Coval, Joshua and Erik Stafford, “Asset fire sales (and purchases) in equity markets,” Journal of Financial
Economics, 2007, 86 (2), 479–512.
Cutler, David M, James M Poterba, and Lawrence H Summers, “Speculative Dynamics And The Role Of
Feedback Traders,” The American Economic Review Papers and Proceedings, 1990, 80 (2), 63–68.
Da, Zhi, Borja Larrain, Clemens Sialm, and Jose Tessada, “Destabilizing Financial Advice: Evidence from
Pension Fund Reallocations,” Review of Financial Studies, 2018, 31 (10), 3720–3755.
De Long, J. Bradford, Andrei Shleifer, Lawrence H. Summers, and Robert J. Waldmann,“NoiseTrader
Risk in Financial Markets,” Journal of Political Economy, 1990, 98 (4), 703–738.
Deuskar, Prachi and Timothy C. Johnson, “Market Liquidity and Flow-driven Risk,” The Review of Financial
Studies, 2011, 24 (3), 721–752.
Di Giovanni, Julian and Andrei A Levchenko, “Country size, international trade, and aggregate fluctuations
in granular economies,” Journal of Political Economy, 2012, 120 (6), 1083–1132.
Di Maggio, Marco, Amir Kermani, and Kaveh Majlesi, “Stock Market Returns and Consumption,” Journal
of Finance, 2020, 75 (6), 3175–3219.
Dierker, Martin, Jung-Wook Kim, Jason Lee, and Randall Morck, “Investors’ Interacting Demand and
Supply Curves for Common Stocks,” Review of Finance, 2016, 20 (4), 1517–1547.
Dong, Xi, Namho Kang, and Joel Peress, “How the Speed of Capital Affects Factor Momentum, Reversal and
Volatility?,” Available at SSRN, 2021.
Dou, Winston, Leonid Kogan, and Wei Wu, “Common Fund Flows: Flow Hedging and Factor Pricing,”
Available at SSRN, 2020.
Duffie, Darrell,“PresidentialAddress: AssetPriceDynamicswithSlow-MovingCapital,” JournalofFinance,2010,
65 (4), 1237–1267.
Duffie, Darrell and Bruno Strulovici, “Capital mobility and asset pricing,” Econometrica, 2012, 80 (6), 2469–
2509.
Edelen, Roger M and Jerold B Warner, “Aggregate price effects of institutional trading: a study of mutual
fund flow and market returns,” Journal of Financial Economics, 2001, 59 (2), 195–220.
Farmer, Roger, Expectations, employment and prices, Oxford University Press, 2010.
Frazzini,AndreaandOwenALamont,“Dumbmoney: Mutualfundflowsandthecross-sectionofstockreturns,”
Journal of Financial Economics, 2008, 88 (2), 299–322.
Frazzini, Andrea, Ronen Israel, and Tobias J Moskowitz, “Trading costs,” Working Paper, 2018.
Friedman, Benjamin M., “Financial Flow Variables and the Short-Run Determination of Long-Term Interest
Rates,” Journal of Political Economy, 1977, 85 (4), 661–689.
Gabaix, Xavier, “The granular origins of aggregate fluctuations,” Econometrica, 2011, 79 (3), 733–772.
Gabaix, Xavier, “Variable rare disasters: An exactly solved framework for ten puzzles in macro-finance,” The
Quarterly journal of economics, 2012, 127 (2), 645–700.
Gabaix, Xavier, “A sparsity-based model of bounded rationality,” The Quarterly Journal of Economics, 2014, 129
(4), 1661–1710.
50

Gabaix, Xavier, “Behavioral Inattention,” Handbook of Behavioral Economics, 2019, 2, 261–344.
Gabaix, Xavier, “A behavioral New Keynesian model,” American Economic Review, 2020, 110 (8), 2271–2327.
Gabaix, Xavier and Matteo Maggiori, “International liquidity and exchange rate dynamics,” The Quarterly
Journal of Economics, 2015, 130 (3), 1369–1420.
Gabaix, XavierandRalphSJKoijen,“Granularinstrumentalvariables,” WorkingPaper28204,NationalBureau
of Economic Research December 2020.
Gabaix, Xavier, Arvind Krishnamurthy, and Olivier Vigneron, “Limits of arbitrage: theory and evidence
from the mortgage-backed securities market,” The Journal of Finance, 2007, 62 (2), 557–595.
Galaasen, S, R Jamilov, R Juelsrud, and H Rey, “Granular credit risk,” Technical Report, Working paper
2020.
Garleanu,Nicolae,LasseHejePedersen,andAllenM.Poteshman,“Demand-BasedOptionPricing,” Review
of Financial Studies, 2009, 22 (10), 4259–4299.
Ghysels, Eric, Hanwei Liu, and Steve Raymond, “Institutional Investors and Granularity in Equity Markets,”
2021. Working Paper.
Giglio, Stefano, Matteo Maggiori, Johannes Stroebel, and Stephen Utkus, “Five Facts About Beliefs and
Portfolios,” American Economic Review, 2021, 111 (5), 1481–1522.
Goetzmann, William N. and Massimo Massa, “Index Funds and Stock Market Growth,” The Journal of
Business, 2003, 76 (1), 1–28.
Gourinchas, Pierre-Olivier, Walker Ray, and Dimitri Vayanos, “A preferred-habitat model of term premia
and currency risk,” Working Paper, 2020.
Greenwood, Robin and Andrei Shleifer, “Expectationsofreturnsandexpectedreturns,” The Review of Finan-
cial Studies, 2014, 27 (3), 714–746.
Greenwood, Robin and Dimitri Vayanos, “Bond Supply and Excess Bond Returns,” The Review of Financial
Studies, 2014, 27 (3), 663–713.
Greenwood,RobinandSamuelGHanson,“Issuerqualityandcorporatebondreturns,” TheReviewofFinancial
Studies, 2013, 26 (6), 1483–1525.
Greenwood, Robin, Samuel G Hanson, Jeremy C Stein, and Adi Sunderam, “A quantity-driven theory of
term premiums and exchange rates,” Working Paper, 2019.
Hamilton, James D., “Why You Should Never Use the Hodrick-Prescott Filter,” The Review of Economics and
Statistics, 2018, 100 (5), 831–843.
Harris, Lawrence and Eitan Gurel, “Price and Volume Effects Associated with Changes in the S&P 500 List:
New Evidence for the Existence of Price Pressures,” Journal of Finance, 1986, 41 (4), 815–829.
He, Zhiguo and Arvind Krishnamurthy, “Intermediary Asset Pricing,” American Economic Review, 2013, 103
(2), 732–770.
Herskovic, Bernard, Bryan T Kelly, Hanno N Lustig, and Stijn Van Nieuwerburgh, “Firm volatility in
granular networks,” Journal of Political Economy, forthcoming.
Johnson, Timothy C, “Dynamic liquidity in endowment economies,” Journal of Financial Economics, 2006, 80
(3), 531–562.
51

Kahneman, Daniel and Dan Lovallo,“Timidchoicesandboldforecasts: Acognitiveperspectiveonrisktaking,”
Management science, 1993, 39 (1), 17–31.
Kekre, Rohan and Moritz Lenel, “Monetary policy, redistribution, and risk premia,” University of Chicago,
Becker Friedman Institute for Economics Working Paper, 2020, (2020-02).
Kendall, Maurice G, “Note on bias in the estimation of autocorrelation,” Biometrika, 1954, 41 (3-4), 403–404.
Koijen, Ralph SJ and Motohiro Yogo, “A demand system approach to asset pricing,” Journal of Political
Economy, 2019, 127 (4), 1475–1515.
Koijen, Ralph SJ and Motohiro Yogo, “Exchange Rates and Asset Prices in a Global Demand System,” 2020.
NBER Working Paper 27342.
Koijen, Ralph SJ, Robert J Richmond, and Motohiro Yogo, “Which investors matter for global equity
valuations and expected returns?,” Working Paper, 2019.
Koijen, Ralph SJ, Tobias J Moskowitz, Lasse Heje Pedersen, and Evert B Vrugt, “Carry,” Journal of
Financial Economics, 2018, 127 (2), 197–225.
Kondor, Péter and Dimitri Vayanos, “Liquidity risk and the dynamics of arbitrage capital,” The Journal of
Finance, 2019, 74 (3), 1139–1173.
Kyle, Albert S., “Continuous Auctions and Insider Trading,” Econometrica, 1985, 53 (6), 1315–1335.
Li, Jennifer, Neil D. Pearson, and Qi Zhang, “Impact of Demand Shocks on the Stock Market: Evidence from
Chinese IPOs,” 2020. Working Paper.
Li, Jiacui, “Slow-moving liquidity provision and flow-driven common factors in stock returns,” Available at SSRN
2909960, 2018.
Li, Jiacui, “What Drives the Size and Value Factors?,” 2021. Working Paper, University of Utah.
Lou, Dong, “A Flow-Based Explanation for Return Predictability,” The Review of Financial Studies, 12 2012, 25
(12), 3457–3489.
Lucas, Robert E. Jr., “Asset Prices in an Exchange Economy,” Econometrica, 1978, 46 (6), 1429–1445.
Ma, Yueran,“NonfinancialFirmsasCross-MarketArbitrageurs,” The Journal of Finance,2019,74(6),3041–3087.
Martin, Ian, “What is the Expected Return on the Market?,” The Quarterly Journal of Economics, 2017, 132 (1),
367–433.
Mitchell, Mark, Lasse Heje Pedersen, and Todd Pulvino,“Slowmovingcapital,” American Economic Review
Papers and Proceedings, 2007, 97 (2), 215–220.
Moreira, Alan, “Capital immobility and the reach for yield,” Journal of Economic Theory, 2019, 183, 907–951.
Newey, Whitney K. and Kenneth D. West, “Automatic Lag Selection in Covariance Matrix Estimation,” The
Review of Economic Studies, 10 1994, 61 (4), 631–653.
Parker, Jonathan A, Antoinette Schoar, and Yang Sun, “Retail Financial Innovation and Stock Market
Dynamics: The Case of Target Date Funds,” Working Paper, 2020.
Pavlova, Anna and Taisiya Sikorskaya, “Benchmarking Intensity,” Working Paper, 2020.
Peng, Cameron and Chen Wang, “Factor demand and factor returns,” Working Paper, 2021.
52

Petajisto, Antti,“Whydodemandcurvesforstocksslopedown?,” Journal of Financial and Quantitative Analysis,
2009, 44 (5), 1013–1044.
Rigobon, Roberto, “Identification through Heteroskedasticity,” The Review of Economics and Statistics, 2003, 85
(4), 777–792.
Samuelson, Paul A, “Summing up on business cycles: opening address,” Conference Proceedings of the Federal
Reserve Bank of Boston, 1998, 42, 33–36.
Schmickler,Simon,“IdentifyingthePriceImpactofFireSalesUsingHigh-FrequencySurpriseMutualFundFlows,”
Working Paper, 2020.
Shiller, Robert,“Stockpricesandsocialdynamics,” Brookingspapersoneconomicactivity,1984,1984(2),457–510.
Shleifer, Andrei, “Do Demand Curves for Stocks Slope Down?,” Journal of Finance, 1986, 41 (3), 579–590.
Shleifer, Andrei, “Inefficient markets: An introduction to behavioural finance,” Oxford University Press, 2000.
Summers, Lawrence H, “Does the stock market rationally reflect fundamental values?,” The Journal of Finance,
1986, 41 (3), 591–601.
Tobin, James,“Monetarypolicy: recenttheoryandpractice,” in“CurrentIssuesinMonetaryEconomics,” Springer,
1998, pp. 13–21.
Vayanos,DimitriandJean-LucVila,“Apreferred-habitatmodelofthetermstructureofinterestrates,” Working
Paper, 2020.
Vayanos, Dimitri and Paul Woolley,“AnInstitutionalTheoryofMomentumandReversal,” ReviewofFinancial
Studies, 2013, 26 (5), 1087–1145.
Wachter, Jessica A, “Can time-varying risk of rare disasters explain aggregate stock market volatility?,” The
Journal of Finance, 2013, 68 (3), 987–1035.
Warther, Vincent A, “Aggregate mutual fund flows and security returns,” Journal of financial economics, 1995,
39 (2-3), 209–235.
Wurgler, Jeffrey and Ekaterina Zhuravskaya, “Does Arbitrage Flatten Demand Curves for Stocks?,” Journal
of Business, 2002, 75 (4), 583–608.
53
