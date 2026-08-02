# Hamiltonian (quantum mechanics)

**Derivation step:** Generator: lawful change before measurement

## Topic Context

In quantum mechanics, the Hamiltonian of a system is an operator corresponding to the total energy of that system, including both kinetic energy and potential energy. Its spectrum, the system's energy spectrum or its set of energy eigenvalues, is the set of possible outcomes obtainable from a measurement of the system's total energy. Due to its close relation to the energy spectrum and time-evolution of a system, it is of fundamental importance in most formulations of quantum theory.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics))

## Role In The Derivation

Hamiltonian (quantum mechanics) is the generator observable: it both transports states and supplies the energy spectrum.

## Why This Step Is Needed

The Hamiltonian specifies both the energy observable and, for a closed system, the generator of time translation. These roles coincide but should not be confused: one concerns possible energy values, the other the path followed by every prepared state.

## Mechanism

The Hamiltonian has a dual role. Dynamically, it generates unitary time evolution. Spectrally, its eigenvalues are admissible energy observables. This dual role is one reason the operator/spectrum branch is central.

## How It Enters The Theory

**Place in the construction.** Hamiltonian (quantum mechanics) contributes a lawful state-transport role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wavefunction, field state, or register on a specified domain. Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: energy spectrum and unitary generation.

```math
H\ket{E_n}=E_n\ket{E_n}
U(t)=e^{-iHt/\hbar}
\rho(t)=U(t)\rho(0)U(t)^\dagger
```

## How To Read The Relation

Exponentiating a self-adjoint Hamiltonian produces the unitary propagator. Its eigenvectors acquire phases at rates set by their energies; relative phases then produce interference and motion. Time dependence or external driving requires a time-ordered propagator.

## Worked Example

For a particle in a static potential, kinetic and potential terms determine both stationary energy levels and the evolution of a wave packet assembled from those levels.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

The Schrodinger equation gives the differential form of this evolution, while path integrals and the Heisenberg picture reorganize the same predictions.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0908.0752](https://arxiv.org/abs/0908.0752)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
