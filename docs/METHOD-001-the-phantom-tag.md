# METHOD-001 · The phantom tag · a defect this project shipped six times, and the machine that now catches it

*Written for a reader who found this repository and wants to know how much of it to trust.
It is not a defence. It is the case against us, assembled by us, with the receipts.*

---

## 0 · What this document is, and why it is public

`docs/` in this repository is a working lab notebook by decision (`ADR-001` §Consequences).
That decision was made for a specific audience — the author's three children — on the
reasoning that **a record in which things went wrong and were caught teaches more about
method than any conclusion the papers reach.**

This file is the sharpest instance available. It documents a single defect that this
project committed **six times across three sessions**, each time in a costume that looked
nothing like the last, each time *after* the lesson had been written down. It gives the
six instances verbatim, explains why writing the lesson down kept failing, and describes
the mechanism that now enforces it — including the test that proves the mechanism works,
because a guard against unverified guards that is itself unverified would be the defect
wearing the costume of the cure.

**Nothing here was found by an outside referee.** Every instance below was found by this
project, about this project, before publication. That is the claim being made, and the
purpose of this document is to let a sceptical reader check it rather than take it.

---

## 1 · The six instances

| # | session | the assertion | why it could not fail |
|---|---|---|---|
| 1 | -06 | `assert 4.0/21 < 4.0/11 < 4.0/7 < 4.0/3` | four rational constants; references **no model output** |
| 2 | -07 | H2b, *"magnitude varies"* | with continuous i.i.d. values and 25 distinct pools, 25 distinct sums is a **probability-1 event under any mechanism** |
| 3 | -07 | `tie_break="index"` as a **negative control** | the array index is a per-item attribute, identical across all labellings — the control was **indistinguishable from the treatment** |
| 4 | -07 | `pressure_trace != pressure_trace` | **compares two invariants**; the quantity being read was the one that cannot vary |
| 5 | -08 | *"raise EVERYONE 20%"* as the population-defined **control** | multiplying every valuation by a constant is **rank-preserving**, so a single answer is forced by monotonicity whatever the allocation does |
| 6 | -08 | 25 uniform allocations reported as 25 **experiments** | 25 draws from a hypergeometric the population already fixes; the reported range 85–103 sits inside the ±2 sd band of its mean, **93.75** |

**In every case the code was correct.** Instance 3's control was a faithful implementation
of what its docstring said; instance 5's perturbation did exactly what it claimed. The
defect is upstream of the code: **the world could not produce a falsifying observation.**

That is why the project's existing rule was not enough. `WT-069` requires that every guard
be mutation-tested — that a deliberate corruption of the *code* be shown to kill it. **All
six instances survive every code mutant**, because there is nothing wrong with the code.

Instances 2, 3 and 4 were committed **in the same session that opened by quoting instance
1 as a cautionary lesson.** Instance 3 was committed inside a control built specifically to
prevent instance 1, whose docstring cites instance 1 by name.

---

## 2 · Why writing the lesson down kept failing

The defect was recorded in the project ledger as *"the `4/21 < 4/11` defect"* — **named
after its first costume.** That is precisely why it was not recognised in its sixth. A
session reads *"do not assert relations between rational constants"*, agrees, and then
reports twenty-five hypergeometric draws as twenty-five experiments. The name pointed at
the disguise rather than at the behaviour.

**A second reason, and it is less comfortable.** Every instance arrived attached to prose
asserting how good a guard it was. Instance 3's module docstring stated that the control
*"smuggles the labelling back in through the ordering"* — it does not — and then quoted the
project's own lesson about vacuous tests. **The stronger the prose claim about a guard, the
more likely the guard is vacuous**, because a guard that works does not need to be argued
for; it just goes red.

That is the same pathology this project ruled against in its **prose** on 2026-08-11 — text
that *announces* its rigour rather than *demonstrating* it. It turns out to have a
counterpart in test suites: **assertions that announce their severity rather than having
it.** The two were found on the same day and were not recognised as the same thing until
they were written next to each other.

---

## 3 · The rename

> **THE PHANTOM TAG.** In baseball, the phantom tag is the fielder credited with an out he
> never actually made — his foot never touched the bag. A phantom-tag assertion is a guard
> credited with catching something it never touched.

The umpire's question — *did the fielder touch the bag?* — translates without loss:
**did the assertion touch a value that could have been otherwise?** A name that describes
the behaviour rather than the first disguise is recognisable in the sixth.

---

## 4 · The mechanism · `scripts/severity.py`

**Every check ships a witness: a callable returning the condition evaluated in a world
where the claim is false. The witness is executed at check time.** If the witness also
passes, the check is a phantom tag and the run dies with a non-zero exit.

```
check("exactly 1 distinct excess-demand schedule",
      len(excesses) == 1,
      witness=w_wedge)        # the same count under a transaction wedge, where the
                              # allocation is KNOWN not to cancel. If it is still 1
                              # there, the check is blind.
```

There is one escape hatch, `DEFINITIONAL(reason)`, for claims no admissible world
falsifies. It demands a reason of at least thirty characters — *"obvious" is rejected by
the harness* — and every use is **counted and reprinted in the run summary**, so a script
that quietly reclassifies its way out of severity says so in its own output.

**This is Mayo's severity requirement applied one level below where this project had been
applying it.** A test passes severely only if it would very probably have *failed* had the
claim been false. The programme had been using severity language for its pre-registrations
and had never once applied it to an assertion. All six instances above have severity zero.

### 4.1 · The payoff that was not obvious

For instances 5 and 6, constructing the witness does not merely *detect* the defect —
**it hands you the correct experiment.**

- *"Show me a population-defined perturbation giving more than one interval"* **is** the
  random-subset control, which is the experiment that exposed instance 5.
- *"Show me an allocation with volume outside 85–103"* **is** the comonotone coupling,
  which is the experiment that exposed instance 6.

Both took an adversarial agent and two hours of session time to find. The witness
requirement would have produced them in the first ten minutes, for free, as a side effect
of being unable to write the check.

### 4.2 · The harness is itself tested, and the test is the original defect

`tests/test_severity.py` runs instance 1 — `4/21 < 4/11 < 4/7 < 4/3`, the assertion that
started the family — through the harness and requires it to die. It also runs instance 5's
shape, a missing witness, a too-thin `DEFINITIONAL` reason, and a genuinely severe guard
that must survive. Six tests. **A harness against unverified guards that had never been
shown to catch one would be this document's own subject.**

---

## 5 · Status, honestly

- **`scripts/wt070_p3_fold.py` is fully retrofitted** and is the worked example: 18 severe,
  1 definitional, 0 vacuous. **Instance 5 is preserved in it**, relabelled
  `HISTORICAL PHANTOM TAG`, with the witness that kills it attached — so the repository
  contains the defect and its refutation in the same file, executable.
- **`wt071_refuter.py` and `wt072_coupling.py` are NOT yet retrofitted.** The mechanism
  exists and one worked example exists; converting them is mechanical and is the first
  item of the next session. Recording this rather than quietly finishing later is the
  point of the document.
- **121 tests passing** at the time of writing.

---

## 6 · A note on publishing this at all

Making an error log public is not the norm in economics, and a reader is entitled to ask
whether it is bravado. Three things are worth saying plainly.

**It is not novel and it is not reckless.** Open-notebook science has existed since the
mid-2000s; registered reports exist precisely to make a failed prediction publishable; and
psychology's Loss-of-Confidence Project asked researchers to self-report published findings
they no longer believe. This project already ships a **failed pre-registration** as a
deliverable and each paper carries its **own hostile referee report**. This document is
continuous with those decisions, not a departure from them.

**The real risk is not embarrassment — it is navigation.** An openness that a later reader
cannot navigate is a trap rather than a gift: a superseded draft read as current does more
damage than no draft at all. Every superseded artifact in this repository therefore carries
a banner naming what supersedes it, and `docs/HANDOFF.md` states the current state of every
paper. **If you are reading a document here and cannot immediately tell whether it is
current, that is a defect in this repository and not in your reading.**

**And the asymmetry that makes it cheap.** The author holds no academic position and this
work has no funding, no tenure clock and no competitor. The usual reason for concealing a
false start — that someone will use it against you — does not apply. What remains is the
reason the notebook was made public in the first place: **a record of six failures, each
caught before publication, is a stronger claim about method than a clean record would be,
because a clean record is indistinguishable from an unexamined one.**

---

*The defect is six sessions old, has been written down five times, and was mechanised
once. The fifth writing-down would itself have been an instance of it.* ⚾
