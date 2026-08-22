---
name: definitions-setup
description: Extract definitions, theorems, notations, and other important foundational information from a chapter and write them to definitions.md.
---

# Definitions setup

Set up an `definitions.md` for a particular chapter.
These will be the crucial pieces of foundational information that the chapter is based on, and that the exercises test the understanding of.
This should be extracted from the text verbatim.

Provide page numbers.

## Example

This is an example snippet of the file you would generate for Chapter 1 of Linear Algebra Done Right by Axler:

`ch01/definitions.md`:
```
# Chapter 1 definitions

## 1.1 definition: complex numbers, 𝐂 (page 2)

  - A _complex number_ is an ordered pair (a,b), where a, b ∈ 𝐑, but we will write this as a + bi.
  - The set of all complex numbers is denoted by 𝐂:

    𝐂 = {a + bi: a, b ∈ 𝐑}

  - _Addition_ and _multiplication_ on 𝐂 are defined by

    (a + bi) + (c + di) = (a + c) + (b + d)i,
    (a + bi)(c + di) = (ac - bd) + (ad + bc)i;

  here a, b, c, d ∈ 𝐑.

## properties of complex arithmetic (page 3)

commutativity
  α + β = β + α and αβ = βα for all α, β ∈ 𝐂

associativity
  (α + β) + λ = α + (β + λ) and (αβ)λ = α(βλ) for all α, β, λ ∈ 𝐂

...
```
