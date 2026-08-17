#!/usr/bin/env python3
"""wealthTensor-64 · P7 pass 3 repairs — Paper II, independently read.

Batched, assert-before-write, .bak every touched file. Ten anchors in paper-II.md and one
in scripts/wt099_edits_pin001.py. Every `old` must occur EXACTLY ONCE or nothing is written.

Run with --dry to print the plan without writing.
"""
import pathlib
import shutil
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-")
                    else ".")
DRY = "--dry" in sys.argv
TAG = "bak-wt64-p7"

P2 = "docs/papers/paper-II-redistribution/paper-II.md"
W99 = "scripts/wt099_edits_pin001.py"

EDITS = [
    # ---------------------------------------------------------------- II-11 · the abstract
    (P2, "II-11 abstract: a module-scoped count attributed to the repository",
     "claim about any institution is made. All results reproduce from an open repository with 18\n"
     "tests.",
     "claim about any institution is made. All results reproduce from open code; 18 tests pin\n"
     "them."),

    # ------------------------------------------------- II-8 · the tolerance, in §1 and §3.1
    (P2, "II-8a §1 c2: 'within 5 %' is tighter than either the table or the suite",
     "with the mechanism identified as κ and a closed form for the flow base's κ that the\n"
     "   simulation reproduces to within 5 % (§3.1).",
     "with the mechanism identified as κ and a closed form for the flow base's κ that the\n"
     "   simulation reproduces to within 7 % at every rate tabulated (§3.1)."),

    (P2, "II-8b §3.1: state the residuals, name the convention, quote the suite's real bound",
     "  **E[η⁺] = μΦ(μ/σ) + σφ(μ/σ) = 0.1073** for the parameters above, which the simulation\n"
     "  reproduces to within 5 % and which the test suite asserts.",
     "  **E[η⁺] = μΦ(μ/σ) + σφ(μ/σ) = 0.1073** for the parameters above. The simulated κ runs\n"
     "  **4–7 % below** that form at every rate tabulated, and the residual is monotone in the\n"
     "  rate — −4.4 %, −4.9 %, −6.8 % at *r* = 1.000, 0.100, 0.025 — which makes it a\n"
     "  denominator convention rather than noise: the implementation measures κ against\n"
     "  post-growth wealth. The test suite asserts agreement within 10 %."),

    # ------------------------------------------------------- II-12 · §3.3's unstated config
    (P2, "II-12a §3.3 periodicity: name the base",
     "**Periodicity.** Holding the average rate constant at 0.02 per period, assessing every *P*\n"
     "periods at rate 0.02·*P* moves the stationary Gini from 0.486 (*P* = 1) to 0.456 (*P* = 20). A",
     "**Periodicity.** On a stock base, holding the average rate constant at 0.02 per period,\n"
     "assessing every *P* periods at rate 0.02·*P* moves the stationary Gini from 0.486 (*P* = 1) to\n"
     "0.456 (*P* = 20). A"),

    (P2, "II-12b §3.3 threshold: name the base and rate",
     "**Threshold.** Monotone and smooth, with no cliff: Gini 0.443 at zero exemption rising to 0.770\n"
     "at 20× the mean of the base. The interesting part is the near end.",
     "**Threshold.** On the same base at *r* = 0.025, monotone and smooth, with no cliff: Gini 0.443\n"
     "at zero exemption rising to 0.770 at 20× the mean of the base. The interesting part is the\n"
     "near end."),

    # ------------------------------------------- II-6 · §3.4's unopposed run is a stale-era run
    (P2, "II-6 §3.4: the 600-period numbers replaced by the T = 1200 run §3.1 publishes",
     "*N* = 800 the unopposed process reads Gini 0.977 and flat, while its top decile holds 0.988 of\n"
     "everything. The drift test was measuring the ceiling.",
     "*N* = 800 and *T* = 1200 the unopposed process reads Gini 0.994 and flat — short of the\n"
     "0.99875 ceiling it is pinned against — while its top decile holds 1.000 of everything. The\n"
     "drift test was measuring the ceiling."),

    # ------------------------------------- II-7 · §3.4's separation range, measured this time
    (P2, "II-7 §3.4: the printed range is refuted by the paper's own sweep, on either reading",
     "The criterion now requires a settled Gini **and** a top decile below 0.90, at which point the\n"
     "separation is unambiguous: bounded runs sit at 0.19–0.50, condensed runs at 0.99–1.00, and the\n"
     "top-share statistic is horizon-stable where the Gini is not.",
     "The criterion now requires a settled Gini **and** a top decile below 0.90 — and it is the\n"
     "second condition that does all of the separating. Across the sweep of §3.1 the bounded runs'\n"
     "Gini spans 0.000–0.891 against the condensed run's 0.994, which separates nothing; their top\n"
     "decile spans 0.100–0.861 against 1.000, clearing the 0.90 threshold with 0.039 to spare. The\n"
     "top-share statistic is also horizon-stable where the Gini is not."),

    # ------------------------------------------------------------------- II-4 · §5's seed claim
    (P2, "II-4 §5 limitation 5: 'means across seeds' is one seed, and robustness is tested not averaged",
     "5. **Finite N and a fixed parameter neighbourhood.** *N* = 800, and the results are means over a\n"
     "   tail window across seeds; the qualitative separations are large relative to that noise, but\n"
     "   the third decimal is not defended.",
     "5. **Finite N, one seed per reported figure, and a fixed parameter neighbourhood.** *N* = 800,\n"
     "   and every number above is a mean over a tail window of a **single** path at `seed = 0`\n"
     "   rather than an ensemble average. Seed-robustness is asserted separately rather than averaged\n"
     "   in: `test_the_result_is_not_a_lucky_seed` holds two configurations inside a stated band\n"
     "   across five seeds. The qualitative separations are large relative to that band, but the\n"
     "   third decimal is not defended."),

    # ------------------------------------------------------------------- II-5 · the §7 pin, twice
    (P2, "II-5a §7: the pin's defining clause was false — PIN-001's shape, in the sibling manuscript",
     "- **Commit for the results reported here:** **d655501** — the last commit touching `src/`, and\n"
     "  therefore the state of the module that produced §3's simulation output. It does **not** cover the\n"
     "  two `scripts/` commands named above, which produce §3 numbers from outside `src/`. *A\n"
     "  head-of-repository SHA will additionally be pinned when this paper is posted, and it is what\n"
     "  covers them.*",
     "- **Commit for the results reported here:** **3b11f23** — the last commit touching\n"
     "  `src/wealth_tensor/redistribution.py`, and therefore the state of the module that produced\n"
     "  §3's simulation output. The pin is **per file** deliberately, and an earlier draft of this\n"
     "  section shows why: it pinned the last commit touching `src/` as a whole, which is a sentence\n"
     "  whose truth changes whenever any unrelated module moves and which nothing in the repository\n"
     "  was watching. It does **not** cover the two `scripts/` commands named above, which produce §3\n"
     "  numbers from outside `src/`. *A head-of-repository SHA will additionally be pinned when this\n"
     "  paper is posted, and it is what covers them.*"),

    (P2, "II-5b §7: the paragraph defending the pin inherits the same phrase",
     "Pinning the last commit that touched `src/` rather than a bare placeholder is deliberate: it is\n"
     "non-circular (a paper cannot cite the commit that adds the paper), it is verifiable today, and it\n"
     "names the object a replicator actually needs — the state of the code, not the state of the prose.",
     "Pinning the last commit that touched the module rather than a bare placeholder is deliberate: it\n"
     "is non-circular (a paper cannot cite the commit that adds the paper), it is verifiable today,\n"
     "and it names the object a replicator actually needs — the state of the code, not the state of\n"
     "the prose."),

    # --------------------------------------------------- II-10 · 'the companion paper' is two papers
    (P2, "II-10a §1 c5: 'the companion paper' here is the price-formation manuscript, not §3.2's",
     "   loudly — alongside a second, in a companion module of the same suite, that does the same\n"
     "   office for the companion paper (§7).",
     "   loudly — alongside a second, in a companion module of the same suite, that does the same\n"
     "   office for this programme's price-formation manuscript (§7)."),

    (P2, "II-10b §7: name it, and disclose that the manuscript it constrains has been superseded",
     "  and `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`, which constrains the\n"
     "  companion paper in the same suite. A test suite that constrains its author is a different\n"
     "  object from one that flatters him, and the difference is checkable rather than asserted.",
     "  and `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`, which constrains this\n"
     "  programme's price-formation manuscript — since superseded by its own internal referee, and the\n"
     "  guard outlives it — in the same suite; it is a different companion from §3.2's work on the\n"
     "  reporting layer. A test suite that constrains its author is a different object from one that\n"
     "  flatters him, and the difference is checkable rather than asserted."),

    # ------------------------------------------------------------------ II-9 · the zakat pointer
    (P2, "II-9a §1: zakat does not appear in §3.1 and has not since the house-style pass",
     "never as a recommendation. Zakat appears in §3.1 for exactly one reason: it is assessed on stock\n"
     "held above a threshold across a full year rather than on income received, which places it\n"
     "somewhere specific on the base axis.",
     "never as a recommendation. Zakat is named in this paper for exactly one reason: it is assessed\n"
     "on stock held above a threshold across a full year rather than on income received, which places\n"
     "it somewhere specific on the base axis."),

    (P2, "II-9b the closing note: same dangling pointer",
     "*One citation is deliberately absent and is flagged rather than faked: §3.1 mentions zakat as a",
     "*One citation is deliberately absent and is flagged rather than faked: §1 mentions zakat as a"),

    # -------------------------- II-5c · instrument the new pin, so it is not prose-only (PIN-001)
    (W99, "II-5c: LATEST_TOUCH gains Paper II's module, so the pin goes red when the module moves",
     'LATEST_TOUCH: dict[str, str] = {\n'
     '    "src/wealth_tensor/edgar.py": "93a159b",',
     'LATEST_TOUCH: dict[str, str] = {\n'
     '    # wealthTensor-64: paper II §7 pinned "the last commit touching src/" — the PIN-001\n'
     '    # sentence, in the sibling manuscript, false since 2026-08-10 and missed by PIN-001\'s\n'
     '    # own census of six occurrences. §7 now pins this module per file; this line is what\n'
     '    # makes that pin go red the day the module moves, instead of nine days later.\n'
     '    "src/wealth_tensor/redistribution.py": "3b11f23",\n'
     '    "src/wealth_tensor/edgar.py": "93a159b",'),
]


def main() -> int:
    texts: dict[str, str] = {}
    for rel, label, old, new in EDITS:
        path = ROOT / rel
        if rel not in texts:
            texts[rel] = path.read_text(encoding="utf-8")
        n = texts[rel].count(old)
        if n != 1:
            print(f"REFUSED  {label}\n         anchor occurs {n}x in {rel}, needs exactly 1")
            print(f"         anchor was: {old[:90]!r}")
            return 1
        texts[rel] = texts[rel].replace(old, new, 1)
        print(f"ok  {rel:52s}  {label}")

    if DRY:
        for rel, text in texts.items():
            out = ROOT / (rel + ".wt64-dryrun")
            out.write_text(text, encoding="utf-8")
            print(f"dry-run wrote {out}")
        return 0

    for rel, text in texts.items():
        path = ROOT / rel
        shutil.copy2(path, str(path) + "." + TAG)
        path.write_text(text, encoding="utf-8")
        print(f"WROTE {rel}  (.{TAG} kept)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
