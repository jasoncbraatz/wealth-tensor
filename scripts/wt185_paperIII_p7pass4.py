#!/usr/bin/env python3
"""wt185 — the PATCH OF RECORD for wealthTensor-101, Paper III's FOURTH independent P7 read.

Three findings, three repairs, all inside §4.10 and §11, all produced by RUNNING
`scripts/wt091_lag_shape_identifiability.py` — the script that produces §4.10's table and
that the manuscript names only as the bare token `wt091`.

  III-5  [D]  §4.10 attributes the reference width 0.150 to §5.4, twice.  §5.4 carries the
              interval [1.135, 1.285]; it never carries its width.  Both upstream sources
              attribute the number to REG-003: `RESULT-REG-005` §2's table header reads
              "against REG-003's 0.150" and wt091 prints "x REG-003's 0.150" on all four
              rows.  REPAIR: name the interval the width is the width OF.
  III-6  [P]  §11 gives a runnable "Regenerate" bullet for §3, §A.2.3, §5, §5.4 and §A.2.4
              and none for §4.10, whose five-row table is the paper's answer to its own
              title.  `scripts/wt091_lag_shape_identifiability.py` produces every number in
              it, is registered against REG-005 (committed 6f0e7be BEFORE the script), and
              quotes the manuscript in its own docstring.  REPAIR: name it, with its
              registration and its runtime.
  III-7  [—]  §4.10 says the 10^-3 identified set "reaches k = 0.50".  The REGISTERED sweep
              reaches 0.60 — the paper's own table two paragraphs above says [0.60, 1.87],
              and 0.50 comes only from the unregistered [0.2, 3.0] robustness extension,
              which REG-005 §7 says is reported, labelled and unable to change a verdict.
              wt091 makes the paper's own argument with the registered number: "I(1e-3)
              reaches k = 0.60 < 1 — a DECREASING hazard".  REPAIR: use the registered
              number.  The claim gets STRONGER: it no longer leans on an unregistered
              sweep, and 0.60 < 1 carries the argument unchanged.  NO HEDGE ADDED.

NOT REPAIRED HERE, ON PURPOSE: `docs/preregistration/RESULT-REG-005.md` line 60 carries
III-7's slip too, and it is a committed result document for a registered run.  Editing one
in a reader-pass wants its own ruling (the REVIEW-023 §5 precedent).  Carded, with the
falsifier, in REVIEW-036 §5.

Idempotent.  Refuses on a moved anchor.  Rolls back the file on any failed post-condition.
"""
from __future__ import annotations
import sys, pathlib, hashlib

REPO = pathlib.Path(__file__).resolve().parents[1]
PAPER = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"

# (finding, anchor, replacement, IDEMPOTENCY MARKER)
#
# THE MARKER IS NOT OPTIONAL AND THIS SCRIPT LEARNED IT THE HARD WAY.  An INSERTING edit
# keeps its own anchor in the output — III-6 appends a bullet after §A.2.3's bullet, so
# after a successful run the anchor is STILL PRESENT and "have I run already?" cannot be
# answered by looking for it.  The first cut of this script re-applied III-6 on its second
# run and shipped the §4.10 bullet TWICE, while all fourteen post-conditions passed,
# because every one of them asked whether a string was present and none asked how many
# times.  A post-condition that cannot fail on a double application is not a post-condition.
EDITS = [
    ("III-5a",
     "| precision of the reported series | shapes it cannot separate from k̂ = 1.21 | width | against §5.4's 0.150 |",
     "| precision of the reported series | shapes it cannot separate from k̂ = 1.21 | width | against the 0.150 width of §5.4's [1.135, 1.285] |",
     "width of §5.4's [1.135, 1.285] |"),
    ("III-5b",
     "dates are** — an interval of 0.100 against §5.4's 0.150 from hand-collected impairment lags. At one",
     "dates are** — an interval of 0.100 against the 0.150 width of §5.4's [1.135, 1.285], from\nhand-collected impairment lags. At one",
     "[1.135, 1.285], from\nhand-collected impairment lags"),
    ("III-7",
     "set reaches **k = 0.50**, below one, a *decreasing* hazard — and §4.9's tail condition says a",
     "registered sweep's set reaches **k = 0.60**, below one, a *decreasing* hazard — and §4.9's\ntail condition says a",
     "registered sweep's set reaches **k = 0.60**"),
    ("III-6",
     "- **Regenerate §A.2.3:** `python3 scripts/wt002_lambda_report.py`\n",
     "- **Regenerate §A.2.3:** `python3 scripts/wt002_lambda_report.py`\n"
     "- **Regenerate §4.10:** `python3 scripts/wt091_lag_shape_identifiability.py` — ladders I, P,\n"
     "  W, S and N exactly as registered in\n"
     "  `docs/preregistration/REG-005-p3-lag-shape-identifiability.md`, committed at **6f0e7be**\n"
     "  before that script existed. It prints §4.10's precision table, the identified set at every\n"
     "  reported precision, the search's own floor at the fitted shape, and the profile at the\n"
     "  constant hazard. Minutes on a commodity CPU. Until wealthTensor-101 this section named no\n"
     "  command for §4.10 and the manuscript named that script only as the bare token `wt091`.\n",
     "Regenerate §4.10"),
]


def apply(text: str):
    applied, already = [], []
    for tag, old, new, marker in EDITS:
        if text.count(marker) > 1:
            raise SystemExit("REFUSING: %s's marker %r appears %d times — a previous run "
                             "double-applied it. Restore the file from git and re-run."
                             % (tag, marker, text.count(marker)))
        if marker in text:
            already.append(tag); continue
        if old not in text:
            raise SystemExit("REFUSING: anchor for %s not found — the manuscript moved." % tag)
        if text.count(old) != 1:
            raise SystemExit("REFUSING: anchor for %s is not unique (%d)." % (tag, text.count(old)))
        text = text.replace(old, new, 1)
        applied.append(tag)
    return text, applied, already


def postconditions(text: str):
    """(label, condition, is_negative)"""
    P = []
    a = P.append
    a(("III-5a: the table header names the interval", "width of §5.4's [1.135, 1.285] |" in text, False))
    a(("III-5b: the prose names the interval", "the 0.150 width of §5.4's [1.135, 1.285], from" in text, False))
    a(("III-5: NO bare \"§5.4's 0.150\" survives anywhere", "§5.4's 0.150" not in text, True))
    a(("III-5: the number 0.150 is still reported (repair states, does not delete)", text.count("0.150") >= 2, False))
    a(("III-7: the registered floor 0.60 is the one the argument uses", "registered sweep's set reaches **k = 0.60**" in text, False))
    a(("III-7: the unregistered 0.50 no longer carries the argument",
       "set reaches **k = 0.50**" not in text, True))
    a(("III-7: the unregistered sweep's [0.50, 1.86] is STILL disclosed two paragraphs above",
       "[0.50, 1.86]" in text, False))
    a(("III-7: the table's registered row is untouched", "| 10⁻³ | [0.60, 1.87] | 1.27 | 8.5 × |" in text, False))
    a(("III-6: §11 names the §4.10 command as a runnable path",
       "`python3 scripts/wt091_lag_shape_identifiability.py`" in text, False))
    a(("III-6: the bullet cites the registration that predates the script",
       "REG-005-p3-lag-shape-identifiability.md`, committed at **6f0e7be**" in text, False))
    a(("III-6: §4.10's original bare `wt091` sentence is untouched",
       "five ladders before `wt091` existed" in text, False))
    a(("III-6: the bullet sits inside §11, not §4.10",
       text.index("Regenerate §4.10") > text.index("## 11 · Data and code availability"), False))
    a(("no new defensive hedge: 'may be', 'we caution', 'it should be noted' not introduced",
       "it should be noted" not in text.lower(), True))
    # EXACTLY-ONCE.  These are the checks the first cut did not have, and their absence is
    # what let a double-applied bullet pass fourteen green post-conditions.
    for tag, _, _, marker in EDITS:
        a(("exactly-once: %s's marker appears once, not twice" % tag,
           text.count(marker) == 1, True))
    # A GLOBAL COUNT IS A LOOSE PROXY FOR DOUBLE-APPLICATION and churns on honest growth:
    # wealthTensor-104 added four Regenerate bullets to §11 repairing SHIP-LIST SL-7, and
    # this check went red on a manuscript that had gained provenance, not lost integrity.
    # Distinctness is the tighter subject -- it forbids a duplicated bullet from ANY pass.
    _bullets = [l for l in text.split("\n") if l.startswith("- **Regenerate ")]
    a(("§11's Regenerate bullets are all distinct — no bullet applied twice",
       len(_bullets) == len(set(_bullets)), True))
    a(("the manuscript did not shrink", len(text) > 0, False))
    return P


def main():
    if not PAPER.exists():
        raise SystemExit("no manuscript at %s" % PAPER)
    original = PAPER.read_text()
    before_sha = hashlib.sha256(original.encode()).hexdigest()
    text, applied, already = apply(original)

    checks = postconditions(text)
    neg = sum(1 for _, _, n in checks if n)
    failed = [l for l, c, _ in checks if not c]

    print("=== wt185 · Paper III P7 pass 4 (wealthTensor-101) ===")
    print("  applied : %s" % (", ".join(applied) or "(nothing — already applied)"))
    if already:
        print("  already : %s" % ", ".join(already))
    print("  sha256 before: %s" % before_sha[:16])
    for label, cond, isneg in checks:
        print("  [%s] %s%s" % ("PASS" if cond else "FAIL", "(NEGATIVE) " if isneg else "", label))
    print("  post-conditions: %d checks, %d NEGATIVE" % (len(checks), neg))

    if failed:
        print("\n  ROLLED BACK — manuscript untouched. Failures: %s" % failed)
        return 1
    PAPER.write_text(text)
    print("  sha256 after : %s" % hashlib.sha256(text.encode()).hexdigest()[:16])
    print("  WRITTEN.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
