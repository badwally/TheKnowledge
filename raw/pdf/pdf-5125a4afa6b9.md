---
id: pdf-5125a4afa6b9
type: pdf
title: FallbackPDF__5125a4af
url: ''
authors: []
ingested_at: '2026-04-29T16:15:04Z'
content_hash: sha256:e61ca8eb18abd4ec6b73916971528819717c69909a3566c24ef81fa6dee52294
source_path: raw/pdf/pdf-5125a4afa6b9.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 47
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__5125a4af.pdf
published_at: '2025'
---
Mathematics for Machine Learning
Garrett Thomas
Department of Electrical Engineering and Computer Sciences
University of California, Berkeley
January 11, 2018
1 About
Machine learning uses tools from a variety of mathematical fields. This document is an attempt to
provide a summary of the mathematical background needed for an introductory class in machine
learning, which at UC Berkeley is known as CS 189/289A.
Ourassumptionisthatthereaderisalreadyfamiliarwiththebasicconceptsofmultivariablecalculus
and linear algebra (at the level of UCB Math 53/54). We emphasize that this document is not a
replacementfortheprerequisiteclasses. Mostsubjectspresentedherearecoveredratherminimally;
weintendtogiveanoverviewandpointtheinterestedreadertomorecomprehensivetreatmentsfor
further details.
Note that this document concerns math background for machine learning, not machine learning
itself. We will not discuss specific machine learning models or algorithms except possibly in passing
to highlight the relevance of a mathematical concept.
Earlier versions of this document did not include proofs. We have begun adding in proofs where
they are reasonably short and aid in understanding. These proofs are not necessary background for
CS 189 but can be used to deepen the reader’s understanding.
You are free to distribute this document as you wish. The latest version can be found at http://
gwthomas.github.io/docs/math4ml.pdf. Pleasereportanymistakestogwthomas@berkeley.edu.
1

Contents
1 About 1
2 Notation 5
3 Linear Algebra 6
3.1 Vector spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.1.1 Euclidean space. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.1.2 Subspaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2 Linear maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2.1 The matrix of a linear map . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2.2 Nullspace, range . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.3 Metric spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4 Normed spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.5 Inner product spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.5.1 Pythagorean Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.5.2 Cauchy-Schwarz inequality . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.5.3 Orthogonal complements and projections . . . . . . . . . . . . . . . . . . . . 12
3.6 Eigenthings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.7 Trace. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.8 Determinant. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.9 Orthogonal matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.10 Symmetric matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.10.1 Rayleigh quotients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.11 Positive (semi-)definite matrices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.11.1 The geometry of positive definite quadratic forms . . . . . . . . . . . . . . . . 19
3.12 Singular value decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.13 Fundamental Theorem of Linear Algebra. . . . . . . . . . . . . . . . . . . . . . . . . 21
3.14 Operator and matrix norms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.15 Low-rank approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.16 Pseudoinverses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.17 Some useful matrix identities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.17.1 Matrix-vector product as linear combination of matrix columns . . . . . . . . 26
3.17.2 Sum of outer products as matrix-matrix product . . . . . . . . . . . . . . . . 26
3.17.3 Quadratic forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4 Calculus and Optimization 27
2

4.1 Extrema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2 Gradients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3 The Jacobian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.4 The Hessian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.5 Matrix calculus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.5.1 The chain rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.6 Taylor’s theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.7 Conditions for local minima . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.8 Convexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.8.1 Convex sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.8.2 Basics of convex functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.8.3 Consequences of convexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.8.4 Showing that a function is convex . . . . . . . . . . . . . . . . . . . . . . . . 33
4.8.5 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
5 Probability 37
5.1 Basics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.1.1 Conditional probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
5.1.2 Chain rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
5.1.3 Bayes’ rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
5.2 Random variables. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2.1 The cumulative distribution function . . . . . . . . . . . . . . . . . . . . . . . 39
5.2.2 Discrete random variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.2.3 Continuous random variables . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.2.4 Other kinds of random variables . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.3 Joint distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.3.1 Independence of random variables . . . . . . . . . . . . . . . . . . . . . . . . 41
5.3.2 Marginal distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.4 Great Expectations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.4.1 Properties of expected value . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5 Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.1 Properties of variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.2 Standard deviation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.6 Covariance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.6.1 Correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.7 Random vectors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3

5.8 Estimation of Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.8.1 Maximum likelihood estimation . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.8.2 Maximum a posteriori estimation . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.9 The Gaussian distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.9.1 The geometry of multivariate Gaussians . . . . . . . . . . . . . . . . . . . . . 45
References 47
4

2 Notation
Notation Meaning
R set of real numbers
R n set (vector space) of n-tuples of real numbers, endowed with the usual inner product
R m ⇥ n set (vector space) of m-by-n matrices
  Kronecker delta, i.e.   =1 if i=j, 0 otherwise
ij ij
f(x) gradient of the function f at x
r
2f(x) Hessian of the function f at x
r
A transpose of the matrix A
>
⌦ sample space
P(A) probability of event A
p(X) distribution of random variable X
p(x) probability density/mass function evaluated at x
Ac complement of event A
A ˙ B union of A and B, with the extra requirement that A B =?
[ \
E[X] expected value of random variable X
Var(X) variance of random variable X
Cov(X,Y) covariance of random variables X and Y
Other notes:
Vectors and matrices are in bold (e.g. x,A). This is true for vectors in R n as well as for
•
vectors in general vector spaces. We generally use Greek letters for scalars and capital Roman
letters for matrices and random variables.
To stay focused at an appropriate level of abstraction, we restrict ourselves to real values. In
•
many places in this document, it is entirely possible to generalize to the complex case, but we
will simply state the version that applies to the reals.
We assume that vectors are column vectors, i.e. that a vector in R n can be interpreted as an
•
n-by-1 matrix. As such, taking the transpose of a vector is well-defined (and produces a row
vector, which is a 1-by-n matrix).
5

3 Linear Algebra
In this section we present important classes of spaces in which our data will live and our operations
will take place: vector spaces, metric spaces, normed spaces, and inner product spaces. Generally
speaking,thesearedefinedinsuchawayastocaptureoneormoreimportantpropertiesofEuclidean
space but in a more general way.
3.1 Vector spaces
Vector spacesarethebasicsettinginwhichlinearalgebrahappens. AvectorspaceV isaset(the
elements of which are called vectors) on which two operations are defined: vectors can be added
together, and vectors can be multiplied by real numbers1 called scalars. V must satisfy
(i) There exists an additive identity (written 0) in V such that x+0=x for all x V
2
(ii) For each x V, there exists an additive inverse (written x) such that x+( x)=0
2    
(iii) There exists a multiplicative identity (written 1) in R such that 1x=x for all x V
2
(iv) Commutativity: x+y=y+x for all x,y V
2
(v) Associativity: (x+y)+z=x+(y+z) and ↵( x)=(↵ )x for all x,y,z V and ↵,  R
2 2
(vi) Distributivity: ↵(x+y)=↵x+↵y and (↵+ )x=↵x+ x for all x,y V and ↵,  R
2 2
A set of vectors v ,...,v V is said to be linearly independent if
1 n
2
↵ v + +↵ v =0 implies ↵ = =↵ =0.
1 1 n n 1 n
··· ···
The span of v ,...,v V is the set of all vectors that can be expressed of a linear combination
1 n
2
of them:
span v ,...,v = v V : ↵ ,...,↵ such that ↵ v + +↵ v =v
1 n 1 n 1 1 n n
{ } { 2 9 ··· }
If a set of vectors is linearly independent and its span is the whole of V, those vectors are said to
be a basis for V. In fact, every linearly independent set of vectors forms a basis for its span.
If a vector space is spanned by a finite number of vectors, it is said to be finite-dimensional.
Otherwise it is infinite-dimensional. The number of vectors in a basis for a finite-dimensional
vector space V is called the dimension of V and denoted dimV.
3.1.1 Euclidean space
ThequintessentialvectorspaceisEuclidean space,whichwedenoteR n. Thevectorsinthisspace
consist of n-tuples of real numbers:
x=(x ,x ,...,x )
1 2 n
For our purposes, it will be useful to think of them as n 1 matrices, or column vectors:
⇥
x
1
x
2 23
x= .
.
.
6 7
6x 7
6 n7
6 7
4 5
1 More generally, vector spaces can be defined over any field F. We take F = R in this document to avoid an
unnecessarydiversionintoabstractalgebra.
6

Addition and scalar multiplication are defined component-wise on vectors in R n:
x +y ↵x
1 1 1
. .
x+y=2 . . 3,↵ x=2 . . 3
x +y ↵x
6 n n7 6 n7
6 7 6 7
4 5 4 5
Euclidean space is used to mathematically represent physical space, with notions such as distance,
length, and angles. Although it becomes hard to visualize for n > 3, these concepts generalize
mathematically in obvious ways. Even when you’re working in more general settings than R n, it is
oftenusefultovisualizevectoradditionandscalarmultiplicationintermsof2Dvectorsintheplane
or 3D vectors in space.
3.1.2 Subspaces
Vector spaces can contain other vector spaces. If V is a vector space, then S V is said to be a
✓
subspace of V if
(i) 0 S
2
(ii) S is closed under addition: x,y S implies x+y S
2 2
(iii) S is closed under scalar multiplication: x S,↵ R implies ↵x S
2 2 2
Note that V is always a subspace of V, as is the trivial vector space which contains only 0.
As a concrete example, a line passing through the origin is a subspace of Euclidean space.
If U and W are subspaces of V, then their sum is defined as
U +W = u+w u U,w W
{ | 2 2 }
It is straightforward to verify that this set is also a subspace of V. If U W = 0 , the sum is said
\ { }
to be a direct sum and written U W. Every vector in U W can be written uniquely as u+w
   
for some u U and w W. (This is both a necessary and su cient condition for a direct sum.)
2 2
The dimensions of sums of subspaces obey a friendly relationship (see [4] for proof):
dim(U +W)=dimU +dimW dim(U W)
  \
It follows that
dim(U W)=dimU +dimW
 
since dim(U W)=dim( 0 )=0 if the sum is direct.
\ { }
3.2 Linear maps
A linear map is a function T :V W, where V and W are vector spaces, that satisfies
!
(i) T(x+y)=Tx+Ty for all x,y V
2
(ii) T(↵x)=↵Tx for all x V,↵ R
2 2
7

The standard notational convention for linear maps (which we follow here) is to drop unnecessary
parentheses, writing Tx rather than T(x) if there is no risk of ambiguity, and denote composition
of linear maps by ST rather than the usual S T.
 
A linear map from V to itself is called a linear operator.
Observe thatthe definitionof alinearmap issuited toreflectthe structureof vector spaces, since it
preservesvectorspaces’twomainoperations,additionandscalarmultiplication. Inalgebraicterms,
alinearmapiscalledahomomorphismofvectorspaces. Aninvertiblehomomorphism(wherethe
inverse is also a homomorphism) is called an isomorphism. If there exists an isomorphism from V
to W, then V and W are said to be isomorphic, and we write V = W. Isomorphic vector spaces
⇠
are essentially “the same” in terms of their algebraic structure. It is an interesting fact that finite-
dimensional vector spaces2 of the same dimension are always isomorphic; if V,W are real vector
spaces with dimV =dimW =n, then we have the natural isomorphism
':V W
!
↵ v + +↵ v ↵ w + +↵ w
1 1 n n 1 1 n n
··· 7! ···
wherev ,...,v andw ,...,w areanybasesforV andW. Thismapiswell-definedbecauseevery
1 n 1 n
vector in V can be expressed uniquely as a linear combination of v ,...,v . It is straightforward
1 n
to verify that ' is an isomorphism, so in fact V =W. In particular, every real n-dimensional vector
⇠
space is isomorphic to R n.
3.2.1 The matrix of a linear map
Vector spaces are fairly abstract. To represent and manipulate vectors and linear maps on a com-
puter, we use rectangular arrays of numbers known as matrices.
SupposeV andW arefinite-dimensionalvectorspaceswithbasesv ,...,v andw ,...,w ,respec-
1 n 1 m
tively, and T :V W is a linear map. Then the matrix of T, with entries A where i=1,...,m,
ij
!
j =1,...,n, is defined by
Tv =A w + +A w
j 1j 1 mj m
···
That is, the jth column of A consists of the coordinates of Tv in the chosen basis for W.
j
Conversely, every matrix A R m ⇥ n induces a linear map T :R n R m given by
2 !
Tx=Ax
and the matrix of this map with respect to the standard bases of R n and R m is of course simply A.
If A R m ⇥ n, its transpose A > R n ⇥ m is given by (A > ) ij = A ji for each (i,j). In other words,
2 2
the columns of A become the rows of A , and the rows of A become the columns of A .
> >
The transpose has several nice algebraic properties that can be easily verified from the definition:
(i) (A ) =A
>>
(ii) (A+B) =A +B
> > >
(iii) (↵A) =↵A
> >
(iv) (AB) =B A
> > >
2 overthesamefield
8

3.2.2 Nullspace, range
Some of the most important subspaces are those induced by linear maps. If T :V W is a linear
!
map, we define the nullspace3 of T as
null(T)= v V Tv=0
{ 2 | }
and the range of T as
range(T)= w W v V such that Tv=w
{ 2 |9 2 }
It is a good exercise to verify that the nullspace and range of a linear map are always subspaces of
its domain and codomain, respectively.
The columnspace of a matrix A R m ⇥ n is the span of its columns (considered as vectors in R m),
2
and similarly the rowspace of A is the span of its rows (considered as vectors in R n). It is not
hard to see that the columnspace of A is exactly the range of the linear map from R n to R m which
is induced by A, so we denote it by range(A) in a slight abuse of notation. Similarly, the rowspace
is denoted range(A ).
>
It is a remarkable fact that the dimension of the columnspace of A is the same as the dimension of
the rowspace of A. This quantity is called the rank of A, and defined as
rank(A)=dimrange(A)
3.3 Metric spaces
Metrics generalize the notion of distance from Euclidean space (although metric spaces need not be
vector spaces).
A metric on a set S is a function d:S S R that satisfies
⇥ !
(i) d(x,y) 0, with equality if and only if x=y
 
(ii) d(x,y)=d(y,x)
(iii) d(x,z) d(x,y)+d(y,z) (the so-called triangle inequality)

for all x,y,z S.
2
A key motivation for metrics is that they allow limits to be defined for mathematical objects other
than real numbers. We say that a sequence x S converges to the limit x if for any ✏> 0, there
n
{ }✓
existsN Nsuchthatd(x
n
,x)<✏ foralln N. Notethatthedefinitionforlimitsofsequencesof
2  
real numbers, which you have likely seen in a calculus class, is a special case of this definition when
using the metric d(x,y)= x y .
|   |
3.4 Normed spaces
Norms generalize the notion of length from Euclidean space.
A norm on a real vector space V is a function :V R that satisfies
k·k !
3 Itissometimescalledthekernelbyalgebraists,butweeschewthisterminologybecausetheword“kernel”has
anothermeaninginmachinelearning.
9

(i) x 0, with equality if and only if x=0
k k 
(ii) ↵x = ↵ x
k k | |k k
(iii) x+y x + y (the triangle inequality again)
k kk k k k
for all x,y V and all ↵ R. A vector space endowed with a norm is called a normed vector
2 2
space, or simply a normed space.
Note that any norm on V induces a distance metric on V:
d(x,y)= x y
k   k
Onecanverifythattheaxiomsformetricsaresatisfiedunderthisdefinitionandfollowdirectlyfrom
the axioms for norms. Therefore any normed space is also a metric space.4
We will typically only be concerned with a few specific norms on R n:
n
x = x
1 i
k k | |
i=1
X
n
x = x2
k k 2 v i
ui=1
uX
t 1
n p
x = x p (p 1)
p i
k k 0 | | 1  
i=1
X
x =@max x A
i
k k1 1 i n| |

Note that the 1- and 2-norms are special cases of the p-norm, and the -norm is the limit of the
1
p-norm as p tends to infinity. We require p 1 for the general definition of the p-norm because the
 
triangle inequality fails to hold if p<1. (Try to find a counterexample!)
Here’s a fun fact: for any given finite-dimensional vector space V, all norms on V are equivalent in
the sense that for two norms , , there exist constants ↵,  >0 such that
A B
k·k k·k
↵ x x   x
A B A
k k k k  k k
for all x V. Therefore convergence in one norm implies convergence in any other norm. This rule
2
may not apply in infinite-dimensional vector spaces such as function spaces, though.
3.5 Inner product spaces
An inner product on a real vector space V is a function , :V V R satisfying
h· ·i ⇥ !
(i) x,x 0, with equality if and only if x=0
h i 
(ii) Linearity in the first slot: x+y,z = x,z + y,z and ↵x,y =↵ x,y
h i h i h i h i h i
(iii) x,y = y,x
h i h i
4Ifanormedspaceiscompletewithrespecttothedistancemetricinducedbyitsnorm,wesaythatitisaBanach
space.
10

for all x,y,z V and all ↵ R. A vector space endowed with an inner product is called an inner
2 2
product space.
Note that any inner product on V induces a norm on V:
x = x,x
k k h i
p
One can verify that the axioms for norms are satisfied under this definition and follow (almost)
directly from the axioms for inner products. Therefore any inner product space is also a normed
space (and hence also a metric space).5
Two vectors x and y are said to be orthogonal if x,y = 0; we write x y for shorthand.
h i ?
Orthogonality generalizes the notion of perpendicularity from Euclidean space. If two orthogonal
vectors x and y additionally have unit length (i.e. x = y = 1), then they are described as
k k k k
orthonormal.
The standard inner product on R n is given by
n
x,y = x y =x y
i i >
h i
i=1
X
The matrix notation on the righthand side arises because this inner product is a special case of
matrix multiplication where we regard the resulting 1 1 matrix as a scalar. The inner product on
⇥
R n is also often written x y (hence the alternate name dot product). The reader can verify that
·
the two-norm 2 on R n is induced by this inner product.
k·k
3.5.1 Pythagorean Theorem
The well-known Pythagorean theorem generalizes naturally to arbitrary inner product spaces.
Theorem 1. If x y, then
?
x+y 2 = x 2+ y 2
k k k k k k
Proof. Suppose x y, i.e. x,y =0. Then
? h i
x+y 2 = x+y,x+y = x,x + y,x + x,y + y,y = x 2+ y 2
k k h i h i h i h i h i k k k k
as claimed.
3.5.2 Cauchy-Schwarz inequality
This inequality is sometimes useful in proving bounds:
x,y x y
|h i|k k k k
for all x,y V. Equality holds exactly when x and y are scalar multiples of each other (or
2
equivalently, when they are linearly dependent).
5 If an inner product space is complete with respect to the distance metric induced by its inner product, we say
thatitisaHilbert space.
11

3.5.3 Orthogonal complements and projections
If S V where V is an inner product space, then the orthogonal complement of S, denoted S ,
?
✓
is the set of all vectors in V that are orthogonal to every element of S:
S = v V v s for all s S
?
{ 2 | ? 2 }
It is easy to verify that S is a subspace of V for any S V. Note that there is no requirement
?
✓
that S itself be a subspace of V. However, if S is a (finite-dimensional) subspace of V, we have the
following important decomposition.
Proposition 1. Let V be an inner product space and S be a finite-dimensional subspace of V. Then
every v V can be written uniquely in the form
2
v=v +v
S
?
where v S and v S .
S ?
2 ? 2
Proof. Let u ,...,u be an orthonormal basis for S, and suppose v V. Define
1 m
2
v = v,u u + + v,u u
S 1 1 m m
h i ··· h i
and
v =v v
S
?  
It is clear that v S since it is in the span of the chosen basis. We also have, for all i=1,...,m,
S
2
v ,u = v ( v,u u + + v,u u ),u
i 1 1 m m i
h ? i   h i ··· h i
= v,u v,u u ,u v,u u ,u
⌦ i 1 1 i m↵ m i
h i h ih i ··· h ih i
= v,u v,u
i i
h i h i
=0
which implies v S .
?
? 2
It remains to show that this decomposition is unique, i.e. doesn’t depend on the choice of basis. To
this end, let u ,...,u be another orthonormal basis for S, and define v and v analogously. We
01 0m S0 0
claim that v =v and v =v . ?
S0 S 0
? ?
By definition,
v +v =v=v +v
S S0 0
? ?
so
v v =v v
S
 
S0
?
0
  ?
2
S
2
S?
From the orthogonality of these subspac|es,{wze}have| {z }
0= v v ,v v = v v ,v v = v v 2
h
S
 
S0
?
0
  ?i h
S
 
S0 S
 
S0
i k
S
 
S0
k
It follows that v v =0, i.e. v =v . Then v =v v =v v =v as well.
S
 
S0 S S0
?
0
 
S0
 
S
?
The existence and uniqueness of the decomposition above mean that
V =S S
?
 
whenever S is a subspace.
12

Since the mapping from v to v in the decomposition above always exists and is unique, we have a
S
well-defined function
P :V S
S
!
v v
S
7!
which is called the orthogonal projection onto S. We give the most important properties of this
function below.
Proposition 2. Let S be a finite-dimensional subspace of V. Then
(i) For any v V and orthonormal basis u ,...,u of S,
1 m
2
P v= v,u u + + v,u u
S 1 1 m m
h i ··· h i
(ii) For any v V, v P v S.
S
2   ?
(iii) P is a linear map.
S
(iv) P is the identity when restricted to S (i.e. P s=s for all s S).
S S
2
(v) range(P )=S and null(P )=S .
S S ?
(vi) P2 =P .
S S
(vii) For any v V, P v v .
S
2 k kk k
(viii) For any v V and s S,
2 2
v P v v s
S
k   kk   k
with equality if and only if s=P v. That is,
S
P v=argmin v s
S
k   k
s S
2
Proof. The first two statements are immediate from the definition of P and the work done in the
S
proof of the previous proposition.
In this proof, we abbreviate P =P for brevity.
S
(iii) Suppose x,y V and ↵ R. Write x = x
S
+x and y = y
S
+y , where x
S
,y
S
S and
2 2 ? ? 2
x ,y S . Then
?
? ? 2
x+y=x +y +x +y
S S
? ?
2
S
2
S?
so P(x+y)=x S +y S =Px+Py, and | {z } | {z }
↵x=↵x +↵x
S
?
2
S
2
S?
|{z} |{z}
so P(↵x)=↵x =↵Px. Thus P is linear.
S
(iv) If s S, then we can write s=s+0 where s S and 0 S , so Ps=s.
?
2 2 2
13

(v) range(P) S: By definition.
✓
range(P) S: Using the previous result, any s S satisfies s = Pv for some v V (specifi-
◆ 2 2
cally, v=s).
null(P) S : Suppose v null(P). Write v = v +v where v S and v S . Then
? S S ?
✓ 2 ? 2 ? 2
0=Pv=v , so v=v S .
S ?
? 2
null(P) S : If v S , then v=0+v where 0 S and v S , so Pv=0.
? ? ?
◆ 2 2 2
(vi) For any v V,
2
P2v=P(Pv)=Pv
since Pv S and P is the identity on S. Hence P2 =P.
2
(vii) Suppose v V. Then by the Pythagorean theorem,
2
v 2 = Pv+(v Pv) 2 = Pv 2+ v Pv 2 Pv 2
k k k   k k k k   k  k k
The result follows by taking square roots.
(viii) Suppose v V and s S. Then by the Pythagorean theorem,-
2 2
v s 2 = (v Pv)+(Pv s) 2 = v Pv 2+ Pv s 2 v Pv 2
k   k k     k k   k k   k  k   k
Weobtain v s v Pv bytakingsquareroots. Equalityholdsi↵ Pv s 2 =0,which
k   k k   k k   k
is true i↵ Pv=s.
Any linear map P that satisfies P2 = P is called a projection, so we have shown that P is a
S
projection (hence the name).
Thelastpartofthepreviousresultshowsthatorthogonalprojectionsolvestheoptimizationproblem
of finding the closest point in S to a given v V. This makes intuitive sense from a pictorial
2
representation of the orthogonal projection:
LetusnowconsiderthespecificcasewhereS isasubspaceofR n withorthonormalbasisu
1
,...,u
m
.
Then
m m m m
P x= x,u u = x u u = u u x= u u x
S
h
i
i
i > i i i >i
0
i >i1
i=1 i=1 i=1 i=1
X X X X
@ A
14

so the operator P can be expressed as a matrix
S
m
P = u u =UU
S i >i >
i=1
X
where U has u ,...,u as its columns. Here we have used the sum-of-outer-products identity.
1 m
3.6 Eigenthings
For a square matrix A R n ⇥ n, there may be vectors which, when A is applied to them, are simply
2
scaledbysomeconstant. Wesaythatanonzerovectorx R nisaneigenvectorofAcorresponding
2
to eigenvalue   if
Ax= x
The zero vector is excluded from this definition because A0=0= 0 for every  .
We now give some useful results about how eigenvalues change after various manipulations.
Proposition 3. Let x be an eigenvector of A with corresponding eigenvalue  . Then
(i) For any   R, x is an eigenvector of A+ I with eigenvalue  + .
2
(ii) If A is invertible, then x is an eigenvector of A 1 with eigenvalue   1.
   
(iii) Akx= kx for any k Z (where A0 =I by definition).
2
Proof. (i) follows readily:
(A+ I)x=Ax+ Ix= x+ x=( + )x
(ii) Suppose A is invertible. Then
x=A 1Ax=A 1( x)= A 1x
     
Dividing by  , which is valid because the invertibility of A implies  =0, gives   1x=A 1x.
   
6
(iii) The case k 0 follows immediately by induction on k. Then the general case k Z follows by
  2
combining the k 0 case with (ii).
 
3.7 Trace
The trace of a square matrix is the sum of its diagonal entries:
n
tr(A)= A
ii
i=1
X
The trace has several nice algebraic properties:
(i) tr(A+B)=tr(A)+tr(B)
(ii) tr(↵A)=↵tr(A)
(iii) tr(A )=tr(A)
>
15

(iv) tr(ABCD)=tr(BCDA)=tr(CDAB)=tr(DABC)
The first three properties follow readily from the definition. The last is known as invariance
under cyclic permutations. Note that the matrices cannot be reordered arbitrarily, for example
tr(ABCD) = tr(BACD) in general. Also, there is nothing special about the product of four
6
matrices – analogous rules hold for more or fewer matrices.
Interestingly, the trace of a matrix is equal to the sum of its eigenvalues (repeated according to
multiplicity):
tr(A)=   (A)
i
i
X
3.8 Determinant
The determinant of a square matrix can be defined in several di↵erent confusing ways, none of
whichareparticularlyimportantforourpurposes; golookatanintroductorylinearalgebratext(or
Wikipedia) if you need a definition. But it’s good to know the properties:
(i) det(I)=1
(ii) det A =det(A)
>
(iii) det (AB )=det(A)det(B)
(iv) det A
 
1 =det(A)  1
(v) det( ↵A) =↵ndet(A)
Interestingly, the determinant of a matrix is equal to the product of its eigenvalues (repeated ac-
cording to multiplicity):
det(A)=   (A)
i
i
Y
3.9 Orthogonal matrices
AmatrixQ R n ⇥ nissaidtobeorthogonalifitscolumnsarepairwiseorthonormal. Thisdefinition
2
implies that
Q Q=QQ =I
> >
or equivalently, Q = Q 1. A nice thing about orthogonal matrices is that they preserve inner
>  
products:
(Qx) (Qy)=x Q Qy=x Iy=x y
> > > > >
A direct result of this fact is that they also preserve 2-norms:
Qx = (Qx) (Qx)=px x= x
k k 2 > > k k 2
q
Therefore multiplication by an orthogonal matrix can be considered as a transformation that pre-
serves length, but may rotate or reflect the vector about the origin.
16

3.10 Symmetric matrices
A matrix A R n ⇥ n is said to be symmetric if it is equal to its own transpose (A=A > ), meaning
2
that A = A for all (i,j). This definition seems harmless enough but turns out to have some
ij ji
strong implications. We summarize the most important of these as
Theorem 2. (Spectral Theorem) If A R n ⇥ n is symmetric, then there exists an orthonormal basis
2
for R n consisting of eigenvectors of A.
The practical application of this theorem is a particular factorization of symmetric matrices, re-
ferred to as the eigendecomposition or spectral decomposition. Denote the orthonormal basis
of eigenvectors q ,...,q and their eigenvalues   ,...,  . Let Q be an orthogonal matrix with
1 n 1 n
q ,...,q as its columns, and ⇤=diag(  ,...,  ). Since by definition Aq =  q for every i, the
1 n 1 n i i i
following relationship holds:
AQ=Q⇤
Right-multiplying by Q , we arrive at the decomposition
>
A=Q⇤Q
>
3.10.1 Rayleigh quotients
Let A R n ⇥ n be a symmetric matrix. The expression x > Ax is called a quadratic form.
2
There turns out to be an interesting connection between the quadratic form of a symmetric matrix
and its eigenvalues. This connection is provided by the Rayleigh quotient
x Ax
>
R (x)=
A
x x
>
The Rayleigh quotient has a couple of important properties which the reader can (and should!)
easily verify from the definition:
(i) Scale invariance: for any vector x=0 and any scalar ↵=0, R (x)=R (↵x).
A A
6 6
(ii) If x is an eigenvector of A with eigenvalue  , then R (x)= .
A
We can further show that the Rayleigh quotient is bounded by the largest and smallest eigenvalues
of A. But first we will show a useful special case of the final result.
Proposition 4. For any x such that x =1,
2
k k
  (A) x Ax   (A)
min > max
 
with equality if and only if x is a corresponding eigenvector.
Proof. We show only the max case because the argument for the min case is entirely analogous.
SinceAissymmetric,wecandecomposeitasA=Q⇤Q . Thenusethechangeofvariabley=Q x,
> >
notingthattherelationshipbetweenxandy isone-to-oneandthat y =1sinceQisorthogonal.
2
k k
Hence
n
max x Ax= max y ⇤y= max   y2
> > i i
k
x k2=1
k
y k2=1 y
1
2+
···
+y
n
2=1
i=1
X
Written this way, it is clear that y maximizes this expression exactly if and only if it satisfies
y2 = 1 where I = i :   = max   =   (A) and y = 0 for j I. That is,
i I i { i j=1,...,n j max } j 62
2
P
17

I contains the index or indices of the largest eigenvalue. In this case, the maximal value of the
expression is
n
  y2 =   y2 =  (A) y2 =  (A)
i i i i max i max
i=1 i I i I
X X2 X2
Then writing q ,...,q for the columns of Q, we have
1 n
n
x=QQ x=Qy= y q = y q
> i i i i
i=1 i I
X X2
where we have used the matrix-vector product identity.
Recall that q 1 ,...,q n are eigenvectors of A and form an orthonormal basis for R n. Therefore by
construction, the set q :i I forms an orthonormal basis for the eigenspace of   (A). Hence
i max
{ 2 }
x, which is a linear combination of these, lies in that eigenspace and thus is an eigenvector of A
corresponding to   (A).
max
Wehaveshownthatmax x Ax=  (A),fromwhichwehavethegeneralinequalityx Ax
k
x k2=1 > max >

  (A) for all unit-length x.
max
By the scale invariance of the Rayleigh quotient, we immediately have as a corollary (since x Ax=
>
R (x) for unit x)
A
Theorem 3. (Min-max theorem) For all x=0,
6
  (A) R (x)   (A)
min A max
 
with equality if and only if x is a corresponding eigenvector.
This is sometimes referred to as a variational characterization of eigenvalues because it ex-
presses the smallest/largest eigenvalue of A in terms of a minimization/maximization problem:
  (A)=min/maxR (x)
min/max A
x=0 x=0
6 6
3.11 Positive (semi-)definite matrices
A symmetric matrix A is positive semi-definite if for all x R n, x > Ax 0. Sometimes people
2  
write A 0 to indicate that A is positive semi-definite.
⌫
AsymmetricmatrixAispositive definiteifforallnonzerox R n, x > Ax>0. Sometimespeople
2
write A 0 to indicate that A is positive definite. Note that positive definiteness is a strictly
 
stronger property than positive semi-definiteness, in the sense that every positive definite matrix is
positive semi-definite but not vice-versa.
These properties are related to eigenvalues in the following way.
Proposition 5. A symmetric matrix is positive semi-definite if and only if all of its eigenvalues are
nonnegative, and positive definite if and only if all of its eigenvalues are positive.
Proof. SupposeAispositivesemi-definite,andletxbeaneigenvectorofAwitheigenvalue . Then
0 x Ax=x ( x)= x x=  x 2
 > > > k k2
18

Since x=0 (by the assumption that it is an eigenvector), we have x 2 >0, so we can divide both
6 k k2
sides by x 2 to arrive at   0. If A is positive definite, the inequality above holds strictly, so
k k2  
 > 0. This proves one direction.
Tosimplifytheproofoftheotherdirection,wewillusethemachineryofRayleighquotients. Suppose
that A is symmetric and all its eigenvalues are nonnegative. Then for all x=0,
6
0   (A) R (x)
min A
 
Since x Ax matches R (x) in sign, we conclude that A is positive semi-definite. If the eigenvalues
> A
of A are all strictly positive, then 0<  (A), whence it follows that A is positive definite.
min
As an example of how these matrices arise, consider
Proposition 6. Suppose A R m ⇥ n. Then A > A is positive semi-definite. If null(A) = 0 , then
2 { }
A A is positive definite.
>
Proof. For any x R n,
2
x (A A)x=(Ax) (Ax)= Ax 2 0
> > > k k2  
so A A is positive semi-definite. If null(A) = 0 , then Ax = 0 whenever x = 0, so Ax 2 > 0,
> { } 6 6 k k2
and thus A A is positive definite.
>
Positive definite matrices are invertible (since their eigenvalues are nonzero), whereas positive semi-
definite matrices might not be. However, if you already have a positive semi-definite matrix, it is
possible to perturb its diagonal slightly to produce a positive definite matrix.
Proposition 7. If A is positive semi-definite and ✏> 0, then A+✏I is positive definite.
Proof. Assuming A is positive semi-definite and ✏> 0, we have for any x=0 that
6
x (A+✏I)x=x Ax+✏x Ix=x Ax+✏ x 2 >0
> > > > k k2
  0 >0
as claimed. | {z } | {z }
An obvious but frequently useful consequence of the two propositions we have just shown is that
A A+✏I is positive definite (and in particular, invertible) for any matrix A and any ✏> 0.
>
3.11.1 The geometry of positive definite quadratic forms
A useful way to understand quadratic forms is by the geometry of their level sets. A level set or
isocontourofafunctionisthesetofallinputssuchthatthefunctionappliedtothoseinputsyields
a given output. Mathematically, the c-isocontour of f is x domf :f(x)=c .
{ 2 }
Let us consider the special case f(x) = x Ax where A is a positive definite matrix. Since A is
>
positive definite, it has a unique matrix square root A1 2 = Q⇤1 2Q > , where Q⇤Q > is the eigende-
composition of A and ⇤1 2 = diag(p  1 ,...p  n ). It is easy to see that this matrix A1 2 is positive
definite (consider its eigenvalues) and satisfies A1 2A1 2 = A. Fixing a value c 0, the c-isocontour
 
of f is the set of x R n such that
2
c=x
>
Ax=x
>
A 1 2A 1 2x=
k
A 1 2x
k
2
2
19

where we have used the symmetry of A1 2. Making the change of variable z = A1 2x, we have the
condition z =pc. Thatis,thevalueszlieonasphereofradiuspc. Thesecanbeparameterized
2
k k
as z=pczˆ where zˆ has zˆ 2 =1. Then since A   1 2 =Q⇤   1 2Q > , we have
k k
x=A
 
1 2z=Q⇤
 
1 2Q
>
pczˆ=pcQ⇤
 
1 2z˜
where z˜ = Q zˆ also satisfies z˜ = 1 since Q is orthogonal. Using this parameterization, we see
> 2
k k
that the solution set x R n :f(x)=c is the image of the unit sphere z˜ R n : z˜ 2 =1 under
{ 2 } { 2 k k }
the invertible linear map x=pcQ⇤
 
1 2z˜.
What we have gained with all these manipulations is a clear algebraic understanding of the c-
isocontour of f in terms of a sequence of linear transformations applied to a well-understood set.
1
We begin with the unit sphere, then scale every axis i by   2, resulting in an axis-aligned ellipsoid.
i
Observe that the axis lengths of the ellipsoid are proportional to the inverse square roots of the
eigenvalues of A. Hence larger eigenvalues correspond to shorter axis lengths, and vice-versa.
Then this axis-aligned ellipsoid undergoes a rigid transformation (i.e. one that preserves length and
angles, such as a rotation/reflection) given by Q. The result of this transformation is that the axes
of the ellipse are no longer along the coordinate axes in general, but rather along the directions
given by the corresponding eigenvectors. To see this, consider the unit vector e i R n that has
2
[e ] =  . In the pre-transformed space, this vector points along the axis with length proportional
i j ij
1
to   2. But after applying the rigid transformation Q, the resulting vector points in the direction
i
of the corresponding eigenvector q , since
i
n
Qe = [e ] q =q
i i j j i
j=1
X
where we have used the matrix-vector product identity from earlier.
Insummary: theisocontoursoff(x)=x Axareellipsoidssuchthattheaxespointinthedirections
>
of the eigenvectors of A, and the radii of these axes are proportional to the inverse square roots of
the corresponding eigenvalues.
3.12 Singular value decomposition
Singular value decomposition (SVD) is a widely applicable tool in linear algebra. Its strength stems
partially from the fact that every matrix A R m ⇥ n has an SVD (even non-square matrices)! The
2
decomposition goes as follows:
A=U⌃V
>
where U R m ⇥ m and V R n ⇥ n are orthogonal matrices and ⌃ R m ⇥ n is a diagonal matrix with
2 2 2
the singular values of A (denoted   ) on its diagonal.
i
Onlythefirstr =rank(A)singularvaluesarenonzero,andbyconvention,theyareinnon-increasing
order, i.e.
      >  = =  =0
1 2 r r+1 min(m,n)
   ···  ···
Another way to write the SVD (cf. the sum-of-outer-products identity) is
r
A=   u v
i i >i
i=1
X
where u and v are the ith columns of U and V, respectively.
i i
20

Observe that the SVD factors provide eigendecompositions for A A and AA :
> >
A A=(U⌃V ) U⌃V =V⌃ U U⌃V =V⌃ ⌃V
> >> > > > > > >
AA =U⌃V (U⌃V ) =U⌃V V⌃ U =U⌃⌃ U
> > >> > > > > >
It follows immediately that the columns of V (the right-singular vectors of A) are eigenvectors
of A A, and the columns of U (the left-singular vectors of A) are eigenvectors of AA .
> >
Thematrices⌃ ⌃and⌃⌃ arenotnecessarilythesamesize,butbotharediagonalwiththesquared
> >
singular values  2 on the diagonal (plus possibly some zeros). Thus the singular values of A are the
i
square roots of the eigenvalues of A A (or equivalently, of AA )6.
> >
3.13 Fundamental Theorem of Linear Algebra
Despite its fancy name, the “Fundamental Theorem of Linear Algebra” is not a universally-agreed-
upon theorem; there is some ambiguity as to exactly what statements it includes. The version we
present here is su cient for our purposes.
Theorem 4. If A R m ⇥ n, then
2
(i) null(A)=range(A )
> ?
(ii) null(A) range(A
>
)=R n
 
(iii) dimrange(A)+dimnull(A)=n.7
rank(A)
| {z }
(iv) If A = U⌃V is the singular value decomposition of A, then the columns of U and V form
>
orthonormal bases for the four “fundamental subspaces” of A:
Subspace Columns
range(A) The first r columns of U
range(A ) The first r columns of V
>
null(A ) The last m r columns of U
>
 
null(A) The last n r columns of V
 
where r =rank(A).
Proof. (i) Let a ,...,a denote the rows of A. Then
1 m
x null(A) Ax=0
2 ()
a x=0 for all i=1,...,m
()
>i
(↵ a + +↵ a ) x=0 for all ↵ ,...,↵
1 1 m m > 1 m
() ···
v x=0 for all v range(A )
> >
() 2
x range(A )
> ?
() 2
which proves the result.
6RecallthatA>AandAA>arepositivesemi-definite,sotheireigenvaluesarenonnegative,andthustakingsquare
rootsisalwayswell-defined.
7 Thisresultissometimesreferredtobyitselfastherank-nullity theorem.
21

(ii) Recall our previous result on orthogonal complements: if S is a finite-dimensional subspace
of V, then V = S S ? . Thus the claim follows from the previous part (take V = R n and
 
S =range(A )).
>
(iii) Recall that if U and W are subspaces of a finite-dimensional vector space V, then dim(U
 
W) = dimU +dimW. Thus the claim follows from the previous part, using the fact that
dimrange(A)=dimrange(A ).
>
A direct result of (ii) is that every x R n can be written (uniquely) in the form
2
x=A v+w
>
for some v R m,w R n, where Aw=0.
2 2
Note that there is some asymmetry in the theorem, but analogous statements can be obtained by
applying the theorem to A .
>
3.14 Operator and matrix norms
If V and W are vector spaces, then the set of linear maps from V to W forms another vector space,
and the norms defined on V and W induce a norm on this space of linear maps. If T :V W is a
!
linear map between normed spaces V and W, then the operator norm is defined as
Tx
W
T =maxk k
op
k k x x2= V 0 k x k V
6
AnimportantclassofthisgeneraldefinitioniswhenthedomainandcodomainareR n andR m, and
the p-norm is used in both cases. Then for a matrix A R m ⇥ n, we can define the matrix p-norm
2
Ax
p
A =maxk k
p
k k x=0 x p
6 k k
In the special cases p=1,2, we have
1
m
A = max A
1 ij
k k 1 j n | |
  i=1
X
n
A = max A
ij
k k1 1 i m | |
 j=1
X
A =  (A)
2 1
k k
where   denotes the largest singular value. Note that the induced 1- and -norms are simply
1
1
the maximum absolute column and row sums, respectively. The induced 2-norm (often called the
spectral norm) simplifies to   by the properties of Rayleigh quotients proved earlier; clearly
1
Ax Ax 2 x A Ax
argmaxk k 2 =argmaxk k2 =argmax > >
x x 2 x x
x 6 =0 k k 2 x 6 =0 k k2 x 6 =0 >
andwehaveseenthattherightmostexpressionismaximizedbyaneigenvectorofA Acorresponding
>
to its largest eigenvalue,   (A A)= 2(A).
max > 1
22

By definition, these induced matrix norms have the important property that
Ax A x
p p p
k k k k k k
for any x. They are also submultiplicative in the following sense.
Proposition 8. AB A B
p p p
k k k k k k
Proof. For any x,
ABx A Bx A B x
p p p p p p
k k k k k k k k k k k k
so
ABx A B x
p p p
AB =maxk k maxk k k k k k = A B
p p p
k k x=0 x p  x=0 x p k k k k
6 k k 6 k k
These are not the only matrix norms, however. Another frequently used is the Frobenius norm
m n min(m,n)
A = A2 = tr(A A)=  2(A)
k k f v ij > v i
u uX i=1 X j=1 q u u X i=1
t t
Thefirstequivalencefollowsstraightforwardlybyexpandingthedefinitionsofmatrixmultiplication
and trace. For the second, observe that (writing A=U⌃V as before)
>
min(m,n)
tr(A A)=tr(V⌃ ⌃V )=tr(V V⌃ ⌃)=tr(⌃ ⌃)=  2(A)
> > > > > > i
i=1
X
using the cyclic property of trace and orthogonality of V.
A matrix norm is said to be unitary invariant if
k·k
UAV = A
k k k k
for all orthogonal U and V of appropriate size. Unitary invariant norms essentially depend only on
the singular values of a matrix, since for such norms,
A = U⌃V = ⌃
>
k k k k k k
Two particular norms we have seen, the spectral norm and the Frobenius norm, can be expressed
solely in terms of a matrix’s singular values.
Proposition 9. The spectral norm and the Frobenius norm are unitary invariant.
Proof. For the Frobenius norm, the claim follows from
tr((UAV) UAV)=tr(V A U UAV)=tr(VV A A)=tr(A A)
> > > > > > >
For the spectral norm, recall that Ux = x for any orthogonal U. Thus
2 2
k k k k
UAVx AVx Ay
2 2 2
UAV =maxk k =maxk k =maxk k = A
2 2
k k x=0 x 2 x=0 x 2 y=0 y 2 k k
6 k k 6 k k 6 k k
where we have used the change of variable y = V x, which satisfies y = x . Since V is
> 2 2 >
k k k k
invertible, x and y are in one-to-one correspondence, and in particular y = 0 if and only if x = 0.
Hence maximizing over y=0 is equivalent to maximizing over x=0.
6 6
23

3.15 Low-rank approximation
AnimportantpracticalapplicationoftheSVDistocomputelow-rank approximationstomatri-
ces. That is, given some matrix, we want to find another matrix of the same dimensions but lower
ranksuchthatthetwomatricesarecloseasmeasuredbysomenorm. Suchanapproximationcanbe
usedtoreducetheamountofdataneededtostoreamatrix, whileretainingmostofitsinformation.
AremarkableresultknownastheEckart-Young-Mirskytheoremtellsusthattheoptimalmatrix
canbecomputedeasilyfromtheSVD,aslongasthenorminquestionisunitaryinvariant(e.g., the
spectral norm or Frobenius norm).
Theorem 5. (Eckart-Young-Mirsky) Let be a unitary invariant matrix norm. Suppose A
R m ⇥ n, where m   n, has singular value d k e ·k composition A = n i=1   i u i v >i . Then the best rank- 2 k
approximation to A, where k rank(A), is given by
 P
k
A =   u v
k i i >i
i=1
X
in the sense that
A A A A˜
k
k   kk   k
for any A˜ R m ⇥ n with rank(A˜) k.
2 
Theproofofthegeneralcaserequiresafairamountofwork,soweproveonlythespecialcasewhere
is the spectral norm.
k·k
Proof. First we compute
n k n
A A =   u v   u v =   u v = 
k   k k 2   i i >i   i i >i    i i >i  k+1
 i=1 i=1    i=k+1  
 X X  2   X  2
       
       
Let A˜ R m ⇥ n have rank(A˜)  k. Then by the Fundam enta l Theorem of Linear Algebra,
2 
dimnull(A˜)=n rank(A˜) n k
     
It follows that
null(A˜) span v ,...,v
1 k+1
\ { }
is non-trivial (has a nonzero element), because otherwise there would be at least (n k)+(k+1)=
 
n+1 linearly independent vectors in R n, which is impossible. Therefore let z be some element of
the intersection, and assume without loss of generality that it has unit norm: z = 1. Expand
2
k k
z=↵ v + +↵ v , noting that
1 1 k+1 k+1
···
1= z 2 = ↵ v + +↵ v 2 =↵2+ +↵2
k k2 k 1 1 ··· k+1 k+1 k2 1 ··· k+1
24

by the Pythagorean theorem. Thus
A A˜ (A A˜)z by def., and z =1
2 2 2
k   k  k   k k k
= Az z null(A˜)
2
k k 2
n
=   u v z
  i i >i  
 i=1  
 X  2
   
 k+1  
   
=   ↵ u
  i i i 
 i=1  
 X  2
   
=  ( 
1
↵
1
)2+  +( 
k+1
↵
k+1
)2 Pythagorean theorem again
   ···
p  ↵2+ +↵2     for i k
  k+1 1 ··· k+1 k+1  i 
= A qA using our earlier results
k 2
k   k
as was to be shown.
A measure of the quality of the approximation is given by
A 2  2+ + 2
k k kf = 1 ··· k
A 2  2+ + 2
k kf 1 ··· r
Ideally, this ratio will be close to 1, indicating that most of the information was retained.
3.16 Pseudoinverses
Let A R m ⇥ n. If m=n, then A cannot possibly be invertible. However, there is a generalization
2 6
of the inverse known as the Moore-Penrose pseudoinverse, denoted A † R n ⇥ m, which always
2
exists and is defined uniquely by the following properties:
(i) AA A=A
†
(ii) A AA =A
† † †
(iii) AA is symmetric
†
(iv) A A is symmetric
†
If A is invertible, then A = A 1. More generally, we can compute the pseudoinverse of a matrix
†  
from its singular value decomposition: if A=U⌃V , then
>
A =V⌃ U
† † >
where ⌃ can be computed from ⌃ by taking the transpose and inverting the nonzero singular
†
values on the diagonal. Verifying that this matrix satisfies the properties of the pseudoinverse is
straightforward and left as an exercise to the reader.
25

3.17 Some useful matrix identities
3.17.1 Matrix-vector product as linear combination of matrix columns
Proposition 10. Let x R n be a vector and A R m ⇥ n a matrix with columns a 1 ,...,a n . Then
2 2
n
Ax= x a
i i
i=1
X
This identity is extremely useful in understanding linear operators in terms of their matrices’
columns. The proof is very simple (consider each element of Ax individually and expand by defini-
tions) but it is a good exercise to convince yourself.
3.17.2 Sum of outer products as matrix-matrix product
An outer product is an expression of the form ab > , where a R m and b R n. By inspection it
2 2
is not hard to see that such an expression yields an m n matrix such that
⇥
[ab ] =a b
>ij i j
Itisnotimmediatelyobvious,butthesumofouterproductsisactuallyequivalenttoanappropriate
matrix-matrix product! We formalize this statement as
Proposition 11. Let a 1 ,...,a k R m and b 1 ,...,b k R n. Then
2 2
k
a b =AB
` >` >
`=1
X
where
A= a a , B= b b
1 k 1 k
··· ···
⇥ ⇤ ⇥ ⇤
Proof. For each (i,j), we have
k k k k
a b = [a b ] = [a ] [b ] = A B
2
` >`3 ` >` ij ` i ` j i` j`
`=1 `=1 `=1 `=1
X ij X X X
4 5
This last expression should be recognized as an inner product between the ith row of A and the jth
row of B, or equivalently the jth column of B . Hence by the definition of matrix multiplication, it
>
is equal to [AB ] .
>ij
3.17.3 Quadratic forms
LetA R n ⇥ n beasymmetricmatrix,andrecallthattheexpressionx > Axiscalledaquadraticform
2
of A. It is in some cases helpful to rewrite the quadratic form in terms of the individual elements
that make up A and x:
n n
x Ax= A x x
> ij i j
i=1j=1
XX
This identity is valid for any square matrix (need not be symmetric), although quadratic forms are
usually only discussed in the context of symmetric matrices.
26

4 Calculus and Optimization
Muchofmachinelearningisaboutminimizingacost function(alsocalledanobjective function
intheoptimizationcommunity),whichisascalarfunctionofseveralvariablesthattypicallymeasures
how poorly our model fits the data we have.
4.1 Extrema
Optimization is about finding extrema, which depending on the application could be minima or
maxima. When defining extrema, it is necessary to consider the set of inputs over which we’re
optimizing. This set R d is called the feasible set. If is the entire domain of the function
X✓ X
being optimized (as it often will be for our purposes), we say that the problem is unconstrained.
Otherwise the problem is constrained and may be much harder to solve, depending on the nature
of the feasible set.
Suppose f :R d R. A point x is said to be a local minimum (resp. local maximum) of f in
! X
iff(x) f(y)(resp. f(x) f(y))forallyinsomeneighborhoodN aboutx.8 Furthermore,if
   ✓X
f(x) f(y) for all y , then x is a global minimum of f in (similarly for global maximum).
 2X X
If the phrase “in ” is unclear from context, assume we are optimizing over the whole domain of
X
the function.
Thequalifierstrict(asine.g. astrictlocalminimum)meansthattheinequalitysigninthedefinition
is actually a > or <, with equality not allowed. This indicates that the extremum is unique within
some neighborhood.
Observethatmaximizingafunctionf isequivalenttominimizing f, sooptimizationproblemsare
 
typically phrased in terms of minimization without loss of generality. This convention (which we
follow here) eliminates the need to discuss minimization and maximization separately.
4.2 Gradients
Thesinglemostimportantconceptfromcalculusinthecontextofmachinelearningisthegradient.
Gradientsgeneralizederivativestoscalarfunctionsofseveralvariables. Thegradientoff :R d R,
!
denoted f, is given by
r
@f
@x . 1 @f
f =2 . . 3 i.e. [ f] i =
r r @x
i
@f
6 7
6@xn7
Gradients have the following very imp4ortan5t property: f(x) points in the direction of steepest
r
ascent from x. Similarly, f(x) points in the direction of steepest descent from x. We will
 r
use this fact frequently when iteratively minimizing a function via gradient descent.
4.3 The Jacobian
The Jacobian of f :R n R m is a matrix of first-order partial derivatives:
!
@f1 ... @f1
J f =2 @x . . . 1 ... @x . . . n 3 i.e. [J f ] ij = @f i
@x
j
6 @fm ... @fm7
6@x1 @xn7
4 5
8 Aneighborhoodaboutxisanopensetwhichcontainsx.
27

Note the special case m=1, where f =J .
r
>f
4.4 The Hessian
The Hessian matrix of f :R d R is a matrix of second-order partial derivatives:
!
@2f
...
@2f
2f =2
@x
. .
.
2
1
...
@x1
. .
.
@xd
3 i.e. [ 2f]
ij
=
@2f
r r @x @x
i j
6 @2f ... @2f 7
6
6
@xd@x1 @x2
d
7
7
4 5
Recall that if the partial derivatives are continuous, the order of di↵erentiation can be interchanged
(Clairaut’s theorem), so the Hessian matrix will be symmetric. This will typically be the case for
di↵erentiable functions that we work with.
The Hessian is used in some optimization algorithms such as Newton’s method. It is expensive to
calculatebutcandrasticallyreducethenumberofiterationsneededtoconvergetoalocalminimum
by providing information about the curvature of f.
4.5 Matrix calculus
Since a lot of optimization reduces to finding points where the gradient vanishes, it is useful to have
di↵erentiation rules for matrix and vector expressions. We give some common rules here. Probably
the two most important for our purposes are
(a x)=a
x >
r
(x Ax)=(A+A )x
x > >
r
Note that this second rule is defined only if A is square. Furthermore, if A is symmetric, we can
simplify the result to 2Ax.
4.5.1 The chain rule
Most functions that we wish to optimize are not completely arbitrary functions, but rather are
composed of simpler functions which we know how to handle. The chain rule gives us a way to
calculate derivatives for a composite function in terms of the derivatives of the simpler functions
that make it up.
The chain rule from single-variable calculus should be familiar:
(f g)(x)=f (g(x))g (x)
0 0 0
 
where denotes function composition. There is a natural generalization of this rule to multivariate
 
functions.
Proposition 12. Suppose f :R m R k and g :R n R m. Then f g :R n R k and
! !   !
J (x)=J (g(x))J (x)
f g f g
 
In the special case k =1 we have the following corollary since f =J .
r
>f
Corollary 1. Suppose f :R m R and g :R n R m. Then f g :R n R and
! !   !
(f g)(x)=J (x) f(g(x))
g >
r   r
28

4.6 Taylor’s theorem
Taylor’s theorem has natural generalizations to functions of more than one variable. We give the
version presented in [1].
Theorem 6. (Taylor’s theorem) Suppose f :R d R is continuously di↵erentiable, and let h R d.
! 2
Then there exists t (0,1) such that
2
f(x+h)=f(x)+ f(x+th) h
>
r
Furthermore, if f is twice continuously di↵erentiable, then
1
f(x+h)= f(x)+ 2f(x+th)hdt
r r r
Z0
and there exists t (0,1) such that
2
1
f(x+h)=f(x)+ f(x) h+ h 2f(x+th)h
> >
r 2 r
This theorem is used in proofs about conditions for local minima of unconstrained optimization
problems. Some of the most important results are given in the next section.
4.7 Conditions for local minima
Proposition13. Ifx isalocalminimumoff andf iscontinuouslydi↵erentiableinaneighborhood
⇤
of x , then f(x )=0.
⇤ ⇤
r
Proof. Let x be a local minimum of f, and suppose towards a contradiction that f(x )=0. Let
⇤ ⇤
r 6
h= f(x ), noting that by the continuity of f we have
⇤
 r r
lim f(x +th)= f(x )=h
⇤ ⇤
t 0 r  r
!
Hence
limh f(x +th)=h f(x )= h 2 <0
t 0 > r ⇤ > r ⇤  k k2
!
Thus there exists T > 0 such that h f(x +th) < 0 for all t [0,T]. Now we apply Taylor’s
> ⇤
r 2
theorem: for any t (0,T], there exists t (0,t) such that
0
2 2
f(x +th)=f(x )+th f(x +th)<f(x )
⇤ ⇤ > ⇤ 0 ⇤
r
whence it follows that x is not a local minimum, a contradiction. Hence f(x )=0.
⇤ ⇤
r
The proof shows us why the vanishing gradient is necessary for an extremum: if f(x) is nonzero,
r
therealwaysexistsasu cientlysmallstep↵> 0suchthatf(x ↵ f(x)))<f(x). Forthisreason,
  r
f(x) is called a descent direction.
 r
Pointswherethegradientvanishesarecalledstationarypoints. Notethatnotallstationarypoints
are extrema. Consider f : R 2 R given by f(x,y) = x2 y2. We have f(0) = 0, but the point
!   r
0 is the minimum along the line y = 0 and the maximum along the line x = 0. Thus it is neither
a local minimum nor a local maximum of f. Points such as these, where the gradient vanishes but
there is no local extremum, are called saddle points.
We have seen that first-order information (i.e. the gradient) is insu cient to characterize local
minima. But we can say more with second-order information (i.e. the Hessian). First we prove a
necessary second-order condition for local minima.
29

Proposition 14. If x is a local minimum of f and f is twice continuously di↵erentiable in a
⇤
neighborhood of x , then 2f(x ) is positive semi-definite.
⇤ ⇤
r
Proof. Let x be a local minimum of f, and suppose towards a contradiction that 2f(x ) is not
⇤ ⇤
r
positive semi-definite. Let h be such that h 2f(x )h < 0, noting that by the continuity of 2f
> ⇤
r r
we have
lim 2f(x +th)= 2f(x )
⇤ ⇤
t 0r r
!
Hence
limh 2f(x +th)h=h 2f(x )h<0
> ⇤ > ⇤
t 0 r r
!
Thus there exists T > 0 such that h 2f(x +th)h < 0 for all t [0,T]. Now we apply Taylor’s
> ⇤
r 2
theorem: for any t (0,T], there exists t (0,t) such that
0
2 2
1
f(x +th)=f(x )+th f(x )+ t2h 2f(x +th)h<f(x )
⇤ ⇤ > ⇤ > ⇤ 0 ⇤
r 2 r
0
where the middle term vanishes becaus|e {fz(x
⇤
)}= 0 by the previous result. It follows that x
⇤
is
r
not a local minimum, a contradiction. Hence 2f(x ) is positive semi-definite.
⇤
r
Now we give su cient conditions for local minima.
Proposition 15. Suppose f is twice continuously di↵erentiable with 2f positive semi-definite in
r
a neighborhood of x , and that f(x ) = 0. Then x is a local minimum of f. Furthermore if
⇤ ⇤ ⇤
r
2f(x ) is positive definite, then x is a strict local minimum.
⇤ ⇤
r
Proof. LetB beanopenballofradiusr >0centeredatx whichiscontainedintheneighborhood.
⇤
Applying Taylor’s theorem, we have that for any h with h <r, there exists t (0,1) such that
2
k k 2
1
f(x +h)=f(x )+h f(x )+ h 2f(x +th)h f(x )
⇤ ⇤ > ⇤ > ⇤ ⇤
r 2 r  
0
The last inequality holds because 2f(|x +{zth)}is positive semi-definite (since th = t h <
⇤ 2 2
r k k k k
h <r), so h 2f(x +th)h 0. Since f(x ) f(x +h) for all h with h <r, we conclude
2 > ⇤ ⇤ ⇤ 2
k k r    k k
that x is a local minimum.
⇤
Now further suppose that 2f(x ) is strictly positive definite. Since the Hessian is continuous we
⇤
r
canchooseanotherballB withradiusr >0centeredatx suchthat 2f(x)ispositivedefinitefor
0 0 ⇤
r
all x B . Then following the same argument as above (except with a strict inequality now since
0
2
the Hessian is positive definite) we have f(x +h)>f(x ) for all h with 0< h <r . Hence x
⇤ ⇤ 2 0 ⇤
k k
is a strict local minimum.
Notethat,perhapscounterintuitively,theconditions f(x )=0and 2f(x )positivesemi-definite
⇤ ⇤
r r
are not enough to guarantee a local minimum at x ! Consider the function f(x) = x3. We have
⇤
f (0) = 0 and f (0) = 0 (so the Hessian, which in this case is the 1 1 matrix 0 , is positive
0 00
⇥
semi-definite). But f has a saddle point at x = 0. The function f(x) = x4 is an even worse
  ⇥ ⇤
o↵ender – it has the same gradient and Hessian at x = 0, but x = 0 is a strict local maximum for
this function!
For these reasons we require that the Hessian remains positive semi-definite as long as we are close
to x . Unfortunately, this condition is not practical to check computationally, but in some cases we
⇤
can verify it analytically (usually by showing that 2f(x) is p.s.d. for all x R d). Also, if 2f(x ⇤ )
r 2 r
is strictly positive definite, the continuity assumption on f implies this condition, so we don’t have
to worry.
30

(a) A convex set (b) A non-convex set
Figure 1: What convex sets look like
4.8 Convexity
Convexity is a term that pertains to both sets and functions. For functions, there are di↵erent
degrees ofconvexity, and how convex afunction istells usalotabout itsminima: dotheyexist, are
they unique, how quickly can we find them using optimization algorithms, etc. In this section, we
present basic results regarding convexity, strict convexity, and strong convexity.
4.8.1 Convex sets
A set R d is convex if
X✓
tx+(1 t)y
  2X
for all x,y and all t [0,1].
2X 2
Geometrically, this means that all the points on the line segment between any two points in are
X
also in . See Figure 1 for a visual.
X
Why do we care whether or not a set is convex? We will see later that the nature of minima can
depend greatly on whether or not the feasible set is convex. Undesirable pathological results can
occur when we allow the feasible set to be arbitrary, so for proofs we will need to assume that it is
convex. Fortunately, we often want to minimize over all of R d, which is easily seen to be a convex
set.
4.8.2 Basics of convex functions
In the remainder of this section, assume f : R d R unless otherwise noted. We’ll start with the
!
definitions and then give some results.
A function f is convex if
f(tx+(1 t)y) tf(x)+(1 t)f(y)
    
for all x,y domf and all t [0,1].
2 2
31

Figure 2: What convex functions look like
If the inequality holds strictly (i.e. < rather than ) for all t (0,1) and x = y, then we say that
 2 6
f is strictly convex.
A function f is strongly convex with parameter m (or m-strongly convex) if the function
m
x f(x) x 2
7!   2 k k2
is convex.
These conditions are given in increasing order of strength; strong convexity implies strict convexity
which implies convexity.
Geometrically, convexity means that the line segment between two points on the graph of f lies on
or above the graph itself. See Figure 2 for a visual.
Strictconvexitymeansthatthelinesegmentliesstrictlyabovethegraphoff,exceptatthesegment
endpoints. (So actually the function in the figure appears to be strictly convex.)
4.8.3 Consequences of convexity
Why do we care if a function is (strictly/strongly) convex?
Basically, our various notions of convexity have implications about the nature of minima. It should
not be surprising that the stronger conditions tell us more about the minima.
Proposition 16. Let be a convex set. If f is convex, then any local minimum of f in is also
X X
a global minimum.
Proof. Suppose f is convex, and let x be a local minimum of f in . Then for some neighborhood
⇤
X
N about x , we have f(x) f(x ) for all x N. Suppose towards a contradiction that there
⇤ ⇤
✓X   2
exists x˜ such that f(x˜)<f(x ).
⇤
2X
32

Consider the line segment x(t)=tx +(1 t)x˜, t [0,1], noting that x(t) by the convexity of
⇤
  2 2X
. Then by the convexity of f,
X
f(x(t)) tf(x )+(1 t)f(x˜)<tf(x )+(1 t)f(x )=f(x )
⇤ ⇤ ⇤ ⇤
    
for all t (0,1).
2
We can pick t to be su ciently close to 1 that x(t) N; then f(x(t)) f(x ) by the definition of
⇤
2  
N, but f(x(t))<f(x ) by the above inequality, a contradiction.
⇤
It follows that f(x ) f(x) for all x , so x is a global minimum of f in .
⇤ ⇤
 2X X
Proposition 17. Let be a convex set. If f is strictly convex, then there exists at most one local
X
minimum of f in . Consequently, if it exists it is the unique global minimum of f in .
X X
Proof. The second sentence follows from the first, so all we must show is that if a local minimum
exists in then it is unique.
X
Suppose x is a local minimum of f in , and suppose towards a contradiction that there exists a
⇤
X
local minimum x˜ such that x˜ =x .
⇤
2X 6
Sincef isstrictlyconvex,itisconvex,sox andx˜ arebothglobalminimaoff in bytheprevious
⇤
X
result. Hence f(x )=f(x˜). Consider the line segment x(t)=tx +(1 t)x˜, t [0,1], which again
⇤ ⇤
  2
must lie entirely in . By the strict convexity of f,
X
f(x(t))<tf(x )+(1 t)f(x˜)=tf(x )+(1 t)f(x )=f(x )
⇤ ⇤ ⇤ ⇤
   
for all t (0,1). But this contradicts the fact that x is a global minimum. Therefore if x˜ is a local
⇤
2
minimum of f in , then x˜ =x , so x is the unique minimum in .
⇤ ⇤
X X
It is worthwhile to examine how the feasible set a↵ects the optimization problem. We will see why
the assumption that is convex is needed in the results above.
X
Consider the function f(x) = x2, which is a strictly convex function. The unique global minimum
of this function in R is x=0. But let’s see what happens when we change the feasible set .
X
(i) = 1 : This set is actually convex, so we still have a unique global minimum. But it is not
X { }
the same as the unconstrained minimum!
(ii) =R 0 : Thissetisnon-convex,andwecanseethatf hasnominimain . Foranypoint
X \{ } X
x , one can find another point y such that f(y)<f(x).
2X 2X
(iii) =( , 1] [0, ): This set is non-convex, and we can see that there is a local minimum
X  1   [ 1
(x= 1) which is distinct from the global minimum (x=0).
 
(iv) = ( , 1] [1, ): This set is non-convex, and we can see that there are two global
X  1   [ 1
minima (x= 1).
±
4.8.4 Showing that a function is convex
Hopefully the previous section has convinced the reader that convexity is an important property.
Next we turn to the issue of showing that a function is (strictly/strongly) convex. It is of course
possible (in principle) to directly show that the condition in the definition holds, but this is usually
not the easiest way.
Proposition 18. Norms are convex.
33

Proof. Let be a norm on a vector space V. Then for all x,y V and t [0,1],
k·k 2 2
tx+(1 t)y tx + (1 t)y = t x + 1 t y =t x +(1 t) y
k   kk k k   k | |k k |   |k k k k   k k
wherewehaveusedrespectivelythetriangleinequality,thehomogeneityofnorms,andthefactthat
t and 1 t are nonnegative. Hence is convex.
  k·k
Proposition 19. Suppose f is di↵erentiable. Then f is convex if and only if
f(x) f(y)+ f(y),x y
  hr   i
for all x,y domf.
2
Proof. (= ) Suppose f is convex, i.e.
)
f(tx+(1 t)y) tf(x)+(1 t)f(y)=f(y)+t(f(x) f(y))
      
for all x,y domf and all t [0,1]. Rearranging gives
2 2
f(y+t(x y)) f(y)
    f(x) f(y)
t   
As t 0, the left-hand side becomes f(y),x y , so the result follows.
! hr   i
( =) Suppose
(
f(x) f(y)+ f(y),x y
  hr   i
for all x,y domf. Fix x,y domf, t [0,1], and define z=tx+(1 t)y. Then
2 2 2  
f(x) f(z)+ f(z),x z
  hr   i
f(y) f(z)+ f(z),y z
  hr   i
so
tf(x)+(1 t)f(y) t f(z)+ f(z),x z +(1 t) f(z)+ f(z),y z
    hr   i   hr   i
=f(z)+ f(z),t(x z)+(1 t)(y z)
       
hr       i
=f(tx+(1 t)y)+ f(z),tx+(1 t)y z
  hr     i
0
=f(tx+(1 t)y)
  | {z }
implying that f is convex.
Proposition 20. Suppose f is twice di↵erentiable. Then
(i) f is convex if and only if 2f(x) 0 for all x domf.
r ⌫ 2
(ii) If 2f(x) 0 for all x domf, then f is strictly convex.
r   2
(iii) f is m-strongly convex if and only if 2f(x) mI for all x domf.
r ⌫ 2
Proof. Omitted.
Proposition 21. If f is convex and ↵ 0, then ↵f is convex.
 
34

Proof. Suppose f is convex and ↵ 0. Then for all x,y dom(↵f)=domf,
  2
(↵f)(tx+(1 t)y)=↵f(tx+(1 t)y)
   
↵ tf(x)+(1 t)f(y)
  
=t(↵f(x))+(1 t)(↵f(y))
   
 
=t(↵f)(x)+(1 t)(↵f)(y)
 
so ↵f is convex.
Proposition 22. If f and g are convex, then f +g is convex. Furthermore, if g is strictly convex,
then f +g is strictly convex, and if g is m-strongly convex, then f +g is m-strongly convex.
Proof. Suppose f and g are convex. Then for all x,y dom(f +g)=domf domg,
2 \
(f +g)(tx+(1 t)y)=f(tx+(1 t)y)+g(tx+(1 t)y)
     
tf(x)+(1 t)f(y)+g(tx+(1 t)y) convexity of f
    
tf(x)+(1 t)f(y)+tg(x)+(1 t)g(y) convexity of g
    
=t(f(x)+g(x))+(1 t)(f(y)+g(y))
 
=t(f +g)(x)+(1 t)(f +g)(y)
 
so f +g is convex.
If g is strictly convex, the second inequality above holds strictly for x=y and t (0,1), so f +g is
6 2
strictly convex.
If g is m-strongly convex, then the function h(x) g(x) m x 2 is convex, so f+h is convex. But
⌘   2k k2
m m
(f +h)(x) f(x)+h(x) f(x)+g(x) x 2 (f +g)(x) x 2
⌘ ⌘   2 k k2 ⌘   2 k k2
so f +g is m-strongly convex.
Proposition 23. If f ,...,f are convex and ↵ ,...,↵ 0, then
1 n 1 n
 
n
↵ f
i i
i=1
X
is convex.
Proof. Follows from the previous two propositions by induction.
Proposition 24. If f is convex, then g(x) f(Ax+b) is convex for any appropriately-sized A
⌘
and b.
Proof. Suppose f is convex and g is defined like so. Then for all x,y domg,
2
g(tx+(1 t)y)=f(A(tx+(1 t)y)+b)
   
=f(tAx+(1 t)Ay+b)
 
=f(tAx+(1 t)Ay+tb+(1 t)b)
   
=f(t(Ax+b)+(1 t)(Ay+b))
 
tf(Ax+b)+(1 t)f(Ay+b) convexity of f
  
=tg(x)+(1 t)g(y)
 
Thus g is convex.
35

Proposition 25. If f and g are convex, then h(x) max f(x),g(x) is convex.
⌘ { }
Proof. Suppose f and g are convex and h is defined like so. Then for all x,y domh,
2
h(tx+(1 t)y)=max f(tx+(1 t)y),g(tx+(1 t)y)
  {     }
max tf(x)+(1 t)f(y),tg(x)+(1 t)g(y)
 {     }
max tf(x),tg(x) +max (1 t)f(y),(1 t)g(y)
 { } {     }
=tmax f(x),g(x) +(1 t)max f(y),g(y)
{ }   { }
=th(x)+(1 t)h(y)
 
Note that in the first inequality we have used convexity of f and g plus the fact that a c,b d
 
impliesmax a,b max c,d . Inthesecondinequalitywehaveusedthefactthatmax a+b,c+d
{ } { } { }
max a,c +max b,d .
{ } { }
Thus h is convex.
4.8.5 Examples
A good way to gain intuition about the distinction between convex, strictly convex, and strongly
convex functions is to consider examples where the stronger property fails to hold.
Functions that are convex but not strictly convex:
(i) f(x) = w > x+↵ for any w R d,↵ R. Such a function is called an a ne function, and it
2 2
is both convex and concave. (In fact, a function is a ne if and only if it is both convex and
concave.) Notethatlinearfunctionsandconstantfunctionsarespecialcasesofa nefunctions.
(ii) f(x)= x
1
k k
Functions that are strictly but not strongly convex:
(i) f(x) = x4. This example is interesting because it is strictly convex but you cannot show this
fact via a second-order argument (since f (0)=0).
00
(ii) f(x) = exp(x). This example is interesting because it’s bounded below but has no local
minimum.
(iii) f(x)= logx. Thisexampleisinterestingbecauseit’sstrictlyconvexbutnotboundedbelow.
 
Functions that are strongly convex:
(i) f(x)= x 2
k k2
36

5 Probability
Probability theory provides powerful tools for modeling and dealing with uncertainty.
5.1 Basics
Suppose we have some sort of randomized experiment (e.g. a coin toss, die roll) that has a fixed set
of possible outcomes. This set is called the sample space and denoted ⌦.
We would like to define probabilities for some events, which are subsets of ⌦. The set of events is
denoted .9 The complement of the event A is another event, Ac =⌦ A.
F \
Then we can define a probability measure P: [0,1] which must satisfy
F!
(i) P(⌦)=1
(ii) Countable additivity: for any countable collection of disjoint sets A ,
i
{ }✓F
P A i = P(A i )
✓ i ◆ i
[ X
The triple (⌦, ,P) is called a probability space.10
F
If P(A) = 1, we say that A occurs almost surely (often abbreviated a.s.).11, and conversely A
occurs almost never if P(A)=0.
From these axioms, a number of useful rules can be derived.
Proposition 26. Let A be an event. Then
(i) P(Ac)=1 P(A).
 
(ii) If B is an event and B A, then P(B) P(A).
✓ 
(iii) 0=P(?) P(A) P(⌦)=1
 
Proof. (i) Using the countable additivity of P, we have
P(A)+P(Ac)=P(A ˙ Ac)=P(⌦)=1
[
To show (ii), suppose B and B A. Then
2F ✓
P(A)=P(B ˙ (A B))=P(B)+P(A B) P(B)
[ \ \  
as claimed.
For (iii): the middle inequality follows from (ii) since ? A ⌦. We also have
✓ ✓
P(?)=P(? ˙ ?)=P(?)+P(?)
[
by countable additivity, which shows P(?)=0.
9 isrequiredtobea -algebrafortechnicalreasons;see[2].
10 F Notethataprobabilityspaceissimplyameasurespaceinwhichthemeasureofthewholespaceequals1.
11 Thisisaprobabilist’sversionofthemeasure-theoretictermalmost everywhere.
37

Proposition 27. If A and B are events, then P(A B)=P(A)+P(B) P(A B).
[   \
Proof. The key is to break the events up into their various overlapping and non-overlapping parts.
P(A B)=P((A B) ˙ (A B) ˙ (B A))
[ \ [ \ [ \
=P(A B)+P(A B)+P(B A)
\ \ \
=P(A B)+P(A) P(A B)+P(B) P(A B)
\   \   \
=P(A)+P(B) P(A B)
  \
Proposition 28. If A is a countable set of events, disjoint or not, then
i
{ }✓F
P A i P(A i )

✓ i ◆ i
[ X
This inequality is sometimes referred to as Boole’s inequality or the union bound.
Proof. Define B = A and B = A ( A ) for i > 1, noting that B = A for all i
1 1 i i \ j<i j j i j j i j
and the B are disjoint. Then  
i
S S S
P A i =P B i = P(B i ) P(A i )

✓ i ◆ ✓ i ◆ i i
[ [ X X
where the last inequality follows by monotonicity since B A for all i.
i i
✓
5.1.1 Conditional probability
The conditional probability of event A given that event B has occurred is written P(AB) and
|
defined as
P(A B)
P(AB)= \
| P(B)
assuming P(B)>0.12
5.1.2 Chain rule
Another very useful tool, the chain rule, follows immediately from this definition:
P(A B)=P(AB)P(B)=P(B A)P(A)
\ | |
5.1.3 Bayes’ rule
Taking the equality from above one step further, we arrive at the simple but crucial Bayes’ rule:
P(B A)P(A)
P(AB)= |
| P(B)
12 Insomecasesitispossibletodefineconditionalprobabilityoneventsofprobabilityzero,butthisissignificantly
moretechnicalsoweomitit.
38

It is sometimes beneficial to omit the normalizing constant and write
P(AB) P(A)P(B A)
| / |
Underthisformulation,P(A)isoftenreferredtoastheprior,P(AB)astheposterior,andP(B A)
| |
as the likelihood.
In the context of machine learning, we can use Bayes’ rule to update our “beliefs” (e.g. values of
our model parameters) given some data that we’ve observed.
5.2 Random variables
Arandom variableissomeuncertainquantitywithanassociatedprobabilitydistributionoverthe
values it can assume.
Formally, a random variable on a probability space (⌦, ,P) is a function13 X :⌦ R.14
F !
We denote the range of X by X(⌦)= X(!):! ⌦ . Togive aconcrete example (taken from [3]),
{ 2 }
suppose X is the number of heads in two tosses of a fair coin. The sample space is
⌦= hh,tt,ht,th
{ }
and X is determined completely by the outcome !, i.e. X = X(!). For example, the event X = 1
is the set of outcomes ht,th .
{ }
It is common to talk about the values of a random variable without directly referencing its sample
space. The two are related by the following definition: the event that the value of X lies in some
set S R is
✓
X S = ! ⌦:X(!) S
2 { 2 2 }
Note that special cases of this definition include X being equal to, less than, or greater than some
specified value. For example
P(X =x)=P( ! ⌦:X(!)=x )
{ 2 }
A word on notation: we write p(X) to denote the entire probability distribution of X and p(x)
for the evaluation of the function p at a particular value x X(⌦). Hopefully this (reasonably
2
standard) abuse of notation is not too distracting. If p is parameterized by some parameters ✓, we
write p(X;✓) or p(x;✓), unless we are in a Bayesian setting where the parameters are considered a
random variable, in which case we condition on the parameters.
5.2.1 The cumulative distribution function
The cumulative distribution function (c.d.f.) gives the probability that a random variable is at
most a certain value:
F(x)=P(X x)

The c.d.f. can be used to give the probability that a variable lies within a certain range:
P(a<X b)=F(b) F(a)
  
13 Thefunctionmustbemeasurable.
14 Moregenerally,thecodomaincanbeanymeasurablespace,butRisthemostcommoncasebyfarandsu cient
forourpurposes.
39

5.2.2 Discrete random variables
A discrete random variable is a random variable that has a countable range and assumes each
value in this range with positive probability. Discrete random variables are completely specified by
their probability mass function (p.m.f.) p:X(⌦) [0,1] which satisfies
!
p(x)=1
x 2XX(⌦)
For a discrete X, the probability of a particular value is given exactly by its p.m.f.:
P(X =x)=p(x)
5.2.3 Continuous random variables
A continuous random variable is a random variable that has an uncountable range and assumes
each value in this range with probability zero. Most of the continuous random variables that one
would encounter in practice are absolutely continuous random variables15, which means that
there exists a function p:R [0, ) that satisfies
! 1
x
F(x) p(z)dz
⌘
Z 1
The function p is called a probability density function (abbreviated p.d.f.) and must satisfy
1
p(x)dx=1
Z 1
The values of this function are not themselves probabilities, since they could exceed 1. However,
they do have a couple of reasonable interpretations. One is as relative probabilities; even though
the probability of each particular value being picked is technically zero, some points are still in a
sense more likely than others.
One can also think of the density as determining the probability that the variable will lie in a small
range about a given value. This is because, for small ✏> 0,
x+✏
P(x ✏ X x+✏)= p(z)dz 2✏p(x)
    ⇡
Zx
 
✏
using a midpoint approximation to the integral.
Here are some useful identities that follow from the definitions above:
b
P(a X b)= p(x)dx
 
Za
p(x)=F (x)
0
5.2.4 Other kinds of random variables
Therearerandomvariablesthatareneitherdiscretenorcontinuous. Forexample,considerarandom
variable determined as follows: flip a fair coin, then the value is zero if it comes up heads, otherwise
draw a number uniformly at random from [1,2]. Such a random variable can take on uncountably
many values, but only finitely many of these with positive probability. We will not discuss such
random variables because they are rather pathological and require measure theory to analyze.
15 Random variables that are continuous but not absolutely continuous are called singular random variables.
Wewillnotdiscussthem,assumingratherthatallcontinuousrandomvariablesadmitadensityfunction.
40

5.3 Joint distributions
Oftenwehaveseveralrandomvariablesandwewouldliketogetadistributionoversomecombination
of them. A joint distribution is exactly this. For some random variables X ,...,X , the joint
1 n
distribution is written p(X ,...,X ) and gives probabilities over entire assignments to all the X
1 n i
simultaneously.
5.3.1 Independence of random variables
We say that two variables X and Y are independent if their joint distribution factors into their
respective distributions, i.e.
p(X,Y)=p(X)p(Y)
We can also define independence for more than two random variables, although it is more compli-
cated. Let X be a collection of random variables indexed by I, which may be infinite. Then
i i I
{ }2
X are independent if for every finite subset of indices i ,...,i I we have
i 1 k
{ } 2
k
p(X ,...,X )= p(X )
i1 ik ij
j=1
Y
Forexample,inthecaseofthreerandomvariables,X,Y,Z,werequirethatp(X,Y,Z)=p(X)p(Y)p(Z)
as well as p(X,Y)=p(X)p(Y), p(X,Z)=p(X)p(Z), and p(Y,Z)=p(Y)p(Z).
Itisoftenconvenient(thoughperhapsquestionable)toassumethatabunchofrandomvariablesare
independent and identically distributed (i.i.d.) so that their joint distribution can be factored
entirely:
n
p(X ,...,X )= p(X )
1 n i
i=1
Y
where X ,...,X all share the same p.m.f./p.d.f.
1 n
5.3.2 Marginal distributions
Ifwehaveajointdistributionoversomesetofrandomvariables,itispossibletoobtainadistribution
for a subset of them by “summing out” (or “integrating out” in the continuous case) the variables
we don’t care about:
p(X)= p(X,y)
y
X
5.4 Great Expectations
If we have some random variable X, we might be interested in knowing what is the “average” value
of X. This concept is captured by the expected value (or mean) E[X], which is defined as
E[X]= xp(x)
x 2XX(⌦)
for discrete X and as
1
E[X]= xp(x)dx
Z 1
for continuous X.
41

In words, we are taking a weighted sum of the values that X can take on, where the weights are
the probabilities of those respective values. The expected value has a physical interpretation as the
“center of mass” of the distribution.
5.4.1 Properties of expected value
A very useful property of expectation is that of linearity:
n n
E ↵ i X i +  = ↵ iE[X i ]+ 
2 3
i=1 i=1
X X
4 5
Note that this holds even if the X are not independent!
i
But if they are independent, the product rule also holds:
n n
E X i = E[X i ]
2 3
i=1 i=1
Y Y
4 5
5.5 Variance
Expectationprovidesameasureofthe“center”ofadistribution,butfrequentlywearealsointerested
in what the “spread” is about that center. We define the variance Var(X) of a random variable X
by
2
Var(X)=E X E[X]
 
Inwords,thisistheaveragesquareddeviationof h t hevalueso f i X fromthemeanofX. Usingalittle
algebra and the linearity of expectation, it is straightforward to show that
Var(X)=E[X2] E[X]2
 
5.5.1 Properties of variance
Variance is not linear (because of the squaring in the definition), but one can show the following:
Var(↵X + )=↵2Var(X)
Basically,multiplicativeconstantsbecomesquaredwhentheyarepulledout,andadditiveconstants
disappear (since the variance contributed by a constant is zero).
Furthermore, if X ,...,X are uncorrelated16, then
1 n
Var(X + +X )=Var(X )+ +Var(X )
1 n 1 n
··· ···
5.5.2 Standard deviation
Variance is a useful notion, but it su↵ers from that fact the units of variance are not the same as
the units of the random variable (again because of the squaring). To overcome this problem we can
usestandard deviation, whichisdefinedas Var(X). ThestandarddeviationofX hasthesame
units as X.
p
16 Wehaven’tdefinedthisyet;seetheCorrelationsectionbelow
42

5.6 Covariance
Covariance is a measure of the linear relationship between two random variables. We denote the
covariance between X and Y as Cov(X,Y), and it is defined to be
Cov(X,Y)=E[(X E[X])(Y E[Y])]
   
Note that the outer expectation must be taken over the joint distribution of X and Y.
Again, the linearity of expectation allows us to rewrite this as
Cov(X,Y)=E[XY] E[X]E[Y]
 
Comparing these formulas to the ones for variance, it is not hard to see that Var(X)=Cov(X,X).
A useful property of covariance is that of bilinearity:
Cov(↵X + Y,Z)=↵Cov(X,Z)+ Cov(Y,Z)
Cov(X,↵Y + Z)=↵Cov(X,Y)+ Cov(X,Z)
5.6.1 Correlation
Normalizing the covariance gives the correlation:
Cov(X,Y)
⇢(X,Y)=
Var(X)Var(Y)
Correlationalsomeasuresthelinearrelationshippbetweentwovariables,butunlikecovariancealways
lies between 1 and 1.
 
Two variables are said to be uncorrelated if Cov(X,Y) = 0 because Cov(X,Y) = 0 implies that
⇢(X,Y) = 0. If two variables are independent, then they are uncorrelated, but the converse does
not hold in general.
5.7 Random vectors
So far we have been talking about univariate distributions, that is, distributions of single vari-
ables. Butwecanalsotalkaboutmultivariate distributionswhichgivedistributionsof random
vectors:
X
1
.
X=2 . . 3
X
6 n7
6 7
4 5
The summarizing quantities we have discussed for single variables have natural generalizations to
the multivariate case.
Expectation of a random vector is simply the expectation applied to each component:
E[X
1
]
.
E[X]=2 . . 3
6E[X
n
]
7
6 7
4 5
43

The variance is generalized by the covariance matrix:
Var(X ) Cov(X ,X ) ... Cov(X ,X )
1 1 2 1 n
Cov(X ,X ) Var(X ) ... Cov(X ,X )
2 2 1 2 2 n 3
⌃=E[(X   E[X])(X   E[X]) > ]= . . . . . . ... . . .
6 7
6Cov(X ,X ) Cov(X ,X ) ... Var(X ) 7
6 n 1 n 2 n 7
6 7
4 5
That is, ⌃ =Cov(X ,X ). Since covariance is symmetric in its arguments, the covariance matrix
ij i j
is also symmetric. It’s also positive semi-definite: for any x,
x
>
⌃x=x >E[(X E[X])(X E[X])
>
]x=E[x
>
(X E[X])(X E[X])
>
x]=E[((X E[X])
>
x)2] 0
           
The inverse of the covariance matrix, ⌃ 1, is sometimes called the precision matrix.
 
5.8 Estimation of Parameters
Nowwegetintosomebasictopicsfromstatistics. Wemakesomeassumptionsaboutourproblemby
prescribing a parametric model (e.g. a distribution that describes how the data were generated),
thenwefittheparametersofthemodeltothedata. Howdowechoosethevaluesoftheparameters?
5.8.1 Maximum likelihood estimation
Acommonwaytofitparametersismaximum likelihood estimation(MLE).Thebasicprinciple
of MLE is to choose values that “explain” the data best by maximizing the probability/density of
the data we’ve seen as a function of the parameters. Suppose we have random variables X ,...,X
1 n
and corresponding observations x ,...,x . Then
1 n
✓ˆ =argmax (✓)
mle
L
✓
where is the likelihood function
L
(✓)=p(x ,...,x ;✓)
1 n
L
Often, we assume that X ,...,X are i.i.d. Then we can write
1 n
n
p(x ,...,x ;✓)= p(x ;✓)
1 n i
i=1
Y
At this point, it is usually convenient to take logs, giving rise to the log-likelihood
n
log (✓)= logp(x ;✓)
i
L
i=1
X
This is a valid operation because the probabilities/densities are assumed to be positive, and since
log is a monotonically increasing function, it preserves ordering. In other words, any maximizer of
log will also maximize .
L L
For some distributions, it is possible to analytically solve for the maximum likelihood estimator. If
log isdi↵erentiable,settingthederivativestozeroandtryingtosolvefor✓ isagoodplacetostart.
L
44

5.8.2 Maximum a posteriori estimation
A more Bayesian way to fit parameters is through maximum a posteriori estimation (MAP).
In this technique we assume that the parameters are a random variable, and we specify a prior
distribution p(✓). Then we can employ Bayes’ rule to compute the posterior distribution of the
parameters given the observed data:
p(✓ x ,...,x ) p(✓)p(x ,...,x ✓)
1 n 1 n
| / |
Computing the normalizing constant is often intractable, because it involves integrating over the
parameter space, which may be very high-dimensional. Fortunately, if we just want the MAP
estimate,wedon’tcareaboutthenormalizingconstant! Itdoesnota↵ectwhichvaluesof✓maximize
the posterior. So we have
✓ˆ =argmaxp(✓)p(x ,...,x ✓)
map 1 n
|
✓
Again, if we assume the observations are i.i.d., then we can express this in the equivalent, and
possibly friendlier, form
n
✓ˆ =argmax logp(✓)+ logp(x ✓)
map i
0 | 1
✓
i=1
X
@ A
A particularly nice case is when the prior is chosen carefully such that the posterior comes from the
same family as the prior. In this case the prior is called a conjugate prior. For example, if the
likelihood is binomial and the prior is beta, the posterior is also beta. There are many conjugate
priors; the reader may find this table of conjugate priors useful.
5.9 The Gaussian distribution
Therearemanydistributions,butoneofparticularimportanceistheGaussian distribution,also
known as the normal distribution. It is a continuous distribution, parameterized by its mean
µ R d and positive-definite covariance matrix ⌃ R d ⇥ d, with density
2 2
1 1
p(x;µ,⌃)= exp (x µ) ⌃ 1(x µ)
>  
(2⇡)ddet(⌃)  2    
✓ ◆
Note that in the special case d=p1, the density is written in the more recognizable form
1 (x µ)2
p(x;µ, 2)= exp  
p2⇡ 2   2 2 !
We write X (µ,⌃) to denote that X is normally distributed with mean µ and variance ⌃.
⇠N
5.9.1 The geometry of multivariate Gaussians
The geometry of the multivariate Gaussian density is intimately related to the geometry of positive
definitequadraticforms,somakesurethematerialinthatsectioniswell-understoodbeforetackling
this section.
First observe that the p.d.f. of the multivariate Gaussian can be rewritten as
p(x;µ,⌃)=g(x˜ ⌃ 1x˜)
>  
45

where x˜ = x   µ and g(z) = [(2⇡)ddet(⌃)]   1 2 exp   z 2 . Writing the density in this way, we see
thataftershiftingbythemeanµ,thedensityisreallyjustasimplefunctionofitsprecisionmatrix’s
   
quadratic form.
Here is a key observation: this function g is strictly monotonically decreasing in its argument.
Thatis,g(a)>g(b)whenevera<b. Therefore,smallvaluesofx˜ ⌃ 1x˜ (whichgenerallycorrespond
>  
topointswherex˜ iscloserto0,i.e. x µ)haverelativelyhighprobabilitydensities,andvice-versa.
⇡
Furthermore, because g is strictly monotonic, it is injective, so the c-isocontours of p(x;µ,⌃) are
the g 1(c)-isocontours of the function x x˜ ⌃ 1x˜. That is, for any c,
  >  
7!
x R d :p(x;µ,⌃)=c = x R d :x˜ > ⌃   1x˜ =g   1(c)
{ 2 } { 2 }
In words, these functions have the same isocontours but di↵erent isovalues.
Recall the executive summary of the geometry of positive definite quadratic forms: the isocontours
of f(x) = x Ax are ellipsoids such that the axes point in the directions of the eigenvectors of
>
A, and the lengths of these axes are proportional to the inverse square roots of the corresponding
eigenvalues. Therefore in this case, the isocontours of the density are ellipsoids (centered at µ) with
axis lengths proportional to the inverse square roots of the eigenvalues of ⌃ 1, or equivalently, the
 
square roots of the eigenvalues of ⌃.
46

Acknowledgements
The author would like to thank Michael Franco for suggested clarifications, and Chinmoy Saayujya
for catching a typo.
References
[1] J. Nocedal and S. J. Wright, Numerical Optimization. New York: Springer Science+Business
Media, 2006.
[2] J.S.Rosenthal,AFirstLookatRigorousProbabilityTheory(SecondEdition). Singapore: World
Scientific Publishing, 2006.
[3] J. Pitman, Probability. New York: Springer-Verlag, 1993.
[4] S. Axler, Linear Algebra Done Right (Third Edition). Springer International Publishing, 2015.
[5] S. Boyd and L. Vandenberghe, Convex Optimization. New York: Cambridge University Press,
2009.
[6] J. A. Rice, Mathematical Statistics and Data Analysis. Belmont, California: Thomson
Brooks/Cole, 2007.
[7] W. Cheney, Analysis for Applied Mathematics. New York: Springer Science+Business Medias,
2001.
47
