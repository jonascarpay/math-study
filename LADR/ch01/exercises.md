# Exercises 1A, page 10

1. Show that α + β = β + α for all α, β ∈ 𝐂.

Write α = a + bi and β = c + di with a, b, c, d ∈ 𝐑. Complex numbers are
ordered pairs, so equality is coordinatewise.

    α + β = (a + c) + (b + d)i     (1.1)
          = (c + a) + (d + b)i     (commutativity of addition on 𝐑)
          = β + α                  (1.1)

<!-- correct -->

2. Show that (α + β) + λ = α + (β + λ) for all α, β, λ ∈ 𝐂.

Write α = a + bi, β = c + di, λ = e + fi with a, …, f ∈ 𝐑.

    (α + β) + λ = ((a + c) + e) + ((b + d) + f)i   (1.1, twice)
                = (a + (c + e)) + (b + (d + f))i   (associativity of addition
                                                    on 𝐑)
                = α + (β + λ)                      (1.1, twice)

<!-- correct -->

3. Show that (αβ)λ = α(βλ) for all α, β, λ ∈ 𝐂.

Write α = a + bi, β = c + di, λ = e + fi with a, …, f ∈ 𝐑.

    αβ    = (ac − bd) + (ad + bc)i                              (1.1)
    (αβ)λ = [(ac − bd)e − (ad + bc)f]
              + [(ac − bd)f + (ad + bc)e]i                      (1.1)
          = (ace − bde − adf − bcf) + (acf − bdf + ade + bce)i;

    βλ    = (ce − df) + (cf + de)i                              (1.1)
    α(βλ) = [a(ce − df) − b(cf + de)]
              + [a(cf + de) + b(ce − df)]i                      (1.1)
          = (ace − adf − bcf − bde) + (acf + ade + bce − bdf)i.

By associativity and commutativity of multiplication on 𝐑, both real parts
consist of the same four terms ace, −bde, −adf, −bcf, and both imaginary
parts of the same four terms acf, −bdf, ade, bce. Equality in 𝐂 is
coordinatewise, so

    (αβ)λ = α(βλ).

<!-- correct -->

4. Show that λ(α + β) = λα + λβ for all λ, α, β ∈ 𝐂.

Write λ = λ_r + λ_i i, α = α_r + α_i i, β = β_r + β_i i with all six
components in 𝐑. Equality in 𝐂 is coordinatewise.

LHS: α + β = (α_r + β_r) + (α_i + β_i)i (1.1), so

    λ(α + β) = (λ_r(α_r + β_r) − λ_i(α_i + β_i))
                 + (λ_r(α_i + β_i) + λ_i(α_r + β_r))i     (1.1)

RHS:

    λα = (λ_r α_r − λ_i α_i) + (λ_r α_i + λ_i α_r)i        (1.1)
    λβ = (λ_r β_r − λ_i β_i) + (λ_r β_i + λ_i β_r)i        (1.1)
    λα + λβ = (λ_r α_r − λ_i α_i + λ_r β_r − λ_i β_i)
                + (λ_r α_i + λ_i α_r + λ_r β_i + λ_i β_r)i  (1.1)

Distributing over 𝐑 in the LHS real and imaginary parts:

    λ_r(α_r + β_r) − λ_i(α_i + β_i)
        = λ_r α_r + λ_r β_r − λ_i α_i − λ_i β_i,
    λ_r(α_i + β_i) + λ_i(α_r + β_r)
        = λ_r α_i + λ_r β_i + λ_i α_r + λ_i β_r,

which agree with the corresponding parts of the RHS up to commutativity of
addition in 𝐑. Hence λ(α + β) = λα + λβ.

<!-- correct -->

5. Show that for every α ∈ 𝐂, there exists a unique β ∈ 𝐂 such that α + β = 0.

Let α = a₁ + a₂i and β = b₁ + b₂i with a₁, a₂, b₁, b₂ ∈ 𝐑, and 0 = 0 + 0i.
Complex numbers are ordered pairs, so equality is coordinatewise.

    α + β = (a₁ + b₁) + (a₂ + b₂)i                      (1.1)
    α + β = 0  ⟺  a₁ + b₁ = 0 and a₂ + b₂ = 0

So the condition on β is exactly that b₁, b₂ are additive inverses of a₁, a₂
in 𝐑.

Existence:

    b₁ = −a₁, b₂ = −a₂                                  (exist in 𝐑)

Uniqueness: suppose γ = c₁ + c₂i also satisfies α + γ = 0.

    a₁ + b₁ = 0 = a₁ + c₁  ⇒  b₁ = c₁                   (uniqueness of
    a₂ + b₂ = 0 = a₂ + c₂  ⇒  b₂ = c₂                    additive inverses
                                                         in 𝐑)
    ⇒ β = γ

<!-- correct -->

6. Show that for every α ∈ 𝐂 with α ≠ 0, there exists a unique β ∈ 𝐂 such
   that αβ = 1.

Let α = a₁ + a₂i with a₁, a₂ ∈ 𝐑, and write s = a₁² + a₂².

Existence: since α ≠ 0, a₁ and a₂ are not both 0; squares in 𝐑 are ≥ 0, so
s > 0 and 1/s ∈ 𝐑. Take β to be the conjugate of α scaled by 1/s.

    β  = (a₁/s) + (−a₂/s)i
    αβ = (a₁·(a₁/s) − a₂·(−a₂/s))
           + (a₁·(−a₂/s) + a₂·(a₁/s))i          (1.1)
       = ((a₁² + a₂²)/s) + 0i
       = 1 + 0i
       = 1

Uniqueness: suppose αβ = αγ = 1.

    γ = γ(αβ)
      = (γα)β                                   (associativity, exercise 3)
      = (αγ)β                                   (commutativity, 1.3)
      = 1β
      = β                                       (λ1 = λ)

<!-- correct -->

7. Show that

       (−1 + √3 i) / 2

   is a cube root of 1 (meaning that its cube equals 1).

Let ω = (−1 + √3 i)/2. Direct expansion via 1.1:

    ω²  = (1 − 2√3 i + 3i²)/4
        = (1 − 3 − 2√3 i)/4
        = (−2 − 2√3 i)/4
        = (−1 − √3 i)/2
    ω³  = ω²·ω
        = ((−1 − √3 i)/2)·((−1 + √3 i)/2)
        = (1 − 3i²)/4
        = (1 + 3)/4
        = 1

<!-- correct -->

8. Find two distinct square roots of i.

    ±(1/√2 + (1/√2)i)

Check:

    (1/√2 + (1/√2)i)²    = (1/2 − 1/2) + (1/2 + 1/2)i     (1.1)
                         = i
    (−(1/√2 + (1/√2)i))² = (1/√2 + (1/√2)i)²
                         = i

<!-- correct -->

9. Find x ∈ 𝐑⁴ such that

       (4, −3, 1, 7) + 2x = (5, 9, −6, 8).

Addition and scalar multiplication in 𝐑⁴ are coordinatewise, so 2xₖ is the
difference of the corresponding coordinates:

    2x = (5 − 4, 9 − (−3), −6 − 1, 8 − 7)
       = (1, 12, −7, 1)
    x  = (1/2, 6, −7/2, 1/2)

<!-- correct -->

10. Explain why there does not exist λ ∈ 𝐂 such that

        λ(2 − 3i, 5 + 4i, −6 + 7i) = (12 − 5i, 7 + 22i, −32 − 9i).

<!-- skipped -->

11. Show that (x + y) + z = x + (y + z) for all x, y, z ∈ 𝐅ⁿ.

Write x = (x₁, …, xₙ), y = (y₁, …, yₙ), z = (z₁, …, zₙ) with all coordinates
in 𝐅. Addition in 𝐅ⁿ is coordinatewise (1.12), so for each k ∈ {1, …, n}:

    ((x + y) + z)ₖ = (xₖ + yₖ) + zₖ
                   = xₖ + (yₖ + zₖ)    (associativity of addition in 𝐅:
                                        𝐑 by assumption, 𝐂 by exercise 2)
                   = (x + (y + z))ₖ

Lists are equal iff their coordinates agree, hence

    (x + y) + z = x + (y + z).

<!-- correct -->

12. Show that (ab)x = a(bx) for all x ∈ 𝐅ⁿ and all a, b ∈ 𝐅.

Write x = (x₁, …, xₙ). Scalar multiplication in 𝐅ⁿ is coordinatewise (1.13),
so for each k ∈ {1, …, n}:

    ((ab)x)ₖ = (ab)xₖ
             = a(bxₖ)      (associativity of multiplication in 𝐅:
                            𝐑 by assumption, 𝐂 by exercise 3)
             = (a(bx))ₖ

These agree for every k, hence

    (ab)x = a(bx).

<!-- correct -->

13. Show that 1x = x for all x ∈ 𝐅ⁿ.

Write x = (x₁, …, xₙ).

    1x = (1x₁, …, 1xₙ)     (1.13)
       = (x₁, …, xₙ)       (1 is the multiplicative identity of 𝐅)
       = x

<!-- correct -->

14. Show that λ(x + y) = λx + λy for all λ ∈ 𝐅 and all x, y ∈ 𝐅ⁿ.

Write x = (x₁, …, xₙ) and y = (y₁, …, yₙ). Addition and scalar multiplication
in 𝐅ⁿ are coordinatewise (1.12, 1.13), so for each k ∈ {1, …, n}:

    (λ(x + y))ₖ = λ(xₖ + yₖ)
                = λxₖ + λyₖ      (distributivity in 𝐅, 1.3)
                = (λx + λy)ₖ

Hence

    λ(x + y) = λx + λy.

<!-- correct -->

15. Show that (a + b)x = ax + bx for all a, b ∈ 𝐅 and all x ∈ 𝐅ⁿ.

<!-- skipped -->

# Exercises 1B, page 16

1. Prove that −(−v) = v for every v ∈ V.

Consider the sum v + (−v) + (−(−v)), and associate it in the two possible
ways:

    (v + (−v)) + (−(−v)) = 0 + (−(−v)) = −(−v),
    v + ((−v) + (−(−v))) = v + 0 = v.

Both use the defining property of the additive inverse (1.28), the additive
identity, and commutativity. Hence −(−v) = v.

<!-- correct -->

2. Suppose a ∈ 𝐅, v ∈ V, and av = 0. Prove that a = 0 or v = 0.

If a = 0, the conclusion holds. So suppose a ≠ 0; then 1/a ∈ 𝐅 exists
(multiplicative inverse, 1.3).

    v = 1v
      = ((1/a)a)v
      = (1/a)(av)      (associativity, 1.20)
      = (1/a)0
      = 0              (1.31)

<!-- correct -->

3. Suppose v, w ∈ V. Explain why there exists a unique x ∈ V such that
   v + 3x = w.

<!-- skipped -->

4. The empty set is not a vector space. The empty set fails to satisfy only
   one of the requirements listed in the definition of a vector space (1.20).
   Which one?

<!-- skipped -->

5. Show that in the definition of a vector space (1.20), the additive inverse
   condition can be replaced with the condition that

       0v = 0 for all v ∈ V.

   Here the 0 on the left side is the number 0, and the 0 on the right side is
   the additive identity of V.

   > The phrase a "condition can be replaced" in a definition means that the
   > collection of objects satisfying the definition is unchanged if the
   > original condition is replaced with the new condition.

<!-- skipped -->

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

No: associativity of addition is violated.

    ∞ + (∞ + (−∞)) = ∞ + 0 = ∞
    (∞ + ∞) + (−∞) = ∞ + (−∞) = 0

<!-- correct -->

7. Suppose S is a nonempty set. Let V^S denote the set of functions from S to
   V. Define a natural addition and scalar multiplication on V^S, and show
   that V^S is a vector space with these definitions.

Define, for f, g ∈ V^S, λ ∈ 𝐅, and all x ∈ S:

    (f + g)(x) = f(x) + g(x)
    (λf)(x)    = λ(f(x))

where the operations on the right are those of V. Two elements of V^S are
equal iff they agree at every x ∈ S, so each property of 1.20 is checked
pointwise.

commutativity:

    (f + g)(x) = f(x) + g(x)
               = g(x) + f(x)
               = (g + f)(x)

associativity:

    ((f + g) + h)(x) = (f(x) + g(x)) + h(x)
                     = f(x) + (g(x) + h(x))
                     = f(x) + (g + h)(x)
                     = (f + (g + h))(x)

    ((ab)f)(x) = (ab)(f(x))
               = a(b(f(x)))
               = a((bf)(x))
               = (a(bf))(x)

additive identity: the function 0 ∈ V^S given by 0(x) = 0.

    (f + 0)(x) = f(x) + 0(x)
               = f(x)

additive inverse: given f ∈ V^S, take w ∈ V^S with w(x) = (−1)(f(x)).

    (f + w)(x) = f(x) + w(x)
               = f(x) + (−1)(f(x))
               = 0(f(x))
               = 0

multiplicative identity:

    (1f)(x) = 1(f(x))
            = f(x)

distributive properties:

    (a(f + g))(x) = a((f + g)(x))
                  = a(f(x) + g(x))
                  = a(f(x)) + a(g(x))
                  = (af)(x) + (ag)(x)
                  = (af + ag)(x)

    ((a + b)f)(x) = (a + b)(f(x))
                  = a(f(x)) + b(f(x))
                  = (af + bf)(x)

<!-- correct -->

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

Elements of V_𝐂 are ordered pairs, so equality is componentwise: two elements
agree iff their "real" and "imaginary" components agree in V. All right-hand
sides below use only the operations of the real vector space V. Verify each
property of 1.20 (scalars now in 𝐂).

Write z_k = u_k + iv_k throughout the additive properties.

commutativity:

    (u₁ + iv₁) + (u₂ + iv₂) = (u₁ + u₂) + i(v₁ + v₂)
    (u₂ + iv₂) + (u₁ + iv₁) = (u₂ + u₁) + i(v₂ + v₁)

and u₁ + u₂ = u₂ + u₁, v₁ + v₂ = v₂ + v₁ by commutativity in V.

associativity of addition:

    ((z₁ + z₂) + z₃) has components ((u₁ + u₂) + u₃, (v₁ + v₂) + v₃)
    (z₁ + (z₂ + z₃)) has components (u₁ + (u₂ + u₃), v₁ + (v₂ + v₃))

equal by associativity of addition in V.

additive identity: 0 + i0, with 0 the additive identity of V.

    (u + iv) + (0 + i0) = (u + 0) + i(v + 0) = u + iv

additive inverse: for u + iv, take (−u) + i(−v), with −u, −v the inverses
in V.

    (u + iv) + ((−u) + i(−v)) = (u + (−u)) + i(v + (−v)) = 0 + i0

associativity of scalar multiplication: λ = a + bi, μ = c + di, z = u + iv,
with a, b, c, d ∈ 𝐑.

    ((a + bi)(c + di))(u + iv)
      = ((ac − bd) + (ad + bc)i)(u + iv)
      = ((ac − bd)u − (ad + bc)v) + i((ac − bd)v + (ad + bc)u)

    (a + bi)((c + di)(u + iv))
      = (a + bi)((cu − dv) + i(du + cv))
      = (a(cu − dv) − b(du + cv)) + i(b(cu − dv) + a(du + cv))
      = (acu − adv − bdu − bcv) + i(bcu − bdv + adu + acv)
      = ((ac − bd)u − (ad + bc)v) + i((ac − bd)v + (ad + bc)u)

multiplicative identity: 1 = 1 + 0i.

    1(u + iv) = (1 + 0i)(u + iv)
              = (1u − 0v) + i(0u + 1v)
              = u + iv

using 1u = u (multiplicative identity in V) and 0v = 0u = 0 (1.30 in V).

distributive property (a + b)v = av + bv, here (λ + μ)z = λz + μz:
λ = a + bi, μ = c + di, z = u + iv.

    (λ + μ)z
      = ((a + c) + (b + d)i)(u + iv)
      = ((a + c)u − (b + d)v) + i((a + c)v + (b + d)u)
      = (au + cu − bv − dv) + i(av + cv + bu + du)

    λz + μz
      = ((au − bv) + i(av + bu)) + ((cu − dv) + i(du + cv))
      = (au + cu − bv − dv) + i(av + cv + bu + du)

distributive property a(u + v) = au + av, here λ(z₁ + z₂) = λz₁ + λz₂:
λ = a + bi, z₁ = x + iy, z₂ = u + iv.

    λ(z₁ + z₂)
      = (a + bi)((x + u) + i(y + v))
      = (a(x + u) − b(y + v)) + i(b(x + u) + a(y + v))
      = (ax + au − by − bv) + i(bx + bu + ay + av)

    λz₁ + λz₂
      = ((ax − by) + i(bx + ay)) + ((au − bv) + i(bu + av))
      = (ax + au − by − bv) + i(bx + bu + ay + av)

Each real/imaginary component agrees by the distributive and
associativity/commutativity laws in V, so all properties of 1.20 hold and V_𝐂
is a complex vector space.

<!-- correct -->

# Exercises 1C, page 24

1. For each of the following subsets of 𝐅³, determine whether it is a subspace
   of 𝐅³.

   (a) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ + 2x₂ + 3x₃ = 0}
   (b) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ + 2x₂ + 3x₃ = 4}
   (c) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁x₂x₃ = 0}
   (d) {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ = 5x₃}

(a) Subspace. Let U = {(x₁, x₂, x₃) ∈ 𝐅³ : x₁ + 2x₂ + 3x₃ = 0}, let x, y ∈ U,
and let λ ∈ 𝐅.

Additive identity: 0 + 2·0 + 3·0 = 0, so (0, 0, 0) ∈ U.

Closed under addition: x + y = (x₁ + y₁, x₂ + y₂, x₃ + y₃), and

    (x₁ + y₁) + 2(x₂ + y₂) + 3(x₃ + y₃)
      = (x₁ + 2x₂ + 3x₃) + (y₁ + 2y₂ + 3y₃)   (distributivity, commutativity,
                                               associativity)
      = 0 + 0
      = 0.

Closed under scalar multiplication: λx = (λx₁, λx₂, λx₃), and

    λx₁ + 2λx₂ + 3λx₃
      = λ(x₁ + 2x₂ + 3x₃)   (distributivity)
      = λ·0
      = 0.

(b) Not a subspace: 0 + 2·0 + 3·0 = 0 ≠ 4, so 0 is not in the set, and the
additive identity condition of 1.34 fails.

(c) Not a subspace. Closure under addition fails:

    1·1·0 = 0 and 0·0·1 = 0, so (1, 1, 0) and (0, 0, 1) are in the set,
    (1, 1, 0) + (0, 0, 1) = (1, 1, 1),
    1·1·1 = 1 ≠ 0.

(d) Subspace. x₁ = 5x₃ ⟺ x₁ + 0x₂ − 5x₃ = 0, which is the same shape as (a)
with coefficients (1, 0, −5) in place of (1, 2, 3), so the argument of (a)
applies verbatim with those coefficients.

<!-- correct -->

2. Verify all assertions about subspaces in Example 1.35.

(a) If b = 0, the set is {(x₁, x₂, x₃, x₄) ∈ 𝐅⁴ : x₃ − 5x₄ = 0}, the same
shape as exercise 1(a) with coefficients (0, 0, 1, −5), so the argument there
applies verbatim.

If b ≠ 0, then (0, 0, 0, 0) has x₃ = 0 while 5x₄ + b = b ≠ 0, so 0 is not in
the set and the additive identity condition of 1.34 fails.

(b) Let U be the set of continuous real-valued functions on [0, 1].

    The additive identity of 𝐑^[0,1] is the constant function 0(x) = 0 (1.25),
      which is continuous, so 0 ∈ U.
    The sum of two continuous functions is continuous, so f, g ∈ U implies
      f + g ∈ U.
    A constant multiple of a continuous function is continuous, so λ ∈ 𝐑 and
      f ∈ U implies λf ∈ U.

(c) Let U be the set of differentiable real-valued functions on 𝐑. Same
argument as (b), with differentiability in place of continuity:

    the constant function 0 is differentiable with 0′ = 0, so 0 ∈ U;
    (f + g)′ = f′ + g′, so f + g is differentiable;
    (λf)′ = λf′, so λf is differentiable.

(d) Skipped. Partial: (f + g)′(2) = f′(2) + g′(2) forces b = b + b, hence
b = 0, giving the "only if" direction — but without exhibiting an element of
the set to apply closure to, and without the "if" direction.

(e) Let U ⊆ 𝐂^∞ be the set of sequences with limit 0.

    The sequence 0 = (0, 0, …) has limit 0, so 0 ∈ U.
    lim(x + y) = lim x + lim y = 0 + 0 = 0, so x, y ∈ U implies x + y ∈ U.
    lim(λx) = λ lim x = λ·0 = 0, so λ ∈ 𝐂 and x ∈ U implies λx ∈ U.

<!-- skipped -->

3. Show that the set of differentiable real-valued functions f on the interval
   (−4, 4) such that f′(−1) = 3f(2) is a subspace of 𝐑^(−4,4).

Let U = {f ∈ 𝐑^(−4,4) : f differentiable, f′(−1) = 3f(2)}.

Additive identity: the constant function 0 is differentiable, and

    0′(−1) = 0 = 3·0 = 3·0(2),

so 0 ∈ U.

Closed under addition: for f, g ∈ U, f + g is differentiable, and

    (f + g)′(−1)
      = f′(−1) + g′(−1)
      = 3f(2) + 3g(2)
      = 3(f(2) + g(2))
      = 3(f + g)(2),

so f + g ∈ U.

Closed under scalar multiplication: for c ∈ 𝐑 and f ∈ U, cf is
differentiable, and

    (cf)′(−1)
      = c·f′(−1)
      = c·3f(2)
      = 3(cf)(2),

so cf ∈ U.

<!-- correct -->

4. Suppose b ∈ 𝐑. Show that the set of continuous real-valued functions f on
   the interval [0, 1] such that ∫₀¹ f = b is a subspace of 𝐑^[0,1] if and
   only if b = 0.

Let U_b = {f ∈ 𝐑^[0,1] : f continuous, ∫₀¹ f = b}.

(⟹) Suppose U_b is a subspace of 𝐑^[0,1]. By 1.34, 0 ∈ U_b, where 0 is the
constant function 0(x) = 0 (1.25). Hence

    b = ∫₀¹ 0 = 0.

(⟸) Suppose b = 0.

Additive identity: ∫₀¹ 0 = 0 = b, so 0 ∈ U₀.

Closed under addition: let f, g ∈ U₀. Addition preserves continuity, so f + g
is continuous, and integration distributes over addition:

    ∫₀¹ (f + g)
      = ∫₀¹ f + ∫₀¹ g
      = 0 + 0
      = 0,

so f + g ∈ U₀.

Closed under scalar multiplication: let λ ∈ 𝐑 and f ∈ U₀. Scaling preserves
continuity, so λf is continuous, and integration commutes with scaling:

    ∫₀¹ λf
      = λ ∫₀¹ f
      = λ·0
      = 0,

so λf ∈ U₀.

<!-- correct -->

5. Is 𝐑² a subspace of the complex vector space 𝐂²?

No. Since 𝐂² is a complex vector space, 𝐅 = 𝐂, and by 1.33 a subspace must
carry the same scalar multiplication. So closure under scalar multiplication
must hold for all a ∈ 𝐂, and it fails:

    (1, 0) ∈ 𝐑²,  i ∈ 𝐂,
    i(1, 0) = (i, 0) ∉ 𝐑².

<!-- correct -->

6. (a) Is {(a, b, c) ∈ 𝐑³ : a³ = b³} a subspace of 𝐑³?
   (b) Is {(a, b, c) ∈ 𝐂³ : a³ = b³} a subspace of 𝐂³?

(a) Yes. On 𝐑 the map x ↦ x³ is strictly increasing, hence injective, so

    a³ = b³ ⟺ a = b,

and the set equals {(a, b, c) ∈ 𝐑³ : a − b + 0c = 0}. That is the shape of
exercise 1(a) with coefficients (1, −1, 0), so the argument there applies
verbatim.

(b) No. Injectivity fails on 𝐂, and closure under addition fails. Let
ω = (−1 + √3 i)/2 be the cube root of 1 from exercise 1A.7, and let
ω̄ = ω² = (−1 − √3 i)/2, so that ω̄³ = (ω³)² = 1. Then

    (ω, 1, 0) and (ω̄, 1, 0) are in the set, since ω³ = 1³ and ω̄³ = 1³,
    (ω, 1, 0) + (ω̄, 1, 0) = (ω + ω̄, 2, 0) = (−1, 2, 0),
    (−1)³ = −1 ≠ 8 = 2³.

<!-- correct -->

7. Prove or give a counterexample: If U is a nonempty subset of 𝐑² such that U
   is closed under addition and under taking additive inverses (meaning
   −u ∈ U whenever u ∈ U), then U is a subspace of 𝐑².

Counterexample: U = 𝐙² = {(m, n) ∈ 𝐑² : m, n ∈ 𝐙}.

    U is nonempty, since (0, 0) ∈ U.
    (m₁, n₁) + (m₂, n₂) = (m₁ + m₂, n₁ + n₂) ∈ U, so U is closed under
      addition.
    −(m, n) = (−m, −n) ∈ U, so U is closed under additive inverses.

But U is not closed under scalar multiplication:

    (1, 1) ∈ U,  0.5 ∈ 𝐑,
    0.5(1, 1) = (0.5, 0.5) ∉ U.

So U is not a subspace of 𝐑² by 1.34.

<!-- correct -->

8. Give an example of a nonempty subset U of 𝐑² such that U is closed under
   scalar multiplication, but U is not a subspace of 𝐑².

Take U = {(x, y) ∈ 𝐑² : xy = 0}, the union of the two coordinate axes.

U is nonempty, since (0, 0) ∈ U.

U is closed under scalar multiplication: for λ ∈ 𝐑 and (x, y) ∈ U,

    λ(x, y) = (λx, λy),
    (λx)(λy) = λ²(xy) = λ²·0 = 0,

so λ(x, y) ∈ U.

U is not closed under addition:

    (1, 0), (0, 1) ∈ U,  since 1·0 = 0 and 0·1 = 0,
    (1, 0) + (0, 1) = (1, 1),
    1·1 = 1 ≠ 0.

So U is not a subspace of 𝐑² by 1.34.

<!-- correct -->

9. A function f : 𝐑 → 𝐑 is called _periodic_ if there exists a positive number
   p such that f(x) = f(x + p) for all x ∈ 𝐑. Is the set of periodic functions
   from 𝐑 to 𝐑 a subspace of 𝐑^𝐑? Explain.

No. Suppose the set of periodic functions were a subspace of 𝐑^𝐑.

Let

    f(x) = sin²(x),
    g(x) = sin²(πx).

Both are periodic (with periods π and 1 respectively), so f + g is periodic
by closure under addition.

Since f ≥ 0 and g ≥ 0,

    (f + g)(x) = 0  ⟺  f(x) = 0 and g(x) = 0.

Let p > 0 be a period of f + g. Then

    (f + g)(p) = (f + g)(0) = 0,

so f(p) = 0 and g(p) = 0. Hence

    f(p) = 0  ⟹  p = k₁π  for some k₁ ∈ 𝐙,
    g(p) = 0  ⟹  p = k₂    for some k₂ ∈ 𝐙,

and since p > 0 we have k₁ ≠ 0. Therefore

    k₁π = k₂,
    π = k₂/k₁,

contradicting the irrationality of π.

<!-- correct -->

10. Suppose V₁ and V₂ are subspaces of V. Prove that the intersection V₁ ∩ V₂
    is a subspace of V.

Subset:

    V₁ ⊆ V and V₂ ⊆ V, therefore V₁ ∩ V₂ ⊆ V.

Additive identity:

    0 ∈ V₁ and 0 ∈ V₂, since V₁ and V₂ are both subspaces of V,
    so 0 ∈ V₁ ∩ V₂.

Closed under addition, for V₁:

    u, w ∈ V₁ ∩ V₂  ⟹  u, w ∈ V₁  ⟹  u + w ∈ V₁   (V₁ is a subspace of V)

Same for V₂. Then

    u + w ∈ V₁ and u + w ∈ V₂  ⟹  u + w ∈ V₁ ∩ V₂.

Closed under scalar multiplication, for V₁, with c ∈ 𝐅:

    u ∈ V₁ ∩ V₂  ⟹  u ∈ V₁  ⟹  cu ∈ V₁   (V₁ is a subspace of V)

Same for V₂. Then

    cu ∈ V₁ and cu ∈ V₂  ⟹  cu ∈ V₁ ∩ V₂.

So V₁ ∩ V₂ is a subspace of V by 1.34.

<!-- correct -->

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
