#!/usr/bin/env python3
"""wealthTensor-65 · record Jason's DECISION-001 ruling on the page that asked for it.

Jason ticked **A** on 2026-08-17, with a sequencing ruling that is not one of the three
options as written and is worth recording in his words rather than collapsing into "A":

    make a full Kelly bet on A, and only re-allocate that bet once we can build -- or IF we
    can build -- credibility behind C.

So: A now, the literature search as the next at-bat, and C priced with the search in hand.
`-60` recommended B; the ruling declines it for a reason `-60` could not have had, because it
is about ORDER rather than about B: if C happens, C replaces the title anyway, which makes B
the option most likely to be wasted work. The title question rides with the C decision.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = "docs/DECISION-001-A2-and-road-one.md"

OLD = """## ☐ Jason's call — tick one

- **☐ A** — stop the internal contradiction now, cheapest honest move, C stays open.
- **☐ B** — A plus retire a title that is two revisions behind its own body. *(My recommendation: B.
  A is strictly incomplete — it fixes the mechanism sentence and leaves the cover of the paper still
  making the claim. B is five more edits, no new risk, and it closes `REVIEW-004` E5 #7 as well.)*
- **☐ C** — commit to Road One. Then the next session's at-bat is **the literature search**, not the
  prose, and the prose follows only if the search comes back clean.
- **☐ none of the above / talk to me first.**"""

NEW = """## ☑ Jason's call — RULED 2026-08-17, in session `wealthTensor-65`

- **☑ A** — stop the internal contradiction now, cheapest honest move, C stays open. **TICKED.**
- **☐ B** — A plus retire a title that is two revisions behind its own body. *(`-60`'s
  recommendation. Declined, and for a reason about ORDER rather than about B: if C happens, C
  replaces the title anyway, which makes B the option most likely to be wasted work. The title
  question rides with the C decision.)*
- **☐ C** — commit to Road One. **NOT foreclosed — deferred behind its own blocker.** The
  literature search is now the next session's at-bat, exactly as this line says.
- **☐ none of the above / talk to me first.**

**THE RULING, IN JASON'S WORDS**, because it is a sequencing decision and not simply "A":

> *make a full Kelly bet on A, and only re-allocate that bet once we can build — or IF we can
> build — credibility behind C.*

**Why the search stopped being a blocker and became an at-bat.** Six sessions carried C as
*"blocked on one literature search, never run"*. A literature search is a Claude with web access
and an afternoon; it is not a decision. It went unrun because it was filed behind the decision,
and the decision waited on the price of C, and the price of C is the thing the search reports —
two items politely holding the door for each other. Breaking the deadlock costs one at-bat.

**The defensibility case that decided it**, recorded so the next session does not relitigate:

* What is actually indefensible today is not that κ is overclaimed, it is that **the paper
  contains its own refutation and does not notice** — §3.1's own table, plus §3.3, sitting four
  paragraphs below the sentence they kill. A referee who finds that concludes the author did not
  read his own table, and that judgement contaminates the parts of the paper that are right.
  **All three options fix this**, so the choice was only ever about what else to take on.
* **C's risk is the search, not the work.** `ROADS-001` calls truncation-vs-scaling *"the
  strongest claim and the one most likely to be wrong"*. Under A, if the effect turns out to be
  known, it is a supporting observation in §3 and gains a citation. Under C it is the title, and
  *"this is known and the author did not know"* is the one referee outcome no reproducibility
  apparatus can absorb.
* **C raises the evidentiary bar without raising the evidence.** Today the paper makes a
  measurement claim defended by committed code that reproduces byte-exact. C makes a theory claim
  about redistributive instruments in general — and `REVIEW-007` has just established that §5's
  results are **one seed** and that §3.4 had carried a 600-period number under a paper-wide
  T = 1200. Those are repaired as prose; the computational base underneath is unchanged.
* **The apparatus is the moat.** This paper's distinctive asset with referees is not its claims;
  it is that it is pre-registered, reproducible, and publicly documents predictions that failed.
  A modest paper behind that apparatus is close to unassailable. An ambitious one invites someone
  to test the ambition against the apparatus — and the apparatus is honest enough to answer.
* **And one of C's two headline payoffs was resting on a misdiagnosis.** `ROADS-001` argued that
  under Road One the ρ = 0 tautology becomes *a passed test — the framework predicting in advance
  that ρ cannot change A's shape*. `-65` measured it: `redistribution.py:131` is
  `recognised_flow += self.rho * gain + self.wage`, so at ρ = 0 the base is the **wage**, κ =
  0.000565 rather than zero, and the identity holds because the wage is **uniform across agents**
  — nothing to do with the multiplicative term. See `WT-098`. The result is real and is stronger
  than the paper claimed; the *story* C wanted to tell about it was not.

**What A cost, measured:** ten edits across two files, no new computation, abstract 249 → **244**
words (six of slack returned rather than spent), suite green. **`II-2` and `II-3` are repaired
here**, as `REVIEW-005` §2 said they would be by whichever option was ticked."""


def main() -> int:
    p = ROOT / DOC
    src = p.read_text(encoding="utf-8")
    n = src.count(OLD)
    if n != 1:
        print(f"ABORT · tick block not unique ({n}x)")
        return 1
    out = src.replace(OLD, NEW, 1)
    widest = max(len(line) for line in out.split("\n"))
    if DRY:
        q = p.with_suffix(p.suffix + ".wt65-dryrun")
        q.write_text(out, encoding="utf-8")
        print(f"DRY  wrote {q}  (widest line {widest})")
    else:
        shutil.copy2(p, p.with_suffix(p.suffix + ".bak-wt65-tick"))
        p.write_text(out, encoding="utf-8")
        print(f"WROTE {DOC}  (widest line {widest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
