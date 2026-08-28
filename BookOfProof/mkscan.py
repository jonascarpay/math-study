#!/usr/bin/env python3
"""Build BookOfProof.txt (the readable scan) from BookOfProof.pdf.

`pdftotext` alone is not usable for this book: none of its fonts carry a
ToUnicode map, so every glyph from the Fourier math fonts arrives as an
unrelated Latin-1 character ({ } | ( ) as © ª ¯ ¡ ¢, and so on), and
sub/superscripts collapse into the baseline, silently turning F_{n+1}^2
into the plausible-but-wrong "F n2+1".

`pdftohtml -xml` exposes, per span, the font family and the position/size.
That is enough to resolve both problems exactly:

  * which font a glyph came from tells us what it really is, so the
    ambiguous cases (";" = empty set vs. semicolon, "p" = radical vs. the
    letter p, "!" = big paren vs. factorial, "0" = prime) are decided by
    provenance rather than by guesswork;
  * height and vertical offset relative to the row baseline tell us
    whether a span is a superscript or a subscript.

Layout is reconstructed on a character grid from the x coordinates, which
keeps the book's two- and four-column exercise blocks and its truth tables
aligned.

Usage: python3 mkscan.py BookOfProof.pdf BookOfProof.txt
"""

import re
import subprocess
import sys
from xml.etree import ElementTree as ET

# ---------------------------------------------------------------------------
# Glyph tables.
#
# Every entry below was confirmed against its surrounding context in the
# book; see BookOfProof/CLAUDE.md for the audit.  Characters not listed pass
# through unchanged, which is correct for the text fonts and for the math
# operators that poppler already decodes properly (∈ ∪ ∩ ⊆ ∀ ∃ ⇒ ≤ …).
# ---------------------------------------------------------------------------

# Scaled delimiters and big operators.  The same logical bracket appears at
# several optical sizes, each landing on a different byte.
EXTENSION = {
    "©": "{", "ª": "}",     # most common brace pair
    "½": "{", "¾": "}",     # brace, larger
    "n": "{", "o": "}",     # brace, larger still
    "¡": "(", "¢": ")",
    "³": "(", "´": ")",
    "µ": "(", "¶": ")",
    "Ã": "(", "!": ")",     # the tall parens of a binomial coefficient
    "£": "[", "¤": "]",
    '"': "[", "#": "]",
    "¯": "|",
    "P": "∑", "X": "∑",     # summation, two sizes
    "[": "⋃", "S": "⋃",     # big union, two sizes
    "\\": "⋂",              # big intersection
}

# Operators and relations.
SYMBOLS = {
    ";": "∅",
    "p": "√",
    "0": "′",
    "b": "⌊", "c": "⌋",
    "d": "⌈", "e": "⌉",
    "m": "⇕",
}

LETTERS = {
    "`": "ℓ",
    "²": "ε",   # varepsilon; the book also uses ε from the same font
}

SCRIPT = {"P": "𝒫", "F": "ℱ"}   # rsfs10: calligraphic
MSAM = {"X": "✓"}
MSBM = {"-": "∤"}

# "6" from the symbol font is a negation slash drawn over the next glyph.
NEGATED = {
    "=": "≠", "⊆": "⊈", "≡": "≢", "<": "≮", "∈": "∉", ">": "≯", "⊂": "⊄",
}

FAMILY_MAP = {
    "Fourier-Math-Extension": EXTENSION,
    "Fourier-Math-Symbols": SYMBOLS,
    "Fourier-Math-Letters": LETTERS,
    "Fourier-Math-Letters-Italic": LETTERS,
    "rsfs10": SCRIPT,
    "MSAM10": MSAM,
    "MSBM10": MSBM,
}

# Pieces of multi-line braces, radicals and under/overbraces.  These only
# mean anything as part of a two-dimensional shape, so rendering them inline
# produces noise; drop them and let the surrounding text carry the sense.
DROP = {
    ("Fourier-Math-Extension", c)
    for c in "|{}z\\"
} - {("Fourier-Math-Extension", "\\")}  # keep \ : it is ⋂, not a brace piece

COL_WIDTH = 7.5     # px per character column, from measured body-text advance
ROW_TOL = 9         # baseline spread that still counts as one row
ATTACH_TOL = 16     # how far a script may sit from its base row's baseline

# The XML's `height` attribute is the glyph bounding box, so it shrinks on
# text that happens to lack ascenders or descenders -- it cannot be used to
# tell a superscript from ordinary prose.  The fontspec `size` can.  Base
# size differs by section (16 through the main body, 15 in the Solutions
# chapter), so it is measured per page and scripts are taken to be anything
# set below SCRIPT_RATIO of it.
SCRIPT_RATIO = 0.8
ASCENT = 0.78       # baseline ~= top + ASCENT * size
FRACTION_X = 4      # left-edge offset above which a stack reads as a fraction


def load_pages(pdf):
    # -i suppresses image extraction; without it pdftohtml litters the
    # working directory with a PNG per figure.
    xml = subprocess.run(
        ["pdftohtml", "-xml", "-i", "-stdout", pdf],
        capture_output=True, check=True,
    ).stdout
    root = ET.fromstring(xml)
    fonts = {}
    for page in root.iter("page"):
        for f in page.findall("fontspec"):
            fonts[f.get("id")] = (
                f.get("family", "").split("+")[-1],
                int(f.get("size")),
            )
        spans = []
        for t in page.iter("text"):
            text = "".join(t.itertext())
            if not text.strip():
                continue
            fam, size = fonts.get(t.get("font"), ("", 0))
            spans.append({
                "fam": fam,
                "size": size,
                "text": text,
                "top": int(t.get("top")),
                "left": int(t.get("left")),
                "w": int(t.get("width")),
                "bl": int(t.get("top")) + ASCENT * size,
            })
        yield page.get("number"), spans


def translate(span):
    """Map a span's characters through its font's table."""
    table = FAMILY_MAP.get(span["fam"])
    out = []
    for ch in span["text"]:
        if (span["fam"], ch) in DROP:
            continue
        out.append(table.get(ch, ch) if table else ch)
    return "".join(out)


def group_rows(spans):
    """Cluster spans into rows, tagging each as base, superscript or subscript."""
    # Base size for this page: the size carrying the most text, among the
    # sizes big enough to be body copy rather than furniture.
    weight = {}
    for s in spans:
        weight[s["size"]] = weight.get(s["size"], 0) + len(s["text"])
    big = [sz for sz in weight if sz >= 13]
    base_size = max(big, key=lambda sz: weight[sz]) if big else 0

    # TeX sets scripts at 0.7x their base, so the gap between base text and a
    # script is wide.  A page mixes several base sizes, though (16pt prose
    # around 14pt exercise math), and a fixed drop would misread the smallest
    # of those as a script -- which turned the perfectly ordinary "{π,e,0}"
    # into "{^π,e,0}".  Scaling the threshold keeps every base size on the
    # baseline while still catching real scripts at 10-12pt.
    script_max = SCRIPT_RATIO * base_size

    base = [s for s in spans if s["size"] > script_max]
    small = [s for s in spans if s["size"] <= script_max]

    # Rows are seeded from full-size text, clustered on baseline.  Poppler
    # reports a glyph bounding box, so `top` for italic or accented spans can
    # sit several px above roman text on the very same line; the tolerance
    # has to absorb that without swallowing the next line, which may be only
    # ~14px away.  Compare against the running mean rather than the previous
    # member so a chain of near-misses cannot drift across a line boundary.
    rows = []
    for b in sorted(s["bl"] for s in base):
        if rows and b - (sum(rows[-1]) / len(rows[-1])) <= ROW_TOL:
            rows[-1].append(b)
        else:
            rows.append([b])
    baselines = [sum(r) / len(r) for r in rows]

    buckets = {b: [] for b in baselines}
    for s in base:
        b = min(baselines, key=lambda x: abs(x - s["bl"]))
        buckets[b].append((s, "base"))

    # A radical sign is drawn tall enough to cover its radicand, so its own
    # baseline points at the row above and would strand it there ("a root
    # of_√" on one line, "x^2−x−1" on the next).  Defer these and place each
    # one against the glyph it actually sits in front of.
    radicals = [s for s in small if translate(s) == "√"]
    small = [s for s in small if translate(s) != "√"]

    for s in small:
        if baselines:
            b = min(baselines, key=lambda x: abs(x - s["bl"]))
            if abs(b - s["bl"]) <= ATTACH_TOL:
                buckets[b].append((s, "sup" if s["bl"] < b else "sub"))
                continue
        # Nothing to attach to: the span stands as its own line.  This is
        # what keeps page furniture, and the two halves of a display
        # fraction, from being glued onto unrelated text.
        buckets.setdefault(s["bl"], []).append((s, "base"))

    for s in radicals:
        best, best_key = None, None
        for b, items in buckets.items():
            for other, kind in items:
                dx = other["left"] - s["left"]
                dy = abs(other["bl"] - s["bl"])
                if 0 <= dx <= 40 and dy <= 30:
                    key = (dx, dy)
                    if best_key is None or key < best_key:
                        best, best_key = (b, kind), key
        if best:
            buckets[best[0]].append((s, best[1]))
        else:
            buckets.setdefault(s["bl"], []).append((s, "base"))

    for b in sorted(buckets):
        items = sorted(buckets[b], key=lambda it: it[0]["left"])
        if items:
            yield items


def _brace(text):
    return text if len(text) == 1 else "{%s}" % text


def _paren(text):
    if len(text) == 1 or (text.startswith("(") and text.endswith(")")):
        return text
    return "(%s)" % text


def render_row(items):
    """Emit one row, resolving script runs into _{} / ^{} or into a fraction."""
    toks = []           # (left_px, right_px, text)
    i = 0
    while i < len(items):
        span, kind = items[i]
        if kind == "base":
            text = translate(span)
            # A delimiter taller than one glyph is drawn as several identical
            # pieces stacked at the same x, which would otherwise come out as
            # "||S^7||" instead of "|S^7|".  The pieces are not always spans
            # of their own -- the first is often bundled onto the end of the
            # preceding one ("}|" then "|") -- so match on the trailing
            # character and on the two spans overlapping horizontally.
            if (toks and len(text) == 1 and toks[-1][2].endswith(text)
                    and span["left"] < toks[-1][1]):
                i += 1
                continue
            toks.append((span["left"], span["left"] + span["w"], text))
            i += 1
            continue

        # A run of consecutive script spans attaches to whatever precedes it.
        run = []
        while i < len(items) and items[i][1] != "base":
            run.append(items[i])
            i += 1
        sup = [s for s, k in run if k == "sup"]
        sub = [s for s, k in run if k == "sub"]
        up = "".join(translate(s) for s in sup).strip()
        down = "".join(translate(s) for s in sub).strip()
        left = min(s["left"] for s, _ in run)
        right = max(s["left"] + s["w"] for s, _ in run)

        # An inline fraction is typeset at script size too, so it arrives here
        # looking like a superscript stacked over a subscript.  The two are
        # told apart by alignment: a real x^a_b hangs both scripts off the
        # same left edge, whereas a fraction centres numerator over
        # denominator, leaving their left edges several px apart.
        if up and down and abs(min(s["left"] for s in sup)
                               - min(s["left"] for s in sub)) > FRACTION_X:
            frag = "%s/%s" % (_paren(up), _paren(down))
        else:
            frag = ""
            if down:
                frag += "_" + _brace(down)
            if up:
                frag += "^" + _brace(up)
        if frag:
            toks.append((left, right, frag))

    # Lay out on a character grid.  Spacing follows the real pixel gap rather
    # than each token's absolute column, which keeps tight math as "(−1)^n"
    # instead of "( − 1) ^n" while still preserving the wide gaps that carry
    # the book's multi-column exercise blocks and truth tables.
    line = ""
    pen = None
    for left, right, text in toks:
        if pen is None:
            line = " " * int(round(left / COL_WIDTH))
        else:
            gap = left - pen
            if gap > 0.45 * COL_WIDTH:
                line += " " * max(1, int(round(gap / COL_WIDTH)))
        line += text
        pen = right
    return line.rstrip()


# A binomial coefficient is a tall paren wrapping a bare superscript over a
# bare subscript, with nothing on the baseline between them -- a shape that
# nothing else in the book produces.  Spelling it out beats leaving the
# reader to decode "(_k^n)".
BINOMIAL = re.compile(r"\(_(\{[^{}]*\}|[^{}\s()])\^(\{[^{}]*\}|[^{}\s()])\)")


def apply_binomials(text):
    def sub(m):
        low, high = (g[1:-1] if g.startswith("{") else g for g in m.groups())
        return "binom(%s,%s)" % (high, low)
    return BINOMIAL.sub(sub, text)


def apply_negations(text):
    out = []
    i = 0
    while i < len(text):
        if text[i] == "\x00":           # negation marker
            # The slash and the glyph it negates are separate spans, so
            # layout may have put a gap between them.
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            nxt = text[j] if j < len(text) else ""
            if nxt in NEGATED:
                out.append(NEGATED[nxt])
                i = j + 1
                continue
            if nxt and nxt != "\n":
                out.append(nxt + "̸")
                i = j + 1
                continue
            out.append("̸")
            i += 1
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def main():
    pdf, dest = sys.argv[1], sys.argv[2]
    pages = []
    for _number, spans in load_pages(pdf):
        for s in spans:
            # Mark the negation slash before translation so it survives as a
            # distinct token, then resolve it against its neighbour below.
            if s["fam"] == "Fourier-Math-Symbols":
                s["text"] = s["text"].replace("6", "\x00")
        lines = [render_row(items) for items in group_rows(spans)]
        pages.append(apply_binomials(apply_negations("\n".join(lines))))
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\f".join(pages))


if __name__ == "__main__":
    main()
