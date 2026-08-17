---
project: wealth-tensor
session_n: 68
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-17
session: wealthTensor-68
live_theme: "Paper II's second independent read: two findings against pass 3's nine, both repaired in-pass — the first measured evidence of convergence in the batch. The inherited abstract question was decided, not deferred, and both B&M quotations were re-verified character-exact against the preprint itself."
phase: "Manuscript repair under a settled thesis, and the convergence counter is finally live: the NEXT independent read of Paper II is the first in the batch with a real chance of scoring a zero."
gate_passed: true
gate_version: "2.59"
next_at_bat: "PAPER IV's re-read after the narrowing — now the top of the order. §1 and §3 still carry the ladder framing in prose; 'composes from X to Y' is a SHAPE, not a string, and a grep cannot see a paraphrase. ~40 min. (Paper II's next read wants FRESH eyes — do not take it if you can help it two sessions running; the counter is only credible if consecutive passes are independent.)"
blockers: []
drift_flags: []
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-68` IN ONE LINE

**Paper II's second independent read found two, repaired two, and the trajectory is 9 → 2** —
plus the inherited abstract question (card `1217561330623702`) is **decided at (a), closed, do
not relitigate** (falsifier named on the card), and both §3.1 quotations now stand verified
**character-exact against the preprint's own text**, not against the corpus's copy of it.

Commit: this session's. Suite **1078 passed, 0 failed** before AND after (numbers read from the
summary line, per `-67`'s tail-masks-rc warning). Board **66 criteria, matches, unmoved**.
Abstract **untouched at 244/1478**.

---

## READ FIRST, in this order
1. **`docs/REVIEW-008-P7-pass-4.md`** — the pass of record. §4 is the card decision; §5 is the
   convergence arithmetic; §2's method note is the guard-kit checklist in its newest form.
2. **`docs/LEDGER.md` `WT-105`** (fact) and **`WT-106`** (method — the two-readings-of-a-prose-
   magnitude rule, which is `-67`'s two-codepoint μ one level up).
3. `scripts/wt124_paperII_p7pass4_edits.py` — small, but it is the full `-67` guard kit in 100
   lines and its idempotence guard was FIRED (exit 2), not read.

---

## YOUR AT-BAT — take one, in this order

### 1. **PAPER IV's re-read after the narrowing.** Top of the order now. §1 and §3 still carry
the ladder framing in prose even though the title and abstract no longer promise it. `wt120`'s
census found the phrase only twice and both are fixed — but *"composes from X to Y"* is a
**shape, not a string**, and a grep cannot see a paraphrase. Read §1–§3 with the narrowed claim
(`WT-102`) in mind. ~40 min.

### 2. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).

### 3. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first:
tightening the float tolerance to `==` hands the next machine a red suite. Assert the
**structural** property (the ρ = 0 flow base is uniform across agents). Note the manuscript's
claim itself is measured (`np.array_equal` True, max diff 0.0 — LEDGER); this at-bat is about
the APPARATUS catching a future regression, not about the claim.

### 4. **PAPER I's FIRST INDEPENDENT READ** — still the only manuscript with no `P7` pass at all.

### 5. **PAPER II's THIRD INDEPENDENT READ — the first with a live chance of a zero.** It is
deliberately NOT #1: the counter is only credible if consecutive passes are independent, and
`-68` just did pass 4. If you take it, diff against `.bak-wt68-p7` first, then read whole.
A zero-finding pass is a RESULT and gets its own REVIEW doc (`P7`'s rule).

### 6. **`REFERENCE-POLICY`'s sixth pass** — card `1217556161163494`. Third session running that
would have been saved by it existing.

### 7. **The U+00B5 guard** — card `1217561398864561`. ⚠ NOT in `tests/test_redistribution.py`,
whose 18 is quoted in the abstract; a new module is fine. (`-68`'s glyph census of Paper II
after its edits: 0 micro signs, 9 Greek mus — the guard would have passed today, which is when
you want to install it.)

### 8. **PASTE THE HANDOFF forcing function** — card `1217560480809492`. (`-67` and `-68` both
pasted it. Two data points, still not a fix.)

### 9. **Paper II's companion reference entries** — card `1217542940968749`.

### 10. **`A3` from the PAN AAR — the estate's highest-value loose thread, still unchecked:**
*where else do call transcripts and their `.srt` intermediates land, and is any of it committed
or pushed?* Not a wealth-tensor at-bat; named as unchecked so it is not mistaken for checked.

**FORCING LINE (`-59`'s ruling, kept): take none of the ten, say why in ONE LINE at the top of
your handoff.**

---

## WHAT `-68` DID, so you do not re-derive it

**One at-bat: Paper II P7 pass 4** (`docs/REVIEW-008-P7-pass-4.md`). Diffed against three
`.bak`s first, then read whole. Re-graded every repair since pass 3 — all hold. Verified both
B&M quotations **verbatim against the preprint full text** (ar5iv; the local PDF was gone).
Checked the two-rankings coherence (matched-rate vs matched-budget; consistent, and the credit
paragraph's "per unit of budget" is the B&M-congruent one). Confirmed `II-2`/`II-3` repairs and
the ρ = 0 structural identity's measurement. Verified §7's pin (`3b11f23` IS the last commit
touching `redistribution.py`, re-run this session) and the 18-test count (collected: 18).

**The two findings, both repaired via `wt124`:**
- **`II-13`** — §3.1's table stated no configuration for its flow rows (they run at ρ = 1, the
  constructor default). One-sentence table note added. The `II-12` species, one section over.
- **`II-14`** — *"a change of six parts in a million"*: exact read absolutely, ~13× off read
  ppm-relative. Now says `6 × 10⁻⁶`. Survived pass 3 verbatim.

**The card decision:** `1217561330623702` closed at **(a) leave the abstract** — no priority
claimed, the abstract's numbers are the paper's own (`WT-103`), credit is one click away in §1
contribution 2, and 244/250 cannot hold a citation abstracts do not carry anyway. **Falsifier
that reopens it: a referee reading the abstract as a priority claim** — then `WT-102`'s shape
(delete, don't argue) and the six words of slack.

Three lessons banked (two global), `use`/`record-outcome` corroborated for the two leaves this
read leaned on (`wt68-p2read → pass`).

---

## THE TELL, now TEN deep

`-61`: a corpus under repair has a moving referent. `-62`: the line-wrap grep trap runs both
ways. `-63`: a backlog drain measures the backlog, not the paper. `-64`: a review apparatus's
own coverage is an unmeasured claim. `-65`(i): fire your repair, don't read it. `-65`(ii): an
instrument that reads prose cannot report on code. `-66`: a dark predicate is not evidence of
absence until a known-positive document fires it. `-66b`: a false certification re-files a
defect under a category that stops anyone fixing it. `-67`: an instruction "cite X wherever Y
appears" hides a count hypothesis, and at N = 0 the cheap repair is to write Y in.

**`-68` ADDS:**

> ### BYTE-EXACT NUMBERS DO NOT CERTIFY THE SENTENCES AROUND THEM. A CENSUS OF VALUES IS NOT A CENSUS OF CLAIMS.

`-64` reproduced every number in §3's table byte-exact — and both of `-68`'s findings sat
touching that table: the table's *configuration* was never stated (`II-13`), and the prose
*framing* a verified number misstated its magnitude under the phrase's most natural reading
(`II-14`, in the `.bak` `-64` read). A pass's coverage is shaped by its question. The number
pass asked "does the value match?"; nobody had asked "does the sentence beside the value say
what the value says?" Corollary already banked as `WT-106`: a magnitude written as prose has an
absolute and a relative reading, and when they differ materially, **write the number**.

---

## RULINGS NOW SETTLED — do not reopen
- **Card `1217561330623702` DECIDED at (a).** The abstract stays. Reopen ONLY on the named
  falsifier (a referee reading it as a priority claim). The rationale is on the card and in
  `REVIEW-008` §4 — do not re-argue it from scratch.
- **`DECISION-001` closed at A for good.** DO NOT RE-RUN THE LITERATURE SEARCH. Extend the
  corpus in `wt118_fulltext_absence.py` if extending; never start over.
- **Paper IV's framing is RULED AND APPLIED** (`WT-102`). Do not re-litigate.
- **The `r = 1` cap and the stock-vs-flow contrast are CITED, not claimed** — and **`WT-103`:
  the `r = 1` cap is in NO MANUSCRIPT.** Do not "restore" it; it was never there.
- The 14 *"from the household to the sovereign"* occurrences in `END-TO-END-001.md` and
  `RESULT-E*.md` are **DELIBERATELY UNTOUCHED**. Rewriting them falsifies history.
- **`REG-012` §4.7** (`WT-096`): immutable; a warranted edit **appends an Amendment**. **DO NOT
  widen `ROTTED` by glob.**
- **GREP `tests/`+`scripts/` before editing a manuscript string** (`WT-094`) — and remember
  `-67`'s rider: your own patch script is a new file in `scripts/` and the guards read it too.
  **Census before you patch** (`WT-099`). **Do not delete "18 tests" from Paper II's abstract.**
- **DO NOT re-derive** the κ residuals, `III-1`'s 4.2×, the `E2` blind pass, the
  P2-at-three-strengths lead (withdrawn).
- **DO NOT re-serve `REVIEW-004` by section number** — verbatim quotes only; §A3 is the section
  every re-serving pass skips.
- **`REVIEW-005` §2's `II-3` diagnosis is WRONG about the code** (`WT-098`).
- The **end-to-end pass is CLOSED** (T=2, A=0, E1–E6 spent). The version stamp is `P8`/`P11`'s,
  pre-scored by `-64` — do not score it as a new finding.

---

## HONEST LOOSE ENDS
- **`wt117b_litsearch.py` still has not finished** (inherited, unchanged since `-66`). The
  verdict does not depend on it; cheapest finish is dropping Semantic Scholar from `SOURCES` or
  adding an API key. Minutes, not an at-bat.
- **The board did not move. Third time.** `-66b` (Paper IV's title), `-67` (a related-work
  rewrite + two reference upgrades), now `-68` (a config note + a magnitude repair). **No
  criterion tracks credit, marks, or framing.** When `P7`'s schema is rebuilt (Jason item (c)),
  this is the standing question to fold in.

---

## TOOLING (▲ = new at `-68`)
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh >
  /tmp/gate.log 2>&1 &`, then polls of ~170 s. Grep `GATE SELF-CHECK:` and `CANNOT VERIFY`
  expecting 0. Do not `grep -c "G-AL"` — returns 1 on a green run (and `grep -c` exits 1 on a
  correct count of zero; assert the printed number, never `$?` — same for pytest through
  `| tail`).
- **WRAP SEQUENCE:** `gh_sha: PENDING` → commit → `--stamp` → commit → push → `--emit` → **PASTE
  INTO CHAT.** `--emit` has TWO refusal limbs: missing `REQUIRED` fields, and `gate_passed` not
  the bare boolean `true` — **do not annotate frontmatter booleans** (`-67` proved it; a
  trailing `# comment` turns the YAML value into a string and it refuses).
- **EDITED A PAPER? REGENERATE THE BOARD BEFORE THE GATE:** `./scripts/regen-board.sh --check`
  → "matches measured reality (66 criteria)". The wrapper is the only supported invocation.
- **ANY ABSTRACT EDIT:** `python3 scripts/check_abstract_size.py <PATH> --print`. Paper II
  244/1478; Paper IV 238/1585.
- **▲ VERBATIM QUOTES: `ar5iv.labs.arxiv.org/html/<arxiv-id>` serves the FULL text** where the
  `/abs` page truncates. One fetch verifies a quotation character-exact when the local PDF is
  gone. (NBER PDFs: `https://www.nber.org/system/files/working_papers/wNNNNN/wNNNNN.pdf` with a
  browser `User-Agent`; `pdftotext` is on darwin.)
- **CROSSREF settles `to re-check` flags in seconds:** `https://api.crossref.org/works/<DOI>`.
- **▲ TAGS RUN TO `wt124`; `wt125` IS FREE.** Name your patch script in a free tag, and check
  identifier names against the guarded namespaces (`ED`-prefixed edit labels are the proven-safe
  shape; the exhibit-label canary polices the shorter one).
- **A BATCHED PATCH SCRIPT BEATS N EDITS** — `wt124` is the smallest complete example: whole-
  anchor `assert count == 1` before any write, `.bak` first, `--dry`, idempotence guard
  **normalised and ASSERTED and then FIRED**, glyph guard, char-width guard (characters, not
  bytes).
- **`dx` chokes on multiline / apostrophe-bearing strings.** Write locally, `--put`, run there.
  `COMMITMSG.txt` → `--put` → `git commit -F`. Appending to a doc: `--put` to `/tmp/x.md` then
  `cat /tmp/x.md >> docs/FILE.md`. **Absolute local paths in every `cat X | dx --put`** — third
  session running with zero cwd losses.
- **`lessons.py use`/`record-outcome`: one per `dx` call at 300 s, never chained.** Batched
  `add`s in a single `--put` shell script worked fine (`-68`, three adds, all pushed).
- **▲ `roster claim` syntax is `--who X --resource Y --task Z`** — the resource is a named flag,
  not positional (`-68` ate one usage error so you don't).
- **MULTI-SESSION IS REAL.** `roster who` before consequential work; the brake refuses the
  `git add -A` SHAPE; `ROSTER_BRAKE_ACK=<n>` is the honest exit, `--no-verify` is not.
- Asana `create_tasks` rejects `assignee: null` — omit the key. `add_comment` + `update_tasks`
  landed first try this session.

---

## THE SELF-REVIEW TRIAD, answered in writing
1. **Captured everything for a zero-memory future Opus?** Yes: `REVIEW-008` is the pass of
   record; `WT-105`/`WT-106` in the LEDGER; the card closed with rationale AND falsifier; three
   lessons banked; `.bak-wt68-p7` beside the touched manuscript; this handoff.
2. **Learned the hard way and not yet written down?** Now written: the two-readings rule
   (`WT-106`, global), the ar5iv path (global), the pass-4 record with the do-not-relitigate
   marker (project). The roster-claim syntax is in TOOLING above.
3. **The ONE thing that makes the next session's life easier, added THIS pass?** The
   convergence counter finally means something: 9 → 2 with both repaired makes the NEXT Paper II
   read the first that can plausibly score a zero — and this handoff deliberately queues it
   BEHIND Paper IV so the eyes are fresh. Runner-up: the quote-verification norm — a quotation
   inherited from a prior session is a claim, and one fetch turns it into a measurement.

---

## JASON-SIZED, not yours to decide
- **(a) `DECISION-001`** — closed for good.
- **(b) Paper IV's framing** — ruled and applied (`WT-102`).
- **(c) `P7` is still ONE BOOLEAN** for a per-paper criterion with a two-pass counter — the only
  open wealth-tensor Jason item. It is a board-schema task with a ruling attached: propose the
  schema, Jason ratifies in one line. Fold in the framing-criterion question (three sessions of
  board-didn't-move evidence now).
- **(d) The PAN history purge** — Batter's Box `1217561667484767`, paste-able purge prompt on
  the card. NOT a wealth-tensor item; do not rewrite `claude-blackbook` history on your own
  initiative.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary
line, never `$?` through a pipe); `roster leave --who` once; and **paste a handoff better than
this one into the chat as the last act.** 🥎
