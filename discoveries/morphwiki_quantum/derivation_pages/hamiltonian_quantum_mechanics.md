# Hamiltonian (quantum mechanics)

**Physical domain:** Dynamics and transformations

## Mechanism

Hamiltonian (quantum mechanics) is the generator observable: it both transports states and supplies the energy spectrum.

The Hamiltonian specifies both the energy observable and, for a closed system, the generator of time translation. These roles coincide but should not be confused: one concerns possible energy values, the other the path followed by every prepared state.

The Hamiltonian has a dual role. Dynamically, it generates unitary time evolution. Spectrally, its eigenvalues are admissible energy observables. This dual role is one reason the operator/spectrum branch is central.

## Physical Construction

The state carrier is a state vector, density operator, wavefunction, field state, or register on a specified domain. The governing operation is Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state. Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. The calculated observables are Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: energy spectrum and unitary generation.

```math
H\ket{E_n}=E_n\ket{E_n}
U(t)=e^{-iHt/\hbar}
\rho(t)=U(t)\rho(0)U(t)^\dagger
```

## Physical Meaning

Exponentiating a self-adjoint Hamiltonian produces the unitary propagator. Its eigenvectors acquire phases at rates set by their energies; relative phases then produce interference and motion. Time dependence or external driving requires a time-ordered propagator.

For a particle in a static potential, kinetic and potential terms determine both stationary energy levels and the evolution of a wave packet assembled from those levels.

The Schrodinger equation gives the differential form of this evolution, while path integrals and the Heisenberg picture reorganize the same predictions.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.
