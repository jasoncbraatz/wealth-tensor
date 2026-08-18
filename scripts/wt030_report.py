import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
import numpy as np
from wealth_tensor.redistribution import (RedistributiveEconomy as E, stationary_gini,
                                          top_share, is_bounded, reachable_frontier)
T=1200
def row(**kw):
    r=E(**kw).run(T); return stationary_gini(r), r["kappa"], top_share(r), is_bounded(r)
print("MAIN TABLE  (N=800, mu=.05, sigma=.20, wage=.05, T=1200, stationary = mean of last quarter)")
print(f"{'levy':34s} {'Gini':>6s} {'kappa':>7s} {'top10%':>7s}  bounded")
g,k,t,b = row(); print(f"{'none (unopposed)':34s} {g:6.3f} {k:7.4f} {t:7.3f}  {b}")
for base in ("stock","flow"):
    for r in (0.01,0.025,0.05,0.10,0.25,0.50,1.00):
        g,k,t,b = row(base=base, rate=r)
        print(f"{base+' r='+format(r,'.3f'):34s} {g:6.3f} {k:7.4f} {t:7.3f}  {b}")
print("\nREALISATION (flow base at the MAXIMUM possible rate, 1.00)")
for rho in (1.0,0.75,0.50,0.25,0.10,0.0):
    g,k,t,b = row(base="flow", rate=1.0, realization=rho)
    print(f"  rho={rho:4.2f}  Gini={g:.3f}  kappa={k:.4f}  top10%={t:.3f}  bounded={b}")
print("\nREACHABLE FRONTIER (min stationary Gini over rate in (0,1])")
print(f"  stock                 {reachable_frontier('stock', periods=T):.3f}")
print(f"  flow, rho=1.00        {reachable_frontier('flow', periods=T):.3f}")
print(f"  flow, rho=0.25        {reachable_frontier('flow', realization=0.25, periods=T):.3f}")
print(f"  flow, rho=0.00        {reachable_frontier('flow', realization=0.0, periods=T):.3f}")
print("\nTHRESHOLD (stock r=0.025, threshold in multiples of the mean of the base)")
for th in (0.0,0.25,0.5,1.0,2.0,5.0,20.0):
    g,k,t,b = row(base="stock", rate=0.025, threshold=th)
    print(f"  thr={th:5.2f}x  Gini={g:.3f}  kappa={k:.4f}  bounded={b}")
print("\nPERIODICITY (stock, rate*P held constant at 0.02/period)")
for P in (1,2,4,10,20,30,50):
    g,k,t,b = row(base="stock", rate=min(1.0,0.02*P), periodicity=P)
    print(f"  every {P:3d} periods at r={min(1.0,0.02*P):.2f}  Gini={g:.3f}  bounded={b}")
