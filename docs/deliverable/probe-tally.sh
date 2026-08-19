# docs/deliverable/probe-tally.sh
# =========================================================================================
# THE PROBE TALLY — a count that is DERIVED, and cheap enough to red-proof.
#
# wealthTensor-98. `redproof-layout.sh` runs four probes and used to print no number at all,
# so the handoff could hold it to an exit code and nothing else. An exit code is the weakest
# half of a claim: it stays 0 while a probe quietly stops being called, which is the same
# shape as `-96` shipping `pytest` 1121 for a suite of 1148 with a green RC every time.
#
# WHY THIS IS ITS OWN FILE AND NOT FOUR LINES INSIDE THE SCRIPT. The script it serves needs
# four full lualatex builds — five to eight minutes — so a red-proof that had to RUN it to
# see whether its count moves would be a red-proof nobody runs. Sourced, the tally can be
# driven with three verdicts, or seven, or none, in milliseconds, and the number it prints
# has to follow. `scripts/redproof_wt180_counts.py` does exactly that, and then runs the
# real script with its probe body stubbed out to prove the WIRING as well as the mechanism.
#
# WHAT IT DOES NOT DO. It counts VERDICTS REPORTED, not probes intended. There is deliberately
# no declared total to compare against: a total written down here would be a constant printed
# back at its reader, and a value you passed in is not a value you measured (`-92`).
# A probe that dies before reporting therefore LOWERS the number — which is the point.
# =========================================================================================

tally_reset() { TALLY=0; }

tally_bump() { TALLY=$(( ${TALLY:-0} + 1 )); }

# tally_line <name> — print the one stable line the handoff's `claims:` registry reads.
# Refuses on zero: a tally that counted nothing must not print a tidy "0 probes reported"
# for a `count_re` to match, because a check that reports having verified nothing, in the
# same shape as a check that verified everything, is worse than no line at all.
tally_line() {
  local who="${1:?tally_line needs the name to print}"
  if [ "${TALLY:-0}" -eq 0 ]; then
    echo "$who: NO PROBES REPORTED — the tally never counted a verdict, so this run is held to nothing." >&2
    return 1
  fi
  echo "$who: ${TALLY} probes reported"
}
