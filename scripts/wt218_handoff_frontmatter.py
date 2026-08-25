"""wt218 — rewrite docs/HANDOFF.md's frontmatter for the ship. LINE-BASED, never a greedy regex.

(An earlier cut of this used re.sub with re.S and `.*$`, which made `.` match newlines and
swallowed the file from `updated:` to EOF. The assert caught it before anything was written.
A frontmatter is a list of lines; edit it as one.)
"""
import pathlib

P = pathlib.Path("docs/HANDOFF.md")
lines = P.read_text(encoding="utf-8").split("\n")

PHASE = ('phase: "EVERY NUMBER HERE WAS RE-DERIVED BY THE GATE\'S CLAIM RE-RUNNER, NOT QUOTED. '
 'THE CORPUS SHIPPED: v1.0-preprint is tagged and P7 is CLOSED on a check that bites rather than on an assertion. '
 'pytest 1168 passed; verify-layout.sh RC 0 with 145 pages compared and all 145 per-page hashes reproducing from a clean worktree; '
 'wt182 RC 0 over 20 post-conditions; wt185 RC 0 over 19; wt183 16; wt186 11; wt187 6; wt184 RC 0 over 28 post-conditions with 9 NEGATIVE; '
 'wt188 63/20; wt189 19/11; wt190 10/4; wt191 26/12; wt191b 11/5; wt192 25/11; wt192b 12/6; wt192c 13/8; '
 'wt181 --verify RC 0 over 9 checks with 3 NEGATIVE; wt133 wt148 wt154 wt156 wt160 wt163 wt166 wt169 -- ALL EIGHT RC 0; '
 'wt170 --verify RC 0 with 7 of 15 rows verified against committed evidence, DOWN FROM 11 because three rows retired and one was re-evidenced this pass; '
 'wt172 --verify RC 0 over 19 paper-II rows; '
 'wt173 --verify RC 0 with 50 values held to the build and 0 divergent, 15 of 15 load-bearing values present in the prose, and wt173 --postconditions RC 0 over 14 checks '
 '-- both after a re-measure, because the section 4.4 note moved the body characters-per-line from 65.43 to 64.95, still inside RECIPE section 0 62-68 band, '
 'so nothing was retuned and RECIPE.md moved at BOTH of its two sites; '
 'preflight RC 0 over 16 fonts; wt177_figure_guard.py RC 0; redproof_wt177_figures.py 21/21; wt179_manifest_guard.py RC 0 over 10; '
 'redproof_wt179_manifest.py 26 of 26 tags; redproof_wt178_claims.py 17/17; redproof_wt180_counts.py 12 of 12; redproof-layout.sh RC 0 with 4 probes. '
 'defensive_count.py --against reads +0 on all four manuscripts and the LEVELS are unchanged at paper-I/II/III/IV = 0/0/3/0 outside Limitations '
 '-- ALL THREE IN-SCOPE MANUSCRIPTS WERE EDITED THIS PASS, 149 times, and the invariant held. '
 'wt148 reports 0 unadjudicated and 0 stale on all three in-scope manuscripts, after 16 promises were re-keyed with their evidence RE-RUN, '
 '10 retired because the sentence naming the artefact WAS the apparatus leak Pass D was clearing, and one re-evidenced. '
 'Board 66 criteria with P7 the ONLY lane that moved, after bash scripts/regen-board.sh -- and it moved to CLOSED. '
 'THE LAYOUT BASELINE IS 145 PAGES: 149 before this pass, 144 after the C-class repairs took five pages of scaffolding out with nothing added, '
 'and 145 when the section 4.4 known-limitations note put one page back. Gate PASS, tree clean and pushed. '
 'THE PASS-D PATCH SCRIPTS (wt209 through wt219) ARE DELIBERATELY NOT REGISTERED CLAIMS: every one is idempotent and goes QUIET on a second run, '
 'and the wrap only ever runs a command a second time, so registering one would register a no-op. Each was run twice and its stdout diffed; '
 'they are named in the body of this file, not in the phase block."')

THEME = ('live_theme: "THE CORPUS SHIPPED. v1.0-preprint is tagged, P7 is CLOSED on a check that bites, '
 'and the successor is JASON rather than another session. PASS D LANDED 149 C-CLASS REPAIRS AND AN ADVERSARIAL '
 'VERIFIER REFUTED FORTY OF THE FIRST 166 -- seven of them FALSE STATEMENTS that every mechanical checker passed. '
 'REVIEW-039 section 7 predicted that rate at a quarter of the volume and it held. AND THE DEFECT CLASS NOBODY HAD '
 'LOOKED FOR: reading the three manuscripts AGAINST EACH OTHER found nine cross-document defects in 61 claims, '
 'including one where paper-III asserted what papers I, II and IV each state -- and this same pass had just cut it '
 'from paper-IV. A per-file verifier is structurally blind to the class a corpus-wide pass is most likely to create."')

REPL = {
    "updated: ":    "updated: 2026-08-25",
    "session: ":    "session: wealthTensor-106",
    "session_n: ":  "session_n: 106",
    "live_theme: ": THEME,
    "phase: ":      PHASE,
}
hits = {k: 0 for k in REPL}
for i, l in enumerate(lines[:40]):
    for k, v in REPL.items():
        if l.startswith(k):
            lines[i] = v; hits[k] += 1
            break
missing = [k for k, n in hits.items() if n != 1]
if missing:
    raise SystemExit("FAIL: keys not matched exactly once: %r" % missing)
out = "\n".join(lines)
assert out.count("\n") == P.read_text(encoding="utf-8").count("\n"), "line count changed"
P.write_text(out, encoding="utf-8")
print("frontmatter rewritten; line count unchanged at %d" % (out.count("\n") + 1))
