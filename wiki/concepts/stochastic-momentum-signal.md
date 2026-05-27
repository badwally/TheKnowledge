---
schema_version: 1
type: concept
slug: stochastic-momentum-signal
canonical_name: Stochastic Momentum Signal
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Stochastic Momentum Signal

## Summary

A re-parameterized Stochastic oscillator that Matthew Ryan repurposes as a momentum-entry timing tool — distinct from the conventional overbought/oversold reading of the indicator — using %K=5, %D=3, smoothing=2, with overbought=80 and oversold=20, and renamed by Ryan to "Momentum Signal" so traders abandon prior Stochastic priors [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Key claims

- Required parameter changes from the default Stochastic settings: %K period 5, %D period 3, smoothing (length) 2, overbought 80, oversold 20 [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Ryan explicitly renames the indicator to "Momentum Signal" so traders throw away any preconceived negative connotations they may have held previously about indicators [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- The overbought and oversold parameters do NOT mean the stock itself is overbought or oversold — Ryan stresses this is not the RSI indicator and that misidentifying the signals will lead to incorrect entries [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Entry rules: only enter LONG when %K is under the oversold condition; only enter SHORT when %K is above the overbought condition; do not open positions when %K is anywhere between the parameters [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Higher-probability entry waits for %K to cross %D and for %D to curl back into the direction of the trade — at the cost of limiting maximum profit because the trader is waiting for confirmation [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- When trading divergences, the trader must wait for the pullback to enter (setting up higher lows or lower highs) [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Reversal-signal probability is increased by pairing with corresponding reversal candles — hammer candles, engulfing candles, and inside bar reversals [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Fakeouts can occur at %K overbought when price is trying to break out, and at %K oversold when price is trying to break down [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Multi-timeframe variant: entry probability further increases when lower-timeframe %K positioning aligns with higher-timeframe %K positioning (e.g., 5-minute %K equals 15-minute %K) [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- TradingView removed the Stochastic Slow indicator after publication; Ryan notes any Stochastic indicator works as long as the parameters are correct, and the default indicator suffices [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Sources

- [[sources/pdf-2248d6cdc39f]]
- [[sources/pdf-6ba2dc608ac8]]

## Related

- [[concepts/two-day-avwap-rule]]
- [[concepts/trend-confluence]]
- [[concepts/bracket-order-risk-management]]
- [[entities/matthew-ryan]]
