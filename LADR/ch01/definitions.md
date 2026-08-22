# Chapter 1 definitions — Vector Spaces

Numbered items are a single continuous sequence covering definitions,
notation, examples, and results. Cite by number.

## 1A — 𝐑ⁿ and 𝐂ⁿ

### 1.1 definition: complex numbers, 𝐂 (page 2)

  - A _complex number_ is an ordered pair (a, b), where a, b ∈ 𝐑, but we will
    write this as a + bi.
  - The set of all complex numbers is denoted by 𝐂:

    𝐂 = {a + bi : a, b ∈ 𝐑}.

  - _Addition_ and _multiplication_ on 𝐂 are defined by

    (a + bi) + (c + di) = (a + c) + (b + d)i,
    (a + bi)(c + di) = (ac − bd) + (ad + bc)i;

  here a, b, c, d ∈ 𝐑.

If a ∈ 𝐑, we identify a + 0i with the real number a. Thus 𝐑 ⊆ 𝐂. We usually
write 0 + bi as just bi, and 0 + 1i as just i. Note i² = −1.

### 1.3 properties of complex arithmetic (page 3)

commutativity
  α + β = β + α and αβ = βα for all α, β ∈ 𝐂

associativity
  (α + β) + λ = α + (β + λ) and (αβ)λ = α(βλ) for all α, β, λ ∈ 𝐂

identities
  λ + 0 = λ and λ1 = λ for all λ ∈ 𝐂

additive inverse
  For every α ∈ 𝐂, there exists a unique β ∈ 𝐂 such that α + β = 0

multiplicative inverse
  For every α ∈ 𝐂 with α ≠ 0, there exists a unique β ∈ 𝐂 such that αβ = 1

distributive property
  λ(α + β) = λα + λβ for all λ, α, β ∈ 𝐂

### 1.5 definition: −α, subtraction, 1/α, division (page 4)

Suppose α, β ∈ 𝐂.

  - Let −α denote the additive inverse of α. Thus −α is the unique complex
    number such that

    α + (−α) = 0.

  - _Subtraction_ on 𝐂 is defined by

    β − α = β + (−α).

  - For α ≠ 0, let 1/α and ¹⁄ₐ denote the multiplicative inverse of α. Thus
    1/α is the unique complex number such that

    α(1/α) = 1.

  - For α ≠ 0, _division_ by α is defined by

    β/α = β(1/α).

### 1.6 notation: 𝐅 (page 4)

Throughout this book, 𝐅 stands for either 𝐑 or 𝐂.

Elements of 𝐅 are called _scalars_. For α ∈ 𝐅 and m a positive integer, αᵐ
denotes the product of α with itself m times. Hence (αᵐ)ⁿ = αᵐⁿ and
(αβ)ᵐ = αᵐβᵐ for all α, β ∈ 𝐅 and all positive integers m, n.

### 1.7 example: 𝐑² and 𝐑³ (page 5)

  - 𝐑² = {(x, y) : x, y ∈ 𝐑}  (think of it as a plane)
  - 𝐑³ = {(x, y, z) : x, y, z ∈ 𝐑}  (think of it as ordinary space)

### 1.8 definition: list, length (page 5)

  - Suppose n is a nonnegative integer. A _list_ of _length_ n is an ordered
    collection of n elements (which might be numbers, other lists, or more
    abstract objects).
  - Two lists are equal if and only if they have the same length and the same
    elements in the same order.

A list of length n might look like (z₁, …, zₙ). A list of length 0 looks like
( ). Lists differ from finite sets in two ways: in lists, order matters and
repetitions have meaning; in sets, order and repetitions are irrelevant.

### 1.10 notation: n (page 6)

Fix a positive integer n for the rest of this chapter.

### 1.11 definition: 𝐅ⁿ, coordinate (page 6)

𝐅ⁿ is the set of all lists of length n of elements of 𝐅:

  𝐅ⁿ = {(x₁, …, xₙ) : x_k ∈ 𝐅 for k = 1, …, n}.

For (x₁, …, xₙ) ∈ 𝐅ⁿ and k ∈ {1, …, n}, we say that x_k is the kᵗʰ
_coordinate_ of (x₁, …, xₙ).

### 1.13 definition: addition in 𝐅ⁿ (page 6)

_Addition_ in 𝐅ⁿ is defined by adding corresponding coordinates:

  (x₁, …, xₙ) + (y₁, …, yₙ) = (x₁ + y₁, …, xₙ + yₙ).

### 1.14 commutativity of addition in 𝐅ⁿ (page 7)

If x, y ∈ 𝐅ⁿ, then x + y = y + x.

### 1.15 notation: 0 (page 7)

Let 0 denote the list of length n whose coordinates are all 0:

  0 = (0, …, 0).

### 1.17 definition: additive inverse in 𝐅ⁿ, −x (page 9)

For x ∈ 𝐅ⁿ, the _additive inverse_ of x, denoted by −x, is the vector
−x ∈ 𝐅ⁿ such that

  x + (−x) = 0.

Thus if x = (x₁, …, xₙ), then −x = (−x₁, …, −xₙ).

### 1.18 definition: scalar multiplication in 𝐅ⁿ (page 9)

The _product_ of a number λ and a vector in 𝐅ⁿ is computed by multiplying
each coordinate of the vector by λ:

  λ(x₁, …, xₙ) = (λx₁, …, λxₙ);

here λ ∈ 𝐅 and (x₁, …, xₙ) ∈ 𝐅ⁿ.

### Digression on fields (page 10)

A _field_ is a set containing at least two distinct elements called 0 and 1,
along with operations of addition and multiplication satisfying all
properties listed in 1.3. Thus 𝐑 and 𝐂 are fields, as is the set of rational
numbers, and the set {0, 1} with 1 + 1 defined to equal 0.

## 1B — Definition of Vector Space

### 1.19 definition: addition, scalar multiplication (page 12)

  - An _addition_ on a set V is a function that assigns an element u + v ∈ V
    to each pair of elements u, v ∈ V.
  - A _scalar multiplication_ on a set V is a function that assigns an element
    λv ∈ V to each λ ∈ 𝐅 and each v ∈ V.

### 1.20 definition: vector space (page 12)

A _vector space_ is a set V along with an addition on V and a scalar
multiplication on V such that the following properties hold.

commutativity
  u + v = v + u for all u, v ∈ V.

associativity
  (u + v) + w = u + (v + w) and (ab)v = a(bv) for all u, v, w ∈ V and for all
  a, b ∈ 𝐅.

additive identity
  There exists an element 0 ∈ V such that v + 0 = v for all v ∈ V.

additive inverse
  For every v ∈ V, there exists w ∈ V such that v + w = 0.

multiplicative identity
  1v = v for all v ∈ V.

distributive properties
  a(u + v) = au + av and (a + b)v = av + bv for all a, b ∈ 𝐅 and all u, v ∈ V.

### 1.21 definition: vector, point (page 12)

Elements of a vector space are called _vectors_ or _points_.

### 1.22 definition: real vector space, complex vector space (page 13)

  - A vector space over 𝐑 is called a _real vector space_.
  - A vector space over 𝐂 is called a _complex vector space_.

### 1.23 example: 𝐅^∞ (page 13)

𝐅^∞ is defined to be the set of all sequences of elements of 𝐅:

  𝐅^∞ = {(x₁, x₂, …) : x_k ∈ 𝐅 for k = 1, 2, …}.

Addition and scalar multiplication on 𝐅^∞ are defined as expected:

  (x₁, x₂, …) + (y₁, y₂, …) = (x₁ + y₁, x₂ + y₂, …),
  λ(x₁, x₂, …) = (λx₁, λx₂, …).

### 1.24 notation: 𝐅^S (page 13)

  - If S is a set, then 𝐅^S denotes the set of functions from S to 𝐅.
  - For f, g ∈ 𝐅^S, the _sum_ f + g ∈ 𝐅^S is the function defined by

    (f + g)(x) = f(x) + g(x)

    for all x ∈ S.
  - For λ ∈ 𝐅 and f ∈ 𝐅^S, the _product_ λf ∈ 𝐅^S is the function defined by

    (λf)(x) = λf(x)

    for all x ∈ S.

### 1.25 example: 𝐅^S is a vector space (page 14)

  - If S is a nonempty set, then 𝐅^S (with the operations above) is a vector
    space over 𝐅.
  - The additive identity of 𝐅^S is the function 0 : S → 𝐅 defined by
    0(x) = 0 for all x ∈ S.
  - For f ∈ 𝐅^S, the additive inverse of f is the function −f : S → 𝐅 defined
    by (−f)(x) = −f(x) for all x ∈ S.

Note 𝐅ⁿ is the special case 𝐅^{1,2,…,n}, and 𝐅^∞ is 𝐅^{1,2,…}.

### 1.26 unique additive identity (page 14)

A vector space has a unique additive identity.

### 1.27 unique additive inverse (page 15)

Every element in a vector space has a unique additive inverse.

### 1.28 notation: −v, w − v (page 15)

Let v, w ∈ V. Then

  - −v denotes the additive inverse of v;
  - w − v is defined to be w + (−v).

### 1.29 notation: V (page 15)

For the rest of this book, V denotes a vector space over 𝐅.

### 1.30 the number 0 times a vector (page 15)

0v = 0 for every v ∈ V.

(The 0 on the left is the scalar 0 ∈ 𝐅; the 0 on the right is the additive
identity of V. The proof must use the distributive property, since that is
the only part of the definition connecting addition and scalar
multiplication.)

### 1.31 a number times the vector 0 (page 16)

a0 = 0 for every a ∈ 𝐅.

### 1.32 the number −1 times a vector (page 16)

(−1)v = −v for every v ∈ V.

## 1C — Subspaces

### 1.33 definition: subspace (page 18)

A subset U of V is called a _subspace_ of V if U is also a vector space with
the same additive identity, addition, and scalar multiplication as on V.

### 1.34 conditions for a subspace (page 18)

A subset U of V is a subspace of V if and only if U satisfies the following
three conditions.

additive identity
  0 ∈ U.

closed under addition
  u, w ∈ U implies u + w ∈ U.

closed under scalar multiplication
  a ∈ 𝐅 and u ∈ U implies au ∈ U.

### 1.35 example: subspaces (page 19)

(a) If b ∈ 𝐅, then {(x₁, x₂, x₃, x₄) ∈ 𝐅⁴ : x₃ = 5x₄ + b} is a subspace of 𝐅⁴
    if and only if b = 0.
(b) The set of continuous real-valued functions on the interval [0, 1] is a
    subspace of 𝐑^{[0,1]}.
(c) The set of differentiable real-valued functions on 𝐑 is a subspace of 𝐑^𝐑.
(d) The set of differentiable real-valued functions f on the interval (0, 3)
    such that f′(2) = b is a subspace of 𝐑^{(0,3)} if and only if b = 0.
(e) The set of all sequences of complex numbers with limit 0 is a subspace of
    𝐂^∞.

{0} is the smallest subspace of V, and V itself is the largest. The subspaces
of 𝐑² are precisely {0}, all lines in 𝐑² containing the origin, and 𝐑². The
subspaces of 𝐑³ are precisely {0}, all lines in 𝐑³ containing the origin, all
planes in 𝐑³ containing the origin, and 𝐑³.

### 1.36 definition: sum of subspaces (page 19)

Suppose V₁, …, V_m are subspaces of V. The _sum_ of V₁, …, V_m, denoted by
V₁ + ⋯ + V_m, is the set of all possible sums of elements of V₁, …, V_m. More
precisely,

  V₁ + ⋯ + V_m = {v₁ + ⋯ + v_m : v₁ ∈ V₁, …, v_m ∈ V_m}.

### 1.40 sum of subspaces is the smallest containing subspace (page 21)

Suppose V₁, …, V_m are subspaces of V. Then V₁ + ⋯ + V_m is the smallest
subspace of V containing V₁, …, V_m.

### 1.41 definition: direct sum, ⊕ (page 21)

Suppose V₁, …, V_m are subspaces of V.

  - The sum V₁ + ⋯ + V_m is called a _direct sum_ if each element of
    V₁ + ⋯ + V_m can be written in only one way as a sum v₁ + ⋯ + v_m, where
    each v_k ∈ V_k.
  - If V₁ + ⋯ + V_m is a direct sum, then V₁ ⊕ ⋯ ⊕ V_m denotes V₁ + ⋯ + V_m,
    with the ⊕ notation serving as an indication that this is a direct sum.

### 1.44 example: a sum that is not a direct sum (page 22)

With V₁ = {(x, y, 0) ∈ 𝐅³}, V₂ = {(0, 0, z) ∈ 𝐅³}, V₃ = {(0, y, 0) ∈ 𝐅³}, we
have 𝐅³ = V₁ + V₂ + V₃ but the sum is not direct, since

  (0, 0, 0) = (0, 1, 0) + (0, 0, 1) + (0, −1, −1)
            = (0, 0, 0) + (0, 0, 0) + (0, 0, 0).

Note V₁ ∩ V₂ = V₁ ∩ V₃ = V₂ ∩ V₃ = {0} — pairwise trivial intersection is
_not_ enough for a direct sum of more than two subspaces.

### 1.45 condition for a direct sum (page 23)

Suppose V₁, …, V_m are subspaces of V. Then V₁ + ⋯ + V_m is a direct sum if
and only if the only way to write 0 as a sum v₁ + ⋯ + v_m, where each
v_k ∈ V_k, is by taking each v_k equal to 0.

### 1.46 direct sum of two subspaces (page 23)

Suppose U and W are subspaces of V. Then

  U + W is a direct sum ⟺ U ∩ W = {0}.
