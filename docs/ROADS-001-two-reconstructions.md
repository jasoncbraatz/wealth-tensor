# TWO ROADS · a co-author's memo, not a report
### `wealthTensor-10`, 2026-08-12 · written by hand, no agents, no ranked findings

*You asked for B+A+C. Here are two of them — one per paper. Each is a **different paper built from
material we already have and have already verified**, not a repair list. For each: the central
claim, the spine, what it costs, what it buys, and what has to be computed before it is true.*

*I am going to tell you which one I would co-write, and why, at the end. The prose is yours to
burn; the moves are what I am handing you.*

---

# ROAD ONE · PAPER II
## *Everything in this paper is about the shape of the levy's bite, not its size.*

### The move

Right now the paper's thesis is **"the base sets a ceiling"** and its mechanism is **κ**. Both are
refuted by its own table. So stop defending them — and notice what is left standing when you take
them out, because it is a better paper and it is *already written, in the wrong order.*

Line up all five findings, including the two you think are failures:

| finding | what the levy does to the growth multiplier *A* |
|---|---|
| stock levy compresses | **scales** *A* — cuts E[log A], leaves Var[log A] alone |
| flow levy compresses more at equal κ | **truncates** *A*'s upper tail — cuts **both** |
| ρ does nothing at zero | doesn't change *A*'s **shape** at all — it is a rate reparameterisation |
| a 0.25× threshold is free | exempts the bottom, never touches the **tail**, so never touches the tail index |
| periodicity is ~neutral once compounding-matched | changes **when**, not **shape** |

**Five results. One principle. Say it once:**

> **A redistributive levy changes a wealth distribution only insofar as it changes the *shape* of the
> growth multiplier's distribution. Everything that alters only how much is collected — the rate, the
> realisation share, the assessment period, the exemption threshold — is trim. What is structural is
> whether the levy SCALES the multiplier or TRUNCATES it.**

### Why this is B+A+C and not a patch

**Your two embarrassments become confirmations, honestly, with no reframing sleight of hand.**

- **ρ = 0.** Under the current thesis this is a tautology you got caught publishing. Under the new
  one, ρ is a coordinate that provably cannot change *A*'s shape, and the framework **predicts in
  advance that it can do nothing** — and then it does nothing. That is a passed test, not a caught
  error. *The tautology was only embarrassing because it was being sold as a discovery. As a
  prediction of a general principle it is a clean instance.*
- **The free threshold.** Currently filed under "trim" and apologised for. Under the new thesis it is
  the sharpest instance in the paper: remove a quarter of the budget and lose nothing measurable,
  **because you removed it from the part of the distribution that does not set the tail.**
- **The periodicity result** stops needing its causal story ("catches dispersion that has had time to
  accumulate," which is wrong) and becomes the third confirmation: timing is not shape.
- **And "the base sets a ceiling" doesn't get retracted — it gets *explained*.** The bases occupy
  nested regions because scaling and truncation are different operations on *A*, not because one base
  is intrinsically stronger. §3.1's half-failure paragraph, which you already wrote, becomes the
  moment the paper finds its actual thesis. **You wrote the discovery and filed it as a disappointment.**

### The spine

| § | |
|---|---|
| **1** | A levy is an operator on the growth multiplier. Two things a levy can do to a random variable: scale it, or truncate it. The distinction is not about money collected. |
| **2** | The model. Four coordinates + the rebate rule as a fifth (it is one, and pinning it at per-capita is a choice). Kesten form stated explicitly: *x′ = A·x + κ*. |
| **3** | **The headline: at matched budget the base ranking reverses.** κ = 0.1000 → Gini 0.222; κ = 0.1026 → Gini **0.125**. Then the tail index from E[*A*^α] = 1, and the fact that at *r* = 1 the flow levy caps *A* below 1 so **no power-law tail exists at all.** |
| **4** | **Trim: three coordinates that cannot matter, and don't.** ρ, threshold, periodicity — each with the shape argument first and the number second. |
| **5** | κ, exactly. κ_flow = r·E[η⁺]/(1+μ+a/w̄), agreeing under 1%. Named as the wealth-tax/income-tax conversion it is, and *then* the interesting part: **κ is the budget, and the budget does not determine the outcome.** |
| **6** | What was tested and survived. *(See the ledger below — this section does not currently exist and it is the biggest single omission.)* |
| **7** | Abandoned approaches — including "the base sets a ceiling regardless of rate," in the body, in full. |
| **8** | Limitations. |

### The sentence I would put in the abstract

> **At equal revenue, a levy contingent on the realised gain compresses a wealth distribution
> substantially more than a proportional levy on the stock — 0.125 against 0.222 at κ ≈ 0.10 — because
> it truncates the growth multiplier's upper tail where the stock levy merely scales it. The
> compressive budget is therefore not the mechanism: two levies moving the same share of aggregate
> wealth per assessment can differ by half in the stationary Gini.**

*That is counterintuitive, it reverses the standard wealth-tax-is-stronger prior, and it is a fact
about your model that as far as I can find nobody has stated.*

### What must be computed before a word of it is true

**WT-053, and I am not going to pretend otherwise. None of the tail-index material is run.**

1. Root-find α from E[*A*^α] = 1 for both levy types across the sweep. This is the theorem.
2. The matched-κ sweep, with seed counts and dispersion on every row.
3. Confirm the *r* = 1 flow levy caps *A* < 1 — i.e. that the power law genuinely vanishes rather than
   becoming very steep. **This is the strongest claim and the one most likely to be wrong.**
4. Compounding-matched periodicity rerun with 1 − (1−r)^P.
5. The κ denominator fix, and tighten the test from 5% to 1%.
6. A proportional-rebate row, to show the rebate rule is a real fifth coordinate.
7. ρ = 0 exactness, including where the `min(rate·liable, w)` clamp bites.

**Two days of honest work and the paper is a different animal.**

### What I could not check and you should

Whether the truncation-versus-scaling effect on the tail index is already known. The
optimal-taxation-with-Pareto-tails literature is where it would live. **This is the single search I
would run before writing, precisely because it is the thing I am telling you to lead with.**

---

# ROAD TWO · PAPER III
## *Limitation 4 is not a limitation. It is the paper.*

### The move

Every fatal finding in the teardown — no price variable, no agent, no equilibrium, no asymmetry in
the recursions, the measurement-rule cell possibly empty — **attacks the crash story.** Not one of
them touches the filter.

So take the crash story out. **Not because it's wrong — because it isn't ready, and there are 209
more papers behind this one.**

What remains is this, from Limitation 4, currently buried on page 40 of your own document:

> **φ reaches the observable only through the product φδ. Recovering the timeliness parameter
> requires dividing by an estimated decay rate, and the variance of the estimate grows like 1/δ².**

That is a **non-identification result**, and — this is the part that makes it a paper — **it is not
about your framework.** It is about *any* attempt to recover reporting timeliness from a reported
series. Which is what the entire conditional-conservatism measurement literature does:

- **the Basu (1997) asymmetric-timeliness coefficient**
- **Khan & Watts (2009) C_Score**
- **Ball & Shivakumar (2006) accrual–cash-flow piecewise measure**
- **Givoly & Hayn (2000) accumulated negative accruals**
- **Bushman & Williams (2015) DELR**

**If timeliness enters the observable only in product with asset durability, then every one of those
measures is mechanically confounded with industry asset life, for reasons having nothing to do with
conservatism.** That is a checkable, falsifiable, cross-sectional prediction about the field's own
instruments — and you measured the effect at **291×** in your own simulations.

### Why the failed pre-registration becomes the paper's best illustration

**And here is the part I want you to sit with, because it is the nicest thing in either road.**

PRE-001 and PRE-002 ordered recognition lag across GAAP asset classes — PP&E, finite-lived
intangibles, indefinite-lived intangibles, goodwill. Those classes differ in φ *and they differ in δ*:
a distribution centre and a software platform do not degrade at the same rate, and goodwill has no
degradation rate at all.

**The test was confounded in exactly the way the theorem says it must be. §4.2 says so — 0, 16 and
100 recognition events at δ = 0.01, 0.05, 0.20 with φ held fixed — and it says so on the page before
the test.**

So the honest sentence, and it is honest:

> *The confound was derivable from §4.2 before the registration was written, and was not derived. That
> is a finding about this programme's process, recorded in §6. It is also the cleanest available
> illustration of the identification result: a design that varies φ across classes whose δ also varies
> cannot recover φ, and did not.*

**You do not get to say the theory was right. You do get to say the null is exactly what the theorem
predicts, and that you should have known.** That is a stronger position than either "the theory
failed" or "the bridge failed," and it is the only one of the three that is *load-bearing*.

### The spine

| § | |
|---|---|
| **1** | A balance sheet is an instrument with a transfer function. *(Your opening line, unchanged — it is the best sentence in the corpus.)* |
| **2** | The filter. E, C, gap, φ, α, θ, δ. Two recursions. No prices, no agents, **and say so up front as a scope statement rather than a limitation.** |
| **3** | Dimensional hygiene and the invariance sweep. Shortened; it earns its place as evidence the instrument is sound, not as a result. |
| **4** | **D(φ) = (1−φ)·D(0)**, the closed form. Inter-event smoothing and event concentration as two statistics rather than one. |
| **5** | **THE THEOREM. φ reaches the observable only as φδ.** Consequences for C_Score, Basu, Givoly–Hayn, DELR. The 1/δ² variance. The 291× measured effect. |
| **6** | **The registered test, and why the theorem predicted it would be uninformative.** All of §5 as written, all of §6.2's bridge-proposition discipline, nothing removed. |
| **7** | What survived. *(New — the ledger.)* |
| **8** | Abandoned approaches, in the body, including **the crash-risk framing, in full, with the three-cell taxonomy and the priority concessions.** |
| **9** | Limitations. |

**Note what §8 does: the entire crash-risk section, Jin & Myers, Bleck & Liu, Kim & Zhang, the
saintly manager, the wedge-lives-in-three-places grid — none of it is deleted.** It moves to
*Abandoned Approaches*, where it is a genuine contribution to the section rather than a claim the
paper cannot yet support. **It also becomes the trailer for the paper that follows it**, which is
exactly what a corpus of 210 wants.

### The abstract sentence

> **A reporting layer that recognises a share φ of physical degradation on arrival and defers the
> remainder to a threshold crossing produces an unrecognised-loss overhang whose integral is exactly
> (1 − φ) times its value at φ = 0. The parameter reaches any observable series only in product with
> the degradation rate δ, so timeliness and durability are not separately identified from reported
> numbers: recovering φ requires dividing by an estimated δ, and the estimator's variance grows like
> 1/δ². A pre-registered test of a lag ordering across GAAP asset classes, registered and replicated,
> returned a null — which is what the identification result predicts for any design that varies φ
> across classes whose δ also varies. That confound was derivable before the test was run and was not
> derived; §6 states the discipline that would have caught it.**

Nothing hidden. Nothing overclaimed. **And a reader finishes it knowing what you found.**

### Titles

1. **"Timeliness and durability are not separately identified from a reported series"** — flat,
   accurate, sounds like an accounting theory paper, will be cited by people who never read §2.
2. **"You cannot read a recognition lag off a balance sheet"** — has a pulse, still exact, and it is
   a claim rather than a topic.
3. *"The φδ problem"* — only once someone else has named it that.

**Drop "tensor."** It is in the title, the keywords and the repo name, and appears once in the body
saying it isn't the claim.

### What this costs

- **You do not ship the crash paper this year.** That is the real price and I will not dress it up.
- Basu still needs reading, but for §5 rather than as load-bearing machinery — the identification
  result stands whether or not Basu's coefficient is the right statistic. *It stands more strongly if
  it is.*
- Beaver & Ryan (2005) still needs reading before you write §5's related work.

### What it buys

- **Every fatal finding in the teardown is answered by removal rather than repair.** No price
  equation, no ratchet, no behavioural limb, no equilibrium.
- The paper is **shorter, sharper, and about the field's instruments rather than about wealth**, which
  is a much larger and much less crowded audience.
- **A theory-only paper with a formal identification result and a registered null is a completely
  normal object in accounting.** A theory-only paper making a crash-risk priority claim is not.
- And it makes Paper IV, or Paper V, the crash paper — written properly, with a price line, after
  Basu and Beaver & Ryan are read.

---

# THE LEDGER BOTH ROADS NEED, AND NEITHER PAPER HAS

You report every test you ran and never report what survived one. Here is the section, drafted, for
Paper III. **Write the Paper II version the same way.**

> ## What was tested and survived
>
> *This section exists because a paper that reports only its failures gives a reader no way to weigh
> them.*
>
> | claim | test | what would have killed it | outcome |
> |---|---|---|---|
> | D(φ) = (1−φ)·D(0) | closed form against simulation | any φ where the ratio departs from (1−φ) | held to 10⁻¹⁵ |
> | Results are dimensionless | η swept over **twelve orders of magnitude** | any dimensionless output moving with η | spread exactly 0.0 |
> | …and not because η is unused | mutation testing (WT-069) | a mutant that leaves results unchanged | **every substituted vacuous witness killed its run** |
> | Recognition frequency is driven by δ | sweep at fixed φ | δ having no effect | 0 → 16 → 100 events |
> | The tier instrument has no baked-in ordering | **label permutation** | a non-null under randomised labels | z-mean **+0.007**, sd 1.025 |
> | The registered design had power | power analysis reported whatever the outcome | power too low to interpret a null | 0.95–1.00, with three qualifications stating why that is an upper bound |
> | The framework's guards can fail | six documented instances of guards that *could not* fail, found and retired | — | found by us, before publication, and recorded in `METHOD-001` |

**That last row is the one nobody else in your field can write.** Not "we were careful" — *"we ran a
guard-audit against our own guards, it found six, here they are."*

---

# ON FUN, SINCE YOU RAISED IT AND SINCE IT IS LOAD-BEARING

The papers are not dour because economics prose is dour. **Coase is funny.** *The Problem of Social
Cost* has jokes in it. Sraffa is dry and arch on purpose. Akerlof's lemons paper is playful about
used cars and won a Nobel. There is a long, respectable tradition of economics papers that are a
pleasure to read, and it is not in tension with rigour — it is a *signal* of rigour, because only
someone comfortable with their result relaxes enough to be witty about it.

What made your drafts grim was never the humour deficit. It was that **every confident sentence had
an apology stapled to it.** Take the apologies off and the wit comes back on its own — it is
already there in the source material:

- *"A balance sheet is not a window. It is an instrument, and instruments have transfer functions."*
- *"Two quantities can share dimensions and remain different quantities."*
- *"A test that cannot fail is not a test."*
- *"An argument is easier to judge when its objections are in the room."*

**Those are all yours, all in the current drafts, and all excellent.** Not one of them needed a
disclaimer and not one of them has one. That is the register. It was never missing — it was just
outnumbered.

---

# WHICH ONE I WOULD CO-WRITE

**Road Two, and I would start it this week.**

Road One is a better *result* — the truncation-versus-scaling theorem is more surprising and it
reverses a standing prior. But it is unrun, it may be known, and it needs two days of computation
before anyone can say whether it is true.

Road Two is already true. **The φδ non-identification result is derived, measured at 291×, and sitting
in a limitations section.** It needs no new code, no price equation, no reading you have not already
queued, and it converts a failed pre-registration from a wound into the theorem's own worked example.
It is a small, hard, correct paper that an accounting journal would recognise on sight — and it is
about *their instruments*, which is how an outsider gets read.

**And it is the right paper 1 of 210.** It says: *this person found something narrow and true, tested
it hard, told you exactly where it broke, and did not oversell a syllable.* Every door you described —
the podcasters, the thought-leadership, the eleven-year line from macro through accounting to CS —
opens wider on that than on a big claim with a concession section.

Road One goes next, after the tail index is computed. It is a genuinely good paper and it should not
be rushed into being a wrong one.

---

*Written by hand. Nothing in the two spines requires a result you do not already have, except the
tail-index computation in Road One, which is flagged in every place it appears.*

*You will rewrite all of it and you should. The moves are the deliverable; the prose is scaffolding.* ⚒️
