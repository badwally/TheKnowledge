---
id: pdf-41bef100a5b8
type: pdf
title: FallbackPDF__41bef100
url: ''
authors:
- Yuriy Reznik
ingested_at: '2026-04-29T16:14:27Z'
content_hash: sha256:ed6eee8b018d612d9067a4b7fca2bcb09d585d697e7d588872db4a067f556869
source_path: raw/pdf/pdf-41bef100a5b8.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 6
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__41bef100.pdf
published_at: '2025'
---
Formulae for CDN cache miss probability
Yuriy Reznik, Brightcove, Inc
February 5, 2019
Basic concepts
Content popularity model
Let us assume that we have a set of content items, e.g. video clips or segments:
𝑆 = {𝑠 ,𝑥 ≥ 1}
𝑥
Let us also assume that these content items are ordered according to their popularity, and that in such
ordered form, their popularity can be modeled by Zeta distribution [1]:
𝑥−𝛼
𝑝(𝑠 )= ,
𝑥 ζ(α)
where 𝛼 is a shape parameter, and ζ(.) is a Riemann Zeta function [2].
Figure 1. Plots of Zeta distributions with several possible values of parameter 𝛼.
This is a classic distribution, which can be understood as a discrete version of Pareto distribution [3], or
generalization of so called 80/20 rule. It is broadly used in practice, and known to be adequate for
modeling of many natural distributions, including distributions of popularity of video content [4].
CDN cache hit and miss probabilities
Let us now assume that our content is being cached by a CDN edge cache with capacity of C items. If the
caching algorithm is ideal, such cache will store C most popular items.
The probability of hit in this case will be:

𝐶
𝐻
𝐶,𝛼
𝑝 (𝐶,𝛼)= ∑𝑝(𝑠 )= ,
ℎ𝑖𝑡 𝑥 ζ(α)
𝑥=1
where
𝐶
1
𝐻 = ∑
𝐶,𝛼 𝑥𝛼
𝑥=1
is a generalized Harmonic number [5]. The probability of miss, consequently, will be:
𝐻
𝐶,𝛼
𝑝 (𝐶,𝛼)= 1−𝑝 (𝐶,𝛼)= 1− ,
𝑚𝑖𝑠𝑠 ℎ𝑖𝑡 ζ(α)
Naturally, the larger the capacity of CDN cache is, the lower is the miss probability.
Asymptotic cache hit and miss probabilities
It is known that generalized Harmonic numbers can also be expressed as a difference between Riemann
and Hurwitz Zeta functions [6]:
𝐻 = 𝜁(𝛼)− 𝜁(𝛼,𝐶 + 1).
𝐶,𝛼
When C is large, we can use known asymptotic expansion of Hurwitz Zeta function, leading to the
following expression:
𝐶 1 𝛼 1
𝐻 =𝜁(𝛼)+𝐶−𝛼( + − +𝑂( )).
𝐶,𝛼 1−𝛼 2 12𝐶 𝐶2
Consequently, by plugging this expansion in formulae for cache hit/miss probabilities, we obtain:
𝐶1−𝛼 1
𝑝 (𝐶,𝛼) ~1− (1+𝑂( ))
ℎ𝑖𝑡 (𝛼−1)ζ(α) 𝐶
𝐶1−𝛼 1
𝑝 (𝐶,𝛼) ~ (1+𝑂( )).
𝑚𝑖𝑠𝑠 (𝛼−1)ζ(α) 𝐶
Analysis of System with 2 Formats
CDN edge cache population
Next, let us now assume that all same content items are now packaged and stored in 2 different
formats:
𝑆 ={𝑠 ,𝑥 ≥ 1}, and 𝑆 = {𝑠 ,𝑥 ≥ 1},
1 1,𝑥 2 2.𝑥
where index 1 could be associated, e.g. with HLS-packaged data, and index 2 – with DASH data.
Naturally, the packaging format does not influence the popularity of content, but it does limit
percentage of players that will be able to pull it.

Hence, if we assume that 𝜋 = {𝜋 ,𝜋 | 𝜋 +𝜋 = 1} defines distribution of players supporting 1st and
1 2 1 2
2nd format respectively, then we can express final probabilities of items as they will be pulled from CDN
as:
𝑝(𝑠 )= 𝜋 ⋅𝑝(𝑠 ), and 𝑝(𝑠 )= 𝜋 ⋅𝑝(𝑠 )
1,𝑥 1 𝑥 2,𝑥 2 𝑥
Next, let us consider a mixed set:
𝑆 = 𝑆 ∪𝑆 ,
Σ 1 2
and order it according to probabilities of all items it contains.
Let’s for simplicity assume that 𝜋 > 𝜋 (e.g., HLS is used more frequently than DASH).
1 2
Then, we can observe the following structure:
Item Probability Comments
𝑠 𝜋 𝑝(1) First go items of more supported format
1,1 1
... ... ...
1
𝑠 𝜋 𝑝(𝑥) 𝑥 = ⌊(
𝜋1)𝛼⌋
, solution of 𝜋 𝑝(𝑥)= 𝜋 𝑝(1)
1,𝑥 1 𝜋2 1 2
𝑠 𝜋 𝑝(1) Now comes first item in less supported format
2,1 2
𝑠 𝜋 𝑝(𝑥+1) Then follow items in more supported content
1,𝑥+1 1
... ... ...
1
𝑠 𝜋 𝑝(𝑥 ) 𝑥 = ⌊2(
𝜋1)𝛼⌋,
solution of 𝜋 𝑝(𝑥 )= 𝜋 𝑝(2)
1,𝑥2 1 2 2 𝜋2 1 2 2
𝑠 𝜋 𝑝(2) Now comes second item in less supported format
2,2 2
𝑠 𝜋 𝑝(𝑥 +1) Then follow items in more supported content
1,𝑥2+1 1 2
... ... ...
In other words, the sorted list will first include a chain of x items from more supported format, followed
by single item from less supported content, then again x items from more supported format, etc.
The quantity x in such interleaved / sorted order is generally
1
𝜋
1 𝛼
𝑥 = ( )
𝜋
2
followed by rounding.
Now, if we again assume that CDN uses an ideal caching algorithm, then such cache will store exactly
first C items from the table described above.

CDN cache hit and miss probabilities in case of 2 formats
Considering the structure of content in cache described above, we can now express both hit and miss
probabilities. For simplicity, we will now assume that C is relatively large, and that CDN cache
𝐶⋅𝑥 𝐶
consequently includes elements of content packaged in format 1, and elements packaged in
𝑥+1 𝑥+1
second format.
This produces:
𝐶𝑥 𝐶
𝑥+1 𝑥+1 𝐻 𝐶𝑥 𝐻 𝐶
,𝛼 ,𝛼
𝑝 (𝐶,𝛼,𝜋)= ∑𝜋 𝑝(𝑠 )+∑𝜋 𝑝(𝑠 )= 𝜋 𝑥+1 + 𝜋 𝑥+1 .
ℎ𝑖𝑡,2 1 𝑥 2 𝑥 1 ζ(α) 2 ζ(α)
𝑥=1 𝑥=1
By plugging asymptotic expansion for generalized Harmonic numbers, we next obtain:
𝐶𝑥 1−𝛼 𝐶 1−𝛼
(
𝑥+1
) 1 (
𝑥+1
) 1
𝑝 (𝐶,𝛼,𝜋) ~ 𝜋 1− (1+𝑂( )) + 𝜋 1− (1+𝑂( )) ,
ℎ𝑖𝑡,2 1 (𝛼−1)ζ(α) 𝐶 2 (𝛼−1)ζ(α) 𝐶
( ) ( )
and consequently:
𝑥 1−𝛼 1 1−𝛼 𝐶1−𝛼 1
𝑝 (𝐶,𝛼,𝜋) ~ 1−(𝜋 ( ) +𝜋 ( ) ) (1+𝑂( )),
ℎ𝑖𝑡,2 1 𝑥+1 2 𝑥+1 (𝛼−1)ζ(α) 𝐶
1
Finally, by plugging expression for 𝑥 = (
𝜋1)𝛼
, noting that 𝜋 = 1−𝜋 , and with some help of MAPLE’s
2 1
𝜋2
symbolic algebra system, we arrive at:
1 1 𝛼 𝐶1−𝛼 1
𝑝 (𝐶,𝛼,𝜋) ~ 1−(𝜋𝛼 +𝜋𝛼) (1+𝑂( )).
ℎ𝑖𝑡,2 1 2 (𝛼−1)ζ(α) 𝐶
The probability of miss, hence, becomes:
1 1 𝛼 𝐶1−𝛼 1
𝑝 (𝐶,𝛼,𝜋) ~ (𝜋𝛼+𝜋𝛼) (1+𝑂( )).
𝑚𝑖𝑠𝑠,2 1 2 (𝛼−1)ζ(α) 𝐶
Relative impact on cache miss probability
Let us now define a ratio between cache miss probabilities in singe and 2-format cases:
𝑝 (𝐶,𝛼,𝜋)
𝑚𝑖𝑠𝑠,2
𝜉(𝐶,𝛼,𝜋)= .
𝑝 (𝐶,𝛼)
𝑚𝑖𝑠𝑠
1
By plugging the respective asymptotic expressions, and disregarding vanishing 𝑂( ) terms, we arrive at:
𝐶
1 1 𝛼
𝜉(𝛼,𝜋) ~ (𝜋𝛼 +𝜋𝛼) .
1 2

We immediately notice that this formula is no longer dependent on CDN cache size C! This means that
regardless of the CDN cache size, the essential effect of using 2nd format on CDN cache miss probability
boils down to a product by a factor
𝛼
1 1
(𝜋𝛼+𝜋𝛼) .
1 2
We also note, that this quantity is effectively a measure of asymmetry of distribution 𝜋.
1
More specifically, it is a classic ℓ -norm over this distribution with norm parameter 𝑝 = .
𝑝
𝛼
When either of the formats has high support probability (i.e. 𝜋 →1 or 𝜋 →1 ), then
1 2
𝜉(𝛼,𝜋)→1,
implying that cache miss probability in 2-format case will be the same as in case of a single format!
This holds regardless of CDN cache size or the popularity distribution decay parameter 𝛼.
This really means that adding an extra format in cases when there are only few clients that can use it –
does not affect performance of CDN cache. It also means almost no impact on cost of using CDN.
The worst-case situation will be when both formats are about equally well supported. In this case:
𝜋 = 𝜋 = 1/2,
1 2
and consequently:
𝜉(𝛼,1/2) ~ 2𝛼−1.
In other words, the cache miss probability grows exponentially as function of content distribution decay
parameter 𝛼!
We show few plots of ratios of miss probabilities for different parameters 𝛼 in plot below:
Figure 2. Relative increase in cache miss probability in case of using 2 formats. Parameter 𝛼 defines
shape in content popularity distribution (higher 𝛼 means more rapidly decaying content popularity).

For typical for many natural distributions decay parameter 𝛼 =1.16 , the corresponding value of
increase in piss probability becomes:
𝜉(1.16,1/2)≈ 1.117287..
In other words, the impact of 2 formats here is only about 11.7%.
But it indeed could be much larger if content popularity distribution is decaying rapidly.
In other words, the impact of 2 format placement may be drastically different for different publishers of
the content.
For publishers with significant amount and broad spread of popularity of content, the impact of 2
formats may not be that significant. But it will be very significant for publishers who only have one or 2
clips that people actually watch.
References
[1] Zeta distribution https://en.wikipedia.org/wiki/Zeta_distribution
[2] Riemann Zeta function http://mathworld.wolfram.com/RiemannZetaFunction.html
[3] Pareto distribution https://en.wikipedia.org/wiki/Pareto_distribution
[4] Cha, Meeyoung & Kwak, Haewoon & Rodriguez, Pablo & Ahn, Yong-Yeol & Moon, Sue. (2009).
Analyzing the Video Popularity Characteristics of Large-Scale User Generated Content Systems.
IEEE/ACM Trans. Netw.. 17. 1357-1370. 10.1145/1665838.1665839.
[5] Hurwitz Zeta function http://mathworld.wolfram.com/HurwitzZetaFunction.html
[6] Generalized harmonic numbers
http://functions.wolfram.com/GammaBetaErf/HarmonicNumber2/introductions/DifferentiatedGam
mas/ShowAll.html
