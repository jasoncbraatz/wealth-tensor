---
project: wealth-tensor
session_n: 70
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-17
session: wealthTensor-70
live_theme: "Paper IV's §4–§10 read against the narrowed framing — three findings, three edits, and then a fourth edit to undo the placement of the third. The ladder phrase was still alive in §4.1 with its articles dropped, §8 carried a cross-reference that -69's own repair had falsified two hours earlier, and §9 did not carry the limitation the abstract advertises. The board caught the repair that every guard in the kit passed."
phase: "Manuscript repair under a settled thesis. Paper IV's framing is now propagated through §10; the manuscripts are clean of the ladder in every form a grep reaches. Paper II's convergence counter is live, untouched since -68, and has a real chance of a zero."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered: Paper II's THIRD independent read (9 → 2 → this one). Untouched since -68, so the eyes are as fresh as they get, and it is the only startable item that can move the project's definition of done — Paper IV's scoped passes do not count under WT-091. Diff against .bak-wt68-p7 FIRST, then read whole. DONE WHEN: Paper II read end-to-end, every finding repaired in-pass or carded with a named falsifier, REVIEW-011 written with its own explicit not-checked list, suite/board/coach green. A ZERO IS THE POINT — it advances the counter and it is a result, not a failure to find anything. ~40 min. Blocked? take the first startable item in the queue and say which, in ONE LINE, at the top of your handoff."
blockers: []
drift_flags: []
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-70` IN ONE LINE

**Took the assigned at-bat as ordered.** Paper IV §4–§10 against `WT-102`: **three findings, three
edits** (`wt126`), and then **a fourth edit** (`wt127`) because the board flipped a criterion red
on a repair that changed no sentence. The biggest finding was **the ladder phrase itself**, alive
in §4.1 with both definite articles dropped — invisible to the census that certified its absence.

Commits `d8fc6bd`←…→HEAD. Suite **1078 passed, 0 failed** before AND after. Board **66 criteria,
matches** — it **moved once and came back**, which is the most informative thing it has done in
five sessions. Coach **0/1, at baseline**. Abstract **untouched at 238/1585**.

---

## READ FIRST, in this order
1. **`docs/REVIEW-010-P7-paperIV-sections4to10.md`** — the pass of record. **§2 is the one to
   read even if you skip the rest**: it is the story of a repair that passed every guard in the
   kit and was caught by the board. **§3 is the CLEARED list** — what was read and found innocent,
   including both sites `-69` predicted. **§4 names what this pass did NOT look at.**
2. **`docs/LEDGER.md` `WT-110`** (an ordinal is a criterion), **`WT-111`** (the censused string is
   not the only string; a scope note needs two halves), **`WT-112`** (Paper IV has ten sections).
3. **`scripts/wt126_…py` and `scripts/wt127_…py`** — the guard kit, plus the two guards that were
   not in it. `wt125` remains the *exemplar*; `wt126` adds the census classifier and the rewrap
   guard, `wt127` adds the reorder guard.

---

## YOUR AT-BAT — ASSIGNED. Do not choose.

> # ▶ `-71`, YOUR AT-BAT IS: **PAPER II'S THIRD INDEPENDENT READ.**
>
> **Start here. You do not need to read the rest of this section to begin, and you are not being
> asked to weigh it against anything.** ~40 min.
>
> **What it is.** Paper II's `P7` convergence counter stands at **9 → 2**: pass 3 found nine
> findings, pass 4 (`-68`, `REVIEW-008`) found two. `-69` and `-70` both worked Paper IV and
> neither opened Paper II, so **the eyes are as fresh as they get** and this is **the first pass
> with a live chance of a zero**. It is also the only startable item that can move the project's
> `definition_of_done`: Paper IV's last two passes were **scoped** (one question, part of one
> manuscript) and do **not** count under `WT-091`. Paper II's counter is the one that converges.
>
> **How.** `diff` `paper-II.md` against **`.bak-wt68-p7` first** — `-61`'s tell, and `-70` is fresh
> evidence it runs in both directions, so also ask *what has been changed under this paper since
> `-68`* (answer: nothing; verify it rather than believe this line). Then **read it whole**,
> end-to-end, not by grep. Census before patching (`WT-099`), one batched guarded script
> (**`wt128` is free**; `wt125` is the exemplar and `wt126`/`wt127` add three guards to it), board
> and coach and suite after.
>
> **Two things this paper specifically will punish you for.** (1) **Do not delete "18 tests" from
> Paper II's abstract** — it is quoted in `tests/test_redistribution.py` and the coupling is
> deliberate. (2) Paper II's abstract is **244/1478** and closest to its ceiling of any manuscript;
> run `check_abstract_size.py` even if you believe you did not touch it.
>
> **DONE WHEN:** Paper II has been read end-to-end; every finding is either repaired in-pass or
> carded with a named falsifier; **`REVIEW-011` exists and carries its own explicit not-checked
> list**; suite green, board re-checked, coach at baseline. **A ZERO IS THE POINT HERE, not a
> disappointment** — it advances the counter, and `-70` is direct evidence that "I looked hard and
> found nothing" is a result this project pays for. A zero still gets `REVIEW-011`.
>
> **IF AND ONLY IF THIS IS GENUINELY BLOCKED** — not merely less appealing than something below —
> take **the first item in the queue you can actually start**, and say in ONE LINE at the top of
> your handoff which you took and what blocked this one. That is the forcing line (`-59`'s ruling,
> kept, pointed at the assignment).
>
> **`-72`'s likely assignment, so you can write your handoff cheaply:** **Paper I's first `P7`
> pass.** It is still the only manuscript with no pass at all and it is now by a wide margin the
> oldest untouched thing in the batch. If Paper II returns a zero, `-72` is where the marginal
> value is; if Paper II returns findings, `-72` is Paper II's fourth read instead.

### THE QUEUE BEHIND IT — context, not a menu. Do not shop here.

Listed so you can *recognise* an item if your assigned at-bat collides with it, and so the next
handoff has a ranked pool to assign from. **Reading this list is not a decision you are being
asked to make.**

1. **PAPER I'S FIRST INDEPENDENT READ** — still the only manuscript with no `P7` pass at all.
   Likely `-72`.
2. **Paper IV §1–§3, re-read against `wt125`'s OWN output** (~15 min, new this session). `-69`
   read §1–§3 against `wt121` and then patched them; **nobody has read them against `wt125`.**
   `IV-15` is proof that a repair's blast radius leaves its own range, and `wt125`'s blast radius
   inside §1–§3 has never been swept. Small, cheap, and created by the work rather than inherited.
3. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
4. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first: tightening the
   float tolerance to `==` hands the next machine a red suite. Assert the **structural** property.
5. **`REFERENCE-POLICY`'s sixth pass** — card `1217556161163494`. **Fifth** session it would have
   saved. `-70` did not read Paper IV's References either.
6. **The U+00B5 guard** — card `1217561398864561`. NOT in `tests/test_redistribution.py`; a new
   module is fine. Three patch scripts now carry an in-script glyph guard; the tree-wide one is
   still missing.
7. **The `CONDUCT_ALLOWED_SECTIONS` gap** — card `1217562682350929`. `-68` hit it; `-69` and `-70`
   both avoided it only by reading the tuple first. A landmine three sessions have walked around.
8. **▲ NEW: a gate check that a `§N` named in `HANDOFF.md` exists in the paper it names** — card
   `1217564707330383`, filed this session (`WT-112`). ~6 lines. The board already locates sections
   by name because hard-coding `## 8` was a defect once; a handoff naming a range makes the same
   hard-coded claim in a file the gate reads.
9. **PASTE THE HANDOFF forcing function** — card `1217560480809492`. (`-67` through `-70` all
   pasted. Four data points, still not a fix.)
10. **Paper II's companion reference entries** — card `1217542940968749`.
11. **`A3` from the PAN AAR — estate-level, STILL UNCHECKED:** where else do call transcripts and
    their `.srt` intermediates land, committed or pushed? Not a wealth-tensor at-bat; named as
    unchecked so it is not mistaken for checked.

---

### ⚖️ WHEN YOU WRITE YOUR OWN HANDOFF: **ASSIGN, DON'T OFFER.** (Jason's ruling, 2026-08-17)

**`HANDOFF-GATE.md` v2.60, G-F recipe slot 5.** Name ONE at-bat, give it a definition of done
someone could mark right or wrong, put everything else under a heading that says it is not a menu,
keep the forcing line but point it at the assignment, and name your best guess at the *next*
session's assignment. **The outgoing session is strictly better positioned to choose than the
incoming one** — it knows what it just touched, what it deliberately left, and which eyes are
fresh, and none of that survives the gap. A menu is a decision handed backwards through the gap,
the one direction a handoff cannot carry anything.

`-70` is the first handoff written under the rule as well as the second written to obey it, and it
reports one thing the rule's author could not have known: **assigning is cheap when you have just
finished.** The choice took under a minute, because the ranking data was in this session's own
head. That is the asymmetry, measured once.

---

## WHAT `-70` DID, so you do not re-derive it

**One at-bat: Paper IV §4–§10, read against `WT-102`.** Diffed against `.bak-wt69-p7` first, read
each section end-to-end on one question — *does this prose assert the ladder, or bound a claim the
abstract no longer makes?*

**The three findings, three edits, all repaired via `wt126`:**
- **`IV-14`** — §4.1's objection, stated in a referee's voice, opened *"You claim a unit that
  **composes from household to sovereign**."* **That is the phrase `WT-102` removed, minus both
  definite articles.** `wt120` censused *"from **the** household to **the** sovereign"* and
  correctly reported it gone; the report was true of a string that differs from this one by two
  function words. Severity is higher than its position suggests: §4.1 is **the paper putting words
  in a referee's mouth about what the paper claims**, at maximum exposure, so after `wt121` the
  abstract and §4.1 disagreed and **§4.1 read as the real position with the abstract as the
  hedge** — the exact inversion `WT-102` exists to prevent. Now: *"a unit that keeps one type at
  the household, firm and sovereign scales and survives being summed"*, which is also the
  **stronger** objection, because it lands on the paragraph's own closing line.
- **`IV-15`** — §8 said *"What is left is weaker, **is what §3 now says**, and is still worth
  publishing: <two-item list>."* **`wt125`'s `ED2` added a third conjunct to §3's closing that
  same day.** `-69` coined the blast-radius tell and generated a fresh instance of it, one section
  outside the range it was reading, while writing the sentence about it. **Repaired by DELETING
  the cross-reference** (`WT-098`): §8's first sentence already names §3, and a paraphrase of
  another section's content is a standing drift generator that nothing measures.
- **`IV-16`** — the narrowed abstract makes exactly **two** headline statements and the second is
  a **limit** (*"those scales share one question, not one structure"*). **§9, titled Limitations,
  carried seven items and none of them was that one.** The limit lived in §3 and §8; §4.4's own
  heading (*"stated here rather than in §9"*) shows the paper treats §9 as the default home and
  **announces** departures. **The narrowing promoted the limit and nobody moved it.** Added to §9,
  worded from §3 and §8 so nothing new is asserted.

**And then `wt127`, which is the part worth your five minutes.** `wt126` placed the new limitation
**first**. Every guard passed — census over 379 files, anchors `== 1` literal and normalised, an
**identity** guard proving all seven pre-existing item bodies survived the renumber byte-for-byte,
set-based width guard, glyph guard, document-wide coach guard. Suite 1078. Then
`regen-board.sh --check` went **STALE** and **`P5g` flipped ✅ → 🔨**, because `P5g` greps **item
1** for `A composed state nobody can read`. `wt127` moves the new item to position 2. It does
**not** reword it to carry `P5g`'s phrase — that satisfies the checker while demoting the item the
criterion protects — and it does **not** edit `wt126`, because `wt126` ran (`-69`'s ruling on
`wt124`, kept). **The two-script trail is the finding.**

**Also done, unassigned, because it was thirty seconds and it closed a named gap:** the
content-word census (`compos.*household.*sovereign` and reverse, whitespace-collapsed) across all
four manuscripts. **Papers I, II, III: zero. Paper IV: two, both correct post-narrowing text.**
The ladder is gone from the manuscripts in every form a grep reaches.

**Six lessons banked, five global, one `use` corroborated.** One card filed to State Machine
(`1217564707330383`).

---

## THE TELL, now FOURTEEN deep

`-61`: a corpus under repair has a moving referent. `-62`: the line-wrap grep trap runs both ways.
`-63`: a backlog drain measures the backlog. `-64`: a review apparatus's coverage is an unmeasured
claim. `-65`(i): fire your repair, don't read it. `-65`(ii): an instrument that reads prose cannot
report on code. `-66`: a dark predicate needs a positive control. `-66b`: a false certification
re-files a defect where nobody fixes it. `-67`: "cite X wherever Y appears" hides a count
hypothesis. `-68`: byte-exact numbers do not certify the sentences around them. `-69`(i): a
framing patch's blast radius is every line that agreed with the old framing in its own words.
`-69`(ii): a guard on a self-describing document must be written in identity, not quantity.

**`-70` ADDS TWO.**

> ### (i) A CENSUS AND AN IDENTITY GUARD PROVE WHAT THE TEXT *SAYS*; NEITHER LOOKS AT *WHERE IT SITS*.

Every guard in the kit answers *what does the text say* — by string, by set, by normalised
identity. Not one answers *where does it sit*, and position is exactly what an insertion changes
about everything below it. **In a corpus that measures list position, an ordinal is a criterion.**
`wt126` changed no sentence and turned the board red. The same holds for reordering a table's
rows, renumbering a section, or moving a paragraph between sections a criterion locates by name.
**Operational rule: before editing a document, grep the criteria that govern it for positional
language** — `grep -nE "FIRST ITEM|first item|\^1\.|last section" docs/done-criteria.tsv`. Five
seconds. It is `-69`'s *read the instrument, and read it early*, pointed at the board instead of
the gate.

And the reason the board caught it is worth as much as the tell: **`P5g` is written positionally
(*"THE FIRST ITEM"*) and its check was tightened at some point to look IN item 1 rather than
anywhere in the file. A weaker criterion would have stayed green while the paper's flagship
self-costing limitation quietly became item 2. A criterion strict enough to be annoying is a
criterion strict enough to fire.**

> ### (ii) THE CENSUSED STRING IS NOT THE ONLY STRING — AND A SCOPE NOTE NEEDS TWO HALVES.

`-69` said *a paraphrase has no string*, and that is right. `IV-14` is the sharper case: **the
paraphrase HAD a string, and it was not the one anybody censused.** Articles, auxiliaries and
prepositions are exactly what a writer drops when compressing a clause. **Census a phrase over its
CONTENT WORDS IN ORDER**, not over the phrase as typed.

And `IV-15` is the same failure in the scope note rather than the census. `REVIEW-009` §5 honestly
declared *what it read*. What no read-range can carry is that **an edit made inside a read range
lands outside it.** **A scope declaration needs two halves: what I read, AND what I changed** —
the second is a coverage claim on sections the first never mentions. `REVIEW-010` §4 is written
that way; copy the shape.

---

## RULINGS NOW SETTLED — do not reopen
- **Paper IV's framing is RULED (`WT-102`) and is now PROPAGATED THROUGH §10.** Do not
  re-litigate. What remains is §1–§3 against `wt125`'s own output (queue item 2) — that is work
  created by a repair, not a reopening.
- **`wt126` is NOT to be edited** and neither is `wt124`. Both ran; both exit 2 on re-run; editing
  a spent script falsifies the record of what ran. The successor script is the fix.
- **§9's item 1 is `P5g`'s and stays there.** Do not insert ahead of it, and do not reword the
  criterion's phrase into a different item to make room.
- **Card `1217561330623702` DECIDED at (a).** Paper II's abstract stays. Reopen ONLY on the named
  falsifier; rationale on the card + `REVIEW-008` §4.
- **`DECISION-001` closed at A for good.** DO NOT RE-RUN THE LITERATURE SEARCH; extend
  `wt118_fulltext_absence.py` if extending, never start over.
- **`WT-103`: the `r = 1` cap is in NO MANUSCRIPT.** Do not "restore" it; it was never there.
- The 14 *"from the household to the sovereign"* occurrences in `END-TO-END-001.md` and
  `RESULT-E*.md` are **DELIBERATELY UNTOUCHED** — rewriting them falsifies history. Same for
  `patch_wt56_e1_remedy.py`'s quoted text and for every `paper-IV.md.bak-*`. **`wt126` formalised
  this**: its census partitions hits into **live / historical (`.bak-*`) / spent one-shot** and
  asserts uniqueness only over live. Copy that partition; do not loosen the assertion instead.
- **`REG-012` §4.7** (`WT-096`): immutable; a warranted edit **appends an Amendment**.
- **GREP `tests/`+`scripts/` before editing a manuscript string** (`WT-094`); **census before you
  patch** (`WT-099`). **Do not delete "18 tests" from Paper II's abstract.**
- **DO NOT re-derive** the κ residuals, `III-1`'s 4.2×, the `E2` blind pass, the
  P2-at-three-strengths lead (withdrawn).
- **DO NOT re-serve `REVIEW-004` by section number** — verbatim quotes only; §A3 is the one every
  re-serving pass skips.
- **`REVIEW-005` §2's `II-3` diagnosis is WRONG about the code** (`WT-098`).
- The **end-to-end pass is CLOSED** (T=2, A=0, E1–E6 spent). The version stamp is `P8`/`P11`'s,
  pre-scored by `-64` — do not score it as new.

---

## HONEST LOOSE ENDS
- **The board MOVED, and that is the news.** Four sessions of "66/66, unmoved" were evidence that
  no criterion tracks credit, marks, framing or internal consistency — `-69` repaired a factually
  **false** sentence without moving it. `-70` moved it, with an edit that **changed no sentence at
  all**, by displacing an ordinal. **The board measures structure, and it measures it well; what
  it does not measure is whether the prose is true.** That sharpens Jason item (c) rather than
  softening it: the instrument works, and it is pointed at a different axis than the one five
  sessions of findings have been on.
- **`wt117b_litsearch.py` still has not finished** (inherited, unchanged since `-66`). The verdict
  does not depend on it; cheapest finish is dropping Semantic Scholar from `SOURCES` or adding an
  API key. Minutes, not an at-bat.
- **`REVIEW-010` §4 names what this pass did not check** — Paper IV's numbers/citations/apparatus,
  its References, §1–§3 against `wt125`, whether Papers I–III *paraphrase* Paper IV's old framing
  (the *string* census is now a clean zero; paraphrase is untested), and Paper I's total absence
  of a `P7` pass.
- **`claude-blackbook` was claimed by a live sibling (`opus-florist-order`) for this whole
  session** and carried one uncommitted metadata line of theirs throughout. `lessons.py` commits
  and pushes **only the leaf it just wrote**, so all six `-70` lessons banked cleanly around it.
  **That is a property of `lessons.py` worth knowing**: you can bank into a claimed repo without
  touching a sibling's working tree. Do not generalise it to `git add`.

---

## TOOLING (▲ = new at `-70`)
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh >
  /tmp/gate.log 2>&1 &`, then polls of ~170 s. Grep `GATE SELF-CHECK:` and `CANNOT VERIFY`
  expecting 0. **Assert the printed number, never `$?`.**
- **WRAP SEQUENCE:** `gh_sha: PENDING` → commit → `--stamp` → commit → push → `--emit` → **PASTE
  INTO CHAT.** `--emit`'s four known refusal limbs: missing `REQUIRED` fields (`-66`);
  `gate_passed` not a bare boolean (`-67`); `G-COACH-3` non-increasing vs
  `docs/.coach-baseline.json` (`-68`); `gh_sha ≠ HEAD` with content changed since the stamp
  (`-68`). **`-70` found no fifth limb either** — two clean sessions running, because both read
  the tuples before writing rather than after being refused.
- **▲ NEVER PIPE A COMMAND WHOSE EXIT CODE YOU INTEND TO READ THROUGH `dx`.**
  `dx 'cmd | tail -6'` returns **`tail`'s** exit code, not `cmd`'s. `-70` ran
  `regen-board.sh --check | tail -6`, saw the word STALE in the output and `RC=0` underneath it,
  and had to re-run unpiped to learn the check had actually failed. Same family as the standing
  *"say the number, never `$?`"* rule, one layer out: **a pipe launders a failure into a
  success.** If you need both the text and the code, run it twice or use `PIPESTATUS`.
- **EDITED A PAPER? REGENERATE THE BOARD BEFORE THE GATE:** `./scripts/regen-board.sh --check` →
  "matches measured reality (66 criteria)". ▲ **And if it says STALE, `regen-board.sh` then
  `git diff --stat docs/CHECKLIST.md`** — an empty diff means the board came back to where it was
  and there is nothing to commit, which is a different and much better outcome than a criterion
  that stayed red.
- **▲ THE BOARD IS ALSO A POSITIONAL INSTRUMENT.** `docs/done-criteria.tsv` holds the actual shell
  for every criterion, one per row, readable with
  `awk -F"\t" '/P5g/{for(i=1;i<=NF;i++) print i": "$i}' docs/done-criteria.tsv`. **Read the row
  before you edit the thing it measures.** `P5g` pins Paper IV §9 **item 1**; `P5f` measures
  Abandoned-approaches *body-ness* by requiring a further numbered section after it; `P5h` locates
  Data-and-code **by name** and records *"III is 11, IV is 10, II is 7"*. All three are position
  claims that ordinary prose edits can break silently.
- **ANY ABSTRACT EDIT:** `python3 scripts/check_abstract_size.py <PATH> --print`. Paper II
  **244/1478** (closest to ceiling), Paper IV 238/1585. Run it even when you believe you did not
  touch the abstract.
- **THE GUARD-KIT EXEMPLAR IS `wt125`; `wt126`/`wt127` ADD THREE GUARDS TO IT.** Take `wt125`
  whole, then add whichever of these the edit calls for:
  - **census classifier** (`wt126`) — partition hits into live / `.bak-*` historical / spent
    one-shot, print all three, assert uniqueness **only over live**. Without it the guard fails on
    every anchor in this corpus; loosening it instead hides a real live duplicate.
  - **rewrap guard** (`wt126`) — when a repair rewraps a paragraph, assert the **normalised text
    after the changed sentence** is identical in anchor and replacement. A rewrap is an excellent
    place to hide an edit and the diff will not show you.
  - **reorder guard** (`wt127`) — for a swap or renumber, assert the **multiset of item bodies** is
    unchanged **and** the exact new order, and assert a pure reordering leaves the document's word
    multiset unchanged. Idempotence must then be checked on **position**, since no body changes —
    a content sentinel is blind to a reorder.
- **▲ `wt126`'s spent-one-shot check is the shape to copy for "is this dead code?":** search for
  the script's name on a line that **also** carries an execution verb (`python`, `import `,
  `subprocess`, `$(`). A line that merely names it is a citation — `wt125`'s docstring names
  `patch_wt56` — and a name-only grep will tell you a spent script is live.
- **▲ TAGS RUN TO `wt127`; `wt128` IS FREE.** `ED`-prefixed edit labels are the proven-safe shape.
- **`dx` chokes on multiline / apostrophe-bearing strings.** Write locally, `--put`, run there.
  **ABSOLUTE local paths in every `cat X | dx --put`** — the container's cwd resets between `Bash`
  calls, and when `cat` fails, `dx --put` **blocks on empty stdin until the tool timeout** instead
  of erroring. Signature: a `--put` silent for more than a few seconds is reading an empty pipe.
  (`-70` paid this zero times, by using absolute paths from the first call.) A
  `git commit -F /dev/stdin <<'MSG'` heredoc through `dx` **commits and then returns RC=2**; check
  `git log`, don't re-commit.
- **▲ `lessons.py add` COMMITS AND PUSHES ONLY THE LEAF IT WROTE**, so it is safe to run in a repo
  a sibling has claimed and left dirty. `use`/`record-outcome`: one per `dx` call at 300 s, never
  chained. Batched `add`s in a single `--put` shell script work fine (`-70`: six `add`s, one
  `use`, one `record-outcome`).
- **`roster claim` syntax is `--who X --resource Y --task Z`** — resource is a NAMED flag.
  `roster join` returns RC=0 with **no output** on a re-join: success, not a hang.
- **MULTI-SESSION IS REAL.** `rail` + `roster who` before consequential work; the brake refuses the
  `git add -A` SHAPE — explicit-path staging goes through clean.
- Asana `create_tasks` rejects `assignee: null` — omit the key.

---

## THE SELF-REVIEW TRIAD, answered in writing
1. **Captured everything for a zero-memory future Opus?** Yes: `REVIEW-010` is the pass of record,
   its §3 is the **cleared** list and its §4 the **not-checked** list; `WT-110`/`WT-111`/`WT-112`
   in the LEDGER; six lessons banked; `.bak-wt70-p7` and `.bak-wt70-p9order` beside the
   manuscript; `wt126` and `wt127` committed and readable; one card filed; this handoff.
2. **Learned the hard way and not yet written down?** Now written: the ordinal tell (`WT-110`,
   global), the content-word census and the two-halved scope note (`WT-111`, global), the
   delete-don't-resync rule for stale cross-references (global), the census classifier (global),
   Paper IV's section inventory (project), and the `dx` pipe-launders-a-failure trap (TOOLING).
3. **The ONE thing that makes the next session's life easier, added THIS pass?** **`REVIEW-010`
   §3 — a CLEARED list, not just a not-checked list.** Every pass in this project has recorded
   what it did not look at; none has recorded **what it looked at and found innocent, and why**.
   §4.4's "degraded link" and "Paper III's ladder results" both look like defects to a cold reader
   working from `WT-102`, and both are fine for reasons that take ten minutes to re-derive and one
   paragraph to record. **A pass that reports only its findings and its gaps silently invites the
   next pass to re-open everything in between.** Runner-up: the assignment above is written from
   `REVIEW-010` §4, so the not-checked list and the next brief are the same list. Bronze: three
   named guards added to the kit, each with the failure that earned it.

---

## JASON-SIZED, not yours to decide
- **(a) `DECISION-001`** — closed for good.
- **(b) Paper IV's framing** — ruled and applied (`WT-102`); propagated through §10 as of `-70`.
- **(c) `P7` IS STILL ONE BOOLEAN** for a per-paper two-pass criterion — **the only open
  wealth-tensor Jason item.** Propose the schema, Jason ratifies in one line; fold in whether ANY
  criterion should track credit, marks, framing or internal consistency. ▲ **`-70` sharpens the
  evidence rather than repeating it.** Four sessions read "the board never moves" as *the board is
  insensitive*. `-70` moved it — with an edit that changed **no sentence** — and moved it back.
  **The board is a working instrument pointed at STRUCTURE: position, presence, naming. It is
  silent on whether a sentence is true.** `-69` repaired a factually false claim (firms are not
  households summed) with the board unmoved; `-70` shifted an ordinal and the board fired within
  seconds. That is not a broken instrument; it is a **missing axis**, and it is a cleaner thing to
  ask Jason to rule on than "the board seems insensitive."
- **(d) The PAN history purge** — Batter's Box `1217561667484767`, paste-able prompt on the card.
  NOT a wealth-tensor item; do not rewrite `claude-blackbook` history on your own initiative.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary
line, never `$?`, and never through a pipe you then read the exit code of); `roster leave --who`
once; and **paste a handoff better than this one into the chat as the last act.**

**And when you write it: ASSIGN ONE AT-BAT WITH A DEFINITION OF DONE. Do not hand `-72` a menu.**
You will know things at wrap that a cold session cannot recover — spend them on the choice. 🥎
