# Quantum amplifier

**Derivation step:** Generator: lawful change before readout
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

Quantum amplifier is an instrument-mediated readout role in the compact quantum constructor. In this tree, quantum amplifier belongs to the lawful-change step: it specifies how the state changes before a question is asked.

## Mechanism

Operationally, Quantum amplifier contributes an instrument-mediated readout role. The mechanism is an apparatus-coupled readout: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate. In the generators step, the generator is the part of the construction that makes the state move while preserving the admissibility conditions. In ordinary quantum mechanics this is usually a Hamiltonian or unitary map; in path-integral language it is an action weight over histories. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Quantum amplifier contributes an instrument-mediated readout role to the quantum construction.
- **Placement:** This page is read first as a lawful-transport move: it identifies what changes the state before readout.
- **Carrier or domain:** A probe state, sample state, field mode, detector state, or estimation register.
- **Operator or map:** An interaction Hamiltonian, transfer map, measurement channel, reconstruction map, or estimator.
- **Admissibility:** The instrument must separate sample signal from preparation, detector response, calibration, noise, and reconstruction artifacts.
- **Readout:** Counts, images, spectra, phase shifts, trajectories, intensity maps, correlation data, or parameter estimates.
- **Check:** The claimed mechanism is credible only when the same readout survives control experiments, calibration changes, and reconstruction checks.

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

- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537), score 0.581
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385), score 0.548
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682), score 0.535
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838), score 0.530
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598), score 0.527
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283), score 0.527
