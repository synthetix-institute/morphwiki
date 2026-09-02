# Particle in a box

**Physical domain:** Boundaries and operator domains

## Mechanism

Particle in a box is a boundary-spectrum constructor: a spatial domain and boundary condition discretize the allowed energy spectrum.

The particle in a box shows in the simplest form that a boundary condition is part of the Hamiltonian's physical definition. Confinement turns a continuous free-particle spectrum into discrete allowed energies.

The page shows how a boundary condition changes the domain of the Hamiltonian and therefore the allowed spectra.

## Physical Construction

The state carrier is Fock space, field configuration space, or a sector selected by charge, spin, momentum, statistics, or gauge data. The governing operation is Creation, annihilation, field, charge, spin, Hamiltonian, or scattering operators acting on the admissible sector. Statistics, gauge constraints, commutation or anticommutation rules, domain conditions, and sector labels decide which states are legal. The calculated observables are Occupation number, charge, spin, momentum, energy, correlation function, cross-section, or scattering amplitude.

## Topic Equations

Standard constructor skeleton: boundary condition and discrete spectrum.

```math
\psi(0)=\psi(L)=0
\psi_n(x)=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L}
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}
```

## Physical Meaning

The wave function satisfies the same differential equation inside the box as a free particle, but vanishing boundary values select standing waves. Only wavelengths fitting the interval are admissible, and their curvature fixes the quantized energies.

Doubling the box length reduces every level spacing by a factor of four. This follows from the boundary-selected wavelength and provides a direct check of the construction.

Replacing an impenetrable wall by a finite barrier leads to tunnelling, resonances, and scattering channels.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:2103.01715](https://arxiv.org/abs/2103.01715)
