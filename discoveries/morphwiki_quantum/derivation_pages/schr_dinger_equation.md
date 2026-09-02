# Schrödinger equation

**Physical domain:** Dynamics and transformations

## Mechanism

Schrödinger equation is the state-transport constructor: the Hamiltonian generates lawful change of the state before measurement.

The Schrodinger equation turns a Hamiltonian into a local rule for the time dependence of a state. It is the point at which the chosen state space, boundary conditions, and interaction model become a calculable prediction.

The Schrödinger equation is not a measurement rule. It is the generator step of the quantum constructor. It evolves the predictive carrier while preserving normalization when the Hamiltonian is self-adjoint.

## Physical Construction

The state carrier is a state vector, density operator, wavefunction, field state, or register on a specified domain. The governing operation is Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state. Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. The calculated observables are Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: Hamiltonian transport and norm preservation.

```math
i\hbar\,\partial_t\ket{\psi(t)}=H\ket{\psi(t)}
\ket{\psi(t)}=U(t)\ket{\psi(0)},\qquad U(t)=e^{-iHt/\hbar}
\frac{d}{dt}\langle\psi(t)|\psi(t)\rangle=0\quad (H=H^\dagger)
```

## Physical Meaning

The time derivative of the state is fixed by the Hamiltonian acting on that state. For a self-adjoint Hamiltonian, the equation preserves norm. Stationary solutions separate time dependence from the spatial eigenvalue problem, but a general preparation is their superposition.

A wave packet in a potential well spreads and interferes according to the same equation whose stationary solutions define the well's energy levels.

Observables determine which consequences of the evolved state are compared with experiment.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:quant-ph/0211042](https://arxiv.org/abs/quant-ph/0211042)
- [arXiv:quant-ph0211042](https://arxiv.org/abs/quant-ph0211042)
- [arXiv:quant-ph/0606183](https://arxiv.org/abs/quant-ph/0606183)
- [arXiv:quant-ph0606183](https://arxiv.org/abs/quant-ph0606183)
