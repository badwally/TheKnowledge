---
type: concept
slug: trend-filtering
canonical_name: Trend filtering
domains:
  - trading-and-markets
---

# Trend filtering

## Summary

Trend filtering (or trend detection) is the time-series problem of extracting from a noisy observed process the smooth component representing long-term movements; in the Lyxor 2011 framework it is the foundational task of any momentum strategy and is fundamental to most momentum strategies developed in asset management and hedge fund sectors to improve performance and limit portfolio risks [[sources/pdf-5ef2018823c8]].

## Key claims

- The trend of a time series is considered to be the component containing the global change, which contrasts with local changes due to noise; trend filtering concerns not only denoising but must also take into account the dynamics of the underlying process [[sources/pdf-5ef2018823c8]].
- Bruder, Dao, Richard, and Roncalli quote Kendall (1973): "the essential idea of trend is that it shall be smooth," implying that changes in the trend x_t must be smaller than those of the process y_t and that σ(y_t − y_{t-1}) ≫ σ(x_t − x_{t-1}) [[sources/pdf-5ef2018823c8]].
- The modern theory of signal filtering originated in the Second World War with Norbert Wiener (1941) working in the frequency domain and Andrei Kolmogorov (1941) working in the time domain, and was extensively developed by Wold, Whittle, Kalman, Priestley, Box and others in the 1950s–60s [[sources/pdf-5ef2018823c8]].
- In economics, trend filtering dates back at least to Muth (1960) and was extensively studied in the 1980s–90s in the business-cycle literature; today the field is most extensively studied in climatology [[sources/pdf-5ef2018823c8]].
- The development of filtering techniques has evolved with computational power: the Savitzky-Golay smoothing procedure, considered revolutionary when published in 1964, may appear basic today, and is still listed as one of the Analytical Chemistry journal's 10 seminal papers [[sources/pdf-5ef2018823c8]].
- Bruder et al. distinguish two classes of filtering technique used to estimate a trend — linear filters (including moving averages) and nonlinear filters — and argue that moving-average filters undoubtedly represent the model most commonly used in trading strategies because they are intuitive and easy to implement [[sources/pdf-5ef2018823c8]].

## Sources

- [[sources/pdf-5ef2018823c8]]

## Related

- [[concepts/linear-filter-convolution]]
- [[concepts/trend-cycle-decomposition]]
- [[concepts/moving-average-crossover]]
- [[concepts/causal-filter]]
- [[concepts/denoising-bias-tradeoff]]
- [[concepts/trend-following-strategy]]
- [[entities/lyxor-asset-management]]
- [[entities/benjamin-bruder]]
- [[entities/thierry-roncalli]]
