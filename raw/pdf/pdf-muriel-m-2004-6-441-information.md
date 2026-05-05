---
id: pdf-muriel-m-2004-6-441-information
type: pdf
title: 6.441 Information Theory, Lecture 1
url: ''
authors:
- Muriel Médard
ingested_at: '2026-04-29T16:11:21Z'
content_hash: sha256:7ce76c1ebcf1f63a808a1c5b91d010d0c1d1fb6284fe47e9dea21daae0a73ec3
source_path: raw/pdf/pdf-muriel-m-2004-6-441-information.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 8
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/aa7737b3645178c0b746a57f1bdff2cd_MIT6_441S10_lec01.pdf
published_at: '2004'
---
LECTURE 1
Introduction
2 Handouts
Lecture outline
• Goals and mechanics of the class
• notation
• entropy: definitions and properties
• mutual information: definitions and prop­
erties
Reading: Ch. 1, Scts. 2.1-2.5.

Goals
Our goals in this class are to establish an
understanding of the intrinsic properties of
transmission of information and the rela­
tion between coding and the fundamental
limits of information transmission in the
context of communications
Our class is not a comprehensive introduc­
tion to the field of information theory and
will not touch in a significant manner on
such important topics as data compression
and complexity, which belong in a source-
coding class
Notation
– random variable (r.v.) : X
– sample value of a random variable : x
– set of possible sample values x of the
r.v. X : X
– Probability mass function (PMF) of a
discrete r.v. X : P (x)
X
– Probability density function (pdf) of a
continuous r.v. : p (x)
X

Entropy
• Entropy is a measure of the average un­
certainty associated with a random vari­
able
• The entropy of a discrete r.v. X is H(X) =
�
− P (x)log (P (x))
x∈X X 2 X
• entropy is always non-negative
• Joint entropy: the entropy of two dis­
crete r.v.s X, Y with joint PMF P (x, y)
X,Y
is:
� �
�
H(X, Y ) = − P (x, y)log P (x, y)
x∈X ,y∈Y X,Y 2 X,Y
• Conditional entropy: expected value of
entropies calculated according to condi­
tional distributions H(Y |X) = E [H(Y |X =
Z
Z)] for r.v. Z independent of X and
identically distributed with X. Intuitively,
this is the average of the entropy of Y
given X over all possible values of X.

Conditional entropy: chain rule
H(Y |X) = E [H(Y |X = Z)]
Z
� �
= − P (x) P (y|x)log [P (y|x)]
X Y |X 2 Y |X
x∈X y∈Y
�
= − P (x, y) log [P (y|x)]
X,Y 2 Y |X
x∈X ,y∈Y
Compare with joint entropy:
H(X, Y )
�
= − P (x, y) log [P (x, y)]
X,Y 2 X,Y
x∈X ,y∈Y
�
= − P (x, y) log [P (y|x)P (x)]
X,Y 2 Y |X X
x∈X ,y∈Y
�
= − P (x, y) log [P (y|x)]
X,Y 2 Y |X
x∈X ,y∈Y
�
− P (x, y) log [P (x)]
X,Y 2 X
x∈X ,y∈Y
= H(Y |X) + H(X)
This is the Chain Rule for entropy:
�
n
H(X , . . . , X ) = H(X |X . . . X ). Ques­
1 n i=1 i 1 i−1
tion: H(Y |X) = H(X|Y )?

Relative entropy
Relative entropy is a measure of the dis­
tance between two distributions, also known
as the Kullback Leibler distance between
PMFs P (x) and P (y).
X Y
Definition:
� �
�
P (x)
D(P ||P ) = P (x) log X
X Y x∈X X
P (x)
Y
in effect we are considering the log to be a
r.v. of which we take the mean (note that
0 p
we assume 0 log( ) = 0 and p log( ) = ∞
p 0

Mutual information
Mutual Information: let X, Y be r.v.s with
joint PMF P (x, y) and marginal PMFs
X,Y
P (x) and P (y)
X Y
Definition:
I(X; Y )
� �
� P (x, y)
X,Y
= P (x, y) log
X,Y
P (x)P (y)
X Y
x∈X ,y∈Y
� �
= D P (x, y)||P (x)P (y)
X,Y X Y
intuitively: measure of how dependent the
r.v.s are
Useful expression for mutual information:
I(X; Y ) = H(X) + H(Y ) − H(X, Y )
= H(Y ) − H(Y |X )
= H(X) − H(X|Y )
= I(Y ; X)
Question: what is I(X; X)?

Mutual information chain rule
Conditional mutual information: I(X; Y |Z) =
H(X|Z) − H(X|Y, Z)
I(X , . . . , X ; Y )
1 n
= H(X , . . . , X ) − H(X , . . . , X |Y )
1 n 1 n
= H(X , . . . , X ) − H(X , . . . , X |Y )
1 n 1 n
n
�
= H(X |X . . . X )
i 1 i−1
i=1
n
�
− H(X |X . . . X , Y )
i 1 i−1
i=1
n
�
= I(X ; Y |X . . . X )
i 1 i−1
i=1
Look at 3 r.v.s: I(X , X ; Y ) = I(X ; Y ) +
1 2 1
I(X ; Y |X ) where I(X ; Y |X ) is the extra
2 1 2 1
information about Y given by X , but not
2
given by X
1

MIT OpenCourseWare
http://ocw.mit.edu
6.441 Information Theory
Spring 2010
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
