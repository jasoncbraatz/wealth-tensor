#!/usr/bin/env python3
"""wt151 · Paper III P7 pass 3 (wealthTensor-83) — REVIEW-023's four repairs.

III-1 §5.4  the pooled firm count is 307 and is not an erratum; the registered
            reconciliation rule is 95%/20%, not "one per cent".
III-2 §6.1  the three post-hoc conjectures live in RESULT-002-wt026.md §4, not
            in the repository's working notes (docs/notes/ holds neither).
III-3 §8.2  the reading list is POSITIONING-002 §6 and is marked UNDISCHARGED;
            §10 of this manuscript holds no queue.
III-4 §7    the three recognition rates agree to 5e-4 at twenty years, not 7e-4
            (RESULT-REG-005 §5 P_rows dev_vs_eff = 0.0005185).

Ten post-conditions, three of them NEGATIVE.
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
P = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
BAK = P.with_suffix(".md.bak-wt151")

src = P.read_text()
before = src

DEFENSIVE = re.compile(
    r"\b(however|although|admittedly|to be fair|it should be noted|caveat|"
    r"arguably|of course|granted|that said)\b", re.I)
def defensive_count(t): return len(DEFENSIVE.findall(t))
d_before = defensive_count(src)

# ---------------------------------------------------------------- III-1 · §5.4
OLD1 = """**The sample rebuilt to within one per cent, which is itself worth one line.** `companyfacts` serves
each firm's latest view of its own history, so a re-pull is not the original pull. Rebuilt: **695
events across 313 firms** against 688 across 311, with three of four tier counts identical in the
pilot and
censoring at 7.7% against 7.8%. The firm count is read back out of the committed
`data/pre-002-events.json`; an earlier revision of this sentence said 307, which would have made
the rebuild *fail* the one-per-cent reconciliation the sentence exists to assert. The registered reconciliation rule, fixed before the count was
known, admits this as the registered sample."""

NEW1 = """**The sample rebuilt at 99.0% agreement, which is itself worth one line.** `companyfacts` serves
each firm's latest view of its own history, so a re-pull is not the original pull. Rebuilt: **695
events across 313 firms** against 688 across 311, with three of four tier counts identical in the
pilot and
censoring at 7.7% against 7.8%. Those firm counts are per-universe sums — 122 + 191 against
121 + 190. Read as a **union** out of the committed `data/pre-002-events.json` the count is
**307**, six registrants having changed SIC between 2013 and 2024 and so entering both universes,
and that union is the *n* of the one-event-per-firm sensitivity below. The registered
reconciliation rule, fixed before the count was known, is 95% agreement in total *n* with no tier
moving by more than 20%; at 99.0% and 1.4% it admits this as the registered sample."""

# ---------------------------------------------------------------- III-2 · §6.1
OLD2 = """Three post-hoc conjectures about where the conjunction broke are recorded in the repository's
working notes."""
NEW2 = """Three post-hoc conjectures about where the conjunction broke are recorded in
`docs/preregistration/RESULT-002-wt026.md` §4."""

# ---------------------------------------------------------------- III-3 · §8.2
OLD3 = """The crash paper is a later paper in this corpus, written with a price line and after the reading
queue in §10 is discharged."""
NEW3 = """The crash paper is a later paper in this corpus, written with a price line and after the reading
list in `docs/papers/paper-III-dual-tensor/POSITIONING-002-second-pass.md` §6 — which that file
still marks undischarged — is discharged."""

# ---------------------------------------------------------------- III-4 · §7
OLD4 = "agree to **7 × 10⁻⁴** at twenty years, **15%** apart at three"
NEW4 = "agree to **5 × 10⁻⁴** at twenty years, **15%** apart at three"

EDITS = [("III-1 §5.4", OLD1, NEW1), ("III-2 §6.1", OLD2, NEW2),
         ("III-3 §8.2", OLD3, NEW3), ("III-4 §7", OLD4, NEW4)]

for tag, old, new in EDITS:
    if src.count(old) != 1:
        sys.exit(f"REFUSE {tag}: anchor occurs {src.count(old)} times, expected 1")
    src = src.replace(old, new)

shutil.copyfile(P, BAK)
P.write_text(src)

# --------------------------------------------------------------- POST-CONDITIONS
checks = []
def ok(n, cond): checks.append((n, bool(cond)))

txt = P.read_text()
ok("1 · §5.4 names the pooled count 307",
   "the count is\n**307**" in txt or "**307**" in txt)
ok("2 · §5.4 states the per-universe sums 122 + 191",
   "122 + 191 against\n121 + 190" in txt)
ok("3 · §5.4 quotes the registered rule verbatim in its own units",
   "95% agreement in total *n* with no tier\nmoving by more than 20%" in txt)
ok("4 · NEGATIVE — the false erratum is gone",
   "an earlier revision of this sentence said 307" not in txt)
ok("5 · NEGATIVE — no 'one-per-cent reconciliation' claim survives",
   "one-per-cent reconciliation" not in txt)
ok("6 · §6.1 points at RESULT-002-wt026.md §4",
   "`docs/preregistration/RESULT-002-wt026.md` §4" in txt)
ok("7 · NEGATIVE — no deferral to 'the repository's working notes'",
   "the repository's\nworking notes" not in txt and "repository's working notes" not in txt)
ok("8 · §8.2 points at POSITIONING-002 §6 and says it is undischarged",
   "POSITIONING-002-second-pass.md` §6" in txt and "still marks undischarged" in txt)
ok("9 · §7's ledger row now reads 5 × 10⁻⁴, matching RESULT-REG-005 §5",
   "agree to **5 × 10⁻⁴** at twenty years" in txt
   and "agree to **7 × 10⁻⁴**" not in txt)
ok("10 · defensive-sentence count non-increasing (charter §2)",
   defensive_count(txt) <= d_before)

for n, good in checks:
    print(("PASS  " if good else "FAIL  ") + n)
print(f"\ndefensive sentences: {d_before} -> {defensive_count(txt)}")
passed = sum(1 for _, g in checks if g)
print(f"{passed}/{len(checks)} post-conditions, 3 NEGATIVE")
if passed != len(checks):
    shutil.copyfile(BAK, P); print("ROLLED BACK from", BAK); sys.exit(1)
print("backup:", BAK)
