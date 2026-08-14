# SCOUT-001 · Paper III · the opposing team

*Scouting report under **CO-AUTHOR-CHARTER §4**. Session `wealthTensor-40`, 2026-08-14.
Scheduled by Claude, per §4's standing schedule and Jason's ruling of 2026-08-14. Not a HITL ask.*

**What this is.** A scouting report on the OPPOSING team — the referees and forum commenters
paper III will actually face — run once, shortly before posting, on a manuscript whose content is
frozen and whose research ledger is empty. Adversarial input, constructive output. Hunt the scoop
and the attack so the whitespace comes out clean.

**What this is not.** Not a referee report, not the dossier era restarting (charter §9 explains why
that ended), and not a verdict of any kind. Every finding below ships with a drill attached —
STEELMAN, REPLACE, CUT or TEE UP — because a verdict without a drill is incomplete work. **ABSORB is
illegal**: nothing here asks for a new hedging sentence. Where a finding looks like it demands one,
the ticket names the narrower claim instead.

**Cage checks, stated up front so they can be audited.**

| guard | status this session |
|---|---|
| **G-COACH-4** — hostile output lands in `docs/scouting/` and nowhere else | held. This file and `probes/` are the session's only new paths. |
| **G-COACH-3** — defensive-sentence count non-increasing | not engaged. **`docs/papers/` was not touched.** `defensive_count.py` reads 3 invariant / 0 limitations, identical to `DEFENSIVE-BASELINE.json`. |
| **G-COACH-1** — every named weakness ships a repair | held, six for six. |
| **G-COACH-5** — at least one specific checkable strength named | held, §3, and two of the three are the obvious mechanical killers of §5's null **measured and absent**. |
| PRE-002 §5 stopping rule · REG-003 §7 | **honoured. No lag gradient was computed on any subsample.** See §5. |

**Every number in this file was measured this session against the committed data, and every probe
asserts against a figure the paper already publishes before it reports anything new.** The gates are
named per ticket. Nothing here is an agent's recollection of a literature.

---

## 0 · The six tickets, at a glance

| # | finding | drill | why it ranks here |
|---|---|---|---|
| **T1** | **`REG-003 §7` forbids rounding α̂ to "the recognition rate." The abstract rounds it, and so do four other sites.** | **REPLACE** | Cheapest repair on the board, unbounded cost if left. It is a registration violated *in the abstract* of a paper whose one unusual asset is registration compliance. |
| **T2** | **ASC 350-20-35-28's elected annual test date is a tier-independent delay bolted onto every lag. Charges concentrate on a firm's own calendar quarter at p < 0.0001 in both universes. The manuscript never mentions it.** | **TEE UP** + **STEELMAN** | The finding that decides acceptance at an accounting journal. It is a complete mechanical account of §5's null, and it is currently unanswered. |
| **T3** | **§4.4's domain rescue is stated at α̂ = 0.408 only. At `REG-003`'s own registered adverse cut of 0.327 the admissible share of disclosed pairs falls 0.974 → 0.814, and the asserted rectangle leaves the domain.** | **STEELMAN** | The referee's obvious next question, answerable from committed data, and answering it costs the paper nothing. |
| **T4** | **§4.2's continuum is presented as a freedom in one unobserved quantity. `wt084`'s own table shows each member also demands a different opening gap — up to +51.3% at φ = 0.** | **STEELMAN** | Turns "φ is free" from a claim that invites *"only under implausible assumptions"* into one priced in a quantity accountants have intuitions about. |
| **T5** | **§6.1's demotion says "over 2013–2024." The events run 2012 Q2 → 2026 Q2; 15.8% and 15.2% of them fall outside. No pull date is pinned anywhere, on an endpoint the paper itself documents as live.** | **REPLACE** | Trivial to fix, and a replicator finds it in ten minutes. The scope sentence is the paper's most carefully worded sentence and it is wrong. |
| **T6** | **§5.3's "no reading of the tier ordering as a noisy version of the predicted one survives that pattern" rests on a shape that survives 34% of firm-clustered resamples in the pilot. The robust statistic is already in hand.** | **REPLACE** | The paper overclaiming *about its own failure* — rarer, and a reader who has watched §7's discipline will notice the one place it lapses. |

---

## 1 · The opposing team

The paper's JEL codes (M41, D80, C18, G14, E01) and its bibliography put it in front of three
distinct benches. **They will not agree about what the paper is**, and the tickets below are ordered
by how much damage each does at the bench that matters most.

### 1.1 · The accounting bench — TAR, JAR, JAE, RAST, CAR

**This is the bench that decides the paper's fate**, and it is the one §4.6 picks a fight with by
name. §4.6 tells the conditional-conservatism literature that its cross-sectional comparisons read a
product, and then cites Khan and Watts (2009) and Ball, Kothari and Nikolaev (2013) as having *met
the confound and read it the other way up*. Those are not neutral citations. An editor drawing
referees from the cited set is drawing from people whose published readings the paper has
re-described as artefacts.

**What this bench actually cares about**, in order: the sample, the instrument, the institutional
detail, and only then the theorem. A referee here reads §5 before §4. **T2 and T5 are addressed to
this bench, and T2 is the one that can end the submission** — because it offers a complete
institutional account of the null that costs the referee no modelling at all.

**What this bench will *not* be moved by:** the 10⁻¹⁶ agreements in §7. To an accounting referee,
thirty rows showing that a closed form matches the simulation that shares its code is a statement
about the code, not about the world. §7's own framing knows this (the two rows it singles out are
the two that risked something); the table does not sort that way, so the signal is diluted by the
noise of its own thoroughness. *That is a presentation observation, not a ticket — the fix is a
column, and it is Jason's call whether the ledger is worth re-sorting for a reader who will skim it.*

### 1.2 · The identification/econometrics bench — and the pharmacometricians behind them

§4.2 is textbook flip-flop, and §4.2 says so, at length, with Bateman, Garrett, Kuan–Wright–Duffull,
Bellman–Åström and Nerlove all conceded in the same three paragraphs. **That concession is the
paper's best defensive work and it will be read as such.** The residual attack from this bench is
not *"you rediscovered flip-flop"* — the paper closes that door — it is:

> *"If the exchange is a clean two-root swap, the accounting content is the **mapping**: that the
> reporting layer is a first-order lag with a scale (1 − φ) and that the accounting primitives
> deliver exactly that form. The mapping is posited in §2, not derived from ASC 360-10-35. So the
> theorem is about a filter someone chose, and its reach over accounting is an assumption."*

The paper has a good answer to this and does not make it: §4.3's closing paragraph — *"Any model in
which reporting lag attenuates a physical signal will multiply a timeliness parameter by an
asset-life parameter somewhere, because the observable is a rate times a duration"* — is the
form-independence argument, and it is buried at the end of a subsection about rankings.
**STEELMAN, no ticket needed, one move:** that sentence belongs in §4.2, immediately after the
theorem box, where it converts "this filter" into "any filter of this kind."

**T4 is addressed to this bench.** It is the one place where a careful reader running the repository
sees a column the prose does not mention.

### 1.3 · The forum bench — SSRN readers, econ Twitter/Bluesky, EJMR, r/accounting

Fast, uncharitable, and they will read three things: the affiliation line, the AI-assistance
declaration, and the abstract. **They will not read §7.**

Their one-sentence dismissals are in §4 below with the sentence that prevents each. The important
structural fact about this bench: **T1 is the ticket they will find**, because "the recognition rate
is 0.41 per year" in an abstract, checked against a public registration that says *no sentence
anywhere may round it to that*, is a screenshot. The registrations being public is the paper's
greatest strength and its sharpest exposure, and those are the same property.

---

## 2 · The repair tickets

---

### T1 · `REG-003 §7` forbids the rounding the abstract performs

**REPLACE.** Five sites, four sentences of work.

**The registered constraint**, `REG-003-p3-recognition-rate-and-off-diagonal.md` §7:

> **α̂ is the recognition rate of the quantity PRE-002's instrument identifies**, under PRE-002's
> onset bridge. It is not "the" recognition rate of US GAAP, and **no sentence anywhere may round it
> to that.**

**The manuscript, at five sites.** Grep is the whole audit:

| line | text | rounds? |
|---|---|---|
| **67–68, the abstract** | *"The same registered events establish it: **the recognition rate is 0.41 per year against a calibration of 0.05**, so the disclosed lives lie inside the model's domain"* | **yes** |
| 614–616, §4.4 | *"That made the recognition rate, not the ordering, the quantity to establish first — and §5.4 establishes it. On the registered sample the recognition rate is **α̂ = 0.408 per year**"* | **yes** |
| 931, §4.9 | *"§5.4 measures the recognition rate and, in the same fit, rejects the shape the model assumes"* | **yes** |
| 1574, §7 ledger | *"**The recognition rate is an order of magnitude above the calibration**"* | **yes** |
| 1747, §9 limitation 4 | *"α is no longer in that list: §5.4 estimates it at 0.408 per year on the registered sample"* | **yes** |
| 1369–1397, §5.4 | *"...by an instrument built to look at something else"*; both registered biases named in the same paragraph; the 0.327 adverse cut given | **no — §5.4 complies** |

**§5.4 is scrupulous and everything downstream of it is not.** That is the shape of the defect, and
it is worse than a uniform lapse would be: the qualification exists, in the right paragraph, and
then every sentence that *uses* the number drops it. A referee who reads §5.4 first will forgive the
abstract; a referee who reads the abstract first will arrive at §5.4 already suspicious.

**The second registered constraint compounds it**, `REG-003` §3.3. α̂ = 0.408 lands in **R1**
(α̂ ≥ 0.33), and R1 is the *weak-evidence* branch by prior commitment:

> **A low α̂ is strong evidence; a high α̂ is weak.** ... If it lands in R1 or R2, the finding is
> exactly what two upward biases would manufacture, and **it must be reported with that sentence
> attached, in the same paragraph, not in a limitations section.**

This is the `-36` tell arriving on schedule: the favourable outcome's meaning was pre-committed, the
favourable outcome arrived, and the pre-commitment travelled to exactly one of the five paragraphs
that report it.

**THE DRILL.** Replace the noun phrase; do not add a caveat. The repair is a *narrower claim*, so
the defensive-sentence count cannot rise:

- **Abstract**, from *"the recognition rate is 0.41 per year"* → **"the peak-to-charge recognition
  rate is 0.41 per year, on both known biases' inflating side"**. Same length, one more fact,
  registration honoured.
- **§4.4, §4.9, §7, §9** → **"the recognition rate PRE-002's instrument identifies"** at first use in
  each, bare α̂ thereafter.
- **§9 limitation 4** → strike *"α is no longer in that list"* and write what is true: α is measured
  *for the quantity PRE-002 dates*, and its bridge to the model's α is the same unwritten bridge
  §4.5 and §6.2 name. **That is not a new concession — it is §6.2's own discipline applied to §5.4's
  own number**, and stating it converts the paper's most obvious internal inconsistency into a
  demonstration that the discipline is live.

**Cost of not doing it:** the paper's only unusual credibility asset is that its registrations are
public and honoured. A public registration that says *no sentence anywhere may round it* against an
abstract that rounds it is the single most quotable object in the repository.

---

### T2 · The elected annual test date is a tier-independent delay, it is measurable, and the manuscript is silent

**TEE UP** (a fresh registration) **+ STEELMAN** (§5.3's qualification 1, which currently says
"unquantified").

**The mechanism.** ASC 350-20-35-28 lets a firm elect *any* annual goodwill test date, provided it
is applied consistently. For a firm that trips no interim trigger, **the earliest possible
recognition is its elected annual date.** That is a 0–4 quarter delay added to every lag,
**independent of observability and identical across tiers** — precisely the kind of common additive
noise that compresses between-tier separation while leaving each tier's median near the others.

**Provenance, stated because it matters.** This was named by `REVIEW-004` **C12** during the dossier
era, with a diagnostic attached. **The diagnostic was never run and the confound never reached the
manuscript or any registration.** `grep -n "annual test\|35-28\|test date" paper-III.md` returns
nothing relevant; `grep -rl` across `docs/preregistration/` returns nothing at all. This report's
contribution is the measurement, not the observation.

**MEASURED — `probes/annual_test_date.py`.** Charge quarters, within firm, against a uniform null
holding each firm's own charge count fixed (4,000 draws):

| universe | firms | modal-quarter share, observed | null mean [95%] | *p* |
|---|---|---|---|---|
| retail, ≥ 2 charges | 60 | **0.751** | 0.575 [0.526, 0.625] | < 0.0003 |
| retail, ≥ 4 charges | 15 | **0.724** | 0.498 [0.434, 0.569] | < 0.0003 |
| computer services, ≥ 2 charges | 104 | **0.665** | 0.566 [0.530, 0.604] | < 0.0003 |
| computer services, ≥ 4 charges | 36 | **0.579** | 0.489 [0.449, 0.530] | < 0.0003 |

Charge calendar-quarter mix: retail **[69, 45, 44, 89]**, computer services **[83, 78, 85, 202]** —
**45% of computer-services charges land in one quarter of the four.** And `annual_attributed` runs
0.62/0.62/0.56/**0.43** across tiers 0–3 in retail and 0.38/0.48/0.47/**0.28** in computer services,
so the annual-versus-interim mix is *itself* tier-dependent, which is the second-order version of
the same problem.

**Every threshold, both universes, same direction, at the resolution 4,000 draws can report.** The
confound is present in the paper's own committed sample.

**What this does and does not license.** It does **not** say the gradient was there all along, and
**this report did not test that** — see §5. What it establishes is that §5.3's qualification 1,
which reads:

> *"Any measurement error in the onset attenuates a true gradient, and the reported power does not
> model that attenuation. The true power is therefore lower than 0.95–1.00, by an unquantified
> amount."*

has a **named institutional mechanism and a measured footprint** available to it, and is currently
carrying neither.

**THE DRILL, two halves.**

1. **STEELMAN §5.3 qualification 1**, in place, without lengthening it. Replace *"Any measurement
   error in the onset"* with the specific one: **the elected annual test date of ASC 350-20-35-28
   rounds every lag up to the firm's own test quarter, identically across tiers**, with the
   concentration statistic above as its footprint. This *strengthens* the paper: a null whose
   leading attenuation mechanism is named and measured is a null that has been thought about, and
   the alternative is a referee naming it first.
2. **TEE UP the fix, and do not run it here.** Any design that uses this — an onset bridge carrying
   the test-date offset, or a restriction to interim-triggered charges — is a **third instrument for
   the lag gradient**, and PRE-002 §5's stopping rule bars it on this data. It needs a fresh
   registration, registered before its instrument is coded (§5.1's own new rule), and it may not
   cite the present failure as support for anything (§9 limitation 2). **Card it. Do not build it
   this session or next.**

**Cost of not doing it:** an accounting referee writes *"the author has measured the audit
calendar"*, and that sentence is very hard to answer after the fact.

---

### T3 · The domain rescue is stated at one α, and `REG-003` registered the cut that moves it

**STEELMAN.** The paper already has the adverse number; it is compared to the wrong benchmark.

**§4.4 line 616 and the abstract both say the asserted rectangle *"lies inside the domain after
all"*** at α̂ = 0.408, with **0.974** of the 683 disclosed pairs admissible. Both true.

**§5.4 also reports the registered adverse cut** — dropping the 175 events charged one quarter after
the peak, *"the mass where the onset bridge is least credible"* — which gives **α̂ = 0.327**, and
comments: *"still an order of magnitude above the calibration."*

**That comparison is against 0.05. The comparison the domain claim needs is against 0.3333** — the
decay rate implied by the three-year life at the fast end of the asserted rectangle. §4.4 states the
threshold itself: *"all of it above α = 0.33."*

> **0.327 < 0.3333.** At the paper's own registered adverse cut, the asserted rectangle is **not**
> fully inside the domain, and the sample falls out of `REG-003` §3.2's **R1** into **R2**, whose
> pre-committed language is *"the domain sentence stands but is much narrower than written."*

**MEASURED — `probes/alpha_domain_sensitivity.py`.** *Gate: reproduces the paper's 683 pairs and
0.9736 admissible share at α = 0.408 exactly before reporting anything else.*

| α | admissible share of the 683 disclosed pairs | *n* | rectangle fully inside? | what this α is |
|---|---|---|---|---|
| **0.327** | **0.8141** | 556 | **no** | `REG-003`'s registered adverse cut |
| 0.3333 | 0.8141 | 556 | boundary | the rectangle's fastest disclosed rate |
| 0.383 | 0.9590 | 655 | yes | α̂ 95% lower bound |
| 0.394 | 0.9590 | 655 | yes | computer services alone |
| **0.408** | **0.9736** | **665** | **yes** | **the headline — matches the paper exactly** |
| 0.433 | 0.9751 | 666 | yes | retail alone |
| 0.460 | 0.9751 | 666 | yes | the unregistered shifted estimate |

**109 of 683 pairs — 16% — are admissible at the headline and not at the adverse cut.**

**The shape of this is worth naming.** *Sampling* uncertainty is benign: at the 95% lower bound the
share is 0.959 and the rectangle is comfortably inside. It is **bridge** uncertainty that bites, and
bridge uncertainty is exactly what `REG-003` §3.3 registered in advance as running in the
paper-flattering direction. The two known biases push α̂ **up**; the domain rescue needs α̂ **high**;
the biases and the finding point the same way, and the registration said so before the number
existed.

**THE DRILL.** Add one column to §4.4's existing table — *R at the adverse cut* — and one clause to
the domain sentence, replacing the flat assertion with the range:

> the asserted rectangle lies inside the domain at the measured rate and at its interval, and at the
> registered adverse cut **0.814** of the disclosed pairs remain admissible.

**That is a number replacing an assertion, not a caveat added to one** — defensive count falls or
holds. And it converts the paper's weakest-looking move (a domain restriction rescued by the
paper's own new measurement) into its most disciplined one: *the rescue was tested against the cut
the registration nominated in advance as the one that would break it, and here is how far it bends.*

---

### T4 · The continuum is priced in the wrong currency, and the right one is already in the run output

**STEELMAN.** The claim is right and under-armed.

**§4.2, lines 439–445:**

> *"Fix a reported series generated at φ = 0.60 ... Assuming a physical scale of 0.76 implies φ = 0;
> assuming 1.27 implies φ = 1 ... **A factor of 1.67 in the unobserved physical scale spans the
> entire unit interval of timeliness.**"*

Exactly true. Also **incomplete**, and the missing part is printed by `wt084`'s own E7 table, one
column to the right of the one the prose quotes:

```
    E0 assumed   implied phi   implied g0    max |C - C_alt|
          0.76     -0.000000     0.513158          2.220e-16
          ...
          1.27      1.000000    -0.092105          1.110e-16
```

**The family is a freedom in two unobserved quantities, not one.** Each member demands its own
opening gap, and the **φ = 0 end requires g₀ = +0.513** — books opening more than half again above
the physical asset. Two smaller things a careful reader will also hit: the family is built around a
world that already opens at **g₀ = +0.15**, two paragraphs after §4.2 introduces *"the books opening
square — C(0) = E(0) = E₀"*; and a positive opening gap is precisely the state impairment accounting
exists to prevent, so **the demanding end of the continuum is the one an accounting referee will
refuse first.**

**MEASURED — `probes/continuum_gap_price.py`.** *Gate: asserts `wt084`'s printed endpoints
(E₀ 0.76 → 1.2667, factor 1.67, g₀ +0.513158 → −0.092105) before reporting anything new.* The
identified set, priced in the opening gap:

| opening-gap bound | φ reachable | width | of the unit interval |
|---|---|---|---|
| \|g₀\| ≤ 0.02 | [0.815, 0.881] | 0.066 | **6.6%** |
| \|g₀\| ≤ 0.05 | [0.765, 0.930] | 0.165 | **16.5%** |
| \|g₀\| ≤ 0.10 | [0.683, 1.000] | 0.317 | **31.7%** |
| \|g₀\| ≤ 0.15 | [0.600, 1.000] | 0.400 | 40.0% |
| \|g₀\| ≤ 0.25 | [0.435, 1.000] | 0.565 | 56.5% |
| \|g₀\| ≤ 0.52 | [0.000, 1.000] | 1.000 | 100.0% |

**The paper loses nothing by publishing this and gains the argument.** A 32%-wide identified set on
a parameter defined on [0, 1], available at a 10% opening gap that no filing discloses, is still
fatal to a cross-sectional ranking of φ — which is all §4.3 and §4.6 need. What it is *not* is
dismissible as an unbounded-freedom artefact, which is exactly how a referee disposes of *"φ is
free"* if the price is never quoted.

**THE DRILL.** Two sentences, both narrowing:

1. After the 1.67 sentence: **"Each member of the family carries its own opening gap; the φ = 0 end
   requires books opening 51% above the physical asset, and bounding the opening gap at ten per cent
   still leaves an identified set 0.32 wide."** One clause of concession buying a hard number — the
   defensive count does not rise, because this replaces nothing and hedges nothing; it states a
   result.
2. One clause at line 441 noting the family is anchored on the g₀ = 0.15 world of the previous
   paragraph, not on the square books of the paragraph before that. **CUT the ambiguity, not the
   claim.**

---

### T5 · The demotion's scope sentence does not describe the sample

**REPLACE.** Ten minutes' work, and the first thing a replicator checks.

**§6.1, the paper's single most carefully worded sentence:**

> **Not supported:** ... in US-listed retail trade or computer and data processing services
> **over 2013–2024**, at the firm level, at effect sizes of one quarter per tier or larger.

**2013–2024 is the *registrant selection* window, not the *event* window.** `RESULT-002-*-run.log`
line 2 reads *"673 registrants ever filing in range 2013-2024"* — a firm qualifies by filing in the
window, and every event `companyfacts` serves for that firm is then retained.

**MEASURED** from `data/pre-002-events.json`, the §5.4 rebuild (247 + 448 = **695**, and the tier
medians reproduce §5.3's published 5.0 / 4.0 / 5.5 / 5.0 and 5.0 / 4.5 / 6.0 / 5.0 exactly, which is
the gate):

- charge quarters span **2012 Q2 → 2026 Q2**; onset quarters span **2010 Q1 → 2026 Q1**
- events outside 2013–2024: **39 of 247 (15.8%)** in retail, **68 of 448 (15.2%)** in computer
  services
- the excess is not uniform across tiers — goodwill carries 27 of retail's 39 and 42 of computer
  services' 68

**And the second half is worse than the first.** §5.4 and §7 both document that `companyfacts`
serves a live endpoint (*"a re-pull is not the original pull"*; 688 → 695 in a week), and **no
retrieval date appears anywhere in the manuscript.** §11 names the source and pins three per-file
commits, which is exactly the right instinct applied to the code and not to the data. **The sample
grows every day the paper is not posted, and there is no sentence a replicator can hold it to.**

**THE DRILL.**

1. **REPLACE** §6.1's clause: *"in US-listed retail trade (SIC 5200–5999) or computer and data
   processing services (SIC 7370–7379), among registrants filing in 2013–2024, on charges recognised
   2012 Q2 – 2026 Q2"*. Longer by a line, narrower by a lot, and it is the sentence the paper
   actually earned.
2. **Pin the pull.** §11 gets a retrieval date and, if it is cheap, a digest of the two events files
   — the same discipline §11 already applies to `src/`. `REG-009`'s `LIVES_SHA256` gate is the
   pattern; the machinery exists.
3. Mirror the corrected window in the abstract if it names a period, and in §5.1.

---

### T6 · §5.3 overclaims, and it overclaims about the paper's own failure

**REPLACE.** The robust statistic is one bootstrap away and it is *stronger* than the rhetorical one.

**§5.3, lines 1344–1351:**

> *"...the ladder does not merely fail to be monotone — it is wrong in a specific and instructive
> place: **tier 2, indefinite-lived intangibles, carries the longest median lag in both universes**
> ... A four-rung ladder whose *third* rung is the tallest cannot be rescued by appeal to the top
> rung's behaviour, and **no reading of the tier ordering as a noisy version of the predicted one
> survives that pattern.**"*

The point estimates are right — 5.5 against 5.0, and 6.0 against 5.0. The inference resting on them
is not, and the paper knows why in a different section: §9 limitation 9 and §5.4 establish that
events are **not independent**, at 4.12× and 2.02× the independence rate.

**MEASURED — `probes/tier2_tallest.py`.** Firm-clustered bootstrap, 20,000 draws, seed recorded,
resampling firms because §5.4's own finding says events are not the unit:

| universe | observed medians (t0…t3) | P(tier 2 strictly the tallest rung) | P(ladder monotone in the predicted order) |
|---|---|---|---|
| retail | 5.0 · 4.0 · **5.5** · 5.0 | **0.339** | **0.057** |
| computer services | 5.0 · 4.5 · **6.0** · 5.0 | **0.526** | **0.058** |

**The shape the sentence rests on appears in a third of the pilot's resamples.** A referee who
re-runs this — and this is the one bootstrap a referee *will* run, because it is the paper's most
assertive empirical sentence — finds the paper's rhetoric outrunning its data in the one place the
paper had no incentive to be careful, which is the direction that costs it the most.

**THE DRILL.** Delete the "no reading ... survives that pattern" clause and put the number that says
it properly:

> **The predicted ordering appears in 5.7% of firm-clustered resamples in retail and 5.8% in
> computer services.**

That is the claim §5.3 wants, it is robust in both universes, it uses the resampling unit §5.4's own
finding demands, and it is **shorter**. Keep the tier-2 observation as an observation — *"tier 2
carries the longest median in both universes"* is true and worth one clause — and stop it before it
becomes an inference.

**Why this is the ticket worth the most to the paper's character.** §7's own commentary says a
survivals ledger containing only survivals is an advertisement, and names the row that cost the
paper its neatest sentence. This is the mirror case: the paper's scrupulousness is calibrated
against the temptation to *flatter* itself and has no guard against the temptation to be
*dramatically hard* on itself. Both are overclaims and only one of them is being watched.

---

## 3 · What the scouting found holding

*Charter §5 requires praise as specific and checkable as criticism, and G-COACH-5 requires at least
one named strength. Two of these three are the obvious mechanical explanations of §5's null,
measured, and absent — which is worth more than the tickets above, because a referee reaching for
either finds nothing.*

**S1 · Censoring is not tier-differential, and the predicted-longest tier has the *least* of it in
the pilot.** The natural attack on any null about long lags is that the instrument's ceiling hides
the tail of the tier predicted to be tallest. Measured from `pre-002-events.json`:

| tier | retail: censored % | computer services: censored % |
|---|---|---|
| 0 · PP&E | 4.8 | 17.6 |
| 1 · finite-lived intangible | 17.6 | 15.7 |
| 2 · indefinite-lived intangible | 11.8 | 17.0 |
| **3 · goodwill (predicted longest)** | **5.1** | **12.5** |

Goodwill is the *least*-censored tier in retail and the least in computer services. **The
twenty-quarter cap is not where the gradient went**, and §5.3's PRE-001-versus-PRE-002 table already
carries half of this argument without drawing the tier-level conclusion. *Free STEELMAN: add the
per-tier censoring column to that table. It costs four numbers and closes an attack outright.*

**S2 · Firm clustering is real but mild, and the paper's concession is more severe than its data.**
§5.3 qualification 2 concedes that 688 events come from 311 firms and calls the effective sample
smaller. Measured: **2.02 events per firm in retail and 2.35 in computer services**, largest single
firm 7 and 12 events, **top-five firms carrying 13.0% and 9.8%** of the sample. No firm dominates
either universe. The concession is correct in direction and the reader is left to imagine a worse
concentration than exists.

**S3 · The §4.5 row that refused.** Named because it is the strongest single fact about this paper's
process and a referee will only find it if the ledger points at it: a check written to confirm that
the identification result explained the registered null **refused in every one of 400 draws**, and
the claim came out of the paper. §7 says so in its commentary. **That row, not the theorem, is what
would make me referee this paper favourably**, and it currently sits in a 40-row table where it
looks like the other 39.

---

## 4 · The one-sentence dismissal, per bench, and the sentence that prevents it

| bench | the sentence they reach for | what prevents it | ticket |
|---|---|---|---|
| **accounting** | *"He measured the audit calendar."* | §5.3 qualification 1 naming ASC 350-20-35-28 and its measured footprint, before a referee does | **T2** |
| **accounting** | *"His own registration says he may not write that sentence, and it's in the abstract."* | four noun-phrase replacements | **T1** |
| **identification** | *"This is flip-flop with an accounting label; the mapping to accounting primitives is posited."* | §4.3's rate-times-duration argument moved up to sit under the theorem box | §1.2, no ticket |
| **identification** | *"The continuum needs assumptions you haven't priced."* | the g₀ table — 32% of the unit interval at a 10% opening gap | **T4** |
| **replication** | *"The stated period doesn't match the data and there's no pull date."* | one corrected clause and one retrieval date | **T5** |
| **forum** | *"Independent researcher, AI-drafted, and the abstract overstates the registration."* | T1 removes the checkable half; the registrations and the run logs handle the rest, and they are the paper's real answer | **T1** |
| **sympathetic reader** | *"Which of these forty rows should I care about?"* | a column on §7 separating algebra-versus-code rows from rows that risked something | §1.1, Jason's call |

---

## 5 · What this report did not do, and why

**Stated explicitly, because a scouting report that quietly steps over a stopping rule is worse than
one that finds nothing.**

- **No lag gradient was computed on any subsample.** T2's confound invites exactly that — split by
  annual-versus-interim and re-run Jonckheere–Terpstra — and it is barred twice: PRE-002 §5's
  stopping rule (*"there is no third instrument"*) and `REG-003` §7 (*"any attempt to read a
  co-occurrence finding as evidence that the lag gradient was there all along is ruled out here, in
  advance, in writing"*). `probes/annual_test_date.py` measures only a property of the instrument —
  do charges concentrate on a firm's own calendar quarter — which is the same kind of object as the
  censoring check in S1, and it is not a re-test.
- **No file under `docs/papers/` was read-modified or written.** G-COACH-4; the manuscript is not
  this report's output. `defensive_count.py` confirms 3 / 0, identical to the committed baseline.
- **No registration was designed.** The research ledger on paper III is empty and stays empty; T2's
  fix is carded, not built.
- **The dossier era was not restarted.** `REVIEW-004` C12 is cited as provenance for T2 and its
  diagnostic is run for the first time; nothing else from `REVIEW-001`, `POSITIONING-001/002` or
  `REVIEW-004` is re-served. Two of those documents' open items (C6's empty-domain challenge, C10's
  IAS 36 cross-regime test) are **still open and still good**, and are not re-argued here because
  re-serving a live finding is how a dossier grows back.
- **Nothing was taken on an agent's word.** Every figure above is from committed data in this
  repository, and every probe asserts against a number the paper already publishes before it reports
  a new one. The four gates are: 683 pairs / 0.9736 admissible (T3), `wt084`'s printed E7 endpoints
  (T4), §5.3's eight published tier medians (T5, T6), and the tier medians again (T2).

---

## 6 · Provenance

| probe | gate it passes before reporting | ticket |
|---|---|---|
| `probes/alpha_domain_sensitivity.py` | 683 disclosed pairs, 0.9736 admissible at α = 0.408 — §4.4 and `REG-009` | T3 |
| `probes/continuum_gap_price.py` | `wt084` E7's printed E₀ 0.76 / 1.2667 and g₀ +0.513158 / −0.092105 | T4 |
| `probes/tier2_tallest.py` | §5.3's published tier medians, both universes | T6 |
| `probes/annual_test_date.py` | §5.3's published tier medians and *n*; scope guard in the docstring | T2, S1, S2 |

All four are read-only, take seconds, need only `numpy`, and write nothing outside this directory.
Run from the repository root:

```
for p in docs/scouting/probes/*.py; do echo "== $p"; python3 "$p"; done
```

**Source documents relied on:** `docs/CO-AUTHOR-CHARTER.md` §§2, 4, 5, 7 ·
`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §§3.2, 3.3, 7 ·
`docs/preregistration/PRE-002-wt026-peak-to-charge.md` §5 ·
`docs/preregistration/RESULT-002-{pilot,replication}-run.log` line 2 ·
`docs/REVIEW-004-pre-posting-dossier.md` C12 · `data/pre-002-events.json` ·
`data/reg-009-p0-lives-{2015,2023}.json` · `data/reg-009-result.json` ·
`scripts/wt084_identification_closed_form.py` E6–E7 ·
`scripts/reg009_ladder_inputs.py` `psi_parts` / `load_population`.

---

*Six findings, six drills, no bare verdicts, and nothing hostile produced outside this directory.
The paper is in better shape than a scouting report makes it look — three of the six tickets are
steelmen that make claims harder to dismiss rather than repairs to claims that are wrong, and the
two obvious mechanical accounts of §5's null were hunted for and are not there. The two that are
real, T1 and T2, are real in different ways: one costs four sentences and buys back the paper's
credibility asset, and the other costs a card and buys back an afternoon of a referee's goodwill.*
