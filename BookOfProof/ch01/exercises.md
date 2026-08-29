# Chapter 1 exercises — Sets

Set complement is written with an overline, `A̅`. When the bar covers a
compound expression it is written `‾(A ∩ B)`.

# Exercises for Section 1.1, page 7

**A.** Write each of the following sets by listing their elements between braces.

1. {5x − 1 : x ∈ ℤ}

{…, −6, −1, 4, 9, …}

<!-- correct -->

2. {3x + 2 : x ∈ ℤ}

{…, −4, −1, 2, 5, …}

<!-- correct -->

3. {x ∈ ℤ : −2 ≤ x < 7}

{−2, −1, 0, 1, 2, 3, 4, 5, 6}

<!-- correct -->

4. {x ∈ ℕ : −2 < x ≤ 7}

{1, 2, 3, 4, 5, 6, 7}

<!-- correct -->

5. {x ∈ ℝ : x² = 3}

{√3, −√3}

<!-- correct -->

6. {x ∈ ℝ : x² = 9}

{3, −3}

<!-- correct -->

7. {x ∈ ℝ : x² + 5x = −6}

{−2, −3}

<!-- correct -->

8. {x ∈ ℝ : x³ + 5x² = −6x}

{−2, −3, 0}

<!-- correct -->

9. {x ∈ ℝ : sin πx = 0}

ℤ = {…, −2, −1, 0, 1, 2, …}

<!-- correct -->

10. {x ∈ ℝ : cos x = 1}

{…, −2τ, −τ, 0, τ, 2τ, …} = {τx : x ∈ ℤ}

<!-- correct -->

11. {x ∈ ℤ : |x| < 5}

{−4, −3, −2, −1, 0, 1, 2, 3, 4}

<!-- correct -->

12. {x ∈ ℤ : |2x| < 5}

{−2, −1, 0, 1, 2}

<!-- correct -->

13. {x ∈ ℤ : |6x| < 5}

{0}

<!-- correct -->

14. {5x : x ∈ ℤ, |2x| ≤ 8}

{−20, −15, −10, −5, 0, 5, 10, 15, 20}

<!-- correct -->

15. {5a + 2b : a, b ∈ ℤ}

ℤ = {…, −2, −1, 0, 1, 2, …}

For any n ∈ ℤ, take a = n and b = −2n. Then

    5a + 2b = 5n + 2(−2n) = n.

<!-- correct -->

16. {6a + 2b : a, b ∈ ℤ}

{…, −4, −2, 0, 2, 4, …} = {2n : n ∈ ℤ}

Multiplying by 6 and by 2, and addition, preserve evenness, so 6a + 2b is
always even.

Conversely, for any even number 2n, pick a = 0 and b = n:

    6a + 2b = 6·0 + 2n = 2n,

so every even number is of this form.

<!-- correct -->

**B.** Write each of the following sets in set-builder notation.

17. {2, 4, 8, 16, 32, 64, …}

{2ⁿ : n ∈ ℕ}

<!-- correct -->

18. {0, 4, 16, 36, 64, 100, …}

{(2n − 2)² : n ∈ ℕ}

<!-- correct -->

19. {…, −6, −3, 0, 3, 6, 9, 12, 15, …}

{3n : n ∈ ℤ}

<!-- correct -->

20. {…, −8, −3, 2, 7, 12, 17, …}

{5n − 3 : n ∈ ℤ}

<!-- correct -->

21. {0, 1, 4, 9, 16, 25, 36, …}

{n² : n ∈ ℤ}

<!-- correct -->

22. {3, 6, 11, 18, 27, 38, …}

{n² + 2 : n ∈ ℕ}

<!-- correct -->

23. {3, 4, 5, 6, 7, 8}

{n ∈ ℕ : 3 ≤ n ≤ 8}

<!-- correct -->

24. {−4, −3, −2, −1, 0, 1, 2}

{n ∈ ℤ : −4 ≤ n ≤ 2}

<!-- correct -->

25. {…, 1/8, 1/4, 1/2, 1, 2, 4, 8, …}

{2ⁿ : n ∈ ℤ}

<!-- correct -->

26. {…, 1/27, 1/9, 1/3, 1, 3, 9, 27, …}

{3ⁿ : n ∈ ℤ}

<!-- correct -->

27. {…, −π, −π/2, 0, π/2, π, 3π/2, 2π, 5π/2, …}

{πn/2 : n ∈ ℤ}

<!-- correct -->

28. {…, −3/2, −3/4, 0, 3/4, 3/2, 9/4, 3, 15/4, 9/2, …}

{3n/4 : n ∈ ℤ}

<!-- correct -->

**C.** Find the following cardinalities.

29. |{{1}, {2, {3,4}}, ∅}|

3

<!-- correct -->

30. |{{1,4}, a, b, {{3,4}}, {∅}}|

5

<!-- correct -->

31. |{{{1}, {2, {3,4}}, ∅}}|

1

<!-- correct -->

32. |{{{1,4}, a, b, {{3,4}}, {∅}}}|

1

<!-- correct -->

33. |{x ∈ ℤ : |x| < 10}|

19

<!-- correct -->

34. |{x ∈ ℕ : |x| < 10}|

9

<!-- correct -->

35. |{x ∈ ℤ : x² < 10}|

7

<!-- correct -->

36. |{x ∈ ℕ : x² < 10}|

3

<!-- correct -->

37. |{x ∈ ℕ : x² < 0}|

0

<!-- correct -->

38. |{x ∈ ℕ : 5x ≤ 20}|

4

<!-- correct -->

**D.** Sketch the following sets of points in the x-y plane.

39. {(x,y) : x ∈ [1,2], y ∈ [1,2]}

The filled quadrilateral with corners (1,1), (1,2), (2,1), (2,2).

<!-- correct -->

40. {(x,y) : x ∈ [0,1], y ∈ [1,2]}

The filled quadrilateral with edges and corners (0,1), (0,2), (1,1), (1,2).

<!-- correct -->

41. {(x,y) : x ∈ [−1,1], y = 1}

The line segment from (−1,1) to (1,1).

<!-- correct -->

42. {(x,y) : x = 2, y ∈ [0,1]}

The line segment from (2,0) to (2,1).

<!-- correct -->

43. {(x,y) : |x| = 2, y ∈ [0,1]}

Two line segments, from (2,0) to (2,1) and from (−2,0) to (−2,1).

<!-- correct -->

44. {(x, x²) : x ∈ ℝ}

The parabola y = x².

<!-- correct -->

45. {(x,y) : x, y ∈ ℝ, x² + y² = 1}

The circle centered at the origin with radius 1.

<!-- correct -->

46. {(x,y) : x, y ∈ ℝ, x² + y² ≤ 1}

The filled disk, including its edge, centered at the origin with radius 1.

<!-- correct -->

47. {(x,y) : x, y ∈ ℝ, y ≥ x² − 1}

The parabola y = x² − 1 together with every point above it.

<!-- correct -->

48. {(x,y) : x, y ∈ ℝ, x > 1}

The region of the plane to the right of the line x = 1.

<!-- correct -->

49. {(x, x + y) : x ∈ ℝ, y ∈ ℤ}

The lines of slope 1 crossing the y-axis at the integers.

<!-- correct -->

50. {(x, x²/y) : x ∈ ℝ, y ∈ ℕ}

An infinite set of parabolas: y = x² at the top, then y = x²/n scaled down by
a factor n, for n = 1, 2, 3, ….

<!-- correct -->

51. {(x,y) ∈ ℝ² : (y − x)(y + x) = 0}

The two lines y = ±x.

<!-- correct -->

52. {(x,y) ∈ ℝ² : (y − x²)(y + x²) = 0}

Same as 51: the two parabolas y = ±x².

<!-- correct -->

# Exercises for Section 1.2, page 11

**A.** Write out the indicated sets by listing their elements between braces.

1. Suppose A = {1, 2, 3, 4} and B = {a, c}.

   (a) A × B
   (b) B × A
   (c) A × A
   (d) B × B
   (e) ∅ × B
   (f) (A × B) × B
   (g) A × (B × B)
   (h) B³

(a) {(1,a), (1,c), (2,a), (2,c), (3,a), (3,c), (4,a), (4,c)}

(b) Same as (a) but flipped:
    {(a,1), (a,2), (a,3), (a,4), (c,1), (c,2), (c,3), (c,4)}

(c) {(1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4),
     (3,1), (3,2), (3,3), (3,4), (4,1), (4,2), (4,3), (4,4)}

(d) {(a,a), (a,c), (c,a), (c,c)}

(e) ∅

(f) {((1,a),a), ((1,a),c), ((1,c),a), ((1,c),c),
     ((2,a),a), ((2,a),c), ((2,c),a), ((2,c),c),
     ((3,a),a), ((3,a),c), ((3,c),a), ((3,c),c),
     ((4,a),a), ((4,a),c), ((4,c),a), ((4,c),c)}

(g) {(1,(a,a)), (1,(a,c)), (1,(c,a)), (1,(c,c)),
     (2,(a,a)), (2,(a,c)), (2,(c,a)), (2,(c,c)),
     (3,(a,a)), (3,(a,c)), (3,(c,a)), (3,(c,c)),
     (4,(a,a)), (4,(a,c)), (4,(c,a)), (4,(c,c))}

(h) {(a,a,a), (a,a,c), (a,c,a), (a,c,c),
     (c,a,a), (c,a,c), (c,c,a), (c,c,c)}

<!-- correct -->

2. Suppose A = {π, e, 0} and B = {0, 1}.

   (a) A × B
   (b) B × A
   (c) A × A
   (d) B × B
   (e) A × ∅
   (f) (A × B) × B
   (g) A × (B × B)
   (h) A × B × B

<!-- skipped -->

3. {x ∈ ℝ : x² = 2} × {a, c, e}

{(√2, a), (−√2, a), (√2, c), (−√2, c), (√2, e), (−√2, e)}

<!-- correct -->

4. {n ∈ ℤ : 2 < n < 5} × {n ∈ ℤ : |n| = 5}

{(3, 5), (3, −5), (4, 5), (4, −5)}

<!-- correct -->

5. {x ∈ ℝ : x² = 2} × {x ∈ ℝ : |x| = 2}

{(√2, 2), (−√2, 2), (√2, −2), (−√2, −2)}

<!-- correct -->

6. {x ∈ ℝ : x² = x} × {x ∈ ℕ : x² = x}

{(0, 1), (1, 1)}

<!-- correct -->

7. {∅} × {0, ∅} × {0, 1}

{(∅, 0, 0), (∅, ∅, 0), (∅, 0, 1), (∅, ∅, 1)}

<!-- correct -->

8. {0, 1}⁴

All 4-tuples of 0s and 1s, in binary counting order:

{(0,0,0,0), (0,0,0,1), (0,0,1,0), (0,0,1,1),
 (0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1),
 (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1),
 (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1)}

<!-- correct -->

**B.** Sketch these Cartesian products on the x-y plane ℝ² (or ℝ³ for the last two).

9. {1, 2, 3} × {−1, 0, 1}

A 3 × 3 grid of 9 points, with (1, 1) at the top left and (3, −1) at the
bottom right:

    y
     1 |  •   •   •
     0 |  •   •   •
    -1 |  •   •   •
       +-----------  x
          1   2   3

<!-- correct -->

10. {−1, 0, 1} × {1, 2, 3}

The same 3 × 3 grid of 9 points, now with (−1, 3) at the top left and
(1, 1) at the bottom right:

    y
     3 |  •   •   •
     2 |  •   •   •
     1 |  •   •   •
       +-----------  x
         -1   0   1

<!-- correct -->

11. [0, 1] × [0, 1]

The filled unit square, with its bottom left corner at the origin.

<!-- correct -->

12. [−1, 1] × [1, 2]

The filled rectangle with corners (−1, 1) and (1, 2).

<!-- correct -->

13. {1, 1.5, 2} × [1, 2]

Three vertical segments from y = 1 to y = 2, at x = 1, x = 1.5 and x = 2.

<!-- correct -->

14. [1, 2] × {1, 1.5, 2}

Three horizontal segments from x = 1 to x = 2, at y = 1, y = 1.5 and y = 2.

<!-- correct -->

15. {1} × [0, 1]

The segment from (1, 0) to (1, 1).

<!-- correct -->

16. [0, 1] × {1}

The segment from (0, 1) to (1, 1).

<!-- correct -->

17. ℕ × ℤ

The unit lattice of points, restricted to those strictly right of the
y-axis.

<!-- correct -->

18. ℤ × ℤ

The whole unit lattice.

<!-- correct -->

19. [0, 1] × [0, 1] × [0, 1]

The filled unit cube, with opposite corners (0, 0, 0) and (1, 1, 1).

<!-- correct -->

20. {(x,y) ∈ ℝ² : x² + y² ≤ 1} × [0, 1]

A solid cylinder around the z-axis, of unit radius, from z = 0 to z = 1.

<!-- correct -->

# Exercises for Section 1.3, page 15

**A.** List all the subsets of the following sets.

1. {1, 2, 3, 4}

∅,
{1}, {2}, {3}, {4},
{1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4},
{2,3,4}, {1,3,4}, {1,2,4}, {1,2,3},
{1,2,3,4}

<!-- correct -->

2. {1, 2, ∅}

∅, {1}, {2}, {∅}, {1,2}, {1,∅}, {2,∅}, {1,2,∅}

<!-- correct -->

3. {{ℝ}}

∅, {{ℝ}}

<!-- correct -->

4. ∅

∅

<!-- correct -->

5. {∅}

∅, {∅}

<!-- correct -->

6. {ℝ, ℚ, ℕ}

∅, {ℝ}, {ℚ}, {ℕ}, {ℝ,ℚ}, {ℝ,ℕ}, {ℚ,ℕ}, {ℝ,ℚ,ℕ}

<!-- correct -->

7. {ℝ, {ℚ, ℕ}}

∅, {ℝ}, {{ℚ,ℕ}}, {ℝ, {ℚ,ℕ}}

<!-- correct -->

8. {{0,1}, {0,1,{2}}, {0}}

<!-- skipped -->

**B.** Write out the following sets by listing their elements between braces.

9. {X : X ⊆ {3, 2, a} and |X| = 2}

{{3,2}, {3,a}, {2,a}}

<!-- correct -->

10. {X ⊆ ℕ : |X| ≤ 1}

<!-- pending -->

11. {X : X ⊆ {3, 2, a} and |X| = 4}

∅

<!-- correct -->

12. {X : X ⊆ {3, 2, a} and |X| = 1}

<!-- pending -->

**C.** Decide if the following statements are true or false. Explain.

13. ℝ³ ⊆ ℝ³

True. Every set is a subset of itself.

<!-- correct -->

14. ℝ² ⊆ ℝ³

<!-- pending -->

15. {(x,y) ∈ ℝ² : x − 1 = 0} ⊆ {(x,y) ∈ ℝ² : x² − x = 0}

True. The left set has x = 1; the right set has x ∈ {0, 1}. So the left is
a subset of the right.

<!-- correct -->

16. {(x,y) ∈ ℝ² : x² − x = 0} ⊆ {(x,y) ∈ ℝ² : x − 1 = 0}

<!-- pending -->

# Exercises for Section 1.4, page 17

**A.** Write the following sets by listing their elements between braces.

1. 𝒫({{a,b}, {c}})

{∅, {{a,b}}, {{c}}, {{a,b},{c}}}

<!-- correct -->

2. 𝒫({1, 2, 3, 4})

<!-- pending -->

3. 𝒫({{∅}, 5})

{∅, {{∅}}, {5}, {{∅}, 5}}

<!-- correct -->

4. 𝒫({ℝ, ℚ})

<!-- pending -->

5. 𝒫(𝒫({2}))

{∅, {∅}, {{2}}, {∅, {2}}}

<!-- correct -->

6. 𝒫({1,2}) × 𝒫({3})

<!-- pending -->

7. 𝒫({a,b}) × 𝒫({0,1})

All 16 pairs of

    {∅, {a}, {b}, {a,b}}  ×  {∅, {0}, {1}, {0,1}}

<!-- correct -->

8. 𝒫({1,2} × {3})

<!-- pending -->

9. 𝒫({a,b} × {0})

{∅, {(a,0)}, {(b,0)}, {(a,0), (b,0)}}

<!-- correct -->

10. {X ∈ 𝒫({1,2,3}) : |X| ≤ 1}

<!-- pending -->

11. {X ⊆ 𝒫({1,2,3}) : |X| ≤ 1}

{∅, {∅}, {{1}}, {{2}}, {{3}}, {{1,2}}, {{1,3}}, {{2,3}}, {{1,2,3}}}

<!-- correct -->

12. {X ∈ 𝒫({1,2,3}) : 2 ∈ X}

<!-- pending -->

**B.** Suppose that |A| = m and |B| = n. Find the following cardinalities.

13. |𝒫(𝒫(𝒫(A)))|

2^(2^(2^m))

<!-- correct -->

14. |𝒫(𝒫(A))|

<!-- pending -->

15. |𝒫(A × B)|

2^(mn)

<!-- correct -->

16. |𝒫(A) × 𝒫(B)|

<!-- pending -->

17. |{X ∈ 𝒫(A) : |X| ≤ 1}|

m + 1

<!-- correct -->

18. |𝒫(A × 𝒫(B))|

<!-- pending -->

19. |𝒫(𝒫(𝒫(A × ∅)))|

4

<!-- correct -->

20. |{X ⊆ 𝒫(A) : |X| ≤ 1}|

<!-- pending -->

# Exercises for Section 1.5, page 19

1. Suppose A = {4, 3, 6, 7, 1, 9}, B = {5, 6, 8, 4} and C = {5, 8, 4}. Find:

   (a) A ∪ B
   (b) A ∩ B
   (c) A − B
   (d) A − C
   (e) B − A
   (f) A ∩ C
   (g) B ∩ C
   (h) B ∪ C
   (i) C − B

(a) {1, 3, 4, 5, 6, 7, 8, 9}
(b) {4, 6}
(c) {1, 3, 7, 9}
(d) {1, 3, 6, 7, 9}
(e) {5, 8}
(f) {4}
(g) {4, 5, 8}
(h) {4, 5, 6, 8}
(i) ∅

<!-- correct -->

2. Suppose A = {0, 2, 4, 6, 8}, B = {1, 3, 5, 7} and C = {2, 8, 4}. Find:

   (a) A ∪ B
   (b) A ∩ B
   (c) A − B
   (d) A − C
   (e) B − A
   (f) A ∩ C
   (g) B ∩ C
   (h) C − A
   (i) C − B

<!-- pending -->

3. Suppose A = {0, 1} and B = {1, 2}. Find:

   (a) (A × B) ∩ (B × B)
   (b) (A × B) ∪ (B × B)
   (c) (A × B) − (B × B)
   (d) (A ∩ B) × A
   (e) (A × B) ∩ B
   (f) 𝒫(A) ∩ 𝒫(B)
   (g) 𝒫(A) − 𝒫(B)
   (h) 𝒫(A ∩ B)
   (i) 𝒫(A × B)

(a) {(1,1), (1,2)}
(b) {(0,1), (0,2), (1,1), (1,2), (2,1), (2,2)}
(c) {(0,1), (0,2)}
(d) {(1,0), (1,1)}
(e) ∅
(f) {∅, {1}}
(g) {{0}, {0,1}}
(h) {∅, {1}}
(i) the power set of {(0,1), (0,2), (1,1), (1,2)}, 16 elements

<!-- correct -->

4. Suppose A = {b, c, d} and B = {a, b}. Find:

   (a) (A × B) ∩ (B × B)
   (b) (A × B) ∪ (B × B)
   (c) (A × B) − (B × B)
   (d) (A ∩ B) × A
   (e) (A × B) ∩ B
   (f) 𝒫(A) ∩ 𝒫(B)
   (g) 𝒫(A) − 𝒫(B)
   (h) 𝒫(A ∩ B)
   (i) 𝒫(A) × 𝒫(B)

<!-- pending -->

5. Sketch the sets X = [1,3] × [1,3] and Y = [2,4] × [2,4] on the plane ℝ².
   On separate drawings, shade in the sets X ∪ Y, X ∩ Y, X − Y and Y − X.
   (Hint: X and Y are Cartesian products of intervals. You may wish to
   review how you drew sets like [1,3] × [1,3] in the exercises for
   Section 1.2.)

<!-- skipped -->

6. Sketch the sets X = [−1,3] × [0,2] and Y = [0,3] × [1,4] on the plane ℝ².
   On separate drawings, shade in the sets X ∪ Y, X ∩ Y, X − Y and Y − X.

<!-- pending -->

7. Sketch the sets X = {(x,y) ∈ ℝ² : x² + y² ≤ 1} and
   Y = {(x,y) ∈ ℝ² : x ≥ 0} on ℝ². On separate drawings, shade in the sets
   X ∪ Y, X ∩ Y, X − Y and Y − X.

<!-- skipped -->

8. Sketch the sets X = {(x,y) ∈ ℝ² : x² + y² ≤ 1} and
   Y = {(x,y) ∈ ℝ² : −1 ≤ y ≤ 0} on ℝ². On separate drawings, shade in the
   sets X ∪ Y, X ∩ Y, X − Y and Y − X.

<!-- pending -->

9. Is the statement (ℝ × ℤ) ∩ (ℤ × ℝ) = ℤ × ℤ true or false? What about the
   statement (ℝ × ℤ) ∪ (ℤ × ℝ) = ℝ × ℝ?

True. ℝ × ℤ is the horizontal lines at integer height, ℤ × ℝ is the
vertical lines at integer x, so their intersection is the lattice ℤ × ℤ.

False. (1.5, 1.5) is in neither of the two sets.

<!-- correct -->

10. Do you think the statement (ℝ − ℤ) × ℕ = (ℝ × ℕ) − (ℤ × ℕ) is true, or
    false? Justify.

<!-- pending -->

# Exercises for Section 1.6, page 21

1. Let A = {4, 3, 6, 7, 1, 9} and B = {5, 6, 8, 4} have universal set
   U = {0, 1, 2, …, 10}. Find:

   (a) A̅
   (b) B̅
   (c) A ∩ A̅
   (d) A ∪ A̅
   (e) A − A̅
   (f) A − B̅
   (g) A̅ − B̅
   (h) A̅ ∩ B
   (i) ‾(A̅ ∩ B)

<!-- skipped -->

2. Let A = {0, 2, 4, 6, 8} and B = {1, 3, 5, 7} have universal set
   U = {0, 1, 2, …, 8}. Find:

   (a) A̅
   (b) B̅
   (c) A ∩ A̅
   (d) A ∪ A̅
   (e) A − A̅
   (f) ‾(A ∪ B)
   (g) A̅ ∩ B̅
   (h) ‾(A ∩ B)
   (i) A̅ × B

<!-- pending -->

3. Sketch the set X = [1,3] × [1,2] on the plane ℝ². On separate drawings,
   shade in the sets X̅ and X̅ ∩ ([0,2] × [0,3]).

<!-- skipped -->

4. Sketch the set X = [−1,3] × [0,2] on the plane ℝ². On separate drawings,
   shade in the sets X̅ and X̅ ∩ ([−2,4] × [−1,3]).

<!-- pending -->

5. Sketch the set X = {(x,y) ∈ ℝ² : 1 ≤ x² + y² ≤ 4} on the plane ℝ². On a
   separate drawing, shade in the set X̅.

<!-- skipped -->

6. Sketch the set X = {(x,y) ∈ ℝ² : y < x²} on ℝ². Shade in the set X̅.

<!-- pending -->

# Exercises for Section 1.7, page 24

1. Draw a Venn diagram for A̅, where A is a subset of a universal set U.

Shade everything in U outside A.

<!-- correct -->

2. Draw a Venn diagram for B − A.

<!-- pending -->

3. Draw a Venn diagram for (A − B) ∩ C.

Shade everything in both A and C but not in B.

<!-- correct -->

4. Draw a Venn diagram for (A ∪ B) − C.

<!-- pending -->

5. Draw Venn diagrams for A ∪ (B ∩ C) and (A ∪ B) ∩ (A ∪ C). Based on your
   drawings, do you think A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)?

Yes. Both shade all of A together with the region B ∩ C: union distributes
over intersection.

<!-- correct -->

6. Draw Venn diagrams for A ∩ (B ∪ C) and (A ∩ B) ∪ (A ∩ C). Based on your
   drawings, do you think A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)?

<!-- pending -->

7. Suppose sets A and B are in a universal set U. Draw Venn diagrams for
   ‾(A ∩ B) and A̅ ∪ B̅. Based on your drawings, do you think it's true that
   ‾(A ∩ B) = A̅ ∪ B̅?

Yes. Both shade everything except the lens A ∩ B — De Morgan's law.

<!-- correct -->

8. Suppose sets A and B are in a universal set U. Draw Venn diagrams for
   ‾(A ∪ B) and A̅ ∩ B̅. Based on your drawings, do you think it's true that
   ‾(A ∪ B) = A̅ ∩ B̅?

<!-- pending -->

9. Draw a Venn diagram for (A ∩ B) − C.

Shade everything in both A and B but not in C.

<!-- correct -->

10. Draw a Venn diagram for (A − B) ∪ C.

<!-- pending -->

Exercises 11–14 are Venn diagrams in the text for expressions involving sets
A, B and C; write a corresponding expression. In each diagram C is the top
circle and A and B are the bottom-left and bottom-right circles. The shaded
region is described here in words.

11. Shaded: the part of B ∩ C lying outside A.

<!-- skipped -->

12. Shaded: the part of A lying outside B, together with all of B ∩ C.

<!-- pending -->

13. Shaded: all of A ∪ B ∪ C except the central region A ∩ B ∩ C.

<!-- skipped -->

14. Shaded: the part of A lying outside B.

<!-- pending -->

# Exercises for Section 1.8, page 29

1. Suppose A₁ = {a, b, d, e, g, f}, A₂ = {a, b, c, d}, A₃ = {b, d, a} and
   A₄ = {a, b, h}.

   (a) ⋃_{i=1}^{4} Aᵢ =
   (b) ⋂_{i=1}^{4} Aᵢ =

(a) {a, b, c, d, e, f, g, h}
(b) {a, b}

<!-- correct -->

2. Suppose

       A₁ = {0, 2, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24},
       A₂ = {0, 3, 6, 9, 12, 15, 18, 21, 24},
       A₃ = {0, 4, 8, 12, 16, 20, 24}.

   (a) ⋃_{i=1}^{3} Aᵢ =
   (b) ⋂_{i=1}^{3} Aᵢ =

<!-- pending -->

3. For each n ∈ ℕ, let Aₙ = {0, 1, 2, 3, …, n}.

   (a) ⋃_{i ∈ ℕ} Aᵢ =
   (b) ⋂_{i ∈ ℕ} Aᵢ =

(a) {0, 1, 2, 3, …}
(b) {0, 1}

<!-- correct -->

4. For each n ∈ ℕ, let Aₙ = {−2n, 0, 2n}.

   (a) ⋃_{i ∈ ℕ} Aᵢ =
   (b) ⋂_{i ∈ ℕ} Aᵢ =

<!-- pending -->

5. (a) ⋃_{i ∈ ℕ} [i, i+1] =
   (b) ⋂_{i ∈ ℕ} [i, i+1] =

(a) [1, ∞)
(b) ∅

<!-- correct -->

6. (a) ⋃_{i ∈ ℕ} [0, i+1] =
   (b) ⋂_{i ∈ ℕ} [0, i+1] =

<!-- pending -->

7. (a) ⋃_{i ∈ ℕ} ℝ × [i, i+1] =
   (b) ⋂_{i ∈ ℕ} ℝ × [i, i+1] =

(a) ℝ × [1, ∞), the half plane above and including y = 1
(b) ∅

<!-- correct -->

8. (a) ⋃_{α ∈ ℝ} {α} × [0, 1] =
   (b) ⋂_{α ∈ ℝ} {α} × [0, 1] =

<!-- pending -->

9. (a) ⋃_{X ∈ 𝒫(ℕ)} X =
   (b) ⋂_{X ∈ 𝒫(ℕ)} X =

<!-- skipped -->

10. (a) ⋃_{x ∈ [0,1]} [x, 1] × [0, x²] =
    (b) ⋂_{x ∈ [0,1]} [x, 1] × [0, x²] =

<!-- pending -->

11. Is ⋂_{α ∈ I} A_α ⊆ ⋃_{α ∈ I} A_α always true for any collection of sets
    A_α with index set I?

Yes. If x is in every A_α (the left side), then x is in at least one A_α
(the right side), since I ≠ ∅ by Definition 1.8.

<!-- correct -->

12. If ⋂_{α ∈ I} A_α = ⋃_{α ∈ I} A_α, what do you think can be said about
    the relationships between the sets A_α?

<!-- pending -->

13. If J ≠ ∅ and J ⊆ I, does it follow that ⋃_{α ∈ J} A_α ⊆ ⋃_{α ∈ I} A_α?
    What about ⋂_{α ∈ J} A_α ⊆ ⋂_{α ∈ I} A_α?

The first holds. If x ∈ ⋃_{α ∈ J} A_α, then x ∈ A_α for some α ∈ J. Since
J ⊆ I, that α ∈ I, which is the definition of x ∈ ⋃_{α ∈ I} A_α.

The second does not. Take J = {1}, I = {1, 2}, A_1 = {1}, A_2 = ∅. Then

  ⋂_{α ∈ J} A_α = {1},
  ⋂_{α ∈ I} A_α = {1} ∩ ∅ = ∅,

and {1} ⊈ ∅.

<!-- correct -->

14. If J ≠ ∅ and J ⊆ I, does it follow that ⋂_{α ∈ I} A_α ⊆ ⋂_{α ∈ J} A_α?
    Explain.

<!-- pending -->
