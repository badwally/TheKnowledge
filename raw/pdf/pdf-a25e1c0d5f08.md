---
id: pdf-a25e1c0d5f08
type: pdf
title: sr677
url: ''
authors:
- FRS User
ingested_at: '2026-04-29T16:24:27Z'
content_hash: sha256:9d8bc22d1025e33fd37048f7a2835a4ec6c79ec8f2cffef62e7c6ead6c3cf745
source_path: raw/pdf/pdf-a25e1c0d5f08.pdf
domains:
- trading-and-markets
nlm_corpus_ids:
- ccbda94f-7251-42bb-864f-0e1c9850f7ad
wiki_pages:
- wiki/entities/allan-malz.md
- wiki/entities/federal-reserve-bank-of-new-york.md
- wiki/entities/stephen-figlewski.md
- wiki/concepts/risk-neutral-distribution.md
- wiki/concepts/breeden-litzenberger-theorem.md
- wiki/concepts/option-implied-volatility-smile.md
- wiki/concepts/clamped-cubic-spline-interpolation.md
- wiki/concepts/no-arbitrage-restrictions-on-options.md
meta:
  page_count: 42
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/sr677.pdf
published_at: '2014'
---
Federal Reserve Bank of New York
Staff Reports
A Simple and Reliable Way to Compute
Option-Based Risk-Neutral Distributions
Allan M. Malz
Staff Report No. 677
June 2014
This paper presents preliminary findings and is being distributed to economists
and other interested readers solely to stimulate discussion and elicit comments.
The views expressed in this paper are those of the author and do not necessarily
reflect the position of the Federal Reserve Bank of New York or the Federal
Reserve System. Any errors or omissions are the responsibility of the author.

A Simple and Reliable Way to Compute Option-Based Risk-Neutral Distributions
Allan M. Malz
Federal Reserve Bank of New York Staff Reports, no. 677
June 2014
JEL classification: G01, G13, G17, G18
Abstract
This paper describes a method for computing risk-neutral density functions based on the
option-implied volatility smile. Its aim is to reduce complexity and provide cookbook-style
guidance through the estimation process. The technique is robust and avoids violations of option
no-arbitrage restrictions that can lead to negative probabilities and other implausible results. I
give examples for equities, foreign exchange, and long-term interest rates.
Key words: option pricing, risk-neutral distributions
_________________
Malz: Federal Reserve Bank of New York (e-mail: amalz@nyc.rr.com). The author thanks Sirio
Aramonte, Bhupinder Bahra, Benson Durham, Stephen Figlewski, Will Melick, Carlo Rosa,
Joshua Rosenberg, Ernst Schaumburg, and seminar participants at the Board of Governors of the
Federal Reserve System for comments. Juan Navarro-Staicos, Kale Smimmo, and Steven Burnett
have collaborated on the implementation of the techniques described here. The views expressed
in this paper are those of the author and do not necessarily reflect the position of the Federal
Reserve Bank of New York or the Federal Reserve System.

Contents
1 Introduction 1
2 Overview of the technique 3
2.1 Implied volatility data . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 The technique in brief . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 The volatility interpolating function . . . . . . . . . . . . . . . . . . 6
2.4 Addressing violations of no-arbitrage . . . . . . . . . . . . . . . . . . 7
2.5 Diagnostic analysis of the technique . . . . . . . . . . . . . . . . . . 11
3 Application to exchange-traded products 12
3.1 Data and computation . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 Time series of tail risk estimates . . . . . . . . . . . . . . . . . . . . 14
4 Application to currencies 16
4.1 Data and computation . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.2 Time series of tail risk estimates . . . . . . . . . . . . . . . . . . . . 19
5 Application to swaptions 20
5.1 Data and computation . . . . . . . . . . . . . . . . . . . . . . . . . 20
5.2 Time series of tail risk estimates . . . . . . . . . . . . . . . . . . . . 23
6 Conclusion 24
ii

1 Introduction
Risk-neutral probability distributions (RNDs) of future asset returns based on the
option-implied volatility smile have been available toresearchers in finance for decades.
These techniques, however, are difficult to implement, because rendering some option
data suitable for this purpose requires a great deal of processing, and because the
algorithms thatcomputetheRNDsarecomplex andhardtoautomate. Thisisperhaps
a major reason that option-based RNDs have been less widely applied and become less
standard than might have been expected given their potential value.
This paper describes a simple technique for computing RNDs given suitable input
data, requiring relatively straightforward programming. While most elements of the
technique have been employed in earlier work, their combination and sequencing as
described here greatly reduce the effort required to obtain results. The aim of the
technique is to reduce complexity and the aim of the paper is to provide cookbook-
style guidance through the estimation process. We give examples for different types
of assets: equities, foreign exchange, and long-term interest rates.1
Methods for computing RNDs from option prices are inspired by the Breeden and
Litzenberger (1978) statement of the relationship between market prices of European
call options and the RND: In the absence of arbitrage, the mathematical derivative
of the call option value with respect to the exercise price is closely related to the
risk-neutral probability that the future asset price will be no higher than the exercise
price at option maturity.2
The payoff at maturity to a European call option maturing at time T, with an exercise
price X, is max(S −X,0), with S representing the terminal underlying price. We
T T
denote the observed time-t market value of a European call struck at X and with a
tenor of τ = T −t by c(t,X,τ). Absent arbitrage, therefore, the option value is equal
to the present expected value of the terminal payoff under the risk-neutral distribution:
(cid:2)
∞
c(t,X,τ) = e−rtτ E˜ [max(S −X,0)] = e−rtτ (s −X)π˜ (s)ds,
t T t
X
where
S ≡ time-t underlying price
t
r ≡ time-t continuously compounded financing rate
t
E˜ [·] ≡ an expectation taken under the time-t risk-neutral probability measure
t
π˜ (·) ≡ time-t risk-neutral probability density of S
t T
1The technique set out here is applied to the measurement of systemic risk in Malz (2013). It is
also used in the Federal Reserve Bank of New York’s market monitoring.
2SurveysoftechniquesforextractingRNDsfromoptionpricesincludeJackwerth(1999)and(2004),
and Mandler (2003). More recent approaches are cited later in this paper. The Breeden-Litzenberger
theorem was first stated in Breeden and Litzenberger (1978) and Banz and Miller (1978).
1

Differentiate the market call price with respect to the exercise price X to get the
“exercise-price delta”
(cid:3)(cid:2) (cid:4)
∂ X
c(t,X,τ) = e−rtτ π˜ (s)ds −1 . (1)
∂X t
0
This result implies that the time-t risk-neutral cumulative distribution function Π˜ (X)
t
of the future asset price—the probability that the terminal underlying price will be X or
lower—is equal to one plus the future value of the exercise-price delta of a European
call struck at X:
(cid:2)
X ∂
Π˜ (X) ≡ π˜ (s)ds = 1+ertτ c(t,τ,X). (2)
t t ∂X
0
Differentiate again to see that the time-t risk-neutral probability density function is
the future value of the second derivative of the call price with respect to the exercise
price:
∂2
π˜ (X) = ertτ c(t,X,τ). (3)
t ∂X2
Though we’ll describe our technique in terms of the market’s pricing schedule for call
options, the put price schedule offers a more direct and intuitive way to state the
relationship between option prices and risk-neutral probabilities:
∂
Π˜ (X) = ertτ p(t,τ,X),
t ∂X
where p(t,X,τ) represents the time-t value of a European put struck at X and with
a tenor of τ.
Figlewski (2010) provides some nice intuition for this statement. Consider the in-
creasing value of a put option, for a given current market price of the underlying, as
the exercise price varies from low to high. At very low exercise prices this function
has a slope and value near zero, and at very high exercise prices a slope equal to erτ
and a value near its intrinsic value. As we increase the exercise price from X to a
nearby point X +Δ, the risk-neutral expected future value of the payoff of the option
increases by Δ times the risk-neutral probability that the option expires in-the-money,
that is, Π˜(X +Δ):
Δ×Π˜(X +Δ) ≈ ertτ [p(t,τ,X +Δ)−p(t,τ,X)].
1
⇒ Π˜(X +Δ) ≈ ertτ [p(t,τ,X +Δ)−p(t,τ,X)]
Δ
2

It’s well known, but worth reiterating, that RNDs are not the same as real-world
probabilities, or the ones in market participants’ heads, but are influenced, perhaps
heavily, byriskpreferences. Achangeinrisk-neutral probabilities canbeduetochanges
in real-world probabilities, or risk preferences, or both.3
2 Overview of the technique
The technique we present here works, in principle, for any asset type, provided data of
acceptable quality are available. We’ll sketch the approach here and give detail on how
it’s applied to different asset classes, as well as examples of the results, in subsequent
sections.
2.1 Implied volatility data
The approach requires data of reasonably good quality on the Black-Scholes implied
volatility smile. The data, that is, are Black-Scholes volatilities for European options
of a given tenor τ, but with a range of exercise prices. The volatility smile changes
over time and for varying tenors, and can be thought of as a slice through the maturity
axis of a time-t Black-Scholes volatility surface σ(t,X,τ). We focus here on a single
tenor, rather than the entire surface.
Although Black-Scholes volatilities are expressed in a metric drawn from a particular
option pricing model, they are associated with market- rather than model-based prices.
Denote the time-t Black-Scholes model value of a European call as
⎡ (cid:7) (cid:8) (cid:9) (cid:10) ⎤
log St + r −q + σ2 τ
v(S ,X,τ,σ,r ,q ) = S e−qtτ Φ ⎣ X √ t t 2 ⎦
t t t t σ τ
⎡ (cid:7) (cid:8) (cid:9) (cid:10) ⎤
log St + r −q − σ2 τ
−Xe−rtτ Φ ⎣ X √ t t 2 ⎦
σ τ
where
3The work surveyed in Garcia, Ghysels and Renault (2010) uses historical data on underlying asset
pricesaswellascontemporaneousoptionpricedatatosimultaneouslyestimateboththerisk-neutraland
real-world probability distributions. Ross (2013) presents a technique that, with suitable assumptions,
identifiesboththerisk-neutralandreal-worldprobabilitiesofdiscretepriceoutcomesfromoptionprices
alone.
3

σ ≡ a Black-Scholes implied volatility
q ≡ time-t continuously compounded cash flow yielded by the underlying asset
t
The volatility surface translates into the time-t market price schedule of European
calls with different tenors and exercise prices via the relationship
c(t,X,τ) = v[S ,X,τ,σ(t,X,τ),r ,q ]. (4)
t t t
We refer to the right-hand side of (4) as the call valuation function. This function
is a standard Black-Scholes formula taking as its implied volatility argument the in-
terpolated volatility corresponding to the given exercise price. It takes an observed or
estimated market-adjusted Black-Scholes volatility, and returns an estimated market
call price. We can view c(t,X,τ) and σ(t,X,τ) as simply two different metrics for
expressing the market values of options.
The implied volatilities can be expressed in various other units, such as Black or
normalized volatilities. The exercise prices can also be expressed in different ways,
such as the ratio or spread to the current spot or forward price, or the option delta.
But under all these conventions, implied volatilities can be transformed into option
prices in currency units for given exercise prices.
One of the main challenges in fitting RNDs is the diversity of option data and the
difficulty of working with it. That’s not the problem we’re solving here. Rather, we’re
attempting to find an easier way to process the option data into an estimated RND
and minimizing the extent to which we add assumptions to the information contained
in the data. The data we use for this paper are obtained from Bloomberg Financial
LP, which aggregates and processes quotes, end-of-day prices, and indicative prices
from a range of dealers and exchanges. As we’ll describe in a moment, we subject the
data to a set of quality diagnostics. While flaws do occasionally appear in the data,
the overall quality is good.
The approach here can be applied to a wide range of data types. We’ve developed
the technique for three input data structures. In each, the data on each date consist
of two columns/rows, one containing implied volatilities and the other the associated
exercise prices:
Asset class Volatility type Units Exercise price metric
Exchange-traded Black-Scholes volatilities Pct. p.a. Ratio to spot
Currencies and gold Black-Scholes volatilities Pct. p.a. Spot delta
Swaptions Black volatilities Pct. p.a. Bps from forward
We’ll provide more detail on the data in a subsequent section on each structure.4
4Intradaydata can be displayedfora given asset using the function OVDV.The documentationfor
4

2.2 The technique in brief
The steps in the computation of the RND are:
(cid:129) Interpolate and extrapolate the volatility smile data using a cubic spline function
thatis “clamped” attheendpoints. Thisistantamount toassuming that implied
volatilities for very deep out-of-the-money calls and puts are identical to those
for the furthest in- and out-of-the-money strikes in the input data.
(cid:129) Apply the call valuation function (4), taking the interpolated Black-Scholes
volatilities and other inputs called for by the Black-Scholes formula as argu-
ments, and returning an option value in currency units.
(cid:129) Numerically difference the call valuation function with respect to the exercise
price to approximate the risk-neutral cumulative probability and probability den-
sity functions. The step size for this differentiation is set so that the density
function is non-negative.
The probability distribution and density functions are estimated by taking finite dif-
ferences in exercise-price space of the call valuation function. Discretized versions of
the option-based estimate of the risk-neutral cumulative probability distribution and
density functions (2)–(3) for a step size Δ are given by
(cid:3) (cid:13) (cid:14) (cid:13) (cid:14)(cid:4)
1 Δ Δ
Π˜ (X) ≈ 1+ertτ c t,X + ,τ −c t,X − ,τ
t
Δ 2 2
and
(cid:3) (cid:13) (cid:14) (cid:13) (cid:14)(cid:4)
1 Δ Δ
π˜ (X) ≈ Π˜ X + −Π˜ X −
t t t
Δ 2 2
1
= ertτ [c(t,X +Δ,τ)+c(t,X −Δ,τ)−2c(t,X,τ)].
Δ2
As Δ → 0, these expressions converge to the risk-neutral distribution functions, but
the propensity for negative probabilities increases.
While fairly standard, two key features in combination simplify the computation pro-
cess without generating anomalies: the use of a clamped cubic spline to interpolate—
and, more importantly, extrapolate—the volatility smile, and treating the differencing
step size as a user setting. Both are intended primarily to avoid processing-induced
violations of no-arbitrage restrictions. We’ll discuss these problems in detail just be-
low. But in a nutshell, if the input implied volatility data don’t violate no-arbitrage
restrictions, why should the interpolating function?
Bloomberg’s implied volatility data is a bit sparse. Some notes and white papers can be downloaded
via the function DRVD (Derivatives Documentation Center).
5

2.3 The volatility interpolating function
A cubic spline is constructed to have continuous first and second derivatives at all
its knot points. The construction of a cubic spline involves solving a set of linear
equations for the coefficients that impose continuity of the first and second deriva-
tives. To complete the algorithm, additional conditions are imposed on the equations
corresponding to the first and last, or boundary, knot points. A natural cubic spline is
constructed so that the second derivatives at the boundary knot points are equal to
zero. As a result, extrapolation beyond the boundary knot points is linear, but gener-
ally with a non-zero slope. This is precisely the behavior that may induce violations of
the no-arbitrage bounds on the volatility smile.
A clamped cubic spline, in contrast, is constructed so that its slope takes on specific
values at the boundary knot points.5 The interpolated volatility function we use is
constructed as a clamped cubic spline, with a slope of zero at the boundary knot
points. We use the input data on the implied volatility smile as the knot points of the
spline. The slope of the fitted spline is thus zero at the highest and lowest exercise
prices in the data. The spline is smooth at those transitions, since continuity of the
second derivatives is still imposed. The extrapolated spline values beyond those points
are then equal to the observed implied volatilities for the highest and lowest exercise
prices.6
Let {(x ,σ ),...,(x ,σ )} represent the input data set or knot points, ordered so
1 1 n n
x > x ,i = 2,...,n, and let f(x) represent the fitted clamped cubic spline. (As
i i−1
noted, the units of the x are different for different asset types.). The interpolating
i
function with its flat-line extensions is defined as the piecewise function
⎧
⎨ σ for x < x
1 1
σ(x) = f(x) for x ≤ x < x
⎩ 1 n
σ for x ≥ x
n n
5Klugman, Panjer and Willmot (2008), pp. 534ff., provides the recipe for constructing a clamped
cubic spline, as well those for natural and other types of cubic splines. The recipes are also contained
in many other numericalmath and computing books. Neuberger(2012)appliesa cubic spline to inter-
polate volatilitydata; Neuberger(2012)and Carrand Wu (2009)extrapolate the impliedvolatilitiesof
theboundarypoints,butwithoutincorporatingtheclampingintothesplinefittingprocedure. Blissand
Panigirtzoglou (2002) and (2004) implement flat-line extrapolation of a natural spline by introducing
additional synthetic data points with implied volatilities equal to those observed for the highest and
lowest exercise prices and with exercise prices outside that range.
6Our interpolating function is not a smoothing spline, as employed for example by Bliss and Pani-
girtzoglou(2002)and(2004);itpassesthrough,ratherthancloseto,alltheknotpoints. Asmoothing
spline requires additional procedures to ensure that no-arbitrage conditions are preserved after fitting
the interpolating function, and introduces additional concerns about inferring rather than observing
data.
6

The highest and lowest exercise prices for which implied volatility data are observed
are generally not quite extreme enough to set the estimated risk-neutral probabilities
equal to0or 1. Itistherefore necessary toextrapolate theinterpolated smile, and thus
the estimated call valuation function, beyond those strikes to obtain a complete RND.
Clamping the interpolated smile so that the extrapolated segments are parallel to the
x-axisat the extreme implied vols ensures that the call valuation function is monotonic
and convex to the origin in the exercise price, avoiding violations of no-arbitrage
restrictions. Volatility smiles are typically U-shaped or L-shaped. Extrapolating a
steep slope out to high or low exercise prices can cause, for example, a call to have a
higher value than a call with a higher exercise price.
Flat-line extrapolation gives the tails of the fitted RND a lognormal shape beyond the
highest and lowest exercise prices in the input data. Figlewski (2010) proposes the
alternative of first estimating the central portion of the RND using the available input
data, and then grafting tails onto it that follow a generalized extreme value (GEV)
distribution. The GEV distribution has better empirical support than the lognormal
as a description of extreme return behavior. The parameters of the GEV distribution
for each tail are estimated by having it coincide with a “penultimate” tail segment of
the observable data-based portion of the RND. However, if observable option price
inputs are available for exercise prices deep in the tails, there is likely to be only a small
impact on estimated probabilities, as these will be already very close to zero or one. If
observable option prices do not extend far into the tails, the GEV distribution-based
tails will be estimated from less suitable data closer to the center of the distribution.
Extrapolation raises an uncomfortable question: Are we just inventing the risk-neutral
tail behavior our procedure will later appear to infer from the data? To some extent,
the answer is yes. The input data have to be far enough out-of-the-money for the risk-
neutral distributions to be accurate, and we shouldn’t be too trustful of statements
about outcomes far beyond the exercise prices in the input data. But it’s unrealistic
to expect data of acceptable quality to typically extend to the points on exercise price
axis at which the risk-neutral density is very close to zero. The choice therefore is not
whether to extrapolate, but how to extrapolate while adding as little assumed behavior
as possible to the available data.
2.4 Addressing violations of no-arbitrage restrictions on the call
valuation function
The key model-free arbitrage condition is that the European call valuation function
is decreasing and convex with respect to the exercise price. These basic no-arbitrage
restrictions imply corresponding restrictions or bounds on the shape of the volatility
7

smile.7
Since the typical volatility smile is U-shaped, flat-line extrapolation seems at first less
accurate than continuing the up- or downward sloping behavior. But keeping the
slope constant over the extrapolated intervals will at least sometimes lead to arbitrage
violations. It makes sense in some contexts, such as the study of market liquidity, to
admit the possibility that they occur, but construction of risk-neutral densities is not
one of them.
(i) Violations of the slope restrictions
The first slope restriction states that the call value can’t rise as the exercise price
rises, that is, the exercise-price delta can’t be positive:
∂
c(t,X,τ) ≤ 0. (5)
∂X
A related restriction pertains to put values, namely, that they are increasing in the
exercise price. We can express the put restriction in terms of the exercise-price delta
of a call by invoking put-call parity.8 It states that the absolute value of the call’s
negative slope with respect to the exercise price can’t exceed the risk-free discount
factor:
∂
c(t,X,τ) ≥ −e−rtτ. (6)
∂X
The validity of these restrictions can also be seen from (1), which shows the con-
sequences of violating them: the risk-neutral cumulative probabilities will not tend
toward zero (unity) for very low (high) terminal underlying prices, and will therefore
not meet the definition of a probability distribution function.
Each of these restrictions leads to a restriction on the slope of the volatility smile.
Differentiate (4) to express the slope of the call valuation function in terms of the
7The no-arbitrage restrictions on option values are laid out in many option-pricing textbooks, e.g.
Cox and Rubinstein (1985), ch. 4. No-arbitrage restrictions on volatility smiles are laid out in Hodges
(1996). A¨ıt-SahaliaandDuarte(2003)discusstheno-arbitrageconditionsonvolatilitysmilesinrelation
to estimation of RNDs.
8To re-express this condition, differentiate the statement of put-call parity
p(t,X,τ)=c(t,X,τ)+Xe−rtτ −S
t
where p(t,X,τ) represents the put value, with respect to X to get
∂ ∂
p(t,X,τ)= c(t,X,τ)+e−rtτ.
∂X ∂X
8

slope of the volatility smile and of the Black-Scholes sensitivities with respect to the
exercise price and volatility, denoted by argument subscripts:
∂ ∂
c(t,X,τ) = v (·)+v (·) σ(t,X,τ).
∂X X σ ∂X
Substituting into the no-arbitrage restrictions (5)–(6) gives us
∂
v (·)+v (·) σ(t,X,τ) ≤ 0
X σ ∂X
∂
v (·)+v (·) σ(t,X,τ) ≥ −e−rtτ,
X σ ∂X
in turn implying an upper and a lower bound on the slope of the volatility smile:
∂ v (·)
σ(t,X,τ) ≤ − X > 0 (7)
∂X v (·)
σ
∂ v (·)+e−rtτ
σ(t,X,τ) ≥ − X < 0. (8)
∂X v (·)
σ
The sign and magnitude of each of the bounds stated in (7)–(8) derives from those of
the Black-Scholes sensitivities. The Black-Scholes exercise-price delta v (·), like that
X
of the call valuation function, is negative and obeys v (·) > e−rtτ. For low exercise
X
prices, v (·) is close to −e−rtτ, that is, slightly flatter than −1 for short tenors and
X
typical interest rates. For high exercise prices, it flattens toward a slope of zero. The
Black-Scholes vega v (·) is always positive, and bell-curve shaped for varying exercise
σ
prices. The upper bound (7) is thus positive, tending to zero for very high exercise
prices, while the lower bound (8) is negative, tending to zero for very low exercise
prices.
The Black-Scholes sensitivities also vary with the general level of implied volatility. For
higher volatilities, v (·) rises more gradually toward zero as the exercise price rises,
X
and v (·) is higher for any exercise price. When volatility is high, the absolute values
σ
of the bounds are low and thus more constraining, since the denominator of (7)–(8)
is large. A scheme for interpolating the volatility smile is therefore most apt to violate
the restrictions on the slope of the volatility smile if the general level of volatility is
high, and then only for very high or low exercise prices.
The extent to which the no-arbitrage constraints bind thus depends on the second-
order Black-Scholes sensitivities withrespect toimpliedvolatility, whicharewidelyused
in option risk management. The most important are vanna, the sensitivity of vega to
changes in the spot price, and volga, the sensitivity of vega to changes in volatility.
9

The no-arbitrage constraints (7)–(8) depend in part on volga and the “exercise-price
vanna.”9
We can think of the bounds in terms of typical U-shaped volatility smile behavior. The
bounds permit both upward- and downward-sloping volatility smiles, so a U shape does
not per se violate them. But the bounds also state that the volatility smile can’t still
be upward-sloping at very high exercise prices, and can’t still be downward-sloping at
very low exercise prices, unless vega has become exceptionally low in those intervals.
Figure 1 compares the results of the clamped cubic spline with flat-line extrapolation
to an alternative polynomial interpolation and extrapolation scheme that adheres more
closely to intuition about typical U-shaped smile behavior, using implied volatilities of
3-month options on the S&P 500 index for two dates. On the earlier date, Feb. 25,
2009, at the height of the post-Lehman financial panic, the general level of S&P 500
implied volatility wasextremely high by historical standards. The flat-line extrapolation
prevents the slope of the call valuation function from falling below −e−rtτ (sloping
more steeply downward) for very low exercise prices, and from turning positive for high
exercise prices. If you look closely, even on the later date, Dec. 21, 2012, although vol
is much lower, the slope of the call function becomes a bit steeper than −e−rtτ for low
exercise prices and positive for high exercise prices when the extrapolated volatilities
are not clamped.10
There are infinite ways to interpolate the volatility smile that will not violate (7)–(8).
The clamped cubic spline approaching we propose has the conceptual advantage that
it adheres to the observable data, and adds little in the way of assumed RND behavior
to the data. It has the practical advantages that is simple, and appears to work in
all cases, making it suitable for software-like implementations requiring frequent or
routinized calculations.
(ii) Violations of the convexity restrictions
The call valuation function must be convex to the origin. The convexity restriction
can be written as
∂2
c(t,X,τ) ≤ 0.
∂X2
If this restriction is violated over some range of exercise prices, it is possible to con-
struct a butterfly consisting of long positions in the relatively cheap pair of options
9CastagnaandMercurio(2007)usevannaandvolgatofindthecoefficientsofano-arbitrageimplied
volatility interpolating function in a stochastic-volatility model.
10Note also that our interpolation technique can induce concave “sneering” or “frowning” intervals
into the generally “smirking” interpolated smile.
10

struck at the ends of the range and short positions in the relatively dear option struck
at the middle of the range that brings in net premium now and can’t lose money at
maturity. Violations imply that the risk-neutral cumulative probability distribution is
falling and that the probability density function is negative over at least some part of
that range.
Even when the volatility smile appears to the eye to be quite smooth, it may still gen-
erate nonconvexities in the call valuation function over small exercise-price intervals,
particularly near knot or inflection points. A good deal of smoothing of the call val-
uation function is accomplished by spline interpolation of the volatilities. Permitting
users to vary the differencing step size Δ further smooths the interpolated volatility
smile and avoids intervals over which the density function is negative.
If Δ is set low enough, negative densities result. We’ve constructed the algorithm
so that the user can vary Δ to find a low value that nonetheless keeps the density
positive everywhere on most days. Some experimentation shows that the estimated
risk-neutral probabilities are not terribly sensitive to variations in Δ. That is, if Δ
is set high to be confident that no negative densities are generated, or Δ is set low
enough to induce negative densities over some exercise price intervals on some days,
the estimated probabilities and quantiles are not drastically changed. We’ll present an
example in the next section.
The propensity to generate negative densities, not surprisingly, is greatest when the
general level of volatility is high. A practical way to find a suitable Δ for a given
asset is to plot the density function for a date on which implied volatility is relatively
high. These dates are almost invariably in late 2008 and implied volatility is generally
a multiple of the high volatilities observed in other subperiods of the time series. A
minimum Δ can be readily found that does not induce negative densities, or induces
only slightly negative densities on a handful of extreme-volatility dates. That Δ can be
used to compute time series of tail probabilities, moments or quantiles. A procedure
could be added to the technique to find a value of Δ that avoids negative densities for
each asset on each day, though at the cost of longer computation time.
2.5 Diagnostic analysis of the technique
Diagnostics on the input data are useful to help users understand better how well
the interpolation is working, how far the extrapolation might be straying from the
unobservable marketreality, andassessthepotentialforestimationerror. We’ll provide
such a table for each of the three asset classes we cover. Among the key diagnostics:
(cid:129) The option deltas tell us how far into the tails the observed data penetrate.
11

(cid:129) The option vega is directly related to the no-arbitrage restrictions. If vegais high
at the extremes of the input data, then the choice of extrapolation technique
has greater potential to influence the shape of the distribution. The focus here
is on how far the vega has fallen at the highest and lowest exercise prices, so
we’ll express the vega for each strike as its ratio to the vega of the at-the-money
(ATM) option.
(cid:129) A version of the risk-neutral distribution based only on the input data provides
rough bounds for the risk-neutral distribution and gives us a sense of how much
estimation error there might be. Rather than fixing Δ for the entire RND, we
use the successive differences between the exercise prices of the options in the
raw data. Let X and X be two of the exercise prices in the data set, ordered
i−1 i
so X > X . Then
i i−1
1+ertτ (X −X ) −1 [c(t,X ,τ)−c(t,X ,τ)], i = 2,...,n,
i i−1 i i−1
is an upper bound on Π˜ (X ) and a lower bound on Π˜ (X ). The upper bound
t i−1 t i
on Π˜ (X ) is 1 and the lower bound on Π˜ (X ) is zero. Based purely on the
t n t 1
observed data, the true values of the Π˜ (X ) can be anywhere in between the
t i
upper and lower bounds.
3 Application to exchange-traded products
3.1 Data and computation
Options on exchange-traded products, primarily single stocks, indexes and futures,
tradeonmanyexchangesandthousandsofassetsworld-wide. Theexchangesgenerate
raw option price data in currency terms. Processed implied volatility data are provided
by Bloomberg, as fields pertaining to a ticker. Time series history is typically available,
though how far back varies widely. “Moneyness” in the data is expressed as a ratio
to the current cash price. An example are data for 3-month options on the S&P 500
index, ticker SPX Index, as of Dec. 21, 2012. The data for SPX and other U.S.
indexes and single stocks are based on prices of CBOE options on the index.11
11TheBloombergdataforeachtickerareconstructedbyfilteringtherawend-of-daydata,extracting
EuropeanoptionimpliedvolatilitiesfromtheAmericanoptionprices,andinterpolatingtheresultsacross
exercise price and tenor. The resulting surfaces are close to the intraday volatility surfaces displayed
on the OVDVscreen. Some of the latter data is identifiedby tickers, but a field search indicatesthere
is no history.
12

Bloomberg field mnemonic moneyness implied vol
3MTH IMPVOL 80%MNY DF 80.0 23.95
3MTH IMPVOL 90.0%MNY DF 90.0 21.71
3MTH IMPVOL 95.0%MNY DF 95.0 18.81
3MTH IMPVOL 97.5%MNY DF 97.5 17.40
3MTH IMPVOL 100.0%MNY DF 100.0 16.09
3MTH IMPVOL 102.5%MNY DF 102.5 14.88
3MTH IMPVOL 105.0%MNY DF 105.0 13.84
3MTH IMPVOL 110.0%MNY DF 110.0 12.48
3MTH IMPVOL 120%MNY DF 120.0 12.34
Computations using these data are illustrated in Figure 2 for two dates, Aug. 7, 2008,
just after the first major overt symptoms of the global financial crisis emerged,12 and
Dec. 21, 2012. The upper left panel displays the Bloomberg data and the interpolated
volatility smile. The x-axis in this and the other panels in the figure is expressed as
the proportional difference between the exercise price and the current forward index
level.
The upper right panel of Figure 2 displays the call valuation function, evaluated for
each exercise price using the interpolated smile for each date. The call prices are
expressed as afraction of the current forward index level, calculated as F = e(rt−qt)τ.
t,τ
Option prices for the S&P 500, forward index levels, and the diagnostics in Table 1,
are calculated using 3-month T-bill yields as a financing rate and trailing (rather than
estimated forward) 12-month dividend yields as the underlying cash flow rate.
The bottom panels of Figure 2 display the risk-neutral distribution and density func-
tions. The finite differences are calculated setting Δ = 0.025 (as a fraction of current
forward index level). For any point on the x-axis, the plot in the bottom left panel
can be read as giving the probability that the price return of the S&P 500 vis-`a-vis
the current forward index level over the subsequent 3 months will be that level or less.
Table 1 displays diagnostics for the computations. The deltas of the input options
extend close to zero and unity on both dates, and the vegas are reasonably small at
the endpoints.
The distributions are typically multi-modal for SPX Index, with a left-tail hump par-
ticularly pronounced. Multi-modal behavior is both an authentic result and an artifact
of the technique. Take, for example, the left-tail hump for Aug. 7, 2008. It appears
for exercise prices roughly 10 to 20 percent below the current forward index. These
12The“quantevent,”inwhichalgorithmicequity-tradingprogramsabruptlybeganexperiencinglosses
far in excess of prior extremes, began on Aug. 6. Paribas halted redemptions from three subprime-
focused hedge funds it managed on Aug. 9. The Federal Reserve introduced its first policy measures
to address the crisis the next day.
13

are the highest implied vols on the smile. In that interval, the call valuation function
declines less slowly than it would if those low-strike implied vols were closer to the
ATM vol. Hence the risk-neutral density is high. But a spline knot point imposes an
inflection point in the smile at an exercise price equal to 1139.46. From that point,
the slope of the volatility smile goes rapidly from steep to flat. Although it is impos-
sible to discern in the graph, at that point the decline in the call valuation function
decelerates, inducing a small region in which the density is close to zero.
The hump behavior is the feature most directly affected by the smoothing parameter
Δ. For example, if Δ were set higher than the value of 0.025 used in the lower-right
plots of Figure 2, the density would be estimated by bridging across wider intervals
of the interpolated smile, reducing the variations in the convexity of the call valuation
function, and thus the propensity of the estimated risk-neutral density to rise and fall.
If Δ is set high enough, the additional mode can be eliminated, without drastically
changing the probabilities of returns of specific magnitudes.
Data on options on money-market futures are also available, but these present partic-
ular difficulties, especially in the current low-rate environment, as the actively traded
exercise-price range is highly compressed against the zero bound. For this group, how-
ever, it is relatively straightforward to construct a cruder estimate of the RND along
the lines of the diagnostic table.13
3.2 Time series of tail risk estimates
The results can be used to compute time series of statistics of interest, including
moments, quantiles and the probabilities of returns of specified sizes. For example,
we can represent risk-neutral tail risk as the probability of a decline in the S&P of a
specific large magnitude. Determining a magnitude to focus on raises similar issues
to stress testing in risk management, namely, finding a shock that qualifies as very
severe, but is nonetheless plausible and in the realm of possibility. If we choose a very
high shock, its risk-neutral probability will almost always be zero. If we choose too
small a shock, its risk-neutral probability will almost always be very high. Either way,
little insight is gained.
One way to find a useful shock magnitude is through this back-of-the-envelope cal-
culation: If returns were normally distributed, a decline (or runup) of about 2.33
standard deviations would have a probability of one percent. The long-term average
annualized implied as well as realized volatility of S&P 500 price returns is roughly
13TheBloombergdataforEDAComdtycontainonlythreedistinctvaluesforthe3-monthtenor,and
itisuncleariftheinterpolationtechniquetheyapplygenerallytoexchange-tradedoptionsiswell-suited
to money-market futures.
14

20 percent. A√rough estimate of the first percentile of 3-month returns is therefore
−20 × 2.33 × 0.25 = −23.3 percent. Avoiding exact numbers, so as not suggest
that this is a precise estimate, the risk-neutral probability of a 20 or 25 percent decline
in the S&P 500 is a reasonable representation of tail risk. We have a mild preference
for 20 percent, since it is the lowest observed exercise price in the data and reduces
reliance on extrapolation.
Theresultsaredisplayed Figure3,coveringtheperiodsinceend-Nov. 2005. Theupper
panel displays the probability of a three-month decline in the S&P 500 of at least 20
percent. The lower panel displays the first percentile of the S&P 500 price return,
displayed as a positive number in percent, in other words, the value-at-risk (VaR) of
a long S&P 500 position, expressed in return terms, at a 99-percent confidence level.
Risk-neutral tail risk was low prior to the crisis, apart from a brief but sharp increase
in mid-2006. At the end of Feb. 2007, tail risk increased sharply, and again after
the quant event of August 2007. Tail risk peaked following the Lehman bankruptcy
at a probability near 35 percent of a further decline of the S&P 500 in excess of 20
percent over the subsequent quarter. The tail probability is low at the time of writing,
just a few percent, but remains generally higher than pre-crisis and fluctuates quite a
bit more than pre-crisis. The extreme quantile or VaR of the distribution tracks the
probability closely, ranging from about 20 percent before and after the crisis to about
60 percent at its peak in late 2008.
To gain some insight on the the effect of different settings for Δ, Figure 4 compares
the estimated tail risk time series for two values, Δ = 0.025 and Δ = 0.100, each held
constant over the entire observation interval. The time series are very close to one
another. The correlation of the two probability series is 0.997 and the correlation of
their daily first differences is 0.977.
As an example of how the techniques can be applied to single stocks, and perhaps
interesting in its own right, Figure 5 displays equity tail risk for American International
Group, Inc. from late 2007 until the Friday preceding the Lehman bankruptcy filing,
Sep. 12, 2008. Tail risk is measured by the risk-neutral probability of a decline of
50 percent or more in the stock price, which can be plausibly said to represent the
risk of a corporate bankruptcy. It is somewhat uncomfortable far from the observed
data, but that far in the tails, the vega is likely very low even for high volatility levels,
and the exercise-price delta very close to −e−rtτ. If there is significant error in the
extrapolation, relative to the unobserved “true” market volatility levels, there will be
more (or less) probability mass between −50 and −20 percent, and less (or more)
between −100 and −50 percent.
The probability is close to zero for most of the period, rising a bit during periods
of fear near the end-2007 and Bear Stearns. The “failure probability” began to rise
rapidly during July 2008, as market concerns about losses at Fannie Mae and Freddie
15

Mac intensified rapidly. By Sep. 12, the Friday before the Lehman bankruptcy filing,
the probability reached 40 percent, but most of that runup had taken place during the
previous few days.
A characteristic of risk-neutral tail risk behavior that appears clearly in Figures 3 and 5
is its propensity to have risen very abruptly when it is high. Tail risk measures tend to
decline gradually from these peaks—unless, as in the AIG case, the peak proves to be
terminal. Peaks in tail risk are associated with and subsequent to an event, but occur
when market-adjusted tail risk has been relatively low. These characteristics seem to
indicate that high tail risk estimates do not provide reliable early warning signals of
risk events.
But periods of low tail risk estimates, especially if interrupted by sudden transitory
spikes in tail risk unaccompanied by major events, such as those of June 2006 and
February 27, 2007, may indicate unease in markets that can lead to future risk events.
Thisobservationiscloselyrelatedtothe“paradoxofvolatility,” inwhichlowvolatilityis
associated with the buildup of financial imbalances, rising leverage and higher financial
stability risk.
4 Application to currencies
4.1 Data and computation
Prices of options on currencies and precious metals are typically expressed by traders
as Black-Scholes implied volatilities. The exercise price of an at-the-money option is
generally understood to be equal to the current forward rather than spot exchange
rate with a time to settlement equal to the option tenor, and the option is called
at-the-money forward (ATMF).
Theexercisepricesofin-andout-of-the-moneycurrency optionsaretypicallyexpressed
in terms of the Black-Scholes delta
∂
v (·) ≡ v(S ,τ,X,σ,r ,q ). (9)
S ∂S t t t
t
For this data structure, therefore, it is most convenient to think of the Black-Scholes
volatility surface as a function σ(t,δ,τ) of the date, tenor and delta rather than
exercise price. Computation of prices of options in currency units for trade-settlement
purposes is easy via the Black-Scholes formula.
Currency options are typically traded as combinations: straddles, strangles and risk
reversals. Strangles and risk reversals, which are combinations of out-of-the-money
16

options, typically have a delta of 0.10 or 0.25. These combinations can be readily
converted into prices of individual options with the specified deltas. For example,
consider a 25-delta one-month strangle. Its price is quoted as the implied vol spread
or difference between the average implied vols of the 25-delta put and call, which are
not directly observed, and the ATMF put or call vol.
(cid:3) (cid:13) (cid:14) (cid:13) (cid:14)(cid:4)
1 1 1
strangle price = σ t,0.25, +σ t,0.75, −ATMF vol,
2 12 12
The risk reversal quote is the implied vol spread between the two “wing” options:
(cid:13) (cid:14) (cid:13) (cid:14)
1 1
risk reversal price = σ t,0.25, −σ t,0.75, .
12 12
Note that strangle and risk reversal are quoted as vol spreads, while the ATMF is a
vol level. Using these definitions, the vol levels of the wing options can be inferred
from the strangle, risk reversal, and ATMF quotes:
(cid:13) (cid:14)
1 1
σ t,0.25, = ATMF vol+strangle price+ ×risk reversal price
12 2
(cid:13) (cid:14)
1 1
σ t,0.75, = ATMF vol+strangle price− ×risk reversal price
12 2
Analogous formulas describe the 10-delta versions of these standard option combina-
tions, and versions for other tenors. From them, we can obtain the 10-, 25-, 75-, and
90-delta implied volatilities. The ATM and ATMF options have deltas close to, but
not exactly, equal to 0.50. We obtain an option with a delta near 50 from the ATMF
option, using (9) to compute the exact delta.
Foreign-exchange option price data is available from a number of data providers and
dealers. The data used here are downloaded from Bloomberg, which stores implied
volatility histories for each point on the volatility surface—tenor and exercise price—
for each currency pair, as a distinct ticker. The data are aggregated, filtered and,
possibly, interpolated from a number of dealer quotes. Bloomberg’s currency option
data appear generally to be the highest quality of the three structures discussed here.
The data structure is illustrated here using 1-month options on EUR-USD, the price
of a Euro in dollars, as of Dec. 31, 2012.14
14Data are also available for the 1-week, 3-, 6-, and 12-month, and 10-year tenors.
17

Bloomberg ticker description implied vol/spread
EURUSDV1M Curncy EUR-USD OPT VOL 1M 8.2200
EURUSD25R1M Curncy EUR-USD RR 25D 1M -0.3025
EURUSD25B1M Curncy EUR-USD BFY 25D 1M 0.1050
EURUSD10R1M Curncy EUR-USD RR 10D 1M -0.4875
EURUSD10B1M Curncy EUR-USD BFY 10D 1M 0.2875
Transformed into a volatility smile in (δ,σ)-space, the data become
delta implied vol
0.1000 8.26375
0.2500 8.17375
0.5015 8.22000
0.7500 8.47625
0.9000 8.75125
Once the input data has been prepared, the volatility smile can be interpolated. We
carry out the interpolation via a clamped cubic spline, but in (δ,σ)- rather than (X,σ)-
space. The x-axisvalues 0.10,0.25,0.75, and 0.90 are the same on each date, but the
center knot point has a slightly different x-axis value near 0.50 each day. Options with
deltas below 0.10 are assigned the 10-delta volatility and options with deltas above
0.90 are assigned the 90-delta volatility.
For this data structure, there is an additional step following interpolation, by which
the smile in (δ,σ)-space is transformed into one in (X,σ)-space. This is slightly less
simple than it might seem, as we can’t map directly from exercise price to delta via
(9), and then to the smile in (δ,σ)-space. The reason is that the volatility argument
in (9) is not constant, but itself varies with delta.15
The computation is as follows: Substitute the expression for the Black-Scholes delta
into the interpolated smile σ(t,δ,τ). For any stipulated X◦, and for fixed values of
the other arguments, we can solve
σ◦ = σ[t,v (S ,τ,X◦,σ◦,r ,q ),τ)]
S t t t
numerically for σ◦.16
15We don’t have that problem when calculating the delta of the ATMF option because we have a
fixed exercise price and volatility.
16In one approach to RND construction from data on exchange-traded options, implied volatilities
initially associated with exercise prices are converted to volatilities associated with the corresponding
18

This transformation is illustrated in Figure 6 for two dates, May 22, 2009 and Nov.
18, 2011. The input data and the initial smile interpolation, carried out via a clamped
cubic spline, are displayed in the left panel. The x-axis is in delta units. The volatility
smiles in the right panel are computed from those in the left panel. They are not
derived by a fresh interpolation but rather functionally, from the interpolated smile in
(δ,σ)-space, via the numerical procedure described in the previous paragraph. Note
that the direction of the x-axis is reversed between the two graphs. On the later date,
options with especially high payoffs if the dollar appreciates sharply vis-`a-vis the euro
have high implied volatilities. These correspond to low exercise prices in currency units
but high call deltas.
Computations using these data are illustrated in Figure 7 for the same two dates as in
Figure 6, May 22, 2009 and Nov. 18, 2011. In all four panels, the x-axis is expressed
as the proportional difference from the 3-month forward rate (USD per EUR). The
RND estimates are computed using Δ = 0.005 (as a fraction of the forward rate).
Option prices for EUR-USD, forward exchange rates, and the diagnostics in Table 2,
are calculated using 1-month U.S. dollar and euro Libor rates as the financing and
underlying cash flow rates.
The two dates display a sharp contrast in the direction of skewness of the risk-neutral
distribution. On the earlier date, there is a sharp skew toward a weaker dollar, while
on the later date there is a skew toward a stronger dollar.
Diagnostics for the data and computations are shown in Table 2. The deltas of the
input options, naturally, extend exactly from 0.10to0.90, but thevegasare reasonably
small at the endpoints. The data are somewhat better-behaved than the S&P 500
option data; the foreign-exchange option data permit a smaller step size in differencing
without encountering non-convexities.
4.2 Time series of tail risk estimates
An example of how the results can be applied is displayed in Figure 8. The upper panel
plots time series of the risk-neutral probabilities of the dollar appreciating and depreci-
ating by 7.5 percent or more over the subsequent month.17 The lower panel plots the
deltas using (9). Interpolation is then carried out in (δ,σ)-space. The conversion to deltas may be
done using the same at-the-money volatility for all strikes (so-called “point conversion”)or using each
strike’s volatility (“smile conversion”) to avoid cases in which segments of the volatility smile are so
steep that an option may have a lower call delta than another with a higher exercise price. Bu and
Hadri(2007)discussthephenomenon,whichintuitivelyseemslikelytobeduetono-arbitrageviolations
in the data. The issue doesn’t arise with our technique because we are going from input data sets in
(δ,σ)-space to (δ,X)-space rather than vice versa.
17This seems like a reasonable threshold: volatility for EUR-USD is typically in the neighborhood of
10percent. Ifexchangeratereturnswerenormallydistributed,thefirstandlastpercentilesof1-month
19

difference between these probabilities, and highlights the direction and magnitude of
the skew in tail risk estimates. In contrast to the S&P 500 and other equity indexes,
the tail risk skew for major currency pairs can and does change direction.
Tail risk first began to rise sharply around the time of the Bear Stearns failure and
spiked following the Lehman filing. Since Lehman, tail risk has often been very high,
and the risk-neutral probability of a sharp dollar appreciation has generally been much
higher than that of a depreciation. This pattern likely reflects safe-haven positioning,
as it began well before the European debt crisis, but was reinforced as the latter played
out.
Both the level of risk-neutral tail risk and its skew to a weaker euro rose steadily
through 2011, but dropped abruptly following the announcement by the European
CentralBankofitslonger-term refinancing operations (LTROs)onDecember 8, 2011.
Tail risk has most recently dropped back to pre-2008 levels, and the directional dif-
ference between dollar appreciation and depreciation is near zero, in spite of a steady
appreciation of the euro vis-`a-vis dollar amounting to 15 percent since mid-2012.
5 Application to swaptions
5.1 Data and computation
Standard swaptions are options that exercise into a payer or receiver position in a
LIBOR interest-rate swap. They are one of the two more-liquid types of markets in
which exposures to longer-term interest rates are traded.18 The other type is options
on government bond futures. Swaption data are better suited than implied volatilities
derived from bond futures options prices for computing interest-rate RNDs:
(cid:129) Swaptions have a fixed term to maturity rather than a fixed maturity date,
generating a time series of expectations measures with a fixed horizon without
requiring interpolation across maturities.
(cid:129) Swaption prices map directly into interest-rate expectations, rather than indi-
rectly via bond prices.
(cid:129) Prices of options on bond futures include compensation for the delivery option,
and switches in the cheapest-to-deliver can distort their signals of interest-rate
prospects.
√
returns would be about ±10×2.33× 0.083¯3=±6.73 percent.
18Breeden and Litzenberger (2013) describe a technique for extracting RNDs of shorter-term rates
from implied volatilities of caps and floors.
20

One disadvantage of swaption data should also be mentioned: The underlying price
of a swaption is the LIBOR swap rate, rather than the risk-free rate, which may differ
from the risk-free rate for a number of risk- and liquidity-based reasons.
Swaption implied volatility data are available on Bloomberg. They are expressed as
Black or lognormal vols, that is, as the standard deviation of logarithmic changes
in the forward swap rate for the given swaption “tail” (swap maturity) and tenor
(option maturity), expressed in percent units at an annual rate. The data are based
on quotes aggregated by Bloomberg from submissions by several contributing dealers.
Bloomberg interpolates across strikes when data is missing. The data appear to be of
reasonably good quality from early 2013 on.
A wide range of tails and tenors are priced. Option tenors range from 3 months to
20 years and underlying swap tails from 2 to 30 years. Exercise prices range from 200
basis points below to 200 above the current forward swap rate for the given tail and
tenor. For tenors and tails with forward swap rates that are close to the zero bound,
there are no recent data for exercise prices 200 basis points below the forward swap
rate, as these would be exercisable only if longer-term rates turned negative.19
As with other types of options, expressing the value of a swaption in terms of an
implied volatility based on a particular model of interest-rate behavior does not mean
themarketbelievesinthatmodel. Rather,itrepresentsaconvenient unitforexpressing
the value or market price of the swaption.
Black vols fit without much further ado into our RND computation scheme. The data
structure on Sep. 5, 2013 for “2-year into 10-year” swaptions—2-year options on
10-year swaps—was
Strike Bloomberg ticker description Black vol
-200 USPAV07C Curncy USD BVOL SWPT-200 2Y10Y 32.5790
-100 USPAV04K Curncy USD BVOL SWPT-100 2Y10Y 28.9314
-50 USPAV036 Curncy USD BVOL SWPT-50 2Y10Y 27.8261
-25 USPAV02H Curncy USD BVOL SWPT-25 2Y10Y 27.3975
0 USSV0210 BBIR Curncy USD SWPT BVOL ATM 2Y10Y 27.0250
25 USPAUZA1 Curncy USD BVOL SWPT 25 2Y10Y 26.7361
50 USPAUZAQ Curncy USD BVOL SWPT 50 2Y10Y 26.4866
100 USPAUZC4 Curncy USD BVOL SWPT 100 2Y10Y 26.1151
200 USPAUZEW Curncy USD BVOL SWPT 200 2Y10Y 25.7388
19The available Bloomberg tickers and data can be identified by configuring the VCUB or interest
rate vol cube function. The configuration tab enables the user to select and display contributed Black
vols for OTM swaptions.
21

The exercise prices are equal tothe 10-year swap rate2 years forward on Sep. 5, 2013,
4.0888, less the stipulated moneyness, expressed in basis points in the first column.
The forward swap rate is today’s market assessment of the fixed rate that sets to
zero the net present value of a 10-year fixed-for-floating swap initiated 2 years hence.
The Black vols (percent per annum) in the last column are the input data provided by
Bloomberg.
The Black formula for the price of a swaption in currency units is the product of three
terms: (i) the notional amount, (ii) the “bps running” or annuity or present value per
basis point of the payments by the fixed leg of the swap, and (iii) the Black-Scholes
option value formula applied to the current swap rate as though it were a proper asset,
and with the risk-free or financing rate set to zero. We can ignore the first two terms,
which are invariant across exercise prices. The last component can be written as
ertτv[F ,X,τ,σ(t,X,τ),0,0] for a payer swaption, where F is the current forward
t,τ t,τ
swap rate for a swap initiated τ years hence.20 A payer swaption gives its owner the
right to enter into a swap at a fixed rate X, and is analogous to a put on a bond, and
to a call in interest-rate terms.
In essence, the swaption valuation formula has a component containing the expected
value of changes in the swap rate vis-`a-vis the current forward value in excess of a
given strike rate, and a component expressing how much that expected value is worth.
The Black formula gives the value of the option in interest-rate terms. It is converted
into currency units using the notional amount and the annuity value.
Withthese modifications, thesamecalculation procedure asforexchange-traded prod-
ucts can be used to compute the RND. The computations are illustrated in Figure 9
for two dates, May 1, 2013 and Sep. 5, 2013. We use a small Δ = 0.0001 (1 basis
point), so this data structure can be said to be relatively cooperative with our tech-
nique. The x axis in the upper panels of the charts is expressed as differences from
the forward swap rate in basis points, analogous to the previous examples. In the
lower panels, the distribution and density are represented as functions of the terminal
10-year swap rate.
Diagnostics for the computations are displayed in Table 3. We see that the data
extend far enough above and below the forward swap rate that the deltas cover much
of the interval (0,1). The vegas for the highest and lowest exercise prices are fairly
low. We are applying a version of the Black formula that isn’t discounted to the
present by the risk-free rate, so low-strike call deltas can be very close to unity.
The volatility smile and the implied RNDs are heavily influenced by the proximity of
spot and forward swap rates to the zero bound. On the earlier date, the implied RND
is skewed quite strongly to higher rates, and on the later date, much less so. But
20The term of the swap isn’t displayed in the notation.
22

on both dates, implied volatilities of low strike options close to the zero bound are
higher, not lower, than those of high-rate strikes. A distribution skewed to the left is
incompatible with low rates.
5.2 Time series of tail risk estimates
As we did for other asset classes, we’ll illustrate the results with time series of tail
risk estimates. We use changes in basis points vis-`a-vis the current forward swap rate
rather than proportional changes to represent extreme moves. In Figure 10, the top
two panels display the risk-neutral probabilities of specific changes in rates, while the
lower panel displays the probabilities of rates reaching specific levels.
The upper panel displays probabilities of changes of at least 200 basis points. From
the beginning of May 2013, the probabilities both of very large decreases and increases
in rates, as well as the forward rates themselves, began to rise. The probability of a
sharp drop in rates rose faster, but the probability of a rate rise accelerated following
the Chairman’s May 22 Joint Economic Committee testimony. As forward rates rose,
these probabilities drew closer together. By the time rates peaked in early September
2013, the tail probabilities were nearly equal. More recently, a skew to sharply higher
has been re-established, but it is less pronounced than in early 2013.
The probabilities of changes of at least 100 basis points, displayed in the center panel
of Figure 10, also rose in 2013. These probabilities are more nearly equal to each
other than those of more extreme rate moves, as one would expect of events closer
to the center of the distribution.
Proximity to the zero bound makes it more difficult to interpret risk-neutral interest-
rate distributions, because it is hard to distinguish between the effects of movement
away from or toward the zero bound from other influences on the shape of the dis-
tribution. The impact of proximity to zero is similar to the pattern seen in the lower
panel of Figure 10, which displays the risk-neutral probabilities of the rate ending at
5 percent or higher, or at 2 percent or lower. These probabilities are driven in large
part by how close to these thresholds the current forward rate happens to be.
Similarly, when rates are close to zero, the probability of a large decline cannot be
high, because there is nowhere for rates to go but up. When the forward swap rate is
relatively low, it is more strongly correlated with the risk of sharply lower rates. When
the swap rate is relatively high, it moves more closely with the risk of a drastic rise in
rates. The level of rates, however, is not the only determinant of rate RNDs. Since
their early September peak, 10-year swap rates 2 years forward have fluctuated in a
1
range between about 3 and 4 percent. During that time, overall rate volatility has
2
declined, and the probability of a decline in rates of at least 200 basis points has fallen
relative to that of a rise in rates of the same magnitude.
23

6 Conclusion
The technique for estimating risk-neutral RNDs described here appears to work well
with several different data structures, and is relatively easy to program and use. There
is considerable demand, particularly in central banks, to apply risk-neutral probabilities
in market monitoring and policy work, and our technique should make it possible to
take some of the effort out of creating the RNDs.
That effort would be better focused on other aspects of RNDs. As far as the quality
and reliability of the results is concerned, assembling and filtering better-quality data
sets is one challenge. But perhaps the most important open task with respect to
risk-neutral RNDs remains how to use and interpret them.
24

References
A¨ıt-Sahalia, Y. and Duarte, J. (2003). Nonparametric option pricing under shape
restrictions, Journal Of Econometrics 116(1/2): 9–47.
Banz, R. W. and Miller, M. H. (1978). Prices for state-contingent claims: some
estimates and applications, Journal of Business 51(4): 653–672.
Bliss, R. R. and Panigirtzoglou, N. (2002). Testing the stability of implied probability
density functions, Journal of Banking and Finance 26(2–3): 381–422.
Bliss, R. R. and Panigirtzoglou, N. (2004). Option-implied risk aversion estimates,
Journal of Finance 59(1): 407–446.
Breeden, D. T. and Litzenberger, R. H. (1978). Prices of state-contingent claims
implicit in option prices, Journal of Business 51(4): 621–651.
Breeden, D. T. and Litzenberger, R. H. (2013). Central bank policy impacts on the
distribution of future interest rates. Available at http://www.dougbreeden.
net/uploads/Breeden˙Litzenberger˙with˙Postscript˙Central˙Bank˙
Policy˙Impacts˙9˙20˙2013.pdf.
Bu, R. and Hadri, K. (2007). Estimating option implied risk-neutral densities using
spline and hypergeometric functions, Econometrics Journal 10(2): 216–244.
Carr, P. and Wu, L. (2009). Variance risk premiums, Review of Financial Studies
22(3): 1311–1341.
Castagna, A. and Mercurio, F. (2007). The vanna-volga method for implied
volatilities, Risk pp. 106–111.
Cox, J. C. and Rubinstein, M. (1985). Options markets, Prentice–Hall, Englewood
Cliffs, NJ.
Figlewski, S. (2010). Estimating the implied risk-neutral density for the U.S. market
portfolio, in T. Bollerslev, J. Russell and M. Watson (eds), Volatility and Time
Series Econometrics: Essays in Honor of Robert F. Engle, Oxford University
Press, Oxford and New York, pp. 323–353.
Garcia, R., Ghysels, E. and Renault, E. (2010). The econometrics of option pricing,
in Y. A¨ıt-Sahalia and L. P. Hansen (eds), Handbook of Financial Econometrics
Tools and Techniques, Vol. 1, Elsevier, Amsterdam, pp. 479–552.
Hodges, H. M. (1996). Arbitrage bounds on the implied volatility strike and term
structures of European-style options, Journal of Derivatives 3(4): 23–35.
25

Jackwerth, J. C. (1999). Option-implied risk-neutral distributions and implied
binomial trees: a literature review, Journal of Derivatives 7(2): 66–82.
Jackwerth, J. C. (2004). Option-implied risk-neutral distributions and risk aversion,
Monograph, Research Foundation of CFA Institute. http://www.cfapubs.
org/doi/pdf/10.2470/rf.v2004.n1.3925.
Klugman, S. A., Panjer, H. H. and Willmot, G. E. (2008). Loss models: from data
to decisions, 3rd edn, John Wiley & Sons, Hoboken, NJ.
Malz, A. M. (2013). Risk-neutral systemic risk indicators, Staff Reports 607, Federal
Reserve Bank of New York. Available at http://www.newyorkfed.org/
research/staff˙reports/sr607.pdf.
Mandler, M. (2003). Market expectations and option prices: techniques and
applications, Physica-Verlag, Heidelberg and New York.
Neuberger, A. (2012). Realized skewness, Review of Financial Studies
25(11): 3423–3455.
Ross, S. A. (2013). The Recovery Theorem, Journal of Finance . Forthcoming,
available at http://onlinelibrary.wiley.com/doi/10.1111/jofi.12092/
pdf.
26

xedni
005
P&S
rof
scitsongaid
dna
ataD
:1
elbaT
8002guA70
)X(tΠ
dnuob
reppU
dnuob
rewoL
ageV
atleD
eulav
llaC
ytilitaloV
X
X S
0440.0
6511.0
0000.0
2781.0
9069.0
8563.252
9850.52
68.2101
008.0
7581.0
7322.0
6511.0
0966.0
6018.0
9268.041
2558.42
64.9311
009.0
6182.0
6223.0
7322.0
2788.0
3486.0
7229.19
8949.22
77.2021
059.0
0363.0
0504.0
6223.0
6469.0
4306.0
7275.07
7589.12
24.4321
579.0
7944.0
8894.0
0504.0
0000.1
1215.0
9918.15
2020.12
70.6621
000.1
6945.0
4995.0
8894.0
6879.0
8314.0
4120.63
1460.02
27.7921
520.1
8646.0
5847.0
4995.0
3298.0
2413.0
8493.32
8911.91
73.9231
050.1
0258.0
0649.0
5847.0
8065.0
1041.0
4345.7
6603.71
86.2931
001.1
7489.0
0000.1
0649.0
9511.0
8810.0
2237.0
1843.71
82.9151
002.1
4102rpA40
)X(tΠ
dnuob
reppU
dnuob
rewoL
ageV
atleD
eulav
llaC
ytilitaloV
X
X S
9710.0
1150.0
0000.0
9880.0
3189.0
5259.463
3903.02
70.2941
008.0
2990.0
9241.0
1150.0
5805.0
5378.0
8679.781
9769.71
85.8761
009.0
2791.0
5932.0
9241.0
0718.0
4437.0
0250.801
8625.51
48.1771
059.0
4192.0
2163.0
5932.0
2949.0
7426.0
1695.27
3780.41
64.8181
579.0
4834.0
5825.0
2163.0
0000.1
0084.0
3318.24
5317.21
90.5681
000.1
0326.0
9917.0
5825.0
2988.0
7113.0
0138.02
6754.11
27.1191
520.1
7218.0
5229.0
9917.0
7306.0
5651.0
4967.7
1693.01
43.8591
050.1
6289.0
1799.0
5229.0
8801.0
5710.0
2545.0
3104.9
06.1502
001.1
0000.1
0000.1
1799.0
4000.0
0000.0
8000.0
5904.9
11.8322
002.1
llac
eht
fo
evitavired
eht
si
atleD
.ecirp
esicrexe
detacidni
eht
htiw
noitpo
na
rof
seitivitisnes
selohcS-kcalB
eht
era
agev
dna
atleD
derusaem
,ytilitalov
deilpmiehtottcepser
htiweulavtuprollacehtfoevitaviredehtsiageV
.ecirp
gniylrednuehtot
tcepserhtiweulav
yenom-eht-ta
eht
fo
agev
eht
ot
ekirts
hcae
rof
agev
eht
fo
oitar
eht
syalpsid
elbat
ehT
.lov
fo
esaercni
na
ot
esnopser
eulav
eht
sa
eht
ni
debircsed
sa
,stniop
atad
war
eht
ni
segnahc
eulav
llac
eht
morf
devired
era
)X(tΠ
no
sdnuob
reppu
dna
rewol
ehT
.noitpo
:)robiL
RUE
dna
DSU
ot
refer
t q
dna
t r
,elbacilppa
erehw
tnecrep(
stluser
etaidemretni
dna
stupni
rehtO
.txet
1−
t t S F
t
F
t q
t
r
t
S
etaD
91.0
17.3621
7734.2
0576.1
70.6621
8002guA70
45.0
94.2241
6032.2
0850.0
51.0341
2102ceD12
27

DSU-RUE
rof
scitsongaid
dna
ataD
:2
elbaT
9002yaM22
)X(
Π
dnuob
reppU
dnuob
rewoL
ageV
atleD
eulav
llaC
ytilitaloV
1−
X
X
t
F
1701.0
0071.0
0000.0
8734.0
0009.0
42970.0
0573.51
550.0-
8223.1
2252.0
5093.0
0071.0
7597.0
0057.0
55840.0
0080.51
820.0-
8953.1
8525.0
9676.0
5093.0
0000.1
7605.0
44420.0
5252.51
000.0
4993.1
7218.0
6968.0
9676.0
0797.0
0052.0
45900.0
0002.61
330.0
5544.1
9809.0
0000.1
6968.0
2044.0
0001.0
52300.0
0553.71
760.0
7394.1
1102voN81
)X(
Π
dnuob
reppU
dnuob
rewoL
ageV
atleD
eulav
llaC
ytilitaloV
1−
X
X
t
F
3801.0
7731.0
0000.0
0734.0
0009.0
30590.0
0082.91
860.0-
0062.1
8181.0
6313.0
7731.0
3597.0
0057.0
14350.0
3152.71
330.0-
3803.1
4864.0
9985.0
6313.0
0000.1
2105.0
80320.0
0551.51
000.0
5253.1
5217.0
1918.0
9985.0
0797.0
0052.0
19700.0
8358.31
720.0
5983.1
8509.0
0000.1
1918.0
2044.0
0001.0
04200.0
0571.31
050.0
9914.1
:)elbacilppa
erehw
tnecrep(
stluser
etaidemretni
dna
stupni
rehtO
.1
elbaT
ot
etontoof
eht
eeS
1−
tS
F
q
r
S
etaD
tF
t
t
t
t
130.0
4993.1
0609.0
1313.0
8993.1
9002yaM22
200.0
5253.1
0991.1
6652.0
5253.1
1102voN81
28

snoitpaws
raey-01
otni
raey-2
rof
scitsongaid
dna
ataD
:3
elbaT
3102yaM10
)X(tΠ
dnuob
reppU
dnuob
rewoL
ageV
atleD
eulav
llaC
ytilitaloV
X
F−
X
1620.0
4370.0
0000.0
1030.0
1699.0
0020.0
4755.05
84.0
002-
2161.0
8962.0
4370.0
6864.0
8498.0
8010.0
0308.63
84.1
001-
8673.0
3214.0
8962.0
3997.0
5067.0
2700.0
0661.43
89.1
05-
9954.0
1605.0
3214.0
2329.0
7776.0
7500.0
4482.33
32.2
52-
8955.0
4306.0
1605.0
0000.1
0195.0
5400.0
0055.23
84.2
0
3746.0
6086.0
4306.0
7620.1
1605.0
5300.0
0790.23
37.2
52
0817.0
0777.0
6086.0
3900.1
5624.0
7200.0
2317.13
89.2
05
6038.0
9498.0
0777.0
4488.0
4292.0
6100.0
9922.13
84.3
001
9149.0
0000.1
9498.0
5045.0
6821.0
6000.0
3249.03
84.4
002
3102peS50
)X(tΠ
dnuob
reppU
dnuob
rewoL
ageV
atleD
eulav
llaC
ytilitaloV
X
F−
X
7901.0
6651.0
0000.0
0542.0
3459.0
4020.0
0975.23
90.2
002-
4162.0
1233.0
6651.0
3586.0
3318.0
1210.0
4139.82
90.3
001-
5214.0
2634.0
1233.0
8588.0
3107.0
8800.0
1628.72
95.3
05-
5674.0
7405.0
2634.0
7559.0
3936.0
4700.0
5793.72
48.3
52-
2645.0
8375.0
7405.0
0000.1
8575.0
2600.0
0520.72
90.4
0
9016.0
2536.0
8375.0
9710.1
8215.0
1500.0
1637.62
43.4
52
9866.0
3717.0
2536.0
0110.1
0254.0
2400.0
6684.62
95.4
05
1867.0
5738.0
3717.0
2739.0
7143.0
9200.0
1511.62
90.5
001
0998.0
0000.1
5738.0
0276.0
9081.0
2100.0
8837.52
90.6
002
:era
setar
paws
drawrof
raey-01
otni
-2
ehT
.1
elbaT
ot
etontoof
eht
eeS
t F
etaD
1974.2
3102yaM10
8880.4
3102peS50
29

snoitcirtser
egartibra-on
dna
noitalopartxE
:1
erugiF
9002beF52:noitcnufnoitaulavllaC
9002beF52:elimsdetalopretnI
07
002
06
051 001
05
05
04
0
03
059
009
058
008
057
007
056
006
059
009
058
008
057
007
056
006
2102ceD12:noitcnufnoitaulavllaC
2102ceD12:elimsdetalopretnI
053 003
03
052
52
002 051
02
001 05
51
0
0081
0071
0061
0051
0041
0031
0021
0011
0081
0071
0061
0051
0041
0031
0021
0011
evitanretla
na
ot
)tolp
kcalb(
noitalopartxe
enil-tafl
htiw
enilps
cibuc
depmalc
eht
fo
stluser
eht
serapmoc
wor
hcae
ni
lenap
tfel
ehT
gnitluser
noitcnuf
noitaulav
llac
eht
serapmoc
wor
hcae
ni
lenap
thgir
ehT
.stniop
tonk/atad
tupni
eht
kram
stod
eulB
.)tolp
der(
.stniop
tonk/atad
tupni
eht
ot
gnidnopserroc
secirp
esicrexe
eht
kram
stod
eulB
.emehcs
noitalopartxe
dna
noitalopretni
hcae
morf
P&S
ni
ecirp
esicrexe
eht
si
lenap
hcae
ni
sixa-x
ehT
.xedni
005
P&S
eht
no
snoitpo
htnom-3
fo
seitilitalov
deilpmi
era
atad
ehT
P&S
ni
secirp
llac
era
slenap
thgir
eht
ni
sexa-y
eht
;tnecrep
ni
seitilitalov
deilpmi
era
slenap
tfel
eht
ni
sexa-y
ehT
.smret
xedni
005
.stinu
xedni
005
30

snoitpo
XPS
htnom-3
:elpmaxe
noitatupmoC
:2
erugiF
noitcnufnoitaulavllaC
elimsdetalopretnI
03.0
42
52.0
22
02.0
02
51.0
81
01.0
61
50.0
41
00.0
21
2.0
1.0
.0
1.0(cid:2)
2.0(cid:2)
3.0(cid:2)
2.0
1.0
.0
1.0(cid:2)
2.0(cid:2)
3.0(cid:2)
noitcnufytisnedytilibaborP
noitcnufnoitubirtsidevitalumuC
0.1 8.0 6.0 4.0 2.0 0.0
2.0
1.0
.0
1.0(cid:2)
2.0(cid:2)
3.0(cid:2)
2.0
1.0
.0
1.0(cid:2)
2.0(cid:2)
3.0(cid:2)
neewteb
secnereffid
lanoitroporp
era
slenap
ruof
lla
ni
sexa-x
eht
fo
stinu
ehT
.2102
,12
.ceD
:stolp
der
;8002
,7
.guA
:stolp
kcalB
trapa(
seulav
eht
dna
stod
yb
dekram
era
stniop
tonk/atad
tupnI
.level
xedni
drawrof
eht
dna
level
xedni
erutuf
ro
ecirp
esicrexe
eht
.tnecrep
ni
erasixa-y
ehtno
seitilitalov
deilpmI
.elims
detalopretni
eht
dna
atadtupni
:tfel
reppU
.1
elbaT
ni
deyalpsid
)seitisned
morf
fo
noitcarf
a
sa
desserpxe
era
sixa-y
eht
no
secirp
llaC
.elims
detalopretni
eht
gnisu
detaulave
,noitcnuf
noitaulav
llac
:thgir
reppU
eht
fo
noitcarf
a
sa(
520.0
=
Δ
ezis
petS
.snoitcnuf
ytisned
dna
noitubirtsid
lartuen-ksir
:slenap
mottoB
.level
xedni
drawrof
eht
sdne
005
P&S
eht
ytilibaborp
eht
sa
daer
eb
nac
lenap
tfel
mottob
eht
ni
tolp
eht
,sixa-x
eht
no
tniop
yna
roF
.)level
xedni
drawrof
.shtnom
3
ni
ssel
ro
level
xedni
drawrof
eht
morf
ecnereffid
lanoitroporp
taht
ta
31

Figure 3: Risk-neutral S&P 500 tail risk
Probabilityofa3(cid:2)monthdeclineofatleast20percent
1750
30 Lehman debtdeal
1500
25 Greece
20 1250
15 quant
1000
10
5
750
0
2006 2007 2008 2009 2010 2011 2012 2013 2014
99(cid:2)thpercentileoflossdistribution
60
1750
quant
1500
50 debtdeal
1250
40 Lehman
1000
30
750
20 Greece
2006 2007 2008 2009 2010 2011 2012 2013 2014
Upper panel:Risk-neutral probability of a 3-month decline of at least 20 percent (black plot,
left axis). Lower panel: (−1)×first percentile of the risk-neutral cumulative distribution of
3-month S&P 500 price returns, percent (black plot, left axis). Δ = 0.025, Nov. 21, 2005 to
Mar. 20, 2014. Purple plot (right axis): logarithm of the S&P 500 index; axis labels show the
index level.
32

ksir
liat
detamitse
no
Δ
gniyrav
fo
tceffE
:4
erugiF
03 52 02 51 01 5 0
4102
3102
2102
1102
0102
9002
8002
7002
6002
:tolp
kcalB
.4102
,02
.raM
ot
5002
,12
.voN
,tnecrep
02
tsael
ta
fo
005
P&S
eht
ni
enilced
htnom-3
a
fo
ytilibaborp
lartuen-ksiR
.001.0=
Δ
:)sixa
thgir(
tolp
egnaro
;520.0
=
Δ
33

ksir
liat
GIA
lartuen-ksiR
:5
erugiF
04
0001
03
057
02
005
01
052
0
luJ
rpA
naJ
tcO
.520.0
=
Δ
,8002
,21
.peS
ot
7002
,1
.tcO
,tnecrep
02
tsael
ta
fo
enilced
htnom-3
a
fo
ytilibaborp
lartuen-ksir
:)sixa
tfel(
tolp
kcalB
.ecirp
ytiuqe
GIA
detsujda-tilps
:)sixa
thgir(
tolp
elpruP
34

DSU-RUE
rof
noitalopretni
elims
ytilitaloV
:6
erugiF
smretycnerrucnielimsdetalopretnI
smretatledllacnielimsdetalopretnI
91
91
81
81
71
71
61
61
51
51
41
41
31
31
521.0
1.0
570.0
50.0
520.0
.0
520.0(cid:2)
50.0(cid:2)
570.0(cid:2)
1.0(cid:2)
521.0(cid:2)
09.0
57.0
05.0
52.0
01.0
aiv
tuo
deirrac
,noitalopretni
elims
laitini
eht
dna
atad
war
:lenap
tfeL
.1102
,81
.voN
:stolp
der
;9002
,22
.yaM
:stolp
kcalB
.ecaps-)σ,X(
ni
detupmocer
elims
ytilitalov
:lenap
thgiR
.stinu
atled
ni
si
sixa-x
,enilps
cibuc
depmalc
35

snoitpo
DSU-RUE
htnom-3
:elpmaxe
noitatupmoC
:7
erugiF
noitcnufnoitaulavllaC
smretycnerrucnielimsdetalopretnI
21.0
91
01.0
81
80.0
71
60.0
61
40.0
51
20.0
41
00.0
31
521.0
1.0
570.0
50.0
520.0
.0
520.0(cid:2)
50.0(cid:2)
570.0(cid:2)
1.0(cid:2)
521.0(cid:2)
521.0
1.0
570.0
50.0
520.0
.0
520.0(cid:2)
50.0(cid:2)
570.0(cid:2)
1.0(cid:2)
521.0(cid:2)
noitcnufytisnedytilibaborP
noitcnufnoitubirtsidevitalumuC
0.1 8.0 6.0 4.0 2.0 0.0
521.0
1.0
570.0
50.0
520.0
.0
520.0(cid:2)
50.0(cid:2)
570.0(cid:2)
1.0(cid:2)
521.0(cid:2)
521.0
1.0
570.0
50.0
520.0
.0
520.0(cid:2)
50.0(cid:2)
570.0(cid:2)
1.0(cid:2)
521.0(cid:2)
ecirp
esicrexe
eht
neewteb
ecnereffid
lanoitroporp
eht
sa
desserpxe
sexa-x
.1102
,81
.voN
:stolp
der
;9002
,22
.yaM
:stolp
kcalB
reppU
.2
elbaT
ni
deyalpsid
)seitisned
morf
trapa(
seulav
eht
dna
stod
yb
dekram
era
stniop
tonk/atad
tupnI
.etar
drawrof
eht
dna
secirp
llaC
.elims
detalopretni
eht
gnisu
detaulave
,noitcnuf
noitaulav
llac
:thgir
reppU
.elims
detalopretni
eht
dna
atad
tupni
:tfel
a
sa(
500.0
=
Δ
ezis
petS
.snoitcnuf
ytisned
dna
noitubirtsid
lartuen-ksir
:slenap
mottoB
.etar
drawrof
eht
fo
noitcarf
a
sa
desserpxe
sdne
orue
eht
ytilibaborp
eht
sa
daer
eb
nac
lenap
tfel
mottob
eht
ni
tolp
eht
,sixa-x
eht
no
tniop
yna
roF
.)etar
drawrof
fo
noitcarf
.htnom
1
ni
ssel
ro
etar
drawrof
eht
morf
ecnereffid
lanoitroporp
taht
ta
36

Figure 8: Risk-neutral currency tail risk: EUR-USD
1.60
15 Greece LTROs
1.50
10
1.40
Lehman
5 1.30
1.20
0
2006 2007 2008 2009 2010 2011 2012 2013 2014
8 1.60
6
1.50
4
1.40
2
0 1.30
(cid:2)2 Lehman Greece LTROs
1.20
2006 2007 2008 2009 2010 2011 2012 2013 2014
Upper panel: Black (orange) plot (left axis): risk-neutral probability of a 1-month dollar
appreciation (depreciation) of at least 7.5 percent vis-`a-vis the euro. Lower panel: Difference
between risk-neutral probability of a 1-month dollar appreciation of at least 7.5 percent vis-
`a-vis the euro minus that of depreciation. Purple plot (right axis) in both panels: EUR-USD
spot exchange rate. Jan. 3, 2006 to Mar. 25, 2014, Δ = 0.005.
37

snoitpaws
raey-01
otni
raey-2
:elpmaxe
noitatupmoC
:9
erugiF
noitcnufnoitaulavllaC
elimsdetalopretnI
05
020.0
54
510.0
04
010.0
53
500.0
03
000.0
52
052
002
051
001
05
0
05(cid:2)
001(cid:2)
051(cid:2)
002(cid:2)
052
002
051
001
05
0
05(cid:2)
001(cid:2)
051(cid:2)
002(cid:2)
noitcnufytisnedytilibaborP
noitcnufnoitubirtsidevitalumuC
0.1
3102yaM10
8.0
3102peS50
6.0
3102yaM10
3102peS50
4.0 2.0 0.0
00.8
00.7
00.6
00.5
00.4
00.3
00.2
00.1
00.0
00.8
00.7
00.6
00.5
00.4
00.3
00.2
00.1
00.0
spb
ni
ecnereffid
eht
sa
desserpxe
era
sexa-x
eht
,slenap
reppu
owt
eht
nI
.3102
,5
.peS
:stolp
der
;3102
,1
yaM
:stolp
kcalB
.etar
paws
drawrof
eht
sa
desserpxe
era
sexa-x
eht
,slenap
rewol
owt
eht
nI
.etar
paws
drawrof
eht
dna
ecirp
esicrexe
eht
neewteb
eht
dna
atad
tupni
:tfel
reppU
.3
elbaT
ni
deyalpsid
)seitisned
morf
trapa(
seulav
eht
dna
stod
yb
dekram
era
stniop
tonk/atad
tupnI
etar
tseretni
ni
desserpxe
secirp
llaC
.elims
detalopretni
eht
gnisu
detaulave
,noitcnuf
noitaulav
llac
:thgir
reppU
.elims
detalopretni
no
tniop
yna
roF
.)pb1(
1000.0
=
Δ
ezis
petS
.snoitcnuf
ytisned
dna
noitubirtsid
lartuen-ksir
:slenap
mottoB
.lamiced
a
sa
stinu
drawrof
gnidnopserroc
eht
ta
sdne
etar
paws
raey-01
eht
ytilibaborp
eht
sa
daer
eb
nac
lenap
tfel
mottob
eht
ni
tolp
eht
,sixa-x
eht
.sraey
2
ni
ssel
ro
etar
paws
38

Figure 10: Risk-neutral interest-rate tail risk
Probabilityofchangeinexcessof(cid:3)200bps
4.00
10
8
3.50
6
3.00
4
2.50
2
Apr Jul Oct Jan Apr
Probabilityofchangeinexcessof(cid:3)100bps
4.00
24
22
3.50
20
3.00
18
16 2.50
Apr Jul Oct Jan Apr
Probabilityofspecificratelevels
4.00
35
30
25 3.50
20
15 3.00
10
5
2.50
Apr Jul Oct Jan Apr
Upper panel: black (blue) plot (left axis) risk-neutral probability of a 2-year increase (decline)
of at least 200 bps in the 10-year swap rate vis-`a-vis the current forward swap rate. Center
panel: black (blue) plot (left axis) risk-neutral probability of a 2-year increase (decline) of at
least 100 bps in the 10-year swap rate. Lower panel: black (blue) plot (left axis) risk-neutral
probability that the 10-year swap rate will be 5 percent or higher (3 percent or lower) in 2
years. Purple plot (right axis): forward swap rate. Feb. 1, 2013 to May 2, 2014; Δ = 0.0001
(1 bp).
39
