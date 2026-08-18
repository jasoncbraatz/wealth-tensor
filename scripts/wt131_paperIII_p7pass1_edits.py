#!/usr/bin/env python3
"""wt131 -- Paper III, FIRST independent P7 read (wealthTensor-73).  Six repairs.

Shape: wt128's census-and-rewrap, wt129's GUARD HONESTY (WT-118) -- every invariant is
asserted against the ORIGINAL text before it is asserted against the patched text, so a
red guard says which of the two failure modes fired instead of leaving the reviewer to
guess.  Run from the repository root.

THE FINDINGS, all six from the wt130 quantifier sweep read FORWARD (WT-115/WT-117):

  III-1  SS2's terminology note: "The word **crisis** is kept in the title".  The title is
         "Timeliness and durability are not separately identified from a reported series"
         and carries no such word.  paper-III.md.bak-pre-roadtwo dates the retitling: the
         old title opened "A crisis is deferred information arriving at once".  SS8.2 --
         written after -- says the crisis framing belongs to a later paper and is "not
         defended here".  The note was written against the old title and survived it.

  III-2  SSA.1.3: "the regimes in which EACH PROPOSITION fails are committed, tested code".
         Two bullets follow.  One is P2.  The other is the phi = 1 switch-off, which the
         bullet itself calls "a separate and equally important point" -- it is not a
         proposition.  P1 and P3 get nothing.  A universal carved out by its own list,
         four lines below it (WT-117).

  III-3  SS11 says "SSA.2 and SS2" four times and labels wt027_report.py "Regenerate SS2".
         SS2 contains no simulation result: it is the model statement.  wt027_report.py's
         three tables are SS3.1's two and SS3.2's one.  SS6.1, in the same manuscript,
         writes the same scope correctly TWICE as "SSA.2 and SSSS2-3".  This is II-19's
         species -- a command named for numbers it does not produce -- with the paper's
         own correct wording available 500 lines upstream.

  III-4  SS7's survivals row is titled "The rectangle's 99.7%" and its own outcome cell
         reports 0.998, as does SS4.4 (99.8%).  99.7% is REG-002 E4's figure at alpha =
         0.35 (RESULT-REG-002 SS4); 0.998 is the figure at the measured alpha-hat = 0.408,
         which is what the row's design column says it ran.  The row title imports a
         number from a different recognition rate and the manuscript carries 99.7%
         nowhere else, so a reader cannot reconcile the title with the row.

  III-5  The Bleck and Liu entry: "SS4.4 and SS10 both cite it ... it states SS4.4's
         volatility result".  It is cited in SS3.2, SS8.2 and SS10.  SS8.2 says so in
         terms -- "retained in SSSS3.2 and 10".  SS4.4 does not mention it.

  III-6  The Jin and Myers entry names "SS10's ONE quotation" and gives a sentence that
         appears nowhere in the manuscript, while SS10 carries five quoted fragments from
         them.  The entry then states the rule the manuscript is breaking: "a reader
         entitled to doubt that on a paraphrase should be able to see the words" -- and
         SS10 now supplies exactly the paraphrase.  Repaired by RESTORING the words to
         SS10, which is the smaller change and the one the entry's own rule asks for.
         The References' fourth-pass note is repaired by APPEND, not rewrite: it is a
         dated record of what that pass found, and what it found was later discharged.

WHAT THIS SCRIPT DOES NOT TOUCH.  The abstract (asserted byte-identical below).  The
title.  RESULT-REG-002's 99.7%, which is correct at its own alpha and is a dated result
of record.  wt097 and wt099, which RAN.  The manuscript's 644/281 disclosure denominators
(REG-007 constants, checked and correct).  The "291-fold" (0.21140/0.00073 prints as 289
only because NOTE-001 rounds the denominator; the underlying pair gives 291).
"""
from __future__ import annotations

import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPER = ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"
TEST = ROOT / "tests" / "test_ledger_provenance.py"
TAG = "wt131"

FAIL: list[str] = []


def guard(name: str, ok_original: bool, ok_patched: bool) -> None:
    """WT-118.  Assert every invariant against the ORIGINAL as well as the patch, so the
    error message distinguishes 'the edit broke it' from 'it was never true'."""
    if not ok_original:
        FAIL.append(f"GUARD VACUOUS -- {name}: FALSE OF THE ORIGINAL TOO. The guard is "
                    f"wrong, not the edit. Fix the guard before reading the edit.")
    elif not ok_patched:
        FAIL.append(f"GUARD RED -- {name}: true of the original, false after the patch. "
                    f"The EDIT broke it.")


# (file, old, new, label) -- every `old` must occur EXACTLY once (census, WT-099).
EDITS = [
    # ---- III-1 ---------------------------------------------------------------------
    (PAPER,
     "The word **crisis** is kept\n"
     "in the title and for the phenomenon the paper is *about*; the systemic, country-level sense used in\n"
     "the banking-crisis literature is not intended anywhere here.",
     "The word **crisis** is used\n"
     "for the phenomenon §2 models and for nothing wider. It is **not** in the title, which names the\n"
     "identification result; §8.2 gives the framing it belongs to and the paper that will carry it. The\n"
     "systemic, country-level sense used in the banking-crisis literature is not intended anywhere here.",
     "III-1 §2 crisis-in-the-title"),

    # ---- III-2 ---------------------------------------------------------------------
    (PAPER,
     "by assertion. Here it is demonstrated, because the regimes in which each proposition fails are\n"
     "committed, tested code rather than thought experiments:",
     "by assertion. Here it is demonstrated for **one** of the three, because the regime in which P2\n"
     "fails is committed, tested code rather than a thought experiment. P1 and P3 are argued deniable\n"
     "in §A.1.1 and §A.1.4 and are not demonstrated in code, and the second item below is the\n"
     "mechanism's own switch-off rather than a proposition:",
     "III-2 §A.1.3 each-proposition"),

    # ---- III-3 ---------------------------------------------------------------------
    (PAPER,
     "Every simulation result in §A.2 and §2 is produced by open code.",
     "Every simulation result in §A.2 and §§2–3 is produced by open code.",
     "III-3a §11 scope line"),
    (PAPER,
     "- **Regenerate §2 (and §A.2.4):** `python3 scripts/wt027_report.py`",
     "- **Regenerate §3 (and §A.2.4):** `python3 scripts/wt027_report.py` — its three tables are\n"
     "  §3.1's two and §3.2's. §2 states the model and reports no simulation result.",
     "III-3b §11 regenerate label"),
    (PAPER,
     "the state that produced every result in §A.2 and §2 —",
     "the state that produced every result in §A.2 and §§2–3 —",
     "III-3c §11 pinned-commit scope"),
    (PAPER,
     "Every figure in §A.2 and §2 regenerates on a commodity CPU in seconds.",
     "Every figure in §A.2 and §§2–3 regenerates on a commodity CPU in seconds.",
     "III-3d §11 hardware scope"),

    # ---- III-4 ---------------------------------------------------------------------
    (PAPER,
     "| **The rectangle's 99.7% is a property of the assumed support",
     "| **The rectangle's 99.8% is a property of the assumed support",
     "III-4 §7 ledger row title"),
    (TEST,
     '"99.7% is a property of the assumed support"',
     '"99.8% is a property of the assumed support"',
     "III-4 test row key (5 sites)"),

    # ---- III-5 ---------------------------------------------------------------------
    (PAPER,
     "§4.4 and §10 both cite it against this paper: it states §4.4's\n"
     "volatility result nineteen years earlier.)*",
     "§3.2 and §10 both cite it against this paper: it states §3.2's\n"
     "volatility result nineteen years earlier.)*",
     "III-5 Bleck and Liu cited-in"),

    # ---- III-6 ---------------------------------------------------------------------
    (PAPER,
     "cost*. The operating asset neither depreciates nor is reinvested in by declared assumption, and the\n",
     "cost*. The operating asset neither depreciates nor is reinvested in — \"For simplicity, we ignore\n"
     "depreciation and reinvestment\" — by declared assumption, and the\n",
     "III-6a §10 restore the quoted words"),
    (PAPER,
     "typeset article. §10's one quotation —",
     "typeset article. The sentence §10 quotes for the no-physical-layer reading —",
     "III-6b Jin and Myers one-quotation"),
    (PAPER,
     "   §10 being attributed to the working paper it was actually read in rather than to the journal.\n",
     "   §10 being attributed to the working paper it was actually read in rather than to the journal.\n"
     "   **That finding was later discharged for the crash-risk entries, and is recorded here rather than\n"
     "   rewritten:** Jin and Myers was afterwards read in the typeset article and its quoted sentence\n"
     "   verified at p. 262 unchanged, so those entries carry **✓**. **✓⧗** now marks three entries,\n"
     "   cited in §§4.4, 4.6 and 4.9.\n",
     "III-6c References pass-4 append"),

    # ---- III-7 (the smallest one, and the same species) ------------------------------
    (PAPER,
     "**exactly one clears §5's floor of 30**",
     "**exactly one clears the registered floor of 30**",
     "III-7 §4.7 floor attribution"),
]


def section(text: str, head_prefix: str) -> str:
    """Body of the first level-2/3 heading starting with `head_prefix`, to its next
    heading of the same or higher level."""
    lines = text.split("\n")
    start = lvl = None
    for i, l in enumerate(lines):
        if l.startswith(head_prefix):
            start, lvl = i, len(l) - len(l.lstrip("#"))
            break
    if start is None:
        return ""
    for j in range(start + 1, len(lines)):
        l = lines[j]
        if l.startswith("#") and (len(l) - len(l.lstrip("#"))) <= lvl:
            return "\n".join(lines[start:j])
    return "\n".join(lines[start:])


def main() -> int:
    originals = {p: p.read_text(encoding="utf-8") for p in {e[0] for e in EDITS}}
    for p in originals:
        if not p.exists():
            print(f"MISSING: {p}", file=sys.stderr)
            return 2

    # ---- CENSUS FIRST (WT-099) ------------------------------------------------------
    print("CENSUS -- every anchor, counted before anything is written")
    census_ok = True
    for path, old, _new, label in EDITS:
        n = originals[path].count(old)
        expected = 5 if label.startswith("III-4 test") else 1
        mark = "ok " if n == expected else "!! "
        if n != expected:
            census_ok = False
        print(f"  {mark}{n:>2} (want {expected})  {label}")
    if not census_ok:
        print("\nCENSUS FAILED -- an anchor is missing or ambiguous. Nothing written.",
              file=sys.stderr)
        return 3

    # ---- the invariants, stated once and checked TWICE (WT-118) ---------------------
    def abstract(t: str) -> str:
        return section(t, "## Abstract")

    def title(t: str) -> str:
        return t.split("\n", 1)[0]

    def bullets_A13(t: str) -> int:
        return section(t, "### A.1.3").count("\n- **")

    def p1h(t: str) -> bool:
        s = section(t, "## 11 · Data and code availability")
        return all(k in s for k in ("github.com/jasoncbraatz/wealth-tensor",
                                    "src/wealth_tensor/", "python3 scripts/", "pytest"))

    def ledger_row(t: str) -> str:
        for l in t.split("\n"):
            if "is a property of the assumed support" in l:
                return l
        return ""

    def p1g(t: str) -> bool:
        return "severe test failed and this paper does not know why" in t

    def jm_quote(t: str) -> int:
        return t.count("For simplicity, we ignore\ndepreciation and reinvestment") + \
               t.count("For simplicity, we ignore depreciation and reinvestment")

    # ---- WRITE ----------------------------------------------------------------------
    patched: dict[pathlib.Path, str] = dict(originals)
    for path, old, new, label in EDITS:
        patched[path] = patched[path].replace(old, new)

    for path, text in patched.items():
        bak = path.with_suffix(path.suffix + f".bak-{TAG}")
        shutil.copy2(path, bak)
        path.write_text(text, encoding="utf-8")
        print(f"\nwrote {path.relative_to(ROOT)}  (backup {bak.name})")

    o, n = originals[PAPER], patched[PAPER]
    ot, nt = originals[TEST], patched[TEST]

    guard("title byte-identical", title(o) == title(o), title(n) == title(o))
    guard("abstract byte-identical", abstract(o) != "", abstract(n) == abstract(o))
    guard("P1g limitation-1 phrase survives", p1g(o), p1g(n))
    guard("P1h data-and-code keys survive", p1h(o), p1h(n))
    guard("§A.1.3 still carries exactly two bullets",
          bullets_A13(o) == 2, bullets_A13(n) == 2)
    guard("§2 no longer claims 'crisis' is in the title",
          "The word **crisis** is kept\nin the title" in o,
          "is kept\nin the title" not in n and "crisis" in n)
    guard("§11 no longer scopes results to §2 alone",
          o.count("§A.2 and §2") == 3,
          n.count("§A.2 and §2 ") == 0 and n.count("§A.2 and §§2–3") == 5)
    guard("§7 ledger row still carries all five of its own figures",
          all(v in ledger_row(o) for v in ("0.659", "0.621", "0.696", "0.998", "0.139")),
          all(v in ledger_row(n) for v in ("0.659", "0.621", "0.696", "0.998", "0.139")))
    guard("§7 row title now agrees with its own outcome cell",
          "99.7%" in ledger_row(o) and "0.998" in ledger_row(o),
          "99.8%" in ledger_row(n) and "99.7%" not in ledger_row(n))
    guard("the test's row key tracks the row title",
          ot.count('"99.7% is a property of the assumed support"') == 5,
          nt.count('"99.8% is a property of the assumed support"') == 5
          and "99.7% is a property" not in nt)
    guard("Bleck and Liu no longer attributed to §4.4",
          "§4.4 and §10 both cite it" in o,
          "§3.2 and §10 both cite it" in n
          and "§4.4 and §10 both cite it" not in n)
    guard("the Jin and Myers sentence is quoted in the body, not only in the entry",
          jm_quote(o) == 1, jm_quote(n) == 2)
    guard("§4.7 no longer attributes the floor of 30 to §5",
          "§5's floor of 30" in o, "§5's floor of 30" not in n)
    guard("no manuscript section was deleted",
          o.count("\n## ") > 0, n.count("\n## ") == o.count("\n## "))
    guard("REG-007 disclosure denominators untouched",
          "644" in o and "281" in o, "644" in n and "281" in n)

    print("\nGUARDS")
    if FAIL:
        for f in FAIL:
            print("  " + f)
        print("\nwt131 FAILED. Backups are beside each file as *.bak-" + TAG)
        return 1
    print("  all green -- every invariant true of the original AND of the patch")
    print(f"\nwt131 OK. 7 findings, {len(EDITS)} edits, 0 carded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
