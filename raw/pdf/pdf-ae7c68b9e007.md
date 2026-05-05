---
id: pdf-ae7c68b9e007
type: pdf
title: 8651_paper_YaE6zR98
url: ''
authors: []
ingested_at: '2026-04-29T16:11:20Z'
content_hash: sha256:8f8cfceb83ebbe7d526f85e328728823445f220d09e3f877ad983bfcb34cf1c2
source_path: raw/pdf/pdf-ae7c68b9e007.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 71
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/8651_paper_YaE6zR98.pdf
published_at: '2014'
---
Exploratory Trading
Adam D. Clark-Joseph∗
December 31, 2014
Abstract
To investigate how high-frequency traders (HFTs) can predict price-changes, I analyze
novel, comprehensive,account-labeledmessagerecordsfromtheE-miniS&P500futuresmar-
ket that allow me to identify and study HFTs’ individual behaviors. I model how an HFT
could actively learn about market conditions, by initiating small (cid:16)exploratory(cid:17) trades and ob-
serving other traders’ responses. Empirical tests of the model’s predictions provide evidence
thatHFTsintheE-miniusethistechniquetoidentifyperiodswhenpricesarelikelytochange.
These(cid:28)ndingsindicatethattheHFTs’superiorcapacitytopredictprice-changesinvolvesmore
than merely reacting to news faster than other traders. The empirical results also elucidate
other connections between high-frequency trading and speed.
JEL classi(cid:28)cation: G14; G19
Keywords: High-frequency trading; Learning; Market microstructure
∗Department of Finance, University of Illinois at Urbana-Champaign. E-mail: adcj@illinois.edu. I thank
Jonathan Brogaard, Eric Budish, Terrence Hendershott, Alp Simsek, and Jeremy Stein for their detailed sug-
gestionsanddiscussion. IalsothankseminarparticipantsatHarvard,UBCSauder,IndianaKelley,StanfordGSB,
Illinois, OSU Fisher, Dartmouth Tuck, Wharton, and NYU Stern for their useful feedback. I am particularly in-
debted to John Campbell and Andrei Shleifer for their invaluable advice and guidance. All remaining errors are
my own. I gratefully acknowledge the support of an NSF Graduate Research Fellowship. The views expressed in
this paper are my own and do not constitute an o(cid:30)cial position of the Commodity Futures Trading Commission,
its Commissioners, or sta(cid:27).
1

1 Introduction
High-frequency algorithmic traders are now responsible for almost half of the trading on (cid:28)nancial
exchanges. Analyzing modern markets requires not only characterizations of what high-frequency
traders(HFTs)do,butalsoexplanationsofhowandwhytheydothosethings. ManyHFTsmanage
to predict price-movements with unprecedented success, and understanding how HFTs accomplish
this feat is crucial for determining the economic mechanisms that underlie high-frequency trading
and its e(cid:27)ects. The standard assumption in the literature has been that HFTs can predict price-
movementsbecause(cid:22)andonlybecause(cid:22)theydigestandrespondtonewpublicinformationbefore
slower traders can do so. Although using new information sooner than other traders unquestion-
ably improves HFTs’ forecasting to some extent, the assumption that this sort of superior speed
is the only mechanism driving HFTs’ exceptional predictions is both strong and restrictive, and
this assumption’s validity has not been assessed empirically. Using novel data at the Commodity
Futures Trading Commission (CFTC) that enable me to analyze individual HFTs’ actions, I study
how HFTs in the E-mini S&P 500 futures market acquire superior information about imminent
price-changes. Speci(cid:28)cally, I investigate whether HFTs obtain any valuable private knowledge in
a way other than just reacting to public information the fastest, and I (cid:28)nd explicit evidence that
in fact they do.
I model a simple framework in which an HFT places small aggressive (i.e., marketable) or-
ders and actively learns about expected price-impact by observing the responses that these (cid:16)ex-
ploratory(cid:17) orders elicit. In the E-mini, as in many markets, aggressive order-(cid:29)ow exhibits strong
predictability at short horizons. However, front-running predictable orders is pro(cid:28)table only when
those orders have a su(cid:30)ciently large price-impact, and price-impact is too small on average for
indiscriminate front-running to be pro(cid:28)table. Through exploratory trading, the HFT gathers in-
formation that helps him to trade ahead of predictable orders at only those times when doing so
will be pro(cid:28)table.1 In general, the market activity following an arbitrary aggressive order often
doesn’t convey information about expected price-impact, because the activity is just a response to
the same stimulus that prompted the order rather than a true reaction caused by the order itself.
1Time-variation in price-impact is a robust empirical fact in the data, and my results neither depend upon
nor dictate the speci(cid:28)c interpretation of that variation. Section 1.3 discusses some of the related empirical and
theoretical literature.
2

The trader who placed the order can judge whether it causes the subsequent activity, but other
traders cannot, and the possibility that they are observing the uninformative scenario diminishes
how much they learn from the market activity. The HFT learns more from his exploratory order
than other traders can learn from it, simply because he alone knows why his exploratory order was
placed. By using exploratory trading, the HFT can leverage his seemingly inconsequential private
knowledge about why he placed a particular order to obtain signi(cid:28)cant private information that
helps him to predict price movements.
UsingtheuniqueCFTCdata, Itestthepredictionsoftheexploratorytradingmodelunderthe
conservative assumption that HFTs’ small aggressive orders all are exploratory in nature. There
are many reasons other than exploration for which HFTs might place small aggressive orders, so
treating all of those orders as exploratory dilutes the e(cid:27)ects from any truly exploratory orders and
therefore raises the bar for obtaining signi(cid:28)cant results. Nevertheless, consistent with the model’s
predictions, I (cid:28)nd that a simple measure of the market response to the last small aggressive order
by a given HFT helps to explain a signi(cid:28)cant component of that HFT’s earnings on subsequent,
larger aggressive orders, even after controlling for the market response to the last small aggressive
order placed by anyone. Also as predicted, after controlling for the market response to the last
small aggressive order by anyone, the market response to the HFT’s last small aggressive order
does not help to explain other traders’ earnings on their subsequent, larger aggressive orders. As
Section 1.2 explains in detail, although futures trades are typically thought of as just one segment
of some cross-market play (hedging, arbitrage, etc.), for the purposes of this paper, empirical
features of the E-mini and of the HFTs’ behavior make it meaningful to analyze HFTs’ earnings
in the E-mini market by itself.
In principle, the two results above could be consistent with the alternative hypothesis that
HFTs somehow possess long-lived private information about future prices and split up their orders
overtime(plausibleinthecontextindividualequities, ifperhapslesssoforindexfutures).2 Unlike
the exploratory trading theory, though, this informed-order-splitting story has the counter-factual
implication that the market response to an HFT’s small order will only help to explain the HFT’s
2TherecenttheoreticalmodelsbyMartinezandRosu(2103),andFoucaultetal. (2013),motivatethisalternative
hypothesis. Thesemodelsincludealong-lived(cid:16)forecasterror(cid:17) componentofinformation,inadditiontothestandard
in(cid:28)nitesimally lived component of information (called (cid:16)news(cid:17) in the models).
3

earnings on a subsequent large order when the two orders have the same sign (i.e., buy or sell).
Empirically, the market response to an HFT’s small order helps to explain the HFT’s earnings on
the larger order regardless of whether both orders have the same sign.
ContrarytotheprevailingassumptionthatHFTs’superiorinformationderivesexclusivelyfrom
superior reaction speed, the empirical evidence in this paper indicates that HFTs in the E-mini
also obtain part of their informational edge through a separate channel: exploratory trading. At
a minimum, this evidence about an important group of HFTs in an important market provides
a signi(cid:28)cant counterexample to the standard (cid:16)simply superior speed(cid:17) assumption. As discussed
in Section 1.3, though, my results are likely not unique to the E-mini, or even to futures mar-
kets, because the microstructure elements that enable exploratory trading are common features of
numerous other markets and have well-established economic foundations.
Beyond illuminating several important issues speci(cid:28)c to high-frequency trading and modern
microstructure, my results also bear on an issue of broad signi(cid:28)cance to the (cid:28)eld of (cid:28)nance,
namely how the quantitative changes in the absolute speed at which markets operate have lead to
qualitative changes in the economic mechanisms at work in those markets. Exploratory trading
only yields substantive information when the time-delay between placing an order and observing
the e(cid:27)ects is su(cid:30)ciently brief, and the temporal resolution of market data is su(cid:30)ciently (cid:28)ne.
Whereas superior reaction time is only a matter of relative speed(cid:22)be it measured in months or
microseconds(cid:22)exploratory trading is tied to the absolute speed at which market activity occurs.
1.1 Related analyses of HFTs
HFTs are not all alike, but they share some distinctive features. They have the capacity to
react to market events and news in milliseconds or less, they trade very frequently and unwind
positions within minutes, and they usually end the trading day holding minimal net inventory. As
HagstromerandNorden(2013)documentintheNASDAQ-OMXequitiesmarket, andBaronet al.
(2013)documentintheE-minimarket,someHFTsbasicallybehaveliketraditionalmarket-makers
and supply liquidity/immediacy, but many others do just the opposite, predominantly placing
marketable orders, which consume liquidity/immediacy. Baron et al. directly compute individual
HFTs’tradingpro(cid:28)tsintheE-miniand(cid:28)ndthatHFTsofbothvarietiestendearnlargeandstable
4

pro(cid:28)ts. SinceHFTs’tradingpro(cid:28)tsarenecessarilysomecombinationofcompensationforproviding
liquidity/immediacy, and gains from trading on information that other market participants do not
have, the Baron et al. results suggest that HFTs of the second variety, at least, possess some kind
of superior information. Reinforcing this conclusion, Brogaard et al. (2013) analyze aggregate
HFT activity in a large sample of NASDAQ stocks and (cid:28)nd that HFTs’ aggressive orders tend
to go in the same direction as subsequent permanent price movements, and su(cid:30)ciently so for the
orders to be pro(cid:28)table on average.
The studies above indicate that HFTs enjoy some sort of valuable informational advantage,
but the empirical literature o(cid:27)ers less clarity about the nature and sources of the advantageous
information. The standard assumption has been that HFTs’ ability to use new public information
fastest is the sole source of their informational edge, and this premise underlies much of the
theoretical work on high-frequency trading, including that of Biais et al. (2010), Jovanovic and
Menkveld (2010), and Budish et al. (2013). This assumption tightly circumscribes the character,
scope, and e(cid:27)ects of high-frequency trading. Empirical evidence indicates that HFTs make use of
publicly available information (cf. Brogaard et al.), and without question they can do so more
quicklythanothertraders. However, thereisnorigorousempiricalbasisforthestrongassumption
that this (cid:16)superior speed(cid:17) mechanism is the only source of HFTs’ exceptional information. The
nature of HFTs’ superior information has far-reaching implications for HFTs’ e(cid:27)ects on markets,
for the structure and functioning of the high-frequency trading industry, and for optimal policy
design, so understanding it is of (cid:28)rst-order importance.
1.2 Studying HFTs’ superior information
When a trader initiates a transaction in the E-mini, i.e., places a so-called (cid:16)aggressive(cid:17) order,
he mechanically pays his counterparty a fraction of the bid-ask spread, and so to pro(cid:28)t on his
aggressiveorder,thetradermustcorrectlyanticipateapricemovement.3 Iusepro(cid:28)tsonaggressive
orders in the E-mini as a medium through which to study HFTs’ superior information. Much of
my empirical analysis involves the pro(cid:28)tability of individual aggressive orders. Because all E-
3Ifthetrader(cid:16)anticipatesapricemovement(cid:17) becauseamispricingintheask(bid)presentsanarbitrageoppor-
tunity, he pays part of the spread in only a nominal sense, because the spread-cost is o(cid:27)set by the simultaneous
gain from buying (selling) the mispriced contracts. I thank an anonymous referee for this observation.
5

mini contracts of a given expiration date are identical, it is neither meaningful nor possible to
distinguish among the individual contracts in a trader’s inventory, so there is generally no way to
determine the exact prices at which a trader bought and sold a particular contract. As a result,
it is typically impossible to measure directly the pro(cid:28)ts that a trader earns on an individual
aggressive order. However, the cumulative price change following an aggressive order, normalized
by the order’s direction (+1 for a buy, or −1 for a sell), can be used to construct a meaningful
estimate of the order’s pro(cid:28)tability, and this general approach is standard in the literature. I
discuss implementation details in Section 4.1 and Internet Appendix B, but roughly speaking,
the average expected trading pro(cid:28)t from an aggressive order equals the expected permanent price
movement in the order’s direction, minus trading/clearing fees and half the bid-ask spread.
Since HFTs exhibit great heterogeneity, aggregate HFT activity reveals little about what indi-
vidual HFTs really do. Regulatory records that the Chicago Mercantile Exchange provides to the
CFTC are currently some of the only data for U.S. markets disaggregated enough to be fully ade-
quate for studying high-frequency trading at the level of individual HFTs. Kirilenko et al. (2010)
pioneered the use of transaction data from these records to investigate high-frequency trading in
the E-mini S&P 500 futures market during the (cid:16)Flash Crash(cid:17) of 2010. That paper introduces a
data-driven scheme to classify trading accounts, and speci(cid:28)cally to identify HFTs, using simple
measures of overall trading activity, and of inter- and intra-day variation in net inventory position.
In the present paper, I analyze a richer sample of E-mini data, and I build upon the techniques of
Kirilenko et al. to identify the HFT accounts; I identify 30 HFTs in my sample.
As a group, the 30 HFTs earn roughly 40% of their trading pro(cid:28)ts in the E-mini from their
aggressive orders. Examining these HFTs individually, however, reveals that although all of them
make money in the E-mini, only eight of the 30 pro(cid:28)t on average from their aggressive trading.
For brevity, I refer to these eight HFTs as (cid:16)A-HFTs,(cid:17) and to the remaining 22 as (cid:16)B-HFTs.(cid:17)
The B-HFTs may or may not possess unusually valuable information, but the A-HFTs de(cid:28)nitely
do. Therefore I focus on the A-HFTs and investigate the origins of their superior information,
speci(cid:28)cally, whether the A-HFTs obtain any of it through exploratory trading.
6

1.3 Microstructure foundations of exploratory trading
Exploratory trading is just a simple form of active learning in a (cid:28)nancial market, an idea that
dates back to the theoretical work of Leach and Madhavan in 1992 and 1993, if not further.
At a mechanical level, exploratory trading involves nothing more than placing small aggressive
orders, then learning about expected price-impact using the responses that the exploratory orders
elicit from market-makers.4 From an economic perspective, exploratory trading is a device for
obtaining knowledge from market-makers about the probability that orders in the near future
will be followed by a permanent price change, i.e., the probability of what can loosely be termed
(cid:16)informed trading.(cid:17)5 Prices in real markets are necessarily discrete, so quoted prices alone can
never perfectly reveal or perfectly aggregate every individual market-maker’s private knowledge.
This slight but inevitable heterogeneity in di(cid:27)erent market-makers’ beliefs makes it possible for an
exploring trader to gather knowledge from some market-makers that other market-makers do not
possesses, and such knowledge enables the explorer to identify order (cid:29)ow that is more likely to be
informed than some market-makers realize. Order (cid:29)ow exhibits strong short-run predictability in
most markets, so the explorer can typically trade ahead of some of the identi(cid:28)ed informed orders,
and thereby earn pro(cid:28)ts.
Starting with Hasbrouck’s work in 1991, short-run persistence in order-(cid:29)ow sign (buy vs. sell)
has been a robust empirical (cid:28)nding across numerous markets. Equally robust and widespread is
the (cid:28)nding that trades tend to cluster together in time. In their 2000 paper, Engle and Dufour
document each of these features independently, and they further (cid:28)nd that the autocorrelation in
order-(cid:29)owsignincreasesasordersarrivemorecloselytogetherintime. IntheE-minidataanalyzed
for the present paper, the signs of aggressive orders exhibit strong positive autocorrelation (the
average probability that an aggressive order will have the same sign as the one before it is around
75%) and this autocorrelation becomes even stronger when the arrival rate of aggressive orders
increases. These (cid:28)ndings yield a picture of trading characterized by frequent, sporadic (cid:16)bursts(cid:17) of
many orders with the same sign arriving in close succession.6
4I use (cid:16)market-maker(cid:17) as a heuristic short-hand for (cid:16)trader with limit orders resting in the order book.(cid:17) In the
E-mini market, speci(cid:28)cally, there are no o(cid:30)cial market-makers.
5This mechanical sense of (cid:16)informed trading(cid:17) is observationally equivalent to the traditional notion for equities
of(cid:16)tradingbasedonprivateinsiderinformation.(cid:17) However,themechanicalcharacterizationismoresuitableforthe
futures markets that I analyze, in which the appropriate analogue of (cid:16)private insider information(cid:17) may be unclear.
6See, for example, Ellul et al. (2007), Biais et al. (1995), and more generally, the literature review by Parlour
7

Such bursts of intense trading activity have two classic, con(cid:29)icting explanations. Admati and
P(cid:29)eiderer (1988) explain the clusters as coordinated liquidity trading among uninformed traders,
while Easley and O’Hara (1992) posit that such bursts arise from information-based clustering
of informed traders. Engle and Russell (1998) present evidence that some clusters of trades
seem largely information-based, while other clusters of trades appear to be liquidity-based. If
market-makers know the current probability of informed trading, standard theory suggests that
the bid-ask spread should widen as that probability increases. Consistent with theory, Engle and
Russell (cid:28)nd that intense clusters of trades tend to be liquidity-based when the spread is narrow,
and information-based when the spread is wide. Permanent price impact will tend to be large for
an information-based burst of orders, but small for a liquidity-based burst.
Because order-(cid:29)ow sign is persistent, especially when orders are arriving rapidly, it is not
di(cid:30)cult to aggressively buy (sell) ahead of future aggressive buy (sell) orders.7 However, indis-
criminatelytradingaheadoftheforeseeableremnantsofaburstoforderstendstobeunpro(cid:28)table,
since the subsequent price-change is generally smaller than the part of the spread you would pay
to aggressively trade ahead of the foreseeable orders. To pro(cid:28)t from order-(cid:29)ow predictability,
a trader needs some private knowledge that helps him distinguish uninformed bursts of orders
from informed ones. More speci(cid:28)cally, the trader needs to be able to make this distinction more
accurately than some market-makers.
If prices were continuous, competitive market-makers would, in equilibrium, post quotes at
precisely the levels that would earn zero expected pro(cid:28)t. In this case, through the spread, all the
market-makers would reveal to one another, and to everyone else, all of their relevant knowledge
about the expected adverse-selection risk. If the market-makers all know the same information,
then knowledge obtained from the market-makers clearly could not give a trader an informational
edge that would permit pro(cid:28)t any market-maker’s expense.
When prices are discrete, the situation is di(cid:27)erent. Competitive market-makers only have to
postquoteswithinthesametickasthezero-pro(cid:28)tprice. Thereforethespreadwillnotbeperfectly
revealing, di(cid:27)erent market-makers can hold slightly di(cid:27)erent beliefs, and knowledge obtained from
and Seppi (2008).
7I emphasize that exploiting this robust statistical property of order (cid:29)ow is very di(cid:27)erent from anticipating a
particular trader’s orders.
8

one (or more) market-maker could therefore grant an informational edge su(cid:30)cient for a trader to
pro(cid:28)t at the expense of a di(cid:27)erent market-maker. Scope for exploratory trading arises precisely
becauseofthispossibilityforheterogeneouslyinformedmarket-makers. Moreover,thelargeristhe
tick-size as a fraction of the spread, the greater is the potential heterogeneity in market-makers’
information and beliefs. Exploratory trading closely ties to emerging research on the relationship
between tick-size and high-frequency trading, e.g., Yao and Ye (2014).
The remainder of this paper is organized as follows: Section 2 introduces a simple model of
exploratory trading along with the model’s central predictions, and sets the empirical agenda.
Section 3 describes the data set, presents some summary statistics, and precisely de(cid:28)nes HFTs.
Section 4 addresses the overall pro(cid:28)tability of HFTs’ aggressive orders and precisely characterizes
the A-HFTs. Section 5 presents direct empirical tests of the exploratory trading model’s key
predictions, and section 6 examines the practical signi(cid:28)cance of exploratory information. Section
7 discusses extensions and implications of the empirical results, and Section 8 concludes.
2 Exploratory trading model
This section introduces a stylized model of exploratory trading that provides the framework for
my empirical analysis. Because my empirical analysis centers on the A-HFTs’ information, my
model shares this tight focus, and it abstracts away from the detailed microstructure foundations
discussed in Section 1.3.
2.1 Preliminaries
In an order-driven market, such as the E-mini, every regular transaction is initiated by one of
the two executing transactors. The transactor who initiates is referred to as the (cid:16)aggressor,(cid:17)
while the opposite transactor is referred to as the (cid:16)passor.(cid:17) The passor’s order was resting in the
order book, and the aggressor entered a new order that executed against the passor’s preexisting
resting order. If the best bid and best ask were held (cid:28)xed, a trader who aggressively entered then
aggressively exited a position would lose the bid-ask spread on each contract, whereas a trader
who passively entered then passively exited a position would earn the bid-ask spread on each
contract. Intuitively, aggressors pay for the privilege of trading precisely when they wish to do
9

so, and passors are compensated for the costs of supplying this (cid:16)immediacy,(cid:17) cf. Grossman and
Miller (1988). These costs include (cid:28)xed operational costs and costs arising from adverse selection,
cf. Glosten and Milgrom (1985), Stoll (1989).
An aggressive order will execute against all passive orders at the best available price level
before executing against any passive orders at the next price, so an aggressive order will only have
a literal price-impact if it eats through all of the resting orders at the best price. In the E-mini
market, it is rare for an aggressive order to have a literal price-impact, not only because there are
typically enormous numbers of contracts at the best bid and best ask, but also because aggressive
orders overwhelmingly take the form of limit orders priced at the opposite best (which cannot
execute at the next price level).
Because the bid-ask spread in the E-mini is essentially constant, movements of the best bid,
best ask, and mid-point prices are generally interchangeable, so unless otherwise noted, I restrict
attention hereafter to price changes distinct from bid-ask bounce.
2.2 Model
Consider an order-driven market with discrete prices, and two periods t = 1,2. Both the order
book and order (cid:29)ow are observable. I refer to the aggregated quantities of the passive orders in
the order book as (cid:16)resting depth.(cid:17)
2.2.1 The HFT
Consider a single trader, (cid:16)the HFT,(cid:17) who has the opportunity to submit an aggressive order at the
start of each time-period. The HFT submits only aggressive orders, and these orders are limited
in size to N contracts or fewer. Let q denote the signed quantity of the aggressive order that
t
the HFT places in period t, where a negative quantity represents a sale, and a positive quantity
represents a purchase. The HFT only trades contracts at the initial best bid or ask, so his orders
a(cid:27)ect resting depth in the order book but have no literal price-impact.
The HFT pays constant trading costs of α ∈ (0.5,1) per contract. The lower bound of 0.5 on
α corresponds to half of the minimum possible bid-ask spread, while the upper bound of 1 merely
excludes trivial cases of the model in which aggressive orders will always be unpro(cid:28)table for the
10

HFT.
2.2.2 Passive orders
There are two possible (cid:16)liquidity states(cid:17) (Λ) for the behavior of passive orders: accommodating
(Λ = A) and unaccommodating (Λ = U). The is the same in both time-periods, t = 1,2. With
ex-ante probability u, Λ = U, and Λ = A with ex-ante probability 1−u. Assume 0 < u < 1, so
that both liquidity states are possible.
Intuitively, aggressive orders have a small price-impact in the accommodating liquidity state,
and a large price-impact in the unaccommodating liquidity state. The liquidity state characterizes
thebehaviorofrestingdepthintheorderbookafteranaggressiveorderexecutes(cid:22)ageneralization
of price-impact appropriate for an order-driven market. When an aggressive buy (sell) order
executes, it mechanically depletes resting depth on the sell (buy) side of the order book. Following
this mechanical depletion, traders may enter, modify, and/or cancel passive orders, so resting
depth at the best ask (bid) can either replenish, stay the same, or deplete further. The aggressive
order’s impact is o(cid:27)set to some extent(cid:22)or even reversed(cid:22)if resting depth replenishes, whereas
the aggressive order’s impact is ampli(cid:28)ed if resting depth depletes further. In the accommodating
state (Λ = A) resting depth weakly replenishes, while in the unaccommodating state (Λ = U)
resting depth further depletes.
Although the order book is observable, the static features of passive orders in the order book
do not directly reveal the liquidity state Λ. Because the liquidity state relates to the dynamic
behavior of resting depth after an aggressive order executes, Λ can only be deduced from the
changes in the order book that follow the execution of an aggressive order.
As a baseline, assume that the HFT learns Λ prior to period 2 if and only if he places an
aggressive order in period 1. This assumption is relaxed in Section 2.4.
2.2.3 Aggressive order-(cid:29)ow
At the end of period 2, traders other than the HFT place aggressive orders. Let the variable
ϕ ∈ {−1,0,+1} characterize this aggressive order-(cid:29)ow. The realization of ϕ does not depend on
the liquidity state, Λ, nor does it depend on the HFT’s actions; assume that ϕ = +1 and ϕ = −1
11

with equal probabilities P{ϕ = +1} = P{ϕ = −1} = v/2, and ϕ = 0 with probability 1−v. The
variable ϕ is just a coarse summary of the order-(cid:29)ow(cid:22)it does not represent the actual number
of contracts. Intuitively, ϕ = −1 represents predictable aggressive selling, ϕ = +1 represents
predictable aggressive buying, and ϕ = 0 represents the absence of predictable aggressive trading
in either direction.
Note about exogeneity assumptions Aggressive order-(cid:29)ow is assumed to be independent
of liquidity state for convenience; introducing dependence between aggressive order-(cid:29)ow and the
liquidity state complicates the algebra but does not change the model in any interesting ways.
The assumption that neither aggressive order-(cid:29)ow nor the liquidity state depend on the HFT’s
actions is more innocuous than it might initially seem, because the HFT will turn out not to do
anything that would particularly stand out to other traders. In the (cid:28)rst period, the HFT will
either place a very small order, or no order. In the second period, if the HFT places an order, it
may be large, but if it is, it will always be in the same direction as expected aggressive order-(cid:29)ow.
2.2.4 Prices and price-changes
Prices remain constant between periods 1 and 2, then at the end of period 2 the price changes by
y ∈ {−1,0,+1}. Together, the aggressive order-(cid:29)ow, ϕ, and the liquidity state, Λ, determine y as
follows:


 ϕ if Λ = U
y = (1)

 0 if Λ = A
When the liquidity state is unaccommodating (Λ = U), the aggressive order-(cid:29)ow can a(cid:27)ect the
price, and y = ϕ. However, if the liquidity state is accommodating (Λ = A), aggressive order-(cid:29)ow
does not a(cid:27)ect the price, and y = 0 even when ϕ (cid:54)= 0. In the spirit of Easley and O’Hara/
Engle and Russell, we would suppose that trading in the unaccommodating state is driven by
information, so that the associated price movements would tend to be permanent.
12

2.2.5 Pro(cid:28)ts
The HFT’s pro(cid:28)t from the aggressive order he places in period t is given by
π = yq −α|q | (2)
t t t
= ϕI{Λ = U}q −α|q | (3)
t t
Where I{Λ = U} is an indicator variable that equals 1 when Λ = U, and 0 when Λ = A. (See
Section 4.1 for discussion of why this speci(cid:28)cation for pro(cid:28)ts is reasonable.)
Denote the HFT’s total combined pro(cid:28)ts from periods 1 and 2 by
π := π +π (4)
total 1 2
The HFT is risk-neutral and seeks to maximize the expectation of π .
total
Note that because E[y|Λ = U] = E[ϕ] = 0 and E[y|Λ = A] = 0, the unconditional expectation
of y is zero, as is the period-1 expectation of y. In expectation, the HFT will therefore lose money
on any aggressive order he places in the (cid:28)rst period.
2.2.6 Model time-line
Period 1 In period 1, the HFT has the opportunity to submit an aggressive order and then
observe any subsequent change in resting depth. The HFT cannot observe the liquidity state
directly, but he can infer the value of Λ from changes in resting depth if he places an aggressive
order. Speci(cid:28)cally, the HFT can conclude that Λ = U if resting depth further depletes following
his order, and that Λ = A otherwise. If the HFT does not place an aggressive order in period 1,
he does not learn Λ.
Period 2 Atthestartofperiod2, theHFTobservesthesignaloffutureaggressiveorder-(cid:29)ow, ϕ.
The HFT observes ϕ regardless of whether he placed an aggressive order in period 1 (this re(cid:29)ects
the idea that aggressive order-(cid:29)ow is easy to predict on the basis of public market data). After the
HFT observes ϕ, he once again has an opportunity to place an aggressive order. Finally, after the
HFT has the chance to trade, aggressive order-(cid:29)ow characterized by ϕ arrives, then prices change
13

as determined by ϕ and Λ in equation (1).
2.3 Analysis of the model
By design, the model is not subtle, and determining the HFT’s optimal strategy is straightforward
(Appendix A contains full mathematical details). The HFT faces a trade-o(cid:27) between the direct
trading costs of placing an exploratory order, and the informational gains from exploration.8
By placing a (costly) aggressive order in period 1, the HFT (cid:16)buys(cid:17) the perturbation needed to
elicit a response in resting depth that reveals the liquidity state. Knowing the liquidity state
enables the HFT, in period 2, to better determine whether he would pro(cid:28)t by trading ahead of
predictable aggressive order (cid:29)ow. Despite its simplicity, the model delivers testable implications
of the hypothesis that a given trader engages in exploration.
2.3.1 Order-sizes and conditions for exploratory trading
For the HFT to weakly prefer to engage in period-1 exploratory trading with order-size |q | ≥ 1,
1
the expected gains from knowing the liquidity state in period two (which work out to equal
|q |vu(1−α)) must weakly exceed the expected losses on the exploratory order itself (given by
2
−α|q |). In other words, a necessary condition for exploratory trading to occur in the model is
1
|q |vu(1−α) ≥ α|q | (5)
2 1
(cid:18) (cid:19)
α 1
⇐⇒ |q | ≥ |q | (6)
2 1
1−α vu
⇒ |q | > |q | (7)
2 1
where the (cid:28)nal strict inequality follows from the assumptions that α ≥ 0.5, and u < 1. This
(cid:16)small exploratory order/large follow-up order(cid:17) pattern arises because the exploratory orders are
always costly in expectation, while the resulting exploratory information is only valuable when
there is predictable aggressive order-(cid:29)ow in the next period (i.e., when ϕ (cid:54)= 0). The per-contract
losses on exploratory orders will therefore be greater in magnitude than the per-contract pro(cid:28)ts
8Parameters of the model determine the relative costs and payo(cid:27)s of exploration. I derive routine comparative
staticsinAppendixA,butbecauseexogenousvariationinN,v,α,oruisscarce,thesecomparativestaticsprovide
little in the way of testable implications.
14

on follow-up orders, so the total pro(cid:28)ts on follow-up orders will only exceed the total losses on
exploratory orders if the follow-up orders are larger.
As a stand-alone result, this order-size pattern isn’t particularly interesting or distinctive, but
it plays an important supporting role in the empirics to follow.
2.3.2 Testable predictions
Assumingforthemomentthatcandidateexploratoryorderscanbedistinguishedfromthetrader’s
otherorders(IaddressthisissueinSection2.5), themodelgeneratestwokeytestableimplications
of the hypothesis that a given trader engages in exploration.
First, the model predicts that the market response following an exploratory order helps to
forecast whether or not the explorer will place a follow-up order. The trader will not place a
follow-up order if Λ = A, while he will place a follow-up order if Λ = U and ϕ (cid:54)= 0. As noted
in Section 2.3.1, the follow-up orders must tend to be larger than the exploratory orders, so the
model implies that, holding (cid:28)xed ϕ, the incidence of the trader’s large aggressive orders will be
higher when Λ = U than when Λ = A, if the trader engages in exploration. In other words, if
a given trader engages in exploration, then the market response to his exploratory orders should
help to explain the incidence of his larger aggressive orders (holding (cid:28)xed the expectation of future
aggressive order-(cid:29)ow analogous to ϕ).
Next, the market response following an exploratory order also helps to forecast whether or not
prices will change soon thereafter, according to equation (1). Because both the price-change and
an exploring trader’s decision to place a follow-up order (in the direction of an imminent price-
change) will depend on Λ, the model implies that if a given trader engages in exploration, then
equation (1) will explain his earnings better than ϕ alone. In other words, the market response to
his exploratory orders should help to explain his earnings on subsequent aggressive orders.
2.4 Private knowledge from exploratory trading
Exploratory trading hinges on the fact that the HFT will learn more if he places an exploratory
order than he would learn otherwise. In the model introduced earlier, the HFT could only observe
a market response if he placed an exploratory order, since no one else submitted aggressive orders
15

in the (cid:28)rst period. In reality though, other traders place aggressive orders all the time, so an
HFT can observe a market response to an aggressive order (placed by someone else) even if he
doesn’t place an exploratory order himself. Because exploratory orders are costly in expectation,
a necessary condition for exploratory trading(cid:22)and a testable prediction of the model(cid:22)is that the
HFT learns more from the market response to his own exploratory orders than he does from the
market response to aggressive orders placed by other traders. In an anonymous market (such as
the E-mini), we obtain by symmetry the related prediction that each other trader obtains no more
useful information from the market response to the exploring trader’s aggressive orders than they
would from the market response to another, arbitrary trader’s aggressive orders.
The testable predictions above do not depend on the particular reason why the HFT learns
more from the market response to his own orders than from the response to others’ orders, but
as mentioned in the introduction, there is a natural explanation for this. Sometimes, the changes
in the order book following the arrival of an aggressive order are truly a response caused by the
aggressive order, in which case the order book activity provides information about the liquidity
state. Often, though, both the aggressive order and the subsequent order book activity are really
just common responses to some third event, so there is no causal link between the aggressive
order and the subsequent order book changes, and consequently the order book activity does not
provideinformationabouttheliquiditystate. Ifsomeoneelseplacedtheaggressiveorder,thesetwo
scenariosareindistinguishabletotheHFT,sothepossibilitythatheisobservingtheuninformative
non-causal scenario attenuates the amount that he can learn from the market response to someone
else’s aggressive order. By contrast, if the HFT places an aggressive order himself, he can be
entirely sure whether he did so for exogenous reasons, so the uninformative scenario need not be
a concern. The HFT learns more about the liquidity state from his own aggressive orders than he
does from those of traders because he can better infer causal e(cid:27)ects from aggressive orders that
he himself placed. (For completeness, in Appendix A, I formalize the arguments above using a
variation of the baseline model.)
Although they would not be consistent with exploratory trading, there are possible scenarios
in which an HFT might learn only as much, or perhaps even less, from the response to his own
orders as he would from the response to others’ orders. Whether an HFT truly learns more from
16

the market response to his own orders is an empirical question, and indeed, this is one of the
questions that the empirical analysis in Section 5 and Section 6 helps to address.
2.5 Empirical agenda
Before attempting any empirical evaluation of the hypothesis that the A-HFTs engage in ex-
ploratory trading, suitable candidates for putative exploratory orders must be identi(cid:28)ed in some
manner among the A-HFTs’ aggressive orders. The results from Section 2.3.1 suggest that small,
unpro(cid:28)table aggressive orders are prime candidates. Empirical results presented in Section 4.3 in-
dicatethattheA-HFTstendtolosemoneyontheirsmallestaggressiveorders,soItestthemodel’s
predictions under the assumption that all of the A-HFTs’ small aggressive orders are exploratory.
Given the myriad other reasons for which an A-HFT might place small aggressive orders, the
assumption is conservative. The high probability that some of the orders are not exploratory only
strengthens my results.
With that preliminary matter resolved, I turn to direct empirical tests of the model’s key
predictions. As a benchmark, I consider the market response following the last small aggressive
order placed by anyone, which is public information. The empirical implications discussed earlier
in this section can then be condensed into three central predictions, namely that relative to the
public-information benchmark, information from the market response following an A-HFT’s small
aggressive orders:
Prediction.1 Explains a significant additional component of that A-HFT’s earnings on
subsequent aggressive orders, but
Prediction.2 Does not explain any additional component of other traders’ earnings on
subsequent aggressive orders, and
Prediction.3 Further explains by a significant margin the incidence of that A-HFT’s sub-
sequent large aggressive orders
In Section 5, I introduce an explicit numeric measure of (cid:16)market response,(cid:17) and in Section 5.3, I
make precise the notion of (cid:16)explaining earnings on subsequent aggressive orders,(cid:17) then I formally
test the predictions above. The variables and functional forms used in these empirical tests follow
closely from the structure of the baseline model and the predictions highlighted in Section 2.3.2.
17

3 High-frequency trading in the E-mini market
The E-mini S&P 500 futures contract is a cash-settled instrument with a notional value equal to
$50.00 times the S&P 500 index. Prices are quoted in terms of the S&P 500 index, at minimum
increments, (cid:16)ticks(cid:17), of 0.25 index points, equivalent to $12.50 per contract. E-mini contracts
are created directly by buyers and sellers, so the quantity of outstanding contracts is potentially
unlimited.
All E-mini contracts trade exclusively on the CME Globex electronic trading platform, in an
order-driven market. Transaction prices/quantities and changes in aggregate depth at individual
price levels in the order book are observable through a public market-data feed, but the E-mini
market provides full anonymity, so the identities of the traders responsible for these events are
not released. Limit orders in the E-mini market are matched according to strict price and time
priority; abuy(sell)limitorderatagivenpriceexecutesaheadofallbuy(sell)limitordersatlower
(higher) prices, and buy (sell) limit orders at the same price execute in the sequence that they
arrived. Certain modi(cid:28)cations to a limit order, most notably size increases, reset the time-stamp
by which time-priority is determined.
E-mini contracts with expiration dates in the (cid:28)ve nearest months of the March quarterly cycle
(March, June, September, December) are listed for trading, but activity typically concentrates
in the contract with the nearest expiration. Aside from brief maintenance periods, the E-mini
marketisopen24hoursaday, thoughmostactivityoccursduring(cid:16)regulartradinghours,(cid:17) namely,
weekdays between 8:30 a.m. and 3:15 p.m. CT.
3.1 Description of the data
Thedataareaccount-labeled,millisecond-timestampedrecordsattheCFTCoftheso-called(cid:16)busi-
nessmessages(cid:17) enteredintotheGlobexsystembetweenSeptember17, 2010andNovember1, 2010
for all E-mini S&P 500 futures contracts. These message records capture not only transactions,
but also events that do not directly result in a trade, such as the entry, cancellation, or modi-
(cid:28)cation of a resting limit order. Essentially, business messages include any action by a market
participant that could potentially result in or a(cid:27)ect a transaction immediately, or at any point in
18

the future.9
I restrict attention to the December-expiring E-mini contract, ticker ESZ0. During my sample
period, ESZ0 activity accounted for roughly 98% of the message volume across all E-mini con-
tracts, and more than 99.9% of the trading volume. Trading volume in ESZ0 by the HFTs that I
study is roughly 500 times greater than the total trading volume (by all traders) in all E-mini con-
tracts other than ESZ0 combined, so cross-contract arbitrage is a negligible issue for my empirical
analysis.
The price of an ESZ0 contract during the sample period was around $55,000 to $60,000, and
(one-sided) trading volume averaged 1,991,252 contracts or approximately $115 billion per day.
Message volume averaged approximately 5 million business messages per day, and the number
of aggressive orders executed per day day averaged 132,127. The intensity of trading varies
considerablythroughouttheday(aggressiveorderstypicallyarriveintightclusters),sothemedian
time interval between aggressive orders during regular trading hours is closer to 20 milliseconds
than it is to the mean interval of roughly 200 milliseconds.
3.2 De(cid:28)ning (cid:16)high-frequency trader(cid:17)
Kirilenko et al. identify as HFTs those traders who exhibit minimal accumulation of directional
positions, high inventory turnover, and high levels of trading activity. I, too, use these three
characteristics to de(cid:28)ne and identify HFTs. To quantify an account’s accumulation of directional
positions, I consider the magnitude of changes in end-of-day net position as a percentage of the
account’s daily trading volume. Similarly, I use an account’s maximal intraday change in net
position, relative to daily volume, to measure inventory turnover. Finally, I use an account’s total
trading volume as a measure of trading activity.
Iselecteachaccountwhoseend-of-daynetpositionchangesbylessthan6%ofitsdailyvolume,
andwhosemaximalintradaynetpositionchangesareless than20%ofitsdailyvolume. Irankthe
selected accounts by total trading volume, and classify the top 30 accounts as HFTs. The original
classi(cid:28)cations of Kirilenko et al. and Baron et al. guided the rough threshold choices for inter-day
9Excludedfromthesedataarepurelyadministrativemessages,suchaslog-onandlog-outmessages. Thegood-
’til-cancelordersintheorderbookatthestartofSeptember2,andasmallnumberofmodi(cid:28)cationmessages(around
2−4%) are also missing from these records. Because I restrict attention to aggressive orders, and I only look at
changes in resting depth (rather than its actual level), my results are not sensitive to these omitted messages.
19

and intraday variation. Thereafter, since con(cid:28)dentiality protocols prohibit disclosing results for
groups smaller than eight trading accounts, the precise cuto(cid:27) values of 6%, 20%, and 30 accounts
were chosen to ensure that all groups of interest would have at least eight members. My central
results are not sensitive to values of these parameters.
Changing the 30-account cuto(cid:27) to (e.g.) 15 accounts or 60 accounts does not substantially
alter my results, because activity heavily concentrates among the largest HFTs. For example,
the combined total trading volume of the 8 largest HFTs exceeds that of HFTs 9-30 by roughly
three-quarters, and the combined aggressive volume of the 8 largest HFTs exceeds that of HFTs
9-30 by a factor of almost 2.5. The set of HFTs corresponds closely to the set of accounts with the
greatest trading volume in my sample, so the set of HFTs is largely invariant both to the exact
characterizations of inter-day and intraday variation in net position relative to volume, and to the
exact cuto(cid:27) values for these quantities. The 6% and 20% cuto(cid:27)s are not remotely binding for the
HFTs with the greatest trading volumes.
3.3 HFTs’ prominence and pro(cid:28)tability
Although HFTs constitute less than 0.1% of the 41,778 accounts that traded the ESZ0 contract
between September 17, 2010 and November 1, 2010, they participate in 46.7% of the total trading
volumeduringthisperiod. Inadditiontotradingvolume, HFTsareresponsibleforalargefraction
of message volume. During the sample period, HFTs account for 31.9% of all order entry, order
modi(cid:28)cationandordercancellationmessages. Inaggregate,approximately48.5%ofHFTs’volume
is aggressive, and this (cid:28)gure rises to 54.2% among the 12 largest HFTs. The HFTs also appear
to earn large and stable pro(cid:28)ts. Gross of trading fees, the 30 HFTs earned a combined average
of $1.51 million per trading day during the sample period. Individual HFTs’ annualized Sharpe
ratios are in the neighborhood of 10 to 11.10
10These average trading pro(cid:28)ts re(cid:29)ect the total cumulative trading pro(cid:28)ts during my sample period, divided by
the number of trading days. Total cumulative trading pro(cid:28)ts are computed using all transactions over the full
course of my sample period, plus the marked-to-market value of each HFTs’ net inventory position at the end of
my sample period, minus the initial marked-to-market value of each HFTs’ net inventory position at the start of
my sample period. Positive (negative) initial inventory values are marked to market at the initial best ask (bid),
while positive (negative) (cid:28)nal inventory values are marked to market at the (cid:28)nal best bid (ask); this yields more
conservativeestimatesthanmarkingtomarketatmidpointprices. Empirically,theinitial/(cid:28)nalnetinventoryvalues
are tiny relative to the full cumulative pro(cid:28)ts from transactions.
Using the same methodology, I compute trading pro(cid:28)ts for each trading day in my sample period (for each
individual HFT), and I calculate the standard deviation of those daily trading pro(cid:28)ts (for each individual HFT). I
20

The Chicago Mercantile Exchange reduces E-mini trading fees on a tiered basis for traders
whose average monthly volume exceeds various thresholds. Trading and clearing fees were either
$0.095 per contract or $0.12 per contract for the 20 largest HFTs, and were at most $0.16 per
contract for the remaining HFTs. Initial and maintenance margins were both $4,500 per contract
for all of the HFTs.
Hereafter, unless otherwise noted, I restrict attention to activity that occurred during regular
trading hours. HFTs’ aggressive trading occurs almost exclusively during regular trading hours
(approximately 95.6%, by volume), and market conditions during these times di(cid:27)er substantially
from those during the complementary o(cid:27)-hours.
4 HFTs’ trading pro(cid:28)ts on aggressive orders
4.1 Measuring aggressive order pro(cid:28)tability
The familiar (cid:16)bookkeeping(cid:17) approach used for computing trading pro(cid:28)ts in the preceding section
is not suitable for measuring trading pro(cid:28)ts on individual aggressive orders because it inevitably
commingles earnings from multiple orders. A more suitable general approach, fairly standard
in the literature, involves examining the cumulative price change following an aggressive order,
normalized by the order’s direction (+1 for a buy, or −1 for a sell). Intuitively, the average
expected trading pro(cid:28)t from an aggressive order equals the expected favorable price movement,
minus trading/clearing fees and half the bid-ask spread. This approach is particularly well-suited
to estimating the pro(cid:28)tability of individual HFTs’ aggressive orders in the E-mini, both because
the number of aggressive-order observations for each HFT is large, and because the bid-ask spread
in the E-mini is essentially constant.
To obtain meaningful estimates, we must accumulate the price-changes following an HFT’s
aggressive order out to some time past the maximum horizon at which the HFT can predict
price-movements. We can (cid:28)nd a suitable accumulation period empirically by calculating cumula-
tive direction-normalized price changes over longer and longer windows until their mean ceases to
signi(cid:28)cantly change; beyond that point, the HFT displays no signi(cid:28)cant capacity to forecast addi-
divideaveragedailypro(cid:28)tsbythisstandarddeviation,togettheSharperatioformysampleperiod,thenmultiply
that Sharpe ratio by 251, i.e. total#tradingdaysinayear, to obtain the annualized Sharpe ratio.
32 #tradingdaysinmysample
21

tional price-changes. Using too long an accumulation period introduces extra noise, but it will not
bias the estimates. I (cid:28)nd that an accumulation period, measured in event-time, of 30 aggressive
order arrivals is su(cid:30)cient to obtain unbiased estimates, but for all of the empirical work in this
paper I use an accumulation period of 50 aggressive order arrivals to allow a wide margin for error.
Estimates do not signi(cid:28)cantly di(cid:27)er using an accumulation period of 200, or even 500 aggressive
order arrivals instead of 50, so we can reasonably interpret the estimated price-movements to be
permanent. See Internet Appendix B for further details.
As noted earlier, the bid-ask spread for the E-mini is almost constantly $12.50 (one tick)
during regular trading hours, and the HFTs in my sample face trading/clearing fees of $0.095 to
$0.16 per contract, so the average favorable price movement necessary for an HFT’s aggressive
order to be pro(cid:28)table is between $6.345 and $6.41 per contract. Since trading/clearing fees vary
across traders, I report aggressive order performance in terms of favorable price movement, that
is, earnings gross of fees and the half-spread.
4.2 HFTs’ overall pro(cid:28)ts from aggressive orders in the E-mini
To measure the overall mean pro(cid:28)tability of a given account’s aggressive trading, I compute the
average cumulative price change following each aggressive order placed by that account, weighted
by executed quantity and normalized by the direction of the aggressive order. As a group, the
30 HFTs in my sample achieve average aggressive order performance of $7.01 per contract. On
an individual basis, nine HFT accounts exceed the relevant $6.25+fees pro(cid:28)tability hurdle, and
each of these nine accounts exceeds this hurdle by a margin that is statistically signi(cid:28)cant at the
0.05 level. One of these nine accounts is linked with another HFT account, and their combined
average performance also signi(cid:28)cantly exceeds the pro(cid:28)tability hurdle.
Overall,theHFTsvastlyoutperformnon-HFTs,whoearnagrossaverageof$3.19peraggressively-
traded contract. However, these overall averages potentially confound e(cid:27)ects of very coarse dif-
ferences in the times at which traders place aggressive orders with e(cid:27)ects of the (cid:28)ner di(cid:27)erences
more directly related to strategic choices. For example, if all aggressive orders were more prof-
itable between 1 p.m. and 2 p.m. than at other times, and HFTs only placed aggressive orders
during this window, the HFTs’ out-performance would not depend on anything characteristically
22

high-frequency.
To control for potential low-frequency confounds, I divide each trading day in my sample
into 90-second segments and regress the pro(cid:28)tability of non-HFTs’ aggressive orders during each
segment on both a constant and the executed quantities of the aggressive orders. Using these
local coe(cid:30)cients, I compute the pro(cid:28)tability of each aggressive order by an HFT in excess of the
expectedpro(cid:28)tabilityofanon-HFTaggressiveorderofthesamesizeduringtherelevant90-second
segment. With these additional controls, only 27 HFT accounts continue to exhibit signi(cid:28)cant
out-performance of non-HFTs, and only eight of the 27 accounts are among those whose absolute
performance exceeded the pro(cid:28)tability hurdle.
4.2.1 A-HFTs and B-HFTs
For expositional ease, I will refer to the eight HFT accounts that make money on their aggressive
trades and outperform the time-varying non-HFT benchmark as (cid:16)A-HFTs,(cid:17) and to the comple-
mentary set of HFTs as (cid:16)B-HFTs.(cid:17) The eight A-HFTs have a combined average daily trading
volume of 982,988 contracts, and on average, 59.2% of this volume is aggressive. The 22 B-HFTs
have a combined average daily trading volume of 828,924 contracts, of which 35.9% is aggressive.
Together, the eight A-HFTs place a daily average of 8,994 aggressive orders (during regular trad-
ing hours), with a mean size of 60.3 contracts and a median size of 10 contracts. The 22 B-HFTs
together place an average of 31,113 aggressive orders per day (during regular trading hours), with
a mean size of 8.3 contracts and a median size of 1 contract. Gross of fees, the A-HFTs earn a
combined average of $793,342 per day, or an individual average of $99,168 per day, while the B-
HFTs earn a combined average of $715,167 per day, or an individual average of $32,508 per day.11
The highest pro(cid:28)tability hurdle among the A-HFTs is $6.37 per aggressively traded contract.
4.3 Identifying some potential exploratory orders
As noted in Section 2.5, to test the empirical predictions of the exploratory trading model, we
must(cid:28)rstspecifysomeorderstotreatasexploratory. Motivatedbytheory,IexaminetheA-HFTs’
small aggressive orders. To make precise the meaning of (cid:16)small(cid:17) aggressive order, I specify a cuto(cid:27)
11The preceding descriptive statistics include the small amount of trading activity that occurred outside regular
trading hours, except where noted otherwise.
23

Table 1: Summary Statistics for A-HFTs’ Small Aggressive Orders
Dollars Earned per Contract (95% CI)
AOs Below AOs Above AOs Below Cuto(cid:27) AOs Below Cuto(cid:27)
Cuto(cid:27) Cuto(cid:27) Size Cuto(cid:27) Size % of All AOs % of Aggr. Volume
1 (3.78,3.89) (7.59,7.74) 24.31% 0.40%
5 (4.17,4.29) (7.62,7.78) 43.74% 1.44%
10 (3.42,3.55) (7.71,7.85) 54.64% 3.09%
15 (3.79,3.92) (7.71,7.86) 56.75% 3.54%
20 (4.08,4.20) (7.75,7.90) 60.82% 4.80%
Table1presentsdescriptivestatisticsaboutaggressiveordersofvaryingsizesplacedbytheA-HFTs. The(cid:16)Cuto(cid:27)(cid:17)
columnindicatesthemaximumsizeforordersincludedinthe(cid:16)belowcuto(cid:27)(cid:17) statistics. Allordersofsizesexceeding
thespeci(cid:28)edcuto(cid:27)areincludedincalculationsofthe(cid:16)abovecuto(cid:27)(cid:17) statistics. Columnstwoandthreepresent95%
con(cid:28)denceintervalsfortheaveragegrossearningspercontract(indollars)amongaggressiveordersintheindicated
size division. Column four reports the percentage ofall aggressiveorders placed bythe A-HFTs with an order-size
no greater than the indicated cuto(cid:27). Column (cid:28)ve reports the A-HFTs’ aggressive volume from orders of size no
greater than the indicated cuto(cid:27), as a percentage of the A-HFTs’ total aggressive volume.
for order-size andde(cid:28)nean order to be (cid:16)small(cid:17) if andonlyif its size is nogreater than the speci(cid:28)ed
cuto(cid:27). Because there is no natural unique cuto(cid:27), I consider a range of di(cid:27)erent order-size cuto(cid:27)s.
The A-HFTs tend to pro(cid:28)t on aggressive orders above size 20, so I consider various order-size
cuto(cid:27)s between 1 and 20.12 Table 1 summarizes some important characteristics of the A-HFTs’
small aggressive orders.
AgivenA-HFTplacesanaggressiveorderofsize20orlessroughlyonceevery34secondsonav-
erage, and this average interval drops to about 3 seconds during periods of intense market activity.
Furthermore, A-HFTs’ aggressive orders of size 20 or less tend to lose money on average. Because
the A-HFTs’ small aggressive orders tend to be unpro(cid:28)table and to arrive rather frequently, they
are at least plausible candidates to be exploratory orders. Clearly, these results don’t provide any
compelling evidence of exploratory trading; orders with analogous features could also arise from
12Presentingstatisticsforeveryorder-sizecuto(cid:27)between1and20couldpotentiallyrevealindividuallyidenti(cid:28)able
information, so I only present results for a regularly spaced subset of order-size cuto(cid:27)s.
24

A-HFTs controlling risk, testing out new strategies, hedging, etc. However, identifying candidate
exploratory orders provides the starting point for direct tests of the exploratory trading model’s
sharper empirical predictions, which, it turns out, do provide compelling evidence of exploratory
trading.
5 Testing the exploratory trading hypothesis
If the A-HFTs indeed engage in exploration using their small aggressive orders, the exploratory
trading model generates the testable predictions presented in Section 2. The present section
introduces empirical analogues of the two quantities from the exploratory trading model that
appear in the model’s predictions: the market-response that reveals the liquidity state (Λ), and
the signal of future aggressive order-(cid:29)ow, ϕ. I use these to directly test the predictions from
Section 2.
The model’s (cid:28)rst two predictions concern the explanatory power of market-response informa-
tion for the earnings of subsequent aggressive orders, and I test these two predictions in the same
empirical framework. The third prediction, concerning the incidence of large aggressive orders,
requires a slightly di(cid:27)erent empirical approach, so I consider this prediction separately. I estimate
results for the A-HFTs individually, but for compliance with con(cid:28)dentiality protocols, I present
cross-sectional averages of these estimates. Empirically, these average results are representative of
the results for individual A-HFTs.13
5.1 A simple measure of market response
The predictions in Section 2 involve the market response to a given A-HFT’s exploratory orders,
which we have conjectured, for the purposes of testing, to be the A-HFT’s small aggressive orders.
To make this precise, de(cid:28)ne an aggressive order to be (cid:16)small(cid:17) if that order’s submitted size is less
than or equal to a speci(cid:28)ed size parameter, which I will denote by q¯.
I characterize the market response to a small aggressive order using subsequent changes in
13ThroughouttheE-minimarket,thereexistassortedlinkagesbetweenvarioustradingaccounts(as,forexample,
in the simple case where single (cid:28)rm trades with multiple accounts), so the trading-account divisions do not neces-
sarily deliver appropriate atomic A-HFT units. Though the speci(cid:28)cs are con(cid:28)dential, the appropriate partition of
the A-HFTs is entirely obvious. For brevity, I use (cid:16)individual A-HFT(cid:17) as shorthand to (cid:16)individual atomic A-HFT
unit,(cid:17) as applicable.
25

order book depth. I examine the interval starting immediately after the arrival and execution of a
givensmallaggressiveorderandendingimmediatelybeforethearrivalofthenextaggressiveorder
(which may or may not be small), and I sum the changes in depth at the best bid and best ask
that occur during this interval.14 For symmetry, I adopt the convention that sell depth is negative
and buy depth is positive. I also normalize these depth changes by the sign of the preceding small
aggressive order to standardize across buy orders and sell orders.
To simplify the analysis and stack the odds against (cid:28)nding signi(cid:28)cant results, I initially focus
only on the signs of the direction-normalized depth changes. These signs merely indicate whether
or not resting depth moved further in the direction of the preceding small aggressive order(cid:22)or in
the language of the model, whether resting depth further depletes or weakly replenishes.
For a given value of q¯, I construct the indicator variable Ω, with kth element Ω de(cid:28)ned by
k


 1 if DC(k;any,q¯) > 0
Ω = (8)
k

 0 otherwise
where DC(k;any,q¯) denotes the direction-normalized depth change following the last small ag-
gressive order (submitted by anyone) that arrived before the kth aggressive order. Similarly, I
construct the indicator variable ΩA, with kth element ΩA de(cid:28)ned by
k


 1 if DC(k;AHFT,q¯) > 0
ΩA = (9)
k

 0 otherwise
where DC(k;AHFT,q¯) denotes the direction-normalized depth change following the last small
aggressive order submitted by a speci(cid:28)ed A-HFT that arrived before the kth aggressive order.
Note the direct parallel between the omega variables and the binary liquidity states in the
exploratory trading model.
14The best bid and best ask prices at which I measure changes in depth are the best bid and ask at start of the
interval. The price levels at which changes in depth are recorded remain the same throughout an interval, even if
the bid and/or ask prices move during the interval.
26

5.2 Order-(cid:29)ow signal
To test the exploratory trading theory, in addition to the measure of market response, we need
something analogous to the signal of future aggressive order-(cid:29)ow, ϕ. Because we are ultimately
interested in how future aggressive order-(cid:29)ow will a(cid:27)ect prices, the task of (cid:28)nding an empirical
analogue to ϕ simpli(cid:28)es to (cid:28)nding variables other than market-response measures that forecast
price movements.
I select a handful of lagged market variables that forecast the cumulative price-change between
theaggressiveorderskandk+50,whichIdenotebyy . Thesevariablesare: thesignsofaggressive
k
orders k−1 through k−4, the signed executed quantities of aggressive orders k−1 through k−4,
and changes in resting depth between aggressive orders k−1 and k at each of the six price levels
within two ticks of the best bid or best ask (with sell depth negative and buy depth positive, as
before). To lighten notation, I concatenate these 14 variables in the row vector z . This vector,
k−1
z , is the analogue of ϕ.
k−1
In the same way that price movements in the exploratory trading model can still be forecast
to some extent by ϕ when the liquidity state is unknown, the variables in z should have some
k−1
power to forecast y , even without the market-response omega variables. As a check on this and
k
as a benchmark, I estimate the equation
y = z Γ+(cid:15) (10)
k k−1 k
where Γ is a column vector of 14 coe(cid:30)cients. As desired, the estimated coe(cid:30)cients have the
expected signs, and their joint signi(cid:28)cance is extremely high. I discuss the regression results
directly, report coe(cid:30)cient estimates, and discuss the choice of explanatory variables in Internet
Appendix C.
Naturally, the set of right-hand-side variables in equation (10) is not comprehensive, and many
other variables can be added that could somewhat improve the price forecasts. However, the
tests of the exploratory trading model’s predictions do not rely on equation (10) as the means of
controlling for public information, but rather rely on a di(cid:27)erent approach (described in the next
section). The tests merely require that equation (10) have some forecasting power.
27

5.3 Testing predictions about explaining earnings
5.3.1 Explained earnings
The (cid:28)rst testable prediction of the exploratory trading model is that the information from the
market response following a given A-HFT’s small aggressive orders will explain a signi(cid:28)cant addi-
tional component of that A-HFT’s earnings on subsequent (large) aggressive orders, beyond what
is explained by a public-information benchmark.
In this paper, the particular notion of (cid:16)explaining earnings(cid:17) that I employ involves computing
what a trader’s earnings are expected to be on the basis of some econometric forecast of price
movements, and comparing that with the trader’s actual earnings. For concreteness, consider a
price forecast based on equation (10). Letting Γˆ denote the estimate of Γ, we have
yˆ = z Γˆ
k k−1
Given the sign of the kth aggressive order, we can compute the forecast earnings on that order,
conditional on the order’s sign. Much as the direction-normalized cumulative price-change sign ∗
k
y provides an estimate of the true earnings on aggressive order k (see Section 4.1), the direction-
k
normalizedforecastcumulativeprice-changesign ∗yˆ providesanestimateoftheforecastearnings
k k
on aggressive order k.
Rather than working with the earnings on order k that are explained by a given econometric
price forecast, it is convenient to work with the earnings on order k that are not explained by the
speci(cid:28)ed forecast. I will refer to the earnings on order k that are not explained by the speci(cid:28)ed
forecast as the (cid:16)excess earnings on order k relative to [the speci(cid:28)ed forecast].(cid:17) In the case above,
the excess earnings on order k relative to the forecast from equation (10), denote it ξ , is given by
k
ξ = sign ∗y −sign ∗yˆ
k k k k k
= sign (y −yˆ )
k k k
so ξ is simply the kth regression residual multiplied by the sign of aggressive order k.15 The
k
15Because yˆ k uses only information available prior to the arrival of the kth aggressive order, there is no orthogo-
nality constraint on the kth regression residual and sign k.
28

additionalcomponentofearningsonaggressiveorderk explainedbysomepriceforecastF,relative
to some other price forecast G is given by ξG−ξF.
k k
Finally, note that the all of the earnings discussed in this section are per contract.
5.3.2 Empirical strategy: overview
Though the implementation is slightly involved, my empirical strategy is straight-forward(cid:22)it is
basically just a di(cid:27)-in-di(cid:27)s approach. First, I augment the regression equation (10) from Section
5.2 using either:
1. Market response information from the last small aggressive order placed by anyone(cid:22)i.e., Ω,
or
2. Both market response information from the last small aggressive order placed by anyone,
and market response information from the last small aggressive order placed by a speci(cid:28)ed
A-HFT(cid:22)i.e., both Ω and ΩA
After estimating both of the regression speci(cid:28)cations above, I (cid:28)nd the additional component of
earnings on larger aggressive orders explained by the second speci(cid:28)cation relative to the (cid:28)rst one.
Themarketresponsefollowinganarbitrarysmallaggressiveorderispubliclyobservable. However,
because the E-mini market operates anonymously, the distinction between a small aggressive
order placed by a particular A-HFT and an arbitrary small aggressive order is private knowledge,
available only to the A-HFT who placed the order. Because the market response information
from the last small aggressive order placed by anyone is weakly more recent than the market
response information from last small aggressive order placed by the A-HFT, comparing the second
speci(cid:28)cation above to the (cid:28)rst helps to isolate the e(cid:27)ects attributable to private knowledge from
e(cid:27)ects attributable to public information.
Finally, I compare the additional explained earnings for the speci(cid:28)ed A-HFT to the additional
explainedearningsforallothertraders. Intuitively,wewanttoverifythattheA-HFT’sexploratory
information provides extra explanatory power for the subsequent performance of the trader privy
to that information (the A-HFT), but not for the performance of traders who aren’t privy to it
(everyone else). Note that (cid:16)everyone else(cid:17) includes the A-HFTs other than the speci(cid:28)ed A-HFT.
29

Some A-HFT accounts and B-HFT/non-HFT accounts belong to the same (cid:28)rms, and various B-
HFTs/non-HFTs may be either directly informed or able to make educated inferences about what
one or more A-HFTs do. As a result, we should not necessarily expect exploratory information
generated by an A-HFT’s small orders to provide no explanatory power whatsoever for all other
traders’ performance. However, we should still expect the additional explanatory power for the
A-HFT’s performance to signi(cid:28)cantly exceed that for the other traders’ performance.
Controlling for public information Comparingthesecondregressionspeci(cid:28)cationtothe(cid:28)rst
one controls for the e(cid:27)ects of most public information, but there could conceivably be some public
information that is correlated with the market response to a speci(cid:28)ed A-HFT’s small aggressive
ordersandyetuncorrelatedwiththemarketresponsetosmallaggressiveordersplacedbyeveryone
else. One way to handle this concern is to compare the additional explained performance for the
speci(cid:28)ed A-HFT to the additional explained performance for some other traders who use the
same public information. Although trading objectives and sophistication vary widely across many
participantsintheE-minimarket,alloftheHFTsaresophisticated,pro(cid:28)tabletraders,withsimilar
(very short) investment horizons, so it is extremely plausible that they all use very similar public
data. Comparing the additional explained performance for the speci(cid:28)ed A-HFT to that for the
other HFTs therefore serves as an added control for any lingering e(cid:27)ects from public information.
5.3.3 Estimation procedure
In the model of exploratory trading presented in Section 2, exploratory information was valuable
only in conjunction with information about future aggressive order (cid:29)ow. Following this notion,
I incorporate market-response information by using the indicators Ω and ΩA to partition the
benchmark regression from Section 5.2.
Recall that Section 5.2 introduced the regression equation (10),
y = z Γ+(cid:15)
k k−1 k
where y denoted the cumulative price-change between the aggressive orders k and k +50, and
k
the vector z consisted of changes in resting depth between aggressive orders k −1 and k, as
k−1
30

well as the signs and signed executed quantities of aggressive orders k−1 through k−4. Using
the indicator Ω, I now partition the equation above into two pieces and estimate the equation
y = Ω z Γa+(1−Ω )z Γb+(cid:15) (11)
k k k−1 k k−1 k
Next, I use the indicator ΩA to further partition (11), and I estimate the equation
(cid:16) (cid:17)
y = ΩA(k) Ω z Γc+(1−Ω )z Γd + (12)
k k k k−1 k k−1
(cid:16) (cid:17)
(cid:0) 1−ΩA(cid:1) Ω z Γe+(1−Ω )z Γf +(cid:15)
k k k−1 k k−1 k
The variables y and z denote the same quantities as before, and the Γj terms each represent
k k−1
vectors of 14 coe(cid:30)cients.
Iestimate(11)and(12)forq¯= 1,5,10,15,20, andforeachspeci(cid:28)cationIcalculatetherelative
excess earnings of the speci(cid:28)ed A-HFT, and of all other trading accounts, on aggressive orders
of size strictly greater than q¯. As in Section 5.3.1, to compute the earnings of aggressive order k
in excess of that explained by each regression speci(cid:28)cation, I normalize the kth residual from the
regression by the sign of the kth aggressive order. I now also control for order-size e(cid:27)ects directly
by regressing the direction-normalized residuals (for the orders of size strictly greater than q¯) on
the (unsigned) executed quantities and a constant, then subtracting o(cid:27) the executed quantity
multiplied by its estimated regression coe(cid:30)cient. Controlling for size e(cid:27)ects in this manner makes
results more comparable for di(cid:27)erent choices of q¯. Size e(cid:27)ects can be addressed by other means
with negligible impact on the (cid:28)nal results.
For each aggressive order larger than q¯placed by the A-HFT under consideration, I compute
the additional component of earnings explained by (12) relative to (11) by subtracting the order’s
excess earnings relative to (12) from its excess earnings relative to (11); I stack these additional
explained components in a vector that I denote by Ξ . I repeat this procedure to obtain the
A
analogous vector for everyone else, Ξ .
ee
Equation (12) has more free parameters than (11), so Ξ and Ξ will both have positive
A ee
means. However, additional explanatory power of (12) due exclusively to the extra degrees of
freedom will, in expectation, manifest equally for all traders, so the extra degrees of freedom alone
31

Figure 3. Additional Performance Explained (95% Confidence Intervals)
Figure 1: Additional Earnings Explained by Exploratory Information
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
0 5 10 15 20
q-Bar
tcartnoC
rep
stneC
A-HFTs Everyone Else
Figure1displaysaverages(with95%con(cid:28)denceintervals)oftheadditionalearningspercontractexplainedby(12)
beyond what is explained by (11). This di(cid:27)erence re(cid:29)ects added explanatory power that arises from including in
(12) information about the market response to the last small aggressive order placed by a speci(cid:28)ed A-HFT (plus
the slight mechanical increase that arises from introducing extra degrees of freedom). The horizontal axis speci(cid:28)es
the cuto(cid:27), q¯, for the maximum size of order de(cid:28)ned to be (cid:16)small.(cid:17) The white circles mark this average computed
among orders placed by an A-HFT, and the black squares mark this average computed among orders placed by
everyone else. Estimates were run and means were computed for each individual A-HFT and the corresponding
(cid:16)everyone else(cid:17); the displayed numbers are cross-sectional averages of the individual estimates’ means.
should not cause Ξ and Ξ to di(cid:27)er signi(cid:28)cantly.
A ee
5.3.4 Results on explaining earnings
I initially evaluate the (cid:28)rst two empirical predictions of the exploratory trading model by com-
paring the additional explained component of earnings for each A-HFT (Ξ ) to the additional
A
explained component of earnings for all other traders (Ξ ). Figure 1 displays the cross-sectional
ee
means of Ξ and Ξ for di(cid:27)erent values of q¯. To formally compare the gain in explanatory power
A ee
fortheA-HFTstothegainforeveryoneelse,Iconstruct95%bootstrapcon(cid:28)denceintervalsforthe
di(cid:27)erence of the pooled means Mean(Ξ )−Mean(Ξ ), displayed in Figure 2. Table 2 reports
A ee
the numeric values from Figures 1 and 2.
Both of the tested predictions are borne out in these results. Information about the market
activityimmediatelyfollowinganA-HFT’ssmallestaggressiveorders(intheformofΩA)improves
our ability to explain that A-HFT’s earnings on larger subsequent aggressive orders by a highly
32

Figure 4. [A-HFT Addt'l Explained] - [Everyone Else Addt'l Explained] (95% Conf. Intervals)
Figure 2: Di(cid:27)erence in Additional Earnings Explained by Exploratory Information
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
0 5 10 15 20
q-Bar
tcartnoC
rep
stneC
Figure2depictsthedi(cid:27)erenceforA-HFTsvs. foreveryoneelseoftheadditionalearningspercontractexplainedby
exploratory information. E(cid:27)ectively, this is just the di(cid:27)erence of the two series displayed in Figure 1. For a given
A-HFT,andthecorresponding(cid:16)everyoneelse,(cid:17) I(cid:28)ndtheadditionalearningspercontractexplainedby(12)beyond
what is explained by (11), and I compute the di(cid:27)erence between the average for the A-HFT, and the average for
everyone else. Estimates were run and means were computed for each individual A-HFT, and the displayed points
are cross-sectional averages of these individual estimates’ means (with 95% con(cid:28)dence intervals). The horizontal
axis speci(cid:28)es the cuto(cid:27), q¯, for the maximum size of order de(cid:28)ned to be (cid:16)small(cid:17) when estimating (12) and (11).
signi(cid:28)cant margin, relative to using only information about the activity following any small ag-
gressive order (in the form of Ω). Furthermore, the extra component of A-HFTs’ earnings on large
aggressive orders explained by using ΩA in addition to Ω is signi(cid:28)cantly greater than the extra
component explained for other traders.
I re(cid:28)ne my empirical evaluation of the (cid:28)rst two predictions by comparing the additional ex-
plained component of earnings for each A-HFT to the additional explained component of earnings
for the other HFTs. Consistent with the notion that certain HFTs may know something about
what various A-HFTs are doing, the extra component of earnings explained by using ΩA in addi-
tion to Ω is larger for the complementary set of HFTs than it is for the broader (cid:16)everyone except
the A-HFT of interest(cid:17) group. Nevertheless, aside from the case of q¯ = 1, the average added
explanatory power for each A-HFT is still signi(cid:28)cantly greater than is that for the complementary
set of HFTs, as shown in Figure 3. See Table 2 for numeric values.
33

noitamrofnI
yrotarolpxE
yb
denialpxE
sgninraE
lanoitiddA
:2
elbaT
.
)slavretni
ecned(cid:28)noc
%59
htiw
,tcartnoc
rep
tnec
a
fo
shtderdnuh
ni
detropeR(
02=¯q
51=¯q
01=¯q
5=¯q
1=¯q
3.11
1.01
4.7
2.8
4.3
srehtOllA
)7.41,7.7(
)3.31,1.7(
)4.01,1.4(
)9.01,5.5(
)8.4,8.1(
3.26
3.35
7.93
9.56
9.71
sTFH-A
)9.97,3.54(
)5.07,5.53(
)0.75,1.22(
)0.58,0.84(
)6.92,9.6(
0.15
2.34
3.23
7.75
5.41
.svTFH-A
)6.86,2.33(
)4.06,4.52(
)0.05,9.31(
)4.67,3.93(
)7.52,6.3(
srehtOllA
6.24
3.23
5.32
8.54
8.3
.svTFH-A
)8.16,8.32(
)3.05,5.31(
)0.24,3.5(
)1.56,9.62(
)4.51,6.7-(
sTFHrehtO
¯q
naht
retaerg
ezis
dettimbus
fo
sredro
evissergga
no
tcartnoc
rep
sgninrae
ssorg
lanoitidda
detamitse
eht
fo
segareva
lanoitces-ssorc
suoirav
stneserp
2
elbaT
rof
tcartnoc
rep
sgninrae
denialpxe
lanoitidda
eht
setoned
(cid:17)srehtO
llA
.sv
TFH-A(cid:16)
.)11(
noisserger
yb
denialpxe
taht
fo
ssecxe
ni
)21(
noisserger
yb
denialpxe
rof
detroper
srebmuN
.ytitnauq
suogolana
na
setoned
(cid:17)sTFH
rehtO
.sv
TFH-A(cid:16)
;sTFH-A
eht
ssorca
degareva
,sredart
rehto
lla
rof
esoht
sunim
TFH-A
nevig
a
TFH-A
ralucitrap
eht
nopu
sdneped
(cid:17)sTFH
rehtO(cid:16)
dna
(cid:17)srehtO
llA(cid:16)
fo
pihsrebmem
ehT
.sTFH-A
laudividni
rof
setamitse
eht
revo
segareva
era
sTFH-A
eht
taht
etoN
.sTFH-A
laudividni
eht
fo
hcae
ot
gnidnopserroc
spuorg
tnere(cid:27)id
ylthgils
eht
ssorca
nekat
segareva
era
srebmun
detroper
eht
dna
,dedulcxe
gnieb
.sTFH-A
rehto
eht
sedulcni
(cid:17)sTFH
rehto(cid:16)
.3
erugiF
ot
sdnopserroc
wor
htruof
eht
dna
,2
erugiF
ot
sdnopserroc
wor
driht
eht
,1
erugiF
ni
detroper
stluser
eht
ot
dnopserroc
swor
owt
tsr(cid:28)
ehT
34

Figure 3: Di(cid:27)erence from Other HFTs in Additional Earnings Explained by Exploratory Informa-
Figure 5. [A-HFT Addt'l Explained] - [Other HFTs Addt'l Explained] (95% Conf. Intervals)
tion
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
-0.1
0 5 10 15 20
q-Bar
tcartnoC
rep
stneC
Figure3depictstheaveragedi(cid:27)erenceinadditionalearningspercontractexplainedbyexploratoryinformationfor
agivenA-HFTvsforallotherHFTs. ForagivenA-HFT,andthecomplementarysetofallotherHFTs,I(cid:28)ndthe
additional earnings per contract explained by (12) beyond what is explained by (11), and I compute the di(cid:27)erence
between the average for the A-HFT, and the average for all the other HFTs. Note that (cid:16)other HFTs(cid:17) includes the
otherA-HFTs. EstimateswererunandmeanswerecomputedforeachindividualA-HFT,andthedisplayedpoints
are cross-sectional averages of these individual estimates’ means (with 95% con(cid:28)dence intervals). The horizontal
axis speci(cid:28)es the cuto(cid:27), q¯, for the maximum size of order de(cid:28)ned to be (cid:16)small(cid:17) when estimating (12) and (11).
5.4 Incidence of A-HFTs’ larger aggressive orders
In this subsection I test the exploratory trading model’s third prediction, namely that the market
response to a given A-HFT’s small aggressive order provides signi(cid:28)cant explanatory power for the
incidence of that A-HFT’s subsequent large aggressive orders, above and beyond that explained
usingthemarketresponsetothelastsmallaggressiveorderplacedbyanyone. Sinceelementsofthe
binary Ω-operators correspond almost directly to the binary liquidity-state Λ in the exploratory
trading model, the incidence prediction can be made even more precise. In particular, all else
being equal, the exploratory trading model predicts that an A-HFT will have a greater tendency
to place large aggressive orders when ΩA = 1 than when ΩA = 0.
5.4.1 Empirical implementation
Much as the HFT in the model from Section 2 considered the signal of future aggressive order-
(cid:29)ow as well as the liquidity state, A-HFTs consider public market data as well as exploratory
information to decide when to place large aggressive orders. The size and direction of A-HFTs’
aggressive orders depend on the same variables that forecast price movements, or equivalently
35

on the forecasts of price movements themselves. On average, the signed quantity of an A-HFT’s
aggressive order should be an increasing function of the future price-change expected on the basis
of public information. In this context, the exploratory trading model predicts that the expected
futureprice-changewillhavealargere(cid:27)ectonthesignedquantityofanA-HFT’saggressiveorders
when ΩA = 1 than it will when ΩA = 0.
To test the exploratory trading model’s prediction about the incidence of A-HFTs’ larger
aggressive orders, I regress the signed quantities of a given A-HFT’s aggressive orders on the
associated (cid:28)tted values of y from equation (11), partitioned by ΩA. In other words, for a speci(cid:28)ed
A-HFT and a given value of q¯, I estimate the equation
q = β (cid:0) 1−ΩA(cid:1) yˆ +β ΩAyˆ +(cid:15) (13)
k 0 k k 1 k k k
where q denotes the signed submitted quantity of the A-HFT’s kth aggressive order, yˆ denotes
k k
the relevant (cid:28)tted value of y from the public-information regression (11), and ΩA is the usual
k
indicator function. I restrict the β coe(cid:30)cients to be the same across all A-HFTs. Note that the
(cid:28)tted value yˆ includes the public market-response information through the inclusion of Ω in
k k
(11), so di(cid:27)erences between β and β do not arise from any public information in ΩA.
0 1
5.4.2 Results on explaining incidence
Table 3 displays the coe(cid:30)cient estimates from (13) for various values of q¯. A Wald test rejects the
null hypothesis β = β at the 10−15 level for all values of q¯. As the exploratory trading model
0 1
predicts, holding (cid:28)xed the price-change expected on the basis of public information, the average
A-HFT places signi(cid:28)cantly larger aggressive orders when ΩA = 1 than when ΩA = 0.
5.5 Possible alternative explanations of the results
Although the empirical results in this section con(cid:28)rm the predictions of the exploratory trading
theory, that does not necessarily rule out alternative explanations for those results. To the extent
that a movement of resting depth in the same direction as the last aggressive order is indicative
of informed trading, the empirical results at (cid:28)rst glance appear to be potentially consistent with
the story that the A-HFTs (somehow) already possess private information and they split up their
36

Table 3: Di(cid:27)erential E(cid:27)ects of Predicted Price-Changes on A-HFT Signed Order Size
q¯= 1 q¯= 5 q¯= 10 q¯= 15 q¯= 20
β 13.35 13.41 13.42 13.34 13.23
0
(β Standard Error) (0.094) (0.093) (0.095) (0.095) (0.094)
0
β 15.26 15.11 14.97 15.10 15.30
1
(β Standard Error) (0.162) (0.169) (0.160) (0.159) (0.160)
1
Table 3 reports coe(cid:30)cient estimates from the regression of the signed quantities of the A-HFTs’ aggressive orders
on the (cid:28)tted values of cumulative future price changes from equation (11):
(cid:16) (cid:17)
q =β 1−ΩA yˆ +β ΩAyˆ +(cid:15)
k 0 k k 1 k k k
The q¯values specify the maximum size of order de(cid:28)ned to be (cid:16)small(cid:17) when computing estimates.
The indicator ΩA is the same market-response variable used elsewhere. The kth element of ΩA equals unity if,
following the most recent small aggressive order placed by a speci(cid:28)ed A-HFT, resting depth moved in the same
directionasthatorder;otherwise,thekthelementofΩA equalszero. Thecoe(cid:30)cientsβ 0 andβ 1 respectivelyre(cid:29)ect
therelativesizesoftheaverageaggressiveorderthatanA-HFTplaceswhenΩA =0,versuswhenΩA =1,holding
yˆ(cid:28)xed. Di(cid:27)erencesbetweenβ
0
andβ
1
canbeattributedtotheprivatecomponentofinformationinΩA becauseyˆ
alreadyincorporatesthepublic-informationanalogueofΩA. Theexploratorytradingmodelpredictsthatβ 1 >β 0.
orders as they trade on that information. While this alternative story would be more appropriate
for individual stocks than for index futures such as the E-mini, it nevertheless merits considera-
tion. However, closer examination indeed con(cid:28)rms that the order-splitting story is not a viable
explanation of the empirical results.
Therearethreemaintypesoforder-splittingtoconsider,twoofwhichcanbereadilydismissed.
First, an A-HFT might split one large order into a near-instantaneous salvo of small orders(cid:22)e.g.,
submit5001-contract orders in amillisecond. Ifall of these child-orders were large, or if theywere
all small (relative to q¯), then they would not show up in my results, since I look at the market
response to small aggressive orders, and the explained characteristics of larger orders. A second
type of order-splitting that would appear in my results would be a salvo of alternating/mixed
large and small orders. However, if an A-HFT actually did this kind of splitting and submitted all
of the orders almost instantaneously, there would be essentially no chance that the resting depth
would further deplete in the minuscule intervals between the arrival of these child orders. During
my sample period, latency (the amount of time required for messages to be processed and pass
37

backandforthbetweenatraderandthemarket)wasseveralmillisecondsintheE-minimarket, so
any further depletion in depth during an one- or two- millisecond salvo of orders almost certainly
could not be a response to those orders, and hence almost certainly would not be an indication
that those orders were informed.
The (cid:28)nal type of order-splitting to consider cannot be so easily ruled out as an explanation.
An A-HFT might split orders into small and large child orders, and submit them at each at least
severalmillisecondsapart, suchthatdepthdepletionfollowingthesmalloneswouldindeedappear
inthedata. Sloworder-splittingofthattype, though, necessarilyimpliesthattheA-HFTspossess
private information which they do not trade on as quickly as they are able. This story leads to the
same fundamental implication as the exploratory trading explanation, namely that the A-HFTs
obtain some of their superior information through some channel other than merely reacting to
public information faster than everyone else.
The slow-order-splitting story isn’t quite observationally equivalent to the exploratory trading
theory. In its simplest form, the order-splitting story would imply that the market response to an
A-HFT’s small aggressive order will only help to explain the A-HFT’s earnings on a subsequent
large aggressive order if both the small order and the large order have the same sign. The ex-
ploratory trading theory predicts that the market response to the small order will help to explain
earnings on the large order, regardless of whether the two orders have the same sign. Consis-
tent with the exploratory trading theory, and in contradiction to the slow-order-splitting story,
the results in this section do not change qualitatively when we restrict attention to the market
response to an A-HFT’s last small aggressive order with the opposite sign from the present order.
Furthermore, as the simulated trading strategy results in the next section will suggest, the market
response to an A-HFT’s small aggressive order can be used to better forecast the performance of
a subsequent aggressive order in either direction.
6 Practical signi(cid:28)cance of exploratory information
The empirical evidence in Section 5 provides strong support for the hypothesis that the A-HFTs
engage in exploratory trading as modeled in Section 2. However, while these results suggest that
exploratory trading plays some part in how A-HFTs obtain the superior information that enables
38

them to pro(cid:28)t from their aggressive orders, the results tell us little about how large that part is.
Estimates of the additional component of the A-HFTs’ aggressive-order earnings directly ex-
plainedbytheprivateinformationinΩA arelikelytodramaticallyunderstatethetruecontribution
of exploratory information, for two reasons. First, ΩA is nearly the simplest possible characteri-
zation of exploratory information. Representations of exploratory information richer than ΩA are
extremely easy to construct. For example, an obvious extension would be to consider the not only
thesign,butalsothemagnitude ofthedirection-normalizeddepthchangefollowinganexploratory
order. Regardless of the particular representation of exploratory information used, though, the
additional explained component of A-HFTs’ pro(cid:28)ts on the aggressive orders they place is likely
to understate the true gains from exploration. As the simple model from Section 2 illustrates,
exploratory information is valuable in large part because it enables a trader to avoid placing un-
pro(cid:28)table aggressive orders. However, estimates of the additional explained component of pro(cid:28)ts
on A-HFTs’ aggressive orders necessarily omit the e(cid:27)ects of such avoided losses. While this bias,
if anything, makes the preceding (cid:28)ndings of statistical signi(cid:28)cance all the more compelling, it also
complicates the task of properly determining the practical importance of exploratory information.
6.1 Simulated trading strategies
To investigate the gains from exploratory information, including the gains from avoiding unprof-
itable aggressive orders, I examine the e(cid:27)ects of incorporating market-response information from
smallaggressiveordersintosimulatedtradingstrategies. Thekeyadvantageofworkingwiththese
simulatedtradingstrategiesisthatavoidedunpro(cid:28)tableaggressiveorderscanbeobserveddirectly.
The basic trading strategy that I consider is a simple adaptation of the benchmark regression
from Section 5.2. I specify a threshold value, and the strategy entails nothing more than placing
an aggressive order with the same sign as yˆ whenever |yˆ| exceeds that threshold. To make
k k
this strategy feasible (in the sense of using only information available before time t to determine
the time-t action) I compute the forecast of the future price movement, yˆ, using the regression
k
coe(cid:30)cients estimated from the previous day’s data. I incorporate market-response information
into this strategy by modifying the rule for placing aggressive orders to, (cid:16)place an aggressive order
(with the same sign as yˆ) if and only if all three of the following conditions hold:
k
39

• |yˆ| exceeds its speci(cid:28)ed threshold,
k
• The direction-normalized depth-change following the last small aggressive order (placed by
anyone) exceeds a speci(cid:28)ed threshold, and
• The direction-normalized depth-change following the last small aggressive order placed by an
A-HFT exceeds a (possibly di(cid:27)erent) speci(cid:28)ed threshold.(cid:17)
Choosing a threshold of −∞ will e(cid:27)ectively remove any of these conditions.
Each strategy yields a set of times to place aggressive orders, and the associated direction for
each order. To measure the performance of a given strategy, I compute the average pro(cid:28)tability
of the indicated orders in the usual manner, with the assumption that these aggressive orders are
all of a uniform size.
Relative to A-HFTs’ losses on small aggressive orders, the additional component of A-HFTs’
pro(cid:28)ts directly explained using ΩA is smallest when q¯= 10, and I present results for q¯= 10 to
highlight the impact of accounting for avoided losses on estimates of the gains from exploratory
information. Results for other values of q¯are similar.
6.2 Three speci(cid:28)c strategies
All three threshold parameters a(cid:27)ect strategy performance, so to emphasize the role of market-
responseinformation, Ipresentresultswiththethresholdfor|yˆ|held(cid:28)xed. Varyingthethreshold
k
for |yˆ | does not alter the qualitative results. In particular, it is not possible by merely raising
k
the threshold for |yˆ | to achieve the same gains in performance that arise from incorporating
k
exploratory information. The forecast yˆ uses coe(cid:30)cients estimated from the previous day’s data,
k
and these forecasts exhibit increasing bias as the z observations assume more extreme values.
k−1
I consider a range of threshold values for the direction-normalized depth-change following the
last small aggressive order placed by anyone, but, for expositional clarity, I present results for
three illustrative threshold choices for the direction-normalized depth-change following the last
small aggressive order placed by an A-HFT. Speci(cid:28)cally, I consider thresholds of −∞ (no A-
HFT market-response information), 0 (the same information contained in ΩA), and 417 (the 99th
percentile value). Figure 4 displays the performance of these three strategies over a range of
40

Figure 4: ExploratoFrigyurIen 6f.o Armbsoaltuitoe nGaIimns pfrroomv eEsxpPloerraftoorrym InafnorcmeaotiofnSimulated Strategies
8.25
8.00
7.75
7.50
7.25
7.00
6.75
6.50
6.25
6.00
50% 55% 60% 65% 70% 75% 80% 85% 90% 95% 100%
Percentile Cutoff for Depth-Change Following Last Small Aggressive Order by Anyone
)sralloD(
tcartnoC
rep
sgninraE
ssorG
.gvA
No A-HFT Info A-HFT DC>0 A-HFT DC>99th %tile
Figure 4 displays the estimated average gross earnings per aggressively traded contract for the three simulated
trading strategies. The starting point for all three trading strategies is a simple linear forecast of the future price-
change,callityˆ,usingthesamelaggedmarketvariablesasinthebaselineregression,equation(10)(i.e.,signsand
signed quantities of the last four aggressive orders, and one lag of the changes in resting depth at prices within
two ticks of the best bid and ask). The strategies also involve the change in resting depth following the last small
aggressive order placed by anyone (normalized by the direction of that order), and similarly, the depth-change
following the last small aggressive order placed by any A-HFT (again, normalized by that order’s direction). The
trading rule is to place an aggressive order with the same sign as yˆwhenever |yˆ|, and both depth-changes exceed
their respective speci(cid:28)ed thresholds.
The three strategies di(cid:27)er in the threshold value for direction-normalized depth-change following the last small
aggressiveorderplacedbyanA-HFTthatmustbesatis(cid:28)edinorderforthestrategytoenteratrade,aslabeledin
the (cid:28)gure. The threshold value for |yˆ| is held (cid:28)xed, and the horizontal axis is the threshold value (in percentiles)
for the direction-normalized depth-change following arbitrary small aggressive orders.
threshold values for the market response following arbitrary small aggressive orders.
While the performance gains from incorporating A-HFT exploratory information are obvious,
an equally important feature of the results above is more subtle. The A-HFTs’ average gross
earningsonaggressiveordersoversize10of$7.78percontractarewellabovethepeakperformance
of the strategy that uses only public information, but substantially below the performance of the
strategy that incorporates the A-HFTs’ exploratory information with the higher threshold. This
is exactly the pattern that we should expect, given that the former strategy excludes information
thatisavailabletotheA-HFTsandthelatterstrategyincludesinformationthatisnotavailableto
anyindividualA-HFT,sotheseresultshelptocon(cid:28)rmtherelevanceandvalidityofthissimulation
methodology.
41

6.2.1 Gains from exploration relative to losses on exploratory orders
Although the two strategies that incorporate exploratory information from the A-HFTs’ small
aggressive orders outperform the strategy that does not, the orders that generated the exploratory
information were costly. To compare the gains from this exploratory information to the costs of
acquiringit,I(cid:28)rstmultiplytheincreasesinper-contractearningsforthetwoexploratorystrategies
(scaled by the respective number of orders relative to the public-information strategy) by the A-
HFTs’ combined aggressive volume on orders over size 10.16 I then divide these calibrated gains
by the A-HFTs’ actual losses on aggressive orders size 10 and under.
Figure 5 displays the calibrated ratio of additional gains to losses for each exploratory simu-
lated strategy over a range of threshold values for the market response following arbitrary small
aggressive orders. Using information from the A-HFTs’ exploratory orders analogous to that in
ΩA, the additional gains are roughly 15% larger than the losses on exploratory orders. Whereas
the extra component of the A-HFTs’ performance directly explained using ΩA represents less than
5% of A-HFTs’ losses on exploratory orders, the analogous estimated performance increases more
thano(cid:27)setthecostsofexplorationonceweincludethegainsfromavoidingunpro(cid:28)tableaggressive
orders. In the case of the strategy that employs information from the A-HFTs’ exploratory orders
with the higher threshold, the estimated gains from exploration exceed the costs by more than
one-third.
Even after netting out the calibrated losses on exploratory orders from the better-performing
exploratory-information simulated strategy in 6.2, the simulated performance exceeds the maxi-
mum pro(cid:28)tability hurdle among HFTs of $6.41 per aggressively traded contract. An almost trivial
trading strategy that incorporates exploratory trading appears to be pro(cid:28)table, suggesting very
stronglythatexploratorytradingisatleastsu(cid:30)cienttoexplainhowatraderintheE-minimarket
could predict price-movements with accuracy adequate to consistently pro(cid:28)t on average from her
aggressive orders.
16The two strategies that incorporate exploratory information select subsets of the aggressive order placement
times generated by the public-information-only strategy. Although the selected orders tend to be more pro(cid:28)table,
they are also fewer in number.
42

Figure 7. Gains from A-HFT Exploratory Info Relative to Losses on Exploratory Orders
Figure 5: Gains from A-HFT Exploratory Info Relative to Losses on Exploratory Orders
1.6
1.5
1.4
1.3
1.2
1.1
1.0
50% 55% 60% 65% 70% 75% 80% 85% 90% 95% 100%
Percentile Cutoff for Depth-Change Following Last Small Aggressive Order by Anyone
sessoL
ot
sniaG
artxE
fo
oitaR
A-HFT DC>0 A-HFT DC>99th %tile
Figure5displaysthecalibratedratioofadditionalgainstolossesforthetwoexploratorysimulatedstrategiesacross
a range of threshold values (in percentiles) for the market response following arbitrary small aggressive orders.
7 Discussion
7.1 Broader opportunities for exploratory gains from aggressive orders
The empirical analysis in the preceding sections focused on the information generated by the A-
HFTs’ smallest aggressive orders. While these orders were the most natural starting point for
an empirical study of exploratory trading, there is no theoretical reason why these small orders
should be the sole source of exploratory information. In the baseline exploratory trading model, it
was only to highlight the key aspects of the model that I assumed the HFT’s period-1 order was
expected to lose money and served no purpose other than exploration.
In principle, even aggressive orders that an A-HFT expects to be directly pro(cid:28)table could
produce valuable, private, exploratory information. To investigate this possibility, I repeat the
analysis of Section 5.3 setting q¯ = 25,30,35,40,45,50,60,75,90. The A-HFTs’ incremental ag-
gressive orders included with each increase of q¯beyond q¯= 20 are directly pro(cid:28)table on average,
and yet the market response following these orders still provides signi(cid:28)cantly more additional ex-
planatory power for the A-HFTs’ performance on larger aggressive orders than it provides for that
of other traders. See Figure 6, and see Table 4 for numeric results.
These results have the interesting implication that the A-HFTs enjoy natural and almost
inevitable economies of scale(cid:22)simply by being in the market and engaging in lots of aggressive
43

Figure 8. [A-HFT Addt'l Explained] - [Everyone Else Addt'l Explained] (95% Conf. Bands)
Figure 6: Di(cid:27)erence in Additional Earnings Explained by Exploratory Information
1.2
1
0.8
0.6
0.4
0.2
0
0 10 20 30 40 50 60 70 80 90 100
q-Bar
tcartnoC
rep
stneC
Figure6isjustanextendedversionofFigure2,extendedtolargervaluesofq¯. Itdepictsthedi(cid:27)erenceforA-HFTs
vs. for everyone else of the additional earnings per contract explained by exploratory information. For a given
A-HFT,andthecorresponding(cid:16)everyoneelse,(cid:17) I(cid:28)ndtheadditionalearningspercontractexplainedby(12)beyond
what is explained by (11), and I compute the di(cid:27)erence between the average for the A-HFT, and the average for
everyone else. Estimates were run for each individual A-HFT, and the displayed solid line displays cross-sectional
averages of these individual estimates (with 95% con(cid:28)dence bands in dotted lines). The horizontal axis speci(cid:28)es
the cuto(cid:27), q¯, for the maximum size of order de(cid:28)ned to be (cid:16)small(cid:17) when estimating (12) and (11).
44

noitamrofnI
yrotarolpxE
yb
denialpxE
sgninraE
lanoitiddA
:4
elbaT
.
)slavretni
ecned(cid:28)noc
%59
htiw
,tcartnoc
rep
tnec
a
fo
shtderdnuh
ni
detropeR(
09=¯q
57=¯q
06=¯q
05=¯q
54=¯q
04=¯q
53=¯q
03=¯q
52=¯q
0.21
1.71
8.12
9.91
2.61
2.61
3.41
7.41
5.71
srehtOllA
)7.81,3.5(
)0.32,2.11(
)2.72,2.61(
)3.52,5.41(
)5.02,9.11(
)5.02,0.21(
)4.81,6.01(
)2.81,6.01(
)3.12,5.31(
0.401
3.701
1.811
3.001
0.58
0.58
3.37
7.96
4.26
sTFH-A
)2.421,1.28(
)3.921,0.68(
)1.831,5.89(
)9.121,0.18(
)3.501,9.56(
)7.301,6.46(
)0.29,1.55(
)4.98,0.25(
)6.08,7.34(
0.29
2.09
4.69
4.08
8.86
8.86
0.95
1.55
0.54
.svTFH-A
)1.511,5.86(
)8.211,7.86(
)2.711,5.57(
)9.101,9.95(
)6.98,2.94(
)6.78,3.84(
)1.87,6.04(
)0.57,0.73(
)9.36,2.62(
srehtOllA
6.47
7.57
6.87
3.46
0.65
0.85
9.84
4.54
0.63
.svTFH-A
)1.99,8.94(
)3.001,5.35(
)2.99,2.65(
)1.78,5.34(
)6.77,4.53(
)9.77,2.63(
)4.86,9.92(
)0.66,2.72(
)4.55,1.71(
sTFHrehtO
no
tcartnoc
rep
sgninrae
ssorg
lanoitidda
detamitse
eht
fo
segareva
lanoitces-ssorc
suoirav
stneserp
elbat
ehT
.¯q
fo
seulav
erom
rof
2
elbaT
sdnetxe
4
elbaT
ehtsetoned
(cid:17)srehtOllA
.svTFH-A(cid:16)
.)11(noissergerybdenialpxetahtfossecxeni)21(noissergerybdenialpxe¯qnahtretaergezisdettimbusfosredroevissergga
setoned
(cid:17)sTFHrehtO
.svTFH-A(cid:16);sTFH-Aehtssorcadegareva,sredartrehtollarofesohtsunimTFH-Anevigaroftcartnocrepsgninraedenialpxelanoitidda
rehtO(cid:16)
dna
(cid:17)srehtO
llA(cid:16)
fo
pihsrebmem
ehT
.sTFH-A
laudividni
rof
setamitse
eht
revo
segareva
era
sTFH-A
eht
rof
detroper
srebmuN
.ytitnauq
suogolana
na
ot
gnidnopserroc
spuorg
tnere(cid:27)id
ylthgils
eht
ssorca
nekat
segareva
era
srebmun
detroper
eht
dna
,dedulcxe
gnieb
TFH-A
ralucitrap
eht
nopu
sdneped
(cid:17)sTFH
.sTFH-A
rehto
eht
sedulcni
(cid:17)sTFH
rehto(cid:16)
taht
etoN
.sTFH-A
laudividni
eht
fo
hcae
detsefinam)noitaredisnocrednuTFH-Aehtotelbaliava(noitamrofnifotnenopmocetavirpehtmorfnoitubirtnocehtstce(cid:29)er)21(forewopyrotanalpxeartxeehT )noitatcepxeni(emasehtsimodeerffoseergedartxeehtmorftce(cid:27)eehtecniS
.)11(otevitaler)21(nimodeerffoseergedartxeehtfotce(cid:27)eehtsallewsa,AΩni
TFH-Ananeewtebro,sredartrehtolladnaTFH-Ananeewtebtcartnocrepsgninraedenialpxelanoitiddani
ecnere(cid:27)idehtnotcapmionsahti,sredartllarof
.sTFH
rehto
lla
dna
45

trading, they automatically generate lots of valuable, private information. Other, more obvious
economies of scale and scope likely exist for high-frequency traders (e.g., tiered trading costs,
applicabilityofsimilaralgorithmsacrossdi(cid:27)erentmarkets),buttheeconomiesofscalearisingfrom
exploratory information appear to be new. The impressive performance of the extremely simple
simulated strategies in Section 6 casts doubt on the standard fallback of (cid:16)intellectual capital(cid:17) as a
barriertoentry. AlthoughtheA-HFTsearnpositivepro(cid:28)tsonaverage, theirmarginalpro(cid:28)tsneed
not be strictly positive, so there may be no incentive for new A-HFTs to enter. However, should
the structure of the A-HFT industry indicate the existence of some barriers to entry, the A-HFTs’
apparent economies of scale could potentially act as one such barrier. Industrial organization of
high-frequency trading entities is an intriguing open area for future investigation, but detailed
treatment lies beyond the scope of this paper.
7.2 Speed and exploratory trading
Evidence in this paper provides empirical justi(cid:28)cation for using the exploratory trading model
to draw conclusions about real-world high-frequency trading. Further analysis of the exploratory
trading model reveals natural connections between exploration and two important concepts of
speed. These connections in turn help to illuminate the role that the two types of speed play in
high-frequency trading. More importantly, although questions of speed arise most commonly in
the context of high-frequency trading, the implications below are applicable much more broadly.
7.2.1 Low latency
One common measure of trading speed is latency(cid:22)the amount of time required for messages to be
processed and pass back and forth between a trader and the market. While low-latency operation
and high-frequency trading are not equivalent, minimal latency is nonetheless a hallmark of high-
frequency traders. HFTs can certainly react and communicate faster than some other market
participants,butanalogousdi(cid:27)erencesintherelative reactionspeedofvarioustraderslongpredate
high-frequency trading. For a trader who can identify pro(cid:28)table trading opportunities, there is
obvious value to possessing latency low enough to take advantage of these opportunities before
they disappear. The new insight from the exploratory trading model concerns the more subtle
46

matter of how low latency connects to the identi(cid:28)cation of such opportunities, that is, why it
might matter for latency to be low in absolute terms.
In the model of exploratory trading developed in Section 2, the HFT’s inference about the
liquiditystate,Λ,onthebasisofmarketactivityfollowinghisaggressiveorderinperiod1implicitly
depends on a notion related to latency. If we suppose that random noise perturbs the order
book, say according to a Poisson arrival process, then the amount of noise present in the HFT’s
observation of the market response in some interval following his aggressive order will depend on
the duration of that interval. The duration of this interval will depend in large part upon the rate
at which market data is collected and disseminated to the HFT, that is, the (cid:16)temporal resolution(cid:17)
of the HFT’s data. Although this temporal resolution does not directly depend on the HFT’s
latency, the temporal resolution of the HFT’s market information does implicitly constrain how
quickly the HFT can learn about market events.
The (cid:28)ner temporal resolution required for low-latency operation enables low-latency traders to
obtainmeaningful(cid:22)andempiricallyvaluable(cid:22)informationaboutthemarketactivityimmediately
following their aggressive orders, and this information degrades at coarser temporal resolutions.
The empirical results from Section 5.3.4 provide a concrete illustration of this e(cid:27)ect. The changes
in resting depth immediately following an arbitrary aggressive order are less useful for forecasting
price movements than are the analogous changes following an A-HFT’s aggressive order, but
the two can only be distinguished (by the A-HFT) in data with a su(cid:30)cient level of temporal
disaggregation.
7.2.2 High frequency
Exploratory trading bears a natural relationship to the practice of placing large numbers of ag-
gressive orders(cid:22)what might be considered (cid:16)high-frequency trading(cid:17) in the most literal sense.
Any exploratory information generated by a given aggressive order is only valuable to the
extent that it can be used to improve subsequent trading performance. Because exploratory
information remains relevant for only some (cid:28)nite period, the value of exploratory information
diminishes as the average interval between a trader’s orders lengthens. The exploratory trading
model readily captures this e(cid:27)ect if we relax the simplifying assumption that the liquidity state
47

Λ remains the same between periods 1 and 2. Suppose that Λ evolves according to a Markov
process, such that with probability τ, a second Λ is drawn in period 2 (from the same distribution
as in period 1), and with probability 1−τ, the original value from period 1 persists in period 2.
Intuitively, τ parametrizes the length of period 1, and this length increases from zero to in(cid:28)nity as
τ increasesfromzerotounity. Asτ tendstowardsunity(cid:22)i.e.,asthelengthofperiod1increasesto
in(cid:28)nity(cid:22)the liquidity state in period 1 becomes progressively less informative about the liquidity
state in period 2.
AsdiscussedinSection7.1,boththeoryandempiricalevidencesuggestthatalmostanyaggres-
sive order that a trader places generates some amount of exploratory information. Consequently,
as a trader places aggressive orders in greater numbers, he will gain access to greater amounts
of exploratory information. Furthermore, the average time interval between a trader’s aggressive
orders necessarily shrinks as the number of those orders grows, so the exploratory information
produced by each order tends to become more valuable to the trader. These synergistic e(cid:27)ects
dramatically magnify the potential gains from exploratory information for traders who place large
numbers of aggressive orders.
8 Conclusion
This paper presents empirical evidence that HFTs use exploratory trading to obtain part of the
superiorinformationthatenablesthem,amongotherthings,topro(cid:28)tablypredictpricemovements.
In particular, these results demonstrate that HFTs do not obtain their informational advantage
purely by reacting to public information milliseconds or microseconds sooner than other traders.
Speed matters immensely, but by no means does it matter exclusively.
The theory of exploratory trading introduced in this paper sheds light on a number of issues
related to HFTs, but it leaves many standing questions unresolved, and indeed, it raises several
new questions. For example, exploratory trading could be considered a form of costly information
acquisition (albeit an unusual one) which raises at least the possibility that HFTs uniquely con-
tribute to the process of e(cid:30)cient price discovery. However, unlike traditional costly information
acquisition, exploratory trading does not generate information that relates directly to the traded
asset’s fundamental value, but that pertains rather to unobservable aspects of market conditions
48

thatcouldeventuallybecomepublic, ex-post, throughordinarymarketinteractions. Furthermore,
because exploratory trading operates through the market mechanism itself, exploration exerts di-
recte(cid:27)ectsonthemarket, distinctfromthesubsequente(cid:27)ectsoftheinformationthatitgenerates.
Comprehensive analysis of the myriad theoretical and empirical aspects of such issues lies beyond
the scope of this paper, but the theory and evidence presented herein provide a starting point
from which to more rigorously address the market-quality implications of high-frequency trading
going forward.
49

A Exploratory trading model details
This appendix presents the full details of solving the models of Section 2.
A.1 Solving the baseline exploratory trading model (leading case)
A.1.1 Solving for the HFT’s optimal trading strategy
When α > u, the HFT will never place an order in period 2 if he doesn’t know the liquidity state,
and I focus on this case initially to provide a more intuitive exposition; results are qualitatively
unchanged for u ≥ α, but for completeness, I analyze the general case in the next subsection.
I solve for the HFT’s optimal trading strategy via backward induction.
Period 2 If the HFT learned the liquidity state during period 1, his optimal aggressive order in
period 2 will depend on the values of both ϕ and Λ. The HFT’s optimal strategy when he knows
Λ is to set q = ϕN if Λ = U, and to set q = 0 if Λ = A . Taking expectations with respect to ϕ
2 2
and then Λ, we (cid:28)nd
E[π |Λ known] = Nv(1−α)∗u+0∗(1−u) (14)
2
= Nvu(1−α)
IftheHFTdidnotlearntheliquiditystateduringperiod1,his(constrained)optimalaggressive
order in period 2 will still depend on the value of ϕ, but it will only depend on the distribution of
Λ, rather that the actual value of Λ. The HFT’s optimal strategy when he does not know Λ is to
set q = ϕN when u ≥ α, and to set q = 0 when α > u. I assumed for simplicity that α > u, so
2 2
E[π |Λ unknown] = 0 (15)
2
Period 1 Atthestartofperiod1, theHFTknowsneitherϕnorΛ,buthefacesthesametrading
costs (α per contract) as in period 2. Consequently, the HFT’s expected direct trading pro(cid:28)ts
from a period-1 aggressive order are negative, given by
E[π ] = −α|q | (16)
1 1
50

Since there is no noise in this baseline model, and the HFT learns Λ perfectly from any aggressive
orderthatheplacesinthe(cid:28)rstperiod, wecanrestrictattentiontothecasesofq = 0and|q | = 1.
1 1
We obtain the following expression for the di(cid:27)erence in the HFT’s total expected pro(cid:28)ts if he
sets |q | = 1 instead of q = 0:
1 1
E[π ||q | = 1]−E[π |q = 0] = Nvu(1−α)−α (17)
total 1 total 1
The HFT engages in exploratory trading if he sets |q | = 1, and he does not engage in exploratory
1
trading if he sets q = 0, so equation (17) represents the expected net gain from exploration.
1
Exploratory trading is optimal for the HFT when this expected net gain is positive.
A.2 Solving the baseline exploratory trading model (general case)
Let s denote the sign of q .
t t
A.2.1 Solving the model: period 2
Ifϕ = 0, theHFT’soptimalchoiceistonotsubmitanaggressiveorderinperiod2, orequivalently,
to set |q | = 0. If ϕ (cid:54)= 0, then it is optimal for the HFT to set s = ϕ (unless the optimal |q | is
2 2 2
zero), so we only need to determine the optimal magnitude, |q | . Because π is linear in |q | when
2 2 2
s is held (cid:28)xed, we can restrict attention to corner solutions (0 or N) for the optimal choice of |q |
2 2
without loss of generality. Note that if q = 0, then π = 0, regardless of the values of ϕ and Λ.
2 2
Suppose that the HFT sets |q | = N. Without loss of generality, assume that s = ϕ (cid:54)= 0. The
2 2
HFT’s period-2 pro(cid:28)ts are given by


 N (1−α) if Λ = U
π˜ = (18)
2

 −Nα if Λ = A
where the tilde on π˜ denotes the fact that the HFT’s choice of q does not condition on the value
2 2
of Λ.
51

HFT does not know Λ IftheHFTdoesnotknowthevalueofΛ, theninthecasewhereϕ (cid:54)= 0,
the HFT’s expected period-2 pro(cid:28)t if he sets |q | = N is
2
E[π˜|ϕ (cid:54)= 0,|q | = N] = uN (1−α)−(1−u)Nα (19)
2 2
= (u−α)N
Taking expectations with respect to ϕ, we (cid:28)nd that the ex-ante expectation of π˜ when the HFT
2
sets |q | = N (and s = ϕ) is given by
2 2
E[π˜||q | = N] = v(u−α)N (20)
2 2
When u−α < 0, if the HFT did not know Λ, he would set q = 0 rather than |q | = N. Hence
2 2
the ex-ante expectation of π˜ is
2
E[π˜] = max{v(u−α)N,0} (21)
2
HFT knows Λ Next, if the HFT does know the value of Λ, then he will set |q | = N (and
2
s = ϕ) only when Λ = U and ϕ (cid:54)= 0. Denoting the HFT’s period-2 pro(cid:28)ts from this strategy by
2
πˆ, we (cid:28)nd
2
E[πˆ|ϕ (cid:54)= 0] = u(1−α)N (22)
2
= (u−α)N +α(1−u)N
E[πˆ] = vu(1−α)N (23)
2
= v(u−α)N +vα(1−u)N
Note that
E[πˆ] > max{v(u−α)N,0} (24)
2
so the HFT’s expected period-2 pro(cid:28)ts are strictly greater when he knows Λ than when he doesn’t
know Λ.
52

A.2.2 Solving the model: period 1
At the start of period 1, the HFT knows neither ϕ nor Λ, but he faces the same trading costs, α,
as he does in period 2. Consequently, the HFT’s expected direct trading pro(cid:28)ts from a period-1
aggressive order are negative:
E[π |q ] = E[|q |(s y−α)|s ,q ] (25)
1 1 1 1 1 1
= |q |s E[y]−α|q |
1 1 1
= −α|q |
1
The second equality relies on the assumptions that ϕ and Λ (and hence y) are independent of s
1
and q , while the (cid:28)nal equality uses the fact that E[y] = 0.
1
Since there is no noise in this baseline model, the HFT learns Λ perfectly from any aggressive
order that he places in the (cid:28)rst period with |q | ≥ 1. An aggressive order of size greater than one
1
yields no more information about Λ than a one-contract aggressive order in this setting, but the
larger aggressive order incurs additional expected losses. Thus without loss of generality, we can
restrict attention to the case of q = 0 and the case of |q | = 1.
1 1
If the HFT sets q = 0, he neither learns Λ nor incurs any direct losses in period 1, so his total
1
expected pro(cid:28)ts are simply
E[π |q = 0] = E[π˜] (26)
total 1 2
= max{v(u−α)N,0}
Alternatively, if the HFT sets |q | = 1, his total expected pro(cid:28)ts are given by
1
E[π ||q | = 1] = −α|q |+E[πˆ] (27)
total 1 1 2
= vu(1−α)N −α
53

A.2.3 Comparative statics for model parameters
Recallthatwhentheexogenousaggressiveorder-(cid:29)owisdescribedbyϕ = 0,theHFTdoesnothave
any pro(cid:28)table period-2 trading opportunities in either liquidity state. The probability that ϕ (cid:54)= 0,
given by the parameter v, represents the extent to which the exogenous aggressive order-(cid:29)ow is
predictable. To characterize how various parameters a(cid:27)ect the viability of exploratory trading, I
consider the minimal value of v for which the HFT (cid:28)nds it optimal to engage in period-1 (i.e.,
exploratory) trading. Denoting this minimal value by v, we have
(cid:16)α(cid:17) 1
v = (28)
u (1−α)N
The closer is v to 0, the more conducive are conditions to exploratory trading, and by inspection,
∂v > 0, ∂v < 0 and ∂v < 0.
∂α ∂N ∂u
The above results are intuitive. First, higher trading costs (α) tend to discourage exploratory
trading. Second, when the HFT can use exploratory information to guide larger orders, the gains
fromexplorationaremagni(cid:28)ed, solargervaluesofN tendtopromoteexploratorytrading. Finally
exploratory trading becomes less viable when u is smaller. The HFT will take the same action in
period 2 when he knows that Λ = A as when he doesn’t know Λ, so when u is small, knowledge of
the liquidity state is less valuable because it is less likely to change the HFT’s period-2 actions.17
A.3 Solving the model of Section 2.4
A.3.1 Formalizing the intuitive argument
To make more rigorous the intuitive explanation of why the HFT could learn from the market
response to his own orders than he could from the market response to an order placed by someone
else,consideravariantofthebaselinemodelfromSection2.2,inwhichnowsomeoneotherthanthe
HFT places an aggressive order at the beginning of period 1. With probability ρ, this aggressive
order is the result of an unobservable informational shock, and resting depth further depletes
following the order, regardless of the liquidity state Λ. Otherwise (with probability 1−ρ) resting
17When u > α, the HFT will take the same action in period 2 when he knows that Λ = U as when he doesn’t
know Λ, so knowledge of the liquidity state is less likely to change the HFT’s period-2 actions when u is large. In
the case of u > α, equation (28) becomes v = 1 , and exploratory trading indeed becomes less viable as u
(1−u)N
approaches 1.
54

depth further depletes after the order if and only if the liquidity state is unaccommodating. Aside
from this new aggressive order, all other aspects of the baseline model remain unchanged.
If the HFT places an aggressive order in period 1, his expected total pro(cid:28)ts are the same as
they were in the baseline model, i.e.,
E[π ||q | = 1] = Nvu(1−α)−α (29)
total 1
However, the HFT’s expected pro(cid:28)ts if he does not place an order in period 1 are now higher
than they were in the baseline model, because the HFT learns something from the depth changes
following the other trader’s aggressive order. If resting depth weakly replenishes after that order,
the HFT learns with certainty that the liquidity state is accommodating (i.e., Λ = A), so the HFT
will not submit an aggressive order in period 2, and his total pro(cid:28)ts will be zero. Alternatively, if
resting depth further depletes following the aggressive order in period 1 (denote this event by g ),
1
we have
P{Λ = U, and g }
P{Λ = U|g } = 1 (30)
1 P{g }
1
P{g |Λ = U}P{Λ = U}
1
=
P{g |Λ = U}P{Λ = U}+P{g |Λ = A}P{Λ = A}
1 1
1∗P{Λ = U}
=
1∗P{Λ = U}+ρ∗P{Λ = A}
u
= (31)
u+ρ(1−u)
The HFT’s optimal strategy when he does not know Λ is to set q = ϕN when u ≥ α, and
2 u+ρ(1−u)
to set q = 0 otherwise. Taking expectations with respect to Λ and ϕ, we (cid:28)nd that the HFT’s
2
ex-ante expected total pro(cid:28)ts in this case are given by
(cid:26) (cid:18) (cid:19) (cid:27)
u
E[π |AO by someone else] = max Nv −α ,0 (32)
total
u+ρ(1−u)
The features of the baseline model discussed in Section 2.3 are qualitatively unchanged in the
modi(cid:28)ed version, but now the (cid:16)privacy(cid:17) parameter ρ also exerts an in(cid:29)uence. In the limiting
55

case where the depth change following an aggressive order placed by someone else is completely
uninformative to the HFT (i.e., ρ = 1), equation (32) collapses down to equation (15) from the
baseline model. At the opposite extreme, when the HFT learns the liquidity state perfectly from
observing another trader’s aggressive order (i.e., ρ = 0), the HFT’s expected total pro(cid:28)ts are
unambiguously lower if he places an aggressive order in period 1 himself. When the HFT can
learn more about the liquidity state through mere observation, as he can when ρ is smaller, he has
less incentive to incur the direct costs of exploratory trading.
56

References
[1] Anat R. Admati and Paul P(cid:29)eiderer. A theory of intraday trading patterns: Volume and
price variability. Review of Financial Studies, 1:3(cid:21)40, 1988.
[2] Matthew Baron, Jonathan Brogaard, and Andrei Kirilenko. The trading pro(cid:28)ts of high
frequency traders. September 2013.
[3] BrunoBiais,ThierryFoucault,andSophieMoinas. Equilibriumalgorithmictrading. Working
Paper, October 2010.
[4] Bruno Biais, Pierre Hillion, and Chester Spatt. An empirical analysis of the limit order book
and the order (cid:29)ow in the paris bourse. The Journal of Finance,, 50(5):1655(cid:21)1689, 1995.
[5] Jonathan Brogaard, Terrence Hendershott, and Ryan Riordan. High frequency trading and
price discovery. April 2013.
[6] EricBudish,PeterCramton,andJohnShim. Thehigh-frequencytradingarmsrace: Frequent
batch auctions as a market design response. Chicago Booth Working Paper, December 2013.
[7] Alfonso Dufour and Robert F. Engle. Time and the price impact of a trade. The Journal of
Finance, 55(6):2467(cid:21)2498, December 2000.
[8] David Easley and Maureen O’Hara. Time and the process of security price adjustment.
Journal of Finance, 47:577(cid:21)605, 1992.
[9] Andrew Ellul, Craig W. Holden, Pankaj Jain, and Robert Jennings. Order dynamics: Recent
evidence from the nyse. Journal of Empirical Finance, 14:636(cid:21)661, 2007.
[10] Robert F. Engle and Je(cid:27)rey R. Russell. Autoregressive conditional duration: A new model
for irregularly spaced transaction data. Econometrica, 66(5):1127(cid:21)1162, September 1998.
[11] ThierryFoucault,JohanHombert,andIoanidRosu. Newstradingandspeed. WorkingPaper,
May 2013.
57

[12] Lawrence R. Glosten and Paul R. Milgrom. Bid, ask and transaction prices in a specialist
market with heterogeneously informed traders. Journal of Financial Economics, 14:71(cid:21)100,
1985.
[13] Sanford J. Grossman and Merton H. Miller. Liquidity and market structure. The Journal of
Finance, 43(3), July 1988.
[14] Bjorn Hagstromer and Lars Norden. The diversity of high-frequency traders. Journal of
Financial Markets, 16(4):741(cid:21)770, 2013.
[15] Joel Hasbrouck. Measuring the information content of stock trades. The Journal of Finance,
XLVI(1), March 1991.
[16] BoyanJovanovicandAlbertJ.Menkveld. Middlemeninlimit-ordermarkets. WorkingPaper,
November 2012.
[17] Andrei Kirilenko, Mehrdad Samadi, Albert S. Kyle, and Tugkan Tuzun. The (cid:29)ash crash: The
impact of high frequency trading on an electronic market. October 2010.
[18] J.Chris Leach and Ananth N Madhavan. Intertemporal price discovery by market makers:
Activeversuspassivelearning. Journal of Financial Intermediation,2(2):Pages207(cid:21)235,June
1992.
[19] J.Chris Leach and Ananth N. Madhavan. Price experimentation and security market struc-
ture. The Review of Financial Studies, 6(2):pp. 375(cid:21)404, 1993.
[20] Victor H. Martinez and Ioanid Rosu. High frequency traders, news and volatility. Working
Paper, March 2013.
[21] ChristineA.ParlourandDuaneJ.Seppi. Handbook of Financial Intermediation and Banking,
chapter 3. Elsevier, 2008.
[22] U.S. SEC. Findings regarding the market events of may 6, 2010, September 2010.
[23] Hans R. Stoll. Inferring the components of the bid-ask spread: Theory and empirical tests.
The Journal of Finance, 44(1):115(cid:21)134, March 1989.
58

[24] Chen Yao and Mao Ye. Tick size constraints, high frequency trading, and liquidity. Working
Paper, July 2014.
59

Internet Appendices
60

B Measuring Aggressive Orders’ Pro(cid:28)tability
Calculating round-trip pro(cid:28)ts using a FIFO or LIFO approach is not a useful way to measure
the pro(cid:28)tability of individual aggressive orders. Even the most aggressive HFTs engage in some
passivetrading,soaFIFO/LIFO-round-tripmeasurewouldeitherconfoundaggressivetradeswith
passive trades, or require some arbitrary assumption to distinguish between inventory acquired
passively and inventory acquired aggressively (on top of the already-arbitrary assumption of FIFO
or LIFO). A second, more general problem is that a measurement scheme based on inventory
round-trips will always combine at least two orders (an entry and an exit), so such measurement
schemes do not actually measure the pro(cid:28)tability of individual aggressive orders.
In this appendix, I provide rigorous justi(cid:28)cation for the claim that the average expected pro(cid:28)t
from an aggressive order in the E-mini market equals the expected favorable price movement,
minus trading/clearing fees and half the bid-ask spread. After presenting the formal proof, I
discuss details of empirically estimating expected favorable price movement.
B.1 Preliminaries
Trading/clearing fees apply equally to both passively and aggressively traded E-mini contracts,
so to simplify the exposition, I will initially ignore these fees. Similarly, I make the simplifying
assumption that the bid-ask spread is constant, and identically equal to one tick; for the E-mini
market, this assumption entails minimal loss of generality.
In the E-mini market, the pro(cid:28)tability of individual aggressive orders can be considered in
isolation from passive orders. Because E-mini contracts can be created directly by buyers and
sellers, a trader’s net inventory position does not constrain his ability to participate in a given
trade18. As long as he can (cid:28)nd a buyer, a trader who wishes to sell an E-mini contract can always
do so, regardless of whether he has a preexisting long position. More generally, if a trader enters
a position aggressively then exits it passively, he could have conducted the passive transaction
even if he hadn’t engaged in the preceding aggressive transaction. While a desire to dispose of
passively-acquired inventory might motivate a trader to submit an aggressive order, the question
18Theoneexceptionwouldariseintheextremelyrareeventthatatraderwhodidnotqualifyforaposition-limit
exemptionheldsomanycontracts(eitherlongorshort)thathisinventoryafterthetradewouldexceedtheposition
limit of 100,000 E-mini contracts. For HFTs, this minor exception can safely be ignored.
61

of underlying motivation is distinct from the question of whether the aggressive order was directly
pro(cid:28)table.
B.2 Formal Argument
With these preliminaries established, I turn to the rigorous argument. Consider a trader who
executes J aggressive sell orders of size one, and J aggressive buy orders of size one, for some large
J. Following the remarks above, the trader’s passive transactions can be ignored. Let the average
(cid:16) (cid:17)
direction-normalized price change after these aggressive orders be ϑ˜≡ ϑ 2J ticks for some ϑ
2J−1
that does not depend on J.
First, suppose that the trader always submits an aggressive sell after an aggressive buy, and
always submits an aggressive buy after an aggressive sell. Without loss of generality, assume that
the trader’s (cid:28)rst aggressive order is a buy. The trader’s combined pro(cid:28)t from all 2J aggressive
orders is
π = −a +b −a +b −...−a +b (33)
2J 1 2 3 4 2J−1 2J
= −a +(a −1)−a +(a −1)−...−a +(a −1) (34)
1 2 3 4 2J−1 2J
= −a +a −a +a −...−a +a −J (35)
1 2 3 4 2J−1 2J
= −a +(a +ζ )−(a +ζ )+(a +ζ )−... (36)
1 1 b,1 2 s,2 3 b,2
...−(a +ζ )+(a +ζ )−J
2J−2 s,J 2J−1 b,J
J J
(cid:88) (cid:88)
= (a +ζ )− (a +ζ )−a −J (37)
2i−1 b,i 2j−2 s,j 1
i=1 j=2
 
J J−1 J J
(cid:88) (cid:88) (cid:88) (cid:88)
= a
2i−1
−a
1
+ a 2j+ ζ
b,i
− ζ
s,j
−J (38)
i=1 j=1 i=1 j=2
where a and b respectively denote the prevailing best ask and best bid at the time the kth
k k
aggressive order executes, ζ denotes the change in midpoint price following the rth aggressive
b,r
buy order, and ζ denotes the change in midpoint price following the rth aggressive sell order.
s,r
(cid:16) (cid:17)
Note that ϑ ≡ 1 (cid:80)J ζ + (cid:80)J (−ζ ) .
2J r=1 b,r r=1 s,r
Next, taking expectations, we (cid:28)nd
62

 
J J−1
(cid:88) (cid:88)
E[π
2J
] = E[a
2i−1
]− E[a
1
]+ E[a
2j
] (39)
i=1 j=1
J J
(cid:88) (cid:88)
+ E[ζ ]− E[ζ ]−J
b,i s,j
i=1 j=2
(cid:104) (cid:105) (cid:16) (cid:104) (cid:105)(cid:17)
= JE[a ]−E[a ]−(J −1)E[a ]+JE ϑ˜ −(J −1) −E ϑ˜ −J (40)
1 1 1
(cid:104) (cid:105)
= (2J −1)E ϑ˜ −J (41)
(cid:18) (cid:19)
2J
= (2J −1) E[ϑ] −J (42)
2J −1
= J(2E[ϑ]−1) (43)
where the second equality uses the assumption that midpoint prices follow a martingale with
respect to their natural (cid:28)ltration, together with the assumption of a constant bid-ask spread.
From the (cid:28)nal equality above, it follows immediately that the trader’s average expected pro(cid:28)t on
an individual aggressive order is given by
1 1
E[π ] = E[ϑ]− (44)
2J
2J 2
Finally,notethatnoneofthecalculationsabovereliedontheassumptionthattheaggressiveorders
alternated between buys and sells (this only simpli(cid:28)ed the notation). It follows immediately from
grouping together multiple aggressive orders of the same sign that the result would hold for orders
of varying sizes, provided that the overall aggressive buy and aggressive sell volumes were equal.
(cid:104) (cid:105)
Under the usual regularity conditions, as J → ∞, ϑ˜→ lim E ϑ˜ = E[ϑ]. (cid:3)
A.S. J→∞
B.3 Obtaining Unbiased Estimates
Recall that the discussion in section 4.1 implied that we can estimate the pro(cid:28)tability of an
HFT’s aggressive order using the (direction-normalized) accumulated price-changes following that
aggressive order out to some time past the HFT’s maximum forecasting horizon. If we choose
too short an accumulation window, the resulting estimates of the long-run direction-normalized
average price changes following an HFT’s aggressive orders will be biased downward. This enables
63

us to empirically determine an adequate accumulation period by calculating cumulative direction-
normalized price changes over longer and longer windows until their mean ceases to signi(cid:28)cantly
increase
Market activity varies considerably in its intensity throughout a trading day, so event-time,
whichImeasureintermsofaggressiveorderarrivals, providesamoreuniformstandardfortempo-
ralmeasurementsthandoesclock-time. Empirically,anaccumulationperiodofabout30aggressive
orders su(cid:30)ces to obtain unbiased estimates of the price movement following an HFT’s aggressive
order, but I consider results for an accumulation period of 50 aggressive orders to allow a wide
margin for error. The mean direction-normalized price changes following individual HFTs’ ag-
gressive orders does not di(cid:27)er signi(cid:28)cantly for accumulation periods of 50, 200, or 500 aggressive
orders, even if we distinguish aggressive orders by size. The same holds true for aggressive orders
placed by non-HFTs. Using too long an accumulation period will not bias the estimates, but it
will introduce unnecessary noise, so I opt for an accumulation period of 50 aggressive orders.
AsIdiscussatgreaterlengthinsectionC.1,futurepricemovementsaremoderatelypredictable
from past aggressive order (cid:29)ow and order book activity, but only at very short horizons. Of the
variables that meaningfully forecast future price changes, the direction of aggressive order (cid:29)ow
is by far the most persistent, but even its forecasting power diminishes to nonexistence for price
movements more than either about 12 aggressive orders or 200 milliseconds in the future. The
adequacy of a 30+ aggressive order accumulation period is entirely consistent with these results.
As a simple empirical check on the validity of direction-normalized cumulative price changes
as a proxy for the pro(cid:28)tability of aggressive orders, I use each HFT’s explicit overall pro(cid:28)ts and
passive trading volume, together with the pro(cid:28)ts on aggressive orders as measured by the proxy,
to back out the HFT’s implicit pro(cid:28)t on each passively traded contract. The resulting estimates of
HFTs’ respective pro(cid:28)ts from passive transactions are all plausible from a theoretical perspective,
and are comparable to non-HFTs’ implicit performance on passive trades.
64

C Benchmark Regression Results
C.1 Variables that Forecast Price Movements
Bid-ask bounce notwithstanding, the price at which aggressive orders execute changes rather
infrequently in the E-mini market. On average, only about 1−3% of aggressive buy (sell) orders
execute at a (cid:28)nal price di(cid:27)erent from the last price at which the previous aggressive buy (sell)
order executed, and the price changes that do occur are almost completely unpredictable on the
basisofpastpricechanges. However, severalothervariablesforecastpriceinnovationssurprisingly
well.
In contrast to price innovations, the direction of aggressive order-(cid:29)ow in the E-mini market
is extremely persistent and predictable. On average, the probability that the next aggressive
order will be a buy (sell) given that the previous aggressive order was a buy (sell) is around
75%. In addition to forecasting the direction of future aggressive order-(cid:29)ow, the direction of
past aggressive order-(cid:29)ow also forecasts future price innovations to statistically and economically
signi(cid:28)cantextent,andforecastsbasedonpastaggressiveordersignsalonearemoderatelyimproved
by information about the (signed) quantities of past aggressive orders. Simple measures of recent
changes in the order book o(cid:27)er further, yet modest, improvement in price forecasts.
The levels of resting depth in the order book, in addition to the changes in resting depth, also
improve price forecasts slightly, but these stock variables cannot be reliably recovered in much
of my data-set because a small number of modi(cid:28)cation messages (around 2 − 4%) are missing.
These occasional missing modi(cid:28)cations introduce only transient noise into (cid:29)ow variables such as
changes in resting depth, but they have permanent e(cid:27)ects on the corresponding stock variables.
Fortunately, omittingresting-depth stockvariables fromthe directtests of theexploratory trading
model’s predictions in section 5 is harmless. These tests use the explanatory variables in the
benchmark regression (45) only as an empirical analogue of ϕ, the signal of future aggressive
order-(cid:29)ow in the exploratory trading model. Thus the tests require only that the benchmark
explanatory variables o(cid:27)er some predictive power, not that those variables control for all public
information (I control for public information by other means, discussed in section 5).
65

C.2 Econometric Benchmark
For each trading day in my sample, I regress the cumulative price-change (in dollars) between the
aggressive orders k and k+50, denoted y , on lagged market variables suggested by the remarks
k
in section C.1. Speci(cid:28)cally, I regress y on the changes in resting depth between aggressive orders
k
k −1 and k at each of the six price levels within two ticks of the best bid or best ask, the signs
of aggressive orders k−1 through k−4, and the signed executed quantities of aggressive orders
k −1 through k −4. For symmetry, I adopt the convention that sell depth is negative and buy
depth is positive, so that an increase in buy depth has the same sign as a decrease in sell depth.
Denoting the row vector of the 14 regressors by z , and a column vector of 14 coe(cid:30)cients by Γ,
k−1
I estimate the equation
y = z Γ+(cid:15) (45)
k k−1 k
:= γ d1 +...+γ d6 + (46)
1 k−1 6 k−1
γ sign +...+γ sign +
7 k−1 10 k−4
γ q +...+γ q +(cid:15)
11 k−1 14 k−4 k
Table 3 summarizes the estimates from the regression above, computed over my entire sample. All
of the variables are antisymmetrical for buys and sells, and so have means extremely close to zero,
but the mean magnitudes in the rightmost column of Table 3 provide some context for scale.
66

Table 5: Estimates from Benchmark Regression
Coe(cid:30)cient (×1000) Robust t-Statistic Variable Avg. Magnitude
dbest bid−2 -0.90 -1.02 4.13
k−1
dbest bid−1 -2.08 -4.29 10.8
k−1
dbest bid 1.13 4.94 23.1
k−1
dbest ask 1.11 4.97 23.4
k−1
dbest ask+1 -2.03 -4.24 11.2
k−1
dbest ask+2 -1.60 -1.90 4.44
k−1
sign 1186 33.3 1
k−1
sign 753 20.2 1
k−2
sign 544 14.6 1
k−3
sign 472 13.4 1
k−4
q 4.09 9.29 12.6
k−1
q 2.66 6.59 12.6
k−2
q 1.85 4.66 12.6
k−3
q 1.16 2.98 12.6
k−4
Comparableresultsobtainusingasfewastwolagsofaggressiveordersignandsignedquantity.
Linear forecasts of y do not bene(cid:28)t appreciably from the inclusion of data on aggressive orders
k
beforek−4,oronchangesinrestingdepthpriortoaggressiveorderk−1. Becausetheprice-change
y is not normalized by the sign of the kth aggressive order, it has an expected value of zero, so I
k
do not include a constant term in the regression. Including a constant term in the regression has
negligible e(cid:27)ect on the results.
Although the last several aggressive order signs do o(cid:27)er rather remarkable explanatory power,
the respective distributions of resting depth changes and executed aggressive order quantities have
muchheaviertailsthanthedistributionofordersign, sopriceforecastsaremeaningfullyimproved
by the inclusion of these variables.
The positive coe(cid:30)cients on the lagged aggressive order variables and on the depth changes at
67

the best bid and best ask are consistent with the general intuition that buy orders portend price
increases, and sell orders portend price decreases. The negative coe(cid:30)cients on depth changes at
the outside price levels require slightly more explanation.
Because the E-mini market operates according to strict price and time priority, a trader who
seeks priority execution of his passive order will generally place that order at the best bid (or best
ask); however, if the trader believes that an adverse price movement is imminent, he will place
his order at the price level that he expects to be the best bid (ask) following the price change. It
is relatively uncommon for prices to change immediately after an aggressive order in the E-mini
market, butwhenpricesdochange, itisextremelyrareduringregulartradinghoursforthechange
to exceed one tick. As a result, the expected best bid (ask) following a price change is typically
one tick away from the previous best, so it is not surprising that (e.g.) an increase in resting
depth one tick below the best bid tends to precede a downward price change. These features of
the E-mini market also shed some light on why changes in depth more than one tick away from
the best (i.e., dbest bid−2 and dbest ask+2) are not signi(cid:28)cant predictors of future price movements.
k−1 k−1
68

D Supplemental Tables of Empirical Results
69

)tcartnoC
rep
sralloD
ni(
epyT
redarT
dna
eziS
yb
,sredrO
evisserggA
fo
sgninraE
ssorG
egarevA
:6
elbaT
sTFH-noN
sTFH-B
sTFH-A
latnemercnI
¯q
≤
sOA
llA
latnemercnI
¯q
≤
sOA
llA
latnemercnI
¯q
≤
sOA
llA
¯q
sOA
sOA
sOA
-
86.1
-
73.4
-
48.3
1
57.1
27.1
46.4
65.4
83.4
32.4
5
98.1
77.1
58.4
66.4
48.2
94.3
01
79.1
97.1
59.4
17.4
93.6
58.3
51
60.2
38.1
80.5
77.4
59.4
41.4
02
02.2
68.1
41.5
18.4
56.6
14.4
52
35.2
09.1
42.5
78.4
97.6
97.4
03
04.2
19.1
01.5
88.4
00.7
99.4
53
55.2
59.1
41.5
19.4
96.6
82.5
04
41.2
59.1
94.5
29.4
40.7
24.5
54
00.2
69.1
41.5
59.4
09.6
16.5
05
78.2
99.1
03.5
89.4
00.7
78.5
06
17.2
30.2
04.5
00.5
02.7
21.6
57
61.2
30.2
25.5
10.5
02.7
83.6
09
02.4
91.3
36.7
76.5
99.7
56.7
0002
70

¯q
dlohserhT
eziS
woleB
sredrO
evisserggA
’sepyT
redarT
fo
snoitcarF
:7
elbaT
sTFH-noN
sTFH-B
sTFH-A
.rggA
fo
%
sOA
llA
fo
%
.rggA
fo
%
sOA
llA
fo
%
.rggA
fo
%
sOA
llA
fo
%
¯q
emuloV
emuloV
emuloV
%86.5
%97.35
%77.4
%84.93
%04.0
%13.42
1
%88.41
%62.38
%31.61
%90.67
%44.1
%47.34
5
%86.02
%78.98
%59.32
%01.48
%90.3
%46.45
01
%50.32
%75.19
%30.03
%10.88
%45.3
%57.65
51
%34.62
%72.39
%28.53
%07.09
%08.4
%28.06
02
%23.92
%14.49
%92.04
%63.29
%73.5
%83.26
52
%70.13
%89.49
%03.64
%41.49
%93.6
%26.46
03
%49.13
%32.59
%65.94
%79.49
%20.7
%28.56
53
%96.33
%66.59
%13.45
%30.69
%15.8
%72.86
04
%33.43
%08.59
%67.55
%23.69
%02.9
%92.96
54
%80.14
%90.79
%92.36
%66.79
%55.01
%70.17
05
%66.24
%63.79
%21.96
%45.89
%79.21
%18.37
06
%67.44
%46.79
%41.37
%20.99
%10.61
%56.67
57
%73.64
%38.79
%68.47
%02.99
%11.12
%86.08
09
71
