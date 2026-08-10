"""Why does fitting phi fail? Conditioning, or optimisation?

NOTATION -- corrected 2026-08-10 after an audit caught a symbol collision, which is the THIRD
instance of this failure mode in the project (WT-049: a model parameter and a measurable sharing
a name; WT-055: Lambda vs lambda; this).

    d      ENTROPY RATE          -- lag.py's `entropy_rate`, paper section 4.1
    m      maintenance ratio     -- lag.py's `maintenance_ratio`
    DELTA  EFFECTIVE DECAY       -- delta = d*(1 - m); THIS is what drives the recursion

    E[t+1] = E[t] * (1 - DELTA)

An earlier version of this file called the effective decay `d`, and the paper inherited the
error -- which understated the divisor in the phi recovery by a factor (1-m) = 0.4, i.e. in the
FLATTERING direction. Everything below is in DELTA. Where sector sketches from the paper's
section 4.2 are used, their entropy rates 0.01/0.05/0.20 are converted at m = 0.6 to effective
decays 0.004/0.02/0.08.

THE ALGEBra. Substituting dE = -DELTA*E[t] into the two recursions:

    C[t+1] = C[t]*(1 - alpha) + E[t]*(alpha - phi*DELTA),   E[t] = E0*(1-DELTA)^t

So phi reaches the observed series ONLY through the product phi*DELTA. The data identify alpha
(from the (1-alpha) coefficient), DELTA (from the geometric rate of the driving term), and the
composite k = alpha - phi*DELTA. Then phi = (alpha - k)/DELTA -- a division by DELTA, so the
estimator's variance grows like 1/DELTA^2 as DELTA -> 0.

This is a CONDITIONING statement, not a non-identifiability one: phi remains identifiable in
principle at every DELTA > 0, and recovery degrades continuously as DELTA falls.

Synthetic data only. See scripts/prototypes/README.md for the WT-052 declaration.
"""
import torch

STEPS, DT, E0 = 400, torch.float64, 100.0
M = 0.6                                   # maintenance ratio, lag.py default


def simulate(phi, alpha, delta, steps=STEPS):
    B = phi.shape[0]
    E = torch.full((B,), E0, dtype=phi.dtype)
    C = torch.full((B,), E0, dtype=phi.dtype)
    out = [C]
    for _ in range(steps):
        E_next = E * (1.0 - delta)
        C = C + phi * (E_next - E) + alpha * (E - C)
        E = E_next
        out.append(C)
    return torch.stack(out, dim=1)


def fit(observed, B, true_delta=None, iters=400):
    phi = torch.full((B,), 0.5, dtype=DT, requires_grad=True)
    alpha = torch.full((B,), 0.05, dtype=DT, requires_grad=True)
    ps = [phi, alpha]
    if true_delta is None:
        delta = torch.full((B,), 0.02, dtype=DT, requires_grad=True)
        ps.append(delta)
    else:
        delta = true_delta
    opt = torch.optim.Adam(ps, lr=0.02)
    for _ in range(iters):
        opt.zero_grad()
        (simulate(phi, alpha, delta) - observed).pow(2).mean().backward()
        opt.step()
        with torch.no_grad():
            phi.clamp_(0.0, 1.0)
            alpha.clamp_(1e-4, 1.0)
            if true_delta is None:
                delta.clamp_(1e-5, 0.5)
    return phi.detach()


def report(label, err):
    print("  %-46s median %.5f   p90 %.5f" % (label, err.median(), err.quantile(0.9)))


torch.manual_seed(0)
B = 2000
true_phi = torch.rand(B, dtype=DT) * 0.8 + 0.1          # phi in [0.1, 0.9]
true_alpha = torch.rand(B, dtype=DT) * 0.08 + 0.02
true_delta = torch.rand(B, dtype=DT) * 0.03 + 0.005     # EFFECTIVE decay in [0.005, 0.035]
clean = simulate(true_phi, true_alpha, true_delta)
noisy = clean + torch.randn_like(clean) * 0.05

print("Synthetic ranges: phi [0.10, 0.90] | alpha [0.02, 0.10] | DELTA [0.005, 0.035]")
print("(For scale: the paper's section 4.2 sector sketches convert to DELTA 0.004 / 0.02 / 0.08.)")
print()
print("=" * 78)
print("LIKE-FOR-LIKE PAIR -- identical batch, identical iteration budget")
print("=" * 78)
e_free = (fit(noisy, B=B) - true_phi).abs()
e_pin = (fit(noisy, B=B, true_delta=true_delta) - true_phi).abs()
report("DELTA free (the reported layer alone)", e_free)
report("DELTA pinned at truth", e_pin)
print("  improvement in the median: %.0fx" % (e_free.median() / e_pin.median()))
print()
print("=" * 78)
print("IS IT THE NOISE?  Fit the noise-free series, DELTA free.")
print("=" * 78)
report("noise-free, DELTA free", (fit(clean, B=B) - true_phi).abs())
print("  -> no better than the noisy fit, so noise is not the explanation.")
print()
print("=" * 78)
print("DOES RECOVERY DEGRADE CONTINUOUSLY AS DELTA FALLS?  (DELTA free)")
print("=" * 78)
print("  %18s %7s %12s %12s" % ("true DELTA range", "n", "median", "p90"))
edges = [0.005, 0.010, 0.017, 0.025, 0.035]
for lo, hi in zip(edges, edges[1:]):
    msk = (true_delta >= lo) & (true_delta < hi)
    if msk.sum() < 10:
        continue
    print("  %8.3f-%-8.3f %7d %12.5f %12.5f"
          % (lo, hi, msk.sum(), e_free[msk].median(), e_free[msk].quantile(0.9)))
print("  -> continuous degradation, NOT a cliff. phi stays identifiable in principle;")
print("     the estimator simply becomes useless as DELTA -> 0.")
print()
print("=" * 78)
print("AT THE PAPER'S OWN SECTOR SKETCHES (section 4.2), DELTA pinned -- best case")
print("=" * 78)
print("  %-34s %12s %12s" % ("sector (entropy rate -> DELTA)", "median", "p90"))
for d_ent, name in ((0.01, "warehouse retail"), (0.05, "industrial"), (0.20, "software")):
    delta_val = d_ent * (1.0 - M)
    n = 600
    tp = torch.rand(n, dtype=DT) * 0.8 + 0.1
    ta = torch.rand(n, dtype=DT) * 0.08 + 0.02
    td = torch.full((n,), delta_val, dtype=DT)
    obs = simulate(tp, ta, td) + torch.randn(n, STEPS + 1, dtype=DT) * 0.05
    e = (fit(obs, B=n, true_delta=td) - tp).abs()
    print("  %-34s %12.5f %12.5f"
          % ("%s (d=%.2f -> %.3f)" % (name, d_ent, delta_val), e.median(), e.quantile(0.9)))
