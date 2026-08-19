#!/usr/bin/env python3
"""Staleness guard for docs/HANDOFF.md.

The handoff lives in the repo so it can be version-controlled and turned over rather than
accreted. The cost of that choice is that a stale file looks authoritative in a way a stale
chat message does not. This script is the price of admission -- HANDOFF-GATE.md §G-F is
explicit that the file half must not be adopted without it.

  --check   run at ORIENT. Compares the handoff's recorded gh_sha against HEAD and
            distinguishes code drift (blocker) from docs-only drift (advisory).
  --stamp   rewrite gh_sha to HEAD. Run AFTER the final content commit.
  --emit    run at WRAP. Refuses to bless the handoff on missing fields, TODO
            placeholders, a dirty tree, gh_sha != HEAD, gate_passed: false, or a
            `phase:` claim that no `claims:` entry declares.
  --claims  G-CLAIMS. RE-RUNS what the handoff's phase block claims, un-piped, and
            re-runs a disagreement before reporting it. --claims-all includes the
            slow ones. See the G-CLAIMS section for why each of those words is load-
            bearing.

Correct wrap sequence -- --emit does NOT stamp, and running it on an unstamped file was
a silent-green failure until 2026-08-05 (see below):

    git commit ...                      # the last content commit
    python3 scripts/handoff_gate.py --stamp
    git commit -am "docs: stamp handoff gh_sha to HEAD"
    python3 scripts/handoff_gate.py --emit

EXIT CODES ARE TRI-STATE. 0 = pass. 1 = BLOCKER. 2 = CANNOT VERIFY, which is NOT a pass.

Why 2 exists (bug found and fixed 2026-08-05, S2). `sh()` swallows git's stderr and returns
an empty string on failure, so `git diff --name-only <garbage>..HEAD` looked exactly like
"nothing changed". A handoff carrying `gh_sha: PENDING` therefore made --check print a cheery
advisory and return 0, and made --emit print "sha matches HEAD" and bless the file. The gate
built to catch stale handoffs was blind to the most obvious stale handoff there is. An
unverifiable claim must never be reported as a verified one.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDOFF = ROOT / "docs" / "HANDOFF.md"
REQUIRED = ["project", "gh_sha", "updated", "session", "gate_passed", "gate_version"]

# --- the definition-of-done force function (ported from the canonical handoff-kit gate,
# --- pitchingMachine-5, 2026-08-15) --------------------------------------------------------
# THIS FILE IS NOT A COPY OF THE CANONICAL GATE. It shares a filename and nothing else -- its
# own lineage, its own REQUIRED set, its own sha classifier, its own coach. The at-bat spec
# said "propagate all 5 copies and verify byte-identity"; that instruction was written from a
# retelling. Byte-propagating here would have DELETED classify_sha, coach() and anchors() --
# every hard-won control wealthTensor-27/-28 built -- and the byte-identity check would have
# reported success. So the FEATURE is ported and the file is not: check() shows the line,
# emit() requires it, stamp() refuses without it. Same three moments, this file's idiom.
#
# No ledger derivation here on purpose: wealth-tensor has no auto-bridge row, so its DoD lives
# in ADR-001 and is quoted into the frontmatter. If it ever gains a row, port ledger_dod() too.
DOD_KEY = "definition_of_done"
DOD_REQUIRED = os.environ.get("HANDOFF_DOD_REQUIRED", "1") not in ("0", "false", "no")
DOD_PLACEHOLDERS = ("", "FILL ME IN", "FILLMEIN", "TODO", "TBD", "XXX", "N/A", "?")


def dod_value(fm):
    """The stated DoD, or "" if what is there is a PLACEHOLDER. A scaffolded key that passes
    the gate is decoration -- the wrap would go green with "FILL ME IN" as the definition of
    done and every surface downstream would print it with a straight face."""
    v = (fm.get(DOD_KEY) or "").strip().strip("\"'").strip()
    u = v.upper()
    if u in DOD_PLACEHOLDERS or u.startswith("FILL ME IN") or (v.startswith("<") and v.endswith(">")):
        return ""
    return v


def dod_howto():
    """A refusal that does not name the fix converts drift-protection into a spelunk. Session 0
    should not have to know where the DoD lives -- it learns here, once, at its first wrap."""
    return [
        "  FIX IT: add this line to the frontmatter of docs/HANDOFF.md --",
        '      %s: "<one checkable sentence>"' % DOD_KEY,
        "  NORTH-STAR §4 is the test: could someone mark that sentence right or wrong?",
        "  For this repo the answer already exists: ADR-001 carries the corpus-level clause",
        "  and the per-paper clauses. Quote it; do not invent a new one.",
    ]


SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def sh(*args):
    """stdout of a git command, or "" -- use `sh_ok` when a failure must be distinguishable."""
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.strip()


def sh_ok(*args):
    """(stdout, ok). The `ok` flag is the whole point: an empty stdout from a FAILED command
    is not the same fact as an empty stdout from a successful one, and conflating them is
    what made this gate score a placeholder sha as a match."""
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip(), r.returncode == 0


def classify_sha(recorded):
    """"placeholder" | "absent" | "present". Three answers, because they need three responses.

    placeholder -- not 40 hex chars at all (PENDING, TODO, an empty string). Unambiguously
                   wrong, and a blocker wherever it is found.
    absent      -- well-formed but not an object in this clone. Could be a shallow clone or a
                   sha from another repo; either way the comparison CANNOT be made. Not a pass.
    present     -- a real commit here; proceed with the normal comparison.
    """
    if not SHA_RE.match(recorded or ""):
        return "placeholder"
    _, ok = sh_ok("git", "cat-file", "-e", f"{recorded}^{{commit}}")
    return "present" if ok else "absent"


def frontmatter():
    if not HANDOFF.exists():
        sys.exit("BLOCKER: docs/HANDOFF.md does not exist")
    text = HANDOFF.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("BLOCKER: docs/HANDOFF.md has no YAML frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", line):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, text


def files_changed_since(sha):
    out = sh("git", "diff", "--name-only", f"{sha}..HEAD")
    return [f for f in out.splitlines() if f]


def show_dod(fm):
    """Print what done looks like, FIRST, above everything else this gate has to say.

    Position is the mechanism. A session reads the top of the output and skims the rest; the
    one line it can least afford to skim therefore goes at the top. A corpus-level DoD matters
    MORE here than in a repo with a passing test, not less: prose has no bit that flips, so
    a stated finish line is the only thing standing between a session and a very well-written
    paragraph nobody asked for. And it has to be the RIGHT line: wealth-tensor carried "three
    preprints publicly posted" as its DoD for fifty-four sessions and its owner's actual finish
    line was "cleared for liftoff", two whole projects earlier."""
    dod = dod_value(fm)
    if not dod:
        print("\U0001F3AF DONE = (NOT STATED — this handoff does not say what done looks like)")
        print("   Fix that before anything else; it is cheaper than any work you could do today.")
        for line in dod_howto():
            print(line)
        print("")
        return
    print(f"\U0001F3AF DONE = {dod}")
    print("   Is your at-bat on the path to that line? If not, STOP and say so —")
    print("   you are on neither the map nor the territory.\n")


def show_checklist():
    """The session-0 checklist CONTOUR, ported BY HAND from the handoff-kit canonical
    (sessionZero-01, 2026-08-16 — this repo's gate is a deliberate fork, propagate-gate.sh
    excludes it, so the port is manual like the DoD one was). docs/CHECKLIST.md is what the
    corpus set out to do; this prints distance-to-done and asks that drift be NAMED. It never
    blocks and never touches the exit code — sixty sessions of handoffs predicting the next
    at-bat from the previous session's vantage point is how ten sessions of guards happened
    to a three-paper corpus, and the cure is a fixed destination in view at every orient,
    not another blocker."""
    path = ROOT / "docs" / "CHECKLIST.md"
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    done, todo = [], []
    for ln in lines:
        m = re.match(r"\s*-\s*\[([ xX])\]\s*(.+)", ln)
        if m:
            (done if m.group(1).strip() else todo).append(m.group(2).strip())
    if not done and not todo:
        return
    print(f"checklist      : {len(done)}/{len(done) + len(todo)} done (docs/CHECKLIST.md — the corpus contours)")
    for t in todo[:8]:
        print(f"     open      : {t}")
    if len(todo) > 8:
        print(f"     open      : ... and {len(todo) - 8} more")
    if todo:
        print("     CONTOUR   : if this session's work aims at none of the open lines, that is")
        print("                 drift — maybe GOOD drift. Name it in the handoff either way,")
        print("                 and if it is a guard, say which PAPER CLAIM the guard protects.")
    else:
        print("     every corpus line is ticked — is the Definition of Done MET? Say so out")
        print("                 loud; a milestone met but never declared keeps getting continued.")


def check():
    fm, _ = frontmatter()
    show_dod(fm)
    show_checklist()
    head = sh("git", "rev-parse", "HEAD")
    recorded = fm.get("gh_sha", "")
    print(f"handoff gh_sha : {recorded}")
    print(f"repo HEAD      : {head}")
    if recorded == head:
        print("IN SYNC: the handoff describes this exact commit.")
        return 0
    kind = classify_sha(recorded)
    if kind == "placeholder":
        print(f"\nBLOCKER: gh_sha {recorded!r} is not a commit sha. The handoff was never\n"
              "         stamped, so nothing about it can be trusted as current. Whoever wrote\n"
              "         it skipped `--stamp`; re-read git log rather than believing the file.")
        return 1
    if kind == "absent":
        print(f"\nCANNOT VERIFY (exit 2): gh_sha {recorded} is well-formed but is not an object\n"
              "         in this clone -- a shallow clone, or a sha from somewhere else. This is\n"
              "         NOT a pass. Run `git fetch --unshallow` and try again.")
        return 2
    changed = files_changed_since(recorded)
    if not changed:
        print("ADVISORY: the recorded commit is an ancestor with no diff to HEAD.")
        return 0
    code = [f for f in changed if not f.startswith("docs/")]
    print(f"\n{len(changed)} file(s) changed since the handoff was written:")
    for f in changed:
        print(f"  {'CODE' if not f.startswith('docs/') else 'docs'}  {f}")
    if code:
        print("\nBLOCKER: code advanced past the handoff. Re-read git log before trusting it.")
        return 1
    print("\nADVISORY: docs-only drift. The described state still holds.")
    return 0



# --------------------------------------------------------------------------- charter
# G-ANCHOR / G-COACH, added wealthTensor-11 from CHARTER-ANCHOR-block.md §5.
# The charter is the constitution; the handoff is the game plan. These checks exist so
# that permeation is automatic rather than memorial -- a rule nobody enforces is a wish.

CHARTER = ROOT / "docs" / "CO-AUTHOR-CHARTER.md"
BASELINE = ROOT / "docs" / ".coach-baseline.json"

ANCHOR_READ = "docs/CO-AUTHOR-CHARTER.md"
ANCHOR_PRECEDENCE = "THE CHARTER WINS"

PAPERS = sorted((ROOT / "docs" / "papers").glob("*/paper-*.md"))

# Sentences that open by conceding rather than by claiming. Counted, not banned: one is
# candour, thirty is a paper apologising for existing. The list is deliberately short and
# literal -- a clever regex here would be a guard that cannot fail.
CONCESSIVES = (
    "Admittedly", "Of course", "It must be conceded", "To be fair", "It should be noted",
    "It is worth noting", "We acknowledge", "It must be admitted", "Needless to say",
    "In fairness", "It bears repeating", "It is important to note",
)

# First-person process narration -- the paper talking about its own conduct instead of
# its subject. Legitimate in the AI-assistance note, in the abandonments and in the
# survivals ledger; a smell anywhere else.
CONDUCT = (
    "this programme", "this paper's earlier draft", "revision history",
    "an earlier draft", "the draft that preceded",
)
CONDUCT_ALLOWED_SECTIONS = ("## 6 ", "## 7 ", "## 8 ", "## 9 ", "## 10 ", "## 11 ",
                            "# Appendix")


def _sections(text):
    """Split a paper into (heading, body) at level-2 headings."""
    out, head, buf = [], "(front matter)", []
    for line in text.split("\n"):
        if line.startswith("## ") or line.startswith("# Appendix"):
            out.append((head, "\n".join(buf)))
            head, buf = line, []
        else:
            buf.append(line)
    out.append((head, "\n".join(buf)))
    return out


def coach(write_baseline=False):
    """G-COACH-2 and G-COACH-3. Countable, so they cannot be argued with."""
    problems, counts = [], {}
    for paper in PAPERS:
        text = paper.read_text()
        key = paper.parent.name
        concessive = sum(text.count(c) for c in CONCESSIVES)
        stray = 0
        for head, body in _sections(text):
            if any(head.startswith(a) for a in CONDUCT_ALLOWED_SECTIONS):
                continue
            stray += sum(body.count(c) for c in CONDUCT)
        counts[key] = {"concessive": concessive, "conduct_outside_allowed": stray}
        print(f"  {key:<28} concessive openers {concessive:>3}   "
              f"conduct narration outside §§6-11 {stray:>3}")

    if write_baseline or not BASELINE.exists():
        BASELINE.write_text(json.dumps(counts, indent=2, sort_keys=True) + "\n")
        print(f"  baseline written to {BASELINE.relative_to(ROOT)} "
              f"({'refreshed' if write_baseline else 'first run'})")
        return 0, problems

    prev = json.loads(BASELINE.read_text())
    for key, now in counts.items():
        was = prev.get(key)
        if was is None:
            continue
        for metric in ("concessive", "conduct_outside_allowed"):
            if now[metric] > was[metric]:
                problems.append(
                    f"G-COACH-3: {key} {metric} rose {was[metric]} -> {now[metric]}; "
                    "defensiveness is non-increasing by charter, or the baseline is "
                    "refreshed deliberately with --coach-refresh")
    return (1 if problems else 0), problems


def anchors():
    """G-ANCHOR-1 and G-ANCHOR-2: the handoff must point at the constitution."""
    problems = []
    if not CHARTER.exists():
        problems.append(f"G-ANCHOR: {CHARTER.relative_to(ROOT)} is missing -- the charter "
                        "is the SSOT and a handoff cannot cite what is not there")
    text = HANDOFF.read_text()
    if ANCHOR_READ not in text:
        problems.append("G-ANCHOR-1: the handoff does not tell the next session to read "
                        f"{ANCHOR_READ} at ORIENT")
    if ANCHOR_PRECEDENCE not in text:
        problems.append("G-ANCHOR-2: the handoff carries no precedence clause "
                        f"({ANCHOR_PRECEDENCE!r}) -- without it a rewrite silently becomes law")
    return problems


def emit():
    fm, text = frontmatter()
    problems = []
    for k in REQUIRED:
        if not fm.get(k):
            problems.append(f"missing frontmatter field: {k}")
    if not dod_value(fm):
        raw = (fm.get(DOD_KEY) or "").strip()
        msg = (f"{DOD_KEY} is still a placeholder ({raw[:40]!r})" if raw else
               f"missing frontmatter field: {DOD_KEY} — the handoff does not say what done "
               "looks like, so nothing downstream can tell drift from progress")
        if DOD_REQUIRED:
            problems.append(msg)
        else:
            print(f"  ! {msg}   [WARNING TODAY, BLOCKER SHORTLY — fix it now]")
    if fm.get("gate_passed", "").lower() != "true":
        problems.append("gate_passed is not true -- walk HANDOFF-GATE.md first")
    head = sh("git", "rev-parse", "HEAD")
    recorded = fm.get("gh_sha", "")
    if recorded != head:
        kind = classify_sha(recorded)
        if kind == "placeholder":
            problems.append(
                f"gh_sha is {recorded!r}, not a commit sha -- run --stamp, commit, then --emit")
        elif kind == "absent":
            problems.append(
                f"gh_sha {recorded} is not an object in this clone; the comparison cannot be "
                "made and an unverifiable handoff must not be blessed")
        else:
            # Stamping necessarily moves HEAD, so gh_sha trails by exactly the stamp commit.
            # Tolerate that and only that: the sole file changed since gh_sha must be this file.
            drifted = [f for f in files_changed_since(recorded) if f != "docs/HANDOFF.md"]
            if drifted:
                problems.append(
                    f"gh_sha {recorded} != HEAD {head}; content changed since stamp: {drifted}")
    if sh("git", "status", "--porcelain"):
        problems.append("working tree is dirty -- commit before emitting")
    body = text.split("---", 2)[-1]
    problems += placeholders_left(body)
    problems += anchors()
    problems += claims_static()
    print("\ncoach metrics (G-COACH-2, G-COACH-3):")
    _, coach_problems = coach()
    problems += coach_problems
    if problems:
        print("HANDOFF REFUSED:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("HANDOFF OK: frontmatter complete, sha matches HEAD, tree clean, no placeholders.")
    return 0



PLACEHOLDERS = ("TODO", "TBD", "FIXME", "<fill", "XXX")


def placeholders_left(body):
    """Placeholder markers actually LEFT in the handoff, not merely named by it.

    A NEGATIVE GREP CANNOT TELL USE FROM MENTION -- and this gate's own handoff has said
    so, in as many words, since wealthTensor-54, in the drift flag about RECIPE.md's banned
    wording. The flag was right and this check was the counter-example: the sentence
    "...classes with no legitimate use (TODO/TBD/FIXME/XXX) and leave wording prohibitions
    to prose" has sat in the handoff body since at least cbffb8d, and it made `--emit`
    refuse a handoff whose only offence was DOCUMENTING THE MARKERS. Found at
    wealthTensor-94, at the last act of the wrap, which is exactly where a checker nobody
    can satisfy does the most damage: the cheap way out is to delete the sentence, and
    deleting documentation to satisfy a checker is how a repository forgets things.

    Two mentions are recognised and skipped, both narrow on purpose:

      1. THE MARKER SET RECITED AS ITSELF -- "TODO/TBD/FIXME/XXX". A slash-joined run of
         two or more markers is an enumeration of the vocabulary, never a placeholder; no
         real leftover looks like that.
      2. A MARKER INSIDE A CODE SPAN -- `TODO`. Backticks are how this corpus quotes a
         token it is talking ABOUT rather than using.

    Everything else still counts, including a bare TODO in prose, which is the case the
    check exists for. If a future handoff needs to discuss a marker outside both forms,
    widen this deliberately and say so here -- do not reword the handoff.
    """
    RECITAL = re.compile(r"\b(?:%s)(?:/(?:%s))+\b"
                         % ("|".join(re.escape(p) for p in PLACEHOLDERS if p.isalpha()),
                            "|".join(re.escape(p) for p in PLACEHOLDERS if p.isalpha())))
    scrubbed = RECITAL.sub("", body)
    scrubbed = re.sub(r"`[^`\n]*`", "", scrubbed)
    return [f"placeholder {p!r} left in the handoff body"
            for p in PLACEHOLDERS if p in scrubbed]


def stamp():
    """Rewrite gh_sha to current HEAD. Run after the final content commit.

    COUNTS THE SUBSTITUTION AND FAILS AT ZERO (wealthTensor-28). `re.sub` returns the
    input unchanged when nothing matches, so the previous version wrote a handoff whose
    frontmatter had no `gh_sha` key straight back to disk, byte-identical, and printed
    "stamped gh_sha: <head>" regardless. It could only fire on a handoff that was ALREADY
    malformed -- which is precisely when a false success costs the most, because --check
    then refuses a file its author has been told is stamped. Live fire: --stamp said it
    stamped, git said "nothing to commit, working tree clean", and --check kept blocking.
    Same family as `grep -c P f || echo 0` (-27): a success report on a path where
    nothing happened."""
    fm, text = frontmatter()
    # The wrap is where the DoD is ENFORCED rather than shown -- and it is the cheapest possible
    # moment to write one, which is exactly why skipping it here is the most expensive.
    if not dod_value(fm):
        raw = (fm.get(DOD_KEY) or "").strip()
        msg = (f"{DOD_KEY} is still a placeholder ({raw[:40]!r})" if raw else
               f"no {DOD_KEY} in the handoff")
        if DOD_REQUIRED:
            print(f"REFUSING TO STAMP: {msg}. NOTHING WAS WRITTEN.", file=sys.stderr)
            for line in dod_howto():
                print(line, file=sys.stderr)
            return 1
        print(f"  ! WARNING: {msg}   [BLOCKER SHORTLY — fix it now]")
    head = sh("git", "rev-parse", "HEAD")
    # Count BEFORE substituting: `count=1` stops at the first hit and reports n == 1
    # whether there is one gh_sha line or five, so the naive form is blind to a
    # DUPLICATED key while catching a missing one. Zero and two are different failures
    # and neither may write.
    n = len(re.findall(r"^gh_sha:.*$", text, flags=re.M))
    new = re.sub(r"^gh_sha:.*$", f"gh_sha: {head}", text, count=1, flags=re.M)
    if n != 1:
        print(f"BLOCKER: --stamp matched {n} gh_sha lines in {HANDOFF.name}, expected 1. "
              f"NOTHING WAS WRITTEN.\n"
              f"         The frontmatter is missing its `gh_sha:` key (required: "
              f"{', '.join(REQUIRED)}).\n"
              f"         Add the key, then re-run --stamp. Do not commit and assume it "
              f"took -- that is the defect this check exists for.", file=sys.stderr)
        return 1
    HANDOFF.write_text(new)
    print(f"stamped gh_sha: {head}")
    return 0


# --------------------------------------------------------------------------- G-CLAIMS
# wealthTensor-96, from State Machine 1217643242299336.
#
# WHY THIS EXISTS. `-93`'s handoff asserted `wt172 --verify` RC 0. At the exact commit it
# handed over, in a clean worktree, that command returns 2. It was RED WHEN IT WAS HANDED
# OVER GREEN, because `$?` after a pipe is the pipe's: `tool --verify | tail -5` prints the
# success-looking last line AND yields tail's zero. Both signals agree and both are wrong.
# The rule against that was ALREADY in STEP 0 of the very handoff it broke -- a rule stated
# inside a document protects the READER of that document, never its writer. The repair is a
# check, not a better sentence.
#
# WHY IT DOES NOT SCRAPE THE PROSE FOR ITS WORK LIST. `-95` wrote a red-proof coverage check
# that regexed a guard's source for the failure tags it can emit, found NINE of FOURTEEN, and
# printed FULL COVERAGE. A CHECK THAT DISCOVERS ITS OWN SCOPE UNDER-DISCOVERS IT SILENTLY.
# So the handoff DECLARES its claims in a `claims:` registry and this leg holds it to the
# registry; the `phase:` prose is read only in the NEGATIVE direction, to catch a claim the
# registry omits (UNREGISTERED-CLAIM). Same regex, opposite failure mode: an assertion this
# leg cannot parse turns it RED instead of quietly shrinking the work list.
#
# WHY A DISAGREEMENT IS RE-RUN BEFORE IT IS REPORTED. `-95` watched `verify-layout.sh` go red
# once, with a real-looking `manuscript changed since the capture`, while no manuscript had
# been edited -- and it would not reproduce across three further runs, one of them deliberately
# concurrent with a full pytest. A gate that re-runs claims will therefore, on a flaky check,
# MANUFACTURE A FALSE ACCUSATION AGAINST AN HONEST PREDECESSOR, and a gate that cries liar is
# a gate somebody switches off. ONE GREEN AND ONE RED IS A FLAKY CHECK, NOT A CAUGHT LIAR:
# mixed verdicts are reported FLAKY and exit 2 (CANNOT VERIFY), never 1 (BLOCKER). Only a
# claim that disagrees on EVERY attempt is called false.
#
# WHY THE EXIT CODES ARE THIS FILE'S EXISTING THREE. 0 pass, 1 blocker, 2 cannot-verify. A
# flaky check and an un-run slow claim are both unverifiable claims, and this file's oldest
# doctrine is that an unverifiable claim must never be reported as a verified one.

CLAIMS_KEY = "claims"
CLAIM_ATTEMPTS = 3          # one run, then up to two MORE, and only when the first disagrees
CLAIM_TIMEOUT = 3600        # a wedged sweep must fail the leg, not hang the wrap

# Every tag this leg can emit, DECLARED rather than discovered -- `-95`'s repair applied to
# its author's successor. `scripts/redproof_wt178_claims.py` imports this dict and reports
# WEAK for any tag it has no probe for, so a verdict added without a probe goes red BY
# CONSTRUCTION rather than by somebody remembering. Emitting a tag that is not in here is
# itself a failure (UNREGISTERED-TAG), because the emission path is the enforcement point.
CLAIM_TAGS = {
    "OK":                 "re-run, and the observation agreed with the claim",
    "FALSE-CLAIM":        "disagreed on every attempt",
    "FLAKY":              "disagreed and then agreed -- a flaky check, NOT a caught liar",
    "SKIPPED-SLOW":       "declared slow and not run in this mode; un-run is not a pass",
    "MISSING-REGISTRY":   "the phase block asserts results and no `claims:` block declares any",
    "PARSE-REFUSED":      "a line inside `claims:` does not match the declared shape",
    "MISSING-FIELD":      "a claim omits id, cmd or rc, or asserts a count it cannot observe",
    "UNKNOWN-FIELD":      "a claim carries a key this leg does not define",
    "DUPLICATE-ID":       "two claims share an id, so one of them is unreachable",
    "BAD-INT":            "rc or count is not an integer",
    "BAD-BOOL":           "slow is neither true nor false",
    "BAD-COUNT-RE":       "count_re does not compile, or does not capture exactly one group",
    "COUNT-NOT-FOUND":    "count_re matched nothing in the output, so the count is unverifiable",
    "TIMEOUT":            "the command did not finish inside CLAIM_TIMEOUT",
    "PIPED-CLAIM":        "the command contains a pipe, a semicolon or an ampersand",
    "UNREGISTERED-CLAIM": "the phase prose asserts an RC or a count that no claim declares",
    "UNREGISTERED-TAG":   "this leg emitted a tag that is not in CLAIM_TAGS",
}

CLAIM_REQUIRED = ("id", "cmd", "rc")
CLAIM_KNOWN = ("id", "cmd", "rc", "count", "count_re", "slow", "note")

# `a | b` yields b's status, `a; b` yields b's, `a &` yields nothing at all. Each is the -93
# defect with a different operator, so a registered command may contain none of them. `&&`
# and `||` are caught by the `&` and `|` rules and that is deliberate: a compound claim
# should be a script with a name, not a one-liner in a handoff.
CLAIM_FORBIDDEN = (("|", "a pipe"), (";", "a semicolon"), ("&", "an ampersand"))

# The prose conventions this leg READS -- it does not impose them. `phase:` has separated its
# assertions with semicolons since long before this leg existed.
PROSE_RC = re.compile(r"\bRC\s+(\d+)", re.I)
PROSE_COUNT = re.compile(r"\b(\d+)\s+passed\b", re.I)
PROSE_TICK = re.compile(r"`([^`\n]+)`")
# What a ticked span has to look like before this leg will insist it be registered: a script
# or tool name, optionally with one flag. It deliberately does NOT match `git diff a..b -- x`
# or an English phrase in backticks, because an audit that flags prose is an audit somebody
# switches off.
PROSE_CMDISH = re.compile(r"^[A-Za-z_][\w./-]*(?: --?[\w-]+)?$")


def _tag(tag, message):
    """Every problem this leg reports goes through here, so an UNDECLARED tag cannot escape.

    A guard that can emit a verdict its own coverage check has never heard of is precisely the
    9-of-14 defect. Making the emission path the enforcement point means a successor who adds
    a verdict and forgets the registry finds out on the first run, not at review."""
    if tag not in CLAIM_TAGS:
        return ("UNREGISTERED-TAG: %r is not in CLAIM_TAGS -- add it, and add a probe for it "
                "in redproof_wt178_claims.py. Original message: %s" % (tag, message))
    return "%s: %s" % (tag, message)


def frontmatter_block(path=None):
    """The raw text between the two `---` fences. `frontmatter()` returns a flattened dict and
    cannot represent a block, so the claims parser reads the source rather than a lossy view."""
    p = Path(path) if path else HANDOFF
    if not p.exists():
        return ""
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    return m.group(1) if m else ""


def phase_of(fm_text):
    """The `phase:` value out of a GIVEN frontmatter block. claims_static() is handed a path
    and must audit THAT file's prose against THAT file's registry -- reading the phase from
    the repository's real handoff instead would make every probe agree with the wrong
    document, which is exactly the shape of failure a red-proof is supposed to catch."""
    for line in fm_text.split("\n"):
        if re.match(r"^phase:", line):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def parse_claims(fm_text):
    """(claims, problems) from the `claims:` block. REFUSES what it cannot parse.

    The shape is fixed and narrow on purpose -- two spaces and a dash opens a claim, four
    spaces continue it, one key per line, the value running to end of line with optional
    surrounding double quotes:

        claims:
          - id: wt172 --verify
            cmd: python3 scripts/wt172_e2e_paper_ii.py --verify
            rc: 0
            count: 17
            count_re: ([0-9]+) paper-II rows
            slow: false
            note: needs lualatex, so it cannot run in CI

    A LINE THIS PARSER DOES NOT UNDERSTAND IS A PROBLEM, NOT A SKIP. The tempting forgiving
    parser -- ignore what you cannot read and carry on -- would let one typo'd key quietly
    drop a sweep from the work list and still print a clean board. That is the entire family
    of defect this leg was built for, and it is not going to be re-introduced by its parser."""
    claims, problems = [], []
    lines = fm_text.split("\n")
    try:
        start = next(i for i, ln in enumerate(lines) if ln.rstrip() == CLAIMS_KEY + ":")
    except StopIteration:
        return [], []
    cur = None
    for ln in lines[start + 1:]:
        if not ln.strip():
            continue
        if not ln.startswith(" "):          # the next top-level key ends the block
            break
        m = re.match(r"^  - (\w+): ?(.*)$", ln)
        if m:
            if cur is not None:
                claims.append(cur)
            cur = {}
        else:
            m = re.match(r"^    (\w+): ?(.*)$", ln)
            if m is None or cur is None:
                problems.append(_tag("PARSE-REFUSED",
                                     "%r is not `  - key: value` or `    key: value` "
                                     "inside `claims:`" % ln))
                continue
        key, val = m.group(1), m.group(2).strip()
        if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
            val = val[1:-1]
        if key not in CLAIM_KNOWN:
            problems.append(_tag("UNKNOWN-FIELD",
                                 "%r (known: %s)" % (key, ", ".join(CLAIM_KNOWN))))
            continue
        if key in cur:
            problems.append(_tag("PARSE-REFUSED", "%r given twice in one claim" % key))
            continue
        cur[key] = val
    if cur is not None:
        claims.append(cur)

    seen = set()
    for c in claims:
        who = c.get("id") or c.get("cmd") or "(unnamed claim)"
        for f in CLAIM_REQUIRED:
            if f not in c:
                problems.append(_tag("MISSING-FIELD", "%s: no %s" % (who, f)))
        if c.get("id") in seen:
            problems.append(_tag("DUPLICATE-ID", "%r declared twice" % c.get("id")))
        seen.add(c.get("id"))
        for f in ("rc", "count"):
            if f in c:
                try:
                    c[f] = int(str(c[f]).strip())
                except ValueError:
                    problems.append(_tag("BAD-INT", "%s: %s=%r" % (who, f, c[f])))
                    c[f] = None
        if "slow" in c:
            if str(c["slow"]).strip().lower() not in ("true", "false"):
                problems.append(_tag("BAD-BOOL", "%s: slow=%r" % (who, c["slow"])))
                c["slow"] = False
            else:
                c["slow"] = str(c["slow"]).strip().lower() == "true"
        else:
            c["slow"] = False
        c["_rx"] = None
        if "count_re" in c:
            try:
                rx = re.compile(c["count_re"])
            except re.error as e:
                problems.append(_tag("BAD-COUNT-RE", "%s: %r (%s)" % (who, c["count_re"], e)))
                rx = None
            if rx is not None and rx.groups != 1:
                problems.append(_tag("BAD-COUNT-RE",
                                     "%s: %r captures %d group(s), needs exactly 1"
                                     % (who, c["count_re"], rx.groups)))
                rx = None
            c["_rx"] = rx
        if c.get("count") is not None and c["_rx"] is None:
            problems.append(_tag("MISSING-FIELD",
                                 "%s: a count with no usable count_re cannot be observed, so "
                                 "it would be asserted and never checked" % who))
        for bad, human in CLAIM_FORBIDDEN:
            if bad in c.get("cmd", ""):
                problems.append(_tag("PIPED-CLAIM",
                                     "%s: %r contains %s. The exit code of a piped or sequenced "
                                     "command is the LAST one's -- that is the defect this leg "
                                     "exists for, and it may not be re-imported through the "
                                     "registry. Give it a script with a name instead."
                                     % (who, c.get("cmd", ""), human)))
    return claims, problems


def unregistered_claims(phase, claims):
    """Assertions the PROSE makes that the REGISTRY does not carry.

    Two rules, and the first is the one that would have caught `-93`:

      FLOOR -- a `;`-separated segment that asserts an RC or a count must name at least one
      registered claim. A handoff with no registry at all fails here, which is the -93 case
      exactly: the sentence existed, nothing re-ran it.

      SWEEP -- every backticked span in such a segment that LOOKS like a command must map to
      a registered id. That is what catches the list form (`wt133` . `wt148` . ... ALL EIGHT
      RC 0) declaring one of eight and passing the floor.
    """
    problems = []
    ids = [c["id"] for c in claims if c.get("id")]

    def registered(token):
        """EXACT, after collapsing whitespace. A substring matcher looks friendlier and is
        wrong in the permissive direction: the id `declared` would satisfy the prose token
        `undeclared`, and an audit that can be satisfied by a near-miss reports coverage it
        does not have. The refusal message names the exact id to add, so exactness costs the
        writer nothing."""
        t = " ".join(token.split())
        return any(" ".join(i.split()) == t for i in ids)

    for seg in phase.split(";"):
        hits = PROSE_RC.findall(seg) + PROSE_COUNT.findall(seg)
        if not hits:
            continue
        named = [i for i in ids if i in seg]
        if not named:
            snippet = " ".join(seg.split())[:90]
            problems.append(_tag("UNREGISTERED-CLAIM",
                                 "no claim is declared for the assertion in %r.\n"
                                 "      FIX IT: add to the `claims:` block of the frontmatter --\n"
                                 "        - id: <the name the prose uses>\n"
                                 "          cmd: <the un-piped command that produces it>\n"
                                 "          rc: 0" % snippet))
            continue
        for token in [t.strip() for t in PROSE_TICK.findall(seg)]:
            if PROSE_CMDISH.match(token) and not registered(token):
                problems.append(_tag("UNREGISTERED-CLAIM",
                                     "the phase block asserts a result beside `%s` and no claim "
                                     "declares it.\n"
                                     "      FIX IT: add to the `claims:` block --\n"
                                     "        - id: %s\n"
                                     "          cmd: <the un-piped command that produces it>\n"
                                     "          rc: 0" % (token, token)))
    return problems


def claims_static(path=None):
    """The half that costs nothing: registry present, parseable, un-piped, and covering what
    the prose asserts. Wired into --emit, where it must never be UNSATISFIABLE -- a correct
    handoff passes it by DECLARING its claims, which takes twenty seconds and is the point."""
    text = frontmatter_block(path)
    claims, problems = parse_claims(text)
    phase = phase_of(text)
    if not claims:
        if PROSE_RC.search(phase) or PROSE_COUNT.search(phase):
            return [_tag("MISSING-REGISTRY",
                         "the phase block asserts exit codes or counts and the frontmatter "
                         "carries no `claims:` block, so nothing re-runs them. That is how -93 "
                         "handed over a red sweep reported green.")]
        return []
    return problems + unregistered_claims(phase, claims)


def run_claim(c):
    """One attempt. (rc, output).

    `bash -c` with captured output is the UN-PIPED form: the returncode is the command's own,
    not a downstream reader's. This is the one line the whole leg exists to get right, so it
    is written once, here, and never re-derived at a call site."""
    try:
        r = subprocess.run(["bash", "-c", c["cmd"]], cwd=ROOT, capture_output=True,
                           text=True, timeout=CLAIM_TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, ""
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def observe(c):
    """(agrees, why) for ONE attempt, against everything the claim asserts."""
    rc, out = run_claim(c)
    if rc is None:
        return False, _tag("TIMEOUT", "no result after %ds" % CLAIM_TIMEOUT)
    if rc != c["rc"]:
        return False, "RC %d, claimed %d" % (rc, c["rc"])
    if c.get("count") is not None:
        m = c["_rx"].search(out)
        if not m:
            return False, _tag("COUNT-NOT-FOUND", "%r matched nothing" % c["count_re"])
        got = int(m.group(1))
        if got != c["count"]:
            return False, "RC %d ok, count %d, claimed %d" % (rc, got, c["count"])
        return True, "RC %d, count %d" % (rc, got)
    return True, "RC %d" % rc


def claims_leg(run_slow=False, path=None):
    """Re-run what the handoff claims. Returns 0 / 1 / 2 -- this file's existing tri-state."""
    problems = claims_static(path)
    if problems:
        print("G-CLAIMS REFUSED before running anything:")
        for p in problems:
            print("  - %s" % p)
        return 1
    claims, _ = parse_claims(frontmatter_block(path))
    if not claims:
        print("G-CLAIMS: the handoff declares no claims and its phase block asserts none.")
        return 0

    print("G-CLAIMS: %d declared claim(s); %s."
          % (len(claims), "running all" if run_slow
             else "the slow ones are skipped -- use --claims-all"))
    ok, flaky, false_claims, skipped = [], [], [], []
    for c in claims:
        who = c["id"]
        if c["slow"] and not run_slow:
            skipped.append(c)
            print("  %-12s %s%s" % ("SKIPPED-SLOW", who,
                                    "   (%s)" % c["note"] if c.get("note") else ""),
                  flush=True)
            continue
        agrees, why = observe(c)
        if agrees:
            ok.append(c)
            print("  %-12s %s   %s" % ("OK", who, why), flush=True)
            continue
        # THE RE-RUN RULE. A disagreement is a question, not yet an accusation.
        trail, agreed_later = [why], False
        print("  %-12s %s   %s   -- re-running before reporting it"
              % ("DISAGREED", who, why), flush=True)
        for _ in range(CLAIM_ATTEMPTS - 1):
            a2, w2 = observe(c)
            trail.append(w2)
            if a2:
                agreed_later = True
                break
        if agreed_later:
            flaky.append((c, trail))
            print("  %-12s %s   %s" % ("FLAKY", who, " | ".join(trail)), flush=True)
        else:
            false_claims.append((c, trail))
            print("  %-12s %s   %s" % ("FALSE-CLAIM", who, " | ".join(trail)), flush=True)

    print("\nG-CLAIMS: %d agreed, %d FLAKY, %d FALSE, %d skipped as slow."
          % (len(ok), len(flaky), len(false_claims), len(skipped)))
    if false_claims:
        print("BLOCKER: the handoff claims a result its own commands do not produce.")
        for c, trail in false_claims:
            print("  - %s" % _tag("FALSE-CLAIM", "%s: %d attempts, every one disagreed: %s"
                                  % (c["id"], CLAIM_ATTEMPTS, " | ".join(trail))))
        return 1
    if flaky:
        print("CANNOT VERIFY (exit 2): a check disagreed and then agreed. THAT IS A FLAKY")
        print("  CHECK, NOT A CAUGHT LIAR -- do not report the predecessor as wrong. Name the")
        print("  flake in a drift flag, and if you can, make it print what it compared.")
        for c, trail in flaky:
            print("  - %s" % _tag("FLAKY", "%s: %s" % (c["id"], " | ".join(trail))))
        return 2
    if skipped:
        print("CANNOT VERIFY (exit 2): %d slow claim(s) were not re-run, and an un-run claim is"
              % len(skipped))
        print("  not a verified one. Run --claims-all before you hand this over.")
        return 2
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--check"
    sys.exit({"--check": check, "--emit": emit, "--stamp": stamp,
              "--claims": lambda: claims_leg(run_slow=False),
              "--claims-all": lambda: claims_leg(run_slow=True),
              "--coach": lambda: coach()[0],
              "--coach-refresh": lambda: coach(write_baseline=True)[0]}.get(arg, check)())
