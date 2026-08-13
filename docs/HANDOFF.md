---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-13
session: wealthTensor-24
gate_passed: PENDING
gate_version: "2.50"
---
# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order
1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. §7's student-in, then §5's at-bat. **§6 first if you are about to run the gate.**

> **`-24` in one line: two documents in this repo said a thing was closed or settled, and both
> were wrong in the same shape — a measurement that could not have seen the thing was read as
> evidence the thing was absent.** §1 and §2. If you read nothing else, read the two failure
> modes, because you will meet the third one.

## 0 · TRANSPORT — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -24 without exception**. Roster join/claim as
`big-wealthTensor-25`. `export LESSONS_CONTRIBUTOR=opus`. **`export GATE_ROSTER_WHO=<you>` at the
TOP of the session**, not at the gate — §6.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put /tmp/msg.txt` → `git commit -F /tmp/msg.txt`.
**Stage by PATH. Never `git add -A` on darwin** — one shared tree, seven sibling claims on this
repo while I worked. Three commits this session, each staged by name, each clean.
**581 tests, ~40 s** (was 569).

**NEW · DO NOT RUN A LONG SEC HARVEST FROM DARWIN.** `data.sec.gov` 429'd darwin about 500 firms
into a 6,400-call probe and stayed hostile for twenty minutes of backoff; the identical script from
the cloud container finished 1,602 firms without a single 429. Move the job, don't wait it out.
And the pacing bug that earned it is worth knowing because it passes its pilot: a module-level
"has enough time passed?" timestamp read outside a lock is **not** a rate limit — four threads read
the same stale value and fire together. The fixed version is in `scripts/source001_concentration.py`
(`_pace()` under a lock, 429 stalls the whole pool inside that same lock, partial checkpoints every
100 firms). Also: `ThreadPoolExecutor.map` yields **in order**, so a progress counter can look
frozen for four minutes while eleven workers are busy. It is not hung.

## THE NINE THINGS THAT HAVE EACH COST A SESSION A RUN
1–7 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery — REG-008 F6 asserts the no-rebuild in code;
`git log -S` recovers a dangling ordinal and dates a number; **a feasibility probe that reads the
arm label is the experiment, whatever the file is named**).
8. **Taking "the latest X" and "the latest Y" independently is comparing two periods.** `-23`'s
   lesson, and it earned its keep: the guard it forced into
   `scripts/source001_concentration.py` (`IMPOSSIBLE = 1.05`, refuse and name the firm) fired
   **seven times on the full panel**, the largest an intangibles share of **704**. Once at sample
   scale. A control that fires seven times in one run is not paranoia.
9. **NEW · A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.** Twice
   this session, in two unrelated places, and it is the same mistake:
   - `companyconcept` returns **404 for every duration-typed XBRL fact**, so `-23` measured
     "0 of 80 firms tag `PropertyPlantAndEquipmentUsefulLife`" and wrote *"it is one these filers
     do not use at all"*. **0.82 of the panel tags it.** §1.
   - an 80-firm sample drew **zero** intangibles-dominant firms, so `-23` wrote *"the branch is
     alive for property only"* and offered it as REG-009's title. **34 of 99 panel survivors are
     intangibles-dominant.** §2.
   Ask of any zero: *could this instrument, or this sample size, have produced a non-zero?*

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.
**The gh_sha dance is NOT a defect — do not "fix" it.** `--stamp`, then a commit whose whole content
is the stamp, so `gh_sha` trails HEAD by exactly that commit. `--check` calls that
`ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED — the δ half of §4.7's claim now has a source, and §3 was wrong
`7f74fd1` (SOURCE-001 §3a) · `42f960c` (reach guard) · `148b1f4` (SOURCE-001 §4b).
**Manuscript untouched** — paper III is byte-identical, sha256 verified after a mutation drill.

**`SOURCE-001` §3a — the XBRL lifetime route is OPEN, and it was open the whole time.**
`-23` measured 0 of 80 via `companyconcept` and titled its section *"the machine-readable route is
closed"*. Useful lives are `xbrli:durationItemType` facts — the value is `P39Y`, an ISO-8601
duration, not a number — and `companyconcept`/`frames` serve **numeric** facts keyed by `units`, so
they 404 for every filer including filers that tag it six times. The SEC's Financial Statement and
**Notes** data sets keep the same split as two files: `num.tsv` numeric, **`txt.tsv` everything
else**. On our own panel's 10-K filers:

| | 2015q1 | 2019q1 | 2023q1 |
|---|---|---|---|
| any useful-life tag | 419/500 = **0.838** | 342/399 = **0.857** | 493/562 = **0.877** |
| `PropertyPlantAndEquipmentUsefulLife` | — | — | 459/562 = **0.817** |

0.972 standard `us-gaap` versions, flat across a decade, **dimensioned by asset component ×
`Range=Minimum/Maximum`** — §4.4's "disclosed rectangle" as literal data, median 8 facts per firm.
Hand-audited on **Target**, one of the three firms `-23` named as proof the tag was unused: its own
inline-XBRL 10-K carries the concept six times (`format="ixt-sec:duryear"`), FSN agrees, and
`companyconcept` still 404s. **The tell that caught it:** the first FSN scan read `num.tsv` and
returned 11 filers of 4,711 — *worse* than the number it was meant to beat. **A coverage number
that gets worse when the surface gets bigger is a statement about the surface.**

**`SOURCE-001` §4b — the full-panel count kept §4a's magnitude and inverted its composition.**
1,444 matchable of 1,602. At ≥0.70 of total assets: **99 firms (0.069)** — PP&E 47, **intangibles
34**, goodwill 18; at ≥0.80, 59 — PP&E 32, intangibles 23, goodwill 4. The 74-firm sample said
6 and 3, with **intangibles zero at every threshold**. The proportion was fine (0.081 vs 0.069);
the composition was wrong in both directions, and the composition is what `-23`'s scope ruling was
made of. The script's `--sample` mode reproduces `-23`'s table exactly (74, 11/9/6/3) — that
reproduction is what licenses the comparison, and it is why the probe is committed rather than
thrown away.

**`tests/test_restatement_reach.py` — widened one layer out.** `RESULT_REACH` pins ten REG-004/
REG-005 restatements §7's ledger never declared: §4.10's α_ser/α_eff grid and REG-005's median k̂.
**The handoff said the mechanism "generalises unchanged". It does not** — `REACH` inherits §7's
curation, this table needs its own selection rule, and a bare number-scrape gives 49 "figures" for
REG-004 that are mostly section cross-references and publication years. The rule is **precision**
(≥4 significant digits), asserted in a test rather than described. Drilled 3/3, mutations anchored
by line number (`-23`'s first-match lesson wearing its seatbelt), sha256 restore verified.

## 2 · RULINGS — DO NOT REOPEN
- Prior rulings stand: no third disclosure instrument on this corpus; the two dead (f) keywords stay
  in `INTERNAL`; phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled;
  References block; §4.5's 400-vs-4,000 not a defect. `SOURCE-001` is **not** a registration.
- **REVERSED · `-23`'s "a dominant-asset σ design is a PROPERTY design" is withdrawn.** It was an
  80-firm artifact (§4b). Restricting REG-009 to PP&E is now a **choice to argue from §2's
  admissibility test**, not a description of the panel. Do not put it in a title unargued.
- **REVERSED · "the machine-readable route to useful lives is closed"** (§3). It is open, cheap,
  and better typed than the prose route. Anything citing the old claim — `-23`'s handoff, its
  commit messages, the banked lesson — is citing a corrected error; all three are now annotated.
- **NEW · δ and σ are no longer symmetric.** §4.7's claim has two halves; **δ now has a source and
  σ does not.** A design testing only the lifetime half is available, cheap, and — this is the
  part worth pausing on — **does not depend on §5's selection problem at all**, because §5 is an
  argument about σ's observability and says nothing about lives. Price that split before
  assuming the paired design.

## 3 · NEW MACHINERY
`scripts/source001_concentration.py` (period-matched, refuses impossible shares, `--sample`
reproduces §4a) · `scripts/source001_lifetime_coverage.py` (offline against an FSN notes zip;
`--audit CIK` prints one firm's life rectangle) · `data/source-001-concentration-full.json`
(per-firm record, so the count is auditable without 6,400 SEC calls) · `RESULT_REACH` +
`RESULT_NOT_COUNTED` in `tests/test_restatement_reach.py`. 581 tests.

## 4 · THE AT-BAT, RANKED
1. **σ, and §4b changed which probe is first.** `SOURCE-001` §6 step 3: equity-return volatility
   for **PP&E-dominant firms** — 47 of them at 0.70, not 5. Still the right first probe under §2,
   but no longer the only arm: **intangibles-dominant firms (34) are unassessed and nobody has
   argued whether they pass §2.** My read, offered as a starting point and not a ruling: they are
   closer to the goodwill objection than to the vessel case, because recognised intangibles are
   mostly acquisition residue one step removed from goodwill — but that is an argument to make,
   and §4b's whole lesson is that absence is not an argument.
2. **The δ design, which is new and may outrank σ.** With 0.82 coverage, a firm-year join of
   disclosed lives onto the existing panel is available now. **Do the caveat first**: §3a's
   coverage is measured on Q1 filings, which favours December year-ends, so confirm per-year
   coverage against the panel's own `fy_end` distribution before designing on 0.82. That is one
   more FSN quarter and an afternoon. It would give REG-009 a half that does not wait on §5.
3. **`aar.py sweep`'s coverage fallback is subject-blind** — State Machine `1217468400555940`.
   `SWEEP_MATCH_WINDOW_DAYS = 3`, so one valid AAR grants coverage to every incident-tagged lesson
   within ±3 days regardless of subject, and G-V treats the sweep as its second evidence source.
   Untouched by `-24`; it weakens the gate every session it survives.
4. **The gate defect card** — State Machine `1217465036940491`. Still open, still a good warm-up.
5. **AAR actions A1/A2** — the `pre-commit` roster brake (`1217468064910605`) and an audit of the
   other four `post-*` hooks in `darwin-mac-ops/hooks`. Still not done; `-24` shares a tree with
   seven claimants and got lucky again.
6. **The phrase set has a passenger** (unchanged): 30.4% of trigger sentences match only
   `events or circumstances`; 7.9% carry safe-harbour language. Post-hoc, labelled, outranked.
7. **Widen the reach guard again, to REG-001/002/006's non-ledger restatements.** The mechanism
   and the precision rule now exist; this is the third layer and is mechanical.
8. Cready et al. (2012) full text, if prior art is reopened.

## 5 · WHAT I WOULD DO DIFFERENTLY, since it cost this session an hour
The concentration recount was launched on darwin, 429'd at firm ~500, was nursed with backoff for
twenty minutes, and then finished in 25 minutes from the cloud container on the first try. The
signal that should have moved it immediately was in the first error, not the fifth: **a throttle
that keeps firing after a compliant backoff is an IP-level flag, and no amount of politeness from
that IP clears it.** The harvest script's own docstring has said "Runs in the cloud" since REG-006.

## 6 · THE GATE
See the frontmatter for the verdict; **believe `--emit`'s exit code over this field.** Run
`export GATE_ROSTER_WHO=big-wealthTensor-25` **before** `~/Scripts/gate-selfcheck.sh` — without it
the script cannot tell a sibling's dirt in `~/Scripts` from yours, and with seven live claimants on
this repo that is the difference between a named warning and a false blocker. This is documented
nowhere else.

## 7 · STUDENT-IN
`lessons.py doctrine`, then `search "<task>" --scope global,wealth-tensor`. `-24` banked two and
**curated two that its own work falsified within the hour** — the XBRL coverage leaf (inverted) and
the dominant-asset leaf (property-only clause removed). Both were `-23`'s, both were `quarantine`,
both were honest reports of what had been measured. That is the corpus working: a leaf is not a
claim about the world forever, it is the best measurement to date, and curating one is a normal
Tuesday rather than an embarrassment.
The new ones worth knowing before you start: **a 404 from `companyconcept` is a statement about the
instrument, not the filer** · **a coverage number that gets worse on a fuller surface is a statement
about the surface** · **a zero cell in a small sample is the absence of information, not a small
number** · **an unsynchronised "has enough time passed?" check is not a rate limit, and it passes
its pilot.**
