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

True.

span(v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄) ⊆ V is automatic. For the other
inclusion, let v ∈ V. Since v₁, v₂, v₃, v₄ spans V, there exist
c₁, c₂, c₃, c₄ ∈ 𝐅 with

    v = c₁v₁ + c₂v₂ + c₃v₃ + c₄v₄.

A linear combination of the second list, distributed and grouped:

    a₁(v₁ − v₂) + a₂(v₂ − v₃) + a₃(v₃ − v₄) + a₄v₄
      = a₁v₁ − a₁v₂ + a₂v₂ − a₂v₃ + a₃v₃ − a₃v₄ + a₄v₄
      = a₁v₁ + (a₂ − a₁)v₂ + (a₃ − a₂)v₃ + (a₄ − a₃)v₄.

Equating with the expression for v, it suffices to solve

    a₁ = c₁
    a₂ − a₁ = c₂  ⟹  a₂ − c₁ = c₂  ⟹  a₂ = c₁ + c₂
    a₃ − a₂ = c₃  ⟹  a₃ − (c₁ + c₂) = c₃  ⟹  a₃ = c₁ + c₂ + c₃
    a₄ − a₃ = c₄  ⟹  a₄ − (c₁ + c₂ + c₃) = c₄  ⟹  a₄ = c₁ + c₂ + c₃ + c₄

These a₁, a₂, a₃, a₄ exist for every v ∈ V, so
v ∈ span(v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄).

<!-- correct -->

3. Suppose v₁, …, v_m is a list of vectors in V. For k ∈ {1, …, m}, let

       w_k = v₁ + ⋯ + v_k.

   Show that span(v₁, …, v_m) = span(w₁, …, w_m).

<!-- pending -->

4. (a) Show that a list of length one in a vector space is linearly
       independent if and only if the vector in the list is not 0.

   (b) Show that a list of length two in a vector space is linearly
       independent if and only if neither of the two vectors in the list is a
       scalar multiple of the other.

<!-- pending -->

5. Find a number t such that

       (3, 1, 4), (2, −3, 5), (5, 9, t)

   is not linearly independent in 𝐑³.

<!-- pending -->

6. Show that the list (2, 3, 1), (1, −1, 2), (7, 3, c) is linearly dependent in
   𝐅³ if and only if c = 8.

<!-- pending -->

7. (a) Show that if we think of 𝐂 as a vector space over 𝐑, then the list
       1 + i, 1 − i is linearly independent.

   (b) Show that if we think of 𝐂 as a vector space over 𝐂, then the list
       1 + i, 1 − i is linearly dependent.

<!-- pending -->

8. Suppose v₁, v₂, v₃, v₄ is linearly independent in V. Prove that the list

       v₁ − v₂, v₂ − v₃, v₃ − v₄, v₄

   is also linearly independent.

<!-- pending -->

9. Prove or give a counterexample: If v₁, v₂, …, v_m is a linearly independent
   list of vectors in V, then

       5v₁ − 4v₂, v₂, v₃, …, v_m

   is linearly independent.

<!-- pending -->

10. Prove or give a counterexample: If v₁, v₂, …, v_m is a linearly independent
    list of vectors in V and λ ∈ 𝐅 with λ ≠ 0, then λv₁, λv₂, …, λv_m is
    linearly independent.

<!-- pending -->

11. Prove or give a counterexample: If v₁, …, v_m and w₁, …, w_m are linearly
    independent lists of vectors in V, then the list v₁ + w₁, …, v_m + w_m is
    linearly independent.

<!-- pending -->

12. Suppose v₁, …, v_m is linearly independent in V and w ∈ V. Prove that if
    v₁ + w, …, v_m + w is linearly dependent, then w ∈ span(v₁, …, v_m).

<!-- pending -->

13. Suppose v₁, …, v_m is linearly independent in V and w ∈ V. Show that

        v₁, …, v_m, w is linearly independent ⟺ w ∉ span(v₁, …, v_m).

<!-- pending -->

14. Suppose v₁, …, v_m is a list of vectors in V. For k ∈ {1, …, m}, let

        w_k = v₁ + ⋯ + v_k.

    Show that the list v₁, …, v_m is linearly independent if and only if the
    list w₁, …, w_m is linearly independent.

<!-- pending -->

15. Explain why there does not exist a list of six polynomials that is linearly
    independent in 𝒫₄(𝐅).

<!-- pending -->

16. Explain why no list of four polynomials spans 𝒫₄(𝐅).

<!-- pending -->

17. Prove that V is infinite-dimensional if and only if there is a sequence
    v₁, v₂, … of vectors in V such that v₁, …, v_m is linearly independent for
    every positive integer m.

<!-- pending -->

18. Prove that 𝐅^∞ is infinite-dimensional.

<!-- pending -->

19. Prove that the real vector space of all continuous real-valued functions on
    the interval [0, 1] is infinite-dimensional.

<!-- pending -->

20. Suppose p₀, p₁, …, p_m are polynomials in 𝒫_m(𝐅) such that p_k(2) = 0 for
    each k ∈ {0, …, m}. Prove that p₀, p₁, …, p_m is not linearly independent
    in 𝒫_m(𝐅).

<!-- pending -->

# Exercises 2B, page 42

1. Find all vector spaces that have exactly one basis.

<!-- pending -->

2. Verify all assertions in Example 2.27.

<!-- pending -->

3. (a) Let U be the subspace of 𝐑⁵ defined by

           U = {(x₁, x₂, x₃, x₄, x₅) ∈ 𝐑⁵ : x₁ = 3x₂ and x₃ = 7x₄}.

       Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝐑⁵.

   (c) Find a subspace W of 𝐑⁵ such that 𝐑⁵ = U ⊕ W.

<!-- pending -->

4. (a) Let U be the subspace of 𝐂⁵ defined by

           U = {(z₁, z₂, z₃, z₄, z₅) ∈ 𝐂⁵ : 6z₁ = z₂ and z₃ + 2z₄ + 3z₅ = 0}.

       Find a basis of U.

   (b) Extend the basis in (a) to a basis of 𝐂⁵.

   (c) Find a subspace W of 𝐂⁵ such that 𝐂⁵ = U ⊕ W.

<!-- pending -->

5. Suppose V is finite-dimensional and U, W are subspaces of V such that
   V = U + W. Prove that there exists a basis of V consisting of vectors in
   U ∪ W.

<!-- pending -->

6. Prove or give a counterexample: If p₀, p₁, p₂, p₃ is a list in 𝒫₃(𝐅) such
   that none of the polynomials p₀, p₁, p₂, p₃ has degree 2, then
   p₀, p₁, p₂, p₃ is not a basis of 𝒫₃(𝐅).

<!-- pending -->

7. Suppose v₁, v₂, v₃, v₄ is a basis of V. Prove that

       v₁ + v₂, v₂ + v₃, v₃ + v₄, v₄

   is also a basis of V.

<!-- pending -->

8. Prove or give a counterexample: If v₁, v₂, v₃, v₄ is a basis of V and U is a
   subspace of V such that v₁, v₂ ∈ U and v₃ ∉ U and v₄ ∉ U, then v₁, v₂ is a
   basis of U.

<!-- pending -->

9. Suppose v₁, …, v_m is a list of vectors in V. For k ∈ {1, …, m}, let

       w_k = v₁ + ⋯ + v_k.

   Show that v₁, …, v_m is a basis of V if and only if w₁, …, w_m is a basis
   of V.

<!-- pending -->

10. Suppose U and W are subspaces of V such that V = U ⊕ W. Suppose also that
    u₁, …, u_m is a basis of U and w₁, …, wₙ is a basis of W. Prove that

        u₁, …, u_m, w₁, …, wₙ

    is a basis of V.

<!-- pending -->

11. Suppose V is a real vector space. Show that if v₁, …, vₙ is a basis of V
    (as a real vector space), then v₁, …, vₙ is also a basis of the
    complexification V_𝐂 (as a complex vector space).

    > See Exercise 8 in Section 1B for the definition of the complexification
    > V_𝐂.

<!-- pending -->

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
