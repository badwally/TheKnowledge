---
schema_version: 1
type: concept
slug: option-contract-anatomy
canonical_name: Five-part option contract anatomy
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Five-part option contract anatomy

## Summary

A pedagogical decomposition of an options contract into five components — underlying stock, option type, strike price, expiration date, and premium — used by Nikonomics to give complete beginners a fixed mental schema before walking them through the trade execution loop on Webull [[sources/pdf-5a5936689043]].

## Key claims

- Nikonomics enumerates five parts of options that "you should know" before trading: underlying stock, option type, strike price, expiration date, and premium [[sources/pdf-5a5936689043]].
- Underlying stock is defined as the stock the options are tied to (Tesla, Apple, Amazon, S&P 500 are given as examples) — "it's just what stock we are trading" in the simplified gloss [[sources/pdf-5a5936689043]].
- Option type is defined as one of two — call options or put options. A call option goes up in value if the stock price goes up; a put option goes up in value if the stock price goes down [[sources/pdf-5a5936689043]].
- Strike price is defined as the predetermined price at which the holder has the right to buy or sell the underlying stock [[sources/pdf-5a5936689043]].
- Expiration date is defined as the date on which the option contract expires and the holder must exercise their right to buy or sell — Nikonomics later operationalizes this as "at this date, it will be worth $0" given the no-exercise framing [[sources/pdf-5a5936689043]].
- Premium is defined as the fee the holder pays to purchase the option contract, determined by supply and demand in the options market and influenced by the price of the underlying stock, time until expiration, and the level of volatility [[sources/pdf-5a5936689043]].
- Nikonomics frames the five-part schema as deliberately oversimplified — "the basics of options if I had to explain it to a 5 year old" — to lower the activation energy for beginners before introducing OTM/ITM, expiration selection, and order types [[sources/pdf-5a5936689043]].

## Sources

- [[sources/pdf-5a5936689043]]

## Related

- [[concepts/options-premium-trading]]
- [[concepts/otm-vs-itm-strikes]]
- [[entities/nikonomics]]
