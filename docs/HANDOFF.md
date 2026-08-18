---
project: wealth-tensor
session_n: 85
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 5182d05227384f36787e854765e953667e0fa5fa
updated: 2026-08-18
session: wealthTensor-85
live_theme: "THE CENSUS IS RUN AND IT LANDED ON THE SAMPLE'S LOWER BOUND, WHICH IS THE FINDING. -84 read twelve rows by hand and got k=5 of 12, Wilson 95% [25, 88] of 129. -85 swept all 129 by machine and got K = 25 — INSIDE the interval, exactly ON its lower bound. That is not the sample having been unlucky high; it is what a pattern sweep MUST return, and one row proves it: 7e1c612368, the fourth row -84 filed as LOCATED, is not one. Its evidence was `grep -n WT-059`, a genuine read, of the artefact the row names — which REVIEW-024's own pattern list excludes in a parenthetical. The commissioned post-condition and the commissioned pattern set contradicted each other. Bending D1 until it caught a grep -n would have been a rescued control, so the real second failure mode got its own detector (D2, under-coverage: the sentence names two artefacts, the evidence opened one) — and D2 IMMEDIATELY caught f43958893d, the mirror row on the same sentence, which had read WT-062 and never WT-059. Neither half had read the other. A pattern sweep can only find the shapes someone has already read: D2 exists because a human read the row first. So the census is a FLOOR under the sample, not a replacement for it, and [25, 88] is not narrowed."
phase: "All 25 flagged rows are repaired in-pass with evidence naming a real read, and every one of the 25 sentences HELD — 0 manuscript edits, 0 class changes, 0 promise_id changes. The file is now clean at its own criterion (wt154 RC 0). What -85 deliberately did NOT do is repair the two defect classes it counted and named rather than flagged: 16 rows whose evidence is `run on darwin, wealthTensor-82; output in the session log` (unreproducible, not undiscriminating) and 18 terse `git log/cat-file` rows. The 16 are -86's at-bat and they are the more dangerous class, because a row nobody can re-run is a row nobody can falsify — the TSV header's whole premise."
gate_passed: PENDING
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: MAKE THE 16 UNREPRODUCIBLE ROWS RE-RUNNABLE, BY RE-RUNNING THEM. Sixteen rows of docs/promises-adjudicated.tsv carry the evidence string `run on darwin, wealthTensor-82; output in the session log`. That evidence RAN something — it is a read of behaviour, so wt154 correctly does not flag it — but the session log is gone, so no later reader can re-check any of them. The TSV's own header says a row is a claim a human RAN OR READ the artefact, and step 2 of its falsification procedure is `run it or read it`. For these sixteen, step 2 is impossible. Write scripts/wt156_reproducibility_sweep.py: flag every adjudicated row whose evidence names a run whose output is not recoverable today — the `output in the session log` string is the known population, but write the RULE (a run with no committed output file, no printed value in the note, and no named test) rather than the string, and report how many rows the rule catches beyond the sixteen. RC 1 when any flags, RC 0 when none, --json. Then REPAIR ALL SIXTEEN BY ACTUALLY RUNNING THEM on darwin and recording, in the note, the value that came back TODAY. THE SEVERE TEST IS AGAIN SITTING IN GIT AND IT IS AGAIN THE POINT: at b50bccd the sweep MUST flag all sixteen; at your HEAD it MUST flag none — put that pair IN the script as post-conditions, at least two NEGATIVE. EXPECT TO FIND A FALSE SENTENCE. -84 found one in five hand-read rows and -85 found none in twenty-five, but -85's twenty-five were rows whose adjudicator had merely LOOKED at the right file; these sixteen are rows where nobody can tell what the adjudicator saw. If a re-run disagrees with its note, that is class R and the manuscript gets repaired in the same pass — say so loudly, it is the most valuable thing this at-bat can produce. DONE WHEN: wt156 exists and is committed with the b50bccd-vs-HEAD pair as post-conditions; all sixteen carry a command re-runnable today plus the value it returned today; docs/REVIEW-026 reports how many of the sixteen AGREED with their old note and how many did not, as a count not a vibe, and states in ONE sentence what a disagreement rate of that size does to REVIEW-024's [3, 47] of 129; wt148 RC 0, wt133 RC 0, wt154 RC 0; suite green AND SAY THE NUMBER; coach at baseline. DO NOT widen #scope to Papers I and II — still parked, still deliberate, FOUR passes running. DO NOT re-open the census; K=25 is measured and REVIEW-025 §5 already discloses its one weakness."
blockers: []
drift_flags: ["THE CENSUS IS A FLOOR AND MUST NOT BE READ AS A MEASUREMENT OF THE SAME QUANTITY THE SAMPLE MEASURED. K=25 is the rate of MECHANICALLY VISIBLE non-discrimination; k=5/12 estimates the TRUE rate. They landed consistent (25 is the interval's lower bound) and that is worth having, but nothing in -85 narrows [25, 88] or moves [3, 47] of 129. Any future session that quotes 25/129 as 'the error rate' is making the same mistake -83's '2 of 127' made, one level up.", "wt154's DETECTORS WERE REFINED AFTER THEIR AUTHOR READ FLAGGED ROWS — 33 -> 25 over four narrowings, every one made after looking, every one reducing the count. REVIEW-025 §5 lists all four in order with the row that caused each. This is the one thing -84's committed-before-scoring sample did NOT have, it cannot be undone retroactively, and the before/after post-conditions are a weaker guard than blindness would have been. Do not cite K as a blind measurement.", "SIXTEEN ROWS CANNOT BE FALSIFIED BY ANYONE, AND THE SWEEP CORRECTLY DOES NOT FLAG THEM. `run on darwin, wealthTensor-82; output in the session log` is a read of behaviour whose record is gone. Counted under `unreproducible` in wt154 --json and named in REVIEW-025 §4. This is -86's at-bat and it is the last named defect class in the file.", "EIGHTEEN MORE ROWS CARRY `git log/cat-file on darwin, wealthTensor-82` — those commands print content so the rows are reads, and terse is not the defect wt154 measures. But they name no object and print no value. If -86's rule for the sixteen is written generally rather than as a string match, check whether it catches these too, and say so either way.", "PAPERS I AND II ARE STILL OUT OF SCOPE AND 28 PROMISES THERE ARE CHECKED BY NOBODY. The sweep prints it on every run — not silent truncation. Widening `#scope` is ONE LINE of data and goes red immediately. FOUR passes have now parked it.", "THE VERSION STAMP IS STILL ONE RULING CLOSING THREE MANUSCRIPTS, and SEVEN consecutive passes have now correctly declined to move it on Jason's behalf. Paper III at Version 0.5 / 2026-08-12, Paper IV at 0.1 / 2026-08-16, both with repairs landed 08-18. Paper II card 1217568297674954.", "THE TWO-INDEPENDENT-READERS DESIGN IS NOW THE ONLY INSTRUMENT LEFT AND IT IS STILL JASON'S CALL. -82's prediction was the first cheap substitute, -84's audit the second, -85's census the third and last. REVIEW-025 §5 states why there is no fourth: a sweep can only find shapes someone has already read. Every remaining question about how many defects a reader would find now costs a reader.", "wt133 STILL HAS ITS ONE-DIRECTIONAL SWEEP-2 BLIND SPOT (entry -> body, never body -> entry). State Machine 1217593142996092. Unchanged.", "lessons.py's CONTRIBUTOR STAMP STILL DOES NOT RESOLVE FROM THE ROSTER — -85 hit it again and passed `--contributor big-wealthTensor-85` on every add, which works. 1534 of 2099 global leaves read 'unknown' and an unstamped leaf can never reach 'trusted'. Still teed up, not fixed: it lives in claude-blackbook, which a sibling holds a claim on."]
parking_lot: ["Widen `#scope` in docs/promises-adjudicated.tsv to paper-I and paper-II and adjudicate the 28 promises there. One line of data, then the work. FOUR passes have now parked this.", "The 18 terse `git log/cat-file on darwin, wealthTensor-82` rows: reads, but naming no object and printing no value. Fold into -86's rule if it generalises; otherwise tag wt157+.", "A THIRD sweep for pointers whose target is a bare noun phrase or a bare section number — the syntax -83's III-2 and III-3 live in, which both existing sweeps miss by construction. Candidate rule: any 'recorded in / named in / given in / listed in <X>' where <X> contains no backticked path and no §N.M. Tag wt157+.", "wt133 sweep 3: proper nouns in the body against a stop-list, to catch a body claim with no reference entry (IV-6's class). State Machine 1217593142996092.", "roster-brake's exit #1 cannot help when the paths you touched ARE the whole dirty tree; ROSTER_BRAKE_ACK=N is the answer and is ranked second. State Machine 1217596263441666."]
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."
---

# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

*Stamped by `scripts/handoff_gate.py --stamp`. If `gh_sha` above is not `HEAD`, this file was
committed without stamping — read `git log` rather than believing it.*

---

## STEP 0 · BRIDGE-BUG ACK, then transport (zero bridge calls)

The desktop bridge rotates its websocket every ~27–33 min (claude-code#81248). **DARLISH DOES NOT
USE IT.** Asana/Gmail/Twilio MCP tools ARE bridge-bound: if one vanishes mid-turn it self-heals in
~1s — retry next turn, and **never declare "can't continue" over it**. Never restart the Claude app
for a darlish problem.

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```
Post the printed `DARLISH-ENROLL v1 id=… fp=…` line, **EXACTLY**, as an Asana comment on task
**1217316841710435**; then run `/tmp/darlish-up` again; then

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-86 --task "The reproducibility repair: wt156 and the sixteen unrunnable rows"'
```

**READY first try at -61 through -85 — TWENTY-FIVE for twenty-five.** Budget four minutes; it takes two.

- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join (and prints an `absorbed N row(s)`
  line when it adopts a `cloud-<fp>` identity from an earlier command in the same container). -85
  saw `absorbed 2 row(s) ... (carried 1 claim(s))` and that is the healthy path, not a warning.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- `roster join` auto-claims the everything folder (resource = `~/Desktop/downloads` **expanded**).
  You do not have to remember it and you should not remove it.
- Run `rail` and `roster who` first. At -85's wrap the board carried `opus-spi-menu` (claims
  STALE, >13h) and a live `opus-florist-order`. Neither touches `wealth-tensor`. The rail lane was
  idle with metaQa / ledgerLens / helloRelay all `complete`.
- ⚠ `roster-brake` **WILL** block your first `git add` commit, reporting you as `cloud-<fp>`
  contending with your own human name. **`ROSTER_BRAKE_ACK=N` is the answer** and it is ranked
  SECOND in the brake's own output. Card 1217596263441666. -85 set it on every commit and lost
  nothing.

### THEN STAGE THE DOCS AS ONE TARBALL

```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'cd ~/repos/wealth-tensor && git pull --ff-only && tar czf /tmp/wt-docs.tgz docs scripts tests'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```

- ⚠ Stage `tests/` **too**.
- ⚠ `tar xzf` prints macOS xattr warnings with the extraction **perfectly fine**.
- ⚠ `.bak` files **sort first**. Read the path, not the first line.
- ⚠ **ANYTHING THAT IMPORTS `src/` MUST RUN ON DARWIN** — wt027 / wt002 / wt026 / wt071 / wt089 and
  all of pytest. `wt133` / `wt148` / `handoff_gate --coach` are pure-doc and run **locally in under
  a second**; run all three before you read anything. ▲ **`wt154` is NOT pure-doc** — its
  post-conditions shell out to `git show`, so it needs the repo and runs on darwin.
- ⚠ ABSOLUTE local paths in every `cat X | /tmp/dx --put`.
- ⚠ **NEVER** pipe a command through `dx` whose exit code you intend to read. -85 did it once on
  the first wt154 run and got an empty `RC=`; the fix is to redirect inside the remote command and
  echo `$?` there.
- ▲ Nested quotes → write the script **LOCALLY**, `--put` it, run `dx 'bash /tmp/x.sh'`. -83 wrote
  all seven of its scripts that way, -84 all six, **-85 all four**, and none of the three lost a
  turn. WRITE THE FILE.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt86/`, poll with a second
  `dx`. **pytest takes ~72s and is worth backgrounding**; -85 started it before the doc gates and
  it was done before they were read.

---

## THE STATE YOU INHERIT AND MUST PRESERVE

🟢 `python3 -m pytest tests/ -q` → **1094 passed, 0 failed, 72.46s.** RUN IT AND SAY THE NUMBER.
🟢 `python3 scripts/wt148_promise_sweep.py` → **RC 0**, paper-III **88 of 88** (81 H · 6 N · 1 R),
   paper-IV **41 of 41** (39 H · 2 R).
🟢 `python3 scripts/wt133_crossref_sweep.py` → **RC 0**.
🟢 ▲ `python3 scripts/wt154_evidence_discrimination_sweep.py` → **RC 0**, 129 rows, 0 flagged,
   **10/10 post-conditions, 4 NEGATIVE**. RC 2 means the sweep itself is broken and its count means
   nothing — that code is load-bearing, do not collapse it into 1.
🟢 coach: paper-III **5 conduct / 0 concessive**; paper-IV **1 / 0**.
🟢 GATE: **PASS**, gate v2.60.

**Wrap order:** commit → `--stamp` → commit → push → `charter-read.sh` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.

---

## ▶ YOUR AT-BAT · THE SIXTEEN ROWS NOBODY CAN FALSIFY

Read `next_at_bat` above; it is the specification and it is one thing. The short version:

Sixteen rows carry `run on darwin, wealthTensor-82; output in the session log`. wt154 does **not**
flag them and that is correct — running a script IS a read of behaviour, not a location. But the
session log is gone. The TSV header's step 2 is *"run it or read it"*, and for these sixteen there
is nothing to run and nothing to read. **A row nobody can falsify is worth exactly what -83 said an
unfalsified row is worth: nothing.**

Write the RULE, not the string — a run with no committed output file, no value printed in the note,
and no named test — and report what the rule catches beyond the sixteen (the 18 terse
`git log/cat-file` rows are the obvious candidate; say either way). Then **re-run all sixteen** and
record what came back today.

**Expect a false sentence.** -85 read 25 artefacts and found zero false sentences, but every one of
those 25 had an adjudicator who at least looked at the right file. These sixteen are rows where
nobody can tell what the adjudicator saw. A disagreement here is class R, repairs the manuscript in
the same pass, and is the most valuable thing this at-bat can produce.

---

## WHAT -85 DID

**The instrument.** `scripts/wt154_evidence_discrimination_sweep.py`, two detectors, reported
separately, with the `8855aba`-vs-HEAD pair inside it as post-conditions.

- **D1 · LOCATE-ONLY** — no read-operation in `evidence` targets the row's own artefact. **23 rows.**
- **D2 · UNDER-COVERAGE** — the sentence names a sibling programme ID the evidence never opened.
  **2 rows.**

**K = 25 of 129** at HEAD before repair; **29** at `8855aba`. REVIEW-024's interval was [25, 88].
**25 lands inside, exactly on the lower bound** — see REVIEW-025 §3 for why a pattern sweep must
read low and why that means the census does not narrow the interval.

**Why there are two detectors.** The handoff commissioned four rows the sweep MUST flag and a
pattern list to flag them with, and **the two contradicted each other**. `7e1c612368`'s evidence at
`8855aba` was `grep -n WT-059 docs/LEDGER.md` — a genuine read, of the artefact the row names, with
the found text quoted in its note. The same handoff's own parenthetical says *the `-l` is the tell;
`grep -n` is a read*. Widening D1 until it caught a `grep -n` would have been tuning the instrument
to a known answer. The row's actual defect was different — the sentence claims a record spanning
**WT-059 and WT-062** and the evidence never opened WT-062 — so it got its own detector. **D2 then
immediately caught `f43958893d`**, the mirror row on the same sentence, whose evidence had opened
WT-062 and never WT-059. Neither half had read the other, and nobody had noticed.

**The repairs.** `scripts/wt155_tsv_readnotlocate.py` — 25 rows, **12 post-conditions, 6 NEGATIVE**,
backup written before the edit, rolls back on any failure. **Every one of the 25 sentences HELD.**
Zero manuscript edits, zero `class` changes, zero `promise_id` changes (post-conditions bind all
four, which is what keeps wt148 at RC 0 instead of reporting 25 rows STALE).

**Three things the reading turned up that no detector could have:**

- **`fa005fbebe` / `af9d1b09c3` — the 62 is real and nobody had counted it.**
  `git show d655501:tests/test_edgar.py | grep -c '^def test_'` returns 42; `test_lag.py` 10;
  `test_lambda_sensitivity.py` 10. **42 + 10 + 10 = 62**, the number Paper III §11 gives. The rows
  carrying that claim had said `same test module`.
- **`a3511853e3` / `31fea3ed33` / `6db7b7ce3d` — the asymmetry the sentence draws is true in the
  commits.** `9722342` is *1 file changed, 283 insertions* (PRE-001 alone). `d655501` is 9 files:
  PRE-002's registration beside `edgar.py` (622) and `wt026_severe_test.py` (224). "Also contains
  the implementation" holds of the second and not the first, exactly as claimed.
- **`3df66f9481` — the twin of a row REVIEW-024 already repaired.** One sentence names
  `PREPRINT-CHECKLIST.md` *and* `docs/REFERENCE-POLICY.md`; `-84` repaired the checklist row and
  the policy row sat at `ls -l` until this pass. It holds (L226, *"Pass 1 — record verified against
  a publisher page, catalogue, Crossref or issuing body"*), but nobody had looked.

**RED-PROOF, this pass, on the real tree.** wt155 refuses and returns 2 unless the set of rows it
repairs is **exactly** the set wt154 flags; it also refuses if wt154 itself returns 2. After the
edit it re-runs the sweep at `8855aba` and requires all four REVIEW-024 rows still flag — proving
the repair moved the file, not the instrument.

---

## THE TELL, now SEVENTY-ONE deep

-61–-84 as before (-84 corrected -83's header from fifty-nine to sixty-five). **-85 adds six.**

**-85(i) A PATTERN SWEEP IS A LOWER BOUND ON A HAND-AUDIT'S QUANTITY, NEVER A REPLACEMENT** — it
can only find the defect shapes someone has already read. The census landed on the sample's Wilson
lower bound, and the proof it must is the one row that needed a second detector, which existed only
because a human had already read that row. Report the two as different quantities; do not let the
census narrow the interval.

**-85(ii) WHEN A COMMISSIONED POST-CONDITION CONTRADICTS THE COMMISSIONED PATTERN SET, THE HANDOFF
HAS BUNDLED TWO FAILURE MODES UNDER ONE NAME** — build the second detector, do not bend the first.
A post-condition you cannot satisfy honestly is evidence about the specification, not about your
instrument. The second detector paid for itself on its first run.

**-85(iii) AN INSTRUMENT REFINED AFTER ITS AUTHOR READ FLAGGED ROWS IS NOT A BLIND MEASUREMENT, AND
THE ONLY HONEST REPAIR IS TO ENUMERATE EVERY NARROWING IN ORDER WITH ITS CAUSE** — 33 → 25 over
four changes, all made after looking, all reducing the count, all listed in REVIEW-025 §5. This is
exactly what -84(ii)'s committed-before-scoring sample avoided by construction, and it cannot be
undone retroactively. Tuning you disclose is auditable; tuning you omit turns a measurement into an
argument.

**-85(iv) `grep -l` IS A LOCATOR EVEN THOUGH grep READS, SO PARSE THE FLAG CLUSTER, NOT THE COMMAND
NAME** — `-l` suppresses matched lines and prints filenames, so `grep -rln` is a locate despite the
`n`, and matching `/grep -[a-z]*n/` scores it a read. That bug silently un-flagged the very row the
sweep was written from. **The converse also bites:** when the claim is about WHICH FILES contain
something, `grep -l` IS the discriminating read, and a locate-detector over-flags it (`2f8a433aa7`).

**-85(v) REPAIRING ONE ARTEFACT OF A TWO-ARTEFACT SENTENCE LEAVES THE OTHER HALF EXACTLY AS BROKEN,
AND THE SENTENCE NOW LOOKS ADJUDICATED** — three instances in one file this pass. When an
enumerator emits one row per (sentence, artefact), the rows are individually adjudicable but the
SENTENCE is not adjudicated until all of them are. After repairing any row, grep for every other
row carrying the same sentence and do them in the same pass. (This is -84(iv) arriving from the
other side: -84 said grep the sentences that PROMISE things about a repaired target; -85 says grep
the SIBLING ROWS of a repaired row.)

**-85(vi) MECHANISING "THE ADJUDICATOR CHECKED A DIFFERENT ARTEFACT" OVER-FIRES UNLESS YOU SCOPE IT
TO ARTEFACTS THAT ARE FILES** — a claim about what `PRE-001` RETURNED is settled by reading
`RESULT-001`, never the registration; a claim about a module's pin is settled by a named green test
whose whole job is asserting about other modules. -83's judgement rule is sound and its naive
mechanisation is not.

---

## TOOLING (▲ new at -85)

- ▲ `scripts/wt154_evidence_discrimination_sweep.py` — the census instrument. `--json`, `--rev REV`,
  `--skip-postconditions`. RC 0 / 1 / **2 (post-condition failed — the sweep is broken)**. Reports
  `rescued` (3) and `unreproducible` (16) alongside the flags, so the classes it deliberately does
  not flag are counted rather than dropped.
- ▲ `scripts/wt155_tsv_readnotlocate.py` — the 25 re-adjudications, 12 post-conditions, 6 NEGATIVE,
  refuses unless its repair set equals wt154's flag set, rolls back from `.bak-wt155` on failure.
- ▲ `docs/REVIEW-025-adjudication-census.md` — K, the floor argument, the 25 repairs, the two
  unflagged classes, and **§5, the construction hazard**, which is the section a sceptic should
  read first. Five-way falsifier block in the front matter.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and will likely 429 — never put it in a critical
  path. Unchanged.
- Tags run to **wt155**; **wt156 is free**.

---

## ESTATE

**ONE card, with a named falsifier, unchanged:** `1217603625863293` — `RESULT-001-wt026.md`'s
summary line says "320 events" where its own §§1–2 report 120 and 202 (=322). Paper III prints 322
in both places and is unaffected. Not repaired in-pass on purpose: the ruling (*"may a later
session correct a non-registered arithmetic slip in a committed `RESULT-*.md` in place?"*) wants to
be made once, by Jason, then applied.

**Standing cards unchanged:** `1217593142996092` (wt133 sweep 2 one-directional),
`1217568297674954` (version stamp), `1217568192511533` (Paper II's nine orphans),
`1217596263441666` (roster-brake), `1217596233063153`, `1217561667484767` (PAN purge, Batter's Box).

**Nothing new was carded this pass.** The two remaining defect classes are assigned to -86 in
`next_at_bat`, which is where a Claude-sized job belongs.

---

## JASON-SIZED, not -86's

- **(a) THE TWO-INDEPENDENT-READERS DESIGN IS NOW THE ONLY INSTRUMENT LEFT.** -82's prediction was
  the first cheap substitute and it held; -84's audit was the second and it is spent; **-85's census
  was the third and last.** REVIEW-025 §5 states why there is no fourth: a sweep can only find the
  shapes someone has already read. Every remaining question about how many defects a reader would
  find now costs a reader.
- **(b) The version stamp** is ONE ruling closing THREE manuscripts; SEVEN consecutive passes have
  now correctly declined to move it.
- **(c) The `RESULT-001` in-place-edit ruling**, card `1217603625863293`.
- **(d) DECISION-001 closed, ROADS-001 unchanged.**
- **(e) wt077 already prints r·E[η⁺]/(1+μ)**, matching to 0.44% where Paper II §3.1's form is off
  4–7% — changes a stated contribution, unassigned since -81.
- **(f) The PAN history purge.**
- **(g) lessons.py's contributor stamp** still does not resolve from the roster; 1534 of 2099 global
  leaves read 'unknown' and an unstamped leaf can never reach 'trusted'.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-86` immediately before the gate; gate detached **with**
`GATE_ROSTER_WHO`; pytest **and say the number**; wt148 **and** wt133 **and** wt154 **and say all
three RCs**; `roster leave --who` once; run `lessons.py search` before finishing and
`use` + `record-outcome` at wrap (**-85 corroborated FIVE leaves — three of -84's four quarantined
leaves moved toward active — and banked SEVEN new, six of them global**); ⚠ pass `--contributor`
explicitly on every `lessons.py add`; paste a handoff better than this one as the last act — and
**assign -87 ONE at-bat with a definition of done. Do not hand them a menu.** 🥎
