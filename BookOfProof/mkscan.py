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

Neither tool sees horizontal rules, though, and this book draws two things
with them: the bar of a set complement and the vinculum of a radical.  Both
therefore vanish without trace -- `A=U −A` for Definition 1.6's `A̅ = U − A`,
and no record of how far a root extends.  `pdftocairo -svg` does emit them,
as stroked one-segment paths, so a second pass over the SVG recovers the
bars and matches each to the glyphs sitting underneath it.

Layout is reconstructed on a character grid from the x coordinates, which
keeps the book's two- and four-column exercise blocks and its truth tables
aligned.

Usage: python3 mkscan.py BookOfProof.pdf BookOfProof.txt
"""

import re
import subprocess
import sys
import unicodedata
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
    # Radical signs at two more optical sizes; the smallest is Symbols' "p".
    # Every occurrence of these two was checked to have a vinculum starting
    # flush against its right edge, which no brace piece does.
    "p": "√", "q": "√",
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

# Rule geometry, in XML pixels.  A complement bar covers between one glyph
# and a short parenthesised expression, so anything longer is furniture: the
# frame around an Exercises block, a number line, a figure axis.  BAR_DROP is
# how far above the glyph tops a bar may sit and still belong to them.
BAR_MIN, BAR_MAX = 3, 250
BAR_DROP = 0.75     # as a fraction of the covered glyph's font size
BAR_KERN = 10       # widest gap between glyphs a single bar may span
BAR_PAD = 0.45      # how far a bar may overhang its glyphs, per font size
SURD_GAP = 3        # a vinculum starts this close to its radical sign

# What a complement may be drawn over.  Geometry alone cannot separate a
# complement bar from a fraction bar -- both are a rule with glyphs beneath
# it, and measuring against the material above fails because the line above
# an overline can sit as close as a numerator does (Exercises 1.7 has the
# bar of one line clearing the previous line's letters by 2px).  What does
# separate them is what they cover: this book complements sets, and sets are
# named with capitals, while every fraction bar found in the text covers
# lowercase names, bare arithmetic, or |…|.  Bars over anything else are
# left alone; there are none in the book.
BAR_OVER = re.compile(r"^[A-Z0-9∩∪−×,()∅_^{}.·\s]*[A-Z∅][A-Z0-9∩∪−×,()∅_^{}.·\s]*$")

OVERLINE = "\x01", "\x02"       # markers for a complement bar
VINCULUM = "\x03", "\x04"       # markers for the bar of a radical


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
                "h": int(t.get("height")),
                "bl": int(t.get("top")) + ASCENT * size,
            })
        yield int(page.get("number")), int(page.get("width")), spans


def load_rules(pdf, number, page_width):
    """The rules drawn on one page, in the XML's pixel coordinates.

    Returns the horizontal ones as (y, x0, x1) and the vertical ones as
    (x, y0, y1); the verticals are only wanted so that a bar can be told
    from the top edge of a box.

    pdftocairo writes SVG one page at a time, which costs a subprocess per
    page but keeps rules keyed to the page they were drawn on.  Its units are
    PDF points, so everything is scaled onto the XML's grid before returning.
    """
    svg = subprocess.run(
        ["pdftocairo", "-svg", "-f", str(number), "-l", str(number), pdf, "-"],
        capture_output=True, check=True,
    ).stdout.decode("utf-8", "replace")
    box = re.search(r'viewBox="0 0 ([\d.]+) ', svg)
    scale = page_width / float(box.group(1))

    # Glyph outlines live in <defs> and are drawn by reference; a page with
    # no text (a chapter opener carrying only a rule) has no <defs> at all.
    body = svg.rsplit("</defs>", 1)[-1]

    rules, posts = [], []
    for m in re.finditer(r"<path([^>]*)/>", body):
        attrs = m.group(1)
        # Glyph outlines are filled, not stroked; rules are the reverse.
        if "stroke-width" not in attrs or "fill-rule" in attrs:
            continue
        points = re.findall(r"([-\d.]+)\s+([-\d.]+)",
                            re.search(r'\bd="([^"]*)"', attrs).group(1))
        if len(points) != 2:            # not a single straight segment
            continue
        (x1, y1), (x2, y2) = [(float(p), float(q)) for p, q in points]
        tr = re.search(r'transform="matrix\(([^)]*)\)"', attrs)
        if tr:
            a, b, c, d, e, f = [float(v) for v in tr.group(1).split(",")]
            x1, y1, x2, y2 = (a * x1 + c * y1 + e, b * x1 + d * y1 + f,
                              a * x2 + c * y2 + e, b * x2 + d * y2 + f)
        if abs(x1 - x2) <= 0.05:        # vertical: the side of a box
            lo, hi = sorted((y1 * scale, y2 * scale))
            posts.append((x1 * scale, lo, hi))
        elif abs(y1 - y2) <= 0.05:
            lo, hi = sorted((x1 * scale, x2 * scale))
            if BAR_MIN <= hi - lo <= BAR_MAX:
                rules.append((y1 * scale, lo, hi))
    return rules, posts


def base_size(spans):
    """The font size carrying the most text, among sizes big enough to be
    body copy rather than furniture.  Scripts are set below SCRIPT_RATIO of
    it; see `group_rows`."""
    weight = {}
    for s in spans:
        weight[s["size"]] = weight.get(s["size"], 0) + len(s["text"])
    big = [sz for sz in weight if sz >= 13]
    return max(big, key=lambda sz: weight[sz]) if big else 0


def _bare(span):
    """A span's text, translated, with any bar markers removed."""
    return "".join(c for c in translate(span) if c not in MARKERS)


def _post_at(posts, x, y):
    """Is a vertical rule hanging from (x, y)?"""
    return any(abs(px - x) <= 3 and py0 - 2 <= y <= py1 for px, py0, py1 in posts)


def mark_bars(spans, rules, posts):
    """Wrap each rule's glyphs in markers, in place.

    A rule is a complement bar over whatever sits directly beneath it, but
    three other things in this book are also drawn as a rule with text below:

      * a fraction bar, which is told apart by what it covers -- see
        BAR_OVER, and note that a size test will not do, because a display
        \\frac sets both halves at full size;
      * a frame: the rules of a truth table, the box around an Exercises
        block, the border of the playing cards in Chapter 3.  These are
        drawn to a layout rather than to their contents, so they overhang
        the glyphs beneath them and span gaps wider than any kerning;
      * a radical's vinculum, which begins flush against the right edge of
        its surd -- and that is worth keeping, since it is the only record
        of how far the root extends.

    Shortest first, so that a bar drawn over an already-barred expression
    (Exercises 1.6 has several) nests outside the one it contains.
    """
    for y, x0, x1 in sorted(rules, key=lambda r: r[2] - r[1]):
        under = sorted(
            (s for s in spans
             if x0 - 1 <= s["left"] + s["w"] / 2 <= x1 + 1
             and 0 <= s["top"] - y <= BAR_DROP * s["size"]),
            key=lambda s: s["left"])
        if not under:
            continue
        if any(b["left"] - (a["left"] + a["w"]) > BAR_KERN
               for a, b in zip(under, under[1:])):
            continue                    # column gaps: this is a frame
        if (under[0]["left"] - x0 > BAR_PAD * under[0]["size"]
                or x1 - (under[-1]["left"] + under[-1]["w"])
                > BAR_PAD * under[-1]["size"]):
            continue                    # overhangs its contents: also a frame
        if (_post_at(posts, x0, y) and _post_at(posts, x1, y)):
            continue                    # has sides: a box, as around the
            # "ABC" that Solutions 3.4.9 asks you to read as one symbol

        surd = any(_bare(s) == "√"
                   and abs(x0 - (s["left"] + s["w"])) <= SURD_GAP
                   for s in spans)
        # Judge the name being complemented, not its subscript: A_n is a set,
        # and the "n" arrives as a separate script-size span.  Markers left by
        # an inner bar are stripped first -- Exercises 1.6.1(i) draws a bar
        # over the whole of A̅ ∩ B, and matching them would reject it.
        script_max = SCRIPT_RATIO * base_size(spans)
        name = "".join(_bare(s) for s in under if s["size"] > script_max)
        if not surd and not BAR_OVER.match(name):
            continue                    # not a set: this is a fraction bar
        if surd and len(under) == 1:
            # The radicand is a single span, so the bar tells us nothing that
            # "√" placed in front of it does not already say -- and poppler
            # bundles trailing punctuation into that span ("2," in Example
            # 1.1), which parenthesising would wrongly swallow.
            continue
        start, end = VINCULUM if surd else OVERLINE
        under[0]["text"] = start + under[0]["text"]
        under[-1]["text"] = under[-1]["text"] + end


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
    # TeX sets scripts at 0.7x their base, so the gap between base text and a
    # script is wide.  A page mixes several base sizes, though (16pt prose
    # around 14pt exercise math), and a fixed drop would misread the smallest
    # of those as a script -- which turned the perfectly ordinary "{π,e,0}"
    # into "{^π,e,0}".  Scaling the threshold keeps every base size on the
    # baseline while still catching real scripts at 10-12pt.
    script_max = SCRIPT_RATIO * base_size(spans)

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


MARKERS = OVERLINE + VINCULUM


def _outside(wrap, text):
    """Apply `wrap` to `text`, leaving any bar markers on its ends outside.

    A bar over A_n puts its closing marker on the subscript, and bracing that
    subscript with the marker still inside would emit "‾(A_{n)}" -- brace and
    bar interleaved rather than nested."""
    i, j = 0, len(text)
    while i < j and text[i] in MARKERS:
        i += 1
    while j > i and text[j - 1] in MARKERS:
        j -= 1
    return text[:i] + wrap(text[i:j]) + text[j:]


def _brace(text):
    return _outside(lambda t: t if len(t) == 1 else "{%s}" % t, text)


def _paren(text):
    def wrap(t):
        if len(t) == 1 or (t.startswith("(") and t.endswith(")")):
            return t
        return "(%s)" % t
    return _outside(wrap, text)


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


# Innermost pair first, so a nested bar resolves before the one that
# encloses it.  Anything still marked afterwards had one end fall on a glyph
# that was dropped, so the leftovers are swept up rather than printed.
BAR = re.compile("[%s%s]([^%s%s%s%s]*)[%s%s]"
                 % (OVERLINE[0], VINCULUM[0],
                    OVERLINE[0], OVERLINE[1], VINCULUM[0], VINCULUM[1],
                    OVERLINE[1], VINCULUM[1]))


def _visible(text):
    return sum(1 for c in text if not unicodedata.combining(c))


def apply_bars(text):
    def sub(m):
        inner = m.group(1)
        if m.group(0)[0] == VINCULUM[0]:        # extent of a radical sign
            return inner if _visible(inner) == 1 else "(%s)" % inner
        if _visible(inner) == 1:
            return inner + "̅"             # combining overline
        return "‾(%s)" % inner
    while True:
        text, n = BAR.subn(sub, text)
        if not n:
            return text.translate({ord(c): None
                                   for c in OVERLINE + VINCULUM})


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
    for number, width, spans in load_pages(pdf):
        for s in spans:
            # Mark the negation slash before translation so it survives as a
            # distinct token, then resolve it against its neighbour below.
            if s["fam"] == "Fourier-Math-Symbols":
                s["text"] = s["text"].replace("6", "\x00")
        mark_bars(spans, *load_rules(pdf, number, width))
        lines = [render_row(items) for items in group_rows(spans)]
        pages.append(apply_binomials(apply_bars(
            apply_negations("\n".join(lines)))))
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\f".join(pages))


if __name__ == "__main__":
    main()
