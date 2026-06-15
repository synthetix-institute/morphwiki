# Quantum Statement Sparse-Attention Audit

Statement: Operationally, quantum mechanics can be read as a rule that assigns probabilities to the spectrum of an observable.

Verdict: `partially_supported_with_boundaries`

## Joint Attention

Component means over the sparse top-k witnesses:
- `prepared_state`: `0.177124`
- `observable_operator`: `0.484402`
- `spectrum_readout`: `0.472317`
- `probability_assignment`: `0.19594`
- `measurement_context`: `0.40343`
- `noncommuting_compatibility`: `0.177656`

Route profile over sparse top-k witnesses:
- `transport_flow_route`: `0.0961`
- `constraint_closure_route`: `0.1246`
- `spectral_operator_route`: `0.4526`
- `boundary_weak_form_route`: `0.0426`
- `commutator_incompatibility_route`: `0.1046`
- `discrete_protocol_route`: `0.0186`

Fiber profile over sparse top-k witnesses:
- `structure`: `0.3472`
- `spectral`: `0.3472`
- `geometry`: `0.3055`
- `syntax`: `0.5858`
- `entropy`: `0.4142`

## Top Joint Witnesses
- `hyperion:EW000003340` attention=`0.050305` score=`0.404134` apparatus=`Α08` [2206.05302](https://arxiv.org/abs/2206.05302)
- `hyperion:EW000000594` attention=`0.046523` score=`0.373752` apparatus=`Α11` [1801.03283](https://arxiv.org/abs/1801.03283)
- `hyperion:EW000000009` attention=`0.046335` score=`0.37224` apparatus=`Α01` [quant-ph0610203](https://arxiv.org/abs/quant-ph/0610203)
- `hyperion:EW000000187` attention=`0.046285` score=`0.371839` apparatus=`Α07` [0809.2455](https://arxiv.org/abs/0809.2455)
- `hyperion:EW000003356` attention=`0.046195` score=`0.371114` apparatus=`Α08` [hep-th9909221](https://arxiv.org/abs/hep-th/9909221)
- `hyperion:EW000000019` attention=`0.044007` score=`0.353537` apparatus=`Α00` [1005.2682](https://arxiv.org/abs/1005.2682)
- `hyperion:EW000000134` attention=`0.043669` score=`0.350822` apparatus=`Α00` [cond-mat0412475](https://arxiv.org/abs/cond-mat/0412475)
- `hyperion:EW000002770` attention=`0.042774` score=`0.34363` apparatus=`Α03` [1612.00682](https://arxiv.org/abs/1612.00682)
- `hyperion:EW000000172` attention=`0.042188` score=`0.338921` apparatus=`Α07` [1711.02122](https://arxiv.org/abs/1711.02122)
- `hyperion:EW000003676` attention=`0.041784` score=`0.335676` apparatus=`Α08` [gr-qc9508045](https://arxiv.org/abs/gr-qc/9508045)

## Alternative Query Contrast
- `tested_statement`: mean top-k score `0.32781`
- `object_taxonomy`: mean top-k score `0.080132`
- `dynamics_only`: mean top-k score `0.408783`
- `spectrum_only`: mean top-k score `0.436962`

## Limitations
- Prepared-state/state-representation support is secondary in the selected public index.
- Probability/readout support is weak in the selected public index.
- Non-commuting compatibility support is present but sparse; do not make it the sole headline.

## Recommended Wording
Hyperion supports a more bounded wording: the ranked witnesses concentrate strongly on operator/spectral structure, with additional but weaker state, probability/readout, context, and non-commutation components.  The public sentence should say that quantum mechanics can be read operationally through prepared states, observables, spectra, and probabilities, not that Hyperion proves this is the whole theory.
