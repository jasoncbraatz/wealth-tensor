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

## 3 · THE BOUNDED PLAN — three passes, named, with a hard stop

### PASS A — `wealthTensor-103` · make the end countable

**The only pass permitted to add to the blocking set.** Its whole job is to convert an open-ended
process into a finite list.

1. **Retrospectively score every finding in the sixteen `p7-passes.tsv` rows** and their REVIEW
   docs against § 2. The rubric is already committed and must not be edited during this step.
2. **Adjudicate `wt184`'s 44 Rule-1 flags on paper-III** — read them *before* touching the rule
   (`III-5` came out of that flag set, so the prior that most are false is not a licence to
   skip them). **Any flag ruled TRUE is an S1 by definition** and goes on the ship list.
3. **Triage all nine carried tee-ups** into S1/S2 (ship list) or S3/idea (`POST-SHIP.md`).
4. **Emit `docs/SHIP-LIST.md`** — every open S1 and S2 across all three manuscripts, numbered,
   each with the repair it needs. **Then close it and freeze it.**
5. **Report the count and the severity distribution across all sixteen passes**, which is the
   measurement this project has been owed for eight sessions: is severity falling while the
   count is flat?

**DONE WHEN** `docs/SHIP-LIST.md` exists, is closed, and every one of its entries names a repair.

> ⚠ **PASS A MAY NOT REPAIR ANYTHING.** Scoring and repairing in the same pass is how a rubric
> gets bent around a repair that was easy. Pass A produces a list; Pass B spends it.

### PASS B — `-104` (and `-105` only if the list demands it) · clear the list

Every S1 and S2 on the ship list repaired, in the charter's order
(**STEELMAN → REPLACE → CUT → TEE-UP**), with `defensive_count.py --against` at **+0** on every
manuscript. **No new looking.** If a repair reveals an adjacent S1 — a genuinely broken thing you
had to touch — it may be repaired and appended, and **that is the only permitted growth of the
list**, logged in `SHIP-LIST.md` with the repair that surfaced it.

**DONE WHEN** every ship-list entry is CLOSED, `pytest` green, all guards green,
`--claims-all` agrees.

### PASS C — the ship pass · verify against the frozen list only, then declare

1. One final read per manuscript **against the frozen instrument set only** — running the
   checkers, not hunting for new classes of defect. A finding here is **S1/S2 only**; S3
   observations go straight to POST-SHIP without discussion.
2. All guards green, `--claims-all` agrees, deliverables rebuilt, layout verified.
3. Write **`docs/SHIP-STATEMENT.md`** (§ 4).
4. Tag `v1.0-preprint`. Close `P7`. Hand `P8`/`P11` to Jason.

### 3.4 · THE HARD STOP

**If Pass B has not cleared the ship list by the end of `-106`, the work stops and Jason rules**
on shipping with the remainder open and disclosed in § 4.3. **The stop is not a failure state.**
It exists so that "a few more passes" is a commitment with an enforcement mechanism rather than an
intention, which is the exact failure the retired criterion demonstrated over sixteen sessions.

---

## 4 · WHAT SHIPPING PRODUCES

**4.1 · The three manuscripts**, rebuilt, layout-verified, at ready-to-submit per ADR-001.

**4.2 · `docs/SHIP-STATEMENT.md`** — the honest provenance record, and the artefact this whole
apparatus was actually building:

* how many independent review passes each manuscript received, and by what axes;
* the frozen instrument list, with what each one checks;
* the total findings raised and repaired, by severity;
* **what is known-imperfect and shipping anyway** — the S3 list, in full.

**4.3 · A short "known limitations of this review" note in each paper.** Two or three sentences,
naming what was checked mechanically, what was checked by hand, and what was not checked. **This
is a strength, not an apology** — it is the same discipline that produced `II-43`, which exists
only because §7 enumerated instead of gesturing. **A paper that says what it did not check is
more trustworthy than one that is silent, and this corpus has earned the right to say it.**

---

## 5 · THE LOOPHOLES THIS CLOSES, NAMED SO A FUTURE SESSION CANNOT REOPEN THEM BY ACCIDENT

| # | the loophole | how it is closed |
|---|---|---|
| L1 | **Don't-look.** A zero-finding pass is purchasable by reading carelessly. | Ship is gated on a **finite enumerated list**, never on a finding count. There is no longer any reward for finding nothing. |
| L2 | **The tee-up escape hatch.** A finding becomes a card, and the pass reports zero. | An S1 or S2 closes **only** by a landed repair or a written Jason ruling. **Carding is not a third option.** |
| L3 | **The new instrument.** Building a checker always finds new things, so the clock resets forever. | § 1.1 freezes the instrument set. False-positive *repairs* are allowed; new *looking* is not. |
| L4 | **The growing backlog.** The generator of new work matched the drain, so the list never emptied. | § 1.2 freezes the blocking set at Pass A's close. Everything later goes to POST-SHIP. |
| L5 | **The tuned rubric.** A severity boundary edited after seeing the finding it would excuse. | § 2 is committed **before** Pass A scores anything, and edits to it are a Jason ruling made **before** a re-score. |
| L6 | **The infinite polish.** "A few more passes" with no enforcement. | § 3.4's hard stop at `-106`, with an explicit ship-with-remainder-disclosed path. |
| L7 | **Scope-and-repair in one hand.** The session that scores also repairs, and grades its own homework. | Pass A may not repair; Pass B may not re-score. |
| L8 | **Silent imperfection.** Shipping while quietly knowing about S3s. | § 4.3 publishes them **in the papers**. |

---

## 6 · THE STAMP

* **Ruled by:** Jason, 2026-08-24, in session `wealthTensor-102`.
* **Freeze commit:** recorded at the top of `docs/POST-SHIP.md` — that file's first line is the
  authority, so "frozen at" is **checkable rather than asserted**.
* **Supersedes:** the convergence clause of `docs/HANDOFF.md`'s `definition_of_done` and the `P7`
  row of `docs/done-criteria.tsv`, both updated in the same commit to point here.
* **What did NOT change:** the charter, the coach model, `G-COACH-3`, the falsifier discipline,
  and the requirement that every finding arrives with its repair. **The bar on the WORK is
  unchanged. Only the stopping rule moved.**
