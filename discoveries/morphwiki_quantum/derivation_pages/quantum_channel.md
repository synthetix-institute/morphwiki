# Quantum channel

**Derivation step:** Protocol layer: engineered transformations
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

Quantum channel is the open-system protocol constructor: it maps input states to output states while preserving complete positivity and trace.

## Mechanism

A channel is the mechanism for noisy transformations, measurements with forgotten outcomes, and subsystem evolution. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Quantum channel contributes an engineered operation-sequence role to the quantum construction.
- **Placement:** This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.
- **Carrier or domain:** Input and output density operators, possibly on different Hilbert spaces or subsystem carriers.
- **Operator or map:** A completely positive trace-preserving map, often represented by Kraus operators or by a Stinespring dilation.
- **Admissibility:** Complete positivity and trace preservation are the legal conditions; non-trace-preserving maps require an explicitly conditioned outcome.
- **Readout:** Output state, final POVM probabilities, fidelity, capacity, error rate, or recovered subsystem statistics.
- **Check:** The channel claim requires a map that stays positive under extension by an untouched reference system and preserves total probability.

## Topic Equations

Standard constructor skeleton: completely positive trace-preserving map and readout.

```math
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger
\sum_aK_a^\dagger K_a=I
p(y)=\operatorname{Tr}(M_y\mathcal E(\rho))
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

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385), score 0.560
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537), score 0.555
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598), score 0.542
- [arXiv:0805.4565](https://arxiv.org/abs/0805.4565), score 0.542
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640), score 0.539
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159), score 0.538
