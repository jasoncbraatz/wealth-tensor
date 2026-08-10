"""Is the dual-tensor recursion CPU-shaped? Measure it, don't opine (L16).

Differentiable port of wealth_tensor.lag.LayeredFirm, batched over firms, correction
mechanism disabled (the filter-isolated case -- the threshold snap is non-differentiable
and would need a soft relaxation anyway).

    E[t+1] = E[t] * (1 - DELTA)
    C[t+1] = C[t] + phi*dE + alpha*gap[t]
    gap[t] = E[t] - C[t]

NOTATION (corrected 2026-08-10 after an audit caught a symbol collision -- the THIRD instance
of this failure mode in the project; see WT-049 and WT-055):

    d      ENTROPY RATE      -- lag.py's `entropy_rate`
    m      maintenance ratio -- lag.py's `maintenance_ratio`
    DELTA  EFFECTIVE DECAY   -- delta = d*(1 - m); THIS is what drives the recursion

An earlier version of this file called the effective decay `d`, and the paper inherited it,
understating the divisor in the phi recovery by a factor (1-m) = 0.4 -- in the FLATTERING
direction. Everything here is in DELTA.

Fit targets: phi (observability), alpha (recognition rate), DELTA (effective decay).

SYNTHETIC DATA ONLY -- see the note at the bottom of this file. This must not touch EDGAR.
"""
import time

import torch

STEPS = 400


def simulate(phi, alpha, delta, steps=STEPS, e0=100.0):
    """Batched forward recursion. phi/alpha/delta are (B,) tensors. Returns C, (B, steps+1)."""
    B = phi.shape[0]
    E = torch.full((B,), e0, dtype=phi.dtype)
    C = torch.full((B,), e0, dtype=phi.dtype)
    out = [C]
    for _ in range(steps):
        E_next = E * (1.0 - delta)
        dE = E_next - E
        C = C + phi * dE + alpha * (E - C)
        E = E_next
        out.append(C)
    return torch.stack(out, dim=1)


def timeit(fn, reps=3):
    fn()                                   # warm up
    t0 = time.perf_counter()
    for _ in range(reps):
        fn()
    return (time.perf_counter() - t0) / reps


def params(B, dtype, grad=False):
    return (torch.full((B,), 0.30, dtype=dtype, requires_grad=grad),
            torch.full((B,), 0.05, dtype=dtype, requires_grad=grad),
            torch.full((B,), 0.02, dtype=dtype, requires_grad=grad))


print("=" * 72)
print("A. FORWARD + BACKWARD, %d sequential steps, batched over firms" % STEPS)
print("=" * 72)
print("%10s %10s %14s %16s" % ("firms", "dtype", "forward", "fwd+backward"))
for dtype in (torch.float32, torch.float64):
    for B in (1, 100, 10_000, 100_000):
        p, a, dl = params(B, dtype)
        t_f = timeit(lambda: simulate(p, a, dl))

        pg, ag, dg = params(B, dtype, grad=True)

        def fwd_bwd():
            loss = simulate(pg, ag, dg).pow(2).mean()
            loss.backward()
            for t in (pg, ag, dg):
                t.grad = None

        t_fb = timeit(fwd_bwd)
        print("%10s %10s %12.1f ms %14.1f ms"
              % (f"{B:,}", str(dtype).replace("torch.", ""), t_f * 1e3, t_fb * 1e3))

print()
print("=" * 72)
print("B. A REAL FIT -- recover known parameters from synthetic observations")
print("=" * 72)

torch.manual_seed(0)
B = 10_000                                  # ~ the size of a full EDGAR firm panel
DT = torch.float64                          # the precision the closed-form work uses

true_phi = torch.rand(B, dtype=DT) * 0.8 + 0.1
true_alpha = torch.rand(B, dtype=DT) * 0.08 + 0.02
true_delta = torch.rand(B, dtype=DT) * 0.03 + 0.005   # EFFECTIVE decay
observed = simulate(true_phi, true_alpha, true_delta)
observed = observed + torch.randn_like(observed) * 0.05      # measurement noise

phi = torch.full((B,), 0.5, dtype=DT, requires_grad=True)
alpha = torch.full((B,), 0.05, dtype=DT, requires_grad=True)
delta = torch.full((B,), 0.02, dtype=DT, requires_grad=True)
opt = torch.optim.Adam([phi, alpha, delta], lr=0.02)

ITERS = 300
t0 = time.perf_counter()
for i in range(ITERS):
    opt.zero_grad()
    loss = (simulate(phi, alpha, delta) - observed).pow(2).mean()
    loss.backward()
    opt.step()
    with torch.no_grad():
        phi.clamp_(0.0, 1.0)
        alpha.clamp_(1e-4, 1.0)
        delta.clamp_(1e-5, 0.5)
wall = time.perf_counter() - t0

with torch.no_grad():
    err_phi = (phi - true_phi).abs()
    err_alpha = (alpha - true_alpha).abs()
    err_delta = (delta - true_delta).abs()

print("firms fitted simultaneously : %s" % f"{B:,}")
print("gradient steps              : %d" % ITERS)
print("precision                   : float64")
print("WALL CLOCK                  : %.1f s   (%.1f ms per gradient step)"
      % (wall, wall / ITERS * 1e3))
print("final loss                  : %.3e" % loss.item())
print("phi   recovery: median abs err %.5f   p90 %.5f" % (err_phi.median(), err_phi.quantile(0.9)))
print("alpha recovery: median abs err %.5f   p90 %.5f" % (err_alpha.median(), err_alpha.quantile(0.9)))
print("DELTA recovery: median abs err %.5f   p90 %.5f" % (err_delta.median(), err_delta.quantile(0.9)))
print()
print("Per-firm cost: %.3f ms for the whole %d-step fit."
      % (wall / B * 1e3, ITERS))
