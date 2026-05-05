---
id: pdf-2248d6cdc39f
type: pdf
title: 'The Study: 2-Day AVWAP Rule + Momentum Signal in Day Trading'
url: ''
authors: []
ingested_at: '2026-04-29T16:26:38Z'
content_hash: sha256:cc6230f5bf7150ffacffdddea75317e0eca63d243e4db6723217d95479f2a124
source_path: raw/pdf/pdf-2248d6cdc39f.pdf
domains:
- trading-and-markets
nlm_corpus_ids:
- ccbda94f-7251-42bb-864f-0e1c9850f7ad
wiki_pages:
- wiki/entities/matthew-ryan.md
- wiki/entities/tradytics.md
- wiki/concepts/anchored-vwap.md
- wiki/concepts/two-day-avwap-rule.md
- wiki/concepts/stochastic-momentum-signal.md
- wiki/concepts/market-net-flow.md
- wiki/concepts/trend-confluence.md
- wiki/concepts/bracket-order-risk-management.md
- wiki/concepts/scale-out-profit-taking.md
meta:
  page_count: 14
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/The Study_ 2-Day AVWAP Rule
    Momentum Signal in Day.2r Trading__2248d6cd.pdf
---
w.andrew.m.grant@gmail.com 08 Apr 2023
The Study
Using the ‘2-Day AVWAP Rule + Momentum Signal’
in Day Trading to become Consistently Profitable
byMatthew Ryan

w.andrew.m.grant@gmail.com 08 Apr 2023
Abstract:in order to become consistently profitable, you need arepeatable, systematic processwith a win
rate of 70% or higher.I will give you that by identifying3 key aspects that we must understand in order to be
successful. The market must either conform to what we need or we do not trade, plain and simple. When you
commit to these three criteria, you will drastically raise the probability that your trades will be profitable.
Hypothesis:New traders lack consistency because ofa limited understanding of these 3 key aspects:
1. Market Context
2. Execution
3. Risk Management
Understanding MARKET CONTEXTwill help us determinethe direction of the trend. I define
EXECUTION as finding high probability entries and exits, or timing the market, which can be
extremely difficult. Proper RISK MANAGEMENTfocuseson position sizing, implementing (and
sticking to) stop losses and defining take profit levels. Do not favor one aspect over the other. Master
all three.
1. INTRODUCTION
This study aims to test the validity of using the 2-Day + Momentum Signal as a technical analysis tool in
intraday trading. The results of this study shows that trading using the 2-Day + Momentum Signal leads to
profitable results, but in case of non-profitable results, a stop-loss is required.
1.1 TOOLS NEEDED
Multiple Anchored VWAP to establish trend
Stochastic Indicator (with precise parameters) for high probability entries
Bracket Orders with automatic STOP LOSS and TAKE PROFIT settings
Additional- Market Net Flow tool byTradytics
2. ESTABLISHING TREND
Trend is the overall direction of a market or an asset's price. Anchor aVWAP to the open of the previous
trading day and to the open of the current trading day.

w.andrew.m.grant@gmail.com 08 Apr 2023
Notice how price reacts favorably to VWAP in trending conditions.Learn more about VWAP here: (VWAP)

w.andrew.m.grant@gmail.com 08 Apr 2023
2.1 VWAP RULES
If price isABOVEboth VWAPS we are in a potentialUPTREND and look for bullish A+ setups only.
If price isBELOWboth VWAPS we are in a potentialDOWNTREND and look for bearish A+ setups only.
We do not trade if price isIN BETWEENboth VWAPSas there is no clear trend established.
2.1.2 VWAP APPLICATION
Your ability to commit these rules to memory will be essential for success. During times of heightened
emotions, these rules must be followed. Eliminate the noise, only trade the trend. No trend, no trade.
2.2 MARKET NET FLOW by TRADYTICS
We can also determine the direction of the trend by using theMarket Net Flowtool by Tradytics, which
shows us how option participants are affecting dealers, forcing them to hedge. Dealer Hedging is a topic that
is too extensive to cover here, but I would encourage everyone to come to an advanced understanding of
these concepts (I implement my understanding of Gamma/Vanna levels for every trade). Here is a tutorial on
the basics of usingMNFby Tradytics:https://www.youtube.com/watch?v=R8-eJ7IJhco&t=1s
2.2.1 BULLISH MNF EXAMPLE
Calls (green line) above Puts (red line) with Puts below zero line

w.andrew.m.grant@gmail.com 08 Apr 2023
2.2.2 BULLISH CONFLUENCE
When price is ABOVE both VWAPS (uptrend), pair with BULLISH MNF for confluence of trend.
2.2.3 BEARISH MNF EXAMPLE
Puts (red line) above Calls (green line) with Calls below zero line
2.2.4 BEARISH CONFLUENCE
When price is BELOW both VWAPS (downtrend), pair with BEARISH MNF for confluence of trend

w.andrew.m.grant@gmail.com 08 Apr 2023
2.2.5 NO DIVERGENCE MNF EXAMPLE
No divergence of either Calls (green line) or Puts (red line)
2.2.6 NO DIVERGENCE CONFLUENCE
When price is between both VWAPS (no trend) and there is no divergence between Calls or Puts, do not take
trades.
2.2.7 ADDITIONAL FACTORS
Sometimes price will be above (or below) both VWAPS but there will be no MNF confluence. It is
recommended to wait for divergence before placing trades. Divergence can show up at any time of the
trading day. Patience is required.

w.andrew.m.grant@gmail.com 08 Apr 2023
3. EXECUTION
What we are looking for with execution isMOMENTUMentering the market. We determine momentum with
the Stochastic Indicator. When used correctly, the Stochastic Indicator can signal when momentum is coming
into the market, if the trend is continuing, or when the trend is reversing.
3.1 MOMENTUM INDICATOR
Once we have established the trend, the next step is to look for A+ entries. Execution is key. Nailing entries
using the MOMENTUM INDICATOR will drastically lower the risk of getting stopped out.
3.1.2 INDICATOR PARAMETERS
There are certain parameters that we need to reconfigure to have the Stochastic indicator operate in this
manner. Change the default settings to these:
%K period: 5
%D period: 3
Smoothing (or length) : 2
Overbought: 80*
Oversold: 20*
3.1.3 NOTEWORTHY
Once these settings have been reconfigured, let’s rename this indicator to the Momentum Signal and throw
away any/all preconceived negative connotations that we may have held previously about indicators.

w.andrew.m.grant@gmail.com 08 Apr 2023
3.1.3b UPDATE (01/17/2023)
TradingView has removed the Stochastic Slow indicator that you see on my chart. But ANY Stochastic
Indicator will work as long as you have the correct settings. The default indicator will suffice.
3.1.3c TradingView’s DEFAULT STOCHASTIC INDICATOR SETTINGS
3.1.4 RULES FOR MOMENTUM BASED ENTRIES
ONLY enter LONG positions when %K is under Oversold condition
ONLY enter SHORT positions when %K is above Overbought condition
WE DO NOT OPEN POSITIONS WHEN %K is anywhere in between the parameters
(Entering when %K crosses %D and %Dcurls backintothe direction of your trade is a higher probability
entry but limits your max profit (waiting for confirmation)
WHEN TRADING DIVERGENCES, WAIT FOR THE PULLBACK TO ENTER (setting up higher lows or lower
highs)

w.andrew.m.grant@gmail.com 08 Apr 2023
3.1.5 MOMENTUM SIGNAL EXAMPLE
Entries become higher probability when we wait for proper MOMENTUM SIGNAL positioning.
3.1.6 MOMENTUM SIGNAL WITH HTF CONTINUITY
Entries become even higher probability when lower time frame positioning aligns with higher time frame
positioning (5min %K = 15min %K)

w.andrew.m.grant@gmail.com 08 Apr 2023
3.2 MOMENTUM SIGNAL NOTEWORTHY
a. Pair reversal signals with corresponding reversal candles for higher probability entry
*Hammer candles
*Engulfing candles
*Inside Bar Reversals
b. Fakeouts can occur at %K overbought when trying to breakout
c. Fakeouts can occur at %K oversold when trying to breakdown
d. OVERBOUGHT and OVERSOLD parameters DO NOT mean that the stock itself is either
overbought or oversold. Do not misidentify these signals. THIS IS NOT THE RSI INDICATOR.
3.2.1 INCREASING PROFITABILITY WITH HIGHER PROBABILITYENTRIES
If bullish conditions ( VWAP + MNF confluence), only BUY at %K oversold condition
If bearish conditions (VWAP + MNF confluence), only SELL at %K overbought condition
3.2.2 ADVICE TO TRADERS
NEW TRADERS: Add the Momentum Signal on to your chart and paper trade to get a feel for identifying
DIVERGENCES, CONTINUATIONS and HIGH PROBABILITY ENTRIES. Once you have a solid foundation,
entries will become much easier to trust and the fear of holding through pullbacks will diminish.
INTERMEDIATE/ADVANCED TRADERS: Add the Momentum Signal to your chart and wait for %K parameters
for higher probability setups.
3.2.3 FINAL NOTE
If you miss an entry, do not chase it. There is always another trade.
4. RISK MANAGEMENT
Risk management refers to the processes that are put into place when trading to help keep losses under
control and keep a good risk/reward ratio.

w.andrew.m.grant@gmail.com 08 Apr 2023
4.1 RISK MANAGEMENT CHART
4.1.2 APPLICATION OF RISK MANAGEMENT
NEVER HOLD A LOSS FOR MORE THAN 20%. DO NOT COMPROMISE THIS.
*If you trade options 2DTE or shorter, I do not recommend holding a loss over 15%.
*Do not buy 0DTE after 11:00am EST
*If an option is OTM and there is novolatility, it'slikely to expire worthless
Risk management also includes eliminating the fear of missing out which produces behaviors such as
a. Anticipatory entries (attempting to maximize profit)
b. Oversizing cheap OTM contracts (cheaper is not necessarily better)
c. Buying 0DTE after 11:00am EST (theta burn)
The best risk management is location/timing of entry. Use %K location to ensure higher probability
entries.
4.2 STOP LOSS
When timing entries using the Momentum Signal, we can drastically lower the risk of getting stopped out.
With that said, there will always be unaccounted for variables due to real time fundamental news, economic
data releases, politics, wars, black swan events, institutional buying and selling, and market maker/dealer
hedging of options gamma. It is your job as a trader to understand how all of these factors can affect price
action and apply a stop loss discipline to your trading. Make this non-negotiable.

w.andrew.m.grant@gmail.com 08 Apr 2023
4.2.1 STOP LOSS APPLICATION
Trailing Stops are useful for securing profit. Using a trailing stop can ensure profits but it can also drastically
skew your Risk to Reward ratio, so keep that in mind.
Consider moving a Stop Loss to breakeven once price action moves in your favor, but watch out for
Theta/Implied Volatility swings that can trigger your stops on pullbacks when trading options.
4.2.2 KEY RULES
NEVER LOWER YOUR STOP. NO MATTER WHAT. ONLY MOVE STOPS UP, NEVER MOVE STOPS DOWN. DO
NOT COMPROMISE.
4.3 TAKE PROFIT
The other side of your Stop Loss requires a Take Profit target. These are subjective levels to the individual
trader. Whether it is high of day, low of day, VWAP, previous day’s high/low or previous market structure, I
would suggest having a different level for the type of trade you are placing. For example, if your trade is a
reversal, VWAP or HOD are sufficient levels to target. If you are fading VWAP, LOD is a practical target.
Previous supply and/or demand zones can be useful targets, or EMA’s on higher timeframes.
4.3.1 TAKE PROFIT STRATEGY
I personally set my target to a precise TICK level and then scale out of my position once that target is hit.
Basically, I will sell back 3/4ths of my position, securing my profits, and let the remaining contracts run while
having a trailing stop in place. Some brokers let you do this mechanically with bracket orders, but you may
need to adjust the default settings.
My TICK level is +20-30 ticks in my favor before I begin to scale out, depending on the location of entry and
what type of trade I have entered.
4.3.2 BRACKET ORDERS
Stop loss at -10 ticks below my entry (NO MATTER WHAT)
Taking 3/4ths of my position at +20-30 ticks above my entry (leaving 1/4th of my position as runners, with a
trailing stop) unless the market offers otherwise.
4.3.3 FINAL NOTE
Find what is best for you and your risk to reward ratio. I utilize ticks to teach my trading brain to
focus on process and not dollar amount. Profits will come once your process is solidified. Do not focus
on outcome, focus on process.

w.andrew.m.grant@gmail.com 08 Apr 2023
5. BACKTESTING
Backtesting isthe general method for seeing how wella strategy or model would have done.Backtesting
assesses the viability of a trading strategy by discovering how it would play out using historical data. If
backtesting works, traders and analysts may have the confidence to employ it going forward.
5.1 BACKTESTING RESULTS
TRADES BULLISH BEARISH
WIN 36 38
LOSS 14 12
ACCURACY % 72% 76%
5.1.2 BACKTESTING SUMMARY
As you can see, utilizing the 2 day VWAP -Momentum Signal strategy is effective, but it does require patience.
Waiting for the market to conform to the requirements of the strategy increases the effectiveness of the
strategy. Anticipating the move before it happens decreases the effectiveness of the strategy. No setup, no
trade.
6. CONCLUSION
Consistently profitable trading requires an effective strategy but also patience. Anyone can learn a strategy,
but proper trading psychology is just as important. If you stick to this strategy you can become consistently
profitable.

w.andrew.m.grant@gmail.com 08 Apr 2023
6.1 DISCLAIMER
*THIS IS NOT FINANCIAL ADVICE. I AM NOT A FINANCIAL ADVISOR. THIS INFORMATION IS FOR EDUCATIONAL PURPOSES ONLY.
YOU ALONE ASSUME THE SOLE RESPONSIBILITY OF EVALUATING THE MERITS AND RISKS ASSOCIATED WITH THE USE OF THIS
INFORMATION. UPON THE PURCHASE OF THIS DIGITAL PRODUCT, YOU AGREE THAT THE AUTHOR IS NOT LIABLE FOR LOSS OR
DAMAGES OF ANY KIND RESULTING FROM YOUR USE OF OR INABILITY TO USE THE CONTENT SUCCESSFULLY.
