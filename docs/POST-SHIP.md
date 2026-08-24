# POST-SHIP — everything that does NOT block the ship

**FREEZE DECLARED AT: `f7afa4fa34a98d29265918c0dbf09430ca63fc99`** — the commit that added `docs/DEFINITION-OF-DONE-SHIP.md`.
**TREE STATE FROZEN: `64d79bf7c9d76480c64c0f68f1e4563db92bf87f`**, its parent — the corpus as it stood when the ruling was made.
*(`wealthTensor-102`, 2026-08-24. Both are named because ONE OF THEM IS THE ANSWER TO A
DIFFERENT QUESTION: `f7afa4fa34a98d29265918c0dbf09430ca63fc99` is what you diff against to see what the freeze changed, `64d79bf7c9d76480c64c0f68f1e4563db92bf87f` is
what you diff against to see what has happened since. `-102`'s freeze commit message
claimed this file carried "this commit's own sha", which no commit can do — it recorded the
PARENT. Repaired here rather than left as a small false statement in the log, which is an S1
under the very rubric that commit introduced.)*
*This line is the authority for "frozen at". `docs/DEFINITION-OF-DONE-SHIP.md` § 1 points here
rather than restating a sha, so the freeze is **checkable rather than asserted**.*

---

Per `docs/DEFINITION-OF-DONE-SHIP.md` § 1.2, **everything discovered after the freeze lands here**,
not on the ship list. Per § 1.1, **every idea for a new instrument lands here too.** This file is
where good ideas go to WAIT, not to die — it is the first thing to read after `v1.0-preprint` is
tagged, and it should be long. **A long POST-SHIP is a sign the freeze worked.**

**Nothing in this file blocks shipping. Nothing in this file is an at-bat until the corpus ships.**

## New instruments proposed after the freeze

- **The scope-sentence sweep** (a natural `wt192` — `wt189`/`wt190` are taken). Enumerate the
  sections that report a computed figure, enumerate the sections §Data-and-code covers, read the
  difference. **THREE witnesses**: `-100`'s IV-10, `-101`'s III-6, `-102`'s II-43. The one
  instrument that would have caught any of them without a human first.
- **`wt133` sweep-3** — a body proper noun with no reference entry is invisible to both existing
  sweeps. Named after IV-6 at `-81`, unbuilt through four passes. SM `1217593142996092`.
- **`A6`, the docstring axis** — nineteen unasserted prose claims in `tests/test_redistribution.py`.
  Parked since `-80`. `-102`'s five-seed table at T = 1200 is now the evidence for the
  highest-value one and it is still not asserted in the docstring's own terms.

## S3 observations — real, non-blocking, and destined for the ship statement

- **Paper II §3.1's "4–7 %" band.** The sweep's max residual is −6.831 %, inside 7 %. An
  **under-claim**, not an error. Killed as a candidate at `-99` and again at `-102`; recorded here
  so it is never re-noticed a third time.
- **Paper-IV §7's Piketty relocation** records no constraint and no lapse. Taste, not a check.

## Open questions that are measurements, not defects

- **The general form of `II-34`** — seventeen of paper-II's eighteen tests run at T = 600 while
  every reported figure is at T = 1200. `-102` answered it for §3.3's periodicity figure only
  (argmin P = 30 on five of five seeds at the reported horizon). A question, not a finding.
- **The two-independent-readers design** — reading one paper twice in the same window is the only
  measurement that separates *"the paper has n defects left"* from *"a reviewer finds n."* Two
  sessions to buy one data point. Jason's to authorise, and it is a POST-SHIP experiment now.
- **Was severity falling while the count stayed flat?** Pass A measures this across all sixteen
  ledger rows. Whatever it finds, the ANSWER belongs in `SHIP-STATEMENT.md` — it is the most
  interesting thing this apparatus knows about itself.

---

# TRIAGED BY PASS A (`wealthTensor-103`, 2026-08-24)

**`docs/SHIP-LIST.md` is CLOSED.** Everything below was ruled non-blocking by Pass A against
`DEFINITION-OF-DONE-SHIP.md` § 2, with its reason. **Nothing here blocks, and nothing here is an
at-bat until the corpus ships.** The evidence is `docs/REVIEW-038-passA-retrospective-scoring.md`.

## Tee-ups ruled S3 — real, non-blocking, shipping disclosed

- **The zakat citation gap** (tee-up 9, **fifth pass carrying it**). Paper-II's own closing note
  flags it: *"One citation is deliberately absent and is flagged rather than faked… The paper's
  argument does not depend on it."* **The paper discloses the gap and scopes it as non-load-bearing
  — the DoD § 2's S3 case in its own words.** Ruled S3 so it is not re-noticed a sixth time.
  *One live thread for Jason at posting, not for a session:* the note promises a primary source
  *"at submission"*, and posting a preprint is arguably that. **His call, not a blocker.**
- **`A6`, the docstring axis** (tee-up 6, sixth pass). **DoD § 2 names `A6` as its own S3
  example** — *"a docstring that does not assert what its test verifies"* — which settles it
  without argument. `-102`'s five-seed table at *T* = 1200 remains the best evidence for the
  highest-value one and is still not asserted in the docstring's own terms. Cheapest item here.

## The `wt184` false-positive reduction — a REPAIR, permitted, not built

DoD § 1.1's narrow exception allows it; Pass A had no mandate to build it and did not.
**`REVIEW-038` § 3.3 carries the full spec, measured against a complete adjudication of all
forty-four flags — the proposed rule returns 2 of 44 and both are the two TRUE ones.** Three
changes: require an attribution token (possessive or verb) rather than paragraph co-occurrence;
exclude `[A-Z]{2,}-\d{3}` and `wealthTensor-\d+` before harvesting numerals; extend `FOREIGN` to
`<DOC-ID> §N.M`. **All three reduce false positives. None makes the instrument look at anything
new.** Card SM `1217774684736450`.

## Two instrument defects recorded by Pass A, uncounted and unbuilt

- **`wt184` and `wt133` still disagree** on an author-attributed citation (`their §4.1`), recorded
  at `-102` and unchanged. Folded into the `FOREIGN` repair above.
- **`p7-passes.tsv` finding ids are not unique across the ledger.** `III-1` names three different
  findings and `IV-1` names two, because each pass restarts its own numbering. **Any future
  aggregation must key on `<pass>/<id>`.** `REVIEW-038` § 1.2 is the first document to say so, and
  it silently loses findings if you do not.

## The C-class soft tail — a gloss pass, not a leak

**53 of the 68 counted C-e items are committed artefacts a reader can actually fetch** —
`scripts/wt###.py`, `PRE-`/`REG-`/`RESULT-` documents, commit hashes, `docs/` paths — named without
a gloss at first use. **`REVIEW-038` § 4.1 has the census.** The hard 15 belong to Pass D; **this
soft tail is a one-clause-at-first-use readability pass and it can wait for Jason's own rewrite**,
which is where voice decisions belong anyway.

## Measurement answered, for `SHIP-STATEMENT.md`

**"Was severity falling while the count stayed flat?" — NO, and neither was.** 70 findings,
**53 S1 (75.7 %), 16 S2, one single S3.** The last six passes returned nineteen S1s against the
first five passes' twenty-one, on a corpus already repaired forty-five times. **`REVIEW-038` § 1
has the thirds table and what it settles.** This was the last open question on this list.

---

## From `wealthTensor-104` (Pass B)

**Nothing here blocks. Nothing here is an at-bat until the corpus ships.**

### Findings made while repairing, filed here rather than on the list (§ 1.2)

- **`wc -w` is locale-dependent on GNU `coreutils` and locale-INDEPENDENT on macOS.** On the same
  bytes (`md5 eb56ef67162df6db0fabf50819db78f0`) macOS `wc -w` returns **7 527** under `LC_ALL=C`,
  `LC_ALL=C.UTF-8` and `LC_ALL=en_US.UTF-8` alike; GNU `wc` returns **7 367** under `LC_ALL=C` and
  **7 527** under `LC_ALL=C.UTF-8`. **`SL-6`'s defect could not be reproduced on darwin at all** —
  it was found and confirmed from the cloud side of the session. *The general shape, which is the
  part worth keeping: a check this repository runs on one platform can be green there and red for a
  reader on another, and the manuscript is read by the reader, not by darwin.*
- **`paper-I` sits outside `#scope` in `docs/promises-adjudicated.tsv`** and therefore carries 13
  unadjudicated promises the sweep prints and does not gate. That is a deliberate scope line, not a
  gap, and it is named here so no later pass reads the sweep's own output as a defect. Widening
  `#scope` is a decision with a real cost (13 rows, each needing evidence re-run) and it belongs
  after the ship, if ever — `paper-I` is superseded and is not one of the papers this corpus joins.
- **The one §4 figure with no command is `§ 4.2`'s 31.7%.** It is `wt084`'s printed family
  restricted to a ten-per-cent opening gap; the restriction is applied in the prose. `SL-7`'s repair
  DISCLOSES this rather than implying a command. If a future session wants it printed, the change is
  four lines in `wt084_identification_closed_form.py` — **and it is a new instrument under § 1.1
  until the corpus ships.**

### What PASS C inherits FROM PASS B, stated so it is not discovered

**REVIEW-038 § 4's C-class census was taken before Pass B's edits existed.** Pass B added prose in
four places; here is what moved, so Pass C can add to that census rather than re-take it.

| where | what Pass B added | C-class effect |
|---|---|---|
| `paper-III` § 11 | four **Regenerate** bullets, ~30 lines | **Zero hard C-e.** Every artefact named is a committed `scripts/wt###.py` a reader can fetch — the § 2.5 repair clause's own permitted case. No session number, no `REVIEW` doc, no `p7-passes.tsv` reference. |
| `paper-IV` § 10 | one **Regenerate** bullet, 4 lines | Zero hard C-e, same reason. |
| `paper-II`/`III`/`IV` front matter | one revision line each | Written as a claim about the work, not about the working. `defensive_count` +0. |
| `paper-II` References | Piketty (2014) removed | One entry fewer: **15**, not 16. |

**No section moved and no section was reordered.** Every Pass B edit is inside an existing section,
so the 13 C-d fold problems and the 1 C-c orphan Pass C inherits are exactly REVIEW-038's, unchanged
in identity and in location-by-section. **The line numbers in REVIEW-038 have moved** — find those
items by their quoted text, the same rule `SHIP-LIST` set for Pass B.

**The layout baseline moved: 145 pages → 147.** `docs/deliverable/LAYOUT-MANIFEST.json` is
regenerated and `verify-layout.sh` reproduces at the new count. Any doc still saying 145 is stale.

### Ideas that arrived with the repairs

- **A locale-pinning guard.** Every command a manuscript names as checkable could carry its locale,
  and a test could assert that any `wc`/`sort`/`uniq` a manuscript names is written with one.
  `SL-6` is the only known instance; the guard is the general form. New instrument — after the ship.
- **A reference-entry reachability sweep run per-section rather than per-document.** `wt133` sweep 2
  answers *is this entry cited anywhere*; it cannot answer *is it cited at the sentence that relies
  on it*, which is the actual `IV-7`/`SL-8` standard and was applied by hand both times.
