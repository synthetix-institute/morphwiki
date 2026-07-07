# Measurement in quantum mechanics

**Derivation step:** Readout rule: how answers become probabilities
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

Measurement in quantum mechanics is the complete readout junction: it combines a state, a measurement model, probabilities, and sometimes an update rule.

## Mechanism

Measurement is not the root of quantum theory in this book. It is the junction where a prepared state and an observable or POVM are converted into probabilities and recorded outcomes. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Measurement in quantum mechanics contributes a probability/readout role to the quantum construction.
- **Placement:** This page is read first as a readout move: it connects the state and question to recorded outcomes.
- **Carrier or domain:** A state vector or density operator together with the measurement context in which outcome channels are defined.
- **Operator or map:** A projection-valued measure, POVM, update map, or instrument map connecting state to record.
- **Admissibility:** Outcome probabilities must be positive, normalized, and tied to a specified readout map rather than to informal observer language.
- **Readout:** Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.
- **Check:** The interpretation is constrained by whether it changes the probability rule, the update rule, the detector model, or only the language used for them.

## Topic Equations

Standard constructor skeleton: generalized measurement probability and conditional update.

```math
p(i)=\operatorname{Tr}(\rho E_i)
\rho\mapsto \rho_i=\frac{K_i\rho K_i^\dagger}{\operatorname{Tr}(K_i\rho K_i^\dagger)}
E_i=K_i^\dagger K_i
```

## What Remains Stable

- the rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation
- the operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels
- the dependence of admissible readout on measurement context or boundary condition
- the non-commuting compatibility structure, which survives changes of representation

## What Changes With Realization

- the name of the carrier: particle, wave, field, qubit, or excitation
- where time dependence is represented: on the state, on the operator, or in a path weight
- the coordinate system, basis, or geometric picture used to display the same relation
- the physical implementation of detector, boundary, preparation, or readout

## Validation Boundary

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385), score 0.579
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537), score 0.551
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823), score 0.544
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682), score 0.535
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159), score 0.535
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283), score 0.534
