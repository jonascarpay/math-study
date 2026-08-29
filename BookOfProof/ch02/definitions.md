# Chapter 2 definitions — Logic

Hammack numbers Definitions, Facts and Examples in separate per-chapter
sequences. Cite by kind and number ("Definition 2.1", "Fact 2.2").

Note: in this book `∼` is **negation** ("not P"), never an equivalence
relation.

## 2.1 Statements

### statement (page 35)

A _statement_ is a sentence or a mathematical expression that is either
definitely true or definitely false.

You can think of statements as pieces of information that are either correct
or incorrect. Thus statements are pieces of information that we might apply
logic to in order to produce other pieces of information (which are also
statements).

### Example 2.1 — statements, all true (page 35)

  - If a circle has radius r, then its area is πr² square units.
  - Every even number is divisible by 2.
  - 2 ∈ ℤ
  - √2 ∉ ℤ
  - ℕ ⊆ ℤ
  - The set {0, 1, 2} has three elements.
  - Some right triangles are isosceles.

### Example 2.2 — statements, all false (page 35)

  - All right triangles are isosceles.
  - 5 = 2
  - √2 ∉ ℝ
  - ℤ ⊆ ℕ
  - {0, 1, 2} ∩ ℕ = ∅

### Example 2.3 — non-statements paired with statements (page 35)

| NOT a statement | Statement |
|---|---|
| Add 5 to both sides. | Adding 5 to both sides of x − 5 = 37 gives x = 42. |
| ℤ | 42 ∈ ℤ |
| 42 | 42 is not a number. |
| What is the solution of 2x = 84? | The solution of 2x = 84 is 42. |

### naming statements, P(x) (page 36)

We will often use the letters P, Q, R and S to stand for specific
statements. When more letters are needed we can use subscripts.

When a sentence or statement P contains a variable such as x, we sometimes
denote it as P(x) to indicate that it is saying something about x. A
statement or sentence involving two variables might be denoted P(x, y), and
so on.

### open sentence (page 36)

A sentence whose truth depends on the value of one or more variables is
called an _open sentence_.

Q(x) : The integer x is even.

Whether it is true or false depends on just which integer x is. It is true
if x = 4 and false if x = 7. Since it is neither definitely true nor
definitely false, Q(x) cannot be a statement.

The variables in an open sentence (or statement) can represent any type of
entity, not just numbers. R(f, g) : "The function f is the derivative of the
function g" is an open sentence whose variables are functions. (page 37)

## 2.2 And, Or, Not

### ∧, "and" (page 39)

If P and Q are statements, P ∧ Q stands for the statement "P and Q." The
statement P ∧ Q is true if both P and Q are true; otherwise it is false.

    P  Q   P∧Q
    T  T    T
    T  F    F
    F  T    F
    F  F    F

In this table, T stands for "True," and F stands for "False." (T and F are
called _truth values_.) Such a table is called a _truth table_.

### ∨, "or" (page 40)

In mathematics, the assertion "P or Q" is always understood to mean that one
or both of P and Q is true.

    P  Q   P∨Q
    T  T    T
    T  F    T
    F  T    T
    F  F    F

This differs from everyday use, where "or" often means exactly one. To
express that exactly one of P and Q is true, use one of:

  - P or Q, but not both.
  - Either P or Q.
  - Exactly one of P or Q.

### ∼, negation (page 41)

We use the symbol ∼ to stand for the words "It's not true that," so ∼P means
"It's not true that P." We can read ∼P simply as "not P." Unlike ∧ and ∨,
which combine two statements, the symbol ∼ just alters a single statement.

    P   ∼P
    T   F
    F   T

The statement ∼P is called the _negation_ of P. The negation of a specific
statement can be expressed in numerous ways. For P : "The number 2 is even,"

  - ∼P : It's not true that the number 2 is even.
  - ∼P : It is false that the number 2 is even.
  - ∼P : The number 2 is not even.

These operations can also be applied to open sentences, or to a mixture of
open sentences and statements.

## 2.3 Conditional Statements

### ⇒, conditional statement (page 42)

Given any two statements P and Q whatsoever, we can form the new statement
"If P, then Q." This is written symbolically as P ⇒ Q, which we read as "If
P, then Q," or "P implies Q."

When we assert that the statement P ⇒ Q is true, we mean that if P is true
then Q must also be true. (In other words we mean that the condition P being
true forces Q to be true.) A statement of form P ⇒ Q is called a
_conditional statement_ because it means Q will be true under the condition
that P is true.

Think of P ⇒ Q as a promise that whenever P is true, Q will be true also.
There is only one way this promise can be broken (i.e., be false), namely if
P is true but Q is false. (page 43)

    P  Q  P⇒Q
    T  T   T
    T  F   F
    F  T   T
    F  F   T

### English constructions meaning P ⇒ Q (page 44)

  - P implies Q.
  - If P, then Q.
  - Q if P.
  - Q whenever P.
  - Q, provided that P.
  - Whenever P, then also Q.
  - P is a sufficient condition for Q.
  - For Q, it is sufficient that P.
  - Q is a necessary condition for P.
  - For P, it is necessary that Q.
  - P only if Q.

P ⇒ Q means the condition of P being true is enough (i.e., sufficient) to
make Q true; hence "P is a sufficient condition for Q." And P ⇒ Q being true
means that it's impossible that P is true but Q is false, so in order for P
to be true it is necessary that Q is true; hence "Q is a necessary condition
for P." And this means that P can only be true if Q is true, i.e., "P only
if Q." (page 45)

## 2.4 Biconditional Statements

### converse (page 46)

The conditional statement Q ⇒ P is called the _converse_ of P ⇒ Q, so a
conditional statement and its converse express entirely different things.

    (a is a multiple of 6) ⇒ (a is divisible by 2)     true
    (a is divisible by 2) ⇒ (a is a multiple of 6)     not necessarily true

### ⇔, biconditional statement (page 46)

The expression P ⇔ Q is understood to have exactly the same meaning as
(P ⇒ Q) ∧ (Q ⇒ P).

Q ⇒ P is read as "P if Q," and P ⇒ Q can be read as "P only if Q." Therefore
we pronounce P ⇔ Q as "P if and only if Q."

    P  Q  P⇔Q
    T  T   T
    T  F   F
    F  T   F
    F  F   T

In general, P ⇔ Q being true means P and Q are both true or both false.
(page 47)

### English constructions meaning P ⇔ Q (page 47)

  - P if and only if Q.
  - P is a necessary and sufficient condition for Q.
  - For P it is necessary and sufficient that Q.
  - P is equivalent to Q.
  - If P, then Q, and conversely.

## 2.5 Truth Tables for Statements

### building truth tables (page 48)

For a compound statement, list the possible true/false combinations of the
component statements, then tally the truth values of intermediate
expressions in "helper columns" before combining them. A statement in n
letters needs 2ⁿ lines.

Example, (P ∨ Q) ∧ ∼(P ∧ Q), which means "P or Q is true, and it is not the
case that both P and Q are true":

    P  Q   (P∨Q)   (P∧Q)   ∼(P∧Q)   (P∨Q)∧∼(P∧Q)
    T  T     T       T        F           F
    T  F     T       F        T           T
    F  T     T       F        T           T
    F  F     F       F        T           F

### parentheses and the scope of ∼ (page 50)

The symbol ∼ is analogous to the minus sign in algebra. It negates the
expression it precedes. Thus ∼P ∨ Q means (∼P) ∨ Q, not ∼(P ∨ Q). In
∼(P ∨ Q), the value of the entire expression P ∨ Q is negated.

Parentheses are likewise necessary in P ⇔ (Q ∨ R), for without them we
wouldn't know whether to read the statement as P ⇔ (Q ∨ R) or (P ⇔ Q) ∨ R.
(page 48)

## 2.6 Logical Equivalence

### logical equivalence, = (page 51)

Two statements are _logically equivalent_ if their truth values match up
line-for-line in a truth table.

This is written with an equals sign, e.g.

    P ⇔ Q  =  (P ∧ Q) ∨ (∼P ∧ ∼Q).

Logical equivalence is important because it can give us different (and
potentially useful) ways of looking at the same thing.

### Fact 2.1 — DeMorgan's Laws (page 51)

  1. ∼(P ∧ Q) = (∼P) ∨ (∼Q)
  2. ∼(P ∨ Q) = (∼P) ∧ (∼Q)

DeMorgan's laws are actually very natural and intuitive. Consider the
statement ∼(P ∧ Q), which we can interpret as meaning that it is not the
case that both P and Q are true. If it is not the case that both P and Q are
true, then at least one of P or Q is false, in which case (∼P) ∨ (∼Q) is
true.

### summary of significant logical equivalences (page 52)

    P ⇒ Q = (∼Q) ⇒ (∼P)                      Contrapositive law   (2.1)

    ∼(P ∧ Q) = ∼P ∨ ∼Q
    ∼(P ∨ Q) = ∼P ∧ ∼Q                       DeMorgan's laws      (2.2)

    P ∧ Q = Q ∧ P
    P ∨ Q = Q ∨ P                            Commutative laws     (2.3)

    P ∧ (Q ∨ R) = (P ∧ Q) ∨ (P ∧ R)
    P ∨ (Q ∧ R) = (P ∨ Q) ∧ (P ∨ R)          Distributive laws    (2.4)

    P ∧ (Q ∧ R) = (P ∧ Q) ∧ R
    P ∨ (Q ∨ R) = (P ∨ Q) ∨ R                Associative laws     (2.5)

The associative laws mean the position of the parentheses is irrelevant, so
we can write P ∧ Q ∧ R and P ∨ Q ∨ R without ambiguity. But parentheses are
essential when there is a mix of ∧ and ∨: P ∨ (Q ∧ R) and (P ∨ Q) ∧ R are
not logically equivalent.

## 2.7 Quantifiers

### Definition 2.1 — quantifiers, ∀ and ∃ (page 53)

The symbols ∀ and ∃ are called _quantifiers_.

  - ∀ stands for the phrase "For all" or "For every," or "For each,"
  - ∃ stands for the phrase "There exists a" or "There is a."

"Every element of X is odd" is written ∀x ∈ X, P(x); "There is at least one
element of X that is odd" is written ∃x ∈ X, P(x).

### universal and existential quantification (page 54)

The symbol ∀ is called the _universal quantifier_ and ∃ is called the
_existential quantifier_. Statements containing them are called _quantified
statements_. A statement beginning with ∀ is called a _universally
quantified statement_, and one beginning with ∃ is called an _existentially
quantified statement_.

Given a set X, a quantified statement of form ∀x ∈ X, P(x) is understood to
be true if P(x) is true for every x ∈ X. If there is at least one x ∈ X for
which P(x) is false, then ∀x ∈ X, P(x) is a false statement. Similarly,
∃x ∈ X, P(x) is true provided that P(x) is true for at least one element
x ∈ X; otherwise it is false.

### Example 2.5 — true quantified statements (page 54)

  - Every integer that is not odd is even.
    ∀n ∈ ℤ, ∼(n is odd) ⇒ (n is even),  or  ∀n ∈ ℤ, ∼O(n) ⇒ E(n).
  - There is an integer that is not even.
    ∃n ∈ ℤ, ∼E(n).
  - For every real number x, there is a real number y for which y³ = x.
    ∀x ∈ ℝ, ∃y ∈ ℝ, y³ = x.
  - Given any two rational numbers a and b, the product ab is rational.
    ∀a, b ∈ ℚ, ab ∈ ℚ.

A statement such as "There exists a subset X of ℕ for which |X| = 5" can be
translated in several ways:

    ∃X, (X ⊆ ℕ) ∧ (|X| = 5)   or   ∃X ⊆ ℕ, |X| = 5   or   ∃X ∈ 𝒫(ℕ), |X| = 5.

### Example 2.6 — false quantified statements (page 54)

  - Every integer is even. ∀n ∈ ℤ, E(n).
  - There is an integer n for which n² = 2. ∃n ∈ ℤ, n² = 2.
  - For every real number x, there is a real number y for which y² = x.
    ∀x ∈ ℝ, ∃y ∈ ℝ, y² = x.
  - Given any two rational numbers a and b, the number √(ab) is rational.
    ∀a, b ∈ ℚ, √(ab) ∈ ℚ.

### Example 2.7 — order of quantifiers matters (page 55)

When a statement contains two quantifiers you must be very alert to their
order, for reversing the order can change the meaning.

    ∀x ∈ ℝ, ∃y ∈ ℝ, y³ = x       true  (take y = ∛x)
    ∃y ∈ ℝ, ∀x ∈ ℝ, y³ = x       false (no single y works for every x)

Quantified statements are often misused in casual conversation. Do not say
"All integers are not even," because that means there are no even integers.
Instead, say "Not all integers are even."

## 2.8 More on Conditional Statements

### the implied universal quantifier (page 56)

In mathematics, whenever P(x) and Q(x) are open sentences concerning
elements x in some set X (depending on context), an expression of form
P(x) ⇒ Q(x) is understood to be the statement ∀x ∈ X, P(x) ⇒ Q(x). In other
words, **if a conditional statement is not explicitly quantified then there
is an implied universal quantifier in front of it.**

So "If x is a multiple of 6, then x is even" is a true statement, and "If x
is even, then x is a multiple of 6" is a false statement.

### Definition 2.2 (page 57)

If P and Q are statements or open sentences, then

    "If P, then Q,"

is a statement. This statement is true if it's impossible for P to be true
while Q is false. It is false if there is at least one instance in which P
is true but Q is false.

True: "If x ∈ ℝ, then x² + 1 > 0." False: "If p is a prime number, then p is
odd." (2 is prime.)

## 2.9 Translating English to Symbolic Logic

### Fact 2.2 (page 58)

Suppose X is a set and Q(x) is a statement about x for each x ∈ X. The
following statements mean the same thing:

    ∀x ∈ X, Q(x)
    (x ∈ X) ⇒ Q(x).

Every universally quantified statement can be expressed as a conditional
statement. This is significant because so many theorems have the form of a
conditional statement; understanding this fact allows us to switch between
the two forms.

### translating with attention to meaning (page 58)

In translating a statement, be attentive to its intended meaning. Don't jump
into, for example, automatically replacing every "and" with ∧ and "or" with
∨.

  - "At least one of the integers x and y is even" is
    (x is even) ∨ (y is even) — despite the word "and."
  - The logical meaning of "but" can be captured by "and": "The integer x is
    even, but the integer y is odd" is (x is even) ∧ (y is odd).

### Example 2.8 — the Mean Value Theorem (page 57)

  If f is continuous on the interval [a,b] and differentiable on (a,b), then
  there is a number c ∈ (a,b) for which f′(c) = (f(b) − f(a))/(b − a).

    ((f cont. on [a,b]) ∧ (f is diff. on (a,b))) ⇒ (∃c ∈ (a,b), f′(c) = (f(b)−f(a))/(b−a))

## 2.10 Negating Statements

### negating a statement (page 59)

Given a statement R, the statement ∼R is called the _negation_ of R. If R is
a complex statement, then it is often the case that its negation ∼R can be
written in a simpler or more useful form. The process of finding this form
is called _negating_ R.

DeMorgan's laws can be viewed as rules that tell us how to negate the
statements P ∧ Q and P ∨ Q:

    ∼(P ∧ Q) = (∼P) ∨ (∼Q)                                      (2.6)
    ∼(P ∨ Q) = (∼P) ∧ (∼Q)                                      (2.7)

### negating quantified statements (page 60)

    ∼(∀x ∈ X, P(x))  =  ∃x ∈ X, ∼P(x)                           (2.8)
    ∼(∃x ∈ X, P(x))  =  ∀x ∈ X, ∼P(x)                           (2.9)

Reading ∼(∀x ∈ ℕ, P(x)) in words: "It is not the case that P(x) is true for
all natural numbers x." This means P(x) is false for at least one x.

### negating a conditional statement (page 61)

∼(P ⇒ Q) literally says "P ⇒ Q is false." The only way P ⇒ Q can be false is
if P is true and Q is false. Therefore

    ∼(P ⇒ Q)  =  P ∧ ∼Q.                                       (2.10)

### Example 2.15 — negating a conditional with a variable (page 62)

R : If x is odd, then x² is odd. Interpreted as ∀x ∈ ℤ, (x odd) ⇒ (x² odd).

    ∼(∀x ∈ ℤ, (x odd) ⇒ (x² odd))  = ∃x ∈ ℤ, ∼((x odd) ⇒ (x² odd))
                                    = ∃x ∈ ℤ, (x odd) ∧ ∼(x² odd).

∼R : There is an odd integer x whose square is not odd.

## 2.11 Logical Inference

### logical inference (page 63)

From two true statements we infer that a third statement is true. In
essence, statements P ⇒ Q and P are "added together" to get Q. We indicate
this by stacking the assumed statements atop a line, with the conclusion
below it.

    Modus Ponens      Modus Tollens      Elimination
      P ⇒ Q              P ⇒ Q              P ∨ Q
      P                  ∼Q                 ∼P
      ─────              ─────              ─────
      Q                  ∼P                 Q

You need not remember their names; few mathematicians can recall the names,
though they use the rules constantly. The names are not important, but the
rules are.

### three more inferences (page 64)

    P                 P ∧ Q             P
    Q                 ─────             ─────
    ─────             P                 P ∨ Q
    P ∧ Q

If P and Q are both true, then so is the statement P ∧ Q. On the other hand,
P ∧ Q being true forces P (also Q) to be true. Finally, if P is true, then
P ∨ Q must be true, no matter what statement Q is.

## 2.12 An Important Note

### why we study logic (page 64)

  - The truth tables tell us the exact meanings of words such as "and,"
    "or," "not" and so on.
  - The rules of inference provide a system in which we can produce new
    information (statements) from known information.
  - Logical rules such as DeMorgan's laws help us correctly change certain
    statements into (potentially more useful) statements with the same
    meaning.

Logic's place is in the background of what we do, not the forefront. From
here on, the beautiful symbols ∧, ∨, ⇒, ⇔, ∼, ∀ and ∃ are rarely written.
But we are aware of their meanings constantly.
