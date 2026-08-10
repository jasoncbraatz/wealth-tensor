"""Why did phi recovery fail? Conditioning, or optimisation?

Algebra first. Substituting dE = -d*E[t] into the recursion:

    C[t+1] = C[t]*(1 - alpha) + E[t]*(alpha - phi*d),   E[t] = E0*(1-d)^t

So the OBSERVED series C depends on phi ONLY through the composite k = (alpha - phi*d).
Three free quantities are visible in C: alpha, d, and k. phi is then recovered as

    phi = (alpha - k) / d

-- a division by d. If d is small the estimator's variance blows up like 1/d^2. That is a
STRUCTURAL identifiability statement about the model, not a failure of Adam.

Three checks, each isolating one explanation. Synthetic data only.
"""
import time

import torch

STEPS, DT, E0 = 400, torch.float64, 100.0


def simulate(phi, alpha, d, steps=STEPS):
    B = phi.shape[0]
    E = torch.full((B,), E0, dtype=phi.dtype)
    C = torch.full((B,), E0, dtype=phi.dtype)
    out = [C]
    for _ in range(steps):
        E_next = E * (1.0 - d)
        C = C + phi * (E_next - E) + alpha * (E - C)
        E = E_next
        out.append(C)
    return torch.stack(out, dim=1)


def fit(observed, true_d=None, iters=400, B=None, noise_free=False):
    """Fit phi/alpha (and d unless true_d is pinned). Returns fitted phi."""
    phi = torch.full((B,), 0.5, dtype=DT, requires_grad=True)
    alpha = torch.full((B,), 0.05, dtype=DT, requires_grad=True)
    ps = [phi, alpha]
    if true_d is None:
        d = torch.full((B,), 0.02, dtype=DT, requires_grad=True)
        ps.append(d)
    else:
        d = true_d
    opt = torch.optim.Adam(ps, lr=0.02)
    for _ in range(iters):
        opt.zero_grad()
        (simulate(phi, alpha, d) - observed).pow(2).mean().backward()
        opt.step()
        with torch.no_grad():
            phi.clamp_(0.0, 1.0)
            alpha.clamp_(1e-4, 1.0)
            if true_d is None:
                d.clamp_(1e-5, 0.5)
    return phi.detach()


torch.manual_seed(0)
B = 2000
true_phi = torch.rand(B, dtype=DT) * 0.8 + 0.1
true_alpha = torch.rand(B, dtype=DT) * 0.08 + 0.02
true_d = torch.rand(B, dtype=DT) * 0.03 + 0.005
clean = simulate(true_phi, true_alpha, true_d)
noisy = clean + torch.randn_like(clean) * 0.05

print("=" * 74)
print("CHECK 1 -- is it the NOISE?  Fit the noise-free series.")
print("=" * 74)
e = (fit(clean, B=B) - true_phi).abs()
print("  phi median abs err: %.5f   p90 %.5f" % (e.median(), e.quantile(0.9)))

print()
print("=" * 74)
print("CHECK 2 -- is it the CONFOUND with d?  Pin d at its true value, fit phi+alpha only.")
print("=" * 74)
e2 = (fit(noisy, true_d=true_d, B=B) - true_phi).abs()
print("  phi median abs err: %.5f   p90 %.5f" % (e2.median(), e2.quantile(0.9)))

print()
print("=" * 74)
print("CHECK 3 -- does the error scale like 1/d, as the algebra predicts?")
print("=" * 74)
print("  Fit noisy data with d free, then bucket the error by the firm's TRUE decay rate.")
fitted = fit(noisy, B=B)
err = (fitted - true_phi).abs()
print("  %14s %8s %16s %16s" % ("true d range", "n", "median |err phi|", "x vs slowest"))
edges = [0.005, 0.010, 0.017, 0.025, 0.035]
base = None
for lo, hi in zip(edges, edges[1:]):
    m = (true_d >= lo) & (true_d < hi)
    if m.sum() < 10:
        continue
    med = err[m].median().item()
    base = med if base is None else base
    print("  %6.3f-%-7.3f %8d %16.5f %15.2fx" % (lo, hi, m.sum(), med, base / med))

print()
print("  For reference, the sector sketches in the paper:")
print("    warehouse retail d=0.01 | industrial d=0.05 | software d=0.20")
print("  Same experiment at those three decay rates, d pinned to true (best case):")
for d_val in (0.01, 0.05, 0.20):
    n = 600
    tp = torch.rand(n, dtype=DT) * 0.8 + 0.1
    ta = torch.rand(n, dtype=DT) * 0.08 + 0.02
    td = torch.full((n,), d_val, dtype=DT)
    obs = simulate(tp, ta, td) + torch.randn(n, STEPS + 1, dtype=DT) * 0.05
    e3 = (fit(obs, true_d=td, B=n, iters=400) - tp).abs()
    print("    d=%.2f  ->  phi median abs err %.5f   p90 %.5f" % (d_val, e3.median(), e3.quantile(0.9)))
