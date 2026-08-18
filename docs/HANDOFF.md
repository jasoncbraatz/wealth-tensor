---
project: wealth-tensor
session_n: 74
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 37a7cdbec4a91d3d36fc92944339df4dff9c58aa
updated: 2026-08-18
session: wealthTensor-74
live_theme: "Paper II's fifth independent read, taken as assigned. FOUR findings, seven edits, two carded — and the instrument this pass adds is four words: RUN THE PAPER'S OWN COMMANDS. Paper II's §7 names two regeneration scripts; six independent reads had reasoned about them and none had executed them, and one prior pass wrote 'No overclaim ... but that is reasoning about the script, not a run of it' and was wrong on the first half. Eleven minutes of wall-clock produced two of the four findings and moved eight cleared rows from inference to measurement. Also closed queue item 4, three sessions deferred: the two cross-reference sweeps are now wt133, a committed instrument with a load-bearing exit code, and its first estate-wide run went red on PAPER IV."
phase: "Manuscript repair under a settled thesis. Paper II's counter runs 9 → 2 → 4 → 3 → 4 across seven passes and has not converged; Paper III's opens at 7, one pass deep. The instrument set now has FOUR axes: quantifiers (wt130), cross-references (wt133, committed this session, RC-1 today), census-and-guard (wt128/wt129/wt132), and the new one — execute the manuscript's own regeneration commands before reading a word of it."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered: RESOLVE wt133'S RED ON PAPER IV, THEN GIVE PAPER IV ITS NEXT INDEPENDENT READ. `python3 scripts/wt133_crossref_sweep.py` exits 1 today and names exactly one site: paper-IV.md L179's bare `§3.1`. The passage's subject is Paper III throughout ('Paper III §2 is that holding', 'Paper III §5.4 goes on to measure'), Paper IV's own §3 has NO subsections — and the very next line does the same thing with a bare '§4', which is WORSE, because Paper IV HAS a §4 and a reader resolves it locally and silently to the wrong section. Fix both, add any genuine class-A dismissals to docs/crossref-dismissed.tsv WITH THEIR REASON, and get wt133 to RC 0. THEN read Paper IV end-to-end — and RUN ITS REGENERATION COMMANDS FIRST (§10), which nobody has ever done for Paper IV. DONE WHEN: wt133 exits 0 across all four manuscripts; Paper IV's §10 commands are executed and every number in the paper checked against their output, with the count of cells verified recorded; Paper IV read end-to-end; every finding repaired in-pass or carded with a named falsifier; REVIEW-015 exists with its own coverage claim, cleared list and not-checked list; suite green, board re-checked, coach at Paper IV's baseline of 1 conduct / 0 concessive. A ZERO IS A RESULT — say so plainly if you get one and do not manufacture a finding."
blockers: []
drift_flags: ["-70's rule ('Paper II returns findings → next session is Paper II again') is being set aside for -75, DELIBERATELY, and here is the reason in one line: wt133 exits 1 on PAPER IV right now, and a committed instrument that is red is a higher-priority object than the next pass on any manuscript — a red left standing teaches the next five sessions to ignore the exit code. -76 goes back to Paper II unless -75 finds a reason in writing.", "PAPER II'S COUNTER IS 9 → 2 → 4 → 3 → 4 AND IS NOT CONVERGING. Five independent reads, and the fifth found as many as the third. Read that as information about the METHOD, not about the paper: each pass has used a NEW instrument (quantifier sweep, blast-radius census, cross-reference sweep, run-the-commands) and each new instrument has found things the previous ones structurally could not. The pair the definition of done wants may not be reachable until the instrument set stops growing — which is itself a finding worth stating to Jason.", "The queue's old item 1, 'Paper I's first P7 pass', remains demoted: Paper I is NOT in definition_of_done and Paper II §7 calls it 'since superseded by its own internal referee'. Carried unchanged from -71 through -74.", "wt133's sweep-2 orphan lists for Papers I, III and IV were PRINTED and NOT ADJUDICATED. Only Paper II's was read. Paper IV shows Mas-Colell, Robinson, Sraffa uncited; Paper I shows its two companion self-citations. Do not read the RC as covering these — sweep 2 does not set the exit code, deliberately, because its false-positive class C (surname-is-also-a-noun) is irreducible."]
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-74` IN ONE LINE

**Took the assigned at-bat as ordered: Paper II's fifth independent `P7` read.** Ran both
cross-reference sweeps and `wt130` before reading a word, then read all 547 lines. **Four findings,
seven edits (`wt132`), two carded.** Paper II's counter goes to **4**.

**Then it did the thing six passes had not: typed the commands the paper gives its readers.**
§7 names `wt030_report.py` and `wt077_tail_index.py`. Running them took eleven minutes, produced
**two of the four findings**, and moved **eight** of `REVIEW-014`'s cleared rows from *inference*
to *measurement*. `-70` had written the not-checked item that says exactly this — *"that is
reasoning about the script, not a run of it"* — and then concluded *"No overclaim"* from the
reasoning. It was an overclaim.

**And it closed queue item 4.** The two cross-reference loops are now
`scripts/wt133_crossref_sweep.py`, with a committed dismissals file so its **exit code means
something**. First estate-wide run: Papers I, II and III clean; **Paper IV red.**

Suite **1078 passed, 0 failed** (66.9 s). Board **66 criteria, `docs/CHECKLIST.md` unmodified —
the board did not move, for the fifth consecutive session.** Coach **RC 0, all four at baseline**
(II = 2/0). Abstract **byte-identical**, asserted in `wt132`'s guards.

---

## READ FIRST, in this order

1. **`docs/REVIEW-014-P7-paperII-pass7.md`** — the pass of record. **§2's `II-23` is the one to
   read even if you skip everything else**, because it is a defect *and* a defect in the guard
   that was supposed to catch it: §3.3 says *"a lumpier assessment is very slightly stronger"*,
   the sweep is **U-shaped** with an interior minimum at *P* = 30, and the test pinning the
   sentence swept `p <= 20` — one point short of the turn — while its docstring generalised.
   §1 is the coverage claim with three counts, §3 is a **27-row cleared list** that says which
   rows were upgraded from inference to measurement and which are loose-but-true, §4 is the
   **not-checked list and your brief is written from it.**
2. **`scripts/wt133_crossref_sweep.py` — RUN IT FIRST, BEFORE YOU READ ANYTHING.** It is the
   instrument `-73` designed and `-74` committed, it takes four seconds, and **it is red.** Its
   docstring carries the three false-positive classes so a flag costs you seconds, not minutes.
   `docs/crossref-dismissed.tsv` is the audit surface: every row is a claim you can delete to
   re-open.
3. **`docs/LEDGER.md` `WT-122`** — this pass in one entry, including what the guard cost. `wt132`
   **aborted on its first run** because a needle was written with backticks and the file has none;
   nothing was written, because the guards run **before** the backups. That ordering is `wt129`'s
   (`WT-118`) and it is why a bad needle is a thirty-second correction instead of a `git checkout`.

---

## YOUR AT-BAT — ASSIGNED. Do not choose.

**Resolve `wt133`'s red on Paper IV, then give Paper IV its next independent read.**

Step one is four seconds of running and probably twenty minutes of fixing:

```
python3 scripts/wt133_crossref_sweep.py     # exits 1; names paper-IV.md L179
```

**What it names, and what it does not.** L179 carries a bare `§3.1` inside a passage whose subject
is Paper III in every surrounding sentence, and Paper IV's own §3 has no subsections — so the
reference resolves to nothing and the sweep sees it. **The line after it is the one the sweep
cannot see**: *"read before §4 indexes the holding by asset class"* — Paper IV **has** a §4, so
that reference resolves **locally and silently to the wrong section**, and no mechanical check
will ever flag it. Read L175–L182 whole before you touch either. That asymmetry is the lesson:
the sweep finds the references that resolve to *nothing*; only a reader finds the ones that
resolve to the *wrong thing*.

Then Paper IV end-to-end — **and run §10's regeneration commands before you read the prose.** No
session has ever done this for Paper IV. On Paper II it produced half the findings.

### WHY PAPER IV AND NOT PAPER II AGAIN, since `-70`'s rule says Paper II

Because a committed instrument is standing red, and that outranks the next pass on any manuscript.
A red exit code left alone for one session is a red exit code everybody stops reading. `-70`'s rule
is set aside for **one** session, exactly as `-72` set it aside for Paper III's first read, and it
comes back in force at `-76`. **If you disagree on reading this, run Paper II's sixth read and say
so in ONE LINE at the top of your handoff.** The one outcome that must not happen is both sessions
deferring, and `wt133` staying red is the specific way that would happen here.

### THE QUEUE BEHIND IT — context, not a menu. Do not shop here.

**Reading this list is not a decision you are being asked to make.**

1. **Paper II's sixth read** — counter at 4 and not converging; pair unstarted. Back in force
   at `-76`.
2. **Paper III's second read** — counter at 7, one pass deep, pair unstarted.
3. **`REFERENCE-POLICY`'s eighth pass** — card `1217556161163494`. **Now the single most-deferred
   item in the project.** Both `-73` and `-74` swept references for **where** each entry claims to
   be cited; neither read them for **what** the sources say. `wt133` mechanises the first question
   permanently, which means the second one is now the *only* part of that card a Claude can still
   add value on.
4. **`III-8`** — card `1217567136996151`. §11 names no regeneration command for Paper III's §4.
   **`-74`'s instrument is the answer to this card**: run Paper III's §11 commands and see which
   of §4's numbers appear. The card carries its own falsifier — it may be wrong.
5. **`II-25`** — card `1217568297674954`, filed today. **All four** manuscripts' `Version X.Y,
   DATE` front-matter stamps predate their own claim-changing commits; Paper II's revision history
   says of v0.2 *"No result, number, claim or citation changed"* with **twelve** commits behind it.
   Step 1 is a Claude-sized test that goes red on all four today; step 2 is one ruling from Jason.
6. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
7. **Paper II's uncited reference entries** — card `1217568192511533`, filed today. 9 of 16
   entries do no work in the body; §6's public-finance paragraph is the one place with a cheap,
   obviously-correct repair.
8. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first: tightening the
   float tolerance to `==` hands the next machine a red suite. **`-74` measured the underlying
   fact and it is stronger than the card assumes**: `wt115` reports `array_equal` **True** and
   max |Δw| / mean w = **0.0**, exactly. Assert the structural property.
9. **The U+00B5 guard** — card `1217561398864561`.
10. **The `CONDUCT_ALLOWED_SECTIONS` gap** — card `1217562682350929`. `-68` hit it; `-69` through
    **`-74`** all avoided it only by reading the tuple first. **Seven** sessions around one
    landmine.
11. **A gate check that a `§N` named in `HANDOFF.md` exists in the paper it names** — card
    `1217564707330383` (`WT-112`). **`wt133` is now 90 % of this**; point it at `HANDOFF.md`.
12. **The duplicated Bouchaud–Mézard description** — card `1217565324215216`. Needs a decision,
    not a patch.
13. **PASTE THE HANDOFF forcing function** — card `1217560480809492`. (`-67` through `-74` all
    pasted. **Eight** data points, still not a fix.)
14. **PAPER I'S FIRST `P7` PASS** — still demoted, still for `drift_flags`' reason.
15. **`A3` from the PAN AAR — estate-level, STILL UNCHECKED.**

---

## WHAT `-74` DID, so you do not re-derive it

**Coverage, all three sweeps run before a word of prose was read.** 46 `§N.M` references on the
whole file / 13 distinct / **zero unresolved** — the first time Paper II's cross-references had
*ever* been checked, three sessions on the queue. 16 reference entries swept by surname; 7 do work
in the body, 9 do not, **zero false claims**. `wt130`: **155 tokens on 118 of 547 lines.**

* **`II-22`** — §7 twice scoped the manuscript's non-simulation numbers to *"the **three**
  quadrature values"*. **E[η⁺] = 0.1073** is a fourth, in bold in §3.1, printed by the very script
  §7 names for the exception (`E[eta+] closed form = 0.107269`). Right provenance, wrong count,
  two sentences. **Repaired at both sites.**
* **`II-23`** — §3.3's *"a lumpier assessment is very slightly **stronger**"*. Measured at
  *P* = 1/2/4/10/15/20/25/**30**/40/50 → .486/.484/.480/.471/.461/.457/.452/**.451**/.458/**.469**.
  **Interior minimum at 30; above the quoted P = 20 endpoint by P = 50** — and the turn is *inside*
  the design, since at *P* = 50 the constant average rate requires exactly *r* = 1.00.
  Horizon-stable at *T* = 600. **The manuscript and the test were both repaired**; the test now
  sweeps to 50 and pins the measured shape.
* **`II-24`** — §1's *"The process responds to four numbers"*, contradicted **five lines later** by
  contribution 1's *"plus the realisation share of the base … a function of these alone"* and by
  §3.2, which moves the reachable Gini **0.125 → 0.994** with all four levy coordinates held
  fixed. `WT-117`, third instance. **Repaired to five.**
* **`II-26`** — §3.4's *"which separates nothing"* of a **0.103** gap. Repaired with the
  paragraph's own ceiling argument. **Named in `REVIEW-014` as the softest of the four** and the
  row most likely to be re-litigated.
* **`II-25` CARDED** and the reference-orphan measurement carded. Both above.
* **Bug spray:** `wt077_tail_index.py`'s docstring named `RedistributionEconomy`; the class is
  `RedistributiveEconomy`. And `wt133`'s **own first run** swept two manuscripts when asked for
  one, because `"paper-II"` is a prefix of `"paper-III"` — found by running what I wrote, fixed,
  and the reason is in a comment above the line.

`LEDGER` `WT-122`. Three lessons banked, four `use`d and corroborated. Commits `58f7f5b` ← `9af89bf`.

---

## ✅ NEW SETTLED, DO NOT REOPEN

**`REVIEW-014` §3's 27 cleared rows are cleared.** Three are named there as most likely to be
re-litigated and they are named here too, so you do not spend the tokens:

* **`C23`** — §1's *"A boundary, stated once and maintained throughout"*, against §5.2, §5.7 and
  §6 all restating it. **Loose, not false, deliberately not repaired**: *"stated once"* reads as
  *argued once rather than defended repeatedly*, and *"and maintained throughout"* is the clause
  that carries the recurrences.
* **`C18`** — §3.1's *"which a stock levy reaches at rate 0.25"*. Stock at *r* = 0.250 reaches
  **0.123**, i.e. it reaches 0.125 slightly *below* rate 0.25. **Conservative, not wrong.**
* **`C19`** — §5.5's *"the exception is §3.1's **three** Var[log *a*] values"* is **correct as
  written** and `II-22` does **not** touch it. That clause is about which numbers are *simulated*;
  §7's is about which are *generated by simulation at all*. Two different sets, and only §7's was
  wrong.

**The regenerated numbers are settled.** Every cell of §3.1, §3.2, §3.3 and §3.4 was reproduced
exactly by `wt030_report.py` and `wt077_tail_index.py` on 2026-08-18. **Do not re-derive them.**
§3.2's ρ = 0 identity is verified to the byte (`array_equal` True, max |Δw| = 0.0) and is the
strongest claim in the paper. §7's pin `3b11f23` is verified as the last commit touching
`redistribution.py`. The **18**-test count is verified by `grep -c "def test_"`.

**`docs/crossref-dismissed.tsv`'s seven rows are adjudicated.** Paper I's §10 / §17 are
Mas-Colell, Whinston and Green's, attributed in the same clause. Paper II's §4.1 is Benhabib et
al.'s, disclosed in the entry. Paper III's §3.3 is `REG-003`'s — `REVIEW-013` §3's single apparent
miss, **independently reproduced** by `wt133`. Paper IV's §5.4 / §A.1.2 / §A.2.2 all name Paper III
in the sentence. **Paper IV's §3.1 is NOT dismissed and must not be** until somebody reads L175–182.

---

## THE TELL, now TWENTY-THREE deep

`-61`–`-70` as before. `-71`: read forward from a quantifier. `-72`: downstream includes four lines
later · grep the document for the failure mode it names · a guard has two failure modes and red
cannot tell them apart (`WT-118`). `-73`: a cross-reference is a quantifier over a section · a
clean sweep is a result and belongs in the review doc · the thing that propagates is the tool's
output *line*, not its number.

**`-74`(i): RUN THE MANUSCRIPT'S OWN REGENERATION COMMAND BEFORE YOU READ THE MANUSCRIPT.**
Reasoning about a script is not a run of it, and the difference is a finding. Six passes reasoned
about Paper II's two commands and one of them wrote *"No overclaim"* on the strength of that
reasoning. Eleven minutes of typing produced two findings and upgraded eight cleared rows. **If a
paper claims reproducibility, the cheapest possible check of every number in it is to type the
command it gives you** — and it is cheaper than reading the section those numbers are in.

**`-74`(ii): A TEST WHOSE SUBJECT STOPS WHERE ITS CLAIM STOPS CANNOT FAIL.** The periodicity test
asserted monotonicity over `p in (1, 2, 4, 10, 20)` and its docstring generalised to all *P*. The
assertion was true, the docstring was false, and **no run could tell them apart**, because the
tuple ended one point before the turn. The repair is not a stronger assertion — it is a **wider
subject**. Sweep at least one point past the last point at which the claim is known to hold, then
pin the **shape you measured**, not the law you hoped for. `WT-092`'s question, asked of a test
instead of a docstring.

**`-74`(iii): AN INSTRUMENT WITHOUT A DISMISSALS FILE IS A REPORT, NOT A TRIPWIRE.** `wt133`'s
class-A false positives are **permanent** — a paper citing another paper's §5.4 will do so forever
— so an unfiltered sweep exits 1 on day one and every day after, and within two sessions nobody
reads the exit code. The dismissals file is what converts *"1 flagged"* into *"1 **new**
flagged"*, and it is also the audit surface: every row is a claim you can delete to re-open.

---

## TOOLING (▲ new at `-74`)

▲ **`scripts/wt133_crossref_sweep.py`** — queue item 4, closed. Both sweeps, all four manuscripts,
`--md` for pasting into a `REVIEW`, three named false-positive classes, and a **load-bearing exit
code** backed by `docs/crossref-dismissed.tsv`. **RC 1 today.**
▲ **`scripts/wt132_paperII_p7pass7.py`** — the guard-honesty exemplar extended to a **test's
assertions**: five manuscript needles asserted exactly once in the *original* before any write,
backups before the first byte moves, abstract-section identity before and after, and a
post-condition that **re-runs sweep 1 on the patched text**.
▲ **The fourth axis, which is not a script:** `python3 scripts/<the command §7 names>`.
· `wt130` (quantifiers), `wt128`/`wt129` (census-and-guard), `wt131b` (amending a frozen section)
all unchanged. **Tags run to `wt133`; `wt134` is free.** Note `wt132` was reserved in `-73`'s
queue for the sweeps and was spent on the patch script; **the sweeps are `wt133`.**

---

## JASON-SIZED, not yours

(a) `DECISION-001` closed. (b) Paper IV framing ruled. (c) **`P7` is still ONE BOOLEAN — and the
argument is now five sessions deep. `-70` moved the board with an edit that changed no sentence;
`-71` changed five and it did not move; `-72` changed three and it did not; `-73` changed thirteen
across seven findings and it did not; `-74` changed seven across four findings — including the
first edit in this batch to a *test's assertions* — and it did not.** Five sessions is enough
evidence to stop testing the proposition. `-72`'s coverage-row proposal stands, and `-74` can now
say precisely what it would have caught: a row requiring each paper's `REVIEW` to carry a sweep
whose counts match a fresh run measures **coverage**, not truth — and it would have failed Paper II
for three sessions on the cross-reference sweep alone, which nobody ran until today. **One line
from you settles it: yes add the coverage row, or no, reviewing stays narrative.**
(d) **NEW, and it is one word: does a `P7` repair pass bump a manuscript's minor version, or does
the stamp only move at submission?** Card `1217568297674954`. All four papers currently claim dates
that predate their own claim-changing commits, and Paper II's revision history claims *"No result,
number, claim or citation changed"* on top of twelve commits. A Claude writes the test either way;
only you can pick the numbering.
(e) **A finding about the process rather than the papers, offered because you asked for exactly
this kind:** Paper II's counter is **9 → 2 → 4 → 3 → 4** and is not converging — but every pass has
used a *new instrument*, and each new instrument found what the previous ones structurally could
not. The pair the definition of done wants may be unreachable until the instrument set stops
growing. That is not a reason to change the bar; it may be a reason to say so out loud in the
definition of done.
(f) The PAN history purge — Batter's Box `1217561667484767`.

---

## WHY NOT `P13`, since `charter-read.sh` asks

`charter-read.sh` reports **`P13` as the first OPEN lane in dependency order** — the beautifully
designed, arXiv-ready PDF. `-74` worked **`P7`** instead, as assigned, and the project's own
ordering ruling is why: **`P13` is a point-in-time capture of the corpus**, and capturing a corpus
whose manuscripts still yield findings per read produces a beautiful PDF of prose that is about to
change. `P7` → `P13` → `P8` is the DoD's own sequence.

**`-74` sharpens `-73`'s version of this argument rather than replacing it.** `-73` wrote that
typesetting a document whose own front matter misdescribed its **title** is the strongest form of
the mistake. `-74` adds the estate-wide instance: **every one of the four manuscripts currently
carries a front-matter version stamp that predates its own claim-changing edits** (`II-25`). A
point-in-time capture whose own point in time is wrong on all four papers is not a capture. **`P13`
should not move until `II-25` is ruled and Paper II's and Paper III's pairs are at least started.**

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary line,
never `$?`, never through a pipe); **`python3 scripts/wt133_crossref_sweep.py` and say its RC**;
`roster leave --who <you>` once; and **paste a handoff better than this one into the chat as the
last act.** Assign `-76` ONE at-bat with a definition of done. Do not hand them a menu. 🥎
