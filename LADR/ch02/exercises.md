# Exercises 2A, page 37

1. Find a list of four distinct vectors in 𝐅³ whose span equals

       {(x, y, z) ∈ 𝐅³ : x + y + z = 0}.

Write U = {(x, y, z) ∈ 𝐅³ : x + y + z = 0}. The list is

    (1, −1, 0), (1, 0, −1), (0, 0, 0), (2, −2, 0).

U ⊆ span: given (x, y, z) ∈ U,

    (x, y, z) = (−y − z, y, z)                    (set predicate)
              = −y(1, −1, 0) − z(1, 0, −1).

span ⊆ U: a linear combination

    x(1, −1, 0) + y(1, 0, −1) + w(0, 0, 0) + z(2, −2, 0)
      = (x + y + 2z, −x − 2z, −y)

fulfills the condition, since (x + y + 2z) + (−x − 2z) + (−y) = 0.

<!-- correct -->

2. Prove or give a counterexample: If v₁, v₂, v₃, v₄ spans V, then the list

       v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄

   also spans V.

True. Write L₁ = v₁, v₂, v₃, v₄ and L₂ = v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄.

span(L₂) ⊆ V: by 2.6, the span of a list of vectors in V is a subspace of V.

V ⊆ span(L₂): span(L₂) is a subspace containing L₂, so

    contains v₃ − v₄, v₄  ⟹  contains v₃
    contains v₂ − v₃, v₃  ⟹  contains v₂
    contains v₁ − v₂, v₂  ⟹  contains v₁

So span(L₂) is a subspace containing L₁, and by 2.6, span(L₁) is the smallest
such subspace, so V = span(L₁) ⊆ span(L₂).

<!-- correct -->

3. Suppose v₁, …, v_m is a list of vectors in V. For k ∈ {1, …, m}, let

       w_k = v₁ + ⋯ + v_k.

   Show that span(v₁, …, v_m) = span(w₁, …, w_m).

Write L₁ = v₁, …, v_m and L₂ = w₁, …, w_m, with w_k = v₁ + ⋯ + v_k.
Write U₁ = span(L₁) and U₂ = span(L₂). Claim U₁ = U₂.

U₂ ⊆ U₁:

  - every w in L₂ is a sum of v's in U₁,
  - U₁ is a subspace,
  - so every w in L₂ is in U₁,
  - so span of the w's is a subspace of U₁ (2.6).

U₁ ⊆ U₂: in other words, ∀k. v_k ∈ U₂.

  - obvious for k = 1, and for k > 1:
  - v_k = w_k − w_{k−1},
  - w_k and w_{k−1} are in U₂,
  - so v_k is in U₂.

<!-- correct -->

4. (a) Show that a list of length one in a vector space is linearly
       independent if and only if the vector in the list is not 0.

   (b) Show that a list of length two in a vector space is linearly
       independent if and only if neither of the two vectors in the list is a
       scalar multiple of the other.

(a) Negate both sides; the claim becomes

    the list v is linearly dependent ⟺ v = 0,

where by 2.15 and 2.17 the left side is ∃a ∈ 𝐅. (av = 0 ∧ a ≠ 0).

(⟹) Let a ∈ 𝐅 with av = 0 and a ≠ 0. Scale by 1/a:

      v = 1v = ((1/a)a)v = (1/a)(av) = (1/a)0 = 0.

(⟸) Assume v = 0. Take a = 1: then av = 0 and a ≠ 0.

(b) For v, w ∈ V, "neither is a scalar multiple of the other" is

    ¬(∃c ∈ 𝐅. v = cw) ∧ ¬(∃c ∈ 𝐅. w = cv).

Negate both sides; the claim becomes

    ∃a, b ∈ 𝐅. (av + bw = 0 ∧ (a ≠ 0 ∨ b ≠ 0))
      ⟺ (∃c ∈ 𝐅. v = cw) ∨ (∃c ∈ 𝐅. w = cv).

(⟹) Let a, b ∈ 𝐅 with av + bw = 0 and a ≠ 0 or b ≠ 0.

  - a ≠ 0: scale by 1/a:

      v + (b/a)w = 0,  so  v = (−b/a)w;

    take c = −b/a.
  - b ≠ 0: same argument, giving w = (−a/b)v.

(⟸) Assume v = cw for some c ∈ 𝐅. Take a = 1, b = −c:

    av + bw = cw − cw = 0,  and  a = 1 ≠ 0.

Same argument for w = cv.

<!-- correct -->

5. Find a number t such that

       (3, 1, 4), (2, −3, 5), (5, 9, t)

   is not linearly independent in 𝐑³.

t = 2, since

    3(3, 1, 4) − 2(2, −3, 5) − 1(5, 9, t)
      = (9 − 4 − 5, 3 + 6 − 9, 12 − 10 − t)
      = (0, 0, 2 − t),

which is 0 for t = 2, with coefficients 3, −2, −1 not all 0.

<!-- correct -->

6. Show that the list (2, 3, 1), (1, −1, 2), (7, 3, c) is linearly dependent in
   𝐅³ if and only if c = 8.

Fix c ∈ 𝐅, and write v₁, v₂, v₃ for the three vectors. The system
x v₁ + y v₂ + z v₃ = 0 is

    2x +  y + 7z = 0    (1)
    3x −  y + 3z = 0    (2)
     x + 2y + cz = 0    (3)

Each step below replaces one equation by an equivalent one, given the others:

    (2)  ⟺  y = 3x + 3z
    (1)  ⟺  2x + (3x + 3z) + 7z = 5x + 10z = 0  ⟺  x = −2z
    (3)  ⟺  −2z − 12z + 6z + cz = −8z + cz = 0  ⟺  8z = cz

So x v₁ + y v₂ + z v₃ = 0 ⟺ (x = −2z and y = −3z and 8z = cz), and the list
is linearly dependent iff

    ∃x, y, z ∈ 𝐅, not all 0, with x = −2z, y = −3z, 8z = cz.

(⟸) Assume c = 8. Take z = 1, y = −3, x = −2: then 8z = cz, and x, y, z are
not all 0.

(⟹) Fix such x, y, z. From x = −2z, x ≠ 0 iff z ≠ 0, and likewise y ≠ 0 iff
z ≠ 0 from y = −3z, so all three are nonzero. Then from 8z = cz with z ≠ 0,

    c = 1c = (1/z)zc = (1/z)(8z) = 8.

<!-- correct -->

7. (a) Show that if we think of 𝐂 as a vector space over 𝐑, then the list
       1 + i, 1 − i is linearly independent.

   (b) Show that if we think of 𝐂 as a vector space over 𝐂, then the list
       1 + i, 1 − i is linearly dependent.

(a) Assume a(1 + i) + b(1 − i) = 0, with a, b ∈ 𝐑; show a = b = 0.

    a + ai + b − bi = 0
    a + ai = −b + bi

With a, b ∈ 𝐑, this is an equality between complex numbers, and two complex
numbers are equal iff their coefficients are equal (1.1), so

    a = −b  and  a = b,

hence a = −a, so a = b = 0.

(b) There exist a, b ∈ 𝐂, not both 0, with a(1 + i) + b(1 − i) = 0:

    (1 − i)(1 + i) + (−1 − i)(1 − i) = 2 − 2 = 0.

<!-- correct -->

8. Suppose v₁, v₂, v₃, v₄ is linearly independent in V. Prove that the list

       v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄

   is also linearly independent.

Write H for the linear independence of v₁, v₂, v₃, v₄. The list
v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄ is linearly independent iff

    a(v₁ − v₂) + b(v₂ − v₃) + c(v₃ − v₄) + d v₄ = 0  ⟹  a = b = c = d = 0,

i.e. iff

    a v₁ + (b − a) v₂ + (c − b) v₃ + (d − c) v₄ = 0  ⟹  a = b = c = d = 0.

Instantiate H with a, b − a, c − b, d − c, giving a = b − a = c − b = d − c = 0.
Then a = 0 gives b − a = b = 0, gives c − b = c = 0, gives d − c = d = 0.

<!-- correct -->

9. Prove or give a counterexample: If v₁, v₂, …, v_m is a linearly independent
   list of vectors in V, then

       5v₁ − 4v₂, v₂, v₃, …, v_m

   is linearly independent.

True. Write H for the linear independence of v₁, …, v_m.

Goal: a(5v₁ − 4v₂) + b v₂ + c v₃ + ⋯ + z v_m = 0 ⟹ a = b = c = ⋯ = z = 0.

Assume I: a(5v₁ − 4v₂) + b v₂ + c v₃ + ⋯ + z v_m = 0. Rewriting I,

    5a v₁ + (b − 4a) v₂ + c v₃ + ⋯ + z v_m = 0.

Instantiating H with 5a, b − 4a, c, …, z gives 5a = b − 4a = c = ⋯ = z = 0.
Then 5a = 0 gives a = 0, and b − 4a = b = 0.

<!-- correct -->

10. Prove or give a counterexample: If v₁, v₂, …, v_m is a linearly independent
    list of vectors in V and λ ∈ 𝐅 with λ ≠ 0, then λv₁, λv₂, …, λv_m is
    linearly independent.

Assume

    a₁(λv₁) + ⋯ + a_m(λv_m)
      = λ(a₁v₁) + ⋯ + λ(a_m v_m)      (assoc., comm. of scalar mult.)
      = λ(a₁v₁ + ⋯ + a_m v_m)          (distributivity)
      = 0.

Multiplying both sides by 1/λ gives

    a₁v₁ + ⋯ + a_m v_m = 0.

Applying H gives a₁ = ⋯ = a_m = 0.

<!-- correct -->

11. Prove or give a counterexample: If v₁, …, v_m and w₁, …, w_m are linearly
    independent lists of vectors in V, then the list v₁ + w₁, …, v_m + w_m is
    linearly independent.

Counterexample. Take m = 1, V = 𝐅, v₁ = 1, w₁ = −1.

The lists 1 and −1 are each linearly independent, since a list of length one is
linearly independent iff its vector is not 0 (2.16(c)).

But v₁ + w₁ = 1 + (−1) = 0, and every list containing the 0 vector is linearly
dependent (2.18).

<!-- correct -->

12. Suppose v₁, …, v_m is linearly independent in V and w ∈ V. Prove that if
    v₁ + w, …, v_m + w is linearly dependent, then w ∈ span(v₁, …, v_m).

Fix a₁, …, a_m ∈ 𝐅 not all 0 such that

    a₁(v₁ + w) + ⋯ + a_m(v_m + w) = 0.

Rewriting,

    a₁v₁ + ⋯ + a_m v_m + (a₁ + ⋯ + a_m)w = 0.

Let u = a₁v₁ + ⋯ + a_m v_m and c = a₁ + ⋯ + a_m, so u + cw = 0.

u ≠ 0, by linear independence of v₁, …, v_m and the a_i not all being 0.

    u = −cw.

If c = 0 then u = 0w = 0 (1.30), contradiction; so c ≠ 0. Multiplying by
c′ = −1/c,

    c′u = w,
    c′a₁v₁ + ⋯ + c′a_m v_m = w,

so w ∈ span(v₁, …, v_m).

<!-- correct -->

13. Suppose v₁, …, v_m is linearly independent in V and w ∈ V. Show that

        v₁, …, v_m, w is linearly independent ⟺ w ∉ span(v₁, …, v_m).

<!-- skipped -->

14. Suppose v₁, …, v_m is a list of vectors in V. For k ∈ {1, …, m}, let

        w_k = v₁ + ⋯ + v_k.

    Show that the list v₁, …, v_m is linearly independent if and only if the
    list w₁, …, w_m is linearly independent.

(⟹) Assume

    a₁w₁ + a₂w₂ + ⋯ + a_m w_m
      = a₁v₁ + a₂(v₁ + v₂) + ⋯ + a_m(v₁ + v₂ + ⋯ + v_m)
      = (a₁ + a₂ + ⋯ + a_m)v₁ + (a₂ + ⋯ + a_m)v₂ + ⋯ + a_m v_m
      = 0.

Applying linear independence of v₁, …, v_m gives

    a₁ + a₂ + ⋯ + a_m = a₂ + ⋯ + a_m = ⋯ = a_{m−1} + a_m = a_m = 0.

Since a_m is zero, a_{m−1} is zero, and by the same process every element, so

    a₁ = a₂ = ⋯ = a_m = 0.

(⟸) Assume

    a₁v₁ + a₂v₂ + ⋯ + a_m v_m
      = a₁w₁ + a₂(w₂ − w₁) + ⋯ + a_m(w_m − w_{m−1})
      = (a₁ − a₂)w₁ + (a₂ − a₃)w₂ + ⋯ + (a_{m−1} − a_m)w_{m−1} + a_m w_m
      = 0.

Applying linear independence of w₁, …, w_m gives

    a₁ − a₂ = a₂ − a₃ = ⋯ = a_{m−1} − a_m = a_m = 0.

Since the last term is 0, the second-to-last term is zero, and by induction all
of them are, so

    a₁ = a₂ = ⋯ = a_m = 0.

<!-- correct -->

15. Explain why there does not exist a list of six polynomials that is linearly
    independent in 𝒫₄(𝐅).

2.22 states that any linearly independent list must have length ≤ the length of
any spanning list.

𝒫₄(𝐅) is spanned by 1, z, z², z³, z⁴, which has 5 elements.

Hence no linearly independent list of length 6 exists in 𝒫₄(𝐅).

<!-- correct -->

16. Explain why no list of four polynomials spans 𝒫₄(𝐅).

1, z, z², z³, z⁴ is linearly independent (2.16(b)).

By 2.22, no spanning list can be shorter than a linearly independent list.

<!-- correct -->

17. Prove that V is infinite-dimensional if and only if there is a sequence
    v₁, v₂, … of vectors in V such that v₁, …, v_m is linearly independent for
    every positive integer m.

<!-- skipped -->

18. Prove that 𝐅^∞ is infinite-dimensional.

<!-- skipped -->

19. Prove that the real vector space of all continuous real-valued functions on
    the interval [0, 1] is infinite-dimensional.

<!-- skipped -->

20. Suppose p₀, p₁, …, p_m are polynomials in 𝒫_m(𝐅) such that p_k(2) = 0 for
    each k ∈ {0, …, m}. Prove that p₀, p₁, …, p_m is not linearly independent
    in 𝒫_m(𝐅).

<!-- skipped -->

# Exercises 2B, page 42

1. Find all vector spaces that have exactly one basis.

Let V have a basis v₁, …, v_m. Then 2v₁, …, 2v_m is also a basis, since it is
linearly independent (2A.10, with λ = 2) and any v = a₁v₁ + ⋯ + a_m v_m
= (a₁/2)(2v₁) + ⋯ + (a_m/2)(2v_m).

Therefore, for the basis to be unique, v₁, …, v_m = 2v₁, …, 2v_m.

Since v = 2v ⟺ 0 = v, which violates linear independence (2.18), only the empty
list satisfies this.

The empty list spans only {0} (2.4).

<!-- correct -->

2. Verify all assertions in Example 2.27.

(a) The list (1, 0, …, 0), (0, 1, 0, …, 0), …, (0, …, 0, 1) is a basis of 𝐅ⁿ.

Linearly independent:

    a₁(1, …, 0) + ⋯ + aₙ(0, …, 1) = (a₁, …, 0) + ⋯ + (0, …, aₙ)
                                   = (a₁, …, aₙ) = 0
      ⟹ a₁ = ⋯ = aₙ = 0.

Spans:

    (a₁, …, aₙ) = (a₁, …, 0) + ⋯ + (0, …, aₙ)
                = a₁(1, …, 0) + ⋯ + aₙ(0, …, 1).

(b) The list (1, 2), (3, 5) is a basis of 𝐅².

Linearly independent:

    a₁(1, 2) + a₂(3, 5) = (a₁ + 3a₂, 2a₁ + 5a₂) = 0
      ⟹ a₁ + 3a₂ = 0, 2a₁ + 5a₂ = 0
      ⟹ a₁ = −3a₂, so −6a₂ + 5a₂ = −a₂ = 0, hence a₂ = a₁ = 0.

Spans: given (a, b), solve

    a₁ + 3a₂ = a
    2a₁ + 5a₂ = b

to get a₂ = 2a − b and a₁ = 3b − 5a, so

    (a, b) = (3b − 5a)(1, 2) + (2a − b)(3, 5).

(c) The list (1, 2, −4), (7, −5, 6) is linearly independent in 𝐅³ but does not
span 𝐅³.

Linearly independent: if it were not, by 2.16(d) there would be

  - a scalar a with a(1, 2, −4) = (7, −5, 6), i.e. a = 7 and 2a = −5;
  - a scalar b with (1, 2, −4) = b(7, −5, 6), i.e. 7b = 1 ⟺ b = 1/7 and
    2 = −5b ⟺ b = −2/5.

Does not span: (1, 0, 0), (0, 1, 0), (0, 0, 1) is linearly independent, so by
2.22 a spanning list must have length at least 3.

(d) The list (1, 2), (3, 5), (4, 13) spans 𝐅² but is not linearly independent.

Not linearly independent: (1, 0), (0, 1) is shorter and spans the space, so by
2.22 no linearly independent list has length 3.

Spans: by the computation in (b),

    (x, y) = (3y − 5x)(1, 2) + (2x − y)(3, 5).

(e) The list (1, 1, 0), (0, 0, 1) is a basis of U = {(x, x, y) ∈ 𝐅³ : x, y ∈ 𝐅}.

Linearly independent:

    a(1, 1, 0) + b(0, 0, 1) = (a, a, b) = 0 ⟹ a = b = 0.

U ⊆ span: (x, x, y) = x(1, 1, 0) + y(0, 0, 1).

span ⊆ U: a(1, 1, 0) + b(0, 0, 1) = (a, a, b) is in U, with x = a, y = b.

(f) The list (1, −1, 0), (1, 0, −1) is a basis of
U = {(x, y, z) ∈ 𝐅³ : x + y + z = 0}.

Linearly independent:

    a(1, −1, 0) + b(1, 0, −1) = (a + b, −a, −b) = 0
      ⟹ a + b = −a = −b = 0 ⟹ a = b = 0.

U ⊆ span: (x, y, z) ∈ U gives x = −y − z, so

    (x, y, z) = (−y − z, y, z) = −y(1, −1, 0) − z(1, 0, −1).

span ⊆ U: a(1, −1, 0) + b(1, 0, −1) = (a + b, −a, −b) is in U, since
(a + b) + (−a) + (−b) = 0.

(g) The list 1, z, …, zᵐ is a basis of 𝒫_m(𝐅).

Linearly independent:

    a₀1 + a₁z + ⋯ + a_m zᵐ = 0 = 0·1 + 0·z + ⋯ + 0·zᵐ
      ⟹ a₀ = a₁ = ⋯ = a_m = 0,

since the coefficients of a polynomial are uniquely determined by the
polynomial (2.10).

Spans:

    a₀ + a₁z + ⋯ + a_m zᵐ = a₀(1) + a₁(z) + ⋯ + a_m(zᵐ).

<!-- correct -->

3. (a) Let U be the subspace of 𝐑⁵ defined by

           U = {(x₁, x₂, x₃, x₄, x₅) ∈ 𝐑⁵ : x₁ = 3x₂ and x₃ = 7x₄}.

       Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝐑⁵.

   (c) Find a subspace W of 𝐑⁵ such that 𝐑⁵ = U ⊕ W.

<!-- skipped -->

4. (a) Let U be the subspace of 𝐂⁵ defined by

           U = {(z₁, z₂, z₃, z₄, z₅) ∈ 𝐂⁵ : 6z₁ = z₂ and z₃ + 2z₄ + 3z₅ = 0}.

       Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝐂⁵.

   (c) Find a subspace W of 𝐂⁵ such that 𝐂⁵ = U ⊕ W.

<!-- skipped -->

5. Suppose V is finite-dimensional and U, W are subspaces of V such that
   V = U + W. Prove that there exists a basis of V consisting of vectors in
   U ∪ W.

U and W are finite-dimensional by 2.25. Say

    U = span(u₁, …, u_m),  W = span(w₁, …, w_n).

By 1.36,

    V = U + W = {u + w : u ∈ span(u₁, …, u_m), w ∈ span(w₁, …, w_n)},

so any v ∈ V is of the form a₁u₁ + ⋯ + a_m u_m + b₁w₁ + ⋯ + b_n w_n. Hence

    V = span(u₁, …, u_m, w₁, …, w_n).

So we have a list of vectors in U ∪ W that spans V. By 2.30, this list contains
a basis.

<!-- correct -->

6. Prove or give a counterexample: If p₀, p₁, p₂, p₃ is a list in 𝒫₃(𝐅) such
   that none of the polynomials p₀, p₁, p₂, p₃ has degree 2, then
   p₀, p₁, p₂, p₃ is not a basis of 𝒫₃(𝐅).

Counterexample. The list

    1, z, z² + z³, z³

has degrees 0, 1, 3, 3, so none of its polynomials has degree 2, yet it is a
basis of 𝒫₃(𝐅).

Linearly independent:

    a₀1 + a₁z + a₂(z² + z³) + a₃z³ = a₀ + a₁z + a₂z² + (a₂ + a₃)z³ = 0
      ⟹ a₀ = a₁ = a₂ = a₂ + a₃ = 0 ⟹ a₃ = 0.

Spans:

    c₀ + c₁z + c₂z² + c₃z³ = c₀1 + c₁z + c₂(z² + z³) + (c₃ − c₂)z³,

and conversely a₀1 + a₁z + a₂(z² + z³) + a₃z³ = a₀ + a₁z + a₂z² + (a₂ + a₃)z³
is in 𝒫₃(𝐅).

<!-- correct -->

7. Suppose v₁, v₂, v₃, v₄ is a basis of V. Prove that

       v₁ + v₂, v₂ + v₃, v₃ + v₄, v₄

   is also a basis of V.

<!-- skipped -->

8. Prove or give a counterexample: If v₁, v₂, v₃, v₄ is a basis of V and U is a
   subspace of V such that v₁, v₂ ∈ U and v₃ ∉ U and v₄ ∉ U, then v₁, v₂ is a
   basis of U.

Counterexample. In V = 𝐅⁴, take the basis

    v₁ = (1, 0, 0, 0),  v₂ = (0, 1, 0, 0),
    v₃ = (0, 0, 1, 1),  v₄ = (0, 0, 1, −1)

and let U = span(u₁, u₂, u₃), where

    u₁ = (1, 0, 0, 0),  u₂ = (0, 1, 0, 0),  u₃ = (0, 0, 1, 0),

so U = {(a₁, a₂, a₃, 0) : a₁, a₂, a₃ ∈ 𝐅}.

U is a subspace of V, since it is the span of a list of vectors in V (2.6).

v₁, v₂ ∈ U, since v₁ = u₁ and v₂ = u₂.

v₃, v₄ ∉ U, since (0, 0, 1, ±1) = (a₁, a₂, a₃, 0) would require 1 = 0.

But span(v₁, v₂) = {(a₁, a₂, 0, 0) : a₁, a₂ ∈ 𝐅}, and u₃ = (0, 0, 1, 0) is not in
it, since that would require 1 = 0. So v₁, v₂ does not span U, and is not a
basis of U.

<!-- correct -->

9. Suppose v₁, …, v_m is a list of vectors in V. For k ∈ {1, …, m}, let

       w_k = v₁ + ⋯ + v_k.

   Show that v₁, …, v_m is a basis of V if and only if w₁, …, w_m is a basis
   of V.

<!-- skipped -->

10. Suppose U and W are subspaces of V such that V = U ⊕ W. Suppose also that
    u₁, …, u_m is a basis of U and w₁, …, wₙ is a basis of W. Prove that

        u₁, …, u_m, w₁, …, wₙ

    is a basis of V.

U = span(u₁, …, u_m),  W = span(w₁, …, wₙ).

Spans: by 1.36,

    V = {u + w : u ∈ span(u₁, …, u_m), w ∈ span(w₁, …, wₙ)},

so any v ∈ V has the form a₁u₁ + ⋯ + a_m u_m + b₁w₁ + ⋯ + bₙwₙ, and by
definition of span, any v is in span(u₁, …, u_m, w₁, …, wₙ).

Linearly independent: let v = u + w with u ∈ U and w ∈ W, and assume v = 0.
Then

    u + w = 0 ⟺ u = −w,

so −w, and therefore w, is in U, and likewise u is in W. By directness
(1.46, U ∩ W = {0}), u = w = 0.

Now let

    v = u + w = a₁u₁ + ⋯ + a_m u_m + b₁w₁ + ⋯ + bₙwₙ = 0.

By the above u = a₁u₁ + ⋯ + a_m u_m = 0 and w = b₁w₁ + ⋯ + bₙwₙ = 0, so by
linear independence of u₁, …, u_m and of w₁, …, wₙ,

    a₁ = ⋯ = a_m = b₁ = ⋯ = bₙ = 0.

<!-- correct -->

11. Suppose V is a real vector space. Show that if v₁, …, vₙ is a basis of V
    (as a real vector space), then v₁, …, vₙ is also a basis of the
    complexification V_𝐂 (as a complex vector space).

    > See Exercise 8 in Section 1B for the definition of the complexification
    > V_𝐂.

Assume v₁, …, vₙ is a basis for V. Goal: v₁ + i0, …, vₙ + i0 is a basis for V_𝐂.

Linearly independent:

    (a₁ + ib₁)(v₁ + i0) + ⋯ + (aₙ + ibₙ)(vₙ + i0)
      = a₁v₁ + ⋯ + aₙvₙ + i(b₁v₁ + ⋯ + bₙvₙ) = 0.

Complex equality requires componentwise equality, so

    a₁v₁ + ⋯ + aₙvₙ = 0
    b₁v₁ + ⋯ + bₙvₙ = 0,

and by linear independence of v₁, …, vₙ: a₁ = ⋯ = aₙ = b₁ = ⋯ = bₙ = 0.

span ⊆ V_𝐂: let v ∈ span(v₁ + i0, …, vₙ + i0), so

    v = (a₁ + ib₁)(v₁ + i0) + ⋯ + (aₙ + ibₙ)(vₙ + i0)
      = a₁v₁ + ⋯ + aₙvₙ + i(b₁v₁ + ⋯ + bₙvₙ)
      = v_r + iv_c.

v_r and v_c are in V, so by the definition of the complexification,
v_r + iv_c ∈ V_𝐂.

V_𝐂 ⊆ span: let v_r + iv_c ∈ V_𝐂. By definition v_r and v_c are in
V = span(v₁, …, vₙ), so

    v_r + iv_c = a₁v₁ + ⋯ + aₙvₙ + i(b₁v₁ + ⋯ + bₙvₙ)
               = (a₁ + ib₁)(v₁ + i0) + ⋯ + (aₙ + ibₙ)(vₙ + i0)
               ∈ span(v₁ + i0, …, vₙ + i0).

<!-- correct -->

# Exercises 2C, page 48

1. Show that the subspaces of 𝐑² are precisely {0}, all lines in 𝐑² containing
   the origin, and 𝐑².

<!-- pending -->

2. Show that the subspaces of 𝐑³ are precisely {0}, all lines in 𝐑³ containing
   the origin, all planes in 𝐑³ containing the origin, and 𝐑³.

<!-- pending -->

3. (a) Let U = {p ∈ 𝒫₄(𝐅) : p(6) = 0}. Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝒫₄(𝐅).

   (c) Find a subspace W of 𝒫₄(𝐅) such that 𝒫₄(𝐅) = U ⊕ W.

<!-- pending -->

4. (a) Let U = {p ∈ 𝒫₄(𝐑) : p″(6) = 0}. Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝒫₄(𝐑).

   (c) Find a subspace W of 𝒫₄(𝐑) such that 𝒫₄(𝐑) = U ⊕ W.

<!-- pending -->

5. (a) Let U = {p ∈ 𝒫₄(𝐅) : p(2) = p(5)}. Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝒫₄(𝐅).

   (c) Find a subspace W of 𝒫₄(𝐅) such that 𝒫₄(𝐅) = U ⊕ W.

<!-- pending -->

6. (a) Let U = {p ∈ 𝒫₄(𝐅) : p(2) = p(5) = p(6)}. Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝒫₄(𝐅).

   (c) Find a subspace W of 𝒫₄(𝐅) such that 𝒫₄(𝐅) = U ⊕ W.

<!-- pending -->

7. (a) Let U = {p ∈ 𝒫₄(𝐑) : ∫₋₁¹ p = 0}. Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝒫₄(𝐑).

   (c) Find a subspace W of 𝒫₄(𝐑) such that 𝒫₄(𝐑) = U ⊕ W.

<!-- pending -->

8. Suppose v₁, …, v_m is linearly independent in V and w ∈ V. Prove that

       dim span(v₁ + w, …, v_m + w) ≥ m − 1.

<!-- pending -->

9. Suppose m is a positive integer and p₀, p₁, …, p_m ∈ 𝒫(𝐅) are such that each
   p_k has degree k. Prove that p₀, p₁, …, p_m is a basis of 𝒫_m(𝐅).

<!-- pending -->

10. Suppose m is a positive integer. For 0 ≤ k ≤ m, let

        p_k(x) = xᵏ(1 − x)^{m−k}.

    Show that p₀, …, p_m is a basis of 𝒫_m(𝐅).

    > The basis in this exercise leads to what are called Bernstein
    > polynomials. You can do a web search to learn how Bernstein polynomials
    > are used to approximate continuous functions on [0, 1].

<!-- pending -->

11. Suppose U and W are both four-dimensional subspaces of 𝐂⁶. Prove that there
    exist two vectors in U ∩ W such that neither of these vectors is a scalar
    multiple of the other.

<!-- pending -->

12. Suppose that U and W are subspaces of 𝐑⁸ such that dim U = 3, dim W = 5,
    and U + W = 𝐑⁸. Prove that 𝐑⁸ = U ⊕ W.

<!-- pending -->

13. Suppose U and W are both five-dimensional subspaces of 𝐑⁹. Prove that
    U ∩ W ≠ {0}.

<!-- pending -->

14. Suppose V is a ten-dimensional vector space and V₁, V₂, V₃ are subspaces of
    V with dim V₁ = dim V₂ = dim V₃ = 7. Prove that V₁ ∩ V₂ ∩ V₃ ≠ {0}.

<!-- pending -->

15. Suppose V is finite-dimensional and V₁, V₂, V₃ are subspaces of V with
    dim V₁ + dim V₂ + dim V₃ > 2 dim V. Prove that V₁ ∩ V₂ ∩ V₃ ≠ {0}.

<!-- pending -->

16. Suppose V is finite-dimensional and U is a subspace of V with U ≠ V. Let
    n = dim V and m = dim U. Prove that there exist n − m subspaces of V, each
    of dimension n − 1, whose intersection equals U.

<!-- pending -->

17. Suppose that V₁, …, V_m are finite-dimensional subspaces of V. Prove that
    V₁ + ⋯ + V_m is finite-dimensional and

        dim(V₁ + ⋯ + V_m) ≤ dim V₁ + ⋯ + dim V_m.

    > The inequality above is an equality if and only if V₁ + ⋯ + V_m is a
    > direct sum, as will be shown in 3.94.

<!-- pending -->

18. Suppose V is finite-dimensional, with dim V = n ≥ 1. Prove that there exist
    one-dimensional subspaces V₁, …, Vₙ of V such that

        V = V₁ ⊕ ⋯ ⊕ Vₙ.

<!-- pending -->

19. Explain why you might guess, motivated by analogy with the formula for the
    number of elements in the union of three finite sets, that if V₁, V₂, V₃
    are subspaces of a finite-dimensional vector space, then

        dim(V₁ + V₂ + V₃)
          = dim V₁ + dim V₂ + dim V₃
            − dim(V₁ ∩ V₂) − dim(V₁ ∩ V₃) − dim(V₂ ∩ V₃)
            + dim(V₁ ∩ V₂ ∩ V₃).

    Then either prove the formula above or give a counterexample.

<!-- pending -->

20. Prove that if V₁, V₂, and V₃ are subspaces of a finite-dimensional vector
    space, then

        dim(V₁ + V₂ + V₃)
          = dim V₁ + dim V₂ + dim V₃

              dim(V₁ ∩ V₂) + dim(V₁ ∩ V₃) + dim(V₂ ∩ V₃)
            − ──────────────────────────────────────────
                                  3

              dim((V₁ + V₂) ∩ V₃) + dim((V₁ + V₃) ∩ V₂) + dim((V₂ + V₃) ∩ V₁)
            − ──────────────────────────────────────────────────────────────
                                          3

    > The formula above may seem strange because the right side does not look
    > like an integer.

<!-- pending -->
