# REVIEW-002 · Internal adversarial referee reports on Paper I v0.1, the priority audit, and the responses

- **Draft reviewed:** `paper-I.md` v0.1, 2026-08-10, session wealthTensor-06 — reviewed the same
  session it was written.
- **Reviewers:** two agents run in parallel against the draft, the modules, the tests and the
  regeneration output. One was instructed to **check every number against the code that produced
  it** and to assess nothing else. One was instructed to **find reasons to reject**, told not to
  praise and not to summarise. A third agent was then run to **verify or refute the second
  referee's priority claims**, and was explicitly warned that an over-eager priority claim is as
  damaging as a missed one.
- **Verdicts returned:** Referee A — 11 defects, all confirmed. Referee B — **Reject**, 15 findings,
  4 rated FATAL. Priority audit — **two of the paper's six contributions are not new.**
- **Status:** **v0.1 does not survive.** The mechanical defects are fixed; the substantive findings
  require the paper to be re-scoped rather than edited, and that is deliberately **not** attempted
  in the session that received them. See §Disposition.

**Why this file exists and is public.** `docs/` is a working lab notebook by decision (ADR-001
§Consequences). A programme whose stated claim to seriousness is that it reported its own failed
prediction cannot then quietly drop a paper that its own referee rejected on the day it was written.
The rejection is the more useful artifact.

---

## The finding that matters most: two contributions are not new

This is first because it is the one that changes what the paper can be, and because it was found by
an agent whose only job was to check whether an accusation was true.

### Contribution 5 — the Cournot damping result — is fully anticipated. WITHDRAWN.

The draft claimed as a sharpening that the damping stabilising Cournot tâtonnement satisfies
*d* < 4/(*n*+1) and therefore vanishes like 4/*n*. The chain of anticipation is complete:

| result | source |
|---|---|
| linearised gain (*n*−1)/2, asymptotic stability lost at *n* ≥ 3 | **Theocharis (1960)**, *RES* 27(2), 133–134 — and argued 20 years earlier by **Palander (1939)** |
| the required adjustment speed *falls* as *n* rises | **Fisher (1961)**, *RES* 28(2), 125–135, in his own words on p. 125: *"the tendency to instability does rise with the number of sellers for most of the processes considered"* |
| the bound ***d* < 4/(*N*+1)** itself | **Bischi, Chiarella, Kopel & Szidarovszky**, *Nonlinear Oligopolies* (Springer, 2010), Ch. 2, **eq. (2.26)**, where it is presented as routine |

The auditor could not obtain Fisher's primary text and says so rather than inferring; it does not
matter, because eq. (2.26) settles the bound whoever first wrote it. **This is a recapitulation, not
a contribution, and the ledger entry that recorded it as a result (WT-064) has been corrected rather
than deleted.**

Two corrections came with it. *"Unstable for *n* ≥ 3"* should be *"loses asymptotic stability for
*n* ≥ 3"* — at *n* = 3 the eigenvalue is exactly −1, giving undamped oscillation; strict instability
begins at *n* = 4. And the paper's gain expression was simply **wrong**: see Referee A's finding 4
below.

### Contribution 2 — the marginal pair — is Böhm-Bawerk (1889). ATTRIBUTION REQUIRED.

The draft claimed as a contribution *"the identification of the market-clearing interval with the
marginal pair, the S-th and (S+1)-th highest reservation prices."* The term is **Böhm-Bawerk's**,
and it is his verbatim (*Positive Theory of Capital*, Smart trans., Book IV Ch. IV, p. 209):

> *"If, finally, we substitute the short and significant name of **'Marginal Pairs'** for the
> detailed description of the four parties whose competition determines the price, we get this very
> simple formula: The market price is limited and determined by the subjective valuations of the two
> Marginal Pairs."*

The auditor did not stop at the term. It took Böhm-Bawerk's own horse market — ten buyers, eight
sellers, valuations listed on p. 203 — pooled the eighteen reservation prices, set *S* = 8, and
**evaluated this paper's formula against them**: 8th-highest 21.5, 9th-highest 21, and
*z*(*p*) = #{*mᵢ* > *p*} − *S* equal to +1 at 20.9, 0 throughout [21, 21.5), −1 at 21.6. Böhm-Bawerk's
stated price zone is **£21 to £21:10s.** The formula reproduces his answer to the shilling, 137 years
later, and the paper claimed it as new.

**One precision that is genuinely the paper's, and one that is a simplification.** Böhm-Bawerk's
object is *four* parties in *two* pairs — the last buyer and last seller who trade, and the first
excluded buyer and seller — which is why the term is plural. The pooled "*S*-th and (*S*+1)-th
highest reservation price" is a one-sided restatement that collapses the two pairs into one order
statistic, and that collapse is what the endowment-invariance makes possible. It is a real
simplification and it is not a new result.

**Shapley & Shubik (1971)**, *"The Assignment Game I: The Core"*, *IJGT* 1, 111–130, is the correct
modern citation. Their model *is* the unit-demand exchange economy with reservation prices; their §4
is titled **"The Horse Market of Böhm-Bawerk"** and reproduces his table; and their §5 establishes
that every core outcome is competitive. They name the bracketing agents explicitly. The paper cited
neither.

### What survives — stated at the strength the audit supports, which is not much

No source checked states the **invariance** half: that *z*(*p*) is invariant to *which agents hold
the units*. Coase (1960) gives allocation-invariance with no price and no excess-demand function, in
bilateral bargaining rather than a market. Gorman (1953) varies the distribution of *income* in a
smooth divisible-goods system that excludes indivisibilities, and the polar form usually attributed
to it is actually Gorman (1961). Böhm-Bawerk and Shapley–Shubik both take the buyer/seller partition
as exogenous data. So the five named sources do not displace it.

**That is not a novelty finding and must not be recorded as one.** The auditor's own warning is
adopted verbatim as the project's position: *"the observation is one short step from all four, it is
the obvious mechanism behind Coase invariance in unit-demand markets, and my search was targeted at
the five sources you named rather than at the unit-demand/mechanism-design literature where it is
plausibly folklore."* It names where to look next — **Gul & Stacchetti, Demange–Gale–Sotomayor, and
law-and-economics treatments of the Coase theorem in indivisible-goods markets** — and that search
is a precondition of any future draft, not an optional extra.

*Note the direction of the whole audit, because it is the opposite of wealthTensor-05's.* That
session's two provenance errors both pushed toward **deleting** a citation, and the lesson recorded
was that rigour which only subtracts is a bias with good manners. This audit pushed the other way:
it found **five works that should have been cited and were not**, in a paper carrying a 1,345-word
apparatus auditing its own bibliography. Referee B's sentence on this is the one worth keeping:
**"an apparatus this elaborate that misses Coase, Gorman, Böhm-Bawerk, Theocharis and Fisher is
auditing the wrong axis."**

---

## Referee B's FATAL findings on the argument

### F1 · The paper's central negative claim is false inside its own model

The abstract: *"the schedules cannot be perturbed independently because their difference does not
move."* §3.3: *"any perturbation of the allocation moves both in lockstep."*

**The second sentence is true and the first does not follow.** The theorem establishes invariance to
*reallocating units among agents whose reservation prices are held fixed* — which is not a demand
shift, not a supply shift, and not an operation any comparative static performs. Comparative statics
moves a schedule by changing preferences, income, substitute prices or costs, all of which change
*c*(*m*).

The referee demonstrated this with the paper's own module, unmodified, on the paper's own population:

- raise **non-holders'** valuations 20 %: the **supply schedule is unchanged at every one of the 399
  grid points**, demand rises by up to 44 units, clearing price 21.4802 → 24.5088;
- lower **holders'** valuations 20 %: the **demand schedule is unchanged at every grid point**,
  supply shifts by up to 41 units, clearing price 21.4802 → 20.1177.

So in this model one schedule *can* be shifted with the other held pointwise fixed, and the cross
then does exactly what the textbook says. **The paper proved that a perturbation nobody performs has
no effect, and labelled that the invalidity of comparative statics.**

This is also the answer to the strawman question §5 poses about itself. The draft did **not** escape
the trap it names; it renamed it. §5 abandons *"the diagram is invalid"* and substitutes *"the
operation on the diagram is invalid"*, which is a different false claim rather than a retreat to a
true one. And §3.1's *"a construction with this property is routinely perturbed one curve at a
time"* is asserted with **no citation of anyone doing it** — no textbook, no article, no applied
paper. *Announcing that you have avoided an error is not avoiding it.*

**Accepted in full.** This is the finding that makes the paper unsalvageable by editing.

### F2 · §3.4 breaks §3.1, and the single-seed reporting concealed it

§3.4 says *"The identity of §3.1 is untouched — this is a different c(m), not a different reading of
the same one."* That is a dodge, and the referee ran the numbers: the transform is
`m2[self.holders] *= loss_aversion`, so **the new c(m) is a function of the allocation.** Composed,
invariance fails:

| λ | distinct excess-demand schedules | distinct clearing intervals |
|---|---|---|
| 1.00 | 1 | 1 |
| 1.30 | **25** | **23** |
| 2.00 | **25** | **23** |

The paper's headline result fails the moment the paper's own behavioural extension is admitted. And
§3.4 is **the one result in §3 reported from a single allocation**, with the 25-allocation machinery
silently dropped exactly where it would have exposed this. **Accepted in full.**

### F3 · The volume decline is forced by construction, not predicted

*"a prediction the modeller does not control."* It is not: raising holders' valuations raises the
upper order statistics, raises the marginal pair, raises the clearing price, and volume
= #{non-holders with *m* > *p*} therefore falls. The referee tested four different increasing
transforms — multiplicative, additive, power, √-shift — and all four give a monotone decline. The
direction is an identity; the magnitude is conceded uncomparable by Limitation 5 while §3.4 keeps
the credit for the match. **Accepted.** Contribution 4 has no empirical content as written.

### F4 · "Exactly recovered" is a coincidence of two resolutions

The marginal-pair interval is 0.036665 wide; `marshallian_cross`'s default grid step is 0.018746.
The "exact recovery" has 1.96 grid points of slack. Holding *S*/*N* fixed and raising *N*, the
order-statistic gap shrinks like 1/*N* while the grid step grows:

| *N* | interval width | grid step | crosses inside |
|---|---|---|---|
| 400 | 0.036665 | 0.018746 | 25/25 |
| 1000 | 0.056690 | 0.022779 | 25/25 |
| 4000 | 0.004385 | 0.033558 | **0/25** |
| 20000 | 0.001961 | 0.056878 | **0/25** |

**And worse, the code does not do what §3.3 says.** `marshallian_cross` never reads the two schedules
separately — it scans for the first *p* with `excess_demand(p) <= 0`, i.e. it is *defined on the
difference*. So §3.3 verifies §3.1 by substituting §3.1 into itself. The two step functions
generically do not intersect at all; the code silently redefines "cross" as the zero of *z*, and the
paper reports the redefinition as a reduction result. **Accepted in full — this is circular as
written**, and `test_marshallian_cross_is_recovered_exactly` pins the coincidence rather than the
claim.

### F5 · Tautologies reported as measurements

`marginal_pair()` is `np.sort(self.m)[::-1]` indexed at *S* and *S*−1. **It never reads
`self.holders`.** So §3.2's row *"distinct clearing intervals across 25 allocations: 1"* reports that
`np.sort` returns the same answer when called 25 times on the same array, and §3.3's *"distinct
cross values: 1"* is a restatement of §3.1. **Accepted.** Only §3.1's 25/25/1 is substantive, because
`demand_at` and `supply_at` genuinely do read the allocation. The other rows are padding, and in a
paper whose §8 makes a virtue of nothing being transcribed, they are the wrong kind.

### F6 · The Lerner identity is baked in, in the precise sense the sentence denies

§4.3: *"a verification of the markup equation rather than an assumption baked into the solver."* The
FOC the solver enforces is *a* − *bQ* − *bqᵢ* − *cᵢ* = 0, i.e. *p* − *cᵢ* = *bqᵢ*. The code computes
`lerner = (p-c)/p` and `share/abs_elasticity = (q/Q)/(p/(bQ)) = b*q/p`. **These are the same
expression.** The residual is identically zero for any *q* satisfying the FOC; 1.1 × 10⁻¹⁶ measures
IEEE-754 rounding. **Accepted.** Likewise *"three independent solution routes"* are three numerical
methods for one linear system, so their agreement is a code check, not confirmation.

### F7 · The artifact designated as the paper's guarantor carried the error the paper disowns

§3.5 correctly says it is *tempting and wrong* to claim SMD "requires at least two goods", then
points at `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` as the mechanism
enforcing the limit. **That test's docstring said "SMD pathology needs at least two goods."** So did
`excess_demand.py`'s module header. So did the regeneration output the paper directs readers to.
**Three files carrying the error the paper identifies and disowns.** WT-057, and the sharpest
instance of it the project has produced: the paper was fixed and the artifacts it cites as its
guarantee were not. **Fixed in all three.**

### F8 · Self-grading, counted

Instructed to apply the programme's own rule — *a defence that recurs is a tell* — the referee
counted **24 distinct places** where the draft announces its own rigour rather than demonstrating
it, and then made the observation that actually stings: the structure is **identical in Paper II and
Paper III**. *"A defence that recurs across three papers is not a defence, it is a house style."*
**Accepted as a finding about the programme, not this draft**, and referred to Jason rather than
acted on unilaterally — the register is his.

---

## Referee A · every number checked against the code

The numeric pass came back **clean on every figure**: all of §2.2, §3.1–3.4, §4.1–4.3 match the
regeneration output at the stated precision, no numeral is stated with more precision than the
output supports, the script's output is byte-identical on re-run, every claim about what a named
test asserts is accurate, and script/test/paper configurations are identical seed for seed. It then
found eleven defects that the clean numbers concealed:

| # | Defect | Status |
|---|---|---|
| A1 | *"invariant at every price"* in §1, contribution 1 and the abstract's justifying clause **drops the tie caveat**. At *p* = *mⱼ* the tied agent is in neither part of the partition and *z* **is** allocation-dependent — verified at the paper's own interval endpoints: *z* = −1 for 16 of 25 allocations and 0 for 9. The caveat is necessary, and both endpoints of the clearing interval are tie prices. | accepted |
| A2 | §3.5's *"+249 to −150"* is **one allocation's** figure; across the 25, the minimum is 249 for 14 and 250 for 11, the maximum −150 for 13 and −149 for 12. Only 8 of 25 give the stated pair. Seed never named. | accepted |
| A3 | §3.4's volume table is allocation-specific (`default_rng(1)`) and **the seed appears nowhere in the paper**. Baseline volume ranges 85–103 across seeds; decline ranges 39.6–50.5 %. The abstract's *"93 → 49"* inherits this. | accepted |
| A4 | **§4.2's gain expression is wrong.** The damped Jacobian is (1−*d*)*I* + *dF* with *F* = −½(**11**ᵀ − *I*); eigenvalues 1 − *d*(*n*+1)/2 (multiplicity 1) **and 1 − *d*/2 (multiplicity *n*−1)**. The gain is the spectral radius, not the first term alone — at *n* = 4, *d* = 0.4 the paper's expression gives 0.0 against an actual radius of 0.8. The **stability condition survives** because 4/(*n*+1) ≤ 4/3 < 4 so the symmetric mode always binds first. Wrong in the paper, the module docstring and the new test's docstring. | **fixed in all three** |
| A5 | *"bracketing the prediction at every n"* is a **closed** bracket at *n* = 3 and 4, where 4/(*n*+1) lands exactly on a grid point and that *d* fails — correctly, since the gain is exactly 1 there. | fixed in the test |
| A6 | §4.3's *"agree to 10⁻⁶"* is **not produced by the regeneration script** and misstates the tolerance (1e-9 closed-form vs FOC; 1e-6 vs tâtonnement). It is transcribed from a test — the exact failure mode the script exists to prevent, in the paper that introduced the script. | accepted |
| A7–A9 | Three broken cross-references: §2.2 points at §7 for the regeneration command (it is §8); §3.5 points at §7 for the axis relation (it is §6, which the same paragraph then cites correctly); §1 says §5 records what the model class costs (§5 is *Abandoned approaches*; §6 does that) **and overstates §6, which explicitly declines the relaxation question.** | accepted |
| A10 | **`[II]` is listed and never cited** — in the paper whose own reference audit removed an entry for exactly that, one paragraph earlier. Two eponymous invocations still carry no year (Bouchaud/Farmer/Lillo, Godley and Lavoie). | accepted |
| A11 | *S* denotes both the stock and the supply schedule, colliding inside the paper's key line. | accepted |

### And the finding neither referee was looking for

§5's tie-convention story **misdescribes its own fix.** The paper says *"the grid now excludes any
point within 10⁻⁹ of a reservation price."* On the actual grid **that filter removes zero points** —
399 interior before, 399 after. The entire 4 → 1 correction came from dropping the two *endpoints*,
which are `M.min()` and `M.max()` and therefore data points. **The fix the paper credits is inert;
the fix that worked is not the one described.** In a section whose whole purpose is calibrating the
reader's trust in the author's self-reports, that is the worst available place for it. The same
error is in LEDGER WT-063 and has been corrected there.

---

## Disposition

**The mechanical defects are fixed** — A4, A5, F7, the arithmetic-only test guard (see below), and
the three files carrying the SMD wording the paper disowns.

**The paper is not.** F1 alone requires the central claim to be re-scoped from *"supply and demand
are not independent equations"* — which the title asserts and which F1 refutes inside the model — to
something much narrower and true: *the schedules are not independent **as functions of the
allocation**, and the allocation cancels from their difference.* That is a real statement. It is not
the paper that was written, and re-scoping it at the end of the session that received four FATAL
findings is exactly the move this project's doctrine warns against. **v0.1 stands in the repository
as written, marked superseded, with this report beside it.**

**A test that could not fail has been replaced.** `test_the_damping_that_rescues_tatonnement_shrinks_like_4_over_n`
closed with `assert 4.0/21 < 4.0/11 < 4.0/7 < 4.0/3` — a statement about four rational constants,
referencing no model output, incapable of failing. It now measures the largest converging damping at
*n* = 3, 6, 12, 24 and asserts that the measured boundary **falls**, and falls by more than 4× across
that range. §8's claim that two tests exist to make overclaiming fail loudly was, until this fix,
partly false.

---

## A note on method, since the audience for `docs/` includes people learning how this is done

**Three agents ran, and each found what the others structurally could not.** The one checking
numbers found every figure correct and eleven defects around them — a wrong eigenvalue expression, a
transcribed tolerance, three broken cross-references, two unstated seeds. The one trying to reject
found that the *argument* fails in the paper's own model, using the paper's own code to show it. The
one auditing priority found that two contributions were 65 and 137 years old. **No single reviewer
would have produced any two of those three sets**, and the numeric pass — the one that came back
cleanest — is the one whose cleanliness was most misleading.

**The sharper lesson, and it amends WT-054.** The standing rule was *two adversarial agents before
any preprint commits*. That is too late. Two results were found by writing the regeneration script,
**banked in the ledger as results, written into the paper, recorded in an ADR addendum and reported
to Jason as discoveries** — and then, in the same session, one turned out to be in a 2010 textbook as
a routine exercise and the other's headline gloss turned out to be refuted by three counterexamples
the referee produced in minutes. The gap between *finding* something and *believing* it was several
hours and four artifacts wide. See **WT-065**.

**And the thing worth being pleased about.** The apparatus worked. The paper was drafted, reviewed,
rejected and diagnosed inside one session, at a cost of a few minutes of agent time, and every
finding above arrived before a referee at a journal saw any of it. The failure mode this project
most fears is a flattering result surviving to publication; that has now failed to happen four times
in six sessions, each time by a different mechanism.
