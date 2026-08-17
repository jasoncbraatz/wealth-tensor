---
project: wealth-tensor
session_n: 67
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 9cb7827675580921d130b9124b6b6fd6a24b8d31
updated: 2026-08-17
session: wealthTensor-67
live_theme: "The two mandatory citations placed — and one of the card's two placement rules turned out to have no site in any manuscript, so the citation went where the paper actually claims something instead of where the instruction said. Then the wrap gate refused, and reading WHY surfaced a live customer credit-card number in the wisdom repo."
phase: "Manuscript repair under a settled thesis. Paper II is credited and internally consistent; its second independent read is now the live at-bat and it inherits one question this session raised and refused to decide."
gate_passed: true  # green on the RE-RUN; the first run FAILED G-V and that failure is the session's second story — see §THE GATE REFUSED
gate_version: "2.59"
next_at_bat: "PAPER II's SECOND INDEPENDENT READ — could start a convergence count, and it now owns the abstract question card 1217561330623702. The manuscript moved in 24 places in 48 hours and then again today in §1, §3.1 and §6. DIFF against paper-II.md.bak-wt67-cites, .bak-wt65-decA and .bak-wt64-p7; do not read the repaired text as given."
blockers: []
drift_flags: []
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-67` IN ONE LINE

**The two mandatory citations are placed, and the interesting part is that I refused half the
instruction.** The card said *cite Benhabib, Bisin & Zhu wherever the `r = 1` cap appears.* The
census found the `r = 1` cap in **8 `docs/` files, 5 `scripts/` — and ZERO of the four
manuscripts.** Paper II is a Gini-and-κ paper; it names no tail index anywhere. The cheap repair
was to write the cap in so the citation had somewhere to land. That would have **manufactured a
claim in order to credit someone else for it** — an overclaim *with* a footnote, which is harder
to catch than one without. BBZ went into §6 against what Paper II actually asserts instead.

**And the defect was never a missing reference.** Both works were **already in the reference
list**: Bouchaud / Mézard / Benhabib / Bisin / Zhu all measured **body = 0, references = 1**.
Listed and never cited — the same defect `paper-I`'s `REVIEW-002` `A10` caught one manuscript
over. A reference-list entry is a signpost, not a credit.

Commit **`bf07363`**. Suite **1078 passed, 0 failed**. Board **66 criteria**. Abstract
**untouched at 244 words** — `-65`'s six words of slack are still on the table.

---

## READ FIRST, in this order
1. **`docs/LEDGER.md` `WT-103`** (the fact: what was placed, where, and why one rule had no site)
   and **`WT-104`** (the method: three near-misses, all one species).
2. **`scripts/wt122_paperII_citation_census.py`** — read its *output*, not just its code. It is
   the newest worked example of a census that names its hazard in advance and carries a positive
   control on every probe.
3. `docs/SCOUT-001-truncation-vs-scaling-prior-art.md` §4 and §8 — still the evidence of record.
4. `docs/papers/paper-II-redistribution/paper-II.md` §1 contribution 2, §3.1's last new
   paragraph, and **all of §6** — that is everything that moved today.

---

## YOUR AT-BAT — take one, in this order

### 1. **PAPER II's SECOND INDEPENDENT READ.** ***This is the one.*** Could start a convergence
count, and it is now overdue in a way it was not yesterday: the manuscript moved in 24 places in
48 hours, and then **`-67` moved §1, §3.1 and §6 on top of that.** **DIFF against
`paper-II.md.bak-wt67-cites` first, then `.bak-wt65-decA` and `.bak-wt64-p7`.** Do not read the
repaired text as given — that is the whole point of an independent read.
**It inherits one live question, carded rather than decided:** card `1217561330623702`. §6 now
concedes the bare stock-versus-flow contrast to Bouchaud & Mézard and §1 was narrowed to match.
**The abstract still opens with *"the base sets a ceiling the rate cannot cross"* and was not
touched.** Whether an abstract owes a related-work concession is a judgement about the
manuscript, not about the citation. The card argues both sides and lists the constraints.

### 2. **PAPER IV's re-read after the narrowing.** §1 and §3 still carry the ladder framing in
prose even though the title and abstract no longer promise it. `wt120`'s census found the phrase
only twice and both are fixed — but *"composes from X to Y"* is a **shape, not a string**, and a
grep cannot see a paraphrase. Read §1–§3 with the narrowed claim in mind. ~40 min.
*(`-67` touched `paper-IV.md` for exactly one token — the `Physica A` issue number — so the
narrowing pass is otherwise undisturbed.)*

### 3. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).

### 4. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first:
tightening the float tolerance to `==` hands the next machine a red suite. Assert the
**structural** property (the ρ = 0 flow base is uniform across agents).

### 5. **PAPER I's FIRST INDEPENDENT READ** — still the only manuscript with no `P7` pass at all.

### 6. **`REFERENCE-POLICY`'s sixth pass** — card `1217556161163494`. The predicate-level ceiling.
`-67` is the second session running that would have been saved by it existing already.

### 7. **The U+00B5 guard** — card `1217561398864561`. **NEW, small, and it is a live hazard.**
See §THE TELL. Note the constraint: **do not add it to `tests/test_redistribution.py`**, whose
count of **18** is quoted in Paper II's abstract and §1. A new module is fine.

### 8. **Make PASTE THE HANDOFF a forcing function** — card `1217560480809492`. Small, and it
failed twice in one session with the fix written down in between. *(`-67` pasted it. That is one
data point, not a fix.)*

### 9. **Paper II's companion reference entries** — card `1217542940968749`.

### 10. **`A3` from the new AAR — the blast-radius question I could not answer.** *Where else do
call transcripts and their `.srt` intermediates land, and is any of it committed or pushed?* This
PAN reached a lesson because it was in a transcript, and `call-artifact-srt-intermediates-on-tmp`
is already an AAR in this corpus about those artefacts sitting in the wrong place. **Unchecked, and
named as unchecked so it is not mistaken for checked.** Not a `wealth-tensor` at-bat — but it is the
highest-value loose thread on the estate right now and it should not wait for someone to trip over it.

**FORCING LINE (`-59`'s ruling, kept): take none of the nine, say why in ONE LINE at the top of
your handoff. It costs nothing.**

---

## WHAT `-67` DID, so you do not re-derive it

**One at-bat.** Two committed instruments, one commit, two `LEDGER` entries, four banked lessons
(three global), three Asana cards (one closed, two filed).

### A · The census (`scripts/wt122_paperII_citation_census.py`)
Named its hazard **before it ran** — *"is the `r = 1` cap actually in a manuscript at all, or only
in `docs/`?"* — walked live `.md` and `.py` with `.bak-*` and `._*` excluded and the exclusions
printed, normalised whitespace before matching, and carried a **positive control on every probe**.

| hypothesis | measured |
|---|---|
| `H1` B&M *"wherever the stock/flow contrast is made"* | **1 site** — §3.1's *"different objects"* paragraph |
| `H2` BBZ *"wherever the `r = 1` cap appears"* | **0 sites, all four manuscripts** |
| `H3` are the works cited or merely listed? | **body 0 / refs 1, all five surnames** |
| `H4` `WT-094` — anchors in `tests/`, `scripts/`, `src/`? | clear |

All three probes fired their controls first, so **`H2`'s zero is a measurement, not a dark
predicate** (`WT-101`'s rule, applied).

### B · The patch (`scripts/wt123_paperII_mandatory_citations.py`)
Whole-paragraph anchors, `assert count == 1` on **every** anchor before any write, `.bak` first,
`--dry`, idempotence guard, character-width assertion, **and a new glyph guard** (see §THE TELL).
Seven edits: §3.1 credit paragraph · §6 rewritten in four paragraphs · §1's contribution 2
narrowed and pointed at §6 · both `paper-II` reference entries upgraded · the `paper-IV` issue
number corrected.

### C · Two bibliographic corrections, both at Crossref
- **`Physica A` 282(3) → 282(3–4).** `doi:10.1016/S0378-4371(00)00205-3` gives issue `"3-4"`.
  **Wrong in `paper-II.md` AND `paper-IV.md`, fixed in both.** `SCOUT-001` §8 had it right — the
  error was in the manuscripts, and it had survived every reference pass to date.
- **BBZ's standing *"page range to re-check"* flag is RESOLVED.** `doi:10.3982/ECTA8416` confirms
  *Econometrica* **79**(1), **123–157**. Closed with a source rather than deleted.
- Both `paper-II` entries move **✓ → ✓⧗** under `REFERENCE-POLICY` §4's pre-publication rule
  (arXiv `cond-mat/0002374`, NBER w14730). **`paper-IV`'s B&M entry KEEPS `✓` deliberately:** it
  quotes nothing, so it leans on no text. Different reliance, different mark — that is what a
  per-entry read-status disclosure *is*.

---

## THE GATE REFUSED, AND THAT IS THE SECOND STORY

**`G-V` failed at wrap.** Not on anything `-67` did — on a lesson a **live sibling session**
(`opus-florist-order`) had banked 49 minutes earlier, incident-tagged with no covering AAR. The
gate offered a one-line escape: adopt the AAR sitting within ±3 days, `stale-session-pointer-false-gate-fail`.

**That adoption would have been a false certification** — a stale session pointer has nothing to do
with a phone-order transcription near-miss — and `WT-102` is one day old and about exactly that:
*a false certification does not merely fail to fix a defect, it re-files it under a category that
stops anyone fixing it.* So instead of adopting, I opened the lesson body to see whether I could
responsibly write the AAR myself.

**The lesson body contained a full 16-digit, Luhn-valid Visa PAN.** A real customer's card, quoted
as the evidence for the lesson, auto-committed and **pushed** by `lessons.py add` in under four
minutes — into the repo every session greps at student-in, whose search output lands in context
windows. `claude-blackbook` is **private**, which is what makes this a cleanup rather than a
disclosure.

| what | state |
|---|---|
| working file redacted + pushed | ✅ `d5f09e31` — PAN gone from all future search output, gate logs and context |
| PAN still in git history and on `origin` | ⚠️ **Jason-sized** — Batter's Box `1217561667484767`, with a paste-able purge prompt |
| pre-commit hook cannot see PANs | 📋 State Machine `1217561601836055` |
| AAR filed, validated, lesson adopted | ✅ `pan-written-into-wisdom-repo`, sweep now **PASS** |

**Three things worth carrying forward, none of them about credit cards:**

1. **`G-AF` reports the pre-commit secret hook covering `114/114` repos and is GREEN. It passed a
   full PAN.** The hook is scoped to *secrets that authenticate us* — API keys, token prefixes,
   high-entropy strings. A card number is *regulated data about a customer*: sixteen low-entropy
   digits inside ordinary prose, space-separated, so even a naive `\d{16}` misses it.
   **`G-AF` measures COVERAGE, not CAPABILITY** — that a hook *runs* in 114 repos, never that it
   can *see*. That is `-64`'s tell one level out and `-66`'s applied to a security control.
2. **The predicate lesson repeated itself, in my hands, within the hour.** My first PAN sweep —
   13–19 digits with a separator allowed anywhere — returned **165 tree-wide hits** and was pure
   noise, because it spans prose and fuses unrelated numbers. Tightened to *16 contiguous digits or
   a **consistently**-separated 4-4-4-4*, then Luhn, then a known issuer BIN: **exactly 1 hit —
   `4111111111111111`, the universal Visa test card, in a docs fixture.** That hit is the
   predicate's **positive control**, and it is the only reason the rest of the tree reading clean is
   a measurement rather than a dark predicate. **A zero-hit sweep with no control is not a clean
   bill of health.** (`-66`, third time this week.)
3. **What actually caught this was a gate that forced a session to READ A DOCUMENT.** No scanner in
   the estate could have. `G-V` was failing about a missing *AAR* and found a *PAN* sideways. When
   `G-V`'s cost gets questioned — and it will, it is the noisiest check in the gate — that is the
   line to remember.

**The roster brake also paid out**, unprompted: `claude-blackbook` was claimed by the live sibling,
and the brake let a single-path `git add` through while refusing the `git add -A` shape — exactly
the distinction `git-add-all-sibling-tree` exists to enforce. When the AAR commit legitimately did
cover the whole dirty tree, `ROSTER_BRAKE_ACK=2` is the honest exit and `--no-verify` is not.

---

## THE TELL, now NINE deep

`-61`: a corpus under repair has a moving referent. `-62`: the line-wrap grep trap runs both
ways. `-63`: a backlog drain measures the backlog, not the paper. `-64`: a review apparatus's own
coverage is an unmeasured claim. `-65` (i): the fix for `WT-092` has `WT-092` — fire your repair,
don't read it. `-65` (ii): an instrument that reads prose cannot report on code. `-66`: a dark
predicate is not evidence of absence until a document you **know** contains the thing has made it
fire. `-66b`: a false certification re-files a defect under a category that stops anyone fixing it.

**`-67` ADDS:**

> ### AN INSTRUCTION THAT SAYS "CITE X WHEREVER Y APPEARS" CONTAINS A HIDDEN COUNT HYPOTHESIS, AND WHEN Y APPEARS NOWHERE THE CHEAP REPAIR IS TO WRITE Y IN.

That repair is **invisible in review** — the paper gains a claim *and* a citation for it in the
same commit, so the citation looks like the reason the claim is there. `WT-099` says treat *"N
places"* as a hypothesis. This is the case where **N = 0**, and it is the one that matters,
because a census that returns zero reads like a chore that found nothing rather than a finding.
It is `-66`'s lesson with the subject changed: `-66` measured whether the *instrument* could fire;
`-67` measured whether the *instruction* had a referent.

**And a second, smaller, entirely self-inflicted — three misses, one species: a name that renders
right and matches wrong.**

1. **The idempotence guard could not see its own edit.** `wt123` printed, in its own post-write
   verification, immediately after a successful apply: `sentinel present: False`. The sentinel was
   chosen from the *unwrapped* source string and the script's own `wrap()` broke it across a line
   before writing. **A re-run would have appended the paragraph twice.** Every other comparison in
   this session normalised whitespace first, because the manuscripts are hard-wrapped — **nobody
   thought of an idempotence check as a comparison against a hard-wrapped corpus, which is exactly
   what it is.** Fixed, and then **fired** (re-run now exits 2) rather than read.
   > **A guard's post-condition must be ASSERTED, not printed.** It printed `False` beside the
   > word `APPLIED` and returned `0`. The bug was one line; the near-miss was the exit code.

2. **U+00B5 vs U+03BC.** `SCOUT-001` writes the Pareto exponent as **MICRO SIGN**; the
   manuscripts use **GREEK SMALL LETTER MU**. They render identically and grep differently.
   Drafting §3.1's credit from `SCOUT-001` would have put the micro sign into a manuscript for the
   **first time** — measured: **6 files carry it, all `docs/` and `scripts/`, ZERO manuscripts.**
   `wt123` now refuses it; card `1217561398864561` asks for a guard that outlives the script.
   *(Underneath the codepoint was a semantic collision too: μ was already the growth drift. The
   new paragraph discloses the clash in the paper's own register — §3.1 already apologises for
   `a` — rather than shipping two meanings for one letter.)*

3. **The homograph canary fired and it was RIGHT.** Suite went **1 failed, 1077 passed** on
   `test_reg002_sec5_e4_extension_label.py::test_the_third_surface_scope_is_warranted`, which pins
   an identity over `scripts/`. `wt123` had named its edits `E1..E7` and an `_NEW`-suffixed
   constant on the fourth **contained the token without being it**. Renamed `ED1..ED7`; back to
   **1078**. **The canary works; the name was the bug; the test was NOT widened.**
   *And the docstring explaining all this tripped the canary a second time*, because the first
   draft spelled the token while explaining why not to. **A warning about a landmine is not exempt
   from the landmine.**

> **`WT-094` says grep `tests/` and `scripts/` for the manuscript strings you are about to edit.
> Necessary; NOT sufficient. A patch script is itself a new file in `scripts/`, and the
> repository's guards read it too.** Three of `-67`'s four self-inflicted problems were in the
> **instrument**, not the prose. The census walked `scripts/`, found its own anchor strings there,
> and reported four `*** UNSAFE ***` anchors — **an instrument that searches the tree it lives in
> manufactures its own collisions**, the same shape as `-66`'s `NO_LOSS_OFFSET` firing on *"without
> loss of generality."* **Read a census's self-hits before believing its refusals.**

---

## RULINGS NOW SETTLED — do not reopen
- **`DECISION-001` closed at A for good.** DO NOT RE-RUN THE LITERATURE SEARCH. `SCOUT-001` is the
  note, `WT-100` the fact, the instruments are committed. To extend it, extend the corpus in
  `wt118_fulltext_absence.py`; do not start over.
- **Paper IV's framing is RULED AND APPLIED** (`WT-102`). Do not re-litigate.
- **The `r = 1` cap and the stock-vs-flow contrast are CITED, not claimed** — and **`WT-103`: the
  `r = 1` cap is in NO MANUSCRIPT.** Do not "restore" it; it was never there.
- The 14 occurrences of *"from the household to the sovereign"* in `END-TO-END-001.md` and the
  `RESULT-E*.md` documents are **DELIBERATELY UNTOUCHED** — records of what the paper said at the
  time. Rewriting them falsifies history.
- **`REG-012` §4.7** (`WT-096`): `SEC_47_AT_REGISTRATION` immutable; a warranted edit **appends an
  Amendment**. **DO NOT widen `ROTTED` by glob.**
- **GREP `tests/`+`scripts/` before editing a manuscript string** (`WT-094`); **census before you
  patch** (`WT-099`). **Do not delete *"18 tests"* from Paper II's abstract.**
- **DO NOT re-derive** the κ residuals, `III-1`'s 4.2×, the `E2` blind pass, the
  P2-at-three-strengths lead (withdrawn).
- **DO NOT re-serve `REVIEW-004` by section number** — verbatim quotes only; **§A3 is the section
  every re-serving pass skips.**
- **`REVIEW-005` §2's `II-3` diagnosis is WRONG about the code** (`WT-098`).
- The **end-to-end pass is CLOSED** (T=2, A=0, E1–E6 spent).

---

## HONEST LOOSE ENDS
- **`wt117b_litsearch.py` still has not finished** (inherited, unchanged). Known-item tier
  completed 12 of 12 — the ceiling that matters — but the P/T/N sweep was still grinding at `-66`'s
  wrap and `/tmp/wt117b-results.json` was never written. Semantic Scholar rate-limits at ~124 s
  per failed call. **The verdict does not depend on it**; `wt118` is what licenses the claim under
  `REFERENCE-POLICY` §1 and it completed. Cheapest finish: drop Semantic Scholar from `SOURCES`
  (OpenAlex covers it) or add an API key, then re-run. Minutes, not an at-bat.
- **The board did not move.** 66 criteria before and after a session that edited two manuscripts
  and rewrote a related-work section. **No criterion tracks credit, reference marks or framing** —
  the same small finding `-66b` reported about Paper IV's title, now seen twice. Worth a thought
  when `P7`'s schema gets rebuilt.

---

## TOOLING (▲ = new at `-67`)
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh >
  /tmp/gate.log 2>&1 &`, then **two** polls of ~170 s. Grep the verdict line `GATE SELF-CHECK:`
  and `CANNOT VERIFY` expecting `0`. **Do not `grep -c "G-AL"`** — returns 1 on a green run.
- **WRAP SEQUENCE:** `gh_sha: PENDING` → commit → `--stamp` → commit → push → `--emit` → **PASTE
  INTO CHAT.** That last step is a step, not a courtesy — card `1217560480809492`.
- **`--emit` refuses on `REQUIRED`**, which is `[project, session_n, gh_repo, branch, gh_sha,
  updated, live_theme, phase, gate_passed, next_at_bat]` (`handoff_gate.py:50`). It was **never**
  refusing over `gate_passed`; handoffs since `-58` said so and were wrong. **Read the failure
  text, do not recall it.**
- **EDITED A PAPER? REGENERATE THE BOARD BEFORE THE GATE:** `./scripts/regen-board.sh --check` →
  *"matches measured reality (66 criteria)"*. **The wrapper is the only supported invocation** —
  bare `board.py` silently produces a degraded board.
- **ANY ABSTRACT EDIT:** `python3 scripts/check_abstract_size.py <PATH> --print` (takes a PATH).
  Paper II is at **244 words / 1478 chars**; Paper IV at 238/1585.
- **▲ `| tail` MASKS `$?` AND IT WILL BITE YOU ON PYTEST.** `-67` ran
  `pytest … 2>&1 | tail -8`, got `PYTEST_RC=0`, and the printed summary said **`1 failed`**.
  **Assert the printed number, always.** (Same family: `grep -c` exits 1 on a count of zero,
  which is a correct zero.)
- **▲ NAME YOUR PATCH SCRIPT IN A FREE `wtNNN` TAG. Tags now run to `wt123`; `wt124` is free.**
- **▲ AND CHECK YOUR IDENTIFIER NAMES AGAINST THE GUARDED NAMESPACES, not just your prose
  strings.** `scripts/` is policed by `test_reg002_sec5_e4_extension_label.py` for a per-script
  local exhibit label; naming a constant after it reds the suite. See §THE TELL (3).
- **A BATCHED PATCH SCRIPT BEATS N EDITS** — `wt123` is the newest example: whole-paragraph
  anchors, `assert count == 1` for EVERY anchor before any write, `.bak` first, `--dry`,
  idempotence guard **that is normalised and asserted**, character-width check, glyph guard.
- **A CENSUS MUST REPORT WHAT IT EXCLUDES** — `wt122` names its roots, prints its exclusions,
  states its hazard in advance, and carries a control per probe. Copy it, it is cheap.
- **`pdftotext` is on darwin** and handled 13 of 13 PDFs that fetched. NBER PDFs live at
  `https://www.nber.org/system/files/working_papers/wNNNNN/wNNNNN.pdf` with a browser `User-Agent`.
- **▲ CROSSREF IS FREE, INSTANT, AND SETTLES `to re-check` FLAGS.**
  `https://api.crossref.org/works/<DOI>` returns issue and pagination as JSON. `-67` closed a
  standing flag and found a wrong issue number in two manuscripts in about ninety seconds.
  **A bibliographic flag that survives five reference passes is usually one nobody costed.**
- **`dx` chokes on multiline / apostrophe-bearing command strings.** Write locally, `--put`, run
  there. `COMMITMSG.txt` → `--put` → `git commit -F`. Also true of `lessons.py add --text`.
  **For appending to a doc: `--put` to `/tmp/x.md`, then `cat /tmp/x.md >> docs/FILE.md`.**
- **USE ABSOLUTE LOCAL PATHS IN EVERY `cat X | dx --put`** — held again, zero cwd losses.
- **`lessons.py use`/`record-outcome` can hang past 4 min** — one per `dx` call at 300 s, never
  chained with `&&`. All returned in seconds this session; the hang is intermittent.
- **Asana `create_tasks` silently drops `projects`** — it did NOT this session (two cards, both
  landed first try, verified with `get_task opt_fields=projects.name`). ▲ **It DOES reject
  `assignee: null`** with a validation error; omit the key instead of nulling it.

---

## THE SELF-REVIEW TRIAD, answered in writing
1. **Captured everything for a zero-memory future Opus?** Yes. Two `LEDGER` entries; two committed
   instruments whose docstrings say *why* and record what the census changed about the card's own
   instructions; `.bak` beside both touched manuscripts; four lessons banked; three cards, one
   closed with the full measurement in its comment.
2. **Learned the hard way and not yet written down?** Now written: the count-hypothesis rule
   (`WT-104`, banked global), the normalised-and-asserted idempotence guard (banked global), the
   guarded-namespace rule and the two-codepoint glyph (banked global), and the project fact that
   the `r = 1` cap is in no manuscript (banked `wealth-tensor`, so no future session goes looking).
3. **The ONE thing that makes the next session's life easier, added THIS pass?**
   **`wt122`'s shape: a census that states, in a docstring, the specific hazard it exists to find
   — and then reports a ZERO as a result rather than as a clean bill of health.** `wt120` had the
   exclusions and the normalisation; `wt122` adds the part that mattered, which is that the
   instruction being executed is itself a claim to be measured. Runner-up: the Crossref line in
   TOOLING — ninety seconds to close a flag five passes had deferred.

---

## JASON-SIZED, not yours to decide
- **(a) `DECISION-001`** — closed for good. No follow-up on this axis.
- **(b) Paper IV's framing** — ✅ ruled and applied 2026-08-17 (`WT-102`).
- **(c) `P7` is still ONE BOOLEAN** for a criterion that is per-paper with a two-pass counter.
  Adding rows moves the 66, so it wants its own at-bat. **STILL THE ONLY OPEN JASON ITEM** — and
  on inspection it is really a **board-schema task with a ruling attached** rather than a judgement
  call, so **propose the schema and Jason can ratify it in one line.**
  ▲ **And when you do, look at whether ANY criterion should track credit and reference marks.**
  `-67` rewrote a related-work section, upgraded two reference marks and corrected a bibliographic
  error in two manuscripts, and **the board did not move by one criterion.** Twice now (`-66b` saw
  it with Paper IV's title). That is either fine or a hole, and nobody has said which out loud.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (and do not
let `| tail` tell you it passed); `roster leave --who` once; and **paste a handoff better than
this one into the chat as the last act.** 🥎
