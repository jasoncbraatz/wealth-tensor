import subprocess, re, json, pathlib, os
R = pathlib.Path.home()/"repos/wealth-tensor"
os.chdir(R)
def run(s): return subprocess.check_output(["python3","scripts/"+s],text=True)

o=run("wt084_identification_closed_form.py")
print("E1|", {k:(k in o) for k in ("A^t coefficient equation residual","D^t coefficient equation residual","a factor of 1.67 in the UNOBSERVED physical scale","0.513158","2.220e-16","3.308e-01")}, "31.7 absent:", ("31.7" not in o and "0.317" not in o))

o=run("wt083_tier_ladder_antialignment.py")
print("E2|", {k:(k in o) for k in ("phi   1-phi   delta   (1-phi)d      R sim   R closed","Kendall tau (registered rank vs observable), assumed ladder : +1.00","Kendall tau (registered rank vs observable), real ladder    : -1.00","dlog(1-phi)   dlog(delta)")})

o=run("wt088_disclosed_ladder.py")
print("E3|", {k:(k in o) for k in ("delta_3*                      = 0.007895","ORDERED (WT-083)       UNORDERED","lag non-decreasing up the ladder, ORDERED delta   : 100.0%","lag non-decreasing up the ladder, UNORDERED delta : 69.0%","PRECISION CHECK, same estimator at M = 2000                       : 66.2%","admissible share")})

o=run("wt085_returns_conditioning.py")
print("E4|", {k:(k in o) for k in ("E2 - returns break the root swap","E3 - the scale continuum survives returns entirely")})

o=run("wt086_exponent_robustness.py")
rows=[l for l in o.split("\n") if re.match(r"^  \S.*  -?\d\.\d{3}  ",l)]
print("E5|", "regime rows:", len([l for l in o.split("\n") if re.search(r"^  [A-Za-z].*\s0\.\d{3}\s+0\.\d{3}\s+-?\d\.\d{3}\s+-?\d\.\d{3}",l)]), "| p_cond/p_se header:", "p_cond    p_se" in o)

o=run("wt087_goodwill_gradient.py")
print("E6|", {k:(k in o) for k in ("0.032   0.002     0.163","0.060   0.030    -0.386","fitted: se ~ (alpha-delta)^-0.700     spread 6.81x")})

o=run("wt090_age_dependent_alpha.py")
print("E7|", {k:(k in o) for k in ("the naive form's pole sits at delta_a = 0.4350","naive overstates by    0.55%","naive overstates by   43.87%","alpha_eff 0.133716/q = 0.4368/yr","alpha_eff 0.149091/q = 0.4758/yr","delta3* = 0.00755/yr","delta3* = 0.00754/yr","reproduces §4.4's published 0.00789".replace("§4.4's","section 4.4's") if False else "0.00789")})

p1 = "docs/papers/paper-I-price-formation/paper-I.md"
c = subprocess.run(f"LC_ALL=C.UTF-8 wc -w {p1}",shell=True,capture_output=True,text=True).stdout.split()[0]
c2 = subprocess.run(f"LC_ALL=C wc -w {p1}",shell=True,capture_output=True,text=True).stdout.split()[0]
head = pathlib.Path(p1).read_text().split("\n")[:14]
print("E8|", "exists:", pathlib.Path(p1).exists(), "| C.UTF-8:", c, "| C(darwin):", c2,
      "| superseded banner:", any("SUPERSEDED" in l.upper() for l in head))
