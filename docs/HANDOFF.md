---
project: wealth-tensor
session_n: 73
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 58f7f5bb05d32932d5f1332c1a79f28f3a1d1e11
updated: 2026-08-18
session: wealthTensor-73
live_theme: "Paper III's first independent read, taken as assigned. SEVEN findings, thirteen edits, one carded — the largest single-pass haul in the project, on the only manuscript in the definition of done that had never been reviewed. Three are WT-117's species exactly (a universal falsified by its own list four lines below it). Four are a NEW species the project now has a name and a script for: a cross-reference is a quantifier over a SECTION, it is falsified only against text hundreds of lines away, and a reviewer physically cannot hold that in their head. Two twenty-line sweeps found three of them. The manuscript's own References section documents four verification passes, one of them literally 'every entry checked against the body', and one of these sat through all four."
phase: "Manuscript repair under a settled thesis. Paper III is now read once and its counter opens at 7. Paper II's counter runs 9 → 2 → 4 → 3 across six passes and has not converged. The review method is still outrunning the manuscripts, and the instrument set now has three axes: quantifiers (wt130), cross-references (two loops, twenty lines, unwritten as a committed script), and census-and-guard (wt128/wt129)."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered: PAPER II'S FIFTH INDEPENDENT READ — the first half of the consecutive-zero pair the definition of done requires. -70's rule is back in force and this is it. RUN THE TWO CROSS-REFERENCE SWEEPS FIRST (REVIEW-013 §3 gives both, twenty lines each): Paper II carries ~40 §x.y references and NOBODY HAS EVER CHECKED ONE, and its References section has never been read for anything but quantifier counts — seven sessions deferred. THEN the wt130 sweep (155 tokens on 118 lines), THEN read it whole. DONE WHEN: both sweeps run and recorded in REVIEW-014 with their counts; Paper II read end-to-end; every finding repaired in-pass or carded with a named falsifier; REVIEW-014 exists with its own cleared list AND its own not-checked list; suite green, board re-checked, coach at Paper II's baseline of 2 conduct / 0 concessive. A ZERO IS THE OUTCOME THIS PROJECT NEEDS and would be the first half of the pair — say so plainly if you get one, and do not manufacture a finding to avoid it. Blocked? take the first startable item in the queue and say which, in ONE LINE, at the top of your handoff."
blockers: []
drift_flags: ["-72 set -70's 'Paper II returns findings → next session is Paper II again' rule aside for ONE session so Paper III could be read. That is discharged: Paper III has now had a pass. The rule is back in force and -74 is Paper II. Do not set it aside a second time without a manuscript in definition_of_done that has zero reads — and there is no longer one.", "The queue's old item 1, 'Paper I's first P7 pass', remains demoted to 13: Paper I is NOT in definition_of_done and Paper II §7 calls it 'since superseded by its own internal referee'. Carried unchanged from -71 and -72, still correct.", "PAPER III'S COUNTER OPENS AT 7 AND THE PAIR IS UNSTARTED. Paper III needs two consecutive zero-finding passes and has had one pass finding seven. Nothing about that is alarming on a first read of 2,694 lines, but do not let the queue forget it: definition_of_done requires the pair for II, III AND IV."]
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-73` IN ONE LINE

**Took the assigned at-bat as ordered: Paper III's first independent `P7` read.** Ran `wt130`
first, read all 2,694 lines, and then ran two cross-reference sweeps that took twenty lines each
and found three findings a careful read cannot find. **Seven findings, thirteen edits (`wt131`),
one carded with a falsifier.** Paper III's counter opens at **7**.

**The new instrument is the deliverable and it is not a script yet.** `wt130` mechanised the
quantifier. The class it does *not* reach is the **cross-reference** — and `§N.M` is a quantifier
too, over a section, falsifiable only against text hundreds of lines away. Four of seven findings
are that shape. Two loops close them and both are in `REVIEW-013` §3, ready to lift.

Suite **1078 passed, 0 failed** (67.2 s). Board **66 criteria, `docs/CHECKLIST.md` unmodified —
the board did not move, for the fourth consecutive session.** Coach **RC 0, all four at baseline**
(III = 5/0). Abstract and title **byte-identical**, asserted in `wt131`'s guards.

---

## READ FIRST, in this order

1. **`docs/REVIEW-013-P7-paperIII-pass1.md`** — the pass of record. **§2's `III-3` is the one to
   read even if you skip everything else**: §11, the data-and-code statement, scoped the whole
   repository's provenance to *"§A.2 and §2"* four times and labelled a script *"Regenerate §2"* —
   and §2 carries no table and no measured number, while **§6.1 writes the same scope correctly,
   twice, 500 lines upstream.** §3 is a **27-row CLEARED list** with every read-forward verdict
   spelled out, §4 is the **NOT-CHECKED list and your brief is written from it**, and Appendix A is
   the full 668-row enumeration you can diff against a fresh run.
2. **`docs/LEDGER.md` `WT-120`** — the tell, and the two loops. **This is the thing to carry into
   Paper II**, because Paper II has ~40 cross-references and nobody has ever checked one.
   `WT-119` is the findings; `WT-121` is what it costs to go *through* a registered freeze rather
   than around it, and it costs two commits.
3. **`scripts/wt131_paperIII_p7pass1_edits.py`** — `wt129`'s guard honesty plus a thirteen-anchor
   census that came back clean first try. Its docstring is the finding list. **`wt131b` is the new
   exemplar: an amendment to a frozen section, with the digest read out of git rather than typed.**

---

## YOUR AT-BAT — ASSIGNED. Do not choose.

> # ▶ `-74`, YOUR AT-BAT IS: **PAPER II'S FIFTH INDEPENDENT READ.**
>
> **Start here. You do not need to read the rest of this file to begin.** ~45 min.
>
> **`-70`'s rule is back in force and this is it.** `-72` set it aside for one session because
> Paper III was in `definition_of_done` with zero reads. Paper III has now had a pass. There is no
> longer a manuscript in the definition of done with zero reads, so there is no longer a reason to
> set the rule aside, and **this is the first half of the consecutive-zero pair the definition of
> done requires.**
>
> **RUN THE TWO CROSS-REFERENCE SWEEPS BEFORE THE QUANTIFIER SWEEP.** Both are in `REVIEW-013`
> §3 and each is about twenty lines:
>
> 1. **Every `§N.M` in the body against the heading list.** Paper III came back **zero
>    unresolved** in ninety seconds, and a clean result is worth having in writing. **Paper II
>    carries ~40 `§x.y` references and not one has ever been checked** — this has been queue item
>    4 for two sessions.
> 2. **Every reference entry's *"cited in §N.M"* against that section's text, by surname.** Paper
>    III: 33 entries, 41 claims, 7 flagged, **6 legitimate false positives, 1 real** (`III-5`, a
>    reference crediting §4.4 for a result that is §3.2's, which sat through the References
>    section's own four documented verification passes). Expect the same ratio and take it: the
>    false-positive classes are named in `REVIEW-013` §3 so you can dismiss them in seconds.
>
> **THEN `python3 scripts/wt130_quantifier_sweep.py paper-II --md`** — 155 tokens on 118 lines —
> **and then read it whole.** The sweeps are two classes of sentence; they are a floor, not a
> ceiling.
>
> **A ZERO IS THE OUTCOME THIS PROJECT NEEDS.** Paper II's counter runs 9 → 2 → 4 → 3 and the
> definition of done wants two consecutive zeros. If you find nothing, **say so plainly and do not
> manufacture a finding to avoid an uncomfortable-looking result** — that is the single way this
> at-bat can be failed. Equally, do not *aim* for zero: `-72` found three where five passes had
> found none.

### WHY PAPER II AND NOT PAPER III AGAIN, since III's counter opens at 7

Because seven findings on a **first** read of a 2,694-line manuscript is the expected number, not
an alarm, and because a second Paper III pass now would be reading text that is four hours old.
Paper III's pair is unstarted and stays unstarted for one session; Paper II's is the one that can
actually close. **If you disagree on reading this, run Paper III's second read and say so in ONE
LINE.** The one outcome that must not happen is both sessions deferring.

### THE QUEUE BEHIND IT — context, not a menu. Do not shop here.

**Reading this list is not a decision you are being asked to make.**

1. **Paper III's second read** — counter at 7, one pass deep, pair unstarted.
2. **Paper IV §1–§3, re-read against `wt125`'s OWN output** (~15 min). `-69` read §1–§3 against
   `wt121` then patched them; **nobody has read them against `wt125`.**
3. **`REFERENCE-POLICY`'s eighth pass** — card `1217556161163494`. `-73` read Paper III's
   References for **where** each entry claims to be cited and found `III-5`/`III-6`; it did **not**
   read them for **what** the sources say. That is still the single most-deferred item.
4. **Make the two cross-reference sweeps a committed script** — `wt132`, the natural sibling of
   `wt130`. `-73` ran them ad hoc and wrote them down in `REVIEW-013` §3 rather than committing
   them, which is exactly the mistake `WT-116` was banked to prevent (*"a procedure that lives in
   a ledger entry is a procedure the next session re-derives"*). **`-73` would rank this above
   items 5–12 and is naming it plainly rather than hiding it in a queue: the loops exist, they are
   forty lines total, and they are the difference between a finding and a class of findings.**
5. **`III-8`** — card `1217567136996151`, filed today. §11 names a regeneration command for §3,
   §A.2.3, §A.2.4 and §5 and **none for §4**, against a front-matter claim covering *every*
   computational result. **The card carries its own falsifier — run it first, the card may be
   wrong.**
6. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
7. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first: tightening the
   float tolerance to `==` hands the next machine a red suite. Assert the **structural** property.
8. **The U+00B5 guard** — card `1217561398864561`. Five patch scripts now carry an in-script glyph
   guard; the tree-wide one is still missing.
9. **The `CONDUCT_ALLOWED_SECTIONS` gap** — card `1217562682350929`. `-68` hit it; `-69` through
   **`-73`** all avoided it only by reading the tuple first. **Six sessions have now walked around
   the same landmine**, which is six data points that the tuple belongs where the writer looks.
10. **A gate check that a `§N` named in `HANDOFF.md` exists in the paper it names** — card
    `1217564707330383` (`WT-112`). ~6 lines. **Overlaps item 4 and should be done inside it.**
11. **The duplicated Bouchaud–Mézard description** — card `1217565324215216`, filed by `-71`. §3.1
    and §6 carry the same ~40 words about one source. Still there, still latent; the placement was
    settled at `bf07363`, so it needs a decision, not a patch.
12. **PASTE THE HANDOFF forcing function** — card `1217560480809492`. (`-67` through `-73` all
    pasted. **Seven** data points, still not a fix.)
13. **Paper II's companion reference entries** — card `1217542940968749`.
14. **PAPER I'S FIRST `P7` PASS** — still demoted, still for `drift_flags`' reason.
15. **`A3` from the PAN AAR — estate-level, STILL UNCHECKED.** Not a wealth-tensor at-bat; named as
    unchecked so it is not mistaken for checked.

---

## WHAT `-73` DID, so you do not re-derive it

**At-bat:** Paper III read whole, lines 1–2,685, `wt130` sweep plus two cross-reference sweeps.
**`REVIEW-013` is the document of record** — §1 is the coverage claim, §2 the findings, §3 a
**27-row CLEARED list**, §4 the **NOT-CHECKED list**, Appendix A the 668-row enumeration.
**7 findings, 13 edits, 1 carded.**

- **`III-1`** — §2 said *"The word **crisis** is kept **in the title**."* The title is *"Timeliness
  and durability are not separately identified from a reported series."*
  `paper-III.md.bak-pre-roadtwo` dates the retitling — the old title opened *"A crisis is deferred
  information arriving at once"* — and §8.2, written after, says the crisis framing belongs to a
  later paper and *"is not defended here."* A claim about the document's own first line, falsified
  by the first line.
- **`III-2`** — §A.1.3: *"the regimes in which **each proposition** fails are committed, tested
  code."* Two bullets follow. One is P2. **The other calls itself "a separate and equally important
  point"** and then says *"P2 still holds at φ = 1"*. P1 and P3 get nothing. `WT-117` exactly.
- **`III-3`** — §11 scoped the repository's provenance to *"§A.2 and §2"* **four times** and
  labelled `wt027_report.py` *"Regenerate §2."* §2 carries no measured number; that script's own
  docstring lists three tables and they are §3.1's two and §3.2's. **§6.1 writes it correctly
  twice.** `II-19`'s species with the right words already in the paper.
- **`III-4`** — §7's survivals row titled *"The rectangle's **99.7%**"* while its own outcome cell
  and §4.4 both report **0.998 / 99.8%**. **Not a rounding:** `RESULT-REG-002` §4 says 99.7% is
  E4's figure **at α = 0.35**, and the row ran at the measured α̂ = 0.408.
  `tests/test_ledger_provenance.py` uses the title as a lookup key in five places and they move
  with it.
- **`III-5`** — the Bleck and Liu entry credits *"§4.4 and §10"* and *"§4.4's volatility result."*
  Cited in **§3.2**, §8.2 and §10, and §8.2 says so in terms.
- **`III-6`** — the Jin and Myers entry names *"§10's **one** quotation"* and gives a sentence
  **absent from the manuscript**, while §10 carries **five** quoted fragments from them — and the
  entry then states the standard §10 is failing: *"a reader entitled to doubt that on a paraphrase
  should be able to see the words."* §10 supplies exactly the paraphrase. **Repaired by restoring
  the words to §10**, which is the smaller change and the one the entry's own rule asks for.
  Separately, the References' fourth-pass note says the crash-risk entries carry **✓⧗** and **none
  of them does** — repaired by **APPEND**, because that paragraph is a dated record of what the
  pass found and what it found was afterwards discharged.
- **`III-7`** — §4.7's *"§5's floor of 30."* §5 states no floor of 30, its one use of the word is
  *"the materiality floor"* with no value, and §5.3's own tier cells run to **n = 21**.
- **`III-8`, CARDED** — `1217567136996151`, with its falsifier. §11 has no regeneration command for
  §4.

**`wt131c`, unasked for and worth two minutes:** `wt130` printed *"864 quantifier tokens on 668
lines"* meaning **lines that carry a quantifier**, and that reading travelled into `-72`'s handoff,
`LEDGER WT-116` and `docs/HANDOFF.md` as *"668 lines, the largest manuscript in the batch"* — with
a "~50 min" budget written from it for a document **2,694 lines** long. All three print sites now
carry the manuscript's own length beside the count. The conclusion (*read Paper III next*) was
right for a different reason and stands.

`LEDGER` `WT-119` / `WT-120` / `WT-121`. Three lessons banked (two global, one project-scoped), two
`use`d and corroborated — **`WT-115`'s leaf graduated quarantine → active on this pass.**
Commits `74734de` ← the amendment ← the wrap.

---

## ✅ NEW SETTLED, DO NOT REOPEN

**`-73`'s seven repairs are settled AS REPAIRS.** In particular:

- **`RESULT-REG-002`'s 99.7% was NOT touched and must not be.** It is correct at its own α = 0.35
  and is a dated result of record, quoted by `tests/test_reg002_sec5_e4_extension_label.py` and by
  `scripts/mutation_control.py` R4b. Only the manuscript's §7 row title moved, to the number that
  row actually produces.
- **The Jin and Myers verification record stays.** *"verified in the published text at p. 262,
  character for character"* is a dated fact about the source, not a claim about §10, and it was
  left alone on purpose — same doctrine as Paper II's `END-TO-END-001` quotations.
- **The References' fourth-pass paragraph was APPENDED to, not rewritten.** Do not tidy the
  original sentence into agreement with the append; the sequence is the record.
- **`REG-012` §4.7's freeze now carries TWO amendments.** `SEC_47_AT_REGISTRATION` is immutable and
  was not touched. If you move §4.7 again, append a third — do not re-pin, do not revert on the
  guard's account alone, and read `WT-121` for the two-commit shape first.
- **`REVIEW-013` §3's 27 CLEARED rows are cleared.** `C19` (the 291-fold reads as 289 from the
  printed pair — a rounding in `NOTE-001`, not an error), `C23` (§11's *"will be pinned when this
  paper is posted"* satisfies `P1m` because the per-file pins are supplied now) and `C24`
  (*"§4.6's question"* is loose, not false, and was deliberately not repaired) are the three most
  likely to be re-litigated. Don't.

**Everything else settled stays settled:** `-72`'s three Paper II repairs; the abstract deliberately
NOT carrying `II-21`'s ρ = 1 caveat; `END-TO-END-001` and `E3`'s quotations of Paper II §7 left
alone on purpose; `wt128` RAN and is not to be edited; Paper II §5 item 1 is `P3g`'s; the
*"Version 0.x, <date>"* header above later content is a CONVENTION across all four manuscripts and
is **not** rot; Paper IV's framing ruled and propagated through §10; card `1217561330623702` at
(a); `DECISION-001` closed at A; `WT-103`; the 14 household-to-sovereign occurrences untouched on
purpose; `REG-012` §4.7 appends Amendments; `WT-094` grep `tests/`+`scripts/` first; never delete
"18 tests"; no re-deriving κ residuals / `III-1`'s 4.2× / E2 blind pass; `REVIEW-004` verbatim
quotes only; `REVIEW-005` §2's `II-3` is WRONG about the code; end-to-end CLOSED.

---

## THE TELL, now NINETEEN deep

`-61` through `-70` as before. `-71`: a quantifier is contradicted downstream, never upstream — so
read forward from it. `-72(i)`: downstream includes **four lines later**. `-72(ii)`: when a document
names a failure mode, **grep the document for that failure mode**. `-72(iii)`: a guard has two
failure modes and the red output cannot tell them apart — assert every invariant against the
ORIGINAL first (`WT-118`).

**`-73(i)` — A CROSS-REFERENCE IS A QUANTIFIER OVER A SECTION, AND IT IS THE ONE A CAREFUL READ
CANNOT CATCH.** `§N.M` is a claim about what that section contains. A reviewer reading forward from
*"every"* holds one set in their head. A reviewer reading *"§4.4's volatility result"* has to hold a
**different section** in their head, and cannot — so this class survives every careful read **by
construction, not by oversight**. Four of seven findings. **Write the loop instead.** And record the
false-positive rate honestly: 1 real in 7 flagged, and still worth its five minutes, because the
alternative is nobody checking at all.

**`-73(ii)` — A CLEAN SWEEP IS A RESULT AND BELONGS IN THE REVIEW DOC.** The §-reference sweep came
back **zero unresolved across the whole manuscript**. That is not a wasted ninety seconds; it is the
first thing in this project that lets a later session skip a class of check with a reason. `-72`
made coverage countable; a clean count is half of what countable buys you.

**`-73(iii)` — THE THING THAT PROPAGATES IS THE TOOL'S OUTPUT LINE, NOT THE TOOL'S NUMBER.**
`wt130`'s *"668 lines"* was correct and its **label** was ambiguous, and the ambiguity travelled
into three documents and a session budget before anyone opened the manuscript to check. `WT-116`
banked the instrument; nobody banked its units. **When a script prints a count, print what it
counts** — and when you inherit a number in a brief, the cheapest possible check is `wc -l`.

---

## TOOLING (▲ new at `-73`)

- ▲ **The two cross-reference loops** — `REVIEW-013` §3, twenty lines each, **not yet a committed
  script** (queue item 4, named plainly rather than buried). (1) every `§N.M` in the body against
  the heading list; (2) every reference entry's *"cited in §N.M"* against that section's text, by
  surname.
- ▲ **`scripts/wt131b_amend.py`** — the exemplar for moving a **frozen** section: reads the digest
  out of git rather than typing it, refuses if the named commit did not move the section, and
  refuses a licence that names the freezing registration's own outcome.
- ▲ **`scripts/wt131c_sweep_wording.py`** — a two-minute bug-spray on `wt130`'s own output. Its
  shape is worth copying: patch the print sites, then **run the tool and assert the counts did not
  move**, which is the only guard that matters for a wording change.
- **`scripts/wt130_quantifier_sweep.py`** — unchanged in behaviour, clearer in output. `--md` still
  emits a table straight into a `REVIEW` doc; no args still gives four lines of orientation and is
  still the cheapest move in the repo.
- **Appending to a big doc** (unchanged, worked first try): `--put` the block to `/tmp/`, then
  `dx 'cp X X.bak-wtNN && cat /tmp/block >> X'` — one round trip, backup first, never re-upload a
  60 KB ledger. **And for anything with nested quotes, write the script LOCALLY and `--put` it**
  — `-73` did every one of `wt131`, `wt131b`, `wt131c` and the lessons batch that way and paid the
  quoting war zero times.
- **Tags run to `wt131c`; `wt132` is free** and is the natural home for queue item 4.
- `.bak-*` gitignored — the undo path lives on darwin, don't force-add.

---

## JASON-SIZED, not yours

(a) `DECISION-001` closed. (b) Paper IV framing ruled and propagated.

**(c) `P7` is still ONE BOOLEAN — the only open wealth-tensor Jason item — and `-73` makes the
argument concrete rather than adding to it.** Four sessions now: `-70` moved the board with an edit
that changed no sentence; `-71` changed five sentences and it did not move; `-72` changed three more
and it did not move; **`-73` changed thirteen, across seven findings, on the manuscript with the
most criteria rows of any in the batch, and the board did not move.** The board is a working
instrument pointed at STRUCTURE and silent on TRUTH. That is settled.

`-72` put a concrete proposal under `-71`'s question and `-73` seconds it **and can now say what it
would have caught**: a board row requiring each paper's `REVIEW` to carry a sweep whose counts match
a fresh run measures **coverage**, not truth — the honest thing a script can know. Paper III would
have failed that row for four months, and failing it is exactly the signal that was missing. **One
line of yours settles it: yes add the coverage row, or no, reviewing stays narrative.**

(d) The PAN history purge — Batter's Box `1217561667484767`; do NOT rewrite `claude-blackbook`
history on your own initiative.

---

## WHY NOT `P13`, since `charter-read.sh` asks

`charter-read.sh` reports **`P13` as the first OPEN lane in dependency order** — the beautifully
designed, arXiv-ready PDF. `-73` worked **`P7`** instead, as assigned, and the project's own
ordering ruling is why: **`P13` is a point-in-time capture of the corpus**, and capturing a corpus
whose manuscripts still yield findings per read produces a beautiful PDF of prose that is about to
change. `P7` → `P13` → `P8` is the DoD's own sequence.

**`-73` retires `-72`'s version of this argument and replaces it with the measured one.** `-72`
wrote *"Paper III is 864 quantifier tokens on 668 lines and has never been read"*; the sentence is
now *"Paper III has been read once, at 2,694 lines, and it returned **seven** findings — three of
them claims the manuscript makes about **itself** that are false."* Typesetting a document whose own
front matter misdescribed its title is the strongest available form of the same mistake. `P13`
should not move until Paper III's pair is at least started.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary line,
never `$?`, never through a pipe); `roster leave --who <you>` once; and **paste a handoff better
than this one into the chat as the last act.** Assign `-75` ONE at-bat with a definition of done.
Do not hand them a menu. 🥎
