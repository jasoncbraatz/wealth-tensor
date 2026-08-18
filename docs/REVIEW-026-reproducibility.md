---
review: REVIEW-026
title: "The sixteen rows nobody could falsify — and what the rule caught beyond them"
session: wealthTensor-86
opened: 2026-08-18
instrument: scripts/wt156_reproducibility_sweep.py
before_rev: b50bccd
# ---------------------------------------------------------------------------------
# THE PREDICTION IS COMMITTED BEFORE THE SWEEP IS RUN.
# wealthTensor-84 established the rule: a count written down after the fact is an
# argument, not a measurement. The predicted numbers below were reasoned out from the
# evidence vocabulary (the 90 distinct `evidence` strings across the 129 rows) and from
# the detector definitions, and committed in this state. The measured numbers replace
# PENDING in a later commit, and this file records both whether or not they agree.
# ---------------------------------------------------------------------------------
predicted_D1_record_in_a_vanished_session: 35
predicted_D2_no_operand: 8
predicted_total_flagged: 43
predicted_beyond_the_sixteen: 27
measured_D1_record_in_a_vanished_session: PENDING
measured_D2_no_operand: PENDING
measured_total_flagged: PENDING
measured_beyond_the_sixteen: PENDING
sixteen_agreed_with_their_old_note: PENDING
sixteen_disagreed_with_their_old_note: PENDING
falsifiers:
  - "Run `python3 scripts/wt156_reproducibility_sweep.py --rev b50bccd --json` and count `n_d1`
     and `n_d2`. If they are not the measured numbers below, this review is wrong."
  - "Run `python3 scripts/wt156_reproducibility_sweep.py` at HEAD. If it does not return 0, the
     repair claimed here did not land."
  - "Take any of the sixteen promise_ids listed in §3, run the command its repaired `evidence`
     column now names, and compare against the value its `note` now records. If they differ, the
     row is FALSE and this review's agreement count is wrong."
  - "The detectors read the `evidence` column only. If you believe the `artefact` column should
     rescue a row, re-run with that change and say how the count moves — §2 argues it should not,
     and that argument is the thing to attack."
---

# REVIEW-026 — the reproducibility sweep

*(in progress — wealthTensor-86)*
