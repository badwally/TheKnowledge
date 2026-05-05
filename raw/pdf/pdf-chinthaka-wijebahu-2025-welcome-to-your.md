---
id: pdf-chinthaka-wijebahu-2025-welcome-to-your
type: pdf
title: Welcome to Your Roadmap To 3DPrinting!
url: ''
authors:
- Chinthaka Wijebahu
ingested_at: '2026-04-29T16:15:54Z'
content_hash: sha256:e6d48c7185bdbbceb2dea981e186330be79c20911b3fb88b3002c48ceb87c9ed
source_path: raw/pdf/pdf-chinthaka-wijebahu-2025-welcome-to-your.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 7
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__6af25b3c.pdf
published_at: '2025'
---
GE Lingo
Key Levels .................................................................................................................................................................. 3
COI (Call Open Interest): .................................................................................................................................................3
POI (Put Open Interest): .................................................................................................................................................3
Open Interest (OI): ............................................................................................................................................................3
pGEX/plus_GEX/+GEX (Positive Gamma Exposure): ............................................................................................3
nGEX/minus_GEX/-GEX (Negative Gamma Exposure): .......................................................................................3
+Trans/Pos Trans/Ptrans (Positive Transition): ......................................................................................................3
-Trans/Neg Trans/Ntrans (Negative Transition): ...................................................................................................3
ZeroGEX/0GEX (Zero Gamma Exposure): .................................................................................................................3
COTMC (Cumulative Out of the Money Calls): ........................................................................................................4
CITMP (Cumulative In the Money Puts): ....................................................................................................................4
COTMP (Cumulative Out of the Money Puts): .........................................................................................................4
CITMC (Cumulative In the Money Calls): ...................................................................................................................4
TGZ (True Gamma Zero): ...............................................................................................................................................4
TDZ (True Delta Zero): ....................................................................................................................................................4
The Greeks ................................................................................................................................................................. 5
Charm: ..................................................................................................................................................................................5
Delta: ....................................................................................................................................................................................5
Gamma: ...............................................................................................................................................................................5
Vanna: ..................................................................................................................................................................................5
Other Terms to Know ............................................................................................................................................. 6
Call Option: .........................................................................................................................................................................6
Put Option: ..........................................................................................................................................................................6
Cumulative Tick: ................................................................................................................................................................6
Filtered Tick: .......................................................................................................................................................................6
ITM (In the Money): ...........................................................................................................................................................6
OTM (Out of the Money): ................................................................................................................................................6
GEX Ratio: ...........................................................................................................................................................................7
DTE (Days to Expiration): ...............................................................................................................................................7
0 DTE (Zero Days to Expiration): .................................................................................................................................7
EMA21: .................................................................................................................................................................................7
SMA50:.................................................................................................................................................................................7

GE Lingo
COI (Call Open Interest): strike price with the largest call open interest in the entire
option complex.
POI (Put Open Interest): strike price with the largest put open interest in the entire
option complex.
Open Interest (OI): amount of open interest associated with the option complex.
Note: the smaller the open interest, the lower the impact of dealer activities. The
threshold for open interest to be deemed significant (by GammaEdge) is 100,000
contracts.
pGEX/plus_GEX/+GEX (Positive Gamma Exposure): largest call-dominated
positive gamma exposure in the entire option complex.
nGEX/minus_GEX/-GEX (Negative Gamma Exposure): largest put-dominated
negative gamma exposure (nGEX) in the entire option complex.
+Trans/Pos Trans/Ptrans (Positive Transition): top of the GammaEdge transition
zone. This strike and all others above have net positive gamma (call-dominated)
for the entire option complex.
-Trans/Neg Trans/Ntrans (Negative Transition): bottom of the GammaEdge
transition zone. This strike and all others below have net negative gamma (put-
dominated) for the entire option complex.
ZeroGEX/0GEX (Zero Gamma Exposure): ZeroGEX is the transition point for the
model where cumulative gamma between puts and calls is “theoretically”
balanced. This value will generally be between the +Trans/Pos Trans and
-Trans/Neg Trans levels previously described. This value is spot-price dependent.

GE Lingo
COTMC (Cumulative Out of the Money Calls): price in the option complex where
calls begin to move from OTM-dominance to ITM-dominance. Spot price above
this level will result in more calls being ITM than OTM; spot price below this level
will produce the opposite. Note: spot price is generally below this value.
CITMP (Cumulative In the Money Puts): price in the option complex where puts
move from ITM-dominance to OTM-dominance. Spot price above this level will
result in more puts being OTM than ITM; spot price below this level will produce
the opposite. Note: spot price is generally below this value.
COTMP (Cumulative Out of the Money Puts): price in the option complex where
puts begin to move from OTM-dominance to ITM-dominance. Spot price below
this level will result in more puts being ITM than OTM; spot price above this level
will produce the opposite. Note that the spot price is generally above this value.
CITMC (Cumulative In the Money Calls): price in the option complex where calls
begin to move from ITM-dominance to OTM-dominance. Spot price below this
level will result in more calls being OTM than ITM; spot price above this level will
produce the opposite. Note: spot price is generally above this value.
TGZ (True Gamma Zero): a theoretical balance point (price) of an option complex
where the put gamma and call gamma are exactly balanced. TGZ is not price
(spot) sensitive. It may better indicate where average dealer gamma levels
transition from net positive exposure to net negative exposure and visa-versa.
TDZ (True Delta Zero): a theoretical balance point (price) of an option complex
where the put delta and call delta are balanced. TDZ is not price (spot) sensitive.
It may better indicate the area where average dealer delta levels transition from
net positive exposure to net negative exposure and visa-versa.

GE Lingo
Charm: measure of the rate of change of an option's delta in relation to changes
in time to expiration.
Delta: measure of the change in the option price in relation to the change in the
underlying asset price.
Gamma: Gamma is the rate of change of an option’s delta in relation to changes
in the underlying asset price.
Vanna: measure of the rate of change of an option's delta in relation to changes
in the implied volatility of the underlying asset.

GE Lingo
Call Option: gives the buyer the right, but not the obligation, to purchase 100
shares of an underlying stock at a predetermined price (i.e., strike price) within a
specified period of time (until the expiration date). Call options be both bought
and sold.
Put Option: gives the buyer the right, but not the obligation, to sell 100 shares of
an underlying stock at a predetermined price (i.e., strike price) within a specified
period of time (until the expiration date). Put options can be other bought and
sold.
Cumulative Tick: a measure of the number of stocks that are trading on an uptick
minus the number that are trading on a downtick. This can help traders determine
whether market sentiment is bullish or bearish.
Filtered Tick: a filtered view of the Cumulative Tick in some measured time interval
which focuses on tick transactions registering +1000 or -1000 or greater. This
helps to get a sense of large/significant/aggressive transactions.
ITM (In the Money): For call options, ITM means the strike price is below the
market price of the underlying asset. For put options, ITM means the strike price
is above the market price of the underlying asset. In-the-money options have
intrinsic value, as exercising the option would result in a profit.
OTM (Out of the Money): For call options, OTM means the strike price is above
the market price of the underlying asset. For put options, OTM means the strike
price is below the market price of the underlying asset. Out of the Money options
have no intrinsic value, only time value (prior to expiration).

GE Lingo
GEX Ratio: ratio of cumulative put gamma exposure to cumulative call gamma
exposure. As it relates to the GammaEdge “Winged Chart” ($c command), the red
wing is cumulative put gamma exposure and the green wing is cumulative call
gamma exposure.
DTE (Days to Expiration): Number of days until the option contract expires.
0 DTE (Zero Days to Expiration): Option contract that expires at the end of the
current trading session.
EMA21: 21-day exponential moving average of price or whatever input is being
measured.
SMA50: 50-day simple moving average of price or whatever input is being
measured.

GE Lingo
