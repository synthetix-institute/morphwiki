# Path integral formulation

**Derivation step:** Generator: lawful change before measurement

## Topic Context

The path integral formulation is a description in quantum mechanics that generalizes the stationary action principle of classical mechanics. It replaces the classical notion of a single, unique classical trajectory for a system with a sum, or functional integral, over an infinity of quantum-mechanically possible trajectories to compute a quantum amplitude.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Path_integral_formulation)

## Role In The Derivation

Path integral formulation is the formulation in which the generator is represented by action-weighted histories.

## Why This Step Is Needed

Path integral formulation separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

This page belongs with lawful change because it changes how the transport step is calculated. The observable predictions remain probabilities after amplitudes are composed and squared or traced.

## How It Enters The Theory

**Place in the construction.** Path integral formulation contributes a lawful state-transport role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wavefunction, field state, or register on a specified domain. Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: transition amplitudes and generating functional.

```math
\langle q_f,t_f|q_i,t_i\rangle=\int\mathcal Dq\,e^{iS[q]/\hbar}
Z[J]=\int\mathcal D\phi\,\exp\!\left(\frac{i}{\hbar}(S[\phi]+\int J\phi)\right)
```

## How To Read The Relation

The displayed relation should be read as a rule for transporting a state, not as a second definition of the state. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

A generator predicts a new state but not yet an experimental number. The next step selects an observable, whose spectrum and expectation values expose consequences of the dynamics.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
