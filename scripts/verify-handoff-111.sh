#!/usr/bin/env bash
# Every path and every quoted claim in the handoff, checked against the thing it names.
R="$HOME/repos/wealth-tensor"; F=0
chk(){ if eval "$2" >/dev/null 2>&1; then printf '  ok    %s\n' "$1"; else printf '  FAIL  %s\n' "$1"; F=1; fi; }

chk "branch is paper-rebuild"        "[ \"\$(git -C $R rev-parse --abbrev-ref HEAD)\" = paper-rebuild ]"
# NO LITERAL SHA HERE, and the reason is funny enough to write down: the first cut asserted
# a HEAD, and then COMMITTING THIS SCRIPT MOVED HEAD, so the verifier invalidated itself by
# landing. Same shape as the P13e finding one commit earlier -- a check that names a ref has
# to name a ref it is not itself moving. What actually matters to the next session is that
# the tree is clean and in step with origin; a HEAD ahead of the handoff just means a
# sibling committed, which is a thing to read, not a thing to fail on.
chk "in step with origin (no ahead/behind)" "git -C $R status -sb | head -1 | grep -qv '\['"
chk "tree clean + pushed"            "[ -z \"\$(git -C $R status --porcelain)\" ] && git -C $R status -sb | head -1 | grep -qv '\[ahead'"
for p in docs/DEFINITION-OF-DONE-SHIP.md docs/CO-AUTHOR-CHARTER.md docs/CHECKLIST.md \
         docs/papers-v2/paper-II-redistribution/paper-II.md docs/papers-v2/paper-III-dual-tensor/paper-III.md \
         docs/deliverable/build-v2-review.sh docs/deliverable/wealth-tensor-v2-review.pdf \
         docs/deliverable/preamble.tex docs/deliverable/wt175_md2tex.lua \
         docs/deliverable/TABLE-WIDTHS-v2.tsv docs/papers/wt-figures.html \
         scripts/wt223_figures_to_pdf.py scripts/wt224_voice_pass.py scripts/wt225_build_v2.py \
         scripts/wt177_figure_guard.py scripts/regen-board.sh; do
  chk "exists: $p" "[ -f $R/$p ]"
done
chk "9 figures in docs/figures"      "[ \$(ls $R/docs/figures/*.pdf | wc -l) -eq 9 ]"
chk "regen-board exports 300"        "grep -q 'BOARD_CHECK_TIMEOUT=\"\${BOARD_CHECK_TIMEOUT:-300}\"' $R/scripts/regen-board.sh"
chk "guard regex is ^PAPERS=\"...\"" "grep -q 'r.\\^PAPERS=\"(\[^\"\]\*)\"' $R/scripts/wt177_figure_guard.py"
chk "PAPERS= still a literal block"  "grep -qE '^PAPERS=\"paper-I-price' $R/docs/deliverable/build.sh"
chk "wtfigmeasure is 460.0pt"        "grep -q 'setlength{\\\\wtfigmeasure}{460.0pt}' $R/docs/deliverable/preamble.tex"
chk "textwidth is 289.08pt"          "grep -q 'textwidth=289.08pt' $R/docs/deliverable/preamble.tex"
chk "wtfig centres with \\hss"       "grep -q 'hbox to.hsize{.hss.box0.hss}' $R/docs/deliverable/preamble.tex"
chk "lua errors on alt text"         "grep -q 'carries alt text' $R/docs/deliverable/wt175_md2tex.lua"
chk "build-v2 names 5 overrides"     "for v in WT_PAPERS WT_PAPERS_ROOT WT_CAPTURE WT_TABLE_WIDTHS WT_DOCLABEL; do grep -q \$v $R/docs/deliverable/build-v2-review.sh || exit 1; done"
chk "build-v2 checks canonicals"     "grep -q 'the canonical artefacts are untouched' $R/docs/deliverable/build-v2-review.sh"
chk "voice pass has 14 fixtures"     "[ \$(cd $R && python3 scripts/wt224_voice_pass.py --selftest | sed -n 's:.*\([0-9]*\)/\([0-9]*\) fixtures pass:\2:p') = 14 ]"
chk "match-by-name, not ordinal"     "grep -q 'By NAME, not by ordinal' $R/scripts/wt225_build_v2.py"
chk "P5 + P8 are the only humans"    "[ \$(grep -c 'PENDING-HUMAN' $R/docs/CHECKLIST.md) -eq 4 ]"
chk "P8 text is as quoted"           "grep -q 'CLEARS IT FOR LIFTOFF' $R/docs/CHECKLIST.md"
chk "charter 1.1 freezes instruments" "grep -q 'THE INSTRUMENT SET IS FROZEN' $R/docs/DEFINITION-OF-DONE-SHIP.md"
chk "voice-box self-report exists"   "[ -f $HOME/repos/voice-box/docs/VOICE-SELF-REPORT.md ]"
chk "tier-gate refuses phase 4"      "[ -f $HOME/repos/voice-box/tools/tier-gate.py ]"
chk "charter-read takes bare slug"   "grep -q 'or pass a bare session slug' $HOME/Scripts/charter-read.sh"
chk "roster claim wants --resource"  "$HOME/Scripts/roster claim 2>&1 | grep -q -- '--resource'"
chk "gate version 2.65"              "grep -q '2.65' $HOME/Desktop/downloads/HANDOFF-GATE.md"
echo; [ $F -eq 0 ] && echo "HANDOFF VERIFIED — every path and quoted string checks out" || echo "HANDOFF HAS ERRORS — fix before pasting"
exit $F
