# POSITIONING-001 · Paper III §9 versus the crash-risk literature · **READ, at last**

> ## ⚠ SUPERSEDED 2026-08-11 (wealthTensor-09) by `POSITIONING-002-second-pass.md`. **READ THAT FIRST.**
>
> This file is kept because its four differentiating axes are still the right axes and two of them
> survive. Three things in it are now known to be wrong or incomplete, and each is marked in place
> below rather than silently edited away:
>
> 1. **The central positioning claim it recommends — "the non-agency generator of the same
>    asymmetry" — is dead.** Jin & Myers' own working paper, pp. 4–5, contains a *saintly manager*
>    case in which news accumulates to a critical threshold and is "released all at once, like a
>    pressure vessel letting off steam." Non-agency accumulate-and-release was published in 2004,
>    one page before the sentence this file quotes. **This file reached that PDF by string search.**
> 2. **Basu is inverted.** §3 below calls conditional conservatism *Threat 1*. It is not a threat;
>    it is the one-way ratchet §4's asymmetry silently depends on. See POSITIONING-002 §4.
> 3. **The §4.4 volatility-relocation result was already published** — Bleck & Liu (2007, *JAR*).
>    This file did not look for it, because it searched the crash-risk literature and not the
>    accounting-measurement one.
>
> *Two quotation defects were also found and are corrected in place below. Both were introduced by
> the retrieval pipeline this file's own §5 warned about, which is the entire argument for WT-059
> arriving as a receipt rather than as a resolution.*

- **Status of the item before this session:** deferred in wealthTensor-06 AND -07. §9 positioned
  against Jin & Myers and Hutton–Marcus–Tehranian **from a search, not from reading them.**
- **Status now:** both read in full text (see §5 for exactly which versions). **§9 does not survive
  as written.** What replaces it is narrower, true, and has a better empirical hook.
- **Read this before touching Paper III §9.**

---

## 1 · Jin & Myers (2006) is our thesis, sentence for sentence, and we must concede it

The accumulate-buffer-then-release-with-severity-scaling-in-opacity structure **is theirs.** Verbatim
from the model:

> "The more opaque the firm, the greater the amount of hidden, firm-specific bad news that may arrive
> in a given span of time. The amount of bad news that insiders are willing to absorb is limited."

> "But if a sufficiently long run of bad firm-specific news is encountered, insiders give up, and all
> the bad news comes out at once."

> "Therefore we predict a greater frequency of large, negative, firm-specific return outliers in
> countries where firms are less transparent to outside investors."

Their opacity is a variance ratio, η = Var(θ₁)/[Var(θ₁)+Var(θ₂)], where outsiders see θ₁ only. Line
that up against our claim component acting as a low-pass filter on the physical one, with lag and
severity scaling in unobservability, and a referee reading only the two abstracts will say we have
restated Jin & Myers with a physics vocabulary. **That is what got the programme demolished twice and
it would be earned a third time.**

**And they already net out the up-tail.** Their COUNT measure subtracts upside frequencies from
downside frequencies; COLLAR shorts a call against a put. The crash-not-jump asymmetry is theirs too.

---

## 2 · Four places we genuinely differ, in descending order of strength

**1 · Their asymmetry generator is not ours, and they say so themselves.**

> "But why should insiders absorb any firm-specific risk on the downside? Why don't they hide the
> upside and reveal the downside? The answer, of course, is that insiders would always report bad
> news."

> "The amount of good news absorbed is, in our model, potentially unlimited."

Their crash asymmetry is **finite insider wealth plus an abandonment option** — a limited-liability
boundary. Not an observability asymmetry. Ours is a different mechanism producing the same sign, and
"same prediction, nicer story" loses unless we produce a prediction that separates them.

**2 · There is no physical layer in their model at all.** Verbatim: *"For simplicity, we ignore
depreciation and reinvestment."* θ₂ is a cash-flow **innovation** — an information object, not a
decaying asset. No capital stock, no degradation, no maintenance.

**3 · Neither paper gives the accounting layer any dynamics.** η is a static variance ratio.
Hutton–Marcus–Tehranian's OPAQUE is a three-year rolling sum of |discretionary accruals| — a
cross-sectional regressor with no state, no reversal, no interaction with anything physical. **The
accounting layer as an object with its own laws is open ground with respect to these two papers.**

**4 · The epistemic difference is real. Both papers' managers know everything.** Jin & Myers:
*"The inside managers observe both θ₁,t and θ₂,t, but outsiders only observe θ₁,t."* The friction is
verifiability toward outsiders, not ignorance. HMT's discretionary accruals measure **intentional**
management, and their own caveat treats the unintentional part as measurement error to apologise for.
**Unobservable-in-principle degradation versus deliberately-withheld known news is the only real
daylight, and it is genuine.**

---

## 3 · But the daylight is narrow, and two threats must be pre-empted

**The distinction is observationally fragile.** From the price's point of view, "insider knows and
won't say" and "nobody knows yet" produce the same widening wedge resolving discontinuously. Worse,
the obvious discriminating tests cut *against* us: deliberate withholding predicts correlation with
insider incentives, insider selling, litigation and regulatory regime — and **HMT's own post-SOX
dissipation is exactly that pattern**, i.e. evidence for the agency generator.

**Threat 1 · Basu (1997) conditional conservatism.** GAAP recognises bad news *faster* than good news
for anything estimable. A blanket "the reported layer lags the physical layer" is contradicted by four
decades of asymmetric-timeliness evidence. **Our claim survives only if restricted to degradation on
which conservatism has nothing to bite** — no impairment trigger, no estimable expected loss, no
observable event. That restriction must be stated explicitly and narrowly, or it is a one-line kill.

**Threat 2 · The delayed-recognition accounting literature has already made the "accounting layer as
its own object" move.** Name these before a referee does: **Beaver & Ryan (2000, JAR)**, which
decomposes book value into a **bias** component and a **lag** component relative to economic value —
the closest prior art to our low-pass-filter claim, and it named both terms 26 years ago;
**Bushman & Williams (2015, JAR)** on delayed expected loss recognition and bank fragility;
**Ramanna & Watts** on unverifiable fair-value estimates and goodwill non-impairment; **Granja (2023)**
on HTM reclassification suppressing recognised losses ahead of a run — which is our recognition-event-
as-cause story, in banks, with 2023 data. **Our daylight is against these two finance papers, not
against accounting.**

---

## 4 · The empirical gift, and it should lead §9

The opacity/agency explanation of crashes is **weakening while the phenomenon grows**:

- **Andreou, Lambertides & Magidou (2023, *British Journal of Management*):** crash incidence rose
  from **5.5% to 27%** of firm-years between 1950 and 2019, while *"the opacity– and
  overinvestment–crash relations are non-significant, especially in the period following the
  enforcement of the Sarbanes–Oxley Act."*
  > **CORRECTED 2026-08-11 against the publisher's own PDF, two defects.** *(i)* The quotation read
  > "nonsignificant"; the abstract reads **"non-significant"**, hyphenated, and uses en-dashes in
  > "opacity– and overinvestment–crash". The abstract uses *both* spellings in consecutive sentences,
  > which is presumably how the retrieval pipeline blended them. *(ii)* Far more consequentially, the
  > **27% is the CRSP–Compustat–Execucomp universe.** The body, p. 2: *"grown steadily from 5.5% in
  > 1950 to 23% in 2019 in the CRSP universe, and to 27% in the CRSP–Compustat–Execucomp universe."*
  > Quoting 27% bare as "crash incidence" is a one-line kill, and §9 was about to lead with it.
- **Datta, Iskandar-Datta & Singh (2014, *RFE*)** fail to confirm the opacity–R² relation; not robust
  to Petersen clustering.
- **HMT concede the post-SOX dissipation in their own abstract.**

**A mechanism that does not require a lying manager is what explains a fivefold rise in crashes
alongside the statistical death of the lying-manager explanation.** Position there — as the
**non-agency generator of the same asymmetry**, complementing Jin & Myers rather than beating them.

---

## 5 · Provenance, and one standing caution

**Read in full text:** Jin & Myers via **NBER WP 10453** (not the typeset JFE 2006 version —
proposition numbering is the working paper's); Hutton, Marcus & Tehranian via full-text HTML (not the
typeset JFE 2009 version). **Abstract-only:** Datta et al. (2014); Andreou et al. (2023) — SSRN only,
Wiley returned 403; Bushman & Williams; Granja; Ramanna & Watts. **Not verified this session:**
Feltham–Ohlson, Allen–Larson–Sloan, Caballero–Hoshi–Kashyap, Palmrose–Richardson–Scholz.

> **WT-059 applies and is not discharged.** Every quotation above reached this file through a
> retrieval pipeline, not through eyes on a typeset page. **Re-check each one character-by-character
> against the published PDF before it appears in Paper III.** The programme has been demolished twice
> for positioning written from summaries; this file exists to end that, and it does not end it until
> the quotes are verified at source.
