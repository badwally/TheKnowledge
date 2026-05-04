---
type: concept
slug: narrative-intensity
canonical_name: Narrative intensity
domains:
  - trading-and-markets
---

# Narrative intensity

## Summary

Narrative intensity is Bhargava, Lou, Ozik, Sadka, and Whitmore's (2022) media-coverage-based measure of attention paid to a narrative — the proportion of articles relevant to that narrative relative to all news articles collected on a given day in a respective reservoir; "negative intensity" is the variant restricted to articles expressing a negative tone, used in the paper's main analysis because it captures both coverage volume and directionality [[sources/pdf-19445750a197]].

## Key claims

- Articles published by over 150,000 global digital media sources are collected daily and assigned to reservoirs based on each article's general topic (e.g., domestic matters, international politics) and the asset covered (e.g., corporations, currencies, country equity indexes) [[sources/pdf-19445750a197]].
- Articles are tagged for relevance to each of a predefined set of 73 narratives using proprietary algorithms based on keyword searches and textual conditions [[sources/pdf-19445750a197]].
- The 73 narratives are identified via two channels: starting from the Journal of Economic Literature (JEL) Classification System — the standard method of classifying scholarly economics literature, used in EconLit — and supplementing with interviews with industry analysts [[sources/pdf-19445750a197]].
- Each article is assigned a sentiment score, adjusted for the overall daily tone of the articles in the reservoir from which the article is extracted [[sources/pdf-19445750a197]].
- Intensity measures the proportion of articles relevant to a narrative relative to all news articles collected in a given day in a respective reservoir, proxying for the importance the media gives to the narrative [[sources/pdf-19445750a197]].
- Negative intensity considers only articles expressing a negative tone, providing a view into how negative the media coverage is for a given theme; the main analysis uses negative intensity because it captures directionality (sign) in addition to coverage amount [[sources/pdf-19445750a197]].
- This is similar in spirit to Engle et al. (2020), which constructs a negative-sentiment climate-change news index using the fraction of media articles about "climate change" assigned a negative sentiment score [[sources/pdf-19445750a197]].
- For analysis, a weekly intensity value is constructed for each day as the average of daily intensity values over the most recent seven days (including weekends), and weekly changes are computed as the seven-day difference (e.g., Tuesday through Monday) [[sources/pdf-19445750a197]].
- Returns are generated over the same five-trading-day window (e.g., Monday close to Monday close), and a daily rolling three-month univariate regression of weekly market index returns on weekly intensity changes is run for every narrative over July 2015 to November 2021; time-series average R² is then used to rank narratives by explanatory power [[sources/pdf-19445750a197]].

## Sources

- [[sources/pdf-19445750a197]]

## Related

- [[concepts/narrative-economics]]
- [[concepts/market-crash-narrative]]
- [[concepts/narrative-based-asset-allocation]]
- [[concepts/narrative-beta-portfolio]]
- [[entities/mkt-mediastats]]
