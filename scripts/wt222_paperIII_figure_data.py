import json, math
import numpy as np

E0=100.0
def sim(alpha,delta,phi,T=400,E0=E0,g0=0.0):
    E=np.empty(T+1); C=np.empty(T+1)
    E[0]=E0; C[0]=E0-g0*E0
    for t in range(T):
        dE=-delta*E[t]
        gap=E[t]-C[t]
        E[t+1]=E[t]+dE
        C[t+1]=C[t]+phi*dE+alpha*gap
    return E,C

out={}

# F1 -- the mirror pair
a,d,p = 0.05, 0.02, 0.60
ap,dp = d,a
pp = p*d/a
E1,C1 = sim(a,d,p)
E2,C2 = sim(ap,dp,pp)
maxdev = float(np.max(np.abs(C1-C2)))
out['F1']={'alpha':a,'delta':d,'phi':p,'alpha_m':ap,'delta_m':dp,'phi_m':pp,
  'maxdev':maxdev,
  't':list(range(0,401,4)),
  'C':[round(float(x),6) for x in C1[::4]],
  'Cm':[round(float(x),6) for x in C2[::4]],
  'E':[round(float(x),6) for x in E1[::4]],
  'Em':[round(float(x),6) for x in E2[::4]],
  'E_end':float(E1[-1]),'Em_end':float(E2[-1])}

# F3 -- the four GAAP tiers
tiers=[('Property, plant & equipment',0.80,0.030),
       ('Finite-lived intangibles',0.60,0.020),
       ('Indefinite-lived intangibles',0.40,0.010),
       ('Goodwill',0.20,0.002)]
alpha_cal=0.05; alpha_meas=0.408
def R(phi,delta,alpha): return (1-phi)*delta/(alpha-delta)
common_d=0.02
out['F3']={'tiers':[{'name':n,'phi':f,'delta':dd,
   'R_cal':round(R(f,dd,alpha_cal),4),
   'R_meas':round(R(f,dd,alpha_meas),4),
   'R_common':round(R(f,common_d,alpha_cal),4)} for n,f,dd in tiers],
   'alpha_cal':alpha_cal,'alpha_meas':alpha_meas,'common_delta':common_d}

# F4 -- validity boundary logistic
xs=np.linspace(-1.6,2.2,60)   # log(leverage/budget)
slope=1.58; x0=math.log(0.61)
out['F4']={'x':[round(float(math.exp(x)),4) for x in xs],
  'p':[round(float(1/(1+math.exp(-slope*(x-x0)))),4) for x in xs],
  'cross':0.61,'ladder':2.58,'slope':slope}

# F5 -- lag vs magnitude, recovery rates
out['F5']=[{'k':'δ common across classes','lag':100.0,'mag':100.0},
           {'k':'δ drawn independently','lag':66.2,'mag':11.5},
           {'k':"δ on the standards' falling ladder",'lag':100.0,'mag':1.9}]

# F6 -- the registered null
out['F6']={'pilot':{'sector':'Retail trade (SIC 5200–5999)','z':-0.290,'p':0.590,
   'tiers':[{'t':'PP&E','n':21,'med':5.0,'q1':3.0,'q3':9.0},
            {'t':'Finite-lived','n':34,'med':4.0,'q1':1.0,'q3':8.0},
            {'t':'Indefinite-lived','n':34,'med':5.5,'q1':1.2,'q3':9.0},
            {'t':'Goodwill','n':155,'med':5.0,'q1':1.0,'q3':9.0}]},
  'repl':{'sector':'Computer & data processing (SIC 7370–7379)','z':-0.095,'p':0.520,
   'tiers':[{'t':'PP&E','n':34,'med':5.0,'q1':1.2,'q3':9.8},
            {'t':'Finite-lived','n':102,'med':4.5,'q1':1.2,'q3':10.0},
            {'t':'Indefinite-lived','n':46,'med':6.0,'q1':2.2,'q3':11.0},
            {'t':'Goodwill','n':262,'med':5.0,'q1':1.0,'q3':10.0}]}}

print(json.dumps({k:(v if k!='F1' else {kk:vv for kk,vv in v.items() if kk not in('t','C','Cm','E','Em')}) for k,v in out.items()},indent=1)[:2000])
json.dump(out,open('figdata.json','w'))

# Provenance: written for paper-III v1.0 (2026-08-26). Produces the plotted values behind
# Figures 1-6. The mirror pair in F1 is simulated here directly from the two recursions;
# the cross-class, boundary, recovery-rate and registered-test values are the numbers the
# paper's own scripts (wt083, wt084, wt027) already publish, restated here for plotting.
