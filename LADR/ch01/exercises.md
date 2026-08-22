# Exercises 1A, page 10

1. Show that α + β = β + α for all α, β ∈ 𝐂.

<!-- pending -->

2. Show that (α + β) + λ = α + (β + λ) for all α, β, λ ∈ 𝐂.

<!-- pending -->

3. Show that (αβ)λ = α(βλ) for all α, β, λ ∈ 𝐂.

<!-- pending -->

4. Show that λ(α + β) = λα + λβ for all λ, α, β ∈ 𝐂.

<!-- pending -->

5. Show that for every α ∈ 𝐂, there exists a unique β ∈ 𝐂 such that α + β = 0.

<!-- pending -->

6. Show that for every α ∈ 𝐂 with α ≠ 0, there exists a unique β ∈ 𝐂 such
   that αβ = 1.

<!-- pending -->

7. Show that

       (−1 + √3 i) / 2

   is a cube root of 1 (meaning that its cube equals 1).

<!-- pending -->

8. Find two distinct square roots of i.

<!-- pending -->

9. Find x ∈ 𝐑⁴ such that

       (4, −3, 1, 7) + 2x = (5, 9, −6, 8).

<!-- pending -->

10. Explain why there does not exist λ ∈ 𝐂 such that

        λ(2 − 3i, 5 + 4i, −6 + 7i) = (12 − 5i, 7 + 22i, −32 − 9i).

<!-- pending -->

11. Show that (x + y) + z = x + (y + z) for all x, y, z ∈ 𝐅ⁿ.

<!-- pending -->

12. Show that (ab)x = a(bx) for all x ∈ 𝐅ⁿ and all a, b ∈ 𝐅.

<!-- pending -->

13. Show that 1x = x for all x ∈ 𝐅ⁿ.

<!-- pending -->

14. Show that λ(x + y) = λx + λy for all λ ∈ 𝐅 and all x, y ∈ 𝐅ⁿ.

<!-- pending -->

15. Show that (a + b)x = ax + bx for all a, b ∈ 𝐅 and all x ∈ 𝐅ⁿ.

<!-- pending -->

# Exercises 1B, page 16

1. Prove that −(−v) = v for every v ∈ V.

<!-- pending -->

2. Suppose a ∈ 𝐅, v ∈ V, and av = 0. Prove that a = 0 or v = 0.

<!-- pending -->

3. Suppose v, w ∈ V. Explain why there exists a unique x ∈ V such that
   v + 3x = w.

<!-- pending -->

4. The empty set is not a vector space. The empty set fails to satisfy only
   one of the requirements listed in the definition of a vector space (1.20).
   Which one?

<!-- pending -->

5. Show that in the definition of a vector space (1.20), the additive inverse
   condition can be replaced with the condition that

       0v = 0 for all v ∈ V.

   Here the 0 on the left side is the number 0, and the 0 on the right side is
   the additive identity of V.

   > The phrase a "condition can be replaced" in a definition means that the
   > collection of objects satisfying the definition is unchanged if the
   > original condition is replaced with the new condition.

<!-- pending -->

6. Let ∞ and −∞ denote two distinct objects, neither of which is in 𝐑. Define
   an addition and scalar multiplication on 𝐑 ∪ {∞, −∞} as you could guess
   from the notation. Specifically, the sum and product of two real numbers is
   as usual, and for t ∈ 𝐑 define

               ⎧ −∞  if t < 0,               ⎧ ∞   if t < 0,
       t∞  =   ⎨  0  if t = 0,     t(−∞)  =  ⎨ 0   if t = 0,
               ⎩  ∞  if t > 0,               ⎩ −∞  if t > 0,

   and

       t + ∞ = ∞ + t = ∞ + ∞ = ∞,
       t + (−∞) = (−∞) + t = (−∞) + (−∞) = −∞,
       ∞ + (−∞) = (−∞) + ∞ = 0.

   With these operations of addition and scalar multiplication, is
   𝐑 ∪ {∞, −∞} a vector space over 𝐑? Explain.

<!-- pending -->

7. Suppose S is a nonempty set. Let V^S denote the set of functions from S to
   V. Define a natural addition and scalar multiplication on V^S, and show
   that V^S is a vector space with these definitions.

<!-- pending -->

8. Suppose V is a real vector space.

   - The _complexification_ of V, denoted by V_𝐂, equals V × V. An element of
     V_𝐂 is an ordered pair (u, v), where u, v ∈ V, but we write this as
     u + iv.
   - Addition on V_𝐂 is defined by

         (u₁ + iv₁) + (u₂ + iv₂) = (u₁ + u₂) + i(v₁ + v₂)

     for all u₁, v₁, u₂, v₂ ∈ V.
   - Complex scalar multiplication on V_𝐂 is defined by

         (a + bi)(u + iv) = (au − bv) + i(av + bu)

     for all a, b ∈ 𝐑 and all u, v ∈ V.

   Prove that with the definitions of addition and scalar multiplication as
   above, V_𝐂 is a complex vector space.

   > Think of V as a subset of V_𝐂 by identifying u ∈ V with u + i0. The
   > construction of V_𝐂 from V can be thought of as generalizing the
   > construction of 𝐂ⁿ from 𝐑ⁿ.

<!-- pending -->

# Exercises 1C, page 24

1. For each of the following subsets of 𝐅³, determine whether it is a subspace
   of 𝐅³.

   (a) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ + 2x₂ + 3x₃ = 0}
   (b) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ + 2x₂ + 3x₃ = 4}
   (c) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁x₂x₃ = 0}
   (d) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ = 5x₃}

<!-- pending -->

2. Verify all assertions about subspaces in Example 1.35.

<!-- pending -->

3. Show that the set of differentiable real-valued functions f on the interval
   (−4, 4) such that f′(−1) = 3f(2) is a subspace of 𝐑^(−4,4).

<!-- pending -->

4. Suppose b ∈ 𝐑. Show that the set of continuous real-valued functions f on
   the interval [0, 1] such that ∫₀¹ f = b is a subspace of 𝐑^[0,1] if and
   only if b = 0.

<!-- pending -->

5. Is 𝐑² a subspace of the complex vector space 𝐂²?

<!-- pending -->

6. (a) Is {(a, b, c) ∈ 𝐑³ : a³ = b³} a subspace of 𝐑³?
   (b) Is {(a, b, c) ∈ 𝐂³ : a³ = b³} a subspace of 𝐂³?

<!-- pending -->

7. Prove or give a counterexample: If U is a nonempty subset of 𝐑² such that U
   is closed under addition and under taking additive inverses (meaning
   −u ∈ U whenever u ∈ U), then U is a subspace of 𝐑².

<!-- pending -->

8. Give an example of a nonempty subset U of 𝐑² such that U is closed under
   scalar multiplication, but U is not a subspace of 𝐑².

<!-- pending -->

9. A function f : 𝐑 → 𝐑 is called _periodic_ if there exists a positive number
   p such that f(x) = f(x + p) for all x ∈ 𝐑. Is the set of periodic functions
   from 𝐑 to 𝐑 a subspace of 𝐑^𝐑? Explain.

<!-- pending -->

10. Suppose V₁ and V₂ are subspaces of V. Prove that the intersection V₁ ∩ V₂
    is a subspace of V.

<!-- pending -->

11. Prove that the intersection of every collection of subspaces of V is a
    subspace of V.

<!-- pending -->

12. Prove that the union of two subspaces of V is a subspace of V if and only
    if one of the subspaces is contained in the other.

<!-- pending -->

13. Prove that the union of three subspaces of V is a subspace of V if and
    only if one of the subspaces contains the other two.

    > This exercise is surprisingly harder than Exercise 12, possibly because
    > this exercise is not true if we replace 𝐅 with a field containing only
    > two elements.

<!-- pending -->

14. Suppose

        U = {(x, −x, 2x) ∈ 𝐅³ : x ∈ 𝐅}  and  W = {(x, x, 2x) ∈ 𝐅³ : x ∈ 𝐅}.

    Describe U + W using symbols, and also give a description of U + W that
    uses no symbols.

<!-- pending -->

15. Suppose U is a subspace of V. What is U + U?

<!-- pending -->

16. Is the operation of addition on the subspaces of V commutative? In other
    words, if U and W are subspaces of V, is U + W = W + U?

<!-- pending -->

17. Is the operation of addition on the subspaces of V associative? In other
    words, if V₁, V₂, V₃ are subspaces of V, is

        (V₁ + V₂) + V₃ = V₁ + (V₂ + V₃)?

<!-- pending -->

18. Does the operation of addition on the subspaces of V have an additive
    identity? Which subspaces have additive inverses?

<!-- pending -->

19. Prove or give a counterexample: If V₁, V₂, U are subspaces of V such that

        V₁ + U = V₂ + U,

    then V₁ = V₂.

<!-- pending -->

20. Suppose

        U = {(x, x, y, y) ∈ 𝐅⁴ : x, y ∈ 𝐅}.

    Find a subspace W of 𝐅⁴ such that 𝐅⁴ = U ⊕ W.

<!-- pending -->

21. Suppose

        U = {(x, y, x + y, x − y, 2x) ∈ 𝐅⁵ : x, y ∈ 𝐅}.

    Find a subspace W of 𝐅⁵ such that 𝐅⁵ = U ⊕ W.

<!-- pending -->

22. Suppose

        U = {(x, y, x + y, x − y, 2x) ∈ 𝐅⁵ : x, y ∈ 𝐅}.

    Find three subspaces W₁, W₂, W₃ of 𝐅⁵, none of which equals {0}, such that
    𝐅⁵ = U ⊕ W₁ ⊕ W₂ ⊕ W₃.

<!-- pending -->

23. Prove or give a counterexample: If V₁, V₂, U are subspaces of V such that

        V = V₁ ⊕ U  and  V = V₂ ⊕ U,

    then V₁ = V₂.

    > Hint: When trying to discover whether a conjecture in linear algebra is
    > true or false, it is often useful to start by experimenting in 𝐅².

<!-- pending -->

24. A function f : 𝐑 → 𝐑 is called _even_ if

        f(−x) = f(x)

    for all x ∈ 𝐑. A function f : 𝐑 → 𝐑 is called _odd_ if

        f(−x) = −f(x)

    for all x ∈ 𝐑. Let V_e denote the set of real-valued even functions on 𝐑
    and let V_o denote the set of real-valued odd functions on 𝐑. Show that
    𝐑^𝐑 = V_e ⊕ V_o.

<!-- pending -->
