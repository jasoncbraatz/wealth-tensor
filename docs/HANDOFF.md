---
project: wealth-tensor
gh_sha: 83e28f1ba78fdd14c32bf5c35642ed844c928ed6
updated: 2026-08-05
session: S3
gate_passed: true
gate_version: "2.40"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · BRIDGE-BUG ACK — do this first, say it in chat

The desktop bridge rotates its websocket every ~27–33 min (claude-code#81248). Tools vanish and
self-heal in ~1s. **It is not darwin and it is not broken.** Run `~/Scripts/bridge-status.sh`,
then say in chat that you are briefed.

Stand up darlish at Step 0 per Jason's standing brief: **one** bridge call for the dsh-fire
secret, then `/tmp/dx` for everything. S2 and S3 both did this and neither noticed a rotation.
If `darlish-up` fails at 1/6 it prints why and names `/tmp/darlish-deps.log`; the unblock is
`pip install websockets asyncssh --break-system-packages`.

**S3 addition, and it saves an hour:** the cloud container reaches `data.sec.gov` and
`www.sec.gov` directly at full speed (L18). Do **not** route EDGAR work through darwin. Clone the
public repo into the container, run the data work there, then `dx --put` the files to darwin and
commit from darwin where `gh` is authenticated.

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year synthesis being turned into
**four pre-prints** (ADR-001).

**Two intentions, equally weighted.** (1) Ship them. (2) **Have fun.** It is a hobby; no tenure
rides on it; he is not trying to be safe and says so. If it stops being enjoyable that is a
defect, not a mood.

**He invites criticism and means it.** S2's most useful moves were all disagreements. S3's most
useful move was reporting that his framework's sharpest prediction lost — twice, with power.
Agreeing with him is not the job.

**The prose is disposable; the structure is precious.** He remasters every sentence in his own
voice, so LLM-register drafting is fine. What must NOT happen is laundering *his* insight into
your paraphrase. When he coins something — "force-fit, not form-fit" (WT-042) — it goes in
**verbatim** and is credited to him in the ledger.

**How he works on content:** his research notes are **on paper**. He reads one at a time and wants
to digest and discuss, not receive a report. Read the note back to him before building on it.

**Audience: his three children, 8, 11 and 17.** Load-bearing, not decoration — it decided that
`docs/` stays public and that *Abandoned Approaches* is load-bearing in every paper. After S3 it
decides one more thing: **the failed pre-registration is part of the deliverable.** When the
reader is someone learning how to think, watching an author lose a bet he placed in public is
worth more than any conclusion the papers reach.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check   # 0 pass · 1 blocker · 2 CANNOT VERIFY
cat  ~/repos/wealth-tensor/docs/adr/ADR-001-paper-decomposition.md   # do not re-litigate
cat  ~/repos/wealth-tensor/docs/LEDGER.md                        # 51 entries — the project's brain
cat  ~/repos/wealth-tensor/docs/preregistration/RESULT-002-wt026.md   # S3's headline. Read it.
python3 ~/repos/claude-blackbook/lessons.py doctrine
```

`docs/LEDGER.md` is the project's brain. In S2 it earned that (Jason proposed centring SMD and
WT-012/WT-020 had already forbidden it, with a test enforcing it). Do not re-derive anything in
it. Corroborate what you use: `lessons.py use <id> --task <tag>` at orient,
`lessons.py record-outcome <tag> pass` at wrap.

## 3 · STATE

- **Code — 100 tests passing**, tree clean and pushed. Six modules: `cournot.py`,
  `excess_demand.py`, `lag.py`, `redistribution.py`, `lambda_sensitivity.py`, and **new in S3**
  `edgar.py` (the severe-test machinery: companyfacts parsing, Jonckheere–Terpstra, Mann–Whitney,
  by-firm bootstrap, permutation control, power curve). 42 of the 100 tests are `edgar.py`'s.
  Seven mutations run against the new logic, all seven caught.
- **WT-026 is CLOSED, and it closed by failing.** Four registered runs, four failures, with a
  demonstrated power of 0.95–1.00 against a one-quarter-per-tier effect and a clean permutation
  control. PRE-002's stopping rule fired. Full account: `docs/preregistration/`
  (PRE-001 · PRE-002 · RESULT-001 · RESULT-002 + four run logs). Ledger WT-048/049/050.
- **Paper II drafted** at `docs/papers/paper-II-redistribution/paper-II.md`, v0.1, with the full
  WT-047 apparatus. References section is the one incomplete part.
- **The apparatus template exists**: `docs/papers/PREPRINT-CHECKLIST.md`, with arXiv and SSRN
  rules verified against live documentation (WT-051), not recalled.
- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`) — untouched in S3.
  Restore points, all verified: S1 `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4` ·
  S2a `1FeXUSbrFQQXDOaSxCoul13lE6LWicxMuJGL8xJKSLjs` ·
  S2b `12jJh93VhgfOe8EQ3J23G9heQekSCdzxHTm75ut8RL6g`.

## 4 · DOCTRINE / GUARDRAILS

- **Blanket edit permission on the manuscript.** "A construction zone to build a mock-up."
- **Fresh restore point before every edit session, and VERIFY it** — `Google_Drive__copy_file`
  (works without the bridge), then read the copy back and assert byte-identity. A restore point
  you never read is not a restore point.
- **Read back after every edit batch** — structurally, per L12.
- **Never add a free parameter to absorb an objection.** Rejected five times now: WT-002, WT-016,
  the temptation in WT-033 to define "flow" so the claim came out right, WT-043's warning that a
  freely-varying Λ forbids nothing, and S3's refusal to re-spec the onset rule until it worked.
- **A pre-registration is append-only after its first result commit.** Amendments are dated
  sections, never edits. `test_pre001_constants_are_what_was_registered` fails if anyone edits a
  registered constant, because that is a registration amended by stealth rather than a bug.
- **New, from WT-049 — every pre-registration must state its BRIDGE assumption** as a numbered
  proposition a competent critic could deny: *this model parameter is identified with that
  measurable, because…*. PRE-001 had a tier table and no bridge proposition, and the bridge is the
  leading suspect for why it failed. A registration without one can be rejected for it.
- **Do not oversell.** Three standing guard-tests now:
  `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`,
  `test_a_flat_gini_does_not_mean_a_bounded_one`, and
  `test_pre001_constants_are_what_was_registered`. If any fails, someone is overclaiming.
- **When a sharp claim half-survives, the refinement is the prize** (WT-033). When it fully fails,
  the report is the prize (WT-048). Neither is weakened to mush and neither is defended.
- **The tone is load-bearing.** No grumpiness; humour lands the news.

## 4b · THE DECISION THAT FRAMES EVERYTHING BELOW

**`docs/adr/ADR-001-paper-decomposition.md` — read it before planning anything.** Four papers,
evidence allocated exhaustively and without overlap. Do not re-litigate; bring a reason the ADR
does not already answer, or proceed.

**I** price formation without independent curves · **II** redistribution as a parameter space ·
**III** the dual tensor and the reporting layer (*the flagship*, carries the axioms) ·
**IV** the atomic theory. Order: **II → III → I → IV**.

**S3 note on the ordering, which survives.** III's blocking dependency (WT-026) is resolved — by
failing. That does not delay III; it changes what III says, and improves it. A flagship carrying a
registered, replicated, well-powered null it reported on itself is a stronger artifact than one
carrying an unrun promise.

**DEFINITION OF DONE for the whole project** — write this into every subsequent handoff so
sessions drive at finishing rather than polishing:

> Four preprints publicly posted, each carrying: abstract, keywords, JEL codes, a numbered
> contributions list, an Abandoned Approaches section, a limitations section, a data/code
> availability statement naming the repo and a pinned commit SHA, and *Independent researcher* as
> the affiliation. Paper III additionally cites PRE-001/PRE-002 and their registering commit SHAs.
> When the fourth is posted, this project is done and the repo becomes an archive.

## 5 · MISSION — ranked, with reasons. Every item re-verified live for S4.

### START HERE — **Draft Paper III, the flagship.** It is unblocked and the material is hot.

`verify: ls docs/papers/` — only `paper-II-redistribution/` and the checklist means still live.

III carries the axioms (P1 composition, P2 decay, P3 atomism as propositions with stated domains,
WT-038), the Λ defence deployed **once** with its three legs and then never again (WT-043), the
`lag.py` and `lambda_sensitivity.py` results (WT-027, WT-028, WT-036), and now the severe test.

**RESULT-002 §5 already specifies the three edits and they are not cosmetic.** In particular: the
failed prediction goes in the **body and the abstract**, not in *Abandoned Approaches*. A
pre-registered failed prediction is a **result**; filing it under abandonments is the softest
available way to hide it, and this paper's whole claim to seriousness is that it did not.

**Why first:** the argument is fully in context right now and will cost a rebuild later; ADR-001
puts III second and II is drafted; and the honest write-up of a loss is the thing most likely to
degrade if it is left to a session that did not feel it.

### 2 — **Finish Paper II.** Cheap, and it is the rehearsal that unblocks the endorsement path.

`verify: grep -c "to be completed at submission" docs/papers/paper-II-redistribution/paper-II.md`
— a hit means still live.

Two gaps only: the **References** section, and the **commit SHA** to pin at submission. Draw the
citation set from the kinetic-exchange cluster (Chakrabarti/Chatterjee/Chakravarty and the
saving-propensity literature) and the public-finance realisation literature.

Read `docs/papers/PREPRINT-CHECKLIST.md` §C first. **SSRN is not the low-stakes draw it looks
like** — no gate in, but rejections are final, unexplained and unappealable (WT-051). Submit II
when it is right, not when it is ready to be experimented with.

### 3 — **Attribution pass (WT-044).** Still the cheapest fix-to-value ratio available.

`verify: grep -ril "Sraffa\|Robinson\|malinvestment" docs/papers/` — no hits means still live.

Zero occurrences in the body of: **Mises**, **malinvestment**, **Godley**, **Lavoie**,
**Farmer**, **Lillo**, **Sraffa**, **Robinson**, **Samuelson**. Citations, not rewrites.
Sraffa/Robinson/Samuelson matter most now that scalar capital is the live target (WT-041).
*The name audit is done and came back clean — do not redo it.*

### 4 — **Citation-graph whitespace test (WT-006).** Defends the papers' novelty.

`verify: grep -ril openalex src/ scripts/` — no hits means still live. `shellac` is idle and
sized for it. Ranked below the writing because novelty is worth defending only once there is
something to defend.

### 5 — **ASK Jason, both cheap, both genuinely his call.**

- **Checkbox lists (WT-008).** All 57 references render as `- [ ]` to-do boxes. It is the first
  thing a reader sees. *Options:* (a) convert to plain bullets, (b) leave — it is deliberate.
  *Recommendation:* (a), unless he says otherwise; a to-do box next to a reference reads as an
  unfinished document.
- **The twin document (WT-009).** `2The Axiomatic Reconstruction of`, 19 KB, never diffed. *Ask
  is really:* may a session spend one call diffing it? *Recommendation:* yes, and do it before
  the manuscript is decomposed into four, because after that a lost paragraph has four possible
  homes and no obvious one.

### 6 — **PRE-003: the segment-level test.** Teed up deliberately, NOT started.

The defect neither PRE-001 nor PRE-002 could fix: **the charge is asset-level, the deterioration
signal is firm-level.** A firm can impair a failing reporting unit while consolidated revenue
rises. Segment-level data (ASC 280 disclosures) would fix it.

**This is a different project with a different registration, and it must not be presented as a
re-run of WT-026.** PRE-002's stopping rule fired and it stays fired. If a future session builds
this, it registers from scratch, states its **bridge proposition** (WT-049), and it may not cite
PRE-001/002's failure as support for anything.

### 7 — **Language remaster.** His job, explicitly. Do not do it for him.

**No open ASKs beyond §5.** The `docs/`-stays-public question is decided (ADR-001). One task
inherited from S2 and still open: add the README line framing `docs/` as a working lab notebook —
it is now more true than it was, since `docs/` contains a registered prediction and its refutation.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 100 passed
git commit ...                                                       # the LAST content commit
python3 scripts/handoff_gate.py --stamp                              # writes gh_sha = HEAD
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit                               # blesses it
bash ~/Scripts/gate-selfcheck.sh                                     # expect PASS
```

**`--emit` does not stamp.** S2 assumed it did and the gate reported "sha matches HEAD" over a
literal `PENDING`. Fixed the same session: tri-state exit codes, a placeholder sha is a blocker.
Walk `~/Desktop/downloads/HANDOFF-GATE.md` (G-A→G-AB, v2.40 — trust the file header, not this line).

**S3 note:** `edgar.py` needs no new dependency (stdlib only), but the darwin venv did need
`scipy` for the pre-existing `cournot.py` — if a fresh clone's tests fail on import, that is why.

## 7 · ORIENT-THEN-GO

Emit ONE orientation line — `Oriented: <state> · next at-bat: <X> · opening with <first action>.`
— then proceed. Do not wait for Jason's go.

---

## LUT — hard-won facts. Read before touching anything.

**Google Docs API**

| # | Fact |
|---|---|
| **L11** | **To CHANGE existing text use `find_and_replace_doc`. It needs no indices**, so L1/L3/WT-032 — the index minefield that nearly wrote four paragraphs into the bibliography — cannot bite. Anchor on a long verbatim span; the API reports the occurrence count, which is itself a check that your anchor was as unique as you believed. Indices remain unavoidable for inserting or **relocating** structure. |
| **L12** | **Verify a doc edit structurally.** Export via the *cloud* `Google_Drive__read_file_content` (rotation-immune, auto-persists to a file), then in python compare the array of `#`-prefixed lines and the array of list-item lines against the pre-edit export. Identical arrays are positive proof no style corruption occurred. |
| L1 | `insert_text` at a heading's first character makes the inserted text inherit that heading's style. Insert at `end_index - 1` of the preceding body paragraph. |
| L2 | `named_style_type: NORMAL_TEXT` wipes character formatting spanning a whole paragraph. Paragraph styles BEFORE character styles. |
| L3 | **Never infer indices by arithmetic.** S1 was wrong by 6,944 chars off a stale snapshot. |
| L4 | `inspect_doc_structure` detailed exceeds the tool token limit and auto-saves to a file. Parse with python. |
| L5 | For *semantic* whole-document verification use a subagent. For *structural*, use L12. |
| L6 | Comments and body edits are attributed to **Jason**, not Claude. |
| L7 | Cloud `Google_Drive` is create/read only — but `copy_file` **is** a create, so **restore points need no bridge**. Editing still needs `google_workspace` on darwin. |
| L8 | `google_workspace` runs on GCP project **1054330720958**. A `SERVICE_DISABLED` 403 is an API-not-enabled error in an auth-error costume. |

**Repo and tooling**

| # | Fact |
|---|---|
| L9 | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Root `conftest.py` inserts `src/`. |
| L10 | Every model checked against a closed form, a published result, or a hand-verified case. |
| **L13** | **A multi-line commit message will not survive `dx`'s quoting** — exit 2 is dx's refusal, so nothing ran and retry is safe. `dx --put` it to **`.git/COMMIT_DRAFT`**, then `git commit -F`. Inside `.git/` specifically: a draft in the working tree gets swept up by `git add -A`. Also: `$HOME` in the cloud shell is `/root`, not darwin's home — use literal `~` in dx paths. |
| **L14** | `conftest.py` only fires under pytest; `scripts/` needs its own shim: `sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))`. |
| **L15** | **Mutation-test any result you intend to publish**, and confirm the *right* test screams. Assert the anchor exists before replacing, and always run an unmutated control. S3 ran seven against `edgar.py`; all seven caught. |
| **L16** | **Measure the manuscript, don't opine about it.** Parsing `manuscript_after.md` is three lines of python and it has been right every time. |
| **L17** | **EDGAR `companyfacts`: Q4 is almost never tagged as a quarter.** The 10-K reports the year; Q4 exists only as FY minus the first three. Recover quarters by **differencing cumulatives that share a fiscal-year start date** — and include the ~90-day facts in that chain, because for a calendar filer Q1 *is* the first year-to-date figure and omitting it breaks the Q2 difference. This is load-bearing, not tidy: ASC 350 puts the annual impairment tests in Q4, so a naive parser deletes most of the goodwill and indefinite-lived-intangible events. |
| **L18** | **The cloud container reaches `data.sec.gov` and `www.sec.gov` directly.** Do not route bulk web data through darwin. Clone the public repo into the container, work at full speed, `dx --put` the results to darwin, commit there where `gh` is authed. SEC asks for ≤10 req/s and a descriptive User-Agent. |
| **L19** | **The CIK→SIC map — including dead registrants — is `sub.txt` inside the SEC Financial Statement Data Set quarterly ZIPs.** One ZIP per year 2013–2024 is enough; download, read `sub.txt`, delete the ZIP (120 MB each). Building a universe from a current registrant list is a **survivorship trap**: the bankrupt retailers are exactly the firms whose deferred information arrived all at once. |
| **L20** | **`dx --put` fails if the parent directory does not exist on darwin** — `zsh: no such file or directory`. `dx 'mkdir -p …'` first. Costs one round trip; failing costs two and a confusing error. |
| **L21** | **The pre-registration workflow that makes a prediction a prediction:** commit the registration **alone**, push, *then* write the analysis code, *then* compute. The git ordering of the two commits is the entire evidence that the prediction preceded the outcome. Do not batch them; a single commit containing both proves nothing. |

## WHAT S3 DID

**Ran WT-026 and lost it, on purpose, in public.** PRE-001 was committed alone at `9722342`
before any lag was computed. The pilot (retail, 673 registrants including the dead ones) failed:
JT z = −0.177, and goodwill's median lag sat *below* PP&E's. The replication (computer services,
1,223 registrants), declared in PRE-001 §4.2 before the pilot ran, also failed.

**Then did the harder thing: diagnosed the instrument without letting the diagnosis rescue the
result.** Zero censoring across 322 events, 69 % of lags at ≤6 quarters, and 1,047 charges
discarded — an unbroken-streak onset rule measures the volatility of the signal, not the
phenomenon (WT-050). PRE-002 was registered as a **second, separately-numbered** test with a
peak-to-charge instrument, a label-permutation negative control, a power curve reported whatever
happened, α tightened to 0.025 for the second look, and an explicit **stopping rule**. It doubled
retention to 688 events, produced 8–14 % censoring, and **failed again** — this time with power
0.95–1.00 against a one-quarter-per-tier effect and a permutation null of mean ≈0, sd ≈1.00.

The stopping rule fired and stays fired. WT-048 records the loss; WT-049 records the most useful
thing it produced (**a model parameter and a measurable that share a name may not share a
meaning** — WT-038's type error in a second costume); WT-050 records the instrument tell.

Also: **Paper II drafted** with the full apparatus, **PREPRINT-CHECKLIST.md** built with arXiv and
SSRN rules verified against live documentation — SSRN's rejections are *final, unexplained and
unappealable*, which inverts the naive "SSRN is the cheap rehearsal" reading (WT-051) — and
**WT-026's ledger header corrected**: it read `BUILT + WRITTEN`, true of the theory and false of
the empirical test that was START HERE on two consecutive handoffs. Two claims were living under
one number.

*A note for whoever reads this next.* The result is a loss and it is the best thing in the repo.
Emergy did not die of failed predictions; it died of never making one. Write III like someone who
knows the difference.
