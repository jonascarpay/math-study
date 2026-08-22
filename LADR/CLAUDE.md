# Linear Algebra Done Right (Axler), 4th edition

Source: `LADR4e.pdf` (404 PDF pages).

## Plaintext scan

`LADR4e.txt` was generated with:

```
pdftotext -enc UTF-8 LADR4e.pdf LADR4e.txt
```

(No `-layout`. The layout variant interleaved the margin notes worse.)

### Page mapping

Pages are separated by form feeds (`\f`). The offset is constant:

```
PDF page = book page + 14
```

Verified at book p.6 → PDF 20, and Exercises 1A (book p.10) → PDF 24.

To jump to a book page in the plaintext:

```
awk 'BEGIN{p=1} /\f/{p++} p==<PDFPAGE>' LADR4e.txt
```

### Caveats when reading the plaintext

The scan is accurate for prose but **lossy for math**. Do not quote
mathematics from it verbatim — read the PDF pages directly (`Read` with
`pages:`) whenever exact notation matters.

- **Superscripts and subscripts are flattened.** `𝐑2` is really 𝐑², `𝐅𝑛`
  is 𝐅ⁿ, `𝑥1` is x₁, `𝑉𝑘` is V_k. This is the single biggest hazard —
  `𝐅5 = 𝑈 ⊕ 𝑊` reads as nonsense until you restore the exponent.
- **Margin notes are interleaved into the body text** at arbitrary points,
  usually as a standalone paragraph mid-sentence.
- **Display math loses alignment**; multi-line derivations come through as
  separate lines with leading `=`.
- Section headers, running heads, and page numbers appear inline.
- Running head on book p.22 is literally `≈ 7π`, not `22` (an Axler joke).
- Letters use mathematical-italic Unicode (`𝑥`, `𝑛`, `𝛼`) and bold-upright
  for 𝐑, 𝐂, 𝐅, 𝐍, 𝐙 — grep accordingly (plain ASCII `x` will not match).

## Chapter map

Book page → PDF page is always `+14`, so only book pages are listed.

| Chapter | Title | Book pages |
|---|---|---|
| 1 | Vector Spaces | 1–26 |
| 2 | Finite-Dimensional Vector Spaces | 27–50 |
| 3 | Linear Maps | 51–118 |
| 4 | Polynomials | 119–131 |
| 5 | Eigenvalues and Eigenvectors | 132–180 |
| 6 | Inner Product Spaces | 181–226 |
| 7 | Operators on Inner Product Spaces | 227–296 |
| 8 | Operators on Complex Vector Spaces | 297–331 |
| 9 | Multilinear Algebra and Determinants | 332–382 |

Chapter 1 sections and their exercise sets:

| Section | Title | Exercises | Book page | PDF page |
|---|---|---|---|---|
| 1A | 𝐑ⁿ and 𝐂ⁿ | 15 | 10–11 | 24–25 |
| 1B | Definition of Vector Space | 8 | 16–17 | 30–31 |
| 1C | Subspaces | 24 | 24–26 | 38–40 |

## Conventions in this book

- Numbered items (1.1, 1.20, 1.34, …) are a single continuous sequence per
  chapter covering definitions, notation, examples, and results. Always
  cite them by number — Axler cross-references heavily this way.
- 𝐅 denotes either 𝐑 or 𝐂 (1.6). 𝑉 denotes a vector space over 𝐅 (1.29).
- 𝑛 is a fixed positive integer for the whole of chapter 1 (1.10).
