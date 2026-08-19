---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-19
session: wealthTensor-88
session_n: 88
live_theme: "THE COUNT WAS A PROPERTY OF THE WORD LIST, AND THE PREDICTION MISSED FOUR, WHICH IS THE STRONGER OUTCOME. Three counts of the same class at 07cd47e under one criterion, differing only in vocabulary: wt160's sixteen surface forms find TEN; wt163's ~fifty a priori forms, commissioned by -87's handoff and never tuned against the corpus, find the SAME TEN and no new real one -- its six additions are all false positives; a reading that consults NO list, enumerating by the fixed structural element (the preposition ' in ') and adjudicating the free one (the verb), finds FOURTEEN. 10 and 14 are the numbers that settle it. The prediction, committed at c89f764 before wt163 existed, said 13 and the measurement said 17: three misses because the prediction's arithmetic counted the participle while the list it had just written also carried the 3sg, and one because \\b fires inside 'mis-specified', so the matcher read 'specified in' out of a word meaning the NEGATION of the verb matched. The author of a word list could not enumerate his own word list's consequences over 3,550 lines. That is the finding, and REVIEW-027's exact agreement could not have produced it."
phase: "SIX criteria green on Papers III and IV: wt148 RC 0 (135 adjudicated), wt133, wt154, wt156, wt160, wt163 all RC 0, suite 1095 passed. The four bare pointers NO verb list reaches were found by reading and repaired by hand (wt164), and wt164's E4 proves mechanically that wt163's flag set did not move across all four repairs -- the instrument could not have found them. The three promises those repairs emitted are adjudicated (wt165). What -88 did NOT do is the attack its own falsifier block names as the most valuable available: REVIEW-028 §6.4 measured that 341 of the corpus's 444 '<token> in <target>' constructions have a BARE target, which is why deleting the verb half does not make the criterion vocabulary-free. Nobody has read those 341. Until someone does, there is no ground truth against which any enumeration -- word-list or structural -- can be scored, and every count in this programme's pointer work rests on one reader's unlabelled judgement."
gate_passed: PENDING
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: BUILD THE LABELLED GROUND TRUTH, THEN SHOW WHETHER ANY VERB-FREE TEST RECOVERS IT. REVIEW-028 §6.4 established that the pointer criterion is irreducibly two-part -- 341 of 444 '<token> in <target>' constructions at 07cd47e have a bare target under N1..N6, and most are ordinary prose ('bites in pharmacokinetics', 'live in different worlds'), so flagging every bare target is useless. REVIEW-028 §8 falsifier 5 names the consequence: if a defensible sub-class of bare targets can be carved out STRUCTURALLY, without any verb list, the enumeration problem is soluble and this programme's pessimism about word lists is wrong. Nobody has tested it because nobody has the labels. Write `docs/pointer-groundtruth.tsv`: ALL 341 rows, one per construction, keyed by (file, verb-token, target) so it is recomputable, each labelled POINTER or NOT-POINTER with a one-line reason. READ THEM. Do not sample, do not shortcut with a verb list -- a ground truth built with a word list cannot score a word list. Then write `scripts/wt166_pointer_groundtruth.py`: it recomputes the 341 from 07cd47e, REFUSES if the file's key set differs by a single row (so the labels cannot drift from the corpus), and scores at least three candidate verb-free structural tests against the labels, reporting precision and recall for each. Candidates worth trying and worth REJECTING out loud: target head-noun definiteness; whether the sentence's subject is a claim rather than an object; whether the target admits a determiner+abstract-noun shape; sentence position within the section. COMMIT THE PREDICTION FIRST, before any scoring runs: predict, in writing, whether ANY verb-free test will clear a precision and recall you name in advance -- and predicting NO is a legitimate and probably correct prediction, so say it and say what would change your mind. DONE WHEN: docs/pointer-groundtruth.tsv holds all 341 rows labelled with reasons; wt166 exists, recomputes the 341 and refuses on any key-set drift, and scores at least three verb-free tests; docs/REVIEW-029 states, in ONE sentence someone could mark right or wrong, whether any verb-free structural test recovers the POINTER rows, WITH the precision and recall numbers that settle it; the prediction is a git object committed before the scoring ran; every new bare pointer the labelling turns up is repaired in-pass and any promise the repair emits adjudicated in the same pass, as wt165 did; wt148 AND wt133 AND wt154 AND wt156 AND wt160 AND wt163 AND wt166 all RC 0; suite green AND SAY THE NUMBER; coach at baseline. THE HONEST ANSWER MAY BE 'NO STRUCTURAL TEST WORKS' AND THAT IS A CELEBRATED RESULT, NOT A FAILED SESSION -- it would close the question of whether this class can ever be swept and hand the two-independent-readers design its final justification. DO NOT widen `#scope` to Papers I and II -- still parked, still deliberate, SEVEN passes running. DO NOT re-run REVIEW-028's vocabulary comparison; it is answered and re-measuring it is the cheap substitute for the work that is left."
blockers: []
drift_flags:
  - "THE 10-VS-14 GAP IS THE RESULT; THE 10-VS-10 AGREEMENT BETWEEN wt160 AND wt163 IS NOT A VALIDATION. Two a priori word lists agreeing measures the LISTS, not the corpus -- it is the same category error REVIEW-027 §5 warned about, one level out again. Anyone quoting 'wt163 confirmed wt160's ten' as evidence the sweep is complete has inverted the finding. The vocabulary-free reading found FOURTEEN."
  - "wt163's SIX FLAGS AT HEAD ARE ALL DISCLOSED FALSE POSITIVES AND THE FILE THAT HOLDS THEM IS PINNED. docs/pointer-exclusions.tsv carries three `held in` and three `holds in` rows, each with a reason; wt163's D3 REFUSES unless the file holds exactly those six. A successor who needs a seventh row must edit D3 and say so in a review. Do not silently append."
  - "THE PREDICTION MISSED FOUR AND THE MISS IS BANKED AS THE FINDING, NOT AS AN ERROR TO BE TIDIED. REVIEW-028 §6.1 states plainly that the session which WROTE the verb list could not predict its output. A successor tempted to 'correct' §5's predicted 13 to match the measured 17 would destroy the only evidence in this repository that word lists are not enumerations. §5 is a git object at c89f764 and must stay as written."
  - "\\b FIRES INSIDE A HYPHENATED COMPOUND AND THE GUARD IS NOW IN BOTH POINTER SWEEPS. `mis-specified in four ways` matched as `specified in`, whose meaning is the negation. `(?<![\\w-])` replaces `\\b` in wt160 and wt163; wt163's D13 proves the guard leaves REVIEW-027's published ten at 07cd47e untouched (10 -> 10) and wt160's C12 pins the case. The defect was LATENT in wt160 for its whole life. Any other token matcher over English prose in this repo has the same bug until checked."
  - "A REPAIR THAT NAMES AN ARTEFACT ADDS ROWS TO THE ADJUDICATION FILE -- unchanged and now twice-confirmed. wt164's four repairs emitted three promises and wt148 went red immediately. wt165 adjudicated all three H, keying each sentence off `wt148 --json` so it is byte-exact. Budget the adjudication into the SAME session or leave the tree red."
  - "AN EVIDENCE COMMAND THAT ASSERTS AN ORDERING MUST QUERY EACH ARTEFACT SEPARATELY. wt165's first PRE-001 evidence ran `git log --diff-filter=A` over the registration AND the pilot log in ONE invocation; the two dates print newest-first, attribute to neither file, and read naively appeared to show the result landing 35 minutes BEFORE its own pre-registration. Per file it shows the truth. An evidence column that cannot attribute its own output is worse than none, because it reads as diligence."
  - "wt154 HAS A BLIND SPOT -86 FOUND AND NOBODY HAS PATCHED: it scores an exit-code predicate as a LOCATE. Card 1217613775009402, named falsifier and shape of the fix inside. Unchanged at -88."
  - "PAPERS I AND II ARE STILL OUT OF SCOPE AND 28 PROMISES THERE ARE CHECKED BY NOBODY. The sweep prints it every run -- not silent truncation. Widening `#scope` is ONE LINE of data and goes red immediately. SEVEN passes have now parked it."
  - "THE VERSION STAMP IS STILL ONE RULING CLOSING THREE MANUSCRIPTS, and TEN consecutive passes have correctly declined to move it on Jason's behalf. Paper III and Paper IV both took prose repairs on 2026-08-19 (wt164) and neither stamp moved. Card 1217568297674954."
  - "THE TWO-INDEPENDENT-READERS DESIGN IS STILL THE ONLY INSTRUMENT LEFT AND IT IS STILL JASON'S CALL. -85's census, -86's runnability sweep, -87's bare-pointer sweep and -88's vocabulary comparison each asked a DIFFERENT question; none is a substitute and none reduces the case. -88 STRENGTHENS the case: §6.1's miss is direct evidence that a single reader building and predicting his own instrument is fallible in exactly the way that design exists to catch."
  - "wt133 STILL HAS ITS ONE-DIRECTIONAL SWEEP-2 BLIND SPOT (entry -> body, never body -> entry). State Machine 1217593142996092. Unchanged."
  - "lessons.py's CONTRIBUTOR STAMP STILL DOES NOT RESOLVE FROM THE ROSTER -- -88 hit it again and passed `--contributor big-wealthTensor-88` on all seven adds, which works. Still teed up, not fixed."
parking_lot:
  - "Widen `#scope` in docs/promises-adjudicated.tsv to paper-I and paper-II and adjudicate the 28 promises there. One line of data, then the work. SEVEN passes have now parked this."
  - "wt133 sweep 3: proper nouns in the body against a stop-list, to catch a body claim with no reference entry (IV-6's class). State Machine 1217593142996092."
  - "Patch wt154's D1 to score an exit-code predicate as a read, with a POSITIVE and a NEGATIVE, and disclose how far the count moves. Card 1217613775009402."
  - "N1..N6 DO NOT MODEL A PAGE NUMBER OR A COMMIT SHA. REVIEW-028 §4 marginals M6 and M7: `verified in the published text at p. 262` and `shipped in the same commit (d655501)` are substantively followable and formally bare. Carded rather than patched mid-pass, because adding N7/N8 moves a published count and needs its own severe test."
  - "Audit every other token matcher in scripts/ for the `\\b`-inside-a-hyphenated-compound bug wt163 surfaced. wt160 was fixed; nothing else was checked."
  - "roster-brake's exit #1 cannot help when the paths you touched ARE the whole dirty tree; ROSTER_BRAKE_ACK=N is the answer and is ranked second. State Machine 1217596263441666."
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."
---

# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

*Stamped by `scripts/handoff_gate.py --stamp`. If `gh_sha` above is not `HEAD`, this file was
committed without stamping — read `git log` rather than believing it.*

---

## STEP 0 · BRIDGE-BUG ACK, then transport (zero bridge calls)

The bridge rotates every ~27–33 min (`claude-code#81248`). **DARLISH DOES NOT USE IT.** Asana /
Gmail / Twilio MCP tools **are** bridge-bound: if one vanishes mid-turn it self-heals in ~1 s,
retry next turn, **NEVER declare "can't continue" over it.** Never restart the Claude app for a
darlish problem.

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
# post the printed DARLISH-ENROLL line, EXACTLY, as an Asana comment on task 1217316841710435
/tmp/darlish-up
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-89 --task "The labelled ground truth: wt166"'
```

**READY first try at -61 through -88 — TWENTY-EIGHT for twenty-eight.** Budget four minutes; it
takes two.

- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join, and prints `absorbed N row(s) …
  (carried 1 claim(s))` when it adopts a `cloud-<fp>` identity. That line is the healthy path.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- ▲ **Changing your own name mid-session:** `join` new → `claim` new → `leave --who <old>`.
- ⚠ `roster-brake` **WILL** block your first `git add` commit, reporting you as `cloud-<fp>`
  contending with your own human name. **`ROSTER_BRAKE_ACK=N` is the answer**, ranked SECOND.
  Card `1217596263441666`. -88 set it on every commit and lost nothing.
- At -88's wrap the rail lane was idle (metaQa / ledgerLens / helloRelay all `complete`) and the
  roster carried only `opus-florist-order` (STALE, claims the everything folder). Neither touches
  `wealth-tensor`. Run `rail` and `roster who` anyway; it costs one call.

### THEN STAGE THE DOCS AS ONE TARBALL

```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'mkdir -p /tmp/wt89'
/tmp/dx 'cd ~/repos/wealth-tensor && git pull --ff-only && tar czf /tmp/wt-docs.tgz docs scripts tests'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```

- ⚠ **`/tmp/dx --put` will NOT create a missing remote directory.** `mkdir -p` on darwin FIRST.
- ⚠ Stage `tests/` **too**.
- ⚠ `tar xzf` prints macOS xattr warnings with the extraction **perfectly fine**.
- ⚠ `.bak` files **sort first**. Read the path, not the first line.
- ⚠ **The local Bash tool's working directory PERSISTS between calls.** Lead with
  `cd /home/claude/wt &&` or use absolute paths.
- ⚠ **ANYTHING THAT IMPORTS `src/` MUST RUN ON DARWIN** — wt027 / wt002 / wt026 / wt071 / wt089 and
  all of pytest. `wt133` / `wt148` / `handoff_gate --coach` are pure-doc and run **locally in under
  a second** — run them before you read anything. `wt154` / `wt156` and **wt160's and wt163's
  post-conditions** shell out to `git show`, so those need the repo; both take
  `--skip-postconditions` if you only want the sweep locally.
  ▲ A script under `tests/` invoked directly needs `PYTHONPATH=src`.
- ⚠ ABSOLUTE local paths in every `cat X | /tmp/dx --put`.
- ⚠ **NEVER** pipe a command through `dx` whose exit code you intend to read — `$?` after a pipe is
  the *last* command's. Redirect inside the remote command and echo `$?` there. -88 lost one
  reading to exactly this.
- ▲ Nested quotes → write the script **LOCALLY**, `--put` it, run `dx 'bash /tmp/x.sh'`. -83 wrote
  all seven that way, -84 all six, -85 all four, -86 all six, -87 all five, **-88 all nine**, and
  none lost a turn. **WRITE THE FILE.**
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt89/`, poll with a second
  `dx`. **pytest takes ~70 s and is worth backgrounding.** ⚠ But a backgrounded pytest launched
  BEFORE a red sweep goes green will report that sweep's failure: -88 read a stale
  `1 failed, 1094 passed` from a run started before `wt165` adjudicated. **Re-run pytest after the
  last mutation, and read the run you started last.**
- ▲ **A `dx` call interrupted client-side may still have RUN on darwin.** Check for the effect
  before re-running a mutating one.

---

## THE STATE YOU INHERIT AND MUST PRESERVE

🟢 `python3 -m pytest tests/ -q` → **1095 passed, 0 failed, 67.31 s.** RUN IT AND SAY THE NUMBER.
🟢 `python3 scripts/wt148_promise_sweep.py` → **RC 0**, **135 adjudicated**: paper-III **90 of 90**
   (83 H · 6 N · 1 R), paper-IV **45 of 45** (43 H · 2 R). (132 before; wt164's repairs emitted three.)
🟢 `python3 scripts/wt133_crossref_sweep.py` → **RC 0**.
🟢 `python3 scripts/wt154_evidence_discrimination_sweep.py` → **RC 0**, 0 flagged, **0 of 135**.
🟢 `python3 scripts/wt156_reproducibility_sweep.py` → **RC 0**, 0 flagged, 4 NEGATIVE.
🟢 `python3 scripts/wt160_bare_pointer_sweep.py` → **RC 0**, **0 flagged of 13 considered**,
   **12/12 post-conditions** (C12 added at -88), including the `908d5b1^`-vs-`908d5b1` pair.
🟢 ▲ `python3 scripts/wt163_pointer_vocabulary.py` → **RC 0**, **21 considered, 6 flagged, all six
   disclosed-excluded, 0 undisclosed**, **13/13 post-conditions, 4 NEGATIVE**, including the
   `07cd47e`-vs-`c14aed3` pair. RC 2 = broken.
🟢 coach: paper-III **5 conduct / 0 concessive**; paper-IV **1 / 0**.
🟢 GATE: **PASS**, gate v2.60, `gate-selfcheck.sh` PASS, handoff-lint clean.

**Wrap order:** commit → `--stamp` → commit → push → `charter-read.sh` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.

---

## ▶ YOUR AT-BAT · LABEL THE 341, THEN SEE IF ANYTHING BUT A READER CAN FIND THEM

`next_at_bat` in the front matter is the full brief and it is binding. The short version:

REVIEW-028 answered its question — the count of ten was a property of the word list — and in
answering it produced a harder one. §6.4 measured that **341 of the corpus's 444
`<token> in <target>` constructions have a bare target**, so the obvious repair (delete the verb
list, flag every bare target) is useless: `bites in pharmacokinetics` is in that 341. The criterion
is irreducibly two-part. **But nobody has read the 341**, so there is no labelled set against
which ANY enumeration — a word list, a structural rule, a future reader — can be scored.

Build the labels. Then test whether any verb-free structural rule recovers the pointers from them,
with a precision and a recall you commit to **before** you score. **Predicting that nothing works
is a legitimate prediction and is probably the right one** — say so in advance, name what would
change your mind, and then a "no" is a result rather than a shrug.

---

## WHAT -88 DID

**The design, in one line:** three counts of the same class at `07cd47e` under ONE criterion
(same twelve-word window, same clause boundaries, same N1–N6), differing only in vocabulary.

- **A · `wt160`, sixteen surface forms, a priori by -87 → 10.**
- **B · `wt163`, ~fifty surface forms, a priori by -87's *handoff* → 17 first run, 16 after the
  tokenisation fix. Ten of them are wt160's ten, verbatim. The other six are false positives.**
- **C · the hand, NO list, enumerating by the preposition and adjudicating the verb → 14.**

`wt163` **imports** `wt160`'s `_flatten`, `_target_window` and `_is_named` rather than
re-implementing them, so "same criterion" is provable and not asserted — post-condition **D6** runs
this module with `wt160`'s own verb list and requires byte-identical output. The vocabulary is the
only difference, by construction.

**The prediction** (`c89f764`, committed before `wt163` existed) said **13** and named the three
`held in` false positives verbatim. The measurement said **17**. Three of the four misses were
`holds in` — the prediction's arithmetic counted the participle while the list it had just written
also carried the 3sg. **The session that wrote the word list could not enumerate its own word
list's consequences.** That is REVIEW-028 §6.1 and it is the finding.

**The fourth miss was better than a miss.** `specified in four ways` came from **`The instrument
was mis-specified in four ways`**: `\b` matches inside the hyphenated compound, so the matcher read
`specified in` out of a word whose meaning is the *negation* of the verb matched. `(?<![\w-])`
fixes it. **D13 proves the guard leaves `wt160`'s published ten untouched (10 → 10)**, which is why
it was applied to `wt160` too and pinned there as **C12**. A wider vocabulary did not find a bare
pointer; it found a bug that had been latent in the narrower instrument for its whole life.

**The four the instruments cannot see** — `visible in the parameter sweep`, `declared in the
registration before the pilot was run`, `printed in the same logs`, `verified in the sessions that
introduced them` — were found by reading and repaired by `wt164` in the two sanctioned charter
modes: two re-targeted (`PRE-001` §4.2; the `RESULT-002-*-run.log` pair), two removed (no artefact
exists for the sweep; *sessions* are not openable, so the mark table that defines the tick is named
instead). **`wt164`'s E4 is the post-condition that carries the claim: `wt163`'s flag set must be
BIT-IDENTICAL across all four repairs, and it is, 6 → 6.** An instrument that noticed these repairs
could have found the defects. Neither could.

**`wt165`** adjudicated the three promises those repairs emitted, all **H**, running every evidence
command inside itself. One nearly went in on evidence that *refuted* it — see the drift flag on
`git log` over several paths.

---

## THE TELL, now NINETY-TWO deep

-61–-87 as before. **-88 adds seven.**

- **-88(i) TWO A PRIORI WORD LISTS AGREEING MEASURES THE LISTS, NOT THE CORPUS.** Sixteen forms
  and fifty forms both returned ten; a reading with no list returned fourteen. Convergence between
  two instruments built the same way is not evidence about the world.
- **-88(ii) THE AUTHOR OF A WORD LIST CANNOT PREDICT WHAT HIS OWN WORD LIST WILL FLAG.** Wrote the
  list, wrote the prediction the same hour, missed four of seventeen. A vocabulary is a way of
  RE-FINDING what someone already found, not of finding the class.
- **-88(iii) `\b` FIRES INSIDE A HYPHENATED COMPOUND.** `mis-specified in` matched as `specified
  in`. Use `(?<![\w-])`. The bug can sit latent in a narrower instrument forever and surface only
  when a widening happens to include a token that occurs as a compound tail.
- **-88(iv) WIDENING A VOCABULARY BUYS FALSE POSITIVES BEFORE IT BUYS FINDINGS.** Six additions,
  six false positives, zero findings. Budget a disclosed exclusions file, pinned by a
  post-condition to the set the PREDICTION named, so it cannot grow silently.
- **-88(v) `git log` OVER SEVERAL PATHS PRINTS DATES YOU CANNOT ATTRIBUTE, AND READ NAIVELY THE
  ORDER APPEARS TO REFUTE WHAT IT SUPPORTS.** Query each artefact separately whenever the claim is
  an ORDERING.
- **-88(vi) DROPPING THE WORD-LIST HALF OF A TWO-PART CRITERION MAKES IT USELESS, NOT
  VOCABULARY-FREE.** Measure the denominator the list selects from BEFORE proposing to remove the
  list: 341 of 444 here.
- **-88(vii) A POST-CONDITION CAN BE WRONG THREE TIMES IN ONE SESSION AND NONE OF THEM IS A VERDICT
  ON THE REPAIR.** D1 compared sets and collapsed duplicate flags (ten read as eight); D3 pinned a
  predicted count the measurement exceeded; E8 asserted a line-count drift that hard-wrapped
  anchors made wrong. Five in two sessions now. **Flatten whitespace in the detector AND in the
  repair's own post-conditions** — -87(vii), earned again by the same mechanism.

---

## TOOLING (▲ new at -88)

- ▲ `scripts/wt163_pointer_vocabulary.py` — `--json`, `--rev REV`, `--census`,
  `--skip-postconditions`; RC 0/1/2. **Imports wt160's criterion**; 13 post-conditions, 4 NEGATIVE;
  D4/D5 pin the instrument's BLINDNESS as NEGATIVEs rather than widening it away.
- ▲ `docs/pointer-exclusions.tsv` — six disclosed false positives with reasons, pinned by D3.
- ▲ `scripts/wt164_offlist_pointers_repaired.py` — 8 post-conditions, 3 NEGATIVE; **E4 requires
  wt163's flag set to be bit-identical across the repairs**; rolls back from `.bak-wt164`.
- ▲ `scripts/wt165_tsv.py` — 13 post-conditions, 4 NEGATIVE; refuses unless wt148 reports exactly
  its three ids; runs all three evidence commands inside itself.
- ▲ `docs/REVIEW-028-pointer-vocabulary.md` — §3 the vocabulary-free method and the 341 denominator,
  §4 the fourteen listed verbatim plus seven disclosed marginals, §6.1 the miss, §6.2 the
  tokenisation defect, §6.3 the one-sentence verdict, §7.2 the three wrong post-conditions, §8
  seven falsifiers.
- `scripts/wt160_bare_pointer_sweep.py` — now 12 post-conditions (C12, the tokenisation guard).
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
- Tags run to **wt165**; `wt166` is free.

---

## ESTATE

Two cards with named falsifiers: `1217603625863293` (RESULT-001's "320 events" against its own
120+202=322 — the ruling wants to be made once, by Jason) and `1217613775009402` (wt154's predicate
blind spot). Standing: `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`.

## JASON-SIZED, not -89's

(a) **The two-independent-readers design** — still the only instrument left, and -88 strengthens
the case rather than substituting for it: §6.1's miss is direct evidence that one reader building
and predicting his own instrument is fallible in exactly the way that design catches.
(b) the version stamp; (c) the RESULT-001 in-place-edit ruling; (d) DECISION-001 closed, ROADS-001
unchanged; (e) `wt077` already prints r·E[η⁺]/(1+μ), matching to 0.44% where Paper II §3.1's form
is off 4–7% — changes a stated contribution, unassigned since -81; (f) the PAN history purge;
(g) `lessons.py`'s contributor stamp.

---

## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)

`docs/CHECKLIST.md`'s first OPEN lane in dependency order is **P13** (the arXiv-ready PDF) and this
pass did not touch it. That is deliberate drift and it is **guard work**, so per the gate's own
instruction: **the claim the guard protects is P7's.**

P7 closes a paper when two consecutive fresh-eyes passes yield zero substantive findings — evidence
only if the checks that found nothing were *capable* of finding something. -83 found a row that had
checked the wrong artefact; -84 measured the rate at 5 of 12; -85 put a floor of 25 of 129 under it;
-86 established that 46 rows could not have been re-checked by anyone; -87 showed a pointer naming
no artefact was invisible to every sweep. **-88 closes the question -87 left open and opens a worse
one: the sweeps that see pointers see them through a WORD LIST, and the list is not the class.** Two
independently chosen a priori vocabularies find the same ten; a reader finds fourteen. A paper
cannot be closed on passes whose completeness is a property of somebody's verb list — so P7's bar
now depends on whether the class can be enumerated at all, which is -89's at-bat and may well
answer *no*.

---

## THE SELF-REVIEW TRIAD, ANSWERED IN WRITING (gate v2.60, G-A / G-B / G-G)

**1 · Did we capture everything for a zero-memory future Opus?** Yes, and the test is that every
claim here has a command beside it. `wt163` carries its criterion **by importing wt160's**, so the
two instruments cannot drift apart, and carries the vocabulary under test, the reason that
vocabulary was NOT tuned, and its own blindness (D4, D5) in the module docstring rather than only in
the review. `wt164` and `wt165` carry their rationale, post-conditions and rollback; `wt165`'s
docstring carries the near-miss on `git log` in full, because the *discarded* evidence command is
the part a successor would otherwise rediscover. `REVIEW-028` carries the prediction, the
measurement, the MISS, the tokenisation defect, the one-sentence verdict, the three wrong
post-conditions and seven falsifiers whose #5 is the next at-bat. **Undo path:** every edited
manuscript has a `.bak-wt164`, the TSV a `.bak-wt165`, the handoff a `.bak-wt88`, and every step is
a separate commit — `c89f764` the prediction, `ae06184` the unrun instrument, `2984726` the
measurement and repairs, `d3a8124` the review. Reverting `2984726` restores all four off-list bare
pointers and leaves `wt163` **green**, which is precisely the finding.

**2 · What did we learn the hard way that is not yet written down?** All seven are banked in
`claude-blackbook` (six global, one project-scoped, all stamped `--contributor big-wealthTensor-88`)
and restated as **-88(i)–(vii)** above. The three that cost the most: `\b` fires inside a hyphenated
compound, so a verb matcher reads `specified in` out of `mis-specified in`; a `git log` over several
paths prints dates you cannot attribute and can appear to refute the claim it supports; and a
backgrounded pytest launched before a red sweep goes green reports the stale failure — read the run
you started **last**.

**3 · What ONE thing makes the next Opus's life easier, and did we add it THIS pass?** Added, this
pass: **`wt164`'s E4 turns "this instrument is blind here" from a sentence in a review into a check
that fails if anyone quietly widens the instrument to cover it.** Four real defects were repaired
and the sweep's flag set did not move by one byte. That is the shape every future blind-spot claim
in this repository should take. And the honest half: **-88's own prediction missed four**, the miss
is written up as the result rather than tidied away, and §5 is pinned as a git object so a
successor cannot quietly correct it. The single most useful thing -88 leaves behind is the number
**341** — the denominator nobody had measured, which converts "widen the word list" from an
obvious next step into a measurably bad one.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-89` immediately before the gate; gate detached **with**
`GATE_ROSTER_WHO`; pytest **AND SAY THE NUMBER**; wt148 AND wt133 AND wt154 AND wt156 AND wt160
AND wt163 AND wt166 **AND SAY ALL SEVEN RCs**; `roster leave --who` once; paste a handoff better
than this one as the last act — and assign -90 **ONE** at-bat with a definition of done. Do not
hand them a menu. 🥎
