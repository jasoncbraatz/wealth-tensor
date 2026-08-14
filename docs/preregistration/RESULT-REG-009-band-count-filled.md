# RESULT · REG-009 §7.5's BAND COUNT, ON THE COVERAGE-FILLED JOIN
*wealthTensor-32 · 2026-08-14 · the measurement `-31` named, priced and left unrun. Construction registered in `CONSTRUCTION-REG-009-coverage-fill.md`, in a commit that carries no number. Instrument: `scripts/reg009_band_count_filled.py`. Full output: `RESULT-REG-009-band-count-filled-run.log`. Table: `data/reg-009-band-count-filled.json`. 21 severe checks, 0 definitional, 0 vacuous.*

---

## 0 · What ran, and what it was run against

`RESULT-REG-009-band-count` §3 reported that 41 of the 151 tier-0 property events could not be binned at all, so the count of one clearing band is a **lower** bound; that a proportional fill of those 41 lands a second band on **30.2** against a floor of 30; and that the measurement replacing both brackets is the coverage fill SOURCE-001 §3b named in its own *"what this does not establish"*.

That fill is run. The seven intervening cycles — `2015-16` through `2021-22` — were extracted with `reg009_p0_lifetime_values.py extract`, the same instrument that produced the two committed cycles, on the same six-zip shape, through the committed 2014-15 window translated forward by whole years. **No window was invented and no rule was re-chosen**; H2 refuses the run if any filled window is not that translation, and its witness is a window displaced by one day.

**`-31`'s row was reproduced before it was extended** (H1): 151 events, 110 joinable, sixteen bands, one clearing. The run stops if it disagrees. That is `-31`'s own discipline — *reproduce the published table before extending it* — turned on `-31`, and this time the published table held.

**The 2014-15 cycle was also re-extracted from the SEC zips and compared to the committed artifact: identical, object for object**, on a different interpreter in a different machine. The fill's inputs are the committed instrument's outputs, not a lookalike.

## 1 · The fill, and the coverage series it completes

| cycle | window | firm-years with a parsed life / panel firm-years in window |
|---|---|---|
| 2014-15 | 2014-10-31 … 2015-09-30 | 612 / 847 = **0.723**  *(committed)* |
| 2015-16 | 2015-10-31 … 2016-09-30 | 593 / 828 = 0.716 |
| 2016-17 | 2016-10-31 … 2017-09-30 | 583 / 767 = 0.760 |
| 2017-18 | 2017-10-31 … 2018-09-30 | 599 / 762 = 0.786 |
| 2018-19 | 2018-10-31 … 2019-09-30 | 600 / 766 = 0.783 |
| 2019-20 | 2019-10-31 … 2020-09-30 | 584 / 737 = 0.792 |
| 2020-21 | 2020-10-31 … 2021-09-30 | 586 / 736 = 0.796 |
| 2021-22 | 2021-10-31 … 2022-09-30 | 685 / 853 = 0.803 |
| 2022-23 | 2022-10-31 … 2023-09-30 | 684 / 837 = **0.817**  *(committed)* |

**This is P0's rate — a parsed canonical life VALUE per panel firm-year — and it is NOT §3b's 0.727 / 0.823, which counts a life being TAGGED on a different instrument.** The two are one level apart and are not plotted as one series. What the nine points do say, at P0's own level, is that SOURCE-001 §3b's open question — *"nothing here says the non-December series rose smoothly rather than in a step"* — has a smooth answer on this measure: the rate rises monotonically from 2015-16 to 2022-23 with no year moving more than 4.4 points. §3b's question about its own instrument stays open; this is the neighbouring series, not that one.

**What the window shape cannot reach, measured rather than closed.** Consecutive windows abut at 09-30 / 10-31, so a fiscal year ending **1–30 October** lies in no window of the series, in any year — eight gaps of thirty days each. Widening the window would be a parameter chosen after the fact, so the gap is reported: **26 panel firm-years across 8 firms** fall in one, **one** of those firms owns a tier-0 property event, and that firm is joined anyway. The gap cost this count nothing, and it is on the record so the next fill does not have to rediscover it.

35 (cik, cycle) pairs carry two firm-year rows inside one window — a firm that changed its fiscal year end. The last row in file order wins, which is exactly what `-31`'s two-cycle index did; the rule is unchanged and the count of rows it decides is printed rather than absorbed.

## 2 · The count

**110 of 151 joinable becomes 133 of 151.** Eighteen events, across sixteen firms, are out of reach in all nine cycles: six of those firms have no panel firm-year inside any window, and ten filed inside a window and never tagged a canonical property life.

**`R_MID`, primary, cycle nearest the event — seventeen occupied bands, and one of them clears 30.** `-31`'s two-cycle row beside it:

| band (years) | events (was) | firms (was) | pilot | replication |
|---|---|---|---|---|
| [2, 3) | 1 (1) | 1 (1) | 0 | 1 |
| [3, 4) | 13 (7) | 11 (7) | 3 | 10 |
| [4, 5) | **27** (22) | 18 (15) | 4 | 23 |
| **[5, 6)** | **47** (36) | **22** (20) | 21 | 26 |
| [6, 7) | 6 (3) | 6 (3) | 4 | 2 |
| [7, 8) | 10 (14) | 6 (6) | 10 | 0 |
| [8, 9) | 2 (1) | 2 (1) | 2 | 0 |
| [9, 10) | 10 (8) | 5 (4) | 10 | 0 |
| [10, 11) | 2 (4) | 2 (3) | 2 | 0 |
| [11, 12) | 1 (1) | 1 (1) | 1 | 0 |
| [12, 13) | 2 (2) | 2 (2) | 1 | 1 |
| [13, 14) | 3 (5) | 2 (3) | 3 | 0 |
| [15, 16) | 3 (3) | 3 (3) | 3 | 0 |
| [17, 18) | 1 (1) | 1 (1) | 1 | 0 |
| [18, 19) | 1 (1) | 1 (1) | 1 | 0 |
| [20, 21) | 1 (1) | 1 (1) | 1 | 0 |
| [21, 22) | **3 (—)** | 1 (—) | 3 | 0 |
*Every band is a band of the DISCLOSED life, not of the economic one — §4.7's own weak joint, and the slack in every row here as in `-31`'s.*

**The second band did not clear.** `[4, 5)` reaches **27** against a floor of 30. `-31`'s proportional bracket predicted **30.2** for that band, so **the unjoined events did not fall like the joined ones** — the bracket was labelled a bracket and not a prediction, and this is what it was hedging against. The adversarial bracket said at most three bands could clear; measured, no reading produces more than two, so that bound held.

**On firms — §3b's own unit is firm-years — zero bands clear. In the pilot and replication universes separately, zero.** Both unchanged from `-31`.

## 3 · The fill's price: the join is not only larger, it is partly RE-CHOSEN

A ninefold cycle set does not only add events. `pick_cycle`'s primary mode is *the cycle nearest the event's own fiscal year*, so an event already binned can acquire a **nearer** disclosure and move band without ever having been unjoinable. Declared in the registration before it was read, decomposed here:

| | events | firms |
|---|---|---|
| newly joinable — the fill's **gain** | **23** | 10 |
| moved band — the fill's **price** | **14** | 8 |
| unchanged | 96 | — |
| still unjoined | 18 | 16 |

The moves, before → after: `[7,8) → [5,6)` six events; `[5,6) → [3,4)` two; `[10,11) → [9,10)` two; and one each of `[4,5) → [6,7)`, `[12,13) → [4,5)`, `[13,14) → [8,9)`, `[13,14) → [12,13)`.

**The clearing band's growth is therefore not eleven events of new coverage.** `[5, 6)` went 36 → 47 on **+7 newly joinable, +6 moved in from `[7, 8)`, −2 moved out to `[3, 4)`**. A filled count reported as a single number would have shown "36 → 47" and hidden that half of it is the same events re-read against a different disclosure.

## 4 · §7.5's decision rule, applied — and the parameter the fill created

**One band clears. Fewer than two. On the registered rule the expensive half still arrives: §4.7's within-band design is not supported by the sample §4.7 says it runs on, and REG-011 still needs a universe outside SIC 5200–5999 and 7370–7379.**

**And that is the weakest form in which this session can state it, because the registered reading is now the ONLY reading that gives one.**

| reading | bands clearing 30 |
|---|---|
| **`R_MID`, cycle nearest the event — REGISTERED PRIMARY** | **1** |
| `R_MID`, earliest cycle | 2 |
| `R_MID`, latest cycle | 2 |
| `R_MID`, nearest cycle, **ties broken to the later disclosure** | **2** |
| `R_MIN` (any cycle choice) | 2 |
| `R_WEIGHT`, nearest cycle | 1 |

**The last row of the second block is the finding.** With two cycles, the *nearest-cycle* rule's tie-break was **structurally unreachable**: 39 events had a life in both cycles and **none** of them was equidistant, so no registration ever had to name a convention it could not reach. With nine cycles the tie is reachable and it decides **50 of the 133 events** — and the count is **1** if a tie breaks to the earlier disclosure and **2** if it breaks to the later one. §7.5's threshold is crossed by that convention alone.

**The convention this run used was fixed in the registration commit, before any count existed** (R4: cycles inserted chronologically, so a tie breaks to the earlier disclosure), and it is not moved now. But a threshold that a pre-registered convention happens to land on the low side of is not the same object as a threshold the sample clears or misses. `-31`'s one was robust — G10 found all three cycle choices agreeing. **This one is not, and the honest report of "one band clears" is "one band clears under the registered reading, and every other reading of the same 133 events gives two."**

**The standing refusal applies in its harder form.** *Never add a free parameter to absorb an objection* has been honoured seven times by refusing to add one. Here the parameter was not added — **it was created by the measurement**, and the refusal that matters is the refusal to *spend* it. `R_MIN` is not promoted (§6 refuses it because it scores best, and it is now also a rule under which the design survives). The cycle pick is not switched to `early` or `late`. The tie-break is not flipped. The registered reading stands and the straddle is reported beside it, which is the same discipline `-31` applied when `R_MIN` gave two and `R_MID` gave one.

## 5 · The residual, and what would move it

Eighteen events remain out of reach. Handing all of them to the cheapest bands lifts at most **two**; distributing them like the joined ones lifts **two**. Both brackets now sit where the measurement sits, which is what a fill is supposed to do to a bracket.

Six of the sixteen residual firms have no panel firm-year inside any of the nine windows at all — they are out of reach of the *window series*, not of the tagging. Extending the series outside 2014-2023 would reach them; that is a different fill, it is not registered anywhere, and it is not run here.

## 6 · The manuscript repair — registered here, before it is performed

Paper III §4.7 currently reads: *"Filling the coverage §5's two cycles leave between them would bring a second band to the floor if the unjoined events fall like the joined ones, and no allocation of them brings more than a third."*

That is a conditional about a measurement that is now run, and its antecedent is false: the unjoined events did **not** fall like the joined ones. **Registered before the edit is made:** the conditional is REPLACED — not hedged, and not annotated — by the measured outcome. The joinable population becomes 133 of 151; the single clearing band is stated; the second band's 27 against the floor of 30 is stated; and the fact that the registered reading is the only one giving one is stated once, in the claim's own units. The bound the old sentence carried ("no allocation brings more than a third") held and is not re-asserted, because a bound that the measurement has superseded is a hedge kept past its usefulness. No other sentence of §4.7 is touched and no hedge is added. G-COACH-3 is evaluated across the edit.

## 7 · What this does not measure

It does not measure whether a within-band timeliness comparison would *work* — only whether the sample can populate the bands it needs. It does not measure the economic δ: every band above is a band of the disclosed life and the δ qualifier stands on all of it. It does not move the 151, the 98 firms, the 683 pairs, Ψ, or any registered REG-009 number, and H6 refuses the run if it does. It does not reach fiscal years ending 1–30 October, by construction. And it does not price REG-011's universe, which §7.5 put out of scope and which stays there.
