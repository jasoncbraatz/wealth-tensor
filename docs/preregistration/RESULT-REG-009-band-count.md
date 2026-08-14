# RESULT · REG-009 §7.5's BAND COUNT — the tee-up's cheap half, run
*wealthTensor-31 · 2026-08-14 · the count §7.5 registered the procedure and the decision rule for, before any number existed. Instrument: `scripts/reg009_band_count.py`. Full output: `RESULT-REG-009-band-count-run.log`. Table: `data/reg-009-band-count.json`. 14 severe checks, 0 definitional, 0 vacuous.*

---

## 0 · What ran, and the rule it was run against

§7.5 of `REG-009-p3-lifetime-sourced-delta.md` priced paper III §4.7's proposed design — *"compares timeliness only within a life band"* — and left one quantity uncounted, with the procedure and the decision rule both written down before any number existed:

> join `reg-006-ladderC-events-corrected.json`'s 151 property events to the disclosed lives, bin them at D3's 1.00-year width, and count how many bands clear 30. … **Only if fewer than two bands clear does the expensive half arrive.**

This is that count. **REG-009 is closed and is not reopened**: nothing here moves a registered number, renumbers a section, or repairs §4's coverage silence. §7.5 registered a procedure and a threshold; this file executes them and reports what came back.

**Nothing about a band is typed in the instrument.** D3's bin index and edges are lifted through `reg009_ladder_inputs.lift_band_rule()`, which lifts them in turn out of `reg009_p0_lifetime_values.py` at run time, and a source-text guard (G3a) refuses this instrument if the bin rule ever reappears in it as a literal. The band width, the floor of 30, the two canonical tags, the three interval rules and the two cycle labels are all imported from the instrument that registered them rather than retyped.

## 1 · §7.5's own table, reproduced before it was extended — and two errata

Every cell of §7.5's table was produced by a probe that was never committed. Until this run, the counts paper III now prints — **151 events, 98 firms, 110 joining to a disclosed life** — had no instrument behind them. G4 reproduces **32 cells** of that table, and G8 pins the join key by showing that tier 1's joinable 71 reproduces under the *intangible* tag and not under the property tag (which would give 96).

**32 of 32 reachable cells reproduce exactly.** The two cells that do not are errata in §7.5 rather than in the crawl, and both are recorded here rather than repaired retroactively:

**ERRATUM 1 · the firm count in the `all` row.** §7.5 prints **307** distinct firms in *both* columns. 307 is the count on the tag list as first collected; the repaired crawl carries **338**. REG-006's repair added firms as well as events — 31 of them — and the row carried the old number across.

**ERRATUM 2 · the denominator of "21 per band".** §7.5 states that "P0-c's one surviving rung holds 7 qualifying bands at a 1.00-year width" and divides 151 by it. Read out of `data/reg-009-p0-result.json`, the 7 is the qualifying-band count under **`R_MIN`** — the rule §6 refuses to promote, and the rule `RESULT-P0` §3 tabulates as "the strongest rung". Under the **primary** rule `R_MID` the same width gives **9** qualifying bands, and the same arithmetic gives **16.8 per band**, not 21. *A count is a claim about the tag list that produced it* was `-28`'s rule; this is the same rule one level over — **a per-band average is a claim about the interval rule that produced the bands**, and the rule that produced this one is the one the registration declined to make primary.

Neither erratum changes the measured count below, because the count does not use either number. Both are recorded because §7.5's arithmetic is what paper III printed.

## 2 · The count

151 tier-0 events. **110 of them can be binned at all**; the other 41 belong to firms with no canonical property life in either of SOURCE-001's cycles, and no band can hold them. Of the 110, **39 events across 24 firms** belong to a firm that discloses a property life in *both* cycles, so something has to choose which disclosure supplies the life — G10 makes that choice three ways (nearest cycle to the event's fiscal year, earliest, latest) and reports all three.

**`R_MID`, primary, cycle nearest the event — 16 occupied bands, and one of them clears 30.**

| band (years) | events | firms | pilot | replication |
|---|---|---|---|---|
| [2, 3) | 1 | 1 | 0 | 1 |
| [3, 4) | 7 | 7 | 0 | 7 |
| [4, 5) | 22 | 15 | 3 | 19 |
| **[5, 6)** | **36** | **20** | **19** | **17** |
| [6, 7) | 3 | 3 | 3 | 0 |
| [7, 8) | 14 | 6 | 8 | 6 |
| [8, 9) | 1 | 1 | 1 | 0 |
| [9, 10) | 8 | 4 | 8 | 0 |
| [10, 11) | 4 | 3 | 4 | 0 |
| [11, 12) | 1 | 1 | 1 | 0 |
| [12, 13) | 2 | 2 | 0 | 2 |
| [13, 14) | 5 | 3 | 5 | 0 |
| [15, 16) | 3 | 3 | 3 | 0 |
| [17, 18) | 1 | 1 | 1 | 0 |
| [18, 19) | 1 | 1 | 1 | 0 |
| [20, 21) | 1 | 1 | 1 | 0 |
*The band a firm-year falls in is a band of its DISCLOSED life, not of the economic one — the same gap §4.7 names as its weak joint, and the slack in every row of this table.*

**The heaping §7.5 predicted is exactly what happened.** One band holds a third of the joinable events; ten of the sixteen hold five or fewer. §7.5 wrote *"the modal band would clear the floor and most of the others would not"* — measured, the modal band clears and **fifteen of sixteen** do not.

**Three counts, not one, and only the first is the registered threshold's subject:**

| reading | bands clearing 30 |
|---|---|
| **events, `R_MID`, all three cycle choices** | **1** |
| firms — §3b's own unit is *firm-years*, not events | **0** |
| events, in the pilot **and** replication universes separately | **0** |

**And the interval rule moves the answer across the threshold.** `R_MID` 1 · `R_MIN` 2 · `R_WEIGHT` 0. The cycle choice does not matter (G10: all three agree under every rule but one); the interval rule does. `R_MIN` is the reading under which the design lives, and `R_MIN` is the rule §6 refuses to promote *because it scores best*. Adopting it here to clear the threshold would be that refusal spent, on the same afternoon the threshold was tested — so the primary rule stands and the count is **1**.

## 3 · What the instrument could not reach

**41 of the 151 events could not be binned, and a count on a population the instrument cannot reach is a LOWER bound rather than an absence.** Two brackets, neither a prediction:

- **Adversarial** — hand every unjoined event to whichever bands are cheapest to lift over the floor: **at most 3** bands could clear.
- **Proportional** — distribute the unjoined events like the joined ones (×1.373): **2** bands clear, and the second one lands on **30.2** against a floor of 30.

**That second number is why the coverage fill is now decision-relevant rather than tidy.** Filling SOURCE-001's coverage series between the two cycles — one minute of download and about sixteen seconds of scan per zip, already teed up and already priced — raises the joinable column, and a representative fill puts `[4, 5)` within two-tenths of an event of the threshold. **The measurement that decides REG-011 costs less than the paragraph arguing about it.** It does not move the 151.

## 4 · §7.5's decision rule, applied

**One band clears. Fewer than two. On the registered rule, the expensive half arrives: §4.7's within-band design is not supported by the sample §4.7 says it runs on, and REG-011 needs a universe outside SIC 5200–5999 and 7370–7379.**

The verdict is reported at the strength the count supports, which is not the strength the rule's binary suggests. §7.5 called the design *marginal*, and marginal is what it stayed: one band clears on events and none on firms, but a proportional coverage fill reaches two. **The honest form of "the expensive half arrives" is therefore "the expensive half arrives unless the cheap fill says otherwise, and the cheap fill has not been run."** That is a narrower claim than the rule's, not a hedge against it — the threshold was crossed downward, and the one measurement that could cross it back is named, priced and unrun.

> **AMENDED 2026-08-14, `wealthTensor-32` — THE CHEAP FILL IS RUN, AND THE SECOND BAND DID NOT CLEAR.** The seven intervening cycles raise the join from 110 to **133 of the 151**, and `[4, 5)` reaches **27** against the floor of 30 where the proportional bracket above predicted 30.2: the unjoined events did not fall like the joined ones. One band still clears and §7.5's verdict stands. **But the fill made the nearest-cycle rule's TIE-BREAK reachable for the first time** — 0 of the 110 joinable events here, 50 of the 133 there — and the count is two under that tie-break's mirror, under both other cycle choices, and under `R_MIN`. The registered reading is now the only reading that gives one. Nothing above is repaired: see `RESULT-REG-009-band-count-filled.md`.

## 5 · The manuscript repair — registered here, before it is performed

Paper III §4.7 currently reads: *"Across the one-year life bands that design requires, 151 events average 21 per band against §5's floor of 30."* That sentence is wrong twice over — its 21 divides by `R_MIN`'s band count (§1, erratum 2), and its 151 is the population *before* the join that the design needs, of which 110 survive. **Registered before the edit is made:** the sentence is replaced by the measured count, its denominator is the joinable population rather than the crawl, the one-band outcome is stated, and the coverage fill is named as the measurement that could change it. No other sentence of §4.7 is hedged in response, and the surrounding "151 property events across 98 firms … with 110 of the 151 joining to a disclosed life" is correct and stays. G-COACH-3 is evaluated across the edit.

## 6 · What this does not measure

It does not measure whether a within-band timeliness comparison would *work* — only whether the sample can populate the bands it needs. It does not measure the economic δ; every band here is a band of the disclosed life. It does not move the 151, the 683 pairs, Ψ, or any registered REG-009 number. And it does not price REG-011's universe, which §7.5 already declared out of scope and which stays there.
