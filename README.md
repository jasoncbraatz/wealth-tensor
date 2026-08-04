# wealth-tensor

Executable mathematical models for a thermodynamic–financial theory of wealth.

Every equation in the companion manuscript should exist here twice: once as a symbol,
once as code that runs. If a model cannot be executed, it is a claim, not a result.

## Why this repo is public

Git commit timestamps are a priority record. Preprint culture in econophysics and
heterodox macro is open by default (arXiv, RePEc, EconStor), and reproducible code is
increasingly a precondition for review rather than a bonus. Secrecy would cost feedback
and buy almost nothing.

## The open problem: dimensional grounding of Lambda

The atomic unit is a dual tensor `W_i(t) = [ E_i(t), C_i(t), L_i(t) ]`:

- `E_i` — biophysical vector, in physical units (J, m^2, kg)
- `C_i` — financial claim vector, in units of account (currency)
- `L_i` — transformation efficiency vector

`L_i` has two components. The first, `eta_exergy_to_work`, is dimensionless (J/J),
bounded above by Carnot, and uncontroversial.

The second, `eta_work_to_financial`, maps joules to currency. Its dimensions are
`[currency] / [J]`. **That is a price.** Any reviewer will say so immediately, and will
then observe that a free scalar which converts physics into money can be tuned to fit
any dataset. This is the same rock that sank Odum's emergy program and, in a different
century, the labour theory of value's transformation problem.

Treating that coefficient as a structural constant is not defensible. The working
position of this repo is that it must instead be:

1. **Measured, not assumed** — it is the reciprocal of energy intensity of output, a
   quantity national statistical agencies have published for decades.
2. **A dependent variable, not a parameter** — its drift and variance are the object of
   study, not a nuisance to be calibrated away.
3. **Stress-tested** — conclusions must be shown invariant across a wide range of it, or
   they are artefacts of the fit.

Item 3 is the reason this repo exists.

## Layout

- `src/wealth_tensor/` — model implementations
- `tests/` — every model checked against a closed form or a published result
- `docs/` — derivations, notes, decisions

## Status

Early. Nothing here is settled.
