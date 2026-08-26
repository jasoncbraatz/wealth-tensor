# RESULT-CROSSING-HEIGHT-001 · The crossing height is the allocation mismatch

*Written at wealthTensor-108, when the fourth manuscript was stood down and its parts were
redistributed. This result was **not** folded into a surviving paper. §0 says why, at the length the
refusal deserves, because a refusal without a reason is indistinguishable from an oversight.*

*Provenance: the argument and every number below are `paper-IV.md` §5, carried over with the
paper's own wording. `paper-IV.md` remains on `main` and under tag `v1.0-preprint`.*

---

## 0 · Why this is not in Paper III §5.6

Paper III §5.6 carries a crossing. Holding the first three tiers of the GAAP ladder fixed, the
deferral measures of goodwill and indefinite-lived intangibles cross at δ₃\* = *K*α/(1 + *K*),
*K* = *R*₂/(1 − φ₃) — a **threshold in a parameter**, above which a ranking is no longer monotone.
The obvious move at redistribution time was to land the result below beside it as "the same shape at
a different scale."

**That move was refused, and the refusal is the point.** The two objects share the English word
*crossing* and nothing else:

| | Paper III §5.6 | this result |
|---|---|---|
| what crosses | two deferral measures, as functions of δ | a demand schedule and a supply schedule, as functions of *p* |
| the crossing's coordinate of interest | the **abscissa** — the δ at which the order flips | the **ordinate** — the quantity traded at *p*\* |
| what the crossing tells you | that a published ranking inverts below a knife edge | that a diagram read as behaviour is reading state |
| the operator | R(δ, φ, α), a steady-state deferral transform | a partition of a finite population by reservation price |

No shared operator, no shared object, no shared parameter. The corpus has been here before: its own
end-to-end check (`docs/RESULT-END-TO-END-001-E1.md`) failed the fourth paper's central thesis at
leg `E1a` for exactly this failure mode — *"ρ and φ are not the same kind of object"* — and Paper III's Appendix A.3 now
records the resulting withdrawal in the manuscript itself — *"the two results share the question and
not the operator."* Landing this beside §5.6 would have committed the same error one level down,
inside the repair.

**So it is retired from the papers and kept here.** It is a real result with a working apparatus and
it is nobody's supporting evidence. If it is ever published it will be published on its own, about
the Marshallian cross, in front of a readership that has never heard of a recognition lag.

---

## 1 · The result

Take a market for a single indivisible good. *N* agents each hold a reservation price *mᵢ*; *S*
units exist; *H* is the set of current holders and *T* the set of the top-*S* valuers. The
textbook reads two schedules off this population — a demand curve and a supply curve — and finds
the price where they cross.

**The two schedules are not independent equations.** Measured over 25 allocations of the same
population at 399 interior grid points: 25 distinct demand schedules, 25 distinct supply
schedules, and **one** distinct excess-demand schedule, equal to #{*i* : *mᵢ* > *p*} − *S* at
every point. The reason is a partition. At any price that is not itself a reservation price the
*S* holders divide into those valuing above it and those valuing below, so the allocation enters
the two counts with opposite signs and cancels — at every price, not merely at the zero.

So the *price* coordinate of the cross reads the population and nothing else. The **quantity**
coordinate — the volume traded at the crossing, and the height of the cross in the diagram — reads
something quite different. At a clearing price strictly inside the interval,

> *D*(*p*\*) = |*T* \ *H*|,  *S*(*p*\*) = |*H* \ *T*|,  and the two are equal.

**The crossing height is the allocation mismatch** — the number of units in the wrong hands — which
is precisely the quantity excess demand cannot deliver. Verified for all 25 allocations.

Read as a composition statement, the diagram is doing two jobs in one picture: the price coordinate
is a fold over the population, and the height is a *coupling* between the population and the
current state. It is not a behavioural aggregate that has smuggled in state information; it is a
state measurement that has been read as behaviour for a century and a half of teaching.

---

## 2 · What this is not

It is not an SMD result and must not be sold as one. Excess demand here is monotone and
single-crossing — zero monotonicity violations across 500 grid points, running from +249 to −150
with one sign change — because each agent demands at most one unit and there is no wealth channel
from the endowment back into demand. Remove that restriction and income effects return, and income
effects are exactly what SMD requires. **The two results sit at opposite ends of one axis**: at zero
income effects the allocation cancels identically and the state is all there is; with income effects
the behavioural map stops composing and SMD is what one gets.

The test suite asserts the monotonicity deliberately, under the name
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`, as a standing limit on the claim
rather than a property being celebrated. **That guard outlives the manuscript it was written for**,
and Paper II §7 says so in the manuscript of record.

The SMD boundary itself — the distinction between a theorem about maps and a claim about states —
did not stay with this result. It is Paper III Appendix **A.4**, where it bounds P3.

---

## 3 · Reproduction

- **Module:** `src/wealth_tensor/excess_demand.py`
- **The table:** `python3 scripts/wt018_report.py` prints the 399 interior grid points, the 25
  demand, 25 supply and one excess-demand schedules, and the 500-point monotonicity sweep with
  **0** violations, endpoints **+249** and **−150**, and one sign change.
- **The identity:** `python3 scripts/wt071_refuter.py` gives the crossing-height identity across all
  25 allocations, together with the *N*-dependence table and its control.
- **The guards:** `python3 -m pytest tests/test_excess_demand.py -q` asserts the schedule counts and
  the twelve-point tie convention. It *asserts* the 399 rather than printing it, so a reader
  wanting the numbers should run the two commands above and read the tests for what may not move.

**A seed warning, paid for at wealthTensor-107.** Match a document's stated seed convention before
re-running anything against its published rows. The numbers above are the fourth manuscript's, at
that manuscript's convention; a sweep run at a different seed puts every figure a hair off every row
here and the discrepancy will look like a defect in the model.
