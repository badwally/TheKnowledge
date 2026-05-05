---
id: pdf-6b4cdd6cf0b7
type: pdf
title: FallbackPDF__6b4cdd6c
url: ''
authors: []
ingested_at: '2026-04-29T16:15:58Z'
content_hash: sha256:59aceb5de052ae1e9686c345b74d5ad70780c0073e3317ebb45865d9d490cb57
source_path: raw/pdf/pdf-6b4cdd6cf0b7.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 116
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__6b4cdd6c.pdf
published_at: '2025'
---
Mathematical Reasoning & Proofs
MAT 1362
Fall 2021
Alistair Savage
Department of Mathematics and Statistics
University of Ottawa
This work is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License

Contents
Preface 4
1 Integers 5
1.1 Axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.2 First consequences of the axioms . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3 Subtraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2 Natural numbers and induction 15
2.1 Natural numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2 Ordering the integers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.3 Induction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.4 The well-ordering principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3 Logic 27
3.1 Quantifiers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2 Implications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.3 Negations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4 Finite series and strong induction 34
4.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.2 Finite series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.3 The Binomial Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.4 Strong induction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5 Naive set theory 46
5.1 Subsets and equality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.2 Intersections and unions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
5.3 Cartesian products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
5.4 Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.5 Russell’s paradox and axiomatic set theory . . . . . . . . . . . . . . . . . . . 55
6 Equivalence relations and modular arithmetic 57
6.1 Equivalence relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6.2 The division algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
6.3 The integers modulo n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
6.4 Prime numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
2

Contents 3
7 Real numbers 73
7.1 Axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
7.2 Positive real numbers and ordering . . . . . . . . . . . . . . . . . . . . . . . 76
7.3 The real numbers versus the integers . . . . . . . . . . . . . . . . . . . . . . 79
7.4 Upper and lower bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
8 Injections, surjections, and bijections 87
8.1 Injections, surjections, and bijections . . . . . . . . . . . . . . . . . . . . . . 87
8.2 Embedding Z in R . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
9 Limits 95
9.1 Unboundedness of the integers . . . . . . . . . . . . . . . . . . . . . . . . . . 95
9.2 Absolute value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
9.3 Distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
9.4 Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
9.5 Square roots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
10 Rational and irrational numbers 109
10.1 Rational numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
10.2 Irrational numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
Index 113

Preface
These are notes for the course Mathematical Reasoning & Proofs at the University of Ot-
tawa. This is an introduction to rigorous mathematical reasoning and the concept of proof
in mathematics. It is a course designed to prepare students for upper-level proof-based
mathematics courses. We will discuss the axiomatic method and various methods of proof
(proof by contradiction, mathematical induction, etc.). We do this in the context of some
fundamental notions in mathematics that are crucial for upper-level mathematics courses.
These include the basics of naive set theory, functions, and relations. We will also discuss, in
a precise manner, the integers, integers modulo n, rational numbers, and real numbers. In
addition, we will discuss concepts related to the real line, such as completeness, supremum,
and the precise definition of a limit. In general, this course is designed to provide students
with a solid theoretical foundation upon which to build in subsequent courses.
This course should be of interest to students who feel dissatisfied with mathematics
courses in which computation is emphasized over proof and explanation. In MAT 1362,
we will rarely perform computations based on standard techniques and algorithms, such as
computing derivatives using the chain and product rules. Instead, we will focus on why
certain mathematical statements are true and why given techniques work. This is often
much more di!cult than following an algorithm to perform a computation. However, it is
much more rewarding and results in a deeper understanding of the material.
Acknowledgement: Significant portions of these notes closely follow the book The Art of
Proof by Matthias Beck and Ross Geoghegan [BG10], which is the o!cial course text.
Alistair Savage
Course website: https://alistairsavage.ca/mat1362
4

Chapter 1
Integers
In this chapter we discuss the integers. While you have encountered the integers in many
previous courses, dating back to grade school, you probably took certain properties for
granted. In this course, we will begin with some precise axioms and deduce other properties
of the integers in a more rigorous way.
1.1 Axioms
We will discuss the concept of a set later, in Chapter 5. For now, we will use the word
intuitively. A set S is a collections of things, called the elements or members of S. We write
a S to indicate that a is an element of S. A binary operation on a set S is a function that
→
takes two elements of S as input and produces another element of S as output.
We will assume there is a set Z, whose members we will call integers. This set comes
with two binary operations:
• addition, denoted +, and
• multiplication, denoted .
·
We will often denote multiplication by juxtaposition. That is, we will write ab instead of
a b.
·
We assume that Z, together with these operations, satisfies the following five axioms, as
well as Axioms 2.1 and 2.17 to be introduced in Chapter 2.
Axiom 1.1 (Commutativity, associativity, and distributivity). For all integers a, b, and c,
we have
(i) a+b = b+a, (commutativity of addition)
(ii) (a+b)+c = a+(b+c), (associativity of addition)
(iii) a (b+c) = a b+a c, (distributivity)
· · ·
(iv) a b = b a, (commutativity of multiplication)
· ·
(v) (a b) c = a (b c). (associativity of multiplication)
· · · ·
5

6 Integers
Axiom 1.2 (Additive identity). There exists an integer 0 such that a+0 = a for all a Z.
→
This element 0 is called an additive identity, or an identity element for addition.
Axiom 1.3 (Multiplicative identity). There exists an integer 1 such that 1 = 0 and a 1 = a
↑ ·
for all a Z. The element 1 is called a multiplicative identity, or an identity element for
→
multiplication.
Axiom 1.4 (Additive inverse). For each a Z, there exists an integer, denoted a, such
→ ↓
that a+( a) = 0. The element a is called the additive inverse of a.
↓ ↓
Axiom 1.5 (Cancellation). If a,b,c Z, a b = a c, and a = 0, then b = c. This is called
→ · · ↑
the cancellation property.
The symbol “=” means equals. When we write a = b for elements a and b of some set
S (e.g. Z), we mean that a and b are the same element. This symbol has the following
properties:
(i) a = a. (reflexivity of equality)
(ii) If a = b, then b = a. (symmetry of equality)
(iii) If a = b and b = c, then a = c. (transitivity of equality)
(iv) If a = b, then a can be replaced by b in any statement or expression, without changing
the meaning of that statement or expression. (In fact, the statement/expression is
unchanged.) We call this the replacement property. For example, if a,b,c Z and
→
a = b, then a+c = b+c.
The symbol = means is not equal to. When we write a = b for a,b Z, we mean that a
↑ ↑ →
and b are not the same element of Z. Note the following:
(i) The symbol = is not reflexive. We never have a = a.
↑ ↑
(ii) The symbol = is symmetric. If a,b Z and a = b, then b = a.
↑ → ↑ ↑
(iii) The symbol = is not transitive. For example, 1 = 2 and 2 = 1, but it is not true that
↑ ↑ ↑
1 = 1 (which is what transitivity would imply).
↑
The symbol means is not an element of.
↑→
1.2 First consequences of the axioms
For now, we only assume Axioms 1.1–1.5. That is, we will not use any other properties of
the integers that you may have learned in previous courses in mathematics. We will deduce
other properties of the integers from these axioms. Once we have proved that some other
statement is true, we may then use it in following statements. In general, we would like
to assume as few axioms as possible, and show that other properties are implied by this
small list of axioms. Note, for example, that we have not yet introduced the operation of
subtraction. (We will see this in Section 1.3.)

First consequences of the axioms 7
Proposition 1.6. If a,b,c Z, then (a+b)c = ac+bc.
→
Proof. Suppose a,b,c Z. Then we have
→
(a+b)c = c(a+b) Axiom 1.1(iv) (commutativity of multiplication)
= ca+cb Axiom 1.1(iii) (distributivity)
= ac+bc. Axiom 1.1(iv) (commutativity of multiplication)
Proposition 1.7. If a Z, then 0+a = a and 1 a = a.
→ ·
Proof. This proof of this proposition is left as an exercise (Exercise 1.2.1).
Proposition 1.8. If a Z, then ( a)+a = 0.
→ ↓
Proof. The proof of this proposition is left as an exercise (Exercise 1.2.2).
Proposition 1.9. If a,b,c Z and a+b = a+c, then b = c.
→
Proof. Suppose a,b,c Z. Then we have
→
a+b = a+c
= ( a)+(a+b) = ( a)+(a+c) replacement property
↔ ↓ ↓
= (( a)+a)+b = (( a)+a)+c Axiom 1.1(ii) (associativity of addition)
↔ ↓ ↓
= 0+b = 0+c Proposition 1.8
↔
= b = c. Proposition 1.7
↔
Above, we have used the symbol = . If P and Q are two statements, then P = Q
↔ ↔
meansthatthestatementP implies thestatementQor, equivalently, thatQfollowslogically
from P. It can also be read “if P, then Q”.
Proposition 1.10 (Uniqueness of the additive inverse). If a,b Z and a + b = 0, then
→
b = a. In other words, the element a mentioned in Axiom 1.4 is the unique additive
↓ ↓
inverse of a (i.e. every integer has exactly one additive inverse).
Proof. Suppose a,b Z. Then we have
→
a+b = 0
= ( a)+(a+b) = ( a)+0 replacement property
↔ ↓ ↓
= ( a)+(a+b) = a Axiom 1.2 (add. ident.)
↔ ↓ ↓
= (( a)+a)+b = a Axiom 1.1(ii) (assoc. of add.)
↔ ↓ ↓
= 0+b = a Proposition 1.8
↔ ↓
= b = a. Proposition 1.7
↔ ↓

8 Integers
Proposition 1.10 is a good example of how we have tried to make the axioms as weak as
possible. We could have worded Axiom 1.4 to say that every integer has a unique additive
inverse. However, Proposition 1.10 shows that it is enough to state the weaker axiom that
every integer has at least one additive inverse. The uniqueness of the additive inverse follows
from the axioms.
Proposition 1.11. Suppose a,b,c,d Z. Then
→
(i) (a+b)(c+d) = (ac+bc)+(ad+bd),
(ii) a+(b+(c+d)) = (a+b)+(c+d) = ((a+b)+c)+d,
(iii) a+(b+c) = (c+a)+b,
(iv) a(bc) = c(ab),
(v) a(b+(c+d)) = (ab+ac)+ad,
(vi) (a(b+c))d = (ab)d+a(cd).
Proof. We will prove part (v) and leave the remaining parts as an exercise (Exercise 1.2.3).
Suppose a,b,c,d Z. Then we have
→
a(b+(c+d)) = ab+a(c+d) Axiom 1.1(iii) (distributivity)
= ab+(ac+ad) Axiom 1.1(iii) (distributivity)
= (ab+ac)+ad. Axiom 1.1(ii) (assoc. of addition)
Proposition 1.12 (Uniqueness of the additive identity). Suppose a Z. If a has the
→
property that b + a = b for all b Z, then a = 0. In other words, the additive identity is
→
unique.
Proof. Suppose a Z has the property that b+a = b for all b Z. In particular, choosing
→ →
b = 0, we have
0+a = 0
= a = 0. Proposition 1.7
↔
Proposition 1.13. Suppose a Z. If a has the property that b + a = b for some b Z,
→ →
then a = 0.
Proof. Suppose a Z has the property that b+a = b for some b Z. By Axiom 1.4, b has
→ →
an additive inverse b Z. Then
↓ →
b+a = b
= ( b)+(b+a) = ( b)+b replacement property
↔ ↓ ↓

First consequences of the axioms 9
= (( b)+b)+a = ( b)+b Axiom 1.1(ii) (associativity of addition)
↔ ↓ ↓
= 0+a = 0 Proposition 1.8
↔
= a = 0. Proposition 1.7
↔
Note the di”erence between Propositions 1.12 and 1.13. In Proposition 1.12, the equation
b+a = b is assumed to hold for all b Z, whereas in Proposition 1.13, it is assumed to hold
→
only for some b Z.
→
Proposition 1.14. If a Z, then a 0 = 0 = 0 a.
→ · ·
Proof. We have
0 = 0+0 Axiom 1.2 (additive identity)
= a 0 = a (0+0) replacement
↔ · ·
= a 0 = a 0+a 0 Axiom 1.1(iii) (distributivity)
↔ · · ·
= a 0+ (a 0) = (a 0+a 0)+ (a 0) replacement
↔ · ↓ · · · ↓ ·
= a 0+! (a 0)" = a 0+ a 0+ ! (a 0)" Axiom 1.1(ii) (assoc. of addition)
↔ · ↓ · · · ↓ ·
! = 0" = a 0+0# ! " $ Axiom 1.4 (additive inverse)
↔ ·
= 0 = a 0 Axiom 1.2 (additive identity).
↔ ·
The equality 0 = 0 a then follows from Axiom 1.1(iv) (commutativity of multiplication).
·
If a,b Z, we say that a is divisible by b (or that b divides a) if there exists c Z such
→ →
that a = bc. We will write b a to indicate that a is divisible by b and b ⊋ a to indicate that a
|
is not divisible by b.
How can we define even integers? Well, as you learn in grade school, even integers are
integers that are divisible by 2. But what is 2? Neither our axioms nor anything we have
proved up to this point discusses the integer 2. However, we can define 2 to be the integer
1+1.
Proposition 1.15. If a and b are even integers, then a+b and ab are also even.
Proof. Suppose a and b are even integers. Then, by definition, there exist j,k Z such that
→
a = 2j and b = 2k. Thus
a+b = 2j +2k replacement property
= 2(j +k) Axiom 1.1(iii) (distributivity)
Since j +k Z, this implies that a+b is divisible by 2, hence is even.
→
We leave the proof that ab is even as an exercise (Exercise 1.2.4).
Proposition 1.16. (i) 0 is divisible by every integer.
(ii) If a Z and a = 0, then 0 ⊋ a.
→ ↑

10 Integers
Proof. (i) Suppose m Z. Then 0 = m 0 by Proposition 1.14. Thus, by the definition
→ ·
of divisibility, 0 is divisible by m.
(ii) Suppose a Z is divisible by 0. Then, by the definition of divisibility, there exists
→
k Z such that a = k 0. But k 0 = 0 by Proposition 1.14. So a = 0. So we have proved
→ · ·
that the only number divisible by zero is zero. It follows that, if a = 0, then 0 ⊋ a.
↑
Proposition 1.17 (Uniqueness of the multiplicative identity). If a Z has the property
→
that ba = b for all b Z, then a = 1.
→
Proof. The proof of this proposition is left as an exercise (Exercise 1.2.5).
Proposition 1.18. If a Z has the property that, for some nonzero b Z, ba = b, then
→ →
a = 1.
Proof. Suppose a Z has the given property. So there exists some nonzero b Z such that
→ →
ba = b. Then
ba = b
= b a = b 1 Axiom 1.3 (multiplicative identity)
↔ · ·
= a = 1. Axiom 1.5 (cancellation)
↔
Proposition 1.19. For all a,b Z, we have ( a)b = (ab).
→ ↓ ↓
Proof. Suppose a,b Z. Then
→
a+( a) = 0 Axiom 1.4 (additive inverse)
↓
= (a+( a))b = 0 b replacement property
↔ ↓ ·
= (a+( a))b = 0 Prop. 1.14
↔ ↓
= ab+( a)b = 0 Prop. 1.6
↔ ↓
= ( a)b = (ab). Prop. 1.10
↔ ↓ ↓
Proposition 1.20. (i) For all a Z, we have ( a) = a.
→ ↓ ↓
(ii) 0 = 0.
↓
Proof. (i) Suppose a Z. We have
→
( a)+ ( a) = 0 = ( a)+a Axiom 1.4 (additive inverse) and Prop. 1.8
↓ ↓ ↓ ↓
= ( a)+ ( a) = ( a)+a transitivity of equality
! "
↔ ↓ ↓ ↓ ↓
= ( a) = a. Prop. 1.9
! "
↔ ↓ ↓

First consequences of the axioms 11
(ii) We have
0+0 = 0 Axiom 1.2 (additive identity)
= 0 = 0. Proposition 1.10
↔ ↓
Proposition 1.21. For all a,b Z, we have ( a)( b) = ab. In particular, ( 1)( 1) = 1.
→ ↓ ↓ ↓ ↓
Proof. Suppose a,b Z. Then
→
( a)( b) = a( b) Prop 1.19
↓ ↓ ↓ ↓
= (( b)a) Axiom 1.1(iv) (commutativity of multiplication)
! "
↓ ↓
= ( (ba)) Prop. 1.19
↓ ↓
= ( (ab)) Axiom 1.1(iv) (commutativity of multiplication)
↓ ↓
= ab. Prop. 1.20(i)
Proposition 1.22. Suppose a,b Z. Then there exists a unique c Z such that a+c = b.
→ →
Note that Proposition 1.22 asserts that there is one and only one c with the given
property. Thus, this statement is asserting two things: that such an element c exists (the
existence part of the statement) and that any two elements with the given property must
be equal (the uniqueness part of the statement). Later, once we have discussed subtraction,
the element c in Proposition 1.22 will be denoted b a.
↓
Proof of Proposition 1.22. To prove the existence part of the statement, we just need to find
one element with the given property. In fact, ( a)+b is such an element, since
↓
a+ ( a)+b = a+( a) +b Axiom 1.1(ii) (associativity of addition)
↓ ↓
= 0+b Axiom 1.4 (additive inverse)
! " ! "
= b. Proposition 1.7
It remains to prove uniqueness. Suppose c and c are two elements with the given
1 2
property. Then we have
a+c = b = a+c
1 2
= a+c = a+c transitivity of equality
1 2
↔
= c = c . Proposition 1.9
1 2
↔
Proposition 1.23. If a Z satisfies a a = a, then a = 0 or a = 1.
→ ·
Proof. The proof of this proposition is left as an exercise (Exercise 1.2.6).

12 Integers
Warning! You cannot start a proof with the statement you are trying to prove. Doing so
results in circular reasoning, which is not valid. For example, in Proposition 1.23, you cannot
start with the statement a = 0 or a = 1. Instead, you must deduce the statement you are
trying to prove from statements you know to be true, or the hypotheses of the proposition.
To illustrate how starting with the statement you are trying to prove can result in nonsense,
consider the following invalid “argument”:
1 = 1
↓
= 1 1 = ( 1)( 1)
↔ · ↓ ↓
= 1 = 1.
↔
We ended up with a true statement, but that does not mean that our original statement is
true. Make sure you avoid this common pitfall.
Proposition 1.24. If a,b Z, then
→
(i) (a+b) = ( a)+( b),
↓ ↓ ↓
(ii) a = ( 1)a, and
↓ ↓
(iii) ( a)b = a( b) = (ab).
↓ ↓ ↓
Proof. The proof of this proposition is left as an exercise (Exercise 1.2.7). Note that some
of part (iii) was proved in Proposition 1.19.
Remark 1.25. In mathematics, the word “or”, without further qualification, is always inclu-
sive. For example, to say that “P or Q is true” means that P is true or Q is true or both P
and Q are true.
Proposition 1.26. If a,b Z satisfy ab = 0, then a = 0 or b = 0.
→
Proof. Suppose a,b Z satisfy ab = 0. Then
→
a b = 0 = a 0.
· ·
We split the proof into two cases: a = 0 and a = 0.
↑
Case 1: If a = 0, then the statement “a = 0 or b = 0” is true, and we are done.
Case 2: If a = 0, then, by Axiom 1.5, we can conclude that b = 0. Thus, the statement
↑
“a = 0 or b = 0” is again true.
Base ten numbers. So far the only specific integers with names are 0, 1, and 1. It is
↓
useful to have names for some more integers. We define the digits
2 := 1+1,
3 := 2+1,
.
.
.
9 := 8+1.
We can then define numbers write in base ten notation, e.g. 11 and 56, as you learn in
elementary school. This is discussed in detail in [BG10, Ch. 7], but we will omit such a
discussion in this course.

Subtraction 13
Powers. Fix an integer b. We define the powers bn for integers n 0 as follows:
↗
(i) We define b0 := 1.
(ii) For n > 0, we define bn = bb b.
···
nterms
Note that it follows from the ab%ov&e’ t(hat 00 = 1. We also have, for all a Z and integers
→
m,k 0,
↗
• amak = am+k.
• (am)k = amk.
Exercises.
1.2.1. Prove Proposition 1.7.
1.2.2. Prove Proposition 1.8.
1.2.3. Prove the remaining parts of Proposition 1.11.
1.2.4. Complete the proof of Proposition 1.15.
1.2.5. Prove Proposition 1.17.
1.2.6. Prove Proposition 1.23. Hint: Split the proof into two cases: a = 0 and a = 0.
↑
1.2.7. Prove Proposition 1.24.
1.3 Subtraction
Although you are all familiar with subtraction of integers, we have not encountered this
concept yet, since it is not mentioned in our axioms or in the results we have proven so far.
We can now define the concept of subtraction precisely.
Definition 1.27 (Subtraction). For a,b Z, we define a b to be a+( b). This new binary
→ ↓ ↓
operation will be called subtraction.
↓
Proposition 1.28. For all a,b,c,d Z, we have
→
(i) (a b)+(c d) = (a+c) (b+d),
↓ ↓ ↓
(ii) (a b) (c d) = (a+d) (b+c),
↓ ↓ ↓ ↓
(iii) (a b)(c d) = (ac+bd) (ad+bc),
↓ ↓ ↓

14 Integers
(iv) a b = c d if and only if a+d = b+c,
↓ ↓
(v) (a b)c = ac bc.
↓ ↓
Proof. The proof of part (i) can be found in [BG10, Prop. 1.27]. We will prove part (iii) and
leave the proofs of the other statements as an exercise (Exercise 1.3.1). We have
(a b)(c d) = a+( b) c+( d) def. of subtraction
↓ ↓ ↓ ↓
= ac+( b)c + a( d)+( b)( d) Prop. 1.11(i)
! "! "
↓ ↓ ↓ ↓
= ac+ ( b)c+a( d) +( b)( d) Prop. 1.11(ii)
! " ! "
↓ ↓ ↓ ↓
= ac+ ( b)c+a( d) +bd Prop. 1.21
! ! ""
↓ ↓
= bd+ ac+ ( b)c+a( d) Axiom 1.1(i) (comm. of add.)
! ! ""
↓ ↓
= (bd+ac)+ ( b)c+a( d) Prop. 1.11(ii)
! ! ""
↓ ↓
= (ac+bd)+ ( b)c+a( d) Axiom 1.1(i) (comm. of add.)
! "
↓ ↓
= (ac+bd)+ (bc)+( (ad)) Prop. 1.19
! "
↓ ↓
= (ac+bd)+ (bc+ad) by Prop. 1.24(i)
! "
↓
= (ac+bd) (bc+ad) def. of subtraction
! "
↓
= (ac+bd) (ad+bc). Axiom 1.1(i) (comm. of add.)
↓
As you can see, writing out some proofs in detail, citing all the appropriate axioms and
results, can become rather lengthy. As we begin to become familiar with the properties, we
will often omit straightforward steps, so that we can focus on the important new ideas in
a proof, instead of the small technical points that are similar to arguments we have done
before. But it is important to realize that one could fill in all the details, justifying every
step.
Remark 1.29. We have seen in this chapter that the arithmetic of integers, as defined by
our axioms, behave as we learned in grade school. From now on, we will start to use the
properties demonstrated in this chapter freely, often omitting some of the justifications. In
particular, asin Proposition1.11(ii), weseethatwecanmovetheparenthesesin theaddition
of multiple integers however we like, leaving the result unchanged. Therefore, if a,b,c,d Z,
→
we can unambiguously write expressions like
a+b+c+d,
since the result of the additions is the same no matter how we group the terms.
Exercises.
1.3.1. Prove the remaining parts of Proposition 1.28.

Chapter 2
Natural numbers and induction
In this section we introduce the natural numbers and an ordering on the integers. We then
see the important principles of mathematical induction and well-ordering.
2.1 Natural numbers
In Chapter 1, we introduced the integers. However, you may notice that none of our axioms
or results so far have referred to positive or negative numbers, nor to the relations “greater
than” or “less than”. We introduce another axiom to deal with these notions.
Axiom 2.1 (Natural numbers). There exists a subset N of Z with the following properties:
(i) If a,b N, then a+b N. (The subset N is closed under addition.)
→ →
(ii) If a,b N, then ab N. (The subset N is closed under multiplication.)
→ →
(iii) 0 N.
↑→
(iv) For every a Z, we have a N or a = 0 or a N.
→ → ↓ →
We call the members of N natural numbers or positive integers. A negative integer is an
integer that is not positive and not zero.
Remark 2.2. It is important to note that some references use the symbol N to denote a
slightly di”erent subset of Z than the one introduced above. Namely, they include 0 in the
set of natural numbers. Keep this in mind when reading other sources, to avoid confusion.
The proof of our next proposition will involve proof by contradiction. This technique
works as follows. Suppose we want to show that some statement P is true. Instead of
showing this directly, we can show that the assumption that P is false leads to a logical
contradiction (such as 1 = 0). We implicitly use the Law of the Excluded Middle, which says
that P must be either true or false. Thus, if its being false leads to a contradiction, it must
be true.
Proposition 2.3. For a Z, one and only one of the following statements is true:
→
15

16 Natural numbers and induction
• a N,
→
• a N,
↓ →
• a = 0.
Proof. Suppose a Z. By Axiom 2.1(iv), at least one of the statements in the proposition
→
is true. So it remains to prove that at most one is true.
First suppose a = 0. Then, by Proposition 1.20(ii), we have a = 0 = 0. Therefore,
↓ ↓
by Axiom 2.1(iii), a N and a N.
↑→ ↓ ↑→
It remains to prove that, if a = 0, then a and a cannot both be in N. We prove this by
↑ ↓
contradiction. Therefore, we assume that the statement
a and a are not both in N (2.1)
↓
is false. This is equivalent to assuming that the statement
a N and a N (2.2)
→ ↓ →
is true. Assuming this, Axiom 2.1(i), tells us that
a+( a) N.
↓ →
However, by Axiom 1.4, we have a + ( a) = 0. Therefore, 0 N. But this contradicts
↓ →
Axiom 2.1(iii). Therefore, our assumption (2.2) must be false. Consequently, the statement
(2.1) must be true, as desired.
Proposition 2.4. We have 1 N.
→
Proof. Since 1 = 0 (by the multiplicative identity axiom, Axiom 1.3), one and only one
↑
of 1 N and 1 N is true by Proposition 2.3. If 1 N, then by the closure of N
→ ↓ → ↓ →
under multiplication (Axiom 2.1(ii)), we have 1 = ( 1)( 1) N, which would contradict
↓ ↓ →
Proposition 2.3. Thus 1 N.
→
2.2 Ordering the integers
Now that we have introduced the natural numbers N, we are able to introduce an order on
the integers.
Definition 2.5 (Order on the integers). For a,b Z, we write a < b (and say a is less than
→
b) or b > a (and say b is greater than a) if and only if
b a N.
↓ →
We write a b (and say a is less than or equal to b) or b a (and say b is greater than or
↘ ↗
equal to a) if and only if
a < b or a = b.

Ordering the integers 17
Proposition 2.6 (Transitivity of <). Suppose a,b,c Z. If a < b and b < c, then a < c.
→
In other words, the relation < is transitive.
Proof. Assume a,b,c Z such that a < b and b < c. Thus, by definition, we have b a N
→ ↓ →
and c b N. Then, by Axiom 2.1(i)
↓ →
c a = (c b)+(b a) N.
↓ ↓ ↓ →
Thus, a < c.
Proposition 2.7 (N has no largest element). For each a N, there exists b N such that
→ →
b > a.
Proof. The proof of this proposition is left as an exercise (Exercise 2.2.1).
Proposition 2.8. If a,b Z satisfy a b a, then a = b.
→ ↘ ↘
Proof. Suppose a,b Z satisfy a b a. Suppose, towards a contradiction, that a = b.
→ ↘ ↘ ↑
Then a < b < a. By definition, this means that
b a N and a b N.
↓ → ↓ →
Then, by Axiom 2.1(i),
0 = (a b)+(b a) N.
↓ ↓ →
This contradicts Axiom 2.1(iii). Since the assumption a = b leads to a contradiction, we
↑
must have a = b.
Proposition 2.9. Suppose a,b,c,d Z.
→
(i) If a < b, then a+c < b+c.
(ii) If a < b and c < d, then a+c < b+d.
(iii) If 0 < a < b and 0 < c d, then ac < bd.
↘
(iv) If a < b and c < 0, then bc < ac.
Proof. The proof of part (iii) can be found in [BG10, Prop. 2.7]. We will prove part (iv) and
leave the proofs of the other parts as an exercise (Exercise 2.2.2).
Suppose a,b,c Z satisfy a < b and c < 0. So b a N and
→ ↓ →
c = 0+( c) = 0 c N.
↓ ↓ ↓ →
Thus, by Axiom 2.1(ii),
(b a)( c) N.
↓ ↓ →
Now,
(b a)( c) = b( c) a( c) = ac bc.
↓ ↓ ↓ ↓ ↓ ↓
Therefore ac bc N, and so bc < ac.
↓ →

18 Natural numbers and induction
Proposition 2.10. If a,b Z, then exactly one of the following statements in true:
→
• a < b,
• a = b,
• a > b.
Proof. The proof of this proposition is left as an exercise (Exercise 2.2.3).
Proposition 2.11. If a Z and a = 0, then a2 N. (Here a2 means a a.)
→ ↑ → ·
Proof. Suppose a Z and a = 0. By Axiom 2.1(iv), either a N or a N.
→ ↑ → ↓ →
Case 1: Suppose a N. Then a2 N by Axiom 2.1(ii).
→ →
Case 2: Suppose a N. Then
↓ →
a2 = a a = ( a)( a) N
· ↓ ↓ →
by Proposition 1.21 and Axiom 2.1(ii).
Proposition 2.12. There is no a Z satisfying a2 = 1.
→ ↓
Proof. We will prove this by contradiction. Suppose there is an a Z such that a2 = 1.
→ ↓
We split the proof into two cases:
Case 1: a = 0. Then a2 = 0 0 = 0, and so 0 = 1. Adding 1 to both sides gives 1 = 0,
· ↓
which contradicts Axiom 1.3.
Case 2: a = 0. In this case, Proposition 2.11 implies that 1 = a2 N. By Proposi-
↑ ↓ →
tion 2.4, we also have 1 N. This contradicts Proposition 2.3.
→
In both cases, we arrived at a contradiction. This completes the proof by contradiction.
Proposition 2.13. If a N and b Z satisfy ab N, then b N.
→ → → →
Proof. The proof of this proposition is left as an exercise (Exercise 2.2.4).
Proposition 2.14. Suppose a,b,c,d Z.
→
(i) a < b if and only if a > b.
↓ ↓
(ii) If c > 0 and ac < bc, then a < b.
(iii) If c < 0 and ac < bc, then b < a.
(iv) If a b and 0 c, then ac bc.
↘ ↘ ↘

Ordering the integers 19
Proof. We prove part (iv) and leave the other parts as exercises (Exercise 2.2.5). Assume
a b and 0 c. We split the proof into three cases.
↘ ↘
Case 1: c = 0. Then ac = 0 and bc = 0. So ac bc is true since 0 0.
↘ ↘
Case 2: c > 0 and a = b. Then ac = bc and so ac bc is true.
↘
Case 3: c > 0 and a < b. Then we have c N and b a N. Therefore,
→ ↓ →
bc ac = (b a)c N,
↓ ↓ →
by the closure of N under multiplication (Axiom 2.1(ii)). Therefore, ac bc.
↘
If A and B are sets, we will write A B to mean that A is a subset of B. In other words
≃
A B means that
≃
x A = x B.
→ ↔ →
Two sets are equal, written A = B, if
A B and B A.
≃ ≃
If other words, A = B means that
x A x B.
→ ⇐↔ →
(If P and Q are statements, then “P Q” means “P = Q and Q = P”.) We
⇐↔ ↔ ↔
write A ⫅̸ B if
A B and A = B.
≃ ↑
Note that this is di!erent than the symbol which means “is not a subset of”. Thus A B
↑≃ ↑≃
if and only if there is at least one element of A that is not an element of B.
It is best to avoid the symbol because of its ambiguity. Some authors use to mean
⇒ ⇒
and others use it to mean ⫅̸.
≃
We will use the notation
n Z : some property of n
{ → }
to denote the set of integers satisfying a given property. For example n Z : n > 3 is the
{ → }
set of all integers greater than 3. We will discuss sets in more detail later, in Chapter 5.
Proposition 2.15. We have N = n Z : n > 0 .
{ → }
Proof. We have
a n Z : n > 0 a Z and a > 0
→{ → }⇐↔ →
a Z and a = a 0 N
⇐↔ → ↓ →
a N.
⇐↔ →

20 Natural numbers and induction
Exercises.
2.2.1. Prove Proposition 2.7.
2.2.2. Prove the remaining parts of Proposition 2.9.
2.2.3. Prove Proposition 2.10.
2.2.4. Prove Proposition 2.13. Hint: Consider three cases: b < 0, b = 0, and b > 0.
2.2.5. Prove the remaining parts of Proposition 2.14.
2.2.6. Prove that if a,b,c Z satisfy a b and b c, then a c. (In other words, the
→ ↘ ↘ ↘
relation is transitive. Note that it follows from this that is also transitive.)
↘ ↗
2.3 Induction
In this section we introduce an important method of proof: mathematical induction. This
method is based on the natural numbers, and we need one further axiom before discussing
induction. Before stating this axiom, we begin with a proposition.
Proposition 2.16. (i) 1 N.
→
(ii) n N = n+1 N.
→ ↔ →
Proof. Part (i) was already proved in Proposition 2.4. Then part (ii) follows from Ax-
iom 2.1(i).
The new axiom states that N is the smallest subset of Z satisfying Proposition 2.16.
Axiom 2.17 (Induction Axiom). Suppose a subset A Z satisfies the following properties:
≃
(i) 1 A,
→
(ii) n A = n+1 A.
→ ↔ →
Then N A.
≃
Proposition 2.18. Suppose B N satisfies:
≃
(i) 1 B,
→
(ii) n B = n+1 B.
→ ↔ →
Then B = N.
Proof. By hypothesis, B N. By Axiom 2.17, N B. Thus B = N.
≃ ≃
Proposition 2.18 is the basis of the principle of induction.

Induction 21
Theorem 2.19 (Principle of mathematical induction: first form). Suppose that, for each
k N, we have a statement P(k). Furthermore, suppose that
→
(i) P(1) is true, and
(ii) for all n N, P(n) = P(n+1).
→ ↔
Then P(k) is true for all k N.
→
Proof. Assume that (i) and (ii) are true. Let
B := k N : P(k) is true .
{ → }
Then 1 B by (i) and n B = n + 1 B by (ii). Therefore, by Proposition 2.18,
→ → ↔ →
B = N. In other words, P(k) is true for all k N.
→
Proofs that use Theorem 2.19 are called proofs by induction. In proofs by induction,
statement (i) is often called the base case and statement (ii) is often called the induction
step. While proving the induction step, we typically assume P(n) is true and then show
that P(n+1) follows from this assumption. When doing this, P(n) is called the induction
hypothesis.
Example 2.20. We will prove by induction that 11n 6 is divisible by 5 for every n N. Let
↓ →
P(k) be the statement
11k 6 is divisible by 5.
↓
Base case: P(1) is the statement that 111 6 is divisible by 5. Since 111 6 = 5, this is
↓ ↓
clearly true.
Induction step: Suppose that P(n) is true for some n N. Thus, 11n 6 is divisible by 5.
→ ↓
Therefore, there exists m Z such that
→
11n 6 = 5m.
↓
We want to show that P(n+1) is true, that is, 11n+1 6 is divisible by 5. We have
↓
11n+1 6 = 11 11n 6
↓ · ↓
= 11(5m+6) 6 (by the induction hypothesis)
↓
= 55m+66 6
↓
= 55m+60
= 5(11m+12).
Thus, 11n+1 6 is divisible by 5. In other words P(n+1) is true. This completes our proof
↓
of the induction step.
Proposition 2.21. For all a N, we have a 1.
→ ↗

22 Natural numbers and induction
Proof. We prove the result by induction on a. Let P(a) be the statement
a 1.
↗
Base case: The base case P(1) is true because 1 1.
↗
Induction step: Suppose that, for some m N, the statement P(m) is true; so m 1. Since
→ ↗
(m+1) m = 1 N,
↓ →
we have m + 1 > m, and so m + 1 m 1. Thus m + 1 1 by transitivity of (see
↗ ↗ ↗ ↗
Exercise 2.2.6). So P(m+1) is true, completing the proof of the inductive step.
Proposition 2.22. There is no integer a satisfying 0 < a < 1.
Proof. Suppose, towards a contradiction, that there is an integer a satisfying 0 < a < 1.
Since a > 0, we have a N. Thus, by Proposition 2.21, we have a 1. Since a < 1 implies
→ ↗
that a 1, we have
↘
1 a 1.
↘ ↘
Therefore, by Proposition 2.8, we have a = 1. Since a < 1, we obtain the inequality 1 < 1,
which means that 0 = 1 1 N. This contradicts Axiom 2.1(iii). Therefore, our original
↓ →
assumption is false. Thus, there is no integer a satisfying 0 < a < 1.
Corollary 2.23. Suppose b Z. There is no integer a satisfying b < a < b+1.
→
Proof. The proof of this corollary is left as an exercise (Exercise 2.3.2).
Proposition 2.24. Suppose a,b N. If b a, then b a.
→ | ↘
Proof. We prove the result by contradiction. Suppose a,b N, b a, and b > a. By the
→ |
definition of divisibility, there exists some c Z such that a = bc. Then the inequality b > a
→
is equivalent to b > bc. By Proposition 2.14(ii), we have 1 > c. Then Proposition 2.22 and
Proposition 2.10 imply that c 0.
↘
Case 1: c = 0. In this case, we have a = b 0 = 0, which contradicts the fact that a N
· →
(by Axiom 2.1(iii)).
Case 2: c < 0. In this case c = 0 c N. Thus
↓ ↓ →
a = (bc) = b( c) N,
↓ ↓ ↓ →
which contradicts the fact that a N (by Proposition 2.3).
→
In either case we arrive at a contradiction, and so our proof is complete.
Example 2.25. Let us prove that 8n 3n is divisible by 5 for all n N. We will prove this
↓ →
by induction. Let
P(n) be the statement “8n 3n is divisible by 5”.
↓
Since 81 31 = 8 3 = 5 = 5 1, we see that P(1) is true.
↓ ↓ ·

Induction 23
Now assume that P(n) is true for some n N. So there exists m Z such that
→ →
8n 3n = 5m. Then
↓
8n+1 3n+1 = 8n+1 3 8n +3 8n 3n+1
↓ ↓ · · ↓
= 8 8n 3 8n +3 8n 3 3n
· ↓ · · ↓ ·
= (8 3) 8n +3 (8n 3n)
↓ · · ↓
= 5 8n +15m
·
= 5 (8n +3m).
·
Since 8n +3m Z, we see that 5 divides 8n+1 3n+1.
→ ↓
Sometimes we wish to start an induction at an integer other than 1.
Theorem 2.26 (Principle of mathematical induction: first form revisited). Suppose m is a
fixed integer and that, for each k Z with k m, we have a statement P(k). Furthermore,
→ ↗
suppose that
(i) P(m) is true, and
(ii) for all n m, P(n) = P(n+1).
↗ ↔
Then P(k) is true for all k m.
↗
Proof. If we set Q(k) = P(k + m 1) for all k N, then this theorem is reduced to
↓ →
Theorem 2.19. See [BG10, Th. 2.25] for details.
Example 2.27. We will prove that
3k2 +15k +19 0 for all integers k 2.
↗ ↗ ↓
Base case: When k = 2, we have 3( 2)2 +15( 2)+19 = 12 30+19 = 1 0. So the
↓ ↓ ↓ ↓ ↗
statement is true for k = 2.
↓
Induction step: Suppose the statement is true for some k 2. Then
↗ ↓
3(k +1)2 +15(k +1)+19 = 3(k2 +2k +1)+15k +15+19
= 3k2 +21k +37
= (3k2 +15k +19)+(6k +18)
0+6k +18 = 6k +18.
↗
Now, we have
k 2 = 6k 12 (by Prop. 2.14(iv))
↗ ↓ ↔ ↗ ↓
= 6k +18 6 0 (by Prop. 2.9(i)).
↔ ↗ ↗
Thus
3(k +1)2 +15(k +1)+19 0,
↗
which completes the induction step.

24 Natural numbers and induction
Exercises.
2.3.1 ([BG10, Prop. 2.18]). Prove the following statements.
(i) For all k N, k3 +2k is divisible by 3.
→
(ii) For all k N, k4 6k3 +11k2 6k is divisible by 4.
→ ↓ ↓
(iii) For all k N, k3 +5k is divisible by 6.
→
2.3.2. Prove Corollary 2.23.
2.3.3 ([BG10, Prop. 2.27]). Prove that, for all integers k 2, we have k2 < k3.
↗
2.4 The well-ordering principle
Definition 2.28 (Smallest and greatest elements). Suppose A Z is nonempty. If there
≃
exists m A such that
→
m a for all a A,
↘ →
then we say m is a smallest element of A and write m = min(A). If there exists M A such
→
that
M a for all a A,
↗ →
then we say M is a greatest element of A and write M = max(A).
Proposition 2.29. Suppose A Z is nonempty.
≃
(i) If A has a smallest element, then this element is unique. In other words, A has at
most one smallest element.
(ii) If A has a greatest element, then this element is unique. In other words, A has at most
one greatest element.
Proof. Suppose a and b are both smallest elements of A. Then a b and b a. Thus,
↘ ↘
by Proposition 2.8, we have a = b. The proof of the second part of the proposition is
analogous.
Example 2.30. By Propositions 2.4 and 2.21, 1 is the smallest element of N. On the other
hand, by Proposition 2.7, N has no greatest element.
Example 2.31. The set of even integers has neither a smallest element nor a greatest element.
However, the set of negative even integers has greatest element 2, but no smallest element.
↓
Remark 2.32. We will always use the words positive and negative in the strict sense. So
a Z is positive if a > 0 and negative if a < 0. We say a Z is nonnegative if a 0.
→ → ↗

The well-ordering principle 25
Theorem 2.33 (Well-ordering principle). Every nonempty subset of N has a smallest ele-
ment.
Proof. Define the set
A := k N : every subset of N containing an integer k has a smallest element .
{ → ↘ }
If we prove that A = N, then we have proved the theorem. We will prove by induction that
A contains every natural number.
Base case: As seen in Example 2.30, 1 is a smallest element of N. Therefore, if any subset
of N contains 1, then 1 is its smallest element. Therefore, 1 A.
→
Induction step: Assume n A for some n N. Suppose that S N contains an integer
→ → ≃
n + 1. We want to prove that S has a smallest element. If S contains an integer n,
↘ ↘
then S has a smallest element by the induction hypothesis. Otherwise (i.e. when S does not
contain an integer n), S must contain n + 1 (by Corollary 2.23), and this integer is the
↘
smallest element of S.
Proposition 2.34. Suppose A is a nonempty subset of Z and b Z satisfies b a for all
→ ↘
a A. (We say that A is bounded below by b.) Then A has a smallest element.
→
Proof. Let A be a nonempty subset of Z and suppose b Z satisfies b a for all a A.
→ ↘ →
Define a new set by
B := a+1 b : a A .
{ ↓ → }
For all a A, we have b a, so b < a+1, and hence a+1 b N. Thus, B N. Since
→ ↘ ↓ → ≃
A is nonempty, so is B. Therefore, by the well-ordering principle (Theorem 2.33), B has a
smallest element c. Then, c = d + 1 b for some d A (by the definition of B). For all
↓ →
a A, we have
→
a+1 b B = a+1 b c = d+1 b = a d.
↓ → ↔ ↓ ↗ ↓ ↔ ↗
Thus d is a smallest element of A.
We will now use the well-ordering principle in a definition. First we need a proposition.
Proposition 2.35. Suppose a and b are integers that are not both 0. Then the set
S = k N : k = ax+by for some x,y Z
{ → → }
is nonempty.
Proof. The proof of this proposition is left as an exercise (Exercise 2.4.1).
Definition 2.36 (gcd). Suppose a,b Z. If a and b are not both zero, we define
→
gcd(a,b) = min k N : k = ax+by for some x,y Z .
{ → → }
(SincethissetisnonemptybyPr!oposition2.35, ithasaminimumelement"byTheorem2.33.)
If a = b = 0, we define gcd(0,0) = 0.
We will see later that gcd(a,b) is actually the greatest common divisor of a and b, justi-
fying the notation (see Proposition 6.29).

26 Natural numbers and induction
Exercises.
2.4.1. Prove Proposition 2.35.

Chapter 3
Logic
We have already used logical argument in Chapters 1 and 2. One of our goals there was to
introduceourselvestotheconceptofmathematicalproofbeforegettingintothetechnicalities
of logic. In the current chapter will examine some basic concepts of logic in more detail.
This will allow us to be more precise in our mathematical arguments.
3.1 Quantifiers
The symbol is called the existential quantifier. It means there exists or there exist. The
⇑
symbol is called the universal quantifier. It means for all or for each or for every or
⇓
whenever.
Examples 3.1. (i) “ m Z such that m > 5” means “there exists an element m Z such
⇑ → →
that m > 5”. (This statement is true.)
(ii) “ m Z, m < 5” means “for all m Z, we have m < 5”. (This statement is false.)
⇓ → →
(iii) Axiom 1.2 could be written: 0 Z such that a Z, a+0 = a.
⇑ → ⇓ →
(iv) Axiom 1.3 could be written: 1 Z such that (1 = 0 and a Z, a 1 = a).
⇑ → ↑ ⇓ → ·
Statements with quantifiers consist of quantified segments of the form ( ... such that)
⇑
and/or ( ...) in a certain order, and then a final statement or assertion. For instance, in
⇓
example (iii) above, we have
( 0 Z such that)( a Z) a+0 = a .
⇑ → ⇓ →
quantifiedsegments finalstatement
% &’ ( % &’ (
The order of quantifiers is very important. Consider the following statements:
(i) ( a Z)( b Z such that) a+b = 0
⇓ → ⇑ →
(ii) ( b Z such that)( a Z) a+b = 0
⇑ → ⇓ →
27

28 Logic
Statement (i) asserts that, for each integer a, there is an integer b Z, which could depend
→
on a, such that a+b = 0. This is true, since one can choose b = a. On the other hand,
↓
statement (ii) asserts that there is some integer b such that a+b = 0 for all integers a. This
is false, since there is no b that satisfies this condition for all a. So in statement (i), b may
depend on a, whereas in statement (ii) it may not.
The particular variable used in a quantified statement is not important. For example,
( a Z)( b Z such that) a+b = 0 ( m Z)( n Z such that) m+n = 0,
⇓ → ⇑ → ⇔ ⇓ → ⇑ →
where the symbol denotes logical equivalence.
⇔
One can combine several consecutive -phrases in a row. For example
⇓
( a Z)( b Z) has the same meaning as ( a,b Z).
⇓ → ⇓ → ⇓ →
Similarly, one can combine several -phrases:
⇑
( a N)( b N) has the same meaning as ( a,b N).
⇑ → ⇑ → ⇑ →
Examples 3.2. We can express many statements using quantifiers.
(i) “Every natural number is greater than 1” can be written as ( n N) n > 1.
↓ ⇓ → ↓
(ii) “Everyintegeristhesumoftwointegers”canbewrittenas( a Z)( b,c Z such that)b+
⇓ → ⇑ →
c = a.
(iii) “There exists a smallest natural number” can be written as ( n N such that)( m
⇑ → ⇓ →
N) n m.
↘
Examples 3.3. (i) The statement “( x Z)( y N such that ) x < y” is true.
⇓ → ⇑ →
(ii) The statement “( y N such that )( x Z) x < y” is false.
⇑ → ⇓ →
(iii) The statement “( x Z) x2 0” is true.
⇓ → ↗
For all statements can often be rewritten as if then statements. For example
( x Z) x2 0 is equivalent to if x Z, then x2 0.
⇓ → ↗ → ↗
The symbol ⫆̸ means there does not exist. For example, the statement
(⫆̸a N such that)( b N) a > b
→ ⇓ →
means that there is no natural number that is greater than all other natural numbers.
Uniqueness. The symbol ! means there exists a unique. For example, Axiom 1.4 and
⇑
Proposition 1.10 imply the statement
( a Z)( !b Z such that) a+b = 0.
⇓ → ⇑ →
A statement of the form ( !n N such that) is actually two statements:
⇑ →
• existence: ( n N such that), and
⇑ →
• uniqueness: (if n N and m N both have the given property, then n = m).
→ →

Implications 29
Exercises.
3.1.1. Express each of the following statements using quantifiers. (Note that we make no
claim as to the validity of these statements. We merely translate them.)
(i) There exists a largest integer.
(ii) There exists a smallest natural number.
(iii) Every integer is the sum of two integers.
(iv) Every integer is the square of an integer.
(v) The equation x2 +5y3 = 4 has a unique integer solution (i.e. it has one and only one
solution where x and y are integers).
3.1.2. For each of the following statements, decide whether it is true or false.
(i) ( x Z)( y Z such that) x+y = 2
⇓ → ⇑ →
(ii) ( x Z)( y N such that) x+y = 2
⇓ → ⇑ →
(iii) ( x Z such that)( y Z) x+y = 2
⇑ → ⇓ →
(iv) ( a Z such that)( b Z) a+b = b
⇑ → ⇓ →
(v) ( b Z)( a Z such that) a+b = b
⇓ → ⇑ →
3.2 Implications
The symbol = means implies. If P and Q are statements, then the following are equiva-
↔
lent:
• P = Q.
↔
• P implies Q.
• If P, then Q.
• (not P) or Q.
Remark 3.4. It is important to note that if P is a false statement, then the implication
P = Q is true. This follows from the fact, mentioned above, that “P = Q” is
↔ ↔
equivalent to “(not P) or Q”. For example, the statement
if 5 is an even number, then there is life on Mars
is true (regardless of whether or not there is life on Mars), since the statement “5 is an even
number” is false.

30 Logic
To see that the implication P = Q is equivalent to “(not P) or Q”, we can compare
↔
their truth tables.
P Q P = Q (not P) or Q
↔
true true true true
true false false false
false true true true
false false true true
The double implication symbol means if and only if. If P and Q are statements,
⇐↔
then the following are equivalent:
• P Q.
⇐↔
• P if and only if Q.
• (P = Q) and (Q = P).
↔ ↔
• Either P and Q are both false, or P are Q are both true.
• (P and Q) or ((not P) and (not Q)).
Examples 3.5. Suppose n is an integer.
(i) The statement (n is divisible by 2 n is even) is true.
⇐↔
(ii) The statement (n is divisible by 4 n is even) is false.
⇐↔
Converse. The converse of the implication P = Q is the implication Q = P.
↔ ↔
Important: An implication and its converse are not equivalent in general. It is possible for
one to be true, while the other is false. (It is also possible for both to be true or both to be
false.)
Example 3.6. The statement
n is divisible by 4 = n is even
↔
is true. However, its converse is
n is even = n is divisible by 4,
↔
which is false.

Negations 31
Contrapositive. The contrapositive of an implication P = Q is the implication (not
↔
Q) = (not P). An implication and its contrapositive are equivalent. That is
↔
P = Q is equivalent to (not Q) = (not P).
↔ ↔
Example 3.7. The statement
n is divisible by 4 = n is even
↔
is equivalent to its contrapositive
n is not even = n is not divisible by 4.
↔
Sometimes the easiest way to prove a statement is to prove its contrapositive.
Exercises.
3.2.1. Give two examples of true mathematical statements whose converses are false. (Do
not give examples that we have already seen.)
3.2.2. Try re-proving some of the if-then propositions in Chapters 1 and 2 by proving their
contrapositives.
3.3 Negations
If P is a statement, then its negation is the statement (not P). For example, the negation
of (n is even) is (n is not even). We will sometimes write P for “not P”.
¬
Negation of “and” and “or”. Negation interchanges “and” and “or” in the following
sense (sometimes called De Morgan’s laws):
• (P or Q) ( P and Q),
¬ ⇔ ¬ ¬
• (P and Q) ( P or Q).
¬ ⇔ ¬ ¬
Example 3.8. Suppose P is some property that an integer may possess. Then the statement
“ !n Z with property P” is equivalent to
⇑ →
( n Z with property P) and (there is at most one integer with property P).
⇑ →
Its negation is therefore
(there is no n Z with property P) or (there is more than one integer with property P).
→

32 Logic
Negation of an implication. Since the implication P = Q is equivalent to “ P or
↔ ¬
Q”, the negation of the implication P = Q is “P and Q”. In other words,
↔ ¬
(P = Q) ( P or Q) (P and Q).
¬ ↔ ⇔¬ ¬ ⇔ ¬
Negations involving quantifiers. Now suppose we want to find the negation of a state-
ment involving the quantifiers and . We write it in the form of quantified segments
⇓ ⇑
followed by a final statement. Then, to find the negation we do the following:
(i) We maintain the order of the quantified segments, but change every ( ...) segment
⇓
into a ( ... such that) segment.
⇑
(ii) Change each ( ... such that) segment into a ( ...) segment.
⇑ ⇓
(iii) Negate the final statement.
Example 3.9. Axiom 1.2 can be written as
( b Z such that)( a Z) a+b = a.
⇑ → ⇓ →
(We have replaced the quantified variable 0 by b, which does not change the meaning of the
implication.) Its negation is
( b Z)( a Z such that) a+b = a.
⇓ → ⇑ → ↑
Examples 3.10. (i) The negation of “every di”erentiable function is continuous” is “there
exists a di”erentiable function that is not continuous”.
(ii) The negation of “none of Paul’s Facebook posts are interesting” is “there exists a
Facebook post by Paul that is interesting”.
(iii) The negation of
( ω> 0) ( ε> 0 such that) ( x R) ( x a <ε = f(x) f(a) <ω )
⇓ ⇑ ⇓ → | ↓ | ↔| ↓ |
is
( ω> 0 such that) ( ε> 0) ( x R such that) ( x a <ε and f(x) f(a) ω).
⇑ ⇓ ⇑ → | ↓ | | ↓ |↗
(The first statement is the definition of continuity at the point a.)

Negations 33
Exercises.
3.3.1. Negate the following statements.
(i) Every polynomial has a real root.
(ii) Steve is blond and Samantha is tall.
(iii) x Z, !y Z such that xy = 3.
⇓ → ⇑ →
(iv) That cow is neither large nor pink.
(v) If f(x,y) > 0, then x > 0 or y 0.
↘
(vi) The quotient group G/N is finite if and only if G is finite.
(vii) For each L N, there exists N N such that x N > L.
→ →

Chapter 4
Finite series and strong induction
In this chapter we will introduce some common mathematical notions such as summation
notation, product notation, and factorials. We will then prove the important Binomial
Theorem and introduce a second form of mathematical induction.
4.1 Preliminaries
An (infinite) sequence is a list of integers x
j
for j N. We denote such a sequence by
→
(x
j
)
→j=1
. (Later we will see that a sequence is a function with domain N. See Example 5.21.)
It is possible that the indices (i.e. the subscripts) do not start at 1, but rather at some other
integer m. In that case, we write (x ) . A finite sequence (x )M is a list of numbers
j →j=m j j=m
x ,x ,x ,...,x ,x .
m m+1 m+2 M 1 M
↑
(Here m,M Z with m M.)
→ ↘
Example 4.1. If we define x = j2 5, then x = 4, x = 1, x = 4, etc. The number x
j 1 2 3 k
↓ ↓ ↓
is called the k-th term of the sequence.
Some sequences are defined recursively.
Example 4.2. Consider a sequence (x ) defined as follows.
j →j=1
(i) Define x = 1.
1
(ii) Assuming x is defined, define x = 2x 3.
n n+1 n
↓
Then, in this sequence, we have x = 1, x = 1, x = 5, x = 13, etc.
1 2 3 4
↓ ↓ ↓
Note that the sequence of Example 4.1 was defined directly. Given any k, we can imme-
diately compute x . On the other hand, the sequence of Example 4.2 was defined recursively.
k
In order to compute the k-th term, we must compute all the terms before it.
Example 4.3. Define a sequence (x ) recursively as follows:
n →n=1
x = 4,
1
↓
34

Preliminaries 35
x = 3x 8 for n 1.
n+1 n
↓ ↗
Let’s prove that x
n
is even for all n N.
→
Base case: When n = 1, we have x = 4 = 2( 2). So x is divisible by 2, hence is even.
1 1
↓ ↓
Induction step: Suppose x is even for some n 1. Thus, we have x = 2m for some
n n
↗
m Z. Then
→
x = 3x 8 = 3(2m) 8 = 2(3m 4).
n+1 n
↓ ↓ ↓
Since m Z, we have 3m 4 Z. Thus x
n+1
is divisible by 2, hence is even. This completes
→ ↓ →
the proof of the induction step.
Summation and product notation. If (x )n is a finite sequence of integers, we define
j j=m
n
x = x +x + +x ,
j m m+1 n
···
j=m
)
n
x = x x x .
j m m+1 n
···
j=m
*
(If m = n, we interpret these as m x = x and m x = x .)
j=m j m j=m j m
We let + ,
Z 0 := n Z : n 0
↓ { → ↗ }
denote the set of nonnegative integers..
Factorial. For n Z 0 we define n! (read “n factorial”) as follows:
→ ↓
(i) We define 0! := 1.
(ii) For n > 0, we define n! = n j = 1 2 n.
j=1 · ·····
,
Exercises.
4.1.1 ([BG10, Proj. 4.3]). Suppose m is a natural number. Define the following sequence:
(i) Define x = m.
1
(ii) Assuming x is defined, define
n
xn if x is even,
x = 2 n
n+1
-x
n
+1 otherwise.

36 Finite series and strong induction
Does this sequence eventually take on the value 1, no matter what value of m N was
→
chosen to start with? Try to prove your assertion.
4.1.2 ([BG10, Prop. 4.7]). Prove that, for all k N:
→
(i) 52k 1 is divisible by 24;
↓
(ii) 22k+1 +1 is divisible by 3;
(iii) 10k +3 4k+2 +5 is divisible by 9.
·
4.1.3 ([BG10, Prop. 4.8]). Prove that, for all k N, 4k > k.
→
4.1.4 ([BG10, Proj. 4.9]). Determine for which natural numbers k the inequality k2 < 2k
holds. Prove your answer.
4.1.5. Prove that 2n < n! for n 4.
↗
4.1.6. Define a sequence (x ) recursively as follows:
n →n=1
x = 12,
1
x = 2x +6 for n 1.
n+1 n
↗
Prove that x
n
is divisible by 3 for all n N.
→
4.1.7. Define a sequence (x ) recursively as follows:
n →n=1
x = 10,
1
x = x2 +3x 5 for n 1.
n+1 n n ↓ ↗
Prove that x
n
is divisible by 5 for all n N.
→
4.2 Finite series
We will now work out some examples of sums that can be explicitly computed, as well as
stating some useful properties of sums.
Recall that if a,b Z and a divides b, then there exists c Z such that ac = b. We
→ →
denote this c by b. Note that this implies that b is an integer and (for now) is only defined
a a
when a divides b. We have not yet introduced the concept of rational numbers.
Proposition 4.4. Suppose n N.
→
n
n(n+1)
(i) j = .
2
j=1
)
n
n(n+1)(2n+1)
(ii) j2 = .
6
j=1
)

Finite series 37
Proof. We will prove the first equality, and leave the second as an exercise. We prove the
first equality by induction on n. If n = 1, we have
1
1(1+1)
j = 1 = ,
2
j=1
)
which proves the base case.
Now assume the result is true for some n N. Then we have
→
n+1 n
j = j +(n+1)
. /
j=1 j=1
) )
n(n+1)
= +(n+1)
2
n(n+1)+2(n+1)
=
2
n2 +3n+2
=
2
(n+1)(n+2)
=
2
(n+1) (n+1)+1
= .
2
! "
This completes the proof of the induction step.
Proposition 4.5. For x Z with x = 1, and n Z 0 , we have
→ ↑ → ↓
n 1 xn+1
xj = ↓ .
1 x
j=0 ↓
)
Proof. Fix x Z, x = 1. We will prove that
→ ↑
k
(1 x) xj = 1 xk+1
↓ ↓
j=0
)
by induction on k 0. The base case k = 0 says that
↗
0
(1 x) xj = 1 x,
↓ ↓
j=0
)
which is true since 0 xj = x0 = 1.
j=0
For the induction step, we assume the result holds for k equal to some n Z 0 . Thus,
we assume that (1 + x) n xj = 1 xn+1. Then → ↓
↓ j=0 ↓
+
n+1 n
(1 x) xj = (1 x) xj +xn+1
↓ ↓
. /
j=0 j=0
) )

38 Finite series and strong induction
n
= (1 x) xj +(1 x)xn+1 = 1 xn+1 +xn+1 xn+2 = 1 xn+2,
↓ ↓ ↓ ↓ ↓
j=0
)
where we used the induction hypothesis in the second-to-last step.
The following propositions provide some useful arithmetic properties of sums.
Proposition 4.6. (i) Suppose a → Z and let (x j )M j=m be a finite sequence in Z. Then
M M
a x = (ax ).
j j
·
. /
j=m j=m
) )
(ii) If a Z, then for all n N,
→ →
n
a = na.
j=1
)
In particular, n 1 = n.
j=1
Proof. (i) We ha+ve
M M
a x = a (x +x + +x ) = ax +ax + +ax = (ax ).
j m m+1 M m m+1 M j
· · ··· ···
. /
j=m j=m
) )
(ii) We have
n
a = a+a+ +a = (1+1+ +1)a = na.
··· ···
) j=1 nterms nterms
Proposition 4.7. Suppose a % ,b,c → &’Z satis ( fy a % ↘ b < & c ’ . Furt ( hermore, suppose (x j )c j=a and
(y
j
)c
j=a
are finite sequences in Z.
c b c
(i) x = x + x .
j j j
j=a j=a j=b+1
) ) )
b b b
(ii) (x +y ) = x + y .
j j j j
j=a j=a j=a
) ) )
Proof. (i) We have
c b c
x = (x + +x )+(x + +x ) = x + x .
j a b b+1 c j j
··· ···
j=a j=a j=b+1
) ) )
(ii) We have
b b b
(x +y ) = (x +y )+ +(x +y ) = (x + +x )+(y + +y ) = x + y .
j j a a b b a b a b j j
··· ··· ···
j=a j=a j=a
) ) )

Finite series 39
The following proposition shows how we can shift the summation index without altering
a sum.
Proposition 4.8. Suppose (x j )M j=m is a finite sequence in Z and that r → Z. Then
M M+r
x = x .
j j r
↑
j=m j=m+r
) )
Proof. We have
M M+r
x = x +x + +x = x +x + +x = x .
j m m+1 M (m+r) r (m+r+1) r (M+r) r j r
··· ↑ ↑ ··· ↑ ↑
j=m j=m+r
) )
Finally, we prove a useful result about inequalities for finite sums.
Proposition 4.9. Suppose (x j )M j=m and (y j )M j=m are finite sequences in Z such that x j ↘ y j
for all m j M. Then
↘ ↘
M M
x y .
j j
↘
j=m k=m
) )
Proof. Let P(M) be the statement that
M M
x y
j j
↘
j=m k=m
) )
for all finite sequences (x j )M j=m and (y j )M j=m in Z such that x j ↘ y j for all m ↘ j ↘ M. We
will prove that P(M) is true for all M m by induction on M.
↗
First note that P(m) is the statement x y , which is true by assumption. Now
m m
↘
suppose that P(M) is true for some M m. Then
↗
M+1 M M M+1
x = x +x y +y = y .
j j M+1 j M+1 j
↘
j=1 j=1 j=1 j=1
) ) ) )
This completes the proof of the induction step.
Exercises.
4.2.1 ([BG10, Proj. 4.12]). Find and prove a formula for k j3.
j=1
4.2.2. Prove by induction that +
k
k(3k 1)
(3i 2) = ↓ for all k N.
↓ 2 →
i=1
)

40 Finite series and strong induction
4.2.3. Prove by induction that
n
2 2n 4
= ↓ for all n Z, n 3.
k2 3k +2 n 1 → ↗
k=3 ↓ ↓
)
(Strictly speaking, this question involves rational numbers, which we haven’t seen yet. But
you can do arithmetic with them just like you have in previous math courses.)
4.3 The Binomial Theorem
Theorem 4.10. Suppose k,m Z 0 , with m k. Then k! is divisible by m!(k m)!.
→ ↓ ↘ ↓
Proof. We will prove this result by induction. However, since the statement involves two
parameters, we have to be careful about how we set up the induction. For each k Z 0 , we
→ ↓
let P(k) be the statement
for all 0 m k, k! is divisible by m!(k m)!.
↘ ↘ ↓
Then, to prove the theorem, it su!ces to prove that P(k) is true for all k Z 0 . We will
→ ↓
do this by induction on k.
The base case is when k = 0. Then the condition 0 m k forces m = 0, and so we
↘ ↘
only need to note that k! = 0! = 1 is divisible by m!(k m)! = 0!0! = 1 1 = 1.
↓ ·
Now we assume that P(n) is true for some n Z 0 , and we need to show that P(n+1)
→ ↓
is true. If m = 0, then m!(n+1 m)! = 0!(n+1)! = (n+1)!, which clearly divides (n+1)!.
↓
Similarly, if m = n+1, then m!(n+1 m)! = (n+1)!0! = (n+1)!, which divides (n+1)!.
↓
So it remains to consider the cases where 1 m n.
↘ ↘
Fix m satisfying 1 m n. We have assumed that P(n) is true. Using the m 1 and
↘ ↘ ↓
m cases of P(n), there exist integers a and b such that
n! = a(m 1)!(n m+1)! and n! = b(m!)(n m)!.
↓ ↓ ↓
Then
(n+1)! = n!(n+1)
= n!(m+n+1 m)
↓
= n!m+n!(n+1 m)
↓
= a(m 1)!(n m+1)!m+b(m!)(n m)!(n+1 m)
↓ ↓ ↓ ↓
= (a+b)(m!)(n m+1)!,
↓
which implies that m!(n + 1 m)! divides (n + 1)!, completing the proof of the induction
↓
step.
By Theorem 4.10, k! is an integer for 0 m k. We define
m!(k m)! ↘ ↘
↑
k k!
= ,
m m!(k m)!
  ↓
which we read as “k choose m” (since one can show that it is equal to the number of ways
of choosing m objects from a collection of k objects) and call it a binomial coe”cient.

The Binomial Theorem 41
Corollary 4.11. For 1 m n, we have
↘ ↘
n+1 n n
= + .
m m 1 m
   ↓   
Proof. In the proof of the Theorem 4.10 we obtained the equality
(n+1)! = n!m+n!(n+1 m).
↓
Dividing both sides by m!(n+1 m)! gives
↓
(n+1)! n!m n!(n+1 m)
= + ↓
m!(n+1 m)! m!(n+1 m)! m!(n+1 m)!
↓ ↓ ↓
(n+1)! n! n!
= = + ,
↔ m!(n+1 m)! (m 1)!(n+1 m)! m!(n m)!
↓ ↓ ↓ ↓
which is precisely the corollary. (Note that, while we have not yet discussed division, the
steps above are justified by the fact that the Binomial Theorem tells us that the fractions
above are actually integers. So we are simply using properties of divisibility of integers.)
Corollary 4.11 tells us that the binomial coe!cients can be obtained from Pascal’s tri-
angle.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
.
.
.
If we number the rows from the top, starting at zero, then the m-th entry in the k-th row
is k . Each entry not on the outside edge is the sum of its two neighbours in the previous
m
row. You may have learned in high school that
! "
(a+b)2 = a2 +2ab+b2,
(a+b)3 = a3 +3a2b+3ab2 +b3.
Here is the general form, allowing you to write a similar formula for any exponent.
Theorem 4.12 (Binomial Theorem for integers). If a,b Z and k Z 0 , then
→ → ↓
k
k
(a+b)k = ambk m.
↑
m
m=0 
)
Proof. We prove the result by induction on k. For the base case, we have
0
(a+b)0 = 1 = a0b0.
0
 

42 Finite series and strong induction
Now assume that, for some n Z 0 , we have
→ ↓
n
n
(a+b)n = ambn m.
↑
m
m=0 
)
Then
n+1
n+1
ambn+1 m
↑
m
m=0 
)
n
n+1 n+1 n+1
= a0bn+1 + ambn+1 m + an+1b0 (by Prop. 4.7(i))
↑
0 m n+1
  m=1   
)
n
n n
= bn+1 + + ambn+1 m +an+1 (by Cor. 4.11)
↑
m 1 m
m=1 ↓   
)
n n
n n
= bn+1 + ambn+1 m + ambn+1 m +an+1 (by Prop. 4.7(ii))
↑ ↑
m 1 m
m=1 ↓  m=1 
) )
n 1 n
↑ n n
= bn+1 + am+1bn+1 (m+1) + ambn+1 m +an+1 (by Prop. 4.8 with r = 1)
↑ ↑
m m
m=0  m=1 
) )
n n
n n
= am+1bn+1 (m+1) + ambn+1 m (by Prop. 4.7(i))
↑ ↑
m m
m=0  m=0 
) )
n n
n n
= a ambn m +b ambn m (by Prop. 4.6(i))
↑ ↑
m m
m=0  m=0 
) )
= a(a+b)n +b(a+b)n (by the induction hypothesis)
= (a+b)n+1,
completing the proof of the induction step.
Theorem 4.12 justifies the term binomial coe”cient, since the integers k are the coef-
m
ficients of the expansion of a power of a binomial.
! "
Corollary 4.13. For k Z 0 , we have
→ ↓
k
k
= 2k.
m
m=0 
)
Proof. Take a = b = 1 in Theorem 4.12.

Strong induction 43
Exercises.
4.3.1 (Leibniz’s formula [BG10, Proj. 4.23]). Consider an operation denoted by that is
↔
applied to functions (denoted u,v,w). Assume that the operation satisfies the following
↔
axioms:
(u+v) = u +v ,
↔ ↔ ↔
(uv) = uv +uv,
↔ ↔ ↔
(cu) = cu, where c is a constant.
↔ ↔
Define w(k) recursively by
(i) w(0) = w.
(ii) Assuming w(n) is defined (where n Z 0 ), define w(n+1) = w(n) ↔.
→ ↓
Prove that ! "
k
k
(uv)(k) = u(m)v(k m).
↑
m
m=0 
)
(Of course, you know an operation with these properties, namely, the derivative. However,
no calculus is needed to prove the above statement.)
4.4 Strong induction
There is a second form of induction, sometimes called strong induction.
Theorem 4.14 (Principle of mathematical induction—second form). For each k N, let
→
P(k) be a statement. Assume that
(i) P(1) is true, and
(ii) if P(j) is true for all integers j such that 1 j n, then P(n+1) is true.
↘ ↘
Then P(k) is true for all k N.
→
Proof. This can be proved by proving the statement “P(j) is true for all integers j such
that 1 j k” by induction (the first form of induction) on k. We leave the details as an
↘ ↘
exercise (Exercise 4.4.1).
Note the di”erence between Theorem 4.14 and Theorem 2.19. In Theorem 2.19, one only
assumes P(n) in the induction step. However, in Theorem 4.14, one assumes P(j) for all
1 j n. Of course, one can start the induction at any integer (as opposed to 1).
↘ ↘
The Fibonacci numbers (f ) are defined by
j →j=1
f = 1, f = 1, and
1 2

44 Finite series and strong induction
f = f +f for n 3.
n n 1 n 2
↑ ↑ ↗
Using strong induction, one can obtain an explicit formula for the Fibonacci numbers—one
thatgivesthen-thFibonaccinumberdirectly, withoutcomputingitrecursively. Theformula
involves irrational numbers, which we will discuss in more detail later. However, since this
is a such a classic example, we will assume for now that we know about irrational numbers.
Proposition 4.15. For k N, we have
→
k k
1 1+↖5 1 ↖5
f = ↓ . (4.1)
k
↖5 
.
2
/
↓
.
2
/

 
Proof. Let
1+↖5 1 ↖5
a = and b = ↓ .
2 2
Since the recursive formula defining the Fibonacci numbers is not valid until n 3, we need
↗
to check two bases cases. We leave it as an exercise to check that (4.1) gives f = 1 and
1
f = 1, as desired.
2
Now we assume that the formula (4.1) holds for all 1 k n for some n 2. We will
↘ ↘ ↗
need the computations
3+↖5 1+2↖5+5
a+1 = = = a2,
2 4
3 ↖5 1 2↖5+5
b+1 = ↓ = ↓ = b2.
2 4
Then we have
f = f +f
n+1 n n 1
↑
1 1
= (an bn)+ (an 1 bn 1)
↑ ↑
↖5 ↓ ↖5 ↓
1
= (an +an 1 bn bn 1)
↑ ↑
↖5 ↓ ↓
1
= (an 1(a+1) bn 1(b+1))
↑ ↑
↖5 ↓
1
= (an 1a2 bn 1b2)
↑ ↑
↖5 ↓
1
= (an+1 bn+1),
↖5 ↓
completing the induction proof.
You might wonder where the formula (4.1) comes from. We see from the proof that the
key property of a and b is that a2 = a + 1 and b2 = b + 1. In fact, the recursion relation
f = f +f leads to the quadratic equation x2 = x+1, and a and b are precisely the
n n 1 n 2
↑ ↑
two roots of this equation.

Strong induction 45
Exercises.
4.4.1. Prove Theorem 4.14.
4.4.2 ([BG10, Proj. 4.26]). A sequence (x ) satisfies
j →j=0
1
x = 1, and for all m n 0, x +x = (x +x ).
1 m+n m n 2m 2n
↗ ↗ ↑ 2
Find a formula for x . Prove that your formula is correct.
j
4.4.3 ([BG10, Prop. 4.30]). Prove that, for all k,m N, where m 2, we have
→ ↗
f = f f +f f .
m+k m 1 k m k+1
↑
4.4.4 ([BG10, Prop. 4.31]). Prove that, for all k N, we have
→
f = f2 +f2 .
2k+1 k k+1
4.4.5 ([BG10, Prop. 4.32]). Prove that, for all k,m N, f
mk
is divisible by f
m
.
→
4.4.6 ([BG10, Proj. 4.33]). How many ways are there to order the numbers 1,2,...,20 in a
row so that the first number is 1, the last number is 20, and each pair of consecutive numbers
di”er by at most 2?

Chapter 5
Naive set theory
In this section we discuss some important basic concepts in set theory. Since everything in
mathematics is, in some sense, built from sets, the notion of a set is fundamental.
5.1 Subsets and equality
As we mentioned before, a set is a collection of things, called its elements or members. We
write x A to indicate that x is a member of the set A and we write x A to indicate that
→ ↑→
x is not a member of the set A.
It is important to note that for each x, the only options are x A and x A. In
→ ↑→
particular, an object cannot be an element of a set more than once and the order of elements
is irrelevant. For instance, the sets
2,2,3 and 2,3 and 3,2
{ } { } { }
are the same. They both contain the natural numbers 2 and 3 and nothing else.
In Section 2.2, we introduced the symbols , ⫅̸, and . In particular
≃ ↑≃
(A B) if and only if (x A = x B).
≃ → ↔ →
We will also sometimes write B A to mean A B.
↙ ≃
Proposition 5.1. Suppose A, B, and C are sets.
(i) A A. (Set containment is reflexive.)
≃
(ii) If A B and B C, then A C. (Set containment is transitive.)
≃ ≃ ≃
Proof. (i) Since x A = x A is clearly true, we have A A.
→ ↔ → ≃
(ii) Suppose A B and B C. We want to show that x A = x C. Indeed, we
≃ ≃ → ↔ →
have
x A = x B (since A B)
→ ↔ → ≃
= x C. (since B C)
↔ → ≃
46

Subsets and equality 47
We also discussed the notion of set equality in Section 2.2. In particular, the following
statements are equivalent for two sets A and B:
• A = B.
• x A x B.
→ ⇐↔ →
• A B and B A.
≃ ≃
Example 5.2. Define
A = 3n+1 : n Z and B = 3m+10 : m Z .
{ → } { → }
We will prove that A = B. We do this by proving that A B and B A.
≃ ≃
First we prove that A B. To do this, we need to prove that x A = x B. So
≃ → ↔ →
suppose x A. Then there exists n Z such that x = 3n+1. Thus
→ →
x = 3n+1 = 3n 9+10 = 3(n 3)+10.
↓ ↓
Therefore, if we take m = n 3, we have m Z and x = 3m+10. So x B. This completes
↓ → →
the proof that x A = x B, hence that A B.
→ ↔ → ≃
Next we prove that B A. So we need to prove that x B = x A. So suppose
≃ → ↔ →
x B. Then there exists m Z such that x = 3m+10. Thus
→ →
x = 3m+10 = 3m+9+1 = 3(m+3)+1.
Therefore, if we let n = m+3, we have n Z and x = 3n+1. So x A. This completes
→ →
the proof that x B = x A, hence that B A.
→ ↔ → ≃
Proposition 5.3. Suppose A, B, and C are sets.
(i) A = A. (Set equality is reflexive.)
(ii) If A = B, then B = A. (Set equality is symmetric.)
(iii) If A = B and B = C, then A = C. (Set equality is transitive.)
Proof. The proof of this proposition is left as an exercise (Exercise 5.1.2).
The empty set, denoted ⫋, is the set with no elements. That is, it is the set such that
x ⫋ is never true, no matter what x is. The following proposition implies that there is
→
only one empty set.
Proposition 5.4. Suppose ⫋1 and ⫋2 have the property that x ⫋1 is never true and
→
x ⫋2 is never true. Then ⫋1 = ⫋2 .
→
Proof. Assume that ⫋1 and ⫋2 have the given properties. The statement ⫋1 = ⫋2 is
equivalent to the statement
x ⫋1 x ⫋2
→ ⇐↔ →
This is clearly true, since both sides are false for all x.

48 Naive set theory
Proposition 5.5. The empty set is a subset of every set. That is, for every set S, we have
⫋ S.
≃
Proof. Suppose S is a set. Then the inclusion ⫋ S is equivalent to the implication
≃
x ⫋ = x S,
→ ↔ →
which is true, since the hypothesis is always false. See Remark 3.4.
Exercises.
5.1.1 ([BG10, Proj. 5.3]). Consider the following sets:
A = 3x : x N ,
{ → }
B = 3x+21 : x N ,
{ → }
C = x+7 : x N ,
{ → }
D = 3x : x N and x > 7 ,
{ → }
E = x : x N ,
{ → }
F = 3x 21 : x N ,
{ ↓ → }
G = x : x N and x > 7 .
{ → }
Determine which of the following set equalities are true. If a statement is true, prove it. If
it is false, explain why the set equality does not hold. (Not all of the sets are used in this
exercise. These sets will play a role in Exercise 5.2.1.)
(i) D = E.
(ii) C = G.
(iii) D = B.
5.1.2. Prove Proposition 5.3.
5.1.3 ([BG10, Proj. 5.5]). Are the following sets equal?
(i) S = m : m N and T m = m for a specified m N.
{ → } { } →
(ii) U = my : y Z, m N, my > 0 and V
m
= my : y Z, my > 0 for a specified
{ → → } { → }
m N.
→
(iii) V
m
and W
m
= my : y Z, y > 0 for a specified m N.
{ → } →
Find the simplest possible way of writing each of these sets.

Intersections and unions 49
5.2 Intersections and unions
The intersection of two sets A and B is
A B = x : x A and x B .
∝ { → → }
In other words,
(x A B) (x A and x B).
→ ∝ ⇐↔ → →
If A B = ⫋, we say that A and B are disjoint.
∝
The union of A and B is
A B = x : x A or x B .
′ { → → }
In other words,
(x A B) (x A or x B).
→ ′ ⇐↔ → →
Examples 5.6. (i) 1,2,5 2,8,9 = 1,2,5,8,9 and 1,2,5 2,8,9 = 2 .
{ }′{ } { } { }∝{ } { }
(ii) n : n Z, n 0 N = Z.
{↓ → ↗ }′
(iii) n N : n is even n N : n is divisible by 4 = n N : n is divisible by 4
{ → }∝{ → } { → }
(iv) If A = 2n : n Z and B = 2n+1 : n Z , then A B = Z and A B = ⫋. In
{ → } { → } ′ ∝
particular, A and B are disjoint.
(v) n Z: n 3 n Z: n is even = 2n: n N, n 2 .
{ → ↗ }∝{ → } { → ↗ }
If A and B are sets, then their set di!erence is
A B = x: x A and x B .
↓ { → ↑→ }
The set di”erence is also sometimes written as A B. The symmetric di!erence of A and B
\
is
A#B = (A B) (B A).
↓ ′ ↓
It is clear from the definition that A#B = B#A, which is why this is called the symmetric
di”erence. (Note that A B is not equal to B A in general.)
↓ ↓
If A X, then the complement of A in X is X A. If the larger set X is clear from the
≃ ↓
context, then we sometimes write A↭ for the complement of A in X. But it is important to
note that the notation A↭ does not make sense unless we have some larger set X in mind.
Examples 5.7. (i) An integer is said to be odd if is it not even. Thus, the set of odd
integers is the complement in Z of the set of even integers:
Z n Z : n is even = n Z : n is odd .
↓{ → } { → }
(ii) Z N = n Z : n 0 and N Z = ⫋.
↓ { → ↘ } ↓
(iii) n Z : n 0 # n Z : n 0 = n Z : n = 0 .
{ → ↘ } { → ↗ } { → ↑ }

50 Naive set theory
Proposition 5.8. Suppose A,B X. Then
≃
A B B↭ A↭.
≃ ⇐↔ ≃
Proof. Suppose A B. Then
≃
x B↭ (x X) and (x / B)
→ ⇐↔ → →
= (x X) and (x / A) (since x A would imply x B)
↔ → → → →
= x A↭.
↔ →
So B↭ A↭.
≃
↭
To prove the reverse implication, first note that, for any Y X, we have Y↭ = Y
≃
(Exercise 5.2.3). Thus, by what we have already proved,
! "
↭ ↭
B↭ A↭ = A↭ B↭ = A B.
≃ ↔ ≃ ↔ ≃
# $ # $
Theorem 5.9 (De Morgan’s laws). Suppose A,B X.
≃
(i) (A B)↭ = A↭ B↭.
∝ ′
(ii) (A B)↭ = A↭ B↭.
′ ∝
Proof. We will prove (ii) and leave the proof of (i) as an exercise (Exercise 5.2.4). For x X,
→
we have
x (A B)↭ (x A B)
→ ′ ⇐↔ ¬ → ′
(x A or x B)
⇐↔ ¬ → →
x A and x B
⇐↔ ↑→ ↑→
x A↭ and x B↭
⇐↔ → →
x A↭ B↭.
⇐↔ → ∝
Thus x (A B)↭ x A↭ B↭, and so (A B)↭ = A↭ B↭.
→ ′ ⇐↔ → ∝ ′ ∝
If A, B, and C are sets, we have
(A B) C = A (B C) and (A B) C = A (B C).
′ ′ ′ ′ ∝ ∝ ∝ ∝
(We leave this as an exercise for you to verify.) In other words, the operations of union and
intersection are associative. Therefore, as for addition (see Remark 1.29), we can unambigu-
ously write expressions like
A B C D and A B C D,
′ ′ ′ ∝ ∝ ∝
since the result is the same no matter how we group the terms.
In fact, onecan formeven morearbitrary unionsand intersections. IfI issomeset (which
we think of as an index set) and, for each i I, A is a set. Then
i
→
A = x : x A for some i I and A = x : x A for all i I .
i i i i
{ → → } { → → }
i I i I
↗ ↗

Intersections and unions 51
Example 5.10. (i) For i Z, define A
i
= n : n Z, n i . Then
→ { → ↗ }
A
i
= ⫋, A
i
= Z.
i ↗ Z i ↗ Z
(ii) We have
n : n N, n m = 1 , n : n N, n m = N
{ → ↘ } { } { → ↘ }
m ↗ N m ↗ N
A special case of the arbitrary unions and intersections defined above is when we have
finitely many sets A
1
,A
2
,...,A
k
for some k N. Then
→
k
A = x : x A for some i 1,2,...,k and
i i
{ → →{ }}
i=1

k
A = x : x A for all i 1,2,...,k .
i i
{ → →{ }}
i=1

Union and intersection are also commutative:
A B = B A and A B = B A.
′ ′ ∝ ∝
We even have a type of distributivity for union and intersection. Our proofs of these prop-
erties will use the following logical facts: If P, Q, and R are statements, then
P and (Q or R) (P and Q) or (P and R)
⇐↔
and
P or (Q and R) (P or Q) and (P or R).
⇐↔
In other words, and is distributive over or, and or is distributive over and.
Proposition 5.11. Suppose A, B, and C are sets. Then
C (A B) = (C A) (C B).
∝ ′ ∝ ′ ∝
Proof. We have
x C (A B) x C and x A B
→ ∝ ′ ⇐↔ → → ′
x C and (x A or x B)
⇐↔ → → →
(x C and x A) or (x C and x B)
⇐↔ → → → →
x C A or x C B
⇐↔ → ∝ → ∝
x (C A) (C B).
⇐↔ → ∝ ′ ∝
Proposition 5.12. Suppose A, B, and C are sets. Then
C (A B) = (C A) (C B).
′ ∝ ′ ∝ ′

52 Naive set theory
Proof. We have
x C (A B) x C or x A B
→ ′ ∝ ⇐↔ → → ∝
x C or (x A and x B)
⇐↔ → → →
(x C or x A) and (x C or x B)
⇐↔ → → → →
(x C A) and (x C B)
⇐↔ → ′ → ′
x (C A) (C B).
⇐↔ → ′ ∝ ′
Proposition 5.11 says that intersection is distributive over union and Proposition 5.12
says that union is distributive over intersection.
Example 5.13. Suppose
A = 1,2,4,5 , B = 2,3,5,6 , C = 4,5,6,7 .
{ } { } { }
Then
C (A B) = 4,5,6,7 2,5 = 2,4,5,6,7 ,
′ ∝ { }′{ } { }
but
(C A) (C B) = 1,2,4,5,6,7 2,3,4,5,6,7 = 2,4,5,6,7 .
′ ∝ ′ { }∝{ } { }
Thus, C (A B) = (C A) (C B).
′ ∝ ′ ∝ ′
Exercises.
5.2.1 ([BG10, Proj. 5.11]). Consider the sets from Exercise 5.1.1. Determine which of the
following set equalities are true. If a statement is true, prove it. If it is false, explain why
the set equality does not hold.
(i) A E = B.
∝
(ii) A C = B.
∝
(iii) E F = A.
∝
5.2.2 ([BG10, Proj. 5.12]). Determine which of the following statements are true for all sets
A, B, and C. If a double implication fails, determine whether one or the other of the possible
implications holds. If a statement is true, prove it. If it is false, provide a counterexample.
(i) C A and C B C (A B).
≃ ≃ ⇐↔ ≃ ′
(ii) C A or C B C (A B).
≃ ≃ ⇐↔ ≃ ′
(iii) C A and C B C (A B).
≃ ≃ ⇐↔ ≃ ∝
(iv) C A or C B C (A B).
≃ ≃ ⇐↔ ≃ ∝

Cartesian products 53
↭
5.2.3. Suppose Y X. Prove that Y↭ = Y
≃
5.2.4. Prove Theorem 5.9(i). ! "
5.2.5 ([BG10, Proj. 5.16]). For each of the following assertions, prove it is true for all sets
A, B, and C, or provide a counterexample.
(i) A (B C) = (A B) (A C).
↓ ′ ↓ ′ ↓
(ii) A (B C) = (A B) (A C).
∝ ↓ ∝ ↓ ∝
5.3 Cartesian products
Suppose A and B are sets. We define a new set
A B := (a,b): a A, b B ,
∞ { → → }
called the Cartesian product of A and B. We call (a,b) an ordered pair. Note that (a,b) is
not thesameastheset a,b . Inaset, theorderofelementsisnotrelevant, so a,b = b,a
{ } { } { }
for all a and b. However, equality of ordered pairs is given by
(a,b) = (c,d) a = c and b = d.
⇐↔
Thus (a,b) = (b,a) if and only if a = b.
Example 5.14. If A = 1,2 and B = 2,3 , then
{ } { }
A B = (1,2),(1,3),(2,2),(2,3) .
∞ { }
Example 5.15. TheCartesianproductN Nisthesetofallorderedpairsofnaturalnumbers.
∞
For example, (3,5) N N.
→ ∞
Example 5.16. We will learn about the set R of real numbers in Section 7. Then R R is
∞
the Cartesian plane you have likely seen in previous math courses.
Proposition 5.17. If A and B are nonempty sets such that A = B, then A B = B A.
↑ ∞ ↑ ∞
Proof. Suppose A and B are nonempty sets, with A = B. Then either A B or B A.
↑ ↑≃ ↑≃
Suppose A B. Then there exists an element a A such that a B. Since B is not empty,
↑≃ → ↑→
there exists some b B. Then (a,b) A B, but (a,b) B A, since a B. The case
→ → ∞ ↑→ ∞ ↑→
where B A is analogous.
↑≃
Remark 5.18. Note ⫋ A = ⫋ = A ⫋, for any set A. This is why we needed the hypothesis
∞ ∞
that A and B are nonempty in Proposition 5.17.
Proposition 5.19. Let A, B, and C be sets.
(i) A (B C) = (A B) (A C).
∞ ′ ∞ ′ ∞
(ii) A (B C) = (A B) (A C).
∞ ∝ ∞ ∝ ∞

54 Naive set theory
Proof. We will prove part (i) and leave the proof of part (ii) as an exercise (Exercise 5.3.1).
We have
(x,y) A (B C) x A and y (B C)
→ ∞ ′ ⇐↔ → → ′
x A and (y B or y C)
⇐↔ → → →
(x A and y B) or (x A and y C)
⇐↔ → → → →
(x,y) A B or (x,y) A C
⇐↔ → ∞ → ∞
(x,y) (A B) (A C).
⇐↔ → ∞ ′ ∞
Exercises.
5.3.1. Prove Proposition 5.19(ii).
5.3.2 ([BG10, Proj. 5.21]). For each of the following statements, prove that it is true for all
sets A, B, C, and D, or give a counterexample.
(i) (A B) (C D) = (A C) (B D).
∞ ′ ∞ ′ ∞ ′
(ii) (A B) (C D) = (A C) (B D).
∞ ∝ ∞ ∝ ∞ ∝
5.4 Functions
We now turn our attention to the important concept of a function. You have all seen
functions in previous math classes. You probably thought of a function in the following way.
A function consists of
• a set A called the domain of the function;
• a set B called the codomain of the function;
• a “rule” f that “assigns” to each a A an element f(a) B.
→ →
We denote such a function f: A B.
∈
Example 5.20. Consider the function f: Z Z given by f(n) = n2 +2 for all n Z. The
∈ →
domain of f is Z and the codomain is also Z. Note that, while f must assign some element
of the codomain to every element of the domain, it is not the case that every element of the
codomain is equal to f(n) for some element n of the domain. For instance, for the above
function f, there is no n Z such that f(n) = 1. The functions
→ ↓
• f: Z Z, f(n) = n2 +2 for all n Z, and
∈ →
• f: Z N, f(n) = n2 +2 for all n Z,
∈ →

Russell’s paradox and axiomatic set theory 55
are di!erent functions, even though their domains are equal and the “rule” is the same.
The domain and the codomain are part of the function. So if two functions have di”erent
codomains, they are di”erent functions.
Example 5.21. Every sequence (x
j
)
→j=1
is really a function with domain N, where we have
just written x instead of f(j).
j
The above definition of a function is rather vague. In particular what do the words “rule”
and “assign” mean? To give a more precise definition of a function, we think of it in terms
of its graph. The graph of f: A B is
∈
$(f) = (a,b) A B : b = f(a) = (a,f(a)) : a A A B.
{ → ∞ } { → }≃ ∞
If you think about the way you have drawn graphs (say, in calculus), you can convince
yourself that this definition corresponds to what you have seen before.
Definition 5.22 (Function). A function with domain A and codomain B is a subset $ of
A B such that for each a A, there is one and only one b B, such that (a,b) $. If
∞ → → →
(a,b) $, we write b = f(a).
→
Remark 5.23. If you think about our precise definition of a function (Definition 5.22), it
corresponds to what you might have called the “vertical line test” for functions in calculus.
Example 5.24. A binary operation on a set A is a function f: A A A. For example,
∞ ∈
addition is a binary operation on Z. So it is a function plus: Z Z Z. However, we
∞ ∈
usually write m+n instead of plus(m,n).
Exercises.
5.4.1. Which of the following are functions?
(i) (a,a2) : a Z Z Z
{ → }≃ ∞
(ii) (a,a2) : a N N N
{ → }≃ ∞
(iii) (a2,a) : a Z n2 : n Z Z
{ → }≃{ → }∞
(iv) (a2,a) : a N n2 : n N N.
{ → }≃{ → }∞
5.5 Russell’s paradox and axiomatic set theory
You may wonder why this chapter of the notes is called naive set theory. It is because we
have implicitly assumed that, given any property P, we can define a set
x : x has property P .
{ }

56 Naive set theory
However, this leads to problems. Consider the set
R = x : x is a set and x x .
{ ↑→ }
Then we ask the question
is R R?
→
Well, if R R, then R R is false, and so, by the definition of R, we have R R. On the
→ ↑→ ↑→
other hand, if R R, then, by the definition of R, we have R R. Thus, we see that
↑→ →
R R R R.
→ ⇐↔ ↑→
This is a contradiction known as Russell’s paradox.
It is possible to fix Russell’s paradox. The fix involves reworking our concept of a set
and starting from a very specific list of axioms about what we are and are not allowed to
do with sets. This is called axiomatic set theory, and is beyond the scope of this course.
The canonical axiomatic set theory is called ZFC, named after Ernst Zermelo, Abraham
Fraenkel, and the Axiom of Choice.
In this course, the problems related to Russell’s paradox are not an issue. All of the sets
that we discuss can be shown to exist in ZFC. Thus, we will remain “naive” and ignore this
issue.

Chapter 6
Equivalence relations and modular
arithmetic
In this chapter we discuss the concept of a relation and, in particular, of an equivalence
relation, a concept that is ubiquitous in mathematics. We then turn our attention to a
particular family of equivalence relations that give rise to modular arithmetic.
6.1 Equivalence relations
Definition 6.1 (Relation). A relation on a set A is a subset of A A. If R A A is a
∞ ≃ ∞
relation on A, we usually write xRy to indicate that (x,y) R and we say that x is related
→
to y by the relation R. So
xRy (x,y) R.
⇐↔ →
We often use other symbols instead of R, such as , , ,<, ,>, , , , etc.
∋ △ ⇔ ↘ ↗ ▽ ̸
Example 6.2. Some examples of relations on Z are:
• equality (=),
• less than (<),
• less than or equal to ( ),
↘
• divides (i.e. a divides b).
For example, formally speaking, the relation is the subset of Z Z given by
↘ ∞
(a,b) : b a N or a = b .
{ ↓ → }
Example 6.3. The graph $(f) of a function f: A A is a special case of a relation, for
∈
which there is exactly one (x,y) $(f) for each x A.
→ →
Definition 6.4 (Equivalence relation, equivalence class). A relation on a set A is an
∋
equivalence relation if it has the following three properties:
57

58 Equivalence relations and modular arithmetic
• a a for all a A. (Reflexivity)
∋ →
• If a b, then b a. (Symmetry)
∋ ∋
• If a b and b c, then a c. (Transitivity)
∋ ∋ ∋
If is an equivalence relation on A, then the equivalence class of a A is
∋ →
[a] := b A : b a .
{ → ∋ }
Sometimes, when we wish to emphasize the particular equivalence relation (for instance,
when we are working with more than one), we write [a] instead of [a].
↘
Examples 6.5. (i) The relation = on Z is an equivalence relation.
(ii) The relation on Z is not an equivalence relation, since it is not symmetric (e.g. 1 2,
↘ ↘
but 2 1).
↑↘
(iii) The relation = on subsets of Z (i.e. set equality) is an equivalence relation.
(iv) The relation on subsets of Z is not an equivalence relation since it is not symmetric.
≃
Note that, in (iii) and (iv), the relation is on the set
A = X : X Z
{ ≃ }
of subsets of Z
Proposition 6.6. Suppose is an equivalence relation on a set A, and a,b A. Then
∋ →
(i) a [a], and
→
(ii) a b [a] = [b].
∋ ⇐↔
Proof. (i) Since is an equivalence relation, it is reflexive. Thus a a. So a [a].
∋ ∋ →
(ii) Suppose a b. We will prove that [a] = [b] by showing the two inclusions [a] [b]
∋ ≃
and [b] [a].
≃
Suppose c [a]. Then c a. Thus, by transitivity of , we have c b, and so c [b].
→ ∋ ∋ ∋ →
Therefore, [a] [b].
≃
Now suppose c [b]. Then c b. By symmetry of , we then have b a (since a b).
→ ∋ ∋ ∋ ∋
Then, by transitivity of , we have c a, and so c [a]. Therefore, [b] [a].
∋ ∋ → ≃
Conversely, suppose [a] = [b]. By part (i), we have a [a] = [b], so a [b]. Hence
→ →
a b.
∋
We say that a is a representative of the equivalence class [a]. Representatives of a given
equivalence class are not unique in general. By Proposition 6.6(ii), b is a representative of
the equivalence class [a] if and only if a b (which is equivalent to b [a]).
∋ →
Proposition 6.6 implies that for each a A, there is a unique equivalence class (namely
→
[a]) containing a. In fact, the equivalence classes of an equivalence relation on A subdivide
the set A in a certain sense, as we shall now explain.

Equivalence relations 59
Proposition 6.7. Suppose is an equivalence relation on a set A. Then, for all a,b A,
∋ →
we have
[a] = [b] or [a] [b] = ⫋.
∝
Proof. Suppose a,b A. If [a] [b] = ⫋, we are done. So assume [a] [b] = ⫋. Then there
→ ∝ ∝ ↑
exists an element c [a] [b]. Thus, a c b, which implies that a b. Therefore, by
→ ∝ ∋ ∋ ∋
Proposition 6.6(ii), we have [a] = [b].
Definition 6.8 (Partition). A partition of a set A is a set %, whose elements are nonempty
subsets of A such that
• P
1
,P
2
%, P
1
= P
2
= P
1
P
2
= ⫋, and
→ ↑ ↔ ∝
• every a A belongs to some P %.
→ →
Equivalently, a set % of nonempty subsets of A is a partition of A if every element of A
belongs to a unique element of %.
Intuitively, a partition of a set A is a subdivision of A into disjoint subsets.
Example 6.9. Let P be the set of even integers and let P be the set of odd integers. Then
1 2
%= P
1
,P
2
is a partition of Z.
{ }
The next proposition says that equivalence relations and partitions are two ways of
viewing the same idea.
Proposition 6.10. (i) Suppose is an equivalence relation on A. Then the set % of
∋
equivalence classes of is partition of A.
∋
(ii) Suppose % is a partition of A. Then the relation defined by
∋
a b a and b lie in the same element of %
∋ ⇐↔
is an equivalence relation on A.
Proof. Part (i) is Proposition 6.6(i) and Proposition 6.7. To prove part (ii), let%be a
partition of A. Define a relation on A by
∋
a b a and b lie in the same element of %.
∋ ⇐↔
Reflexivity: Suppose a A. Then a P for some P %. Thus a a.
→ → → ∋
Symmetry: Suppose a,b A and a b. Then a and b lie in the same element of %. Thus
→ ∋
we also have b a.
∋
Transitivity: Suppose a,b,c A, a b, and b c. Then a and b lie in some P %. Also, b
→ ∋ ∋ →
and c lie in some P %. Since b can only lie in one element of %, we have P = P . Hence
↔ ↔
→
a and c both lie in P, so that a c.
∋
The absolute value of an integer x is defined to be
x if x 0,
x = ↗
| | - x if x < 0.
↓

60 Equivalence relations and modular arithmetic
Example 6.11. Consider the relation on Z defined by
x y x = y .
∋ ⇐↔ | | | |
• Reflexivity: For all x Z, x = x , so x x.
→ | | | | ∋
• Symmetry: For all x,y Z,
→
x y = x = y = y = x = y x.
∋ ↔| | | | ↔| | | | ↔ ∋
• Transitivity: For x,y,z Z,
→
x y and y z = x = y = z = x z.
∋ ∋ ↔| | | | | | ↔ ∋
Thus is an equivalence relation. The equivalence class of x Z is the set x, x . The
∋ → { ↓ }
set
%= x, x : x Z
{{ ↓ } → }
is a partition of Z.
Example 6.12. Consider the relation on Z Z defined by
∞
(x,y) (v,w) 2x 3y = 2v 3w.
∋ ⇐↔ ↓ ↓
• Reflexivity: For all (x,y) Z Z, we have 2x 3y = 2x 3y, so (x,y) (x,y).
→ ∞ ↓ ↓ ∋
• Symmetry: (x,y) (v,w) = 2x 3y = 2v 3w = 2v 3w = 2x 3y =
∋ ↔ ↓ ↓ ↔ ↓ ↓ ↔
(v,w) (x,y).
∋
• Transitivity: Suppose (x,y) (v,w) and (v,w) (u,z). Then 2x 3y = 2v 3w and
∋ ∋ ↓ ↓
2v 3w = 2u 3z. Hence 2x 3y = 2u 3z, and so (x,y) (u,z).
↓ ↓ ↓ ↓ ∋
Thus is an equivalence relation on Z Z. The equivalence classes are sets
∋ ∞
(x,y) Z Z : 2x 3y = n , n Z.
{ → ∞ ↓ } →
That is, they are the points with integer coordinates that lie on a fixed line 2x 3y = n in
↓
the plane.
Exercises.
6.1.1 ([BG10, Proj. 6.7]). For each of thefollowingrelations defined onZ, determinewhether
it is an equivalence relation. If it is, determine the equivalence classes.
(i) x y if x < y.
∋

The division algorithm 61
(ii) x y if x y.
∋ ↘
(iii) x y if x = y .
∋ | | | |
(iv) x y if x = y.
∋ ↑
(v) x y if xy > 0.
∋
(vi) x y if (x y or y x).
∋ | |
6.1.2 ([BG10, Proj. 6.8]). Prove that each of the following relations defined on Z Z is an
∞
equivalence relation. Determine the equivalence classes for each relation.
(i) (x,y) (v,w) if x2 +y2 = v2 +w2.
∋
(ii) (x,y) (v,w) if y x2 = w v2.
∋ ↓ ↓
(iii) (x,y) (v,w) if xy = vw.
∋
(iv) (x,y) (v,w) if x+2y = v +2w.
∋
6.1.3 ([BG10, Proj. 6.9]). On Z (Z 0 ) we define the relation (m 1 ,n 1 ) (m 2 ,n 2 ) if
∞ ↓{ } ∋
m n = n m .
1 2 1 2
(i) Show that this is an equivalence relation.
(ii) For two equivalence classes [(m ,n )] and [(m ,n )], we define two binary operations
1 1 2 2
and via
⊕ ∀
[(m ,n )] [(m ,n )] = [(m n +m n ,n n )]
1 1 2 2 1 2 2 1 1 2
⊕
and
[(m ,n )] [(m ,n )] = [(m m ,n n )].
1 1 2 2 1 2 1 2
∀
What properties do the binary operations have? For example, which axioms of the
integers are satisfied?
6.2 The division algorithm
In Section 6.3, we will discuss an important equivalence relation. We first need a theorem
about division of integers.
Theorem 6.13 (The Division Algorithm). Suppose n N. For every m Z, there exist
→ →
unique q,r Z such that
→
m = qn+r and 0 r n 1.
↘ ↘ ↓
The integer q is called the quotient and r is called the remainder upon division of m by n.

62 Equivalence relations and modular arithmetic
Proof. Fix n N. Let us first prove the existence part of the theorem. We first consider the
→
m 0 case by induction. For the base case m = 0, we can set q = r = 0.
↗
For the induction step, assume there exist q,r Z such that
→
m = qn+r and 0 r n 1.
↘ ↘ ↓
Case 1: r < n 1. Then set q = q and r = r+1, so that
↔ ↔
↓
m+1 = q n+r and 0 r n 1.
↔ ↔ ↔
↘ ↘ ↓
Case 2: r = n 1. Then set q = q +1 and r = 0, so that
↔ ↔
↓
m+1 = qn+r+1 = (q +1)n = q n+r and 0 r n 1.
↔ ↔ ↔
↘ ↘ ↓
In both cases, we found integers q and r with the required properties, completing the proof
↔ ↔
of the induction step.
Now consider the case m < 0. Since m > 0 we can find, by the first part of our proof,
↓
integers q and r such that
m = qn+r and 0 r n 1.
↓ ↘ ↘ ↓
Case 1: r = 0. Then m = ( q)n+0 is the required expression for m.
↓
Case 2: r > 0. Then
m = qn r = ( q 1)n+(n r)
↓ ↓ ↓ ↓ ↓
is the required expression, since 0 < n r < n.
↓
It remains to prove the uniqueness part of the theorem. Suppose that m Z and
→
q
1
n+r
1
= m = q
2
n+r
2
for some q
1
,q
2
,r
1
,r
2
Z, 0 r
1
,r
2
n 1.
→ ↘ ↘ ↓
Then we have
(q q )n = r r . (6.1)
1 2 2 1
↓ ↓
Thus, r r is divisible by n. But since 0 r ,r n 1, we have
2 1 1 2
↓ ↘ ↘ ↓
1 n r r n 1.
2 1
↓ ↘ ↓ ↘ ↓
Since the only multiple of n between 1 n and n 1 is 0, we have r r = 0, so that
2 1
↓ ↓ ↓
r = r . Then (6.1) implies that q = q as well.
1 2 1 2
Examples 6.14. (i) For n = 3 and m = 11, we obtain q = 3 and r = 2 since 11 = 3 3+2.
·
(ii) For n = 5 and m = 26, we obtain q = 6 and r = 4 since 26 = ( 6) 5+4.
↓ ↓ ↓ ↓ ·

The integers modulo n 63
Exercises.
6.2.1. Prove the following statements.
(i) An integer m Z is odd if and only if there exists q Z such that m = 2q +1.
→ →
(ii) For every n Z, n is even or n+1 is even.
→
(iii) An integer m Z is even if and only if m2 is even.
→
6.3 The integers modulo n
Inthissection,wediscussanimportant,andfrequentlyencountered,conceptinmathematics:
the integers modulo n.
For a fixed n N, we define a relation on Z by
→ ⇔
x y x y is divisible by n.
⇔ ⇐↔ ↓
The natural number n is called the modulus. When we wish to make the modulus explicit,
we write
x y mod n.
⇔
If x y mod n, we say that x and y are equivalent modulo n or congruent modulo n (or
⇔
sometimes simply equivalent/congruent mod n). Note that x y mod 1 for all x,y Z,
⇔ →
and so equivalence modulo 1 is not so interesting. For this reason, we usually assume n 2.
↗
Example 6.15. Suppose n = 2. Then x y mod 2 if and only if x y is even, i.e. x and y
⇔ ↓
are either both even or both odd. In this case, we say that x and y have the same parity.
Example 6.16. Fix the modulus 7. Then 2 16, since 2 16 = 14 is divisible by 7.
⇔ ↓ ↓
Similarly, we have
0 7 7 14, 1 6 8 701, 5 7005.
⇔ ↓ ⇔ ⇔ ⇔ ↓ ⇔ ⇔ ⇔
Example 6.17. Suppose n N and m Z. By the Division Algorithm (Theorem 6.13), we
→ →
have
m = qn+r for some q,r Z, 0 r n 1.
→ ↘ ↘ ↓
Then m r = qn is divisible by n, and so m r mod n.
↓ ⇔
Proposition 6.18. Fix a modulus n N.
→
(i) Equivalence modulo n (i.e. ) is an equivalence relation.
⇔
(ii) The equivalence relation has exactly n distinct equivalence classes, namely
⇔
[0],[1],...,[n 1].
↓

64 Equivalence relations and modular arithmetic
Proof. To prove (i), we need to check that is reflexive, symmetric, and transitive.
⇔
Reflexivity: For a Z, we have a a = 0, which is divisible by n, hence a a.
→ ↓ ⇔
Symmetry: Suppose a b. Then n divides a b. So there exists j Z, such that a b = jn.
⇔ ↓ → ↓
Then b a = jn = ( j)n is also divisible by n, and so b a.
↓ ↓ ↓ ⇔
Transitivity: Suppose a b and b c. Then n divides both a b and b c. So there exist
⇔ ⇔ ↓ ↓
j,k Z such that
→
a b = jn and b c = kn.
↓ ↓
Then
a c = (a b)+(b c) = jn+kn = (j +k)n
↓ ↓ ↓
is divisible by n, hence a c.
⇔
To prove (ii), we need to show that the equivalence classes [0],[1],...,[n 1] are distinct,
↓
and that every integer lies in one of them.
If m Z, then Example 6.17 shows that m [r] for some 0 r n 1. So every integer
→ → ↘ ↘ ↓
lies in one of the given classes.
It remains to show that the given equivalence classes are distinct. So suppose 0 m,k
↘ ↘
n 1 and [m] = [k] (i.e. n divides m k). We want to show that this implies m = k. Now,
↓ ↓
0 m,k n 1 = n+1 m k n 1,
↘ ↘ ↓ ↔ ↓ ↘ ↓ ↘ ↓
and the only number between n+1 and n 1 divisible by n is 0. Thus m k = 0, and
↓ ↓ ↓
hence m = k, as desired.
The set of equivalence classes for the relation of equivalence modulo n is called the set
of integers modulo n, and is denoted by Zn or Z/nZ.
Example 6.19. We have
Z5 = [0],[1],[2],[3],[4] .
{ }
Example 6.20. By Proposition 6.18, for any integer a, its equivalence class modulo n is equal
to one of the classes
[0],[1],...,[n 1].
↓
Example 6.17 tells us how to find out which one: we have [a] = [r], where r is the remainder
upon division of a by n. For example, if n = 5, then we have
31 = 6 5+1,
·
and so [31] = [1]. Similarly,
[26] = [1], [ 1] = [4], [12] = [2], [35] = [0].
↓
(The basic idea is that we add or subtract multiples of n until the representative lies in the
range 0,1,...,n 1.) If n = 3, we have
↓
[ 2] = [1], [33] = [0], [20] = [2].
↓

The integers modulo n 65
Proposition 6.21. Fix a modulus n N. If a a
↔
and b b
↔
, then
→ ⇔ ⇔
a+b a +b and ab ab.
↔ ↔ ↔ ↔
⇔ ⇔
Proof. Fix a modulus n. Suppose a a ↔ and b b ↔ . Then there exist k,ϑ Z such that
⇔ ⇔ →
a a = kn and b b = ϑn.
↔ ↔
↓ ↓
Then
(a+b) (a +b) = (a a)+(b b) = kn+ϑn = (k +ϑ)n,
↔ ↔ ↔ ↔
↓ ↓ ↓
and so a+b a +b. Furthermore,
↔ ↔
⇔
ab ab = ab ab +ab ab = a(b b)+(a a)b = aϑn+knb = (aϑ+kb)n,
↔ ↔ ↔ ↔ ↔ ↔ ↔ ↔ ↔ ↔ ↔
↓ ↓ ↓ ↓ ↓
and so ab ab.
↔ ↔
⇔
The above proposition allows us to define two operations on Zn . Namely, we define
addition and multiplication on Zn by
⊕ ∀
[a] [b] = [a+b] and [a] [b] = [ab].
⊕ ∀
Remark 6.22. It is important that you understand why we needed Proposition 6.21 in order
to be able to define the above operations. Remember that [a] = [a] a a and
↔ ↔
⇐↔ ⇔
[b] = [b] b b (by Proposition 6.6(ii)). Our definition of then says that the sum of
↔ ↔
⇐↔ ⇔ ⊕
the classes [a] = [a] and [b] = [b] is
↔ ↔
[a] [b] = [a+b]
⊕
and also that it is
[a] [b] = [a +b].
↔ ↔ ↔ ↔
⊕
So if it is not true that [a+b] = [a +b], then the operation is not well defined, since we
↔ ↔
⊕
are defining it to be two di”erent things (i.e. there is a conflict in our definition). Luckily,
Proposition 6.21 tells us precisely that [a+b] = [a +b].
↔ ↔
To further illustrate this point, suppose we tried to define a function
f: Z5 Z, f([n]) = n.
∈
Then, since [1] = [6], we should have f([1]) = f([6]). But f([1]) = 1 = 6 = f([6]). So, in
↑
fact, this function is not well-defined.
Remark 6.23. Many texts simply reuse the notation + and for addition and multiplication
·
in Zn . (In fact, this is the most common convention.) We use the notation and to make
⊕ ∀
it explicit that these are operations on a di”erent set (Zn as opposed to Z).
Example 6.24. Fix a modulus n N. By Proposition 6.18(ii), for every a Z, the equiva-
→ →
lenceclass[a]mustbeequaltooneoftheclasses[0],[1],...,[n 1]. Whendoingcomputations
↓
in modular arithmetic, we usually write our final answer in this form. (See Example 6.20.)
For example,

66 Equivalence relations and modular arithmetic
(i) If n = 4, we have [3] [2] = [3+2] = [5] = [1].
⊕
(ii) If n = 5, we have [4] [3] = [4 3] = [12] = [2].
∀ ·
(iii) If n = 2, then
[235] [35423] [24] = [1] [1] [0] = [1 1 0] = [0].
∀ ∀ ∀ ∀ · ·
Proposition 6.25. Fix an integer n 2. Addition and multiplication in Zn are commu-
↗
tative, associative, and distributive. Also, the set Zn has an additive identity [0], a multi-
plicative identity [1], and additive inverses (the additive inverse of [a] being [ a]). In other
↓
words, Axioms 1.1–1.4 hold with Z replaced everywhere by Zn .
Proof. We will prove three of these statements, and leave the rest as exercises.
Addition in Zn is commutative: Choose two arbitrary elements [a],[b] Zn . Then we
→
have
[a] [b] = [a+b] by the definition of
⊕ ⊕
= [b+a] commutativity of addition in Z
= [b] [a]. by the definition of
⊕ ⊕
Thus addition in Zn is commutative.
MultiplicationisdistributiveoveradditioninZn : Choosethreearbitraryelements[a],[b],[c]
→
Zn . Then we have
[a] ([b] [c]) = [a] [b+c] by the definition of
∀ ⊕ ∀ ⊕
= [a(b+c)] by the definition of
∀
= [ab+ac] distributivity in Z
= [ab] [ac] by the definition of
⊕ ⊕
= [a] [b] [a] [c]. by the definition of
∀ ⊕ ∀ ∀
Thus distributivity holds in Zn .
The element [0] Zn is an additive identity: Choose an arbitrary element [a] Zn .
→ →
Then we have
[a] [0] = [a+0] by the definition of
⊕ ⊕
= [a]. since 0 is an additive identity for Z
Thus, for all [a] Zn , we have [a] [0] = [a]. So [0] is an additive identity for Zn .
→ ⊕
The remaining statements are left as an exercise (Exercise 6.3.3).

The integers modulo n 67
Exercises.
6.3.1. Perform the following computations in Zn for the given value of n. In each case, write
your final answer in the standard form: [0],[1],[2],...,[n 1]. You should not have to use a
↓
calculator.
(i) [3] [4], n = 5.
⊕
(ii) [0] [4], n = 8.
⊕
(iii) [3667] [6991], n = 3.
⊕
(iv) [2] [3], n = 6.
∀
(v) [2] [3], n = 5.
∀
(vi) [5] [6], n = 7.
∀
(vii) [503259] [32485], n = 2.
∀
6.3.2. Foreachofthefollowingquestions,writeyouranswerinthestandardform: [0],[1],[2],...,[n
↓
1], where n is the modulus.
(i) What is the additive inverse of [3] in Z7 ?
(ii) What is the additive inverse of [3] in Z6 ?
(iii) What is the additive inverse of [5] in Z21 ?
(iv) Is there an element [a] of Z7 such that [a] [3] = [1]? If so, find it. If not, prove that
∀
no such element exists.
(v) Is there an element [a] of Z12 such that [a] [3] = [1]? If so, find it. If not, prove that
∀
no such element exists.
6.3.3. Complete the proof of Proposition 6.25.
6.3.4. Fix a modulus n. Suppose a,b Z satisfy 0 < b < n and [a] [b] = [0]. Prove that
→ ∀
[a] cannot have a multiplicative inverse. In other words, show that there is no [c] Zn such
→
that [c] [a] = [1].
∀
6.3.5. Prove that there are no integers x,y,z such that
9x6 +13y5 +4y2 +3z6 = 0 and 6x4 2y5 +y2 3z8 = 1.
↓ ↓ ↓
Hint: Prove the result by contradiction. Assume the equations have a solution and then do
some computations modulo 3 to arrive at a contradiction.

68 Equivalence relations and modular arithmetic
6.3.6. (i) Without using induction, prove that the following statement is true:
a Z a2 is divisible by 4 or a2 +3 is divisible by 4 .
⇓ →
! "
Hint: Use modular arithmetic.
(ii) Is the statement
a Z, a2 is divisible by 4 or a Z, a2 +3 is divisible by 4
⇓ → ⇓ →
! " ! "
true? Justify your answer.
6.4 Prime numbers
Definition 6.26 (Prime number, composite number, factor). An integer n 2 is prime
↗
if it is divisible only by 1 and n. If an integer n 2 is not prime, it is composite. If
± ± ↗
n = q
1
q
2
q
k
for some q
1
,q
2
,...,q
k
Z, then the q
1
,q
2
,...,q
k
are called factors of n, and
··· →
the expression n = q q q is called a factorization of n.
1 2 k
···
Proposition 6.27. Every integer n 2 can be factored into primes.
↗
Proof. We prove the result by induction on n. The base case is when n = 2, which is already
prime.
For the induction step, assume that n 3 and that any integer less than n (and 2)
↗ ↗
can be factored into primes. If n is prime, we are done. Otherwise, there exist a,b N,
→
a,b 2, such that n = ab. Then a,b < n and so, by the induction hypothesis, a and b can
↗
each be written as a product of primes. This gives a prime factorization of n.
Proposition 6.28. There are infinitely many prime numbers.
Proof. Weprovetheresultbycontradiction. Supposetherearefinitelymanyprimesp ,p ,...,p .
1 2 n
Then consider the number
q = p p p +1.
1 2 n
···
The remainder upon division of q by p is 1, for all 1 i n. Thus, q is not divisi-
i
↘ ↘
ble by any prime number. Therefore q does not have a prime factorization, contradicting
Proposition 6.27.
Recall, from Definition 2.36 that, for m,n Z, not both zero, we define gcd(m,n) to be
→
the smallest element of the set
S = k N : k = mx+ny for some x,y Z .
{ → → }
When m = n = 0, the set S is empty, in which case we define gcd(0,0) = 0.
Proposition 6.29. Suppose m,n Z.
→
(i) gcd(m,n) divides both m and n.

Prime numbers 69
(ii) If m and n are not both zero, then gcd(m,n) > 0.
(iii) Every integer that divides both m and n also divides gcd(m,n).
Proof. The proof of this proposition can be found in [BG10, Prop. 6.29].
Propositions 6.29 and 2.24 imply that gcd(m,n) is the largest integer that divides both
m and n. Thus gcd(m,n) is the greatest common divisor of m and n, justifying the notation.
Proposition 6.30. For all k,m,n Z, we have
→
gcd(km,kn) = k gcd(m,n).
| |
Proof. If k = 0, then
gcd(km,kn) = gcd(0,0) = 0 = 0gcd(m,n).
Now assume k = 0. Let
↑
S = j N : j = mx+ny for some x,y Z
{ → → }
and
T = j N : j = kmx+kny for some x,y Z .
{ → → }
Set g = gcd(m,n) and h = gcd(km,kn). So g is the smallest element of S and h is the
smallest element of T. Our goal is to prove that k g = h.
| |
Since g S, there exist integers x and y such that g = mx +ny . Therefore,
1 1 1 1
→
k g = m( k x )+n( k y ) = mk( x )+nk( y )
1 1 1 1
| | | | | | ± ±
is an element of T. (Here we use the fact that k is equal to either k or k.) Since h is the
| | ↓
smallest element of T, this implies that k g h.
| | ↗
On the other hand, h T, and so there exist integers x and y such that
2 2
→
h = kmx +kny = k (mx +ny ).
2 2 2 2
±| |
So k divides h, and the integer h = (mx +ny ) = m( x )+n( y ) in an element of
| | k ± 2 2 ± 2 ± 2
S. Since g is the smallest element | o | f S, we have g h , and so k g h.
↘ k | | ↘
| |
The two inequalities imply that k g = h.
| |
Proposition 6.31 (Euclid’s lemma). Suppose p is a prime and m,n N. If p mn, then
→ |
p m or p n.
| |
Proof. Suppose p divides mn. If p divides m, we are done. So consider the case that p does
not divide m. We need to show that p divides n. Since p is prime and does not divide m,
we have gcd(m,p) = 1. By Proposition 6.30, we have
gcd(mn,pn) = ngcd(m,p) = n.
Then, by Proposition 6.29(iii), since p divides both mn and pn, we can conclude that p also
divides n.

70 Equivalence relations and modular arithmetic
Corollary 6.32. Suppose k N, p is a prime, and m
1
,...,m
k
N. If p m
1
m
2
m
k
, then
→ → | ···
p m for some 1 i k.
i
| ↘ ↘
Proof. Let P(k) be the statement
m
1
,m
2
,...,m
k
N, (p m
1
m
2
m
k
) = (p m
i
for some 1 i k).
⇓ → | ··· ↔ | ↘ ↘
We prove that P(k) is true for all k 1 by induction on k.
↗
Base case: Consider the case k = 1. The statement P(1) is
m
1
N, (p m
1
) = (p m
1
),
⇓ → | ↔ |
which is clearly true.
Induction step: Assume that P(n) is true for some n N. We will show that P(n+1)
→
is true. Suppose m 1 ,...,m n+1 N and p divides
→
m m m = (m m m )m .
1 2 n+1 1 2 n n+1
··· ···
Then, by Proposition 6.31, p m m or p m . In the first case, the induction hypothesis
1 n n+1
| ··· |
implies that p m for some 1 i n. Thus, in either case, we have p m for some 1 i
i i
| ↘ ↘ | ↘ ↘
n+1. This completes the proof of the induction step.
By Proposition 6.27 every integer n 2 has a prime factorization. Our next goal is to
↗
show that, in fact, such a prime factorization is unique. Of course, one can always re-order
the factors in any factorization. For example,
30 = 2 3 5 = 3 2 5.
· · · ·
So the best we can hope for is that prime factorizations are unique up to such re-ordering
(i.e. that any two prime factorizations of the same integer n 2 d”ier only by re-ordering).
↗
Theorem 6.33. Every integer n 2 has a unique (up to re-ordering) prime factorization.
↗
Proof. A prime factorization exists by Proposition 6.27. It remains to show the uniqueness
part of the theorem. We will do this by induction on n.
Base case: When n = 2, the only factorization is simply the expression 2 itself, since
there is no other way to write 2 as a product of primes (since there are no primes less than
2).
Induction step: Now consider n 3 and suppose that every integer less than n (and 2)
↗ ↗
has a unique prime factorization. Suppose n has two prime factorizations
n = p p p = q q q .
1 2 k 1 2 j
··· ···
Then, by Corollary 6.32, p divides q for some 1 i j. But since q is prime, this implies
1 i i
↘ ↘
that p = q (since p cannot equal 1 or q , and those are the only other factors of q ). So
1 i 1 i i
± ↓
we have
n
= p p p = q q q q q .
2 3 k 1 2 i 1 i+1 j
p 1 ··· ··· ↑ ···
Bytheinductionhypothesis, thesetwoprimefactorizationsof n areequal, uptore-ordering.
p1
Therefore, the two given prime factorizations of n are equal, up to re-ordering.

Prime numbers 71
Proposition 6.34. If p is prime and 0 < r < p, then p is divisible by p.
r
Proof. The proof of this proposition can be found in [B!G"10, Prop. 6.34].
Theorem 6.35 (Fermat’s Little Theorem). If m Z and p is prime, then
→
mp m mod p.
⇔
Proof. Fix a prime p. If p = 2, then Fermat’s Little Theorem says that m2 is even if and
only if m is even, which was Proposition 6.2.1(iii). So we assume p > 2.
Let P(k) be the statement
kp k mod p.
⇔
We will first prove that P(m) is true for all m 0. (We will deal with the case m < 0 after.)
↗
Base case: Since 0p 0 = 0 0 = 0 is divisible by p, we have 0p 0.
↓ ↓ ⇔
Induction step: We assume that P(m) is true for some m 0 and show that P(m+1)
↗
is true. By the Binomial Theorem (Theorem 4.12), we have
p p
p p
(m+1)p = mω1p ω = mω.
↑
ϑ ϑ
ω=0   ω=0  
) )
By Proposition 6.34, p 0 mod p for 0 <ϑ< p . Therefore,
ω ⇔
!p"
p p p
(m+1)p = mω m0 + mp = 1+mp 1+m mod p,
ϑ ⇔ 0 p ⇔
ω=0      
)
where we used the induction hypothesis in the last step. This completes the proof of the
induction step. (Note that the string of “equations” above involves both = and . But since
⇔
equality implies equivalence mod p, the corresponding string, where we replace all = symbols
by symbols is also true. Then we use transitivity of to conclude that (m+1)p 1+m.)
⇔ ⇔ ⇔
It remains to prove the statement for m < 0. Suppose m < 0. Define n = m. Then
↓
n > 0 and so, by the above, we have np n mod p. Since p is odd, we have
⇔
mp = ( n)p = ( 1)pnp = np n = m.
↓ ↓ ↓ ⇔ ↓
Thus the result also holds for m < 0.
Corollary 6.36. Suppose m Z and let p be a prime that does not divide m. Then
→
mp 1 1 mod p.
↑
⇔
Proof. By Theorem 6.35, we have mp m. In other words, p divides mp m = m(mp 1 1).
↑
⇔ ↓ ↓
Since p does not divide m, we can conclude that p divides mp 1 1 by Proposition 6.31.
↑
↓
Thus mp 1 1.
↑
⇔
Remark 6.37. Fermat’sLittleTheoremisthemathematicsthatunderpinsthetheoryofRSA
encryption. So your bank account information is secure when you check your balance online
because of Fermat’s Little Theorem.

72 Equivalence relations and modular arithmetic
Exercises.
6.4.1 ([BG10, Proj. 6.27]). For which n 2 does Zn satisfy the cancellation property (Ax-
↗
iom 1.5)? Prove your assertion.
6.4.2. Let m,n N. Suppose m divides n, and p is a prime factor of n that is not a prime
→
factor of m. Prove that m divides n. Hint: Use prime factorizations.
p
6.4.3. Given a,b N, we can write them as products of primes
→
a = pn1pn2 pnk and b = pm1pm2 pmk,
1 2 ··· k 1 2 ··· k
where the p 1 ,...,p k are distinct prime numbers, and the exponents are elements of Z 0 . (We
↓
allow the exponent zero so that we can write the prime factorizations of a and b using the
same set of primes—using an exponent of zero if a particular prime does not appear in one
of the factorizations. This also allows us to consider the case a = 1 or b = 1, in which case
all of the corresponding exponents are zero.) Prove that a divides b if and only if n m
i i
↘
for all 1 i k.
↘ ↘
6.4.4. Suppose p is a prime number. Prove that, for all x Z,
→
3xp2 5xp3
+2x
↓
is divisible by p.
6.4.5. Suppose that a,b N have prime factorizations
→
a = pn1pn2 pnk and b = pm1pm2 pmk,
1 2 ··· k 1 2 ··· k
where the p 1 ,...,p k are distinct prime numbers, and the exponents are elements of Z 0 .
↓
Define
GCD(a,b) = pω1pω2 pωk
1 2 ··· k
where, for 1 i k, we define ϑ to be the minimum of n and m . (Note the di”erence
i i i
↘ ↘
between this and the definition of gcd(a,b).)
(i) Prove that GCD(a,b) divides gcd(a,b). Hint: Use Proposition 6.29(iii).
(ii) Prove that gcd(a,b) divides GCD(a,b). Hint: Use Proposition 6.29(i).
(iii) Prove that GCD(a,b) = gcd(a,b).

Chapter 7
Real numbers
Inthischapter, wewillintroducetherealnumbers. Aswasthecasefortheintegers, youhave
likely encountered real numbers before. However, we will take a more rigorous approach.
Namely, we will start from a precise list of axioms, and we will assume that a set R exists
that satisfies these axioms. Many of the axioms are the same as those we saw for the integers.
However, there are some important di”erences.
7.1 Axioms
We will assume that there is a set, denoted R, with binary operations + (addition) and
·
(multiplication) satisfying Axioms 7.1–7.5, 7.13 and 7.35. The elements of R are called real
numbers.
Axiom 7.1 (Commutativity, associativity, and distributivity). For all x,y,z R, we have
→
(i) x+y = y +x, (commutativity of addition)
(ii) (x+y)+z = x+(y +z), (associativity of addition)
(iii) x (y +z) = x y +x z, (distributivity)
· · ·
(iv) x y = y x, (commutativity of multiplication)
· ·
(v) (x y) z = x (y z). (associativity of multiplication)
· · · ·
As we did for the integers, we will often denote multiplication by juxtaposition. That is,
we will write xy instead of x y.
·
Axiom 7.2 (Additive identity). There exists a real number 0 satisfying x R, x+0 = x.
⇓ →
This element 0 is called an additive identity, or an identity element for addition.
Axiom 7.3 (Multiplicative identity). There exists a real number 1 such that 1 = 0 and
↑
x R, x 1 = x. The element 1 is called a multiplicative identity, or an identity element
⇓ → ·
for multiplication.
Axiom 7.4 (Additive inverse). For each x R, there exists a real number, denoted x,
→ ↓
such that x+( x) = 0. The element x is called an additive inverse of x.
↓ ↓
73

74 Real numbers
Axiom 7.5 (Multiplicative inverse). For each x R 0 , there exists a real number,
→ ↓{ }
denoted x 1, such that x x 1 = 1. The element x 1 is called a multiplicative inverse of x.
↑ ↑ ↑
·
Remark 7.6. Although we use the same notation 0 and 1 for the additive and multiplicative
identities of the real numbers R as we did for the corresponding elements of the integers Z,
these are a priori di”erent elements since we have not discussed any relationship between Z
and R. Later, in Section 8.2, we will discuss how we can view Z as a subset of R, and then
the 0 of Z will correspond to the 0 of R, and similarly for 1. This explains our use of the
same notation.
Proposition 7.7. For each x R 0 , there exists a unique real number y such that
→ ↓{ }
xy = 1.
Proof. Suppose x R 0 . By Axiom 7.5, there exists a real number y such that xy = 1. It
→ ↓{ }
remains to show that this element is unique. Suppose z is another real number such xz = 1.
Then we have
y = y 1 = y(xz) = (yx)z = (xy)z = 1 z = z 1 = z.
· · ·
Thus, the element with the given property is unique.
Proposition 7.7 justifies calling x 1 the (as opposed to a) multiplicative inverse of x.
↑
Corollary 7.8. For x R, x = 0, we have (x
↑
1)↑ 1 = x.
→ ↑
Proof. Suppose x R with x = 0. Then
→ ↑
x 1x = xx 1 = 1.
↑ ↑
Therefore, x is a multiplicative inverse of x 1. Since the multiplicative inverse is unique by
↑
Proposition 7.7, we must have (x
↑
1)↑ 1 = x.
Remark 7.9. Since addition and multiplication of real numbers is associative, we can omit
the parentheses when writing the addition or multiplication of more than two elements. For
instance, if w,x,y,z R, we have unambiguously write expressions like
→
w+x+y +z and wxyz,
since the results of the additions and multiplications is the same no matter how we group
the terms. See Remark 1.29.
Proposition 7.10. For all x,y R 0 , we have (xy) ↑ 1 = x ↑ 1y ↑ 1.
→ ↓{ }
Proof. Suppose x,y R 0 . By Axiom 7.5, x and y have multiplicative inverses x ↑ 1 and
→ ↓{ }
y 1, respectively. We have
↑
(xy) 1xy = 1
↑
= (xy) 1xyy 1 = y 1
↑ ↑ ↑
↔
= (xy) 1x 1 = y 1
↑ ↑
↔ ·
= (xy) 1x = y 1
↑ ↑
↔

Axioms 75
= (xy) 1xx 1 = y 1x 1
↑ ↑ ↑ ↑
↔
= (xy) 1 1 = x 1y 1
↑ ↑ ↑
↔ ·
= (xy) 1 = x 1y 1.
↑ ↑ ↑
↔
Proposition 7.11. Suppose x,y,z R and x = 0. If xy = xz, then y = z.
→ ↑
Proof. Assume x,y,z R, x = 0, and xy = xz. By Axiom 7.5, x has a multiplicative inverse
→ ↑
x 1. Then
↑
xy = xz
= x 1xy = x 1xz
↑ ↑
↔
= xx 1y = xx 1z
↑ ↑
↔
= 1 y = 1 z
↔ · ·
= y 1 = z 1
↔ · ·
= y = z.
↔
Remark 7.12. You should compare Axioms 7.1–7.5 to Axioms 1.1–1.5. Replacing Z by R,
• Axiom 1.1 becomes Axiom 7.1,
• Axiom 1.2 becomes Axiom 7.2,
• Axiom 1.3 becomes Axiom 7.3, and
• Axiom 1.4 becomes Axiom 7.4.
However, Axioms 1.5 and 7.5 are di”erent. Nevertheless, Proposition 7.11 shows us that
Axiom 1.5 holds for R as well (i.e. Axiom 7.5 is stronger than Axiom 1.5). Therefore, any
proposition we proved for Z using only axioms Axioms 1.1–1.5 also holds for R, with an
identical proof. In particular all of the propositions of Section 1.2 hold with Z replaced
by R. We will refer to the R analogues of these propositions by appending “for R”. For
example, we may say “by Proposition 1.9 for R”.
Subtraction. As for the integers, we define subtraction in R by
x y := x+( y), x,y R.
↓ ↓ →
Then Proposition 1.28 also holds with Z replaced by R.
Division. We have not yet discussed division in this course, because division is not very
well behaved for the integers. (More precisely, given two random integers, it is unlikely that
you can divide one by the other and obtain an integer.) However, we can define division in
R. If x,y R and x = 0, we define
→ ↑ y
:= yx 1.
↑
x
Precisely, division is a function
division: R (R 0 ) R, division(y,x) = yx ↑ 1.
∞ ↓{ } ∈

76 Real numbers
Note that
1
= 1 x 1 = x 1.
↑ ↑
x ·
Exercises.
7.1.1. Using only Axioms 7.1–7.5 and the definition of division, show that you can add
“fractions” with common denominators the way you learn in grade school. More precisely,
show that, for all a,b,c R with c = 0,
→ ↑
a b a+b
+ = .
c c c
7.1.2. Suppose a,b,c,d R and b,d = 0. Show that
→ ↑
a c ad+bc
+ = .
b d bd
Show all your steps.
7.1.3. Suppose x R and x = 0. Prove that ( x) ↑ 1 = x ↑ 1
→ ↑ ↓ ↓
7.1.4. Suppose a,b R and b = 0. Prove that
→ ↑
a a a
↓ = = .
b ↓b b
↓
7.1.5. Prove that zero does not have a multiplicative inverse.
7.2 Positive real numbers and ordering
In our discussion of the natural numbers, after introducing Axioms 1.1–1.5 and proving some
propositions that result from these axioms, we added an axiom (Axiom 2.1) that guaranteed
the existence of the set N of natural numbers. This resulted in an ordering on the integers.
We now introduce an analogue of Axiom 2.1 for R. Just as N turned out to be the set of
positive integers, its analogue for R will be the set of positive real numbers.
Axiom 7.13. There exists a subset R>0 R with the following properties:
≃
(i) If x,y R>0 , then x+y R>0 . (The subset R>0 is closed under addition.)
→ →
(ii) If x,y R>0 , then xy R>0 . (The subset R>0 is closed under multiplication.)
→ →
(iii) 0 R>0 .
↑→
(iv) For every x R, we have x R>0 or x = 0 or x R>0 .
→ → ↓ →

Positive real numbers and ordering 77
The elements of R>0 are called positive real numbers. A real number that is neither
positive nor zero is a negative real number.
Note that Axiom 7.13 is the same as Axiom 2.1, but with Z and N replaced by R and
R>0 , respectively.
Proposition 7.14. (i) For x R, one and only one of the following statements is true:
→
• x R>0 ,
→
• x R>0 ,
↓ →
• x = 0.
(ii) We have 1 R>0 .
→
Proof. The proof of part (i) is the same as the proof of Proposition 2.3, but with Z and N
replaced by R and R>0 , respectively. Similarly, the proof of part (ii) is the same as that of
Proposition 2.4.
We now define an ordering on the set of real numbers, just as we did for the integers.
Definition 7.15 (Order on the real numbers). For x,y R, we write x < y (and say x is
→
less than y) or y > x (and say y is greater than x) if and only if
y x R>0 .
↓ →
We write x y (and say x is less than or equal to y) or y x (and say y is greater than or
↘ ↗
equal to x) if and only if
x < y or x = y.
Remark 7.16. Note that Definition 7.15 is the same as Definition 2.5, but with Z and N
replaced by R and R>0 , respectively. Therefore, many of the propositions concerning the
ordering on Z that we proved in Section 2.2 also hold with Z and N replaced by R and
R>0 , with an identical proof. In particular, Propositions 2.6–2.15 all hold for R. Again (see
Remark 7.12) we will refer to the R analogues of these propositions by appending “for R”.
Proposition 7.17. (i) Suppose x
→
R, x
↑
= 0. Then x
→
R>0 if and only if
x
1
→
R>0 .
(ii) Suppose x,y
→
R>0 . If x < y, then 0 <
y
1 <
x
1.
Proof. (i) Suppose x
→
R>0 . By Axiom 7.13(iv), we have
x
1
→
R>0 or
x
1 = 0 or
↓x
1
→
R>0 .
We will show that the latter two cases lead to a contradiction. First assume that 1 = 0.
x
Then
1
1 = x = x 0 = 0,
· x ·
where, in the last equality we used Proposition 1.14 for R. But the equality 1 = 0 contradicts
Axiom 7.3. Next, assume that
↓x
1
→
R>0 . Then
1 1
1 = x = x R>0 ,
↓ ↓ · x · ↓x →
   
by the closure of R>0 under multiplication (Axiom 7.13(ii)). But this contradicts Proposi-
tion 7.14. So we must have
x
1
→
R>0 .
Conversely, suppose x ↑ 1 = x 1 → R>0 . Then, by the above, x = (x ↑ 1) ↑ 1 → R>0 .

78 Real numbers
(ii) Now suppose x,y R>0 satisfy x < y. Then x ↑ 1,y ↑ 1 R>0 by part (i), and hence
→ →
x ↑ 1y ↑ 1 R>0 by the closure of R>0 under multiplication (Axiom 7.13(ii)). Therefore, we
→
have
x < y = x 1y 1x < x 1y 1y = y 1 < x 1,
↑ ↑ ↑ ↑ ↑ ↑
↔ ↔
where, in the first implication, we used Proposition 2.9(iii) for R.
Example 7.18. We will prove that, for all x R,
→
1
x4 < 2x5 x > . (7.1)
⇐↔ 2
Let’s split into two cases: x = 0 and x = 0.
↑
Case 1: Suppose x = 0. Then x4 = 04 = 0 and 2x5 = 2 05 = 0. Thus, the statement
·
x4 < 2x5 is false since 0 < 0. Since the statement 0 > 1 is also false, the double implication
↑ 2
(7.1) is true.
Case 2: Suppose x = 0. Since x4 = (x2)2, Proposition 2.11 for R implies that x4 R>0 .
↑ →
Therefore, (x4) ↑ 1 → R>0 by Proposition 7.17. Similarly, 1 2 → R>0 . Thus
x4 < 2x5 = (x4)
↑
1x4 < (x4)
↑
12x5 (Proposition 2.9(iii) for R)
↔
= 1 < 2x
↔
1 1
= 1 < 2x (Proposition 2.9(iii) for R)
↔ 2 · 2 ·
1
= < x.
↔ 2
For the other implication, we have
1 1
x > = 2x > 2 (Proposition 2.9(iii) for R)
2 ↔ · 2
= 2x > 1
↔
= x4 2x > x4 1 (Proposition 2.9(iii) for R)
↔ · ·
= 2x5 > x4.
↔
For later use, we define
R 0 := R>0 0 = x R : x 0 .
↓ ′{ } { → ↗ }
Exercises.
7.2.1 ([BG10, Prop. 8.41]). Let x R. Prove that x2 < x3 if and only if x > 1.
→

The real numbers versus the integers 79
7.2.2. Recall that we defined 2 := 1+1 Z. Prove that there is no integer n Z such that
→ →
2n = 1. Therefore, unlike R, the set Z of integers does not have multiplicative inverses of
all nonzero elements. Hint: Try a proof by contradiction, using Proposition 2.21.
7.2.3. Suppose x,y R. Prove that
→
xy R>0 (x,y R>0 ) or ( x, y R>0 ).
→ ⇐↔ → ↓ ↓ →
7.2.4. Prove that, for all x R,
→
x2 4 > 0 x < 2 or x > 2.
↓ ⇐↔ ↓
7.2.5. Suppose x,y R and x = 0. Prove that
→ ↑
y
R>0 (x,y R>0 ) or ( x, y R>0 ).
x → ⇐↔ → ↓ ↓ →
7.3 The real numbers versus the integers
As we have discussed, Axioms 1.1–1.4 for Z are identical to Axioms 7.1–7.4. Similarly,
Axiom 2.1 and Axiom 7.13 are identical.
However, Axiom 1.5 (cancellation) and Axiom 7.5 are di”erent. We showed in Proposi-
tion 7.11 that Axiom 7.5 implies Axiom 1.5 (with Z replaced by R). However, the converse
implication is false. For example, the integer 2 does not have a multiplicative inverse in Z.
Thus, Axiom 7.5 does not hold with R replaced by Z. This is therefore a d”eirence between
Z and R.
Another important di”erence between Z and R concerns the ordering. By Proposi-
tion 2.21, the set N of natural numbers has a smallest element, namely 1. The analogous
statement for R is false. Before proving this (Theorem 7.20), we prove a lemma.
Lemma 7.19. We have 0 < 1 < 1.
2
Proof. Since 2 = 1+1 R>0 by the closure of R>0 under addition (Axiom 7.13(i)), it follows
→
from Proposition 7.17(i) that 0 < 1
2
. Since 2
↓
1 = (1+1)
↓
1 = 1
→
R>0 , we have 1 < 2.
Therefore, by Proposition 7.17(ii), we have 1 < 1 = 1.
2 1
Alternate proof: We can also prove that 1 < 1 by contradiction. Suppose 1 1. Then we
2 ↘ 2
have
1
0 < 1 < 2 and 0 < 1 .
↘ 2
By Proposition 2.9(iii) for R, we then have
1
1 1 < 2 = 1 < 1 = 0 = 1 1 R>0 ,
· · 2 ↔ ↔ ↓ →
which contradicts Axiom 7.13(iii).
Theorem 7.20. The set R>0 of positive real numbers does not have a smallest element.

80 Real numbers
Proof. We will prove the result by contradiction. Suppose x is a smallest element of R>0 .
Then (using Lemma 7.19) we have
1
0 < < 1 and 0 < x x.
2 ↘
By Proposition 2.9(iii) for R, we then have
1
x < x.
2 ·
However, by the closure of R>0 under multiplication (Axiom 7.13(ii)), we have 1
2 ·
x
→
R>0 .
This contradicts our assumption that x is a smallest element of R>0 .
Another important di”erence between Z and R concerns “gaps” between numbers. The
integers have gaps. For instance, by Proposition 2.22, there is no integer between 0 and 1.
In contrast, the real numbers have no such gaps, as the following theorem shows.
Theorem 7.21. For all x,y R such that x < y, there exists a z R such that x < z < y.
→ →
Proof. Suppose x,y R satisfy x < y. We will show that z = x+y satisfies x < z < y. First,
→ 2
x+y x+y 1 1 1
z x = 1 x = 2 x = (x+y 2x) = (y x) R>0 ,
↓ 2 ↓ · 2 ↓ 2 · · 2 ↓ 2 ↓ →
by closure of R>0 under multiplication (Axiom 7.13(ii)), since 1
2 →
R>0 (by Lemma 7.19) and
y x R>0 by assumption. Thus x < z. Second,
↓ →
x+y 1 x+y 1 1
y z = 1 y = 2 y = (2y (x+y)) = (y x) R>0 ,
↓ · ↓ 2 2 · · ↓ 2 2 ↓ 2 ↓ →
and so z < y.
The final axiom for Z, Axiom 2.17 has no analogue for R. On the other hand, we will
introduce one final axiom for R which has no analogue for Z.
Exercises.
7.3.1 ([BG10, Proj. 8.44]). Construct a subset A R that satisfies
≃
(i) 1 A and
→
(ii) if n A, then n+1 A,
→ →
yet for which R>0 is not a subset of A.

Upper and lower bounds 81
7.4 Upper and lower bounds
Before introducing our last axiom for R, we begin with some definitions.
Definition 7.22 (Bounded sets, supremum, infimum). Let A R such that A = ⫋.
≃ ↑
(i) The set A is bounded above if there exists b R such that a A, a b. Any real
→ ⇓ → ↘
number b with this property is called an upper bound for A.
(ii) The set A is bounded below if there exists b R such that a A, b a. Any real
→ ⇓ → ↘
number b with this property is called a lower bound for A.
(iii) The set A is bounded if it is both bounded above and bounded below.
(iv) A least upper bound, or supremum, for A is an upper bound that is less than or equal
to every upper bound for A.
(v) A greatest lower bound, or infimum, for A is a lower bound that is greater than or
equal to every lower bound for A.
The next proposition shows that suprema and infima are unique, if they exist.
Proposition 7.23. Suppose A is a nonempty subset of R.
(i) If x and x are least upper bounds for A, then x = x .
1 2 1 2
(ii) If x and x are greatest lower bounds for A, then x = x .
1 2 1 2
Proof. We will prove the first statement, since the proof of the second is analogous. Suppose
x and x are least upper bounds for A. Then, since x is an upper bound for A and x is a
1 2 1 2
least upper bound, we have x x . Similarly, we have x x . Thus x = x .
2 1 1 2 1 2
↘ ↘
For a nonempty subset A of R, the least upper bound (supremum) of A is denoted by
sup(A) (or supA) and the greatest upper bound (infimum) of A is denoted by inf(A) (or
infA). Keep in mind that, for an arbitrary nonempty set A R, infA and/or supA may
≃
not exist, as we will see.
Example 7.24. We will show that infR>0 = 0. Since 0 < x for all x R>0 , we have that 0 is
→
a lower bound for R. It remains to show that 0 is the greatest lower bound. We do this by
contradiction. Suppose y R is a lower bound for R>0 and 0 < y. Then, by Theorem 7.21,
→
there exists z R such that 0 < z < y. But then z R>0 does not satisfy y z. This
→ → ↘
contradicts the fact that y is a lower bound for R>0 .
Example 7.25. We have infR
0
= 0. The proof is almost identical to that of Example 7.24.
↓
Examples 7.24 and 7.25 illustrate an important point: the supremum or infimum of a set
A (if it exists) may or may not be an element of A. In addition, infima and suprema may
not exist, as the following example illustrates.
Proposition 7.26. The set R>0 has no upper bound.

82 Real numbers
Proof. We prove the result by contradiction. Suppose x is an upper bound for R>0 . Then,
since 1 R>0 by Proposition 7.14(ii), we have
→
x 1 > 0 = x > 0 = x R>0 .
↗ ↔ ↔ →
Thus x+1 R>0 by closure of R>0 under addition (Axiom 7.13(i)). Since
→
(x+1) x = 1 R>0 ,
↓ →
we have x+1 > x. This contradicts the assumption that x is an upper bound for R>0 .
Example 7.27. Consider the set
A = x ↑ 1 : x R>0 .
{ → }
We will show that inf(A) = 0.
To prove this, first note that, by Proposition 7.17, x ↑ 1 > 0 for all x R>0 . Thus 0 is a
→
lower bound for A.
Itremainstoshowthatitisthegreatest lowerbound. Wewillprovethisbycontradiction.
Suppose y is another lower bound such that 0 < y. Then, by Theorem 7.21, there exists
z R such that 0 < z < y. Let x = z ↑ 1. Then, by Proposition 7.17, x R>0 and so, by
→ →
Corollary 7.8, we have z = x 1 A. But this contradicts the assumption that y is a lower
↑
→
bound for A (since z < y). Therefore, 0 = inf(A).
Example 7.28. Let us find the supremum of the set
3
A = 2 : x R>0 .
↓ x →
 
We will prove that
supA = 2.
To prove this, we first show that 2 is a upper bound for A. Indeed
x R>0 = x > 0
→ ↔
1
= > 0 (Prop. 7.17(i))
↔ x
3
= ↓ < 0 (Prop. 2.9(iv) for R)
↔ x
3
= 2 < 2. (Prop. 2.9(i) for R)
↔ ↓ x
Since every element of A is of the form 2
↓ x
3 for some x
→
R>0 , the above argument implies
that 2 is an upper bound for A.
Now we must show that 2 is the least upper bound for A. We prove this by contradiction.
Suppose A has an upper bound b with b < 2. Thus 2 b R>0 . Since b is an upper bound
↓ →
for A, we have, for all x R>0 ,
→
3 3
2 < b = > 2 b
↓ x ↔ x ↓

Upper and lower bounds 83
x 1
= < (Prop. 7.17(ii))
↔ 3 2 b
↓
3
= x < . (Prop. 2.9(iii))
↔ 2 b
↓
This implies that R>0 is bounded above by
2
3
b
, contradicting Proposition 7.26.
↑
Example 7.29. Let us show that the set
3
A = 2 : x R>0 .
↓ x →
 
of Example 7.28 has no lower bound, and hence no infimum. We prove this by contradiction.
Suppose b were a lower bound for A. Then, in particular, we have b 2 3 < 2. So
↘ ↓ 4
3
b 2 for all x R>0
↘ ↓ x →
3
= 2 b for all x R>0
↔ x ↘ ↓ →
3
= x for all x R>0 . (since x R>0 , 2 b R>0 )
↔ 2 b ↘ → → ↓ →
↓
However, since
2
3
b
> 0, we can find x
→
R>0 such that x <
2
3
b
by Theorem 7.20. Thus we
have arrived at a↑contradiction, as desired. ↑
Examples 7.30. (i) The set x R : x < 0 has supremum 0, but no infimum.
{ → }
(ii) The set x R : x 0 has supremum 0, but no infimum.
{ → ↘ }
(iii) The set R has no supremum and no infimum.
(iv) The set x R : 0 x 1 has infimum 0 and supremum 1.
{ → ↘ ↘ }
(v) The set x R : 0 < x 1 has infimum 0 and supremum 1.
{ → ↘ }
(vi) The set x Z : 0 < x has infimum 1, but no supremum. (Technically speaking, we
{ → }
have not defined infima and suprema for subsets of Z, but the definitions are the same.
Furthermore, we will discuss in Section 8.2 how we can view Z as a subset of R.)
Definition 7.31 (Maximum, minimum). Suppose A R.
≃
(i) An element b A is the maximum or largest element of A if a A, a b. If this is
→ ⇓ → ↘
the case, we write b = max(A).
(ii) An element b A is the minimum or smallest element of A if a A, b a. If this
→ ⇓ → ↘
is the case, we write b = min(A).
Note the important di”erence between Definition 7.31 and parts (i) and (ii) of Defini-
tion 7.22. In the definition of upper/lower bounds, the bound is an element of R, whereas
in Definition 7.31, the maximum/minimum element is required to be an element of the set
A itself.

84 Real numbers
Proposition 7.32. Suppose A R is nonempty.
≃
(i) If A has a supremum and sup(A) A, then A also has a largest element and sup(A) =
→
max(A). Conversely, if A has a largest element then A has a supremum, max(A) =
sup(A), and sup(A) A.
→
(ii) If A has an infimum and inf(A) A, then A also has a smallest element and inf(A) =
→
min(A). Conversely, if A has a smallest element then A has an infimum, min(A) =
inf(A), and inf(A) A.
→
Proof. We will prove the first statement, since the proof of the second is analogous. Suppose
Ahasasupremumbandb A. Then, bythedefinitionofsupremum, wehave a A, a b.
→ ⇓ → ↘
Thus b = max(A).
Conversely, suppose A has a largest element b. Then b A and a A, a b. Thus
→ ⇓ → ↘
b is an upper bound for A. We prove that b is a supremum by contradiction. Suppose that
b is not the least upper bound. Then there exists an upper bound c for A with c < b. But
since b A, this contradicts the fact that c is an upper bound for A. Therefore, b must be
→
the least upper bound of A, i.e. b = sup(A). Therefore sup(A) = b = max(A) A.
→
Proposition7.32essentiallysaysthatgreatestelementsofasetAaresimplysupremathat
are contained in A. Similarly smallest elements of A are simply infima that are contained
in A. It follows from this and Proposition 7.23 that greatest and smallest elements, if they
exist, are unique.
Example 7.33. Consider the set
3
A = 2 : x R>0 .
↓ x →
 
of Examples 7.28 and 7.29.
We showed in Example 7.28 that supA = 2. By Proposition 7.32(i), if A had a largest
element, it would be 2. But 2 / A since, as shown in Example 7.28, all elements of A are
→
strictly less than 2. Thus A does not have a largest element.
In addition, we showed in Example 7.29 that A does not have an infimum. Thus, by
Proposition 7.32(ii), it also does not have a smallest element.
Examples 7.34. Let us take another look at the sets of Examples 7.30.
(i) The set x R : x < 0 has no maximum and no minimum.
{ → }
(ii) The set x R : x 0 has maximum 0 and no minimum.
{ → ↘ }
(iii) The set R has no maximum and no minimum.
(iv) The set x R : 0 x 1 has minimum 0 and maximum 1.
{ → ↘ ↘ }
(v) The set x R : 0 < x 1 has maximum 1 and no minimum.
{ → ↘ }
Here is our final axiom for the real numbers.

Upper and lower bounds 85
Axiom 7.35 (Completeness axiom). Every nonempty subset of R that is bounded above
has a least upper bound.
Proposition 7.36. Suppose that A B R, that A and B are nonempty, and that B is
≃ ≃
bounded above. Then sup(A) sup(B).
↘
Proof. Since B is bounded above and A B, we know that A is also bounded above. Thus,
≃
by Axiom 7.35, sup(A) and sup(B) exist. By definition, we have b sup(B) for all b B.
↘ →
Since A B, this implies that a sup(B) for all a A. Therefore, sup(B) is an upper
≃ ↘ →
bound for A. Since sup(A) is the least upper bound, we have sup(A) sup(B).
↘
We now define intervals. For x,y R, we define
→
[x,y] := z R : x z y ,
{ → ↘ ↘ }
(x,y] := z R : x < z y ,
{ → ↘ }
[x,y) := z R : x z < y ,
{ → ↘ }
(x,y) := z R : x < z < y ,
{ → }
( ,y] := z R : z y ,
↓∃ { → ↘ }
( ,y) := z R : z < y ,
↓∃ { → }
[x, ) := z R : x z ,
∃ { → ↘ }
(x, ) := z R : x < z ,
∃ { → }
( , ) := R.
↓∃ ∃
Remark 7.37. (i) Note that and are not real numbers. We are using these symbols
∃ ↓∃
just as part of the notation.
(ii) The text [BG10] requires that x < y for the above intervals. However, this is not
necessary. For instance, when x = y, we have
[x,x] = x , [x,x) = (x,x] = (x,x) = ⫋,
{ }
and when x > y, we have
[x,y] = [x,y) = (x,y] = (x,y) = ⫋.
(iii) We use the same notation for the interval (x,y) and the point (x,y) R 2, so there is
→
some potential chance for confusion. It should be clear from the context whether we
are referring to an interval or a point in R 2.
Proposition 7.38. Every nonempty subset of R that is bounded below has a greatest lower
bound.
Proof. Suppose A is a nonempty subset of R that is bounded below. Therefore, there exists
an m R such that x A, m x. Define
→ ⇓ → ↘
B = x : x A .
{↓ → }

86 Real numbers
We will show that B is bounded above by m. Indeed,
↓
x B = x A = m x = x m.
→ ↔ ↓ → ↔ ↘ ↓ ↔ ↘ ↓
Thus, x B,x m, as desired. Therefore, by Axiom 7.35, B has a least upper bound y.
⇓ → ↘ ↓
We will show that y is a greatest lower bound for A. Since
↓
x A = x B = x y = x y,
→ ↔ ↓ → ↔ ↓ ↘ ↔ ↗ ↓
we see that y is a lower bound for A. It remains to show that y is the greatest lower
↓ ↓
bound for A. Suppose z is another lower bound for A. Then, as above, z is an upper
↓
bound for B. Since y is the least upper bound for B, we have y z. Therefore y z.
↘ ↓ ↓ ↗
It follows that y is a greatest lower bound for A.
↓
Exercises.
7.4.1. Suppose that A R has supremum M. Show that the set
≃
B = 5 2x : x A
{ ↓ → }
has infimum 5 2M.
↓
7.4.2. Suppose A and B are nonempty subsets of R that are bounded above. Furthermore,
suppose that A B = ⫋. Show that A B is bounded above and that
∝ ↑ ∝
sup(A B) min supA,supB .
∝ ↘ { }
7.4.3. SupposeAisasubsetofRwithamaximumandminimumelement, suchthatmaxA =
minA. Prove that A has exactly one element.
7.4.4. Suppose a,b R with a < b. Prove that
→
inf(a,b) = a and sup(a,b) = b.
(Recall that (a,b) = x R : a < x < b .)
{ → }
7.4.5. Find the supremum and infimum of the set
x R : x2 < 4
{ → }
or show that they do not exist.

Chapter 8
Injections, surjections, and bijections
In this chapter will we examine some important types of functions. Namely we will consider
functions that are injective, surjective, or both. We will then discuss how we can identify
the set of integers as a subset of the set of real numbers in a way that preserves all of the
important operations and relations that we have discussed.
8.1 Injections, surjections, and bijections
Definition 8.1 (Injective, injection). A function f: A B is said to be injective (or to be
∈
an injection, or to be one-to-one) if
x,y A, x = y = f(x) = f(y).
⇓ → ↑ ↔ ↑
Equivalently (taking the contrapositive) f is injective if
x,y A, f(x) = f(y) = x = y.
⇓ → ↔
Example 8.2. If c R, c = 0, then the function
→ ↑
f: R R, f(x) = cx,
∈
is injective. To prove this, suppose x,y R. Then
→
f(x) = f(y) = cx = cy = x = y,
↔ ↔
where the last implication follows from Proposition 7.11 (alternatively, multiply both sides
by c 1). Thus f is injective.
↑
Example 8.3. The function
f: R R, f(x) = x2,
∈
is not injective. To prove that a function f is not injective, it is enough to find two elements
x and y of the domain such that x = y and f(x) = f(y). In this case, we have 1 = 1, but
↑ ↑ ↓
f(1) = 1 = f( 1). Thus f is not injective.
↓
87

88 Injections, surjections, and bijections
Definition 8.4 (Surjective, surjection, image). A function f: A B is surjective (or is a
∈
surjection, or is onto) if
b B a A such that f(a) = b.
⇓ → ⇑ →
For any subset S A, the image of S under f is the set
≃
f(S) := f(a) : a S B.
{ → }≃
The image of f is f(A). In other words, the image of f is the image of the domain of f
under f. Thus, f is surjective if and only if f(A) = B (i.e. the image of f is equal to the
codomain of f).
Example 8.5. The function
f: Z 0 N, f(x) = x ,
↓{ }∈ | |
is surjective. To prove this, note that, for all x N, we have f(x) = x = x.
→ | |
Definition 8.6 (Bijective, bijection). A function is bijective (or is a bijection) if it is both
injective and surjective.
Example 8.7. For any nonempty set A, we have the identity function
id : A A, id (a) = a for all a A.
A A
∈ →
This function is bijective.
Example 8.8. Consider the function
x
f: R R, f(x) = +1.
∈ 3
We will show that this function is bijective. Suppose x,y R. Then
→
x y x y
f(x) = f(y) = +1 = +1 = +1 1 = +1 1
↔ 3 3 ↔ 3 ↓ 3 ↓
x y x y
= = = 3 = 3 = x = y.
↔ 3 3 ↔ · 3 · 3 ↔
So f is injective.
It remains to prove that f is surjective. Let y R. We wish to find x R such that
→ →
f(x) = y. Note that
x
f(x) = y +1 = y x = 3(y 1).
⇐↔ 3 ⇐↔ ↓
Since 3(y 1) R (by closure of R under addition and multiplication), it lies in the domain
↓ →
of f. We have
3(y 1)
f 3(y 1) = ↓ +1 = y 1+1 = y.
↓ 3 ↓
Therefore f is surjective.! "

Injections, surjections, and bijections 89
Examples 8.9. (i) The function f: 0 2,5, 4 given by f(0) = 4, is injective but
{ }∈{ ↓ } ↓
not surjective.
(ii) The function f: 1,2 1 given by f(1) = f(2) = 1 is surjective but not injective.
{ }∈{ }
(iii) The function f: 1,2 1,8 given by f(1) = f(2) = 8 is neither surjective nor
{ }∈{ }
injective.
(iv) The function f: 1,1 2,13 given by f( 1) = 2, f(1) = 13, is bijective.
{↓ } ∈ {↓ } ↓ ↓
(v) The function f: Z Z 0 , f(n) = n2, is not injective since, for example f(1) = 1 =
∈ ↓
f( 1). Itisalsonotsurjective, since,forexample, thereisnon Zsuchthatf(n) = 3.
↓ →
(vi) The function f: Z 0 Z 0 , f(n) = n2, is injective but not surjective.
↓ ∈ ↓
(vii) The function f: R 0 R 0 , f(x) = 3x, is bijective.
↓ ∈ ↓
(viii) The function f: R 0 R 0 , f(x) = 3x + 1 is injective, but not surjective. (For
↓ ∈ ↓
instance, its image does not contain 0.)
If f: A B and g: B C, then their composite is the function
∈ ∈
g f: A C, (g f)(a) = g(f(a)) for all a A.
¬ ∈ ¬ →
Composition is the operation that takes two functions and returns their composite (i.e. the
composite function is the result of composition).
Example 8.10. Define
f: 1,2,3 2,4 , f(1) = f(2) = 4, f(3) = 2,
{ }∈{ }
g: 2,4 1,8,10 , g(2) = 8, g(4) = 10.
{ }∈{ }
Then
g f: 1,2,3 1,8,10
¬ { }∈{ }
is given by
(g f)(1) = g(f(1)) = g(4) = 10,
¬
(g f)(2) = g(f(2)) = g(4) = 10,
¬
(g f)(3) = g(f(3)) = g(2) = 8.
¬
Example 8.11. If f: A B, then
∈
id f = f and f id = f.
B A
¬ ¬
Proposition 8.12. Suppose f: A B and g: B C. So g f: A C.
∈ ∈ ¬ ∈
(i) If f and g are both injective, then g f is injective.
¬
(ii) If f and g are both surjective, then g f is surjective.
¬

90 Injections, surjections, and bijections
(iii) If f and g are both bijective, then g f is bijective.
¬
Proof. (i) Suppose f and g are both injective. For a ,a A, we have
1 2
→
(g f)(a ) = (g f)(a )
1 2
¬ ¬
= g(f(a )) = g(f(a ))
1 2
↔
= f(a ) = f(a ) since g is injective
1 2
↔
= a = a . since f is injective
1 2
↔
(ii) Suppose f and g are both surjective. Let c C. Since g is surjective, there exists
→
b B such that g(b) = c. Then, since f is surjective, there exists a A such that f(a) = b.
→ →
Then
(g f)(a) = g(f(a)) = g(b) = c.
¬
Thus, for all c C, there exists a A such that (g f)(a) = c. So g f is surjective.
→ → ¬ ¬
(iii) This follows from the previous two parts, by the definition of bijectivity.
Definition 8.13 (Inverse functions). Suppose f: A B.
∈
(i) A left inverse of f is a function g: B A such that
∈
g f = id .
A
¬
(ii) A right inverse of f is a function g: B A such that
∈
f g = id .
B
¬
(iii) A two-sided inverse (or simply inverse) of f is a function that is both a left inverse
and a right inverse of f.
Example 8.14. Consider the functions
f: Z 0 Z, f(x) = x,
↓ ∈
g: Z Z 0 , g(x) = x .
∈ ↓ | |
Then, for all x Z 0 , we have
→ ↓
(g f)(x) = g(f(x)) = g(x) = x = x.
¬ | |
Thus
g f = id ,
¬ Z 0
→
and so g is a left inverse of f and f is a right inverse of g. However, f g = id since, for
¬ ↑ Z
example
(f g)( 1) = f(g( 1)) = f(1) = 1 = 1 = id ( 1).
¬ ↓ ↓ ↑ ↓ Z ↓
Therefore, g is not a right inverse of f and f is not a left inverse of g.

Injections, surjections, and bijections 91
Example 8.15. Consider the functions
f: R R, f(x) = 3x+1,
∈
x 1
g: R R, g(x) = ↓ .
∈ 3
Then
f g = id and g f = id .
¬ R ¬ R
Thus f is an inverse of g and g is an inverse of f.
Proposition 8.16. Suppose f is a function.
(i) The function f is injective if and only if f has a left inverse.
(ii) The function f is surjective if and only if f has a right inverse.
(iii) The function f is bijective if and only if f has an inverse.
Proof. (i) Suppose f: A B is injective. Fix an a A and define a function g: B A
0
∈ → ∈
by
a if b is in the image of f and f(a) = b,
g(b) =
-a
0
otherwise.
The function g is well-defined since f is injective, so if b is in the image of f, there is exactly
one a A such that f(a) = b. By construction we have g f = id , and so g is a left inverse
A
→ ¬
of f.
Conversely, assume that f: A B has a left inverse g: B A. Then, for a ,a A, we
1 2
∈ ∈ →
have
f(a ) = f(a ) = g(f(a )) = g(f(a )) = (g f)(a ) = (g f)(a )
1 2 1 2 1 2
↔ ↔ ¬ ¬
= id (a ) = id (a ) = a = a .
A 1 A 2 1 2
↔ ↔
Thus, f is injective.
(ii) Suppose f: A B is surjective. We define a function g: B A as follows. For
∈ ∈
each b B, choose an a A such that f(a) = b (which we can do since f is surjective) and
→ →
define g(b) = a. Then, for all b B, we have
→
(f g)(b) = f(g(b)) = f(a) = b,
¬
and so g is a right inverse of f.
Conversely, suppose that f: A B has a right inverse g: B A. Then, for all b B, we
∈ ∈ →
have
f(g(b)) = (f g)(b) = id (b) = b,
B
¬
and so b is in the image of f. Since b was arbitrary, this proves that f is surjective.

92 Injections, surjections, and bijections
(iii) Suppose f: A B is bijective. Then we can define a function g: B A as follows.
∈ ∈
For each b, there exists exactly one a A such that f(a) = b (since f is bijective). We define
→
g(b) = a. Then, by construction, (f g)(b) = b for all b B, and (g f)(a) = a for all a A.
¬ → ¬ →
So g is an inverse of f.
Conversely, suppose that f has an inverse. Then f is injective by (i) and surjective by (ii).
Hence f is bijective.
Proposition 8.17. Suppose f has left inverse g and right inverse h. Then g = h, and so f
is invertible with inverse g.
Proof. Suppose f: A B has left inverse g: B A and right inverse h: B A. Then
∈ ∈ ∈
g = g id = g f h = id h = h.
B A
¬ ¬ ¬ ¬
Corollary 8.18. If a function is bijective, then its inverse is unique.
Proof. Suppose f has two inverses g and h. Then g is a left inverse of f and h is a right
inverse of f. Thus, the result follows from Proposition 8.17.
Proposition 8.19. Suppose A and B are sets. There exists an injection from A to B if and
only if there exists a surjection from B to A.
Proof. Suppose f: A B is an injection. Then, by Proposition 8.16(i), f has a left inverse
∈
g: B A. So
∈
g f = id . (8.1)
A
¬
This implies that g has a right inverse, and thus g is surjective by Proposition 8.16(ii).
Similarly, if g: B A is surjective, then g has a right inverse f: A B satisfying (8.1).
∈ ∈
Thus f has a left inverse, hence f is injective.
Exercises.
8.1.1. Define the function
g: R 0 R, g(x) = 3x+4.
↓ ∈ ↓
(i) Prove that g is injective.
(ii) What is the image of g? Write your answer as an interval and justify your answer.
(iii) Is g surjective?
8.1.2. Consider the function
f: R R 0 , f(x) = 2x+3 .
∈ ↓ | |

Injections, surjections, and bijections 93
(i) Is f injective? Justify your answer.
(ii) Is f surjective? Justify your answer.
(iii) Does f have a left inverse? If it does, give one and show that it is indeed a left inverse.
Otherwise, justify why f does not have a left inverse.
(iv) Does f have a right inverse? If it does, give one and show that it is indeed a right
inverse. Otherwise, justify why f does not have a right inverse.
8.1.3. Consider the function
x
f: R 0 R 0 , f(x) = +1.
↓ ∈ ↓ 3
(i) Is f injective? Justify your answer.
(ii) Is f surjective? Justify your answer.
(iii) Does f have a left inverse? If it does, give one and show that it is indeed a left inverse.
Otherwise, justify why f does not have a left inverse.
(iv) Does f have a right inverse? If it does, give one and show that it is indeed a right
inverse. Otherwise, justify why f does not have a right inverse.
8.1.4. (i) Suppose f: A B and g: B C are functions, and that g is surjective. Does
∈ ∈
it follow that g f is surjective? If yes, give a proof. If not, give a counterexample.
¬
(ii) Suppose f: A B and g: B C are functions, and that f is injective. Does it follow
∈ ∈
that g f is injective? If yes, give a proof. If not, give a counterexample.
¬
(iii) Suppose f: A B and g: B C are functions such that g f is injective. Does it
∈ ∈ ¬
follow that f is injective? If yes, give a proof. If not, give a counterexample.
(iv) Suppose f: A B and g: B C are functions such that g f is surjective. Does it
∈ ∈ ¬
follow that g is surjective? If yes, give a proof. If not, give a counterexample.
8.1.5. Suppose that A and B are nonempty subsets of R, and that f: A B is a function
∈
satisfying
a ,a A, a < a = f(a ) < f(a ) .
1 2 1 2 1 2
⇓ → ↔
(Such a function is said to be strictly increasing.) Prove that f is injective.
! "
8.1.6. (i) Give an example of a function with two di”erent left inverses.
(ii) Give an example of a function with two di”erent right inverses.
8.1.7. (i) Suppose f: A B and g: B C both have left inverses. Prove that g f has
∈ ∈ ¬
a left inverse.
(ii) Suppose f: A B and g: B C both have right inverses. Prove that g f has a
∈ ∈ ¬
right inverse.
(iii) Suppose f: A B and g: B C both have inverses. Prove that g f has an inverse.
∈ ∈ ¬

94 Injections, surjections, and bijections
8.2 Embedding Z in R
We introduced the set Z of integers and the set R of real numbers axiomatically. That is,
we assumed that there existed sets with binary operations of addition and multiplication
satisfying certain axioms. Because of this approach, there is a priori no connection between
Z and R. For example, the additive identity of Z is not related to the additive identity of
R (and similarly for the multiplicative identities). For this reason, in this section we will
denote the additive and multiplicative identities of Z by 0 and 1 , and the additive and
Z Z
multiplicative identities of R by 0 and 1 .
R R
We will now briefly outline how we can view Z as a subset of R in a way that respects
the operations of addition and multiplication. Further details can be found in [BG10, §9.2].
Definition 8.20 (Embedding of Z in R). We define a function e: Z R as follows:
∈
(i) WefirstdefineeonZ
0
recursively. Wedefine e(0
Z
) = 0
R
and, assuminge(n)isdefined
↓
for some n Z 0 , we define
→ ↓
e(n+1 ) := e(n)+1 .
Z R
(ii) Then we define e on negative integers. For k Z with k < 0, we define
→
e(k) := e( k).
↓ ↓
Proposition 8.21. The function e: Z R defined in Definition 8.20 has the following
∈
properties.
(i) e(1 ) = 1 .
Z R
(ii) For all k Z, e( k) = e(k). (The function e preserves additive inverses.)
→ ↓ ↓
(iii) For all m,k Z, we have e(m+k) = e(m)+e(k). (The function e preserves addition.)
→
(iv) For all m,k Z, we have e(mk) = e(m)e(k). (The function e preserves multiplica-
→
tion.)
(v) For all m,k Z, we have m < k e(m) < e(k). (The function e preserves order.)
→ ⇐↔
(vi) e is injective.
Proof. See [BG10, §9.2].
By Proposition 8.21, the image e(Z) of e is a subset of R that behaves exactly like Z.
In other words, e is a bijection between Z and a subset of R, and this bijection preserves
addition, multiplication, additive inverses, and order. Therefore, from now on, we will
identify Z with this subset of R by identifying n Z with e(n) R. In this way, we will
→ →
think of Z as being a subset of R.

Chapter 9
Limits
In this chapter, we introduce and discuss the concept of a limit. This is a crucial concept
in mathematics, especially in the field of analysis, which includes d”ierential and integral
calculus. While limits are often treated in a intuitive way in calculus courses, we will work
with the precise definition.
9.1 Unboundedness of the integers
InProposition2.7,wesawthatNhasnolargestelement. However,thatdoesnotimmediately
imply that N is not bounded above as a subset of R, since we have not yet ruled out the
possibility that there is some real number that is larger than all natural numbers.
Proposition 9.1. The set N of natural numbers, considered as a subset of R, is not bounded
above.
Proof. We prove the result by contradiction. Suppose N is bounded above. Then, by Ax-
iom 7.35, N has a least upper bound u. Consider the interval
1 1
u ,u = x R : u < x u .
↓ 2 → ↓ 2 ↘
   
If this interval did not contain any natural number, then u 1 would be an upper bound
↓ 2
for N, contradicting the assumption that u is a least upper bound. So there is some n N
→
such that n (u 1,u]. Then
→ ↓ 2
1 1
u < n = u < n+ < n+1.
↓ 2 ↔ 2
However, n + 1 N, since 1 N (by Proposition 2.4) and N is closed under addition
→ →
(Axiom 2.1(i)), this contradicts our assumption that u is an upper bound.
Corollary 9.2. The set Z of integers is neither bounded above nor bounded below.
Proof. Since N Z, any upper bound for Z would also be an upper bound for N, contra-
≃
dicting Proposition 9.1.
95

96 Limits
Nowsuppose, towards acontradiction, thatZ isbounded belowby b. Then, for all n N,
→
we have
n Z = b n = n b,
↓ → ↔ ↘ ↓ ↔ ↘ ↓
and so N would be bounded above by b, again contradicting Proposition 9.1.
↓
Proposition 9.3. For every ω
→
R>0 , there exists n
→
N such that
n
1 <ω .
Proof. Suppose ω
→
R>0 . Then 1
ε →
R>0 by Proposition 7.17(i). Therefore, by Propo-
sition 9.1, there exist n N such that n > 1. Then, by Proposition 7.17(ii), we have
→ ε
1 <ω .
n
Exercises.
9.1.1. Consider the set
3
A = 5+ : n N
2n →
 
(i) Find the infimum of A or prove that it does not exist.
(ii) Find the minimum element of A or prove that it does not exist.
(iii) Find the maximum element of A or prove that it does not exist.
(iv) Find the supremum of A or prove that it does not exist.
9.2 Absolute value
We define the absolute value of real numbers just as we did for the integers in Section 6.1.
Namely, for x R, we define
→
x, if x 0,
x = ↗
| | - x, if x < 0.
↓
So x R 0 for all x R.
| |→ ↓ →
Proposition 9.4. For all x,y R 0 , we have
→ ↓
x < y x2 < y2.
⇐↔
Proof. Let x,y R 0 .
→ ↓
First suppose that x < y so that y x R>0 . If x = 0, this implies that y R>0 , and
↓ → →
thus
y2 > 0 = x2

Absolute value 97
by Axiom 7.13(ii). On the other hand, if x > 0, then we have y > x > 0, and so x+y R>0
→
by Axiom 7.13(i). Thus
y2 x2 = (y x)(y +x) R>0
↓ ↓ →
by Axiom 7.13(ii). So x2 < y2.
Conversely, suppose that x2 < y2, so that
(y x)(y +x) = y2 x2 R>0 .
↓ ↓ →
We cannot have x = y = 0, since this would imply x2 = 0 = y2. Thus, at least one of x and
y is positive, and hence x+y R>0 . Thus
→
y2 x2
y x = ↓ R>0 ,
↓ y +x →
and so x < y.
Proposition 9.5. For all x R, we have x 2 = x2.
→ | |
Proof. This proof is left as an exercise (Exercise 9.2.1).
Proposition 9.6. For all x,y R, we have:
→
(i) x = 0 if and only if x = 0,
| |
(ii) xy = x y ,
| | | || |
(iii) x x x ,
↓| |↘ ↘| |
(iv) x+y x + y (the triangle inequality),
| |↘| | | |
(v) if y < x < y, then x < y .
↓ | | | |
Proof. (i) See [BG10, Prop. 10.8(i)].
(ii) If x,y 0, then xy 0, and so
↗ ↗
xy = xy = x y .
| | | || |
If x 0 and y < 0, then xy 0 and so
↗ ↘
xy = xy = x( y) = x y .
| | ↓ ↓ | || |
The remaining cases, where x < 0, y 0, and where x,y < 0 are similar and are left
↗
as an exercise.
(iii) If x 0, then x = x and so
↗ | |
x = x 0 x = x = x x x .
↓| | ↓ ↘ ↘ | | ↔ ↓| |↘ ↘| |
On the other hand, if x < 0, then x = x and so
| | ↓
x = ( x) = x < 0 x = x x x .
↓| | ↓ ↓ ↘| | ↔ ↓| |↘ ↘| |

98 Limits
(iv) We have
x+y 2 = (x+y)2 (by Proposition 9.5)
| |
= x2 +2xy +y2
= x 2 +2xy + y 2 (by Proposition 9.5)
| | | |
x 2 + 2xy + y 2 (by part (iii))
↘| | | | | |
= x 2 +2 x y + y 2 (by part (ii))
| | | || | | |
= ( x + y )2.
| | | |
Thus, by Proposition 9.4, we have x+y x + y .
| |↘| | | |
(v) Suppose y < x < y. Then, in particular, we have y < y, which implies that y > 0
↓ ↓
and so y = y. If x 0, then
| | ↗
x = x < y = y .
| | | |
On the other hand, if x < 0, then
x = x < y = y ,
| | ↓ | |
where the inequality x < y follows from the assumption that y < x.
↓ ↓
Proposition 9.7. Suppose x R satisfies 0 x 1. Furthermore suppose m,n N such
→ ↘ ↘ →
that m n. Then xm xn.
↗ ↘
Proof. Let 0 x 1 and fix n N. Let P(m) be the statement
↘ ↘ →
xm xn.
↘
We will prove by induction on m that P(m) is true for all m n.
↗
The base case, when m = n is clearly true since xn xn. Now suppose k n and P(k)
↘ ↗
is true. Since 0 x 1, we have xn x xn 1 = xn. So
↘ ↘ · ↘ ·
xk+1 = xk x xn x xn,
· ↘ · ↘
where the first inequality follows from the induction hypothesis.
Exercises.
9.2.1. Prove Proposition 9.5. Hint: Consider the two cases x < 0 and x 0.
↗
9.2.2 ([BG10, Prop. 10.7]). Let x,y R. Prove that x < y if and only if x2 < y2.
→ | | | |
9.2.3. Prove that for all n N and x 1 ,x 2 ,...,x n R,
→ →
n n
x x .
i i
  ↘ | |
) i=1  ) i=1
 
 
 

Distance 99
9.3 Distance
In this section, we briefly discuss the idea of the distance between two real numbers. For
x,y R, we define the distance between x and y to be x y . This matches our intuition
→ | ↓ |
of thinking of real numbers as points on the real line.
Proposition 9.8 (Properties of distance). Suppose x,y,z R.
→
(i) x y = 0 x = y. (Distance satisfies the separation property.)
| ↓ | ⇐↔
(ii) x y = y x . (Distance is symmetric.)
| ↓ | | ↓ |
(iii) x z x y + y z . (The triangle inequality.)
| ↓ |↘| ↓ | | ↓ |
(iv) x y x y .
| ↓ |↗ | |↓| |
Proof. (i) ByProposition 9.6(i), we have
 
x y = 0 x y = 0 x = y.
| ↓ | ⇐↔ ↓ ⇐↔
(ii) By Proposition 9.6(ii), we have
x y = ( 1)(y x) = 1 y x = 1 y x = y x .
| ↓ | | ↓ ↓ | |↓ || ↓ | ·| ↓ | | ↓ |
(iii) By Proposition 9.6(iv), we have
x z = (x y)+(y z) x y + y z .
| ↓ | | ↓ ↓ |↘| ↓ | | ↓ |
(iv) Switching the roles of x and y if necessary, we may assume that x y . Then
| |↗| |
x y = x y . Taking z = 0 in part (iii), we have
| |↓| | | |↓| |
  x = x 0 x y + y 0 = x y + y ,
  | | | ↓ |↘| ↓ | | ↓ | | ↓ | | |
and so
x y x y = x y .
| ↓ |↗| |↓| | | |↓| |
 
 
Proposition 9.9. Let z R 0 . Then
→ ↓
z = 0 ω R>0 , z <.ω
⇐↔ ⇓ →
Proof. If z = 0, then z <ω for all ω R>0 . Now assume z = 0. Then z > 0. Thus,
→ ↑
by Theorem 7.21, there exists an ω R, such that 0 <ω< z . Therefore, the statement
→
ω R>0 , z <ω is false.
⇓ →
Corollary 9.10. For x,y R, we have
→
x = y ω> 0, x y <ω.
⇐↔ ⇓ | ↓ |
Proof. We have
x = y x y = 0 (Proposition 9.8(i))
⇐↔ | ↓ |
ω> 0, x y <ω. (Proposition 9.9 with z = x y )
⇐↔ ⇓ | ↓ | | ↓ |

100 Limits
Exercises.
9.3.1. Prove that, for all x,y R, we have x y x + y .
→ | ↓ |↘| | | |
9.3.2. Suppose z R 0 . Prove that
→ ↓
1
z = 0 n N, z < .
⇐↔ ⇓ → n
9.4 Limits
We are now ready to give the precise definition of the limit of a sequence.
Definition 9.11 (Limit of a sequence). Let (x k ) →k=1 be a sequence in R and L
→
R. We say
that (x ) converges to L if
k →k=1
ω> 0, N N such that n N, x n L <ω,
⇓ ⇑ → ⇓ ↗ | ↓ |
or, equivalently, if
ω> 0, N N such that n N = x n L <ω .
⇓ ⇑ → ↗ ↔| ↓ |
! "
When (x ) converges to L, we call L the limit of the sequence (x ) and we write
k →k=1 k
lim x = L.
k
k
≃→
We say that a sequence converges if there exists some L such that the sequence converges to
L. If no such L exists, then we say the sequence diverges. Thus, the sequence (x ) diverges
k
if
L R ω> 0 such that N N n N such that x n L ω.
⇓ → ⇑ ⇓ → ⇑ ↗ | ↓ |↗
It can take some time to get used to the formal definition of a limit, but it is important
that you master this concept. Intuitively, the sequence (x ) converges to L if, given any
k
distance ω, the terms of sequence are eventually within a distance ω of L.
Proposition 9.12. We have
1
lim = 0.
k k
≃→
Proof. Let ω> 0. By Proposition 9.1, there exists N N with N > 1. Then, for all n N,
→ ε ↗
we have
1 1 1
0 = <ω
n ↓ n ↘ N
 
 
Hence lim 1 = 0.  
k k  
≃→

Limits 101
Example 9.13. We will prove that
2k 3
lim ↓ = 2.
k k
≃→
First note that, for n > 0, we have
2n 3 2n 3 2n 3 3
↓ 2 = ↓ = ↓ = .
n ↓ n ↓ n n n
     
     
Fix ω> 0. By Proposition 9.1, there exists N N withN > 3. Then, for all n N, we
   →    ε ↗
have
2n 3 3 3
↓ 2 = <ω,
n ↓ n ↘ N
 
 
as desired.
 
 
Example 9.14. We will prove that
3k2 +8k 5 3
lim ↓ = .
k 4k2 +1 4
≃→
First note that
3n2 +8n 5 3 3n2 +8n 5 3 n2 + 1 8n 23
↓ = ↓ 4 = ↓ 4 .
 4n2 +1 ↓ 4  

4n2 +1 ↓ 4 ! n2 + 1 4"

 4n2 +1 
   
 
Now, when n  1, we have 8n  8 > 23. Also, 0 < 4n2!< 4n2 +"1. T  hus, 
   
↗ ↗  4 
8n 23 8n 23 8n 2
↓ 4 = ↓ 4 = .
4n2 +1 4n2 +1 ↘ 4n2 n
 
 
Now suppose ω> 0. By Proposition9.1, there exists N N with N > 2. Then, for all
  → ε
n N, we have
↗ 3n2 +8n 5 3 2 2
↓ <ω,
4n2 +1 ↓ 4 ↘ n ↘ N
 
 
as desired.
 
 
Example 9.15. We will show that the sequence (x ) given by x = 2k+1 diverges. So we
k →k=1 k
need to show that it does not converge to any real number. Let L R. We will prove by
→
contradiction that the sequence does not converge to L.
Suppose that lim x = L. For k L , we have, by the triangle inequality,
k k
≃→ ↗| |
x L + L x = 2k +1 = 2k +1 2 L +1,
k k
| ↓ | | |↗| | | | ↗ | |
and so
x L L +1.
k
| ↓ |↗| |
Therefore, if ω L + 1, no matter which N N we choose, we can always choose an n
↘| | →
greater than both L and N, and then we have
| |
x L L +1 ω.
n
| ↓ |↗| | ↗
So the sequence (x ) does not converge to L.
k

102 Limits
Proposition 9.16 (Uniqueness of limits). If a sequence converges, then its limit is unique.
In other words, if a sequence (x ) converges to L and to L , then L = L .
k →k=1 1 2 1 2
Proof. Suppose (x ) converges to both L and L . Choose ω> 0. Then there exists a natural
k 1 2
number N such that
1
ω
n N = x L < .
1 n 1
↗ ↔| ↓ | 2
Similarly, there exists a natural number N such that
2
ω
n N = x L < .
2 n 2
↗ ↔| ↓ | 2
Let N = max N ,N . Then, for n N, we have
1 2
{ } ↗
ω ω
x L < and x L < ,
n 1 n 2
| ↓ | 2 | ↓ | 2
and so, by the triangle inequality, we have
ω ω
L L L x + x L < + = ω.
1 2 1 n n 2
| ↓ |↘| ↓ | | ↓ | 2 2
Since our choice of ω> 0 was arbitrary, we conclude from Corollary 9.10 that L = L .
1 2
Proposition 9.17. Suppose r
→
N and (x k ) →k=1 is a sequence of real numbers. Then (x k ) →k=1
converges to L if and only if (x ) converges to L
k+r →k=1
Proof. Suppose lim k x k = L. Let ω> 0. Then there exists N N such that
≃→ →
n N = x L <ω.
n
↗ ↔| ↓ |
But then, for all n N, we have n+r > n N and so
↗ ↗
x L <ω.
n+r
| ↓ |
So lim x = L. The reverse implication is left as Exercise 9.4.9.
k k+r
≃→
Proposition 9.17 tells us that we can always ignore some finite number of terms at the
beginning of a sequence when computing limits.
Proposition 9.18 (Bernoulli’s inequality). For x R 0 and k Z 0 , we have
→ ↓ → ↓
(1+x)k 1+kx.
↗
Proof. The statement is clearly true for k = 0 and k = 1, so we assume k 2. Although we
↗
only proved the Binomial Theorem for the integers (Theorem 4.12), the same proof shows
that it also holds for a,b R. Thus we have
→
k k
k k
(1+x)k = xm = 1+kx+ xm 1+kx.
m m ↗
m=0  m=2 
) )
Proposition 9.19. If x R with x < 1, then lim k xk = 0.
→ | | ≃→

Limits 103
Proof. The case x = 0 is easy (see Proposition 9.25(i)), so we assume 0 < x < 1. Then for
| |
N 0, by Proposition 9.18, we have
↗
N N
1 1 x 1 x 1 x
= 1+ ↓| | 1+ ↓| | N > ↓| | N. (9.1)
x x ↗ x x
| |  | |   | |   | | 
Now suppose ω> 0. By Proposition 9.1, there exists a natural number N such that
x 1
N > | | . (9.2)
1 x ω
↓| |
Then, for n N, we have
↗
xn 0 = x n
| ↓ | | |
x N (by Proposition 9.7)
↘| |
x 1
< | | (by (9.1))
1 x N
↓| |
<ω. (by (9.2))
Definition 9.20 (Bounded, increasing, decreasing, monotonic sequence). Suppose (x )
k →k=1
is a sequence.
(i) The sequence is bounded if there exist ϑ,u R such that k N, ϑ x k u.
→ ⇓ → ↘ ↘
Equivalently, it is bounded if there exists ϑ R such that k N, x k ϑ.
→ ⇓ → | |↘
(ii) The sequence is increasing if x
k+1
x
k
for all k N.
↗ →
(iii) The sequence is decreasing if x
k+1
x
k
for all k N.
↘ →
(iv) The sequence is monotonic if it is either increasing or decreasing.
Theorem 9.21. Every monotonic bounded sequence converges.
Proof. We will prove that every decreasing bounded sequence converges. The proof for
increasing bounded sequences is analogous and can be found in [BG10, Th. 10.19].
Suppose (x ) is decreasing and bounded. Then the set
k →k=1
A = x k : k N R
{ → }≃
is bounded. Thus, by Proposition 7.38, it has a greatest lower bound s. We will show that
lim x = s.
k k
≃→
Let ω> 0. Then s+ω> s , and so s+ω is not a lower bound for A. Thus, there exists
some N N such that x N < s+ω. Since the sequence is decreasing, we have x n x N for
→ ↘
all n N. Therefore, for n N, we have
↗ ↗
s ω< s x x < s+ω,
n N
↓ ↘ ↘
and so x s <ω by Proposition 9.6(v).
n
| ↓ |

104 Limits
Note that increasing sequences are always bounded below (by the first term), so they are
bounded if and only if they are bounded above. Similarly, decreasing sequences are bounded
if and only if they are bounded below.
Examples 9.22. (i) Thesequence 4+ 1 → isdecreasingandboundedbelowby4. There-
n n=1
fore it converges.
! "
(ii) The sequence 8 2 → is increasing and bounded above by 8. Therefore it con-
↓ 3k2+5 k=1
verges.
! "
Proposition 9.23. Suppose the sequence (x ) converges to L.
k →k=1
(i) If (x
k
)
→k=1
is increasing, then x
k
↘
L for all k
→
N.
(ii) If (x
k
)
→k=1
is decreasing, then x
k
↗
L for all k
→
N.
Proof. We will prove part (i), since the proof of part (ii) is analogous.
Assume (x ) is increasing and lim x = L. We will prove the result by contradic-
k →k=1 k k
≃→
tion. Assume there exists m N such that x m > L. Let ω = x m L. Then for any N N,
→ ↓ →
let n = max N,m . So, in particular, n N. Since the sequence is increasing, we have
{ } ↗
x x > L. But then
n m
↗
x L = x L x L = ω.
n n m
| ↓ | ↓ ↗ ↓
Thus the sequence (x ) does not converge to L, which is a contradiction.
k →k=1
Proposition 9.24. Every convergent sequence is bounded.
Proof. Suppose (x ) converges. Taking ω = 1 in the definition of a limit, there exists
k →k=1
N N such that for all n N, we have x n L < 1. Note that
→ ↗ | ↓ |
x L < 1 = x L x L x L < 1 = x < L +1,
n n n n n
| ↓ | ↔| |↓| |↘ | |↓| | ↘| ↓ | ↔| | | |
 
where, in the second inequality after the first implication, we used Proposition 9.8(iv). Now
 
let
M = max x , x ,..., x , L +1 ,
1 2 N 1
{| | | | | ↑ | | | }
which exists since the maximum of any finite set exists. Then we have x M for all
k
| |↘
k N, and so the sequence is bounded.
→
Proposition 9.25 (Arithmetic of limits). Suppose lim a = A, lim b = B, and
k k k k
≃→ ≃→
c R.
→
(i) lim c = c.
k
≃→
(ii) lim (ca ) = cA.
k k
≃→
(iii) lim (a +b ) = A+B.
k k k
≃→
(iv) lim (a b ) = AB.
k k k
≃→
(v) If A = 0, then lim 1 = 1.
↑ k ≃→ ak A

Limits 105
Proof. We will prove parts (i), (iii), and (v). The proofs of the other parts can be found in
[BG10, Prop. 10.23].
Proof of (i): For any ω> 0, we have c c = 0 <ω , and so we can take any N N in
| ↓ | →
the definition of a limit (Definition 9.11).
Proof of (iii): Let ω> 0. Then there exists N 1 N such that
→
ω
n N = a A < ,
1 n
↗ ↔| ↓ | 2
and there exists N 2 N such that
→
ω
n N = b B < .
2 n
↗ ↔| ↓ | 2
Define N = max N ,N . Then, for all n N, we have
1 2
{ } ↗
(a +b ) (A+B) = (a A)+(b B)
n n n n
| ↓ | | ↓ ↓ |
a A + b B (by the triangle inequality)
n n
↘| ↓ | | ↓ |
ω ω
< + = ω.
2 2
Proof of (v): Suppose A = 0. Choose N 1 N such that, for n N 1 , we have a n A <
↑ → ↗ | ↓ |
| A |. Note that
2
A A A
a A < | | = A a A a A a < | | = | | < a ,
n n n n n
| ↓ | 2 ↔| |↓| |↘ | |↓| | ↘| ↓ | 2 ↔ 2 | |
 
where, in the second inequality after thefirst implication, we used Proposition 9.8(iv). Thus,
for all n N , we have
1
↗
A 1 2
0 < | | < a = 0 < < .
n
2 | | ↔ a A
n
| | | |
Thus, for n N ,
1
↗
1 1 A a A a 2
n n
= ↓ = | ↓ | A a .
a ↓ A Aa A a ↘ A 2| ↓ n |
 n   n  | || n | | |
   
Now let ω> 0. Sin  ce lim k   a k = A, w  e can choose N 2 N such that
≃→ →
A 2
n N = A a < | | ω.
2 n
↗ ↔| ↓ | 2
Define N = max N ,N . Then, for n N, we have
1 2
{ } ↗
1 1 2 2 A 2
A a < | | ω = ω.
a ↓ A ↘ A 2| ↓ n | A 2 2
 n  | | | |
 
Proposition 9.25 is extremelyuseful, since it allows us to compute new limits from old
 
ones.

106 Limits
Proposition 9.26. For ϑ N, we have
→
1
lim = 0.
k kω
≃→
Proof. We prove the result by induction on ϑ. The base case ϑ = 1 is Proposition 9.12. Now
assume n N and the result holds for ϑ = n. Then, by Proposition 9.25(iv), we have
→
1 1 1
lim = lim lim = 0 0 = 0,
k kn+1 k k k kn ·
≃→  ≃→  ≃→ 
and so the result also holds for ϑ = n+1. This completes the proof of the induction step.
Example 9.27. We have
4k2 5k +2 4k2 5k 2
lim ↓ = lim + ↓ +
k 3k2 k 3k2 3k2 3k2
≃→ ≃→ 
4 5 1 2 1 4 4
= lim lim + lim = +0+0 = .
k 3 ↓ 3 k k 3 k k2 3 3
≃→   ≃→   ≃→ 
Example 9.28. Consider the sequence ( 1)k → . This sequence is bounded since ( 1)k
↓ k=1 | ↓ |↘
1 for all k N. However, this sequence does not converge. We prove this by contradiction.
→ ! "
Suppose lim k ( 1)k = L. Then there exists N N such that
≃→ ↓ →
1
n N, ( 1)n L < .
⇓ ↗ | ↓ ↓ | 2
Since 2N,2N +1 > N, we then have, by the triangle inequality,
1 1
2 = ( 1)2N ( 1)2N+1 ( 1)2N L + L ( 1)2N+1 < + = 1,
↓ ↓ ↓ ↘ ↓ ↓ ↓ ↓ 2 2
     
which is a contradiction.     
Example 9.29. Consider the sequences (a ) and (b ) , where
k →k=1 k →k=1
a = 2 k and b = k.
k k
↓
Neither of these sequences is bounded, hence both sequences diverge by Proposition 9.24.
However, (a + b ) is the constant sequence (2) , which converges to 2 by Proposi-
k k →k=1 →k=1
tion 9.25(i).

Limits 107
Exercises.
9.4.1. Using the definition of a limit directly, find
8
lim .
k 3k
≃→
9.4.2. Using the definition of a limit directly, find
2k2 +3k 1
lim ↓ .
k 5k2 +5
≃→
9.4.3. Suppose (x ) , (y ) , and (z ) are sequences satisfying
k →k=1 k →k=1 k →k=1
x
k
y
k
z
k
for all k N.
↘ ↘ →
Furthermore, suppose that lim
k
x
k
= L = lim
k
z
k
for some L R. Prove that
≃→ ≃→ →
lim y = L.
k k
≃→
9.4.4. A function f: R R is said to be increasing if
∈
x,y R, x y = f(x) f(y) .
⇓ → ↘ ↔ ↘
Prove that if (x k ) →k=1 is an increasing se!quence and f: R
∈
R is"an increasing function whose
image is bounded, then the sequence (f(x )) converges.
k →k=1
9.4.5. Let (x
k
)
→k=1
be a sequence and let L
→
R.
(i) Prove that if lim x = L, then lim x = L .
k k k k
≃→ ≃→| | | |
(ii) Give an example of a sequence (x ) that diverges, but for which the sequence
k →k=1
( x ) converges.
|
k
|
→k=1
9.4.6. Using any results we have proved, find
3k3 +8k2 3k 11
lim ↓ ↓ .
k 6k3
≃→
9.4.7. Define a sequence x by
{
k
}
→k=1
0 if k is odd,
x =
k
-1 if k is even.
Prove that the sequence x diverges.
{
k
}
→k=1
9.4.8. Consider the sequence (a ) , where a = ( 1)k. Find a sequence (b ) such that
k →k=1 k
↓
k →k=1
the sequence (a +b ) converges.
k k →k=1
9.4.9. Complete the proof of Proposition 9.17 by showing that if (x ) converges to L,
k+r →k=1
then (x ) converges to L.
k →k=1

108 Limits
9.5 Square roots
The completeness axiom (Axiom 7.35) allows us to prove the existence of certain real num-
bers, such as square roots. For any r R>0 , we define the square root of r to be
→
↖r := sup x R : x2 < r .
{ → }
We define ↖0 := 0.
Theorem 9.30. For r R>0 , the real number ↖r is well-defined, positive, and (↖r)2 = r.
→
Sketch of proof. We will consider the case r = 2. The proof for other values of r is similar.
We first prove that ↖2 is well-defined. Let
A = x R : x2 < 2 .
{ → }
So we want to show that supA exists. Since 12 = 1 < 2, we see that A is nonempty. Now,
x 2 = x2 4 > 2.
↗ ↔ ↗
Thus, x < 2 for all x A. So A is bounded above. Therefore, by the completeness axiom
→
(Axiom 7.35), the set A has a supremum. So ↖2 is well-defined.
It remains to prove that (↖2)2 = 2. This involves showing that the assumptions
(↖2)2 < 2 or (↖2)2 > 2 lead to contradictions, using the definition of supremum. See
[BG10, Th. 10.25] for details.
Remark 9.31. Note that ↖2 is also a number whose square is equal to 2. The notation ↖2
↓
means the positive square root.
Proposition 9.32. Suppose r R 0 . Then the number ↖r is unique. More precisely, if
x R 0 satisfies x2 = r, then x → = ↖ ↓ r.
→ ↓
Proof. First consider the case r = 0. By Axiom 7.13(ii), if x > 0, then x2 > 0. Thus,
x = 0 = ↖0 is the only solution to x2 = 0 with x R 0 .
Now suppose r > 0 and x R 0 satisfies x2 = → r = ↓ (↖r)2. Then
→ ↓
0 = x2 (↖r)2 = (x ↖r)(x+↖r).
↓ ↓
Since x+↖r > 0, this implies that x ↖r = 0, and so x = ↖r.
↓
Proposition 9.33. If r R, r < 0, then there is no x R such that x2 = r.
→ →
Proof. If x = 0, then x2 = 0 = r. On the other hand, if x = 0, then by Proposition 2.11 for
↑ ↑
R, we have x2 > 0. Thus x2 = r.
↑
Proposition 9.33 says that negative real numbers do not have real square roots. In future
courses you will discuss the complex numbers. It will turn out that, when working over the
complex numbers, all square roots exist. In particular, negative real numbers have square
roots in the complex numbers.

Chapter 10
Rational and irrational numbers
In this chapter, we briefly discuss the concept of rational numbers, which are numbers that
can be written as a quotient of two integers. We also consider irrational numbers.
10.1 Rational numbers
Definition 10.1. A real number r R is rational if r = m for some m,n Z, n = 0. A
→ n → ↑
real number that is not rational is irrational. The set of all rational numbers is denoted Q.
Proposition 10.2. We have Z Q.
≃
Proof. For n Z, we have n = n Q.
→ 1 →
Proposition 10.3. Any rational number r Q can be written in the form r = m where
→ n
n > 0 and m and n have no common factors (other than 1).
±
Sketch of proof. Let r Q. By definition r = a for some a,b Z, b = 0. If b < 0, then
→ b → ↑
we write r = a and the denominator is positive. Thus, we can assume the denominator is
↑
b
positive. Then↑we factor the numerator and denominator as products of primes and cancel
all common prime factors.
When r is written in the form r = m where n > 0 and m and n have no common factors,
n
we say that the representation m is in lowest terms.
n
Proposition 10.4. Suppose r,s Q. Then
→
(i) r+s Q,
→
(ii) rs Q,
→
(iii) r Q,
↓ →
(iv) r s Q,
↓ →
(v) if r = 0, then r
↑
1 Q.
↑ →
109

110 Rational and irrational numbers
Proof. We can write r = a and s = c for some a,b,c,d Z with b,d = 0. Then
b d → ↑
a c ad bc ad+bc
r+s = + = + = Q.
b d bd bd bd →
This proves part (i). The proof of the remaining parts is left as an exercise.
Theorem 10.5. Suppose x,y R with x < y. Then there exists r Q such that x < r < y.
→ →
Proof. If x = 0, then, by Proposition 9.3, we can find n N such that x = 0 < 1 < y.
→ n
Now assume x > 0. By Proposition 9.3, there exists m N such that 1 < y x. Also,
→ m ↓
since N is unbounded, there exists n N with n > mx. By the well-ordering principle
→
(Theorem 2.33), we can choose this n to be minimal, so that n 1 mx < n. Dividing by
↓ ↘
m, we have
n 1 n
x < .
m ↓ m ↘ m
The left-hand inequality above implies
n 1
x+ < x+(y x) = y.
m ↘ m ↓
Therefore we have
n
x < < y,
m
as desired.
Now suppose x < 0. If y > 0, then we can simply take r = 0. Therefore, we assume
y 0. So we have 0 y < x. By the above, there is a rational number r such that
↘ ↘ ↓ ↓
y < r < x. Then r is also rational (by Proposition 10.4) and we have x < r < y, as
↓ ↓ ↓ ↓
desired.
Theorem 10.5 says that the rational numbers are dense in the real numbers. (The word
dense is a term in the field of topology and applies in a more general context.)
Corollary 10.6. There is no smallest positive rational number.
Proof. We prove the result by contradiction. Suppose a is a smallest positive rational num-
ber. So 0 < a. Then, by Theorem 10.5, there exists some r Q such that 0 < r < a. This
→
contradicts the fact that a is a smallest positive rational number.
Exercises.
10.1.1 ([BG10, Prop. 11.2]). Let x,y,z,w R with y = 0 and w = 0. Prove that if x = z,
→ ↑ ↑ y w
then xw = zy.
10.1.2 ([BG10, Prop. 11.3]). Prove that if x,y,z R with y = 0 and z = 0, then xz = x.
→ ↑ ↑ yz y

Irrational numbers 111
10.1.3 ([BG10, Prop. 11.5]). Let m,n,s,t Z be such that n,t = 0, and m and n do not
→ ↑
have any common factors. Prove that if m = s, then m divides s and n divides t.
n t
10.1.4 ([BG10, Prop. 11.7]). The rational number m
n →
Q is positive (i.e. m
n →
R>0 ) if and
only if either m > 0 and n > 0, or m < 0 and n < 0.
10.2 Irrational numbers
While we already know rational numbers exist (e.g. the integers are rational numbers), we
have not yet proven that any irrational numbers exist.
Proposition 10.7. The real number ↖2 is irrational.
Proof. We will prove the result by contradiction. By Proposition 10.3, we can write ↖2 = m,
n
where m,n Z have no common factors (other than 1). Then we have
→ ±
m2 m 2
= = (↖2)2 = 2 = m2 = 2n2.
n2 n ↔
# $
Thus, 2 divides m2. Then, by Euclid’s Lemma (Proposition 6.31), 2 divides m. So there
exists some a Z such that 2a = m. Note that
→
2a = m = 22a2 = m2 = 2n2 = 2a2 = n2.
↔ ↔
So 2 divides n2. Again, by Euclid’s Lemma (Proposition 6.31), 2 divides n. But then 2 is
a common factor of m and n, contradicting our assumption that m and n have no common
factors.
In fact, Proposition 10.7 can be generalized. An integer n is said to be a perfect square
if n = m2 for some m Z. Then we have the following result.
→
Theorem 10.8. If a N is not a perfect square, then ↖a is irrational.
→
Proof. The proof of this result is left as an exercise. Hint: Follow the argument in the proof
of Proposition 10.7 using a prime factor of a.
Example 10.9. The real number ↖2+↖3 is irrational. We can prove this by contradiction.
Suppose ↖2+↖3 Q. Then
→
2
↖2+↖3 = 2+2↖6+3 = 5+2↖6 Q.
→
# $
So 5+2↖6 = a for some a Q. But then ↖6 = a ↑ 5 Q by Proposition 10.4, contradicting
→ 2 →
Theorem 10.8.
Note that Q does not satisfy the completeness axiom (Axiom 7.35). For example, the set
r Q : r2 < 2
{ → }
is bounded above by a rational number (say, by 2), but has no least upper bound in Q. Of
course, it has a least upper bound in R, namely ↖2. Similarly, the irrational numbers do
not satisfy the completeness axiom.

112 Rational and irrational numbers
Exercises.
10.2.1 ([BG10, Prop.11.13]). Letmandnbenonzerointegers. Provethat m↖2isirrational.
n

Index
, 28 bounded, 81
⇔
, 27 above, 81
⇑
, 27 below, 25, 81
⇓
, 30 sequence, 103
⇐↔
= , 29
↔
, 5 cancellation property, 6
→
, 31 Cartesian plane, 53
¬
⫆̸, 28 Cartesian product, 53
, 19 codomain, 54, 55
↑≃
, 49 commutativity
\
, 19 of addition, 5, 73
≃
⫅̸, 19 of multiplication, 5, 73
, 46 complement, 49
↙
, 53 complex numbers, 108
∞
⫋, 47 composite, 68
=, 6 composition, 89
congruent modulo n, 63
absolute value, 59 contradiction, proof by, 15
addition, 5, 73 contrapositive, 31
modulo n, 65 converge, 100
additive identity, 6, 73 converse, 30
additive inverse, 6, 73
associativity De Morgan’s laws, 31
of addition, 5, 73 decreasing, 103
of multiplication, 5, 73 di”erence of sets, 49
axiomatic set theory, 56 digits, 12
axioms disjoint, 49
integers, 5 distance, 99
real numbers, 73 distributivity, 5, 73
diverge, 100
base case, 21 divisibility, 9
Bernoulli’s inequality, 102 division, 75
bijection, 88 division algorithm, 61
bijective, 88 domain, 54, 55
binary operation, 5 double implication, 30
binomial coe!cient, 40
Binomial Theorem, 40 empty set, 47
for integers, 41 equality of sets, 19
113

114 Index
equivalence class, 58 multiplicative, 74
equivalence relation, 57 right, 90
equivalent modulo n, 63 two-sided, 90
existential quantifier, 27 irrational number, 109
factor, 68 juxtaposition, 5, 73
factorial, 35
largest element, 83
factorization, 68
Law of the Excluded Middle, 15
Fermat’s Little Theorem, 71
least upper bound, 81
Fibonacci numbers, 43
left inverse, 90
finite sequence, 34
less than, 16, 77
function, 54, 55
limit, 100
gcd, 25, 68 uniqueness, 102
graph, 55 lower bound, 81
greater than, 16, 77 lowest terms, 109
greatest element, 24
maximum, 83
greatest lower bound, 81
minimum, 83
identity mod, 63
additive, 6, 73 modular arithmetic, 63
multiplicative, 6, 73 modulus, 63
identity element monotonic, 103
for addition, 6, 73 multiplication, 5, 73
for multiplication, 6, 73 modulo n, 65
identity function, 88 multiplicative identity, 6, 73
if and only if, 30 multiplicative inverse, 74
image, 88
implies, 29
N, 15
natural numbers, 15
increasing, 103
negation, 31
induction, 21, 23
negative, 24
second form, 43
negative integer, 15
strong, 43
negative real number, 77
induction hypothesis, 21
nonnegative, 24
induction step, 21
inequality, Bernoulli’s, 102
odd, 49
inf, 81
one-to-one, 87
infimum, 81
onto, 88
injection, 87
ordered pair, 53
injective, 87
integers, 5 parity, 63
modulo n, 64 partition, 59
intersection, 49 Pascal’s triangle, 41
inverse, 90 perfect square, 111
additive, 6, 73 positive, 24
left, 90 positive real numbers, 77

Index 115
prime, 68 transitivity of equality, 6
product notation, 35 triangle inequality, 97, 99
proof by contradiction, 15 two-sided inverse, 90
quantifier union, 49
existential, 27 universal quantifier, 27
universal, 27 upper bound, 81
quotient, 61
well-ordering principle, 25
R, 73
R>0 , 76 Z ↓ 0 , 35
ZFC, 56
R 0 , 78
ra
↓
tional number, 109
Zn , 64
Z/nZ, 64
real number, 73
positive, 77
reflexivity of equality, 6
relation, 57
equivalence, 57
remainder, 61
replacement, 6
representative, 58
right inverse, 90
RSA encryption, 71
Russell’s paradox, 56
separation, 99
sequence, 34
finite, 34
set, 46
di”erence, 49
set theory, 46
smallest element, 24, 83
square root, 108
strong induction, 43
subset, 19
subtraction, 13, 75
summation notation, 35
sup, 81
supremum, 81
surjection, 88
surjective, 88
symmetric, 99
symmetric di”erence, 49
symmetry of equality, 6
term, 34

Bibliography
[BG10] Matthias Beck and Ross Geoghegan. The Art of Proof. Undergraduate Texts in
Mathematics. Springer, 2010. http://dx.doi.org/10.1007/978-1-4419-7023-7.
116
