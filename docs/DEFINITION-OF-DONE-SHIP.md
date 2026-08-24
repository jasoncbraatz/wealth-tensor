# DEFINITION OF DONE — the SHIP definition

**Ruled by Jason, 2026-08-24, at `wealthTensor-102`.** This document REPLACES the convergence
criterion for `P7`. It is the SSOT for what "done" means on this corpus; where any other file
disagrees, including `docs/HANDOFF.md`'s `definition_of_done` field and `docs/CHECKLIST.md`'s `P7`
row, **this file wins.** The `CO-AUTHOR-CHARTER.md` still wins over this file.

---

## 0 · Why the old one is being replaced, in numbers

The retired criterion: *"fresh-eyes review passes repeat until TWO CONSECUTIVE passes yield ZERO
substantive findings, per paper."*

**Sixteen passes have been run and none has yielded zero.** Paper II's counter across thirteen
reads: **9, 2, 4, 3, 4, 5, 3, 2, 2, 3, 2** — the last eight sit flat in a 2–5 band with no
downward slope. That is a **plateau, not a convergence**, and the mechanism is visible in the
bookkeeping rather than the prose: at `-102` one tee-up was retired and one was added. **Net change
to the backlog: zero.**

**A criterion that terminates only when a backlog empties, attached to a process whose backlog is
stationary, has no termination proof.** That is not a criticism of the passes — the passes have
been excellent, and pass 13 found a real over-credit to a cited paper that twelve reads missed.
It is a statement about the *stopping rule*, which was the wrong instrument for the job.

**AND THE OLD RULE PAID A WORSE PRICE THAN NON-TERMINATION: IT REWARDED NOT LOOKING.** A
zero-finding pass is trivially purchasable by reading carelessly. Every honest session felt that
and compensated by looking harder, which is exactly why the counter never fell. The criterion was
in a tug-of-war with the charter, and the charter kept winning. Good.

**What replaces it is a punch list, not a limit.** Freeze the scope, enumerate the finite work,
do it, ship. Termination is by construction.

---

## 1 · THE FREEZE

**Freeze commit: `SHIP_FREEZE_SHA` (recorded in `docs/POST-SHIP.md` line 1 and in this file's
own § 6 stamp). Anything dated after it is out of scope by default.**

Three things freeze at that commit and **cannot be reopened without a Jason ruling in writing**:

**1.1 · THE INSTRUMENT SET IS FROZEN.** `wt130` through `wt190` plus the guards in `tests/` are
the review apparatus, entire. **No pass after the freeze may build a new axis, a new sweep, or a
new checker as part of shipping.** Ideas for new instruments are welcome and go to
`docs/POST-SHIP.md`; they do not block, they do not go in a `p7-passes.tsv` row, and they are not
an at-bat until the corpus has shipped.

> **THE ONE EXCEPTION, and it is narrow:** a change that makes an existing instrument produce
> **fewer false positives** is a *repair*, not a new instrument. `wt184`'s Rule 1 attribution
> defect qualifies. A change that makes an instrument look at something new does **not** qualify,
> however small. If you cannot tell which one you have, it is a new instrument.

**1.2 · THE BACKLOG IS FROZEN.** The blocking set is exactly what `docs/SHIP-LIST.md` contains
when Pass A closes it. **Anything discovered after that goes to `docs/POST-SHIP.md`.** Not to the
ship list, not to a `p7-passes.tsv` row, not to the at-bat. A session that grows the blocking set
has broken the definition of done, not satisfied it.

**1.3 · THE SEVERITY RUBRIC IS FROZEN, AND IT WAS WRITTEN BEFORE ANYTHING WAS SCORED AGAINST IT.**
§ 2 below is committed at the freeze, **ahead of Pass A's retrospective audit**, precisely so it
cannot be tuned until the answer comes out "done." **If a future session wants to move a boundary
in § 2, that is a Jason ruling and it must be made BEFORE the re-score, never after seeing one.**

---

## 2 · THE SEVERITY RUBRIC — what blocks shipping and what does not

Every finding, past or future, sorts into exactly one of three. **Ship requires zero OPEN S1 and
zero OPEN S2. S3 is counted and published, never gated.**

### S1 · BLOCKING — the manuscript states something that is not true

A reader who checks it finds the paper wrong. Examples from the actual ledger:

* a reported number that does not reproduce from the named command;
* a claim about **another author's work** that their paper does not support — `II-44`, where the
  paper credited Bouchaud & Mézard with two coordinates they never model;
* an enumeration that is wrong — `II-43`, *"five quantities"* where there are six;
* a cross-reference that resolves to the wrong place — `II-40`;
* an artefact named in the paper that does not exist, or does not do what the paper says it does;
* a quotation that is not verbatim, or is attributed to the wrong source.

### S2 · BLOCKING — the manuscript asserts something nothing supports

Not false, but not backed. A reader who asks *"how do you know?"* has no answer available:

* a reported figure that **no named command produces**, in a paper that promises provenance;
* an attribution with no reference entry, or a reference entry the body never cites where the
  body relies on it;
* a promise about an artefact (*"§10 names the record"*) where the artefact does not carry it;
* a claim of scope (*"every simulation in §§2–3"*) that is narrower than what the paper reports.

### S3 · NON-BLOCKING — precision, taste, and honest imperfection

Real observations that do not make the paper wrong or unsupported:

* an **under-claim** — §3.1's *"4–7 %"* band where the sweep's max is 6.831 %. True as written.
* a defensible-but-loose word; a tighter phrasing available;
* a check that *could* be run but whose absence the paper already discloses;
* a docstring that does not assert what its test verifies (`A6`);
* an instrument's own limitation, recorded and disclosed.

**S3 ITEMS ARE NOT SWEPT UNDER A RUG. THEY SHIP WITH THE PAPER**, in a short *"known limitations
of this review"* note (§ 4.3), which is the honest version of what every preprint's silence
already implies.

### 2.4 · The tie-breaker, so nobody has to litigate it twice

**When a finding could be S2 or S3, ask one question: does the paper CLAIM the thing that is
missing?** A paper that promises *"every number is regenerated from committed scripts"* and then
reports a number no script produces has an **S2** — the paper wrote the check it failed. A paper
that simply did not run an available check, and never said it did, has an **S3**.

**When it could be S1 or S2, ask: is the statement WRONG, or merely UNBACKED?** Wrong is S1.

**Ambiguity resolves UPWARD, once.** If two readers disagree S1-vs-S2, it is S1 — both block, so
the cost of the rule is zero and it removes the argument.


---

## 2.5 · THE COHERENCE CLASS — the axis § 2 was missing

**Jason's ruling, 2026-08-24, second amendment.** §§ 2.1–2.4 grade **truth**: is the statement false,
is it unsupported, is it merely imprecise. **A manuscript can pass all of that and still read like a
lab notebook**, and a lab notebook is not something a human can rewrite from without wasting hours.

**THE DEFECT CLASS THAT MOTIVATED THIS AMENDMENT IS ENTIRELY TRUE STATEMENTS.** A long build leaves
scar tissue in the prose: the aside recording that a test went sideways, the antithesis realisation
that a suspected result did not appear, the sentence that made sense in the session that wrote it.
**Every one of those is true, so every one scores S3 under § 2 and ships** — which is exactly
backwards. They are not errors. They are *seams*, and a published paper has none.

**C-class findings block the ship. They are found and repaired in PASS D, never on the S1/S2 ship
list**, because they are a different kind of work: § 2 is checked sentence by sentence, and
coherence is only visible from thirty thousand feet.

### The named C-class defect types

| type | what it looks like | the repair |
|---|---|---|
| **C-a · antithesis residue** | *"We expected the threshold to matter here; it does not."* True, and written as an in-line aside where the reader trips on it. | Integrate into the claim it qualifies, promote to a Limitations bullet, or move to an appendix. **Never delete a negative result** — it is often the most honest thing in the paper. |
| **C-b · scaffolding voice** | *"as noted above"*, *"this was originally"*, *"the pass that added this"* — process narration that outlived its process. | Cut, or restate as a claim about the work rather than about the working. |
| **C-c · orphan** | A paragraph, table, or figure nothing references and no later claim depends on. | Anchor it to the claim it serves, or cut it. An orphan that survives is a reader's dead end. |
| **C-d · fold problem** | A result stated before the definition or the method it rests on; a term first used two sections after it is defined. | Reorder. **This is the one that most directly costs Jason hours**, because he cannot re-voice a paragraph that is in the wrong place without first discovering it is in the wrong place. |
| **C-e · apparatus leak** | The manuscript points at a REVIEW doc, a `wt###` script, a session number, or `p7-passes.tsv` as if the reader had them. | Repoint at the paper's own §, or at a committed artefact the reader can actually fetch. |
| **C-f · register drift** | Two sections that read as if written by two people, because they were written eighteen sessions apart. | Flag it and leave it. **Re-voicing is JASON'S pass, not a session's** — a session that "harmonises the voice" has spent his hours for him and probably lost something. **Flagging is the repair.** |
| **C-g · unplaced evidence** | A table or figure with no anchor sentence telling the reader what to see in it. | Add the anchor sentence. Every piece of evidence gets one. |

> **C-f IS DELIBERATELY THE ONE THAT DOES NOT GET FIXED.** The line between *structural* work (a
> session's job) and *voice* work (Jason's) is the whole point of this amendment, and a session that
> crosses it is doing damage that looks like help.

### 2.6 · The C-class tie-breaker

**Ask: would a reader who has never seen this repository notice?** If the seam is only visible to
someone who knows the build history, it is **C-b** at most and probably nothing. If a first-time
reader stumbles, it is a C-class finding. **When in doubt, read the paragraph out loud starting from
the section heading above it** — fold problems and orphans are audible in a way they are not visible.

---

## 3 · THE BOUNDED PLAN — four passes, and a RATCHET rather than a countdown

### 3.0 · THE RATCHET — read this before the pass descriptions

**NO SESSION MAY STOP BECAUSE ITS NUMBER CAME UP.** *"I am `-105`, therefore I stop"* is a failure,
not compliance, and it is the specific behaviour this clause exists to forbid.

**EVERY PASS OWNS ITS SUCCESSOR'S PRECONDITIONS.** A pass is not finished when it has done its own
work; it is finished when **the next pass can start and finish**. The question at the end of every
session is not *"did I complete my list?"* but:

> **"What does the NEXT pass need in hand, and have I put it there?"**

Concretely: Pass B does not close by repairing the last S1 — it closes by confirming Pass C can
verify without discovering scope Pass B left implicit. Pass C does not close by going green — it
closes by handing Pass D a manuscript whose structure is settled enough to be read at thirty
thousand feet. **Pass D does not close by finishing a checklist — it closes when Jason can start
rewriting without hitting a false start.**

**IF A PASS CANNOT MEET ITS SUCCESSOR'S PRECONDITIONS, IT SAYS SO LOUDLY AND HANDS OVER THE
REMAINDER.** That is a normal outcome and costs one extra session. It is **never** a reason to
declare done, and it is **never** a reason to keep polishing past the point of usefulness.

### PASS A — `wealthTensor-103` · make the end countable

**The only pass permitted to add to the blocking set.** It may not repair anything: scoring and
repairing in the same hand is how a rubric gets bent around a fix that was easy.

1. **Retrospectively score** every finding in all sixteen `p7-passes.tsv` rows against § 2. The
   rubric is committed and **must not be edited while you score**.
2. **Adjudicate `wt184`'s 44 Rule-1 flags** on paper-III — read them **before** touching the rule
   (`III-5` came out of that set). **Any flag ruled TRUE is an S1** and goes on the ship list.
3. **Triage the nine carried tee-ups** into S1/S2 (ship list) or S3/idea (`docs/POST-SHIP.md`).
4. **INVENTORY THE C-CLASS — count, do not repair.** Sweep all three manuscripts for C-a through
   C-g and **report a count per type per paper.** This is what makes Pass D's size known *before*
   Pass D starts, and it is the difference between a plan and a hope. **A rough count beats an
   elegant absence of one.**
5. **Emit `docs/SHIP-LIST.md`** — every open S1 and S2, numbered, each naming its repair — then
   **close and freeze it.**
6. **Report the severity distribution across all sixteen passes.** *Is severity falling while the
   count is flat?*

**SUCCESSOR PRECONDITION (§ 3.0):** Pass B can start iff every ship-list entry names a repair
specific enough to execute without re-deriving the finding.

### PASS B — `-104` · clear the truth list

Every S1 and S2 repaired in the charter's order (**STEELMAN → REPLACE → CUT → TEE-UP**), with
`defensive_count.py --against` at **+0** on every manuscript. **No new looking.** If a repair
reveals an adjacent S1 you had to touch, repair and append it — **the only permitted growth of the
list**, logged with the repair that surfaced it.

**SUCCESSOR PRECONDITION:** Pass C can start iff the ship list is CLOSED, `pytest` is green, and
every guard the repairs reddened has been closed **in the same session that reddened it**.

### PASS C — `-105` · verify the truth, and settle the structure

1. One read per manuscript **against the frozen instrument set only** — running the checkers, not
   hunting new classes. Findings here are S1/S2 only; S3 goes straight to POST-SHIP.
2. All guards green, `--claims-all` agrees, deliverables rebuilt, layout verified.
3. **SETTLE THE STRUCTURE.** Fix C-d (fold problems) and C-c (orphans) — the two C-types that
   change what *exists and in what order*, as opposed to how it reads. **They are done here, not in
   Pass D, because Pass D's thirty-thousand-foot read is worthless on a document whose sections are
   still moving.**

**SUCCESSOR PRECONDITION:** Pass D can start iff no section will move again.

### PASS D — `-106` · the coherence pass · **THE ONE THAT PRODUCES JASON'S INPUT**

**This pass has one reader in mind and it is Jason, about to spend a large number of hours
rewriting.** Its job is to make sure those hours are not a false start.

1. **Clear the remaining C-class** — C-a (antithesis residue), C-b (scaffolding voice), C-e
   (apparatus leaks), C-g (unplaced evidence). **FLAG C-f (register drift); do not fix it.**
2. **Read each manuscript end to end at thirty thousand feet**, once, in one sitting, asking only:
   *does this read as one connected paper?* Not sentence-by-sentence — that is Passes B and C, and
   they are done.
3. **Emit `docs/FIGURE-PLAN.md`** (§ 4.3). **This is the deliverable Jason's layout work runs on.**
4. **Emit `docs/SHIP-STATEMENT.md`** (§ 4.2).
5. Rebuild, verify layout, tag `v1.0-preprint`, close `P7`.

**SUCCESSOR PRECONDITION — and the last one, because the successor is Jason:** he can open any of
the three manuscripts, start rewriting at paragraph one in his own voice, and **never discover that
a paragraph should not exist, sits in the wrong place, or is missing the chart that would carry it.**

### 3.5 · WHEN THE RATCHET STALLS

If a pass cannot meet its successor's precondition, **it hands over the remainder and says so in
one loud paragraph at the top of its handoff.** One extra session is the normal cost.

**Jason rules — and it is a ruling, never an automatic stop — when the ratchet stalls TWICE ON THE
SAME PRECONDITION.** Two sessions failing at the same gate is evidence the gate is wrong or the
scope was mis-estimated, and both are decisions a human makes. **A single stall is just work.**

---

## 4 · WHAT SHIPPING PRODUCES

**THE END PRODUCT IS NOT "A CORRECT MANUSCRIPT". IT IS A MANUSCRIPT JASON CAN REWRITE FROM.**
Those are different bars and the second is higher. Correctness is necessary and it is not
sufficient: a paper can be free of S1 and S2 and still cost its author a wasted weekend, because
the seams only show up once you are three hours into re-voicing it.

**4.1 · Three manuscripts that are STRUCTURALLY FINAL.** Rebuilt, layout-verified, at
ready-to-submit per ADR-001, **and**:

* **no section will move again** — the order is settled (Pass C);
* **no paragraph exists that should not** — orphans resolved (Pass C);
* **no scar tissue** — antithesis residue integrated or promoted, scaffolding voice gone (Pass D);
* **every table and figure carries an anchor sentence** saying what the reader should see in it;
* **the voice is NOT harmonised** — that is Jason's pass, and C-f is flagged, not fixed.

> **THE TEST, STATED SO IT CAN BE FAILED:** Jason opens the file, starts rewriting at paragraph
> one, and **never discovers that a paragraph should not exist, sits in the wrong place, or is
> missing the chart that would carry it.** If he does, Pass D did not finish — regardless of what
> its checklist said.

**4.2 · `docs/SHIP-STATEMENT.md`** — the provenance record this whole apparatus was building:
passes per manuscript and by what axes; the frozen instrument list; findings raised and repaired by
severity; the C-class counts before and after; **and what is known-imperfect and shipping anyway.**

**4.3 · `docs/FIGURE-PLAN.md` — THE ARTEFACT JASON'S LAYOUT WORK RUNS ON.**

**Measured at `-102`: the four manuscripts carry ZERO figure captions and roughly 230 markdown
table rows between them (paper-III alone has 157).** So this is not *"where do the existing charts
go"* — **there are no charts.** The real question is *which of these tables wants to be a picture,
and what would it show.* A blank page is a bad place to start a large piece of design work; this
file is the running start.

For **every** table and every proposed figure, one row:

| column | what it answers |
|---|---|
| **id / location** | which § it currently lives in |
| **what it shows** | in one sentence, in reader's terms |
| **which claim it carries** | the specific sentence that fails without it — **if none, it is a C-c orphan, not a figure** |
| **must follow** | the earliest point in the paper where the reader has enough to read it |
| **load-bearing or supporting** | does an argument break without it, or does it merely help |
| **chart candidate** | the table is fine as a table · **or** the shape it wants (a sweep is a line, a comparison across four coordinates is a small-multiple, a distribution is not a bar chart) and **why that shape** |

**A session may PROPOSE chart forms and must NOT build them.** Jason decides what gets drawn, where
it sits, and what is above the fold. **The plan is the deliverable; the drawing is his.**

**4.4 · A short "known limitations of this review" note in each paper.** Two or three sentences on
what was checked mechanically, what by hand, and what not at all. **This is a strength, not an
apology** — the same discipline that produced `II-43`, which exists only because §7 enumerated
instead of gesturing.

---

## 5 · THE LOOPHOLES THIS CLOSES, NAMED SO A FUTURE SESSION CANNOT REOPEN THEM BY ACCIDENT

| # | the loophole | how it is closed |
|---|---|---|
| L1 | **Don't-look.** A zero-finding pass is purchasable by reading carelessly. | Ship is gated on a **finite enumerated list**, never on a finding count. There is no longer any reward for finding nothing. |
| L2 | **The tee-up escape hatch.** A finding becomes a card, and the pass reports zero. | An S1 or S2 closes **only** by a landed repair or a written Jason ruling. **Carding is not a third option.** |
| L3 | **The new instrument.** Building a checker always finds new things, so the clock resets forever. | § 1.1 freezes the instrument set. False-positive *repairs* are allowed; new *looking* is not. |
| L4 | **The growing backlog.** The generator of new work matched the drain, so the list never emptied. | § 1.2 freezes the blocking set at Pass A's close. Everything later goes to POST-SHIP. |
| L5 | **The tuned rubric.** A severity boundary edited after seeing the finding it would excuse. | § 2 is committed **before** Pass A scores anything, and edits to it are a Jason ruling made **before** a re-score. |
| L6 | **The infinite polish.** "A few more passes" with no enforcement. | § 3.0's **ratchet** — a pass closes only when its successor can start AND finish — plus § 3.5, where a **twice-stalled** precondition becomes a Jason ruling with an explicit ship-with-remainder-disclosed path. *(This row named § 3.4's hard stop until `-102` noticed the amendment had DELETED § 3.4: the loophole table had a dangling pointer to the mechanism it was citing, and nothing went red. See L10.)* |
| L7 | **Scope-and-repair in one hand.** The session that scores also repairs, and grades its own homework. | Pass A may not repair; Pass B may not re-score. |
| L8 | **Silent imperfection.** Shipping while quietly knowing about S3s. | § 4.3 publishes them **in the papers**. |
| L9 | **Truth-only grading.** A paper free of S1 and S2 that still reads as a lab notebook — every seam is a TRUE statement, so every seam scored S3 and shipped. | § 2.5's **C-class**, blocking, with seven named defect types and a Pass that owns them. |
| L10 | **Stopping on a number.** *"I am `-105`, therefore I stop."* The countdown taught the exact behaviour it was meant to prevent. | § 3.0's **ratchet** — every pass owns its SUCCESSOR'S preconditions; Jason rules only on a **twice-stalled** gate, never on a session number. |
| L11 | **A session re-voicing the papers.** "Harmonising" spends Jason's hours for him and usually loses something. | **C-f is flagged, never fixed.** The structural/voice line is drawn in § 2.5 and restated in § 4.1. |

---

## 6 · THE STAMP

* **Ruled by:** Jason, 2026-08-24, in session `wealthTensor-102`.
* **AMENDED the same day, same session, by Jason:** § 2.5 (the coherence class), § 3.0 (the ratchet, replacing the `-106` hard stop), § 3's fourth pass, § 4's restated end product and `FIGURE-PLAN.md`, and loopholes L9–L11. **The amendment RAISED the bar** — correct is no longer sufficient; structurally final is the bar.
* **Freeze commit:** recorded at the top of `docs/POST-SHIP.md` — that file's first line is the
  authority, so "frozen at" is **checkable rather than asserted**.
* **Supersedes:** the convergence clause of `docs/HANDOFF.md`'s `definition_of_done` and the `P7`
  row of `docs/done-criteria.tsv`, both updated in the same commit to point here.
* **What did NOT change:** the charter, the coach model, `G-COACH-3`, the falsifier discipline,
  and the requirement that every finding arrives with its repair. **The bar on the WORK is
  unchanged. Only the stopping rule moved.**
