# Quantum circuit

**Derivation step:** Protocol layer: engineered transformations
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

Quantum circuit is the engineered-composition constructor: a finite sequence of admissible maps prepares, transforms, and measures a register.

## Mechanism

A circuit is the protocol layer of the same state-operator-readout machinery. Gates are controlled unitary or channel maps; measurement converts final states into output probabilities. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Quantum circuit contributes an engineered operation-sequence role to the quantum construction.
- **Placement:** This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.
- **Carrier or domain:** An input state, register, channel state, error syndrome, key, or controlled experimental configuration.
- **Operator or map:** An ordered sequence of gates, channels, measurements, corrections, encodings, or conditional maps.
- **Admissibility:** Each step must belong to the claimed map class: unitary, completely positive, trace-preserving, projective, conditional, or corrective.
- **Readout:** Output state, key, error rate, fidelity, channel capacity, algorithmic success probability, or sensor estimate.
- **Check:** Changing operation order, inserting classical controls, or replacing a quantum channel should identify which step carries the effect.

## Topic Equations

```math
B \longmapsto \rho_B \quad \text{(context specifies an admissible state)}
\rho_t = U_t \rho_B U_t^\dagger \quad \text{(unitary evolution from preparation to readout)}
O = \sum_i \lambda_i P_i,\quad p_i=\operatorname{Tr}(P_i\rho_t) \quad \text{(spectral probability measure)}
[O_1,O_2]\neq 0 \quad \text{(incompatible observables: no common sharp basis)}
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

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385), score 0.552
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823), score 0.551
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682), score 0.537
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838), score 0.532
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159), score 0.530
- [arXiv:0805.4565](https://arxiv.org/abs/0805.4565), score 0.529
