# POSITIONING-002 · Paper III §9, second pass · **THE §9 WRITTEN FROM POSITIONING-001 DID NOT SURVIVE EITHER**

- **Supersedes** `POSITIONING-001-crash-risk.md` as the positioning of record for Paper III §9.
  POSITIONING-001 is not withdrawn — its four differentiators are still the right axes and two of
  them survive intact. What it lacked was one paragraph of Jin & Myers that it never reached, because
  it reached that paper through a retrieval pipeline and asked it the wrong question.
- **Written** 2026-08-11, session `wealthTensor-09`.
- **Status of §9 in the paper:** rewritten from POSITIONING-001 earlier this session, then demolished
  by its own adversarial pass within the hour. The rewrite's *facts* survive; its *positioning claim*
  does not. §9 is provisional pending §6 below.
- **Read this before touching Paper III §9 or §4.4.**
- **AMENDED 2026-08-11, session `wealthTensor-10`.** §6's table is rewritten with verified
  read-statuses — **three of the four unread items are now discharged.** The discharge found a
  fourth death for the paper's positioning claim and, in the same pass, a better one to replace it.
  **See §9, appended below.** §7 is CLOSED — Jason ruled 2026-08-11.

---

## 1 · The fact that killed it, and it was one page from the sentence we quote

Jin & Myers, NBER Working Paper 10453, pp. 4–5. **Verified character-by-character against the PDF by
`pdftotext` and `grep` — no model, no summariser, no retrieval layer anywhere in the loop:**

> "There is only one case where greater opaqueness does not reduce R2. The case is improbable but
> worth noting for completeness. Imagine an opaque firm run by a saintly manager who always acts in
> shareholders' interest, never taking a dollar more or less than deserved. That manager does not
> have to soak up any firm specific risk. All firm-specific good or bad news is absorbed by investors
> sooner or later, even if they cannot see the news as it happens.
>
> The properties of stock market returns in this case depend on how information is finally released.
> There are three possibilities. (1) If the saintly manager reports everything promptly and credibly,
> opaqueness is eliminated and returns are not affected. (2) Suppose that hidden news is revealed
> after a stable lag. Then the average amount of firm-specific information released in any period is
> the same as for a transparent firm. Average firm-specific variance and R2 are not affected by
> delayed reporting. (3) If a stable lag is implausible, think of good or bad news accumulating
> within the firm until the difference between intrinsic value and share price reaches a critical
> value. The news would then be released all at once, like a pressure vessel letting off steam. The
> releases would not affect average, long-run R2s, although we would see long tails in the
> distribution of stock returns. (We will control for kurtosis in our tests.)"

**A non-agency manager, accumulation to a critical threshold, release all at once.** §9 as rewritten
this morning positioned this paper as *"the non-agency generator of the same asymmetry."* That claim
is dead, and it died to a paragraph sitting one page before the sentence §9 quotes — in the same PDF,
which had been string-searched rather than read.

**This is the third framing this programme has lost to prior art in four sessions**, and the first one
it found itself before writing the claim down as a result. That is what WT-065 exists for and it is
the only consolation on offer.

---

## 2 · What survives case (3), read forensically rather than defensively

Four questions, each answered from the text and not from the shape of it.

**Is the saintly manager IGNORANT, or merely HONEST? — Honest, and fully informed.** "Saintly"
qualifies *capture*, not *information*: he never takes "a dollar more or less than deserved." The
giveaway is the following sentence — "even if **they** cannot see the news as it happens" — where
*they* is investors. The model's information structure is untouched: "The inside managers observe
both θ₁,t and θ₂,t, but outsiders only observe θ₁,t." **There is still an informed party holding the
wedge. §4 has none.** POSITIONING-001's differentiator 4 survives case (3) completely, and is now
carrying more weight than it was built for.

**Is the channel SYMMETRIC or ASYMMETRIC? — Symmetric, and stated twice.** "All firm-specific **good
or bad** news"; "think of **good or bad** news accumulating"; and the trigger is a two-sided threshold
on a signed quantity, "the **difference** between intrinsic value and share price."

**Does it produce SKEW or KURTOSIS? — Kurtosis, and they say so:** "we would see long tails in the
distribution of stock returns. (We will control for kurtosis in our tests.)" **Jin & Myers then use
kurtosis as a control variable in their crash regressions.** Their non-agency accumulate-and-release
channel is the nuisance term they partial *out* in order to identify the agency one. It is not a
crash mechanism in their hands; it is the thing standing in the way of measuring theirs.

**Is there an accounting layer? — None whatsoever.** Full-text counts in WP 10453:

| term | occurrences |
|---|---|
| `goodwill` | 0 |
| `intangible` | 0 |
| `impair` | 0 |
| `GAAP` | 0 |
| `asset class` | 0 |
| `book value` | 0 |
| `historical cost` | 0 |
| `historic cost` | 0 |

**And the footnote is better for us than the main text.** WP 10453 footnote 4, attached to "For
simplicity, we ignore depreciation and reinvestment": *"It is easy to introduce depreciation and
re-investment according to a pre-defined schedule. But discretionary investment would introduce
complications not modeled here."* A pre-defined schedule is common knowledge and enters value and
price identically, so it generates no wedge. **Jin & Myers concede the case that produces nothing and
explicitly decline the case that produces everything.** A referee reaching for footnote 4 to say they
handled depreciation has misread it.

---

## 3 · The larger casualty is not Jin & Myers — it is §4.4, and the owner is Bleck & Liu

**Bleck, A., & Liu, X. (2007). Market transparency and the accounting regime. *Journal of Accounting
Research*, 45(2), 229–256.** Verified by `pdftotext` on the author-hosted PDF, my own eyes on the
extracted text:

> "Historic cost accounting indeed stabilizes asset prices in the short term. **Under the veil of this
> apparent stability, volatility actually accumulates only to hit the market at a later date.** Put
> differently, historic cost accounting not only **transfers volatility across time** but also
> increases asset price volatility overall."

and, from the abstract:

> "historic cost accounting can make the financial market **more rather than less volatile**, which
> runs counter to conventional wisdom."

and, on the accumulation:

> "Failure of the shareholder to discriminate good from bad projects at an early stage allows bad
> projects to be kept alive and to potentially **worsen in quality over time**. The poor performance
> of these projects can thus **accumulate and only eventually materialize** at their final maturity,
> **leading to a crash in the asset price**."

**That is §4.4 — "volatility is not suppressed, it is relocated" — stated qualitatively in *JAR* in
2007.** §4.4 currently reads as a discovery. It is a φ-parameterised **quantification** of a
nineteen-year-old result, and the paper must say so.

**The separation is real but it is the whole separation, and it is one axis wide.** Bleck & Liu's
manager is strategic and fully informed — "the manager knows perfectly that the project will not
recover and may even worsen, he still prefers not to divest" — with a private benefit and a
gambling-for-resurrection payoff. The veil is *exploited*. §4 has no strategic actor and nothing to
exploit. There is also no observability parameter in Bleck & Liu: it is a discrete regime comparison,
historic cost against mark-to-market, and their crash arrives at a project's final maturity rather
than at a threshold crossing.

**This is the same axis that survives Jin & Myers, which is either reassuring or the last plank.**

---

## 4 · The correction that matters most: the asymmetry is ASSUMED, not DERIVED — and Basu is the ingredient, not the threat

POSITIONING-001 treated Basu (1997) as **Threat 1**, a conditional-conservatism result to be scoped
around. That is backwards.

Jin & Myers *derive* one-sidedness from symmetric primitives: absorption is bounded below because
capture is unbounded above ("The amount of good news absorbed is, in our model, potentially
unlimited. Insiders can hide good news simply by capturing the increased cash flows"). §4 does not
derive its asymmetry. It **assumes** a physical layer that only degrades.

And one-signed degradation in *levels* does not even deliver a one-signed *wedge*. If true capacity
declines at a stochastic rate around a booked rate, the reporting error is two-signed and §4 lands
back inside Jin & Myers' case (3), with a two-sided threshold and long tails rather than skew. What
makes the wedge one-signed is a **second** condition: that reported value may fall but may not rise.

**That condition is conditional conservatism.** It is ASC 350/360 — no upward revaluation of PP&E, no
impairment reversal for goodwill or indefinite-lived intangibles — and it is Basu's object.

> **The ratchet §4 relies on is not §4's device. It is the device Basu documented in 1997, and this
> programme was about to cite him as an obstacle to it.**

What is left to claim is narrower and, unlike the last two attempts, is a claim about *form* rather
than about priority: **that literature models conditional conservatism as a contemporaneous
asymmetric response coefficient — the Basu regression — and §4 models it as threshold-crossing
accumulation under a continuous observability parameter.** A response coefficient cannot express
recognition lag, jump magnitude, or where in a path the variance sits. That gap is real, it is small,
and it is honest.

---

## 5 · One adversarial over-reach, struck

The prosecution held that Jin & Myers' case (3) "predicted the failure of the registered prediction
in 2004," on the strength of case (2)'s "Average firm-specific variance and R2 are not affected by
delayed reporting."

**Struck, and struck on evidence I ran myself.** PRE-001 registered an ordering of *recognition lags
across GAAP asset classes* (PP&E < finite-lived intangibles < indefinite-lived intangibles <
goodwill). See the zero-hit table in §2: WP 10453 contains no accounting-recognition vocabulary at
all. Jin & Myers make claims about the R² and tail thickness of stock returns; they neither state nor
imply an ordering over asset classes. Their case (3) in fact *opens* by declining to resolve lag
structure — "If a stable lag is implausible" — so they could not have predicted the failure of a
prediction about lag, having declined to make one.

*Recorded because agreeing with an adversary is as much a failure as agreeing with oneself, and this
programme has now been wrong in both directions inside a single session.*

---

## 6 · **UNDISCHARGED — the reading list, with read-status attached to every entry**

**WT-059 applies and is NOT discharged. Nothing below enters Paper III until it is read at source by
the author.** Four of these reached this file through adversarial agents, which is a retrieval
pipeline wearing a better suit.

| work | why it matters | read-status |
|---|---|---|
| Jin & Myers, NBER WP 10453 (2004) | case (3); the quoted sentence; the zero-hit table | **FULL TEXT, verified by `pdftotext`+`grep`, own eyes** |
| Jin & Myers (2006), *JFE* 79(2) | the article of record | **NOT ACCESSED.** Paywalled. Whether case (3) survived revision is unknown |
| Bleck & Liu (2007), *JAR* 45(2) | owns §4.4's relocation result | **FULL TEXT, verified, own eyes** |
| Andreou, Lambertides & Magidou (2023), *BJM* 34(4) | the 5.5%→27% trend; the post-SOX nulls | **FULL TEXT, verified, own eyes** |
| Hutton, Marcus & Tehranian (2009), *JFE* 94(1) | OPAQUE; post-SOX dissipation | **ABSTRACT verified at source.** Body not read as typeset |
| Basu (1997), *JAE* 24(1) | supplies the one-way ratchet | **ABSTRACT ONLY** (author's own SSRN posting) |
| Beaver & Ryan (2000), *JAR* 38(1) | bias/lag decomposition | **ABSTRACT ONLY** |
| **Ryan (1995), *JAR* 33(1), 95–112** — *A model of accrual measurement with implications for the evolution of the book-to-market ratio* | may be **closer prior art than Beaver & Ryan (2000)** — a *model* where B&R (2000) is an empirical decomposition | **STILL NOT READ — and no legitimate open copy exists.** Bibliographic record verified four ways (JSTOR `10.2307/2491294`, RePEc, Crossref, Ryan's own NYU Stern CV). Unpaywall `closed`, zero repository copies, no working-paper predecessor — it **predates the accounting preprint era.** JSTOR read-online is the only route and it is Jason's; card issued 2026-08-11 (`~/Desktop/downloads/READING-CARD-ryan-1995.md`). **⚠ An ERRATUM exists that this project did not know about: *JAR* 33(2), p. 417, `10.2307/2491496`. Contents unknown.** ⚠ The "abstract" circulating for this paper is **indexer-manufactured** — *JAR* printed no abstracts in 1995. See §9.4. |
| Kim & Zhang (2016), *CAR* 33(1), 412–441 | conditional conservatism **lowers** crash risk — §4.2's comparative static, empirically supported | **FULL TEXT, verified by `pdftotext`+`grep`, own eyes.** Accepted manuscript, CORE `200253419`, md5 `6f5fc5f96ef554e59e135352bba10267`, 65 pp, ms-paginated 1–63 — **not** the 412–441 typesetting, so **✓⧗**. Deposited by SMU InK. Sample **1964–2007, 114,548 firm-years — confirmed.** See §9.2. |
| Kim, Wang & Zhang (2016), *CAR* 33(4), 1720–1749 | CEO overconfidence: a manager who genuinely misperceives — blocks loose use of "non-agency" | **FULL TEXT, verified by `pdftotext`+`grep`, own eyes.** Submitted version, CORE `200253418`, 49 pp, ms-paginated — **✓⧗**. **This is the paper that killed the positioning claim. See §9.1.** |
| Zhu (2016), *RAST* 21(2), 349–399 | accruals accumulate to a tipping point, release at once; agency-based | **ABSTRACT ONLY — and by necessity, not by laziness. ✓◐.** No legitimate open copy exists: Unpaywall `closed`, SSRN 2758880 states "Not Available for Download", no IDEALS deposit, not among the five working papers the author self-hosts. Abstract verified **verbatim and identical across three sources.** The agent-reported characterisation **held on the check**: "tipping point" is **Zhu's own phrase**, and the mechanism is explicitly *"managers' use of income-increasing accrual estimates to hoard bad news."* Distinguishes cheaply; string cite only; **no absence claim may rest on it.** |
| Bushman & Williams (2015), *JAR* 53(3) | delayed expected-loss recognition | **BIBLIOGRAPHIC ONLY** |
| Gorton & Ordoñez (2014), *AER* | symmetric ignorance, wedge grows with time, threshold, discontinuous collapse | agent-verified as **two-sided** (collateral reverts up as well as down) — a structural rhyme, **not prior art**. Not read by the author |
| Zeira (1999), *JME* | informational overshooting | has a **boom phase** §4 does not have. Judged padding. Not read by the author |

**The two that could still change a verdict:** Ryan (1995), which may displace Beaver & Ryan (2000)
as closest prior art to the filter; and Kim & Zhang (2016), which may already have tested §4.2's
comparative static and found it.

---

## 7 · ~~OPEN~~ **CLOSED 2026-08-11 — Jason ruled: BOTH, conservatism primary, crash risk secondary**

> **The ruling.** §9 leads with conservatism-as-a-dynamic-system and retains a shorter crash-risk
> subsection positioning against Jin & Myers, Bleck & Liu, Kim & Zhang and Kim/Wang/Zhang.
> Longer §9, but it does not abandon the readers who arrive by the crash-risk keyword.
>
> **§9.1 below makes this ruling look better than it did when it was made.** The crash-risk
> subsection is no longer a priority fight the paper loses; it is a three-way disambiguation the
> paper wins, because the crash-risk literature turns out to have carved the space and left exactly
> one cell empty. See the grid.

*The original recommendation is retained below, unedited, because the reasoning is still the
reasoning even though the verdict went one step further than it asked for.*

**Recommendation was: move it from crash risk to conservatism and measurement.**

The crash-risk literature is crowded, empirical, and agency-dominated. Paper III is theory-only, with
two failed registrations, and §9 concedes it is "much the weaker of the two accounts" on evidence.
It loses there, and it will keep losing there, because the axis of competition is panel evidence and
this paper has none.

The conservatism/measurement literature is where the surviving claim in §4 above is strongest — a
genuine modelling gap rather than a priority contest — and where a failed asset-class prediction is a
normal open question rather than a refutation.

**This is a repositioning of the paper and not an edit to §9, so it is not taken unilaterally.**

---

## 8 · Method note, recorded because the method is the deliverable

Three adversarial agents ran (WT-070): a prosecution, a priority audit prompted per L28 to state what
it could not access, and a defence attorney. **The defence attorney did the most damage for the third
consecutive session** — it supplied the assumed-not-derived correction of §4, identified Bleck & Liu
as the real threat where the prosecution had buried it in a list, and caught the prosecution's
over-reach in §5.

**Two of the three agents' most damaging claims were then verified by the author, mechanically,
against source PDFs, before any of this was written down.** Both held. Four other claims were not
verified and are marked as such in §6, and none of them appears in the paper.

*The prosecution's prompt ended with a paste marker and no pasted section — it never received §9's
text and said so, then landed the session's fatal hit from the summary alone. The defect is recorded
because the lesson is not "check your prompts": it is that a hit available from a two-line summary was
a hit available to any referee who had read the source at all.*

---
---

# 9 · **ADDENDUM, session `wealthTensor-10`, 2026-08-11 — what the §6 discharge found**

*Three of the four unread items are now read at source. Everything below was verified by
`pdftotext` + `grep` on PDFs downloaded and hashed by this session — no agent, no summariser, no
retrieval layer in the loop for any quoted sentence. Four adversarial research agents located the
sources; **not one of their content claims entered this document without being re-run by hand.***

## 9.1 · The positioning claim died a fourth time, and its killer is the paper that saves it

**Kim, J.-B., Wang, Z., & Zhang, L. (2016). CEO overconfidence and stock price crash risk.
*Contemporary Accounting Research* 33(4), 1720–1749.** Read in the SMU InK submitted version
(CORE `200253418`, 49 pp, ms-paginated — hence **✓⧗**). Manuscript p. 9, verbatim:

> "It is important to first stress that our hypothesis **does not depend on the existence of any
> rational moral hazard behavior**, such as empire building, stealing, or other types of private
> interest seeking. Instead, we are concerned with situations where **the interests of the manager
> and outside investors are perfectly aligned.**"

and, from their conclusion:

> "The poor performance of these bad projects will **accumulate and eventually materialize** at their
> final maturity, leading to a market crash of the stock price."

**A published crash mechanism that explicitly disclaims agency, with accumulation and release.**
Any §9 that calls this paper "the non-agency generator of the same asymmetry" is dead on arrival.
*That is the third framing this programme has lost to prior art in five sessions, and the second
found by us before it was written down.*

## 9.2 · What replaces it, and the axis was never the one we were arguing about

Read together, the five crash-risk papers carve a grid and leave **exactly one cell empty.**

| | manager's beliefs | manager's incentives | **where the wedge lives** |
|---|---|---|---|
| Jin & Myers (2004/06) | correct | capture | in the **incentive** |
| Bleck & Liu (2007) | correct — *"unbiased estimates of the projects' intrinsic value"* | private benefit | in the **incentive** (+ regime) |
| Zhu (2016) | correct | hoarding via accrual estimates | in the **incentive** |
| Kim & Zhang (2016) | correct | hoarding | in the **incentive** |
| Kim, Wang & Zhang (2016) | **wrong** | **aligned** | in the **manager's head** |
| **§4** | **correct** | **aligned** | **in the measurement rule** |

**The axis was never *agency vs. non-agency*.** Kim/Wang/Zhang own non-agency and say so in terms.
The axis is **where the wedge lives**, and there are three places, not two: an incentive, a belief,
or the rule that computes the number. Everyone else takes the first two. §4 takes the third —
nobody is mistaken, nobody is concealing, and the gap opens anyway because of how the reported value
is *required* to be computed.

**This is a claim about form, it is narrower than what died, and unlike the last three attempts it
is verified rather than asserted.**

*Kim, Wang & Zhang hand us the template for making the move.* They distinguish themselves from
Bleck & Liu on precisely this axis, at manuscript p. 9: *"in the Bleck–Liu model, managers are
rational, in the sense that they have unbiased estimates of the projects' intrinsic value and keep
the bad projects to derive more private benefits."* §9 performs the same operation one column
further along, and cites them while doing it.

**⚠ The honest weakness, stated here so §9 must deal with it.** KWZ's overconfident CEO *does*
privately observe negative feedback and *is* "reluctant to release" it — the authors write that
overconfidence "can lead to bad news hoarding." So their channel routes through concealment even
though it does not originate there. §4 must therefore distinguish on **origin**, not on outcome:
in KWZ, fix the CEO's beliefs and the wedge vanishes; in §4, give everyone correct beliefs and the
wedge remains, because it is in the reported number rather than in anyone's head.

## 9.3 · Kim & Zhang (2016) — the corroboration and the ceiling, both confirmed against the text

Read in the SMU InK accepted manuscript (CORE `200253419`, md5
`6f5fc5f96ef554e59e135352bba10267`, 65 pp, ms-paginated 1–63 — **✓⧗**).

**The accumulate-to-threshold-then-release story is in their introduction, in prose, and nowhere in
their measurement.** Manuscript p. 1: *"Once the amount of accumulated bad news reaches a certain
threshold, it will be released all at once, leading to stock price crashes."* Manuscript p. 5:
*"When the accumulated bad news reaches a certain tipping point…"*

Severity witness — full-text counts over the extracted manuscript, run by this session:

| term | count | | term | count |
|---|---|---|---|---|
| `threshold` | **1** | | `goodwill` | 0 |
| `tipping point` | **1** | | `impair` | 0 |
| `unrecognized` | 0 | | `intangible` | 0 |
| `recognition lag` | 0 | | `useful life` | 0 |
| `asset class` | 0 | | `historical cost` | 0 |
| `write-down` / `write-off` | 0 | | `fair value` | 0 |

Controls fire correctly: `conservatism` 185, `crash` 252, `Basu` 45, `accrual` 21, `hoard` 5.
And `unconditional` appears **exactly twice in 63 pages** — once in footnote 1 as a definitional
contrast, once as the label "Unconditional Crash Probability = 12%", which is a base rate and not a
construct. **Only conditional conservatism is measured; the paper cannot and does not speak to
unconditional.**

**So the gap §4 claims is real and now demonstrated rather than asserted:** they model conservatism
as a contemporaneous asymmetric response coefficient — Basu, Ball–Shivakumar, Khan–Watts `CSCORE` —
and assert accumulation in the prose. There is no stock variable, no accumulated-unrecognised-loss
reserve, and no threshold parameter anywhere in the paper.

**And the direction is corroboration, which this framework has never had before.** Conditional
conservatism is significantly and negatively associated with future crash risk, 114,548 firm-years,
1964–2007. That is §4.2's comparative static, empirically supported by somebody else. **Handle both
halves: it is simultaneously the best external support the programme has ever received and a ceiling
on how novel §4.2 may claim to be.**

*One item §9 must not round off:* their Table 10 extends the forecast window to 2 and 3 years and
finds predictive power **increases** with window length, which they read as *"the hidden bad news of
less conservative firms is more likely to materialize in longer terms."* That is the closest their
**empirics** come to an accumulation story, it is offered as a tentative "may suggest", and it is the
single most useful sentence in the paper for us.

## 9.4 · Ryan (1995) — still undischarged, and it came with two surprises

**No legitimate open copy exists.** Unpaywall `closed`; zero repository copies; no working-paper
predecessor — the article **predates the accounting preprint era.** JSTOR is the only route and it is
the author's to walk. Bibliographic record verified four ways.

1. **⚠ An erratum exists that this project did not know about.** *JAR* 33(2), Autumn 1995, p. 417,
   `10.2307/2491496`. Contents unknown. **If Ryan (1995) is ever cited here, the erratum is cited
   with it.**
2. **⚠ The "abstract" circulating for Ryan (1995) is manufactured by an indexer.** *JAR* printed no
   abstracts in 1995. What OpenAlex serves is assembled from Microsoft Academic Graph metadata and
   visibly restarts its own framing mid-way — abstract text welded to opening-paragraph text.
   Semantic Scholar declines to serve one at all. **Nothing in this document rests on it.**

   *This is the phantom tag in a fourth medium: an abstract credited to a paper that never had one.
   See `METHOD-001` §5 and `REFERENCE-POLICY` §6.*

## 9.5 · Zhu (2016) — the check came back agreeing, and that is recorded too

The agent was instructed that *a confirmation of what I told you is more suspicious than a
contradiction.* It confirmed anyway, and it was right to. "Tipping point" is **Zhu's own phrase**,
from his own published abstract, and the mechanism is explicitly *"managers' use of income-increasing
accrual estimates to hoard bad news"* — which cannot operate with nobody informed. Agency, cheap to
distinguish, string cite. **✓◐** — abstract only, by necessity: no legitimate open copy exists.

*Recorded because §5 of this document records an adversary struck for over-reaching, and a file that
only ever records the adversary being wrong is not a record, it is a defence.*

## 9.6 · What remains before §9 can be called final

1. **Ryan (1995) + its erratum** — Jason's read; card issued; seven questions, of which
   **Q2 (is the measurement error one-signed or two-signed?) decides whether §4's ratchet is a
   distinct object.**
2. **Beaver & Ryan (2000)** — §9 names it closest prior art **on an abstract.** If Ryan (1995)
   displaces it, we will have displaced something we never read.
3. **Basu (1997)** — §4's ratchet *is* his object, and this project has never read him. Closed
   everywhere; the author route is the play.

*Nothing in §9.1–§9.3 is contingent on those three. Nothing in §9.1–§9.3 may be written as final
until they are resolved.*
