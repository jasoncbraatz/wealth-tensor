#!/usr/bin/env python3
"""END-TO-END-001 · E1 FAIL — apply the pre-registered remedy, and nothing beyond it.

The design's E1 table, written before the run, says on FAIL:

  * Paper II §3.2's outward-connecting paragraph is cut back to a claim about observability
    alone, with the "same structure" sentence removed.
  * Paper IV §3's "a chain rather than three analogies" is demoted IN TERMS to "three
    instances of one question, asked at three scales".

Applied here verbatim in scope. NOT applied: the abstract narrowing and the ADR-001 addendum,
which belong to §3's T >= 2 branch and are not this leg's to spend; and the refuted branch's
new §3.x for Paper II, which is a remedy for the outcome that did NOT occur.

Two P7-class repairs ride along (found while running E1, single-paper findable, scoring
nothing): Paper II §3.1's Var[log a] shares its letter with §2.1's wage, and Paper II §7's
regeneration line names one script for numbers that come from two.

Every file gets a .bak-wt56-e1 first (and .bak-* is gitignored by standing rule, so the
reversal path that counts is git, not the backup).

RUN ONCE. Three of the ten anchors are PREFIXES of their own replacements, so `--check` after a
successful application still reports them as present; SENTINEL below is what actually decides
whether the remedy has already landed. Do not read a clean `--check` as "not yet applied".
"""
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent   # repo root; this file lives in scripts/
P2 = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
P4 = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"

EDITS = [
    # ---------------- Paper II §3.2 · the pre-registered cut-back -----------------------
    (P2, """This connects outward, and the connection is why this result belongs to a larger programme:
unrealised appreciation is precisely wealth whose growth the reporting layer has not been asked
to recognise. A levy that cannot see an accrual and a financial statement that does not record a
degradation are the same structure — a measurement layer with a systematically incomplete view —
seen from two sides.""",
     """This is a claim about observability, and it is bounded by that. Unrealised appreciation is wealth
whose growth the assessing layer has not been asked to recognise, and what the ρ axis measures is
how much of a period's gain that layer can see at all.

**A stronger reading is available, was tested, and is withdrawn here.** An earlier version of this
paragraph held that a levy which cannot see an accrual and a financial statement which does not
record a degradation *are the same structure*, seen from two sides. Put to a cross-scale check
against the companion work on the reporting layer, that identification does not hold. The share of
a change a reporting filter fails to recognise is **deferred** — it accumulates and is released
later at a stated rate — while the share of a gain this model's base fails to recognise is **never
assessed at all**. Deferred arrival and non-arrival are different operators, and a shared adjective
between them is not an equation. The check, its thresholds, and the fact that this withdrawal was
written down before the check was run are recorded in `docs/RESULT-END-TO-END-001-E1.md`.""" ),

    # ---------------- Paper II §3.1 · P7: the letter *a* carries two objects --------------
    (P2, """**The two bases do not merely differ in budget. They act on different objects.** Matched at
κ ≈ 0.10, the two levies compress the cross-section unequally — Gini 0.222 against 0.125 — but the
more telling comparison is what each does to the variance of the log multiplier, Var[log *a*]: the
generator of the process rather than its outcome. Unlevied, Var[log *a*] = 0.076542.""",
     """**The two bases do not merely differ in budget. They act on different objects.** Matched at
κ ≈ 0.10, the two levies compress the cross-section unequally — Gini 0.222 against 0.125 — but the
more telling comparison is what each does to the variance of the log multiplier: the generator of
the process rather than its outcome. Write that multiplier, normalised by aggregate growth, as
*a*(η) — a different object from §2.1's wage *a*, with which it unhappily shares a letter — so the
quantity is Var[log *a*]. Unlevied, Var[log *a*] = 0.076542.""" ),

    # ---------------- Paper II §7 · P6/P7: one command named for two sources ---------------
    (P2, """- **Regenerate every number in §3:** `python3 scripts/wt030_report.py`""",
     """- **Regenerate every number in §3:** `python3 scripts/wt030_report.py` — except the three
  Var[log *a*] values in §3.1, which are quadrature over the multiplier's distribution rather than
  simulation output and come from `python3 scripts/wt077_tail_index.py`. The two commands are named
  separately because a single command named for numbers it does not produce is a provenance claim
  that reads as checked and is not.""" ),

    # ---------------- Paper IV §3 · the pre-registered demotion, in terms ------------------
    (P4, """**Note what makes this a chain rather than three analogies.** At each step the same two components
appear, the same question is asked of them""",
     """**Note what this is: three instances of one question, asked at three scales.** At each step the
same two components appear, the same question is asked of them""" ),

    (P4, """is a composition quantity: it is defined at the firm scale and is *written* as diagonal over asset
classes — a form the next paragraph reports as tested and rejected, which changes what the link
carries and not whether there is one.""",
     """is a composition quantity: it is defined at the firm scale and is *written* as diagonal over asset
classes — a form the next paragraph reports as tested and rejected, which changes what the link
carries and not whether there is one.

**An earlier draft of this section claimed more than three instances of one question, and the
corpus's first end-to-end test took the surplus away.** It said the three scales made *a chain
rather than three analogies*. `END-TO-END-001` leg `E1` asked whether the sovereign and firm scales
stand in the relation the word *chain* asserts — whether Paper II's realisation share ρ and Paper
III's observability share φ are the same object seen twice — and they are not. What Paper III's
filter does not recognise is **deferred**, held in an unrecognised gap and released at rate α;
what Paper II's base does not recognise is **never assessed**. A lag and a loss are different
operators, and Paper II has no parameter that plays α's part. So what joins the scales is the
question and the fact that each scale answers it quantitatively, which is what this section now
claims and no more. The demotion was written into that document's §2 **before** the leg was run,
precisely so that it could not be renegotiated afterwards; `docs/RESULT-END-TO-END-001-E1.md`
records the run and the reasoning.""" ),

    # -------- Paper IV · four downstream uses of "chain" that the demotion strands ---------
    (P4, """And **the place where the chain could break was named, was tested, and the test rejected it.**""",
     """And **the place where the firm-scale link could break was named, was tested, and the test rejected
it.**""" ),
    (P4, """§2.2 whatever the recording practice does. The chain's firm-scale link is therefore degraded and
not severed:""",
     """§2.2 whatever the recording practice does. The firm-scale link is therefore degraded and
not severed:""" ),
    (P4, """firm-quarter in both universes. The composition chain therefore has a *degraded* link at exactly
   the scale where the accounting is done""",
     """firm-quarter in both universes. The composition claim therefore has a *degraded* link at exactly
   the scale where the accounting is done""" ),
    (P4, """form in §3 is an approximation and not an identity, and the chain's link at the scale where
   accounting happens is degraded.""",
     """form in §3 is an approximation and not an identity, and the composition claim's link at the scale
   where accounting happens is degraded.""" ),

    # ---------------- Paper IV §8 · the killed framing goes in the body, in full -----------
    (P4, """**A fourth paper, on price formation, that was written and is not being published.**""",
     """**"A chain rather than three analogies."** The sentence this paper's §3 carried until the corpus's
first end-to-end test was run against it. Had it survived, §3 would assert a structural
correspondence between the sovereign scale's realisation share and the firm scale's observability
share, and that correspondence — not the three separate results — would have been this paper's
central contribution. `END-TO-END-001` leg `E1` shows the two shares are not the same kind of
object: the unrecognised remainder is deferred in one and discarded in the other, and the firm
scale carries a release rate α for which the sovereign scale has no counterpart. What is left is
weaker, is what §3 now says, and is still worth publishing: one question, asked at three scales,
answered quantitatively at each. The surviving resemblance is not nothing and is not a structure —
and the test that separated those two readings was designed, with its response to every outcome
fixed in advance, before anybody knew which one it would return.

**A fourth paper, on price formation, that was written and is not being published.**""" ),
]


# One phrase that exists nowhere in the corpus except in this remedy's output.
SENTINEL = ("A stronger reading is available, was tested, and is withdrawn here.", P2)


def already_applied():
    text, path = SENTINEL[1].read_text(), SENTINEL[1]
    return SENTINEL[0] in text, path


def main():
    landed, where = already_applied()
    if landed:
        print(f"ALREADY APPLIED — the remedy's sentinel is present in {where.name}. "
              "This script is a one-shot record of an applied registration; re-running it "
              "would be an edit made twice. Nothing done.")
        return 0
    if "--check" in sys.argv:
        bad = 0
        for path, old, _ in EDITS:
            n = path.read_text().count(old)
            if n != 1:
                print(f"ANCHOR {n}x (want 1): {path.name} :: {old[:60]!r}")
                bad += 1
        print("all anchors unique" if not bad else f"{bad} anchor problem(s)")
        return 0 if not bad else 1

    touched = set()
    for path, old, new in EDITS:
        text = path.read_text()
        if text.count(old) != 1:
            print(f"ABORT — anchor not unique in {path.name}: {old[:60]!r}")
            return 1
        if path not in touched:
            shutil.copy2(path, str(path) + ".bak-wt56-e1")
            touched.add(path)
        path.write_text(text.replace(old, new, 1))
        print(f"ok  {path.name}  <- {old.splitlines()[0][:56]}")
    print(f"\n{len(EDITS)} edit(s) applied across {len(touched)} file(s); .bak-wt56-e1 beside each")
    return 0


if __name__ == "__main__":
    sys.exit(main())
