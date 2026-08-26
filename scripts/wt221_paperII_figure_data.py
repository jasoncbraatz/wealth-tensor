import json, numpy as np, sys
sys.path.insert(0,'src')
from wealth_tensor.redistribution import (RedistributiveEconomy, stationary_gini,
                                          top_share, is_bounded)
T=1200
def run(**kw):
    m=RedistributiveEconomy(n_agents=800,growth_mean=0.05,growth_sd=0.20,wage=0.05,seed=0,**kw)
    r=m.run(periods=T)
    return dict(gini=stationary_gini(r),kappa=r['kappa'],top=top_share(r),bounded=bool(is_bounded(r)))
out={}
# F1: frontier in kappa for both bases
rates=[0.01,0.025,0.05,0.1,0.25,0.5,0.75,1.0]
for base in ('stock','flow'):
    rows=[]
    for r in rates:
        try: rows.append(dict(rate=r,**run(base=base,rate=r)))
        except Exception as e: rows.append(dict(rate=r,err=str(e)))
    out['frontier_'+base]=rows
out['none']=run(base='stock',rate=0.0)
# F2: realisation sweep, flow base, confiscatory rate
rhos=[0.0,0.05,0.1,0.15,0.25,0.4,0.55,0.7,0.85,1.0]
out['rho']=[dict(rho=p,**run(base='flow',rate=1.0,realization=p)) for p in rhos]
print(json.dumps(out,indent=1))

# Provenance: written for paper-II v1.0 (2026-08-26) to produce the seven new realisation
# rows in §3.2 and the plotted values behind Figures 1-3. Imports the committed model
# unchanged; seed 0, T = 1200, the parameter neighbourhood of §2.1.
