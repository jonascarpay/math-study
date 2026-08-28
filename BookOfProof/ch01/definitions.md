# Chapter 1 definitions — Sets

Hammack numbers Definitions, Facts and Examples in separate per-chapter
sequences. Cite by kind and number ("Definition 1.3", "Fact 1.2").

Notation used in this file: set complement is written with an overline, `A̅`.
When the bar covers a compound expression it is written `‾(A ∩ B)`.

## 1.1 Introduction to Sets

### set, element (page 3)

A _set_ is a collection of things. The things are called _elements_ of the
set.

A set is often expressed by listing its elements between commas, enclosed by
braces, e.g. {2, 4, 6, 8}.

A set is called an _infinite set_ if it has infinitely many elements;
otherwise it is called a _finite set_.

Two sets are _equal_ if they contain exactly the same elements. Order and
repetition do not matter:

    {2, 4, 6, 8} = {4, 2, 8, 6},   but   {2, 4, 6, 8} ≠ {2, 4, 6, 7}.

### ∈, ∉ (page 3)

To express that 2 is an element of the set A, we write 2 ∈ A, and read this
as "2 is an element of A," or "2 is in A," or just "2 in A."

5 ∉ A reads "5 is not an element of A."

Expressions like 6, 2 ∈ A or 2, 4, 8 ∈ A indicate that several things are in
a set.

### ℕ, ℤ, ℝ (page 4)

  - The set of _natural numbers_ (the positive whole numbers):

    ℕ = {1, 2, 3, 4, 5, 6, 7, …}.

  - The set of _integers_:

    ℤ = {…, −3, −2, −1, 0, 1, 2, 3, 4, …}.

  - ℝ stands for the set of all _real numbers_.

Sets need not have numbers as elements. A set may itself have sets as
elements: E = {1, {2, 3}, {2, 4}} has three elements — the number 1, the set
{2, 3} and the set {2, 4}. Thus 1 ∈ E and {2, 3} ∈ E and {2, 4} ∈ E, but
2 ∉ E, 3 ∉ E and 4 ∉ E.

### cardinality, |X| (page 4)

If X is a finite set, its _cardinality_ or _size_ is the number of elements
it has, and this number is denoted as |X|.

The bars are overloaded: |X| means absolute value if X is a number and
cardinality if X is a set. The distinction is always to be read from
context. In {x ∈ ℤ : |x| < 4} the x is a number, so |x| is absolute value;
in {X ∈ A : |X| < 3} with A = {{1,2}, {3,4,5,6}, {7}} the X are sets, so |X|
is cardinality. (page 6)

### the empty set, ∅ (page 4)

The _empty set_ is the set { } that has no elements. We denote it as ∅, so
∅ = { }. Observe that |∅| = 0. The empty set is the only set whose
cardinality is zero.

Do not write {∅} when you mean ∅. These sets cannot be equal because ∅
contains nothing while {∅} contains one thing, namely the empty set:

    ∅ ≠ {∅},   |∅| = 0,   |{∅}| = 1.

The box analogy: a set is a box with things in it. ∅ = { } is an empty box;
{∅} is a box with an empty box inside it. F = {∅, {∅}, {{∅}}} is a box
containing three things, so |F| = 3. G = {ℕ, ℤ} is a box containing two
boxes, so |G| = 2. (page 5)

### set-builder notation (page 5)

_Set-builder notation_ describes sets that are too big or complex to list
between braces. In general a set X written with set-builder notation has the
syntax

    X = {expression : rule},

where the elements of X are understood to be all values of "expression" that
are specified by "rule."

Read the first brace as "the set of all things of form," and the colon as
"such that." So E = {2n : n ∈ ℤ} reads "E equals the set of all things of
form 2n, such that n is an element of ℤ."

There can be many ways to express the same set:

    E = {2n : n ∈ ℤ} = {n : n is an even integer} = {n : n = 2k, k ∈ ℤ}
      = {n ∈ ℤ : n is even}.

Some writers use a bar instead of a colon, e.g. E = {n ∈ ℤ | n is even}. We
use the colon.

### Example 1.1 — illustrations of set-builder notation (page 5)

  1. {n : n is a prime number} = {2, 3, 5, 7, 11, 13, 17, …}
  2. {n ∈ ℕ : n is prime} = {2, 3, 5, 7, 11, 13, 17, …}
  3. {n² : n ∈ ℤ} = {0, 1, 4, 9, 16, 25, …}
  4. {x ∈ ℝ : x² − 2 = 0} = {√2, −√2}
  5. {x ∈ ℤ : x² − 2 = 0} = ∅
  6. {x ∈ ℤ : |x| < 4} = {−3, −2, −1, 0, 1, 2, 3}
  7. {2x : x ∈ ℤ, |x| < 4} = {−6, −4, −2, 0, 2, 4, 6}
  8. {x ∈ ℤ : |2x| < 4} = {−1, 0, 1}

### Example 1.2 (page 6)

Describe the set A = {7a + 3b : a, b ∈ ℤ}.

Solution: This set contains all numbers of form 7a + 3b, where a and b are
integers. Each such number is an integer, so A contains only integers. But
which integers? If n is any integer, then n = 7n + 3(−2n), so n = 7a + 3b
where a = n and b = −2n. Therefore n ∈ A. We've now shown that A contains
only integers, and also that every integer is an element of A. Consequently
A = ℤ.

### summary of special sets (page 6)

  - The empty set: ∅ = { }
  - The natural numbers: ℕ = {1, 2, 3, 4, 5, …}
  - The integers: ℤ = {…, −3, −2, −1, 0, 1, 2, 3, 4, 5, …}
  - The rational numbers: ℚ = {x : x = m/n, where m, n ∈ ℤ and n ≠ 0}
  - The real numbers: ℝ

We visualize ℝ as an infinitely long number line. ℚ is the set of all
numbers in ℝ that can be expressed as a fraction of two integers; ℚ ≠ ℝ,
as √2 ∉ ℚ but √2 ∈ ℝ.

### intervals (page 7)

Any two numbers a, b ∈ ℝ with a < b give rise to various intervals.

  - Closed interval:      [a, b]   = {x ∈ ℝ : a ≤ x ≤ b}
  - Open interval:        (a, b)   = {x ∈ ℝ : a < x < b}
  - Half-open interval:   (a, b]   = {x ∈ ℝ : a < x ≤ b}
  - Half-open interval:   [a, b)   = {x ∈ ℝ : a ≤ x < b}
  - Infinite interval:    (a, ∞)   = {x ∈ ℝ : a < x}
  - Infinite interval:    [a, ∞)   = {x ∈ ℝ : a ≤ x}
  - Infinite interval:    (−∞, b)  = {x ∈ ℝ : x < b}
  - Infinite interval:    (−∞, b]  = {x ∈ ℝ : x ≤ b}

Each of these intervals is an infinite set. It is an unfortunate notational
accident that (a, b) can denote both an open interval on the line and a
point on the plane; the difference is usually clear from context.

## 1.2 The Cartesian Product

### Definition 1.1 — ordered pair (page 8)

An _ordered pair_ is a list (x, y) of two things x and y, enclosed in
parentheses and separated by a comma.

(2, 4) ≠ (4, 2): the order matters. The things in an ordered pair need not
be numbers — (ℓ, m), ({2,5}, {3,2}), ((2,4), (4,2)), (2, {1,2,3}), (ℝ, (0,0))
are all ordered pairs.

### Definition 1.2 — Cartesian product, A × B (page 8)

The _Cartesian product_ of two sets A and B is another set, denoted as A × B
and defined as

    A × B = {(a, b) : a ∈ A, b ∈ B}.

For example, if A = {k, ℓ, m} and B = {q, r}, then

    A × B = {(k,q), (k,r), (ℓ,q), (ℓ,r), (m,q), (m,r)}.

### Fact 1.1 (page 9)

If A and B are finite sets, then |A × B| = |A| · |B|.

### ordered triples, n-fold products (page 10)

An _ordered triple_ is a list (x, y, z). In general,

    A₁ × A₂ × ⋯ × Aₙ = {(x₁, x₂, …, xₙ) : xᵢ ∈ Aᵢ for each i = 1, 2, …, n}.

Be mindful of parentheses: ℝ × (ℕ × ℤ) is a Cartesian product of two sets,
whose elements are ordered pairs (x, (y,z)); ℝ × ℕ × ℤ is a Cartesian
product of three sets, whose elements are ordered triples (x, y, z). For now
we regard them as different.

### Cartesian power, Aⁿ (page 10)

For any set A and positive integer n, the _Cartesian power_ Aⁿ is

    Aⁿ = A × A × ⋯ × A = {(x₁, x₂, …, xₙ) : x₁, x₂, …, xₙ ∈ A}.

ℝ² is the familiar Cartesian plane and ℝ³ is three-dimensional space;
ℤ² = {(m,n) : m, n ∈ ℤ} is a grid of points on the plane.

## 1.3 Subsets

### Definition 1.3 — subset, ⊆, ⊈ (page 12)

Suppose A and B are sets. If every element of A is also an element of B,
then we say A is a _subset_ of B, and we denote this as A ⊆ B. We write
A ⊈ B if A is not a subset of B, that is, if it is not true that every
element of A is also an element of B. Thus A ⊈ B means that there is at
least one element of A that is not an element of B.

### Example 1.5 (page 12)

  1. {2, 3, 7} ⊆ {2, 3, 4, 5, 6, 7}
  2. {2, 3, 7} ⊈ {2, 4, 5, 6, 7}
  3. {2, 3, 7} ⊆ {2, 3, 7}
  4. {(x, sin(x)) : x ∈ ℝ} ⊆ ℝ²
  5. {1, 3, 5, 7, 11, 13, 17, …} ⊆ ℕ
  6. ℕ ⊆ ℤ ⊆ ℚ ⊆ ℝ
  7. ℝ × ℕ ⊆ ℝ × ℝ
  8. A ⊆ A for any set A
  9. ∅ ⊆ ∅

### Fact 1.2 (page 12)

The empty set is a subset of all sets, that is, ∅ ⊆ B for any set B.

Why: ∅ ⊈ B would mean there is at least one element of ∅ that is not an
element of B. But this cannot be so because ∅ contains no elements.

### Fact 1.3 (page 13)

If a finite set has n elements, then it has 2ⁿ subsets.

Why: build a subset by starting with { } and, for each element of B in turn,
choosing to insert it or not. At each branching the number of subsets
doubles.

### Example 1.6 — element vs. subset (page 14)

  1.  1 ∈ {1, {1}} ............ 1 is the first element listed in {1, {1}}
  2.  1 ⊈ {1, {1}} ............ because 1 is not a set
  3.  {1} ∈ {1, {1}} .......... {1} is the second element listed
  4.  {1} ⊆ {1, {1}} .......... make subset {1} by selecting 1
  5.  {{1}} ∉ {1, {1}} ........ {1, {1}} contains only 1 and {1}, not {{1}}
  6.  {{1}} ⊆ {1, {1}} ........ make subset {{1}} by selecting {1}
  7.  ℕ ∉ ℕ .................. ℕ is a set (not a number), ℕ contains only numbers
  8.  ℕ ⊆ ℕ .................. because X ⊆ X for every set X
  9.  ∅ ∉ ℕ .................. ℕ contains only numbers and no sets
  10. ∅ ⊆ ℕ .................. ∅ is a subset of every set
  11. ℕ ∈ {ℕ} ................ {ℕ} has just one element, the set ℕ
  12. ℕ ⊈ {ℕ} ................ because, for instance, 1 ∈ ℕ but 1 ∉ {ℕ}
  13. ∅ ∉ {ℕ} ................ the only element of {ℕ} is ℕ, and ℕ ≠ ∅
  14. ∅ ⊆ {ℕ} ................ ∅ is a subset of every set
  15. ∅ ∈ {∅, ℕ} ............. ∅ is the first element listed in {∅, ℕ}
  16. ∅ ⊆ {∅, ℕ} ............. ∅ is a subset of every set
  17. {ℕ} ⊆ {∅, ℕ} ........... make subset {ℕ} by selecting ℕ
  18. {ℕ} ⊈ {∅, {ℕ}} ......... because ℕ ∉ {∅, {ℕ}}
  19. {ℕ} ∈ {∅, {ℕ}} ......... {ℕ} is the second element listed
  20. {(1,2), (2,2), (7,1)} ⊆ ℕ × ℕ ... each pair is in ℕ × ℕ

Note the pattern in {1, 2, {1,3}}: although {1, 3} ⊈ B, it is true that
{1, 3} ∈ B; and {{1, 3}} ⊆ B.

## 1.4 Power Sets

### Definition 1.4 — power set, 𝒫(A) (page 15)

If A is a set, the _power set_ of A is another set, denoted as 𝒫(A) and
defined to be the set of all subsets of A. In symbols,

    𝒫(A) = {X : X ⊆ A}.

For A = {1, 2, 3}:

    𝒫(A) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}.

### Fact 1.4 (page 15)

If A is a finite set, then |𝒫(A)| = 2^|A|.

### Example 1.7 (page 16)

  1. 𝒫({0,1,3}) = {∅, {0}, {1}, {3}, {0,1}, {0,3}, {1,3}, {0,1,3}}
  2. 𝒫({1,2}) = {∅, {1}, {2}, {1,2}}
  3. 𝒫({1}) = {∅, {1}}
  4. 𝒫(∅) = {∅}
  5. 𝒫({a}) = {∅, {a}}
  6. 𝒫({∅}) = {∅, {∅}}
  7. 𝒫({a}) × 𝒫({∅}) = {(∅,∅), (∅,{∅}), ({a},∅), ({a},{∅})}
  8. 𝒫(𝒫({∅})) = {∅, {∅}, {{∅}}, {∅,{∅}}}
  9. 𝒫({1, {1,2}}) = {∅, {1}, {{1,2}}, {1,{1,2}}}
  10. 𝒫({ℤ, ℕ}) = {∅, {ℤ}, {ℕ}, {ℤ,ℕ}}

And three that are _wrong_:

  11. 𝒫(1) = {∅, {1}} ......... meaningless because 1 is not a set
  12. 𝒫({1,{1,2}}) = {∅,{1},{1,2},{1,{1,2}}} ... wrong: {1,2} ⊈ {1,{1,2}}
  13. 𝒫({1,{1,2}}) = {∅,{{1}},{{1,2}},{1,{1,2}}} ... wrong: {{1}} ⊈ {1,{1,2}}

## 1.5 Union, Intersection, Difference

### Definition 1.5 — ∪, ∩, − (page 18)

Suppose A and B are sets.

  - The _union_ of A and B is the set

    A ∪ B = {x : x ∈ A or x ∈ B}.

  - The _intersection_ of A and B is the set

    A ∩ B = {x : x ∈ A and x ∈ B}.

  - The _difference_ of A and B is the set

    A − B = {x : x ∈ A and x ∉ B}.

In words: A ∪ B is the set of all things in A or in B (or in both); A ∩ B is
the set of all things in both A and B; A − B is the set of all things in A
but not in B.

For any sets X and Y it is always true that X ∪ Y = Y ∪ X and X ∩ Y = Y ∩ X,
but in general X − Y ≠ Y − X. (page 18)

### Example 1.8 (page 18)

With A = {a,b,c,d,e}, B = {d,e,f}, C = {1,2,3}:

  1.  A ∪ B = {a,b,c,d,e,f}
  2.  A ∩ B = {d,e}
  3.  A − B = {a,b,c}
  4.  B − A = {f}
  5.  (A−B) ∪ (B−A) = {a,b,c,f}
  6.  A ∪ C = {a,b,c,d,e,1,2,3}
  7.  A ∩ C = ∅
  8.  A − C = {a,b,c,d,e}
  9.  (A∩C) ∪ (A−C) = {a,b,c,d,e}
  10. (A∩B) × B = {(d,d), (d,e), (d,f), (e,d), (e,e), (e,f)}
  11. (A×C) ∩ (B×C) = {(d,1), (d,2), (d,3), (e,1), (e,2), (e,3)}
  12. [2,5] ∪ [3,6] = [2,6]
  13. [2,5] ∩ [3,6] = [3,5]
  14. [2,5] − [3,6] = [2,3)
  15. [0,3] − [1,2] = [0,1) ∪ (2,3]

## 1.6 Complement

### universal set, U (page 20)

When dealing with a set, we almost always regard it as a subset of some
larger set. The set of prime numbers P carries the unstated assumption
P ⊆ ℕ, because ℕ is the most natural setting in which to discuss prime
numbers. This larger set ℕ is called the _universal set_ or _universe_
for P.

In the absence of specifics, if A is a set, then its universal set is often
denoted as U.

### Definition 1.6 — complement, A̅ (page 20)

Let A be a set with a universal set U. The _complement_ of A, denoted A̅, is
the set

    A̅ = U − A.

### Example 1.10 (page 21)

If P is the set of prime numbers, then

    P̅ = ℕ − P = {1, 4, 6, 8, 9, 10, 12, …}.

Thus P̅ is the set of composite numbers and 1.

### Example 1.11 (page 21)

Let A = {(x, x²) : x ∈ ℝ} be the graph of y = x², with universal set ℝ².
Then

    A̅ = ℝ² − A = {(x,y) ∈ ℝ² : y ≠ x²}.

## 1.7 Venn Diagrams

### Venn diagram (page 22)

In thinking about sets it is sometimes helpful to draw informal, schematic
diagrams of them, representing a set with a circle (or oval) regarded as
enclosing all the elements of the set. Such graphical representations of
sets are called _Venn diagrams_, after their inventor, British logician John
Venn, 1834–1923.

You are unlikely to draw Venn diagrams as part of a proof, but they are
useful "scratch work" devices.

### associativity, and why parentheses matter (page 23)

    A ∩ B ∩ C = (A ∩ B) ∩ C = A ∩ (B ∩ C)
    A ∪ B ∪ C = (A ∪ B) ∪ C = A ∪ (B ∪ C)

but in general

    (A ∪ B) ∩ C ≠ A ∪ (B ∩ C).

### Important Points (page 24)

  - If an expression involving sets uses only ∪, then parentheses are
    optional.
  - If an expression involving sets uses only ∩, then parentheses are
    optional.
  - If an expression uses both ∪ and ∩, then parentheses are **essential**.

So an expression such as A ∪ B ∩ C is absolutely meaningless, because we
can't tell whether it means (A ∪ B) ∩ C or A ∪ (B ∩ C).

## 1.8 Indexed Sets

### indexed sets (page 25)

When a problem involves lots of sets it is often convenient to keep track of
them using subscripts (also called _indices_): A₁, A₂, A₃ rather than A, B,
C. These are called _indexed sets_.

### Definition 1.7 (page 25)

Suppose A₁, A₂, …, Aₙ are sets. Then

    A₁ ∪ A₂ ∪ A₃ ∪ ⋯ ∪ Aₙ = {x : x ∈ Aᵢ for at least one set Aᵢ, for 1 ≤ i ≤ n},
    A₁ ∩ A₂ ∩ A₃ ∩ ⋯ ∩ Aₙ = {x : x ∈ Aᵢ for every set Aᵢ, for 1 ≤ i ≤ n}.

### ⋃ and ⋂ notation (page 25)

Given sets A₁, A₂, A₃, …, Aₙ, we define

    ⋃_{i=1}^{n} Aᵢ = A₁ ∪ A₂ ∪ A₃ ∪ ⋯ ∪ Aₙ,
    ⋂_{i=1}^{n} Aᵢ = A₁ ∩ A₂ ∩ A₃ ∩ ⋯ ∩ Aₙ.

The notation is also used when the list of sets is infinite (page 26):

    ⋃_{i=1}^{∞} Aᵢ = A₁ ∪ A₂ ∪ A₃ ∪ ⋯ = {x : x ∈ Aᵢ for at least one set Aᵢ with 1 ≤ i},
    ⋂_{i=1}^{∞} Aᵢ = A₁ ∩ A₂ ∩ A₃ ∩ ⋯ = {x : x ∈ Aᵢ for every set Aᵢ with 1 ≤ i}.

### Example 1.12 (page 25)

With A₁ = {0,2,5}, A₂ = {1,2,5}, A₃ = {2,5,7}:

    ⋃_{i=1}^{3} Aᵢ = {0, 1, 2, 5, 7},   ⋂_{i=1}^{3} Aᵢ = {2, 5}.

### Example 1.13 (page 26)

With A₁ = {−1,0,1}, A₂ = {−2,0,2}, A₃ = {−3,0,3}, …, Aᵢ = {−i, 0, i}, …:

    ⋃_{i=1}^{∞} Aᵢ = ℤ,   ⋂_{i=1}^{∞} Aᵢ = {0}.

### index set, I (page 26)

We can write ⋃_{i=1}^{3} Aᵢ = ⋃_{i ∈ {1,2,3}} Aᵢ, and likewise
⋃_{i=1}^{∞} Aᵢ = ⋃_{i ∈ ℕ} Aᵢ, and similarly for ⋂.

In general we have a collection of sets Aᵢ for i ∈ I, where I is the set of
possible subscripts. The set I is called an _index set_.

I need not consist of integers — we can subscript with letters or real
numbers. To avoid the reflex of reading i as an integer, use α, not i, for
an element of I.

### Definition 1.8 (page 26)

If A_α is a set for every α in some index set I ≠ ∅, then

    ⋃_{α ∈ I} A_α = {x : x ∈ A_α for at least one set A_α with α ∈ I},
    ⋂_{α ∈ I} A_α = {x : x ∈ A_α for every set A_α with α ∈ I}.

### Example 1.14 (page 27)

Index set I = [0,2] = {x ∈ ℝ : 0 ≤ x ≤ 2}. For each α ∈ I define
A_α = [α, 2] × [0, α], the rectangle in the x-y plane whose base runs from α
to 2 on the x-axis and whose height is α.

Note A₀ = [0,2] × {0} is the interval [0,2] on the x-axis (a "flat"
rectangle), and A₂ = {2} × [0,2] is a vertical segment.

    ⋃_{α ∈ I} A_α = the triangle with vertices (0,0), (2,0), (2,2),
    ⋂_{α ∈ I} A_α = {(2, 0)}.

### Example 1.15 (page 28)

Here the sets are indexed by ℝ². For any (a,b) ∈ ℝ², let

    P_(a,b) = {(x,y,z) ∈ ℝ³ : ax + by = 0},

a plane in ℝ³ containing the z-axis. Since any two such planes intersect
along the z-axis, and the z-axis is a subset of every P_(a,b),

    ⋂_{(a,b) ∈ ℝ²} P_(a,b) = {(0,0,z) : z ∈ ℝ} = "the z-axis",
    ⋃_{(a,b) ∈ ℝ²} P_(a,b) = ℝ³.

(Note P_(0,0) = ℝ³ is the only P_(a,b) that is not a plane.)

## 1.9 Sets That Are Number Systems

### the well-ordering principle (page 30)

Any non-empty subset of ℕ has a smallest element. In other words, if A ⊆ ℕ
and A ≠ ∅, then there is an element x₀ ∈ A that is smaller than every other
element of A. Similarly, given b ∈ ℤ, any non-empty subset
A ⊆ {b, b+1, b+2, b+3, …} has a smallest element.

This says something special about the integers: the corresponding statement
for the positive reals is false. The subset A = {1/n : n ∈ ℕ} of the
positive reals has no smallest element, because for any x₀ = 1/n ∈ A there
is a smaller element 1/(n+1) ∈ A.

We accept the familiar commutative, associative and distributive properties
of ℤ, ℚ and ℝ, and the natural ordering of ℕ, ℤ, ℚ and ℝ, as ground rules
that need no proof.

### Fact 1.5 — the Division Algorithm (page 30)

Given integers a and b with b > 0, there exist unique integers q and r for
which a = qb + r and 0 ≤ r < b.

This follows from the well-ordering principle: given a, b with b > 0, form

    A = {a − xb : x ∈ ℤ, 0 ≤ a − xb} ⊆ {0, 1, 2, 3, …}.

By the well-ordering principle A has a smallest element r = a − qb for some
q ∈ ℤ, so a = qb + r, and 0 ≤ r since r ∈ A. If r ≥ b, then
r − b = a − (q+1)b would be a smaller element of A than r, a contradiction.
Hence 0 ≤ r < b. (Uniqueness is Exercise 28 of Chapter 7.)

### numbers as sets (page 31)

Any number can itself be understood as a set. Begin with 0 = ∅. Then
1 = {∅} = {0}, and 2 = {∅, {∅}} = {0, 1}, and 3 = {∅, {∅}, {∅,{∅}}} =
{0, 1, 2}. In general the natural number n is the set n = {0, 1, 2, …, n−1}
of the n numbers (which are themselves sets) that come before it.

## 1.10 Russell's Paradox

Background information, not used in the remainder of the book.

### Russell's paradox (page 32)

Russell's paradox involves the set of all sets that do not include
themselves as elements:

    A = {X : X is a set and X ∉ X}.                          (1.1)

Most sets are in A: ℤ ∉ ℤ, so ℤ ∈ A; and ∅ ∈ A because ∅ is a set and
∅ ∉ ∅. But B = {{{{…}}}} — a box containing a box, containing a box,
forever — has just one element, namely B itself, so B ∈ B and hence B ∉ A.

The paradox arises from the question "Is A an element of A?" Equation (1.1)
says X ∈ A means the same thing as X ∉ X. Taking X = A: A ∈ A means the same
thing as A ∉ A. If A ∈ A is true, then it is false; if A ∈ A is false, then
it is true.

### the Zermelo-Fraenkel axioms (page 32)

The paradox instigated a careful examination of what can and cannot be
regarded as a set, and mathematicians eventually settled upon the
_Zermelo-Fraenkel axioms_. One of these is the well-ordering principle.
Another, the _axiom of foundation_, states that no non-empty set X is
allowed to have the property X ∩ x ≠ ∅ for all its elements x. This rules
out circularly defined "sets" such as B = {B}.
