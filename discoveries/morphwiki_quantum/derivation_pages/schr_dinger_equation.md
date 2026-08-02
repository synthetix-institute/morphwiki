# Schrödinger equation

**Derivation step:** Generator: lawful change before measurement

## Topic Context

The Schrödinger equation is a partial differential equation that governs the wave function of a non-relativistic quantum-mechanical system. Its discovery was a significant landmark in the development of quantum mechanics. It is named after Erwin Schrödinger, an Austrian physicist, who postulated the equation in 1925 and published it in 1926, forming the basis for the work that resulted in his Nobel Prize in Physics in 1933.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation)

## Role In The Derivation

Schrödinger equation is the state-transport constructor: the Hamiltonian generates lawful change of the state before measurement.

## Why This Step Is Needed

The Schrodinger equation turns a Hamiltonian into a local rule for the time dependence of a state. It is the point at which the chosen state space, boundary conditions, and interaction model become a calculable prediction.

## Mechanism

The Schrödinger equation is not a measurement rule. It is the generator step of the quantum constructor. It evolves the predictive carrier while preserving normalization when the Hamiltonian is self-adjoint.

## How It Enters The Theory

**Place in the construction.** Schrödinger equation contributes a lawful state-transport role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wavefunction, field state, or register on a specified domain. Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: Hamiltonian transport and norm preservation.

```math
i\hbar\,\partial_t\ket{\psi(t)}=H\ket{\psi(t)}
\ket{\psi(t)}=U(t)\ket{\psi(0)},\qquad U(t)=e^{-iHt/\hbar}
\frac{d}{dt}\langle\psi(t)|\psi(t)\rangle=0\quad (H=H^\dagger)
```

## How To Read The Relation

The time derivative of the state is fixed by the Hamiltonian acting on that state. For a self-adjoint Hamiltonian, the equation preserves norm. Stationary solutions separate time dependence from the spatial eigenvalue problem, but a general preparation is their superposition.

## Worked Example

A wave packet in a potential well spreads and interferes according to the same equation whose stationary solutions define the well's energy levels.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Observables determine which consequences of the evolved state are compared with experiment.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
