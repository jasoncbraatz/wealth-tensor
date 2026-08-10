"""Is the dual-tensor recursion CPU-shaped? Measure it, don't opine (L16).

Differentiable port of wealth_tensor.lag.LayeredFirm, batched over firms, correction
mechanism disabled (the filter-isolated case -- the threshold snap is non-differentiable
and would need a soft relaxation anyway).

    E[t+1] = E[t] * (1 - d)
    C[t+1] = C[t] + phi*dE + alpha*gap[t]
    gap[t] = E[t] - C[t]

Fit targets: phi (observability), alpha (recognition rate), d (effective decay).

SYNTHETIC DATA ONLY -- see the note at the bottom of this file. This must not touch EDGAR.
"""
import time

import torch

STEPS = 400


def simulate(phi, alpha, d, steps=STEPS, e0=100.0):
    """Batched forward recursion. phi/alpha/d are (B,) tensors. Returns C, (B, steps+1)."""
    B = phi.shape[0]
    E = torch.full((B,), e0, dtype=phi.dtype)
    C = torch.full((B,), e0, dtype=phi.dtype)
    out = [C]
    for _ in range(steps):
        E_next = E * (1.0 - d)
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
        p, a, dd = params(B, dtype)
        t_f = timeit(lambda: simulate(p, a, dd))

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
true_d = torch.rand(B, dtype=DT) * 0.03 + 0.005
observed = simulate(true_phi, true_alpha, true_d)
observed = observed + torch.randn_like(observed) * 0.05      # measurement noise

phi = torch.full((B,), 0.5, dtype=DT, requires_grad=True)
alpha = torch.full((B,), 0.05, dtype=DT, requires_grad=True)
d = torch.full((B,), 0.02, dtype=DT, requires_grad=True)
opt = torch.optim.Adam([phi, alpha, d], lr=0.02)

ITERS = 300
t0 = time.perf_counter()
for i in range(ITERS):
    opt.zero_grad()
    loss = (simulate(phi, alpha, d) - observed).pow(2).mean()
    loss.backward()
    opt.step()
    with torch.no_grad():
        phi.clamp_(0.0, 1.0)
        alpha.clamp_(1e-4, 1.0)
        d.clamp_(1e-5, 0.5)
wall = time.perf_counter() - t0

with torch.no_grad():
    err_phi = (phi - true_phi).abs()
    err_alpha = (alpha - true_alpha).abs()
    err_d = (d - true_d).abs()

print("firms fitted simultaneously : %s" % f"{B:,}")
print("gradient steps              : %d" % ITERS)
print("precision                   : float64")
print("WALL CLOCK                  : %.1f s   (%.1f ms per gradient step)"
      % (wall, wall / ITERS * 1e3))
print("final loss                  : %.3e" % loss.item())
print("phi   recovery: median abs err %.5f   p90 %.5f" % (err_phi.median(), err_phi.quantile(0.9)))
print("alpha recovery: median abs err %.5f   p90 %.5f" % (err_alpha.median(), err_alpha.quantile(0.9)))
print("d     recovery: median abs err %.5f   p90 %.5f" % (err_d.median(), err_d.quantile(0.9)))
print()
print("Per-firm cost: %.3f ms for the whole %d-step fit."
      % (wall / B * 1e3, ITERS))
