#!/usr/bin/env python3
"""wt203 — mark every SHIP-LIST entry repaired, with the commit that repaired it.

Pass B does not close by repairing the last S1; DoD §3.0 closes it when Pass C can start
AND finish.  This script writes the first half of that: the list itself now says, per
entry, what landed and where.  The second half is the handoff.

Idempotent: NO-OP on a second run, exit 0.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/SHIP-LIST.md"
C = "1e1e2a5"

HEAD_OLD = "**Nine entries. Six S1, three S2. Zero carried S3** — every S3 is in `POST-SHIP.md`."
HEAD_NEW = (
    "**Nine entries. Six S1, three S2. Zero carried S3** — every S3 is in `POST-SHIP.md`.\n\n"
    "---\n\n"
    "## ✅ CLOSED AT `wealthTensor-104` (PASS B), 2026-08-24 — ALL NINE REPAIRED IN `" + C + "`\n\n"
    "**Every entry below carries a `REPAIRED` line naming what landed.** The list did not grow: the\n"
    "one permitted growth (DoD § 3, Pass B) was not needed — no repair revealed an adjacent S1 at its\n"
    "own site. Two things Pass B found that are NOT on this list and are in `POST-SHIP.md` instead,\n"
    "which is § 1.2 working rather than failing:\n\n"
    "- `wc -w` on **macOS returns 7 527 in every locale**, so `SL-6`'s defect is invisible on darwin\n"
    "  and reproduces only under GNU `coreutils`. The repair names the locale for that reason.\n"
    "- `paper-I` is outside `#scope` in `docs/promises-adjudicated.tsv`, so its 13 promises are\n"
    "  unadjudicated by design. Untouched here; widening scope is a decision, not a repair.\n\n"
    "**Guards these repairs reddened, all closed in this same session:** `TERM-001` (wording),\n"
    "`REG-003 §7` (the peak-to-charge qualifier), `test_restatement_reach` (§ 4.9 DECLARED for α̂ —\n"
    "a tighter pin, not a weaker one), and `wt148`'s promise sweep (10 rows adjudicated `H` with\n"
    "their evidence re-run here, 2 superseded rows dropped with lineage markers).\n\n"
    "**`defensive_count.py --against 7c5b6fb` reads +0 on all three manuscripts.**\n\n"
    "---"
)

MARKS = {
 "SL-1": "**REPAIRED** `" + C + "` · `scripts/wt193_sl1_sl2_attribution.py`. The relative clause no longer points at\n`0.333`: the sentence now reads *\"outside the rectangle, whose own fastest disclosed rate is 0.333 —\nand above §5.4's measured peak-to-charge recognition rate of 0.408 per year as well.\"* The\ncomparison Pass A said was wanted is kept and made true; **the arithmetic was not touched.** The\nqualifier is not decoration — `REG-003 §7` forbids attaching a measurement of α̂ to an unqualified\n*recognition rate*, and its guard caught the first draft of this repair doing exactly that.",
 "SL-2": "**REPAIRED** `" + C + "` · same script. The possessive is gone: *\"from 0.00789 at the calibration —\n§4.4's closed form evaluated there — to 0.00755 at the measured rate\"*. `wt090` prints\n`reproduces §4.4's published 0.00789 at alpha=0.05`, so the new attribution is the true one.",
 "SL-3": "**REPAIRED** `" + C + "` · `scripts/wt194_version_stamps.py`. **Version 0.3, 2026-08-24**, and one\nclass-level line appended to the existing revision history. No ruling from Jason had landed, so the\nbump was made rather than waited for. `git log --since=2026-08-24 -- <the file>` returned 0 commits\nbefore the repair commit itself.",
 "SL-4": "**REPAIRED** `" + C + "` · same script. **Version 0.6, 2026-08-24**, plus a *Revision note* (this\npaper carried no revision history at all). Same class-level wording as `SL-3`.",
 "SL-5": "**REPAIRED** `" + C + "` · same script. **Version 0.2, 2026-08-24**, plus a *Revision note*.",
 "SL-6": "**REPAIRED** `" + C + "` · `scripts/wt195_wordcount_locale.py`. § 10 gains a **Regenerate §8's word\ncount** bullet naming the command *and* the locale —\n`LC_ALL=C.UTF-8 wc -w docs/papers/paper-I-price-formation/paper-I.md` → **7,527** — and states that\nthe same bytes return **7,367** under GNU `wc` in a non-UTF-8 locale. § 8 now points at § 10 instead\nof claiming the draft file is the only place the count is checkable. *\"roughly 7,500\"* is unchanged,\nas Pass A required. **Note for anyone re-checking on darwin: macOS `wc` returns 7 527 in every\nlocale. The 7 367 reproduces under GNU `coreutils`.**",
 "SL-7": "**REPAIRED** `" + C + "` · `scripts/wt197_paperIII_sec4_provenance.py`. § 11's scope sentence now reads\n*\"Every simulation result in §A.2, §§2–3 and §4 is produced by open code, and the bullets below name\nthe command that prints it. Where a figure is printed by no command here, the bullet says so.\"*\nFour **Regenerate** bullets follow, covering §§ 4.2, 4.4, 4.5, 4.6, 4.7, 4.8 and 4.9 — `wt084`,\n`wt083`, `wt088`, `wt085`, `wt086`, `wt087` and `wt090`. **Every figure quoted in them was re-run\nbefore it was written down**, and all seven are adjudicated `H` in `docs/promises-adjudicated.tsv`.\nOne figure has no command and the bullet says so rather than implying one: **§ 4.2's 31.7%** is\n`wt084`'s printed family restricted to a ten-per-cent opening gap, and the restriction is applied in\nthe prose. That is § 11's own § 5.3 form, copied rather than reinvented.",
 "SL-8": "**REPAIRED** `" + C + "` · `scripts/wt198_paperII_citations.py`, copying `-81`'s `IV-7` repair. Eight of\nthe nine are now cited at the sentence that relies on them — the three kinetic-exchange entries at\n§ 1's *\"the kinetic-exchange literature has established this repeatedly\"*, Gabaix at § 6's tail-index\nclause, and Kaldor, Auerbach, Toder and Viard, and Saez and Zucman at § 6's public-finance paragraph.\n**Piketty (2014) is CUT:** no sentence relies on it, the paper is positive throughout and says so,\nand padding the body to justify an entry is the move Pass A forbade. **Checked:**\n`wt133_crossref_sweep.py` sweep 2 now reports paper-II **15 entries, 15 cited, 0 not**.",
 "SL-9": "**REPAIRED** `" + C + "` · `scripts/wt196_absence_census.py`. **Two clauses, not one** — the item asserted\nits census twice, and a repair landing at one site leaves the document asserting both things. The\nlede is now *\"One of this paper's absences is measured and three others named here are asserted\"*\nand the enumeration *\"Three others, named here, are not measured\"*. Exhaustiveness was **not**\nverified; that is POST-SHIP work and is logged there.",
}

def main() -> int:
    text = P.read_text(encoding="utf-8")
    if "CLOSED AT `wealthTensor-104`" in text:
        print("wt203: NO-OP (already marked)"); return 0
    if HEAD_OLD not in text:
        print("wt203: header anchor not found"); return 2
    text = text.replace(HEAD_OLD, HEAD_NEW, 1)
    for tag, mark in MARKS.items():
        anchor = "### `" + tag + "` ·"
        i = text.index(anchor)
        # insert the mark just before the next heading (or the section rule) after this entry
        j = text.find("\n### ", i + 1)
        k = text.find("\n---", i + 1)
        end = min(x for x in (j, k) if x != -1)
        text = text[:end] + "\n\n" + mark + "\n" + text[end:]
    P.write_text(text, encoding="utf-8")
    print("wt203: APPLIED — nine entries marked repaired at " + C)
    return 0

sys.exit(main())
