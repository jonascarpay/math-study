# Chapter 2 definitions — Finite-Dimensional Vector Spaces

Numbered items are a single continuous sequence covering definitions,
notation, examples, and results. Cite by number.

Standing assumptions for this chapter (page 27):

  - 𝐅 denotes 𝐑 or 𝐂.
  - V denotes a vector space over 𝐅.

## 2A — Span and Linear Independence

### 2.1 notation: list of vectors (page 28)

We will usually write lists of vectors without surrounding parentheses.

For example, (4, 1, 6), (9, 5, 7) is a list of length two of vectors in 𝐑³.

### 2.2 definition: linear combination (page 28)

A _linear combination_ of a list v₁, …, v_m of vectors in V is a vector of the
form

  a₁v₁ + ⋯ + a_m v_m,

where a₁, …, a_m ∈ 𝐅.

### 2.3 example: linear combinations in 𝐑³ (page 28)

  - (17, −4, 2) is a linear combination of (2, 1, −3), (1, −2, 4), because

    (17, −4, 2) = 6(2, 1, −3) + 5(1, −2, 4).

  - (17, −4, 5) is not a linear combination of (2, 1, −3), (1, −2, 4), because
    the system

      17 = 2a₁ + a₂
      −4 = a₁ − 2a₂
      5 = −3a₁ + 4a₂

    has no solutions.

### 2.4 definition: span (page 29)

The set of all linear combinations of a list of vectors v₁, …, v_m in V is
called the _span_ of v₁, …, v_m, denoted by span(v₁, …, v_m). In other words,

  span(v₁, …, v_m) = {a₁v₁ + ⋯ + a_m v_m : a₁, …, a_m ∈ 𝐅}.

The span of the empty list ( ) is defined to be {0}.

### 2.6 span is the smallest containing subspace (page 29)

The span of a list of vectors in V is the smallest subspace of V containing
all vectors in the list.

### 2.7 definition: spans (page 29)

If span(v₁, …, v_m) equals V, we say that the list v₁, …, v_m _spans_ V.

### 2.8 example: a list that spans 𝐅ⁿ (page 30)

Suppose n is a positive integer. The list

  (1, 0, …, 0), (0, 1, 0, …, 0), …, (0, …, 0, 1)

spans 𝐅ⁿ. Here the kᵗʰ vector in the list has 1 in the kᵗʰ slot and 0 in all
other slots. Indeed, for (x₁, …, xₙ) ∈ 𝐅ⁿ,

  (x₁, …, xₙ) = x₁(1, 0, …, 0) + x₂(0, 1, 0, …, 0) + ⋯ + xₙ(0, …, 0, 1).

### 2.9 definition: finite-dimensional vector space (page 30)

A vector space is called _finite-dimensional_ if some list of vectors in it
spans the space.

(Recall that by definition every list has finite length. Thus 𝐅ⁿ is
finite-dimensional for every positive integer n, by 2.8.)

### 2.10 definition: polynomial, 𝒫(𝐅) (page 30)

  - A function p : 𝐅 → 𝐅 is called a _polynomial with coefficients in 𝐅_ if
    there exist a₀, …, a_m ∈ 𝐅 such that

      p(z) = a₀ + a₁z + a₂z² + ⋯ + a_m zᵐ

    for all z ∈ 𝐅.
  - 𝒫(𝐅) is the set of all polynomials with coefficients in 𝐅.

With the usual operations of addition and scalar multiplication, 𝒫(𝐅) is a
vector space over 𝐅, and hence is a subspace of 𝐅^𝐅.

The coefficients of a polynomial are uniquely determined by the polynomial
(proved later — see 4.8).

### 2.11 definition: degree of a polynomial, deg p (page 31)

  - A polynomial p ∈ 𝒫(𝐅) is said to have _degree_ m if there exist scalars
    a₀, a₁, …, a_m ∈ 𝐅 with a_m ≠ 0 such that for every z ∈ 𝐅, we have

      p(z) = a₀ + a₁z + ⋯ + a_m zᵐ.

  - The polynomial that is identically 0 is said to have degree −∞.
  - The degree of a polynomial p is denoted by deg p.

### 2.12 notation: 𝒫_m(𝐅) (page 31)

For m a nonnegative integer, 𝒫_m(𝐅) denotes the set of all polynomials with
coefficients in 𝐅 and degree at most m.

Convention: −∞ < m, so the polynomial 0 is in 𝒫_m(𝐅).

If m is a nonnegative integer, then 𝒫_m(𝐅) = span(1, z, …, zᵐ). Thus 𝒫_m(𝐅)
is finite-dimensional for each nonnegative integer m.

### 2.13 definition: infinite-dimensional vector space (page 31)

A vector space is called _infinite-dimensional_ if it is not
finite-dimensional.

### 2.14 example: 𝒫(𝐅) is infinite-dimensional (page 31)

Consider any list of elements of 𝒫(𝐅). Let m denote the highest degree of the
polynomials in this list. Then every polynomial in the span of this list has
degree at most m. Thus z^{m+1} is not in the span of our list. Hence no list
spans 𝒫(𝐅).

### 2.15 definition: linearly independent (page 32)

  - A list v₁, …, v_m of vectors in V is called _linearly independent_ if the
    only choice of a₁, …, a_m ∈ 𝐅 that makes

      a₁v₁ + ⋯ + a_m v_m = 0

    is a₁ = ⋯ = a_m = 0.
  - The empty list ( ) is also declared to be linearly independent.

v₁, …, v_m is linearly independent if and only if each vector in
span(v₁, …, v_m) has only one representation as a linear combination of
v₁, …, v_m.

### 2.16 example: linearly independent lists (page 32)

(a) (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0) is linearly independent in 𝐅⁴.
(b) For m a nonnegative integer, 1, z, …, zᵐ is linearly independent in 𝒫(𝐅).
(c) A list of length one in a vector space is linearly independent if and only
    if the vector in the list is not 0.
(d) A list of length two in a vector space is linearly independent if and only
    if neither of the two vectors in the list is a scalar multiple of the
    other.

If some vectors are removed from a linearly independent list, the remaining
list is also linearly independent (page 33).

### 2.17 definition: linearly dependent (page 33)

  - A list of vectors in V is called _linearly dependent_ if it is not
    linearly independent.
  - In other words, a list v₁, …, v_m of vectors in V is linearly dependent if
    there exist a₁, …, a_m ∈ 𝐅, not all 0, such that
    a₁v₁ + ⋯ + a_m v_m = 0.

### 2.18 example: linearly dependent lists (page 33)

  - (2, 3, 1), (1, −1, 2), (7, 3, 8) is linearly dependent in 𝐅³ because

      2(2, 3, 1) + 3(1, −1, 2) + (−1)(7, 3, 8) = (0, 0, 0).

  - If some vector in a list of vectors in V is a linear combination of the
    other vectors, then the list is linearly dependent.
  - Every list of vectors in V containing the 0 vector is linearly dependent.

### 2.19 linear dependence lemma (page 33)

Suppose v₁, …, v_m is a linearly dependent list in V. Then there exists
k ∈ {1, 2, …, m} such that

  v_k ∈ span(v₁, …, v_{k−1}).

Furthermore, if k satisfies the condition above and the kᵗʰ term is removed
from v₁, …, v_m, then the span of the remaining list equals span(v₁, …, v_m).

If k = 1, then v_k ∈ span(v₁, …, v_{k−1}) means that v₁ = 0, because
span( ) = {0} (page 34).

### 2.22 length of linearly independent list ≤ length of spanning list (page 35)

In a finite-dimensional vector space, the length of every linearly independent
list of vectors is less than or equal to the length of every spanning list of
vectors.

### 2.23 example: no list of length 4 is linearly independent in 𝐑³ (page 36)

The list (1, 0, 0), (0, 1, 0), (0, 0, 1), which has length three, spans 𝐑³.
Thus no list of length larger than three is linearly independent in 𝐑³.

### 2.24 example: no list of length 3 spans 𝐑⁴ (page 36)

The list (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), which has
length four, is linearly independent in 𝐑⁴. Thus no list of length less than
four spans 𝐑⁴.

### 2.25 finite-dimensional subspaces (page 36)

Every subspace of a finite-dimensional vector space is finite-dimensional.

## 2B — Bases

### 2.26 definition: basis (page 39)

A _basis_ of V is a list of vectors in V that is linearly independent and
spans V.

### 2.27 example: bases (page 39)

(a) The list (1, 0, …, 0), (0, 1, 0, …, 0), …, (0, …, 0, 1) is a basis of 𝐅ⁿ,
    called the _standard basis_ of 𝐅ⁿ.
(b) The list (1, 2), (3, 5) is a basis of 𝐅².
(c) The list (1, 2, −4), (7, −5, 6) is linearly independent in 𝐅³ but is not a
    basis of 𝐅³ because it does not span 𝐅³.
(d) The list (1, 2), (3, 5), (4, 13) spans 𝐅² but is not a basis of 𝐅² because
    it is not linearly independent.
(e) The list (1, 1, 0), (0, 0, 1) is a basis of {(x, x, y) ∈ 𝐅³ : x, y ∈ 𝐅}.
(f) The list (1, −1, 0), (1, 0, −1) is a basis of
    {(x, y, z) ∈ 𝐅³ : x + y + z = 0}.
(g) The list 1, z, …, zᵐ is a basis of 𝒫_m(𝐅), called the _standard basis_ of
    𝒫_m(𝐅).

### 2.28 criterion for basis (page 39)

A list v₁, …, vₙ of vectors in V is a basis of V if and only if every v ∈ V
can be written uniquely in the form

  2.29:  v = a₁v₁ + ⋯ + aₙvₙ,

where a₁, …, aₙ ∈ 𝐅.

### 2.30 every spanning list contains a basis (page 40)

Every spanning list in a vector space can be reduced to a basis of the vector
space.

### 2.31 basis of finite-dimensional vector space (page 41)

Every finite-dimensional vector space has a basis.

### 2.32 every linearly independent list extends to a basis (page 41)

Every linearly independent list of vectors in a finite-dimensional vector
space can be extended to a basis of the vector space.

### 2.33 every subspace of V is part of a direct sum equal to V (page 42)

Suppose V is finite-dimensional and U is a subspace of V. Then there is a
subspace W of V such that V = U ⊕ W.

## 2C — Dimension

### 2.34 basis length does not depend on basis (page 44)

Any two bases of a finite-dimensional vector space have the same length.

### 2.35 definition: dimension, dim V (page 44)

  - The _dimension_ of a finite-dimensional vector space is the length of any
    basis of the vector space.
  - The dimension of a finite-dimensional vector space V is denoted by dim V.

### 2.36 example: dimensions (page 44)

  - dim 𝐅ⁿ = n, because the standard basis of 𝐅ⁿ has length n.
  - dim 𝒫_m(𝐅) = m + 1, because the standard basis 1, z, …, zᵐ of 𝒫_m(𝐅) has
    length m + 1.
  - If U = {(x, x, y) ∈ 𝐅³ : x, y ∈ 𝐅}, then dim U = 2, because
    (1, 1, 0), (0, 0, 1) is a basis of U.
  - If U = {(x, y, z) ∈ 𝐅³ : x + y + z = 0}, then dim U = 2, because
    (1, −1, 0), (1, 0, −1) is a basis of U.

The role played by the choice of 𝐅 cannot be neglected: the real vector space
𝐑² has dimension two; the complex vector space 𝐂 has dimension one (page 45).

### 2.37 dimension of a subspace (page 45)

If V is finite-dimensional and U is a subspace of V, then dim U ≤ dim V.

### 2.38 linearly independent list of the right length is a basis (page 45)

Suppose V is finite-dimensional. Then every linearly independent list of
vectors in V of length dim V is a basis of V.

### 2.39 subspace of full dimension equals the whole space (page 45)

Suppose that V is finite-dimensional and U is a subspace of V such that
dim U = dim V. Then U = V.

### 2.42 spanning list of the right length is a basis (page 46)

Suppose V is finite-dimensional. Then every list of vectors in V that spans V
and has length dim V is a basis of V.

### 2.43 dimension of a sum (page 47)

If V₁ and V₂ are subspaces of a finite-dimensional vector space, then

  dim(V₁ + V₂) = dim V₁ + dim V₂ − dim(V₁ ∩ V₂).

### Analogy: finite sets vs. finite-dimensional vector spaces (page 48)

| sets | vector spaces |
|---|---|
| S is a finite set | V is a finite-dimensional vector space |
| #S | dim V |
| for subsets S₁, S₂ of S, the union S₁ ∪ S₂ is the smallest subset of S containing S₁ and S₂ | for subspaces V₁, V₂ of V, the sum V₁ + V₂ is the smallest subspace of V containing V₁ and V₂ |
| #(S₁ ∪ S₂) = #S₁ + #S₂ − #(S₁ ∩ S₂) | dim(V₁ + V₂) = dim V₁ + dim V₂ − dim(V₁ ∩ V₂) |
| #(S₁ ∪ S₂) = #S₁ + #S₂ ⟺ S₁ ∩ S₂ = ∅ | dim(V₁ + V₂) = dim V₁ + dim V₂ ⟺ V₁ ∩ V₂ = {0} |
| S₁ ∪ ⋯ ∪ S_m is a disjoint union ⟺ #(S₁ ∪ ⋯ ∪ S_m) = #S₁ + ⋯ + #S_m | V₁ + ⋯ + V_m is a direct sum ⟺ dim(V₁ + ⋯ + V_m) = dim V₁ + ⋯ + dim V_m |

The result in the last box is proved in 3.94.
