# Path integral

**Derivation step:** Generator: lawful change before measurement

## Topic Context

Path integral may refer to:Line integral, the integral of a function along a curve Contour integral, the integral of a complex function along a curve used in complex analysis Functional integration, the integral of a functional over a space of curves Path integral formulation, Richard Feynman's formulation of quantum mechanics using functional integration

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Path_integral)

## Role In The Derivation

Path integral is an alternate generator constructor: transition amplitudes are obtained by summing phase weights over histories.

## Why This Step Is Needed

Path integral separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

The path integral does not replace the operator constructor. It repackages the generator step as a weighted sum over histories between boundary conditions. It is especially useful when action, symmetry, and field degrees of freedom are more natural than state-vector evolution.

## How It Enters The Theory

**Place in the construction.** Path integral contributes a lawful state-transport role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wavefunction, field state, or register on a specified domain. Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: boundary-to-boundary transition amplitude through action weights.

```math
K(x_f,t_f;x_i,t_i)=\int_{x_i}^{x_f}\mathcal D x(t)\,\exp\!\left(\frac{i}{\hbar}S[x]\right)
\psi(x_f,t_f)=\int K(x_f,t_f;x_i,t_i)\psi(x_i,t_i)\,dx_i
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

- [arXiv:2107.01923](https://arxiv.org/abs/2107.01923)
- [arXiv:0801.3568](https://arxiv.org/abs/0801.3568)
- [arXiv:2105.11733](https://arxiv.org/abs/2105.11733)
- [arXiv:1706.07300](https://arxiv.org/abs/1706.07300)
- [arXiv:cond-mat0108470](https://arxiv.org/abs/cond-mat/0108470)
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
