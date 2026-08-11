# REG-001 · Structural registration · P3's second layer

- **Status:** REGISTERED — committed before any line of the instrument was written, and before any
  statistic was computed. WT-052.
- **Registered:** 2026-08-11, session wealthTensor-07.
- **Series:** `REG-*`, new, and deliberately **not** `PRE-*`. See §1. It does **not** consume the
  `PRE-003` slot, which stays reserved for the segment-level test (HANDOFF §5.7).

---

## 1 · Why this is not a PRE

`PRE-001` and `PRE-002` are empirical pre-registrations. They state a prediction about the world
and they can fail against EDGAR data. `PRE-002`'s stopping rule fired and stays fired.

This document registers something structurally different: a claim about **whether a mathematical
property of one of our models survives being carried into another**. It can only fail against our
own code. Filing it as a `PRE` would let a structural pass masquerade as empirical support, which
is the specific confusion this project has already paid for once. Different series, different
evidential weight, stated here so nobody has to reconstruct the distinction later.

**Nothing in this registration may be cited as evidence for or against P1, P2 or P3 as claims about
the world.** It tests only whether one identity is portable.

## 2 · The background, in one paragraph

Paper I v0.1 was rejected by its own referee (`REVIEW-002`), and the one claim that survived —
that excess demand `z(p) = #{mᵢ > p} − S` is invariant to the allocation at every non-reservation
price — was then found in **Wicksteed (1910)**, Book II Ch. IV, on the same horse market, with the
same reallocation exercise, verified verbatim against the 1910 Macmillan first edition. Within a
market Wicksteed's statement is *more* general than ours: he covers divisible goods and multi-unit
holdings, which our unit-demand form does not.

The re-scope decided on 2026-08-11 (Jason) is to state the claim one level up, as an instance of
**P3 · Atomism** (*measured aggregates are folds over units*): excess demand is a fold over units;
the supply and demand schedules are folds over units **and the allocation**, which is not a property
of the population. Wicksteed has no P3 — his apparatus is subjective scales of preference, which is
domain-bound by construction.

**That re-scope is only worth anything if the identity does work somewhere Wicksteed's apparatus
cannot follow.** If it does not, the re-scope is Wicksteed with new vocabulary and must be reported
as such. This registration is the test.

## 3 · The port, specified before the instrument exists

Price layer, as in `src/wealth_tensor/excess_demand.py`:

| object | price layer |
|---|---|
| unit | agent *i* with reservation price *mᵢ* |
| label | *S* of them hold a unit; set *H*, \|*H*\| = *S* |
| index | price *p* |
| the two halves | demand(*p*) = #{*i* ∉ *H* : *mᵢ* > *p*} · supply(*p*) = #{*i* ∈ *H* : *mᵢ* < *p*} |
| the fold | *z*(*p*) = #{*mᵢ* > *p*} − *S* |

Recognition layer, ported:

| object | recognition layer |
|---|---|
| unit | item *i* with recognition threshold *τᵢ* — the scrutiny at which it must be booked |
| label | *R* of them are currently recognised (on the books); set *B*, \|*B*\| = *R* |
| index | scrutiny level *s* |
| the two halves | newly-recognisable(*s*) = #{*i* ∉ *B* : *τᵢ* < *s*} · derecognisable(*s*) = #{*i* ∈ *B* : *τᵢ* > *s*} |
| the fold | *n*(*s*) = #{*τᵢ* < *s*} − *R* |

## 4 · The three registered predictions, and which one actually discriminates

> **H1 — the static count.** *n*(*s*) = #{*τᵢ* < *s*} − *R* at every *s* that is not itself a
> threshold, for every choice of *B* with \|*B*\| = *R*.
>
> **Registered expectation: PASS, and near-trivially.**

**H1 is not sufficient and must not be reported as if it were.** The partition argument is
identical to the price layer's; passing it demonstrates that the nouns were swapped correctly and
nothing more. A paper that claims a second instantiation on the strength of H1 alone has
**force-fit, not form-fit** (WT-042), and this sentence is registered in advance so that a later
session — or this one — cannot pretend otherwise.

> **H2 — the discriminating test.** Let the booked set be generated **endogenously** by the
> model's own dynamics rather than assigned exogenously, with recognition applied at rate *α* to
> the **aggregate** gap (as `lag.py` does — recognition is coupled across items, which the price
> layer's allocation is not). Then, across many initial booked sets of the same size *R*:
>
> - **H2a · the timing of recognition events is invariant** to the initial booked set;
> - **H2b · the magnitude of recognition events is NOT** invariant to it.
>
> **Registered expectation: H2a passes, H2b passes (i.e. magnitude genuinely varies).**

H2 is the whole test. It discriminates because the recognition layer has two structures the price
layer does not: the label set is **endogenous and path-dependent**, and recognition is
**aggregate-coupled**. Neither has an analogue in a market where the allocation is exogenous data.
If the invariance survives both, the identity is portable and P3 has a second instantiation. If it
does not, it is not, and the paper says so.

**H2b is registered as an expected pass in the direction that costs us something.** A magnitude
that also turned out invariant would be a *stronger* and more flattering result; predicting the
weaker one in advance is deliberate. It is also the derivation of the thing Wicksteed asserted and
never proved — that the partition *"does affect the amount of business done"* while leaving the
determination of price alone. Same split, different layer: **the count is a fold, the magnitude is
not.**

> **H3 — the falsifier.** If aggregate-coupled recognition breaks **H1**, the port is invalid at
> the first step, the P3 second-layer claim **FAILS**, and the re-scope is reported as unexercised
> generality in the paper's limitations section rather than repaired.

## 5 · Stopping rule

**One instrument. No second port.** If H2a fails, the finding is that the identity does not survive
endogenous labelling, and that is the result. This registration may not be amended after the first
result commit, and a third porting attempt would be a hypothesis being fitted — the same judgement
`PRE-002` §5 made, applied to the same temptation in a different costume.

## 6 · Bindings, fixed now

- Instrument: `scripts/wt066_p3_port.py`, written after this file is committed and pushed.
- Thresholds *τᵢ* drawn from the same generator family the price layer uses, seeds stated in the
  script and reported in any output.
- **Every published number comes from that committed script, run** (WT-053).
- **Adversarial review fires before any of this is called a result** — before a ledger entry,
  before paper text, before Jason is told (WT-065). Three checks: refute the interpretation
  separately from the arithmetic; a priority audit told that an over-eager priority claim is as
  damaging as a missed one (L28); and *what would have to be true for this to be false.*
- Guard tests must be checked that they **can fail** — the `4/21 < 4/11` lesson.

## 7 · What a pass does NOT license

A pass licenses exactly this sentence: *the fold-invariance survives a change of layer, including
endogenous and aggregate-coupled labelling.* It does **not** license any claim that the recognition
layer is empirically correct, that P3 is true of the world, or that the price-layer result is novel
— which it is not, and Wicksteed gets that credit in the text.
